---
title: "Alibaba Cloud Apsara Stack v3.18.6-2607 Alibaba Cloud Security-Server Guard Advanced Edition Container Security Service Developer Guide 20260828"
product_version: "V3.18.6_2607"
doc_version: "20260828"
pdf_pages: 189
source_pdf: "92e5294fcfeb1cee_Alibaba Cloud Apsara Stack v3.18.6-2607 Alibaba Cloud Security-Server Guard Advanced Edition Contain"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/3816%202607/pdf%203/%E4%BA%91%E5%AE%89%E5%85%A8%E4%B8%AD%E5%BF%83%EF%BC%88%E5%AE%89%E9%AA%91%E5%A3%AB%EF%BC%89%EF%BC%88%E4%B8%93%E6%9C%89%E4%BA%91%EF%BC%89/Alibaba%20Cloud%20Apsara%20Stack%20v3.18.6-2607%20Alibaba%20Cloud%20Security-Server%20Guard%20Advanced%20Edition%20Container%20Security%20Service%20Developer%20Guide%2020260828.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings)
---

# Alibaba Cloud Apsara Stack v3.18.6-2607 Alibaba Cloud Security-Server Guard Advanced Edition Container Security Service Developer Guide 20260828

## Table of Contents

- 1 Getting started
  - 1.1 Apsara Stack documentation
  - 1.2 Procedure for API calls
- 2 Preparations
  - 2.1 Obtain an AccessKey pair
  - 2.2 Obtain an AccessKey pair assigned by STS
  - 2.3 Obtain API information and the endpoint of an API operation
- 3 Call examples
  - 3.1 Call examples for SDK for Java
    - 3.1.1 Quick start
    - 3.1.2 Use SDK
      - 3.1.2.1 Install SDK for Java
      - 3.1.2.2 Use CommonRequest
  - 3.2 Call examples for SDK for Python
    - 3.2.1 Quick start
    - 3.2.2 Use SDK
      - 3.2.2.1 Install SDK for Python
      - 3.2.2.2 Use CommonRequest
  - 3.3 Call examples for SDK for Go
    - 3.3.1 Quick start
    - 3.3.2 Use SDK
      - 3.3.2.1 Install the core package of SDK for Go
      - 3.3.2.2 Use CommonRequest
- 4 Common parameters
- 5 API reference
  - 5.1 DescribeLatestScanTask
  - 5.2 ListImageRisk
  - 5.3 UpdateJenkinsImageScanTaskStatus
  - 5.4 DescribeImageInfoList
  - 5.5 DescribeImageBaselineCheckSummary
  - 5.6 DescribeImageListWithBaselineName
  - 5.7 DescribeImageBaselineItemList
  - 5.8 DescribeCycleTaskList
  - 5.9 DescribeContainerCriteria
  - 5.10 DescribeContainerFieldStatistics
  - 5.11 DescribeContainerGroupedFieldDetail
  - 5.12 DescribeContainerInstances
  - 5.13 DescribeGroupedContainerInstances
  - 5.14 DescribeImageSecurityScanCount
  - 5.15 DescribeImageCriteria
  - 5.16 GetRegistryScanDayNum
  - 5.17 DescribeImageInstances
  - 5.18 ListPrivateRegistryList
  - 5.19 ListPrivateRegistryType
  - 5.20 DescribeAlarmEventDetail
  - 5.21 DescribeNsasSuspEventType
  - 5.22 DescribeSuspEvents
  - 5.23 DescribeConcernNecessity
  - 5.24 DescribeEventLevelCount
  - 5.25 DescribeSecurityEventOperations
  - 5.26 DescribeGroupedVul
  - 5.27 DescribeImageGroupedVulList
  - 5.28 DescribeAllGroups
  - 5.29 DescribeImageVulList
  - 5.30 DescribeVulDetails
  - 5.31 DescribeAssetDetailByUuid
  - 5.32 DescribeAllEntity
  - 5.33 DescribeClusterVulStatistics
  - 5.34 DescribeContainerInstancesWithoutAscm
  - 5.35 DescribeExportInfo
  - 5.36 DescribePropertyCount
  - 5.37 DescribePropertyCronDetail
  - 5.38 DescribePropertySoftwareDetail
  - 5.39 DescribePropertyUserDetail
  - 5.40 ExportRecord
  - 5.41 GetClusterCheckItemWarningStatistics
  - 5.42 GetClusterSuspEventStatistics
  - 5.43 IgnoreCheckItems
  - 5.44 ListCheckItemWarningMachine
  - 5.45 ListCheckItemWarningSummary
  - 5.46 ModifyOperateVul
- 6 Error codes

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
2. Click the **Enterprise**, **Agility&XStack**, or **All-in-one** tab based on the Apsara Stack edition that you use.
3. Select an Apsara Stack version from the drop-down list.
4. In the left-side navigation pane, select the Apsara Stack service whose documentation you want to view.
5. In the product documentation section, click **View Details** or **Download PDF**.

### 1.2 Procedure for API calls

By default, Apsara Stack Enterprise Edition V3.16.0 and later versions use the point of presence (POP) gateway to deliver the same user experience as in the Alibaba Cloud public cloud. This topic describes how to use the POP gateway to call Apsara Stack API operations.

**Flowchart**

Obtain API information Obtain an AccessKey pair or STS Make prepara access credentials Obtain the values of common request headers Obtain the endpoint of the Apsara Uni-manager Management Console Make API calls Obtain an SDK package of the Apsara Uni-manager Management Console Call an API operation

**Procedure**

1. Obtain an AccessKey pair.
Obtain the AccessKey credential that is required for calling an API operation. For more information, see Obtain an AccessKey pair or Obtain an AccessKey pair assigned by STS.

**Note**

We recommend that you use an AccessKey pair or STS access credentials of a personal account to call the API operations of the Apsara Uni-manager Management Console and cloud services.
2. Obtain the region ID.
3. Obtain the organization ID and the resource set ID.
You must call an API operation to obtain an organization ID. For more information, see GetOrganizationList in Apsara Uni-manager Management Console Developer Guide. You must call an API operation to obtain a resource set ID. For more information, see ListResourceGroup in Apsara Uni-manager Management Console Developer Guide.

**Note**

When you call an API operation, set the `<x-acs-organizationid>` header to the organization ID that you queried, and set the `<x-acs-resourcegroupid>` header to the resource set ID that you queried. This way, you can query resources in the specified organization and resource set. If you do not specify the `<x-acs-organizationid>` parameter, the organization to which the current user belongs is used. If you do not specify the `<x-acs-resourcegroupid>` parameter, this parameter is left empty. If you specify a resource set, you must also specify an organization ID.
4. View the developer guide of the cloud service that you want to use to learn how to make the API call.
To learn the features of API operations and how to call the API operations, obtain the developer guide of the Apsara Stack service that you want to use. For more information, see Apsara Stack documentation.
5. Obtain the endpoint of the cloud service.
6. Obtain the SDK of the cloud service and make the API call.

## 2 Preparations

### 2.1 Obtain an AccessKey pair

Access credentials are assigned by Resource Access Management (RAM) or Security Token Service (STS). You can use one type of access credential for authentication when you make an API request. This topic describes how to obtain an AccessKey pair that is assigned by RAM.

**Background information**

An AccessKey pair is used to verify the identity of a request sender. An AccessKey pair consists of an AccessKey ID and an AccessKey secret that are used to implement symmetric encryption. The AccessKey ID is used to identify a user. The AccessKey secret is used to encrypt the signature string. You can use RAM or STS to assign an access credential for authentication. An AccessKey pair that is assigned by RAM to a third party consists of an AccessKey ID and an AccessKey secret. An access credential that is assigned by STS to a third party consists of an AccessKey ID, an AccessKey secret, and a security token. For more information, see Obtain an AccessKey pair assigned by STS. The Apsara Uni-manager Management Console provides AccessKey pairs to personal accounts and organizations. Only the administrators of level-1 organizations and operations administrators can obtain the AccessKey pairs of organizations. We recommend that you use the AccessKey pairs of personal accounts to call the operations provided by the Apsara Uni-manager Management Console and cloud services. If you use the AccessKey pair of a personal account, configure the header parameters that are described in the following table for access control. Otherwise, an error that indicates insufficient permissions may occur.

**Warning**

The AccessKey pair of a personal account is managed and limited by the permission system of the Apsara Uni-manager Management Console. If you need to obtain the AccessKey pair of an organization, make sure that your operation is allowed by an administrator. This ensures security.

| Parameter | Description |
|---|---|
| x-acs-regionid | The ID of the region. Example: cn-hangzhou-*. |
| x-acs-organizationid | The ID of the organization in the Apsara Uni-manager Management Console. For more information about how to obtain an organization ID, see the GetOrganizationList section in Apsara Uni-manager Management Console Developer Guide. |
| x-acs-resourcegroupid | The ID of the resource set in the Apsara Uni-manager Management Console. For more information about how to obtain a resource set ID, see the "ListResourceGroup" section in Apsara Uni-manager Management Console Developer Guide. |
| x-acs-instanceid | The ID of the instance that you want to manage. If you want to obtain the ID of an Elastic Compute Service (ECS) instance, you can obtain the ID from the ECS instance list. |

**Obtain the AccessKey pair of a personal account**

To obtain the AccessKey pair of a personal account, perform the following steps:
1. Log on to the Apsara Uni-manager Management Console.
2. Click the profile picture in the upper-right corner of the page and click **User Information**.
3. In the **AccessKey Pair** section, view the AccessKey pair of the personal account.

**Note**

The AccessKey pair provides full permissions on cloud resources within your Alibaba Cloud account. You must keep the AccessKey pair confidential.

**Obtain the AccessKey pair of an organization**

To obtain the AccessKey pair of an organization, perform the following steps:
1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, click **Enterprise**.
3. In the left-side navigation pane, choose **Resources > Organizations**.
4. In the organization list, click the name of the level-1 organization whose AccessKey pair you want to
obtain.
5. On the right side of the page that appears, click **Management AccessKey**.
6. In the dialog box that appears, view the AccessKey pair of the organization.

### 2.2 Obtain an AccessKey pair assigned by STS

**by STS**

This topic describes how to use Security Token Service (STS) to make API calls.

**Background information**

Alibaba Cloud STS allows you to manage temporary credentials to your Alibaba Cloud resources. You can use STS to make API calls. An AccessKey pair assigned by STS consists of an AccessKey ID, an AccessKey secret, and a security token. When you use STS to make API calls, you must use an AccessKey pair assigned by STS.

**Procedure**

1. Obtain your `RAM role` .
i. Log on to the Apsara Uni-manager Management Console. ii. Click the profile picture in the upper-right corner of the page and click **User Information**. iii. Click **View Current Role Policy**. In the **View Policies of Current Role** dialog box, view your `RAM role` .
2. Obtain the AccessKey pair assigned by STS.

**Note**

You must use the actual values to replace the variables in the following sample code. The angle brackets <> are not retained in the final code. The following list describes the variables: <yourRegionID>: Replace it with the actual region ID. <yourAccessKeyID>: Replace it with your AccessKey ID. <yourAccessKeySecret>: Replace it with your AccessKey secret. <yourRoleSessionName>: Replace it with your current session name. In most cases, this variable is set to the identity of the user who make API calls. Example: Username. You can distinguish the users who assume the same RAM role to perform operations based on the value of the `RoleSessionName` variable. This way, you can perform user-specific auditing. The value of this variable must be 2 to 64 characters in length and can contain letters, digits, periods (.), at signs (@), hyphens (-), and underscores (_). <yourRoleArn>: Replace it with the Alibaba Cloud Resource Name (ARN) of your RAM role. "sts.aliyuns.com": Replace it with the endpoint of STS.

