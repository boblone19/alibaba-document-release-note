---
title: "Alibaba Cloud Apsara Stack V3.18.2 Alibaba Cloud Security-Server Guard Advanced Edition Server Guard Advanced Edition Developer Guide 20250613"
product_version: "V3.18.2"
doc_version: "20250613"
pdf_pages: 165
source_pdf: "Alibaba Cloud Apsara Stack V3.18.2 Alibaba Cloud Security-Server Guard Advanced Edition Server Guard Advanced Edition Developer Guide 20250613.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/v3.18.2%E7%89%88%E6%9C%AC%E6%96%87%E6%A1%A3/%E5%AE%89%E9%AA%91%E5%A3%AB/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.2%20Alibaba%20Cloud%20Security-Server%20Guard%20Advanced%20Edition%20Server%20Guard%20Advanced%20Edition%20Developer%20Guide%2020250613.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes)
---

# Alibaba Cloud Apsara Stack V3.18.2 Alibaba Cloud Security-Server Guard Advanced Edition Server Guard Advanced Edition Developer Guide 20250613

## Table of Contents

- 1 Preparations
  - 1.1 Obtain API information and the endpoint of an API operation
  - 1.2 Obtain an AccessKey pair
  - 1.3 Obtain the values of common request headers
  - 1.4 Obtain an AccessKey pair assigned by STS
- 2 Call examples
  - 2.1 Call examples for SDK for Java
    - 2.1.1 Use SDK
      - 2.1.1.1 Install SDK for Java
      - 2.1.1.2 Use CommonRequest
  - 2.2 Call examples for SDK for Python
    - 2.2.1 Use SDK
      - 2.2.1.1 Install SDK for Python
      - 2.2.1.2 Use CommonRequest
  - 2.3 Call examples for SDK for Go
    - 2.3.1 Use SDK
      - 2.3.1.1 Install the core package of SDK for Go
      - 2.3.1.2 Use CommonRequest
- 3 Common parameters
- 4 API documentation
  - 4.1 Make API requests
    - 4.1.1 Request structure
    - 4.1.2 Request signatures
    - 4.1.3 Common request parameters
    - 4.1.4 Response structure
  - 4.2 Asset management
    - 4.2.1 DescribeGroupSummary
    - 4.2.2 DescribeGroupStruct
    - 4.2.3 DescribeAllEntity
    - 4.2.4 DescribeEntityList
    - 4.2.5 DescribeMachines
    - 4.2.6 DescribeMachineDetail
    - 4.2.7 DescribePropertyStatistic
    - 4.2.8 DescribePropertyPortItem
    - 4.2.9 DescribePropertyPortDetail
    - 4.2.10 DescribePropertyProcItem
    - 4.2.11 DescribePropertyProcDetail
    - 4.2.12 DescribePropertySoftwareItem
    - 4.2.13 DescribePropertySoftwareDetail
    - 4.2.14 DescribePropertyUserItem
    - 4.2.15 DescribePropertyUserDetail
    - 4.2.16 DescribeTopRiskyAssets
  - 4.3 Vulnerability management
    - 4.3.1 DescribeTarget
    - 4.3.2 DescribeVulTargetStatistics
    - 4.3.3 DescribeTargetConfig
    - 4.3.4 DescribeVulConfig
    - 4.3.5 DescribeAutoDelConfig
    - 4.3.6 DescribeVulLevel
    - 4.3.7 DescribeVulWhitelist
    - 4.3.8 DescribeGroupedVul
    - 4.3.9 DescribeVulList
    - 4.3.10 DescribeVulDetails
    - 4.3.11 DescribeVulNumStatistics
    - 4.3.12 DescribeVulLevelStatistics
    - 4.3.13 DescribeVulMachineList
  - 4.4 Baseline check
    - 4.4.1 DescribeStratetyDetail
    - 4.4.2 DescribeStrategyTarget
    - 4.4.3 DescribeUuidConfig
    - 4.4.4 DescribeUserSetting
    - 4.4.5 DescribeRiskWhiteList
    - 4.4.6 DescribeStratety
    - 4.4.7 DescribeStrategyExecDetail
    - 4.4.8 DescribeRiskType
    - 4.4.9 Describesummary
  - 4.5 Unusual logon detection
    - 4.5.1 DescribeBaseConfigs
    - 4.5.2 DescribeSwitchConfigs
    - 4.5.3 DescribeConfigTarget
    - 4.5.4 ModifyBaseConfig
    - 4.5.5 DeleteBaseConfig
    - 4.5.6 ModifySwitchConfig
  - 4.6 Webshell detection
    - 4.6.1 DescribeCategoryCount
    - 4.6.2 DescribeWebshell
    - 4.6.3 DescribeQuaraFile
    - 4.6.4 RollbackQuaraFile
    - 4.6.5 DescribeWebPath
    - 4.6.6 ModifyWebPath
    - 4.6.7 OperateTrojan
  - 4.7 Exception detection on hosts
    - 4.7.1 DescribeSuspEventTypes
    - 4.7.2 DescribeSuspTrendStatistics
    - 4.7.3 DescribeSuspiciousExportInfo
    - 4.7.4 OperateSuspiciousEvent
    - 4.7.5 OperateLoginLog
    - 4.7.6 DescribeVirusInfo
    - 4.7.7 CreateSuspiciousExport
  - 4.8 Retrieval of host logs
    - 4.8.1 DescribeFilterFields
    - 4.8.2 DescribeHistogram
    - 4.8.3 DescribeLogInfo
    - 4.8.4 DescribeLogItems
    - 4.8.5 CreateLogQuery
    - 4.8.6 DescribeLogQuery
    - 4.8.7 DeleteLogQuery
- 5 Error codes

## 1 Preparations

### 1.1 Obtain API information and the endpoint of an API operation

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
7. Select an API operation and obtain the POP endpoint of the cloud service on the Parameter
tab.

### 1.2 Obtain an AccessKey pair

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

### 1.3 Obtain the values of common request headers

**request headers**

You must specify multiple request headers when you call Apsara Stack API operations. This topic describes the common request headers and how to obtain the values of the request headers. This topic also describes the return values of specific parameters after you call API operations.

**Common request headers**

| Header | Description |
|---|---|
| x-acs-regionid | The ID of the region. For more information about how to obtain region IDs, see Obtain a region ID. |
| x-acs-organizationid | The ID of the organization in the Apsara Uni- manager Management Console. For more information about how to obtain organization IDs, see Obtain an organization ID. |
| x-acs-resourcegroupid | The ID of the resource set in the Apsara Uni- manager Management Console. For more information about how to obtain resource set IDs, see Obtain a resource set ID. |
| x-acs-instanceid | The ID of the instance that you want to manage. For more information about how to obtain instance IDs, see Obtain an instance ID. |

**Obtain a region ID**

1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, click **Enterprise**.
3. In the left-side navigation pane, choose **Resources** > **Regions**.
4. Click the name of the required organization.
5. In the **Regions** section, view the region ID.

**Obtain an organization ID**

You must call an operation to obtain an organization ID. For more information about how to obtain organization IDs, see the GetOrganizationList section in Apsara Uni-manager Management Console Developer Guide.

**Obtain a resource set ID**

You must call an operation to obtain a resource set ID. For more information about how to obtain resource set IDs, see the ListResourceGroup section in Apsara Uni-manager Management Console Developer Guide.

**Obtain an instance ID**

You can obtain the ID of an instance in a service console of the Apsara Uni-manager Management Console. This section uses the Elastic Compute Service (ECS) console as an example. Perform the following operations to obtain the ID of an ECS instance:
1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Products** > **Elastic Computing** > **Elastic Compute**
**Service**.
3. In the left-side navigation pane, click **Instances**.
4. View the **instance ID** in the instance list.
The following table describes the additional response parameters that are returned by default when you call API operations to query the instances of cloud services.

| Parameter | Description |
|---|---|
| ResourceGroupName | The name of the resource set. |
| ResourceGroup | The ID of the resource set. |
| DepartmentName | The name of the organization. |
| Department | The ID of the organization. |

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
> "sts.aliyuns.com": Replace it with the endpoint of STS.

```java
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
private static String callAssumeRole(IAcsClient client) {
    CommonRequest request = new CommonRequest();
    // Replace "sts.aliyuns.com" with the actual endpoint of STS. The format of an ST
S endpoint is sts-vpc.${global:region}.${global:internet-domain}.
    request.setSysDomain("sts.aliyuns.com");
    request.setSysProduct("Sts");
    request.setSysAction("AssumeRole");
    request.setSysVersion("2015-04-01");
    request.setSysMethod(MethodType.POST);
    request.setHttpContentType(FormatType.FORM);
    // Replace "<yourRoleSessionName>" with the name of the current session.
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
    return null;
```

3. Use the AccessKey pair assigned by STS to call an operation of a cloud service. The
following sample code provides an example on how to use the AccessKey pair assigned by STS to call the `DescribeZones` operation of Elastic Compute Service (ECS):

> **Note:** You must use the actual values to replace the variables in the following sample code. The angle brackets <> are not retained in the final code.
> The following list describes the variables:
> <yourRegionID>: Replace it with the actual region ID.
> <yourStsAccesskeyID>: Replace it with your STS AccessKey ID.
> <yourStsAccessKeySecret>: Replace it with your STS AccessKey secret.
> <yourStsToken>: Replace it with the security token of the AccessKey pair assigned by STS.
> <yourResourceGroupID>: Replace it with the actual resource set ID.
> <yourOrganizationID>: Replace it with the actual organization ID.

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

## 2 Call examples

### 2.1 Call examples for SDK for Java

#### 2.1.1 Use SDK

##### 2.1.1.1 Install SDK for Java

This topic describes how to install and use Apsara Stack Security SDK for Java. Apsara Stack SDK for Java supports Java Development Kit (JDK) 1.8 or later. You can install Apsara Stack SDK for Java by adding Maven dependencies or downloading the SDK. For more information, visit Alibaba Cloud SDKs. If you want to use Apsara Stack Security SDK for Java, you must install the core library of Apsara Stack SDK for Java. We recommend that you use V4.5.17 or later of the core library. When you install the core library, you must add the following dependency to the pom.xml file. For more information about the specific SDK version, visit Alibaba Cloud SDKs.

```xml
<!-- Alibaba Cloud SDK for Java --> <dependency>
    <groupId>com.aliyun</groupId>
    <artifactId>aliyun-java-sdk-core</artifactId>
    <version>4.5.17</version>
</dependency>
```

##### 2.1.1.2 Use CommonRequest

Before you use point of presence (POP) SDK for Java to make API calls, you must first understand the remote procedure call (RPC) and resource-oriented architecture (ROA) styles.

**Prerequisites**

We recommend that you use CommonRequest to make API calls in Apsara Stack. You can go to the Apsara Uni-manager Management Console and choose **Products** > **Development**
**Tools** > **API & SDK** > **OpenAPI Explorer,** and then select **API Integration** > **SDK**
**Examples** to view the recommended SDK versions and sample code.

**Important**

We do not recommend that you download SDKs from the SDK Center for use in Apsara Stack scenarios. The SDKs for Alibaba Cloud public cloud may not support the APIs of Apsara Stack. Compatibility issues may occur. Use these SDKs with caution! RPC call example with the following API information: product (apigateway), operation (DescribeApiGroups), and version (2016-07-14). Sample code:

```java
import com.aliyuncs.CommonRequest; import com.aliyuncs.CommonResponse; import com.aliyuncs.DefaultAcsClient;
```

```java
import com.aliyuncs.IAcsClient; import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.exceptions.ServerException; import com.aliyuncs.http.MethodType; import com.aliyuncs.profile.DefaultProfile; public class DescribeApiGroups {
    public static void main(String[] args) {
        // Create a DefaultAcsClient instance and initialize it.
        DefaultProfile profile = DefaultProfile.getProfile("", "", "");
        // Ignore SSL certificate verification.
        // HttpClientConfig clientConfig = HttpClientConfig.getDefault();
        // clientConfig.setIgnoreSSLCerts(true);
        // Specify the timeout period for a connection.
        // clientConfig.setConnectionTimeoutMillis(3000L);
        // Specify the read timeout period.
        // clientConfig.setReadTimeoutMillis(10000L);
        // profile.setHttpClientConfig(clientConfig);
        IAcsClient client = new DefaultAcsClient(profile);
        // Create an API request and set the parameters.
        CommonRequest request = new CommonRequest();
        // Specify the request method
        request.setSysMethod(MethodType.POST);
        // Specify the endpoint of the service.
        request.setSysDomain("");
        // Specify the API version.
        request.setSysVersion("2016-07-14");
        // Specify the service name.
        request.setSysLocationProduct("apigateway");
        // Specify the name of the API operation.
        request.setSysAction("DescribeApiGroups");
        // If you use the Security Token Service (STS) AccessKey pair to call RPC API o
perations, you must specify the SecurityToken parameter.
        // request.putBodyParameter("SecurityToken", "");
        // Set service-related parameters.
        request.putQueryParameter("PageSize", "10");
        request.putQueryParameter("PageNumber", "1");
        // (Required) Specify the call source.
        request.putHeadParameter("x-acs-caller-sdk-source", "ApiTestDemo");
        // (Optional) You must specify this parameter for Apsara Stack V3.15.0 or
earlier.
        request.putHeadParameter("x-acs-regionid", "");
        // (Optional) Specify the ID of the resource set.
        request.putHeadParameter("x-acs-resourcegroupid", "");
        // (Required) Specify the organization ID.
        request.putHeadParameter("x-acs-organizationid", "");
        // (Optional) You must specify this parameter when you modify or delete
resources.
```

