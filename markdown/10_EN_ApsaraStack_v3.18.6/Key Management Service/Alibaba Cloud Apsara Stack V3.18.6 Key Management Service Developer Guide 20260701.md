---
title: "Key Management Service Developer Guide 20260701"
product_version: "V3.18.6"
pdf_pages: 127
source_pdf: "6a2db6ff626c4c86_Alibaba Cloud Apsara Stack V3.18.6 Key Management Service Developer Guide 20260701.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/v3.18.6%E7%89%88%E6%9C%AC%E6%96%87%E6%A1%A3/%E5%AF%86%E9%92%A5%E7%AE%A1%E7%90%86%E6%9C%8D%E5%8A%A1/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.6%20Key%20Management%20Service%20Developer%20Guide%2020260701.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings)
---

# Key Management Service Developer Guide 20260701

## Table of Contents

- 1 Preparations
  - 1.1 Log on to the API Tool console
  - 1.2 Obtain API information
  - 1.3 Obtain an AccessKey pair
  - 1.4 Obtain access credentials assigned by STS
  - 1.5 Obtain the values of common header parameters
  - 1.6 Obtain KMS SDKs
- 2 Call example of KMS SDK for Java
  - 2.1 Use SDK
    - 2.1.1 Install KMS SDK for Java
    - 2.1.2 Configure authentication credentials
    - 2.1.3 Configure connection requests
    - 2.1.4 Call KMS SDK for Java
    - 2.1.5 Error handling
    - 2.1.6 Use CommonRequest to call API operations
- 3 Call example of KMS SDK for Python
  - 3.1 Use SDK
    - 3.1.1 Install KMS SDK for Python
    - 3.1.2 Configure authentication credentials
    - 3.1.3 Set HTTPS requests
    - 3.1.4 Call KMS SDK for Python
    - 3.1.5 Error handling
    - 3.1.6 Use CommonRequest to call API operations
- 4 Call example of KMS SDK for Go
  - 4.1 Use SDK
    - 4.1.1 Install Go SDK
    - 4.1.2 Configure authentication credentials
    - 4.1.3 Call KMS SDK for Go
    - 4.1.4 Error handling
    - 4.1.5 Use CommonRequest to call API operations
- 5 API reference
  - 5.1 KMS API reference
    - 5.1.1 Make API requests
      - 5.1.1.1 Request syntax
      - 5.1.1.2 Common parameters
      - 5.1.1.3 Signature method
      - 5.1.1.4 Responses
    - 5.1.2 List of operations by function
      - 5.1.2.1 Tag
        - 5.1.2.1.1 TagResource
        - 5.1.2.1.2 ListResourceTags
        - 5.1.2.1.3 UntagResource
      - 5.1.2.2 Keys
        - 5.1.2.2.1 GenerateAndExportDataKey
        - 5.1.2.2.2 ExportDataKey
        - 5.1.2.2.3 CreateKey
        - 5.1.2.2.4 GetParametersForImport
        - 5.1.2.2.5 ImportKeyMaterial
        - 5.1.2.2.6 EnableKey
        - 5.1.2.2.7 DisableKey
        - 5.1.2.2.8 ScheduleKeyDeletion
        - 5.1.2.2.9 DeleteKeyMaterial
        - 5.1.2.2.10 DescribeKey
        - 5.1.2.2.11 UpdateKeyDescription
        - 5.1.2.2.12 ListKeys
        - 5.1.2.2.13 CancelKeyDeletion
        - 5.1.2.2.14 ReEncrypt
        - 5.1.2.2.15 Encrypt
        - 5.1.2.2.16 GenerateDataKey
        - 5.1.2.2.17 GenerateDataKeyWithoutPlaintext
        - 5.1.2.2.18 Decrypt
        - 5.1.2.2.19 CreateAlias
        - 5.1.2.2.20 UpdateAlias
        - 5.1.2.2.21 DeleteAlias
        - 5.1.2.2.22 ListAliases
        - 5.1.2.2.23 ListAliasesByKeyId
        - 5.1.2.2.24 DescribeRegions
        - 5.1.2.2.25 CreateKeyVersion
        - 5.1.2.2.26 DescribeKeyVersion
        - 5.1.2.2.27 ListKeyVersions
        - 5.1.2.2.28 UpdateRotationPolicy
        - 5.1.2.2.29 AsymmetricDecrypt
        - 5.1.2.2.30 AsymmetricEncrypt
        - 5.1.2.2.31 AsymmetricSign
        - 5.1.2.2.32 AsymmetricVerify
        - 5.1.2.2.33 GetPublicKey
- 6 Appendixes
  - 6.1 STS overview
    - 6.1.1 What is STS?
    - 6.1.2 AssumeRole

## 1 Preparations

### 1.1 Log on to the API Tool console

You can log on to the API Tool console from the Apsara Uni-manager Management Console.

**Prerequisites**

Before you log on to the Apsara Uni-manager Management Console, the endpoint of the console is obtained from the deployment personnel. A browser is available. We recommend that you use Google Chrome.

**Procedure**

1. Enter the URL of the Apsara Uni-manager Management Console in the address bar and
press Enter.
2. Enter your username and password.
Obtain the username and password that are used to log on to the Apsara Uni-manager Management Console from the operations administrator. When you log on to the Apsara Uni-manager Management Console for the first time, you must change the password of your account. For security purposes, your password must meet the minimum complexity requirements. The password must be 10 to 32 characters in length and must contain at least two of the following character types: Uppercase or lowercase letters Digits Special characters, which include ! @ # $ %
3. Click **Log On**.
4. If your account has multi-factor authentication (MFA) enabled, perform corresponding
operations in the following scenarios: You log on to the Apsara Uni-manager Management Console for the first time after MFA is enabled by the administrator. a. On the Bind Virtual MFA Device page, bind an MFA device. b. Enter the username and password again as in Step 2 and click **Log On**. c. Enter a six-digit MFA verification code and click **Authenticate**. You have enabled MFA and bound an MFA device. Enter a six-digit MFA verification code and click **Authenticate**. For more information, see the **Bind a virtual MFA device to enable MFA** topic in
**Apsara Uni-manager Management Console User Guide** .
5. In the top navigation bar, choose **Products > Others > API Tool**.

### 1.2 Obtain API information

To call API operations by using an SDK, you must obtain information that includes service names, API operation names, and API versions.

**Background information**

The API operations on the API Directory page are for reference only. For information about how to call API operations, see the developer guide of the corresponding cloud service. If the information on the API Directory page is different from that in the developer guide of a cloud service, the information in the developer guide prevails.

**Procedure**

1. Log on to the API Tool console.
2. In the left-side navigation pane, click .
3. On the **API Directory** page, select the required service from the drop-down list and enter
the keyword of an API operation name to search for the API operation.
4. View and record the service name, API operation name, and API version.

### 1.3 Obtain an AccessKey pair

An AccessKey pair that consists of an AccessKey ID and an AccessKey secret is used to implement symmetric encryption and verify the identity of a request sender. The AccessKey ID is used to identify a user. The AccessKey secret is used to encrypt the signature string. This topic describes how to obtain an AccessKey pair.

**Prerequisites**

Only operations administrators and level-1 organization administrators can obtain AccessKey pairs for organizations.

**Obtain the AccessKey pair of an organization**

To obtain the AccessKey pair of an organization, perform the following steps:
1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, click **Enterprise**.
3. In the left-side navigation pane of the **Enterprise** page, click **Organizations**.
4. In the organization navigation tree, click the
icon next to an organization name.
5. Select **AccessKey** from the drop-down list.
6. In the message that appears, obtain the AccessKey pair of the organization.
An AccessKey pair is automatically allocated to a level-1 organization. Subordinate organizations use the same AccessKey pair as their level-1 organization.

**Obtain the AccessKey pair of a personal account**

To obtain the AccessKey pair of a personal account, perform the following steps:
1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the upper-right corner of the homepage, move the pointer over the profile picture and
click User Information.
3. In the AccessKey Pair section, view your AccessKey pair.
The AccessKey pair provides full access to cloud resources within your Apsara Stack tenant account. You must keep the AccessKey pair confidential.

### 1.4 Obtain access credentials assigned by STS

**assigned by STS**

This topic describes how to use Security Token Service (STS) to call API operations in Apsara Stack.

**Background information**

Apsara Stack STS allows you to manage temporary access credentials for your Apsara Stack resources. You can use STS to call API operations in Apsara Stack. To call API operations in Apsara Stack by using STS, you must obtain an AccessKey ID, an AccessKey secret, and a security token assigned by STS. For more information about STS, see the "STS overview" topic in Common Content - Developer Guide.

**Procedure**

1. Obtain the Alibaba Cloud Resource Name (ARN) of your `RAM role` .
i. Log on to the Apsara Uni-manager Management Console. ii. Click the profile picture in the upper-right corner of the page and select **User**
**Information**.
iii. Click **View Current Role Policy**. In the **View Policies of Current Role** dialog box, view the ARN of your `RAM role` .
2. Obtain the access credential assigned by STS.
You must replace the variables in the following code with actual values. Delete the angle brackets (<>) before you submit the code. Variables: <yourRegionID>: Replace this variable with your region ID. <yourAccessKeyID>: Replace this variable with your AccessKey ID. <yourAccessKeySecret>: Replace this variable with your AccessKey secret. <yourRoleSessionName>: Replace this variable with the name of the current session. <yourRoleArn>: Replace this variable with the ARN of your RAM role. "sts.aliyuns.com": Replace this variable with the endpoint of STS.

```java
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
    // Obtain the access credential assigned by STS.
    String stsAK = credentials.getString("AccessKeyId");
    String stsSK = credentials.getString("AccessKeySecret");
    String stsToken = credentials.getString("SecurityToken");
private static String callAssumeRole(IAcsClient client) {
    CommonRequest request = new CommonRequest();
    // Replace "sts.aliyuns.com" with the endpoint of STS. Format: sts-
vpc.${global:region}.${global:internet-domain}.
    request.setSysDomain("sts.aliyuns.com");
    request.setSysProduct("Sts");
    request.setSysAction("AssumeRole");
    request.setSysVersion("2015-04-01");
    request.setSysMethod(MethodType.POST);
    request.setHttpContentType(FormatType.FORM);
    // Replace <yourRoleSessionName> with the name of the current session.
    request.putQueryParameter("RoleSessionName", "<yourRoleSessionName>");
    // Replace <yourRoleArn> with the actual ARN that you obtained in the preceding s
tep for the RAM role.
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

3. Use the access credential assigned by STS to call an API operation of a cloud service. The
following sample code provides an example on how to use the access credential assigned by STS to call the `DescribeZones` operation of Elastic Compute Service (ECS). Replace the sample code based on your cloud service. You must replace the variables in the following code with actual values. Delete the angle brackets (<>) before you submit the code. Variables: <yourRegionID>: Replace this variable with your region ID. <yourStsAccesskeyID>: Replace this variable with your AccessKey ID. <yourStsAccessKeySecret>: Replace this variable with your AccessKey secret. <yourStsToken>. Replace this variable with your security token. <yourResourceGroupID>: Replace this variable with your resource set ID. <yourRegionID>: Replace this variable with your organization ID.

```java
public static void main(String[] args) {
    // Replace <yourRegionID> with your region ID.
    // Replace <yourStsAccessKeyID> and <yourStsAccessKeySecret> with the AccessKey I
D and AccessKey secret assigned by STS.
    DefaultProfile profile = DefaultProfile.getProfile("<yourRegionID>", "
<yourStsAccesskey>", "<yourStsAccessSecret>");
    HttpClientConfig clientConfig = HttpClientConfig.getDefault();
    clientConfig.setIgnoreSSLCerts(true);
    clientConfig.setProtocolType(ProtocolType.HTTPS);
    profile.setHttpClientConfig(clientConfig);
    IAcsClient client = new DefaultAcsClient(profile);
    CommonRequest request = new CommonRequest();
    request.setSysDomain("ecs.aliyuns.com");
    request.setSysProduct("ECS");
    request.setSysAction("DescribeZones");
    request.setSysVersion("2014-05-26");
    request.setSysMethod(MethodType.POST);
    request.setHttpContentType(FormatType.FORM);
    // Replace <yourRegionID> with your region ID.
    request.putHeadParameter("x-acs-regionid", "<yourRegionID>");
    // Replace <yourStsToken> with the security token assigned by STS.
    request.putQueryParameter("SecurityToken", "<yourStsToken>");
    // Optional. Replace <yourResourceGroupID> with your resource set ID.
    // request.putHeadParameter("x-acs-resourcegroupid", "<yourResourceGroupID>");
    // Required. Replace <yourOrganizationID> with your organization ID.
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

### 1.5 Obtain the values of common header parameters

**header parameters**

You must provide multiple header parameters when you call API operations in Apsara Stack. This topic describes how to obtain the values of common header parameters. This topic also explains the response parameters that are returned after you call API operations.

**Obtain a region ID**

1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, click **Enterprise**.
3. In the left-side navigation pane, choose **Resources** > **Regions**.
4. Click the name of the desired organization.
5. In the **Regions** section, view the region ID.

**Obtain an organization ID**

You can call the GetOrganizationList operation to obtain the organization ID. For more information, see GetOrganizationList in Apsara Uni-manager Management Console Developer Guide.

**Obtain a resource set ID**

You can call the ListResourceGroup operation to obtain the resource set ID. For more information, see ListResourceGroup in Apsara Uni-manager Management Console Developer Guide.

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
| ResourceGroupName | The name of a resource set. |
| ResourceGroup | The ID of a resource set. |
| DepartmentName | The name of an organization. |

| Department | The ID of an organization. |
|---|---|

### 1.6 Obtain KMS SDKs

When you call API operations in Apsara Stack by using POP gateways, you must use the SDKs of Key Management Service (KMS). This topic describes how to obtain KMS SDKs.

| Alibaba Cloud SDK | KMS SDK |
|---|---|
| Alibaba Cloud SDK for Java | Alibaba Cloud KMS SDK for Java |
| Alibaba Cloud SDK for Python | Alibaba Cloud KMS SDK for Python |
| Alibaba Cloud SDK for Go | Alibaba Cloud KMS SDK for Go |

DK for Java

## 2 Call example of KMS SDK for Java

**for Java**

### 2.1 Use SDK

#### 2.1.1 Install KMS SDK for Java

Before you install KMS SDK for Java, you must obtain KMS SDK for Java and add Maven dependencies.

**Step 1: Obtain KMS SDK for Java**

Apsara Stack SDK for Java supports Java Development Kit (JDK) 1.8 or later. To use KMS SDK for Java, you must install core library 4.5.17 or later for Apsara Stack SDK for Java and KMS SDK for Java 2.15.0 or later. Visit SDK Center to obtain desired KMS SDK for Java.

**Step 2: Add Maven dependencies**

When you install KMS SDK for Java, you must add the following dependencies to the pom.xml file:

```xml
<!-- Alibaba Cloud SDK for Java --> <dependency>
    <groupId>com.aliyun</groupId>
    <artifactId>aliyun-java-sdk-core</artifactId>
    <version>4.5.17</version>
</dependency> <!-- KMS SDK for Java --> <dependency>
    <groupId>com.aliyun</groupId>
    <artifactId>aliyun-java-sdk-kms</artifactId>
    <version>2.15.0</version>
</dependency>
```

#### 2.1.2 Configure authentication credentials

When you use Apsara Stack SDKs to access Apsara Stack services, you must provide an authorized account for authentication. This topic describes how to configure authentication credentials. Key Management Service (KMS) SDK for Java allows you to complete the authentication process by using an AccessKey pair. For more information, see **Obtain an AccessKey pair**. If you want to use your AccessKey pair to access KMS, you must configure the AccessKey pair as an access credential when you create a client. DK for Java

**Warning**

Do not disclose the code that contains your AccessKey pair. For example, do not commit the code to publicly-accessible GitHub projects. Otherwise, your Apsara Stack tenant account may be compromised.

```
DefaultProfile profile = DefaultProfile.getProfile(
    "<yourRegionID>",         // Replace this variable with the actual region ID.
    "<yourAccessKeyID>",      // Replace this variable with your AccessKey ID.
    "<yourAccessKeySecret>"); // Replace this variable with your AccessKey secret.
```

In the preceding sample code, replace the variables with the actual information. Delete the angle brackets (<>) in the final code.

#### 2.1.3 Configure connection requests

This topic describes how to configure a connection request by using the HttpClientConfig object. You can use the following code to configure the HttpClientConfig object. We recommend that you select and configure the following parameters based on your business requirements. You must use actual values to replace the variables in the following sample code. Do not retain the angle brackets (<>) in the final code. The following list describes the variables: <readTimeout>: Specify the read timeout period based on your business requirements. Unit: milliseconds. <connectionTimeout>: Specify the connection timeout period based on your business requirements. Unit: milliseconds. <maxRequestsPerHost>: Specify the maximum number of requests that are supported by each server based on your business requirements. The supported data type is INTEGER. <maxRequests>: Specify the maximum number of requests based on your business requirements. The supported data type is INTEGER. <http://192.168.XX.XX:33XX>: Replace it with the actual IP address and port of the proxy. DK for Java

```
// Obtain the HttpClientConfig object. HttpClientConfig clientConfig = HttpClientConfig.getDefault(); // Specify whether to ignore certificates. clientConfig.setIgnoreSSLCerts(true); // (Optional) Specify the read timeout period. Unit: milliseconds. clientConfig.setReadTimeoutMillis(<readTimeout>); // (Optional) Specify the connection timeout period. Unit: milliseconds. clientConfig.setConnectionTimeoutMillis(<connectionTimeout>); // (Optional) Specify the maximum number of requests that are supported by each server. The supported data type is INTEGER. clientConfig.setMaxRequestsPerHost(<maxRequestsPerHost>); // (Optional) Specify the maximum number of requests. The supported data type is INTEGE
```

`R.`

```
clientConfig.setMaxRequests(<maxRequests>); // (Optional) Specify the protocol type. clientConfig.setProtocolType(ProtocolType.HTTP); /** (Optional) Specify whether to configure the proxy based on your business requirements. The following code is available: clientConfig.setHttpProxy("<http://192.168.XX.XX:33XX>");
```

`Or`

```
clientConfig.setHttpsProxy("<https://192.168.XX.XX:33XX>"); Replace https://192.168.XX.XX:33XX with the actual IP address and port of the proxy.
```

`*/`

```
profile.setHttpClientConfig(clientConfig);
```

#### 2.1.4 Call KMS SDK for Java

This topic describes how to call KMS SDK for Java.

**Procedure**

1. Create an AcsClient instance.

```
IAcsClient client = new DefaultAcsClient(profile);
```

2. Create a request.
The request name must be in the ${apiName}Request format, where **${apiName}** indicates the name of the API operation. Example: Encrypt. When multiple KMS SDKs for Java are used, different requests may have the same name. Differentiate these requests by using package names.

```
EncryptRequest request = new EncryptRequest(); // The service-related parameters. request.setKeyId("alias/Example"); request.setPlaintext("Hello world"); // The header parameters that are used for resource isolation. Replace the variables with the actual organization ID and resource set ID. request.putHeadParameter("x-acs-organizationid", "1"); request.putHeadParameter("x-acs-resourcegroupid", "11");
```

3. Initiate the request and handle exceptions.
DK for Java

```java
EncryptResponse response; try {
    response = client.getAcsResponse(request);
    System.out.println(new Gson().toJson(response));
} catch (ServerException e) {
    e.printStackTrace();
} catch (ClientException e) {
    e.printStackTrace();
```

In most cases, all response fields are deserialized into the response. You can call `response.getXXX()` to obtain the values of the response fields.

```
ciphertextBlob = response.getCiphertextBlob();
```

If an exception occurs or you need to obtain the original HTTP response, call `doAction()` to obtain the original response.

```
HttpResponse response = client.doAction(request);
```

#### 2.1.5 Error handling

When you use KMS SDK for Java, errors may occur. If an error occurs on the server, the SDK returns a `ServerException` error response. If an error occurs on a client instance, the SDK returns a `ClientException` error response. An error response is composed of an error code and an error message. In most cases, you do not need to handle client errors. You need to only handle server errors. If you want to handle client errors, you can refer to the following sample code:

```java
try {
    FooResponse response = client.getAcsResponse(request);
    // Handle the response.
}catch (ServerException e){
    // Specify your error handling logic.
    // For example, you can display the details of the error.
    System.out.println("ErrorCode=" + e.getErrCode());
    System.out.println("ErrorMessage=" + e.getErrMsg());
    // If the error is tricky, you can submit a ticket and provide the request ID.
    System.out.println("ResponseId=" + e.getRequestId());
}catch (ClientException e){
    // Specify your error handling logic.
    // For example, you can display the details of the error.
    System.out.println("ErrorCode=" + e.getErrCode());
    System.out.println("ErrorMessage=" + e.getErrMsg());
```

#### 2.1.6 Use CommonRequest to call API operations

**operations**

DK for Java If you want to call the API operations of an Apsara Stack service that does not provide SDKs, or the requests and responses of the API operations that you call by using an SDK do not meet your business requirements, you can use CommonRequest to call the API operations. You can use CommonRequest to call all API operations. The following code provides an example on how to call the Encrypt operation of Key Management Service (KMS) to encrypt plaintext into ciphertext. In the following sample code, you should replace the variables with actual values and delete the angle brackets (<>) from the code. Variables: <yourRegionID>: Replace this variable with the actual region ID. <yourAccessKeyID>: Replace this variable with your AccessKey ID. <yourAccessKeySecret>: Replace this variable with your AccessKey secret. <yourSecurityToken>: Replace this variable with your security token. <yourResourceGroupID>: Replace this variable with the actual resource set ID. <yourOrganizationID>: Replace this variable with the actual organization ID. <http://192.168.XX.XX:33XX>: Replace this variable with the actual proxy IP address and port number. <endpoint>: Replace this variable with the actual endpoint. <alias/Example>: Replace this variable with the actual alias or ID of the Customer Master Key (CMK).

```java
import com.aliyuncs.CommonRequest; import com.aliyuncs.CommonResponse; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.exceptions.ServerException; import com.aliyuncs.http.HttpClientConfig; import com.aliyuncs.http.ProtocolType; import com.aliyuncs.profile.DefaultProfile; public class Sample {
    public static void main(String[] args) {
        // Create and initialize a DefaultAcsClient instance.
        DefaultProfile profile = DefaultProfile.getProfile(
                "<yourRegionUD>",          // Replace this variable with the actual regi
on ID.
                "<yourAccessKeyID>",      // Replace this variable with your AccessKey I
```

`D.`

```
                "<yourAccessKeySecret>")  // Replace this variable with your AccessKey s
ecret.
        HttpClientConfig clientConfig = HttpClientConfig.getDefault();
        clientConfig.setIgnoreSSLCerts(true);// Disable certificate verification.
        clientConfig.setProtocolType(ProtocolType.HTTPS);
        /**
         Configure an HTTP or HTTPS proxy based on your business requirements. Replace
the variable with the actual proxy IP address and port number.
         Format:
```

DK for Java `*/`

```
        clientConfig.setHttpsProxy("<http://192.168.XX.XX:33XX>");
        profile.setHttpClientConfig(clientConfig);
        IAcsClient client = new DefaultAcsClient(profile);
        // Create an API request and specify parameters.
        CommonRequest request = new CommonRequest();
        // Replace <endpoint> with the actual endpoint.
        request.setSysDomain("<endpoint>");
        request.setSysLocationProduct("Kms");
        request.setSysVersion("2016-01-20");
        request.setSysAction("Encrypt");
        request.putQueryParameter("KeyId", "<alias/Example>");
        request.putQueryParameter("Plaintext", "Hello world");
        request.putHeadParameter("x-acs-resourcegroupid", "<yourResourceGroupID>");// O
ptional. Replace this variable with the actual resource set ID.
        request.putHeadParameter("x-acs-organizationid", "<yourOrganizationID>");// Req
uired. Replace this variable with the actual organization ID.
        request.putHeadParameter("x-acs-caller-sdk-source","ApiTestDemo");// Required.
Specify the source of the API call.
        request.putHeadParameter("x-acs-regionid", "<yourRegionID>");// Optional.
Replace this variable with the actual region ID.
        /**
         When you use an access credential assigned by STS to call an API operation, yo
u must add the SecurityToken field in request parameters.
         Format:
         request.putQueryParameter("SecurityToken", "<yourSecurityToken>");
         Replace <yourSecurityToken> with your security token.
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

DK for Python

## 3 Call example of KMS SDK for Python

**for Python**

### 3.1 Use SDK

#### 3.1.1 Install KMS SDK for Python

This topic describes how to install KMS SDK for Python. Apsara Stack SDK for Python supports Python 2.6.x, 2.7.x, 3.x, and later. You can use pip to install Apsara Stack SDK for Python.
1. Install the core library of Apsara Stack SDK for Python.
If you use Python 2.x, run the following command:

```
pip install aliyun-python-sdk-core
```

If you use Python 3.x, run the following command:

```
pip3 install aliyun-python-sdk-core-v3
```

2. Install KMS SDK for Python.
If you use Python 2.x, run the following command:

```
pip install aliyun-python-sdk-kms
```

If you use Python 3.x, run the following command:

```
pip3 install aliyun-python-sdk-kms
```

#### 3.1.2 Configure authentication credentials

When you use Apsara Stack SDKs to access Apsara Stack services, you must provide an authorized account for authentication. This topic describes how to configure authentication credentials. Key Management Service (KMS) SDK for Python supports authentication based on an AccessKey pair. For more information, see **Obtain an AccessKey pair**. If you want to use your AccessKey pair to access KMS, you must configure the AccessKey pair as an access credential when you create a client.

**Warning**

Do not disclose the code that contains your AccessKey pair. For example, do not commit the code to publicly-accessible GitHub projects. Otherwise, your Apsara Stack tenant account may be compromised.

```python
from aliyunsdkcore import client clt = client.AcsClient(secret_id, secret_key, region_id)
```

#### 3.1.3 Set HTTPS requests

DK for Python The Python SDK supports using HTTP and HTTPS to initiate API requests. When using the Python SDK, you can specify a protocol (HTTP or HTTPS) for a specific request to use, or set a global default protocol for all requests to use. The default protocol (HTTP or HTTPS) of a product takes precedence over the global default protocol you set.

**Add OpenSSL dependency**

HTTPS of the Python SDK depends on the OpenSSL support in Python. To use Alibaba Cloud SDK to send HTTPS requests, you must add OpenSSL support in Python.

| python -c "import ssl" |   | command to chec |
|---|---|---|
| L. If the |   |   |

OpenSSL is supported in Python. If Python does not support OpenSSL, run the following command to install OpenSSL:

```
pip install pyopenssl
```

**Set HTTP/HTTPS for a request**

See the following code example for reference to set the HTTPS call for an API:

```bash
request = CreateInstanceRequest.CreateInstanceRequest() request.set_protocol_type("https")
# Value: "https" or "http"
```

**Set global default protocol for all requests**

See the following code example for reference to set the global default protocol for all requests:

```java
import aliyunsdkcore.request aliyunsdkcore.request.set_default_protocol_type("https")
# Create a request and call client.do_action_with_exception() to send the request.
```

#### 3.1.4 Call KMS SDK for Python

This topic describes how to call KMS SDK for Python.

**Procedure**

1. Import KMS SDK for Python.

```python
from aliyunsdkcore import client from aliyunsdkcore.profile import region_provider from aliyunsdkkms.request.v20160120 import EncryptRequest
```

2. Create an AcsClient instance.

```
client.region_provider.modify_point(product_name, region_id, endpoint) clt = client.AcsClient(access_key, access_secret, region_id) clt.set_verify(False)
```

3. Create a request.
DK for Python

```
request = EncryptRequest.EncryptRequest() request.set_accept_format('json') request.set_KeyId('<alias/Example>') request.set_Plaintext('Hello world')
```

4. Initiate the request and handle the response.

```
response = clt.do_action_with_exception(request) print response
```

#### 3.1.5 Error handling

When you use KMS SDK for Python, errors may occur. If an error occurs on the server, the SDK returns a `ServerException` error response. If an error occurs on a client instance, the SDK returns a `ClientException` error response. An error response is composed of an error code and an error message. In most cases, you do not need to handle client errors. You need to only handle server errors. If you want to handle client errors, you can refer to the following sample code:

```bash
#coding=utf-8
try:
    response = client.do_action_with_exception(request)
except ServerException as e:
    # Specify your error handling logic.
    # For example, you can display the details of the error.
    print e.get_http_status()
    print e.get_error_code()
    print e.get_error_msg()
```

#### 3.1.6 Use CommonRequest to call API operations

**operations**

If you want to call the API operations of an Apsara Stack service that does not provide SDKs, or the requests and responses of the API operations that you call by using an SDK do not meet your business requirements, you can use CommonRequest to call the API operations. You can use CommonRequest to call all API operations. The following code provides an example on how to call the Encrypt operation of Key Management Service (KMS) to encrypt plaintext into ciphertext. DK for Python In the following sample code, replace the variables with actual values. Delete the angle brackets (<>) from the code. Variables: <yourRegionID>: Replace this variable with the actual region ID. <yourAccessKeyID>: Replace this variable with your AccessKey ID. <yourAccessKeySecret>: Replace this variable with your AccessKey secret. <yourSecurityToken>: Replace this variable with your security token. <yourResourceGroupID>: Replace this variable with the actual resource set ID. <yourOrganizationID>: Replace this variable with the actual organization ID. <http://192.168.XX.XX:33XX>: Replace this variable with the actual proxy IP address and port number. <endpoint>: Replace this variable with the actual endpoint. <alias/Example>: Replace this variable with the actual alias or ID of the customer master key (CMK). DK for Python

```java
#!/usr/bin/env python
# coding=utf-8
import os from aliyunsdkcore.client import AcsClient from aliyunsdkcore.request import CommonRequest
# Specify the AccessKey ID, AccessKey secret, and region ID.
client = AcsClient('{<yourAccessKeyID>}', '{<yourAccessKeySecret>}', '{<yourRegionID>}') client.set_verify(False)
# Specify the IP address and port number of your proxy.
os.environ['HTTPS_PROXY'] = '<http://192.168.XX.XX:33XX>' request = CommonRequest() request.set_product('Kms') request.set_action_name('Encrypt') request.set_version('2016-01-20') request.set_domain('<endpoint>') # Specify the endpoint.
# or:
# request = = CommonRequest(product='Kms', action_name='Encrypt',version='2016-01-20',d
omain='<endpoint>')
######
# Specify the HTTPS protocol.
# request.set_protocol_type('https')
######
request.set_accept_format('json') request.set_method('POST')
# Required. Specify the service name.
request.add_query_param('Product', 'Kms')
# Replace <alias/Example> with the actual CMK alias or CMK ID.
request.add_query_param('KeyId', '<alias/Example>') request.add_query_param('Plaintext', 'Hello world')
######
# If you use an access credential assigned by Security Token Service (STS) to call an A
PI operation, you must add the SecurityToken field in request parameters.
# Format:
# request.add_query_param("SecurityToken", "<yourSecurityToken>");
# Replace <yourSecurityToken> with your security token.
######
# Optional. Specify the resource set ID.
request.add_header("x-acs-resourcegroupid", "<yourResourceGroupID>")
# Required. Specify the organization ID.
request.add_header("x-acs-organizationid", "<yourOrganizationID>")
# Required. Specify the source of the API call.
request.add_header("x-acs-caller-sdk-source", "ApiTestDemo")
# Optional. Specify the region ID.
request.add_header("x-acs-regionid", "<yourRegionID>") response = client.do_action_with_exception(request) print(str(response, encoding='utf-8'))
```

DK for Go

## 4 Call example of KMS SDK for Go

**for Go**

### 4.1 Use SDK

#### 4.1.1 Install Go SDK

This topic describes how to install the Go SDK. The Alibaba Cloud Go SDK supports Go 1.7 or later versions. Install the Go SDK manually.
1. Download the source code of the Go SDK from the official site of Apsara Stack.
2. Extract the package to the directory where the GO_PATH file of the current user resides.

#### 4.1.2 Configure authentication credentials

When you use Apsara Stack SDKs to access Apsara Stack services, you must provide an Apsara Stack tenant account for authentication. Key Management Service (KMS) SDK for Go supports authentication by using an AccessKey pair. For more information, see **Obtain an AccessKey pair**. If you want to use your AccessKey pair to access KMS, you must configure the AccessKey pair as an access credential when you initialize a client instance.

**Warning**

Do not disclose the code that contains your AccessKey pair. For example, do not commit the code to publicly-accessible GitHub projects. Otherwise, your Apsara Stack tenant account may be compromised.

```
// Initialize a client instance. kmsClient, err := kms.NewClientWithAccessKey(
        "<yourRegionID>",                 // Replace this variable with the actual regio
n ID.
        "<yourAccessKeyID>",             // Replace this variable with your AccessKey ID
```

`.`

```
        "<yourAccessKeySecret>")        // Replace this variable with your AccessKey
