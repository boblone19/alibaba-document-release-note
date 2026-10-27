---
title: "Alibaba Cloud Apsara Stack Enterprise V3.18.1 IPv6 Gateway Developer Guide 20231124"
product_version: "V3.18.1"
doc_version: "20231124"
pdf_pages: 84
source_pdf: "Alibaba Cloud Apsara Stack Enterprise V3.18.1 IPv6 Gateway Developer Guide 20231124.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/3.18.1%E7%89%88%E6%9C%AC%E6%96%87%E6%A1%A3/IPV6/Alibaba%20Cloud%20Apsara%20Stack%20Enterprise%20V3.18.1%20IPv6%20Gateway%20Developer%20Guide%2020231124.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes+edge-junk)
---

# Alibaba Cloud Apsara Stack Enterprise V3.18.1 IPv6 Gateway Developer Guide 20231124

## Table of Contents

- 1 Getting started
  - 1.1 Usage notes on development documentation
  - 1.2 Call API operations
- 2 Preparations
  - 2.1 Log on to the API Tool console
  - 2.2 View information about API operations
  - 2.3 Obtain an AccessKey pair
  - 2.4 Obtain common header parameters
  - 2.5 Obtain an STS AccessKey pair
- 3 Use POP to make API calls
  - 3.1 Preparations
  - 3.2 SDK for Java
  - 3.3 SDK for Go
  - 3.4 SDK for Python
- 4 Use ASAPI to make API calls
  - 4.1 ASAPI overview
  - 4.2 Generate an endpoint for ASAPI
  - 4.3 Obtain Apsara Stack SDKs
  - 4.4 Common request parameters
  - 4.5 SDK description
    - 4.5.1 SDK for Java
    - 4.5.2 SDK for Python
    - 4.5.3 SDK for Node.js
    - 4.5.4 SDK for POP
    - 4.5.5 SDK for POP
  - 4.6 HTTP requests
    - 4.6.1 Overview
    - 4.6.2 Request structure
    - 4.6.3 Request signatures
    - 4.6.4 Responses
- 5 API references
  - 5.1 List of operations by function
  - 5.2 Make API requests
    - 5.2.1 Request syntax
    - 5.2.2 API authorization
    - 5.2.3 Sign an API request
  - 5.3 RAM authentication
  - 5.4 common parameters
  - 5.5 IPv6 gateways
    - 5.5.1 CreateIpv6Gateway
    - 5.5.2 DescribeIpv6Gateways
    - 5.5.3 DescribeIpv6GatewayAttribute
    - 5.5.4 ModifyIpv6GatewayAttribute
    - 5.5.5 ModifyIpv6GatewaySpec
    - 5.5.6 DeleteIpv6Gateway
    - 5.5.7 DescribeIpv6EgressOnlyRules
    - 5.5.8 CreateIpv6EgressOnlyRule
    - 5.5.9 DeleteIpv6EgressOnlyRule
    - 5.5.10 AllocateIpv6InternetBandwidth
    - 5.5.11 ModifyIpv6AddressAttribute
    - 5.5.12 DeleteIpv6InternetBandwidth
    - 5.5.13 DescribeIpv6Addresses
    - 5.5.14 ModifyIpv6InternetBandwidth

## 1 Getting started

### 1.1 Usage notes on development documentation

**documentation**

This topic describes how to view the desired product development documentation when you use Apsara Stack API (ASAPI).

**Prerequisites**

The Apsara Stack version is obtained from an O&M personnel or operations administrator.

**Procedure**

You can go to the Apsara Stack documentation center and view the desired product documentation.
1. Go to the Apsara Stack Documentation Centerpage by using a browser.
2. Click the **Enterprise**, **Agility**, or **All-in-one** tab based on the Apsara Stack version that you
use.
3. Select an Apsara Stack version from the drop-down list.
4. In the left-side navigation pane, select the name of the product that you want to view.
5. In the upper-right corner of the product documentation section, click **View Details** or
**Download PDF**.

### 1.2 Call API operations

Apsara Stack allows you to call API operations by using the point of presence (POP) gateway or the Apsara Stack API (ASAPI) gateway. To ensure that Apsara Stack provides the same experience as the public cloud, API operations in Apsara Stack are called by using the POP gateway by default starting Apsara Stack Enterprise V3.16.0. This topic describes how to use POP Gateway to call Apsara Stack API operations.

> **Note:** The method of using ASAPI Gateway to call Apsara Stack APIs in earlier versions is still valid. For more information, see the "Virtual Private Cloud Developer Guide" in the Apsara Stack Documentation Center. **Appendix**>> **ASAPI Gateway call process description** chapterGenerate an endpoint for ASAPI, obtain the SDK package of ASAPI.

**Procedure**

1. Obtain security credentials used to call APIs.
Obtain the AccessKey credentials that are required when you call an API operation. For more information, see Obtain an AccessKey pair or Obtain an STS AccessKey 3-tuple.

> **Note:** We recommend that you use the AccessKey pair of a personal account assigned by Resource Access Management (RAM) or a Security Token Service (STS) AccessKey 3- tuple to call the API operations of the Apsara Uni-manager Management Console and cloud services.

2. Obtain the region ID.
For more information, see Obtain the values of common headers.
3. Obtain the organization ID and the resource set ID.
Obtain the organization ID by calling the GetOrganizationList operation. For more information, see GetOrganizationList in Apsara Uni-manager Management Console Develop er Guide. Obtain the resource set ID by calling the ListResourceGroup operation. For more information, see ListResourceGroup in Apsara Uni-manager Management Console Develope r Guide.

|   | Note When you call an API operation, you can specify the organization ID by using <x-acs- organizationid> and the resource set ID by using <x-acs-resourcegroupid> to query only resources that belong to the specified resource set and organization. If you do not specify the <x-acs-organizationid> parameter, the organization to which the current user belongs is used. If you do not specify the <x-acs-resourcegroupid> parameter, this parameter is left empty. If you specify a resource set ID, you must also specify an organization ID. |   |   |   |
|---|---|---|---|---|
|   |   |   | <x-acs- |   |
|   | organizationid> | <x-acs-resourcegroupid> |   |   |

4. View the developer guide of the cloud service that you want to use to learn how to make
the API call. Obtain the developer guide of the cloud service that you want to use. You can learn the features of API operations and how to call the API operations. For more information, see Usage notes on development documentation.
5. Obtain the endpoint of the cloud service.
6. Obtain the SDK of the cloud service and call an API operation.

## 2 Preparations

### 2.1 Log on to the API Tool console

You can log on to the API Tool console from the Apsara Uni-manager Management Console.

**Prerequisites**

The URL of the console that is obtained from the deployment personnel. A web browser. We recommend that you use Google Chrome.

**Procedure**

1. Enter the URL of the Apsara Uni-manager Management Console in the address bar and
press the Enter key.
2. Enter your username and password.
You need to obtain the username and password from an operations administrator.

> **Note:** **First logon**
> The first time that you log on to the Apsara Uni-manager Management Console, you need to change the password of your account. The password must be 10 to 32 characters in length. It must contain all of the following character types: uppercase letters, lowercase letters, digits, and special characters. Supported special characters include: ! @ # $ %
> **Forget password**
> If you have forgotten your password, click Forgot Password. On the page that appears, enter the username of your account, the email address that was used to create the account, and the CAPTCHA code. Then, the system sends a link for resetting the password to the specified email address.

3. Click **Log On**.
4. If multi-factor authentication (MFA) is enabled for your account, perform the corresponding
operations in the following scenarios: You log on to the Apsara Uni-manager Management Console for the first time after MFA is enabled by the administrator. a. On the Bind Virtual MFA Device page, bind an MFA device. b. Enter the username and password again as in Step 2 and click **Log On**. c. Enter a six-digit MFA verification code and click **Authenticate**. You have enabled MFA and bound an MFA device: Enter a six-digit MFA verification code and click **Authenticate**.

> **Note:** For information about how to bind and enable MFA, see Manage MFA.

5. In the top navigation bar, choose **Products > Others > API Tool**.

### 2.2 View information about API operations

**operations**

This topic describes how to view information about API operations. Before you use SDKs, obtain service names, API operation names, and API operation versions.

**Background information**