```java
        // request.putHeadParameter("x-acs-instanceid", "");
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

ROA call example with the following API information: product (CR), operation (GetNamespaceList), and version (2016-06-07). Sample code:

```java
import com.aliyuncs.CommonRequest; import com.aliyuncs.CommonResponse; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.exceptions.ServerException; import com.aliyuncs.http.MethodType; import com.aliyuncs.profile.DefaultProfile; public class GetNamespaceList {
    public static void main(String[] args) {
        // Create a DefaultAcsClient instance and initialize it.
        DefaultProfile profile = DefaultProfile.getProfile("", "", "");
        // Ignore SSL certificate verification.
        // HttpClientConfig clientConfig = HttpClientConfig.getDefault();
        // clientConfig.setIgnoreSSLCerts(true);
        // Specify the timeout period for a connection.
        // clientConfig.setConnectionTimeoutMillis(3000L);
        // Specify the read timeout period.
        // clientConfig.setReadTimeoutMillis(10000L);
        // profile.setHttpClientConfig(clientConfig);
        IAcsClient client = new DefaultAcsClient(profile);
        // Create an API request and set the parameters.
        CommonRequest request = new CommonRequest();
        // Configure HTTPS access
        request.setSysProtocol(ProtocolType.HTTP);
        // Specify the request method
        request.setSysMethod(MethodType.GET);
        // Specify the endpoint of the service
```

`p` `y` `p`

```java
        request.setSysDomain("");
        // Specify the API version
        request.setSysVersion("2016-06-07");
        // Set the URI pattern (required only for ROA calls)
        request.setSysUriPattern("/namespace");
        // Specify the service name
        request.setSysLocationProduct("cr");
        // Specify the name of the API operation
        request.setSysAction("GetNamespaceList");
        // (Required) Specify the call source.
        request.putHeadParameter("x-acs-caller-sdk-source", "ApiTestDemo");
        // (Optional) You must specify this parameter for Apsara Stack V3.15.0 or
earlier.
        request.putHeadParameter("x-acs-regionid", "");
        // Optional. Specify the ID of the resource set.
        request.putHeadParameter("x-acs-resourcegroupid", "");
        // Required. Specify the organization ID.
        request.putHeadParameter("x-acs-organizationid", "");
        // (Optional) You must specify this parameter when you modify or delete
resources.
        // request.putHeadParameter("x-acs-instanceid", "");
        // When you use an STS AccessKey pair to call ROA API operations, you must add
the x-acs-security-token field to the header
        // request.putHeadParameter("x-acs-security-token", "");
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

> **Important:** By default, if you send API requests over HTTPS, the SDK enables certificate verification to verify the validity of SSL/TLS certificates. If no certificate is configured in the development environment, an error that indicates the certificate verification fails is reported.
> To ensure communication security in the production environment, we recommend that you enable certificate verification. If certificate verification must be disabled in the test environment, you can configure the following setting:

Java

```
HttpClientConfig clientConfig = HttpClientConfig.getDefault(); // Disable server certificate verification. clientConfig.setIgnoreSSLCerts(true)
```

### 2.2 Call examples for SDK for Python

**Python**

#### 2.2.1 Use SDK

##### 2.2.1.1 Install SDK for Python

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

##### 2.2.1.2 Use CommonRequest

This topic describes how to use POP Python SDK to call cloud product APIs.

**Prerequisites**

We recommend using CommonRequest for API calls in Apsara Stack. You can view the recommended SDK version and sample code in the Apsara Uni-manager Management Console by navigating to **Products** > **Development Tools** > **API & SDK** > **OpenAPI**
**Explorer**, and selecting **API Integration** > **SDK Examples**.

**Important**

We do not recommend downloading SDKs directly from the SDK Center for use in Apsara Stack scenarios. The public cloud SDKs may not support Apsara Stack APIs and may have compatibility issues. Please use with caution!

**Background information**

Currently, only the RPC method is supported for API calls.

**CommonRequest call example**

Example interface information: Product (ECS), Interface (DescribeInstances), Version (2014- 05-26). Sample code is as follows:

```java
from aliyunsdkcore.client import AcsClient import os from aliyunsdkcore.request import CommonRequest
# Create AcsClient instance
client = AcsClient(
    "<AccessKey ID>",
    "<AccessKey Secret>",
    "<your-RegionID>",
    timeout=1000,  # Set timeout
    verify=False, # Ignore certificate or verify='<certificate location>'
```

);

```python
# Use with https
# client.set_verify(False)
# os.environ["HTTPS_PROXY"] = "http://127.0.0.1:8080"
# os.environ["HTTP_PROXY"] = "http://127.0.0.1:8080"
def describe_api_groups():
    # Create request and set parameters
    request = CommonRequest()
    # When using sts ak to call rpc interface, you need to add SecurityToken field in p
arameters
    # params = {"PageSize":"10","PageNumber":"1","SecurityToken":"<your-
SecurityToken>"};
    params = {"PageSize":"10","PageNumber":"1"};
    request.set_query_params(params)
    headers = {
        # Required, call source description
        "x-acs-caller-sdk-source":"ApiTestDemo",
        # Optional, required for historical versions before Enterprise Edition V3.15.0
        "x-acs-regionid":"<your-RegionID>",
        # Optional, resource set ID
        "x-acs-resourcegroupid":"<your-ResourceGroupID>",
        # Required, organization ID
        "x-acs-organizationid":"<your-OrganizationID>"
        # Optional, required for modify & delete operations
        # "x-acs-instanceid":"<your-InstanceID>"
    request.set_headers(headers)
    request.set_version("2016-07-14")
    request.set_action_name("DescribeApiGroups")
    request.set_endpoint("<ApigatewayEndpoint>")   //Please replace Endpoint with the r
eal address
    request.set_product("apigateway")
    request.set_method("POST")
    # Initiate API request and display return value
```

```python
    response = client.do_action_with_exception(request)
    print(response)
if __name__ == '__main__':
    print("Hello Aliyun OpenApi!")
    describe_api_groups()
```

**Set proxy**

When calling APIs, you may need to set HTTP_PROXY and HTTPS_PROXY through environment variables. Sample code is as follows:

```bash
# https proxy
os.environ["HTTPS_PROXY"] = "http://x.x.x.x:xxxx"
# http proxy
os.environ["HTTP_PROXY"] = "https://x.x.x.x:xxxx"
```

**HTTPS configuration**

The following describes how to access OpenAPI using HTTPS protocol.

**Using HTTPS protocol**

SDK uses HTTPS protocol by default.

```
from aliyunsdkecs.request.v20140526.DescribeInstancesRequest import DescribeInstancesRequest from aliyunsdkcore.client import AcsClient client = AcsClient(
    region_id='<region_id>',  # Region ID
```

`)`

```
request = DescribeInstancesRequest() request.set_protocol_type('https') # Use https client.do_action_with_exception(request)
```

**Ignore certificate**

> **Important:** When accessing OpenAPI using HTTPS protocol, the SDK will verify SSL/TLS certificate validity by default. If your code environment does not have a certificate environment, it will report a certificate verification failure error.
> To ensure communication security in production environments, we recommend keeping verification enabled. If you must ignore certificate verification in a test environment, you can set it through the `verify` parameter.

```
from aliyunsdkcore.client import AcsClient client = AcsClient(
    region_id='<region_id>',  # Region ID
    verify=False  # Ignore SSL certificate verification
```

`)`

**Specify CA certificate file**

```
from aliyunsdkcore.client import AcsClient client = AcsClient(
    region_id='<region_id>',  # Region ID
    verify='./cacert.pem'  # Certification path
```

`)`

### 2.3 Call examples for SDK for Go

#### 2.3.1 Use SDK

##### 2.3.1.1 Install the core package of SDK for Go

This topic describes how to install the core package of SDK for Go. Apsara Stack SDK for Go supports Go 1.10.x and later. You can run the following command to install the core package:

```
go get -u github.com/aliyun/alibaba-cloud-sdk-go/sdk
```

##### 2.3.1.2 Use CommonRequest

This topic describes how to work with the POP SDK for Go.

**Prerequisites**

For Apsara Stack, we recommend that you use CommonRequest to call API operations. You can view the recommended SDK versions and sample code in the Apsara Uni-manager Management Console by choosing **Products** > **Development Tools** > **API & SDK** >
**OpenAPI Explorer**, and then selecting **API Integration** > **SDK Examples**.

**Important**

We do not recommend that you download SDKs from the SDK center for use in Apsara Stack environments. The SDKs for Alibaba Cloud public cloud may not support the API operations of Apsara Stack and may have compatibility issues. Use them with caution!

**Background information**

Remote procedure call (RPC) and resource-oriented architecture (ROA) styles are supported for API calls. RPC example API information: product (apigateway), API operation (DescribeApiGroups), and version (2016-07-14). The following sample code provides an example:

```java
package main import (
    "fmt"
    "github.com/aliyun/alibaba-cloud-sdk-go/sdk"
    "github.com/aliyun/alibaba-cloud-sdk-go/sdk/requests"
```

`)`

```
func main() {
    client, err := sdk.NewClientWithAccessKey("", "", "")
    request := requests.NewCommonRequest()
    request.Method = "POST"
    request.Domain = ""
    request.Version = "2016-07-14"
    request.ApiName = "DescribeApiGroups"
    request.Product = "apigateway"
    // If you use the Security Token Service (STS) to AccessKey pair to call RPC API op
erations, you must specify the SecurityToken parameter.
    // request.QueryParams["SecurityToken"]=""
    // Required. Specify the call source.
    request.Headers["x-acs-caller-sdk-source"] = "ApiTestDemo"
    // Optional. You must specify this parameter for Apsara Stack V3.15.0 or earlier.
    request.Headers["x-acs-regionid"] = ""
    // Optional. Specify the ID of the resource set.
    request.Headers["x-acs-resourcegroupid"] = ""
    // Required. Specify the organization ID.
    request.Headers["x-acs-organizationid"] = ""
    // Optional. You must specify this parameter when you modify or delete resources.
    // request.Headers["x-acs-instanceid"] = ""
    response, err := client.ProcessCommonRequest(request)
    if err != nil {
        panic(err)
    fmt.Print(response.GetHttpContentString())
```

ROA example API information: product (CR), API operation (GetNamespaceList), and version (2016-06-07). Sample code:

```java
package main import (
 "fmt"
 "github.com/aliyun/alibaba-cloud-sdk-go/sdk"
 "github.com/aliyun/alibaba-cloud-sdk-go/sdk/requests"
 "os"
```

`)`

```
func main() {
    client, err := sdk.NewClientWithAccessKey("", "", "")
 request := requests.NewCommonRequest()
 request.Method = "GET"
 request.Domain = ""
 request.Version = "2016-06-07"
 request.ApiName = "GetNamespaceList"
 request.Product = "cr"
 request.PathPattern = "/namespace"
 // If you use the STS AccessKey pair to call ROA API operations, you must add the x-
acs-security-token field to the header
 // request.Headers["x-acs-security-token"] = ""
 // Required. Specify the call source.
 request.Headers["x-acs-caller-sdk-source"] = "ApiTestDemo"
    // Optional. You must specify this parameter for Apsara Stack V3.15.0 or earlier.
    request.Headers["x-acs-regionid"] = ""
    // Optional. Specify the ID of the resource set.
    request.Headers["x-acs-resourcegroupid"] = ""
    // Required. Specify the organization ID.
    request.Headers["x-acs-organizationid"] = ""
 // Optional. You must specify this parameter when you modify or delete resources.
 // request.Headers["x-acs-instanceid"] = ""
 response, err := client.ProcessCommonRequest(request)
 if err != nil {
  panic(err)
 fmt.Print(response.GetHttpContentString())
```

**Proxy settings**

You can configure a proxy in one of the following ways when you call API operations: Method 1: Configure a proxy by using environment variables. Specify the HTTP_PROXY and HTTPS_PROXY environment variables, or specify the NO_PROXY environment variable. Sample code:

```java
import (
    "os"
```

`)`

```
func main(){
 os.Setenv("HTTP_PROXY", "http://x.x.x.x:xxxx") // Specify the HTTP_PROXY environment
variable.
 os.Setenv("HTTPS_PROXY", "https://x.x.x.x:xxxx") // Specify the HTTPS_PROXY environm
ent variable.
```

Method 2: Configure a proxy on the client. Sample code:

```
// The proxy settings on the client take precedence over the environment variables. client.SetHttpProxy("http://x.x.x.x:xxxx") // Configure the HTTP proxy. client.GetHttpProxy() // Query the HTTP proxy. client.SetHttpsProxy("https://x.x.x.x:xxxx") // Configure the HTTPS proxy. client.GetHttpsProxy() // Query the HTTPS proxy. client.SetNoProxy("127.0.0.1,localhost") // Configure the proxy whitelist. client.GetNoProxy() // Query the proxy whitelist.
```

**SSL verification**

**Summary**

You can configure SSL certificate verification for requests. If you set this parameter to `true` , certificate verification is disabled. This is not secure. We recommend that you configure certificates. If you set this parameter to `false` , SSL certificate verification is enabled. By default, the CA certificates provided by the operating system are used.

**Default value**

The default value is `false` .

**Settings**

> **Important:** By default, if you send API requests over HTTPS, the SDK enables certificate verification to verify the validity of SSL certificates. If no certificate is configured in the development environment, an error that indicates the certificate verification fails is reported. To ensure communication security in the production environment, we recommend that you enable certificate verification. If certificate verification must be disabled in the test environment, you can specify the following settings:

```
// Configure HTTPSInsecure for the request (affects only the current request) request.SetHTTPSInsecure(true) // Set HTTPSInsecure to true fo r the request. isInsecure := request.GetHTTPSInsecure() // Query the HTTPSInsecure sett ing for the request.
```

The HTTPSInsecure setting takes effect for the client only when you do not specify the HTTPSInsecure parameter for the request.

```
// Configure HTTPSInsecure for the client (affects all requests sent by the client). client.SetHTTPSInsecure(true) // Set HTTPSInsecure to true for t he client. isInsecure := client.GetHTTPSInsecure() // Query the HTTPSInsecure setting for the client.
```

ters

## 3 Common parameters

**Common request parameters**

Common request parameters must be included in all Apsara Stack API requests. Table 1. Common request parameters

| Parameter | Type | Requi red | Description |
|---|---|---|---|
| Format | Strin g | No | The type of the returned value. Set the value to JSON. |
| Version | Strin g | Yes | The version number of the API. Specify the version number in the YYYY-MM-DD format. Valid values: 2018-01-16: Auditprivate 2019-07-23: yundunnextsoc 2018-12-03: Sas 2016-11-11: aegis 2021-10-11: yundun-css 2019-08-05: secspy 2018-01-16: Ddosprivate 2018-06-30: hsm-private 2017-12-07: Cloudfw 2019-01-03: Sddp 2020-07-01: semawaf 2018-12-03: soar |
| AccessKeyId | Strin g | Yes | The AccessKey ID that is provided by Apsara Stack. |
| AccessKeySe cret | Strin g | Yes | The AccessKey secret that is provided by Apsara Stack. |
| RegionId | Strin g | Yes | The region ID of the service. |

ters

| Product | Strin g | Yes | The name of the service to which the operation belongs. Valid values: Auditprivate: basic components of Apsara Stack Security yundunnextsoc: Security Operations Center (SOC) Sas: Threat Detection Service aegis: Server Guard yundun-css: Container Protection secspy: Network Detection and Response Ddosprivate: Anti-DDoS Service hsm-private: Data Encryption Service Cloudfw: Cloud Firewall Sddp: Sensitive Data Discovery and Protection (SDDP) semawaf: Web Application Firewall (WAF) soar: Security Orchestration and Automation Response (SOAR) |
|---|---|---|---|
| EndpointPre | Strin g | Yes | The prefix in the endpoint of the service to which the operation belongs. Valid values: auditprivate: the prefix in the endpoint of basic components of Apsara Stack Security yundunnextsoc-pop: the prefix in the endpoint of SOC tds: the prefix in the endpoint of Threat Detection Service aegis: the prefix in the endpoint of Server Guard yundun-css: the prefix in the endpoint of Container Protection secspy-share: the prefix in the endpoint of Network Detection and Response ddosprivate: the prefix in the endpoint of Anti-DDoS Service hsmprivate: the prefix in the endpoint of Data Encryption Service cloudfw: the prefix in the endpoint of Cloud Firewall sddp-api: the prefix in the endpoint of SDDP semawaf: the prefix in the endpoint of WAF soar: the prefix in the endpoint of SOAR |

**Common response parameters**

API responses use the HTTP response format: A 2xx status code indicates a successful call. A 4xx or 5xx status code indicates a failed call. Responses are returned in the JSON format. Every response returns a unique RequestID regardless of whether the call is successful.

## 4 API documentation

### 4.1 Make API requests

#### 4.1.1 Request structure

Apsara Stack Security API is based on Remote Procedure Call (RPC). This topic describes the structure of the API requests. You can send an HTTP request to call an API operation. The URL of the request must be in the following format:

```
http://endpoint/?Action=xx&parameters
```

Where:

| endpoint | : the endpoint used to call a clo |
|---|---|

`endpoint` : the endpoint used to call a cloud service. The endpoint for the Server Guard service is `aegis.[ RegionId].example.com` . `Action` : the operation that you want to perform. For example, you can set this parameter to DescribeFeatures to query the deployed Apsara Stack Security features. `parameters` : the request parameters. Request parameters include common request parameters and custom request parameters. Request parameters must be separated with ampersands (&). Common request parameters include information such as the API version and authentication information. For more information about the custom request parameters, see the corresponding operation description.

**Example**

Call the DescribeFeatures operation to query the deployed Apsara Stack Security features.

```
https://yundunprivate.[ RegionId].example.com/?Action=DescribeFeatures&AccessKeyId=keytest&Format=JSON&SecureTransport=true&SignatureMethod=HMAC- SHA1&SignatureNonce=15215528852396&SignatureVersion=1.0&SourceIp=1xxxx6&Timestamp=2018- 03-02Txxxxxxx&Version=2018-01-16&Signature=xxxx%xxxx%3D
```

API requests are presented in the following easy-to-read format in this document:

```
https://yundunprivate.[ RegionId].example.com/?Action=DescribeFeatures &Format=JSON &Version=2018-01-16 &Signature=xxxx%xxxx%3D &SignatureMethod=HMAC-SHA1 &SignatureNonce=15215528852396 &SignatureVersion=1.0 &AccessKeyId=key-test &Timestamp=2012-06-01T12:00:00Z
```

#### 4.1.2 Request signatures

Apsara Stack Security authenticates each access request. Therefore, a request must contain signature information regardless of whether it is sent over HTTP or HTTPS.

**Authorization**

To ensure the security of your account, we recommend that you use a RAM user to call API operations. Before you use a RAM user to call an API operation, you must grant the RAM user the required permissions by creating an policy and attaching the policy to the RAM user.

**Signature**

You must sign all API requests to ensure security. Alibaba Cloud uses the request signature to verify the identity of the API caller. When you manually make an API request, you must use the AccessKey secret to calculate an HMAC value based on the encoded and sorted request string. The HMAC value is the signature. For more information, see the definition in RFC 2104. The following parameters are used in the following procedure to describe how to calculate a signature.

| Parameter | Description |
|---|---|
| Endpoint | http://tds.[RegionId].example.com/? |
| Operation-specific parameters | Action=DescribeFeatures |
| Common parameters except Signature | &Timestamp=2018-12-24T12:46:24Z &Format=JSON &AccessKeyId=<yourAccessKeyId> &SignatureMethod=HMAC-SHA1 &SignatureNonce=3ee8c1b8-83d3-44af-a94f-4e0ad82fd6cf &Version=2018-12-03 &SignatureVersion=1.0 |
| Access Key Secret | <yourAccessKeySecret> |

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

#### 4.1.3 Common request parameters

The following table describes the common request parameters that are used to indicate information such as the API version and authentication information.

| Name | Type | Required | Description |
|---|---|---|---|
| Version | String | Yes | The API version in the format of YYYY- MM-DD. Set the value to 2016-11-11. |
| AccessKeyId | String | Yes | The key ID that Alibaba Cloud assigns to a user for service access. |
| Signature | String | Yes | The signature string. |
| SignatureMethod | String | Yes | The signature method. Set the value to HMAC-SHA1. |
| Timestamp | String | Yes | The timestamp of the request. Follow the ISO 8601 standard to specify the date and use the offset from Coordinated Universal Time (UTC) to specify the time zone. The format is YYYY-MM- DDThh:mm:ssZ . For example, 2014-05-26T12:00:00Z indicates 20:00:00 on May 26, 2014, Beijing time. |

|   |   | YYYY-MM- |
|---|---|---|
|   | DDThh:mm:ssZ |   |

| SignatureVersion | String | Yes | The signature algorithm version. Set the value to 1.0. |
|---|---|---|---|
| SignatureNonce | String | Yes | The unique random number used to prevent network replay attacks. You must use different random numbers for different requests. |
| ResourceOwnerA ccount | String | No | The owner account of the resource to be accessed through this API request, that is, the logon username. |
| Format | String | No | The format of the response. Set the value to JSON or XML. Note Default value: XML. |

#### 4.1.4 Response structure

Apsara Stack Security API responses can be returned in either the XML or JSON format. Every response returns a unique ID (indicated by **RequestId**) regardless of whether the call is successful.

**Sample responses (XML format)**

```xml
<? xml version="1.0" encoding="UTF-8"? > <! --The root node of the result--> <Operation name+Response>
    <! --Returned request ID-->
    <RequestId>4C467B38-3910-447D-87BC-AC049166F216</RequestId>
    <! --Returned data-->
</Operation name+Response>
```

**Sample responses (JSON format)**

```json
"RequestId": "4C467B38-3910-447D-87BC-AC049166F216", /* Returned data */
```

### 4.2 Asset management

#### 4.2.1 DescribeGroupSummary

You can call this operation to obtain a list of asset groups.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeGroupSummary. |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| Count | Integer | The number of asset groups. |
| Groups | List | The information about asset groups. For more information, see the following parameter descriptions. |
| GroupId | Long | The asset group ID. |
| GroupIndex | Integer | The sequence number of the asset group. |
| GroupLevel | Integer | The level of the asset group. |
| GroupName | String | The name of the asset group. |
| GroupFather | Integer | The ID of the parent asset group. |
| GroupFlag | Integer | The type of the asset group. Valid values: 1: indicates a non-leaf node group that contains child asset groups. 0: indicates a leaf node group. |
| MachineNum | Integer | The number of ECS instances contained in the group. |

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=DescribeGroupSummary
```

Sample responses (JSON format)

```json
 "Groups":[
   "GroupFlag":1,
   "GroupName":"Test group 21",
   "GroupIndex":1,
   "MachineNum":0,
   "GroupId":346
```

`},`

```json
   "GroupFlag":1,
   "GroupName":"Test group 1",
   "GroupIndex":2,
   "MachineNum":0,
   "GroupId":343
```

`},`

```json
   "GroupFlag":1,
   "GroupName":"Test group 2",
   "GroupIndex":3,
   "MachineNum":0,
   "GroupId":345
```

`},`

```json
   "GroupFlag":0,
   "GroupName":"Not grouped",
   "GroupIndex":100,
   "MachineNum":1,
   "GroupId":336
```

`],`

```json
 "Count":4,
 "RequestId":"B9FB5483-3CA6-4520-9F89-068ED6AAC6EE"
