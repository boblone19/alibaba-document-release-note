---
title: "Alibaba Cloud Apsara Stack Enterprise V3.18.1 Alibaba Cloud Security-Situation Awareness Cloud Security Management Center Developer Guide 20250612"
product_version: "V3.18.1"
doc_version: "20250612"
pdf_pages: 309
source_pdf: "Alibaba Cloud Apsara Stack Enterprise V3.18.1 Alibaba Cloud Security-Situation Awareness Cloud Security Management Center Developer Guide 20250612.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/3.18.1%E7%89%88%E6%9C%AC%E6%96%87%E6%A1%A3/%E6%80%81%E5%8A%BF%E6%84%9F%E7%9F%A5/Alibaba%20Cloud%20Apsara%20Stack%20Enterprise%20V3.18.1%20Alibaba%20Cloud%20Security-Situation%20Awareness%20Cloud%20Security%20Management%20Center%20Developer%20Guide%2020250612.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes+edge-junk)
---

# Alibaba Cloud Apsara Stack Enterprise V3.18.1 Alibaba Cloud Security-Situation Awareness Cloud Security Management Center Developer Guide 20250612

## Table of Contents

- 1 Preparations
  - 1.1 Log on to the API Tool console
  - 1.2 View the information about an operation
  - 1.3 Obtain an AccessKey pair
  - 1.4 Obtain an AccessKey pair assigned by STS
  - 1.5 Obtain an endpoint
- 2 Call examples
  - 2.1 Call examples for SDK for Java
    - 2.1.1 Quick start
    - 2.1.2 Use SDK
      - 2.1.2.1 Install SDK for Java
      - 2.1.2.2 Use CommonRequest to call API operations
  - 2.2 Call examples for SDK for Python
    - 2.2.1 Quick start
    - 2.2.2 Use SDK
      - 2.2.2.1 Install SDK for Python
      - 2.2.2.2 Use CommonRequest to call API operations
  - 2.3 Call examples for SDK for Go
    - 2.3.1 Quick start
    - 2.3.2 Use SDK
      - 2.3.2.1 Install Go SDK
      - 2.3.2.2 Use CommonRequest to call API operations
- 3 Common parameters
- 4 Security Operations Center
  - 4.1 Request method
    - 4.1.1 Request syntax
    - 4.1.2 Sign API requests
    - 4.1.3 Common parameters
    - 4.1.4 Response structure
  - 4.2 Operations
    - 4.2.1 DescribeAttacks
    - 4.2.2 DescribeAlarms
    - 4.2.3 DescribeVulFrangs
    - 4.2.4 DescribeHcFrangs
  - 4.3 SOAR
    - 4.3.1 Playbooks
      - 4.3.1.1 ModifyPlaybook
      - 4.3.1.2 TriggerPlaybook
      - 4.3.1.3 PublishPlaybook
      - 4.3.1.4 StopOneAction
      - 4.3.1.5 DescribePlaybook
      - 4.3.1.6 DescribeSoarRecords
    - 4.3.2 Intelligence
      - 4.3.2.1 SyncBanRecord
    - 4.3.3 Cases
      - 4.3.3.1 CreateEventByAlert
    - 4.3.4 Tasks
      - 4.3.4.1 DescribeManualTaskInfo
  - 4.4 Operations Center
    - 4.4.1 QueryThreats
    - 4.4.2 QueryThreatChartData
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

### 1.2 View the information about an operation

**operation**

When you use a service SDK to call an operation of the service, you must obtain the service name, operation name, and API version. This topic describes how to view the information about an operation.

**Background information**

The operations on the API Directory page are for reference only. For information about how to call operations, see API references of the corresponding services. If the information on the API Directory page is inconsistent with that in the API reference of the corresponding service, the information in the API reference takes precedence.

**Procedure**

1. Log on to the API Tool console.
2. In the left-side navigation pane, click **API Directory**.
3. On the **API Directory** page, select the required service from the drop-down list, enter a
keyword of an operation name in the search box, and then click Search.
4. View and record the service name, operation name, and API version.

### 1.3 Obtain an AccessKey pair

AccessKey pairs are classified into AccessKey pairs assigned by Resource Access Management (RAM) and AccessKey pairs assigned by Security Token Service (STS). You can use either type of AccessKey pair for authentication when you call operations. This topic describes how to obtain an AccessKey pair that is assigned by RAM.

**Background information**

An AccessKey pair is used to verify the identity of request senders. An AccessKey pair consists of an AccessKey ID and an AccessKey secret that are used to implement symmetric encryption. The AccessKey ID is used to identify a user. The AccessKey secret is used to encrypt the signature string. You can use RAM or STS to assign an AccessKey pair for authentication. Use RAM to assign an AccessKey ID and an AccessKey secret to a third party. Use STS to assign an AccessKey ID, an AccessKey secret, and a security token to a third party. For more information, see Obtain an STS AccessKey pair. The Apsara Uni-manager Management Console provides AccessKey pairs for personal accounts or organizations. Only the administrators of level-1 organizations and operations administrators can obtain the AccessKey pairs of organizations. We recommend that you use the AccessKey pairs of personal accounts to call the operations provided by the Apsara Unimanager Management Console and cloud services. If you use the AccessKey pair of a personal account, you must add the following parameters in request headers for access control. If you do not add the parameters, an error may occur. The error indicates that permissions are insufficient.

> **Warning:** The AccessKey pair of a personal account is managed by the permission system of the Apsara Uni-manager Management Console. The AccessKey pair of an organization has more permissions than the AccessKey pair of a personal account. If you want to obtain the AccessKey pair of an organization, make sure that you are authorized by an administrator. This helps ensure security.

| Parameter | Description |
|---|---|
| x-acs-regionid | The ID of the region. Example: cn-hangzhou-*. |
| x-acs-organizationid | The ID of the organization in the Apsara Uni- manager Management Console. For more information about how to obtain organization IDs, see the GetOrganizationList section in Apsara Uni-manager Management Console Developer Guide. |
| x-acs-resourcegroupid | The ID of the resource set in the Apsara Uni- manager Management Console. For more information about how to obtain resource set IDs, see the ListResourceGroup section in Apsara Uni-manager Management Console Developer Guide. |
| x-acs-instanceid | The ID of the instance on which you want to perform operations. For example, you can obtain the ID of an Elastic Compute Service (ECS) instance from the ECS instance list. |

**Obtain the AccessKey pair of a personal account**

To obtain the AccessKey pair of a personal account, perform the following operations:
1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the homepage, move the pointer over the profile picture and
click **User Information**.
3. In the **AccessKey Pair** section, view the AccessKey pair of your account.

> **Note:** An AccessKey pair consists of an AccessKey ID and an AccessKey secret. These credentials provide full permissions on cloud resources within your account. You must keep the AccessKey pair confidential.

**Obtain the AccessKey pair of an organization**

To obtain the AccessKey pair of an organization, perform the following operations:
1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, click **Enterprise**.
3. In the left-side navigation pane, choose **Resources > Organizations**.
4. In the organization list, click the name of the level-1 organization whose AccessKey pair you
want to obtain.
5. Click **Management Accesskey**.
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

1. Log on to the Apsara Infrastructure Management console. For more information, see
**Getting Started > Log on to the Apsara Uni-manager Operations Console** in
**Apsara Uni-manager Management Console User Guide** .
2. In the top navigation bar, choose **Products > Infrastructure Management**.
3. In the left-side navigation pane, click **Product & Cluster O&M**.
4. On the page that appears, enter yundun-advance in the **Product | Cluster** search box. In
the list that appear, find BasicThinCluster and click **Cluster Details** in the **Actions** column.
5. On the **Desired State Configuration** tab of the page that appears, search for the **kv.conf**
file and open it. Find the **region** and **internet-domain** parameters in the file.
6. Obtain the value of the **EndpointPre** parameter. For more information, see Common
parameters.
7. Obtain the endpoint based on the **region**, **internet-domain**, and **EndpointPre**
parameters. The endpoint of a cloud service is in the following format:

```
${EndpointPre}.${global:region}.${global:internet-domain}
```

**What to do next**

If you want to call the API operations of Apsara Stack Security services from the service domain or O&M domain, you must configure the hosts file on your computer.
1. Obtain the virtual IP address (VIP) of the POP.
i. In the left-side navigation pane, click **Product & Cluster O&M**. ii. On the page that appears, enter webappAll in the **Product | Cluster** search box. In the list that appear, find StandardCloudCluster and click **Cluster Details** in the **Actions** column. iii. On the **Resource Details** tab of the page that appears, find the O&M domain **pop-vip-**
**ops**, management domain **pop-vip-mgmt**, and business domain **pop-vip-biz**, and then
click the icon in the **Resource Application Result** column to obtain the value of the vip_ip parameter.
2. Configure the following hosts file on your local computer.

```xml
<vip_ip> <Endpoint of the API operation that you want to request>
```

s

## 2 Call examples

### 2.1 Call examples for SDK for Java

#### 2.1.1 Quick start

This topic describes how to obtain and use Apsara Stack SDK for Java.

**Prerequisites**

An Apsara Stack tenant account that has the required permissions and an AccessKey pair that consists of an AccessKey ID and an AccessKey secret are obtained before you can use Apsara Stack SDK for Java. You can view and obtain your AccessKey pair in the Apsara Unimanager Management Console. For more information, see Obtain an AccessKey pair. For more information about how to obtain the endpoint, see Obtain an endpoint. Java Development Kit (JDK) 1.8 or later is installed before you can use Apsara Stack SDK for Java.

**Installation**

If you use Apache Maven to manage a Java project, you need to only import the JAR file of Apsara Stack SDK for Java to the pom.xml file of the project. If you want to use Apsara Stack Security SDK for Java, you must install the core library of Apsara Stack SDK for Java. We recommend that you use V4.5.17 or later of the core library.

**Usage**

To use Apsara Stack SDK for Java, perform the following steps:
1. Create a DefaultAcsClient instance and initialize the instance.
2. Create an API request and configure the required parameters.
3. Initiate the API request and process the response or exception.

> **Note:** In the following code, replace the variables with actual values. Delete the angle brackets <> in the final code.
> The following section describes the variables:
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

##### 2.1.2.2 Use CommonRequest to call API operations

> **Note:** If you want to call the API operations of a service that does not provide SDKs, you can use CommonRequest. You can use CommonRequest to call API operations.

**Benefits**

CommonRequest provides the following benefits:
1. Lightweight: You need to only download the core package. You do not need to download
and install SDKs of services.
2. Easy to use: You can call the newly released API operations of a service without the need to
update the SDK for the service.
3. Fast iteration.

**Use CommonRequest to call an API operation**

Apsara Stack services provide RPC and RESTful APIs. The request method of CommonRequest varies based on the style of the API that you want to call. In most cases, an API uses the RPC style if the API operations include the Action parameter. An API uses the RESTful style if the API operations include the PathPattern parameter. All API operations of a service use the same API style. The API of each service supports only one style. If you pass an invalid identifier, another API operation may be called, or the `ApiNotFound` error is returned. If you want to send a CommonRequest request, you must obtain the values of the following parameters. For more information about the values of these parameters, see the API reference in DocumentationDocumentation. You can also visit OpenAPI Explorer to obtain the parameter values of API operations for some services. Endpoint: the endpoint of a service. Version: the version of the API. The version is in the YYYY-MM-DD format. Operation information: the name of the API operation that you want to call. The APIs of most Apsara Stack services, such as Threat Detection Service, are RPC APIs. If you want to call an RPC API operation, you must obtain the value of the Action parameter, and then specify the value in the `request.ApiName = "<Action>"` format. If you want to call a RESTful API operation of a service, such as Container Service for Kubernetes (ACK), you must obtain the value of the PathPattern parameter, and then specify the RESTful path in the `request.PathPattern = "<PathPattern>"` format.

**Example: Call an RPC API operation**

The following sample code shows how to use CommonRequest to call an API operation of Apsara Stack Security: s

```java
import com.aliyuncs.CommonRequest; import com.aliyuncs.CommonResponse; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.exceptions.ServerException; import com.aliyuncs.profile.DefaultProfile; public class Sample {
    public static void main(String[] args) {
        // Create a DefaultAcsClient instance and initialize the instance.
        DefaultProfile profile = DefaultProfile.getProfile(
            "<your-region-id>",          // The ID of the region.
            "<your-access-key-id>",      // The AccessKey ID.
            "<your-access-key-secret>"); // The AccessKey secret.
        IAcsClient client = new DefaultAcsClient(profile);
        // Create an API request and specify parameters.
        CommonRequest request = new CommonRequest();
        request.setDomain("<your-endpoint>");// The endpoint of the service.
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

### 2.2 Call examples for SDK for Python

**Python**

#### 2.2.1 Quick start

This topic describes how to obtain and use the SDK for Python.

**Prerequisites**

An authorized account and an AccessKey pair (AccessKey ID and AccessKey secret) are obtained. For more information, see Obtain an AccessKey pair. The endpoint of a service is obtained. For more information, see Obtain an endpoint.

**Install the core library of the SDK for Python**

If you use Python 2.x, run the following command: s

```
pip install aliyun-python-sdk-core
```

If you use Python 3.x, run the following command:

```
pip3 install aliyun-python-sdk-core-v3
```

**Use the SDK for Python**

To use the SDK for Python, perform the following steps:
1. Create a client instance.
When you create a client instance, you must obtain a region ID, AccessKey ID, and AccessKey secret.
2. Create an API request and specify the required parameters.
3. Initiate the API request and process the response or exception.

> **Note:** In the following code, replace the variables with actual values. Delete the angle brackets <> in the final code.
> The following section describes the variables:
> <your_region_id>: Replace the value of this parameter with the region ID.
> <your_access_key_id>: Replace the the value of this parameter with your AccessKey ID.
> <your_access_key_secret>: Replace the value of this parameter with your AccessKey secret.
> <your-endpoint>: Replace the value of this parameter with the endpoint of the service.
> <API-version>: Replace the value of this parameter with the version of the API.
> <your-action>: Replace the value of this parameter with the name of the API operation.

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

##### 2.2.2.2 Use CommonRequest to call API operations

> **Note:** If you want to call the API operations of an Apsara Stack service that does not provide SDKs, you can use CommonRequest. You can use CommonRequest to call API operations.

**Benefits**

CommonRequest provides the following benefits:
1. Lightweight: You need only to download the core package. You do not need to download
and install SDKs of Apsara Stack services.
2. Easy to use: You can call the newly released API operations of an Apsara Stack service
without the need to update the SDK for the service.
3. Fast iteration.

**Use CommonRequest to call an API operation**

Apsara Stack services provide RPC and RESTful APIs. The request method of CommonRequest varies based on the style of the API that you want to call. In most cases, an API uses the RPC style if the API operations include the Action parameter. An API uses the RESTful style if the API operations include the PathPattern parameter. All API operations of a service use the same API style. The API of each service supports only one style. If you pass an invalid identifier, another API operation may be called, or the `ApiNotFound` error is returned. If you want to send a CommonRequest request, you must obtain the values of the following parameters. For more information about the values of these parameters, see the API reference in DocumentationDocumentation. You can also visit OpenAPI Explorer to obtain the parameter values of API operations for some services. Endpoint: the endpoint of a service. Version: the version of the API. The version is in the YYYY-MM-DD format. s Operation information: the name of the API operation that you want to call. The APIs of most Apsara Stack services, such as Threat Detection Service, are RPC APIs. If you want to call an RPC API operation, you must obtain the value of the Action parameter, and then specify the value in the `request.ApiName = "<Action>"` format. If you want to call a RESTful API operation of a service, such as Container Service for Kubernetes (ACK), you must obtain the value of the PathPattern parameter, and then specify the RESTful path in the `request.PathPattern = "<PathPattern>"` format.

**Example: Call an RPC API operation**

The following sample code shows how to use the CommonRequest method to call the API operation:

```bash
from aliyunsdkcore.client import AcsClient from aliyunsdkcore.request import CommonRequest client = AcsClient('{your_access_key_id}', '{your_access_key_secret}', '{your_region_id}') request = CommonRequest() request.set_domain('<your-endpoint>') //The endpoint of the service. request.set_version('<API-version>') //The version of the API. request.set_action_name('<your-action>')//The name of the API operation.
# or:
# request = CommonRequest(domain='<your-endpoint>', version='<API-version>',
action_name='your-action') request.add_query_param('PageNumber', '1') request.add_query_param('PageSize', '30') response = client.do_action_with_exception(request)
```

### 2.3 Call examples for SDK for Go

#### 2.3.1 Quick start

Apsara Stack SDK for Go allows you to access services without complex coding. This topic describes how to obtain and use the SDK for Go.

**Prerequisites**

An authorized account and an AccessKey pair (AccessKey ID and AccessKey secret) are obtained. You can obtain and view your AccessKey pair in the Apsara Uni-manager Management Console. For more information, see Obtain an AccessKey pair. The endpoint of a service is obtained. For more information, see Obtain an endpoint.

**Install the core package of Apsara Stack SDK for Go**

Apsara Stack SDK for Go supports Go 1.10.x and later. You can run the following command to install the core package:

```
go get -u github.com/aliyun/alibaba-cloud-sdk-go/sdk
```

**Use the SDK for Go**

To use the SDK for Go, perform the following steps:
1. Initialize a client instance.
s
2. Create an API request and specify the required parameters.
3. Initiate the API request and process the response or exception.

> **Note:** In the following code, replace the variables with actual values. Delete the angle brackets <> in the final code.
> The following section describes the variables:
> <your_region_id>: Replace the value of this parameter with the region ID.
> <your_access_key_id>: Replace the value of this parameter with your AccessKey ID.
> <your_access_key_secret>: Replace the value of this parameter with your AccessKey secret.
> <your-endpoint>: Replace the value of this parameter with the endpoint of the service.
> <API-version>: Replace the value of this parameter with the version of the API.
> <your-action>: Replace the value of this parameter with the name of the API operation.

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

This topic describes how to install the Go SDK. s The Alibaba Cloud Go SDK supports Go 1.7 or later versions. Install the Go SDK manually.
1. Download the source code of the Go SDK from the official site of Apsara Stack.
2. Extract the package to the directory where the GO_PATH file of the current user resides.

##### 2.3.2.2 Use CommonRequest to call API operations

> **Note:** If you want to call the API operations of an Apsara Stack service that does not provide SDKs, you can use CommonRequest. You can use CommonRequest to call API operations.

**Benefits**

CommonRequest provides the following benefits:
1. Lightweight: You need only to download the core package. You do not need to download
and install SDKs of Apsara Stack services.
2. Easy to use: You can call the newly released API operations of an Apsara Stack service
without the need to update the SDK for the service.
3. Fast iteration.

**Use CommonRequest to call an API operation**

Apsara Stack services provide RPC and RESTful APIs. The request method of CommonRequest varies based on the style of the API that you want to call. In most cases, an API uses the RPC style if the API operations include the Action parameter. An API uses the RESTful style if the API operations include the PathPattern parameter. All API operations of a service use the same API style. The API of each service supports only one style. If you pass an invalid identifier, another API operation may be called, or the `ApiNotFound` error is returned. If you want to send a CommonRequest request, you must obtain the values of the following parameters. For more information about the values of these parameters, see the API reference in DocumentationDocumentation. You can also visit OpenAPI Explorer to obtain the parameter values of API operations for some services. Endpoint: the endpoint of a service. Version: the version of the API. The version is in the YYYY-MM-DD format. Operation information: the name of the API operation that you want to call. The APIs of most Apsara Stack services, such as Threat Detection Service, are RPC APIs. If you want to call an RPC API operation, you must obtain the value of the Action parameter, and then specify the value in the `request.ApiName = "<Action>"` format. If you want to call a RESTful API operation of a service, such as Container Service for Kubernetes (ACK), you must obtain the value of the PathPattern parameter, and then specify the RESTful path in the `request.PathPattern = "<PathPattern>"` format.

**Example: Call an RPC API operation**

The following sample code shows how to use the CommonRequest method to call the API operation: s

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
    request.Domain = "<your-endpoint>"// The endpoint of the service.
    request.Version = "<API-version>"// The version of the API.
    request.ApiName = "<your-action>"// The name of the API operation.
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

Common request parameters must be included in all Apsara Stack Security API requests. Table 1. Table of common request parameters

| Parameter | Type | Requi red | Description |
|---|---|---|---|
| Format | Strin g | No | The format in which to return the response. Set the value to JSON. |
| Version | Strin g | Yes | The version number of the API. Specify the version number in the YYYY-MM-DD format. Valid values: If you call the API operations of the cloud service whose service code is Auditprivate, set the value to 2018-01-16. If you call the API operations of the cloud service whose service code is yundunnextsoc, set the value to 2019-07-23. If you call the API operations of the cloud service whose service code is Sas, set the value to 2018-12-03. If you call the API operations of the cloud service whose service code is aegis, set the value to 2016-11-11. If you call the API operations of the cloud service whose service code is yundun-css, set the value to 2021-10-11. If you call the API operations of the cloud service whose service code is secspy, set the value to 2019-08-05. If you call the API operations of the cloud service whose service code is Ddosprivate, set the value to 2018-01-16. If you call the API operations of the cloud service whose service code is hsm-private, set the value to 2018-06-30. If you call the API operations of the cloud service whose service code is Cloudfw, set the value to 2017-12-07. If you call the API operations of the cloud service whose service code is Sddp, set the value to 2019-01-03. If you call the API operations of the cloud service whose service code is semawaf, set the value to 2020-07-01. If you call the API operations of the cloud service whose service code is soar, set the value to 2018-12-03. |
| AccessKeyId | Strin g | Yes | The AccessKey ID provided to you by Apsara Stack. |
| AccessKeySe cret | Strin g | Yes | The AccessKey secret provided to you by Apsara Stack. |
| RegionId | Strin g | Yes | The region ID of the service. |

ameters

| Product | Strin g | Yes | The name of the service to which the API operation belongs. Valid values: Auditprivate: basic components of Apsara Stack Security yundunnextsoc: Security Operations Center (SOC) Sas: Threat Detection Service aegis: Server Guard yundun-css: Container Production secspy: Network Detection and Response Ddosprivate: Anti-DDoS Service hsm-private: Data Encryption Service Cloudfw: Cloud Firewall Sddp: Sensitive Data Discovery and Protection (SDDP) semawaf: Web Application Firewall (WAF) soar: Security Orchestration and Automation Response (SOAR) |
|---|---|---|---|
| EndpointPre | Strin g | Yes | The prefix in the endpoint of the service to which the API operation belongs. Valid values: auditprivate: the prefix in the endpoint of basic components of Apsara Stack Security yundunnextsoc-pop: the prefix in the endpoint of SOC tds: the prefix in the endpoint of Threat Detection Service aegis: the prefix in the endpoint of Server Guard yundun-css: the prefix in the endpoint of Container Protection secspy-share: the prefix in the endpoint of Network Detection and Response ddosprivate: the prefix in the endpoint of Anti-DDoS Service hsmprivate: the prefix in the endpoint of Data Encryption Service cloudfw: the prefix in the endpoint of Cloud Firewall sddp-api: the prefix in the endpoint of SDDP semawaf: the prefix in the endpoint of WAF soar: the prefix in the endpoint of SOAR |

**Common response parameters**

API responses use the HTTP response format: A 2xx status code indicates a successful call. A 4xx or 5xx status code indicates a failed call. Responses are returned in the JSON format. Every response returns a unique RequestID regardless of whether the call is successful. rations Center

## 4 Security Operations Center

### 4.1 Request method

#### 4.1.1 Request syntax

**Description**

where: `endpoint` : the endpoint of the Security Operations Center (SOC) API is `yundunnewsoc-pop.`

```
[ RegionId].example.com .
```

**Note**

`Action` : the name of the operation being performed. For example, if `Action=GetEcsProtectCount` ,You can call this operation to query the number of ECS instances with an online Server Guard agent and the number of ECS instances with an offline agent.

#### 4.1.2 Sign API requests

Apsara Stack Security authenticates each access request. Therefore, a request must contain signature information regardless of whether it is sent over HTTP or HTTPS.

**Authorization**

To ensure the security of your account, we recommend that you use a RAM user to call API operations. Before you use a RAM user to call an API operation, you must grant the RAM user the required permissions by creating an policy and attaching the policy to the RAM user.

**API signature**

You must sign all API requests to ensure security. Alibaba Cloud uses the request signature to verify the identity of the API caller. When you manually make an API request, you must use the AccessKey secret to calculate an HMAC value based on the encoded and sorted request string. The HMAC value is the signature. For more information, see the definition in RFC 2104. The following parameters are used in the following procedure to describe how to calculate a signature.

| Parameter | Description |
|---|---|
| Endpoint | http://yundunnewsoc-pop.[ RegionId].example.com/? |
| Operation-specific parameters | Action=GetEcsProtectCount |

rations Center

| Common parameters except Signature | &Timestamp=2016-02-23T12:46:24Z &Format=JSON &AccessKeyId=<yourAccessKeyId> &SignatureMethod=HMAC-SHA1 &SignatureNonce=3ee8c1b8-83d3-44af-a94f-4e0ad82fd6cf &Version=2019-07-23 &SignatureVersion=1.0 |
|---|---|
| AccessKey secret | <yourAccessKeySecret> |

1. Create a canonicalized query string by arranging the request parameters.

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

rations Center Common request parameters must be included in all Apsara Stack Security API requests, such as the API version number and authentication information.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Version | String | Yes | The version number of the API. The value is in the format of YYYY-MM-DD. Set the value to 2019-07-23. |
| AccessKeyId | String | Yes | The AccessKey ID provided to you by Alibaba Cloud. |
| Signature | String | Yes | The signature string of the current request. |
| SignatureMethod | String | Yes | The encryption method of the signature string. Set the value to HMAC-SHA1. |
| Timestamp | String | Yes | The timestamp of the request. Specify the time in the ISO 8601 standard in the YYYY-MM-DDThh:mm:ssZ format. The time must be in UTC. For example, 2014-05-26T12:00:00Z indicates 20:00:00 on May 26, 2014 (UTC+8). |
| SignatureVersion | String | Yes | The version of the signature encryption algorithm. Set the value to 1.0. |
| SignatureNonce | String | Yes | A unique, random number used to prevent replay attacks. You must use different numbers for different requests. |
| ResourceOwnerA ccount | String | No | The owner account (the logon username) of the resource you want to access by using this API request. |
| Format | String | No | The format of the response. Valid values: JSON and XML. Default value: XML. |

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

| libaba Cloud wareness | Security- | Situation |   | er De | veloper Guide·Security Op rations Cente |
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

| A A | libaba Cloud Sec wareness | urity-Situation |   | Cloud Security Management Cen er Developer Guide·Security Op rations Cente | t e r |
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

You can call this operation to query security alerts on users or on the platform based on specified conditions.

**Request parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeAlarms. |
| DataScope | Integer | Yes | Specifies whether the alerts on users or the platform are queried. Valid values: 0: platform 1: users |
| SourceFrom | Integer | No | The data source of security alerts. |
| UserId | Long | No | The ID of the department to query. |
| PageSize | Integer | Yes | The number of alerts to return on each page. |
| PageNo | Integer | Yes | The number of the page to return. |

rations Center

| AlarmType | String | No | The type of the alerts to query. |
|---|---|---|---|
| ProcessState | Integer | No | The processing status of the alerts to query. |
| KeyWord | String | No | The keywords of the alerts or keywords in the ID or names of assets related to the alerts. |
| RiskLevels | List<Integer> | No | The risk levels of the alerts to query. |

**Response parameters**

| Parameter | Type | Description |
|---|---|---|
| RequestId | String | The ID of the request. |
| AlarmId | Long | The ID of the alert. |
| RiskLevel | Integer | The risk level of the alert. |
| AlarmName | String | The name of the alert. |
| AssetType | String | The type of the asset. |
| Asset | String | The ID of the asset. |
| UserName | String | The user name. |
| UserId | Long | The ID of the user or platform. |
| RaisedTime | Long | The time when the alert was generated. |
| ProcessState | Integer | The processing status of the alert. |
| AlarmType | String | The type of the alert. |
| SourceFrom | Integer | The data source of the alert. |
| AttackerIp | String | The IP address of the attacker. |
| AssetName | String | The name of the asset. |
| AssetPublicIps | String | The public IP address of the affected asset. |
| AssetPrivateIps | String | The internal IP address of the affected asset. |
| AlarmUniqueInfo | String | The unique key of the alert. |
| LastTime | String | The last time when the alert was generated. |
| Total | Integer | The total number of entries returned. |

**Examples**

Sample requests rations Center

```
http(s)://yundunnewsoc-pop.[ RegionId].example.com/? Action=DescribeAlarms &RiskLevels=[0,1,2] &DataScope=1 &PageSize=20 &PageNo=1 &<Common request parameters>
```

Sample success responses in JSON format `{`

```json
    "code":200,
    "data":{
        "Data":{
            "PageSize":20,
            "Total":177,
            "Items":[
```

`{`

```json
                    "AlarmId":30307,
                    "UserName":"yundun****",
                    "AlarmType":"Malicious Process",
                    "SourceFrom":20,
                    "AssetName":"yun****",
                    "AssetPrivateIps":"192. *. *.1",
                    "ProcessState":1,
                    "AssetType":"ECS",
                    "AlarmName":"Mining process",
                    "UserId":1****,
                    "AlarmUniqueInfo":"34dsa1",
                    "AssetPublicIps":"10. *. *.1",
                    "Asset":"2f43eb69-****",
                    "RaisedTime":1571826361000,
                    "RiskLevel":2,
                    "LastTime":1573021501000
```

`}` `],`

```json
            "PageNo":1
```

`}` `},`

```json
    "requestId":"B2C5D1EB-202F-4132-A763-2D16538B****",
    "success":true
```

`}`

**Error codes**

For a list of error codes, visit the Error codes.

#### 4.2.3 DescribeVulFrangs

You can call this operation to query vulnerabilities.

**Request parameters**

rations Center

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeVulFrangs. |
| UserId | Long | No | The ID of the department to query. |
| RiskLevels | Integer | No | The severity of the vulnerabilities to query. |
| ProcessState | Integer | No | The processing status of the vulnerabilities to query. |
| Page | Integer | Yes | The number of the page to return. |
| PageSize | Integer | Yes | The number of entries to return on each page. |
| VulType | String | No | The type of the vulnerabilities to query. |
| KeyWord | String | No | The name of the vulnerability or asset to query. |
| DataScope | Integer | Yes | Specifies whether the data of users or the platform is queried. Valid values: 0: platform 1: users |
| NeedFix | String | No | Specifies whether the vulnerabilities to query require fixes. |

**Response parameters**

| Parameter | Type | Description |
|---|---|---|
| RequestId | String | The ID of the request. |
| PageSize | Integer | The number of entries returned per page. |
| PageNo | Integer | The page number of the returned page. |
| Total | Integer | The number of entries returned. |
| Items | Array | The list of vulnerabilities. |
| └LastTime | Long | The last time when the vulnerability was detected. |
| └RiskLevel | Integer | The severity of the vulnerability. |
| └ProcessState | Integer | The processing status of the vulnerability. |
| └AssetType | String | The type of the affected asset. |
| └NeedFix | String | Indicates whether the vulnerability requires a fix. |

rations Center

| └VulRelated | String | The ID of the vulnerability details. |
|---|---|---|
| └Asset | String | The ID of the asset affected by the vulnerability. |
| └SourceFrom | Integer | The data source. |
| └Id | Long | The ID of the vulnerability. |
| └RaisedTime | Long | The first time when the vulnerability was detected. |
| └VulName | String | The name of the vulnerability. |
| └VulType | String | The type of the vulnerability. |
| └AssetPublicIps | String | The public IP address of the affected asset. |
| └AssetPrivateIps | String | The internal IP address of the affected asset. |
| └AssetName | String | The name of the affected asset. |

**Examples**

Sample requests

```
http(s)://yundunnewsoc-pop.[ RegionId].example.com/? Action=DescribeVulFrangs &DataScope=1 &PageSize=20 &Page=1 &<Common request parameters>
```

Sample success responses in JSON format rations Center `{`

```json
    "code":200,
    "data":{
        "Data":{
            "PageSize":20,
            "Total":445,
            "Items":[
```

`{`

```json
                    "ProcessState":1,
                    "AssetType":"ECS",
                    "NeedFix":"later",
                    "VulRelated":"CVE-2016-5195",
                    "Asset":"eb9ea4b0-****",
                    "SourceFrom":1,
                    "Id":6370,
                    "RaisedTime":2019,
                    "RiskLevel":1,
                    "VulName":"RHSA-2017:0372: kernel-aarch64 security and bug fix updat
e",
                    "LastTime":"2019-11-05 17:12:12",
                    "VulType":"cve"
```

`}` `],`

```json
            "PageNo":1
```

`}` `},`

```json
    "requestId":"32B57B56-958C-49C5-BB49-0BABE2060305",
    "success":true
```

`}`

**Error codes**

For a list of error codes, visit the Error codes.

#### 4.2.4 DescribeHcFrangs

You can call this operation to query the risks in the server configurations set by the user.

**Request parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeHcFrangs. |
| ProcessState | Integer | No | The processing status of the risks to query. |
| HcType | String | No | The type of server configuration risks to query. |
| Page | Integer | Yes | The number of the page to return. |

rations Center

| PageSize | Integer | Yes | The number of entries to return on each page. |
|---|---|---|---|
| KeyWord | String | No | The server baseline name or asset name. |
| DataScope | Integer | Yes | Specifies whether the data of users or the platform is queried. Valid values: 0: platform 1: users |
| UserId | Long | No | The ID of the department to query. |

**Response parameters**

| Parameter | Type | Description |
|---|---|---|
| RequestId | String | The ID of the request. |
| PageSize | Integer | The number of entries returned per page. |
| PageNo | Integer | The page number of the returned page. |
| Total | Integer | The total number of the returned entries. |
| Items | Array | The list of servers that SOC is authorized to scan. |
| └lastFoundTime | Long | The last time when risks were detected. |
| └RiskLevel | Integer | The level of the risk. Valid values: 0: low 1: medium 3: high |
| └ProcessState | Integer | The processing status of the risk. 1: handled 2: unhandled |
| └HcName | String | The name of the server configuration risk. |
| └HcType | String | The type of the server configuration risk. |
| └UserName | String | The name of the department to which the affected asset belongs. |
| └UserId | Long | The ID of the department to which the affected asset belongs. |
| └SourceFrom | Integer | The data source. |
| └Id | Long | The ID of the entry. |
| └Asset | String | The ID of the affected asset. |
| └AssetType | String | The type of the affected asset. |

rations Center

| └AssetName | String | The name of the affected asset. |
|---|---|---|
| └AssetPublicIps | String | The public IP address of the affected asset. |
| └AssetPrivateIps | String | The internal IP address of the affected asset. |

**Examples**

Sample requests

```
http(s)://yundunnewsoc-pop.[ RegionId].example.com/? Action=DescribeHcFrangs &DataScope=1 &PageSize=20 &Page=1 &<Common request parameters>
```

Sample success responses in JSON format `{`

```json
    "code":200,
    "data":{
        "Data":{
            "PageSize":20,
            "Total":47,
            "Items":[
```

`{`

```json
                    "UserName":"yun****",
                    "SourceFrom":2,
                    "HcType":"Alibaba Cloud",
                    "AssetName":"yun3 ",
                    "LastFoundTime":"2019-11-06 01:03:55",
                    "AssetPrivateIps":"192. *. *.1",
                    "ProcessState":1,
                    "HcName":"Alibaba Cloud Standard",
                    "AssetType":"ECS",
                    "UserId":11424,
                    "AssetPublicIps":"10. *. *.1",
                    "Asset":"71513dfc ",
                    "Id":111,
                    "RiskLevel":2
```

`}` `],`

```json
            "PageNo":1
```

`}` `},`

```json
    "requestId":"FE7137B7-84D8-4AF7-969B-C0DF5118****",
    "success":true
```

`}`

**Error codes**

For a list of error codes, visit the Error codes. rations Center

### 4.3 SOAR

#### 4.3.1 Playbooks

##### 4.3.1.1 ModifyPlaybook

Modifies a playbook.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyPlaybook | The operation that you want to perform. Set the value to ModifyPlaybook. |
| DisplayName | String | Yes | Test 1 | The display name of the playbook. |
| PlaybookId | Integer | Yes | 582 | The ID of the playbook. |
| Taskflow | String | No | XXX | The configuration file of the playbook. |
| Description | String | No | Demo playbook | The description of the playbook. |
| InputType | String | No | event | The input type. Set the value to event. |
| OperateType | String | No | general | The operation type of the playbook. Set the value to general. |
| OwnType | String | No | user | The ownership type of the playbook. Valid values: user: custom sys: built-in |
| ExecuteMode | String | No | one | The execution method of the playbook in the production environment. Valid values: one: The playbook is manually run. mul: The playbook is run based on scheduling configurations. stream: The playbook is run based on streaming data. |

rations Center

| Cron | String | No | 0 0 9 * * ? | The scheduling configurations for the playbook. |
|---|---|---|---|---|

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 8277EDCA-9E03- 4102-867E- E346E280865C | The ID of the request. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=ModifyPlaybook &DisplayName=Test 1 &PlaybookId=582 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RequestId>8277EDCA-9E03-4102-867E-E346E280865C</RequestId>
```

`JSON` format `{`

```json
    "RequestId": "8277EDCA-9E03-4102-867E-E346E280865C"
```

`}`

##### 4.3.1.2 TriggerPlaybook

Runs a playbook.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | TriggerPlaybook | The operation that you want to perform. Set the value to TriggerPlaybook. |
| InputParam | String | Yes | {"name":"test"," ip":"10.123.10.1 0"} | The parameters that are used to run the playbook. Specify the custom input parameters of the playbook. |

rations Center

