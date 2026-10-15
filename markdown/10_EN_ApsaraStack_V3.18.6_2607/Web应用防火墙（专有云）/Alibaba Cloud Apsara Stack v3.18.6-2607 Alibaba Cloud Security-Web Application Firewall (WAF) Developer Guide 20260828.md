---
title: "Alibaba Cloud Apsara Stack v3.18.6-2607 Alibaba Cloud Security-Web Application Firewall (WAF) Developer Guide 20260828"
product_version: "V3.18.6_2607"
doc_version: "20260828"
pdf_pages: 214
source_pdf: "0a06f421d337689a_Alibaba Cloud Apsara Stack v3.18.6-2607 Alibaba Cloud Security-Web Application Firewall (WAF) Develo"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/3816%202607/pdf%203/Web%E5%BA%94%E7%94%A8%E9%98%B2%E7%81%AB%E5%A2%99%EF%BC%88%E4%B8%93%E6%9C%89%E4%BA%91%EF%BC%89/Alibaba%20Cloud%20Apsara%20Stack%20v3.18.6-2607%20Alibaba%20Cloud%20Security-Web%20Application%20Firewall%20%28WAF%29%20Developer%20Guide%2020260828.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings)
---

# Alibaba Cloud Apsara Stack v3.18.6-2607 Alibaba Cloud Security-Web Application Firewall (WAF) Developer Guide 20260828

## Table of Contents

- 1 Preparations
  - 1.1 Log in to OpenAPI Explorer
  - 1.2 View the information about an operation
  - 1.3 Obtain an AccessKey pair
  - 1.4 Obtain access credentials assigned by STS
  - 1.5 Obtain an endpoint
- 2 Common parameters
- 3 Call examples
  - 3.1 Call examples for SDK for Java
    - 3.1.1 Use SDK
      - 3.1.1.1 Install SDK for Java
      - 3.1.1.2 Use CommonRequest to call API operations
  - 3.2 Call examples for SDK for Python
    - 3.2.1 Use SDK
      - 3.2.1.1 Install SDK for Python
      - 3.2.1.2 Use CommonRequest to call API operations
  - 3.3 Call examples for SDK for Go
    - 3.3.1 Use SDK
      - 3.3.1.1 Install the core package of SDK for Go
      - 3.3.1.2 Use CommonRequest to call API operations
- 4 Web Application Firewall
  - 4.1 Invocation method
    - 4.1.1 Request structure
    - 4.1.2 Request signatures
    - 4.1.3 Common parameters
    - 4.1.4 Response structure
  - 4.2 Website protection
    - 4.2.1 DescribeWebsite
    - 4.2.2 CreateWebsite
    - 4.2.3 EditWebsite
    - 4.2.4 ToggleWebsite
    - 4.2.5 QueryAsyncTaskStatus
    - 4.2.6 QueryAsyncTaskStatus
    - 4.2.7 UploadResponsePage
    - 4.2.8 DescribeInvalidWebsite
    - 4.2.9 DeleteInvalidWebsite
    - 4.2.10 DescribeInternetVip
    - 4.2.11 CreateInternetVip
    - 4.2.12 DeleteInternetVip
    - 4.2.13 DescribeVpc
    - 4.2.14 DescribeVSwitch
    - 4.2.15 DescribeVpcVip
    - 4.2.16 CreateVpcVip
    - 4.2.17 DeleteVpcVip
    - 4.2.18 DescribeEcs
    - 4.2.19 DescribeSlb
  - 4.3 HTTP flood protection rules
    - 4.3.1 DescribeCCRuleTemplate
    - 4.3.2 CreateCCRuleTemplate
    - 4.3.3 EditCCRuleTemplate
    - 4.3.4 ToggleCCRuleTemplate
    - 4.3.5 DeleteCCRuleTemplate
    - 4.3.6 ClearCCRestrictionList
    - 4.3.7 DescribeCCWhitelist
    - 4.3.8 CreateCCWhitelist
    - 4.3.9 DeleteCCWhitelist
  - 4.4 Custom rules
    - 4.4.1 DescribePolicyRule
    - 4.4.2 CreatePolicyRule
    - 4.4.3 EditPolicyRule
    - 4.4.4 TogglePolicyRule
    - 4.4.5 DeletePolicyRule
    - 4.4.6 EditPolicyRulePriority
    - 4.4.7 GenerateFalsePositiveRuleCorrection
    - 4.4.8 CreateDetectionModuleRule
    - 4.4.9 EditDetectionModuleRule
    - 4.4.10 EditPolicyRuleWebsiteBinding
    - 4.4.11 DeletePolicyRuleWebsiteBinding
  - 4.5 Protection policies
    - 4.5.1 DescribePolicyGroup
    - 4.5.2 CreatePolicyGroup
    - 4.5.3 EditPolicyGroup
    - 4.5.4 DeletePolicyGroup
  - 4.6 Protection logs
    - 4.6.1 QueryAsyncTaskStatus
    - 4.6.2 QueryAttackDetectionLog
    - 4.6.3 QueryAttackDetectionDetailLog
    - 4.6.4 QueryAuditLog
    - 4.6.5 QueryCCRuleExecutionLog
    - 4.6.6 QueryFullAccessLog
    - 4.6.7 QueryFullAccessDetailLog
    - 4.6.8 QueryPerformanceStatistics
  - 4.7 SSL certificate management
    - 4.7.1 DescribeSSLCert
    - 4.7.2 UploadSSLCert
    - 4.7.3 EditSSLCert
    - 4.7.4 DeleteSSLCert
  - 4.8 System information
    - 4.8.1 DescribeMetrics
    - 4.8.2 DescribeNodeStatus
    - 4.8.3 DescribeRealTimeAccess
    - 4.8.4 DescribeAttackDetectionAggregation
    - 4.8.5 DescribeAttackDetectionAggregationConfig
    - 4.8.6 ToggleAttackDetectionAggregation
- 5 Error codes

## 1 Preparations

### 1.1 Log in to OpenAPI Explorer

You can log in to OpenAPI Explorer from the Apsara Uni-manager Management Console.

**Prerequisites**

The URL of the Apsara Uni-manager Management Console is obtained from a deployment engineer. A browser is available. We recommend that you use Google Chrome.

**Procedure**

1. Enter the URL of the Apsara Uni-manager Management Console in the address bar of your
browser and press the Enter key.
2. On the login page, enter your username and password.
You need to obtain the username and password from an operations administrator.

**Note**

The first time you log in to the Apsara Uni-manager Management Console, you must change the password of your account as prompted. For security purposes, your password must be 10 to 32 characters in length and must contain at least two of the following character types: Letters Digits Special characters, including exclamation points (!), at signs (@), number signs (#), dollar signs ($), and percent signs (%)
3. Click **Log In**.
4. If multi-factor authentication (MFA) is enabled for your account, perform the following
operations based on the login scenario: Scenario 1: You log in to the Apsara Uni-manager Management Console for the first time after MFA is enabled by the administrator. a. On the Bind Virtual MFA Device page, bind an MFA device as prompted. b. Re-enter the username and password as described in Step 2 and click **Log In**. c. Enter the six-digit MFA verification code and click **Authenticate**. Scenario 2: You log in to the Apsara Uni-manager Management Console after MFA is enabled and an MFA device is bound. Enter the six-digit MFA verification code and click **Authenticate**.

**Note**

For more information, see **Bind a virtual MFA device to enable MFA** in **Apsara**
**Uni-manager Management Console User Guide**.
5. In the top navigation bar, choose **Products > Development Tools > OpenAPI Explorer**.

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

**Warning**

The AccessKey pair of a personal account is managed by the permission system of the Apsara Uni-manager Management Console. The AccessKey pair of an organization has more permissions than the AccessKey pair of a personal account. If you want to obtain the AccessKey pair of an organization, make sure that you are authorized by an administrator. This helps ensure security.

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

**Note**

An AccessKey pair consists of an AccessKey ID and an AccessKey secret. These credentials provide full permissions on cloud resources within your account. You must keep the AccessKey pair confidential.

**Obtain the AccessKey pair of an organization**

To obtain the AccessKey pair of an organization, perform the following operations:
1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, click **Enterprise**.
3. In the left-side navigation pane, choose **Resources > Organizations**.
4. In the organization list, click the name of the level-1 organization whose AccessKey pair you
want to obtain.
5. Click **Management Accesskey**.
6. In the dialog box that appears, view the AccessKey pair of the organization.

### 1.4 Obtain access credentials assigned by STS

**assigned by STS**

This topic describes how to use Security Token Service (STS) to call API operations in Apsara Stack.

**Background information**

Apsara Stack STS allows you to manage temporary credentials for your Apsara Stack resources. You can use STS to call API operations in Apsara Stack. Access credentials assigned by STS consist of an AccessKey ID, an AccessKey secret, and a security token. When you use STS to call API operations, you must use the access credentials assigned by STS.

**Procedure**

1. Obtain the Alibaba Cloud Resource Name (ARN) of your `Resource Access Management (RAM)`
`role` . i. Log on to the Apsara Uni-manager Management Console. ii. Click the profile picture in the upper-right corner of the page and click **User**
**Information**.
iii. Click **View Current Role Policy**. In the **View Policies of Current Role** dialog box, view the ARN of your `RAM role` .
2. Obtain the access credentials assigned by STS.

**Note**

You must replace the variables in the following code with actual values. Delete the angle brackets (<>) before you submit the code. Variables: <yourRegionID>: Replace it with the actual region ID. <yourAccessKeyID>: Replace it with your AccessKey ID. <yourAccessKeySecret>: Replace it with your AccessKey secret. <yourRoleSessionName>: Replace it with the current session name. In most cases, this variable is set to the identity of the user who makes API calls. Example: username. You can identify the users who assume the same RAM role to perform operations based on the value of the `RoleSessionName` variable. This way, you can perform user-specific auditing. The value is 2 to 64 characters in length and can contain letters, digits, periods (.), at signs (@), hyphens (-), and underscores (_). <yourRoleArn>: Replace it with the ARN of your RAM role. "sts.aliyuns.com": Replace it with the actual endpoint of STS.

```xml
public static void main(String[] args) {
    // Create a DefaultAcsClient instance and initialize the instance.
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
e that is obtained in the preceding step.
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
3. Use the access credentials assigned by STS to call an operation of a service. The following
sample code provides an example on how to use the access credentials assigned by STS to call the ECS `DescribeZones` operation:

**Note**

You must replace the variables in the following code with actual values. Delete the angle brackets (<>) before you submit the code. Variables: <yourRegionID>: Replace it with the actual region ID. <yourStsAccesskeyID>: Replace it with your AccessKey ID. <yourStsAccessKeySecret>: Replace it with your AccessKey secret. <yourStsToken>: Replace it with your security token. <yourResourceGroupID>: Replace it with the actual resource set ID. <yourOrganizationID>: Replace it with the actual organization ID.

```java
public static void main(String[] args) {
    // Replace "<yourRegionID>" with the actual region ID.
    // Replace "<yourStsAccessKeyID>" and "<yourStsAccessKeySecret>" with the AccessK
ey ID and AccessKey secret assigned by STS. The AccessKey ID and AccessKey secret are obtained in the preceding step.
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
    // Replace "<yourStsToken>" with the STS token assigned by STS. The STS token is
obtained in the preceding step.
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

If you want to call API operations in Apsara Stack by using the POP gateway, you must specify the endpoint of the corresponding cloud service. You can obtain an endpoint from onsite Apsara Stack O&M engineers. This topic describes how to obtain an endpoint.

**Procedure**

1. Log on to the Apsara Infrastructure Management console.
1.
2. In the left-side navigation pane, click **Product & Cluster O&M**.
3. In the **Product | Cluster** search box, enter **yundun-advance**. Find the cluster whose
name contains **BasicThinCluster** and click **Cluster Details** in the Actions column.
4. On the **Desired State Configuration** tab, search for the **kv.conf** file and open the file. In
the file, find the **region** and **internet-domain** parameters.
5. Obtain the value of the **EndpointPre** parameter. For more information, see Common
parameters.
6. Obtain the endpoint based on the **region**, **internet-domain**, and **EndpointPre**
parameters. The endpoint of a cloud service is in the following format:

```
${EndpointPre}.${global:region}.${global:internet-domain}
```

**What to do next**

If you want to call the API operations of Apsara Stack Security services from the service domain or O&M domain, you must configure the hosts file on your computer.
1. Obtain the virtual IP address (VIP) of the POP.
i. Click **Back to Old Version** to switch to Apsara Infrastructure Management of the previous version. In the top navigation bar, choose **Operations > Cluster Operations**. ii. Enter **webappAll** in the **Project** search box and **StandardCloudCluster** in the **Cluster** search box. Click the name of the first **StandardCloudCluster** cluster. iii. In the **Cluster Resource** section, find the O&M domain, management domain, and service domain. Click the icon to the right of **Type**, select **Contains** from the dropdown list, and then enter `vip` in the Filter field.

**Note**

The following section describes the cluster resources of the preceding domains: O&M domain: The value of the **Name** parameter of the cluster resource is
**pop-vip-ops**.
Management domain: The value of the **Name** parameter of the cluster resource is **pop-vip-mgmt**. Service domain: The value of the **Name** parameter of the cluster resource is
**pop-vip-biz**.
iv. Right-click the value of the **Result** parameter of the O&M domain, management domain, or service domain. Click **Show More** and view the value of the **vip_ip** parameter in the Details dialog box.
2. Configure the following hosts file on your computer.

```xml
<vip_ip> <Endpoint of the API that you want to request>
```

eters

## 2 Common parameters

**Common request parameters**

Common request parameters must be included in all Apsara Stack Security API requests. Table 1. Table of common request parameters

| Parameter | Type | Requi red | Description |
|---|---|---|---|
| Format | Strin g | No | The format in which to return the response. Set the value to JSON. |
| Version | Strin g | Yes | The version number of the API. Specify the version number in the YYYY-MM-DD format. Valid values: If you call the API operations of the cloud service whose service code is Auditprivate, set the value to 2018-01-16. If you call the API operations of the cloud service whose service code is yundunnextsoc, set the value to 2019-07-23. If you call the API operations of the cloud service whose service code is Sas, set the value to 2018-12-03. If you call the API operations of the cloud service whose service code is aegis, set the value to 2016-11-11. If you call the API operations of the cloud service whose service code is yundun-css, set the value to 2021-10-11. If you call the API operations of the cloud service whose service code is secspy, set the value to 2019-08-05. If you call the API operations of the cloud service whose service code is Ddosprivate, set the value to 2018-01-16. If you call the API operations of the cloud service whose service code is hsm-private, set the value to 2018-06-30. If you call the API operations of the cloud service whose service code is Cloudfw, set the value to 2017-12-07. If you call the API operations of the cloud service whose service code is Sddp, set the value to 2019-01-03. If you call the API operations of the cloud service whose service code is semawaf, set the value to 2020-07-01. If you call the API operations of the cloud service whose service code is soar, set the value to 2018-12-03. |
| AccessKeyId | Strin g | Yes | The AccessKey ID provided to you by Apsara Stack. |
| AccessKeySe cret | Strin g | Yes | The AccessKey secret provided to you by Apsara Stack. |
| RegionId | Strin g | Yes | The region ID of the service. |

eters

| Product | Strin g | Yes | The name of the service to which the API operation belongs. Valid values: Auditprivate: basic components of Apsara Stack Security yundunnextsoc: Security Operations Center (SOC) Sas: Threat Detection Service aegis: Server Guard yundun-css: Container Production secspy: Network Detection and Response Ddosprivate: Anti-DDoS Service hsm-private: Data Encryption Service Cloudfw: Cloud Firewall Sddp: Sensitive Data Discovery and Protection (SDDP) semawaf: Web Application Firewall (WAF) soar: Security Orchestration and Automation Response (SOAR) |
|---|---|---|---|
| EndpointPre | Strin g | Yes | The prefix in the endpoint of the service to which the API operation belongs. Valid values: auditprivate: the prefix in the endpoint of basic components of Apsara Stack Security yundunnextsoc-pop: the prefix in the endpoint of SOC tds: the prefix in the endpoint of Threat Detection Service aegis: the prefix in the endpoint of Server Guard yundun-css: the prefix in the endpoint of Container Protection secspy-share: the prefix in the endpoint of Network Detection and Response ddosprivate: the prefix in the endpoint of Anti-DDoS Service hsmprivate: the prefix in the endpoint of Data Encryption Service cloudfw: the prefix in the endpoint of Cloud Firewall sddp-api: the prefix in the endpoint of SDDP semawaf: the prefix in the endpoint of WAF soar: the prefix in the endpoint of SOAR |

**Common response parameters**

API responses use the HTTP response format: A 2xx status code indicates a successful call. A 4xx or 5xx status code indicates a failed call. Responses are returned in the JSON format. Every response returns a unique RequestID regardless of whether the call is successful.

## 3 Call examples

### 3.1 Call examples for SDK for Java

#### 3.1.1 Use SDK

##### 3.1.1.1 Install SDK for Java

This topic describes how to install and use Apsara Stack Security SDK for Java. Apsara Stack SDK for Java supports Java Development Kit (JDK) 1.8 or later. You can install Apsara Stack SDK for Java by adding Maven dependencies or downloading the SDK. For more information, visit Alibaba Cloud SDKs. If you want to use Apsara Stack Security SDK for Java, you must install the core library of Apsara Stack SDK for Java. We recommend that you use V4.5.17 or later of the core library. When you install the core library, you must add the following dependency to the pom.xml file. For more information about the specific SDK version, visit Alibaba Cloud SDKs.

```xml
<!-- Alibaba Cloud SDK for Java --> <dependency>
    <groupId>com.aliyun</groupId>
    <artifactId>aliyun-java-sdk-core</artifactId>
    <version>4.5.17</version>
</dependency>
```

##### 3.1.1.2 Use CommonRequest to call API operations

**Note**

If you want to call the API operations of a service that does not provide SDKs, you can use CommonRequest. You can use CommonRequest to call API operations.

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

The following sample code shows how to use CommonRequest to call an API operation of Apsara Stack Security:

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

### 3.2 Call examples for SDK for Python

**Python**

#### 3.2.1 Use SDK

##### 3.2.1.1 Install SDK for Python

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

##### 3.2.1.2 Use CommonRequest to call API operations

**Note**

If you want to call the API operations of an Apsara Stack service that does not provide SDKs, you can use CommonRequest. You can use CommonRequest to call API operations.

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

The following sample code shows how to use the CommonRequest method to call the API operation:

```bash
from aliyunsdkcore.client import AcsClient from aliyunsdkcore.request import CommonRequest client = AcsClient('{your_access_key_id}', '{your_access_key_secret}', '{your_region_id}') request = CommonRequest() request.set_domain('<your-endpoint>') //The endpoint of the service. request.set_version('<API-version>') //The version of the API. request.set_action_name('<your-action>')//The name of the API operation.
# or:
# request = CommonRequest(domain='<your-endpoint>', version='<API-version>',
action_name='your-action') request.add_query_param('PageNumber', '1') request.add_query_param('PageSize', '30') response = client.do_action_with_exception(request)
```

### 3.3 Call examples for SDK for Go

#### 3.3.1 Use SDK

##### 3.3.1.1 Install the core package of SDK for Go

This topic describes how to install the core package of SDK for Go. Apsara Stack SDK for Go supports Go 1.10.x and later. You can run the following command to install the core package:

```
go get -u github.com/aliyun/alibaba-cloud-sdk-go/sdk
```

##### 3.3.1.2 Use CommonRequest to call API operations

**Note**

If you want to call the API operations of an Apsara Stack service that does not provide SDKs, you can use CommonRequest. You can use CommonRequest to call API operations.

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

The following sample code shows how to use the CommonRequest method to call the API operation:

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

`}`

## 4 Web Application Firewall

### 4.1 Invocation method

#### 4.1.1 Request structure

Apsara Stack Security API operations use the RPC protocol. This topic describes the structure of API requests. You can call Apsara Stack Security API operations by sending HTTP requests. The request syntax is as follows:

```
http://endpoint/?Action=xx&parameters
```

where:

|   | endpoint |   | : The endpoin |
|---|---|---|---|
| [RegionId].example.com |   |   |   |
|   | Action | : the name of t |   |

`endpoint` : The endpoint of the Web Application Firewall (WAF) API is `semawaf.` `Action` : the name of the operation being performed. For example, to query the Apsara Stack Security features that are deployed, you must set the Action parameter to DescribeFeatures. `parameters` : the request parameters for the operation. Separate multiple parameters with ampersands (&). Request parameters include both common parameters and operationspecific parameters. Common parameters include information such as the API version number and authentication information. For more information about operation-specific parameters, see the corresponding operation description. The following example demonstrates how to call the DescribeFeatures operation to query the Apsara Stack Security features that are deployed:

```
https://yundunprivate.[RegionId].example.com/?Action=DescribeFeatures&AccessKeyId=key-t est&Format=JSON&SecureTransport=true&SignatureMethod=HMAC- SHA1&SignatureNonce=15215528852396&SignatureVersion=1.0&SourceIp=1xxxx6&Timestamp=2018- 03-02Txxxxxxx&Version=2018-01-16&Signature=xxxx%xxxx%3D
```

API requests are presented in the following easy-to-read format in this document:

```
https://yundunprivate.[RegionId].example.com/?Action=DescribeFeatures &Format=JSON &Version=2020-07-01 &Signature=xxxx%xxxx%3D &SignatureMethod=HMAC-SHA1 &SignatureNonce=15215528852396 &SignatureVersion=1.0 &AccessKeyId=key-test &Timestamp=2012-06-01T12:00:00Z
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

**Note**

The request parameters include operation-specific parameters and all common request parameters except Signature. i. Sort the request parameters. Sort the request parameters in alphabetical order. ii. Encode the parameters. Encode the canonicalized query string in UTF-8 based on the following rules: Uppercase letters, lowercase letters, digits, and some special characters such as hyphens (-), underscores (_), periods (.), and tildes (~) do not need to be encoded. Other characters must be percent encoded in the %XY format. XY represents the ASCII code of the characters in hexadecimal notation. For example, double quotation marks (") are encoded as %22. Extended UTF-8 characters are encoded in the %XY%ZA… format. Spaces must be encoded as %20. Do not encode spaces as plus signs (+). iii. Connect the encoded parameter names and values by using equal signs (=). iv. Sort the pairs of parameter names and values that are connected by using equal signs (=) in alphabetical order. Connect the pairs with ampersands (&) to create a canonicalized query string.
2. Create a string-to-sign from the encoded canonicalized query string based on the following
rule:

```
StringToSign=HTTPMethod + "&" + percentEncode("/") + "&" + percentEncode(CanonicalizedQueryString)
```

3. Calculate the HMAC value of the string-to-sign based on the HMAC definition in RFC 2104.

**Note**

Your AccessKey secret in combination with an ampersand (&) (ASCII:38) is used as the key for the HMAC calculation. The SHA1 algorithm is used to calculate the HMAC value of the string-to-sign.
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
| Version | String | Yes | The version number of the API. The value is in the format of YYYY-MM-DD. Set the value to 2018-01-16. |
| AccessKeyId | String | Yes | The AccessKey ID provided to you by Alibaba Cloud. |
| Signature | String | Yes | The signature string of the current request. |
| SignatureMethod | String | Yes | The encryption method of the signature string. Set the value to HMAC-SHA1. |
| Timestamp | String | Yes | The timestamp of the request. Specify the time in the ISO 8601 standard in the YYYY-MM-DDThh:mm:ssZ format. The time must be in UTC. For example, 2014-05-26T12:00:00Z indicates 20:00:00 on May 26, 2014 (UTC+8). |
| SignatureVersion | String | Yes | The version of the signature encryption algorithm. Set the value to 1.0. |

| SignatureNonce | String | Yes | A unique, random number used to prevent replay attacks. You must use different numbers for different requests. |
|---|---|---|---|
| ResourceOwnerA ccount | String | No | The owner account (the logon username) of the resource you want to access by using this API request. |
| Format | String | No | The format of the response. Valid values: JSON and XML. Default value: XML. |

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

`{`

```json
"RequestId": "4C467B38-3910-447D-87BC-AC049166F216", /* Returned data */
```

`}`

### 4.2 Website protection

#### 4.2.1 DescribeWebsite

Queries the information about the websites that are protected by WAF.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeWebsite | The operation that you want to perform. Set the value to DescribeWebsite. |

| RegionId | String | Yes | cn-hangzhou | The ID of the region. |
|---|---|---|---|---|
| Id | Integer | No | 1 | The ID of the website. |
| PageSize | Integer | No | 20 | The number of entries to return on each page. Default value: 10. |
| PageNumber | Integer | No | 1 | The number of the page to return. Default value: 1. |
| IsVpcWebsite | Boolean | No | true | Specifies whether the websites to query are in a virtual private cloud (VPC). Default value: false. Valid values: true false |
| WebsiteNameF ilter | RepeatL ist | No | ["website-1", "website-2"] | The name of the website to query. You can enter multiple names. |
| ServerNameFil ter | RepeatL ist | No | ["www.taobao.c om", "www.aliyun.co m"] | The domain name of the website to query. You can enter multiple domain names. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 53e59af3-3209-452a-853c-ac10ad815929 | The ID of the request. |

| Result | String | {"items": [{"id": 1, "ip": ["0.0.XX.XX"], "session method": {"type": "off"}, _ "policy rules": [], "health check status": _ _ _ "", "backend config": {"type": "proxy", _ "load balance policy": "Round Robin", _ _ "servers": [{"protocol": "http", "attr": "slb", "host": "192.168.XX.XX", "port": 80, "weight": 1}], "x forwarded for action": _ _ _ "append", "header config": [], _ "health check config": {"is enabled": _ _ _ false, "check http expect alive": _ _ _ ["http 2xx", "http 3xx"], "check type": _ _ _ "http", "interval": 30000, "fall": 5, "rise": 2, "timeout": 1000, "port": null, "host": "", "method": "GET", "path": "/"}, "proxy ssl protocols": [], _ _ "proxy ssl ciphers": ""}, "vpc": "vpc- _ _ tx9isq1jrry8k3h9q****", "vpc name": _ "tongquesingle****", "vip": ["42.36.XX.XX"], "ports": [{"port": 80, "ssl": false, "http2": false}], "is vpc website": false, "operation mode": _ _ _ "Software Reverse Proxy", "interface": "virtual", "server names": _ ["www.taobao.com"], "ssl protocols": [], _ "ssl ciphers": "", "name": _ "www.taobao.com", "create time": _ "1594371049", "last update time": _ _ "1594374794", "is enabled": false, _ "detector ip source": ["Socket"], _ _ "proxy ip list": [], "proxy ip groups": [], _ _ _ _ "access log": {"is enabled": true, _ _ "log request header": false, _ _ "log response header": false, _ _ "log request body": false, "log payload": _ _ _ false, "log dest ip": true, _ _ "is enable full access log": false, _ _ _ _ "log src port": true, "log event id": true, _ _ _ _ "log proxy name": true}, _ _ "proxy bind config": {"enable": false, _ _ "hash select ip method": _ _ _ "remote addr and port", _ _ _ "proxy bind ip list": null}, "remark": "", _ _ _ "ssl cert": null, "policy group": 6}], _ _ "total": 1} | The information about the websites. |
|---|---|---|---|

**Examples**

Sample requests

```
https://semawaf.[ RegionId].aliyuncs.com/?Action=DescribeWebsite &RegionId=cn-hangzhou &Id=1 &PageSize=20 &PageNumber=1 &IsVpcWebsite=true &WebsiteNameFilter.1=website-1 &ServerNameFilter.1=www.taobao.com
```

Sample success responses `XML` format

```json
<DescribeWebsiteResponse>
    <RequestId>53e59af3-3209-452a-853c-ac10ad815929</RequestId>
    <Result>{"items": [{"id": 1, "ip": ["0.0.XX.XX"], "session_method": {"type": "off"}
, "policy_rules": [], "health_check_status": "", "backend_config": {"type": "proxy", "l oad_balance_policy": "Round Robin", "servers": [{"protocol": "http", "attr": "slb", "ho st": "192.168.XX.XX", "port": 80, "weight": 1}], "x_forwarded_for_action": "append", "h eader_config": [], "health_check_config": {"is_enabled": false, "check_http_expect_alive": ["http_2xx", "http_3xx"], "check_type": "http", "interval": 30000, "fall": 5, "rise": 2, "timeout": 1000, "port": null, "host": "", "method": "GET" , "path": "/"}, "proxy_ssl_protocols": [], "proxy_ssl_ciphers": ""}, "vpc": "vpc-tx9isq 1jrry8k3h9q****", "vpc_name": "tongquesingletunnel", "vip": ["42.36.XX.XX"], "ports": [ {"port": 80, "ssl": false, "http2": false}], "is_vpc_website": false, "operation_mode": "Software Reverse Proxy", "interface": "virtual", "server_names": ["www.taobao.com"], " ssl_protocols": [], "ssl_ciphers": "", "name": "www.taobao.com", "create_time": "159437 1049", "last_update_time": "1594374794", "is_enabled": false, "detector_ip_source": ["S ocket"], "proxy_ip_list": [], "proxy_ip_groups": [], "access_log": {"is_enabled": true, "log_request_header": false, "log_response_header": false, "log_request_body": false, " log_payload": false, "log_dest_ip": true, "is_enable_full_access_log": false, "log_src_ port": true, "log_event_id": true, "log_proxy_name": true}, "proxy_bind_config": {"enab le": false, "hash_select_ip_method": "remote_addr_and_port", "proxy_bind_ip_list": null }, "remark": "", "ssl_cert": null, "policy_group": 6}], "total": 1}</Result> </DescribeWebsiteResponse>
```

`JSON` format `{`

```json
  "RequestId":"53e59af3-3209-452a-853c-ac10ad815929",
  "Result":"{\"items\": [{\"id\": 1, \"ip\": [\"0.0.XX.XX\"], \"session_method\": {\"ty
pe\": \"off\"}, \"policy_rules\": [], \"health_check_status\": \"\", \"backend_config\": {\"type\": \"proxy\", \"load_balance_policy\": \"Round Robin\", \"s ervers\": [{\"protocol\": \"http\", \"attr\": \"slb\", \"host\": \"192.168.XX.XX\", \"p ort\": 80, \"weight\": 1}], \"x_forwarded_for_action\": \"append\", \"header_config\": [], \"health_check_config\": {\"is_enabled\": false, \"check_http_expect_alive\": [\"ht tp_2xx\", \"http_3xx\"], \"check_type\": \"http\", \"interval\": 30000, \"fall\": 5, \" rise\": 2, \"timeout\": 1000, \"port\": null, \"host\": \"\", \"method\": \"GET\", \"pa th\": \"/\"}, \"proxy_ssl_protocols\": [], \"proxy_ssl_ciphers\": \"\"}, \"vpc\": \"vpc -tx9isq1jrry8k3h9q****\", \"vpc_name\": \"tongquesingletunnel\", \"vip\": [\"42.36.XX.XX\"], \"ports\": [{\"port\": 80, \"ssl\": false, \"http2\": false}], \"is_ vpc_website\": false, \"operation_mode\": \"Software Reverse Proxy\", \"interface\": \" virtual\", \"server_names\": [\"www.taobao.com\"], \"ssl_protocols\": [], \"ssl_ciphers\": \"\", \"name\": \"www.taobao.com\", \"create_time\": \"1594371049\", \ "last_update_time\": \"1594374794\", \"is_enabled\": false, \"detector_ip_source\": [\" Socket\"], \"proxy_ip_list\": [], \"proxy_ip_groups\": [], \"access_log\": {\"is_enabled\": true, \"log_request_header\": false, \"log_response_header\": false, \ "log_request_body\": false, \"log_payload\": false, \"log_dest_ip\": true, \"is_enable_ full_access_log\": false, \"log_src_port\": true, \"log_event_id\": true, \"log_proxy_name\": true}, \"proxy_bind_config\": {\"enable\": false, \"hash_select_ip_method\": \"remote_addr_and_port\", \"proxy_bind_ip_list\": null}, \"r emark\": \"\", \"ssl_cert\": null, \"policy_group\": 6}], \"total\": 1}"
```

`}`

**Error codes**

For a list of error codes, see Error codes.

#### 4.2.2 CreateWebsite

Adds a website.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateWebsite | The operation that you want to perform. Set the value to CreateWebsite. |
| RegionId | String | Yes | cn-hangzhou |   |
| Name | String | Yes | test-website-1 | The website name. |
| ServerNameLis t | RepeatL ist | Yes | ["www.aliyundoc .com", "www.example.c om"] | The domain name of the website. You can enter multiple domain names. |
| PortList | RepeatL ist | Yes | [{"port":80,"ssl": false,"http2":fals e}, {"port":443,"ssl" :true,"http2":tru e}] | The port information about the website. Set this parameter to a string that consists of JSON arrays. The value is a string that consists of a JSON struct. The JSON struct contains the following fields: port: the port number of the website. This field is required. Data type: integer. Valid values: 1 to 65535. ssl: specifies whether to enable an SSL certificate. This field is required. Data type: Boolean. http2: specifies whether to enable HTTP/2. This field is required. Data type: Boolean. |
| SSLCertId | Integer | No | 3 | The ID of the SSL certificate. If ssl of a port specified in PortList is set to true, this field is required. You can call the DescribeSSLCert operation to query the ID of the SSL certificate. |
|   |   |   |   | The configurations of the website. The value is a string that consists of a JSON struct. The JSON struct contains the following fields: type: the method to respond to requests. This field is required. Data type: string. Valid values: proxy: forwards requests to the backend server. redirect: redirects requests. |

| ation Firewall (WAF | ) |   |   | n Firewal |
|---|---|---|---|---|
| BackendConfig | Json | Yes | {"type": "proxy", "servers": [{"host": "192.168.XX.XX" , "port": 80, "protocol": "http", "attr": "ecs", "weight": 1}], "load balance p _ _ olicy": "Round Robin", "x forwarded fo _ _ r action": _ "append", "header config": _ []} | response: returns specific content. servers: the information about the backend server. Set this parameter to a string that consists of JSON arrays. The value is a string that consists of a JSON struct. The JSON struct contains the following fields: path: the destination address for redirection. Data type: string. If type in BackendConfig is set to redirect or response, this field is required. status code: the status code in _ the responses. Data type: integer. If type in BackendConfig is set to redirect or response, this field is required. host: the IP address of the backend server. This field is required. Data type: string. If the backend server is an Elastic Compute Service (ECS) or Server Load Balancer (SLB) instance, you can call the DescribeEcs or DescribeSlb operation to query the values of the host field of backend servers. port: the port number of the backend server. This field is required. Data type: integer. Valid values: 1 to 65535. protocol: the protocol of the backend server. This field is required. Data type: string. Valid values: http and https. attr: the type of the backend server. This field is required. Data type: string. If you do not need to forward requests destined for the website to a specific backend server, set the value to normal. If you need to forward requests destined for the website to a specific backend server, set the value to ecs or slb. weight: the weight of the backend server. This field is required. Data type: integer. Valid values: positive numbers. load balance policy: the _ _ scheduling algorithm. This field is required. Data type: string. Valid values: Round Robin: weighted round- robin |

|   |   |   |   | Least Connected: least connection scheduling IP Hash: source IP hash x forwarded for action: the _ _ _ action on the X-Forwarded-For field in the HTTP request header. To identify the actual IP addresses of the clients that access your website by using HTTP proxies or load balancing servers, you can specify this field. This field is required. Data type: string. Valid values: append: appends the last-hop IP address to the X-Forwarded- For field. cover: overwrites the original value of the X-Forwarded-For field with the last-hop IP address. no action: retains the original _ value of the X-Forwarded-For field. header config: the HTTP header _ configurations. This field is required. Data type: list. If you do not need to configure the HTTP header, set the field to an empty array. Set this parameter to a string that consists of JSON arrays. The value is a string that consists of a JSON struct. The JSON struct contains the following fields: name: the name of the HTTP header. This field is required. Data type: string. context: the type of the HTTP header. This field is required. Data type: string. Valid values: request and response. action: the action on the HTTP header. This field is required. Data type: string. Valid values: set and hide. name: the value of the HTTP header. This field is required. Data type: string. |
|---|---|---|---|---|
| PolicyGroupId | Integer | No | 6 | The ID of the protection policy. If type in BackendConfig is set to proxy, this field is required. You can call the DescribePolicyRule operation to query the IDs of protection policies. |

| SessionMetho d | Json | Yes | {"param":"userI d","type":"url qu _ ery"} | The method to identify users. The value is a string that consists of a JSON struct. The JSON struct contains the following fields: param: the ID of the user. type: the method to identify users. This field is required. Data type: string. Valid values: off: does not identify users. custom: identifies users based on their IDs that are extracted from requests. cookie: identifies users based on the Cookie field. url query: identifies users _ based on the GET parameters. body form: identifies users _ based on the POST parameters. header: identifies users based on the HTTP header. internal session: identifies _ users based on their systems. |
|---|---|---|---|---|
| Remark | String | No | Test site-1 | The remarks. |
| Vpc | String | No | vpc- RSABVqbNiS**** | The ID of the virtual private cloud (VPC). You can call the DescribeVpc operation to query the IDs of VPCs. |
| VpcName | String | No | csw | The name of the VPC. You can call the DescribeVpc operation to query the names of VPCs. |
| IsVpcWebsite | Boolean | No | true | Specifies whether the website is in a VPC. Default value: false. Valid values: true false |
| VipList | RepeatL ist | Yes | ["192.168.XX.XX ", "192.168.XX.XX" ] | The virtual IP address (VIP). You can enter multiple VIPs. You can call the DescribeInternetVip operation to query the VIPs on the Internet and the DescribeVpcVip operation to query the VIPs in VPCs. |
| IpSourceMetho d | RepeatL ist | No | ["Socket"] | The method to obtain the actual IP address. You can enter multiple methods. To obtain the actual IP address from a field in the HTTP request header, set the value to XYZ/X-Forwarded-For:-n. To obtain the socket information about the last nth proxy from X-Forwarded-For, append Socket to the end of the parameter value. |

| AccessLogConf ig | Json | No | {"is enabled": _ true, "log request he _ _ ader": false, "log response h _ _ eader": false, "log request bo _ _ dy": false, "log payload": _ false, "log dest ip": _ _ true, "is enable full a _ _ _ ccess log": _ false, "log src port": _ _ true, "log event id": _ _ true, "log proxy nam _ _ e": true} | The configurations for access logs. The value is a string that consists of a JSON struct. The JSON struct contains the following fields: is enabled: specifies whether to _ record HTTP access logs. This parameter is required. Data type: Boolean. log request header: specifies _ _ whether to record the HTTP request header. This parameter is required. Data type: Boolean. log response header: specifies _ _ whether to record the HTTP response header. This parameter is required. Data type: Boolean. log request body: specifies _ _ whether to record the HTTP request body. This parameter is required. Data type: Boolean. The maximum size of the HTTP request body that can be logged is 4 KB. log payload: specifies whether to _ record the payload. This parameter is required. Data type: Boolean. log dest ip: specifies whether to _ _ record the destination IP address. This parameter is required. Data type: Boolean. is enable full access log: _ _ _ _ specifies whether to record the full access logs. This parameter is required. Data type: Boolean. log src port: specifies whether to _ _ record the source port. This parameter is required. Data type: Boolean. log event id: specifies whether _ _ to record the ID of the event. This parameter is required. Data type: Boolean. log proxy name: specifies _ _ whether to record the name of the proxy. This parameter is required. Data type: Boolean. |
|---|---|---|---|---|

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 53e59af3-3209- 452a-853c- ac10ad815929 | The request ID. |
| TaskStatus | Struct |   | The status of the task. |

| └TaskId | String | c68646a1-58f8- 4b75-828a- a2d3b19b**** | The task ID. |
|---|---|---|---|
| └Time | String | 1593593692 | The time when the task status message was generated. Unit: seconds. |
| └TaskList | String | ["Generated website configurations", "Generated policy configurations"] | The descriptions of the task. This value is returned only for asynchronous tasks. |
| └StatusMess age | String | The configuration is in effect. | The status message of the task. You can ignore this reserved parameter. |
| └SuccessCod e | String | 1 | The status code of the task. Valid values: 0: The task fails. 1: The task is successful. 2: The task is not started. |
|   |   | {"id": 7, "ip": ["0.0.XX.XX"], "session method": _ {"type": "off"}, "policy rules": [], _ "health check stat _ _ us": "", "backend config": _ {"type": "proxy", "load balance poli _ _ cy": "Round Robin", "servers": [{"protocol": "http", "attr": "normal", "host": "10.10.XX.XX", "port": 15334, "weight": 1}], "x forwarded for a _ _ _ ction": "append", "header config": [], _ "health check conf _ _ ig": {"is enabled": _ false, "check http expec _ _ t alive": _ ["http 2xx", _ "http 3xx"], _ "check type": _ "http", "interval": 30000, "fall": 5, "rise": 2, "timeout": 1000, "port": null, "host": "", "method": "GET", "path": "/"}, "proxy ssl protocol _ _ s": [], "proxy ssl ciphers" _ _ : ""}, "vpc": "vpc- tx9v6pc1nwc7pgtjx |   |

| └Result | String | ****", "vpc name": _ "yundun****", "vip": ["10.10.XX.XX"], "ports": [{"port": 80, "ssl": false, "http2": false}], "is vpc website": _ _ false, "operation mode": _ "Software Reverse Proxy", "interface": "virtual", "server names": _ ["www.aliyun.com"] , "ssl protocols": [], _ "ssl ciphers": "", _ "name": "www.aliyun.com", "create time": _ "1598243334", "last update time" _ _ : "1598339330", "is enabled": true, _ "detector ip sourc _ _ e": ["Socket"], "proxy ip list": [], | The information about the added website. |
|---|---|---|---|
|   |   | _ _ "proxy ip groups": _ _ [], "access log": _ {"is enabled": _ true, "log request head _ _ er": false, "log response hea _ _ der": false, "log request body" _ _ : false, "log payload": _ false, "is enable full acc _ _ _ ess log": false, _ "log dest ip": true, _ _ "log src port": _ _ true, "log event id": _ _ true, "log proxy name": _ _ true}, "remark": "", "ssl cert": null, _ "policy group": _ 26} |   |

**Examples**

Sample requests

```
https://semawaf.[RegionId].aliyuncs.com/?Action=CreateWebsite &RegionId=cn-hangzhou &Name=test-website-1 &ServerNameList.1=www.aliyun.com &PortList.1={\"port\":80,\"http2\":false,\"ssl\":false} &SSLCertId=3 &BackendConfig={\"type\": \"proxy\", \"servers\": [{\"host\": \"192.168.XX.XX\", \"port \": 80, \"protocol\": \"http\", \"attr\": \"ecs\", \"weight\": 1, \"health_check_status\": \"UNKNOWN\"}], \"load_balance_policy\": \"Round Robin\", \"x_f orwarded_for_action\": \"append\", \"header_config\": []} &PolicyGroupId=6 &SessionMethod={\"param\":\"userId\",\"type\":\"url_query\"} &Remark=**site-1 &Vpc=vpc-RSABVqbNiS**** &VpcName=csw &IsVpcWebsite=true &VipList.1=192.168.XX.XX &IpSourceMethod.1=Socket &AccessLogConfig={\"is_enabled\": true, \"log_request_header\": false, \"log_response_header\": false, \"log_request_body\": false, \"log_payload\": false, \" log_dest_ip\": true, \"is_enable_full_access_log\": false, \"log_src_port\": true, \"lo g_event_id\": true, \"log_proxy_name\": true}
```

Sample success responses `XML` format

```json
<CreateWebsiteResponse>
    <RequestId>53e59af3-3209-452a-853c-ac10ad815929</RequestId>
    <TaskStatus>
        <TaskId>c68646a1-58f8-4b75-828a-a2d3b19b382a</TaskId>
        <Time>1593593692</Time>
        <TaskList>["Generated website configurations", "Generated policy
configurations"]<TaskList>
        <StatusMessage>The configuration is in effect.</StatusMessage>
        <SuccessCode>1</SuccessCode>
        <Result>{"id": 7, "ip": ["0.0.XX.XX"], "session_method": {"type": "off"},
"policy_rules": [], "health_check_status": "", "backend_config": {"type": "proxy", "loa d_balance_policy": "Round Robin", "servers": [{"protocol": "http", "attr": "normal", "h ost": "10.10.XX.XX", "port": 15334, "weight": 1}], "x_forwarded_for_action": "append", "header_config": [], "health_check_config": {"is_enabled": false, "check_http_expect_alive": ["http_2xx", "http_3xx"], "check_type": "http", "interval": 30000, "fall": 5, "rise": 2, "timeout": 1000, "port": null, "host": "", "method": "GET" , "path": "/"}, "proxy_ssl_protocols": [], "proxy_ssl_ciphers": ""}, "vpc": "vpc-tx9v6p c1nwc7pgtjx****", "vpc_name": "yundun****", "vip": ["10.10.XX.XX"], "ports": [{"port": 80, "ssl": false, "http2": false}], "is_vpc_website": false, "operation_mode": "Softwar e Reverse Proxy", "interface": "virtual", "server_names": ["www.aliyun.com"], "ssl_protocols": [], "ssl_ciphers": "", "name": "www.aliyun.com", "create_time": "15982 43334", "last_update_time": "1598339330", "is_enabled": true, "detector_ip_source": ["S ocket"], "proxy_ip_list": [], "proxy_ip_groups": [], "access_log": {"is_enabled": true, "log_request_header": false, "log_response_header": false, "log_request_body": false, " log_payload": false, "is_enable_full_access_log": false, "log_dest_ip": true, "log_src_ port": true, "log_event_id": true, "log_proxy_name": true}, "remark": "", "ssl_cert": n ull, "policy_group": 26}</Result>
    </TaskStatus>
</CreateWebsiteResponse>
```

`JSON` format `{`

```json
  "RequestId":"53e59af3-3209-452a-853c-ac10ad815929",
  "TaskStatus":{
    "TaskId":"c68646a1-58f8-4b75-828a-a2d3b19b382a",
    "TaskList":"[\"Generated website configurations\", \"Generated policy
configurations\"]",
    "SuccessCode":"1",
    "Time":"1593593692",
    "StatusMessage":"The configuration is in effect.",
    "Result":"{\"id\": 7, \"ip\": [\"0.0.XX.XX\"], \"session_method\": {\"type\": \"off
\"}, \"policy_rules\": [], \"health_check_status\": \"\", \"backend_config\": {\"type\" : \"proxy\", \"load_balance_policy\": \"Round Robin\", \"servers\": [{\"protocol\": \"h ttp\", \"attr\": \"normal\", \"host\": \"10.10.XX.XX\", \"port\": 15334, \"weight\": 1} ], \"x_forwarded_for_action\": \"append\", \"header_config\": [], \"health_check_config\": {\"is_enabled\": false, \"check_http_expect_alive\": [\"http_2 xx\", \"http_3xx\"], \"check_type\": \"http\", \"interval\": 30000, \"fall\": 5, \"rise \": 2, \"timeout\": 1000, \"port\": null, \"host\": \"\", \"method\": \"GET\", \"path\" : \"/\"}, \"proxy_ssl_protocols\": [], \"proxy_ssl_ciphers\": \"\"}, \"vpc\": \"vpc-tx9 v6pc1nwc7pgtjx****\", \"vpc_name\": \"yundun****\", \"vip\": [\"10.10.XX.XX\"], \"ports \": [{\"port\": 80, \"ssl\": false, \"http2\": false}], \"is_vpc_website\": false, \"op eration_mode\": \"Software Reverse Proxy\", \"interface\": \"virtual\", \"server_names\": [\"www.aliyun.com\"], \"ssl_protocols\": [], \"ssl_ciphers\": \"\", \ "name\": \"www.aliyun.com\", \"create_time\": \"1598243334\", \"last_update_time\": \"1 598339330\", \"is_enabled\": true, \"detector_ip_source\": [\"Socket\"], \"proxy_ip_list\": [], \"proxy_ip_groups\": [], \"access_log\": {\"is_enabled\": true, \"log_request_header\": false, \"log_response_header\": false, \"log_request_body\": fa lse, \"log_payload\": false, \"is_enable_full_access_log\": false, \"log_dest_ip\": tru e, \"log_src_port\": true, \"log_event_id\": true, \"log_proxy_name\": true}, \"remark\ ": \"\", \"ssl_cert\": null, \"policy_group\": 26}"
```

`}` `}`

**Error codes**

For a list of error codes, see Error codes.

#### 4.2.3 EditWebsite

Modifies the information about a specific website.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | EditWebsite | The operation that you want to perform. Set the value to EditWebsite. |
| RegionId | String | Yes | cn-hangzhou |   |

| Id | Integer | Yes | 1 | The ID of the website. |
|---|---|---|---|---|
| Name | String | Yes | test-website-1 | The name of the website. |
| ServerNameLis t | RepeatL ist | Yes | ["www.aliyun.co m", "www.taobao.co m"] | The domain name of the website. You can enter multiple domain names. |
| PortList | RepeatL ist | Yes | [{"port":80,"ssl": false,"http2":fals e}, {"port":443,"ssl" :true,"http2":tru e}] | The port information about the website. This parameter is a string consisting of JSON arrays. Each element in a JSON array is a JSON struct that includes the following fields: port: the port number of the website. This field is required. Data type: integer. Valid values: 1 to 65535. ssl: specifies whether to enable an SSL certificate. This field is required. Data type: Boolean. http2: specifies whether to enable HTTP/2. This field is required. Data type: Boolean. |
| SSLCertId | Integer | No | 3 | The ID of the SSL certificate. If ssl of a port specified in PortList is set to true, this field is required. |
|   |   |   |   | The configurations of the website. This parameter is a string consisting of JSON structs. A JSON struct includes the following fields: type: the method to respond to requests. This field is required. Data type: string. Valid values: proxy: forwards requests to the backend server. redirect: redirects requests. response: returns specific content. servers: the information about the backend server. This field is a string consisting of JSON arrays. Each element in a JSON array is a JSON struct that includes the following fields: path: the destination address for redirection. Data type: string. If type in BackendConfig is set to redirect or response, this field is required. |

|   |   |   |   | status code: the status code in _ the responses. Data type: integer. If type in BackendConfig is set to redirect or response, this field is required. host: the IP address of the backend server. This field is required. Data type: string. If the backend server is an Elastic Compute Service (ECS) or Server Load Balancer (SLB) instance, you can call the DescribeEcs or DescribeSlb operation to query the IP |
|---|---|---|---|---|
| BackendConfig | Json | Yes | {"type": "proxy", "servers": [{"host": "192.168.XX.XX" , "port": 80, "protocol": "http", "attr": "ecs", "weight": 1}], "load balance p _ _ olicy": "Round Robin", "x forwarded fo _ _ r action": _ "append", "header config": _ []} | addresses (values of the host field) of backend servers. port: the port number of the backend server. This field is required. Data type: integer. Valid values: 1 to 65535. protocol :the protocol of the backend server. This field is required. Data type: string. Valid values: http and https. attr: the type of the backend server. This field is required. Data type: string. If you do not need to forward requests destined for the website to a specific backend server, set the value to normal. If you need to forward requests destined for the website to a specific backend server, set the value to ecs or slb. weight: the weight of the backend server. This field is required. Data type: integer. Valid values: any non-zero positive integer. load balance policy: the _ _ scheduling algorithm. This field is required. Data type: string. Valid values: Round Robin: weighted round- robin Least Connected: least connection scheduling IP Hash: source IP hash x forwarded for action: the _ _ _ action on the X-Forwarded-For field in the HTTP request header. To identify the actual IP addresses of the clients that access your website by using HTTP proxies or load balancing servers, you can specify this field. This field is required. Data type: string. Valid values: |

|   |   |   |   | append: appends the last-hop IP address to the X-Forwarded- For field. cover: overwrites the original value of the X-Forwarded-For field with the last-hop IP address. no action: retains the original _ value of the X-Forwarded-For field. header config: the HTTP header _ configurations. This field is required. Data type: list. If you do not need to configure the HTTP header, set the field to an empty array. This field is a string consisting of JSON arrays. Each element in a JSON array is a JSON struct that includes the following fields: name: the name of the HTTP header. This field is required. Data type: string. context: the type of the HTTP header. This field is required. Data type: string. Valid values: request and response. action: the action on the HTTP header. This field is required. Data type: string. Valid values: set and hide. |
|---|---|---|---|---|
| PolicyGroupId | Integer | No | 6 | name: the value of the HTTP header. This field is required. The ID of the protection policy. If Data type: string. type in BackendConfig is set to proxy, this field is required. |
| SessionMetho d | Json | Yes | {"param":"userI d","type":"url qu _ ery"} | The method to identify users. This parameter is a string consisting of JSON structs. A JSON struct includes the following fields: param: the ID of the user. type: the method to identify users. This field is required. Data type: string. Valid values: off: does not identify users. custom: identifies users based on their IDs that are extracted from requests. cookie: identifies users based on the Cookie field. url query: identifies users _ based on the GET parameters. body form: identifies users _ based on the POST parameters. header: identifies users based on the HTTP header. internal session: identifies _ users based on their systems. |

| Remark | String | No | Test site-1 | The remarks. |
|---|---|---|---|---|
| Vpc | String | No | vpc- RSABVqbNiS**** | The ID of the virtual private cloud (VPC). You can call the DescribeVpc operation to query the IDs of VPCs. |
| VpcName | String | No | csw | The name of the VPC. You can call the DescribeVpc operation to query the names of VPCs. |
| IsVpcWebsite | Boolean | No | true | Specifies whether the website is in a VPC. Default value: false. Valid values: true false |
| VipList | RepeatL ist | Yes | ["192.168.XX.XX ", "192.168.XX.XX" ] | The virtual IP address (VIP). You can enter multiple VIPs. You can call the DescribeInternetVip operation to query the VIPs on the Internet and the DescribeVpcVip operation to query the VIPs in VPCs. |
| IpSourceMetho d | RepeatL ist | Yes | ["Socket"] | The method to obtain the actual IP address. You can enter multiple methods. To obtain the actual IP address from a field in the HTTP request header, set the value to XYZ/X-Forwarded-For:-n. To obtain the socket information about the last nth proxy from X-Forwarded-For, append Socket to the end of the parameter value. |

| AccessLogConf ig | Json | Yes | {"is enabled": _ true, "log request he _ _ ader": false, "log response h _ _ eader": false, "log request bo _ _ dy": false, "log payload": _ false, "log dest ip": _ _ true, "is enable full a _ _ _ ccess log": _ false, "log src port": _ _ true, "log event id": _ _ true, "log proxy nam _ _ e": true} | The configurations for access logs. This parameter is a string consisting of JSON structs. A JSON struct includes the following fields: is enabled: specifies whether to _ record HTTP access logs. This parameter is required. Data type: Boolean. log request header: specifies _ _ whether to record the HTTP request header. This parameter is required. Data type: Boolean. log response header: specifies _ _ whether to record the HTTP response header. This parameter is required. Data type: Boolean. log request body: specifies _ _ whether to record the HTTP request body. This parameter is required. Data type: Boolean. The maximum size of the HTTP request body that can be logged is 4 KB. log payload: specifies whether to _ record the payload. This parameter is required. Data type: Boolean. log dest ip: specifies whether to _ _ record the destination IP address. This parameter is required. Data type: Boolean. is enable full access log: _ _ _ _ specifies whether to record the full access logs. This parameter is required. Data type: Boolean. log src port: specifies whether to _ _ record the source port. This parameter is required. Data type: Boolean. log event id: specifies whether _ _ to record the ID of the event. This parameter is required. Data type: Boolean. log proxy name: specifies _ _ whether to record the name of the proxy. This parameter is required. Data type: Boolean. |
|---|---|---|---|---|
| SSLProtocols | RepeatL ist | No | ["TLSv1.1", "TLSv1.2"] | The version of the SSL protocol. Valid values: SSLv2, SSLv3, TLSv1, TLSv1.1, TLSv1.2, and TLSv1.3. |

| SSLCiphers | String | No | TLS RSA WITH _ _ _ AES 128 CBC S _ _ _ HA | The SSL cipher suite. This parameter is empty by default. You can directly use the cipher strings provided by OpenSSL. You can also concatenate and combine the cipher strings to match the value of the SSLProtocols parameter. Example: TLSv1.2:!eNULL:!aNULL:!TLSv1.1:!TL Sv1:!SSLv3. |
|---|---|---|---|---|
| ProxyBindingC onfig | Json | No | {"enable": true, "hash select ip _ _ _ method": "remote addr a _ _ nd port", _ "proxy bind ip li _ _ _ st": [{"id": "c43b02112.clo ud.b03.amtest2 1", "ips": ["10.10.XX.XX"] }]} | The configurations of back-to-origin IP addresses. The value is a string that consists of a JSON struct. The JSON struct contains the following fields: enable: specifies whether to enable session persistence. This field is required. Data type: Boolean. hash select ip method: the _ _ _ method for session persistence. This field is optional. Data type: string. Valid values: remote addr: source address- _ based hashing remote addr and port: _ _ _ source port-based hashing proxy bind ip list: the list of IP _ _ _ addresses. This field is optional. Data type: list. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 53e59af3-3209- 452a-853c- ac10ad815929 | The ID of the request. |
| TaskStatus | Struct |   |   |
| └TaskId | String | c68646a1-58f8- 4b75-828a- a2d3b19b382a |   |
| └Time | String | 1593593692 | The timestamp when the task is complete. Unit: seconds. |

| └TaskList | String | ["Generated website configurations", "Generated policy configurations"] | The descriptions of the task. This value is returned only for asynchronous tasks. |
|---|---|---|---|
| └StatusMess age | String | The configuration is in effect. | The status information about the task. |
| └SuccessCod e | String | 1 | The status code of the task. Valid values: 0: The task fails. 1: The task is successful. 2: The task is not started. |
|   |   | {"id": 7, "ip": ["0.0.XX.XX"], "session method": _ {"type": "off"}, "policy rules": [], _ "health check stat _ _ us": "", "backend config": _ {"type": "proxy", "load balance poli _ _ cy": "Round Robin", "servers": [{"protocol": "http", "attr": "normal", "host": "10.10.XX.XX", "port": 15334, "weight": 1}], "x forwarded for a _ _ _ ction": "append", "header config": [], _ "health check conf _ _ ig": {"is enabled": _ false, "check http expec _ _ t alive": _ ["http 2xx", _ "http 3xx"], _ "check type": _ "http", "interval": 30000, "fall": 5, "rise": 2, "timeout": 1000, "port": null, "host": "", "method": "GET", "path": "/"}, "proxy ssl protocol _ _ s": [], "proxy ssl ciphers" _ _ : ""}, "vpc": "vpc- tx9v6pc1nwc7pgtjx ****", "vpc name": _ |   |

| └Result | String | "yundun****", "vip": ["10.10.XX.XX"], "ports": [{"port": 80, "ssl": false, "http2": false}], "is vpc website": _ _ false, "operation mode": _ "Software Reverse Proxy", "interface": "virtual", "server names": _ ["www.aliyun.com"] , "ssl protocols": [], _ "ssl ciphers": "", _ "name": "www.aliyun.com", "create time": _ "1598243334", "last update time" _ _ : "1598339330", "is enabled": true, _ "detector ip sourc _ _ e": ["Socket"], "proxy ip list": [], _ _ "proxy ip groups": _ _ [], "access log": _ | The information about the website after modification. |
|---|---|---|---|
|   |   | {"is enabled": _ true, "log request head _ _ er": false, "log response hea _ _ der": false, "log request body" _ _ : false, "log payload": _ false, "is enable full acc _ _ _ ess log": false, _ "log dest ip": true, _ _ "log src port": _ _ true, "log event id": _ _ true, "log proxy name": _ _ true}, "remark": "", "ssl cert": null, _ "policy group": _ 26} |   |

**Examples**

Sample requests

```
https://semawaf.[RegionId].aliyuncs.com/?Action=EditWebsite &RegionId=cn-hangzhou &Id=1 &Name=test-website-1 &ServerNameList.1=www.aliyun.com &PortList.1={\"port\":80,\"http2\":false,\"ssl\":false} &SSLCertId=3 &BackendConfig={\"type\": \"proxy\", \"servers\": [{\"host\": \"192.168.XX.XX\", \"port \": 80, \"protocol\": \"http\", \"attr\": \"ecs\", \"weight\": 1, \"health_check_status\": \"UNKNOWN\"}], \"load_balance_policy\": \"Round Robin\", \"x_f orwarded_for_action\": \"append\", \"header_config\": []} &PolicyGroupId=6 &SessionMethod={\"param\":\"userId\",\"type\":\"url_query\"} &Remark=****website-1 &Vpc=vpc-RSABVqbNiS**** &VpcName=csw &IsVpcWebsite=true &VipList.1=192.168.XX.XX &IpSourceMethod.1=Socket &AccessLogConfig={\"is_enabled\": true, \"log_request_header\": false, \"log_response_header\": false, \"log_request_body\": false, \"log_payload\": false, \" log_dest_ip\": true, \"is_enable_full_access_log\": false, \"log_src_port\": true, \"lo g_event_id\": true, \"log_proxy_name\": true} &SSLProtocols.1=TLSv1.1 &SSLCiphers=TLS_RSA_WITH_AES_128_CBC_SHA &ProxyBindingConfig={\"enable\": true, \"hash_select_ip_method\": \"remote_addr_and_port\", \"proxy_bind_ip_list\": [{\"id\": \"c43b02112.cloud.b03****\", \"ips\": [\"10.10.XX.XX\"]}]}
```

Sample success responses `XML` format

```json
<EditWebsiteResponse>
    <RequestId>53e59af3-3209-452a-853c-ac10ad815929</RequestId>
    <TaskStatus>
        <TaskId>c68646a1-58f8-4b75-828a-a2d3b19b382a</TaskId>
        <Time>1593593692</Time>
        <TaskList>["Generated website configurations", "Generated policy
configurations"]<TaskList>
        <StatusMessage>The configuration is in effect.</StatusMessage>
        <SuccessCode>1</SuccessCode>
        <Result>{"id": 7, "ip": ["0.0.XX.XX"], "session_method": {"type": "off"},
"policy_rules": [], "health_check_status": "", "backend_config": {"type": "proxy", "loa d_balance_policy": "Round Robin", "servers": [{"protocol": "http", "attr": "normal", "h ost": "10.10.XX.XX", "port": 15334, "weight": 1}], "x_forwarded_for_action": "append", "header_config": [], "health_check_config": {"is_enabled": false, "check_http_expect_alive": ["http_2xx", "http_3xx"], "check_type": "http", "interval": 30000, "fall": 5, "rise": 2, "timeout": 1000, "port": null, "host": "", "method": "GET" , "path": "/"}, "proxy_ssl_protocols": [], "proxy_ssl_ciphers": ""}, "vpc": "vpc-tx9v6p c1nwc7pgtjx****", "vpc_name": "yundun****", "vip": ["10.10.XX.XX"], "ports": [{"port": 80, "ssl": false, "http2": false}], "is_vpc_website": false, "operation_mode": "Softwar e Reverse Proxy", "interface": "virtual", "server_names": ["www.aliyun.com"], "ssl_protocols": [], "ssl_ciphers": "", "name": "www.aliyun.com", "create_time": "15982 43334", "last_update_time": "1598339330", "is_enabled": true, "detector_ip_source": ["S ocket"], "proxy_ip_list": [], "proxy_ip_groups": [], "access_log": {"is_enabled": true, "log_request_header": false, "log_response_header": false, "log_request_body": false, " log_payload": false, "is_enable_full_access_log": false, "log_dest_ip": true, "log_src_ port": true, "log_event_id": true, "log_proxy_name": true}, "remark": "", "ssl_cert": n ull, "policy_group": 26}</Result>
    </TaskStatus>
</EditWebsiteResponse>
```

`JSON` format `{`

```json
  "RequestId":"53e59af3-3209-452a-853c-ac10ad815929",
  "TaskStatus":{
    "TaskId":"c68646a1-58f8-4b75-828a-a2d3b19b382a",
    "TaskList":"[\"Generated website configurations\", \"Generated policy
configurations\"]",
    "SuccessCode":"1",
    "Time":"1593593692",
    "StatusMessage":"The configuration is in effect.",
    "Result":"{\"id\": 7, \"ip\": [\"0.0.XX.XX\"], \"session_method\": {\"type\": \"off
\"}, \"policy_rules\": [], \"health_check_status\": \"\", \"backend_config\": {\"type\" : \"proxy\", \"load_balance_policy\": \"Round Robin\", \"servers\": [{\"protocol\": \"h ttp\", \"attr\": \"normal\", \"host\": \"10.10.XX.XX\", \"port\": 15334, \"weight\": 1} ], \"x_forwarded_for_action\": \"append\", \"header_config\": [], \"health_check_config\": {\"is_enabled\": false, \"check_http_expect_alive\": [\"http_2 xx\", \"http_3xx\"], \"check_type\": \"http\", \"interval\": 30000, \"fall\": 5, \"rise \": 2, \"timeout\": 1000, \"port\": null, \"host\": \"\", \"method\": \"GET\", \"path\" : \"/\"}, \"proxy_ssl_protocols\": [], \"proxy_ssl_ciphers\": \"\"}, \"vpc\": \"vpc-tx9 v6pc1nwc7pgtjx****\", \"vpc_name\": \"yundun****\", \"vip\": [\"10.10.XX.XX\"], \"ports \": [{\"port\": 80, \"ssl\": false, \"http2\": false}], \"is_vpc_website\": false, \"op eration_mode\": \"Software Reverse Proxy\", \"interface\": \"virtual\", \"server_names\": [\"www.aliyun.com\"], \"ssl_protocols\": [], \"ssl_ciphers\": \"\", \ "name\": \"www.aliyun.com\", \"create_time\": \"1598243334\", \"last_update_time\": \"1 598339330\", \"is_enabled\": true, \"detector_ip_source\": [\"Socket\"], \"proxy_ip_list\": [], \"proxy_ip_groups\": [], \"access_log\": {\"is_enabled\": true, \"log_request_header\": false, \"log_response_header\": false, \"log_request_body\": fa lse, \"log_payload\": false, \"is_enable_full_access_log\": false, \"log_dest_ip\": tru e, \"log_src_port\": true, \"log_event_id\": true, \"log_proxy_name\": true}, \"remark\ ": \"\", \"ssl_cert\": null, \"policy_group\": 26}"
```

`}` `}`

**Error codes**

For a list of error codes, see Error codes.

#### 4.2.4 ToggleWebsite

Enables or disables WAF protection for a specific website.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ToggleWebsite | The operation that you want to perform. Set the value to ToggleWebsite. |
| RegionId | String | Yes | cn-hangzhou |   |

| IdList | RepeatL ist | Yes | [1, 2] | The IDs of websites. You can call the DescribeWebsite operation to query the IDs of websites. |
|---|---|---|---|---|
| ToggleAction | String | Yes | disable | Specifies the protection status of the website. Valid values: enable: enables WAF protection. disable: disables WAF protection. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 53e59af3-3209- 452a-853c- ac10ad815929 | The ID of the request. |
| TaskStatus | Struct |   | The returned information. |
| └TaskId | String | c68646a1-58f8- 4b75-828a- a2d3b19b382a | The ID of the task. |
| └Time | String | 1593593692 | The time when the task status message was generated. This value is a UNIX timestamp representing the number of seconds that have elapsed since the epoch time January 1, 1970, 00:00:00 UTC. |
| └TaskList | String | ["Website-related configuration generation", "Policy-related configuration generation"] | The descriptions of the task. This value is returned only for asynchronous tasks. |
| └StatusMess age | String | The configuration is in effect. | The status message of the task. |
| └SuccessCod e | String | 1 | The status code of the task. Valid values: 0: The task fails. 1: The task is successful. 2: The task is not started. |

**Examples**

Sample requests

```
https://semawaf.[ RegionId].aliyuncs.com/?Action=ToggleWebsite &RegionId=cn-hangzhou &IdList.1=1 &ToggleAction=disable
```

Sample success responses `XML` format

```xml
<ToggleWebsiteResponse>
    <RequestId>53e59af3-3209-452a-853c-ac10ad815929</RequestId>
    <TaskStatus>
        <TaskId>c68646a1-58f8-4b75-828a-a2d3b19b382a</TaskId>
        <Time>1593593692</Time>
        <TaskList>["Website-related configuration generation", "Policy-related
configuration generation"]</TaskList>
        <StatusMessage>The configuration is in effect.</StatusMessage>
        <SuccessCode>1</SuccessCode>
    </TaskStatus>
</ToggleWebsiteResponse>
```

`JSON` format `{`

```json
  "RequestId":"53e59af3-3209-452a-853c-ac10ad815929",
  "TaskStatus":{
    "TaskId":"c68646a1-58f8-4b75-828a-a2d3b19b382a",
    "TaskList":"[\"Website-related configuration generation\", \"Policy-related
configuration generation\"]",
    "SuccessCode":"1",
    "Time":"1593593692",
    "StatusMessage":"The configuration is in effect."
```

`}` `}`

**Error codes**

For a list of error codes, see Error codes.

#### 4.2.5 QueryAsyncTaskStatus

Queries the status of an asynchronous task.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | QueryAsyncTask Status | The operation that you want to perform. Set the value to QueryAsyncTaskStatus. |
| RegionId | String | Yes | cn-hangzhou |   |
| TaskId | String | Yes | 11c745fc-1d66- 40ea-90d7- 7e9a12b987b2 | The ID of the asynchronous task. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|

| RequestId | String | 53e59af3-3209- 452a-853c- ac10ad815929 | The ID of the request. |
|---|---|---|---|
| TaskStatus | Struct |   |   |
| └TaskId | String | c68646a1-58f8- 4b75-828a- a2d3b19b382a | The ID of the task. |
| └Time | String | 1593593692 | The time when the task status message was generated. This value is a UNIX timestamp representing the number of seconds that have elapsed since the epoch time January 1, 1970, 00:00:00 UTC. |
| └TaskList | String | ["Website-related configuration generation", "Policy-related configuration generation"] | The descriptions of the task. This value is returned only for asynchronous tasks. |
| └StatusMess age | String | The configuration is in effect. | The status message of the task. |
| └SuccessCod e | String | 1 | The status code of the task. Valid values: 0: The task fails. 1: The task is successful. 2: The task is not started. |

**Examples**

Sample requests

```
https://semawaf.[ RegionId].aliyuncs.com/?Action=QueryAsyncTaskStatus &RegionId=cn-hangzhou &TaskId=11c745fc-1d66-40ea-90d7-7e9a12b987b2
```

Sample success responses `XML` format

```xml
<QueryAsyncTaskStatusResponse>
    <RequestId>53e59af3-3209-452a-853c-ac10ad815929</RequestId>
    <TaskStatus>
        <TaskId>c68646a1-58f8-4b75-828a-a2d3b19b382a</TaskId>
        <Time>1593593692</Time>
        <TaskList>["Website-related configuration generation", "Policy-related
configuration generation"]</TaskList>
        <StatusMessage>The configuration is in effect.</StatusMessage>
        <SuccessCode>1</SuccessCode>
    </TaskStatus>
</QueryAsyncTaskStatusResponse>
```

`JSON` format

|   | { "RequestId":"53e59af3-3209-452a-853c-ac10ad815929", "TaskStatus":{ "TaskId":"c68646a1-58f8-4b75-828a-a2d3b19b382a", "TaskList":"[\"Website-related configuration generation\", \"Policy-related configuration generation\"]", "SuccessCode":"1", "Time":"1593593692", "StatusMessage":"The configuration is in effect." } } |
|---|---|

**Error codes**

For a list of error codes, see Error codes.

#### 4.2.6 QueryAsyncTaskStatus

Queries the status of an asynchronous task.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | QueryAsyncTask Status | The operation that you want to perform. Set the value to QueryAsyncTaskStatus. |
| RegionId | String | Yes | cn-hangzhou |   |
| TaskId | String | Yes | 11c745fc-1d66- 40ea-90d7- 7e9a12b987b2 | The ID of the asynchronous task. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 53e59af3-3209- 452a-853c- ac10ad815929 | The ID of the request. |
| TaskStatus | Struct |   |   |
| └TaskId | String | c68646a1-58f8- 4b75-828a- a2d3b19b382a | The ID of the task. |
| └Time | String | 1593593692 | The time when the task status message was generated. This value is a UNIX timestamp representing the number of seconds that have elapsed since the epoch time January 1, 1970, 00:00:00 UTC. |

| └TaskList | String | ["Website-related configuration generation", "Policy-related configuration generation"] | The descriptions of the task. This value is returned only for asynchronous tasks. |
|---|---|---|---|
| └StatusMess age | String | The configuration is in effect. | The status message of the task. |
| └SuccessCod e | String | 1 | The status code of the task. Valid values: 0: The task fails. 1: The task is successful. 2: The task is not started. |

**Examples**

Sample requests

```
https://semawaf.[ RegionId].aliyuncs.com/?Action=QueryAsyncTaskStatus &RegionId=cn-hangzhou &TaskId=11c745fc-1d66-40ea-90d7-7e9a12b987b2
```

Sample success responses `XML` format

```xml
<QueryAsyncTaskStatusResponse>
    <RequestId>53e59af3-3209-452a-853c-ac10ad815929</RequestId>
    <TaskStatus>
        <TaskId>c68646a1-58f8-4b75-828a-a2d3b19b382a</TaskId>
        <Time>1593593692</Time>
        <TaskList>["Website-related configuration generation", "Policy-related
configuration generation"]</TaskList>
        <StatusMessage>The configuration is in effect.</StatusMessage>
        <SuccessCode>1</SuccessCode>
    </TaskStatus>
</QueryAsyncTaskStatusResponse>
```

`JSON` format `{`

```json
  "RequestId":"53e59af3-3209-452a-853c-ac10ad815929",
  "TaskStatus":{
    "TaskId":"c68646a1-58f8-4b75-828a-a2d3b19b382a",
    "TaskList":"[\"Website-related configuration generation\", \"Policy-related
configuration generation\"]",
    "SuccessCode":"1",
    "Time":"1593593692",
    "StatusMessage":"The configuration is in effect."
```

`}` `}`

**Error codes**

For a list of error codes, see Error codes.

#### 4.2.7 UploadResponsePage

Uploads a response page file.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | UploadResponse Page | The operation that you want to perform. Set the value to UploadResponsePage. |
| RegionId | String | Yes | cn-hangzhou |   |
| FileName | String | No | forbidden.html | The name of the file. |
| FileContent | String | Yes | VXVPVm5QZEVu WHJhc2ViUGhNZ EZRWHBjSnNRZ XJn | The Base64-encoded content of the file. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 53e59af3-3209- 452a-853c- ac10ad815929 | The ID of the request. |
| Result | String | {"path":"572e83ed 33331eb575f2dbd 39f07e155"} | The returned information. path: the path of the uploaded file. |

**Examples**

Sample requests

```
https://semawaf.[ RegionId].aliyuncs.com/?Action=UploadResponsePage &RegionId=cn-hangzhou &FileName=forbidden.html &FileContent=VXVPVm5QZEVuWHJhc2ViUGhNZEZRWHBjSnNRZXJn
```

Sample success responses `XML` format

```xml
<UploadResponsePageResponse>
    <RequestId>53e59af3-3209-452a-853c-ac10ad815929</RequestId>
    <Result>{&quot;path&quot;: &quot;572e83ed33331eb575f2dbd39f07e155&quot;}</Result>
</UploadResponsePageResponse>
```

`JSON` format `{`

```json
  "RequestId":"53e59af3-3209-452a-853c-ac10ad815929",
  "Result":"{\"path\": \"572e83ed33331eb575f2dbd39f07e155\"}"
```

`}`

**Error codes**

For a list of error codes, see Error codes.

#### 4.2.8 DescribeInvalidWebsite

Queries the information about the invalid websites that are discovered by the upgrade detection feature.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeInvalid Website | The operation that you want to perform. Set the value to DescribeInvalidWebsite. |
| RegionId | String | Yes | cn-hangzhou |   |
| Id | Integer | No | 1 | The ID of the invalid website. |
| PageSize | Integer | No | 20 | The number of entries to return on each page. Default value: 10. |
| PageNumber | Integer | No | 1 | The number of the page to return. Default value: 1. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 53e59af3-3209- 452a-853c- ac10ad815929 | The ID of the request. |

| Result | String | [{"id": 1, "name": "invalid website 1" _ _ , "server names": _ ["www.taobao.com "], "backend config": _ {"type": "proxy", "load balance poli _ _ cy": "Round Robin", "servers": [{"protocol": "http", "attr": "slb", "host": "192.168.XX.XX", "port": 80, "weight": 1}], "x forwarded for a _ _ _ ction": "append", "header config": [], _ "health check conf _ _ ig": {"is enabled": _ false, "check http expec _ _ t alive": _ ["http 2xx", _ "http 3xx"], _ "check type": _ "http", "interval": 30000, "fall": 5, "rise": 2, "timeout": 1000, "port": null, "host": "", "method": "GET", "path": "/"}, "proxy ssl protocol _ _ s": [], "proxy ssl ciphers" _ _ : ""}, "aliyun info": _ {"id": 1, "vpc": "vpc- tx9isq1jrry8k3h9q* ***", "vswitch": "vsw- tx9v9qpazlcdcc86f ****", "vip": ["10.10.XX.XX"], "is normal": true, _ "frontend port": _ [80]}}] | The returned result of the request. |
|---|---|---|---|

**Examples**

Sample requests

```
https://semawaf.[ RegionId].aliyuncs.com/?Action=DescribeInvalidWebsite &RegionId=cn-hangzhou &Id=1 &PageSize=20 &PageNumber=1
```

Sample success responses `XML` format

```json
<DescribeInvalidWebsiteResponse>
    <RequestId>53e59af3-3209-452a-853c-ac10ad815929</RequestId>
    <Result>[{"id": 1, "name": "invalid_website_1", "server_names": ["www.taobao.com"],
"backend_config": {"type": "proxy", "load_balance_policy": "Round Robin", "servers": [{ "protocol": "http", "attr": "slb", "host": "192.168.XX.XX", "port": 80, "weight": 1}], "x_forwarded_for_action": "append", "header_config": [], "health_check_config": {"is_en abled": false, "check_http_expect_alive": ["http_2xx", "http_3xx"], "check_type": "http ", "interval": 30000, "fall": 5, "rise": 2, "timeout": 1000, "port": null, "host": "", "method": "GET", "path": "/"}, "proxy_ssl_protocols": [], "proxy_ssl_ciphers": ""}, "al iyun_info": {"id": 1, "vpc": "vpc-tx9isq1jrry8k3h9q****", "vswitch": "vswtx9v9qpazlcdcc86f****", "vip": ["10.10.XX.XX"], "is_normal": true, "frontend_port": [80 ]}}]</Result> </DescribeInvalidWebsiteResponse>
```

`JSON` format `{`

```json
  "RequestId":"53e59af3-3209-452a-853c-ac10ad815929",
  "Result":"[{\"id\": 1, \"name\": \"invalid_website_1\", \"server_names\":
[\"www.taobao.com\"], \"backend_config\": {\"type\": \"proxy\", \"load_balance_policy\": \"Round Robin\", \"servers\": [{\"protocol\": \"http\", \"attr \": \"slb\", \"host\": \"192.168.XX.XX\", \"port\": 80, \"weight\": 1}], \"x_forwarded_for_action\": \"append\", \"header_config\": [], \"health_check_config\": {\"is_enabled\": false, \"check_http_expect_alive\": [\"http_2xx\", \"http_3xx\"], \"ch eck_type\": \"http\", \"interval\": 30000, \"fall\": 5, \"rise\": 2, \"timeout\": 1000, \"port\": null, \"host\": \"\", \"method\": \"GET\", \"path\": \"/\"}, \"proxy_ssl_protocols\": [], \"proxy_ssl_ciphers\": \"\"}, \"aliyun_info\": {\"id\": 1, \"vpc\": \"vpc-tx9isq1jrry8k3h9q****\", \"vswitch\": \"vsw-tx9v9qpazlcdcc86f****\", \"v ip\": [\"10.10.XX.XX\"], \"is_normal\": true, \"frontend_port\": [80]}}]"
```

`}`

**Error codes**

For a list of error codes, see Error codes.

#### 4.2.9 DeleteInvalidWebsite

Deletes a specific invalid website. If you use Apsara Stack Enterprise V3.12.0 or upgrade Apsara Stack Enterprise to a later version, WAF performs validity checks and measures invalid websites.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteInvalidWe bsite | The operation that you want to perform. Set the value to DeleteInvalidWebsite. |
| RegionId | String | Yes | cn-hangzhou |   |

| IdList | RepeatL ist | Yes | [1, 2] | The ID of the invalid website. You can enter multiple IDs. You can call the DescribeWebsite operation to query the IDs of websites. |
|---|---|---|---|---|

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 53e59af3-3209- 452a-853c- ac10ad815929 | The ID of the request. |
| Result | String | None | The returned information. This value is empty. |

**Examples**

Sample requests

```
https://semawaf.[ RegionId].aliyuncs.com/?Action=DeleteInvalidWebsite &RegionId=cn-hangzhou &IdList.1=1
```

Sample success responses `XML` format

```xml
<DeleteInvalidWebsiteResponse>
    <RequestId>53e59af3-3209-452a-853c-ac10ad815929</RequestId>
    <Result></Result>
</DeleteInvalidWebsiteResponse>
```

`JSON` format `{`

```json
  "RequestId":"53e59af3-3209-452a-853c-ac10ad815929",
  "Result":""
```

`}`

**Error codes**

For a list of error codes, see Error codes.

#### 4.2.10 DescribeInternetVip

Queries the information about the virtual IP addresses (VIPs) on the Internet.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|

| Action | String | Yes | DescribeIntern etVip | The operation that you want to perform. Set the value to DescribeInternetVip. |
|---|---|---|---|---|
| RegionId | String | Yes | cn-hangzhou |   |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 53e59af3-3209- 452a-853c- ac10ad815929 | The ID of the request. |
| Result | String | [{"ip": "42.36.XX.XX", "type": "internet IP", "delete": false}, {"ip": "10.10.XX.XX", "type": "intranet IP", "delete": false}] | The information about the VIPs on the Internet. The information includes the following fields: ip: the VIP on the Internet. type: the type of the return value. The field value is fixed as internet IP, which indicates a VIP on the Internet. delete: indicates whether the VIP can be deleted. Valid values: true: The VIP can be deleted. false: The VIP cannot be deleted. |

**Examples**

Sample requests

```
https://semawaf.[ RegionId].aliyuncs.com/?Action=DescribeInternetVip &RegionId=cn-hangzhou
```

Sample success responses `XML` format

```xml
<DescribeInternetVipResponse>
    <RequestId>53e59af3-3209-452a-853c-ac10ad815929</RequestId>
    <Result>[{"ip": "42.36.XX.XX", "type": "internet IP", "delete": false}, {"ip": "10.
10.XX.XX", "type": "intranet IP", "delete": false}]</Result> </DescribeInternetVipResponse>
```

`JSON` format `{`

```json
  "RequestId":"53e59af3-3209-452a-853c-ac10ad815929",
  "Result":"[{\"ip\": \"42.36.XX.XX\", \"type\": \"internet IP\", \"delete\": false}, {
\"ip\": \"10.10.XX.XX\", \"type\": \"intranet IP\", \"delete\": false}]"
```

`}`

**Error codes**

For a list of error codes, see Error codes.

#### 4.2.11 CreateInternetVip

Creates a virtual IP address (VIP) on the Internet.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateInternet Vip | The operation that you want to perform. Set the value to CreateInternetVip. |
| RegionId | String | Yes | cn-hangzhou |   |
| IpAddress | String | No | 10.10.XX.XX | The VIP that you want to create on the Internet. |
| IpVersion | String | No | ipv6 | The version of the IP protocol. Valid values: ipv4 ipv6 |
| NetworkType | String | Yes | internet | The type of the network. Valid values: intranet internet If you set the IpVersion parameter to ipv6, you can set the NetworkType parameter only to intranet. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 53e59af3-3209- 452a-853c- ac10ad815929 | The ID of the request. |
| Result | String | {"ip": "42.36.XX.XX", "type": "internet IP", "delete": true} | The information about the created VIP. The information includes the following fields: ip: the VIP on the Internet. type: the type of the return value. The field value is fixed as internet IP, which indicates a VIP on the Internet. delete: indicates whether the VIP can be deleted. Valid values: true: The VIP can be deleted. false: The VIP cannot be deleted. |

**Examples**

Sample requests

```
https://semawaf.[ RegionId].aliyuncs.com/?Action=CreateInternetVip &RegionId=cn-hangzhou &IpAddress=10.10.XX.XX &IpVersion=ipv6 &NetworkType=internet
```

Sample success responses `XML` format

```xml
<CreateInternetVipResponse>
    <RequestId>53e59af3-3209-452a-853c-ac10ad815929</RequestId>
    <Result>{"ip": "42.36.XX.XX", "type": "internet IP", "delete": true}</Result>
</CreateInternetVipResponse>
```

`JSON` format `{`

```json
  "RequestId":"53e59af3-3209-452a-853c-ac10ad815929",
  "Result":"{\"ip\": \"42.36.XX.XX\", \"type\": \"internet IP\", \"delete\": true}"
```

`}`

**Error codes**

For a list of error codes, see Error codes.

#### 4.2.12 DeleteInternetVip

Deletes a virtual IP address (VIP) on the Internet.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteInternet Vip | The operation that you want to perform. Set the value to DeleteInternetVip. |
| RegionId | String | Yes | cn-hangzhou |   |
| Vip | String | No | 10.10.XX.XX | The VIP that you want to delete on the Internet. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 53e59af3-3209- 452a-853c- ac10ad815929 | The ID of the request. |
| Result | String | Empty | The returned information. This value is empty. |

**Examples**

Sample requests

```
https://semawaf.[ RegionId].aliyuncs.com/?Action=DeleteInternetVip &RegionId=cn-hangzhou &Vip=10.10.XX.XX
```

Sample success responses `XML` format

```xml
<DeleteInternetVipResponse>
    <RequestId>53e59af3-3209-452a-853c-ac10ad815929</RequestId>
    <Result></Result>
</DeleteInternetVipResponse>
```

`JSON` format `{`

```json
  "RequestId":"53e59af3-3209-452a-853c-ac10ad815929",
  "Result":""
```

`}`

**Error codes**

For a list of error codes, see Error codes.

#### 4.2.13 DescribeVpc

Queries the information about virtual private clouds (VPCs).

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeVpc | The operation that you want to perform. Set the value to DescribeVpc. |
| RegionId | String | Yes | cn-hangzhou |   |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 53e59af3-3209- 452a-853c- ac10ad815929 | The ID of the request. |

| Result | String | {"vpc list": _ [{"vpc id": "vpc- _ tx9fk7rftc9wbroix* ***", "name": "cfw vpc****", _ "desc": "", "cidr": "172.16.XX.XX/16" }] | The information about the VPCs. |
|---|---|---|---|

**Examples**

Sample requests

```
https://semawaf.[ RegionId].aliyuncs.com/?Action=DescribeVpc &RegionId=cn-hangzhou
```

Sample success responses `XML` format

```xml
<DescribeVpcResponse>
    <RequestId>53e59af3-3209-452a-853c-ac10ad815929</RequestId>
    <Result>{"vpc_list": [{"vpc_id": "vpc-tx9fk7rftc9wbroix****", "name":
"cfw_vpc****", "desc": "", "cidr": "172.16.XX.XX/16"}]</Result> </DescribeVpcResponse>
```

`JSON` format `{`

```json
  "RequestId":"53e59af3-3209-452a-853c-ac10ad815929",
  "Result":"{\"vpc_list\": [{\"vpc_id\": \"vpc-tx9fk7rftc9wbroix****\", \"name\": \"cfw
_vpc****\", \"desc\": \"\", \"cidr\": \"172.16.XX.XX/16\"}]"
```

`}`

**Error codes**

For a list of error codes, see Error codes.

#### 4.2.14 DescribeVSwitch

Queries the information about the vSwitches in a specific virtual private cloud (VPC).

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeVSwitc h | The operation that you want to perform. Set the value to DescribeVSwitch. |
| RegionId | String | Yes | cn-hangzhou |   |

| VpcId | String | Yes | vpc- RSABVqbNiSs* *** | The ID of the VPC. You can call the DescribeVpc operation to query the IDs of VPCs. |
|---|---|---|---|---|

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 53e59af3-3209- 452a-853c- ac10ad815929 | The ID of the request. |
| Result | String | {"vswitch list": _ [{"instanceId": "vsw- tx9v9qpazlcdcc86* ***", "instanceName": "zyp004", "vpcId": "vpc- tx9evaxvf65gt95gb ****", "cidrBlock": "192.168.XX.XX/16 ", "description": ""}]} | The information about the vSwitches in the VPC. |

**Examples**

Sample requests

```
https://semawaf.[ RegionId].aliyuncs.com/?Action=DescribeVSwitch &RegionId=cn-hangzhou &VpcId=vpc-RSABVqbNiSs****
```

Sample success responses `XML` format

```json
<DescribeVSwitchResponse>
    <RequestId>53e59af3-3209-452a-853c-ac10ad815929</RequestId>
    <Result>{"vswitch_list": [{"instanceId": "vsw-tx9v9qpazlcdcc86f****",
"instanceName": "zyp004", "vpcId": "vpc-tx9evaxvf65gt95gb****", "cidrBlock": "192.168.X X.XX/16", "description": ""}]}</Result> </DescribeVSwitchResponse>
```

`JSON` format `{`

```json
  "RequestId":"53e59af3-3209-452a-853c-ac10ad815929",
  "Result":"{\"vswitch_list\": [{\"instanceId\": \"vsw-tx9v9qpazlcdcc86f****\", \"insta
nceName\": \"zyp004\", \"vpcId\": \"vpc-tx9evaxvf65gt95gb****\", \"cidrBlock\": \"192.1 68.XX.XX/16\", \"description\": \"\"}]}"
```

`}`

**Error codes**

For a list of error codes, see Error codes.

#### 4.2.15 DescribeVpcVip

Queries the information about the virtual IP addresses (VIPs) in a specific virtual private cloud (VPC).

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeVpcVi p | The operation that you want to perform. Set the value to DescribeVpcVip. |
| RegionId | String | Yes | cn-hangzhou |   |
| VpcId | String | Yes | vpc- RSABVqbNiSs* *** | The ID of the VPC. You can call the DescribeVpc operation to query the IDs of VPCs. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 53e59af3-3209- 452a-853c- ac10ad815929 | The ID of the request. |
| Result | String | {"items": [{"ip": "192.168.XX.XX", "type": " IP"}], "total": 1} | The information about the VIPs in the VPC. The information includes the following fields: items: the returned VIPs. Information about the VIPs: ip: the VIP in the VPC. type: the type of the return value. The field value is fixed as IP, which indicates a VIP. total: the total number of VIPs returned. |

**Examples**

Sample requests

```
https://semawaf.[ RegionId].aliyuncs.com/?Action=DescribeVpcVip &RegionId=cn-hangzhou &VpcId=vpc-RSABVqbNiSs****
```

Sample success responses `XML` format

```xml
<DescribeVpcVipResponse>
    <RequestId>53e59af3-3209-452a-853c-ac10ad815929</RequestId>
    <Result>{"items": [{"ip": "192.168.XX.XX", "type": " IP"}], "total": 1}</Result>
</DescribeVpcVipResponse>
```

`JSON` format `{`

```json
  "RequestId":"53e59af3-3209-452a-853c-ac10ad815929",
  "Result":"{\"items\": [{\"ip\": \"192.168.XX.XX\", \"type\": \" IP\"}], \"total\": 1}
```

`"` `}`

**Error codes**

For a list of error codes, see Error codes.

#### 4.2.16 CreateVpcVip

Creates a virtual IP address (VIP) in a specific virtual private cloud (VPC).

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateVpcVip | The operation that you want to perform. Set the value to CreateVpcVip. |
| RegionId | String | Yes | cn-hangzhou |   |
| VpcId | String | Yes | vpc- RSABVqbNiSs* *** | The ID of the VPC. You can call the DescribeVpc operation to query the IDs of VPCs. |
| VSwitchId | String | Yes | vsw- APUjoSJOoBw** ** | The ID of the vSwitch. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 53e59af3-3209- 452a-853c- ac10ad815929 | The ID of the request. |
| Result | String | {"ip": "192.168.XX.XX", "type": "intranet IP"} | The information about the created VIP. The type field indicates the type of the VIP. The field value is fixed as intranet IP, which indicates an internal IP address. |

**Examples**

Sample requests

```
https://semawaf.[ RegionId].aliyuncs.com/?Action=CreateVpcVip &RegionId=cn-hangzhou &VpcId=vpc-RSABVqbNiSs**** &VSwitchId=vsw-APUjoSJOoBw****
```

Sample success responses `XML` format

```xml
<CreateVpcVipResponse>
    <RequestId>53e59af3-3209-452a-853c-ac10ad815929</RequestId>
    <Result>{"ip": "192.168.XX.XX", "type": "intranet IP"}</Result>
</CreateVpcVipResponse>
```

`JSON` format `{`

```json
  "RequestId":"53e59af3-3209-452a-853c-ac10ad815929",
  "Result":"{\"ip\": \"192.168.XX.XX\", \"type\": \"intranet IP\"}"
```

`}`

**Error codes**

For a list of error codes, see Error codes.

#### 4.2.17 DeleteVpcVip

Deletes a virtual IP address (VIP) in a specific virtual private cloud (VPC).

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteVpcVip | The operation that you want to perform. Set the value to DeleteVpcVip. |
| RegionId | String | Yes | cn-hangzhou |   |
| VpcId | String | Yes | vpc- RSABVqbNiSs* *** | The ID of the VPC. You can call the DescribeVpc operation to query the IDs of VPCs. |
| Vip | String | Yes | 10.10.XX.XX | The VIP in the VPC. You can call the DescribeVpcVip operation to query the VIPs in a specific VPC. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 53e59af3-3209- 452a-853c- ac10ad815929 | The ID of the request. |
| Result | String | None | The returned information. If the call is successful, this value is empty. |

**Examples**

Sample requests

```
https://semawaf.[ RegionId].aliyuncs.com/?Action=DeleteVpcVip &RegionId=cn-hangzhou &VpcId=vpc-RSABVqbNiSs**** &Vip=10.10.XX.XX
```

Sample success responses `XML` format

```xml
<DeleteVpcVipResponse>
    <RequestId>53e59af3-3209-452a-853c-ac10ad815929</RequestId>
    <Result></Result>
</DeleteVpcVipResponse>
```

`JSON` format `{`

```json
  "RequestId":"53e59af3-3209-452a-853c-ac10ad815929",
  "Result":""
```

`}`

**Error codes**

For a list of error codes, see Error codes.

#### 4.2.18 DescribeEcs

Queries the information about the Elastic Compute Service (ECS) instances in a specific virtual private cloud (VPC).

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeEcs | The operation that you want to perform. Set the value to DescribeEcs. |
| RegionId | String | Yes | cn-hangzhou |   |

| VpcId | String | Yes | vpc- RSABVqbNiSs* *** | The ID of the VPC. You can call the DescribeVpc operation to query the IDs of VPCs. |
|---|---|---|---|---|

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 53e59af3-3209- 452a-853c- ac10ad815929 | The ID of the request. |
| Result | String | {"ecs": [{"instanceId": "i- tx905fcsw7erxzox* ***", "instanceName": "ecs****", "internetIp": "", "intranetIp": "192.168.XX.XX", "eip": "", "natIp": "6.6.XX.XX", "status": "Running", "networkType": "vpc", "vpcId": "vpc- tx94ktgeqccd7l98c ****", "vswitchId": "vsw- tx9vktwbt8w3vw6w h****", "securityGroupId": "sg- tx9aps47sy596qwj ****", "hostName": "iZtx905fcsw7erxz oxa****", "osType": "CentOS 7.2", "createTime": 1588838676000}] } | The information about the ECS instances in the VPC. |

**Examples**

Sample requests

```
https://semawaf.[ RegionId].aliyuncs.com/?Action=DescribeEcs &RegionId=cn-hangzhou &VpcId=vpc-RSABVqbNiSs****
```

Sample success responses `XML` format

```xml
<DescribeEcsResponse>
    <RequestId>53e59af3-3209-452a-853c-ac10ad815929</RequestId>
    <Result>{"ecs": [{"instanceId": "i-tx905fcsw7erxzox****", "instanceName": "ecs****"
, "internetIp": "", "intranetIp": "192.168.XX.XX", "eip": "", "natIp": "6.6.XX.XX", "st atus": "Running", "networkType": "vpc", "vpcId": "vpc-tx94ktgeqccd7l98c****", "vswitchI d": "vsw-tx9vktwbt8w3vw6wh****", "securityGroupId": "sg-tx9aps47sy596qwj****", "hostNam e": "iZtx905fcsw7erxzoxa****", "osType": "CentOS 7.2", "createTime": 1588838676000}]}</ Result> </DescribeEcsResponse>
```

`JSON` format `{`

```json
  "RequestId":"53e59af3-3209-452a-853c-ac10ad815929",
  "Result":"{\"ecs\": [{\"instanceId\": \"i-tx905fcsw7erxzox****\", \"instanceName\": \
"ecs****\", \"internetIp\": \"\", \"intranetIp\": \"192.168.XX.XX\", \"eip\": \"\", \"n atIp\": \"6.6.XX.XX\", \"status\": \"Running\", \"networkType\": \"vpc\", \"vpcId\": \" vpc-tx94ktgeqccd7l98c****\", \"vswitchId\": \"vsw-tx9vktwbt8w3vw6wh****\", \"securityGroupId\": \"sg-tx9aps47sy596qwj****\", \"hostName\": \"iZtx905fcsw7erxzoxa****\", \"osType\": \"CentOS 7.2\", \"createTime\": 1588838676000}]}"
```

`}`

**Error codes**

For a list of error codes, see Error codes.

#### 4.2.19 DescribeSlb

Queries the information about the Server Load Balancer (SLB) instances in a specific virtual private cloud (VPC).

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeSlb | The operation that you want to perform. Set the value to DescribeSlb. |
| RegionId | String | Yes | cn-hangzhou |   |
| VpcId | String | Yes | vpc- RSABVqbNiSs* *** | The ID of the VPC. You can call the DescribeVpc operation to query the IDs of VPCs. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|

| RequestId | String | 53e59af3-3209- 452a-853c- ac10ad815929 | The ID of the request. |
|---|---|---|---|
| Result | String | {"slb": [{"instanceId": "slb- tx9n49pigmazoow 4h****", "instanceName": "waf****", "status": "active", "networkType": "intranet", "ip": "192.168.XX.XX", "ipVersion": "ipv4"}]} | The information about the SLB instances in the VPC. |

**Examples**

Sample requests

```
https://semawaf.[ RegionId].aliyuncs.com/?Action=DescribeSlb &RegionId=cn-hangzhou &VpcId=vpc-RSABVqbNiSs****
```

Sample success responses `XML` format

```xml
<DescribeSlbResponse>
    <RequestId>53e59af3-3209-452a-853c-ac10ad815929</RequestId>
    <Result>{"slb": [{"instanceId": "slb-tx9n49pigmazoow4h****", "instanceName": "waf**
**", "status": "active", "networkType": "intranet", "ip": "192.168.XX.XX", "ipVersion":
"ipv4"}]}</Result> </DescribeSlbResponse>
```

`JSON` format `{`

```json
  "RequestId":"53e59af3-3209-452a-853c-ac10ad815929",
  "Result":"{\"slb\": [{\"instanceId\": \"slb-tx9n49pigmazoow4h****\",
\"instanceName\": \"waf****\", \"status\": \"active\", \"networkType\": \"intranet\", \ "ip\": \"192.168.XX.XX\", \"ipVersion\": \"ipv4\"}]}"
```

`}`

**Error codes**

For a list of error codes, see Error codes.

### 4.3 HTTP flood protection rules

#### 4.3.1 DescribeCCRuleTemplate

Queries the information about HTTP flood protection rules.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeCCRul eTemplate | The operation that you want to perform. Set the value to DescribeCCRuleTemplate. |
| RegionId | String | Yes | cn-hangzhou |   |
| Id | Integer | No | 1 | The ID of the HTTP flood protection rule. |
| PageSize | Integer | No | 10 | The number of entries to return on each page. Default value: 10. |
| PageNumber | Integer | No | 1 | The number of the page to return. Default value: 1. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 53e59af3-3209- 452a-853c- ac10ad815929 | The ID of the request. |
| Result | String | {"items": [{"id": 1, "name": "cc-policy- test", "version": 40, "is enabled": _ true, "match method": _ {"target type": _ "CIDR", "period": null, "limit": null, "scope": "URL Prefix", "policy": "www.taobao.com" , "scheme": "http"}, "action": {"action": "forbid"}, "create time": _ "1594627307", "expire period": _ 10, "execution number _ ": 0, "template type": _ "manual", "is inaccurate": _ false, "dry run": _ false}], "total": 1} | The returned result of the request. For more information about the match method parameter in the _ returned result, see the description of MatchMethod in CreateCCRuleTemplate. |

**Examples**

Sample requests

```
https://semawaf.[ RegionId].aliyuncs.com/?Action=DescribeCCRuleTemplate &RegionId=cn-hangzhou &Id=1 &PageSize=20 &PageNumber=1
```

Sample success responses `XML` format

```xml
<DescribeCCRuleTemplateResponse>
    <RequestId>53e59af3-3209-452a-853c-ac10ad815929</RequestId>
    <Result>{"items": [{"id": 1, "name": "cc-policy-test", "version": 40, "is_enabled":
true, "match_method": {"target_type": "CIDR", "period": null, "limit": null, "scope": " URL Prefix", "policy": "www.taobao.com", "scheme": "http"}, "action": {"action": "forbi d"}, "create_time": "1594627307", "expire_period": 10, "execution_number": 0, "template _type": "manual", "is_inaccurate": false, "dry_run": false}], "total": 1}</Result> </DescribeCCRuleTemplateResponse>
```

`JSON` format `{`

```json
  "RequestId":"53e59af3-3209-452a-853c-ac10ad815929",
  "Result":"{\"items\": [{\"id\": 1, \"name\": \"cc-policy-test\", \"version\": 40, \"i
s_enabled\": true, \"match_method\": {\"target_type\": \"CIDR\", \"period\": null, \"li mit\": null, \"scope\": \"URL Prefix\", \"policy\": \"www.taobao.com\", \"scheme\": \"h ttp\"}, \"action\": {\"action\": \"forbid\"}, \"create_time\": \"1594627307\", \"expire _period\": 10, \"execution_number\": 0, \"template_type\": \"manual\", \"is_inaccurate\": false, \"dry_run\": false}], \"total\": 1}"
```

`}`

**Error codes**

For a list of error codes, see Error codes.

#### 4.3.2 CreateCCRuleTemplate

Creates an HTTP flood protection rule.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateCCRuleT emplate | The operation that you want to perform. Set the value to CreateCCRuleTemplate. |
| RegionId | String | Yes | cn-hangzhou |   |
| Name | String | Yes | cc-rule-1 | The name of the HTTP flood protection rule. |

| TemplateTyp e | String | Yes | auto | The type of the rule. Valid values: manual: limits requests based on specific IP addresses or sessions. auto: limits requests that meet specific conditions. |
|---|---|---|---|---|
| Enable | Boolean | No | true | Specifies whether to enable the rule. Default value: true. Valid values: true: enables the HTTP flood protection rule. false: disables the HTTP flood protection rule. |
| RuleMode | Boolean | No | false | The mode of the rule. Default value: false. Valid values: true: monitors specific requests. false: blocks specific requests. |
| RuleList | RepeatList | No | ["192.168.XX.X X", "192.168.XX.X X/24"] | The IP addresses, classless inter- domain routing (CIDR) blocks, or sessions. If you set TemplateType to manual to limit requests from known sources, this parameter is required |
| RuleAction | Json | Yes | {"action":"forbi d","limit rate li _ _ mit":1,"limit ra _ te period":5} _ | The action on requests. This parameter is a string consisting of JSON structs. A JSON struct includes the following fields: action: the action on the requests. This field is required. Data type: string. Valid values: forbid and Limit Rate. The value forbid indicates that the system blocks requests. The value Limit Rate indicates that the system limits the number of requests to handle over a specific period. limit rate limit: the number _ _ of requests to handle over a specific period. If you set action to Limit Rate, this field is required. Data type: integer. Valid values: any non-zero positive integer. limit rate period: the period _ _ in which the system limits the number of requests to handle. If you set action to Limit Rate, this field is required. Data type: integer. Valid values: any non- zero positive integer. |

| FuzzyCount | Boolean | No | false | The statistical aggregation method to count requests. Default value: false. Valid values: true: counts requests with the most occurrence. false: counts all requests. |
|---|---|---|---|---|
| MatchMethod | Json | Yes | {"scope":"URL Prefix","limit":" 10","period":5, "target type":" _ CIDR","policy": "www.aliyun.co m","scheme":" http"} | The match conditions. This parameter is a string consisting of JSON structs. A JSON struct includes the following fields: scope :the statistical aggregation method to count requests. This field is required. Data type: string. Valid values: URL Prefix, URL, and All. The value URL Prefix indicates that the requests containing the specific URL prefix are counted. The value URL indicates that the requests containing the specific URL are counted. The value All indicates that all requests are counted. limit: the number of requests to handle over a specific period. If you set RuleAction.action to Limit Rate, this field is required. Data type: integer. Valid values: any non-zero positive integer. period: the period in which the system limits the number of requests to handle. If you set RuleAction.action to Limit Rate, this field is required. Data type: integer. Valid values: any non-zero positive integer. target type: the object type _ based on which the system limits requests. This field is required. Data type: string. Valid values: CIDR and Session. policy: the URL or URL prefix based on which requests are counted. If you set scope to URL Prefix or URL, this field is required. policy: the scheme based on which requests are counted. If you set scope to URL Prefix or URL, this field is required. Valid values: http and https. |
| ExpirePeriod | Integer | No | 86400 | The validity period after the rule is triggered. Unit: seconds. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 53e59af3-3209- 452a-853c- ac10ad815929 | The ID of the request. |
| TaskStatus | Struct |   | The returned information. |
| └TaskId | String | c68646a1-58f8- 4b75-828a- a2d3b19b382a | The ID of the task. The ID of the task. |
| └Time | String | 1593593692 | The time when the task status message was generated. This value is a UNIX timestamp representing the number of seconds that have elapsed since the epoch time January 1, 1970, 00:00:00 UTC. |
| └TaskList | String | ["Website-related configuration generation", "Policy-related configuration generation"] | The descriptions of the task. This value is returned only for asynchronous tasks. |
| └StatusMess age | String | The configuration is in effect. | The status message of the task. You can ignore this reserved parameter. |
| └SuccessCod e | String | 1 | The status code of the task. Valid values: 0: The task fails. 1: The task is successful. 2: The task is not started. |
| └Result | String | {"id": 17, "name": "test-cc-rule-1", "version": 65, "is enabled": true, _ "match method": _ {"target type": _ "CIDR", "period": 5, "limit": 5, "scope": "All"}, "action": {"action": "forbid"}, "create time": _ "1598337034", "expire period": _ null, "execution number _ ": 0, "template type": _ "auto", "is inaccurate": _ false, "dry run": _ false} | The returned result of the request. |

**Examples**

Sample requests

```
https://semawaf.[ RegionId].aliyuncs.com/?Action=CreateCCRuleTemplate &RegionId=cn-hangzhou &Name=cc-rule-1 &TemplateType=auto &Enable=true &RuleMode=true &RuleList.1=192.168.XX.XX &RuleAction={"action":"forbid","limit_rate_limit":1,"limit_rate_period":5} &FuzzyCount=true &MatchMethod={"scope":"URL Prefix","limit":"10","period":5,"target_type":"CIDR","policy":"www.aliyun.com","scheme":" tp"} &ExpirePeriod=86400
```

Sample success responses `XML` format

```json
<CreateCCRuleTemplateResponse>
    <RequestId>53e59af3-3209-452a-853c-ac10ad815929</RequestId>
    <TaskStatus>
        <TaskId>c68646a1-58f8-4b75-828a-a2d3b19b382a</TaskId>
        <Time>1593593692</Time>
        <TaskList>["Website-related configuration generation", "Policy-related
configuration generation"]</TaskList>
        <StatusMessage>The configuration is in effect.</StatusMessage>
        <SuccessCode>1</SuccessCode>
        <Result>{"id": 17, "name": "test-cc-rule-1", "version": 65, "is_enabled": true,
"match_method": {"target_type": "CIDR", "period": 5, "limit": 5, "scope": "All"}, "acti on": {"action": "forbid"}, "create_time": "1598337034", "expire_period": null, "executi on_number": 0, "template_type": "auto", "is_inaccurate": false, "dry_run": false}</Resu lt>
    </TaskStatus>
</CreateCCRuleTemplateResponse>
```

`JSON` format `{`

```json
  "RequestId":"53e59af3-3209-452a-853c-ac10ad815929",
  "TaskStatus":{
    "TaskId":"c68646a1-58f8-4b75-828a-a2d3b19b382a",
    "TaskList":"[\"Website-related configuration generation\", \"Policy-related
configuration generation\"]",
    "SuccessCode":"1",
    "Time":"1593593692",
    "StatusMessage":"The configuration is in effect.",
    "Result":"{\"id\": 17, \"name\": \"test-cc-rule-1\", \"version\": 65,
\"is_enabled\": true, \"match_method\": {\"target_type\": \"CIDR\", \"period\": 5, \"li mit\": 5, \"scope\": \"All\"}, \"action\": {\"action\": \"forbid\"}, \"create_time\": \ "1598337034\", \"expire_period\": null, \"execution_number\": 0, \"template_type\": \"a uto\", \"is_inaccurate\": false, \"dry_run\": false}"
```

`}` `}`

**Error codes**

For a list of error codes, see Error codes.

#### 4.3.3 EditCCRuleTemplate

Modifies a specific HTTP flood protection rule.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | EditCCRuleTem plate | The operation that you want to perform. Set the value to EditCCRuleTemplate. |
| RegionId | String | Yes | cn-hangzhou |   |
| Id | Integer | No | 1 | The ID of the HTTP flood protection rule. You can call the DescribeCCRuleTemplate operation to query the IDs of HTTP flood protection rules. |
| Name | String | Yes | cc-rule-1 | The name of the HTTP flood protection rule. |
| Enable | Boolean | No | true | Specifies whether to enable the rule. Default value: true. Valid values: true: enables the HTTP flood protection rule. false: disables the HTTP flood protection rule. |
| RuleMode | Boolean | No | false | The mode of the rule. Default value: false. Valid values: true: monitors specific requests. false: blocks specific requests. |

| RuleAction | Json | Yes | {"action":"forbi d","limit rate li _ _ mit":1,"limit ra _ te period":5} _ | The action on requests. This parameter is a string consisting of JSON structs. A JSON struct includes the following fields: action: the action on the requests. This field is required. Data type: string. Valid values: forbid and Limit Rate. The value forbid indicates that the system blocks requests. The value Limit Rate indicates that the system limits the number of requests to handle over a specific period. limit rate limit: the number _ _ of requests to handle over a specific period. If you set action to Limit Rate, this field is required. Data type: integer. Valid values: any non-zero positive integer. limit rate period: the period _ _ in which the system limits the number of requests to handle. If you set action to Limit Rate, this field is required. Data type: integer. Valid values: any non- zero positive integer. |
|---|---|---|---|---|
| FuzzyCount | Boolean | No | false | The statistical aggregation method to count requests. Default value: false. Valid values: true: counts requests with the most occurrence. false: counts all requests. |

| MatchMethod | Json | Yes | {"scope":"URL Prefix","limit":" 10","period":5, "target type":" _ CIDR","policy": "www.aliyun.co m","scheme":" http"} | The match conditions. This parameter is a string consisting of JSON structs. A JSON struct includes the following fields: scope :the statistical aggregation method to count requests. This field is required. Data type: string. Valid values: URL Prefix, URL, and All. The value URL Prefix indicates that the requests containing the specific URL prefix are counted. The value URL indicates that the requests containing the specific URL are counted. The value All indicates that all requests are counted. limit: the number of requests to handle over a specific period. If you set RuleAction.action to Limit Rate, this field is required. Data type: integer. Valid values: any non-zero positive integer. period: the period in which the system limits the number of requests to handle. If you set RuleAction.action to Limit Rate, this field is required. Data type: integer. Valid values: any non-zero positive integer. target type: the object type _ based on which the system limits requests. This field is required. Data type: string. Valid values: CIDR and Session. policy: the URL or URL prefix based on which requests are counted. If you set scope to URL Prefix or URL, this field is required. policy: the scheme based on which requests are counted. If you set scope to URL Prefix or URL, this field is required. Valid values: http and https. |
|---|---|---|---|---|
| ExpirePeriod | Integer | No | 86400 | The validity period after the rule is triggered. Unit: seconds. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 53e59af3-3209- 452a-853c- ac10ad815929 | The ID of the request. |
| TaskStatus | Struct |   |   |

| └TaskId | String | c68646a1-58f8- 4b75-828a- a2d3b19b382a | The ID of the task. |
|---|---|---|---|
| └Time | String | 1593593692 | The time when the task status message was generated. This value is a UNIX timestamp representing the number of seconds that have elapsed since the epoch time January 1, 1970, 00:00:00 UTC. |
| └TaskList | String | ["Website-related configuration generation", "Policy-related configuration generation"] | The descriptions of the task. This value is returned only for asynchronous tasks. |
| └StatusMess age | String | The configuration is in effect. | The status message of the task. You can ignore this reserved parameter. |
| └SuccessCod e | String | 1 | The status code of the task. Valid values: 0: The task fails. 1: The task is successful. 2: The task is not started. |
| └Result | String | {"id": 1, "name": "test-cc-rule-1", "version": 65, "is enabled": true, _ "match method": _ {"target type": _ "CIDR", "period": 5, "limit": 5, "scope": "All"}, "action": {"action": "forbid"}, "create time": _ "1598337034", "expire period": _ null, "execution number _ ": 0, "template type": _ "auto", "is inaccurate": _ false, "dry run": _ false} | The returned result of the request. |

**Examples**

Sample requests

```
https://semawaf.[ RegionId].aliyuncs.com/?Action=EditCCRuleTemplate &RegionId=cn-hangzhou &Id=1 &Name=cc-rule-1 &Enable=true &RuleMode=true &RuleAction={"action":"forbid","limit_rate_limit":1,"limit_rate_period":5} &FuzzyCount=true &MatchMethod={"scope":"URL Prefix","limit":"10","period":5,"target_type":"CIDR","policy":"www.aliyun.com","scheme":" tp"} &ExpirePeriod=86400
```

Sample success responses `XML` format

```json
<EditCCRuleTemplateResponse>
    <RequestId>53e59af3-3209-452a-853c-ac10ad815929</RequestId>
    <TaskStatus>
        <TaskId>c68646a1-58f8-4b75-828a-a2d3b19b382a</TaskId>
        <Time>1593593692</Time>
        <TaskList>["Website-related configuration generation", "Policy-related
configuration generation"]</TaskList>
        <StatusMessage>The configuration is in effect.</StatusMessage>
        <SuccessCode>1</SuccessCode>
        <Result>{"id": 1, "name": "test-cc-rule-1", "version": 65, "is_enabled": true,
"match_method": {"target_type": "CIDR", "period": 5, "limit": 5, "scope": "All"}, "acti on": {"action": "forbid"}, "create_time": "1598337034", "expire_period": null, "executi on_number": 0, "template_type": "auto", "is_inaccurate": false, "dry_run": false}</Resu lt>
    </TaskStatus>
</EditCCRuleTemplateResponse>
```

`JSON` format `{`

```json
  "RequestId":"53e59af3-3209-452a-853c-ac10ad815929",
  "TaskStatus":{
    "TaskId":"c68646a1-58f8-4b75-828a-a2d3b19b382a",
    "TaskList":"[\"Website-related configuration generation\", \"Policy-related
configuration generation\"]",
    "SuccessCode":"1",
    "Time":"1593593692",
    "StatusMessage":"The configuration is in effect.",
    "Result":"{\"id\": 1, \"name\": \"test-cc-rule-1\", \"version\": 65,
\"is_enabled\": true, \"match_method\": {\"target_type\": \"CIDR\", \"period\": 5, \"li mit\": 5, \"scope\": \"All\"}, \"action\": {\"action\": \"forbid\"}, \"create_time\": \ "1598337034\", \"expire_period\": null, \"execution_number\": 0, \"template_type\": \"a uto\", \"is_inaccurate\": false, \"dry_run\": false}"
```

`}` `}`

**Error codes**

For a list of error codes, see Error codes.

#### 4.3.4 ToggleCCRuleTemplate

Enables or disables a specific HTTP flood protection rule.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ToggleCCRuleTe mplate | The operation that you want to perform. Set the value to ToggleCCRuleTemplate. |
| RegionId | String | Yes | cn-hangzhou |   |
| IdList | RepeatL ist | Yes | [1, 2] | The ID of the HTTP flood protection rule. You can enter multiple IDs. You can call the DescribeCCRuleTemplate operation to query the IDs of HTTP flood protection rules. |
| ToggleAction | String | Yes | disable | Specifies the status of the HTTP flood protection rule. Valid values: enable disable |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 53e59af3-3209- 452a-853c- ac10ad815929 | The ID of the request. |
| TaskStatus | Struct |   |   |
| └TaskId | String | c68646a1-58f8- 4b75-828a- a2d3b19b382a | The ID of the task. |
| └Time | String | 1593593692 | The time when the task status message was generated. This value is a UNIX timestamp representing the number of seconds that have elapsed since the epoch time January 1, 1970, 00:00:00 UTC. |
| └TaskList | String | ["Website-related configuration generation", "Policy-related configuration generation"] | The descriptions of the task. This value is returned only for asynchronous tasks. |

| └StatusMess age | String | The configuration is in effect. | The status message of the task. You can ignore this reserved parameter. |
|---|---|---|---|
| └SuccessCod e | String | 1 | The status code of the task. Valid values: 0: The task fails. 1: The task is successful. 2: The task is not started. |

**Examples**

Sample requests

```
https://semawaf.[ RegionId].aliyuncs.com/?Action=ToggleCCRuleTemplate &RegionId=cn-hangzhou &IdList.1=1 &ToggleAction=disable
```

Sample success responses `XML` format

```xml
<ToggleCCRuleTemplateResponse>
    <RequestId>53e59af3-3209-452a-853c-ac10ad815929</RequestId>
    <TaskStatus>
        <TaskId>c68646a1-58f8-4b75-828a-a2d3b19b382a</TaskId>
        <Time>1593593692</Time>
        <TaskList>["Website-related configuration generation", "Policy-related
configuration generation"]</TaskList>
        <StatusMessage>The configuration is in effect.</StatusMessage>
        <SuccessCode>1</SuccessCode>
    </TaskStatus>
</ToggleCCRuleTemplateResponse>
```

`JSON` format `{`

```json
  "RequestId":"53e59af3-3209-452a-853c-ac10ad815929",
  "TaskStatus":{
    "TaskId":"c68646a1-58f8-4b75-828a-a2d3b19b382a",
    "TaskList":"[\"Website-related configuration generation\", \"Policy-related
configuration generation\"]",
    "SuccessCode":"1",
    "Time":"1593593692",
    "StatusMessage":"The configuration is in effect."
```

`}` `}`

**Error codes**

For a list of error codes, see Error codes.

#### 4.3.5 DeleteCCRuleTemplate

Deletes a specific HTTP flood protection rule.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteCCRuleTe mplate | The operation that you want to perform. Set the value to DeleteCCRuleTemplate. |
| RegionId | String | Yes | cn-hangzhou |   |
| IdList | RepeatL ist | Yes | [1, 2] | The ID of the HTTP flood protection rule. You can enter multiple IDs. You can call the DescribeCCRuleTemplate operation to query the IDs of HTTP flood protection rules. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 53e59af3-3209- 452a-853c- ac10ad815929 | The ID of the request. |
| TaskStatus | Struct |   |   |
| └TaskId | String | c68646a1-58f8- 4b75-828a- a2d3b19b382a | The ID of the task. |
| └Time | String | 1593593692 | The time when the task status message was generated. This value is a UNIX timestamp representing the number of seconds that have elapsed since the epoch time January 1, 1970, 00:00:00 UTC. |
| └TaskList | String | ["Website-related configuration generation", "Policy-related configuration generation"] | The descriptions of the task. This value is returned only for asynchronous tasks. |
| └StatusMess age | String | The configuration is in effect. | The status message of the task. You can ignore this reserved parameter. |

| └SuccessCod e | String | 1 | The status code of the task. Valid values: 0: The task fails. 1: The task is successful. 2: The task is not started. |
|---|---|---|---|

**Examples**

Sample requests

```
https://semawaf.[ RegionId].aliyuncs.com/?Action=DeleteCCRuleTemplate &RegionId=cn-hangzhou &IdList.1=1
```

Sample success responses `XML` format

```xml
<DeleteCCRuleTemplateResponse>
    <RequestId>53e59af3-3209-452a-853c-ac10ad815929</RequestId>
    <TaskStatus>
        <TaskId>c68646a1-58f8-4b75-828a-a2d3b19b382a</TaskId>
        <Time>1593593692</Time>
        <TaskList>["Website-related configuration generation", "Policy-related
configuration generation"]</TaskList>
        <StatusMessage>The configuration is in effect.</StatusMessage>
        <SuccessCode>1</SuccessCode>
    </TaskStatus>
</DeleteCCRuleTemplateResponse>
```

`JSON` format `{`

```json
  "RequestId":"53e59af3-3209-452a-853c-ac10ad815929",
  "TaskStatus":{
    "TaskId":"c68646a1-58f8-4b75-828a-a2d3b19b382a",
    "TaskList":"[\"Website-related configuration generation\", \"Policy-related
configuration generation\"]",
    "SuccessCode":"1",
    "Time":"1593593692",
    "StatusMessage":"The configuration is in effect."
```

`}` `}`

**Error codes**

For a list of error codes, see Error codes.

#### 4.3.6 ClearCCRestrictionList

Removes the restricted users in a specific HTTP flood protection rule.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ClearCCRestricti onList | The operation that you want to perform. Set the value to ClearCCRestrictionList. |
| RegionId | String | Yes | cn-hangzhou |   |
| CCRuleTempla teId | Integer | Yes | 35 | The ID of the HTTP flood protection rule. You can call the DescribeCCRuleTemplate operation to query the IDs of HTTP flood protection rules. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 53e59af3-3209- 452a-853c- ac10ad815929 | The ID of the request. |
| TaskStatus | Struct |   |   |
| └TaskId | String | c68646a1-58f8- 4b75-828a- a2d3b19b382a | The ID of the task. |
| └Time | String | 1593593692 | The time when the task status message was generated. This value is a UNIX timestamp representing the number of seconds that have elapsed since the epoch time January 1, 1970, 00:00:00 UTC. |
| └TaskList | String | ["Website-related configuration generation", "Policy-related configuration generation"] | The descriptions of the task. This value is returned only for asynchronous tasks. |
| └StatusMess age | String | The configuration is in effect. | The status message of the task. You can ignore this reserved parameter. |
| └SuccessCod e | String | 1 | The status code of the task. Valid values: 0: The task fails. 1: The task is successful. 2: The task is not started. |

**Examples**

Sample requests

```
https://semawaf.[ RegionId].aliyuncs.com/?Action=ClearCCRestrictionList &RegionId=cn-hangzhou &CCRuleTemplateId=35
```

Sample success responses `XML` format

```xml
<ClearCCRestrictionListResponse>
    <RequestId>53e59af3-3209-452a-853c-ac10ad815929</RequestId>
    <TaskStatus>
        <TaskId>c68646a1-58f8-4b75-828a-a2d3b19b382a</TaskId>
        <Time>1593593692</Time>
        <TaskList>["Website-related configuration generation", "Policy-related
configuration generation"]</TaskList>
        <StatusMessage>The configuration is in effect.</StatusMessage>
        <SuccessCode>1</SuccessCode>
    </TaskStatus>
</ClearCCRestrictionListResponse>
```

`JSON` format `{`

```json
  "RequestId":"53e59af3-3209-452a-853c-ac10ad815929",
  "TaskStatus":{
    "TaskId":"c68646a1-58f8-4b75-828a-a2d3b19b382a",
    "TaskList":"[\"Website-related configuration generation\", \"Policy-related
configuration generation\"]",
    "SuccessCode":"1",
    "Time":"1593593692",
    "StatusMessage":"The configuration is in effect."
```

`}` `}`

**Error codes**

For a list of error codes, see Error codes.

#### 4.3.7 DescribeCCWhitelist

Queries the information about HTTP flood protection whitelists.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeCCWhi telist | The operation that you want to perform. Set the value to DescribeCCWhitelist. |
| RegionId | String | Yes | cn-hangzhou |   |
| Id | Integer | No | 1 | The ID of the HTTP flood protection whitelist. |

| PageSize | Integer | No | 10 | The number of entries to return on each page. Default value: 10. |
|---|---|---|---|---|
| PageNumber | Integer | No | 1 | The number of the page to return. Default value: 1. |
| TargetTypeFi lter | RepeatList | No | ["CIDR", "Session"] | The type to filter whitelists. You can enter multiple types. Valid values: CIDR Session |
| CommentFilt er | RepeatList | No | ["cc-whitelist- 1", "cc- whitelist-2"] | The remarks to filter whitelists. You can enter multiple remarks. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 53e59af3-3209- 452a-853c- ac10ad815929 | The ID of the request. |
| Result | String | {"items": [{"id": 5, "target": "10.12.XX.XX", "target type": _ "CIDR", "target ip group": _ _ null, "comment": "", "create time": _ "1594627457"}], "total": 1} |   |

**Examples**

Sample requests

```
https://semawaf.[RegionId].aliyuncs.com/?Action=DescribeCCWhitelist &RegionId=cn-hangzhou &PageSize=10 &PageNumber=1 &TargetTypeFilter.1=CIDR &CommentFilter.1=cc-whitelist-1
```

Sample success responses `XML` format

```xml
<DescribeCCWhitelistResponse>
    <RequestId>53e59af3-3209-452a-853c-ac10ad815929</RequestId>
    <Result>{"items": [{"id": 5, "target": "10.12.XX.XX", "target_type": "CIDR", "targe
t_ip_group": null, "comment": "", "create_time": "1594627457"}], "total": 1}</Result> </DescribeCCWhitelistResponse>
```

`JSON` format

|   | { "RequestId":"53e59af3-3209-452a-853c-ac10ad815929", "Result":"{\"items\": [{\"id\": 5, \"target\": \"10.12.XX.XX\", \"target type\": \"CI _ DR\", \"target ip group\": null, \"comment\": \"\", \"create time\": \"1594627457\"}], _ _ _ \"total\": 1}" } |
|---|---|

**Error codes**

For a list of error codes, see Error codes.

#### 4.3.8 CreateCCWhitelist

Creates an HTTP flood protection whitelist.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateCCWhite list | The operation that you want to perform. Set the value to CreateCCWhitelist. |
| RegionId | String | Yes | cn-hangzhou |   |
| TargetType | String | Yes | auto | The type of the HTTP flood protection whitelist. Valid values: CIDR Session |
| Comment | String | Yes | Whitelist- 192168100200 | The remarks of the whitelist. |
| TargetList | RepeatList | Yes | ["10.10.XX.XX" , "10.10.XX.XX/2 4"] | The IP address, CIDR block, or session in the whitelist. You can enter multiple IP addresses, CIDR blocks, or sessions. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 53e59af3-3209- 452a-853c- ac10ad815929 | The ID of the request. |
| TaskStatus | Struct |   | The returned information. |
| └TaskId | String | c68646a1-58f8- 4b75-828a- a2d3b19b382a | The ID of the task. The ID of the task. |

| └Time | String | 1593593692 | The time when the task status message was generated. This value is a UNIX timestamp representing the number of seconds that have elapsed since the epoch time January 1, 1970, 00:00:00 UTC. |
|---|---|---|---|
| └TaskList | String | ["Website-related configuration generation", "Policy-related configuration generation"] | The descriptions of the task. This value is returned only for asynchronous tasks. |
| └StatusMess age | String | The configuration is in effect. | The status message of the task. You can ignore this reserved parameter. |
| └SuccessCod e | String | 1 | The status code of the task. Valid values: 0: The task fails. 1: The task is successful. 2: The task is not started. |
| └Result | String | [{"id": null, "target": "10.10.XX.XX", "target type": _ "CIDR", "target ip group": _ _ null, "comment": "", "create time": _ "1598337455"}] | The information about the created whitelist. |

**Examples**

Sample requests

```
https://semawaf.[ RegionId].aliyuncs.com/?Action=CreateCCWhitelist &RegionId=cn-hangzhou &TargetType=CIDR &Comment=Whitelist-192168100200 &TargetList.1=10.10.XX.XX
```

Sample success responses `XML` format

```json
<CreateCCWhitelistResponse>
    <RequestId>53e59af3-3209-452a-853c-ac10ad815929</RequestId>
    <TaskStatus>
        <TaskId>c68646a1-58f8-4b75-828a-a2d3b19b382a</TaskId>
        <Time>1593593692</Time>
        <TaskList>["Website-related configuration generation", "Policy-related
configuration generation"]</TaskList>
        <StatusMessage>The configuration is in effect.</StatusMessage>
        <SuccessCode>1</SuccessCode>
        <Result>[{"id": null, "target": "10.10.XX.XX", "target_type": "CIDR",
"target_ip_group": null, "comment": "", "create_time": "1598337455"}]</Result>
    </TaskStatus>
</CreateCCWhitelistResponse>
```

`JSON` format `{`

```json
  "RequestId":"53e59af3-3209-452a-853c-ac10ad815929",
  "TaskStatus":{
    "TaskId":"c68646a1-58f8-4b75-828a-a2d3b19b382a",
    "TaskList":"[\"Website-related configuration generation\", \"Policy-related
configuration generation\"]",
    "SuccessCode":"1",
    "Time":"1593593692",
    "StatusMessage":"The configuration is in effect.",
    "Result":"[{\"id\": null, \"target\": \"10.10.XX.XX\", \"target_type\": \"CIDR\", \
"target_ip_group\": null, \"comment\": \"\", \"create_time\": \"1598337455\"}]"
```

`}` `}`

**Error codes**

For a list of error codes, see Error codes.

#### 4.3.9 DeleteCCWhitelist

Deletes a specific HTTP flood protection whitelist.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteCCWhite list | The operation that you want to perform. Set the value to DeleteCCWhitelist. |
| RegionId | String | Yes | cn-hangzhou |   |

| IdList | RepeatList | Yes | [1, 2] | The ID of the HTTP flood protection whitelist. You can enter multiple IDs. You can call the DescribeCCWhitelist operation to query the IDs of HTTP flood protection whitelists. |
|---|---|---|---|---|

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 53e59af3-3209- 452a-853c- ac10ad815929 | The ID of the request. |
| TaskStatus | Struct |   |   |
| └TaskId | String | c68646a1-58f8- 4b75-828a- a2d3b19b382a | The ID of the task. The ID of the task. |
| └Time | String | 1593593692 | The time when the task status message was generated. This value is a UNIX timestamp representing the number of seconds that have elapsed since the epoch time January 1, 1970, 00:00:00 UTC. |
| └TaskList | String | ["Generated website configurations", "Generated policy configurations"] | The descriptions of the task. This value is returned only for asynchronous tasks. |
| └StatusMess age | String | The configuration is in effect. | The status message of the task. You can ignore this reserved parameter. |
| └SuccessCod e | String | 1 | The status code of the task. Valid values: 0: The task fails. 1: The task is successful. 2: The task is not started. |

**Examples**

Sample requests

```
https://semawaf.[RegionId].aliyuncs.com/?Action=DeleteCCWhitelist &RegionId=cn-hangzhou &IdList.1=1
```

Sample success responses `XML` format

```xml
<DeleteCCWhitelistResponse>
    <RequestId>53e59af3-3209-452a-853c-ac10ad815929</RequestId>
    <TaskStatus>
        <TaskId>c68646a1-58f8-4b75-828a-a2d3b19b382a</TaskId>
        <Time>1593593692</Time>
        <TaskList>["Generated website configurations", "Generated policy
configurations"]<TaskList>
        <StatusMessage>The configuration is in effect.</StatusMessage>
        <SuccessCode>1</SuccessCode>
    </TaskStatus>
</DeleteCCWhitelistResponse>
```

`JSON` format `{`

```json
  "RequestId":"53e59af3-3209-452a-853c-ac10ad815929",
  "TaskStatus":{
    "TaskId":"c68646a1-58f8-4b75-828a-a2d3b19b382a",
    "TaskList":"[\"Generated website configurations\", \"Generated policy
configurations\"]",
    "SuccessCode":"1",
    "Time":"1593593692",
    "StatusMessage":"The configuration is in effect."
```

`}` `}`

**Error codes**

For a list of error codes, see Error codes.

### 4.4 Custom rules

#### 4.4.1 DescribePolicyRule

Queries the information about custom rules.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribePolicy Rule | The operation that you want to perform. Set the value to DescribePolicyRule. |
| RegionId | String | Yes | cn-hangzhou |   |
| Id | Integer | No | 1 | The ID of the custom rule. |
| Enable | Boolean | No | true | Specifies whether to filter custom rules. |

| RiskLevelFilt er | RepeatList | No | [1, 2] | The risk level to filter rules. You can enter multiple values. Valid values: 0: no risks 1: low 2: medium 3: high |
|---|---|---|---|---|
| AttackTypeFi lter | RepeatList | No | [1, 2, 3] | The attack type to filter rules. You can enter multiple values. Valid values: -1 (non-web attacks), 0 (SQL injection attacks), 1 (XSS attacks), 2 (CSRF attacks), 3 (SSRF attacks), 4 (denial of service attacks), 5 (backdoors), 6 (deserialization attacks), 7 (code executions), 8 (code injection attacks), 9 (command injection attacks), 10 (file uploads), 11 (file inclusions), 12 (redirection attacks), 13 (improper authorization), 14 (information leaks), 15 (unauthorized access), 16 (insecure configurations), 17 (XXE attacks), 18 (Xpath injection attacks), 19 (LDAP injection attacks), 20 (path traversal attacks), 21 (scanners), 22 (horizontal authorization bypass), 23 (vertical authorization bypass), 24 (file modifications), 25 (file reads), 26 (file deletions), 27 (logical errors), 28 (CRLF injection attacks), 29 (template injection attacks), 30 (click hijacking attacks), 31 (buffer overflows), 32 (integer overflows), 33 (format string attacks), 34 (race condition attacks), 61 (timeout errors), and 62 (unknown attacks). |
| PolicyActionF ilter | RepeatList | No | ["deny", "allow"] | The action to filter rules. You can enter multiple values. Valid values: deny, allow, dry run, and modify module. _ _ The value dry run indicates the _ rules that monitor requests. The value modify module indicates _ the rules that are intended for detection modules. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 53e59af3-3209- 452a-853c- ac10ad815929 | The ID of the request. |

| Result | String | [{"id": 19, "version": "19@time- 1594205736", "websites": [1746], "target": "logic expr", _ "pattern": {"$AND": [{"infix": {"decoded path": _ "asda"}}]}, "action": "deny", "is enabled": true, _ "is expired": false, _ "comment": "1111", "attack type": -1, _ "log option": _ "Persistence", "create time": _ "1594205736", "last update time" _ _ : "1594205736", "expire time": null, _ "is global": false, _ "forbidden page c _ _ onfig": null, "priority": 0, "module managem _ ent": null, "risk level": 0, _ "extra": null}] | The returned result of the request. For more information about the pattern parameter in the returned result, see Fields in match conditions. |
|---|---|---|---|

**Examples**

Sample requests

```
https://semawaf.[ RegionId].aliyuncs.com/?Action=DescribePolicyRule &RegionId=cn-hangzhou &Id=1 &Enable=true &RiskLevelFilter.1=1 &AttackTypeFilter.1=1 &PolicyActionFilter.1=deny
```

Sample success responses `XML` format

```xml
<DescribePolicyRuleResponse>
    <RequestId>53e59af3-3209-452a-853c-ac10ad815929</RequestId>
    <Result>[{"id": 19, "version": "19@time-1594205736", "websites": [1746], "target":
"logic_expr", "pattern": {"$AND": [{"infix": {"decoded_path": "asda"}}]}, "action": "de ny", "is_enabled": true, "is_expired": false, "comment": "1111", "attack_type": -1, "lo g_option": "Persistence", "create_time": "1594205736", "last_update_time": "1594205736", "expire_time": null, "is_global": false, "forbidden_page_config": null, " priority": 0, "module_management": null, "risk_level": 0, "extra": null}]</Result> </DescribePolicyRuleResponse>
```

`JSON` format `{`

```json
  "RequestId":"53e59af3-3209-452a-853c-ac10ad815929",
  "Result":"[{\"id\": 19, \"version\": \"19@time-1594205736\", \"websites\": [1746], \"
target\": \"logic_expr\", \"pattern\": {\"$AND\": [{\"infix\": {\"decoded_path\": \"asd a\"}}]}, \"action\": \"deny\", \"is_enabled\": true, \"is_expired\": false, \"comment\": \"1111\", \"attack_type\": -1, \"log_option\": \"Persistence\", \"create_t ime\": \"1594205736\", \"last_update_time\": \"1594205736\", \"expire_time\": null, \"i s_global\": false, \"forbidden_page_config\": null, \"priority\": 0, \"module_management\": null, \"risk_level\": 0, \"extra\": null}]"
```

`}`

**Error codes**

For a list of error codes, see Error codes.

#### 4.4.2 CreatePolicyRule

Creates a custom rule to deny, allow, or monitor requests.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreatePolicyRu le | The operation that you want to perform. Set the value to CreatePolicyRule. |
| RegionId | String | Yes | cn-hangzhou |   |

| ForbiddenPa geConfig | Json | No | {"status code" _ :405,"action":" response","pat h":""} | The configurations to block requests. The value is a string that consists of a JSON struct. The JSON struct contains the following fields: status code: the status code. _ This field is required. Data type: integer. Valid values: 200, 301, 302, 307, 400, 403, 404, 501, and 502. action: the method to respond to the requests. This field is required. Data type: string. Valid values: redirect and response. The value redirect indicates that the system redirects the requests. The value response indicates that the system returns specific content. If status code is set _ to 301 or 302, set action to redirect. If status code is set _ to a different value, set action to response. path: the destination address for redirection. Data type: string. If action is set to redirect, this field is required. Otherwise, leave this field empty. |
|---|---|---|---|---|
| Comment | String | Yes | policy-rule-1 | The description of the rule. |
| Enable | Boolean | No | true | Specifies whether to enable the custom rule. Default value: true. |
| PolicyAction | String | Yes | deny | The action on requests. Valid values: deny, allow, and dry run. The value dry run _ _ indicates that the system allows and monitors the requests. |

| AttackType | Integer | Yes | -1 | The attack type in the custom rule. Valid values: -1 (non-web attacks), 0 (SQL injection attacks), 1 (XSS attacks), 2 (CSRF attacks), 3 (SSRF attacks), 4 (denial of service attacks), 5 (backdoors), 6 (deserialization attacks), 7 (code executions), 8 (code injection attacks), 9 (command injection attacks), 10 (file uploads), 11 (file inclusions), 12 (redirection attacks), 13 (improper authorization), 14 (information leaks), 15 (unauthorized access), 16 (insecure configurations), 17 (XXE attacks), 18 (Xpath injection attacks), 19 (LDAP injection attacks), 20 (path traversal attacks), 21 (scanners), 22 (horizontal authorization bypass), 23 (vertical authorization bypass), 24 (file modifications), 25 (file reads), 26 (file deletions), 27 (logical errors), 28 (CRLF injection attacks), 29 (template injection attacks), 30 (click hijacking attacks), 31 (buffer overflows), 32 (integer overflows), 33 (format string attacks), 34 (race condition attacks), 61 (timeout errors), and 62 (unknown attacks). |
|---|---|---|---|---|
| RiskLevel | Integer | Yes | 3 | The risk level in the custom rule. Valid values: 0: no risks 1: low 2: medium 3: high |
| LogOption | String | Yes | log | The logging operation. Valid values: log and drop. The value log indicates that matched requests are logged. The value drop indicates that matched requests are not logged. |
| Pattern | Json | Yes | {"$AND": [{"$NOT": [{"infix": {"urlpath":"ad min"}}]}]} | The match conditions. The value is a string that consists of a JSON struct. For information about the JSON struct, see Fields in match conditions. |
| ExpireTime | Long | No | 1594982409 | The UNIX timestamp of when the custom rule expires. Unit: seconds. If you leave this parameter empty or set it to 0, the rule does not expire. |

| WebsiteIdList | RepeatList | No | [1, 2] | The ID of the website to which the custom rule applies. You can enter multiple IDs. You can call the DescribePolicyRule operation to query the IDs of websites. |
|---|---|---|---|---|

**Fields in match conditions**

The match conditions of a custom rule are specified in a string that consists of a JSON struct. The JSON struct contains the following fields: `{`

```
  "$AND": [                    //The match conditions. This field is required. Data type
: list. You can specify the field value in the following default format:
```

`{`

```json
      "Operator":            //This field is required. Data type: string.
        "Match field": "Match content",  //This field is required. Data type: string. I
f the match content is a value, use this format.
        "Match field": {                      //This field is required. Data type:
string. If the match content is a key-value pair, use this format.
          "key": "Match field",                  //This field is required. Data type: st
ring.
          "value": "Match content"        //This field is required. Data type: string.
```

`}` `}` `},` `{`

```
      "$NOT":                                       //If the operator is prefixed with no
t, this field is required. Data type: string. You must specify the field value in the f ollowing default format:
```

`{`

```json
          "Operator": {                             //This field is required. Data type:
string.
            "Match field": "Match content",  //This field is required. Data type:
string. If the match content is a value, use this format. If the operator is prefixed w ith not, remove not.
            "Match field": {                      //This field is required. Data type:
string. If the match content is a key-value pair, use this format. If the operator is p refixed with not, remove not.
              "key": "Match field",                  //This field is required. Data
type: string.
              "value": "Match content"                  //This field is required. Data t
ype: string.
```

`}` `}` `}` `]` `}` `]` `}`

**Operators and match fields**

The following lists describe the operators and match fields. The system does not support custom operators or match fields.

**Operators**

**infix**: inclusion
**notinfix**: exclusion
**str**: exact match
**notstr**: fuzzy match
**re**: match based on regular expressions
**notre**: reverse match based on regular expressions

**Match fields and match content types**

**urlpath**: the original URI in the request, which is not decoded. Match content type: value.
Example: /query%20news?q=1%20or%201%3D1.
**decoded_path**: the path after decoding. Match content type: value. The path is the
content from the forward slash (**/**) to the question mark (**?**) in the URL.The path must be URL-decoded. Example: /query news.
**decoded_query**: the query string in the URL. Match content type: value. The query
string is the content from the question mark (**?**)to the end of the URL. The query string must be URL-decoded. Example: q=1 or 1=1.
**query**: the parameters in the query string. Match content type: key-value pair. The
parameters are obtained by splitting the content from the question mark (**?**) to the end of the URL into key-value pairs. The parameters must be URL-decoded. Example: Parameter name q Parameter value 1 or 1=1.
**method**: the method of the HTTP request. Match content type: value. Example: GET or
POST.
**host**: the Host field in the HTTP request header. Match content type: value.
**cookie_raw**: the Cookie field that is not split into key-value pairs. Match content type:
value.
**cookie**: the cookies that are obtained by splitting the Cookie field into key-value pairs.
Match content type: key-value pair.
**user_agent**: The User-Agent field in the HTTP request header. Match content type:
value.
**referer**: the Referrer field in the HTTP request header. Match content type: value.
**content_type**: the Content-Type field in the HTTP request header. Match content type:
value.
**remote_addr**: the actual IP address of the client. Match content type: value.
**x_forwarded_for**: the X-Forwarded-For field in the HTTP request header. Match content
type: value.
**origin**: the Origin field in the HTTP request header. Match content type: value.
**session**: the Session content. You can configure this field only after you configure the
session settings for your website. Match content type: value.
**request_header**: the complete header of the original HTTP request. Match content type:
value.
**custom_header**: the HTTP request header that is split into key-value pairs. Match
content type: key-value pair.
**request_header_length**: the length of the HTTP request header. Match content type:
value.
**request_body_length**: the length of the HTTP request body. Match content type: value.
**form**: the form data in the HTTP request body. The data must be split into key-value
pairs and URL-decoded. Match content type: key-value pair.
**file_name**: the name of the file that you want to upload in the HTTP request. Match
content type: value.
**request_body**: the complete body of the HTTP request. Match content type: value.
**response_status**: the HTTP status code that the server returns. Match content type:
value.
**response_header**: the HTTP response header that is split into key-value pairs. Match
content type: key-value pair.
**response_body**: the complete response that the server returns. Match content type:
value.

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 53e59af3-3209- 452a-853c- ac10ad815929 | The ID of the request. |
| TaskStatus | Struct |   |   |
| └TaskId | String | c68646a1-58f8- 4b75-828a- a2d3b19b382a | The ID of the task. The ID of the task. |
| └Time | String | 1593593692 | The time when the task status message was generated. This value is a UNIX timestamp representing the number of seconds that have elapsed since the epoch time January 1, 1970, 00:00:00 UTC. |
| └TaskList | String | ["Website-related configuration generation", "Policy-related configuration generation"] | The descriptions of the task. This value is returned only for asynchronous tasks. |
| └StatusMess age | String | The configuration is in effect. | The status message of the task. You can ignore this reserved parameter. |
| └SuccessCod e | String | 1 | The status code of the task. Valid values: 0: The task fails. 1: The task is successful. 2: The task is not started. |

| └Result | String | {"id": 57, "version": "57@time- 1598336466", "websites": [781], "target": "logic expr", _ "pattern": {"$AND": [{"infix": {"urlpath": "abcedfgh"}}]}, "action": "deny", "is enabled": true, _ "is expired": false, _ "comment": "test- policy-rule-1", "attack type": -1, _ "log option": _ "Persistence", "create time": _ "1598336466", "last update time" _ _ : "1598336466", "expire time": null, _ "is global": false, _ "forbidden page c _ _ onfig": null, "priority": 0, "module managem _ ent": null, "risk level": 0, _ "extra": null} | The information about the added website. |
|---|---|---|---|

**Examples**

Sample requests

```
https://semawaf.[RegionId].aliyuncs.com/?Action=CreatePolicyRule &RegionId=cn-hangzhou &ForbiddenPageConfig={"status_code":405,"action":"response","path":""} &Comment=policy-rule-1 &Enable=true &PolicyAction=deny &AttackType=-1 &RiskLevel=3 &LogOption=log &Pattern={"\$AND":[{"\$NOT":[{"infix":{"urlpath":"admin"}}]}]} &ExpireTime=1594982409 &WebsiteIdList.1=1
```

Sample success responses `XML` format

```json
<CreatePolicyRuleResponse>
    <RequestId>53e59af3-3209-452a-853c-ac10ad815929</RequestId>
    <TaskStatus>
        <TaskId>c68646a1-58f8-4b75-828a-a2d3b19b382a</TaskId>
        <Time>1593593692</Time>
        <TaskList>["Website-related configuration generation", "Policy-related
configuration generation"]</TaskList>
        <StatusMessage>The configuration is in effect.</StatusMessage>
        <SuccessCode>1</SuccessCode>
        <Result>{"id": 57, "version": "57@time-1598336466", "websites": [781],
"target": "logic_expr", "pattern": {"$AND": [{"infix": {"urlpath": "abcedfgh"}}]}, "act ion": "deny", "is_enabled": true, "is_expired": false, "comment": "test-policy-rule-1", "attack_type": -1, "log_option": "Persistence", "create_time": "1598336466", "last_update_time": "1598336466", "expire_time": null, "is_global": false, "forbidden_page_config": null, "priority": 0, "module_management": null, "risk_level": 0, "extra": null}</Result>
    </TaskStatus>
</CreatePolicyRuleResponse>
```

`JSON` format `{`

```json
  "RequestId":"53e59af3-3209-452a-853c-ac10ad815929",
  "TaskStatus":{
    "TaskId":"c68646a1-58f8-4b75-828a-a2d3b19b382a",
    "TaskList":"[\"Website-related configuration generation\", \"Policy-related
configuration generation\"]",
    "SuccessCode":"1",
    "Time":"1593593692",
    "StatusMessage":"The configuration is in effect.",
    "Result":"{\"id\": 57, \"version\": \"57@time-1598336466\", \"websites\": [781], \"
target\": \"logic_expr\", \"pattern\": {\"$AND\": [{\"infix\": {\"urlpath\": \"abcedfgh\"}}]}, \"action\": \"deny\", \"is_enabled\": true, \"is_expired\": false, \" comment\": \"test-policy-rule-1\", \"attack_type\": -1, \"log_option\": \"Persistence\", \"create_time\": \"1598336466\", \"last_update_time\": \"1598336466\", \"expire_time\": null, \"is_global\": false, \"forbidden_page_config\": null, \"priorit y\": 0, \"module_management\": null, \"risk_level\": 0, \"extra\": null}"
```

`}` `}`

**Error codes**

For a list of error codes, see Error codes.

#### 4.4.3 EditPolicyRule

Modifies a specific custom rule.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|

| Action | String | Yes | EditPolicyRule | The operation that you want to perform. Set the value to EditPolicyRule. |
|---|---|---|---|---|
| RegionId | String | Yes | cn-hangzhou |   |
| ForbiddenPa geConfig | Json | No | {"status code" _ :405,"action":" response","pat h":""} | The configurations to block requests. This parameter is a string consisting of JSON structs. A JSON struct includes the following fields: status code: the status code _ in the responses. This field is required. Data type: integer. Valid values: 200, 301, 302, 307, 400, 403, 404, 501, and 502. action: the method to respond to the requests. This field is required. Data type: string. Valid values: redirect and response. The value redirect indicates that the system redirects the requests. The value response indicates that the system returns specific content. If status code is set _ to 301 or 302, set action to redirect. If status code is set _ to another value, set action to response. path: the destination address for redirection. Data type: string. If action is set to redirect, this field is required. In other cases, leave this field unspecified. |
| Comment | String | Yes | policy-rule-1 | The remarks. |
| Enable | Boolean | No | true | Specifies whether to enable the custom rule. Default value: true. |
| PolicyAction | String | Yes | deny | The action on requests. Valid values: deny, allow, and dry run. The value dry run _ _ indicates that the system allows and monitors the requests. |

| AttackType | Integer | Yes | -1 | The attack type in the custom rule. Valid values: -1 (non-web attacks), 0 (SQL injection attacks), 1 (XSS attacks), 2 (CSRF attacks), 3 (SSRF attacks), 4 (denial of service attacks), 5 (backdoors), 6 (deserialization attacks), 7 (code executions), 8 (code injection attacks), 9 (command injection attacks), 10 (file uploads), 11 (file inclusions), 12 (redirection attacks), 13 (improper authorization), 14 (information leaks), 15 (unauthorized access), 16 (insecure configurations), 17 (XXE attacks), 18 (Xpath injection attacks), 19 (LDAP injection attacks), 20 (path traversal attacks), 21 (scanners), 22 (horizontal authorization bypass), 23 (vertical authorization bypass), 24 (file modifications), 25 (file reads), 26 (file deletions), 27 (logical errors), 28 (CRLF injection attacks), 29 (template injection attacks), 30 (click hijacking attacks), 31 (buffer overflows), 32 (integer overflows), 33 (format string attacks), 34 (race condition attacks), 61 (timeout errors), and 62 (unknown attacks). |
|---|---|---|---|---|
| RiskLevel | Integer | Yes | 3 | The risk level in the custom rule. Valid values: 0: no risks 1: low 2: medium 3: high |
| LogOption | String | Yes | log | The logging operation. Valid values: log and drop. The value log indicates that matched requests are logged. The value drop indicates that matched requests are not logged. |
| Pattern | Json | Yes | {"$AND": [{"$NOT": [{"infix": {"urlpath":"ad min"}}]}]} | The match conditions. This parameter is a string consisting of JSON structs. For information about the JSON structs, see Fields in match conditions. |

| ExpireTime | Long | No | 1594982409 | The expiration time of the custom rule. This value is a UNIX timestamp representing the number of seconds that have elapsed since the epoch time January 1, 1970, 00:00:00 UTC. If you leave this parameter unspecified or set it to 0, the rule does not expire. |
|---|---|---|---|---|
| WebsiteIdList | RepeatList | No | [1, 2] | The ID of the website to which the custom rule applies. You can enter multiple IDs. You can call the DescribePolicyRule operation to query the IDs of websites. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 53e59af3-3209- 452a-853c- ac10ad815929 | The ID of the request. |
| TaskStatus | Struct |   |   |
| └TaskId | String | c68646a1-58f8- 4b75-828a- a2d3b19b382a | The ID of the task. The ID of the task. |
| └Time | String | 1593593692 | The time when the task status message was generated. This value is a UNIX timestamp representing the number of seconds that have elapsed since the epoch time January 1, 1970, 00:00:00 UTC. |
| └TaskList | String | ["Website-related configuration generation", "Policy-related configuration generation"] | The descriptions of the task. This value is returned only for asynchronous tasks. |
| └StatusMess age | String | The configuration is in effect. | The status message of the task. You can ignore this reserved parameter. |
| └SuccessCod e | String | 1 | The status code of the task. Valid values: 0: The task fails. 1: The task is successful. 2: The task is not started. |

| └Result | String | {"id": 57, "version": "57@time- 1598336466", "websites": [781], "target": "logic expr", _ "pattern": {"$AND": [{"infix": {"urlpath": "abcedfgh"}}]}, "action": "deny", "is enabled": true, _ "is expired": false, _ "comment": "test- policy-rule-1", "attack type": -1, _ "log option": _ "Persistence", "create time": _ "1598336466", "last update time" _ _ : "1598336466", "expire time": null, _ "is global": false, _ "forbidden page c _ _ onfig": null, "priority": 0, "module managem _ ent": null, "risk level": 0, _ "extra": null} | The information about the added website. |
|---|---|---|---|

**Examples**

Sample requests

```
https://semawaf.[ RegionId].aliyuncs.com/?Action=EditPolicyRule &RegionId=cn-hangzhou &Id=1 &ForbiddenPageConfig={"status_code":405,"action":"response","path":""} &Comment=policy-rule-1 &Enable=true &PolicyAction=deny &AttackType=-1 &RiskLevel=3 &LogOption=log &Pattern={"\$AND":[{"\$NOT":[{"infix":{"urlpath":"admin"}}]}]} &ExpireTime=1594982409 &WebsiteIdList.1=1
```

Sample success responses `XML` format

```json
<EditPolicyRuleResponse>
    <RequestId>53e59af3-3209-452a-853c-ac10ad815929</RequestId>
    <TaskStatus>
        <TaskId>c68646a1-58f8-4b75-828a-a2d3b19b382a</TaskId>
        <Time>1593593692</Time>
        <TaskList>["Website-related configuration generation", "Policy-related
configuration generation"]</TaskList>
        <StatusMessage>The configuration is in effect.</StatusMessage>
        <SuccessCode>1</SuccessCode>
        <Result>{"id": 57, "version": "57@time-1598336466", "websites": [781],
"target": "logic_expr", "pattern": {"$AND": [{"infix": {"urlpath": "abcedfgh"}}]}, "act ion": "deny", "is_enabled": true, "is_expired": false, "comment": "test-policy-rule-1", "attack_type": -1, "log_option": "Persistence", "create_time": "1598336466", "last_update_time": "1598336466", "expire_time": null, "is_global": false, "forbidden_page_config": null, "priority": 0, "module_management": null, "risk_level": 0, "extra": null}</Result>
    </TaskStatus>
</EditPolicyRuleResponse>
```

`JSON` format `{`

```json
  "RequestId":"53e59af3-3209-452a-853c-ac10ad815929",
  "TaskStatus":{
    "TaskId":"c68646a1-58f8-4b75-828a-a2d3b19b382a",
    "TaskList":"[\"Website-related configuration generation\", \"Policy-related
configuration generation\"]",
    "SuccessCode":"1",
    "Time":"1593593692",
    "StatusMessage":"The configuration is in effect.",
    "Result":"{\"id\": 57, \"version\": \"57@time-1598336466\", \"websites\": [781], \"
target\": \"logic_expr\", \"pattern\": {\"$AND\": [{\"infix\": {\"urlpath\": \"abcedfgh\"}}]}, \"action\": \"deny\", \"is_enabled\": true, \"is_expired\": false, \" comment\": \"test-policy-rule-1\", \"attack_type\": -1, \"log_option\": \"Persistence\", \"create_time\": \"1598336466\", \"last_update_time\": \"1598336466\", \"expire_time\": null, \"is_global\": false, \"forbidden_page_config\": null, \"priorit y\": 0, \"module_management\": null, \"risk_level\": 0, \"extra\": null}"
```

`}` `}`

**Error codes**

For a list of error codes, see Error codes.

#### 4.4.4 TogglePolicyRule

Enables or disables a specific custom rule.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|

| Action | String | Yes | TogglePolicyRul e | The operation that you want to perform. Set the value to TogglePolicyRule. |
|---|---|---|---|---|
| RegionId | String | Yes | cn-hangzhou |   |
| IdList | RepeatL ist | Yes | [1, 2] | The ID of the custom rule. You can enter multiple IDs. You can call the DescribePolicyRule operation to query the IDs of custom rules. |
| ToggleAction | String | Yes | disable | Specifies the status of the custom rule. Valid values: enable disable |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 53e59af3-3209- 452a-853c- ac10ad815929 | The ID of the request. |
| TaskStatus | Struct |   | The returned information. |
| └TaskId | String | c68646a1-58f8- 4b75-828a- a2d3b19b382a | The ID of the task. |
| └Time | String | 1593593692 | The time when the task status message was generated. This value is a UNIX timestamp representing the number of seconds that have elapsed since the epoch time January 1, 1970, 00:00:00 UTC. |
| └TaskList | String | ["Website-related configuration generation", "Policy-related configuration generation"] | The descriptions of the task. This value is returned only for asynchronous tasks. |
| └StatusMess age | String | The configuration is in effect. | The status message of the task. You can ignore this reserved parameter. |
| └SuccessCod e | String | 1 | The status code of the task. Valid values: 0: The task fails. 1: The task is successful. 2: The task is not started. |

**Examples**

Sample requests

```
https://semawaf.[ RegionId].aliyuncs.com/?Action=TogglePolicyRule &RegionId=cn-hangzhou &IdList.1=1 &ToggleAction=disable
```

Sample success responses `XML` format

```xml
<TogglePolicyRuleResponse>
    <RequestId>53e59af3-3209-452a-853c-ac10ad815929</RequestId>
    <TaskStatus>
        <TaskId>c68646a1-58f8-4b75-828a-a2d3b19b382a</TaskId>
        <Time>1593593692</Time>
        <TaskList>["Website-related configuration generation", "Policy-related
configuration generation"]</TaskList>
        <StatusMessage>The configuration is in effect.</StatusMessage>
        <SuccessCode>1</SuccessCode>
    </TaskStatus>
</TogglePolicyRuleResponse>
```

`JSON` format `{`

```json
  "RequestId":"53e59af3-3209-452a-853c-ac10ad815929",
  "TaskStatus":{
    "TaskId":"c68646a1-58f8-4b75-828a-a2d3b19b382a",
    "TaskList":"[\"Website-related configuration generation\", \"Policy-related
configuration generation\"]",
    "SuccessCode":"1",
    "Time":"1593593692",
    "StatusMessage":"The configuration is in effect."
```

`}` `}`

**Error codes**

For a list of error codes, see Error codes.

#### 4.4.5 DeletePolicyRule

Deletes a specific custom rule.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeletePolicyRule | The operation that you want to perform. Set the value to DeletePolicyRule. |
| RegionId | String | Yes | cn-hangzhou |   |

| IdList | RepeatL ist | Yes | [1, 2] | The ID of the custom rule. You can enter multiple IDs. You can call the DescribePolicyRule operation to query the IDs of custom rules. |
|---|---|---|---|---|

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 53e59af3-3209- 452a-853c- ac10ad815929 | The ID of the request. |
| TaskStatus | Struct |   |   |
| └TaskId | String | c68646a1-58f8- 4b75-828a- a2d3b19b382a | The ID of the task. |
| └Time | String | 1593593692 | The time when the task status message was generated. This value is a UNIX timestamp representing the number of seconds that have elapsed since the epoch time January 1, 1970, 00:00:00 UTC. |
| └TaskList | String | ["Website-related configuration generation", "Policy-related configuration generation"] | The descriptions of the task. This value is returned only for asynchronous tasks. |
| └StatusMess age | String | The configuration is in effect. | The status message of the task. You can ignore this reserved parameter. |
| └SuccessCod e | String | 1 | The status code of the task. Valid values: 0: The task fails. 1: The task is successful. 2: The task is not started. |

**Examples**

Sample requests

```
https://semawaf.[ RegionId].aliyuncs.com/?Action=DeletePolicyRule &RegionId=cn-hangzhou &IdList.1=1
```

Sample success responses `XML` format

```xml
<DeletePolicyRuleResponse>
    <RequestId>53e59af3-3209-452a-853c-ac10ad815929</RequestId>
    <TaskStatus>
        <TaskId>c68646a1-58f8-4b75-828a-a2d3b19b382a</TaskId>
        <Time>1593593692</Time>
        <TaskList>["Website-related configuration generation", "Policy-related
configuration generation"]</TaskList>
        <StatusMessage>The configuration is in effect.</StatusMessage>
        <SuccessCode>1</SuccessCode>
    </TaskStatus>
</DeletePolicyRuleResponse>
```

`JSON` format `{`

```json
  "RequestId":"53e59af3-3209-452a-853c-ac10ad815929",
  "TaskStatus":{
    "TaskId":"c68646a1-58f8-4b75-828a-a2d3b19b382a",
    "TaskList":"[\"Website-related configuration generation\", \"Policy-related
configuration generation\"]",
    "SuccessCode":"1",
    "Time":"1593593692",
    "StatusMessage":"The configuration is in effect."
```

`}` `}`

**Error codes**

For a list of error codes, see Error codes.

#### 4.4.6 EditPolicyRulePriority

Modifies the priorities of custom rules for a specific website. The rules in PolicyRuleIdList are prioritized in descending order.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | EditPolicyRuleP riority | The operation that you want to perform. Set the value to EditPolicyRulePriority. |
| RegionId | String | Yes | cn-hangzhou |   |
| WebsiteId | Integer | No | 101 | The ID of the website for which you want to modify custom rule priorities. |
| PolicyRuleIdL ist | Integer | No | 10 | The ID of the custom rule. You can enter multiple IDs. You can call the DescribePolicyRule operation to query the IDs of custom rules. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 53e59af3-3209- 452a-853c- ac10ad815929 | The ID of the request. |
| TaskStatus | Struct |   |   |
| └TaskId | String | c68646a1-58f8- 4b75-828a- a2d3b19b382a | The ID of the task. |
| └Time | String | 1593593692 | The time when the task status message was generated. This value is a UNIX timestamp representing the number of seconds that have elapsed since the epoch time January 1, 1970, 00:00:00 UTC. |
| └TaskList | String | ["Website-related configuration generation", "Policy-related configuration generation"] | The descriptions of the task. This value is returned only for asynchronous tasks. |
| └StatusMess age | String | The configuration is in effect. | The status message of the task. You can ignore this reserved parameter. |
| └SuccessCod e | └Result | String | The status code of the task. Valid values: 0: The task fails. 1: The task is successful. 2: The task is not started. |
| └Result | String | {"website": 12, "policy rule ids": _ _ [12, 17]} | The returned result of the request. |

**Examples**

Sample requests

```
https://semawaf.[ RegionId].aliyuncs.com/?Action=EditPolicyRulePriority &RegionId=cn-hangzhou &WebsiteId=101 &PolicyRuleIdList.1=3
```

Sample success responses `XML` format

```xml
<EditPolicyRulePriorityResponse>
    <RequestId>53e59af3-3209-452a-853c-ac10ad815929</RequestId>
    <TaskStatus>
        <TaskId>c68646a1-58f8-4b75-828a-a2d3b19b382a</TaskId>
        <Time>1593593692</Time>
        <TaskList>["Website-related configuration generation", "Policy-related
configuration generation"]</TaskList>
        <StatusMessage>The configuration is in effect.</StatusMessage>
        <SuccessCode>1</SuccessCode>
        <Result>{"website": 12, "policy_rule_ids": [12, 17]}</Result>
    </TaskStatus>
</EditPolicyRulePriorityResponse>
```

`JSON` format `{`

```json
  "RequestId":"53e59af3-3209-452a-853c-ac10ad815929",
  "TaskStatus":{
    "TaskId":"c68646a1-58f8-4b75-828a-a2d3b19b382a",
    "TaskList":"[\"Website-related configuration generation\", \"Policy-related
configuration generation\"]",
    "SuccessCode":"1",
    "Time":"1593593692",
    "StatusMessage":"The configuration is in effect.",
    "Result":"{\"website\": 12, \"policy_rule_ids\": [12, 17]}"
```

`}` `}`

**Error codes**

For a list of error codes, see Error codes.

#### 4.4.7 GenerateFalsePositiveRuleCorrection

Generates correction rules based on false positives.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | GenerateFalse PositiveRuleCo rrection | The operation that you want to perform. Set the value to GenerateFalsePositiveRuleCorrecti on. |
| RegionId | String | Yes | cn-hangzhou |   |
| LogId | String | Yes | 1e23f8d1- a9d2-4dd9- b7e2- 424b9832183f | The ID of the log. |
| RuleId | String | Yes | m sqli _ | The ID of the rule. |

| UrlPath | String | Yes | / | The path of the URL. |
|---|---|---|---|---|
| Host | String | Yes | www.taobao.co m | The domain name. |
| SourceIpAddr ess | String | Yes | 10.17.XX.XX | The source IP address. |
| DestinationIp | String | Yes | 43.17.XX.XX | The destination IP address. |
| DestinationP ort | Integer | Yes | 80 | The destination port. |
| RequestBody | String | No |   | The body of the request. |
| RawRequest Header | String | Yes | GET /? id=1 or 1=1 HTTP/1.1\r\nUs er-Agent: curl/7.29.0\r\n Accept: /\r\nhost: www.taobao.co m\r\n\r\n | The original header of the request. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 53e59af3-3209- 452a-853c- ac10ad815929 | The ID of the request. |
| Result | String | {"pattern": {"decoded path": _ "/", "host": "40.73.XX.XX", "remote addr": _ "139.162.XX.XX"}, "action": "allow", "comment": "Clear false positives - 550877"} | The returned result of the request. |

**Examples**

Sample requests

```
https://semawaf.[ RegionId].aliyuncs.com/?Action=GenerateFalsePositiveRuleCorrection &RegionId=cn-hangzhou &LogId=1e23f8d1-a9d2-4dd9-b7e2-424b9832183f &RuleId=m_sqli &UrlPath=/ &Host=www.taobao.com &SourceIpAddress=10.17.XX.XX &DestinationIp=43.17.XX.XX &DestinationPort=80 &RequestBody= &RawRequestHeader=GET /? id=1 or 1=1 HTTP/1.1\r\nUser-Agent: curl/7.29.0\r\nAccept: */* \r\nhost: www.taobao.com\r\n\r\n
```

Sample success responses `XML` format

```xml
<GenerateFalsePositiveRuleCorrectionResponse>
    <RequestId>53e59af3-3209-452a-853c-ac10ad815929</RequestId>
    <Result>{"pattern": {"decoded_path": "/", "host": "40.73.XX.XX", "remote_addr": "13
9.162.XX.XX"}, "action": "allow", "comment": "Clear false positives - 550877"}</Result> </GenerateFalsePositiveRuleCorrectionResponse>
```

`JSON` format `{`

```json
  "RequestId":"53e59af3-3209-452a-853c-ac10ad815929",
  "Result":"{\"pattern\": {\"decoded_path\": \"/\", \"host\": \"40.73.XX.XX\", \"remote
_addr\": \"139.162.XX.XX\"}, \"action\": \"allow\", \"comment\": \"Clear false positive s - 550877\"}"
```

`}`

**Error codes**

For a list of error codes, see Error codes.

#### 4.4.8 CreateDetectionModuleRule

Creates a rule for detection module control.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateDetectio nModuleRule | The operation that you want to perform. Set the value to CreateDetectionModuleRule. |
| RegionId | String | Yes | cn-hangzhou |   |

| ForbiddenPa geConfig | Json | No | {"status code" _ :405,"action":" response","pat h":""} | The configurations to block requests. This parameter is a string consisting of JSON structs. A JSON struct includes the following fields: status code: the status code _ in the responses. This field is required. Data type: integer. Valid values: 200, 301, 302, 307, 400, 403, 404, 501, and 502. action: the method to respond to the requests. This field is required. Data type: string. Valid values: redirect and response. The value redirect indicates that the system redirects the requests. The value response indicates that the system returns specific content. If status code is set _ to 301 or 302, set action to redirect. If status code is set _ to another value, set action to response. path: the destination address for redirection. Data type: string. If action is set to redirect, this field is required. In other cases, leave this field unspecified. |
|---|---|---|---|---|
| Comment | String | Yes | detection- module-rule-1 | The remarks. |
| PolicyAction | String | Yes | modify module _ | The action in the rule. Set the value to modify module, which _ indicates detection module control. |
| Enable | Boolean | No | true | Specifies whether to enable the rule for detection module control. Default value: true. |
| ModuleMana gement | Json | Yes | {"disabled": ["m xss"],"ena _ bled":[]} | Specifies whether to enable detection module control. This parameter is a string consisting of JSON structs. A JSON struct includes the following fields: disabled: disables detection module control. This field is required. Data type: list. enabled: enables detection module control. This filed is required. Data type: list. For more information about detection modules, see Module description. |

| LogOption | String | Yes | log | The logging operation. Valid values: log and drop. The value log indicates that matched requests are logged. The value drop indicates that matched requests are not logged. |
|---|---|---|---|---|
| Pattern | Json | Yes | {"$AND": [{"$NOT": [{"infix": {"urlpath":"ad min"}}]}]} | The match conditions. This parameter is a string consisting of JSON structs. For more information about the JSON structs, see Fields in match conditions. |
| ExpireTime | Long | No | 1594982409 | The expiration time of the custom rule. This value is a UNIX timestamp representing the number of seconds that have elapsed since the epoch time January 1, 1970, 00:00:00 UTC. If you leave this parameter unspecified or set it to 0, the rule does not expire. |
| WebsiteIdList | RepeatList | No | [1, 2] | The ID of the website to which the custom rule applies. You can enter multiple IDs. You can call the DescribePolicyRule operation to query the IDs of websites. |

| Code | Description |
|---|---|
| m sqli _ | SQL Injection Detection Module |
| m xss _ | XSS Detection Module |
| m rule _ | Intelligence Module |
| m csrf _ | CSRF Detection Module |
| m ssrf _ | SSRF Detection Module |
| m php unserialize _ _ | PHP Deserialization Detection Module |
| m java unserialize _ _ | Java Deserialization Detection Module |
| m file upload _ _ | File Upload Attack Detection Module |
| m file include _ _ | File Inclusion Attack Detection Module |
| m php code injection _ _ _ | PHP Code Injection Detection Module |
| m java _ | Java Code Injection Detection Module |
| m cmd injection _ _ | Command Injection Detection Module |
| m response _ | Server Response Detection Module |

| m scanner _ | Robot Detection Module |
|---|---|
| m asp code injection _ _ _ | ASP Code Injection Detection Module |
| m ssti _ | Template Injection Detection Module |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 53e59af3-3209- 452a-853c- ac10ad815929 | The ID of the request. |
| TaskStatus | Struct |   |   |
| └TaskId | String | c68646a1-58f8- 4b75-828a- a2d3b19b382a | The ID of the task. The ID of the task. |
| └Time | String | 1593593692 | The time when the task status message was generated. This value is a UNIX timestamp representing the number of seconds that have elapsed since the epoch time January 1, 1970, 00:00:00 UTC. |
| └TaskList | String | ["Website-related configuration generation", "Policy-related configuration generation"] | The descriptions of the task. This value is returned only for asynchronous tasks. |
| └StatusMess age | String | The configuration is in effect. | The status message of the task. You can ignore this reserved parameter. |
| └SuccessCod e | String | 1 | The status code of the task. Valid values: 0: The task fails. 1: The task is successful. 2: The task is not started. |

| └Result | String | {"id": 58, "version": "58@time- 1598338353", "websites": [], "target": "logic expr", _ "pattern": {"$AND": [{"infix": {"urlpath": "1234567"}}]}, "action": "modify module", _ "is enabled": true, _ "is expired": false, _ "comment": "test- module-rule-1", "attack type": -1, _ "log option": _ "Persistence", "create time": _ "1598338348", "last update time" _ _ : "1598338353", "expire time": null, _ "is global": false, _ "forbidden page c _ _ onfig": null, "priority": 0, "module managem _ ent": {"disabled": ["m sqli"], _ "enabled": []}, "risk level": 0, _ "extra": null} | The returned result of the request. |
|---|---|---|---|

**Examples**

Sample requests

```
https://semawaf.[RegionId].aliyuncs.com/?Action=CreateDetectionModuleRule &RegionId=cn-hangzhou &ForbiddenPageConfig={"status_code":405,"action":"response","path":""} &Comment=detection-module-rule-1 &PolicyAction=modify_module &Enable=true &ModuleManagement={"disabled":["m_xss"],"enabled":[]} &LogOption=log &Pattern={"\$AND":[{"\$NOT":[{"infix":{"urlpath":"admin"}}]}]} &ExpireTime=1594982409 &WebsiteIdList.1=1
```

Sample success responses `XML` format

```json
<CreateDetectionModuleRuleResponse>
    <RequestId>53e59af3-3209-452a-853c-ac10ad815929</RequestId>
    <TaskStatus>
        <TaskId>c68646a1-58f8-4b75-828a-a2d3b19b382a</TaskId>
        <Time>1593593692</Time>
        <TaskList>["Website-related configuration generation", "Policy-related
configuration generation"]</TaskList>
        <StatusMessage>The configuration is in effect.</StatusMessage>
        <SuccessCode>1</SuccessCode>
        <Result>{"id": 58, "version": "58@time-1598338353", "websites": [], "target": "
logic_expr", "pattern": {"$AND": [{"infix": {"urlpath": "1234567"}}]}, "action": "modif y_module", "is_enabled": true, "is_expired": false, "comment": "test-module-rule-1", "a ttack_type": -1, "log_option": "Persistence", "create_time": "1598338348", "last_update_time": "1598338353", "expire_time": null, "is_global": false, "forbidden_page_config": null, "priority": 0, "module_management": {"disabled": ["m_sql i"], "enabled": []}, "risk_level": 0, "extra": null}</Result>
    </TaskStatus>
</CreateDetectionModuleRuleResponse>
```

`JSON` format `{`

```json
  "RequestId":"53e59af3-3209-452a-853c-ac10ad815929",
  "TaskStatus":{
    "TaskId":"c68646a1-58f8-4b75-828a-a2d3b19b382a",
    "TaskList":"[\"Website-related configuration generation\", \"Policy-related
configuration generation\"]",
    "SuccessCode":"1",
    "Time":"1593593692",
    "StatusMessage":"The configuration is in effect.",
    "Result":"{\"id\": 58, \"version\": \"58@time-1598338353\", \"websites\": [], \"tar
get\": \"logic_expr\", \"pattern\": {\"$AND\": [{\"infix\": {\"urlpath\": \"1234567\"}}]}, \"action\": \"modify_module\", \"is_enabled\": true, \"is_expired\": f alse, \"comment\": \"test-module-rule-1\", \"attack_type\": -1, \"log_option\": \"Persi stence\", \"create_time\": \"1598338348\", \"last_update_time\": \"1598338353\", \"expi re_time\": null, \"is_global\": false, \"forbidden_page_config\": null, \"priority\": 0 , \"module_management\": {\"disabled\": [\"m_sqli\"], \"enabled\": []}, \"risk_level\": 0, \"extra\": null}"
```

`}` `}`

**Error codes**

For a list of error codes, see Error codes.

#### 4.4.9 EditDetectionModuleRule

Modifies a specific rule for detection module control.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|

| Action | String | Yes | EditDetectionM oduleRule | The operation that you want to perform. Set the value to EditDetectionModuleRule. |
|---|---|---|---|---|
| RegionId | String | Yes | cn-hangzhou |   |
| Id | Integer | Yes | 1 | The ID of the rule for detection module control. |
| ForbiddenPa geConfig | Json | No | {"status code" _ :405,"action":" response","pat h":""} | The configurations to block requests. This parameter is a string consisting of JSON structs. A JSON struct includes the following fields: status code: the status code _ in the responses. This field is required. Data type: integer. Valid values: 200, 301, 302, 307, 400, 403, 404, 501, and 502. action: the method to respond to the requests. This field is required. Data type: string. Valid values: redirect and response. The value redirect indicates that the system redirects the requests. The value response indicates that the system returns specific content. If status code is set _ to 301 or 302, set action to redirect. If status code is set _ to another value, set action to response. path: the destination address for redirection. Data type: string. If action is set to redirect, this field is required. In other cases, leave this field unspecified. |
| Comment | String | Yes | detection- module-rule-1 | The remarks. |
| PolicyAction | String | Yes | modify module _ | The action in the rule. Set the value to modify module, which _ indicates detection module control. |
| Enable | Boolean | No | true | Specifies whether to enable the rule for detection module control. Default value: true. |

| ModuleMana gement | Json | Yes | {"disabled": ["m xss"],"ena _ bled":[]} | Specifies whether to enable detection module control. This parameter is a string consisting of JSON structs. A JSON struct includes the following fields: disabled: disables detection module control. This field is required. Data type: list. enabled: enables detection module control. This field is required. Data type: list. For more information about detection modules, see Module description. |
|---|---|---|---|---|
| LogOption | String | Yes | log | The logging operation. Valid values: log and drop. The value log indicates that matched requests are logged. The value drop indicates that matched requests are not logged. |
| Pattern | Json | Yes | {"$AND": [{"$NOT": [{"infix": {"urlpath":"ad min"}}]}]} | The match conditions. This parameter is a string consisting of JSON structs. For more information about the JSON structs, see Fields in match conditions. |
| ExpireTime | Long | No | 1594982409 | The expiration time of the custom rule. This value is a UNIX timestamp representing the number of seconds that have elapsed since the epoch time January 1, 1970, 00:00:00 UTC. If you leave this parameter unspecified or set it to 0, the rule does not expire. |
| WebsiteIdList | RepeatList | No | [1, 2] | The ID of the website to which the custom rule applies. You can enter multiple IDs. You can call the DescribePolicyRule operation to query the IDs of websites. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 53e59af3-3209- 452a-853c- ac10ad815929 | The ID of the request. |
| TaskStatus | Struct |   |   |
| └TaskId | String | c68646a1-58f8- 4b75-828a- a2d3b19b382a | The ID of the task. The ID of the task. |

| └Time | String | 1593593692 | The time when the task status message was generated. This value is a UNIX timestamp representing the number of seconds that have elapsed since the epoch time January 1, 1970, 00:00:00 UTC. |
|---|---|---|---|
| └TaskList | String | ["Website-related configuration generation", "Policy-related configuration generation"] | The descriptions of the task. This value is returned only for asynchronous tasks. |
| └StatusMess age | String | The configuration is in effect. | The status message of the task. You can ignore this reserved parameter. |
| └SuccessCod e | String | 1 | The status code of the task. Valid values: 0: The task fails. 1: The task is successful. 2: The task is not started. |
| └Result | String | {"id": 58, "version": "58@time- 1598338353", "websites": [], "target": "logic expr", _ "pattern": {"$AND": [{"infix": {"urlpath": "1234567"}}]}, "action": "modify module", _ "is enabled": true, _ "is expired": false, _ "comment": "test- module-rule-1", "attack type": -1, _ "log option": _ "Persistence", "create time": _ "1598338348", "last update time" _ _ : "1598338353", "expire time": null, _ "is global": false, _ "forbidden page c _ _ onfig": null, "priority": 0, "module managem _ ent": {"disabled": ["m sqli"], _ "enabled": []}, "risk level": 0, _ "extra": null} | The returned result of the request. |

**Examples**

Sample requests

```
https://semawaf.[RegionId].aliyuncs.com/?Action=EditDetectionModuleRule &RegionId=cn-hangzhou &Id=1 &ForbiddenPageConfig={"status_code":405,"action":"response","path":""} &Comment=detection-module-rule-1 &PolicyAction=modify_module &Enable=true &ModuleManagement={"disabled":["m_xss"],"enabled":[]} &LogOption=log &Pattern={"\$AND":[{"\$NOT":[{"infix":{"urlpath":"admin"}}]}]} &ExpireTime=1594982409 &WebsiteIdList.1=1
```

Sample success responses `XML` format

```json
<EditDetectionModuleRuleResponse>
    <RequestId>53e59af3-3209-452a-853c-ac10ad815929</RequestId>
    <TaskStatus>
        <TaskId>c68646a1-58f8-4b75-828a-a2d3b19b382a</TaskId>
        <Time>1593593692</Time>
        <TaskList>["Website-related configuration generation", "Policy-related
configuration generation"]</TaskList>
        <StatusMessage>The configuration is in effect.</StatusMessage>
        <SuccessCode>1</SuccessCode>
        <Result>{"id": 58, "version": "58@time-1598338353", "websites": [], "target": "
logic_expr", "pattern": {"$AND": [{"infix": {"urlpath": "1234567"}}]}, "action": "modif y_module", "is_enabled": true, "is_expired": false, "comment": "test-module-rule-1", "a ttack_type": -1, "log_option": "Persistence", "create_time": "1598338348", "last_update_time": "1598338353", "expire_time": null, "is_global": false, "forbidden_page_config": null, "priority": 0, "module_management": {"disabled": ["m_sql i"], "enabled": []}, "risk_level": 0, "extra": null}</Result>
    </TaskStatus>
</EditDetectionModuleRuleResponse>
```

`JSON` format `{`

```json
  "RequestId":"53e59af3-3209-452a-853c-ac10ad815929",
  "TaskStatus":{
    "TaskId":"c68646a1-58f8-4b75-828a-a2d3b19b382a",
    "TaskList":"[\"Website-related configuration generation\", \"Policy-related
configuration generation\"]",
    "SuccessCode":"1",
    "Time":"1593593692",
    "StatusMessage":"The configuration is in effect.",
    "Result":"{\"id\": 58, \"version\": \"58@time-1598338353\", \"websites\": [], \"tar
get\": \"logic_expr\", \"pattern\": {\"$AND\": [{\"infix\": {\"urlpath\": \"1234567\"}}]}, \"action\": \"modify_module\", \"is_enabled\": true, \"is_expired\": f alse, \"comment\": \"test-module-rule-1\", \"attack_type\": -1, \"log_option\": \"Persi stence\", \"create_time\": \"1598338348\", \"last_update_time\": \"1598338353\", \"expi re_time\": null, \"is_global\": false, \"forbidden_page_config\": null, \"priority\": 0 , \"module_management\": {\"disabled\": [\"m_sqli\"], \"enabled\": []}, \"risk_level\": 0, \"extra\": null}"
```

`}` `}`

**Error codes**

For a list of error codes, see Error codes.

#### 4.4.10 EditPolicyRuleWebsiteBinding

Modifies the binding relationship between a specific website and its custom rules.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | EditPolicyRule WebsiteBindin g | The operation that you want to perform. Set the value to EditPolicyRuleWebsiteBinding. |
| RegionId | String | Yes | cn-hangzhou |   |
| WebsiteId | Integer | No | 101 | The ID of the website for which you want to modify the binding relationship. |
| PolicyRuleIdL ist | Integer | No | 10 | The ID of the custom rule. You can enter multiple IDs. You can call the DescribePolicyRule operation to query the IDs of custom rules. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|

| RequestId | String | 53e59af3-3209- 452a-853c- ac10ad815929 | The ID of the request. |
|---|---|---|---|
| TaskStatus | Struct |   |   |
| └TaskId | String | c68646a1-58f8- 4b75-828a- a2d3b19b382a | The ID of the task. |
| └Time | String | 1593593692 | The time when the task status message was generated. This value is a UNIX timestamp representing the number of seconds that have elapsed since the epoch time January 1, 1970, 00:00:00 UTC. |
| └TaskList | String | ["Website-related configuration generation", "Policy-related configuration generation"] | The descriptions of the task. This value is returned only for asynchronous tasks. |
| └StatusMess age | String | The configuration is in effect. | The status message of the task. You can ignore this reserved parameter. |
| └SuccessCod e | └Result | String | The status code of the task. Valid values: 0: The task fails. 1: The task is successful. 2: The task is not started. |
| └Result | String | {"website": 12, "policy rule ids": _ _ [12, 17]} | The returned result of the request. |

**Examples**

Sample requests

```
https://semawaf.[ RegionId].aliyuncs.com/?Action=EditPolicyRuleWebsiteBinding &RegionId=cn-hangzhou &WebsiteId=101 &PolicyRuleIdList.1=3
```

Sample success responses `XML` format

```xml
<EditPolicyRuleWebsiteBindingResponse>
    <RequestId>53e59af3-3209-452a-853c-ac10ad815929</RequestId>
    <TaskStatus>
        <TaskId>c68646a1-58f8-4b75-828a-a2d3b19b382a</TaskId>
        <Time>1593593692</Time>
        <TaskList>["Website-related configuration generation", "Policy-related
configuration generation"]</TaskList>
        <StatusMessage>The configuration is in effect.</StatusMessage>
        <SuccessCode>1</SuccessCode>
        <Result>{"website": 12, "policy_rule_ids": [12, 17]}</Result>
    </TaskStatus>
</EditPolicyRuleWebsiteBindingResponse>
```

`JSON` format `{`

```json
  "RequestId":"53e59af3-3209-452a-853c-ac10ad815929",
  "TaskStatus":{
    "TaskId":"c68646a1-58f8-4b75-828a-a2d3b19b382a",
    "TaskList":"[\"Website-related configuration generation\", \"Policy-related
configuration generation\"]",
    "SuccessCode":"1",
    "Time":"1593593692",
    "StatusMessage":"The configuration is in effect.",
    "Result":"{\"website\": 12, \"policy_rule_ids\": [12, 17]}"
```

`}` `}`

**Error codes**

For a list of error codes, see Error codes.

#### 4.4.11 DeletePolicyRuleWebsiteBinding

Deletes the binding relationship between a specific website and specific custom rules.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeletePolicyRu leWebsiteBindi ng | The operation that you want to perform. Set the value to DeletePolicyRuleWebsiteBinding. |
| RegionId | String | Yes | cn-hangzhou |   |
| WebsiteId | Integer | No | 101 | The ID of the website for which you want to modify the binding relationship. |

| PolicyRuleIdL ist | Integer | No | 10 | The ID of the custom rule. You can enter multiple IDs. You can call the DescribePolicyRule operation to query the IDs of custom rules. |
|---|---|---|---|---|

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 53e59af3-3209- 452a-853c- ac10ad815929 | The ID of the request. |
| TaskStatus | Struct |   |   |
| └TaskId | String | c68646a1-58f8- 4b75-828a- a2d3b19b382a | The ID of the task. |
| └Time | String | 1593593692 | The time when the task status message was generated. This value is a UNIX timestamp representing the number of seconds that have elapsed since the epoch time January 1, 1970, 00:00:00 UTC. |
| └TaskList | String | ["Website-related configuration generation", "Policy-related configuration generation"] | The descriptions of the task. This value is returned only for asynchronous tasks. |
| └StatusMess age | String | The configuration is in effect. | The status message of the task. You can ignore this reserved parameter. |
| └SuccessCod e | └Result | String | The status code of the task. Valid values: 0: The task fails. 1: The task is successful. 2: The task is not started. |

**Examples**

Sample requests

```
https://semawaf.[ RegionId].aliyuncs.com/?Action=DeletePolicyRuleWebsiteBinding &RegionId=cn-hangzhou &WebsiteId=101 &PolicyRuleId=12
```

Sample success responses `XML` format

```xml
<DeletePolicyRuleWebsiteBindingResponse>
    <RequestId>53e59af3-3209-452a-853c-ac10ad815929</RequestId>
    <TaskStatus>
        <TaskId>c68646a1-58f8-4b75-828a-a2d3b19b382a</TaskId>
        <Time>1593593692</Time>
        <TaskList>["Website-related configuration generation", "Policy-related
configuration generation"]</TaskList>
        <StatusMessage>The configuration is in effect.</StatusMessage>
        <SuccessCode>1</SuccessCode>
    </TaskStatus>
</DeletePolicyRuleWebsiteBindingResponse>
```

`JSON` format `{`

```json
  "RequestId":"53e59af3-3209-452a-853c-ac10ad815929",
  "TaskStatus":{
    "TaskId":"c68646a1-58f8-4b75-828a-a2d3b19b382a",
    "TaskList":"[\"Website-related configuration generation\", \"Policy-related
configuration generation\"]",
    "SuccessCode":"1",
    "Time":"1593593692",
    "StatusMessage":"The configuration is in effect."
```

`}` `}`

**Error codes**

For a list of error codes, see Error codes.

### 4.5 Protection policies

#### 4.5.1 DescribePolicyGroup

Queries the information about protection policies.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribePolicy Group | The operation that you want to perform. Set the value to DescribePolicyGroup. |
| RegionId | String | Yes | cn-hangzhou |   |
| Id | Integer | No | 101 | The ID of the protection policy. |

**Response parameters**

| Paramete r | Type | Example | Descriptio n |
|---|---|---|---|

| RequestId | String | 53e59af3-3209-452a-853c-ac10ad815929 | The ID of the request. |
|---|---|---|---|
| Result | String | DescribePolicyGroup": "[{"id": 6, "is timeout enabled": _ _ true, "name": "Default Policy Strategy", "create time": _ "1589275411", "last update time": "1594607697", _ _ "is default": true, "modules state": true, _ _ "response detection state": true, _ _ "response detection max body size": 1024, _ _ _ _ "response detection generate log": false, _ _ _ "request detection max body size": 1024, _ _ _ _ "detection timeout threshold": 1000, _ _ "log detection timeout event": true, _ _ _ "forbidden page config": {"action": "response", _ _ "status code": 405, "path": ""}, _ "modules detection config": {"m cmd injection": _ _ _ _ {"low risk enable log": 1, "high risk enable log": 1, _ _ _ _ _ _ "low risk action": "continue", "medium risk action": _ _ _ _ "continue", "state": "disabled", "medium risk enable log": 1, "high risk action": _ _ _ _ _ "deny"}, "m scanner": {"low risk enable log": 1, _ _ _ _ "high risk enable log": 1, "detect config": _ _ _ _ {"robot types": ["scanner"]}, "low risk action": _ _ _ "continue", "medium risk action": "continue", "state": _ _ "disabled", "medium risk enable log": 1, _ _ _ "high risk action": "deny"}, "m file include": _ _ _ _ {"low risk enable log": 1, "high risk enable log": 1, _ _ _ _ _ _ "low risk action": "continue", "medium risk action": _ _ _ _ "continue", "state": "enabled", "medium risk enable log": 1, "high risk action": _ _ _ _ _ "deny"}, "m php code injection": _ _ _ {"low risk enable log": 1, "high risk enable log": 1, _ _ _ _ _ _ "detect config": {"detect upload file": true}, _ _ _ "low risk action": "continue", "medium risk action": _ _ _ _ "continue", "state": "enabled", "medium risk enable log": 1, "high risk action": _ _ _ _ _ "deny"}, "m response": {"low risk enable log": 1, _ _ _ _ "high risk enable log": 1, "detect config": _ _ _ _ {"error types": ["directory indexing", "SQL execution _ error", "server exception"]}, "low risk action": _ _ "continue", "medium risk action": "continue", "state": _ _ "disabled", "medium risk enable log": 1, _ _ _ "high risk action": "deny"}, "m java unserialize": _ _ _ _ {"low risk enable log": 1, "high risk enable log": 1, _ _ _ _ _ _ "low risk action": "continue", "medium risk action": _ _ _ _ "continue", "state": "enabled", "medium risk enable log": 1, "high risk action": _ _ _ _ _ "deny"}, "m sqli": {"low risk enable log": 1, _ _ _ _ "high risk enable log": 1, "detect config": _ _ _ _ {"detect non injection sql": true}, "low risk action": _ _ _ _ _ "continue", "medium risk action": "continue", "state": _ _ "enabled", "medium risk enable log": 1, _ _ _ "high risk action": "deny"}, "m csrf": _ _ _ {"low risk enable log": 1, "high risk enable log": 1, _ _ _ _ _ _ "low risk action": "continue", "medium risk action": _ _ _ _ "continue", "state": "enabled", "medium risk enable log": 1, "high risk action": _ _ _ _ _ "deny"}, "m java": {"low risk enable log": 1, _ _ _ _ "high risk enable log": 1, "detect config": _ _ _ _ {"detect upload file": true}, "low risk action": _ _ _ _ "continue", "medium risk action": "continue", "state": _ _ "enabled", "medium risk enable log": 1, _ _ _ "high risk action": "deny"}, "m file upload": _ _ _ _ {"low risk enable log": 1, "high risk enable log": 1, _ _ _ _ _ _ "low risk action": "continue", "medium risk action": _ _ _ _ | The returned result of the request. |

|   |   | "continue", "state": "enabled", "medium risk enable log": 1, "high risk action": _ _ _ _ _ "deny"}, "m php unserialize": {"low risk enable log": 1, _ _ _ _ _ "high risk enable log": 1, "low risk action": "continue", _ _ _ _ _ "medium risk action": "continue", "state": "enabled", _ _ "medium risk enable log": 1, "high risk action": _ _ _ _ _ "deny"}, "m rule": {"low risk enable log": 1, _ _ _ _ "high risk enable log": 1, "detect config": _ _ _ _ {"info leak types": ["test file", "backup file", "code _ _ repository", "server sensitive file"], "check info leak by rsp": false, "detection configure": _ _ _ _ _ ["detect phpinfo", "detect admin page", _ _ _ "detect backdoor", "detect php vuln", "detect nginx", _ _ _ _ "detect dedecms", "detect apache", "detect xml", _ _ _ "detect struts2", "detect java vuln", "detect php168", _ _ _ _ "detect wordpress", "detect directory traversal", _ _ _ "detect iis", "detect gogs gitea", "detect thinkphp", _ _ _ _ "detect jenkins", "detect ecshop", "detect nexus", _ _ _ "detect drupal", "detect ghostscript", "detect atlassian", _ _ _ "detect weblogic", "detect coremail", "detect phpcms", _ _ _ "detect spring", "detect southidc", "detect fastjson", _ _ _ "detect tbk dvr", "detect joomla", "detect ecology oa", _ _ _ _ _ "detect jackson", "detect xstream", "detect activemq", _ _ _ "detect solr"]}, "low risk action": "continue", _ _ _ "medium risk action": "continue", "state": "enabled", _ _ "medium risk enable log": 1, "high risk action": _ _ _ _ _ "deny"}, "m ssrf": {"low risk enable log": 1, _ _ _ _ "high risk enable log": 1, "low risk action": "continue", _ _ _ _ _ "medium risk action": "continue", "state": "enabled", _ _ "medium risk enable log": 1, "high risk action": _ _ _ _ _ "deny"}, "m xss": {"low risk enable log": 1, _ _ _ _ "high risk enable log": 1, "detect config": _ _ _ _ {"detect complete html": true}, "low risk action": _ _ _ _ "continue", "medium risk action": "continue", "state": _ _ "enabled", "medium risk enable log": 1, _ _ _ "high risk action": "deny"}, "m asp code injection": _ _ _ _ _ {"state": "disabled", "high risk action": "deny", _ _ "high risk enable log": 1, "medium risk action": _ _ _ _ _ "continue", "medium risk enable log": 1, _ _ _ "low risk action": "continue", "low risk enable log": 1, _ _ _ _ _ "detect config": {}}, "m ssti": {"state": "disabled", _ _ "high risk action": "deny", "high risk enable log": 1, _ _ _ _ _ "medium risk action": "continue", _ _ "medium risk enable log": 1, "low risk action": _ _ _ _ _ "continue", "low risk enable log": 1, "detect config": _ _ _ _ {}}}, "misc detection config": {"decode config": _ _ _ {"decode methods": ["url decode", "JSON", "base64", _ |   |
|---|---|---|---|
|   |   | "hex", "eval", "XML", "utf7"]}}}] |   |

**Examples**

Sample requests

```
https://semawaf.[ RegionId].aliyuncs.com/?Action=DescribePolicyGroup &RegionId=cn-hangzhou &Id=1
```

Sample success responses `XML` format

```xml
<DescribePolicyGroupResponse>
    <RequestId>53e59af3-3209-452a-853c-ac10ad815929</RequestId>
    <Result>DescribePolicyGroup": "[{"id": 6, "istimeoutenabled": true, "name": "Defa
```

`_` `_`

```json
ult Policy Strategy", "create_time": "1589275411", "last_update_time": "1594607697", "i s_default": true, "modules_state": true, "response_detection_state": true, "response_detection_max_body_size": 1024, "response_detection_generate_log": false, "re quest_detection_max_body_size": 1024, "detection_timeout_threshold": 1000, "log_detection_timeout_event": true, "forbidden_page_config": {"action": "response", "s tatus_code": 405, "path": ""}, "modules_detection_config": {"m_cmd_injection": {"low_ri sk_enable_log": 1, "high_risk_enable_log": 1, "low_risk_action": "continue", "medium_risk_action": "continue", "state": "disabled", "medium_risk_enable_log": 1, "hi gh_risk_action": "deny"}, "m_scanner": {"low_risk_enable_log": 1, "high_risk_enable_log": 1, "detect_config": {"robot_types": ["scanner"]}, "low_risk_action": "continue", "medium_risk_action": "continue", "state": "disabled", " medium_risk_enable_log": 1, "high_risk_action": "deny"}, "m_file_include": {"low_risk_enable_log": 1, "high_risk_enable_log": 1, "low_risk_action": "continue", "m edium_risk_action": "continue", "state": "enabled", "medium_risk_enable_log": 1, "high_ risk_action": "deny"}, "m_php_code_injection": {"low_risk_enable_log": 1, "high_risk_enable_log": 1, "detect_config": {"detect_upload_file": true}, "low_risk_action": "continue", "medium_risk_action": "continue", "state": "enabled", "m edium_risk_enable_log": 1, "high_risk_action": "deny"}, "m_response": {"low_risk_enable_log": 1, "high_risk_enable_log": 1, "detect_config": {"error_types": ["directory indexing", "SQL execution error", "server exception"]}, "low_risk_action": "continue", "medium_risk_action": "continue", "state": "disabled", "medium_risk_enable_log": 1, "high_risk_action": "deny"}, "m_java_unserialize": {"low_r isk_enable_log": 1, "high_risk_enable_log": 1, "low_risk_action": "continue", "medium_risk_action": "continue", "state": "enabled", "medium_risk_enable_log": 1, "hig h_risk_action": "deny"}, "m_sqli": {"low_risk_enable_log": 1, "high_risk_enable_log": 1 , "detect_config": {"detect_non_injection_sql": true}, "low_risk_action": "continue", " medium_risk_action": "continue", "state": "enabled", "medium_risk_enable_log": 1, "high _risk_action": "deny"}, "m_csrf": {"low_risk_enable_log": 1, "high_risk_enable_log": 1, "low_risk_action": "continue", "medium_risk_action": "continue", "state": "enabled", "m edium_risk_enable_log": 1, "high_risk_action": "deny"}, "m_java": {"low_risk_enable_log": 1, "high_risk_enable_log": 1, "detect_config": {"detect_upload_file": true}, "low_risk_action": "continue", "medium_risk_action": "con tinue", "state": "enabled", "medium_risk_enable_log": 1, "high_risk_action": "deny"}, " m_file_upload": {"low_risk_enable_log": 1, "high_risk_enable_log": 1, "low_risk_action": "continue", "medium_risk_action": "continue", "state": "enabled", "m edium_risk_enable_log": 1, "high_risk_action": "deny"}, "m_php_unserialize": {"low_risk _enable_log": 1, "high_risk_enable_log": 1, "low_risk_action": "continue", "medium_risk_action": "continue", "state": "enabled", "medium_risk_enable_log": 1, "hig h_risk_action": "deny"}, "m_rule": {"low_risk_enable_log": 1, "high_risk_enable_log": 1 , "detect_config": {"info_leak_types": ["test file", "backup file", "code repository", "server sensitive file"], "check_info_leak_by_rsp": false, "detection_configure": ["det ect_phpinfo", "detect_admin_page", "detect_backdoor", "detect_php_vuln", "detect_nginx", "detect_dedecms", "detect_apache", "detect_xml", "detect_struts2", "det ect_java_vuln", "detect_php168", "detect_wordpress", "detect_directory_traversal", "det ect_iis", "detect_gogs_gitea", "detect_thinkphp", "detect_jenkins", "detect_ecshop", "d etect_nexus", "detect_drupal", "detect_ghostscript", "detect_atlassian", "detect_weblogic", "detect_coremail", "detect_phpcms", "detect_spring", "detect_southidc", "detect_fastjson", "detect_tbk_dvr", "detect_joomla", "detect_ecology_oa", "detect_jackson", "detect_xstream", "detect_activemq", "detect_solr"]}, "low_risk_action": "continue", "medium_risk_action": "continue", "stat e": "enabled", "medium_risk_enable_log": 1, "high_risk_action": "deny"}, "m_ssrf": {"lo w_risk_enable_log": 1, "high_risk_enable_log": 1, "low_risk_action": "continue", "mediu m_risk_action": "continue", "state": "enabled", "medium_risk_enable_log": 1, "high_risk _action": "deny"}, "m_xss": {"low_risk_enable_log": 1, "high_risk_enable_log": 1, "dete
```

```json
ct_config": {"detect_complete_html": true}, "low_risk_action": "continue", "medium_risk_action": "continue", "state": "enabled", "medium_risk_enable_log": 1, "hig h_risk_action": "deny"}, "m_asp_code_injection": {"state": "disabled", "high_risk_action": "deny", "high_risk_enable_log": 1, "medium_risk_action": "continue", "medium_risk_enable_log": 1, "low_risk_action": "continue", "low_risk_enable_log": 1, "detect_config": {}}, "m_ssti": {"state": "disabled", "high_r isk_action": "deny", "high_risk_enable_log": 1, "medium_risk_action": "continue", "medi um_risk_enable_log": 1, "low_risk_action": "continue", "low_risk_enable_log": 1, "detec t_config": {}}}, "misc_detection_config": {"decode_config": {"decode_methods": ["url de code", "JSON", "base64", "hex", "eval", "XML", "utf7"]}}}]</Result> </DescribePolicyGroupResponse>
```

`JSON` format `{`

```json
  "RequestId":"53e59af3-3209-452a-853c-ac10ad815929",
  "Result":"DescribePolicyGroup\": \"[{\"id\": 6, \"is_timeout_enabled\": true, \"name\
": \"Default Policy Strategy\", \"create_time\": \"1589275411\", \"last_update_time\": \"1594607697\", \"is_default\": true, \"modules_state\": true, \"response_detection_state\": true, \"response_detection_max_body_size\": 1024, \"respo nse_detection_generate_log\": false, \"request_detection_max_body_size\": 1024, \"detec tion_timeout_threshold\": 1000, \"log_detection_timeout_event\": true, \"forbidden_page_config\": {\"action\": \"response\", \"status_code\": 405, \"path\": \ "\"}, \"modules_detection_config\": {\"m_cmd_injection\": {\"low_risk_enable_log\": 1, \"high_risk_enable_log\": 1, \"low_risk_action\": \"continue\", \"medium_risk_action\": \"continue\", \"state\": \"disabled\", \"medium_risk_enable_log\": 1, \"high_risk_action\": \"deny\"}, \"m_scanner\": {\"low_risk_enable_log\": 1, \"high_risk_enable_log\": 1, \"detect_config\": {\"robot_types\": [\"scanner\"]}, \"low _risk_action\": \"continue\", \"medium_risk_action\": \"continue\", \"state\": \"disabled\", \"medium_risk_enable_log\": 1, \"high_risk_action\": \"deny\"}, \"m_file_ include\": {\"low_risk_enable_log\": 1, \"high_risk_enable_log\": 1, \"low_risk_action\": \"continue\", \"medium_risk_action\": \"continue\", \"state\": \"e nabled\", \"medium_risk_enable_log\": 1, \"high_risk_action\": \"deny\"}, \"m_php_code_injection\": {\"low_risk_enable_log\": 1, \"high_risk_enable_log\": 1, \"d etect_config\": {\"detect_upload_file\": true}, \"low_risk_action\": \"continue\", \"me dium_risk_action\": \"continue\", \"state\": \"enabled\", \"medium_risk_enable_log\": 1 , \"high_risk_action\": \"deny\"}, \"m_response\": {\"low_risk_enable_log\": 1, \"high_ risk_enable_log\": 1, \"detect_config\": {\"error_types\": [\"directory indexing\", \"S QL execution error\", \"server exception\"]}, \"low_risk_action\": \"continue\", \"medi um_risk_action\": \"continue\", \"state\": \"disabled\", \"medium_risk_enable_log\": 1, \"high_risk_action\": \"deny\"}, \"m_java_unserialize\": {\"low_risk_enable_log\": 1, \ "high_risk_enable_log\": 1, \"low_risk_action\": \"continue\", \"medium_risk_action\": \"continue\", \"state\": \"enabled\", \"medium_risk_enable_log\": 1, \"high_risk_action\": \"deny\"}, \"m_sqli\": {\"low_risk_enable_log\": 1, \"high_risk_enable_log\": 1, \"detect_config\": {\"detect_non_injection_sql\": true}, \ "low_risk_action\": \"continue\", \"medium_risk_action\": \"continue\", \"state\": \"en abled\", \"medium_risk_enable_log\": 1, \"high_risk_action\": \"deny\"}, \"m_csrf\": {\ "low_risk_enable_log\": 1, \"high_risk_enable_log\": 1, \"low_risk_action\": \"continue\", \"medium_risk_action\": \"continue\", \"state\": \"enabled\", \"medium_risk_enable_log\": 1, \"high_risk_action\": \"deny\"}, \"m_java\": {\"low_risk _enable_log\": 1, \"high_risk_enable_log\": 1, \"detect_config\": {\"detect_upload_file\": true}, \"low_risk_action\": \"continue\", \"medium_risk_action\": \"continue\", \"state\": \"enabled\", \"mediumriskenablelog\": 1, \"highriskaction\": \"deny\"}, \"mfileupload\": {\"l
```

\ `_` `_` `_` g\ `,`\ `g``_` `_` \ \

```
y\},\
```

`_` `_``p` \ {\

```
ow_risk_enable_log\": 1, \"high_risk_enable_log\": 1, \"low_risk_action\": \"continue\", \"medium_risk_action\": \"continue\", \"state\": \"enabled\", \"medium_risk_enable_log\": 1, \"high_risk_action\": \"deny\"}, \"m_php_unserialize\": {\"low_risk_enable_log\": 1, \"high_risk_enable_log\": 1, \"low_risk_action\": \"contin ue\", \"medium_risk_action\": \"continue\", \"state\": \"enabled\", \"medium_risk_enable_log\": 1, \"high_risk_action\": \"deny\"}, \"m_rule\": {\"low_risk _enable_log\": 1, \"high_risk_enable_log\": 1, \"detect_config\": {\"info_leak_types\": [\"test file\", \"backup file\", \"code repository\", \"server sensitive file\"], \"che ck_info_leak_by_rsp\": false, \"detection_configure\": [\"detect_phpinfo\", \"detect_ad min_page\", \"detect_backdoor\", \"detect_php_vuln\", \"detect_nginx\", \"detect_dedecms\", \"detect_apache\", \"detect_xml\", \"detect_struts2\", \"detect_java_vuln\", \"detect_php168\", \"detect_wordpress\", \"detect_directory_traversal\", \"detect_iis\", \"detect_gogs_gitea\", \"detect_thinkphp\", \"detect_jenkins\", \"detect_ecshop\", \"detect_nexus\", \"detect_ drupal\", \"detect_ghostscript\", \"detect_atlassian\", \"detect_weblogic\", \"detect_c oremail\", \"detect_phpcms\", \"detect_spring\", \"detect_southidc\", \"detect_fastjson\", \"detect_tbk_dvr\", \"detect_joomla\", \"detect_ecology_oa\", \"de tect_jackson\", \"detect_xstream\", \"detect_activemq\", \"detect_solr\"]}, \"low_risk_action\": \"continue\", \"medium_risk_action\": \"continue\", \"state\": \"e nabled\", \"medium_risk_enable_log\": 1, \"high_risk_action\": \"deny\"}, \"m_ssrf\": { \"low_risk_enable_log\": 1, \"high_risk_enable_log\": 1, \"low_risk_action\": \"continue\", \"medium_risk_action\": \"continue\", \"state\": \"enabled\", \"medium_risk_enable_log\": 1, \"high_risk_action\": \"deny\"}, \"m_xss\": {\"low_risk_enable_log\": 1, \"high_risk_enable_log\": 1, \"detect_config\": {\"detect_complete_html\": true}, \"low_risk_action\": \"continue\", \"medium_risk_action\": \"continue\", \"state\": \"enabled\", \"medium_risk_enable_log\": 1, \"high_risk_action\": \"deny\"}, \"m_asp_code_injection\": {\"state\": \"disabled\", \"high_risk_action\": \"deny\", \"h igh_risk_enable_log\": 1, \"medium_risk_action\": \"continue\", \"medium_risk_enable_log\": 1, \"low_risk_action\": \"continue\", \"low_risk_enable_log\": 1, \"detect_config\": {}}, \"m_ssti\": {\"state\": \"disabled\", \"high_risk_action\": \"deny\", \"high_risk_enable_log\": 1, \"medium_risk_action\": \"continue\", \"medium_risk_enable_log\": 1, \"low_risk_action\": \"continue\", \"low_risk_enable_log\": 1, \"detect_config\": {}}}, \"misc_detection_config\": {\"decode_config\": {\"decode_methods\": [\"url decode\", \" JSON\", \"base64\", \"hex\", \"eval\", \"XML\", \"utf7\"]}}}]"
```

`}`

**Error codes**

For a list of error codes, see Error codes.

#### 4.5.2 CreatePolicyGroup

Creates a protection policy.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreatePolicyGr oup | The operation that you want to perform. Set the value to CreatePolicyGroup. |

| RegionId | String | Yes | cn-hangzhou |   |
|---|---|---|---|---|
| PolicyGroupN ame | String | Yes | Loose protection policy | The name of the protection policy. |

**Response parameters**

| Paramete r | Type | Example | Descriptio n |
|---|---|---|---|
| RequestId | String | 53e59af3-3209-452a-853c-ac10ad815929 | The ID of the request. |
|   |   | {"id": 75, "is timeout enabled": true, "name": "policy- _ _ group-test", "create time": "1594695152", _ "last update time": "1594695152", "is default": false, _ _ _ "modules state": true, "response detection state": true, _ _ _ "response detection max body size": 1024, _ _ _ _ "response detection generate log": false, _ _ _ "request detection max body size": 1024, _ _ _ _ "detection timeout threshold": 1000, _ _ "log detection timeout event": true, _ _ _ "forbidden page config": {"action": "response", _ _ "status code": 405, "path": ""}, _ "modules detection config": {"m cmd injection": _ _ _ _ {"low risk enable log": 1, "high risk enable log": 1, _ _ _ _ _ _ "low risk action": "continue", "medium risk action": _ _ _ _ "continue", "state": "disabled", "medium risk enable log": 1, "high risk action": _ _ _ _ _ "deny"}, "m scanner": {"low risk enable log": 1, _ _ _ _ "high risk enable log": 1, "detect config": _ _ _ _ {"robot types": ["scanner"]}, "low risk action": _ _ _ "continue", "medium risk action": "continue", "state": _ _ "disabled", "medium risk enable log": 1, _ _ _ "high risk action": "deny"}, "m file include": _ _ _ _ {"low risk enable log": 1, "high risk enable log": 1, _ _ _ _ _ _ "low risk action": "continue", "medium risk action": _ _ _ _ "continue", "state": "enabled", "medium risk enable log": 1, "high risk action": _ _ _ _ _ "deny"}, "m php code injection": _ _ _ {"low risk enable log": 1, "high risk enable log": 1, _ _ _ _ _ _ "detect config": {"detect upload file": true}, _ _ _ "low risk action": "continue", "medium risk action": _ _ _ _ "continue", "state": "enabled", "medium risk enable log": 1, "high risk action": _ _ _ _ _ "deny"}, "m response": {"low risk enable log": 1, _ _ _ _ "high risk enable log": 1, "detect config": _ _ _ _ {"error types": ["directory indexing", "SQL execution _ error", "server exception"]}, "low risk action": _ _ "continue", "medium risk action": "continue", "state": _ _ "disabled", "medium risk enable log": 1, _ _ _ "high risk action": "deny"}, "m java unserialize": _ _ _ _ {"low risk enable log": 1, "high risk enable log": 1, _ _ _ _ _ _ "low risk action": "continue", "medium risk action": _ _ _ _ "continue", "state": "enabled", "medium risk enable log": 1, "high risk action": _ _ _ _ _ "deny"}, "m sqli": {"low risk enable log": 1, _ _ _ _ "high risk enable log": 1, "detect config": _ _ _ _ {"detect non injection sql": true}, "low risk action": _ _ _ _ _ "continue", "medium risk action": "continue", "state": _ _ "enabled", "medium risk enable log": 1, _ _ _ "high risk action": "deny"}, "m csrf": _ _ _ |   |

| Result | String | {"low risk enable log": 1, "high risk enable log": 1, _ _ _ _ _ _ "low risk action": "continue", "medium risk action": _ _ _ _ "continue", "state": "enabled", "medium risk enable log": 1, "high risk action": _ _ _ _ _ "deny"}, "m java": {"low risk enable log": 1, _ _ _ _ "high risk enable log": 1, "detect config": _ _ _ _ {"detect upload file": true}, "low risk action": _ _ _ _ "continue", "medium risk action": "continue", "state": _ _ "enabled", "medium risk enable log": 1, _ _ _ "high risk action": "deny"}, "m file upload": _ _ _ _ {"low risk enable log": 1, "high risk enable log": 1, _ _ _ _ _ _ "low risk action": "continue", "medium risk action": _ _ _ _ "continue", "state": "enabled", "medium risk enable log": 1, "high risk action": _ _ _ _ _ "deny"}, "m php unserialize": {"low risk enable log": 1, _ _ _ _ _ "high risk enable log": 1, "low risk action": "continue", _ _ _ _ _ "medium risk action": "continue", "state": "enabled", _ _ "medium risk enable log": 1, "high risk action": _ _ _ _ _ "deny"}, "m rule": {"low risk enable log": 1, _ _ _ _ "high risk enable log": 1, "detect config": _ _ _ _ {"info leak types": ["test file", "backup file", "code _ _ repository", "server sensitive file"], "check info leak by rsp": false, "detection configure": _ _ _ _ _ ["detect phpinfo", "detect admin page", _ _ _ "detect backdoor", "detect php vuln", "detect nginx", _ _ _ _ "detect dedecms", "detect apache", "detect xml", _ _ _ "detect struts2", "detect java vuln", "detect php168", _ _ _ _ "detect wordpress", "detect directory traversal", _ _ _ "detect iis", "detect gogs gitea", "detect thinkphp", _ _ _ _ "detect jenkins", "detect ecshop", "detect nexus", _ _ _ "detect drupal", "detect ghostscript", "detect atlassian", _ _ _ "detect weblogic", "detect coremail", "detect phpcms", _ _ _ "detect spring", "detect southidc", "detect fastjson", _ _ _ "detect tbk dvr", "detect joomla", "detect ecology oa", _ _ _ _ _ | The returned result of the request. |
|---|---|---|---|
|   |   | "detect jackson", "detect xstream", "detect activemq", _ _ _ "detect solr"]}, "low risk action": "continue", _ _ _ "medium risk action": "continue", "state": "enabled", _ _ "medium risk enable log": 1, "high risk action": _ _ _ _ _ "deny"}, "m ssrf": {"low risk enable log": 1, _ _ _ _ "high risk enable log": 1, "low risk action": "continue", _ _ _ _ _ "medium risk action": "continue", "state": "enabled", _ _ "medium risk enable log": 1, "high risk action": _ _ _ _ _ "deny"}, "m xss": {"low risk enable log": 1, _ _ _ _ "high risk enable log": 1, "detect config": _ _ _ _ {"detect complete html": true}, "low risk action": _ _ _ _ "continue", "medium risk action": "continue", "state": _ _ "enabled", "medium risk enable log": 1, _ _ _ "high risk action": "deny"}, "m asp code injection": _ _ _ _ _ {"state": "disabled", "high risk action": "deny", _ _ "high risk enable log": 1, "medium risk action": _ _ _ _ _ "continue", "medium risk enable log": 1, _ _ _ "low risk action": "continue", "low risk enable log": 1, _ _ _ _ _ "detect config": {}}, "m ssti": {"state": "disabled", _ _ "high risk action": "deny", "high risk enable log": 1, _ _ _ _ _ "medium risk action": "continue", _ _ "medium risk enable log": 1, "low risk action": _ _ _ _ _ "continue", "low risk enable log": 1, "detect config": _ _ _ _ {}}}, "misc detection config": {"decode config": _ _ _ {"decode methods": ["url decode", "JSON", "base64", _ "hex", "eval", "XML", "utf7"]}}} |   |

**Examples**

Sample requests

```
https://semawaf.[ RegionId].aliyuncs.com/?Action=CreatePolicyGroup &RegionId=cn-hangzhou &PolicyGroupName=Loose protection policy
```

Sample success responses `XML` format

```json
<CreatePolicyGroupResponse>
    <RequestId>53e59af3-3209-452a-853c-ac10ad815929</RequestId>
    <Result>{"id": 75, "is_timeout_enabled": true, "name": "policy-group-test", "create
_time": "1594695152", "last_update_time": "1594695152", "is_default": false, "modules_state": true, "response_detection_state": true, "response_detection_max_body_size": 1024, "response_detection_generate_log": false, "re quest_detection_max_body_size": 1024, "detection_timeout_threshold": 1000, "log_detection_timeout_event": true, "forbidden_page_config": {"action": "response", "s tatus_code": 405, "path": ""}, "modules_detection_config": {"m_cmd_injection": {"low_ri sk_enable_log": 1, "high_risk_enable_log": 1, "low_risk_action": "continue", "medium_risk_action": "continue", "state": "disabled", "medium_risk_enable_log": 1, "hi gh_risk_action": "deny"}, "m_scanner": {"low_risk_enable_log": 1, "high_risk_enable_log": 1, "detect_config": {"robot_types": ["scanner"]}, "low_risk_action": "continue", "medium_risk_action": "continue", "state": "disabled", " medium_risk_enable_log": 1, "high_risk_action": "deny"}, "m_file_include": {"low_risk_enable_log": 1, "high_risk_enable_log": 1, "low_risk_action": "continue", "m edium_risk_action": "continue", "state": "enabled", "medium_risk_enable_log": 1, "high_ risk_action": "deny"}, "m_php_code_injection": {"low_risk_enable_log": 1, "high_risk_enable_log": 1, "detect_config": {"detect_upload_file": true}, "low_risk_action": "continue", "medium_risk_action": "continue", "state": "enabled", "m edium_risk_enable_log": 1, "high_risk_action": "deny"}, "m_response": {"low_risk_enable_log": 1, "high_risk_enable_log": 1, "detect_config": {"error_types": ["directory indexing", "SQL execution error", "server exception"]}, "low_risk_action": "continue", "medium_risk_action": "continue", "state": "disabled", "medium_risk_enable_log": 1, "high_risk_action": "deny"}, "m_java_unserialize": {"low_r isk_enable_log": 1, "high_risk_enable_log": 1, "low_risk_action": "continue", "medium_risk_action": "continue", "state": "enabled", "medium_risk_enable_log": 1, "hig h_risk_action": "deny"}, "m_sqli": {"low_risk_enable_log": 1, "high_risk_enable_log": 1 , "detect_config": {"detect_non_injection_sql": true}, "low_risk_action": "continue", " medium_risk_action": "continue", "state": "enabled", "medium_risk_enable_log": 1, "high _risk_action": "deny"}, "m_csrf": {"low_risk_enable_log": 1, "high_risk_enable_log": 1, "low_risk_action": "continue", "medium_risk_action": "continue", "state": "enabled", "m edium_risk_enable_log": 1, "high_risk_action": "deny"}, "m_java": {"low_risk_enable_log": 1, "high_risk_enable_log": 1, "detect_config": {"detect_upload_file": true}, "low_risk_action": "continue", "medium_risk_action": "con tinue", "state": "enabled", "medium_risk_enable_log": 1, "high_risk_action": "deny"}, " m_file_upload": {"low_risk_enable_log": 1, "high_risk_enable_log": 1, "low_risk_action": "continue", "medium_risk_action": "continue", "state": "enabled", "m edium_risk_enable_log": 1, "high_risk_action": "deny"}, "m_php_unserialize": {"low_risk _enable_log": 1, "high_risk_enable_log": 1, "low_risk_action": "continue", "medium_risk_action": "continue", "state": "enabled", "medium_risk_enable_log": 1, "hig h_risk_action": "deny"}, "m_rule": {"low_risk_enable_log": 1, "high_risk_enable_log": 1 , "detect_config": {"info_leak_types": ["test file", "backup file", "code repository", "server sensitive file"], "check_info_leak_by_rsp": false, "detection_configure": ["det ect_phpinfo", "detect_admin_page", "detect_backdoor", "detect_php_vuln", "detect_nginx", "detect_dedecms", "detect_apache", "detect_xml", "detect_struts2", "det
```

```json
ect_java_vuln", "detect_php168", "detect_wordpress", "detect_directory_traversal", "det ect_iis", "detect_gogs_gitea", "detect_thinkphp", "detect_jenkins", "detect_ecshop", "d etect_nexus", "detect_drupal", "detect_ghostscript", "detect_atlassian", "detect_weblogic", "detect_coremail", "detect_phpcms", "detect_spring", "detect_southidc", "detect_fastjson", "detect_tbk_dvr", "detect_joomla", "detect_ecology_oa", "detect_jackson", "detect_xstream", "detect_activemq", "detect_solr"]}, "low_risk_action": "continue", "medium_risk_action": "continue", "stat e": "enabled", "medium_risk_enable_log": 1, "high_risk_action": "deny"}, "m_ssrf": {"lo w_risk_enable_log": 1, "high_risk_enable_log": 1, "low_risk_action": "continue", "mediu m_risk_action": "continue", "state": "enabled", "medium_risk_enable_log": 1, "high_risk _action": "deny"}, "m_xss": {"low_risk_enable_log": 1, "high_risk_enable_log": 1, "dete ct_config": {"detect_complete_html": true}, "low_risk_action": "continue", "medium_risk_action": "continue", "state": "enabled", "medium_risk_enable_log": 1, "hig h_risk_action": "deny"}, "m_asp_code_injection": {"state": "disabled", "high_risk_action": "deny", "high_risk_enable_log": 1, "medium_risk_action": "continue", "medium_risk_enable_log": 1, "low_risk_action": "continue", "low_risk_enable_log": 1, "detect_config": {}}, "m_ssti": {"state": "disabled", "high_r isk_action": "deny", "high_risk_enable_log": 1, "medium_risk_action": "continue", "medi um_risk_enable_log": 1, "low_risk_action": "continue", "low_risk_enable_log": 1, "detec t_config": {}}}, "misc_detection_config": {"decode_config": {"decode_methods": ["url de code", "JSON", "base64", "hex", "eval", "XML", "utf7"]}}}</Result> </CreatePolicyGroupResponse>
```

`JSON` format `{`

```json
  "RequestId":"53e59af3-3209-452a-853c-ac10ad815929",
  "Result":"{\"id\": 75, \"is_timeout_enabled\": true, \"name\": \"policy-group-test\",
\"create_time\": \"1594695152\", \"last_update_time\": \"1594695152\", \"is_default\": false, \"modules_state\": true, \"response_detection_state\": true, \"response_detection_max_body_size\": 1024, \"response_detection_generate_log\": false, \"request_detection_max_body_size\": 1024, \"detection_timeout_threshold\": 1000, \"log _detection_timeout_event\": true, \"forbidden_page_config\": {\"action\": \"response\", \"status_code\": 405, \"path\": \"\"}, \"modules_detection_config\": {\"m_cmd_injection\": {\"low_risk_enable_log\": 1, \"high_risk_enable_log\": 1, \"low_r isk_action\": \"continue\", \"medium_risk_action\": \"continue\", \"state\": \"disabled\", \"medium_risk_enable_log\": 1, \"high_risk_action\": \"deny\"}, \"m_scann er\": {\"low_risk_enable_log\": 1, \"high_risk_enable_log\": 1, \"detect_config\": {\"r obot_types\": [\"scanner\"]}, \"low_risk_action\": \"continue\", \"medium_risk_action\": \"continue\", \"state\": \"disabled\", \"medium_risk_enable_log\": 1, \"high_risk_action\": \"deny\"}, \"m_file_include\": {\" low_risk_enable_log\": 1, \"high_risk_enable_log\": 1, \"low_risk_action\": \"continue\", \"medium_risk_action\": \"continue\", \"state\": \"enabled\", \"medium_risk_enable_log\": 1, \"high_risk_action\": \"deny\"}, \"m_php_code_injection\": {\"low_risk_enable_log\": 1, \"high_risk_enable_log\": 1, \"d etect_config\": {\"detect_upload_file\": true}, \"low_risk_action\": \"continue\", \"me dium_risk_action\": \"continue\", \"state\": \"enabled\", \"medium_risk_enable_log\": 1 , \"high_risk_action\": \"deny\"}, \"m_response\": {\"low_risk_enable_log\": 1, \"high_ risk_enable_log\": 1, \"detect_config\": {\"error_types\": [\"directory indexing\", \"S QL execution error\", \"server exception\"]}, \"low_risk_action\": \"continue\", \"medi um_risk_action\": \"continue\", \"state\": \"disabled\", \"medium_risk_enable_log\": 1, \"high_risk_action\": \"deny\"}, \"m_java_unserialize\": {\"low_risk_enable_log\": 1, \ "high_risk_enable_log\": 1, \"low_risk_action\": \"continue\", \"medium_risk_action\": \"continue\", \"state\": \"enabled\", \"mediumriskenablelog\": 1,
```

```
\cot ue\,\state\:\eabed\,\ edu_ s_eabe_og\:
```

`,`

```
\"high_risk_action\": \"deny\"}, \"m_sqli\": {\"low_risk_enable_log\": 1, \"high_risk_enable_log\": 1, \"detect_config\": {\"detect_non_injection_sql\": true}, \ "low_risk_action\": \"continue\", \"medium_risk_action\": \"continue\", \"state\": \"en abled\", \"medium_risk_enable_log\": 1, \"high_risk_action\": \"deny\"}, \"m_csrf\": {\ "low_risk_enable_log\": 1, \"high_risk_enable_log\": 1, \"low_risk_action\": \"continue\", \"medium_risk_action\": \"continue\", \"state\": \"enabled\", \"medium_risk_enable_log\": 1, \"high_risk_action\": \"deny\"}, \"m_java\": {\"low_risk _enable_log\": 1, \"high_risk_enable_log\": 1, \"detect_config\": {\"detect_upload_file\": true}, \"low_risk_action\": \"continue\", \"medium_risk_action\": \"continue\", \"state\": \"enabled\", \"medium_risk_enable_log\": 1, \"high_risk_action\": \"deny\"}, \"m_file_upload\": {\"l ow_risk_enable_log\": 1, \"high_risk_enable_log\": 1, \"low_risk_action\": \"continue\", \"medium_risk_action\": \"continue\", \"state\": \"enabled\", \"medium_risk_enable_log\": 1, \"high_risk_action\": \"deny\"}, \"m_php_unserialize\": {\"low_risk_enable_log\": 1, \"high_risk_enable_log\": 1, \"low_risk_action\": \"contin ue\", \"medium_risk_action\": \"continue\", \"state\": \"enabled\", \"medium_risk_enable_log\": 1, \"high_risk_action\": \"deny\"}, \"m_rule\": {\"low_risk _enable_log\": 1, \"high_risk_enable_log\": 1, \"detect_config\": {\"info_leak_types\": [\"test file\", \"backup file\", \"code repository\", \"server sensitive file\"], \"che ck_info_leak_by_rsp\": false, \"detection_configure\": [\"detect_phpinfo\", \"detect_ad min_page\", \"detect_backdoor\", \"detect_php_vuln\", \"detect_nginx\", \"detect_dedecms\", \"detect_apache\", \"detect_xml\", \"detect_struts2\", \"detect_java_vuln\", \"detect_php168\", \"detect_wordpress\", \"detect_directory_traversal\", \"detect_iis\", \"detect_gogs_gitea\", \"detect_thinkphp\", \"detect_jenkins\", \"detect_ecshop\", \"detect_nexus\", \"detect_ drupal\", \"detect_ghostscript\", \"detect_atlassian\", \"detect_weblogic\", \"detect_c oremail\", \"detect_phpcms\", \"detect_spring\", \"detect_southidc\", \"detect_fastjson\", \"detect_tbk_dvr\", \"detect_joomla\", \"detect_ecology_oa\", \"de tect_jackson\", \"detect_xstream\", \"detect_activemq\", \"detect_solr\"]}, \"low_risk_action\": \"continue\", \"medium_risk_action\": \"continue\", \"state\": \"e nabled\", \"medium_risk_enable_log\": 1, \"high_risk_action\": \"deny\"}, \"m_ssrf\": { \"low_risk_enable_log\": 1, \"high_risk_enable_log\": 1, \"low_risk_action\": \"continue\", \"medium_risk_action\": \"continue\", \"state\": \"enabled\", \"medium_risk_enable_log\": 1, \"high_risk_action\": \"deny\"}, \"m_xss\": {\"low_risk_enable_log\": 1, \"high_risk_enable_log\": 1, \"detect_config\": {\"detect_complete_html\": true}, \"low_risk_action\": \"continue\", \"medium_risk_action\": \"continue\", \"state\": \"enabled\", \"medium_risk_enable_log\": 1, \"high_risk_action\": \"deny\"}, \"m_asp_code_injection\": {\"state\": \"disabled\", \"high_risk_action\": \"deny\", \"h igh_risk_enable_log\": 1, \"medium_risk_action\": \"continue\", \"medium_risk_enable_log\": 1, \"low_risk_action\": \"continue\", \"low_risk_enable_log\": 1, \"detect_config\": {}}, \"m_ssti\": {\"state\": \"disabled\", \"high_risk_action\": \"deny\", \"high_risk_enable_log\": 1, \"medium_risk_action\": \"continue\", \"medium_risk_enable_log\": 1, \"low_risk_action\": \"continue\", \"low_risk_enable_log\": 1, \"detect_config\": {}}}, \"misc_detection_config\": {\"decode_config\": {\"decode_methods\": [\"url decode\", \" JSON\", \"base64\", \"hex\", \"eval\", \"XML\", \"utf7\"]}}}"
```

`}`

**Error codes**

For a list of error codes, see Error codes.

#### 4.5.3 EditPolicyGroup

Modifies a specific protection policy.

**Request parameters**

| Parameter | Type | Require d | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | EditPolicyGroup | The operation that you want to perform. Set the value to EditPolicyGroup. |
| RegionId | String | Yes | cn-hangzhou |   |
| Id | Integer | Yes | 1 | The ID of the protection policy. You can call the DescribePolicyGroup operation to query the IDs of protection policies. |

| ForbiddenPag eConfig | Json | Yes | {"status code":405,"action":"res _ ponse","path":""} | The configurations to block requests. This parameter is a string consisting of JSON structs. A JSON struct includes the following fields: status code: the _ status code in the responses. This field is required. Data type: integer. Valid values: 200, 301, 302, 307, 400, 403, 404, 501, and 502. action: the method to respond to the requests. This field is required. Data type: string. Valid values: redirect and response. The value redirect indicates that the system redirects the requests. The value response indicates that the system returns specific content. If status code is _ set to 301 or 302, set action to redirect. If status code is set _ to another value, set action to response. path: the destination address for redirection. Data type: string. If action is set to redirect, this field is required. In other cases, leave this field unspecified. |
|---|---|---|---|---|
| ResponseDete ction | Boolean | Yes | true | Specifies whether to enable response detection. Valid values: true false |

| ResponseDete ctionLog | Boolean | No | false | Specifies whether to record response content in attack detection logs. Default value: false. Valid values: true false |
|---|---|---|---|---|
| ResponseDete ctionMaxBody | Integer | Yes | 1024 | The maximum size of a response body for detection. Unit: KB. |
| RequestDetec tionMaxBody | Integer | Yes | 1024 | The maximum size of a request body for detection. Unit: KB. |
| DetectionTim eout | Boolean | Yes | true | Specifies whether to enable detection timeout. Valid values: true false |
| DetectionTim eoutThreshold | Integer | Yes | 1000 | The detection timeout period. Unit: ms. If the DetectionTimeout parameter is set to true, this parameter is required. |
| DetectionTim eoutLog | Boolean | Yes | true | Specifies whether to record detection timeout in attack detection logs. If the DetectionTimeout parameter is set to false, this parameter is unavailable. |
|   |   |   |   | The configurations of the attack detection module. You can call the DescribePolicyGroup operation to query the configurations. We recommend that you use the configurations in the query result. The value is a string that consists of a JSON struct. The JSON struct contains the following fields: detect config: _ the configurations |

|   |   |   | {"m cmd injection": _ _ | of the attack detection module. This field is required. Data type: string. |
|---|---|---|---|---|
|   |   |   | {"low risk enable log": 1, _ _ _ "high risk enable log": 1, _ _ _ "low risk action": "continue", _ _ "medium risk action": _ _ "continue", "state": "disabled", "medium risk enable log": 1, _ _ _ "high risk action": "deny"}, _ _ "m scanner": _ {"low risk enable log": 1, _ _ _ "high risk enable log": 1, _ _ _ "detect config": {"robot types": _ _ ["scanner"]}, "low risk action": _ _ "continue", "medium risk action": _ _ "continue", "state": "disabled", "medium risk enable log": 1, _ _ _ "high risk action": "deny"}, _ _ "m file include": _ _ {"low risk enable log": 1, _ _ _ "high risk enable log": 1, _ _ _ "low risk action": "continue", _ _ "medium risk action": _ _ "continue", "state": "enabled", "medium risk enable log": 1, _ _ _ "high risk action": "deny"}, _ _ "m php code injection": _ _ _ {"low risk enable log": 1, _ _ _ "high risk enable log": 1, _ _ _ "detect config": _ {"detect upload file": true}, _ _ "low risk action": "continue", _ _ "medium risk action": _ _ "continue", "state": "enabled", "medium risk enable log": 1, _ _ _ "high risk action": "deny"}, _ _ "m response": _ {"low risk enable log": 1, _ _ _ "high risk enable log": 1, _ _ _ "detect config": {"error types": _ _ ["directory indexing", "SQL execution error", "server exception"]}, "low risk action": _ _ "continue", "medium risk action": _ _ "continue", "state": "disabled", "medium risk enable log": 1, _ _ _ "high risk action": "deny"}, _ _ "m java unserialize": _ _ {"low risk enable log": 1, _ _ _ "high risk enable log": 1, _ _ _ "low risk action": "continue", _ _ "medium risk action": _ _ "continue", "state": "enabled", "medium risk enable log": 1, _ _ _ "high risk action": "deny"}, _ _ "m sqli": {"low risk enable log": _ _ _ _ 1, "high risk enable log": 1, _ _ _ "detect config": _ {"detect non injection sql": _ _ _ true}, "low risk action": _ _ "continue", "medium risk action": _ _ "continue" "state": "enabled" | high risk action _ _ : the action on requests when the upper threshold for blocking is triggered. This field is required. Data type: string. Valid values: deny and continue. The value deny indicates that requests are blocked. The value continue indicates that requests are not blocked. If the high risk action, _ _ medium risk act _ _ ion, and low risk action _ _ fields are all set to deny, all requests are blocked. If all the three fields are set to continue, no requests are blocked. medium risk act _ _ ion: the action on requests when the medium threshold for blocking is triggered. This field is required. Data type: string. Valid values: deny and continue. The value deny indicates that requests are blocked. The value continue indicates that requests are not blocked. If the high risk action _ _ and medium risk act _ _ ion fields are set to deny and the low risk action _ _ field is set to continue, high- risk and medium- risk requests are blocked. If all the |

| DetectionMod uleConfig | Json | Yes | "continue", "state": "enabled", "medium risk enable log": 1, _ _ _ "high risk action": "deny"}, _ _ "m csrf": {"low risk enable log": _ _ _ _ 1, "high risk enable log": 1, _ _ _ "low risk action": "continue", _ _ "medium risk action": _ _ "continue", "state": "enabled", "medium risk enable log": 1, _ _ _ "high risk action": "deny"}, _ _ "m java": _ {"low risk enable log": 1, _ _ _ "high risk enable log": 1, _ _ _ "detect config": _ {"detect upload file": true}, _ _ "low risk action": "continue", _ _ "medium risk action": _ _ "continue", "state": "enabled", "medium risk enable log": 1, _ _ _ "high risk action": "deny"}, _ _ "m file upload": _ _ {"low risk enable log": 1, _ _ _ "high risk enable log": 1, _ _ _ "low risk action": "continue", _ _ "medium risk action": _ _ "continue", "state": "enabled", "medium risk enable log": 1, _ _ _ "high risk action": "deny"}, _ _ "m php unserialize": _ _ {"low risk enable log": 1, _ _ _ "high risk enable log": 1, _ _ _ "low risk action": "continue", _ _ "medium risk action": _ _ "continue", "state": "enabled", "medium risk enable log": 1, _ _ _ "high risk action": "deny"}, _ _ "m rule": {"low risk enable log": _ _ _ _ 1, "high risk enable log": 1, _ _ _ "detect config": _ {"info leak types": ["test file", _ _ "backup file", "code repository", "server sensitive file"], "check info leak by rsp": false, _ _ _ _ "detection configure": _ ["detect phpinfo", _ "detect admin page", _ _ "detect backdoor", _ "detect php vuln", _ _ "detect nginx", _ "detect dedecms", _ "detect apache", "detect xml", _ _ "detect struts2", _ "detect java vuln", _ _ "detect php168", _ "detect wordpress", _ "detect directory traversal", _ _ "detect iis", "detect gogs gitea", _ _ _ "detect thinkphp", _ "detect jenkins", _ "detect ecshop", "detect nexus", _ _ "detect drupal", _ "detect ghostscript", _ "detect atlassian", _ "detect weblogic", _ "detect coremail", _ "detect phpcms", _ "detect spring", _ "d t t thid " | three fields are set to continue, no requests are blocked. low risk action: _ _ the action on requests when the lower threshold for blocking is triggered. This field is required. Data type: string. Valid values: deny and continue. The value deny indicates that requests are blocked. The value continue indicates that requests are not blocked. If the high risk action _ _ field is set to deny and the medium risk act _ _ ion and low risk action _ _ fields are set to continue, high- risk requests are blocked. If all the three fields are set to continue, no requests are blocked. high risk enable _ _ log: specifies _ whether to enable logging when the upper threshold is triggered. This field is required. Data type: integer. Valid values: 0 and 1. The value 0 indicates that logs are not recorded. The value 1 indicates that logs are recorded. If the high risk enable _ _ log, _ medium risk en _ _ able log, and _ low risk enable _ _ _ log fields are all set to1, all logs are recorded. If all the three fields are set to 0, no logs are recorded. |
|---|---|---|---|---|
| 49 |   |   | > Docu | ment Version: 2026082 |

|   |   |   | "detect southidc", _ "detect fastjson", _ "detect tbk dvr", _ _ "detect joomla", _ "detect ecology oa", _ _ "detect jackson", _ "detect xstream", _ "detect activemq", _ "detect solr"]}, "low risk action": _ _ _ "continue", "medium risk action": _ _ "continue", "state": "enabled", "medium risk enable log": 1, _ _ _ "high risk action": "deny"}, _ _ "m ssrf": {"low risk enable log": _ _ _ _ 1, "high risk enable log": 1, _ _ _ "low risk action": "continue", _ _ "medium risk action": _ _ "continue", "state": "enabled", "medium risk enable log": 1, _ _ _ "high risk action": "deny"}, _ _ "m xss": {"low risk enable log": _ _ _ _ 1, "high risk enable log": 1, _ _ _ "detect config": _ {"detect complete html": true}, _ _ "low risk action": "continue", _ _ "medium risk action": _ _ "continue", "state": "enabled", "medium risk enable log": 1, _ _ _ "high risk action": "deny"}, _ _ "m asp code injection": {"state": _ _ _ "disabled", "high risk action": _ _ "deny", "high risk enable log": 1, _ _ _ "medium risk action": _ _ "continue", "medium risk enable log": 1, _ _ _ "low risk action": "continue", _ _ "low risk enable log": 1, _ _ _ "detect config": {}}, "m ssti": _ _ {"state": "disabled", "high risk action": "deny", _ _ "high risk enable log": 1, _ _ _ "medium risk action": _ _ "continue", "medium risk enable log": 1, _ _ _ "low risk action": "continue", _ _ "low risk enable log": 1, _ _ _ "detect config": {}}} _ | medium risk en _ _ able log: _ specifies whether to enable logging when the medium threshold is triggered. This field is required. Data type: integer. Valid values: 0 and 1. The value 0 indicates that logs are not recorded. The value 1 indicates that logs are recorded. If the high risk enable _ _ log and _ medium risk en _ _ able log fields _ are set to 1 and the low risk enable _ _ _ log field is set to 0, high-risk and medium-risk logs are recorded. If all the three fields are set to 0, no logs are recorded. low risk enable _ _ _ log: specifies whether to enable logging when the lower threshold is triggered. This field is required. Data type: integer. Valid values: 0 and 1. The value 0 indicates that logs are not recorded. The value 1 indicates that logs are recorded. If the high risk enable _ _ log field is set to _ 1 and the medium risk en _ _ able log and _ low risk enable _ _ _ log fields are set to 0, high-risk logs are recorded. If all the three fields are set to 0, no logs are recorded. state: specifies whether to enable the attack detection module. This field is |
|---|---|---|---|---|
| > Document Versio | n: 2026082 | 8 |   | 15 |

|   |   |   |   | required. Data type: string. Valid values: enabled and disabled. |
|---|---|---|---|---|
| MiscModuleCo nfig | Json | Yes | {"decode config": _ {"decode methods":["url _ decode","JSON","base64","hex"," eval","XML","PHP deserialize","utf7"]}} | The configurations of other modules. The value is a string that consists of JSON arrays. The value is a string that consists of a JSON struct. The JSON struct contains the following fields: decode methods: _ This field is required. Valid values: url decode (URL decoding), JSON (JSON parsing), base64 (Base64 decoding), hex (hexadecimal conversion), eval (slash unescaping), XML (XML parsing), PHP deserialize (parsing of PHP serialized objects), and utf7 (UTF-7 decoding). |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 53e59af3-3209- 452a-853c- ac10ad815929 | The ID of the request. |
| TaskStatus | Struct |   | The returned information. |
| └TaskId | String | c68646a1-58f8- 4b75-828a- a2d3b19b382a | The ID of the task. The ID of the task. |
| └Time | String | 1593593692 | The time when the task status message was generated. This value is a UNIX timestamp representing the number of seconds that have elapsed since the epoch time January 1, 1970, 00:00:00 UTC. |
| └TaskList | String | ["Website-related configuration generation", "Policy-related configuration generation"] | The descriptions of the task. This value is returned only for asynchronous tasks. |

| └StatusMess age | String | The configuration is in effect. | The status message of the task. You can ignore this reserved parameter. |
|---|---|---|---|
| └SuccessCod e | String | 1 | The status code of the task. Valid values: 0: The task fails. 1: The task is successful. 2: The task is not started. |

**Examples**

Sample requests

```json
https://semawaf.[RegionId].aliyuncs.com/?Action=EditPolicyGroup &RegionId=cn-hangzhou &Id=1 &ForbiddenPageConfig={"status_code":405,"action":"response","path":""} &ResponseDetection=true &ResponseDetectionLog=true &ResponseDetectionMaxBody=1024 &RequestDetectionMaxBody=1024 &DetectionTimeout=true &DetectionTimeoutThreshold=1000 &DetectionTimeoutLog=true &DetectionModuleConfig={"m_cmd_injection": {"low_risk_enable_log": 1, "high_risk_enable_log": 1, "low_risk_action": "continue", "medium_risk_action": "contin ue", "state": "disabled", "medium_risk_enable_log": 1, "high_risk_action": "deny"}, "m_ scanner": {"low_risk_enable_log": 1, "high_risk_enable_log": 1, "detect_config": {"robo t_types": ["scanner"]}, "low_risk_action": "continue", "medium_risk_action": "continue" , "state": "disabled", "medium_risk_enable_log": 1, "high_risk_action": "deny"}, "m_fil e_include": {"low_risk_enable_log": 1, "high_risk_enable_log": 1, "low_risk_action": "c ontinue", "medium_risk_action": "continue", "state": "enabled", "medium_risk_enable_log": 1, "high_risk_action": "deny"}, "m_php_code_injection": {"low _risk_enable_log": 1, "high_risk_enable_log": 1, "detect_config": {"detect_upload_file": true}, "low_risk_action": "continue", "medium_risk_action": "con tinue", "state": "enabled", "medium_risk_enable_log": 1, "high_risk_action": "deny"}, " m_response": {"low_risk_enable_log": 1, "high_risk_enable_log": 1, "detect_config": {"e rror_types": ["directory indexing", "SQL execution error", "server exception"]}, "low_r isk_action": "continue", "medium_risk_action": "continue", "state": "disabled", "medium _risk_enable_log": 1, "high_risk_action": "deny"}, "m_java_unserialize": {"low_risk_enable_log": 1, "high_risk_enable_log": 1, "low_risk_action": "continue", "m edium_risk_action": "continue", "state": "enabled", "medium_risk_enable_log": 1, "high_ risk_action": "deny"}, "m_sqli": {"low_risk_enable_log": 1, "high_risk_enable_log": 1, "detect_config": {"detect_non_injection_sql": true}, "low_risk_action": "continue", "me dium_risk_action": "continue", "state": "enabled", "medium_risk_enable_log": 1, "high_r isk_action": "deny"}, "m_csrf": {"low_risk_enable_log": 1, "high_risk_enable_log": 1, " low_risk_action": "continue", "medium_risk_action": "continue", "state": "enabled", "me dium_risk_enable_log": 1, "high_risk_action": "deny"}, "m_java": {"low_risk_enable_log": 1, "high_risk_enable_log": 1, "detect_config": {"detect_upload_file": true}, "low_risk_action": "continue", "medium_risk_action": "con tinue", "state": "enabled", "medium_risk_enable_log": 1, "high_risk_action": "deny"}, " m_file_upload": {"low_risk_enable_log": 1, "high_risk_enable_log": 1, "low_risk_action": "continue", "medium_risk_action": "continue", "state": "enabled", "m edium_risk_enable_log": 1, "high_risk_action": "deny"}, "m_php_unserialize": {"low_risk
```

```json
_enable_log": 1, "high_risk_enable_log": 1, "low_risk_action": "continue", "medium_risk_action": "continue", "state": "enabled", "medium_risk_enable_log": 1, "hig h_risk_action": "deny"}, "m_rule": {"low_risk_enable_log": 1, "high_risk_enable_log": 1 , "detect_config": {"info_leak_types": ["test file", "backup file", "code repository", "server sensitive file"], "check_info_leak_by_rsp": false, "detection_configure": ["det ect_phpinfo", "detect_admin_page", "detect_backdoor", "detect_php_vuln", "detect_nginx", "detect_dedecms", "detect_apache", "detect_xml", "detect_struts2", "det ect_java_vuln", "detect_php168", "detect_wordpress", "detect_directory_traversal", "det ect_iis", "detect_gogs_gitea", "detect_thinkphp", "detect_jenkins", "detect_ecshop", "d etect_nexus", "detect_drupal", "detect_ghostscript", "detect_atlassian", "detect_weblogic", "detect_coremail", "detect_phpcms", "detect_spring", "detect_southidc", "detect_fastjson", "detect_tbk_dvr", "detect_joomla", "detect_ecology_oa", "detect_jackson", "detect_xstream", "detect_activemq", "detect_solr"]}, "low_risk_action": "continue", "medium_risk_action": "continue", "stat e": "enabled", "medium_risk_enable_log": 1, "high_risk_action": "deny"}, "m_ssrf": {"lo w_risk_enable_log": 1, "high_risk_enable_log": 1, "low_risk_action": "continue", "mediu m_risk_action": "continue", "state": "enabled", "medium_risk_enable_log": 1, "high_risk _action": "deny"}, "m_xss": {"low_risk_enable_log": 1, "high_risk_enable_log": 1, "dete ct_config": {"detect_complete_html": true}, "low_risk_action": "continue", "medium_risk_action": "continue", "state": "enabled", "medium_risk_enable_log": 1, "hig h_risk_action": "deny"}, "m_asp_code_injection": {"state": "disabled", "high_risk_action": "deny", "high_risk_enable_log": 1, "medium_risk_action": "continue", "medium_risk_enable_log": 1, "low_risk_action": "continue", "low_risk_enable_log": 1, "detect_config": {}}, "m_ssti": {"state": "disabled", "high_r isk_action": "deny", "high_risk_enable_log": 1, "medium_risk_action": "continue", "medi um_risk_enable_log": 1, "low_risk_action": "continue", "low_risk_enable_log": 1, "detec t_config": {}}} &MiscModuleConfig={"decode_config":{"decode_methods":["url decode","JSON","base64","hex","eval","XML","PHP deserialize","utf7"]}}
```

Sample success responses `XML` format

```xml
<EditPolicyGroupResponse>
    <RequestId>53e59af3-3209-452a-853c-ac10ad815929</RequestId>
    <TaskStatus>
        <TaskId>c68646a1-58f8-4b75-828a-a2d3b19b382a</TaskId>
        <Time>1593593692</Time>
        <TaskList>["Website-related configuration generation", "Policy-related
configuration generation"]</TaskList>
        <StatusMessage>The configuration is in effect.</StatusMessage>
        <SuccessCode>1</SuccessCode>
    </TaskStatus>
</EditPolicyGroupResponse>
```

`JSON` format `{`

```json
  "RequestId":"53e59af3-3209-452a-853c-ac10ad815929",
  "TaskStatus":{
    "TaskId":"c68646a1-58f8-4b75-828a-a2d3b19b382a",
    "TaskList":"[\"Website-related configuration generation\", \"Policy-related
configuration generation\"]",
    "SuccessCode":"1",
    "Time":"1593593692",
    "StatusMessage":"The configuration is in effect."
```

`}` `}`

**Error codes**

For a list of error codes, see Error codes.

#### 4.5.4 DeletePolicyGroup

Deletes a specific protection policy.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeletePolicyGro up | The operation that you want to perform. Set the value to DeletePolicyGroup. |
| RegionId | String | Yes | cn-hangzhou |   |
| IdList | RepeatL ist | Yes | [1, 2] | The ID of the protection policy. You can enter multiple IDs. You can call the DescribePolicyGroup operation to query the IDs of protection policies. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 53e59af3-3209- 452a-853c- ac10ad815929 | The ID of the request. |
| Result | String |   | The returned result of the request. |

**Examples**

Sample requests

```
https://semawaf.[ RegionId].aliyuncs.com/?Action=DeletePolicyGroup &RegionId=cn-hangzhou &IdList.1=1
```

Sample success responses `XML` format

```xml
<DeletePolicyGroupResponse>
    <RequestId>53e59af3-3209-452a-853c-ac10ad815929</RequestId>
    <Result></Result>
</DeletePolicyGroupResponse>
```

`JSON` format `{`

```json
  "RequestId":"53e59af3-3209-452a-853c-ac10ad815929",
  "Result":""
```

`}`

**Error codes**

For a list of error codes, see Error codes.

### 4.6 Protection logs

#### 4.6.1 QueryAsyncTaskStatus

Queries the status of an asynchronous task.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | QueryAsyncTask Status | The operation that you want to perform. Set the value to QueryAsyncTaskStatus. |
| RegionId | String | Yes | cn-hangzhou |   |
| TaskId | String | Yes | 11c745fc-1d66- 40ea-90d7- 7e9a12b987b2 | The ID of the asynchronous task. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 53e59af3-3209- 452a-853c- ac10ad815929 | The ID of the request. |
| TaskStatus | Struct |   |   |
| └TaskId | String | c68646a1-58f8- 4b75-828a- a2d3b19b382a | The ID of the task. |

| └Time | String | 1593593692 | The time when the task status message was generated. This value is a UNIX timestamp representing the number of seconds that have elapsed since the epoch time January 1, 1970, 00:00:00 UTC. |
|---|---|---|---|
| └TaskList | String | ["Website-related configuration generation", "Policy-related configuration generation"] | The descriptions of the task. This value is returned only for asynchronous tasks. |
| └StatusMess age | String | The configuration is in effect. | The status message of the task. |
| └SuccessCod e | String | 1 | The status code of the task. Valid values: 0: The task fails. 1: The task is successful. 2: The task is not started. |

**Examples**

Sample requests

```
https://semawaf.[ RegionId].aliyuncs.com/?Action=QueryAsyncTaskStatus &RegionId=cn-hangzhou &TaskId=11c745fc-1d66-40ea-90d7-7e9a12b987b2
```

Sample success responses `XML` format

```xml
<QueryAsyncTaskStatusResponse>
    <RequestId>53e59af3-3209-452a-853c-ac10ad815929</RequestId>
    <TaskStatus>
        <TaskId>c68646a1-58f8-4b75-828a-a2d3b19b382a</TaskId>
        <Time>1593593692</Time>
        <TaskList>["Website-related configuration generation", "Policy-related
configuration generation"]</TaskList>
        <StatusMessage>The configuration is in effect.</StatusMessage>
        <SuccessCode>1</SuccessCode>
    </TaskStatus>
</QueryAsyncTaskStatusResponse>
```

`JSON` format `{`

```json
  "RequestId":"53e59af3-3209-452a-853c-ac10ad815929",
  "TaskStatus":{
    "TaskId":"c68646a1-58f8-4b75-828a-a2d3b19b382a",
    "TaskList":"[\"Website-related configuration generation\", \"Policy-related
configuration generation\"]",
    "SuccessCode":"1",
    "Time":"1593593692",
    "StatusMessage":"The configuration is in effect."
```

`}` `}`

**Error codes**

For a list of error codes, see Error codes.

#### 4.6.2 QueryAttackDetectionLog

Queries attack detection logs.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | QueryAttackDet ectionLog | The operation that you want to perform. Set the value to QueryAttackDetectionLog. |
| RegionId | String | Yes | cn-hangzhou |   |
| PageSize | Integer | No | 10 | The number of entries to return on each page. Default value: 10. |
| PageNumb er | Integer | No | 1 | The number of the page to return. Default value: 1. |
| Timestam pRangeFil ter | RepeatList | No | ["1594656000- 1596729600"] | The time range to filter logs. You can enter multiple time ranges. |
| RiskLevelF ilter | RepeatList | No | [1, 2] |   |
| AttackTyp eFilter | RepeatList | No | [1, 2, 3] |   |
| ActionFilt er | RepeatList | No | [1, 2] | The action to filter logs. You can enter multiple actions. Valid values: 1, 0, and 2. The value 1 specifies block, the value 0 specifies allow, and the value 2 specifies that all attack detection logs are returned. |

| ProtocolFil ter | RepeatList | No | [0, 1] | The protocol to filter logs. You can enter multiple protocols. Valid values: 0: HTTP 1: HTTPS |
|---|---|---|---|---|
|   |   |   |   | The country or region to filter logs. You can enter multiple countries or regions. Valid values: CN (China), AD (Andorra), AE (United Arab Emirates), AF (Afghanistan), AG (Antigua and Barbuda), AI (Anguilla), AL (Albania), AM (Armenia), AO (Angola), AQ (Antarctica), AR (Argentina), AS (American Samoa), AT (Austria), AU (Australia), AW (Aruba), AX (Åland Islands), AZ (Azerbaijan), BA (Bosnia and Herzegovina), BB (Barbados), BD (Bangladesh), BE (Belgium), BF (Burkina Faso), BG (Bulgaria), BH (Bahrain), BI (Burundi), BJ (Benin), BL (Saint Barthelemy), BM (Bermuda), BN (Brunei), BO (Bolivia), BQ (Caribbean Netherlands), BR (Brazil), BS (Bahamas), BT (Bhutan), BV (Bouvet Island), BW (Botswana), BY (Belarus), BZ (Belize), CA (Canada), CC (Cocos (Keeling) Islands), CD (Democratic Republic of the Congo), CF (Central Africa Republic), CG (Republic of the Congo), CH (Switzerland), CI (Côte d'Ivoire), CK (Cook Islands), CL (Chile), CM (Cameroon), CO (Colombia), CR (Costa Rica), CU (Cuba), CV (Cabo Verde), CW (Curacao), CX (Christmas Island), CY (Cyprus), CZ (Czech Republic), DE (Germany), DJ (Djibouti), DK (Denmark), DM (Dominica), DO (Dominican Republic), DZ (Algeria), EC (Ecuador), EE (Estonia), EG (Egypt), EH (Sahrawi Arab Democratic Republic), ER (Eritrea), ES (Spain), ET (Ethiopia), FI (Finland), FJ (Fiji), FK (Falkland Islands), FM (Federated States of Micronesia), FO (Faroe Islands), FR (France), GA (Gabon), GB (United Kingdom), GD (Grenada), GE (Georgia), GF (French Guiana), GG (Guernsey), GH (Ghana), GI (Gibraltar), GL (Greenland), GM (Gambia), GN (Guinea), GP (Guadeloupe), GQ (Equatorial Guinea), GR (Greece), GS (South Georgia and The South Sandwich Islands), GT (Guatemala), GU (Guam), GW (Guinea-Bissau), GY (Guyana), HK (Hong Kong), HM (Heard Island and McDonald |

| CountryFil ter | RepeatList | No | ["GB, "US"] | Islands), HN (Honduras), HR (Croatia), HT (Haiti), HU (Hungary), ID (Indonesia), IE (Ireland), IL (Israel), IM (Isle of Man), IN (India), IO (British Indian Ocean Territory), IQ (Iraq), IR (Iran), IS (Iceland), IT (Italy), JE (Jersey), JM (Jamaica), JO (Jordan), JP (Japan), KE (Kenya), KG (Kyrgyzstan), KH (Kampuchea), KI (Kiribati), KM (Comoros), KN (Saint Kitts and Nevis), KP (Democratic People's Republic of Korea), KR (Republic of Korea), KW (Kuwait), KY (Cayman Islands), KZ (Kazakhstan), LA (Laos), LB (Lebanon), LC (Saint Lucia), LI (Liechtenstein), LK (Sri Lanka), LR (Liberia), LS (Lesotho), LT (Lithuania), LU (Luxembourg), LV (Latvia), LY (Libya), MA (Morocco), MC (Monaco), MD (Moldova), ME (Montenegro), MF (Saint Martin), MG (Madagascar), MH (Marshall Islands), MK (Macedonia), ML (Mali), MM (Myanmar), MN (Mongolia), MP (Northern Mariana Islands), MQ (Martinique), MR (Mauritania), MS (Montserrat), MT (Malta), MU (Mauritius), MV (Maldives), MW (Malawi), MX (Mexico), MY (Malaysia), MZ (Mozambique), NA (Namibia), NC (New Caledonia), NE (Niger), NF (Norfolk Island), NG (Nigeria), NI (Nicaragua), NL (Netherlands), NO (Norway), NP (Nepal), NR (Nauru), NU (Niue), NZ (New Zealand), OM (Oman), PA (Panama), PE (Peru), PF (French Polynesia), PG (Papua New Guinea), PH (Philippines), PK (Pakistan), PL (Poland), PM (Saint Pierre and Miquelon), PN (Pitcairn Islands), PR (Puerto Rico), PS (Palestine), PT (Portugal), PW (Palau), PY |
|---|---|---|---|---|
|   |   |   |   | (Paraguay), QA (Qatar), RE (Reunion), RO (Romania), RS (Serbia), RU (Russia), RW (Rwanda), SA (Saudi Arabia), SB (Solomon Islands), SC (Seychelles), SD (Sudan), SE (Sweden), SG (Singapore), SH (Saint Helena), SI (Slovenia), SJ (Svalbard and Jan Mayen Islands), SK (Slovakia), SL (Sierra Leone), SM (San Marino), SN (Senegal), SO (Somalia), SR (Suriname), SS (South Sudan), ST (Sao Tome and Principe), SV (El Salvador), SX (Sint Maarten), SY (Syria), SZ (Eswatini), TC (Turks and Caicos Islands), TD (Chad), TF (French Southern and Antarctic Lands), TG (Togo), TH (Thailand), TJ (Tajikistan), TK (Tokelau), TL (East Timor), TM (Turkmenistan), TN (Tunisia), TO (Tonga), TR (Turkey), TT (Trinidad and Tobago), TV |

|   |   |   |   | (Tuvalu), TZ (Tanzania), UA (Ukraine), UG (Uganda), UM (United States Minor Outlying Islands), US (United States), UY (Uruguay), UZ (Uzbekistan), VA (Vatican City), VC (Saint Vincent and the Grenadines), VE (Venezuela), VG (British Virgin Islands), VI (United States Virgin Islands), VN (Vietnam), VU (Vanuatu), WF (Wallis and Futuna Islands), WS (Samoa), YE (Yemen), YT (Mayotte), ZA (South Africa), ZM (Zambia), and ZW (Zimbabwe). |
|---|---|---|---|---|
| EventIdFil ter | RepeatList | No | ["2a0ca6e9- a33d-4164- 8a8d- 3b0e91130069" ] | The event ID to filter logs. You can enter multiple IDs. |
| SourceIpFi lter | RepeatList | No | ["192.168.XX.X X"] | The source IP address to filter logs. You can enter multiple source IP addresses. |
| HostFilter | RepeatList | No | ["www.aliyun.co m"] | The attacked domain name to filter logs. You can enter multiple domain names. |
| UrlPathFilt er | RepeatList | No | ["/"] | The URL path to filter logs. You can enter multiple URL paths. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 53e59af3-3209- 452a-853c- ac10ad815929 | The ID of the request. |
|   |   | {"items": [{"attack type": _ "SQL injection", "risk level": "High _ risk", "action": {"value": 1, "translation": "Block"}, "protocol": "http", "country": "United States", "province": "", "dest port": 80, _ "src ip": _ "1.2.XX.XX", "url path": "/", _ "host": "www.baidu.com", "timestamp": 1594610215, "id": "976ada8c-7561- 48be-8d63- 2d668defcbad", "event id": _ |   |

|   |   | "7f7ae14bada0490 bb257547f05901ec 7", "rule id": _ "m sqli", _ "detector": "a36c01009.cloud. c01.amtest11", "proxy name": _ "a36c01009.cloud. |   |
|---|---|---|---|
| Result | String | c01.amtest11", "src port": 34109, _ "dest ip": _ "43.17.XX.XX", "req header raw": _ _ ""HEAD /?id=1 or b=2 HTTP/1.1\r\nUser- Agent: curl/7.29.0\r\nAcce pt: /\r\nHost: www.baidu.com\r\n X-Forwarded-For: 1.2.XX.XX\r\n\r\n"", "req body": """", _ "resp header raw": _ _ """", "resp body": _ """", "payload": ""1 or b=2"", "session": "", "location": "urlpath", "decode path": "", _ "ali uid": _ "13769889336188 53", "aliyun extra": _ " {"resource port m _ _ apping":{}}", "real dest port": _ _ 80, "vpc id": "", _ "vpc name": _ "yd vpc", "extra": " _ {}", "module": "SQL injection detection module", "reason": "SQL injection detected", "website": "http://www.baidu. com/"}], "total": "101"} |   |

**Examples**

Sample requests

```
https://semawaf.[RegionId].aliyuncs.com/?Action=QueryAttackDetectionLog &RegionId=cn-hangzhou &PageSize=20 &PageNumber=1 &TimestampRangeFilter.1=1594656000-1596729600 &RiskLevelFilter.1=1 &AttackTypeFilter.1=1 &ActionFilter.1=1 &ProtocolFilter.1=0 &CountryFilter.1=["GB, "US"] &EventIdFilter.1=2a0ca6e9-a33d-4164-8a8d-3b0e91130069 &SourceIpFilter.1=192.168.100.200 &HostFilter.1=www.aliyun.com &UrlPathFilter.1=/
```

Sample success responses `XML` format

```json
<QueryAttackDetectionLogResponse>
    <RequestId>53e59af3-3209-452a-853c-ac10ad815929</RequestId>
    <Result>{"items": [{"attack_type": "SQL injection", "risk_level": "High risk", "act
ion": {"value": 1, "translation": "Block"}, "protocol": "http", "country": "United Stat es", "province": "", "dest_port": 80, "src_ip": "1.2.XX.XX", "url_path": "/", "host": " www.baidu.com", "timestamp": 1594610215, "id": "976ada8c-7561-48be-8d63-2d668defcbad", "event_id": "7f7ae14bada0490bb257547f05901ec7", "rule_id": "m_sqli", "detector": "a36c0 1009.cloud.c01.amtest11", "proxy_name": "a36c01009.cloud.c01.amtest11", "src_port": 341 09, "dest_ip": "43.17.XX.XX", "req_header_raw": ""HEAD /?id=1 or b=2 HTTP/1.1\\r\\nUser-Agent: curl/7.29.0\\r\\nAccept: */*\\r\\nHost: www.baidu.com\\r\\nX- Forwarded-For: 1.2.XX.XX\\r\\n\\r\\n"", "req_body": """", "resp_header_raw": """", "res p_body": """", "payload": ""1 or b=2"", "session": "", "location": "urlpath", "decode_p ath": "", "ali_uid": "1376988933618853", "aliyun_extra": "{"resource_port_mapping":{}}" , "real_dest_port": 80, "vpc_id": "", "vpc_name": "yd_vpc", "extra": "{}", "module": "S QL injection detection module", "reason": "SQL injection detected", "website": "http:// www.baidu.com/"}], "total": "101"}</Result> </QueryAttackDetectionLogResponse>
```

`JSON` format `{`

```json
  "RequestId":"53e59af3-3209-452a-853c-ac10ad815929",
  "Result":"{\"items\": [{\"attack_type\": \"SQL injection\", \"risk_level\": \"High ri
sk \", \"action\": {\"value\": 1, \"translation\": \"Block\"}, \"protocol\": \"http\", \"country\": \"United States \", \"province\": \"\", \"dest_port\": 80, \"src_ip\": \"1 .2.XX.XX\", \"url_path\": \"/\", \"host\": \"www.baidu.com\", \"timestamp\": 1594610215, \"id\": \"976ada8c-7561-48be-8d63-2d668defcbad\", \"event_id\": \"7f7ae14bada0490bb257547f05901ec7\", \"rule_id\": \"m_sqli\", \"detector\": \"a36c01009.cloud.c01.amtest11\", \"proxy_name\": \"a36c01009.cloud.c01.amtest11\", \"s rc_port\": 34109, \"dest_ip\": \"43.17.XX.XX\", \"req_header_raw\": \"\"HEAD /?id=1 or b=2 HTTP/1.1\\\\r\\\\nUser-Agent: curl/7.29.0\\\\r\\\\nAccept: */*\\\\r\\\\nHost: www.b aidu.com\\\\r\\\\nX-Forwarded-For: 1.2.XX.XX\\\\r\\\\n\\\\r\\\\n\"\", \"req_body\": \"\ "\"\", \"resp_header_raw\": \"\"\"\", \"resp_body\": \"\"\"\", \"payload\": \"\"1 or b= 2\"\", \"session\": \"\", \"location\": \"urlpath\", \"decode_path\": \"\", \"ali_uid\": \"1376988933618853\", \"aliyun_extra\": \"{\"resource_port_mapping\":{}}\" , \"real_dest_port\": 80, \"vpc_id\": \"\", \"vpc_name\": \"yd_vpc\", \"extra\": \"{}\" , \"module\": \"SQL injection detection module\", \"reason\": \"SQL injection detected\ ", \"website\": \"http://www.baidu.com/\"}], \"total\": \"101\"}"
```

`}`

**Error codes**

For a list of error codes, see Error codes.

#### 4.6.3 QueryAttackDetectionDetailLog

Queries the details of a specific attack detection log.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | QueryAttackDet ectionDetailLog | The operation that you want to perform. Set the value to QueryAttackDetectionDetailLog. |
| RegionId | String | Yes | cn-hangzhou |   |
| LogId | String | Yes | 1e23f8d1-a9d2- 4dd9-b7e2- 424b9832183f | The ID of the attack detection log. |

**Response parameters**

| Paramete r | Type | Example | Descriptio n |
|---|---|---|---|
| RequestId | String | 53e59af3-3209-452a-853c-ac10ad815929 | The ID of the request. |

| Result | String | {"items": [{"attack type": "SQL injection", "risk level": _ _ "High risk", "action": {"value": 1, "translation": "Block"}, "protocol": "http", "country": "United States", "province": "", "dest port": 80, "src ip": "1.2.XX.XX", "url path": "/", _ _ _ "host": "www.baidu.com", "timestamp": 1594610215, "id": "976ada8c-7561-48be-8d63-2d668defcbad", "event id": "7f7ae14bada0490bb257547f05901ec7", _ "rule id": "m sqli", "detector": _ _ "a36c01009.cloud.c01.amtest11", "proxy name": _ "a36c01009.cloud.c01.amtest11", "src port": 34109, _ "dest ip": "43.17.XX.XX", "req header raw": ""HEAD /? _ _ _ id=1 or b=2 HTTP/1.1\r\nUser-Agent: curl/7.29.0\r\nAccept: /\r\nHost: www.baidu.com\r\nX- Forwarded-For: 1.2.XX.XX\r\n\r\n"", "req body": """", _ "resp header raw": """", "resp body": """", "payload": ""1 _ _ _ or b=2"", "session": "", "location": "urlpath", "decode path": "", "ali uid": "1376988933618853", _ _ "aliyun extra": "{"resource port mapping":{}}", _ _ _ "real dest port": 80, "vpc id": "", "vpc name": "yd vpc", _ _ _ _ _ "extra": "{}", "module": "SQL injection detection module", "reason": "SQL injection detected", "website": "http://www.baidu.com/"}]} | The returned result of the request. |
|---|---|---|---|

**Examples**

Sample requests

```
https://semawaf.[ RegionId].aliyuncs.com/?Action=QueryAttackDetectionDetailLog &RegionId=cn-hangzhou &LogId=1e23f8d1-a9d2-4dd9-b7e2-424b9832183f
```

Sample success responses `XML` format

```json
<QueryAttackDetectionDetailLogResponse>
    <RequestId>53e59af3-3209-452a-853c-ac10ad815929</RequestId>
    <Result>{"items": [{"attack_type": "SQL injection", "risk_level": "High risk", "act
ion": {"value": 1, "translation": "Block"}, "protocol": "http", "country": "United Stat es", "province": "", "dest_port": 80, "src_ip": "1.2.XX.XX", "url_path": "/", "host": " www.baidu.com", "timestamp": 1594610215, "id": "976ada8c-7561-48be-8d63-2d668defcbad", "event_id": "7f7ae14bada0490bb257547f05901ec7", "rule_id": "m_sqli", "detector": "a36c0 1009.cloud.c01.amtest11", "proxy_name": "a36c01009.cloud.c01.amtest11", "src_port": 341 09, "dest_ip": "43.17.XX.XX", "req_header_raw": ""HEAD /? id=1 or b=2 HTTP/1.1\\r\\nUser-Agent: curl/7.29.0\\r\\nAccept: */*\\r\\nHost: www.baidu.com\\r\\nX- Forwarded-For: 1.2.XX.XX\\r\\n\\r\\n"", "req_body": """", "resp_header_raw": """", "res p_body": """", "payload": ""1 or b=2"", "session": "", "location": "urlpath", "decode_p ath": "", "ali_uid": "1376988933618853", "aliyun_extra": "{"resource_port_mapping":{}}" , "real_dest_port": 80, "vpc_id": "", "vpc_name": "yd_vpc", "extra": "{}", "module": "S QL injection detection module", "reason": "SQL injection detected", "website": "http:// www.baidu.com/"}]}</Result> </QueryAttackDetectionDetailLogResponse>
```

`JSON` format `{`

```json
  "RequestId":"53e59af3-3209-452a-853c-ac10ad815929",
  "Result":"{\"items\": [{\"attack_type\": \"SQL injection\", \"risk_level\": \"High ri
sk\", \"action\": {\"value\": 1, \"translation\": \"Block\"}, \"protocol\": \"http\", \ "country\": \"United States\", \"province\": \"\", \"dest_port\": 80, \"src_ip\": \"1.2 .XX.XX\", \"url_path\": \"/\", \"host\": \"www.baidu.com\", \"timestamp\": 1594610215, \"id\": \"976ada8c-7561-48be-8d63-2d668defcbad\", \"event_id\": \"7f7ae14bada0490bb257547f05901ec7\", \"rule_id\": \"m_sqli\", \"detector\": \"a36c01009.cloud.c01.amtest11\", \"proxy_name\": \"a36c01009.cloud.c01.amtest11\", \"s rc_port\": 34109, \"dest_ip\": \"43.17.XX.XX\", \"req_header_raw\": \"\"HEAD /? id=1 or b=2 HTTP/1.1\\\\r\\\\nUser-Agent: curl/7.29.0\\\\r\\\\nAccept: */*\\\\r\\\\nHost: www.b aidu.com\\\\r\\\\nX-Forwarded-For: 1.2.XX.XX\\\\r\\\\n\\\\r\\\\n\"\", \"req_body\": \"\ "\"\", \"resp_header_raw\": \"\"\"\", \"resp_body\": \"\"\"\", \"payload\": \"\"1 or b= 2\"\", \"session\": \"\", \"location\": \"urlpath\", \"decode_path\": \"\", \"ali_uid\": \"1376988933618853\", \"aliyun_extra\": \"{\"resource_port_mapping\":{}}\" , \"real_dest_port\": 80, \"vpc_id\": \"\", \"vpc_name\": \"yd_vpc\", \"extra\": \"{}\" , \"module\": \"SQL injection detection module\", \"reason\": \"SQL injection detected\ ", \"website\": \"http://www.baidu.com/\"}]}"
```

`}`

**Error codes**

For a list of error codes, see Error codes.

#### 4.6.4 QueryAuditLog

Queries system operations logs.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | QueryAuditLog | The operation that you want to perform. Set the value to QueryAuditLog. |
| RegionId | String | Yes | cn-hangzhou |   |
| PageNumber | Integer | No | 1 | The number of the page to return. Default value: 1. |
| PageSize | Integer | No | 20 | The number of entries to return on each page. Default value: 10. |

**Response parameters**

| Paramete r | Type | Example | Descriptio n |
|---|---|---|---|
| RequestId | String | 53e59af3-3209-452a-853c-ac10ad815929 | The ID of the request. |

| Result | String | {"items": [{"content": "An access control whitelist is created. Data: {'comment': '', 'target type': 'Session', _ 'target list': ['1313'], 'target group list': []}", _ _ _ "username": "1376988933618853", "id": "756897bd- a178-445b-a193-5b46c14fa44c", "ip": "10.17.XX.XX", "user agent": "Apache-HttpClient/4.5.2 (Java/1.8.0 152)", _ _ "log type": "Access control and management", _ "create time": "1594653501"}], "total": "36"} _ | The returned result of the request. |
|---|---|---|---|

**Examples**

Sample requests

```
https://semawaf.[ RegionId].aliyuncs.com/?Action=QueryAuditLog &RegionId=cn-hangzhou &PageSize=20 &PageNumber=1
```

Sample success responses `XML` format

```xml
<QueryAuditLogResponse>
    <RequestId>53e59af3-3209-452a-853c-ac10ad815929</RequestId>
    <Result>{"items": [{"content": "An access control whitelist is created. Data: {'com
ment': '', 'target_type': 'Session', 'target_list': ['1313'], 'target_group_list': []}" , "username": "1376988933618853", "id": "756897bd-a178-445b-a193-5b46c14fa44c", "ip": " 10.17.XX.XX", "user_agent": "Apache-HttpClient/4.5.2 (Java/1.8.0_152)", "log_type": "Ac cess control and management", "create_time": "1594653501"}], "total": "36"}</Result> </QueryAuditLogResponse>
```

`JSON` format `{`

```json
  "RequestId":"53e59af3-3209-452a-853c-ac10ad815929",
  "Result":"{\"items\": [{\"content\": \"An access control whitelist is created. Data:
{'comment': '', 'target_type': 'Session', 'target_list': ['1313'], 'target_group_list': []}\", \"username\": \"1376988933618853\", \"id\": \"756897bd-a178-445b-a193-5b46c14fa4 4c\", \"ip\": \"10.17.XX.XX\", \"user_agent\": \"Apache-HttpClient/4.5.2 (Java/1.8.0_152)\", \"log_type\": \"Access control and management\", \"create_time\": \ "1594653501\"}], \"total\": \"36\"}"
```

`}`

**Error codes**

For a list of error codes, see Error codes.

#### 4.6.5 QueryCCRuleExecutionLog

Queries the logs on the execution of HTTP flood protection rules.

**Request parameters**

| > Document Versio | n: 20260828 |   |   | 16 |
|---|---|---|---|---|

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | QueryCCRuleEx ecutionLog | The operation that you want to perform. Set the value to QueryCCRuleExecutionLog. |
| RegionId | String | Yes | cn-hangzhou |   |
| PageNumber | Integer | No | 1 | The number of the page to return. Default value: 1. |
| PageSize | Integer | No | 20 | The number of entries to return on each page. Default value: 10. |
| TimestampRan geFilter | RepeatL ist | No | ["1594656000- 1596729600"] | The time range to filter logs. You can enter multiple ranges. Unit: seconds. |
| CCRuleTemplate IdList | RepeatL ist | No | [1, 2] | The rule ID to filter logs. You can enter multiple IDs. You can call the DescribeCCRuleTemplate operation to query the IDs of HTTP flood protection rules. |

**Response parameters**

| Paramete r | Type | Example | Descriptio n |
|---|---|---|---|
| RequestId | String | 53e59af3-3209-452a-853c-ac10ad815929 | The ID of the request. |
| Result | String | {"items": [{"acl rule id": "29", "acl rule template id": _ _ _ _ _ "38", "acl rule template version": "39", "timestamp": _ _ _ "1594610400", "count": "100", "acl rule target": _ _ "1.2.XX.XX", "acl rule template": {"name": "123", _ _ "match method": {"target type": "CIDR", "period": 5, _ _ "limit": 1, "scope": "URL", "policy": "www.baidu.com", "scheme": "http"}, "action": {"action": "forbid"}, "template type": "auto", "dry run": false, "status": _ _ "ok"}}], "total": 11} |   |

**Examples**

Sample requests

```
https://semawaf.[RegionId].aliyuncs.com/?Action=QueryCCRuleExecutionLog &RegionId=cn-hangzhou &PageSize=20 &PageNumber=1 &TimestampRangeFilter.1=1594656000-1596729600 &CCRuleTemplateIdList.1=1
```

Sample success responses `XML` format

```json
<QueryCCRuleExecutionLogResponse>
    <RequestId>53e59af3-3209-452a-853c-ac10ad815929</RequestId>
    <Result>{"items": [{"acl_rule_id": "29", "acl_rule_template_id": "38",
"acl_rule_template_version": "39", "timestamp": "1594610400", "count": "100", "acl_rule _target": "1.2.XX.XX", "acl_rule_template": {"name": "123", "match_method": {"target_ty pe": "CIDR", "period": 5, "limit": 1, "scope": "URL", "policy": "www.baidu.com", "schem e": "http"}, "action": {"action": "forbid"}, "template_type": "auto", "dry_run": false, "status": "ok"}}], "total": 11}</Result> </QueryCCRuleExecutionLogResponse>
```

`JSON` format `{`

```json
  "RequestId":"53e59af3-3209-452a-853c-ac10ad815929",
  "Result":"{\"items\": [{\"acl_rule_id\": \"29\", \"acl_rule_template_id\": \"38\", \"
acl_rule_template_version\": \"39\", \"timestamp\": \"1594610400\", \"count\": \"100\", \"acl_rule_target\": \"1.2.XX.XX\", \"acl_rule_template\": {\"name\": \"123\", \"match_ method\": {\"target_type\": \"CIDR\", \"period\": 5, \"limit\": 1, \"scope\": \"URL\", \"policy\": \"www.baidu.com\", \"scheme\": \"http\"}, \"action\": {\"action\": \"forbid \"}, \"template_type\": \"auto\", \"dry_run\": false, \"status\": \"ok\"}}], \"total\": 11}"
```

`}`

**Error codes**

For a list of error codes, see Error codes.

#### 4.6.6 QueryFullAccessLog

Queries full access logs.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | QueryFullAcces sLog | The operation that you want to perform. Set the value to QueryFullAccessLog. |
| RegionId | String | Yes | cn-hangzhou |   |
| PageSize | Integer | No | 10 | The number of entries to return on each page. Default value: 10. |
| PageNumb er | Integer | No | 1 | The number of the page to return. Default value: 1. |
| Timestam pRangeFil ter | RepeatList | No | ["1594656000- 1596729600"] | The time range to filter logs. You can enter multiple time ranges. |
| SourceIpFi lter | RepeatList | No | ["192.168.XX.X X"] | The source IP address to filter logs. You can enter multiple source IP addresses. |

| Destinatio nIp | RepeatList | No | ["10.10.XX.XX"] | The destination IP address to filter logs. You can enter multiple destination IP addresses. |
|---|---|---|---|---|
| MethodFil ter | RepeatList | No | ["POST"] | The request method to filter logs. You can enter multiple methods. |
| SourcePor tFilter | RepeatList | No | [11013, 55555] | The source port to filter logs. You can enter multiple source ports. |
| ResponseC ode | RepeatList | No | [302, 404] | The response code to filter logs. You can enter multiple codes. |
| Destinatio nPortFilte r | RepeatList | No | [80, 443] | The destination port to filter logs. You can enter multiple destination ports. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 53e59af3-3209- 452a-853c- ac10ad815929 | The ID of the request. |

| Result | String | {"items": [{"id": "a03511f0-b325- 4674-8f50- 80feb5de2023", "ali uid": _ "13769889336188 53", "timestamp": 1594698077, "dest ip": _ "43.17.XX.XX", "dest port": 10003, _ "real dest port": _ _ 80, "src ip": _ "10.17.XX.XX", "src port": 37078, _ "req header raw": _ _ ""GET / HTTP/1.1\r\nUser- Agent: curl/7.29.0\r\nAcce pt: /\r\nhost: www.wafcloud.com \r\n\r\n"", "method": "GET", "req body": """", _ "resp header raw": _ _ ""HTTP/1.1 200 OK\r\nServer: nginx/1.10.2\r\nDat e: Tue, 14 Jul 2020 03:40:35 GMT\r\nContent- Type: text/html\r\nConte nt-Length: 3700\r\nLast- Modified: Tue, 28 Mar 2017 07:33:40 GMT\r\nConnection : keep- alive\r\nETag: "58da11d4- e74"\r\nAccept- Ranges: bytes\r\n\r\n"", "resp code": 200, _ "payload": """", "url": "/", "content type": _ "text/html", "event id": "", _ "session": "null", "proxy name": _ "a36c01009.cloud. c01.amtest11", "website": "www.wafcloud.co m", "host": "www.wafcloud.co m", "vpc": "vpc- 9qb3r79gohas1khs r2x7e", "vpc name": "-"}], _ "total": "1"} | The returned result of the request. |
|---|---|---|---|

**Examples**

Sample requests

```
https://semawaf.[ RegionId].aliyuncs.com/?Action=QueryFullAccessLog &RegionId=cn-hangzhou &PageSize=20 &PageNumber=1 &TimestampRangeFilter.1=1594656000-1596729600 &SourceIpFilter.1=192.168.XX.XX &DestinationIp.1=10.10.XX.XX &MethodFilter.1=POST &ResponseCode.1=302 &SourcePortFilter.1=11013 &DestinationPortFilter.1=80 &HostFilter.1=192.168.XX.XX &PathFilter.1=/index.html
```

Sample success responses `XML` format

```json
<QueryFullAccessLogResponse>
    <RequestId>53e59af3-3209-452a-853c-ac10ad815929</RequestId>
    <Result>{"items": [{"id": "a03511f0-b325-4674-8f50-80feb5de2023", "ali_uid": "13769
88933618853", "timestamp": 1594698077, "dest_ip": "43.17.XX.XX", "dest_port": 10003, "r eal_dest_port": 80, "src_ip": "10.17.XX.XX", "src_port": 37078, "req_header_raw": ""GET / HTTP/1.1\r\nUser-Agent: curl/7.29.0\r\nAccept: */*\r\nhost: www.wafcloud.com\r\n\r\n"", "method": "GET", "req_body": """", "resp_header_raw": ""HTT P/1.1 200 OK\r\nServer: nginx/1.10.2\r\nDate: Tue, 14 Jul 2020 03:40:35 GMT\r\nContent- Type: text/html\r\nContent-Length: 3700\r\nLast-Modified: Tue, 28 Mar 2017 07:33:40 GMT \r\nConnection: keep-alive\r\nETag: \"58da11d4-e74\"\r\nAccept-Ranges: bytes\r\n\r\n"", "resp_code": 200, "payload": """", "url": "/", "content_type": "text/html", "event_id": "", "session": "null", "proxy_name": "a36c01009.cloud.c01.amtest11", "website": "www.wa fcloud.com", "host": "www.wafcloud.com", "vpc": "vpc-9qb3r79gohas1khsr2x7e", "vpc_name" : "-"}], "total": "1"}</Result> </QueryFullAccessLogResponse>
```

`JSON` format `{`

```json
  "RequestId":"53e59af3-3209-452a-853c-ac10ad815929",
  "Result":"{\"items\": [{\"id\": \"a03511f0-b325-4674-8f50-80feb5de2023\",
\"ali_uid\": \"1376988933618853\", \"timestamp\": 1594698077, \"dest_ip\": \"43.17.XX.X X\", \"dest_port\": 10003, \"real_dest_port\": 80, \"src_ip\": \"10.17.XX.XX\", \"src_p ort\": 37078, \"req_header_raw\": \"\"GET / HTTP/1.1\\r\\nUser-Agent: curl/7.29.0\\r\\nAccept: */*\\r\\nhost: www.wafcloud.com\\r\\n\\r\\n\"\", \"method\": \ "GET\", \"req_body\": \"\"\"\", \"resp_header_raw\": \"\"HTTP/1.1 200 OK\\r\\nServer: n ginx/1.10.2\\r\\nDate: Tue, 14 Jul 2020 03:40:35 GMT\\r\\nContent-Type: text/html\\r\\nContent-Length: 3700\\r\\nLast-Modified: Tue, 28 Mar 2017 07:33:40 GMT\\ r\\nConnection: keep-alive\\r\\nETag: \\\"58da11d4-e74\\\"\\r\\nAccept-Ranges: bytes\\r \\n\\r\\n\"\", \"resp_code\": 200, \"payload\": \"\"\"\", \"url\": \"/\", \"content_type\": \"text/html\", \"event_id\": \"\", \"session\": \"null\", \"proxy_name\": \"a36c01009.cloud.c01.amtest11\", \"website\": \"www.wafcloud.com\", \" host\": \"www.wafcloud.com\", \"vpc\": \"vpc-9qb3r79gohas1khsr2x7e\", \"vpc_name\": \"- \"}], \"total\": \"1\"}"
```

`}`

**Error codes**

For a list of error codes, see Error codes.

#### 4.6.7 QueryFullAccessDetailLog

Queries the details of a specific full access log.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | QueryFullAccess DetailLog | The operation that you want to perform. Set the value to QueryFullAccessDetailLog. |
| RegionId | String | Yes | cn-hangzhou |   |
| LogId | String | Yes | 1e23f8d1-a9d2- 4dd9-b7e2- 424b9832183f | The ID of the log. |

**Response parameters**

| Paramete r | Type | Example | Descriptio n |
|---|---|---|---|
| RequestId | String | 53e59af3-3209-452a-853c-ac10ad815929 | The ID of the request. |

| Result | String | {"items": [{"id": "a03511f0-b325-4674-8f50- 80feb5de2023", "ali uid": "1376988933618853", _ "timestamp": 1594698077, "dest ip": "43.17.XX.XX", _ "dest port": 10003, "real dest port": 80, "src ip": _ _ _ _ "10.17.XX.XX", "src port": 37078, "req header raw": _ _ _ ""GET / HTTP/1.1\r\nUser-Agent: curl/7.29.0\r\nAccept: /\r\nhost: www.wafcloud.com\r\n\r\n"", "method": "GET", "req body": """", "resp header raw": ""HTTP/1.1 200 _ _ _ OK\r\nServer: nginx/1.10.2\r\nDate: Tue, 14 Jul 2020 03:40:35 GMT\r\nContent-Type: text/html\r\nContent- Length: 3700\r\nLast-Modified: Tue, 28 Mar 2017 07:33:40 GMT\r\nConnection: keep-alive\r\nETag: "58da11d4-e74"\r\nAccept-Ranges: bytes\r\n\r\n"", "resp code": 200, "payload": """", "url": "/", _ "content type": "text/html", "event id": "", "session": _ _ "null", "proxy name": "a36c01009.cloud.c01.amtest11", _ "website": "www.wafcloud.com", "host": "www.wafcloud.com", "vpc": "vpc- 9qb3r79gohas1khsr2x7e", "vpc name": "-"}]} _ |   |
|---|---|---|---|

**Examples**

Sample requests

```
https://semawaf.[RegionId].aliyuncs.com/?Action=QueryFullAccessDetailLog &RegionId=cn-hangzhou &LogId=1e23f8d1-a9d2-4dd9-b7e2-424b9832183f
```

Sample success responses `XML` format

```json
<QueryFullAccessDetailLogResponse>
    <RequestId>53e59af3-3209-452a-853c-ac10ad815929</RequestId>
    <Result>{"items": [{"id": "a03511f0-b325-4674-8f50-80feb5de2023", "ali_uid": "13769
88933618853", "timestamp": 1594698077, "dest_ip": "43.17.XX.XX", "dest_port": 10003, "r eal_dest_port": 80, "src_ip": "10.17.XX.XX", "src_port": 37078, "req_header_raw": ""GET / HTTP/1.1\r\nUser-Agent: curl/7.29.0\r\nAccept: */*\r\nhost: www.wafcloud.com\r\n\r\n"", "method": "GET", "req_body": """", "resp_header_raw": ""HTT P/1.1 200 OK\r\nServer: nginx/1.10.2\r\nDate: Tue, 14 Jul 2020 03:40:35 GMT\r\nContent- Type: text/html\r\nContent-Length: 3700\r\nLast-Modified: Tue, 28 Mar 2017 07:33:40 GMT \r\nConnection: keep-alive\r\nETag: \"58da11d4-e74\"\r\nAccept-Ranges: bytes\r\n\r\n"", "resp_code": 200, "payload": """", "url": "/", "content_type": "text/html", "event_id": "", "session": "null", "proxy_name": "a36c01009.cloud.c01.amtest11", "website": "www.wa fcloud.com", "host": "www.wafcloud.com", "vpc": "vpc-9qb3r79gohas1khsr2x7e", "vpc_name" : "-"}]}</Result> </QueryFullAccessDetailLogResponse>
```

`JSON` format `{`

```json
  "RequestId":"53e59af3-3209-452a-853c-ac10ad815929",
  "Result":"{\"items\": [{\"id\": \"a03511f0-b325-4674-8f50-80feb5de2023\",
\"ali_uid\": \"1376988933618853\", \"timestamp\": 1594698077, \"dest_ip\": \"43.17.XX.X X\", \"dest_port\": 10003, \"real_dest_port\": 80, \"src_ip\": \"10.17.XX.XX\", \"src_p ort\": 37078, \"req_header_raw\": \"\"GET / HTTP/1.1\\r\\nUser-Agent: curl/7.29.0\\r\\nAccept: */*\\r\\nhost: www.wafcloud.com\\r\\n\\r\\n\"\", \"method\": \ "GET\", \"req_body\": \"\"\"\", \"resp_header_raw\": \"\"HTTP/1.1 200 OK\\r\\nServer: n ginx/1.10.2\\r\\nDate: Tue, 14 Jul 2020 03:40:35 GMT\\r\\nContent-Type: text/html\\r\\nContent-Length: 3700\\r\\nLast-Modified: Tue, 28 Mar 2017 07:33:40 GMT\\ r\\nConnection: keep-alive\\r\\nETag: \\\"58da11d4-e74\\\"\\r\\nAccept-Ranges: bytes\\r \\n\\r\\n\"\", \"resp_code\": 200, \"payload\": \"\"\"\", \"url\": \"/\", \"content_type\": \"text/html\", \"event_id\": \"\", \"session\": \"null\", \"proxy_name\": \"a36c01009.cloud.c01.amtest11\", \"website\": \"www.wafcloud.com\", \" host\": \"www.wafcloud.com\", \"vpc\": \"vpc-9qb3r79gohas1khsr2x7e\", \"vpc_name\": \"- \"}]}"
```

`}`

**Error codes**

For a list of error codes, see Error codes.

#### 4.6.8 QueryPerformanceStatistics

Queries the historical performance data of a specific node.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | QueryPerforman ceStatistics | The operation that you want to perform. Set the value to QueryPerformanceStatistics. |
| RegionId | String | Yes | cn-hangzhou |   |
| NodeName | String | Yes | a36c01009.clou d.c01.amtest11 | The name of the node. |
| TimestampRan geFilter | RepeatL ist |   | ["1594656000- 1596729600"] | The time range to filter historical performance data. You can enter multiple time ranges. |

**Response parameters**

| Paramete r | Type | Example | Descriptio n |
|---|---|---|---|
| RequestId | String | 53e59af3-3209-452a-853c-ac10ad815929 | The ID of the request. |

| Result | String | [{"id": 2005654, "name": "c43b02111.cloud.b03.amtest21", "timestamp": "1594697170", "cpu usage": 1.5670533277966774, _ "memory usage": 8.946810185810278, "disk usage": _ _ 5.475940507296313, "network read": _ 26010.129032258064, "network write": _ 25739.064516129034, "qps": 0.0, "cps": 10.6, "extra": {}}, {"id": 2005652, "name": "c43b02111.cloud.b03.amtest21", "timestamp": "1594697165", "cpu usage": 1.3590924225742251, _ "memory usage": 8.943323969418117, "disk usage": _ _ 5.475936863788965, "network read": _ 23102.645161290322, "network write": _ 22265.774193548386, "qps": 0.0, "cps": 9.2, "extra": {}}] | The returned result of the request. |
|---|---|---|---|

**Examples**

Sample requests

```
https://semawaf.[ RegionId].aliyuncs.com/?Action=QueryPerformanceStatistics &RegionId=cn-hangzhou &NodeName=a36c01009.cloud.c01.amtest11 &TimestampRangeFilter.1=1594656000-1596729600
```

Sample success responses `XML` format

```json
<QueryPerformanceStatisticsResponse>
    <RequestId>53e59af3-3209-452a-853c-ac10ad815929</RequestId>
    <Result>[{"id": 2005654, "name": "c43b02111.cloud.b03.amtest21", "timestamp": "1594
697170", "cpu_usage": 1.5670533277966774, "memory_usage": 8.946810185810278, "disk_usage": 5.475940507296313, "network_read": 26010.129032258064, "network_write": 2 5739.064516129034, "qps": 0.0, "cps": 10.6, "extra": {}}, {"id": 2005652, "name": "c43b 02111.cloud.b03.amtest21", "timestamp": "1594697165", "cpu_usage": 1.3590924225742251, "memory_usage": 8.943323969418117, "disk_usage": 5.475936863788965, "network_read": 231 02.645161290322, "network_write": 22265.774193548386, "qps": 0.0, "cps": 9.2, "extra": {}}]</Result> </QueryPerformanceStatisticsResponse>
```

`JSON` format `{`

```json
  "RequestId":"53e59af3-3209-452a-853c-ac10ad815929",
  "Result":"[{\"id\": 2005654, \"name\": \"c43b02111.cloud.b03.amtest21\",
\"timestamp\": \"1594697170\", \"cpu_usage\": 1.5670533277966774, \"memory_usage\": 8.9 46810185810278, \"disk_usage\": 5.475940507296313, \"network_read\": 26010.129032258064, \"network_write\": 25739.064516129034, \"qps\": 0.0, \"cps\": 10.6, \"extra\": {}}, {\"id\": 2005652, \"name\": \"c43b02111.cloud.b03.amtest21\", \"timesta mp\": \"1594697165\", \"cpu_usage\": 1.3590924225742251, \"memory_usage\": 8.943323969418117, \"disk_usage\": 5.475936863788965, \"network_read\": 23102.645161290322, \"network_write\": 22265.774193548386, \"qps\": 0.0, \"cps\": 9.2, \"extra\": {}}]"
```

`}`

**Error codes**

For a list of error codes, see Error codes.

### 4.7 SSL certificate management

#### 4.7.1 DescribeSSLCert

Queries the information about SSL certificates.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeSSLCe rt | The operation that you want to perform. Set the value to DescribeSSLCert. |
| RegionId | String | Yes | cn-hangzhou |   |
| Id | Integer | No | 1 | The ID of the SSL certificate. |
| PageSize | Integer | No | 10 | The number of entries to return on each page. Default value: 10. |
| PageNumber | Integer | No | 1 | The number of the page to return. Default value: 1. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 53e59af3-3209- 452a-853c- ac10ad815929 | The ID of the request. |
| Result | String | [{"id": 1, "websites": [], "create time": _ "1589445455", "name": "test cert 1", _ _ "signature": "329b059f298419c 002fc69f1ee9a3df1 ", "info": {"serial": "0xb79b1ba15f4fb 061", "issuer": "Aliyun", "not valid before": _ _ 1567468800, "not valid after": _ _ 1882828800, "domains": []}}] | The returned result of the request. |

**Examples**

Sample requests

```
https://semawaf.[ RegionId].aliyuncs.com/?Action=DescribeSSLCert &RegionId=cn-hangzhou &Id=1 &PageSize=10 &PageNumber=1
```

Sample success responses `XML` format

```json
<DescribeSSLCertResponse>
    <RequestId>53e59af3-3209-452a-853c-ac10ad815929</RequestId>
    <Result>[{"id": 1, "websites": [], "create_time": "1589445455", "name":
"test_cert_1", "signature": "329b059f298419c002fc69f1ee9a3df1", "info": {"serial": "0xb 79b1ba15f4fb061", "issuer": "Aliyun", "not_valid_before": 1567468800, "not_valid_after": 1882828800, "domains": []}}]</Result> </DescribeSSLCertResponse>
```

`JSON` format `{`

```json
  "RequestId":"53e59af3-3209-452a-853c-ac10ad815929",
  "Result":"[{\"id\": 1, \"websites\": [], \"create_time\": \"1589445455\", \"name\": \
"test_cert_1\", \"signature\": \"329b059f298419c002fc69f1ee9a3df1\", \"info\": {\"seria l\": \"0xb79b1ba15f4fb061\", \"issuer\": \"Aliyun\", \"not_valid_before\": 1567468800, \"not_valid_after\": 1882828800, \"domains\": []}}]"
```

`}`

**Error codes**

For a list of error codes, see Error codes.

#### 4.7.2 UploadSSLCert

Uploads an SSL certificate.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | UploadSSLCert | The operation that you want to perform. Set the value to UploadSSLCert. |
| RegionId | String | Yes | cn-hangzhou |   |
| CertName | String | No | taobao cert _ | The name of the SSL certificate. |

| CertFile | Json | Yes | {"name":"","co ntent":"bEtrYm drVFVSb3plY1d Ma01BVmZrek hGdGxw****"} | The Base64-encoded certificate authority (CA) certificate file. This parameter is a string consisting of JSON structs. A JSON struct includes the following fields: name: Leave this field unspecified. content: the Base64-encoded CA certificate file. |
|---|---|---|---|---|
| KeyFile | Json | No | {"name":"","co ntent":"eElzcE ZEaElzaXlqVFB GU1B0ZG9qd m1iSEV1****"} | The Base64-encoded private key file. This parameter is a string consisting of JSON structs. A JSON struct includes the following fields: name: Leave this field unspecified. content: the Base64-encoded private key file. |
| CertPassword | String | No | jgXzOoigHGWC LxE | The password of the SSL certificate. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 53e59af3-3209- 452a-853c- ac10ad815929 | The ID of the request. |
| Result | String | {"id": 7, "websites": [], "create time": _ "1589771325", "name": "test-cert- 1", "signature": "ec23ec040764d0c c078879582a375c 2c", "info": {"serial": "0xdd45e828dca4b 8c9", "issuer": null, "not valid before": _ _ 1560816000, "not valid after": _ _ 1592352000, "domains": []}} |   |

**Examples**

Sample requests

```
https://semawaf.[RegionId].aliyuncs.com/?Action=UploadSSLCert &RegionId=cn-hangzhou &CertName=taobao_cert &CertFile={"name":"","content":"bEtrYmdrVFVSb3plY1dMa01BVmZrekhGdGxweVpl"} &KeyFile={"name":"","content":"eElzcEZEaElzaXlqVFBGU1B0ZG9qdm1iSEV1YW16"} &CertPassword=jgXzOoigHGWCLxE
```

Sample success responses `XML` format

```json
<UploadSSLCertResponse>
    <RequestId>53e59af3-3209-452a-853c-ac10ad815929</RequestId>
    <Result>{"id": 7, "websites": [], "create_time": "1589771325", "name": "test-cert-1
", "signature": "ec23ec040764d0cc078879582a375c2c", "info": {"serial": "0xdd45e828dca4b8c9", "issuer": null, "not_valid_before": 1560816000, "not_valid_after": 1592352000, "domains": []}}</Result> </UploadSSLCertResponse>
```

`JSON` format `{`

```json
  "RequestId":"53e59af3-3209-452a-853c-ac10ad815929",
  "Result":"{\"id\": 7, \"websites\": [], \"create_time\": \"1589771325\", \"name\": \"
test-cert-1\", \"signature\": \"ec23ec040764d0cc078879582a375c2c\", \"info\": {\"serial \": \"0xdd45e828dca4b8c9\", \"issuer\": null, \"not_valid_before\": 1560816000, \"not_v alid_after\": 1592352000, \"domains\": []}}"
```

`}`

**Error codes**

For a list of error codes, see Error codes.

#### 4.7.3 EditSSLCert

Modifies the name of a specific SSL certificate.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | EditSSLCert | The operation that you want to perform. Set the value to EditSSLCert. |
| RegionId | String | Yes | cn-hangzhou |   |
| Id | Integer | No | 1 | The ID of the SSL certificate. You can call the DescribeSSLCert operation to query the ID of the SSL certificate. |
| CertName | String | No | aliyun cert _ | The name of the SSL certificate. You can call the DescribeSSLCert operation to query the name of the SSL certificate. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|

| RequestId | String | 53e59af3-3209- 452a-853c- ac10ad815929 | The ID of the request. |
|---|---|---|---|
| Result | String | {"id": 1, "websites": [], "create time": _ "1589771325", "name": "test-cert- 1", "signature": "ec23ec040764d0c c078879582a375c 2c", "info": {"serial": "0xdd45e828dca4b 8c9", "issuer": null, "not valid before": _ _ 1560816000, "not valid after": _ _ 1592352000, "domains": []}} | The returned result of the request. |

**Examples**

Sample requests

```
https://semawaf.[ RegionId].aliyuncs.com/?Action=EditSSLCert &RegionId=cn-hangzhou &Id=1 &CertName=aliyun_cert
```

Sample success responses `XML` format

```json
<EditSSLCertResponse>
    <RequestId>53e59af3-3209-452a-853c-ac10ad815929</RequestId>
    <Result>{"id": 7, "websites": [], "create_time": "1589771325", "name": "test-cert-1
", "signature": "ec23ec040764d0cc078879582a375c2c", "info": {"serial": "0xdd45e828dca4b8c9", "issuer": null, "not_valid_before": 1560816000, "not_valid_after": 1592352000, "domains": []}}</Result> </EditSSLCertResponse>
```

`JSON` format `{`

```json
  "RequestId":"53e59af3-3209-452a-853c-ac10ad815929",
  "Result":"{\"id\": 7, \"websites\": [], \"create_time\": \"1589771325\", \"name\": \"
test-cert-1\", \"signature\": \"ec23ec040764d0cc078879582a375c2c\", \"info\": {\"serial \": \"0xdd45e828dca4b8c9\", \"issuer\": null, \"not_valid_before\": 1560816000, \"not_v alid_after\": 1592352000, \"domains\": []}}"
```

`}`

**Error codes**

For a list of error codes, see Error codes.

#### 4.7.4 DeleteSSLCert

Deletes a specific SSL certificate.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteSSLCert | The operation that you want to perform. Set the value to DeleteSSLCert. |
| RegionId | String | Yes | cn-hangzhou |   |
| IdList | RepeatL ist | Yes | [1, 2] | The ID of the SSL certificate. You can enter multiple IDs. You can call the DescribeSSLCert operation to query the IDs of SSL certificates. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 53e59af3-3209- 452a-853c- ac10ad815929 | The ID of the request. |
| Result | String |   | The returned result of the request. |

**Examples**

Sample requests

```
https://semawaf.[ RegionId].aliyuncs.com/?Action=DeleteSSLCert &RegionId=cn-hangzhou &IdList.1=1
```

Sample success responses `XML` format

```xml
<DeleteSSLCertResponse>
    <RequestId>53e59af3-3209-452a-853c-ac10ad815929</RequestId>
    <Result></Result>
</DeleteSSLCertResponse>
```

`JSON` format `{`

```json
  "RequestId":"53e59af3-3209-452a-853c-ac10ad815929",
  "Result":""
```

`}`

**Error codes**

For a list of error codes, see Error codes.

### 4.8 System information

#### 4.8.1 DescribeMetrics

Queries the monitoring metrics of physical WAF nodes.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeMetric s | The operation that you want to perform. Set the value to DescribeMetrics. |
| RegionId | String | Yes | cn-hangzhou |   |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 53e59af3-3209- 452a-853c- ac10ad815929 | The ID of the request. |
| Result | String | {"nodes": [{"id": "a36c01009.cloud. c01.amtest11", "qps": 0, "disk watermark": _ 0.0561921115664 5502, "throughput read": _ 368475, "throughput write" _ : 368434, "connections": 1, "delta connections _ ": 0}], "website count": 0, _ "domain count": 0, _ "is healthy": true} _ | The returned result of the request. |

**Examples**

Sample requests

```
https://semawaf.[ RegionId].aliyuncs.com/?Action=DescribeMetrics &RegionId=cn-hangzhou
```

Sample success responses `XML` format

```json
<DescribeMetricsResponse>
    <RequestId>53e59af3-3209-452a-853c-ac10ad815929</RequestId>
    <Result>{"nodes": [{"id": "a36c01009.cloud.c01.amtest11", "qps": 0,
"disk_watermark": 0.05619211156645502, "throughput_read": 368475, "throughput_write": 3 68434, "connections": 1, "delta_connections": 0}], "website_count": 0, "domain_count": 0, "is_healthy": true}</Result> </DescribeMetricsResponse>
```

`JSON` format `{`

```json
  "RequestId":"53e59af3-3209-452a-853c-ac10ad815929",
  "Result":"{\"nodes\": [{\"id\": \"a36c01009.cloud.c01.amtest11\", \"qps\": 0, \"disk_
watermark\": 0.05619211156645502, \"throughput_read\": 368475, \"throughput_write\": 36 8434, \"connections\": 1, \"delta_connections\": 0}], \"website_count\": 0, \"domain_count\": 0, \"is_healthy\": true}"
```

`}`

**Error codes**

For a list of error codes, see Error codes.

#### 4.8.2 DescribeNodeStatus

Queries the status information about physical WAF nodes.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeNodeS tatus | The operation that you want to perform. Set the value to DescribeNodeStatus. |
| RegionId | String | Yes | cn-hangzhou |   |

**Response parameters**

| Paramet er | Typ e | Example | Descripti on |
|---|---|---|---|
| RequestI d | Strin g | 53e59af3-3209-452a-853c-ac10ad815929 | The ID of the request. |
|   |   | [{"ha": {"services": [{"estate": "master", "healthy": true, "mstate": "idle", "name": "redis", "url": ""}]}, "id": "c43b02111.cloud.b03.amtest21", "node": {"cpu": 0.015010513044737767, "detector": {"conn client": 14, _ "conn client close": 0, "conn client estab": 0, "conn server": 0, _ _ _ _ _ "conn server close": 0, "conn server estab": 0, "cpu": 7.2e-05, _ _ _ _ "detector version": "4.1.4-5b5eb8e3", "fusion stat": {"req": _ _ {"average length": 0, "average time": 0, "count": 0, _ _ "max length": 0, "max time": 0, "min length": 0, "min time": 0, _ _ _ _ "sd length": 0, "sd time": 0, "top10 length": 0, "top10 time": 0, _ _ _ _ "top50 length": 0, "top50 time": 0, "top90 length": 0, _ _ _ |   |

| libaba Cloud ation Firewal | Security l (WAF) | -Web Appli Developer Guide·W | eb Applicati n Firewal |
|---|---|---|---|
| Result | Strin g | "top90 time": 0, "top99 length": 0, "top99 time": 0}, "rsp": _ _ _ {"average length": 0, "average time": 0, "count": 0, _ _ "max length": 0, "max time": 0, "min length": 0, "min time": 0, _ _ _ _ "sd length": 0, "sd time": 0, "top10 length": 0, "top10 time": 0, _ _ _ _ "top50 length": 0, "top50 time": 0, "top90 length": 0, _ _ _ "top90 time": 0, "top99 length": 0, "top99 time": 0}}, "ioread": _ _ _ 12782, "iowrite": 3416, "mem": 0.004292, "node": "c43b02111.cloud.b03.amtest21", "policy version": _ {"cc config version": "2827", "config version": "4", _ _ _ "current version": "1", "detector config version": "1890", _ _ _ "extra config version": "1890", "ip group config version": "7", _ _ _ _ _ "policy config version": "1890", "site config version": "1890"}, _ _ _ _ "req average time": 0, "req detect count": 0, "req detect time": _ _ _ _ _ _ 0, "req detect time distribution": [{"latency": 0, "percent": 99}, _ _ _ {"latency": 0, "percent": 90}, {"latency": 0, "percent": 75}, {"latency": 0, "percent": 50}], "req ngx count": 0, _ _ "req ngx time": 0, "req ngx time distribution": {}, _ _ _ _ _ "req num accepted": 0, "req num access log": 0, _ _ _ _ _ "req num attack": 0, "req num attack acl": 0, _ _ _ _ _ "req num attack web": 0, "req num blocked": 0, _ _ _ _ _ "req num blocked acl": 0, "req num blocked web": 0, _ _ _ _ _ _ "req num dropped": 0, "req num handled": 0, "req num total": _ _ _ _ _ _ 0, "rsp average time": 0, "rsp detect count": 0, _ _ _ _ "rsp detect time": 0, "rsp detect time distribution": [{"latency": _ _ _ _ _ 0, "percent": 99}, {"latency": 0, "percent": 90}, {"latency": 0, "percent": 75}, {"latency": 0, "percent": 50}], "rsp ngx count": 0, _ _ "rsp ngx time": 0, "rsp ngx time distribution": {}, _ _ _ _ _ "rsp num accepted": 0, "rsp num access log": 0, _ _ _ _ _ "rsp num attack": 0, "rsp num attack acl": 0, _ _ _ _ _ "rsp num attack web": 0, "rsp num blocked": 0, _ _ _ _ _ "rsp num blocked acl": 0, "rsp num blocked web": 0, _ _ _ _ _ _ "rsp num dropped": 0, "rsp num handled": 0, "rsp num total": 0, _ _ _ _ _ _ "time from": "1594696127.271", "time to": "1594696132.271", _ _ "uptime": "6 23:33:25.880", "workers": [{"conn client": 1, _ "conn client close": 0, "conn client estab": 0, "conn server": 0, _ _ _ _ _ "conn server close": 0, "conn server estab": 0, "cpu": 0, "index": _ _ _ _ 0, "ioread": 913, "iowrite": 244}, {"conn client": 1, _ "conn client close": 0, "conn client estab": 0, "conn server": 0, _ _ _ _ _ "conn server close": 0, "conn server estab": 0, "cpu": 0, "index": _ _ _ _ 1, "ioread": 913, "iowrite": 244}]}, "disk info": {"raids status": [], _ _ "read": 0, "time from": "1594696127", "time to": "1594696132", _ _ "total": "1124191502336", "usage": "61553455104", "write": 229376}, "last timestamp": "1594696127", "mario": _ {"access log stat": {"num pending": 0, "num processed": 3, _ _ _ _ "num processed last 10s": 0}, "detect log stat": _ _ _ _ _ {"num pending": 0, "num processed": 3, _ _ "num processed last 10s": 0}, "num goroutine": 8903, _ _ _ _ "policy version": {"acl data config": "11", "acl template": "58", _ _ _ _ "acl whitelist": "18", "detect log forward config": "10", _ _ _ _ "log aggregate config": "18", "plugin": "17", "summary config": _ _ _ "14"}, "router message stat": {"num receive": 0, _ _ _ "num receive error": 0, "num receive error last 10s": 0, _ _ _ _ _ _ "num receive last 10s": 0, "num receive pending": 0, _ _ _ _ _ "num send": 0, "num send error": 0, "num send error last 10s": _ _ _ _ _ _ _ 0, "num send last 10s": 0}}, "mem": 0.08940248252983965, _ _ _ "network io": [{"interface": "eth0", "read": 417525, "time from": _ _ "1594696127", "time to": "1594696132", "write": 467457}, _ {"interface": "eth1", "read": 403066, "time from": "1594696127", _ "time to": "1594696132", "write": 322033}, {"interface": _ "ens1f0", "read": 0, "time from": "1594696127", "time to": _ _ "1594696132", "write": 0}, {"interface": "ens1f1", "read": 0, "time from": "1594696127", "time to": "1594696132", "write": _ _ 0}, {"interface": "ens2f0", "read": 0, "time from": "1594696127", _ "time to": "1594696132", "write": 0}, {"interface": "ens2f1", _ "read": 0, "time from": "1594696127", "time to": "1594696132", _ _ "write": 0}], "received timestamp": 1594696132, "tengine": _ | The returned result of the request. |

|   |   | {"config version": 1868, "stats": {"accepts": 45, "connections": 1, _ "handled": 45, "requests": 2, "time from": 1594696127, "time to": _ _ 1594696132, "avg time": 0}, "hostname": _ "c43b02111.cloud.b03.amtest21"}, "timestamp": "1594696132", "uptime": 5188576, "status": "HEALTHY"}, "services": [{"cpu": 2.413311965811966e-05, "extra": null, "hostname": "c43b02111.cloud.b03.amtest21", "mem": 0.007124904089239252, "name": "tengine", "status": "HEALTHY", "uptime": 603206, "version": "v3.12.0 r5"}, {"cpu": _ 2.523696581196581e-05, "extra": null, "hostname": "c43b02111.cloud.b03.amtest21", "mem": 0.004504908368650695, "name": "detector-srv", "status": "HEALTHY", "uptime": 603206, "version": "v3.12.0 r5"}, {"cpu": _ 0.0011938266737891738, "extra": null, "hostname": "3ed9747c2003", "mem": 0.007155565200169913, "name": "mario", "status": "HEALTHY", "uptime": 603207, "version": "v3.12.0 r5"}, {"cpu": 0.0036347603276353276, "extra": null, _ "hostname": "598a767919bc", "mem": 0.0373652018262435, "name": "mgt-api", "status": "HEALTHY", "uptime": 321446, "version": "v3.12.0 r5"}, {"cpu": 0.0002562163105413105, _ "extra": null, "hostname": "c43b02111.cloud.b03.amtest21", "mem": 0.043149085452621895, "name": "mgt-redis", "status": "HEALTHY", "uptime": 603208, "version": "5.0"}, {"cpu": 1.5907836879432624e-05, "extra": null, "hostname": "c43b02111.cloud.b03.amtest21", "mem": 0.008885680945231749, "name": "agent", "status": "HEALTHY", "uptime": 603205, "version": "v3.12.0 r5"}, {"cpu": _ 0.037529611403212516, "extra": null, "hostname": "c43b02111.cloud.b03.amtest21", "mem": 0.0002865208871662617, "name": "minion", "status": "HEALTHY", "uptime": 603209, "version": "v3.12.0 r5"}], "sites": _ [{"name": "1749", "servers": {"10.10.XX.XX:15044": "HEALTHY"}}], " version details": [{"service name": "tengine", _ _ _ "versions": {"config version": {"heartbeat version": 1868, _ _ "database version": 1868, "version status": "sync"}}, _ _ "service status": "HEALTHY"}, {"service name": "detector-srv", _ _ "versions": {"cc config version": {"heartbeat version": 2827, _ _ _ "database version": 2837, "version history": [], "version status": _ _ _ "fall behind"}, "detector config version": {"heartbeat version": _ _ _ _ 1890, "database version": 1890, "version status": "sync"}, _ _ "extra config version": {"heartbeat version": 1890, _ _ _ "database version": 1890, "version status": "sync"}, _ _ "ip group config version": {"heartbeat version": 7, _ _ _ _ "database version": 7, "version status": "sync"}, _ _ "policy config version": {"heartbeat version": 1890, _ _ _ "database version": 1890, "version status": "sync"}, _ _ "site config version": {"heartbeat version": 1890, _ _ _ "database version": 1890, "version status": "sync"}}, _ _ "service status": "HEALTHY"}, {"service name": "mario", _ _ "versions": {"acl data config": {"heartbeat version": 11, _ _ _ "database version": 12, "version history": [], "version status": _ _ _ "fall behind"}, "acl template": {"heartbeat version": 58, _ _ _ "database version": 62, "version history": [], "version status": _ _ _ "fall behind"}, "acl whitelist": {"heartbeat version": 18, _ _ _ "database version": 18, "version status": "sync"}, _ _ "detect log forward config": {"heartbeat version": 10, _ _ _ _ "database version": 11, "version history": [], "version status": _ _ _ "fall behind"}, "log aggregate config": {"heartbeat version": 18, _ _ _ _ "database version": 20, "version history": [], "version status": _ _ _ "fall behind"}, "plugin": {"heartbeat version": 17, _ _ "database version": 20, "version history": [], "version status": _ _ _ "fall behind"}, "summary config": {"heartbeat version": 14, _ _ _ "database version": 14, "version status": "sync"}}, |   |
|---|---|---|---|

"service_status": "HEALTHY"}]}]

**Examples**

Sample requests

```
https://semawaf.[ RegionId].aliyuncs.com/?Action=DescribeNodeStatus &RegionId=cn-hangzhou
```

Sample success responses `XML` format

```json
<DescribeNodeStatusResponse>
    <RequestId>53e59af3-3209-452a-853c-ac10ad815929</RequestId>
    <Result>[{"ha": {"services": [{"estate": "master", "healthy": true, "mstate": "idle
", "name": "redis", "url": ""}]}, "id": "c43b02111.cloud.b03.amtest21", "node": {"cpu": 0.015010513044737767, "detector": {"conn_client": 14, "conn_client_close": 0, "conn_cli ent_estab": 0, "conn_server": 0, "conn_server_close": 0, "conn_server_estab": 0, "cpu": 7.2e-05, "detector_version": "4.1.4-5b5eb8e3", "fusion_stat": {"req": {"average_length": 0, "average_time": 0, "count": 0, "max_length": 0, "max_time": 0, "m in_length": 0, "min_time": 0, "sd_length": 0, "sd_time": 0, "top10_length": 0, "top10_time": 0, "top50_length": 0, "top50_time": 0, "top90_length": 0, "top90_time": 0 , "top99_length": 0, "top99_time": 0}, "rsp": {"average_length": 0, "average_time": 0, "count": 0, "max_length": 0, "max_time": 0, "min_length": 0, "min_time": 0, "sd_length": 0, "sd_time": 0, "top10_length": 0, "top10_time": 0, "top50_length": 0, "t op50_time": 0, "top90_length": 0, "top90_time": 0, "top99_length": 0, "top99_time": 0}} , "ioread": 12782, "iowrite": 3416, "mem": 0.004292, "node": "c43b02111.cloud.b03.amtest21", "policy_version": {"cc_config_version": "2827", "config _version": "4", "current_version": "1", "detector_config_version": "1890", "extra_config_version": "1890", "ip_group_config_version": "7", "policy_config_version": "1890", "site_config_version": "1890"}, "req_average_time": 0, "req_detect_count": 0, "req_detect_time": 0, "req_detect_time_distribution": [{"latency": 0, "percent": 99}, {"latency": 0, "percent": 90}, {"latency": 0, "percent" : 75}, {"latency": 0, "percent": 50}], "req_ngx_count": 0, "req_ngx_time": 0, "req_ngx_time_distribution": {}, "req_num_accepted": 0, "req_num_access_log": 0, "req_n um_attack": 0, "req_num_attack_acl": 0, "req_num_attack_web": 0, "req_num_blocked": 0, "req_num_blocked_acl": 0, "req_num_blocked_web": 0, "req_num_dropped": 0, "req_num_handled": 0, "req_num_total": 0, "rsp_average_time": 0, "rsp_detect_count": 0, "rsp_detect_time": 0, "rsp_detect_time_distribution": [{"latency": 0, "percent": 99}, { "latency": 0, "percent": 90}, {"latency": 0, "percent": 75}, {"latency": 0, "percent": 50}], "rsp_ngx_count": 0, "rsp_ngx_time": 0, "rsp_ngx_time_distribution": {}, "rsp_num_ accepted": 0, "rsp_num_access_log": 0, "rsp_num_attack": 0, "rsp_num_attack_acl": 0, "r sp_num_attack_web": 0, "rsp_num_blocked": 0, "rsp_num_blocked_acl": 0, "rsp_num_blocked_web": 0, "rsp_num_dropped": 0, "rsp_num_handled": 0, "rsp_num_total": 0, "time_from": "1594696127.271", "time_to": "1594696132.271", "uptime": "6 23:33:25.880", "workers": [{"conn_client": 1, "conn_client_close": 0, "conn_client_estab": 0, "conn_server": 0, "conn_server_close": 0, "conn_server_estab": 0, "cpu": 0, "index": 0, "ioread": 913, "iowrite": 244}, {"conn_client": 1, "conn_client_close": 0, "conn_client_estab": 0, "conn_server": 0, "conn_server_close": 0, "conn_server_estab": 0, "cpu": 0, "index": 1, "ioread": 913, "iowrite": 244}]}, "dis k_info": {"raids_status": [], "read": 0, "time_from": "1594696127", "time_to": "1594696 132", "total": "1124191502336", "usage": "61553455104", "write": 229376}, "last_timesta mp": "1594696127", "mario": {"access_log_stat": {"num_pending": 0, "num_processed": 3, "num_processed_last_10s": 0}, "detect_log_stat": {"num_pending": 0, "num_processed": 3, "num_processed_last_10s": 0}, "num_goroutine": 8903, "policy_version": {"acl_data_config": "11", "acl_template": "58", "acl_whitelist": "18", "detect_log_forward_config": "10", "log_aggregate_config": "18", "plugin": "17", "summa ryconfig":"14"},"routermessagestat":{"numreceive":0,"numreceiveerror":0,"n
```

```json
ry_config: 14}, router_message_stat: {num_receive: 0, num_receive_error: 0, n um_receive_error_last_10s": 0, "num_receive_last_10s": 0, "num_receive_pending": 0, "nu m_send": 0, "num_send_error": 0, "num_send_error_last_10s": 0, "num_send_last_10s": 0}} , "mem": 0.08940248252983965, "network_io": [{"interface": "eth0", "read": 417525, "tim e_from": "1594696127", "time_to": "1594696132", "write": 467457}, {"interface": "eth1", "read": 403066, "time_from": "1594696127", "time_to": "1594696132", "write": 322033}, { "interface": "ens1f0", "read": 0, "time_from": "1594696127", "time_to": "1594696132", " write": 0}, {"interface": "ens1f1", "read": 0, "time_from": "1594696127", "time_to": "1 594696132", "write": 0}, {"interface": "ens2f0", "read": 0, "time_from": "1594696127", "time_to": "1594696132", "write": 0}, {"interface": "ens2f1", "read": 0, "time_from": " 1594696127", "time_to": "1594696132", "write": 0}], "received_timestamp": 1594696132, " tengine": {"config_version": 1868, "stats": {"accepts": 45, "connections": 1, "handled" : 45, "requests": 2, "time_from": 1594696127, "time_to": 1594696132, "avg_time": 0}, "h ostname": "c43b02111.cloud.b03.amtest21"}, "timestamp": "1594696132", "uptime": 5188576 , "status": "HEALTHY"}, "services": [{"cpu": 2.413311965811966e-05, "extra": null, "hos tname": "c43b02111.cloud.b03.amtest21", "mem": 0.007124904089239252, "name": "tengine", "status": "HEALTHY", "uptime": 603206, "version": "v3.12.0_r5"}, {"cpu": 2.523696581196581e-05, "extra": null, "hostname": "c43b02111.cloud.b03.amtest21", "mem" : 0.004504908368650695, "name": "detector-srv", "status": "HEALTHY", "uptime": 603206, "version": "v3.12.0_r5"}, {"cpu": 0.0011938266737891738, "extra": null, "hostname": "3e d9747c2003", "mem": 0.007155565200169913, "name": "mario", "status": "HEALTHY", "uptime ": 603207, "version": "v3.12.0_r5"}, {"cpu": 0.0036347603276353276, "extra": null, "hos tname": "598a767919bc", "mem": 0.0373652018262435, "name": "mgt-api", "status": "HEALTH Y", "uptime": 321446, "version": "v3.12.0_r5"}, {"cpu": 0.0002562163105413105, "extra": null, "hostname": "c43b02111.cloud.b03.amtest21", "mem": 0.043149085452621895, "name": "mgt-redis", "status": "HEALTHY", "uptime": 603208, "version": "5.0"}, {"cpu": 1.590783 6879432624e-05, "extra": null, "hostname": "c43b02111.cloud.b03.amtest21", "mem": 0.008 885680945231749, "name": "agent", "status": "HEALTHY", "uptime": 603205, "version": "v3 .12.0_r5"}, {"cpu": 0.037529611403212516, "extra": null, "hostname": "c43b02111.cloud.b03.amtest21", "mem": 0.0002865208871662617, "name": "minion", "status ": "HEALTHY", "uptime": 603209, "version": "v3.12.0_r5"}], "sites": [{"name": "1749", " servers": {"10.10.XX.XX:15044": "HEALTHY"}}], "_version_details": [{"service_name": "te ngine", "versions": {"config_version": {"heartbeat_version": 1868, "database_version": 1868, "version_status": "sync"}}, "service_status": "HEALTHY"}, {"service_name": "detec tor-srv", "versions": {"cc_config_version": {"heartbeat_version": 2827, "database_version": 2837, "version_history": [], "version_status": "fall_behind"}, "det ector_config_version": {"heartbeat_version": 1890, "database_version": 1890, "version_s tatus": "sync"}, "extra_config_version": {"heartbeat_version": 1890, "database_version": 1890, "version_status": "sync"}, "ip_group_config_version": {"heart beat_version": 7, "database_version": 7, "version_status": "sync"}, "policy_config_version": {"heartbeat_version": 1890, "database_version": 1890, "version _status": "sync"}, "site_config_version": {"heartbeat_version": 1890, "database_version": 1890, "version_status": "sync"}}, "service_status": "HEALTHY"}, {"s ervice_name": "mario", "versions": {"acl_data_config": {"heartbeat_version": 11, "datab ase_version": 12, "version_history": [], "version_status": "fall_behind"}, "acl_template": {"heartbeat_version": 58, "database_version": 62, "version_history": [] , "version_status": "fall_behind"}, "acl_whitelist": {"heartbeat_version": 18, "databas e_version": 18, "version_status": "sync"}, "detect_log_forward_config": {"heartbeat_version": 10, "database_version": 11, "version_history": [], "version_status": "fall_behind"}, "log_aggregate_config": {"heartbeat_version": 18, "da tabase_version": 20, "version_history": [], "version_status": "fall_behind"}, "plugin": {"heartbeat_version": 17, "database_version": 20, "version_history": [], "version_status": "fall_behind"}, "summary_config": {"heartbeat_version": 14, "database _version": 14, "version_status": "sync"}}, "service_status": "HEALTHY"}]}]</Result> </DescribeNodeStatusResponse>
```

`p` `JSON` format `{`

```json
  "RequestId":"53e59af3-3209-452a-853c-ac10ad815929",
  "Result":"[{\"ha\": {\"services\": [{\"estate\": \"master\", \"healthy\": true, \"mst
ate\": \"idle\", \"name\": \"redis\", \"url\": \"\"}]}, \"id\": \"c43b02111.cloud.b03.amtest21\", \"node\": {\"cpu\": 0.015010513044737767, \"detector\ ": {\"conn_client\": 14, \"conn_client_close\": 0, \"conn_client_estab\": 0, \"conn_ser ver\": 0, \"conn_server_close\": 0, \"conn_server_estab\": 0, \"cpu\": 7.2e-05, \"detec tor_version\": \"4.1.4-5b5eb8e3\", \"fusion_stat\": {\"req\": {\"average_length\": 0, \ "average_time\": 0, \"count\": 0, \"max_length\": 0, \"max_time\": 0, \"min_length\": 0 , \"min_time\": 0, \"sd_length\": 0, \"sd_time\": 0, \"top10_length\": 0, \"top10_time\": 0, \"top50_length\": 0, \"top50_time\": 0, \"top90_length\": 0, \"top90 _time\": 0, \"top99_length\": 0, \"top99_time\": 0}, \"rsp\": {\"average_length\": 0, \ "average_time\": 0, \"count\": 0, \"max_length\": 0, \"max_time\": 0, \"min_length\": 0 , \"min_time\": 0, \"sd_length\": 0, \"sd_time\": 0, \"top10_length\": 0, \"top10_time\": 0, \"top50_length\": 0, \"top50_time\": 0, \"top90_length\": 0, \"top90 _time\": 0, \"top99_length\": 0, \"top99_time\": 0}}, \"ioread\": 12782, \"iowrite\": 3 416, \"mem\": 0.004292, \"node\": \"c43b02111.cloud.b03.amtest21\", \"policy_version\": {\"cc_config_version\": \"2827\", \"config_version\": \"4\", \"current_version\": \"1\" , \"detector_config_version\": \"1890\", \"extra_config_version\": \"1890\", \"ip_group_config_version\": \"7\", \"policy_config_version\": \"1890\", \"site_config_version\": \"1890\"}, \"req_average_time\": 0, \"req_detect_count\": 0, \ "req_detect_time\": 0, \"req_detect_time_distribution\": [{\"latency\": 0, \"percent\": 99}, {\"latency\": 0, \"percent\": 90}, {\"latency\": 0, \"percent\": 75}, {\"latency\": 0, \"percent\": 50}], \"req_ngx_count\": 0, \"req_ngx_time\": 0, \"req_ngx_time_distribution\": {}, \"req_num_accepted\": 0, \"req_num_access_log\": 0, \"req_num_attack\": 0, \"req_num_attack_acl\": 0, \"req_num_attack_web\": 0, \"req_num_blocked\": 0, \"req_num_blocked_acl\": 0, \"req_num_blocked_web\": 0, \"req_n um_dropped\": 0, \"req_num_handled\": 0, \"req_num_total\": 0, \"rsp_average_time\": 0, \"rsp_detect_count\": 0, \"rsp_detect_time\": 0, \"rsp_detect_time_distribution\": [{\" latency\": 0, \"percent\": 99}, {\"latency\": 0, \"percent\": 90}, {\"latency\": 0, \"p ercent\": 75}, {\"latency\": 0, \"percent\": 50}], \"rsp_ngx_count\": 0, \"rsp_ngx_time\": 0, \"rsp_ngx_time_distribution\": {}, \"rsp_num_accepted\": 0, \"rsp_ num_access_log\": 0, \"rsp_num_attack\": 0, \"rsp_num_attack_acl\": 0, \"rsp_num_attack_web\": 0, \"rsp_num_blocked\": 0, \"rsp_num_blocked_acl\": 0, \"rsp_nu m_blocked_web\": 0, \"rsp_num_dropped\": 0, \"rsp_num_handled\": 0, \"rsp_num_total\": 0, \"time_from\": \"1594696127.271\", \"time_to\": \"1594696132.271\", \"uptime\": \"6 23:33:25.880\", \"workers\": [{\"conn_client\": 1, \"conn_client_close\": 0, \"conn_client_estab\": 0, \"conn_server\": 0, \"conn_server_close\": 0, \"conn_server_estab\": 0, \"cpu\": 0, \"index\": 0, \"ioread\": 913, \"iowrite\": 244}, {\"conn_client\": 1, \"conn_client_close\": 0, \"conn_client_estab\": 0, \"conn_server\": 0, \"conn_server_close\": 0, \"conn_server_estab\": 0, \"cpu\": 0, \"i ndex\": 1, \"ioread\": 913, \"iowrite\": 244}]}, \"disk_info\": {\"raids_status\": [], \"read\": 0, \"time_from\": \"1594696127\", \"time_to\": \"1594696132\", \"total\": \"1 124191502336\", \"usage\": \"61553455104\", \"write\": 229376}, \"last_timestamp\": \"1 594696127\", \"mario\": {\"access_log_stat\": {\"num_pending\": 0, \"num_processed\": 3 , \"num_processed_last_10s\": 0}, \"detect_log_stat\": {\"num_pending\": 0, \"num_processed\": 3, \"num_processed_last_10s\": 0}, \"num_goroutine\": 8903, \"policy _version\": {\"acl_data_config\": \"11\", \"acl_template\": \"58\", \"acl_whitelist\": \"18\", \"detect_log_forward_config\": \"10\", \"log_aggregate_config\": \"18\", \"plug in\": \"17\", \"summary_config\": \"14\"}, \"router_message_stat\": {\"num_receive\": 0 \"numreceiveerror\":0 \"numreceiveerrorlast10s\":0
```

```
, \num_receive_error\: 0, \num_receive_error_last_10s\: 0, \"num_receive_last_10s\": 0, \"num_receive_pending\": 0, \"num_send\": 0, \"num_send_error\": 0, \"num_send_error_last_10s\": 0, \"num_send_last_10s\": 0}}, \"me m\": 0.08940248252983965, \"network_io\": [{\"interface\": \"eth0\", \"read\": 417525, \"time_from\": \"1594696127\", \"time_to\": \"1594696132\", \"write\": 467457}, {\"inte rface\": \"eth1\", \"read\": 403066, \"time_from\": \"1594696127\", \"time_to\": \"1594 696132\", \"write\": 322033}, {\"interface\": \"ens1f0\", \"read\": 0, \"time_from\": \ "1594696127\", \"time_to\": \"1594696132\", \"write\": 0}, {\"interface\": \"ens1f1\", \"read\": 0, \"time_from\": \"1594696127\", \"time_to\": \"1594696132\", \"write\": 0}, {\"interface\": \"ens2f0\", \"read\": 0, \"time_from\": \"1594696127\", \"time_to\": \" 1594696132\", \"write\": 0}, {\"interface\": \"ens2f1\", \"read\": 0, \"time_from\": \" 1594696127\", \"time_to\": \"1594696132\", \"write\": 0}], \"received_timestamp\": 1594 696132, \"tengine\": {\"config_version\": 1868, \"stats\": {\"accepts\": 45, \"connections\": 1, \"handled\": 45, \"requests\": 2, \"time_from\": 1594696127, \"time _to\": 1594696132, \"avg_time\": 0}, \"hostname\": \"c43b02111.cloud.b03.amtest21\"}, \ "timestamp\": \"1594696132\", \"uptime\": 5188576, \"status\": \"HEALTHY\"}, \"services \": [{\"cpu\": 2.413311965811966e-05, \"extra\": null, \"hostname\": \"c43b02111.cloud.b03.amtest21\", \"mem\": 0.007124904089239252, \"name\": \"tengine\", \"status\": \"HEALTHY\", \"uptime\": 603206, \"version\": \"v3.12.0_r5\"}, {\"cpu\": 2. 523696581196581e-05, \"extra\": null, \"hostname\": \"c43b02111.cloud.b03.amtest21\", \ "mem\": 0.004504908368650695, \"name\": \"detector-srv\", \"status\": \"HEALTHY\", \"up time\": 603206, \"version\": \"v3.12.0_r5\"}, {\"cpu\": 0.0011938266737891738, \"extra\ ": null, \"hostname\": \"3ed9747c2003\", \"mem\": 0.007155565200169913, \"name\": \"mar io\", \"status\": \"HEALTHY\", \"uptime\": 603207, \"version\": \"v3.12.0_r5\"}, {\"cpu \": 0.0036347603276353276, \"extra\": null, \"hostname\": \"598a767919bc\", \"mem\": 0. 0373652018262435, \"name\": \"mgt-api\", \"status\": \"HEALTHY\", \"uptime\": 321446, \ "version\": \"v3.12.0_r5\"}, {\"cpu\": 0.0002562163105413105, \"extra\": null, \"hostna me\": \"c43b02111.cloud.b03.amtest21\", \"mem\": 0.043149085452621895, \"name\": \"mgtredis\", \"status\": \"HEALTHY\", \"uptime\": 603208, \"version\": \"5.0\"}, {\"cpu\": 1.5907836879432624e-05, \"extra\": null, \"hostname\": \"c43b02111.cloud.b03.amtest21\", \"mem\": 0.008885680945231749, \"name\": \"agent\", \ "status\": \"HEALTHY\", \"uptime\": 603205, \"version\": \"v3.12.0_r5\"}, {\"cpu\": 0.0 37529611403212516, \"extra\": null, \"hostname\": \"c43b02111.cloud.b03.amtest21\", \"m em\": 0.0002865208871662617, \"name\": \"minion\", \"status\": \"HEALTHY\", \"uptime\": 603209, \"version\": \"v3.12.0_r5\"}], \"sites\": [{\"name\": \"1749\", \"servers\": {\ "10.10.XX.XX:15044\": \"HEALTHY\"}}], \"_version_details\": [{\"service_name\": \"tengi ne\", \"versions\": {\"config_version\": {\"heartbeat_version\": 1868, \"database_version\": 1868, \"version_status\": \"sync\"}}, \"service_status\": \"HEALT HY\"}, {\"service_name\": \"detector-srv\", \"versions\": {\"cc_config_version\": {\"he artbeat_version\": 2827, \"database_version\": 2837, \"version_history\": [], \"version _status\": \"fall_behind\"}, \"detector_config_version\": {\"heartbeat_version\": 1890, \"database_version\": 1890, \"version_status\": \"sync\"}, \"extra_config_version\": {\ "heartbeat_version\": 1890, \"database_version\": 1890, \"version_status\": \"sync\"}, \"ip_group_config_version\": {\"heartbeat_version\": 7, \"database_version\": 7, \"vers ion_status\": \"sync\"}, \"policy_config_version\": {\"heartbeat_version\": 1890, \"dat abase_version\": 1890, \"version_status\": \"sync\"}, \"site_config_version\": {\"heart beat_version\": 1890, \"database_version\": 1890, \"version_status\": \"sync\"}}, \"ser vice_status\": \"HEALTHY\"}, {\"service_name\": \"mario\", \"versions\": {\"acl_data_config\": {\"heartbeat_version\": 11, \"database_version\": 12, \"version_h istory\": [], \"version_status\": \"fall_behind\"}, \"acl_template\": {\"heartbeat_version\": 58, \"database_version\": 62, \"version_history\": [], \"versio n_status\": \"fall_behind\"}, \"acl_whitelist\": {\"heartbeat_version\": 18, \"database_version\": 18, \"version_status\": \"sync\"}, \"detect_log_forward_config\": {\"heartbeat_version\": 10, \"database_version\": 11, \"version_history\": [], \"versio nstatus\": \"fallbehind\"}, \"logaggregateconfig\": {\"heartbeatversion\": 18, \"d
```

```
_status\:\
```

`a`

```
_be d\},\ og_aggegate_co g\:{\ eatbeat_eso\: 8,\d atabase_version\": 20, \"version_history\": [], \"version_status\": \"fall_behind\"}, \ "plugin\": {\"heartbeat_version\": 17, \"database_version\": 20, \"version_history\": [ ], \"version_status\": \"fall_behind\"}, \"summary_config\": {\"heartbeat_version\": 14 , \"database_version\": 14, \"version_status\": \"sync\"}}, \"service_status\": \"HEALT HY\"}]}]"
```

`}`

**Error codes**

For a list of error codes, see Error codes.

#### 4.8.3 DescribeRealTimeAccess

Queries the monitoring information about access status.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeRealTi meAccess | The operation that you want to perform. Set the value to DescribeRealTimeAccess. |
| RegionId | String | Yes | cn-hangzhou |   |
| Type | String | Yes | ip | The type to filter monitoring information. Valid values: ip session website url If you leave this parameter unspecified, all monitoring information is returned. These types can be combined to filter monitoring information. Example: ipwebsite. |
| OrderBy | String | Yes | count | The method to sort monitoring information. Valid values: count: the number of requests time: the average time of responses |
| Limit | Integer | No | 100 | The upper limit of returned entries. Default value: 100. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 53e59af3-3209- 452a-853c- ac10ad815929 | The ID of the request. |

| Result | String | {"data": [{"ip": "10.10.XX.XX", "count": 2}], "type": "top ip", _ "order by": _ "count"} | The returned result of the request. |
|---|---|---|---|

**Examples**

Sample requests

```
https://semawaf.[ RegionId].aliyuncs.com/?Action=DescribeRealTimeAccess &RegionId=cn-hangzhou &Type=ip &OrderBy=count &Limit=100
```

Sample success responses `XML` format

```xml
<DescribeRealTimeAccessResponse>
    <RequestId>53e59af3-3209-452a-853c-ac10ad815929</RequestId>
    <Result>{"data": [{"ip": "10.10.XX.XX", "count": 2}], "type": "top_ip", "order_by":
"count"}</Result> </DescribeRealTimeAccessResponse>
```

`JSON` format `{`

```json
  "RequestId":"53e59af3-3209-452a-853c-ac10ad815929",
  "Result":"{\"data\": [{\"ip\": \"10.10.XX.XX\", \"count\": 2}], \"type\": \"top_ip\",
\"order_by\": \"count\"}"
```

`}`

**Error codes**

For a list of error codes, see Error codes.

#### 4.8.4 DescribeAttackDetectionAggregation

Queries the statistics on attack detection aggregation.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeAttack DetectionAggr egation | The operation that you want to perform. Set the value to DescribeAttackDetectionAggregati on. |
| RegionId | String | Yes | cn-hangzhou |   |

| AggregationT ype | String | Yes | source | The type of attack detection aggregation. Valid values: source destination |
|---|---|---|---|---|

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 53e59af3-3209- 452a-853c- ac10ad815929 | The ID of the request. |
| Result | String | {"aggregate type": _ "src ip", "values": _ [{"item": "10.10.XX.XX", "value": 3, "timestamp": "1594695947"}]} | The returned result of the request. |

**Examples**

Sample requests

```
https://semawaf.[ RegionId].aliyuncs.com/?Action=DescribeAttackDetectionAggregation &RegionId=cn-hangzhou &AggregationType=source
```

Sample success responses `XML` format

```json
<DescribeAttackDetectionAggregationResponse>
    <RequestId>53e59af3-3209-452a-853c-ac10ad815929</RequestId>
    <Result>{"aggregate_type": "src_ip", "values": [{"item": "10.10.XX.XX", "value": 3,
"timestamp": "1594695947"}]}</Result> </DescribeAttackDetectionAggregationResponse>
```

`JSON` format

```
https://semawaf.[ RegionId].aliyuncs.com/?Action=DescribeAttackDetectionAggregation &RegionId=cn-hangzhou &AggregationType=source
```

**Error codes**

For a list of error codes, see Error codes.

**4.8.5.**

#### DescribeAttackDetectionAggregationConfig

Queries the configurations of attack detection aggregation.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeAttack DetectionAggr egationConfig | The operation that you want to perform. Set the value to DescribeAttackDetectionAggregati onConfig. |
| RegionId | String | Yes | cn-hangzhou |   |

**Response parameters**

| Paramete r | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 53e59af3-3209-452a-853c- ac10ad815929 | The ID of the request. |
| Result | String | {"is enabled": true} _ |   |

**Examples**

Sample requests

```
https://semawaf.[RegionId].aliyuncs.com/? Action=DescribeAttackDetectionAggregationConfig &RegionId=cn-hangzhou
```

Sample success responses `XML` format

```xml
<DescribeAttackDetectionAggregationConfigResponse>
    <RequestId>53e59af3-3209-452a-853c-ac10ad815929</RequestId>
    <Result>{"is_enabled": true}</Result>
</DescribeAttackDetectionAggregationConfigResponse>
```

`JSON` format `{`

```json
  "RequestId":"53e59af3-3209-452a-853c-ac10ad815929",
  "Result":"{\"is_enabled\": true}"
```

`}`

**Error codes**

For a list of error codes, see Error codes.

#### 4.8.6 ToggleAttackDetectionAggregation

Enables or disables the attack detection aggregation feature.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ToggleAttackDet ectionAggregati on | The operation that you want to perform. Set the value to ToggleAttackDetectionAggregation. |
| RegionId | String | Yes | cn-hangzhou |   |
| Enable | Boolean | No | true | Specifies whether to enable the attack detection aggregation feature. Valid values: true false Default value: true. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 53e59af3-3209- 452a-853c- ac10ad815929 | The ID of the request. |
| Result | String | {"is enabled": _ true} | The returned result of the request. |

**Examples**

Sample requests

```
https://semawaf.[ RegionId].aliyuncs.com/?Action=ToggleAttackDetectionAggregation &RegionId=cn-hangzhou &Enable=true
```

Sample success responses `XML` format

```xml
<ToggleAttackDetectionAggregationResponse>
    <RequestId>53e59af3-3209-452a-853c-ac10ad815929</RequestId>
    <Result></Result>
</ToggleAttackDetectionAggregationResponse>
```

`JSON` format `{`

```json
  "RequestId":"53e59af3-3209-452a-853c-ac10ad815929",
  "Result":""
```

`}`

**Error codes**

For a list of error codes, see Error codes.

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