```

#### 4.2.2 DescribeGroupStruct

You can call this operation to query the asset group structure.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set this parameter to DescribeGroupStruct. |
| Mark | String | No | The IP address or instance name of the server. |

| TagIdList | String | No | The server tag ID. |
|---|---|---|---|

| Parameter | Type | Description |
|---|---|---|
| RequestId | String | The ID of the request. |
| GroupFather | Integer | The ID of the parent asset group. |
| GroupId | Long | The ID of the asset group. |
| Groups | List | The asset groups. For more information, see the following descriptions. |
| GroupId | Long | The ID of the asset group. |
| GroupIndex | Integer | The sequence number of the asset group. |
| GroupLevel | Integer | The level of the asset group. |
| GroupName | String | The name of the asset group. |
| GroupFather | Integer | The ID of the parent asset group. |
| GroupFlag | Integer | The type of the asset group. Valid values: 1: indicates a non-leaf node group that contains child asset groups. 0: indicates a leaf node group. |
| ChildGroups | List | The child asset groups. |

For more information about the error codes that this operation can return, see Error codes. Sample request

```
https://aegis.[ RegionId].example.com/?Action=DescribeGroupStruct &remark=x.x.x.x &tagIdList=123
```

Sample response (JSON format)

```json
    "Groups":[
            "groupIndex":2,
            "groupFather":0,
            "groupId":343,
            "groupName":"****",
            "groupLevel":1,
            "groupFlag":1,
            "childGroups":[]
```

`},`

```json
            "groupIndex":3,
            "groupFather":0,
            "groupId":345,
            "groupName":"****",
            "groupLevel":1,
            "groupFlag":1,
            "childGroups":[
                    "groupIndex":1,
                    "groupFather":345,
                    "groupId":346,
                    "groupName":"****",
                    "groupLevel":2,
                    "groupFlag":1,
                    "childGroups":[]
```

`]` `},`

```json
            "groupIndex":100,
            "groupFather":0,
            "groupId":336,
            "groupName":"****",
            "groupFlag":0,
            "childGroups":[]
```

`],`

```json
    "RequestId":"C4490A16-DDE4-4351-A366-57F9FCDC188F",
    "GroupFather":0,
    "GroupId":0
```

#### 4.2.3 DescribeAllEntity

You can call this operation to query information about all servers.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set this parameter to DescribeAllEntity. |
| GroupId | Long | No | The ID of the asset group. |
| Os | String | No | The operating system of the server. Valid values: win: indicates the Windows operating system. linux: indicates the Linux operating system. |

| Parameter | Type | Description |
|---|---|---|
| RequestId | String | The ID of the request. |
| Count | Integer | The number of returned records. |
| EntityList | Array | The servers. For more information, see the following descriptions. |
| GroupId | Integer | The ID of the asset group. |
| Uuid | String | The universally unique identifier (UUID) of the server. |
| InstanceName | String | The instance name of the server. |
| Ip | String | The IP address of the server. Note The public IP address of the server is displayed preferentially. If no public IP address is assigned to the server, the private IP address of the server is displayed. |

For more information about the error codes that this operation can return, see Error codes. Sample request

```
https://aegis.[ RegionId].example.com/?Action=DescribeAllEntity &GroupId=123 &Os=win
```

Sample response (JSON format)

```json
    "Count":2,
    "RequestId":"09D7C349-5306-4335-849A-10916F89E769",
    "EntityList":[
            "Uuid":"inet-00f20b1a-e2dd-408b-b38e-6a6e1ed5d818",
            "Ip":"x.x.x.x",
            "GroupId":336,
            "InstanceName":"****"
```

`},`

```
        ......
```

`]`

#### 4.2.4 DescribeEntityList

You can call this operation to query servers of a specified type. For example, you can query servers by security event type.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set this parameter to DescribeEntityList. |
| PageSize | Integer | No | The number of records to return on each page. Default value: 20. |
| CurrentPage | Integer | No | The number of the page to return. Default value: 1. |
| RegionNo | String | No | The ID of the region. |
| GroupId | Long | No | The ID of the asset group. |
| Os | String | No | The operating system of the server. Valid values: win: indicates the Windows operating system. linux: indicates the Linux operating system. |
| Account | String | No | Queries servers with unusual logons detected. Set this parameter to remoteLogin. |

| Health | String | No | Queries servers with baseline check issues detected. Set this parameter to exception. |
|---|---|---|---|
| Patch | String | No | Queries servers with vulnerabilities detected. Set this parameter to vul. |
| Suspicious | String | No | Queries servers with unusual events detected. Set this parameter to exception. |
| Trojan | String | No | Queries servers with webshells detected. Valid values: webshell: indicates trojan files. process: indicates trojan processes. |
| Status | String | No | The status of the Server Guard Agent. Valid values: offline: indicates that the Server Guard Agent is offline. pause: indicates that the Server Guard Agent is disabled. |
| TagIdList | String | No | The server tag ID. |

| Parameter | Type | Description |
|---|---|---|
| RequestId | String | The ID of the request. |
| CurrentPage | Integer | The number of the current page returned. |
| PageSize | Integer | The number of records returned on each page. |
| TotalCount | Integer | The number of returned records. |
| EntityList | Array | The servers. For more information, see the following descriptions. |
| AegisOnline | Boolean | Indicates whether the Server Guard Agent is online. |
| AegisVersion | String | The version of the Server Guard Agent. |
| BuyVersion | String | The version of the Server Guard package. |
| GroupId | Integer | The ID of the asset group. |
| ClientStatus | Boolean | Indicates whether the server is protected. A value of false indicates that the protection for the server is paused. |

| Flag | Integer | The type of the server. Valid values: 0: indicates an Alibaba Cloud ECS instance. 1: indicates an external server. |
|---|---|---|
| Uuid | String | The universally unique identifier (UUID) of the server. |
| InstanceName | String | The instance name of the server. |
| Os | String | The type of the operating system. |
| Region | String | The ID of the region. |
| Ip | String | The IP address of the server. Note The public IP address of the server is displayed preferentially. If no public IP address is assigned to the server, the private IP address of the server is displayed. |

For more information about the error codes that this operation can return, see Error codes. Sample request

```
https://aegis.[ RegionId].example.com/?Action=DescribeEntityList &Account=remoteLogin &CurrentPage=1 &GroupId=1 &Health=exception &Os=windows &PageSize=20 &Patch=vul &RegionNo=**** &Remark=x.x.x.x &Status=offline &Suspicious=exception &TagIdList=1,2,3 &Trojan=webshell
```

Sample response (JSON format)

```json
    "TotalCount":1,
    "PageSize":1,
    "RequestId":"8BFB5273-6582-446A-9E0B-BAC0A1A468EA",
    "CurrentPage":1,
    "EntityList":[
            "Uuid":"inet-00f20b1a-e2dd-408b-b38e-6a6e1ed5d818",
            "Os":"linux",
            "ClientStatus":false,
            "Ip":"x.x.x.x",
            "Region":"****",
            "Flag":0,
            "BuyVersion":"4",
            "GroupId":336,
            "InstanceName":"****"
```

`]`

#### 4.2.5 DescribeMachines

You can call this operation to query servers that match the specified criteria. For example, you can query all servers in an asset group.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set this parameter to DescribeMachines. |
| GroupId | Long | No | The ID of the asset group. |
| TagIdList | String | No | The server tag ID. |
| Mark | String | No | The IP address or instance name of the server. |

| Parameter | Type | Description |
|---|---|---|
| RequestId | String | The ID of the request. |
| Count | Integer | The number of returned records. |
| Machines | Array | The servers. For more information, see the following descriptions. |

| GroupId | Integer | The ID of the asset group. |
|---|---|---|
| InstanceName | String | The instance name of the server. |
| Os | String | The type of the operating system. |
| Ip | String | The IP address of the server. Note The public IP address of the server is displayed preferentially. If no public IP address is assigned to the server, the private IP address of the server is displayed. |
| Uuid | String | The universally unique identifier (UUID) of the server. |

For more information about the error codes that this operation can return, see Error codes. Sample request

```
https://aegis.[ RegionId].example.com/?Action=DescribeMachines &GroupId=123
```

Sample response (JSON format)

```json
    "Count":1,
    "Machines":[
            "groupId":336,
            "os":"linux",
            "instanceName":"****",
            "uuid":"inet-db626549-870c-4d3e-b0b5-4d8a5c7268a6",
            "ip":"192.168.x.x"
```

`],`

```json
    "RequestId":"C984123D-C8E0-4974-9CEE-ADD0596C46DB"