| PlaybookName | String | Yes | test rtap _ | The name of the playbook that you want to run. |
|---|---|---|---|---|
| PlaybookId | Integer | No | 531 | The ID of the playbook that you want to run. |
| TriggerType | String | No | manual | The method for running the playbook. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0E402C78-34DC- 4B2B-BB15- 73BB914172C1 | The ID of the request. |
| TriggerUuid | String | a5a60946-3ad4- 4e0d-92db- 500da9619793 | The UUID of the task that is generated when the playbook is run. You can stop the task or query the result of the task by using the UUID. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=TriggerPlaybook &InputParam={"name":"test","ip":"10.123.10.10"} &PlaybookName=test_rtap &<Common request parameters>
```

Sample success responses `XML` format

```xml
<TriggerUuid>a5a60946-3ad4-4e0d-92db-500da9619793</TriggerUuid> <RequestId>0E402C78-34DC-4B2B-BB15-73BB914172C1</RequestId>
```

`JSON` format `{`

```json
    "TriggerUuid": "a5a60946-3ad4-4e0d-92db-500da9619793",
    "RequestId": "0E402C78-34DC-4B2B-BB15-73BB914172C1"
```

`}`

##### 4.3.1.3 PublishPlaybook

Publishes a playbook.

**Request parameters**

rations Center

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | PublishPlaybook | The operation that you want to perform. Set the value to PublishPlaybook. |
| PlaybookId | Integer | Yes | 531 | The ID of the playbook. An ID is generated for each playbook that you create. You can manage playbooks by ID. |
| Restart | Boolean | Yes | true | Specifies whether to restart the playbook. Valid values: true: restarts and publishes the playbook after the playbook is stopped. false: directly publishes the playbook. |
| State | Boolean | Yes | true | The status of the playbook. Valid values: true: The playbook is published. false: The playbook is disabled. |
| PicUrl | String | No | http://sophon- gen//2018-12- 03/-4a86-aa76- 8705e4fc6988.j pg | The URL of the image for the playbook. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 913BE26B-F9CC- 4A84-8CEC- 190E4BADD246 | The ID of the request. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=PublishPlaybook &PlaybookId=531 &Restart=true &State=true &<Common request parameters>
```

Sample success responses `XML` format rations Center

```xml
<RequestId>913BE26B-F9CC-4A84-8CEC-190E4BADD246</RequestId>
```

`JSON` format `{`

```json
    "RequestId": "913BE26B-F9CC-4A84-8CEC-190E4BADD246"
```

`}`

##### 4.3.1.4 StopOneAction

Stops the task that is generated when a playbook is run.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | StopOneAction | The operation that you want to perform. Set the value to StopOneAction. |
| RequestUuid | String | Yes | 73b14357-e011- 4993-a769- bfb779ab3638 | The UUID of the task that you want to stop. You can obtain the UUID from TriggerUuid by calling the TriggerPlaybook operation. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | C8242F6C-F6E9- 491C-AA00- D619224268ED | The ID of the request. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=StopOneAction &RequestUuid=73b14357-e011-4993-a769-bfb779ab3638 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RequestId>C8242F6C-F6E9-491C-AA00-D619224268ED</RequestId>
```

`JSON` format rations Center `{`

```json
    "RequestId": "C8242F6C-F6E9-491C-AA00-D619224268ED"
```

`}`

##### 4.3.1.5 DescribePlaybook

Queries the details of a playbook.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribePlayboo k | The operation that you want to perform. Set the value to DescribePlaybook. |
| PlaybookId | Integer | No | 597 | The ID of the playbook. |
| PlaybookName | String | No | Portrait of victi _ _ m | The name of the playbook. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Playbook | Struct |   | The details of the playbook. |
| Active | Boolean | false | The status of the playbook. Valid values: true: The playbook is enabled. false: The playbook is disabled. |
| Compiledresul t | String | "" | The compilation result of the playbook. |
| Creator | String | sys | The user who created the playbook. |
| Cron | String | 0 0 9 * * ? | The scheduling configurations for the playbook. |
| Description | String | "" | The description of the playbook. |
| DisplayName | String | Test 1 | The display name of the playbook. |
| DomainId | String | ids-group | The tenant information of the playbook. |

rations Center

| ExecuteMode | String | one | The execution method of the playbook. Valid values: one: The playbook is manually run. mul: The playbook is run based on scheduling configurations. stream: The playbook is run based on streaming data. |
|---|---|---|---|
| GmtCreate | Long | 1642066923992 | The time at which the playbook was created. The value is a 13-byte timestamp. Unit: milliseconds. |
| GmtModified | Long | 1642066923992 | The time at which the playbook was last modified. The value is a 13-byte timestamp. Unit: milliseconds. |
| Id | Long | 582 | The ID of the playbook. |
| InputParams | String | [{"name":"compon ent name","dataTy _ pe":"String","descri ption":"Component name","required":f alse,"stanchDefault Value":""}, {"name":"version", "dataType":"String ","description":"Co mponent version","required" :false,"stanchDefau ltValue":""}] | The input parameters of the playbook. |
| Inputtype | String | event | The input type. |
| Modifier | String | yundunluck | The user who last modified the playbook. |
| Name | String | Test 1 | The name of the playbook. |
| OnlineActive | Boolean | false | The status of the playbook. Valid values: true: The playbook is enabled. false: The playbook is disabled. |
| OnlineCompile dresult | String | "" | The compilation result of the playbook in the production environment. |

rations Center

| OnlineExecute Mode | String | one | The execution method of the playbook in the production environment. Valid values: one: The playbook is manually run. mul: The playbook is run based on scheduling configurations. stream: The playbook is run based on streaming data. |
|---|---|---|---|
| OnlineOss | String | sophon- gen/23cf45b4- ab29-4e36-accb- ba81cd3cc999- 1641814492160- beaver linkage att _ _ ack ban v62 test.j _ _ _ ar | The Object Storage Service (OSS) storage path that is used for the compilation result of the playbook in the production environment. |
| OperateType | String | general | The operation type of the playbook. |
| Oss | String | sophon- gen/23cf45b4- ab29-4e36-accb- ba81cd3cc999- 1641814492160- beaver linkage att _ _ ack ban v62 test.j _ _ _ ar | The OSS storage path that is used for the compilation result of the playbook. |
| Owner | String | sys | The owner of the playbook. |
| Taskconfig | String | {\"apps\": [{\"actions\": [{\"customInput\":t rue,\"description\":\ "Call an API operation\",\"id\":0, \"name\":\"execute API\" | The configuration file of the playbook. |
| Taskflow | String | <?xml version=\"1.0\" encoding=\"UTF- 8\"?> <bpmn:definitions xmlns:xsi=\"http:// www.w3.org/2001/ XMLSchema- instance\ | The information about the component on which the playbook depends. |
| TenantId | String | baba | The tenant information. |
| TriggerInfo | String | {"Query start time":"2022-01-05 10:10:10","Query end time":"2022- 01-05 10:10:10"} | The information that is used to manually run the playbook. |

rations Center

| ownType | String | user | The ownership type of the playbook. Valid values: user: custom sys: built-in |
|---|---|---|---|
| RequestId | String | 65C02B7B-C23D- 4929-A378- 11EB59813141 | The ID of the request. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribePlaybook &<Common request parameters>
```

Sample success responses `XML` format rations Center

```json
<Playbook>
    <Owner>sys</Owner>
    <Description>""</Description>
    <GmtModified>1642066923992</GmtModified>
    <Creator>sys</Creator>
    <OnlineExecuteMode>one</OnlineExecuteMode>
    <Cron>0 0 9 * * ?</Cron>
    <Taskconfig>{\"apps\":[{\"actions\":[{\"customInput\":true,\"description\":\"Call a
n API operation\",\"id\":0,\"name\":\"executeAPI\"</Taskconfig>
    <Name>Test 1</Name>
    <Compiledresult>""</Compiledresult>
    <InputParams>[{"name":"component_name","dataType":"String","description":"Component
name","required":false,"stanchDefaultValue":""}, {"name":"version","dataType":"String","description":"Component version","required":false,"stanchDefaultValue":""}]</InputParams>
    <OnlineActive>false</OnlineActive>
    <DisplayName>Test 1</DisplayName>
    <Inputtype>event</Inputtype>
    <ExecuteMode>one</ExecuteMode>
    <Modifier>yundunluck</Modifier>
    <OperateType>general</OperateType>
    <Taskflow>&lt;?xml version=\"1.0\" encoding=\"UTF-8\"?&gt;&lt;bpmn:definitions xmln
s:xsi=\"http://www.w3.org/2001/XMLSchema-instance\</Taskflow>
    <TriggerInfo>{"Query start time":"2022-01-05 10:10:10","Query end time":"2022-01-05
10:10:10"}</TriggerInfo>
    <Oss>sophon-gen/23cf45b4-ab29-4e36-accb-ba81cd3cc999-1641814492160-
beaver_linkage_attack_ban_v62_test.jar</Oss>
    <TenantId>baba</TenantId>
    <GmtCreate>1642066923992</GmtCreate>
    <Active>false</Active>
    <DomainId>ids-group</DomainId>
    <OnlineOss>sophon-gen/23cf45b4-ab29-4e36-accb-ba81cd3cc999-1641814492160-
beaver_linkage_attack_ban_v62_test.jar</OnlineOss>
    <ownType>user</ownType>
    <OnlineCompiledresult>""</OnlineCompiledresult>
    <Id>582</Id>
</Playbook> <RequestId>65C02B7B-C23D-4929-A378-11EB59813141</RequestId>
```

`JSON` format rations Center `{`

```json
    "Playbook": {
        "Owner": "sys",
        "Description": "\"\"",
        "GmtModified": 1642066923992,
        "Creator": "sys",
        "OnlineExecuteMode": "one",
        "Cron": "0 0 9 * * ?",
        "Taskconfig": "{\\\"apps\\\":[{\\\"actions\\\":
[{\\\"customInput\\\":true,\\\"description\\\":\\\"Call an API operation\\\",\\\"id\\\":0,\\\"name\\\":\\\"executeAPI\\\"",
        "Name": "Test 1",
        "Compiledresult": "\"\"",
        "InputParams": "
[{\"name\":\"component_name\",\"dataType\":\"String\",\"description\":\"Component name\ ",\"required\":false,\"stanchDefaultValue\":\"\"}, {\"name\":\"version\",\"dataType\":\"String\",\"description\":\"Component version\",\"required\":false,\"stanchDefaultValue\":\"\"}]",
        "OnlineActive": false,
        "DisplayName": "Test 1",
        "Inputtype": "event",
        "ExecuteMode": "one",
        "Modifier": "yundunluck",
        "OperateType": "general",
        "Taskflow": "&lt;?xml version=\\\"1.0\\\" encoding=\\\"UTF-8\\\"?
&gt;&lt;bpmn:definitions xmlns:xsi=\\\"http://www.w3.org/2001/XMLSchema-instance\\",
        "TriggerInfo": "{\"Query start time\":\"2022-01-05 10:10:10\",\"Query end
time"\":\"2022-01-05 10:10:10\"}",
        "Oss": "sophon-gen/23cf45b4-ab29-4e36-accb-ba81cd3cc999-1641814492160-
beaver_linkage_attack_ban_v62_test.jar",
        "TenantId": "baba",
        "GmtCreate": 1642066923992,
        "Active": false,
        "DomainId": "ids-group",
        "OnlineOss": "sophon-gen/23cf45b4-ab29-4e36-accb-ba81cd3cc999-1641814492160-bea
ver_linkage_attack_ban_v62_test.jar",
        "ownType": "user",
        "OnlineCompiledresult": "\"\"",
        "Id": 582
```

`},`

```json
    "RequestId": "65C02B7B-C23D-4929-A378-11EB59813141"
```

`}`

##### 4.3.1.6 DescribeSoarRecords

Queries the execution history of a playbook.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|

rations Center

