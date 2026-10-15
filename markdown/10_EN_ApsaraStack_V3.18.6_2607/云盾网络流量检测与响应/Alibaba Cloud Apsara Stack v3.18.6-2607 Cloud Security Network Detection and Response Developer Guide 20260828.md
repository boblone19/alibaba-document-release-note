---
title: "Alibaba Cloud Apsara Stack v3.18.6-2607 Cloud Security Network Detection and Response Developer Guide 20260828"
product_version: "V3.18.6_2607"
doc_version: "20260828"
pdf_pages: 457
source_pdf: "Alibaba Cloud Apsara Stack v3.18.6-2607 Cloud Security Network Detection and Response Developer Guide 20260828.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/3816%202607/pdf%203/%E4%BA%91%E7%9B%BE%E7%BD%91%E7%BB%9C%E6%B5%81%E9%87%8F%E6%A3%80%E6%B5%8B%E4%B8%8E%E5%93%8D%E5%BA%94/Alibaba%20Cloud%20Apsara%20Stack%20v3.18.6-2607%20Cloud%20Security%20Network%20Detection%20and%20Response%20Developer%20Guide%2020260828.pdf"
converter: pdf2md (PyMuPDF line classifier)
---

# Alibaba Cloud Apsara Stack v3.18.6-2607 Cloud Security Network Detection and Response Developer Guide 20260828

## Quick Start

### Using the development

**documentation**

This topic describes how to find the product documentation that you need to use Apsara Stack APIs.

**Workflow**

Follow the steps in the flowchart below to find the development documentation that you need.

**Prerequisites**

Obtain the Apsara Stack version from an Operations and Maintenance (O&M) engineer or an operations administrator.

**Procedure**

Obtain the product documentation that you need from the Apsara Stack Documentation Center.
1. In a browser, open the Apsara Stack Documentation Center.
2. Based on your Apsara Stack version, click the **Enterprise**, **Agile**, or **All-in-One** tab.
3. From the drop-down list, select your Apsara Stack version.
4. In the navigation pane on the left, select the product.
5. In the document area, click **view details** or **download PDF**.

### API call flow

Apsara Stack supports API calls through a POP gateway, providing an experience consistent with the public cloud. Starting with Enterprise Edition V3.16.0, Apsara Stack APIs use a POP gateway for calls by default. This topic describes how to call Apsara Stack APIs through a POP gateway.

**Flowchart**

| Obtain API information. Obtain an AccessKey or an STS AccessKey. Obtain common header parameters. |   |
|---|---|
| Obtain the Endpoint for Apsara Uni- manager Management Console. Obtain the SDK package for Apsara Uni-manager Management Console. Call the API. |   |

Make prep Make the ca

**Steps**

1. Obtain the required AccessKey.
For more information, see Get an AccessKey or Get an STS AccessKey.

**Note**

You can use a personal AccessKey or an STS AccessKey to call the APIs of Apsara Unimanager Management Console and other cloud products.
2. Obtain the RegionID.
3. Obtain the organization ID and resource group ID.
You can obtain the organization ID by calling an API. For more information, see the GetOrga nizationList chapter in the Apsara Uni-manager Management Console Developer Guide. You can obtain the resource group ID by calling an API. For more information, see the ListResourceGroup chapter in the Apsara Uni-manager Management Console Developer Gui de.

**Note**

When you call an API, add the organization ID `<x-acs-organizationid>` and the resource group ID `<x-acs-resourcegroupid>` to the header parameters. This specifies the organization and resource group for the resource and allows for isolated queries of instance resources. If you omit the organization ID `<x-acs-organizationid>` , the current user's organization is used by default. If you omit the resource group ID `<x-acs-resourcegroupid>` , the value is empty by default. If you specify a resource group ID, you must also specify an organization ID.
4. Obtain the relevant API reference document.
Review the developer guide for the target cloud product to understand its features and usage. For more information about how to obtain and use the developer guide, see Developer documentation instructions.
5. Obtain the cloud product Endpoint.
6. Obtain the cloud product SDK and call the cloud product API.

## Preparations

### Obtain the information and

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
6. In the API operation list, view all API operations of the current version.
7. Click the operation that you want to call. Obtain the endpoint from the Endpoint parameter
on the Parameter tab.

### Log on to the developer portal

**console**

You can log on to the developer portal console from the Apsara Uni-manager Management Console.

**Prerequisites**

Before logging on to the Apsara Uni-manager Management Console, obtain the service domain name from the deployment administrator. Use the Chrome browser.

**Procedure**

1. In the address bar of your browser, enter the service domain name of the Apsara Uni-
manager Management Console and press Enter.
2. Enter the correct username and password.
Obtain the username and password to log on to the console from the operations administrator.

**Note**

When you log on to the Apsara Uni-manager Management Console for the first time, you must change the password. Follow the prompts to change the password. To improve security, the password must be 10 to 32 characters long and contain characters from at least two of the following types: Uppercase or lowercase letters (A–Z, a–z) Digits (0–9) Special characters, such as exclamation points (!), at signs (@), number signs (#), dollar signs ($), and percent signs (%)
3. Click **Log On**.
4. If multi-factor authentication (MFA) is enabled for your account, perform one of the
following operations: First logon after an administrator forces MFA: a. On the page for attaching a virtual MFA device, follow the on-screen instructions to attach the MFA device. b. Re-enter your username and password as described in Step 2, and then click **Log On**. c. Enter the 6-digit MFA code and click **Authenticate**. You have enabled and attached MFA: Enter the 6-digit MFA code and click **Authenticate**.

**Note**

For more information, see the **"Attach and enable a virtual MFA device"** topic in the **Apsara Uni-manager Management Console User Guide** .
5. In the menu bar at the top of the page, choose **Products > Application Services >**
**Developer Portal**.

### Obtain an AccessKey

An AccessKey supports two authorization modes: Resource Access Management (RAM) and Security Token Service (STS). When you make a call, you can use an AccessKey from either mode. This topic describes how to obtain an AccessKey that uses RAM authorization.

**Background information**

An AccessKey consists of an AccessKey ID and an AccessKey secret. It uses symmetric encryption to authenticate the identity of a request sender. The AccessKey ID identifies the user, and the AccessKey secret is a string that the user uses to create an encrypted signature. The two authorization modes for an AccessKey are as follows: RAM authorization: Provides an AccessKey ID and an AccessKey secret to a third-party requester. STS authorization: Provides an AccessKey ID, an AccessKey secret, and a security token to a third-party requester. For more information, see Obtain an STS AccessKey. Apsara Uni-manager Management Console provides two types of AccessKeys: personal and organization. Only operations administrators and primary organization administrators can obtain organization AccessKeys. You can use a personal account AccessKey to call the APIs of Apsara Uni-manager Management Console and other cloud products. If you use a personal account AccessKey, you must add the required restrictive parameters to the header to prevent permission errors.

**Warning**

A personal account AccessKey has restricted permissions and is managed by the Apsara Uni-manager Management Console permission system. In contrast, an organization AccessKey has broader permissions. Administrators must ensure the security of any operation that uses an organization AccessKey.

| Parameter | Description |
|---|---|
| x-acs-regionid | The region. For example, cn-hangzhou-*. |
| x-acs-organizationid | The ID of the organization in Apsara Uni-manager Management Console. To obtain the ID, see the Apsara Uni-manager Management Console Development Guide document about GetOrganizationList. |
| x-acs-resourcegroupid | The ID of the resource group in Apsara Uni- manager Management Console. To obtain the ID, see the Apsara Uni-manager Management Console Development Guide document about ListResourceGroup. |
| x-acs-instanceid | The ID of the instance for the operation. For example, you can find the instance ID of an ECS instance in the ECS instance list. |

**Obtain a personal account AccessKey**

Follow these steps to obtain a personal account AccessKey:
1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the page, click your profile picture, and then click **Personal**
**Information**.
3. In the **Alibaba Cloud AccessKey** section, view the AccessKey information for your
personal account.

**Note**

Your AccessKey ID and AccessKey secret are the credentials used to access your cloud resources. These credentials grant full permissions to your account. Keep them secure.

**Obtain an organization AccessKey**

Follow these steps to obtain an organization AccessKey:
1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top menu bar, click **Enterprise**.
3. In the navigation pane on the left, choose **Resource Management > Organization**
**Management**.
4. In the organization chart, click the name of the target primary organization.
5. Click **Manage AccessKey**.
6. In the dialog box that appears, view the organization AccessKey information.

### Obtain an AccessKey pair

**assigned by STS**

This topic describes how to use Security Token Service (STS) to call API operations in Apsara Stack.

**Background information**

Apsara Stack STS allows you to manage temporary credentials for your Apsara Stack resources. You can use STS to call API operations in Apsara Stack. An AccessKey pair assigned by STS consists of an AccessKey ID, an AccessKey secret, and a security token. When you use STS to call API operations, you must use an AccessKey pair assigned by STS.

**Procedure**

1. Obtain the Alibaba Cloud Resource Name (ARN) of your `Resource Access Management (RAM)`
`role` . i. Log on to the Apsara Uni-manager Management Console. ii. Click the profile picture in the upper-right corner of the page and click **User**
**Information**.
iii. Click **View Current Role Policy**. In the **View Policies of Current Role** dialog box, view the ARN of your `RAM role` .
2. Obtain the AccessKey pair assigned by STS.

**Note**

You must replace the variables in the following code with actual values. Delete the angle brackets (<>) before you submit the code. Variables: <yourRegionID>: Replace it with the actual region ID. <yourAccessKeyID>: Replace it with your AccessKey ID. <yourAccessKeySecret>: Replace it with your AccessKey secret. <yourRoleSessionName>: Replace it with your current session name. In most cases, this variable is set to the identity of the user who makes API calls. Example: username. You can identify the users who assume the same RAM role to perform operations based on the value of the `RoleSessionName` variable. This way, you can perform user-specific auditing. The value is 2 to 64 characters in length and can contain letters, digits, periods (.), at signs (@), hyphens (-), and underscores (_). <yourRoleArn>: Replace it with the ARN of your RAM role. "sts.aliyuns.com": Replace it with the actual endpoint of STS.

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
3. Use the AccessKey pair assigned by STS to call an operation of a cloud service. The
following sample code provides an example on how to use the AccessKey pair assigned by STS to call the `DescribeZones` operation of Elastic Compute Service (ECS):

**Note**

You must replace the variables in the following code with actual values. Delete the angle brackets (<>) before you submit the code. Variables: <yourRegionID>: Replace it with the actual region ID. <yourStsAccesskeyID>: Replace it with your AccessKey ID. <yourStsAccessKeySecret>: Replace it with your AccessKey secret. <yourStsToken>: Replace it with the security token of the AccessKey pair assigned by STS. <yourResourceGroupID>: Replace it with the actual resource set ID. <yourOrganizationID>: Replace it with the actual organization ID.

```java
public static void main(String[] args) {
    // Replace "<yourRegionID>" with the actual region ID.
    // Replace "<yourStsAccessKeyID>" and "<yourStsAccessKeySecret>" with the AccessK
ey ID and AccessKey secret of the AccessKey pair assigned by STS. The AccessKey ID an d AccessKey secret are obtained in the preceding step.
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
STS. The STS token is obtained in the preceding step.
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

`}` `}` sts

## Make API requests

### Request structure

Apsara Stack Security API operations use the RPC protocol. This topic describes the structure of API requests. You can call Apsara Stack Security API operations by sending HTTP requests. The request structure is as follows:

```
http://endpoint/?Action=xx&parameters
```

where:

|   | Endpoint |   | : The endpoin |
|---|---|---|---|
| [RegionId].example.com |   |   |   |
|   | Action | : the name of t |   |

`Endpoint` : The endpoint of the Network Traffic Monitoring System API is `secspy.` `Action` : the name of the operation being performed. For example, to query the Apsara Stack Security features that are deployed, you must set the Action parameter to DescribeFeatures. `Parameters` : the request parameters for the operation. Separate multiple parameters with ampersands (&). Request parameters include both common parameters and operationspecific parameters. Common parameters include information such as the API version number and authentication information. For more information about operation-specific parameters, see the corresponding operation description. The following example demonstrates how to call the DescribeFeatures operation to query the Apsara Stack Security features that are deployed:

```
https://secspy.[RegionId].example.com/?Action=DescribeFeatures&AccessKeyId=key-test&For mat=JSON&SecureTransport=true&SignatureMethod=HMAC- SHA1&SignatureNonce=15215528852396&SignatureVersion=1.0&SourceIp=1xxxx6&Timestamp=2019- 12-02Txxxxxxx&Version=2019-08-05&Signature=xxxx%xxxx%3D
```

API requests are presented in the following easy-to-read format in this document:

```
https://secspy.[RegionId].example.com/?Action=DescribeFeatures &Format=JSON &Version=2019-08-05 &Signature=xxxx%xxxx%3D &SignatureMethod=HMAC-SHA1 &SignatureNonce=15215528852396 &SignatureVersion=1.0 &AccessKeyId=key-test &Timestamp=2019-12-02T12:00:00Z
```

sts

### Request signatures

Apsara Stack Security authenticates each access request. Therefore, a request must contain signature information regardless of whether it is sent over HTTP or HTTPS.

**Authorization**

To ensure the security of your account, we recommend that you use a Resource Access Management (RAM) user to call API operations. Before you use a RAM user to call an API operation, you must grant the RAM user the required permissions by creating a policy and attaching the policy to the RAM user.

**Signature**

You must sign all API requests to ensure security. Alibaba Cloud uses the request signature to verify the identity of the API caller. When you manually make an API request, you must use the AccessKey secret to calculate an HMAC value based on the encoded and sorted request string. The HMAC value is the signature. For more information, see the definition in RFC 2104. This section uses the raw access parameters in the following table to describe how to create an operation signature.

| Parameter | Description |
|---|---|
| Endpoint | http://secspy.[RegionId].example.com/? |
| Operation-specific parameters | Action=DescribeFeatures |
| Common parameters except Signature | &Timestamp=2019-12-01T12:46:24Z &Format=JSON &AccessKeyId=<yourAccessKeyId> &SignatureMethod=HMAC-SHA1 &SignatureNonce=3ee8c1b8-83d3-44af-a94f-4e0ad82fd6cf &Version=2019-08-05 &SignatureVersion=1.0 |
| AccessKey secret | <yourAccessKeySecret> |

1. Create a canonicalized query string by arranging the request parameters.

**Important**

The request parameters include operation-specific parameters and all common request parameters except Signature. i. Sort the request parameters. Sort the request parameters (including all common and operation-specific parameters except **Signature**) in alphabetical order.

**Note**

If you use the GET method to send a request,these parameters are connected by ampersands (&) and included in the request URL. The first request parameter follows a question mark (?). sts ii. Encode the parameters. Encode the canonicalized query string in UTF-8 based on the following rules: Uppercase letters, lowercase letters, digits, and some special characters such as hyphens (-), underscores (_), periods (.), and tildes (~) do not need to be encoded. Other characters must be percent encoded in the %XY format. XY represents the ASCII code of the characters in hexadecimal notation. For example, double quotation marks (") are encoded as %22. Extended UTF-8 characters are encoded in the %XY%ZA… format. Spaces must be encoded as %20. Do not encode spaces as plus signs (+). iii. Connect the encoded parameter names and their values with equal signs (=). iv. Sort the parameters in the order specified in the Sort parameters step and connect them with ampersands (&) to produce a canonicalized query string.
2. Create a string-to-sign from the encoded canonicalized query string.

```
StringToSign=HTTPMethod + "&" + percentEncode("/") + "&" + percentEncode(CanonicalizedQueryString)
```

3. Calculate the HMAC value of the string-to-sign based on RFC 2104.

**Note**

Use the SHA1 algorithm to calculate the HMAC value of the string-to-sign. The AccessKey secret to which an ampersand (&) (ASCII:38) is appended is used as the key for HMAC calculation.
4. Encode the HMAC value in Base64 to obtain the signature string.

```
LEW8N4y7Uasop******
```

5. Add the signature string to the request as the Signature parameter.

### Common parameters

Common request parameters must be included in all Apsara Stack Security API requests, such as the API version number and authentication information.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Version | String | Yes | The version number of the API. The value is in the format of YYYY-MM-DD. Set the value to 2019-08-05. |
| AccessKeyId | String | Yes | The AccessKey ID provided to you by Alibaba Cloud. |
| Signature | String | Yes | The signature string of the current request. |
| SignatureMethod | String | Yes | The encryption method of the signature string. Set the value to HMAC-SHA1. |

sts

| Timestamp | String | Yes | The timestamp of the request. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC. For example, use 2019-12- 01T12:00:00Z to indicate 12:00:00, December 1, 2019 in UTC+8. |
|---|---|---|---|
| SignatureVersion | String | Yes | The version of the signature encryption algorithm. Set the value to 1.0. |
| SignatureNonce | String | Yes | A unique random number used to prevent replay attacks. You must use different numbers for different requests. |
| ResourceOwnerA ccount | String | No | The Alibaba Cloud account to which the resource you want to access belongs. |
| Format | String | No | The response format. Valid values: JSON or XML. Note Default value: XML. |

### Response structure

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

## Sample calls

### Java SDK call examples

#### User guide

##### Install the Java SDK

This topic describes how to install and use the Alibaba Cloud Security Java SDK. The Apsara Stack Java SDK supports JDK 1.8 and later. You can install the Apsara Stack Java SDK by adding a Maven dependency or by downloading the Alibaba Cloud SDK. To use the Alibaba Cloud Security SDK, you must install the Alibaba Cloud Java SDK core library. Use version 4.5.17 or later of the core library. When you install the Alibaba Cloud Java SDK core library, add the following dependency to your pom.xml file. For the exact SDK version number, see Alibaba Cloud SDK.

```xml
<!-- Alibaba Cloud SDK for Java --> <dependency>
    <groupId>com.aliyun</groupId>
    <artifactId>aliyun-java-sdk-core</artifactId>
    <version>4.5.17</version>
</dependency>
```

##### Make calls using CommonRequest

To use the POP Java SDK to call a product API, you must know whether the product uses RPC or ROA calls.

**Prerequisites**

Apsara Stack recommends that you use CommonRequest to make calls. To find the recommended SDK version and sample code, go to the Apsara Uni-manager Management Console. Choose **Product** > **Application Service** > **Developer Portal**. Then, choose **API**
**Integration** > **SDK Sample**.

**Important**

Do not download the SDK from the SDK Center for use with Apsara Stack. The public cloud SDK might not support Apsara Stack APIs. This can cause compatibility problems. Use it with caution.

**Use CommonRequest**

Alibaba Cloud product APIs use two styles: RPC and RESTful. The method for making a CommonRequest call differs for each style. APIs that include an `Action` parameter are typically RPC style, while APIs that include a `PathPattern` parameter are RESTful style. All APIs within a product usually use the same style, and each API supports only one style. If you provide the wrong identifier, you might call a different API or receive an `ApiNotFound` error message. To make a CommonRequest call, you need the following parameter values. You can find these values in the API documentation for each product in the Documentation Center or Documentation Center. For some products, you can also find API parameter information in the OpenAPI Developer Portal. Endpoint: The product's endpoint. API version (version): The API version number in YYYY-MM-DD format. API information: The name of the API to call. If the API is RPC style, such as most Alibaba Cloud Security (Sas) APIs, obtain the `Action` parameter. Use `request.ApiName = "<Action>"` to specify the API name. If the API is RESTful style, such as Container Service, obtain the `PathPattern` parameter. Use `request.PathPattern = "<PathPattern>"` to specify the RESTful path.

**Example: Call an RPC-style API**

The following code shows how to use CommonRequest to call an Alibaba Cloud Security API:

```java
import com.aliyuncs.CommonRequest; import com.aliyuncs.CommonResponse; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.exceptions.ServerException; import com.aliyuncs.profile.DefaultProfile; public class Sample {
    public static void main(String[] args) {
        // Create and initialize a DefaultAcsClient instance.
        DefaultProfile profile = DefaultProfile.getProfile(
            "<your-region-id>",          // Your region ID
            "<your-access-key-id>",      // Your AccessKey ID
            "<your-access-key-secret>"); // Your AccessKey secret
        IAcsClient client = new DefaultAcsClient(profile);
        // Create an API request and set the parameters.
        CommonRequest request = new CommonRequest();
        request.setDomain("<your-endpoint>");// The actual endpoint of the product
        request.setVersion("<API-version>");// The version of the API
        request.setAction("<your-action>");// The name of the API
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

**Example: Call a RESTful (ROA)-style API**

The following code shows how to use CommonRequest to call the Container Service API to list all cluster instances.

```java
import com.aliyuncs.CommonRequest; import com.aliyuncs.CommonResponse; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.exceptions.ServerException; import com.aliyuncs.profile.DefaultProfile; public class Sample {
    public static void main(String[] args) {
        // Create and initialize a DefaultAcsClient instance.
        DefaultProfile profile = DefaultProfile.getProfile(
                // Your region ID
                "<your-region-id>",
                // Get the AccessKey ID of the RAM user from the environment variable.
                System.getenv("ALIBABA_CLOUD_ACCESS_KEY_ID"),
                // Get the AccessKey secret of the RAM user from the environment
variable.
                System.getenv("ALIBABA_CLOUD_ACCESS_KEY_SECRET"));
        IAcsClient client = new DefaultAcsClient(profile);
        // Create an API request and set the parameters.
        CommonRequest request = new CommonRequest();
        request.setSysDomain("cs.aliyuncs.com");
        request.setSysVersion("2015-12-15");
        request.setSysUriPattern("/clusters");
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

### Python SDK call examples

#### User guide

##### Install the Python SDK

This document describes how to install and call the Python SDK. The Apsara Stack Python SDK supports Python 2.6.x, 2.7.x, and 3.x or later. You can use pip to install the SDK.

**Note**

All product SDKs require the Alibaba Cloud Python SDK core library. For Python 2.x, run the following command to install the Alibaba Cloud Python SDK core library:

```
pip install aliyun-python-sdk-core
```

For Python 3.x, run the following command to install the Alibaba Cloud Python SDK core library:

```
pip3 install aliyun-python-sdk-core-v3
```

##### Make calls using CommonRequest

This topic describes how to make calls using CommonRequest.

**Prerequisites**

For Apsara Stack, use CommonRequest to make calls. To find the recommended software development kit (SDK) versions and sample code, navigate to **Products** > **Application**
**Services** > **Developer Portal** and choose **API Integration** > **SDK Examples** in the Apsara
Uni-manager Management Console.

**Important**

Do not download SDKs directly from the SDK Center for use in Apsara Stack environments. SDKs for the public cloud may not support Apsara Stack APIs, which can cause compatibility issues.

**Use CommonRequest**

Alibaba Cloud product APIs use either the RPC or RESTful style. The method for making a CommonRequest call differs depending on the API style. Typically, an API is RPC-style if its parameters include an Action parameter. An API is RESTfulstyle if its parameters include a PathPattern parameter. Generally, all APIs for a single product use the same style. Each API supports only one style. If you use the wrong style identifier, you might call a different API or receive an `ApiNotFound` error message. To initiate a CommonRequest, you need to obtain the values of the following parameters. You can obtain the values of these parameters from the API documentation for each product in the Document CenterDocument Center. Additionally, for some products, you can also obtain API parameter information from the OpenAPI Developer Portal. Endpoint: The endpoint of the product. API version: The version number of the API. The format is YYYY-MM-DD. API information: The name of the API to call. If the API is RPC-style, which is used for most Alibaba Cloud product APIs such as Sas, obtain the Action parameter. Use `request.ApiName = "<Action>"` to specify the API name. If the API is RESTful-style, such as Container Service, obtain the PathPattern parameter. Use `request.PathPattern = "<PathPattern>"` to specify the RESTful path.

**Example: Call an RPC-style API**

The following code shows how to use CommonRequest to call an RPC-style API:

```bash
from aliyunsdkcore.client import AcsClient from aliyunsdkcore.request import CommonRequest client = AcsClient('{your_access_key_id}', '{your_access_key_secret}', '{your_region_id}') request = CommonRequest() request.set_domain('<your-endpoint>') // The actual endpoint of the product. request.set_version('<API-version>') // The version of the API. request.set_action_name('<your-action>')// The name of the API.
# or:
# request = CommonRequest(domain='<your-endpoint>', version='<API-version>',
action_name='your-action') request.add_query_param('PageNumber', '1') request.add_query_param('PageSize', '30') response = client.do_action_with_exception(request)
```

**Example: Call a RESTful (ROA)-style API**

The following code shows how to use CommonRequest to call the Container Service API to view all cluster instances:

```bash
from aliyunsdkcore.client import AcsClient from aliyunsdkcore.request import CommonRequest client = AcsClient('{your_access_key_id}', '{your_access_key_secret}', '{your_region_id}') request = CommonRequest() request.set_domain('cs.aliyuncs.com') request.set_version('2015-12-15') request.set_uri_pattern('/clusters')
# or:
# request = CommonRequest(domain='ecs.aliyuncs.com', version='2014-05-26',
uri_pattern='/clusters') response = client.do_action_with_exception(request)
```

### Go SDK call examples

#### User guide

##### Install the Go SDK core package

This document describes how to install the Go SDK core package. The Alibaba Cloud SDK for Go supports Go 1.10.x and later versions. You can run the following command to install the core package.

```
go get -u github.com/aliyun/alibaba-cloud-sdk-go/sdk
```

##### Make calls using CommonRequest

This topic describes how to make calls using CommonRequest.

**Prerequisites**

**q**

For Apsara Stack, you can use CommonRequest to make API calls. To view the recommended software development kit (SDK) versions and sample code, go to **Products** > **Application**
**Services** > **Developer Portal** in the Apsara Uni-manager Management Console. Then,
choose **API Integration** > **SDK Examples**.

**Important**

Do not download SDKs from SDK Center for use with Apsara Stack. Public cloud SDKs might not support Apsara Stack APIs, which can lead to compatibility issues.

**Using CommonRequest**

Alibaba Cloud product APIs use either the RPC or RESTful style. The method for making a CommonRequest call differs for each style. APIs that include an `Action` parameter are typically RPC-style. APIs that include a `PathPattern` parameter are RESTful-style. Within a product, all APIs usually share the same style. Each API supports only one style. If you pass an incorrect identifier, you might call the wrong API or receive an `ApiNotFound` error message. To make a CommonRequest call, obtain the values for the following parameters. You can find these values in the API documentation for each product in the Documentation Center or Documentation Center. For some products, this information is also available in the OpenAPI Developer Portal. Endpoint: The endpoint for the product. Version: The version number of the API, in YYYY-MM-DD format. API information: The name of the API to call. If the API is RPC-style, which is used for most Alibaba Cloud product APIs such as Sas, obtain the Action parameter. Use `request.ApiName = "<Action>"` to specify the API name. If the API is RESTful-style, such as for Container Service, obtain the PathPattern parameter. Use `request.PathPattern = "<PathPattern>"` to specify the RESTful path.

**Example: Use an RPC-style API**

The following code shows how to call an RPC-style API using CommonRequest:

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
    request.Domain = "<your-endpoint>"// The actual endpoint of the product.
    request.Version = "<API-version>"// The version of the API.
    request.ApiName = "<your-action>"// The name of the API.
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

**Example: Call a RESTful (ROA)-style API**

The following code shows how to use CommonRequest to call the Container Service API to retrieve all cluster instances:

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
    request.Domain = "cs.aliyuncs.com"
    request.Version = "2015-12-15"
    // Specify PathPattern because this is a RESTful API.
    request.PathPattern = "/clusters"
    response, err := client.ProcessCommonRequest(request)
    if err != nil {
        panic(err)
```

`}`

```
    fmt.Print(response.GetHttpContentString())
```

`}`

## API documentation

This is the API reference content

### Traffic trend

#### DescribeNtaTrafficTrend

Queries the network traffic trend.

**Authorization information**

| Operation | Access level | Resource type |
|---|---|---|
| yundun- cloudfirewall:DescribeNtaTraffic Trend | Read | acs:yundun-cloudfirewall:*: {#accountId}:* |

**Throttling**

You can call this operation up to 100 times per second per account. You can call this operation up to 200 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Lang | Strin g | Query | No | zh | The language. Valid values: zh and en. You can leave this parameter empty if it is not required for your business. |
| AliUid | Strin g | Query | No | 1234567890 | The user ID. |
| StartTime | Strin g | Query | No | 1525833105 | The beginning of the time range to query. |
| EndTime | Strin g | Query | No | 1525833105 | The end of the time range to query. |
| Direction | Strin g | Query | No | in | The traffic direction. Valid values: in and out. |

| i | Developer Gui on | de·API d | ocumentat |   | Cloud | Security Network Detecti n and Respons | o e |
|---|---|---|---|---|---|---|---|

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| SrcPublicI P | Strin g | Query | No | 1.1.1.1 | The source IP address. |
| DstPublicI P | Strin g | Query | No | 1.1.1.1 | The destination IP address. |
| NetType | Strin g | Query | No | isw | The network type. Valid values: isw and csw. |
| VpcId | Strin g | Query | No | vpc-test**** | The virtual private cloud (VPC) ID. This parameter is required when NetType is set to csw. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| DataList | Array |   |   |
| -InBps | Integer | 10 | The inbound bytes per second (BPS). |
| -Time | Integer | 1525833105 | The point in time of the query. |
| -OutBps | Integer | 10 | The outbound BPS. |
| -InPps | Integer | 10 | The inbound packets per second (PPS). |
| -OutPps | Integer | 10 | The outbound PPS. |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| MaxInBps | Integer | 100 | The maximum inbound BPS. |
| MaxOutBps | Integer | 100 | The maximum outbound BPS. |
| AvgInBps | Integer | 10 | The average inbound BPS. |
| AvgOutBps | Integer | 10 | The average outbound BPS. |

| Cloud Security Ne | twork Detectio |   | Developer Guide·API documenta |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| Module | String | ndr*** | The name of the module. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=DescribeNtaTrafficTrend&RegionId=cnhangzhou&Lang=zh&AliUid=1234567890&StartTime=1525833105&EndTime=1525833105&Direction=in&S PublicIP=1.1.1.1&DstPublicIP=1.1.1.1&NetType=isw&VpcId=vpc-test****
```

Sample success responses `JSON` format

```
Content-Type:application/json
```

`{`

```json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "DataList":[
```

`{`

```json
            "OutPps":10,
            "OutBps":10,
            "InBps":10,
            "InPps":10,
            "Time":1525833105
```

`}` `],`

```json
    "MaxInBps":100,
    "MaxOutBps":100,
    "AvgInBps":10,
    "AvgOutBps":10,
    "Module":"ndr***"
```

`}` `XML` format

```xml
Content-Type:application/xml <DescribeNtaTrafficTrendResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <DataList>
        <InBps>10</InBps>
        <Time>1525833105</Time>
        <OutBps>10</OutBps>
        <InPps>10</InPps>
        <OutPps>10</OutPps>
    </DataList>
    <MaxInBps>100</MaxInBps>
    <MaxOutBps>100</MaxOutBps>
    <AvgInBps>10</AvgInBps>
    <AvgOutBps>10</AvgOutBps>
    <Module>ndr***</Module>
</DescribeNtaTrafficTrendResponse>
```

#### DescribeNtaTrafficTopInfo

Queries the top N resources that have the largest amount of traffic.

**Authorization information**

| Operation | Access level | Resource type |
|---|---|---|
| yundun- cloudfirewall:DescribeNtaTraffic TopInfo | Read | acs:yundun-cloudfirewall:*: {#accountId}:* |

**Throttling**

You can call this operation up to 100 times per second per account. You can call this operation up to 200 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Lang | Strin g | Query | No | zh | The language. Valid values: zh and en. You can leave this parameter empty if it is not required for your business. |

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Direction | Strin g | Query | No | in | The traffic direction. Valid values: in and out. |
| Sort | Strin g | Query | No | total bytes _ | The sorting method. Valid values: in bytes, _ out bytes, total bytes, _ _ in packets, out packets, _ _ and session count. _ |
| DataType | Strin g | Query | No | in dst ip _ _ | The data type. Valid values of the inbound traffic: in dst ip, _ _ in top app, and _ _ in top session. Valid _ _ values of the outbound traffic: out src ip, _ _ out top app, _ _ out top session. _ _ |
| StartTime | Strin g | Query | No | 1525833105 | The beginning of the time range to query. |
| EndTime | Strin g | Query | No | 1525833105 | The end of the time range to query. |
| Limit | Strin g | Query | No | 5 | The top N resources to be returned. Default value: 5. Valid values: 1 to 10. |
| NetType | Strin g | Query | No | isw | The network type. Valid values: isw and csw. |
| AliUid | Strin g | Query | No | 1234567890 | The user ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| DataList | Array |   |   |
| -DataValue | String | 95 | The percentage of total traffic attributed to the top N resources. |

| Developer Guide·A on | PI documentat |   | Cloud Security Network Detecti n and Respons |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| -DataName | String | 1.1.1.1 | The identifier of the resources for which traffic statistics are provided. The value can be an IP address or an application name. |
| -TotalBytes | Integer | 100 | The total amount of traffic. Unit: bytes. |
| -SessionCount | Integer | 100 | The number of sessions. |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| DataCount | Integer | 10 | The number of rows returned. |
| DataType | String | in dst ip _ _ | The statistical dimension. |
| Module | String | ndr*** | The name of the module. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=DescribeNtaTrafficTopInfo&RegionId=cnhangzhou&Lang=zh&Direction=in&Sort=total_bytes&DataType=in_dst_ip&StartTime=1525833105&En ime=1525833105&Limit=5&NetType=isw&AliUid=1234567890
```

Sample success responses `JSON` format

```
Content-Type:application/json
```

`{`

```json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "DataList":[
```

`{`

```json
            "DataValue":"95",
            "TotalBytes":100,
            "SessionCount":100,
            "DataName":"1.1.1.1"
```

`}` `],`

```json
    "DataCount":10,
    "DataType":"in_dst_ip",
    "Module":"ndr***"
```

`}` `XML` format

```xml
Content-Type:application/xml <DescribeNtaTrafficTopInfoResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <DataList>
        <DataValue>95</DataValue>
        <DataName>1.1.1.1</DataName>
        <TotalBytes>100</TotalBytes>
        <SessionCount>100</SessionCount>
    </DataList>
    <DataCount>10</DataCount>
    <DataType>in_dst_ip</DataType>
    <Module>ndr***</Module>
</DescribeNtaTrafficTopInfoResponse>
```

### Network traffic analysis

#### DescribeNtaTrafficListByIp

Queries network traffic information by IP address.

**Authorization information**

| Operation | Access level | Resource type |
|---|---|---|
| yundun- cloudfirewall:DescribeNtaTraffic ListByIp | Read | acs:yundun-cloudfirewall:*: {#accountId}:* |

**Throttling**

You can call this operation up to 200 times per second per account. You can call this operation up to 200 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Lang | Strin g | Query | No | zh | The language. Valid values: zh and en. You can leave this parameter empty if it is not required for your business. |

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Direction | Strin g | Query | No | in | The traffic direction. Valid values: in and out. |
| StartTime | Strin g | Query | No | 1525833105 | The beginning of the time range to query. |
| EndTime | Strin g | Query | No | 1525833105 | The end of the time range to query. |
| SrcIp | Strin g | Query | No | 1.1.1.1 | The source IP address. |
| DstIp | Strin g | Query | No | 1.1.1.1 | The destination IP address. |
| AliUid | Strin g | Query | No | 1234567890 | The user ID. |
| CurrentPa ge | Strin g | Query | No | 1 | The page number. |
| PageSize | Strin g | Query | No | 10 | The number of entries per page. |
| DataType | Strin g | Query | Yes | src ip statistic _ _ | The statistical dimension. A value of src ip statistic indicates _ _ that the network traffic is queried by source IP address. A value of dst ip statistic indicates _ _ that the network traffic is queried by destination IP address. |
| NetType | Strin g | Query | No | isw | The network type. Valid values: isw and csw. |
| Sort | Strin g | Query | No | total bytes _ | The sorting method. Valid values: total bytes, _ session count, _ sip count, and _ dip count. _ |

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| VpcId | Strin g | Query | No | vpc-test**** | The virtual private cloud (VPC) ID. This parameter is required when NetType is set to csw. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| DataList | Array |   |   |
| -QueryIp | String | 1.1.1.1 | The IP address. |
| -IpLoc | String | Beijing | The geographical location. |
| -TrafficBps | String | 100 | The amount of traffic. Unit: BPS. |
| -SessionCount | String | 100 | The number of session rows. |
| -PortCount | String | 100 | The number of ports. |
| -VisitIpCount | String | 100 | The total number of accessed IP addresses. |
| -AppCount | String | 100 | The number of applications. |
| -StartTime | Integer | 1525833105 | The beginning of the time range to query. |
| -EndTime | Integer | 1525833105 | The end of the time range to query. |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| TotalCount | Integer | 100 | The total number of entries returned. |
| Module | String | ndr*** | The name of the module. |
| PageInfo | Struct |   |   |
| -PageSize | Integer | 10 | The number of entries per page. |

| i | Developer Guide·A on | PI documentat |   | Cloud Security Network Detecti n and Respons | o e |
|---|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| -CurrentPage | Integer | 1 | The page number. |
| -TotalCount | Integer | 100 | The total number of entries returned. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=DescribeNtaTrafficListByIp&RegionId=cnhangzhou&Lang=zh&Direction=in&StartTime=1525833105&EndTime=1525833105&SrcIp=1.1.1.1&DstIp .1.1.1&AliUid=1234567890&CurrentPage=1&PageSize=10&DataType=src_ip_statistic&NetType=isw& rt=total_bytes&VpcId=vpc-test****
```

Sample success responses `JSON` format

```
Content-Type:application/json
```

`{`

```json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "DataList":[
```

`{`

```json
            "IpLoc":"Beijing",
            "VisitIpCount":"100",
            "EndTime":1525833105,
            "AppCount":"100",
            "StartTime":1525833105,
            "QueryIp":"1.1.1.1",
            "TrafficBps":"100",
            "PortCount":"100",
            "SessionCount":"100"
```

`}` `],`

```json
    "TotalCount":100,
    "PageInfo":{
        "TotalCount":100,
        "PageSize":10,
        "CurrentPage":1
```

`},`

```json
    "Module":"ndr***"
```

`}` `XML` format

```xml
Content-Type:application/xml <DescribeNtaTrafficListByIpResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <DataList>
        <QueryIp>1.1.1.1</QueryIp>
        <IpLoc>Beijing</IpLoc>
        <TrafficBps>100</TrafficBps>
        <SessionCount>100</SessionCount>
        <PortCount>100</PortCount>
        <VisitIpCount>100</VisitIpCount>
        <AppCount>100</AppCount>
        <StartTime>1525833105</StartTime>
        <EndTime>1525833105</EndTime>
    </DataList>
    <TotalCount>100</TotalCount>
    <PageInfo>
        <PageSize>10</PageSize>
        <CurrentPage>1</CurrentPage>
        <TotalCount>100</TotalCount>
    </PageInfo>
    <Module>ndr***</Module>
</DescribeNtaTrafficListByIpResponse>
```

#### DescribeVpcInfoByUid

Queries virtual private cloud (VPC) information by user ID.

**Authorization information**

| Operation | Access level | Resource type |
|---|---|---|
| yundun- cloudfirewall:DescribeVpcInfoBy Uid | Read | acs:yundun-cloudfirewall:*: {#accountId}:* |

**Throttling**

You can call this operation up to 10 times per second per account. You can call this operation up to 100 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Lang | Strin g | Query | No | zh | The language. Valid values: zh and en. You can leave this parameter empty if it is not required for your business. |
| AliUid | Strin g | Query | No | 1234567890 | The user ID. |
| CurrentPa ge | Strin g | Query | No | 1 | The page number. |
| PageSize | Strin g | Query | No | 10 | The number of entries per page. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| DataList | Array |   |   |
| -VpcId | String | vpc-test**** | The VPC ID. |
| -VpcName | String | vpc-test**** | The name of the VPC. |
| -AliUid | String | 1234567890 | The user ID. |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Module | String | ndr*** | The name of the module. |
| PageInfo | Struct |   |   |
| -PageSize | Integer | 10 | The number of entries per page. |
| -CurrentPage | Integer | 1 | The page number. |
| -TotalCount | Integer | 100 | The total number of entries returned. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=DescribeVpcInfoByUid&RegionId=cnhangzhou&Lang=zh&AliUid=1234567890&CurrentPage=1&PageSize=10
```

Sample success responses `JSON` format

```
Content-Type:application/json
```

`{`

```json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "DataList":[
```

`{`

```json
            "VpcId":"vpc-test****",
            "VpcName":"vpc-test****",
            "AliUid":"1234567890"
```

`}` `],`

```json
    "PageInfo":{
        "TotalCount":100,
        "PageSize":10,
        "CurrentPage":1
```

`},`

```json
    "Module":"ndr***"
```

`}` `XML` format

```xml
Content-Type:application/xml <DescribeVpcInfoByUidResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <DataList>
        <VpcId>vpc-test****</VpcId>
        <VpcName>vpc-test****</VpcName>
        <AliUid>1234567890</AliUid>
    </DataList>
    <PageInfo>
        <PageSize>10</PageSize>
        <CurrentPage>1</CurrentPage>
        <TotalCount>100</TotalCount>
    </PageInfo>
    <Module>ndr***</Module>
</DescribeVpcInfoByUidResponse>
```

#### DescribeNtaTrafficStatisticsByUid

Queries network traffic statistics by user ID.

**Authorization information**

| Operation | Access level | Resource type |
|---|---|---|
| yundun- cloudfirewall:DescribeNtaTraffic StatisticsByUid | Read | acs:yundun-cloudfirewall:*: {#accountId}:* |

**Throttling**

You can call this operation up to 100 times per second per account. You can call this operation up to 200 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Lang | Strin g | Query | No | zh | The language. Valid values: zh and en. You can leave this parameter empty if it is not required for your business. |
| Direction | Strin g | Query | No | in | The traffic direction. Valid values: in and out. |
| StartTime | Strin g | Query | No | 1525833105 | The beginning of the time range to query. |
| EndTime | Strin g | Query | No | 1525833105 | The end of the time range to query. |
| AliUid | Strin g | Query | No | 1234567890 | The user ID. |
| NetType | Strin g | Query | No | isw | The network type. Valid values: isw and csw. |
| VpcId | Strin g | Query | No | vpc-test**** | The virtual private cloud (VPC) ID. This parameter is required when NetType is set to csw. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| SipCount | Integer | 100 | The number of source IP addresses. |
| DipCount | Integer | 100 | The number of destination IP addresses. |
| AppCount | Integer | 100 | The number of applications. |
| SessionCount | Integer | 100 | The number of sessions. |
| AttackCount | Integer | 100 | The number of attacks. |
| Module | String | ndr*** | The name of the module. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=DescribeNtaTrafficStatisticsByUid&RegionId=cnhangzhou&Lang=zh&Direction=in&StartTime=1525833105&EndTime=1525833105&AliUid=1234567890&N Type=isw&VpcId=vpc-test****
```

Sample success responses `JSON` format

```
Content-Type:application/json
```

`{`

```json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "SipCount":100,
    "DipCount":100,
    "AppCount":100,
    "SessionCount":100,
    "AttackCount":100,
    "Module":"ndr***"
```

`}` `XML` format

```xml
Content-Type:application/xml <DescribeNtaTrafficStatisticsByUidResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <SipCount>100</SipCount>
    <DipCount>100</DipCount>
    <AppCount>100</AppCount>
    <SessionCount>100</SessionCount>
    <AttackCount>100</AttackCount>
    <Module>ndr***</Module>
</DescribeNtaTrafficStatisticsByUidResponse>
```

#### DescribeSessionByApp

Queries the session information about an application.

**Authorization information**

| Operation | Access level | Resource type |
|---|---|---|
| yundun- cloudfirewall:DescribeSessionB yApp | Read | acs:yundun-cloudfirewall:*: {#accountId}:* |

**Throttling**

You can call this operation up to 100 times per second per account. You can call this operation up to 200 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Lang | Strin g | Query | No | zh | The language. Valid values: zh and en. You can leave this parameter empty if it is not required for your business. |
| Direction | Strin g | Query | No | in | The traffic direction. Valid values: in and out. |

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| StartTime | Strin g | Query | No | 1525833105 | The beginning of the time range to query. |
| EndTime | Strin g | Query | No | 1525833105 | The end of the time range to query. |
| AliUid | Strin g | Query | No | 1234567890 | The user ID. |
| App | Strin g | Query | No | HTTP | The name of the application. |
| NetType | Strin g | Query | No | isw | The network type. Valid values: isw and csw. |
| Sort | Strin g | Query | No | total packet bytes _ _ | The sorting method. Valid values: total packet bytes and _ _ total packet count. _ _ |
| CurrentPa ge | Strin g | Query | No | 1 | The page number. |
| PageSize | Strin g | Query | No | 10 | The number of entries per page. |
| SrcPort | Strin g | Query | No | 65534 | The source port. |
| DstPort | Strin g | Query | No | 8080 | The destination port. |
| VpcId | Strin g | Query | No | vpc-test**** | The virtual private cloud (VPC) ID. This parameter is required when NetType is set to csw. |
| Lang | Strin g | Query | No | zh | The language. Valid values: zh and en. You can leave this parameter empty if it is not required for your business. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| DataList | Array |   |   |
| -StartTime | Integer | 1525833105 | The start time of the session. |
| -SrcIp | String | 1.1.1.1 | The source IP address. |
| -Loction | String | Beijing | The geographical location of the source IP address. |
| -SrcPort | Integer | 80 | The source port. |
| -DstIp | String | 1.1.1.1 | The destination IP address. |
| -DstLoc | String | Beijing | The geographical location of the destination IP address. |
| -DstPort | Integer | 80 | The destination port. |
| -App | String | HTTP | The name of the application. |
| -PktCount | Integer | 10 | The number of session packets. |
| -TrafficBps | Integer | 10 | The amount of traffic. |
| -Duration | Integer | 10 | The duration of the session. Unit: seconds. |
| -AttackType | String |   | The attack type. No data is returned. |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| TotalCount | Integer | 100 | The total number of entries returned. |
| Module | String | ndr*** | The name of the module. |
| PageInfo | Struct |   |   |
| -PageSize | Integer | 10 | The number of entries per page. |

| Cloud Security Ne | twork Detectio |   | Developer Guide·API documenta |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| -CurrentPage | Integer | 1 | The page number. |
| -TotalCount | Integer | 100 | The total number of entries returned. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=DescribeSessionByApp&RegionId=cnhangzhou&Lang=zh&Direction=in&StartTime=1525833105&EndTime=1525833105&AliUid=1234567890&A =HTTP&NetType=isw&Sort=total_packet_bytes&CurrentPage=1&PageSize=10&SrcPort=65534&DstPort 080&VpcId=vpc-test****&Lang=zh
```

Sample success responses `JSON` format

```
Content-Type:application/json
```

`{`

```json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "DataList":[
```

`{`

```json
            "App":"HTTP",
            "SrcPort":80,
            "StartTime":1525833105,
            "Loction":"Beijing",
            "DstIp":"1.1.1.1",
            "DstLoc":"Beijing",
            "PktCount":10,
            "Duration":10,
            "AttackType":"",
            "DstPort":80,
            "TrafficBps":10,
            "SrcIp":"1.1.1.1"
```

`}` `],`

```json
    "TotalCount":100,
    "PageInfo":{
        "TotalCount":100,
        "PageSize":10,
        "CurrentPage":1
```

`},`

```json
    "Module":"ndr***"
```

`}` `XML` format

```xml
Content-Type:application/xml <DescribeSessionByAppResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <DataList>
        <StartTime>1525833105</StartTime>
        <SrcIp>1.1.1.1</SrcIp>
        <Loction>Beijing</Loction>
        <SrcPort>80</SrcPort>
        <DstIp>1.1.1.1</DstIp>
        <DstLoc>Beijing</DstLoc>
        <DstPort>80</DstPort>
        <App>HTTP</App>
        <PktCount>10</PktCount>
        <TrafficBps>10</TrafficBps>
        <Duration>10</Duration>
        <AttackType></AttackType>
    </DataList>
    <TotalCount>100</TotalCount>
    <PageInfo>
        <PageSize>10</PageSize>
        <CurrentPage>1</CurrentPage>
        <TotalCount>100</TotalCount>
    </PageInfo>
    <Module>ndr***</Module>
</DescribeSessionByAppResponse>
```

#### DescribeNtaTrafficListByApp

Queries network traffic statistics by application.

**Authorization information**

| Operation | Access level | Resource type |
|---|---|---|
| yundun- cloudfirewall:DescribeNtaTraffic ListByApp | Read | acs:yundun-cloudfirewall:*: {#accountId}:* |

**Throttling**

You can call this operation up to 100 times per second per account. You can call this operation up to 200 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Lang | Strin g | Query | No | zh | The language. Valid values: zh and en. You can leave this parameter empty if it is not required for your business. |
| Direction | Strin g | Query | No | in | The traffic direction. Valid values: in and out. |
| StartTime | Strin g | Query | No | 1525833105 | The beginning of the time range to query. |
| EndTime | Strin g | Query | No | 1525833105 | The end of the time range to query. |
| AliUid | Strin g | Query | No | 1234567890 | The user ID. |
| App | Strin g | Query | No | HTTP | The name of the application. |
| NetType | Strin g | Query | No | isw | The network type. Valid values: isw and csw. |
| Sort | Strin g | Query | No | total bytes _ | The sorting method. Valid values: total bytes, _ session count, _ sip count, and _ dip count. _ |
| CurrentPa ge | Strin g | Query | No | 1 | The page number. |
| PageSize | Strin g | Query | No | 10 | The number of entries per page. |
| VpcId | Strin g | Query | No | vpc-test**** | The virtual private cloud (VPC) ID. This parameter is required when NetType is set to csw. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| DataList | Array |   |   |
| -App | String | HTTP | The name of the application. |
| -Proto | String | 3234 | The agreement number. |
| -SipCount | String | 100 | The number of source IP addresses. |
| -DipCount | String | 100 | The number of destination IP addresses. |
| -SessionCount | String | 100 | The number of sessions. |
| -TrafficBps | String | 100 | The amount of traffic. Unit: BPS. |
| -StartTime | Integer | 1525833105 | The beginning of the time range to query. |
| -EndTime | Integer | 1525833105 | The end of the time range to query. |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| TotalCount | Integer | 100 | The total number of entries returned. |
| Module | String | ndr*** | The name of the module. |
| PageInfo | Struct |   |   |
| -PageSize | Integer | 10 | The number of entries per page. |
| -CurrentPage | Integer | 1 | The page number. |
| -TotalCount | Integer | 100 | The total number of entries returned. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=DescribeNtaTrafficListByApp&RegionId=cnhangzhou&Lang=zh&Direction=in&StartTime=1525833105&EndTime=1525833105&AliUid=1234567890&A =HTTP&NetType=isw&Sort=total_bytes&CurrentPage=1&PageSize=10&VpcId=vpc-test****
```

Sample success responses `JSON` format

```
Content-Type:application/json
```

`{`

```json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "DataList":[
```

`{`

```json
            "App":"HTTP",
            "Proto":"3234",
            "EndTime":1525833105,
            "DipCount":"100",
            "SipCount":"100",
            "StartTime":1525833105,
            "TrafficBps":"100",
            "SessionCount":"100"
```

`}` `],`

```json
    "TotalCount":100,
    "PageInfo":{
        "TotalCount":100,
        "PageSize":10,
        "CurrentPage":1
```

`},`

```json
    "Module":"ndr***"
```

`}` `XML` format

```xml
Content-Type:application/xml <DescribeNtaTrafficListByAppResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <DataList>
        <App>HTTP</App>
        <Proto>3234</Proto>
        <SipCount>100</SipCount>
        <DipCount>100</DipCount>
        <SessionCount>100</SessionCount>
        <TrafficBps>100</TrafficBps>
        <StartTime>1525833105</StartTime>
        <EndTime>1525833105</EndTime>
    </DataList>
    <TotalCount>100</TotalCount>
    <PageInfo>
        <PageSize>10</PageSize>
        <CurrentPage>1</CurrentPage>
        <TotalCount>100</TotalCount>
    </PageInfo>
    <Module>ndr***</Module>
</DescribeNtaTrafficListByAppResponse>
```

#### DescribeIncAppInfo

Queries the information about new applications.

**Authorization information**

| Operation | Access level | Resource type |
|---|---|---|
| yundun- cloudfirewall:DescribeIncAppInf o | Read | acs:yundun-cloudfirewall:*: {#accountId}:* |

**Throttling**

You can call this operation up to 10 times per second per account. You can call this operation up to 100 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Lang | Strin g | Query | No | zh | The language. Valid values: zh and en. You can leave this parameter empty if it is not required for your business. |
| Direction | Strin g | Query | No | in | The traffic direction. Valid values: in and out. |
| StartTime | Strin g | Query | No | 1525833105 | The beginning of the time range to query. |
| EndTime | Strin g | Query | No | 1525833105 | The end of the time range to query. |
| AliUid | Strin g | Query | No | 1234567890 | The user ID. |
| NetType | Strin g | Query | No | isw | The network type. Valid values: isw and csw. |
| VpcId | Strin g | Query | No | vpc-test**** | The virtual private cloud (VPC) ID. This parameter is required when NetType is set to csw. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| IncCount | Integer | 3 | The number of new applications. |
| AliUid | String | 1234567890 | The user ID. |
| Module | String | ndr*** | The name of the module. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=DescribeIncAppInfo&RegionId=cnhangzhou&Lang=zh&Direction=in&StartTime=1525833105&EndTime=1525833105&AliUid=1234567890&N Type=isw&VpcId=vpc-test****
```

Sample success responses `JSON` format

```
Content-Type:application/json
```

`{`

```json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "IncCount":3,
    "AliUid":"1234567890",
    "Module":"ndr***"
```

`}` `XML` format

```xml
Content-Type:application/xml <DescribeIncAppInfoResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <IncCount>3</IncCount>
    <AliUid>1234567890</AliUid>
    <Module>ndr***</Module>
</DescribeIncAppInfoResponse>
```

#### DescribeEcsByIp

Queries the Elastic Compute Service (ECS) asset information by IP address.

**Authorization information**

| Operation | Access level | Resource type |
|---|---|---|
| yundun- cloudfirewall:DescribeEcsByIp | Read | acs:yundun-cloudfirewall:*: {#accountId}:* |

**Throttling**

You can call this operation up to 10 times per second per account. You can call this operation up to 100 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Lang | Strin g | Query | No | zh | The language. Valid values: zh and en. You can leave this parameter empty if it is not required for your business. |
| QueryIp | Strin g | Query | No | 1.1.1.1 | The IP address. |
| StartTime | Strin g | Query | No | 1525833105 | The beginning of the time range to query. |
| EndTime | Strin g | Query | No | 1525833105 | The end of the time range to query. |
| AliUid | Strin g | Query | No | 1234567890 | The user ID. |
| NetType | Strin g | Query | No | isw | The network type. Valid values: isw and csw. |
| CurrentPa ge | Strin g | Query | No | 1 | The page number. |
| PageSize | Strin g | Query | No | 10 | The number of entries per page. |
| VpcId | Strin g | Query | No | vpc-test**** | The virtual private cloud (VPC) ID. This parameter is required when NetType is set to csw. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| DataList | Array | ... | The response parameters. |
| -PrivateIp | String | 192.167.*.* | The private IP address. |
| -InstanceId | String | i-test*** | The ECS instance ID. |
| - InstanceName | String | test linux 9 0 x86 _ _ _ _ 64 20G ***** _ _ _ | The name of the ECS instance. |

| i | Developer Guide·A on | PI documentat |   | Cloud Security Network Detecti n and Respons | o e |
|---|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| - InstanceStatus | String | Running | The status of the ECS instance. |
| -DeptName | String | test | The name of the department. |
| -Uuid | String | f819af20-c094- 4a48-98e1-******** | The ECS instance UUID. |
| -CreateTime | String | test | The time when the ECS instance was created. |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| TotalCount | Integer | 100 | The total number of entries returned. |
| Module | String | ndr*** | The name of the module. |
| PageInfo | Struct | ... | The pagination details. |
| -PageSize | Integer | 10 | The number of entries per page. |
| -CurrentPage | Integer | 1 | The page number. |
| -TotalCount | Integer | 100 | The total number of entries returned. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=DescribeEcsByIp&RegionId=cnhangzhou&Lang=zh&QueryIp=1.1.1.1&StartTime=1525833105&EndTime=1525833105&AliUid=123456789 NetType=isw&CurrentPage=1&PageSize=10&VpcId=vpc-test****
```

Sample success responses `JSON` format

```
Content-Type:application/json
```

`{`

```json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "DataList":[
```

`{`

```json
            "InstanceName":"test_linux_9_0_x86_64_20G_*****",
            "Uuid":"f819af20-c094-4a48-98e1-********",
            "PrivateIp":"192.167.*.*",
            "InstanceId":"i-test***",
            "InstanceStatus":"Running",
            "CreateTime":"test",
            "DeptName":"test"
```

`}` `],`

```json
    "TotalCount":100,
    "PageInfo":{
        "TotalCount":100,
        "PageSize":10,
        "CurrentPage":1
```

`},`

```json
    "Module":"ndr***"
```

`}` `XML` format

```xml
Content-Type:application/xml <DescribeEcsByIpResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <DataList>
        <PrivateIp>192.167.*.*</PrivateIp>
        <InstanceId>i-test***</InstanceId>
        <InstanceName>test_linux_9_0_x86_64_20G_*****</InstanceName>
        <InstanceStatus>Running</InstanceStatus>
        <DeptName>test</DeptName>
        <Uuid>f819af20-c094-4a48-98e1-********</Uuid>
        <CreateTime>test</CreateTime>
    </DataList>
    <TotalCount>100</TotalCount>
    <PageInfo>
        <PageSize>10</PageSize>
        <CurrentPage>1</CurrentPage>
        <TotalCount>100</TotalCount>
    </PageInfo>
    <Module>ndr***</Module>
</DescribeEcsByIpResponse>
```

#### DescribeAssetByIp

Queries asset information by IP address.

**Authorization information**

| Operation | Access level | Resource type |
|---|---|---|
| yundun- cloudfirewall:DescribeAssetByIp | Read | acs:yundun-cloudfirewall:*: {#accountId}:* |

**Throttling**

You can call this operation up to 10 times per second per account. You can call this operation up to 100 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Lang | Strin g | Query | No | zh | The language. Valid values: zh and en. You can leave this parameter empty if it is not required for your business. |
| QueryIp | Strin g | Query | No | 1.1.1.1 | The IP address. |
| StartTime | Strin g | Query | No | 1525833105 | The beginning of the time range to query. |
| EndTime | Strin g | Query | No | 1525833105 | The end of the time range to query. |
| AliUid | Strin g | Query | No | 1234567890 | The user ID. |
| NetType | Strin g | Query | No | isw | The network type. Valid values: isw and csw. |
| VpcId | Strin g | Query | No | vpc-test**** | The virtual private cloud (VPC) ID. This parameter is required when NetType is set to csw. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Type | String | ecs | The type of the asset. Valid values: ecs, eip, and slb. |
| InstanceId | String | i-test*** | The instance ID. |
| RegionId | String | region-test | The region ID. |
| DeptName | String | test | The name of the department. |
| InstanceStatus | String | in use _ | The status of the instance. |
| Status | String | in use _ | The status of the instance. |
| BandWidth | Integer | 10 | The bandwidth. |
| Module | String | ndr*** | The name of the module. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=DescribeAssetByIp&RegionId=cnhangzhou&Lang=zh&QueryIp=1.1.1.1&StartTime=1525833105&EndTime=1525833105&AliUid=123456789 NetType=isw&VpcId=vpc-test****
```

Sample success responses `JSON` format

```
Content-Type:application/json
```

`{`

```json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "Type":"ecs",
    "InstanceId":"i-test***",
    "RegionId":"region-test",
    "DeptName":"test",
    "InstanceStatus":"in_use",
    "Status":"in_use",
    "BandWidth":10,
    "Module":"ndr***"
```

`}` `XML` format

```xml
Content-Type:application/xml <DescribeAssetByIpResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <Type>ecs</Type>
    <InstanceId>i-test***</InstanceId>
    <RegionId>region-test</RegionId>
    <DeptName>test</DeptName>
    <InstanceStatus>in_use</InstanceStatus>
    <Status>in_use</Status>
    <BandWidth>10</BandWidth>
    <Module>ndr***</Module>
</DescribeAssetByIpResponse>
```

#### DescribeNtaAppTrend

Queries the traffic trend of an application.

**Authorization information**

| Operation | Access level | Resource type |
|---|---|---|
| yundun- cloudfirewall:DescribeNtaAppTr end | Read | acs:yundun-cloudfirewall:*: {#accountId}:* |

**Throttling**

You can call this operation up to 100 times per second per account. You can call this operation up to 200 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Lang | Strin g | Query | No | zh | The language. Valid values: zh and en. You can leave this parameter empty if it is not required for your business. |
| Direction | Strin g | Query | No | in | The traffic direction. Valid values: in and out. |
| StartTime | Strin g | Query | No | 1525833105 | The beginning of the time range to query. |
| EndTime | Strin g | Query | No | 1525833105 | The end of the time range to query. |
| App | Strin g | Query | No | HTTP | The name of the application. |
| AliUid | Strin g | Query | No | 1234567890 | The user ID. |
| NetType | Strin g | Query | No | isw | The network type. Valid values: isw and csw. |
| VpcId | Strin g | Query | No | vpc-test**** | The virtual private cloud (VPC) ID. This parameter is required when NetType is set to csw. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| DataList | Array |   |   |
| -InBps | Integer | 10 | The inbound bytes per second (BPS). |
| -Time | Integer | 1525833105 | The point in time of the query. |
| -OutBps | Integer | 10 | The outbound BPS. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| -InPps | Integer | 10 | The inbound packets per second (PPS). |
| -OutPps | Integer | 10 | The outbound PPS. |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| MaxInBps | Integer | 100 | The maximum inbound BPS. |
| MaxOutBps | Integer | 100 | The maximum outbound BPS. |
| AvgInBps | Integer | 10 | The average inbound BPS. |
| AvgOutBps | Integer | 10 | The average outbound BPS. |
| Module | String | ndr*** | The name of the module. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=DescribeNtaAppTrend&RegionId=cnhangzhou&Lang=zh&Direction=in&StartTime=1525833105&EndTime=1525833105&App=HTTP&AliUid=123 67890&NetType=isw&VpcId=vpc-test****
```

Sample success responses `JSON` format

```
Content-Type:application/json
```

`{`

```json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "DataList":[
```

`{`

```json
            "OutPps":10,
            "OutBps":10,
            "InBps":10,
            "InPps":10,
            "Time":1525833105
```

`}` `],`

```json
    "MaxInBps":100,
    "MaxOutBps":100,
    "AvgInBps":10,
    "AvgOutBps":10,
    "Module":"ndr***"
```

`}` `XML` format

```xml
Content-Type:application/xml <DescribeNtaAppTrendResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <DataList>
        <InBps>10</InBps>
        <Time>1525833105</Time>
        <OutBps>10</OutBps>
        <InPps>10</InPps>
        <OutPps>10</OutPps>
    </DataList>
    <MaxInBps>100</MaxInBps>
    <MaxOutBps>100</MaxOutBps>
    <AvgInBps>10</AvgInBps>
    <AvgOutBps>10</AvgOutBps>
    <Module>ndr***</Module>
</DescribeNtaAppTrendResponse>
```

#### DescribeSessionByIp

Queries the session information by IP address.

**Authorization information**

| Operation | Access level | Resource type |
|---|---|---|
| yundun- cloudfirewall:DescribeSessionB yIp | Read | acs:yundun-cloudfirewall:*: {#accountId}:* |

**Throttling**

You can call this operation up to 100 times per second per account. You can call this operation up to 200 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Lang | Strin g | Query | No | zh | The language. Valid values: zh and en. You can leave this parameter empty if it is not required for your business. |
| Direction | Strin g | Query | No | in | The traffic direction. Valid values: in and out. |
| StartTime | Strin g | Query | No | 1525833105 | The beginning of the time range to query. |
| EndTime | Strin g | Query | No | 1525833105 | The end of the time range to query. |
| AliUid | Strin g | Query | No | 1234567890 | The user ID. |
| SrcIp | Strin g | Query | No | 1.1.1.1 | The source IP address. |
| DstIp | Strin g | Query | No | 1.1.1.1 | The destination IP address. |
| NetType | Strin g | Query | No | isw | The network type. Valid values: isw and csw. |

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Sort | Strin g | Query | No | total packet bytes _ _ | The sorting method. Valid values: total packet bytes and _ _ total packet count. _ _ |
| App | Strin g | Query | No | HTTP | The name of the application. |
| CurrentPa ge | Strin g | Query | No | 1 | The page number. |
| PageSize | Strin g | Query | No | 10 | The number of entries per page. |
| SrcPort | Strin g | Query | No | 65534 | The source port. |
| DstPort | Strin g | Query | No | 8080 | The destination port. |
| VpcId | Strin g | Query | No | vpc-test**** | The virtual private cloud (VPC) ID. This parameter is required when NetType is set to csw. |
| Lang | Strin g | Query | No | zh | The language. Valid values: zh and en. You can leave this parameter empty if it is not required for your business. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| DataList | Array |   |   |
| -StartTime | Integer | 1525833105 | The start time of the session. |
| -SrcIp | String | 1.1.1.1 | The source IP address. |
| -Loction | String | Beijing | The geographical location of the source IP address. |

| Developer Guide·A on | PI documentat |   | Cloud Security Network Detecti n and Respons |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| -SrcPort | Integer | 80 | The source port. |
| -DstIp | String | 1.1.1.1 | The destination IP address. |
| -DstLoc | String | Beijing | The geographical location of the destination IP address. |
| -DstPort | Integer | 80 | The destination port. |
| -App | String | HTTP | The name of the application. |
| -PktCount | Integer | 10 | The number of session packets. |
| -TrafficBps | Integer | 10 | The amount of traffic. |
| -Duration | Integer | 10 | The duration of the session. Unit: seconds. |
| -AttackType | String |   | The attack type. No data is returned. |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| TotalCount | Integer | 100 | The total number of entries returned. |
| Module | String | ndr*** | The name of the module. |
| PageInfo | Struct |   |   |
| -PageSize | Integer | 10 | The number of entries per page. |
| -CurrentPage | Integer | 1 | The page number. |
| -TotalCount | Integer | 100 | The total number of entries returned. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=DescribeSessionByIp&RegionId=cnhangzhou&Lang=zh&Direction=in&StartTime=1525833105&EndTime=1525833105&AliUid=1234567890&S Ip=1.1.1.1&DstIp=1.1.1.1&NetType=isw&Sort=total_packet_bytes&App=HTTP&CurrentPage=1&PageS e=10&SrcPort=65534&DstPort=8080&VpcId=vpc-test****&Lang=zh
```

Sample success responses `JSON` format

```
Content-Type:application/json
```

`{`

```json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "DataList":[
```

`{`

```json
            "App":"HTTP",
            "SrcPort":80,
            "StartTime":1525833105,
            "Loction":"Beijing",
            "DstIp":"1.1.1.1",
            "DstLoc":"Beijing",
            "PktCount":10,
            "Duration":10,
            "AttackType":"",
            "DstPort":80,
            "TrafficBps":10,
            "SrcIp":"1.1.1.1"
```

`}` `],`

```json
    "TotalCount":100,
    "PageInfo":{
        "TotalCount":100,
        "PageSize":10,
        "CurrentPage":1
```

`},`

```json
    "Module":"ndr***"
```

`}` `XML` format

```xml
Content-Type:application/xml <DescribeSessionByIpResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <DataList>
        <StartTime>1525833105</StartTime>
        <SrcIp>1.1.1.1</SrcIp>
        <Location>Beijing</Location>
        <SrcPort>80</SrcPort>
        <DstIp>1.1.1.1</DstIp>
        <DstLoc>Beijing</DstLoc>
        <DstPort>80</DstPort>
        <App>HTTP</App>
        <PktCount>10</PktCount>
        <TrafficBps>10</TrafficBps>
        <Duration>10</Duration>
        <AttackType></AttackType>
    </DataList>
    <TotalCount>100</TotalCount>
    <PageInfo>
        <PageSize>10</PageSize>
        <CurrentPage>1</CurrentPage>
        <TotalCount>100</TotalCount>
    </PageInfo>
    <Module>ndr***</Module>
</DescribeSessionByIpResponse>
```

### Log retrieval

#### DescribeHitLogColumns

Queries log data to be displayed in column charts.

**Authorization information**

| Operation | Access level | Resource type |
|---|---|---|
| yundun- cloudfirewall:DescribeHitLogCol umns | Read | acs:yundun-cloudfirewall:*: {#accountId}:* |

**Throttling**

You can call this operation up to 10 times per second per account. You can call this operation up to 100 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

**q**

**p**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Lang | Strin g | Query | No | zh | The language. Valid values: zh and en. You can leave this parameter empty if it is not required for your business. |
| AliUid | Long | Query | No | 123456789 | The user ID. |
| IndexType | Strin g | Query | No | ndr reset log _ _ | The log type. |
| Query | Strin g | Query | No | src ip:10.x.x.x _ | The query condition. |
| StartTime | Long | Query | No | 1706668721 | The beginning of the time range to query. |
| EndTime | Long | Query | No | 1706668721 | The end of the time range to query. |
| Interval | Long | Query | No | 5000 | The interval. |
| DeptAliUid | Strin g | Query | No | 1234567890 | The department ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| DataList | Array |   |   |
| -StartTime | Integer | 1706668721 | The beginning of the time range to query. |
| -EndTime | Integer | 1706668721 | The end of the time range to query. |
| -Count | Integer | 1000 | The number of entries returned. |
| -Interval | Integer | 5000 | The interval. |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |

| Developer Guide·A | PI documentat |   | Cloud Security Network Detecti |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| Module | String | ndr*** | The name of the module. |
| TaskUUID | String | cfa13285-5330- 402e-xxx- 5075c12c6aa8 | The task ID. |
| TotalCount | Integer | 100 | The total number of entries returned. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=DescribeHitLogColumns&RegionId=cnhangzhou&Lang=zh&AliUid=123456789&IndexType=ndr_reset_log&Query=src_ip:10.x.x.x&StartTime 706668721&EndTime=1706668721&Interval=5000&DeptAliUid=1234567890
```

Sample success responses `JSON` format

```
Content-Type:application/json
```

`{`

```json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "Module":"ndr***",
    "TaskUUID":"cfa13285-5330-402e-xxx-5075c12c6aa8",
    "TotalCount":100,
    "DataList":[
```

`{`

```json
            "EndTime":1706668721,
            "StartTime":1706668721,
            "Count":1000,
            "Interval":5000
```

`}` `]` `}` `XML` format

```xml
Content-Type:application/xml <DescribeHitLogColumnsResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <Module>ndr***</Module>
    <TaskUUID>cfa13285-5330-402e-xxx-5075c12c6aa8</TaskUUID>
    <TotalCount>100</TotalCount>
    <DataList>
        <StartTime>1706668721</StartTime>
        <EndTime>1706668721</EndTime>
        <Count>1000</Count>
        <Interval>5000</Interval>
    </DataList>
</DescribeHitLogColumnsResponse>
```

#### DescribeSearchTemplate

Queries the information about a template.

**Authorization information**

| Operation | Access level | Resource type |
|---|---|---|
| yundun- cloudfirewall:DescribeSearchTe mplate | Read | acs:yundun-cloudfirewall:*: {#accountId}:* |

**Throttling**

You can call this operation up to 10 times per second per account. You can call this operation up to 100 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Lang | Strin g | Query | No | zh | The language. Valid values: zh and en. You can leave this parameter empty if it is not required for your business. |

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| AliUid | Long | Query | No | 123456789 | The user ID. |
| PageSize | Integ er | Query | No | 10 | The number of entries per page. |
| PageNo | Integ er | Query | No | 1 | The page number. |
| Filter | Strin g | Query | No | src ip:10.x.x.x _ | The query condition that contains keywords to perform queries on TemName and Query. |
| DeptAliUid | Strin g | Query | No | 1234567890 | The department ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| DataList | Array |   |   |
| -TemID | Integer | 1 | The template ID. |
| -AliUid | Long | 123456789 | The user ID. |
| -TemName | String | test tem _ | The name of the template. |
| -LogType | String | ndr reset log _ _ | The log type. |
| -Query | String | src ip:10.x.x.x _ | The query condition. |
| -StartTime | Integer | 1706668721 | The beginning of the time range to query. |
| -EndTime | Integer | 1706668721 | The end of the time range to query. |
| -RangeFlag | Integer | 100000 | The interval. |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| module | String |   |   |

| n | Cloud Security Ne and Response | twork Detectio |   | Developer Guide·API documenta io | t n |
|---|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| TotalCount | Integer | 100 | The total number of entries returned. |
| PageSize | Integer | 10 | The number of entries per page. |
| CurrentPage | Integer | 1 | The page number. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=DescribeSearchTemplate&RegionId=cnhangzhou&Lang=zh&AliUid=123456789&PageSize=10&PageNo=1&Filter=src_ip:10.x.x.x&DeptAliUid= 34567890
```

Sample success responses `JSON` format

```
Content-Type:application/json
```

`{`

```json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "module":"",
    "TotalCount":100,
    "PageSize":10,
    "CurrentPage":1,
    "DataList":[
```

`{`

```json
            "Query":"src_ip:10.x.x.x",
            "EndTime":1706668721,
            "RangeFlag":100000,
            "TemID":1,
            "LogType":"ndr_reset_log",
            "StartTime":1706668721,
            "TemName":"test_tem",
            "AliUid":123456789
```

`}` `]` `}` `XML` format

```xml
Content-Type:application/xml <DescribeSearchTemplateResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <module></module>
    <TotalCount>100</TotalCount>
    <PageSize>10</PageSize>
    <CurrentPage>1</CurrentPage>
    <DataList>
        <TemID>1</TemID>
        <AliUid>123456789</AliUid>
        <TemName>test_tem</TemName>
        <LogType>ndr_reset_log</LogType>
        <Query>src_ip:10.x.x.x</Query>
        <StartTime>1706668721</StartTime>
        <EndTime>1706668721</EndTime>
        <RangeFlag>100000</RangeFlag>
    </DataList>
</DescribeSearchTemplateResponse>
```

#### UpdateVisibleLogFields

Displays or hides a field.

**Authorization information**

| Operation | Access level | Resource type |
|---|---|---|
| yundun- cloudfirewall:UpdateVisibleLogF ields | Write | acs:yundun-cloudfirewall:*: {#accountId}:* |

**Throttling**

You can call this operation up to 10 times per second per account. You can call this operation up to 100 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Lang | Strin g | Query | No | zh | The language. Valid values: zh and en. You can leave this parameter empty if it is not required for your business. |
| IndexType | Strin g | Query | No | ndr reset log _ _ | The log type. |
| FieldNam e | Strin g | Query | No | src ip _ | The name of the field. |
| Display | Integ er | Query | No | 0 | Indicates whether to display the field. A value of 0 indicates that the field is hidden. A value of 1 indicates that the field is displayed. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Module | String | ndr*** | The name of the module. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=UpdateVisibleLogFields&RegionId=cnhangzhou&Lang=zh&IndexType=ndr_reset_log&FieldName=src_ip&Display=0
```

Sample success responses `JSON` format

```
Content-Type:application/json
```

`{`

```json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "Module":"ndr***"
```

`}` `XML` format

```xml
Content-Type:application/xml <UpdateVisibleLogFieldsResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <Module>ndr***</Module>
</UpdateVisibleLogFieldsResponse>
```

#### ExportHitlogs

Exports specific logs.

**Authorization information**

| Operation | Access level | Resource type |
|---|---|---|
| yundun- cloudfirewall:ExportHitlogs | Write | acs:yundun-cloudfirewall:*: {#accountId}:* |

**Throttling**

You can call this operation up to 10 times per second per account. You can call this operation up to 100 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Lang | Strin g | Query | No | zh | The language. Valid values: zh and en. You can leave this parameter empty if it is not required for your business. |
| AliUid | Strin g | Query | No | 123456789 | The user ID. |
| IndexType | Strin g | Query | No | ndr reset log _ _ | The log type. |
| Query | Strin g | Query | No | src ip:10.x.x.x _ | The query condition. |
| StartTime | Strin g | Query | No | 1706668721 | The beginning of the time range to query. |

| Cloud Security and Respon | Network se | Detectio |   | Devel | oper Guide·API documenta io |
|---|---|---|---|---|---|

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| EndTime | Strin g | Query | No | 1706668721 | The end of the time range to query. |
| Filter | Integ er | Query | No | 0 | The export mode. A value of 0 indicates that all fields are exported. A value of 1 indicates that only selected fields are exported. |
| Sort | Strin g | Query | No | [{'session time': _ {'order':'desc'}}, {'source ip: _ {'order':'asc'}}] | The sorting method. By default, logs are sorted by session time in _ descending order. To sort logs by other fields, modify the JSON string to include those fields in the same format. |
| Size | Integ er | Query | No | 100 | The number of rows in the exported file. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Module | String | ndr*** | The name of the module. |
| TaskUUID | String | cfa13285-5330- 402e-xxx- 5075c12c6aa8 | The export task ID. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=ExportHitlogs&RegionId=cnhangzhou&Lang=zh&AliUid=123456789&IndexType=ndr_reset_log&Query=src_ip:10.x.x.x&StartTime 706668721&EndTime=1706668721&Filter=0&Sort=[{'session_time':{'order':'desc'}},{'source_ ip:{'order':'asc'}}]&Size=100
```

Sample success responses `JSON` format

```
Content-Type:application/json
```

`{`

```json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "Module":"ndr***",
    "TaskUUID":"cfa13285-5330-402e-xxx-5075c12c6aa8"
```

`}` `XML` format

```xml
Content-Type:application/xml <ExportHitlogsResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <Module>ndr***</Module>
    <TaskUUID>cfa13285-5330-402e-xxx-5075c12c6aa8</TaskUUID>
</ExportHitlogsResponse>
```

#### DescribeGivenFieldStatistics

Queries the statistics on a specific field.

**Authorization information**

| Operation | Access level | Resource type |
|---|---|---|
| yundun- cloudfirewall:DescribeGivenFiel dStatistics | Read | acs:yundun-cloudfirewall:*: {#accountId}:* |

**Throttling**

You can call this operation up to 10 times per second per account. You can call this operation up to 100 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Lang | Strin g | Query | No | zh | The language. Valid values: zh and en. You can leave this parameter empty if it is not required for your business. |
| AliUid | Long | Query | No | 123456789 | The user ID. |
| IndexType | Strin g | Query | No | ndr reset log _ _ | The log type. |
| Query | Strin g | Query | No | src ip:10.x.x.x _ | The query condition. |
| StartTime | Integ er | Query | No | 1706668721 | The beginning of the time range to query. |
| EndTime | Integ er | Query | No | 1706668721 | The end of the time range to query. |
| FieldNam e | Strin g | Query | No | src ip _ | The name of the field. |
| DeptAliUid | Strin g | Query | No | 1234567890 | The department ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| DataList | Array |   |   |
| -Type | String | 1 | The category of the field. |
| -Count | String | 1000 | The number of entries returned. |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Module | String | ndr*** | The name of the module. |
| TotalCount | Integer | 100 | The total number of entries returned. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=DescribeGivenFieldStatistics&RegionId=cnhangzhou&Lang=zh&AliUid=123456789&IndexType=ndr_reset_log&Query=src_ip:10.x.x.x&StartTime 706668721&EndTime=1706668721&FieldName=src_ip&DeptAliUid=1234567890
```

Sample success responses `JSON` format

```
Content-Type:application/json
```

`{`

```json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "Module":"ndr***",
    "TotalCount":100,
    "DataList":[
```

`{`

```json
            "Type":"1",
            "Count":"1000"
```

`}` `]` `}` `XML` format

```xml
Content-Type:application/xml <DescribeGivenFieldStatisticsResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <Module>ndr***</Module>
    <TotalCount>100</TotalCount>
    <DataList>
        <Type>1</Type>
        <Count>1000</Count>
    </DataList>
</DescribeGivenFieldStatisticsResponse>
```

#### DescribeHitLogColumnsData

Queries logs to display data in column charts.

**Authorization information**

| Operation | Access level | Resource type |
|---|---|---|
| yundun- cloudfirewall:DescribeHitLogCol umnsData | Read | acs:yundun-cloudfirewall:*: {#accountId}:* |

**Throttling**

You can call this operation up to 10 times per second per account. You can call this operation up to 100 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Lang | Strin g | Query | No | zh | The language. Valid values: zh and en. You can leave this parameter empty if it is not required for your business. |
| AliUid | Long | Query | No | 123456789 | The user ID. |
| TaskUUID | Strin g | Query | No | cfa13285-5330-402e- xxx-5075c12c6aa8 | The task UUID. |
| DeptAliUid | Strin g | Query | No | 1234567890 | The department ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Module | String | ndr*** | The name of the module. |
| TaskUUID | String | cfa13285-5330- 402e-xxx- 5075c12c6aa8 | The task UUID. |
| TaskStatus | Integer | 1 | The status of the task. A value of 0 indicates that the query is not complete and needs to be performed again. A value of 1 indicates that the query is complete. |
| HitLogData | Struct |   |   |
| -DataList | Array |   |   |
| --StartTime | Integer | 1706668721 | The beginning of the time range to query. |

| Developer Guide·A on | PI documentat |   | Cloud Security Network Detecti n and Respons |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| --EndTime | Integer | 1706668721 | The end of the time range to query. |
| --Count | Integer | 1000 | The number of matched logs. |
| --Interval | Integer | 5000 | The interval. |
| -TotalCount | Integer | 100 | The total number of entries returned. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=DescribeHitLogColumnsData&RegionId=cnhangzhou&Lang=zh&AliUid=123456789&TaskUUID=cfa13285-5330-402e-xxx- 5075c12c6aa8&DeptAliUid=1234567890
```

Sample success responses `JSON` format

```
Content-Type:application/json
```

`{`

```json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "Module":"ndr***",
    "TaskUUID":"cfa13285-5330-402e-xxx-5075c12c6aa8",
    "TaskStatus":1,
    "HitLogData":{
        "DataList":[
```

`{`

```json
                "EndTime":1706668721,
                "StartTime":1706668721,
                "Count":1000,
                "Interval":5000
```

`}` `],`

```json
        "TotalCount":100
```

`}` `}` `XML` format

```xml
Content-Type:application/xml <DescribeHitLogColumnsDataResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <Module>ndr***</Module>
    <TaskUUID>cfa13285-5330-402e-xxx-5075c12c6aa8</TaskUUID>
    <TaskStatus>1</TaskStatus>
    <HitLogData>
        <TotalCount>100</TotalCount>
        <DataList>
            <StartTime>1706668721</StartTime>
            <EndTime>1706668721</EndTime>
            <Count>1000</Count>
            <Interval>5000</Interval>
        </DataList>
    </HitLogData>
</DescribeHitLogColumnsDataResponse>
```

#### DescribeHitStatistics

Queries hit logs.

**Authorization information**

| Operation | Access level | Resource type |
|---|---|---|
| yundun- cloudfirewall:DescribeHitStatisti cs | Read | acs:yundun-cloudfirewall:*: {#accountId}:* |

**Throttling**

You can call this operation up to 10 times per second per account. You can call this operation up to 100 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Lang | Strin g | Query | No | zh | The language. Valid values: zh and en. You can leave this parameter empty if it is not required for your business. |

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| AliUid | Long | Query | No | 123456789 | The user ID. |
| IndexType | Strin g | Query | No | ndr reset log _ _ | The log type. |
| Query | Strin g | Query | No | src ip:10.x.x.x _ | The query condition. |
| StartTime | Long | Query | No | 1706668721 | The beginning of the time range to query. |
| EndTime | Long | Query | No | 1706668721 | The end of the time range to query. |
| DeptAliUid | Strin g | Query | No | 1234567890 | The department ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| IndexList | Array |   |   |
| -IndexName | String | ndr reset log _ _ | The name of the index that contains data. |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Module | String | ndr*** | The name of the module. |
| TotalCount | Long | 100 | The total number of entries returned. |
| StartTime | Long | 1706668721 | The beginning of the time range to query. |
| EndTime | Long | 1706668721 | The end of the time range to query. |
| Interval | Long | 5000 | The interval. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=DescribeHitStatistics&RegionId=cnhangzhou&Lang=zh&AliUid=123456789&IndexType=ndr_reset_log&Query=src_ip:10.x.x.x&StartTime 706668721&EndTime=1706668721&DeptAliUid=1234567890
```

Sample success responses `JSON` format

```
Content-Type:application/json
```

`{`

```json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "Module":"ndr***",
    "TotalCount":100,
    "StartTime":1706668721,
    "EndTime":1706668721,
    "Interval":5000,
    "IndexList":[
```

`{`

```json
            "IndexName":"ndr_reset_log"
```

`}` `]` `}` `XML` format

```xml
Content-Type:application/xml <DescribeHitStatisticsResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <Module>ndr***</Module>
    <TotalCount>100</TotalCount>
    <StartTime>1706668721</StartTime>
    <EndTime>1706668721</EndTime>
    <Interval>5000</Interval>
    <IndexList>
        <IndexName>ndr_reset_log</IndexName>
    </IndexList>
</DescribeHitStatisticsResponse>
```

#### DescribeLogFieldIntroduction

Queries the field description of Elasticsearch logs.

**Authorization information**

| Operation | Access level | Resource type |
|---|---|---|
| yundun- cloudfirewall:DescribeLogFieldI ntroduction | Read | acs:yundun-cloudfirewall:*: {#accountId}:* |

**Throttling**

You can call this operation up to 10 times per second per account. You can call this operation up to 100 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Lang | Strin g | Query | No | zh | The language. Valid values: zh and en. You can leave this parameter empty if it is not required for your business. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| SecureEvents | Array |   |   |
| -FieldList | Array |   |   |
| --FieldName | String | src ip _ | The name of the field. |
| --FieldNameEn | String | src ip _ | The name of the field in English. |
| --FieldNameZh | String | src ip _ | The name of the field in Chinese. |
| --FieldDesc | String | test | The description of the field. |
| --FieldDescEn | String | test | The description of the field in English. |
| --FieldType | String | text | The data type of the field. |
| -IndexName | String | ndr attack log _ _ | The name of the index. |

| loud Security Net and Response | work Detectio |   | Developer Guide·API documenta io |
|---|---|---|---|
| Parameter | Type | Example | Description |
| -Ttl | Integer | 10 | The time-to-live (TTL) of data. |
| TrafficLogs | Array |   |   |
| -FieldList | Array |   |   |
| --FieldName | String | src ip _ | The name of the field. |
| --FieldNameEn | String | src ip _ | The name of the field in English. |
| --FieldNameZh | String | src ip _ | The name of the field in Chinese. |
| --FieldDesc | String | test | The description of the field. |
| --FieldDescEn | String | test | The description of the field in English. |
| --FieldType | String | text | The data type of the field. |
| -IndexName | String | ndr attack log _ _ | The name of the index. |
| -Ttl | Integer | 10 | The TTL of data. |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Module | String | ndr*** | The name of the module. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=DescribeLogFieldIntroduction&RegionId=cn-hangzhou&Lang=zh
```

Sample success responses `JSON` format

```
Content-Type:application/json
```

`{`

```json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "Module":"ndr***",
    "SecureEvents":[
```

`{`

```json
            "IndexName":"ndr_attack_log",
            "Ttl":10,
            "FieldList":[
```

`{`

```json
                    "FieldDescEn":"test",
                    "FieldNameEn":"src_ip",
                    "FieldNameZh":"src_ip",
                    "FieldName":"src_ip",
                    "FieldDesc":"test",
                    "FieldType":"text"
```

`}` `]` `}` `],`

```json
    "TrafficLogs":[
```

`{`

```json
            "IndexName":"ndr_attack_log",
            "Ttl":10,
            "FieldList":[
```

`{`

```json
                    "FieldDescEn":"test",
                    "FieldNameEn":"src_ip",
                    "FieldNameZh":"src_ip",
                    "FieldName":"src_ip",
                    "FieldDesc":"test",
                    "FieldType":"text"
```

`}` `]` `}` `]` `}` `XML` format

```xml
Content-Type:application/xml <DescribeLogFieldIntroductionResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <Module>ndr***</Module>
    <SecureEvents>
        <IndexName>ndr_attack_log</IndexName>
        <Ttl>10</Ttl>
        <FieldList>
            <FieldName>src_ip</FieldName>
            <FieldNameEn>src_ip</FieldNameEn>
            <FieldNameZh>src_ip</FieldNameZh>
            <FieldDesc>test</FieldDesc>
            <FieldDescEn>test</FieldDescEn>
            <FieldType>text</FieldType>
        </FieldList>
    </SecureEvents>
    <TrafficLogs>
        <IndexName>ndr_attack_log</IndexName>
        <Ttl>10</Ttl>
        <FieldList>
            <FieldName>src_ip</FieldName>
            <FieldNameEn>src_ip</FieldNameEn>
            <FieldNameZh>src_ip</FieldNameZh>
            <FieldDesc>test</FieldDesc>
            <FieldDescEn>test</FieldDescEn>
            <FieldType>text</FieldType>
        </FieldList>
    </TrafficLogs>
</DescribeLogFieldIntroductionResponse>
```

#### DescribeHitDetailList

Queries the details of rule hit results.

**Authorization information**

| Operation | Access level | Resource type |
|---|---|---|
| yundun- cloudfirewall:DescribeHitDetailL ist | Read | acs:yundun-cloudfirewall:*: {#accountId}:* |

**Throttling**

You can call this operation up to 100 times per second per account. You can call this operation up to 1,000 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Lang | Strin g | Query | No | zh | The language. Valid values: zh and en. You can leave this parameter empty if it is not required for your business. |
| AliUid | Long | Query | No | 123456789 | The user ID. |
| IndexType | Strin g | Query | No | ndr reset log _ _ | The log type. |
| Query | Strin g | Query | No | src ip:10.x.x.x _ | The query condition. |
| StartTime | Long | Query | No | 1706668721 | The beginning of the time range to query. |
| EndTime | Long | Query | No | 1706668721 | The end of the time range to query. |
| PageSize | Integ er | Query | No | 10 | The number of entries per page. |
| PageNo | Integ er | Query | No | 1 | The page number. |
| Sort | Strin g | Query | No | [{session time: _ {order:desc}}, {source ip: _ {order:asc}}] | The sorting method. By default, logs are sorted by session time in _ descending order. To sort logs by other fields, modify the JSON string to include those fields in the same format. |
| DeptAliUid | Strin g | Query | No | 1234567890 | The department ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| DataList | Array |   |   |
| -Index | String | ndr reset log _ _ | The name of the index that is used as the data source. |

| Cloud Security Ne and Response | twork Detectio |   | Developer Guide·API documenta io |
|---|---|---|---|
| Parameter | Type | Example | Description |
| -Display | Map | {src ip:10.x.x.x,dst _ ip:10.x.x.x} _ | The data source of display fields. |
| -Original | Map | {src ip:10.x.x.x,dst _ ip:10.x.x.x,dst por _ _ t:80} | The original data source. |
| -Mapping | Map | {test:test} | The mapping table of special fields. |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Module | String | ndr*** | The name of the module. |
| TotalCount | Integer | 100 | The total number of entries returned. |
| PageSize | Integer | 10 | The number of entries per page. |
| CurrentPage | Integer | 1 | The page number. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=DescribeHitDetailList&RegionId=cnhangzhou&Lang=zh&AliUid=123456789&IndexType=ndr_reset_log&Query=src_ip:10.x.x.x&StartTime 706668721&EndTime=1706668721&PageSize=10&PageNo=1&Sort=[{session_time:{order:desc}},{so urce_ip:{order:asc}}]&DeptAliUid=1234567890
```

Sample success responses `JSON` format

```
Content-Type:application/json
```

`{`

```json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "Module":"ndr***",
    "TotalCount":100,
    "PageSize":10,
    "CurrentPage":1,
    "DataList":[
```

`{`

```json
            "Index":"ndr_reset_log",
            "Mapping":"{test:test}",
            "Original":"{src_ip:10.x.x.x,dst_ip:10.x.x.x,dst_port:80}",
            "Display":"{src_ip:10.x.x.x,dst_ip:10.x.x.x}"
```

`}` `]` `}` `XML` format

```xml
Content-Type:application/xml <DescribeHitDetailListResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <Module>ndr***</Module>
    <TotalCount>100</TotalCount>
    <PageSize>10</PageSize>
    <CurrentPage>1</CurrentPage>
    <DataList>
        <Index>ndr_reset_log</Index>
        <Display>{src_ip:10.x.x.x,dst_ip:10.x.x.x}</Display>
        <Original>{src_ip:10.x.x.x,dst_ip:10.x.x.x,dst_port:80}</Original>
        <Mapping>{test:test}</Mapping>
    </DataList>
</DescribeHitDetailListResponse>
```

#### DescribeLogFields

Queries the fields that are displayed and hidden in logs.

**Authorization information**

| Operation | Access level | Resource type |
|---|---|---|
| yundun- cloudfirewall:DescribeLogFields | Read | acs:yundun-cloudfirewall:*: {#accountId}:* |

**Throttling**

You can call this operation up to 10 times per second per account. You can call this operation up to 100 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Lang | Strin g | Query | No | zh | The language. Valid values: zh and en. You can leave this parameter empty if it is not required for your business. |
| IndexType | Strin g | Query | No | ndr reset log _ _ | The log type. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| DisplayList | Array |   |   |
| -FieldName | String | src ip _ | The name of the field. |
| -FiledNameZh | String | src ip _ | The name of the field in Chinese. |
| -FiledNameEn | String | src ip _ | The name of the field in English. |
| -FiledType | String | text | The data type of the field. |
| -FiledDesc | String | test | The description of the field. |
| -FiledDescEn | String | test | The description of the field in English. |
| -FiledsNo | Integer | 10 | The sequence number of the field. |
| NoDisplayList | Array |   |   |
| -FieldName | String | src ip _ | The name of the field. |
| -FiledNameZh | String | src ip _ | The name of the field in Chinese. |

| i | Developer Guide·A on | PI documentat |   | Cloud Security Network Detecti n and Respons | o e |
|---|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| -FiledNameEn | String | src ip _ | The name of the field in English. |
| -FiledType | String | text | The data type of the field. |
| -FiledDesc | String | test | The description of the field. |
| -FiledDescEn | String | test | The description of the field in English. |
| -FiledsNo | Integer | 10 | The sequence number of the field. |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Module | String | ndr*** | The name of the module. |
| TotalCount | Integer | 100 | The total number of entries returned. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=DescribeLogFields&RegionId=cnhangzhou&Lang=zh&IndexType=ndr_reset_log
```

Sample success responses `JSON` format

```
Content-Type:application/json
```

`{`

```json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "Module":"ndr***",
    "TotalCount":100,
    "DisplayList":[
```

`{`

```json
            "FiledNameZh":"src_ip",
            "FiledDesc":"test",
            "FiledsNo":10,
            "FiledType":"text",
            "FiledDescEn":"test",
            "FiledNameEn":"src_ip",
            "FieldName":"src_ip"
```

`}` `],`

```json
    "NoDisplayList":[
```

`{`

```json
            "FiledNameZh":"src_ip",
            "FiledDesc":"test",
            "FiledsNo":10,
            "FiledType":"text",
            "FiledDescEn":"test",
            "FiledNameEn":"src_ip",
            "FieldName":"src_ip"
```

`}` `]` `}` `XML` format

```xml
Content-Type:application/xml <DescribeLogFieldsResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <Module>ndr***</Module>
    <TotalCount>100</TotalCount>
    <DisplayList>
        <FieldName>src_ip</FieldName>
        <FiledNameZh>src_ip</FiledNameZh>
        <FiledNameEn>src_ip</FiledNameEn>
        <FiledType>text</FiledType>
        <FiledDesc>test</FiledDesc>
        <FiledDescEn>test</FiledDescEn>
        <FiledsNo>10</FiledsNo>
    </DisplayList>
    <NoDisplayList>
        <FieldName>src_ip</FieldName>
        <FiledNameZh>src_ip</FiledNameZh>
        <FiledNameEn>src_ip</FiledNameEn>
        <FiledType>text</FiledType>
        <FiledDesc>test</FiledDesc>
        <FiledDescEn>test</FiledDescEn>
        <FiledsNo>10</FiledsNo>
    </NoDisplayList>
</DescribeLogFieldsResponse>
```

#### DescribeLogType

Queries the types of Elasticsearch logs.

**Authorization information**

| Operation | Access level | Resource type |
|---|---|---|
| yundun- cloudfirewall:DescribeLogType | Read | acs:yundun-cloudfirewall:*: {#accountId}:* |

**Throttling**

You can call this operation up to 10 times per second per account. You can call this operation up to 100 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Lang | Strin g | Query | No | zh | The language. Valid values: zh and en. You can leave this parameter empty if it is not required for your business. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| SecureEventLi st | Array |   |   |
| -IndexType | String | TrafficLog | The index type. A value of SecureEvent indicates the index of security event logs. A value of TrafficLog indicates the index of full traffic logs. |
| -IndexName | String | ndr attack log _ _ | The name of the index. |
| -IndexNameEn | String | ndr attack log _ _ | The name of the index in English. |
| -IndexDesc | String | test | The description of the index. |
| -IndexCycle | String | day | The indexing cycle. Valid values: no, day, mon, and year. |
| TrafficLogList | Array |   |   |
| -IndexType | String | TrafficLog | The index type. A value of SecureEvent indicates the index of security event logs. A value of TrafficLog indicates the index of full traffic logs. |
| -IndexName | String | ndr attack log _ _ | The name of the index. |
| -IndexNameEn | String | ndr attack log _ _ | The name of the index in English. |
| -IndexDesc | String | test | The description of the index. |
| -IndexCycle | String | day | The indexing cycle. Valid values: no, day, mon, and year. |

| Developer Guide·A | PI documentat |   | Cloud Security Network Detecti |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| BehaviorAnaly sisList | Array |   |   |
| -IndexType | String | TrafficLog | The index type. A value of SecureEvent indicates the index of security event logs. A value of TrafficLog indicates the index of full traffic logs. |
| -IndexName | String | ndr attack log _ _ | The name of the index. |
| -IndexNameEn | String | ndr attack log _ _ | The name of the index in English. |
| -IndexDesc | String | test | The description of the index. |
| -IndexCycle | String | day | The indexing cycle. Valid values: no, day, mon, and year. |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Module | String | ndr*** | The name of the module. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=DescribeLogType&RegionId=cn-hangzhou&Lang=zh
```

Sample success responses `JSON` format

```
Content-Type:application/json
```

`{`

```json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "Module":"ndr***",
    "SecureEventList":[
```

`{`

```json
            "IndexName":"ndr_attack_log",
            "IndexNameEn":"ndr_attack_log",
            "IndexCycle":"day",
            "IndexDesc":"test",
            "IndexType":"TrafficLog"
```

`}` `],`

```json
    "TrafficLogList":[
```

`{`

```json
            "IndexName":"ndr_attack_log",
            "IndexNameEn":"ndr_attack_log",
            "IndexCycle":"day",
            "IndexDesc":"test",
            "IndexType":"TrafficLog"
```

`}` `],`

```json
    "BehaviorAnalysisList":[
```

`{`

```json
            "IndexName":"ndr_attack_log",
            "IndexNameEn":"ndr_attack_log",
            "IndexCycle":"day",
            "IndexDesc":"test",
            "IndexType":"TrafficLog"
```

`}` `]` `}` `XML` format

```xml
Content-Type:application/xml <DescribeLogTypeResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <Module>ndr***</Module>
    <SecureEventList>
        <IndexType>TrafficLog</IndexType>
        <IndexName>ndr_attack_log</IndexName>
        <IndexNameEn>ndr_attack_log</IndexNameEn>
        <IndexDesc>test</IndexDesc>
        <IndexCycle>day</IndexCycle>
    </SecureEventList>
    <TrafficLogList>
        <IndexType>TrafficLog</IndexType>
        <IndexName>ndr_attack_log</IndexName>
        <IndexNameEn>ndr_attack_log</IndexNameEn>
        <IndexDesc>test</IndexDesc>
        <IndexCycle>day</IndexCycle>
    </TrafficLogList>
    <BehaviorAnalysisList>
        <IndexType>TrafficLog</IndexType>
        <IndexName>ndr_attack_log</IndexName>
        <IndexNameEn>ndr_attack_log</IndexNameEn>
        <IndexDesc>test</IndexDesc>
        <IndexCycle>day</IndexCycle>
    </BehaviorAnalysisList>
</DescribeLogTypeResponse>
```

#### DelSearchTemplate

Deletes a log retrieval template.

**Authorization information**

| Operation | Access level | Resource type |
|---|---|---|
| yundun- cloudfirewall:DelSearchTemplat e | Write | acs:yundun-cloudfirewall:*: {#accountId}:* |

**Throttling**

You can call this operation up to 10 times per second per account. You can call this operation up to 100 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Lang | Strin g | Query | No | zh | The language. Valid values: zh and en. You can leave this parameter empty if it is not required for your business. |
| AliUid | Long | Query | No | 1234567890 | The user ID. |
| TemID | Integ er | Query | No | 1024,1025 | The template IDs. You can delete multiple template IDs at a time. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Module | String | ndr*** | The name of the module. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=DelSearchTemplate&RegionId=cnhangzhou&Lang=zh&AliUid=1234567890&TemID=1024,1025
```

Sample success responses `JSON` format

```
Content-Type:application/json
```

`{`

```json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "Module":"ndr***"
```

`}` `XML` format

```xml
Content-Type:application/xml <DelSearchTemplateResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <Module>ndr***</Module>
</DelSearchTemplateResponse>
```

#### AddSearchTemplate

Creates a log retrieval template.

**Authorization information**

| Operation | Access level | Resource type |
|---|---|---|
| yundun- cloudfirewall:AddSearchTempla te | Write | acs:yundun-cloudfirewall:*: {#accountId}:* |

**Throttling**

You can call this operation up to 10 times per second per account. You can call this operation up to 100 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Lang | Strin g | Query | No | zh | The language. Valid values: zh and en. You can leave this parameter empty if it is not required for your business. |
| AliUid | Long | Query | No | 1234567890 | The user ID. |
| LogType | Strin g | Query | No | ndr attack log _ _ | The type of the log that you want to query. |
| Query | Strin g | Query | No | dest ip:1.1.1.1 _ | The query statement. |

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| StartTime | Integ er | Query | No | 1707148800 | The beginning of the time range to query. |
| EndTime | Integ er | Query | No | 1707185678 | The end of the time range to query. |
| TemName | Strin g | Query | No | test | The name of the template. |
| rangeFlag | Integ er | Query | No | 1 | The flag for the frontend. You can leave this parameter empty. |
| DeptAliUid | Strin g | Query | No | 1234567890 | The department ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Module | String | ndr*** | The name of the module. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=AddSearchTemplate&RegionId=cnhangzhou&Lang=zh&AliUid=1234567890&LogType=ndr_attack_log&Query=dest_ip:1.1.1.1&StartTime 707148800&EndTime=1707185678&TemName=test&rangeFlag=1&DeptAliUid=1234567890
```

Sample success responses `JSON` format

```
Content-Type:application/json
```

`{`

```json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "Module":"ndr***"
```

`}` `XML` format

```xml
Content-Type:application/xml <AddSearchTemplateResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <Module>ndr***</Module>
</AddSearchTemplateResponse>
```

### Attacker profile

#### DescribeAggAttackProcess

Queries a list of attack processes.

**Authorization information**

| Operation | Access level | Resource type |
|---|---|---|
| yundun- cloudfirewall:DescribeAggAttac kProcess | Read | acs:yundun-cloudfirewall:*: {#accountId}:* |

**Throttling**

You can call this operation up to 10 times per second per account. You can call this operation up to 100 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Lang | Strin g | Query | No | zh | The language. Valid values: zh and en. You can leave this parameter empty if it is not required for your business. |
| AliUid | Long | Query | No | 1234567890 | The user ID. |
| StartTime | Long | Query | No | 1707118672 | The beginning of the time range to query. |

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| EndTime | Long | Query | No | 1707118672 | The end of the time range to query. |
| AttackRes ult | Strin g | Query | No | 0 | The attack result. A value of 0 indicates that the attacker attempted an attack. A value of 1 indicates that the attack is successful. A value of -1 indicates that the attack has failed. |
| VulLevel | Strin g | Query | No | 1 | The threat level. A value of 1 indicates low risk. A value of 2 indicates medium risk. A value of 3 indicates high risk. |
| SrcIP | Strin g | Query | No | 1.1.1.1 | The source IP address. |
| DeptAliUid | Strin g | Query | No | 1234567890 | The department ID. |
| PageSize | Integ er | Query | No | 10 | The number of entries per page. |
| PageNo | Integ er | Query | No | 1 | The page number. |
| LinkType | Strin g | Query | No | 0 | The product on which the attack is detected. A value of 0 indicates Inter-connection Switch (ISW). A value of 1 indicates Customer Access Switch (CSW). A value of 2 indicates LVS Switch (LSW). A value of 3 indicates Elastic Network Interface (ENI). |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| AttackProcess List | Array |   |   |
| -StartTime | Long | 1707118672 | The beginning of the time range to query. |

| i | Developer Guide·A on | PI documentat |   | Cloud Security Network Detecti n and Respons | o e |
|---|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| -EndTime | Long | 1707118672 | The end of the time range to query. |
| -SrcIP | String | 1.1.1.1 | The source IP address. |
| -AttackerIP | String | 1.1.1.1 | The IP address of the attacker. |
| -AttackType | String | Web attack | The attack type. |
| -RuleNote | String | Web attack | The description of the rule. |
| -RuleID | Long | 12323 | The rule ID. |
| -DstIP | String | 2.2.2.2 | The destination IP address. |
| -DstDomin | String | www.test.com | The domain name. |
| -DstIPType | String | EIP | The type of the destination IP address. |
| - TotalAttackTi mes | Integer | 100 | The total number of attacks. |
| - AttackSuccess Count | Integer | 10 | The number of successful attacks. |
| - AttackFailCoun t | Integer | 80 | The number of failed attacks. |
| - AttackTryCoun t | Integer | 10 | The total number of attack attempts. |
| -RelatedEcs | Map | ... | The associated Elastic Compute Service (ECS) instance. |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| TotalCount | Integer | 100 | The total number of entries returned. |
| PageSize | Integer | 10 | The number of entries per page. |

| Cloud Security Ne and Response | twork Detectio |   | Developer Guide·API documenta io |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| CurrentPage | Integer | 1 | The page number. |
| FirstAttackTim e | Long | 1707118672 | The time when the first attack occurred. |
| FirstAttackedIP | String | 2.2.2.2 | The destination IP address of the first attack. |
| Success | Boolean | true | Indicates whether the HTTP request was successful. |
| Module | String | ndr*** | The name of the module. |
| HttpStatusCod e | Integer | 200 | The HTTP status code. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=DescribeAggAttackProcess&RegionId=cnhangzhou&Lang=zh&AliUid=1234567890&StartTime=1707118672&EndTime=1707118672&AttackResult=0 ulLevel=1&SrcIP=1.1.1.1&DeptAliUid=1234567890&PageSize=10&PageNo=1&LinkType=0
```

Sample success responses `JSON` format

```
Content-Type:application/json
```

`{`

```json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "TotalCount":100,
    "PageSize":10,
    "CurrentPage":1,
    "FirstAttackTime":1707118672,
    "FirstAttackedIP":"2.2.2.2",
    "AttackProcessList":[
```

`{`

```json
            "AttackTryCount":10,
            "DstDomin":"www.test.com",
            "EndTime":1707118672,
            "AttackFailCount":80,
            "RuleID":12323,
            "StartTime":1707118672,
            "TotalAttackTimes":100,
            "AttackType":"Web attack",
            "AttackerIP":"1.1.1.1",
            "SrcIP":"1.1.1.1",
            "DstIPType":"EIP",
            "RuleNote":"Web attack",
            "DstIP":"2.2.2.2",
            "RelatedEcs":"...",
            "AttackSuccessCount":10
```

`}` `],`

```json
    "Success":true,
    "Module":"ndr***",
    "HttpStatusCode":200
```

`}` `XML` format

```xml
Content-Type:application/xml <DescribeAggAttackProcessResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <TotalCount>100</TotalCount>
    <PageSize>10</PageSize>
    <CurrentPage>1</CurrentPage>
    <FirstAttackTime>1707118672</FirstAttackTime>
    <FirstAttackedIP>2.2.2.2</FirstAttackedIP>
    <AttackProcessList>
        <StartTime>1707118672</StartTime>
        <EndTime>1707118672</EndTime>
        <SrcIP>1.1.1.1</SrcIP>
        <AttackerIP>1.1.1.1</AttackerIP>
        <AttackType>Web attack</AttackType>
        <RuleNote>Web attack</RuleNote>
        <RuleID>12323</RuleID>
        <DstIP>2.2.2.2</DstIP>
        <DstDomin>www.test.com</DstDomin>
        <DstIPType>EIP</DstIPType>
        <TotalAttackTimes>100</TotalAttackTimes>
        <AttackSuccessCount>10</AttackSuccessCount>
        <AttackFailCount>80</AttackFailCount>
        <AttackTryCount>10</AttackTryCount>
        <RelatedEcs>...</RelatedEcs>
    </AttackProcessList>
    <Success>true</Success>
    <Module>ndr***</Module>
    <HttpStatusCode>200</HttpStatusCode>
</DescribeAggAttackProcessResponse>
```

#### ExportAggAttackEventMergePcap

Exports the packet capture file of attacks.

**Authorization information**

| Operation | Access level | Resource type |
|---|---|---|
| yundun- cloudfirewall:ExportAggAttackE ventMergePcap | Write | acs:yundun-cloudfirewall:*: {#accountId}:* |

**Throttling**

You can call this operation up to 10 times per second per account. You can call this operation up to 100 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Lang | Strin g | Query | No | zh | The language. Valid values: zh and en. You can leave this parameter empty if it is not required for your business. |
| StartTime | Long | Query | No | 1706668721 | The beginning of the time range to query. |
| EndTime | Long | Query | No | 1706668721 | The end of the time range to query. |
| SrcIP | Strin g | Query | No | 10.x.x.x | The source IP address. |
| SrcPort | Strin g | Query | No | 80 | The source port. |
| Direction | Integ er | Query | No | 1 | The traffic direction. |
| Size | Integ er | Query | No | 100 | The number of entries to be exported. |
| AliUid | Long | Query | No | 123456789 | The user ID. |
| Module | Strin g | Query | No | dispatch rule _ | The name of the module. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Module | String | ndr*** | The name of the module. |
| TaskUUID | String | cfa13285-5330- 402e-xxx- 5075c12c6aa8 | The export task ID. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=ExportAggAttackEventMergePcap&RegionId=cnhangzhou&Lang=zh&StartTime=1706668721&EndTime=1706668721&SrcIP=10.x.x.x&SrcPort=80&Direct n=1&Size=100&AliUid=123456789&Module=dispatch_rule
```

Sample success responses `JSON` format

```
Content-Type:application/json
```

`{`

```json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "Module":"ndr***",
    "TaskUUID":"cfa13285-5330-402e-xxx-5075c12c6aa8"
```

`}` `XML` format

```xml
Content-Type:application/xml <ExportAggAttackEventMergePcapResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <Module>ndr***</Module>
    <TaskUUID>cfa13285-5330-402e-xxx-5075c12c6aa8</TaskUUID>
</ExportAggAttackEventMergePcapResponse>
```

#### DescribeAttackEventRecords

Queries the attack event records of an attacker.

**Authorization information**

| Operation | Access level | Resource type |
|---|---|---|
| yundun- cloudfirewall:DescribeAttackEv entRecords | Read | acs:yundun-cloudfirewall:*: {#accountId}:* |

**Throttling**

You can call this operation up to 10 times per second per account. You can call this operation up to 100 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Lang | Strin g | Query | No | zh | The language. Valid values: zh and en. You can leave this parameter empty if it is not required for your business. |
| AliUid | Long | Query | No | 1234567890 | The user ID. |
| StartTime | Long | Query | No | 1707118672 | The beginning of the time range to query. |
| EndTime | Long | Query | No | 1707118672 | The end of the time range to query. |
| AttackRes ult | Strin g | Query | No | 0 | The attack result. A value of 0 indicates that the attacker attempted an attack. A value of 1 indicates that the attack is successful. A value of -1 indicates that the attack has failed. |
| VulLevel | Strin g | Query | No | 1 | The threat level. A value of 1 indicates low risk. A value of 2 indicates medium risk. A value of 3 indicates high risk. |
| SrcIP | Strin g | Query | No | 1.1.1.1 | The IP address of the attacker. |
| Sort | Strin g | Query | No | 10 | The sorting method. A value of 1 indicates sorting by score. A value of 2 indicates sorting by time. |
| PageSize | Strin g | Query | No | 10 | The number of entries per page. |
| PageNo | Strin g | Query | No | 1 | The page number. |
| DeptAliUid | Strin g | Query | No | 1234567890 | The department ID. |

| loud Security and Respon | Network se | Detectio |   | Devel | oper Guide·API documenta io |
|---|---|---|---|---|---|

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| LinkType | Strin g | Query | No | 0 | The product on which the attack is detected. A value of 0 indicates Inter-connection Switch (ISW). A value of 1 indicates Customer Access Switch (CSW). A value of 2 indicates LVS Switch (LSW). A value of 3 indicates Elastic Network Interface (ENI). |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| DataList | Array |   |   |
| -SessionTime | Long | 1707118672 | The session time. |
| -SrcIP | String | 1.1.1.1 | The source IP address. |
| -AttackerIP | String | 1.1.1.1 | The IP address of the attacker. |
| -Direction | String | in | The traffic direction. Valid values: in and out. |
| -DstIP | String | 1.1.1.1 | The destination IP address. |
| -DstIPType | String | EIP | The type of the destination IP address. |
| -Host | String | 1.1.1.1 | The Host header. |
| -XFF | String | 1.1.1.1 | The X-Forwarded-For (XFF) header. |
| -DstPort | Integer | 80 | The destination port. |
| -RuleID | Long | 12323 | The rule ID. |
| -RuleType | String | Web attack | The type of the rule. |
| -RuleNote | String | Web attack | The description of the rule. |

| Developer Guide·A on | PI documentat |   | Cloud Security Network Detecti n and Respons |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| -VulLevel | String | 1 | The threat level. A value of 1 indicates low risk. A value of 2 indicates medium risk. A value of 3 indicates high risk. |
| -AttackResult | String | 0 | The attack result. A value of 0 indicates that the attacker attempted an attack. A value of 1 indicates that the attack is successful. A value of -1 indicates that the attack has failed. |
| -IPProtocol | String | tcp | The transport layer protocol. |
| -LocationZh | String | 北京 | The geographical location in Chinese. |
| -LocationEn | String | beijing | The geographical location in English. |
| -StartTime | Long | 1707118672 | The beginning of the time range to query. |
| -EndTime | Long | 1707118672 | The end of the time range to query. |
| -ScanTool | String | Nmap | The scanner. |
| -IntellLable | Integer | 1 | The threat intelligence label. |
| -Department | String | test | The department. |
| -LinkType | String | 0 | The product on which the attack is detected. A value of 0 indicates ISW. A value of 1 indicates CSW. A value of 2 indicates LSW. A value of 3 indicates ENI. |
| - DstRelatedECS | Map | ... | The associated Elastic Compute Service (ECS) instance. |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| TotalCount | Integer |   |   |
| PageSize | Integer |   |   |
| CurrentPage | Integer |   |   |

| Cloud Security Ne | twork Detectio |   | Developer Guide·API documenta |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| Success | Boolean | true | Indicates whether the HTTP request was successful. |
| Module | String | ndr*** | The name of the module. |
| HttpStatusCod e | Integer | 200 | The HTTP status code. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=DescribeAttackEventRecords&RegionId=cnhangzhou&Lang=zh&AliUid=1234567890&StartTime=1707118672&EndTime=1707118672&AttackResult=0 ulLevel=1&SrcIP=1.1.1.1&Sort=10&PageSize=10&PageNo=1&DeptAliUid=1234567890&LinkType=0
```

Sample success responses `JSON` format

```
Content-Type:application/json
```

`{`

```json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "TotalCount":"",
    "PageSize":"",
    "CurrentPage":"",
    "DataList":[
```

`{`

```json
            "DstRelatedECS":"...",
            "EndTime":1707118672,
            "LocationEn":"beijing",
            "RuleID":12323,
            "IPProtocol":"tcp",
            "StartTime":1707118672,
            "Host":"1.1.1.1",
            "RuleType":"Web attack",
            "DstPort":80,
            "AttackerIP":"1.1.1.1",
            "SrcIP":"1.1.1.1",
            "Direction":"in",
            "DstIPType":"EIP",
            "SessionTime":1707118672,
            "Department":"test",
            "ScanTool":"Nmap",
            "AttackResult":"0",
            "RuleNote":"Web attack",
            "IntellLable":1,
            "DstIP":"1.1.1.1",
            "XFF":"1.1.1.1",
            "LocationZh":"北京",
            "LinkType":"0",
            "VulLevel":"1"
```

`}` `],`

```json
    "Success":true,
    "Module":"ndr***",
    "HttpStatusCode":200
```

`}` `XML` format

```xml
Content-Type:application/xml <DescribeAttackEventRecordsResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <TotalCount></TotalCount>
    <PageSize></PageSize>
    <CurrentPage></CurrentPage>
    <DataList>
        <SessionTime>1707118672</SessionTime>
        <SrcIP>1.1.1.1</SrcIP>
        <AttackerIP>1.1.1.1</AttackerIP>
        <Direction>in</Direction>
        <DstIP>1.1.1.1</DstIP>
        <DstIPType>EIP</DstIPType>
        <Host>1.1.1.1</Host>
        <XFF>1.1.1.1</XFF>
        <DstPort>80</DstPort>
        <RuleID>12323</RuleID>
        <RuleType>Web attack</RuleType>
        <RuleNote>Web attack</RuleNote>
        <VulLevel>1</VulLevel>
        <AttackResult>0</AttackResult>
        <IPProtocol>tcp</IPProtocol>
        <LocationZh>北京</LocationZh>
        <LocationEn>beijing</LocationEn>
        <StartTime>1707118672</StartTime>
        <EndTime>1707118672</EndTime>
        <ScanTool>Nmap</ScanTool>
        <IntellLable>1</IntellLable>
        <Department>test</Department>
        <LinkType>0</LinkType>
        <DstRelatedECS>...</DstRelatedECS>
    </DataList>
    <Success>true</Success>
    <Module>ndr***</Module>
    <HttpStatusCode>200</HttpStatusCode>
</DescribeAttackEventRecordsResponse>
```

#### DescribeAggAttackEventList

Queries a list of attack events.

**Authorization information**

| Operation | Access level | Resource type |
|---|---|---|
| yundun- cloudfirewall:DescribeAggAttac kEventList | Read | acs:yundun-cloudfirewall:*: {#accountId}:* |

**Throttling**

You can call this operation up to 10 times per second per account. You can call this operation up to 100 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Lang | Strin g | Query | No | zh | The language. Valid values: zh and en. You can leave this parameter empty if it is not required for your business. |
| AliUid | Long | Query | No | 1234567890 | The user ID. |
| StartTime | Long | Query | No | 1707118672 | The beginning of the time range to query. |
| EndTime | Long | Query | No | 1707118672 | The end of the time range to query. |
| AttackRes ult | Strin g | Query | No | 0 | The attack result. A value of 0 indicates that the attacker attempted an attack. A value of 1 indicates that the attack is successful. A value of -1 indicates that the attack has failed. |
| VulLevel | Strin g | Query | No | 1 | The threat level. A value of 1 indicates low risk. A value of 2 indicates medium risk. A value of 3 indicates high risk. |
| SrcIP | Strin g | Query | No | 1.1.1.1 | The source IP address of the attack. |
| Sort | Strin g | Query | No | 10 | The sorting method. A value of 1 indicates sorting by score. A value of 2 indicates sorting by time. |

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| PageSize | Integ er | Query | No | 10 | The number of entries per page. |
| PageNo | Integ er | Query | No | 1 | The page number. |
| DeptAliUid | Strin g | Query | No | 1234567890 | The department ID. |
| LinkType | Strin g | Query | No | 0 | The product on which the attack is detected. A value of 0 indicates Inter-connection Switch (ISW). A value of 1 indicates Customer Access Switch (CSW). A value of 2 indicates LVS Switch (LSW). A value of 3 indicates Elastic Network Interface (ENI). |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| DataList | Array |   |   |
| -SrcIP | String | 1.1.1.1 | The source IP address. |
| -AttackerIP | String | 1.1.1.1 | The IP address of the attacker. |
| -LocationZh | String | 北京 | The geographical location in Chinese. |
| -LocationEn | String | beijing | The geographical location in English. |
| -Duration | String | 10 | The duration of the attack. Unit: seconds. |
| -StartTime | Long | 1707118672 | The start time of the attack. |
| -EndTime | Long | 1707118672 | The end time of the attack. |
| -ScanTool | String | Nmap | The scanner. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| -IntellLable | Integer | 1 | The threat intelligence label. |
| -AttackTimes | Integer | 100 | The number of attacks. |
| - AttackSuccess Count | Integer | 10 | The number of successful attacks. |
| - AttackFailCoun t | Integer | 10 | The number of failed attacks. |
| - AttackTryCoun t | Integer | 10 | The number of attack attempts. |
| -VulHighCount | Integer | 10 | The number of high-risk attacks. |
| -VulMidCount | Integer | 10 | The number of medium-risk attacks. |
| -VulLowCount | Integer | 10 | The number of low-risk attacks. |
| -SortScore | Long | 110 | The score for sorting. |
| -RuleInfo | Map |   | The hit rule. This parameter is discontinued. |
| -DstAddrInfo | Map |   | The destination IP address. This parameter is discontinued. |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| TotalCount | Integer | 100 | The total number of entries returned. |
| PageSize | Integer | 10 | The number of entries per page. |
| CurrentPage | Integer | 1 | The page number. |
| Success | Boolean | true | Indicates whether the HTTP request was successful. |
| Module | String | ndr*** | The name of the module. |

| Cloud Security Ne and Response | twork Detectio |   | Developer Guide·API documenta io |
|---|---|---|---|
| Parameter | Type | Example | Description |
| HttpStatusCod e | Integer | 200 | The HTTP status code. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=DescribeAggAttackEventList&RegionId=cnhangzhou&Lang=zh&AliUid=1234567890&StartTime=1707118672&EndTime=1707118672&AttackResult=0 ulLevel=1&SrcIP=1.1.1.1&Sort=10&PageSize=10&PageNo=1&DeptAliUid=1234567890&LinkType=0
```

Sample success responses `JSON` format

```
Content-Type:application/json
```

`{`

```json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "TotalCount":100,
    "PageSize":10,
    "CurrentPage":1,
    "DataList":[
```

`{`

```json
            "VulMidCount":10,
            "AttackTryCount":10,
            "AttackTimes":100,
            "EndTime":1707118672,
            "AttackFailCount":10,
            "LocationEn":"beijing",
            "VulHighCount":10,
            "StartTime":1707118672,
            "Duration":"10",
            "AttackerIP":"1.1.1.1",
            "SrcIP":"1.1.1.1",
            "VulLowCount":10,
            "DstAddrInfo":"",
            "ScanTool":"Nmap",
            "IntellLable":1,
            "LocationZh":"北京",
            "AttackSuccessCount":10,
            "RuleInfo":"",
            "SortScore":110
```

`}` `],`

```json
    "Success":true,
    "Module":"ndr***",
    "HttpStatusCode":200
```

`}` `XML` format

```xml
Content-Type:application/xml <DescribeAggAttackEventListResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <TotalCount>100</TotalCount>
    <PageSize>10</PageSize>
    <CurrentPage>1</CurrentPage>
    <DataList>
        <SrcIP>1.1.1.1</SrcIP>
        <AttackerIP>1.1.1.1</AttackerIP>
        <LocationZh>北京</LocationZh>
        <LocationEn>beijing</LocationEn>
        <Duration>10</Duration>
        <StartTime>1707118672</StartTime>
        <EndTime>1707118672</EndTime>
        <ScanTool>Nmap</ScanTool>
        <IntellLable>1</IntellLable>
        <AttackTimes>100</AttackTimes>
        <AttackSuccessCount>10</AttackSuccessCount>
        <AttackFailCount>10</AttackFailCount>
        <AttackTryCount>10</AttackTryCount>
        <VulHighCount>10</VulHighCount>
        <VulMidCount>10</VulMidCount>
        <VulLowCount>10</VulLowCount>
        <SortScore>110</SortScore>
        <RuleInfo></RuleInfo>
        <DstAddrInfo></DstAddrInfo>
    </DataList>
    <Success>true</Success>
    <Module>ndr***</Module>
    <HttpStatusCode>200</HttpStatusCode>
</DescribeAggAttackEventListResponse>
```

**5.4.5.**

#### DescribeAggAttackEventMergePcapCount

Queries the number of attack evidence packets.

**Authorization information**

| Operation | Access level | Resource type |
|---|---|---|
| yundun- cloudfirewall:DescribeAggAttac kEventMergePcapCount | Read | acs:yundun-cloudfirewall:*: {#accountId}:* |

**Throttling**

You can call this operation up to 10 times per second per account. You can call this operation up to 100 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Lang | Strin g | Query | No | zh | The language. Valid values: zh and en. You can leave this parameter empty if it is not required for your business. |
| StartTime | Long | Query | No | 1707118672 | The beginning of the time range to query. |
| EndTime | Long | Query | No | 1707118672 | The end of the time range to query. |
| SrcIP | Strin g | Query | No | 1.1.1.1 | The source IP address of the attack. |
| SrcPort | Strin g | Query | No | 8080 | The source port of the attack. |
| Direction | Integ er | Query | No | 1 | The traffic direction. A value of 1 indicates inbound traffic. A value of 2 indicates outbound traffic. |
| AliUid | Long | Query | No | 1234567890 | The user ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Module | String | ndr*** | The name of the module. |
| TotalCount | String | 10 | The number of attack packets. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=DescribeAggAttackEventMergePcapCount&RegionId=cn-hangzhou&La ng=zh&StartTime=1707118672&EndTime=1707118672&SrcIP=1.1.1.1&SrcPort=8080&Direction=1&AliU =1234567890
```

Sample success responses `JSON` format

```
Content-Type:application/json
```

`{`

```json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "Module":"ndr***",
    "TotalCount":"10"
```

`}` `XML` format

```xml
Content-Type:application/xml <DescribeAggAttackEventMergePcapCountResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <Module>ndr***</Module>
    <TotalCount>10</TotalCount>
</DescribeAggAttackEventMergePcapCountResponse>
```

#### ExportAttackEventPcap

Exports the packet capture file of attack logs.

**Authorization information**

| Operation | Access level | Resource type |
|---|---|---|
| yundun- cloudfirewall:ExportAttackEvent Pcap | Write | acs:yundun-cloudfirewall:*: {#accountId}:* |

**Throttling**

You can call this operation up to 10 times per second per account. You can call this operation up to 100 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Lang | Strin g | Query | No | zh | The language. Valid values: zh and en. You can leave this parameter empty if it is not required for your business. |
| AliUid | Long | Query | No | 123456789 | The user ID. |
| StartTime | Long | Query | No | 1706668721 | The beginning of the time range to query. |
| EndTime | Long | Query | No | 1706668721 | The end of the time range to query. |
| AttackRes ult | Strin g | Query | No | 0 | The attack result. A value of 0 indicates that the attack is under review. A value of 1 indicates that the attack is successful. A value of 2 indicates that the attacker attempted an attack. A value of 3 indicates that the system has been compromised. A value of 4 indicates that the attack has failed. |
| VulLevel | Strin g | Query | No | 1 | The risk level. A value of 1 indicates low risk. A value of 2 indicates medium risk. A value of 3 indicates high risk. |
| SrcIP | Strin g | Query | No | 10.x.x.x | The source IP address. |
| SrcPort | Strin g | Query | No | 80 | The source port. |

| Developer Gui on | de·API d | ocumentat |   | Cloud | Security Network Detecti n and Respons |
|---|---|---|---|---|---|

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| DstIP | Strin g | Query | No | 10.x.x.x | The destination IP address. |
| DstPort | Strin g | Query | No | 80 | The destination port. |
| AttackTyp e | Strin g | Query | No | xss | The attack type. |
| RuleID | Strin g | Query | No | 65535 | The rule ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Module | String | ndr*** | The name of the module. |
| PcapName | String | test.cap | The name of the file to which results are exported. |
| PcapUrl | String | https://xxx.com | The download URL of the file. |
| TaskUUID | String | cfa13285-5330- 402e-xxx- 5075c12c6aa8 | The export task ID. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=ExportAttackEventPcap&RegionId=cnhangzhou&Lang=zh&AliUid=123456789&StartTime=1706668721&EndTime=1706668721&AttackResult=0& lLevel=1&SrcIP=10.x.x.x&SrcPort=80&DstIP=10.x.x.x&DstPort=80&AttackType=xss&RuleID=65535
```

Sample success responses `JSON` format

```
Content-Type:application/json
```

`{`

```json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "Module":"ndr***",
    "PcapName":"test.cap",
    "PcapUrl":"https://xxx.com",
    "TaskUUID":"cfa13285-5330-402e-xxx-5075c12c6aa8"
```

`}` `XML` format

```xml
Content-Type:application/xml <ExportAttackEventPcapResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <Module>ndr***</Module>
    <PcapName>test.cap</PcapName>
    <PcapUrl>https://xxx.com</PcapUrl>
    <TaskUUID>cfa13285-5330-402e-xxx-5075c12c6aa8</TaskUUID>
</ExportAttackEventPcapResponse>
```

#### DescribeExportMergePcapTaskByUuid

Asynchronously queries the information about a download task for the aggregated packet capture file.

**Authorization information**

| Operation | Access level | Resource type |
|---|---|---|
| yundun- cloudfirewall:DescribeExportMe rgePcapTaskByUuid | Read | acs:yundun-cloudfirewall:*: {#accountId}:* |

**Throttling**

You can call this operation up to 10 times per second per account. You can call this operation up to 100 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Lang | Strin g | Query | No | zh | The language. Valid values: zh and en. You can leave this parameter empty if it is not required for your business. |
| TaskUUID | Strin g | Query | No | d5b969bf-cd21-4dd0- 84ff-******* | The download task UUID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Module | String | ndr*** | The name of the module. |
| TaskUUID | String | d5b969bf-cd21- 4dd0-84ff-******* | The download task UUID. |
| TaskStatus | Integer | 1 | The status of the download task. A value of 0 indicates that the task is in progress. A value of 1 indicates that the task is successful. |
| FileUrl | String | https://test.com | The download URL of the file. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=DescribeExportMergePcapTaskByUuid&RegionId=cnhangzhou&Lang=zh&TaskUUID=d5b969bf-cd21-4dd0-84ff-*******
```

Sample success responses `JSON` format

```
Content-Type:application/json
```

`{`

```json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "Module":"ndr***",
    "TaskUUID":"d5b969bf-cd21-4dd0-84ff-*******",
    "TaskStatus":1,
    "FileUrl":"https://test.com"
```

`}` `XML` format

```xml
Content-Type:application/xml <DescribeExportMergePcapTaskByUuidResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <Module>ndr***</Module>
    <TaskUUID>d5b969bf-cd21-4dd0-84ff-*******</TaskUUID>
    <TaskStatus>1</TaskStatus>
    <FileUrl>https://test.com</FileUrl>
</DescribeExportMergePcapTaskByUuidResponse>
```

### Threat detection

#### Threat detection

##### AddCustomTag

Adds a custom tag based on threat detection logs.

**Authorization information**

| Operation | Access level | Resource type |
|---|---|---|
| yundun- cloudfirewall:AddCustomTag | Write | acs:yundun-cloudfirewall:*: {#accountId}:* |

**Throttling**

You can call this operation up to 10 times per second per account. You can call this operation up to 100 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Lang | Strin g | Query | No | zh | The language. Valid values: zh and en. You can leave this parameter empty if it is not required for your business. |
| AliUid | Long | Query | No | 1234567890 | The user ID. |
| Tag | Strin g | Query | No | test | The tag that you want to add. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Success | Boolean | true | Indicates whether the HTTP request was successful. |
| Module | String | ndr*** | The name of the module. |
| HttpStatusCod e | Integer | 200 | The HTTP status code. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=AddCustomTag&RegionId=cnhangzhou&Lang=zh&AliUid=1234567890&Tag=test
```

Sample success responses `JSON` format

```
Content-Type:application/json
```

`{`

```json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "Success":true,
    "Module":"ndr***",
    "HttpStatusCode":200
```

`}` `XML` format

```xml
Content-Type:application/xml <AddCustomTagResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <Success>true</Success>
    <Module>ndr***</Module>
    <HttpStatusCode>200</HttpStatusCode>
</AddCustomTagResponse>
```

##### ExportAttackRecordsPcap

Downloads the packet capture file of attack logs.

**Authorization information**

| Operation | Access level | Resource type |
|---|---|---|
| yundun- cloudfirewall:ExportAttackRecor dsPcap | Write | acs:yundun-cloudfirewall:*: {#accountId}:* |

**Throttling**

You can call this operation up to 10 times per second per account. You can call this operation up to 100 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Lang | Strin g | Query | No | zh | The language. Valid values: zh and en. You can leave this parameter empty if it is not required for your business. |
| StartTime | Long | Query | No | 1706668721 | The beginning of the time range to query. |
| EndTime | Long | Query | No | 1706668721 | The end of the time range to query. |

| Developer Gui | de·API d | ocumentat |   | Cloud | Security Network Detecti |
|---|---|---|---|---|---|

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| DstIP | Strin g | Query | No | 10.x.x.x | The destination IP address. |
| SrcIP | Strin g | Query | No | 10.x.x.x | The source IP address. |
| AliUid | Long | Query | No | 123456789 | The user ID. |
| HTTPCode | Integ er | Query | No | 200 | The HTTP status code. |
| AttackRes ult | Strin g | Query | No | 0 | The attack result. A value of 0 indicates that the attack is under review. A value of 1 indicates that the attack is successful. A value of 2 indicates that the attacker attempted an attack. A value of 3 indicates that the system has been compromised. A value of 4 indicates that the attack has failed. |
| RuleID | Integ er | Query | No | 123 | The rule ID. |
| Origin | Integ er | Query | No | 1 | The source of the rule. A value of 0 indicates Intrusion detection system (IDS). A value of 1 indicates web IDS. |
| DstPort | Integ er | Query | No | 80 | The destination port. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| PcapName | String | test.cap | The name of the file. |
| PcapUrl | String | https://xxx.com | The download URL of the file. |

| Cloud Security Ne and Response | twork Detectio |   | Developer Guide·API documenta io |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| TaskUUID | String | cfa13285-5330- 402e-xxx- 5075c12c6aa8 | The export task ID. |
| Module | String | ndr*** | The name of the module. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=ExportAttackRecordsPcap&RegionId=cnhangzhou&Lang=zh&StartTime=1706668721&EndTime=1706668721&DstIP=10.x.x.x&SrcIP=10.x.x.x&Al id=123456789&HTTPCode=200&AttackResult=0&RuleID=123&Origin=1&DstPort=80
```

Sample success responses `JSON` format

```
Content-Type:application/json
```

`{`

```json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "PcapName":"test.cap",
    "PcapUrl":"https://xxx.com",
    "TaskUUID":"cfa13285-5330-402e-xxx-5075c12c6aa8",
    "Module":"ndr***"
```

`}` `XML` format

```xml
Content-Type:application/xml <ExportAttackRecordsPcapResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <PcapName>test.cap</PcapName>
    <PcapUrl>https://xxx.com</PcapUrl>
    <TaskUUID>cfa13285-5330-402e-xxx-5075c12c6aa8</TaskUUID>
    <Module>ndr***</Module>
</ExportAttackRecordsPcapResponse>
```

##### DescribeAggAttackTopIPRecords

Queries the top five IP addresses from which most attacks are launched.

**Authorization information**

| Operation | Access level | Resource type |
|---|---|---|
| yundun- cloudfirewall:DescribeAggAttac kTopIPRecords | Read | acs:yundun-cloudfirewall:*: {#accountId}:* |

**Throttling**

You can call this operation up to 10 times per second per account. You can call this operation up to 100 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Lang | Strin g | Query | No | zh | The language. Valid values: zh and en. You can leave this parameter empty if it is not required for your business. |
| StartTime | Long | Query | No | 1707118672 | The beginning of the time range to query. |
| EndTime | Long | Query | No | 1707118672 | The end of the time range to query. |
| DstIP | Strin g | Query | No | 1.1.1.1 | The destination IP address. |
| SrcIP | Strin g | Query | No | 1.1.1.1 | The source IP address. |
| AliUid | Long | Query | No | 1234567890 | The user ID. |
| HTTPCode | Integ er | Query | No | 200 | The HTTP status code. |
| XFF | Strin g | Query | No | 2.2.2.2 | The X-Forwarded-For (XFF) header. |

| loud Security | Network | Detectio |   | Devel | oper Guide·API documenta |
|---|---|---|---|---|---|

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Host | Strin g | Query | No | 2.2.2.2 | The Host header. |
| AttackRes ult | Strin g | Query | No | 0 | The attack result. A value of 0 indicates that the attacker attempted an attack. A value of 1 indicates that the attack is successful. A value of -1 indicates that the attack has failed. |
| RuleID | Long | Query | No | 12323 | The hit rule ID. |
| Origin | Strin g | Query | No | 0 | The source of the rule. A value of 0 indicates Intrusion detection system (IDS). A value of 1 indicates web IDS. |
| RuleType | Strin g | Query | No | Web attack | The type of the rule. |
| VulLevel | Strin g | Query | No | 1 | The threat level. A value of 1 indicates low risk. A value of 2 indicates medium risk. A value of 3 indicates high risk. |
| DepAliUid | Strin g | Query | No | 1234567890 | The department ID. |
| Label | Strin g | Query | No | test | The label. |

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| IPType | Strin g | Query | No | 1 | The type of the service to which the IP address belongs. A value of 0 indicates others. A value of 1 indicates Web Application Firewall (WAF). A value of 2 indicates Server Load Balancer (SLB). A value of 3 indicates Elastic IP Address (EIP). A value of 4 indicates Elastic Compute Service (ECS). |
| ProtectSta tus | Strin g | Query | No | 0 | The protection status. A value of 0 indicates that the attack is not handled. A value of 1 indicates that the attack is blocked. A value of 2 indicates that the IP address is added to the whitelist. A value of 3 indicates that the attack is ignored. |
| LinkType | Strin g | Query | No | 0 | The product on which the attack is detected. A value of 0 indicates Inter-connection Switch (ISW). A value of 1 indicates Customer Access Switch (CSW). A value of 2 indicates LVS Switch (LSW). A value of 3 indicates Elastic Network Interface (ENI). |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| DataList | Array |   |   |
| -IP | String | 1.1.1.1 | The IP address. |
| -Count | Integer | 100 | The number of attacks. |
| -Type | String |   | The attack type. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| TotalCount | Integer | 100 | The total number of entries returned. |
| TimeOut | Boolean | false | Indicates whether the request timed out. Valid values: true and false. |
| Success | Boolean | true | Indicates whether the HTTP request was successful. |
| Module | String | ndr*** | The name of the module. |
| HttpStatusCod e | Integer | 200 | The HTTP status code. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=DescribeAggAttackTopIPRecords&RegionId=cnhangzhou&Lang=zh&StartTime=1707118672&EndTime=1707118672&DstIP=1.1.1.1&SrcIP=1.1.1.1&AliU =1234567890&HTTPCode=200&XFF=2.2.2.2&Host=2.2.2.2&AttackResult=0&RuleID=12323&Origin=0&Ru Type=Web attack&VulLevel=1&DepAliUid=1234567890&Label=test&IPType=1&ProtectStatus=0&LinkType=0
```

Sample success responses `JSON` format

```
Content-Type:application/json
```

`{`

```json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "TotalCount":100,
    "TimeOut":false,
    "DataList":[
```

`{`

```json
            "Type":"",
            "IP":"1.1.1.1",
            "Count":100
```

`}` `],`

```json
    "Success":true,
    "Module":"ndr***",
    "HttpStatusCode":200
```

`}` `XML` format

```xml
Content-Type:application/xml <DescribeAggAttackTopIPRecordsResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <TotalCount>100</TotalCount>
    <TimeOut>false</TimeOut>
    <DataList>
        <IP>1.1.1.1</IP>
        <Count>100</Count>
        <Type></Type>
    </DataList>
    <Success>true</Success>
    <Module>ndr***</Module>
    <HttpStatusCode>200</HttpStatusCode>
</DescribeAggAttackTopIPRecordsResponse>
```

##### DescribeDeptInfo

Queries a list of departments.

**Authorization information**

| Operation | Access level | Resource type |
|---|---|---|
| yundun- cloudfirewall:DescribeDeptInfo | Read | acs:yundun-cloudfirewall:*: {#accountId}:* |

**Throttling**

You can call this operation up to 10 times per second per account. You can call this operation up to 100 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Lang | Strin g | Query | No | zh | The language. Valid values: zh and en. You can leave this parameter empty if it is not required for your business. |

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| AliUid | Long | Query | No | 1234567890 | The user ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| DataList | Array |   |   |
| -DeptName | String | test | The name of the department. |
| -AliUid | Long | 1234567890 | The department ID. |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Success | Boolean | true | Indicates whether the HTTP request was successful. |
| Module | String | ndr*** | The name of the module. |
| HttpStatusCod e | Integer | 200 | The HTTP status code. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=DescribeDeptInfo&RegionId=cnhangzhou&Lang=zh&AliUid=1234567890
```

Sample success responses `JSON` format

```
Content-Type:application/json
```

`{`

```json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "DataList":[
```

`{`

```json
            "DeptName":"test",
            "AliUid":1234567890
```

`}` `],`

```json
    "Success":true,
    "Module":"ndr***",
    "HttpStatusCode":200
```

`}` `XML` format

```xml
Content-Type:application/xml <DescribeDeptInfoResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <DataList>
        <DeptName>test</DeptName>
        <AliUid>1234567890</AliUid>
    </DataList>
    <Success>true</Success>
    <Module>ndr***</Module>
    <HttpStatusCode>200</HttpStatusCode>
</DescribeDeptInfoResponse>
```

##### AddIDSWhiteRule

You can call the AddIDSWhiteRule operation to add a threat detection whitelist to ignore alert logs for known threats.

**Authorization information**

| Operation | Access level | Resource type |
|---|---|---|
| yundun- cloudfirewall:AddIDSWhiteRule | Write | acs:yundun-cloudfirewall:*: {#accountId}:* |

**Throttling**

Single user call frequency: 10 queries per second (QPS). API call frequency: 100 QPS.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Lang | Strin g | Query | No | zh | The language of the response. Valid values: zh for Chinese and en for English. This parameter is not required. |
| IPList | Strin g | Query | No | 1.1.1.1,2.2.2.2 | A list of one or more IP addresses. |
| SrcIP | Strin g | Query | No | 1.1.1.1 | The source IP address. |
| DstIP | Strin g | Query | No | 1.1.1.1 | The destination IP address. |
| RuleNote | Strin g | Query | No | code execution | The name of the rule. |
| Payload | Strin g | Query | No | code execution | The payload. |
| StartTime | Long | Query | No | 1704335379 | The time when the rule takes effect. |
| EndTime | Long | Query | No | 1704335379 | The time when the rule expires. |
| AliUid | Long | Query | No | 1234567890 | The UID of the user. |
| User | Strin g | Query | No | user | The user who performs the operation. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The ID of the request. Alibaba Cloud generates this unique ID for each request. Use this ID to troubleshoot issues. |
| Success | Boolean | true | Indicates whether the request was successful. |

| Developer Guide·A on | PI documentat |   | Cloud Security Network Detecti n and Respons |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| Module | String | ndr*** | The name of the module. |
| HttpStatusCod e | Integer | 200 | The HTTP status code. |

**Examples**

Sample request

```
https://[Endpoint]/?Action=AddIDSWhiteRule&RegionId=cnhangzhou&Lang=zh&IPList=1.1.1.1,2.2.2.2&SrcIP=1.1.1.1&DstIP=1.1.1.1&RuleNote=code execu tion&Payload=code execution&StartTime=1704335379&EndTime=1704335379&AliUid=1234567890&User=user
```

Sample response `JSON` format

```
Content-Type:application/json
```

`{`

```json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "Success":true,
    "Module":"ndr***",
    "HttpStatusCode":200
```

`}` `XML` format

```xml
Content-Type:application/xml <AddIDSWhiteRuleResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <Success>true</Success>
    <Module>ndr***</Module>
    <HttpStatusCode>200</HttpStatusCode>
</AddIDSWhiteRuleResponse>
```

##### DescribeExportTaskByUuid

Asynchronously queries the information about an exported file download task.

**Authorization information**

| Operation | Access level | Resource type |
|---|---|---|
| yundun- cloudfirewall:DescribeExportTas kByUuid | Read | acs:yundun-cloudfirewall:*: {#accountId}:* |

**Throttling**

You can call this operation up to 10 times per second per account. You can call this operation up to 100 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Lang | Strin g | Query | No | zh | The language. Valid values: zh and en. You can leave this parameter empty if it is not required for your business. |
| TaskUUID | Strin g | Query | No | d5b969bf-cd21-4dd0- 84ff-******* | The download task UUID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Module | String | ndr*** | The name of the module. |
| TaskUUID | String | d5b969bf-cd21- 4dd0-84ff-******* | The download task UUID. |
| TaskStatus | Integer | 1 | The status of the download task. A value of 0 indicates that the task is in progress. A value of 1 indicates that the task is successful. |
| FileUrl | String | https://test.com | The download URL of the file. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=DescribeExportTaskByUuid&RegionId=cnhangzhou&Lang=zh&TaskUUID=d5b969bf-cd21-4dd0-84ff-*******
```

Sample success responses `JSON` format

```
Content-Type:application/json
```

`{`

```json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "Module":"ndr***",
    "TaskUUID":"d5b969bf-cd21-4dd0-84ff-*******",
    "TaskStatus":1,
    "FileUrl":"https://test.com"
```

`}` `XML` format

```xml
Content-Type:application/xml <DescribeExportTaskByUuidResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <Module>ndr***</Module>
    <TaskUUID>d5b969bf-cd21-4dd0-84ff-*******</TaskUUID>
    <TaskStatus>1</TaskStatus>
    <FileUrl>https://test.com</FileUrl>
</DescribeExportTaskByUuidResponse>
```

##### DeleteIDSWhiteRules

Removes rules from the whitelist for threat detection.

**Authorization information**

| Operation | Access level | Resource type |
|---|---|---|
| yundun- cloudfirewall:DeleteIDSWhiteRu les | Write | acs:yundun-cloudfirewall:*: {#accountId}:* |

**Throttling**

You can call this operation up to 10 times per second per account. You can call this operation up to 100 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Lang | Strin g | Query | No | zh | The language. Valid values: zh and en. You can leave this parameter empty if it is not required for your business. |
| User | Strin g | Query | No | user | The user. |
| RuleIDList | Strin g | Query | No | 1024,1025 | The IDs of the rules that you want to remove. You can remove multiple rules at a time. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Success | Boolean | true | Indicates whether the HTTP request was successful. |
| Module | String | ndr*** | The name of the module. |
| HttpStatusCod e | Integer | 200 | The HTTP status code. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=DeleteIDSWhiteRules&RegionId=cnhangzhou&Lang=zh&User=user&RuleIDList=1024,1025
```

Sample success responses `JSON` format

```
Content-Type:application/json
```

`{`

```json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "Success":true,
    "Module":"ndr***",
    "HttpStatusCode":200
```

`}` `XML` format

```xml
Content-Type:application/xml <DeleteIDSWhiteRulesResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <Success>true</Success>
    <Module>ndr***</Module>
    <HttpStatusCode>200</HttpStatusCode>
</DeleteIDSWhiteRulesResponse>
```

##### DescribeAggAttackTopStatistics

Queries the statistics on the top five attackers that launch the most attacks.

**Authorization information**

| Operation | Access level | Resource type |
|---|---|---|
| yundun- cloudfirewall:DescribeAggAttac kTopStatistics | Read | acs:yundun-cloudfirewall:*: {#accountId}:* |

**Throttling**

You can call this operation up to 10 times per second per account. You can call this operation up to 100 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Lang | Strin g | Query | No | zh | The language. Valid values: zh and en. You can leave this parameter empty if it is not required for your business. |
| AliUid | Long | Query | No | 1234567890 | The user ID. |
| StartTime | Long | Query | No | 1707118672 | The beginning of the time range to query. |
| EndTime | Long | Query | No | 1707118672 | The end of the time range to query. |
| AttackRes ult | Strin g | Query | No | 0 | The attack result. A value of 0 indicates that the attacker attempted an attack. A value of 1 indicates that the attack is successful. A value of -1 indicates that the attack has failed. |
| VulLevel | Strin g | Query | No | 1 | The threat level. A value of 1 indicates low risk. A value of 2 indicates medium risk. A value of 3 indicates high risk. |
| SrcIP | Strin g | Query | No | 1.1.1.1 | The source IP address. |
| DeptAliUid | Strin g | Query | No | 1234567890 | The department ID. |
| LinkType | Strin g | Query | No | 0 | The product on which the attack is detected. A value of 0 indicates Inter-connection Switch (ISW). A value of 1 indicates Customer Access Switch (CSW). A value of 2 indicates LVS Switch (LSW). A value of 3 indicates Elastic Network Interface (ENI). |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| AttackDomain Statistics | Array |   |   |
| -AttackDomain | String | www.test.com | The domain name that is attacked. |
| -AttackTimes | Integer | 10 | The number of attacks. |
| AttackIPStatisti cs | Array |   |   |
| -AttackIP | String | 1.1.1.1 | The IP address. |
| -AttackTimes | Integer | 10 | The number of attacks. |
| -AttackIPType | String | 1 | The type of the service to which the IP address belongs. A value of 0 indicates others. A value of 1 indicates Web Application Firewall (WAF). A value of 2 indicates Server Load Balancer (SLB). A value of 3 indicates Elastic IP Address (EIP). A value of 4 indicates Elastic Compute Service (ECS). |
| AttackResultSt atistics | Array |   |   |
| -AttackResult | String | 0 | The attack result. A value of 0 indicates that the attacker attempted an attack. A value of 1 indicates that the attack is successful. A value of -1 indicates that the attack has failed. |
| -AttackTimes | Integer | 10 | The number of attacks. |
| VulLevelStatist ics | Array |   |   |
| -VulLevel | String | 1 | The threat level. A value of 1 indicates low risk. A value of 2 indicates medium risk. A value of 3 indicates high risk. |
| -AttackTimes | Integer | 10 | The number of attacks. |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Module | String | ndr*** | The name of the module. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=DescribeAggAttackTopStatistics&RegionId=cnhangzhou&Lang=zh&AliUid=1234567890&StartTime=1707118672&EndTime=1707118672&AttackResult=0 ulLevel=1&SrcIP=1.1.1.1&DeptAliUid=1234567890&LinkType=0
```

Sample success responses `JSON` format

```
Content-Type:application/json
```

`{`

```json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "Module":"ndr***",
    "AttackDomainStatistics":[
```

`{`

```json
            "AttackTimes":10,
            "AttackDomain":"www.test.com"
```

`}` `],`

```json
    "AttackIPStatistics":[
```

`{`

```json
            "AttackTimes":10,
            "AttackIPType":"1",
            "AttackIP":"1.1.1.1"
```

`}` `],`

```json
    "AttackResultStatistics":[
```

`{`

```json
            "AttackTimes":10,
            "AttackResult":"0"
```

`}` `],`

```json
    "VulLevelStatistics":[
```

`{`

```json
            "AttackTimes":10,
            "VulLevel":"1"
```

`}` `]` `}` `XML` format

```xml
Content-Type:application/xml <DescribeAggAttackTopStatisticsResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <Module>ndr***</Module>
    <AttackDomainStatistics>
        <AttackDomain>www.test.com</AttackDomain>
        <AttackTimes>10</AttackTimes>
    </AttackDomainStatistics>
    <AttackIPStatistics>
        <AttackIP>1.1.1.1</AttackIP>
        <AttackTimes>10</AttackTimes>
        <AttackIPType>1</AttackIPType>
    </AttackIPStatistics>
    <AttackResultStatistics>
        <AttackResult>0</AttackResult>
        <AttackTimes>10</AttackTimes>
    </AttackResultStatistics>
    <VulLevelStatistics>
        <VulLevel>1</VulLevel>
        <AttackTimes>10</AttackTimes>
    </VulLevelStatistics>
</DescribeAggAttackTopStatisticsResponse>
```

##### DescribeAttackRecordList

Queries the attack log details for threat detection.

**Authorization information**

| Operation | Access level | Resource type |
|---|---|---|
| yundun- cloudfirewall:DescribeAttackRe cordList | Read | acs:yundun-cloudfirewall:*: {#accountId}:* |

**Throttling**

You can call this operation up to 10 times per second per account. You can call this operation up to 100 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Lang | Strin g | Query | No | zh | The language. Valid values: zh and en. You can leave this parameter empty if it is not required for your business. |
| CurrentPa ge | Strin g | Query | No | 1 | The page number. |
| PageSize | Strin g | Query | No | 10 | The number of entries per page. |
| StartTime | Long | Query | No | 1707118672 | The beginning of the time range to query. |
| EndTime | Long | Query | No | 1707118672 | The end of the time range to query. |
| DstIP | Strin g | Query | No | 1.1.1.1 | The destination IP address. |
| SrcIP | Strin g | Query | No | 1.1.1.1 | The source IP address. |
| AliUid | Long | Query | No | 1234567890 | The user ID. |
| HTTPCode | Integ er | Query | No | 200 | The HTTP status code. |
| AttackRes ult | Strin g | Query | No | 0 | The attack result. A value of 0 indicates that the attacker attempted an attack. A value of 1 indicates that the attack is successful. A value of -1 indicates that the attack has failed. |
| RuleID | Long | Query | No | 12323 | The hit rule ID. |
| Origin | Integ er | Query | No | 0 | The source of the rule. A value of 0 indicates Intrusion detection system (IDS). A value of 1 indicates web IDS. |

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| DstPort | Integ er | Query | No | 8080 | The destination port. |
| Host | Strin g | Query | No | 1.1.1.1 | The HOST header. |
| Count | Integ er | Query | No | 10 | The number of entries returned. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| DataList | Array |   |   |
| -SrcIP | String | 1.1.1.1 | The source IP address. |
| -DstIP | String | 1.1.1.1 | The destination IP address. |
| -SessionTime | Long | 1707118672 | The session time. |
| -Department | String | test | The name of the department. |
| -RuleType | String | Web attack | The type of the rule. |
| -RuleName | String | Web attack | The name of the rule. |
| -VulLevel | String | 1 | The threat level. A value of 1 indicates low risk. A value of 2 indicates medium risk. A value of 3 indicates high risk. |
| -HTTPCode | Integer | 200 | The HTTP status code. |
| -AttackResult | String | 0 | The attack result. A value of 0 indicates that the attacker attempted an attack. A value of 1 indicates that the attack is successful. A value of -1 indicates that the attack has failed. |
| -XFF | String | 2.2.2.2 | The X-Forwarded-For (XFF) header. |
| -RuleID | Long | 12323 | The hit rule ID. |

| C n | loud Security Net and Response | work Detectio |   | Developer Guide·API documenta io | t n |
|---|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| -MatchData | String | GET /aaa.jsp? test=JavaSCript:ale rt(123) HTTP/1.1*** | The payload. |
| -RequsetData | String | GET /aaa.jsp? test=JavaSCript:ale rt(123) HTTP/1.1*** | The request data. |
| - ResponseData | String | 404 | The response data. |
| -HTTPType | Integer | 1 | The type of the HTTP rule. A value of 0 indicates a Layer 4 detection rule. A value of 1 indicates a Layer 7 detection rule. |
| -DstPort | String | 8080 | The destination port. |
| -SrcPort | String | 8080 | The source port. |
| -Tags | String | test | The tags. |
| -IPVersion | String | 4 | The IP version. A value of 4 indicates IPv4. A value of 6 indicates IPv6. |
| -IPProtol | String | tcp | The transport layer protocol. |
| - RequsetLengt h | Integer | 100 | The request length. |
| - ResponseLeng th | Integer | 100 | The response length. |
| -Origin | String | 0 | The source of the rule. A value of 0 indicates Intrusion detection system (IDS). A value of 1 indicates web IDS. |
| -LinkType | String | 0 | The product on which the attack is detected. A value of 0 indicates Inter- connection Switch (ISW). A value of 1 indicates Customer Access Switch (CSW). A value of 2 indicates LVS Switch (LSW). A value of 3 indicates Elastic Network Interface (ENI). |
| -RelatedEcs | Map | ... | The associated Elastic Compute Service (ECS) instance. |

| i | Developer Guide·A on | PI documentat |   | Cloud Security Network Detecti n and Respons | o e |
|---|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| TotalCount | Integer | 100 | The total number of entries returned. |
| PageSize | Integer | 10 | The number of entries per page. |
| CurrentPage | Integer | 1 | The page number. |
| Success | Boolean | true | Indicates whether the HTTP request was successful. |
| Module | String | ndr*** | The name of the module. |
| HttpStatusCod e | Integer | 200 | The HTTP status code. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=DescribeAttackRecordList&RegionId=cnhangzhou&Lang=zh&CurrentPage=1&PageSize=10&StartTime=1707118672&EndTime=1707118672&DstIP= 1.1.1&SrcIP=1.1.1.1&AliUid=1234567890&HTTPCode=200&AttackResult=0&RuleID=12323&Origin=0&D Port=8080&Host=1.1.1.1&Count=10
```

Sample success responses `JSON` format

```
Content-Type:application/json
```

`{`

```json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "TotalCount":100,
    "PageSize":10,
    "CurrentPage":1,
    "DataList":[
```

`{`

```json
            "Origin":"0",
            "Department":"test",
            "AttackResult":"0",
            "XFF":"2.2.2.2",
            "RuleName":"Web attack",
            "Tags":"test",
            "VulLevel":"1",
            "ResponseLength":100,
            "SrcPort":"8080",
            "HTTPType":1,
            "RuleID":12323,
            "ResponseData":"404",
            "RuleType":"Web attack",
            "HTTPCode":200,
            "DstPort":"8080",
            "MatchData":"GET /aaa.jsp?test=JavaSCript:alert(123) HTTP/1.1***",
            "SrcIP":"1.1.1.1",
            "IPProtol":"tcp",
            "SessionTime":1707118672,
            "RequsetData":"GET /aaa.jsp?test=JavaSCript:alert(123) HTTP/1.1***",
            "DstIP":"1.1.1.1",
            "RelatedEcs":"...",
            "LinkType":"0",
            "RequsetLength":100,
            "IPVersion":"4"
```

`}` `],`

```json
    "Success":true,
    "Module":"ndr***",
    "HttpStatusCode":200
```

`}` `XML` format

```xml
Content-Type:application/xml <DescribeAttackRecordListResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <TotalCount>100</TotalCount>
    <PageSize>10</PageSize>
    <CurrentPage>1</CurrentPage>
    <DataList>
        <SrcIP>1.1.1.1</SrcIP>
        <DstIP>1.1.1.1</DstIP>
        <SessionTime>1707118672</SessionTime>
        <Department>test</Department>
        <RuleType>Web attack</RuleType>
        <RuleName>Web attack</RuleName>
        <VulLevel>1</VulLevel>
        <HTTPCode>200</HTTPCode>
        <AttackResult>0</AttackResult>
        <XFF>2.2.2.2</XFF>
        <RuleID>12323</RuleID>
        <MatchData>GET /aaa.jsp?test=JavaSCript:alert(123) HTTP/1.1***</MatchData>
        <RequsetData>GET /aaa.jsp?test=JavaSCript:alert(123) HTTP/1.1***</RequsetData>
        <ResponseData>404</ResponseData>
        <HTTPType>1</HTTPType>
        <DstPort>8080</DstPort>
        <SrcPort>8080</SrcPort>
        <Tags>test</Tags>
        <IPVersion>4</IPVersion>
        <IPProtol>tcp</IPProtol>
        <RequsetLength>100</RequsetLength>
        <ResponseLength>100</ResponseLength>
        <Origin>0</Origin>
        <LinkType>0</LinkType>
        <RelatedEcs>...</RelatedEcs>
    </DataList>
    <Success>true</Success>
    <Module>ndr***</Module>
    <HttpStatusCode>200</HttpStatusCode>
</DescribeAttackRecordListResponse>
```

##### DescribeThreatSrcIPInfo

Queries the information about a threat intelligence source.

**Authorization information**

| Operation | Access level | Resource type |
|---|---|---|
| yundun- cloudfirewall:DescribeThreatSrc IPInfo | Read | acs:yundun-cloudfirewall:*: {#accountId}:* |

**Throttling**

You can call this operation up to 10 times per second per account. You can call this operation up to 100 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Lang | Strin g | Query | No | zh | The language. Valid values: zh and en. You can leave this parameter empty if it is not required for your business. |
| SrcIP | Strin g | Query | No | 10.x.x.x | The IP address of the threat intelligence source. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Source | String | 10.x.x.x | The source of the threat intelligence. A value 1 indicates public cloud Web Application Firewall (WAF) or distributed denial of service (DDoS). A value of 2 indicates the console. A value of 3 indicates third-party intelligence services. |
| VulLevel | Integer | 1 | The threat level. Valid values: 1 to 10. A higher value indicates higher risks. |
| AttackType | String | IOA | The attack type. |
| Tag | String | test tag _ | The tag. |
| SyncTime | Long | 1706668721 | The synchronization time. |
| Success | Boolean | true | Indicates whether the HTTP request was successful. |

| i | Developer Guide·A on | PI documentat |   | Cloud Security Network Detecti n and Respons | o e |
|---|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| Module | String | ndr*** | The name of the module. |
| HttpStatusCod e | Integer | 200 | The HTTP status code. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=DescribeThreatSrcIPInfo&RegionId=cnhangzhou&Lang=zh&SrcIP=10.x.x.x
```

Sample success responses `JSON` format

```
Content-Type:application/json
```

`{`

```json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "Source":"10.x.x.x",
    "VulLevel":1,
    "AttackType":"IOA",
    "Tag":"test_tag",
    "SyncTime":1706668721,
    "Success":true,
    "Module":"ndr***",
    "HttpStatusCode":200
```

`}` `XML` format

```xml
Content-Type:application/xml <DescribeThreatSrcIPInfoResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <Source>10.x.x.x</Source>
    <VulLevel>1</VulLevel>
    <AttackType>IOA</AttackType>
    <Tag>test_tag</Tag>
    <SyncTime>1706668721</SyncTime>
    <Success>true</Success>
    <Module>ndr***</Module>
    <HttpStatusCode>200</HttpStatusCode>
</DescribeThreatSrcIPInfoResponse>
```

##### ModifyCustomAttackLogFields

Modifies the fields that you want to display in attack logs.

**Authorization information**

| Operation | Access level | Resource type |
|---|---|---|
| yundun- cloudfirewall:ModifyCustomAtta ckLogFields | Write | acs:yundun-cloudfirewall:*: {#accountId}:* |

**Throttling**

You can call this operation up to 10 times per second per account. You can call this operation up to 100 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Lang | Strin g | Query | No | zh | The language. Valid values: zh and en. You can leave this parameter empty if it is not required for your business. |
| AliUid | Long | Query | No | 123456789 | The user ID. |
| CustomFie lds | Strin g | Query | No | {'StartTime':true, 'RuleName':true} | Specifies whether to display the custom fields. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Module | String | ndr*** | The name of the module. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=ModifyCustomAttackLogFields&RegionId=cnhangzhou&Lang=zh&AliUid=123456789&CustomFields={'StartTime':true, 'RuleName':true}
```

Sample success responses `JSON` format

```
Content-Type:application/json
```

`{`

```json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "Module":"ndr***"
```

`}` `XML` format

```xml
Content-Type:application/xml <ModifyCustomAttackLogFieldsResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <Module>ndr***</Module>
</ModifyCustomAttackLogFieldsResponse>
```

##### DescribeAggAttackPPS

Queries the trend of packets per second (PPS) of attacks.

**Authorization information**

| Operation | Access level | Resource type |
|---|---|---|
| yundun- cloudfirewall:DescribeAggAttac kPPS | Read | acs:yundun-cloudfirewall:*: {#accountId}:* |

**Throttling**

You can call this operation up to 10 times per second per account. You can call this operation up to 100 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Lang | Strin g | Query | No | zh | The language. Valid values: zh and en. You can leave this parameter empty if it is not required for your business. |
| StartTime | Long | Query | No | 1707118672 | The beginning of the time range to query. |
| EndTime | Long | Query | No | 1707118672 | The end of the time range to query. |
| DstIP | Strin g | Query | No | 1.1.1.1 | The destination IP address. |
| SrcIP | Strin g | Query | No | 1.1.1.1 | The source IP address. |
| AliUid | Long | Query | No | 1234567890 | The user ID. |
| HTTPCode | Integ er | Query | No | 200 | The HTTP status code. |
| XFF | Strin g | Query | No | 2.2.2.2 | The X-Forwarded-For (XFF) header. |
| Host | Strin g | Query | No | 2.2.2.2 | The Host header. |
| AttackRes ult | Strin g | Query | No | 0 | The attack result. A value of 0 indicates that the attacker attempted an attack. A value of 1 indicates that the attack is successful. A value of -1 indicates that the attack has failed. |
| RuleID | Long | Query | No | 12323 | The hit rule ID. |
| Origin | Strin g | Query | No | 0 | The source of the rule. A value of 0 indicates Intrusion detection system (IDS). A value of 1 indicates web IDS. |

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| RuleType | Strin g | Query | No | Web attack | The type of the rule. |
| VulLevel | Strin g | Query | No | 1 | The threat level. A value of 1 indicates low risk. A value of 2 indicates medium risk. A value of 3 indicates high risk. |
| DepAliUid | Strin g | Query | No | 1234567890 | The department ID. |
| Label | Strin g | Query | No | test | The label. |
| IPType | Strin g | Query | No | test | The type of the service to which the IP address belongs. A value of 0 indicates others. A value of 1 indicates Web Application Firewall (WAF). A value of 2 indicates Server Load Balancer (SLB). A value of 3 indicates Elastic IP Address (EIP). A value of 4 indicates Elastic Compute Service (ECS). |
| ProtectSta tus | Strin g | Query | No | 0 | The protection status. A value of 0 indicates that the attack is not handled. A value of 1 indicates that the attack is blocked. A value of 2 indicates that the IP address is added to the whitelist. A value of 3 indicates that the attack is ignored. |
| LinkType | Strin g | Query | No | 0 | The product on which the attack is detected. A value of 0 indicates Inter-connection Switch (ISW). A value of 1 indicates Customer Access Switch (CSW). A value of 2 indicates LVS Switch (LSW). A value of 3 indicates Elastic Network Interface (ENI). |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| DataList | Array |   |   |
| -Date | String | 2024-02-06 00:00:00 | The date. |
| -PPS | Integer | 100 | The number of attacks. |
| -Time | Long | 1707148800 | The timestamp. |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| TotalCount | Integer | 100 | The total number of entries returned. |
| TimeOut | Boolean | false | Indicates whether the request timed out. Valid values: true and false. |
| Success | Boolean | true | Indicates whether the HTTP request was successful. |
| Module | String | ndr*** | The name of the module. |
| HttpStatusCod e | Integer | 200 | The HTTP status code. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=DescribeAggAttackPPS&RegionId=cnhangzhou&Lang=zh&StartTime=1707118672&EndTime=1707118672&DstIP=1.1.1.1&SrcIP=1.1.1.1&AliU =1234567890&HTTPCode=200&XFF=2.2.2.2&Host=2.2.2.2&AttackResult=0&RuleID=12323&Origin=0&Ru Type=Web attack&VulLevel=1&DepAliUid=1234567890&Label=test&IPType=test&ProtectStatus=0&LinkType=0
```

Sample success responses `JSON` format

```
Content-Type:application/json
```

`{`

```json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "TotalCount":100,
    "TimeOut":false,
    "DataList":[
```

`{`

```json
            "PPS":100,
            "Time":1707148800,
            "Date":"2024-02-06 00:00:00"
```

`}` `],`

```json
    "Success":true,
    "Module":"ndr***",
    "HttpStatusCode":200
```

`}` `XML` format

```xml
Content-Type:application/xml <DescribeAggAttackPPSResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <TotalCount>100</TotalCount>
    <TimeOut>false</TimeOut>
    <DataList>
        <Date>2024-02-06 00:00:00</Date>
        <PPS>100</PPS>
        <Time>1707148800</Time>
    </DataList>
    <Success>true</Success>
    <Module>ndr***</Module>
    <HttpStatusCode>200</HttpStatusCode>
</DescribeAggAttackPPSResponse>
```

##### AddAttackDisposal

Updates the protection status based on threat detection logs.

**Authorization information**

| Operation | Access level | Resource type |
|---|---|---|
| yundun- cloudfirewall:AddAttackDisposal | Write | acs:yundun-cloudfirewall:*: {#accountId}:* |

**Throttling**

You can call this operation up to 10 times per second per account. You can call this operation up to 100 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Lang | Strin g | Query | No | zh | The language. Valid values: zh and en. You can leave this parameter empty if it is not required for your business. |
| StartTime | Long | Query | No | 1704252277 | The beginning of the time range to query. |
| EndTime | Long | Query | No | 1704252277 | The end of the time range to query. |
| DstIP | Strin g | Query | No | 1.1.1.1 | The source IP address. |
| SrcIP | Strin g | Query | No | 2.2.2.2 | The destination IP address. |
| AliUid | Long | Query | No | 1234567890 | The user ID. |
| HTTPCode | Integ er | Query | No | 404 | The HTTP status code. |
| XFF | Strin g | Query | No | 1.1.1.1 | The X-Forwarded-For (XFF) header. |
| Host | Strin g | Query | No | 1.1.1.1 | The HOST header. |
| AttackRes ult | Strin g | Query | No | 0 | The attack result. A value of 0 indicates that the attacker attempted an attack. A value of 1 indicates that the attack is successful. A value of -1 indicates that the attack has failed. |

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| RuleID | Integ er | Query | No | 1024 | The hit rule ID. |
| Origin | Strin g | Query | No | 0 | The source of the rule. A value of 0 indicates Intrusion detection system (IDS). A value of 1 indicates web IDS. |
| RuleType | Strin g | Query | No | Code execution | The type of the rule. |
| VulLevel | Strin g | Query | No | 1 | The threat level. A value of 1 indicates low risk. A value of 2 indicates medium risk. A value of 3 indicates high risk. |
| DepAliUid | Strin g | Query | No | 1234567890 | The department ID. |
| Label | Strin g | Query | No | test | The label. |
| IPType | Strin g | Query | No | 2 | The type of the asset. A value of 0 indicates others. A value of 1 indicates Web Application Firewall (WAF). A value of 2 indicates Server Load Balancer (SLB). A value of 3 indicates Elastic IP Address (EIP). A value of 4 indicates Elastic Compute Service (ECS). A value of 5 indicates domain. |

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| ProtectSta tus | Strin g | Query | No | 0 | The protection status. A value of 0 indicates that the attack is not handled. A value of 1 indicates that the attack is blocked. A value of 2 indicates that the IP address is added to the whitelist. A value of 3 indicates that the attack is ignored. |
| DealStatu s | Strin g | Query | No | 1 | Indicates how the attack is handled. A value of 1 indicates that the attack is blocked. A value of 2 indicates that the IP address is added to the whitelist. A value of 3 indicates that the attack is ignored. |
| User | Strin g | Query | No | user | The user. |
| Payload | Strin g | Query | No | POST / HTTP/1.1\r Host:1.1.1.1 | The payload. |
| GroupMd5 | Strin g | Query | No | 818e990abdf5967841df 467dd5098*** | The grouping MD5 hash value. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Success | Boolean | true | Indicates whether the HTTP request was successful. |
| Module | String | ndr*** | The name of the module. |
| Error | String |   |   |
| HttpStatusCod e | Integer | 200 | The HTTP status code. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=AddAttackDisposal&RegionId=cnhangzhou&Lang=zh&StartTime=1704252277&EndTime=1704252277&DstIP=1.1.1.1&SrcIP=2.2.2.2&AliU =1234567890&HTTPCode=404&XFF=1.1.1.1&Host=1.1.1.1&AttackResult=0&RuleID=1024&Origin=0&Rul ype=Code execution&VulLevel=1&DepAliUid=1234567890&Label=test&IPType=2&ProtectStatus=0&DealStatus= User=user&Payload=POST / HTTP/1.1\rHost:1.1.1.1&GroupMd5=818e990abdf5967841df467dd5098***
```

Sample success responses `JSON` format

```
Content-Type:application/json
```

`{`

```json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "Success":true,
    "Module":"ndr***",
    "Error":"",
    "HttpStatusCode":200
```

`}` `XML` format

```xml
Content-Type:application/xml <AddAttackDisposalResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <Success>true</Success>
    <Module>ndr***</Module>
    <Error></Error>
    <HttpStatusCode>200</HttpStatusCode>
</AddAttackDisposalResponse>
```

##### DescribeCustomAttackLogFields

Queries the custom display fields in attack logs of threat detection.

**Authorization information**

| Operation | Access level | Resource type |
|---|---|---|
| yundun- cloudfirewall:DescribeCustomAt tackLogFields | Read | acs:yundun-cloudfirewall:*: {#accountId}:* |

**Throttling**

You can call this operation up to 10 times per second per account. You can call this operation up to 100 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Lang | Strin g | Query | No | zh | The language. Valid values: zh and en. You can leave this parameter empty if it is not required for your business. |
| AliUid | Long | Query | No | 1234567890 | The user ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| ShowFields | Normal | ['AttackTime','Rule Name','SrcIP' ...] | The display fields. |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=DescribeCustomAttackLogFields&RegionId=cnhangzhou&Lang=zh&AliUid=1234567890
```

Sample success responses `JSON` format

```
Content-Type:application/json
```

`{`

```json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "ShowFields":"['AttackTime','RuleName','SrcIP' ...]"
```

`}` `XML` format

```xml
Content-Type:application/xml <DescribeCustomAttackLogFieldsResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <ShowFields>
        <ShowFields>['AttackTime','RuleName','SrcIP' ...]</ShowFields>
    </ShowFields>
</DescribeCustomAttackLogFieldsResponse>
```

##### TagAttackRecodes

Adds a tag to specific attack log entries.

**Authorization information**

| Operation | Access level | Resource type |
|---|---|---|
| yundun- cloudfirewall:TagAttackRecodes | Write | acs:yundun-cloudfirewall:*: {#accountId}:* |

**Throttling**

You can call this operation up to 10 times per second per account. You can call this operation up to 100 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Lang | Strin g | Query | No | zh | The language. Valid values: zh and en. You can leave this parameter empty if it is not required for your business. |
| AliUid | Long | Query | No | 123456789 | The user ID. |
| Tag | Strin g | Query | No | test tag _ | The tag that you want to add. |

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| FilterParas | Strin g | Query | No | {AliUid:123456789,SrcIP :10.x.x.x} | A JSON string that contains conditions to filter log entries. The filter conditions can contain the following parameters: AliUid, StartTime, EndTime, SrcIP, DstIP, DstPort, AttackResult, RuleID, Origin, and Tags. You can specify multiple tags in Tags. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Success | Boolean | true | Indicates whether the HTTP request was successful. |
| Module | String | ndr*** | The name of the module. |
| HttpStatusCod e | Integer | 200 | The HTTP status code. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=TagAttackRecodes&RegionId=cnhangzhou&Lang=zh&AliUid=123456789&Tag=test_tag&FilterParas= {AliUid:123456789,SrcIP:10.x.x.x}
```

Sample success responses `JSON` format

```
Content-Type:application/json
```

`{`

```json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "Success":true,
    "Module":"ndr***",
    "HttpStatusCode":200
```

`}` `XML` format

```xml
Content-Type:application/xml <TagAttackRecodesResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <Success>true</Success>
    <Module>ndr***</Module>
    <HttpStatusCode>200</HttpStatusCode>
</TagAttackRecodesResponse>
```

##### DescribeAggAttackVulLevel

Queries the statistics on threat levels.

**Authorization information**

| Operation | Access level | Resource type |
|---|---|---|
| yundun- cloudfirewall:DescribeAggAttac kVulLevel | Read | acs:yundun-cloudfirewall:*: {#accountId}:* |

**Throttling**

You can call this operation up to 10 times per second per account. You can call this operation up to 100 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Lang | Strin g | Query | No | zh | The language. Valid values: zh and en. You can leave this parameter empty if it is not required for your business. |
| StartTime | Long | Query | No | 1707118672 | The beginning of the time range to query. |
| EndTime | Long | Query | No | 1707118672 | The end of the time range to query. |
| DstIP | Strin g | Query | No | 1.1.1.1 | The destination IP address. |
| SrcIP | Strin g | Query | No | 1.1.1.1 | The source IP address. |
| AliUid | Long | Query | No | 1234567890 | The user ID. |
| HTTPCode | Integ er | Query | No | 200 | The HTTP status code. |
| XFF | Strin g | Query | No | 2.2.2.2 | The X-Forwarded-For (XFF) header. |
| Host | Strin g | Query | No | 2.2.2.2 | The HOST header. |
| AttackRes ult | Strin g | Query | No | 0 | The attack result. A value of 0 indicates that the attacker attempted an attack. A value of 1 indicates that the attack is successful. A value of -1 indicates that the attack has failed. |
| RuleID | Long | Query | No | 12323 | The hit rule ID. |
| Origin | Strin g | Query | No | 0 | The source of the rule. A value of 0 indicates Intrusion detection system (IDS). A value of 1 indicates web IDS. |

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| RuleType | Strin g | Query | No | Web attack | The type of the rule. |
| VulLevel | Strin g | Query | No | 1 | The threat level. A value of 1 indicates low risk. A value of 2 indicates medium risk. A value of 3 indicates high risk. |
| DepAliUid | Strin g | Query | No | 1234567890 | The department ID. |
| Label | Strin g | Query | No | test | The label. |
| IPType | Strin g | Query | No | 1 | The type of the service to which the IP address belongs. A value of 0 indicates others. A value of 1 indicates Web Application Firewall (WAF). A value of 2 indicates Server Load Balancer (SLB). A value of 3 indicates Elastic IP Address (EIP). A value of 4 indicates Elastic Compute Service (ECS). |
| ProtectSta tus | Strin g | Query | No | 0 | The protection status. A value of 0 indicates that the attack is not handled. A value of 1 indicates that the attack is blocked. A value of 2 indicates that the IP address is added to the whitelist. A value of 3 indicates that the attack is ignored. |
| LinkType | Strin g | Query | No | 0 | The product on which the attack is detected. A value of 0 indicates Inter-connection Switch (ISW). A value of 1 indicates Customer Access Switch (CSW). A value of 2 indicates LVS Switch (LSW). A value of 3 indicates Elastic Network Interface (ENI). |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| TimeOut | Boolean | false | Indicates whether the request timed out. Valid values: true and false. |
| TotalCount | Integer | 100 | The total number of entries returned. |
| HighCount | Integer | 100 | The number of high-risk attacks. |
| MediumCount | Integer | 100 | The number of medium-risk attacks. |
| LowCount | Integer | 100 | The number of low-risk attacks. |
| Success | Boolean | true | Indicates whether the HTTP request was successful. |
| Module | String | ndr*** | The name of the module. |
| HttpStatusCod e | Integer | 200 | The HTTP status code. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=DescribeAggAttackVulLevel&RegionId=cnhangzhou&Lang=zh&StartTime=1707118672&EndTime=1707118672&DstIP=1.1.1.1&SrcIP=1.1.1.1&AliU =1234567890&HTTPCode=200&XFF=2.2.2.2&Host=2.2.2.2&AttackResult=0&RuleID=12323&Origin=0&Ru Type=Web attack&VulLevel=1&DepAliUid=1234567890&Label=test&IPType=1&ProtectStatus=0&LinkType=0
```

Sample success responses `JSON` format

```
Content-Type:application/json
```

`{`

```json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "TimeOut":false,
    "TotalCount":100,
    "HighCount":100,
    "MediumCount":100,
    "LowCount":100,
    "Success":true,
    "Module":"ndr***",
    "HttpStatusCode":200
```

`}` `XML` format

```xml
Content-Type:application/xml <DescribeAggAttackVulLevelResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <TimeOut>false</TimeOut>
    <TotalCount>100</TotalCount>
    <HighCount>100</HighCount>
    <MediumCount>100</MediumCount>
    <LowCount>100</LowCount>
    <Success>true</Success>
    <Module>ndr***</Module>
    <HttpStatusCode>200</HttpStatusCode>
</DescribeAggAttackVulLevelResponse>
```

##### DescribeAggAttackType

Retrieves statistics on threat detection attack types.

**Authorization information**

| Operation | Access level | Resource type |
|---|---|---|
| yundun- cloudfirewall:DescribeAggAttac kType | Read | acs:yundun-cloudfirewall:*: {#accountId}:* |

**Throttling**

The throttling limit for a single user is 10 queries per second (QPS). The throttling limit for this operation is 100 QPS.

**Request headers**

This operation uses common request headers. No special request headers are required. For more information, see Common request parameters.

**Request parameters**

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| Lang | Strin g | Query | No | zh | The language of the response. Valid values: `zh` (Chinese) and `en` (English). This parameter is optional. |
| StartTime | Long | Query | No | 1707118672 | The start time of the query. |
| EndTime | Long | Query | No | 1707118672 | The end time of the query. |
| DstIP | Strin g | Query | No | 1.1.1.1 | The destination IP address. |
| SrcIP | Strin g | Query | No | 1.1.1.1 | The source IP address. |
| AliUid | Long | Query | No | 1234567890 | The user UID. |
| HTTPCode | Integ er | Query | No | 200 | The HTTP response code. |
| XFF | Strin g | Query | No | 2.2.2.2 | The X-Forwarded-For (XFF) field. |
| Host | Strin g | Query | No | 2.2.2.2 | The Host field. |
| AttackRes ult | Strin g | Query | No | 0 | The result of the attack. Valid values: `0` (attempt), `1` (success), and `-1` (failure). |
| RuleID | Long | Query | No | 12323 | The ID of the rule that was hit. |

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| Origin | Strin g | Query | No | 0 | The source of the rule. Valid values: `0` (Intrusion Detection System (IDS)) and `1` (Web Intrusion Detection System (WEBIDS)). |
| RuleType | Strin g | Query | No | Web attack | The type of the rule. |
| VulLevel | Strin g | Query | No | 1 | The threat level. Valid values: `1` (low), `2` (medium), and `3` (high). |
| DepAliUid | Strin g | Query | No | 1234567890 | The UID of the department. |
| Label | Strin g | Query | No | test | The label. |
| IPType | Strin g | Query | No | 1 | The type of the IP address. Valid values: `0` (Other), `1` (Web Application Firewall (WAF)), `2` (Server Load Balancer (SLB)), `3` (Elastic IP Address (EIP)), and `4` (Elastic Compute Service (ECS)). |
| ProtectSta tus | Strin g | Query | No | 0 | The protection status. Valid values: `0` (Not processed), `1` (Blocked), `2` (Whitelisted), and `3` (Ignored). |

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| LinkType | Strin g | Query | No | 0 | The detection location. Valid values: `0` (Inter- connection Switch (ISW)), `1` (Customer Switch (CSW)), `2` (LVS Switch (LSW)), and `3` (Elastic Network Interface (ENI)). |

**Returned data**

| Parameter | Type | Example | Description |
|---|---|---|---|
| DataList | Array |   |   |
| -RuleType | String | Web attack | The type of the rule. |
| -Count | Integer | 100 | The number of attacks. |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The ID of the request. Alibaba Cloud generates a unique ID for each request. You can use the ID to troubleshoot issues. |
| TotalCount | Integer | 100 | The total number of entries. |
| TimeOut | Boolean | false | Indicates whether the request timed out. `true`: The request timed out. `false`: The request did not time out. |
| Success | Boolean | true | Indicates whether the HTTP request was successful. |
| Module | String | ndr*** | The name of the module. |
| HttpStatusCod e | Integer | 200 | The HTTP response code for the request. |

**Examples**

Sample request

```
https://[Endpoint]/?Action=DescribeAggAttackType&RegionId=cnhangzhou&Lang=zh&StartTime=1707118672&EndTime=1707118672&DstIP=1.1.1.1&SrcIP=1.1.1.1&AliU =1234567890&HTTPCode=200&XFF=2.2.2.2&Host=2.2.2.2&AttackResult=0&RuleID=12323&Origin=0&Ru Type=Web%20attack&VulLevel=1&DepAliUid=1234567890&Label=test&IPType=1&ProtectStatus=0&Lin ype=0
```

Sample response `JSON` format

```
Content-Type:application/json
```

`{`

```json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "TotalCount":100,
    "TimeOut":false,
    "DataList":[
```

`{`

```json
            "RuleType":"Web attack",
            "Count":100
```

`}` `],`

```json
    "Success":true,
    "Module":"ndr***",
    "HttpStatusCode":200
```

`}` `XML` format

```xml
Content-Type:application/xml <DescribeAggAttackTypeResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <TotalCount>100</TotalCount>
    <TimeOut>false</TimeOut>
    <DataList>
        <RuleType>Web attack</RuleType>
        <Count>100</Count>
    </DataList>
    <Success>true</Success>
    <Module>ndr***</Module>
    <HttpStatusCode>200</HttpStatusCode>
</DescribeAggAttackTypeResponse>
```

##### DescribeAggAttackRecords

You can call the DescribeAggAttackRecords operation to query a list of threat detection attacks.

**Authorization information**

| Operation | Access level | Resource type |
|---|---|---|
| yundun- cloudfirewall:DescribeAggAttac kRecords | Read | acs:yundun-cloudfirewall:*: {#accountId}:* |

**Throttling**

The call frequency for a single user is limited to 10 queries per second (QPS). The API call frequency is limited to 100 QPS.

**Request header**

This operation uses common request headers. No special request headers are required. For more information, see the common request parameters document.

**Request parameters**

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| Lang | Strin g | Query | No | en | The language of the response. Valid values: `zh` for Chinese and `en` for English. This is not a business-critical parameter and can be ignored. |
| StartTime | Long | Query | No | 1707118672 | The start time of the query. |
| EndTime | Long | Query | No | 1707118672 | The end time of the query. |
| DstIP | Strin g | Query | No | 1.1.1.1 | The destination IP address. |
| SrcIP | Strin g | Query | No | 1.1.1.1 | The source IP address. |
| AliUid | Long | Query | No | 1234567890 | The user UID. |
| HTTPCode | Integ er | Query | No | 200 | The HTTP response code. |
| XFF | Strin g | Query | No | 2.2.2.2 | The X-Forwarded-For (XFF) field. |
| Host | Strin g | Query | No | 2.2.2.2 | The Host field. |
| AttackRes ult | Strin g | Query | No | 0 | The result of the attack. 0 indicates an attempt. 1 indicates a success. -1 indicates a failure. |

| i | Developer Gui on | de·API d | ocumentat |   | Cloud | Security Network Detecti n and Respons | o e |
|---|---|---|---|---|---|---|---|

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| RuleID | Long | Query | No | 12323 | The ID of the rule that was hit. |
| Origin | Strin g | Query | No | 0 | The source of the rule. 0 indicates Intrusion Detection System (IDS). 1 indicates Web Intrusion Detection System (WEBIDS). |
| RuleType | Strin g | Query | No | Web attack | The type of the rule. |
| VulLevel | Strin g | Query | No | 1 | The threat level. 1 indicates low risk. 2 indicates medium risk. 3 indicates high risk. |
| DepAliUid | Strin g | Query | No | 1234567890 | The UID of the department. |
| Label | Strin g | Query | No | test | The label. |
| IPType | Strin g | Query | No | test | The IP address type. 0 indicates other. 1 indicates WAF. 2 indicates SLB. 3 indicates EIP. 4 indicates ECS. |
| PageSize | Integ er | Query | No | 10 | The number of entries per page. |
| CurrentPa ge | Integ er | Query | No | 1 | The page number. |
| ProtectSta tus | Strin g | Query | No | 0 | The protection status. 0 indicates not processed. 1 indicates blocked. 2 indicates added to the whitelist. 3 indicates ignored. |

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| LinkType | Strin g | Query | No | 0 | The detection location. 0 indicates Inter- connection Switch (ISW). 1 indicates Customer Switch (CSW). 2 indicates LVS Switch (LSW). 3 indicates Elastic Network Interface (ENI). |

**Response data**

| Parameter | Type | Example | Description |
|---|---|---|---|
| DataList | Array |   |   |
| -SrcIP | String | 1.1.1.1 | The source IP address. |
| -DstIP | String | 1.1.1.1 | The destination IP address. |
| -DestPort | String | 80 | The destination port. |
| -StartTime | Long | 1707118672 | The start time of the attack. |
| -EndTime | Long | 1707118672 | The end time of the attack. |
| -Department | String | test | The department name. |
| -RuleType | String | Web attack | The type of the rule. |
| -RuleName | String | Web attack | The name of the rule. |
| -Payload | String | GET /aaa.jsp? test=JavaSCript:ale rt(123) HTTP/1.1*** | The payload. |
| -VulLevel | String | 1 | The threat level. 1 indicates low risk. 2 indicates medium risk. 3 indicates high risk. |
| -HTTPCode | String | 200 | The HTTP response code. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| -AttackResult | String | 0 | The result of the attack. 0 indicates an attempt. 1 indicates a success. -1 indicates a failure. |
| -Count | Integer | 200 | The number of attacks. |
| -XFF | String | 2.2.2.2 | The XFF field. |
| -Origin | String | 0 | The source of the rule. 0 indicates IDS. 1 indicates WEBIDS. |
| -RuleID | String | 12323 | The ID of the rule that was hit. |
| -Tags | String | test | The tags. |
| -Intell | Boolean | false | Indicates whether the source IP address is from threat intelligence. |
| -ProtectStatus | String | 0 | The protection status. 0 indicates not processed. 1 indicates blocked. 2 indicates added to the whitelist. 3 indicates ignored. |
| -Host | String | 2.2.2.2 | The Host field. |
| -LinkType | String | 0 | The detection location. 0 indicates ISW. 1 indicates CSW. 2 indicates LSW. 3 indicates ENI. |
| -GroupMd5 | String | bdc77918a3a7d87f 1d282b7f45b43f** | The MD5 hash of the group. |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The ID of the request. This unique identifier is generated by Alibaba Cloud and can be used to troubleshoot issues. |
| TimeOut | Boolean | false | Indicates whether the request timed out. `true` indicates a timeout. `false` indicates no timeout. |
| TotalCount | Integer | 100 | The total number of entries. |
| CurrentPage | Integer | 1 | The page number. |

| n | Cloud Security Ne and Response | twork Detectio |   | Developer Guide·API documenta io | t n |
|---|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| PageSize | Integer | 10 | The number of entries per page. |
| Success | Boolean | true | Indicates whether the HTTP request was successful. |
| Module | String | ndr*** | The name of the module. |
| HttpStatusCod e | Integer | 200 | The HTTP response code of the request. |

**Examples**

Sample request

```
https://[Endpoint]/?Action=DescribeAggAttackRecords&RegionId=cnhangzhou&Lang=en&StartTime=1707118672&EndTime=1707118672&DstIP=1.1.1.1&SrcIP=1.1.1.1&AliU =1234567890&HTTPCode=200&XFF=2.2.2.2&Host=2.2.2.2&AttackResult=0&RuleID=12323&Origin=0&Ru Type=Web%20attack&VulLevel=1&DepAliUid=1234567890&Label=test&IPType=test&PageSize=10&Curr tPage=1&ProtectStatus=0&LinkType=0
```

Sample successful response `JSON` format

```
Content-Type:application/json
```

`{`

```json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "TimeOut":false,
    "TotalCount":100,
    "CurrentPage":1,
    "PageSize":10,
    "DataList":[
```

`{`

```json
            "Origin":"0",
            "Intell":false,
            "EndTime":1707118672,
            "RuleID":"12323",
            "DestPort":"80",
            "StartTime":1707118672,
            "RuleType":"Web attack",
            "Host":"2.2.2.2",
            "HTTPCode":"200",
            "Count":200,
            "SrcIP":"1.1.1.1",
            "Department":"test",
            "AttackResult":"0",
            "GroupMd5":"bdc77918a3a7d87f1d282b7f45b43f**",
            "DstIP":"1.1.1.1",
            "XFF":"2.2.2.2",
            "ProtectStatus":"0",
            "Payload":"GET /aaa.jsp?test=JavaSCript:alert(123) HTTP/1.1***",
            "LinkType":"0",
            "RuleName":"Web attack",
            "Tags":"test",
            "VulLevel":"1"
```

`}` `],`

```json
    "Success":true,
    "Module":"ndr***",
    "HttpStatusCode":200
```

`}` `XML` format

```xml
Content-Type:application/xml <DescribeAggAttackRecordsResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <TimeOut>false</TimeOut>
    <TotalCount>100</TotalCount>
    <CurrentPage>1</CurrentPage>
    <PageSize>10</PageSize>
    <DataList>
        <SrcIP>1.1.1.1</SrcIP>
        <DstIP>1.1.1.1</DstIP>
        <DestPort>80</DestPort>
        <StartTime>1707118672</StartTime>
        <EndTime>1707118672</EndTime>
        <Department>test</Department>
        <RuleType>Web attack</RuleType>
        <RuleName>Web attack</RuleName>
        <Payload>GET /aaa.jsp?test=JavaSCript:alert(123) HTTP/1.1***</Payload>
        <VulLevel>1</VulLevel>
        <HTTPCode>200</HTTPCode>
        <AttackResult>0</AttackResult>
        <Count>200</Count>
        <XFF>2.2.2.2</XFF>
        <Origin>0</Origin>
        <RuleID>12323</RuleID>
        <Tags>test</Tags>
        <Intell>false</Intell>
        <ProtectStatus>0</ProtectStatus>
        <Host>2.2.2.2</Host>
        <LinkType>0</LinkType>
        <GroupMd5>bdc77918a3a7d87f1d282b7f45b43f**</GroupMd5>
    </DataList>
    <Success>true</Success>
    <Module>ndr***</Module>
    <HttpStatusCode>200</HttpStatusCode>
</DescribeAggAttackRecordsResponse>
```

##### DescribeAttackRecord

You can call the DescribeAttackRecord operation to query a single threat detection attack record.

**Authorization**

| Operation | Access level | Resource type |
|---|---|---|
| yundun- cloudfirewall:DescribeAttackRe cord | Read | acs:yundun-cloudfirewall:*: {#accountId}:* |

**Throttling**

Per user: 10 queries per second (QPS). Per API operation: 100 QPS.

**Request header**

This operation uses common request headers. Special request headers are not required. For more information, see Common request parameters.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Lang | Strin g | Query | No | zh | The language of the response. Valid values: `zh` for Chinese and `en` for English. This parameter is optional. |
| StartTime | Long | Query | No | 1707118672 | The start time of the query. |
| EndTime | Long | Query | No | 1707118672 | The end time of the query. |
| DstIP | Strin g | Query | No | 1.1.1.1 | The destination IP address. |
| SrcIP | Strin g | Query | No | 1.1.1.1 | The source IP address. |
| AliUid | Long | Query | No | 1234567890 | The user UID. |
| HTTPCode | Integ er | Query | No | 200 | The HTTP response code. |
| AttackRes ult | Strin g | Query | No | 0 | The result of the attack. Valid values: `0` (attempt), `1` (success), and `-1` (failure). |
| RuleID | Long | Query | No | 12323 | The ID of the rule that was hit. |
| Origin | Integ er | Query | No | 0 | The source of the rule. Valid values: `0` for Intrusion Detection System (IDS) and `1` for Web IDS. |

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| DstPort | Integ er | Query | No | 8080 | The destination port. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The ID of the request. |
| SrcIP | String | 1.1.1.1 | The source IP address. |
| DstIP | String | 1.1.1.1 | The destination IP address. |
| SessionTime | String | 1707118672 | The session time. |
| Department | String | test | The department name. |
| RuleType | String | Web Attack | The rule type. |
| RuleName | String | Web Attack | The rule name. |
| VulLevel | String | 1 | The threat level. Valid values: `1` (low), `2` (medium), and `3` (high). |
| HTTPCode | String | 200 | The HTTP response code. |
| AttackResult | String | 0 | The result of the attack. Valid values: `0` (attempt), `1` (success), and `-1` (failure). |
| XFF | String | 2.2.2.2 | The X-Forwarded-For (XFF) header field. |
| RuleID | String | 12323 | The ID of the rule that was hit. |
| MatchData | String | GET /aaa.jsp? test=JavaSCript:ale rt(123) HTTP/1.1*** | The payload. |
| RequsetData | String | GET /aaa.jsp? test=JavaSCript:ale rt(123) HTTP/1.1*** | The request data. |

| Developer Guide·A | PI documentat |   | Cloud Security Network Detecti |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| ResponseData | String | 404 | The response data. |
| HTTPType | String | 1 | The HTTP type. Valid values: `0` (Layer 4 detection) and `1` (Layer 7 detection). |
| DstPort | String | 8080 | The destination port. |
| SrcPort | String | 8080 | The source port. |
| Tags | String | test | The tag. |
| IPVersion | String | 4 | The IP version. Valid values: `4` (IPv4) and `6` (IPv6). |
| IPProtol | String | tcp | The IP protocol. |
| RequsetLengt h | Integer | 100 | The length of the request information. |
| ResponseLeng th | Integer | 100 | The length of the response information. |
| Origin | String | 0 | The source of the rule. Valid values: `0` (IDS) and `1` (Web IDS). |
| LinkType | String | 0 | The detection location. Valid values: `0` for Inter-connection Switch (ISW), `1` for Customer Switch (CSW), `2` for LVS Switch (LSW), and `3` for Elastic Network Interface (ENI). |
| Success | Boolean | true | Indicates whether the HTTP request was successful. |
| Module | String | ndr*** | The module name. |
| HttpStatusCod e | Integer | 200 | The HTTP status code of the response. |

**Examples**

Request example

```
https://[Endpoint]/?Action=DescribeAttackRecord&RegionId=cnhangzhou&Lang=zh&StartTime=1707118672&EndTime=1707118672&DstIP=1.1.1.1&SrcIP=1.1.1.1&AliU =1234567890&HTTPCode=200&AttackResult=0&RuleID=12323&Origin=0&DstPort=8080&Host=test.com& F=1.1.1.1
```

Response example `JSON` format

```
Content-Type:application/json
```

`{`

```json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "SrcIP":"1.1.1.1",
    "DstIP":"1.1.1.1",
    "SessionTime":"1707118672",
    "Department":"test",
    "RuleType":"Web Attack",
    "RuleName":"Web Attack",
    "VulLevel":"1",
    "HTTPCode":"200",
    "AttackResult":"0",
    "XFF":"2.2.2.2",
    "RuleID":"12323",
    "MatchData":"GET /aaa.jsp?test=JavaScript:alert(123) HTTP/1.1***",
    "RequestData":"GET /aaa.jsp?test=JavaScript:alert(123) HTTP/1.1***",
    "ResponseData":"404",
    "HTTPType":"1",
    "DstPort":"8080",
    "SrcPort":"8080",
    "Tags":"test",
    "IPVersion":"4",
    "IPProtocol":"tcp",
    "RequestLength":100,
    "ResponseLength":100,
    "Origin":"0",
    "LinkType":"0",
    "Success":true,
    "Module":"ndr***",
    "HttpStatusCode":200
```

`}` `XML` format

```xml
Content-Type:application/xml <DescribeAttackRecordResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <SrcIP>1.1.1.1</SrcIP>
    <DstIP>1.1.1.1</DstIP>
    <SessionTime>1707118672</SessionTime>
    <Department>test</Department>
    <RuleType>Web Attack</RuleType>
    <RuleName>Web Attack</RuleName>
    <VulLevel>1</VulLevel>
    <HTTPCode>200</HTTPCode>
    <AttackResult>0</AttackResult>
    <XFF>2.2.2.2</XFF>
    <RuleID>12323</RuleID>
    <MatchData>GET /aaa.jsp?test=JavaScript:alert(123) HTTP/1.1***</MatchData>
    <RequestData>GET /aaa.jsp?test=JavaScript:alert(123) HTTP/1.1***</RequestData>
    <ResponseData>404</ResponseData>
    <HTTPType>1</HTTPType>
    <DstPort>8080</DstPort>
    <SrcPort>8080</SrcPort>
    <Tags>test</Tags>
    <IPVersion>4</IPVersion>
    <IPProtocol>tcp</IPProtocol>
    <RequestLength>100</RequestLength>
    <ResponseLength>100</ResponseLength>
    <Origin>0</Origin>
    <LinkType>0</LinkType>
    <Success>true</Success>
    <Module>ndr***</Module>
    <HttpStatusCode>200</HttpStatusCode>
</DescribeAttackRecordResponse>
```

##### DescribeIDSWhiteRules

Call the DescribeIDSWhiteRules operation to query the rules in the Intrusion Detection System (IDS) whitelist.

**Authorization information**

| Operation | Access level | Resource type |
|---|---|---|
| yundun- cloudfirewall:DescribeIDSWhite Rules | Read | acs:yundun-cloudfirewall:*: {#accountId}:* |

**Throttling**

The throttling limit for a single user is 10 queries per second (QPS). The throttling limit for this operation is 100 QPS.

**Request headers**

This operation uses only common request headers. For more information, see the Common parameters document.

**Request parameters**

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| Lang | Strin g | Query | No | zh | The language of the response. Valid values: zh for Chinese and en for English. This parameter is optional. |
| CurrentPa ge | Strin g | Query | No | 1 | The number of the page to return. |
| PageSize | Strin g | Query | No | 10 | The number of entries to return on each page. |
| Query | Strin g | Query | No | 10.x.x.x | The keyword for a fuzzy query. Supports fuzzy queries by rule ID and IP address. |
| AliUid | Strin g | Query | No | 123456789 | The user ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| DataList | Array |   |   |
| -IpVersion | Integer | 4 | The IP version number. |
| -IP | String | 10.x.x.x | The IP address. |
| -StartTime | Long | 1706668721 | The start time. This is a UNIX timestamp. |
| -EndTime | Long | 1706668721 | The end time. This is a UNIX timestamp. |
| -RuleID | String | 100 | The rule ID. |
| -DstIP | String | 10.x.x.x | The destination IP address. |
| -RuleNote | String | test | The description of the rule. |

| Developer Guide·A on | PI documentat |   | Cloud Security Network Detecti n and Respons |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| -PayLoad | String | test | The rule matching information. |
| -DeptName | String | yundun | The department name. |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The ID of the request. Alibaba Cloud generates this ID for each request. Use this ID to troubleshoot issues. |
| TotalCount | Integer | 100 | The total number of entries returned. |
| PageSize | Integer | 10 | The number of entries returned on the current page. |
| CurrentPage | Integer | 1 | The number of the returned page. |
| Success | Boolean | true | Indicates whether the request was successful. |
| Module | String | ndr*** | The name of the module. |
| HttpStatusCod e | Integer | 200 | The HTTP status code of the response. |

**Examples**

Request example

```
https://[Endpoint]/?Action=DescribeIDSWhiteRules&RegionId=cnhangzhou&Lang=zh&CurrentPage=1&PageSize=10&Query=10.x.x.x&AliUid=123456789
```

Response example `JSON` format

```
Content-Type:application/json
```

`{`

```json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "TotalCount":100,
    "PageSize":10,
    "CurrentPage":1,
    "DataList":[
```

`{`

```json
            "EndTime":1706668721,
            "IpVersion":4,
            "IP":"10.x.x.x",
            "RuleID":"100",
            "RuleNote":"test",
            "StartTime":1706668721,
            "DstIP":"10.x.x.x",
            "PayLoad":"test",
            "DeptName":"yundun"
```

`}` `],`

```json
    "Success":true,
    "Module":"ndr***",
    "HttpStatusCode":200
```

`}` `XML` format

```xml
Content-Type:application/xml <DescribeIDSWhiteRulesResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <TotalCount>100</TotalCount>
    <PageSize>10</PageSize>
    <CurrentPage>1</CurrentPage>
    <DataList>
        <IpVersion>4</IpVersion>
        <IP>10.x.x.x</IP>
        <StartTime>1706668721</StartTime>
        <EndTime>1706668721</EndTime>
        <RuleID>100</RuleID>
        <DstIP>10.x.x.x</DstIP>
        <RuleNote>test</RuleNote>
        <PayLoad>test</PayLoad>
        <DeptName>yundun</DeptName>
    </DataList>
    <Success>true</Success>
    <Module>ndr***</Module>
    <HttpStatusCode>200</HttpStatusCode>
</DescribeIDSWhiteRulesResponse>
```

##### DescribeCustomTags

Call the DescribeCustomTags operation to query custom tags for threat detection.

**Authorization information**

| Operation | Access level | Resource type |
|---|---|---|
| yundun- cloudfirewall:DescribeCustomT ags | Read | acs:yundun-cloudfirewall:*: {#accountId}:* |

**Throttling**

Throttling limit for a single user: 10 queries per second (QPS). Throttling limit for this API operation: 100 QPS.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

**Request parameters**

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| Lang | Strin g | Query | No | zh | The language of the response. Valid values: `zh` for Chinese and `en` for English. This parameter is optional. |
| AliUid | Long | Query | No | 1234567890 | The user ID (UID). |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Tags | Normal | ['tag1','tag2','tag3' ...] | A list of tags. |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The ID of the request. This ID is generated by Alibaba Cloud and is unique for each request. It can be used to troubleshoot issues. |
| Success | Boolean | true | Indicates whether the HTTP request was successful. |
| Module | String | ndr*** | The name of the module. |

| Cloud Security Ne | twork Detectio |   | Developer Guide·API documenta |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| HttpStatusCod e | Integer | 200 | The HTTP status code of the response. |

**Examples**

Sample request

```
https://[Endpoint]/?Action=DescribeCustomTags&RegionId=cnhangzhou&Lang=zh&AliUid=1234567890
```

Sample successful response `JSON` format

```
Content-Type:application/json
```

`{`

```json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "Tags":"['tag1','tag2','tag3' ...]",
    "Success":true,
    "Module":"ndr***",
    "HttpStatusCode":200
```

`}` `XML` format

```xml
Content-Type:application/xml <DescribeCustomTagsResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <Tags>
        <Tags>['tag1','tag2','tag3' ...]</Tags>
    </Tags>
    <Success>true</Success>
    <Module>ndr***</Module>
    <HttpStatusCode>200</HttpStatusCode>
</DescribeCustomTagsResponse>
```

##### ExportAggAttackRecords

You can call the ExportAggAttackRecords and ExportAggResetRecords APIs to export aggregated attack logs.

**Authorization**

| Operation | Access level | Resource type |
|---|---|---|
| yundun- cloudfirewall:ExportAggAttackR ecords | Write | acs:yundun-cloudfirewall:*: {#accountId}:* |

**Throttling**

Throttling limit for a single user: 10 queries per second (QPS). Throttling limit for this operation: 100 QPS.

**Request headers**

This operation uses only common request headers. For more information, see Common parameters.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Lang | Strin g | Query | No | zh | The language of the response. Valid values: `zh` (Chinese) and `en` (English). This parameter is optional. |
| StartTime | Long | Query | No | 1706668721 | The start UNIX timestamp. |
| EndTime | Long | Query | No | 1706668721 | The end UNIX timestamp. |
| DstIP | Strin g | Query | No | 10.x.x.x | The destination IP address. |
| SrcIP | Strin g | Query | No | 10.x.x.x | The source IP address. |
| AliUid | Long | Query | No | 123456789 | The user ID (UID). |
| HTTPCode | Integ er | Query | No | 200 | The HTTP response code. |
| XFF | Strin g | Query | No | 2.2.2.2 | The value of the X- Forwarded-For header. |
| Host | Strin g | Query | No | xxx.com | The domain name. |

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| AttackRes ult | Strin g | Query | No | 1 | The result of the attack. Valid values: `0`: pending confirmation, `1`: successful, `2`: attempted, `3`: compromised, `4`: failed. |
| RuleID | Integ er | Query | No | 65535 | The rule ID. |
| Origin | Strin g | Query | No | 1 | The source of the rule. Valid values: `0`: intrusion detection system (IDS), `1`: web application firewall (WAF). |
| RuleType | Strin g | Query | No | sql | The rule type. |
| VulLevel | Strin g | Query | No | 1 | The risk level. Valid values: `1`: low, `2`: medium, `3`: high. |
| DepAliUid | Strin g | Query | No | 1234567890 | The department ID. |
| Label | Strin g | Query | No | tag1,tag2 | The tag. |
| IPType | Strin g | Query | No | ipv4 | The IP address type. |
| ProtectSta tus | Strin g | Query | No | 1 | The protection status. Valid values: `0`: unhandled, `1`: blocked, `2`: whitelisted, `3`: ignored. |
| LinkType | Strin g | Query | No | tcp | The network connectivity type. |

**Return Data**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The ID of the request. |

| Developer Guide·A on | PI documentat |   | Cloud Security Network Detecti n and Respons |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| ExportFileNam e | String | test.cap | The name of the file. |
| ExportFileUrl | String | https://xxx.com | The download URL for the file. |
| TaskUUID | String | cfa13285-5330- 402e-xxx- 5075c12c6aa8 | The ID of the export task. |
| Success | Boolean | true | Indicates whether the request was successful. |
| Module | String | ndr*** | The name of the module. |
| HttpStatusCod e | Integer | 200 | The HTTP status code of the response. |

**Examples**

Request example

```
https://[Endpoint]/?Action=ExportAggAttackRecords&RegionId=cnhangzhou&Lang=zh&StartTime=1706668721&EndTime=1706668721&DstIP=10.x.x.x&SrcIP=10.x.x.x&Al id=123456789&HTTPCode=200&XFF=2.2.2.2&Host=xxx.com&AttackResult=1&RuleID=65535&Origin=1&R eType=sql&VulLevel=1&DepAliUid=1234567890&Label=tag1,tag2&IPType=ipv4&ProtectStatus=1&Lin ype=tcp
```

Response examples `JSON` format

```
Content-Type:application/json
```

`{`

```json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "ExportFileName":"test.cap",
    "ExportFileUrl":"https://xxx.com",
    "TaskUUID":"cfa13285-5330-402e-xxx-5075c12c6aa8",
    "Success":true,
    "Module":"ndr***",
    "HttpStatusCode":200
```

`}` `XML` format

```xml
Content-Type:application/xml <ExportAggAttackRecordsResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <ExportFileName>test.cap</ExportFileName>
    <ExportFileUrl>https://xxx.com</ExportFileUrl>
    <TaskUUID>cfa13285-5330-402e-xxx-5075c12c6aa8</TaskUUID>
    <Success>true</Success>
    <Module>ndr***</Module>
    <HttpStatusCode>200</HttpStatusCode>
</ExportAggAttackRecordsResponse>
```

##### DescribeAggAttackEventDetail

You can call the DescribeAggAttackEventDetail operation to query the basic information about an attacker profile.

**Authorization information**

| Operation | Access level | Resource type |
|---|---|---|
| yundun- cloudfirewall:DescribeAggAttac kEventDetail | Read | acs:yundun-cloudfirewall:*: {#accountId}:* |

**Throttling**

Limit for a single user: 10 QPS. Limit for this API operation: 100 QPS.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Lang | Strin g | Query | No | zh | The language of the response. Set the value to zh for Chinese or en for English. This parameter is optional. |
| AliUid | Long | Query | No | 1234567890 | The UID of the user. |
| StartTime | Long | Query | No | 1707118672 | The start of the time range to query. |

| Developer Gui | de·API d | ocumentat |   | Cloud | Security Network Detecti |
|---|---|---|---|---|---|

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| EndTime | Long | Query | No | 1707118672 | The end of the time range to query. |
| SrcIP | Strin g | Query | No | 1.1.1.1 | The source IP address of the attack. |
| AttackRes ult | Strin g | Query | No | 0 | The result of the attack. `0` indicates an attempt. `1` indicates a success. `-1` indicates a failure. |
| VulLevel | Strin g | Query | No | 1 | The threat level. `1` indicates low risk. `2` indicates medium risk. `3` indicates high risk. |
| DeptAliUid | Strin g | Query | No | 1234567890 | The UID of the department. |
| LinkType | Strin g | Query | No | 0 | The detection location. `0` indicates ISW. `1` indicates CSW. `2` indicates LSW. `3` indicates ENI. |

**Returned data**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The ID of the request. Alibaba Cloud generates a unique ID for each request. Use this ID to troubleshoot issues. |
| SrcIP | String | 1.1.1.1 | The source IP address. |
| AttackerIP | String | 1.1.1.1 | The IP address of the attacker. |
| LocationZh | String | Beijing | Geographic location in China. |
| LocationEn | String | beijing | Geographic location in English. |

| Cloud Security Ne | twork Detectio |   | Developer Guide·API documenta |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| StartTime | Long | 1707118672 | The start time of the attack. |
| EndTime | Long | 1707118672 | The end time of the attack. |
| ScanTool | String | Nmap | The scanning tool. |
| IntellLable | String | threat intelligence | The threat intelligence tag. |
| RuleInfo | Map | [{'RuleID':'100030 84','RuleNote':'web attack'}] | The list of rule hits. |
| Success | Boolean | true | Indicates whether the HTTP request was successful. |
| Module | String | ndr*** | The name of the module. |
| HttpStatusCod e | Integer | 200 | The HTTP status code of the response. |

**Examples**

Request example

```
https://[Endpoint]/?Action=DescribeAggAttackEventDetail&RegionId=cnhangzhou&Lang=zh&AliUid=1234567890&StartTime=1707118672&EndTime=1707118672&SrcIP=1.1.1.1& tackResult=0&VulLevel=1&DeptAliUid=1234567890&LinkType=0
```

Response example `JSON` format

```
Content-Type:application/json
```

`{`

```json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "SrcIP":"1.1.1.1",
    "AttackerIP":"1.1.1.1",
    "LocationZh":"Beijing",
    "LocationEn":"beijing",
    "StartTime":1707118672,
    "EndTime":1707118672,
    "ScanTool":"Nmap",
    "IntellLable":"threat intelligence",
    "RuleInfo":"[{'RuleID':'10003084','RuleNote':'web attack'}]",
    "Success":true,
    "Module":"ndr***",
    "HttpStatusCode":200
```

`}` `XML` format

```xml
Content-Type:application/xml <DescribeAggAttackEventDetailResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <SrcIP>1.1.1.1</SrcIP>
    <AttackerIP>1.1.1.1</AttackerIP>
    <LocationZh>Beijing</LocationZh>
    <LocationEn>beijing</LocationEn>
    <StartTime>1707118672</StartTime>
    <EndTime>1707118672</EndTime>
    <ScanTool>Nmap</ScanTool>
    <IntellLable>threat intelligence</IntellLable>
    <RuleInfo>[{'RuleID':'10003084','RuleNote':'web attack'}]</RuleInfo>
    <Success>true</Success>
    <Module>ndr***</Module>
    <HttpStatusCode>200</HttpStatusCode>
</DescribeAggAttackEventDetailResponse>
```

##### DescribeIDSRuleInfo

Call the DescribeIDSRuleInfo operation to query the details of an intrusion detection rule.

**Authorization**

| Operation | Access level | Resource type |
|---|---|---|
| yundun- cloudfirewall:DescribeIDSRuleIn fo | Read | acs:yundun-cloudfirewall:*: {#accountId}:* |

**Throttling**

The throttling limit for a single user is 10 queries per second (QPS). The throttling limit for this operation is 100 QPS.

**Request headers**

This operation uses common request headers and has no special request headers. For more information about common request headers, see Common parameters.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Lang | Strin g | Query | No | en | The language of the response. Valid values: `zh` for Chinese and `en` for English. This parameter is optional. |
| RuleID | Long | Query | No | 100 | The ID of the rule. |
| Origin | Integ er | Query | No | 1 | The source of the rule. Valid values: `0` for Intrusion Detection System (IDS) and `1` for Web Application Firewall (WAF). |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The unique ID of the request. To contact Alibaba Cloud Support, provide this ID. |
| ReleaseTime | String | 1706668721 | Publication timestamp. |
| RuleName | String | test | The name of the rule. |
| RuleType | String | webshell | The type of the rule. |
| VulLevel | Integer | 1 | The threat level. Valid values: `1` (low), `2` (medium), and `3` (high). |
| RuleDesc | String | test | The description of the rule. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RuleSource | String | 1 | The source of the rule. Valid values: `1` (IDS), `2` (WAF), and `3` (threat intelligence). |
| RuleAction | String | pass | The action of the rule. Valid values: `pass` (allow), `alert` (monitor), and `drop` (block). |
| RuleStatus | Integer | 0 | The status of the rule. Valid values: `0` (disabled) and `1` (enabled). |
| Success | Boolean | true | Indicates whether the request was successful. |
| Module | String | ndr*** | The name of the module. |
| HttpStatusCod e | Integer | 200 | The HTTP status code returned for the request. |

**Examples**

Request example

```
https://[Endpoint]/?Action=DescribeIDSRuleInfo&RegionId=cnhangzhou&Lang=en&RuleID=100&Origin=1
```

Response examples `JSON` format

```
Content-Type:application/json
```

`{`

```json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "ReleaseTime":"1706668721",
    "RuleName":"test",
    "RuleType":"webshell",
    "VulLevel":1,
    "RuleDesc":"test",
    "RuleSource":"1",
    "RuleAction":"pass",
    "RuleStatus":0,
    "Success":true,
    "Module":"ndr***",
    "HttpStatusCode":200
```

`}` `XML` format

```xml
Content-Type:application/xml <DescribeIDSRuleInfoResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <ReleaseTime>1706668721</ReleaseTime>
    <RuleName>test</RuleName>
    <RuleType>webshell</RuleType>
    <VulLevel>1</VulLevel>
    <RuleDesc>test</RuleDesc>
    <RuleSource>1</RuleSource>
    <RuleAction>pass</RuleAction>
    <RuleStatus>0</RuleStatus>
    <Success>true</Success>
    <Module>ndr***</Module>
    <HttpStatusCode>200</HttpStatusCode>
</DescribeIDSRuleInfoResponse>
```

#### Block logs

##### DescribeAggResetData

Queries the number of attacks by day based on blocked traffic logs.

**Authorization information**

| Operation | Access level | Resource type |
|---|---|---|
| yundun- cloudfirewall:DescribeAggReset Data | Read | acs:yundun-cloudfirewall:*: {#accountId}:* |

**Throttling**

You can call this operation up to 10 times per second per account. You can call this operation up to 100 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Lang | Strin g | Query | No | zh | The language. Valid values: zh and en. You can leave this parameter empty if it is not required for your business. |
| TaskUUID | Strin g | Query | No | F0A8A039-930D-5EC1- 97C8-************ | The asynchronous task UUID. |
| AliUid | Strin g | Query | No | 1234567890 | The user ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| TaskUUID | String | F0A8A039-930D- 5EC1-97C8- ************ | The asynchronous task UUID. |
| TaskStatus | Integer | 1 | The status of the asynchronous query task. A value of 0 indicates that the task is in progress. A value of 1 indicates that the task is complete. |
| Success | Boolean | true | Indicates whether the HTTP request was successful. |
| Module | String | ndr*** | The name of the module. |
| HttpStatusCod e | Integer | 200 | The HTTP status code. |
| ResetLogData | Struct |   |   |
| -DataList | Array |   |   |
| --Date | String | ... | The log date. This parameter is discontinued. |
| --Count | Integer | 100 | The number of attacks. |
| --Time | Long | 1707148800 | The timestamp. |

| Cloud Security Ne and Response | twork Detectio |   | Developer Guide·API documenta io |
|---|---|---|---|
| Parameter | Type | Example | Description |

| -TotalCount | Integer | 100 | The total number of entries returned. |
|---|---|---|---|

**Examples**

Sample requests

```
https://[Endpoint]/?Action=DescribeAggResetData&RegionId=cnhangzhou&Lang=zh&TaskUUID=F0A8A039-930D-5EC1-97C8-************&AliUid=1234567890
```

Sample success responses `JSON` format

```
Content-Type:application/json
```

`{`

```json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "TaskUUID":"F0A8A039-930D-5EC1-97C8-************",
    "TaskStatus":1,
    "ResetLogData":{
        "DataList":[
```

`{`

```json
                "Time":1707148800,
                "Count":100,
                "Date":"..."
```

`}` `],`

```json
        "TotalCount":100
```

`},`

```json
    "Success":true,
    "Module":"ndr***",
    "HttpStatusCode":200
```

`}` `XML` format

```xml
Content-Type:application/xml <DescribeAggResetDataResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <TaskUUID>F0A8A039-930D-5EC1-97C8-************</TaskUUID>
    <TaskStatus>1</TaskStatus>
    <ResetLogData>
        <TotalCount>100</TotalCount>
        <DataList>
            <Date>...</Date>
            <Count>100</Count>
            <Time>1707148800</Time>
        </DataList>
    </ResetLogData>
    <Success>true</Success>
    <Module>ndr***</Module>
    <HttpStatusCode>200</HttpStatusCode>
</DescribeAggResetDataResponse>
```

##### DescribeAggResetTopIPRecordsData

Asynchronously queries the top five IP addresses based on the blocked traffic logs.

**Authorization information**

| Operation | Access level | Resource type |
|---|---|---|
| yundun- cloudfirewall:DescribeAggReset TopIPRecordsData | Read | acs:yundun-cloudfirewall:*: {#accountId}:* |

**Throttling**

You can call this operation up to 10 times per second per account. You can call this operation up to 100 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Lang | Strin g | Query | No | zh | The language. Valid values: zh and en. You can leave this parameter empty if it is not required for your business. |

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| TaskUUID | Strin g | Query | No | F0A8A039-930D-5EC1- 97C8-************ | The asynchronous task UUID. |
| AliUid | Strin g | Query | No | 1234567890 | The user ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| TaskUUID | String | F0A8A039-930D- 5EC1-97C8- ************ | The asynchronous task UUID. |
| TaskStatus | Integer | 1 | The status of the asynchronous query task. A value of 0 indicates that the task is in progress. A value of 1 indicates that the task is complete. |
| Success | Boolean | true | Indicates whether the HTTP request was successful. |
| Module | String | ndr*** | The name of the module. |
| HttpStatusCod e | Integer | 200 | The HTTP status code. |
| ResetLogData | Struct |   |   |
| -DataList | Array |   |   |
| --IP | String | 1.1.1.1 | The IP address. |
| --Count | Integer | 100 | The number of attacks. |
| -TotalCount | Integer | 100 | The total number of entries returned. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=DescribeAggResetTopIPRecordsData&RegionId=cnhangzhou&Lang=zh&TaskUUID=F0A8A039-930D-5EC1-97C8-************&AliUid=1234567890
```

Sample success responses `JSON` format

```
Content-Type:application/json
```

`{`

```json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "TaskUUID":"F0A8A039-930D-5EC1-97C8-************",
    "TaskStatus":1,
    "ResetLogData":{
        "DataList":[
```

`{`

```json
                "IP":"1.1.1.1",
                "Count":100
```

`}` `],`

```json
        "TotalCount":100
```

`},`

```json
    "Success":true,
    "Module":"ndr***",
    "HttpStatusCode":200
```

`}` `XML` format

```xml
Content-Type:application/xml <DescribeAggResetTopIPRecordsDataResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <TaskUUID>F0A8A039-930D-5EC1-97C8-************</TaskUUID>
    <TaskStatus>1</TaskStatus>
    <ResetLogData>
        <TotalCount>100</TotalCount>
        <DataList>
            <IP>1.1.1.1</IP>
            <Count>100</Count>
        </DataList>
    </ResetLogData>
    <Success>true</Success>
    <Module>ndr***</Module>
    <HttpStatusCode>200</HttpStatusCode>
</DescribeAggResetTopIPRecordsDataResponse>
```

##### ExportAggResetRecords

Exports aggregated blocking logs.

**Authorization information**

| Operation | Access level | Resource type |
|---|---|---|
| yundun- cloudfirewall:ExportAggResetRe cords | Write | acs:yundun-cloudfirewall:*: {#accountId}:* |

**Throttling**

You can call this operation up to 10 times per second per account. You can call this operation up to 100 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Lang | Strin g | Query | No | zh | The language. Valid values: zh and en. You can leave this parameter empty if it is not required for your business. |
| StartTime | Long | Query | No | 1706668721 | The beginning of the time range to query. |
| EndTime | Long | Query | No | 1706668721 | The end of the time range to query. |
| DstIP | Strin g | Query | No | 10.x.x.x | The destination IP address. |
| SrcIP | Strin g | Query | No | 10.x.x.x | The source IP address. |
| ActionTyp e | Strin g | Query | No | xss | The attack type. |
| AliUid | Strin g | Query | No | 123456789 | The user ID. |
| RuleID | Long | Query | No | 65535 | The rule ID. |

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Size | Integ er | Query | No | 100000 | The number of logs to be exported. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| ExportFileNam e | String | test.cap | The name of the file. |
| ExportFileUrl | String | https://xxx.com | The download URL of the file. |
| TaskUUID | String | cfa13285-5330- 402e-xxx- 5075c12c6aa8 | The export task ID. |
| Success | Boolean | true | Indicates whether the HTTP request was successful. |
| Module | String | ndr*** | The name of the module. |
| HttpStatusCod e | Integer | 200 | The HTTP status code. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=ExportAggResetRecords&RegionId=cnhangzhou&Lang=zh&StartTime=1706668721&EndTime=1706668721&DstIP=10.x.x.x&SrcIP=10.x.x.x&Ac onType=xss&AliUid=123456789&RuleID=65535&Size=100000
```

Sample success responses `JSON` format

```
Content-Type:application/json
```

`{`

```json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "ExportFileName":"test.cap",
    "ExportFileUrl":"https://xxx.com",
    "TaskUUID":"cfa13285-5330-402e-xxx-5075c12c6aa8",
    "Success":true,
    "Module":"ndr***",
    "HttpStatusCode":200
```

`}` `XML` format

```xml
Content-Type:application/xml <ExportAggResetRecordsResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <ExportFileName>test.cap</ExportFileName>
    <ExportFileUrl>https://xxx.com</ExportFileUrl>
    <TaskUUID>cfa13285-5330-402e-xxx-5075c12c6aa8</TaskUUID>
    <Success>true</Success>
    <Module>ndr***</Module>
    <HttpStatusCode>200</HttpStatusCode>
</ExportAggResetRecordsResponse>
```

##### DescribeAggResetPPS

Queries the packet rate based on blocked traffic logs.

**Authorization information**

| Operation | Access level | Resource type |
|---|---|---|
| yundun- cloudfirewall:DescribeAggReset PPS | Read | acs:yundun-cloudfirewall:*: {#accountId}:* |

**Throttling**

You can call this operation up to 10 times per second per account. You can call this operation up to 100 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Lang | Strin g | Query | No | zh | The language. Valid values: zh and en. You can leave this parameter empty if it is not required for your business. |
| StartTime | Long | Query | No | 1707118672 | The beginning of the time range to query. |
| EndTime | Long | Query | No | 1707118672 | The end of the time range to query. |
| DstIP | Strin g | Query | No | 1.1.1.1 | The destination IP address. |
| SrcIP | Strin g | Query | No | 1.1.1.1 | The source IP address. |
| ActionTyp e | Strin g | Query | No | pass | The protection type. A value of pass indicates that access is allowed. A value of alert indicates that access is observed. A value of drop indicates that access is blocked. |
| AliUid | Strin g | Query | No | 1234567890 | The user ID. |
| RuleID | Long | Query | No | 12323 | The hit rule ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| DataList | Array |   |   |
| -Date | String |   | The log date. This parameter is discontinued. |
| -Count | Integer | 100 | The number of attacks. |
| -Time | Long | 1707148800 | The log timestamp. |

| Cloud Security Ne | twork Detectio |   | Developer Guide·API documenta |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| TaskUUID | String | F0A8A039-930D- 5EC1-97C8- ************ | The asynchronous task UUID. |
| TotalCount | Integer | 100 | The total number of entries returned. |
| Success | Boolean | true | Indicates whether the HTTP request was successful. |
| Module | String | ndr*** | The name of the module. |
| HttpStatusCod e | Integer | 200 | The HTTP status code. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=DescribeAggResetPPS&RegionId=cnhangzhou&Lang=zh&StartTime=1707118672&EndTime=1707118672&DstIP=1.1.1.1&SrcIP=1.1.1.1&Acti Type=pass&AliUid=1234567890&RuleID=12323
```

Sample success responses `JSON` format

```
Content-Type:application/json
```

`{`

```json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "TaskUUID":"F0A8A039-930D-5EC1-97C8-************",
    "TotalCount":100,
    "DataList":[
```

`{`

```json
            "Time":1707148800,
            "Count":100,
            "Date":""
```

`}` `],`

```json
    "Success":true,
    "Module":"ndr***",
    "HttpStatusCode":200
```

`}` `XML` format

```xml
Content-Type:application/xml <DescribeAggResetPPSResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <TaskUUID>F0A8A039-930D-5EC1-97C8-************</TaskUUID>
    <TotalCount>100</TotalCount>
    <DataList>
        <Date></Date>
        <Count>100</Count>
        <Time>1707148800</Time>
    </DataList>
    <Success>true</Success>
    <Module>ndr***</Module>
    <HttpStatusCode>200</HttpStatusCode>
</DescribeAggResetPPSResponse>
```

##### DescribeAggResetTopIPRecords

Queries the top five IP addresses based on blocked traffic logs.

**Authorization information**

| Operation | Access level | Resource type |
|---|---|---|
| yundun- cloudfirewall:DescribeAggReset TopIPRecords | Read | acs:yundun-cloudfirewall:*: {#accountId}:* |

**Throttling**

You can call this operation up to 10 times per second per account. You can call this operation up to 100 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Lang | Strin g | Query | No | zh | The language. Valid values: zh and en. You can leave this parameter empty if it is not required for your business. |

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| StartTime | Long | Query | No | 1707118672 | The beginning of the time range to query. |
| EndTime | Long | Query | No | 1707118672 | The end of the time range to query. |
| DstIP | Strin g | Query | No | 1.1.1.1 | The destination IP address. |
| SrcIP | Strin g | Query | No | 1.1.1.1 | The source IP address. |
| ActionTyp e | Strin g | Query | No | pass | The protection type. A value of pass indicates that access is allowed. A value of alert indicates that access is observed. A value of drop indicates that access is blocked. |
| AliUid | Strin g | Query | No | 1234567890 | The user ID. |
| IPType | Strin g | Query | No | 1 | The type of the service to which the IP address belongs. A value of 0 indicates others. A value of 1 indicates Web Application Firewall (WAF). A value of 2 indicates Server Load Balancer (SLB). A value of 3 indicates Elastic IP Address (EIP). A value of 4 indicates Elastic Compute Service (ECS). |
| RuleID | Long | Query | No | 12323 | The hit rule ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| TaskUUID | String | F0A8A039-930D- 5EC1-97C8- ************ | The UUID of the asynchronous query task. |

| Developer Guide·A on | PI documentat |   | Cloud Security Network Detecti n and Respons |
|---|---|---|---|
| Parameter | Type | Example | Description |
| TaskStatus | Integer | 1 | The status of the asynchronous query task. A value of 0 indicates that the task is in progress. A value of 1 indicates that the task is complete. |
| Success | Boolean | true | Indicates whether the HTTP request was successful. |
| Module | String | ndr*** | The name of the module. |
| HttpStatusCod e | Integer | 200 | The HTTP status code. |
| ResetLogData | Struct |   |   |
| -DataList | Array |   |   |
| --IP | String | 1.1.1.1 | The IP address. |
| --Count | Integer | 100 | The number of attacks. |
| -TotalCount | Integer | 100 | The total number of entries returned. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=DescribeAggResetTopIPRecords&RegionId=cnhangzhou&Lang=zh&StartTime=1707118672&EndTime=1707118672&DstIP=1.1.1.1&SrcIP=1.1.1.1&Acti Type=pass&AliUid=1234567890&IPType=test&RuleID=12323
```

Sample success responses `JSON` format

```
Content-Type:application/json
```

`{`

```json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "TaskUUID":"F0A8A039-930D-5EC1-97C8-************",
    "TaskStatus":1,
    "ResetLogData":{
        "DataList":[
```

`{`

```json
                "IP":"1.1.1.1",
                "Count":100
```

`}` `],`

```json
        "TotalCount":100
```

`},`

```json
    "Success":true,
    "Module":"ndr***",
    "HttpStatusCode":200
```

`}` `XML` format

```xml
Content-Type:application/xml <DescribeAggResetTopIPRecordsResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <TaskUUID>F0A8A039-930D-5EC1-97C8-************</TaskUUID>
    <TaskStatus>1</TaskStatus>
    <ResetLogData>
        <TotalCount>100</TotalCount>
        <DataList>
            <IP>1.1.1.1</IP>
            <Count>100</Count>
        </DataList>
    </ResetLogData>
    <Success>true</Success>
    <Module>ndr***</Module>
    <HttpStatusCode>200</HttpStatusCode>
</DescribeAggResetTopIPRecordsResponse>
```

##### DescribeAggResetRecords

Queries the logs of blocked traffic.

**Authorization information**

| Operation | Access level | Resource type |
|---|---|---|
| yundun- cloudfirewall:DescribeAggReset Records | Read | acs:yundun-cloudfirewall:*: {#accountId}:* |

**Throttling**

You can call this operation up to 10 times per second per account. You can call this operation up to 100 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Lang | Strin g | Query | No | zh | The language. Valid values: zh and en. You can leave this parameter empty if it is not required for your business. |
| CurrentPa ge | Strin g | Query | No | 1 | The page number. |
| PageSize | Strin g | Query | No | 10 | The number of entries per page. |
| StartTime | Long | Query | No | 1707118672 | The beginning of the time range to query. |
| EndTime | Long | Query | No | 1707118672 | The end of the time range to query. |
| DstIP | Strin g | Query | No | 1.1.1.1 | The destination IP address. |
| SrcIP | Strin g | Query | No | 1.1.1.1 | The source IP address. |

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| ActionTyp e | Strin g | Query | No | pass | The protection type. A value of pass indicates that access is allowed. A value of alert indicates that access is observed. A value of drop indicates that access is blocked. |
| AliUid | Strin g | Query | No | 1234567890 | The user ID. |
| RuleID | Long | Query | No | 12323 | The hit rule ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| TaskUUID | String | F0A8A039-930D- 5EC1-97C8- ************ | The UUID of the asynchronous query task. |
| TaskStatus | Integer | 1 | The status of the asynchronous query task. A value of 0 indicates that the task is in progress. A value of 1 indicates that the task is complete. |
| Success | Boolean | true | Indicates whether the HTTP request was successful. |
| Module | String | ndr*** | The name of the module. |
| HttpStatusCod e | Integer | 200 | The HTTP status code. |
| ResetLogData | Struct |   |   |
| -DataList | Array |   |   |
| --SrcIP | String | 1.1.1.1 | The source IP address. |
| --DstIP | String | 1.1.1.1 | The destination IP address. |
| --DstPort | String | 80 | The destination port. |

| Developer Guide·A on | PI documentat |   | Cloud Security Network Detecti n and Respons |
|---|---|---|---|
| Parameter | Type | Example | Description |

| --CreateTime | String | 2024-02- 06T12:46:36+08:0 0 | The time when the log was generated. |
|---|---|---|---|
| --ActionType | String | pass | The protection type. A value of pass indicates that access is allowed. A value of alert indicates that access is observed. A value of drop indicates that access is blocked. |
| --RuleID | String | 12323 | The hit rule ID. |
| --Count | String | 100 | The number of attacks. |
| --Origin | Integer | 100 | The rule type. A value of 1 indicates a Layer 4 access control list (ACL) blocking rule. A value of 2 indicates a Layer 7 blocking rule. A value of 3 indicates a threat intelligence rule. A value of 4 indicates a port spoofing rule. |
| --IsExisted | Boolean | false | Indicates whether the rule still exists. Valid values: true and false. |
| --AliUid | Long | 1234567890 | The user ID. |
| --IsGlobal | Boolean | false | Indicates whether the rule is a global rule. Valid values: true and false. |
| --RuleName | String | test | The name of the rule. |
| -TotalCount | Integer | 100 | The total number of entries returned. |
| -PageSize | Integer | 10 | The number of entries per page. |
| -CurrentPage | Integer | 1 | The page number. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=DescribeAggResetRecords&RegionId=cnhangzhou&Lang=zh&CurrentPage=1&PageSize=10&StartTime=1707118672&EndTime=1707118672&DstIP= 1.1.1&SrcIP=1.1.1.1&ActionType=pass&AliUid=1234567890&RuleID=12323
```

Sample success responses `JSON` format

```
Content-Type:application/json
```

`{`

```json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "TaskUUID":"F0A8A039-930D-5EC1-97C8-************",
    "TaskStatus":1,
    "ResetLogData":{
        "DataList":[
```

`{`

```json
                "Origin":100,
                "ActionType":"pass",
                "CreateTime":"2024-02-06T12:46:36+08:00",
                "RuleID":"12323",
                "IsExisted":false,
                "DstIP":"1.1.1.1",
                "DstPort":"80",
                "Count":"100",
                "SrcIP":"1.1.1.1",
                "IsGlobal":false,
                "RuleName":"test",
                "AliUid":1234567890
```

`}` `],`

```json
        "TotalCount":100,
        "PageSize":10,
        "CurrentPage":1
```

`},`

```json
    "Success":true,
    "Module":"ndr***",
    "HttpStatusCode":200
```

`}` `XML` format

```xml
Content-Type:application/xml <DescribeAggResetRecordsResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <TaskUUID>F0A8A039-930D-5EC1-97C8-************</TaskUUID>
    <TaskStatus>1</TaskStatus>
    <ResetLogData>
        <TotalCount>100</TotalCount>
        <PageSize>10</PageSize>
        <CurrentPage>1</CurrentPage>
        <DataList>
            <SrcIP>1.1.1.1</SrcIP>
            <DstIP>1.1.1.1</DstIP>
            <DstPort>80</DstPort>
            <CreateTime>2024-02-06T12:46:36+08:00</CreateTime>
            <ActionType>pass</ActionType>
            <RuleID>12323</RuleID>
            <Count>100</Count>
            <Origin>100</Origin>
            <IsExisted>false</IsExisted>
            <AliUid>1234567890</AliUid>
            <IsGlobal>false</IsGlobal>
            <RuleName>test</RuleName>
        </DataList>
    </ResetLogData>
    <Success>true</Success>
    <Module>ndr***</Module>
    <HttpStatusCode>200</HttpStatusCode>
</DescribeAggResetRecordsResponse>
```

##### DescribeAggResetDayCount

Asynchronously queries the number of attacks by day based on blocked traffic logs.

**Authorization information**

| Operation | Access level | Resource type |
|---|---|---|
| yundun- cloudfirewall:DescribeAggReset DayCount | Read | acs:yundun-cloudfirewall:*: {#accountId}:* |

**Throttling**

You can call this operation up to 10 times per second per account. You can call this operation up to 100 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Lang | Strin g | Query | No | zh | The language. Valid values: zh and en. You can leave this parameter empty if it is not required for your business. |
| StartTime | Long | Query | No | 1707118672 | The beginning of the time range to query. |
| EndTime | Long | Query | No | 1707118672 | The end of the time range to query. |
| DstIP | Strin g | Query | No | 1.1.1.1 | The destination IP address. |
| SrcIP | Strin g | Query | No | 1.1.1.1 | The source IP address. |
| ActionTyp e | Strin g | Query | No | pass | The protection type. A value of pass indicates that access is allowed. A value of alert indicates that access is observed. A value of drop indicates that access is blocked. |
| AliUid | Strin g | Query | No | 1234567890 | The user ID. |
| RuleID | Long | Query | No | 12323 | The hit rule ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| DataList | Array |   |   |
| -Date | String |   | The log date. This parameter is discontinued. |
| -Count | Integer | 100 | The number of attacks. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| -Time | Long | 1707148800 | The timestamp. |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| TaskUUID | String | F0A8A039-930D- 5EC1-97C8- ************ | The UUID of the asynchronous query task. |
| TotalCount | Integer | 100 | The total number of entries returned. |
| Success | Boolean | true | Indicates whether the HTTP request was successful. |
| Module | String | ndr*** | The name of the module. |
| HttpStatusCod e | Integer | 200 | The HTTP status code. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=DescribeAggResetDayCount&RegionId=cnhangzhou&Lang=zh&StartTime=1707118672&EndTime=1707118672&DstIP=1.1.1.1&SrcIP=1.1.1.1&Acti Type=pass&AliUid=1234567890&RuleID=12323
```

Sample success responses `JSON` format

```
Content-Type:application/json
```

`{`

```json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "TaskUUID":"F0A8A039-930D-5EC1-97C8-************",
    "TotalCount":100,
    "DataList":[
```

`{`

```json
            "Time":1707148800,
            "Count":100,
            "Date":""
```

`}` `],`

```json
    "Success":true,
    "Module":"ndr***",
    "HttpStatusCode":200
```

`}` `XML` format

```xml
Content-Type:application/xml <DescribeAggResetDayCountResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <TaskUUID>F0A8A039-930D-5EC1-97C8-************</TaskUUID>
    <TotalCount>100</TotalCount>
    <DataList>
        <Date></Date>
        <Count>100</Count>
        <Time>1707148800</Time>
    </DataList>
    <Success>true</Success>
    <Module>ndr***</Module>
    <HttpStatusCode>200</HttpStatusCode>
</DescribeAggResetDayCountResponse>
```

##### DescribeAggResetRecordsData

Asynchronously queries the logs of blocked traffic.

**Authorization information**

| Operation | Access level | Resource type |
|---|---|---|
| yundun- cloudfirewall:DescribeAggReset RecordsData | Read | acs:yundun-cloudfirewall:*: {#accountId}:* |

**Throttling**

You can call this operation up to 10 times per second per account. You can call this operation up to 100 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Lang | Strin g | Query | No | zh | The language. Valid values: zh and en. You can leave this parameter empty if it is not required for your business. |

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| TaskUUID | Strin g | Query | No | F0A8A039-930D-5EC1- 97C8-************ | The UUID of the asynchronous query task. |
| AliUid | Strin g | Query | No | 1234567890 | The user ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| TaskUUID | String | F0A8A039-930D- 5EC1-97C8- ************ | The UUID of the asynchronous query task. |
| TaskStatus | Integer | 1 | The status of the asynchronous query task. A value of 0 indicates that the task is in progress. A value of 1 indicates that the task is complete. |
| Success | Boolean | true | Indicates whether the HTTP request was successful. |
| Module | String | ndr*** | The name of the module. |
| HttpStatusCod e | Integer | 200 | The HTTP status code. |
| ResetLogData | Struct |   |   |
| -DataList | Array |   |   |
| --SrcIP | String | 1.1.1.1 | The source IP address. |
| --DstIP | String | 1.1.1.1 | The destination IP address. |
| --DstPort | String | 80 | The destination port. |
| --CreateTime | String | 2024-02- 06T12:46:36+08:0 0 | The time when the record was logged. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| --ActionType | String | pass | The protection type. A value of pass indicates that access is allowed. A value of alert indicates that access is observed. A value of drop indicates that access is blocked. |
| --RuleID | String | 12323 | The hit rule ID. |
| --Count | String | 100 | The number of attacks. |
| --Origin | Integer | 1 | The rule type. A value of 1 indicates a Layer 4 access control list (ACL) blocking rule. A value of 2 indicates a Layer 7 blocking rule. A value of 3 indicates a threat intelligence rule. A value of 4 indicates a port spoofing rule. |
| --IsExisted | Boolean | false | Indicates whether the rule still exists. Valid values: true and false. |
| --AliUid | Long | 1234567890 | The user ID. |
| --IsGlobal | Boolean | false | Indicates whether the rule is a global rule. Valid values: true and false. |
| --RuleName | String | test | The name of the rule. |
| -TotalCount | Integer | 100 | The total number of entries returned. |
| -PageSize | Integer | 10 | The number of entries per page. |
| -CurrentPage | Integer | 1 | The page number. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=DescribeAggResetRecordsData&RegionId=cnhangzhou&Lang=zh&TaskUUID=F0A8A039-930D-5EC1-97C8-************&AliUid=1234567890
```

Sample success responses `JSON` format

```
Content-Type:application/json
```

`{`

```json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "TaskUUID":"F0A8A039-930D-5EC1-97C8-************",
    "TaskStatus":1,
    "ResetLogData":{
        "DataList":[
```

`{`

```json
                "Origin":100,
                "ActionType":"pass",
                "CreateTime":"2024-02-06T12:46:36+08:00",
                "RuleID":"12323",
                "IsExisted":false,
                "DstIP":"1.1.1.1",
                "DstPort":"80",
                "Count":"100",
                "SrcIP":"1.1.1.1",
                "IsGlobal":false,
                "RuleName":"test",
                "AliUid":1234567890
```

`}` `],`

```json
        "TotalCount":100,
        "PageSize":10,
        "CurrentPage":1
```

`},`

```json
    "Success":true,
    "Module":"ndr***",
    "HttpStatusCode":200
```

`}` `XML` format

```xml
Content-Type:application/xml <DescribeAggResetRecordsDataResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <TaskUUID>F0A8A039-930D-5EC1-97C8-************</TaskUUID>
    <TaskStatus>1</TaskStatus>
    <ResetLogData>
        <TotalCount>100</TotalCount>
        <PageSize>10</PageSize>
        <CurrentPage>1</CurrentPage>
        <DataList>
            <SrcIP>1.1.1.1</SrcIP>
            <DstIP>1.1.1.1</DstIP>
            <DstPort>80</DstPort>
            <CreateTime>2024-02-06T12:46:36+08:00</CreateTime>
            <ActionType>pass</ActionType>
            <RuleID>12323</RuleID>
            <Count>100</Count>
            <Origin>100</Origin>
            <IsExisted>false</IsExisted>
            <AliUid>1234567890</AliUid>
            <IsGlobal>false</IsGlobal>
            <RuleName>test</RuleName>
        </DataList>
    </ResetLogData>
    <Success>true</Success>
    <Module>ndr***</Module>
    <HttpStatusCode>200</HttpStatusCode>
</DescribeAggResetRecordsDataResponse>
```

### Behavior Analysis

#### DNS Behavior Analysis

##### GetBhaAggDnsTunnelRule

Queries the information about the rule for detecting DNS tunneling attacks.

**Authorization information**

| Operation | Access level | Resource type |
|---|---|---|
| yundun- cloudfirewall:GetBhaAggDnsTu nnelRule | Read | acs:yundun-cloudfirewall:*: {#accountId}:* |

**Throttling**

You can call this operation up to 10 times per second per account. You can call this operation up to 100 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Lang | Strin g | Query | No | zh | The language. Valid values: zh and en. You can leave this parameter empty if it is not required for your business. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| RangeTime | Integer | 100 | The time range to query. |
| Length | Integer | 10 | The length of the result. |
| Count | Integer | 10 | The number of entries returned. |
| Success | Boolean | true | Indicates whether the HTTP request was successful. |
| Module | String | ndr*** | The name of the module. |
| HttpStatusCod e | Integer | 200 | The HTTP status code. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=GetBhaAggDnsTunnelRule&RegionId=cn-hangzhou&Lang=zh
```

Sample success responses `JSON` format

```
Content-Type:application/json
```

`{`

```json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "RangeTime":100,
    "Length":10,
    "Count":10,
    "Success":true,
    "Module":"ndr***",
    "HttpStatusCode":200
```

`}` `XML` format

```xml
Content-Type:application/xml <GetBhaAggDnsTunnelRuleResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <RangeTime>100</RangeTime>
    <Length>10</Length>
    <Count>10</Count>
    <Success>true</Success>
    <Module>ndr***</Module>
    <HttpStatusCode>200</HttpStatusCode>
</GetBhaAggDnsTunnelRuleResponse>
```

##### GetBhaDnsWhiteList

Queries the whitelist for DNS behavior analysis.

**Authorization information**

| Operation | Access level | Resource type |
|---|---|---|
| yundun- cloudfirewall:GetBhaDnsWhiteLi st | Read | acs:yundun-cloudfirewall:*: {#accountId}:* |

**Throttling**

You can call this operation up to 10 times per second per account. You can call this operation up to 100 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Lang | Strin g | Query | No | zh | The language. Valid values: zh and en. You can leave this parameter empty if it is not required for your business. |
| AliUid | Strin g | Query | No | 123456789 | The user ID. |
| Domain | Strin g | Query | No | xxx.com | The domain name. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| DataList | Array |   |   |
| -Domain | String | xxx.com | The domain name. |
| -AliUid | String | 123456789 | The user ID. |
| -CreatTime | String | 2020-12-31 16:30:36 | The time when the DNS behavior was logged. |
| -Id | String | 10 | The ID. |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| TotalCount | Integer | 100 | The total number of entries returned. |
| Module | String | ndr*** | The name of the module. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=GetBhaDnsWhiteList&RegionId=cnhangzhou&Lang=zh&AliUid=123456789&Domain=xxx.com
```

Sample success responses `JSON` format

```
Content-Type:application/json
```

`{`

```json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "TotalCount":100,
    "DataList":[
```

`{`

```json
            "CreatTime":"2020-12-31 16:30:36",
            "Id":"10",
            "Domain":"xxx.com",
            "AliUid":"123456789"
```

`}` `],`

```json
    "Module":"ndr***"
```

`}` `XML` format

```xml
Content-Type:application/xml <GetBhaDnsWhiteListResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <TotalCount>100</TotalCount>
    <DataList>
        <Domain>xxx.com</Domain>
        <AliUid>123456789</AliUid>
        <CreatTime>2020-12-31 16:30:36</CreatTime>
        <Id>10</Id>
    </DataList>
    <Module>ndr***</Module>
</GetBhaDnsWhiteListResponse>
```

##### GetBhaDnsTunnelAggTopHost

Queries the statistics on domain names involved in DNS tunneling attacks.

**Authorization information**

| Operation | Access level | Resource type |
|---|---|---|
| yundun- cloudfirewall:GetBhaDnsTunnel AggTopHost | Read | acs:yundun-cloudfirewall:*: {#accountId}:* |

**Throttling**

You can call this operation up to 10 times per second per account. You can call this operation up to 100 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Lang | Strin g | Query | No | zh | The language. Valid values: zh and en. You can leave this parameter empty if it is not required for your business. |
| StartTime | Long | Query | Yes | 1706668721 | The beginning of the time range to query. |
| EndTime | Long | Query | Yes | 1706668721 | The end of the time range to query. |
| AliUid | Strin g | Query | No | 123456789 | The user ID. |
| SrcIP | Strin g | Query | No | 10.x.x.x | The source IP address. |
| Domain | Strin g | Query | No | xxx.com | The domain name. |
| DepAliUid | Strin g | Query | No | 1234567890 | The department ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| DataList | Array |   |   |
| -Domain | String | xxx.com | The domain name. |
| -Count | Integer | 100 | The number of detected DNS tunneling attacks associated with the domain name. |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| TotalCount | Integer | 100 | The total number of entries returned. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Success | Boolean | true | Indicates whether the HTTP request was successful. |
| Module | String | ndr*** | The name of the module. |
| HttpStatusCod e | Integer | 200 | The HTTP status code. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=GetBhaDnsTunnelAggTopHost&RegionId=cnhangzhou&Lang=zh&StartTime=1706668721&EndTime=1706668721&AliUid=123456789&SrcIP=10.x.x.x& main=xxx.com&DepAliUid=1234567890
```

Sample success responses `JSON` format

```
Content-Type:application/json
```

`{`

```json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "TotalCount":100,
    "DataList":[
```

`{`

```json
            "Count":100,
            "Domain":"xxx.com"
```

`}` `],`

```json
    "Success":true,
    "Module":"ndr***",
    "HttpStatusCode":200
```

`}` `XML` format

```xml
Content-Type:application/xml <GetBhaDnsTunnelAggTopHostResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <TotalCount>100</TotalCount>
    <DataList>
        <Domain>xxx.com</Domain>
        <Count>100</Count>
    </DataList>
    <Success>true</Success>
    <Module>ndr***</Module>
    <HttpStatusCode>200</HttpStatusCode>
</GetBhaDnsTunnelAggTopHostResponse>
```

##### AddBhaDnsWhiteList

Adds a domain name to the whitelist for DNS behavior analysis.

**Authorization information**

| Operation | Access level | Resource type |
|---|---|---|
| yundun- cloudfirewall:AddBhaDnsWhiteL ist | Write | acs:yundun-cloudfirewall:*: {#accountId}:* |

**Throttling**

You can call this operation up to 10 times per second per account. You can call this operation up to 100 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Lang | Strin g | Query | No | zh | The language. Valid values: zh and en. You can leave this parameter empty if it is not required for your business. |

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| AliUid | Strin g | Query | No | 1234567890 | The user ID. |
| Domain | Strin g | Query | No | test.com | The domain name. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Module | String | ndr*** | The name of the module. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=AddBhaDnsWhiteList&RegionId=cnhangzhou&Lang=zh&AliUid=1234567890&Domain=test.com
```

Sample success responses `JSON` format

```
Content-Type:application/json
```

`{`

```json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "Module":"ndr***"
```

`}` `XML` format

```xml
Content-Type:application/xml <AddBhaDnsWhiteListResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <Module>ndr***</Module>
</AddBhaDnsWhiteListResponse>
```

##### ExportBhaAggDnsRecords

Exports aggregated attack logs for DNS behavior analysis.

**Authorization information**

| Operation | Access level | Resource type |
|---|---|---|
| yundun- cloudfirewall:ExportBhaAggDns Records | Write | acs:yundun-cloudfirewall:*: {#accountId}:* |

**Throttling**

You can call this operation up to 10 times per second per account. You can call this operation up to 100 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Lang | Strin g | Query | No | zh | The language. Valid values: zh and en. You can leave this parameter empty if it is not required for your business. |
| StartTime | Long | Query | Yes | 1706668721 | The beginning of the time range to query. |
| EndTime | Long | Query | Yes | 1706668721 | The end of the time range to query. |
| AliUid | Strin g | Query | No | 123456789 | The user ID. |
| SrcIP | Strin g | Query | No | 10.x.x.x | The source IP address. |
| Domain | Strin g | Query | No | xxx.com | The domain name. |
| AttackTyp e | Strin g | Query | No | http | The attack type. |
| DepAliUid | Strin g | Query | No | 1234567890 | The department ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| ExportFileNam e | String | test.csv | The name of the file. |
| ExportFileUrl | String | https://xxx.com | The download URL of the file. |
| TaskUUID | String | cfa13285-5330- 402e-xxx- 5075c12c6aa8 | The export task ID. |
| Success | Boolean | true | Indicates whether the HTTP request was successful. |
| Module | String | ndr*** | The name of the module. |
| HttpStatusCod e | Integer | 200 | The HTTP status code. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=ExportBhaAggDnsRecords&RegionId=cnhangzhou&Lang=zh&StartTime=1706668721&EndTime=1706668721&AliUid=123456789&SrcIP=10.x.x.x& main=xxx.com&AttackType=http&DepAliUid=1234567890
```

Sample success responses `JSON` format

```
Content-Type:application/json
```

`{`

```json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "ExportFileName":"test.csv",
    "ExportFileUrl":"https://xxx.com",
    "TaskUUID":"cfa13285-5330-402e-xxx-5075c12c6aa8",
    "Success":true,
    "Module":"ndr***",
    "HttpStatusCode":200
```

`}` `XML` format

```xml
Content-Type:application/xml <ExportBhaAggDnsRecordsResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <ExportFileName>test.csv</ExportFileName>
    <ExportFileUrl>https://xxx.com</ExportFileUrl>
    <TaskUUID>cfa13285-5330-402e-xxx-5075c12c6aa8</TaskUUID>
    <Success>true</Success>
    <Module>ndr***</Module>
    <HttpStatusCode>200</HttpStatusCode>
</ExportBhaAggDnsRecordsResponse>
```

##### GetBhaAggDnsRecords

Queries the aggregated attack logs for DNS behavior analysis.

**Authorization information**

| Operation | Access level | Resource type |
|---|---|---|
| yundun- cloudfirewall:GetBhaAggDnsRe cords | Read | acs:yundun-cloudfirewall:*: {#accountId}:* |

**Throttling**

You can call this operation up to 10 times per second per account. You can call this operation up to 100 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Lang | Strin g | Query | No | zh | The language. Valid values: zh and en. You can leave this parameter empty if it is not required for your business. |
| CurrentPa ge | Integ er | Query | No | 1 | The page number. |
| PageSize | Integ er | Query | No | 10 | The number of entries per page. |

| loud Security and Respon | Network se | Detectio |   | Devel | oper Guide·API documenta io |
|---|---|---|---|---|---|

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| StartTime | Long | Query | No | 1706668721 | The beginning of the time range to query. |
| EndTime | Long | Query | No | 1706668721 | The end of the time range to query. |
| AliUid | Strin g | Query | No | 123456789 | The user ID. |
| SrcIP | Strin g | Query | No | 10.x.x.x | The source IP address. |
| Domain | Strin g | Query | No | xxx.com | The domain name. |
| AttackTyp e | Strin g | Query | No | http | The attack type. |
| DepAliUid | Strin g | Query | No | 1234567890 | The department ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| DataList | Array |   |   |
| -LastTime | String | 2020-12-31 16:30:36 | The time when the request was last initiated. |
| -SrcIp | String | 10.x.x.x | The source IP address. |
| -Department | String | test | The department. |
| -Domain | String | xxx.com | The domain name. |
| -AttackType | String | http | The attack type. |
| -Count | Integer | 10 | The number of times that the DNS behavior was detected. |
| -CreateTime | String | 2020-12-31 16:30:36 | The time when the DNS behavior was logged. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| TotalCount | Integer | 100 | The total number of entries returned. |
| PageSize | Integer | 10 | The number of entries per page. |
| CurrentPage | Integer | 1 | The page number. |
| Success | Boolean | true | Indicates whether the HTTP request was successful. |
| Module | String | ndr*** | The name of the module. |
| HttpStatusCod e | Integer | 200 | The HTTP status code. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=GetBhaAggDnsRecords&RegionId=cnhangzhou&Lang=zh&CurrentPage=1&PageSize=10&StartTime=1706668721&EndTime=1706668721&AliUid 23456789&SrcIP=10.x.x.x&Domain=xxx.com&AttackType=http&DepAliUid=1234567890
```

Sample success responses `JSON` format

```
Content-Type:application/json
```

`{`

```json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "TotalCount":100,
    "PageSize":10,
    "CurrentPage":1,
    "DataList":[
```

`{`

```json
            "Department":"test",
            "CreateTime":"2020-12-31 16:30:36",
            "AttackType":"http",
            "Count":10,
            "Domain":"xxx.com",
            "SrcIp":"10.x.x.x",
            "LastTime":"2020-12-31 16:30:36"
```

`}` `],`

```json
    "Success":true,
    "Module":"ndr***",
    "HttpStatusCode":200
```

`}` `XML` format

```xml
Content-Type:application/xml <GetBhaAggDnsRecordsResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <TotalCount>100</TotalCount>
    <PageSize>10</PageSize>
    <CurrentPage>1</CurrentPage>
    <DataList>
        <LastTime>2020-12-31 16:30:36</LastTime>
        <SrcIp>10.x.x.x</SrcIp>
        <Department>test</Department>
        <Domain>xxx.com</Domain>
        <AttackType>http</AttackType>
        <Count>10</Count>
        <CreateTime>2020-12-31 16:30:36</CreateTime>
    </DataList>
    <Success>true</Success>
    <Module>ndr***</Module>
    <HttpStatusCode>200</HttpStatusCode>
</GetBhaAggDnsRecordsResponse>
```

##### GetBhaAggDnsRecordsDetail

Queries the attack log details for DNS behavior analysis.

**Authorization information**

| Operation | Access level | Resource type |
|---|---|---|
| yundun- cloudfirewall:GetBhaAggDnsRe cordsDetail | Read | acs:yundun-cloudfirewall:*: {#accountId}:* |

**Throttling**

You can call this operation up to 10 times per second per account. You can call this operation up to 100 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Lang | Strin g | Query | No | zh | The language. Valid values: zh and en. You can leave this parameter empty if it is not required for your business. |
| CurrentPa ge | Integ er | Query | No | 1 | The page number. |
| PageSize | Integ er | Query | No | 10 | The number of entries per page. |
| StartTime | Long | Query | No | 1706668721 | The beginning of the time range to query. |
| EndTime | Long | Query | No | 1706668721 | The end of the time range to query. |
| AliUid | Strin g | Query | No | 123456789 | The user ID. |
| SrcIP | Strin g | Query | No | 10.x.x.x | The source IP address. |
| Domain | Strin g | Query | No | xxx.com | The domain name. |
| DepAliUid | Strin g | Query | No | 1234567890 | The department ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| DataList | Array |   |   |
| -Id | String | 1 | The ID. |
| -SrcIp | String | 10.x.x.x | The source IP address. |
| -Department | String | test | The department. |
| -Domain | String | xxx.com | The domain name. |
| -AttackType | String | http | The attack type. |
| -Count | Integer | 10 | The number of attacks. |
| -CreateTime | String | 2020-12-31 16:30:36 | The time when the attack was logged. |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| TotalCount | Integer | 100 | The total number of entries returned. |
| PageSize | Integer | 10 | The number of entries per page. |
| CurrentPage | Integer | 1 | The page number. |
| Success | Boolean | true | Indicates whether the HTTP request was successful. |
| Module | String | ndr*** | The name of the module. |
| HttpStatusCod e | Integer | 200 | The HTTP status code. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=GetBhaAggDnsRecordsDetail&RegionId=cnhangzhou&Lang=zh&CurrentPage=1&PageSize=10&StartTime=1706668721&EndTime=1706668721&AliUid 23456789&SrcIP=10.x.x.x&Domain=xxx.com&DepAliUid=1234567890
```

Sample success responses `JSON` format

```
Content-Type:application/json
```

`{`

```json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "TotalCount":100,
    "PageSize":10,
    "CurrentPage":1,
    "DataList":[
```

`{`

```json
            "Department":"test",
            "CreateTime":"2020-12-31 16:30:36",
            "AttackType":"http",
            "Id":"1",
            "Count":10,
            "Domain":"xxx.com",
            "SrcIp":"10.x.x.x"
```

`}` `],`

```json
    "Success":true,
    "Module":"ndr***",
    "HttpStatusCode":200
```

`}` `XML` format

```xml
Content-Type:application/xml <GetBhaAggDnsRecordsDetailResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <TotalCount>100</TotalCount>
    <PageSize>10</PageSize>
    <CurrentPage>1</CurrentPage>
    <DataList>
        <Id>1</Id>
        <SrcIp>10.x.x.x</SrcIp>
        <Department>test</Department>
        <Domain>xxx.com</Domain>
        <AttackType>http</AttackType>
        <Count>10</Count>
        <CreateTime>2020-12-31 16:30:36</CreateTime>
    </DataList>
    <Success>true</Success>
    <Module>ndr***</Module>
    <HttpStatusCode>200</HttpStatusCode>
</GetBhaAggDnsRecordsDetailResponse>
```

##### UpdateBhaAggDnsTunnelRule

Modifies the rule for detecting DNS tunneling attacks.

**Authorization information**

| Operation | Access level | Resource type |
|---|---|---|
| yundun- cloudfirewall:UpdateBhaAggDns TunnelRule | Write | acs:yundun-cloudfirewall:*: {#accountId}:* |

**Throttling**

You can call this operation up to 10 times per second per account. You can call this operation up to 100 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Lang | Strin g | Query | No | zh | The language. Valid values: zh and en. You can leave this parameter empty if it is not required for your business. |
| RangeTim e | Integ er | Query | Yes | 100 | The time range. Unit: minutes. |
| Length | Integ er | Query | Yes | 10 | The total length of the DNS domain name. Unit: character. |
| Count | Integ er | Query | Yes | 10 | The number of requests. |

**Response parameters**

| Parameter | Type | Examples | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Module | String | ndr*** | The name of the module. |

| Developer Guide·A on | PI documentat |   | Cloud Security Network Detecti n and Respons |
|---|---|---|---|
| Parameter | Type | Examples | Description |
| Success | Boolean | true | Indicates whether the HTTP request was successful. |
| HttpStatusCod e | Integer | 200 | The HTTP status code. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=UpdateBhaAggDnsTunnelRule&RegionId=cnhangzhou&Lang=zh&RangeTime=100&Length=10&Count=10
```

Sample success responses `JSON` format

```
Content-Type:application/json
```

`{`

```json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "Module":"ndr***",
    "Success":true,
    "HttpStatusCode":200
```

`}` `XML` format

```xml
Content-Type:application/xml <UpdateBhaAggDnsTunnelRuleResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <Module>ndr***</Module>
    <Success>true</Success>
    <HttpStatusCode>200</HttpStatusCode>
</UpdateBhaAggDnsTunnelRuleResponse>
```

##### DeleteBhaDnsWhiteList

Removes a domain name from the whitelist for DNS behavior analysis.

**Authorization information**

| Operation | Access level | Resource type |
|---|---|---|
| yundun- cloudfirewall:DeleteBhaDnsWhit eList | Write | acs:yundun-cloudfirewall:*: {#accountId}:* |

**Throttling**

You can call this operation up to 10 times per second per account. You can call this operation up to 100 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Lang | Strin g | Query | No | zh | The language. Valid values: zh and en. You can leave this parameter empty if it is not required for your business. |
| AliUid | Strin g | Query | No | 1234567890 | The user ID. |
| Domain | Strin g | Query | No | test.com | The domain name. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Module | String | ndr*** | The name of the module. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=DeleteBhaDnsWhiteList&RegionId=cnhangzhou&Lang=zh&AliUid=1234567890&Domain=test.com
```

Sample success responses `JSON` format

```
Content-Type:application/json
```

`{`

```json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "Module":"ndr***"
```

`}` `XML` format

```xml
Content-Type:application/xml <DeleteBhaDnsWhiteListResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <Module>ndr***</Module>
</DeleteBhaDnsWhiteListResponse>
```

##### GetBhaAggAttackDnsHost

Queries the trend of suspicious domain name resolutions.

**Authorization information**

| Operation | Access level | Resource type |
|---|---|---|
| yundun- cloudfirewall:GetBhaAggAttack DnsHost | Read | acs:yundun-cloudfirewall:*: {#accountId}:* |

**Throttling**

You can call this operation up to 10 times per second per account. You can call this operation up to 100 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Lang | Strin g | Query | No | zh | The language. Valid values: zh and en. You can leave this parameter empty if it is not required for your business. |

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| StartTime | Integ er | Query | Yes | 1706668721 | The beginning of the time range to query. |
| EndTime | Integ er | Query | Yes | 1706668721 | The end of the time range to query. |
| AliUid | Strin g | Query | No | 123456789 | The user ID. |
| SrcIP | Strin g | Query | No | 10.x.x.x | The source IP address. |
| Domain | Strin g | Query | No | xxx.com | The domain name. |
| AttackTyp e | Strin g | Query | No | http | The attack type. |
| DepAliUid | Strin g | Query | No | 1234567890 | The department ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| DataList | Array |   |   |
| -Date | String | 2020-12-31 16:30:36 | The date. |
| -Time | Integer | 1706668721 | The timestamp. |
| -Count | Integer | 10 | The number of suspicious domain names. |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| TotalCount | Integer | 100 | The total number of entries returned. |
| Success | Boolean | true | Indicates whether the HTTP request was successful. |
| Module | String | ndr*** | The name of the module. |

| Developer Guide·A on | PI documentat |   | Cloud Security Network Detecti n and Respons |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| HttpStatusCod e | Integer | 200 | The HTTP status code. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=GetBhaAggAttackDnsHost&RegionId=cnhangzhou&Lang=zh&StartTime=1706668721&EndTime=1706668721&AliUid=123456789&SrcIP=10.x.x.x& main=xxx.com&AttackType=http&DepAliUid=1234567890
```

Sample success responses `JSON` format

```
Content-Type:application/json
```

`{`

```json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "TotalCount":100,
    "DataList":[
```

`{`

```json
            "Time":1706668721,
            "Count":10,
            "Date":"2020-12-31 16:30:36"
```

`}` `],`

```json
    "Success":true,
    "Module":"ndr***",
    "HttpStatusCode":200
```

`}` `XML` format

```xml
Content-Type:application/xml <GetBhaAggAttackDnsHostResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <TotalCount>100</TotalCount>
    <DataList>
        <Date>2020-12-31 16:30:36</Date>
        <Time>1706668721</Time>
        <Count>10</Count>
    </DataList>
    <Success>true</Success>
    <Module>ndr***</Module>
    <HttpStatusCode>200</HttpStatusCode>
</GetBhaAggAttackDnsHostResponse>
```

##### GetBhaDgaAggTopHost

Queries the statistics on domain names generated by Domain Generation Algorithm (DGA) in DNS behavior analysis.

**Authorization information**

| Operation | Access level | Resource type |
|---|---|---|
| yundun- cloudfirewall:GetBhaDgaAggTo pHost | Read | acs:yundun-cloudfirewall:*: {#accountId}:* |

**Throttling**

You can call this operation up to 10 times per second per account. You can call this operation up to 100 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Lang | Strin g | Query | No | zh | The language. Valid values: zh and en. You can leave this parameter empty if it is not required for your business. |
| StartTime | Long | Query | Yes | 1706668721 | The beginning of the time range to query. |
| EndTime | Long | Query | Yes | 1706668721 | The end of the time range to query. |
| AliUid | Strin g | Query | No | 123456789 | The user ID. |
| SrcIP | Strin g | Query | No | 10.x.x.x | The source IP address. |
| Domain | Strin g | Query | No | xxx.com | The domain name. |
| DepAliUid | Strin g | Query | No | 1234567890 | The department ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| DataList | Array |   |   |
| -Domain | String | xxx.com | The domain name. |
| -Count | Integer | 100 | The number of times that the domain name was detected. |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| TotalCount | Integer | 100 | The total number of entries returned. |
| Success | Boolean | true | Indicates whether the HTTP request was successful. |
| Module | String | ndr*** | The name of the module. |
| HttpStatusCod e | Integer | 200 | The HTTP status code. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=GetBhaDgaAggTopHost&RegionId=cnhangzhou&Lang=zh&StartTime=1706668721&EndTime=1706668721&AliUid=123456789&SrcIP=10.x.x.x& main=xxx.com&DepAliUid=1234567890
```

Sample success responses `JSON` format

```
Content-Type:application/json
```

`{`

```json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "TotalCount":100,
    "DataList":[
```

`{`

```json
            "Count":100,
            "Domain":"xxx.com"
```

`}` `],`

```json
    "Success":true,
    "Module":"ndr***",
    "HttpStatusCode":200
```

`}` `XML` format

```xml
Content-Type:application/xml <GetBhaDgaAggTopHostResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <TotalCount>100</TotalCount>
    <DataList>
        <Domain>xxx.com</Domain>
        <Count>100</Count>
    </DataList>
    <Success>true</Success>
    <Module>ndr***</Module>
    <HttpStatusCode>200</HttpStatusCode>
</GetBhaDgaAggTopHostResponse>
```

#### Encrypted traffic analysis

##### AddBhaEncryptWhiteList

Adds an IP address to the whitelist of encrypted traffic analysis.

**Authorization information**

| Operation | Access level | Resource type |
|---|---|---|
| yundun- cloudfirewall:AddBhaEncryptWh iteList | Write | acs:yundun-cloudfirewall:*: {#accountId}:* |

**Throttling**

You can call this operation up to 10 times per second per account. You can call this operation up to 100 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Lang | Strin g | Query | No | zh | The language. Valid values: zh and en. You can leave this parameter empty if it is not required for your business. |

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| AliUid | Strin g | Query | No | 1234567890 | The user ID. |
| Ip | Strin g | Query | Yes | 1.1.1.1 | The IP address. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Module | String | ndr*** | The name of the module. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=AddBhaEncryptWhiteList&RegionId=cnhangzhou&Lang=zh&AliUid=1234567890&Ip=1.1.1.1
```

Sample success responses `JSON` format

```
Content-Type:application/json
```

`{`

```json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "Module":"ndr***"
```

`}` `XML` format

```xml
Content-Type:application/xml <AddBhaEncryptWhiteListResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <Module>ndr***</Module>
</AddBhaEncryptWhiteListResponse>
```

##### GetBhaTLsTopApp

Queries the statistics on encrypted traffic types by using TLS.

**Authorization information**

| Operation | Access level | Resource type |
|---|---|---|
| yundun- cloudfirewall:GetBhaTLsTopApp | Read | acs:yundun-cloudfirewall:*: {#accountId}:* |

**Throttling**

You can call this operation up to 10 times per second per account. You can call this operation up to 100 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Lang | Strin g | Query | No | zh | The language. Valid values: zh and en. You can leave this parameter empty if it is not required for your business. |
| StartTime | Long | Query | Yes | 1706668721 | The beginning of the time range to query. |
| EndTime | Long | Query | Yes | 1706668721 | The end of the time range to query. |
| AliUid | Strin g | Query | No | 123456789 | The user ID. |
| SrcIP | Strin g | Query | No | 10.x.x.x | The source IP address. |
| DstIP | Strin g | Query | No | 10.x.x.x | The destination IP address. |
| AttackTool s | Strin g | Query | No | Burpsuite | The attack tools. |
| DepAliUid | Strin g | Query | No | 1234567890 | The department ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| DataList | Array |   |   |
| -AppName | String | DNS | The name of the top application. |
| -Count | Integer | 100 | The number of attacks. |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| TotalCount | Integer | 100 | The total number of entries queried. |
| Success | Boolean | true | Indicates whether the HTTP request was successful. |
| Module | String | ndr*** | The name of the module. |
| HttpStatusCod e | Integer | 200 | The HTTP status code. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=GetBhaTLsTopApp&RegionId=cnhangzhou&Lang=zh&StartTime=1706668721&EndTime=1706668721&AliUid=123456789&SrcIP=10.x.x.x& tIP=10.x.x.x&AttackTools=Burpsuite&DepAliUid=1234567890
```

Sample success responses `JSON` format

```
Content-Type:application/json
```

`{`

```json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "TotalCount":100,
    "DataList":[
```

`{`

```json
            "Count":100,
            "AppName":"DNS"
```

`}` `],`

```json
    "Success":true,
    "Module":"ndr***",
    "HttpStatusCode":200
```

`}` `XML` format

```xml
Content-Type:application/xml <GetBhaTLsTopAppResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <TotalCount>100</TotalCount>
    <DataList>
        <AppName>DNS</AppName>
        <Count>100</Count>
    </DataList>
    <Success>true</Success>
    <Module>ndr***</Module>
    <HttpStatusCode>200</HttpStatusCode>
</GetBhaTLsTopAppResponse>
```

##### DeleteBhaEncryptWhiteList

Remove an IP address from the whitelist for encrypted traffic analysis.

**Authorization information**

| Operation | Access level | Resource type |
|---|---|---|
| yundun- cloudfirewall:DeleteBhaEncrypt WhiteList | Write | acs:yundun-cloudfirewall:*: {#accountId}:* |

**Throttling**

You can call this operation up to 10 times per second per account. You can call this operation up to 100 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Lang | Strin g | Query | No | zh | The language. Valid values: zh and en. You can leave this parameter empty if it is not required for your business. |

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| AliUid | Strin g | Query | No | 1234567890 | The user ID. |
| Ip | Strin g | Query | Yes | 1.1.1.1 | The IP address. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Module | String | ndr*** | The name of the module. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=DeleteBhaEncryptWhiteList&RegionId=cnhangzhou&Lang=zh&AliUid=1234567890&Ip=1.1.1.1
```

Sample success responses `JSON` format

```
Content-Type:application/json
```

`{`

```json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "Module":"ndr***"
```

`}` `XML` format

```xml
Content-Type:application/xml <DeleteBhaEncryptWhiteListResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <Module>ndr***</Module>
</DeleteBhaEncryptWhiteListResponse>
```

##### GetBhaTLsTopDstIP

Queries the top destination IP addresses based on encrypted traffic analysis.

**Authorization information**

| Operation | Access level | Resource type |
|---|---|---|
| yundun- cloudfirewall:GetBhaTLsTopDstI P | Read | acs:yundun-cloudfirewall:*: {#accountId}:* |

**Throttling**

You can call this operation up to 10 times per second per account. You can call this operation up to 100 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Lang | Strin g | Query | No | zh | The language. Valid values: zh and en. You can leave this parameter empty if it is not required for your business. |
| StartTime | Long | Query | Yes | 1706668721 | The beginning of the time range to query. |
| EndTime | Long | Query | Yes | 1706668721 | The end of the time range to query. |
| AliUid | Strin g | Query | No | 123456789 | The user ID. |
| SrcIP | Strin g | Query | No | 10.x.x.x | The source IP address. |
| DstIP | Strin g | Query | No | 10.x.x.x | The destination IP address. |
| AttackTool s | Strin g | Query | No | Burpsuite | The attack tool. |
| DepAliUid | Strin g | Query | No | 1234567890 | The department ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| DataList | Array |   |   |
| -Ip | String | 10.x.x.x | The top attacked IP address. |
| -Count | Integer | 100 | The number of attacks. |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| TotalCount | Integer | 100 | The total number of entries returned. |
| Success | Boolean | true | Indicates whether the HTTP request was successful. |
| Module | String | ndr*** | The name of the module. |
| HttpStatusCod e | Integer | 200 | The HTTP status code. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=GetBhaTLsTopDstIP&RegionId=cnhangzhou&Lang=zh&StartTime=1706668721&EndTime=1706668721&AliUid=123456789&SrcIP=10.x.x.x& tIP=10.x.x.x&AttackTools=Burpsuite&DepAliUid=1234567890
```

Sample success responses `JSON` format

```
Content-Type:application/json
```

`{`

```json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "TotalCount":100,
    "DataList":[
```

`{`

```json
            "Ip":"10.x.x.x",
            "Count":100
```

`}` `],`

```json
    "Success":true,
    "Module":"ndr***",
    "HttpStatusCode":200
```

`}` `XML` format

```xml
Content-Type:application/xml <GetBhaTLsTopDstIPResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <TotalCount>100</TotalCount>
    <DataList>
        <Ip>10.x.x.x</Ip>
        <Count>100</Count>
    </DataList>
    <Success>true</Success>
    <Module>ndr***</Module>
    <HttpStatusCode>200</HttpStatusCode>
</GetBhaTLsTopDstIPResponse>
```

##### GetBhaEncryptWhiteList

Queries the whitelist for encrypted traffic analysis.

**Authorization information**

| Operation | Access level | Resource type |
|---|---|---|
| yundun- cloudfirewall:GetBhaEncryptWh iteList | Read | acs:yundun-cloudfirewall:*: {#accountId}:* |

**Throttling**

You can call this operation up to 10 times per second per account. You can call this operation up to 100 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Lang | Strin g | Query | No | zh | The language. Valid values: zh and en. You can leave this parameter empty if it is not required for your business. |

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| AliUid | Strin g | Query | No | 123456789 | The user ID. |
| Ip | Strin g | Query | No | 10.x.x.x | The IP address. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| DataList | Array |   |   |
| -Ip | String | 10.x.x.x | The IP address. |
| -AliUid | String | 123456789 | The user ID. |
| -CreatTime | String | 2020-12-31 16:30:36 | The time when the IP address was added to the whitelist. |
| -Id | String | 10 | The record ID. |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| TotalCount | Integer | 100 | The total number of entries returned. |
| Success | Boolean | true | Indicates whether the HTTP request was successful. |
| Module | String | ndr*** | The name of the module. |
| HttpStatusCod e | Integer | 200 | The HTTP status code. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=GetBhaEncryptWhiteList&RegionId=cnhangzhou&Lang=zh&AliUid=123456789&Ip=10.x.x.x
```

Sample success responses `JSON` format

```
Content-Type:application/json
```

`{`

```json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "TotalCount":100,
    "DataList":[
```

`{`

```json
            "CreatTime":"2020-12-31 16:30:36",
            "Ip":"10.x.x.x",
            "Id":"10",
            "AliUid":"123456789"
```

`}` `],`

```json
    "Success":true,
    "Module":"ndr***",
    "HttpStatusCode":200
```

`}` `XML` format

```xml
Content-Type:application/xml <GetBhaEncryptWhiteListResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <TotalCount>100</TotalCount>
    <DataList>
        <Ip>10.x.x.x</Ip>
        <AliUid>123456789</AliUid>
        <CreatTime>2020-12-31 16:30:36</CreatTime>
        <Id>10</Id>
    </DataList>
    <Success>true</Success>
    <Module>ndr***</Module>
    <HttpStatusCode>200</HttpStatusCode>
</GetBhaEncryptWhiteListResponse>
```

##### GetBhaAggTlsRecordsDetail

Queries the attack log details for encrypted traffic analysis.

**Authorization information**

| Operation | Access level | Resource type |
|---|---|---|
| yundun- cloudfirewall:GetBhaAggTlsRec ordsDetail | Read | acs:yundun-cloudfirewall:*: {#accountId}:* |

**Throttling**

You can call this operation up to 10 times per second per account. You can call this operation up to 100 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Lang | Strin g | Query | No | zh | The language. Valid values: zh and en. You can leave this parameter empty if it is not required for your business. |
| CurrentPa ge | Integ er | Query | No | 1 | The page number. |
| PageSize | Integ er | Query | No | 10 | The number of entries per page. |
| StartTime | Long | Query | No | 1706668721 | The beginning of the time range to query. |
| EndTime | Long | Query | No | 1706668721 | The end of the time range to query. |
| AliUid | Strin g | Query | No | 123456789 | The user ID. |
| SrcIP | Strin g | Query | No | 10.x.x.x | The source IP address. |
| DstIP | Strin g | Query | No | 10.x.x.x | The destination IP address. |
| AttackTool s | Strin g | Query | No | Burpsuite | The attack tool. |
| DepAliUid | Strin g | Query | No | 1234567890 | The department ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| DataList | Array |   |   |

| C n | loud Security Net and Response | work Detectio |   | Developer Guide·API documenta io | t n |
|---|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| -SrcIp | String | 10.x.x.x | The source IP address. |
| -DstIp | String | 10.x.x.x | The destination IP address. |
| -DstPort | String | 8080 | The destination port. |
| -Protocol | String | http | The exception type. |
| -AttackTools | String | Burpsuite | The attack tool. |
| -Count | Integer | 20 | The number of requests. |
| -CreateTime | String | 2020-12-31 16:30:36 | The time when the attack log was created. |
| -Department | String | test | The department. |
| -LastTime | String | 2020-12-31 16:30:36 | The time when the last request was sent. |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| TotalCount | Integer | 100 | The total number of entries returned. |
| PageSize | Integer | 10 | The number of entries per page. |
| CurrentPage | Integer | 1 | The page number. |
| Success | Boolean | true | Indicates whether the HTTP request was successful. |
| Module | String | ndr*** | The name of the module. |
| HttpStatusCod e | Integer | 200 | The HTTP status code. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=GetBhaAggTlsRecordsDetail&RegionId=cnhangzhou&Lang=zh&CurrentPage=1&PageSize=10&StartTime=1706668721&EndTime=1706668721&AliUid 23456789&SrcIP=10.x.x.x&DstIP=10.x.x.x&AttackTools=Burpsuite&DepAliUid=1234567890
```

Sample success responses `JSON` format

```
Content-Type:application/json
```

`{`

```json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "TotalCount":100,
    "PageSize":10,
    "CurrentPage":1,
    "DataList":[
```

`{`

```json
            "Department":"test",
            "AttackTools":"Burpsuite",
            "CreateTime":"2020-12-31 16:30:36",
            "DstIp":"10.x.x.x",
            "DstPort":"8080",
            "Count":20,
            "Protocol":"http",
            "SrcIp":"10.x.x.x",
            "LastTime":"2020-12-31 16:30:36"
```

`}` `],`

```json
    "Success":true,
    "Module":"ndr***",
    "HttpStatusCode":200
```

`}` `XML` format

```xml
Content-Type:application/xml <GetBhaAggTlsRecordsDetailResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <TotalCount>100</TotalCount>
    <PageSize>10</PageSize>
    <CurrentPage>1</CurrentPage>
    <DataList>
        <SrcIp>10.x.x.x</SrcIp>
        <DstIp>10.x.x.x</DstIp>
        <DstPort>8080</DstPort>
        <Protocol>http</Protocol>
        <AttackTools>Burpsuite</AttackTools>
        <Count>20</Count>
        <CreateTime>2020-12-31 16:30:36</CreateTime>
        <Department>test</Department>
        <LastTime>2020-12-31 16:30:36</LastTime>
    </DataList>
    <Success>true</Success>
    <Module>ndr***</Module>
    <HttpStatusCode>200</HttpStatusCode>
</GetBhaAggTlsRecordsDetailResponse>
```

##### GetBhaTLsTopSrcIP

Queries the top source IP addresses based on encrypted traffic analysis.

**Authorization information**

| Operation | Access level | Resource type |
|---|---|---|
| yundun- cloudfirewall:GetBhaTLsTopSrcI P | Read | acs:yundun-cloudfirewall:*: {#accountId}:* |

**Throttling**

You can call this operation up to 10 times per second per account. You can call this operation up to 100 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Lang | Strin g | Query | No | zh | The language. Valid values: zh and en. You can leave this parameter empty if it is not required for your business. |
| StartTime | Long | Query | Yes | 1706668721 | The beginning of the time range to query. |
| EndTime | Long | Query | Yes | 1706668721 | The end of the time range to query. |
| AliUid | Strin g | Query | No | 123456789 | The user ID. |
| SrcIP | Strin g | Query | No | 10.x.x.x | The source IP address. |
| DstIP | Strin g | Query | No | 10.x.x.x | The destination IP address. |
| AttackTool s | Strin g | Query | No | Burpsuite | The attack tool. |
| DepAliUid | Strin g | Query | No | 1234567890 | The department ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| DataList | Array |   |   |
| -Ip | String | 10.x.x.x | The source IP address that launches the most attacks. |
| -Count | Integer | 100 | The number of attacks. |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| TotalCount | Integer | 100 | The total number of entries returned. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Success | Boolean | true | Indicates whether the HTTP request was successful. |
| Module | String | ndr*** | The name of the module. |
| HttpStatusCod e | Integer | 200 | The HTTP status code. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=GetBhaTLsTopSrcIP&RegionId=cnhangzhou&Lang=zh&StartTime=1706668721&EndTime=1706668721&AliUid=123456789&SrcIP=10.x.x.x& tIP=10.x.x.x&AttackTools=Burpsuite&DepAliUid=1234567890
```

Sample success responses `JSON` format

```
Content-Type:application/json
```

`{`

```json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "TotalCount":100,
    "DataList":[
```

`{`

```json
            "Ip":"10.x.x.x",
            "Count":100
```

`}` `],`

```json
    "Success":true,
    "Module":"ndr***",
    "HttpStatusCode":200
```

`}` `XML` format

```xml
Content-Type:application/xml <GetBhaTLsTopSrcIPResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <TotalCount>100</TotalCount>
    <DataList>
        <Ip>10.x.x.x</Ip>
        <Count>100</Count>
    </DataList>
    <Success>true</Success>
    <Module>ndr***</Module>
    <HttpStatusCode>200</HttpStatusCode>
</GetBhaTLsTopSrcIPResponse>
```

##### GetBhaAggTlsRecords

Queries the aggregated attack logs for encrypted traffic analysis.

**Authorization information**

| Operation | Access level | Resource type |
|---|---|---|
| yundun- cloudfirewall:GetBhaAggTlsRec ords | Read | acs:yundun-cloudfirewall:*: {#accountId}:* |

**Throttling**

You can call this operation up to 10 times per second per account. You can call this operation up to 100 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Lang | Strin g | Query | No | zh | The language. Valid values: zh and en. You can leave this parameter empty if it is not required for your business. |

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| CurrentPa ge | Integ er | Query | Yes | 1 | The page number. |
| PageSize | Integ er | Query | Yes | 10 | The number of entries per page. |
| StartTime | Long | Query | Yes | 1706668721 | The beginning of the time range to query. |
| EndTime | Long | Query | Yes | 1706668721 | The end of the time range to query. |
| AliUid | Strin g | Query | No | 123456789 | The user ID. |
| SrcIP | Strin g | Query | No | 10.x.x.x | The source IP address. |
| DstIP | Strin g | Query | No | 10.x.x.x | The destination IP address. |
| AttackTool s | Strin g | Query | No | Burpsuite | The attack tool. |
| DepAliUid | Strin g | Query | No | 1234567890 | The department ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| DataList | Array |   |   |
| -SrcIp | String | 10.x.x.x | The source IP address. |
| -DstIp | String | 10.x.x.x | The destination IP address. |
| -DstPort | String | 8080 | The destination port. |
| -Protocol | String | http | The exception type. |
| -AttackTools | String | Burpsuite | The attack tool. |
| -Count | Integer | 20 | The number of times that the request was detected. |

| Developer Guide·A on | PI documentat |   | Cloud Security Network Detecti n and Respons |
|---|---|---|---|
| Parameter | Type | Example | Description |
| -CreateTime | String | 2020-12-31 16:30:36 | The time when the request was logged. |
| -Department | String | test | The department. |
| -LastTime | String | 2020-12-31 16:30:36 | The time when the request was last initiated. |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| TotalCount | Integer | 100 | The total number of entries returned. |
| PageSize | Integer | 10 | The number of entries per page. |
| CurrentPage | Integer | 1 | The page number. |
| Success | Boolean | true | Indicates whether the HTTP request was successful. |
| Module | String | ndr*** | The name of the module. |
| HttpStatusCod e | Integer | 200 | The HTTP status code. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=GetBhaAggTlsRecords&RegionId=cnhangzhou&Lang=zh&CurrentPage=1&PageSize=10&StartTime=1706668721&EndTime=1706668721&AliUid 23456789&SrcIP=10.x.x.x&DstIP=10.x.x.x&AttackTools=Burpsuite&DepAliUid=1234567890
```

Sample success responses `JSON` format

```
Content-Type:application/json
```

`{`

```json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "TotalCount":100,
    "PageSize":10,
    "CurrentPage":1,
    "DataList":[
```

`{`

```json
            "Department":"test",
            "AttackTools":"Burpsuite",
            "CreateTime":"2020-12-31 16:30:36",
            "DstIp":"10.x.x.x",
            "DstPort":"8080",
            "Count":20,
            "Protocol":"http",
            "SrcIp":"10.x.x.x",
            "LastTime":"2020-12-31 16:30:36"
```

`}` `],`

```json
    "Success":true,
    "Module":"ndr***",
    "HttpStatusCode":200
```

`}` `XML` format

```xml
Content-Type:application/xml <GetBhaAggTlsRecordsResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <TotalCount>100</TotalCount>
    <PageSize>10</PageSize>
    <CurrentPage>1</CurrentPage>
    <DataList>
        <SrcIp>10.x.x.x</SrcIp>
        <DstIp>10.x.x.x</DstIp>
        <DstPort>8080</DstPort>
        <Protocol>http</Protocol>
        <AttackTools>Burpsuite</AttackTools>
        <Count>20</Count>
        <CreateTime>2020-12-31 16:30:36</CreateTime>
        <Department>test</Department>
        <LastTime>2020-12-31 16:30:36</LastTime>
    </DataList>
    <Success>true</Success>
    <Module>ndr***</Module>
    <HttpStatusCode>200</HttpStatusCode>
</GetBhaAggTlsRecordsResponse>
```

##### GetBhaTLsTopTools

Queries the information about top attack tools.

**Authorization information**

| Operation | Access level | Resource type |
|---|---|---|
| yundun- cloudfirewall:GetBhaTLsTopTool s | Read | acs:yundun-cloudfirewall:*: {#accountId}:* |

**Throttling**

You can call this operation up to 10 times per second per account. You can call this operation up to 100 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Lang | Strin g | Query | No | zh | The language. Valid values: zh and en. You can leave this parameter empty if it is not required for your business. |
| StartTime | Long | Query | Yes | 1706668721 | The beginning of the time range to query. |
| EndTime | Long | Query | Yes | 1706668721 | The end of the time range to query. |
| AliUid | Strin g | Query | No | 123456789 | The user ID. |
| SrcIP | Strin g | Query | No | 10.x.x.x | The source IP address. |
| DstIP | Strin g | Query | No | 10.x.x.x | The destination IP address. |
| AttackTool s | Strin g | Query | No | Burpsuite | The attack tool. |

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| DepAliUid | Strin g | Query | No | 1234567890 | The department ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| DataList | Array |   |   |
| -AppName | String | Burpsuite | The name of the attack tool. |
| -Count | Integer | 100 | The number of attacks. |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| TotalCount | Integer | 100 | The total number of entries returned. |
| Success | Boolean | true | Indicates whether the HTTP request was successful. |
| Module | String | ndr*** | The name of the module. |
| HttpStatusCod e | Integer | 200 | The HTTP status code. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=GetBhaTLsTopTools&RegionId=cnhangzhou&Lang=zh&StartTime=1706668721&EndTime=1706668721&AliUid=123456789&SrcIP=10.x.x.x& tIP=10.x.x.x&AttackTools=Burpsuite&DepAliUid=1234567890
```

Sample success responses `JSON` format

```
Content-Type:application/json
```

`{`

```json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "TotalCount":100,
    "DataList":[
```

`{`

```json
            "Count":100,
            "AppName":"Burpsuite"
```

`}` `],`

```json
    "Success":true,
    "Module":"ndr***",
    "HttpStatusCode":200
```

`}` `XML` format

```xml
Content-Type:application/xml <GetBhaTLsTopToolsResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <TotalCount>100</TotalCount>
    <DataList>
        <AppName>Burpsuite</AppName>
        <Count>100</Count>
    </DataList>
    <Success>true</Success>
    <Module>ndr***</Module>
    <HttpStatusCode>200</HttpStatusCode>
</GetBhaTLsTopToolsResponse>
```

##### ExportBhaAggTlsRecords

Exports aggregated attack logs for encrypted traffic analysis.

**Authorization information**

| Operation | Access level | Resource type |
|---|---|---|
| yundun- cloudfirewall:ExportBhaAggTlsR ecords | Write | acs:yundun-cloudfirewall:*: {#accountId}:* |

**Throttling**

You can call this operation up to 10 times per second per account. You can call this operation up to 100 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Lang | Strin g | Query | No | zh | The language. Valid values: zh and en. You can leave this parameter empty if it is not required for your business. |
| CurrentPa ge | Integ er | Query | Yes | 1 | The page number. |
| PageSize | Integ er | Query | Yes | 10 | The number of entries per page. |
| StartTime | Long | Query | Yes | 1706668721 | The beginning of the time range to query. |
| EndTime | Long | Query | Yes | 1706668721 | The end of the time range to query. |
| AliUid | Strin g | Query | No | 123456789 | The user ID. |
| SrcIP | Strin g | Query | No | 10.x.x.x | The source IP address. |
| DstIP | Strin g | Query | No | 10.x.x.x | The destination IP address. |
| AttackTool s | Strin g | Query | No | Burpsuite | The attack tool. |
| DepAliUid | Strin g | Query | No | 1234567890 | The department ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| ExportFileNam e | String | test.csv | The name of the file. |

| i | Developer Guide·A on | PI documentat |   | Cloud Security Network Detecti n and Respons | o e |
|---|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| ExportFileUrl | String | https://xxx.com | The download URL of the file. |
| TaskUUID | String | cfa13285-5330- 402e-xxx- 5075c12c6aa8 | The export task ID. |
| Success | Boolean | true | Indicates whether the HTTP request was successful. |
| Module | String | ndr*** | The name of the module. |
| HttpStatusCod e | Integer | 200 | The HTTP status code. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=ExportBhaAggTlsRecords&RegionId=cnhangzhou&Lang=zh&CurrentPage=1&PageSize=10&StartTime=1706668721&EndTime=1706668721&AliUid 23456789&SrcIP=10.x.x.x&DstIP=10.x.x.x&AttackTools=Burpsuite&DepAliUid=1234567890
```

Sample success responses `JSON` format

```
Content-Type:application/json
```

`{`

```json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "ExportFileName":"test.csv",
    "ExportFileUrl":"https://xxx.com",
    "TaskUUID":"cfa13285-5330-402e-xxx-5075c12c6aa8",
    "Success":true,
    "Module":"ndr***",
    "HttpStatusCode":200
```

`}` `XML` format

```xml
Content-Type:application/xml <ExportBhaAggTlsRecordsResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <ExportFileName>test.csv</ExportFileName>
    <ExportFileUrl>https://xxx.com</ExportFileUrl>
    <TaskUUID>cfa13285-5330-402e-xxx-5075c12c6aa8</TaskUUID>
    <Success>true</Success>
    <Module>ndr***</Module>
    <HttpStatusCode>200</HttpStatusCode>
</ExportBhaAggTlsRecordsResponse>
```

### Policy configuration

#### Network-layer policy

##### ModL4RuleAction

Modifies the action for network-layer rules.

**Authorization information**

| Operation | Access level | Resource type |
|---|---|---|
| yundun- cloudfirewall:ModL4RuleAction | Write | acs:yundun-cloudfirewall:*: {#accountId}:* |

**Throttling**

You can call this operation up to 10 times per second per account. You can call this operation up to 100 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Lang | Strin g | Query | No | zh | The language. Valid values: zh and en. You can leave this parameter empty if it is not required for your business. |

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| AliUid | Long | Query | No | 123456789 | The user ID. |
| RuleIdList | Strin g | Query | No | 100,101 | The rule IDs. Separate multiple values with commas (,). |
| RuleUuidL ist | Strin g | Query | No | cfa13285-5330-xxx-xxx- 5075c12c6aa8,cfa13285 -5330-xxx-xxx- 5075c12c6aa8 | The rule UUIDs. Separate multiple values with commas (,). |
| ActionTyp e | Strin g | Query | No | pass | The action. A value of pass indicates that access is allowed. A value of alert indicates that access is only logged. A value of drop indicates that access is blocked. |
| User | Strin g | Query | No | admin | The username. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Module | String | ndr*** | The name of the module. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=ModL4RuleAction&RegionId=cnhangzhou&Lang=zh&AliUid=123456789&RuleIdList=100,101&RuleUuidList=cfa13285-5330-xxx-xxx -5075c12c6aa8,cfa13285-5330-xxx-xxx-5075c12c6aa8&ActionType=pass&User=admin
```

Sample success responses `JSON` format

```
Content-Type:application/json
```

`{`

```json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "Module":"ndr***"
```

`}` `XML` format

```xml
Content-Type:application/xml <ModL4RuleActionResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <Module>ndr***</Module>
</ModL4RuleActionResponse>
```

##### ModifySafetySwitch

Modifies the status of a security feature.

**Authorization information**

| Operation | Access level | Resource type |
|---|---|---|
| yundun- cloudfirewall:ModifySafetySwitc h | Write | acs:yundun-cloudfirewall:*: {#accountId}:* |

**Throttling**

You can call this operation up to 10 times per second per account. You can call this operation up to 100 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Lang | Strin g | Query | No | zh | The language. Valid values: zh and en. You can leave this parameter empty if it is not required for your business. |

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| AliUid | Long | Query | No | 123456789 | The user ID. |
| SwitchTyp e | Strin g | Query | No | ids | The security feature that you want to modify. A value of black indicates the feature of blocking multiple IP addresses at a time. A value of ids indicates Intrusion Detection System (IDS). A value of threat indicates threat intelligence. A value of waf indicates Web Application Firewall (WAF). |
| SwitchStat us | Strin g | Query | No | on | The status of the security feature. A value of on indicates that the feature is enabled. A value of off indicates that the feature is disabled. |
| User | Strin g | Query | No | admin | The username. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Module | String | ndr*** | The name of the module. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=ModifySafetySwitch&RegionId=cnhangzhou&Lang=zh&AliUid=123456789&SwitchType=ids&SwitchStatus=on&User=admin
```

Sample success responses `JSON` format

```
Content-Type:application/json
```

`{`

```json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "Module":"ndr***"
```

`}` `XML` format

```xml
Content-Type:application/xml <ModifySafetySwitchResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <Module>ndr***</Module>
</ModifySafetySwitchResponse>
```

##### AddL4Rule

Creates a network-layer rule.

**Authorization information**

| Operation | Access level | Resource type |
|---|---|---|
| yundun- cloudfirewall:AddL4Rule | Write | acs:yundun-cloudfirewall:*: {#accountId}:* |

**Throttling**

You can call this operation up to 10 times per second per account. You can call this operation up to 100 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Lang | Strin g | Query | No | zh | The language. Valid values: zh and en. You can leave this parameter empty if it is not required for your business. |

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| RuleName | Strin g | Query | No | test | The name of the rule. |
| RuleDescr iption | Strin g | Query | No | test | The description of the rule. |
| Direction | Strin g | Query | No | in | The traffic direction. Valid values: in and out. Set the value to in. |
| ActionTyp e | Strin g | Query | No | alert | The action. A value of pass indicates that access is allowed. A value of alert indicates that access is observed. A value of drop indicates that access is blocked. |
| SourceAd dressCidrL ist | Strin g | Query | No | 10.82.0.10/32,10.82.0.1 0/23,10.82.0.10/16 | The source IP addresses. |
| SourceAd dressGrou pUuidList | Strin g | Query | No | cfa13285-5330-402e- 980c-********,cfa13285- 5330-402e-980c-****** | The UUIDs of the source address books. |
| DestAddre ssCidrList | Strin g | Query | No | 10.82.0.10/32,10.82.0.1 0/23,10.82.0.10/16 | The destination IP addresses. |
| DestAddre ssGroupU uidList | Strin g | Query | No | cfa13285-5330-402e- 980c-********,cfa13285- 5330-402e-980c-****** | The UUIDs of the destination address books. |
| SwitchStat us | Strin g | Query | No | online | The status of the rule. A value of online indicates that the rule is enabled. A value of offline indicates that the rule is disabled. |
| StartTime | Strin g | Query | No | 1943432341 | The time when the rule takes effect. |
| EndTime | Strin g | Query | No | 1943432341 | The time when the rule expires. |
| AliUid | Long | Query | No | 1234567890 | The user ID. |

| loud Security and Respon | Network se | Detectio |   | Devel | oper Guide·API documenta io |
|---|---|---|---|---|---|

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| RuleType | Strin g | Query | No | src ip _ | The type of the rule. A value of src ip indicates _ that only source IP addresses are specified for the rule. A value of dst ip indicates that _ only destination IP addresses are specified for the rule. A value of src dst ip indicates that _ _ both source and destination IP addresses are specified for the rule. |
| AddressCi drList | Strin g | Query | No | 127.85.10.10;10.25.0.0/ 16;10.126.11.26:8888;1 0.126.11.8:80 | The IP addresses. |
| AddressFil eNameList | Strin g | Query | No | test.csv | The files to be uploaded. |
| AddressFil eUrlList | Strin g | Query | No | ... | The URLs of the files to be uploaded. |
| AddressFil eObjList | Strin g | Query | No | ... | The file objects to be uploaded. |
| User | Strin g | Query | No | user | The user. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| RuleId | Long | 100 | The rule ID. |
| RuleUuid | String | cfa13285-5330- xxx-xxx- 5075c12c6aa8 | The rule UUID. |
| Module | String | ndr*** | The name of the module. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=AddL4Rule&RegionId=cnhangzhou&Lang=zh&RuleName=test&RuleDescription=test&Direction=in&ActionType=alert&SourceA ressCidrList=10.82.0.10/32,10.82.0.10/23,10.82.0.10/16&SourceAddressGroupUuidList=cfa1328 5330-402e-980c-********,cfa13285-5330-402e-980c-
******&DestAddressCidrList=10.82.0.10/32,10.82.0.10/23,10.82.0.10/16&DestAddressGroupUuid
st=cfa13285-5330-402e-980c-********,cfa13285-5330-402e-980c-
******&SwitchStatus=online&StartTime=1943432341&EndTime=1943432341&AliUid=1234567890&Rule
pe=src_ip&AddressCidrList=127.85.10.10;10.25.0.0/16;10.126.11.26:8888;10.126.11.8:80&Addr sFileNameList=test.csv&AddressFileUrlList=...&AddressFileObjList=...&User=user
```

Sample success responses `JSON` format

```
Content-Type:application/json
```

`{`

```json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "RuleId":100,
    "RuleUuid":"cfa13285-5330-xxx-xxx-5075c12c6aa8",
    "Module":"ndr***"
```

`}` `XML` format

```xml
Content-Type:application/xml <AddL4RuleResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <RuleId>100</RuleId>
    <RuleUuid>cfa13285-5330-xxx-xxx-5075c12c6aa8</RuleUuid>
    <Module>ndr***</Module>
</AddL4RuleResponse>
```

##### ModifyL4Rule

Modifies a network-layer rule.

**Authorization information**

| Operation | Access level | Resource type |
|---|---|---|
| yundun- cloudfirewall:ModifyL4Rule | Write | acs:yundun-cloudfirewall:*: {#accountId}:* |

**Throttling**

You can call this operation up to 10 times per second per account. You can call this operation up to 100 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Lang | Strin g | Query | No | zh | The language. Valid values: zh and en. You can leave this parameter empty if it is not required for your business. |
| RuleName | Strin g | Query | No | bot scanner block _ _ | The name of the rule. |
| RuleDescr iption | Strin g | Query | No | test | The description of the rule. |
| Direction | Strin g | Query | No | in | The traffic direction. Valid values: in and out. |
| ActionTyp e | Strin g | Query | No | pass | The action. A value of pass indicates that access is allowed. A value of alert indicates that access is only logged. A value of drop indicates that access is blocked. |
| SourceAd dressCidrL ist | Strin g | Query | No | 10.82.x.10/32,10.82.x.10 /23,10.82.x.10/16 | The source IP addresses. |
| SourceAd dressGrou pUuidList | Strin g | Query | No | cfa13285-5330-xxx-xxx- 5075c12c6aa8 | The source address books. |
| DestAddre ssCidrList | Strin g | Query | No | 10.82.x.10/32,10.82.x.10 /23,10.82.x.10/16 | The destination IP addresses. |
| DestAddre ssGroupU uidList | Strin g | Query | No | cfa13285-5330-xxx-xxx- 5075c12c6aa8 | The destination IP address books. |

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| SwitchStat us | Strin g | Query | No | online | The status of the rule. A value online indicates that the rule is enabled. A value of offline indicates that the rule is configured but disabled. |
| StartTime | Long | Query | No | 1706668721 | The time when the rule takes effect. |
| EndTime | Long | Query | No | 1706668721 | The time when the rule expires. |
| AliUid | Long | Query | No | 123456789 | The user ID. |
| RuleType | Strin g | Query | No | 1 | The type of the rule. If you set this parameter to 1, you need to specify only source IP addresses for the rule, and you must specify fileNameList, sourceAddressCidrList, and sourceAddressGroupUui d. If you set this parameter to 2, you need to specify only destination IP addresses for the rule, and you must specify fileNameList, destAddressCidrList, and destAddressGroupUuid. If you set this parameter to 3, you need to specify both source and destination IP addresses or ports, and you must specify addressCidrList. |
| AddressCi drList | Strin g | Query | No | 10.82.x.10/32,10.82.x.10 /23,10.82.x.10/16 | The IP addresses. |
| AddressFil eNameList | Strin g | Query | No | filename1,filename2 | The files. |
| AddressFil eUrlList | Strin g | Query | No | fileUrl1,fileUrl2 | The file routes. |
| AddressFil eObjList | Strin g | Query | No | fileObj1,fileObj2 | The file objects. |

| Cloud Security and Respon | Network se | Detectio |   | Devel | oper Guide·API documenta io |
|---|---|---|---|---|---|

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| RuleUuid | Strin g | Query | No | cfa13285-5330-xxx-xxx- 5075c12c6aa8,cfa13285 -5330-xxx-xxx- 5075c12c6aa8 | The rule UUIDs. Separate multiple values with commas (,). |
| User | Strin g | Query | No | admin | The username. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Module | String | ndr*** | The name of the module. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=ModifyL4Rule&RegionId=cnhangzhou&Lang=zh&RuleName=bot_scanner_block&RuleDescription=test&Direction=in&ActionType= ss&SourceAddressCidrList=10.82.x.10/32,10.82.x.10/23,10.82.x.10/16&SourceAddressGroupUuid st=cfa13285-5330-xxx-xxx- 5075c12c6aa8&DestAddressCidrList=10.82.x.10/32,10.82.x.10/23,10.82.x.10/16&DestAddressGro UuidList=cfa13285-5330-xxx-xxx- 5075c12c6aa8&SwitchStatus=online&StartTime=1706668721&EndTime=1706668721&AliUid=123456789 uleType=1&AddressCidrList=10.82.x.10/32,10.82.x.10/23,10.82.x.10/16&AddressFileNameList=f ename1,filename2&AddressFileUrlList=fileUrl1,fileUrl2&AddressFileObjList=fileObj1,fileObj RuleUuid=cfa13285-5330-xxx-xxx-5075c12c6aa8,cfa13285-5330-xxx-xxx- 5075c12c6aa8&User=admin
```

Sample success responses `JSON` format

```
Content-Type:application/json
```

`{`

```json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "Module":"ndr***"
```

`}` `XML` format

```xml
Content-Type:application/xml <ModifyL4RuleResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <Module>ndr***</Module>
</ModifyL4RuleResponse>
```

##### ImportSrcIpFile

Imports a script file.

**Authorization information**

| Operation | Access level | Resource type |
|---|---|---|
| yundun- cloudfirewall:ImportSrcIpFile | Write | acs:yundun-cloudfirewall:*: {#accountId}:* |

**Throttling**

You can call this operation up to 10 times per second per account. You can call this operation up to 100 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Lang | Strin g | Query | No | zh | The language. Valid values: zh and en. You can leave this parameter empty if it is not required for your business. |
| AliUid | Long | Query | No | 123456789 | The user ID. |

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| ModuleNa me | Strin g | Query | No | RuleConfig | The name of the module. Different modules are accessed from different URLs. A value of RuleConfig indicates the policy configuration module. A value of AddressBook indicates the address book management module. |
| FileName | Strin g | Query | No | test | The name of the file to be uploaded. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Host | String | https://xxx.com | The download URL of the file. |
| AccessId | String | xxxyyyzzz | The AccessKey ID used for authentication. |
| AccessKeySecr et | String | xxxyyyzzz | The AccessKey secret used for authentication. |
| Key | String | Import/test | The names of the OSS bucket and the file. |
| Policy | String | Policy information | The information about the policy. |
| Signature | String | Signature information | The signature used for verification. |
| Authorization | String | Authorization information | The authorization information. |
| Module | String | ndr*** | The name of the module. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=ImportSrcIpFile&RegionId=cnhangzhou&Lang=zh&AliUid=123456789&ModuleName=RuleConfig&FileName=test
```

Sample success responses `JSON` format

```
Content-Type:application/json
```

`{`

```json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "Host":"https://xxx.com",
    "AccessId":"xxxyyyzzz",
    "AccessKeySecret":"xxxyyyzzz",
    "Key":"Import/test",
    "Policy":"Policy information",
    "Signature":"Signature information",
    "Authorization":"Authorization information",
    "Module":"ndr***"
```

`}` `XML` format

```xml
Content-Type:application/xml <ImportSrcIpFileResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <Host>https://xxx.com</Host>
    <AccessId>xxxyyyzzz</AccessId>
    <AccessKeySecret>xxxyyyzzz</AccessKeySecret>
    <Key>Import/test</Key>
    <Policy>Policy information</Policy>
    <Signature>Signature information</Signature>
    <Authorization>Authorization information</Authorization>
    <Module>ndr***</Module>
</ImportSrcIpFileResponse>
```

##### DelL4Rule

Deletes one or more network-layer rules.

**Authorization information**

| Operation | Access level | Resource type |
|---|---|---|
| yundun-cloudfirewall:DelL4Rule | Write | acs:yundun-cloudfirewall:*: {#accountId}:* |

**Throttling**

You can call this operation up to 10 times per second per account. You can call this operation up to 100 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Lang | Strin g | Query | No | zh | The language. Valid values: zh and en. You can leave this parameter empty if it is not required for your business. |
| AliUid | Long | Query | No | 1234567890 | The user ID. |
| RuleUuidL ist | Strin g | Query | No | 13285-5330-402e-980c- 5075c12c6xx8,13285- 5330-402e-980c- 5075c12c6yy8 | The UUIDs of the rules that you want to delete. You can delete multiple rules at a time. |
| User | Strin g | Query | No | user | The user. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Module | String | ndr*** | The name of the module. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=DelL4Rule&RegionId=cnhangzhou&Lang=zh&AliUid=1234567890&RuleUuidList=13285-5330-402e-980c- 5075c12c6xx8,13285-5330-402e-980c-5075c12c6yy8&User=user
```

Sample success responses `JSON` format

```
Content-Type:application/json
```

`{`

```json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "Module":"ndr***"
```

`}` `XML` format

```xml
Content-Type:application/xml <DelL4RuleResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <Module>ndr***</Module>
</DelL4RuleResponse>
```

##### ImportL4Rules

Imports network-layer rules.

**Authorization information**

| Operation | Access level | Resource type |
|---|---|---|
| yundun- cloudfirewall:ImportL4Rules | Write | acs:yundun-cloudfirewall:*: {#accountId}:* |

**Throttling**

You can call this operation up to 10 times per second per account. You can call this operation up to 100 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Lang | Strin g | Query | No | zh | The language. Valid values: zh and en. You can leave this parameter empty if it is not required for your business. |

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| AliUid | Long | Query | No | 123456789 | The user ID. |
| ImportTyp e | Integ er | Query | No | 1 | The import method. A value of 0 indicates import based on a downloaded template. A value of 1 indicates incremental import. A value of 2 indicates full import. |
| FileName | Strin g | Query | No | test.csv | The name of the file. |
| FileUrl | Strin g | Query | No | https://xxx.com | The download URL of the file. |
| Object | Strin g | Query | No | xxx | The key used to upload the file. |
| User | Strin g | Query | No | admin | The username. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| TemplateNam e | String | test.csv | The name of the file. |
| TemplateUrl | String | https://xxx.com | The download URL of the file. |
| Module | String | ndr*** | The name of the module. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=ImportL4Rules&RegionId=cnhangzhou&Lang=zh&AliUid=123456789&ImportType=1&FileName=test.csv&FileUrl=https://xxx.com& ject=xxx&User=admin
```

Sample success responses `JSON` format

|   | HTTP/1.1 200 OK Content-Type:application/json { "RequestId":"F0A8A039-930D-5EC1-97C8-************", "TemplateName":"test.csv", "TemplateUrl":"https://xxx.com", "Module":"ndr***" } |   |
|---|---|---|

`XML` format

```xml
Content-Type:application/xml <ImportL4RulesResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <TemplateName>test.csv</TemplateName>
    <TemplateUrl>https://xxx.com</TemplateUrl>
    <Module>ndr***</Module>
</ImportL4RulesResponse>
```

##### DescribeOssInfo

Queries Object Storage Service (OSS) information.

**Authorization information**

| Operation | Access level | Resource type |
|---|---|---|
| yundun- cloudfirewall:DescribeOssInfo | Read | acs:yundun-cloudfirewall:*: {#accountId}:* |

**Throttling**

You can call this operation up to 10 times per second per account. You can call this operation up to 100 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Lang | Strin g | Query | No | zh | The language. Valid values: zh and en. You can leave this parameter empty if it is not required for your business. |
| AliUid | Long | Query | No | 123456789 | The user ID. |
| ModuleNa me | Strin g | Query | No | RuleConfig | The name of the module. Different modules are accessed from different URLs. A value of RuleConfig indicates the policy configuration module. A value of AddressBook indicates the address book management module. |
| FileName | Strin g | Query | No | test | The name of the file that you want to upload. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Host | String | https://xxx.com | The download URL of the file. |
| AccessId | String | xxxyyyzzz | The AccessKey ID used for authentication. |
| AccessKeySecr et | String | xxxyyyzzz | The AccessKey secret used for authentication. |
| Key | String | Import/test | The names of the OSS bucket and the file. |
| Policy | String | Policy information | The information about the policy. |
| Signature | String | Signature information | The signature used for verification. |

| Developer Guide·A | PI documentat |   | Cloud Security Network Detecti |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| Authorization | String | Authorization information | The authorization information. |
| SignedURL | String | https://xxx.com | The authentication path. |
| Module | String | ndr*** | The name of the module. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=DescribeOssInfo&RegionId=cnhangzhou&Lang=zh&AliUid=123456789&ModuleName=RuleConfig&FileName=test
```

Sample success responses `JSON` format

```
Content-Type:application/json
```

`{`

```json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "Host":"https://xxx.com",
    "AccessId":"xxxyyyzzz",
    "AccessKeySecret":"xxxyyyzzz",
    "Key":"Import/test",
    "Policy":"Policy information",
    "Signature":"Signature information",
    "Authorization":"Authorization information",
    "SignedURL":"https://xxx.com",
    "Module":"ndr***"
```

`}` `XML` format

```xml
Content-Type:application/xml <DescribeOssInfoResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <Host>https://xxx.com</Host>
    <AccessId>xxxyyyzzz</AccessId>
    <AccessKeySecret>xxxyyyzzz</AccessKeySecret>
    <Key>Import/test</Key>
    <Policy>Policy information </Policy>
    <Signature>Signature information</Signature>
    <Authorization>Authorization information</Authorization>
    <SignedURL>https://xxx.com</SignedURL>
    <Module>ndr***</Module>
</DescribeOssInfoResponse>
```

##### DescribeSafetySwitchStatus

Queries the status of a security feature.

**Authorization information**

| Operation | Access level | Resource type |
|---|---|---|
| yundun- cloudfirewall:DescribeSafetySwi tchStatus | Read | acs:yundun-cloudfirewall:*: {#accountId}:* |

**Throttling**

You can call this operation up to 10 times per second per account. You can call this operation up to 100 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Lang | Strin g | Query | No | zh | The language. Valid values: zh and en. You can leave this parameter empty if it is not required for your business. |

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| AliUid | Long | Query | No | 123456789 | The user ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| DataList | Array |   |   |
| -SwitchType | String | black | The security feature whose status you want to query. A value of black indicates the feature of blocking multiple IP addresses at a time. A value of ids indicates Intrusion Detection System (IDS). A value of threat indicates threat intelligence. A value of waf indicates Web Application Firewall (WAF). |
| -SwitchStatus | String | on | The status of the security feature. A value of on indicates that the feature is enabled. A value of off indicates that the feature is disabled. |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Module | String | ndr*** | The name of the module. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=DescribeSafetySwitchStatus&RegionId=cnhangzhou&Lang=zh&AliUid=123456789
```

Sample success responses `JSON` format

```
Content-Type:application/json
```

`{`

```json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "DataList":[
```

`{`

```json
            "SwitchType":"black",
            "SwitchStatus":"on"
```

`}` `],`

```json
    "Module":"ndr***"
```

`}` `XML` format

```xml
Content-Type:application/xml <DescribeSafetySwitchStatusResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <DataList>
        <SwitchType>black</SwitchType>
        <SwitchStatus>on</SwitchStatus>
    </DataList>
    <Module>ndr***</Module>
</DescribeSafetySwitchStatusResponse>
```

##### SwitchL4RuleStatus

Modifies the status of a network-layer rule.

**Authorization information**

| Operation | Access level | Resource type |
|---|---|---|
| yundun- cloudfirewall:SwitchL4RuleStatu s | Write | acs:yundun-cloudfirewall:*: {#accountId}:* |

**Throttling**

You can call this operation up to 10 times per second per account. You can call this operation up to 100 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Lang | Strin g | Query | No | zh | The language. Valid values: zh and en. You can leave this parameter empty if it is not required for your business. |
| User | Strin g | Query | No | user | The user. |
| AliUid | Long | Query | No | 123456789 | The user ID. |
| RuleUuidL ist | Strin g | Query | No | cfa13285-5330-xxx-xxx- 5075c12c6aa8,cfa13285 -5330-xxx-xxx- 5075c12c6aa8 | The rule UUIDs. Separate multiple values with commas (,). |
| SwitchStat us | Strin g | Query | No | online | The status of the rule. A value of online indicates that the rule is published and takes effect. A value of offline indicates that the rule is unpublished and does not take effect. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Module | String | ndr*** | The name of the module. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=SwitchL4RuleStatus&RegionId=cnhangzhou&Lang=zh&User=user&AliUid=123456789&RuleUuidList=cfa13285-5330-xxx-xxx-5075c12c 6aa8,cfa13285-5330-xxx-xxx-5075c12c6aa8&SwitchStatus=online
```

Sample success responses `JSON` format

```
Content-Type:application/json
```

`{`

```json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "Module":"ndr***"
```

`}` `XML` format

```xml
Content-Type:application/xml <SwitchL4RuleStatusResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <Module>ndr***</Module>
</SwitchL4RuleStatusResponse>
```

##### ExportL4Rules

Exports network-layer rules.

**Authorization information**

| Operation | Access level | Resource type |
|---|---|---|
| yundun- cloudfirewall:ExportL4Rules | Write | acs:yundun-cloudfirewall:*: {#accountId}:* |

**Throttling**

You can call this operation up to 10 times per second per account. You can call this operation up to 100 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Lang | Strin g | Query | No | zh | The language. Valid values: zh and en. You can leave this parameter empty if it is not required for your business. |

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| AliUid | Long | Query | No | 123456789 | The user ID. |
| ExportTyp e | Strin g | Query | No | batch | The export type. A value of batch indicates that rules are exported in batches. A value of total indicates that all rules are exported. If you set ExportType to batch, you must specify RuleUuidList. |
| RuleUuidL ist | Strin g | Query | No | cfa13285-5330-402e- xxx- 5075c12c6aa8,cfa13285 -5330-402e-xxx- 5075c12c6aa8 | The rule UUIDs. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| ExportFileNam e | String | test.csv | The name of the file. |
| ExportFileUrl | String | https://xxx.com | The download URL of the file. |
| TaskUUID | String | cfa13285-5330- 402e-xxx- 5075c12c6aa8 | The export task ID. |
| Module | String | ndr*** | The name of the module. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=ExportL4Rules&RegionId=cnhangzhou&Lang=zh&AliUid=123456789&ExportType=batch&RuleUuidList=cfa13285-5330-402e-xxx- 5075c12c6aa8,cfa13285-5330-402e-xxx-5075c12c6aa8
```

Sample success responses `JSON` format

```
Content-Type:application/json
```

`{`

```json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "ExportFileName":"test.csv",
    "ExportFileUrl":"https://xxx.com",
    "TaskUUID":"cfa13285-5330-402e-xxx-5075c12c6aa8",
    "Module":"ndr***"
```

`}` `XML` format

```xml
Content-Type:application/xml <ExportL4RulesResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <ExportFileName>test.csv</ExportFileName>
    <ExportFileUrl>https://xxx.com</ExportFileUrl>
    <TaskUUID>cfa13285-5330-402e-xxx-5075c12c6aa8</TaskUUID>
    <Module>ndr***</Module>
</ExportL4RulesResponse>
```

##### DescribeL4Rule

Queries the information about a network-layer rule.

**Authorization information**

| Operation | Access level | Resource type |
|---|---|---|
| yundun- cloudfirewall:DescribeL4Rule | Read | acs:yundun-cloudfirewall:*: {#accountId}:* |

**Throttling**

You can call this operation up to 10 times per second per account. You can call this operation up to 100 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Lang | Strin g | Query | No | zh | The language. Valid values: zh and en. You can leave this parameter empty if it is not required for your business. |
| RuleName | Strin g | Query | No | bot scanner block _ _ | The name of the rule. |
| AliUid | Long | Query | No | 123456789 | The user ID. |
| CurrentPa ge | Integ er | Query | No | 1 | The page number. |
| PageSize | Integ er | Query | No | 10 | The number of entries per page. |
| ActionTyp e | Strin g | Query | No | pass | The action. A value of pass indicates that access is allowed. A value of alert indicates that access is only logged. A value of drop indicates that access is blocked. |
| Direction | Strin g | Query | No | in | The traffic direction. Valid values: in and out. |
| Query | Strin g | Query | No | 10.x.x.x | The conditions for fuzzy search. |

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| QueryTim eType | Integ er | Query | No | 1 | The type of the query time. A value of 1 indicates to query rules created before the specified point in time. A value of 2 indicates to query rules created at the specified point in time. A value of 3 indicates to query rules created after the specified point in time. A value of 4 indicates to query rules created within the specified time range. A value of 5 indicates to query rules that expire before the specified point in time. A value of 6 indicates to query rules that expire at the specified point in time. A value of 7 indicates to query rules that expire after the specified point in time. A value of 8 indicates to query rules that expire within the specified time range. |
| QueryStar tTime | Long | Query | No | 1706668721 | The beginning of the time range to query. |
| QueryEnd Time | Long | Query | No | 1706668721 | The end of the time range to query. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| DataList | Array |   |   |
| - AddressFileGr oupList | Array |   |   |

| i | Developer Guide·A on | PI documentat |   | Cloud Security Network Detecti n and Respons | o e |
|---|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| -- AddresGroupU uid | String | cfa13285-5330- xxx-xxx- 5075c12c6aa8 | The address book UUID. |
| --FileName | String | test | The name of the file. |
| --FileNameUrl | String | https://xxx.com | The download URL of the file. |
| -RuleId | Integer | 13282 | The rule ID. |
| -RuleUuid | String | cfa13285-5330- 402e-xxx- 5075c12c6aa8 | The rule UUID. |
| -AliUid | Long | 123456789 | The user ID. |
| -RuleName | String | test | The name of the rule. |
| - RuleDescriptio n | String | test | The description of the rule. |
| -Direction | String | in | The traffic direction. Valid values: in and out. |
| -ActionType | String | pass | The action. A value of pass indicates that access is allowed. A value of alert indicates that access is only logged. A value of drop indicates that access is blocked. |
| - SourceAddress CidrList | String | 10.82.x.10/32,10.8 2.x.10/23,10.82.x.1 0/16 | The source IP addresses. |
| - SourceAddress GroupUuidList | String | cfa13285-5330- xxx-xxx- 5075c12c6aa8 | The UUIDs of source address books. |
| - DestAddressCi drList | String | 10.82.x.10/32,10.8 2.x.10/23,10.82.x.1 0/16 | The destination IP addresses. |
| - DestAddressGr oupUuidList | String | cfa13285-5330- xxx-xxx- 5075c12c6aa8 | The UUIDs of destination address books. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| -SwitchStatus | String | online | The status of the rule. A value of init indicates that the rule is in the initialized state and to be enabled. A value of online indicates that the rule is published and takes effect. A value of offline indicates that the rule is unpublished and does not take effect. |
| -StartTime | Long | 1706668721 | The time when the rule takes effect. |
| -EndTime | Long | 1706668721 | The time when the rule expires. |
| -HitTimes | Integer | 1706668721 | The time when the rule was hit. |
| -RuleType | String | 1 | The type of the rule. A value of value 1 indicates that only source IP addresses are specified for the rule, and the addresses books are specified by fileNameList, sourceAddressCidrList, and sourceAddressGroupUuid. A value of 2 indicates that only destination IP addresses are specified for the rule, and the address books are specified by fileNameList, destAddressCidrList, and destAddressGroupUuid. A value of 3 indicates that both source and destination IP addresses or ports are specified for the rule, and the address books are specified by addressCidrList. |
| - AddressCidrLis t | String | 10.82.x.10/32,10.8 2.x.10/23,10.82.x.1 0/16 | The IP addresses. |
| -Modifier | String | admin | The user who last modified the rule. |
| -CreateTime | String | 1706668721 | The time when the rule was created. |
| - AddressFileNa meList | String | filename1,filename 2 | The files. |
| -DeptName | String | yundun | The name of the department. |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| TotalCount | Integer | 100 | The total number of entries returned. |

| i | Developer Guide·A on | PI documentat |   | Cloud Security Network Detecti n and Respons | o e |
|---|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| PageSize | Integer | 10 | The number of entries per page. |
| CurrentPage | Integer | 1 | The page number. |
| Success | Boolean | true | Indicates whether the HTTP request was successful. |
| Module | String | ndr*** | The name of the module. |
| HttpStatusCod e | Integer | 200 | The HTTP status code. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=DescribeL4Rule&RegionId=cnhangzhou&Lang=zh&RuleName=bot_scanner_block&AliUid=123456789&CurrentPage=1&PageSize=10&Ac onType=pass&Direction=in&Query=10.x.x.x&QueryTimeType=1&QueryStartTime=1706668721&QueryEn ime=1706668721
```

Sample success responses `JSON` format

```
Content-Type:application/json
```

`{`

```json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "TotalCount":100,
    "PageSize":10,
    "CurrentPage":1,
    "DataList":[
```

`{`

```json
            "RuleDescription":"test",
            "ActionType":"pass",
            "AddressCidrList":"10.82.x.10/32,10.82.x.10/23,10.82.x.10/16",
            "EndTime":1706668721,
            "RuleId":13282,
            "CreateTime":"1706668721",
            "StartTime":1706668721,
            "DestAddressGroupUuidList":"cfa13285-5330-xxx-xxx-5075c12c6aa8",
            "SourceAddressGroupUuidList":"cfa13285-5330-xxx-xxx-5075c12c6aa8",
            "RuleType":"1",
            "RuleUuid":"cfa13285-5330-402e-xxx-5075c12c6aa8",
            "Direction":"in",
            "SourceAddressCidrList":"10.82.x.10/32,10.82.x.10/23,10.82.x.10/16",
            "HitTimes":1706668721,
            "DestAddressCidrList":"10.82.x.10/32,10.82.x.10/23,10.82.x.10/16",
            "AddressFileGroupList":[
```

`{`

```json
                    "FileNameUrl":"https://xxx.com",
                    "AddresGroupUuid":"cfa13285-5330-xxx-xxx-5075c12c6aa8",
                    "FileName":"test"
```

`}` `],`

```json
            "DeptName":"yundun",
            "Modifier":"admin",
            "AddressFileNameList":"filename1,filename2",
            "RuleName":"test",
            "SwitchStatus":"online",
            "AliUid":123456789
```

`}` `],`

```json
    "Success":true,
    "Module":"ndr***",
    "HttpStatusCode":200
```

`}` `XML` format

```xml
Content-Type:application/xml <DescribeL4RuleResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <TotalCount>100</TotalCount>
    <PageSize>10</PageSize>
    <CurrentPage>1</CurrentPage>
    <DataList>
        <RuleId>13282</RuleId>
        <RuleUuid>cfa13285-5330-402e-xxx-5075c12c6aa8</RuleUuid>
        <AliUid>123456789</AliUid>
        <RuleName>test</RuleName>
        <RuleDescription>test</RuleDescription>
        <Direction>in</Direction>
        <ActionType>pass</ActionType>
<SourceAddressCidrList>10.82.x.10/32,10.82.x.10/23,10.82.x.10/16</SourceAddressCidrList>
        <SourceAddressGroupUuidList>cfa13285-5330-xxx-xxx-
5075c12c6aa8</SourceAddressGroupUuidList> <DestAddressCidrList>10.82.x.10/32,10.82.x.10/23,10.82.x.10/16</DestAddressCidrList>
        <DestAddressGroupUuidList>cfa13285-5330-xxx-xxx-
5075c12c6aa8</DestAddressGroupUuidList>
        <SwitchStatus>online</SwitchStatus>
        <StartTime>1706668721</StartTime>
        <EndTime>1706668721</EndTime>
        <HitTimes>1706668721</HitTimes>
        <RuleType>1</RuleType>
        <AddressCidrList>10.82.x.10/32,10.82.x.10/23,10.82.x.10/16</AddressCidrList>
        <Modifier>admin</Modifier>
        <CreateTime>1706668721</CreateTime>
        <AddressFileGroupList>
            <AddresGroupUuid>cfa13285-5330-xxx-xxx-5075c12c6aa8</AddresGroupUuid>
            <FileName>test</FileName>
            <FileNameUrl>https://xxx.com</FileNameUrl>
        </AddressFileGroupList>
        <AddressFileNameList>filename1,filename2</AddressFileNameList>
        <DeptName>yundun</DeptName>
    </DataList>
    <Success>true</Success>
    <Module>ndr***</Module>
    <HttpStatusCode>200</HttpStatusCode>
</DescribeL4RuleResponse>
```

#### Application layer policies

##### AddL7Rule

Creates an application-layer rule.

**Authorization information**

| Operation | Access level | Resource type |
|---|---|---|
| yundun- cloudfirewall:AddL7Rule | Write | acs:yundun-cloudfirewall:*: {#accountId}:* |

**Throttling**

You can call this operation up to 10 times per second per account. You can call this operation up to 100 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Lang | Strin g | Query | No | zh | The language. Valid values: zh and en. You can leave this parameter empty if it is not required for your business. |
| AliUid | Long | Query | No | 1234567890 | The user ID. |
| RuleName | Strin g | Query | No | test | The name of the rule. |
| RuleDescr iption | Strin g | Query | No | test | The description of the rule. |
| Direction | Strin g | Query | No | in | The traffic direction. Valid values: in and out. |
| ActionTyp e | Strin g | Query | No | alert | The action. A value of pass indicates that access is allowed. A value of alert indicates that access is observed. A value of drop indicates that access is blocked. |

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| SwitchStat us | Strin g | Query | No | online | The status of the rule. A value of online indicates that the rule is enabled. A value of offline indicates that the rule is disabled. |
| StartTime | Long | Query | No | 1943432341 | The time when the rule takes effect. |
| EndTime | Long | Query | No | 1943432341 | The time when the rule expires. |
| Matchs | Strin g | Query | No | W3siaGVhZGVyX25hbW UiOiJIb3N0IiwiY29udGVu dCI6WyIxLjEuMS4xIl0sI m5vY2FzZSI6MCwibWF0 Y2hfdHlwZSI6ImZ1enp5I iwieF9wb3NpdGlvbiI6MH 1d | The content of the rule. The value is similar to the Base64-encoded value of [{'header name':'Host',' _ content': ['1.1.1.1'],'nocase':0,'ma tch type':'fuzzy','x positi _ _ on':0}]. |
| User | Strin g | Query | No | user | The user. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| RuleId | Long | 100 | The rule ID. |
| RuleUuid | String | cfa13285-5330- xxx-xxx- 5075c12c6aa8 | The rule UUID. |
| Success | Boolean | true | Indicates whether the HTTP request was successful. |
| Module | String | ndr*** | The name of the module. |
| HttpStatusCod e | Integer | 200 | The HTTP status code. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=AddL7Rule&RegionId=cnhangzhou&Lang=zh&AliUid=1234567890&RuleName=test&RuleDescription=test&Direction=in&Action pe=alert&SwitchStatus=online&StartTime=1943432341&EndTime=1943432341&Matchs=W3siaGVhZGVyX hbWUiOiJIb3N0IiwiY29udGVudCI6WyIxLjEuMS4xIl0sIm5vY2FzZSI6MCwibWF0Y2hfdHlwZSI6ImZ1enp5Iiwi 9wb3NpdGlvbiI6MH1d&User=user
```

Sample success responses `JSON` format

```
Content-Type:application/json
```

`{`

```json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "RuleId":100,
    "RuleUuid":"cfa13285-5330-xxx-xxx-5075c12c6aa8",
    "Success":true,
    "Module":"ndr***",
    "HttpStatusCode":200
```

`}` `XML` format

```xml
Content-Type:application/xml <AddL7RuleResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <RuleId>100</RuleId>
    <RuleUuid>cfa13285-5330-xxx-xxx-5075c12c6aa8</RuleUuid>
    <Success>true</Success>
    <Module>ndr***</Module>
    <HttpStatusCode>200</HttpStatusCode>
</AddL7RuleResponse>
```

##### ModifyL7Rule

Modifies an application-layer rule.

**Authorization information**

| Operation | Access level | Resource type |
|---|---|---|
| yundun- cloudfirewall:ModifyL7Rule | Write | acs:yundun-cloudfirewall:*: {#accountId}:* |

**Throttling**

You can call this operation up to 10 times per second per account. You can call this operation up to 100 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Lang | Strin g | Query | No | zh | The language. Valid values: zh and en. You can leave this parameter empty if it is not required for your business. |
| AliUid | Long | Query | No | 123456789 | The user ID. |
| RuleUuid | Strin g | Query | No | cfa13285-5330-xxx-xxx- 5075c12c6aa8 | The address book UUID. |
| RuleName | Strin g | Query | No | bot scanner block _ _ | The name of the rule. |
| RuleDescr iption | Strin g | Query | No | test | The description of the rule. |
| Direction | Strin g | Query | No | in | The traffic direction. Valid values: in and out. |
| ActionTyp e | Strin g | Query | No | pass | The action. A value of pass indicates that access is allowed. A value of alert indicates that access is only logged. A value of drop indicates that access is blocked. |

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| SwitchStat us | Strin g | Query | No | online | The status of the rule. A value of init indicates that the rule does not take effect immediately after it is created. The rule takes effect after further modifications or manual activation. A value of online indicates that the rule takes effect immediately after it is published. |
| StartTime | Long | Query | No | 1706668721 | The time when the rule takes effect. |
| EndTime | Long | Query | No | 1706668721 | The time when the rule expires. |
| Matchs | Strin g | Query | No | Matching rule content | The matching rule. |
| User | Strin g | Query | No | admin | The username. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Success | Boolean | true | Indicates whether the HTTP request was successful. |
| Module | String | ndr*** | The name of the module. |
| HttpStatusCod e | Integer | 200 | The HTTP status code. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=ModifyL7Rule&RegionId=cnhangzhou&Lang=zh&AliUid=123456789&RuleUuid=cfa13285-5330-xxx-xxx- 5075c12c6aa8&RuleName=bot_scanner_block&RuleDescription=test&Direction=in&ActionType=pass witchStatus=online&StartTime=1706668721&EndTime=1706668721&Matchs=Matching rule content &User=admin
```

Sample success responses `JSON` format

```
Content-Type:application/json
```

`{`

```json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "Success":true,
    "Module":"ndr***",
    "HttpStatusCode":200
```

`}` `XML` format

```xml
Content-Type:application/xml <ModifyL7RuleResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <Success>true</Success>
    <Module>ndr***</Module>
    <HttpStatusCode>200</HttpStatusCode>
</ModifyL7RuleResponse>
```

##### DescribeL7Rule

Queries the information about an application-layer rule.

**Authorization information**

| Operation | Access level | Resource type |
|---|---|---|
| yundun- cloudfirewall:DescribeL7Rule | Read | acs:yundun-cloudfirewall:*: {#accountId}:* |

**Throttling**

You can call this operation up to 10 times per second per account. You can call this operation up to 100 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Lang | Strin g | Query | No | zh | The language. Valid values: zh and en. You can leave this parameter empty if it is not required for your business. |
| RuleStatu s | Strin g | Query | No | online | The status of the rule. A value of online indicates that the rule is published and takes effect. A value of offline indicates that the rule is unpublished and does not take effect. |
| AliUid | Long | Query | No | 123456789 | The user ID. |
| CurrentPa ge | Integ er | Query | No | 1 | The page number. |
| PageSize | Integ er | Query | No | 10 | The number of entries per page. |
| ActionTyp e | Strin g | Query | No | pass | The action. A value of pass indicates that access is allowed. A value of alert indicates that access is only logged. A value of drop indicates that access is blocked. |
| Direction | Strin g | Query | No | in | The traffic direction. Valid values: in and out. |
| Query | Strin g | Query | No | 10.x.x.x | The query string. |

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| QueryTim eType | Integ er | Query | No | 1 | The type of the query time. A value of 1 indicates to query rules created before the specified point in time. A value of 2 indicates to query rules created at the specified point in time. A value of 3 indicates to query rules created after the specified point in time. A value of 4 indicates to query rules created within the specified time range. A value of 5 indicates to query rules that expire before the specified point in time. A value of 6 indicates to query rules that expire at the specified point in time. A value of 7 indicates to query rules that expire after the specified point in time. A value of 8 indicates to query rules that expire within the specified time range. |
| QueryStar tTime | Long | Query | No | 1706668721 | The beginning of the time range to query. |
| QueryEnd Time | Long | Query | No | 1706668721 | The end of the time range to query. |
| WhiteRule ID | Long | Query | No | 13282 | The whitelist rule ID. |
| BlackRuleI D | Long | Query | No | 13282 | The blacklist rule ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| DataList | Array |   |   |
| -MatchsDesc | Normal | The URL contains a.com and the host address is 1.1.1.1 | The matching item in the rule that is used to monitor HTTP requests. |
| - MatchsDescEn | Normal | url contain a.com,host equal 1.1.1.1 | The matching item in the rule that is used to monitor HTTP requests. This parameter is intended for users outside the Chinese mainland. |
| -matchs | Array |   |   |
| --Content | Normal |   |   |
| --HeaderName | String | x-forward-for | The name of the HTTP header. This value is case-insensitive. |
| --MatchType | String | strict | The rule matching mode. A value of strict indicates that the HTTP header must exactly match that of the rule. A value of fuzzy indicates that the HTTP header must contain that of the rule. A value of notexist indicates that the specified HTTP header must be excluded from the request. |
| --NoCase | Integer | 1 | The case sensitivity. A value of 1 indicates case-insensitive. A value of 0 indicates case-sensitive. |
| --XPosition | Integer | 1 | The position from which the originating IP address is obtained in the HTTP header, such as X-Forwarded-For. The value of this parameter starts from 1. If -1 or an integer that is smaller than 0 is returned, the originating IP address may be in any position of the HTTP header. |
| -- TcpOptionKind | Integer | 28 | The decimal value of the TCP Options field. |
| -RuleId | Integer | 13282 | The rule ID. |

| Developer Guide·A | PI documentat |   | Cloud Security Network Detecti |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| -RuleUuid | String | cfa13285-5330- 402e-xxx- 5075c12c6aa8 | The rule UUID. |
| -AliUid | Long | 123456789 | The user ID. |
| -RuleName | String | test | The name of the rule. |
| - RuleDescriptio n | String | test | The description of the rule. |
| -Direction | String | in | The traffic direction. Valid values: in and out. |
| -ActionType | String | pass | The action. A value of pass indicates that access is allowed. A value of alert indicates that access is only logged. A value of drop indicates that access is blocked. |
| -SwitchStatus | String | online | The status of the rule. A value of init indicates that the rule is in the initialized state and to be enabled. A value of online indicates that the rule is published and takes effect. A value of offline indicates that the rule is unpublished and does not takes effect. |
| -Modifier | String | admin | The user who last modified the rule. |
| -ModifiedTime | String | 2018-05-14 14:50:54 | The time when the rule was updated. |
| -OnlineTime | String | 2018-05-14 14:50:54 | The time when the rule was published. |
| -ExpiredTime | String | 2018-05-14 14:50:54 | The time when the rule is to be unpublished. |
| -OfflineTime | String | 2018-05-14 14:50:54 | The time when the rule was unpublished. |
| -CreateTime | String | 2018-05-14 14:50:54 | The time when the rule was created. |
| -StartTime | Long | 1706668721 | The time when the rule takes effect. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| -EndTime | Long | 1706668721 | The time when the rule expires. |
| -HitTimes | Integer | 1706668721 | The time when the rule was hit. |
| -DeptName | String | yundun | The name of the department. |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| TotalCount | Integer | 100 | The total number of entries returned. |
| PageSize | Integer | 10 | The number of entries per page. |
| CurrentPage | Integer | 1 | The page number. |
| Success | Boolean | true | Indicates whether the HTTP request was successful. |
| Module | String | ndr*** | The name of the module. |
| HttpStatusCod e | Integer | 200 | The HTTP status code. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=DescribeL7Rule&RegionId=cnhangzhou&Lang=zh&RuleStatus=online&AliUid=123456789&CurrentPage=1&PageSize=10&ActionType= ss&Direction=in&Query=10.x.x.x&QueryTimeType=1&QueryStartTime=1706668721&QueryEndTime=170 68721&WhiteRuleID=13282&BlackRuleID=13282
```

Sample success responses `JSON` format

```
Content-Type:application/json
```

`{`

```json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "TotalCount":100,
    "PageSize":10,
    "CurrentPage":1,
    "DataList":[
```

`{`

```json
            "RuleDescription":"test",
            "MatchsDescEn":"url contain a.com,host equal 1.1.1.1",
            "ActionType":"pass",
            "OfflineTime":"2018-05-14 14:50:54",
            "matchs":[
```

`{`

```json
                    "XPosition":1,
                    "MatchType":"strict",
                    "HeaderName":"x-forward-for",
                    "TcpOptionKind":28,
                    "NoCase":1
```

`}` `],`

```json
            "EndTime":1706668721,
            "RuleId":13282,
            "CreateTime":"2018-05-14 14:50:54",
            "StartTime":1706668721,
            "OnlineTime":"2018-05-14 14:50:54",
            "RuleUuid":"cfa13285-5330-402e-xxx-5075c12c6aa8",
            "Direction":"in",
            "ModifiedTime":"2018-05-14 14:50:54",
            "HitTimes":1706668721,
            "ExpiredTime":"2018-05-14 14:50:54",
            "DeptName":"yundun",
            "MatchsDesc":"The URL contains a.com and the host address is 1.1.1.1",
            "Modifier":"admin",
            "RuleName":"test",
            "SwitchStatus":"online",
            "AliUid":123456789
```

`}` `],`

```json
    "Success":true,
    "Module":"ndr***",
    "HttpStatusCode":200
```

`}` `XML` format

```xml
Content-Type:application/xml <DescribeL7RuleResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <TotalCount>100</TotalCount>
    <PageSize>10</PageSize>
    <CurrentPage>1</CurrentPage>
    <DataList>
        <RuleId>13282</RuleId>
        <RuleUuid>cfa13285-5330-402e-xxx-5075c12c6aa8</RuleUuid>
        <AliUid>123456789</AliUid>
        <RuleName>test</RuleName>
        <RuleDescription>test</RuleDescription>
        <Direction>in</Direction>
        <ActionType>pass</ActionType>
        <SwitchStatus>online</SwitchStatus>
        <Modifier>admin</Modifier>
        <ModifiedTime>2018-05-14 14:50:54</ModifiedTime>
        <OnlineTime>2018-05-14 14:50:54</OnlineTime>
        <ExpiredTime>2018-05-14 14:50:54</ExpiredTime>
        <OfflineTime>2018-05-14 14:50:54</OfflineTime>
        <CreateTime>2018-05-14 14:50:54</CreateTime>
        <StartTime>1706668721</StartTime>
        <EndTime>1706668721</EndTime>
        <HitTimes>1706668721</HitTimes>
        <matchs>
            <HeaderName>x-forward-for</HeaderName>
            <Content>
                <String></String>
            </Content>
            <MatchType>strict</MatchType>
            <NoCase>1</NoCase>
            <XPosition>1</XPosition>
            <TcpOptionKind>28</TcpOptionKind>
        </matchs>
        <MatchsDesc>
            <String>The URL contains a.com and the host address is 1.1.1.1</String>
        </MatchsDesc>
        <MatchsDescEn>
            <String>url contain a.com,host equal 1.1.1.1</String>
        </MatchsDescEn>
        <DeptName>yundun</DeptName>
    </DataList>
    <Success>true</Success>
    <Module>ndr***</Module>
    <HttpStatusCode>200</HttpStatusCode>
</DescribeL7RuleResponse>
```

##### DelL7Rule

Deletes one or more application-layer rules.

**Authorization information**

| Operation | Access level | Resource type |
|---|---|---|
| yundun-cloudfirewall:DelL7Rule | Write | acs:yundun-cloudfirewall:*: {#accountId}:* |

**Throttling**

You can call this operation up to 10 times per second per account. You can call this operation up to 100 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Lang | Strin g | Query | No | zh | The language. Valid values: zh and en. You can leave this parameter empty if it is not required for your business. |
| AliUid | Long | Query | No | 1234567890 | The user ID. |
| RuleUuidL ist | Strin g | Query | No | 13285-5330-402e-980c- 5075c12c6xx8,13285- 5330-402e-980c- 5075c12c6yy8 | The UUIDs of the rules that you want to delete. You can delete multiple rules at a time. |
| User | Strin g | Query | No | user | The user. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Success | Boolean | true | Indicates whether the HTTP request was successful. |
| Module | String | ndr*** | The name of the module. |

| n | Cloud Security Ne and Response | twork Detectio |   | Developer Guide·API documenta io | t n |
|---|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| HttpStatusCod e | Integer | 200 | The HTTP status code. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=DelL7Rule&RegionId=cnhangzhou&Lang=zh&AliUid=1234567890&RuleUuidList=13285-5330-402e-980c- 5075c12c6xx8,13285-5330-402e-980c-5075c12c6yy8&User=user
```

Sample success responses `JSON` format

```
Content-Type:application/json
```

`{`

```json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "Success":true,
    "Module":"ndr***",
    "HttpStatusCode":200
```

`}` `XML` format

```xml
Content-Type:application/xml <DelL7RuleResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <Success>true</Success>
    <Module>ndr***</Module>
    <HttpStatusCode>200</HttpStatusCode>
</DelL7RuleResponse>
```

##### SwitchL7RuleStatus

Modifies the status of one ore more application-layer rules.

**Authorization information**

| Operation | Access level | Resource type |
|---|---|---|
| yundun- cloudfirewall:SwitchL7RuleStatu s | Write | acs:yundun-cloudfirewall:*: {#accountId}:* |

**Throttling**

You can call this operation up to 10 times per second per account. You can call this operation up to 100 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Lang | Strin g | Query | No | zh | The language. Valid values: zh and en. You can leave this parameter empty if it is not required for your business. |
| AliUid | Long | Query | No | 123456789 | The user ID. |
| RuleUuidL ist | Strin g | Query | No | cfa13285-5330-xxx-xxx- 5075c12c6aa8,cfa13285 -5330-xxx-xxx- 5075c12c6aa8 | The rule UUIDs. Separate multiple UUIDs with commas (,). |
| SwitchStat us | Strin g | Query | No | online | The status of the rule. A value of online indicates that the rule is published and takes effect. A value of offline indicates that the rule is unpublished and does not take effect. |
| User | Strin g | Query | No | admin | The username. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Success | Boolean | true | Indicates whether the HTTP request was successful. |
| Module | String | ndr*** | The name of the module. |
| HttpStatusCod e | Integer | 200 | The HTTP status code. |

| Cloud Security Ne and Response | twork Detectio |   | Developer Guide·API documenta io |
|---|---|---|---|
| Parameter | Type | Example | Description |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=SwitchL7RuleStatus&RegionId=cnhangzhou&Lang=zh&AliUid=123456789&RuleUuidList=cfa13285-5330-xxx-xxx- 5075c12c6aa8,cfa13285-5330-xxx-xxx-5075c12c6aa8&SwitchStatus=online&User=admin
```

Sample success responses `JSON` format

```
Content-Type:application/json
```

`{`

```json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "Success":true,
    "Module":"ndr***",
    "HttpStatusCode":200
```

`}` `XML` format

```xml
Content-Type:application/xml <SwitchL7RuleStatusResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <Success>true</Success>
    <Module>ndr***</Module>
    <HttpStatusCode>200</HttpStatusCode>
</SwitchL7RuleStatusResponse>
```

##### ExportL7Rules

Exports application-layer rules.

**Authorization information**

| Operation | Access level | Resource type |
|---|---|---|
| yundun- cloudfirewall:ExportL7Rules | Write | acs:yundun-cloudfirewall:*: {#accountId}:* |

**Throttling**

You can call this operation up to 10 times per second per account. You can call this operation up to 100 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Lang | Strin g | Query | No | zh | The language. Valid values: zh and en. You can leave this parameter empty if it is not required for your business. |
| AliUid | Long | Query | No | 123456789 | The user ID. |
| ExportTyp e | Strin g | Query | No | batch | The export type. A value of batch indicates that rules are exported in batches. A value of total indicates that all rules are exported. If you set ExportType to batch, you must specify RuleUuidList. |
| RuleUuidL ist | Strin g | Query | No | cfa13285-5330-402e- xxx- 5075c12c6aa8,cfa13285 -5330-402e-xxx- 5075c12c6aa8 | The rule UUIDs. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| ExportFileNam e | String | test.csv | The name of the file to which rules are exported. |
| ExportFileUrl | String | https://xxx.com | The download URL of the file. |
| TaskUUID | String | cfa13285-5330- 402e-xxx- 5075c12c6aa8 | The export task ID. |

| Cloud Security Ne and Response | twork Detectio |   | Developer Guide·API documenta io |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| Success | Boolean | true | Indicates whether the HTTP request was successful. |
| Module | String | ndr*** | The name of the module. |
| HttpStatusCod e | Integer | 200 | The HTTP status code. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=ExportL7Rules&RegionId=cnhangzhou&Lang=zh&AliUid=123456789&ExportType=batch&RuleUuidList=cfa13285-5330-402e-xxx- 5075c12c6aa8,cfa13285-5330-402e-xxx-5075c12c6aa8
```

Sample success responses `JSON` format

```
Content-Type:application/json
```

`{`

```json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "ExportFileName":"test.csv",
    "ExportFileUrl":"https://xxx.com",
    "TaskUUID":"cfa13285-5330-402e-xxx-5075c12c6aa8",
    "Success":true,
    "Module":"ndr***",
    "HttpStatusCode":200
```

`}` `XML` format

```xml
Content-Type:application/xml <ExportL7RulesResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <ExportFileName>test.csv</ExportFileName>
    <ExportFileUrl>https://xxx.com</ExportFileUrl>
    <TaskUUID>cfa13285-5330-402e-xxx-5075c12c6aa8</TaskUUID>
    <Success>true</Success>
    <Module>ndr***</Module>
    <HttpStatusCode>200</HttpStatusCode>
</ExportL7RulesResponse>
```

##### GetWafRules

Queries the information about Web Application Firewall (WAF) rules.

**Authorization information**

| Operation | Access level | Resource type |
|---|---|---|
| yundun- cloudfirewall:GetWafRules | Read | acs:yundun-cloudfirewall:*: {#accountId}:* |

**Throttling**

You can call this operation up to 10 times per second per account. You can call this operation up to 100 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Lang | Strin g | Query | No | zh | The language. Valid values: zh and en. You can leave this parameter empty if it is not required for your business. |
| PageSize | Integ er | Query | No | 10 | The number of entries per page. |
| CurrentPa ge | Integ er | Query | No | 1 | The page number. |
| RuleStatu s | Strin g | Query | No | online | The status of the rule. A value of online indicates that the rule is published. A value of offline indicates that the rule is unpublished. |
| RuleId | Strin g | Query | No | 100 | The rule ID. |
| IpBlockSta tus | Strin g | Query | No | disable | Specifies whether the rule is enabled. Valid values: enable and disable. |

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| ActionTyp e | Strin g | Query | No | pass | The action. A value of pass indicates that access is allowed. A value of alert indicates that access is only logged. A value of drop indicates that access is blocked. |
| RuleName | Strin g | Query | No | test | The name of the rule. |
| ProtectTy pe | Strin g | Query | No | Protection type | The protection type. |
| CveID | Strin g | Query | No | cve | The Common Vulnerabilities and Exposures (CVE) ID. |
| RuleActio nType | Strin g | Query | No | enableDrop | The blocking type of the rule. A value of enableDrop indicates that blocking is enabled. A value of disableDrop indicates that blocking is disabled. |
| AppType | Strin g | Query | No | Application type | The type of the application. |
| VulLevel | Strin g | Query | No | mid | The threat level. A value of low indicates low risk. A value of mid indicates medium risk. A value of high indicates high risk. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| DataList | Array |   |   |
| -ID | Integer | 10 | The sequence number of the rule. |
| -RuleId | String | 100 | The rule ID. |

| Developer Guide·A | PI documentat |   | Cloud Security Network Detecti |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| -Action | String | pass | The action. A value of pass indicates that access is allowed. A value of alert indicates that access is only logged. A value of drop indicates that access is blocked. |
| -RuleStatus | String | online | The status of the rule. A value of online indicates that the rule is published. A value of offline indicates that the rule is unpublished. |
| -RuleName | String | test | The name of the rule. |
| -RuleDesc | String | test | The description of the rule. |
| -AppType | String | Application type | The type of the application. |
| - RuleActionTyp e | String | pass | The action. A value of pass indicates that access is allowed. A value of alert indicates that access is only logged. A value of drop indicates that access is blocked. |
| -ProtectType | String | Protection type | The protection type. |
| -VulLevel | String | mid | The threat level. A value of low indicates low risk. A value of mid indicates medium risk. A value of high indicates high risk. |
| -CVE | String | cve | The CVE ID. |
| -IPBlockStatus | String | disable | Indicates whether the rule is enabled. Valid values: enable and disable. |
| -HitIntervalSec | Integer | 10 | The interval between two hits. |
| -HitCount | Integer | 100 | The number of hits. |
| - TimeoutTempl atName | String | test | The name of the timeout template. |
| -UpdateTime | String | 2020-12-31 16:30:36 | The time when the rule was updated. |

| Cloud Security Ne | twork Detectio |   | Developer Guide·API documenta |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| TotalCount | Integer | 100 | The total number of entries returned. |
| CurrentPage | Integer | 1 | The page number. |
| PageSize | Integer | 10 | The number of entries per page. |
| Success | Boolean | true | Indicates whether the HTTP request was successful. |
| Module | String | ndr*** | The name of the module. |
| HttpStatusCod e | Integer | 200 | The HTTP status code. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=GetWafRules&RegionId=cnhangzhou&Lang=zh&PageSize=10&CurrentPage=1&RuleStatus=online&RuleId=100&IpBlockStatus=dis le&ActionType=pass&RuleName=test&ProtectType=Protection type&CveID=cve&RuleActionType=enableDrop&AppType=Application type&VulLevel=mid
```

Sample success responses `JSON` format

```
Content-Type:application/json
```

`{`

```json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "TotalCount":100,
    "CurrentPage":1,
    "PageSize":10,
    "DataList":[
```

`{`

```json
            "RuleActionType":"pass",
            "Action":"pass",
            "HitCount":100,
            "RuleId":"100",
            "TimeoutTemplatName":"test",
            "CVE":"cve",
            "IPBlockStatus":"disable",
            "UpdateTime":"2020-12-31 16:30:36",
            "RuleDesc":"test",
            "ProtectType":"Protection type",
            "RuleStatus":"online",
            "ID":10,
            "AppType":"Application type",
            "RuleName":"test",
            "HitIntervalSec":10,
            "VulLevel":"mid"
```

`}` `],`

```json
    "Success":true,
    "Module":"ndr***",
    "HttpStatusCode":200
```

`}` `XML` format

```xml
Content-Type:application/xml <GetWafRulesResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <TotalCount>100</TotalCount>
    <CurrentPage>1</CurrentPage>
    <PageSize>10</PageSize>
    <DataList>
        <ID>10</ID>
        <RuleId>100</RuleId>
        <Action>pass</Action>
        <RuleStatus>online</RuleStatus>
        <RuleName>test</RuleName>
        <RuleDesc>test</RuleDesc>
        <AppType>Application type</AppType>
        <RuleActionType>pass</RuleActionType>
        <ProtectType>Protection type</ProtectType>
        <VulLevel>mid</VulLevel>
        <CVE>cve</CVE>
        <IPBlockStatus>disable</IPBlockStatus>
        <HitIntervalSec>10</HitIntervalSec>
        <HitCount>100</HitCount>
        <TimeoutTemplatName>test</TimeoutTemplatName>
        <UpdateTime>2020-12-31 16:30:36</UpdateTime>
    </DataList>
    <Success>true</Success>
    <Module>ndr***</Module>
    <HttpStatusCode>200</HttpStatusCode>
</GetWafRulesResponse>
```

##### DescribeAllHttpFields

Queries the matching fields of application-layer rules.

**Authorization information**

| Operation | Access level | Resource type |
|---|---|---|
| yundun- cloudfirewall:DescribeAllHttpFie lds | Read | acs:yundun-cloudfirewall:*: {#accountId}:* |

**Throttling**

You can call this operation up to 10 times per second per account. You can call this operation up to 100 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Lang | Strin g | Query | No | zh | The language. Valid values: zh and en. You can leave this parameter empty if it is not required for your business. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| HttpFileds | Normal | ['Method', 'URL', 'Host', 'X- Forwarded-For', 'Cookie', 'User- Agent'] | The fields. |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Success | Boolean | true | Indicates whether the HTTP request was successful. |
| Module | String | ndr*** | The name of the module. |
| HttpStatusCod e | Integer | 200 | The HTTP status code. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=DescribeAllHttpFields&RegionId=cn-hangzhou&Lang=zh
```

Sample success responses `JSON` format

```
Content-Type:application/json
```

`{`

```json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "HttpFileds":[
        "Method",
        "URL",
        "Host",
        "X-Forwarded-For",
        "Cookie",
        "User-Agent"
```

`],`

```json
    "Success":true,
    "Module":"ndr***",
    "HttpStatusCode":200
```

`}` `XML` format

```xml
Content-Type:application/xml <DescribeAllHttpFieldsResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <HttpFileds>
        <string>['Method', 'URL', 'Host', 'X-Forwarded-For', 'Cookie', 'User-Agent']</s
tring>
    </HttpFileds>
    <Success>true</Success>
    <Module>ndr***</Module>
    <HttpStatusCode>200</HttpStatusCode>
</DescribeAllHttpFieldsResponse>
```

##### UpdateWafRuleAction

Modifies the action for Web Application Firewall (WAF) rules.

**Authorization information**

| Operation | Access level | Resource type |
|---|---|---|
| yundun- cloudfirewall:UpdateWafRuleAct ion | Write | acs:yundun-cloudfirewall:*: {#accountId}:* |

**Throttling**

You can call this operation up to 10 times per second per account. You can call this operation up to 100 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Lang | Strin g | Query | No | zh | The language. Valid values: zh and en. You can leave this parameter empty if it is not required for your business. |
| RuleId | Strin g | Query | No | 100 | The rule ID. |
| ActionTyp e | Strin g | Query | No | pass | The action. A value of pass indicates that access is allowed. A value of alert indicates that access is only logged. A value of drop indicates that access is blocked. |
| RuleStatu s | Strin g | Query | No | online | The status of the rule. A value of online indicates that the rule is published and takes effect. A value of offline indicates that the rule is unpublished and does not take effect. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Success | Boolean | true | Indicates whether the HTTP request was successful. |
| Module | String | ndr*** | The name of the module. |

| Cloud Security Ne | twork Detectio |   | Developer Guide·API documenta |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| HttpStatusCod e | Integer | 200 | The HTTP status code. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=UpdateWafRuleAction&RegionId=cnhangzhou&Lang=zh&RuleId=100&ActionType=pass&RuleStatus=online
```

Sample success responses `JSON` format

```
Content-Type:application/json
```

`{`

```json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "Success":true,
    "Module":"ndr***",
    "HttpStatusCode":200
```

`}` `XML` format

```xml
Content-Type:application/xml <UpdateWafRuleActionResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <Success>true</Success>
    <Module>ndr***</Module>
    <HttpStatusCode>200</HttpStatusCode>
</UpdateWafRuleActionResponse>
```

#### Port scan spoofing policy

##### DescribePortScanProtectRules

Queries a protection rule for port scanning.

**Authorization information**

| Operation | Access level | Resource type |
|---|---|---|
| yundun- cloudfirewall:DescribePortScan ProtectRules | Read | acs:yundun-cloudfirewall:*: {#accountId}:* |

**Throttling**

You can call this operation up to 10 times per second per account. You can call this operation up to 100 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Lang | Strin g | Query | No | zh | The language. Valid values: zh and en. You can leave this parameter empty if it is not required for your business. |
| AliUid | Long | Query | No | 123456789 | The user ID. |
| DeptAliUid | Long | Query | No | 1234567890 | The department ID. |
| AddressTy pe | Integ er | Query | No | 1 | The type of the address to which the rule applies. A value of 1 indicates Web Application Firewall (WAF). A value of 2 indicates Server Load Balancer (SLB). A value of 3 indicates Elastic IP Address (EIP). A value of 4 indicates custom. By default, all types of addresses are queried if this parameter is not specified. |
| AssetType | Strin g | Query | No | WAF | The type of the asset. |
| Address | Strin g | Query | No | 10.x.x.x | The IP address. |
| Query | Strin g | Query | No | 80 | The keyword used for fuzzy search. You can enter an IP address, a port number, or the rule ID. |

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| PageSize | Integ er | Query | No | 10 | The number of entries per page. |
| PageNo | Integ er | Query | No | 1 | The page number. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| DataList | Array |   |   |
| -RuleID | Integer | 1 | The rule ID. |
| -AliUid | Long | 123456789 | The user ID. |
| -Dept | String | yundun | The name of the department. |
| -AddressType | String | 1 | The type of the address to which the rule applies. A value of 1 indicates WAF. A value of 2 indicates SLB. A value of 3 indicates EIP. A value of 4 indicates custom. By default, all types of addresses are queried if this parameter is not specified. |
| -Address | String | 10.x.x.x | The IP address. |
| -ProtectPorts | String | 8080 | The protected port number. |
| -ProtectMode | Integer | 0 | The protection mode. A value of 0 indicates that the system only generates alerts but does not block attacks. A value of 1 indicates that the system blocks attacks. |
| -EnableStatus | Integer | 1 | Indicates whether the rule is enabled. A value of 0 indicates that the rule is disabled. A value of 1 indicates that the rule is enabled. |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |

| Developer Guide·A on | PI documentat |   | Cloud Security Network Detecti n and Respons |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| TotalCount | Integer | 100 | The total number of entries returned. |
| PageSize | Integer | 10 | The number of entries per page. |
| CurrentPage | Integer | 1 | The page number. |
| Success | Boolean | true | Indicates whether the HTTP request was successful. |
| Module | String | ndr*** | The name of the module. |
| HttpStatusCod e | Integer | 200 | The HTTP status code. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=DescribePortScanProtectRules&RegionId=cnhangzhou&Lang=zh&AliUid=123456789&DeptAliUid=1234567890&AddressType=1&AssetType=WAF&Addre =10.x.x.x&Query=80&PageSize=10&PageNo=1
```

Sample success responses `JSON` format

```
Content-Type:application/json
```

`{`

```json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "TotalCount":100,
    "PageSize":10,
    "CurrentPage":1,
    "DataList":[
```

`{`

```json
            "ProtectPorts":"8080",
            "Address":"10.x.x.x",
            "Dept":"yundun",
            "EnableStatus":1,
            "RuleID":1,
            "AddressType":"1",
            "AliUid":123456789,
            "ProtectMode":0
```

`}` `],`

```json
    "Success":true,
    "Module":"ndr***",
    "HttpStatusCode":200
```

`}` `XML` format

```xml
Content-Type:application/xml <DescribePortScanProtectRulesResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <TotalCount>100</TotalCount>
    <PageSize>10</PageSize>
    <CurrentPage>1</CurrentPage>
    <DataList>
        <RuleID>1</RuleID>
        <AliUid>123456789</AliUid>
        <Dept>yundun</Dept>
        <AddressType>1</AddressType>
        <Address>10.x.x.x</Address>
        <ProtectPorts>8080</ProtectPorts>
        <ProtectMode>0</ProtectMode>
        <EnableStatus>1</EnableStatus>
    </DataList>
    <Success>true</Success>
    <Module>ndr***</Module>
    <HttpStatusCode>200</HttpStatusCode>
</DescribePortScanProtectRulesResponse>
```

##### UpdatePortScanProtectRule

Modifies a protection rule for port scanning.

**Authorization information**

| Operation | Access level | Resource type |
|---|---|---|
| yundun- cloudfirewall:UpdatePortScanPr otectRule | Write | acs:yundun-cloudfirewall:*: {#accountId}:* |

**Throttling**

You can call this operation up to 10 times per second per account. You can call this operation up to 100 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Lang | Strin g | Query | No | zh | The language. Valid values: zh and en. You can leave this parameter empty if it is not required for your business. |
| AliUid | Long | Query | No | 123456789 | The user ID. |
| DeptAliUid | Long | Query | No | 1234567890 | The department ID. |
| AddressTy pe | Integ er | Query | No | 1 | The type of the address to which the rule applies. A value of 1 indicates Web Application Firewall (WAF). A value of 2 indicates Server Load Balancer (SLB). A value of 3 indicates Elastic IP Address (EIP). A value of 4 indicates custom. If you use a global role, you can set AddressType to 1, 2, 3, or 4. If you use a tenant role, you can set AddressType to 2 or 3. |
| AssetType | Strin g | Query | No | slb | The type of the asset. |

| Cloud Security and Respon | Network se | Detectio |   | Devel | oper Guide·API documenta io |
|---|---|---|---|---|---|

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Address | Strin g | Query | No | 10.x.x.x | The protected IP address. You can select an IP address from the drop-down list based on DeptAliUid and AddressType. If AddressType is set to 4, you can enter an IP address. |
| ProtectPor ts | Strin g | Query | No | 1-65535 | The whitelist of protected ports. Separate multiple ports with commas (,). Valid values: 1 to 65535. The port number cannot be greater than 65535 or smaller than 0 for frontend and backend verification. |
| ProtectMo de | Integ er | Query | No | 0 | The protection mode. A value of 0 indicates that the system only generates alerts but does not block attacks. A value of 1 indicates that the system blocks attacks. |
| RuleID | Integ er | Query | No | 100 | The rule ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Success | Boolean | true | Indicates whether the HTTP request was successful. |
| Module | String | ndr*** | The name of the module. |
| HttpStatusCod e | Integer | 200 | The HTTP status code. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=UpdatePortScanProtectRule&RegionId=cnhangzhou&Lang=zh&AliUid=123456789&DeptAliUid=1234567890&AddressType=1&AssetType=slb&Addre =10.x.x.x&ProtectPorts=1-65535&ProtectMode=0&RuleID=100
```

Sample success responses `JSON` format

```
Content-Type:application/json
```

`{`

```json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "Success":true,
    "Module":"ndr***",
    "HttpStatusCode":200
```

`}` `XML` format

```xml
Content-Type:application/xml <UpdatePortScanProtectRuleResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <Success>true</Success>
    <Module>ndr***</Module>
    <HttpStatusCode>200</HttpStatusCode>
</UpdatePortScanProtectRuleResponse>
```

##### DeletePortScanProtectRule

Removes protection rules from the whitelist for port scanning.

**Authorization information**

| Operation | Access level | Resource type |
|---|---|---|
| yundun- cloudfirewall:DeletePortScanPro tectRule | Write | acs:yundun-cloudfirewall:*: {#accountId}:* |

**Throttling**

You can call this operation up to 10 times per second per account. You can call this operation up to 100 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Lang | Strin g | Query | No | zh | The language. Valid values: zh and en. You can leave this parameter empty if it is not required for your business. |
| RuleIdList | Strin g | Query | No | 1024,1025 | The IDs of the rules that you want to remove. You can remove multiple rules at a time. |
| User | Strin g | Query | No | user | The user. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Success | Boolean | true | Indicates whether the HTTP request was successful. |
| Module | String | ndr*** | The name of the module. |
| HttpStatusCod e | Integer | 200 | The HTTP status code. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=DeletePortScanProtectRule&RegionId=cnhangzhou&Lang=zh&RuleIdList=1024,1025&User=user
```

Sample success responses `JSON` format

```
Content-Type:application/json
```

`{`

```json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "Success":true,
    "Module":"ndr***",
    "HttpStatusCode":200
```

`}` `XML` format

```xml
Content-Type:application/xml <DeletePortScanProtectRuleResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <Success>true</Success>
    <Module>ndr***</Module>
    <HttpStatusCode>200</HttpStatusCode>
</DeletePortScanProtectRuleResponse>
```

##### SwitchPortProtectRuleStatus

Modifies the status of a protection rule for port scanning.

**Authorization information**

| Operation | Access level | Resource type |
|---|---|---|
| yundun- cloudfirewall:SwitchPortProtect RuleStatus | Write | acs:yundun-cloudfirewall:*: {#accountId}:* |

**Throttling**

You can call this operation up to 10 times per second per account. You can call this operation up to 100 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Lang | Strin g | Query | No | zh | The language. Valid values: zh and en. You can leave this parameter empty if it is not required for your business. |
| RuleIdList | Strin g | Query | No | 1001,1002,1003 | The one or more IDs of the rules whose status you want to modify. |
| EnableSta tus | Integ er | Query | No | 0 | The status of the rule. A value of 0 indicates that the rule is disabled. A value of 1 indicates that the rule is enabled. |
| User | Strin g | Query | No | admin | The username. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Success | Boolean | true | Indicates whether the HTTP request was successful. |
| Module | String | ndr*** | The name of the module. |
| HttpStatusCod e | Integer | 200 | The HTTP status code. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=SwitchPortProtectRuleStatus&RegionId=cnhangzhou&Lang=zh&RuleIdList=1001,1002,1003&EnableStatus=0&User=admin
```

Sample success responses `JSON` format

```
Content-Type:application/json
```

`{`

```json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "Success":true,
    "Module":"ndr***",
    "HttpStatusCode":200
```

`}` `XML` format

```xml
Content-Type:application/xml <SwitchPortProtectRuleStatusResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <Success>true</Success>
    <Module>ndr***</Module>
    <HttpStatusCode>200</HttpStatusCode>
</SwitchPortProtectRuleStatusResponse>
```

##### DescribeAssetsAddressAndPorts

Queries the IP address and listener port of an asset.

**Authorization information**

| Operation | Access level | Resource type |
|---|---|---|
| yundun- cloudfirewall:DescribeAssetsAd dressAndPorts | Read | acs:yundun-cloudfirewall:*: {#accountId}:* |

**Throttling**

You can call this operation up to 10 times per second per account. You can call this operation up to 100 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Lang | Strin g | Query | No | zh | The language. Valid values: zh and en. You can leave this parameter empty if it is not required for your business. |
| AliUid | Long | Query | No | 1234567890 | The user ID. |
| DeptAliUid | Long | Query | No | 1234567890 | The department ID. |
| AddressTy pe | Integ er | Query | No | EIP | The address type. This parameter is discontinued. |
| AssetType | Strin g | Query | No | EIP | The type of the asset. Valid values include EIP, SLB, and WAF. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| DataList | Array |   |   |
| -Address | String | 1.1.1.1 | The IP address of the asset. |
| -Ports | String | 80,8080 | The listener port of the asset. |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| TotalCount | Integer | 100 | The total number of entries returned. |
| Success | Boolean | true | Indicates whether the HTTP request was successful. |
| Module | String | ndr*** | The name of the module. |
| HttpStatusCod e | Integer | 200 | The HTTP status code. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=DescribeAssetsAddressAndPorts&RegionId=cnhangzhou&Lang=zh&AliUid=1234567890&DeptAliUid=1234567890&AddressType=EIP&AssetType=EIP
```

Sample success responses `JSON` format

```
Content-Type:application/json
```

`{`

```json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "TotalCount":100,
    "DataList":[
```

`{`

```json
            "Address":"1.1.1.1",
            "Ports":"80,8080"
```

`}` `],`

```json
    "Success":true,
    "Module":"ndr***",
    "HttpStatusCode":200
```

`}` `XML` format

```xml
Content-Type:application/xml <DescribeAssetsAddressAndPortsResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <TotalCount>100</TotalCount>
    <DataList>
        <Address>1.1.1.1</Address>
        <Ports>80,8080</Ports>
    </DataList>
    <Success>true</Success>
    <Module>ndr***</Module>
    <HttpStatusCode>200</HttpStatusCode>
</DescribeAssetsAddressAndPortsResponse>
```

##### AddPortScanProtectRule

Creates a protection rule for port proofing.

**Authorization information**

| Operation | Access level | Resource type |
|---|---|---|
| yundun- cloudfirewall:AddPortScanProte ctRule | Write | acs:yundun-cloudfirewall:*: {#accountId}:* |

**Throttling**

You can call this operation up to 10 times per second per account. You can call this operation up to 100 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Lang | Strin g | Query | No | zh | The language. Valid values: zh and en. You can leave this parameter empty if it is not required for your business. |
| User | Strin g | Query | No | user | The user. |
| AliUid | Long | Query | No | 1234567890 | The user ID. |
| DeptAliUid | Long | Query | No | 1234567890 | The department ID. This parameter is used if you are a global organization security administrator. |
| AddressTy pe | Integ er | Query | No | 3 | The address type. This parameter is used in Apsara Stack versions earlier than V3.18. A value of 1 indicates Web Application Firewall (WAF). A value of 2 indicates Server Load Balancer (SLB). A value of 3 indicates Elastic IP Address (EIP). A value of 4 indicates custom. |
| AssetType | Strin g | Query | No | EIP | The type of the asset. |

| Developer Gui on | de·API d | ocumentat |   | Cloud | Security Network Detecti n and Respons |
|---|---|---|---|---|---|

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Address | Strin g | Query | No | 1.1.1.1 | The asset address. |
| ProtectPor ts | Strin g | Query | No | 80,90 | The port whitelist. You can specify multiple ports and separate them with commas (,). You can also specify a port range, such as 80-90. |
| ProtectMo de | Integ er | Query | No | 0 | The protection mode. A value of 0 indicates observing. A value of 1 indicates protection. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Success | Boolean | true | Indicates whether the HTTP request was successful. |
| Module | String | ndr*** | The name of the module. |
| HttpStatusCod e | Integer | 200 | The HTTP status code. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=AddPortScanProtectRule&RegionId=cnhangzhou&Lang=zh&User=user&AliUid=1234567890&DeptAliUid=1234567890&AddressType=3&AssetTyp EIP&Address=1.1.1.1&ProtectPorts=80,90&ProtectMode=0
```

Sample success responses `JSON` format

```
Content-Type:application/json
```

`{`

```json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "Success":true,
    "Module":"ndr***",
    "HttpStatusCode":200
```

`}` `XML` format

```xml
Content-Type:application/xml <AddPortScanProtectRuleResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <Success>true</Success>
    <Module>ndr***</Module>
    <HttpStatusCode>200</HttpStatusCode>
</AddPortScanProtectRuleResponse>
```

##### DescribeAssetsAddressTypes

You can call the DescribeAssetsAddressTypes operation to query the types of assets.

**Authorization information**

| Operation | Access level | Resource type |
|---|---|---|
| yundun- cloudfirewall:DescribeAssetsAd dressTypes | Read | acs:yundun-cloudfirewall:*: {#accountId}:* |

**Throttling**

Call frequency for a single user: 10 queries per second (QPS). API call frequency: 100 QPS.

**Request headers**

This operation uses common request headers. No special request headers are required. For more information, see Common request parameters.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Lang | Strin g | Query | No | zh | The language of the response. Valid values: zh for Chinese and en for English. This parameter is optional. |
| AliUid | Long | Query | No | 1234567890 | The UID of the user. |
| DeptAliUid | Long | Query | No | 1234567890 | The UID of the department. |

**Response data**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Types | Normal | ['EIP','WAF', 'Public SLB'] | A list of asset types. |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The ID of the request. This unique identifier is generated by Alibaba Cloud and can be used to troubleshoot issues. |
| Success | Boolean | true | Indicates whether the HTTP request was successful. |
| Module | String | ndr*** | The name of the module. |
| HttpStatusCod e | Integer | 200 | The HTTP status code of the response. |

**Examples**

Request example

```
https://[Endpoint]/?Action=DescribeAssetsAddressTypes&RegionId=cnhangzhou&Lang=zh&AliUid=1234567890&DeptAliUid=1234567890
```

Successful response example `JSON` format

```
Content-Type:application/json
```

`{`

```json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "Types":[
        "EIP",
        "WAF",
        "Public SLB"
```

`],`

```json
    "Success":true,
    "Module":"ndr***",
    "HttpStatusCode":200
```

`}` `XML` format

```xml
Content-Type:application/xml <DescribeAssetsAddressTypesResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <Types>
        <Types>['EIP','WAF', 'Public SLB']</Types>
    </Types>
    <Success>true</Success>
    <Module>ndr***</Module>
    <HttpStatusCode>200</HttpStatusCode>
</DescribeAssetsAddressTypesResponse>
```

#### Manage address books

##### ModifyAddressGroup

Modifies an address book.

**Authorization information**

| Operation | Access level | Resource type |
|---|---|---|
| yundun- cloudfirewall:ModifyAddressGro up | Write | acs:yundun-cloudfirewall:*: {#accountId}:* |

**Throttling**

You can call this operation up to 10 times per second per account. You can call this operation up to 100 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Lang | Strin g | Query | No | zh | The language. Valid values: zh and en. You can leave this parameter empty if it is not required for your business. |
| AliUid | Long | Query | No | 123456789 | The user ID. |
| GroupNa me | Strin g | Query | No | GroupName | The name of the address book. |
| GroupTyp e | Strin g | Query | No | ip | The type of the address book. |
| ActionTyp e | Strin g | Query | No | pass | The action. A value of pass indicates that access is allowed. A value of alert indicates that access is only logged. A value of drop indicates that access is blocked. |
| Descriptio n | Strin g | Query | No | test | The description of the address book. |
| AddressLi st | Strin g | Query | No | 10.82.x.10/32,10.82.x.10 /23,10.82.x.10/16 | The IP addresses. |

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| AddressTy pe | Strin g | Query | No | mdi | Indicates how the IP addresses are specified. A value of fileImport indicates that the IP addresses are specified by importing a file. A value of mdi indicates that the IP addresses are manually specified. If you set the parameter to fileImport, FileUrl and FileName are required. If you set the parameter to mdi, AddressList is required. |
| FileUrl | Strin g | Query | No | http://xxx.com | The URL of the file. |
| FileName | Strin g | Query | No | test | The name of the file. |
| AddressGr oupUuid | Strin g | Query | No | cfa13285-5330-xxx-xxx- 5075c12c6aa8 | The address book UUID. |
| FileObj | Strin g | Query | No | test obj _ | The file object. |
| User | Strin g | Query | No | admin | The username. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Module | String | ndr*** | The name of the module. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=ModifyAddressGroup&RegionId=cnhangzhou&Lang=zh&AliUid=123456789&GroupName=GroupName&GroupType=ip&ActionType=pass&Descri ion=test&AddressList=10.82.x.10/32,10.82.x.10/23,10.82.x.10/16&AddressType=mdi&FileUrl=ht ://xxx.com&FileName=test&AddressGroupUuid=cfa13285-5330-xxx-xxx- 5075c12c6aa8&FileObj=test_obj&User=admin
```

Sample success responses `JSON` format

```
Content-Type:application/json
```

`{`

```json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "Module":"ndr***"
```

`}` `XML` format

```xml
Content-Type:application/xml <ModifyAddressGroupResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <Module>ndr***</Module>
</ModifyAddressGroupResponse>
```

##### DelAddressGroup

Deletes one or more address books.

**Authorization information**

| Operation | Access level | Resource type |
|---|---|---|
| yundun- cloudfirewall:DelAddressGroup | Write | acs:yundun-cloudfirewall:*: {#accountId}:* |

**Throttling**

You can call this operation up to 10 times per second per account. You can call this operation up to 100 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Lang | Strin g | Query | No | zh | The language. Valid values: zh and en. You can leave this parameter empty if it is not required for your business. |
| User | Strin g | Query | No | user | The user. |
| AliUid | Long | Query | No | 1234567890 | The user ID. |
| AddressGr oupUuidLi st | Strin g | Query | No | 13285-5330-402e-980c- 5075c12c6xx8,13285- 5330-402e-980c- 5075c12c6yy8 | The UUIDs of the address books that you want to delete. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Module | String | ndr*** | The name of the module. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=DelAddressGroup&RegionId=cnhangzhou&Lang=zh&User=user&AliUid=1234567890&AddressGroupUuidList=13285-5330-402e-980c- 5075c12c6xx8,13285-5330-402e-980c-5075c12c6yy8
```

Sample success responses `JSON` format

```
Content-Type:application/json
```

`{`

```json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "Module":"ndr***"
```

`}` `XML` format

```xml
Content-Type:application/xml <DelAddressGroupResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <Module>ndr***</Module>
</DelAddressGroupResponse>
```

##### AddAddressGroup

Creates an address book.

**Authorization information**

| Operation | Access level | Resource type |
|---|---|---|
| yundun- cloudfirewall:AddAddressGroup | Write | acs:yundun-cloudfirewall:*: {#accountId}:* |

**Throttling**

You can call this operation up to 10 times per second per account. You can call this operation up to 100 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Lang | Strin g | Query | No | zh | The language. Valid values: zh and en. You can leave this parameter empty if it is not required for your business. |
| AliUid | Long | Query | No | 1234567890 | The user ID. |
| GroupNa me | Strin g | Query | No | test | The name of the address book. |
| GroupTyp e | Strin g | Query | No | ip | The type of the address book. Default value: ip. |

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| ActionTyp e | Strin g | Query | No | pass | The action. Default value: pass. |
| Descriptio n | Strin g | Query | No | test | The description of the address book. |
| AddressTy pe | Strin g | Query | No | mdi | Indicates how the IP addresses are specified. A value of fileImport indicates that the IP addresses are specified by importing a file. A value of mdi indicates that the IP addresses are manually specified. |
| AddressLi st | Strin g | Query | No | 1.1.1.1,2.2.2.2 | The IP addresses. This parameter is required if AddressType is set to mdi. |
| FileUrl | Strin g | Query | No | https://bucket.test.com | The URL of the file. This parameter is required if AddressType is set to fileImport. |
| FileName | Strin g | Query | No | test.csv | The name of the file. This parameter is required if AddressType is set to fileImport. |
| FileObj | Strin g | Query | No | test object.csv _ | The file that is stored in Object Storage Service (OSS) as an object. This parameter is required if AddressType is set to fileImport. |
| User | Strin g | Query | No | test | The user. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |

| Developer Guide·A on | PI documentat |   | Cloud Security Network Detecti n and Respons |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| Success | Boolean | true | Indicates whether the request was successful. |
| Module | String | dispatch rule _ | The name of the module. |
| Error | String | error | The error message. |
| HttpStatusCod e | Integer | 404 | The error code. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=AddAddressGroup&RegionId=cnhangzhou&Lang=zh&AliUid=1234567890&GroupName=test&GroupType=ip&ActionType=pass&Descriptio test&AddressType=mdi&AddressList=1.1.1.1,2.2.2.2&FileUrl=https://bucket.test.com&FileName est.csv&FileObj=test_object.csv&User=test
```

Sample success responses `JSON` format

```
Content-Type:application/json
```

`{`

```json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "Success":true,
    "Module":"dispatch_rule",
    "Error":"error",
    "HttpStatusCode":404
```

`}` `XML` format

```xml
Content-Type:application/xml <AddAddressGroupResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <Success>true</Success>
    <Module>dispatch_rule</Module>
    <Error>error</Error>
    <HttpStatusCode>404</HttpStatusCode>
</AddAddressGroupResponse>
```

##### GetAllAddressGroupName

Queries the information about all address books.

**Authorization information**

| Operation | Access level | Resource type |
|---|---|---|
| yundun- cloudfirewall:GetAllAddressGro upName | Read | acs:yundun-cloudfirewall:*: {#accountId}:* |

**Throttling**

You can call this operation up to 10 times per second per account. You can call this operation up to 100 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Lang | Strin g | Query | No | zh | The language. Valid values: zh and en. You can leave this parameter empty if it is not required for your business. |
| GroupTyp e | Strin g | Query | No | ip | The type of the address book. |
| AliUid | Strin g | Query | No | 123456789 | The user ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| DataList | Array |   |   |
| - AddressGroup Uuid | String | cfa13285-5330- xxx-xxx- 5075c12c6aa8 | The address book UUID. |
| -GroupName | String | GroupName | The name of the address book. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| TotalCount | Integer | 100 | The total number of entries returned. |
| Success | Boolean | true | Indicates whether the HTTP request was successful. |
| Module | String | ndr*** | The name of the module. |
| HttpStatusCod e | Integer | 200 | The HTTP status code. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=GetAllAddressGroupName&RegionId=cnhangzhou&Lang=zh&GroupType=ip&AliUid=123456789
```

Sample success responses `JSON` format

```
Content-Type:application/json
```

`{`

```json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "TotalCount":100,
    "DataList":[
```

`{`

```json
            "GroupName":"GroupName",
            "AddressGroupUuid":"cfa13285-5330-xxx-xxx-5075c12c6aa8"
```

`}` `],`

```json
    "Success":true,
    "Module":"ndr***",
    "HttpStatusCode":200
```

`}` `XML` format

```xml
Content-Type:application/xml <GetAllAddressGroupNameResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <TotalCount>100</TotalCount>
    <DataList>
        <AddressGroupUuid>cfa13285-5330-xxx-xxx-5075c12c6aa8</AddressGroupUuid>
        <GroupName>GroupName</GroupName>
    </DataList>
    <Success>true</Success>
    <Module>ndr***</Module>
    <HttpStatusCode>200</HttpStatusCode>
</GetAllAddressGroupNameResponse>
```

##### DescribeAddressGroup

Queries a list of address books.

**Authorization information**

| Operation | Access level | Resource type |
|---|---|---|
| yundun- cloudfirewall:DescribeAddressG roup | Read | acs:yundun-cloudfirewall:*: {#accountId}:* |

**Throttling**

You can call this operation up to 10 times per second per account. You can call this operation up to 100 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Lang | Strin g | Query | No | zh | The language. Valid values: zh and en. You can leave this parameter empty if it is not required for your business. |

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| AliUid | Long | Query | No | 1234567890 | The user ID. |
| ActionTyp e | Strin g | Query | No | none | The action. Default value: none. |
| GroupTyp e | Strin g | Query | No | ip | The type of the address book. Default value: ip. |
| Query | Strin g | Query | No | test | The keywords used to filter address books. You can enter a name, a description, or an IP address. |
| CurrentPa ge | Integ er | Query | No | 1 | The page number. |
| PageSize | Integ er | Query | No | 10 | The number of entries per page. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| AddressGroup s | Array |   |   |
| -GroupName | String | test | The name of the address book. |
| -Description | String | test | The description of the address book. |
| -AddressList | String | 223.5.5.0/24,1.1.1. 1/32 | The IP addresses. |
| - AddressGroup Uuid | String | cfa13285-5330- 402e-980c- 5075c12c6aa8 | The address book UUID. |
| -ActionType | String | none | The action. |
| -GroupType | String | ip | The type of the address book. Default value: ip. |
| -AliUid | Long | 1234567890 | The user ID. |

| Cloud Security Ne and Response | twork Detectio |   | Developer Guide·API documenta io |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| -AddressType | String | mdi | Indicates how the IP addresses are specified. A value of fileImport indicates that the IP addresses are specified by importing a file. A value of mdi indicates that the IP addresses are manually specified. |
| -FileName | String | test.csv | The name of the file. This parameter is required when AddressType is set to fileImport. |
| -FileUrl | String | https//:bucket.oss.t est.com | The download URL of the file. |
| -UseCount | Integer | 2 | The number of times that the address book is referenced. |
| -DeptName | String | test | The name of the department. |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| TotalCount | Integer | 100 | The total number of entries returned. |
| PageSize | Integer | 10 | The number of entries per page. |
| CurrentPage | Integer | 1 | The page number. |
| Module | String | ndr*** | The name of the module. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=DescribeAddressGroup&RegionId=cnhangzhou&Lang=zh&AliUid=1234567890&ActionType=none&GroupType=ip&Query=test&CurrentPage=1& geSize=10
```

Sample success responses `JSON` format

```
Content-Type:application/json
```

`{`

```json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "TotalCount":100,
    "PageSize":10,
    "CurrentPage":1,
    "AddressGroups":[
```

`{`

```json
            "GroupName":"test",
            "FileUrl":"https//:bucket.oss.test.com",
            "Description":"test",
            "ActionType":"none",
            "GroupType":"ip",
            "UseCount":2,
            "FileName":"test.csv",
            "DeptName":"test",
            "AddressList":"223.5.5.0/24,1.1.1.1/32",
            "AddressType":"mdi",
            "AddressGroupUuid":"cfa13285-5330-402e-980c-5075c12c6aa8",
            "AliUid":1234567890
```

`}` `],`

```json
    "Module":"ndr***"
```

`}` `XML` format

```xml
Content-Type:application/xml <DescribeAddressGroupResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <TotalCount>100</TotalCount>
    <PageSize>10</PageSize>
    <CurrentPage>1</CurrentPage>
    <AddressGroups>
        <GroupName>test</GroupName>
        <Description>test</Description>
        <AddressList>223.5.5.0/24,1.1.1.1/32</AddressList>
        <AddressGroupUuid>cfa13285-5330-402e-980c-5075c12c6aa8</AddressGroupUuid>
        <ActionType>none</ActionType>
        <GroupType>ip</GroupType>
        <AliUid>1234567890</AliUid>
        <AddressType>mdi</AddressType>
        <FileName>test.csv</FileName>
        <FileUrl>https//:bucket.oss.test.com</FileUrl>
        <UseCount>2</UseCount>
        <DeptName>test</DeptName>
    </AddressGroups>
    <Module>ndr***</Module>
</DescribeAddressGroupResponse>
```

#### Intrusion detection rules

##### DescribeIdsRulesList

Queries a list of Intrusion Detection System (IDS) rules.

**Authorization information**

| Operation | Access level | Resource type |
|---|---|---|
| yundun- cloudfirewall:DescribeIdsRulesLi st | Read | acs:yundun-cloudfirewall:*: {#accountId}:* |

**Throttling**

You can call this operation up to 10 times per second per account. You can call this operation up to 100 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Lang | Strin g | Query | No | zh | The language. Valid values: zh and en. You can leave this parameter empty if it is not required for your business. |
| PageNo | Strin g | Query | No | 1 | The page number. |
| PageSize | Strin g | Query | No | 10 | The number of entries per page. |
| OtherRule | Strin g | Query | No | Rule name | The information about the rule, such as the rule ID, the rule name, and the application from which attacks are launched |
| RuleEngin e | Repe atList | Query | No | basicRule | The rule engine. A value of basicRule indicates a basic rule. A value of patchRule indicates a virtual rule. |
| DefaultSta tus | Repe atList | Query | No | 1 | The status of the rule. A value of 0 indicates that the rule is disabled. A value of 1 indicates that the rule is enabled. |
| VulLevel | Repe atList | Query | No | Risk level | The risk level. |

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| AttackTyp e | Repe atList | Query | No | 1 | The attack type. A value of 1 indicates abnormal connections. A value of 2 indicates command executions. A value of 3 indicates brute-force attacks. A value of 4 indicates scanning attacks. A value of 5 indicates other attacks. A value of 6 indicates information leaks. A value of 7 indicates distributed denial of service attacks. A value of 8 indicates overflow attacks. A value of 9 indicates web attacks. A value of 10 indicates Webshell attacks. A value of 11 indicates viruses and worms. A value of 12 indicates mining behaviors. A value of 13 indicates reverse shells. A value of 14 indicates abnormal links. |
| DefaultMo de | Repe atList | Query | No | 0 | The default action. A value of 0 indicates that access is allowed. A value of 1 indicates that an alert is sent. A value of 2 indicates that access is blocked. A value of 4 indicates that access is logged. A value of 5 indicates that access is observed or blocked. |
| RuleDirect ion | Repe atList | Query | No | in | The traffic direction. Valid values: in and out. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Rules | Array |   |   |

| on |   |   | n and Respons |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| -RuleMode | Integer | Rule mode | The mode of the rule. |
| -UpdateTime | String | 1706668721 | The time when the rule was updated. |
| -EventDetailEn | String | Event details in English | The event details in English. |
| -Remark | String | Rule remarks | The remarks of the rule. |
| -RuleStatus | Integer | 1 | The status of the rule. A value of 0 indicates that the rule is disabled. A value of 1 indicates that the rule is enabled. |
| -AttackApp | String | Attack target | The attack target. |
| -ManualCheck | Integer | Manual checks | The manual checks |
| -RuleContent | String | Rule content | The content of the rule. |
| -Reference | String | Association information | The association information. |
| -DefaultStatus | String | 1 | The status of the rule. A value of 0 indicates that the rule is disabled. A value of 1 indicates that the rule is enabled. |
| -Cve | String | CVE ID | The common vulnerabilities and exposures (CVE) ID. |
| -AttackType | Integer | 1 | The attack type. A value of 1 indicates abnormal connections. A value of 2 indicates command executions. A value of 3 indicates brute-force attacks. A value of 4 indicates scanning attacks. A value of 5 indicates other attacks. A value of 6 indicates information leaks. A value of 7 indicates distributed denial of service attacks. A value of 8 indicates overflow attacks. A value of 9 indicates web attacks. A value of 10 indicates Webshell attacks. A value of 11 indicates viruses and worms. A value of 12 indicates mining behaviors. A value of 13 indicates reverse shells. A value of 14 indicates abnormal links. |
| -RuleUuid | String | Rule UUID | The rule UUID. |

| loud Security Net and Response | work Detectio |   | Developer Guide·API documenta io |
|---|---|---|---|
| Parameter | Type | Example | Description |
| -CreateTime | String | 1706668721 | The time when the rule was created. |
| -DefaultMode | Integer | 0 | The default action. A value of 0 indicates that access is allowed. A value of 1 indicates that an alert is sent. A value of 2 indicates that access is blocked. A value of 4 indicates that access is logged. A value of 5 indicates that access is observed or blocked. |
| -InvadeDetect | Integer | Protection type | The protection type. |
| -RuleName | String | Rule name | The name of the rule. |
| -MaySkip | Integer | Skipped or not | Indicates whether the rule can be skipped. |
| -VulLevel | Integer | Risk level | The risk level. |
| -EventDetail | String | Event details | The event details. |
| -ReferenceEn | String | Association information in English | The association information in English. |
| -VulId | String | Rule actual ID | The actual ID of the rule. |
| -Operation | String | Operation type | The operation type. |
| -RuleSource | String | Rule data source | The data source of the rule. |
| -RuleEngine | String | basicRule | The rule engine. A value of basicRule indicates a basic rule. A value of patchRule indicates a virtual rule. |
| -Description | String | Rule description | The description of the rule. |
| -DescriptionEn | String | Rule description in English | The description of the rule in English. |
| -RuleDirection | String | in | The traffic direction. Valid values: in and out. |
| -RuleOwner | String | Rule creator | The user who created the rule. |

| Developer Guide·A on | PI documentat |   | Cloud Security Network Detecti n and Respons |
|---|---|---|---|
| Parameter | Type | Example | Description |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| PageNo | Integer | 1 | The page number. |
| PageSize | Integer | 10 | The number of entries per page. |
| TotalCount | Integer | 100 | The total number of entries returned. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=DescribeIdsRulesList&RegionId=cnhangzhou&Lang=zh&PageNo=1&PageSize=10&OtherRule=Rule name&RuleEngine.1=basicRule&DefaultStatus.1=1&VulLevel.1=Risk level&AttackType.1=1&DefaultMode.1=0&RuleDirection.1=in
```

Sample success responses `JSON` format

```
Content-Type:application/json
```

`{`

```json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "PageNo":1,
    "PageSize":10,
    "Rules":[
```

`{`

```json
            "RuleSource":"Rule data source",
            "Description":"Rule description",
            "ReferenceEn":"Association information in English",
            "RuleMode":"Rule mode",
            "RuleContent":"Rule content",
            "EventDetail":"Event details",
            "Operation":"Operation type",
            "Remark":"Rule remarks",
            "DefaultStatus":"1",
            "ManualCheck":"Manual checks",
            "RuleOwner":"Rule creator",
            "VulId":"Rule actual ID",
            "RuleName":"Rule name",
            "VulLevel":"Risk level",
            "RuleEngine":"basicRule",
            "Reference":"Association information",
            "DescriptionEn":"Rule description in English",
            "CreateTime":"1706668721",
            "EventDetailEn":"Event details in English",
            "AttackType":1,
            "RuleUuid":"Rule UUID",
            "RuleDirection":"in",
            "MaySkip":"Skipped or not",
            "Cve":"CVE ID",
            "UpdateTime":"1706668721",
            "RuleStatus":1,
            "InvadeDetect":"Protection type",
            "AttackApp":"Attack target",
            "DefaultMode":0
```

`}` `],`

```json
    "TotalCount":100
```

`}` `XML` format

```xml
Content-Type:application/xml <DescribeIdsRulesListResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <PageNo>1</PageNo>
    <PageSize>10</PageSize>
    <Rules>
        <RuleMode>Rule mode</RuleMode>
        <UpdateTime>1706668721</UpdateTime>
        <EventDetailEn>Event details in English</EventDetailEn>
        <Remark>Rule remarks</Remark>
        <RuleStatus>1</RuleStatus>
        <AttackApp>Attack target</AttackApp>
        <ManualCheck>Manual checks</ManualCheck>
        <RuleContent>Rule content</RuleContent>
        <Reference>Association information</Reference>
        <DefaultStatus>1</DefaultStatus>
        <Cve>CVE ID</Cve>
        <AttackType>1</AttackType>
        <RuleUuid>Rule UUID</RuleUuid>
        <CreateTime>1706668721</CreateTime>
        <DefaultMode>0</DefaultMode>
        <InvadeDetect>Protection type</InvadeDetect>
        <RuleName>Rule name</RuleName>
        <MaySkip>Skipped or not</MaySkip>
        <VulLevel>Risk level</VulLevel>
        <EventDetail>Event details</EventDetail>
        <ReferenceEn>Association information in English</ReferenceEn>
        <VulId>Rule actual ID</VulId>
        <Operation>Operation type</Operation>
        <RuleSource>Rule data source</RuleSource>
        <RuleEngine>basicRule</RuleEngine>
        <Description>Rule description</Description>
        <DescriptionEn>Rule description in English</DescriptionEn>
        <RuleDirection>in</RuleDirection>
        <RuleOwner>Rule creator</RuleOwner>
    </Rules>
    <TotalCount>100</TotalCount>
</DescribeIdsRulesListResponse>
```

##### UpdateSingleIdsDefaultStatus

You can call the UpdateSingleIdsDefaultStatus operation to update the default status of an Intrusion Detection System (IDS) rule.

**Authorization information**

| Operation | Access level | Resource type |
|---|---|---|
| yundun- cloudfirewall:UpdateSingleIdsD efaultStatus | Write | acs:yundun-cloudfirewall:*: {#accountId}:* |

**Throttling**

Per user: 10 queries per second (QPS). Per operation: 100 QPS.

**Request headers**

This operation uses only common request headers. For more information, see Common parameters.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Lang | Strin g | Query | No | zh | The language of the response. Valid values: zh (Chinese) and en (English). |
| RuleEngin e | Strin g | Query | No | basicRule | The rules engine. Valid values: basicRule (Basic Policies) and patchRule (virtual patches). |
| RuleUuid | Strin g | Query | No | RuleUuid | The UUID of the rule. |
| DefaultSta tus | Long | Query | No | 1 | The status of the rule. Valid values: 0 (disable) and 1 (enable). |

**Data**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The ID of the request. |
| Code | Integer | 200 | The HTTP status code. |
| Module | String | ndr*** | The name of the module. |
| Message | String | success | The response message. |

**Examples**

Request example

```
https://[Endpoint]/?Action=UpdateSingleIdsDefaultStatus&RegionId=cnhangzhou&Lang=zh&RuleEngine=basicRule&RuleUuid=RuleUuid&DefaultStatus=1
```

Sample responses `JSON` format

```
Content-Type:application/json
```

`{`

```json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "Code":200,
    "Module":"ndr***",
    "Message":"success"
```

`}` `XML` format

```xml
Content-Type:application/xml <UpdateSingleIdsDefaultStatusResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <Code>200</Code>
    <Module>ndr***</Module>
    <Message>success</Message>
</UpdateSingleIdsDefaultStatusResponse>
```

##### AddCustomIdsRule

Creates a custom Intrusion Detection System (IDS) rule.

**Authorization information**

| Operation | Access level | Resource type |
|---|---|---|
| yundun- cloudfirewall:AddCustomIdsRul e | Write | acs:yundun-cloudfirewall:*: {#accountId}:* |

**Throttling**

You can call this operation up to 10 times per second per account. You can call this operation up to 100 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Lang | Strin g | Query | No | zh | The language. Valid values: zh and en. You can leave this parameter empty if it is not required for your business. |
| RuleEngin e | Strin g | Query | No | basicRule | The rule engine. A value of basicRule indicates a basic rule. A value of patchRule indicates a virtual rule. |
| RuleConte nt | Strin g | Query | No | Rule content | The content of the rule. |
| RuleMode | Long | Query | No | Rule mode | The mode of the rule. |
| VulLevel | Long | Query | No | Risk level | The risk level. |
| RuleName | Strin g | Query | No | Rule name | The name of the rule. |
| RuleName En | Strin g | Query | No | Rule name in English | The name of the rule in English. |
| Descriptio n | Strin g | Query | No | Rule description | The description of the rule. |
| Descriptio nEn | Strin g | Query | No | Rule description in English | The description of the rule in English. |
| RuleOwne r | Strin g | Query | No | Rule creator | The user who created the rule. |

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| AttackTyp e | Long | Query | No | 1 | The attack type. A value of 1 indicates abnormal connections. A value of 2 indicates command executions. A value of 3 indicates brute-force attacks. A value of 4 indicates scanning attacks. A value of 5 indicates other attacks. A value of 6 indicates information leaks. A value of 7 indicates distributed denial of service attacks. A value of 8 indicates overflow attacks. A value of 9 indicates web attacks. A value of 10 indicates Webshell attacks. A value of 11 indicates viruses and worms. A value of 12 indicates mining behaviors. A value of 13 indicates reverse shells. A value of 14 indicates abnormal links. |
| InvadeDet ect | Long | Query | No | Protection type | The protection type. |
| EventDeta il | Strin g | Query | No | Event details | The event details. |
| EventDeta ilEn | Strin g | Query | No | Event details in English | The event details in English. |
| Reference | Strin g | Query | No | Association information | The association information. |
| Reference En | Strin g | Query | No | Association information in English | The association information in English. |

| loud Security | Network | Detectio |   | Devel | oper Guide·API documenta |
|---|---|---|---|---|---|

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Operation | Strin g | Query | No | Operation type | The operation type. |
| ManualCh eck | Long | Query | No | Manual checks | The manual checks. |
| MaySkip | Long | Query | No | Skipped or not | Specifies whether to skip the rule. |
| AttackApp | Strin g | Query | No | Attack target | The attack target. |
| DefaultMo de | Long | Query | No | 0 | The default action. A value of 0 indicates that access is allowed. A value of 1 indicates that an alert is sent. A value of 2 indicates that access is blocked. A value of 4 indicates access is logged. A value of 5 indicates that access is observed or blocked. |
| Cve | Strin g | Query | No | CVE ID | The common vulnerabilities and exposures (CVE) ID. |
| Remark | Strin g | Query | No | Rule remarks | The remarks of the rule. |
| DefaultSta tus | Long | Query | No | 1 | The status of the rule. A value of 0 indicates that the rule is disabled. A value of 1 indicates that the rule is enabled. |
| RuleDirect ion | Strin g | Query | No | in | The traffic direction. Valid values: in and out. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Code | Integer | 200 | The HTTP status code. |

| Developer Guide·A on | PI documentat |   | Cloud Security Network Detecti n and Respons |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| Module | String | ndr*** | The name of the module. |
| Message | String | success | The returned message. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=AddCustomIdsRule&RegionId=cnhangzhou&Lang=zh&RuleEngine=basicRule&RuleContent=Rule content&RuleMode=Rule mode&VulLe vel=Risk level&RuleName=Rule name&RuleNameEn=Rule name in English&Description=Rule desc ription&DescriptionEn=Rule description in English&RuleOwner=Rule creator&AttackType=1&InvadeDetect=Protection type&EventDetail=Event details&EventDetailEn=Event details in English&Reference=Association information&ReferenceEn=Association information in English&Operation=Operation type&Man ualCheck=Manual checks&MaySkip=Skipped or not&AttackApp=Attack target&DefaultMode=0&Cve=CVE ID&Remark=Rule remarks&DefaultStatus=1&RuleDirection=in
```

Sample success responses `JSON` format

```
Content-Type:application/json
```

`{`

```json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "Code":200,
    "Module":"ndr***",
    "Message":"success"
```

`}` `XML` format

```xml
Content-Type:application/xml <AddCustomIdsRuleResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <Code>200</Code>
    <Module>ndr***</Module>
    <Message>success</Message>
</AddCustomIdsRuleResponse>
```

##### DeleteIdsRule

Deletes an Intrusion Detection System (IDS) rule.

**Authorization information**

| Operation | Access level | Resource type |
|---|---|---|
| yundun- cloudfirewall:DeleteIdsRule | Write | acs:yundun-cloudfirewall:*: {#accountId}:* |

**Throttling**

You can call this operation up to 10 times per second per account. You can call this operation up to 100 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Lang | Strin g | Query | No | zh | The language. Valid values: zh and en. You can leave this parameter empty if it is not required for your business. |
| RuleUuid | Strin g | Query | No | Rule UUID | The rule UUID. |
| RuleEngin e | Strin g | Query | No | basicRule | The rule engine. A value of basicRule indicates a basic rule. A value of patchRule indicates a virtual rule. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Code | Integer | 200 | The HTTP status code. |
| Module | String | ndr*** | The name of the module. |
| Message | String | success | The returned message. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=DeleteIdsRule&RegionId=cn-hangzhou&Lang=zh&RuleUuid=Rule UUI D&RuleEngine=basicRule
```

Sample success responses `JSON` format

```
Content-Type:application/json
```

`{`

```json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "Code":200,
    "Module":"ndr***",
    "Message":"success"
```

`}` `XML` format

```xml
Content-Type:application/xml <DeleteIdsRuleResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <Code>200</Code>
    <Module>ndr***</Module>
    <Message>success</Message>
</DeleteIdsRuleResponse>
```

##### UpdateIdsDefaultStatus

Modifies the default status of Intrusion Detection System (IDS) rules.

**Authorization information**

| Operation | Access level | Resource type |
|---|---|---|
| yundun- cloudfirewall:UpdateIdsDefaultS tatus | Write | acs:yundun-cloudfirewall:*: {#accountId}:* |

**Throttling**

You can call this operation up to 10 times per second per account. You can call this operation up to 100 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Lang | Strin g | Query | No | zh | The language. Valid values: zh and en. You can leave this parameter empty if it is not required for your business. |
| RuleUuidL ist | Repe atList | Query | No | Uuid1,Uuid2 | The rule UUIDs. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Code | Integer | 200 | The HTTP status code. |
| Module | String | ndr*** | The name of the module. |
| Message | String | success | The returned message. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=UpdateIdsDefaultStatus&RegionId=cnhangzhou&Lang=zh&RuleUuidList.1=Uuid1,Uuid2
```

Sample success responses `JSON` format

```
Content-Type:application/json
```

`{`

```json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "Code":200,
    "Module":"ndr***",
    "Message":"success"
```

`}` `XML` format

```xml
Content-Type:application/xml <UpdateIdsDefaultStatusResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <Code>200</Code>
    <Module>ndr***</Module>
    <Message>success</Message>
</UpdateIdsDefaultStatusResponse>
```

##### UpdateIdsRule

Updates an Intrusion Detection System (IDS) rule.

**Authorization information**

| Operation | Access level | Resource type |
|---|---|---|
| yundun- cloudfirewall:UpdateIdsRule | Write | acs:yundun-cloudfirewall:*: {#accountId}:* |

**Throttling**

You can call this operation up to 10 times per second per account. You can call this operation up to 100 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Lang | Strin g | Query | No | zh | The language. Valid values: zh and en. You can leave this parameter empty if it is not required for your business. |
| RuleEngin e | Strin g | Query | No | basicRule | The rule engine. A value of basicRule indicates a basic rule. A value of patchRule indicates a virtual rule. |
| RuleConte nt | Strin g | Query | No | Rule content | The content of the rule. |
| RuleMode | Long | Query | No | Rule mode | The mode of the rule. |

| loud Security and Respon | Network se | Detectio |   | Devel | oper Guide·API documenta io |
|---|---|---|---|---|---|

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| VulLevel | Long | Query | No | Risk level | The risk level. |
| RuleName | Strin g | Query | No | Rule name | The name of the rule. |
| RuleName En | Strin g | Query | No | Rule name in English | The name of the rule in English. |
| Descriptio n | Strin g | Query | No | Rule description | The description of the rule. |
| Descriptio nEn | Strin g | Query | No | Rule description in English | The description of the rule in English. |
| RuleOwne r | Strin g | Query | No | Creator | The user who created the rule. |
| AttackTyp e | Long | Query | No | 1 | The attack type. A value of 1 indicates abnormal connections. A value of 2 indicates command executions. A value of 3 indicates brute-force attacks. A value of 4 indicates scanning attacks. A value of 5 indicates other attacks. A value of 6 indicates information leaks. A value of 7 indicates distributed denial of service attacks. A value of 8 indicates overflow attacks. A value of 9 indicates web attacks. A value of 10 indicates Webshell attacks. A value of 11 indicates viruses and worms. A value of 12 indicates mining behaviors. A value of 13 indicates reverse shells. A value of 14 indicates abnormal links. |
| InvadeDet ect | Long | Query | No | Protection type | The protection type. |
| EventDeta il | Strin g | Query | No | Event details | The event details. |

| Developer Gui on | de·API d | ocumentat |   | Cloud | Security Network Detecti n and Respons |
|---|---|---|---|---|---|

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| EventDeta ilEn | Strin g | Query | No | Event details in English | The event details in English. |
| Reference | Strin g | Query | No | Association information | The association information. |
| Reference En | Strin g | Query | No | Association information in English | The association information in English. |
| Operation | Strin g | Query | No | Operation type | The operation type. |
| ManualCh eck | Long | Query | No | Manual checks | The manual checks. |
| MaySkip | Long | Query | No | Skipped or not | Specifies whether to skip the rule. |
| AttackApp | Strin g | Query | No | Attack target | The attack target. |
| DefaultMo de | Long | Query | No | 0 | The default action. A value of 0 indicates that access is allowed. A value of 1 indicates that an alert is sent. A value of 2 indicates that access is blocked. A value of 4 indicates access is logged. A value of 5 indicates that access is observed or blocked. |
| Cve | Strin g | Query | No | CVE ID | The common vulnerabilities and exposures (CVE) ID. |
| Remark | Strin g | Query | No | Rule remarks | The remarks of the rule. |
| DefaultSta tus | Long | Query | No | 1 | The status of the rule. A value of 0 indicates that the rule is disabled. A value of 1 indicates that the rule is enabled. |
| RuleDirect ion | Strin g | Query | No | in | The traffic direction. Valid values: in and out. |

| Cloud Security and Respon | Network se | Detectio |   | Devel | oper Guide·API documenta io |
|---|---|---|---|---|---|

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| RuleUuid | Strin g | Query | No | Rule UUID | The rule UUID. |
| VulId | Strin g | Query | No | Rule actual ID | The actual ID of the rule. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Code | Integer | 200 | The HTTP status code. |
| Module | String | ndr*** | The name of the module. |
| Message | String | success | The returned message. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=UpdateIdsRule&RegionId=cnhangzhou&Lang=zh&RuleEngine=basicRule&RuleContent=Rule content&RuleMode=Rule mode&VulLe vel=Risk level&RuleName=Rule name&RuleNameEn=Rule name in English&Description=Rule desc ription&DescriptionEn=Rule description in English&RuleOwner=Rule creator&AttackType=1&InvadeDetect=Protection type&EventDetail=Event details&EventDetailEn=Event details in English&Reference=Association information&ReferenceEn=Association information in English&Operation=Operation type&Man ualCheck=Manual checks&MaySkip=Skipped or not&AttackApp=Attack target&DefaultMode=0&Cve=CVE ID&Remark=Rule remarks&DefaultStatus=1&RuleDirection=in&RuleUuid=Rule UUID&VulId=Rule actual ID
```

Sample success responses `JSON` format

```
Content-Type:application/json
```

`{`

```json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "Code":200,
    "Module":"ndr***",
    "Message":"success"
```

`}` `XML` format

```xml
Content-Type:application/xml <UpdateIdsRuleResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <Code>200</Code>
    <Module>ndr***</Module>
    <Message>success</Message>
</UpdateIdsRuleResponse>
```

#### IP address pools for internal network

**assets**

##### ModifyIpSegment

Modifies a CIDR block for traffic collection.

**Authorization information**

| Operation | Access level | Resource type |
|---|---|---|
| yundun- cloudfirewall:ModifyIpSegment | Write | acs:yundun-cloudfirewall:*: {#accountId}:* |

**Throttling**

You can call this operation up to 10 times per second per account. You can call this operation up to 100 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Lang | Strin g | Query | No | zh | The language. Valid values: zh and en. You can leave this parameter empty if it is not required for your business. |

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| IpSegmen tName | Strin g | Query | No | 1.1.1.0/24 | The CIDR block. |
| IpId | Strin g | Query | No | 1024 | The policy ID. |
| InfoName | Strin g | Query | No | region-test | The region to which the CIDR block belongs. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=ModifyIpSegment&RegionId=cnhangzhou&Lang=zh&IpSegmentName=1.1.1.0/24&IpId=1024&InfoName=region-test
```

Sample success responses `JSON` format

```
Content-Type:application/json
```

`{`

```json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************"
```

`}` `XML` format

```xml
Content-Type:application/xml <ModifyIpSegmentResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
</ModifyIpSegmentResponse>
```

##### CreateIpSegment

Adds a CIDR block for traffic collection.

**Authorization information**

| Operation | Access level | Resource type |
|---|---|---|
| yundun- cloudfirewall:CreateIpSegment | Write | acs:yundun-cloudfirewall:*: {#accountId}:* |

**Throttling**

You can call this operation up to 10 times per second per account. You can call this operation up to 100 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Lang | Strin g | Query | No | zh | The language. Valid values: zh and en. You can leave this parameter empty if it is not required for your business. |
| InfoType | Strin g | Query | No | distribution | The type of the CIDR block information. Default value: distribution. |
| IpSegmen tName | Strin g | Query | No | 1.1.1.0/24 | The CIDR block. |
| InfoName | Strin g | Query | No | region-test | The region to which the CIDR block belongs. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=CreateIpSegment&RegionId=cnhangzhou&Lang=zh&InfoType=distribution&IpSegmentName=1.1.1.0/24&InfoName=region-test
```

Sample success responses `JSON` format

```
Content-Type:application/json
```

`{`

```json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************"
```

`}` `XML` format

```xml
Content-Type:application/xml <CreateIpSegmentResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
</CreateIpSegmentResponse>
```

##### DescribeRegionName

Queries the information about a region.

**Authorization information**

| Operation | Access level | Resource type |
|---|---|---|
| yundun- cloudfirewall:DescribeRegionNa me | Read | acs:yundun-cloudfirewall:*: {#accountId}:* |

**Throttling**

You can call this operation up to 10 times per second per account. You can call this operation up to 100 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Lang | Strin g | Query | No | zh | The language. Valid values: zh and en. You can leave this parameter empty if it is not required for your business. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RegionNameLi st | Array |   |   |
| -Code | String | region-test | The code of the region. |
| -CodeName | String | region-test | The name of the region. |
| -CodeType | String | distribution | The code type. Default value: distribution. |
| -Description | String | distribution | The code type. Default value: distribution. |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=DescribeRegionName&RegionId=cn-hangzhou&Lang=zh
```

Sample success responses `JSON` format

```
Content-Type:application/json
```

`{`

```json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "RegionNameList":[
```

`{`

```json
            "CodeName":"region-test",
            "Description":"distribution",
            "CodeType":"distribution",
            "Code":"region-test"
```

`}` `]` `}` `XML` format

```xml
Content-Type:application/xml <DescribeRegionNameResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <RegionNameList>
        <Code>region-test</Code>
        <CodeName>region-test</CodeName>
        <CodeType>distribution</CodeType>
        <Description>distribution</Description>
    </RegionNameList>
</DescribeRegionNameResponse>
```

##### DescribeIpSegment

Queries the configurations of a CIDR block for traffic collection.

**Authorization information**

| Operation | Access level | Resource type |
|---|---|---|
| yundun- cloudfirewall:DescribeIpSegmen t | Read | acs:yundun-cloudfirewall:*: {#accountId}:* |

**Throttling**

You can call this operation up to 10 times per second per account. You can call this operation up to 100 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Lang | Strin g | Query | No | zh | The language. Valid values: zh and en. You can leave this parameter empty if it is not required for your business. |
| IpSegmen t | Strin g | Query | No | 1.1.1.0/24 | The CIDR block. |
| Distributio n | Strin g | Query | No | region-test | The region to which the CIDR block belongs. |

| Developer Gui on | de·API d | ocumentat |   | Cloud | Security Network Detecti n and Respons |
|---|---|---|---|---|---|

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| InfoType | Strin g | Query | No | distribution | The type of the CIDR block information. Default value: distribution. |
| CurrentPa ge | Strin g | Query | No | 1 | The page number. |
| PageSize | Strin g | Query | No | 10 | The number of entries per page. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| IpSegmentList | Array |   |   |
| -Id | Integer | 1024 | The policy ID. |
| -GmtCreate | String | 2024-01- 03T10:38:41Z | The time when the CIDR block for traffic collection was created. |
| -GmtModified | String | 2024-01- 03T10:38:41Z | The time when the CIDR block for traffic collection was modified. |
| -InfoType | String | distribution | The type of the CIDR block information. Default value: distribution. |
| -InfoName | String | region-test | The region to which the CIDR block belongs. |
| -IpExpressions | String | 1.1.1.0/24 | The CIDR block. |
| -IpType | String | ipv4 | The IP address type. |
| -RegionName | String | region-test | The region to which the CIDR block belongs. |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| TotalCount | Integer | 100 | The total number of entries returned. |

| Cloud Security Ne and Response | twork Detectio |   | Developer Guide·API documenta io |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| PageSize | Integer | 10 | The number of entries per page. |
| CurrentPage | Integer | 1 | The page number. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=DescribeIpSegment&RegionId=cnhangzhou&Lang=zh&IpSegment=1.1.1.0/24&Distribution=regiontest&InfoType=distribution&CurrentPage=1&PageSize=10
```

Sample success responses `JSON` format

```
Content-Type:application/json
```

`{`

```json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "TotalCount":100,
    "PageSize":10,
    "CurrentPage":1,
    "IpSegmentList":[
```

`{`

```json
            "IpExpressions":"1.1.1.0/24",
            "GmtCreate":"2024-01-03T10:38:41Z",
            "IpType":"ipv4",
            "RegionName":"region-test",
            "GmtModified":"2024-01-03T10:38:41Z",
            "Id":1024,
            "InfoName":"region-test",
            "InfoType":"distribution"
```

`}` `]` `}` `XML` format

```xml
Content-Type:application/xml <DescribeIpSegmentResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <TotalCount>100</TotalCount>
    <PageSize>10</PageSize>
    <CurrentPage>1</CurrentPage>
    <IpSegmentList>
        <Id>1024</Id>
        <GmtCreate>2024-01-03T10:38:41Z</GmtCreate>
        <GmtModified>2024-01-03T10:38:41Z</GmtModified>
        <InfoType>distribution</InfoType>
        <InfoName>region-test</InfoName>
        <IpExpressions>1.1.1.0/24</IpExpressions>
        <IpType>ipv4</IpType>
        <RegionName>region-test</RegionName>
    </IpSegmentList>
</DescribeIpSegmentResponse>
```

##### DeleteIpSegment

Deletes a CIDR block for traffic collection.

**Authorization information**

| Operation | Access level | Resource type |
|---|---|---|
| yundun- cloudfirewall:DeleteIpSegment | Write | acs:yundun-cloudfirewall:*: {#accountId}:* |

**Throttling**

You can call this operation up to 10 times per second per account. You can call this operation up to 100 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Lang | Strin g | Query | No | zh | The language. Valid values: zh and en. You can leave this parameter empty if it is not required for your business. |

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| IpId | Strin g | Query | No | 1024 | The policy ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=DeleteIpSegment&RegionId=cn-hangzhou&Lang=zh&IpId=1024
```

Sample success responses `JSON` format

```
Content-Type:application/json
```

`{`

```json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************"
```

`}` `XML` format

```xml
Content-Type:application/xml <DeleteIpSegmentResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
</DeleteIpSegmentResponse>
```

##### CheckIpSegment

Checks the policy of a CIDR block for traffic collection.

**Authorization information**

| Operation | Access level | Resource type |
|---|---|---|
| yundun- cloudfirewall:CheckIpSegment | Write | acs:yundun-cloudfirewall:*: {#accountId}:* |

**Throttling**

You can call this operation up to 10 times per second per account. You can call this operation up to 100 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Lang | Strin g | Query | No | zh | The language. Valid values: zh and en. You can leave this parameter empty if it is not required for your business. |
| IpSegmen tName | Strin g | Query | No | 1.1.1.0/24 | The CIDR block. |
| InfoName | Strin g | Query | No | region-test | The region to which the CIDR block belongs. |
| InfoType | Strin g | Query | No | distribution | The type of the CIDR block information. Default value: distribution. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=CheckIpSegment&RegionId=cnhangzhou&Lang=zh&IpSegmentName=1.1.1.0/24&InfoName=region-test&InfoType=distribution
```

Sample success responses `JSON` format

```
Content-Type:application/json
```

`{`

```json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************"
```

`}` `XML` format

```xml
Content-Type:application/xml <CheckIpSegmentResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
</CheckIpSegmentResponse>
```

### Download task management

#### DescribeDownloadTasks

Queries a list of download tasks.

**Authorization information**

| Operation | Access level | Resource type |
|---|---|---|
| yundun- cloudfirewall:DescribeDownload Tasks | Read | acs:yundun-cloudfirewall:*: {#accountId}:* |

**Throttling**

You can call this operation up to 10 times per second per account. You can call this operation up to 100 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Lang | Strin g | Query | No | zh | The language. Valid values: zh and en. You can leave this parameter empty if it is not required for your business. |

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| AliUid | Long | Query | No | 1234567890 | The user ID. |
| Module | Strin g | Query | No | Threat detection | The name of the module. |
| PageNo | Strin g | Query | No | 1 | The page number. |
| PageSize | Strin g | Query | No | 10 | The number of entries per page. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| DataList | Array |   |   |
| -StartTime | Long | 1707118672 | The beginning of the time range to query. |
| -EndTime | Long | 1707118672 | The end of the time range to query. |
| -TaskUUID | String | d5b969bf-cd21- 4dd0-84ff- 8e57c95ef*** | The task UUID. |
| -FileName | String | test.pcap | The name of the file. |
| -Process | Integer | 100 | The progress of the download task. |
| -Module | String | ndr*** | The name of the module. |
| -Status | Integer | 1 | The status of the download task. A value of 0 indicates that the task is in progress. A value of 1 indicates that the task is successful. |
| -SignUrl | String | https://test.com | The download URL of the file. |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| TotalCount | Integer | 100 | The total number of entries returned. |

| Cloud Security Ne and Response | twork Detectio |   | Developer Guide·API documenta io |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| PageSize | Integer | 10 | The number of entries per page. |
| CurrentPage | Integer | 1 | The page number. |
| Success | Boolean | true | Indicates whether the HTTP request was successful. |
| Module | String | ndr*** | The name of the module. |
| HttpStatusCod e | Integer | 200 | The HTTP status code. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=DescribeDownloadTasks&RegionId=cnhangzhou&Lang=zh&AliUid=1234567890&Module=Threat detection&PageNo=1&PageSize=10
```

Sample success responses `JSON` format

```
Content-Type:application/json
```

`{`

```json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "TotalCount":100,
    "PageSize":10,
    "CurrentPage":1,
    "DataList":[
```

`{`

```json
            "Status":1,
            "SignUrl":"https://test.com",
            "EndTime":1707118672,
            "FileName":"test.pcap",
            "StartTime":1707118672,
            "TaskUUID":"d5b969bf-cd21-4dd0-84ff-8e57c95ef***",
            "Process":100,
            "Module":"ndr***"
```

`}` `],`

```json
    "Success":true,
    "Module":"ndr***",
    "HttpStatusCode":200
```

`}` `XML` format

```xml
Content-Type:application/xml <DescribeDownloadTasksResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <TotalCount>100</TotalCount>
    <PageSize>10</PageSize>
    <CurrentPage>1</CurrentPage>
    <DataList>
        <StartTime>1707118672</StartTime>
        <EndTime>1707118672</EndTime>
        <TaskUUID>d5b969bf-cd21-4dd0-84ff-8e57c95ef***</TaskUUID>
        <FileName>test.pcap</FileName>
        <Process>100</Process>
        <Module>ndr***</Module>
        <Status>1</Status>
        <SignUrl>https://test.com</SignUrl>
    </DataList>
    <Success>true</Success>
    <Module>ndr***</Module>
    <HttpStatusCode>200</HttpStatusCode>
</DescribeDownloadTasksResponse>
```

#### DescribeDownloadModules

Queries a list of download and management modules.

**Authorization information**

| Operation | Access level | Resource type |
|---|---|---|
| yundun- cloudfirewall:DescribeDownload Modules | Read | acs:yundun-cloudfirewall:*: {#accountId}:* |

**Throttling**

You can call this operation up to 10 times per second per account. You can call this operation up to 100 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Lang | Strin g | Query | No | zh | The language. Valid values: zh and en. You can leave this parameter empty if it is not required for your business. |
| AliUid | Long | Query | No | 1234567890 | The user ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Modules | Normal | ['Log Query','Attacker Profile' ...] | The modules. |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Success | Boolean | true | Indicates whether the HTTP request was successful. |
| Module | String | ndr*** | The name of the module. |
| HttpStatusCod e | Integer | 200 | The HTTP status code. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=DescribeDownloadModules&RegionId=cnhangzhou&Lang=zh&AliUid=1234567890
```

Sample success responses `JSON` format

```
Content-Type:application/json
```

`{`

```json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "Modules":"['Log Query','Attacker Profile' ...]",
    "Success":true,
    "Module":"ndr***",
    "HttpStatusCode":200
```

`}` `XML` format

```xml
Content-Type:application/xml <DescribeDownloadModulesResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <Modules>
        <string>['Log Query','Attacker Profile' ...]</string>
    </Modules>
    <Success>true</Success>
    <Module>ndr***</Module>
    <HttpStatusCode>200</HttpStatusCode>
</DescribeDownloadModulesResponse>
```

#### DeleteDownloadTaskByUuid

Deletes a download task.

**Authorization information**

| Operation | Access level | Resource type |
|---|---|---|
| yundun- cloudfirewall:DeleteDownloadT askByUuid | Write | acs:yundun-cloudfirewall:*: {#accountId}:* |

**Throttling**

You can call this operation up to 10 times per second per account. You can call this operation up to 100 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Lang | Strin g | Query | No | zh | The language. Valid values: zh and en. You can leave this parameter empty if it is not required for your business. |

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| User | Strin g | Query | No | user | The user. |
| TaskUUID | Strin g | Query | No | F0A8A039-930D-5EC1- 97C8-************ | The task UUID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Success | Boolean | true | Indicates whether the HTTP request was successful. |
| Module | String | ndr*** | The name of the module. |
| HttpStatusCod e | Integer | 200 | The HTTP status code. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=DeleteDownloadTaskByUuid&RegionId=cnhangzhou&Lang=zh&User=user&TaskUUID=F0A8A039-930D-5EC1-97C8-************
```

Sample success responses `JSON` format

```
Content-Type:application/json
```

`{`

```json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "Success":true,
    "Module":"ndr***",
    "HttpStatusCode":200
```

`}` `XML` format

```xml
Content-Type:application/xml <DeleteDownloadTaskByUuidResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <Success>true</Success>
    <Module>ndr***</Module>
    <HttpStatusCode>200</HttpStatusCode>
</DeleteDownloadTaskByUuidResponse>
```

### One-click block

#### AddToBlackList

Adds the source IP address of an attack to the blacklist.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | AddToBlackLi st | The operation that you want to perform. Set the value to AddToBlackList. |
| SrcIp | String | Yes | 183.100.XX.X X | The source IP address of an attack. |
| DstIp | String | No | 120.223.XX.X X | The destination IP address of an attack. |
| DstPort | String | Yes | 8080 | The start of the destination port range of an attack. Valid values: 0 to 65535. If you set this parameter to 0, all ports are specified. |
| DstPortEnd | String | No | 8081 | The end of the destination port range of an attack. Valid values: 0 to 65535. If you set this parameter to 0, all ports are specified. |
| LiveTime | String | Yes | 5 | The validity period of the blacklist. Unit: minutes. Valid values: 1 to 10080. If you leave this parameter unspecified, the default value 5 is used. |

| Filter | String | No | inbound | The direction of the attack traffic that can be blocked by the blacklist. This parameter is available only for the blacklist. Valid values: inbound: blocks traffic destined for data centers in which Apsara Stack is deployed. This is the default value. outbound: blocks traffic sent from data centers in which Apsara Stack is deployed. |
|---|---|---|---|---|
| AliUid | String | No | 123456**** | The Apsara Stack tenant account. |
| IpType | String | No | 4 | The type of the IP addresses. Valid values: 4: IPv4 addresses. This is the default value. 6: IPv6 addresses. |
| Note | String | No | Add the IP address to the blacklist. | The additional description. |

All Alibaba Cloud API operations must include common request parameters. For more information about common request parameters, see Common parameters. For more information about sample requests, see the "Examples" section of this topic.

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | String | 200 | The status code returned for the request. |
| success | String | true | Indicates whether the request is successful. Valid values: true: The request is successful. false: The request failed. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=AddToBlackList &SrcIp=183.100.XX.XX &DstIp=120.223.XX.XX &DstPort=8080 &LiveTime=5 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<code>200</code> <success>true</requestId>
```

`JSON` format `{`

```json
  "code": 200,
  "success": "true"
```

`}`

**Error codes**

For a list of error codes, see Error codes.

#### AddToWhiteList

Adds the source IP address of an attack to the whitelist.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | AddToWhiteLi st | The operation that you want to perform. Set the value to AddToWhiteList. |
| SrcIp | String | No | 183.100.XX.X X | The source IP address of an attack. |
| DstIp | String | Yes | 120.223.XX.X X | The destination IP address of an attack. |
| DstPort | String | No | 8080 | The start of the destination port range of an attack. Valid values: 0 to 65535. If you set this parameter to 0, all ports are specified. |
| DstPortEnd | String | No | 8081 | The end of the destination port range of an attack. Valid values: 0 to 65535. If you set this parameter to 0, all ports are specified. |
| LiveTime | String | No | 5 | The validity period of the whitelist. Unit: minutes. Valid values: 1 to 10080. If you leave this parameter unspecified, the default value 5 is used. |
| AliUid | String | Yes | 123456**** | The Apsara Stack tenant account. |

| IpType | String | Yes | 4 | The type of the IP addresses. Valid values: 4: IPv4 addresses. This is the default value. 6: IPv6 addresses. |
|---|---|---|---|---|
| Note | String | Yes | Add the IP address to the whitelist. | The additional description. |

All Alibaba Cloud API operations must include common request parameters. For more information about common request parameters, see Common parameters. For more information about sample requests, see the "Examples" section of this topic.

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | String | 200 | The status code returned for the request. |
| success | String | true | Indicates whether the request is successful. Valid values: true: The request is successful. false: The request failed. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=AddToWhiteList &SrcIp=183.100.XX.XX &DstIp=120.223.XX.XX &AliUid=123456**** &IpType=4 &Note=Add the IP address to the whitelist. &<Common request parameters>
```

Sample success responses `XML` format

```xml
<code>200</code> <success>true</requestId>
```

`JSON` format `{`

```json
  "code": 200,
  "success": "true"
```

`}`

**Error codes**

For a list of error codes, see Error codes.

#### DelFromBlackList

Removes the source IP address of an attack from the blacklist.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DelFromBlack List | The operation that you want to perform. Set the value to DelFromBlackList. |
| SrcIp | String | Yes | 183.100.XX.X X | The source IP address of an attack. |
| DstIp | String | No | 120.223.XX.X X | The destination IP address of an attack. |
| DstPort | String | No | 8080 | The start of the destination port range of an attack. Valid values: 0 to 65535. If you set this parameter to 0, all ports are specified. |
| DstPortEnd | String | No | 8081 | The end of the destination port range of an attack. Valid values: 0 to 65535. If you set this parameter to 0, all ports are specified. |
| LiveTime | String | No | 5 | The validity period of the blacklist. Unit: minutes. Valid values: 1 to 10080. If you leave this parameter unspecified, the default value 5 is used. |
| Filter | String | No | outbound | The direction of the attack traffic that can be blocked by the blacklist. This parameter is available only for the blacklist. Valid values: inbound: blocks traffic destined for data centers in which Apsara Stack is deployed. This is the default value. outbound: blocks traffic sent from data centers in which Apsara Stack is deployed. |
| AliUid | String | Yes | 123456**** | The Apsara Stack tenant account. |

| IpType | String | No | 4 | The type of the IP addresses. Valid values: 4: IPv4 addresses. This is the default value. 6: IPv6 addresses. |
|---|---|---|---|---|

All Alibaba Cloud API operations must include common request parameters. For more information about common request parameters, see Common parameters. For more information about sample requests, see the "Examples" section of this topic.

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | String | 200 | The status code returned for the request. |
| success | String | true | Indicates whether the request is successful. Valid values: true: The request is successful. false: The request failed. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DelFromBlackList &SrcIp=183.100.XX.XX &DstIp=120.223.XX.XX &AliUid=123456**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<code>200</code> <success>true</requestId>
```

`JSON` format `{`

```json
  "code": 200,
  "success": "true"
```

`}`

**Error codes**

For a list of error codes, see Error codes.

#### DelFromWhiteList

Removes the source IP address of an attack from the whitelist.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DelFromWhit eList | The operation that you want to perform. Set the value to DelFromWhiteList. |
| SrcIp | String | No | 183.100.XX.X X | The source IP address of an attack. |
| DstIp | String | Yes | 120.223.XX.X X | The destination IP address of an attack. |
| DstPort | String | No | 8080 | The start of the destination port range of an attack. Valid values: 0 to 65535. If you set this parameter to 0, all ports are specified. |
| DstPortEnd | String | No | 8081 | The end of the destination port range of an attack. Valid values: 0 to 65535. If you set this parameter to 0, all ports are specified. |
| LiveTime | String | No | 5 | The validity period of the whitelist. Unit: minutes. Valid values: 1 to 10080. If you leave this parameter unspecified, the default value 5 is used. |
| AliUid | String | Yes | 123456**** | The Apsara Stack tenant account. |
| IpType | String | No | 4 | The type of the IP addresses. Valid values: 4: IPv4 addresses. This is the default value. 6: IPv6 addresses. |

All Alibaba Cloud API operations must include common request parameters. For more information about common request parameters, see Common parameters. For more information about sample requests, see the "Examples" section of this topic.

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | String | 200 | The status code returned for the request. |

| success | String | true | Indicates whether the request is successful. Valid values: true: The request is successful. false: The request failed. |
|---|---|---|---|

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DelFromWhiteList &SrcIp=183.100.XX.XX &DstIp=120.223.XX.XX &AliUid=123456**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<code>200</code> <success>true</requestId>
```

`JSON` format `{`

```json
  "code": 200,
  "success": "true"
```

`}`

**Error codes**

For a list of error codes, see Error codes.

#### DescribeBlackList

Queries the details of the blacklist.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeBlack List | The operation that you want to perform. Set the value to DescribeBlackList. |
| SrcIp | String | No | 183.100.XX.X X | The source IP address of an attack. |
| DstIp | String | No | 120.223.XX.X X | The destination IP address of an attack. |

| DstPort | String | No | 8080 | The start of the destination port range of an attack. Valid values: 0 to 65535. If you set this parameter to 0, all ports are specified. |
|---|---|---|---|---|
| StartTime | Number | No | 16309962310 00 | The beginning of the time range when the blacklist is valid. Unit: milliseconds. |
| EndTime | Number | No | 16309964110 00 | The end of the time range when the blacklist expires. Unit: milliseconds. |
| AliUid | String | Yes | 123456**** | The Apsara Stack tenant account. |
| IpType | String | No | 4 | The type of the IP addresses. Valid values: 4: IPv4 addresses. This is the default value. 6: IPv6 addresses. |

All Alibaba Cloud API operations must include common request parameters. For more information about common request parameters, see Common parameters. For more information about sample requests, see the "Examples" section of this topic.

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | String | 200 | The status code returned for the request. |
| success | String | true | Indicates whether the request is successful. Valid values: true: The request is successful. false: The request failed. |
| data | Object |   | The returned data. |
| └DataList | Array |   | The details of the entry returned. |
| └└SrcIp | String | 183.100.XX.XX | The source IP address of an attack. |
| └└DstIp | String | 120.223.XX.XX | The destination IP address of an attack. |
| └└DstPort | Number | 8080 | The start of the destination port range of an attack. |
| └└DstPortEnd | Number | 8081 | The end of the destination port range of an attack. |
| └└LiveTime | String | 5 | The validity period of the blacklist. Default value: 5. Unit: minutes. |

| └└HitTimes | String | 10000 | The number of attacks. |
|---|---|---|---|
| └└Filter | String | inbound | The direction of the attack traffic that can be blocked by the blacklist. Valid values: inbound: blocks traffic destined for data centers in which Apsara Stack is deployed. This is the default value. outbound: blocks traffic sent from data centers in which Apsara Stack is deployed. |
| └└Note | String | Query the details of the blacklist. | The additional description. |
| └└StartTime | String | 1630996231000 | The beginning of the time range when the blacklist is valid. Unit: milliseconds. |
| └└EndTime | String | 1630996411000 | The end of the time range when the blacklist expires. Unit: milliseconds. |
| └└IpType | String | 4 | The type of the IP addresses. Valid values: 4: IPv4 addresses. This is the default value. 6: IPv6 addresses. |
| └Count | Number | 5 | The number of entries returned. |
| └Module | String | dispatch rule _ | The name of the process for this request. Default value: dispatch rule. _ |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeBlackList &AliUid=123456**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<code>200</code> <success>true</success> <data>
    <DataList>
        <SrcIp>183.100.XX.XX</SrcIp>
        <DstIp>120.223.XX.XX</DstIp>
        <DstPort>8080</DstPort>
        <DstPortEnd>8081</DstPortEnd>
        <LiveTime>5</LiveTime>
        <HitTimes>10000</HitTimes>
        <Filter></Filter>
        <Note></Note>
        <StartTime>1630996231000</StartTime>
        <EndTime>1630996411000</EndTime>
        <IpType>4</IpType>
    </DataList>
    <Count>1</Count>
    <Module>dispatch_rule</Module>
</data>
```

`JSON` format `{`

```json
  "code": "200",
  "success": "true",
  "data": {
    "DataList": [
```

`{`

```json
        "SrcIp": "183.100.XX.XX",
        "DstIp": "120.223.XX.XX",
        "DstPort": 8080,
        "DstPortEnd": 8081,
        "LiveTime": "5",
        "HitTimes": "10000",
        "Filter": "",
        "Note": "",
        "StartTime": "1630996231000",
        "EndTime": "1630996411000",
        "IpType": "4"
```

`}` `],`

```json
    "Count": 1,
    "Module": "dispatch_rule"
```

`}` `}`

**Error codes**

For a list of error codes, see Error codes.

#### DescribeWhiteList

Queries the details of the whitelist.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeWhit eList | The operation that you want to perform. Set the value to DescribeWhiteList. |
| SrcIp | String | No | 183.100.XX.X X | The source IP address of an attack. |
| DstIp | String | No | 120.223.XX.X X | The destination IP address of an attack. |
| DstPort | String | No | 8080 | The start of the destination port range of an attack. Valid values: 0 to 65535. If you set this parameter to 0, all ports are specified. |
| StartTime | Number | No | 16309962310 00 | The beginning of the time range when the whitelist is valid. Unit: milliseconds. |
| EndTime | Number | No | 16309964110 00 | The end of the time range when the whitelist is valid. Unit: milliseconds. |
| AliUid | String | Yes | 123456**** | The Apsara Stack tenant account. |
| IpType | String | No | 4 | The type of the IP addresses. Valid values: 4: IPv4 addresses. This is the default value. 6: IPv6 addresses. |

All Alibaba Cloud API operations must include common request parameters. For more information about common request parameters, see Common parameters. For more information about sample requests, see the "Examples" section of this topic.

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | String | 200 | The status code returned for the request. |
| success | String | true | Indicates whether the request is successful. Valid values: true: The request is successful. false: The request failed. |
| data | Object |   | The returned data. |

| └DataList | Array |   | The details of the entry returned. |
|---|---|---|---|
| └└SrcIp | String | 183.100.XX.XX | The source IP address of an attack. |
| └└DstIp | String | 120.223.XX.XX | The destination IP address of an attack. |
| └└DstPort | Number | 8080 | The start of the destination port range of an attack. |
| └└DstPortEnd | Number | 8081 | The end of the destination port range of an attack. |
| └└LiveTime | String | 5 | The validity of the whitelist. Default value: 5. Unit: minutes. |
| └└HitTimes | String | 10000 | The number of attacks. |
| └└Filter | String | inbound | The direction of the traffic that is allowed by the whitelist. Valid values: inbound: allows traffic destined for data centers in which Apsara Stack is deployed. This is the default value. outbound: allows traffic sent from data centers in which Apsara Stack is deployed. |
| └└Note | String | Query the details of the whitelist. | The additional description. |
| └└StartTime | String | 1630996231000 | The beginning of the time range when the whitelist is valid. Unit: milliseconds. |
| └└EndTime | String | 1630996411000 | The end of the time range when the whitelist is valid. Unit: milliseconds. |
| └└IpType | String | 4 | The type of the IP addresses. Valid values: 4: IPv4 addresses 6: IPv6 addresses |
| └Count | Number | 5 | The number of entries returned. |
| └Module | String | dispatch rule _ | The name of the process for this request. Default value: dispatch rule. _ |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeWhiteList &AliUid=123456**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<code>200</code> <success>true</success> <data>
    <DataList>
        <SrcIp>183.100.XX.XX</SrcIp>
        <DstIp>120.223.XX.XX</DstIp>
        <DstPort>8080</DstPort>
        <DstPortEnd>8081</DstPortEnd>
        <LiveTime>5</LiveTime>
        <HitTimes>10000</HitTimes>
        <Filter></Filter>
        <Note></Note>
        <StartTime>1630996231000</StartTime>
        <EndTime>1630996411000</EndTime>
        <IpType>4</IpType>
    </DataList>
    <Count>1</Count>
    <Module>dispatch_rule</Module>
</data>
```

`JSON` format `{`

```json
  "code": "200",
  "success": "true",
  "data": {
    "DataList": [
```

`{`

```json
        "SrcIp": "183.100.XX.XX",
        "DstIp": "120.223.XX.XX",
        "DstPort": 8080,
        "DstPortEnd": 8081,
        "LiveTime": "5",
        "HitTimes": "10000",
        "Filter": "",
        "Note": "",
        "StartTime": "1630996231000",
        "EndTime": "1630996411000",
        "IpType": "4"
```

`}` `],`

```json
    "Count": 1,
    "Module": "dispatch_rule"
```

`}` `}`

**Error codes**

For a list of error codes, see Error codes. rameters

## API common parameters

**Common request parameters**

Include common request parameters in every API call. Table 1. Common request parameters

| Name | Type | Requi red | Description |
|---|---|---|---|
| Format | Strin g | No | The format of the return value. Only JSON is supported. |
| Version | Strin g | Yes | The API version number, in YYYY-MM-DD format. Valid values: Auditprivate: 2018-01-16. yundunnextsoc: 2019-07-23. Sas: 2018-12-03. aegis: 2016-11-11. yundun-css: 2021-10-11. secspy: 2019-08-05. Ddosprivate: 2018-01-16. hsm-private: 2018-06-30. Cloudfw: 2017-12-07. Sddp: 2019-01-03. semawaf: 2020-07-01. soar: 2018-12-03. |
| AccessKeyId | Strin g | Yes | The ID of the AccessKey used to access the service. |
| AccessKeySe cret | Strin g | Yes | The secret of the AccessKey used to access the service. |
| RegionId | Strin g | Yes | The ID of the region where the service is deployed. |
| Product | Strin g | Yes | The name of the product that corresponds to the API. Valid values: Auditprivate: Alibaba Cloud Security basic component. yundunnextsoc: Security Center (SOC). Sas: Threat Detection Service. aegis: Server Guard. yundun-css: Container Security. secspy: Network Traffic Detection and Response. Ddosprivate: DDoS traffic scrubbing. hsm-private: Cloud Hardware Security Module (HSM). Cloudfw: Cloud Firewall. Sddp: Sensitive Data Discovery and Protection. semawaf: Web Application Firewall. soar: Security Center (SOC) - Orchestration Response. |

rameters

| EndpointPre | Strin g | Yes | The domain name prefix that corresponds to the API. Valid values: auditprivate: Alibaba Cloud Security basic component. yundunnextsoc-pop: Security Center (SOC). tds: Threat Detection Service. aegis: Server Guard. yundun-css: Container Security. secspy-share: Network Traffic Detection and Response. ddosprivate: DDoS traffic scrubbing. hsmprivate: Cloud Hardware Security Module (HSM). cloudfw: Cloud Firewall. sddp-api: Sensitive Data Discovery and Protection. semawaf: Web Application Firewall. soar: Security Center (SOC) - Orchestration Response. |
|---|---|---|---|

**Common response parameters**

API responses use a standard format. The HTTP status code indicates the result of the call: A 2xx HTTP status code indicates that the call was successful. A 4xx or 5xx HTTP status code indicates that the call failed. Successful calls return data in JSON format. A unique RequestId is returned for every API call, regardless of the outcome.

## Error codes

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