```

#### 4.2.6 DescribeMachineDetail

You can call this operation to query the detailed information about a specified server.

| Parameter | Type | Required | Description |
|---|---|---|---|

| Action | String | Yes | The operation that you want to perform. Set this parameter to DescribeMachineDetail. |
|---|---|---|---|
| Uuid | String | No | The universally unique identifier (UUID) of the server. |

| Parameter | Type | Description |
|---|---|---|
| RequestId | String | The ID of the request. |
| MachineDetail | Array | The detailed information about the server. For more information, see the following descriptions. |
| AegisOnline | Boolean | Indicates whether the Server Guard Agent is online. |
| AegisVersion | String | The version of the Server Guard Agent. |
| BuyVersion | String | The version of the Server Guard package. |
| GroupId | Integer | The ID of the asset group. |
| ClientStatus | Boolean | Indicates whether the server is protected. A value of false indicates that the protection for the server is paused. |
| Flag | Integer | The type of the server. Valid values: 0: indicates an Alibaba Cloud ECS instance. 1: indicates an external server. |
| GroupId | Long | The ID of the asset group. |
| GroupTrace | String | The full path of the asset group. |
| InstanceId | String | The instance ID of the server. |
| InstanceName | String | The instance name of the server. |
| Os | String | The type of the operating system. |
| Region | String | The ID of the region. |
| Ip | String | The IP address of the server. Note The public IP address of the server is displayed preferentially. If no public IP address is assigned to the server, the private IP address of the server is displayed. |
| IntranetIp | String | The private IP address of the server. |
| Uuid | String | The UUID of the server. |

| Tag | String | The server tag ID. |
|---|---|---|

For more information about the error codes that this operation can return, see Error codes. Sample request

```
https://aegis.[ RegionId].example.com/?Action=DescribeMachineDetail &Uuid=6dbdbfe7-06fa-4d9a-8268-ce2dc6d673ac
```

Sample response (JSON format)

```json
    "RequestId":"5D5D6F8F-6986-4996-9321-8EEA9FC048D1",
    "MachineDetail":{
        "Uuid":"inet-db626549-870c-4d3e-b0b5-4d8a5c7268a6",
        "Ip":"192.168.x.x",
        "GroupTrace":"Not grouped",
        "Os":"linux",
        "ClientStatus":true,
        "Region":"outside-of-aliyun",
        "Tag":"",
        "AegisOnline":false,
        "InstanceName":"****"
```

#### 4.2.7 DescribePropertyStatistic

You can call this operation to query the server statistics.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribePropertyStatistic. |
| Uuids | String | No | The UUID of the server. Separate multiple UUIDs with commas (,). |

| Name | Type | Description |
|---|---|---|

| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
|---|---|---|
| PropertyStatistics | Array | The list of server statistics. For more information, see the following parameter descriptions. |
| PortCount | String | The number of enabled ports. |
| PortGetDate | String | The port information update time. |
| ProcCount | String | The number of running processes. |
| ProcGetDate | String | The process information update time. |
| RootUserCount | String | The number of user accounts with root permission. |
| UserCount | String | The total number of user accounts. |
| UserGetDate | String | The user account information update time. |
| Uuid | String | The UUID of the server. |

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=DescribePropertyStatistic &Uuids=inet-00f20b1a-e2dd-408b-b38e-6a6e1ed5d818
```

Sample responses (JSON format)

```json
 "PropertyStatistics":[
   "UserGetDate":1514373155000,
   "Uuid":"inet-00f20b1a-e2dd-408b-b38e-6a6e1ed5d818",
   "RootUserCount":1,
   "UserCount":33,
   "ProcCount":89,
   "PortGetDate":1514115614000,
   "PortCount":6,
   "ProcGetDate":1514373133000
```

`],`

```json
 "RequestId":"C1CACE7E-E868-4E44-A52E-4CB1463B62BB"
```

#### 4.2.8 DescribePropertyPortItem

You can call this operation to obtain a list of listener ports on hosts.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribePropertyPortItem. |
| PageSize | Integer | No | The maximum number of records to be displayed on each page of the query output. Default value: 20. |
| CurrentPage | Integer | No | The current page number. Default value: 1. |
| Port | String | No | The port number. |
| ProcName | String | No | The process name. |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| TotalCount | Integer | The total number of returned records. |
| Count | Integer | The number of records on the current page. |
| CurrentPage | Integer | The current page number. |
| PageSize | Integer | The maximum number of records displayed on a page. |
| PropertyPortItems | Array | The list of listener ports on hosts. For more information, see the following parameter descriptions. |
| Count | Integer | The number of hosts that have enabled the specified port. |
| Port | String | The port number. |
| Proto | String | The network protocol, such as TCP or UDP. |

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=DescribePropertyPortItem &Port=22
```

Sample responses (JSON format)

```json
 "TotalCount":1,
 "PageSize":20,
 "RequestId":"9D38986A-F145-4FA8-AE1C-1DB1C2BDF4C0",
 "CurrentPage":1,
 "PropertyPortItems":[
   "Proto":"tcp",
   "Port":"22",
   "Count":2
```

`],`

```json
 "Count":1
```

#### 4.2.9 DescribePropertyPortDetail

You can call this operation to query detailed information about a listening port.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set this parameter to DescribePropertyPortDetail. |
| PageSize | Integer | No | The number of records to return on each page. Default value: 20. |
| CurrentPage | Integer | No | The number of the page to return. Default value: 1. |
| GroupId | Long | No | The ID of the asset group. |
| Ip | String | No | The IP address of the server. |
| Port | String | No | The port number. |

| Extend | String | No | Indicates whether fuzzy match is enabled to search for port numbers. Valid values: 1: indicates that fuzzy match is enabled. 0: indicates that fuzzy match is disabled. |
|---|---|---|---|
| ProcName | String | No | The name of the process. |
| Mark | String | No | The IP address or instance name of the server. Note Fuzzy match is supported. |
| TagIdListString | String | No | The server tag ID. |
| Uuid | String | No | The universally unique identifier (UUID) of the server. |

| Parameter | Type | Description |
|---|---|---|
| RequestId | String | The ID of the request. |
| TotalCount | Integer | The number of returned records. |
| Count | Integer | The number of records returned on the current page. |
| CurrentPage | Integer | The number of the current page returned. |
| PageSize | Integer | The number of records returned on each page. |
| PropertyPorts | Array | The information about the listening port. For more information, see the following descriptions. |
| BindIp | String | The IP address bound to the port. |
| Create | String | The time when the port was enabled. |
| InstanceName | String | The instance name of the server. |
| Ip | String | The IP address of the server. |
| Port | String | The port number. |
| ProcName | String | The name of the process. |
| Proto | String | The network protocol, such as TCP and UDP. |
| Uuid | String | The UUID of the server. |

For more information about the error codes that this operation can return, see Error codes. Sample request

```
https://aegis.[ RegionId].example.com/?Action=DescribePropertyPortDetail &Uuid=inet-f6ac9a93-0818-4052-90e2-d24f18ee198b
```

Sample response (JSON format)

```json
    "TotalCount":1,
    "PageSize":20,
    "RequestId":"D85484BB-4DC2-44EC-AD67-0B3765EC9213",
    "CurrentPage":1,
    "PropertyPorts":[
            "InstanceName":"****",
            "Uuid":"inet-f6ac9a93-0818-4052-90e2-d24f18ee198b",
            "Proto":"tcp",
            "Create":1514373168000,
            "Ip":"x.x.x.x",
            "Port":"22",
            "ProcName":"sshd",
            "BindIp":"0.0.0.0"
```

`],`

```json
    "Count":1
```

#### 4.2.10 DescribePropertyProcItem

You can call this operation to obtain a list of server processes.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribePropertyProcItem. |
| PageSize | Integer | No | The maximum number of records to be displayed on each page of the query output. Default value: 20. |

| CurrentPage | Integer | No | The current page number. Default value: 1. |
|---|---|---|---|
| Name | String | No | The process name. |
| User | String | No | The user who started the process. |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| TotalCount | Integer | The total number of returned records. |
| Count | Integer | The number of records on the current page. |
| CurrentPage | Integer | The current page number. |
| PageSize | Integer | The maximum number of records displayed on a page. |
| PropertyProcItems | Array | The list of server processes. For more information, see the following parameter descriptions. |
| Count | Integer | The number of servers on which the process is running. |
| Name | String | The process name. |

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=DescribePropertyProcItem &Name=init
```

Sample responses (JSON format)

```json
 "TotalCount":1,
 "PropertyProcItems":[
   "Count":2,
   "Name":"init"
```

`],`

```json
 "PageSize":20,
 "RequestId":"8BE95FB1-66B7-4509-AF82-3AA67368A5D8",
 "CurrentPage":1,
 "Count":1
```

#### 4.2.11 DescribePropertyProcDetail

You can call this operation to query server process details.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set this parameter to DescribePropertyProcDetail. |
| PageSize | Integer | No | The number of records to return on each page. Default value: 20. |
| CurrentPage | Integer | No | The number of the page to return. Default value: 1. |
| GroupId | Long | No | The ID of the asset group. |
| Ip | String | No | The IP address of the server. |
| Name | String | No | The name of the process. |
| Extend | String | No | Indicates whether fuzzy match is enabled to search for process names. Valid values: 1: indicates that fuzzy match is enabled. 0: indicates that fuzzy match is disabled. |
| User | String | No | The user who started the process. |

| Mark | String | No | The IP address or instance name of the server. Note Fuzzy match is supported. |
|---|---|---|---|
| Cmdline | String | No | The process parameter. |
| TagIdListString | String | No | The server tag ID. |
| Uuid | String | No | The universally unique identifier (UUID) of the server. |

| Parameter | Type | Description |
|---|---|---|
| RequestId | String | The ID of the request. |
| TotalCount | Integer | The number of returned records. |
| Count | Integer | The number of records returned on the current page. |
| CurrentPage | Integer | The number of the current page returned. |
| PageSize | Integer | The number of records returned on each page. |
| PropertyProcs | Array | The details of the server process. For more information, see the following descriptions. |
| Cmdline | String | The process parameter. |
| Create | String | The time when the information was reported. |
| EuidName | String | The permissions that the process has to access resources and files. |
| InstanceName | String | The instance name of the server. |
| Md5 | String | The MD5 value of the executable file. |
| Name | String | The name of the process. |
| Path | String | The path of the process. |
| Pid | String | The ID of the process. |
| ProcName | String | The name of the process. |
| Pname | String | The name of the parent process. |
| StartTime | String | The time when the process was started. |
| User | String | The user who started the process. |

| Uuid | String | The UUID of the server. |
|---|---|---|

For more information about the error codes that this operation can return, see Error codes. Sample request

```
https://aegis.[ RegionId].example.com/?Action=DescribePropertyProcDetail &Uuid=inet-00f20b1a-e2dd-408b-b38e-6a6e1ed5d818
```

Sample response (JSON format)

```json
    "PropertyProcs":[
            "InstanceName":"****",
            "Path":"/sbin/init",
            "Pname":"N/A",
            "Uuid":"inet-00f20b1a-e2dd-408b-b38e-6a6e1ed5d818",
            "User":"root",
            "Create":1514373133000,
            "StartTime":"2017-12-26 22:34:45",
            "Pid":"1",
            "EuidName":"root",
            "Cmdline":"/sbin/init",
            "Name":"init",
            "Md5":"70023aaf3f480d198d3b078d8c39****"
```

`],`

```json
    "TotalCount":1,
    "PageSize":20,
    "RequestId":"AB20A6D4-43EB-44E2-AD64-E03EAC1C14D9",
    "CurrentPage":1,
    "Count":1
```

#### 4.2.12 DescribePropertySoftwareItem

You can call this operation to query servers that have been installed with the specified application.

| Name | Type | Required | Description |
|---|---|---|---|

| Action | String | Yes | The operation that you want to perform. Set the value to DescribePropertySoftwareItem. |
|---|---|---|---|
| PageSize | Integer | No | The maximum number of records displayed on a page. Default value: 20. |
| CurrentPage | Integer | No | The current page number. Default value: 1. |
| Name | String | No | The name of the application. |
| Path | String | No | The application installation path. |
| SoftwareVersion | String | No | The version of the application. |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| TotalCount | Integer | The number of returned records. |
| Count | Integer | The number of records on the current page. |
| CurrentPage | Integer | The current page number. |
| PageSize | Integer | The maximum number of records displayed on a page. |
| PropertySoftwareItems | Array | A list of servers that have been installed with the application. For more information, see the following parameter descriptions. |
| Count | Integer | The number of servers that have been installed with the application. |
| Name | String | The name of the application. |

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=DescribePropertySoftwareItem &Name=spice-vdagent
```

Sample responses (JSON format)

```json
 "TotalCount":1,
 "PropertySoftwareItems":[
   "count":2,
   "Name":"spice-vdagent"
```

`],`

```json
 "PageSize":20,
 "RequestId":"0F2A3DEA-A5B3-4C2A-8BFC-4724A205E28B",
 "CurrentPage":1,
 "count": 1,
```

#### 4.2.13 DescribePropertySoftwareDetail

You can call this operation to query the details of software installed on a server.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set this parameter to DescribePropertySoftwareDetail. |
| PageSize | Integer | No | The number of records to return on each page. Default value: 20. |
| CurrentPage | Integer | No | The number of the page to return. Default value: 1. |
| Ip | String | No | The IP address of the server. |
| Name | String | No | The name of the software. |
| Extend | String | No | Indicates whether fuzzy match is enabled to search for software names.. Valid values: 1: indicates that fuzzy match is enabled. 0: indicates that fuzzy match is disabled. |
| Path | String | No | The installation path of the software. |

| Remark | String | No | The IP address or instance name of the server. Note Fuzzy match is supported. |
|---|---|---|---|
| SoftwareVersion | String | No | The version of the software. |
| Uuid | String | No | The universally unique identifier (UUID) of the server. |

| Parameter | Type | Description |
|---|---|---|
| RequestId | String | The ID of the request. |
| TotalCount | Integer | The number of returned records. |
| Count | Integer | The number of records returned on the current page. |
| CurrentPage | Integer | The number of the current page returned. |
| PageSize | Integer | The number of records returned on each page. |
| PropertySoftwares | Array | The details of software installed on the server. For more information, see the following descriptions. |
| Create | String | The time when the information was reported. |
| InstallTime | String | The time when the software was installed. |
| InstanceName | String | The instance name of the server. |
| Ip | String | The IP address of the server. |
| Path | String | The installation path of the software. |
| Version | String | The version of the software. |
| Uuid | String | The UUID of the server. |

For more information about the error codes that this operation can return, see Error codes. Sample request

```
https://aegis.[ RegionId].example.com/?Action=DescribePropertySoftwareDetail &Uuid=inet-00f20b1a-e2dd-408b-b38e-6a6e1ed5d818
```

Sample response (JSON format)

```json
    "TotalCount":1,
    "PropertySoftwares":[
            "InstanceName":"****",
            "Path":"/usr/libexec/gvfs-gphoto2-volume-monitor",
            "Uuid":"inet-00f20b1a-e2dd-408b-b38e-6a6e1ed5d818",
            "InstallTime":"2016-06-29 06:55:22",
            "Version":"1.4.3",
            "Create":1514172615000,
            "Ip":"x.x.x.x"
```

`],`

```json
    "PageSize":20,
    "RequestId":"31409246-AB88-4B36-A2B8-16D21BA9E170",
    "CurrentPage":1,
    "Count":1
```

#### 4.2.14 DescribePropertyUserItem

You can call this operation to query user account information.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribePropertyUserItem. |
| PageSize | Integer | No | The maximum number of records displayed on a page. Default value: 20. |
| CurrentPage | Integer | No | The current page number. Default value: 1. |
| User | String | No | The username of the account. |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| TotalCount | Integer | The number of returned records. |

| Count | Integer | The number of records on the current page. |
|---|---|---|
| CurrentPage | Integer | The current page number. |
| PageSize | Integer | The maximum number of records displayed on a page. |
| PropertyUserItems | Array | The returned user account information. For more information, see the following parameter descriptions. |
| Count | Integer | The number of servers under the account. |
| Name | String | The username of the account. |

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=DescribePropertyUserItem
```

Sample responses (JSON format)

```json
 "TotalCount":2,
 "PropertyUserItems":[
   "User":"abrt",
   "Count": 2
```

`},`

```json
   "User":"adm",
   "Count": 2
```

`],`

```json
 "PageSize":20,
 "RequestId":"E80981C2-AD12-4C60-9976-6927C1FE449B",
 "CurrentPage":1,
 "Count": 2
```

#### 4.2.15 DescribePropertyUserDetail

You can call this operation to query user account details.

| Parameter | Type | Required | Description |
|---|---|---|---|

| Action | String | Yes | The operation that you want to perform. Set this parameter to DescribePropertyUserDetail. |
|---|---|---|---|
| PageSize | Integer | No | The number of records to return on each page. Default value: 20. |
| CurrentPage | Integer | No | The number of the page to return. Default value: 1. |
| GroupId | Long | No | The ID of the asset group. |
| Ip | String | No | The IP address of the server. |
| IsRoot | String | No | Indicates whether the user account is a root account. Valid values: 1: indicates yes. 0: indicates no. |
| User | String | No | The name of the user account. |
| Extend | String | No | Indicates whether fuzzy match is enabled to search for user accounts. Valid values: 1: indicates that fuzzy match is enabled. 0: indicates that fuzzy match is disabled. |
| Mark | String | No | The IP address or instance name of the server. Note Fuzzy match is supported. |
| TagIdListString | String | No | The server tag ID. |
| Uuid | String | No | The universally unique identifier (UUID) of the server. |

| Parameter | Type | Description |
|---|---|---|
| RequestId | String | The ID of the request. |
| TotalCount | Integer | The number of returned records. |
| Count | Integer | The number of records returned on the current page. |
| CurrentPage | Integer | The number of the current page returned. |

| PageSize | Integer | The number of records returned on each page. |
|---|---|---|
| PropertyUsers | Array | The details of the user account. For more information, see the following descriptions. |
| AccountsExpirationDat e | String | The time when the user account expires. |
| Create | String | The time when the information was reported. |
| GroupName | String | The information about the user group. |
| InstanceName | String | The instance name of the server. |
| Ip | String | The IP address of the server. |
| IsRoot | String | Indicates whether the user account is a root account. |
| LastLoginIp | String | The last IP address that is used by the user account to log on to the server. |
| LastLoginTime | String | The last logon time of the user account. |
| PasswordExpirationDat e | String | The time when the password of the user account expires. |
| User | String | The name of the user account. |
| Uuid | String | The UUID of the server. |

For more information about the error codes that this operation can return, see Error codes. Sample request

```
https://aegis.[ RegionId].example.com/?Action=DescribePropertyUserDetail &Uuid=inet-00f20b1a-e2dd-408b-b38e-6a6e1ed5d818
```

Sample response (JSON format)

```json
    "TotalCount":66,
    "PageSize":2,
    "RequestId":"2EEAE2A6-1662-471C-A5E5-8A6190B01AFF",
    "CurrentPage":1,
    "Count":1,
    "PropertyUsers":[
            "GroupName":[
                "root"
```

`],`

```json
            "InstanceName":"****",
            "IsRoot":"1",
            "LastLoginTime":"2017-12-27 10:22:25",
            "Uuid":"inet-00f20b1a-e2dd-408b-b38e-6a6e1ed5d818",
            "User":"root",
            "LastLoginIp":"192.168.x.x",
            "Create":1514373155000,
            "Ip":"x.x.x.x",
            "AccountsExpirationDate":"never",
            "PasswordExpirationDate":"never"
```

`]`

#### 4.2.16 DescribeTopRiskyAssets

You can call this operation to query top N vulnerable servers.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set this parameter to DescribeTopRiskyAssets. |
| PageSize | Integer | No | The number of records to return, that is, the top N vulnerable servers. |

| Parameter | Type | Description |
|---|---|---|
| RequestId | String | The ID of the request. |
| TotalCount | Integer | The number of returned records. |

| TopRiskyAssets | Array | The top N vulnerable servers. For more information, see the following descriptions. |
|---|---|---|
| HcCount | String | The number of at-risk items detected in the baseline check. |
| Ip | String | The IP address of the server. |
| Uuid | String | The universally unique identifier (UUID) of the server. |
| VulCount | String | The number of detected vulnerabilities. |
| WarningCount | String | The number of detected security events. |

For more information about the error codes that this operation can return, see Error codes. Sample request

```
https://aegis.[ RegionId].example.com/?Action=DescribeTopRiskyAssets &PageSize=1
```

Sample response (JSON format)

```json
    "TotalCount": 1,
    "RequestId": "5D8D4058-2EE3-4599-9951-BDAA3340AD4D",
    "TopRiskyAssets": [
            "Ip": "192.168.x.x",
            "Uuid": "inet-dsljaoe-jjdsklaj****",
            "VulCount": 2,
            "HcCount": 1,
            "WarningCount": 2
```

`]`

### 4.3 Vulnerability management

#### 4.3.1 DescribeTarget

You can call this operation to query the servers that are checked for the specified type of risks in vulnerability management.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeTarget. |
| Type | String | No | The type of the risks. For example, vul represents vulnerabilities. |
| Config | String | No | The type of the vulnerabilities in JSON format. For example, {"vulType":"cve"} represents Linux software vulnerabilities. |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| TotalCount | Integer | The number of returned records. |
| Targets | Array | A list of servers that are checked for the specified type of risks. For more information, see the following parameter descriptions. |
| TargetType | String | Valid values: groupId: indicates the ID of an asset group. uuid: indicates the UUID of a server. |
| Target | String | The asset group ID or server UUID. |

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=DescribeTarget &Config={"vulType":"cve"} &Type=vul
```

Sample responses (JSON format)

```json
    "TotalCount":2,
    "RequestId":"1FF54D56-47ED-47FB-B4DB-2BDF3857D526",
    "Targets":[
            "Target":"inet-00f20b1a-e2dd-408b-b38e-6a6e1ed5d818",
            "TargetType":"uuid"
```

`},`

```json
            "Target":"336",
            "TargetType":"groupId"
```

`]`

#### 4.3.2 DescribeVulTargetStatistics

You can call this operation to query the information about target hosts for which vulnerability detection is enabled in the vulnerability management configuration.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeVulTargetStatistics. |
| Type | String | No | The vulnerability type. |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| CurrentPage | Integer | The current page number. |
| PageSize | Integer | The maximum number of records displayed on a page. |
| TotalCount | Integer | The total number of returned records. |
| TargetStats | Array | The list of target hosts for which vulnerability detection is enabled. For more information, see the following parameter descriptions. |
| VulType | String | The vulnerability type. |

| Targets | Array | The information about target hosts. For more information, see the following parameter descriptions. |
|---|---|---|
| Flag | String | Indicates whether vulnerability detection is enabled. |
| TargetType | String | The type of the Target parameter value. Valid values: groupId: indicates an asset group ID. uuid: indicates a host asset UUID. |
| Target | String | The asset group ID or host asset UUID. |

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=DescribeVulTargetStatistics &Type=cve
```

Sample responses (JSON format)

```json
 "TotalCount":1,
 "TargetStats":[
   "VulType":"cve","Targets":[]
```

`},`

```json
 "PageSize":10,
 "RequestId":"89DD84B4-B592-476C-A6C0-51D56B3E8EAC",
 "CurrentPage":1
```

#### 4.3.3 DescribeTargetConfig

You can call this operation to query the vulnerability scanning configuration information of a specified server.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeTargetConfig. |
| Type | String | No | The type of the vulnerability. |

| Uuid | String | No | The UUID of the server. |
|---|---|---|---|

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| TotalCount | Integer | The total number of the returned records. |
| TargetConfigs | Array | The list of vulnerability scanning configuration information. For more information, see the following parameter descriptions. |
| Type | String | The type of the vulnerability. |
| Config | String | Whether vulnerability scanning is enabled. Valid values: on and off. |
| OverAllConfig | String | Whether global vulnerability scanning is enabled. Valid values: on and off. Note The global vulnerability scanning configuration overrides the vulnerability scanning configuration for a single server. |

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=DescribeTargetConfig &Type=cve &Uuid=inet-00f20b1a-e2dd-408b-b38e-6a6e1ed5d818
```

Sample responses (JSON format)

```json
 "TotalCount":1,
 "RequestId":"092094BF-910F-4CE6-BE93-C3989B607977",
 "TargetConfigs":[
   "Config":"off",
   "Type":"cve",
   "OverAllConfig":"off"
```

`]`

#### 4.3.4 DescribeVulConfig

You can call this operation to query the global scanning configuration for each vulnerability type.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeVulConfig. |
| Type | String | No | The type of the vulnerability. |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| TotalCount | Integer | The total number of returned records. |
| TargetConfigs | Array | The list of global vulnerability scanning configurations. For more information, see the following parameter descriptions. |
| Type | String | The type of the vulnerability. |
| Config | String | The global scanning configuration for the vulnerability type. Valid values: on and off. |

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=DescribeVulConfig &Type=cve
```

Sample responses (JSON format)

```json
 "TotalCount":1,
 "RequestId":"A8E09216-31DF-45B6-A76B-E3F053752C07",
 "TargetConfigs":[
   "Config":"off",
   "Type":"cve"
```

#### 4.3.5 DescribeAutoDelConfig

You can call this operation to query the number of days that an invalid vulnerability is kept for before it is automatically deleted in the vulnerability management settings.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeAutoDelConfig. |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| Days | Integer | The number of days that an invalid vulnerability is kept for. |

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=DescribeAutoDelConfig
```

Sample responses (JSON format)

```json
 "RequestId":"E3785090-CFF4-4C53-82E4-08F902586053",
 "Days":7
```

#### 4.3.6 DescribeVulLevel

You can call this operation to query the vulnerability severities that require attention.

| Name | Type | Required | Description |
|---|---|---|---|

| Action | String | Yes | The operation that you want to perform. Set the value to DescribeVulLevel. |
|---|---|---|---|

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| ConcernLevels | List | The list of vulnerability severities that require attention. |

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=DescribeVulLevel
```

Sample responses (JSON format)

```json
 "RequestId":"7935CB7A-D1B7-4EE6-93D0-FF3D040CF19B",
 "ConcernLevels":["high","medium"]
```

#### 4.3.7 DescribeVulWhitelist

You can call this operation to obtain the whitelist of vulnerabilities.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeVulWhitelist. |
| PageSize | Integer | No | The maximum number of records to be displayed on each page of the query output. Default value: 20. |
| CurrentPage | Integer | No | The current page number. Default value: 1. |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| CurrentPage | Integer | The current page number. |
| PageSize | Integer | The maximum number of records displayed on a page. |
| TotalCount | Integer | The total number of returned records. |
| VulWhitelists | Array | The vulnerability whitelist. For more information, see the following parameter descriptions. |
| AliasName | String | The alias of the vulnerability. |
| Name | String | The name of the vulnerability. |
| Reason | String | The reason for adding the vulnerability to the whitelist. |
| Type | String | The vulnerability type. |

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=DescribeVulWhitelist &CurrentPage=1 &PageSize=20
```

Sample responses (JSON format)

```json
 "TotalCount":1,
 "VulWhitelists":[
   "Name":"oval:com.redhat.rhsa:def:20173263",
   "AliasName":"RHSA-2017:3263: curl security update",
   "Type":"cve",
   "Reason":"Not fixed at present"
```

`],`

```json
 "PageSize":3,
 "RequestId":"74F97EF7-B543-43FD-A4E9-18456731F9C5",
 "CurrentPage":1
