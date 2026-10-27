---
title: "Alibaba Cloud Apsara Stack V3.18.2 IPv6 Gateway Developer Guide 20240516"
product_version: "V3.18.2"
doc_version: "20240516"
pdf_pages: 61
source_pdf: "Alibaba Cloud Apsara Stack V3.18.2 IPv6 Gateway Developer Guide 20240516.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/v3.18.2%E7%89%88%E6%9C%AC%E6%96%87%E6%A1%A3/IPv6%E7%BD%91%E5%85%B3/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.2%20IPv6%20Gateway%20Developer%20Guide%2020240516.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes+edge-junk)
---

# Alibaba Cloud Apsara Stack V3.18.2 IPv6 Gateway Developer Guide 20240516

## Table of Contents

- 1 Getting started
  - 1.1 Apsara Stack documentation
  - 1.2 Call API operations
- 2 Preparations
  - 2.1 Log on to the API Tool console
  - 2.2 Obtain API information
  - 2.3 Obtain an AccessKey pair
  - 2.4 Obtain the values of common header parameters
  - 2.5 Obtain access credentials assigned by STS
- 3 Use POP to make API calls
  - 3.1 Preparations
  - 3.2 SDK for Java
  - 3.3 SDK for Go
  - 3.4 SDK for Python
- 4 API references
  - 4.1 List of operations by function
  - 4.2 Make API requests
    - 4.2.1 Request syntax
    - 4.2.2 API authorization
    - 4.2.3 Sign an API request
  - 4.3 RAM authentication
  - 4.4 common parameters
  - 4.5 IPv6 gateways
    - 4.5.1 CreateIpv6Gateway
    - 4.5.2 DescribeIpv6Gateways
    - 4.5.3 DescribeIpv6GatewayAttribute
    - 4.5.4 ModifyIpv6GatewayAttribute
    - 4.5.5 ModifyIpv6GatewaySpec
    - 4.5.6 DeleteIpv6Gateway
    - 4.5.7 DescribeIpv6EgressOnlyRules
    - 4.5.8 CreateIpv6EgressOnlyRule
    - 4.5.9 DeleteIpv6EgressOnlyRule
    - 4.5.10 AllocateIpv6InternetBandwidth
    - 4.5.11 ModifyIpv6AddressAttribute
    - 4.5.12 DeleteIpv6InternetBandwidth
    - 4.5.13 DescribeIpv6Addresses
    - 4.5.14 ModifyIpv6InternetBandwidth

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
2. Click the **Enterprise**, **Agility**, or **All-in-one** tab based on the Apsara Stack version that you
use.
3. Select an Apsara Stack version from the drop-down list.
4. In the left-side navigation pane, select the Apsara Stack service whose documentation you
want to view.
5. In the product documentation section, click **View Details** or **Download PDF**.

### 1.2 Call API operations

Apsara Stack allows you to call API operations by using the point of presence (POP) gateway. To ensure that Apsara Stack provides the same experience as Alibaba Cloud public cloud, API operations in Apsara Stack Enterprise V3.16.0 and later are called by using the POP gateway by default. This topic describes how to use the POP gateway to call Apsara Stack API operations.

**Flowchart**

**Procedure**

1. Obtain an access credential.
Obtain the access credentials that are required when you call an API operation. For more information, see Obtain an AccessKey pair or Obtain access credentials assigned by STS.

> **Note:** We recommend that you use the AccessKey pair of a personal account assigned by Resource Access Management (RAM) or an access credential assigned by Security Token Service (STS) to call the API operations of the Apsara Uni-manager Management Console and cloud services.

2. Obtain a region ID.
For more information about how to obtain a region ID, see Obtain the values of common header parameters.
3. Obtain an organization ID and a resource set ID.
Obtain an organization ID by calling the GetOrganizationList operation. For more information, see GetOrganizationList in Apsara Uni-manager Management Console Develop er Guide. Obtain a resource set ID by calling the ListResourceGroup operation. For more information, see ListResourceGroup in Apsara Uni-manager Management Console Developer Guide.

> **Note:** When you call an API operation, set the `<x-acs-organizationid>` header to the organization ID that you queried, and set the `<x-acs-resourcegroupid>` header to the resource set ID that you queried. This way, you can query resources in the specified organization and resource set.
> If you do not specify the `<x-acs-organizationid>` header, the organization to which the current user belongs is used by default.
> If you do not specify the `<x-acs-resourcegroupid>` header, this header is left empty by default. If you specify a resource set ID, you must also specify an organization ID.

4. Obtain the API references.
Obtain the developer guide of the cloud service that you want to use. You can learn the features of API operations and how to call the API operations. For more information, see Apsara Stack documentation.
5. Obtain the endpoint of the cloud service.
6. Obtain the service SDK and use the SDK to call the API operations of the service.

## 2 Preparations

### 2.1 Log on to the API Tool console

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

> **Note:** For more information, see the **Bind a virtual MFA device to enable** **MFA** topic in **Apsara Uni-manager Management Console User Guide** .

5. In the top navigation bar, choose **Products > Others > API Tool**.

### 2.2 Obtain API information

To call API operations by using an SDK, you must obtain information that includes service names, API operation names, and API versions.

**Background information**

The information on the API Directory page is for reference only. For more information about how to call API operations, see the developer guides of cloud services. If the information on the API Directory page is different from that in the developer guide of a cloud service, the information in the developer guide shall prevail.

**Procedure**

1. Log on to the API Tool console.
2. In the left-side navigation pane, click **API Directory**.
3. On the **API Directory** page, select the desired service from the Product Name drop-down
list and enter a keyword of an API operation name to search for the API operation.
4. View and record the service name, API operation name, and API version.

### 2.3 Obtain an AccessKey pair

An AccessKey pair that consists of an AccessKey ID and an AccessKey secret is used to implement symmetric encryption to verify the identity of a request sender. The AccessKey ID is used to identify a user. The AccessKey secret is used to encrypt a signature string. This topic describes how to obtain an AccessKey pair that is assigned by Resource Access Management (RAM).

**Prerequisites**

Only operations administrators and level-1 organization administrators can obtain the AccessKey pairs of organizations.

**Background information**

Access credentials can be assigned by RAM or Security Token Service (STS). RAM: assigns an AccessKey pair that consists of an AccessKey ID and an AccessKey secret. STS: assigns an access credential that consists of an AccessKey ID, an AccessKey secret, and a security token. This topic describes how to obtain an AccessKey pair that is assigned by RAM. For more information about how to obtain an access credential that is assigned by STS, see Obtain access credentials assigned by STS. We recommend that you use the AccessKey pairs of personal accounts to call the API operations of the Apsara Uni-manager Management Console and cloud services. If you use the AccessKey pair of a personal account, configure the header parameters that are described in the following table for access control. Otherwise, an error message that indicates insufficient permissions may appear.

| Parameter | Description |
|---|---|
| x-acs-regionid | The region ID. Example: cn-hangzhou-*. |
| x-acs-organizationid | The organization ID in the Apsara Uni-manager Management Console. For more information about how to obtain an organization ID, see the "GetOrganizationList" section in Apsara Uni- manager Management Console Developer Guide. |

| x-acs-resourcegroupid | The resource set ID in the Apsara Uni-manager Management Console. For more information about how to obtain a resource set ID, see the "ListResourceGroup" section in Apsara Uni- manager Management Console Developer Guide. |
|---|---|
| x-acs-instanceid | The ID of the instance that you want to manage. If you want to perform an operation on an Elastic Compute Service (ECS) instance, obtain the ECS instance ID from the ECS instance list. |

> **Warning:** The AccessKey pair of a personal account is managed and limited by the permission system of the Apsara Uni-manager Management Console. If you need to obtain the AccessKey pair of an organization, make sure that your operation is allowed by an administrator. This ensures security.

**Obtain the AccessKey pair of a personal account**

To obtain the AccessKey pair of a personal account, perform the following steps:
1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the page that appears, move the pointer over the profile
picture, and click **User Information**.
3. In the **AccessKey** section, view the AccessKey pair of your personal account.

> **Note:** The AccessKey pair provides full permissions on cloud resources within your account. You must keep the AccessKey pair confidential.

**Obtain the AccessKey pair of an organization**

To obtain the AccessKey pair of an organization, perform the following steps:
1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, click **Enterprise**.
3. In the left-side navigation pane, choose **Resources > Organizations**.
4. In the organization list, click the name of the level-1 organization whose AccessKey pair you
want to obtain.
5. On the right side of the page that appears, click **Management Accesskey**.
6. In the dialog box that appears, view the AccessKey pair of the organization.

### 2.4 Obtain the values of common header parameters

**header parameters**

You must provide multiple header parameters when you call API operations in Apsara Stack. This topic describes how to obtain the values of common header parameters. This topic also explains the response parameters that are returned after you call API operations.

**Obtain a region ID**

1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, click **Enterprise**.
3. In the left-side navigation pane, choose **Resources** > **Regions**.
4. Click the name of the desired organization.
5. View the region ID in the **Regions** section.

**Obtain an organization ID**

You can call the GetOrganizationList operation to obtain the organization ID. For more information, see GetOrganizationList in Apsara Uni-manager Management Console Developer Guide.

**Obtain a resource set ID**

You can call the ListResourceGroup operation to obtain the resource set ID. For more information, see ListResourceGroup in Apsara Uni-manager Management Console Developer Guide.

**Obtain an instance ID**

You can obtain the ID of an instance in a cloud service console of the Apsara Uni-manager Management Console. Perform the following steps to obtain the ID of an IPv6 gateway:
1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Products** > Networking > Virtual Private Cloud.
3. In the left-side navigation pane, click **IPv6 Gateways**.
4. View the **instance ID** in the instance list.

**Response parameters**

The following table describes the additional response parameters that are returned by default when you call API operations to query the instances of cloud services.

| Parameter | Description |
|---|---|
| ResourceGroupName | The name of the resource set. |
| ResourceGroup | The ID of the resource set. |
| DepartmentName | The name of the organization. |

| Department | The ID of the organization. |
|---|---|

### 2.5 Obtain access credentials assigned by STS

**assigned by STS**

This topic describes how to use Security Token Service (STS) to call API operations in Apsara Stack.