The API operations on the API Directory page are only for reference. For information about how to call API operations, see developer guides of the corresponding cloud services. If the information on the API Directory page is inconsistent with that in the developer guide of the corresponding cloud service, the information in the developer guide prevails.

**Procedure**

1. Go to the API Tool console. For more information, see Log on to the API Tool console.
2. In the left-side navigation pane, click **API Directory**.
3. On the **API Directory** page, select the desired service from the drop-down list, enter a
keyword of an API operation name in the search box, and then click the search icon.
4. Then, you can view the service name, API operation name, and API operation version.

### 2.3 Obtain an AccessKey pair

An AccessKey pair consists of an AccessKey ID and an AccessKey secret. AccessKey pairs are used to implement symmetric encryption to verify the identity of requesters. The AccessKey ID is used to identify a user. The AccessKey secret is used to encrypt a signature string. This topic describes how to obtain an AccessKey pair.

**Prerequisites**

An account that assumes the operations administrator or level-1 organization administrator role is obtained. Only an operations administrator or a level-1 organization administrator can obtain an AccessKey pair of the organization.

**Background information**

AccessKey supports the following authorization methods: Use RAM to authorize the AccessKey ID and AccessKey secret to third-party requesters. Use STS to authorize the AccessKey ID, AccessKey secret, and security token to third-party requesters. This topic describes how to obtain an AccessKey pair authorized by RAM. For more information about how to obtain an AccessKey pair authorized by STS, see **Obtain an STS**
**AccessKey pair**.
We recommend that you use the AccessKey pair of a personal account to call the API operations of the Apsara Uni-manager Management Console and cloud services. If you use the AccessKey pair of a personal account, configure the request headers that are described in the following table for access control. Otherwise, an error that indicates insufficient permissions can occur.

| Parameter | Description |
|---|---|
| x-acs-regionid | The ID of the region, such as cn-hangzhou-*. |
| x-acs-organizationid | The ID of the organization in the Apsara Uni- manager Management Console. For information about how to obtain an organization ID, see the "GetOrganizationList" section in Apsara Uni- manager Management Console Developer Guide. |
| x-acs-resourcegroupid | The ID of the resource set in the Apsara Uni- manager Management Console. For information about how to obtain a resource set ID, see the "ListResourceGroup" section in Apsara Uni- manager Management Console Developer Guide. |
| x-acs-instanceid | The ID of the instance on which to perform operations. For example, you can query the ID of an Elastic Compute Service (ECS) instance from the ECS instance list. |

> **Warning:** The AccessKey pair of a personal account is managed and controlled by the permission system of the Apsara Uni-manage Management Console. If you need to obtain the AccessKey pair of an account that has permissions on an organization, make sure that your operation is allowed by an administrator. This ensures security. The account that has permissions on an organization is a privileged account.

**Obtain the AccessKey pair of a personal account**

To obtain the AccessKey pair of a personal account, perform the following steps:
1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the homepage, move the pointer over the profile picture and
choose **User Information** from the shortcut menu.
3. In the **Apsara Stack AccessKey Pair** section, obtain the AccessKey pair.

> **Note:** The AccessKey pair consists of an AccessKey ID and an AccessKey secret. These credentials provide you with full permissions on Apsara Stack resources. You must keep the AccessKey pair confidential.

**Obtain the AccessKey pair of an organization**

To obtain the AccessKey pair of an organization, perform the following steps:
1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, click **Enterprise**.
3. In the left-side navigation pane, choose **Resources > Organizations**.
4. In the organization navigation tree, click the name of the level-1 organization for which you
want to obtain AccessKey pairs.
5. Click **Management AccessKey** on the right side of the page.
6. In the AccessKey message, view the AccessKey pair of the organization.

### 2.4 Obtain common header parameters

**parameters**

You must provide multiple header parameters when you call API operations. This topic describes how to obtain common header parameters. Some response parameters are also explained.

**Query a region ID**

1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, click **Enterprise**.
3. In the left-side navigation pane, choose **Resources** > **Regions**.
4. Click the name of the organization that you want to view.
5. View the region ID in the **Regions** window on the right.

**Obtain an organization ID**

You can call the API operation to obtain the organization ID. For more information about how to obtain the organization ID, see GetOrganizationList in Apsara Uni-manager Management Console Developer Guide.

**Obtain a resource set ID**

You can call the API operation to obtain the resource set. For more information about how to obtain the resource set ID, see ListResourceGroup in Apsara Uni-manager Management Console Developer Guide.

**Obtain an instance ID**

You can obtain the ID of an instance in the cloud service console of the Apsara Uni-manager Management Console. This topic illustrates how to obtain the ID of an ECS instance. Perform the following steps:
1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Products** > **Elastic Computing** > **Elastic Compute**
**Service**.
3. In the left-side navigation pane, choose **Instances & Images > Instances**.
4. View the **instance ID** in the instance list.

**Response parameters**

The following response parameter are returned by default when you call list-type API operations for cloud product resource instances.

| Parameter | Description |
|---|---|
| ResourceGroupName | The name of the resource set. |
| ResourceGroup | The ID of the resource set. |
| DepartmentName | The name of the organization. |
| Department | The ID of the organization. |

### 2.5 Obtain an STS AccessKey pair

This topic describes how to use STS to make API calls.

**Background information**

Alibaba Cloud Security Token Service (STS) allows you to manage temporary credentials to your Alibaba Cloud resources. You can use STS to make API calls.

**Procedure**

1. Obtain the `RAM role` .
i. Log on to the Apsara Uni-manager Management Console. ii. Move the pointer over the profile picture in the upper-right corner of the page and click
**Personal Information**.
iii. Click **View Current Role Policy**. In the **View Policies of Current Role** dialog box, view your `RAM role` .
2. Use the following code to obtain `stsAK` , `stsSK` , and `stsToken` by using your `RAM`
`role` .

```
public static void main(String[] args) {
     ASClient asClient = new ASClient();
     // The call source.
        asClient.setSdkSource("asapi_test");
     // Pass in the ARN.
        String assumeRole = AssumeRole(asClient, "<RAM Role>");
        JSONObject assumeRoleJson = JSONObject.parseObject(assumeRole);
        JSONObject credentials = assumeRoleJson.getJSONObject("Credentials");
        // Obtain the STS triplet.
        String stsAK = credentials.getString("AccessKeyId");
        String stsSK = credentials.getString("AccessKeySecret");
        String stsToken = credentials.getString("SecurityToken");
```

`}`

```
public static String AssumeRole(ASClient asClient, String roleArn) {
        Map<String, String> headers = new HashMap<>();
        Map<String, Object> reqParams = new HashMap<>();
        reqParams.put("action", "AssumeRole");
        reqParams.put("Product", "Sts");
        reqParams.put("Version", "2015-04-01");
        reqParams.put("regionId", regionId);
     // Your AccessKey ID.
        reqParams.put("AccessKeyId", <Your AccessKey ID>);
     // Your AccessKey secret.
        reqParams.put("AccessKeySecret", <Your AccessKey secret>);
        reqParams.put("roleSessionName", "AsapiStsUser");
        reqParams.put("roleArn", roleArn);
        return asClient.doRequest(endpoint, headers, reqParams);
```

`}`
3. You can use STS to make API calls. The following sample code demonstrates how to call
ECS API operations.

```
public static void main(String[] args) {
     ASClient asClient = new ASClient();
        asClient.setSdkSource("asapi_test");
  // Call ECS API operations.
        String ecsRes = DescribeZones(asClient,<stsAK>,<stsSK>,<stsToken>);
```

`}`

```
public static String DescribeZones(ASClient asClient, String stsAK, String stsSK, Str ing stsToken) {
        Map<String, String> headers = new HashMap<>();
        Map<String, Object> reqParams = new HashMap<>();
        reqParams.put("action", "DescribeZones");
        reqParams.put("Product", "Ecs");
        reqParams.put("Version", "2014-05-26");
        reqParams.put("regionId", "<your-RegionID>");
        // The STS triplet of AccessKey ID, AccessKey secret, and security token.
        reqParams.put("AccessKeyId", <stsAK>);
        reqParams.put("AccessKeySecret", <stsSK>);
        reqParams.put("SecurityToken", <stsToken>);
        return asClient.doRequest(endpoint, headers, reqParams, HttpMethod.GET);
```

`}` e API calls

## 3 Use POP to make API calls

### 3.1 Preparations