```

#### 4.3.8 DescribeGroupedVul

You can call this operation to query information about the specified vulnerability group. The vulnerability management feature can display detected vulnerability records by group. A vulnerability group contains all servers with a specific vulnerability detected by Server Guard.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeGroupedVul. |
| PageSize | Integer | No | The maximum number of records to be displayed on each page of the query output. Default value: 20. |
| CurrentPage | Integer | No | The current page number. Default value: 1. |
| Dealed | String | No | Indicates whether the vulnerability has been handled. Valid values: Y: indicates that the vulnerability has been handled. N: indicates that the vulnerability has not been handled. |
| Direction | String | No | The sorting mode of vulnerabilities in the vulnerability group. Valid values: asc: indicates sorting in ascending order. desc: indicates sorting in descending order. |
| LastTsEnd | Long | No | The end time of the last detection of the vulnerability. |
| LastTsStart | Long | No | The start time of the last detection of the vulnerability. |
| Level | String | No | The severity of the vulnerability. Valid values: serious: critical high: important medium: moderate low: low |
| Name | String | No | The name of the vulnerability. |

| Necessity | String | No | The necessity for fixing the vulnerability. Valid values: asap: indicates that the vulnerability must be fixed as soon as possible. later: indicates that the vulnerability can be fixed later. nntf: indicates that the vulnerability can be ignored. |
|---|---|---|---|
| OrderBy | String | No | The field based on which the vulnerabilities in the vulnerability group are sorted. You can specify other request parameters for sorting order. |
| PatchId | Long | No | The ID of the patch used to fix the vulnerability. |
| Product | String | No | The product where the vulnerability exists. |

| StatusList | String | No | The status of the vulnerability. Valid values: 1: indicates that the vulnerability has not been fixed. 2: indicates that the vulnerability fix failed. 3: indicates that the server has failed to be rolled back to the version before the vulnerability fix. 4: indicates that the vulnerability is being fixed. 5: indicates that the server is being rolled back to the version before the vulnerability fix. 6: indicates that the vulnerability fix is being verified. 7: indicates that the vulnerability has been fixed successfully. 8: indicates that the vulnerability has been fixed successfully, and that the server is waiting for restart. 9: indicates that the server has been rolled back to the version before the vulnerability fix. 10: indicates that the vulnerability has been ignored. 11: indicates that the server has been rolled back to the version before the vulnerability fix, and that the server is waiting for restart. 12: indicates that the vulnerability does not exist. 20: indicates that the vulnerability is invalid. Note The statuses are specified in a single parameter, separated with commas (,). |
|---|---|---|---|
| Type | String | No | The type of the vulnerability. |
| Uuids | String | No | The UUID of the server. Separate multiple UUIDs with commas (,). |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| CurrentPage | Integer | The current page number. |

| PageSize | Integer | The maximum number of records displayed on a page. |
|---|---|---|
| TotalCount | Integer | The total number of returned records. |
| GroupedVulItems | Array | The information about the vulnerability group. For more information, see the following parameter descriptions. |
| AliasName | String | The alias of the vulnerability. |
| AsapCount | Integer | The number of assets to be fixed as soon as possible. |
| Count | Integer | The total number of vulnerabilities. |
| GmtLast | Long | The last time when the vulnerability was detected. |
| HandledCount | Integer | The total number of vulnerabilities handled. |
| Level | String | The severity of the vulnerability. |
| Name | String | The name of the vulnerability. |
| PendingCount | Integer | The number of vulnerabilities that have not been handled. |
| Product | String | The product affected by the vulnerability. |
| Status | Integer | The status of the vulnerability. |
| TotalCount | Integer | The total number of vulnerabilities. |
| Type | String | The type of the vulnerability. |

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=DescribeGroupedVul &CurrentPage=1 &Dealed=y &Direction=asc &LastTsEnd=1517414400000 &LastTsStart=1517414500000 &Level=high &Name=oval:com.redhat.rhsa:def:20170817 &Necessity=asap &OrderBy=name &PageSize=20 &PatchId=27001 &Product=redhat &SourceIp= &StatusList=1,2 &Type=cve &Uuids=46ef7c05-0c53-486c-b446-ef6ff972551c,b688bf9f-1fd9-42c8-bb34-28697f562dc5
```

Sample responses (JSON format)

```json
 "GroupedVulItems":[
   "Name":"oval:com.redhat.rhsa:def:20170817",
   "Status":7,
   "Count":0,
   "TotalCount":1,
   "PendingCount":0,
   "AliasName":"RHSA-2017:0817: kernel security, bug fix, and enhancement update",
   "AsapCount":0,
   "Type":"cve",
   "GmtLast":1513695612000,
   "Level":"high",
   "HandledCount":1
```

`},` `],`

```json
 "TotalCount":1,
 "PageSize":10,
 "RequestId":"6FCF95BE-7A78-4AD8-811C-BF12FC34AC34",
 "CurrentPage":1
```

#### 4.3.9 DescribeVulList

You can call this operation to obtain the vulnerability list of the specified host asset.

| Name | Type | Required | Description |
|---|---|---|---|

| Action | String | Yes | The operation that you want to perform. Set the value to DescribeVulList. |
|---|---|---|---|
| PageSize | Integer | No | The maximum number of records to be displayed on each page of the query output. Default value: 20. |
| CurrentPage | Integer | No | The current page number. Default value: 1. |
| Dealed | String | No | Indicates whether the vulnerability has been handled. Valid values: Y: indicates that the vulnerability has been handled. N: indicates that the vulnerability has not been handled. |
| Level | String | No | The severity of the vulnerability. Valid values: serious: critical high: important medium: moderate low: low |
| Name | String | No | The name of the vulnerability. |
| Necessity | String | No | The necessity for fixing the vulnerability. Valid values: asap: indicates that the vulnerability must be fixed as soon as possible. later: indicates that the vulnerability can be fixed later. nntf: indicates that the vulnerability can be ignored. |
| Type | String | No | The type of the vulnerability. |

| StatusList | String | No | The status of the vulnerability. Valid values: 1: indicates that the vulnerability has not been fixed. 2: indicates that the vulnerability fix failed. 3: indicates that the host has failed to be rolled back to the version before the vulnerability fix. 4: indicates that the vulnerability is being fixed. 5: indicates that the host is being rolled back to the version before the vulnerability fix. 6: indicates that the vulnerability fix is being verified. 7: indicates that the vulnerability has been fixed successfully. 8: indicates that the vulnerability has been fixed successfully, and that the host is waiting for restart. 9: indicates that the host has been rolled back to the version before the vulnerability fix. 10: indicates that the vulnerability has been ignored. 11: indicates that the host has been rolled back to the version before the vulnerability fix, and that the host is waiting for restart. 12: indicates that the vulnerability does not exist. 20: indicates that the vulnerability is invalid. Note Note: The statuses are specified in a single parameter, separated with commas (,). |
|---|---|---|---|
| Uuids | String | No | The UUID of the host asset. Separate multiple host asset UUIDs with commas (,). |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| CurrentPage | Integer | The current page number. |
| PageSize | Integer | The maximum number of records displayed on a page. |

| TotalCount | Integer | The total number of records returned from the query. |
|---|---|---|
| VulRecords | Array | The list of vulnerabilities. For more information, see the following parameter descriptions. |
| AliasName | String | The alias of the vulnerability. |
| ExtendContent | String | The extended information of the vulnerability. |
| ExtendContentJson | String | The extended information of the vulnerability (JSON format). |
| FirstTs | Long | The first time when the vulnerability was detected. |
| ModifyTs | Long | The last time when the vulnerability was updated. |
| LastTs | Long | The last time when the vulnerability was detected. |
| Level | String | The severity of the vulnerability. |
| Name | String | The name of the vulnerability. |
| Necessity | String | The necessity for fixing the vulnerability. Valid values: asap: indicates that the vulnerability must be fixed as soon as possible. later: indicates that the vulnerability can be fixed later. nntf: indicates that the vulnerability can be ignored. |
| PrimaryId | Long | The ID of the primary key. |
| Product | String | The product affected by the vulnerability. |
| RecordId | Long | The ID of the vulnerability record. |
| Related | String | The CVE ID of the vulnerability. |
| RepairTs | Long | The time when the vulnerability was fixed. |
| ResultCode | String | The code of the vulnerability handling result. |
| ResultMessage | String | The message of the vulnerability handling result. |
| RiskDesc | String | The risk description of the vulnerability. |
| RiskLevel | Integer | The risk level of the vulnerability. |

| Status | Integer | The status of the vulnerability. Valid values: 1: indicates that the vulnerability is to be handled. 2: indicates that the vulnerability has been ignored. 3: indicates that the vulnerability has been confirmed. 8: indicates that the vulnerability has been marked as a false positive. 16: indicates that the vulnerability is being handled. 32: indicates that the vulnerability has been handled. |
|---|---|---|
| Tag | String | The tag of the vulnerability. |
| Type | String | The type of the vulnerability. |
| Uuid | String | The UUID of the host asset. |

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=DescribeVulList &CurrentPage=1 &Dealed=n &Level=serious &Name=RHSA-2017:1100: nss and nss-util security update &Necessity=asap &PageSize=20 &StatusList=1 &Type=cve &Uuids=f293ade2-e5b1-4cc0-99a6-cc993a4158cc
```

Sample responses (JSON format)

```json
 "TotalCount":1,
 "PageSize":20,
 "RequestId":"2E35F7F7-DA6D-46A5-BA9D-8751BDAE7710",
 "CurrentPage":1,
 "VulRecords":[
   "Uuid":"b688bf9f-1fd9-42c8-bb34-28697f562dc5",
   "Necessity":"nntf",
   "ModifyTs":1512949391000,
   "Type":"cve",
   "FirstTs":1499321694000,
   "Related":"CVE-2016-1248",
   "ExtendContentJson":{"Necessity":
{"Cvss_factor":"6.8","Total_score":"6.799999965526585","Status":"normal","Enviroment_fa or":"1.0","Time_factor":"0.9999999949303802","Assets_factor":"1","Gmt_create":"20171210 "Is_calc":"1"},"Os":"centos","cveList":["CVE-2016-1248"],"RpmEntityList": [{"Name":"vim-minimal","Version":"7.4.160","FullVersion":"7.4.160- 1.el7","MatchDetail":"vim-minimal version less than 2:7.4.160- 1.el7_3.1","UpdateCmd":"yum update vimminimal","Path":"/etc/virc"}],"OsRelease":"7"},
   "Name":"oval:com.redhat.rhsa:def:20162972",
   "Status":1,
   "LastTs":1512949391000,
   "AliasName":"RHSA-2016:2972: vim security update (Moderate)",
   "Tag":"oval",
   "PrimaryId":281156,
   "Level":"high"
```

`]`

#### 4.3.10 DescribeVulDetails

You can call this operation to query detailed information about a vulnerability.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeVulDetails. |
| Type | Integer | Yes | The type of the vulnerability. |
| Name | String | Yes | The name of the vulnerability. |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| Cves | Array | The vulnerability details. For more information, see the following parameter descriptions. |
| Classify | String | The vulnerability type code. |
| Classifys | Array | The detailed vulnerability information. For more information, see the following parameter descriptions. |
| Classify | String | The vulnerability type code. |
| Description | String | The description of the vulnerability type. |
| DemoVideoUrl | String | The URL of the vulnerability video demo. |
| CnvdId | String | The CNVD ID. |
| Complexity | String | The complexity. |
| Content | String | The vulnerability details. |
| ExtendContentJson | String | The additional information about the vulnerability (JSON format). |
| CveId | String | The CVE ID. |
| CvssScore | String | The CVSS score. |
| CvssVector | String | The CVSS score string. |
| OtherId | String | The ID of the vulnerability. |
| Poc | String | The proof of concept (POC) method. |
| PocCreateTime | Long | The time when the POC method was created. |
| PocDisclosureTime | Long | The time when the POC method was revealed. |
| Service | String | The products that are affected by the vulnerability. |
| Reference | String | The corresponding reference. |
| ReleaseTime | Long | The time when the vulnerability was revealed. |
| Solution | String | The solution for fixing the vulnerability. |
| Summary | String | The vulnerability summary. |
| Title | String | The title of the vulnerability. |
| Vendor | String | The vendors that are affected by the vulnerability. |

| VulLevel | String | The severity level of the vulnerability. |
|---|---|---|

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=DescribeVulDetails &Name=oval:com.redhat.rhsa:def:20170036 &Type=cve
```

Sample responses (JSON format)

```json
 "Cves": [{
  "CvssVector": "CVSS:3.0/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H",
  "OtherId": "CVE-2016-7117",
  "Classifys": [],
  "Vendor": "Linux",
  "CvssScore": "10.0",
  "CnvdId": "CNVD-2016-09362",
  "Reference": "http://www.securityfocus.com/bid/93304",
  "Solution": "<p>The vendor has released a patch to fix this vulnerability. Download
the patch from: \n<br />https://bugzilla.redhat.com/show_bug.cgi?id=1382268</p>\n",
  "CveId": "CVE-2016-7117",
  "ReleaseTime": 1476028800000,
  "VulLevel": "serious",
  "Title": "The use-after-free vulnerability in __sys_recvmmsg function in the Linux
kernel",
  "Summary": "The Linux kernel is released by the Linux Foundation of the United Stat
es for Linux operating systems. The use-after-free vulnerability is found in the net/ socket.c file in \n\nLinux kernel 4.5.2 and earlier versions. It allows remote attack ers to execute arbitrary code."
 }],
 "RequestId": "70DEE6B7-A167-4B5D-ADAA-3631443D5190"
```

#### 4.3.11 DescribeVulNumStatistics

You can call this operation to query vulnerability statistics.

| Name | Type | Required | Description |
|---|---|---|---|

| Action | String | Yes | The operation that you want to perform. Set the value to DescribeVulNumStatistics. |
|---|---|---|---|
| StartTs | Long | No | The start time for statistics collection. |
| EndTs | Long | No | The end time for statistics collection. |
| Uuids | String | No | The UUID of the server. Separate multiple UUIDs with commas (,). |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| CmsDealedTotalNum | Integer | The number of CMS vulnerabilities handled. |
| CmsNum | Integer | The number of CMS vulnerabilities. |
| CveNum | Integer | The number of CVE vulnerabilities. |
| EmgNum | Integer | The number of other vulnerabilities. |
| SysNum | Integer | The number of Windows OS vulnerabilities. |
| VulAsapSum | Integer | The number of vulnerabilities that need to be handled as soon as possible. |
| VulDealedTotalNum | Integer | The total number of vulnerabilities handled. |
| VulSeriousTotal | Integer | The total number of critical vulnerabilities. |
| VulHighTotal | Integer | The total number of important vulnerabilities. |
| VulMediumTotal | Integer | The total number of moderate vulnerabilities. |
| VulLowTotal | Integer | The total number of low vulnerabilities. |
| VulLaterSum | Integer | The number of vulnerabilities that can be handled later. |
| VulNntfSum | Integer | The number of vulnerabilities that do not need to be fixed temporarily. |

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=DescribeVulNumStatistics &EndTs=1514736000000 &StartTs=1514736000000 &Uuids=46ef7c05-0c53-486c-b446-ef6ff972551c
```

Sample responses (JSON format)

```json
    "VulHighTotal":0,
    "CveNum":1,
    "VulMediumTotal":0,
    "EmgNum":0,
    "VulLowTotal":0,
    "VulNntfSum":1,
    "VulAsapSum":0,
    "SysNum":0,
    "VulDealedTotalNum":1,
    "RequestId":"093C121C-2981-4E69-8309-CD1BDD8C872A",
    "CmsNum":0,
    "VulSeriousTotal":0,
    "CmsDealedTotalNum":0,
    "VulLaterSum":0
```

#### 4.3.12 DescribeVulLevelStatistics

You can call this operation to obtain the statistics on vulnerabilities by vulnerability severity.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeVulLevelStatistics. |
| StartTs | Long | No | The start time of the time frame specified for query. |
| EndTs | Long | No | The end time of the time frame specified for query. |
| Uuids | String | No | The UUID of the server. Separate multiple UUIDs with commas (,). |

| Name | Type | Description |
|---|---|---|

| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
|---|---|---|
| TotalCount | Integer | The total number of returned records. |
| LevelStatistics | Array | The vulnerability statistics. For more information, see the following parameter descriptions. |
| CmsDealedTotalNum | Integer | The number of handled CMS vulnerabilities. |
| CmsNum | Integer | The number of CMS vulnerabilities. |
| CveNum | Integer | The number of CVE vulnerabilities. |
| EmgNum | Integer | The number of other vulnerabilities. |
| Level | String | The severity of the vulnerability. |
| SysNum | Integer | The number of Windows vulnerabilities. |
| VulAsapSum | Integer | The number of high-priority vulnerabilities. |
| VulDealedTotalNum | Integer | The total number of handled vulnerabilities. |
| VulSeriousTotal | Integer | The total number of critical-risk vulnerabilities. |
| VulHighTotal | Integer | The total number of important-risk vulnerabilities. |
| VulMediumTotal | Integer | The total number of moderate-risk vulnerabilities. |
| VulLowTotal | Integer | The total number of low-risk vulnerabilities. |
| VulLaterSum | Integer | The number of medium-priority vulnerabilities. |
| VulNntfSum | Integer | The number of low-priority vulnerabilities. |

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=DescribeVulLevelStatistics &EndTs=1514736000000 &StartTs=1514736000000 &Uuids=46ef7c05-0c53-486c-b446-ef6ff972551c,b688bf9f-1fd9-42c8-bb34-28697f562dc5
```

Sample responses (JSON format)

```json
 "TotalCount":0,
 "LevelStatistics":[
   "VulHighTotal":0,
   "CveNum":0,
   "VulMediumTotal":0,
   "EmgNum":0,
   "VulLowTotal":0,
   "VulNntfSum":0,
   "VulAsapSum":0,
   "SysNum":0,
   "VulDealedTotalNum":0,
   "CmsNum":0,
   "Level":"high",
   "VulSeriousTotal":0,
   "CmsDealedTotalNum":0,
   "VulLaterSum":0
```

`},`

```json
   "VulHighTotal":0,
   "CveNum":0,
   "VulMediumTotal":0,
   "EmgNum":0,
   "VulLowTotal":0,
   "VulNntfSum":0,
   "VulAsapSum":0,
   "SysNum":0,
   "VulDealedTotalNum":0,
   "CmsNum":0,
   "Level":"low",
   "VulSeriousTotal":0,
   "CmsDealedTotalNum":0,
   "VulLaterSum":0
```

`],`

```json
 "RequestId":"9B062D3F-AD5A-4D3E-9A7A-45CAC2713FC0"
```

#### 4.3.13 DescribeVulMachineList

You can call this operation to query the vulnerability statistics of a specified server.

| Name | Type | Required | Description |
|---|---|---|---|

| Action | String | Yes | The operation that you want to perform. Set the value to DescribeVulMachineList. |
|---|---|---|---|
| StartTs | Long | No | The start time of the time frame during which the statistics were collected. |
| EndTs | Long | No | The end time of the time frame during which the statistics were collected. |
| Uuids | String | No | The UUID of the server. Separate multiple UUIDs with commas (,). |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| TotalCount | Integer | The total number of the returned records. |
| MachineStatistics | Array | The vulnerability statistics. For more information, see the following parameter descriptions. |
| CmsDealedTotalNum | Integer | The number of CMS vulnerabilities that have been handled. |
| CmsNum | Integer | The number of CMS vulnerabilities. |
| CveNum | Integer | The number of CVE vulnerabilities. |
| EmgNum | Integer | The number of other vulnerabilities. |
| SysNum | Integer | The number of Windows vulnerabilities. |
| VulAsapSum | Integer | The number of high-priority vulnerabilities. |
| VulDealedTotalNum | Integer | The total number of vulnerabilities that have been handled. |
| VulSeriousTotal | Integer | The total number of critical-risk vulnerabilities. |
| VulHighTotal | Integer | The total number of important-risk vulnerabilities. |
| VulMediumTotal | Integer | The total number of moderate-risk vulnerabilities. |
| VulLowTotal | Integer | The total number of low-risk vulnerabilities. |
| VulLaterSum | Integer | The number of medium-priority vulnerabilities. |
| VulNntfSum | Integer | The number of low-priority vulnerabilities. |
| Uuid | String | The UUID of the server. |

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=DescribeVulMachineList &EndTs=1514736000000 &StartTs=1514736000000 &Uuids=46ef7c05-0c53-486c-b446-ef6ff972551c
```

Sample responses (JSON format)

```json
 "TotalCount":0,
 "MachineStatistics":[
   "Uuid":"577f9886-bf66-4c3c-88ac-28c938cb527b",
   "VulHighTotal":0,
   "CveNum":1,
   "VulMediumTotal":0,
   "EmgNum":0,
   "VulLowTotal":0,
   "VulNntfSum":0,
   "VulAsapSum":0,
   "SysNum":0,
   "VulDealedTotalNum":0,
   "CmsNum":0,
   "VulSeriousTotal":0,
   "CmsDealedTotalNum":0,
   "VulLaterSum":0
```

`],`

```json
 "RequestId":"A3F8BE63-9BA1-450D-BB5D-CE9205E6645D"
```

### 4.4 Baseline check

#### 4.4.1 DescribeStratetyDetail

You can call this operation to query the details of a specified baseline check policy.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeStratetyDetail. |

| Id | String | No | The ID of the baseline check policy. |
|---|---|---|---|

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| Strategy | Array | The details of the baseline check policy. For more information, see the following parameter descriptions. |
| CycleDays | Integer | The cycle of policy execution. |
| CycleStartTime | Integer | The start time of policy execution. Valid values: 0: indicates the period from 00:00 to 06:00. 6: indicates the period from 06:00 to 12:00. 12: indicates the period from 12:00 to 18:00. 18: indicates the period from 18:00 to 24:00. |
| Id | Integer | The ID of the policy. |
| Name | String | The name of the policy. |
| Type | Integer | The type of the policy. Valid values: 1: indicates a system default policy. 2: indicates a custom policy. |
| RiskTypeWhiteListQue ryResultList | Array | The risk information contained in the policy. For more information, see the following parameter descriptions. |
| Alias | String | The name of the risk category. |
| On | Boolean | Indicates whether to check for risks of the specified category. |
| TypeName | String | The code of the risk category. |
| SubTypes | Array | The list of risk subcategories. For more information, see the following parameter descriptions. |
| Alias | String | The name of the risk subcategory. |
| TypeName | String | The code of the risk subcategory. |
| On | Boolean | Indicates whether to check for risks of the specified subcategory. |

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=DescribeStratetyDetail &Id=1
```

Sample responses (JSON format)

```json
     "RequestId": "99F17C4B-2E23-4B41-BBEB-C03963B06EB4",
     "Strategy": {
  "Name": "Yunwu testing",
             "CycleDays": 1,
             "CycleStartTime": 18,
             "Type": 2,
             "Id": 12,
             "RiskTypeWhiteListQueryResultList": [
                     "On": false,
                     "Alias": "Compliance with Security Standards",
                     "TypeName": "cis",
                     "SubTypes": [
                              "On": true,
                              "Alias": "Memcached",
                              "TypeName": "memcached-check"
```

`},`

```json
                              "On": true,
                              "Alias": "CentOS 7",
                              "TypeName": "centos7"
```

`},`

```json
                              "On": false,
                              "Alias": "Tomcat 7",
                              "TypeName": "tomcat7"
```

`},`

```json
                              "On": false,
                              "Alias": "MongoDB",
                              "TypeName": "mongodb-check"
```

`]` `]`

#### 4.4.2 DescribeStrategyTarget

You can call this operation to query the information about asset groups to which a specified baseline check policy applies.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeStrategyTarget. |
| Config | String | No | The policy configuration information. The baseline check policy ID is specified in JSON format, for example, {"strategyId":15161} . |
| Type | String | No | The configuration type. Set the value to hc strategy. _ |
| Target | String | No | The ID of the asset group to which the baseline check policy applies. |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| Count | Integer | The total number of returned records. |
| StrategyTargets | Array | The information about asset groups to which the policy applies. For more information, see the following parameter descriptions. |
| Flag | String | Indicates whether the policy applies to the specified asset group. Valid values: add: indicates the whitelist mode, that is, the policy applies to the asset group. del: indicates the blacklist mode, that is, the policy does not apply to the asset group. Note Generally, the blacklist mode is used for system default policies, and the whitelist mode is used for custom policies. |
| TargetType | String | The return value is fixed to groupId, indicating that the value of the Target parameter is the ID of the asset group. |
| Target | String | The asset group ID. |

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=DescribeStrategyTarget &Config={"strategyId":15161} &Type=hc_strategy
```

Sample responses (JSON format)

```json
        "Count": 1,
        "StrategyTargets":[
                "Flag": "del",
                "Target": "281801",
                "TargetType": "groupId"
```

`]`

```json
 "requestId": "B44F545D-15CF-4A57-B8BF-4340D15D0507"
```

#### 4.4.3 DescribeUuidConfig

You can call this operation to check whether baseline check is enabled for a specified server.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeUuidConfig. |
| Uuid | String | No | The UUID of the server. |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| Data | Struct | The baseline check configuration. For more information, see the following parameter descriptions. |
| Flag | String | Indicates whether baseline check is enabled. Valid values: add: indicates enabled. del: indicates disabled. |

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=DescribeUuidConfig &uuid=4bc19998-e100-4b04-ab11-1e677418d311
```

Sample responses (JSON format)

```json
    "Data": {
        "Flag": "del"
```

`},`

```json
    "RequestId": "A89978FE-BC35-427E-A4B1-7AEEAE741CC2",
```

#### 4.4.4 DescribeUserSetting

You can call this operation to query the number of days an invalid risk is kept for before it is automatically deleted in baseline check.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeUserSetting. |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| InvalidWarningKeepDa ys | Integer | The number of days that an invalid risk is kept for. |

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=DescribeUserSetting
```

Sample responses (JSON format)

```json
 "InvalidWarningKeepDays":90,
 "RequestId":"0A079FE2-0D1B-4A4D-A4EF-D02B5DDE12A7"
```

#### 4.4.5 DescribeRiskWhiteList

You can call this operation to obtain the whitelist of risk items that are exempt from the baseline check.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeRiskWhiteList. |
| PageSize | Integer | No | The maximum number of records to be displayed on each page of the query output. Default value: 20. |
| CurrentPage | Integer | No | The current page number. Default value: 1. |
| RiskName | String | No | The name of the risk item. This parameter supports fuzzy match. |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| TotalCount | Integer | The total number of returned records. |
| Count | Integer | The number of records on the current page. |
| CurrentPage | Integer | The current page number. |
| PageSize | Integer | The maximum number of records displayed on a page. |
| WhiteLists | Array | The risk item whitelist. For more information, see the following parameter descriptions. |
| Reason | String | The reason for adding the risk item to the whitelist. |
| RiskId | Long | The ID of the risk item. |

| RiskName | String | The name of the risk item. |
|---|---|---|

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=DescribeRiskWhiteList &RiskName=SSH logon baseline check
```

Sample responses (JSON format)

```json
 "TotalCount":1,
 "PageSize":20,
 "RequestId":"B452E97A-7DFA-44FC-915D-5D590A702846",
 "CurrentPage":1,
 "WhiteLists":[
   "RiskName":"SSH logon baseline check",
   "RiskId":1
```

`],`

```json
 "Count":1
```

#### 4.4.6 DescribeStratety

You can call this operation to query the execution details of a specified baseline check policy.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeStratety. |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| Strategies | Array | The list of baseline check policies. For more information, see the following parameter descriptions. |

| CycleDays | Integer | The execution cycle of the policy. |
|---|---|---|
| CycleStartTime | Integer | The start time of policy execution. |
| EcsCount | Integer | The number of hosts to which the policy applies. |
| ExecStatus | Integer | The current execution status of the policy. Valid values: 1: indicates that the policy has been executed. 2: indicates that the policy is being executed. |
| Id | Integer | The ID of the policy. |
| Name | String | The name of the policy. |
| ProcessRate | Integer | The progress of policy execution. Unit: percentage. |
| RiskCount | Integer | The number of risk items contained in the policy. |
| ConfigTargets | Array | The asset group to which the policy applies. For more information, see the following parameter descriptions. |
| Flag | String | Indicates whether the policy applies to the specified asset group. Valid values: add: indicates the whitelist mode, that is, the policy applies to the asset group. del: indicates the blacklist mode, that is, the policy does not apply to the asset group. Note Generally, the blacklist mode is used for system default policies, and the whitelist mode is used for custom policies. |
| TargetType | String | The return value is fixed to groupId, indicating that the value of the Target parameter is the ID of the asset group. |
| Target | String | The asset group ID. |

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=DescribeStratety
```

Sample responses (JSON format)

```json
        "requestId": "751BEDD8-A16F-49CE-A3C4-605849645D79",
    "Strategies": [
                "Name": "Threat Detection Service No. 12345",
                "RiskCount": 4,
                "CycleDays": 1,
                "CycleStartTime": 6,
                "Type": 2,
                "ProcessRate": 0,
                "ConfigTargets": [
                        "Flag": "add",
                        "Target": "5078483",
                        "TargetType": "groupId"
```

`],`

```json
                "Id": 36071,
                "ExecStatus": 1,
                "EcsCount": 2
```

`]`

#### 4.4.7 DescribeStrategyExecDetail

You can call this operation to query the execution details of a baseline check policy.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeStrategyExecDetail. |
| StrategyId | Integer | No | The ID of the baseline check policy. |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| EndTime | String | The time when the baseline check was complete. |
| FailCount | Integer | The number of servers that failed to pass the check. |

| FailedEcsList | Array | A list of servers that failed to pass the check. For more information, see the following parameter descriptions. |
|---|---|---|
| Ip | String | The IP address of the server. |
| InstanceName | String | The instance name of the server. |
| IntranetIp | String | The private IP address of the server. |
| Reason | String | The reason that causes the baseline check failure. |
| InProcessCount | Integer | The number of servers that are being checked. |
| percent | String | The baseline check progress in percentage. |
| Source | String | The baseline check mode: automatic or manual. |
| StartTime | String | The time when the baseline check started. |
| SuccessCount | Integer | The number of servers that have passed the check. |

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=DescribeStrategyExecDetail &StrategyId=1
```

Sample responses (JSON format)

```json
     "requestId": "751BEDD8-A16F-49CE-A3C4-605849645D79",
       "Source": "Schedule",
       "InProcessCount": 0,
       "SuccessCount": 1,
       "Percent": 100,
       "EndTime": "2018-04-08 12:15:20",
       "FailedEcsList": [],
       "StartTime": "2018-04-08 12:15:10",
       "FailCount": 0,
```

#### 4.4.8 DescribeRiskType

You can call this operation to query all types of risks detected in baseline check and view the number of risks that have been detected by a baseline check policy or on the specified servers for a specific risk type.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeRiskType. |
| StrategyId | Long | No | The ID of the baseline check policy. |
| Uuids | String | No | The UUID of the server. Multiple UUIDs are separated with commas (,). |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| Count | Integer | The number of risk types. |
| RiskTypes | Array | A list of risk types. For more information, see the following parameter descriptions. |
| Alias | String | The name of the risk type. |
| TypeName | String | The code of the risk type. |
| WarnCount | String | The number of risks that have been detected. |
| SubTypes | Array | A list of sub-risk types. For more information, see the following parameter descriptions. |
| Alias | String | The name of the sub-risk type. |
| TypeName | String | The code of the sub-risk type. |
| WarnCount | String | The number of risks that have been detected. |

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=DescribeRiskType &StrategyId=10
```

Sample responses (JSON format)

```json
 "RequestId":"11D3993A-02B8-4FD9-9116-922BCDE53A80",
 "RiskTypes":[
   "TypeName":"system",
   "SubTypes":[
     "TypeName":"group_policy",
     "Alias":"Group policy",
     "WarnCount":0
```

`},`

```json
     "TypeName":"baseline",
     "Alias":"Baseline policy",
     "WarnCount":0
```

`},`

```json
     "TypeName":"register",
     "Alias":"Registry",
     "WarnCount":0
```

`],`

```json
   "Alias":"System",
   "WarnCount":0
```

`],`

```json
 "count": 1,