| Action | String | Yes | DescribeSoarRe cords | The operation that you want to perform. Set the value to DescribeSoarRecords. |
|---|---|---|---|---|
| PageNumber | Integer | Yes | 1 | The number of the page to return. |
| PageSize | Integer | Yes | 20 | The number of entries to return on each page. |
| QueryCondition | String | Yes | {\"type\":\"comp lex\",\"condition\ ":\" {\\\"condition\\\" :\\\"AND\\\",\\\"ru les\\\": [{\\\"field\\\":\\\"t askName\\\",\\\" match\\\":\\\"is\\\ ",\\\"type\\\":\\\"s tring\\\",\\\"value \\\": [\\\"test rtap\\\"] _ }]}\"} | The query conditions. The value of this parameter includes the following fields: field: the field to match. value: the value to match. type: the type of match that you want to perform. Valid values: match: EQUALS TO. contains: CONTAINS. complex: a nested query. You must specify a nested query based on the description for QueryCondition. |
| TaskUuid | String | No | 73b14357-e011- 4993-a769- bfb779ab3638 | The UUID of the task that is generated when the playbook is run. You can obtain the UUID from TriggerUuid by calling the TriggerPlaybook operation. If you specify TriggerUuid, the value of QueryCondition does not take effect. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| PageNumber | Integer | 1 | The page number of the returned page. |
| PageSize | Integer | 20 | The number of entries returned per page. |
| RequestId | String | B57576EA-1F92- 4810-8CC7- B27FEE6CD9DE | The ID of the request. |
| SoarExecuteR ecords | Array of SoarExecuteR ecord |   | An array that consists of details of the execution history. |
| All | Integer | 1 | The number of times that the playbook is run. |

rations Center

| DataSourceNa me | String | 4357 | The name of the data source that triggers the playbook. |
|---|---|---|---|
| EndTime | Long | 1641460993364 | The time at which the playbook stops running. The value is a 13-byte timestamp. Unit: milliseconds. |
| EventId | String | 1641460993340 | The ID of the event that triggers the playbook. |
| RawEventReq | String | {\"ac\":\"c60dcd29f 8b0acc18028d0dc 82d73d3b\",\"data SourceName\":\"43 57\",\"domainId\":\" ids- group\",\"eventId\": \"1641460993340\ ",\"eventStr\": {},\"taskList\": [\"test rtap\"],\"tas _ kTriggerList\": [],\"tenantId\":\"ba ba\",\"triggerType\" :\"manual\",\"trigge rUser\":\"sys\",\"ts\" :\"1641460993340\ "}" | The detailed raw data about how the playbook is triggered. |
| RequestUuid | String | a5a60946-3ad4- 4e0d-92db- 500da9619793 | The UUID of the task that is generated when the playbook is run. |
| ResultLevel | String | DEBUG | The log level of the execution result for the playbook. Valid values: DEBUG INFO ERROR |
| ResultMessage | String | "" | The message of the execution result for the playbook. |
| Sao | String | test rtap _ | The name of the playbook. |
| SaoId | Long | 531 | The ID of the playbook. |
| SrcIp | String | 10.10.XX.XX | The IP address of the server on which the playbook is run. |

rations Center

| StartTime | Long | 1641460993348 | The time at which the playbook starts to run. The value is a 13-byte timestamp. Unit: milliseconds. |
|---|---|---|---|
| Status | String | success | The execution result. Valid values: success failed inprogresss |
| Success | Integer | 1 | The number of successful tasks. |
| TaskName | String | test rtap _ | The name of the task. |
| TaskUuid | String | cfa5cc68-9279- 45fa-88a0- c79cca020efe | The UUID of the task. |
| TriggerDataId | String | 1641460993340 | The ID of the data source that triggers the playbook. |
| TriggerType | String | manual | The method for running the playbook. |
| TriggerUser | String | 12385**452 | The user who triggers the playbook. The value is the ID of the account that is used for logon and API calls. |
| resultMessage | String | "" | The information about the execution result for the playbook. This parameter is deprecated. |
| TotalCount | Integer | 23 | The total number of entries returned. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeSoarRecords &PageNumber=1 &PageSize=20 &QueryCondition={\"type\":\"complex\",\"condition\":\" {\\\"condition\\\":\\\"AND\\\",\\\"rules\\\": [{\\\"field\\\":\\\"taskName\\\",\\\"match\\\":\\\"is\\\",\\\"type\\\":\\\"string\\\",\\\ alue\\\":[\\\"test_rtap\\\"]}]}\"} &<Common request parameters>
```

Sample success responses `XML` format rations Center

```xml
<TotalCount>23</TotalCount> <PageSize>20</PageSize> <RequestId>B57576EA-1F92-4810-8CC7-B27FEE6CD9DE</RequestId> <PageNumber>1</PageNumber> <SoarExecuteRecords>
    <Status>success</Status>
    <Sao>test_rtap</Sao>
    <All>1</All>
    <TriggerType>manual</TriggerType>
    <SaoId>531</SaoId>
    <EndTime>1641460993364</EndTime>
    <TaskUuid>cfa5cc68-9279-45fa-88a0-c79cca020efe</TaskUuid>
    <StartTime>1641460993348</StartTime>
    <resultMessage>""</resultMessage>
    <ResultMessage>""</ResultMessage>
    <SrcIp>10.10.XX.XX</SrcIp>
    <Success>1</Success>
    <TriggerUser>12385**452</TriggerUser>
    <TriggerDataId>1641460993340</TriggerDataId>
    <ResultLevel>DEBUG</ResultLevel>
    <TaskName>test_rtap</TaskName>
    <DataSourceName>4357</DataSourceName>
    <EventId>1641460993340</EventId>
    <RequestUuid>a5a60946-3ad4-4e0d-92db-500da9619793</RequestUuid>
    <RawEventReq>
{\"ac\":\"c60dcd29f8b0acc18028d0dc82d73d3b\",\"dataSourceName\":\"4357\",\"domainId\":\"i -group\",\"eventId\":\"1641460993340\",\"eventStr\":{},\"taskList\": [\"test_rtap\"],\"taskTriggerList\": [],\"tenantId\":\"baba\",\"triggerType\":\"manual\",\"triggerUser\":\"sys\",\"ts\":\"1641 0993340\"}" </RawEventReq> </SoarExecuteRecords>
```

`JSON` format rations Center `{`

```json
    "TotalCount": 23,
    "PageSize": 20,
    "RequestId": "B57576EA-1F92-4810-8CC7-B27FEE6CD9DE",
    "PageNumber": 1,
    "SoarExecuteRecords": {
        "Status": "success",
        "Sao": "test_rtap",
        "All": 1,
        "TriggerType": "manual",
        "SaoId": 531,
        "EndTime": 1641460993364,
        "TaskUuid": "cfa5cc68-9279-45fa-88a0-c79cca020efe",
        "StartTime": 1641460993348,
        "resultMessage": "\"\"",
        "ResultMessage": "\"\"",
        "SrcIp": "10.10.XX.XX",
        "Success": 1,
        "TriggerUser": "12385**452",
        "TriggerDataId": 1641460993340,
        "ResultLevel": "DEBUG",
        "TaskName": "test_rtap",
        "DataSourceName": 4357,
        "EventId": 1641460993340,
        "RequestUuid": "a5a60946-3ad4-4e0d-92db-500da9619793",
        "RawEventReq": "
{\\\"ac\\\":\\\"c60dcd29f8b0acc18028d0dc82d73d3b\\\",\\\"dataSourceName\\\":\\\"4357\\\", \"domainId\\\":\\\"idsgroup\\\",\\\"eventId\\\":\\\"1641460993340\\\",\\\"eventStr\\\":{},\\\"taskList\\\":[\ \\"test_rtap\\\"],\\\"taskTriggerList\\\": [],\\\"tenantId\\\":\\\"baba\\\",\\\"triggerType\\\":\\\"manual\\\",\\\"triggerUser\\\":\ "sys\\\",\\\"ts\\\":\\\"1641460993340\\\"}\""
```

`}` `}`

#### 4.3.2 Intelligence

##### 4.3.2.1 SyncBanRecord

Synchronizes blocking records.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | SyncBanRecord | The operation that you want to perform. Set the value to SyncBanRecord. |

rations Center

| BanType | String | Yes | ban-whole | The type of the blocking operation. You can specify this parameter based on your business requirements. The type of the blocking operation is returned when you unblock a threat indicator. |
|---|---|---|---|---|
| EndTime | Long | Yes | -1 | The end of the time range during which a threat indicator is blocked. The value is a 13-byte timestamp. Unit: milliseconds. If a threat indicator is permanently blocked, set the value to -1. |
| Entity | String | Yes | 12.12.XX.XX | The value of the blocked threat indicator. |
| EntityType | String | Yes | IP | The type of the blocked threat indicator. Valid values include IP and file hash. _ |
| PolicyId | String | Yes | 23 | The ID of the blocking rule that triggers the blocking operation. The ID is specified in the system that performs the blocking operation. |
| RuleConfig | String | Yes | {} | The custom configurations of the blocking rule. |
| StartTime | Long | Yes | 1640169543000 | The beginning of the time range during which a threat indicator is blocked. The value is a 13-byte timestamp. Unit: milliseconds. |
| TaskName | String | No | Test blocking record | The name of the task. |
| EventUuid | String | No | 3BB85AD2- E1D2-45C5- B22B- 949CBC9BD98B | The UUID of the case. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Id | Long | 10 | The ID of the blocking result. |

rations Center

| RequestId | String | 3BB85AD2-E1D2- 45C5-B22B- 949CBC9BD98B | The ID of the request. |
|---|---|---|---|

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=SyncBanRecord &BanType=ban-whole &EndTime=-1 &Entity=12.12.XX.XX &EntityType=IP &PolicyId=23 &RuleConfig={} &StartTime=1640169543000 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RequestId>3BB85AD2-E1D2-45C5-B22B-949CBC9BD98B</RequestId> <Id>10</Id>
```

`JSON` format `{`

```json
    "RequestId": "3BB85AD2-E1D2-45C5-B22B-949CBC9BD98B",
    "Id": 10
```

`}`

#### 4.3.3 Cases

##### 4.3.3.1 CreateEventByAlert

Creates a case based on a threat event that is reported by Security Operations Center (SOC).

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateEventByAl ert | The operation that you want to perform. Set the value to CreateEventByAlert. |

rations Center

| DocId | String | No | 1234567 | The docId of the threat event data in an Elasticsearch index. |
|---|---|---|---|---|
| BatchCode | String | No | 20212045 | The batch code of the threat event data. You can use the code to associate the threat event with raw error logs. |
| EsIndex | String | No | soc- alarms 2021.1 ___ 2.2 | The name of the Elasticsearch index to which the threat event belongs. |
| Name | String | No | SOAR-Webshell event | The name of the case. |
| Severity | String | No | information | The severity of the threat event. Valid values: 1. information 2. suspicious 3. general 4. serious 5. urgent |
| Type | String | No | networkScannin g | The type of the threat event. Valid values: 1. networkScanning 2. exploitVulnerability 3. maliciousSoftware 4. networkAttack 5. riskConnection 6. abnormalBehavior 7. illegalAccount |
| SourceIps | String | No | [{"ip":"12.12.XX. XX","port":123,"l ocation":"China" }] | The list of source IP addresses. |
| DestIps | String | No | [{"ip":"12.12.XX. XX","port":123,"l ocation":"China" }] | The list of destination IP addresses. |
| StartTime | Long | No | 1641540484251 | The start time of the case. The value is a 13-byte timestamp. Unit: milliseconds. |

rations Center

| ThreatTime | Long | No | 1641540484251 | The beginning of the time range for the threat event. The value is a 13- byte timestamp. Unit: milliseconds. |
|---|---|---|---|---|
| EndTime | Long | No | 1641540484251 | The end time of the case. The value is a 13-byte timestamp. Unit: milliseconds. |
| AttCks | String | No | attack | The name of the Adversarial Tactics, Techniques, and Common Knowledge (ATT&CK) stage. |
| Suggestions | String | No | Handling suggestion | The suggestions to handle the threat event. |
| Description | String | No | Threat description | The description of the threat event. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Id | Long | 12 | The ID of the case. |
| RequestId | String | 3BB85AD2-E1D2- 45C5-B22B- 949CBC9BD98B | The ID of the request. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=CreateEventByAlert &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RequestId>3BB85AD2-E1D2-45C5-B22B-949CBC9BD98B</RequestId> <Id>12</Id>
```

`JSON` format `{`

```json
    "RequestId": "3BB85AD2-E1D2-45C5-B22B-949CBC9BD98B",
    "Id": 12
```

`}` rations Center

#### 4.3.4 Tasks

##### 4.3.4.1 DescribeManualTaskInfo

Queries the execution results.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeManual TaskInfo | The operation that you want to perform. Set the value to DescribeManualTaskInfo. |
| NeedDataInfo | Boolean | Yes | true | Specifies whether to return details. Valid values: true: yes false: no |
| PageNumber | Integer | Yes | 10 | The number of the page to return. |
| PageSize | Integer | Yes | 1 | The number of entries to return on each page. |
| Id | Long | No | 1 | The ID of the task. |
| NodeName | String | No | test | The name of the node. |
| TaskUuid | String | No | 13123233 | The UUID of the task. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| ManualTaskRe cords | Array of SaoManualTas kInfoDO |   | An array that consists of details about the task. |
| ActionUuid | String | AF2B656D-C2C1- 4E47-85FD- 1596C83C6B86 | The UUID of the action. |
| ActualDealedT ime | Long | 1641803299000 | The time at which the task is handled. |
| ActualDealerId | String | 1 | The ID of the user who handled the task. |

rations Center

| AkkaActorInfo | String | test | The actor information in Akka. |
|---|---|---|---|
| AssignedUser Group | String | test | The name of the user group. |
| AssignedUserI d | String | test | The ID of the user. |
| Content | String | Data information | The content. |
| DataInfo | String | {"k":"value"} | The data information. |
| DataUrl | String | http://xxxxxx | The data URL. |
| DeadlineTime | Long | 1641803299000 | The deadline for handling the task. |
| DisplayAction Uuid | String | AF2B656D-C2C1- 4E47-85FD- 1596C83C6B86 | The display UUID of the action. |
| DownloadUrl | String | http://xxxxxx | The download URL. |
| GmtCreate | Long | 1641803299000 | The creation time. |
| GmtModified | Long | 1641803299000 | The modification time. |
| Id | Long | 1231 | The ID of the node. |
| NeedDataInfo | Boolean | true | Indicates whether data information is required. |
| NodeName | String | test | The name of the node. |
| PageConfigId | Long | 1 | The ID of the page configuration. |
| PlaybookId | Long | 1 | The ID of the playbook. |
| PlaybookName | String | test | The name of the playbook. |

rations Center

| Status | Integer | 0 | The status of the task. If this parameter is not specified, all tasks are queried. Valid values: -1: handling not required 0: unhandled 1: handled 2: unhandled after the deadline |
|---|---|---|---|
| TaskType | Integer | 1 | The type of the task. Valid values: 0: manual handling 1: notification |
| TaskUuid | String | AF2B656D-C2C1- 4E47-85FD- 1596C83C6B86 | The UUID of the task. |
| TenantId | String | yundun | The ID of the tenant. |
| Url | String | http:// | The data URL. |
| PageNumber | Long | 1 | The page number of the returned page. |
| PageSize | Long | 10 | The number of entries returned per page. |
| RequestId | String | AF2B656D-C2C1- 4E47-85FD- 1596C83C6B86 | The ID of the request. |
| TotalCount | Long | 100 | The total number of entries returned. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeManualTaskInfo &NeedDataInfo=true &PageNumber=10 &PageSize=1 &<Common request parameters>
```

Sample success responses `XML` format rations Center

```xml
<TotalCount>100</TotalCount> <PageSize>10</PageSize> <RequestId>AF2B656D-C2C1-4E47-85FD-1596C83C6B86</RequestId> <PageNumber>1</PageNumber> <ManualTaskRecords>
    <DataInfo>{"k":"value"}</DataInfo>
    <Status>0</Status>
    <ActualDealedTime>1641803299000</ActualDealedTime>
    <ActionUuid>AF2B656D-C2C1-4E47-85FD-1596C83C6B86</ActionUuid>
    <AssignedUserId>test</AssignedUserId>
    <NodeName>test</NodeName>
    <AssignedUserGroup>test</AssignedUserGroup>
    <NeedDataInfo>true</NeedDataInfo>
    <TaskUuid>AF2B656D-C2C1-4E47-85FD-1596C83C6B86</TaskUuid>
    <GmtModified>1641803299000</GmtModified>
    <AkkaActorInfo>test</AkkaActorInfo>
    <PlaybookName>test</PlaybookName>
    <Url>http://</Url>
    <PageConfigId>1</PageConfigId>
    <TenantId>yundun</TenantId>
    <GmtCreate>1641803299000</GmtCreate>
    <Content>Data information</Content>
    <DeadlineTime>1641803299000</DeadlineTime>
    <TaskType>1</TaskType>
    <DataUrl>http://xxxxxx</DataUrl>
    <PlaybookId>1</PlaybookId>
    <Id>1231</Id>
    <DisplayActionUuid>AF2B656D-C2C1-4E47-85FD-1596C83C6B86</DisplayActionUuid>
    <ActualDealerId>1</ActualDealerId>
    <DownloadUrl>http://xxxxxx</DownloadUrl>
</ManualTaskRecords>
```

`JSON` format rations Center `{`

```json
    "TotalCount": 100,
    "PageSize": 10,
    "RequestId": "AF2B656D-C2C1-4E47-85FD-1596C83C6B86",
    "PageNumber": 1,
    "ManualTaskRecords": {
        "DataInfo": "{\"k\":\"value\"}",
        "Status": 0,
        "ActualDealedTime": 1641803299000,
        "ActionUuid": "AF2B656D-C2C1-4E47-85FD-1596C83C6B86",
        "AssignedUserId": "test",
        "NodeName": "test",
        "AssignedUserGroup": "test",
        "NeedDataInfo": true,
        "TaskUuid": "AF2B656D-C2C1-4E47-85FD-1596C83C6B86",
        "GmtModified": 1641803299000,
        "AkkaActorInfo": "test",
        "PlaybookName": "test",
        "Url": "http://",
        "PageConfigId": 1,
        "TenantId": "yundun",
        "GmtCreate": 1641803299000,
        "Content": "Data information",
        "DeadlineTime": 1641803299000,
        "TaskType": 1,
        "DataUrl": "http://xxxxxx",
        "PlaybookId": 1,
        "Id": 1231,
        "DisplayActionUuid": "AF2B656D-C2C1-4E47-85FD-1596C83C6B86",
        "ActualDealerId": 1,
        "DownloadUrl": "http://xxxxxx"
```

`}` `}`

### 4.4 Operations Center

#### 4.4.1 QueryThreats

Queries attack data in the Operations Center dashboard.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | QueryThreats | The operation that you want to perform. Set the value to QueryThreats. |
| FromTime | Long | No | 1640944798076 | The beginning of the time range to query. Unit: milliseconds. |

rations Center

| ToTime | Long | No | 1641549603697 | The end of the time range to query. Unit: milliseconds. |
|---|---|---|---|---|
| CurrentPage | Integer | No | 1 | The number of the page to return. |
| PageSize | Integer | No | 10 | The number of entries to return on each page. |
| Index | String | No | threat | The data index. Set the value to threat. |
| UserIds | String | No | - 1,29561408888 8**** | The ID of the department. You can specify -1 or the ID of a tenant organization. The value -1 specifies that data on the platform side is queried. Separate multiple values with commas (,). |
| Aliuid | Long | No | 1 | This parameter is deprecated. |
| Query | String | No | 192.168.XX.XX | The keyword to match. You can specify the IP address of an alerting asset or the IP address in an attack. |
| ProcessStatus | String | No | 1 | The handling status. Valid values: 1: unhandled 2: handled |
| ThreatLevel | String | No | 1 | The risk level of the attack. Valid values: 1: low 2: medium 3: high |
| SrcFrom | String | No | 20,40 | The source of data. Separate multiple values with commas (,). Valid values: 20: Server Guard 40: Web Application Firewall (WAF) 41: Cloud Firewall 44: Network Detection and Response (NDR) |

rations Center

| ThreatType | String | No | Suspicious process | The type of the alert that is generated for the attack. Valid values include Non-web attack, Precise defense, Web attack, Other, and Suspicious process. |
|---|---|---|---|---|
| ThreatName | String | No | Suspicious encoded command | The name of the attack. |
| ProcessWay | String | No | 1 | The handling method. Valid values: 0: allow 1: intercept 2: ignore 3: manually handle 4: batch block 5: automatically handle 6: alert 7: discard 8: block |
| ThreatInoutside | String | No | 1 | The source of the attack. Valid values: 1: internal attack 2: external attack |
| ThreatResult | String | No | Success | The result of the attack. Valid values include Attempt, Success, and Failure. |
| Lang | String | No | zh CN _ | The language of the content within the request and response. Valid values: zh CN: Simplified Chinese _ zh TW: Traditional Chinese _ en US: English _ |
| Tag | String | No | 121 | The tag. |
| DestinationIp | String | No | 192.168.XX.XX | The attacked IP address. |
| ThreatSourceIp | String | No | 172.12.XX.XX | The source IP address of the attack. |
| UrlHost | String | No | www.ecs****.co m | The website. |

**Response parameters**

rations Center

| Parameter | Type | Example | Description |
|---|---|---|---|
| CurrentPage | Integer | 1 | The page number of the returned page. |
| Datas | List | {"lastTime":16415 49724000," logTi __ me":16415497242 87,"process way":" _ "} | The list of data records that are queried from Elasticsearch. Each array in the list represents a data record. |
| FromTime | Long | 1641484800000 | The start time of the attack. Unit: milliseconds. |
| HistogramInter val | Long | 0 | The interval of the histogram. |
| PageSize | Integer | 10 | The number of entries returned per page. |
| RequestId | String | 8010791A-3154- 4154-ACB2- 866E56A6**** | The ID of the request. |
| ToTime | Long | 1641550177290 | The end time of the attack. Unit: milliseconds. |
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

`JSON` format rations Center

```json
{"ToTime":"1641550177290","PageSize":"10","RequestId":"8010791A-3154-4154-ACB2-866E56A6
****","HistogramInterval":"0","CurrentPage":"1","Datas":"
{\"lastTime\":1641549724000,\"__logTime\":1641549724287,\"process_way\":\"\"}","Total":"2 ","FromTime":"1641484800000"}
```

#### 4.4.2 QueryThreatChartData

Queries the data in a chart of the Operations Center dashboard.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | QueryThreatCha rtData | The operation that you want to perform. Set the value to QueryThreatChartData. |
| FromTime | Long | No | 1640944798076 | The beginning of the time range to query. Unit: milliseconds. |
| ToTime | Long | No | 1641549603697 | The end of the time range to query. Unit: milliseconds. |
| CurrentPage | Integer | No | 1 | The number of the page to return. |
| PageSize | Integer | No | 10 | The number of entries to return on each page. |
| Index | String | No | threat | The data index. Set the value to threat. |
| Aliuid | Long | No | 1 | This parameter is deprecated. |
| UserIds | String | No | - 1,29561408888 8**** | The ID of the department. You can specify -1 or the ID of a tenant organization. The value -1 specifies that data on the platform side is queried. Separate multiple values with commas (,). |
| Query | String | No | 192.168.XX.XX | The keyword to match. You can specify the IP address of an alerting asset or the IP address in an attack. |

rations Center

| ProcessStatus | String | No | 1 | The handling status. Valid values: 1: unhandled 2: handled |
|---|---|---|---|---|
| ThreatLevel | String | No | 1 | The risk level of the attack. Valid values: 1: low 2: medium 3: high |
| SrcFrom | String | No | 20,40 | The source of data. Separate multiple values with commas (,). Valid values: 20: Server Guard 40: Web Application Firewall (WAF) 41: Cloud Firewall 44: Network Detection and Response (NDR) |
| ThreatType | String | No | Suspicious process | The type of the alert that is generated for the attack. Valid values include Non-web attack, Precise defense, Web attack, Other, and Suspicious process. |
| ThreatName | String | No | Suspicious encoded command | The name of the attack. |
| ProcessWay | String | No | 1 | The handling method. Valid values: 0: allow 1: intercept 2: ignore 3: manually handle 4: batch block 5: automatically handle 6: alert 7: discard 8: block |
| ThreatInoutside | String | No | 1 | The source of the attack. Valid values: 1: internal attack 2: external attack |

rations Center

| ThreatResult | String | No | Success | The result of the attack. Valid values include Attempt, Success, and Failure. |
|---|---|---|---|---|
| Properties | String | No | {"x type":"term" _ ,"y config 1":"sr _ _ c from,count"} _ | The settings that are used to query the chart. Specify the value in the following JSON format: {"x type":"term"(X- _ axis),"y config 1":"src from(Y- _ _ _ axis),count(Count)"}. |
| ChartType | String | No | pie | The type of the chart. Valid values include histogram, bar, line, pie, table, and value. |
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

rations Center Sample success responses `XML` format

```xml
<RequestId>8010791A-3154-4154-ACB2-866E56A6****</RequestId> <Data>{"20":{"src_from,count":"23507"}}</Data>
```

`JSON` format

```json
{"RequestId":"8010791A-3154-4154-ACB2-866E56A6****","Data":"{\"20\": {\"src_from,count\":\"23507\"}}"}
```

## 5 APIs

### 5.1 CreateEventType

**Description**

You can call this operation to create an audit event type.

**Request parameters**

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to CreateEventType. |
| SourceId | String | Yes | The ID of the log source. |
| LogType | String | Yes | The log type code. |
| Name | String | Yes | The name of the audit event type. |
| Mark | String | Yes | The description of the audit event type. |

**Response parameters**

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| EventType | Struct | Information about the created audit event type. For more information, see the following parameter descriptions. |
| CreateTime | Long | The time when the audit event type was created. |
| Id | Integer | The ID of the audit event type. |
| LogType | Integer | The log type code. |
| Name | String | The audit event type name. |
| Mark | String | The description of the audit event type. |
| Reserved | Boolean | Indicates whether this is a system-reserved event type. |
| SourceId | Integer | The ID of the log source. |
| SourceName | String | The name of the log source. |

**Error codes**

For more information about the error codes that this operation can return, see Error codes.

**Examples**

Sample requests

```
https://auditprivate.[ RegionId].example.com/?Action=CreateEventType &LogType=5 &Name=High-risk database query &Remark=High-risk database query operation &SourceId=10000 &<Common request parameters>
```

Sample responses (JSON format) `{`

```json
 "RequestId":"4E5FB761-4927-443A-9606-79F22D516BE8",
 "EventType": {
  "CreateTime":1519810541531,
  "SourceId":10000,
  "LogType":5,
  "SourceName":"DRDS Rtools audit log",
  "Id":10235,
  "Name":"High-risk database query",
  "Reserved":false,
  "Remark":"High-risk database query operation"
```

`}` `}`

### 5.2 DescribeEventType

**Description**

You can call this operation to query information about audit event types.

**Request parameters**

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeEventType |
| PageSize | String | No | The maximum number of records displayed on a page. |
| CurrentPage | String | No | The current page number. |
| SourceId | String | No | The ID of the log source. Default value: null. If you do not specify this parameter, the log source ID is null. |
| LogType | String | No | The code of the log type. |

**Response parameters**

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| CurrentPage | Integer | The current page number. |
| PageSize | Integer | The maximum number of records displayed on a page. |
| TotalCount | Integer | The total number of returned records. |
| EventTypeList | Array | The list of audit event types. For more information, see the following parameter descriptions. |
| CreateTime | Long | The creation time. |
| Code | String | The code of the audit event type. |
| Id | Integer | The ID of the audit event type. |
| LogType | Integer | The code of the log type. |
| Name | String | The name of the audit event type. |
| Remark | String | The description of the audit event type. |
| Reserved | Boolean | Indicates whether this is a reserved event type in the system. |
| SourceId | Integer | The ID of the log source. |
| SourceName | String | The name of the log data source. |

**Error codes**

For more information about the error codes that this operation can return, see Error codes.

**Examples**

Sample requests

```
https://auditprivate.[ RegionId].example.com/?Action=DescribeEventType &CurrentPage=1 &LogType=1 &PageSize=100 &SourceId=1 &<Common request parameters>
```

Sample responses (JSON format) `{`

```json
 "RequestId":"1D494150-8CFC-4A53-9AD4-4E7EA5C2C245",
 "TotalCount":6,
 "PageSize":20,
 "CurrentPage":1,
 "EventTypeList":[
```

`{`

```json
           "CreateTime":1519810541531,
            "SourceId":10000,
            "LogType":5,
            "SourceName":"DRDS Rtools Audit Log",
            "Id":10235,
            "Name":"High-risk query",
            "Reserved":false,
            "Remark":"High-risk database query operation"
```

`}` `]` `}`

### 5.3 DeleteEventType

**Description**

You can call this operation to delete an audit event type.

**Request parameters**

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DeleteEventType. |
| Id | Integer | Yes | The ID of the audit event type. |

**Response parameters**

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |

**Error codes**

For more information about the error codes that this operation can return, see Error codes.

**Examples**

Sample requests

```
https://auditprivate.[ RegionId].example.com/?Action=DeleteEventType &Id=10001 &<Common request parameters>
```

Sample responses (JSON format) `{`

```json
 "RequestId":"4E5FB761-4927-443A-9606-79F22D516BE8"
```

`}`

### 5.4 CreateLogFilter

**Description**

You can call this operation to create a match criterion for audit log query.

**Request parameters**

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to CreateLogFilter. |
| SourceId | String | Yes | The ID of the log source. |
| LogType | String | Yes | The type of the log. |
| Name | String | Yes | The name of the match criterion. |
| Type | Integer | Yes | The type of the match criterion. Valid values: 1: filters by log. 2: filters by audit event. |
| Alertable | String | No | Indicates whether alerting is enabled. Valid values: True: indicates that alerting is enabled. False: indicates that alerting is disabled. |
| Defaultable | String | No | Indicates whether the match criterion is a default match criterion. Valid values: True: indicates that it is a default match criterion. False: indicates that it is not a default match criterion. |
| EndTime | String | No | The end time of the time frame specified for query, in timestamp format. |
| EventRiskLevel | String | No | The risk level code. |
| EventType | String | No | The audit event type. |
| LogAction | String | No | The action to be performed when the criterion is matched. |

| loud Security Mana r Developer Guide·A | gement Cent PIs |   | Alibaba Cloud Security-Situation Awarenes |
|---|---|---|---|

| LogInitiatior | String | No | The user that initiates the security audit. |
|---|---|---|---|
| LogOutcome | String | No | The result. |
| LogReason | String | No | The reason. |
| LogTarget | String | No | The target. |
| Query | String | No | The keywords specified for query. |
| StartTime | String | No | The end time of the time frame specified for query, in timestamp format. |

**Response parameters**

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| LogFilter | Struct | The created match criterion. For more information, see the following parameter descriptions. |
| CreateTime | Long | The time when the match criterion was created. |
| EventType | Integer | The audit event type. |
| Defaultable | Boolean | Indicates whether the match criterion is a default match criterion. |
| Id | Integer | The ID of the match criterion. |
| LogType | Integer | The type of the log. |
| Name | String | The name of the match criterion. |
| SourceId | Integer | The ID of the log source. |
| Type | Integer | The match criterion type code. |
| UserId | String | The ID of the creator. |

**Error codes**

For more information about the error codes that this operation can return, see Error codes.

**Examples**

Sample requests

```
https://auditprivate.[ RegionId].example.com/?Action=CreateLogFilter &LogType=5 &Name=test &SourceId=10000 &Type=1 &Alertable=null &Defaultable=null &EndTime=null &EventRiskLevel=null &EventType=info &LogAction=null &LogInitiatior=null &LogOutcome=null &LogReason=null &LogTarget=null &Query=null &StartTime=1 &<Common request parameters>
```

Sample responses (JSON format) `{`

```json
 "RequestId":"4320E3EC-AAC0-46BB-9814-4E1DBE550F76",
 "LogFilter":{
  "Type":1,
  "UserId":1519714049632764,
  "CreateTime":1519813584985,
  "SourceId":10000,
  "LogType":5,
  "Id":10109,
  "Name":"test2",
  "Defaultable":false
```

`}` `}`

### 5.5 DescribeLogFilter

**Description**

You can call this operation to query audit log filter criteria.

**Request parameters**

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeLogFilter. |

| SourceId | String | No | The ID of the log source. Default value: null. If you use the default setting, the log source with ID null is used. |
|---|---|---|---|
| LogType | String | No | The type of the log. |
| Type | Integer | Yes | The type of the filter criteria. Valid values: 1: indicates filtering by log. 2: indicates filtering by audit event. |
| Count | Integer | No | The number of returned records. |

**Response parameters**

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| LogFilterList | Array | A list of filter criteria. For more information, see the following parameter descriptions. |
| Alertable | Boolean | Indicates whether alerting is enabled. |
| CreateTime | Long | The time when the criterion was created. |
| Defaultable | Boolean | Indicates whether the criterion is a default filter criterion. |
| EndTime | Long | The time when the query was complete. |
| EventRiskLevel | Integer | The ID of the event risk level. |
| EventType | Integer | The ID of the event type. |
| Id | Integer | The ID of the filter criterion. |
| LogType | Integer | The type of the log. |
| Name | String | The name of the filter criterion. |
| LogAction | String | The action to be performed. |
| LogInitiatior | String | The user that sent the log query. |
| LogOutcome | String | The result. |
| LogReason | String | The reason. |
| LogTarget | String | The target. |
| Query | String | The keywords for query. |

| StartTime | Long | The start time of the time frame specified for query. |
|---|---|---|
| SourceId | Integer | The ID of the log source. |
| Type | Integer | The code of the filter criterion type. |
| UserId | String | The ID of the creator. |

**Error codes**

For more information about the error codes that this operation can return, see Error codes.

**Examples**

Sample requests

```
https://auditprivate.[ RegionId].example.com/?Action=DescribeLogFilter &Count=10 &LogType=1 &SourceId=1 &Type=null &<Common request parameters>
```

Sample responses (JSON format) `{`

```json
 "RequestId":"6893FB2A-4D4D-4F3B-9963-59D9B9435FDD",
 "LogFilterList":[
```

`{`

```json
              "query":"",
   "EndTime":0,
   "EventType":1,
   "SourceId":10000,
   "CreateTime":1522315869000,
   "LogType":5,
   "Starttime": 0,
   "EventRiskLevel":0,
   "LogTarget":"",
   "Name":"test2",
   "Type":1,
   "LogAction":"",
   "LogInitiatior":"",
   "UserId":"1519714049632764",
   "LogReason":"",
   "LogOutcome":"",
   "Alertable":true,
   "Id":10130,
   "Defaultable":true
```

`}` `]` `}`

### 5.6 DeleteLogFilter

You can call this operation to delete audit log search conditions.

**Request parameters**

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DeleteLogFilter. |
| Id | Integer | No | The ID of the search condition. |

**Response parameters**

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |

**Error codes**

For more information about the error codes that this operation can return, see Error codes.

**Examples**

Sample requests

```
https://auditprivate.[ RegionId].example.com/?Action=DeleteLogFilter &Id=10001 &<Common request parameters>
```

Sample responses (JSON format) `{`

```json
 "RequestId":"4320E3EC-AAC0-46BB-9814-4E1DBE550F76"
```

`}`

### 5.7 CreateReceiver

**Description**

Creates an alert recipient for audit events.

**Request parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to CreateReceiver |
| Contact | String | Yes | The contact information about the alert recipient. |

| LogType | String | Yes | The type of log. |
|---|---|---|---|
| Name | String | Yes | The name of the alert recipient. |
| Type | Integer | Yes | The code of the alert receiving method. Set the value to 1. In this case, alerts are sent through emails. |
| EventRiskLevel | String | Yes | The code of the risk level. |
| SourceId | String | Yes | The ID of the log source. |

**Response parameters**

| Parameter | Type | Description |
|---|---|---|
| RequestId | String | The ID of the request. |
| Receiver | Struct | The created alert recipient. For more information, see the following parameter descriptions. |
| Contact | String | The contact information about the alert recipient. |
| CreateTime | Long | The time when the alert recipient was created. |
| EventRiskLevel | Integer | The code of the risk level. |
| Id | Integer | The ID of the alert recipient. |
| LogType | Integer | The type of log. |
| Name | String | The name of the alert recipient. |
| SourceId | Integer | The ID of the log source. |
| SourceName | String | The name of the log source. |
| Type | Integer | The code of the alert receiving method. |

**Error codes**

For a list of error codes, see Error codes.

**Examples**

Sample requests

```
https://auditprivate.[RegionId].example.com/?Action=CreateReceiver &Contact=test@example.com &EventRiskLevel=1 &LogType=5 &Name=test &SourceId=100000 &Type=1 &<Common request parameters>
```

Sample success responses in JSON format `{`

```json
    "RequestId":"452C6406-D60E-4E20-A2D3-2AF1BACD24FC",
    "Receiver":{
        "Type":1,
        "CreateTime":1519817388511,
        "SourceId":10000,
        "LogType":5,
        "SourceName":"DRDS Rtools audit logs",
        "Id":10010,
        "EventRiskLevel":1,
        "Name":"test",
        "Contact":"test@example.com"
```

`}` `}`

### 5.8 DescribeReceiver

**Description**

Queries information about alert recipients.

**Request parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeReceiver. |
| PageSize | String | No | The number of entries to return on each page. |
| CurrentPage | String | No | The number of the page to return. |
| Contact | String | No | The contact information about the alert recipient. |
| LogType | String | No | The type of log. |
| Name | String | No | The name of the alert recipient. |

| EventRiskLevel | String | No | The code of the risk level. |
|---|---|---|---|
| SourceId | String | No | The ID of the log source. Default value: null. If you do not specify this parameter, the log source ID is null. |
| SourceName | String | No | The name of the log source. |

**Response parameters**

| Parameter | Type | Description |
|---|---|---|
| RequestId | String | The ID of the request. |
| CurrentPage | Integer | The page number of the returned page. |
| PageSize | Integer | The number of entries returned per page. |
| TotalCount | Integer | The number of entries returned. |
| ReceiverList | Array | The list of alert recipients. For more information, see the following parameter descriptions. |
| Contact | String | The contact information about the alert recipient. |
| CreateTime | Long | The time when the alert recipient was created. |
| EventRiskLevel | Integer | The code of the risk level. |
| Id | Integer | The ID of the alert recipient. |
| LogType | Integer | The type of log. |
| Name | String | The name of the alert recipient. |
| SourceId | Integer | The ID of the log source. |
| SourceName | String | The name of the log source. |
| Type | Integer | The code of the alert receiving method. |

**Error codes**

For a list of error codes, see Error codes.

**Examples**

Sample requests

```
https://auditprivate.[RegionId].example.com/?Action=DescribeReceiver &Contact=null &CurrentPage=1 &EventRiskLevel=1 &LogType=1 &Name=null &PageSize=100 &SourceId=1 &SourceName=null &<Common request parameters>
```

Sample success responses in JSON format `{`

```json
    "RequestId":"AF012FF0-3851-4132-A7A8-3F77DE40BF91",
    "TotalCount":2,
    "PageSize":20,
    "CurrentPage":1,
    "ReceiverList":[
```

`{`

```json
            "Type":1,
            "CreateTime":1519817388511,
            "SourceId":10000,
            "LogType":5,
            "SourceName":"DRDS Rtools audit logs",
            "Id":10010,
            "EventRiskLevel":1,
            "Name":"test",
            "Contact":"test@example.com"
```

`}` `]` `}`

### 5.9 DeleteReceiver

**Description**

You can call this operation to delete an audit event alert recipient.

**Request parameters**

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DeleteReceiver. |
| Id | Integer | Yes | The ID of the alert recipient. |

**Response parameters**

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |

**Error codes**

For more information about the error codes that this operation can return, see Error codes.

**Examples**

Sample requests

```
https://auditprivate.[ RegionId].example.com/?Action=DeleteReceiver &Id=10000 &<Common request parameters>
```

Sample responses (JSON format) `{`

```json
   "RequestId":"452C6406-D60E-4E20-A2D3-2AF1BACD24FC"
```

`}`

### 5.10 CreateRule

**Description**

You can call this operation to create an audit rule.

**Request parameters**

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to CreateRule. |
| Alertable | Boolean | Yes | Indicates whether alerting is enabled. |
| EventTypeId | Integer | Yes | The audit event type code. |
| LogType | Integer | Yes | The log type code. |
| RuleName | String | Yes | The name of the audit rule. |
| AlertActionList | String | No | The alert recipient. Separate multiple alert recipients with commas (,). |
| EndTime | String | No | The end time in timestamp format. |
| Expression | String | No | The audit rule expression. |
| LogAction | String | No | The audit target. |
| LogInitiatior | String | No | The user that initiates the security audit. |

| LogOutcome | String | No | The auditing result. |
|---|---|---|---|
| LogReason | String | No | The reason. |
| LogTarget | String | No | The target. |
| Mark | String | No | Remarks. |
| StartTime | String | No | The time when the security audit starts, in timestamp format. |
| EventRiskLevel | String | Yes | The risk level code. |
| SourceId | String | Yes | The ID of the log source. |

**Response parameters**

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| Rule | Struct | The created audit rule. For more information, see the following parameter descriptions. |
| AlertActions | String | The alert recipient. |
| CreateTime | Long | The time at which the audit rule was created. |
| EventRiskLevel | Integer | The risk level code. |
| Enabled | Boolean | Indicates whether the rule is enabled. |
| Alertable | Boolean | Indicates whether alerting is enabled. |
| EventTypeId | Integer | The audit event type ID. |
| EventTypeName | String | The type of the audit event. |
| Id | Integer | The ID of the audit rule. |
| LogType | Integer | The type of the log. |
| Name | String | The name of the audit rule. |
| Reserved | Boolean | Indicates whether the rule is reserved. |
| SourceId | Integer | The ID of the log source. |
| SourceName | String | The name of the log source. |

**Error codes**

For more information about the error codes that this operation can return, see Error codes.

**Examples**

Sample requests

```
https://auditprivate.[ RegionId].example.com/?Action=CreateRule &Alertable=false &EventRiskLevel=1 &EventTypeId=10003 &LogType=5 &RuleName=test &SourceId=10000 &AlertActionList=null &EndTime=null &Expression=null &LogAction=null &LogInitiatior=null &LogOutcome=null &LogReason=null &LogTarget=null &Remark=null &StartTime=1 &<Common request parameters>
```

Sample responses (JSON format) `{`

```json
 "RequestId":"A9B34E07-02E2-4DC7-8A30-27D59E940279",
 "Rule ":[
  "SourceId":10000,
  "CreateTime":1519816442199,
  "LogType":5,
  "Enable": true,
  "EventTypeId":10003,
  "SourceName":"DRDS Rtools audit log",
  "AlertActions":"",
  "Name":"test2",
  "EventTypeName":"Create",
  "Alertable":false,
  "Id":25765,
  "EventRiskLevel":1,
  "Reserved":false
```

`}` `}`

### 5.11 DescribeRule

**Description**

You can call this operation to query audit rules.

**Request parameters**

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeRule. |

| PageSize | String | No | The maximum number of records displayed on a page. |
|---|---|---|---|
| CurrentPage | String | No | The current page number. |
| Alertable | Boolean | No | Indicates whether alarming is enabled |
| Enabled | Boolean | No | Indicates whether the rule is enabled. |
| EventTypeId | Integer | No | The audit event type code. |
| LogType | Integer | No | The log type code |
| Expression | String | No | The expression of the audit rule. |
| EventRiskLevel | String | No | The risk level code. |
| SourceId | String | No | The ID of the log source. Default value: null. If you use the default setting, the log source with ID null is used. |

**Response parameters**

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| CurrentPage | Integer | The current page number. |
| PageSize | Integer | The maximum number of records displayed on a page. |
| TotalCount | Integer | The number of returned records. |
| RuleList | Struct | A list of audit rules. For more information, see the following parameter descriptions. |
| AlertActions | String | The alarm recipient. |
| CreateTime | Long | The time when the audit rule was created. |
| EventRiskLevel | Integer | The risk level code. |
| Enabled | Boolean | Indicates whether the rule is enabled. |
| Alertable | Boolean | Indicates whether alerting is enabled. |
| EventTypeId | Integer | The ID of the event type. |
| EventTypeName | String | The name of the event type. |
| Expression | String | The expression of the audit rule. |
| SourceName | String | The name of the log source. |

| Id | Integer | The ID of the audit rule. |
|---|---|---|
| LogType | Integer | The type of the log. |
| Name | String | The name of the audit rule. |
| Reserved | Boolean | Indicates whether the audit rule is reserved. |

**Error codes**

For more information about the error codes that this operation can return, see Error codes.

**Examples**

Sample requests

```
https://auditprivate.[ RegionId].example.com/?Action=DescribeRule &Alertable=true &CurrentPage=1 &Enabled=true &EventRiskLevel=1 &EventTypeId=1000 &Expression=null &LogType=5 &PageSize=100 &SourceId=100000 &<Common request parameters>
```

Sample responses (JSON format) `{`

```json
 "RequestId":"A6204082-0FD3-4F9A-AFAD-1E2E3F56748A",
 "TotalCount":16,
 "PageSize":20,
 "CurrentPage":1,
 "RuleList":[
```

`{`

```json
   "Expression":"( initiator= \"1\" OR initiator= \"2\" OR initiator= \"3\" ) AND ( t
arget INCLUDE \"4\" OR target INCLUDE \"5\" OR target INCLUDE \"6\" ) AND ( action RE GEX \"7\" OR action REGEX \"8\" OR action REGEX \"9\" ) AND ( outcome = \"aa\" ) AND ( reason = \"bb\" )",
   "CreateTime":1513156159000,
   "Type":1,
   "Enable": true,
   "EventTypeName":"1982",
   "EventTypeId":10208,
   "Alertable":true,
   "Id":25740,
   "AlertActions":"",
   "EventRiskLevel":1,
   "Name":"test2",
   "Reserved":false
```

`}` `]` `}`

### 5.12 EnableRule

**Description**

You can call this operation to enable an audit rule.

**Request parameters**

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to EnableRule. |
| Id | Integer | Yes | The ID of the audit rule. |

**Response parameters**

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |

**Error codes**

For more information about the error codes that this operation can return, see Error codes.

**Examples**

Sample requests

```
https://auditprivate.[ RegionId].example.com/?Action=EnableRule &Id=10001 &<Common request parameters>
```

Sample responses (JSON format) `{`

```json
 "RequestId":"A9B34E07-02E2-4DC7-8A30-27D59E940279"
```

`}`

### 5.13 DisableRule

**Description**

You can call this operation to disable an audit rule.

**Request parameters**

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DisableRule. |

| Id | Integer | Yes | The ID of the audit rule. |
|---|---|---|---|

**Response parameters**

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |

**Error codes**

For more information about the error codes that this operation can return, see Error codes.

**Examples**

Sample requests

```
https://auditprivate.[ RegionId].example.com/?Action=DisableRule &Id=10001 &<Common request parameters>
```

Sample responses (JSON format) `{`

```json
 "RequestId":"A9B34E07-02E2-4DC7-8A30-27D59E940279"
```

`}`

### 5.14 DeleteRule

**Description**

You can call this operation to delete an audit rule.

**Request parameters**

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DeleteRule. |
| Id | Integer | Yes | The ID of the audit rule. |

**Response parameters**

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |

**Error codes**

For more information about the error codes that this operation can return, see Error codes.

**Examples**

Sample requests

```
https://auditprivate.[ RegionId].example.com/?Action=DeleteRule &Id=10000 &<Common request parameters>
```

Sample responses (JSON format) `{`

```json
 "RequestId":"A9B34E07-02E2-4DC7-8A30-27D59E940279"
```

`}`

### 5.15 CreateTask

**Description**

You can call this operation to create an export task.

**Request parameters**

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to CreateTask. |
| Type | Integer | Yes | The type of the export task. |
| Param | String | Yes | The query parameters in JSON format. For information about the parameter format, see the following sample request. |

**Response parameters**

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| Task | Struct | The created export task. For more information, see the following parameter descriptions. |
| CreateTime | Long | The time when the export task was created. |
| Id | Integer | The ID of the export task. |
| Param | String | The query parameters. |
| Status | Integer | The status of the export task. Valid values: 1: indicates that the task is in preparation. 2: indicates that the task is being executed. 3: indicates that the task is complete. 4: indicates that the task has failed. |

| Result | String | The task execution result. |
|---|---|---|
| Type | Integer | The type of the export task. |

**Error codes**

For more information about the error codes that this operation can return, see Error codes.

**Examples**

Sample requests

```
https://auditprivate.[ RegionId].example.com/?Action=CreateTask &Param={"logType":4,"sourceId":"","q":"","name":"Query all","from":1526987580000,"to":1527073980000} &Type=1 &<Common request parameters>
```

Sample responses (JSON format) `{`

```json
   "RequestId":"5529324A-7E32-414F-8ADD-B7C3FF32EB6E",
 "Task":[
  "Status":1,
  "Type":1,
  "CreateTime":1519814652404,
  "Param":"{}",
  "Id":10033,
  "Result":""
```

`}` `}`

### 5.16 DescribeTask

**Description**

Queries information about export tasks.

**Request parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeTask. |
| PageSize | String | No | The number of entries to return on each page. |
| CurrentPage | String | No | The number of the page to return. |
| Status | Integer | No | The status of the export task. |
| Type | Integer | No | The type of the export task. |

**Response parameters**

| Parameter | Type | Description |
|---|---|---|
| RequestId | String | The ID of the request. |
| CurrentPage | Integer | The page number of the returned page. |
| PageSize | Integer | The number of entries returned per page. |
| TotalCount | Integer | The number of entries returned. |
| TaskList | Array | The list of export tasks. For more information, see the following parameter descriptions. |
| CreateTime | Long | The time when the export task was created. |
| StartTime | Long | The time when the export task started. |
| EndTime | Long | The time when the export task ended. |
| Id | Integer | The ID of the export task. |
| Param | String | The query parameters. |
| Status | Integer | The status of the export task. Valid values: 1: indicates that the task is in preparation. 2: indicates that the task is running. 3: indicates that the task is complete. 4: indicates that the task failed. |
| Result | String | The result of the export task. |
| Type | Integer | The type of the export task. |

**Error codes**

For a list of error codes, see Error codes.

**Examples**

Sample requests

```
https://auditprivate.[RegionId].example.com/?Action=DescribeTask &CurrentPage=1 &PageSize=100 &Status=2 &Type=1 &<Common request parameters>
```

Sample success responses in JSON format `{`

```json
    "RequestId":"2CF939E5-A0EF-4C0F-A761-CBC7DF4DE1BD",
    "TotalCount":18,
    "PageSize":20,
    "CurrentPage":1,
    "TaskList":[
```

`{`

```json
                  "Status":1,
            "Type":1,
            "CreateTime":1519814652404,
            "StartTime":1519814652000,
                  "EndTime":1519814653000,
            "Param":"{}",
            "Id":10033,
            "Result":"{\"url\":\"http://security-auditlog-archive-dev1.oss-cn-
hangzhou.example.com/download/20180228184412_243797.log? Expires=1519901052&OSSAccessKeyId=<yourAccessKeyId>&Signature=xxxx%xxxx%3D\"}"
```

`}` `]` `}`

### 5.17 DeleteTask

**Description**

You can call this operation to delete an export task.

**Request parameters**

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DeleteTask. |
| Id | Integer | Yes | The ID of the export task. |

**Response parameters**

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |

**Error codes**

For more information about the error codes that this operation can return, see Error codes.

**Examples**

Sample requests

```
https://auditprivate.[ RegionId].example.com/?Action=DeleteTask &Id=10000 &<Common request parameters>
```

Sample responses (JSON format) `{`

```json
   "RequestId":"5529324A-7E32-414F-8ADD-B7C3FF32EB6E"
```

`}`

### 5.18 DescribeSetting

**Description**

You can call this operation to query the system parameter settings of security audit.

**Request parameters**

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeSetting. |

**Response parameters**

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| SettingList | Array | The list of system parameters. For more information, see the following parameter descriptions. |
| Id | Integer | The system parameter ID. |
| Name | String | The system parameter name. |
| Remark | String | The system parameter description. |
| Type | Integer | The data type. |
| UpdateTime | Long | The last modification time. |
| Value | String | The system parameter value. |

**Error codes**

For more information about the error codes that this operation can return, see Error codes.

**Examples**

Sample requests

```
https://auditprivate.[ RegionId].example.com/?Action=DescribeSetting &<Common request parameters>
```

Sample responses (JSON format) `{`

```json
 "RequestId":"0C4EF12F-9736-429F-9A7A-7C0807BFBA91",
 "SettingList":[
```

`{`

```json
   "Type":2,
   "Value":"2000",
   "UpdateTime":1517566573000,
   "Id":10004,
   "Name":"max_day_alert_number",
   "Remark":"The maximum number of alerts reported every day."
```

`}` `]` `}`

### 5.19 ModifySetting

**Description**

You can call this operation to modify the system parameter settings of Security Audit.

**Request parameters**

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to ModifySetting. |
| Name | String | Yes | The name of the system parameter. |
| Value | String | Yes | The value of the system parameter. |

**Response parameters**

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |

**Error codes**

For more information about the error codes that this operation can return, see Error codes.

**Examples**

Sample requests

```
https://auditprivate.[ RegionId].example.com/?Action=ModifySetting &Name=max_day_alert_number &Value=2000 &<Common request parameters>
```

Sample responses (JSON format) `{`

```json
 "RequestId":"0C4EF12F-9736-429F-9A7A-7C0807BFBA91"
```

`}`

### 5.20 DescribeLogType

**Description**

You can call this operation to obtain a list of log types.

**Request parameters**

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeLogType. |

**Response parameters**

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| LogTypeList | Array | The list of log types. For more information, see the following parameter descriptions. |
| Type | Integer | The code of the log type. |
| Remark | String | The name of the log type. |

**Error codes**

For more information about the error codes that this operation can return, see Error codes.

**Examples**

Sample requests

```
https://auditprivate.[ RegionId].example.com/?Action=DescribeLogType &CurrentPage=1 &Enabled=true &LogType=1 &PageSize=100 &<Common request parameters>
```

Sample responses (JSON format) `{`

```json
   "RequestId":"DD601BAA-4B2A-4CB3-954A-4A09A8771233",
 "LogTypeList":[
```

`{`

```json
   "Type":1,
   "Remark":"Database"
```

`}` `]` `}`

### 5.21 DescribeLogSource

**Description**

You can call this operation to query log source information.

**Request parameters**

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeLogSource. |
| PageSize | String | No | The maximum number of records displayed on a page. |
| CurrentPage | String | No | The current page number. |
| Enabled | Boolean | No | Indicates whether the log source is enabled. |
| LogType | Integer | No | The log type code. |

**Response parameters**

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| CurrentPage | Integer | The current page number. |
| PageSize | Integer | The maximum number of records displayed on a page. |
| TotalCount | Integer | The number of returned records. |
| LogSourceList | Array | A list of log sources.For more information, see the following parameter descriptions. |
| Alertable | Boolean | Indicates whether alerting is enabled. |
| Code | String | The log source code. |

| CreateTime | Long | The time when the log source was created. |
|---|---|---|
| Enabled | Boolean | Indicates whether the log source is enabled. |
| Id | Integer | The ID of the log source. |
| LogType | Integer | The log type code. |
| Name | String | The name of the log source. |

**Error codes**

For more information about the error codes that this operation can return, see Error codes.

**Examples**

Sample requests

```
https://auditprivate.[ RegionId].example.com/?Action=DescribeLogSource &CurrentPage=1 &Enabled=true &LogType=1 &PageSize=100 &<Common request parameters>
```

Sample responses (JSON format) `{`

```json
 "RequestId":"CEF1CFC8-53E9-45B7-B3FF-730636A5B430",
 "CurrentPage":1,
 "TotalCount":13,
 "PageSize":1000,
 "LogSourceList":[
```

`{`

```json
   "CreateTime":1497686376000,
   "LogType":5,
   "Enable": true,
   "Alertable":false,
   "Id": "10000",
   "Code":"drds-rtools",
   "Name":"DRDS Rtools audit log"
```

`}` `]` `}`

### 5.22 DescribeLogCountStat

**Description**

You can call this operation to query raw log statistics.

**Request parameters**

| Name | Type | Required | Description |
|---|---|---|---|

| Action | String | Yes | The operation that you want to perform. Set the value to DescribeLogCountStat. |
|---|---|---|---|
| EndTime | String | No | The end time of the time frame specified for query, in timestamp format. |
| LogTypeList | String | No | The log type code. Separate multiple log types with commas (,). |
| StartTime | String | No | The start time of the time frame specified for query, in timestamp format. |

**Response parameters**

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| StatList | Array | A list of raw log statistics. For more information, see the following parameter descriptions. |
| LogType | Integer | The log type code. |
| StatItemList | Array | The raw log statistics. For more information, see the following parameter descriptions. |
| Capacity | Float | The storage space usage. |
| Count | Integer | The number of raw log entries. |
| Time | Long | The time when the statistics were collected, in timestamp format. |

**Error codes**

For more information about the error codes that this operation can return, see Error codes.

**Examples**

Sample requests

```
https://auditprivate.[ RegionId].example.com/?Action=DescribeLogCountStat &EndTime=1517630399000 &LogTypeList=1,2,3 &StartTime=1517414400000 &<Common request parameters>
```

Sample responses (JSON format) `{`

```json
 "RequestId":"A633CC4C-914E-49D5-8AC2-1A0B82796E66",
 "StatList":[
```

`{`

```json
   "StatItemList":[
```

`{`

```json
     "Time":1517414400000,
     "Count":215239,
     "capacity":356106.0
```

`}` `],`

```json
   "LogType":1
```

`}` `]` `}`

### 5.23 DescribeLog

**Description**

Queries the details about raw logs.

**Request parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeLog. |
| PageSize | String | No | The number of entries to return on each page. |
| CurrentPage | String | No | The number of the page to return. |
| EndTime | String | No | The end of the time range to query. This value is a timestamp. |
| Query | String | No | The keywords for query. |
| SourceId | String | No | The ID of the log source. Default value: null. If you do not specify this parameter, the log source ID is null. |
| StartTime | String | No | The start of the time range to query. This value is a timestamp. |

**Response parameters**

| Parameter | Type | Description |
|---|---|---|
| RequestId | String | The ID of the request. |

| CurrentPage | Integer | The page number of the returned page. |
|---|---|---|
| PageSize | Integer | The number of entries returned per page. |
| TotalCount | Integer | The number of entries returned. |
| LogList | Array | The list of raw logs. For more information, see the following parameter descriptions. |
| LogTime | Long | The time when the log was generated. |
| Source | String | The name of the log source. |
| ColumnList | Array | The list of log details. For more information, see the following parameter descriptions. |
| Key | String | The name of the column. |
| Value | String | The value of the column. |
| TokenList | Array | The list of tokens. For more information, see the following descriptions. |
| Delimit | Boolean | Indicates whether the token is limited. |
| Work | String | The fixed value of the token. |
| HistogramList | Array | The information that indicates the number of raw logs. For more information, see the following descriptions. |
| Completed | Boolean | Indicates whether all of the raw logs that are generated within the specified time range have been collected. If not, the Count parameter shows an estimated value. |
| Count | Integer | The number of audit events. |
| EndTime | Long | The end time. |
| StartTime | Long | The start time. |

**Error codes**

For a list of error codes, see Error codes.

**Examples**

Sample requests

```
https://auditprivate.[RegionId].example.com/?Action=DescribeLog &CurrentPage=1 &EndTime=1517630399000 &PageSize=100 &Query=null &SourceId=2 &StartTime=1517414400000 &<Common request parameters>
```

Sample success responses in JSON format `{`

```json
      "RequestId":"DD601BAA-4B2A-4CB3-954A-4A09A8771233",
      "TotalCount":0,
    "PageSize":20,
    "CurrentPage":1,
      "HistogramList":[
```

`{`

```json
            "StartTime": 1517414400000,
            "EndTime": 1517630399000,
              "Count" : 1,
              "Completed" : true
```

`}` `],`

```json
    "LogList":[
```

`{`

```json
            "ColumnList" : [
```

`{`

```json
                    "TokenList" : [
```

`{`

```json
                            "Delimit" : true,
                              "Word" : "a"
```

`}` `],`

```json
                    "Value" : "delete",
                      "Key" : "action"
```

`}` `],`

```json
              "Source" : 1,
              "LogTime" : 1517630399000
```

`}` `]` `}`

### 5.24 DescribeEventRisk

**Description**

You can call this operation to query the risk level information of an audit event.

**Request parameters**

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeEventRisk. |

**Response parameters**

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| EventRiskList | Array | The list of event risk levels. For more information, see the following parameter descriptions. |
| Level | Integer | The code of the risk level. |
| Name | String | The name of the risk level. |

**Error codes**

For more information about the error codes that this operation can return, see Error codes.

**Examples**

Sample requests

```
https://auditprivate.[ RegionId].example.com/?Action=DescribeEventRisk &<Common request parameters>
```

Sample responses (JSON format) `{`

```json
 "RequestId":"802DD13D-AEDE-4BD0-86B3-2F44D6D867A0",
 "RiskList":[
```

`{`

```json
   "Level":0,
   "Name":"Global risk"
```

`}` `]` `}`

### 5.25 DescribeEventRiskStat

**Description**

Queries audit event statistics by risk level.

**Request parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeEventRiskStat. |
| EndTime | String | No | The end of the time range to query. This value is a timestamp. |

| LogTypeList | String | No | The code of the log type. Separate multiple codes of log types with commas (,). |
|---|---|---|---|
| StartTime | String | No | The start of the time range to query. This value is a timestamp. |

**Response parameters**

| Parameter | Type | Description |
|---|---|---|
| RequestId | String | The ID of the request. |
| StatList | Array | The list of audit event statistics. For more information, see the following parameter descriptions. |
| LogType | Integer | The code of the log type. |
| StatItemList | Array | The statistical data. For more information, see the following parameter descriptions. |
| Count | Integer | The number of audit events. |
| Capacity | Float | The storage space usage. |
| EventRiskLevel | Integer | The code of the risk level. |

**Error codes**

For a list of error codes, see Error codes.

**Examples**

Sample requests

```
https://auditprivate.[RegionId].example.com/?Action=DescribeEventRiskStat &EndTime=1517630399000 &LogTypeList=1,2,3 &StartTime=1517414400000 &<Common request parameters>
```

Sample success responses in JSON format `{`

```json
    "RequestId":"63DDF633-1394-4AEB-A8E3-6467BC23D78D",
    "StatList":[
```

`{`

```json
            "LogType":1,
            "StatDataList":[
```

`{`

```json
                    "EventRiskLevel":3,
                    "Count":100
```

`}` `]` `}` `]` `}`

### 5.26 DescribeEventTypeStat

**Description**

You can call this operation to query audit event statistics by event type.

**Request parameters**

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeEventTypeStat. |
| EndTime | String | No | The end time of the time frame specified for query, in timestamp format. |
| LogTypeList | String | No | The log type code. Separate multiple log types with commas (,). |
| StartTime | String | No | The start time of the time frame specified for query, in timestamp format. |

**Response parameters**

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| StatList | Array | A list of audit event statistics. For more information, see the following parameter descriptions. |
| Capacity | Float | The storage space usage. |

| Reserved | Boolean | Indicates whether the audit event type is a default audit event type. |
|---|---|---|
| Count | Integer | The number of audit events. |
| Id | Integer | The audit event type ID. |
| Name | String | The audit event type name. |

**Error codes**

For more information about the error codes that this operation can return, see Error codes.

**Examples**

Sample requests

```
https://auditprivate.[ RegionId].example.com/?Action=DescribeEventTypeStat &EndTime=1517630399000 &LogTypeList=1,2,3 &StartTime=1517414400000 &<Common request parameters>
```

Sample responses (JSON format) `{`

```json
 "RequestId":"75F7A5A7-E9E4-476C-8D09-93B00D7EB120",
 "StatList":[
```

`{`

```json
   "Count":634,
   "Id":10208,
   "Name":"1982"
```

`}` `]` `}`

### 5.27 DescribeEventCountStat

**Description**

You can call this operation to query audit event statistics.

**Request parameters**

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeEventCountStat. |
| EndTime | String | No | The end time of the time frame specified for query, in timestamp format. |

| LogTypeList | String | No | The log type code. Separate multiple log types with commas (,). |
|---|---|---|---|
| StartTime | String | No | The start time of the time frame specified for query, in timestamp format. |

**Response parameters**

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| StatList | Array | A list of audit event statistics. For more information, see the following parameter descriptions. |
| LogType | Integer | The log type code. |
| StatItemList | Array | The audit event information. For more information, see the following parameter descriptions. |
| Capacity | Float | The storage space usage. |
| Count | Integer | The number of audit events. |
| Time | Long | The time when the statistics were collected, in timestamp format. |

**Error codes**

For more information about the error codes that this operation can return, see Error codes.

**Examples**

Sample requests

```
https://auditprivate.[ RegionId].example.com/?Action=DescribeEventCountStat &EndTime=1517630399000 &LogTypeList=1,2,3 &StartTime=1517414400000 &<Common request parameters>
```

Sample responses (JSON format) `{`

```json
 "RequestId":"63DDF633-1394-4AEB-A8E3-6467BC23D78D",
 "StatList":[
```

`{`

```json
   "Type":1,
   "StatDataList":[
```

`{`

```json
     "Capacity":55881.0,
     "Time":1519228800000,
     "Count":100
```

`}` `]` `}` `]` `}`

### 5.28 DescribeEvent

**Description**

Queries audit event details.

**Request parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeEvent. |
| PageSize | String | No | The number of entries to return on each page. |
| CurrentPage | String | No | The number of the page to return. |
| Alertable | Boolean | No | Specifies whether an alert is triggered. |
| EndTime | String | No | The end of the time range to query. This value is a timestamp. |
| EventRiskLevel | Integer | No | The code of the risk level. |
| EventTypeId | Long | No | The ID of the audit event type. |
| Keyword | String | No | The keywords for query. |
| LogAction | String | No | The operation. |
| LogInitiatior | String | No | The initiator. |
| LogOutcome | String | No | The result. |
| LogReason | String | No | The reason. |

| LogTarget | String | No | The physical machine on which the operation is performed. |
|---|---|---|---|
| LogType | Integer | No | The code of the log type. |
| RuleId | Long | No | The ID of the audit rule. |
| SourceId | String | No | The ID of the log source. Default value: null. If you do not specify this parameter, the log source ID is null. |
| StartTime | String | No | The start of the time range to query. This value is a timestamp. |

**Response parameters**

| Parameter | Type | Description |
|---|---|---|
| RequestId | String | The ID of the request. |
| CurrentPage | Integer | The page number of the returned page. |
| PageSize | Integer | The number of entries returned per page. |
| TotalCount | Integer | The number of entries returned. |
| EventList | Array | The list of audit events. For more information, see the following parameter descriptions. |
| CreateTime | Long | The time when the audit event was created. |
| EventRiskLevel | Integer | The code of the risk level. |
| EventTypeId | Integer | The ID of the audit event type. |
| EventTypeName | String | The name of the audit event type. |
| EventTypeReserved | Boolean | Indicates whether the audit event type is the default audit event type. |
| Id | Integer | The ID of the audit event. |
| LogAction | String | The operation. |
| LogContent | String | The log content. |
| LogInitiatior | String | The initiator. |
| LogMd5 | String | The MD5 value of the log file. |
| LogOutcome | String | The result. |
| LogReason | String | The reason. |
| LogSha256 | String | The SHA-256 value of the log file. |

| LogTarget | String | The physical machine on which the operation is performed. |
|---|---|---|
| LogTime | Long | The time when the log was generated. |
| LogType | Integer | The code of the log type. |
| Receivers | String | The alert recipient. |
| RuleId | Integer | The ID of the audit rule. |
| SourceId | Integer | The ID of the log source. |
| SourceName | String | The name of the log source. |
| HistogramList | Array | The information that indicates the number of audit events. For more information, see the following descriptions. |
| Completed | Boolean | Indicates whether all of the audit events that occurred within the specified time range have been collected. If not, the Count parameter shows an estimated value. |
| Count | Integer | The number of audit events. |
| EndTime | Long | The end time. |
| StartTime | Long | The start time. |

**Error codes**

For a list of error codes, see Error codes.

**Examples**

Sample requests

```
https://auditprivate.[RegionId].example.com/?Action=DescribeEvent &Alertable=yes &CurrentPage=100 &EndTime=1517414400000 &EventRiskLevel=null &EventTypeId=1 &Keyword=null &LogAction=null &LogInitiatior=null &LogOutcome=null &LogReason=null &LogTarget=null &LogType=2 &PageSize=1 &RuleId=null &SourceId=1 &SourceIp=x.x.x.x &StartTime=1517630399000 &<Common request parameters>
```

Sample success responses in JSON format `{`

```json
    "RequestId":"DD601BAA-4B2A-4CB3-954A-4A09A8771233",
    "TotalCount":0,
    "PageSize":20,
    "CurrentPage":1,
      "HistogramList":[
```

`{`

```json
            "StartTime": 1517414400000,
            "EndTime": 1517630399000,
            "Count" : 1,
            "Completed" : true
```

`}` `],`

```json
    "EventList":[
```

`{`

```json
            "LogInitiatior":"histie",
            "LogAction":"insert betorcinol into(unnervous,dreadingly)
value('rashti','interscapular');",
            "LogMd5":"",
            "SourceId":11140,
            "CreateTime":1519803668679,
            "RuleId":25728,
            "LogTime":1519803664000,
            "Receivers":"2:<test01@example.com>;xxx:<test02@example.com>",
            "LogType":1,
            "EventTypeId":10208,
            "SourceName":"1585",
            "LogReason":"",
            "LogTarget":" abdominales",
            "LogOutcome":"0",
            "LogSha256":"",
            "LogContent":"{\"_action\":\"insert betorcinol into(unnervous,dreadingly)
value('rashti','interscapular');\",\"db\":\" abdominales\",\"origin_time\":\"3189556\",\"hash\":\"1906992916\",\"_initiatior\":\"his e\",\"return_rows\":\"14\",\"ip\":\"x.x.x.x\",\"isbind\":\"1\",\"time\":1519803664000,\ atency\":\"533\",\"sql\":\"insert betorcinol into(unnervous,dreadingly) value('rashti','interscapular');\",\"fail\":\"0\",\"_outcome\":\"0\",\"check_rows\":\"5 \",\"update_rows\":\"13860\",\"tid\":\"20794\",\"_target\":\" abdominales\",\"user\":\"histie\",\"_access_time\":1519803664000}",
            "EventTypeName":"1982",
            "Id":151980366867940****,
            "EventRiskLevel":1
```

`}` `]` `}`

### 5.29 DescribeArchiveCountStat

You can call this operation to query log and event archiving statistics.

**Request parameters**

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeArchiveCountStat. |
| EndTime | String | No | The end time of the time frame specified for query, in timestamp format. |
| LogTypeList | String | No | The log type code. Separate multiple log types with commas (,). |
| StartTime | String | No | The start time of the time frame specified for query, in timestamp format. |

**Response parameters**

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| StatList | Array | A list of archiving statistics. For more information, see the following parameter descriptions. |
| LogType | Integer | The log type code. |
| StatItemList | Array | The archiving information. For more information, see the following parameter descriptions. |
| Capacity | Float | The storage space used for archiving. |
| Count | Integer | The number of archives. |
| Time | Long | The time when the statistics were collected, in timestamp format. |

**Error codes**

For more information about the error codes that this operation can return, see Error codes.

**Examples**

Sample requests

```
https://auditprivate.[ RegionId].example.com/?Action=DescribeArchiveCountStat &EndTime=1517630399000 &LogTypeList=1,2,3 &StartTime=1497516900000 &<Common request parameters>
```

Sample responses (JSON format) `{`

```json
 "RequestId":"63DDF633-1394-4AEB-A8E3-6467BC23D78D",
 "StatList":[
```

`{`

```json
   "Type":1,
   "StatDataList":[
```

`{`

```json
     "Time":1519228800000,
     "count":10,
     "capacity":356106.0
```

`}` `]` `}` `]` `}`

### 5.30 DescribeArchive

**Description**

You can call this operation to query log and event archive details.

**Request parameters**

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeArchive. |
| PageSize | String | No | The maximum number of records displayed on a page. |
| CurrentPage | String | No | The current page number. |
| EndTime | String | No | The end time, in timestamp format. |
| LogType | String | No | The log type code. |
| StartTime | String | No | The start time, in timestamp format. |
| Type | String | No | The archive type. |

**Response parameters**

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| CurrentPage | Integer | The current page number. |
| PageSize | Integer | The maximum number of records displayed on a page. |

| TotalCount | Integer | The total number of the returned records. |
|---|---|---|
| ArchiveList | Array | The list of archived data. For more information, see the following parameter descriptions. |
| CompactAlg | Integer | The type of the compression algorithm. |
| Count | Integer | The number of records. |
| CreateTime | Long | The time when the archive was created. |
| Id | Integer | The ID of the archive. |
| LogType | Integer | The log type code. |
| Md5 | String | The MD5 value of the archive file. |
| Name | String | The name of the archive file. |
| Sha256 | String | The SHA256 value of the archive file. |
| Type | Integer | The archive type. |

**Error codes**

For more information about the error codes that this operation can return, see Error codes.

**Examples**

Sample requests

```
https://auditprivate.[ RegionId].example.com/?Action=DescribeArchive &CurrentPage=1 &EndTime=1517630399000 &LogType=1 &PageSize=100 &StartTime=1517414400000 &Type=null &<Common request parameters>
```

Sample responses (JSON format) `{`

```json
 "RequestId":"D33241CB-8E4F-4803-A4D1-59E5B5C8849C",
 "TotalCount":1664162,
 "PageSize":20,
   "CurrentPage":1,
 "ArchiveList":[
```

`{`

```json
   "Type":1,
   "CompactAlg":2,
   "CreateTime":1519818135000,
   "LogType":5,
   "Count":2,
   "Id":3719841,
   "Name":"OPS/2018-02-28/OPS-20180228194215.gz",
   "Md5":"2637db033ab1d3501c1e9eeff8553fbe",
"Sha256":"06bbc4e58c8e938a9a1acd3edba3cbf6255cbf6e1302bbc8db0ad5c4dfc50a30"
```

`}` `]` `}`

## 6 Threat Detection Service (TDS)

**(TDS)**

### 6.1 Asset management

#### 6.1.1 DescribeFieldStatistics

Queries statistics of the assets.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeFieldSta tistics | The operation that you want to perform. Set the value to DescribeFieldStatistics. |
| MachineTypes | String | No | ecs | The types of the assets. If the asset type is not specified, the statistics of all types of assets are queried. ecs: an ECS instance cloud product: a cloud service _ |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| GroupedFields | - | - | The asset information. |
| GroupCount | Integer | 20 | The number of server groups. |
| InstanceCount | Integer | 100 | The total number of assets. |
| NewInstanceC ount | Integer | 10 | The number of new servers. |
| NotRunningSta tusCount | Integer | 10 | The number of servers that are not started. |
| OfflineInstanc eCount | Integer | 21 | The number of offline servers. |
| RegionCount | Integer | 11 | The number of regions to which the servers belong. |

| RiskInstanceC ount | Integer | 90 | The number of assets that are at risk. |
|---|---|---|---|
| UnprotectedIn stanceCount | Integer | 10 | The number of unprotected assets. |
| VpcCount | Integer | 5 | The number of VPCs. |
| RequestId | String | 7E0618A9-D5EF- 4220-9471- C42B5E92719F | The ID of the request. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeFieldStatistics &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeFieldStatistics>
  <RequestId>20CB6B41-0ED9-4679-BF5D-B84B8F7E70FC</RequestId>
  <GroupedFields>
        <InstanceCount>216</InstanceCount>
        <GroupCount>3</GroupCount>
        <NewInstanceCount>11</NewInstanceCount>
        <VpcCount>109</VpcCount>
        <RiskInstanceCount>121</RiskInstanceCount>
        <OfflineInstanceCount>48</OfflineInstanceCount>
        <UnprotectedInstanceCount>48</UnprotectedInstanceCount>
        <RegionCount>25</RegionCount>
        <NotRunningStatusCount>9</NotRunningStatusCount>
  </GroupedFields>
</DescribeFieldStatistics>
```

`JSON` format `{`

```json
 "RequestId":"20CB6B41-0ED9-4679-BF5D-B84B8F7E70FC",
 "GroupedFields":{
  "InstanceCount":216,
  "NewInstanceCount":11,
  "GroupCount":3,
  "VpcCount":109,
  "RiskInstanceCount":121,
  "UnprotectedInstanceCount":48,
  "OfflineInstanceCount":48,
  "RegionCount":25,
  "NotRunningStatusCount":9
```

`}` `}`

**Error codes**

For a list of error codes, see Error codes.

#### 6.1.2 DescribeGroupedTags

Queries the statistics of asset tags.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeGroupe dTags | The operation that you want to perform. Set the value to DescribeGroupedTags. |
| MachineTypes | String | No | ecs | The types of the assets. If the asset type is not specified, the statistics of all asset tags are queried. ecs: an ECS instance cloud product: a cloud service _ |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Count | Integer | 2 | The number of entries returned on the current page. |
| GroupedFileds | Array |   | The statistics of the asset tag. |
| Count | String | 2 | The number of assets to which a tag attaches. |

| Name | String | test | The name of the tag. |
|---|---|---|---|
| TagId | Integer | 8704 | The ID of the tag. |
| HttpStatusCod e | Integer | 200 | The HTTP status code of the returned results. |
| RequestId | String | 7E0618A9-D5EF- 4220-9471- C42B5E92719F | The ID of the request. |
| Success | Boolean | true | Indicates whether the request was successful. true: successful false: failed |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeGroupedTags &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeGroupedTags>
  <HttpStatusCode>200</HttpStatusCode>
  <Count>1</Count>
  <RequestId>DD5AFF52-0827-4FC9-B6EA-B233FF3AFF91</RequestId>
  <Success>true</Success>
  <GroupedFileds>
        <Name>test</Name>
        <Count>167</Count>
        <TagId>8704</TagId>
  </GroupedFileds>
</DescribeGroupedTags>
```

`JSON` format `{`

```json
 "HttpStatusCode":200,
 "Count":1,
 "RequestId":"DD5AFF52-0827-4FC9-B6EA-B233FF3AFF91",
 "Success":true,
 "GroupedFileds":[
```

`{`

```json
   "Name":"test",
   "Count":"167",
   "TagId":8704
```

`}` `]` `}`

**Error codes**

For a list of error codes, see Error codes.

#### 6.1.3 DescribeAllGroups

Queries the grouping information about servers.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeAllGrou ps | The operation that you want to perform. Set the value to DescribeAllGroups. |
| Lang | String | No | zh | The natural language of the request and response. Valid values: zh: Chinese en: English |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Count | Integer | 2 | The number of entries returned on the current page. |
| Groups | Array |   | The grouping information about the servers. |
| GroupFlag | Integer | 1 | The type of the server group. 0: default group 1: other groups |

| GroupId | Integer | 8834224 | The ID of the server group. |
|---|---|---|---|
| GroupName | String | test | The name of the server group. |
| RequestId | String | "requestId": "7E0618A9-D5EF- 4220-9471- C42B5E92719F", | The ID of the request. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeAllGroups &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeAllGroups>
  <Groups>
        <GroupFlag>0</GroupFlag>
        <GroupName>Ungrouped</GroupName>
        <GroupId>4120080</GroupId>
  </Groups>
  <Groups>
        <GroupFlag>1</GroupFlag>
        <GroupName>leaves</GroupName>
        <GroupId>8831497</GroupId>
  </Groups>
  <Groups>
        <GroupFlag>1</GroupFlag>
        <GroupName>test</GroupName>
        <GroupId>8834224</GroupId>
  </Groups>
  <Count>3</Count>
  <RequestId>9DD4B19B-CA32-41DA-AED7-77B4F84A91D5</RequestId>
</DescribeAllGroups>
```

`JSON` format `{`

```json
 "Groups":[
```

`{`

```json
   "GroupFlag":0,
   "GroupName":"Ungrouped",
   "GroupId":4120080
```

`},` `{`

```json
   "GroupFlag":1,
   "GroupName":"leaves",
   "GroupId":8831497
```

`},` `{`

```json
   "GroupFlag":1,
   "GroupName":"test",
   "GroupId":8834224
```

`}` `],`

```json
 "Count":3,
 "RequestId":"9DD4B19B-CA32-41DA-AED7-77B4F84A91D5"
```

`}`

**Error codes**

For a list of error codes, see Error codes.

#### 6.1.4 DescribeInstanceStatistics

Queries risk information about an asset.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| From | String | Yes | sas | The source of the data. Set the value to sas. |
| Uuid | String | Yes | a51cec37-ed73- 4c53-b467-*** | The IDs of the assets. Separate multiple IDs with commas (,). Note To query the risk information about an asset, you must provide the ID of the asset. You can call the DescribeCloudCenterInstances operation to obtain the ID. |
| SourceIp | String | No | 1.2.3.4 | The source IP address of the request. |

| Lang | String | No | zh | The natural language of the request and response. Valid values: zh: Chinese en: English |
|---|---|---|---|---|

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 7E0618A9-D5EF- 4220-9471- C42B5E92719F | The ID of the request. |
| Data | Array |   | The risk information about the asset. |
| Uuid | String | us1233****** | The ID of the asset. |
| Account | Integer | 1 | The type of the asset group. Valid values: 0: default group 1: other groups |
| Health | Integer | 1 | The number of issues detected by the baseline check. |
| Trojan | Integer | 1 | The number of trojans. |
| Suspicious | Integer | 2 | The number of alerts. |
| Vul | Integer | 4 | The total number of vulnerabilities: CveNum + EmgNum + SysNum + CmsNum + AppNum. |
| CveNum | Integer | 1 | The number of Linux software vulnerabilities. |
| EmgNum | Integer | 0 | The number of emergency vulnerabilities. |
| SysNum | Integer | 1 | The number of Windows vulnerabilities. |
| CmsNum | Integer | 2 | The number of Web CMS vulnerabilities. |
| AppNum | Integer | 0 | The number of application vulnerabilities. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeInstanceStatistics &From=sas &Uuid=a51cec37-ed73-4c53-b467-*** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeInstanceStatisticsResponse>
  <Data>
        <SysNum>1</SysNum>
        <Uuid>a51cec37-ed73-4c53-b467-***</Uuid>
        <CveNum>1</CveNum>
        <Suspicious>1</Suspicious>
        <Trojan>0</Trojan>
        <Account>0</Account>
        <CmsNum>1</CmsNum>
        <EmgNum>1</EmgNum>
        <Health>0</Health>
        <AppNum>1</AppNum>
        <Vul>5</Vul>
  </Data>
  <Data>
        <SysNum>2</SysNum>
        <Uuid>33f107a3-4653-4228-a428-***</Uuid>
        <CveNum>1</CveNum>
        <Suspicious>2</Suspicious>
        <Trojan>0</Trojan>
        <Account>0</Account>
        <CmsNum>1</CmsNum>
        <EmgNum>2</EmgNum>
        <Health>0</Health>
        <AppNum>1</AppNum>
        <Vul>7</Vul>
  </Data>
  <RequestId>44AE72D4-2DDF-4CEC-9957-64C470CC90FC</RequestId>
</DescribeInstanceStatisticsResponse>
```

`JSON` format `{`

```json
    "Data": [
```

`{`

```json
            "SysNum": 1,
            "Uuid": "a51cec37-ed73-4c53-b467-***",
            "CveNum": 1,
            "Suspicious": 1,
            "Trojan": 0,
            "Account": 0,
            "CmsNum": 1,
            "EmgNum": 1,
            "Health": 0,
            "AppNum": 1,
            "Vul": 5
```

`},` `{`

```json
            "SysNum": 2,
            "Uuid": "33f107a3-4653-4228-a428-***",
            "CveNum": 1,
            "Suspicious": 2,
            "Trojan": 0,
            "Account": 0,
            "CmsNum": 1,
            "EmgNum": 2,
            "Health": 0,
            "AppNum": 1,
            "Vul": 7
```

`}` `],`

```json
    "RequestId": "44AE72D4-2DDF-4CEC-9957-64C470CC90FC"
```

`}`

**Error codes**

For a list of error codes, see Error codes.

#### 6.1.5 DescribeCloudProductFieldStatistics

Queries the statistics on cloud services that are protected by Threat Detection Service.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeCloudPr oductFieldStatist ics | The operation that you want to perform. Set the value to DescribeCloudProductFieldStatistics. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 7E0618A9-D5EF- 4220-9471- C42B5E92719F | The ID of the request. |
| GroupedFields | Struct |   | The statistics on cloud services that are protected by Threat Detection Service. |
| RiskInstanceC ount | Integer | 90 | The number of assets that are at risk. |
| InstanceCount | Integer | 100 | The total number of assets. |
| CategoryCount | String | [{"MachineType":1 ,"Count":11}] | The statistics on the numbers of assets of different types. MachineType specifies the type of the asset.Count specifies the number of assets of a specific type. Valid values of MachineType: 1: Server Load Balancer (SLB) 2: NAT Gateway 3: ApsaraDB RDS 4: ApsaraDB for MongoDB |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeCloudProductFieldStatistics &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeCloudProductFieldStatistics>
      <code>200</code>
      <data>
            <GroupedFields>
                  <InstanceCount>100</InstanceCount>
                  <RiskInstanceCount>90</RiskInstanceCount>
                  <categoryCount>
                        <MachineType>1</MachineType>
                        <Count>11</Count>
                  </categoryCount>
            </GroupedFields>
      </data>
      <requestId>7E0618A9-D5EF-4220-9471-C42B5E92719F</requestId>
      <success>true</success>
</DescribeCloudProductFieldStatistics>
```

`JSON` format `{`

```json
  "code": 200,
  "data": {
    "GroupedFields": {
      "InstanceCount": 100,
      "RiskInstanceCount": 90,
      "categoryCount":[{"MachineType":1,"Count":11}]
```

`}` `},`

```json
  "requestId": "7E0618A9-D5EF-4220-9471-C42B5E92719F",
  "success": true
```

`}`

**Error codes**

For a list of error codes, see Error codes.

#### 6.1.6 DescribeCloudCenterInstances

Queries the asset information on the Assets page, such as the name and region of an asset instance.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeCloudC enterInstances | The operation that you want to perform. Set the value to DescribeCloudCenterInstances. |
| Criteria | String | No | [{"name":"riskSt atus","value":"Y ES"}, {"name":"intern etIp","value":"1. 2."}] | Specifies the search conditions, such as instance IDs, instance names, VPC IDs, regions, and IP addresses. |
| CurrentPage | Integer | No | 1 | The page number of the current page. |
| LogicalExp | String | No | OR | The logical relationship between search conditions. Valid values: OR: The logical relationship between search conditions is OR. AND: The logical relationship between search conditions is AND. |
| MachineTypes | String | No | ecs | The type of the asset. ecs: an Elastic Compute Service (ECS) instance cloud product: a cloud service _ |

| NoPage | Boolean | No | true | Specifies whether to enable paged query. Valid values: true: enables paged query. false: disables paged query. |
|---|---|---|---|---|
| PageSize | Integer | No | 20 | The number of entries to return on each page. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Instances | Array |   | The asset details. |
| AlarmStatus | String | NO | Indicates whether alerts are configured for the asset instance. Valid values: YES NO |
| AssetType | String | ecs | The type of the asset. |
| ClientStatus | String | online | Indicates whether the asset instance is protected by the agent. Valid values: online: The protection status of the asset is Enabled. offline: The protection status of the asset is Disabled. pause: The protection status of the asset is Paused. |
| Flag | Integer | 0 | Indicates whether the asset instance is provided by Alibaba Cloud. Valid values: 0: The asset instance is provided by Alibaba Cloud. 1: The asset instance is not provided by Alibaba Cloud. |
| GroupId | String | 4120080 | The ID of the group to which the asset instance belongs. |
| HcStatus | String | YES | Indicates whether the asset instance is exposed to baseline risks. Valid values: YES NO |

| HealthCheckC ount | Integer | 1 | The number of issues that are detected in baseline checks. |
|---|---|---|---|
| InstanceId | String | i-m5*** | The ID of the asset instance. |
| InstanceName | String | yztest-l*** | The name of the asset instance. |
| InternetIp | String | 1.2.3.4 | The public IP address of the asset instance. |
| IntranetIp | String | 1.2.3.0 | The private IP address of the asset instance. |
| Ip | String | 1.2.3.4 | The public IP address of the asset instance. |
| Os | String | Linux | The operating system of the asset instance. |
| OsName | String | CentOS 7.6 64-bit | The kernel version of the asset instance. |
| Region | String | cn-hangzhou- cm***-*** | The region where the asset instance is deployed. |
| RegionId | String | cn-hanghzou | The ID of the region where the asset instance is deployed. |
| RegionName | String | China (Qingdao) | The name of the region where the asset instance is deployed. |
| RiskStatus | String | NO | Indicates whether the asset instance is exposed to security risks. Valid values: YES NO |
| SafeEventCou nt | Integer | 5 | The number of alerts detected on the asset instance. |
| Status | String | Running | The status of the asset instance. Valid values: Running: The instance is running. notRunning: The instance is not running. |

| Tag | String | InternetIp | The tag of the asset instance. |
|---|---|---|---|
| Uuid | String | c9107c04-942f- 40c1-981a-f1c1*** | The ID of the asset instance. |
| VpcInstanceId | String | classic | The ID of the VPC to which the asset instance belongs. |
| VulCount | Integer | 2 | The number of vulnerabilities detected on the asset instance. |
| VulStatus | String | YES | Indicates whether the asset instance is exposed to vulnerabilities. Valid values: YES NO |
| PageInfo |   |   | The page information. |
| Count | Integer | 10 | The number of entries returned on the current page. |
| CurrentPage | Integer | 1 | The page number of the current page. |
| PageSize | Integer | 20 | The number of entries returned per page. |
| TotalCount | Integer | 50 | The total number of entries. |
| RequestId | String | 32A73759-4C0F- 4801-BE98- 901223ACEE9A | The ID of the request. |
| Success | Boolean | true | Indicates whether the request is successful. true: successful false: failed |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeCloudCenterInstances &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeCloudCenterInstances>
```

```xml
  <RequestId>32A73759-4C0F-4801-BE98-901223ACEE9A</RequestId>
  <PageInfo>
        <Count>0</Count>
        <TotalCount>691</TotalCount>
        <PageSize>20</PageSize>
        <CurrentPage>1</CurrentPage>
  </PageInfo>
  <Instances>
        <RiskStatus>NO</RiskStatus>
        <Uuid>88f7ce77-595e-4580-b655-3***</Uuid>
        <Ip>1.2.3.4</Ip>
        <Flag>0</Flag>
        <RegionName>China (Hangzhou)</RegionName>
        <OsName>CentOS 7.6 64-bit</OsName>
        <AssetType>0</AssetType>
        <InstanceId>i-m5e50***</InstanceId>
        <InternetIp>1.2.3.4</InternetIp>
        <HealthCheckCount>0</HealthCheckCount>
        <HcStatus>NO</HcStatus>
        <Os>linux</Os>
        <ClientStatus>online</ClientStatus>
        <Status>Running</Status>
        <Region>cn-hangzhou-cm***-***</Region>
        <VpcInstanceId>classic</VpcInstanceId>
        <VulStatus>NO</VulStatus>
        <Tag>InternetIp</Tag>
        <RegionId>cn-hangzhou</RegionId>
        <IntranetIp>1.2.3.0</IntranetIp>
        <AlarmStatus>NO</AlarmStatus>
        <VulCount>0</VulCount>
        <SafeEventCount>0</SafeEventCount>
        <InstanceName>yztest-l***</InstanceName>
  </Instances>
  <Instances>
        <RiskStatus>NO</RiskStatus>
        <Uuid>7a4735d6-75a4-4555-a18f-b***</Uuid>
        <Ip>1.2.3.4</Ip>
        <Flag>0</Flag>
        <RegionName>China (Hangzhou)</RegionName>
        <OsName>CentOS 7.6 64-bit</OsName>
        <AssetType>0</AssetType>
        <InstanceId>i-m5e5***</InstanceId>
        <InternetIp>1.2.3.4</InternetIp>
        <HealthCheckCount>0</HealthCheckCount>
        <HcStatus>NO</HcStatus>
        <Os>linux</Os>
        <ClientStatus>online</ClientStatus>
        <Status>Running</Status>
        <Region>cn-hangzhou-cm***-***</Region>
        <VpcInstanceId>classic</VpcInstanceId>
        <VulStatus>NO</VulStatus>
        <Tag>InternetIp</Tag>
        <RegionId>cn-hangzhou</RegionId>
        <IntranetIp>1.2.3.0</IntranetIp>
```

```xml
        <AlarmStatus>NO</AlarmStatus>
        <VulCount>0</VulCount>
        <SafeEventCount>0</SafeEventCount>
        <InstanceName>yztest-l***</InstanceName>
  </Instances>
  <Success>true</Success>
</DescribeCloudCenterInstances>
```

`JSON` format `{`

```json
 "RequestId":"32A73759-4C0F-4801-BE98-901223ACEE9A",
 "Instances":[
```

`{`

```json
   "RiskStatus":"NO",
   "Uuid":"88f7ce77-595e-4580-b655-3***",
   "Ip":"1.2.3.4",
   "Flag":0,
   "RegionName":"China (Hangzhou)",
   "OsName":"CentOS 7.6 64-bit",
   "AssetType":"0",
   "InstanceId":"i-m5e50***",
   "InternetIp":"1.2.3.4",
   "HealthCheckCount":0,
   "HcStatus":"NO",
   "Os":"linux",
   "Status":"Running",
   "ClientStatus":"online",
   "Region":"cn-hangzhou-cm***-***",
   "VpcInstanceId":"classic",
   "Tag":"InternetIp",
   "VulStatus":"NO",
   "IntranetIp":"1.2.3.0",
   "RegionId":"cn-hangzhou",
   "AlarmStatus":"NO",
   "VulCount":0,
   "InstanceName":"yztest-l***",
   "SafeEventCount":0
```

`},` `{`

```json
   "RiskStatus":"NO",
   "Uuid":"7a4735d6-75a4-4555-a18f-b***",
   "Ip":"1.2.3.4",
   "Flag":0,
   "RegionName":"China (Hangzhou)",
   "OsName":"CentOS 7.6 64-bit",
   "AssetType":"0",
   "InstanceId":"i-m5e5***",
   "InternetIp":"1.2.3.4",
   "HealthCheckCount":0,
   "HcStatus":"NO",
   "Os":"linux",
   "Status":"Running",
   "ClientStatus":"online",
```

`,`

```json
   "Region":"cn-hangzhou-cm***-***",
   "VpcInstanceId":"classic",
   "Tag":"InternetIp",
   "VulStatus":"NO",
   "IntranetIp":"1.2.3.0",
   "RegionId":"cn-hangzhou",
   "AlarmStatus":"NO",
   "VulCount":0,
   "InstanceName":"yztest-l***",
   "SafeEventCount":0
```

`}` `],`

```json
 "PageInfo":{
  "Count":0,
  "TotalCount":691,
  "PageSize":20,
  "CurrentPage":1
```

`},`

```json
 "Success":true
```

`}`

**Error codes**

For a list of error codes, see Error codes.

#### 6.1.7 DescribeSummaryInfo

Queries the security information about an asset, such as the security score and the numbers of protected and unprotected assets.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeSumma ryInfo | The operation that you want to perform. Set the value to DescribeSummaryInfo. |
| Lang | String | No | zh | The natural language of the request and response. Valid values: zh: Chinese en: English |
| SourceIp | String | No | 1.2.3.4 | The source IP address of the request. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|

| AegisClientOffl ineCount | Integer | 12 | The number of unprotected assets. |
|---|---|---|---|
| AegisClientOnl ineCount | Integer | 127 | The number of protected assets. |
| RequestId | String | D40198E1-6EA8- 482E-B3C7- D9573D75C0CA | The ID of the request. |
| SecurityScore | Integer | 44 | The security score of assets. Valid values: 95 to 100: The assets are secure. 85 to 94: The assets are exposed to a few security risks. We recommend that you reinforce your security system as soon as possible. 70 to 84: The assets are exposed to many security risks. We recommend that you reinforce your security system as soon as possible. 69 or lower: The current security system is unable to protect the assets against attacker intrusions. We recommend that you reinforce your security system as soon as possible. |
| Success | Boolean | true | Indicates whether the request is successful. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeSummaryInfo &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeSummaryInfo>
  <SecurityScore>44</SecurityScore>
  <AegisClientOnlineCount>127</AegisClientOnlineCount>
  <RequestId>D40198E1-6EA8-482E-B3C7-D9573D75C0CA</RequestId>
  <Success>true</Success>
  <AegisClientOfflineCount>12</AegisClientOfflineCount>
</DescribeSummaryInfo>
```

`JSON` format `{`

```json
 "AegisClientOnlineCount":127,
 "SecurityScore":44,
 "RequestId":"D40198E1-6EA8-482E-B3C7-D9573D75C0CA",
 "Success":true,
 "AegisClientOfflineCount":12
```

`}`

**Error codes**

For a list of error codes, see Error codes.

### 6.2 Secure score

#### 6.2.1 DescribeSecureSuggestion

Queries suggestions about how to manage the security risks that affect the security score.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeSecure Suggestion | The operation that you want to perform. Set the value to DescribeSecureSuggestion. |
| SourceIp | String | No | 1.2.3.4 | The source IP address of the request. |
| Lang | String | No | zh | The natural language of the request and response. Valid values: zh: Chinese en: English |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F35F45B0-5D6B- 4238-BE02- A62D0760E840 | The ID of the request. |
| Suggestions | Array |   | The suggestions on risk management. |
| Detail | Array |   | The details of risk management suggestions. |

| Description | String | You have four ApsaraDB RDS instances at risk. | The description of the suggestion for risk management. |
|---|---|---|---|
| SubType | String | CLOUD HC RDS _ _ | The type of the unhandled risk. |
| Title | String | The check on security policies of ApsaraDB RDS instances has failed. The instances are at risk. | The name of the unhandled risk. |
| Points | Integer | 40 | The penalty points of each item. |
| SuggestType | String | SS ALARM _ | The type of the unhandled risk. Valid values: SS REINFORCE: Key features, such as _ the antivirus feature, are not configured. SS ALARM: unhandled risks. _ SS VUL: unhandled vulnerabilities. _ SS HC: baseline check risks. _ SS AK: AccessKey pair leaks. _ SS CLOUD HC: configuration risks in _ _ Alibaba Cloud services. OTHER: other risks. |
| TotalCount | Integer | 15 | The total number of unhandled risks. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeSecureSuggestion &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeSecureSuggestionResponse>
  <Suggestions>
        <Points>40</Points>
        <SuggestType>SS_ALARM</SuggestType>
        <Detail>
              <Description>You have 691 security alerts, which affects 56 assets.
</Description>
              <SubType>ALARM_HIGH</SubType>
              <Title>You have unhandled high-risk alerts</Title>
        </Detail>
<Detail>
```

```xml
        <Detail>
              <Description>You have 501 security alerts, which affects 119 assets.
</Description>
              <SubType>ALARM_MEDIUM</SubType>
              <Title>You have unhandled medium-risk alerts</Title>
        </Detail>
  </Suggestions>
  <Suggestions>
        <Points>12</Points>
        <SuggestType>SS_VUL</SuggestType>
        <Detail>
              <Description>You have five vulnerabilities.</Description>
              <SubType>VUL_CMS</SubType>
              <Title>You have unhandled CMS vulnerabilities</Title>
        </Detail>
        <Detail>
              <Description>You have 107 vulnerabilities, which affects 68 servers.
</Description>
              <SubType>VUL_WIN</SubType>
              <Title>You have unhandled Windows host vulnerabilities</Title>
        </Detail>
        <Detail>
              <Description>You have 701 vulnerabilities, which affects 87 servers.
</Description>
              <SubType>VUL_LINUX</SubType>
              <Title>You have unhandled Linux host vulnerabilities</Title>
        </Detail>
        <Detail>
              <Description>You have one unhandled urgent vulnerability.</Description>
              <SubType>VUL_EMR_UNFIX</SubType>
              <Title>You have unhandled urgent vulnerabilities</Title>
        </Detail>
  </Suggestions>
  <Suggestions>
        <Points>2</Points>
        <SuggestType>SS_HC</SuggestType>
        <Detail>
              <Description>You have 46 baseline check risks, which affects 260 servers.
</Description>
              <SubType>HC_WARN</SubType>
              <Title>You have unhandled baseline check risks</Title>
        </Detail>
  </Suggestions>
  <Suggestions>
        <Points>30</Points>
        <SuggestType>SS_AK</SuggestType>
        <Detail>
              <Description>You have 12 AccessKey pair leaks.</Description>
              <SubType>ACCESSKEY_LEAK</SubType>
              <Title>You have potential AccessKey pair leaks</Title>
        </Detail>
  </Suggestions>
  <Suggestions>
        <Points>35</Points>
<SuggestType>SSCLOUDHC</SuggestType>
```

```xml
        <SuggestType>SS_CLOUD_HC</SuggestType>
        <Detail>
              <Description>You have four ApsaraDB RDS instances at risk.</Description>
              <SubType>CLOUD_HC_RDS</SubType>
              <Title>The check on security policies of ApsaraDB RDS instances has
failed. The instances are at risk</Title>
        </Detail>
        <Detail>
              <Description>You have three high configuration risks for Alibaba Cloud ser
vices.</Description>
              <SubType>CLOUD_HC_HIGH_LEVEL</SubType>
              <Title>You have high configuration risks for Alibaba Cloud services</Title
```

`>`

```xml
        </Detail>
        <Detail>
              <Description>You have 28 medium or low configuration risks for Alibaba
Cloud services.</Description>
              <SubType>CLOUD_HC_OTHER_LEVEL</SubType>
              <Title>You have medium or low configuration risks for Alibaba Cloud servic
es</Title>
        </Detail>
  </Suggestions>
  <Suggestions>
        <Points>5</Points>
        <SuggestType>OTHER</SuggestType>
        <Detail>
              <Description>You have been attacked 5,767 times.</Description>
              <SubType>OTHER_ATTACH</SubType>
              <Title>You are under attack</Title>
        </Detail>
  </Suggestions>
  <TotalCount>12</TotalCount>
  <requestId>F35F45B0-5D6B-4238-BE02-A62D0760E840</requestId>
</DescribeSecureSuggestionResponse>
```

`JSON` format `{`

```json
    "Suggestions": [{
        "Points": 40,
        "SuggestType": "SS_ALARM",
        "Detail": [{
            "Description": "You have 691 security alerts, which affects 56 assets",
            "SubType": "ALARM_HIGH",
            "Title": "You have unhandled high-risk alerts"
        }, {
            "Description": "You have 501 security alerts, which affects 119 assets",
            "SubType": "ALARM_MEDIUM",
            "Title": "You have unhandled medium-risk alerts"
```

`}]`

```json
    }, {
        "Points": 12,
        "SuggestType": "SS_VUL",
        "Detail": [{
```

`"D`

```
iti
```

`"` `"Y` `h` `fi` `l`

```
biliti
```

`"`

```json
            "Description": "You have five vulnerabilities",
            "SubType": "VUL_CMS",
            "Title": "You have unhandled CMS vulnerabilities"
        }, {
            "Description": "You have 107 vulnerabilities, which affects 68 servers",
            "SubType": "VUL_WIN",
            "Title": "You have unhandled Windows host vulnerabilities"
        }, {
            "Description": "You have 701 vulnerabilities, which affects 87 servers",
            "SubType": "VUL_LINUX",
            "Title": "You have unhandled Linux host vulnerabilities"
        }, {
            "Description": "You have one unhandled urgent vulnerability",
            "SubType": "VUL_EMR_UNFIX",
            "Title": "You have unhandled urgent vulnerabilities"
```

`}]`

```json
    }, {
        "Points": 2,
        "SuggestType": "SS_HC",
        "Detail": [{
            "Description": "You have 46 baseline check risks, which affects 260
servers",
            "SubType": "HC_WARN",
            "Title": "You have baseline check risks"
```

`}]`

```json
    }, {
        "Points": 30,
        "SuggestType": "SS_AK",
        "Detail": [{
            "Description": "You have 12 potential AccessKey pair leaks",
            "SubType": "ACCESSKEY_LEAK",
            "Title": "You have potential AccessKey pair leaks"
```

`}]`

```json
    }, {
        "Points": 35,
        "SuggestType": "SS_CLOUD_HC",
        "Detail": [{
            "Description": "You have four ApsaraDB RDS instances at risk",
            "SubType": "CLOUD_HC_RDS",
            "Title": "The check on security policies of ApsaraDB RDS instances has fail
ed. The instances are at risk"
        }, {
            "Description": "You have three high configuration risks for Alibaba Cloud se
rvices",
            "SubType": "CLOUD_HC_HIGH_LEVEL",
            "Title": "You have high configuration risks for Alibaba Cloud services"
        }, {
            "Description": "You have 28 medium or low configuration risks for Alibaba
Cloud services",
            "SubType": "CLOUD_HC_OTHER_LEVEL",
            "Title": "You have medium or low configuration risks for Alibaba cloud
services"
```

`}]`

```json
    }, {
"Points":5
```

```json
        Points: 5,
        "SuggestType": "OTHER",
        "Detail": [{
            "Description": "You have been attacked 5,767 times",
            "SubType": "OTHER_ATTACH",
            "Title": "You are under attack."
```

`}]`

```json
    }],
    "TotalCount": 12,
    "requestId": "F35F45B0-5D6B-4238-BE02-A62D0760E840"
```

`}`

**Error codes**

For a list of error codes, see Error codes.

### 6.3 Security alerts

#### 6.3.1 DescribeAlarmEventList

Queries alert events on the Alerts page. An alert event consists of alerts and exceptions. Each alert event is related to multiple exceptions.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeAlarmE ventList | The operation that you want to perform. Set the value to DescribeAlarmEventList. |
| CurrentPage | Integer | Yes | 1 | The page number of the current page. Pages start from page 1. Default value: 1. |
| From | String | Yes | sas | The ID of the request source. Set the value to sas. |
| PageSize | String | Yes | 20 | The number of entries to return on each page. Default value: 20. |
| SourceIp | String | No | 1.2.3.4 | The source IP address of the request. |
| Lang | String | No | zh | The natural language of the request and response. Valid values: zh: Chinese en: English |

| Dealed | String | No | Y | The status of the alert event. Valid values: N: unhandled Y: handled |
|---|---|---|---|---|
| Levels | String | No | serious | The severity levels of the alert events. Separate multiple levels with commas (,). Valid values: serious suspicious remind |
| Remark | String | No | database server _ | The name of the alert, or the asset information. |
| GroupId | String | No | tst*** | The group ID of the affected asset. |
| AlarmEventNa me | String | No | DDoS trojans | The name of the alert event. |
| AlarmEventTy pe | String | No | Malicious process (cloud threat detection) | The type of the alert event. |

| OperateErrorC odeList.N | RepeatL ist | No | ignore. Success | Alert handling result code N. The value is in the format of Operation type.Operation result code. Operation types include: Common: performs common operations. deal: handles the alert. ignore: ignores the alert. offline handled: marks the alert as _ handled. mark mis info: marks the alerts as _ _ false positives by adding them to the whitelist. rm mark mis info: cancels false _ _ _ positives by removing the alerts from the whitelist. quara: quarantines the source file of the malicious process. kill and quara: kills the malicious _ _ process and quarantines the source file. kill virus: deletes the source file of _ the malicious process. block ip: blocks the source IP _ addresses. manual handled: manually _ handles the alert. Operation result codes: Success: The operation is successful. Failure: The operation fails. AgentOffline: The agent is offline. |
|---|---|---|---|---|

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 28267723-D857- 4DD8-B295- 013100000000 | The ID of the request. |
| SuspEvents | Array |   | The information about the alert event. |
| AlarmUniqueIn fo | String | 8df914418f4211fbf 756efe7a6f40cbc | The ID of the alert event. |

| Solution | String | Check the malicious URLs that have been listed in the alert. Check the directory for malicious files. Terminate the malicious processes. If you manually run the processes, you can mark them as false positives in the console. | The solution to handle the alert event. |
|---|---|---|---|
| Level | String | serious | The severity level of the alert event. Valid values: serious suspicious remind |
| CanBeDealOnL ine | Boolean | true | Indicates whether the online processing of the alert event is supported, such as quarantining the source file of the malicious process, adding the alert event to the whitelist, and ignoring the alert event. true: Online processing is supported. false: Online processing is not supported. |
| Description | String | After an attacker accesses a victim server, to keep the malicious programs running, the attacker may have imported malicious shell scripts into scheduled tasks such as crontab and systemd. | The description of the alert event. |
| StartTime | Long | 1543740301000 | The time when the alert event starts. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since the epoch time January 1, 1970, 00:00:00 UTC. |
| EndTime | Long | 1543740301000 | The time when the alert event ends. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since the epoch time January 1, 1970, 00:00:00 UTC. |

| AlarmEventTy pe | String | Suspicious processes | The type of the alert event. |
|---|---|---|---|
| SuspiciousEve ntCount | Integer | 1 | The number of exceptions related to the alert event. |
| Uuid | String | 47900178-885d- 4fa4-9d77-*** | The ID of the related asset. |
| InstanceName | String | Test server | The name of the affected asset. |
| InternetIp | String | 1.2.3.4 | The public IP address of the affected asset. |
| IntranetIp | String | 1.2.3.5 | The private IP address of the affected asset. |
| AlarmEventNa me | String | Running malicious commands | The name of the alert event. |
| SaleVersion | String | 1 | The version in which the alert event detection can be enabled. Valid values: 0: Basic Edition 1: Enterprise Edition |
| DataSource | String | aegis *** _ | The source of data. |
| CanCancelFaul t | Boolean | false | Indicates whether you can cancel marking this alert event as a false positive. |
| Dealed | Boolean | false | Indicates whether the alert has been handled. Valid values: true: handled false: unhandled |
| GmtModified | Long | 1569235879000 | The last time when the alert was triggered. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since the epoch time January 1, 1970, 00:00:00 UTC. |
| HasTraceInfo | Boolean | true | Indicates whether the alert has trace information. true: The alert has trace information. false: The alert does not have trace information. |

| SecurityEventI ds | String | 270789 | The ID of the related exception. |
|---|---|---|---|
| OperateErrorC ode | String | kill and quara.Suc _ _ cess | The handling result code of the alert event. |
| AlarmEventNa meOriginal | String | Precise defense against malicious commands | The original parent name of the alert event. |
| InstanceId | String | i-e*** | The ID of the affected asset. |
| PageInfo | Struct |   | The page information. |
| Count | Integer | 1 | The number of entries returned on the current page. |
| PageSize | Integer | 20 | The number of entries returned per page. |
| TotalCount | Integer | 1 | The total number of the alert events. |
| CurrentPage | Integer | 1 | The page number of the current page. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeAlarmEventList &CurrentPage=1 &From=sas &PageSize=20 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeAlarmEventList>
  <RequestId>1D7FB2DD-4B80-41F4-94CF-C484EF6A5CAC</RequestId>
  <PageInfo>
        <Count>1</Count>
        <TotalCount>58</TotalCount>
        <PageSize>1</PageSize>
        <CurrentPage>1</CurrentPage>
  </PageInfo>
  <SuspEvents>
        <Uuid>c4678332-ef35-4ad4-8358-681ebbc0ccab</Uuid>
        <Dealed>true</Dealed>
        <SecurityEventIds>261401</SecurityEventIds>
        <Description>Cloud threat detection (mining programs)</Description>
        <CanCancelFault>false</CanCancelFault>
        <InstanceId>i-bp***</InstanceId>
        <OperateErrorCode></OperateErrorCode>
        <InternetIp>1.2.3.5</InternetIp>
        <GmtModified>1572524936000</GmtModified>
        <SuspiciousEventCount>1</SuspiciousEventCount>
        <HasTraceInfo>false</HasTraceInfo>
        <AlarmUniqueInfo>8b59e7bd134797758709983c26ece2a2</AlarmUniqueInfo>
        <AlarmEventName>Mining programs</AlarmEventName>
        <AlarmEventType>Precise defense</AlarmEventType>
        <IntranetIp>1.2.3.4</IntranetIp>
        <Level>serious</Level>
        <EndTime>1572524936000</EndTime>
        <StartTime>1572524936000</StartTime>
        <AlrmEventNameOriginal>Precise defense against mining
programs</AlarmEventNameOriginal>
        <SaleVersion>0</SaleVersion>
        <CanBeDealOnLine>false</CanBeDealOnLine>
        <InstanceName>cit***</InstanceName>
  </SuspEvents>
</DescribeAlarmEventList>
```

`JSON` format `{`

```json
    "RequestId": "1D7FB2DD-4B80-41F4-94CF-C484EF6A5CAC",
    "PageInfo": {
        "Count": 1,
        "TotalCount": 58,
        "PageSize": 1,
        "CurrentPage": 1
```

`},`

```json
    "SuspEvents": [
```

`{`

```json
            "Uuid": "c4678332-ef35-4ad4-8358-681ebbc0ccab",
            "Dealed": true,
            "SecurityEventIds": "261401",
            "Description": "Cloud threat detection (mining programs)",
            "CanCancelFault": false,
            "InstanceId": "i-bp***",
            "OperateErrorCode": "",
            "InternetIp": "1.2.3.5",
            "GmtModified": 1572524936000,
            "SuspiciousEventCount": 1,
            "HasTraceInfo": false,
            "AlarmUniqueInfo": "8b59e7bd134797758709983c26ece2a2",
            "AlarmEventName": "Mining programs",
            "AlarmEventType": "Precise defense",
            "IntranetIp": "1.2.3.4",
            "Level": "serious",
            "EndTime": 1572524936000,
            "StartTime": 1572524936000,
            "AlarmEventNameOriginal": "Precise defense against mining programs",
            "SaleVersion": "0",
            "CanBeDealOnLine": false,
            "InstanceName": "cit***"
```

`}` `]` `}`

**Error codes**

For a list of error codes, see Error codes.

#### 6.3.2 DescribeAlarmEventDetail

Queries details of an alert event. An alert event consists of alerts and exceptions. Each alert event contains multiple exceptions.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|

| Action | String | Yes | DescribeAlarmE ventDetail | The operation that you want to perform. Set the value to DescribeAlarmEventDetail. |
|---|---|---|---|---|
| AlarmUniqueIn fo | String | Yes | 8df914418f4211 fbf756efe7a6f40 cbc | The ID of the alert event. Note To query details of an alert event, you must specify the ID of the alert event. You can call the DescribeAlarmEventList operation to obtain the ID. |
| From | String | Yes | sas | The ID of the request source. Set the value to sas. |
| SourceIp | String | No | 1.2.3.4 | The source IP address of the request. |
| Lang | String | No | zh | The natural language of the request and response. Valid values: zh: Chinese en: English |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Data | Struct |   | The details of the alert event. |
| AlarmEventAli asName | String | Suspicious process behavior-execution of suspicious commands in scheduled Linux tasks | The complete name of the alert event. |
| AlarmEventDe sc | String | After an attacker accesses a victim server, to keep the malicious programs running, the attacker may have imported malicious shell scripts into scheduled tasks such as crontab and systemd. | The description of the alert event. |
| AlarmUniqueIn fo | String | 8df914418f4211fbf 756efe700000000 | The ID of the alert event. |

| CanBeDealOnL ine | Boolean | false | Indicates whether processing alert events online is supported, such as blocking an alert, adding an alert to the whitelist, and ignoring an alert. Valid values: true: Online processing is supported. false: Online processing is not supported. |
|---|---|---|---|
| CanCancelFaul t | Boolean | false | Indicates whether you can cancel labelling this alert event as a false positive. Valid values: true: You can cancel labeling this alert event as a false positive. false: You cannot cancel labeling this alert event as a false positive. |
| CauseDetails | Array |   | The cause of the alert event (the information used to trace the alert). |
| Key | String | item | The format of the text. Valid values: text html |
| Value | Array |   | The value of the field displaying the information used to trace alerts. |
| Name | String | Solutions | The key of the field displaying the information used to trace alerts. |
| Type | String | html | The format of the field displaying the information used to trace alerts. |
| Value | String | Check for the exploited pages of your Web services and vulnerabilities in parameter configuration, and resolve these issues. | The value of the field displaying the information used to trace alerts. |
| DataSource | String | aegis *** _ | The source of data. |
| EndTime | Long | 1542366542000 | The end time of the alert event. |
| InstanceName | String | Test server | The name of the associated instance. |

| InternetIp | String | 1.2.3.1 | The public IP address of the associated instance. |
|---|---|---|---|
| IntranetIp | String | 1.2.3.5 | The private IP address of the associated instance. |
| Level | String | serious | The level of the alert event. Valid values: serious suspicious remind |
| Solution | String | Check the malicious URLs that have been listed in the alert. Check the directory for malicious file downloads. Stop the malicious processes that are running. If you trust the processes, mark the alert as a false positive in the console, and submit a ticket to security engineers. | The solution to the alert event. |
| StartTime | Long | 1542378601000 | The timestamp when the alert event was detected. |
| Type | String | Suspicious network connections | The type of the alert event. |
| Uuid | String | 47900178-885d- 4fa4-9d77- XXXXXXXXXXXX | The ID of the related instance. |
| RequestId | String | 5A1DDB3C-798C- 4A84-BF6E- 3DC700000000 | The ID of the request. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeAlarmEventDetail &AlarmUniqueInfo=8df914418f4211fbf756efe7a6f40cbc &From=sas &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeAlarmEventDetailResponse>
  <Data>
        <Uuid>47900178-885d-4fa4-9d77-XXXXXXXXXXXX</Uuid>
        <AlarmEventAliasName>Suspicious Process - Command Exceptions in Scheduled Linux
Tasks</AlarmEventAliasName>
        <Type>Suspicious process behavior</Type>
        <InternetIp>1.2.3.1</InternetIp>
        <AlarmEventDesc>After accessing a victim server, the attacker may have imported
malicious shell scripts into scheduled tasks such as crontab and systemd, to enable per sistent execution of malicious backdoor programs. </AlarmEventDesc>
        <IntranetIp>1.2.3.5</IntranetIp>
        <CauseDetails>
              <Value>
                    <Type>text</Type>
                    <Value>An attacker has logged on to your server and has written webs
hells by editing the configuration file.</Value>
                    <Name>Intrusion cause</Name>
              </Value>
              <Value>
                    <Type>text</Type>
                    <Value>2018-11-16 19:09:02</Value>
                    <Name>Attack time</Name>
              </Value>
              <Value>
                    <Type>text</Type>
                    <Value>N/A</Value>
                    <Name>Source IP of attack</Name>
              </Value>
              <Value>
                    <Type>text</Type>
                    <Value>N/A</Value>
                    <Name>Payload of attack</Name>
              </Value>
              <Value>
                    <Type>text</Type>
                    <Value>Check for the exploited pages of your Web services and vulner
abilities in parameter configuration, and resolve these issues. </Value>
                    <Name>Solutions</Name>
              </Value>
              <Key>item</Key>
        </CauseDetails>
        <Level>serious</Level>
        <EndTime>1543741201000</EndTime>
        <StartTime>1543312803000</StartTime>
        <CanBeDealOnLine>false</CanBeDealOnLine>
        <InstanceName>serve***</InstanceName>
  </Data>
  <RequestId>5A1DDB3C-798C-4A84-BF6E-3DC7F7D7EB4A</RequestId>
</DescribeAlarmEventDetailResponse>
```

`JSON` format `{`

```json
    "Data": {
        "Uuid": "47900178-885d-4fa4-9d77-XXXXXXXXXXXX",
        "AlarmEventAliasName": "Suspicious process behavior-execution of suspicious com
mands in scheduled Linux tasks",
        "Type": "Suspicious process behavior",
        "InternetIp": "1.2.3.1",
        "AlarmEventDesc": "After an attacker accesses a victim server, to keep the mali
cious programs running, the attacker may have imported malicious shell scripts into sch eduled tasks such as crontab and systemd.",
        "IntranetIp": "1.2.3.5",
        "CauseDetails": [
```

`{`

```json
                "Value": [
```

`{`

```json
                        "Type": "text",
                        "Value": "An attacker has logged on to your ECS instance and has
written webshells by editing files.",
                        "Name": "Intrusion cause"
```

`},` `{`

```json
                        "Type": "text",
                        "Value": "2018-11-16 19:09:02",
                        "Name": "Time of attack"
```

`},` `{`

```json
                        "Type": "text",
                        "Value": "N/A",
                        "Name": "Source IP of attack"
```

`},` `{`

```json
                        "Type": "text",
                        "Value": "N/A",
                        "Name": "Payload of attack"
```

`},` `{`

```json
                        "Type": "text",
                        "Value": "Check for the exploited pages of your Web services and
vulnerabilities in parameter configuration, and resolve these issues.",
                        "Name": "Solutions"
```

`}` `],`

```json
                "Key": "item"
```

`}` `],`

```json
        "Level": "serious",
        "EndTime": 1543741201000,
        "StartTime": 1543312803000,
        "CanBeDealOnLine": false,
        "InstanceName": "serve***"
```

`},`

```json
    "RequestId": "5A1DDB3C-798C-4A84-BF6E-3DC7F7D7EB4A"
```

`}`

**Error codes**

For a list of error codes, see Error codes.

#### 6.3.3 DescribeSuspEvents

Queries information about exceptions. An alert event consists of alerts and exceptions. Each alert event is related to multiple exceptions.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeSuspEv ents | The operation that you want to perform. Set the value to DescribeSuspEvents. |
| From | String | Yes | sas | The data source on which the exception is detected. Set the value to sas. |
| SourceIp | String | No | 1.2.3.4 | The source IP address of the request. |
| Dealed | String | No | N | The status of the exception. Valid values: N: unhandled Y: handled |
| Name | String | No | ecs-xxx | The name of the exception or the affected server. Fuzzy match is supported. |
| Levels | String | No | serious | The severity levels of the alert events. Separate multiple levels with commas (,). The following levels are listed in descending order. serious suspicious remind |
| ParentEventTy pes | String | No | Webshells | The type of the alert event to which the exception is related. |
| Remark | String | No | Test server | The IP address or name of the server. |

| PageSize | String | No | 20 | The number of entries to return on each page. Default value: 20. |
|---|---|---|---|---|
| CurrentPage | String | No | 1 | The page number of the current page. |
| Lang | String | No | zh | The natural language of the request and response. Valid values: zh: Chinese en: English |
| AlarmUniqueIn fo | String | No | 8df914418f4211 fbf*** | The alert event to which the exception is related. Note To query details about exceptions of an alert event, you must provide the ID of the alert event. You can call the DescribeAlarmEventList operation to obtain the ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 43F670F3-AB40- 4E91-BC7D- C57400000000 | The ID of the request. |
| Count | Integer | 1 | The number of entries returned on the current page. |
| PageSize | Integer | 20 | The number of entries returned per page. |
| TotalCount | Integer | 100 | The total number of the exceptions. |
| CurrentPage | Integer | 1 | The page number of the current page. |
| SuspEvents | Array |   | The details of the exception. |
| LastTime | String | 2018-09-26 01:51:01 | The last time when the exception occurred. |
| OccurrenceTi me | String | 2018-09-26 01:51:01 | The first time when the exception occurred. |

| Id | Long | 1000 | The ID of the exception to query. |
|---|---|---|---|
| UniqueInfo | String | e17e*** | The ID of the exception. |
| InstanceName | String | nginx | The name of the related asset. |
| InternetIp | String | 1.2.3.1 | The public IP address of the related asset. |
| IntranetIp | String | 1.2.3.5 | The private IP address of the related asset. |
| Uuid | String | bf6b30d3-eea8- 4924-9f0a-*** | The ID of the related asset. |
| Name | String | Malicious processes (cloud threat detection) - XOR DDoS trojan | The complete name of the exception. |
| EventSubType | String | XorDDoS trojan | The name of the exception. |
| Level | String | serious | The severity level of the exception. Valid values: serious suspicious remind |
| EventStatus | Integer | 1 | The status of the exception. Valid values: 1: unhandled 2: ignored 4: confirmed 8: marked as false positive 16: handling 32: handled 64: expired |
| Desc | String | webshell | The impact of the exception. |
| OperateMsg | String | success | The operation remarks of the exception. |
| DataSource | String | aegis suspicious * _ _ ** | The data source. |

| CanBeDealOnL ine | Boolean | true | Indicates whether the online processing of the exception is supported. The processing includes quarantining the exception. Valid values: true: Online processing is supported. false: Online processing is not supported. |
|---|---|---|---|
| SaleVersion | String | 1 | The version in which the exception detection can be enabled. Valid values: 0: Basic Edition 1: Enterprise Edition |
| AlarmEventTy pe | String | Suspicious processes | The type of the alert event. |
| AlarmEventNa me | String | Suspicious command running in scheduled Linux tasks | The name of the alert event. |
| AlarmUniqueIn fo | String | 8df914418f*** | The ID of the alert event. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeSuspEvents &From=saas &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeSuspEvents>
  <TotalCount>3</TotalCount>
  <Count>2</Count>
  <PageSize>20</PageSize>
  <RequestId>0C7FAD74-83FA-4671-9250-A5F2A64F437A</RequestId>
  <CurrentPage>1</CurrentPage>
  <SuspEvents>
        <EventStatus>1</EventStatus>
        <SaleVersion>1</SaleVersion>
        <IntranetIp>1.2.3.4</IntranetIp>
        <EventSubType>XOR DDoS trojan</EventSubType>
        <Name>Malicious processes (cloud threat detection) - XOR DDoS trojan</Name>
        <DataSource>aegis_suspiciou***</DataSource>
        <OccurrenceTime>2018-09-26 01:51:01</OccurrenceTime>
        <InstanceName>server01</InstanceName>
        <Desc>After accessing the server, XOR DDoS trojan may have injected malicious c
ode into Linux scheduled tasks. </Desc>
        <CanBeDealOnLine>false</CanBeDealOnLine>
        <Uuid>bf6b30d3-eea8-4924***</Uuid>
        <InternetIp>1.2.3.4</InternetIp>
        <Level>serious</Level>
        <Id>3682</Id>
        <LastTime>2018-10-24 21:06:01</LastTime>
  </SuspEvents>
  <SuspEvents>
        <EventStatus>1</EventStatus>
        <SaleVersion>1</SaleVersion>
        <IntranetIp>1.2.3.5</IntranetIp>
        <EventSubType>XOR DDoS trojan</EventSubType>
        <Name>Malicious processes (cloud threat detection) - XOR DDoS trojan</Name>
        <DataSource>aegis_suspiciou***</DataSource>
        <OccurrenceTime>2018-09-26 02:01:01</OccurrenceTime>
        <InstanceName>server01</InstanceName>
        <Desc>After accessing the server, XOR DDoS trojan may have injected malicious c
ode into Linux scheduled tasks. </Desc>
        <CanBeDealOnLine>false</CanBeDealOnLine>
        <Uuid>bf6b30d3-eea8-4924-***</Uuid>
        <InternetIp>1.2.3.4</InternetIp>
        <Level>serious</Level>
        <Id>3683</Id>
        <LastTime>2018-10-24 21:01:01</LastTime>
  </SuspEvents>
</DescribeSuspEvents>
```

`JSON` format `{`

```json
    "TotalCount": 3,
    "Count": 2,
    "PageSize": 20,
    "RequestId": "0C7FAD74-83FA-4671-9250-A5F2A64F437A",
    "CurrentPage": 1,
    "SuspEvents": [
```

`{`

```json
            "EventStatus": 1,
            "SaleVersion": "1",
            "IntranetIp": "1.2.3.4",
            "EventSubType": "XOR DDoS trojan"
            "Name": "Malicious processes (cloud threat detection) - XOR DDoS trojan",
            "DataSource": "aegis_suspiciou***",
            "OccurrenceTime": "2018-09-26 01:51:01",
            "InstanceName": "server01",
            "Desc": "After accessing the server, XOR DDoS trojan may have injected mali
cious code into Linux scheduled tasks.",
            "CanBeDealOnLine": false,
            "Uuid": "bf6b30d3-eea8-4924***",
            "InternetIp": "1.2.3.4",
            "Level": "serious",
            "Id": 3682,
            "LastTime": "2018-10-24 21:06:01"
```

`},` `{`

```json
            "EventStatus": 1,
            "SaleVersion": "1",
            "IntranetIp": "1.2.3.5",
            "EventSubType": "XOR DDoS trojan"
            "Name": "Malicious processes (cloud threat detection) - XOR DDoS trojan",
            "DataSource": "aegis_suspiciou***",
            "OccurrenceTime": "2018-09-26 02:01:01",
            "InstanceName": "server01",
            "Desc": "After accessing the server, XOR DDoS trojan may have injected mali
cious code into Linux scheduled tasks.",
            "CanBeDealOnLine": false,
            "Uuid": "bf6b30d3-eea8-4924-***",
            "InternetIp": "1.2.3.4",
            "Level": "serious",
            "Id": 3683,
            "LastTime": "2018-10-24 21:01:01"
```

`}` `]` `}`

**Error codes**

For a list of error codes, see Error codes.

#### 6.3.4 DescribeSuspEventDetail

Queries details of a specific exception. An alert event consists of alerts and exceptions. Each alert event is related to multiple exceptions.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeSuspEv entDetail | The operation that you want to perform. Set the value to DescribeSuspEventDetail. |
| From | String | Yes | sas | The data source on which the exception is detected. Set the value to sas. |
| SourceIp | String | No | 1.2.3.4 | The source IP address of the request. |
| Lang | String | No | zh | The natural language of the request and response. Valid values: zh: Chinese en: English |
| SuspiciousEve ntId | Integer | No | 1 | The ID of the exception to query. Note To query the details of an exception, you must provide the ID of the exception. You can call the DescribeSuspEvents operation to obtain the ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 1 | The ID of the request. |
| LastTime | String | 2018-10-30 11:43:46 | The last time when the exception occurred. |
| Id | Integer | 1991 | The ID of the exception to query. |
| InstanceName | String | ca cpm test1 _ _ | The name of the related asset. |
| InternetIp | String | 1.2.3.5 | The public IP address of the related asset. |

| IntranetIp | String | 1.2.3.1 | The private IP address of the related asset. |
|---|---|---|---|
| Uuid | String | bffb12c3-590a- 4db2-b538-*** | The ID of the related asset. |
| EventDesc | String | This file may have been uploaded by an attacker that has intruded into your website. Check the validity of this file. | The description of the exception. |
| EventTypeDes c | String | Webshell - Webshell | The type of the exception. |
| Level | String | serious | The severity level of the exception. Valid values: serious suspicious remind |
| EventStatus | String | 1 | The status of the exception. Valid values: 1: unhandled 2: ignored 4: confirmed 8: marked as false positive 16: handling 32: handled 64: expired |
| SaleVersion | String | 1 | The version in which exception detection can be enabled. Valid values: 0: Basic Edition 1: Enterprise Edition |
| DataSource | String | aegis suspicious * _ _ ** | The data source on which the exception is detected. |
| OperateMsg | String | success | The operation remarks of the exception. |
| SasId | String | 1sdeswdd**** | The ID of the service in Threat Detection Service. |
| EventName | String | WEBSHELL | The name of the exception. |

| CanBeDealOnL ine | Boolean | true | Indicates whether the online processing of the exception is supported. Valid values: true: Online processing is supported. false: Online processing is not supported. |
|---|---|---|---|
| Details | Array |   | The details of the exception. |
| Name | String | The update time. | The name in the exception details. |
| Type | String | html | The format in the exception details. Valid values: text html |
| InfoType | String | download url _ | The type of the icon. |
| Value | String | 2018-12-12 12:00:00 | The content in the exception details. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeSuspEventDetail &From=sas &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeSuspEventDetailResponse>
  <RequestId>43F670F3-AB40-4E91-BC7D-C57468834F67</RequestId>
  <EventDesc>This file may have been uploaded by an attacker that has intruded into you
r website. Check the validity of this file. </EventDesc>
  <EventTypeDesc>Webshell - Webshell</EventTypeDesc>
  <EventStatus>1</EventStatus>
  <EventName>WEBSHELL</EventName>
  <SaleVersion>1</SaleVersion>
  <IntranetIp>1.2.3.4</IntranetIp>
  <DataSource>aegis_suspicious_***</DataSource>
  <InstanceName>ca_***</InstanceName>
  <CanBeDealOnLine>true</CanBeDealOnLine>
  <OperateMsg></OperateMsg>
  <Uuid>bffb12c3-590a-4db2-b538-***</Uuid>
  <Details>
        <Type>text</Type>
        <Value>/data/ftpUser/pub/***</Value>
        <InfoType>trojan_path</InfoType>
        <Name>Trojan path</Name>
```

`j` `p` `/`

```xml
  </Details>
  <Details>
        <Type>text</Type>
        <Value>--</Value>
        <Name>Affected domain</Name>
  </Details>
  <Details>
        <Type>text</Type>
        <Value>2018-10-30 05:00:56</Value>
        <InfoType>frist_found_time</InfoType>
        <Name>First detected time<Name>
  </Details>
  <Details>
        <Type>text</Type>
        <Value>2018-10-30 11:43:45</Value>
        <InfoType>update_time</InfoType>
        <Name>Update time</Name>
  </Details>
  <Details>
        <Type>text</Type>
        <Value>Webshell</Value>
        <InfoType>trojan_type</InfoType>
        <Name>Trojan type</Name>
  </Details>
  <Details>
        <Type>html</Type>
        <Value>&lt;a href="http:// bucket*"&gt; Download&lt;/a&gt;</Value>
        <InfoType>download_url</InfoType>
        <Name>Source file download</Name>
  </Details>
  <InternetIp>1.2.3.5</InternetIp>
  <Level>serious</Level>
  <Id>129636</Id>
  <LastTime>2018-10-30 11:43:46</LastTime>
  <SasId>39938056</SasId>
</DescribeSuspEventDetailResponse>
```

`JSON` format `{`

```json
    "RequestId": "43F670F3-AB40-4E91-BC7D-C57468834F67",
    "EventDesc": "This file may have been uploaded by an attacker that has intruded int
o your website. Check the validity of this file.",
    "EventTypeDesc": "Webshell - Webshell",
    "EventStatus": 1,
    "EventName": "WEBSHELL",
    "SaleVersion": "1",
    "IntranetIp": "1.2.3.4",
    "DataSource": "aegis_suspicious_***",
    "InstanceName": "ca_***",
    "CanBeDealOnLine": true,
    "OperateMsg": "",
    "Uuid": "bffb12c3-590a-4db2-b538-***",
"Details":[
```

```json
    "Details": [
```

`{`

```json
            "Type": "text",
            "Value": "/data/ftpUser/pub/***",
            "InfoType": "trojan_path",
            "Name": "Trojan path",
```

`},` `{`

```json
            "Type": "text",
            "Value": "--",
            "Name": "Affected domain",
```

`},` `{`

```json
            "Type": "text",
            "Value": "2018-10-30 05:00:56",
            "InfoType": "frist_found_time",
            "Name": "First detected time",
```

`},` `{`

```json
            "Type": "text",
            "Value": "2018-10-30 11:43:45",
            "InfoType": "update_time",
            "Name": "Update time",
```

`},` `{`

```json
            "Type": "text",
            "Value": "Webshell",
            "InfoType": "trojan_type",
            "Name": "Trojan type",
```

`},` `{`

```json
            "Type": "html",
            "Value": "<a href=\" http:// ${* \"> Download </a>",
            "InfoType": "download_url",
            "Name":"Source file download",
```

`}` `],`

```json
    "InternetIp": "1.2.3.5",
    "Level": "serious",
    "Id": 129636,
    "LastTime": "2018-10-30 11:43:46",
    "SasId": "39938056"
```

`}`

**Error codes**

For a list of error codes, see Error codes.

### 6.4 Configuration assessment

#### 6.4.1 DescribeRiskItemType

Queries types of check items for cloud service configurations. Each check item is categorized into a type. Types of check items include identity authentication and permissions, network access control, log auditing, data security, monitoring and alerting, and basic security protection.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeRiskIte mType | The operation that you want to perform. Set the value to DescribeRiskItemType. |
| Lang | String | No | zh | The natural language of the request and response. Valid values: zh: Chinese en: English |
| SourceIp | String | No | 1.2.3.4 | The source IP address of the request. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| List | Array |   | The information about the check item. |
| Id | Long | 1 | The ID of the check item. |
| Title | String | Identity authentication and permissions | The type of the check item. Example: Identity authentication and permissions. |
| RequestId | String | 3B3F3A90-46A5- 4023-A2D8- D68B14262F96 | The ID of the request. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeRiskItemType &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeRiskItemType>
   <RequestId>3B3F3A90-46A5-4023-A2D8-D68B14262F96</RequestId>
   <List>
      <Title>Identity authentication and permissions</Title>
      <Id>1</Id>
   </List>
   <List>
      <Title>Network access control</Title>
      <Id>2</Id>
   </List>
   <List>
      <Title>Log auditing</Title>
      <Id>3</Id>
   </List>
   <List>
      <Title>Data security</Title>
      <Id>4</Id>
   </List>
   <List>
      <Title>Basic security protection</Title>
      <Id>6</Id>
   </List>
    </DescribeRiskItemType>
```

`JSON` format `{`

```json
 "RequestId":"3B3F3A90-46A5-4023-A2D8-D68B14262F96",
 "List":[
```

`{`

```json
   "Id":1,
   "Title":"Identity authentication and permissions"
```

`},` `{`

```json
   "Id":2,
   "Title":"Network access control"
```

`},` `{`

```json
   "Id":3,
   "Title":"Log auditing"
```

`},` `{`

```json
   "Id":4,
   "Title":"Data security"
```

`},` `{`

```json
   "Id":6,
   "Title":"Basic security protection"
```

`}` `]` `}`

**Error codes**

For a list of error codes, see Error codes.

#### 6.4.2 StartBaselineSecurityCheck

Checks cloud service configurations. You can check all items or a specific item, and you can verify whether an item is already checked.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | StartBaselineSe curityCheck | The operation that you want to perform. Set the value to StartBaselineSecurityCheck. |
| Type | String | Yes | check | The type of the check task. Valid values: check verify |
| SourceIp | String | No | 1.2.3.4 | The source IP address of the request. |
| Lang | String | No | zh | The natural language of the request and response. Valid values: zh: Chinese en: English |
| ItemIds.N | RepeatL ist | No | 1 | The ID of the check item. Note To perform the check task on cloud service configurations, you must provide the ID of the check item. You can call the DescribeRiskItemType operation to obtain the ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 48D2E9A9-A1B0- 4295-B727- 0995757C47E9 | The ID of the request. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=StartBaselineSecurityCheck &Type=check &<Common request parameters>
```

Sample success responses `XML` format

```xml
<StartBaselineSecurityCheckResponse>
  <RequestId>48D2E9A9-A1B0-4295-B727-0995757C47E9</RequestId>
</StartBaselineSecurityCheckResponse>
```

`JSON` format `{`

```json
    "RequestId":"48D2E9A9-A1B0-4295-B727-0995757C47E9"
```

`}`

**Error codes**

For a list of error codes, see Error codes.

#### 6.4.3 DescribeRiskCheckSummary

Queries the summary of check items for cloud service configurations. The operation returns the following information: the number of risk items, the risk rate, the number of affected assets, the last check time, and the statistics of each type of check items.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeRiskChe ckSummary | The operation that you want to perform. Set the value to DescribeRiskCheckSummary. |
| SourceIp | String | No | 1.2.3.4 | The source IP address of the request. |
| Lang | String | No | zh | The natural language of the request and response. Valid values: zh: Chinese en: English |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|

| RequestId | String | 291B49F9-1685- 4005-9D34- 606B6F78740F | The ID of the request. |
|---|---|---|---|
| RiskCheckSum mary | Struct |   | The summary of check items for cloud service configurations. |
| RiskCount | Integer | 1 | The number of risk items. |
| PreviousCount | Integer | 0 | The number of risk items in the last check. |
| ItemCount | Integer | 4 | The number of check items. |
| RiskRate | Float | 0.25 | The proportion of risk items in the total number to check items. |
| AffectedAsset Count | Integer | 0 | The number of affected assets. |
| PreviousTime | Long | 1545012926000 | The timestamp of the last check. |
| EnabledRiskCo unt | Integer | 3 | The number of check items that passed the check. |
| DisabledRiskC ount | Integer | 0 | The number of risk items that failed to pass the check. |
| RiskLevelCoun t | Array |   | The number of risk items for each level. high medium low |
| Key | String | medium | The severity level of the risk item. |
| Count | Integer | 1 | The number of risk items. |
| Groups | Array |   | The types of check items. |
| Id | Long | 1 | The type ID of the check item. |
| Title | String | Identity authentication and permissions | The type of the check item. |

| Status | String | finish | Indicates whether the check is finished. finish: The check is finished. Running: The check is in process. waiting: The check is pending. NoStart: The check is not started. |
|---|---|---|---|
| RemainingTim e | Integer | 0 | The time when the next check will be performed. |
| Sort | Integer | 1 | The sequence number of the check item type in the All Types drop-down list in the console. |
| CountByStatus | Array |   | The statistics of check results. |
| Status | String | pass | The status of the check item after the check is finished. Valid values: pass: The check item is normal. failed: The check item is at risk. |
| Count | Integer | 2 | The number of risk items. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeRiskCheckSummary &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeRiskCheckSummary>
      <RequestId>291B49F9-1685-4005-9D34-606B6F78740F</RequestId>
      <RiskCheckSummary>
            <RiskCount>1</RiskCount>
            <RiskRate>0.25</RiskRate>
            <PreviousTime>1545012926000</PreviousTime>
            <ItemCount>4</ItemCount>
            <AffectedAssetCount>0</AffectedAssetCount>
            <RiskLevelCount>
                  <Count>1</Count>
                  <Key>medium</Key>
            </RiskLevelCount>
            <Groups>
                  <Status>finish</Status>
                  <CountByStatus>
                        <Status>exception</Status>
                        <Count>2</Count>
```

```xml
Cout /Cout
                  </CountByStatus>
                  <RemainingTime>0</RemainingTime>
                  <Sort>1</Sort>
                  <Title>Identity authentication and permissions</Title>
                  <Id>1</Id>
            </Groups>
            <Groups>
                  <Status>finish</Status>
                  <CountByStatus>
                        <Status>exception</Status>
                        <Count>5</Count>
                  </CountByStatus>
                  <RemainingTime>0</RemainingTime>
                  <Sort>2</Sort>
                  <Title>Network access control</Title>
                  <Id>2</Id>
            </Groups>
            <Groups>
                  <Status>finish</Status>
                  <CountByStatus>
                        <Status>pass</Status>
                        <Count>1</Count>
                  </CountByStatus>
                  <RemainingTime>0</RemainingTime>
                  <Sort>3</Sort>
                  <Title>Log auditing</Title>
                  <Id>3</Id>
            </Groups>
            <Groups>
                  <Status>finish</Status>
                  <CountByStatus>
                        <Status>exception</Status>
                        <Count>2</Count>
                  </CountByStatus>
                  <RemainingTime>0</RemainingTime>
                  <Sort>4</Sort>
                  <Title>Data security</Title>
                  <Id>4</Id>
            </Groups>
            <Groups>
                  <Status>finish</Status>
                  <CountByStatus>
                        <Status>exception</Status>
                        <Count>2</Count>
                  </CountByStatus>
                  <RemainingTime>0</RemainingTime>
                  <Sort>6</Sort>
                  <Title>Basic security protection</Title>
                  <Id>6</Id>
            </Groups>
            <PreviousCount>0</PreviousCount>
      </RiskCheckSummary>
    </DescribeRiskCheckSummary>
```

`JSON` format `{`

```json
  "RequestId": "291B49F9-1685-4005-9D34-606B6F78740F",
  "RiskCheckSummary": {
    "RiskCount": 1,
    "RiskRate": 0.25,
    "PreviousTime": 1545012926000,
    "ItemCount": 4,
    "AffectedAssetCount": 0,
    "RiskLevelCount": [
```

`{`

```json
        "Count": 1,
        "Key": "medium"
```

`}` `],`

```json
    "Groups": [
```

`{`

```json
        "Status": "finish",
        "CountByStatus": [
```

`{`

```json
            "Status": "exception",
            "Count": 2
```

`}` `],`

```json
        "RemainingTime": 0,
        "Sort": 1,
        "Title": "Identity authentication and permissions",
        "Id": 1
```

`},` `{`

```json
        "Status": "finish",
        "CountByStatus": [
```

`{`

```json
            "Status": "exception",
            "Count": 5
```

`}` `],`

```json
        "RemainingTime": 0,
        "Sort": 2,
        "Title": "Network access control",
        "Id": 2
```

`},` `{`

```json
        "Status": "finish",
        "CountByStatus": [
```

`{`

```json
            "Status": "pass",
            "Count": 1
```

`}` `],`

```json
        "RemainingTime": 0,
        "Sort": 3,
        "Title": "Log auditing",
```

```json
        "Id": 3
```

`},` `{`

```json
        "Status": "finish",
        "CountByStatus": [
```

`{`

```json
            "Status": "exception",
            "Count": 2
```

`}` `],`

```json
        "RemainingTime": 0,
        "Sort": 4,
        "Title": "Data security",
        "Id": 4
```

`},` `{`

```json
        "Status": "finish",
        "CountByStatus": [
```

`{`

```json
            "Status": "exception",
            "Count": 2
```

`}` `],`

```json
        "RemainingTime": 0,
        "Sort": 6,
        "Title": "Basic security protection",
        "Id": 6
```

`}` `],`

```json
    "PreviousCount": 0
```

`}` `}`

**Error codes**

For a list of error codes, see Error codes.

#### 6.4.4 DescribeRiskCheckResult

Queries the results of check items by type or name.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeRiskChe ckResult | The operation that you want to perform. Set the value to DescribeRiskCheckResult. |

| SourceIp | String | No | 1.2.3.4 | The source IP address of the request. |
|---|---|---|---|---|
| Lang | String | No | zh | The natural language of the request and response. Valid values: zh: Chinese en: English |
| GroupId | Long | No | 21000 | The type ID of the check item. Valid values: 1: identity authentication and permissions 2: network access control 3: log audit 4: data security 5: monitoring and alerting 6: basic security protection |
| CurrentPage | Integer | No | 1 | The page number of the current page. |
| RiskLevel | String | No | high | The risk level of the check item. Valid values: high medium low |
| Status | String | No | pass | The status of the check result. Valid values: pass failed running waiting ignored falsePositive |
| ItemIds.N | RepeatL ist | No | sde*** | The ID of check item N. For more information about the description of the check item specified by this parameter, see the check item table in the "Response parameters" section of this topic. |
| AssetType | String | No | RDS | The type of the cloud service. For more information about the description of the cloud service specified by this parameter, see the check item table in the "Response parameters" section of this topic. |

| Name | String | No | Cloud platform - Multi-factor authentication (MFA) configuration of Apsara Stack tenant accounts | The name of the check item. For more information about the description of the check item name, see the check item table in the "Response parameters" section of this topic. |
|---|---|---|---|---|
| PageSize | Integer | No | 10 | The number of entries to return on each page. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Count | Integer | 10 | The number of entries returned on the current page. |
| CurrentPage | Integer | 1 | The page number of the current page. |
| List | Array |   | The information about the check item. |
| AffectedCount | Integer | 0 | The number of the affected assets. |
| CheckTime | Long | 1543991525000 | The time when the last check was performed. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since the epoch time January 1, 1970, 00:00:00 UTC. |
| ItemId | Long | 1 | The ID of the check item. For more information about the description of the check item specified by this parameter, see the check item table in the "Response parameters" section of this topic. |
| RemainingTim e | Integer | 0 | The time when the next check will be performed. |
| RepairStatus | String | disabled | Indicates whether the risk of the check item can be fixed. Valid values: enabled: The risk can be fixed. disabled: The risk cannot be fixed. |
| RiskAssertTyp e | String | ECS | The type of the affected asset. |
| RiskItemResou rces | Array |   | The details of the check item. |

| ContentResour ce | Json | {"type": "link", "value": "Risk: MFA is disabled\n", "url": "https://***.aliyun.c om/#/secure\n" } | The content in the check item details. |
|---|---|---|---|
| ResourceNam e | String | bestPractice | The title in the check item details. Valid values: bestPractice: description influence: risk suggestion: solution helpResource: reference |
| RiskLevel | String | high | The risk level of the check item. Valid values: high medium low |
| Sort | Integer | 1 | The sequence number of the check result. The check items are sorted based on the sequence number. |
| StartStatus | String | enabled | Indicates whether the check item is supported by the cloud service. Valid values: enabled: supported disable: unsupported |
| Status | String | pass | The status of the check result. Valid values: pass failed running waiting ignored falsePositive |
| TaskId | Long | 647189 | The ID of the check task. |
| Title | String | Cloud platform - MFA configuration of Apsara Stack tenant accounts | The name of the check item. |

| Type | String | Identity authentication and permissions | The type of the check item. Valid values: Identity authentication and permissions Network access control Log audit Data security Monitoring and alerting Basic security protection |
|---|---|---|---|
| PageCount | Integer | 20 | The total number of pages returned. |
| PageSize | Integer | 10 | The number of entries returned per page. |
| RequestId | String | AD271C07-4ACE- 413D-AA9B- F14FD3B7717F | The ID of the request. |
| TotalCount | Integer | 12 | The total number of entries returned. |

The following table describes the check items supported by the cloud platform, including the ID, name, type, risk level, and service type.

| ItemId | Name | GroupId | RiskLevel | AssetType | Description |
|---|---|---|---|---|---|
| 1 | ActionTrail - Logging configuration | 3: log audit | medium | ActionTrail | Checks whether you enable ActionTrail to record operations logs on the cloud and save the logs to Object Storage Service (OSS) buckets. |

| 2 | ApsaraDB RDS - Database security policy | 4: data security | medium | RDS | Checks whether you enable Secure Sockets Layer (SSL), Transparent Data Encryption (TDE), and SQL audit services for each ApsaraDB RDS instance. |
|---|---|---|---|---|---|
| 3 | Apsara Stack tenant account security - MFA | 1: identity authenticatio n and permissions | high | RAM | Checks whether MFA is enabled for Apsara Stack tenant accounts. |

| 4 | Apsara Stack Security - Back-to-origin configuration s of Anti- DDoS Pro or Anti-DDoS Premium | 2: network access control | high | DDOS | Checks whether actual IP addresses of backend servers are hidden after you use Anti- DDoS Pro or Anti-DDoS Premium. If the actual IP addresses are hidden, attackers cannot directly access the actual IP addresses. <note> To hide the actual IP addresses, you can |
|---|---|---|---|---|---|
|   |   |   |   |   | configure whitelist policies, for example, when the actual IP addresses are the IP addresses of Server Load Balancer (SLB) instances. When the IP addresses are the IP addresses of Elastic Compute Service (ECS) instances, you can configure access control policies for ECS security groups. All these policies allow access from only back-to-origin IP addresses of Anti-DDoS Pro or Anti- DDoS Premium. </note> |

| 5 | ApsaraDB RDS - Whitelist configuration | 2: network access control | high | RDS | Checks whether the RDS access control policy is set to 0.0.0.0/0, which allows requests from all IP addresses. We recommend that you limit the access scope to a specific range of IP addresses rather than exposing database services to the Internet. |
|---|---|---|---|---|---|
| 6 | SLB - High- risk port | 2: network access control | high | SLB | Checks whether SLB forwards requests from high-risk ports to the Internet. |

|   |   |   |   |   | Checks |
|---|---|---|---|---|---|
| 7 | Apsara Stack Security - Back-to-origin configuration s of Web Application Firewall (WAF) | 2: network access control | high | WAF | whether the actual IP addresses of backend servers are hidden after you use WAF. If the actual IP addresses are hidden, attackers cannot directly access the actual IP addresses. To hide the actual IP addresses, you can configure whitelist policies, for example, when the actual IP addresses are the IP addresses of SLB instances. When the IP addresses are the IP addresses of ECS instances, you can configure access control policies for ECS security groups. All these policies allow access from only back-to-origin IP addresses of WAF. |

| 8 | Apsara Stack Security - Threat Detection Service agent online status | 6: basic security protection | high | ECS | Checks whether the Threat Detection Service agent on the ECS instance is always online and provides protection. |
|---|---|---|---|---|---|
| 12 | OSS - Bucket access permissions | 4: data security | high | OSS | Checks whether the access permission on your OSS buckets is public-read or public-read- write. If yes, the check fails. |
| 13 | Threat Detection Service - AccessKey leak detection | 5: monitoring and alerting | medium | RAM | Checks whether AccessKey leak detection is enabled. If no, the check fails. |
| 14 | ApsaraDB for MongoDB - Whitelist configuration | 2: network access control | high | MongoDB | Checks whether the whitelist is enabled for ApsaraDB for MongDB instances. If the whitelist is enabled and set to 0.0.0.0/0, which allows access from all devices, the check fails. |
| 15 | RAM - MFA configuration for RAM users | 1: identity authenticatio n and permissions | medium | RAM | Checks whether MFA is enabled for RAM users. |

| 16 | OSS - Logging configuration | 4: data security | medium | OSS | Checks whether the logging feature is enabled for all OSS buckets. If no, the check fails. |
|---|---|---|---|---|---|
| 17 | OSS - Cross- region replication configuration | 4: data security | low | OSS | Checks whether the cross-region replication is enabled for all OSS buckets. If no, the check fails. |
| 18 | ApsaraDB RDS - Backup configuration | 4: data security | medium | RDS | Checks whether database backup is enabled for ApsaraDB RDS instances. If no, the check fails. |
| 19 | KVStore for Redis - Whitelist configuration | 2: network access control | high | Redis | Checks access control configuration s of KVStore for Redis. |
| 20 | ECS - SSH key pairs | 1: identity authenticatio n and permissions | medium | ECS | Checks whether SSH key pair- based logons are enabled for ECS instances. |

| 21 | SLB - Health status | 5: monitoring and alerting | low | SLB | Checks the health status of SLB instances. |
|---|---|---|---|---|---|
| 22 | PolarDB - Whitelist configuration | 2: network access control | medium | POLARDB | Checks the whitelist configured for PolarDB. If the whitelist is enabled and set to 0.0.0.0/0, which allows access from all devices, the check fails. |
| 23 | AnalyticDB for PostgreSQL - Whitelist configuration | 2: network access control | medium | PostgreSQL | Checks the whitelist configured for AnalyticDB for PostgreSQL instances. If the whitelist is enabled and set to 0.0.0.0/0, which allows access from all devices, the check fails. |
| 24 | ECS - Storage encryption | 4: data security | low | ECS | Checks whether storage encryption is enabled. If no, the check fails. |
| 25 | SLB - Whitelist configuration | 2: network access control | medium | SLB | Checks SLB whitelist configuration s. If the whitelist is enabled and set to 0.0.0.0/0, which allows access from all devices, the check fails. |

| 26 | SLB - Certificate expiration | 5: monitoring and alerting | medium | SLB | Checks whether the SLB certificate has expired. |
|---|---|---|---|---|---|
| 27 | ECS - Automatic snapshot policy | 4: data security | medium | ECS | Checks whether automatic snapshot policies are enabled for ECS instances. |
| 28 | SSL certificate - Expiration check | 4: data security | medium | SSL | Checks whether the SSL certificate is within its validity period. |
| 30 | OSS - Server- side encryption | 4: data security | low | OSS | Checks whether server-side encryption is enabled for OSS buckets. |
| 31 | OSS - Hotlink protection | 2: network access control | low | OSS | Checks whether hotlink protection is configured for OSS buckets. |
| 32 | ApsaraDB RDS - Cross- region backup configuration | 4: data security | low | RDS | Checks whether cross-region backup is configured for ApsaraDB RDS instances. |
| 33 | ApsaraDB for MongoDB - Backup configuration | 4: data security | medium | MongoDB | Checks whether data backup is enabled for ApsaraDB for MongoDB instances. |

| 34 | ApsaraDB for MongoDB - Log audit | 3: log audit | medium | MongoDB | Checks whether log audit is enabled for ApsaraDB for MongoDB instances. |
|---|---|---|---|---|---|
| 35 | ApsaraDB for MongoDB - SSL certificate | 4: data security | medium | MongoDB | Checks whether SSL certificate checks are enabled for ApsaraDB for MongoDB instances. |
| 36 | Cloud Monitor - Host monitoring plug-in | 5: monitoring and alerting | medium | CloudMonitor | Checks whether the status of the Cloud Monitor agent is normal. |
| 37 | ECS - Security group policies | 2: network access control | medium | ECS | Checks the ECS security group policies. |
| 38 | VPC - DNAT management port mapping | 2: network access control | medium | VPC | Checks whether a VPC DNAT rule is configured to map management ports to the Internet. |
| 39 | KVStore for Redis - Backup configuration | 4: data security | medium | Redis | Checks whether data backup is enabled for KVStore for Redis. |
| 40 | Container Registry - Repository permission configuration s | 4: data security | high | CR | Checks whether permissions are correctly configured for the repository in Container Registry. |

| 41 | Container Registry - Security scan | 6: basic security protection | low | CR | Checks whether security scan is enabled for Container Registry. |
|---|---|---|---|---|---|
| 42 | SLB - Access logging configuration | 3: log audit | medium | SLB | Checks whether access logging is configured for SLB instances. |
| 43 | KVStore for Redis - Log audit | 3: log audit | low | Redis | Checks whether log audit is configured for KVStore for Redis. |
| 44 | OSS - Authorization policy | 1: identity authenticatio n and permissions | medium | OSS | Checks whether correct authorization policies are enabled for OSS. |
| 46 | PolarDB - Backup configuration | 4: data security | medium | POLARDB | Checks whether the backup configuration is enabled for PolarDB. |
| 47 | PolarDB - SQL explorer | 3: log audit | medium | POLARDB | Checks whether SQL Explorer is enabled for PolarDB. |
| 48 | Apsara Stack tenant account security - AccessKey pair | 1: identity authenticatio n and permissions | medium | RAM | Checks whether the AccessKey pair is enabled for your Apsara Stack tenant account. |

| 50 | CDN - Real- time logging | 3: log audit | medium | CDN | Checks whether real- time logging push is enabled for CDN. |
|---|---|---|---|---|---|
| 51 | KVStore for Redis - SSL certificate | 4: data security | medium | Redis | Checks whether KVStore for Redis uses SSL certificates. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeRiskCheckResult &GroupId=1 &RiskLevel=high &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeRiskCheckResultResponse>
      <TotalCount>12</TotalCount>
      <RequestId>AD271C07-4ACE-413D-AA9B-F14FD3B7717F</RequestId>
      <PageCount>20</PageCount>
      <PageSize>10</PageSize>
      <CurrentPage>1</CurrentPage>
      <List>
            <Status>pass</Status>
            <CheckTime>1543991525000</CheckTime>
            <TaskId>647189</TaskId>
            <RemainingTime>0</RemainingTime>
            <Title>Cloud platform - MFA configuration of Apsara Stack tenant
accounts</Title>
            <ItemId>1</ItemId>
            <RiskAssertType>ECS</RiskAssertType>
            <Type>Identity authentication and permissions</Type>
            <StartStatus>enabled</StartStatus>
            <AffectedCount>0</AffectedCount>
            <Sort>1</Sort>
            <RepairStatus>disabled</RepairStatus>
            <RiskLevel>high</RiskLevel>
            <RiskItemResources>
                  <ContentResource>{   "type": "link",   "value": "Risk: MFA is disabled
\n", "url": "https://***.aliyun.com/#/secure\n" }</ContentResource>
                  <ResourceName>bestPractice</ResourceName>
            </RiskItemResources>
      </List>
      <Count>10</Count>
</DescribeRiskCheckResultResponse>
```

`JSON` format `{`

```json
    "TotalCount": "12",
    "RequestId": "AD271C07-4ACE-413D-AA9B-F14FD3B7717F",
    "PageCount": "20",
    "PageSize": "10",
    "CurrentPage": "1",
    "List": {
            "Status": "pass",
            "CheckTime": "1543991525000",
            "TaskId": "647189",
            "RemainingTime": "0",
            "Title": "Cloud platform - MFA configuration of Apsara Stack tenant
accounts",
            "ItemId": "1",
            "RiskAssertType": "ECS",
            "Type": "Identity authentication and permissions",
            "StartStatus": "enabled",
            "AffectedCount": "0",
            "Sort": "1",
            "RepairStatus": "disabled",
            "RiskLevel": "high",
            "RiskItemResources": {
                "ContentResource": "{   \"type\": \"link\",   \"value\": \"Risk: MFA is
disabled\\n\", \"url\": \"https://***.aliyun.com/#/secure\\n\" }",
                "ResourceName": "bestPractice"
```

`}` `},`

```json
    "Count": "10"
```

`}`

**Error codes**

For a list of error codes, see Error codes.

#### 6.4.5 DescribeSecurityCheckScheduleConfig

Queries the custom check cycle and time period.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeSecurit yCheckSchedule Config | The operation that you want to perform. Set the value to DescribeSecurityCheckScheduleConfi g. |
| Lang | String | No | zh | The natural language of the request and response. Valid values: zh: Chinese en: English |

| SourceIp | String | No | 1.2.3.4 | The source IP address of the request. |
|---|---|---|---|---|

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 48D2E9A9-A1B0- 4295-B727- 0995757C47E9 | The ID of the request. |
| RiskCheckJobC onfig |   |   | The settings of scheduled checks. |
| DaysOfWeek | String | 1,2,3 | The days when checks are performed every week. You can specify multiple days. Separate multiple days with commas (,). Valid values: 1: Monday 2: Tuesday 3: Wednesday 4: Thursday 5: Friday 6: Saturday 7: Sunday |
| EndTime | Integer | 12 | The time period during which the configuration check ends. Valid values: 6: 00:00 to 06:00 12: 06:00 to 12:00 18: 12:00 to 18:00 24: 18:00 to 24:00 |
| StartTime | Integer | 6 | The time period during which the configuration check starts. Valid values: 0: 00:00 to 06:00 6: 06:00 to 12:00 12: 12:00 to 18:00 18: 18:00 to 24:00 |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeSecurityCheckScheduleConfig &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeSecurityCheckScheduleConfig>
  <RiskCheckJobConfig>
        <DaysOfWeek>1,2,3</DaysOfWeek>
        <EndTime>12</EndTime>
        <StartTime>6</StartTime>
  </RiskCheckJobConfig>
  <RequestId>C17F3C01-0AFD-4898-A950-AA0129025B41</RequestId>
</DescribeSecurityCheckScheduleConfig>
```

`JSON` format `{`

```json
 "RequestId":"C17F3C01-0AFD-4898-A950-AA0129025B41",
 "RiskCheckJobConfig":{
  "DaysOfWeek":"1,2,3",
  "EndTime":12,
  "StartTime":6
```

`}` `}`

**Error codes**

For a list of error codes, see Error codes.

### 6.5 Vulnerability management

#### 6.5.1 DescribeVulList

Queries vulnerabilities by type.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeVulList | The operation that you want to perform. Set the value to DescribeVulList. |
| Type | String | Yes | cve | The type of the vulnerability. Valid values: cve: Linux software vulnerabilities sys: Windows vulnerabilities cms: Web CMS vulnerabilities app: application vulnerabilities emg: emergency vulnerabilities |

| Lang | String | No | zh | The natural language of the request and response. Valid values: zh: Chinese en: English |
|---|---|---|---|---|
| Remark | String | No | 1.2.3.4 | The tag to query, which can be the internal IP address, public IP address, or name of the asset. |
| Uuids | String | No | 1587bedb-fdb4- 48c4-9330- ************ | The ID of the asset. Separate multiple IDs with commas (,). |
| AliasName | String | No | RHSA- 2019:0230- Important: polkit security update | The alias of the vulnerability. |
| Necessity | String | No | asap,later,nntf | The priority to fix vulnerabilities. Separate multiple priorities with commas (,). Valid values: asap: high later: medium nntf: low |
| Dealed | String | No | n | Specifies whether the vulnerability is handled. Valid values: y: handled n: unhandled |
| CurrentPage | Integer | No | 1 | The page number of the current page. Pages start from page 1. Default value: 1. |
| PageSize | Integer | No | 20 | The number of entries to return on each page. Default value: 20. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | ECDE6715-6286- 40E6-A32D- 3094051FD74D | The ID of the request. |
| CurrentPage | Integer | 1 | The page number of the current page. |
| PageSize | Integer | 20 | The number of entries returned per page. |

| TotalCount | Integer | 2 | The total number of entries returned. |
|---|---|---|---|
| VulRecords | Array |   | The vulnerability information. |
| AliasName | String | RHSA-2017:0574: gnutls security, bug fix, and enhancement update | The alias of the vulnerability. |
| ExtendContent Json | Struct |   | The extended information. |
| AbsolutePath | String | /roo/www/web | The package path of the software that has the vulnerability. |
| AliasName | String | RHSA-2017:0574: gnutls security, bug fix, and enhancement update | The alias of the vulnerability. |
| Ip | String | 1.2.3.1 | The public IP address of the asset that is affected by the vulnerability. |
| LastTs | Long | 1554189334000 | The timestamp when the vulnerability was last detected. |
| Necessity | Struct |   | Indicates whether the vulnerability needs to be fixed. |
| Assets factor _ | String | 1 | The asset score. |
| Cvss factor _ | String | 7.8 | The Common Vulnerability Scoring System (CVSS) score. |
| Enviroment fa _ ctor | String | 1.0 | The environmental score. |
| Gmt create _ | String | 20190331 | The creation time. |
| Is calc _ | String | 1 | Indicates whether the vulnerability severity score is calculated. Valid values: 0: The score is not calculated. 1: The score is calculated. |

| Status | String | normal | The status of the vulnerability severity score. Valid values: none: No score is generated. pending: The score is pending calculation. miss: The score failed to be calculated. normal: The calculation is normal. |
|---|---|---|---|
| Time factor _ | String | 1.0 | The temporal score. |
| Total score _ | String | 7.8 | The total vulnerability severity score. We recommend that you apply the following rules: Critical: The severity score is between 13.5 and 15, which typically represents a high-risk vulnerability. Important: The severity score is between 7.1 and 13.5, which typically represents a medium-risk vulnerability. Moderate: The severity score is below 7, which typically represents a low-risk vulnerability. |
| Os | String | centos | The operating system. |
| OsRelease | String | 7 | The version of the operating system. |
| PrimaryId | Long | 111 | The ID of the vulnerability. |
| RpmEntityList | Array |   | The details about the RPM package. |
| FullVersion | String | 3.10.0-693.2.2.el7 | The complete version number. |
| MatchDetail | String | python-perf version less than 0:3.10.0- 693.21.1.el7 | The detailed matching information of the vulnerability. |
| Name | String | python-perf | The name of the RPM package. |
| Path | String | /usr/lib64/python2. 7/site-packages | The path of the software that has the vulnerability. |
| UpdateCmd | String | *** update python- perf | The command that can be run to fix the vulnerability. |

| Version | String | 3.10.0 | The version of the operating system. |
|---|---|---|---|
| Status | Integer | 1 | The status of the vulnerability. Valid values: 1: unfixed 2: fix failed 3: rollback failed 4: fixing 5: rolling back 6: verifying 7: fixed 8: fixed and to be restarted 9: rolled back 10: ignored 11: rolled back and to be restarted 12: not found 20: expired |
| Tag | String | oval | The tag of the vulnerability. |
| cveList | List | ["CVE-2016-8610", "CVE-2017-5335" ] | The Common Vulnerabilities and Exposures (CVEs) list. |
| FirstTs | Long | 1554189334000 | The first time when the vulnerability was detected. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since the epoch time January 1, 1970, 00:00:00 UTC. |
| GroupId | Integer | 281801 | The ID of the asset group. |
| InstanceId | String | i-bp18t*** | The ID of the asset instance. |
| InstanceName | String | Test ECS | The name of the asset instance. |
| InternetIp | String | 1.2.3.1 | The public IP address of the asset. |
| IntranetIp | String | 1.2.3.4 | The private IP address of the asset. |
| LastTs | Long | 1541207563000 | The timestamp when the vulnerability was last detected. |

| ModifyTs | Long | 1541207563000 | The timestamp when the vulnerability was modified. |
|---|---|---|---|
| Name | String | oval:com.redhat.rh sa:def:20170574 | The name of the vulnerability. |
| Necessity | String | asap | The priority to fix vulnerabilities. Valid values: asap: high later: medium nntf: low Note We recommend that you fix the high-level vulnerabilities as soon as possible. |
| Online | Boolean | true | Indicates whether the asset instance is online. Valid values: true: online false: offline |
| OsVersion | String | linux | The version of the operating system. |
| PrimaryId | Long | 101162078 | The ID of the vulnerability. |
| Related | String | CVE-2017- 7518,CVE-2017- 12188 | The list of CVEs related to the vulnerability. Separate multiple CVEs with commas (,). |
| RepairTs | Long | 1541207563000 | The timestamp when the vulnerability was fixed. |
| ResultCode | String | 0 | The result code returned after the vulnerability is fixed. |
| ResultMessage | String | timeout | The message returned after the vulnerability is fixed. |

| Status | Integer | 1 | The status of the vulnerability. Valid values: 1: unfixed 2: fix failed 3: rollback failed 4: fixing 5: rolling back 6: verifying 7: fixed 8: fixed and to be restarted 9: rolled back 10: ignored 11: rolled back and to be restarted 12: not found 20: expired |
|---|---|---|---|
| Tag | String | oval | The tag of the vulnerability. |
| Type | String | cve | The type of the vulnerability. Valid values: cve: Linux vulnerabilities sys: Windows vulnerabilities cms: Web CMS vulnerabilities emg: emergency vulnerabilities app: application vulnerabilities |
| Uuid | String | 04c56617-23fc- 43a5-ab9b- ************ | The ID of the asset. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeVulList &Type=cve &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeVulListResponse>
      <TotalCount>2</TotalCount>
      <RequestId>ECDE6715-6286-40E6-A32D-3094051FD74D</RequestId>
      <PageSize>20</PageSize>
      <VulRecords>
            <Status>1</Status>
            <InstanceId>i-bp18t***</InstanceId>
            <OsVersion>linux</OsVersion>
            <LastTs>1541207563000</LastTs>
            <Necessity>asap</Necessity>
```

```xml
            <ResultMessage>timeout</ResultMessage>
            <IntranetIp>1.2.3.4</IntranetIp>
            <Name>oval:com.redhat.rhsa:def:20170574</Name>
            <GroupId>281801</GroupId>
            <RepairTs>1541207563000</RepairTs>
            <InstanceName>Test ECS</InstanceName>
            <Type>cve</Type>
            <FirstTs>1554189334000</FirstTs>
            <Uuid>04c56617-23fc-43a5-ab9b-************</Uuid>
            <Related>CVE-2017-7518,CVE-2017-12188</Related>
            <ModifyTs>1541207563000</ModifyTs>
            <InternetIp>1.2.3.1</InternetIp>
            <AliasName>RHSA-2017:0574: gnutls security, bug fix, and enhancement
update</AliasName>
            <Tag>oval</Tag>
            <Online>true</Online>
            <PrimaryId>101162078</PrimaryId>
            <ResultCode>0</ResultCode>
      </VulRecords>
      <VulRecords>
            <ExtendContentJson>
                  <Status>1</Status>
                  <Os>centos</Os>
                  <AliasName>RHSA-2017:0574: gnutls security, bug fix, and enhancement
update</AliasName>
                  <Ip>1.2.3.1</Ip>
                  <LastTs>1554189334000</LastTs>
                  <cveList>["CVE-2016-8610", "CVE-2017-5335" ]</cveList>
                  <Necessity>
                        <Status>normal</Status>
                        <Total_score>7.8</Total_score>
                        <Gmt_create>20190331</Gmt_create>
                        <Cvss_factor>7.8</Cvss_factor>
                        <Time_factor>1.0</Time_factor>
                        <Is_calc>1</Is_calc>
                        <Enviroment_factor>1.0</Enviroment_factor>
                        <Assets_factor>1</Assets_factor>
                  </Necessity>
                  <RpmEntityList>
                        <Path>/usr/lib64/python2.7/site-packages</Path>
                        <UpdateCmd>*** update python-perf</UpdateCmd>
                        <Version>3.10.0</Version>
                        <FullVersion>3.10.0-693.2.2.el7</FullVersion>
                        <MatchDetail>python-perf version less than 0:3.10.0-
693.21.1.el7</MatchDetail>
                        <Name>python-perf</Name>
                  </RpmEntityList>
                  <Tag>oval</Tag>
                  <OsRelease>7</OsRelease>
                  <AbsolutePath>/roo/www/web</AbsolutePath>
                  <PrimaryId>111</PrimaryId>
            </ExtendContentJson>
      </VulRecords>
      <CurrentPage>1</CurrentPage>
```

```
</DescribeVulListResponse>
```

`JSON` format `{`

```json
        "TotalCount": "2",
        "RequestId": "ECDE6715-6286-40E6-A32D-3094051FD74D",
        "PageSize": "20",
        "VulRecords": [{
            "Status": "1",
            "InstanceId": "i-bp18t***",
            "OsVersion": "linux",
            "LastTs": "1541207563000",
            "Necessity": "asap",
            "ResultMessage": "timeout",
            "IntranetIp": "1.2.3.4",
            "Name": "oval:com.redhat.rhsa:def:20170574",
            "GroupId": "281801",
            "RepairTs": "1541207563000",
            "InstanceName": "Test ECS",
            "Type": "cve",
            "FirstTs": "1554189334000",
            "Uuid": "04c56617-23fc-43a5-ab9b-************",
            "Related": "CVE-2017-7518,CVE-2017-12188",
            "ModifyTs": "1541207563000",
            "InternetIp": "1.2.3.1",
            "AliasName": "RHSA-2017:0574: gnutls security, bug fix, and enhancement upd
ate",
            "Tag": "oval",
            "Online": "true",
            "PrimaryId": "101162078",
            "ResultCode": "0"
        }, {
            "ExtendContentJson": {
                "Status": "1",
                "Os": "centos",
                "AliasName": "RHSA-2017:0574: gnutls security, bug fix, and enhancement
update",
                "Ip": "1.2.3.1",
                "LastTs": "1554189334000",
                "cveList": "[\"CVE-2016-8610\", \"CVE-2017-5335\" ]",
                "Necessity": {
                    "Status": "normal",
                    "Total_score": "7.8",
                    "Gmt_create": "20190331",
                    "Cvss_factor": "7.8",
                    "Time_factor": "1.0",
                    "Is_calc": "1",
                    "Enviroment_factor": "1.0",
                    "Assets_factor": "1"
```

`},`

```json
                "RpmEntityList": [{
                    "Path": "/usr/lib64/python2.7/site-packages",
                    "UpdateCmd": "*** update python-perf",
```

`p` `p` `py` `p` `,`

```json
                    "Version": "3.10.0",
                    "FullVersion": "3.10.0-693.2.2.el7",
                    "MatchDetail": "python-perf version less than 0:3.10.0-693.21.1.el7"
```

`,`

```json
                    "Name": "python-perf"
                }],
                "Tag": "oval",
                "OsRelease": "7",
                "AbsolutePath": "/roo/www/web",
                "PrimaryId": "111"
```

`}`

```json
        }],
        "CurrentPage": "1"
```

`}`

**Error codes**

For a list of error codes, see Error codes.

#### 6.5.2 DescribeVulWhitelist

Queries the whitelist of vulnerabilities by page.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeVulWhit elist | The operation that you want to perform. Set the value to DescribeVulWhitelist. |
| CurrentPage | Integer | No | 1 | The number of the page to return. Pages start from page 1. Default value: 1. |
| PageSize | Integer | No | 10 | The number of entries to return on each page. Default value: 20. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| CurrentPage | Integer | 1 | The page number of the current page. |
| PageSize | Integer | 10 | The number of entries returned per page. |

| RequestId | String | 74F97EF7-B543- 43FD-A4E9- 18456731F9C5 | The ID of the request. |
|---|---|---|---|
| TotalCount | Integer | 1 | The total number of returned entries. |
| VulWhitelists | Array |   | The information about the vulnerability whitelist. |
| AliasName | String | RHSA-2017:3263: curl security update | The alias of the vulnerability. |
| Name | String | oval:com.redhat.rh sa:def:20173263 | The name of the vulnerability. |
| Reason | String | Not urgent | The reason for adding the vulnerability to the whitelist. |
| Type | String | cve | The type of the vulnerability. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeVulWhitelist &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeVulWhitelist>
  <TotalCount>1</TotalCount>
  <VulWhitelists>
        <Name>oval:com.redhat.rhsa:def:20173263</Name>
        <AliasName>RHSA-2017:3263: curl security update</AliasName>
        <Type>cve</Type>
        <Reason>Not urgent</Reason>
  </VulWhitelists>
  <PageSize>3</PageSize>
  <RequestId>74F97EF7-B543-43FD-A4E9-18456731F9C5</RequestId>
  <CurrentPage>1</CurrentPage>
</DescribeVulWhitelist>
```

`JSON` format `{`

```json
 "TotalCount":1,
 "PageSize":3,
 "VulWhitelists":[
```

`{`

```json
   "Name":"oval:com.redhat.rhsa:def:20173263",
   "AliasName":"RHSA-2017:3263: curl security update",
   "Type":"cve",
   "Reason":"Not urgent"
```

`}` `],`

```json
 "RequestId":"74F97EF7-B543-43FD-A4E9-18456731F9C5",
 "CurrentPage":1
```

`}`

**Error codes**

For a list of error codes, see Error codes.

#### 6.5.3 DescribeConcernNecessity

Queries the priority to fix the vulnerability.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeConcer nNecessity | The operation that you want to perform. Set the value to DescribeConcernNecessity. |
| Lang | String | No | zh | The natural language of the request and response. Valid values: zh: Chinese en: English |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| ConcernNeces sity | List | [ "asap", "later", "nntf"] | The priority to fix the vulnerability. Valid values: asap: high later: medium nntf: low |
| RequestId | String | 9139DAF6-5CE0- 49A0-926E- 07243A290F70 | The ID of the request. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeConcernNecessity &Lang=zh &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeConcernNecessity>
  <ConcernNecessity>asap</ConcernNecessity>
  <ConcernNecessity>later</ConcernNecessity>
  <ConcernNecessity>nntf</ConcernNecessity>
  <RequestId>9139DAF6-5CE0-49A0-926E-07243A290F70</RequestId>
</DescribeConcernNecessity>
```

`JSON` format `{`

```json
 "ConcernNecessity":[
  "asap",
  "later",
  "nntf"
```

`],`

```json
 "RequestId":"9139DAF6-5CE0-49A0-926E-07243A290F70"
```

`}`

**Error codes**

For a list of error codes, see Error codes.

#### 6.5.4 DescribeGroupedVul

Queries information about vulnerabilities by group.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeGroupe dVul | The operation that you want to perform. Set the value to DescribeGroupedVul. |
| Lang | String | No | zh | The natural language of the request and response. Valid values: zh: Chinese en: English |

| Type | String | No | cve | The type of the vulnerability. Valid values: cve: Linux vulnerabilities sys: Windows vulnerabilities cms: Web CMS vulnerabilities app: application vulnerabilities emg: emergency vulnerabilities |
|---|---|---|---|---|
| Uuids | String | No | d42f938c-d962- 48a0-90f9- 05e4ea****** | The IDs of the asset instances. Separate multiple IDs with commas (,). |
| AliasName | String | No | RHSA- 2019:0230- Important: polkit security update | The alias of the vulnerability. |
| Necessity | String | No | asap,later,nntf | The priority to fix the vulnerability. Separate multiple priorities with commas (,). Valid values: asap: high later: medium nntf: low |
| Dealed | String | No | n | Specifies whether the vulnerability is handled. y: handled n: unhandled |
| CurrentPage | Integer | No | 1 | The page number of the current page. Pages start from page 1. Default value: 1. |
| PageSize | Integer | No | 20 | The number of entries to return on each page. Default value: 20. |
| GroupId | String | No | weds**** | The ID of the asset group. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0DFCADBA-7065- 42DA-AF17- 6868B9C2A8CF | The ID of the request. |
| PageSize | Integer | 20 | The number of entries returned per page. |

| CurrentPage | Integer | 1 | The page number of the current page. |
|---|---|---|---|
| TotalCount | Integer | 2 | The total number of entries returned. |
| GroupedVulIte ms | Array |   | Details about vulnerabilities by group. |
| Name | String | ***glibc security and bug fixes | The name of the vulnerability. |
| AliasName | String | RHSA-2019:0230- Important: polkit security update | The alias of the vulnerability. |
| Type | String | cve | The type of the vulnerability. Valid values: cve: Linux vulnerabilities sys: Windows vulnerabilities cms: Web CMS vulnerabilities app: application vulnerabilities emg: emergency vulnerabilities |
| GmtLast | Long | 1554185744000 | The time when the vulnerability was last detected. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since the epoch time January 1, 1970, 00:00:00 UTC. |
| AsapCount | Integer | 0 | The number of high-priority vulnerabilities. |
| LaterCount | Integer | 0 | The number of medium-priority vulnerabilities. |
| NntfCount | Integer | 59 | The number of low-priority vulnerabilities. |
| HandledCount | Integer | 0 | The total number of handled vulnerabilities. |
| Tags | String | Force restart | The tag of the vulnerability. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeGroupedVul &Lang=zh &Type=cve &AliasName=RHSA-2019:0230-Important: polkit security update &Necessity=asap,later,nntf &Dealed=n &CurrentPage=1 &PageSize=20 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeGroupedVul>
  <GroupedVulItems>
        <Tags></Tags>
        <LaterCount>0</LaterCount>
        <AliasName>RHSA-2019:0230-Important: polkit security update</AliasName>
        <AsapCount>0</AsapCount>
        <Type>cve</Type>
        <NntfCount>59</NntfCount>
        <GmtLast>1554185744000</GmtLast>
        <HandledCount>0</HandledCount>
  </GroupedVulItems>
  <GroupedVulItems>
        <Tags></Tags>
        <LaterCount>0</LaterCount>
        <AliasName>RHSA-2019:0368-Important: systemd security update</AliasName>
        <AsapCount>0</AsapCount>
        <Type>cve</Type>
        <NntfCount>59</NntfCount>
        <GmtLast>1554185744000</GmtLast>
        <HandledCount>0</HandledCount>
  </GroupedVulItems>
  <TotalCount>432</TotalCount>
  <PageSize>2</PageSize>
  <RequestId>0DFCADBA-7065-42DA-AF17-6868B9C2A8CF</RequestId>
  <CurrentPage>1</CurrentPage>
</DescribeGroupedVul>
```

`JSON` format `{`

```json
    "GroupedVulItems": [
```

`{`

```json
            "Tags": "",
            "LaterCount": 0,
            "AliasName": "RHSA-2019:0230-Important: polkit security update",
            "AsapCount": 0,
            "Type": "cve",
            "NntfCount": 59,
            "GmtLast": 1554185744000,
            "HandledCount": 0
```

`},` `{`

```json
            "Tags": "",
            "LaterCount": 0,
            "AliasName": "RHSA-2019:0368-Important: systemd security update",
            "AsapCount": 0,
            "Type": "cve",
            "NntfCount": 59,
            "GmtLast": 1554185744000,
            "HandledCount": 0
```

`}` `],`

```json
    "TotalCount": 432,
    "PageSize": 2,
    "RequestId": "0DFCADBA-7065-42DA-AF17-6868B9C2A8CF",
    "CurrentPage": 1
```

`}`

**Error codes**

For a list of error codes, see Error codes.

#### 6.5.5 DescribeAutoDelConfig

Queries the configurations for automatic vulnerability deletion.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeAutoDel Config | The operation that you want to perform. Set the value to DescribeAutoDelConfig. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|

| RequestId | String | 43186B14-5A39- 44E0-860E- 8B24D1EF82CC | The ID of the request. |
|---|---|---|---|
| Days | Integer | 7 | The number of days that a detected vulnerability is retained. |

**Examples**

Sample requests

```
/?Action=DescribeAutoDelConfig &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeAutoDelConfig>
  <RequestId>43186B14-5A39-44E0-860E-8B24D1EF82CC</RequestId>
  <Days>7</Days>
</DescribeAutoDelConfig>
```

`JSON` format `{`

```json
    "RequestId": "43186B14-5A39-44E0-860E-8B24D1EF82CC",
    "Days": 7
```

`}`

**Error codes**

For a list of error codes, see Error codes.

### 6.6 Baseline check

#### 6.6.1 DescribeCheckWarningSummary

Queries the statistical information about baseline check results. The information includes the number of servers on which a baseline check is performed, the number of baseline check items, and the last check pass rate.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeCheckW arningSummary | The operation that you want to perform. Set the value to DescribeCheckWarningSummary. |

| CurrentPage | Integer | No | 1 | The page number of the current page. |
|---|---|---|---|---|
| Lang | String | No | zh | The natural language of the request and response. Valid values: zh: Chinese en: English |
| PageSize | Integer | No | 10 | The number of entries to return on each page. |
| RiskName | String | No | Redis security baseline check | The name of the risk item. |
| RiskStatus | Integer | No | 1 | The status of the baseline check. Valid values: 1: failed 3: passed |
| SourceIp | String | No | 1.2.3.4 | The source IP address of the request. |
| Status | String | No | 1 | The status of the check item. Valid values: 1: failed 2: verifying 3: passed 5: expired 6: ignored |
| StrategyId | Long | No | 1 | The ID of the baseline check policy. |
| TypeName | String | No | database | The level-1 type of check items. |
| Uuids | String | No | f03259d8-1e81- 4fae-bcbb- 275fb5****** | The ID of the server. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Count | Integer | 10 | The number of check items returned on the current page. |
| CurrentPage | Integer | 1 | The page number of the current page. |

| PageSize | Integer | 10 | The number of entries returned per page. |
|---|---|---|---|
| RequestId | String | 00BD7CE2-284A- 4534-BD09- FB69836DD750 | The ID of the request. |
| TotalCount | Integer | 100 | The total number of baseline check items. |
| WarningSumm arys | Array |   | The statistics of check items. |
| CheckCount | Integer | 10 | The number of check items. |
| HighWarningC ount | Integer | 1 | The number of high-risk items. |
| LastFoundTim e | String | 2019-01-01 12:23:00 | The time when the last baseline check was performed. |
| Level | String | high | The severity level of the risk item. Valid values: High Medium Low |
| LowWarningCo unt | Integer | 3 | The number of low-risk check items. |
| MediumWarni ngCount | Integer | 2 | The number of medium-risk check items. |
| RiskId | Long | 1 | The ID of the risk item. |
| RiskName | String | Redis password | The name of the risk item. |
| SubTypeAlias | String | Redis | The level-2 type of the risk item. |
| TypeAlias | String | Database | The type of the check item. Valid values: database, system, weak password, and middleware. |
| WarningMachi neCount | Integer | 11 | The number of assets on which risk items are detected. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeCheckWarningSummary &Lang=zh &TypeName=database &Status=1 &RiskStatus=1 &RiskName=Redis security baseline check &StrategyId=1 &Uuids=f03259d8-1e81-4fae-bcbb-275fb55efb34 &CurrentPage=1 &PageSize=20 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeCheckWarningSummary>
   <TotalCount>25</TotalCount>
   <PageSize>20</PageSize>
   <RequestId>DFA6CDC5-E826-4D18-A499-BEF9DA31F1AD</RequestId>
   <CurrentPage>1</CurrentPage>
   <Count>20</Count>
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
      <SubTypeAlias>CentOS Linux 7 security standard compliance - MLPS level-
3</SubTypeAlias>
      <LowWarningCount>0</LowWarningCount>
      <RiskName>CentOS Linux 7 security standard compliance - MLPS level-3</RiskName>
```

```xml
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
      <SubTypeAlias>CentOS Linux 7 security standard compliance - MLPS level-
2</SubTypeAlias>
      <LowWarningCount>0</LowWarningCount>
      <RiskName>CentOS Linux 7 security standard compliance - MLPS level-2</RiskName>
   </WarningSummarys>
   <WarningSummarys>
      <RiskId>3</RiskId>
      <LastFoundTime>2019-04-10 08:31:32</LastFoundTime>
      <MediumWarningCount>0</MediumWarningCount>
      <WarningMachineCount>1</WarningMachineCount>
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
```

```xml
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
```

`<L` `tF`

```
dTi >20190410083132</L
```

`tF`

```
dTi
```

`>`

```xml
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
```

```xml
      <WarningMachineCount>0</WarningMachineCount>
      <CheckCount>12</CheckCount>
      <HighWarningCount>0</HighWarningCount>
      <Level>medium</Level>
      <TypeAlias>System</TypeAlias>
      <SubTypeAlias>CentOS Linux 6 security standard compliance - MLPS level-
2</SubTypeAlias>
      <LowWarningCount>0</LowWarningCount>
      <RiskName>CentOS Linux 6 security standard compliance - MLPS level-2</RiskName>
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
      <SubTypeAlias>CentOS Linux 6 security standard compliance - MLPS level-
3</SubTypeAlias>
      <LowWarningCount>0</LowWarningCount>
      <RiskName>CentOS Linux 6 security standard compliance - MLPS level-3</RiskName>
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
      <SubTypeAlias>Linux Ubuntu security standard compliance - MLPS level-
2</SubTypeAlias>
      <LowWarningCount>0</LowWarningCount>
      <RiskName>Linux Ubuntu security standard compliance - MLPS level-2</RiskName>
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
      <SubTypeAlias>Linux Ubuntu security standard compliance - MLPS level-
3</SubTypeAlias>
      <LowWarningCount>0</LowWarningCount>
      <RiskName>Linux Ubuntu security standard compliance - MLPS level-3</RiskName>
   </WarningSummarys>
   <WarningSummarys>
      <RiskId>54</RiskId>
      <LastFoundTime>2019-02-19 12:57:23</LastFoundTime>
```

`/`

```xml
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
 "Count":20,
 "TotalCount":25,
 "WarningSummarys":[
```

`{`

```json
   "SubTypeAlias":"CentOS Linux 7 security baseline check\n
\n ",
   "HighWarningCount":8,
   "WarningMachineCount":3,
   "RiskName":"CentOS Linux 7 security baseline check\n
\n ",
   "LowWarningCount":0,
   "CheckCount":16,
   "RiskId":43,
   "Level":"high",
   "MediumWarningCount":0,
   "TypeAlias":"System",
   "LastFoundTime":"2019-04-10 00:33:00"
```

`},` `{`

```json
   "SubTypeAlias":"CentOS Linux 7 security standard compliance - MLPS level-3",
   "HighWarningCount":7,
   "WarningMachineCount":2,
   "RiskName":"CentOS Linux 7 security standard compliance - MLPS level-3",
   "LowWarningCount":0,
   "CheckCount":15,
"RiskId":47
```

```json
   "RiskId":47,
   "Level":"medium",
   "MediumWarningCount":0,
   "TypeAlias":"System",
   "LastFoundTime":"2019-04-10 00:58:11"
```

`},` `{`

```json
   "SubTypeAlias":"CentOS Linux 7 security standard compliance - MLPS level-2",
   "HighWarningCount":6,
   "WarningMachineCount":2,
   "RiskName":"CentOS Linux 7 security standard compliance - MLPS level-2",
   "LowWarningCount":0,
   "CheckCount":12,
   "RiskId":48,
   "Level":"medium",
   "MediumWarningCount":0,
   "TypeAlias":"System",
   "LastFoundTime":"2019-04-10 00:58:11"
```

`},` `{`

```json
   "SubTypeAlias":"Redis security baseline check",
   "HighWarningCount":1,
   "WarningMachineCount":1,
   "RiskName":"Redis security baseline check",
   "LowWarningCount":0,
   "CheckCount":1,
   "RiskId":3,
   "Level":"high",
   "MediumWarningCount":0,
   "TypeAlias":"Database",
   "LastFoundTime":"2019-04-10 08:31:32"
```

`},` `{`

```json
   "SubTypeAlias":"Linux weak password",
   "HighWarningCount":1,
   "WarningMachineCount":1,
   "RiskName":"Linux weak password",
   "LowWarningCount":0,
   "CheckCount":1,
   "RiskId":19,
   "Level":"high",
   "MediumWarningCount":0,
   "TypeAlias":"Weak password",
   "LastFoundTime":"2019-04-10 08:31:32"
```

`},` `{`

```json
   "SubTypeAlias":"Anonymous FTP logon",
   "HighWarningCount":1,
   "WarningMachineCount":1,
   "RiskName":"Anonymous FTP logon",
   "LowWarningCount":0,
   "CheckCount":1,
   "RiskId":12,
   "Level":"high",
"MediumWarningCount":0,
```

```json
   MediumWarningCount:0,
   "TypeAlias":"Weak password",
   "LastFoundTime":"2019-04-10 08:31:32"
```

`},` `{`

```json
   "SubTypeAlias":"Windows weak password",
   "HighWarningCount":1,
   "WarningMachineCount":1,
   "RiskName":"Windows weak password",
   "LowWarningCount":0,
   "CheckCount":1,
   "RiskId":13,
   "Level":"high",
   "MediumWarningCount":0,
   "TypeAlias":"Weak password",
   "LastFoundTime":"2019-04-10 06:58:58"
```

`},` `{`

```json
   "SubTypeAlias":"Apache Tomcat security baseline check",
   "HighWarningCount":0,
   "WarningMachineCount":0,
   "RiskName":"Apache Tomcat security baseline check",
   "LowWarningCount":0,
   "CheckCount":8,
   "RiskId":23,
   "Level":"medium",
   "MediumWarningCount":0,
   "TypeAlias":"Middleware",
   "LastFoundTime":"2019-04-10 14:00:17"
```

`},` `{`

```json
   "SubTypeAlias":"PostgreSQL weak password",
   "HighWarningCount":0,
   "WarningMachineCount":0,
   "RiskName":"PostgreSQL weak password",
   "LowWarningCount":0,
   "CheckCount":1,
   "RiskId":2,
   "Level":"high",
   "MediumWarningCount":0,
   "TypeAlias":"Weak password",
   "LastFoundTime":"2019-04-10 08:31:32"
```

`},` `{`

```json
   "SubTypeAlias":"MySQL weak password",
   "HighWarningCount":0,
   "WarningMachineCount":0,
   "RiskName":"MySQL weak password",
   "LowWarningCount":0,
   "CheckCount":1,
   "RiskId":11,
   "Level":"high",
   "MediumWarningCount":0,
   "TypeAlias":"Weak password",
   "LastFoundTime":"2019-04-10 08:31:32"
```

`},` `{`

```json
   "SubTypeAlias":"FTP weak password",
   "HighWarningCount":0,
   "WarningMachineCount":0,
   "RiskName":"FTP weak password",
   "LowWarningCount":0,
   "CheckCount":1,
   "RiskId":20,
   "Level":"high",
   "MediumWarningCount":0,
   "TypeAlias":"Weak password",
   "LastFoundTime":"2019-04-10 08:31:32"
```

`},` `{`

```json
   "SubTypeAlias":"Microsoft SQL Server weak password",
   "HighWarningCount":0,
   "WarningMachineCount":0,
   "RiskName":"Microsoft SQL Server weak password",
   "LowWarningCount":0,
   "CheckCount":1,
   "RiskId":17,
   "Level":"high",
   "MediumWarningCount":0,
   "TypeAlias":"Weak password",
   "LastFoundTime":"2019-04-10 06:58:58"
```

`},` `{`

```json
   "SubTypeAlias":"Memcached security baseline check",
   "HighWarningCount":0,
   "WarningMachineCount":0,
   "RiskName":"Memcached security baseline check",
   "LowWarningCount":0,
   "CheckCount":2,
   "RiskId":24,
   "Level":"medium",
   "MediumWarningCount":0,
   "TypeAlias":"Database",
   "LastFoundTime":"2019-04-10 06:52:05"
```

`},` `{`

```json
   "SubTypeAlias":"CentOS Linux 6 security baseline check",
   "HighWarningCount":0,
   "WarningMachineCount":0,
   "RiskName":"CentOS Linux 6 security baseline check",
   "LowWarningCount":0,
   "CheckCount":16,
   "RiskId":42,
   "Level":"high",
   "MediumWarningCount":0,
   "TypeAlias":"System",
   "LastFoundTime":"2019-02-19 14:59:17"
```

`},` `{`

```json
   "SubTypeAlias":"CentOS Linux 6 security standard compliance - MLPS level-2",
   "HighWarningCount":0,
   "WarningMachineCount":0,
   "RiskName":"CentOS Linux 6 security standard compliance - MLPS level-2",
   "LowWarningCount":0,
   "CheckCount":12,
   "RiskId":49,
   "Level":"medium",
   "MediumWarningCount":0,
   "TypeAlias":"System",
   "LastFoundTime":"2019-02-19 14:59:17"
```

`},` `{`

```json
   "SubTypeAlias":"CentOS Linux 6 security standard compliance - MLPS level-3",
   "HighWarningCount":0,
   "WarningMachineCount":0,
   "RiskName":"CentOS Linux 6 security standard compliance - MLPS level-3",
   "LowWarningCount":0,
   "CheckCount":15,
   "RiskId":50,
   "Level":"medium",
   "MediumWarningCount":0,
   "TypeAlias":"System",
   "LastFoundTime":"2019-02-19 14:59:17"
```

`},` `{`

```json
   "SubTypeAlias":"Linux Ubuntu security standard compliance - MLPS level-2",
   "HighWarningCount":0,
   "WarningMachineCount":0,
   "RiskName":"Linux Ubuntu security standard compliance - MLPS level-2",
   "LowWarningCount":0,
   "CheckCount":14,
   "RiskId":55,
   "Level":"medium",
   "MediumWarningCount":0,
   "TypeAlias":"System",
   "LastFoundTime":"2019-02-19 12:57:23"
```

`},` `{`

```json
   "SubTypeAlias":"Linux Ubuntu security standard compliance - MLPS level-3",
   "HighWarningCount":0,
   "WarningMachineCount":0,
   "RiskName":"Linux Ubuntu security standard compliance - MLPS level-3",
   "LowWarningCount":0,
   "CheckCount":15,
   "RiskId":56,
   "Level":"medium",
   "MediumWarningCount":0,
   "TypeAlias":"System",
   "LastFoundTime":"2019-02-19 12:57:23"
```

`},` `{`

```json
   "SubTypeAlias":"Linux Ubuntu security baseline check",
   "HighWarningCount":0,
```

```json
   "WarningMachineCount":0,
   "RiskName":"Linux Ubuntu security baseline check",
   "LowWarningCount":0,
   "CheckCount":16,
   "RiskId":54,
   "Level":"high",
   "MediumWarningCount":0,
   "TypeAlias":"System",
   "LastFoundTime":"2019-02-19 12:57:23"
```

`},` `{`

```json
   "SubTypeAlias":"Windows 2012 R2 security baseline check",
   "HighWarningCount":0,
   "WarningMachineCount":0,
   "RiskName":"Windows 2012 R2 security baseline check",
   "LowWarningCount":0,
   "CheckCount":12,
   "RiskId":51,
   "Level":"high",
   "MediumWarningCount":0,
   "TypeAlias":"System",
   "LastFoundTime":"2019-02-19 12:44:58"
```

`}` `],`

```json
 "PageSize":20,
 "RequestId":"DFA6CDC5-E826-4D18-A499-BEF9DA31F1AD",
 "CurrentPage":1
```

`}`

**Error codes**

For a list of error codes, see Error codes.

#### 6.6.2 DescribeStratety

Queries the configurations of baseline check policies.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeStratety | The operation that you want to perform. Set the value to DescribeStratety. |
| Lang | String | No | zh | The natural language of the request and response. Valid values: zh: Chinese en: English |

| SourceIp | String | No | 1.2.3.4 | The source IP address of the request. |
|---|---|---|---|---|
| StrategyIds | String | No | test1,test2,test3 | The IDs of the baseline check policies. Separate multiple IDs with commas (,). |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 16B9826C-B99F- 4F8A-8048- EA81D6D3DE8B | The ID of the request. |
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
|---|---|---|---|
| Name | String | test | The name of the policy. |
| PassRate | Integer | 80 | The pass rate of the latest baseline check. |
| ProcessRate | Integer | 80 | The progress of the baseline check. |
| RiskCount | Integer | 5 | The number of selected check items. |
| Type | Integer | 1 | The type of the baseline check policy. Valid values: 1: default policy 2: custom policy |

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

Queries the details of the latest baseline check by using a baseline check policy. The details include the time when the check is performed, the number of risk items, and the baseline risk details.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeStrateg yExecDetail | The operation that you want to perform. Set the value to DescribeStrategyExecDetail. |
| StrategyId | Integer | Yes | 1 | The ID of the baseline check policy. Note To query the results of a baseline check that uses only one policy, you must specify the ID of the policy. You can call the DescribeStratety operation to obtain the ID. |
| SourceIp | String | No | 1.2.3.4 | The source IP address of the request. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| EndTime | String | 2019-01-08 20:11:20 | The time when the baseline check ends. |
| FailCount | Integer | 94 | The number of risk items that failed to pass the baseline check. |
| FailedEcsList | Array |   | The list of servers on which risk items were detected. |
| IP | String | 1.2.3.4 | The IP address of the instance on which the baseline check was performed. |
| InstanceName | String | Test-20180703 | The name of the instance. |
| IntranetIp | String | 1.2.3.5 | The internal IP address. |
| Reason | String | Detect timeout | The cause of the baseline check failure. |

| InProcessCoun t | Integer | 0 | The number of baseline check tasks that are running. |
|---|---|---|---|
| Percent | String | 100% | The progress of the baseline check. |
| RequestId | String | 09322632-4668- 4AD9-BD0D- 32757DEFBBA6 | The ID of the request. |
| Source | String | Manual | The type of the baseline check. Schedule Manual |
| StartTime | String | 2019-01-08 19:41:12 | The time when the baseline check starts. |
| SuccessCount | Integer | 81 | The number of check items that passed the baseline check. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeStrategyExecDetail &StrategyId=1 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeStrategyExecDetail>
   <RequestId>6489FA6A-D241-4380-9D8C-A8804484CA40</RequestId>
   <EndTime>2019-04-10 00:58:30</EndTime>
   <Percent>100%</Percent>
   <FailCount>1</FailCount>
   <StartTime>2019-04-10 00:19:01</StartTime>
   <SuccessCount>1</SuccessCount>
   <Source>Schedule</Source>
   <FailedEcsList>
      <InstanceName>health-check002</InstanceName>
      <IP>1.2.3.4</IP>
      <IntranetIp>1.2.3.5</IntranetIp>
      <Reason>Agent offline</Reason>
   </FailedEcsList>
   <InProcessCount>0</InProcessCount>
</DescribeStrategyExecDetail>
```

`JSON` format `{`

```json
 "Source":"Schedule",
 "InProcessCount":0,
 "SuccessCount":1,
 "RequestId":"6489FA6A-D241-4380-9D8C-A8804484CA40",
 "Percent":"100%",
 "FailedEcsList":[
```

`{`

```json
   "IntranetIp":"1.2.3.5",
   "IP":"1.2.3.4",
   "InstanceName":"health-check002",
   "Reason":"Agent offline"
```

`}` `],`

```json
 "EndTime":"2019-04-10 00:58:30",
 "StartTime":"2019-04-10 00:19:01",
 "FailCount":1
```

`}`

**Error codes**

For a list of error codes, see Error codes.

#### 6.6.4 DescribeCheckWarnings

Queries specified risk items and check items of a specified server.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeCheckW arnings | The operation that you want to perform. Set the value to DescribeCheckWarnings. |
| RiskId | Long | Yes | 1 | The ID of the risk item. Note To query specified risk items and check items of a specified server, you must specify the IDs of the risk items. You can call the DescribeCheckWarningSummary operation to obtain the IDs. |

| Uuid | String | Yes | d42f938c-d962- 48a0-90f9- 05********** | The ID of the server on which a baseline check is performed. The ID of the risk item. Note To query specified risk items and check items of a specified server, you must specify the ID of the server on which the baseline check is run. You can call the DescribeWarningMachines operation to obtain the IDs. |
|---|---|---|---|---|
| CurrentPage | Integer | No | 1 | The number of the current page. Pages start from page 1. The default value is 1, which indicates that the first page is displayed. |
| Lang | String | No | zh | The natural language of the request and response. Valid values: zh: Chinese en: English |
| PageSize | Integer | No | 20 | The number of entries to return on each page. The default value is 20, which indicates that 20 entries are returned on each page. |
| SourceIp | String | No | 1.2.3.4 | The source IP address of the request. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| CheckWarning s | Array |   | The information about the check item. |
| CheckId | Long | 1 | The ID of the check item. |
| CheckWarning Id | Long | 10 | The ID of the alert. |
| Item | String | Password expiration alert | The name of the check item. |

| Level | String | high | The severity level of the risk item. Valid values: high medium low |
|---|---|---|---|
| Status | Integer | 1 | The status of the check item. Valid values: 1: failed 2: verifying 3: passed 5: expired 6: ignored |
| Type | String | Identity authentication | The type of the check item. |
| Uuid | String | d42f938c-d962- 48a0-90f9- *********** | The ID of the server on which the baseline check was performed. |
| Count | Integer | 10 | The number of entries returned on the current page. |
| CurrentPage | Integer | 1 | The page number of the current page. |
| PageSize | Integer | 20 | The number of entries returned per page. |
| RequestId | String | 0DFCADBA-7065- 42DA-AF17- 6868B9C2A8CF | The ID of the request. |
| TotalCount | Integer | 100 | The total number of entries. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeCheckWarnings &RiskId=1 &Uuid=d42f938c-d962-48a0-90f9-05e4eaf92e34 &Lang=zh &SourceIp=127.0.0.1 &CurrentPage=1 &PageSize=20 &<Common request parameters>
```

Sample success responses `XML` format

|   | <DescribeCheckWarnings> <TotalCount>16</TotalCount> <CheckWarnings> <Status>6</Status> <Item>Check accounts without passwords in the system </Item> <Type>Identity authentication</Type> <Uuid>974af549-3248-44dd-9180-***</Uuid> <CheckId>1</CheckId> <CheckWarningId>1393768</CheckWarningId> <Level>high</Level> </CheckWarnings> <CheckWarnings> <Status>6</Status> <Item>Check password complexity</Item> <Type>Identity authentication</Type> <Uuid>974af549-3248-44dd-9180-***</Uuid> <CheckId>52</CheckId> <CheckWarningId>1393774</CheckWarningId> <Level>high</Level> </CheckWarnings> <CheckWarnings> <Status>6</Status> <Item>Make sure that root is the only account whose UID is 0</Item> <Type>Identity authentication</Type> <Uuid>974af549-3248-44dd-9180-***</Uuid> <CheckId>15</CheckId> <CheckWarningId>1393773</CheckWarningId> <Level>high</Level> </CheckWarnings> <CheckWarnings> <Status>6</Status> <Item>Enable address space layout randomization</Item> <Type>Intrusion prevention</Type> <Uuid>974af549-3248-44dd-9180-***</Uuid> <CheckId>14</CheckId> <CheckWarningId>1393772</CheckWarningId> <Level>high</Level> </CheckWarnings> <CheckWarnings> <Status>6</Status> <Item>Specify user permissions on file configurations</Item> <Type>File permissions</Type> <Uuid>974af549-3248-44dd-9180-***</Uuid> <CheckId>13</CheckId> <CheckWarningId>1393767</CheckWarningId> <Level>high</Level> </CheckWarnings> <CheckWarnings> <Status>6</Status> <Item>Specify permissions on the access control configuration file</Item> <Type>File permissions</Type> <Uuid>974af549-3248-44dd-9180-***</Uuid> |
|---|---|

```xml
        <CheckId>12</CheckId>
        <CheckWarningId>1393771</CheckWarningId>
        <Level>high</Level>
  </CheckWarnings>
  <CheckWarnings>
        <Status>6</Status>
        <Item>Make sure that SSH LogLevel is set to INFO</Item>
        <Type>Service configuration</Type>
        <Uuid>974af549-3248-44dd-9180-***</Uuid>
        <CheckId>11</CheckId>
        <CheckWarningId>1393766</CheckWarningId>
        <Level>high</Level>
  </CheckWarnings>
  <CheckWarnings>
        <Status>6</Status>
        <Item>Make sure that the rsyslog service is enabled</Item>
        <Type>Security auditing</Type>
        <Uuid>974af549-3248-44dd-9180-***</Uuid>
        <CheckId>10</CheckId>
        <CheckWarningId>1393770</CheckWarningId>
        <Level>high</Level>
  </CheckWarnings>
  <CheckWarnings>
        <Status>6</Status>
        <Item>Specify the timeout period for SSH idle connections</Item>
        <Type>Service configuration</Type>
        <Uuid>974af549-3248-44dd-9180-***</Uuid>
        <CheckId>8</CheckId>
        <CheckWarningId>1393765</CheckWarningId>
        <Level>high</Level>
  </CheckWarnings>
  <CheckWarnings>
        <Status>6</Status>
        <Item>Make sure that SSH V2 is used</Item>
        <Type>Service configuration</Type>
        <Uuid>974af549-3248-44dd-9180-***</Uuid>
        <CheckId>7</CheckId>
        <CheckWarningId>1393764</CheckWarningId>
        <Level>high</Level>
  </CheckWarnings>
  <CheckWarnings>
        <Status>6</Status>
        <Item>Make sure that SSH MaxAuthTries is set to a value from 3 to 6</Item>
        <Type>Service configuration</Type>
        <Uuid>974af549-3248-44dd-9180-***</Uuid>
        <CheckId>6</CheckId>
        <CheckWarningId>1393763</CheckWarningId>
        <Level>high</Level>
  </CheckWarnings>
  <CheckWarnings>
        <Status>6</Status>
        <Item>Make sure that alerts are triggered at least seven days before passwords
expire</Item>
        <Type>Identity authentication</Type>
```

```xml
        <Uuid>974af549-3248-44dd-9180-***</Uuid>
        <CheckId>5</CheckId>
        <CheckWarningId>1393769</CheckWarningId>
        <Level>high</Level>
  </CheckWarnings>
  <CheckWarnings>
        <Status>6</Status>
        <Item>Set the shortest interval between password changes</Item>
        <Type>Identity authentication</Type>
        <Uuid>974af549-3248-44dd-9180-***</Uuid>
        <CheckId>4</CheckId>
        <CheckWarningId>1393761</CheckWarningId>
        <Level>high</Level>
  </CheckWarnings>
  <CheckWarnings>
        <Status>6</Status>
        <Item>Set the password validity period</Item>
        <Type>Identity authentication</Type>
        <Uuid>974af549-3248-44dd-9180-***</Uuid>
        <CheckId>3</CheckId>
        <CheckWarningId>1393760</CheckWarningId>
        <Level>high</Level>
  </CheckWarnings>
  <CheckWarnings>
        <Status>6</Status>
        <Item>Disable SSH logon for accounts without specified passwords
                            </Item>
        <Type>Service configuration</Type>
        <Uuid>974af549-3248-44dd-9180-***</Uuid>
        <CheckId>2</CheckId>
        <CheckWarningId>1393762</CheckWarningId>
        <Level>high</Level>
  </CheckWarnings>
  <CheckWarnings>
        <Status>6</Status>
        <Item>Check whether password reuse is limited</Item>
        <Type>Identity authentication</Type>
        <Uuid>974af549-3248-44dd-9180-***</Uuid>
        <CheckId>58</CheckId>
        <CheckWarningId>1393775</CheckWarningId>
        <Level>high</Level>
  </CheckWarnings>
  <PageSize>20</PageSize>
  <RequestId>C1E6C4FE-DE00-4B75-A01E-FCAB55A36449</RequestId>
  <CurrentPage>1</CurrentPage>
  <Count>16</Count>
</DescribeCheckWarnings>
```

`JSON` format `{`

|   | { "Count":16, "TotalCount":16, "PageSize":20, "RequestId":"C1E6C4FE-DE00-4B75-A01E-FCAB55A36449", "CurrentPage":1, "CheckWarnings":[ { "Uuid":"974af549-3248-44dd-9180-***", "Status":6, "CheckWarningId":1393768, "Item":"Check accounts without passwords in the system\r\n \r\n ", "Type":"Identity authentication", "Level":"high", "CheckId":1 }, { "Uuid":"974af549-3248-44dd-9180-***", "Status":6, "CheckWarningId":1393774, "Item":"Check password complexity", "Type":"Identity authentication", "Level":"high", "CheckId":52 }, { "Uuid":"974af549-3248-44dd-9180-***", "Status":6, "CheckWarningId":1393773, "Item":"Make sure that root is the only account whose UID is 0", "Type":"Identity authentication", "Level":"high", "CheckId":15 }, { "Uuid":"974af549-3248-44dd-9180-***", "Status":6, "CheckWarningId":1393772, "Item":"Enable address space layout randomization", "Type":"Intrusion prevention", "Level":"high", "CheckId":14 }, { "Uuid":"974af549-3248-44dd-9180-***", "Status":6, "CheckWarningId":1393767, "Item":"Specify user permissions on file configurations", "Type":"File permissions", "Level":"high", "CheckId":13 }, { "Uuid":"974af549-3248-44dd-9180-***", |   |
|---|---|---|

```json
   "Status":6,
   "CheckWarningId":1393771,
   "Item":"Specify the permissions on the access control configuration file",
   "Type":"File permissions",
   "Level":"high",
   "CheckId":12
```

`},` `{`

```json
   "Uuid":"974af549-3248-44dd-9180-***",
   "Status":6,
   "CheckWarningId":1393766,
   "Item":"Make sure that SSH LogLevel is set to INFO",
   "Type":"Service configuration",
   "Level":"high",
   "CheckId":11
```

`},` `{`

```json
   "Uuid":"974af549-3248-44dd-9180-***",
   "Status":6,
   "CheckWarningId":1393770,
   "Item":"Make sure that the rsyslog service is enabled",
   "Type":"Security auditing",
   "Level":"high",
   "CheckId":10
```

`},` `{`

```json
   "Uuid":"974af549-3248-44dd-9180-***",
   "Status":6,
   "CheckWarningId":1393765,
   "Item":"Specify the timeout period for SSH idle connections",
   "Type":"Service configuration",
   "Level":"high",
   "CheckId":8
```

`},` `{`

```json
   "Uuid":"974af549-3248-44dd-9180-***",
   "Status":6,
   "CheckWarningId":1393764,
   "Item":"Make sure that SSH V2 is used",
   "Type":"Service configuration",
   "Level":"high",
   "CheckId":7
```

`},` `{`

```json
   "Uuid":"974af549-3248-44dd-9180-***",
   "Status":6,
   "CheckWarningId":1393763,
   "Item":"Make sure that SSH MaxAuthTries is set to a value from 3 to 6",
   "Type":"Service configuration",
   "Level":"high",
   "CheckId":6
```

`},` `{`

```json
   "Uuid":"974af549-3248-44dd-9180-***",
```

```json
   "Status":6,
   "CheckWarningId":1393769,
   "Item":"Make sure that alerts are triggered at least seven days before passwords exp
ire",
   "Type":"Identity authentication",
   "Level":"high",
   "CheckId":5
```

`},` `{`

```json
   "Uuid":"974af549-3248-44dd-9180-***",
   "Status":6,
   "CheckWarningId":1393761,
   "Item":"Set the shortest interval between password changes",
   "Type":"Identity authentication",
   "Level":"high",
   "CheckId":4
```

`},` `{`

```json
   "Uuid":"974af549-3248-44dd-9180-***",
   "Status":6,
   "CheckWarningId":1393760,
   "Item":"Set the password validity period",
   "Type":"Identity authentication",
   "Level":"high",
   "CheckId":3
```

`},` `{`

```json
   "Uuid":"974af549-3248-44dd-9180-***",
   "Status":6,
   "CheckWarningId":1393762,
   "Item":"Disable SSH logon for accounts without specified passwords
\r\n \r\n \r\n
```

`",`

```json
   "Type":"Service configuration",
   "Level":"high",
   "CheckId":2
```

`},` `{`

```json
   "Uuid":"974af549-3248-44dd-9180-***",
   "Status":6,
   "CheckWarningId":1393775,
   "Item":"Check whether password reuse is limited",
   "Type":"Identity authentication",
   "Level":"high",
   "CheckId":58
```

`}` `]` `}`

**Error codes**

For a list of error codes, see Error codes.

#### 6.6.5 DescribeCheckWarningDetail

Queries the details of a specific check item.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeCheckW arningDetail | The operation that you want to perform. Set the value to DescribeCheckWarningDetail. |
| CheckWarningI d | Long | Yes | 1 | The ID of the alert triggered by the check item. Note To query the details of a specific check item, you must specify the ID of the alert triggered by the check item. You can call the DescribeCheckWarnings operation to obtain the alert ID. |
| Lang | String | No | zh | The natural language of the request and response. Valid values: zh: Chinese en: English |
| SourceIp | String | No | 1.2.3.4 | The source IP address of the request. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Advice | String | Fix now | The suggestion for the management of the risk item. |
| CheckId | Long | 1 | The ID of the check item. |
| Description | String | Password expiring | The additional details about the risk item. |
| Item | String | Password expiration alert | The name of the check item. |

| Level | String | high | The severity level of the risk item. high: The item is a high-risk one and highlighted in red. medium: The item is a medium-risk one and highlighted in orange. low: The item is a low-risk one and highlighted in gray. |
|---|---|---|---|
| Prompt | String | Password expiration alert | The prompt for the risk item. |
| RequestId | String | 09969D2C-4FAD- 429E-BFBF- 9A60DEF8BF6F | The ID of the request. |
| Type | String | Identity authentication | The type of the check item. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeCheckWarningDetail &CheckWarningId=1 &SourceIp=127.0.0.1 &Lang=zh &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeCheckWarningDetail>
   <Item>Specify user permissions on file configurations</Item>
   <Type>File permissions</Type>
   <Description>Specify user permissions on file configurations</Description>
   <RequestId>9F2361B3-B7C3-4189-8DB5-C6D1F67BC225</RequestId>
   <CheckId>13</CheckId>
   <Prompt></Prompt>
   <Level>high</Level>
   <Advice>Run the following five commands
  chown root:root /etc/passwd /etc/shadow /etc/group /etc/gshadow
  chmod 0644 /etc/group
  chmod 0644 /etc/passwd
  chmod 0400 /etc/shadow
 chmod 0400 /etc/gshadow  </Advice>
</DescribeCheckWarningDetail>
```

`JSON` format `{`

```json
 "Prompt":"",
 "Description":"Specify user permissions on file configurations",
 "Item":"Specify user permissions on file configurations",
 "Type":"File permissions",
 "RequestId":"9F2361B3-B7C3-4189-8DB5-C6D1F67BC225",
 "Advice":"Run the following five commands\r\nchown root:root /etc/passwd /etc/shadow /
etc/group /etc/gshadow\r\nchmod 0644 /etc/group \r\nchmod 0644 /etc/passwd \r\nchmod 0400 /etc/shadow \r\nchmod 0400 /etc/gshadow ",
 "Level":"high",
 "CheckId":13
```

`}`

**Error codes**

For a list of error codes, see Error codes.

#### 6.6.6 DescribeWarningMachines

Queries information about servers on which a baseline check is performed. The information includes the statistics and status of risk items and IDs of the servers.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeWarnin gMachines | The operation that you want to perform. Set the value to DescribeWarningMachines. |
| RiskId | Long | Yes | 1 | The ID of the risk item. Note To query information about servers on which a baseline check is performed, you must specify the ID of the risk item that is related to the baseline check. You can call the DescribeCheckWarningSummary operation to obtain the ID. |
| SourceIp | String | No | 1.2.3.4 | The source IP address of the request. |
| Lang | String | No | zh | The natural language of the request and response. Valid values: zh: Chinese en: English |

| MachineName | String | No | test ecs172 _ | The name of the server on which a baseline check is performed. |
|---|---|---|---|---|
| Uuids | String | No | xxx-aaa-bbb-ccc | The ID of the server on which a baseline check is performed. Separate multiple IDs with commas (,). |
| StrategyId | Long | No | 1 | The ID of the baseline check policy. |
| PageSize | Integer | No | 10 | The number of entries to return on each page. |
| CurrentPage | Integer | No | 1 | The number of the current page. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Count | Integer | 10 | The number of entries returned on the current page. |
| CurrentPage | Integer | 1 | The number of the current page. |
| PageSize | Integer | 10 | The number of entries returned per page. |
| RequestId | String | 00BDE2-284A- 4534-BD09- FB69836DD750 | The ID of the request. |
| TotalCount | Integer | 100 | The total number of returned entries. |
| WarningMachi nes | Array |   | The information about the servers that generate alerts. |
| HighWarningC ount | Integer | 10 | The number of high-risk check items. |
| InstanceId | String | i- m5ee8b9nr3h30m hb**** | The instance ID of the server. |
| InstanceName | String | aaawebtest | The name of the instance. |
| InternetIp | String | 1.2.3.4 | The public IP address of the server. |

| IntranetIp | String | 1.2.3.5 | The private IP address of the server. |
|---|---|---|---|
| LowWarningCo unt | Integer | 3 | The number of low-risk check items. |
| MediumWarni ngCount | Integer | 2 | The number of medium-risk check items. |
| PassCount | Integer | 10 | The number of items that have passed the baseline check. |
| RegionId | String | cn-qingdao | The region ID of the server. |
| Status | Integer | 1 | The verification status of the risk items that are fixed. Valid values: 1: completed 2: verifying |
| Uuid | String | xxx-aaa-bbb-ccc | The ID of the server on which a baseline check is performed. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeWarningMachines &RiskId=1 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeWarningMachinesResponse>
      <TotalCount>100</TotalCount>
      <RequestId>00BDE2-284A-4534-BD09-FB69836DD750</RequestId>
      <PageSize>10</PageSize>
      <CurrentPage>1</CurrentPage>
      <WarningMachines>
            <InstanceName>aaawebtest</InstanceName>
            <Status>1</Status>
            <MediumWarningCount>2</MediumWarningCount>
            <Uuid>xxx-aaa-bbb-ccc</Uuid>
            <InternetIp>1.2.3.4</InternetIp>
            <InstanceId>i-m5ee8b9nr3h30mhb****</InstanceId>
            <HighWarningCount>10</HighWarningCount>
            <RegionId>cn-qingdao</RegionId>
            <PassCount>10</PassCount>
            <IntranetIp>1.2.3.5</IntranetIp>
            <LowWarningCount>3</LowWarningCount>
      </WarningMachines>
      <Count>10</Count>
</DescribeWarningMachinesResponse>
```

`JSON` format `{`

```json
    "TotalCount": "100",
    "RequestId": "00BDE2-284A-4534-BD09-FB69836DD750",
    "PageSize": "10",
    "CurrentPage": "1",
    "WarningMachines": [{
        "InstanceName": "aaawebtest",
        "Status": "1",
        "MediumWarningCount": "2",
        "Uuid": "xxx-aaa-bbb-ccc",
        "InternetIp": "1.2.3.4",
        "InstanceId": "i-m5ee8b9nr3h30mhb****",
        "HighWarningCount": "10",
        "RegionId": "cn-qingdao",
        "PassCount": "10",
        "IntranetIp": "1.2.3.5",
        "LowWarningCount": "3"
    }],
    "Count": "10"
```

`}`

**Error codes**

For a list of error codes, see Error codes.

### 6.7 Asset fingerprints

#### 6.7.1 DescribePropertyCount

Queries the statistics of asset fingerprints, including the numbers of processes, ports, software, users, and scheduled tasks.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribePropert yCount | The operation that you want to perform. Set the value to DescribePropertyCount. |
| Type | String | No | port | The type of the asset fingerprint. Valid values: user software process port cron: scheduled tasks Note If you do not specify a type, all types of asset fingerprints are queried. |
| UuidList | String | No | [c4678332- ef3**,c46***] | The IDs of the assets, which are unique. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Cron | Integer | 261 | The number of scheduled tasks. |
| Port | Integer | 163 | The number of listening ports. |
| Process | Integer | 367 | The number of running processes. |
| RequestId | String | 7E0618A9-D5EF- 4220-9471- C42B5E92719F | The ID of the request. |
| Software | Integer | 5073 | The number of software assets. |
| User | Integer | 114 | The number of users. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribePropertyCount &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribePropertyCount>
  <User>340</User>
  <Software>2598</Software>
  <Port>265</Port>
  <Process>395</Process>
  <RequestId>3D93ABAB-0AC2-4A27-A03B-35C0E4AA0443</RequestId>
  <Cron>261</Cron>
</DescribePropertyCount>
```

`JSON` format `{`

```json
 "User":340,
 "Software":2598,
 "Port":265,
 "RequestId":"3D93ABAB-0AC2-4A27-A03B-35C0E4AA0443",
 "Process":395,
 "Cron":261
```

`}`

**Error codes**

For a list of error codes, see Error codes.

#### 6.7.2 DescribePropertyPortDetail

Queries the details of a port.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribePropert yPortDetail | The operation that you want to perform. Set the value to DescribePropertyPortDetail. |
| Remark | String | No | 1.2.3.4 | The name or IP address of the server. |
| Port | String | No | 22 | The port of the server. |

| ProcName | String | No | sshd | The name of the process. |
|---|---|---|---|---|
| Uuid | String | No | 50d213b4-3a35- 427a-b8a5-*** | The ID of the asset, which is unique. |
| CurrentPage | Integer | No | 1 | The page number of the current page. |
| PageSize | Integer | No | 6 | The number of entries to return on each page. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | FAA793EF-5B14- 4CDD-B3E0- B14D4342C422 | The ID of the request. |
| Propertys | Array |   | Details of the port. |
| BindIp | String | 1.2.3.4 | The IP addresses bound to the port. |
| Port | String | 22 | The port number. |
| InstanceName | String | test-*** | The name of the asset related to the port. |
| Proto | String | tcp | The network protocol. |
| Ip | String | 1.2.3.1 | The public IP address of the asset. |
| Create | String | 2019-05- 13T10:39Z | The time when the data is last collected. |
| CreateTimesta mp | Long | 1557715141000 | The timestamp of last data collection. |
| ProcName | String | sshd | The name of the process that is using the port. |
| Uuid | String | 50d213b4-3a35- 427a-b8a5- 04b0c7e1f4d2" | The ID of the asset related to the port. |
| InstanceId | String | 50d213b4-3a35- 427a-b8a5- 04b0c7e1f4d2" | The ID of the asset related to the port. |

| IntranetIp | String | 1.2.3.2 | The private IP address of the asset. |
|---|---|---|---|
| InternetIp | String | 1.2.3.1 | The public IP address of the asset. |
| PageInfo | Struct |   | The page information. |
| Count | Integer | 5 | The number of entries returned on the current page. |
| PageSize | Integer | 5 | The number of entries returned per page. |
| TotalCount | Integer | 762 | The total number of returned entries. |
| CurrentPage | Integer | 1 | The page number of the current page. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribePropertyPortDetail &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribePropertyPortDetailResponse>
  <Propertys>
        <InstanceName>centos-xx</InstanceName>
        <Uuid>00274759-73ef-485a-ae40-c2b5972f50cd</Uuid>
        <Proto>tcp</Proto>
        <InternetIp>101.xx.xx.104</InternetIp>
        <InstanceId>i-2ze645t5u9jo4txxx</InstanceId>
        <Create>2020-01-09T13:53Z</Create>
        <Port>22</Port>
        <Ip>101.xx.xx.104</Ip>
        <ProcName>sshd</ProcName>
        <CreateTimestamp>1578549227000</CreateTimestamp>
        <IntranetIp>192.xx.xx.96</IntranetIp>
        <BindIp>0.0.0.0</BindIp>
  </Propertys>
  <Propertys>
        <InstanceName>paas-xxx-test1122</InstanceName>
        <Uuid>007ecd45-e90f-4290-9eac-758407aa1509</Uuid>
        <Proto>tcp</Proto>
        <InternetIp>118.xx.xx.7</InternetIp>
        <InstanceId>i-m5e56ycm6xx7if43xx</InstanceId>
        <Create>2020-02-18T15:52Z</Create>
        <Port>10251</Port>
```

```xml
        <Ip>118.xx.xx.7</Ip>
        <ProcName>kube-scheduler</ProcName>
        <CreateTimestamp>1582012349000</CreateTimestamp>
        <IntranetIp>192.xx.xx.192</IntranetIp>
        <BindIp>::</BindIp>
  </Propertys>
  <Propertys>
        <InstanceName>paas-xx-2</InstanceName>
        <Uuid>007ecd45-e9xx-4290-9eac-758407aa15xx</Uuid>
        <Proto>tcp</Proto>
        <InternetIp>118.xx.xx.7</InternetIp>
        <InstanceId>i-m5e56ycm6s0xxf43maxx</InstanceId>
        <Create>2020-02-18T15:52Z</Create>
        <Port>10252</Port>
        <Ip>118.xx.xx.7</Ip>
        <ProcName>kube-controller-manager</ProcName>
        <CreateTimestamp>1582012349000</CreateTimestamp>
        <IntranetIp>192.xx.xx.192</IntranetIp>
        <BindIp>::</BindIp>
  </Propertys>
  <Propertys>
        <InstanceName>paas-xx-2</InstanceName>
        <Uuid>007ecd45-e90f-42xx-9eac-758407aa15xx</Uuid>
        <Proto>tcp</Proto>
        <InternetIp>118.xx.xx.7</InternetIp>
        <InstanceId>i-m5e56ycmxx07if43maxx</InstanceId>
        <Create>2020-02-18T15:52Z</Create>
        <Port>2379</Port>
        <Ip>118.xx.xx.7</Ip>
        <ProcName>etcd</ProcName>
        <CreateTimestamp>1582012349000</CreateTimestamp>
        <IntranetIp>192.xx.xx.192</IntranetIp>
        <BindIp>::</BindIp>
  </Propertys>
  <Propertys>
        <InstanceName>paas-xx-2</InstanceName>
        <Uuid>007ecd45-e90f-4290-9exx-758407aa15xx</Uuid>
        <Proto>tcp</Proto>
        <InternetIp>118.xx.xx.7</InternetIp>
        <InstanceId>i-m5e56ycm6s07if43maxx</InstanceId>
        <Create>2020-02-18T15:52Z</Create>
        <Port>6443</Port>
        <Ip>118.xx.xx.7</Ip>
        <ProcName>kube-apiserver</ProcName>
        <CreateTimestamp>1582012349000</CreateTimestamp>
        <IntranetIp>192.xx.xx.192</IntranetIp>
        <BindIp>::</BindIp>
  </Propertys>
  <PageInfo>
        <Count>5</Count>
        <PageSize>5</PageSize>
        <TotalCount>762</TotalCount>
        <CurrentPage>1</CurrentPage>
  </PageInfo>
```

```xml
  <requestId>FAA793EF-5B14-4CDD-B3E0-B14D4342C422</requestId>
</DescribePropertyPortDetailResponse>
```

`JSON` format `{`

```json
  "Propertys": [
```

`{`

```json
       "InstanceName": "centos-xx",
              "Uuid": "00274759-73ef-485a-ae40-c2b5972f50cd",
             "Proto": "tcp",
             "InternetIp": "101.xx.xx.104",
             "InstanceId": "i-2ze645t5u9jo4txxx",
             "Create": "2020-01-09T13:53Z",
             "Port": "22",
             "Ip": "101.xx.xx.104",
             "ProcName": "sshd",
             "CreateTimestamp": 1578549227000,
             "IntranetIp": "192.xx.xx.96",
           "BindIp": "0.0.0.0"
```

`},` `{`

```json
       "InstanceName": "paas-xxx-test1122",
             "Uuid": "007ecd45-e90f-4290-9eac-758407aa1509",
             "Proto": "tcp",
              "InternetIp": "118.xx.xx.7",
             "InstanceId": "i-m5e56ycm6xx7if43xx",
             "Create": "2020-02-18T15:52Z",
             "Port": "10251",
             "Ip": "118.xx.xx.7",
             "ProcName": "kube-scheduler",
             "CreateTimestamp": 1582012349000,
             "IntranetIp": "192.xx.xx.192",
             "BindIp": "::"
```

`},` `{`

```json
       "InstanceName": "paas-xx-2",
             "Uuid": "007ecd45-e9xx-4290-9eac-758407aa15xx",
             "Proto": "tcp",
             "InternetIp": "118.xx.xx.7",
             "InstanceId": "i-m5e56ycm6s0xxf43maxx",
             "Create": "2020-02-18T15:52Z",
             "Port": "10252",
             "Ip": "118.xx.xx.7",
             "ProcName": "kube-controller-manager",
             "CreateTimestamp": 1582012349000,
             "IntranetIp": "192.xx.xx.192",
             "BindIp": "::"
```

`},` `{`

```json
            "InstanceName": "paas-xx-2",
            "Uuid": "007ecd45-e90f-42xx-9eac-758407aa15xx",
            "Proto": "tcp",
            "InternetIp": "118.xx.xx.7",
```

```json
            "InstanceId": "i-m5e56ycmxx07if43maxx",
            "Create": "2020-02-18T15:52Z",
            "Port": "2379",
            "Ip": "118.xx.xx.7",
            "ProcName": "etcd",
            "CreateTimestamp": 1582012349000,
            "IntranetIp": "192.xx.xx.192",
            "BindIp": "::"
```

`},` `{`

```json
            "InstanceName": "paas-xx-2",
            "Uuid": "007ecd45-e90f-4290-9exx-758407aa15xx",
            "Proto": "tcp",
            "InternetIp": "118.xx.xx.7",
            "InstanceId": "i-m5e56ycm6s07if43maxx",
            "Create": "2020-02-18T15:52Z",
            "Port": "6443",
            "Ip": "118.xx.xx.7",
            "ProcName": "kube-apiserver",
            "CreateTimestamp": 1582012349000,
            "IntranetIp": "192.xx.xx.192",
            "BindIp": "::"
```

`}` `],`

```json
"PageInfo": {
      "Count": 5,
      "PageSize": 5,
      "TotalCount": 762,
      "CurrentPage": 1
```

`},`

```json
  "requestId": "FAA793EF-5B14-4CDD-B3E0-B14D4342C422"
```

`}`

**Error codes**

For a list of error codes, see Error codes.

#### 6.7.3 DescribePropertyProcDetail

Queries the details of a process.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribePropert yProcDetail | The operation that you want to perform. Set the value to DescribePropertyProcDetail. |
| Cmdline | String | No | . /8888 | The parameter that is used to start the process. |

| CurrentPage | Integer | No | 1 | The page number of the current page. |
|---|---|---|---|---|
| Name | String | No | 8888 | The name of the process. |
| PageSize | Integer | No | 5 | The number of entries to return on each page. |
| Remark | String | No | 1.2.3.4 | The name or IP address of the server. |
| User | String | No | root | The user who runs the process. |
| Uuid | String | No | c4678332-ef35- 4ad4-*** | The ID of the asset related to the process. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| PageInfo |   |   | The page information. |
| Count | Integer | 1 | The number of entries returned on the current page. |
| CurrentPage | Integer | 1 | The page number of the current page. |
| PageSize | Integer | 5 | The number of entries returned per page. |
| TotalCount | Integer | 1 | The total number of returned entries. |
| Propertys | Array |   | The returned process information. |
| Cmdline | String | . /8888 | The parameter that was used to start the process. |
| Create | String | 2019-05- 15T11:08Z | The last time when the data was collected. |
| CreateTimesta mp | Long | 1565686951000 | The timestamp of last data collection. |
| EuidName | String | root | The permission to run the process. |

| InstanceId | String | c4678332-ef35- 4ad4-8358-*** | The ID of the asset. |
|---|---|---|---|
| InstanceName | String | test-*** | The name of the asset. |
| InternetIp | String | 1.2.3.1 | The public IP address of the asset. |
| IntranetIp | String | 1.2.3.2 | The private IP address of the asset. |
| Md5 | String | N/A | The MD5 value of the file. |
| Name | String | 8888 | The name of the process. |
| Path | String | /root/Oracle/Middle ware/***/8888 | The path of the process. |
| Pid | String | 12826 | The ID of the process. |
| Pname | String | start***.s | The parent name of the process. |
| StartTime | String | 2019-08-07 10:09:05 | The time when the process started. |
| User | String | root | The user who runs the process. |
| Uuid | String | c4678332-ef35- 4ad4-8358-6*** | The ID of the asset related to the process. |
| RequestId | String | 64388374-A309- 4191-8606- 3346CCA364B0 | The ID of the request. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribePropertyProcDetail &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribePropertyProcDetail>
   <RequestId>64388374-A309-4191-8606-3346CCA364B0</RequestId>
   <PageInfo>
      <Count>2</Count>
      <TotalCount>8184</TotalCount>
      <PageSize>2</PageSize>
      <CurrentPage>1</CurrentPage>
   </PageInfo>
   <Propertys>
      <User>N/A</User>
      <Uuid>90d4cc6a-806f-***</Uuid>
      <Md5>N/A</Md5>
      <CreateTimestamp>1557889713000</CreateTimestamp>
      <InstanceId>i-bp1***</InstanceId>
      <InternetIp></InternetIp>
      <Path>N/A</Path>
      <Name>N/A</Name>
      <IntranetIp>1.2.3.4</IntranetIp>
      <Create>2019-05-15T11:08Z</Create>
      <Pname>N/A</Pname>
      <EuidName>N/A</EuidName>
      <StartTime>N/A</StartTime>
      <Pid>0</Pid>
      <InstanceName>test_***</InstanceName>
      <Cmdline>N/A</Cmdline>
   </Propertys>
   <Propertys>
      <User>N/A</User>
      <Uuid>90d4cc6a-806f-4***</Uuid>
      <Md5>N/A</Md5>
      <CreateTimestamp>1557889713000</CreateTimestamp>
      <InstanceId>i-b***</InstanceId>
      <InternetIp></InternetIp>
      <Path>N/A</Path>
      <Name>N/A</Name>
      <IntranetIp>1.2.3.5</IntranetIp>
      <Create>2019-05-15T11:08Z</Create>
      <Pname>N/A</Pname>
      <EuidName>N/A</EuidName>
      <StartTime>N/A</StartTime>
      <Pid>4</Pid>
      <InstanceName>tsy_***</InstanceName>
      <Cmdline>N/A</Cmdline>
   </Propertys>
</DescribePropertyProcDetail>
```

`JSON` format `{`

```json
 "RequestId":"64388374-A309-4191-8606-3346CCA364B0",
 "PageInfo":{
  "Count":2,
  "TotalCount":8184,
  "PageSize":2,
  "CurrentPage":1
```

`},`

```json
 "Propertys":[
```

`{`

```json
   "User":"N/A",
   "Uuid":"90d4cc6a-806f-***",
   "Md5":"N/A",
   "CreateTimestamp":1557889713000,
   "InstanceId":"i-bp1***",
   "InternetIp":"",
   "Path":"N/A",
   "Name":"N/A",
   "IntranetIp":"1.2.3.4",
   "Create":"2019-05-15T11:08Z",
   "Pname":"N/A",
   "StartTime":"N/A",
   "EuidName":"N/A",
   "Pid":"0",
   "Cmdline":"N/A",
   "InstanceName":"test_***"
```

`},` `{`

```json
   "User":"N/A",
   "Uuid":"90d4cc6a-806f-4***",
   "Md5":"N/A",
   "CreateTimestamp":1557889713000,
   "InstanceId":"i-b***",
   "InternetIp":"",
   "Path":"N/A",
   "Name":"N/A",
   "IntranetIp":"1.2.3.5",
   "Create":"2019-05-15T11:08Z",
   "Pname":"N/A",
   "StartTime":"N/A",
   "EuidName":"N/A",
   "Pid":"4",
   "Cmdline":"N/A",
   "InstanceName":"tsy_***"
```

`}` `]` `}`

**Error codes**

For a list of error codes, see Error codes.

#### 6.7.4 DescribePropertyPortItem

Queries information about ports.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribePropert yPortItem | The operation that you want to perform. Set the value to DescribePropertyPortItem. |
| ForceFlush | Boolean | No | true | Specifies whether to force refresh the data that you want to query. |
| Port | String | No | 22 | The port number. |
| CurrentPage | Integer | No | 1 | The page number of the current page. |
| PageSize | Integer | No | 5 | The number of entries to return on each page. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 7E0618A9-D5EF- 4220-9471- C42B5E92719F | The ID of the request. |
| PropertyItems | Array |   | Details of the port. |
| Port | String | 22 | The number of the listener port. |
| Proto | String | tcp | The network protocol of the port. |
| Count | Integer | 495 | The number of servers that use the port. |
| PageInfo | Struct |   | The page information. |
| Count | Integer | 5 | The number of entries returned on the current page. |

| PageSize | Integer | 5 | The number of entries returned per page. |
|---|---|---|---|
| TotalCount | Integer | 163 | The total number of entries. |
| CurrentPage | Integer | 1 | The page number of the current page. |

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

**Error codes**

For a list of error codes, see Error codes.

#### 6.7.5 DescribePropertyProcItem

Queries information about all processes.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|

| Action | String | Yes | DescribePropert yProcItem | The operation that you want to perform. Set the value to DescribePropertyProcItem. |
|---|---|---|---|---|
| CurrentPage | Integer | No | 1 | The page number of the current page. |
| ForceFlush | Boolean | No | true | Specifies whether to force refresh the data that you want to query. |
| Name | String | No | test | The name of the process. |
| PageSize | Integer | No | 10 | The number of entries to return on each page. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| PageInfo |   |   | The page information. |
| Count | Integer | 5 | The number of entries returned on the current page. |
| CurrentPage | Integer | 1 | The page number of the current page. |
| PageSize | Integer | 5 | The number of entries returned per page. |
| TotalCount | Integer | 372 | The total number of entries. |
| PropertyItems | Array |   | The process information. |
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
 "RequestId":"BD8AD4C6-A169-4FA3-BA1F-ED40ED52973B",
 "PropertyItems":[
```

`{`

```json
   "Name":"(sd-**)",
   "Count":7
```

`},` `{`

```json
   "Name":"6Cm***",
   "Count":1
```

`}` `],`

```json
 "PageInfo":{
  "Count":2,
  "TotalCount":395,
  "PageSize":2,
  "CurrentPage":1
```

`}` `}`

**Error codes**

For a list of error codes, see Error codes.

#### 6.7.6 DescribePropertySoftwareDetail

Queries the details of a software asset.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribePropert ySoftwareDetail | The operation that you want to perform. Set the value to DescribePropertySoftwareDetail. |
| CurrentPage | Integer | No | 1 | The page number of the current page. |
| Name | String | No | tes*** | The name of the software. |
| PageSize | Integer | No | 5 | The number of entries to return on each page. |
| Path | String | No | /etc/test | The directory where the software is installed. |
| Remark | String | No | 1.2.3.4 | The name or IP address of the server. |
| SoftwareVersi on | String | No | 11 | The version of the software. |
| Uuid | String | No | 50d213b4-3a35- 427a-b8a5-*** | The ID of the software asset. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| PageInfo |   |   | The page information. |
| Count | Integer | 2 | The number of entries returned on the current page. |
| CurrentPage | Integer | 1 | The page number of the current page. |
| PageSize | Integer | 2 | The number of entries returned per page. |
| TotalCount | Integer | 23 | The total number of returned entries. |

| Propertys | Array |   | The details of the software. |
|---|---|---|---|
| Create | Long | 2019-06-24 | The last time when the data was collected. |
| CreateTimesta mp | Long | 1565539587000 | The last time when the data was collected. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since the epoch time January 1, 1970, 00:00:00 UTC. |
| InstallTime | String | 2017-09-07 10:54:49 | The time when the software was installed. |
| InstanceId | String | i-uf*** | The ID of the asset. |
| InstanceName | String | test | The name of the asset. |
| InternetIp | String | 1.2.3.1 | The public IP address of the asset. |
| IntranetIp | String | 1.2.3.2 | The private IP address of the asset. |
| Ip | String | 1.2.3.1 | The public IP address of the asset. |
| Name | String | aaa base _ | The name of the software. |
| Path | String | /etc/test | The directory where the software is installed. |
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
<DescribePropertySoftwareDetail>
  <RequestId>9C5AE850-7140-4DE6-B892-055EB0D9F28A</RequestId>
  <PageInfo>
        <Count>2</Count>
        <TotalCount>35795</TotalCount>
        <PageSize>2</PageSize>
        <CurrentPage>1</CurrentPage>
  </PageInfo>
  <Propertys>
        <Uuid>04c56617-23fc-***</Uuid>
        <Name>abrt</Name>
        <Ip>1.2.3.1</Ip>
        <CreateTimestamp>1561330240000</CreateTimestamp>
        <IntranetIp>1.2.3.3</IntranetIp>
        <InstanceId>i-bp***</InstanceId>
        <Create>2019-06-24T06:50Z</Create>
        <InternetIp>1.2.3.1</InternetIp>
        <InstallTime>2014-08-14 21:18:50</InstallTime>
        <Version>2.0.8</Version>
        <InstanceName>Test***</InstanceName>
        <Path>/etc/abrt</Path>
  </Propertys>
  <Propertys>
        <Uuid>c038fd42-3151-4***</Uuid>
        <Name>abrt</Name>
        <Ip>1.2.3.5</Ip>
        <CreateTimestamp>1562283761000</CreateTimestamp>
        <IntranetIp>1.2.3.6</IntranetIp>
        <InstanceId>i-b***</InstanceId>
        <Create>2019-07-05T07:42Z</Create>
        <InternetIp>1.2.3.5</InternetIp>
        <InstallTime>2014-11-21 18:23:32</InstallTime>
        <Version>2.1.11</Version>
        <InstanceName>Test host***</InstanceName>
        <Path>/etc/abrt</Path>
  </Propertys>
</DescribePropertySoftwareDetail>
```

`JSON` format `{`

```json
 "RequestId":"9C5AE850-7140-4DE6-B892-055EB0D9F28A",
 "PageInfo":{
  "Count":2,
  "TotalCount":35795,
  "PageSize":2,
  "CurrentPage":1
```

`},`

```json
 "Propertys":[
```

`{`

```json
   "Name":"abrt",
   "Uuid":"04c56617-23fc-***",
   "Ip":"1.2.3.1",
   "CreateTimestamp":1561330240000,
   "Create":"2019-06-24T06:50Z",
   "InstanceId":"i-bp***",
   "IntranetIp":"1.2.3.3",
   "InternetIp":"1.2.3.1",
   "InstallTime":"2014-08-14 21:18:50",
   "Version":"2.0.8",
   "InstanceName":"Test****",
   "Path":"/etc/abrt"
```

`},` `{`

```json
   "Name":"abrt",
   "Uuid":"c038fd42-3151-4***",
   "Ip":"1.2.3.5",
   "CreateTimestamp":1562283761000,
   "Create":"2019-07-05T07:42Z",
   "InstanceId":"i-b***",
   "IntranetIp":"1.2.3.6",
   "InternetIp":"1.2.3.5",
   "InstallTime":"2014-11-21 18:23:32",
   "Version":"2.1.11",
   "InstanceName":"Test host****",
   "Path":"/etc/abrt"
```

`}` `]` `}`

**Error codes**

For a list of error codes, see Error codes.

#### 6.7.7 DescribePropertySoftwareItem

Queries information about all software assets.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|

| Action | String | Yes | DescribePropert ySoftwareItem | The operation that you want to perform. Set the value to DescribePropertySoftwareItem. |
|---|---|---|---|---|
| ForceFlush | Boolean | No | true | Specifies whether to force refresh the data that you want to query. |
| Name | String | No | test | The name of the software. |
| CurrentPage | Integer | No | 1 | The page number of the current page. |
| PageSize | Integer | No | 10 | The number of entries to return on each page. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 3A85CFCF-05C8- 451A-9E41- C0D5E96BA407 | The ID of the request. |
| PropertyItems | Array |   | The returned software assets. |
| Name | String | aaa base _ | The name of the returned software asset. |
| Count | Integer | 23 | The number of servers on which the software is installed. |
| PageInfo | Struct |   | The page information. |
| Count | Integer | 2 | The number of entries returned on the current page. |
| PageSize | Integer | 2 | The number of entries returned per page. |
| TotalCount | Integer | 5037 | The total number of returned entries. |
| CurrentPage | Integer | 1 | The page number of the current page. |

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

**Error codes**

For a list of error codes, see Error codes.

#### 6.7.8 DescribePropertyUserDetail

Queries the details of an account in the account list.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribePropert yUserDetail | The operation that you want to perform. Set the value to DescribePropertyUserDetail. |
| Remark | String | No | 0.0.0.0 | The name or IP address of the server. |
| User | String | No | test | The name of the account that you want to query. |
| IsRoot | String | No | 0 | Specifies whether the account has root permissions. Valid values: 0: The account does not have root permissions. 1: The account has root permissions. |
| Uuid | String | No | 50d213b4-3a35- 427a-b8a5- 04b0c7e1f4d2 | The UUID of the asset. |
| CurrentPage | Integer | No | 1 | The number of the page to return. |
| PageSize | Integer | No | 2 | The number of entries to return on each page. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | FAA793EF-5B14- 4CDD-B3E0- B14D4342C422 | The ID of the request. |
| Propertys | Array |   | The returned account details. |
| LastLoginTime | String | xxxx | The time of the last logon. |

| IsRoot | String | 0 | Indicates whether the account has root permissions. 0: The account does not have root permissions. 1: The account has root permissions. |
|---|---|---|---|
| InstanceName | String | null | The name of the asset. |
| AccountsExpir ationDate | String | never | The expiration date of the account. |
| PasswordExpir ationDate | String | never | The expiration date of the account password. |
| Ip | String | null | The IP address of the asset. |
| Create | String | 1565644643000 | The timestamp when the last asset fingerprint was collected. |
| CreateTimesta mp | Long | 1565644643000 | The timestamp generated for the asset fingerprint. |
| User | String | adm | The name of the account. |
| Uuid | String | 02c4a5dc-c2d2- 483a-9015- f972b44d2cd9 | The UUID of the asset. |
| LastLoginIp | String | N/A | The source IP address of the last logon. |
| InstanceId | String | 02c4a5dc-c2d2- 483a-9015- f972b44d2cd9 | The ID of the asset. |
| IntranetIp | String | 0.0.0.0 | The private IP address of the asset. |
| InternetIp | String | 0.0.0.0 | The public IP address of the asset. |
| Status | String | 0 | The logon status of the account. Valid values: 0: The account cannot log on. 1: The account can log on. |
| GroupNames | List | adm | The name of the user group. |

| PageInfo | Struct |   | The page information. |
|---|---|---|---|
| Count | Integer | 2 | The number of entries returned on the current page. |
| PageSize | Integer | 2 | The number of entries returned per page. |
| TotalCount | Integer | 384 | The total number of returned entries. |
| CurrentPage | Integer | 1 | The page number of the returned page. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribePropertyUserDetail &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribePropertyUserDetailResponse>
  <requestId>FAA793EF-5B14-4CDD-B3E0-B14D4342C422</requestId>
  <PageInfo>
        <Count>2</Count>
        <PageSize>2</PageSize>
        <TotalCount>384</TotalCount>
        <CurrentPage>1</CurrentPage>
  </PageInfo>
  <Propertys>
        <LastLoginTime>N/A</LastLoginTime>
        <GroupName>adm</GroupName>
        <IsRoot>0</IsRoot>
        <InstanceName></InstanceName>
        <AccountsExpirationDate>never</AccountsExpirationDate>
        <PasswordExpirationDate>never</PasswordExpirationDate>
        <Ip></Ip>
        <Create>1565644643000</Create>
        <Status>0</Status>
        <User>adm</User>
        <Uuid>00ea0155-548e-4f32-bb53-3a000110b30d</Uuid>
        <LastLoginIp>N/A</LastLoginIp>
  </Propertys>
  <Propertys>
        <LastLoginTime>N/A</LastLoginTime>
        <GroupName>adm</GroupName>
        <IsRoot>0</IsRoot>
        <InstanceName></InstanceName>
        <AccountsExpirationDate>never</AccountsExpirationDate>
        <PasswordExpirationDate>never</PasswordExpirationDate>
        <Ip></Ip>
        <Create>1565652008000</Create>
        <Status>0</Status>
        <User>adm</User>
        <Uuid>02c4a5dc-c2d2-483a-9015-f972b44d2cd9</Uuid>
        <LastLoginIp>N/A</LastLoginIp>
  </Propertys>
</DescribePropertyUserDetailResponse>
```

`JSON` format `{`

```json
    "requestId": "FAA793EF-5B14-4CDD-B3E0-B14D4342C422",
    "PageInfo": {
      "Count": 2,
      "PageSize": 2,
      "TotalCount": 384,
      "CurrentPage": 1
```

`},`

```json
    "Propertys": [
```

`{`

```json
        "LastLoginTime": "N/A",
        "GroupName": [
          "adm"
```

`],`

```json
        "IsRoot": "0",
        "InstanceName": null,
        "AccountsExpirationDate": "never",
        "PasswordExpirationDate": "never",
        "Ip": null,
        "Create": 1565644643000,
        "Status": 0,
        "User": "adm",
        "Uuid": "00ea0155-548e-4f32-bb53-3a000110b30d",
        "LastLoginIp": "N/A"
```

`},` `{`

```json
        "LastLoginTime": "N/A",
        "GroupName": [
          "adm"
```

`],`

```json
        "IsRoot": "0",
        "InstanceName": null,
        "AccountsExpirationDate": "never",
        "PasswordExpirationDate": "never",
        "Ip": null,
        "Create": 1565652008000,
        "Status": 0,
        "User": "adm",
        "Uuid": "02c4a5dc-c2d2-483a-9015-f972b44d2cd9",
        "LastLoginIp": "N/A"
```

`}` `]` `}`

**Error codes**

For a list of error codes, see Error codes.

#### 6.7.9 DescribePropertyUserItem

Queries the account information about an asset.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribePropert yUserItem | The operation that you want to perform. Set the value to DescribePropertyUserItem. |
| CurrentPage | Integer | No | 1 | The page number of the current page. |
| ForceFlush | Boolean | No | true | Specifies whether to force refresh the data that you want to query. |
| PageSize | Integer | No | 2 | The number of entries to return on each page. |
| User | String | No | adm | The account information about the asset fingerprint. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| PageInfo |   |   | The page information. |
| Count | Integer | 2 | The number of entries returned on the current page. |
| CurrentPage | Integer | 1 | The page number of the current page. |
| PageSize | Integer | 2 | The number of entries returned per page. |
| TotalCount | Integer | 114 | The total number of returned entries. |
| PropertyItems | Array |   | The account information. |
| Count | Integer | 384 | The number of servers that belong to the current account. |
| User | String | adm | The name of the account. |
| RequestId | String | 76068BE2-F9C4- 4EDD-967B- F503B8CCDD3D | The ID of the request. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribePropertyUserItem &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribePropertyUserItem>
  <PropertyItems>
        <User>a123456</User>
        <Count>1</Count>
  </PropertyItems>
  <PropertyItems>
        <User>aaaa</User>
        <Count>1</Count>
  </PropertyItems>
  <PropertyItems>
        <User>aaaa1</User>
        <Count>1</Count>
  </PropertyItems>
  <RequestId>76068BE2-F9C4-4EDD-967B-F503B8CCDD3D</RequestId>
  <PageInfo>
        <Count>3</Count>
        <TotalCount>340</TotalCount>
        <PageSize>3</PageSize>
        <CurrentPage>1</CurrentPage>
  </PageInfo>
</DescribePropertyUserItem>
```

`JSON` format `{`

```json
 "RequestId":"76068BE2-F9C4-4EDD-967B-F503B8CCDD3D",
 "PropertyItems":[
```

`{`

```json
   "User":"a123456",
   "Count":1
```

`},` `{`

```json
   "User":"aaaa",
   "Count":1
```

`},` `{`

```json
   "User":"aaaa1",
   "Count":1
```

`}` `],`

```json
 "PageInfo":{
  "Count":3,
  "TotalCount":340,
  "PageSize":3,
  "CurrentPage":1
```

`}` `}`

**Error codes**

For a list of error codes, see Error codes.

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

| Count | Integer | 2 | The number of module configurations. |
|---|---|---|---|
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