Apsara Stack is the same as the public cloud, you can use the POP gateway to make API calls. This topic describes the preparations before you use the POP gateway to call API operations.

**Background information**

In Apsara Stack, you can use both Apsara Stack API (ASAPI) and the POP gateway to call API operations. To keep Apsara Stack in the same way as the public cloud and enable you to have a more convenient and consistent experience, we recommend that you use the POP gateway to call Apsara Stack APIs.

**Obtain service endpoints**

To use the POP gateway to call API operations, you must use the service endpoints. You can obtain service endpoints from Apsara Stack onsite O&M engineers. You can also obtain service endpoints by yourself. The following example describes how to obtain a service endpoint. IPv6 Gateway is used in this example.
1. Log on to the Apsara Infrastructure Management console.
i. Go to the Apsara Uni-manager Operations Console. ii. In the top navigation bar, choose **Products** > **Base /Cloud Platform** > **Apsara**
**Infrastructure Management Platform**.
2. In the left-side navigation pane, choose **O&M Tools** > **Basic Data Management** >
**Service Registration Variable Dashboard**.
3. On the Registration Variable Dashboard page, click **Advanced Filter**.
4. Enter a `ipv6gateway` in the Service Registration field and click **Search**.
icon.
5. In the **Service Registration** column for the `ipv6gateway` service, click the
6. Click the text information in the `ipv6gateway` Service **Service Registration** column. In
the **Register Variable** dialog box, view the **internal.openapi.endpoint** value, which is the `Endpoint` value.

**Obtain common parameters**

You must obtain the parameters required when you use the POP gateway to call API operations, such as the organization ID, resource set ID, region ID, and instance ID. For more information, see Obtain common header parameters.

### 3.2 SDK for Java

Before you use POP SDK for Java to make API calls, you must first understand the RPC and ROA styles.

**Prerequisites**

An Alibaba Cloud SDK package is downloaded for the service that you want to access. The required dependencies are installed. SSL certificate validation is ignored for requests over HTTPS.

**Call examples**

e API calls The following sample code provides an example on how to use the RPC style to make an API call. In this example, the DescribeInstances operation of Elastic Compute Service (ECS) is called, and the API version is 2014-05-26. Sample code:

```java
import com.aliyuncs.CommonRequest; import com.aliyuncs.CommonResponse; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.exceptions.ServerException; import com.aliyuncs.http.MethodType; import com.aliyuncs.profile.DefaultProfile; public class DescribeInstances {
    public static void main(String[] args) {
        // Create and initialize a DefaultAcsClient instance.
        DefaultProfile profile = DefaultProfile.getProfile("<your-regionid>", "
<yourAccessKeyId>", "<yourAccessSecret>");
        // Ignore SSL certificate validation.
        // HttpClientConfig clientConfig = HttpClientConfig.getDefault();
        // clientConfig.setIgnoreSSLCerts(true);
        // Configure the time-out period for a connection.
        // clientConfig.setConnectionTimeoutMillis(3000L);
        // Set the read timeout period.
        // clientConfig.setReadTimeoutMillis(10000L);
        // profile.setHttpClientConfig(clientConfig);
        IAcsClient client = new DefaultAcsClient(profile);
        // Create an API request and configure the parameters.
        CommonRequest request = new CommonRequest();
        // Specify the request method.
        request.setSysMethod(MethodType.POST);
        // Set the service endpoint.
        request.setSysDomain("<ecsEndpoint>");
        // Specify the version of the API operation.
        request.setSysVersion("2014-05-26");
        // Specify the name of the service that you want to access and the region where
the service resides.
        request.setSysLocationProduct("Ecs");
        // Specify the name of the API operation.
        request.setSysAction("DescribeInstances");
        // When you use the STS AccessKey ID to call RPC API operations, you must add t
he SecurityToken parameter to the header.
        // request.putBodyParameter("SecurityToken", "<your-SecurityToken>");
        // Configure operation-specific parameters.
        request.putBodyParameter("PageSize", "10");
        request.putBodyParameter("PageNumber", "1");
        // Required. The call source.
```

e API calls

```java
        request.putHeadParameter("x-acs-caller-sdk-source", "ApiTestDemo");
        // Optional. For the historical versions before Enterprise Edition V3.15.0.
        request.putHeadParameter("x-acs-regionid", "<your-regionid>");
        // Optional. The resource set ID.
        request.putHeadParameter("x-acs-resourcegroupid", "<your-resourcegroupid>");
        // Required. The organization ID.
        request.putHeadParameter("x-acs-organizationid", "<your-organizationid>");
        // Optional. For the modify and delete operations.
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
        // Configure the time-out period for a connection.
        // clientConfig.setConnectionTimeoutMillis(3000L);
        // Set the read timeout period.
        // clientConfig.setReadTimeoutMillis(10000L);
        // profile.setHttpClientConfig(clientConfig);
```

e API calls

```java
        IAcsClient client = new DefaultAcsClient(profile);
        // Create an API request and configure the parameters.
        CommonRequest request = new CommonRequest();
        // Set the request protocol to HTTPS.
        request.setSysProtocol(ProtocolType.HTTP);
        // Specify the request method.
        request.setSysMethod(MethodType.GET);
        // Set the service endpoint.
        request.setSysDomain("<crEndpoint>");
        // Specify the version of the API operation.
        request.setSysVersion("2016-06-07");
        // Configure the uriPattern parameter, which is required for the ROA style.
        request.setSysUriPattern("/namespace");
        // Specify the name of the service that you want to access and the region where
the service resides.
        request.setSysLocationProduct("cr");
        // Specify the name of the API operation.
        request.setSysAction("GetNamespaceList");
        // Required. The call source.
        request.putHeadParameter("x-acs-caller-sdk-source", "ApiTestDemo");
        // Optional. For the historical versions before Enterprise Edition V3.15.0.
        request.putHeadParameter("x-acs-regionid", "<your-regionid>");
        // Optional. The resource set ID.
        request.putHeadParameter("x-acs-resourcegroupid", "<your-resourcegroupid>");
        // Required. The organization ID.
        request.putHeadParameter("x-acs-organizationid", "<your-organizationid>");
        // Optional. For the modify and delete operations.
        // request.putHeadParameter("x-acs-instanceid", "<your-instanceid>");
        // When you use the STS AccessKey ID to call ROA API operations, you must add t
he x-acs-security-token parameter to the header.
        // request.putHeadParameter("x-acs-security-token", "<your-securitytoken>");
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

`}` `}` `}` e API calls

> **Important:** If you send a request over HTTPS, you must enable the request to ignore SSL certificate validation.

### 3.3 SDK for Go

This topic describes how to use POP SDK for Go.

**Prerequisites**

An Alibaba Cloud SDK package is downloaded for the service that you want to access. The required dependencies are installed.

**Background information**

Both RPC and ROA styles are supported for API calls.

**Call examples**

The following sample code provides an example on how to use the RPC style to make an API call. In this example, the DescribeInstances operation of Elastic Compute Service (ECS) is called, and the API version is 2014-05-26. Sample code: e API calls

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
    request.Domain = "<ECSEndpoint>"
    request.Version = "2014-05-26"
    request.ApiName = "DescribeInstances"
    request.Product = "Ecs"
    // When you use the STS AccessKey ID to call RPC API operations, you must add the S
ecurityToken parameter to the header.
    // request.QueryParams["SecurityToken"]="<your-SecurityToken>"
    // Required. The call source.
    request.Headers["x-acs-caller-sdk-source"] = "ApiTestDemo"
    // Optional. For the historical versions before Enterprise Edition V3.15.0.
    request.Headers["x-acs-regionid"] = "<your-RegionID>"
    // Optional. The resource set ID.
    request.Headers["x-acs-resourcegroupid"] = "<your-ResourceGroupID>"
    // Required. The organization ID.
    request.Headers["x-acs-organizationid"] = "<your-OrganizationID>"
    // Optional. For the modify and delete operations.
    // request.Headers["x-acs-instanceid"] = "<your-InstanceID>"
    response, err := client.ProcessCommonRequest(request)
    if err != nil {
        panic(err)
```

`}`

```
    fmt.Print(response.GetHttpContentString())
```