```

#### 4.4.9 Describesummary

You can call this operation to query the risks detected in baseline check by risk type.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to Describesummary. |
| PageSize | Integer | No | The number of records displayed on a page. Default value: 20. |
| CurrentPage | Integer | No | The current page number. Default value: 1. |

| Dealed | String | No | Indicates whether the risk has been handled. Valid values: Y: indicates that the risk has been handled. N: indicates that the risk has not been handled. |
|---|---|---|---|
| RiskLevels | String | No | The risk level. Separate multiple risk levels with commas (,). |
| RiskName | String | No | The name of the risk. Note Fuzzy match is supported. |
| StatusList | String | No | The status of the risk. Valid values: 1: indicates that the risk is pending. 2: indicates that the risk has been ignored. 3: indicates that the risk has been confirmed. 8: indicates that the risk has been marked as a false positive. 16: indicates that the risk is being handled. 32: indicates that the risk has been handled. You can specify multiple statuses and separate them with commas (,). |
| StrategyId | Long | No | The ID of the baseline check policy. |
| TypeNames | String | No | The type of the risk. Separate multiple risk types with commas (,). |
| SubTypeNames | String | No | The type of the sub-risk. Separate multiple sub-risk types with commas (,). |
| Uuids | String | No | The UUID of the server. Separate multiple UUIDs with commas (,). |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| TotalCount | Integer | The number of returned records. |
| Count | Integer | The number of returned risk records. |
| CurrentPage | Integer | The current page number. |

| PageSize | Integer | The maximum number of records displayed on a page. |
|---|---|---|
| WarningSummarys | Array | A list of risks. For more information, see the following parameter descriptions. |
| LastFoundTime | String | The latest time when the risk was detected. |
| Level | String | The risk level. |
| PendingCount | Integer | The number of pending risks. |
| RiskDetail | String | The risk details. |
| RiskId | Long | The ID of the risk. |
| RiskName | String | The name of the risk. |
| TypeAlias | String | The type of the risk. |
| SubTypeAlias | String | The type of the sub-risk. |
| TotalCount | Integer | The total number of risks. |

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=Describesummary &CurrentPage=20 &Dealed=Y &PageSize=10 &StrategyId=1 &Uuid=2738e842-7d46-42f7-acb4-e6796b051ddc
```

Sample responses (JSON format)

```json
 "TotalCount":1,
 "PageSize":20,
 "RequestId":"38AAFEEE-F52F-4B2E-9F28-FC4A35F8D432",
 "CurrentPage":1,
 "count": 1,
 "WarningSummarys":[
   "RiskId":1,
   "LastFoundTime":"2018-04-08 16:51:26",
   "RiskDetail":"The SSH logon security policy checks the following configurations: \
n1. Checks whether the logon port is the default port 22\n2 and whether the root acco unt is allowed\n3. Checks whether the SSH V1 protocol is used\n4. Checks whether the RSH protocol is used\n5. Checks whether authentication-based logon is performed\n Sol ution: \n Edit /etc/ssh/sshd_config\n1. Port (not 22)\n2. PermitRootLogin (no)\n3. Pr otocol (2)\n4. IgnoreRhosts (yes)\n5. e) HostbasedAuthentication (no)
   "Level":"low",
   "TypeAlias":"System",
   "SubTypeAlias":"Baseline check policy",
   "RiskName":"SSH logon baseline check"
```

`]`

### 4.5 Unusual logon detection

#### 4.5.1 DescribeBaseConfigs

You can call this operation to query the logon security settings.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeBaseConfigs. |
| Type | String | Yes | The type of the logon security configuration record. Valid values: login common location: indicates _ _ an approved logon location. login common ip: indicates an _ _ approved logon IP address. login common time: indicates an _ _ approved logon time period. login common account: indicates _ _ an approved logon account. |

| Target | String | No | The specified server. Note You must specify this parameter to query the logon security settings of a specified server. For more information about the format, see the sample request. |
|---|---|---|---|
| PageSize | Integer | No | The maximum number of records to be displayed on each page. Default value: 20. |
| CurrentPage | Integer | No | The current page number. Default value: 1. |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| CurrentPage | Integer | The current page number. |
| PageSize | Integer | The maximum number of records displayed on a page. |
| TotalCount | Integer | The total number of the returned records. |
| BaseConfigs | Array | The logon security settings. For more information, see the following parameter descriptions. |
| Account | String | The approved logon account. |
| EndTime | String | The end time of the approved logon time period. |
| Ip | String | The approved logon IP address. |
| Location | String | The approved logon location. |
| StartTime | String | The start time of the approved logon time period. |
| TotalCount | Integer | The total number of servers. |
| UuidCount | Integer | The number of servers to which the specified configuration record applies. |
| TargetList | Array | The information about servers to which the specified configuration record applies. For more information, see the following parameter descriptions. |

| TargetType | String | The type of the Target parameter value. Valid values: groupId: indicates an asset group ID. uuid: indicates a server UUID. |
|---|---|---|
| Target | String | The asset group ID or server UUID. |

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=DescribeBaseConfigs &CurrentPage=1 &PageSize=20 &Target=[{"targetType":"uuid","target":"6dbdbfe7-06fa-4d9a-8268-ce2dc6d673ac"}] &Type=login_common_location
```

Sample responses (JSON format)

```json
 "BaseConfigs": [{
  "totalCount": 9,
  "location": "United States",
  "uuidCount": 1,
  "targetList": [{
   "target": "6dbdbfe7-06fa-4d9a-8268-ce2dc6d673ac",
   "targetType": "uuid"
```

`}]`

```json
 }],
 "TotalCount": 1,
 "PageSize": 5,
 "RequestId": "485ABE58-4E27-4416-997C-F8F3B8748EB6",
 "CurrentPage": 1
```

#### 4.5.2 DescribeSwitchConfigs

You can call this operation to query the logon security configuration records in the logon security settings.

| Name | Type | Required | Description |
|---|---|---|---|

| Action | String | Yes | The operation that you want to perform. Set the value to DescribeSwitchConfigs. |
|---|---|---|---|

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| Count | Integer | The total number of returned records. |
| ConfigList | Array | The statuses of the logon security configuration items. For more information, see the following parameter descriptions. |
| Item | String | The logon security configuration items. Valid values: login common location: indicates an approved _ _ logon location. login common ip: indicates an approved logon _ _ IP address. login common time: indicates an approved _ _ logon time range. login common account: indicates an approved _ _ logon account. |
| Status | Integer | The status of the configuration item. Valid values: 1: indicates enabled. 0: indicates disabled. |

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=DescribeSwitchConfigs
```

Sample responses (JSON format)

```json
 "Count":3,
 "RequestId":"3F2C126D-870B-4AE4-8604-58BDECF873F4",
 "ConfigList":[
   "Status":1,
   "Item":"login_common_ip"
```

`},`