secret.
```

In the preceding sample code, replace the variables with the actual information. Delete the angle brackets (<>) in the final code.

#### 4.1.3 Call KMS SDK for Go

This topic describes how to call KMS SDK for Go.

**Procedure**

DK for Go
1. Import KMS SDK for Go.

```java
import github.com/aliyun/alibaba-cloud-sdk-go/services/kms
```

2. Create a client instance that contains all the API operations of Key Management Service
(KMS). You must replace the variables in the following code with the actual values. Delete the angle brackets (<>) before you submit the code.

```
kmsClient,err := kms.NewClientWithAccessKey(
    "<yourRegionID>",  // Replace this variable with your region ID.
    "<yourAccessKeyID>",  // Replace this variable with your AccessKey ID.
    "<yourAccessKeySecret>")  // Replace this variable with your AccessKey secret.
kmsClient.Domain = "<endpoint>" // Replace this variable with the Endpoint. kmsClient.SetHTTPSInsecure(true) // Disable certificate verification.
```

3. Use `kms.CreateEncryptRequest` to create a request.
You can replace Encrypt with the name of another API operation.

```
request := kms.CreateEncryptRequest() request.KeyId = ""
```

4. Initiate the request.

```
response, err := kmsClient.Encrypt(request)
```

#### 4.1.4 Error handling

|   |   |   | ClientError |
|---|---|---|---|
| ServerError |   | respo |   |
| ded in |   |   |   |

interface and can be handled in a similar manner as standard Go errors.

**Overview**

You can use the following code to handle errors:

```
response,err := kmsClient.Encrypt(request) if err != nil {
    // Obtain the error response.
   err.Error()
```

**ClientError**

When you send a request, if an error occurs on the client instance and cannot be automatically handled, the SDK returns a ClientError error response. DK for Go The following sample code provides an example on how to obtain and determine the error

| message in the | ClientError | error response: |
|---|---|---|
| response, err := kmsClient.Encrypt(request) if clientError, ok := err.(*errors.ClientError); ok{ // Obtain the error code. clientError.ErrorCode() // Obtain the error message. clientError.Message() // Obtain the original error. clientError.OriginError() } |   |   |

**Important**

When you use a specific error struct, you must add the error package `github.com/aliyun/alibaba-cloud-sdk-go/sdk/errors` by using the following code:

```java
package main import (
    "github.com/aliyun/alibaba-cloud-sdk-go/services/kms"
    "github.com/aliyun/alibaba-cloud-sdk-go/sdk/requests"
    // Add an error package.
    "github.com/aliyun/alibaba-cloud-sdk-go/sdk/errors"
    "fmt"
```

`)`

**ServerError**

When the server returns an error message, the SDK wraps the message into the ServerError error response and returns it to the client. In this case, you can still obtain the original HTTP response from the error response. The following sample code provides an example on how to obtain and determine the error

| message in the | ServerError | error response: |
|---|---|---|
| response, err := kmsClient.Encrypt(request) if serverError, ok := err.(*errors.ServerError); ok{ // Obtain the error code. serverError.ErrorCode() // Obtain the error message. serverError.Message() // Obtain the original HTTP response. response.GetOriginHttpResponse() } |   |   |

DK for Go When you use a specific error struct, you must add the error package `github.com/aliyun/alibaba-cloud-sdk-go/sdk/errors` by using the following code:

```java
package main import (
    "github.com/aliyun/alibaba-cloud-sdk-go/services/kms"
    "github.com/aliyun/alibaba-cloud-sdk-go/sdk/requests"
    // Add an error package.
    "github.com/aliyun/alibaba-cloud-sdk-go/sdk/errors"
    "fmt"
```

`)`

#### 4.1.5 Use CommonRequest to call API operations

**operations**

If you want to call the API operations of an Apsara Stack service that does not provide SDKs, or the requests and responses of the API operations that you call by using an SDK do not meet your business requirements, you can use CommonRequest to call the API operations. You can use CommonRequest to call all API operations. The following code provides an example on how to call the Encrypt operation of Key Management Service (KMS) to encrypt plaintext into ciphertext. You must replace the variables in the code with actual values. Delete the angle brackets (<>) before you submit the code. Variables: <yourRegionID>: Replace this variable with the actual region ID. <yourAccessKeyID>: Replace this variable with your AccessKey ID. <yourAccessKeySecret>: Replace this variable with your AccessKey secret. <yourSecurityToken>: Replace this variable with your security token. <yourResourceGroupID>: Replace this variable with the actual resource set ID. <yourOrganizationID>: Replace this variable with the actual organization ID. <http://192.168.XX.XX:33XX>: Replace this variable with the actual proxy IP address and port number. <endpoint>: Replace this variable with the endpoint. <alias/Example>: Replace this variable with the actual alias or ID of the customer master key (CMK). `k` `i` DK for Go

```java
package main import (
    "fmt"
    "github.com/aliyun/alibaba-cloud-sdk-go/sdk"
    "github.com/aliyun/alibaba-cloud-sdk-go/sdk/requests"
```

`)`

```
func main() {
    client, err := sdk.NewClientWithAccessKey(
        "<yourRegionID>",        // Replace this variable with the actual region ID.
        "<yourAccessKeyID>",     // Replace this variable with your AccessKey ID.
        "<yourAccessKeySecret>") // Replace this variable with your AccessKey secret.
    if err != nil {
        panic(err)
    client.SetHTTPSInsecure(true) // Disable certificate verification.
    client.SetHttpsProxy("<http://192.168.XX.XX:33XX>") // Replace this variable with t
he actual proxy IP address and port number.
    request := requests.NewCommonRequest()
    request.Method = "POST"
    request.Scheme = "HTTPS"
    request.Domain = "<endpoint>" // Replace this variable with the endpoint.
    request.Version = "2016-01-20"
    // Specify the name of the API operation. This parameter is required because the op
eration is to be called by using the Remote Procedure Call (RPC) style.
    request.ApiName = "Encrypt"
    // Required. Specify the service name.
    request.QueryParams["Product"] = "Kms"
    // Specify service-related parameters.
    request.QueryParams["KeyId"] = "<alias/Example>" // Replace this variable with the
actual CMK alias or CMK ID.
    request.QueryParams["Plaintext"] = "Hello world"
```

`/*`

```
       When you use an access credential assigned by Security Token Service (STS) to ca
ll an RPC API operation, you must add the SecurityToken field to the request parameters
```

`.`

```
       Format:
       request.QueryParams["SecurityToken"]="<yourSecurityToken>"
       Replace <yourSecurityToken> with your security token.
```

`*/`

```
    request.Headers["x-acs-caller-sdk-source"] = "ApiTestDemo"         // Required.
Specify the source of the call.
    request.Headers["x-acs-regionid"] = "<yourRegionID>"               // Optional. Spec
ify the region ID.
    request.Headers["x-acs-resourcegroupid"] = "<yourResourceGroupID>" // Optional. Spe
cify the resource set ID.
    request.Headers["x-acs-organizationid"] = "<yourOrganizationID>"   // Required. Spe
cify the organization ID.
    response, err := client.ProcessCommonRequest(request)
    if err != nil {
        panic(err)
    fmt.Print(response.GetHttpContentString())
```

DK for Go

## 5 API reference

### 5.1 KMS API reference

#### 5.1.1 Make API requests

##### 5.1.1.1 Request syntax

This topic describes the endpoint, communication protocols, HTTPS request methods, and request parameters of the Key Management Service (KMS) API.

**Endpoint**

The endpoint of the KMS API is kms.example.com.

**Communication protocols**

You must call KMS API operations by sending Transport Layer Security (TLS)-encrypted HTTPS requests. KMS does not support SSL 2.0 or SSL 3.0. KMS supports only TLS 1.0 and later.

**Request methods**

You can call KMS API operations by sending HTTPS POST or GET requests. The request parameters must be included in the request URL.

**Request parameters**

Each request must specify the operation to be performed. For example, to create a customer master key (CMK), you must set the Action parameter to `CreateKey` . Request parameters include both common parameters and API operation-specific parameters.

**Character encoding**

All requests and responses are UTF-8 encoded.

##### 5.1.1.2 Common parameters

Common request parameters must be included in all KMS API requests.

**Common request parameters**

Common request parameters must be included in all KMS API requests.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Format | String | No | The format in which to return the response. Valid values: JSON and XML. Default value: JSON. |

| Version | String | Yes | The version number of the API. The format is YYYY-MM-DD. The current version is 2016-01-20. |
|---|---|---|---|
| AccessKeyId | String | Yes | The AccessKey ID provided to you by Apsara Stack. |
| Signature | String | Yes | The signature string of the current request. For more information about how signatures are calculated, see Signature method. |
| SignatureMethod | String | Yes | The encryption method of the signature string. Set the value to HMAC- SHA1. |
| Timestamp | String | Yes | The timestamp of the request. Specify the time in the ISO 8601 standard in the YYYY- MM-DDThh:mm:ssZ format. The time must be in UTC. For example, 2015-12- 01T12:00:00Z indicates 20:00:00 on December 1, 2015 (UTC+8). |
| SignatureVersion | String | Yes | The version of the signature encryption algorithm. Set the value to 1.0. |

Examples

```
https://kms.cn-hangzhou.example.com/? Format=json &Version=2016-01-20 &AccessKeyId=testid &Signature=YlrFhyqDZQ1ThNYARrv3Ptaxqf**** &SignatureMethod=HMAC-SHA1 &Timestamp=2016-03-25T09:36:58Z &SignatureVersion=1.0
```

**Common response parameters**

API responses use the HTTP response format. Responses can be returned in either the JSON or XML format. You can specify the response format in the request. The default response format is JSON. Every response returns a unique **RequestId** regardless of whether the call is successful. An HTTP `2xx` status code indicates a successful call. An HTTP `4xx` or `5xx` status code indicates a failed call. Sample responses: XML format

```xml
<?xml version="1.0" encoding="utf-8"?>
    <!--Result root node-->
    <KMS>
        <!--Return request tag-->
        <RequestId>4C467B38-3910-447D-87BC-AC049166F216</RequestId>
        <!--Return result data-->
    </KMS>
```

JSON format `{`

```json
    "RequestId":"4C467B38-3910-447D-87BC-AC049166F216"
    /*Return result data*/
```

##### 5.1.1.3 Signature method

You must sign all API requests to ensure security. Alibaba Cloud uses the request signature to verify the identity of the API caller. If you use HTTPS to send an API request, you must include the signature in the request.

**Signature overview**

You must add the signature to Key Management Service (KMS) API requests in the following format:

```
https://Endpoint/?SignatureVersion=1.0&SignatureMethod=HMAC- SHA1&Signature=CT9X0VtwR86fNWSnsc6v8YGOjuE%3D&
```

A signature contains the following parameters:
**SignatureMethod**: the encryption method of the signature string. Set the value to HMAC-
SHA1.
**SignatureVersion**: the version of the signature encryption algorithm. Set the value to 1.0.
**Signature**: the signature string generated after the request is symmetrically encrypted by
using the AccessKey secret. The HMAC-SHA1 algorithm specified in RFC 2104 is used for encryption. The AccessKey secret is used to calculate the hash-based message authentication code (HMAC) value of the encoded and sorted query string, and the HMAC value is used as the signature string. Request signatures include operation-specific parameters. Therefore, the signature of a request varies based on the request parameters. To calculate a signature, perform the steps in this topic.

```
Signature = Base64( HMAC-SHA1( AccessKey Secret, UTF-8-Encoding-Of(StringToSign)) )
```

**Step 1: Compose and encode a string-to-sign**

1. Create a canonicalized query string by arranging the request parameters.
i. Arrange the request parameters (including all common and operation-specific parameters except Signature) in alphabetical order. When you use the GET method to submit a request, these parameters constitute the parameter field of the request URL. These parameters are placed after the question mark (?) in the request URI and connected by ampersands (&). ii. Encode the names and values of the arranged request parameters in the request URL by using the UTF-8 character set. The following table describes the encoding rules.

| Character | Encoding rule |
|---|---|
| Uppercase letters, lowercase letters, digits, hyphens (-), underscores ( ), periods (.), _ and tildes (~) | These characters do not need to be encoded. |
| Other characters | These characters must be percent encoded in the %XY format. XY represents the ASCII code of the characters in hexadecimal notation. For example, double quotation marks (") are encoded as %22 . |
| Extended UTF-8 characters | These characters must be encoded in the %XY%ZA… format. |
| Spaces | Spaces must be encoded as %20 . Do not encode spaces as plus signs (+). This encoding method is different from the Multipurpose Internet Mail Extensions (MIME) encoding algorithm application/x-www-form-urlencoded , such as the java.net.URLEncoder class that is provided by the Java standard library. However, you can apply the MIME encoding algorithm and then replace the plus sign (+) in the encoded string with %20 , the asterisk (*) with %2A , and %7E with the tilde (~). You can use the following percentEncode method to implement the algorithm: private static final String ENCODING = "UTF-8"; private static String percentEncode(String value) throws UnsupportedEncodingException { return value != null ? URLEncoder.encode(value, ENCODING).replace("+", "%20").replace("*", "%2A").replace("%7E", "~") : null; } |

iii. Connect the encoded parameter names and values by using equal signs (=). iv. Sort the connected parameter name and value pairs in the specified order and connect the pairs by using ampersands (&) to obtain the canonicalized query string.
2. Create a string-to-sign from the encoded canonicalized query string in the following way:

```
StringToSign=
      HTTPMethod + "&" +
      percentEncode("/") + "&" +
      percentEncode(CanonicalizedQueryString)
```

The following list describes the parameters:
**HTTPMethod**: specifies the HTTP method used to submit a request, such as GET.
**percentEncode("/")**: specifies the encoded value (%2F) of a forward slash (/). The
encoding follows the URL encoding rules.
**percentEncode(CanonicalizedQueryString)**: specifies the encoded canonicalized
query string based on the URL encoding rules.

**Step 2: Calculate the signature string**

1. Calculate the HMAC value of the string-to-sign based on RFC 2104.
Use the SHA1 algorithm to calculate the HMAC value of the string-to-sign. The combination of your AccessKey secret and an ampersand (&) (ASCII code 38) is used as the key for the HMAC calculation.
2. Encode the HMAC value in Base64 to obtain the signature string.
3. Add the signature string to the request as the **Signature** parameter.
When the obtained signature value is submitted as the final request parameter value, the value must be URL-encoded like other parameters based on rules defined in RFC 3986.

**Examples**

The CreateKey operation is used as an example to introduce the signature method. Request URL before the request is signed:

```
https://kms.cn-hangzhou.aliyuncs.com/?Action=CreateKey &SignatureVersion=1.0 &Format=json &Version=2016-01-20 &AccessKeyId=testid &SignatureMethod=HMAC-SHA1 &Timestamp=2016-03-28T03:13:08Z
```

`StringToSign` for the request URL:

```
GET&%2F&AccessKeyId%3Dtestid%26Action%3DCreateKey%26Format%3Djson%26SignatureMethod%3DHMA SHA1%26SignatureVersion%3D1.0%26Timestamp%3D2016-03- 28T03%253A13%253A08Z%26Version%3D2016-01-20
```

If the AccessKey ID is testid and the AccessKey secret is testsecret, the key that is used to calculate the HMAC value of the string-to-sign is testsecret&. The signature value is `******************************` . Request URL after the request is signed:

```
https://kms.cn-hangzhou.aliyuncs.com/?Action=CreateKey &SignatureVersion=1.0 &Format=json &Version=2016-01-20 &AccessKeyId=testid &SignatureMethod=HMAC-SHA1 &Timestamp=2016-03-28T03:13:08Z &Signature=41wk2SSX1GJh7fwnc5eqOfiJPF****
```

##### 5.1.1.4 Responses

API responses use the HTTP response format where a 2xx status code indicates a successful call and a 4xx or 5xx status code indicates a failed call. Sample responses in API Reference are formatted in a way that is easier for you to read. The actual responses are not formatted with line breaks or indentation.

**Sample success responses**

`XML` format

```xml
<?xml version="1.0" encoding="UTF-8"?> <!--Result root node--> <Operation name + Response>
    <!--Return request tag-->
    <RequestId>4C467B38-3910-447D-87BC-AC049166F216</RequestId>
    <!--Return result data-->
</Operation name + Response>
```

`JSON` format `{`

```json
    "RequestId": "4C467B38-3910-447D-87BC-AC049166F216",
    /* Return result data */
```

**Sample error responses**

If an error occurs when you call an API operation, no result data is returned. You can troubleshoot the error based on the error code returned and common error codes. If an error occurs when you call an API operation, the HTTP status code, error code, error message, and ID of the request are returned in the response. If you cannot troubleshoot the error based on the error code and error message, you can provide Alibaba Cloud technical support with the ID of the request to locate the request log. The following sample responses indicate the error that occurs when the required timestamp is not provided. `XML` format

```xml
<KMS>
     <HttpStatus>400</HttpStatus>
     <Code>IllegalTimestamp</Code>
     <Message>The input parameter "Timestamp" that is mandatory for processing this req
uest is not supplied.</Message>
     <RequestId>3b237773-bc2c-4bea-95fc-319a1a5baa68</RequestId>
</KMS>
```

`JSON` format `{`

```json
     "HttpStatus": 400,
     "Code": "IllegalTimestamp",
     "Message": "The input parameter \"Timestamp\" that is mandatory for processing thi
s request is not supplied.",
     "RequestId": "e85db688-a2d3-44ca-9790-4259f59e90d8"
```

**Common error codes**

| Error code | Error message | HTTP status code |
|---|---|---|
| InternalFailure | Internal Failure | 500 |
| SerivceUnavailableTemporary | Service Unavailable Temporary | 503 |
| InvalidAccessKeyId.NotFound | The AccessKey ID provided does not exist in our records. | 404 |
| Forbidden.KeyNotFound | The specified Key is not found. | 404 |
| Forbidden.AliasNotFound | The specified Alias is not found. | 404 |
| Forbidden.NoPermission | This operation is forbidden by permission system. | 403 |
| Forbidden.AccessKey | This AccessKey is not enabled. | 403 |
| UnsupportedHTTPMethod | This http method is not supported. | 403 |
| Forbidden.UbsmsInvalidUserid | Userid Invalid For Ubsms | 403 |
| Forbidden.UbsmsInvalidBid | Your account partner does not have KMS Service | 403 |
| Forbidden.KmsServiceNotEnabl ed | Kms service is not Enabled for current user. Please get access permission first | 403 |
| Forbidden.ProhibitedByRiskCont rol | Current user is Prohibited By Risk Control | 403 |
| Forbidden.InDebtOverdue | Current user is indebted Overdue | 403 |
| Forbidden.InDebt | Current user is indebted | 403 |
| ParseRequestParameterExcepti on | Server parse parameters exception. Please check your input params. | 400 |
| MissingParameter | The parameter "< parameter name >" is needed but not provided. | 400 |

| InvalidParameter | The specified parameter "< parameter name >" is not valid. | 400 |
|---|---|---|
| IncompleteSignature | The request signature does not conform to Alibaba Cloud standards. | 400 |
| IllegalTimestamp | The input parameter "Timestamp" that is required for processing this request is not supplied. | 400 |
| Rejected.LimitExceeded | The request was rejected because user create resource limit was exceeded | 400 |
| AliasAlreadyExists | AliasName Already Exists | 400 |
| InvalidKeyMaterial | key material is invalid | 400 |
| InvalidImportToken | import token is invalid | 400 |
| ExpiredImportToken | import token is expired | 400 |
| Unsupported.Origin | This key origin is not valid for this api | 400 |
| Unsupported.Alias | Alias is not valid for this api | 400 |
| Rejected.StateModifiedFailed | Keystate modified failed | 409 |
| Rejected.Disabled | The request was rejected because the key state is Disabled | 409 |
| Rejetced.PendingDeletion | The request was rejected because the key state is PendingDeletion | 409 |
| Rejected.PendingImport | The request was rejected because the key state is PendingImport | 409 |

#### 5.1.2 List of operations by function

##### 5.1.2.1 Tag

###### 5.1.2.1.1 TagResource

Adds tags to a customer master key (CMK). A CMK can have more than one tag. Each tag consists of a key and a value. You can add up to 10 tags for a CMK. Request format: `KeyId="string"&Tags=[{ "TagKey": "string","TagValue": "string"} ]`

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | TagResource | The operation that you want to perform. Set the value to TagResource. |
| Tags | String | Yes | [{\"TagKey\":\"S 1key1\",\"TagVal ue\":\"S1val1\"}, {\"TagKey\":\"S1 key2\",\"TagValu e\":\"S2val2\"}] | One or more tags. Separate multiple tags with commas (,). Each tag consists of the following attributes: TagKey: the key of the tag TagValue: the value of the tag |
| KeyId | String | Yes | 08c33a6f-4e0a- 4a1b-a3fa- 7ddf**** | The ID of the CMK. The ID must be globally unique. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 4162a6af-bc99- 40b3-a552- 89dcc8aaf7c8 | The ID of the request. |

**Examples**

Sample requests

```
https://kms.cn-hangzhou.aliyuncs.com/?Action=TagResource &KeyId=08c33a6f-4e0a-4a1b-a3fa-7ddf**** &Tags=[{\"TagKey\":\"S1key1\",\"TagValue\":\"S1val1\"}, {\"TagKey\":\"S1key2\",\"TagValue\":\"S2val2\"}] &<Common request parameters>
```

Sample success responses `XML` format

```xml
<KMS>
    <RequestId>4162a6af-bc99-40b3-a552-89dcc8aaf7c8</RequestId>
</KMS>
```

`JSON` format `{`

```json
    "RequestId": "4162a6af-bc99-40b3-a552-89dcc8aaf7c8"
```

**Error codes**

For a list of error codes, visit the Common error codes.

###### 5.1.2.1.2 ListResourceTags

Queries the tags of a customer master key (CMK). Request format: KeyId="string"

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ListResourceTag s | The operation that you want to perform. Set the value to ListResourceTags. |
| KeyId | String | Yes | 1234abcd-12ab- 34cd-56ef- 12345678**** | The ID of the CMK. The ID must be globally unique. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 4162a6af-bc99- 40b3-a552- 89dcc8aaf7c8 | The ID of the request. |
| Tags | Array | [{"KeyId": "33caea95-c3e5- 4b3e-a9c6- cec76e4e****","Ta gKey": "Project","TagValu e": "Test" }] | An array that consists of the tags of the CMK. |
| KeyId | String | 33caea95-c3e5- 4b3e-a9c6- cec76e4e**** | The ID of the CMK. The ID must be globally unique. |
| TagKey | String | Project | The key of the tag. |
| TagValue | String | Test | The value of the tag. |

**Examples**

Sample requests

```
https://kms.cn-hangzhou.aliyuncs.com/?Action=ListResourceTags &KeyId=1234abcd-12ab-34cd-56ef-12345678**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<KMS>
          <RequestId>0f900dad-c747-4170-9962-1bfb6b31436b</RequestId>
          <Tags>
                <Tag>
                      <KeyId>33caea95-c3e5-4b3e-a9c6-cec76e4e****</KeyId>
                      <TagKey>Project</TagKey>
                      <TagValue>Test</TagValue>
                </Tag>
          </Tags>
</KMS>
```

`JSON` format `{`

```json
    "RequestId": "4162a6af-bc99-40b3-a552-89dcc8aaf7c8",
    "Tags": {
            "Tag": [
```

`{`

```json
                    "KeyId": "33caea95-c3e5-4b3e-a9c6-cec76e4e****",
                    "TagKey": "Project",
                    "TagValue": "Test"
```

`]`

**Error codes**

| HttpCod e | Error code | Error message | Description |
|---|---|---|---|
| 400 | Throttling | Request was denied due to request throttling. | The error message returned because your traffic in this period has exceeded the limit. If your business requirements are not met, submit a ticket. |

For a list of error codes, visit the Common error codes.

###### 5.1.2.1.3 UntagResource

Deletes the specified tags of a customer master key (CMK). Request format: `KeyId="string"&TagKeys=["tagkey1","tagkey2"]`

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | UntagResource | The operation that you want to perform. Set the value to UntagResource. |
| TagKeys | String | Yes | ["key1"] | One or more tag keys. Multiple tag keys are separated by commas (,). Each tag key must be 1 to 128 bytes in length. Note You need only to specify the tag key and do not need to specify the tag value. |
| KeyId | String | Yes | 08c33a6f-4e0a- 4a1b-a3fa- 7ddf**** | The ID of the CMK. The ID must be globally unique. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 4162a6af-bc99- 40b3-a552- 89dcc8aaf7c8 | The ID of the request. |

**Examples**

Sample requests

```
https://kms.cn-hangzhou.aliyuncs.com/?Action=UntagResource &TagKeys=["key1"] &KeyId=08c33a6f-4e0a-4a1b-a3fa-7ddf**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<KMS>
    <RequestId>4162a6af-bc99-40b3-a552-89dcc8aaf7c8</RequestId>
</KMS>
```

`JSON` format `{`

```json
    "RequestId": "4162a6af-bc99-40b3-a552-89dcc8aaf7c8"
```

**Error codes**

For a list of error codes, visit the Common error codes.

##### 5.1.2.2 Keys

###### 5.1.2.2.1 GenerateAndExportDataKey

Generates a data key and uses a public key and a customer master key (CMK) to protect the data key.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | GenerateAndEx portDataKey | The operation that you want to perform. Set the value to GenerateAndExportDataKey. |
| KeyId | String | No | 1234abcd-12ab- 34cd-56ef- 12345678**** | The ID of the CMK. The ID must be globally unique. |
| KeySpec | String | No | AES 256 _ | The length of the data key that you want to generate. Valid values: AES 256: a 256-bit symmetric key _ AES 128: a 128-bit symmetric key _ Note We recommend that you use the KeySpec or NumberOfBytes parameter to specify the length of a data key. If none of the parameters are specified, KMS generates a 256- bit data key. If both of them are specified, KMS ignores the KeySpec parameter. |

|   | KeySpec |
|---|---|
| NumberOfBytes |   |

| PublicKeyBlob | String | Yes | MIIBIjANBgkqhki G9w0BAQEFAAO CAQ8AMIIBCgKC AQEAs5Yu9AEgA TN2/e3nUz1K\nE y6ng8MSPutcse 2/VECG/NUF9C6 D4IsJ64ShzY3dc n34WYzTOe916 eMJFxyrNrSw\nH tc4UOR5AvaoRrf pgu2uq+i70/ZXr WL+pGb1hgZV8 cWheIHMxwrR3Ii QlM5qN7EF\n9B dyWtyBfUGsp0B n1VqlPc5G0x0a 9xU2z9YtP994y DenNVIoIQ6Cov 1lIEuwXAb2\n7b oC41ePXwD0JWt 41sP+rgCmpjBx 00puIG+IlnoReE gI1ZGYmK98Gg A/XzmNjZiD\nyv XJZAcM33Ue85 +PkR5iHTtSEbi4 QAoqpJabprUzz3 Fin2j1dRrcacxG b7p31A9c\nJQID AQAB | The public key of an external application. It is used to protect the data key. It must be specified in the DER format and Base64 encoded. |
|---|---|---|---|---|
| WrappingKeyS pec | String | No | EC SM2 _ | The type of the public key. Valid values: RSA 2048 _ EC SM2 _ |
| WrappingAlgor ithm | String | Yes | SM2PKE | The encryption algorithm of the public key. Valid values: RSAES PKCS1 V1 5 _ _ _ RSAES OAEP SHA 1 _ _ _ RSAES OAEP SHA 256 _ _ _ SM2PKE |
| NumberOfByte s | Integer | No | 32 | The length of the data key that you want to generate. Valid values: 1 to 1024. Unit: bytes. |
| EncryptionCon text | Json | No | {"Example":"Ex ample"} | The JSON string that consists of key- value pairs. If you specify this parameter, an equivalent value is required when you call the Decrypt operation. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| KeyId | String | 1234abcd-12ab- 34cd-56ef- 12345678**** | The ID of the CMK. The ID must be globally unique. |
| KeyVersionId | String | 2ab1a983-7072- 4bbc-a582- 584b5bd8**** | The ID of the CMK version. The ID must be globally unique. |
| ExportedData Key | String | BQKP+1zK6+ZEMx TP5qaVzcsgXtWplY BKm0NXdSnB5Fzli FxE1bSiu4dnEIlca2J peH7yz1/S6fed630 H+hIH6DoM25fTLN cKj+mFB0Xnh9m2 +HN59Mn4qyTfcU eadnfCXSWcGBouh XFwcdd2rJ3n337bz Tf4jm659gZu3L0i6 PLuxM9p7mqdwO0 cKJPfGVfhnfMz+f4a lMg79WB/NNyE2ly X7/qxvV49ObNrrJb KSFiz8Djocaf0IESN LMbfYI5bXjWkJlX92 DQbKhibtQW8ZOJ// ZC6t0AWcUoKL6Q Dm/dg5koQalcleRi npB+QadFm894sL bVZ9+N4GVsv1Wb jwg== | The data key that is protected by using the public key. |
| CiphertextBlob | String | ODZhOWVmZDktM 2QxNi00ODk0LWJk NGYtMWZjNDNmM 2YyYWJmS7FmDBB Q0BkKsQrtRnidtPwi rmDcS0ZuJCU41xx AAWk4Z8qsADfbV0 b+i6kQmlvj79dJdG OvtX69Uycs901qOj op4bTSl0oQ | The ciphertext data key that is encrypted by using the primary CMK version. |
| RequestId | String | 7021b6ec-4be7- 4d3c-8a68- 1e85d4d515a0 | The ID of the request. |

**Examples**

Sample requests

```
https://kms.cn-hangzhou.aliyuncs.com/?Action=GenerateAndExportDataKey &KeyId=1234abcd-12ab-34cd-56ef-12345678**** &PublicKeyBlob=MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAs5Yu9AEgATN2/e3nUz1K\nEy6ng8MS tcse2/VECG/NUF9C6D4IsJ64ShzY3dcn34WYzTOe916eMJFxyrNrSw\nHtc4UOR5AvaoRrfpgu2uq+i70/ZXrWL+p 1hgZV8cWheIHMxwrR3IiQlM5qN7EF\n9BdyWtyBfUGsp0Bn1VqlPc5G0x0a9xU2z9YtP994yDenNVIoIQ6Cov1lIE XAb2\n7boC41ePXwD0JWt41sP+rgCmpjBx00puIG+IlnoReEgI1ZGYmK98GgA/XzmNjZiD\nyvXJZAcM33Ue85+Pk iHTtSEbi4QAoqpJabprUzz3Fin2j1dRrcacxGb7p31A9c\nJQIDAQAB &WrappingAlgorithm=SM2PKE &WrappingKeySpec=EC_SM2 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<KMS> <CiphertextBlob>ODZhOWVmZDktM2QxNi00ODk0LWJkNGYtMWZjNDNmM2YyYWJmS7FmDBBQ0BkKsQrtRnidtPwir cS0ZuJCU41xxAAWk4Z8qsADfbV0b+i6kQmlvj79dJdGOvtX69Uycs901qOjop4bTSl0oQ</CiphertextBlob>
    <KeyId>1234abcd-12ab-34cd-56ef-12345678****</KeyId>
    <KeyVersionId>2ab1a983-7072-4bbc-a582-584b5bd8****</KeyVersionId>
<ExportedDataKey>BQKP+1zK6+ZEMxTP5qaVzcsgXtWplYBKm0NXdSnB5FzliFxE1bSiu4dnEIlca2JpeH7yz1/S ed630H+hIH6DoM25fTLNcKj+mFB0Xnh9m2+HN59Mn4qyTfcUeadnfCXSWcGBouhXFwcdd2rJ3n337bzTf4jm659gZ L0i6PLuxM9p7mqdwO0cKJPfGVfhnfMz+f4alMg79WB/NNyE2lyX7/qxvV49ObNrrJbKSFiz8Djocaf0IESNLMbfYI XjWkJlX92DQbKhibtQW8ZOJ//ZC6t0AWcUoKL6QDm/dg5koQalcleRinpB+QadFm894sLbVZ9+N4GVsv1Wbjwg== </ExportedDataKey>
    <RequestId>7021b6ec-4be7-4d3c-8a68-1e85d4d515a0</RequestId>
</KMS>
```

`JSON` format `{`

```json
    "CiphertextBlob":
"ODZhOWVmZDktM2QxNi00ODk0LWJkNGYtMWZjNDNmM2YyYWJmS7FmDBBQ0BkKsQrtRnidtPwirmDcS0ZuJCU41xxA k4Z8qsADfbV0b+i6kQmlvj79dJdGOvtX69Uycs901qOjop4bTSl0oQ",
    "KeyId": "1234abcd-12ab-34cd-56ef-12345678****",
    "KeyVersionId": "2ab1a983-7072-4bbc-a582-584b5bd8****",
    "ExportedDataKey":
"BQKP+1zK6+ZEMxTP5qaVzcsgXtWplYBKm0NXdSnB5FzliFxE1bSiu4dnEIlca2JpeH7yz1/S6fed630H+hIH6DoM fTLNcKj+mFB0Xnh9m2+HN59Mn4qyTfcUeadnfCXSWcGBouhXFwcdd2rJ3n337bzTf4jm659gZu3L0i6PLuxM9p7mq O0cKJPfGVfhnfMz+f4alMg79WB/NNyE2lyX7/qxvV49ObNrrJbKSFiz8Djocaf0IESNLMbfYI5bXjWkJlX92DQbKh tQW8ZOJ//ZC6t0AWcUoKL6QDm/dg5koQalcleRinpB+QadFm894sLbVZ9+N4GVsv1Wbjwg==",
    "RequestId": "7021b6ec-4be7-4d3c-8a68-1e85d4d515a0"
```

**Error codes**

For a list of error codes, visit the Common error codes.

###### 5.1.2.2.2 ExportDataKey

Decrypts the ciphertext specified by CiphertextBlob and uses a public key to protect the output.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ExportDataKey | The operation that you want to perform. Set the value to ExportDataKey. |
| CiphertextBlob | String | Yes | ODZhOWVmZDk tM2QxNi00ODk0 LWJkNGYtMWZj NDNmM2YyYWJ mS7FmDBBQ0B kKsQrtRnidtPwir mDcS0ZuJCU41 xxAAWk4Z8qsA DfbV0b+i6kQml vj79dJdGOvtX69 Uycs901qOjop4 bTSl0oQ | The ciphertext of the data key that is encrypted by using the primary CMK version. |
| EncryptionCon text | Json | No | {"Example":"Ex ample"} | The JSON string that consists of key- value pairs. If you specify this parameter when you call an operation to generate the data key, an equivalent value is required. |
| PublicKeyBlob | String | Yes | MIIBIjANBgkqhki G9w0BAQEFAAO CAQ8AMIIBCgKC AQEAs5Yu9AEgA TN2/e3nUz1K\nE y6ng8MSPutcse 2/VECG/NUF9C6 D4IsJ64ShzY3dc n34WYzTOe916 eMJFxyrNrSw\nH tc4UOR5AvaoRrf pgu2uq+i70/ZXr WL+pGb1hgZV8 cWheIHMxwrR3Ii QlM5qN7EF\n9B dyWtyBfUGsp0B n1VqlPc5G0x0a 9xU2z9YtP994y DenNVIoIQ6Cov 1lIEuwXAb2\n7b oC41ePXwD0JWt 41sP+rgCmpjBx 00puIG+IlnoReE gI1ZGYmK98Gg A/XzmNjZiD\nyv XJZAcM33Ue85 +PkR5iHTtSEbi4 QAoqpJabprUzz3 Fin2j1dRrcacxG b7p31A9c\nJQID AQAB | The public key of an external application. It is used to protect the data key. It must be specified in the DER format and Base64 encoded. |

| WrappingKeyS pec | String | No | EC SM2 _ | The type of the public key. Valid values: RSA 2048 _ EC SM2 _ |
|---|---|---|---|---|
| WrappingAlgor ithm | String | Yes | SM2PKE | The encryption algorithm of the public key. Valid values: RSAES PKCS1 V1 5 _ _ _ RSAES OAEP SHA 1 _ _ _ RSAES OAEP SHA 256 _ _ _ SM2PKE |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| KeyId | String | 1234abcd-12ab- 34cd-56ef- 12345678**** | The ID of the CMK. The ID must be globally unique. |
| KeyVersionId | String | 2ab1a983-7072- 4bbc-a582- 584b5bd8**** | The ID of the CMK version. The ID must be globally unique. |
| ExportedData Key | String | BQKP+1zK6+ZEMx TP5qaVzcsgXtWplY BKm0NXdSnB5Fzli FxE1bSiu4dnEIlca2J peH7yz1/S6fed630 H+hIH6DoM25fTLN cKj+mFB0Xnh9m2 +HN59Mn4qyTfcU eadnfCXSWcGBouh XFwcdd2rJ3n337bz Tf4jm659gZu3L0i6 PLuxM9p7mqdwO0 cKJPfGVfhnfMz+f4a lMg79WB/NNyE2ly X7/qxvV49ObNrrJb KSFiz8Djocaf0IESN LMbfYI5bXjWkJlX92 DQbKhibtQW8ZOJ// ZC6t0AWcUoKL6Q Dm/dg5koQalcleRi npB+QadFm894sL bVZ9+N4GVsv1Wb jwg== | The data key that is protected by using the public key. |
| RequestId | String | 7021b6ec-4be7- 4d3c-8a68- 1e85d4d515a0 | The ID of the request. |

**Examples**

Sample requests

```
https://kms.cn-hangzhou.aliyuncs.com/?Action=ExportDataKey &CiphertextBlob=ODZhOWVmZDktM2QxNi00ODk0LWJkNGYtMWZjNDNmM2YyYWJmS7FmDBBQ0BkKsQrtRnidtPwir cS0ZuJCU41xxAAWk4Z8qsADfbV0b+i6kQmlvj79dJdGOvtX69Uycs901qOjop4bTSl0oQ &PublicKeyBlob=MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAs5Yu9AEgATN2/e3nUz1K\nEy6ng8MS tcse2/VECG/NUF9C6D4IsJ64ShzY3dcn34WYzTOe916eMJFxyrNrSw\nHtc4UOR5AvaoRrfpgu2uq+i70/ZXrWL+p 1hgZV8cWheIHMxwrR3IiQlM5qN7EF\n9BdyWtyBfUGsp0Bn1VqlPc5G0x0a9xU2z9YtP994yDenNVIoIQ6Cov1lIE XAb2\n7boC41ePXwD0JWt41sP+rgCmpjBx00puIG+IlnoReEgI1ZGYmK98GgA/XzmNjZiD\nyvXJZAcM33Ue85+Pk iHTtSEbi4QAoqpJabprUzz3Fin2j1dRrcacxGb7p31A9c\nJQIDAQAB &WrappingAlgorithm=SM2PKE &WrappingKeySpec=EC_SM2 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<KMS>
          <KeyId>1234abcd-12ab-34cd-56ef-12345678****</KeyId>
          <KeyVersionId>2ab1a983-7072-4bbc-a582-584b5bd8****</KeyVersionId>
<ExportedDataKey>BQKP+1zK6+ZEMxTP5qaVzcsgXtWplYBKm0NXdSnB5FzliFxE1bSiu4dnEIlca2JpeH7yz1/S ed630H+hIH6DoM25fTLNcKj+mFB0Xnh9m2+HN59Mn4qyTfcUeadnfCXSWcGBouhXFwcdd2rJ3n337bzTf4jm659gZ L0i6PLuxM9p7mqdwO0cKJPfGVfhnfMz+f4alMg79WB/NNyE2lyX7/qxvV49ObNrrJbKSFiz8Djocaf0IESNLMbfYI XjWkJlX92DQbKhibtQW8ZOJ//ZC6t0AWcUoKL6QDm/dg5koQalcleRinpB+QadFm894sLbVZ9+N4GVsv1Wbjwg== </ExportedDataKey>
          <RequestId>7021b6ec-4be7-4d3c-8a68-1e85d4d515a0</RequestId>
</KMS>
```

`JSON` format `{`

```json
        "KeyId": "1234abcd-12ab-34cd-56ef-12345678****",
        "KeyVersionId": "2ab1a983-7072-4bbc-a582-584b5bd8****",
        "ExportedDataKey":
"BQKP+1zK6+ZEMxTP5qaVzcsgXtWplYBKm0NXdSnB5FzliFxE1bSiu4dnEIlca2JpeH7yz1/S6fed630H+hIH6DoM fTLNcKj+mFB0Xnh9m2+HN59Mn4qyTfcUeadnfCXSWcGBouhXFwcdd2rJ3n337bzTf4jm659gZu3L0i6PLuxM9p7mq O0cKJPfGVfhnfMz+f4alMg79WB/NNyE2lyX7/qxvV49ObNrrJbKSFiz8Djocaf0IESNLMbfYI5bXjWkJlX92DQbKh tQW8ZOJ//ZC6t0AWcUoKL6QDm/dg5koQalcleRinpB+QadFm894sLbVZ9+N4GVsv1Wbjwg==",
        "RequestId": "7021b6ec-4be7-4d3c-8a68-1e85d4d515a0"
```

**Error codes**

For a list of error codes, visit the Common error codes.

###### 5.1.2.2.3 CreateKey

Creates a customer master key (CMK). A CMK can be symmetric or asymmetric. Symmetric CMKs are used to generate data keys. These data keys are used to encrypt large amounts of data and less than 6 KB of data. Asymmetric CMKs cannot be used to generate data keys. The following table lists the CMK types and operations supported by symmetric and asymmetric CMKs.

| CMK type | KeySpec | Description | Encryption and decryption | Signature and verification |
|---|---|---|---|---|
| Symmetric CMK | Aliyun AES 256 _ _ | AES key with a length of 256 bits | Supported | Not supported |
| Symmetric CMK | Aliyun SM4 _ | SM4 key | Supported | Not supported |
| Asymmetric CMK | RSA 2048 _ | RSA key with a length of 2,048 bits | Supported | Supported |
| Asymmetric CMK | EC P256 _ | NIST- recommended elliptic curve P- 256 (secp256r1) | Not supported | Supported |
| Asymmetric CMK | EC P256K _ | SECC elliptic curve secp256k1 | Not supported | Supported |
| Asymmetric CMK | EC SM2 _ | 256-bit elliptic curves over the prime field that is defined in GB/T 32918 | Supported | Supported |

The KeySpec parameter for a symmetric CMK consists of the standard key type prefixed with `Aliyun_` . The prefix indicates that the CMK uses a standard encryption algorithm. However, the cyphertext that is generated by using the CMK is not standard. An asymmetric CMK generates standard ciphertext or signatures. An RSA CMK supports either the ENCRYPT/DECRYPT or SIGN/VERIFY operation rather than both. SM4 and SM2 are block ciphers used in the Chinese National Standards. KMS supports SM4 and SM2 CMKs created in a Managed HSM that is deployed in a mainland China region.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateKey | The operation that you want to perform. Set the value to CreateKey. |

| Description | String | No | key description example | The description of the CMK. The description can be 0 to 8,192 characters in length. |
|---|---|---|---|---|
| KeySpec | String | No | Aliyun AES 256 _ _ | The type of the CMK. Valid values: Aliyun AES 256 _ _ Aliyun SM4 _ RSA 2048 _ EC P256 _ EC P256K _ EC SM2 _ Default value: Aliyun SM 4: CMKs created in a _ Managed HSM that is deployed in a mainland China region. Aliyun AES 256: other CMKs. _ _ |
| KeyUsage | String | No | ENCRYPT/DECRY PT | The usage of the CMK. Valid values: ENCRYPT/DECRYPT: The CMK encrypts or decrypts data. SIGN/VERIFY: The CMK generates or verifies a digital signature. |
| Origin | String | No | Aliyun KMS _ | The source of key material. Valid values: Aliyun KMS. This is the default _ value. EXTERNAL Note The value of this parameter is case- sensitive. If you set the KeySpec parameter to an asymmetric CMK type, do not set Origin to EXTERNAL. If you set Origin to EXTERNAL, you must import key material. |

| ProtectionLeve l | String | No | SOFTWARE | The protection level of the CMK. Valid values: SOFTWARE. This is the default value. HSM Note The value of this parameter is case- sensitive. Assume that you set this parameter to HSM. If you set the Origin parameter to Aliyun KMS, the CMK _ is created in Managed HSM. If you set the Origin parameter to EXTERNA, you can import external keys to Managed HSM. |
|---|---|---|---|---|
| EnableAutoma ticRotation | Boolean | No | false | Specifies whether to enable automatic key rotation. Valid values: true false. This is the default value. Note If the Origin parameter is set to EXTERNAL or the KeySpec parameter is set to an asymmetric CMK type, automatic key rotation is unavailable. |
| RotationInterv al | String | No | 365d | The period of automatic key rotation. It must be in the integer[unit] format. The unit can be d (day), h (hour), m (minute), or s (second). For example, both 7d and 604800s represent a 7-day period. The period can range from 7 days to 730 days. Note You must specify this parameter if the EnableAutomaticRotation parameter is set to true. You can ignore this parameter if the EnableAutomaticRotation parameter is set to false. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| KeyMetadata | Struct | See sample success responses | The metadata of the CMK. |

| Arn | String | acs:kms:cn- hangzhou:123456: key/08c33a6f- 4e0a-4a1b-a3fa- 7ddf**** | The Alibaba Cloud Resource Name (ARN) of the cloud resource. |
|---|---|---|---|
| AutomaticRota tion | String | Enabled | Indicates whether automatic key rotation is enabled. Enabled Disabled Suspended Note Automatic key rotation is suitable only for symmetric CMKs. |
| CreationDate | String | 2016-03- 25T10:42:40Z | The date and time when the CMK was created. The time is displayed in UTC. |
| Creator | String | 123456 | The creator of the CMK. |
| DeleteDate | String | 2020-07- 06T18:22:03Z | The scheduled time to delete the CMK. Note This value is returned only when the value of the KeyState parameter is PendingDeletion. |
| Description | String | key description example | The description of the CMK. |
| KeyId | String | 08c33a6f-4e0a- 4a1b-a3fa-7ddf**** | The ID of the CMK. |
| KeySpec | String | Aliyun AES 256 _ _ | The type of the CMK. |
| KeyState | String | Enabled | The status of the CMK. Valid values: Enabled: The CMK is enabled. Disabled: The CMK is disabled. PendingDeletion: The CMK is to be deleted. PendingImport: The CMK is to be imported. |
| KeyUsage | String | ENCRYPT/DECRYPT | The usage of the CMK. Valid values: ENCRYPT/DECRYPT: The CMK encrypts or decrypts data. SIGN/VERIFY: The CMK generates or verifies a digital signature. |

| LastRotationD ate | String | 2019-06- 06T18:22:03Z | The date and time when the last rotation was performed. The time is displayed in UTC. For a new CMK, the value of this parameter is the date and time when the initial version of the CMK was generated. |
|---|---|---|---|
| MaterialExpire Time | String | 2020-07- 06T18:22:03Z | The date and time when the key material for the CMK expires. The time is displayed in UTC. If the value is empty, the key material for the CMK does not expire. |
| NextRotationD ate | String | 2020-07- 06T18:22:03Z | The time when the next rotation is scheduled for execution. Note This value is returned only when the AutomaticRotation parameter is set to Enabled or Suspended. |
| Origin | String | Aliyun KMS _ | The source of the key material for the CMK. |
| PrimaryKeyVer sion | String | 0ec2d249-9f64- 4d8f-9587- 1215525e**** | The ID of the current primary key version of the symmetric CMK. Note The primary key version of a CMK is an active encryption key. KMS uses the primary key version of a specified CMK to encrypt data. This parameter is unsuitable for asymmetric CMKs. |
| ProtectionLeve l | String | SOFTWARE | The protection level of the CMK. Valid values: SOFTWARE HSM |
| RotationInterv al | String | 31536000s | The period of automatic key rotation. Unit: seconds. The format is an integer followed by the letter s. For example, if you want to specify a 7-day rotation period, set this parameter to 604800s. This value is returned only when the AutomaticRotation parameter is set to Enabled or Suspended. |

| RequestId | String | 3455b9b4-95c1- 419d-b310- db6a53b09a39 | The ID of the request. |
|---|---|---|---|

**Examples**

Sample requests

```
https://kms.cn-hangzhou.aliyuncs.com/?Action=CreateKey &<Common request parameters>
```

Sample success responses `XML` format

```xml
<KMS>
    <KeyMetadata>
        <CreationDate>2016-03-25T10:42:40Z</CreationDate>
        <Description>key description example</Description>
        <KeyId>08c33a6f-4e0a-4a1b-a3fa-7ddfa1d4****</KeyId>
        <KeySpec>Aliyun_AES_256</KeySpec>
        <KeyState>Enabled</KeyState>
        <KeyUsage>ENCRYPT/DECRYPT</KeyUsage>
        <PrimaryKeyVersion>0ec2d249-9f64-4d8f-9587-1215525e****</PrimaryKeyVersion>
        <DeleteDate></DeleteDate>
        <Creator>123456</Creator>
        <Arn>acs:kms:cn-hangzhou:123456:key/08c33a6f-4e0a-4a1b-a3fa-7ddfa1d4****</Arn>
        <Origin>Aliyun_KMS</Origin>
        <MaterialExpireTime></MaterialExpireTime>
        <ProtectionLevel>SOFTWARE</ProtectionLevel>
        <LastRotationDate>2016-03-25T10:42:40Z</LastRotationDate>
        <AutomaticRotation>Enabled</AutomaticRotation>
        <RotationInterval>31536000s</RotationInterval>
        <NextRotationDate>2017-03-25T10:42:40Z</NextRotationDate>
    </KeyMetadata>
    <RequestId>3455b9b4-95c1-419d-b310-db6a53b09a39</RequestId>
</KMS>
```

`JSON` format `{`

```json
        "KeyMetadata": {
                "CreationDate": "2016-03-25T10:42:40Z",
                "Description": "key description example",
                "KeyId": "08c33a6f-4e0a-4a1b-a3fa-7ddfa1d4****",
                "KeySpec": "Aliyun_AES_256",
                "KeyState": "Enabled",
                "KeyUsage": "ENCRYPT/DECRYPT",
                "PrimaryKeyVersion": "0ec2d249-9f64-4d8f-9587-1215525e****",
                "DeleteDate": "",
                "Creator":"123456",
                "Arn":"acs:kms:cn-hangzhou:123456:key/08c33a6f-4e0a-4a1b-a3fa-7ddfa1d4**
**",
                "Origin":"Aliyun_KMS",
                "MaterialExpireTime":"",
                "ProtectionLevel":"SOFTWARE",
                "LastRotationDate":"2016-03-25T10:42:40Z",
                "AutomaticRotation": "Enabled",
                "RotationInterval": "31536000s",
                "NextRotationDate":"2017-03-25T10:42:40Z"
```

`},`

```json
        "RequestId": "3455b9b4-95c1-419d-b310-db6a53b09a39"
```

**Error codes**

For a list of error codes, visit the Common error codes.

###### 5.1.2.2.4 GetParametersForImport

Obtains the parameters that you use to import key material for a customer master key (CMK). The returned parameters can be used to call the ImportKeyMaterial operation. You can import key material only for CMKs whose Origin parameter is EXTERNAL. The call returns the public key that is used to encrypt key material, the token that is used to import key material, and the expiration time of the token. The public key is encoded in Base64. The token is valid for 24 hours. The public key and token that are returned by the call can be used only for CMKs that are specified in this call. The public key and token that are returned by the same call must be used together. The algorithm that is used to encrypt key material must be the one that is specified in the call. The public key and token that are returned by each call must be unique. You must specify the type of public key and the encryption algorithm that are used to encrypt key material. The following table lists the types of public keys and encryption algorithms.

| Public key type | Encryption algorithm | Description |
|---|---|---|

| RSA 2048 _ | RSAES PKCS1 V1 5 _ _ _ RSAES OAEP SHA 1 _ _ _ RSAES OAEP SHA 256 _ _ _ | Keys of all regions and all protection levels are supported. |
|---|---|---|
| EC SM2 _ | SM2PKE | You can import only the keys whose protection level is HSM and certification type is State Cryptography Administration (SCA) certification. |

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | GetParametersF orImport | The operation that you want to perform. Set the value to GetParametersForImport. |
| KeyId | String | Yes | 1234abcd-12ab- 34cd-56ef- 12345678**** | The ID of the CMK. The ID must be globally unique. Note You can import key material only for CMKs whose Origin parameter is EXTERNAL. |
| WrappingAlgor ithm | String | Yes | RSAES PKCS1 V _ _ 1 5 _ | The algorithm that is used to encrypt key material. |
| WrappingKeyS pec | String | Yes | RSA 2048 _ | The type of the public key that is used to encrypt key material. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| ImportToken | String | Base64String | The token that is used to import key material. The value of this parameter is required when you call the ImportKeyMaterial operation. |
| KeyId | String | 1234abcd-12ab- 34cd-56ef- 12345678**** | The ID of the CMK. The ID must be globally unique. The value of this parameter is required when you call the ImportKeyMaterial operation. |

| PublicKey | String | MIIBIjANBgkqhkiG9 w0BAQEFAAOCAQ8 AMIIBCgKCAQEAlls 4uIBxD0GG84C+lG BO6Dhpf1J3XimC6 cPmPNaKKJMOzoX4 tD+C+r7aZv8lZ3v nPfxuxvy/YwG+wh UxTEEFUdqJTOIzhP fYucupqKM92crVHI uG+xtMVeHKjyTr+ UrtKCsQikqHT+19y DRN/RMoo2HUx0g mEnRyXd8t3JyUXu n9FdoxKA08GrsV7 nodb9ZsoBLhnev7t TLcXvLyKW6XG1Z QCQm6dPnbnwLeD XR7uK0Lqn9PM28 mBIdaiQUQxj2XbM 1CoJA+JiyVX3Ptdb +4rqukb4Rb05B80 Bs9xV/cf7FIku08l7 xGhrGiQFq+DFXw QWtwihXHZxz3Lhl dU+4ZPwIDAQAB | The public key that is used to encrypt key material. |
|---|---|---|---|
| RequestId | String | 8cdf51fd-bcd6- d79a-0ef4- e52c9b5466dc | The ID of the request. |
| TokenExpireTi me | String | 2018-01- 25T00:01:02Z | The time when the token to import key material expires. |

**Examples**

Sample requests

```
https://kms.cn-hangzhou.aliyuncs.com/?Action=GetParametersForImport &KeyId=1234abcd-12ab-34cd-56ef-12345678**** &WrappingAlgorithm=RSAES_PKCS1_V1_5 &WrappingKeySpec=RSA_2048 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<KMS>
    <ImportToken>Base64String</ImportToken>
<PublicKey>MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAlls4uIBxD0GG84C+lGBO6Dhpf1J3XimC6c PNaKKJMOzoX4tD+C+r7aZv8lZ3vnPfxuxvy/YwG+whUxTEEFUdqJTOIzhPfYucupqKM92crVHIuG+xtMVeHKjyTr+ tKCsQikqHT+19yDRN/RMoo2HUx0gmEnRyXd8t3JyUXun9FdoxKA08GrsV7nodb9ZsoBLhnev7tTLcXvLyKW6XG1ZQ m6dPnbnwLeDXR7uK0Lqn9PM28mBIdaiQUQxj2XbM1CoJA+JiyVX3Ptdb+4rqukb4Rb05B80Bs9xV/cf7FIku08l7x rGiQFq+DFXwQWtwihXHZxz3LhldU+4ZPwIDAQAB</PublicKey>
    <KeyId>1234abcd-12ab-34cd-56ef-12345678****</KeyId>
    <TokenExpireTime>2018-01-25T00:01:02Z</TokenExpireTime>
    <RequestId>8cdf51fd-bcd6-d79a-0ef4-e52c9b5466dc</RequestId>
</KMS>
```

`JSON` format `{`

```json
        "ImportToken":"Base64String",
"PublicKey":"MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAlls4uIBxD0GG84C+lGBO6Dhpf1J3XimC PmPNaKKJMOzoX4tD+C+r7aZv8lZ3vnPfxuxvy/YwG+whUxTEEFUdqJTOIzhPfYucupqKM92crVHIuG+xtMVeHKjyT UrtKCsQikqHT+19yDRN/RMoo2HUx0gmEnRyXd8t3JyUXun9FdoxKA08GrsV7nodb9ZsoBLhnev7tTLcXvLyKW6XG1 CQm6dPnbnwLeDXR7uK0Lqn9PM28mBIdaiQUQxj2XbM1CoJA+JiyVX3Ptdb+4rqukb4Rb05B80Bs9xV/cf7FIku08l GhrGiQFq+DFXwQWtwihXHZxz3LhldU+4ZPwIDAQAB",
        "KeyId":"1234abcd-12ab-34cd-56ef-12345678****",
        "TokenExpireTime":"2018-01-25T00:01:02Z",
        "RequestId":"8cdf51fd-bcd6-d79a-0ef4-e52c9b5466dc"
```

**Error codes**

For a list of error codes, visit the Common error codes.

###### 5.1.2.2.5 ImportKeyMaterial

Imports key material. When you call the CreateKey operation to create a customer master key (CMK), you can set Origin to EXTERNAL to use external key material. You can call this operation to import key material for a CMK whose Origin is set to EXTERNAL. If you use a CMK whose type is Aliyun_AES_256, the key material that you import must be a 256-bit key. If you use a CMK whose type is Aliyun_SM4, the key material that you import must be a 128-bit key. You can set the expiration time of the key material. You can also set the expiration time to never expire. You can always reimport the same key material and reset the expiration time. After the imported key material expires or is deleted, the specified CMK is unavailable until the same key material is imported again. The same key material can be imported to different CMKs. The data or data key that is encrypted by using one CMK cannot be decrypted by using another CMK.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ImportKeyMateri al | The operation that you want to perform. Set the value to ImportKeyMaterial. |
| EncryptedKey Material | String | Yes | bCPZx7I6v6KXs qEpr2OXKxuj2C CRtKdwp75Bw+ BGncYqBdfjFBYR tOE6HRlT0oeiRD Wzwnw9OA54O L36smDJrq4Lo9x 0CyYDiuKnRkcKt MtlzW0din7Pd7Il ZWWRdVueiw2q pzl7PkUWQGTds dbzpfJJQ+qj/cRIr k/E83UGyeyytSp gnb+lu0xEYcPaj RyWNsbi98N3pq qQzHXNNHO2NJ qHlnQgglqTiBEjk GeKFhfKmTc3vj ulIdVa3EaVIN6l wWfgx+UUYSrv bA77WDYKlDsZ 4SbK2/T7za9Tp1 qU7Ynqba7OKG VVj7PMbiaO80A xWZnjUMYCgEp 5w7V+seOXqw == | The public key that is returned when you call the GetParametersForImport operation. The public key is Base64 encoded. |
| ImportToken | String | Yes | Base64String | The token that is used to import key material. The token is returned when you call the GetParametersForImport operation. |
| KeyId | String | Yes | 1234abcd-12ab- 34cd-56ef- 12345678**** | The ID of the CMK for which you want to import key material. |
| KeyMaterialEx pireUnix | Long | Yes | 0 | The time when the key material expires. If you do not set this parameter or set this parameter to 0, the key material never expires. Note The value of this parameter cannot be earlier than the time when you call the operation. The time is based on the time of the KMS server. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | ec1017cf-ead4- f3ca-babc- c3b34f3dbecb | The ID of the request. |

**Examples**

Sample requests

```
https://kms.cn-hangzhou.aliyuncs.com/?Action=ImportKeyMaterial &EncryptedKeyMaterial=bCPZx7I6v6KXsqEpr2OXKxuj2CCRtKdwp75Bw+BGncYqBdfjFBYRtOE6HRlT0oeiRDW nw9OA54OL36smDJrq4Lo9x0CyYDiuKnRkcKtMtlzW0din7Pd7IlZWWRdVueiw2qpzl7PkUWQGTdsdbzpfJJQ+qj/c rk/E83UGyeyytSpgnb+lu0xEYcPajRyWNsbi98N3pqqQzHXNNHO2NJqHlnQgglqTiBEjkGeKFhfKmTc3vjulIdVa3 VIN6lwWfgx+UUYSrvbA77WDYKlDsZ4SbK2/T7za9Tp1qU7Ynqba7OKGVVj7PMbiaO80AxWZnjUMYCgEp5w7V+seOX
```

`==`

```
&ImportToken=Base64String &KeyId=1234abcd-12ab-34cd-56ef-12345678**** &KeyMaterialExpireUnix=0 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<KMS>
    <RequestId>ec1017cf-ead4-f3ca-babc-c3b34f3dbecb</RequestId>
</KMS>
```

`JSON` format `{`

```json
        "RequestId":"ec1017cf-ead4-f3ca-babc-c3b34f3dbecb"
```

**Error codes**

For a list of error codes, visit the Common error codes.

###### 5.1.2.2.6 EnableKey

Enables a specified customer master key (CMK). If a CMK is enabled, the CMK can be used for encryption and decryption.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | EnableKey | The operation that you want to perform. Set the value to EnableKey. |

| KeyId | String | Yes | 1234abcd-12ab- 34cd-56ef- 12345678**** | The ID of the CMK. The ID must be globally unique. |
|---|---|---|---|---|

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | efb1cbbd-a093- 4278-bc03- 639dd4fcc207 | The ID of the request. |

**Examples**

Sample requests

```
https://kms.cn-hangzhou.aliyuncs.com/?Action=EnableKey &KeyId=1234abcd-12ab-34cd-56ef-12345678**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<KMS>
    <RequestId>efb1cbbd-a093-4278-bc03-639dd4fcc207</RequestId>
</KMS>
```

`JSON` format `{`

```json
    "RequestId": "efb1cbbd-a093-4278-bc03-639dd4fcc207"
```

**Error codes**

For a list of error codes, visit the Common error codes.

###### 5.1.2.2.7 DisableKey

Disables a specified customer master key (CMK). If a CMK is disabled, the CMK cannot be used for encryption and decryption. The ciphertext encrypted by using this CMK cannot be decrypted until you re-enable the CMK.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DisableKey | The operation that you want to perform. Set the value to DisableKey. |

| KeyId | String | Yes | 1234abcd-12ab- 34cd-56ef- 12345678**** | The ID of the CMK. The ID must be globally unique. |
|---|---|---|---|---|

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 2fe70ce2-3303- 4fd6-b3ac- 472fb2705c62 | The ID of the request. |

**Examples**

Sample requests

```
https://kms.cn-hangzhou.aliyuncs.com/?Action=DisableKey &KeyId=1234abcd-12ab-34cd-56ef-12345678**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<KMS>
      <RequestId>2fe70ce2-3303-4fd6-b3ac-472fb2705c62</RequestId>
</KMS>
```

`JSON` format `{`

```json
    "RequestId": "2fe70ce2-3303-4fd6-b3ac-472fb2705c62"
```

**Error codes**

For a list of error codes, visit the Common error codes.

###### 5.1.2.2.8 ScheduleKeyDeletion

Deletes a specified customer master key (CMK). During the scheduled deletion time, the CMK is in the PendingDeletion state and cannot be used to encrypt data, decrypt data, or generate data keys. After a CMK is deleted, it cannot be recovered, and the data and the ciphertext data keys encrypted by using this CMK cannot be decrypted. Therefore, to prevent you from deleting CMKs by mistake, KMS allows you only to schedule key deletion tasks. You cannot immediately delete CMKs. If you want to delete a CMK, you can call the DisableKey operation to disable the CMK. When you call this operation, you must specify a waiting period of 7 to 30 days. The waiting period starts from the time when you submit the request.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ScheduleKeyDel etion | The operation that you want to perform. Set the value to ScheduleKeyDeletion. |
| KeyId | String | Yes | 1234abcd-12ab- 34cd-56ef- 12345678**** | The ID of the CMK. The ID must be globally unique. |
| PendingWindowI nDays | Integer | No | 7 | The number of days before the CMK is deleted. During this period, the CMK is in the PendingDeletion state. After this period ends, you cannot cancel the deletion. Valid values: 7 to 30. Unit: days. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 3da5b8cc-8107- 40ac-a170- 793cd181d7b7 | The ID of the request. |

**Examples**

Sample requests

```
https://kms.cn-hangzhou.aliyuncs.com/?Action=ScheduleKeyDeletion &KeyId=1234abcd-12ab-34cd-56ef-12345678**** &PendingWindowInDays=7 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<KMS>
    <RequestId>3da5b8cc-8107-40ac-a170-793cd181d7b7</RequestId>
</KMS>
```

`JSON` format `{`

```json
   "RequestId": "3da5b8cc-8107-40ac-a170-793cd181d7b7"
```

**Error codes**

| HttpCod e | Error code | Error message | Description |
|---|---|---|---|
| 400 | Throttling | Request was denied due to request throttling. | The error message returned because your traffic in this period has exceeded the limit. If your business requirements are not met, submit a ticket. |
| 404 | Forbidden.KeyNotF ound | The specified Key is not found. | The error message returned because the specified key does not exist. |

For a list of error codes, visit the Common error codes.

###### 5.1.2.2.9 DeleteKeyMaterial

Deletes the key material that you imported. This operation does not delete the customer master key (CMK) that is created by using the key material. If the CMK is in the PendingDeletion state, the state of the CMK and the scheduled deletion time do not change after you call this operation. If the CMK is not in the PendingDeletion state, the state of the CMK changes to PendingImport after you call this operation. After you delete the key material, you can import only the same key material to KMS.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteKeyMateri al | The operation that you want to perform. Set the value to DeleteKeyMaterial. |
| KeyId | String | Yes | 1234abcd-12ab- 34cd-56ef- 12345678**** | The ID of the CMK. The ID must be globally unique. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 4162a6af-bc99- 40b3-a552- 89dcc8aaf7c8 | The ID of the request. |

**Examples**

Sample requests

```
https://kms.cn-hangzhou.aliyuncs.com/?Action=DeleteKeyMaterial &KeyId=1234abcd-12ab-34cd-56ef-12345678**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<KMS>
       <RequestId>4162a6af-bc99-40b3-a552-89dcc8aaf7c8</RequestId>
</KMS>
```

`JSON` format `{`

```json
       "RequestId": "4162a6af-bc99-40b3-a552-89dcc8aaf7c8"
```

**Error codes**

For a list of error codes, visit the Common error codes.

###### 5.1.2.2.10 DescribeKey

Queries the information about a specified customer master key (CMK).

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeKey | The operation that you want to perform. Set the value to DescribeKey. |
| KeyId | String | Yes | 1234abcd-12ab- 34cd-56ef- 12345678**** | The ID of the CMK. The ID must be globally unique. You can also set this parameter to an alias that is bound to the CMK. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 3455b9b4-95c1- 419d-b310- db6a53b09a39 | The ID of the request. |
| KeyMetadata | Struct | See sample success responses | The metadata of the CMK. |
| CreationDate | String | 2016-03- 25T10:42:40Z | The date and time when the CMK was created. The time is displayed in UTC. |
| Description | String | key description example | The description of the CMK. |

| KeyId | String | 08c33a6f-4e0a- 4a1b-a3fa-7ddf**** | The ID of the CMK. |
|---|---|---|---|
| KeyState | String | Enabled | The status of the CMK. Valid values: Enabled: The CMK is enabled. Disabled: The CMK is disabled. PendingDeletion: The CMK is to be deleted. PendingImport: The CMK is to be imported. |
| KeyUsage | String | ENCRYPT/DECRYPT | The usage of the CMK. Valid values: ENCRYPT/DECRYPT: The CMK encrypts or decrypts data. SIGN/VERIFY: The CMK generates or verifies a digital signature. |
| DeleteDate | String | 2020-07- 06T18:22:03Z | The scheduled time to delete the CMK. Note This value is returned only when the value of the KeyState parameter is PendingDeletion. |
| Creator | String | 123456 | The creator of the CMK. |
| Arn | String | acs:kms:cn- hangzhou:123456: key/08c33a6f- 4e0a-4a1b-a3fa- 7ddf**** | The Alibaba Cloud Resource Name (ARN) of the cloud resource. |
| Origin | String | Aliyun KMS _ | The source of the key material for the CMK. |
| MaterialExpire Time | String | 2020-07- 06T18:22:03Z | The date and time when the key material for the CMK expires. The time is displayed in UTC. If the value is empty, the key material for the CMK does not expire. |
| ProtectionLeve l | String | SOFTWARE | The protection level of the CMK. Valid values: SOFTWARE HSM |

| PrimaryKeyVer sion | String | 0ec2d249-9f64- 4d8f-9587- 1215525e**** | The ID of the current primary key version of the symmetric CMK. The primary key version of a CMK is an active encryption key. KMS uses the primary key version of a specified CMK to encrypt data. This parameter is unsuitable for asymmetric CMKs. |
|---|---|---|---|
| LastRotationD ate | String | 2019-06- 06T18:22:03Z | The date and time when the last rotation was performed. The time is displayed in UTC. For a new CMK, the value of this parameter is the date and time when the initial version of the CMK was generated. |
| AutomaticRota tion | String | Enabled | Indicates whether to enable automatic key rotation. Valid values: Enabled Disabled Suspended This parameter is suitable only for symmetric CMKs. |
| RotationInterv al | String | 31536000s | The period of automatic key rotation. Unit: seconds. The format is an integer followed by the letter s. For example, if you want to specify a 7-day rotation period, set this parameter to 604800s. This value is returned only when the AutomaticRotation parameter is set to Enabled or Suspended. |
| NextRotationD ate | String | 2020-07- 06T18:22:03Z | The time when the next rotation is scheduled for execution. Note This value is returned only when the AutomaticRotation parameter is set to Enabled or Suspended. |
| KeySpec | String | Aliyun AES 256 _ _ | The type of the CMK. |

**Examples**

Sample requests

```
https://kms.cn-hangzhou.aliyuncs.com/?Action=DescribeKey &KeyId=1234abcd-12ab-34cd-56ef-12345678**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<KMS>
    <KeyMetadata>
        <CreationDate>2016-03-25T10:42:40Z</CreationDate>
        <Description>key description example</Description>
        <KeyId>08c33a6f-4e0a-4a1b-a3fa-7ddf****</KeyId>
        <KeySpec>Aliyun_AES_256</KeySpec>
        <KeyState>Enabled</KeyState>
        <KeyUsage>ENCRYPT/DECRYPT</KeyUsage>
        <PrimaryKeyVersion>0ec2d249-9f64-4d8f-9587-1215525e****</PrimaryKeyVersion>
        <DeleteDate></DeleteDate>
        <Creator>123456</Creator>
        <Arn>acs:kms:cn-hangzhou:123456:key/08c33a6f-4e0a-4a1b-a3fa-7ddf****</Arn>
        <Origin>Aliyun_KMS</Origin>
        <MaterialExpireTime></MaterialExpireTime>
        <ProtectionLevel>SOFTWARE</ProtectionLevel>
        <LastRotationDate>2019-06-06T18:22:03Z</LastRotationDate>
        <AutomaticRotation>Enabled</AutomaticRotation>
        <RotationInterval>31536000s</RotationInterval>
        <NextRotationDate>2020-07-06T18:22:03Z</NextRotationDate>
    </KeyMetadata>
    <RequestId>3455b9b4-95c1-419d-b310-db6a53b09a39</RequestId>
</KMS>
```

`JSON` format `{`

```json
        "KeyMetadata": {
                "CreationDate": "2016-03-25T10:42:40Z",
                "Description": "key description example",
                "KeyId": "08c33a6f-4e0a-4a1b-a3fa-7ddf****",
                "KeySpec": "Aliyun_AES_256",
                "KeyState": "Enabled",
                "KeyUsage": "ENCRYPT/DECRYPT",
                "PrimaryKeyVersion": "0ec2d249-9f64-4d8f-9587-1215525e****",
                "DeleteDate": "",
                "Creator":"123456",
                "Arn":"acs:kms:cn-hangzhou:123456:key/08c33a6f-4e0a-4a1b-a3fa-7ddf****",
                "Origin":"Aliyun_KMS",
                "MaterialExpireTime":"",
                "ProtectionLevel":"SOFTWARE",
                "LastRotationDate": "2019-06-06T18:22:03Z",
                "AutomaticRotation": "Enabled",
                "RotationInterval": "31536000s",
                "NextRotationDate": "2020-07-06T18:22:03Z"
```

`},`

```json
        "RequestId": "3455b9b4-95c1-419d-b310-db6a53b09a39"
```

**Error codes**

For a list of error codes, visit the Common error codes.

###### 5.1.2.2.11 UpdateKeyDescription

Updates the description of a specified CMK. This operation replaces the Description of the CMK with the value that you specify. For more information about the Description of the CMK, see DescribeKey. You can add or update the description of a CMK by using this operation.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | UpdateKeyDescr iption | The operation that you want to perform. Set the value to UpdateKeyDescription. |
| Description | String | Yes | key description example | The description of the CMK. This description includes the usage of the CMK, such as the types of data that you want to protect and the applications that can use the CMK. |
| KeyId | String | Yes | 1234abcd-12ab- 34cd-56ef- 12345678**** | The ID of the CMK. The ID must be globally unique. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 3455b9b4-95c1- 419d-b310- db6a53b09a39 | The ID of the request. |

**Examples**

Sample requests

```
https://kms.cn-hangzhou.aliyuncs.com/?Action=UpdateKeyDescription &Description=key description example &KeyId=1234abcd-12ab-34cd-56ef-12345678**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<KMS>
      <RequestId>3455b9b4-95c1-419d-b310-db6a53b09a39</RequestId>
</KMS>
```

`JSON` format `{`

```json
    "RequestId": "3455b9b4-95c1-419d-b310-db6a53b09a39"
```

**Error codes**

For a list of error codes, visit the Common error codes.

###### 5.1.2.2.12 ListKeys

Queries all customer master keys (CMKs) of the current Alibaba Cloud account in the current region.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ListKeys | The operation that you want to perform. Set the value to ListKeys. |
| PageNumber | Integer | No | 1 | The number of the page to return. Pages start from page 1. Default value: 1. |
| PageSize | Integer | No | 10 | The number of entries to return on each page. Valid values: 1 to 100. Default value: 10. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| TotalCount | Integer | 3 | The total number of CMKs. |
| PageNumber | Integer | 1 | The page number of the returned page. |
| PageSize | Integer | 10 | The number of entries returned per page. |
| RequestId | String | 1050b8f1-b264- 496d-a782- 6299cbaf15f8 | The ID of the request. |

| Keys | Array | [{"KeyId": "80e9409f-78fa- 42ab-84bd- 83f40c81****","Key Arn": "acs:kms:cn- hangzhou:123456: key/80e9409f- 78fa-42ab-84bd- 83f40c81****" }, {"KeyId": "8fbb1226-a06f- 4c57-8887- daa5b627****", "KeyArn": "acs:kms:cn- hangzhou:123456: key/8fbb1226- a06f-4c57-8887- daa5b627****"}, ] | An array that consists of the CMKs of the current Alibaba Cloud account in the current region. |
|---|---|---|---|
| KeyId | String | 08c33a6f-4e0a- 4a1b-a3fa- 7ddfa1d4**** | The ID of the CMK. The ID must be globally unique. |
| KeyArn | String | acs:kms:cn- hangzhou:123456: key/80e9409f- 78fa-42ab-84bd- 83f40c81**** | The Alibaba Cloud Resource Name (ARN) of the CMK. |

**Examples**

Sample requests

```
https://kms.cn-hangzhou.aliyuncs.com/?Action=ListKeys &PageNumber=1 &PageSize=10 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<KMS>
        <Keys>
                <Key>
                        <KeyId>80e9409f-78fa-42ab-84bd-83f40c81****</KeyId>
                        <KeyArn>acs:kms:cn-hangzhou:123456:key/80e9409f-78fa-42ab-84bd-8
3f40c81****</KeyArn>
                </Key>
                <Key>
                        <KeyId>8fbb1226-a06f-4c57-8887-daa5b627****</KeyId>
                        <KeyArn>acs:kms:cn-hangzhou:123456:key/8fbb1226-a06f-4c57-8887-d
aa5b627****</KeyArn>
                </Key>
                    </Keys>
        <TotalCount>3</TotalCount>
        <PageNumber>1</PageNumber>
        <PageSize>10</PageSize>
        <RequestId>bc29ec35-3373-48d1-8202-520fd78d****</RequestId>
</KMS>
```

`JSON` format `{`

```json
        "Keys": {
                "Key": [
```

`{`

```json
                                "KeyId": "80e9409f-78fa-42ab-84bd-83f40c81****",
                                "KeyArn": "acs:kms:cn-hangzhou:123456:key/80e9409f-78fa-
42ab-84bd-83f40c81****"
```

`},` `{`

```json
                                "KeyId": "8fbb1226-a06f-4c57-8887-daa5b627****",
                                "KeyArn": "acs:kms:cn-hangzhou:123456:key/8fbb1226-a06f-
4c57-8887-daa5b627****"
```

`},` `]`

```json
                "TotalCount": 3,
        "PageNumber": 1,
        "PageSize": 10,
        "RequestId": "bc29ec35-3373-48d1-8202-520fd78d****"
```

**Error codes**

| HttpCod e | Error code | Error message | Description |
|---|---|---|---|
| 400 | Throttling | Request was denied due to request throttling. | The error message returned because your traffic in this period has exceeded the limit. If your business requirements are not met, submit a ticket. |

For a list of error codes, visit the Common error codes.

###### 5.1.2.2.13 CancelKeyDeletion

Cancels the deletion of a CMK. When the deletion of a CMK is canceled, the CMK returns to the Enabled state.

**Debugging**

OpenAPI Explorer automatically calculates the signature value. For your convenience, we recommend that you call this operation in OpenAPI Explorer. OpenAPI Explorer dynamically generates the sample code of the operation for different SDKs.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CancelKeyDeleti on | The operation that you want to perform. Set the value to CancelKeyDeletion. |
| KeyId | String | Yes | 1234abcd-12ab- 34cd-56ef- 12345678**** | The globally unique ID of the CMK. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 3da5b8cc-8107- 40ac-a170- 793cd181d7b7 | The ID of the request. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=CancelKeyDeletion &KeyId=1234abcd-12ab-34cd-56ef-12345678**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<KMS>
      <RequestId>3da5b8cc-8107-40ac-a170-793cd181d7b7</RequestId>
</KMS>
```

`JSON` format `{`

```json
"RequestId": "3da5b8cc-8107-40ac-a170-793cd181d7b7"
```

###### 5.1.2.2.14 ReEncrypt

Re-encrypts ciphertext. When you call this operation, Key Management Service (KMS) decrypts the ciphertext, uses a different key to re-encrypt the generated plaintext or data key, and then returns the new ciphertext. You can call this operation in the following scenarios: After a key that is used to encrypt your data is rotated, you can call this operation to use the latest key version to re-encrypt the data. The key that is used to encrypt your data remains unchanged, but the encryption context is changed. In this scenario, you can call this operation to re-encrypt the data. You can call this operation to use a key in KMS to re-encrypt data or a data key that is previously encrypted by using a different key. To call the ReEncrypt operation, you must have the following permissions: The kms:ReEncryptFrom permission on the source key The kms:ReEncryptTo permission on the destination key For simplicity, you can specify kms:ReEncrypt* to allow both of the preceding permissions.

**Debugging**

OpenAPI Explorer automatically calculates the signature value. For your convenience, we recommend that you call this operation in OpenAPI Explorer. OpenAPI Explorer dynamically generates the sample code of the operation for different SDKs.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ReEncrypt | The operation that you want to perform. Set the value to ReEncrypt. |
| CiphertextBlob | String | Yes | ODZhOWVmZDk tM2QxNi00ODk0 LWJkNGYtMWZj NDNmM2YyYWJ mS7FmDBBQ0B kKsQrtRnidtPwir mDcS0ZuJCU41 xxAAWk4Z8qsA DfbV0b+i6kQml vj79dJdGOvtX69 Uycs901q******* * | The ciphertext. You can set this parameter to the ciphertext that is returned after a symmetric or asymmetric encryption operation. Symmetric encryption: the ciphertext that is returned by calling the Encrypt, GenerateDataKey, GenerateDataKeyWithoutPlaintext, or GenerateAndExportDataKey operation. Asymmetric encryption: the public key-encrypted ciphertext that is returned by calling the GenerateAndExportDataKey operation or the ciphertext that is encrypted by an external system using the public key of an asymmetric key. |

| DestinationKe yId | String | Yes | 1234abcd-12ab- 34cd-56ef- 12345678**** | The ID of the symmetric key that is used to re-encrypt the decrypted data or data key after the ciphertext is decrypted. |
|---|---|---|---|---|
| SourceKeyId | String | No | 5c438b18-05be- 40ad-b6c2- 3be6752c**** | The ID of the key that is used to decrypt the ciphertext. The ID must be globally unique. Note If you set CiphertextBlob to the public key-encrypted ciphertext that is returned after an asymmetric encryption operation, specify this parameter. |
| SourceKeyVers ionId | String | No | 2ab1a983-7072- 4bbc-a582- 584b5bd8**** | The version ID of the key that is used to decrypt the ciphertext. Note If you set CiphertextBlob to the public key-encrypted ciphertext that is returned after an asymmetric encryption operation, specify this parameter. |
| SourceEncrypt ionAlgorithm | String | No | RSAES OAEP SH _ _ A 256 _ | The encryption algorithm that is used by the public key to encrypt ciphertext when CiphertextBlob is set to the public key-encrypted ciphertext. For more information about encryption algorithms, see AsymmetricDecrypt. Valid values: RSAES OAEP SHA 256 _ _ _ RSAES OAEP SHA 1 _ _ _ SM2PKE Note If you set CiphertextBlob to the public key-encrypted ciphertext that is returned after an asymmetric encryption operation, specify this parameter. |

| SourceEncrypt ionContext | Json | No | {"Example":"Ex ample"} | The JSON string that consists of key- value pairs. If you configure this parameter when you call the Encrypt, GenerateDataKey, GenerateDataKeyWithoutPlaintext, or GenerateAndExportDataKey operation, an equivalent value is required when you decrypt data. Note If you set CiphertextBlob to the ciphertext that is returned after a symmetric encryption operation, specify this parameter. |
|---|---|---|---|---|
| DestinationEnc ryptionContext | Json | No | {"Example":"Ex ample"} | A JSON string that consists of key- value pairs. This parameter specifies the encryption context that is used to re-encrypt the decrypted data or data key. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| CiphertextBlob | String | DZhOWVmZDktM2 QxNi00ODk0LWJkN GYtMWZjNDNmM2 YyYWJmaaSl+TztSI Me43nbTH/Z1Wr4X fLftKhAciUmDQXu MRl4WTvKhxjMThj K**** | The new ciphertext. |
| KeyId | String | 2ab1a983-7072- 4bbc-a582- 584b5bd8**** | The ID of the key that is used to decrypt the ciphertext. The ID must be globally unique. |
| KeyVersionId | String | 202b9877-5a25- 46e3-a763- e20791b5**** | The version ID of the key that is used to decrypt the ciphertext. |

| RequestId | String | 207596a2-36d3- 4840-b1bd- f87044699bd7 | The ID of the request. |
|---|---|---|---|

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=ReEncrypt &CiphertextBlob=ODZhOWVmZDktM2QxNi00ODk0LWJkNGYtMWZjNDNmM2YyYWJmS7FmDBBQ0BkKsQrtRnidtPwir cS0ZuJCU41xxAAWk4Z8qsADfbV0b+i6kQmlvj79dJdGOvtX69Uycs901q******** &DestinationKeyId=1234abcd-12ab-34cd-56ef-12345678**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<KMS>
          <KeyId>202b9877-5a25-46e3-a763-e20791b5****</KeyId>
          <KeyVersionId>2ab1a983-7072-4bbc-a582-584b5bd8****</KeyVersionId>
<CiphertextBlob>DZhOWVmZDktM2QxNi00ODk0LWJkNGYtMWZjNDNmM2YyYWJmaaSl+TztSIMe43nbTH/Z1Wr4Xf tKhAciUmDQXuMRl4WTvKhxjMThjK****</CiphertextBlob>
          <RequestId>4bd560a1-729e-45f1-a3d9-b2a33d61046b</RequestId>
</KMS>
```

`JSON` format `{`

```json
    "KeyId": "202b9877-5a25-46e3-a763-e20791b5****",
    "KeyVersionId": "2ab1a983-7072-4bbc-a582-584b5bd8****",
    "CiphertextBlob":
"DZhOWVmZDktM2QxNi00ODk0LWJkNGYtMWZjNDNmM2YyYWJmaaSl+TztSIMe43nbTH/Z1Wr4XfLftKhAciUmDQXuM 4WTvKhxjMThjK****",
    "RequestId": "4bd560a1-729e-45f1-a3d9-b2a33d61046b"
```

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 500 | InternalFailure | Internal Failure. | An internal error occurred. Try again later. If the error persists, submit a ticket. |

For a list of error codes, see Service error codes.

###### 5.1.2.2.15 Encrypt

Encrypts plaintext by using a symmetric customer master key (CMK). KMS uses the primary version of a specified CMK to encrypt data. Only data of 6 KB or less can be encrypted. For example, you can call this operation to encrypt RSA keys, database logon passwords, or other sensitive information. When you migrate encrypted data across regions, you can call this operation in the destination region to encrypt the plaintext data key that is used to encrypt the migrated data in the source region. This way, the ciphertext data key is generated in the destination region. You can also call the Decrypt operation to decrypt the data key.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | Encrypt | The operation that you want to perform. Set the value to Encrypt. |
| KeyId | String | Yes | 1234abcd-12ab- 34cd-56ef- 12345678**** | The ID of the CMK. The ID must be globally unique. You can also set this parameter to an alias that is bound to the CMK. |
| Plaintext | String | Yes | SGVsbG8gd29y* *** | The plaintext to be encrypted. Note The plaintext must be Base64 encoded. |
| EncryptionCon text | Json | No | {"Example":"Ex ample"} | A JSON string that consists of key- value pairs. If you specify this parameter, an equivalent value is required when you call the Decrypt operation. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| CiphertextBlob | String | DZhOWVmZDktM2 QxNi00ODk0LWJkN GYtMWZjNDNmM2 YyYWJmaaSl+TztSI Me43nbTH/Z1Wr4X fLftKhAciUmDQXu MRl4WTvKhxjMThj K**** | The ciphertext that is encrypted by using the primary CMK version. |
| KeyId | String | 1234abcd-12ab- 34cd-56ef- 12345678**** | The ID of the CMK. The ID must be globally unique. If you set the KeyId parameter in the request to an alias, the ID of the CMK to which the alias is bound is returned. |

| KeyVersionId | String | 86a9efd9-3d16- 4894-bd4f- 1fc43f3f**** | The ID of the CMK version. The ID must be globally unique. |
|---|---|---|---|
| RequestId | String | 475f1620-b9d3- 4d35-b5c6- 3fbdd941423d | The ID of the request. |

**Examples**

Sample requests

```
https://kms.cn-hangzhou.aliyuncs.com/?Action=Encrypt &KeyId=1234abcd-12ab-34cd-56ef-12345678**** &Plaintext=SGVsbG8gd29y**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<KMS>
        <RequestId>475f1620-b9d3-4d35-b5c6-3fbdd941423d</RequestId>
<CiphertextBlob>DZhOWVmZDktM2QxNi00ODk0LWJkNGYtMWZjNDNmM2YyYWJmaaSl+TztSIMe43nbTH/Z1Wr4Xf tKhAciUmDQXuMRl4WTvKhxjMThjK****</CiphertextBlob>
        <KeyId>1234abcd-12ab-34cd-56ef-12345678****</KeyId>
        <KeyVersionId>86a9efd9-3d16-4894-bd4f-1fc43f3f****</KeyVersionId>
</KMS>
```

`JSON` format `{`

```json
    "RequestId":"475f1620-b9d3-4d35-b5c6-3fbdd941423d",
"CiphertextBlob":"DZhOWVmZDktM2QxNi00ODk0LWJkNGYtMWZjNDNmM2YyYWJmaaSl+TztSIMe43nbTH/Z1Wr4 LftKhAciUmDQXuMRl4WTvKhxjMThjK****",
    "KeyId":"1234abcd-12ab-34cd-56ef-12345678****",
    "KeyVersionId":"86a9efd9-3d16-4894-bd4f-1fc43f3f****"
```

**Error codes**

For a list of error codes, visit the Common error codes.

###### 5.1.2.2.16 GenerateDataKey

Generates a random data key. You can use the data key to locally encrypt data. This operation creates a random data key, encrypts the data key by using the specified customer master key (CMK), and returns the plaintext data key and the ciphertext data key. You can use the plaintext data key to locally encrypt data without using KMS. When you store the encrypted data, you also need to store the ciphertext data key. You can obtain the plaintext data key by querying the value of the Plaintext parameter in the response and obtain the ciphertext data key by querying the value of the CiphertextBlob parameter in the response. The CMK that you specify in the request of this operation is used only to encrypt the data key and is not involved in the generation of the data key. KMS does not record or store the generated data key. Therefore, you need to store the ciphertext data key in persistent storage. We recommend that you perform the following steps to locally encrypt data: Call the GenerateDataKey operation. Use the plaintext data key that you obtain to locally encrypt data without using KMS. Then, delete the plaintext data key from memory. Store the encrypted data along with the ciphertext data key that you obtain. We recommend that you perform the following steps to locally decrypt data: Call the Decrypt operation to decrypt the locally stored ciphertext data key. The plaintext data key is then returned. Use the plaintext data key to locally decrypt data without using KMS. Then, delete the plaintext data key from memory.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | GenerateDataKe y | The operation that you want to perform. Set the value to GenerateDataKey. |
| KeyId | String | Yes | 1234abcd-12ab- 34cd-56ef- 12345678**** | The ID of the CMK. The ID must be globally unique. You can also set this parameter to an alias that is bound to the CMK. |
| KeySpec | String | No | AES 256 _ | The length of the data key that you want to generate. Valid values: AES 256: a 256-bit symmetric key _ AES 128: a 128-bit symmetric key _ Note We recommend that you use the KeySpec or NumberOfBytes parameter to specify the length of a data key. If none of the parameters are specified, KMS generates a 256- bit data key. If both parameters are specified, KMS ignores the KeySpec parameter. |

| NumberOfByte s | Integer | No | 256 | The length of the data key that you want to generate. Valid values: 1 to 1024. Unit: bytes. |
|---|---|---|---|---|
| EncryptionCon text | Json | No | {"Example":"Ex ample"} | A JSON string that consists of key- value pairs. If you specify this parameter, an equivalent value is required when you call the Decrypt operation. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| CiphertextBlob | String | ODZhOWVmZDktM 2QxNi00ODk0LWJk NGYtMWZjNDNmM 2YyYWJmS7FmDBB Q0BkKsQrtRnidtPwi rmDcS0ZuJCU41xx AAWk4Z8qsADfbV0 b+i6kQmlvj79dJdG OvtX69Uycs901qOj op4bTSl0oQ | The ciphertext data key that is encrypted by using the primary CMK version. |
| KeyId | String | 599fa825-17de- 417e-9554- bb032cc6**** | The ID of the CMK. The ID must be globally unique. Note If you set the KeyId parameter to an alias of the CMK, the ID of the CMK to which the alias is bound is returned. |
| KeyVersionId | String | 2ab1a983-7072- 4bbc-a582- 584b5bd8**** | The ID of the CMK version. The ID must be globally unique. |
| Plaintext | String | QmFzZTY0IGVuY29 kZWQgcGxhaW50Z Xh0 | The plaintext data key. The value must be Base64 encoded. |
| RequestId | String | 7021b6ec-4be7- 4d3c-8a68- 1e85d4d515a0 | The ID of the request. |

**Examples**

Sample requests

```
https://kms.cn-hangzhou.aliyuncs.com/?Action=GenerateDataKey &KeyId=1234abcd-12ab-34cd-56ef-12345678**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<KMS> <CiphertextBlob>ODZhOWVmZDktM2QxNi00ODk0LWJkNGYtMWZjNDNmM2YyYWJmS7FmDBBQ0BkKsQrtRnidtPwir cS0ZuJCU41xxAAWk4Z8qsADfbV0b+i6kQmlvj79dJdGOvtX69Uycs901qOjop4bTSl0oQ</CiphertextBlob>
          <KeyId>599fa825-17de-417e-9554-bb032cc6****</KeyId>
          <KeyVersionId>2ab1a983-7072-4bbc-a582-584b5bd8****</KeyVersionId>
          <Plaintext>QmFzZTY0IGVuY29kZWQgcGxhaW50ZXh0</Plaintext>
          <RequestId>7021b6ec-4be7-4d3c-8a68-1e85d4d515a0</RequestId>
</KMS>
```

`JSON` format `{`

```json
        "CiphertextBlob":
"ODZhOWVmZDktM2QxNi00ODk0LWJkNGYtMWZjNDNmM2YyYWJmS7FmDBBQ0BkKsQrtRnidtPwirmDcS0ZuJCU41xxA k4Z8qsADfbV0b+i6kQmlvj79dJdGOvtX69Uycs901qOjop4bTSl0oQ",
        "KeyId": "599fa825-17de-417e-9554-bb032cc6****",
        "KeyVersionId": "2ab1a983-7072-4bbc-a582-584b5bd8****",
        "Plaintext": "QmFzZTY0IGVuY29kZWQgcGxhaW50ZXh0",
        "RequestId": "7021b6ec-4be7-4d3c-8a68-1e85d4d515a0"
```

**Error codes**

| HttpCod e | Error code | Error message | Description |
|---|---|---|---|
| 400 | Throttling | Request was denied due to request throttling. | The error message returned because your traffic in this period has exceeded the limit. If your business requirements are not met, submit a ticket. |

For a list of error codes, visit the Common error codes.

###### 5.1.2.2.17 GenerateDataKeyWithoutPlaintext

Generates a random data key, which can be used to locally encrypt data. This operation creates a random data key, encrypts the data key by using a specific symmetric customer master key (CMK), and then returns the ciphertext data key. This operation serves the same purpose as the GenerateDataKey operation. The only difference is that this operation does not return the plaintext data key. The CMK that you specify in the request of this operation is used only to encrypt the data key and is not involved in the generation of the data key. KMS does not record or store the generated data key. This operation is suitable for the scenario where you do not need to use the data key to immediately encrypt data. Before you can use the data key to encrypt data, you must call the Decrypt operation to decrypt the ciphertext data key. This operation is also suitable for a distributed system with different trust levels. For example, a system stores data in different partitions based on a preset trust policy. A module of the system creates different partitions and generates different data keys for each partition. This module is not involved in data production and consumption after it completes the initialization of the control plane. This module is the key provider. When a module on the control plane produces and consumes data, the module obtains the ciphertext data key for each partition. After the module decrypts the ciphertext data key, the module uses the plaintext data key to encrypt or decrypt data and then deletes the plaintext data key from memory. In such a system, the key provider does not need to obtain the plaintext data key. It needs only to have the permissions to call the GenerateDataKeyWithoutPlaintext operation. The data producers or consumers do not need to generate new data keys. They need only to have the permissions to call the Decrypt operation.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | GenerateDataKe yWithoutPlainte xt | The operation that you want to perform. Set the value to GenerateDataKeyWithoutPlaintext. |
| KeyId | String | Yes | 1234abcd-12ab- 34cd-56ef- 12345678**** | The ID of the CMK. The ID must be globally unique. You can also set this parameter to an alias that is bound to the CMK. |
| KeySpec | String | No | AES 256 _ | The length of the data key that you want to generate. Valid values: AES 256: a 256-bit symmetric key _ AES 128: a 128-bit symmetric key _ Note We recommend that you use the KeySpec or NumberOfBytes parameter to specify the length of a data key. If none of the parameters are specified, KMS generates a 256- bit data key. If both parameters are specified, KMS ignores the KeySpec parameter. |
| NumberOfByte s | Integer | No | 256 | The length of the data key. Valid values: 1 to 1024. Unit: bytes. |

| EncryptionCon text | Json | No | {"Example":"Ex ample"} | The JSON string that consists of key- value pairs. If you specify this parameter, an equivalent value is required when you call the Decrypt operation. |
|---|---|---|---|---|

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| CiphertextBlob | String | ODZhOWVmZDktM 2QxNi00ODk0LWJk NGYtMWZjNDNmM 2YyYWJmS7FmDBB Q0BkKsQrtRnidtPwi rmDcS0ZuJCU41xx AAWk4Z8qsADfbV0 b+i6kQmlvj79dJdG OvtX69Uycs901qOj op4bTS**** | The ciphertext data key that is encrypted by using the primary CMK version. |
| KeyId | String | 599fa825-17de- 417e-9554- bb032cc6**** | The ID of the CMK. The ID must be globally unique. Note If you set the KeyId parameter in the request to an alias of the CMK, the ID of the CMK to which the alias is bound is returned. |
| KeyVersionId | String | 2ab1a983-7072- 4bbc-a582- 584b5bd8**** | The ID of the CMK version. The ID must be globally unique. |
| RequestId | String | 7021b6ec-4be7- 4d3c-8a68- 1e85d4d515a0 | The ID of the request. |

**Examples**

Sample requests

```
https://kms.cn-hangzhou.aliyuncs.com/?Action=GenerateDataKeyWithoutPlaintext &KeyId=1234abcd-12ab-34cd-56ef-12345678**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<KMS>
         <RequestId>7021b6ec-4be7-4d3c-8a68-1e85d4d515a0</RequestId>
<CiphertextBlob>ODZhOWVmZDktM2QxNi00ODk0LWJkNGYtMWZjNDNmM2YyYWJmS7FmDBBQ0BkKsQrtRnidtPwir cS0ZuJCU41xxAAWk4Z8qsADfbV0b+i6kQmlvj79dJdGOvtX69Uycs901qOjop4bTS****</CiphertextBlob>
         <KeyId>599fa825-17de-417e-9554-bb032cc6****</KeyId>
         <KeyVersionId>2ab1a983-7072-4bbc-a582-584b5bd8****</KeyVersionId>
</KMS>
```

`JSON` format `{`

```json
    "RequestId":"7021b6ec-4be7-4d3c-8a68-1e85d4d515a0",
"CiphertextBlob":"ODZhOWVmZDktM2QxNi00ODk0LWJkNGYtMWZjNDNmM2YyYWJmS7FmDBBQ0BkKsQrtRnidtPw mDcS0ZuJCU41xxAAWk4Z8qsADfbV0b+i6kQmlvj79dJdGOvtX69Uycs901qOjop4bTS****",
    "KeyId":"599fa825-17de-417e-9554-bb032cc6****",
    "KeyVersionId":"2ab1a983-7072-4bbc-a582-584b5bd8****"
```

**Error codes**

For a list of error codes, visit the Common error codes.

###### 5.1.2.2.18 Decrypt

Decrypts the ciphertext that is specified by the CiphertextBlob parameter. You can call this operation to decrypt the ciphertext that is generated by using the following operations:

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | Decrypt | The operation that you want to perform. Set the value to Decrypt. |
| CiphertextBlob | String | Yes | DZhOWVmZDkt M2QxNi00ODk0 LWJkNGYtMWZj NDNmM2YyYWJ maaSl+TztSIMe 43nbTH/Z1Wr4X fLftKhAciUmDQX uMRl4WTvKhxjM ThjK**** | The ciphertext that you want to decrypt. |

| EncryptionCon text | Json | No | {"Example":"Ex ample"} | A JSON string that consists of key- value pairs. If you specify this parameter, an equivalent value is required when you call the Decrypt operation. |
|---|---|---|---|---|

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| KeyId | String | 202b9877-5a25- 46e3-a763- e20791b5**** | The ID of the customer master key (CMK) that is used to decrypt the ciphertext. The ID must be globally unique. |
| KeyVersionId | String | 2ab1a983-7072- 4bbc-a582- 584b5bd8**** | The ID of the CMK version that is used to decrypt the ciphertext. |
| Plaintext | String | tRYXuCwgja12xxO 1N/gZERDDCLw9d oZEQiPDk/Bv**** | The decrypted plaintext. |
| RequestId | String | 207596a2-36d3- 4840-b1bd- f87044699bd7 | The ID of the request. |

**Examples**

Sample requests

```
https://kms.cn-hangzhou.aliyuncs.com/?Action=Decrypt &CiphertextBlob=DZhOWVmZDktM2QxNi00ODk0LWJkNGYtMWZjNDNmM2YyYWJmaaSl+TztSIMe43nbTH/Z1Wr4Xf tKhAciUmDQXuMRl4WTvKhxjMThjK**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<KMS>
          <KeyId>202b9877-5a25-46e3-a763-e20791b5****</KeyId>
          <KeyVersionId>2ab1a983-7072-4bbc-a582-584b5bd8****</KeyVersionId>
          <Plaintext>tRYXuCwgja12xxO1N/gZERDDCLw9doZEQiPDk/Bv****</Plaintext>
          <RequestId>4bd560a1-729e-45f1-a3d9-b2a33d61046b</RequestId>
</KMS>
```

`JSON` format `{`

```json
    "KeyId": "202b9877-5a25-46e3-a763-e20791b5****",
    "KeyVersionId": "2ab1a983-7072-4bbc-a582-584b5bd8****",
    "Plaintext": "tRYXuCwgja12xxO1N/gZERDDCLw9doZEQiPDk/Bv****",
    "RequestId": "207596a2-36d3-4840-b1bd-f87044699bd7"
```

**Error codes**

For a list of error codes, visit the Common error codes.

###### 5.1.2.2.19 CreateAlias

Creates an alias for a customer master key (CMK). Each alias can represent only one CMK. The aliases of CMKs in the same region must be unique.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateAlias | The operation that you want to perform. Set the value to CreateAlias. |
| AliasName | String | Yes | alias/example | The alias that you want to create. The value must be 1 to 255 characters in length and must include the alias/ prefix. |
| KeyId | String | Yes | 1234abcd-12ab- 34cd-56ef- 12345678**** | The ID of the CMK. The ID must be globally unique. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 1d2baaf3-d357- 46c2-832e- 13560c2bd9cd | The ID of the request. |

**Examples**

Sample requests

```
https://kms.cn-hangzhou.aliyuncs.com/?Action=CreateAlias &KeyId=1234abcd-12ab-34cd-56ef-12345678**** &AliasName=alias/example &<Common request parameters>
```

Sample success responses `XML` format

```xml
<KMS>
        <RequestId>1d2baaf3-d357-46c2-832e-13560c2bd9cd</RequestId>
</KMS>
```

`JSON` format `{`

```json
       "RequestId": "1d2baaf3-d357-46c2-832e-13560c2bd9cd"
```

**Error codes**

| HttpCod e | Error code | Error message | Description |
|---|---|---|---|
| 400 | Throttling | Request was denied due to request throttling. | The error message returned because your traffic in this period has exceeded the limit. If your business requirements are not met, submit a ticket. |

For a list of error codes, visit the Common error codes.

###### 5.1.2.2.20 UpdateAlias

Binds an existing alias to a different customer master key (CMK) ID.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | UpdateAlias | The operation that you want to perform. Set the value to UpdateAlias. |
| AliasName | String | Yes | alias/example | The alias that you want to bind to a different CMK ID. The value must be 1 to 255 characters in length and must include the alias/ prefix. |

| KeyId | String | Yes | 1234abcd-12ab- 34cd-56ef- 12345678**** | The ID of the CMK. The ID must be globally unique. |
|---|---|---|---|---|

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 1d2baaf3-d357- 46c2-832e- 13560c2bd9cd | The ID of the request. |

**Examples**

Sample requests

```
https://kms.cn-hangzhou.aliyuncs.com/?Action=UpdateAlias &AliasName=alias/example &KeyId=1234abcd-12ab-34cd-56ef-12345678**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<KMS>
          <RequestId>1d2baaf3-d357-46c2-832e-13560c2bd9cd</RequestId>
</KMS>
```

`JSON` format `{`

```json
        "RequestId": "1d2baaf3-d357-46c2-832e-13560c2bd9cd"
```

**Error codes**

| HttpCod e | Error code | Error message | Description |
|---|---|---|---|
| 400 | Throttling | Request was denied due to request throttling. | The error message returned because your traffic in this period has exceeded the limit. If your business requirements are not met, submit a ticket. |
| 404 | Forbidden.KeyNotF ound | The specified Key is not found. | The error message returned because the specified key does not exist. |

For a list of error codes, visit the Common error codes.

###### 5.1.2.2.21 DeleteAlias

Deletes an alias.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteAlias | The operation that you want to perform. Set the value to DeleteAlias. |
| AliasName | String | Yes | alias/example | The alias that you want to delete. The value must be 1 to 255 characters in length and must include the alias/ prefix. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 4c8ae23f-3a42- 6791-a4ba- 1faa77831c28 | The ID of the request. |

**Examples**

Sample requests

```
https://kms.cn-hangzhou.aliyuncs.com/?Action=DeleteAlias &AliasName=alias/example &<Common request parameters>
```

Sample success responses `XML` format

```xml
<KMS>
        <RequestId>4c8ae23f-3a42-6791-a4ba-1faa77831c28</RequestId>
</KMS>
```

`JSON` format `{`

```json
        "RequestId": "4c8ae23f-3a42-6791-a4ba-1faa77831c28"
```

**Error codes**

For a list of error codes, visit the Common error codes.

###### 5.1.2.2.22 ListAliases

Queries all aliases in the current region for the current account.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ListAliases | The operation that you want to perform. Set the value to ListAliases. |
| PageNumber | Integer | No | 1 | The number of the page to return. Valid values: any non-zero positive integer. Default value: 1 |
| PageSize | Integer | No | 10 | The number of entries to return on each page. Valid values: 0 to 101. Default value: 10. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| TotalCount | Integer | 1 | The total number of returned customer master keys (CMKs). |
| PageNumber | Integer | 1 | The page number of the returned page. |
| PageSize | Integer | 10 | The number of entries returned per page. |
| RequestId | String | 1b57992c-834b- 4811-a889- f8bac1ba0353 | The ID of the request. |
| Aliases | Array | [{"AliasName": "alias/ExampleAlias 1","KeyId": "08c33a6f-4e0a- 4a1b-a3fa- 7ddfa1d****","Alias Arn": "acs:kms:cn- hangzhou:123456: alias/ExampleAlias 1"}] | The alias. |
| KeyId | String | 08c33a6f-4e0a- 4a1b-a3fa- 7ddfa1d**** | The CMK to which an alias is bound. |
| AliasName | String | alias/ExampleAlias 1 | The ID of the alias. |

| AliasArn | String | acs:kms:cn- hangzhou:123456: alias/ExampleAlias 1 | The Alibaba Cloud Resource Name (ARN) of the alias. |
|---|---|---|---|

**Examples**

Sample requests

```
https://kms.cn-hangzhou.aliyuncs.com/?Action=ListAliases &PageNumber=1 &PageSize=10 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<KMS>
        <Aliases>
                <Alias>
                        <AliasName>alias/ExampleAlias1</AliasName>
                        <KeyId>08c33a6f-4e0a-4a1b-a3fa-7ddfa1****</KeyId>
                        <AliasArn>acs:kms:cn-
hangzhou:123456:alias/ExampleAlias1</AliasArn>
                </Alias>
        </Aliases>
        <TotalCount>1</TotalCount>
        <PageNumber>1</PageNumber>
        <PageSize>10</PageSize>
        <RequestId>1b57992c-834b-4811-a889-f8bac1ba0353</RequestId>
</KMS>
```

`JSON` format `{`

```json
        "Aliases": {
                "Alias": [
```

`{`

```json
                                "AliasName": "alias/ExampleAlias1",
                                "KeyId": "08c33a6f-4e0a-4a1b-a3fa-7ddfa1d****",
                                "AliasArn": "acs:kms:cn-
hangzhou:123456:alias/ExampleAlias1"
```

`]` `},`

```json
        "TotalCount": 1,
        "PageNumber": 1,
        "PageSize": 10,
        "RequestId": "1b57992c-834b-4811-a889-f8bac1ba0353"
```

**Error codes**

| HttpCod e | Error code | Error message | Description |
|---|---|---|---|
| 400 | Throttling | Request was denied due to request throttling. | The error message returned because your traffic in this period has exceeded the limit. If your business requirements are not met, submit a ticket. |

For a list of error codes, visit the Common error codes.

###### 5.1.2.2.23 ListAliasesByKeyId

Queries all aliases that are bound to a specified customer master key (CMK).

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ListAliasesByKey Id | The operation that you want to perform. Set the value to ListAliasesByKeyId. |
| KeyId | String | Yes | 1234abcd-12ab- 34cd-56ef- 12345678**** | The ID of the CMK. The ID must be globally unique. |
| PageNumber | Integer | No | 1 | The number of the page to return. Valid values: any non-zero positive integer. Default value: 1 |
| PageSize | Integer | No | 10 | The number of entries to return on each page. Valid values: 0 to 101. Default value: 10 |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| TotalCount | Integer | 1 | The total number of returned CMKs. |
| PageNumber | Integer | 1 | The page number of the returned page. |
| PageSize | Integer | 10 | The number of entries returned per page. |
| RequestId | String | 1b57992c-834b- 4811-a889- f8bac1ba0353 | The ID of the request. |

| Aliases | Array | [ {"AliasName": "alias/ExampleAlias 1","KeyId": "08c33a6f-4e0a- 4a1b-a3fa- 7ddfa1d4****", "AliasArn": "acs:kms:cn- hangzhou:123456: alias/ExampleAlias 1"} ] | The alias. |
|---|---|---|---|
| KeyId | String | 08c33a6f-4e0a- 4a1b-a3fa- 7ddfa1d4**** | The ID of the CMK to which an alias is bound. |
| AliasName | String | alias/ExampleAlias 1 | The ID of the alias. |
| AliasArn | String | acs:kms:cn- hangzhou:123456: alias/ExampleAlias 1 | The Alibaba Cloud Resource Name (ARN) of the alias. |

**Examples**

Sample requests

```
https://kms.cn-hangzhou.aliyuncs.com/?Action=ListAliasesByKeyId &PageNumber=1 &PageSize=10 &KeyId=1234abcd-12ab-34cd-56ef-12345678**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<KMS>
        <Aliases>
                <Alias>
                        <AliasName>alias/ExampleAlias1</AliasName>
                        <KeyId>08c33a6f-4e0a-4a1b-a3fa-7ddfa1d4****</KeyId>
                        <AliasArn>acs:kms:cn-
hangzhou:123456:alias/ExampleAlias1</AliasArn>
                </Alias>
        </Aliases>
        <TotalCount>1</TotalCount>
        <PageNumber>1</PageNumber>
        <PageSize>10</PageSize>
        <RequestId>1b57992c-834b-4811-a889-f8bac1ba0353</RequestId>
</KMS>
```

`JSON` format `{`

```json
        "Aliases": {
                "Alias": [
```

`{`

```json
                                "AliasName": "alias/ExampleAlias1",
                                "KeyId": "08c33a6f-4e0a-4a1b-a3fa-7ddfa1d4****",
                                "AliasArn": "acs:kms:cn-
hangzhou:123456:alias/ExampleAlias1"
```

`]` `},`

```json
        "TotalCount": 1,
        "PageNumber": 1,
        "PageSize": 10,
        "RequestId": "1b57992c-834b-4811-a889-f8bac1ba0353"
```

**Error codes**

| HttpCod e | Error code | Error message | Description |
|---|---|---|---|
| 400 | Throttling | Request was denied due to request throttling. | The error message returned because your traffic in this period has exceeded the limit. If your business requirements are not met, submit a ticket. |

For a list of error codes, visit the Common error codes.

###### 5.1.2.2.24 DescribeRegions

Queries available regions for the current Alibaba Cloud account.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeRegions | The operation that you want to perform. Set the value to DescribeRegions. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Regions | Array |   | An array that consists of the regions that are available to use within the Alibaba Cloud account. |

| Region | Array |   | An array that consists of the information about the region that is available to use within the Alibaba Cloud account. |
|---|---|---|---|
| RegionId | String | cn-hangzhou | The ID of the region. |
| RequestId | String | 815240e2-aa37- 4c26-9cca- 05d4df3e8fe6 | The ID of the request. |

**Examples**

Sample requests

```
https://kms.cn-hangzhou.aliyuncs.com/?Action=DescribeRegions &<Common request parameters>
```

Sample success responses `XML` format

```xml
<KMS>
      <Regions>
            <Region>
                  <RegionId>cn-beijing</RegionId>
            </Region>
            <Region>
                  <RegionId>cn-hangzhou</RegionId>
            </Region>
      </Regions>
      <RequestId>815240e2-aa37-4c26-9cca-05d4df3e8fe6</RequestId>
</KMS>
```

`JSON` format `{`

```json
        "Regions": {
                "Region": [
```

`{`

```json
                                "RegionId": "cn-beijing"
```

`},` `{`

```json
                                "RegionId": "cn-hangzhou"
```

`]` `},`

```json
        "RequestId": "815240e2-aa37-4c26-9cca-05d4df3e8fe6"
```

**Error codes**

For a list of error codes, visit the Common error codes.

###### 5.1.2.2.25 CreateKeyVersion

Creates a version for a customer master key (CMK). This operation is supported only for asymmetric CMKs. The CMKs must be enabled. The minimum interval at which a CMK version is created is seven days. If you call this operation within seven days after the last CMK version is created, the error code Rejected.UnsupportedOperation is returned. The creation date of the last CMK version is specified by the LastRotationDate parameter. Each user can hold up to 50 asymmetric CMK versions in each region.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateKeyVersio n | The operation that you want to perform. Set the value to CreateKeyVersion. |
| KeyId | String | Yes | 0b30658a-ed1a- 4922-b8f7- a673ca9c**** | The ID of the CMK. The ID must be globally unique. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | b96f250a-4b75- 498c-91be- 22c6928f85be | The ID of the request. |
| KeyVersion | Struct | {"KeyId": "0b30658a-ed1a- 4922-b8f7- a673ca9c****","Ke yVersionId": "c0a3d5dc-0b47- 4199-a050- b289349a****", "CreationDate": "2019-08- 02T10:38:27Z"} | The metadata of the new CMK version. |
| KeyId | String | 0b30658a-ed1a- 4922-b8f7- a673ca9c**** | The ID of the CMK. The ID must be globally unique. |
| KeyVersionId | String | c0a3d5dc-0b47- 4199-a050- b289349a**** | The ID of the CMK version. The ID must be globally unique. |

| CreationDate | String | 2019-08- 02T10:38:27Z | The date and time the new CMK version was created. The time is displayed in UTC. |
|---|---|---|---|

**Examples**

Sample requests

```
https://kms.cn-hangzhou.aliyuncs.com/?Action=CreateKeyVersion &KeyId=0b30658a-ed1a-4922-b8f7-a673ca9c**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<KMS>
    <KeyVersion>
        <KeyId>0b30658a-ed1a-4922-b8f7-a673ca9c****</KeyId>
        <KeyVersionId>c0a3d5dc-0b47-4199-a050-b289349a****</KeyVersionId>
        <CreationDate>2019-08-02T10:38:27Z</CreationDate>
    </KeyVersion>
    <RequestId>b96f250a-4b75-498c-91be-22c6928f85be</RequestId>
</KMS>
```

`JSON` format `{`

```json
        "KeyVersion": {
                "KeyId": "0b30658a-ed1a-4922-b8f7-a673ca9c****",
                "KeyVersionId": "c0a3d5dc-0b47-4199-a050-b289349a****",
                "CreationDate": "2019-08-02T10:38:27Z"
```

`},`

```json
        "RequestId": "b96f250a-4b75-498c-91be-22c6928f85be"
```

**Error codes**

For a list of error codes, visit the Common error codes.

###### 5.1.2.2.26 DescribeKeyVersion

Queries detailed information about a specified CMK version.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeKeyVer sion | The operation that you want to perform. Set the value to DescribeKeyVersion. |

| KeyId | String | Yes | 1234abcd-12ab- 34cd-56ef- 12345678**** | The ID of the CMK. The ID must be globally unique. |
|---|---|---|---|---|
| KeyVersionId | String | Yes | 2ab1a983-7072- 4bbc-a582- 584b5bd8**** | The ID of the CMK version. The ID must be globally unique. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| KeyVersion | Struct | {"CreationDate":"2 016-03- 25T10:42:40Z","Ke yId":"599fa825- 17de-417e-9554- bb032cc6****","Ke yVersionId":"2ab1a 983-7072-4bbc- a582- 584b5bd8****"} | The metadata of the CMK version. |
| CreationDate | String | 2016-03- 25T10:42:40Z | The date and time when the CMK version was created. The time is displayed in UTC. |
| KeyId | String | 599fa825-17de- 417e-9554- bb032cc6**** | The ID of the CMK. The ID must be globally unique. Note If you set the KeyId parameter in the request to an alias, the ID of the CMK to which the alias is bound is returned. |
| KeyVersionId | String | 2ab1a983-7072- 4bbc-a582- 584b5bd8**** | The ID of the CMK version. |
| RequestId | String | 7021b6ec-4be7- 4d3c-8a68- 1e85d4d515a0 | The ID of the request. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/? Action=DescribeKeyVersion &KeyId=1234abcd-12ab-34cd-56ef-12345678**** &KeyVersionId=2ab1a983-7072-4bbc-a582-584b5bd8**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<KMS>
         <RequestId>7021b6ec-4be7-4d3c-8a68-1e85d4d515a0</RequestId>
         <KeyVersion>
                   <CreationDate>2016-03-25T10:42:40Z</CreationDate>
                   <KeyId>599fa825-17de-417e-9554-bb032cc6****</KeyId>
                   <KeyVersionId>2ab1a983-7072-4bbc-a582-584b5bd8****</KeyVersionId>
         </KeyVersion>
</KMS>
```

`JSON` format `{`

```json
    "RequestId":"7021b6ec-4be7-4d3c-8a68-1e85d4d515a0",
    "KeyVersion":{
        "CreationDate":"2016-03-25T10:42:40Z",
        "KeyId":"599fa825-17de-417e-9554-bb032cc6****",
        "KeyVersionId":"2ab1a983-7072-4bbc-a582-584b5bd8****"
```

**Error codes**

For a list of error codes, visit the Common error codes.

###### 5.1.2.2.27 ListKeyVersions

Queries all versions of a specified CMK.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ListKeyVersions | The operation that you want to perform. Set the value to ListKeyVersions. |
| KeyId | String | Yes | 0b30658a-ed1a- 4922-b8f7- a673ca9c**** | The ID of the CMK. The ID must be globally unique. You can also set this parameter to an alias that is bound to the CMK. |
| PageNumber | Integer | Yes | 1 | The number of the page to return. Pages start from page 1. Default value: 1 |

| PageSize | Integer | No | 10 | The number of entries to return on each page. Valid values: 0 to 101. Default value: 10. |
|---|---|---|---|---|

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| KeyVersions | Array |   | An array that consists of CMK versions. |
| KeyVersion | Array |   | The returned CMK version. |
| CreationDate | String | 2016-03- 25T10:42:40Z | The date and time when the CMK version was created. The time is displayed in UTC. |
| KeyId | String | 0b30658a-ed1a- 4922-b8f7- a673ca9c**** | The ID of the CMK. The ID must be globally unique. Note If you set the KeyId parameter in the request to an alias, the ID of the CMK to which the alias is bound is returned. |
| KeyVersionId | String | 1e3304fd-68ac- 4d5b-8886- ae5f01a1**** | The ID of the CMK version. The ID must be globally unique. |
| PageNumber | Integer | 1 | The page number of the returned page. |
| PageSize | Integer | 10 | The number of entries returned per page. |
| RequestId | String | f71204c4-53cd- 4eea-b405- 653ba2db7e86 | The ID of the request. |
| TotalCount | Integer | 3 | The total number of returned CMK versions. |

**Examples**

Sample requests

```
https://kms.cn-hangzhou.aliyuncs.com/?Action=ListKeyVersions &KeyId=1234abcd-12ab-34cd-56ef-12345678**** &PageNumber=1 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<KMS>
          <RequestId>f71204c4-53cd-4eea-b405-653ba2db7e86</RequestId>
          <KeyVersions>
                    <KeyVersion>
                              <KeyId>0b30658a-ed1a-4922-b8f7-a673ca9c****</KeyId>
                              <KeyVersionId>1e3304fd-68ac-4d5b-8886-ae5f01a1****
</KeyVersionId>
                              <CreationDate>2019-08-06T10:22:03Z</CreationDate>
                    </KeyVersion>
                    <KeyVersion>
                              <KeyId>0b30658a-ed1a-4922-b8f7-a673ca9c****</KeyId>
                              <KeyVersionId>2ab1a983-7072-4bbc-a582-584b5bd8****
</KeyVersionId>
                              <CreationDate>2019-08-06T10:19:18Z</CreationDate>
                    </KeyVersion>
                    <KeyVersion>
                              <KeyId>0b30658a-ed1a-4922-b8f7-a673ca9c****</KeyId>
                              <KeyVersionId>6a69c763-388a-4708-9fc0-4322266b****
</KeyVersionId>
                              <CreationDate>2019-08-06T10:17:04Z</CreationDate>
                    </KeyVersion>
          </KeyVersions>
          <TotalCount>3</TotalCount>
          <PageNumber>1</PageNumber>
          <PageSize>10</PageSize>
</KMS>
```

`JSON` format `{`

```json
    "KMS": {
        "RequestId": "f71204c4-53cd-4eea-b405-653ba2db7e86",
        "KeyVersions": {
            "KeyVersion": [
```

`{`

```json
                    "KeyId": "0b30658a-ed1a-4922-b8f7-a673ca9c****",
                    "KeyVersionId": "1e3304fd-68ac-4d5b-8886-ae5f01a1****",
                    "CreationDate": "2019-08-06T10:22:03Z"
```

`},` `{`

```json
                    "KeyId": "0b30658a-ed1a-4922-b8f7-a673ca9c****",
                    "KeyVersionId": "2ab1a983-7072-4bbc-a582-584b5bd8****",
                    "CreationDate": "2019-08-06T10:19:18Z"
```

`},` `{`

```json
                    "KeyId": "0b30658a-ed1a-4922-b8f7-a673ca9c****",
                    "KeyVersionId": "6a69c763-388a-4708-9fc0-4322266b****",
                    "CreationDate": "2019-08-06T10:17:04Z"
```

`]` `},`

```json
        "TotalCount": 3,
        "PageNumber": 1,
        "PageSize": 10
```

**Error codes**

For a list of error codes, visit the Common error codes.

###### 5.1.2.2.28 UpdateRotationPolicy

Updates a key rotation policy. When automatic key rotation is enabled, KMS automatically creates a new key version after the preset rotation period arrives. In addition, KMS sets the new key version as the primary key version. An automatic rotation policy cannot be defined in the following scenarios: The specified customer master key (CMK) is an asymmetric key. The specified CMK is a key that KMS manages for another Alibaba Cloud service. The specified CMK is a bring your own key (BYOK) that is imported into KMS. The specified CMK is not in the Enabled state.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | UpdateRotationP olicy | The operation that you want to perform. Set the value to UpdateRotationPolicy. |

| EnableAutoma ticRotation | Boolean | Yes | true | Specifies whether to enable automatic key rotation. Valid values: true false |
|---|---|---|---|---|
| KeyId | String | Yes | 1234abcd-12ab- 34cd-56ef- 12345678**** | The ID of the CMK. The ID must be globally unique. |
| RotationInterv al | String | No | 30d | The period of automatic key rotation. It must be in the integer[unit] format. The unit can be d (day), h (hour), m (minute), or s (second). For example, both 7d and 604800s represent a 7-day period. The period can range from 7 to 730 days. Unit: days. Note You must specify this parameter if you set EnableAutomaticRotation to true. You can ignore this parameter if you set EnableAutomaticRotation to false. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | efb1cbbd-a093- 4278-bc03- 639dd4fcc207 | The ID of the request. |

**Examples**

Sample requests

```
https://kms.cn-hangzhou.aliyuncs.com/?Action=UpdateRotationPolicy &EnableAutomaticRotation=true &KeyId=1234abcd-12ab-34cd-56ef-12345678**** &RotationInterval=30d &<Common request parameters>
```

Sample success responses `XML` format

```xml
<KMS>
    <RequestId>efb1cbbd-a093-4278-bc03-639dd4fcc207</RequestId>
</KMS>
```

`JSON` format `{`

```json
    "RequestId": "efb1cbbd-a093-4278-bc03-639dd4fcc207"
```

**Error codes**

For a list of error codes, visit the Common error codes.

###### 5.1.2.2.29 AsymmetricDecrypt

Decrypts data by using an asymmetric key. This operation is supported only for asymmetric keys for which the Usage parameter is set to ENCRYPT/DECRYPT. The following table lists the supported asymmetric encryption algorithms.

| KeySpec | Algorithm | Description | Maximum length (bytes) |
|---|---|---|---|
| RSA 2048 _ | RSAES OAEP SHA 256 _ _ _ | RSAES-OAEP using SHA-256 and MGF1 with SHA-256 | 256 |
| RSA 2048 _ | RSAES OAEP SHA 1 _ _ _ | RSAES-OAEP using SHA1 and MGF1 with SHA1 | 256 |
| EC SM2 _ | SM2PKE | SM2 elliptic curve public key encryption algorithm | 6144 |

The ciphertext is generated by calling the AsymmetricEncrypt operation or by using one of the asymmetric decryption algorithms that are listed in the preceding table.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | AsymmetricDecr ypt | The operation that you want to perform. Set the value to AsymmetricDecrypt. |
| Algorithm | String | Yes | RSAES OAEP SH _ _ A 1 _ | The asymmetric decryption algorithm that you use. |

| CiphertextBlob | String | Yes | BQKP+1zK6+ZE MxTP5qaVzcsgX tWplYBKm0NXd SnB5FzliFxE1bSi u4dnEIlca2JpeH 7yz1/S6fed630H +hIH6DoM25fTL NcKj+mFB0Xnh 9m2+HN59Mn4 qyTfcUeadnfCXS WcGBouhXFwcd d2rJ3n337bzTf4j m659gZu3L0i6P LuxM9p7mqdwO 0cKJPfGVfhnfMz +f4alMg79WB/N NyE2lyX7/qxvV4 9ObNrrJbKSFiz8 Djocaf0IESNLMb fYI5bXjWkJlX92D QbKhibtQW8ZOJ //ZC6t0AWcUoK L6QDm/dg5koQ alcleRinpB+Qad Fm894sLbVZ9+ N4GVsv1Wbjwg == | The ciphertext that you want to decrypt. Note We recommend that you use the Base64 encoding method. |
|---|---|---|---|---|
| KeyId | String | Yes | 5c438b18-05be- 40ad-b6c2- 3be6752c**** | The ID of the customer master key (CMK). The ID must be globally unique. Note You can also set this parameter to an alias that is bound to the CMK. |
| KeyVersionId | String | Yes | 2ab1a983-7072- 4bbc-a582- 584b5bd8**** | The ID of the CMK version. The ID must be globally unique. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| KeyId | String | 5c438b18-05be- 40ad-b6c2- 3be6752c**** | The ID of the CMK. The ID must be globally unique. Note If you set the KeyId parameter to an alias of the CMK, the ID of the CMK to which the alias is bound is returned. |

| KeyVersionId | String | 2ab1a983-7072- 4bbc-a582- 584b5bd8**** | The ID of the CMK version. The ID must be globally unique. |
|---|---|---|---|
| Plaintext | String | SGVsbG8gd29ybG Q= | The Base64-encoded plaintext that was generated after decryption. |
| RequestId | String | 475f1620-b9d3- 4d35-b5c6- 3fbdd941423d | The ID of the request. |

**Examples**

Sample requests

```
https://kms.cn-hangzhou.aliyuncs.com/?Action=AsymmetricDecrypt &Algorithm=RSAES_OAEP_SHA_1 &CiphertextBlob=BQKP+1zK6+ZEMxTP5qaVzcsgXtWplYBKm0NXdSnB5FzliFxE1bSiu4dnEIlca2JpeH7yz1/S6 d630H+hIH6DoM25fTLNcKj+mFB0Xnh9m2+HN59Mn4qyTfcUeadnfCXSWcGBouhXFwcdd2rJ3n337bzTf4jm659gZu 0i6PLuxM9p7mqdwO0cKJPfGVfhnfMz+f4alMg79WB/NNyE2lyX7/qxvV49ObNrrJbKSFiz8Djocaf0IESNLMbfYI5 jWkJlX92DQbKhibtQW8ZOJ//ZC6t0AWcUoKL6QDm/dg5koQalcleRinpB+QadFm894sLbVZ9+N4GVsv1Wbjwg== &KeyId=5c438b18-05be-40ad-b6c2-3be6752c**** &KeyVersionId=2ab1a983-7072-4bbc-a582-584b5bd8**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<KMS>
    <KeyId>5c438b18-05be-40ad-b6c2-3be6752c****</KeyId>
    <KeyVersionId>2ab1a983-7072-4bbc-a582-584b5bd8****</KeyVersionId>
    <Plaintext>SGVsbG8gd29ybGQ=</Plaintext>
    <RequestId>475f1620-b9d3-4d35-b5c6-3fbdd941423d</RequestId>
</KMS>
```

`JSON` format `{`

```json
  "KeyId": "5c438b18-05be-40ad-b6c2-3be6752c****",
  "KeyVersionId": "2ab1a983-7072-4bbc-a582-584b5bd8****",
  "Plaintext": "SGVsbG8gd29ybGQ=",
  "RequestId": "475f1620-b9d3-4d35-b5c6-3fbdd941423d"
```

**Error codes**

For a list of error codes, visit the Common error codes.

###### 5.1.2.2.30 AsymmetricEncrypt

Encrypts data by using asymmetric keys. This operation is supported only for asymmetric keys for which the Usage parameter is set to ENCRYPT/DECRYPT. The following table lists the supported encryption algorithms.

| KeySpec | Algorithm | Description | Maximum length in bytes |
|---|---|---|---|
| RSA 2048 _ | RSAES OAEP SHA 256 _ _ _ | RSAES-OAEP using SHA-256 and MGF1 with SHA-256 | 190 |
| RSA 2048 _ | RSAES OAEP SHA 1 _ _ _ | RSAES-OAEP using SHA1 and MGF1 with SHA1 | 214 |
| EC SM2 _ | SM2PKE | SM2 elliptic curve public key encryption algorithm | 6047 |

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | AsymmetricEncr ypt | The operation that you want to perform. Set the value to AsymmetricEncrypt. |
| Algorithm | String | Yes | RSAES OAEP SH _ _ A 1 _ | The encryption algorithm that you use. |
| KeyId | String | Yes | 5c438b18-05be- 40ad-b6c2- 3be6752c**** | The ID of the CMK. The ID must be globally unique. Note You can also set this parameter to an alias that is bound to the CMK. |
| KeyVersionId | String | Yes | 2ab1a983-7072- 4bbc-a582- 584b5bd8**** | The ID of the CMK version. The ID must be globally unique. |
| Plaintext | String | Yes | SGVsbG8gd29yb GQ= | The plaintext to be encrypted, which must be Base64-encoded. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|

| KeyId | String | 5c438b18-05be- 40ad-b6c2- 3be6752c**** | The ID of the CMK. The ID must be globally unique. Note If you set the KeyId parameter in the request to an alias, the ID of the CMK to which the alias is bound is returned. |
|---|---|---|---|
| KeyVersionId | String | 2ab1a983-7072- 4bbc-a582- 584b5bd8**** | The ID of the CMK version. The ID must be globally unique. |
| CiphertextBlob | String | BQKP+1zK6+ZEMx TP5qaVzcsgXtWplY BKm0NXdSnB5Fzli FxE1bSiu4dnEIlca2J peH7yz1/S6fed630 H+hIH6DoM25fTLN cKj+mFB0Xnh9m2 +HN59Mn4qyTfcU eadnfCXSWcGBouh XFwcdd2rJ3n337bz Tf4jm659gZu3L0i6 PLuxM9p7mqdwO0 cKJPfGVfhnfMz+f4a lMg79WB/NNyE2ly X7/qxvV49ObNrrJb KSFiz8Djocaf0IESN LMbfYI5bXjWkJlX92 DQbKhibtQW8ZOJ// ZC6t0AWcUoKL6Q Dm/dg5koQalcleRi npB+QadFm894sL bVZ9+N4GVsv1Wb jwg== | The ciphertext. Note We recommend that you use the Base64 encoding method. |
| RequestId | String | 475f1620-b9d3- 4d35-b5c6- 3fbdd941423d | The ID of the request. |

**Examples**

Sample requests

```
https://kms.cn-hangzhou.aliyuncs.com/?Action=AsymmetricEncrypt &KeyId=5c438b18-05be-40ad-b6c2-3be6752c**** &KeyVersionId=2ab1a983-7072-4bbc-a582-584b5bd8**** &Algorithm=RSAES_OAEP_SHA_1 &Plaintext=SGVsbG8gd29ybGQ= &<Common request parameters>
```

Sample success responses `XML` format

```xml
<KMS>
    <KeyId>5c438b18-05be-40ad-b6c2-3be6752c****</KeyId>
    <KeyVersionId>2ab1a983-7072-4bbc-a582-584b5bd8****</KeyVersionId>
<CiphertextBlob>RKF5WeXJtusIrvuPOjpkA/55EKzi8Wmc/eJ2fQUKphvL750jtInSX1wijw/7jGxUaTHTW6tgI 2ReN1aI1/wxqGxdzScwsMHxCBncnzQsZF+Fi4UFpI9pr4A1wc2u5Ngwyx9uA4K/kJ5bkS4NvmanxssAPZfSfbJSrA CP11tS0Cd54tQVGj4XK9tP9bJDKzKis1NClsOXZtNPX88kUqr3LkgFCsD07IwiePAfI2tn2fzeisje1Q7/d6VkF48 ZE0DAmnLRujt3yRRGDaKUkI6SUDjuKD4yqBUX15/DKfJtya+JIPQGiO2IEPlhL7+NMT17U0tKtK5ZPNEwxfZw== </CiphertextBlob>
    <RequestId>475f1620-b9d3-4d35-b5c6-3fbdd941423d</RequestId>
</KMS>
```

`JSON` format `{`

```json
  "KeyId": "5c438b18-05be-40ad-b6c2-3be6752c****",
  "KeyVersionId": "2ab1a983-7072-4bbc-a582-584b5bd8****",
  "CiphertextBlob":
"RKF5WeXJtusIrvuPOjpkA/55EKzi8Wmc/eJ2fQUKphvL750jtInSX1wijw/7jGxUaTHTW6tgIJl2ReN1aI1/wxqG zScwsMHxCBncnzQsZF+Fi4UFpI9pr4A1wc2u5Ngwyx9uA4K/kJ5bkS4NvmanxssAPZfSfbJSrAWlCP11tS0Cd54tQ j4XK9tP9bJDKzKis1NClsOXZtNPX88kUqr3LkgFCsD07IwiePAfI2tn2fzeisje1Q7/d6VkF48c3ZE0DAmnLRujt3 RGDaKUkI6SUDjuKD4yqBUX15/DKfJtya+JIPQGiO2IEPlhL7+NMT17U0tKtK5ZPNEwxfZw==",
  "RequestId": "475f1620-b9d3-4d35-b5c6-3fbdd941423d"
```

**Error codes**

For a list of error codes, visit the Common error codes.

###### 5.1.2.2.31 AsymmetricSign

Signs data by using asymmetric keys. This operation is supported only for asymmetric keys for which the Usage parameter is set to SIGN/VERIFY. The following table lists the supported signature algorithms.

| KeySpec | Algorithm | Description |
|---|---|---|
| RSA 2048 _ | RSA PSS SHA 256 _ _ _ | RSASSA-PSS using SHA-256 and MGF1 with SHA-256 |
| RSA 2048 _ | RSA PKCS1 SHA 256 _ _ _ | RSASSA-PKCS1-v1 5 using SHA- _ 256 |
| EC P256 _ | ECDSA SHA 256 _ _ | ECDSA on the P-256 Curve(secp256r1) with a SHA- 256 digest |

| EC P256K _ | ECDSA SHA 256 _ _ | ECDSA on the P-256K Curve(secp256k1) with a SHA- 256 digest |
|---|---|---|
| EC SM2 _ | SM2DSA | SM2 elliptic curve public key encryption algorithm |

When you calculate the SM2 signature based on GB/T 32918, the Digest parameter is used to calculate the digest value of the combination of Z(A) and M, rather than the SM3 digest value. M indicates the original message to be signed. Z(A) indicates the hash value for User A. The hash value is defined in GB/T 32918.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | AsymmetricSign | The operation that you want to perform. Set the value to AsymmetricSign. |
| Algorithm | String | Yes | RSA PSS SHA 2 _ _ _ 56 | The algorithm that is used to sign data. |
| Digest | String | Yes | ZOyIygCyaOW6 GjVnihtTFtIS9PN mskdyMlNKiuyjfz w= | The digest that is generated for the original message by using a hash algorithm. The hash algorithm is specified by the Algorithm parameter. Note We recommend that you use the Base64 encoding method. |
| KeyId | String | Yes | 5c438b18-05be- 40ad-b6c2- 3be6752c**** | The ID of the CMK. The ID must be globally unique. Note You can also set this parameter to an alias that is bound to the CMK. |
| KeyVersionId | String | Yes | 2ab1a983-7072- 4bbc-a582- 584b5bd8**** | The ID of the CMK version. The ID must be globally unique. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|

| KeyId | String | 5c438b18-05be- 40ad-b6c2- 3be6752c**** | The ID of the CMK. The ID must be globally unique. Note If you set the KeyId parameter in the request to an alias, the ID of the CMK to which the alias is bound is returned. |
|---|---|---|---|
| KeyVersionId | String | 2ab1a983-7072- 4bbc-a582- 584b5bd8**** | The ID of the CMK version. The ID must be globally unique. |
| Value | String | M2CceNZH00ZgL9 ED/ZHFp21YRAvYe ZHknJUc207OCZ0N 9wNn9As4z2bON3F F3je+1Nu+2+/8Zj 50HpMTpzYpMp2R 93cYmACCmhaYoK ydxylbyGzJR8y9lik ZRCrkD38lRoS40a BBvv/6iRKzQuo9EG YVcel36cMNg00Vm YNBy3pa1rwg3gA4 l3cy6kjayZja1WGP kVhrVKsrJMdbpl0A pLjXKuD8rw1n1XL CwCUEL5eLPljTZaA veqdOFQOiZnZEGI 27qIiZe7I1fN8tcz6a nS/gTM7xRKE++5 egEvRWlTQQTJeAp nPSiUPA+8ZykNdel QsOQh5SrGoyI4A5 pq3a/w== | The calculated signature. Note We recommend that you use the Base64 encoding method. |
| RequestId | String | 475f1620-b9d3- 4d35-b5c6- 3fbdd941423d | The ID of the request. |

**Examples**

Sample requests

```
https://kms.cn-hangzhou.aliyuncs.com/?Action=AsymmetricSign &KeyId=5c438b18-05be-40ad-b6c2-3be6752c**** &KeyVersionId=2ab1a983-7072-4bbc-a582-584b5bd8**** &Algorithm=RSA_PSS_SHA_256 &Digest=ZOyIygCyaOW6GjVnihtTFtIS9PNmskdyMlNKiuyjfzw= &<Common request parameters>
```

Sample success responses `XML` format

```xml
<KMS>
    <KeyId>5c438b18-05be-40ad-b6c2-3be6752c****</KeyId>
    <KeyVersionId>2ab1a983-7072-4bbc-a582-584b5bd8****</KeyVersionId>
<Value>M2CceNZH00ZgL9ED/ZHFp21YRAvYeZHknJUc207OCZ0N9wNn9As4z2bON3FF3je+1Nu+2+/8Zj50HpMTpz Mp2R93cYmACCmhaYoKydxylbyGzJR8y9likZRCrkD38lRoS40aBBvv/6iRKzQuo9EGYVcel36cMNg00VmYNBy3pa1 g3gA4l3cy6kjayZja1WGPkVhrVKsrJMdbpl0ApLjXKuD8rw1n1XLCwCUEL5eLPljTZaAveqdOFQOiZnZEGI27qIiZ I1fN8tcz6anS/gTM7xRKE++5egEvRWlTQQTJeApnPSiUPA+8ZykNdelQsOQh5SrGoyI4A5pq3a/w==</Value>
    <RequestId>475f1620-b9d3-4d35-b5c6-3fbdd941423d</RequestId>
</KMS>
```

`JSON` format `{`

```json
  "KeyId": "5c438b18-05be-40ad-b6c2-3be6752c****",
  "KeyVersionId": "2ab1a983-7072-4bbc-a582-584b5bd8****",
  "Value":
"M2CceNZH00ZgL9ED/ZHFp21YRAvYeZHknJUc207OCZ0N9wNn9As4z2bON3FF3je+1Nu+2+/8Zj50HpMTpzYpMp2R cYmACCmhaYoKydxylbyGzJR8y9likZRCrkD38lRoS40aBBvv/6iRKzQuo9EGYVcel36cMNg00VmYNBy3pa1rwg3gA 3cy6kjayZja1WGPkVhrVKsrJMdbpl0ApLjXKuD8rw1n1XLCwCUEL5eLPljTZaAveqdOFQOiZnZEGI27qIiZe7I1fN cz6anS/gTM7xRKE++5egEvRWlTQQTJeApnPSiUPA+8ZykNdelQsOQh5SrGoyI4A5pq3a/w==",
  "RequestId": "475f1620-b9d3-4d35-b5c6-3fbdd941423d"
```

**Error codes**

For a list of error codes, visit the Common error codes.

###### 5.1.2.2.32 AsymmetricVerify

Verifies signatures by using asymmetric keys. This operation is supported only for asymmetric keys for which the Usage parameter is set to SIGN/VERIFY. The following table lists the supported signature algorithms.

| KeySpec | Algorithm | Description |
|---|---|---|
| RSA 2048 _ | RSA PSS SHA 256 _ _ _ | RSASSA-PSS using SHA-256 and MGF1 with SHA-256 |
| RSA 2048 _ | RSA PKCS1 SHA 256 _ _ _ | RSASSA-PKCS1-v1 5 using SHA- _ 256 |
| EC P256 _ | ECDSA SHA 256 _ _ | ECDSA on the P-256 Curve(secp256r1) with a SHA- 256 digest |

| EC P256K _ | ECDSA SHA 256 _ _ | ECDSA on the P-256K Curve(secp256k1) with a SHA- 256 digest |
|---|---|---|
| EC SM2 _ | SM2DSA | SM2 elliptic curve public key encryption algorithm |

When you calculate the SM2 signature based on GB/T 32918, the Digest parameter is used to calculate the digest value of the combination of Z(A) and M, rather than the SM3 digest value. M indicates the original message to be signed. Z(A) indicates the hash value for User A. The hash value is defined in GB/T 32918.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | AsymmetricVerif y | The operation that you want to perform. Set the value to AsymmetricVerify. |
| Algorithm | String | Yes | RSA PSS SHA 2 _ _ _ 56 | The algorithm that is used to sign data. |
| Digest | String | Yes | ZOyIygCyaOW6 GjVnihtTFtIS9PN mskdyMlNKiuyjfz w= | The digest that is generated for the original message by using a hash algorithm. The hash algorithm is specified by the Algorithm parameter. Note We recommend that you use the Base64 encoding method. |
| KeyId | String | Yes | 5c438b18-05be- 40ad-b6c2- 3be6752c**** | The ID of the CMK. The ID must be globally unique. Note You can also set this parameter to an alias that is bound to the CMK. |
| KeyVersionId | String | Yes | 2ab1a983-7072- 4bbc-a582- 584b5bd8**** | The ID of the CMK version. The ID must be globally unique. |

| Value | String | Yes | M2CceNZH00Zg L9ED/ZHFp21YR AvYeZHknJUc20 7OCZ0N9wNn9A s4z2bON3FF3je +1Nu+2+/8Zj50 HpMTpzYpMp2R 93cYmACCmhaY oKydxylbyGzJR8 y9likZRCrkD38lR oS40aBBvv/6iRK zQuo9EGYVcel3 6cMNg00VmYNB y3pa1rwg3gA4l 3cy6kjayZja1WG PkVhrVKsrJMdbp l0ApLjXKuD8rw1 n1XLCwCUEL5eL PljTZaAveqdOFQ OiZnZEGI27qIiZ e7I1fN8tcz6anS/ gTM7xRKE++5e gEvRWlTQQTJeA pnPSiUPA+8Zyk NdelQsOQh5SrG oyI4A5pq3a/w= = | The signature value to be verified. Note We recommend that you use the Base64 encoding method. |
|---|---|---|---|---|

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| KeyId | String | 5c438b18-05be- 40ad-b6c2- 3be6752c**** | The ID of the CMK. The ID must be globally unique. Note If you set the KeyId parameter to an alias, the ID of the CMK to which the alias is bound is returned. |
| KeyVersionId | String | 2ab1a983-7072- 4bbc-a582- 584b5bd8**** | The ID of the CMK version. The ID must be globally unique. |
| Value | Boolean | true | Indicates whether the signature passed the verification. |
| RequestId | String | 475f1620-b9d3- 4d35-b5c6- 3fbdd941423d | The ID of the request. |

**Examples**

Sample requests

```
https://kms.cn-hangzhou.aliyuncs.com/?Action=AsymmetricVerify &KeyId=5c438b18-05be-40ad-b6c2-3be6752c**** &KeyVersionId=2ab1a983-7072-4bbc-a582-584b5bd8**** &Algorithm=RSA_PSS_SHA_256 &Digest=ZOyIygCyaOW6GjVnihtTFtIS9PNmskdyMlNKiuyjfzw= &Value=M2CceNZH00ZgL9ED/ZHFp21YRAvYeZHknJUc207OCZ0N9wNn9As4z2bON3FF3je+1Nu+2+/8Zj50HpMTpz Mp2R93cYmACCmhaYoKydxylbyGzJR8y9likZRCrkD38lRoS40aBBvv/6iRKzQuo9EGYVcel36cMNg00VmYNBy3pa1 g3gA4l3cy6kjayZja1WGPkVhrVKsrJMdbpl0ApLjXKuD8rw1n1XLCwCUEL5eLPljTZaAveqdOFQOiZnZEGI27qIiZ I1fN8tcz6anS/gTM7xRKE++5egEvRWlTQQTJeApnPSiUPA+8ZykNdelQsOQh5SrGoyI4A5pq3a/w== &<Common request parameters>
```

Sample success responses `XML` format

```xml
<KMS>
    <KeyId>5c438b18-05be-40ad-b6c2-3be6752c****</KeyId>
    <KeyVersionId>2ab1a983-7072-4bbc-a582-584b5bd8****</KeyVersionId>
    <Value>true</Value>
    <RequestId>475f1620-b9d3-4d35-b5c6-3fbdd941423d</RequestId>
</KMS>
```

`JSON` format `{`

```json
  "KeyId": "5c438b18-05be-40ad-b6c2-3be6752c****",
  "KeyVersionId": "2ab1a983-7072-4bbc-a582-584b5bd8****",
  "Value": true,
  "RequestId": "475f1620-b9d3-4d35-b5c6-3fbdd941423d"
```

**Error codes**

For a list of error codes, visit the Common error codes.

###### 5.1.2.2.33 GetPublicKey

Queries the public key of an asymmetric key pair. You can locally use the public key to encrypt data and verify signatures.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | GetPublicKey | The operation that you want to perform. Set the value to GetPublicKey. |

| KeyId | String | Yes | 5c438b18-05be- 40ad-b6c2- 3be6752c**** | The ID of the customer master key (CMK). The ID must be globally unique ID. You can also set this parameter to an alias that is bound to the CMK. |
|---|---|---|---|---|
| KeyVersionId | String | Yes | 2ab1a983-7072- 4bbc-a582- 584b5bd8**** | The ID of the CMK version. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| PublicKey | String | -----BEGIN PUBLIC KEY----- \nMIIBIjANBgkqhki G9w0BAQEFAAOCA Q8AMIIBCgKCAQEA s5Yu9AEgATN2/e3 nUz1K\nEy6ng8MS Putcse2/VECG/NUF 9C6D4IsJ64ShzY3d cn34WYzTOe916e MJFxyrNrSw\nHtc4 UOR5AvaoRrfpgu2 uq+i70/ZXrWL+pG b1hgZV8cWheIHM xwrR3IiQlM5qN7EF \n9BdyWtyBfUGsp0 Bn1VqlPc5G0x0a9x U2z9YtP994yDenN VIoIQ6Cov1lIEuwX Ab2\n7boC41ePXw D0JWt41sP+rgCmp jBx00puIG+IlnoReE gI1ZGYmK98GgA/X zmNjZiD\nyvXJZAc M33Ue85+PkR5iHT tSEbi4QAoqpJabpr Uzz3Fin2j1dRrcacx Gb7p31A9c\nJQIDA QAB\n-----END PUBLIC KEY-----\n | The public key returned in the PEM format. |
| KeyId | String | 5c438b18-05be- 40ad-b6c2- 3be6752c**** | The ID of the CMK. The ID must be globally unique. Note If you set the KeyId parameter in the request to an alias of the CMK, the ID of the CMK to which the alias is bound is returned. |
| RequestId | String | 475f1620-b9d3- 4d35-b5c6- 3fbdd941423d | The ID of the request. |

| KeyVersionId | String | 2ab1a983-7072- 4bbc-a582- 584b5bd8**** | The version of the CMK that is used to encrypt plaintext. |
|---|---|---|---|

**Examples**

Sample requests

```
https://kms.cn-hangzhou.aliyuncs.com/?Action=GetPublicKey &KeyId=5c438b18-05be-40ad-b6c2-3be6752c**** &KeyVersionId=2ab1a983-7072-4bbc-a582-584b5bd8**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<KMS>
    <KeyId>5c438b18-05be-40ad-b6c2-3be6752c****</KeyId>
    <KeyVersionId>2ab1a983-7072-4bbc-a582-584b5bd8****</KeyVersionId>
    <PublicKey>-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAl8FS40RYCB2IWt6VZdDS MLoUu/UYLr3l62IoRui1iXLZEUdoFHs1Tz4IscAGnavS7z6MKhfI88z4DuKrPb+B zc3iuhNcq9YoV96xatbRogRvLYsZt91w3/jiV72T8bVin6Fg3+FIvwf5oUHDCxxb ImbSMCgyybNnEx6sR3C5CIQO75Vv6Qrdg5lgXfyL6F9MyqFzCbLj/M7dFyhTq/bJ SNb0bgi61Xsn1oQb3vjEbn1hnMi4bVgNJCg65vwk2asC1445snkERoO7uWtYO6jr CWMduQxw/hCzCyTIegMlp0apDoStj633fZFJwO4PYmM1WGpkyhmubGZZ5sIbLeLA iwIDAQAB -----END PUBLIC KEY----- </PublicKey>
    <RequestId>475f1620-b9d3-4d35-b5c6-3fbdd941423d</RequestId>
</KMS>
```

`JSON` format `{`

```json
  "KeyId": "5c438b18-05be-40ad-b6c2-3be6752c****",
  "KeyVersionId": "2ab1a983-7072-4bbc-a582-584b5bd8****",
  "PublicKey": "-----BEGIN PUBLIC KEY-----
\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAs5Yu9AEgATN2/e3nUz1K\nEy6ng8MSPutcse2/VECG/ F9C6D4IsJ64ShzY3dcn34WYzTOe916eMJFxyrNrSw\nHtc4UOR5AvaoRrfpgu2uq+i70/ZXrWL+pGb1hgZV8cWheI xwrR3IiQlM5qN7EF\n9BdyWtyBfUGsp0Bn1VqlPc5G0x0a9xU2z9YtP994yDenNVIoIQ6Cov1lIEuwXAb2\n7boC4 PXwD0JWt41sP+rgCmpjBx00puIG+IlnoReEgI1ZGYmK98GgA/XzmNjZiD\nyvXJZAcM33Ue85+PkR5iHTtSEbi4QA pJabprUzz3Fin2j1dRrcacxGb7p31A9c\nJQIDAQAB\n-----END PUBLIC KEY-----\n",
  "RequestId": "475f1620-b9d3-4d35-b5c6-3fbdd941423d"
```

**Error codes**

For a list of error codes, visit the Common error codes.

## 6 Appendixes

### 6.1 STS overview

#### 6.1.1 What is STS?

Security Token Service (STS) allows you to manage temporary credentials to your Apsara Stack resources. Resource Access Management (RAM) provides RAM users and RAM roles. A RAM role does not have permanent identity credentials. A RAM role can be assumed to access Apsara Stack resources by using an issued STS token. When the STS token is issued, you can specify a validity period and access permissions for the STS token.

**Use a RAM user to obtain an STS token**

An authorized RAM user can use an AccessKey pair to call the AssumeRole operation. This way, the RAM user can obtain an STS token of a RAM role and can use the STS token to access Apsara Stack resources.

**Benefits**

STS tokens help reduce the risks of AccessKey pair leaks. An AccessKey pair is a long-term credential for a RAM user. STS tokens are temporary credentials. You can specify the validity period for STS tokens. After STS tokens expire, they become invalid. Therefore, you do not need to rotate the STS tokens on a regular basis. You can attach custom policies to STS tokens for flexible and fine-grained authorization.

#### 6.1.2 AssumeRole

Obtains a Security Token Service (STS) token that is used by a RAM user to assume a RAM role. In this example, an Apsara Stack tenant account is used as the trusted entity of the RAM role.

**Request parameters**

| Parameter | Type | Requ ired | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | AssumeRole | The operation that you want to perform. Set the value to AssumeRole. |
| RoleArn | String | Yes | acs:ram::123456 789012****:role/ adminrole | The Apsara Stack Resource Name (ARN) of the RAM role. The trusted entity of the RAM role is an Apsara Stack tenant account. |

| Parameter | Type | Requ ired | Example | Description |
|---|---|---|---|---|
| RoleSessionNa me | String | Yes | alice | The name of the role session. Set this parameter based on your business requirements. In most cases, you can set this parameter to the identity of the user who calls the operation. For example, specify a username. In ActionTrail logs, you can distinguish the users who assume the same RAM role to perform operations based on the value of the RoleSessionName parameter. This way, you can perform user-specific auditing. The name must be 2 to 64 characters in length and can contain letters, digits, periods (.), at signs (@), hyphens (-), and underscores ( ). _ |
| Policy | String | No | {"Statement": [{"Action": ["*"],"Effect": "Allow","Resourc e": ["*"]}],"Version":" 1"} | The policy that specifies the permissions of the STS token. You can use this parameter to grant the STS token fewer permissions than the permissions granted to the RAM role. The policy must be 1 to 1,024 characters in length. |

**Responses**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 6894B13B-6D71- 4EF5-88FA- F32781734A7F | The ID of the request. |
| Credentials | None | None | The access credentials. |
| AccessKeyId | String | STS.L4aBSCSJVMuK g5U1**** | The AccessKey ID. |
| AccessKeySecret | String | ****************************************** | The AccessKey secret. |
| SecurityToken | String | ******** | The security token. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Expiration | String | 2015-04- 09T11:52:19Z | The time when the STS token expires. |
| AssumedRoleUser | None | None | The temporary identity that you use to assume the RAM role. |
| Arn | String | acs:ram::12345678 9012****:role/admi nrole/alice | The ARN of the temporary identity that you use to assume the RAM role. |
| AssumedRoleId | String | 34458433936495** **:alice | The ID of the temporary identity that you use to assume the RAM role. |

**Examples**

**Add Project Object Model (POM) dependencies**

The Alibaba Cloud core library is required. Perform the following steps to add the Alibaba Cloud core library to POM:

```xml
    <dependency>
      <groupId>com.aliyun</groupId>
      <artifactId>aliyun-java-sdk-core</artifactId>
      <version>[4.4.9,5.0.0)</version>
    </dependency>
```

**Call an API operation to obtain the STS AccessKey 3-tuple.**

In the following sample code, the `Sts::AssumeRole::2015-04-01` operation is used to obtain the 3-tuple.

```java
package com.aliyuns.test; import com.alibaba.fastjson.JSONObject; import com.aliyuncs.CommonRequest; import com.aliyuncs.CommonResponse; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.exceptions.ServerException; import com.aliyuncs.http.FormatType; import com.aliyuncs.http.HttpClientConfig; import com.aliyuncs.http.MethodType; import com.aliyuncs.http.ProtocolType; import com.aliyuncs.profile.DefaultProfile; import org.apache.commons.lang3.StringUtils; public class STSAccessKeyDemo {
    public static void main(String[] args) {
//CreateandinitialieaDefaltAcsClientinstance
```

```java
        // Create and initialize a DefaultAcsClient instance.
        DefaultProfile profile = DefaultProfile.getProfile("<yourRegionID>", "
<yourAccessKeyID>", "<yourAccessKeySecret>");
        HttpClientConfig clientConfig = HttpClientConfig.getDefault();
        clientConfig.setIgnoreSSLCerts(true);
        clientConfig.setProtocolType(ProtocolType.HTTPS);
        profile.setHttpClientConfig(clientConfig);
        IAcsClient client = new DefaultAcsClient(profile);
        CommonRequest request = new CommonRequest();
        // Replace "sts.aliyuns.com" with the actual endpoint of STS. In most cases, th
e endpoint is in the following format: sts-vpc.${global:region}.${global:internet-domai n}.
        request.setSysDomain("sts.aliyuns.com");
        request.setSysProduct("Sts");
        request.setSysAction("AssumeRole");
        request.setSysVersion("2015-04-01");
        request.setSysMethod(MethodType.POST);
        request.setHttpContentType(FormatType.FORM);
        // Replace "<yourRoleSessionName>" with the alias that you specify for the curr
ent role session.
        request.putQueryParameter("RoleSessionName", "<yourRoleSessionName>");
        // Replace "<yourRoleArn>" with the actual ARN that you obtained for the RAM ro
le in the preceding step.
        request.putQueryParameter("RoleArn", "<yourRoleArn>");
        try {
            CommonResponse response = client.getCommonResponse(request);
            String assumeRole = response.getData();
            if (StringUtils.isEmpty(assumeRole)) return;
            JSONObject assumeRoleJson = JSONObject.parseObject(assumeRole);
            JSONObject credentials = assumeRoleJson.getJSONObject("Credentials");
            // Obtain the STS AccessKey 3-tuple.
            String stsAK = credentials.getString("AccessKeyId");
            String stsSK = credentials.getString("AccessKeySecret");
            String stsToken = credentials.getString("SecurityToken");
            System.out.println("stsAk: " + stsAK +"\nstsSk: " + stsSK + "\nstsToken: "
+ stsToken);
        } catch (ServerException e) {
            System.out.println(e.getErrCode());
            System.out.println(e.getErrMsg());
        } catch (ClientException e) {
            System.out.println(e.getErrCode());
            System.out.println(e.getErrMsg());
```

**Call examples**

In the following sample code, the `DescribeZones` operation in Elastic Compute Service (ECS) is used.

```java
package com.aliyuns.test; import com.aliyuncs.CommonRequest; importcomaliyuncsCommonResponse;
```

```java
import com.aliyuncs.CommonResponse; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.exceptions.ServerException; import com.aliyuncs.http.FormatType; import com.aliyuncs.http.HttpClientConfig; import com.aliyuncs.http.MethodType; import com.aliyuncs.http.ProtocolType; import com.aliyuncs.profile.DefaultProfile; public class DescribeZonesDemo {
    public static void main(String[] args) {
        // Replace "<yourRegionID>" with the actual region ID.
        // Replace "<yourStsAccesskey>" and "<yourStsAccessKeySecret>" with the
AccessKey ID and secret in the 3-tuple that you obtained in the preceding step.
        DefaultProfile profile = DefaultProfile.getProfile("<yourRegionID>", "
<yourStsAccessKey>", "<yourStsAccessKeySecret>");
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
        //Replace "<yourRegionID>" with the actual region ID.
        request.putHeadParameter("x-acs-regionid", "<yourRegionID>");
        // Replace "<yourStsToken>" with the STS token in the 3-tuple that you obtained
in the preceding step.
        request.putQueryParameter("SecurityToken", "<yourStsToken>");
        // Optional. Specify the resource set ID.
        // request.putHeadParameter("x-acs-resourcegroupid", "<yourResourceGroupID>");
        // Required. Specify the organization ID.
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

**Error codes**

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | InvalidParameter | The parameter RoleArn is wrongly formed. | The error message returned because the ARN format of the RAM role is invalid. |
| 400 | InvalidParameter.Role Arn | The parameter RoleArn is wrongly formed. | The error message returned because the ARN format of the RAM role is invalid. |
| 400 | InvalidParameter.Role SessionName | The parameter RoleSessionName is wrongly formed. | The error message returned because the value of the RoleSessionName parameter is in an invalid format. The value must be 2 to 64 characters in length and can contain letters, digits, periods (.), at signs (@), hyphens (-), and underscores ( ). _ |
| 400 | InvalidParameter.Dura tionSeconds | The Min/Max value of DurationSeconds is 15min/1hr. | The error message returned because the value of the DurationSeconds parameter is invalid. The minimum value is 900, and the maximum value is equal to the value of the MaxSessionDuration parameter. |
| 400 | InvalidParameter.Polic yGrammar | The parameter Policy has not passed grammar check. | The error message returned because the syntax of the policy is invalid. |
| 400 | InvalidParameter.Polic ySize | The size of Policy must be smaller than 1024 bytes. | The error message returned because the length of the specified policy string exceeds the upper limit. The policy string can be up to 1,024 characters in length. |

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 403 | NoPermission | You are not authorized to do this action. You should be authorized by RAM. | The error message returned because the STS token does not have the required permissions. |
| 404 | EntityNotExist.Role | The specified Role not exists. | The error message returned because the specified RAM role does not exist. |
| 500 | InternalError | STS Server Internal Error happened. | The error message returned because an internal server error occurred. |