`}` The following sample code provides an example on how to use the ROA style to make an API call. In this example, the GetNamespaceList operation of Container Registry is called, and the API version is 2016-06-07. The following sample code shows how to call API operations: e API calls

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
    // Optional. For the historical versions before Enterprise Edition V3.15.0.
    request.Headers["x-acs-regionid"] = "<your-RegionID>"
    // Optional. The resource set ID.
    request.Headers["x-acs-resourcegroupid"] = "<your-ResourceGroupID>"
    // Required. The organization ID.
    request.Headers["x-acs-organizationid"] = "<your-OrganizationID>"
 // Optional. For the modify and delete operations.
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

You can configure proxies in one of the following ways when you call API operations: Configure proxies as environment variables. Set the HTTP_PROXY and HTTPS_PROXY environment variables, or set the NO_PROXY environment variable. Sample code: e API calls

```java
import (
    "os"
```

`)`

```
func main(){
 os.Setenv("HTTP_PROXY", "http://x.x.x.x:xxxx") // Configure the HTTP_PROXY environme
nt variable.
 os.Setenv("HTTPS_PROXY", "https://x.x.x.x:xxxx") // Configure the HTTPS_PROXY enviro
nment variable.
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

ake API calls

## 4 Use ASAPI to make API calls

**calls**

### 4.1 ASAPI overview

This topic describes the architecture and features of the Apsara Stack API (ASAPI). The ASAPI is a unified ingress gateway for Apsara Stack services and a main component of the Apsara Uni-manager Management Console. The ASAPI provides a unified method for you to manage and make API calls. You can use Apsara Stack SDK to centrally make API calls to Apsara Stack services, including Elastic Compute Service (ECS) and Virtual Private Cloud (VPC). The ASAPI allows you to make API calls to manage and maintain Apsara Stack services. Make API calls to implement enterprise-grade management. For example, you can manage organizations, users, roles, resource sets, and logon policies. These operations are provided by the Apsara Uni-manager Management Console. Make API calls to manage operations. For example, you can manage quotas, usage statistics, specifications, and password policies. These operations are provided by the Apsara Uni-manager Management Console. ake API calls Make API calls to manage resources. For example, you can create, delete, query, or modify cloud resources. These operations are provided by Apsara Stack services. If you call an API operation to create an ECS instance or a VPC, the API operation is provided by ECS or VPC. Make API calls to query monitoring metrics of Apsara Stack services. These operations are provided by the Apsara Uni-manager Management Console. Make API calls to perform O&M. For example, you can manage monitoring and alerting, inventories, tasks, and physical servers. These operations are provided by the Apsara Unimanager Operations Console. For more information, see the developer guide of the corresponding Apsara Stack service. For information about API operations used to manage organization users, see Apsara Unimanager Management Console Developer Guide. For information about the API operation used to create an ECS instance, see ECS Developer Guide.

> **Note:** If the "Use Apsara Stack SDK to make API calls" section is included in the developer guide of an Apsara Stack service, the ASAPI is supported by the Apsara Stack service. In this case, you can make API calls based on the developer guide.

### 4.2 Generate an endpoint for ASAPI

**ASAPI**

This topic describes three methods used to generate an endpoint for Apsara Stack API (ASAPI).

**Method 1: Use Registration Vars of Services to generate an**

**endpoint**

1. Log on to Apsara Infrastructure Management Framework.
i. Log on to the Apsara Uni-manager Operations Console. ii. In the top navigation bar, click **O&M**. iii. In the left-side navigation pane, choose **Product Management** > **Products**. iv. In the Apsara Stack O&M section, click **Apsara Infrastructure Management**
**Framework**.
2. In the left-side navigation pane, click **Reports**.
3. On the **All Reports** page, search for `Registration Vars of Services` and click the report
name. ake API calls
4. On the **Registration Vars of Services** page, click the
icon next to **Service** and search for `asapi` .
5. Find the asapi service, right-click in the **Service Registration** column, and then select
**Show More** from the shortcut menu.
In the **Details** dialog box, obtain the value of **asapi.public.endpoint**.
6. Generate an endpoint for ASAPI based on the following format:

```
https://<asapi.public.endpoint>/asapi/v3
```

**Method 2: Use cluster resources to generate an endpoint**

1. Log on to Apsara Infrastructure Management Framework.
i. Log on to the Apsara Uni-manager Operations Console. ii. In the top navigation bar, click **O&M**. iii. In the left-side navigation pane, choose **Product Management** > **Products**. iv. In the Apsara Stack O&M section, click **Apsara Infrastructure Management**
**Framework**.
2. Go to the cluster operations page.
i. In the left-side navigation pane, choose Operations > Cluster Operations. ii. In the **Cluster** search box, enter `ascm` . iii. Find the cluster that you want to manage and click **Operations** in the **Actions** column.
3. Obtain the value of the domain parameter.
i. Click the Cluster Resources tab. ii. In the **Name** field, search for `asapi_dns_public` . iii. Click **Details** in the **Application Parameter** column. In the **Application Parameter** message, obtain the value of the **domain** parameter.
4. Generate an endpoint for ASAPI based on the following format:

```
https://<domain>/asapi/v3
```

**Method 3: Concatenate strings to generate an endpoint**

You can also concatenate strings to generate an endpoint based on the following format:

```
https://public.asapi.<region>.<internet-domain>/asapi/v3
```

ake API calls

**Note**

1. Replace <region> with your actual region ID. For information about how to query a
region ID, see Query a region ID.
2. Replace <internet-domain> with the root domain of your Apsara Stack service. To
obtain the root domain, contact Apsara Stack O&M personnel. Take note of this point: Use the internet-domain parameter instead of the intranet-domain parameter. If the **region** value is `cn-****-****-d01` and the **internet-domain** value is `inter.****.****.com` , the following endpoint can be generated: An example of a complete endpoint:

```
https://public.asapi.cn-****-****-d01.inter.****.****.com/asapi/v3
```

### 4.3 Obtain Apsara Stack SDKs

Apsara Stack API (ASAPI) is a unified portal provided by Apsara Stack. You can use the ASAPI to connect to all Apsara Stack services. Apsara Stack provides SDKs for API calls. You can go to Apsara Stack documentation and download the Apsara Stack SDKs in the **Other**
**Resources** section at the lower part of the page.

### 4.4 Common request parameters

Common request parameters must be included in all API requests.

**Sample common parameters**

The following table describes the common parameters that are used when you call API operations supported by Apsara Stack API (ASAPI).

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. For more information, see View the information about API operations. |
| Product | String | Yes | The name of the service. |
| Version | String | Yes | The version of the API operation. For more information, see View information about API operations. |

ake API calls

| Parameter | Type | Required | Description |
|---|---|---|---|
| RegionId | String | Yes | The ID of the region. For more informatio, see Query a region ID. |
| AccessKeyId | String | Yes | The AccessKey ID used to connect to the service. For more information, see Obtain an AccessKey pair. |
| Signature | String | Yes | The signature string of the current request. For more information about how signatures are calculated, see Request signatures. |
| SignatureMethod | String | Yes | The encryption method of the signature string. Valid values: HMAC-SHA1 and HMAC-SHA256. |
| SignatureVersion | String | Yes | The version of the signature encryption algorithm. Valid values: 1.0 and 2.0. |
| SignatureNonce | String | Yes | A unique, random number used to prevent replay attacks. You must use different numbers for different requests. |
| Timestamp | String | Yes | The timestamp of the request. Specify the time in the ISO 8601 standard in the yyyy- MM-ddTHH:mm:ssZ format. The time must be in UTC. Example: 2018-01- 01T12:00:00Z. |
| Format | String | Yes | The format in which to return the response. Set the value to JSON. |

ake API calls

**Note**

|   | Signature |
|---|---|
| Timestamp |   |

```
The Signature , SignatureMethod , SignatureVersion , SignatureNonce ,
```

> `Timestamp` , and `Format` parameters are encapsulated into Apsara Stack SDK. You do not need to configure these parameters.

### 4.5 SDK description

#### 4.5.1 SDK for Java

This topic describes how to obtain and use Apsara Stack SDK for Java to call API operations.

**Prerequisites**

An authorized account and an AccessKey pair are obtained. The AccessKey pair consists of an AccessKey ID and an AccessKey secret. You can obtain and view your AccessKey pair in the Apsara Uni-manager Management Console. For more information, see Obtain an AccessKey pair. The endpoint of the ASAPI is obtained. For more information, see Generate an endpoint for ASAPI. The endpoint of ASAPI is obtained. For more information about how to obtain the endpoint of ASAPI, see Obtain the endpoint of ASAPI. Apsara Stack SDK for Java 1.8 or later is installed.

**Background information**

The help center of Apsara Stack provides Maven dependencies and JAR files for Apsara Stack SDK for Java. You can write code to use Apsara Stack SDK for Java to call API operations. In this example, the Windows 10 64-bit OS and IntelliJ IDEA are used.

**Procedure**

1. Use one of the following methods to configure Maven in IntelliJ IDEA. Maven is a tool used
for project management. Use Maven that is integrated in IntelliJ IDEA. Download Maven based on the OS that you are using from the official website and configure Maven. For more information, see Download Maven.
2. Obtain the Maven dependencies for Apsara Stack SDK for Java from the official website.
3. Use one of the following methods to create a Maven project:
Method 1: Create a Maven project in IntelliJ IDEA. ake API calls Method 2: Convert an existing project to a Maven project. a. Right-click the project that you want to convert and select **Add Framework**
**Support...**.
b. Select **Maven** and click **OK**.
4. Create a folder named libs in the root directory of the project. Then, add the JAR file of
Apsara Stack SDK for Java to the libs folder, as shown in the following figure. ake API calls
5. Add the dependencies of Apsara Stack SDK for Java to the pom.xml file in the project
directory.

```xml
<dependencies>
    <dependency>
        <groupId>com.aliyun</groupId>
        <artifactId>asapi</artifactId>
        <version>1.0.6.4-RELEASE</version>
        <scope>system</scope>
        <systemPath>${project.basedir}/libs/asapi-1.0.6.4-RELEASE.jar</systemPath>
    </dependency>
  <dependency>
        <groupId>com.alibaba</groupId>
        <artifactId>alicrypto-java-aliyun</artifactId>
    <version>1.0.4</version>
    <systemPath>${project.basedir}/libs/alicrypto-java-aliyun-1.0.4.jar</systemPath>
  </dependency>
  <dependency>
    <groupId>com.aliyun</groupId>
    <artifactId>gmsse</artifactId>
    <version>1.1.0</version>
    <systemPath>${project.basedir}/libs/gmsse-1.1.0.jar</systemPath>
  </dependency>
    <dependency>
    <groupId>org.apache.httpcomponents</groupId>
    <artifactId>httpclient</artifactId>
    <version>4.5.7</version>
    <systemPath>${project.basedir}/libs/httpclient-4.5.7.jar</systemPath>
  </dependency>