```json
   "Status":0,
   "Item":"login_common_account"
```

`},`

```json
   "Status":0,"Item":"login_common_time"
```

`]`

#### 4.5.3 DescribeConfigTarget

You can call this operation to query the information about servers to which a specified logon security configuration record applies.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeConfigTarget. |
| Type | String | Yes | The logon security configuration record used to identify a valid logon to a server. Valid values: login common location: indicates _ _ an approved logon location. login common ip: indicates an _ _ approved logon IP address. login common time: indicates an _ _ approved logon time range. login common account: indicates _ _ an approved logon account. |
| Target | String | No | The specified server. Note You need to specify this parameter to query the logon security configuration records of a specified server. For more information about the format, see the sample request. |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| Count | Integer | The total number of returned records. |
| TargetList | Array | The information about server to which the specified configuration record applies. For more information, see the following parameter descriptions. |
| TargetType | String | The type of the Target parameter value. Valid values: groupId: indicates an asset group ID. uuid: indicates a server UUID. |
| Target | String | The asset group ID or server UUID. |

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=DescribeConfigTarget &Config={"uuidCount":1,"location":"Ganzhou"} &Target=[{"targetType":"uuid","target":"6dbdbfe7-06fa-4d9a-8268-ce2dc6d673ac"}] &Type=login_common_location
```

Sample responses (JSON format)

```json
  "TargetList": [{
   "Target": "inet-e53455ec-a134-4d46-9ff5-c4f3a5fe0f02",
   "TargetType": "uuid"
  }, {
   "Target": "inet-25f4ef74-29c7-49fd-85cc-b4543a2489a8",
   "TargetType": "uuid"
 "Count": 2,
 "RequestId": "B8064EA4-9472-4D03-B7D1-6684DB5CD0BE",
```

#### 4.5.4 ModifyBaseConfig

You can call this operation to modify logon security settings.

| Name | Type |   | Required | Description |   |   |
|---|---|---|---|---|---|---|
| Action | String |   | Yes | The operation that you want to perform. Set the value to ModifyBaseConfig. |   |   |
| Type | String |   | Yes | The type of the logon security settings. Valid values: login common location: indicates _ _ approved logon locations. login common ip: indicates _ _ approved logon IP addresses. login common time: indicates _ _ approved logon time periods. login common account: indicates _ _ approved logon accounts. |   |   |
| Target | String |   | No | The target server. Note You must set this parameter when you need to query the logon security settings for a server. For more information about the format, see the following sample request. |   |   |
| Config | String |   | No | The logon security settings. The formats for all the settings are as follows: Approved logon locations: {"location":"Ganzhou City"} Approved logon IP addresses: {"ip":"x.x.x.x"} Approved logon time periods: {"startTime":"16:18","endTime" :"16:18"} Approved logon accounts: {"account":"dbaadmin"} |   |   |
|   |   |   |   |   | {"startTime":"16:18","endTime" |   |
|   |   |   |   | :"16:18"} |   |   |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=ModifyBaseConfig &Config={"startTime":"16:18","endTime":"16:18"} &Target=[{"targetType":"uuid","target":"0c797eb1-e6b9-4b5a-8917a7e6cbbb4b2e","flag":"add"},{"targetType":"uuid","target":"1759b0ea-6dd7-438b-b60d-c9 0179bd9ebc","flag":"del"}] &Type=login_common_location
```

Sample responses (JSON format)

```json
 "RequestId":"BB8F5902-BD50-49AB-B124-18E9CA92BB99"
```

#### 4.5.5 DeleteBaseConfig

You can call this operation to delete a logon security setting, such as an approved logon location or IP address.

| Parameter | Type |   | Required | Description |   |   |
|---|---|---|---|---|---|---|
| Action | String |   | Yes | The operation that you want to perform. Set this parameter to DeleteBaseConfig. |   |   |
| Config | String |   | Yes | The logon security setting. The formats of the logon security settings and examples are as follows: Approved logon location: {"location":"Ganzhou City"} Approved logon IP address: {"ip":" x.x.x.x"} Approved logon time range: {"startTime":"16:18","endTime" :"16:18"} Approved logon account: {"account":"dbaa****"} |   |   |
|   |   |   |   |   | {"startTime":"16:18","endTime" |   |
|   |   |   |   | :"16:18"} |   |   |
| Type | String |   | Yes | The type of the logon security setting. Valid values: login common location: indicates _ _ an approved logon location. login common ip: indicates an _ _ approved logon IP address. login common time: indicates an _ _ approved logon time range. login common account: indicates _ _ an approved logon account. |   |   |

| Target | String | No | The target server. Note You must set this parameter if you want to delete a logon security setting for a server. For more information about the format, see the following sample request. |
|---|---|---|---|

| Parameter | Type | Description |
|---|---|---|
| RequestId | String | The ID of the request. |

For more information about the error codes that this operation can return, see Error codes. Sample request

```
https://aegis.[ RegionId].example.com/?Action=DeleteBaseConfig &Config={"location":"Ganzhou City"} &Target=[{"targetType":"uuid","target":"6dbdbfe7-06fa-4d9a-8268-ce2dc6d673ac"}] &Type=login_common_location
```

Sample response (JSON format)

```json
    "RequestId":"E3785090-CFF4-4C53-82E4-08F902586053"
```

#### 4.5.6 ModifySwitchConfig

You can call this operation to modify the setting about whether to enable a logon security configuration record to identify a valid logon to a server in the logon security settings.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to ModifySwitchConfig. |

| Item | String | Yes | The logon security configuration items. Valid values: login common location: indicates _ _ an approved logon location. login common ip: indicates an _ _ approved logon IP address. login common time: indicates an _ _ approved logon time range. login common account: indicates _ _ an approved logon account. |
|---|---|---|---|
| Status | Integer | Yes | The status of the logon security configuration switch. Valid values: 1: indicates enabled. 0: indicates disabled. |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| Count | Integer | The total number of returned records. |
| ConfigList | Array | The status of the logon security configuration switch. For more information, see the following parameter descriptions. |
| Item | String | The logon security configuration items. Valid values: login common location: indicates an approved _ _ logon location. login common ip: indicates an approved logon _ _ IP address. login common time: indicates an approved _ _ logon time range. login common account: indicates an approved _ _ logon account. |
| Status | Integer | The status of the logon security configuration switch. Valid values: 1: indicates enabled. 0: indicates disabled. |

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=ModifySwitchConfig &Item=login_common_location &Status=1
```

Sample responses (JSON format)

```json
 "RequestId":"3F2C126D-870B-4AE4-8604-58BDECF873F4"
```

### 4.6 Webshell detection

#### 4.6.1 DescribeCategoryCount

You can call this operation to query the number of webshells detected by Server Guard.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeCategoryCount. |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| Webshell | Integer | The number of webshells. |

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=DescribeCategoryCount
```

Sample responses (JSON format)

```json
    "RequestId": "43F670F3-AB40-4E91-BC7D-C57468834F67",
    "Webshell": 2
```

#### 4.6.2 DescribeWebshell

You can call this operation to query records of webshell files that have been detected by Server Guard, including the detection time and webshell file path.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set this parameter to DescribeWebshell. |
| GroupId | Integer | No | The ID of the asset group. |
| Mark | String | No | The IP address or instance name of the server. |
| Tag | Integer | No | The server tag ID. |
| Dealed | String | No | The status of the webshell event. Valid values: n: indicates that the event is pending. y: indicates that the event has been handled. |

| Parameter | Type | Description |
|---|---|---|
| RequestId | String | The ID of the request. |
| WebshellList | Array | The webshell events. For more information, see the following descriptions. |
| Os | String | The operating system of the server. |
| InstanceName | String | The instance name of the server. |
| GroupId | Long | The ID of the asset group. |
| Ip | String | The IP address of the server. Note The public IP address of the server is displayed preferentially. If no public IP address is assigned to the server, the private IP address of the server is displayed. |

| Uuid | String | The universally unique identifier (UUID) of the server. |
|---|---|---|
| FoundTime | String | The time when the webshell file was detected. |
| InstanceId | String | The instance ID of the server. |
| TrojanType | String | The type of the webshell file. |
| FirstFoundTime | String | The time when the webshell file was detected for the first time. |
| TrojanSize | Long | The size of the webshell file. |
| Domain | String | The domain name associated with the server. |
| TrojanPath | String | The path of the webshell file. |
| Region | String | The region where the server resides. |
| Status | Integer | The status of the webshell event. Valid values: 1: indicates that the event is pending. 2: indicates that the event has been ignored. 3: indicates that the event has been confirmed. 8: indicates that the event has been labeled as a false positive. 16: indicates that the event is being handled. 32: indicates that the event has been handled. |

For more information about the error codes that this operation can return, see Error codes. Sample request

```
https://aegis.[ RegionId].example.com/?Action=DescribeWebshell &Dealed=n &GroupId=1 &Remark=xx.xx.xx.xx &Tag=11
```

Sample response (JSON format)

```json
    "WebshellList": [{
        "Uuid": "aa46dbe9-d35d-4b77-a4d9-10bc6b1b****",
        "FoundTime": "2018-02-27 03:23:18",
        "Ip": "xx.xx.xx.xx",
        "FirstFoundTime": "2017-12-24 03:36:03",
        "Domain": "",
        "TrojanType": "Webshell",
        "InstanceId": "i-bp15xtqydmbujgep****",
        "TrojanPath": "c:/zhb/wamp/wamp/www/My.php",
        "GroupId": 3259405,
        "Os": "windows",
        "Status": 1,
        "Region": "cn-hangzhou-dg-a01",
        "TrojanSize": 0,
        "InstanceName": "win08****"
    }, {
        "Uuid": "aa46dbe9-d35d-4b77-a4d9-10bc6b1bb610",
        "FoundTime": "2017-12-25 03:53:22",
        "Ip": "x.x.x.x",
        "FirstFoundTime": "2017-12-24 03:36:01",
        "Domain": "",
        "TrojanType": "Webshell",
        "InstanceId": "i-bp15xtqydmbujgepdbev",
        "TrojanPath": "c:/zhb/wamp/../wamp/wamp/www/abc/My.php",
        "GroupId": 3259405,
        "Os": "windows",
        "Status": 9,
        "Region": "cn-hangzhou-dg-a01",
        "TrojanSize": 0,
        "InstanceName": "win08-zhb"
    }],
    "RequestId": "E4B254AE-5CB1-4810-8B51-A08DF5697F25"
```

#### 4.6.3 DescribeQuaraFile

You can call this operation to obtain the list of quarantined files.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeQuaraFile. |

| PageSize | Integer | No | The maximum number of records to be displayed on each page of the query result. Default value: 20. |
|---|---|---|---|
| CurrentPage | Integer | No | The current page number. Default value: 1. |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| TotalCount | Integer | The total number of returned records. |
| CurrentPage | Integer | The current page number. |
| PageSize | Integer | The maximum number of records displayed on a page. |
| QuaraFiles | Array | The list of quarantined files. For more information, see the following parameter descriptions. |
| EventName | String | The name of the unusual event. |
| EventType | String | The type of the unusual event. |
| FileStatus | String | The status of the quarantined file. Valid values: quaraFailed("0"): indicates that the file failed to be quarantined. rollbackFailed("1"): indicates that the file failed to be rolled back to a previous version. quaraDone("2"): indicates that the file has been quarantined. rollbackDone("3"): indicates that the file has been rolled back to a previous version. quaraing("4"): indicates that the file is being quarantined. rollbacking("5"): indicates that the file is being rolled back to a previous version. |
| Md5 | String | The MD5 value of the file. |
| Online | Boolean | Indicates whether the Server Guard agent on the server is online. |
| Path | String | The file path. |
| Tag | String | The unique identifier of the unusual event. |
| Uuid | String | The UUID of the server. |

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=DescribeQuaraFile
```

Sample responses (JSON format)

```json
    "TotalCount":1,
    "PageSize":20,
    "RequestId":"0C7FAD74-83FA-4671-9250-A5F2A64F437A",
    "CurrentPage":1,
    "QuaraFiles":[
            "Path":"/bin/ping",
            "Uuid":"9b0c4d55-2f1f-4766-a90a-2c9d8a0b7642",
            "FileStatus":"quaraDone",
            "EventType":"Parent class of cloud scanning events (test ping)",
            "EventName":"Sub-class of cloud scanning events (test ping)",
            "Tag":"1d791175ad0bffd973b039248d6086e0",
            "Online":false,
            "Md5":"1421d9ad2b0031483f396154d48161f1"
```

`]`

#### 4.6.4 RollbackQuaraFile

You can call this operation to restore a specified quarantined file.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to RollbackQuaraFile. |
| EventName | String | No | The name of the unusual event. |
| EventType | String | No | The type of the unusual event. |
| Tag | String | No | The GUID of the unusual event. |
| Uuid | String | No | The UUID of the server. |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=RollbackQuaraFile &EventName=DDoS trojan &EventType=Malicious process &Tag=a50f96f958fbd59f68e4bca4d90679d6 &Uuid=00f11fcb-1a9a-4fd5-a48a-e0e5bd12a6a4
```

Sample responses (JSON format)

```json
 "RequestId":"0C7FAD74-83FA-4671-9250-A5F2A64F437A",
```

#### 4.6.5 DescribeWebPath

You can call this operation to query the Web directories defined in webshell settings.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set this parameter to DescribeWebPath. |
| PageSize | Integer | No | The number of records to return on each page. Default value: 20. |
| CurrentPage | Integer | No | The number of the page to return. Default value: 1. |
| Type | String | No | The type of the settings. Set this parameter to web path to _ specify the Web directory settings. |

| Parameter | Type | Description |
|---|---|---|
| RequestId | String | The ID of the request. |
| TotalCount | Integer | The number of returned records. |
| CurrentPage | Integer | The number of the current page returned. |
| PageSize | Integer | The number of records returned on each page. |
| Count | Integer | The number of Web directories. |
| ConfigList | Array | The Web directories. For more information, see the following descriptions. |
| WebPath | String | The path of the Web directory. |
| TargetList | Array | The servers that the Web directory has been applied to. For more information, see the following descriptions. |
| TargetType | String | This parameter always returns a value of uuid, which means that the Target parameter returns the universally unique identifier (UUID) of the server. |
| Target | String | The UUID of the server. |

For more information about the error codes that this operation can return, see Error codes. Sample request

```
https://aegis.[ RegionId].example.com/?Action=DescribeWebPath
```

Sample response (JSON format)

```json
 "TotalCount":1,
 "PageSize":5,
 "RequestId":"7B6AD7C9-0F8D-4126-B8AA-6DC308B0B534",
 "CurrentPage":1,
 "Count":1,
 "ConfigList":[
   "TargetList":[
     "Target":"inet-f6ac9a93-0818-4052-90e2-d24f18ee198b",
     "TargetType":"uuid"
```

`],`

```json
   "WebPath":"/usr/local/tomcat/webroot18"
```

`]`

#### 4.6.6 ModifyWebPath

You can call this operation to modify the Web directory in webshell settings.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to ModifyWebPath. |
| Type | String | No | The configuration type. Set the value to web path, indicating _ the web directory configuration. |
| Config | String | No | The Web directory configuration, in JSON format. For more information, see the sample request. |
| Target | String | No | The list of target servers to which the Web directory configuration applies, in JSON format. For more information, see the sample request. |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=ModifyWebPath &Type=web_path &Config={"webPath":"/test"} &Target={"targetType":"uuid","target":"0c797eb1-e6b9-4b5a-8917a7e6cbbb4b2e","flag":"add"}
```

Sample responses (JSON format)

```json
 "RequestId":"7B6AD7C9-0F8D-4126-B8AA-6DC308B0B534"
```

#### 4.6.7 OperateTrojan

You can call this operation to handle detected webshells.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to OperateTrojan. |
| Info | String | No | The webshell information, in JSON format. For more information, see the sample request. |
| OperateType | String | No | The type of the operation. Valid values: isolate: indicates an operation to quarantine the file. trust: indicates an operation to trust the file. untrust: indicates an operation to cancel trusting the file. restore: indicates an operation to restore the file. |
| Type | Integer | No | The type of the trojan. Set the value to 1. |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| FailedCount | Integer | The number of failed operations. |
| SuccessCount | Integer | The number of successful operations. |

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=OperateTrojan &Info=[{"uuid":"97988c2b-de9d-4159-90ab- 7cc73561c64c","filePath":"/home/test/Z02.php","webshellId":""}] &OperateType=trust &Type=1
```

Sample responses (JSON format)

```json
    "RequestId": "43F670F3-AB40-4E91-BC7D-C57468834F67",
    "FailedCount": 0,
    "SuccessCount": 1
```

### 4.7 Exception detection on hosts

#### 4.7.1 DescribeSuspEventTypes

You can call this operation to query the unusual event types.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeSuspEventTypes. |

| Name | Type | Description |
|---|---|---|

| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
|---|---|---|
| TotalCount | Integer | The total number of returned records. |
| EventTypes | Array | The list of unusual event types. For more information, see the following parameter descriptions. |
| AliseEventType | String | The name of the unusual event type. |
| EventType | String | The identifier of the unusual event type. |

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=DescribeSuspEventTypes
```

Sample responses (JSON format)

```json
 "TotalCount":1,
 "RequestId":"66BE7091-BC00-4943-8A0D-B3DCE90AD7B5",
 "EventTypes":[
   "EventType":"Suspicious process",
   "AliseEventType":"Suspicious process"
```

`]`

#### 4.7.2 DescribeSuspTrendStatistics

You can call this operation to query the chart data on different types of unusual server events on each day.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeSuspTrendStatistics. |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| Interval | Integer | The time length of the the time frame specified for query. |
| StartTime | Integer | The start time of the time frame specified for query. |
| SuspiciousItems | List | The statistics on numbers of different types of suspicious events. |

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=DescribeSuspTrendStatistics
```

Sample responses (JSON format)

```json
 "RequestId":"66BE7091-BC00-4943-8A0D-B3DCE90AD7B5",
 "Start":-28800000,
 "Interval":86400000,
 "SuspiciousItems":[ ]
```

#### 4.7.3 DescribeSuspiciousExportInfo

You can call this operation to query an unusual event export task.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set this parameter to DescribeSuspiciousExportInfo. |
| ExportId | Long | No | The ID of the export task. |

| Parameter | Type | Description |
|---|---|---|
| RequestId | String | The ID of the request. |

| CurrentCount | Integer | The number of records that have been exported. |
|---|---|---|
| ExportStatus | String | The status of the export task. Valid values: init: indicates that the export task is being initialized. pending: indicates that the export task is pending. exporting: indicates that the export task is being executed. success: indicates that the export task has been completed. fail: indicates that the export task has failed. |
| Message | String | The status description or failure information of the export task. |
| FileName | String | The name of the exported file. |
| Id | Integer | The ID of the export task. |
| GmtCreate | Long | The time when the export task was created. |
| Link | String | The download link of the exported file. |
| Progress | Integer | The export progress. |
| TotalCount | Integer | The total number of records that have been exported. |

For more information about the error codes that this operation can return, see Error codes. Sample request

```
https://aegis.[ RegionId].example.com/?Action=DescribeSuspiciousExportInfo &ExportId=1
```

Sample response (JSON format)

```json
 "TotalCount":30,
 "GmtCreate":1518071546000,
 "Progress":100,
 "Message":"success",
 "RequestId":"654A6FD8-B55D-4D6B-AAFF-4122503D108B",
 "FileName":"suspicious_20180208",
 "ExportStatus":"success",
 "CurrentCount":30,
 "Id":11,
 "Link":"http://suspicious-export.oss-cn-
shanghai.example.com/export/suspicious_20180208_1518071576098.zip? Expires=1518075176&OSSAccessKeyId=<yourAccessKeyId>&Signature=xxxx%xxxx%3D"
```

#### 4.7.4 OperateSuspiciousEvent

You can call this operation to handle detected unusual events.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to OperateSuspiciousEvent. |
| Data | String | No | The unusual event to be handled, in JSON format. For more information, see the sample request. |
| OperateType | String | No | The type of the operation. Valid values: deal: indicates an operation to handle the unusual event. confirm: indicates an operation to mark the unusual event as handled. mark misinformation: indicates an _ operation to mark the unusual event as false positive. unmark misinformation: indicates _ an operation to remove the false positive mark of the unusual event. ignore: indicates an operation to ignore the unusual event. |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=OperateSuspiciousEvent &OperateType=ignore &Data={"uuid":"97988c2b-de9d-4159-90ab- 7cc73561c64c","tag":"f87eb0ee5934f6f65343ec601ce71c2f","eventType":"Malicious process es (malware checking)","eventName":"DDoS Trojan},{"uuid":"97988c2b-de9d-4159-90ab-7cc 73561c64c","tag":"95347a77b8c0d6dae99a23ab69aa90f4","eventType":"Malicious processes (malware checking)","eventName":"GateDDoS Trojan"}
```

Sample responses (JSON format)

```json
 "RequestId":"654A6FD8-B55D-4D6B-AAFF-4122503D108B"
```

#### 4.7.5 OperateLoginLog

You can call this operation to label a detected unusual logon event as handled.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to OperateLoginLog. |
| Ids | String | Yes | The ID of the unusual logon log. Separate multiple log IDs with commas (,). |
| OperateType | String | Yes | The type of the operation. Set the value to confirm, indicating that the event has been handled. |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=OperateLoginLog &Ids=2006434 &OperateType=confirm
```

Sample responses (JSON format)

```json
 "RequestId":"BE391ABB-6B7C-4C41-9F6C-862C1DEE3905"
```

#### 4.7.6 DescribeVirusInfo

You can call this operation to upload the MD5 values of files and use Alibaba Cloud Antivirus to determine whether the files are malicious programs.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeVirusInfo. |
| Md5 | String | Yes | The MD5 value of the file. |
| Lang | String | No | The language attribute of the file, such as zh. |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| Data | Boolean | Indicates whether the file is malicious. Valid values: True: Indicates that the file is malicious. False: Indicates that the file is not malicious. |

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].aliyuncs.com/?Action= DescribeVirusInfo &Md5=6f6628d923f9018b28acc5f905e03244
```

Sample responses (JSON format)

```json
 "RequestId": "A2423F39-3272-4491-804E-D0EBDE3E894D",
 "Data": true
```

#### 4.7.7 CreateSuspiciousExport

You can call this operation to export the information about unusual events on servers based on search conditions.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to CreateSuspiciousExport. |
| Dealed | String | No | Indicates whether the unusual event has been handled. Valid values: Y: indicates that the event has been handled. N: indicates that the event has not been handled. |
| EventNameRema rk | String | No | The name of the event. Fuzzy matching is supported. |
| EventType | String | No | The name of the event type. Valid values: Unusual logon Suspicious process Suspicious account Sensitive file tampering Suspicious network connection Unusual event Suspicious file Malicious process |
| GroupId | String | No | The ID of the asset group. |

| Level | String | No | The risk level of the event. Valid values: Critical: indicates a critical-risk event. Important: indicates an important- risk event. Moderate: indicates a moderate-risk event. low: indicates a low-risk event. You can specify multiple event levels and separate them with commas (,). |
|---|---|---|---|
| Remark | String | No | The name or IP address of the server. Fuzzy matching is supported. |
| StatusList | String | No | The handling status of the event. Valid values: 1: indicates that the event is to be handled. 2: indicates that the event has been ignored. 3: indicates that the event has been confirmed. 8: indicates that the event has been labeled as a false positive. 16: indicates that the event is being handled. 32: indicates that the event has been handled. You can specify multiple statuses and separate them with commas (,). |
| Tag | String | No | The tag of the server. |
| Uuids | String | No | The UUID of the server. Separate multiple UUIDs with commas (,). |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| FileName | String | The name of the exported file. |
| Id | Long | The ID of the export task. |

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=CreateSuspiciousExport &Remark=23 &EventType=Suspicious process &Level=serious,high,medium,low &Dealed=n
```

Sample responses (JSON format)

```json
    "RequestId": "43F670F3-AB40-4E91-BC7D-C57468834F67",
    "FileName": "suspicious_20180408",
    "Id": 387
```

### 4.8 Retrieval of host logs

#### 4.8.1 DescribeFilterFields

You can call this operation to query the filter fields of a specified server log search condition.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeFilterFields. |
| Query | String | No | The log search condition. |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| Total | String | The total number of search conditions. |
| LogFilterList | Array | The filter field information. For more information, see the following parameter descriptions. |
| Fields | String | The filter fields. |

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=DescribeFilterFields &Query=aegis-log-login@warn_port:22
```

Sample responses (JSON format)

```json
 "LogFilterList":[
   "Fields":"IP;IP address,UUID;Client ID","fieldsName":"default"
```

`],`

```json
 "Total":"20",
 "RequestID":"883e1e3d-4443-4206-871c-6c0625c01332"
```

#### 4.8.2 DescribeHistogram

You can call this operation to obtain the statistics on server logs generated within a specified time frame.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeHistogram. |
| Query | String | Yes | The log query conditions. |
| EndTime | String | Yes | The end time of the time frame specified for query. |
| StartTime | String | Yes | The start time of the time frame specified for query. |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| Categories | String | The timeline information. |
| Items | Array | The log quantity statistics. For more information, see the following parameter descriptions. |
| Data | List | The number of logs. |

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=DescribeHistogram &EndTime=2018-03-03 17:41:03 &Query=aegis-log-login@warn_port:22 &StartTime=2018-03-02 17:41:03
```

Sample responses (JSON format)

```json
 "RequestId":"82D245FB-7A5D-4155-B59F-5B084CE93B6B",
 "Categories":[
  "1519983663000,1519984800000",
  "1519984800000,1519986600000",
  "1519986600000,1519988400000",
  "1519988400000,1519990200000",
  "1519990200000,1519992000000",
  "1519992000000,1519993800000",
  "1519993800000,1519995600000"
```

`],`

```json
 "Items":[
   "Data":[
```

`0,` `0,` `0,` `0,` `0,` `0,` `]` `]`

#### 4.8.3 DescribeLogInfo

You can call this operation to query the server log fields based on specified query conditions.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeLogInfo. |

| PageSize | Integer | No | The maximum number of records to be displayed on each page of the query result. Default value: 20. |
|---|---|---|---|
| CurrentPage | Integer | No | The current page number. Default value: 1. |
| Query | String | Yes | The log query conditions. |
| EndTime | String | Yes | The end time of the query. |
| StartTime | String | Yes | The start time of the query. |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| TotalCount | Integer | The total number of returned records. |
| LogInfoItems | Array | The information about server log fields. For more information, see the following parameter descriptions. |
| Id | String | The ID of the log source. |
| Name | String | The name of the log source. |
| Fields | Array | The list of server log fields. For more information, see the following parameter descriptions. |
| Name | String | The ID of the log field. |
| Desc | String | The name of the log field. |
| Type | String | The type of the log field. |

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=DescribeLogInfo &CurrentPage=1 &EndTime=2018-03-03 17:41:03 &PageSize=20 &Query=aegis-log-login@warn_port:22 &StartTime=2018-03-02 17:41:03
```

Sample responses (JSON format)

```json
    "TotalCount":1,
    "RequestId":"3A7CFB73-C24C-4711-B7D9-2BE74EBFFE78",
    "LogInfoItems":[
            "Fields":[
                    "Desc":"IP address",
                    "Type":"string",
                    "Name":"ip"
```

`},`

```json
                    "Desc":"Client number",
                    "Type":"string",
                    "Name":"uuid"
```

`},`

```json
                    "Desc":"Logon source IP address",
                    "Type":"string",
                    "Name":"warn_ip"
```

`},`

```json
                    "Desc":"Logon port",
                    "Type":"string",
                    "Name":"warn_port"
```

`},`

```json
                    "Desc":"Logon username",
                    "Type":"string",
                    "Name":"warn_user"