**Background information**

STS allows you to manage temporary access credentials for your Apsara Stack resources. You can use STS to call API operations in Apsara Stack. To call API operations in Apsara Stack by using STS, you must obtain an AccessKey ID, an AccessKey secret, and a security token assigned by STS. For more information about STS, see the "STS overview" topic in Common Content - Developer Guide.

**Procedure**

1. Obtain the Apsara Stack Resource Name (ARN) of your `RAM role` .
i. Log on to the Apsara Uni-manager Management Console. ii. Click the profile picture in the upper-right corner of the page that appears and click **User**
**Information**.
iii. Click **View Current Role Policy**. In the **View Policies of Current Role** dialog box, view the ARN of your `RAM role` .
2. Obtain the access credential assigned by STS.

> **Note:** You must replace the variables in the following code with actual values. Delete the angle brackets (<>) before you submit the code.
> The following section describes the variables.
> <yourRegionID>: Replace this variable with your region ID.
> <yourAccessKeyID>: Replace this variable with your AccessKey ID.
> <yourAccessKeySecret>: Replace this variable with your AccessKey secret.
> <yourRoleSessionName>: Replace this variable with the name of the current session.
> <yourRoleArn>: Replace this variable with the ARN of your RAM role.
> "sts.aliyuns.com": Replace this variable with the endpoint of STS.

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
    // Obtain the access credential assigned by STS.
    String stsAK = credentials.getString("AccessKeyId");
    String stsSK = credentials.getString("AccessKeySecret");
    String stsToken = credentials.getString("SecurityToken");
```

`}`

```java
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
```

`}`

```
    return null;