</dependencies>
```

> **Note:** Replace `1.0.6.4-RELEASE` with the actual version of Apsara Stack SDK for Java.

6. On the right side of IntelliJ IDEA, view information in the Maven section.
If the information in the following figure appears, the dependencies are added. ake API calls

**Use Apsara Stack SDK for Java**

You can use the GET or POST method to call API operations provided by ASAPI. The following sample code shows how to call API operations: ake API calls

```java
// 1. Create a connection to an ASClient object. ASClient client = new ASClient(); // 2. Configure the identifier of the requester. This parameter is required and used on ly for identification. You can set this parameter to a random value. client.setSdkSource("<The identifier of the requester>"); Map<String, Object> parameters = new HashMap<String, Object>(); // 3. Configure the parameters for authorization. The parameter values vary based on yo ur environment. // The AccessKey ID of your Apsara Stack tenant account. parameters.put("AccessKeyId","<AccessKey ID>"); // The AccessKey secret of your Apsara Stack tenant account. parameters.put("AccessKeySecret", "<AccessKey Secret>"); // The ID of the region. parameters.put("RegionId", "<your RegionID>"); // 4. Configure parameters for an API call. In this example, the Product, Action, and V ersion parameters are configured. parameters.put("Product", "<The name of the service>"); parameters.put("Action", "<The name of the API operation>"); parameters.put("Version", "<The version of the API operation>"); // When you use the STS AccessKey ID to call RPC API operations, you must add the SecurityToken parameter to the header. // parameters.put("SecurityToken", "<your-securitytoken>"); // When you use the STS AccessKey ID to call ROA API operations, you must add the xacs-security-token parameter to the header. // headers.put("x-acs-security-token", "<your-securitytoken>"); // 5. Configure operation-specific parameters. parameters.put("<The name of the operation-specific parameter>", "<The value of the ope ration-specific parameter>"); // 6. Configure request headers and the encryption method for the signature string. Val id values of the SignatureMethod parameter: HMAC-SHA1 and HMAC-SHA256. By default, HMAC -SHA256 is used. Map<String, String> headers = new HashMap<String, String>(); //headers.put("SignatureMethod", "HMAC-SHA1"); headers.put("x-acs-regionid", "<your-regionid>"); headers.put("x-acs-resourcegroupid", "<your-resourcegroupid>"); headers.put("x-acs-organizationid", "<your-organizationid>"); headers.put("x-acs-instanceid", "<your-instanceid>"); // 7. Make an API call. We recommend that you use the doPost() method. // Configure the time-out period for a connection. //client.setConnectTimeout(10000); // Configure the time-out period for a request. // client.setSocketTimeout(10000); String result = client.doPost(endpoint, headers, parameters); System.out.println(result);
```

**Configure proxies**

If you need to use a proxy to make API calls, use the following sample code to configure the proxy: ake API calls

```
Cloud cloud = new Cloud(); // Configure the IP address of the proxy. cloud.setConfig("proxy_host", "<IP>"); // Configure the port used by the proxy. cloud.setConfig("proxy_port", "<Port>"); Create a connection to an ASClient object. ASClient client = new ASClient(cloud);
```

**Header parameters**

| Parameter | Description |
|---|---|
| x-acs-regionid | The ID of the region. For more information about how to obtain a region ID, see Query a region ID. |
| x-acs-organizationid | The ID of the organization in the Apsara Uni- manager Management Console. |
| x-acs-resourcegroupid | The ID of the resource set in the Apsara Uni- manager Management Console. |
| x-acs-instanceid | The ID of the instance to which you make API calls. |

#### 4.5.2 SDK for Python

This topic describes how to obtain and use Apsara Stack SDK for Python to call API operations.

**Preparations**

An authorized account and an AccessKey pair are obtained. The AccessKey pair consists of an AccessKey ID and an AccessKey secret. For more information about how to obtain an AccessKey pair in the Apsara Uni-manager Management Console, see Obtain an AccessKey pair. The endpoint of ASAPI is obtained. For more information, see Generate an endpoint for ASAPI. The endpoint of ASAPI is obtained. For more information, see Generate an endpoint for ASAPI.

**Install Apsara Stack SDK for Python**

1. Download the required version of Apsara Stack SDK for Python. For more information, see
Obtain Apsara Stack SDKs.
2. Upload the compressed file of Apsara Stack SDK for Python to the host from which you want
to send API requests and extract the file. Then, run the following code in the directory of the extracted files to install Apsara Stack SDK for Python:

```bash
# Install Apsara Stack SDK for Python 2.x.
pip install aliyun-python2-sdk-asapi-2.4.7.tar.gz
# Install Apsara Stack SDK for Python 3.x.
pip3 install aliyun-python3-sdk-asapi-2.4.7.tar.gz
```

ake API calls

> **Note:** Replace `2.4.7` with the actual version of Apsara Stack SDK for Python.

**Sample requests**

You can use the GET or POST method to call API operations provided by ASAPI.

```xml
# 1. Import dependencies.
   from aliyunsdkasapi.ASClient import ASClient
   from aliyunsdkasapi.AsapiRequest import AsapiRequest
   if __name__ == '__main__':
    # 2. Create a request. The Product parameter specifies the name of the service. The
Version parameter specifies the version of the API operation. The Action parameter spec ifies the operation that you want to perform. The asapi-endpoint parameter specifies th e endpoint of ASAPI.
    req = AsapiRequest("<Product>", "<Version>", "<Action>", "<asapi-endpoint>")
    # 3. Configure operation-specific parameters.
    req.add_body_params("<key>", "<value>")
 # When you use the STS AccessKey ID to call RPC API operations, you must add the
SecurityToken parameter to the header.
 # req.add_body_params("SecurityToken", "<your-securitytoken>");
 # When you use the STS AccessKey ID to call ROA API operations, you must add the x-