```

`},`

```json
                    "Desc":"Logon type",
                    "Type":"string",
                    "Name":"warn_type"
```

`},`

```json
                    "Desc":"Logon count",
                    "Type":"string",
                    "Name":"warn_count"
```

`],`

```json
            "Id":"aegis-log-login",
            "Name":"Logon serial number"
```

`},` `]`

#### 4.8.4 DescribeLogItems

You can call this operation to query the server log details that are returned by a query.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeLogItems. |
| PageSize | Integer | No | The number of records displayed on a page. Default value: 20. |
| CurrentPage | Integer | No | The current page number. Default value: 1. |
| Query | String | No | The log query criterion. |
| AccountSnapshot Offset | Integer | No | The offset of the account snapshot log. |
| CrackOffset | Integer | No | The offset of the brute force password cracking log. |
| LoginOffset | Integer | No | The offset of the logon log. |
| NetworkOffset | Integer | No | The offset of the network connection log. |
| PortSnapshotOffs et | Integer | No | The offset of the listening port snapshot log. |
| ProcessOffset | Integer | No | The offset of the process startup log. |
| ProcessSnapshot Offset | Integer | No | The offset of the process snapshot log. |
| EndTime | String | Yes | The end time of the time frame specified for query. |
| StartTime | String | Yes | The start time of the time frame specified for query. |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| TotalCount | Integer | The number of returned records. |
| CurrentPage | Integer | The current page number. |

| SetPageSize | Integer | The maximum number of records displayed on a page. |
|---|---|---|
| AccountSnapshotOffse t | Integer | The offset of the account snapshot log. |
| AccountSnapshotTotal Count | Integer | The total number of account snapshot log entries. |
| CrackOffset | Integer | The offset of the brute force password cracking log. |
| CrackTotalCount | Integer | The total number of brute force password cracking log entries. |
| LoginTotalCount | Integer | The total number of logon log entries. |
| NetworkOffset | Integer | The offset of the network connection log. |
| NetworkTotalCount | Integer | The total number of network connection log entries. |
| PortSnapshotOffset | Integer | The offset of the listening port snapshot log. |
| PortSnapshotTotalCou nt | Integer | The total number of listening port snapshot log entries. |
| ProcessOffset | Integer | The offset of the process startup log. |
| ProcessTotalCount | Integer | The total number of process startup log entries. |
| ProcessSnapshotOffset | Integer | The offset of the process snapshot log. |
| ProcessSnapshotTotal Count | Integer | The total number of process snapshot log entries. |
| LogsList | Array | A list of host log details. For more information, see the following parameter descriptions. |
| LogSourceID | String | The ID of the log source. |
| LogSource | String | The name of the log source. |
| MLogTime | String | The time when the log entry was created. |
| MContents | Array | A list of host log entries. For more information, see the following parameter descriptions. |
| MKey | String | The log entry. |
| MValue | String | The value of the log entry. |

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=DescribeLogItems &CurrentPage=1 &PageSize=100 &AccountSnapshotOffset=1000 &CrackOffset=1000 &EndTime=2018-03-05 11:46:07 &LoginOffset=1000 &NetworkOffset=1000 &PortSnapshotOffset=1000 &ProcessOffset=1000 &ProcessSnapshotOffset=1000 &Query=aegis-log-login@warn_port:22 &StartTime=2018-03-02 17:41:03
```

Sample responses (JSON format)

```json
 "RequestId":"BE391ABB-6B7C-4C41-9F6C-862C1DEE3905",
 "PageSize":100,
 "AccountSnapshotTotalCount":0,
 "LogsList":[],
 "CrackOffset":0,
 "ProcessOffset":0,
 "NetworkOffset":0,
 "ProcessSnapshotOffset":0,
 "LoginTotalCount":0,
 "CurrentPage":1,
 "PortSnapshotOffset":0,
 "NetworkTotalCount":0,
 "AccountSnapshotOffset":0,
 "CrackTotalCount":0,
 "PortSnapshotTotalCount":0,
 "ProcessSnapshotTotalCount":0,
 "ProcessTotalCount":0
```

#### 4.8.5 CreateLogQuery

You can call this operation to create or save server log search conditions.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to CreateLogQuery. |
| Conditions | String | No | The log search condition. |

| QueryDetail | String | No | The log search sub-conditions. |
|---|---|---|---|
| QueryName | String | No | The saved search name. |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |

For more information about the error codes that this operation can return, see Error codes. Sample requests

```json
https://aegis.[ RegionId].example.com/?Action=CreateLogQuery &Conditions=aegis-log-login@warn_port:22 &QueryDetail=[[{"itemForm":{},"d":{"name":"Logons","id":"aegis-log-login","fields":[{ "name":"ip","type":"string","desc":"IP address","text":"IP(IP address)"}]] &QueryName=test
```

Sample responses (JSON format)

```json
 "RequestId":"415AE1FC-3C11-4AA9-A06F-DE13D3430366"
```

#### 4.8.6 DescribeLogQuery

You can call this operation to query the saved server log search conditions.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeLogQuery. |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| ListTotal | Integer | The total number of returned records. |

| QueryItems | Array | The details of log search conditions. For more information, see the following parameter descriptions. |
|---|---|---|
| Conditions | String | The log search conditions. |
| QueryDetail | String | The log search sub-conditions. |
| QueryName | String | The name of the log search task. |

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=DescribeLogQuery
```

Sample responses (JSON format)

```json
 "RequestId":"65802B9B-4D30-40F0-8691-F126652DBEBE",
 "ListTotal":1,
 "QueryItems":[
   "QueryDetail":"[[{\"itemForm\":{},\"d\":{\"name\":\"Account
snapshot\",\"id\":\"aegis-snapshot-host\",\"fields\": [{\"name\":\"ip\",\"type\":\"string\",\"desc\":\"IP address\"}, {\"name\":\"uuid\",\"type\":\"string\",\"desc\":\"Client ID\"}, {\"name\":\"perm\",\"type\":\"string\",\"desc\":\"Root permission availability\"},{\" name\":\"home_dir\",\"type\":\"string\",\"desc\":\"Home directory\"}, {\"name\":\"warn_time\",\"type\":\"string\",\"desc\":\"Password expiration reminder t ime\"},{\"name\":\"groups\",\"type\":\"array\",\"desc\":\"User group\"}, {\"name\":\"login_ip\",\"type\":\"string\",\"desc\":\"Last logon IP\"}, {\"name\":\"last_chg\",\"type\":\"string\",\"desc\":\"Last password change time\"},{\ "name\":\"shell\",\"type\":\"string\",\"desc\":\"Linux shell command\"}, {\"name\":\"domain\",\"type\":\"string\",\"desc\":\"Windows domain\"}, {\"name\":\"tty\",\"type\":\"string\",\"desc\":\"Logon terminal\"}, {\"name\":\"account_expire\",\"type\":\"string\",\"desc\":\"Account expiration time\" },{\"name\":\"passwd_expire\",\"type\":\"string\",\"desc\":\"Password expiration time \"},{\"name\":\"last_logon\",\"type\":\"string\",\"desc\":\"Last logon time\"},{\"nam e\":\"user\",\"type\":\"string\",\"desc\":\"User\"}, {\"name\":\"status\",\"type\":\"string\",\"desc\":\"User status: 0-disabled, 1-enable d\"}]},\"searchFields\":[{\"name\":\"ip\",\"type\":\"string\",\"desc\":\"IP address\" },{\"name\":\"uuid\",\"type\":\"string\",\"desc\":\"Client ID\"}, {\"name\":\"perm\",\"type\":\"string\",\"desc\":\"Root permission availability\"},{\" name\":\"home_dir\",\"type\":\"string\",\"desc\":\"Home directory\"}, {\"name\":\"warn_time\",\"type\":\"string\",\"desc\":\"Password expiration reminder t ime\"},{\"name\":\"groups\",\"type\":\"array\",\"desc\":\"User group\"}, {\"name\":\"login_ip\",\"type\":\"string\",\"desc\":\"Last logon IP\"}, {\"name\":\"last_chg\",\"type\":\"string\",\"desc\":\"Last password change time\"},{\ "name\":\"shell\",\"type\":\"string\",\"desc\":\"Linux shell command\"}, {\"name\":\"domain\",\"type\":\"string\",\"desc\":\"Windows domain\"}, {\"name\":\"tty\",\"type\":\"string\",\"desc\":\"Logon terminal\"}, {\"name\":\"account_expire\",\"type\":\"string\",\"desc\":\"Account expiration time\" },{\"name\":\"passwd_expire\",\"type\":\"string\",\"desc\":\"Password expiration time \"},{\"name\":\"last_logon\",\"type\":\"string\",\"desc\":\"Last logon time\"},{\"nam e\":\"user\",\"type\":\"string\",\"desc\":\"User\"}, {\"name\":\"status\",\"type\":\"string\",\"desc\":\"User status: 0-disabled, 1-enable d\"}],\"f\":{\"name\":\"ip\",\"type\":\"string\",\"desc\":\"IP address\"},\"searchLimit\": [{\"name\":\"Including\",\"value\":\":\"}],\"l\":\":\",\"kw\":\"string\"}]]",
   "Conditions":"aegis-snapshot-host@ip:string",
   "QueryName":"aa"
```

`]`

#### 4.8.7 DeleteLogQuery

You can call this operation to delete the saved server log search conditions.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DeleteLogQuery. |
| QueryName | String | No | The name of the saved search. |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=DeleteLogQuery &QueryName=test
```

Sample responses (JSON format)

```json
 "RequestId":"415AE1FC-3C11-4AA9-A06F-DE13D3430366"
```

## 5 Error codes

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