```

`}`
3. Use the access credential assigned by STS to call an API operation of a cloud service. The
following sample code provides an example on how to use the access credential assigned by STS to call the `DescribeZones` operation of Elastic Compute Service (ECS).

> **Note:** You must replace the variables in the following code with actual values. Delete the angle brackets (<>) before you submit the code.
> The following section describes the variables.
> <yourRegionID>: Replace this variable with your region ID.
> <yourStsAccesskeyID>: Replace this variable with your AccessKey ID.
> <yourStsAccessKeySecret>: Replace this variable with your AccessKey secret.
> <yourStsToken>. Replace this variable with your security token.
> <yourResourceGroupID>: Replace this variable with your resource set ID.
> <yourOrganizationID>: Replace this variable with your organization ID.

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

e API calls

## 3 Use POP to make API calls

### 3.1 Preparations

You can use the point of presence (POP) gateway to call API operations in Apsara Stack in the same way as in Alibaba Cloud public cloud. This topic describes the preparations before you use the POP gateway to call API operations.

**Background information**

In Apsara Stack, you can use both the Apsara Stack API (ASAPI) gateway and the POP gateway to call API operations. To enable you to use the API call method in Alibaba Cloud public cloud and have a more convenient and consistent experience, we recommend that you use the POP gateway to call Apsara Stack API operations.

**Obtain service endpoints**

To use the POP gateway to call API operations, you must use service endpoints. You can obtain service endpoints from Apsara Stack onsite O&M engineers. You can also obtain service endpoints by yourself. The following example describes how to obtain a service endpoint of IPv6 Gateway.
1. Log on to the Apsara Infrastructure Management console.
i. Log on to the Apsara Uni-manager Operations Console. ii. In the top navigation bar, choose **Products** > **Base/Cloud Platform** > **Apsara**
**Infrastructure Management Platform**.
2. In the left-side navigation pane, choose **O&M Tools** > **Basic Data Management** >
**Service Registration Variable Dashboard**.
3. On the Registration Variable Dashboard page, click **Advanced Filter**.
4. Enter `ipv6gateway` in the Service Registration field and click **Search**.
icon.
5. In the **Service Registration** column for the ipv6gateway service, click the
6. Click the text information in the **Service Registration** column of the `ipv6gateway`
service. In the **Register Variable** dialog box that appears, view the ipv6gateway.openapi.endpoint value, which is the `Endpoint` value.

**Obtain common parameters**

You must obtain the parameters required when you use the POP gateway to call API operations, such as the organization ID, resource set ID, region ID, and instance ID. For more information, see Obtain common header parameters.

### 3.2 SDK for Java

Before you use point of presence (POP) SDK for Java to make API calls, you must first understand the remote procedure call (RPC) and resource-oriented architecture (ROA) styles.

**Prerequisites**

An Alibaba Cloud SDK package is downloaded for the service that you want to access. The required dependencies are installed. SSL certificate validation is ignored for requests over HTTPS. e API calls

**Sample request**

The following sample code provides an example on how to use the RPC style to make an API call. In this example, the DescribeApiGroups operation of API Gateway is called, and the API version is 2016-07-14. Sample code:

```java
import com.aliyuncs.CommonRequest; import com.aliyuncs.CommonResponse; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.exceptions.ServerException; import com.aliyuncs.http.MethodType; import com.aliyuncs.profile.DefaultProfile; public class DescribeApiGroups {
    public static void main(String[] args) {
        // Create and initialize a DefaultAcsClient instance.
        DefaultProfile profile = DefaultProfile.getProfile("<your-regionid>", "
<yourAccessKeyId>", "<yourAccessSecret>");
        // Ignore SSL certificate validation.
        // HttpClientConfig clientConfig = HttpClientConfig.getDefault();
        // clientConfig.setIgnoreSSLCerts(true);
        // Specify the timeout period for a connection.
        // clientConfig.setConnectionTimeoutMillis(3000L);
        // Specify the read timeout period.
        // clientConfig.setReadTimeoutMillis(10000L);
        // profile.setHttpClientConfig(clientConfig);
        IAcsClient client = new DefaultAcsClient(profile);
        // Create an API request and configure the request parameters.
        CommonRequest request = new CommonRequest();
        // Specify the request method.
        request.setSysMethod(MethodType.POST);
        // Specify the service endpoint.
        request.setSysDomain("<apigatewayEndpoint>");
        // Specify the API version.
        request.setSysVersion("2016-07-14");
        // Specify the name of the service that you want to access and the region where
the service resides.
        request.setSysLocationProduct("apigateway");
        // Specify the name of the API operation.
        request.setSysAction("DescribeApiGroups");
        // When you use the Security Token Service (STS) AccessKey ID to call RPC API o
perations, you must add the SecurityToken parameter to the header.
        // request.putBodyParameter("SecurityToken", "<your-SecurityToken>");
        // Specify service-related parameters.
        request.putQueryParameter("PageSize", "10");
        request.putQueryParameter("PageNumber", "1");
```

e API calls

```java
        // Required. The call source.
        request.putHeadParameter("x-acs-caller-sdk-source", "ApiTestDemo");
        // Optional. This parameter is required for the Enterprise Edition V3.15.0 and
earlier versions.
        request.putHeadParameter("x-acs-regionid", "<your-regionid>");
        // Optional. The resource set ID.
        request.putHeadParameter("x-acs-resourcegroupid", "<your-resourcegroupid>");
        // Required. The organization ID.
        request.putHeadParameter("x-acs-organizationid", "<your-organizationid>");
        // Optional. This parameter is required for the modify and delete operations.
        // request.putHeadParameter("x-acs-instanceid", "<your-instanceid>");
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

`}` `}` `}` The following sample code provides an example on how to use the ROA style to make an API call. In this example, the GetNamespaceList operation of Container Registry is called, and the API version is 2016-06-07. Sample code:

```java
import com.aliyuncs.CommonRequest; import com.aliyuncs.CommonResponse; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.exceptions.ServerException; import com.aliyuncs.http.MethodType; import com.aliyuncs.profile.DefaultProfile; public class GetNamespaceList {
    public static void main(String[] args) {
        // Create and initialize a DefaultAcsClient instance.
        DefaultProfile profile = DefaultProfile.getProfile("<your-regionid>", "
<yourAccessKeyId>", "<yourAccessSecret>");
        // Ignore SSL certificate validation.
        // HttpClientConfig clientConfig = HttpClientConfig.getDefault();
        // clientConfig.setIgnoreSSLCerts(true);
        // Specify the timeout period for a connection.
        // clientConfig.setConnectionTimeoutMillis(3000L);
```

`//` e API calls

|   | // Specify the read timeout period. // clientConfig.setReadTimeoutMillis(10000L); // profile.setHttpClientConfig(clientConfig); IAcsClient client = new DefaultAcsClient(profile); // Create an API request and configure the request parameters. CommonRequest request = new CommonRequest(); // Specify the request protocol to HTTPS. request.setSysProtocol(ProtocolType.HTTP); // Specify the request method. request.setSysMethod(MethodType.GET); // Specify the service endpoint. request.setSysDomain("<crEndpoint>"); // Specify the API version. request.setSysVersion("2016-06-07"); // Specify the uriPattern parameter, which is required for the ROA style. request.setSysUriPattern("/namespace"); // Specify the name of the service that you want to access and the region where the service resides. request.setSysLocationProduct("cr"); // Specify the name of the API operation. request.setSysAction("GetNamespaceList"); // Required. The call source. request.putHeadParameter("x-acs-caller-sdk-source", "ApiTestDemo"); // Optional. This parameter is required for the Enterprise Edition V3.15.0 and earlier versions. request.putHeadParameter("x-acs-regionid", "<your-regionid>"); // Optional. The resource set ID. request.putHeadParameter("x-acs-resourcegroupid", "<your-resourcegroupid>"); // Required. The organization ID. request.putHeadParameter("x-acs-organizationid", "<your-organizationid>"); // Optional. This parameter is required for the modify and delete operations. // request.putHeadParameter("x-acs-instanceid", "<your-instanceid>"); // When you use the STS AccessKey ID to call ROA API operations, you must add t he x-acs-security-token parameter to the header. // request.putHeadParameter("x-acs-security-token", "<your-securitytoken>"); try { // Initiate the request and handle the response or exceptions. CommonResponse response = client.getCommonResponse(request); System.out.println(response.getData()); } catch (ServerException e) { e.printStackTrace(); } catch (ClientException e) { System.out.println("ErrCode:" + e.getErrCode()); System.out.println("ErrMsg:" + e.getErrMsg()); System.out.println("RequestId:" + e.getRequestId()); } } } |   |
|---|---|---|

e API calls

> **Important:** If you send a request over HTTPS, you must set the request to ignore SSL certificate validation.

### 3.3 SDK for Go

This topic describes how to use point of presence (POP) SDK for Go.

**Prerequisites**

An Alibaba Cloud SDK package is downloaded for the service that you want to access. The required dependencies are installed.

**Background information**

Both remote procedure call (RPC) and resource-oriented architecture (ROA) styles are supported for API calls.

**Sample request**

The following sample code provides an example on how to use the RPC style to make an API call. In this example, the DescribeApiGroups operation of API Gateway is called, and the API version is 2016-07-14. Sample code: e API calls

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
cessKey Secret>")
    request := requests.NewCommonRequest()
    request.Method = "POST"
    request.Domain = "<ApigatewayEndpoint>"
    request.Version = "2016-07-14"
    request.ApiName = "DescribeApiGroups"
    request.Product = "apigateway"
    // When you use the Security Token Service (STS) AccessKey ID to call RPC API opera
tions, you must add the SecurityToken parameter to the header.
    // request.QueryParams["SecurityToken"]="<your-SecurityToken>"
    // Required. The call source.
    request.Headers["x-acs-caller-sdk-source"] = "ApiTestDemo"
    // Optional. This parameter is required for the Enterprise Edition V3.15.0 and earl
ier versions.
    request.Headers["x-acs-regionid"] = "<your-RegionID>"
    // Optional. The resource set ID.
    request.Headers["x-acs-resourcegroupid"] = "<your-ResourceGroupID>"
    // Required. The organization ID.
    request.Headers["x-acs-organizationid"] = "<your-OrganizationID>"
    // Optional. This parameter is required for the modify and delete operations.
    // request.Headers["x-acs-instanceid"] = "<your-InstanceID>"
    response, err := client.ProcessCommonRequest(request)
    if err != nil {
        panic(err)
```

`}`

```
    fmt.Print(response.GetHttpContentString())
```

`}` The following sample code provides an example on how to use the ROA style to make an API call. In this example, the GetNamespaceList operation of Container Registry is called, and the API version is 2016-06-07. Sample code: e API calls

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
 // When you use the STS AccessKey ID to call ROA API operations, you must add the x-
acs-security-token parameter to the header.
 // request.Headers["x-acs-security-token"] = "<your-SecurityToken>"
 // Required. The call source.
 request.Headers["x-acs-caller-sdk-source"] = "ApiTestDemo"
    // Optional. This parameter is required for the Enterprise Edition V3.15.0 and earl
ier versions.
    request.Headers["x-acs-regionid"] = "<your-RegionID>"
    // Optional. The resource set ID.
    request.Headers["x-acs-resourcegroupid"] = "<your-ResourceGroupID>"
    // Required. The organization ID.
    request.Headers["x-acs-organizationid"] = "<your-OrganizationID>"
 // Optional. This parameter is required for the modify and delete operations.
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

**Configure proxies**

You can configure proxies in one of the following ways when you call API operations: Configure proxies by using environment variables. Specify the HTTP_PROXY and HTTPS_PROXY environment variables, or specify the NO_PROXY environment variable. Sample code: e API calls

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

`}` Configure proxies on the client. Sample code:

```
// The proxies that are configured on the client take precedence over those that are configured by using environment variables. client.SetHttpProxy("http://x.x.x.x:xxxx") // Configure the HTTP proxy. client.GetHttpProxy() // Query the HTTP proxy. client.SetHttpsProxy("https://x.x.x.x:xxxx") // Configure the HTTPS proxy. client.GetHttpsProxy() // Query the HTTPS proxy. client.SetNoProxy("127.0.0.1,localhost") // Configure the proxy whitelist. client.GetNoProxy() // Query the proxy whitelist.
```

### 3.4 SDK for Python

This topic describes how to use POP SDK for Python.

**Prerequisites**

An Alibaba Cloud SDK package is downloaded for the service that you want to access. The required dependencies are installed.

**Background information**

Only the remote procedure call (RPC) style is supported for API calls.

**Call examples**

The following sample code provides an example on how to make an API call. In this example, the DescribeInstances operation of Elastic Compute Service (ECS) is called, and the API version is 2014-05-26. Sample code:

```java
from aliyunsdkcore.client import AcsClient import os from aliyunsdkcore.request import CommonRequest
# Create an AcsClient object.
client = AcsClient(
    "<AccessKey ID>",
    "<AccessKey Secret>",
    "<your-RegionID>",
    timeout=1000,  # Set the timeout period.
    verify=False, # Ignore certificate validation. or verify='<The location where the c
ertificateisstored>'
```

e API calls

```
ertificate is stored.>'
```

);

```python
# Set the following parameters for the HTTPS request protocol:
# client.set_verify(False)
# os.environ["HTTPS_PROXY"] = "http://127.0.0.1:8080"
# os.environ["HTTP_PROXY"] = "http://127.0.0.1:8080"
def hello_ecs_instance():
    # Create a request and set the parameters.
    request = CommonRequest()
    # When you use the STS AccessKey ID to call RPC API operations, you must add the Se
curityToken parameter to the header.
    # params = {"PageSize":"10","PageNumber":"1","SecurityToken":"<your-
SecurityToken>"};
    params = {"PageSize":"10","PageNumber":"1"};
    request.set_body_params(params)
    headers = {
        # Required. The call source.
        "x-acs-caller-sdk-source":"ApiTestDemo",
        # Optional. For the historical versions before Enterprise Edition V3.15.0.
        "x-acs-regionid":"<your-RegionID>",
        # Optional. The resource set ID.
        "x-acs-resourcegroupid":"<your-ResourceGroupID>",
        # Required. The organization ID.
        "x-acs-organizationid":"<your-OrganizationID>"
        # Optional. For the modify and delete operations.
        # "x-acs-instanceid":"<your-InstanceID>"
```

`}`

```
    request.set_headers(headers)
    request.set_version("2014-05-26")
    request.set_action_name("DescribeInstances")
    request.set_endpoint("<ecsEndpoint>") // Replace ecsEndpoint with the real endpoint
```

`.`

```python
    request.set_product("Ecs")
    request.set_method("POST")
    # Initiate the API request and obtain the response.
    response = client.do_action_with_exception(request)
    print(response)
if __name__ == '__main__':
    print("Hello Aliyun OpenApi!")
    hello_ecs_instance()
```

**Configure proxies**

You can configure HTTP_PROXY and HTTPS_PROXY environment variables when you call API operations. Sample code: e API calls

```bash
# Configure the HTTPS proxy.
os.environ["HTTPS_PROXY"] = "http://x.x.x.x:xxxx"
# Configure the HTTP proxy.
os.environ["HTTP_PROXY"] = "https://x.x.x.x:xxxx"
```

## 4 API references

### 4.1 List of operations by function

The following table lists API operations available for use in IPv6 Gateway.

| API | Description |
|---|---|
| CreateIpv6Gateway | Creates an IPv6 gateway. |
| DescribeIpv6Gateways | Queries IPv6 gateways. |
| DescribeIpv6GatewayAttribute | Queries detailed information about an IPV6 gateway. |
| ModifyIpv6GatewayAttribute | Modifies the information about an IPv6 gateway. |
| ModifyIpv6GatewaySpec | Modifies the specification of an IPv6 gateway. |
| DeleteIpv6Gateway | Deletes an IPv6 gateway. |
| DescribeIpv6EgressOnlyRules | Queries egress-only rules. |
| CreateIpv6EgressOnlyRule | Adds an egress-only rule to an IPv6 address. |
| DeleteIpv6EgressOnlyRule | Deletes an egress-only rule. |
| AllocateIpv6InternetBandwidth | Purchases Internet bandwidth resources for an IPv6 address. |
| ModifyIpv6InternetBandwidth | Modifies the Internet bandwidth value of an IPv6 address. |
| DeleteIpv6InternetBandwidth | Sets the Internet bandwidth value of an IPv6 address to zero. |
| DescribeIpv6Addresses | Queries IPv6 addresses. |
| ModifyIpv6AddressAttribute | Modifies the name and description of an IPv6 address. |

### 4.2 Make API requests

#### 4.2.1 Request syntax

To call an IPv6 Gateway API operation, you must send an HTTP GET request to the endpoint of the IPv6 Gateway API. You must add the request parameters that correspond to the API operation being called. After you call the API operation, the system returns a response. Requests and responses are encoded in UTF-8. IPv6 Gateway API operations use the RPC protocol. You can call IPv6 Gateway API operations by sending HTTP GET requests. The following example shows the syntax of an IPv6 Gateway API request:

```
http://Endpoint/?Action=xx&Parameters
```

where:
**Endpoint**: the endpoint of the IPv6 Gateway API. The endpoint of the IPv6 Gateway API is

| vpc.example.com | . |
|---|---|
| Note example.com is a custom domain name. You can obtain the endpoint in the Apsara Uni-manager Operations Console. For more information, see Generate the ASAPI endpoint. |   |

**Action**: the name of the operation that you want to perform. For example, to query IPv6
gateways, you must set the Action parameter to DescribeIpv6Gateways.
**Version**: the version of the API that you want to call. The current IPv6 Gateway API version
is 2016-04-28.
**Parameters**: the request parameters for the operation. Separate multiple parameters with
ampersands (&). Request parameters include common parameters and operation-specific parameters. Common parameters include the API version and authentication information. For more information about common parameters, see common parameters. The following example demonstrates how to call the DescribeIpv6Gateways operation to query IPv6 gateways.

> **Note:** The sample requests are formatted to improve readability.

```
https://vpc.example.com/?Action=DescribeIpv6Gateways &Format=xml &Version=2016-04-28 &Signature=xxxx%xxxx%3D &SignatureMethod=HMAC-SHA1 &SignatureNonce=15215528852396 &SignatureVersion=1.0 &AccessKeyId=key-test &Timestamp=2012-06-01T12:00:00Z
```

#### 4.2.2 API authorization

To ensure the security of your account, we recommend that you call IPv6 Gateway API operations as a RAM user. To call the IPv6 Gateway API as a RAM user, you must create and add an authorization policy that grants permissions to call specific API operations. For more information about the IPv6 Gateway resources and API operations that allow the authorization, see RAM authentication.

#### 4.2.3 Sign an API request

You must sign all API requests to ensure security. Apsara Stack uses the request signature to verify the identity of the API caller. IPv6 Gateway implements symmetric encryption with an AccessKey pair to verify the identity of the request sender. An AccessKey pair is an identity credential issued to Apsara Stack accounts and RAM users that is similar to a logon username and password. An AccessKey pair consists of an AccessKey ID and an AccessKey secret. The AccessKey ID is used to verify the identity of the user, while the AccessKey secret is used to encrypt and verify the signature string. You must keep your AccessKey secret strictly confidential. For more information about how to create an AccessKey pair, see Obtain an AccessKey pair. You must add the signature to an RPC API request in the following format:

```
 https://endpoint/?SignatureVersion=1.0&SignatureMethod=HMAC-
SHA1&Signature=xxxx%xxxx%3D&SignatureNonce=3ee8c1b8-83d3-44af-a94f-4e0ad82fd6cf
```

In the DescribeIpv6Gateways example, if the AccessKey ID is `testid` and the AccessKey secret is `testsecret` , the request URL before signing is as follows:

```
http://vpc.example.com/?Action=DescribeIpv6Gateways &Timestamp=2016-02-23T12:46:24Z &Format=XML &AccessKeyId=testid &SignatureMethod=HMAC-SHA1 &SignatureNonce=3ee8c1b8-83d3-44af-a94f-4e0ad82fd6cf &Version=2016-04-28 &SignatureVersion=1.0
```

Perform the following operations to calculate the signature:
1. Create a string-to-sign using the request parameters:

```
GET&%2F&AccessKeyId%3Dtestid&Action%3DDescribeIpv6Gateways&Format%3DXML&SignatureMethod DHMAC-SHA1&SignatureNonce%3D3ee8c1b8-83d3-44af-a94f- 4e0ad82fd6cf&SignatureVersion%3D1.0&TimeStamp%3D2016-02- 23T12%253A46%253A24Z&Version%3D2016-04-28
```

2. Calculate the HMAC value of the string-to-sign.
Append an ampersand (&) to the end of the AccessKey secret as the key to calculate the HMAC value. In this example, the key is `testsecret&` .

```
CT9X0VtwR86fNWSnsc6v8YGOjuE=
```

3. Add signature to request parameters:

```
http://vpc.example.com/?Action=DescribeIpv6Gateways &Timestamp=2016-02-23T12:46:24Z &Format=XML &AccessKeyId=testid &SignatureMethod=HMAC-SHA1 &SignatureNonce=3ee8c1b8-83d3-44af-a94f-4e0ad82fd6cf &Version=2016-04-28 &SignatureVersion=1.0 &Signature=xxxx%xxxx%3D
```

### 4.3 RAM authentication

Before you call an IPv6 Gateway operation as a RAM user, you must use an Apsara Stack tenant account to create an authorization policy to grant permissions to the RAM user. In the authorization policy, an Alibaba Cloud Resource Name (ARN) is used to specify a resource.

**IPv6 Gateway resources that allow authorized access**

The following table lists the IPv6 Gateway resources that allow authorized access and their ARNs.

| Resource type | ARN |
|---|---|
| IPv6 gateways | acs:vpc:$regionid:$accountid:ipv6gateway/$ipv6gatewayid |
|   | acs:vpc:$regionid:$accountid:ipv6gateway/* |
|   | acs:vpc:*:$accountid:ipv6gateway/* |
| IPv6 Internet bandwidth | acs:vpc:$regionid:$accountid:ipv6bandwidth/$ipv6instanceid |
|   | acs:vpc:$regionid:$accountid:ipv6bandwidth/* |
|   | acs:vpc:*:$accountid:ipv6bandwidth/* |
| General resources | acs:vpc:$regionid:$accountid:* |
|   | acs:vpc:*:$accountid:* |

$regionid/accoutid/vrouterid are IDs of the specific resources, and `*` represents all resources.

**IPv6 Gateway API operations that allow authorized access**

The following table lists the IPv6 Gateway API operations that allow authorized access and their ARNs.

| API | ARN |   |   |
|---|---|---|---|
| CreateIpv6Gateway | acs:vpc:$regionid:$accountid:ipv6gateway/* |   |   |
|   | acs:vpc:$regionid:$accountid:ipv6gateway/$ipv6gatewayi d |   |   |
|   |   | acs:vpc:$regionid:$accountid:ipv6gateway/$ipv6gatewayi |   |
| DeleteIpv6Gateway | d |   |   |
| DescribeIpv6Gateways | acs:vpc:$regionid:$accountid:ipv6gateway/* |   |   |
|   | acs:vpc:$regionid:$accountid:ipv6gateway/$ipv6gatewayi d |   |   |
|   |   | acs:vpc:$regionid:$accountid:ipv6gateway/$ipv6gatewayi |   |
|   | d |   |   |
| AllocateIpv6InternetBandwidth | acs:vpc:$regionid:$accountid:ipv6bandwidth/* |   |   |
| CreateIpv6EgressOnlyRule | acs:vpc:$regionid:$accountid:ipv6gateway/* |   |   |
| DeleteIpv6EgressOnlyRule | acs:vpc:$regionid:$accountid:ipv6gateway/$ruleid |   |   |
|   | acs:vpc:$regionid:$accountid:ipv6bandwidth/$ipv6bandwi dthid |   |   |
|   |   | acs:vpc:$regionid:$accountid:ipv6bandwidth/$ipv6bandwi |   |
| DeleteIpv6InternetBandwidth | dthid |   |   |
| DescribeIpv6Addresses | acs:vpc:$regionid:$accountid:vpc/* |   |   |

| > Document Version: 20240516 | 2 |
|---|---|

|   | acs:vpc:$regionid:$accountid:ipv6gateway/$ipv6gatewayi d |   |   |
|---|---|---|---|
|   |   | acs:vpc:$regionid:$accountid:ipv6gateway/$ipv6gatewayi |   |
| DescribeIpv6EgressOnlyRules | d |   |   |
|   | acs:vpc:$regionid:$accountid:ipv6gateway/$ipv6gatewayi d |   |   |
|   |   | acs:vpc:$regionid:$accountid:ipv6gateway/$ipv6gatewayi |   |
| DescribeIpv6GatewayAttribute | d |   |   |
| ModifyIpv6AddressAttribute | acs:vpc:$regionid:$accountid:vpc/$ipv6instanceid |   |   |
|   | acs:vpc:$regionid:$accountid:ipv6gateway/$ipv6gatewayi d |   |   |
|   |   | acs:vpc:$regionid:$accountid:ipv6gateway/$ipv6gatewayi |   |
| ModifyIpv6GatewayAttribute | d |   |   |
|   | acs:vpc:$regionid:$accountid:ipv6gateway/$ipv6gatewayi d |   |   |
|   |   | acs:vpc:$regionid:$accountid:ipv6gateway/$ipv6gatewayi |   |
| ModifyIpv6GatewaySpec | d |   |   |
|   | acs:vpc:$regionid:$accountid:ipv6bandwidth/$ipv6instan ceid |   |   |
|   |   | acs:vpc:$regionid:$accountid:ipv6bandwidth/$ipv6instan |   |
| ModifyIpv6InternetBandwidth | ceid |   |   |

### 4.4 common parameters

This topic describes common parameters, including common request parameters and common response parameters. Common parameters are required by all API operations.

**Common request parameters**

Common request parameters must be included in all API requests. Table 1: Common request parameters

| Header | Type | Requi red | Description |
|---|---|---|---|
| Format | Strin g | No | The format in which to return the response. Valid values: JSON and XML. Default value: JSON. |
| Version | Strin g | Yes | The API version number, in the YYYY-MM-DD date format. Valid values: 2016-04-28 |
| AccessKeyId | Strin g | Yes | The AccessKey ID provided to you by Alibaba Cloud. |
| Signature | Strin g | Yes | The signature string of the current request. |
| SignatureMe thod | Strin g | Yes | The encryption method of the signature string. Set the value to HMAC-SHA1 |
| Timestamp | Strin g | Yes | The timestamp of the request. The time follows the ISO8601 standard in UTC. The format is YYYY-MM-DDThh:mm:ssZ . For example, use 2013-01-10T12:00:00Z to specify 20:00:00 on January 10, 2013 (UTC+8). |

| SignatureVer sion | Strin g | Yes | The version of the signature encryption algorithm. Set the value to 1.0 |
|---|---|---|---|
| SignatureNo nce | Strin g | Yes | A unique, random number that is used to prevent replay attacks. You must use a unique random number for each request. |

**Example**

```
http://vpc.example.com/?Action=DescribeIpv6Gateways &Timestamp=2016-02-23T12:46:24Z &Format=XML &AccessKeyId=testid &SignatureMethod=HMAC-SHA1 &SignatureNonce=3ee8c1b8-83d3-44af-a94f-4e0ad82fd6cf &Version=2016-04-28 &SignatureVersion=1.0
```

**Common response parameters**

API responses use the HTTP response format where a 2xx status code indicates a successful call and a 4xx or 5xx status code indicates a failed call. Responses can be returned in the JSON or XML format. You can specify the response format in the request. The default response format is XML. The system returns a unique identifier **RequestId** for each API call, regardless of whether the call is successful. XML format

```xml
<?xml version="1.0" encoding="utf-8"?>
      <!--Result root node-->
      <Operation name + Response>
      <!--Return Request Tag-->
      <RequestId>4C467B38-3910-447D-87BC-AC049166F216</RequestId>
      <!--Return Result Data-->
      </Interface Name+Response>
```

JSON format `{`

```json
      "RequestId":"4C467B38-3910-447D-87BC-AC049166F216",
      /*Returned data*/
```

`}`

### 4.5 IPv6 gateways

#### 4.5.1 CreateIpv6Gateway

Creates an IPv6 gateway.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateIpv6Gate way | The operation that you want to perform. Set the value to CreateIpv6Gateway. |
| RegionId | String | Yes | cn-neimeng- env133-d01 | The region ID of the IPv6 gateway. You can call the DescribeRegions operation to query the most recent region list. |
| VpcId | String | Yes | vpc- 123sedrfswd23* *** | The ID of the virtual private cloud (VPC) for which you want to create the IPv6 gateway. |
| Spec | String | No | Small | The specification of the IPv6 gateway. Valid values: Small (default): Free Edition Medium: Enterprise Edition Large: Enhanced Enterprise Edition The forwarding capacity of an IPv6 gateway varies based on the specification. |
| Name | String | No | ipv6GW | The name of the IPv6 gateway. The name must be 2 to 128 characters in length, and can contain letters, digits, underscores ( ), and _ hyphens (-). The name must start with a letter but cannot start with http:// or https:// . |
| Description | String | No | ipv6gatewayfor VPC1 | The description of the IPv6 gateway. The description must be 2 to 256 characters in length. It cannot start with http:// or https:// . |
| ClientToken | String | No | 123456 | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Ipv6GatewayId | String | ipv6gw- hp3y0l3ln89j8cdvf* *** | The ID of the IPv6 gateway. |
| RequestId | String | 0ED8D006-F706- 4D23-88ED- E11ED28DCAC | The ID of the request. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=CreateIpv6Gateway &RegionId=cn-neimeng-env133-d01 &VpcId=vpc-123sedrfswd23**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<CreateIpv6GatewayResponse>
        <RequestId>0ED8D006-F706-4D23-88ED-E11ED28DCAC0</RequestId>
        <Ipv6GatewayId>ipv6gw-hp3y0l3ln89j8cdvf****</Ipv6GatewayId>
</CreateIpv6GatewayResponse>
```

`JSON` format `{`

```json
    "RequestId": "0ED8D006-F706-4D23-88ED-E11ED28DCAC0",
    "Ipv6GatewayId": "ipv6gw-hp3y0l3ln89j8cdvf****"
```

`}`

**Error codes**

| HttpCod e | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidRegionId.Not Found | The specified RegionId does not exist in our records. | The error message returned because the specified region ID does not exist. |
| 404 | InvalidVpcId.NotFo und | Specified VPC does not exist. | The error message returned because the specified VPC does not exist. |

#### 4.5.2 DescribeIpv6Gateways

Queries IPv6 gateways in a specified region.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeIpv6Gat eways | The operation that you want to perform. Set the value to DescribeIpv6GateWays. |
| RegionId | String | Yes | cn-neimeng- env133-d01 | The region ID of the IPv6 gateway. You can call the DescribeRegions operation to query the most recent region list. |
| Ipv6GatewayId | String | No | ipv6gw- 123456**** | The ID of the IPv6 gateway. |
| VpcId | String | No | vpc-123456**** | The ID of the virtual private cloud (VPC) to which the IPv6 gateway belongs. |
| Name | String | No | ipv6GW**** | The name of the IPv6 gateway. |
| PageNumber | Integer | No | 1 | The number of the page to return. |
| PageSize | Integer | No | 10 | The number of entries to return on each page. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Ipv6Gateways | Array of Ipv6Gateway |   | The details about the IPv6 gateways. |
| Ipv6Gateway |   |   |   |
| BusinessStatu s | String | Normal | The status of the IPv6 gateway. Valid values: Normal: normal FinancialLocked: locked due to overdue payments |
| CreationTime | String | 2020-12- 20T14:51:23Z | The time when the IPv6 gateway was created. |
| Description | String | descriptionforIPv6 GW | The description of the IPv6 gateway. |

| ExpiredTime | String | 2020-12- 21T14:51:23Z | The time when the IPv6 gateway expires. |
|---|---|---|---|
| InstanceCharg eType | String | PostPaid | The metering method of the IPv6 gateway. |
| Ipv6GatewayId | String | ipv6gw- hp3rwmtmfhgis*** * | The ID of the IPv6 gateway. |
| Name | String | name | The name of the IPv6 gateway. |
| RegionId | String | cn-neimeng- env133-d01 | The region ID of the IPv6 gateway. |
| Spec | String | Small | The specification of the IPv6 gateway. Small: Free Edition Medium: Enterprise Edition Large: Enhanced Enterprise Edition |
| Status | String | Available | The status of the IPv6 gateway. |
| VpcId | String | vpc-123456**** | The ID of the VPC to which the IPv6 gateway belongs. |
| PageNumber | Integer | 1 | The number of the returned page. |
| PageSize | Integer | 19 | The number of entries returned per page. |
| RequestId | String | E3A06196-3E7C- 490D-8F39- CB4B5A0CE8AD | The ID of the request. |
| TotalCount | Integer | 2 | The total number of entries returned. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeIpv6Gateways &RegionId=cn-neimeng-env133-d01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeIpv6GatewaysResponse>
   <PageNumber>1</PageNumber>
   <Ipv6Gateways>
      <Ipv6Gateway>
         <Name></Name>
         <CreationTime>2018-12-20T14:51:23Z</CreationTime>
         <Status>Available</Status>
         <Description></Description>
         <BusinessStatus>Normal</BusinessStatus>
         <Spec>Medium</Spec>
         <RegionId>cn-huhehaote</RegionId>
         <InstanceChargeType>PostPaid</InstanceChargeType>
         <ExpiredTime></ExpiredTime>
         <VpcId>vpc-hp3ag7ydchedxxxxxxxxx</VpcId>
         <Ipv6GatewayId>ipv6gw-hp33of4uz4k4kxxxxxxxx</Ipv6GatewayId>
      </Ipv6Gateway>
      <Ipv6Gateway>
         <CreationTime>2018-12-05T09:21:35Z</CreationTime>
         <Name>IPv6 gateway</Name>
         <Status>Available</Status>
         <Description></Description>
         <BusinessStatus>Normal</BusinessStatus>
         <Spec>Medium</Spec>
         <RegionId>cn-huhehaote</RegionId>
         <InstanceChargeType>PostPaid</InstanceChargeType>
         <ExpiredTime></ExpiredTime>
         <VpcId>vpc-hp3kzilwd9yflxxxxxxxx</VpcId>
         <Ipv6GatewayId>ipv6gw-hp33p10bdbt77xxxxxxxx</Ipv6GatewayId>
      </Ipv6Gateway>
   </Ipv6Gateways>
   <TotalCount>2</TotalCount>
   <PageSize>10</PageSize>
   <RequestId>E3A06196-3E7C-490D-8F39-CB4B5A0CE8AD</RequestId>
</DescribeIpv6GatewaysResponse>
```

`JSON` format `{`

```json
    "PageNumber": 1,
    "Ipv6Gateways": {
        "Ipv6Gateway": [
```

`{`

```json
                "Name": "",
                "CreationTime": "2018-12-20T14:51:23Z",
                "Status": "Available",
                "Description": "",
                "BusinessStatus": "Normal",
                "Spec": "Medium",
                "RegionId": "cn-huhehaote",
                "InstanceChargeType": "PostPaid",
                "ExpiredTime": "",
                "VpcId": "vpc-hp3ag7ydchedxxxxxxxxx",
                "Ipv6GatewayId": "ipv6gw-hp33of4uz4k4kxxxxxxxx"
```

`},` `{`

```json
                "CreationTime": "2018-12-05T09:21:35Z",
                "Name": "IPv6 gateway",
                "Status": "Available",
                "Description": "",
                "BusinessStatus": "Normal",
                "Spec": "Medium",
                "RegionId": "cn-huhehaote",
                "InstanceChargeType": "PostPaid",
                "ExpiredTime": "",
                "VpcId": "vpc-hp3kzilwd9yflxxxxxxxx",
                "Ipv6GatewayId": "ipv6gw-hp33p10bdbt77xxxxxxxx"
```

`}` `]` `},`

```json
    "TotalCount": 2,
    "PageSize": 10,
    "RequestId": "E3A06196-3E7C-490D-8F39-CB4B5A0CE8AD"
```

`}`

#### 4.5.3 DescribeIpv6GatewayAttribute

Queries detailed information about a specified IPv6 gateway.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeIpv6Gat ewayAttribute | The operation that you want to perform. Set the value to DescribeIpv6GatewayAttribute. |

| Ipv6GatewayId | String | Yes | ipv6gw- 123456**** | The ID of the IPv6 gateway that you want to query. |
|---|---|---|---|---|
| RegionId | String | Yes | cn-neimeng- env133-d01 | The region ID of the IPv6 gateway. You can call the DescribeRegions operation to query the most recent region list. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| BusinessStatu s | String | Normal | The status of the IPv6 gateway. Valid values: Normal: normal FinacialLocked: locked due to overdue payments SecurityLocked: locked due to security reasons |
| CreationTime | String | 2020-12- 05T09:21:35Z | The time when the IPv6 gateway was created. |
| Description | String | test | The description of the IPv6 gateway. |
| ExpiredTime | String | 2020-12- 06T09:21:35Z | The time when the IPv6 gateway expires. |
| InstanceCharg eType | String | PostPaid | The metering method of the IPv6 gateway. |
| Ipv6GatewayId | String | ipv6gw-123456**** | The ID of the IPv6 gateway. |
| Name | String | test | The name of the IPv6 gateway. |
| RegionId | String | cn-neimeng- env133-d01 | The region ID of the IPv6 gateway. |
| RequestId | String | E3A06196-3E7C- 490D-8F39- CB4B5A0CE8AD | The ID of the request. |
| Spec | String | Small | The specification of the IPv6 gateway. Small: Free Edition Medium: Enterprise Edition Large: Enhanced Enterprise Edition |
| Status | String | Available | The status of the IPv6 gateway. |

| VpcId | String | vpc-123456**** | The ID of the virtual private cloud (VPC) to which the IPv6 gateway belongs. |
|---|---|---|---|

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeIpv6GatewayAttribute &Ipv6GatewayId=ipv6gw-123456**** &RegionId=cn-neimeng-env133-d01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeIpv6GatewayAttributeResponse>
  <Status>Available</Status>
  <Description>test</Description>
  <RequestId>E3A06196-3E7C-490D-8F39-CB4B5A0CE8AD</RequestId>
  <InstanceChargeType>PostPaid</InstanceChargeType>
  <Ipv6GatewayId>ipv6gw-123456****</Ipv6GatewayId>
  <BusinessStatus>Normal</BusinessStatus>
  <Name>test</Name>
  <VpcId>vpc-123456****</VpcId>
  <ExpiredTime>2020-12-06T09:21:35Z</ExpiredTime>
  <CreationTime>2020-12-05T09:21:35Z</CreationTime>
  <RegionId>cn-neimeng-env133-d01</RegionId>
  <Spec>Small</Spec>
</DescribeIpv6GatewayAttributeResponse>
```

`JSON` format `{`

```json
    "Status": "Available",
    "Description": "test",
    "RequestId": "E3A06196-3E7C-490D-8F39-CB4B5A0CE8AD",
    "InstanceChargeType": "PostPaid",
    "Ipv6GatewayId": "ipv6gw-123456****",
    "BusinessStatus": "Normal",
    "Name": "test",
    "VpcId": "vpc-123456****",
    "ExpiredTime": "2020-12-06T09:21:35Z",
    "CreationTime": "2020-12-05T09:21:35Z",
    "RegionId": "cn-neimeng-env133-d01",
    "Spec": "Small"
```

`}`

**Error codes**

| HttpCod e | Error code | Error message | Description |
|---|---|---|---|

| 404 | InvalidRegionId.Not Found | The specified RegionId does not exist in our records. | The error message returned because the specified region ID does not exist. |
|---|---|---|---|

#### 4.5.4 ModifyIpv6GatewayAttribute

Modifies the name and description of an IPv6 gateway.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyIpv6Gate wayAttribute | The operation that you want to perform. Set the value to ModifyIpv6GatewayAttribute. |
| Ipv6GatewayId | String | Yes | ipv6gw- hp39kh1ya51yz p2lu**** | The ID of the IPv6 gateway that you want to modify. |
| RegionId | String | Yes | cn-neimeng- env133-d01 | The region ID of the IPv6 gateway. You can call the DescribeRegions operation to query the most recent region list. |
| Name | String | No | ipv6name | The new name of the IPv6 gateway. |
| Description | String | No | ipv6description | The new description of the IPv6 gateway. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 9DFEDBEE-E5AB- 49E8-A2DC- CC114C67AF75 | The ID of the request. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=ModifyIpv6GatewayAttribute &Ipv6GatewayId=ipv6gw-hp39kh1ya51yzp2lu**** &RegionId=cn-neimeng-env133-d01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ModifyIpv6GatewayAttributeResponse>
   <RequestId>9DFEDBEE-E5AB-49E8-A2DC-CC114C67AF75</RequestId>
</ModifyIpv6GatewayAttributeResponse>
```

`JSON` format `{`

```json
 "RequestId": "9DFEDBEE-E5AB-49E8-A2DC-CC114C67AF75"
```

`}`

**Error codes**

| HttpCod e | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidRegionId.Not Found | The specified RegionId does not exist in our records. | The error message returned because the specified region ID does not exist. |

#### 4.5.5 ModifyIpv6GatewaySpec

Changes the specification of an IPv6 gateway. The forwarding capacity and bandwidth of an IPv6 gateway vary based on the specification.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyIpv6Gate waySpec | The operation that you want to perform. Set the value to ModifyIpv6GatewaySpec. |
| Ipv6GatewayId | String | Yes | ipv6gw- 123456**** | The ID of the IPv6 gateway. |
| RegionId | String | Yes | cn-neimeng- env133-d01 | The region ID of the IPv6 gateway. You can call the DescribeRegions operation to query the most recent region list. |
| Spec | String | Yes | Small | The new specification that you want to set for the IPv6 gateway. Valid values: Small (default): Free Edition Middle: Enterprise Edition Large: Enhanced Enterprise Edition |

| ClientToken | String | No | 0c593ea1-3bea- 11e9-b96b- 88e9fe637760 | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |
|---|---|---|---|---|

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 9DFEDBEE-E5AB- 49E8-A2DC- CC114C67AF75 | The ID of the request. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=ModifyIpv6GatewaySpec &Ipv6GatewayId=ipv6gw-123456**** &RegionId=cn-neimeng-env133-d01 &Spec=Small &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ModifyIpv6GatewaySpecResponse>
   <RequestId>9DFEDBEE-E5AB-49E8-A2DC-CC114C67AF75</RequestId>
</ModifyIpv6GatewaySpecResponse>
```

`JSON` format `{`

```json
 "RequestId": "9DFEDBEE-E5AB-49E8-A2DC-CC114C67AF75"
```

`}`

**Error codes**

| HttpCod e | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidRegionId.Not Found | The specified RegionId does not exist in our records. | The error message returned because the specified region ID does not exist. |

#### 4.5.6 DeleteIpv6Gateway

Deletes an IPv6 gateway. Before you delete an Enterprise Edition or Enhanced Enterprise Edition IPv6 gateway, you must delete the egress-only rules configured on the IPv6 gateway.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteIpv6Gate way | The operation that you want to perform. Set the value to DeleteIpv6Gateway. |
| Ipv6GatewayId | String | Yes | ipv6gw- hp3y0l3ln89j8** ** | The ID of the IPv6 gateway that you want to delete. |
| RegionId | String | Yes | cn-neimeng- env133-d01 | The region ID of the IPv6 gateway. You can call the DescribeRegions operation to query the most recent region list. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | E9A8AABE-A84B- 4AF2-A68A- 8E2EA190E7AE | The ID of the request. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DeleteIpv6Gateway &Ipv6GatewayId=ipv6gw-hp3y0l3ln89j8**** &RegionId=cn-neimeng-env133-d01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DeleteIpv6GatewayResponse>
      <RequestId>E9A8AABE-A84B-4AF2-A68A-8E2EA190E7AE</RequestId>
</DeleteIpv6GatewayResponse>
```

`JSON` format `{`

```json
 "RequestId": "E9A8AABE-A84B-4AF2-A68A-8E2EA190E7AE"
```

**Error codes**

| HttpCod e | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidRegionId.Not Found | The specified RegionId does not exist in our records. | The error message returned because the specified region ID does not exist. |

#### 4.5.7 DescribeIpv6EgressOnlyRules

Queries egress-only rules.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeIpv6Egr essOnlyRules | The operation that you want to perform. Set the value to DescribeIpv6EgressOnlyRules. |
| Ipv6GatewayId | String | Yes | ipv6gw- 123456**** | The ID of the IPv6 gateway. |
| RegionId | String | Yes | cn-neimeng- env133-d01 | The region ID of the IPv6 gateway. You can call the DescribeRegions operation to query the most recent region list. |
| Ipv6EgressOnlyR uleId | String | No | ipv6gwpy- 123456**** | The ID of the egress-only rule that you want to query. |
| Name | String | No | rulename | The name of the egress-only rule. |
| InstanceType | String | No | Ipv6Address | The type of the instance to which the egress-only rule applies. Set the value to: Ipv6Address, which specifies that the egress-only rule applies to an IPv6 address. |
| InstanceId | String | No | i-123456**** | The ID of the Elastic Compute Service (ECS) instance that is associated with the IPv6 address to which the egress-only rule applies. |

| PageNumber | Integer | No | 1 | The number of the page to return. Default value: 1. |
|---|---|---|---|---|
| PageSize | Integer | No | 10 | The number of entries to return on each page. Maximum value: 50. Default value: 10. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Ipv6EgressOnl yRules | Array of Ipv6EgressOnl yRule |   | The details about the egress-only rules. |
| Ipv6EgressOnl yRule |   |   |   |
| Description | String | ruledescription | The description of the egress-only rule. |
| InstanceId | String | i-123456**** | The ID of the instance to which the egress- only rule applies. |
| InstanceType | String | Ipv6Address | The type of the instance to which the egress-only rule applies. |
| Ipv6EgressOnl yRuleId | String | ipv6gwpy- 123456**** | The ID of the egress-only rule. |
| Name | String | rulename | The name of the egress-only rule. |
| Status | String | Available | The status of the egress-only rule. |
| PageNumber | Integer | 1 | The number of the returned page. Default value: 1. |
| PageSize | Integer | 10 | The number of entries returned on each page. Maximum value: 50. Default value: 10. |
| RequestId | String | E16671B7-DEA6- 48E0-8E9C- 41913DAD44DD | The ID of the request. |
| TotalCount | Integer | 1 | The number of entries returned. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeIpv6EgressOnlyRules &Ipv6GatewayId=ipv6gw-123456**** &RegionId=cn-neimeng-env133-d01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeIpv6EgressOnlyRulesResponse>
  <TotalCount>1</TotalCount>
  <PageSize>10</PageSize>
  <RequestId>E16671B7-DEA6-48E0-8E9C-41913DAD44DD</RequestId>
  <PageNumber>1</PageNumber>
  <Ipv6EgressOnlyRules>
        <Status>Available</Status>
        <Ipv6EgressOnlyRuleId>ipv6gwpy-123456****</Ipv6EgressOnlyRuleId>
        <Description>ruledescription</Description>
        <InstanceId>i-123456****</InstanceId>
        <InstanceType>Ipv6Address</InstanceType>
        <Name>rulename</Name>
  </Ipv6EgressOnlyRules>
</DescribeIpv6EgressOnlyRulesResponse>
```

`JSON` format `{`

```json
    "TotalCount": 1,
    "PageSize": 10,
    "RequestId": "E16671B7-DEA6-48E0-8E9C-41913DAD44DD",
    "PageNumber": 1,
    "Ipv6EgressOnlyRules": {
        "Status": "Available",
        "Ipv6EgressOnlyRuleId": "ipv6gwpy-123456****",
        "Description": "ruledescription",
        "InstanceId": "i-123456****",
        "InstanceType": "Ipv6Address",
        "Name": "rulename"
```

`}` `}`

#### 4.5.8 CreateIpv6EgressOnlyRule

Creates an egress-only rule for an IPv6 address.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|

| Action | String | Yes | CreateIpv6Egres sOnlyRule | The operation that you want to perform. Set the value to CreateIpv6EgressOnlyRule. |
|---|---|---|---|---|
| InstanceId | String | Yes | ipv6- hp3nxjkfxn5pnh gl5**** | The ID of the IPv6 address to which you want to apply the egress-only rule. |
| Ipv6GatewayId | String | Yes | ipv6gw- hp3c2paq0ywau asza**** | The ID of the IPv6 gateway. |
| RegionId | String | Yes | cn-neimeng- env133-d01 | The region ID of the IPv6 gateway. You can call the DescribeRegions operation to query the most recent region list. |
| InstanceType | String | No | IPv6Address | The type of the instance to which you want to apply the egress-only rule. Set the value to: Ipv6Address (default): an IPv6 address. |
| Name | String | No | rulename | The name of the egress-only rule. The name must be 2 to 128 characters in length, and can contain letters, digits, underscores ( ), and _ hyphens (-). The name must start with a letter but cannot start with http:// or https:// . |
| Description | String | No | ruledescription | The description of the egress-only rule. The description must be 2 to 256 characters in length. It cannot start with http:// or https:// . |
| ClientToken | String | No | 0c593ea1-3bea- 11e9-b96b- 88e9fe637760 | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|

| Ipv6EgressRul eId | String | ipv6py- hp3w98rmlbqp012 45**** | The ID of the egress-only rule. |
|---|---|---|---|
| RequestId | String | 9DFEDBEE-E5AB- 49E8-A2DC- CC114C67AF75 | The ID of the request. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=CreateIpv6EgressOnlyRule &InstanceId=ipv6-hp3nxjkfxn5pnhgl5**** &Ipv6GatewayId=ipv6gw-hp3c2paq0ywauasza**** &RegionId=cn-neimeng-env133-d01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<CreateIpv6EgressOnlyRuleResponse>
      <RequestId>9DFEDBEE-E5AB-49E8-A2DC-CC114C67AF75</RequestId>
      <Ipv6EgressRuleId>ipv6py-hp3w98rmlbqp01245****</Ipv6EgressRuleId>
</CreateIpv6EgressOnlyRuleResponse>
```

`JSON` format `{`

```json
    "Ipv6EgressRuleId": "ipv6py-hp3w98rmlbqp01245****",
    "RequestId": "9DFEDBEE-E5AB-49E8-A2DC-CC114C67AF75"
```

`}`

**Error codes**

| HttpCod e | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidRegionId.Not Found | The specified RegionId does not exist in our records. | The error message returned because the specified region ID does not exist. |

#### 4.5.9 DeleteIpv6EgressOnlyRule

Deletes an egress-only rule.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|

| Action | String | Yes | DeleteIpv6Egres sOnlyRule | The operation that you want to perform. Set the value to DeleteIpv6EgressOnlyRule. |
|---|---|---|---|---|
| Ipv6EgressOnlyR uleId | String | Yes | ipv6py- hp3w98rmlbqp0 **** | The ID of the egress-only rule that you want to delete. |
| RegionId | String | Yes | cn-neimeng- env133-d01 | The ID of the IPv6 gateway. |
| ClientToken | String | No | 0c593ea1-3bea- 11e9-b96b- 88e9fe637760 | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 9DFEDBEE-E5AB- 49E8-A2DC- CC114C67AF75 | The ID of the request. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DeleteIpv6EgressOnlyRule &Ipv6EgressOnlyRuleId=ipv6py-hp3w98rmlbqp0**** &RegionId=cn-neimeng-env133-d01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DeleteIpv6EgressOnlyRuleResponse>
   <RequestId>9DFEDBEE-E5AB-49E8-A2DC-CC114C67AF75</RequestId>
</DeleteIpv6EgressOnlyRuleResponse>
```

`JSON` format `{`

```json
 "RequestId": "4E40EAF1-783D-4C05-948D-DA0426C398C1"
```

#### 4.5.10 AllocateIpv6InternetBandwidth

Purchases Internet bandwidth resources for an IPv6 address.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | AllocateIpv6Inte rnetBandwidth | The operation that you want to perform. Set the value to AllocateIpv6InternetBandwidth. |
| Bandwidth | Integer | Yes | 2 | The Internet bandwidth resources that you want to purchase for the IPv6 address. Unit: Mbit/s. Valid values: 1 to 5000. If InternetChargeType is set to PayByBandwidth, valid values are 1 to 5000. If InternetChargeType is set to PayByTraffic, valid values vary based on the specification of the IPv6 gateway. Small (default) specifies the Free Edition and the valid values are 1 to 500. Medium specifies the Enterprise Edition and the valid values are 1 to 1000. Large specifies the Enterprise Enhanced Edition and the valid values are 1 to 2000. |
| Ipv6AddressId | String | Yes | ipv6-123456**** | The ID of the IPv6 address for which the Internet bandwidth resources are purchased. |
| Ipv6GatewayId | String | Yes | ipv6gw- 123456**** | The ID of the IPv6 gateway. |
| RegionId | String | Yes | cn-neimeng- env133-d01 | The region ID of the IPv6 gateway. You can call the DescribeRegions operation to query the most recent region list. |
| InternetChargeT ype | String | No | PayByTraffic | The metering method of the Internet bandwidth resources of the IPv6 gateway. Valid values: PayByTraffic: pay-by-data- transfer PayByBandwidth (default): pay- by-bandwidth |

| ClientToken | String | No | 0c593ea1-3bea- 11e9-b96b- 88e9fe637760 | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |
|---|---|---|---|---|

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| InternetBandw idthId | String | 2 | The Internet bandwidth resources that you purchased. Unit: Mbit/s. |
| Ipv6AddressId | String | ipv6-123456**** | The ID of the IPv6 address for which the Internet bandwidth resources were purchased. |
| RequestId | String | 6972A26E-99B1- 4367-9890- FBDEBB0F5E7D | The ID of the request. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=AllocateIpv6InternetBandwidth &Bandwidth=2 &Ipv6AddressId=ipv6-123456**** &Ipv6GatewayId=ipv6gw-123456**** &RegionId=cn-neimeng-env133-d01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<AllocateIpv6InternetBandwidthResponse>
  <RequestId>6972A26E-99B1-4367-9890-FBDEBB0F5E7D</RequestId>
  <InternetBandwidthId>2</InternetBandwidthId>
  <Ipv6AddressId>ipv6-123456****</Ipv6AddressId>
</AllocateIpv6InternetBandwidthResponse>
```

`JSON` format `{`

```json
    "RequestId": "6972A26E-99B1-4367-9890-FBDEBB0F5E7D",
    "InternetBandwidthId": 2,
    "Ipv6AddressId": "ipv6-123456****"
```

`}`

**Error codes**

| HttpCod e | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidRegionId.Not Found | The specified RegionId does not exist in our records. | The error message returned because the specified region ID does not exist. |

#### 4.5.11 ModifyIpv6AddressAttribute

Modifies the name and description of an IPv6 address.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyIpv6Addre ssAttribute | The operation that you want to perform. Set the value to ModifyIpv6AddressAttribute. |
| Ipv6AddressId | String | Yes | ipv6- hp32vv2klzw4ye rdf**** | The ID of the IPv6 address that you want to modify. |
| RegionId | String | Yes | cn-neimeng- env133-d01 | The region ID of the IPv6 address. You can call the DescribeRegions operation to query the most recent region list. |
| Name | String | No | test | The new name of the IPv6 address. The name must be 2 to 128 characters in length, and can contain letters, digits, underscores ( ), and _ hyphens (-). The name must start with a letter, but cannot start with http:// or https:// . |

| Description | String | No | test | The new description of the IPv6 address. The description must be 2 to 256 characters in length. It cannot start with http:// or https:// . |
|---|---|---|---|---|

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | D560AF68-4CE8- 4A5C-B3FE- 469F558094D0 | The ID of the request. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=ModifyIpv6AddressAttribute &Ipv6AddressId=ipv6-hp32vv2klzw4yerdf**** &RegionId=cn-neimeng-env133-d01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ModifyIpv6AddressAttributeResponse>
   <RequestId>D560AF68-4CE8-4A5C-B3FE-469F558094D0</RequestId>
</ModifyIpv6AddressAttributeResponse>
```

`JSON` format `{`

```json
 "RequestId": "D560AF68-4CE8-4A5C-B3FE-469F558094D0"
```

`}`

**Error codes**

| HttpCod e | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidRegionId.Not Found | The specified RegionId does not exist in our records. | The error message returned because the specified region ID does not exist. |

#### 4.5.12 DeleteIpv6InternetBandwidth

Sets the Internet bandwidth value of an IPv6 address to zero.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteIpv6Intern etBandwidth | The operation that you want to perform. Set the value to DeleteIpv6InternetBandwidth. |
| RegionId | String | Yes | cn-neimeng- env133-d01 | The region ID of the IPv6 gateway. You can call the DescribeRegions operation to query the most recent region list. |
| Ipv6AddressId | String | No | ipv6-123456**** | The ID of the IPv6 address whose Internet bandwidth value you want to set to zero. |
| Ipv6InternetBan dwidthId | String | No | 2 | The Internet bandwidth value of the IPv6 address. Unit: Mbit/s. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | E07E0FE6-5C21- 405F-AF82- 7613AA81EF92 | The ID of the request. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DeleteIpv6InternetBandwidth &RegionId=cn-neimeng-env133-d01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DeleteIpv6InternetBandwidthResponse>
   <RequestId>6972A26E-99B1-4367-9890-FBDEBB0F5E7D</RequestId>
</DeleteIpv6InternetBandwidthResponse>
```

`JSON` format `{`

```json
 "RequestId": "E07E0FE6-5C21-405F-AF82-7613AA81EF92"
```

`}`

**Error codes**

| HttpCod e | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidRegionId.Not Found | The specified RegionId does not exist in our records. | The error message returned because the specified region ID does not exist. |

#### 4.5.13 DescribeIpv6Addresses

Queries the IPv6 addresses in a specified region.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeIpv6Ad dresses | The operation that you want to perform. Set the value to DescribeIpv6Addresses. |
| RegionId | String | Yes | cn-neimeng- env133-d01 | The region ID of the IPv6 address. You can call the DescribeRegions operation to query the most recent region list. |
| Ipv6AddressId | String | No | ipv6- n2yrzmwjz2uj3s 7j5**** | The ID of the IPv6 address. You can specify up to 20 IDs in each call. Separate multiple IDs with commas (,). |
| Ipv6Address | String | No | 2408:XXXX:180: 1701:94c7:bc38 :3bfa:d2c | The IPv6 address that you want to query. |
| Name | String | No | test | The name of the IPv6 address. |
| AssociatedInstan ceId | String | No | i-123456**** | The ID of the instance that is assigned the IPv6 address. |
| AssociatedInstan ceType | String | No | EcsInstance | The type of the instance that is assigned the IPv6 address. Set the value to EcsInstance: an Elastic Compute Service (ECS) instance in a virtual private cloud (VPC). This is the default value. |

| NetworkType | String | No | Public | The type of connection supported by the IPv6 address. Valid values: Private: communication within the private network Public: communication over the Internet |
|---|---|---|---|---|
| VpcId | String | No | vpc- hp325kt6307*** * | The ID of the VPC to which the IPv6 address belongs. |
| VSwitchId | String | No | vsw-123456**** | The ID of the vSwitch to which the IPv6 address belongs. |
| Ipv6InternetBan dwidthId | String | No | 1 | The Internet bandwidth value of the IPv6 address. Unit: Mbit/s. |
| PageNumber | Integer | No | 1 | The number of the page to return. Default value: 1. |
| PageSize | Integer | No | 10 | The number of entries to return on each page. Maximum value: 50. Default value: 10. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Ipv6Addresses | Array of Ipv6Address |   | The details about the IPv6 addresses. |
| Ipv6Address |   |   |   |
| AllocationTime | String | 2020-12- 20T14:56:09Z | The time when the IPv6 address was created. |
| AssociatedInst anceId | String | i-hp325kt6307**** | The ID of the instance that is assigned the IPv6 address. |
| AssociatedInst anceType | String | EcsInstance | The type of the instance that is assigned the IPv6 address. Only EcsInstance is returned, which indicates an ECS instance in a VPC. |
| Ipv6Address | String | 2408:XXXX:180:17 01:94c7:bc38:3bfa: d2c | The IPv6 address. |

| Ipv6AddressId | String | ipv6- n2yrzmwjz2uj3s7j5 **** | The ID of the IPv6 address. |
|---|---|---|---|
| Ipv6AddressNa me | String | test | The name of the IPv6 address. |
| Ipv6GatewayId | String | ipv6gw- hp38x2x0fz7**** | The ID of the IPv6 gateway to which the IPv6 address belongs. |
| Ipv6InternetBa ndwidth | Struct |   | The information about the Internet bandwidth of the IPv6 address. |
| Bandwidth | Integer | 2 | The exclusive Internet bandwidth of the IPv6 address. Unit: Mbit/s. |
| BusinessStatu s | String | Normal | The status of the exclusive Internet bandwidth of the IPv6 address. Valid values: Normal: normal FinacialLocked: locked due to overdue payments SecurityLocked: locked due to security reasons |
| InstanceCharg eType | String | PostPaid | The billing method of the IPv6 gateway. Only PostPaid is returned, which indicates the pay-as-you-go billing method. |
| InternetCharg eType | String | PayByTraffic | The metering method of the IPv6 gateway. Valid values: PayByTraffic: pay-by-data-transfer PayByBandwidth: pay-by-bandwidth |
| Ipv6InternetBa ndwidthId | String | ipv6bw- hp3b35oq1fj50kb** ** | The ID of the Internet bandwidth. |
| NetworkType | String | Public | The type of connection supported by the IPv6 address. Valid values: Private: communication within the private network Public: communication over the Internet |
| RealBandwidth | Integer | 2 | The actual maximum bandwidth of the IPv6 address. Unit: Mbit/s. |

| Status | String | Available | The status of the IPv6 address. Valid values: Pending: The IPv6 address is being configured. Available: The IPv6 address is available. |
|---|---|---|---|
| VSwitchId | String | vsw-123456**** | The ID of the vSwitch to which the IPv6 address belongs. |
| VpcId | String | vpc- hp325kt6307**** | The ID of the VPC to which the IPv6 address belongs. |
| PageNumber | Integer | 1 | The number of the returned page. Default value: 1. |
| PageSize | Integer | 10 | The number of entries returned on each page. Maximum value: 50. Default value: 10. |
| RequestId | String | AA4486A8-B6AE- 469E-AB09- 820EF8ECFA2B | The ID of the request. |
| TotalCount | Integer | 2 | The number of entries returned. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeIpv6Addresses &RegionId=cn-neimeng-env133-d01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeIpv6AddressesResponse>
  <TotalCount>2</TotalCount>
  <PageSize>10</PageSize>
  <RequestId>AA4486A8-B6AE-469E-AB09-820EF8ECFA2B</RequestId>
  <PageNumber>1</PageNumber>
  <Ipv6Addresses>
        <AllocationTime>2020-12-20T14:56:09Z</AllocationTime>
        <Status>Available</Status>
        <AssociatedInstanceId>i-hp325kt6307****</AssociatedInstanceId>
        <VpcId>vpc-hp325kt6307****</VpcId>
        <NetworkType>Public</NetworkType>
        <VSwitchId>vsw-123456****</VSwitchId>
        <Ipv6AddressId>ipv6-n2yrzmwjz2uj3s7j5****</Ipv6AddressId>
        <Ipv6GatewayId>ipv6gw-hp38x2x0fz7****</Ipv6GatewayId>
        <RealBandwidth>2</RealBandwidth>
        <AssociatedInstanceType>EcsInstance</AssociatedInstanceType>
        <Ipv6Address>2408:XXXX:180:1701:94c7:bc38:3bfa:d2c</Ipv6Address>
        <Ipv6AddressName>test</Ipv6AddressName>
        <Ipv6InternetBandwidth>
              <InstanceChargeType>PostPaid</InstanceChargeType>
              <Bandwidth>2</Bandwidth>
              <Ipv6InternetBandwidthId>ipv6bw-hp3b35oq1fj50kb****
</Ipv6InternetBandwidthId>
              <BusinessStatus>Normal</BusinessStatus>
              <InternetChargeType>PayByTraffic</InternetChargeType>
        </Ipv6InternetBandwidth>
  </Ipv6Addresses>
</DescribeIpv6AddressesResponse>
```

`JSON` format `{`

```json
    "TotalCount": 2,
    "PageSize": 10,
    "RequestId": "AA4486A8-B6AE-469E-AB09-820EF8ECFA2B",
    "PageNumber": 1,
    "Ipv6Addresses": {
        "AllocationTime": "2020-12-20T14:56:09Z",
        "Status": "Available",
        "AssociatedInstanceId": "i-hp325kt6307****",
        "VpcId": "vpc-hp325kt6307****",
        "NetworkType": "Public",
        "VSwitchId": "vsw-123456****",
        "Ipv6AddressId": "ipv6-n2yrzmwjz2uj3s7j5****",
        "Ipv6GatewayId": "ipv6gw-hp38x2x0fz7****",
        "RealBandwidth": 2,
        "AssociatedInstanceType": "EcsInstance",
        "Ipv6Address": "2408:XXXX:180:1701:94c7:bc38:3bfa:d2c",
        "Ipv6AddressName": "test",
        "Ipv6InternetBandwidth": {
            "InstanceChargeType": "PostPaid",
            "Bandwidth": 2,
            "Ipv6InternetBandwidthId": "ipv6bw-hp3b35oq1fj50kb****",
            "BusinessStatus": "Normal",
            "InternetChargeType": "PayByTraffic"
```

`}` `}` `}`

**Error codes**

| HttpCod e | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidRegionId.Not Found | The specified RegionId does not exist in our records. | The error message returned because the specified region ID does not exist. |

#### 4.5.14 ModifyIpv6InternetBandwidth

Modifies the Internet bandwidth value of an IPv6 address.

**Request parameters**

| Header | Type | Requir ed | Example value | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyIpv6Intern etBandwidth | The operation that you want to perform. Set the value to ModifyIpv6InternetBandwidth. |

| Bandwidth | Long | Yes | 4 | The Internet bandwidth of the IPv6 address. Unit: Mbit /s. Valid values: 1 to 5000. When the InternetChargeType is PayByBandwidth, the public bandwidth of the IPv6 address is 1 to 5000. When the InternetChargeType is PayByTraffic, the public bandwidth range of the IPv6 address is also limited by the IPv6 gateway specification. Small (the default free edition), the public bandwidth range is 1 to 500. For Medium (Enterprise Edition), the public bandwidth ranges from 1 to 1000. Large (Enterprise Enhanced Edition), the public bandwidth ranges from 1 to 2000. |
|---|---|---|---|---|
| RegionId | String | Yes | cn-neimeng- env133-d01 | The region ID of the IPv6 gateway. You can call the DescribeRegions operation to query the region ID. |
| Ipv6AddressId | String | No | ipv6gw- bp1go67rxgxc8l 7t0**** | The ID of the IPv6 address whose Internet bandwidth value you want to modify. Note Only one of Ipv6BandwidthId and Ipv6AddressId can be passed in. |
| Ipv6InternetBan dwidthId | String | No | ipv6- bp1t5rqb7pbxfx smy***** | The ID of the Internet bandwidth for the IPv6 address. Note You can only select one of Ipv6BandwidthId and Ipv6AddressId. |
| ClientToken | String | No | 0c593ea1-3bea- 11e9-b96b- 88e9fe637760 | The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |

**Response parameters**

| Header | Type | Example value | Description |
|---|---|---|---|
| RequestId | String | D560AF68-4CE8- 4A5C-B3FE- 469F558094D0 | The ID of the request. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=ModifyIpv6InternetBandwidth &Bandwidth=4 &RegionId=cn-neimeng-env133-d01 &<Common request parameters>
```

Sample success response `XML` format

```xml
<ModifyIpv6InternetBandwidthResponse>
   <RequestId>D560AF68-4CE8-4A5C-B3FE-469F558094D0</RequestId>
</ModifyIpv6InternetBandwidthResponse>
```

`JSON` format `{`

```json
 "RequestId": "D560AF68-4CE8-4A5C-B3FE-469F558094D0"
```

`}`

**Error code**

| HttpCod e | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidRegionId.Not Found | The specified RegionId does not exist in our records. | The region ID does not exist. |