acs-security-token parameter to the header.
 # req.add_header("x-acs-security-token", "<your-securitytoken>");
    # 4. Configure request headers.
    req.add_header("x-acs-resourcegroupid", "<your-resourcegroupid>");
    req.add_header("x-acs-organizationid", "<your-organizationid>");
    req.add_header("x-acs-regionid", "<your-regionid>");
    req.add_header("x-acs-instanceid", "<your-instanceid>");
    # 5. Configure a request method.
    req.set_method("POST")
    # 6. Configure initialization parameters for an ASClient object. The parameter valu
es vary based on your environment. The timeout parameter specifies the time-out period for a request. The cert_file parameter specifies the certificate. The verify parameter specifies whether to verify the certificate.
    as_client = ASClient("<accesskeyid>", "<accesskeysecret>", "
<regionid>",timeout=1000,
            cert_file=None,
            verify=False)
    # Configure the identifier of the requester. This parameter is required and used on
ly for identification. You can set this parameter to a random value.
    as_client.setSdkSource("<The identifier of the requester>")
    response = as_client.do_request(req)
    print(response)
```

**Header parameters**

ake API calls

| Parameter | Description |
|---|---|
| x-acs-resourcegroupid | The ID of the resource set in the Apsara Uni- manager Management Console. |
| x-acs-organizationid | The ID of the organization in the Apsara Uni- manager Management Console. |
| x-acs-regionid | The ID of the region. For more information about how to obtain a region ID, see Query a region ID. |
| x-acs-instanceid | The ID of the instance on which you want to perform operations. |

**Configure proxies**

Perform the following steps to configure a proxy:
1. Import OS dependencies.

```java
import os
```

2. Configure one or more proxies.

```bash
# Before you make an API call, configure one or more proxies.
os.environ['http_proxy'] = "http://x.x.x.x:xxxx" os.environ['https_proxy'] = "https://x.x.x.x:xxxx"
```

#### 4.5.3 SDK for Node.js

This topic describes how to obtain and use Apsara Stack SDK for Node.js to call API operations.

**Preparations**

An authorized account and an AccessKey pair are obtained. The AccessKey pair consists of an AccessKey ID and an AccessKey secret. For more information about how to obtain an AccessKey pair in the Apsara Uni-manager Management Console, see Obtain an AccessKey pair. The endpoint of Apsara Stack API (ASAPI) is obtained. For more information, see Generate an endpoint for the ASAPI. The endpoint of ASAPI is obtained. For more information about how to obtain the endpoint of ASAPI, see Obtain the endpoint of ASAPI. For more information about how to obtain the region ID, see Obtain the endpoint of ASAPI.

**Add dependencies**

Run the following command to install Apsara Stack SDK for Node.js:

```
 tnpm i @ali/asapi-nodejs-sdk@0.0.33 --save
```

**Use Apsara Stack SDK for Node.js**

ake API calls The following sample code shows how to use Apsara Stack SDK for Node.js to make API calls:

```
// 1. Import the dependencies of Apsara Stack SDK for Node.js. const Controller = require('egg').Controller; const ASAPIClient = require('@ali/asapi-nodejs-sdk'); // 2. Configure the parameters. const cnofig = {
    API_GATEWAY: '<The endpoint of ASAPI>',
    regionId: '<The ID of the region in which the Apsara Stack service is deployed>',
    accessKeyId: '<The AccessKey ID of your Apsara Stack tenant account>',
    accessKeySecret: '<The AccessKey secret of your Apsara Stack tenant account>'
```

};

```json
// 3. Initialize a client for API calls. const AsapiClient = new ASAPIClient(cnofig, this.ctx); // 4. Configure request parameters. const params = {
    "Action": "<The name of the API operation>",
    "Product": "<The name of the service that provides the API operation>",
    "Version": "<The version of the API operation>",
    "regionId": '<The ID of the region in which the Apsara Stack service is deployed>',
    // When you use the STS AccessKey ID to call RPC API operations, you must add the S
ecurityToken parameter to the header.
    // "SecurityToken": "<your-securitytoken>",
      "<The name of the operation-specific parameter required by the API operation>": "