```
public static void main(String[] args) {
    // Create a DefaultAcsClient instance and initialize it.
    // Replace <yourRegionID>, <yourAccessKeyID>, and <yourAccessKeySecret> with the actual region I
D, your AccessKey ID, and your AccessKey secret.
    DefaultProfile profile = DefaultProfile.getProfile("<yourRegionID>", "<yourAccessKeyID>", "<your
AccessKeySecret>");
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
    // Replace "sts.aliyuns.com" with the actual endpoint of STS. The format of an STS endpoint is
sts-vpc.${global:region}.${global:internet-domain}.
    request.setSysDomain("sts.aliyuns.com");
    request.setSysProduct("Sts");
    request.setSysAction("AssumeRole");
    request.setSysVersion("2015-04-01");
    request.setSysMethod(MethodType.POST);
    request.setHttpContentType(FormatType.FORM);
    // Replace "<yourRoleSessionName>" with the name of the current session.
    request.putQueryParameter("RoleSessionName", "<yourRoleSessionName>");
    // The ARN of your RAM role. Replace "<yourRoleArn>" with the ARN of your RAM role that is obtai
ned in the previous step.
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
3. Use the AccessKey pair assigned by STS to call an operation of a cloud service. The following sample code
provides an example on how to use the AccessKey pair assigned by STS to call the `DescribeZones` operation of Elastic Compute Service (ECS):

**Note**

You must use the actual values to replace the variables in the following sample code. The angle brackets <> are not retained in the final code. The following list describes the variables: <yourRegionID>: Replace it with the actual region ID. <yourStsAccesskeyID>: Replace it with your STS AccessKey ID. <yourStsAccessKeySecret>: Replace it with your STS AccessKey secret. <yourStsToken>: Replace it with the security token of the AccessKey pair assigned by STS. <yourResourceGroupID>: Replace it with the actual resource set ID. <yourOrganizationID>: Replace it with the actual organization ID.

```java
public static void main(String[] args) {
    // Replace "<yourRegionID>" with the actual region ID.
    // Replace "<yourStsAccessKeyID>" and "<yourStsAccessKeySecret>" with the AccessKey ID and Acces
sKey secret of the AccessKey pair assigned by STS. The AccessKey ID and AccessKey secret are obtained in the previous step.
    DefaultProfile profile = DefaultProfile.getProfile("<yourRegionID>", "<yourStsAccesskey>", "<you
rStsAccessSecret>");
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
    // Replace "<yourStsToken>" with the STS token of the AccessKey pair assigned by STS. The STS
token is obtained in the previous step.
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

### 2.3 Obtain API information and the endpoint of an API operation

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
7. Select an API operation and obtain the POP endpoint of the cloud service on the Parameter tab.

## 3 Call examples

### 3.1 Call examples for SDK for Java

#### 3.1.1 Quick start

This topic describes how to obtain and use Apsara Stack SDK for Java.

**Prerequisites**

An Apsara Stack tenant account that has the required permissions and an AccessKey pair that consists of an AccessKey ID and an AccessKey secret are obtained before you can use Apsara Stack SDK for Java. You can view and obtain your AccessKey pair in the Apsara Uni-manager Management Console. For more information, see Obtain an AccessKey pair. The endpoint of a service is obtained. For more information, see Obtain an endpoint. Java Development Kit (JDK) 1.8 or later is installed.

**Installation**

If you use Apache Maven to manage a Java project, you need to only import the JAR file of Apsara Stack SDK for Java to the pom.xml file of the project. If you want to use Apsara Stack Security SDK for Java, you must install the core library of Apsara Stack SDK for Java. We recommend that you use V4.5.17 or later of the core library.

**Usage**

To use Apsara Stack SDK for Java, perform the following steps:
1. Create a DefaultAcsClient instance and initialize the instance.
2. Create an API request and specify the required parameters.
3. Initiate the API request and manage the response or exceptions.

**Note**

In the following sample code, replace the variables with actual values based on your business requirements and remove the angle brackets (<>) from the final code. Variables: <your-region-id>: Replace this variable with the region ID. <your-access-key-id>: Replace this variable with your AccessKey ID. <your-access-key-secret>: Replace this variable with your AccessKey secret. <your-endpoint>: Replace this variable with the endpoint of the service. <API-version>: Replace this variable with the version of the API. <your-action>: Replace this variable with the name of the API operation.

```java
import com.aliyuncs.CommonRequest; import com.aliyuncs.CommonResponse; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.exceptions.ServerException; import com.aliyuncs.profile.DefaultProfile; public class Sample {
    public static void main(String[] args) {
        // Create a DefaultAcsClient instance and initialize the instance.
        DefaultProfile profile = DefaultProfile.getProfile(
            "<your-region-id>",          // The ID of the region.
            "<your-access-key-id>",      // The AccessKey ID.
            "<your-access-key-secret>"); // The AccessKey secret.
        IAcsClient client = new DefaultAcsClient(profile);
        // Create an API request and configure parameters.
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

#### 3.1.2 Use SDK

##### 3.1.2.1 Install SDK for Java

This topic describes how to install and use Apsara Stack Security SDK for Java. Apsara Stack SDK for Java supports Java Development Kit (JDK) 1.8 or later. You can install Apsara Stack SDK for Java by adding Maven dependencies or downloading the SDK. For more information, visit Alibaba Cloud SDKs. If you want to use Apsara Stack Security SDK for Java, you must install the core library of Apsara Stack SDK for Java. We recommend that you use V4.5.17 or later of the core library. When you install the core library, you must add the following dependency to the pom.xml file. For more information about the specific SDK version, visit Alibaba Cloud SDKs.

```xml
<!-- Alibaba Cloud SDK for Java --> <dependency>
    <groupId>com.aliyun</groupId>
    <artifactId>aliyun-java-sdk-core</artifactId>
    <version>4.5.17</version>
</dependency>
```

##### 3.1.2.2 Use CommonRequest

Before you call the SDK for Java to access the endpoint of a cloud service by using the Point of Presence (POP) gateway, you must familiarize yourself with the call style of the cloud service. The following call styles are supported: remote procedure call (RPC) and resource-oriented architecture (ROA).

**Prerequisites**

We recommend that you use CommonRequest to call Apsara Stack API operations. To view the recommended SDK version and sample code, perform the following operations: Log in to the Apsara Unimanager Management Console. In the top navigation bar, choose **Products** > **Development Tools** > **API**
**& SDK** > **OpenAPI Explorer**. In the top navigation bar of the page that appears, choose **API Integration** >
**API Debugging**.

**Important**

We recommend that you do not download SDKs fromSDK Centerand use them in Apsara Stack. SDKs for the Alibaba Cloud public cloud may not support Apsara Stack API operations and may have compatibility issues. Proceed with caution.

**Use CommonRequest to call API operations**

The following sample code provides an example on how to call RPC API operations. In this example, the DescribeApiGroups operation of API Gateway is called, and the API version is 2016-07-14. Sample code:

```java
import com.aliyuncs.CommonRequest; import com.aliyuncs.CommonResponse; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.exceptions.ServerException; import com.aliyuncs.http.MethodType; import com.aliyuncs.profile.DefaultProfile; public class DescribeApiGroups {
    public static void main(String[] args) {
        // Create a DefaultAcsClient instance and initialize the instance.
        DefaultProfile profile = DefaultProfile.getProfile("<your-regionid>", "<yourAccessKeyId>", "<y
ourAccessSecret>");
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
        // Specify the name of the service that you want to access and the region where the service re
sides.
        request.setSysLocationProduct("apigateway");
        // Specify the name of the API operation.
        request.setSysAction("DescribeApiGroups");
```

`//`

```java
        // If you use access credentials assigned by Security Token Service (STS) to call RPC API oper
ations, you must specify the SecurityToken parameter.
        // request.putBodyParameter("SecurityToken", "<your-SecurityToken>");
        // Configure service-related parameters.
        request.putQueryParameter("PageSize", "10");
        request.putQueryParameter("PageNumber", "1");
        // Required. Specify the call source.
        request.putHeadParameter("x-acs-caller-sdk-source", "ApiTestDemo");
        // Optional. The region ID. This parameter is required for Apsara Stack V3.15.0 and earlier.
        request.putHeadParameter("x-acs-regionid", "<your-regionid>");
        // Optional. Specify the ID of the resource set.
        request.putHeadParameter("x-acs-resourcegroupid", "<your-resourcegroupid>");
        // Required. Specify the organization ID.
        request.putHeadParameter("x-acs-organizationid", "<your-organizationid>");
        // Optional. The instance ID. This parameter is required for the modify and delete
operations.
        // request.putHeadParameter("x-acs-instanceid", "<your-instanceid>");
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

`}` `}` `}` The following sample code provides an example on how to call ROA API operations. In this example, the GetNamespaceList operation of Container Registry is called, and the API version is 2016-06-07. Sample code:

```java
import com.aliyuncs.CommonRequest; import com.aliyuncs.CommonResponse; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.exceptions.ServerException; import com.aliyuncs.http.MethodType; import com.aliyuncs.profile.DefaultProfile; public class GetNamespaceList {
    public static void main(String[] args) {
        // Create a DefaultAcsClient instance and initialize the instance.
        DefaultProfile profile = DefaultProfile.getProfile("<your-regionid>", "<yourAccessKeyId>", "<y
ourAccessSecret>");
        // Ignore SSL certificate verification.
        // HttpClientConfig clientConfig = HttpClientConfig.getDefault();
        // clientConfig.setIgnoreSSLCerts(true);
        // Specify the timeout period for a connection.
        // clientConfig.setConnectionTimeoutMillis(3000L);
        // Specify the read timeout period.
        // clientConfig.setReadTimeoutMillis(10000L);
//profilesetHttpClientConfig(clientConfig)
```

```java
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
        request.setSysUriPattern("/namespace");
        // Specify the name of the service that you want to access and the region where the service re
sides.
        request.setSysLocationProduct("cr");
        // Specify the name of the API operation.
        request.setSysAction("GetNamespaceList");
        // Required. Specify the call source.
        request.putHeadParameter("x-acs-caller-sdk-source", "ApiTestDemo");
        // Optional. The region ID. This parameter is required for Apsara Stack V3.15.0 and earlier.
        request.putHeadParameter("x-acs-regionid", "<your-regionid>");
        // Optional. Specify the ID of the resource set.
        request.putHeadParameter("x-acs-resourcegroupid", "<your-resourcegroupid>");
        // Required. Specify the organization ID.
        request.putHeadParameter("x-acs-organizationid", "<your-organizationid>");
        // Optional. The instance ID. This parameter is required for the modify and delete
operations.
        // request.putHeadParameter("x-acs-instanceid", "<your-instanceid>");
        // If you use access credentials assigned by STS to call ROA API operations, you must add the
x-acs-security-token field to the header.
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

**Important**

By default, if you send API requests over HTTPS, the SDK enables certificate verification to verify the validity of SSL/TLS certificates. If no certificate is configured in the development environment, an error that indicates the certificate verification fails is reported. To ensure communication security in the production environment, we recommend that you enable certificate verification. If certificate verification must be disabled in the test environment, you can specify the following setting: Java

```
HttpClientConfig clientConfig = HttpClientConfig.getDefault(); // Disable server certificate verification. clientConfig.setIgnoreSSLCerts(true)
```

### 3.2 Call examples for SDK for Python

#### 3.2.1 Quick start

This topic describes how to obtain and use Apsara Stack SDK for Python.

**Prerequisites**

An Apsara Stack tenant account that has the required permissions and an AccessKey pair that consists of an AccessKey ID and an AccessKey secret are obtained before you can use Apsara Stack SDK for Python. For more information, see Obtain an AccessKey pair. The endpoint of a service is obtained. For more information, see Obtain an endpoint.

**Installation**

If you use Python 2.x, run the following command to install the core library of Apsara Stack SDK for Python:

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
3. Initiate the API request and manage the response or exceptions.

**Note**

In the following sample code, replace the variables with actual values based on your business requirements and remove the angle brackets (<>) from the final code. The following list describes the variables: <your_region_id>: Replace this variable with the region ID. <your_access_key_id>: Replace this variable with your AccessKey ID. <your_access_key_secret>: Replace this variable with your AccessKey secret. <your-endpoint>: Replace this variable with the endpoint of the service. <API-version>: Replace this variable with the version of the API. <your-action>: Replace this variable with the name of the API operation.

```bash
from aliyunsdkcore.client import AcsClient from aliyunsdkcore.request import CommonRequest client = AcsClient('{your_access_key_id}','{your_access_key_secret}', '{your_region_id}') request = CommonRequest() request.set_domain('<your-endpoint>') # The endpoint of the service. request.set_version('<API-version>') # The version of the API. request.set_action_name('<your-action>') # The name of the API operation.
# or request = CommonRequest(domain='<your-endpoint>', version='<API-version>',action_name='<your-ac
tion>') request.add_query_param('PageNumber', '1') request.add_query_param('PageSize', '30') response = client.do_action_with_exception(request)
```

#### 3.2.2 Use SDK

##### 3.2.2.1 Install SDK for Python

This topic describes how to install and use SDK for Python. Apsara Stack SDK for Python supports Python 2.6.x, Python 2.7.x, and Python 3.x or later. You can install Apsara Stack SDK for Python by using pip.

**Note**

To use the SDK of an Apsara Stack service, you must install the core library of Apsara Stack SDK for Python. If you use Python 2.x, run the following command to install the core library:

```
pip install aliyun-python-sdk-core
```

If you use Python 3.x, run the following command to install the core library:

```
pip3 install aliyun-python-sdk-core-v3
```

##### 3.2.2.2 Use CommonRequest

This topic describes how to use the POP Python software development kit (SDK) to call cloud product APIs.

**Prerequisites**

In Apsara Stack, use CommonRequest to make API calls. You can find the recommended SDK version and sample code in the Apsara Uni-manager Management Console. To do this, navigate to **Products** >
**Development Tools** > **API And Tools** > **Developer Portal** and select **API Integration** > **API**
**Debugging**.

**Important**

Do not download SDKs directly from the SDK Center for Apsara Stack scenarios. The SDKs for the public cloud may not support Apsara Stack APIs or have compatibility issues. Use them with caution.

**Background information**

Currently, you can call APIs only using the Remote Procedure Call (RPC) method.

**CommonRequest call example**

The following example shows how to call the DescribeInstances operation of ECS. The API version is 2014-05- 26. The following is the sample code:

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

```python
# Use with HTTPS.
# client.set_verify(False)
# os.environ["HTTPS_PROXY"] = "http://127.0.0.1:8080"
# os.environ["HTTP_PROXY"] = "http://127.0.0.1:8080"
def describe_api_groups():
    # Create a request and set its parameters.
    request = CommonRequest()
    # When you call an RPC API using an STS AccessKey pair, add the SecurityToken field to the paramet
ers.
    # params = {"PageSize":"10","PageNumber":"1","SecurityToken":"<your-SecurityToken>"};
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
    request.set_endpoint("<ApigatewayEndpoint>")   // Replace <ApigatewayEndpoint> with the actual end
point.
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

**Important**

When you access OpenAPI using the HTTPS protocol, the SDK verifies the SSL/TLS certificate by default. If your code environment does not have a certificate, a certificate verification error is reported. To ensure secure communication in a production environment, keep this verification enabled. If you must ignore certificate verification in a test environment, set the `verify` parameter.

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

### 3.3 Call examples for SDK for Go

#### 3.3.1 Quick start

Apsara Stack SDK for Go allows you to access services without complex coding. This topic describes how to obtain and use Apsara Stack SDK for Go.

**Prerequisites**

An Apsara Stack tenant account that has the required permissions and an AccessKey pair that consists of an AccessKey ID and an AccessKey secret are obtained before you can use Apsara Stack SDK for Go. You can view and obtain your AccessKey pair in the Apsara Uni-manager Management Console. For more information, see Obtain an AccessKey pair. The endpoint of a service is obtained. For more information, see Obtain an endpoint.

**Install the core package of Apsara Stack SDK for Go**

Apsara Stack SDK for Go supports Go 1.10.x and later. You can run the following command to install the core library:

```
go get -u github.com/aliyun/alibaba-cloud-sdk-go/sdk
```

**Use Apsara Stack SDK for Go**

To use Apsara Stack SDK for Go, perform the following steps:
1. Initialize a client instance.
2. Create an API request and specify the required parameters.
3. Initiate the API request and manage the response or exceptions.

**Note**

In the following sample code, replace the variables with actual values based on your business requirements and remove the angle brackets (<>) from the final code. Variables: <your_region_id>: Replace this variable with the region ID. <your_access_key_id>: Replace this variable with your AccessKey ID. <your_access_key_secret>: Replace this variable with your AccessKey secret. <your-endpoint>: Replace this variable with the endpoint of the service. <API-version>: Replace this variable with the version of the API. <your-action>: Replace this variable with the name of the API operation.

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

#### 3.3.2 Use SDK

##### 3.3.2.1 Install the core package of SDK for Go

This topic describes how to install the core package of SDK for Go. Apsara Stack SDK for Go supports Go 1.10.x and later. You can run the following command to install the core package:

```
go get -u github.com/aliyun/alibaba-cloud-sdk-go/sdk
```

##### 3.3.2.2 Use CommonRequest

This topic describes how to use the POP Go software development kit (SDK) to make API calls.

**Prerequisites**

For Apsara Stack, use CommonRequest to make API calls. In the Apsara Uni-manager Management Console, go to **Products** > **Development Tools** > **API And Tools** > **Developer Portal**. Then, choose **API**
**Integration** > **API Debugging** to view the recommended SDK versions and sample code.

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
    client, err := sdk.NewClientWithAccessKey("<your-RegionID>", "<AccessKey ID>", "<AccessKey secret>
```

`")`

```
    request := requests.NewCommonRequest()
    request.Method = "POST"
    request.Domain = "<ApigatewayEndpoint>"
    request.Version = "2016-07-14"
    request.ApiName = "DescribeApiGroups"
    request.Product = "apigateway"
    // If you use an STS AccessKey pair to call an RPC API, add the SecurityToken parameter.
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
 // If you use an STS AccessKey pair to call a ROA API, add the x-acs-security-token field to the hea
der.
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
 os.Setenv("HTTP_PROXY", "http://x.x.x.x:xxxx") // Set the HTTP_PROXY environment variable.
 os.Setenv("HTTPS_PROXY", "https://x.x.x.x:xxxx") // Set the HTTPS_PROXY environment variable.
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

**Important**

When you access OpenAPI over HTTPS, the SDK enables SSL certificate validation by default. If your code environment does not have a certificate, a validation error occurs. To ensure secure communication in a production environment, keep this validation enabled. To ignore certificate validation in a test environment, use the following settings.

```
// Set HTTPSInsecure for the request (affects only the current request). request.SetHTTPSInsecure(true) // Set HTTPSInsecure for the request to true. isInsecure := request.GetHTTPSInsecure() // Get the HTTPSInsecure setting for the requ est.
```

The client-level setting takes effect only if the request-level setting is not set.

```
// Set HTTPSInsecure for the client (affects all requests sent by the client). client.SetHTTPSInsecure(true) // Set HTTPSInsecure for the client to true. isInsecure := client.GetHTTPSInsecure() // Get the HTTPSInsecure setting for the client.
```

## 4 Common parameters

**Common request parameters**

Common request parameters must be included in all Apsara Stack API requests. Table 1. Common request parameters

| Parameter | Type | Requir ed | Description |
|---|---|---|---|
| Format | String | No | The type of the returned value. Set the value to JSON. |
| Version | String | Yes | The version number of the API. Specify the version number in the YYYY-MM- DD format. Valid values: 2018-01-16: Auditprivate 2019-07-23: yundunnextsoc 2018-12-03: Sas 2016-11-11: aegis 2021-10-11: yundun-css 2019-08-05: secspy 2018-01-16: Ddosprivate 2018-06-30: hsm-private 2017-12-07: Cloudfw 2019-01-03: Sddp 2020-07-01: semawaf 2018-12-03: soar |
| AccessKeyId | String | Yes | The AccessKey ID that is provided by Apsara Stack. |
| AccessKeySecre t | String | Yes | The AccessKey secret that is provided by Apsara Stack. |
| RegionId | String | Yes | The region ID of the service. |
| Product | String | Yes | The name of the service to which the operation belongs. Valid values: Auditprivate: basic components of Apsara Stack Security yundunnextsoc: Security Operations Center (SOC) Sas: Threat Detection Service aegis: Server Guard yundun-css: Container Protection secspy: Network Detection and Response Ddosprivate: Anti-DDoS Service hsm-private: Data Encryption Service Cloudfw: Cloud Firewall Sddp: Sensitive Data Discovery and Protection (SDDP) semawaf: Web Application Firewall (WAF) soar: Security Orchestration and Automation Response (SOAR) |

| EndpointPre | String | Yes | The prefix in the endpoint of the service to which the operation belongs. Valid values: auditprivate: the prefix in the endpoint of basic components of Apsara Stack Security yundunnextsoc-pop: the prefix in the endpoint of SOC tds: the prefix in the endpoint of Threat Detection Service aegis: the prefix in the endpoint of Server Guard yundun-css: the prefix in the endpoint of Container Protection secspy-share: the prefix in the endpoint of Network Detection and Response ddosprivate: the prefix in the endpoint of Anti-DDoS Service hsmprivate: the prefix in the endpoint of Data Encryption Service cloudfw: the prefix in the endpoint of Cloud Firewall sddp-api: the prefix in the endpoint of SDDP semawaf: the prefix in the endpoint of WAF soar: the prefix in the endpoint of SOAR |
|---|---|---|---|

**Common response parameters**

API responses use the HTTP response format: A 2xx status code indicates a successful call. A 4xx or 5xx status code indicates a failed call. Responses are returned in the JSON format. Every response returns a unique RequestID regardless of whether the call is successful.

## 5 API reference

### 5.1 DescribeLatestScanTask

Queries the progress of the last virus scan task.

**Authorization information**

| Operation | Access level | Resource type |
|---|---|---|
| yundun-css:DescribeLatestScanTask | Read | acs:yundun-css:*:{#accountId}:* |

**Traffic throttling**

You can call this operation up to 10 times per second per account. You can call this operation up to 100 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Uuids | Normal | 78645c8e-2e89-441b- 8eb***,a9622a6b- adb5-4dd3- 929e,0136460a-1cb5- 44e8-**** | The UUIDs. Multiple UUIDs are separated by commas (,). |
| RequestId | String | F0A8A039-930D-5EC1- 97C8-************ | The request ID. |
| LastCheckTime | Long | 1671610264000 | The timestamp when the last check was performed. Unit: milliseconds. |
| RiskNum | Integer | 1 | The number of viruses detected on the server. |

| TargetInfo | String | [{"type":"uuid","name" :"host001","target":"50 3201a7-14c6-4280- 801b-1169ed42****"}] | The information about the asset on which the virus scan task runs. The value is a string that consists of JSON arrays. Each element in a JSON array is a JSON struct that contains the following fields: type: the type of the asset on which the virus scan task runs. Valid values: groupId: server group. uuid: server. name: the name of the server group or server. target: the asset on which the virus scan task runs. The value of this field varies based on the value of the type field. If the value of type is groupId, the value of this field is the ID of the server group. If the value of type is uuid, the value of this field is the UUID of the server. |
|---|---|---|---|

**Examples**

Sample requests

```
https://[Endpoint]/?Action=DescribeLatestScanTask&RegionId=cn-hangzhou
```

Sample success responses `JSON` format

```
HTTP/1.1 200 OK Content-Type:application/json
```

`{`

```json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "LastCheckTime":1671610264000,
    "RiskNum":1,
    "TargetInfo":"[{\"type\":\"uuid\",\"name\":\"host001\",\"target\":\"503201a7-14c6-4280-801b-1169ed
42****\"}]",
    "Uuids":"78645c8e-2e89-441b-8eb***,a9622a6b-adb5-4dd3-929e,0136460a-1cb5-44e8-****"
```

`}` `XML` format

```xml
HTTP/1.1 200 OK Content-Type:application/xml <DescribeLatestScanTaskResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <LastCheckTime>1671610264000</LastCheckTime>
    <RiskNum>1</RiskNum>
    <TargetInfo>[{"type":"uuid","name":"host001","target":"503201a7-14c6-4280-801b-1169ed42****"}]</Ta
rgetInfo>
    <Uuids>
        <uuid>78645c8e-2e89-441b-8eb***,a9622a6b-adb5-4dd3-929e,0136460a-1cb5-44e8-****</uuid>
    </Uuids>
</DescribeLatestScanTaskResponse>
```

### 5.2 ListImageRisk

Queries security information about a container image.

**Authorization information**

| Operation | Access level | Resource type |
|---|---|---|
| yundun-css:ListImageRisk | Read | acs:yundun-css:*:{#accountId}:* |

**Traffic throttling**

You can call this operation up to 10 times per second per account. You can call this operation up to 100 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parameter | Type | Positi on | Required | Example | Description |
|---|---|---|---|---|---|
| CurrentPage | Intege r | Query | No | 1 | The page number. |
| PageSize | Intege r | Query | No | 20 | The number of entries per page. Default value: 20. |
| ClusterId | String | Query | No | c80f79959fd724a888e118777 9b13**** | The ID of the cluster to which the container belongs. |
| Namespace | String | Query | No | kube-sy**** | The namespace to which the image repository belongs. |
| AppName | String | Query | No | e**** | The application name. |
| ImageName | String | Query | No | container-***:**** | The image name. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| ImageRiskList | Array |   | The security information about the image. |
| -EndPointList | Array |   | The details of the endpoint. |
| --Domains | String | ['xxx.com','aaa.com'] | The details of the domain name in the endpoint. |
| --Type | String | internet | The type of the domain name in the endpoint. Valid values: internet intranet |

| -RepoNamespace | String | vultar*** | The namespace to which the image repository belongs. |
|---|---|---|---|
| -RepoName | String | scan test _ | The name of the image repository. |
| -Tag | String | 0.1.0 | The image tag. |
| -RegionId | String | cn-hangzhou | The region of the image repository. |
| -Digest | String | 3f8efc2184cf1d24936b 49c27286a284714b77 be34c80c9ee38ca6bf3 22445**** | The digest value of the image. |
| -RepoId | String | crr-bk2l746eyxca1**** | The ID of the image repository. |
| -RepoType | String | PRIVATE | The type of the repository. Valid values: PUBLIC PRIVATE |
| -RegistryType | String | harbor | The type of the image repository. Valid values: acr: Container Registry. harbor: Harbor. quay: Quay. CI/CD: Jenkins. |
| -Endpoints | String | https://172.20.XXX.XX X/test | The endpoint of Container Registry. |
| -ImageId | String | f922bfeb6960436fe3f0 e7b62fc6b9a0b479809 86669c367c22433269 404**** | The image ID. |
| -TagImmutable | Integer | 0 | Indicates whether the image version is immutable. If the image version is immutable, only the image of the latest version in the image repository can be overwritten. Valid values: 0: yes. 1: no. |
| -Statistics | String | { "baselineNum": 0, "newSuspicious": 0, "vul": 0 } | The statistics on a security event. |
| - ImageAccessType | String | IN SAS _ | The registration status of the image repository. Valid values: IN SAS: The image repository is registered with _ Security Center. NOT IN SAS: The image repository is not _ _ registered with Security Center. |

| -Image | String | .aliyuncs.com/sas test/ _ baseline:exploit | The image. |
|---|---|---|---|
| -Uuid | String | 624778f3-5bf2-423c- ac0c-47a62c05**** | The UUID of the image. |
| -InternetURLs | String | ****registry- registry.cn-shenzhen- finance- 1.cr.aliyuncs.com/xxxx /docker-**** | The public endpoint of the image repository. |
| -VpcURLs | String | ****-registry-registry- vpc.cn-shenzhen- finance- 1.cr.aliyuncs.com/xxxx /docker-**** | The endpoint of the image repository in the virtual private cloud (VPC). |
| -OrgId | String | 12 | The organization ID. |
| -ResourceSetId | String | 12 | The ID of the resource set. |
| RequestId | String | F0A8A039-930D-5EC1- 97C8-************ | The request ID. |
| PageInfo | Struct |   | The pagination information. |
| -TotalCount | Integer | 23 | The total number of entries returned. |
| -Count | Integer | 3 | The number of entries on the current page. |
| -PageSize | Integer | 20 | The number of entries per page. |
| -CurrentPage | Integer | 1 | The page number. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=ListImageRisk&RegionId=cnhangzhou&CurrentPage=1&PageSize=20&ClusterId=c80f79959fd724a888e1187779b13****&Namespace=kube-sy****&A ppName=e****&ImageName=container-***:****
```

Sample success responses `JSON` format

```
HTTP/1.1 200 OK Content-Type:application/json
```

`{`

```json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "ImageRiskList":[
```

`{`

```json
            "ImageAccessType":"IN_SAS",
            "RepoNamespace":"vultar***",
            "RegistryType":"harbor",
            "Digest":"3f8efc2184cf1d24936b49c27286a284714b77be34c80c9ee38ca6bf322445****",
            "RepoName":"scan_test",
            "TagImmutable":0,
            "Image":".aliyuncs.com/sas_test/baseline:exploit",
            "Statistics":"{ \"baselineNum\": 0, \"newSuspicious\": 0, \"vul\": 0 }",
            "InternetURLs":"****registry-registry.cn-shenzhen-finance-1.cr.aliyuncs.com/xxxx/docker-**
**",
            "Endpoints":"https://172.20.XXX.XXX/test",
            "OrgId":"12",
            "Uuid":"624778f3-5bf2-423c-ac0c-47a62c05****",
            "RepoType":"PRIVATE",
            "EndPointList":[
```

`{`

```json
                    "Domains":[
                        "xxx.com",
                        "aaa.com"
```

`],`

```json
                    "Type":"internet"
```

`}` `],`

```json
            "ImageId":"f922bfeb6960436fe3f0e7b62fc6b9a0b47980986669c367c22433269404****",
            "Tag":"0.1.0",
            "RegionId":"cn-hangzhou",
            "RepoId":"crr-bk2l746eyxca1****",
            "VpcURLs":"****-registry-registry-vpc.cn-shenzhen-finance-1.cr.aliyuncs.com/xxxx/docker-**
**",
            "ResourceSetId":"12"
```

`}` `],`

```json
    "PageInfo":{
        "TotalCount":23,
        "PageSize":20,
        "CurrentPage":1,
        "Count":3
```

`}` `}` `XML` format

```xml
HTTP/1.1 200 OK Content-Type:application/xml <ListImageRiskResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <ImageRiskList>
        <RepoNamespace>vultar***</RepoNamespace>
        <RepoName>scan_test</RepoName>
        <Tag>0.1.0</Tag>
        <RegionId>cn-hangzhou</RegionId>
        <Digest>3f8efc2184cf1d24936b49c27286a284714b77be34c80c9ee38ca6bf322445****</Digest>
        <RepoId>crr-bk2l746eyxca1****</RepoId>
        <RepoType>PRIVATE</RepoType>
        <RegistryType>harbor</RegistryType>
        <Endpoints>https://172.20.XXX.XXX/test</Endpoints>
        <ImageId>f922bfeb6960436fe3f0e7b62fc6b9a0b47980986669c367c22433269404****</ImageId>
        <TagImmutable>0</TagImmutable>
        <Statistics>{ "baselineNum": 0, "newSuspicious": 0, "vul": 0 }</Statistics>
        <ImageAccessType>IN_SAS</ImageAccessType>
        <Image>.aliyuncs.com/sas_test/baseline:exploit</Image>
        <Uuid>624778f3-5bf2-423c-ac0c-47a62c05****</Uuid>
        <InternetURLs>****registry-registry.cn-shenzhen-finance-1.cr.aliyuncs.com/xxxx/docker-****</In
ternetURLs>
        <VpcURLs>****-registry-registry-vpc.cn-shenzhen-finance-1.cr.aliyuncs.com/xxxx/docker-****</Vp
cURLs>
        <OrgId>12</OrgId>
        <ResourceSetId>12</ResourceSetId>
        <EndPointList>
            <Type>internet</Type>
            <Domains>
                <domain>['xxx.com','aaa.com']</domain>
            </Domains>
        </EndPointList>
    </ImageRiskList>
    <PageInfo>
        <TotalCount>23</TotalCount>
        <Count>3</Count>
        <PageSize>20</PageSize>
        <CurrentPage>1</CurrentPage>
    </PageInfo>
</ListImageRiskResponse>
```

### 5.3 UpdateJenkinsImageScanTaskStatus

Changes the status of the scan task on a Jenkins image repository.

**Authorization information**

| Operation | Access level | Resource type |
|---|---|---|
| yundun- css:UpdateJenkinsImageScanTaskStat us | Write | acs:yundun-css:*:{#accountId}:* |

**Traffic throttling**

You can call this operation up to 10 times per second per account. You can call this operation up to 100 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parameter | Type | Positio n | Required | Example | Description |
|---|---|---|---|---|---|
| Token | String | Body | No | 3c3c602c-fa1f-4bc0-992f- b4b2cac7**** | The value of the token. |
| TaskId | String | Body | No | e900f528f5a6229bb640ca27c b44c98e | The task ID. |
| Result | String | Body | No | SUCCESS | The result of the scan task. Valid values: SUCCESS: The scan task is successful. TASK NOT SUPPORT REGIO _ _ _ N: The image is deployed in a region that is not supported by container image scan. TASK NOT EXISTS: The _ _ scan task does not exist. |
| Status | String | Body | No | START | The status of the scan task. Valid values: START SUCCESS FAIL TIMEOUT |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D-5EC1- 97C8-************ | The request ID. |
| TimeCost | Long | 1 | The time consumed. Unit: seconds. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=UpdateJenkinsImageScanTaskStatus&RegionId=cn-hangzhou&Token=3c3c602c-fa1f-4 bc0-992f-b4b2cac7****&TaskId=e900f528f5a6229bb640ca27cb44c98e&Result=SUCCESS&Status=START
```

Sample success responses `JSON` format

```
HTTP/1.1 200 OK Content-Type:application/json
```

`{`

```json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "TimeCost":1
```

`}` `XML` format

```xml
HTTP/1.1 200 OK Content-Type:application/xml <UpdateJenkinsImageScanTaskStatusResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <TimeCost>1</TimeCost>
</UpdateJenkinsImageScanTaskStatusResponse>
```

### 5.4 DescribeImageInfoList

Queries the information about images.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeImageInfoL ist | The operation that you want to perform. Set the value to DescribeImageInfoList. |
| Uuids | String | Yes | UUID1,UUID2,UUID3 | The UUIDs of the images. Separate multiple UUIDs with commas (,). |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| ImageInfos | Array of ImageInfo |   | An array that consists of the information about the images. |
| AlarmCount | Integer | 1 | The number of exceptions. |
| AlarmStatus | String | NO | Indicates whether alerts are triggered. Valid values: YES NO |
| Digest | String | 6a5e1031a5858617f7d 8a179ead6*** | The digest of the image. |
| Endpoints | String | [] | The endpoint of the image. |
| ImageCreate | Long | 1639236844747 | The time when the image was created. The value is a UNIX timestamp. Unit: milliseconds. |
| ImageId | String | asdaSdasd****** | The ID of the image. |

| ard Advanced Edit | ion |   | oper Guide·API reference |
|---|---|---|---|

| ImageSize | Long | 100 | The size of the image. |
|---|---|---|---|
| ImageUpdate | Long | 1639236844747 | The time when the image was updated. The value is a UNIX timestamp. Unit: milliseconds. |
| InstanceId | String | i-km100o6qy8gid***** | The ID of the instance. |
| RegionId | String | cn-wu***-env***- d01*** | The region ID. |
| RegistryType | String | defaultAcr | The type of the registration. |
| RepoId | String | crr-vridcl4**** | The ID of the image repository. |
| RepoName | String | centos | The name of the image repository. |
| RepoNamespace | String | hang***-namespace | The namespace to which the image repository belongs. |
| RepoType | String | PRIVATE | The type of the image repository. The value is fixed as PRIVATE. |
| RiskStatus | String | YES | Indicates whether risks are detected. Valid values: YES NO |
| Status | String | NORMAL | The status of the image. |
| Tag | String | 0.2 | The tag that is added to the image. |
| TagImmutable | Integer | 1 | The label that cannot be changed. |
| Uuid | String | B41B****-337A-472D- B82E-9FD3642B8*** | The UUID of the image. |
| VulCount | Integer | 1 | The number of vulnerabilities that are detected in the image. |
| VulStatus | String | YES | Indicates whether vulnerabilities are detected. Valid values: YES NO |
| RequestId | String | B41B****-337A-472D- B82E-9FD3642B**** | The ID of the request. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeImageInfoList &Uuids=UUID1,UUID2,UUID3 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ImageInfos>
    <Status>NORMAL</Status>
    <RepoNamespace>hang***-namespace</RepoNamespace>
    <RegistryType>defaultAcr</RegistryType>
    <VulStatus>YES</VulStatus>
    <ImageSize>100</ImageSize>
    <Digest>6a5e1031a5858617f7d8a179ead6***</Digest>
    <InstanceId>i-km100o6qy8gid*****</InstanceId>
    <TagImmutable>1</TagImmutable>
    <RepoName>centos</RepoName>
    <RiskStatus>YES</RiskStatus>
    <VulCount>1</VulCount>
    <Endpoints>[]</Endpoints>
    <Uuid>B41B****-337A-472D-B82E-9FD3642B8***</Uuid>
    <ImageCreate>1639236844747</ImageCreate>
    <RepoType>PRIVATE</RepoType>
    <AlarmStatus>NO</AlarmStatus>
    <ImageId>asdaSdasd******</ImageId>
    <ImageUpdate>1639236844747</ImageUpdate>
    <Tag>0.2</Tag>
    <RegionId>cn-wu***-env***-d01***</RegionId>
    <RepoId>crr-vridcl4****</RepoId>
    <AlarmCount>1</AlarmCount>
</ImageInfos> <RequestId>B41B****-337A-472D-B82E-9FD3642B****</RequestId>
```

`JSON` format `{`

```json
    "ImageInfos": {
        "Status": "NORMAL",
        "RepoNamespace": "hang***-namespace",
        "RegistryType": "defaultAcr",
        "VulStatus": "YES",
        "ImageSize": 100,
        "Digest": "6a5e1031a5858617f7d8a179ead6***",
        "InstanceId": "i-km100o6qy8gid*****",
        "TagImmutable": 1,
        "RepoName": "centos",
        "RiskStatus": "YES",
        "VulCount": 1,
        "Endpoints": "[]",
        "Uuid": "B41B****-337A-472D-B82E-9FD3642B8***",
        "ImageCreate": 1639236844747,
        "RepoType": "PRIVATE",
        "AlarmStatus": "NO",
        "ImageId": "asdaSdasd******",
        "ImageUpdate": 1639236844747,
        "Tag": 0.2,
        "RegionId": "cn-wu***-env***-d01***",
        "RepoId": "crr-vridcl4****",
        "AlarmCount": 1
```

`},`

```json
    "RequestId": "B41B****-337A-472D-B82E-9FD3642B****"
```

`}`

**5.5.**

### DescribeImageBaselineCheckSummary

Queries image baseline check results.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeImageBase lineCheckSummary | The operation that you want to perform. Set the value to DescribeImageBaselineCheckSummary. |
| RiskLevel | String | No | high,medium,low | The severity of the image baseline risk. Separate multiple severities with commas (,). Valid values: high medium low |

| Criteria | String | No | [{\"name\":\"riskSta tus\",\"value\":\"YES \"}, {\"name\":\"internet Ip\",\"value\":\"1.2.3 .4\"}] | The search conditions for assets. Set the value in the following format: [{\"name\":\"Name of Condition 1\",\"value\":\"Value of Condition 1\"},{\"name\":\"Name of Condition 2\",\"value\":\"Value of Condition 2\"},{},...] |
|---|---|---|---|---|
| CriteriaType | String | No | BaselineClassAlias | The type of the query condition. Valid values: BaselineClassAlias: baseline category BaselineNameAlias: baseline name |
| PageSize | Integer | No | 20 | The number of entries to return on each page. |
| CurrentPage | Integer | No | 1 | The number of the page to return. |
| Lang | String | No | zh | The language of the content within the request and response. Valid values: zh: Chinese en: English |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| BaselineResultSu mmary | Array of BaselineResultSu mmary |   | An array that consists of the image baseline check results. |
| BaselineClassAlia s | String | Identity authentication | The category of the baseline. |
| BaselineClassKey | String | identification | The key of the baseline category. |
| BaselineNameAlia s | String | Identity authentication | The name of the baseline. |
| BaselineNameKe y | String | identification | The key of the baseline name. |
| BaselineNameLev el | String | high | The severity of the baseline. |
| FirstScanTime | Long | 1639236844747 | The time when the first image baseline check was performed. The value is a UNIX timestamp. Unit: milliseconds. |

| HighRiskImage | Integer | 1 | The number of images on which high baseline risks are detected. |
|---|---|---|---|
| LastScanTime | Long | 1639236844747 | The time when the last image baseline check was performed. The value is a UNIX timestamp. Unit: milliseconds. |
| LowRiskImage | Integer | 2 | The number of images on which low baseline risks are detected. |
| MiddleRiskImage | Integer | 3 | The number of images on which medium baseline risks are detected. |
| Status | Integer | 0 | The status of the baseline. Valid values: 0: normal 1: abnormal |
| PageInfo | Struct |   | The pagination information. |
| Count | Integer | 18 | The total number of returned pages. |
| CurrentPage | Integer | 1 | The page number of the returned page. |
| PageSize | Integer | 20 | The number of entries returned per page. |
| TotalCount | Integer | 18 | The total number of entries returned. |
| RequestId | String | B41B3780-337A-472D- B82E-9FD3642B9350 | The ID of the request. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeImageBaselineCheckSummary &<Common request parameters>
```

Sample success responses `XML` format

```xml
<PageInfo>
    <TotalCount>18</TotalCount>
    <PageSize>20</PageSize>
    <CurrentPage>1</CurrentPage>
    <Count>18</Count>
</PageInfo> <RequestId>B41B3780-337A-472D-B82E-9FD3642B9350</RequestId> <BaselineResultSummary>
    <Status>0</Status>
    <BaselineClassKey>identification</BaselineClassKey>
    <FirstScanTime>1639236844747</FirstScanTime>
    <LowRiskImage>2</LowRiskImage>
    <BaselineClassAlias>Identity authentication</BaselineClassAlias>
    <BaselineNameAlias>Identity authentication</BaselineNameAlias>
    <MiddleRiskImage>3</MiddleRiskImage>
    <HighRiskImage>1</HighRiskImage>
    <BaselineNameLevel>high</BaselineNameLevel>
    <LastScanTime>1639236844747</LastScanTime>
    <BaselineNameKey>identification</BaselineNameKey>
</BaselineResultSummary>
```

`JSON` format `{`

```json
    "PageInfo": {
        "TotalCount": 18,
        "PageSize": 20,
        "CurrentPage": 1,
        "Count": 18
```

`},`

```json
    "RequestId": "B41B3780-337A-472D-B82E-9FD3642B9350",
    "BaselineResultSummary": {
        "Status": 0,
        "BaselineClassKey": "identification",
        "FirstScanTime": 1639236844747,
        "LowRiskImage": 2,
        "BaselineClassAlias": "Identity authentication",
        "BaselineNameAlias": "Identity authentication",
        "MiddleRiskImage": 3,
        "HighRiskImage": 1,
        "BaselineNameLevel": "high",
        "LastScanTime": 1639236844747,
        "BaselineNameKey": "identification"
```

`}` `}`

**5.6.**

### DescribeImageListWithBaselineName

Queries baseline check results.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeImageList WithBaselineName | The operation that you want to perform. Set the value to DescribeImageListWithBaselineName. |

| BaselineNameKey | String | Yes | identification | The key of the baseline name. |
|---|---|---|---|---|
| Criteria | String | No | [{\"name\":\"riskSta tus\",\"value\":\"YES \"}, {\"name\":\"internet Ip\",\"value\":\"1.2.3 .4\"}] | The search conditions for assets. Set the value in the following format: [{\"name\":\"Name of Condition 1\",\"value\":\"Value of Condition 1\"},{\"name\":\"Name of Condition 2\",\"value\":\"Value of Condition 2\"},{},...] |
| CriteriaType | String | No | BaselineNameAlias | The type of the query condition. Valid values: BaselineClassAlias: baseline category BaselineNameAlias: baseline name |
| RepoInstanceId | String | No | cri-datvailb**** | The ID of the Container Registry instance. |
| RepoName | String | No | centos | The name of the image repository. |
| RepoNamespace | String | No | hanghai- namespace | The namespace to which the image repository belongs. |
| ImageDigest | String | No | 6a5e103187b31a94 592a47a5858617f7 a179ead61df7606* *** | The digest of the image. |
| PageSize | Integer | No | 20 | The number of entries to return on each page. |
| CurrentPage | Integer | No | 1 | The number of the page to return. |
| Lang | String | No | zh | The language of the content within the request and response. Valid values: zh: Chinese en: English |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| ImageInfos | Array of ImageInfos |   | An array that consists of the information about the image. |
| Digest | String | 6a5e1031a5858617f7d 8a179ead6**** | The digest of the image. |
| Endpoints | String | [] | The endpoint of the image. |
| HighRiskImage | Integer | 1 | The number of images on which high baseline risks are detected. |

| ImageCreate | Long | 1639236844747 | The time when the image was created. The value is a UNIX timestamp. Unit: milliseconds. |
|---|---|---|---|
| ImageId | String | asdaSdasd*** | The ID of the image. |
| ImageSize | Integer | 212 | The size of the image. |
| ImageUpdate | Long | 1639236844747 | The time when the image was updated. The value is a UNIX timestamp. Unit: milliseconds. |
| InstanceId | String | i- km100o6qy8gidwn3*** * | The ID of the instance. |
| LowRiskImage | Integer | 2 | The number of images on which low baseline risks are detected. |
| MiddleRiskImage | Integer | 3 | The number of images on which medium baseline risks are detected. |
| NoRiskImage | Integer | 3 | The number of images on which no baseline risks are detected. |
| RegionId | String | cn-wulan-env116- d01*** | The region ID. |
| RepoId | String | crr-vridcl4**** | The ID of the image repository. |
| RepoName | String | centos1 | The name of the image repository. |
| RepoNamespace | String | hanghai-namespace | The namespace to which the image repository belongs. |
| RepoType | String | PRIVATE | The type of the image repository. The value is fixed as PRIVATE. |
| RiskStatus | String | YES | Indicates whether risks are detected. Valid values: YES NO |
| Tag | String | 0.2 | The tag that is added to the image. |
| TotalItemCount | Integer | 1 | The total number of images. |
| Uuid | String | B41B3780-337A-472D- B82E-9FD36****** | The UUID of the image. |
| PageInfo | Struct |   | The pagination information. |
| Count | Integer | 18 | The total number of returned pages. |

| CurrentPage | Integer | 1 | The page number of the returned page. |
|---|---|---|---|
| PageSize | Integer | 20 | The number of entries returned per page. |
| TotalCount | Integer | 18 | The total number of entries returned. |
| RequestId | String | B41B3780-337A-472D- B82E-9FD3642B935 | The ID of the request. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeImageListWithBaselineName &BaselineNameKey=identification &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ImageInfos>
    <NoRiskImage>3</NoRiskImage>
    <RepoNamespace>hanghai-namespace</RepoNamespace>
    <ImageSize>212</ImageSize>
    <Digest>6a5e1031a5858617f7d8a179ead6****</Digest>
    <InstanceId>i-km100o6qy8gidwn3****</InstanceId>
    <TotalItemCount>1</TotalItemCount>
    <RepoName>centos1</RepoName>
    <RiskStatus>YES</RiskStatus>
    <Endpoints>[]</Endpoints>
    <Uuid>B41B3780-337A-472D-B82E-9FD36******</Uuid>
    <LowRiskImage>2</LowRiskImage>
    <ImageCreate>1639236844747</ImageCreate>
    <RepoType>PRIVATE</RepoType>
    <MiddleRiskImage>3</MiddleRiskImage>
    <HighRiskImage>1</HighRiskImage>
    <ImageId>asdaSdasd***</ImageId>
    <ImageUpdate>1639236844747</ImageUpdate>
    <Tag>0.2</Tag>
    <RegionId>cn-wulan-env116-d01***</RegionId>
    <RepoId>crr-vridcl4****</RepoId>
</ImageInfos> <PageInfo>
    <TotalCount>18</TotalCount>
    <PageSize>20</PageSize>
    <CurrentPage>1</CurrentPage>
    <Count>18</Count>
</PageInfo> <RequestId>B41B3780-337A-472D-B82E-9FD3642B935</RequestId>
```

`JSON` format `{`

```json
    "ImageInfos": {
        "NoRiskImage": 3,
        "RepoNamespace": "hanghai-namespace",
        "ImageSize": 212,
        "Digest": "6a5e1031a5858617f7d8a179ead6****",
        "InstanceId": "i-km100o6qy8gidwn3****",
        "TotalItemCount": 1,
        "RepoName": "centos1",
        "RiskStatus": "YES",
        "Endpoints": "[]",
        "Uuid": "B41B3780-337A-472D-B82E-9FD36******",
        "LowRiskImage": 2,
        "ImageCreate": 1639236844747,
        "RepoType": "PRIVATE",
        "MiddleRiskImage": 3,
        "HighRiskImage": 1,
        "ImageId": "asdaSdasd***",
        "ImageUpdate": 1639236844747,
        "Tag": 0.2,
        "RegionId": "cn-wulan-env116-d01***",
        "RepoId": "crr-vridcl4****"
```

`},`

```json
    "PageInfo": {
        "TotalCount": 18,
        "PageSize": 20,
        "CurrentPage": 1,
        "Count": 18
```

`},`

```json
    "RequestId": "B41B3780-337A-472D-B82E-9FD3642B935"
```

`}`

### 5.7 DescribeImageBaselineItemList

Queries the baseline check items of an image.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeImageBase lineItemList | The operation that you want to perform. Set the value to DescribeImageBaselineItemList. |
| ImageUuid | String | Yes | e05c0de798217637 868ef4**** | The UUID of the image. |
| Status | String | No | 1 | The status of the baseline check item. |
| BaselineClassKey | String | No | identification | The key of the baseline type. |
| BaselineNameKey | String | No | identification | The key of the baseline name. |
| PageSize | Integer | No | 20 | The number of entries to return on each page. |

| CurrentPage | Integer | No | 1 | The number of the page to return. |
|---|---|---|---|---|
| Lang | String | No | zh | The language of the content within the request and response. Valid values: zh: Chinese en: English |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| BaselineItemInfos | Array of BaselineItemInfos |   | An array that consists of the baseline check items. |
| BaselineClassAlia s | String | Identity authentication | The type of the baseline. |
| BaselineClassKey | String | identification | The key of the baseline type. |
| BaselineItemAlias | String | Make sure that no accounts in the system use blank passwords | The baseline check item. |
| BaselineItemKey | String | non pwd user _ _ | The key of the baseline check item. |
| BaselineNameAlia s | String | Identity authentication | The name of the baseline. |
| BaselineNameKe y | String | identification | The key of the baseline name. |
| Status | Integer | 0 | The status of the baseline check item. Valid values: 0: normal 1: abnormal |
| WhiteList | Integer | 0 | The whitelist. |
| PageInfo | Struct |   | The pagination information. |
| Count | Integer | 18 | The total number of returned pages. |
| CurrentPage | Integer | 1 | The page number of the returned page. |
| PageSize | Integer | 20 | The number of entries returned per page. |
| TotalCount | Integer | 200 | The total number of entries returned. |
| RequestId | String | B41B3780-337A-472D- B82E-9FD3642B9350 | The ID of the request. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeImageBaselineItemList &ImageUuid=e05c0de798217637868ef4**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<BaselineItemInfos>
    <Status>0</Status>
    <BaselineClassKey>identification</BaselineClassKey>
    <BaselineItemAlias>Make sure that no accounts in the system use blank
passwords</BaselineItemAlias>
    <BaselineClassAlias>Identity authentication</BaselineClassAlias>
    <BaselineItemKey>non_pwd_user</BaselineItemKey>
    <BaselineNameAlias>Identity authentication</BaselineNameAlias>
    <WhiteList>0</WhiteList>
    <BaselineNameKey>identification</BaselineNameKey>
</BaselineItemInfos> <PageInfo>
    <TotalCount>200</TotalCount>
    <PageSize>20</PageSize>
    <CurrentPage>1</CurrentPage>
    <Count>18</Count>
</PageInfo> <RequestId>B41B3780-337A-472D-B82E-9FD3642B9350</RequestId>
```

`JSON` format `{`

```json
    "BaselineItemInfos": {
        "Status": 0,
        "BaselineClassKey": "identification",
        "BaselineItemAlias": "Make sure that no accounts in the system use blank passwords",
        "BaselineClassAlias": "Identity authentication",
        "BaselineItemKey": "non_pwd_user",
        "BaselineNameAlias": "Identity authentication",
        "WhiteList": 0,
        "BaselineNameKey": "identification"
```

`},`

```json
    "PageInfo": {
        "TotalCount": 200,
        "PageSize": 20,
        "CurrentPage": 1,
        "Count": 18
```

`},`

```json
    "RequestId": "B41B3780-337A-472D-B82E-9FD3642B9350"
```

`}`

### 5.8 DescribeCycleTaskList

Queries image scan tasks.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeCycleTaskL ist | The operation that you want to perform. Set the value to DescribeCycleTaskList. |

| TaskType | String | Yes | IMAGE SCAN _ | The type of the task. Set the value to IMAGE SCAN. _ |
|---|---|---|---|---|
| TaskName | String | No | IMAGE SCAN _ | The name of the task. Set the value to IMAGE SCAN. _ |
| CurrentPage | Integer | No | 1 | The number of the page to return. |
| PageSize | Integer | No | 20 | The number of entries to return on each page. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| CycleScheduleRe sponseList | Array of CycleScheduleRe sponse |   | An array that consists of scheduled tasks. |
| ConfigId | String | 60846e06a516e91ce1 665a8b50***** | The ID of the configuration. |
| Enable | Integer | 1 | Indicates whether the task is enabled. 0: no 1: yes |
| FirstDateStr | Long | 1639236844747 | The time of the first scan. The value is a UNIX timestamp. Unit: milliseconds. |
| IntervalPeriod | Integer | 3 | The scan interval. |
| LastTaskId | String | c619d978da536af2532 ea45501ef**** | The ID of the latest task. |
| NextStartTimeStr | Long | 1639236844747 | The time when the next scan will be performed. The value is a UNIX timestamp. Unit: milliseconds. |
| Param | String | null | The parameters of the task. |
| PeriodUnit | String | day | The unit of the scan cycle. The value is fixed as day. |
| TargetEndTime | Integer | 24 | The end time of the task. Unit: hours. |
| TargetStartTime | Integer | 0 | The start time of the task. Unit: hours. |
| TaskName | String | IMAGE SCAN _ | The name of the task. The value is fixed as IMAGE SCAN. _ |
| TaskType | String | IMAGE SCAN _ | The type of the task. The value is fixed as IMAGE SCAN. _ |

| PageInfo | Struct |   | The pagination information. |
|---|---|---|---|
| Count | Integer | 15 | The total number of returned pages. |
| CurrentPage | Integer | 1 | The page number of the returned page. |
| PageSize | Integer | 20 | The number of entries returned per page. |
| TotalCount | Integer | 15 | The total number of entries returned. |
| RequestId | String | B41B3780-337A-472D- B82E-9FD3642B9350 | The ID of the request. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeCycleTaskList &TaskType=IMAGE_SCAN &<Common request parameters>
```

Sample success responses `XML` format

```xml
<CycleScheduleResponseList>
    <TargetEndTime>24</TargetEndTime>
    <TaskName>IMAGE_SCAN</TaskName>
    <TaskType>IMAGE_SCAN</TaskType>
    <Param>{}</Param>
    <Enable>1</Enable>
    <FirstDateStr>1639236844747</FirstDateStr>
    <IntervalPeriod>3</IntervalPeriod>
    <TargetStartTime>0</TargetStartTime>
    <NextStartTimeStr>1639236844747</NextStartTimeStr>
    <ConfigId>60846e06a516e91ce1665a8b50*****</ConfigId>
    <LastTaskId>c619d978da536af2532ea45501ef****</LastTaskId>
    <PeriodUnit>day</PeriodUnit>
</CycleScheduleResponseList> <PageInfo>
    <TotalCount>15</TotalCount>
    <PageSize>20</PageSize>
    <CurrentPage>1</CurrentPage>
    <Count>15</Count>
</PageInfo> <RequestId>B41B3780-337A-472D-B82E-9FD3642B9350</RequestId>
```

`JSON` format `{`

```json
    "CycleScheduleResponseList": {
        "TargetEndTime": 24,
        "TaskName": "IMAGE_SCAN",
        "TaskType": "IMAGE_SCAN",
        "Param": "{}",
        "Enable": 1,
        "FirstDateStr": 1639236844747,
        "IntervalPeriod": 3,
        "TargetStartTime": 0,
        "NextStartTimeStr": 1639236844747,
        "ConfigId": "60846e06a516e91ce1665a8b50*****",
        "LastTaskId": "c619d978da536af2532ea45501ef****",
        "PeriodUnit": "day"
```

`},`

```json
    "PageInfo": {
        "TotalCount": 15,
        "PageSize": 20,
        "CurrentPage": 1,
        "Count": 15
```

`},`

```json
    "RequestId": "B41B3780-337A-472D-B82E-9FD3642B9350"
```

`}`

### 5.9 DescribeContainerCriteria

Queries the conditions that are used to query containers.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeContainerC riteria | The operation that you want to perform. Set the value to DescribeContainerCriteria. |
| GroupField | String | No | pod | The type of the group that you want to query. Valid values: pod appName namespace clusterId |
| Value | String | No | test | The fuzzy search conditions that can be automatically matched. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| CriteriaList | Array of Criteria |   | An array that consists of the query conditions. |
| Name | String | demoKey | The key of the parameter. |

| Type | String | select | The type of the parameter. Valid values: input: input box select: drop-down list |
|---|---|---|---|
| Values | String | value1,value2,value3 | The values of the parameter. Multiple values are separated by commas (,). |
| RequestId | String | clusterTypeB41B3780- 337A-472D-B82E- 9FD3642B9350 | The ID of the request. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeContainerCriteria &<Common request parameters>
```

Sample success responses `XML` format

```xml
<CriteriaList>
    <Type>select</Type>
    <Values>value1,value2,value3</Values>
    <Name>demoKey</Name>
</CriteriaList> <RequestId>clusterTypeB41B3780-337A-472D-B82E-9FD3642B9350</RequestId>
```

`JSON` format `{`

```json
    "CriteriaList": {
        "Type": "select",
        "Values": "value1,value2,value3",
        "Name": "demoKey"
```

`},`

```json
    "RequestId": "clusterTypeB41B3780-337A-472D-B82E-9FD3642B9350"
```

`}`

### 5.10 DescribeContainerFieldStatistics

Queries statistics of container risks.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeContainerFi eldStatistics | The operation that you want to perform. Set the value to DescribeContainerFieldStatistics. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| ContainerGroupe dFields | Struct |   | The information about the pod. |

| AlarmContainerC ount | Integer | 2 | The number of containers on which alerts are generated. |
|---|---|---|---|
| AlarmInstanceCo unt | Integer | 3 | The number of instances on which alerts are generated. |
| AppCount | Integer | 1 | The number of applications. |
| ClusterCount | Integer | 3 | The number of clusters. |
| ContainerCount | Integer | 4 | The number of containers. |
| ImageCount | Integer | 5 | The number of images. |
| InstanceCount | Integer | 2 | The number of instances. |
| NamespaceCount | Integer | 1 | The number of namespaces. |
| PodCount | Integer | 2 | The number of pods. |
| RiskAppCount | Integer | 3 | The number of applications on which risks are detected. |
| RiskContainerCou nt | Integer | 4 | The number of containers on which risks are detected. |
| RiskImageCount | Integer | 1 | The number of images on which risks are detected. |
| RiskInstanceCoun t | Integer | 2 | The number of instances on which risks are detected. |
| RiskPodCount | Integer | 3 | The number of pods on which risks are detected. |
| RequestId | String | B41B3780-337A-472D- B82E-9FD3642B9350 | The ID of the request. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeContainerFieldStatistics &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RequestId>B41B3780-337A-472D-B82E-9FD3642B9350</RequestId> <ContainerGroupedFields>
    <RiskContainerCount>4</RiskContainerCount>
    <AlarmInstanceCount>3</AlarmInstanceCount>
    <AppCount>1</AppCount>
    <ClusterCount>3</ClusterCount>
    <RiskInstanceCount>2</RiskInstanceCount>
    <RiskAppCount>3</RiskAppCount>
    <NamespaceCount>1</NamespaceCount>
    <PodCount>2</PodCount>
    <InstanceCount>2</InstanceCount>
    <RiskImageCount>1</RiskImageCount>
    <ImageCount>5</ImageCount>
    <ContainerCount>4</ContainerCount>
    <AlarmContainerCount>2</AlarmContainerCount>
    <RiskPodCount>3</RiskPodCount>
</ContainerGroupedFields>
```

`JSON` format `{`

```json
    "RequestId": "B41B3780-337A-472D-B82E-9FD3642B9350",
    "ContainerGroupedFields": {
        "RiskContainerCount": 4,
        "AlarmInstanceCount": 3,
        "AppCount": 1,
        "ClusterCount": 3,
        "RiskInstanceCount": 2,
        "RiskAppCount": 3,
        "NamespaceCount": 1,
        "PodCount": 2,
        "InstanceCount": 2,
        "RiskImageCount": 1,
        "ImageCount": 5,
        "ContainerCount": 4,
        "AlarmContainerCount": 2,
        "RiskPodCount": 3
```

`}` `}`

**5.11.**

### DescribeContainerGroupedFieldDetail

Queries the details of pods.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeContainerG roupedFieldDetail | The operation that you want to perform. Set the value to DescribeContainerGroupedFieldDetail. |

| Criteria | String | Yes | [{\"name\":\"riskSta tus\",\"value\":\"YES \"}, {\"name\":\"internet Ip\",\"value\":\"1.2.3 .4\"}] | The search conditions for assets. Set the value in the following format: [{\"name\":\"Name of Condition 1\",\"value\":\"Value of Condition 1\"},{\"name\":\"Name of Condition 2\",\"value\":\"Value of Condition 2\"},{},...] Supported search conditions include the instance ID, instance name, virtual private cloud (VPC) ID, region, and public IP address. You can call the DescribeCriteria operation to query the supported search conditions. |
|---|---|---|---|---|
| GroupField | String | Yes | pod | The group type that you want to use for query. Valid values: pod appName namespace clusterId |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Data | Struct |   | The details of the pod. |
| AlarmCount | Integer | 1 | The statistics of alerts. |
| AppName | String | csi-provisioner | The name of the application. |
| ClusterCurrentVe rsion | String | None | This parameter is deprecated. |
| ClusterId | String | Cccfd68c474454665ac e07efce924**** | The ID of the cluster. |
| ClusterName | String | test**** | The name of the cluster. |
| ClusterState | String | None | This parameter is deprecated. |
| ClusterType | String | None | This parameter is deprecated. |
| ContainerCount | Integer | 1 | The number of containers. |
| CreateTime | Long | 1639236844747 | The creation time. The value is a UNIX timestamp. Unit: milliseconds. |
| InstanceCount | Integer | 1 | The number of instances. |

| Namespace | String | ********-namespace | The namespace to which the image repository belongs. |
|---|---|---|---|
| NodeName | String | cn-****-env116-d01.i- km100o6qw4bhyq**** ** | The name of the node. |
| Pod | String | csi-provisioner- 564c7989c4-9t8z8 | The pod. |
| PodCount | Integer | 2 | The number of pods. |
| PodIp | String | 172.29.0.130 | The IP address of the pod. |
| RegionId | String | cn-wulan-env116-d01 | The region ID. |
| VulCount | Integer | 2 | The number of vulnerabilities. |
| RequestId | String | B41B3780-337A-472D- B82E-9FD3642B9350 | The ID of the request. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeContainerGroupedFieldDetail &Criteria=[{\"name\":\"riskStatus\",\"value\":\"YES\"}, {\"name\":\"internetIp\",\"value\":\"1.2.3.4\"}] &GroupField=pod &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RequestId>B41B3780-337A-472D-B82E-9FD3642B9350</RequestId> <Data>
    <ClusterState>None</ClusterState>
    <Pod>csi-provisioner-564c7989c4-9t8z8</Pod>
    <ClusterId>Cccfd68c474454665ace07efce924****</ClusterId>
    <NodeName>cn-****-env116-d01.i-km100o6qw4bhyq******</NodeName>
    <CreateTime>1639236844747</CreateTime>
    <ClusterType>None</ClusterType>
    <Namespace>********-namespace</Namespace>
    <VulCount>2</VulCount>
    <AppName>csi-provisioner</AppName>
    <PodCount>2</PodCount>
    <InstanceCount>1</InstanceCount>
    <ClusterCurrentVersion>None</ClusterCurrentVersion>
    <ContainerCount>1</ContainerCount>
    <PodIp>172.29.0.130</PodIp>
    <ClusterName>test****</ClusterName>
    <RegionId>cn-wulan-env116-d01</RegionId>
    <AlarmCount>1</AlarmCount>
</Data>
```

`JSON` format `{`

```json
    "RequestId": "B41B3780-337A-472D-B82E-9FD3642B9350",
    "Data": {
        "ClusterState": "None",
        "Pod": "csi-provisioner-564c7989c4-9t8z8",
        "ClusterId": "Cccfd68c474454665ace07efce924****",
        "NodeName": "cn-****-env116-d01.i-km100o6qw4bhyq******",
        "CreateTime": 1639236844747,
        "ClusterType": "None",
        "Namespace": "********-namespace",
        "VulCount": 2,
        "AppName": "csi-provisioner",
        "PodCount": 2,
        "InstanceCount": 1,
        "ClusterCurrentVersion": "None",
        "ContainerCount": 1,
        "PodIp": "172.29.0.130",
        "ClusterName": "test****",
        "RegionId": "cn-wulan-env116-d01",
        "AlarmCount": 1
```

`}` `}`

### 5.12 DescribeContainerInstances

Queries containers.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeContainerI nstances | The operation that you want to perform. Set the value to DescribeContainerInstances. |
| Criteria | String | No | [{\"name\":\"riskSta tus\",\"value\":\"YES \"}, {\"name\":\"internet Ip\",\"value\":\"1.2.3 .4\"}] | The search conditions for assets. Set the value in the following format: [{\"name\":\"Name of Condition 1\",\"value\":\"Value of Condition 1\"},{\"name\":\"Name of Condition 2\",\"value\":\"Value of Condition 2\"},{},...] Supported search conditions include the instance ID, instance name, virtual private cloud (VPC) ID, region, and public IP address. You can call the DescribeCriteria operation to query the supported search conditions. |
| LogicalExp | String | No | OR | The logical relationship among the search conditions. Valid values: OR: The logical relationship among the search conditions is OR. AND: The logical relationship among the search conditions is AND. |

| PageSize | Integer | No | 20 | The number of entries to return on each page. |
|---|---|---|---|---|
| CurrentPage | Integer | No | 1 | The number of the page to return. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| ContainerInstanc eList | Array of ContainerInstanc e |   | An array that consists of the containers. |
| AlarmCount | Integer | 1 | The statistics of alerts. |
| AlarmStatus | String | NO | Indicates whether alerts were triggered. Valid values: YES NO |
| AppName | String | csi-provisioner | The name of the application. |
| ClusterId | String | Cccfd68c474454665ac e07efce924**** | The ID of the cluster to which the container belongs. |
| ClusterName | String | test**** | The name of the cluster to which the container belongs. |
| ContainerId | String | B41B3780-337A-472D- B82E-9FD3******** | The ID of the container. |
| CreateTimestamp | Long | 1639236844747 | The timestamp when the container was created. Unit: milliseconds. |
| HcCount | Integer | 1 | The number of baseline risks. |
| HcStatus | String | NO | Indicates whether baseline risks were detected. Valid values: YES NO |
| HostIp | String | 47.100.XX.XX | The IP address. |
| Image | String | registry.acs.intra.env1 16.shuguang.com/acs/l og-controller:0.2.7.0- 68ada84-aliyun | The image. |
| ImageDigest | String | 6a5e103187b31a9459 2a47a5858617f7a179e ad61df7606**** | The digest of the image. |
| ImageId | String | asdaSdasd******** | The ID of the image. |

| ImageRepoName | String | centos1 | The image repository. |
|---|---|---|---|
| ImageRepoName space | String | shanghai-namespace | The namespace to which the image repository belongs. |
| ImageRepoTag | String | 0.2.7.0-68ada84-aliyun | The tag that is added to the image repository. |
| ImageUuid | String | e05c0de79821763786 8ef4**** | The UUID of the image. |
| InstanceId | String | i- km100o6qy8g********* | The ID of the instance. |
| Namespace | String | shanghai-namespace | The namespace to which the image repository belongs. |
| NodeInfo | String | None | This parameter is deprecated. |
| NodeName | String | cn-wulan-env116- d01.i- km100o6qw4bhyqo7p bvb | The name of the node. |
| Pod | String | csi-provisioner- 564c7989c4-9**** | The pod. |
| PodIp | String | 172.29.0.130 | The IP address of the pod. |
| RegionId | String | cn-***-env116-d01 | The region ID. |
| RiskCount | String | 1 | The number of risks. |
| RiskStatus | String | YES | Indicates whether risks were detected. Valid values: YES NO |
| UpdateMark | String | None | This parameter is deprecated. |
| VulCount | Integer | 0 | The number of vulnerabilities. |
| VulStatus | String | NO | Indicates whether vulnerabilities were detected. Valid values: YES NO |
| PageInfo | Struct |   | The pagination information. |
| Count | Integer | 20 | The total number of returned pages. |
| CurrentPage | Integer | 1 | The page number of the returned page. |

| PageSize | Integer | 20 | The number of entries returned per page. |
|---|---|---|---|
| TotalCount | Integer | 50 | The total number of entries returned. |
| RequestId | String | B41B3780-337A-472D- B82E-9FD3642B9350 | The ID of the request. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeContainerInstances &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ContainerInstanceList>
    <VulStatus>NO</VulStatus>
    <ImageDigest>6a5e103187b31a94592a47a5858617f7a179ead61df7606****</ImageDigest>
    <NodeName>cn-wulan-env116-d01.i-km100o6qw4bhyqo7pbvb</NodeName>
    <ImageRepoNamespace>shanghai-namespace</ImageRepoNamespace>
    <Image>registry.acs.intra.env116.shuguang.com/acs/log-controller:0.2.7.0-68ada84-aliyun</Image>
    <ImageUuid>e05c0de798217637868ef4****</ImageUuid>
    <RiskCount>1</RiskCount>
    <AppName>csi-provisioner</AppName>
    <ContainerId>B41B3780-337A-472D-B82E-9FD3********</ContainerId>
    <ImageId>asdaSdasd</ImageId>
    <ClusterName>test****</ClusterName>
    <CreateTimestamp>1639236844747</CreateTimestamp>
    <AlarmCount>1</AlarmCount>
    <HcCount>1</HcCount>
    <HostIp>192.1.1.130</HostIp>
    <Pod>csi-provisioner-564c7989c4-9****</Pod>
    <InstanceId>i-km100o6qy8g*********</InstanceId>
    <ClusterId>Cccfd68c474454665ace07efce924****</ClusterId>
    <RiskStatus>YES</RiskStatus>
    <Namespace>shanghai-namespace</Namespace>
    <VulCount>0</VulCount>
    <ImageRepoName>centos1</ImageRepoName>
    <NodeInfo>None</NodeInfo>
    <PodIp>172.29.0.130</PodIp>
    <AlarmStatus>NO</AlarmStatus>
    <RegionId>cn-***-env116-d01</RegionId>
    <ImageRepoTag>0.2.7.0-68ada84-aliyun</ImageRepoTag>
    <HcStatus>NO</HcStatus>
    <UpdateMark>None</UpdateMark>
</ContainerInstanceList> <PageInfo>
    <TotalCount>50</TotalCount>
    <PageSize>20</PageSize>
    <CurrentPage>1</CurrentPage>
    <Count>20</Count>
</PageInfo> <RequestId>B41B3780-337A-472D-B82E-9FD3642B9350</RequestId>
```

`JSON` format `{`

```json
    "ContainerInstanceList": {
        "VulStatus": "NO",
        "ImageDigest": "6a5e103187b31a94592a47a5858617f7a179ead61df7606****",
        "NodeName": "cn-wulan-env116-d01.i-km100o6qw4bhyqo7pbvb",
        "ImageRepoNamespace": "shanghai-namespace",
        "Image": "registry.acs.intra.env116.shuguang.com/acs/log-controller:0.2.7.0-68ada84-aliyun",
        "ImageUuid": "e05c0de798217637868ef4****",
        "RiskCount": 1,
        "AppName": "csi-provisioner",
        "ContainerId": "B41B3780-337A-472D-B82E-9FD3********",
        "ImageId": "asdaSdasd",
        "ClusterName": "test****",
        "CreateTimestamp": 1639236844747,
        "AlarmCount": 1,
        "HcCount": 1,
        "HostIp": "192.1.1.130",
        "Pod": "csi-provisioner-564c7989c4-9****",
        "InstanceId": "i-km100o6qy8g*********",
        "ClusterId": "Cccfd68c474454665ace07efce924****",
        "RiskStatus": "YES",
        "Namespace": "shanghai-namespace",
        "VulCount": 0,
        "ImageRepoName": "centos1",
        "NodeInfo": "None",
        "PodIp": "172.29.0.130",
        "AlarmStatus": "NO",
        "RegionId": "cn-***-env116-d01",
        "ImageRepoTag": "0.2.7.0-68ada84-aliyun",
        "HcStatus": "NO",
        "UpdateMark": "None"
```

`},`

```json
    "PageInfo": {
        "TotalCount": 50,
        "PageSize": 20,
        "CurrentPage": 1,
        "Count": 20
```

`},`

```json
    "RequestId": "B41B3780-337A-472D-B82E-9FD3642B9350"
```

`}`

**5.13.**

### DescribeGroupedContainerInstances

Queries the details about containers by group, such as application, cluster, namespace, or pod.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeGroupedCo ntainerInstances | The operation that you want to perform. Set the value to DescribeGroupedContainerInstances. |

| Criteria | String | No | [{\"name\":\"riskSta tus\",\"value\":\"YES \"}, {\"name\":\"internet Ip\",\"value\":\"1.2.3 .4\"}] | The search conditions for assets. Set the value in the following format: [{\"name\":\"Name of Condition 1\",\"value\":\"Value of Condition 1\"},{\"name\":\"Name of Condition 2\",\"value\":\"Value of Condition 2\"},{},...] Supported search conditions include the instance ID, instance name, virtual private cloud (VPC) ID, region, and public IP address. You can call the DescribeCriteria operation to query the supported search conditions. |
|---|---|---|---|---|
| LogicalExp | String | No | OR | The logical relationship among the search conditions. OR: The logical relationship among the search conditions is OR. AND: The logical relationship among the search conditions is AND. |
| GroupField | String | No | pod | The type of the container group that you want to query. Valid values: pod appName namespace clusterId |
| FieldValue | String | No | pod | The keyword that is used to search for containers based on the specified group type. The value is automatically identified as a parameter. You must specify this parameter based on the value of the GroupField parameter. pod: the name of the pod that you want to query. appName: the name of the application that you want to query. namespace: the namespace that you want to query. clusterId: the ID of the cluster that you want to query. |
| PageSize | Integer | No | 20 | The number of entries to return on each page. |
| CurrentPage | Integer | No | 1 | The number of the page to return. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| GroupedContaine rInstanceList | Array of GroupedContaine rInstance |   | An array that consists of the details about the containers of the specified group. |

| AlarmCount | Integer | 1 | The number of alerts. |
|---|---|---|---|
| AppName | String | csi-provisioner | The name of the application. |
| ClusterId | String | Cccfd68c474454665ac e07efce924**** | The ID of the cluster to which the container belongs. |
| ClusterName | String | test*** | The name of the cluster to which the container belongs. |
| ClusterType | String | NotManagedKubernete s | The type of the cluster. Valid values: ManagedKubernetes NotManagedKubernetes PrivateKubernetes |
| CreateTime | Long | 1639236844747 | The creation time. The value is a UNIX timestamp. Unit: milliseconds. |
| CusterState | String | running | The status of the cluster. |
| HostIp | String | 47.100.XX.XX | The IP address of the server. |
| InstanceCount | Integer | 2 | The number of instances. |
| InstanceId | String | i- km100o6qy8gidw***** * | The ID of the instance. |
| Namespace | String | hangzhou-namespace | The namespace. |
| Pod | String | csi-provisioner- 564c7989c4-9**** | The pod. |
| PodIp | String | 47.100.XX.XX | The IP address of the pod. |
| RegionId | String | cn-*****-env116-d01 | The region ID. |
| RiskInstanceCoun t | Integer | 5 | The number of at-risk instances. |
| RiskLevel | String | medium | The risk level. Valid values: high medium low |
| RiskStatus | String | YES | Indicates whether risks were detected. Valid values: YES NO |
| VulCount | Integer | 2 | The number of vulnerabilities. |

| PageInfo | Struct |   | The pagination information. |
|---|---|---|---|
| Count | Integer | 20 | The total number of returned pages. |
| CurrentPage | Integer | 1 | The page number of the returned page. |
| PageSize | Integer | 20 | The number of entries returned per page. |
| TotalCount | Integer | 35 | The total number of entries returned. |
| RequestId | String | B41B3780-337A-472D- B82E-9FD3642B9350 | The ID of the request. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeGroupedContainerInstances &<Common request parameters>
```

Sample success responses `XML` format

```xml
<GroupedContainerInstanceList>
    <HostIp>47.100.XX.XX</HostIp>
    <Pod>csi-provisioner-564c7989c4-9****</Pod>
    <InstanceId>i-km100o6qy8gidw******</InstanceId>
    <ClusterId>Cccfd68c474454665ace07efce924****</ClusterId>
    <CusterState>running</CusterState>
    <CreateTime>1639236844747</CreateTime>
    <RiskInstanceCount>5</RiskInstanceCount>
    <ClusterType>NotManagedKubernetes</ClusterType>
    <RiskStatus>YES</RiskStatus>
    <Namespace>hangzhou-namespace</Namespace>
    <AppName>csi-provisioner</AppName>
    <VulCount>2</VulCount>
    <InstanceCount>2</InstanceCount>
    <PodIp>47.100.XX.XX</PodIp>
    <ClusterName>test***</ClusterName>
    <RegionId>cn-*****-env116-d01</RegionId>
    <RiskLevel>medium</RiskLevel>
    <AlarmCount>1</AlarmCount>
</GroupedContainerInstanceList> <PageInfo>
    <TotalCount>35</TotalCount>
    <PageSize>20</PageSize>
    <CurrentPage>1</CurrentPage>
    <Count>20</Count>
</PageInfo> <RequestId>B41B3780-337A-472D-B82E-9FD3642B9350</RequestId>
```

`JSON` format `{`

```json
    "GroupedContainerInstanceList": {
        "HostIp": "47.100.XX.XX",
        "Pod": "csi-provisioner-564c7989c4-9****",
        "InstanceId": "i-km100o6qy8gidw******",
        "ClusterId": "Cccfd68c474454665ace07efce924****",
        "CusterState": "running",
        "CreateTime": 1639236844747,
        "RiskInstanceCount": 5,
        "ClusterType": "NotManagedKubernetes",
        "RiskStatus": "YES",
        "Namespace": "hangzhou-namespace",
        "AppName": "csi-provisioner",
        "VulCount": 2,
        "InstanceCount": 2,
        "PodIp": "47.100.XX.XX",
        "ClusterName": "test***",
        "RegionId": "cn-*****-env116-d01",
        "RiskLevel": "medium",
        "AlarmCount": 1
```

`},`

```json
    "PageInfo": {
        "TotalCount": 35,
        "PageSize": 20,
        "CurrentPage": 1,
        "Count": 20
```

`},`

```json
    "RequestId": "B41B3780-337A-472D-B82E-9FD3642B9350"
```

`}`

### 5.14 DescribeImageSecurityScanCount

Queries the results of an image scan.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeImageSecu rityScanCount | The operation that you want to perform. Set the value to DescribeImageSecurityScanCount. |
| RepoRegionId | String | No | cn-********** | The region ID of the image repository. |
| RepoInstanceId | String | No | cri-datvailb**** | The ID of the Container Registry instance. |
| RepoId | String | No | crr-vridcl4**** | The ID of the image repository. |
| ImageTag | String | No | 0.2 | The tag that is added to the image. |
| ImageDigest | String | No | 6a5e103187b31a94 592a47a5858617f7 a179ead61df7606* *** | The digest of the image. |

| Dealed | String | No | N | The status of the vulnerabilities that are detected. Valid values: Y: handled N: unhandled |
|---|---|---|---|---|
| ImageUuid | String | No | e05c0de798217637 868ef4**** | The ID of the image. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Data | Struct |   | The information of image. |
| ImageBaselineCo unt | Integer | 1 | The number of image baselines. |
| ImageCveVulCou nt | Integer | 2 | The number of image system vulnerabilities. |
| ImageMaliciousFil eCount | Integer | 3 | The number of alerts that are generated for suspicious file changes. |
| ImageScaVulCou nt | Integer | 1 | The number of Software Composition Analysis (SCA) vulnerabilities. |
| RequestId | String | B41B3780-337A-472D- B82E-9FD3642B9350 | The ID of the request. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeImageSecurityScanCount &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RequestId>B41B3780-337A-472D-B82E-9FD3642B9350</RequestId> <Data>
    <ImageBaselineCount>1</ImageBaselineCount>
    <ImageCveVulCount>2</ImageCveVulCount>
    <ImageMaliciousFileCount>3</ImageMaliciousFileCount>
    <ImageScaVulCount>1</ImageScaVulCount>
</Data>
```

`JSON` format `{`

```json
    "RequestId": "B41B3780-337A-472D-B82E-9FD3642B9350",
    "Data": {
        "ImageBaselineCount": 1,
        "ImageCveVulCount": 2,
        "ImageMaliciousFileCount": 3,
        "ImageScaVulCount": 1
```

`}` `}`

### 5.15 DescribeImageCriteria

Queries the search conditions that can be used to obtain images.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeImageCrite ria | The operation that you want to perform. Set the value to DescribeImageCriteria. |
| Value | String | No | demo | The search conditions. Fuzzy match is supported. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| CriteriaList | Array of Criteria |   | An array that consists of the search conditions. |
| Name | String | riskStatus | The name of the search condition. |
| Type | String | select | The type of the search condition. input: text box select: drop-down list |
| Values | String | NO | The value of the search condition. |
| RequestId | String | B41B3780-337A-472D- B82E-9FD3642B9350 | The ID of the request. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeImageCriteria &<Common request parameters>
```

Sample success responses `XML` format

```xml
<CriteriaList>
    <Type>select</Type>
    <Values>NO</Values>
    <Name>riskStatus</Name>
</CriteriaList> <RequestId>B41B3780-337A-472D-B82E-9FD3642B9350</RequestId>
```

`JSON` format `{`

```json
    "CriteriaList": {
        "Type": "select",
        "Values": "NO",
        "Name": "riskStatus"
```

`},`

```json
    "RequestId": "B41B3780-337A-472D-B82E-9FD3642B9350"
```

`}`

### 5.16 GetRegistryScanDayNum

Queries the time setting for image scans.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | GetRegistryScanDa yNum | The operation that you want to perform. Set the value to GetRegistryScanDayNum. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | B41B3780-337A-472D- B82E-9FD3642B9350 | The ID of the request. |
| ScanDayNumCon fig | Struct |   | The settings for image scans. |
| DayNumList | String | 1,3,7,15,30,90,180,365 | The valid values of the time setting for image scans. |
| ScanDayNum | Integer | 90 | The time setting for scanning images. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=GetRegistryScanDayNum &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ScanDayNumConfig>
    <DayNumList>1,3,7,15,30,90,180,365</DayNumList>
    <ScanDayNum>90</ScanDayNum>
</ScanDayNumConfig> <RequestId>B41B3780-337A-472D-B82E-9FD3642B9350</RequestId>
```

`JSON` format `{`

```json
    "ScanDayNumConfig": {
        "DayNumList": "1,3,7,15,30,90,180,365",
        "ScanDayNum": 90
```

`},`

```json
    "RequestId": "B41B3780-337A-472D-B82E-9FD3642B9350"
```

`}`

### 5.17 DescribeImageInstances

Queries the information of images.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeImageInsta nces | The operation that you want to perform. Set the value to DescribeImageInstances. |
| Criteria | String | No | [{\"name\":\"riskSta tus\",\"value\":\"YES \"}, {\"name\":\"internet Ip\",\"value\":\"1.2.3 .4\"}] | The search conditions for assets. Set the value in the following format: [{"name":"Name of Condition 1","value":"Value of Condition 1"}, {"name":"Name of Condition 2","value":"Value of Condition 2"}]. Supported search conditions include the instance ID, instance name, virtual private cloud (VPC) ID, region, and public IP address. |
| LogicalExp | String | No | OR | The logical relationship among the search conditions. Valid values: OR: The logical relationship among the search conditions is OR. AND: The logical relationship among the search conditions is AND. |
| PageSize | Integer | No | 20 | The number of entries to return on each page. |
| CurrentPage | Integer | No | 1 | The number of the page to return. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| ImageInstanceLis t | Array of responses |   | An array that consists of the images. |
| AlarmCount | Integer | 1 | The number of alerts. |
| AlarmStatus | String | YES | Indicates whether alerts were triggered. Valid values: YES NO |

| Digest | String | 6a5e1031a5858617f7d 8a179ead6*** | The digest of the image. |
|---|---|---|---|
| Endpoints | String | [] | The endpoint of the image. |
| HcCount | Integer | 0 | The number of baseline checks. |
| HcStatus | String | NO | Indicates whether baseline risks were detected. Valid values: YES NO |
| ImageCreate | String | 1234567890123 | The timestamp when the image was created. Unit: milliseconds. |
| ImageId | String | asdaSdasd | The ID of the image. |
| ImageSize | String | 101 | The size of the image. |
| ImageUpdate | String | 1639236844747 | The timestamp when the image was updated. Unit: milliseconds. |
| InstanceId | String | i- km100o6qy8gidwn3*** * | The ID of the instance. |
| RegionId | String | cn-wulan-env116-d01 | The region ID. |
| RegistryType | String | defaultAcr | The registration type of the image. |
| RepoId | String | crr-vridcl4**** | The ID of the image repository. |
| RepoName | String | centos1 | The name of the image repository. |
| RepoNamespace | String | hangzhou-namespace | The namespace to which the image repository belongs. |
| RepoType | String | PRIVATE | The type of the image repository. |
| RiskStatus | String | NO | Indicates whether risks were detected. Valid values: YES NO |
| ScaProgress | Integer | 1 | This parameter is deprecated. |
| ScaResult | String | None | This parameter is deprecated. |

| ScaStatus | String | YES | Indicates whether Software Composition Analysis (SCA) vulnerabilities were detected. YES NO |
|---|---|---|---|
| Status | String | NORMAL | The status. |
| Tag | String | 0.1 | The tag that is added to the image. |
| Uuid | String | B41B****-337A-472D- B82E-9FD3642B**** | The UUID of the asset. |
| VulCount | Integer | 1 | The number of vulnerabilities. |
| VulStatus | String | YES | Indicates whether vulnerabilities were detected. Valid values: YES NO |
| PageInfo | Struct |   | The pagination information. |
| Count | Integer | 15 | The total number of returned pages. |
| CurrentPage | Integer | 1 | The page number of the returned page. |
| PageSize | Integer | 20 | The number of entries returned per page. |
| TotalCount | Integer | 15 | The total number of entries returned. |
| RequestId | String | B41B3780-337A-472D- B82E-9FD3642B9350 | The ID of the request. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeImageInstances &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ImageInstanceList>
    <VulStatus>YES</VulStatus>
    <ImageSize>101</ImageSize>
    <Endpoints>[]</Endpoints>
    <ScaProgress>1</ScaProgress>
    <ImageId>asdaSdasd</ImageId>
    <ImageUpdate>1639236844747</ImageUpdate>
    <ScaResult>None</ScaResult>
    <AlarmCount>1</AlarmCount>
    <HcCount>0</HcCount>
    <Status>NORMAL</Status>
    <RepoNamespace>hangzhou-namespace</RepoNamespace>
    <RegistryType>defaultAcr</RegistryType>
    <InstanceId>i-km100o6qy8gidwn3****</InstanceId>
    <Digest>6a5e1031a5858617f7d8a179ead6***</Digest>
    <RepoName>centos1</RepoName>
    <RiskStatus>NO</RiskStatus>
    <VulCount>1</VulCount>
    <ScaStatus>YES</ScaStatus>
    <Uuid>B41B****-337A-472D-B82E-9FD3642B****</Uuid>
    <ImageCreate>1234567890123</ImageCreate>
    <RepoType>PRIVATE</RepoType>
    <AlarmStatus>YES</AlarmStatus>
    <Tag>0.1</Tag>
    <RegionId>cn-wulan-env116-d01</RegionId>
    <RepoId>crr-vridcl4****</RepoId>
    <HcStatus>NO</HcStatus>
</ImageInstanceList> <PageInfo>
    <TotalCount>15</TotalCount>
    <PageSize>20</PageSize>
    <CurrentPage>1</CurrentPage>
    <Count>15</Count>
</PageInfo> <RequestId>B41B3780-337A-472D-B82E-9FD3642B9350</RequestId>
```

`JSON` format `{`

```json
    "ImageInstanceList": {
        "VulStatus": "YES",
        "ImageSize": 101,
        "Endpoints": "[]",
        "ScaProgress": 1,
        "ImageId": "asdaSdasd",
        "ImageUpdate": 1639236844747,
        "ScaResult": "None",
        "AlarmCount": 1,
        "HcCount": 0,
        "Status": "NORMAL",
        "RepoNamespace": "hangzhou-namespace",
        "RegistryType": "defaultAcr",
        "InstanceId": "i-km100o6qy8gidwn3****",
        "Digest": "6a5e1031a5858617f7d8a179ead6***",
        "RepoName": "centos1",
        "RiskStatus": "NO",
        "VulCount": 1,
        "ScaStatus": "YES",
        "Uuid": "B41B****-337A-472D-B82E-9FD3642B****",
        "ImageCreate": 1234567890123,
        "RepoType": "PRIVATE",
        "AlarmStatus": "YES",
        "Tag": 0.1,
        "RegionId": "cn-wulan-env116-d01",
        "RepoId": "crr-vridcl4****",
        "HcStatus": "NO"
```

`},`

```json
    "PageInfo": {
        "TotalCount": 15,
        "PageSize": 20,
        "CurrentPage": 1,
        "Count": 15
```

`},`

```json
    "RequestId": "B41B3780-337A-472D-B82E-9FD3642B9350"
```

`}`

### 5.18 ListPrivateRegistryList

Queries third-party image repositories.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ListPrivateRegistryL ist | The operation that you want to perform. Set the value to ListPrivateRegistryList. |
| RegistryType | String | No | defaultAcr | The type of the repository. Set the value to defaultAcr. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| ImageRegistryInf os | Array of ImageRegistryInf o |   | An array that consists of image repositories. |

| AliUid | Long | 1 | The Apsara Stack tenant account. |
|---|---|---|---|
| DomainName | String | 192.168.0.1 | The domain name of the repository. Note An IP address is returned only in an internal network. |
| Id | Long | 1 | The ID of the image repository. |
| NetType | Long | 1 | The type of the network. |
| ProtocolType | Long | 1 | The type of the protocol. |
| RegionId | String | cn-*****-env116-d01 | The region ID. |
| RegistryHostIp | String | 47.100.XX.XX | The IP address of the host on which the repository is deployed. |
| RegistryType | String | defaultAcr | The type of the repository. The value is fixed as defaultAcr. |
| RegistryVersion | String | 1 | The version of the repository. |
| Token | String | 3fa33eb3-16f9-4ee8- 921f-fb558******* | The token. |
| VpcId | String | 112*** | The ID of the virtual private cloud (VPC). |
| WhiteList | String | 47.100.XX.XX/24 | The whitelist. |
| RequestId | String | B41B3780-337A-472D- B82E-9FD3642B9350 | The ID of the request. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=ListPrivateRegistryList &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RequestId>B41B3780-337A-472D-B82E-9FD3642B9350</RequestId> <ImageRegistryInfos>
    <VpcId>112***</VpcId>
    <RegistryType>defaultAcr</RegistryType>
    <DomainName>http://192.168.0.1</DomainName>
    <RegistryHostIp>47.100.XX.XX</RegistryHostIp>
    <ProtocolType>1</ProtocolType>
    <WhiteList>47.100.XX.XX/24</WhiteList>
    <Token>3fa33eb3-16f9-4ee8-921f-fb558*******</Token>
    <RegionId>cn-*****-env116-d01</RegionId>
    <Id>1</Id>
    <NetType>1</NetType>
    <RegistryVersion>1</RegistryVersion>
    <AliUid>1</AliUid>
</ImageRegistryInfos>
```

`JSON` format `{`

```json
    "RequestId": "B41B3780-337A-472D-B82E-9FD3642B9350",
    "ImageRegistryInfos": {
        "VpcId": "112***",
        "RegistryType": "defaultAcr",
        "DomainName": "http://192.168.0.1",
        "RegistryHostIp": "47.100.XX.XX",
        "ProtocolType": 1,
        "WhiteList": "47.100.XX.XX/24",
        "Token": "3fa33eb3-16f9-4ee8-921f-fb558*******",
        "RegionId": "cn-*****-env116-d01",
        "Id": 1,
        "NetType": 1,
        "RegistryVersion": 1,
        "AliUid": 1
```

`}` `}`

### 5.19 ListPrivateRegistryType

Queries the types of image repositories.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ListPrivateRegistryT ype | The operation that you want to perform. Set the value to ListPrivateRegistryType. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RegistryTypeInfos | Array of RegistryTypeInfo |   | An array that consists of the information about repository types. |
| Count | Long | 2 | The number of repositories of the type. |
| RegistryType | String | defaultAcr | The type of the repository. |

| RequestId | String | B41B3780-337A-472D- B82E-9FD3642B9350 | The ID of the request. |
|---|---|---|---|

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=ListPrivateRegistryType &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RegistryTypeInfos>
    <RegistryType>defaultAcr</RegistryType>
    <Count>2</Count>
</RegistryTypeInfos> <RequestId>B41B3780-337A-472D-B82E-9FD3642B9350</RequestId>
```

`JSON` format `{`

```json
    "RegistryTypeInfos": {
        "RegistryType": "defaultAcr",
        "Count": 2
```

`},`

```json
    "RequestId": "B41B3780-337A-472D-B82E-9FD3642B9350"
```

`}`

### 5.20 DescribeAlarmEventDetail

Queries the details of an exception.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeAlarmEven tDetail | The operation that you want to perform. Set the value to DescribeAlarmEventDetail. |
| AlarmUniqueInfo | String | Yes | asdsafasdfadsfasdf* ****** | The unique value that identifies the exception. |
| From | String | Yes | css | The code of the service. Set the value to css. |
| SourceIp | String | No | 47.100.XX.XX | The source IP address of the request. |
| Lang | String | No | zh | The language of the content within the request and response. Valid values: zh: Chinese en: English |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|

| Data | Struct |   | The details of the exception. |
|---|---|---|---|
| AccessCode | String | None | This parameter is deprecated. |
| AlarmEventAliasN ame | String | Webshell - Webshell file | The alias of the alert type. |
| AlarmEventDesc | String | After an attacker accesses a server, the attacker may import malicious shell scripts into scheduled tasks to keep malicious programs running. The scheduled tasks include crontab and systemd. | The description of the alert event. |
| AlarmUniqueInfo | String | asdajshdklahsdj****** | The unique value that identifies the alert event. |
| CanBeDealOnLine | Boolean | false | Indicates whether the online processing of alert events is supported, such as blocking an alert, adding an alert to the whitelist, and ignoring an alert. Valid values: true: yes false: no |
| CanCancelFault | Boolean | false | Indicates whether you can cancel marking the alert as a false positive. Valid values: true: yes false: no |
| CauseDetails | Array of CauseDetail |   | An array that consists of the details about the exception. |
| Key | String | html | The format in the exception details. Valid values: text html |
| Value | Array of Value |   | An array that consists of exception details. |
| Name | String | Solution | The name of the field that displays tracing information. |
| Type | String | html | The format of the field that displays tracing information. Valid values: text html |
| Value | String | [] | The value of the field that displays tracing information. |
| DataSource | String | console | The source of data. |

| Dealed | Boolean | false | The status of the exception. Valid values: true: handled false: unhandled |
|---|---|---|---|
| EndTime | Long | 1639236844747 | The end of the time range during which the exception was handled. The value is a UNIX timestamp. Unit: milliseconds. |
| HasTraceInfo | Boolean | false | This parameter is deprecated. |
| InstanceName | String | worker-k8s-for-cs- cb9218d50728c470fb7 dfbc16577a2673 | The name of the instance. |
| InternetIp | String | 47.100.XX.XX | The public IP address. |
| IntranetIp | String | 192.168.0.1 | The private IP address. |
| Level | String | suspicious | The severity of the exception. Valid values: serious suspicious remind |
| Solution | String | Check the malicious URLs that are listed in the alert. Check the directory for malicious file downloads. Stop the malicious processes that are running. If you trust the processes, mark the alert as a false positive in the console, and submit a ticket to notify security engineers. | The solution to the exception. |
| StartTime | Long | 1234567890123 | The start of the time range during which the exception was handled. The value is a UNIX timestamp. Unit: milliseconds. |

| Type | String | Webshell | The type of the alert event. Valid values: Suspicious process Webshell Unusual logon Exception Sensitive file tampering Malicious process Suspicious network connection Other. Abnormal account. Application intrusion event Cloud threat detection Precise defense Application whitelist. Persistent webshell Web application threat detection Malicious script Threat intelligence. Malicious network activity |
|---|---|---|---|
| Uuid | String | B41B3780-337A-472D- B82E-9FD364****** | The UUID of the asset. |
| RequestId | String | B41B3780-337A-472D- B82E-9FD3642B9350 | The ID of the request. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeAlarmEventDetail &AlarmUniqueInfo=asdsafasdfadsfasdf******* &From=css &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RequestId>B41B3780-337A-472D-B82E-9FD3642B9350</RequestId> <Data>
    <CanCancelFault>false</CanCancelFault>
    <EndTime>1639236844747</EndTime>
    <StartTime>1234567890123</StartTime>
    <AccessCode>None</AccessCode>
    <Dealed>false</Dealed>
    <HasTraceInfo>false</HasTraceInfo>
    <IntranetIp>1.1.1.1</IntranetIp>
    <DataSource>console</DataSource>
    <InstanceName>worker-k8s-for-cs-cb9218d50728c470fb7dfbc16577a2673</InstanceName>
    <CanBeDealOnLine>false</CanBeDealOnLine>
    <Type>Webshell</Type>
    <Uuid>B41B3780-337A-472D-B82E-9FD3642B9350</Uuid>
    <InternetIp>1.1.1.1</InternetIp>
    <AlarmUniqueInfo>asdajshdklahsdjkashdjka</AlarmUniqueInfo>
    <AlarmEventDesc>After an attacker accesses a server, the attacker may import malicious shell
scripts into scheduled tasks to keep malicious programs running. The scheduled tasks include crontab and systemd. </AlarmEventDesc>
    <AlarmEventAliasName>Webshell - Webshell file</AlarmEventAliasName>
    <Level>suspicious</Level>
    <Solution>Check the malicious URLs that are listed in the alert. Check the directory for
malicious file downloads. Stop the malicious processes that are running. If you trust the processes, mark the alert as a false positive in the console, and submit a ticket to notify security engineers. </Solution>
    <CauseDetails>
        <Key>html</Key>
        <Value>
            <Type>html</Type>
            <Value>[]</Value>
            <Name>Solution</Name>
        </Value>
    </CauseDetails>
</Data>
```

`JSON` format `{`

```json
    "RequestId": "B41B3780-337A-472D-B82E-9FD3642B9350",
    "Data": {
        "CanCancelFault": false,
        "EndTime": 1639236844747,
        "StartTime": 1234567890123,
        "AccessCode": "None",
        "Dealed": false,
        "HasTraceInfo": false,
        "IntranetIp": "1.1.1.1",
        "DataSource": "console",
        "InstanceName": "worker-k8s-for-cs-cb9218d50728c470fb7dfbc16577a2673",
        "CanBeDealOnLine": false,
        "Type": "Webshell",
        "Uuid": "B41B3780-337A-472D-B82E-9FD3642B9350",
        "InternetIp": "1.1.1.1",
        "AlarmUniqueInfo": "asdajshdklahsdjkashdjka",
        "AlarmEventDesc": "After an attacker accesses a server, the attacker may import malicious shel
l scripts into scheduled tasks to keep malicious programs running. The scheduled tasks include crontab and systemd.",
        "AlarmEventAliasName": "Webshell - Webshell file",
        "Level": "suspicious",
        "Solution": "Check the malicious URLs that are listed in the alert. Check the directory for ma
licious file downloads. Stop the malicious processes that are running. If you trust the processes, mark the alert as a false positive in the console, and submit a ticket to notify security engineers.",
        "CauseDetails": {
            "Key": "html",
            "Value": {
                "Type": "html",
                "Value": "[]",
                "Name": "Solution"
```

`}` `}` `}` `}`

### 5.21 DescribeNsasSuspEventType

Queries the types of alert events.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeNsasSuspE ventType | The operation that you want to perform. Set the value to DescribeNsasSuspEventType. |
| SourceIp | String | No | 47.100.XX.XX | The source IP address of the request. |
| Remark | String | No | test | The conditions for fuzzy search. |
| Name | String | No | Threat Intelligence | The name of the alert event. |

| Lang | String | No | zh | The language of the content within the request and response. Valid values: zh: Chinese en: English |
|---|---|---|---|---|
| From | String | No | css | The code of the service. Set the value to css. |
| Uuids | String | No | 4b092975242bea7f a4af*******,072829 75242bea7fa4af*** *** | The UUIDs. Separate multiple UUIDs with commas (,). |
| ClusterId | String | No | cb9218d50728c470 fb7dfbc1657****** | The ID of the cluster. |
| ContainerFieldName | String | No | containerId | The type of the search condition that is used to query containers. |
| ContainerFieldValue | String | No | 4b092975242bea7f a4af8515057f660fa f2b285bc1693fd4cb 0e7bfac******* | The search term that is used to query containers. |
| TargetType | String | No | containerId | The information that is used to query the types of alert events. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| EventTypes | Array of Data |   | An array that consists of the types of alert events. |
| Name | String | Threat Intelligence | The name of the exception. |
| SuspEventCount | Integer | 12 | The number of exceptions. |
| Type | String | Threat Intelligence | The type of the exception. |
| RequestId | String | B41B3780-337A-472D- B82E-9FD3642B9350 | The ID of the request. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeNsasSuspEventType &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RequestId>B41B3780-337A-472D-B82E-9FD3642B9350</RequestId> <EventTypes>
    <Type>Threat Intelligence</Type>
    <SuspEventCount>12</SuspEventCount>
    <Name>Threat Intelligence</Name>
</EventTypes>
```

`JSON` format `{`

```json
    "RequestId": "B41B3780-337A-472D-B82E-9FD3642B9350",
    "EventTypes": {
        "Type": "Threat Intelligence",
        "SuspEventCount": 12,
        "Name": "Threat Intelligence"
```

`}` `}`

### 5.22 DescribeSuspEvents

Queries exceptions.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeSuspEvent s | The operation that you want to perform. Set the value to DescribeSuspEvents. |
| SourceIp | String | No | 47.100.XX.XX | The source IP address of the request. |
| Dealed | String | No | Y | The status of the exception. Valid values: N: unhandled Y: handled |
| Name | String | No | ecs-xxx | The name of the exception or the hostname of the server. |
| Levels | String | No | serious | The severity of the exception. Separate multiple severities with commas (,). Valid values: serious suspicious remind |
| ParentEventTypes | String | No | Webshell | The type of the alert with which the exception is associated. |
| Remark | String | No | test | The IP address or hostname of the server. |
| Status | String | No | None | This parameter is deprecated. |
| PageSize | String | No | 20 | The number of entries to return on each page. |

| CurrentPage | String | No | 1 | The number of the page to return. |
|---|---|---|---|---|
| Lang | String | No | zh | The language of the content within the request and response. Valid values: zh: Chinese en: English |
| AlarmUniqueInfo | String | No | asdhlashdlkah****** * | The unique identifier of the alert event. |
| UniqueInfo | String | No | a097975445d891dd f86a3f56****** | The unique information. |
| From | String | No | css | The code of the service. Set the value to css. |
| Source | String | No | None | This parameter is deprecated. |
| GroupId | Long | No | 1 | This parameter is deprecated. |
| Uuids | String | No | None | This parameter is deprecated. |
| OperateErrorCodeLi st.N | RepeatList | No | [] | The error codes. |
| ClusterId | String | No | asdjashdkashdkj*** * | The ID of the cluster to which the container belongs. |
| ContainerFieldName | String | No | appName | The key that is used to query the container. |
| ContainerFieldValue | String | No | nginx-ingress- controller | The value that is used to query the container. |
| TargetType | String | No | containerId | The container that matches both the value of ContainerFieldValue and the value of ContainerFieldName. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Count | Integer | 20 | The total number of returned pages. |
| CurrentPage | Integer | 1 | The page number of the returned page. |
| PageSize | Integer | 20 | The number of entries returned per page. |
| RequestId | String | B41B3780-337A-472D- B82E-9FD3642B9350 | The ID of the request. |
| SuspEvents | Array of WarningSummary |   | The content of the exception. |

| Advanced | Boolean | false | Indicates whether the Advanced edition is used. true: yes false: no |
|---|---|---|---|
| AlarmEventName | String | DDoS trojan | The name of the exception. |
| AlarmEventName Display | String | None | This parameter is deprecated. |
| AlarmEventType | String | Malicious process | The type of the alert event. Valid values: Suspicious process Webshell Unusual logon Exception Sensitive file tampering Malicious process Suspicious network connection Other Abnormal account Application intrusion event Cloud threat detection Precise defense Application whitelist Persistent webshell Web application threat detection Malicious script Threat intelligence Malicious network activity |
| AlarmEventType Display | String | None | This parameter is deprecated. |
| AlarmUniqueInfo | String | asdhkashdkash**** | The unique identifier of the alert event. |
| AppName | String | app1 | The name of the application. |
| AssetType | Integer | 0 | The type of the asset. Valid values: 0: Elastic Compute Service (ECS) instance 1: Server Load Balancer (SLB) instance 2: NAT gateway 3: ApsaraDB RDS database 4: ApsaraDB for MongoDB database 6: container image 7: container |
| AutoBreaking | Boolean | false | Indicates whether the exception is automatically blocked. true: yes false: no |

| CanBeDealOnLine | Boolean | false | Indicates whether the online processing of alert events is supported, such as blocking an alert, adding an alert to the whitelist, and ignoring an alert. Valid values: true: yes false: no |
|---|---|---|---|
| CanCancelFault | Boolean | false | Indicates whether you can cancel marking the alert as a false positive. Valid values: true: yes false: no |
| ContainHwMode | Boolean | false | This parameter is deprecated. |
| ContainerId | String | asdaksDaksh****** | The ID of the container. |
| ContainerImageId | String | asdalsdka****** | The ID of the image to which the container belongs. |
| ContainerImageN ame | String | name1 | The name of the image to which the container belongs. |
| DataSource | String | aegis suspicious *** _ _ | The data source on which the exception is detected. |
| Desc | String | The threat detection model detected that the command line data of a process on your server was highly suspicious. This may be related to trojans, viruses, or attackers. | The description of the exception. |
| Details | Array of QuaraFile |   | The details of the exception. |
| InfoType | String | None | This parameter is deprecated. |
| Name | String | ${suspicious.sp.rs.des cription} | The keyword that identifies the exception for internationalization. |
| NameDisplay | String | Event description | The display name of the exception. |
| Type | String | text | The format in which the details of the exception are displayed. Valid values: text html |
| Value | String | The threat detection model detected that the command line data of a process on your server was highly suspicious. This may be related to trojans, viruses, or attackers. | The detailed content of the exception. |

| ValueDisplay | String | The threat detection model detected that the command line data of a process on your server was highly suspicious. This may be related to trojans, viruses, or attackers. | The detailed content that is displayed. |
|---|---|---|---|
| EventNotes | Array of EventNote |   | This parameter is deprecated. |
| Note | String | None | This parameter is deprecated. |
| NoteId | Long | 1 | This parameter is deprecated. |
| NoteTime | String | None | This parameter is deprecated. |
| EventStatus | Integer | 1 | The status of the alert event. Valid values: 1: pending handling 2: ignored 4: confirmed 8: marked as a false positive 16: handling 32: handled 64: expired |
| EventSubType | String | Suspicious process | The type of the alert event. Valid values: Suspicious process Webshell Unusual logon Exception Sensitive file tampering Malicious process Suspicious network connection Other Abnormal account Application intrusion event Cloud threat detection Precise defense Application whitelist Persistent webshell Web application threat detection Malicious script Threat intelligence Malicious network activity |
| HasTraceInfo | Boolean | false | This parameter is deprecated. |
| Id | Long | 1 | The ID. |
| InstanceId | String | i-asdasdjhkjh****** | The ID of the instance. |

| InstanceName | String | worker-k8s-for-cs- cb9218d50728c470fb7 dfbc16577a2673 | The name of the instance. |
|---|---|---|---|
| InternetIp | String | 47.100.XX.XX | The public IP address. |
| IntranetIp | String | 192.168.0.1 | The private IP address. |
| K8sClusterId | String | asdasdkah****** | The ID of the Kubernetes cluster. |
| K8sClusterName | String | cqqtesttest | The name of the Kubernetes cluster. |
| K8sNamespace | String | hangzhou-namespace | The namespace of the Kubernetes cluster. |
| K8sNodeId | String | nod****** | The ID of the node in the Kubernetes cluster. |
| K8sNodeName | String | nodeName1 | The name of the node in the Kubernetes cluster. |
| K8sPodName | String | PodName1 | The name of the pod in the Kubernetes cluster. |
| LastTime | String | 2022-01-06 18:41:24 | The time when the exception was last updated. The time is in the yyyy-MM-dd HH:mm:ss format. |
| LastTimeStamp | Long | 1234567890123 | The timestamp when the exception was last updated. The value is a UNIX timestamp. Unit: milliseconds. |
| Level | String | serious | The severity of the exception. serious suspicious remind |
| LogAnalysis | String | None | This parameter is deprecated. |
| LogFromTime | Long | 1 | This parameter is deprecated. |
| LogToTime | Long | 1 | This parameter is deprecated. |
| MarkMisRules | String | None | This parameter is deprecated. |
| Name | String | ${suspicious.sp.rs.des cription} | The keyword that identifies the exception for internationalization. |
| OccurrenceTime | String | 2022-01-06 18:41:24 | The time when the exception was detected. The time is in the yyyy-MM-dd HH:mm:ss format. |
| OccurrenceTimeS tamp | Long | 1234567890123 | The timestamp when the exception was detected. The value is a UNIX timestamp. Unit: milliseconds. |

| OperateErrorCod e | String | quara.Succes | The handling result of the exception. |
|---|---|---|---|
| OperateMsg | String | succes | The message that describes the handling result of the exception. |
| OperateTime | Long | 1234567890123 | The time when the exception was handled. The value is a UNIX timestamp. Unit: milliseconds. |
| RegionId | String | cn-*****-env116-d01 | The region ID. |
| SaleVersion | String | None | This parameter is deprecated. |
| SecurityEventIds | String | 1212*** | The ID of the exception. |
| Stages | String | None | This parameter is deprecated. |
| TraceBackInfo | String | None | This parameter is deprecated. |
| UniqueInfo | String | asdljkhaskl****** | The unique information. |
| Uuid | String | B41B3780-337A-472D- B82E-9FD364****** | The UUID of the asset. |
| TotalCount | Integer | 35 | The total number of entries returned. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeSuspEvents &<Common request parameters>
```

Sample success responses `XML` format

```xml
<TotalCount>35</TotalCount> <PageSize>20</PageSize> <RequestId>B41B3780-337A-472D-B82E-9FD3642B9350</RequestId> <CurrentPage>1</CurrentPage> <Count>20</Count> <SuspEvents>
    <K8sNodeId>nod******</K8sNodeId>
    <K8sNodeName>nodeName1</K8sNodeName>
    <ContainHwMode>false</ContainHwMode>
    <HasTraceInfo>false</HasTraceInfo>
    <IntranetIp>192.168.0.1</IntranetIp>
    <K8sClusterId>asdasdkah******</K8sClusterId>
    <Name>${suspicious.sp.rs.description}</Name>
    <K8sNamespace>hangzhou-namespace</K8sNamespace>
    <Desc>The threat detection model detected that the command line data of a process on your server w
as highly suspicious. This may be related to trojans, viruses, or attackers. </Desc>
    <TraceBackInfo>None</TraceBackInfo>
    <InternetIp>47.100.XX.XX</InternetIp>
    <ContainerId>asdaksDaksh******</ContainerId>
    <AlarmEventType>Malicious process</AlarmEventType>
```

`a`

```
etype
```

`a`

```
couspocess/
```

`a`

```xml
etype
    <LogToTime>1</LogToTime>
    <AlarmEventNameDisplay>None</AlarmEventNameDisplay>
    <UniqueInfo>asdljkhaskl******</UniqueInfo>
    <CanCancelFault>false</CanCancelFault>
    <InstanceId>i-asdasdjhkjh******</InstanceId>
    <LogFromTime>1</LogFromTime>
    <SaleVersion>None</SaleVersion>
    <ContainerImageId>asdalsdka******</ContainerImageId>
    <DataSource>aegis_suspicious_***</DataSource>
    <LogAnalysis>None</LogAnalysis>
    <InstanceName>worker-k8s-for-cs-cb9218d50728c470fb7dfbc16577a2673</InstanceName>
    <OccurrenceTime>2022-01-06 18:41:24</OccurrenceTime>
    <OperateTime>1234567890123</OperateTime>
    <CanBeDealOnLine>false</CanBeDealOnLine>
    <K8sClusterName>cqqtesttest</K8sClusterName>
    <ContainerImageName>name1</ContainerImageName>
    <AlarmUniqueInfo>asdhkashdkash****</AlarmUniqueInfo>
    <OccurrenceTimeStamp>1234567890123</OccurrenceTimeStamp>
    <Level>serious</Level>
    <Id>1</Id>
    <Advanced>false</Advanced>
    <OperateErrorCode>quara.Succes</OperateErrorCode>
    <AlarmEventName>DDoS trojan</AlarmEventName>
    <SecurityEventIds>1212***</SecurityEventIds>
    <EventStatus>1</EventStatus>
    <EventSubType>Suspicious process</EventSubType>
    <AppName>app1</AppName>
    <LastTimeStamp>1234567890123</LastTimeStamp>
    <AlarmEventTypeDisplay>None</AlarmEventTypeDisplay>
    <Stages>None</Stages>
    <MarkMisRules>None</MarkMisRules>
    <K8sPodName>PodName1</K8sPodName>
    <OperateMsg>succes</OperateMsg>
    <AssetType>0</AssetType>
    <Uuid>B41B3780-337A-472D-B82E-9FD364******</Uuid>
    <AutoBreaking>false</AutoBreaking>
    <RegionId>cn-*****-env116-d01</RegionId>
    <LastTime>2022-01-06 18:41:24</LastTime>
    <Details>
        <Type>text</Type>
        <Value>The threat detection model detected that the command line data of a process on your ser
ver was highly suspicious. This may be related to trojans, viruses, or attackers. </Value>
        <ValueDisplay>The threat detection model detected that the command line data of a process on y
our server was highly suspicious. This may be related to trojans, viruses, or attackers. </ValueDisplay>
        <InfoType>None</InfoType>
        <NameDisplay>Event description</NameDisplay>
        <Name>${suspicious.sp.rs.description}</Name>
    </Details>
    <EventNotes>
        <NoteId>1</NoteId>
        <Note>None</Note>
        <NoteTime>None</NoteTime>
    </EventNotes>
</SuspEvents>
```

`JSON` format `{`

```json
    "TotalCount": 35,
    "PageSize": 20,
    "RequestId": "B41B3780-337A-472D-B82E-9FD3642B9350",
```

```json
    "CurrentPage": 1,
    "Count": 20,
    "SuspEvents": {
        "K8sNodeId": "nod******",
        "K8sNodeName": "nodeName1",
        "ContainHwMode": false,
        "HasTraceInfo": false,
        "IntranetIp": "192.168.0.1",
        "K8sClusterId": "asdasdkah******",
        "Name": "${suspicious.sp.rs.description}",
        "K8sNamespace": "hangzhou-namespace",
        "Desc": "The threat detection model detected that the command line data of a process on your s
erver was highly suspicious. This may be related to trojans, viruses, or attackers.",
        "TraceBackInfo": "None",
        "InternetIp": "47.100.XX.XX",
        "ContainerId": "asdaksDaksh******",
        "AlarmEventType": "Malicious process",
        "LogToTime": 1,
        "AlarmEventNameDisplay": "None",
        "UniqueInfo": "asdljkhaskl******",
        "CanCancelFault": false,
        "InstanceId": "i-asdasdjhkjh******",
        "LogFromTime": 1,
        "SaleVersion": "None",
        "ContainerImageId": "asdalsdka******",
        "DataSource": "aegis_suspicious_***",
        "LogAnalysis": "None",
        "InstanceName": "worker-k8s-for-cs-cb9218d50728c470fb7dfbc16577a2673",
        "OccurrenceTime": "2022-01-06 18:41:24",
        "OperateTime": 1234567890123,
        "CanBeDealOnLine": false,
        "K8sClusterName": "cqqtesttest",
        "ContainerImageName": "name1",
        "AlarmUniqueInfo": "asdhkashdkash****",
        "OccurrenceTimeStamp": 1234567890123,
        "Level": "serious",
        "Id": 1,
        "Advanced": false,
        "OperateErrorCode": "quara.Succes",
        "AlarmEventName": "DDoS trojan",
        "SecurityEventIds": "1212***",
        "EventStatus": 1,
        "EventSubType": "Suspicious process",
        "AppName": "app1",
        "LastTimeStamp": 1234567890123,
        "AlarmEventTypeDisplay": "None",
        "Stages": "None",
        "MarkMisRules": "None",
        "K8sPodName": "PodName1",
        "OperateMsg": "succes",
        "AssetType": 0,
        "Uuid": "B41B3780-337A-472D-B82E-9FD364******",
        "AutoBreaking": false,
        "RegionId": "cn-*****-env116-d01",
        "LastTime": "2022-01-06 18:41:24",
        "Details": {
            "Type": "text",
            "Value": "The threat detection model detected that the command line data of a process on y
our server was highly suspicious. This may be related to trojans, viruses, or attackers.",
            "ValueDisplay": "The threat detection model detected that the command line data of a proce
ss on your server was highly suspicious. This may be related to trojans, viruses, or attackers.",
            "InfoType": "None",
            "NameDisplay": "Event description",
```

`p` `y` `p` `,`

```json
            "Name": "${suspicious.sp.rs.description}"
```

`},`

```json
        "EventNotes": {
            "NoteId": 1,
            "Note": "None",
            "NoteTime": "None"
```

`}` `}` `}`

### 5.23 DescribeConcernNecessity

Queries the severities of alert events.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeConcernNe cessity | The operation that you want to perform. Set the value to DescribeConcernNecessity. |
| Lang | String | No | zh | The language of the content within the request and response. Valid values: zh: Chinese en: English |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| ConcernNecessity | List | ["nntf", "later", "asap"] | The severities of alert events. nntf: low later: medium asap: high |
| RequestId | String | B41B3780-337A-472D- B82E-9FD3642B9350 | The ID of the request. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeConcernNecessity &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RequestId>B41B3780-337A-472D-B82E-9FD3642B9350</RequestId> <ConcernNecessity>["nntf", "later", "asap"]</ConcernNecessity>
```

`JSON` format `{`

```json
    "RequestId": "B41B3780-337A-472D-B82E-9FD3642B9350",
    "ConcernNecessity": "[\"nntf\", \"later\", \"asap\"]"
```

`}`

### 5.24 DescribeEventLevelCount

Queries the severities of alerts.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeEventLevel Count | The operation that you want to perform. Set the value to DescribeEventLevelCount. |
| SourceIp | String | No | 47.100.XX.XX | The source IP address of the request. |
| Type | String | No | alarm | The type of the query. Set the value to alarm. |
| From | String | No | css | The code of the service. Set the value to css. |
| ClusterId | String | No | Cccfd68c47445466 5ace07efce924*** | The ID of the cluster to which the container belongs. |
| ContainerFieldName | String | No | containerId | The key that is used to query the container. |
| ContainerFieldValue | String | No | 4b092975242bea7f a4af8515057f660fa f2b285bc1693fd4cb 0e7bfac***** | The value that is used to query the container. |
| TargetType | String | No | containerId | The container that matches both the value of ContainerFieldName and the value of ContainerFieldValue. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| EventLevels | Struct |   | The alerts. |
| Remind | Integer | 1 | The number of alerts that have the remind severity. |
| Serious | Integer | 2 | The number of alerts that have the serious severity. |
| Suspicious | Integer | 3 | The number of alerts that have the suspicious severity. |
| RequestId | String | B41B3780-337A-472D- B82E-9FD3642B9350 | The ID of the request. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeEventLevelCount &<Common request parameters>
```

Sample success responses `XML` format

```xml
<EventLevels>
    <Serious>2</Serious>
    <Suspicious>3</Suspicious>
    <Remind>1</Remind>
</EventLevels> <RequestId>B41B3780-337A-472D-B82E-9FD3642B9350</RequestId>
```

`JSON` format `{`

```json
    "EventLevels": {
        "Serious": 2,
        "Suspicious": 3,
        "Remind": 1
```

`},`

```json
    "RequestId": "B41B3780-337A-472D-B82E-9FD3642B9350"
```

`}`

### 5.25 DescribeSecurityEventOperations

Queries the operations that are performed on alert events.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeSecurityEv entOperations | The operation that you want to perform. Set the value to DescribeSecurityEventOperations. |
| SourceIp | String | No | 47.100.XX.XX | The source IP address of the request. |
| Lang | String | No | zh | The language of the content within the request and response. Valid values: zh: Chinese en: English |
| SecurityEventId | Long | No | 1 | The ID of the alert event. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | B41B3780-337A-472D- B82E-9FD3642B9350 | The ID of the request. |
| SecurityEventOpe rationsResponse | Array of SecurityEventOpe ration |   | An array that consists of the operations performed on alert events. |

| MarkField | Array of MarkField |   | This parameter is deprecated. |
|---|---|---|---|
| FiledAliasName | String | None | This parameter is deprecated. |
| FiledName | String | None | This parameter is deprecated. |
| MarkMisType | String | None | This parameter is deprecated. |
| MarkMisValue | String | None | This parameter is deprecated. |
| SupportedMisTyp e | List | None | This parameter is deprecated. |
| MarkFieldsSource | Array of SecurityEventOpe ration |   | An array that consists of the information of the alert events. |
| FiledAliasName | String | Process path | The name of the alert. |
| FiledName | String | proc path _ | The key of the field. |
| MarkMisValue | String | /usr/bin/ps | The operation instruction. |
| SupportedMisTyp e | List | ["contains", "notContains", "regex", "strEqual", "strNotEqual"] | The operations that can be performed. |
| OperationCode | String | ignore | The operation performed on the alert event. Valid values: ignore: ignores the alerts. advance mark mis info: adds the alert to the _ _ _ whitelist. manual handled: manually handled. _ |
| OperationParams | String | demo | The parameters of the operation. |
| UserCanOperate | Boolean | false | Indicates whether you can handle the alert. Valid values: true: yes false: no |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeSecurityEventOperations &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RequestId>B41B3780-337A-472D-B82E-9FD3642B9350</RequestId> <SecurityEventOperationsResponse>
    <OperationParams>demo</OperationParams>
    <OperationCode>ignore</OperationCode>
    <UserCanOperate>false</UserCanOperate>
    <MarkField>
        <FiledName>None</FiledName>
        <MarkMisValue>None</MarkMisValue>
        <MarkMisType>None</MarkMisType>
        <FiledAliasName>None</FiledAliasName>
        <SupportedMisType>None</SupportedMisType>
    </MarkField>
    <MarkFieldsSource>
        <FiledName>proc_path</FiledName>
        <MarkMisValue>/usr/bin/ps</MarkMisValue>
        <FiledAliasName>Process path</FiledAliasName>
        <SupportedMisType>["contains", "notContains", "regex", "strEqual", "strNotEqual"]</SupportedMi
sType>
    </MarkFieldsSource>
</SecurityEventOperationsResponse>
```

`JSON` format `{`

```json
    "RequestId": "B41B3780-337A-472D-B82E-9FD3642B9350",
    "SecurityEventOperationsResponse": {
        "OperationParams": "demo",
        "OperationCode": "ignore",
        "UserCanOperate": false,
        "MarkField": {
            "FiledName": "None",
            "MarkMisValue": "None",
            "MarkMisType": "None",
            "FiledAliasName": "None",
            "SupportedMisType": "None"
```

`},`

```json
        "MarkFieldsSource": {
            "FiledName": "proc_path",
            "MarkMisValue": "/usr/bin/ps",
            "FiledAliasName": "Process path",
            "SupportedMisType": "[\"contains\", \"notContains\", \"regex\", \"strEqual\",
\"strNotEqual\"]"
```

`}` `}` `}`

### 5.26 DescribeGroupedVul

Queries vulnerabilities by group.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeGroupedVu l | The operation that you want to perform. Set the value to DescribeGroupedVul. |
| SourceIp | String | No | 47.100.XX.XX | The source IP address of the request. |

| Lang | String | No | zh | The language of the content within the request and response. Valid values: zh: Chinese en: English |
|---|---|---|---|---|
| Type | String | No | cve | The type of the vulnerability. Valid values: CVE: image system vulnerabilities SCA: image application vulnerabilities |
| GroupId | String | No | None | This parameter is deprecated. |
| CveId | String | No | q3w4er12*** | The Common Vulnerabilities and Exposures (CVE) ID of the vulnerability. |
| Uuids | String | No | uuid1,uuid2 | The UUID of the asset. Separate multiple UUIDs with commas (,). |
| Name | String | No | debian:10:CVE- 2019-9893 | The name of the vulnerability. |
| AliasName | String | No | DSA-2019 libseccomp security vulnerability | The alias of the vulnerability. |
| PatchId | Long | No | 1 | This parameter is deprecated. |
| Level | String | No | None | This parameter is deprecated. |
| LastTsStart | Long | No | 1 | This parameter is deprecated. |
| LastTsEnd | Long | No | 1 | This parameter is deprecated. |
| StatusList | String | No | None | This parameter is deprecated. |
| OrderBy | String | No | None | This parameter is deprecated. |
| Direction | String | No | None | This parameter is deprecated. |
| Necessity | String | No | later,nntf,asap | The severity of the vulnerability. Separate multiple severities with commas (,). Valid values: serious suspicious remind |
| Dealed | String | No | Y | The status of the vulnerability. Valid values: N: unhandled Y: handled |
| CreateTsStart | Long | No | 1 | This parameter is deprecated. |

| CreateTsEnd | Long | No | 1 | This parameter is deprecated. |
|---|---|---|---|---|
| CurrentPage | Integer | No | 1 | The number of the page to return. |
| PageSize | Integer | No | 20 | The number of entries to return on each page. |
| SearchTags | String | No | None | This parameter is deprecated. |
| AttachTypes | String | No | sca | The type of the vulnerability. Valid values: CVE: image system vulnerabilities SCA: image application vulnerabilities |
| ContainerFieldName | String | No | containerId | The key that is used to query the container. |
| ContainerFieldValue | String | No | 4b092975242bea7f a4af85150*****faf2 b285bc1693fd4cb0 e7bfac300f5c7 | The value that is used to query the container. |
| TargetType | String | No | containerId | The container that matches both the value of ContainerFieldName and the value of ContainerFieldValue. |
| ClusterId | String | No | cs-adasdas | The ID of the cluster to which the container belongs. |
| MinScore | Integer | No | 1 | This parameter is deprecated. |
| VpcInstanceIds | String | No | None | This parameter is deprecated. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| CurrentPage | Integer | 1 | The page number of the returned page. |
| GroupedVulItems | Array of GroupedVulItem |   | An array that consists of the vulnerabilities by group. |
| AliasName | String | DSA-2019 libseccomp security vulnerability | The alias of the vulnerability. |
| AsapCount | Integer | 1 | The number of vulnerabilities that have the high priority. |
| GmtLast | Long | 1234567890123 | The timestamp when the last scan was performed. Unit: milliseconds. |
| HandledCount | Integer | 1 | The number of handled vulnerabilities. |

| LaterCount | Integer | 2 | The number of vulnerabilities that have the medium priority. |
|---|---|---|---|
| Name | String | debian:10:CVE-2019- 9893 | The name of the vulnerability. |
| NntfCount | Integer | 4 | The number of vulnerabilities that have the low risks. |
| Status | Integer | 0 | The status of the vulnerability. Valid values: 0: unhandled 1: handled 2: being verified 3: added to the whitelist |
| Tags | String | Code execution | The tag that is added to the vulnerability. Valid values: Restart required Remote exploitation Exploit exists Exploitable Privilege escalation Code execution |
| TotalFixCount | Long | 233 | The total number of fixed vulnerabilities. |
| Type | String | cve | Valid values: CVE: image system vulnerabilities SCA: image application vulnerabilities |
| PageSize | Integer | 20 | The number of entries returned per page. |
| RequestId | String | B41B3780-337A-472D- B82E-9FD3642B9350 | The ID of the request. |
| TotalCount | Integer | 25 | The total number of entries returned. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeGroupedVul &<Common request parameters>
```

Sample success responses `XML` format

```xml
<TotalCount>25</TotalCount> <PageSize>20</PageSize> <RequestId>B41B3780-337A-472D-B82E-9FD3642B9350</RequestId> <CurrentPage>1</CurrentPage> <GroupedVulItems>
    <Status>0</Status>
    <Type>cve</Type>
    <LaterCount>2</LaterCount>
    <GmtLast>1234567890123</GmtLast>
    <HandledCount>1</HandledCount>
    <AliasName>DSA-2019 libseccomp security vulnerability</AliasName>
    <AsapCount>1</AsapCount>
    <TotalFixCount>233</TotalFixCount>
    <NntfCount>4</NntfCount>
    <Tags>Code execution</Tags>
    <Name>debian:10:CVE-2019-9893</Name>
</GroupedVulItems>
```

`JSON` format `{`

```json
    "TotalCount": 25,
    "PageSize": 20,
    "RequestId": "B41B3780-337A-472D-B82E-9FD3642B9350",
    "CurrentPage": 1,
    "GroupedVulItems": {
        "Status": 0,
        "Type": "cve",
        "LaterCount": 2,
        "GmtLast": 1234567890123,
        "HandledCount": 1,
        "AliasName": "DSA-2019 libseccomp security vulnerability",
        "AsapCount": 1,
        "TotalFixCount": 233,
        "NntfCount": 4,
        "Tags": "Code execution",
        "Name": "debian:10:CVE-2019-9893"
```

`}` `}`

### 5.27 DescribeImageGroupedVulList

Queries image vulnerabilities by group.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeImageGrou pedVulList | The operation that you want to perform. Set the value to DescribeImageGroupedVulList. |
| Type | String | No | sca | The type of the vulnerability that you want to query. Valid values: CVE: image system vulnerability SCA: image application vulnerability |
| GroupId | String | No | 12345*** | The ID of the asset group. |

| CveId | String | No | CVE-2017-15420 | The Common Vulnerabilities and Exposures (CVE) ID of the vulnerability. |
|---|---|---|---|---|
| Uuids | String | No | uuid1,uuid2,uuid3 | The IDs of assets. Separate multiple IDs with commas (,). |
| AliasName | String | No | DSA-2019 libseccomp security vulnerability | The alias of the vulnerability. |
| PatchId | Long | No | 1 | The ID of the patch that is used to fix the vulnerability. |
| Necessity | String | No | later,nntf,asap | The priority to fix the vulnerability. Separate multiple priorities with commas (,). Valid values: asap: high later: medium nntf: low |
| CurrentPage | Integer | No | 1 | The number of the page to return. |
| PageSize | Integer | No | 20 | The number of entries to return on each page. |
| RepoRegionId | String | No | cn-********* | The region ID of the image repository. |
| RepoInstanceId | String | No | cri-adasdasdsda*** | The ID of the container image. |
| RepoId | String | No | crr-dadsdafs**** | The ID of the image repository. |
| RepoName | String | No | centos1 | The name of the image repository. |
| RepoNamespace | String | No | hangzhou- namespace | The namespace to which the image repository belongs. |
| ImageTag | String | No | 0.2 | The tag that is added to the image. |
| ImageDigest | String | No | 6a5e103187b31a94 592a47a5858617f7 a179ead61df7606* **** | The digest of the image. |
| ImageLayer | String | No | 27213ad375b53628 dd152a5ca**** | The information about the image layer. |
| Lang | String | No | zh | The language of the content within the request and response. Valid values: zh: Chinese en: English |

| IsLatest | Integer | No | 0 | Specifies whether to query the vulnerabilities in the latest images. If you do not specify this parameter, the vulnerabilities of all images are queried. Valid values: 0: no 1: yes |
|---|---|---|---|---|

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| CurrentPage | Integer | 1 | The page number of the returned page. |
| GroupedVulItems | Array of GroupedVulItem |   | An array that consists of the vulnerabilities by group. |
| AliasName | String | DSA-2019 libseccomp security vulnerability | The alias of the vulnerability. |
| AsapCount | Integer | 1 | The number of vulnerabilities that have the high priority. |
| GmtLast | Long | 1234567890123 | The time when the status of the image vulnerability is last modified. The value is a UNIX timestamp. Unit: milliseconds. |
| LastScanTime | Long | 1234567890123 | The last scan time. The value is a UNIX timestamp. Unit: milliseconds. |
| LaterCount | Integer | 2 | The number of vulnerabilities that have the medium priority. |
| Name | String | debian:10:CVE-2019- 9893 | The name of the vulnerability. |
| NntfCount | Integer | 3 | The number of vulnerabilities that have the low priority. |
| Status | Integer | 0 | The status of the vulnerability. Valid values: 0: unhandled 1: handled 2: being verified 3: added to the whitelist |
| Tags | String | Code execution | The tag that is added to the vulnerability. Valid values: Restart required Remote exploitation Exploit exists Exploitable Privilege escalation Code execution |

| Type | String | sca | The type of the vulnerability. Valid values: CVE: image system vulnerability SCA: image application vulnerability |
|---|---|---|---|
| PageSize | Integer | 20 | The number of entries returned per page. |
| RequestId | String | B41B3780-337A-472D- B82E-9FD3642B9350 | The ID of the request. |
| TotalCount | Integer | 27 | The total number of entries returned. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeImageGroupedVulList &<Common request parameters>
```

Sample success responses `XML` format

```xml
<TotalCount>27</TotalCount> <PageSize>20</PageSize> <RequestId>B41B3780-337A-472D-B82E-9FD3642B9350</RequestId> <CurrentPage>1</CurrentPage> <GroupedVulItems>
    <Status>0</Status>
    <Type>sca</Type>
    <LaterCount>2</LaterCount>
    <GmtLast>1234567890123</GmtLast>
    <AliasName>DSA-2019 libseccomp security vulnerability</AliasName>
    <AsapCount>1</AsapCount>
    <LastScanTime>1234567890123</LastScanTime>
    <NntfCount>3</NntfCount>
    <Tags>Code execution</Tags>
    <Name>debian:10:CVE-2019-9893</Name>
</GroupedVulItems>
```

`JSON` format `{`

```json
    "TotalCount": 27,
    "PageSize": 20,
    "RequestId": "B41B3780-337A-472D-B82E-9FD3642B9350",
    "CurrentPage": 1,
    "GroupedVulItems": {
        "Status": 0,
        "Type": "sca",
        "LaterCount": 2,
        "GmtLast": 1234567890123,
        "AliasName": "DSA-2019 libseccomp security vulnerability",
        "AsapCount": 1,
        "LastScanTime": 1234567890123,
        "NntfCount": 3,
        "Tags": "Code execution",
        "Name": "debian:10:CVE-2019-9893"
```

`}` `}`

### 5.28 DescribeAllGroups

Queries the grouping information about servers.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeAllGroups | The operation that you want to perform. Set the value to DescribeAllGroups. |
| Lang | String | No | zh | The language of the content within the request and response. Valid values: zh: Chinese en: English |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Count | Integer | 1 | The total number of groups. |
| Groups | Array of Group |   | An array that consists of the grouping information. |
| GroupFlag | Integer | 0 | The type of the server group. Valid values: 0: default group 1: other groups |
| GroupId | Integer | 123 | The ID of the group. |
| GroupName | String | abc | The name of the group. |
| RequestId | String | 7E0618A9-D5EF-4220- 9471-C42B5E92719F | The ID of the request. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeAllGroups &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RequestId>7E0618A9-D5EF-4220-9471-C42B5E92719F</RequestId> <Groups>
    <GroupName>abc</GroupName>
    <GroupFlag>0</GroupFlag>
    <GroupId>123</GroupId>
</Groups> <Count>1</Count>
```

`JSON` format `{`

```json
    "RequestId": "7E0618A9-D5EF-4220-9471-C42B5E92719F",
    "Groups": {
        "GroupName": "abc",
        "GroupFlag": 0,
        "GroupId": 123
```

`},`

```json
    "Count": 1
```

`}`

### 5.29 DescribeImageVulList

Queries image vulnerabilities.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeImageVulLi st | The operation that you want to perform. Set the value to DescribeImageVulList. |
| Lang | String | No | zh | The language of the content within the request and response. Valid values: zh: Chinese en: English |
| Type | String | No | cve | The type of the vulnerability. Valid values: CVE: image system vulnerability SCA: image application vulnerability |
| Uuids | String | No | uuid1,uuid2 | The IDs of assets. Separate multiple IDs with commas (,). |
| Name | String | No | debian:10:CVE- 2019-9893 | The name of the vulnerability. |
| AliasName | String | No | DSA-2019 libseccomp security vulnerability | The alias of the vulnerability. |
| StatusList | String | No | None | This parameter is deprecated. |
| Necessity | String | No | later,nntf,asap | The priority to fix the vulnerability. Separate multiple priorities with commas (,). Valid values: asap: high later: medium nntf: low |
| Dealed | String | No | N | The status of the vulnerability. Valid values: Y: handled N: unhandled |
| CurrentPage | Integer | No | 1 | The number of the page to return. |

| PageSize | Integer | No | 20 | The number of entries to return on each page. |
|---|---|---|---|---|
| RepoRegionId | String | No | cn-hangzhou | The region ID of the image repository. |
| RepoInstanceId | String | No | cri-datvailb**** | The ID of the container image. |
| RepoId | String | No | crr-vridcl4**** | The ID of the image repository. |
| RepoName | String | No | centos1 | The name of the image repository. |
| RepoNamespace | String | No | hangzhou- namespace | The namespace to which the image repository belongs. |
| RegionId | String | No | cn-******** | The region ID. |
| InstanceId | String | No | i-qeqew******* | The ID of the instance. |
| Tag | String | No | None | This parameter is deprecated. |
| Digest | String | No | None | This parameter is deprecated. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| CurrentPage | Integer | 1 | The page number of the returned page. |
| PageSize | Integer | 20 | The number of entries returned per page. |
| RequestId | String | B41B3780-337A-472D- B82E-9FD3642B9350 | The ID of the request. |
| TotalCount | Integer | 25 | The total number of entries returned. |
| VulRecords | Array of VulRecord |   | An array that consists of the vulnerabilities. |
| AliasName | String | DSA-2019 libseccomp security vulnerability | The alias of the vulnerability. |
| CanUpdate | Boolean | false | Indicates whether the information about the vulnerability can be modified. Valid values: true false |
| ExtendContentJso n | Struct |   | The extended information about the vulnerability. |
| Os | String | centos | The name of the operating system. |

| OsRelease | String | 7 | The version of the operating system. |
|---|---|---|---|
| RpmEntityList | Array of RpmEntity |   | An array that consists of the information about RPM Package Manager (RPM) packages. |
| FullVersion | String | 1.4.3-12.el7 6.2 _ | The complete version number. |
| Layer | String | 27213ad3447f0209dd 152a5cadea**** | The image layer. |
| MatchDetail | String | libssh2 version less than 0:1.4.3-12.el7 6.3 _ | The details about how the vulnerability was detected. |
| MatchList | String | libglib2.0-0 version less than 2.50.3- 2+deb9u1 | The rule that is used to detect the vulnerability. |
| Name | String | libssh2 | The name of the RPM package. |
| Path | String | /usr/lib64/libssh2.so.1 | The path of the software that has the vulnerability. |
| UpdateCmd | String | yum update libssh2 | The command that is used to fix the vulnerability. |
| Version | String | 1.4.3 | The version number. |
| FirstTs | Long | 1580808765000 | The time when the vulnerability was first detected. The value is a UNIX timestamp. Unit: milliseconds. |
| ImageDigest | String | dsadkjahksdhjasdh**** | The digest of the image. |
| LastTs | Long | 1580808765000 | The time when the vulnerability was last detected. The value is a UNIX timestamp. Unit: milliseconds. |
| Layers | List | ["b1f5b9420803ad065 7cf21566e3e20acc085 81e7f22991249ef3aa8 0b8b1c587"] | The image layers. |
| ModifyTs | Long | 1580808765000 | The time when the vulnerability record was updated. The value is a UNIX timestamp. Unit: milliseconds. |
| Name | String | debian:10:CVE-2019- 9893 | The name of the vulnerability. |
| Necessity | String | asap | The priority to fix the vulnerability. Multiple priorities are separated by commas (,). Valid values: asap: high later: medium nntf: low |

| PrimaryId | Long | 2 | The ID. |
|---|---|---|---|
| Related | String | CVE-2019-3862 | The Common Vulnerabilities and Exposures (CVE) ID of the associated vulnerability. |
| RepoName | String | centos | The name of the image repository. |
| RepoNamespace | String | hangzhou-namespace | The namespace of the image. |
| Status | Integer | 0 | The status of the vulnerability. Valid values: 0: unhandled 1: handled 2: being verified 3: added to the whitelist |
| SupportFix | Integer | 1 | This parameter is deprecated. |
| Tag | String | 0.2 | The tag that is added to the image. |
| Type | String | cve | The type of the vulnerability. Valid values: CVE: image system vulnerability SCA: image application vulnerability |
| Uuid | String | B41B3780-337A-472D- B82E-9FD3********* | The UUID of the asset. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeImageVulList &<Common request parameters>
```

Sample success responses `XML` format

```xml
<TotalCount>25</TotalCount> <PageSize>20</PageSize> <RequestId>B41B3780-337A-472D-B82E-9FD3642B9350</RequestId> <VulRecords>
    <Status>0</Status>
    <RepoNamespace>hangzhou-namespace</RepoNamespace>
    <ImageDigest>dsadkjahksdhjasdh****</ImageDigest>
    <RepoName>centos</RepoName>
    <Necessity>asap</Necessity>
    <LastTs>1580808765000</LastTs>
    <Name>debian:10:CVE-2019-9893</Name>
    <FirstTs>1580808765000</FirstTs>
    <Type>cve</Type>
    <ModifyTs>1580808765000</ModifyTs>
    <Related>CVE-2019-3862</Related>
    <Uuid>B41B3780-337A-472D-B82E-9FD3642B9350</Uuid>
    <CanUpdate>false</CanUpdate>
    <AliasName>DSA-2019 libseccomp security vulnerability</AliasName>
    <Tag>0.2</Tag>
    <SupportFix>1</SupportFix>
    <PrimaryId>2</PrimaryId>
    <Layers>["b1f5b9420803ad0657cf21566e3e20acc08581e7f22991249ef3aa80b8b1c587"]</Layers>
    <ExtendContentJson>
        <Os>centos</Os>
        <OsRelease>7</OsRelease>
        <RpmEntityList>
            <Path>/usr/lib64/libssh2.so.1</Path>
            <UpdateCmd>yum update libssh2</UpdateCmd>
            <MatchList>libglib2.0-0 version less than 2.50.3-2+deb9u1</MatchList>
            <Version>1.4.3</Version>
            <FullVersion>1.4.3-12.el7_6.2</FullVersion>
            <Layer>27213ad3447f0209dd152a5cadea****</Layer>
            <MatchDetail>libssh2 version less than 0:1.4.3-12.el7_6.3</MatchDetail>
            <Name>libssh2</Name>
        </RpmEntityList>
    </ExtendContentJson>
</VulRecords> <CurrentPage>1</CurrentPage>
```

`JSON` format `{`

```json
    "TotalCount": 25,
    "PageSize": 20,
    "RequestId": "B41B3780-337A-472D-B82E-9FD3642B9350",
    "VulRecords": {
        "Status": 0,
        "RepoNamespace": "hangzhou-namespace",
        "ImageDigest": "dsadkjahksdhjasdh****",
        "RepoName": "centos",
        "Necessity": "asap",
        "LastTs": 1580808765000,
        "Name": "debian:10:CVE-2019-9893",
        "FirstTs": 1580808765000,
        "Type": "cve",
        "ModifyTs": 1580808765000,
        "Related": "CVE-2019-3862",
        "Uuid": "B41B3780-337A-472D-B82E-9FD3642B9350",
        "CanUpdate": false,
        "AliasName": "DSA-2019 libseccomp security vulnerability",
        "Tag": 0.2,
        "SupportFix": 1,
        "PrimaryId": 2,
        "Layers": "[\"b1f5b9420803ad0657cf21566e3e20acc08581e7f22991249ef3aa80b8b1c587\"]",
        "ExtendContentJson": {
            "Os": "centos",
            "OsRelease": 7,
            "RpmEntityList": {
                "Path": "/usr/lib64/libssh2.so.1",
                "UpdateCmd": "yum update libssh2",
                "MatchList": "libglib2.0-0 version less than 2.50.3-2+deb9u1",
                "Version": "1.4.3",
                "FullVersion": "1.4.3-12.el7_6.2",
                "Layer": "27213ad3447f0209dd152a5cadea****",
                "MatchDetail": "libssh2 version less than 0:1.4.3-12.el7_6.3",
                "Name": "libssh2"
```

`}` `}` `},`

```json
    "CurrentPage": 1
```

`}`

### 5.30 DescribeVulDetails

Queries the details of a vulnerability.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeVulDetails | The operation that you want to perform. Set the value to DescribeVulDetails. |
| Name | String | Yes | debian:10:CVE- 2019-9893 | The name of the vulnerability. |
| Type | String | Yes | cve | The type of the vulnerability. Valid values: CVE: system vulnerability SCA: application vulnerability |

| SourceIp | String | No | 47.100.XX.XX | The source IP address of the request. |
|---|---|---|---|---|
| Lang | String | No | zh | The language of the content within the request and response. Valid values: zh: Chinese en: English |
| AliasName | String | No | DSA-2019 libseccomp security vulnerability | The alias of the vulnerability. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Cves | Array of Cve |   | An array that consists of system vulnerabilities. |
| Classify | String | None | This parameter is deprecated. |
| Classifys | Array of Classify |   | This parameter is deprecated. |
| Classify | String | None | This parameter is deprecated. |
| DemoVideoUrl | String | None | This parameter is deprecated. |
| Description | String | None | This parameter is deprecated. |
| CnvdId | String | CNVD-2017-*** | CNVD ID |
| Complexity | String | None | This parameter is deprecated. |
| Content | String | FasterXML Jackson is a Java-oriented data processing tool provided by FasterXML. The jackson-databind component of FasterXML Jackson is used to bind data. \nA vulnerability was detected in FasterXML jackson-databind 2.x versions earlier than FasterXML jackson- databind 2.9.10.5. Attacker can exploit this vulnerability to execute arbitrary code on the system by sending commands. | The description of the vulnerability. |
| CveId | String | CVE-2018-** | The Common Vulnerabilities and Exposures (CVE) ID of the vulnerability. |
| CvssScore | String | 9.3 | The Common Vulnerability Scoring System (CVSS) score. |

| CvssVector | String | CVSS:3.1/AV:N/AC:H/P R:N/UI:N/S:U/C:H/I:H/A: H | The CVSS vendor. |
|---|---|---|---|
| OtherId | String | CVE-1999-** | The ID of the associated vulnerability. |
| Poc | String | None | This parameter is deprecated. |
| PocCreateTime | Long | 1 | This parameter is deprecated. |
| PocDisclosureTim e | Long | 1 | This parameter is deprecated. |
| Product | String | None | This parameter is deprecated. |
| Reference | String | https://github.com/Fast erXML/jackson- databind/issues/2765 | The reference. |
| ReleaseTime | Long | 1234567890123 | The disclosure time of the vulnerability. The value is a UNIX timestamp. Unit: milliseconds. |
| Solution | String | <p>The vendor has released a patch to fix this vulnerability. Download the patch from:\n<br />https://github.com/F asterXML/jackson- databind/issues/2765< /p>\n | The solution. |
| Summary | String | FasterXML Jackson is a Java-oriented data processing tool provided by FasterXML. The jackson-databind component of FasterXML Jackson is used to bind data. \n\nA vulnerability was detected in FasterXML jackson-databind 2.x versions earlier than FasterXML jackson- databind 2.9.10.5. Attacker can exploit this vulnerability to execute arbitrary code on the system by sending commands. \n | The digest of the vulnerability. |
| Title | String | FasterXML jackson- databind Code vulnerability | The title of the vulnerability. |
| Vendor | String | Alibaba Cloud | The vendor that disclosed the vulnerability. |
| VulLevel | String | serious | The severity of the vulnerability. |
| RequestId | String | B41B3780-337A-472D- B82E-9FD3642B9350 | The ID of the request. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeVulDetails &Name=debian:10:CVE-2019-9893 &Type=cve &<Common request parameters>
```

Sample success responses `XML` format

```xml
<Cves>
    <CvssVector>CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H</CvssVector>
    <CvssScore>9.3</CvssScore>
    <Classify>None</Classify>
    <PocDisclosureTime>1</PocDisclosureTime>
    <Poc>None</Poc>
    <Reference>https://github.com/FasterXML/jackson-databind/issues/2765</Reference>
    <Product>None</Product>
    <Title>FasterXML jackson-databind Code vulnerability</Title>
    <CveId>CVE-2018-**</CveId>
    <Vendor>Alibaba Cloud</Vendor>
    <OtherId>CVE-1999-**</OtherId>
    <CnvdId>CNVD-2017-***</CnvdId>
    <Complexity>None</Complexity>
    <PocCreateTime>1</PocCreateTime>
    <ReleaseTime>1234567890123</ReleaseTime>
    <Content>FasterXML Jackson is a Java-oriented data processing tool provided by FasterXML. The jack
son-databind component of FasterXML Jackson is used to bind data. \nA vulnerability was detected in Fa sterXML jackson-databind 2.x versions earlier than FasterXML jackson-databind 2.9.10.5. Attacker can exploit this vulnerability to execute arbitrary code on the system by sending commands. </Content>
    <Summary>FasterXML Jackson is a Java-oriented data processing tool provided by FasterXML. The jack
son-databind component of FasterXML Jackson is used to bind data. \n\nA vulnerability was detected in FasterXML jackson-databind 2.x versions earlier than FasterXML jackson-databind 2.9.10.5. Attacker ca n exploit this vulnerability to execute arbitrary code on the system by sending commands. \n</Summary>
    <Solution>&lt;p&gt;The vendor has released a patch to fix this vulnerability. Download the patch
from:\n&lt;br /&gt;https://github.com/FasterXML/jackson-databind/issues/2765&lt;/p&gt;\n</Solution>
    <VulLevel>serious</VulLevel>
    <Classifys>
        <DemoVideoUrl>None</DemoVideoUrl>
        <Description>None</Description>
        <Classify>None</Classify>
    </Classifys>
</Cves> <RequestId>B41B3780-337A-472D-B82E-9FD3642B9350</RequestId>
```

`JSON` format `{`

```json
    "Cves": {
        "CvssVector": "CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H",
        "CvssScore": 9.3,
        "Classify": "None",
        "PocDisclosureTime": 1,
        "Poc": "None",
        "Reference": "https://github.com/FasterXML/jackson-databind/issues/2765",
        "Product": "None",
        "Title": "FasterXML jackson-databind Code vulnerability",
        "CveId": "CVE-2018-**",
        "Vendor": "Alibaba Cloud",
        "OtherId": "CVE-1999-**",
        "CnvdId": "CNVD-2017-***",
        "Complexity": "None",
        "PocCreateTime": 1,
        "ReleaseTime": 1234567890123,
        "Content": "FasterXML Jackson is a Java-oriented data processing tool provided by FasterXML. T
he jackson-databind component of FasterXML Jackson is used to bind data. \\nA vulnerability was detect ed in FasterXML jackson-databind 2.x versions earlier than FasterXML jackson-databind 2.9.10.5. Attacker can exploit this vulnerability to execute arbitrary code on the system by sending commands.",
        "Summary": "FasterXML Jackson is a Java-oriented data processing tool provided by FasterXML. T
he jackson-databind component of FasterXML Jackson is used to bind data. \\n\\nA vulnerability was det ected in FasterXML jackson-databind 2.x versions earlier than FasterXML jackson-databind 2.9.10.5. Attacker can exploit this vulnerability to execute arbitrary code on the system by sending commands. \ \n",
        "Solution": "&lt;p&gt;The vendor has released a patch to fix this vulnerability. Download the
patch from:\\n&lt;br /&gt;https://github.com/FasterXML/jackson-databind/issues/2765&lt;/p&gt;\\n",
        "VulLevel": "serious",
        "Classifys": {
            "DemoVideoUrl": "None",
            "Description": "None",
            "Classify": "None"
```

`}` `},`

```json
    "RequestId": "B41B3780-337A-472D-B82E-9FD3642B9350"
```

`}`

### 5.31 DescribeAssetDetailByUuid

Queries the details of an asset by using the UUID of the asset.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeAssetDetail ByUuid | The operation that you want to perform. Set the value to DescribeAssetDetailByUuid. |
| Uuid | String | Yes | 9e6cad93-a379- 46fd-a701- 9bbf02f4**** | The UUID of the asset that you want to query. |
| SourceIp | String | No | 192.0.XX.XX | The source IP address of the request. |

| Lang | String | No | zh | The language of the content within the request and response. Default value: zh. Valid values: zh: Chinese en: English |
|---|---|---|---|---|

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| AssetDetail | Struct |   | The details of the asset. |
| AssetType | String | 6 | The type of the asset. Valid values: 0: Elastic Compute Service (ECS) instance 1: Server Load Balancer (SLB) instance 2: NAT gateway 3: ApsaraDB RDS database 4: ApsaraDB for MongoDB database 5: KVStore for Redis database 6: image 7: container |
| AuthModifyTime | Long | 1627974044000 | The timestamp when Container Protection was authorized to scan the asset. Unit: milliseconds. |
| AuthVersion | Integer | 1 | The edition of Container Protection that is authorized to scan the asset. Valid values: 1: Basic edition (Unauthorized) 6: Anti-virus edition 5: Advanced edition 3: Enterprise edition 7: Ultimate edition 10: Value-added Plan edition |
| Bind | Boolean | true | Indicates whether Container Protection is authorized to scan the asset. Valid values: true: yes false: no |
| ClientStatus | String | online | The status of the agent. Valid values: pause: The agent suspends protection for your asset. online: The agent is protecting your asset. offline: The agent does not protect your asset. |
| Cpu | Integer | 4 | The number of CPU cores. |
| CpuInfo | String | Intel(R) Xeon(R) Platinum 8163 CPU @ 2.50GHz | The details of the CPU. |
| CreateTime | Long | 1603863599000 | The timestamp when Container Protection records the details of the asset. Unit: milliseconds. |

| DiskInfoList | List | [ { "diskName": "/dev/vda1", "totalSize": 20, "useSize": 2 } ] | The information about the disk. This parameter contains the following fields: diskName: the name of the disk. totalSize: the total amount of the disk space. Unit: GB. useSize: the amount of the used disk space. Unit: GB. |
|---|---|---|---|
| GroupTrace | String | Ungrouped | The group to which the asset belongs. By default, the assets that are not grouped belong to the Ungrouped group. |
| HostName | String | qewrqwerqs**** | The hostname of the asset. |
| InstanceId | String | i- uf6h7p2fgk6rkk0g**** | The instance ID of the asset. |
| InstanceName | String | i-fasdfasdfadfafa**** | The instance name of the asset. |
| InternetIp | String | 10.18.XX.XX | The public IP address of the server. |
| IntranetIp | String | 192.168.XX.XX | The private IP address of the server. |
| Ip | String | 192.168.XX.XX | The IP address of the asset. |
| IpList | List | ["192.168.XX.XX","192. 168.XX.XX"] | The list of IP addresses. |
| Kernel | String | 4.18.0- 80.11.2.el8 0.x86 64 _ _ | The kernel version of the operating system. |
| MacList | List | ["00:16:3*:1*:9*:cf"] | The MAC address. |
| Mem | Integer | 32 | The memory size of the server. Unit: GB. |
| Os | String | linux | The type of the operating system. |
| OsDetail | String | Linux 64bit | The version of the operating system. |
| OsName | String | CentOS 8.0 64-bit | The name of the operating system. |
| Region | String | cn-hangzhou-dg-a01 | The region. |
| RegionId | String | cn-hanghzou | The region ID. |
| RegionName | String | China (Hangzhou) | The region name. |
| SysInfo | String | CentOS Linux 8.0.1905 | The details of the operating system. |
| Tag | String | InternetIp | The tag that is added to the asset. |

| Uuid | String | 9e6cad93-a379-46fd- a701-9bbf02f4**** | The UUID of the asset. |
|---|---|---|---|
| VpcInstanceId | String | vpc- bp1fs3bwonlfq503w*** * | The ID of the virtual private cloud (VPC) to which the asset belongs. |
| RequestId | String | 39031E31-6BBA-5C99- A870-D807E78918CD | The ID of the request, which is used to locate and troubleshoot issues. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeAssetDetailByUuid &Uuid=9e6cad93-a379-46fd-a701-9bbf02f4**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RequestId>39031E31-6BBA-5C99-A870-D807E78918CD </RequestId> <AssetDetail>
    <GroupTrace>Ungrouped</GroupTrace>
    <Bind>true</Bind>
    <Os>linux</Os>
    <Ip>192.168.XX.XX </Ip>
    <Cpu>4</Cpu>
    <OsDetail>Linux 64bit </OsDetail>
    <IntranetIp>192.168.XX.XX </IntranetIp>
    <AuthModifyTime>1627974044000</AuthModifyTime>
    <InternetIp>10.18.XX.XX </InternetIp>
    <RegionName>China (Hangzhou)</RegionName>
    <Kernel>4.18.0-80.11.2.el8_0.x86_64 </Kernel>
    <HostName>qewrqwerqs**** </HostName>
    <ClientStatus>online</ClientStatus>
    <CpuInfo>Intel(R) Xeon(R) Platinum 8163 CPU @ 2.50GHz </CpuInfo>
    <InstanceId>i-uf6h7p2fgk6rkk0g**** </InstanceId>
    <CreateTime>1603863599000</CreateTime>
    <OsName>CentOS 8.0 64-bit</OsName>
    <SysInfo>CentOS Linux 8.0.1905 </SysInfo>
    <InstanceName>i-fasdfasdfadfafa**** </InstanceName>
    <AssetType>6</AssetType>
    <Uuid>9e6cad93-a379-46fd-a701-9bbf02f4**** </Uuid>
    <Mem>32</Mem>
    <Region>cn-hangzhou-dg-a01 </Region>
    <VpcInstanceId>vpc-bp1fs3bwonlfq503w**** </VpcInstanceId>
    <Tag>InternetIp </Tag>
    <RegionId>cn-hanghzou </RegionId>
    <AuthVersion>1</AuthVersion>
    <IpList>["192.168.XX.XX","192.168.XX.XX"] </IpList>
    <MacList>["00:16:3*:1*:9*:cf"] </MacList>
    <DiskInfoList>[ { "diskName": "/dev/vda1", "totalSize": 20, "useSize": 2 } ]</DiskInfoList>
</AssetDetail>
```

`JSON` format `{`

```json
    "RequestId": "39031E31-6BBA-5C99-A870-D807E78918CD",
    "AssetDetail": {
        "GroupTrace": "Ungrouped",
        "Bind": true,
        "Os": "linux",
        "Ip": "192.168.XX.XX",
        "Cpu": 4,
        "OsDetail": "Linux 64bit",
        "IntranetIp": "192.168.XX.XX",
        "AuthModifyTime": 1627974044000,
        "InternetIp": "10.18.XX.XX",
        "RegionName": "China (Hangzhou)",
        "Kernel": "4.18.0-80.11.2.el8_0.x86_64",
        "HostName": "qewrqwerqs****",
        "ClientStatus": "online",
        "CpuInfo": "Intel(R) Xeon(R) Platinum 8163 CPU @ 2.50GHz",
        "InstanceId": "i-uf6h7p2fgk6rkk0g****",
        "CreateTime": 1603863599000,
        "OsName": "CentOS 8.0 64-bit",
        "SysInfo": "CentOS Linux 8.0.1905",
        "InstanceName": "i-fasdfasdfadfafa****",
        "AssetType": 6,
        "Uuid": "9e6cad93-a379-46fd-a701-9bbf02f4****",
        "Mem": 32,
        "Region": "cn-hangzhou-dg-a01",
        "VpcInstanceId": "vpc-bp1fs3bwonlfq503w****",
        "Tag": "InternetIp",
        "RegionId": "cn-hanghzou",
        "AuthVersion": 1,
        "IpList": "[\"192.168.XX.XX\",\"192.168.XX.XX\"]",
        "MacList": "[\"00:16:3*:1*:9*:cf\"]",
        "DiskInfoList": "[ { \"diskName\": \"/dev/vda1\", \"totalSize\": 20, \"useSize\": 2 } ]"
```

`}` `}`

### 5.32 DescribeAllEntity

Queries information about all entities and supports multiple filter conditions for different scenarios.

**Request header**

This operation uses common request headers. No special request headers are required. For more information, see Common request parameters.

**Request parameters**

| Paramete r | Type | Positio n | Required | Example | Description |
|---|---|---|---|---|---|
| GroupId | Long | Query | No | 1 | Deprecated. |
| Os | String | Query | No | linux | The operating system. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| EntityList | Array | [ "003d544744249351** **" ] | The list of entities. |
| -GroupId | Integer | 12345 | The ID of the node group. |
| -InstanceName | String | test | The name of the node instance. |
| -Ip | String | 127.0.0.1 | The public IP address of the asset that is associated with the vulnerability. |
| -Uuid | String | 49e25e0f-bb51-4a5a- a1b3-13a4ddaa**** | The universally unique identifier (UUID) of the asset. |
| -Os | String | linux | The type of the operating system. |
| -InternetIp | String | 8.210.XX.XX | The public IP address of the server. |
| -IntranetIp | String | 192.168.XX.XX | The private IP address of the node. |
| RequestId | String | F0A8***-930D-5EC1- 97C8-************ | The request ID. |

**Examples**

Request example

```
http(s)://[Endpoint]/?Action=DescribeAllEntity &<Common request parameters>
```

Response example `JSON` format

```
HTTP/1.1 200 OK Content-Type:application/json
```

`{`

```json
 "RequestId":"F0A8***-930D-5EC1-97C8-************",
 "EntityList":[
```

`{`

```json
   "InstanceName":"test",
   "Uuid":"49e25e0f-bb51-4a5a-a1b3-13a4ddaa****",
   "Os":"linux",
   "InternetIp":"8.210.XX.XX",
   "Ip":"127.0.0.1",
   "IntranetIp":"192.168.XX.XX",
   "GroupId":12345
```

`}` `]` `}`

### 5.33 DescribeClusterVulStatistics

Queries vulnerability statistics.

**Authorization information**

| Operation | Access level | Resource type |
|---|---|---|
| yundun- css:DescribeClusterVulStatistics | Read | acs:yundun-css:*:{#accountId}:* |

**Traffic shaping**

The throttling limit for a single user is 10 queries per second (QPS). The throttling limit for this operation is 100 QPS.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

**Request parameters**

| Paramete r | Type | Positio n | Required | Example | Description |
|---|---|---|---|---|---|
| SourceIp | String | Query | No | 219.133.XX.XX | The source IP address. |
| ClusterId | String | Query | No | c690a0789419f4284a4e0a29 e12fe**** | The ID of the cluster. |
| Types | String | Query | No | cve,app,sca | The types of vulnerabilities to query. Valid values: cve: Linux software vulnerabilities app: application vulnerabilities sca: software composition analysis (SCA) vulnerabilities |
| From | String | Query | No | css | The identifier of the request source. Valid values: sas: Server Guard css: Container Security |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D-5EC1- 97C8-************ | The request ID is a unique identifier generated by Alibaba Cloud. You can use this ID to troubleshoot and locate problems. |
| RequestId | String | F0A8A039-930D-5EC1- 97C8-************ | The request ID is a unique identifier generated by Alibaba Cloud and can be used to troubleshoot issues. |
| VulStat | Struct | { "LaterCount":"2", "AsapCount":"1", "NntfCount":"3" } | The vulnerability statistics. |
| -AsapCount | String | 1 | The number of high-risk vulnerabilities. |
| -LaterCount | String | 2 | The number of medium-risk vulnerabilities. |

| Alibaba Cloud Sec ard Advanced Edit | urity-Server Gu ion |   | Container Security Service Deve oper Guide·API reference |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| -NntfCount | String | 3 | The number of low-risk vulnerabilities. |

**Examples**

Sample request

```
https://[Endpoint]/?Action=DescribeClusterVulStatistics&RegionId=cnhangzhou&SourceIp=219.133.XX.XX&ClusterId=c690a0789419f4284a4e0a29e12fe****&Types=cve,app,sca&From=css
```

Sample response `JSON` format

```
HTTP/1.1 200 OK Content-Type:application/json
```

`{`

```json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "VulStat":{
        "LaterCount":"2",
        "AsapCount":"1",
        "NntfCount":"3"
```

`}` `}` `XML` format

```xml
HTTP/1.1 200 OK Content-Type: application/xml <DescribeClusterVulStatisticsResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <VulStat>
        <AsapCount>1</AsapCount>
        <LaterCount>2</LaterCount>
        <NntfCount>3</NntfCount>
    </VulStat>
</DescribeClusterVulStatisticsResponse>
```

**5.34.**

### DescribeContainerInstancesWithoutAscm

Queries a list of containers without filtering the results by multi-level organization information.

**Authorization**

| Operation | Access level | Resource type |
|---|---|---|
| yundun- css:DescribeContainerInstancesWitho utAscm | Read | acs:yundun-css:*:{#accountId}:* |

**Throttling**

Call frequency per user: 10 queries per second (QPS). Overall API call frequency: 100 QPS.

**Request headers**

This operation uses only common request headers. For more information, see the documentation about common request parameters.

**Request parameters**

| Paramete r | Type | Positio n | Required | Example | Description |
|---|---|---|---|---|---|
| Criteria | String | Query | No | [{"name":"flag","value":"0\|8" ,"logicalExp":"AND"}, {"name":"ecsType","value":" !8","logicalExp":"AND"}] [{"name":"clusterType","valu e":"NotManagedKubernetes", "logicalExp":"AND"}] | The conditions to search for assets. This parameter is a case-sensitive JSON string. It contains the following fields: name : The search item. value : The value of the search item. logicalExp : The logical relationship between multiple search items. Valid values: OR: The search items are combined with a logical OR. AND: The search items are combined with a logical AND. |
| LogicalExp | String | Query | No | OR | The logical relationship that applies to multiple search conditions. Valid values: OR: The conditions are combined with a logical OR. AND: The conditions are combined with a logical AND. |
| PageSize | Integer | Query | No | 20 | The maximum number of entries to return on each page. |
| CurrentPage | Integer | Query | No | 1 | The page number of the current page. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
|   |   | [ { "ImageRepoTag": "0.3.1.0-dfa2010- aliyun", "AppName": "alibaba-log- controller", "PodIp": "172.24.XX.XX", "VulCount": 15, "HcStatus": "YES", "ImageId": "registry- vpc.cn- beijing.aliyuncs.com/ac s/log- controller@sha256:5b0 46e2de8c4908191251 93ee2eb71a66f2cc16c 032dcd8b69ead4be10 24****", "ClusterId": "cfb41a869c71e4678a 97021582dd8a****", "I R N " |   |

| Parameter | Type | "ImageRepoName": "Eloxga-mcopntlreoller", | Description |
|---|---|---|---|
|   |   | "HostIp": |   |
| ContainerInstanc eList | Array | "172.24.XX.XX", "Pod": "alibaba-log-controller- 6f847f8786-mk2mg", "RiskStatus": "YES", "VulStatus": "YES", "AlarmStatus": "YES", "Image": "docker.io/library/nginx :latest", "ImageRepoNamespac e": "acs", "ImageDigest": "5b046e2de8c490819 125193ee2eb71a66f2c c16c032dcd8b69ead4 be1024****", "Namespace": "kube- system", "InstanceId": "i- 2zegzjyotydfkz9****", "NodeInfo": "test", "ImageUuid": "5f23dfbceec289a49ac 94e035e2****", "RegionId": "cn- hangzhou", "UpdateMark": "79cff74d-e967-5407- 8a78-ee03b9****", "ContainerId": "48a6d9a92435a13ad 573372c3f3c63b7e04d 106458141df9f921557 09d****", "NodeName": "test", "HcCount": 1, "ClusterName": "test", "RiskCount": 1, "AlarmCount": 1, "CreateTimestamp": 1670368337000, "Exposed": 1, "ExposedDetail": " [{\\\"exposedName\\\": \\\"nginx-ingress- lb\\\",\\\"exposedType\\ \":\\\"LoadBalancer\\\",\ \\"portDOList\\\": [{\\\"name\\\":\\\"http\\\ ",\\\"nodePort\\\":32268 ,\\\"port\\\":80,\\\"target Port\\\":80}, {\\\"name\\\":\\\"https\\ \",\\\"nodePort\\\":3237 6,\\\"port\\\":443,\\\"tar getPort\\\":443}]}] " } ] | The list of containers. |
| -ContainerId | String | B41B3780-337A-472D- B82E-9FD3******** | The container ID. |
| -Image | String | registry.acs.intra.***.** *.com/acs/log- ***:0.2.7.0-68ada84- aliyun | The image. |
| -ImageId | String | asdaSdasd******** | The image ID. |
| -Pod | String | csi-provisioner- 564c7989c4-9**** | The pod. |

|   | Container Security oper Guide·API ref | Service Devel erence |   | Alibaba Cloud Security-Server G ard Advanced Edition | u |
|---|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| -Namespace | String | shanghai-namespace | The namespace of the image repository. |
| -AppName | String | csi-provisioner | The application name. |
| -NodeName | String | cn-wulan-env116- d01.i- km100o6qw4bhyqo7p bvb | The node name. |
| -PodIp | String | 172.29.0.130 | The IP address of the pod. |
| -HostIp | String | 47.100.XX.XX | The IP address of the host. |
| -ClusterId | String | Cccfd68c474454665ac e07efce924**** | The ID of the container cluster. |
| -InstanceId | String | i- km100o6qy8g********* | The instance ID. |
| -NodeInfo | String | None | This parameter is deprecated. |
| -ImageUuid | String | e05c0de79821763786 8ef4**** | The UUID of the image. |
| -UpdateMark | String | None | This parameter is deprecated. |
| - ImageRepoName space | String | shanghai-namespace | The namespace of the image repository. |
| -ImageRepoName | String | centos1 | The image repository. |
| -ImageRepoTag | String | 0.2.7.0-68ada84-aliyun | The tag of the image repository. |
| -ImageDigest | String | 6a5e103187b31a9459 2a47a5858617f7a179e ad61df7606**** | The image digest. |
| -ClusterName | String | test**** | The name of the container cluster. |
| -HcStatus | String | NO | Indicates whether baseline security risks exist. Valid values: YES: Baseline security risks exist. NO: No baseline security risks exist. |
| -VulStatus | String | NO | Indicates whether vulnerabilities exist. Valid values: YES: Vulnerabilities exist. NO: No vulnerabilities exist. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| -AlarmStatus | String | NO | Indicates whether security alerts exist. Valid values: YES: Security alerts exist. NO: No security alerts exist. |
| -RiskStatus | String | YES | Indicates whether risks exist. Valid values: YES: Risks exist. NO: No risks exist. |
| -RiskCount | String | 1 | The number of risks. |
| - CreateTimestamp | Long | 1639236844747 | The time when the container was created. This is a UNIX timestamp. Unit: milliseconds. |
| -RegionId | String | cn-***-env116-d01 | The region ID. |
| -HcCount | Integer | 1 | The number of baseline check risks. |
| -VulCount | Integer | 0 | The number of vulnerability risks. |
| -AlarmCount | Integer | 1 | The number of security alerts. |
| -OrgId | String | 12 | The organization ID. |
| -ResourceSetId | String | 12 | The resource set ID. |
| RequestId | String | F0A8A039-930D-5EC1- 97C8-************ | The unique ID of the request. It is used to locate and troubleshoot issues. |
| PageInfo | Struct | { "total": 100, "currentPage": 1, "pageSize": 10 } | The paging information. |
| -Count | Integer | 20 | Total pages |
| -PageSize | Integer | 20 | The maximum number of entries returned on each page. |
| -TotalCount | Integer | 50 | The total number of entries. |
| -CurrentPage | Integer | 1 | The page number of the current page. |

**Examples**

Request example

```
https://[Endpoint]/?Action=DescribeContainerInstancesWithoutAscm&RegionId=cn-hangzhou&Criteria=[{"name ":"flag","value":"0|8","logicalExp":"AND"},{"name":"ecsType","value":"!8","logicalExp":"AND"}][{"name" :"clusterType","value":"NotManagedKubernetes","logicalExp":"AND"}]&LogicalExp=OR&PageSize=20&CurrentPage
```

Response example `JSON` format

```
HTTP/1.1 200 OK Content-Type:application/json
```

`{`

```json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "PageInfo":{
        "TotalCount":50,
        "PageSize":20,
        "CurrentPage":1,
        "Count":20
```

`},`

```json
    "ContainerInstanceList":[
```

`{`

```json
            "NodeName":"cn-wulan-env116-d01.i-km100o6qw4bhyqo7pbvb",
            "ImageDigest":"6a5e103187b31a94592a47a5858617f7a179ead61df7606****",
            "VulStatus":"NO",
            "ImageRepoNamespace":"shanghai-namespace",
            "Image":"registry.acs.intra.***.***.com/acs/log-***:0.2.7.0-68ada84-aliyun",
            "ImageUuid":"e05c0de798217637868ef4****",
            "RiskCount":"1",
            "AppName":"csi-provisioner",
            "ContainerId":"B41B3780-337A-472D-B82E-9FD3********",
            "ImageId":"asdaSdasd********",
            "ClusterName":"test****",
            "ResourceSetId":"12",
            "CreateTimestamp":1639236844747,
            "AlarmCount":1,
            "HostIp":"47.100.XX.XX",
            "HcCount":1,
            "Pod":"csi-provisioner-564c7989c4-9****",
            "ClusterId":"Cccfd68c474454665ace07efce924****",
            "InstanceId":"i-km100o6qy8g*********",
            "RiskStatus":"YES",
            "Namespace":"shanghai-namespace",
            "VulCount":0,
            "ImageRepoName":"centos1",
            "OrgId":"12",
            "NodeInfo":"None",
            "PodIp":"172.29.0.130",
            "AlarmStatus":"NO",
            "RegionId":"cn-***-env116-d01",
            "ImageRepoTag":"0.2.7.0-68ada84-aliyun",
            "UpdateMark":"None",
            "HcStatus":"NO"
```

`}` `]` `}` `XML` format

```xml
HTTP/1.1 200 OK Content-Type:application/xml <DescribeContainerInstancesWithoutAscmResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <PageInfo>
        <Count>20</Count>
        <PageSize>20</PageSize>
        <TotalCount>50</TotalCount>
        <CurrentPage>1</CurrentPage>
    </PageInfo>
    <ContainerInstanceList>
        <ContainerId>B41B3780-337A-472D-B82E-9FD3********</ContainerId>
        <Image>registry.acs.intra.***.***.com/acs/log-***:0.2.7.0-68ada84-aliyun</Image>
        <ImageId>asdaSdasd********</ImageId>
        <Pod>csi-provisioner-564c7989c4-9****</Pod>
        <Namespace>shanghai-namespace</Namespace>
        <AppName>csi-provisioner</AppName>
        <NodeName>cn-wulan-env116-d01.i-km100o6qw4bhyqo7pbvb</NodeName>
        <PodIp>172.29.0.130</PodIp>
        <HostIp>47.100.XX.XX</HostIp>
        <ClusterId>Cccfd68c474454665ace07efce924****</ClusterId>
        <InstanceId>i-km100o6qy8g*********</InstanceId>
        <NodeInfo>None</NodeInfo>
        <ImageUuid>e05c0de798217637868ef4****</ImageUuid>
        <UpdateMark>None</UpdateMark>
        <ImageRepoNamespace>shanghai-namespace</ImageRepoNamespace>
        <ImageRepoName>centos1</ImageRepoName>
        <ImageRepoTag>0.2.7.0-68ada84-aliyun</ImageRepoTag>
        <ImageDigest>6a5e103187b31a94592a47a5858617f7a179ead61df7606****</ImageDigest>
        <ClusterName>test****</ClusterName>
        <HcStatus>NO</HcStatus>
        <VulStatus>NO</VulStatus>
        <AlarmStatus>NO</AlarmStatus>
        <RiskStatus>YES</RiskStatus>
        <RiskCount>1</RiskCount>
        <CreateTimestamp>1639236844747</CreateTimestamp>
        <RegionId>cn-***-env116-d01</RegionId>
        <HcCount>1</HcCount>
        <VulCount>0</VulCount>
        <AlarmCount>1</AlarmCount>
        <OrgId>12</OrgId>
        <ResourceSetId>12</ResourceSetId>
    </ContainerInstanceList>
</DescribeContainerInstancesWithoutAscmResponse>
```

### 5.35 DescribeExportInfo

Queries the details of an export task.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

**Request parameters**

| Paramete r | Type | Positio n | Required | Example | Description |
|---|---|---|---|---|---|
| ExportId | Long | Query | No | 14356 | The ID of the vulnerability export task. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8***-930D-5EC1- 97C8-************ | The request ID. |
| Id | Long | 1 | ID |
| FileName | String | example.mp4 | The name of the file. |
| CurrentCount | Integer | 1 | The number of data entries that have been exported. |
| TotalCount | Integer | 32 | The total number of data entries found. |
| Progress | Integer | 100 | The export progress in percentage (%). |
| ExportStatus | String | success | The status of the task. |
| Message | String | success | The response message. |
| Link | String | http://xxxxx | The download link for the file. |

**Examples**

Sample request

```
http(s)://[Endpoint]/?Action=DescribeExportInfo &Common request parameters
```

Sample response Sample response in `JSON` format

```
HTTP/1.1 200 OK Content-Type:application/json
```

`{`

```json
 "TotalCount":32,
 "Progress":100,
 "RequestId":"F0A8***-930D-5EC1-97C8-************",
 "Message":"success",
 "FileName":"example.mp4",
 "ExportStatus":"success",
 "CurrentCount":1,
 "Id":1,
 "Link":"http://xxxxx"
```

`}`

### 5.36 DescribePropertyCount

Counts the properties of assets in Security Center to provide a comprehensive overview of your assets.

**Request headers**

This operation has no special request headers. For more information about common request headers, see Common request parameters.

**Request parameters**

| Paramete r | Type | Positio n | Required | Example | Description |
|---|---|---|---|---|---|
| Type | String | Query | No | containerNetwork | The type of active protection to query. Valid values: auto breaking : Anti- _ virus ransomware breaking _ : Anti-ransomware (bait capture) webshell cloud breakin _ _ g : Web shell connection protection (not yet available) alinet : Malicious network behavior protection k8s log analysis : _ _ Container K8s threat detection (not yet available) alisecguard : Client self- protection. |
| UuidList | String | Query | No | a9a95aad-2b60-4812-b22d- ***********,a9a95aad-2b60- 4812-b22d-*********** | A list of server UUIDs. Note: If you set UuidList, Server Guard deletes the tag only from the servers specified in the list. If UuidList is empty, Server Guard deletes the tag from all servers. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8***-930D-5EC1- 97C8-************ | The request ID. |
| Port | Integer | 3306 | The destination port number. |
| Process | Integer | 0 | The progress. |
| Software | Integer | 111 | The number of software. |
| User | Integer | root | The username. |
| Cron | Integer | 123 | The cron job for timed scheduling. |
| Sca | Integer | 112 | The number of middleware. |
| Autorun | Integer | 3 | The number of startup items. |

**Examples**

Sample request

```
http(s)://[Endpoint]/?Action=DescribePropertyCount &Common request parameters
```

Sample success response `JSON` format

```
HTTP/1.1 200 OK Content-Type:application/json
```

`{`

```json
 "Sca":112,
 "User":"",
 "RequestId":"F0A8***-930D-5EC1-97C8-************",
 "Port":3306,
 "Process":0,
 "Software":111,
 "Cron":123,
 "Autorun":3
```

`}`

### 5.37 DescribePropertyCronDetail

The DescribePropertyCronDetail operation queries the details of scheduled tasks on your host assets.

**Authorization information**

| Operation | Access level | Resource type |
|---|---|---|
| yundun- css:DescribePropertyCronDetail | Read | acs:yundun-css:*:{#accountId}:* |

**Traffic shaping**

The rate limit for a single user is 10 queries per second (QPS). The rate limit for this operation is 100 QPS.

**Request header**

This operation uses common request headers and has no special request headers. For more information, see Common request parameters.

**Request parameters**

| Paramete r | Type | Positio n | Required | Example | Description |
|---|---|---|---|---|---|
| Remark | String | Query | No | 192.168.XX.XX | The name or IP address of the server to query. |
| Source | String | Query | No | /etc/cron.d/root | The path of the task to query. |
| User | String | Query | No | root | The account name for the scheduled task to query. |
| Uuid | String | Query | No | 50d213b4-3a35-427a-b8a5- 04b0c7e1**** | The UUID of the server to query. |

| Paramete r | Type | Positio n | Required | Example | Description |
|---|---|---|---|---|---|
| CurrentPage | Integer | Query | No | 1 | The page number to return. Default value: 1. |
| PageSize | Integer | Query | No | 10 | The number of entries to return on each page. Default value: 10. |
| SelectType | String | Query | No | equals | The query type. Default value: like . Valid values: equals : term query. such as : fuzzy query. |
| AssetType | String | Query | No | IMAGE | The type of the asset fingerprint. Default value: HOST . Valid values: Image : image asset fingerprint Host : host asset fingerprint |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Propertys | Array | [ { "User":"root", "InstanceId":"i- hp35tftuh52wbp1g**** ", "ResourceSetName":"t est", "Ip":"192.168.XX.XX", "Period":"*/10 * * * *", "OrgName":"test", "IntranetIp":"100.104.X X.XX", "Source":"/etc/cron.d/r oot", "InstanceName":"hc- host-****", "OrgId":"12", "Uuid":"162eb349- c2d9-4f8b-805c- 75b43d4c****", "InternetIp":"192.168.X X.XX", "Create":"1704248312 000", "Cmd":"/usr/lib64/sa/sa 1 1 1", "ResourceSetId":"12", "CreateTimestamp":16 49149566000, "Md5":"4cc8f97c2bf9c babb2c2be2erqw****" } ] | A list of the asset fingerprints for the scheduled tasks. |
| -InstanceName | String | hc-host-**** | The name of the server instance. |
| -Ip | String | 192.168.XX.XX | The IP addresses of the server. |

| Container Security | Service Devel |   | Alibaba Cloud Security-Server G |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| -Create | String | 1704248312000 | The time of the latest scan. |
| - CreateTimestamp | Long | 1649149566000 | The timestamp of the latest scan for the asset fingerprint, in milliseconds. |
| -Uuid | String | 162eb349-c2d9-4f8b- 805c-75b43d4c**** | The UUID of the server. |
| -InstanceId | String | i- hp35tftuh52wbp1g**** | The instance ID of the server. |
| -IntranetIp | String | 100.104.XX.XX | The private IP address of the server. |
| -InternetIp | String | 192.168.XX.XX | The public IP address of the server. |
| -Period | String | */10 * * * * | The execution period of the scheduled task. |
| -Source | String | /etc/cron.d/root | The path of the scheduled task. |
| -Cmd | String | /usr/lib64/sa/sa1 1 1 | The command executed by the scheduled task. |
| -User | String | root | The account name used to execute the scheduled task. |
| -Md5 | String | 4cc8f97c2bf9cbabb2c2 be2erqw**** | The MD5 hash of the scheduled task path. |
| -OrgId | String | 12 | The organization ID. |
| -ResourceSetId | String | 12 | The resource set ID. |
| -OrgName | String | test | The organization name. |
| - ResourceSetNam e | String | test | The resource set name. |
| RequestId | String | F0A8A039-930D-5EC1- 97C8-************ | The ID of the request. This ID is a unique identifier generated by Alibaba Cloud. You can use this ID to troubleshoot issues. |
| PageInfo | Struct | { "TotalCount":1, "PageSize":10, "CurrentPage":1, "Count":1 } | The query results page shows the following information. |
| -Count | Integer | 1 | The number of entries returned on the current page. |
| -PageSize | Integer | 10 | Specifies the number of fingerprints for Scheduled Task Assets to display on each page of a paged query. The default is 10. |

| Alibaba Cloud Sec ard Advanced Edit | urity-Server Gu ion |   | Container Security Service Deve oper Guide·API reference |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| -TotalCount | Integer | 1 | The total number of fingerprints for the assets in the queried scheduled task. |
| -CurrentPage | Integer | 1 | The page number of the returned page. |

**Examples**

Request example

```
https://[Endpoint]/?Action=DescribePropertyCronDetail&RegionId=cnhangzhou&Remark=192.168.XX.XX&Source=/etc/cron.d/root&User=root&Uuid=50d213b4-3a35-427a-b8a5-04b0c7e1*
***&CurrentPage=1&PageSize=10&SelectType=equals&AssetType=IMAGE
```

Response examples `JSON` format

```
HTTP/1.1 200 OK Content-Type:application/json
```

`{`

```json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "Propertys":[
```

`{`

```json
            "User":"root",
            "InstanceId":"i-hp35tftuh52wbp1g****",
            "ResourceSetName":"test",
            "Ip":"192.168.XX.XX",
            "Period":"*/10 * * * *",
            "OrgName":"test",
            "IntranetIp":"100.104.XX.XX",
            "Source":"/etc/cron.d/root",
            "InstanceName":"hc-host-****",
            "OrgId":"12",
            "Uuid":"162eb349-c2d9-4f8b-805c-75b43d4c****",
            "InternetIp":"192.168.XX.XX",
            "Create":"1704248312000",
            "Cmd":"/usr/lib64/sa/sa1 1 1",
            "ResourceSetId":"12",
            "CreateTimestamp":1649149566000,
            "Md5":"4cc8f97c2bf9cbabb2c2be2erqw****"
```

`}` `],`

```json
    "PageInfo":{
        "TotalCount":1,
        "PageSize":10,
        "CurrentPage":1,
        "Count":1
```

`}` `}` `XML` format

```xml
HTTP/1.1 200 OK Content-Type:application/xml <DescribePropertyCronDetailResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <Propertys>
        <InstanceName>hc-host-****</InstanceName>
        <Ip>192.168.XX.XX</Ip>
        <Create>1704248312000</Create>
        <CreateTimestamp>1649149566000</CreateTimestamp>
        <Uuid>162eb349-c2d9-4f8b-805c-75b43d4c****</Uuid>
        <InstanceId>i-hp35tftuh52wbp1g****</InstanceId>
        <IntranetIp>100.104.XX.XX</IntranetIp>
        <InternetIp>192.168.XX.XX</InternetIp>
        <Period>*/10 * * * *</Period>
        <Source>/etc/cron.d/root</Source>
        <Cmd>/usr/lib64/sa/sa1 1 1</Cmd>
        <User>root</User>
        <Md5>4cc8f97c2bf9cbabb2c2be2erqw****</Md5>
        <OrgId>12</OrgId>
        <ResourceSetId>12</ResourceSetId>
        <OrgName>test</OrgName>
        <ResourceSetName>test</ResourceSetName>
    </Propertys>
    <PageInfo>
        <Count>1</Count>
        <PageSize>10</PageSize>
        <TotalCount>1</TotalCount>
        <CurrentPage>1</CurrentPage>
    </PageInfo>
</DescribePropertyCronDetailResponse>
```

### 5.38 DescribePropertySoftwareDetail

Queries the details of software assets.

**Authorization**

| Operation | Access level | Resource type |
|---|---|---|
| yundun- css:DescribePropertySoftwareDetail | Read | acs:yundun-css:*:{#accountId}:* |

**Throttling**

For a single user: 10 queries per second (QPS). For this operation: 100 QPS.

**Request headers**

This operation uses only common request headers. For more information, see the documentation on common parameters.

**Request parameters**

| Paramete r | Type | Positio n | Required | Example | Description |
|---|---|---|---|---|---|
| Remark | String | Query | No | 47.100.XX.XX | The name or IP address of the server. |

| Alibaba Cloud | Security- | Server Gu |   | Conta | iner Security Service Deve |
|---|---|---|---|---|---|

| Paramete r | Type | Positio n | Required | Example | Description |
|---|---|---|---|---|---|
| Name | String | Query | No | sshd | The name of the software. |
| Path | String | Query | No | /usr/xxx | The installation path of the software. |
| SoftwareVer sion | String | Query | No | 1.1.x.x | The version of the software. |
| Extend | String | Query | No | 1 | Specifies whether to use fuzzy search for the Name parameter. 1 : Yes 0 : No |
| Uuid | String | Query | No | inet-f6ac9a93-xxx | The UUID of the server. |
| CurrentPage | Integer | Query | No | 1 | The number of the page to return. |
| PageSize | Integer | Query | No | 20 | The number of entries to return on each page. |
| SelectType | String | Query | No | equals | The query type. Default value: like . Valid values: equals : term query. like : fuzzy query. |
| Ip | String | Query | No | 47.100.XX.XX | The IP address of the server. |
| GroupId | String | Query | No | 1 | The ID of the group. |
| AssetType | String | Query | No | IMAGE | The type of the Asset Fingerprint. Default value: HOST . Valid values: IMAGE : Image Asset Fingerprint HOST : Host Asset Fingerprint. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| Propertys | Array | [ { "Path":"/boot/.vmlinuz- 3.10.0- 514.el7.x86 64.hmac", _ "InstallTimeStamp":14 98375028000, "InstallTime":"2017-06- 25 15:17:08", "InstanceId":"i- 5fq05ua8z5cd1spus1t w", "ResourceSetName":"t est", "Ip":"192.168.176.124" , "OrgName":"test", "IntranetIp":"192.168.1 76.124", "Name":"kernel", "InstanceName":"test1 ", "OrgId":"12", "Uuid":"9d327322- 895b-4ba4-9801- 24411187b1e2", "InternetIp":"43.186.xx .xx", "Version":"3.10.0", "Create":17042483130 00, "ResourceSetId":"12", "CreateTimestamp":17 04248313000 } ] | The details of the software on the server. |
| -Name | String | kernel | The name of the software. |
| -Path | String | /boot/.vmlinuz-3.10.0- 514.el7.x86 64.hmac _ | The path of the software. |
| -InstanceName | String | test1 | The name of the instance. |
| -Ip | String | 192.168.176.124 | The IP address of the server. |
| -Create | Long | 1704248313000 | The timestamp of the last scan. |
| - CreateTimestamp | Long | 1704248313000 | The timestamp of the last scan. |
| -InstallTime | String | 2017-06-25 15:17:08 | The installation time of the software. |
| - InstallTimeStamp | Long | 1498375028000 | The UNIX timestamp of the software installation. |
| -Version | String | 3.10.0 | The version of the software. |
| -Uuid | String | 9d327322-895b-4ba4- 9801-24411187b1e2 | The UUID of the server where the software is installed. |
| -InstanceId | String | i- 5fq05ua8z5cd1spus1t w | The ID of the instance where the software is installed. |
| -IntranetIp | String | 192.168.176.124 | The internal IP address of the server. |

| ard Advanced Edit | ion |   | oper Guide·API reference |
|---|---|---|---|
| Parameter | Type | Example | Description |

| -InternetIp | String | 43.186.xx.xx | The public IP address of the server. |
|---|---|---|---|
| -OrgId | String | 12 | The ID of the organization. |
| -ResourceSetId | String | 12 | The ID of the resource set. |
| -OrgName | String | test | The name of the organization. |
| - ResourceSetNam e | String | test | The name of the resource set. |
| RequestId | String | F0A8A039-930D-5EC1- 97C8-************ | The request ID is a unique identifier generated by Alibaba Cloud and can be used to troubleshoot issues. |
| PageInfo | Struct | { "TotalCount":2, "PageSize":20, "CurrentPage":1, "Count":2 } | The paging information. |
| -Count | Integer | 2 | The number of entries on the current page. |
| -PageSize | Integer | 20 | The number of entries per page. |
| -TotalCount | Integer | 2 | The total number of software entries. |
| -CurrentPage | Integer | 1 | The page number. |

**Examples**

Request example

```
https://[Endpoint]/?Action=DescribePropertySoftwareDetail&RegionId=cnhangzhou&Remark=47.100.XX.XX&Name=sshd&Path=/usr/xxx&SoftwareVersion=1.1.x.x&Extend=1&Uuid=inet-f6ac9a xxx&ContainerId=c1caea99b7649408aa5035dca00ac97ed&CurrentPage=1&PageSize=20&SelectType=equals&Ip=47.100. XX&GroupId=1&AssetType=IMAGE
```

Sample successful response `JSON` format

```
HTTP/1.1 200 OK Content-Type:application/json
```

`{`

```json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "Propertys":[
```

`{`

```json
            "Path":"/boot/.vmlinuz-3.10.0-514.el7.x86_64.hmac",
            "InstallTimeStamp":1498375028000,
            "InstallTime":"2017-06-25 15:17:08",
            "InstanceId":"i-5fq05ua8z5cd1spus1tw",
            "ResourceSetName":"test",
            "Ip":"192.168.176.124",
            "OrgName":"test",
            "IntranetIp":"192.168.176.124",
            "Name":"kernel",
            "InstanceName":"test1",
            "OrgId":"12",
            "Uuid":"9d327322-895b-4ba4-9801-24411187b1e2",
            "InternetIp":"43.186.xx.xx",
            "Version":"3.10.0",
            "Create":1704248313000,
            "ResourceSetId":"12",
            "CreateTimestamp":1704248313000
```

`}` `],`

```json
    "PageInfo":{
        "TotalCount":2,
        "PageSize":20,
        "CurrentPage":1,
        "Count":2
```

`}` `}` `XML` format

```xml
HTTP/1.1 200 OK Content-Type:application/xml <DescribePropertySoftwareDetailResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <Propertys>
        <Name>kernel</Name>
        <Path>/boot/.vmlinuz-3.10.0-514.el7.x86_64.hmac</Path>
        <InstanceName>test1</InstanceName>
        <Ip>192.168.176.124</Ip>
        <Create>1704248313000</Create>
        <CreateTimestamp>1704248313000</CreateTimestamp>
        <InstallTime>2017-06-25 15:17:08</InstallTime>
        <InstallTimeStamp>1498375028000</InstallTimeStamp>
        <Version>3.10.0</Version>
        <Uuid>9d327322-895b-4ba4-9801-24411187b1e2</Uuid>
        <InstanceId>i-5fq05ua8z5cd1spus1tw</InstanceId>
        <IntranetIp>192.168.176.124</IntranetIp>
        <InternetIp>43.186.xx.xx</InternetIp>
        <OrgId>12</OrgId>
        <ResourceSetId>12</ResourceSetId>
        <OrgName>test</OrgName>
        <ResourceSetName>test</ResourceSetName>
    </Propertys>
    <PageInfo>
        <Count>2</Count>
        <PageSize>20</PageSize>
        <TotalCount>2</TotalCount>
        <CurrentPage>1</CurrentPage>
    </PageInfo>
</DescribePropertySoftwareDetailResponse>
```

### 5.39 DescribePropertyUserDetail

Queries the details of server accounts.

**Authorization information**

| Operation | Access level | Resource type |
|---|---|---|
| yundun- css:DescribePropertyUserDetail | Read | acs:yundun-css:*:{#accountId}:* |

**Throttling**

Single user: 10 queries per second (QPS). API: 100 QPS.

**Request headers**

This operation uses common request headers. No special request headers are required. For more information, see Common request parameters.

**Request parameters**

| Paramete r | Type | Positio n | Required | Example | Description |
|---|---|---|---|---|---|
| Remark | String | Query | No | 192.168.x.x | The name or IP address of the server. |

| Container Sec | urity Serv | ice Devel |   | Alibab | a Cloud Security-Server G |
|---|---|---|---|---|---|

| Paramete r | Type | Positio n | Required | Example | Description |
|---|---|---|---|---|---|
| User | String | Query | No | root | The username. |
| IsRoot | String | Query | No | 1 | Specifies whether the account has root permissions. Valid values: 0 : No 1 : Yes |
| Extend | String | Query | No | 1 | Specifies whether to use a fuzzy search for the User parameter. 1 : Yes 0 : No |
| Uuid | String | Query | No | inet-00f20b1a-e2dd-408b- b38e-***** | The UUID of the asset. |
| CurrentPage | Integer | Query | No | 1 | The number of the page to return. |
| PageSize | Integer | Query | No | 20 | The number of entries to return on each page. |
| SelectType | String | Query | No | equals | The query type. The default value is like . Valid values: equals : term query like : fuzzy query |
| AssetType | String | Query | No | IMAGE | The type of the asset fingerprint. The default value is HOST . Valid values: IMAGE : image asset fingerprint HOST : host asset fingerprint |
| Ip | String | Query | No | 47.200.XX.XX | The IP address of the server. |
| GroupId | String | Query | No | 1 | The group ID. |
| TagIdListStri ng | String | Query | No | 1 | A list of tags. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| Propertys | Array | [ { "IsRoot":"0", "User":"root", "LastLoginIp":"N/A", "ResourceSetName":"t est", "Ip":"192.168.176.124" , "IsCouldLogin":0, "OrgName":"test", "IntranetIp":"172.25.X X.XX", "LastLoginTimestamp": 1704248304000, "InternetIp":"1.2.XX.XX ", "Create":"1704248304 000", "ResourceSetId":"12", "CreateTimestamp":17 04248304000, "IsPasswdExpired":0, "PasswordExpirationDa te":"never", "IsSudoer":0, "Status":"0", "GroupNames":" [bin,admin]", "InstanceId":"", "IsPasswdLocked":0, "AccountsExpirationDa te":"never", "InstanceName":"", "LastLoginTime":"N/A", "OrgId":"12", "Uuid":"00f2-xxx-xxx", "IsUserExpired":0 } ] | A list of account information. |
| -GroupNames | String | [bin,admin] | The user groups. |
| -LastLoginTime | String | N/A | The time of the last logon. |
| - LastLoginTimesta mp | Long | 1704248304000 | The timestamp of the last logon. |
| -IsRoot | String | 0 | Indicates whether the account has root permissions. 1 : Yes. 0 : No. |
| -InstanceName | String | test | The name of the instance. |
| - AccountsExpiratio nDate | String | never | The expiration date of the account. |
| - PasswordExpirati onDate | String | never | The expiration date of the password. |
| -Ip | String | 192.168.176.124 | The IP address of the server. |
| -Create | String | 1704248304000 | The time of the last scan. |

| Container Security oper Guide·API ref | Service Devel erence |   | Alibaba Cloud Security-Server G ard Advanced Edition |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| - CreateTimestamp | Long | 1704248304000 | The timestamp of the last scan. |
| -User | String | root | User groups |
| -Uuid | String | 00f2-xxx-xxx | The unique ID of the server. |
| -LastLoginIp | String | N/A | Last login |
| -InstanceId | String | idaas ue2jvisn35ea5lm _ thk267xxxxx | The ID of the instance. |
| -IntranetIp | String | 172.25.XX.XX | The private IP address of the server. |
| -InternetIp | String | 1.2.XX.XX | The public IP address of the instance. |
| -IsPasswdExpired | Integer | 0 | Indicates whether the password has expired. * 0 : No * 1 : Yes |
| -IsPasswdLocked | Integer | 0 | Indicates whether the password is locked. 0 : No 1 : Yes |
| -IsUserExpired | Integer | 0 | Indicates whether the user account has expired. 0 : No 1 : Yes |
| -IsCouldLogin | Integer | 0 | Indicates whether the account can be used for interactive logon. 0 : No 1 : Yes |
| -IsSudoer | Integer | 0 | Indicates whether the account has sudo permissions. 0 : No 1 : Yes |
| -Status | String | 0 | The logon status of the account. 0 : Logon is not allowed. 1 : Logon is allowed. |
| -OrgId | String | 12 | The organization ID. |
| -ResourceSetId | String | 12 | The resource set ID. |
| -OrgName | String | test | The organization name. |

| Alibaba Cloud Sec | urity-Server Gu |   | Container Security Service Deve |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| - ResourceSetNam e | String | test | The resource set name. |
| RequestId | String | F0A8A039-930D-5EC1- 97C8-************ | The request ID is a unique identifier generated by Alibaba Cloud to help you troubleshoot issues. |
| PageInfo | Struct | { "TotalCount":20, "PageSize":20, "CurrentPage":1, "Count":2 } | The pagination information. |
| -Count | Integer | 2 | The number of entries on the current page. |
| -PageSize | Integer | 20 | The number of entries per page. |
| -TotalCount | Integer | 20 | The total number of entries returned. |
| -CurrentPage | Integer | 1 | The page number of the returned page. |

**Examples**

Sample request

```
https://[Endpoint]/?Action=DescribePropertyUserDetail&RegionId=cnhangzhou&Remark=192.168.x.x&User=root&IsRoot=1&Extend=1&Uuid=inet-00f20b1a-e2dd-408b-b38e-
*****&CurrentPage=1&PageSize=20&SelectType=equals&AssetType=IMAGE&Ip=47.200.XX.XX&GroupId=1&TagIdListStr
```

`=1` Sample responses `JSON` format

```
HTTP/1.1 200 OK Content-Type:application/json
```

`{`

```json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "PageInfo":{
        "TotalCount":20,
        "PageSize":20,
        "CurrentPage":1,
        "Count":2
```

`},`

```json
    "Propertys":[
```

`{`

```json
            "IsRoot":"0",
            "User":"root",
            "LastLoginIp":"N/A",
            "ResourceSetName":"test",
            "Ip":"192.168.176.124",
            "IsCouldLogin":0,
            "OrgName":"test",
            "IntranetIp":"172.25.XX.XX",
            "LastLoginTimestamp":1704248304000,
            "InternetIp":"1.2.XX.XX",
            "Create":"1704248304000",
            "ResourceSetId":"12",
            "CreateTimestamp":1704248304000,
            "IsPasswdExpired":0,
            "PasswordExpirationDate":"never",
            "IsSudoer":0,
            "Status":"0",
            "GroupNames":"[bin,admin]",
            "InstanceId":"",
            "IsPasswdLocked":0,
            "AccountsExpirationDate":"never",
            "InstanceName":"",
            "LastLoginTime":"N/A",
            "OrgId":"12",
            "Uuid":"00f2-xxx-xxx",
            "IsUserExpired":0
```

`}` `]` `}` `XML` format

```xml
HTTP/1.1 200 OK Content-Type:application/xml <DescribePropertyUserDetailResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <PageInfo>
        <Count>2</Count>
        <PageSize>20</PageSize>
        <TotalCount>20</TotalCount>
        <CurrentPage>1</CurrentPage>
    </PageInfo>
    <Propertys>
        <LastLoginTime>N/A</LastLoginTime>
        <LastLoginTimestamp>1704248304000</LastLoginTimestamp>
        <GroupNames>
            <GroupName>[bin,admin]</GroupName>
        </GroupNames>
        <IsRoot>0</IsRoot>
        <InstanceName></InstanceName>
        <AccountsExpirationDate>never</AccountsExpirationDate>
        <PasswordExpirationDate>never</PasswordExpirationDate>
        <Ip>192.168.176.124</Ip>
        <Create>1704248304000</Create>
        <CreateTimestamp>1704248304000</CreateTimestamp>
        <User>root</User>
        <Uuid>00f2-xxx-xxx</Uuid>
        <LastLoginIp>N/A</LastLoginIp>
        <InstanceId></InstanceId>
        <IntranetIp>172.25.XX.XX</IntranetIp>
        <InternetIp>1.2.XX.XX</InternetIp>
        <IsPasswdExpired>0</IsPasswdExpired>
        <IsPasswdLocked>0</IsPasswdLocked>
        <IsUserExpired>0</IsUserExpired>
        <IsCouldLogin>0</IsCouldLogin>
        <IsSudoer>0</IsSudoer>
        <Status>0</Status>
        <OrgId>12</OrgId>
        <ResourceSetId>12</ResourceSetId>
        <OrgName>test</OrgName>
        <ResourceSetName>test</ResourceSetName>
    </Propertys>
</DescribePropertyUserDetailResponse>
```

### 5.40 ExportRecord

Call the ExportRecord operation to export detection results to an Excel file. You can export results from various pages, such as Asset Center, cloud platform configuration checks, image security scans, attack analysis, and AccessKey pair leak detection.

**Authorization information**

| Operation | Access level | Resource type |
|---|---|---|
| yundun-css:ExportRecord | Write | acs:yundun-css:*:{#accountId}:* |

**Traffic shaping**

Call frequency per user: 10 queries per second (QPS). Call frequency for the API: 100 QPS.

**Request header**

This operation has no special request headers. For information about common request headers, see Common request parameters.

**Request parameters**

| Paramete r | Type | Positio n | Required | Example | Description |
|---|---|---|---|---|---|
| Lang | String | Query | No | zh | The language of the request and response. Default value: zh. zh: Chinese. en: English. |
| Params | String | Query | No | {"extend":"1","currentPage": 1,"pageSize":10} | The filter conditions for the export. Note This is a generic export operation for the detection lists of multiple Security Center features. The fields for this parameter vary based on the feature. Avoid specifying this parameter when you call the operation. Leave this parameter unspecified to export the information list. Then, filter the data in the exported Excel file. |

| Paramete r | Type | Positio n | Required | Example | Description |
|---|---|---|---|---|---|
| ExportType | String | Query | Yes | database | The type of list to export. Valid values: assetInstance : The list of servers in Asset Center. user : The list of Asset Fingerprints for accounts. port : The list of Asset Fingerprints for ports. process : The list of Asset Fingerprints for processes. sca : The list of Asset Fingerprints for middleware. database : The list of Asset Fingerprints for databases. web : The list of Asset Fingerprints for web services. software : The list of Asset Fingerprints for software. cron : The list of Asset Fingerprints for cron jobs. autorun : The list of Asset Fingerprints for startup items. lkm : The list of Asset Fingerprints for kernel modules. webserver : The list of Asset Fingerprints for websites. imageVulExport : The list of system vulnerabilities for images. imageBaseLineExport : The list of baseline check results for images. imageAffectedMalicious Export : The list of check results for malicious samples in images. baselineCspm : The list of detection results from cloud platform configuration checks. attack : The list of alert events from attack analysis. accessKey : The list of alert events from AccessKey pair leak detection. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D-5EC1- 97C8-************ | The ID of the request. It is a unique identifier generated by Alibaba Cloud for this request and can be used to troubleshoot issues. |
| Id | Long | 131231 | The ID of the exported file. |
| FileName | String | cms 20171101.xlsx _ | The name of the exported file. |

**Examples**

Request example

```json
https://[Endpoint]/?Action=ExportRecord&RegionId=cn-hangzhou&Lang=zh&Params= {"extend":"1","currentPage":1,"pageSize":10}&ExportType=database
```

Response example `JSON` format

```
HTTP/1.1 200 OK Content-Type:application/json
```

`{`

```json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "Id":131231,
    "FileName":"cms_20171101.xlsx"
```

`}` `XML` format

```xml
HTTP/1.1 200 OK Content-Type:application/xml <ExportRecordResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <Id>131231</Id>
    <FileName>cms_20171101.xlsx</FileName>
</ExportRecordResponse>
```

**5.41.**

### GetClusterCheckItemWarningStatistics

Call the GetClusterCheckItemWarningStatistics operation to retrieve statistics about baseline check results, such as the number of servers that are checked, the number of check items, and the recent pass rate.

**Authorization information**

| Operation | Access level | Resource type |
|---|---|---|
| yundun- css:GetClusterCheckItemWarningStat istics | Read | acs:yundun-css:*:{#accountId}:* |

**Traffic shaping**

The request frequency for a single user is limited to 10 queries per second (QPS). The request frequency for this operation is limited to 100 queries per second (QPS).

**Request header**

This operation uses only common request headers. For more information, see Common request parameters.

**Request parameters**

| Paramete r | Type | Positio n | Required | Example | Description |
|---|---|---|---|---|---|
| SourceIp | String | Query | No | 219.133.XX.XX | The source IP address. |
| ClusterId | String | Query | No | c690a0789419f4284a4e0a29 e12fe**** | The cluster ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D-5EC1- 97C8-************ | The request ID is a unique identifier generated by Alibaba Cloud that is used to troubleshoot issues. |
| Data | Struct | { "MediumWarningCount ":2, "HighWarningCount":1 0, "LowWarningCount":3 } | The statistics of baseline check warnings. |
| - LowWarningCoun t | Integer | 3 | The number of low-risk check items on the server. |
| - MediumWarningC ount | Integer | 2 | The number of medium-risk check items on the server. |
| - HighWarningCou nt | Integer | 10 | The number of high-risk check items on the server. |

**Examples**

Request example

```
https://[Endpoint]/?Action=GetClusterCheckItemWarningStatistics&RegionId=cnhangzhou&SourceIp=219.133.XX.XX&ClusterId=c690a0789419f4284a4e0a29e12fe****
```

Response example `JSON` format

```
HTTP/1.1 200 OK Content-Type:application/json
```

`{`

```json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "Data":{
        "MediumWarningCount":2,
        "HighWarningCount":10,
        "LowWarningCount":3
```

`}` `}` `XML` format

```xml
HTTP/1.1 200 OK Content-Type:application/xml <GetClusterCheckItemWarningStatisticsResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <Data>
        <LowWarningCount>3</LowWarningCount>
        <MediumWarningCount>2</MediumWarningCount>
        <HighWarningCount>10</HighWarningCount>
    </Data>
</GetClusterCheckItemWarningStatisticsResponse>
```

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | -101 | -101 | %s %s |

### 5.42 GetClusterSuspEventStatistics

Call the GetClusterSuspEventStatistics operation to query statistics on the severity levels of alerts.

**Authorization information**

| Operation | Access level | Resource type |
|---|---|---|
| yundun- css:GetClusterSuspEventStatistics | Read | acs:yundun-css:*:{#accountId}:* |

**Throttling**

The throttling limit for each user is 10 queries per second (QPS). The throttling limit for this operation is 100 QPS.

**Request headers**

This operation uses common request headers. Special request headers are not required. For more information, see Common request parameters.

**Request parameters**

| Paramete r | Type | Positio n | Required | Example | Description |
|---|---|---|---|---|---|
| SourceIp | String | Query | No | 219.133.XX.XX | The source IP address of the request. |
| Type | String | Query | No | alarm | The type. The value is fixed to `alarm` for alert queries. |
| From | String | Query | No | css | The source of the request. The value is fixed to `css`. |
| ClusterId | String | Query | No | Cccfd68c474454665ace07ef ce924*** | The ID of the container cluster. |

| Alibaba Cloud ard Advanced | Security- Edition | Server Gu |   | Conta | iner Security Service Deve oper Guide·API reference |
|---|---|---|---|---|---|

| Paramete r | Type | Positio n | Required | Example | Description |
|---|---|---|---|---|---|
| ContainerFie ldName | String | Query | No | containerId | The container search item. Valid values: instanceId: The ID of the container instance. clusterId: The ID of the cluster. regionId: The region of the container. clusterName: The name of the cluster. image: The name of the image. imageRepoName: The name of the image repository. imageRepoNamespace: The namespace of the image repository. imageRepoTag: The tag of the image repository. imageDigest: The digest of the image. clusterType: The type of the cluster. hostIp: The public IP address. pod: The pod. podIp: The IP address of the pod. containerId: The ID of the container. vulStatus: Specifies whether the container has vulnerabilities. alarmStatus: Specifies whether the container has security alerts. riskStatus: Specifies whether the container has threats. riskLevel: The threat level of the container. containerScope: The type of the container. |
| ContainerFie ldValue | String | Query | No | 4b092975242bea7fa4af8515 057f660faf2b285bc1693fd4c b0e7bfac***** | The value of the container search item. |
| TargetType | String | Query | No | containerId | The ContainerFieldName and ContainerFieldValue parameters are used to filter the target information. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D-5EC1- 97C8-************ | The request ID is a unique identifier generated by Alibaba Cloud that helps you troubleshoot issues. |

| Container Security oper Guide·API ref | Service Devel erence |   | Alibaba Cloud Security-Server Gu ard Advanced Edition |
|---|---|---|---|
| Parameter | Type | Example | Description |

| SuspStatistics | Struct | { "Serious":2, "Suspicious":3, "Remind":1 } | Events |
|---|---|---|---|
| -Serious | Integer | 2 | The number of serious events. |
| -Suspicious | Integer | 3 | The number of suspicious events. |
| -Remind | Integer | 1 | The number of reminder events. |

**Examples**

Request example

```
https://[Endpoint]/?Action=GetClusterSuspEventStatistics&RegionId=cnhangzhou&SourceIp=219.133.XX.XX&Type=alarm&From=css&ClusterId=Cccfd68c474454665ace07efce924***&Container ldName=containerId&ContainerFieldValue=4b092975242bea7fa4af8515057f660faf2b285bc1693fd4cb0e7bfac*****&Ta tType=containerId
```

Response example `JSON` format

```
HTTP/1.1 200 OK Content-Type:application/json
```

`{`

```json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "SuspStatistics":{
        "Serious":2,
        "Suspicious":3,
        "Remind":1
```

`}` `}` `XML` format

```xml
HTTP/1.1 200 OK Content-Type:application/xml <GetClusterSuspEventStatisticsResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <SuspStatistics>
        <Serious>2</Serious>
        <Suspicious>3</Suspicious>
        <Remind>1</Remind>
    </SuspStatistics>
</GetClusterSuspEventStatisticsResponse>
```

### 5.43 IgnoreCheckItems

Call the IgnoreCheckItems operation to ignore risk items in baseline checks.

**Authorization**

| Operation | Access level | Resource type |
|---|---|---|
| yundun-css:IgnoreCheckItems | Write | acs:yundun-css:*:{#accountId}:* |

**Throttling**

Calls from a single user: 10 queries per second (QPS). Calls to the API operation: 100 QPS.

**Request headers**

This operation uses common request headers. No special request headers are required. For more information, see Common request parameters.

**Request parameters**

| Paramete r | Type | Positio n | Required | Example | Description |
|---|---|---|---|---|---|
| SourceIp | String | Query | No | 219.133.XX.XX | The source IP address of the request. |
| Type | Integer | Query | Yes | 1 | The type of operation. Valid values: 1: Ignore 2: Stop ignoring |
| Reason | String | Query | No | already config in another way | Rationale |
| Source | String | Query | No | default | The data source. Valid values: default: host baseline agentless: agentless baseline |
| UuidList | Repeat List | Query | No | 55bf7984-9b3b-4e8d-be8e- f3e5b0b4**** | The UUIDs of the servers to ignore. |
| CheckAndRis kTypeList | Repeat List | Query | No | [{"CheckId":52,"RiskType","w eak password"}] _ | A list of check items to ignore. |
| -CheckId | Long |   | No | 52 | The ID of the check item. |
| -RiskType | String |   | No | weak password _ | The type of the baseline risk. |
| CheckIds | Repeat List | Query | No | 1 | A list of check item IDs. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D-5EC1- 97C8-************ | The ID of the request. This ID is unique to the request. You can use this ID to troubleshoot issues. |

**Examples**

Request example

```
https://[Endpoint]/?Action=IgnoreCheckItems&RegionId=cnhangzhou&SourceIp=219.133.XX.XX&Type=1&Reason=already config in another way&Source=default&UuidList.1=55bf7984-9b3b-4e8d-be8e-f3e5b0b4****&CheckIds.1=1
```

Response example `JSON` format

```
HTTP/1.1 200 OK Content-Type:application/json
```

`{`

```json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************"
```

`}` `XML` format

```xml
HTTP/1.1 200 OK Content-Type:application/xml <IgnoreCheckItemsResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
</IgnoreCheckItemsResponse>
```

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 500 | -100 | ServerError | ServerError |
| 500 | ServerError | ServerError | ServerError |
| 403 | NoPermission | NoPermission | caller has no permission |

### 5.44 ListCheckItemWarningMachine

Call the ListCheckItemWarningMachine operation to retrieve the machines that have alerts for a specific baseline check item.

**Authorization information**

| Operation | Access level | Resource type |
|---|---|---|
| yundun- css:ListCheckItemWarningMachine | Read | acs:yundun-css:*:{#accountId}:* |

**Traffic shaping**

Rate limit for a single user: 10 queries per second (QPS). Rate limit for this operation: 100 QPS.

**Request headers**

This operation uses common request headers. No special request headers are required. For more information, see Common parameters.

**Request parameters**

| Paramete r | Type | Locatio n | Required | Example | Description |
|---|---|---|---|---|---|
| SourceIp | String | Query | No | 219.133.XX.XX | The source IP address. |
| CheckId | Long | Query | Yes | 8 | The ID of the check item. |
| RiskType | String | Query | No | cis | The category of the check item. |
| Status | Integer | Query | No | 3 | The status of the check item. The default value is null. Valid values: 1: Failed 2: Verifying 3: Passed 6: Ignored 7: Fixing |
| Remark | String | Query | No | 225 | Fuzzy machine matching. |
| ContainerFie ldName | String | Query | No | clusterId | The name of the query parameter for container security. |
| ContainerFie ldValue | String | Query | No | ce89cdd0ea732472a870382 1b19e**** | The value of the query parameter for container security. |
| Lang | String | Query | No | zh | The language of the content in the request and response. Default value: zh. Valid values: zh: Chinese en: English |
| CurrentPage | Integer | Query | No | 1 | The page number to return. The value must be a positive integer. Default value: 1. |
| PageSize | Integer | Query | No | 20 | The number of entries to return on each page. Default value: 20. If you leave this parameter empty, 20 entries are returned. |
| GroupId | Long | Query | No | 1161**** | The ID of the asset group to query. |

| Paramete r | Type | Locatio n | Required | Example | Description |
|---|---|---|---|---|---|
| Source | String | Query | No | default | The data source. If you leave this parameter empty, the results of host baselines are queried by default. Valid values: default: host agentless: agentless |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| List | Array | [ { "Status":7, "Bind":true, "InstanceId":"i- bp1a69mvjujbakxu**** ", "PortOpen":true, "WarningRiskList":[ { "RiskId":215, "RiskName":"Alibaba Cloud Linux/Aliyun Linux 2 Baseline for China classified protection of cybersecurity-Level II" } ], "LastScanTime":16946 92471000, "TargetName":"jenkins ****", "IntranetIp":"172.25.X X.XX", "TargetId":"30****", "InstanceName":"sql- test-0****", "OrgId":"1", "Uuid":"49e25e0f- bb51-4a5a-a1b3- 13a4ddaa****", "FixList":[ { "RiskId":215, "RiskName":"Alibaba Cloud Linux/Aliyun Linux 2 Baseline for China classified protection of cybersecurity-Level II" } ], "InternetIp":"8.210.XX. XX", "ContainerId":"48a6d9 a92435a13ad573372c 3f3c63b7e04d1064581 41df9f9215570******** ", "ContainerName":"mys ql", "TargetType":"ECS IMA _ GE", "Prompt":"There is a weak password (username/password): root/he*****34", "RegionId":"cn- hangzhou", "AuthVersion":5, "ResourceSetId":"11", "LastHandleTime":169 4692471000 } ] | A list of machines that have alerts. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| -WarningRiskList | Array | [ { "RiskId":215, "RiskName":"Alibaba Cloud Linux/Aliyun Linux 2 Baseline for China classified protection of cybersecurity-Level II" } ] | A list of baselines that have threats detected for this check item. |
| --RiskId | Long | 215 | The ID of the baseline. |
| --RiskName | String | Alibaba Cloud Linux/Aliyun Linux 2 Baseline for China classified protection of cybersecurity-Level II | The name of the baseline. |
| -FixList | Array | [ { "RiskId":215, "RiskName":"Alibaba Cloud Linux/Aliyun Linux 2 Baseline for China classified protection of cybersecurity-Level II" } ] | A list of baselines that have fixable threats for this check item. |
| --RiskId | Long | 215 | The ID of the baseline. |
| --RiskName | String | Alibaba Cloud Linux/Aliyun Linux 2 Baseline for China classified protection of cybersecurity-Level II | The name of the baseline. |
| -Status | Integer | 7 | The status of the check item. Valid values: 1: Failed 2: Verifying 3: Passed 6: Ignored 7: Fixing |
| -Bind | Boolean | true | Indicates whether the asset is granted the required permissions. Valid values: true: The asset is granted the required permissions. false: The asset is not granted the required permissions. |
| -AuthVersion | Integer | 5 | The edition of Security Center that is authorized to protect the asset. Valid values: 1: Free Edition 6: Anti-virus Edition 5: Premium Edition 3: Enterprise Edition 7: Ultimate Edition 10: Value-added Service Edition |

| Parameter | Type | Example | Description |
|---|---|---|---|
| -PortOpen | Boolean | true | Indicates whether a port of the server is exposed to the Internet. Valid values: true: A port of the server is exposed to the Internet. false: No ports of the server are exposed to the Internet. |
| -InstanceId | String | i- bp1a69mvjujbakxu**** | The ID of the server instance. |
| -IntranetIp | String | 172.25.XX.XX | The private IP address of the affected asset. |
| -InternetIp | String | 8.210.XX.XX | The public IP address of the affected asset. |
| -InstanceName | String | sql-test-0**** | The name of the server instance. |
| -Uuid | String | 49e25e0f-bb51-4a5a- a1b3-13a4ddaa**** | The UUID of the server. |
| -RegionId | String | cn-hangzhou | The ID of the region where the asset resides. |
| -Prompt | String | There is a weak password (username/password): root/he*****34 | The message for the baseline check threat. |
| -ContainerId | String | 48a6d9a92435a13ad5 73372c3f3c63b7e04d1 06458141df9f9215570 ******** | The container ID. |
| -ContainerName | String | mysql | The name of the container. |
| -TargetName | String | jenkins**** | The name of the scanned object. |
| -TargetId | String | 30**** | The ID of the scanned object. |
| -TargetType | String | ECS IMAGE _ | The type of the scanned object. Valid values: ECS SNAPSHOT: snapshot _ ECS IMAGE: image _ |
| -LastScanTime | Long | 1694692471000 | The timestamp of the last scan. Unit: milliseconds. |
| -LastHandleTime | Long | 1694692471000 | The timestamp of when the check item threat on the machine was last handled. Unit: milliseconds. |
| -OrgId | String | 1 | The ID of the organization. |
| -ResourceSetId | String | 11 | The ID of the resource set. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D-5EC1- 97C8-************ | The invocation request ID is a unique identifier generated by Alibaba Cloud that you can use to troubleshoot issues. |
| PageInfo | Struct | { "TotalCount":103, "PageSize":20, "CurrentPage":1, "Count":2, "LastRowKey":"null" } | The pagination information. |
| -CurrentPage | Integer | 1 | The page number of the returned page. |
| -PageSize | Integer | 20 | The number of entries returned on each page. |
| -TotalCount | Integer | 103 | The total number of affected assets. |
| -Count | Integer | 2 | The number of affected assets returned on the current page. |

**Examples**

Request example

```
https://[Endpoint]/?Action=ListCheckItemWarningMachine&RegionId=cnhangzhou&SourceIp=219.133.XX.XX&CheckId=8&RiskType=cis&Status=3&Remark=225&ContainerFieldName=clusterId& tainerFieldValue=ce89cdd0ea732472a8703821b19e****&Lang=zh&CurrentPage=1&PageSize=20&GroupId=1161****&Sou =default
```

Successful response example `JSON` format

```
HTTP/1.1 200 OK Content-Type:application/json
```

`{`

```json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "List":[
```

`{`

```json
            "Status":7,
            "Bind":true,
            "InstanceId":"i-bp1a69mvjujbakxu****",
            "PortOpen":true,
            "WarningRiskList":[
```

`{`

```json
                    "RiskId":215,
                    "RiskName":"Alibaba Cloud Linux/Aliyun Linux 2 Baseline for China classified
protection of cybersecurity-Level II"
```

`}` `],`

```json
            "LastScanTime":1694692471000,
            "TargetName":"jenkins****",
            "IntranetIp":"172.25.XX.XX",
            "TargetId":"30****",
            "InstanceName":"sql-test-0****",
            "OrgId":"1",
            "Uuid":"49e25e0f-bb51-4a5a-a1b3-13a4ddaa****",
            "FixList":[
```

`{`

```json
                    "RiskId":215,
                    "RiskName":"Alibaba Cloud Linux/Aliyun Linux 2 Baseline for China classified
protection of cybersecurity-Level II"
```

`}` `],`

```json
            "InternetIp":"8.210.XX.XX",
            "ContainerId":"48a6d9a92435a13ad573372c3f3c63b7e04d106458141df9f9215570********",
            "ContainerName":"mysql",
            "TargetType":"ECS_IMAGE",
            "Prompt":"There is a weak password (username/password): root/he*****34",
            "RegionId":"cn-hangzhou",
            "AuthVersion":5,
            "ResourceSetId":"11",
            "LastHandleTime":1694692471000
```

`}` `],`

```json
    "PageInfo":{
        "TotalCount":103,
        "PageSize":20,
        "CurrentPage":1,
        "Count":2,
        "LastRowKey":"null"
```

`}` `}` `XML` format

```xml
HTTP/1.1 200 OK Content-Type:application/xml <ListCheckItemWarningMachineResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <List>
        <Status>7</Status>
        <Bind>true</Bind>
        <AuthVersion>5</AuthVersion>
        <PortOpen>true</PortOpen>
        <InstanceId>i-bp1a69mvjujbakxu****</InstanceId>
        <IntranetIp>172.25.XX.XX</IntranetIp>
        <InternetIp>8.210.XX.XX</InternetIp>
        <InstanceName>sql-test-0****</InstanceName>
        <Uuid>49e25e0f-bb51-4a5a-a1b3-13a4ddaa****</Uuid>
        <RegionId>cn-hangzhou</RegionId>
        <Prompt>There is a weak password (username/password): root/he*****34</Prompt>
        <ContainerId>48a6d9a92435a13ad573372c3f3c63b7e04d106458141df9f9215570********</ContainerId>
        <ContainerName>mysql</ContainerName>
        <TargetName>jenkins****</TargetName>
        <TargetId>30****</TargetId>
        <TargetType>ECS_IMAGE</TargetType>
        <LastScanTime>1694692471000</LastScanTime>
        <LastHandleTime>1694692471000</LastHandleTime>
        <OrgId>1</OrgId>
        <ResourceSetId>11</ResourceSetId>
        <WarningRiskList>
            <RiskId>215</RiskId>
            <RiskName>Alibaba Cloud Linux/Aliyun Linux 2 Baseline for China classified protection of c
ybersecurity-Level II</RiskName>
        </WarningRiskList>
        <FixList>
            <RiskId>215</RiskId>
            <RiskName>Alibaba Cloud Linux/Aliyun Linux 2 Baseline for China classified protection of c
ybersecurity-Level II</RiskName>
        </FixList>
    </List>
    <PageInfo>
        <CurrentPage>1</CurrentPage>
        <LastRowKey>null</LastRowKey>
        <PageSize>20</PageSize>
        <TotalCount>103</TotalCount>
        <Count>2</Count>
    </PageInfo>
</ListCheckItemWarningMachineResponse>
```

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | -101 | -101 | %s %s |

### 5.45 ListCheckItemWarningSummary

Call the ListCheckItemWarningSummary operation to retrieve statistics about risks for baseline check items.

**Authorization**

| Operation | Access level | Resource type |
|---|---|---|
| yundun- css:ListCheckItemWarningSummary | Read | acs:yundun-css:*:{#accountId}:* |

**Traffic shaping**

Throttling limit for a single user: 10 queries per second (QPS). Throttling limit for the API operation: 100 QPS.

**Request headers**

This operation uses common request headers. No special request headers are required. For more information, see Common request parameters.

**Request parameters**

| Paramete r | Type | Positio n | Required | Example | Description |
|---|---|---|---|---|---|
| SourceIp | String | Query | No | 219.133.XX.XX | The source IP address of the request. |
| CheckWarni ngStatus | Integer | Query | No | 1 | The status of the threat. If you do not specify this parameter, threats in all statuses are queried. Valid values: * 1: Failed * 3: Passed * 6: Whitelisted |
| CheckLevel | String | Query | No | high | The severity level of the threat. If you do not specify this parameter, threats of all severity levels are queried. Valid values: * high * medium * low |
| ContainerFie ldName | String | Query | No | clusterId | The name of the query parameter for container security. |
| ContainerFie ldValue | String | Query | No | c471f0f61b9c04f8380556e9 22cf1**** | The value of the query parameter for container security. |
| TargetType | String | Query | No | 1 | This parameter is deprecated. |
| ClusterId | String | Query | No | c690a0789419f4284a4e0a29 e12fe**** | The ID of the cluster. |
| CurrentPage | Integer | Query | No | 1 | The number of the page to return. Default value: 1. |
| PageSize | Integer | Query | No | 20 | The number of entries to return on each page. Default value: 20. |

| Paramete r | Type | Positio n | Required | Example | Description |
|---|---|---|---|---|---|
| CheckItemF uzzy | String | Query | No | password | The name of the check item to query. Fuzzy match is supported. |

**Response data**

| Parameter | Type | Example | Description |
|---|---|---|---|
| List | Array | [ { "Status":1, "EnableRisks":[ "CIS Ubuntu Linux 14 LTS Benchmark" ], "Description":"Config the Event Audit policys", "CheckLevel":"high", "AffiliatedRisks":[ "CIS Ubuntu Linux 14 LTS Benchmark" ], "AffiliatedRiskTypes":[ "CIS Compliance checks" ], "ContainerCheckItem": true, "CheckId":696, "CheckItem":"Config the Event Audit policys", "Alias":"week pa****", _ "CheckType":"Security audit", "WarningMachineCoun t":20, "Advice":"In the Administrative Tools window, double-click Local Security Policy. In the Local Security Policy window that appears, choose Security Settings\\\\Local Policies\\\\Audit Policy, configure all audit policies as: `Success, Failure`.", "RiskType":"weak pass _ word" } ] | The list of statistics about check item risks. |
| - AffiliatedRiskType s | List | ["CIS Compliance checks"] | The list of baseline classifications to which the check item belongs. |
| -AffiliatedRisks | List | ["CIS Ubuntu Linux 14 LTS Benchmark"] | The list of baselines to which the check item belongs. |
| -EnableRisks | String | ["CIS Ubuntu Linux 14 LTS Benchmark"] | The list of baselines that are enabled for the check item. |
| -RiskType | String | weak password _ | The classification of the baseline. |
| -Alias | String | week pa**** _ | The name of the baseline classification. |
| -CheckId | Long | 696 | The ID of the check item. |

| Container Security oper Guide·API ref | Service Devel erence |   | Alibaba Cloud Security-Server G ard Advanced Edition |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| -CheckItem | String | Config the Event Audit policys | The description of the check item. |
| -CheckLevel | String | high | The severity level of the threat. Valid values: high medium: Indicates a medium severity. low |
| -CheckType | String | Security audit | The type of the check item. |
| -Advice | String | In the Administrative Tools window, double- click Local Security Policy. In the Local Security Policy window that appears, choose Security Settings\\Local Policies\\Audit Policy, configure all audit policies as: `Success, Failure`. | The suggestion for handling the check item. |
| -Description | String | Config the Event Audit policys | The detailed description of the check item. |
| -Status | Integer | 1 | The status of the threat. Valid values: 1: Failed 3: Passed 6: Whitelisted |
| - WarningMachine Count | Integer | 20 | The number of machines affected by the risk that is associated with the check item. |
| - ContainerCheckIt em | Boolean | true | Indicates whether the check item belongs to the pod runtime class. Valid values: true false |
| RequestId | String | F0A8A039-930D-5EC1- 97C8-************ | The request ID is a unique identifier generated by Alibaba Cloud and can be used to troubleshoot problems. |
| PageInfo | Struct | { "TotalCount":105, "PageSize":20, "CurrentPage":1, "Count":3, "LastRowKey":"null" } | The pagination information. |
| -CurrentPage | Integer | 1 | The page number of the returned page. |
| -PageSize | Integer | 20 | The number of entries returned per page. |
| -TotalCount | Integer | 105 | The total number of check items found. |

| Alibaba Cloud Sec | urity-Server Gu |   | Container Security Service Deve |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| -Count | Integer | 3 | The number of check items returned on the current page. |

**Examples**

Sample request

```
https://[Endpoint]/?Action=ListCheckItemWarningSummary&RegionId=cnhangzhou&SourceIp=219.133.XX.XX&CheckWarningStatus=1&CheckLevel=high&ContainerFieldName=clusterId&Contai FieldValue=c471f0f61b9c04f8380556e922cf1****&TargetType=1&ClusterId=c690a0789419f4284a4e0a29e12fe****&Cu ntPage=1&PageSize=20&CheckItemFuzzy=password
```

Sample responses `JSON` format

```
HTTP/1.1 200 OK Content-Type:application/json
```

`{`

```json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "List":[
```

`{`

```json
            "Status":1,
            "EnableRisks":[
                "CIS Ubuntu Linux 14 LTS Benchmark"
```

`],`

```json
            "Description":"Configure the event audit policies",
            "CheckLevel":"high",
            "AffiliatedRisks":[
                "CIS Ubuntu Linux 14 LTS Benchmark"
```

`],`

```json
            "AffiliatedRiskTypes":[
                "CIS Compliance checks"
```

`],`

```json
            "ContainerCheckItem":true,
            "CheckId":696,
            "CheckItem":"Configure the event audit policies",
            "Alias":"week_pa****",
            "CheckType":"Security audit",
            "WarningMachineCount":20,
            "Advice":"In the Administrative Tools window, double-click Local Security Policy. In the L
ocal Security Policy window, go to Security Settings\\\\Local Policies\\\\Audit Policy and set all au dit policies to `Success, Failure`.",
            "RiskType":"weak_password"
```

`}` `],`

```json
    "PageInfo":{
        "TotalCount":105,
        "PageSize":20,
        "CurrentPage":1,
        "Count":3,
        "LastRowKey":"null"
```

`}` `}` `XML` format

```xml
HTTP/1.1 200 OK Content-Type:application/xml <ListCheckItemWarningSummaryResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <List>
        <RiskType>weak_password</RiskType>
        <Alias>week_pa****</Alias>
        <CheckId>696</CheckId>
        <CheckItem>Configure the event audit policies</CheckItem>
        <CheckLevel>high</CheckLevel>
        <CheckType>Security audit</CheckType>
        <Advice>In the Administrative Tools window, double-click Local Security Policy. In the Local S
ecurity Policy window, go to Security Settings\\Local Policies\\Audit Policy and set all audit policies to `Success, Failure`.</Advice>
        <Description>Configure the event audit policies</Description>
        <Status>1</Status>
        <WarningMachineCount>20</WarningMachineCount>
        <ContainerCheckItem>true</ContainerCheckItem>
        <AffiliatedRiskTypes>
            <affiliatedRiskType>["CIS Compliance checks"]</affiliatedRiskType>
        </AffiliatedRiskTypes>
        <AffiliatedRisks>
            <affiliatedRisk>["CIS Ubuntu Linux 14 LTS Benchmark"]</affiliatedRisk>
        </AffiliatedRisks>
        <EnableRisks>
            <enableRisk>["CIS Ubuntu Linux 14 LTS Benchmark"]</enableRisk>
        </EnableRisks>
    </List>
    <PageInfo>
        <CurrentPage>1</CurrentPage>
        <LastRowKey>null</LastRowKey>
        <PageSize>20</PageSize>
        <TotalCount>105</TotalCount>
        <Count>3</Count>
    </PageInfo>
</ListCheckItemWarningSummaryResponse>
```

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | -101 | -101 | %s %s |

### 5.46 ModifyOperateVul

Call the ModifyOperateVul operation to manage detected vulnerabilities.

**Authorization information**

| Operation | Access level | Resource type |
|---|---|---|
| yundun-css:ModifyOperateVul | Write | acs:yundun-css:*:{#accountId}:* |

**Traffic shaping**

Throttling limit for a single user: 10 queries per second (QPS). Throttling limit for this operation: 100 QPS.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

**Request parameters**

| Paramete r | Type | Locatio n | Required | Example | Description |
|---|---|---|---|---|---|
| Info | String | Query | Yes | [{"name":"alilinux2:2.1903:A LINUX2-SA- 2022:0007","uuid":"a3bb82a 8-a3bd-4546-acce- 45ac34af****","tag":"oval","i sFront":0}, {"name":"alilinux2:2.1903:AL INUX2-SA- 2022:0007","uuid":"98a6fecc -88cd-46f2-8e35- f808a388****","tag":"oval","i sFront":0}] | The information about the vulnerabilities to manage. This parameter is a JSON string and contains the following fields: name: The name of the vulnerability. uuid: The universally unique identifier (UUID) of the server where the vulnerability exists. tag: The tag of the vulnerability. Valid values: oval : Linux software vulnerability system : Windows system vulnerability cms : Web-CMS vulnerability Note To obtain the tag values for other vulnerability types, call the DescribeVulList operation. isFront: Specifies whether the Windows patch is a prerequisite patch. This parameter is required only when you manage Windows system vulnerabilities. It can be ignored for other vulnerability types. Valid values: 0 : No 1 : Yes Note You can manage multiple vulnerabilities at a time. Separate the information for each vulnerability with a comma (,). To obtain vulnerability information, call the DescribeVulList operation. |

| Paramete r | Type | Locatio n | Required | Example | Description |
|---|---|---|---|---|---|
| OperateType | String | Query | Yes | vul fix _ | The management operation for the vulnerability. Valid values: vul fix: Fix the _ vulnerability. vul verify: Verify the _ vulnerability. vul ignore: Ignore the _ vulnerability. vul undo ignore: Cancel _ _ ignoring the vulnerability. vul delete: Delete the _ vulnerability. |
| Type | String | Query | Yes | cve | The type of the vulnerability to manage. Valid values: cve: Linux software vulnerability sys: Windows system vulnerability cms: Web-CMS vulnerability emg: Emergency vulnerability app: Application vulnerability sca: Software constituency parsing vulnerability Note The fix operation is not supported for emergency vulnerabilities (emg), application vulnerabilities (app), and software constituency parsing vulnerabilities (sca). |
| Reason | String | Query | No | not operate | The reason for managing the vulnerability. Note This parameter is required only when you set OperateType to vulignore. _ |
| From | String | Query | No | css | The source of the request. The value is fixed to css. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D-5EC1- 97C8-************ | The request ID is generated by Alibaba Cloud. You can use this ID to troubleshoot issues. |

**Examples**

Sample request

```
https://[Endpoint]/?Action=ModifyOperateVul&RegionId=cn-hangzhou&Info= [{"name":"alilinux2:2.1903:ALINUX2-SA-2022:0007","uuid":"a3bb82a8-a3bd-4546-acce- 45ac34af****","tag":"oval","isFront":0},{"name":"alilinux2:2.1903:ALINUX2-SA- 2022:0007","uuid":"98a6fecc-88cd-46f2-8e35f808a388****","tag":"oval","isFront":0}]&OperateType=vul_fix&Type=cve&Reason=not operate&From=css
```

Sample responses `JSON` format

```
HTTP/1.1 200 OK Content-Type:application/json
```

`{`

```json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************"
```

`}` `XML` format

```xml
HTTP/1.1 200 OK Content-Type:application/xml <ModifyOperateVulResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
</ModifyOperateVulResponse>
```

## 6 Error codes

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
| yd.error.all.ConsoleSystemError 1014 _ | The format of the specified parameter is invalid. | The error message returned because the format of the specified parameter is invalid. Check the parameter and try again. |
| yd.error.all.ConsoleNeedLogin | You are not logged on. | The error message returned because you are not authorized to perform the operation. Check the account permissions. |

| Alibaba Cloud Security-Server Gu ard Advanced Edition |   | Container Security Service Deve oper Guide·Error code |
|---|---|---|

| yd.error.all.InvalidApi | An operation exception occurred. | The error message returned because an operation exception occurred. Try again later. |
|---|---|---|
| yd.error.all.InvalidParameter | The parameter is invalid. | The error message returned because the specified parameter is invalid. Check the request parameter and try again. |
| yd.error.all.InvalidResult | The return value is invalid. | The error message returned because the return value is invalid. Try again later. |
| yd.error.all.PropertyConvertFailed | An error occurred during conversion. | The error message returned because property conversion failed. Try again later. |
| yd.error.all.NoPermission | Authorization required. | The error message returned because you are not authorized to perform the operation. Check the account permissions. |
| yd.error.all.ServerError | A server error occurred. | The error message returned because a server error occurred. Try again later or contact Alibaba Cloud technical support. |
| yd.error.all.UnkownError | An unknown error occurred. | The error message returned because an unknown error occurred. Try again later or contact Alibaba Cloud technical support. |

Table 2. Error codes specific to Threat Detection Service

| Error code | Error message | Description |
|---|---|---|
| yd.error.sas.1 | The specified field does not exist in the metadata. | The error message returned because the field you queried does not exist in the metadata. Check the request and try again. |
| yd.error.sas.2 | An error occurred while invoking the task engine. Try again. | The error message returned because the system failed to invoke the task engine. Try again later. |
| yd.error.sas.3 | An error occurred while starting the task. Try again. | The error message returned because the system failed to start the task. Try again later. |
| yd.error.sas.4 | An error occurred while stopping the task. Try again. | The error message returned because the system failed to stop the task. Try again later. |
| yd.error.sas.5 | An error occurred while restarting the task. Try again. | The error message returned because the system failed to restart the task. Try again later. |
| yd.error.sas.6 | An error occurred while obtaining the task status. Try again. | The error message returned because the system failed to obtain the task status. Try again later. |
| yd.error.sas.7 | An error occurred while deleting the task. Try again. | The error message returned because the system failed to delete the task. Try again later. |

| yd.error.sas.8 | The specified table does not contain metadata. | The error message returned because the table you queried does not contain metadata. Check the request and try again. |
|---|---|---|
| yd.error.sas.100 | Request failed. Refresh the page and try again. | The error message returned because the request failed. Try again later. |
| yd.error.sas.101 | The parameter is invalid. | The error message returned because the parameter is invalid. Check the parameter and try again. |
| yd.error.sas.103 | Request failed. | The error message returned because the request failed. Check the request and try again later. |
| yd.error.sas.400 | The asset is under protection. Uninstall the Server Guard agent and try again. | The error message returned because the asset that you want to delete is protected by the Server Guard agent. Uninstall the Server Guard agent from the server and try again. |
| yd.error.sas.500 | A system error occurred. | The error message returned because a system error occurred. Contact Alibaba Cloud technical support. |
| yd.error.sas.501 | The feature is not available in the current version. | The error message returned because the version you used does not support this feature. |
| yd.error.sas.502 | You are not authorized to access the server. | The error message returned because you are not authorized to manage the server. |

Table 3. Error codes specific to Anti-DDoS Service

| Error code | Error message | Description |
|---|---|---|
| yd.error.ddos.400 | An error occurred while accessing the server. Try again. | The error message returned because the system failed to access the server. Try again later. |
| yd.error.ddos.500 | An error occurred on the server. Contact technical support. | The error message returned because an error occurred on the server. Contact Alibaba Cloud technical support. |
| yd.error.ddos.UNKNOWN EXCEPTION _ | An unknown error occurred. | The error message returned because an unknown error occurred. Contact Alibaba Cloud technical support. |
| yd.error.ddos.REQUEST TIMEOUT _ | The request timed out. | The error message returned because the request timed out. Try again later. |
| yd.error.ddos.SERVER FAILED _ | The operation failed. | The error message returned because the operation failed. Contact Alibaba Cloud technical support. |
| yd.error.ddos.NOT AUTHORIZED _ | Authorization required. | The error message returned because you are not authorized to perform the operation. Check the account permissions. |
| yd.error.ddos.PARAMETER INVALID _ | The parameter is invalid or is not specified. | The error message returned because the specified request parameter is invalid. Check the parameter and try again. |

| yd.error.ddos.IP SEGMENT INVALID _ _ | The specified CIDR block is invalid. Check the parameter and enter another value. | The error message returned because the specified CIDR block is invalid. Check the CIDR block specified in the request parameter. |
|---|---|---|
| yd.error.ddos.IP SEGMENT REPEAT _ _ | One CIDR block cannot be used in different regions. Enter another CIDR block. | The error message returned because the specified CIDR block is invalid. Check the CIDR block specified in the request parameter. |
| yd.error.ddos.IP SEGMENT ALREADY _ _ | The specified CIDR block already exists. | The error message returned because the specified CIDR block is in use. Check the CIDR block specified in the request parameter. |
| yd.error.ddos.IP SEGMENT MASK LE _ _ _ NGTH ERR _ | The mask can contain a maximum of 24 bits. | The error message returned because the mask contains more than 24 bits. Check the mask of the CIDR block specified in the request parameter. |
| yd.error.ddos.QUERY REGION LIST E _ _ _ RR | An error occurred while obtaining the region list. | The error message returned because the system failed to obtain the region list. Try again later. |
| yd.error.ddos.IP SEGMENT OPERATIO _ _ N ERR _ | An error occurred while processing the CIDR block. | The error message returned because the system failed to process the CIDR block. Try again later. |
| yd.error.ddos.QUERY IP SEGMENT E _ _ _ RR | An error occurred while obtaining the CIDR block. | The error message returned because the system failed to obtain the CIDR block. Try again later. |
| yd.error.ddos.MODIFY IP SEGMENT E _ _ _ RR | An error occurred while modifying the CIDR block. | The error message returned because the system failed to modify the CIDR block. Try again later. |
| yd.error.ddos.IP SEGMENT TYPE ERR _ _ _ | Check whether the type of the CIDR block (internal or external) is specified. | The error message returned because the CIDR block type is not specified. Check the CIDR block type and try again. |
| yd.error.ddos.CANCEL FLOW CLEAN _ _ _ ERR | An error occurred while canceling traffic scrubbing. Check whether the network connection to Network Detection and Response is normal. | The error message returned because the system failed to cancel traffic scrubbing. Check the network connection to Network Detection and Response and try again. |
| yd.error.ddos.QUERY FLOW ANALYSI _ _ S ERR _ | An error occurred while obtaining the traffic analysis result. Check whether the network connection to Network Detection and Response is normal. | The error message returned because the system failed to obtain the traffic analysis result. Check the network connection to Network Detection and Response and try again. |
| yd.error.ddos.QUERY BEAVER URL E _ _ _ RR | An error occurred while obtaining the URL of Network Detection and Response. | The error message returned because the system failed to obtain the URL of Network Detection and Response. Check the network connection to Network Detection and Response and try again. |
| yd.error.ddos.SET VALVE INVALID _ _ | The threshold validation failed. Check the thresholds and enter correct values. | The error message returned because the threshold verification failed. Check the thresholds and try again. |
| yd.error.ddos.VALVE DEFAULT ALRE _ _ ADY | The specified request is invalid. You cannot add the default threshold. | The error message returned because the system failed to add the default threshold. The default threshold can only be modified. |

| yd.error.ddos.NOT BELONG BEAVER _ _ _ IP SEGMENT _ | Check whether the specified CIDR block belongs to the internal network of Network Detection and Response. | The error message returned because the CIDR block you entered does not belong to the internal network of Network Detection and Response. Check the CIDR block. |
|---|---|---|
| yd.error.ddos.VALVE DELETE ERR _ _ | The default threshold or the threshold configured for 128.0.XX.XX/XX cannot be deleted. | The error message returned because the system failed to delete the default threshold or the threshold configured for 128.0.XX.XX/XX. |
| yd.error.ddos.QUERY CODE ERR _ _ | An error occurred while obtaining the product configuration. | The error message returned because the system failed to obtain the product configuration. Try again later. |
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
| yd.error.code.-360108 | An error occurred while paging. |
| yd.error.code.-360109 | The service is not supported. |
| yd.error.code.-360110 | The format of the specified IP address is invalid. Enter another value. |
| yd.error.code.-360111 | The specified time is invalid. Enter another value. |
| yd.error.code.-360112 | A parsing error occurred. |
| yd.error.code.-360113 | The name of the firewall is invalid. Enter another value. |
| yd.error.code.-360114 | The specified network instance is invalid. Enter another value. |

| yd.error.code.-360115 | The specified VPC is invalid. Enter another value. |
|---|---|
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
|---|---|
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
|---|---|
| yd.error.code.-360178 | An unknown error occurred. |
| yd.error.code.-360179 | An error occurred while calling the operation. |
| yd.error.code.-360180 | The number of VPCs that are attached to the CEN instance is insufficient. |
| yd.error.code.-360181 | The firewall of the CEN instance is overwritten. You do not need to create a firewall. |
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

| yd.error.code.-360206 | The specified ECS instance does not exist. |
|---|---|
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
| yd.error.code.-360312 | An error occurred while querying the IP address pool. |
| yd.error.code.-360313 | An error occurred while updating the IP address pool. |
| yd.error.code.-360314 | An error occurred while updating the information about the VPC route. |
| yd.error.code.-360315 | An error occurred while updating the status of the VPC. |
| yd.error.code.-360316 | An error occurred while inserting the firewall ns. |
| yd.error.code.-360317 | An error occurred while updating the VLAN. |

| yd.error.code.-360318 | An error occurred while updating the endpoint information about the firewall. |
|---|---|
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
|---|---|
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
|---|---|
| yd.error.code.-200100 | The request method is invalid. |
| yd.error.code.-200101 | Authentication failed. |
| yd.error.code.-200102 | Invocation failed. |
| yd.error.code.-200103 | The parameter is invalid. Try again. |
| yd.error.code.-200104 | The specified UID is invalid.Try again. |
| yd.error.code.-200105 | An error occurred while paging. |
| yd.error.code.-200106 | The IP address in the address book is invalid. Check the parameter and enter another value. |
| yd.error.code.-200107 | The address book already exists. |
| yd.error.code.-200108 | An error occurred. Try again. |
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
|---|---|
| yd.error.code.-200130 | The number of address books exceeds the upper limit. |
| yd.error.code.-200200 | A backend error occurred. |
| yd.error.code.-200201 | A backend error occurred. |
| yd.error.code.-200202 | A backend error occurred. |
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

| yd.error.code.-230101 | Authentication failed. |
|---|---|
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
| yd.error.code.-230128 | The IP address in the rule is invalid. |
| yd.error.code.-230129 | The network type of the rule is invalid. Select another value. |
| yd.error.code.-230130 | An error occurred while managing the rule. |
| yd.error.code.-230131 | The policy cannot be submitted. |
| yd.error.code.-230150 | The policy group does not exist. Specify another value. |

| yd.error.code.-230151 | The number of policy groups exceeds the limit. |
|---|---|
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
| ErrorParametersDstIP.-210921 | invalid para dst ip (The value of the dstIP parameter is invalid.) | The error message returned because the value of the dstIP parameter is invalid. Specify a valid value. |
| ErrorParametersPort.-210208 | invalid port, must 0~65535 (The specified port number is invalid. The port number must range from 0 to 65535.) | The error message returned because the specified port number is invalid. Specify a port number ranging from 0 to 65535. |
| ErrorParametersLiveTime.-210922 | invalid para live time (The value of the liveTime parameter is invalid.) | The error message returned because the value of the liveTime parameter is invalid. Specify a valid value. |
| ErrorDBInsert.-210122 | internal error: sql insert (An internal error occurred while executing the INSERT statement.) | The error message returned because an internal error occurred while executing the INSERT statement. |
| ErrorInnerUuid.-210606 | internal error: uuid list is 0 (The internal error of empty UUID list occurred.) | The error message returned because the UUID list is empty. |
| ErrorDBSelect.-210124 | internal error: sql select (An internal error occurred while executing the SELECT statement.) | The error message returned because an internal error occurred while executing the SELECT statement. |
| ErrorParasAddressCidrFeild.-210915 | paras addressCidrList filed (Failed to reset the addressCidrList rule.) | The error message returned because the system failed to reset the addressCidrList rule. |

| ErrorPortAddressGroup.-210303 | get port in address group failed (Failed to obtain port information from the address group.) | The error message returned because the system failed to obtain port information from the address group. |
|---|---|---|
| ErrorPortAddressGroup.-210303 | get port in address group failed (Failed to obtain port information from the address group.) | The error message returned because the system failed to obtain port information from the address group. |
| ErrorSourceAddressGroup.-210304 | get source address in address group failed (Failed to obtain source addresses from the address group.) | The error message returned because the system failed to obtain source addresses from the address group. |
| ErrorSourceAddressRange.-210306 | source address range error, must be like \"192.168.XX.XX/192.168.XX.XX\" (The source address range is invalid. Example: \"192.168.XX.XX/192.168.XX.XX\") | The error message returned because the source address range is invalid. Specify the value in the \"192.168.XX.XX/192.168.XX.XX\" format. |
| ErrorDestAddressGroup.-210305 | get dest address in address group failed (Failed to obtain destination addresses from the address group.) | The error message returned because the system failed to obtain destination addresses from the address group. |
| ErrorNoBeaverRules.-210226 | no beaver rules for online (The specified Network Detection and Response rule does not exist.) | The error message returned because the specified Network Detection and Response rule does not exist. |
| ErrorDBUpdate.-210121 | internal error: sql update (An internal error occurred while executing the UPDATE statement.) | The error message returned because an internal error occurred while executing the UPDATE statement. |
| ErrorDBDelete.-210123 | internal error: sql delete (An internal error occurred while executing the DELETE statement.) | The error message returned because an internal error occurred while executing the DELETE statement. |
| ErrorMarshalJSON.-210125 | internal error: marshal json (An internal error occurred while marshaling JSON data.) | The error message returned because an internal error occurred while marshaling JSON data. |