<The value of the operation-specific parameter>"
```

`}`

```
// 5. Configure request headers. // When you use the STS AccessKey ID to call ROA API operations, you must add the xacs-security-token parameter to the header. // AsapiClient.addHeader("x-acs-security-token", "<your-securitytoken>") AsapiClient.addHeader('x-acs-caller-sdk-source', '<The identifier of the requester>') AsapiClient.addHeader('x-acs-roleid', '<The ID of the role>') AsapiClient.addHeader('x-acs-userid', '<The ID of the user>') AsapiClient.addHeader('x-acs-organizationid', '<your-organizationid>') AsapiClient.addHeadert("x-acs-regionid", "<your-regionid>"); AsapiClient.addHeader("x-acs-resourcegroupid", "<your-resourcegroupid>"); AsapiClient.addHeader("x-acs-instanceid", "<your-instanceid>"); // 6. Make an API call and obtain the response. try {
  const res = await AsapiClient.doRequest(cnofig.API_GATEWAY, params, {
    method: 'POST', // The request method.
    formatParams: false, // Specifies whether to format parameters and capitalize the f
irst letter of each parameter.
    enableProxy: true, // Specifies whether to configure a proxy.
    proxy: 'http://x.x.x.x:xxxx',
    timeout: 10000, // The time-out period.
  // ca: , // The certificate issued by a certificate authority (CA). For more informat
ion, visit https://nodejs.org/api/https.html#https_https_request_options_callback.
```

`})`

```
  console.log(res)
} catch (e) {
  console.log(e)
```

ake API calls

**Disable certificate validation**

The following sample code shows how to disable certificate validation:

```
Configure the environment variable. NODE_TLS_REJECT_UNAUTHORIZED=0
```

**Request headers**

| Parameter | Description |
|---|---|
| x-acs-regionid | The ID of the region. For more information about how to obtain a region ID, see Query a region ID. |
| x-acs-organizationid | The ID of the organization in the Apsara Uni- manager Management Console. |
| x-acs-resourcegroupid | The ID of the resource set in the Apsara Uni- manager Management Console. |
| x-acs-instanceid | The ID of the instance on which you want to perform operations. |
| x-acs-caller-sdk-source | The custom name of the requester or the system. This parameter is used to identify the source of the API request. |
| x-acs-roleid | The ID of the role. |
| x-acs-userid | The ID of the user. |

#### 4.5.4 SDK for POP

This topic describes how to switch the gateway to ASAPI if an application uses SDK for POP to call cloud services.

**Procedure**

Reference the following sample code and add required common parameters and the **Product**
**Name** field to the request header. Then, run code to switch the gateway to ASAPI.

> **Note:** Each service uses a unique endpoint in SDK for POP. However, ASAPI provides only one endpoint. You cannot identify the service to which an API operation belongs based on the API operation name and the version number. For example, both ECS and KVStore for Redis provide the DescribeInstances API operation of the 2015-01-01 version.

**Sample code**

In the following example, an ECS API operation is called: ake API calls

```java
 try {
            DefaultProfile clientProfile = DefaultProfile.getProfile(regionId,
accessKeyId, accessKeySecret);
            // Set the ASAPI gateway. Format: server.asapi.aliyuns.com/asapi/v3.
            clientProfile.addEndpoint(region, region, "ecs", "<ASAPI gateway>");
            DefaultAcsClient acsClient = new DefaultAcsClient(clientProfile);
            DescribeImagesRequest request = new DescribeImagesRequest();
            request.setSysRegionId(regionId); // Or setRegionId(regionId)
            // Configure common parameters based on the information about the current
user.
            request.putHeaderParameter("x-acs-organizationid", "<Organization ID>");
            request.putHeaderParameter("x-acs-resourcegroupid", "<Resource group ID>");
            request.putHeaderParameter("x-ascm-product-name", "<Service name>");
            request.putHeaderParameter("x-ascm-product-version", "<API version");
            DescribeImagesResponse result = (DescribeImagesResponse)
acsClient.getAcsResponse(request);
            List<DescribeImagesResponse.Image> images = result.getImages();
            for (DescribeImagesResponse.Image image: images) {
                System.out.println(image.getImageId());
                System.out.println(image.getImageName());
```

`}`

```
        } catch (Exception e) {
            e.printStackTrace();
```

`}`

**Header parameters**

| Parameter | Description |
|---|---|
| x-ascm-product-name | The name of the service to which the API operation belongs. For more information about how to obtain the service name, see View the information about API operations. |
| x-ascm-product-version | The API version. For more information how to obtain the API version, see View the information about API operations. |
| x-acs-regionid | The region ID. For more information about how to obtain the region ID, see Query the region ID. |
| x-acs-organizationid | The ID of the organization in the Apsara Uni- manager Management Console. |
| x-acs-resourcegroupid | The ID of the resource set in the Apsara Uni- manager Management Console. |
| x-acs-instanceid | The ID of the instance on which you want to perform operations. |

ake API calls

#### 4.5.5 SDK for POP

### 4.6 HTTP requests

#### 4.6.1 Overview

This topic describes how to make API requests and is intended for users who use API URLs to initiate HTTP GET requests. If you are using an SDK to initiate requests, you can skip this topic. The request URL consists of different parameters and has a fixed syntax. The URL contains common request parameters, your signature, and operation-specific parameters. Sample request URLs are provided for each API operation. These URLs are not encoded to make them easy to read. Before you make a request, you must encode the request URL. After the authentication process is complete based on your signature, the results are returned to you. Response parameters are returned if the call is successful, whereas an error message is returned if the call fails. You can troubleshoot issues based on the error message.

#### 4.6.2 Request structure

You can use API URLs to initiate HTTP GET requests. Each URL must include request parameters. This topic describes the syntax of HTTP GET requests and provides the endpoint of ASAPI.

**Sample request**

GetOrganizationList is used in the following unencoded URL request:

```
https://public.asapi.aliyuns.com/asapi/v3? Action=GetOrganizationList&Product=ascm&Version=2019-05-10&Id=<Organization ID>&<Common parameters>
```

`https` : the protocol used to transmit the request. `public.asapi.aliyuns.com/asapi/v3` : the endpoint of ASAPI. `Action=GetOrganizationList Product=ascm Version=2019-05-10` : the API operation. `Id` : the ID of the organization. `<Common request parameters>` : common parameters specified in the system.

**Protocols**

ASAPI supports only the HTTP request protocol.

**Endpoints**

For more information about how to obtain the endpoint of ASAPI, see Generate an endpoint for ASAPI. You must use the `Action, Product, and Version` parameters to specify an API operation. For example, you can set `Action to GetOrganizationList, Product to ascm, and Version to` `2019-05-10` . You must also specify other operation-specific request parameters and common request parameters. For more information, see Common request parameters. ake API calls

#### 4.6.3 Request signatures

This topic describes how to sign HTTP API requests. ASAPI uses the request signature to verify the identity of the request sender. ASAPI implements symmetric encryption by using an AccessKey pair to verify the identity of the request sender.

> **Note:** An AccessKey pair consists of an AccessKey ID and an AccessKey secret, which are issued to each user or organization in the Apsara Uni-manager Management Console.
> The AccessKey ID is used to verify identities of users, and the AccessKey secret is used to encrypt and verify signature strings. You must keep your AccessKey secret confidential.
> ASAPI provides SDKs for Node.js, Python, and Java to facilitate complex signature calculation. For more information, see Obtain the core package for ASAPI.

**Step 1: Create a canonicalized query string**

1. Arrange the request parameters in alphabetical order, including all common and operation-
specific parameters except the `Signature` parameter.

> **Note:** If you use the GET method to send a request,these parameters are connected by ampersands (&) and included in the request URL. The first request parameter follows a question mark (?).

2. Encode the request parameters and their values in UTF-8 based on RFC 3986. The following
rules apply in the encoding process: Letters, digits, and special characters such as hyphens ( `-` ), underscores ( `_` ), and periods ( `.` ) do not need to be encoded. Other characters must be percent encoded in the %XY format. `XY` represents the ASCII code of the characters in hexadecimal notation. For example, double quotation marks ( `"` ) are encoded as %22 . Extended UTF-8 characters are encoded in the %XY%ZA… format. Spaces must be encoded as %20 . Do not encode spaces as plus signs ( `+` ). This encoding method is similar to but different from the `application/x-www-form-` `urlencoded` MIME encoding algorithm. If you use `java.net.URLEncoder` from the Java standard library, use `percentEncode` to encode request parameters and their values. In the encoded query string, replace the plus signs ( `+` ) with %20 , asterisks ( `*` ) with %2A , and %7E with tildes ( ~ ). This way, you can obtain an encoded string that matches the preceding encoding rules.

```java
private static final String ENCODING = "UTF-8"; private static String percentEncode(String value) throws UnsupportedEncodingException {
    return value != null ? URLEncoder.encode(value, ENCODING).replace("+", "%20").r
eplace("*", "%2A").replace("%7E", "~") : null;
```

ake API calls
3. Use equal signs ( `=` ) to connect the encoded request parameters and their values.
4. Use ampersands ( `&` ) to connect the encoded request parameters. These parameters
must be arranged in the same order as those in Step 1. Then, a canonicalized query string that follows the request structure is obtained. For more information, see Request structure.

**Step 2: Create a string-to-sign**

1. Create a `string-to-sign` . You can also use `percentEncode` to encode the canonicalized
query string created in Step 1 based on the following rules:

```
StringToSign=
    HTTPMethod + "&" + //HTTPMethod: the HTTP method that is used to send a request,
such as GET.
    percentEncode("/") + "&" + //percentEncode("/"): Encode the forward slash (/) in
UTF-8 as %2F.
    percentEncode(CanonicalizedQueryString) // Encode the canonicalized query string
created in Step 1.
```

2. Calculate the RFC 2104-compliant HMAC-SHA1 or HMAC-256 value of `StringToSign` . In
the following example, Java Base64 is used:

```
String signature = Base64.getEncoder().encodeToString(signData);
```

> **Note:** When you calculate the signature, the key value specified by RFC 2104 is your
> `AccessKey secret` plus an ampersand (&), which has an ASCII value of 38. For more information, see Obtain an AccessKey pair.

3. Encode the `Signature` parameter based on RFC 3986 and add it to the canonicalized
query string.

**Example 1: Concatenate parameters**

| GetOrganizationList |   | is used in this |
|---|---|---|
| is set to testid and |   |   |

`GetOrganizationList` is used in this example to query regions. For example, `AccessKeyID` is set to testid and `AccessKeySecret` is set to testsecret. Perform the following operations:
1. Construct a canonicalized query string.

```
https://public.asapi.aliyuns.com/asapi/v3/? AccessKeyId=testid&Action=GetOrganizationList&Format=JSON&Id=1&Product=ascm&RegionId=cn region-test&SignatureMethod=HMAC-SHA1&SignatureNonce=43967c6e-e3ad-44fa-b06b-fcf3db5f 39d2&SignatureVersion=1.0&Timestamp=2020-09-15T08%3A50%3A40Z&Version=2019-05-10
```

2. Create a `string-to-sign` .

```
GET&%2F&AccessKeyId%3Dtestid%26Action%3DGetOrganizationList%26Format%3DJSON%26Id%3D1%26 oduct%3Dascm%26RegionId%3Dcn-region-test%26SignatureMethod%3DHMAC- SHA1%26SignatureNonce%3D43967c6e-e3ad-44fa-b06bfcf3db5f39d2%26SignatureVersion%3D1.0%26Timestamp%3D2020-09- 15T08%253A50%253A40Z%26Version%3D2019-05-10
```

3. Calculate the signature.
ake API calls Calculate the signature. The key value used for calculation is `testsecret&` because `AccessKeySecret` is set to testsecret. The calculated signature is `OLeaidS1JvxuMvnyHOwuJ+uX5qY=` . Java Base64 is used in the following sample code:

```
 String signature = Base64.getEncoder().encodeToString(signData);  Encode
```

`Signature=hvqv9Ll5RE6kQ4YsQXFAf9VuRIY=` based on RFC 3986 and add it to the canonicalized query string.

```
https://public.asapi.aliyuns.com/asapi/v3/? AccessKeyId=testid&Action=GetOrganizationList&Format=JSON&Id=1&Product=ascm&RegionId=cn region-test&SignatureMethod=HMAC-SHA1&SignatureNonce=43967c6e-e3ad-44fa-b06b-fcf3db5f 39d2&SignatureVersion=1.0&Timestamp=2020-09-15T08%3A50%3A40Z&Version=2019-05-10
```

You can use browsers or tools such as cURL and Wget to initiate an HTTP request for calling the `DescribeRegions` operation to query the Alibaba Cloud region list.

**Example 2: Use the standard library of the programming language**

| GetOrganizationList |   | is used in t |
|---|---|---|

`GetOrganizationList` is used in this example to query regions. For example, `AccessKeyID` is set to testid, `AccessKeySecret` is set to testsecret, and all request parameters are stored

| Map<String, String> |   |   |
|---|---|---|
|   |   | o |

1. Predefine an encoding method.

```java
private static final String ENCODING = "UTF-8"; private static String percentEncode(String value) throws UnsupportedEncodingException
```

`{`

```
        return value != null ? URLEncoder.encode(value, ENCODING).replace("+",
"%20").replace("*", "%2A").replace("%7E", "~") : null;
```

`}`
2. Predefine the time format for the `Timestamp` parameter. Specify the `Timestamp`
parameter in the ISO 8601 format. The time must be in UTC+0.

```java
private static final String ISO8601_DATE_FORMAT = "yyyy-MM-dd'T'HH:mm:ss'Z'"; private static String formatIso8601Date(Date date) {
    SimpleDateFormat df = new SimpleDateFormat(ISO8601_DATE_FORMAT);
    df.setTimeZone(new SimpleTimeZone(0, "GMT"));
    return df.format(date);
```

`}`
3. Create a request string.
ake API calls

```
final String HTTP_METHOD = "GET"; Map parameters = new HashMap(); // Specify request parameters. parameters.put("Product", "ascm"); parameters.put("Action", "GetOrganizationList"); parameters.put("Version", "2019-05-10"); parameters.put("AccessKeyId", "testid"); parameters.put("RegionId", "cn-region-test"); parameters.put("Timestamp", formatIso8601Date(new Date())); parameters.put("SignatureMethod", "HMAC-SHA1"); parameters.put("SignatureVersion", "1.0"); parameters.put("SignatureNonce", UUID.randomUUID().toString()); parameters.put("Format", "JSON"); parameters.put("Id", "1"); // Arrange request parameters. String[] sortedKeys = parameters.keySet().toArray(new String[]{}); Arrays.sort(sortedKeys); final String SEPARATOR = "&"; // Create a string-to-sign. StringBuilder stringToSign = new StringBuilder(); stringToSign.append(HTTP_METHOD).append(SEPARATOR); stringToSign.append(percentEncode("/")).append(SEPARATOR); StringBuilder canonicalizedQueryString = new StringBuilder(); for(String key : sortedKeys) {
    // Encode the key and the value.
    canonicalizedQueryString.append("&")
    .append(percentEncode(key)).append("=")
    .append(percentEncode(parameters.get(key)));
```

`}`

```
//Encode the canonicalized query string. stringToSign.append(percentEncode( canonicalizedQueryString.toString().substring(1)));
```

4. The signature. The key value used for calculation is `testsecret&` because

| AccessKeySecret | is set to testsecre |
|---|---|

```
 OLeaidS1JvxuMvnyHOwuJ%2BuX5qY%3D .
// The following sample code shows how to calculate the signature: final String ALGORITHM = "HmacSHA1"; final String ENCODING = "UTF-8"; key = "testsecret&"; Mac mac = Mac.getInstance(ALGORITHM); mac.init(new SecretKeySpec(key.getBytes(ENCODING), ALGORITHM)); byte[] signData = mac.doFinal(stringToSign.getBytes(ENCODING)); String signature = Base64.getEncoder().encodeToString(signData);
```

Encode the Signature parameter based on RFC 3986 and add it to the canonicalized query string. The following URL is obtained:

```
https://public.asapi.aliyuns.com/asapi/v3/? AccessKeyId=testid&Action=GetOrganizationList&Format=JSON&Id=1&Product=ascm&RegionId=cn region-test&SignatureMethod=HMAC-SHA1&SignatureNonce=43967c6e-e3ad-44fa-b06b-fcf3db5f 39d2&SignatureVersion=1.0&Timestamp=2020-09-15T08%3A50%3A40Z&Version=2019-05-10
```

ake API calls
5. Use browsers or tools such as cURL and Wget to initiate an HTTP request.

#### 4.6.4 Responses

Responses are returned only in the JSON format. If a return code is greater than or equal to 200 and less than 300, a success response is returned. Otherwise, an error response is returned.

**Sample success responses**

If a request is successful, the request ID and operation-specific parameter values are returned. For more information, see the developer guide of the corresponding Apsara Stack service.

```json
   "successResponse":true,
  "eagleEyeTraceId":"xxxxxxxxxxxxxx",
  "asapiSuccess":true,
  "code":"200",
  "cost":12,
  "asapiRequestId":"xxxxxxxxxxxxxx",
  "data":[
```

`{`

```json
      "muserId":"aliyuntest",
      "internal":false,
      "level":"0",
      "supportRegions":"cn-*",
      "personNum":100,
      "mtime":1553247962000,
      "uuid":"1",
      "parentId":0,
      "supportRegionList":[
        "cn-*"
```

`],`

```json
      "name":"root",
      "alias":"root",
      "ctime":1553247962000,
      "id":1,
      "resourceGroupNum":100,
      "cuserId":"aliyuntest"
```

`}` `],`

```json
  "requestId":"xxxxxxxxxxxxxx",
  "success":true,
  "message":"success"
```

`}`

**Sample error responses**

If a request fails, the following information is returned. For more information, see the developer guide of the corresponding Apsara Stack service. ake API calls `{`

```json
    "code": "asapi.server.api.notfound",// The error code.
    "eagleEyeTraceId": "xxx-xxx-xxx-xxx", // The trace ID provided by EagleEye.
    "asapiSuccess": false, // Indicates whether the request is successful.
    "hostId": "xxxx", // The ID of the host.
    "message": "Failed to ....", // The message returned.
    "asapiErrorMessage": "Failed to ....", // The error message provided by ASAPI.
    "asapiErrorCode": "asapi.server.api.notfound" // The error code provided by ASAPI.
```

`}`

## 5 API references

### 5.1 List of operations by function

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

### 5.2 Make API requests

#### 5.2.1 Request syntax

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
ampersands (&). Request parameters include common parameters and operation-specific parameters. Common parameters include the API version and authentication information. For more information about common parameters, see Common parameters. The following example demonstrates how to call the DescribeIpv6Gateways operation to query IPv6 gateways.

> **Note:** The sample requests are formatted to improve readability.

```
https://vpc.example.com/?Action=DescribeIpv6Gateways &Format=xml &Version=2016-04-28 &Signature=xxxx%xxxx%3D &SignatureMethod=HMAC-SHA1 &SignatureNonce=15215528852396 &SignatureVersion=1.0 &AccessKeyId=key-test &Timestamp=2012-06-01T12:00:00Z
```

#### 5.2.2 API authorization

To ensure the security of your account, we recommend that you call IPv6 Gateway API operations as a RAM user. To call the IPv6 Gateway API as a RAM user, you must create and add an authorization policy that grants permissions to call specific API operations. For more information about the IPv6 Gateway resources and API operations that allow the authorization, see RAM authentication.

#### 5.2.3 Sign an API request

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

### 5.3 RAM authentication

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

| 1 | > Document Version: 2023112 |
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

### 5.4 common parameters

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

### 5.5 IPv6 gateways

#### 5.5.1 CreateIpv6Gateway

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

#### 5.5.2 DescribeIpv6Gateways

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

#### 5.5.3 DescribeIpv6GatewayAttribute

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

#### 5.5.4 ModifyIpv6GatewayAttribute

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

#### 5.5.5 ModifyIpv6GatewaySpec

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

#### 5.5.6 DeleteIpv6Gateway

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

#### 5.5.7 DescribeIpv6EgressOnlyRules

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

#### 5.5.8 CreateIpv6EgressOnlyRule

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

#### 5.5.9 DeleteIpv6EgressOnlyRule

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

#### 5.5.10 AllocateIpv6InternetBandwidth

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

#### 5.5.11 ModifyIpv6AddressAttribute

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

#### 5.5.12 DeleteIpv6InternetBandwidth

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

#### 5.5.13 DescribeIpv6Addresses

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

#### 5.5.14 ModifyIpv6InternetBandwidth

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
