---
title: "Alibaba Cloud Apsara Stack Enterprise V3.12.0 Auto Scaling Developer Guide 20220928"
product_version: "V3.12.0"
doc_version: "20220928"
pdf_pages: 106
source_pdf: "Alibaba Cloud Apsara Stack Enterprise V3.12.0 Auto Scaling Developer Guide 20220928.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/01_ApsaraStackEnterprise/V3.12/%E5%BC%B9%E6%80%A7%E8%AE%A1%E7%AE%97/Alibaba%20Cloud%20Apsara%20Stack%20Enterprise%20V3.12.0%20Auto%20Scaling%20Developer%20Guide%2020220928.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes+edge-junk)
---

# Alibaba Cloud Apsara Stack Enterprise V3.12.0 Auto Scaling Developer Guide 20220928

## Table of Contents

- 1 Call SDKs for cloud services by using ASAPI
  - 1.1 ASAPI
    - 1.1.1 Overview
    - 1.1.2 Log on to the API Tool console
    - 1.1.3 View the information about API operations
    - 1.1.4 Obtain the endpoint of ASAPI
    - 1.1.5 Obtain the core package for ASAPI
    - 1.1.6 Obtain an AccessKey pair
    - 1.1.7 Query the region ID
    - 1.1.8 SDK for Java
    - 1.1.9 SDK for Node.js
    - 1.1.10. (Optional) Switch the gateway to ASAPI in POP SDK
- 2 API reference
  - 2.1 API Reference
    - 2.1.1 API usage instructions
    - 2.1.2 Make API requests
    - 2.1.3 Request structure
    - 2.1.4 Common parameters
      - 2.1.4.1 Common request parameters
      - 2.1.4.2 Common response parameters
    - 2.1.5 Responses
      - 2.1.5.1 Successful response examples
      - 2.1.5.2 Sample error responses
    - 2.1.6 Request signatures
    - 2.1.7 Scaling groups
      - 2.1.7.1 CreateScalingGroup
      - 2.1.7.2 ModifyScalingGroup
      - 2.1.7.3 EnableScalingGroup
      - 2.1.7.4 DisableScalingGroup
      - 2.1.7.5 DeleteScalingGroup
      - 2.1.7.6 DescribeScalingGroups
      - 2.1.7.7 DescribeScalingInstances
      - 2.1.7.8 DescribeScalingActivities
    - 2.1.8 Scaling configurations
      - 2.1.8.1 CreateScalingConfiguration
      - 2.1.8.2 DescribeScalingConfigurations
      - 2.1.8.3 DeleteScalingConfiguration
    - 2.1.9 Scaling rules
      - 2.1.9.1 CreateScalingRule
      - 2.1.9.2 ModifyScalingRule
      - 2.1.9.3 DescribeScalingRules
      - 2.1.9.4 DeleteScalingRule
    - 2.1.10 Scaling tasks
      - 2.1.10.1 ExecuteScalingRule
      - 2.1.10.2 AttachInstances
      - 2.1.10.3 RemoveInstances
      - 2.1.10.4 DetachInstances
    - 2.1.11 Scheduled tasks
      - 2.1.11.1 CreateScheduledTask
      - 2.1.11.2 ModifyScheduledTask
      - 2.1.11.3 DescribeScheduledTasks
      - 2.1.11.4 DeleteScheduledTask
    - 2.1.12 Error codes
      - 2.1.12.1 Client errors
      - 2.1.12.2 Server errors
    - 2.1.13 Ensure idempotence

services by using ASAPI

## 1 Call SDKs for cloud services by using ASAPI

by using ASAPI

### 1.1 ASAPI

#### 1.1.1 Overview

This topic describes the architecture and features of Apsara Stack API (ASAPI). ASAPI is a platform that integrates all features and is the only portal to connect to Apsara Stack. ASAPI can categorize, audit, and manage API operations. It can also assemble and customize existing operations and adapt to your operations. Each cloud service can call ASAPI for required data and features, which avoids inconsistent operations caused by different calling methods and separate encapsulation. This can ensure the operation program integrity and improve development efficiency and code portability. services by using ASAPI ASAPI allows you to manage and call operations in a centralized manner and customize development. ASAPI supports access to most cloud services deployed in Apsara Stack and supports passthrough or encapsulation of different backend APIs. This way, operations can be called using the same method. ASAPI allows you to use SDKs and API portals to call APIs registered on ASAPI, customize SDKs, and manage versions of Apsara Stack, services, and APIs.

#### 1.1.2 Log on to the API Tool console

You can log on to the API Tool console through the Apsara Stack Cloud Management (ASCM) console. Prerequisites Before you log on to the Apsara Uni-manager Management Console, the endpoint of the console is obtained from the deployment staff. We recommend that you use Google Chrome. Procedure
1. Enter the URL of the Apsara Uni-manager Management Console in the address bar and press the
Enter key.
2. Enter your username and password.
Obtain the username and password that you use to log on to the Apsara Uni-manager Management Console from the operations administrator. Not e The first time that you log on to the Apsara Uni-manager Management Console, you must change the password of your account. For security purposes, your password must meet the minimum complexity requirements. The password must be 10 to 32 characters in length and must contain at least two of the following character types: Uppercase or lowercase letters Digits Special characters, including exclamation points (!), at signs (@), number signs (#), dollar signs ($), and percent signs (%)
3. Click Log On.
4. In the top navigation bar, choose Product s > Ot hers > API T ool.

#### 1.1.3 View the information about API operations

You must obtain a service name, API operation name, and API version. All the information is required when you use SDKs. Procedure
1. Log on to the API Tool console.
2. In the left-side navigation pane, click API f old.
3. On the API Direct ory page, select the target service from the drop-down list, enter the API
operation name in the search box, and then click the search icon. services by using ASAPI
4. View and remember the service name, API operation name, and API version.

#### 1.1.4 Obtain the endpoint of ASAPI

You can obtain the endpoint of Apsara Stack API (ASAPI) in the Apsara Stack Operations (ASO) console. Procedure
1. In the address bar, enter the URL region-id.aso.intranet-domain-id.com and press the Enter key.
Not e You can select a language from the drop-down list in the upper-right corner of the page.
2. Enter your username and password.
Not e Obtain the username and password for logging on to the ASO console from the deployment personnel or an administrator. When you log on to the ASO console for the first time, you must change the password of your username as prompted. To enhance security, a password must meet the following requirements: It must contain uppercase and lowercase letters. It must contain digits. It must contain special characters such as exclamation points (!), at signs (@), number signs (#), services by using ASAPI dollar signs ($), and percent signs (%). It must be 10 to 20 characters in length.
3. Click Log On to go to the ASO console.
4. In the left-side navigation pane, choose Product s > Product List . On the Product List page, click
Apsara Inf rast ruct ure Management Framework.
5. In the left-side navigation pane of the Apsara Infrastructure Management Framework console, click
Report s.
6. On the All Report s page, search for Regist rat ion Vars of Services. Click Regist rat ion Vars of
Services.
7. On the Regist rat ion Vars of Services page, click the
icon next to Service. In the dialog box that appears, search for asapi.
8. Right-click the Service Regist rat ion column corresponding to asapi and select Show More.
9. In the Det ails dialog box, view the value of asapi.gat eway.endpoint . The value is the logon URL
of the Apsara ASAPI Management platform. services by using ASAPI

#### 1.1.5 Obtain the core package for ASAPI

Apsara Stack uses Apsara Stack API (ASAPI) as a unified portal for all Apsara Stack products that are connected to ASAPI. ASAPI also provides SDKs to call product APIs. For more information about how to obtain the core package for ASAPI, see Apsara Stack documentation.

#### 1.1.6 Obtain an AccessKey pair

An AccessKey pair consists of an AccessKey ID and an AccessKey secret. The AccessKey pair is used to implement symmetric encryption to verify the identity of the requester. The AccessKey ID is used to identify a user. The AccessKey secret is used to encrypt the signature string. This topic describes how to obtain the AccessKey pair of an organization. Prerequisites Only operations administrators and level-1 organization administrators can obtain the AccessKey pair of an organization. Obtain the AccessKey pair of an organization To obtain the AccessKey pair of an organization, perform the following operations:
1. Log on to the Apsara Stack Cloud Management (ASCM) console as an administrator.
2. In the top navigation bar, click Ent erprise.
3. In the left-side navigation pane of the Ent erprise page, click Organizat ions.
4. In the Organizations navigation tree, click the
icon on the right of the organization to be added.
5. Select AccessKey.
6. In the message that appears, view the AccessKey pair of the organization.
Not e An AccessKey pair is automatically allocated to a level-1 organization. Subordinate organizations use the same AccessKey pair as their level-1 organization. services by using ASAPI Obtain the AccessKey pair of a personal account To obtain the AccessKey pair of a personal account, perform the following operations:
1. Log on to the ASCM console as an administrator.
2. In the upper-right corner of the homepage, move the pointer over the profile picture and click User
Inf ormat ion.
3. In the Apsara St ack AccessKey Pair section of the User Information page, view your AccessKey
pair. Not e The AccessKey pair consists of an AccessKey ID and an AccessKey secret. They allow you to access Apsara Stack resources with full permissions for your account. You must keep them confidential.

#### 1.1.7 Query the region ID

You must specify the region ID when you call Apsara Stack SDK for Node.js. You must query the region ID in the Apsara Stack Cloud Management (ASCM) console. Procedure
1. Log on to the ASCM console as an administrator.
2. In the upper-right corner of the homepage, move the pointer over the profile picture and click User
Inf ormat ion.
3. In the Apsara St ack AccessKey Pair section, you can view the region ID.

#### 1.1.8 SDK for Java

This topic describes how to obtain and use Apsara Stack SDK for Java to call API operations. Prerequisites The following operations are performed: Obtain an authorized account. Obtain an AccessKey pair. Obtain the endpoint of Asapi. Make sure that JDK V1.6 or later is used. Add dependencies services by using ASAPI If you use Apache Maven to manage Java projects, you must add the following dependencies to the pom.xml file:

```xml
<dependency>
    <groupId>com.aliyun</groupId>
    <artifactId>asapi</artifactId>
    <version>0.0.3-RELEASE</version>
</dependency>
```

SDK for Java usage Perform the following operations to use SDK for Java to call API operations:
1. Configure parameters.
2. Create an ASClient instance for initiating requests.
3. Initiate a request and obtain the response.
Sample code You can call API operations on ASAPI by using GET and POST requests. The following example shows a GET request:

```
// Obtain the endpoint of ASAPI. String endpoint = "<asapi-endpoint>"; // Enter the obtained ASAPI endpoint. // Configure request parameters. Map<String, String> parameters = new HashMap<String, String>(); // Configure parameters for the service. parameters.put("Product", "ess"); // The service name must be the same as that displayed in the corresponding API directory. parameters.put("Action", "DescribeScalingGroups"); // The API operation name, wh ich is case-sensitive and must be the same as that displayed in the API directory. parameters.put("Version", "2014-08-28"); // Enter the API version. // Configure authorization-related parameters. parameters.put("AccessKeyId", "<your-access-key-id>"); // Enter the AccessKey ID of the authorized account. parameters.put("AccessKeySecret", "<your-access-key-secret>"); // Enter the AccessKey se cret of the authorized account. parameters.put("RegionId", "<Region>"); // The region ID. // Configure business parameters. parameters.put("ScalingGroupId.1", "<your-scalinggroupId>"); // The ID of the scaling group whose information you want to obtain. // Create an ASClient instance for initiating requests. ASClient client = new ASClient(); // Initiate a request and obtain the response (the first form). String result = client.doGet(endpoint, parameters); // Initiate a request and obtain the response (the second form). String result = client.doRequest(endpoint, parameters);
```

The following example shows a POST request: services by using ASAPI

```
// Obtain the endpoint of ASAPI. String endpoint = "<asapi-endpoint>"; // Enter the obtained ASAPI endpoint. // Configure request parameters. Map<String, String> parameters = new HashMap<String, String>(); // Configure parameters for the service. parameters.put("Product", "ess"); // The service name must be the same as that displayed in the corresponding API directory. parameters.put("Action", "DescribeScalingGroups"); // The API operation name, wh ich is case-sensitive and must be the same as that displayed in the API directory. parameters.put("Version", "2014-08-28"); // Enter the API version. // Configure authorization-related parameters. parameters.put("AccessKeyId", "<your-access-key-id>"); // Enter the AccessKey ID of the authorized account. parameters.put("AccessKeySecret", "<your-access-key-secret>"); // Enter the AccessKey se cret of the authorized account. parameters.put("RegionId", "<your-regionid>"); // The region ID. // Configure business parameters. parameters.put("ScalingGroupId.1", "<your-scalinggroupId>"); // The ID of the scaling group of which you want to obtain information. // Create an ASClient instance for initiating requests. ASClient client = new ASClient(); // Add request headers. client.addHeader("x-acs-regionid", "<your-regionid>"); client.addHeader("x-acs-organizationid", "<your-organizationid>"); client.addHeader("x-acs-resourcegroupid", "<your-resourcegroupid>"); client.addHeader("x-acs-scalinggroupid", "<your-scalinggroupid>"); // Initiate a request and obtain the response. String result = client.doPost(endpoint, parameters);
```

Header parameters

| Parameter | Description |
|---|---|
| x-acs-regionid | The region ID. For information about how to obtain the region ID, see Query the region ID. |
| x-acs-organizat ionid | The organization ID in the ASCM console. |
| x-acs-resourcegroupid | The ID of the resource set in the ASCM console. |
| x-acs-scalinggroupid | The ID of the target scaling group. |

#### 1.1.9 SDK for Node.js

This topic describes how to obtain and use Apsara Stack SDK for Node.js to call API operations. Prerequisites The following operations are performed: Obtain an authorized account. Obtain an AccessKey pair. services by using ASAPI Obtain the endpoint of Asapi. Query the region ID. Add dependencies
1. Install SDK for Node.js.

```
 tnpm install --save @ali/asapi-nodejs-sdk
```

2. If your application is dependent on the Egg.js framework, add dependencies to the mocha.opts
file.

```
--recursive --colors --timeout 60000 --reporter mochawesome --require co-mocha --require egg-ts-helper/register --require espower-typescript/guess --require intelli-espower-loader
```

SDK for Node.js usage Perform the following operations to use SDK for Node.js to call API operations:
1. Create an ASClient instance for initiating requests.
To create a client instance, you must configure the region ID, endpoint, AccessKey ID, and AccessKey secret in the config.ts file. Example:

```
local: {
    regionId: 'cn-qingdao-****',
    API_GATEWAY: '<asapi-endpoint>',
    accessKeyId: '<your-access-key-id>',
    accessKeySecret: '<your-access-key-secret>',
```

`},`
2. Configure parameters.
3. Initiate a request and obtain the response.
Sample code Example: services by using ASAPI

```
// Obtain the endpoint of ASAPI. const API_GATEWAY = "<asapi-endpoint>" // Create a Remote Procedure Call (RPC) client. const asapiClient = ctx.service.sdk.rpcClient; // Configure parameters. let params = {
    Action: 'DescribeScalingGroups',
    Product: 'ess',
    regionId: 'cn-qingdao-****',
    accessKeyId: '<your-access-key-id>',
    accessKeySecret: '<your-access-key-secret>',
    Version: '2014-08-28',
```

};

```
// Configure request headers. asapiClient.addHeader("x-acs-regionId", "cn-qingdao-****"); // Initiate a request and obtain the response. const result = await asapiClient.doRequest(API_GATEWAY, params, {});
```

1.1.10. (Optional) Switch the gateway to ASAPI in POP SDK If an application used POP SDK to call API operations, you must switch the gateway to ASAPI by performing the operations described in this topic. Procedure Refer to the following sample code and add required common parameters and the service name field to the request header. Use the code to switch the gateway to ASAPI. Not e Each service corresponds to a unique domain name in POP SDK. However, ASAPI provides only one domain name. You cannot identify the service to which an API operation belongs based on the API operation name and the version number. For example, both ECS and KVStore for Redis provide the DescribeInstances operation of the 2015-01-01 version. Sample code The following example shows how to call ESS API operations: services by using ASAPI

```java
 try {
            DefaultProfile clientProfile = DefaultProfile.getProfile(regionId, accessKeyId,
accessKeySecret);
            // Configure the ASAPI gateway. Format: server.asapi.${intranet-domain}.
            clientProfile.addEndpoint(region, "ess", "<ASAPI gateway>");
            DefaultAcsClient acsClient = new DefaultAcsClient(clientProfile);
            DescribeScalingGroupsRequest request = new DescribeScalingGroupsRequest();
            request.setSysRegionId(regionId); // Or setRegionId(regionId).
            // Configure common parameters based on the information about the current user.
            rrequest.putHeaderParameter("x-acs-organizationid", "<Organization ID>");
            request.putHeaderParameter("x-acs-resourcegroupid", "<Resource set ID>");
            request.putHeaderParameter("x-ascm-product-name", "<Service name>");
            request.putHeaderParameter("x-ascm-product-version", "<API version");
            request.putHeaderParameter("x-ascm-product-ak", "<AccessKey ID>");
            request.putHeaderParameter("x-ascm-product-sk", "<AccessKey Secret>");
            DescribeScalingGroupsResponse result = (DescribeScalingGroupsResponse) acsClien
t.getAcsResponse(request);
            List<DescribeScalingGroupsResponse.ScalingGroup> scalinggroups = result.getScal
ingGroups();
            for (DescribeScalingGroupsResponse.ScalingGroup scalinggroup: scalinggroups) {
                System.out.println(scalinggroup.getScalingGroupId());
                System.out.println(scalinggroup.getScalingGroupName());
```

`}`

```
        } catch (Exception e) {
            e.printStackTrace();
```

`}` Header parameters

| Parameter | Description |
|---|---|
| x-ascm-product -name | The name of the service to which the API operation belongs. |
| x-ascm-product -version | The API version. |
| x-ascm-product -ak | The AccessKey ID of the organization in the ASCM console. |
| x-ascm-product -sk | The AccessKey secret of the organization in the ASCM console. |

## 2 API reference

### 2.1 API Reference

#### 2.1.1 API usage instructions

Before you call ESS API operations, you must be granted the ESS API permissions in the ESS console. If you are not authorized, the following error codes will be returned. Error code description

| Description | Error code | Error message | HTTP status code |
|---|---|---|---|
| The error message returned because ESS is not activated and you are not authorized to call this operation. | Forbidden.Unsubscribed | Do not have permission to access this API. | 403 |
| The error message returned because you are not authorized to call ESS API operations. | Forbidden.Unauthorized | A required authorization for the specified action is not supplied. | 403 |

#### 2.1.2 Make API requests

Call an ESS API operation, send an HTTP GET request to the ESS API server, and add corresponding parameters to the request based on the description of the corresponding API operation. After the request is processed, the system will return a result.

#### 2.1.3 Request structure

This topic describes the structure of an API request. Endpoints For information about how to obtain an endpoint, see Generate the endpoint of ASAPI. Protocols You can send requests over HTTP or HTTPS. For a higher level of security, we recommend that you send requests over HTTPS. Methods You can use the HTTP GET method to send the request for calling an API operation. If you use this method, the request parameters must be included in the URL of the request. Parameters For each request, you must specify the operation that you want to perform, such as CreateScalingGroup. Additionally, each request must contain the common request parameters and operation-specific request parameters. Encoding All requests and responses are encoded in UTF-8.

#### 2.1.4 Common parameters

##### 2.1.4.1 Common request parameters

Common request parameters must be included in all Auto Scaling API requests. Description

| Parameter | Type | Required | Description |
|---|---|---|---|
| Format | String | No | The format in which to return the response. Valid values: JSON and XML. Default value: XML. |
| Version | String | Yes | The version number of the API. The format is YYYY-MM-DD. The version is 2014-08-28. |
| AccessKeyId | String | Yes | The AccessKey ID provided to you by Alibaba Cloud. |
| Signature | String | Yes | The signature string of the current request. For more information about how signatures are calculated, see the "Request signatures" section. |
| SignatureMethod | String | Yes | The encryption method of the signature string. Set the value to HMAC- SHA1. |
| Timestamp | String | Yes | The timestamp of the request. Specify the time in the ISO 8601 standard in the YYYY- MM-DDThh:mm:ssZ format. The time must be in UTC. For example, 20:00:00, August 28, 2014, UTC+8 will be written as 2014-08- 28T12:00:00Z. |

| Parameter | Type | Required | Description |
|---|---|---|---|
| SignatureVersion | String | Yes | The version of the signature encryption algorithm. Set the value to 1.0. |
| SignatureNonce | String | Yes | A unique, random number used to prevent replay attacks. You must use different numbers for different requests. |

XML format

```
https://ess.example.com/ ?Format=xml &Version=2014-08-28 &Signature=Pc5WB8gokVn0xfeu%2FZV%2BiNM1**** &SignatureMethod=HMAC-SHA1 &SignatureNonce=1521552885**** &SignatureVersion=1.0 &AccessKeyId=key-test &Timestamp=2014-08-28T12:00:00Z
```

##### 2.1.4.2 Common response parameters

Every response returns a unique RequestID regardless of whether the call is successful. XML format

```xml
<?xml version="1.0" encoding="UTF-8"? > <!--Root node of the response--> <Operation name+Response>
    <!--Response tag-->
    <RequestId>4C467B38-3910-447D-87BC-AC049166F216</RequestId>
    <!--Responses-->
</Operation name+Response>
```

JSON format `{`

```json
    "RequestId": "4C467B38-3910-447D-87BC-AC049166F216",
    /* Responses */
```

`}`

#### 2.1.5 Responses

##### 2.1.5.1 Successful response examples

API responses use the HTTP response format where a 2xx status code indicates a successful call and a 4xx or 5xx status code indicates a failed call. Responses can be returned in either the JSON or XML format. You can specify the response format in the request. The default response format is XML. Not e Sample responses in our API documents are formatted in a way that is easier for you to read. The actual responses are not formatted with line breaks or indentation. Responses in the XML format include information about whether the request succeeds and specific service data.

```xml
<?xml version="1.0" encoding="UTF-8"? > <!--Result Root Node--> <Operation Name+Response>
    <!--Return Request Tag-->
    <RequestId>4C467B38-3910-447D-87BC-AC049166F216</RequestId>
    <!--Return Result Data-->
</Operation Name+Response>
```

JSON format `{`

```json
    "RequestId": "4C467B38-3910-447D-87BC-AC049166F216",
    /* Return Result Data */
```

`}`

##### 2.1.5.2 Sample error responses

When an error occurs during an API call, no result data is returned. You can locate the cause of an error based on the error codes defined by each API operation, the error code table in the appendix Client errors, and Server errors. When an error occurs on an HTTP request for an API operation, a 4xx or 5xx HTTP status code is returned. The response body includes the error code and error message. The response body also contains a globally unique request ID (RequestId) and the ID of the site you accessed with this request (HostId). XML format

```xml
<?xml version="1.0" encoding="UTF-8"? > <Error>
   <RequestId>8906582E-6722-409A-A6C4-0E7863B733A5</RequestId>
   <HostId>ess.example.com</HostId>
   <Code>UnsupportedOperation</Code>
   <Message>The specified action is not supported. </Message>
</Error>
```

JSON format `{`

```json
    "RequestId": "8906582E-6722-409A-A6C4-0E7863B733A5",
    "HostId": "ess.example.com",
    "Code": "UnsupportedOperation",
    "Message": "The specified action is not supported."
```

`}`

#### 2.1.6 Request signatures

This topic describes how to use the request signature to verify the identity of the API caller. Auto Scaling authenticates each access request. Therefore, each request must contain signature information, regardless of whether the request is sent over HTTP or HTTPS. Auto Scaling implements symmetric encryption with an AccessKey pair to verify the identity of the request sender. You can obtain the AccessKey ID and the AccessKey secret in the Alibaba Cloud Apsara Stack console. For more information, see Obtain an AccessKey pair. The AccessKey ID is used to verify the identity of the user, while the AccessKey secret is used to encrypt and verify the signature string. You must keep your AccessKey secret confidential. Perform the following steps to sign an access request:
1. Create a canonicalized query string by using request parameters.
i. Arrange all request parameters in alphabetical order. These parameters include all common request parameters and operation-specific parameters except the Signature parameter in the common request parameters. If you use the GET method to make a request, the request parameters are included as a part of the request URL. The first parameter follows the question mark ( ? ) in the URL, and the other parameters follow an ampersand ( `&` ). ii. Encode the name and value of each request parameter. The parameter names and values must be URL-encoded in UTF-8 based on the following encoding rules: Uppercase letters, lowercase letters, digits, and some special characters such as ampersands (&), hyphens (-), underscores (_), periods (.), and tildes (~) do not need to be encoded. Other characters must be percent encoded in the %XY format. `XY` represents the ASCII code of the characters in hexadecimal notation. For example, double quotation marks (") are encoded as %22 . Extended UTF-8 characters are encoded in the %XY%ZA... format. Spaces must be encoded as %20 . Do not encode spaces as plus signs `(+)` .

|   | Not e Most libraries that support URL encoding, such as java.net.URLEncoder, comply with the Multipurpose Internet Mail Extensions (MIME) encoding rules of application/x-ww w-form-urlencoded . If this encoding method is used, replace the plus signs (+) with %20 , the asterisks (*) with %2A , and %7E with tildes (~) in the encoded strings to obtain the required strings. |
|---|---|
|   | w-form-urlencoded |

iii. Connect the encoded parameter names and values with equal signs (=). iv. Arrange the parameter name and value pairs connected by equal signs in alphabetical order, and connect them with ampersands (&) to obtain a canonicalized query string.
2. Create a string-to-sign from the encoded canonicalized query string based on the following rules:

```
 StringToSign=
 HTTPMethod + "&" +
 percentEncode("/") + "&" +
 percentEncode(CanonicalizedQueryString)
```

3. Use the signature string to calculate the HMAC value of the string-to-sign as defined in RFC 2104.
The key used for signature calculation is the combination of your AccessKey secret and an ampersand (&) (ASCII 38). Secure Hash Algorithm 1 (SHA1) is used as the hash algorithm.
4. Encode the HMAC value in Base64 to obtain the signature string.
5. Add the signature string to the request as the Signature parameter to sign the request.
When the signature string is submitted to the ECS server as the final request parameter value, the string must be URL-encoded as other parameters based on rules defined in RFC 3986. DescribeScalingGroups is used in the example. The following section shows the request URL to be signed:

```
http://ess.example.com/?TimeStamp=2014-08-15T11%3A10%3A07Z&Format=xml&AccessKeyId=testid&Ac tion=DescribeScalingGroups&SignatureMethod=HMAC-SHA1&RegionId=cn-qingdao&SignatureNonce=132 4fd0e-e2bb-4bb1-917c-bd6e437f****&SignatureVersion=1.0&Version=2014-08-28
```

The corresponding StringToSign is:

```
GET&%2F&AccessKeyId%3Dtestid&Action%3DDescribeScalingGroups&Format%3Dxml&RegionId%3Dcn-qing dao&SignatureMethod%3DHMAC-SHA1&SignatureNonce%3D1324fd0e-e2bb-4bb1-917c-bd6e437f***&Signat ureVersion%3D1.0&TimeStamp%3D2014-08-15T11%253A10%253A07Z&Version%3D2014-08-28
```

If the AccessKey ID is testid and the AccessKey secret is testsecret, the Key used for HMAC calculation is testsecret&. Then, the calculated signature value is SmhZuLUnXmqxSEZ%2FGqyiwGqmf%2BM=. The following section shows the URL of the signed request:

```
http://ess.example.com/?TimeStamp=2014-08-15T11%3A10%3A07Z&Format=xml&AccessKeyId=testid&Ac tion=DescribeScalingGroups&SignatureMethod=HMAC-SHA1&RegionId=cn-qingdao&SignatureNonce=132 4fd0e-e2bb-4bb1-917c-bd6e437f****&SignatureVersion=1.0&Version=2014-08-28&Signature=SmhZuLU nXmqxSEZ%2FGqyiwGqmf%****
```

The signature string is used as the value of the Signature parameter, and the parameter is added to the request URL.

#### 2.1.7 Scaling groups

##### 2.1.7.1 CreateScalingGroup

You can call this operation to create a scaling group. You can call this operation to create a scaling group based on input parameters. MinSize specifies the minimum number of ECS instances in a scaling group. MaxSize specifies the maximum number of ECS instances in a scaling group. If the number of ECS instances in a scaling group is less than the MinSize value, Auto Scaling automatically adds ECS instances to the scaling group to make sure that the number of instances is equal to the MinSize value. If the number of ECS instances in a scaling group is greater than the MaxSize value, Auto Scaling automatically removes ECS instances from the scaling group to make sure that the number of instances is equal to the MaxSize value. DefaultCooldown specifies the default cooldown period of a scaling group. During the cooldown period after a scale-in or scale-out event is executed, the scaling group cannot execute other scaling activities. This parameter is valid only for scaling activities that are triggered by Cloud Monitor eventtriggered tasks. RemovalPolicy is used to filter and remove ECS instances from a scaling group. This parameter allows you to remove instances based on multiple filter conditions. If an SLB instance is associated with a scaling group, Auto Scaling automatically adds ECS instances that are added to the scaling group to the specified SLB instance. The specified SLB instance must be in the active state. Health check must be enabled on all ports of listeners that are configured for the specified SLB instance. Otherwise, the scaling group fails to be created. If ECS instances of the VPC type have been added to an SLB instance, the SLB instance cannot be associated with a scaling group. The default weight of an ECS instance that is added to an SLB instance is 50. If an ApsaraDB for RDS instance is specified for a scaling group, the scaling group automatically adds the internal IP addresses of its ECS instances to the whitelist of the specified ApsaraDB for RDS instance. The specified ApsaraDB for RDS instance must be in the running state. The number of IP addresses added to the whitelist of the specified ApsaraDB for RDS instance cannot be greater than or equal to the upper limit. A scaling group does not immediately take effect after it is created. You must enable the scaling group to trigger scaling rules and execute scaling activities. The scaling group must be in the same region as the associated SLB instance and ApsaraDB for RDS instance. You can create up to 20 scaling groups. Request parameters Description

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to CreateScalingGroup. |

| uto Scaling |   |   | Developer Guide·API referenc |
|---|---|---|---|
| Parameter | Type | Required | Description |
| RegionId | String | Yes | The ID of the region in which to create the scaling group. |
| MaxSize | Integer | Yes | The maximum number of ECS instances in the scaling group. Valid values: 0 to 100. |
| MinSize | Integer | Yes | The minimum number of ECS instances in the scaling group. Valid values: 0 to 100. |
| ScalingGroupName | String | No | The name of the scaling group. The name must be 2 to 40 characters in length and can contain digits, letters, underscores ( ), _ hyphens (-), and periods (.). It must start with a letter or digit. This name must be unique to an Apsara Stack account in a region. If you do not specify this parameter, the default value is ScalingGroupId. |
| DefaultCooldown | Integer | No | The default cooldown time of the scaling group. Valid values: 0 to 86400. Unit: seconds. Default value: 300. |
| RemovalPolicy.N | String | No | The policy for removing ECS instances from a scaling group. Valid values: OldestInstance: removes the ECS instance that was added to the scaling group at the earliest point in time. NewestInstance: removes the ECS instance that was most recently added to the scaling group. OldestScalingConfiguration: removes the ECS instance that was created based on the earliest scaling configuration. Default values: OldestScalingConfiguration and OldestInstance. You can specify up to two values. |
| LoadBalancerIds | String | No | The IDs of SLB instances to be associated with the scaling group. The instance IDs are formatted as a JSON array such as [ “lb- id0”, “lb-id1”, … “lb-idz” ]. You can specify a maximum of five SLB instances. |
| DBInstanceIds | String | No | The IDs of ApsaraDB for RDS instances to be associated with the scaling group. The instance IDs are formatted as a JSON array such as [ “rm-id0”, “rm-id1”, … “rm- idz” ]. You can specify a maximum of eight ApsaraDB for RDS instances. |

| Parameter | Type | Required | Description |
|---|---|---|---|
| VSwitchId | String | No | The ID of the VSwitch. It must be specified when you create a scaling group of the VPC type. |
| VSwitchIds.N | String | No | The IDs of VSwitch N. If VSwitchIds.N is set, VSwitchId is ignored. This parameter enables you to specify a maximum of five VSwitches of one VPC in multiple zones when you create a scaling group. Valid values of N: 1 to 5. The VSwitch priority is indicated by an ascending set of numbers. 1 indicates the highest priority. If an ECS instance cannot be created in the zone where the VSwitch with the highest priority resides, the system automatically uses the VSwitch with the next highest priority to create the ECS instance. |

Response parameters Description

| Parameter | Type | Description |
|---|---|---|
| ScalingGroupId | String | The ID of the scaling group, which was generated by the system and globally unique. |

Error codes For more information about errors common to all operations, see Client errors or Server errors. Error code description

| Description | Error code | Error message | HTTP status code |
|---|---|---|---|
| The error message returned because the specified scaling group name already exists. | InvalidScalingGroupNam e.Duplicate | The specified value of parameter <parameter name> is duplicated. | 400 |
| The error message returned because the maximum number of scaling groups has been reached. | QuotaExceeded.Scaling Group | Scaling group quota exceeded. | 400 |

|   |   | 400 |
|---|---|---|
| <parameter name> |   |   |

| Description | Error code | Error message | HTTP status code |
|---|---|---|---|
| The error message returned because the specified region does not exist. | InvalidRegionId.NotFoun d | The specified region does not exist. | 404 |
| The error message returned because the specified MinSize value is greater than the MaxSize value. | InvalidParameter.Conflic t | The value of parameter <parameter name> and parameter <parameter name> are conflict. | 400 |
| The error message returned because the specified SLB instance does not exist in this account. | InvalidLoadBalancerId.N otFound | The specified Load Balancer does not exist. | 404 |
| The error message returned because the specified SLB instance and scaling group are not in the same region. | InvalidLoadBalancerId.R egionMismatch | The specified Load Balancer and the specified scaling group are not in the same Region. | 400 |
| The error message returned because the specified SLB instance is not in the active state. | IncorrectLoadBalancerSt atus | The current status of the specified load balancer does not support this action. | 400 |
| The error message returned because health check is not enabled for the specified SLB instance. | IncorrectLoadBalancerH ealthCheck | The current health check type of specified load balancer does not support this action. | 400 |
| The error message returned because the network type of the specified SLB instance is VPC after you specify the VSwitch ID. | InvalidLoadBalancerId.In correctAddressType | The current address type of specified load balancer does not support this action. | 400 |
| The error message returned because the network type of the ECS instance that is added to the specified SLB instance is different from that of the scaling group. | InvalidLoadBalancerId.In correctInstanceNetwork Type | The network type of the instance in specified Load Balancer does not support this action. | 400 |

|   |   | <parameter name> |
|---|---|---|

| Description | Error code | Error message | HTTP status code |
|---|---|---|---|
| The error message returned because the ECS instance that is added to the associated SLB instance and the VSwitch are not in the same VPC. | InvalidLoadBalancerId.V PCMismatch | The specified virtual switch and the instance in specified Load Balancer are not in the same VPC. | 400 |
| The error message returned because the specified ApsaraDB for RDS instance does not exist in this account. | InvalidDBInstanceId.NotF ound | DB instance “XXX” does not exist. | 404 |
| The error message returned because the specified ApsaraDB for RDS instance and scaling group are not in the same region. | InvalidDBInstanceId. RegionMismatch | DB instance “XXX” and the specified scaling group are not in the same Region. | 400 |
| The error message returned because the specified ApsaraDB for RDS instance is not in the running state. | IncorrectDBInstanceStat us | The current status of DB instance “XXX” does not support this action. | 400 |
| The error message returned because the maximum number of IP addresses added to the whitelist of the specified ApsaraDB for RDS instance has been reached. | QuotaExceeded.DBInsta nceSecurityIP | Security IP quota exceeded in DB instance “XXX”. | 400 |
| The error message returned because the specified VSwitch does not exist. | InvalidVSwitchId.NotFou nd | The specified virtual switch does not exist. | 404 |
| The error message returned because the maximum number of private IP addresses of the VSwitch has been reached. | QuotaExceeded.PrivateI pAddress | Private IP address quota exceeded in the specified virtual switch. | 400 |
| The error message returned because the maximum number of instances in the VPC has been reached. | QuotaExceeded.VPCInst ance | Instance quota exceeded in the specified VPC. | 400 |

| uto Scaling |   | De | veloper Guide·API referenc |
|---|---|---|---|

| Description | Error code | Error message | HTTP status code |
|---|---|---|---|
| The error message returned because the VSwitch is unavailable, and instances cannot be created. | IncorrectVSwitchStatus | The current status of virtual switch does not support this operation. | 400 |

Examples Sample request s

```
http://ess.example.com/?Action=CreateScalingGroup &RegionId=cn-qingdao &MaxSize=20 &MinSize=2 &LoadBalancerId=147b46d767c-cn-qingdao-c**** &DBInstanceId.1=rdszzzyyuny**** &DBInstanceId.2=rdsia3u3yia**** &<Common request parameters>
```

Sample responses XM format

```xml
<CreateScalingGroupResponse>
    <RequestId>536E9CAD-DB30-4647-AC87-AA5CC38C5382</RequestId>
    <ScalingGroupId>dP8VqSd9ENXPc0ciVmbc****</ScalingGroupId>
</CreateScalingGroupResponse>
```

JSON format `{`

```json
    "RequestId": "536E9CAD-DB30-4647-AC87-AA5CC38C5382",
    "ScalingGroupId": "dP8VqSd9ENXPc0ciVmbc****"
```

`}`

##### 2.1.7.2 ModifyScalingGroup

You can modify a scaling group. Description You can call this operation to modify the attributes of a scaling group. However, the following attributes cannot be modified: RegionId LoadBalancerId DBInstanceId This operation can only be called when the scaling group is in active or inactive state. When the specified scaling configuration needs to be modified, the InstanceType of the modified scaling configuration must be the same as the active InstanceType of the scaling configuration. After a new scaling configuration is added to the scaling group, the running ECS instances that were created based on the previous scaling configuration will remain unchanged. If the number of ECS instances does not meet the requirements of the modified MaxSize and MinSize parameters, ECS instances will be added to or removed from the group, so that the number of instances is equal to the MaxSize or MinSize parameter. Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to ModifyScalingGroup. |
| ScalingGroupId | String | Yes | The ID of a scaling group. |
| ScalingGroupName | String | No | The displayed name of the scaling group. The name must be 2 to 40 characters in length. It must start with a letter or number. It can contain numbers, uppercase letters, lowercase letters, underscores ( ), hyphens (-), and periods (.). _ The name of the scheduled task must be unique to an Alibaba Cloud account in the region it is located. |
| ActiveScalingConfigurati onId | String | No | The ID of the active scaling configuration in the scaling group. |
| MinSize | Integer | No | The minimum number of ECS instances in the scaling group. Valid values: [0, 100]. |
| MaxSize | Integer | No | The maximum number of ECS instances in the scaling group. Valid values: [0, 100]. |
| DefaultCooldown | Integer | No | The default cool-down time of the scaling group. Valid values: [0, 86400]. Unit: second. |

| Parameter | Type | Required | Description |
|---|---|---|---|
| RemovalPolicy.N | String | No | The ECS instance removal policy for the scaling group. Valid values: OldestInstance: Remove the ECS instance that was added to the scaling group first. NewestInstance: Remove the ECS instance that was added to the scaling group last. OldestScalingConfiguration: Remove ECS instances that were created based on the earliest scaling configuration. A maximum of two values can be entered. |

Response parameters For more information, see Common response parameters. Error code For more information about common error codes, see Client errors or Server errors.

| Description | Error code | Description | HTTP status code |
|---|---|---|---|
| The error message returned when the specified scaling group does not exist under this account. | InvalidScalingGroupId.NotFoun d | The specified scaling group does not exist. | 404 |
| The error message returned when the scaling group name already exists. | InvalidScalingGroupName.Dupli cate | The specified value of parameter <parameter name> is duplicated. | 400 |

| Description | Error code | Description | HTTP status code |
|---|---|---|---|
| The error message returned when the specified scaling configuration does not exist in the specified scaling group. | InvalidScalingConfigurationId.N otFound | The specified scaling configuration does not exist. | 404 |
| The error message returned when the instances types of the specified scaling configuration and the active scaling configuration are different. | InvalidScalingConfigurationId.In stanceTypeMismatch | The specified scaling configuration and existing active scaling configuration have different instance type. | 400 |
| The error message returned when the specified MinSize is greater than MaxSize. | InvalidParameter.Conflict | The values of parameter <Parameter name> and parameter <Parameter name> are conflict. | 400 |

Examples Sample request s

```
http://ess.example.com/?Action=ModifyScalingGroup &ScalingGroupId=cqS5QbbhmvGLcJbWoDbW**** &ScalingGroupName=ScalingGroup &<Common request parameter>
```

Response examples XML format

```xml
<ModifyScalingGroupResponse>
    <RequestId>6469DCD0-13AC-487E-85A0-CE4922908FDE</RequestId>
</ModifyScalingGroupResponse>
```

JSON format `{`

```json
    "RequestId": "6469DCD0-13AC-487E-85A0-CE4922908FDE"
```

`}`

##### 2.1.7.3 EnableScalingGroup

You can call this operation to enable a scaling group. Description After a scaling group is enabled, the ECS instances specified by InstanceId.N are added to the scaling group. If the number of ECS instances in the scaling group is less than the MinSize value after the ECS instances are added, additional ECS instances are automatically created to achieve the MinSize value. For example, a scaling group is created with the MinSize parameter set to 5. Two existing ECS instances are specified in the InstanceId.N parameter when the scaling group is enabled. Then, three additional ECS instances are automatically created after the two ECS instances are added by Auto Scaling to the scaling group. You can call this operation only when the scaling group is inactive. If the scaling group has no active scaling configuration, you must specify a scaling configuration when you enable the scaling group. A single scaling group can only have one active scaling configuration at a time. If an active scaling configuration exists before the scaling group is enabled, this configuration will become inactive after you specify a new active scaling configuration when you call the operation. The limits on ECS instances to be added are as follows: The ECS instances and the scaling group must be in the same region. The ECS instances must have the same instance type as that of the active scaling configuration. The ECS instances must be running. The ECS instances have not been added to any scaling group. If the VSwitchId parameter is specified for a scaling group, the ECS instances that reside in a classic network or in other VPCs cannot be added to the scaling group. If the VSwitchId parameter is not specified for a scaling group, ECS instances that belong to a VPC cannot be added to the scaling group. If the sum of the number of instances to be added specified by this operation and the number of existing ECS instances in the scaling group is greater than the MaxSize value, the call fails. Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to EnableScalingGroup. |
| ScalingGroupId | String | Yes | The ID of the scaling group. |

| Parameter | Type | Required | Description |
|---|---|---|---|
| ActiveScalingConfigurati onId | String | No | The ID of the scaling configuration to be activated in the scaling group. |
| InstanceId.N | String | No | The IDs of ECS instances to be added to the enabled scaling group. Valid values of N: 1 to 20. |

Response parameters For more information, see Common response parameters. Error codes For more information about errors common to all operations, see Client errors or Server errors.

| Description | Error code | Error message | HTTP status code |
|---|---|---|---|
| The error message returned because the specified scaling group does not exist under this account. | InvalidScalingGroupId.NotFound | The specified scaling group does not exist. | 404 |
| The error message returned because Auto Scaling is not authorized to call the specified operation. | Forbidden.Unauthorized | A required authorization for the specified action is not supplied. | 403 |
| The error message returned because the specified scaling group is currently being deleted. | IncorrectScalingGroupStatus | The current status of the specified scaling group does not support this action. | 400 |
| The error message returned because the specified scaling configuration does not exist in the specified scaling group. | InvalidScalingConfigurationId.NotFound | The specified scaling configuration does not exist. | 404 |

| Description | Error code | Error message | HTTP status code |
|---|---|---|---|
| The error message returned because the instance type of the specified scaling configuration is different from that of the active scaling configuration. | InvalidScalingConfigurationId.InstanceT ypeMismatch | The specified scaling configuration and existing active scaling configuration have different instance type. | 400 |
| The error message returned because no active scaling configuration is specified for the scaling group. | MissingActiveScalingConfiguration | An active scaling configuration for the specified scaling group is not supplied. | 400 |
| The error message returned because the specified ECS instance does not exist in the current account. | InvalidInstanceId.NotFound | Instance "XXX" does not exist. | 404 |
| The error message returned because the specified ECS instance and the scaling group are not in the same region. | InvalidInstanceId. RegionMismatch | Instance "XXX" and the specified scaling group are not in the same Region. | 400 |
| The error message returned because the type of the specified ECS instance is different from that in the active scaling configuration. | InvalidInstanceId. InstanceTypeMismatch | Instance "XXX" and existing active scaling configuration have different instance type. | 400 |
| The error message returned because the specified ECS instance is not running. | IncorrectInstanceStatus | The current status of instance "XXX" does not support this action. | 400 |

| Description | Error code | Error message | HTTP status code |
|---|---|---|---|
| The error message returned because the network type of the specified ECS instance is different from that of the scaling group. | InvalidInstanceId. NetworkTypeMismatch | The network type of instance "XXX" does not support this action. | 400 |
| The error message returned because the added ECS instance and the specified scaling group are not in the same VPC. | InvalidInstanceId.VPCMismatch | Instance "XXX" and the specified scaling group are not in the same VPC. | 400 |
| The error message returned because the specified ECS instance is already added to another scaling group. | InvalidInstanceId.InUse | Instance "XXX" is already attached to another scaling group. | 400 |
| The error message returned because the specified SLB instance is not active. | IncorrectLoadBalancerStatus | The current status of the specified load balancer does not support this action. | 400 |
| The error message returned because health check is not enabled for the specified SLB instance. | IncorrectLoadBalancerHealthCheck | The current health check type of specified load balancer does not support this action. | 400 |
| The error message returned because the network type of the ECS instance attached to the specified SLB instance is different from that of the scaling group. | InvalidLoadBalancerId.IncorrectInstance NetworkType | The network type of the instance in specified Load Balancer does not support this action. | 400 |

| Description | Error code | Error message | HTTP status code |
|---|---|---|---|
| The error message returned because the ECS instance attached to the specified SLB instance is not in the same VPC as the VSwitch specified by VSwitchID. | InvalidLoadBalancerId.VPCMismatch | The specified virtual switch and the instance in specified Load Balancer are not in the same VPC. | 400 |
| The error message returned because the specified RDS instance is not running. | IncorrectDBInstanceStatus | The current status of DB instance "XXX" does not support this action. | 400 |
| The error message returned because the total number of ECS instances (Total Capacity) exceeds the specified value of MaxSize after ECS instances are added to the specified scaling group. | IncorrectCapacity.MaxSize | To attach the instances, the total capacity will be greater than the max size. | 400 |

Examples Sample requests

```
http://ess.example.com/?Action=EnableScalingGroup &ScalingGroupId=dmIDKNcyWfzncX9MWX1**** &InstanceId.1=i-283vv**** &<Common request parameters>
```

Sample responses XML format

```xml
<EnableScalingGroupResponse>
    <RequestId>6469DCD0-13AC-487E-85A0-CE4922908FDE</RequestId>
</EnableScalingGroupResponse>
```

JSON format `{`

```json
    "RequestId": "6469DCD0-13AC-487E-85A0-CE4922908FDE"
```

`}`

##### 2.1.7.4 DisableScalingGroup

You can disable a specified scaling group. Description The scaling activity that is being executed before this operation is called will be continued until it is completed. Scaling activity requests after this operation is called will be rejected. The operation can only be called when the scaling group is active. Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DisableScalingGroup. |
| ScalingGroupId | String | Yes | The ID of the scaling group. |

Response parameters For more information about response parameters, see Common response parameters. Error code For more information about common error codes, see Client errors or Server errors.

| Error message | Error code | Description | HTTP status code |
|---|---|---|---|
| The error message returned when the specified scaling group does not exist under this account. | InvalidScalingGroupId.N otFound | The specified scaling group does not exist. | 404 |

Examples Sample request s

```
http://ess.example.com/?Action=DisableScalingGroup &ScalingGroupId=dmIDKNcyWfzncX9MWX1**** &<Common request parameter>
```

Response examples XML format

```xml
< DisableScalingGroupResponse>
    <RequestId>6469DCD0-13AC-487E-85A0-CE4922908FDE</RequestId>
</ DisableScalingGroupResponse>
```

JSON format `{`

```json
    "RequestId": "6469DCD0-13AC-487E-85A0-CE4922908FDE"
```

`}`

##### 2.1.7.5 DeleteScalingGroup

You can delete a specified scaling group. Description ForceDelete indicates whether to forcibly delete a scaling group and remove and release its ECS instances when the scaling group contains ECS instances or is undergoing a scaling activity. When ForceDelete is set to false, the scaling group can only be deleted when the following conditions are met: Condition 1: The scaling group is not currently undergoing a scaling activity. Condition 2: The number of ECS instances currently in the scaling group (Total Capacity) is 0. If these two conditions are met, the scaling group can be disabled and deleted. If ForceDelete is set to true, we recommend that you perform the following procedure: Disable the scaling group to reject new scaling activity requests. Remove all ECS instances from the scaling group after the ongoing scaling activities are completed and then delete the scaling group. Manually added ECS instances are only removed from the scaling group, whereas automatically created instances are deleted. Note that deleting a scaling group also deletes its scaling configurations, rules, activities, and requests. The following tasks and instances are not deleted: scheduled tasks, CloudMonitor alarm tasks, Server Load Balancer instances, and ApsaraDB RDS instances. Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DeleteScalingGroup. |
| ScalingGroupId | String | Yes | The ID of the scaling group. |

| Parameter | Type | Required | Description |
|---|---|---|---|
| ForceDelete | Bool | No | Indicates whether to forcibly delete a scaling group and remove and release its ECS instances when the scaling group contains ECS instances or is undergoing scaling activity. The default value is false, indicating that the scaling group will not be forcibly deleted. |

Response parameters For more information about response parameters, see Common response parameters. Error code

| Error message | Error code | Description | HTTP status code |
|---|---|---|---|
| The error message returned when the specified scaling group does not exist under this account. | InvalidScalingGroupId.NotF ound | The specified scaling group does not exist. | 404 |
| The error message returned when Auto Scaling does not have full authorization with Open API. | Forbidden.Unauthorized | A required authorization for the specified action is not supplied. | 403 |
| The error message returned when the specified scaling group still contains ECS instances. | InstanceInUse | You cannot delete a scaling configuration or scaling group while there is an instance associated with it. | 400 |

Examples Sample request s

```
http://ess.example.com/?Action=DeleteScalingGroup &ScalingGroupId=dmIDKNcyWfzncX9MWX1**** &<Common request parameters>
```

Response examples XML format

```xml
<DeleteScalingGroupResponse>
    <RequestId>6469DCD0-13AC-487E-85A0-CE4922908FDE</RequestId>
</DeleteScalingGroupResponse>
```

JSON format `{`

```json
   "RequestId": "6469DCD0-13AC-487E-85A0-CE4922908FDE"
```

`}`

##### 2.1.7.6 DescribeScalingGroups

You can call this operation to query scaling groups. Description A scaling group can have the following lifecycle states: Active: The active scaling group can receive requests to execute scaling rules and trigger scaling activities. Inactive: The inactive scaling group cannot receive any requests to execute scaling rules. Deleting: The scaling group is being deleted and cannot receive any requests to execute scaling rules. Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeScalingGroups. |
| RegionId | String | Yes | The ID of the region where the scaling group resides. |
| ScalingGroupId.N | String | No | The ID of the scaling group. Valid values of N: 1 to 20. The IDs of inactive scaling groups will not be displayed in the query result and no errors will be returned. |
| ScalingGroupName.N | String | No | The name of the scaling group. Valid values of N: 1 to 20. The names of inactive scaling groups will not be displayed in the query result and no errors will be returned. |

| Parameter | Type | Required | Description |
|---|---|---|---|
| PageNumber | Integer | No | The number of the page to return. Pages start from page 1. Default value: 1. |
| PageSize | Integer | No | The number of entries to return on each page. Valid values: 1 to 50. Default value: 10. |

Response parameters

| Parameter | Type | Description |
|---|---|---|
| TotalCount | Integer | The total number of scaling groups. |
| PageNumber | Integer | The page number of the returned page. |
| PageSize | Integer | The number of entries returned per page. |
| ScalingGroups | ScalingGroupSetType | A collection of details about the scaling groups you are querying. |

ScalingGroupSetType is a collection of ScalingGroupItemType.

| Parameter | Type | Description |
|---|---|---|
| ScalingGroup | ScalingGroupItemType | The details of the scaling group. |

The following table describes the attributes of ScalingGroupItemType.

| Parameter | Type | Description |
|---|---|---|
| ScalingGroupId | String | The ID of the scaling group. |
| ScalingGroupName | String | The display name of the scaling group. |
| ActiveScalingConfigurationId | String | The ID of the active scaling configuration in the scaling group. |
| RegionId | String | The ID of the region where the scaling group resides. |
| MinSize | Integer | The minimum number of ECS instances in the scaling group. |

| uto Scaling |   | Developer Guide·API referenc |
|---|---|---|

| Parameter | Type | Description |
|---|---|---|
| MaxSize | Integer | The maximum number of ECS instances in the scaling group. |
| DefaultCooldown | Integer | The default cooldown time of the scaling group. |
| RemovalPolicies | RemovalPolicySetType | The collection of policies for removing ECS instances from the scaling group. |
| LoadBalancerIds | List of LoadBalancerId | The IDs of the SLB instances. |
| DBInstanceIds | DBInstanceIdSetType | The IDs of the RDS instances. |
| VSwitchId | String | The ID of the VSwitch corresponding to the scaling group. |
| LifecycleState | String | The lifecycle status of the scaling group. Active: The active scaling group can receive requests to execute scaling rules and trigger scaling activities. Inactive: The inactive scaling group cannot receive any requests to execute scaling rules. Deleting: The scaling group is currently being deleted and cannot receive any requests to execute scaling rules. |
| TotalCapacity | Integer | The total number of ECS instances in the scaling group. |
| ActiveCapacity | Integer | The number of Elastic Compute Service (ECS) instances that have been added to the scaling group and are running properly. |
| PendingCapacity | Integer | The number of ECS instances that are being added to the scaling group, but are still being configured. |
| RemovingCapacity | Integer | The number of ECS instances that are being removed from the scaling group. |
| CreationTime | String | The time when the scaling group was created. |

RemovalPolicySetType is a collection of strings.

| Parameter | Type | Description |
|---|---|---|
| RemovalPolicy | String | The policy for removing ECS instances from the scaling group. |

DBInstanceIdSetType is a collection of strings.

| Parameter | Type | Description |
|---|---|---|
| DBInstanceId | String | The ID of the RDS instance. |

Error codes For more information about errors common to all operations, see Client errors or Server errors. Examples Sample requests

```
http://ess.example.com/?Action=DescribeScalingGroups &RegionId=cn-qingdao &PageSize=50 &<Common request parameters>
```

Sample responses XML format

```xml
<DescribeScalingGroupsResponse>
    <RequestId>6393C3A8-B611-42F2-AFA6-F080FC45D5D0</RequestId>
    <TotalCount>1</TotalCount>
    <PageNumber>1</PageNumber>
    <PageSize>10</PageSize>
    <ScalingGroups>
    <ScalingGroup>
            <ActiveCapacity>1</ActiveCapacity>
            <ActiveScalingConfigurationId>dyo713cNYIB4ddEVlKbc****</ActiveScalingConfigurat
ionId>
            <DBInstanceIds>
                <DBInstanceId>rdszzzyyuny****</DBInstanceId>
            </DBInstanceIds>
            <VSwitchId>vpc-25j4g****</VSwitchId>
            <DefaultCooldown>20</DefaultCooldown>
            <LifecycleState>Active</LifecycleState>
            <LoadBalancerId>147b46d767c-cn-qingdao-c****</LoadBalancerId>
            <MaxSize>1</MaxSize>
            <MinSize>0</MinSize>
            <PendingCapacity>0</PendingCapacity>
            <RegionId>cn-qingdao</RegionId>
            <RemovingCapacity>0</RemovingCapacity>
            <ScalingGroupId>dyrSuvBOtO1dEdIlIbp****</ScalingGroupId>
            <ScalingGroupName>dyrSuvBOtO1dEdIlIbp****</ScalingGroupName>
            <RemovalPolicies>
                <RemovalPolicy>OldestScalingConfiguration</RemovalPolicy>
                <RemovalPolicy>OldestInstance</RemovalPolicy>
            </RemovalPolicies>
            <TotalCapacity>1</TotalCapacity>
            <CreationTime>2014-08-14T10:58Z</CreationTime>
        </ScalingGroup>
    </ScalingGroups>
</DescribeScalingGroupsResponse>
```

JSON format `{`

```json
  "RequestId": "68386699-8B9E-4D5B-BC4C-75A28F6C2A00",
  "TotalCount": 1,
  "PageSize": 10,
  "PageNumber": 1,
  "ScalingGroups": {
    "ScalingGroup": [
```

`{`

```json
        "ScalingGroupId": "b8pYCVbIV5k9cz4PWpbe****",
        "ScalingGroupName": "b8pYCVbIV5k9cz4PWpbe****",
        "RegionId": "cn-qingdao",
        "RemovingCapacity": 0,
        "DefaultCooldown": 300,
        "MinSize": 1,
        "MaxSize": 2,
        "LifecycleState": "Inactive",
        "ActiveScalingConfigurationId": " dyo713cNYIB4ddEVlKbc****",
        "LoadBalancerId": "147b46d767c-cn-qingdao-c****",
        "PendingCapacity": 0,
        "TotalCapacity": 0,
        "ActiveCapacity": 0,
        "CreationTime": "2014-08-14T10:58Z",
        "DBInstanceIds": {
          "DBInstanceId": [
            "rdsia3u3yia****",
            "rdszzzyyuny****"
```

`]` `},`

```json
        "VSwitchId":"vpc-25j4g****",
        "RemovalPolicies": {
          "RemovalPolicy": [
            "OldestScalingConfiguration",
            "OldestInstance"
```

`]` `}` `}` `]` `}` `}`

##### 2.1.7.7 DescribeScalingInstances

You can query ECS instances in a scaling group. You can query ECS instances by specifying the scaling group ID, scaling configuration ID, health status, lifecycle status, and creation type. Description ECS instances in a scaling group can be either automatically created or manually added. Automatically created ECS instances refer to those created by Auto Scaling during scaling based on user-defined scaling configurations and rules. Manually added ECS instances refer to those added to a scaling group manually by you. An ECS instance in a scaling group will go through the following status during its lifecycle: Pending: The ECS instance is currently being added to the scaling group. For example, the instance might currently be being created, added to a Server Load Balancer instance, or added to ApsaraDB RDS. InService: The ECS instance has been successfully added to the scaling group and is providing service normally. Removing: The ECS instance is being removed from the scaling group. An ECS instance in a scaling group can be in either of the following health status: Healthy: If an ECS instance is running, it is considered as healthy. Unhealthy: If an ECS instance is not in the Running status, it will be considered as unhealthy. Auto Scaling automatically removes unhealthy ECS instances from the scaling group. Auto Scaling will stop and release automatically created ECS instances that are unhealthy. Auto Scaling will not stop or release manually added ECS instances that are unhealthy. Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value DescribeScalingInstances. |
| RegionId | String | Yes | The ID of the region where the scaling group is located. |
| ScalingGroupId | String | No | The ID of the scaling group. |
| ScalingConfigurationId | String | No | The ID of an associated scaling configuration. |
| InstanceId.N | String | No | The ID of ECS instance N. N ranges from 1 to 20. The IDs of inactive instances are ignored in the query results, and no error is reported. |
| HealthStatus | String | No | The health status of an ECS instance in the scaling group. Valid values: Healthy: The ECS instances are in running status. Unhealthy: The ECS instances are not in running status. |

| Parameter | Type | Required | Description |
|---|---|---|---|
| LifecycleState | String | No | The lifecycle status of an ECS instance in the scaling group. Valid values: InService: the ECS instance has been added to the scaling group and runs properly. Pending: the ECS instance is being added to the scaling group with relevant configurations not completed. Removing: The ECS instance is being removed from the scaling group. |
| CreationType | String | No | The ECS instance type. Valid values: AutoCreated: the ECS instance is automatically created by the Auto Scaling service in the scaling group. Added: the ECS instance is created outside the Auto Scaling service and manually added to the scaling group. |
| PageNumber | Integer | No | The page number of the ECS instance list. The initial value and default value are both 1. |
| PageSize | Integer | No | When querying by page, this parameter indicates the number of lines per page. Maximum value: 50. Default value: 10. |

Response parameters

| Parameter | Type | Description |
|---|---|---|
| TotalCount | Integer | The total number of the ECS instances. |
| PageNumber | Integer | The number of current page. |
| PageSize | Integer | The number of lines per page. |
| ScalingInstances | ScalingInstanceSetType | A collection of details about the ECS instances that you are querying. |

ScalingInstanceSetType is a collection of ScalingInstanceItemTypes.

| Parameter | Type | Description |
|---|---|---|
| ScalingInstance | ScalingInstanceItemType | The details of an ECS instance. |

The following table describes the attributes of ScalingInstanceItemType.

| Parameter | Type | Description |
|---|---|---|
| InstanceId | String | The ID of an ECS instance. |
| ScalingGroupId | String | The ID of the scaling group to which an ECS instance belongs. |
| ScalingConfigurationId | String | The ID of an associated scaling configuration. |
| HealthStatus | String | The health status of an ECS instance in the scaling group. |
| LifecycleState | String | The lifecycle status of an ECS instance in the scaling group. |
| CreationTime | String | The time at which an ECS instance was added to the scaling group. |
| CreationType | String | The ECS instance type. |

Error code For more information about common error codes, see Client errors or Server errors. Examples Sample request s

```
http://ess.example.com/?Action=DescribeScalingInstances &RegionId=cn-qingdao & ScalingGroupId = dBCYxE26IHKcGq1xPcT **** &<Common request parameter>
```

Response examples XML format

```xml
<DescribeScalingInstancesResponse>
    <RequestId>DFF8797F-5B73-4BD7-A7D0-03479C458F7A</RequestId>
    <TotalCount>1</TotalCount>
    <PageNumber>1</PageNumber>
    <PageSize>10</PageSize>
    <ScalingInstances>
        <ScalingInstance>
            <CreationTime>2014-08-15T17:37Z</CreationTime>
            <CreationType>AutoCreated</CreationType>
            <HealthStatus>Healthy</HealthStatus>
            <InstanceId>i-283vvyytn</InstanceId>
            <LifecycleState>Active</LifecycleState>
            <ScalingConfigurationId>eOs27Kb0oXvQcUYjEGel****</ScalingConfigurationId>
            <ScalingGroupId>dBCYxE26IHKcGq1xPcTNBwV</ScalingGroupId>
        </ScalingInstance>
    </ScalingInstances>
</DescribeScalingInstancesResponse>
```

JSON format `{`

```json
  "RequestId": "13305F2D-A4C2-4E6B-B7C7-0F2150842EA3",
  "TotalCount": 1,
  "PageNumber": 1,
  "PageSize": 50,
  "ScalingInstances": {
    "ScalingInstance": [
```

`{`

```json
        "ScalingConfigurationId": "bU5uZHcAgtzwcL4IeDea****",
        "CreationType": "AutoCreated",
        "InstanceId": "i-28sov****",
        "CreationTime": "2014-08-14T10:59Z",
        "HealthStatus": "Healthy",
        "LifecycleState": "InService",
        "ScalingGroupId": "dE9YbOdCHqaFdFZHXVdD****"
```

`}` `]` `}` `}`

##### 2.1.7.8 DescribeScalingActivities

You can call this operation to query the scaling activities of a scaling group. Description You can specify a scaling group ID to query all scaling activities of the scaling group. You can filter query results based on the status of scaling activities. Only scaling activities during the last 30 days can be returned. Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation you want to perform. Set the value to DescribeScalingActivities. |
| RegionId | String | Yes | The ID of the region where a scaling activity is located. |
| ScalingGroupId | String | No | The ID of the scaling group. |
| ScalingActivityId.N | String | No | The ID of the scaling activity. Valid values of N: 1 to 10. The IDs of inactive scaling activities will not be displayed in the query result and no errors will be returned. |
| StatusCode | String | No | The status of the scaling activity. Valid values: Successful: The scaling activity was successful. Warning: The scaling activity was partially successful. Failed: The scaling activity failed. InProgress: The scaling activity is in progress. Rejected: The scaling activity request is rejected. |
| PageNumber | Integer | No | The number of the page to return. Pages start from page 1. Default value: 1. |
| PageSize | Integer | No | The number of entries to return on each page. Valid values: 1 to 50. Default value: 10. |

Response parameters

| Parameter | Type | Description |
|---|---|---|
| TotalCount | Integer | The total number of scaling activities. |
| PageNumber | Integer | The page number of the returned page. |
| PageSize | Integer | The number of entries returned per page. |

| Parameter | Type | Description |
|---|---|---|
| ScalingActivities | ScalingActivitySetType | A collection of the scaling activity information. |

ScalingActivitySetType is a collection of ScalingActivityItemType.

| Parameter | Type | Description |
|---|---|---|
| ScalingActivity | ScalingActivityItemType | The details about the scaling activity. |

The following table describes the attributes of ScalingActivityItemType.

| Parameter | Type | Description |
|---|---|---|
| ScalingActivityId | String | The ID of the scaling activity. |
| ScalingGroupId | String | The ID of the scaling group. |
| Description | String | The description of the scaling activity. |
| Cause | String | The trigger for the scaling activity. |
| StartTime | String | The time when the scaling activity started. |
| EndTime | String | The time when the scaling activity ended. |
| Progress | Integer | The execution progress of the scaling activity. |
| StatusCode | String | The status of the scaling activity. |
| StatusMessage | String | Indicates whether the scaling activity is attaching or removing Elastic Compute Service (ECS) instances to or from the scaling group. |

Error codes For more information about errors common to all operations, see Client errors or Server errors. Examples Sample requests

```
http://ess.example.com/?Action=DescribeScalingActivities &RegionId=cn-qingdao &PageSize=50 &<Common request parameters>
```

Sample responses XML format

```xml
<DescribeScalingActivitiesResponse>
    <RequestId>8FAAE99E-EB43-4838-85AD-93F62454904C</RequestId>
    <TotalCount>1</TotalCount>
    <PageNumber>1</PageNumber>
    <PageSize>10</PageSize>
    <ScalingActivities>
        <ScalingActivity>
            <Cause>A scheduled task excuete scaling rule "srtest", changing the Total Capac
ity from "0" to "1". </Cause>
            <Description>Add "1" ECS instance</Description>
            <EndTime>2014-08-17T12:39Z</EndTime>
            <Progress>100</Progress>
            <ScalingActivityId>ebta5WbUzC8gcwUWvfch****</ScalingActivityId>
            <ScalingGroupId>AG6CQdPU8OKdwLjgZcJ****</ScalingGroupId>
            <StartTime>2014-08-17T12:39Z</StartTime>
            <StatusCode>Successful</StatusCode>
            <StatusMessage>"1" ECS instances is added. </StatusMessage>
        </ScalingActivity>
    </ScalingActivities>
</DescribeScalingActivitiesResponse>
```

JSON format `{`

```json
  "RequestId":"0A016AD6-A91F-4210-9DEE-D5BBD4270F45",
  "TotalCount":2582,
  "PageNumber":1,
  "PageSize":1,
  "ScalingActivities":{
  "ScalingActivity":[
```

`{`

```json
        "ScalingActivityId":"bBxOR5dhKFoccGkbTrcy****",
        "StartTime":"2014-08-18T20:49Z",
        "EndTime":"2014-08-18T20:49Z",
        "Cause":" A scheduled task excuete scaling rule \"srtest\", changing the Total Capa
city from \"0\" to \"1\".",
        "Description":" Add \"1\" ECS instance ",
        "Progress":100,
        "ScalingGroupId":"c7acXJbAJmpPcGE7G3bw****",
        "StatusCode":"Successful",
        "StatusMessage":"\"1\" ECS instances is added. "
```

`}` `]` `},` `}`

#### 2.1.8 Scaling configurations

##### 2.1.8.1 CreateScalingConfiguration

You can call this operation to create a scaling configuration. You can create up to 10 scaling configurations in a scaling group. The created scaling configuration cannot be modified. To use a different scaling configuration, you must create a new one and activate it in the scaling group by modifying the ActiveScalingConfigurationId parameter for the group. When creating a scaling configuration, you must select an image to determine the system disk configuration of the instances to be created. The image contains OS and application software configurations. The system disk of an instance created from an image is the clone of the image. A security group must be specified for an instance when it is created, so a scaling configuration must also have a security group specified for instances to be created. Instances in the same security group can access each other. By default, instances in different security groups are isolated by firewalls and cannot access each other. You can configure security group rules to allow instances in different groups to access each other. A security group can contain a maximum of 1,000 instances. If a security group already contains 1,000 instances, the group cannot be specified when you create an instance. When you create an instance, the system allocates a system disk of the appropriate size for the specified instance image. The system disk type can be specified as a cloud disk, or as an ephemeral disk if you have the permission to activate an ephemeral disk. New users do not have this permission. Windows operating systems are not supported on instances with memory of 512 MiB or less. 32-bit operating systems are not supported on instances with a memory greater than or equal to 4 GiB. The capacity of a cloud disk cannot exceed 2,000 GiB, and the capacity of an ephemeral disk cannot exceed 1 TiB (1,024 GiB). The Portable attribute of cloud disk that is created together with an instance is False. This indicates that the cloud disk cannot be added or removed. The DeleteWithInstance attribute of each created disk is True. A maximum of four data disks can be added to an instance. The total capacity of ephemeral disks added to an instance cannot exceed 2 TiB (2,048 GiB). This value does not include the capacity of the system disk. If the system disk is a cloud disk, you cannot add ephemeral disks as data disks. If the system disk is an ephemeral disk, you can add ephemeral or cloud disks as data disks. A security group with a specified VPCId cannot be specified for a scaling configuration unless the VSwitchId parameter has been specified for the scaling group. Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to CreateScalingConfiguration. |
| ScalingGroup Id | String | Yes | The ID of the scaling group to which the scaling configuration belongs. |
| ImageId | String | Yes | The ID of the image file that you specified when you create the instance. |

| uto Scaling |   |   | Developer Guide·API referenc |
|---|---|---|---|

| Parameter | Type | Required | Description |
|---|---|---|---|
| InstanceTyp e | String | Yes | The ECS instance type. |
| SecurityGrou pId | String | Yes | The ID of the security group to which the instance belongs. Instances that belong to the same security group have mutual access. |
| ScalingConfi gurationNam e | String | No | The name of the scaling configuration. It must be 2 to 40 characters in length. It must start with a digit, uppercase letter, or lowercase letter. It can contain letters, digits, underscores ( ), hyphens (-), and periods (.). This parameter _ must be unique in the scaling group. If this parameter is not specified, the default value is the value of ScalingConfigurationId. |
| InternetMaxB andwidthIn | Integer | No | Network ingress bandwidth (Mbit/s). Unit: Mbit/s. Valid values: 1 to 200. If this parameter is not specified, the default network ingress bandwidth is 200 Mbit/s. |
| IoOptimized | String | No | Specifies whether the instance is I/O optimized. Valid values: Optimized: The instance is of I/O optimized type. If this parameter is not specified: Instance types of Generation I are non I/O-optimized by default. Instance types other than Generation I are I/O- optimized by default. For non I/O-optimized instance types, this parameter cannot be specified. |
| SystemDisk.C ategory | String | No | The system disk type. Valid values: cloud: basic disk cloud efficiency: ultra disk _ cloud ssd: standard SSD _ ephemeral ssd: local SSD _ The default value is cloud for I/O-optimized instances of Generation I types. The default value is cloud efficiency for _ other types of instances. |
| SystemDisk.S ize | Integer | No | The size of the system disk. Unit: GiB. Valid values: cloud: 40 to 500 cloud efficiency: 40 to 500 _ cloud ssd: 40 to 500 _ ephemeral ssd: 40 to 500 _ Default value: 40 or the size of the image, depending on whichever is greater. If this parameter is specified, the size of the system disk must be greater than or equal to max{40, ImageSize}. |

| Parameter | Type | Required | Description |
|---|---|---|---|
| DataDisk.N.C ategory | String | No | The category of data disk N. Valid values: cloud: basic disk cloud efficiency: ultra disk _ cloud ssd: standard SSD _ ephemeral ssd: local SSD _ Default value: cloud |
| DataDisk.N.Si ze | Integer | No | The size of data disk N. Unit: GiB. Valid values of N: 1 to 4. Valid values: cloud: 5 to 2000 cloud efficiency: 20 to 32768 _ cloud ssd: 20 to 32768 _ ephemeral ssd: 5 to 800 _ The value of this parameter must be greater than or equal to the size specified by the SnapshotId parameter. |
| DataDisk.N.S napshotId | String | No | The ID of the snapshot used to create data disk N. Valid values of N: 1 to 4. If this parameter is specified, the DataDisk.N.Size parameter is ignored. The size of the specified snapshot is equal to the size of the created data disk. If the snapshot was created on or before July 15, 2013, this operation cannot be performed and the InvalidSnapshot.TooOld error is returned in the response. |
| DataDisk.N.D evice | String | No | The mount point of data disk N. Valid values of N: 1 to 4. When this parameter is not specified, a mount point is assigned automatically when an ECS instance is created. Valid values: /dev/xvdb, /dev/xvdc... /dev/xvdz. The parameter value is empty by default. |
| DataDisk.n.D eleteWithIns tance | String | No | Specifies whether the data disk is released with the instance. Valid values: true: The disk is released with the instance. false: The disk is not released with the instance. Default value: true This parameter is valid only for disks that are created separately and whose DataDisk.N.Category parameter is set to cloud, cloud efficiency, or cloud ssd. If _ _ you set this parameter for other disks, an error is returned. |
| LoadBalance rWeight | Integer | No | The weight of the back-end server. Valid values: 0 to 100. Default value: 50. |
| UserData | String | No | The custom data of the instance. It must be encoded in Base64. The maximum size of the raw data is 16 KiB. |

| Parameter | Type | Required | Description |
|---|---|---|---|
| KeyPairName | String | No | The name of the key pair. When you specify Windows-based ECS instances, ignore this parameter. Default value: null. The password is valid even if you have specified this parameter. Linux instances forbid the use of passwords for log on during initialization. |
| RamRoleNa me | String | No | The RAM role name of the instance. It is provided and maintained by RAM. You can use ListRoles to query the role name. For more information about the RamRoleName parameter, see API CreateRole and ListRoles. |
| Tags | String | No | The tags of the instance. Tags must be specified as key- value pairs, such as {"key1":"value1","key2":"value2", ... "key5":"value5"}. A maximum of five tags can be specified for an instance. The following limits apply to a tag key: It can be a maximum of 64 characters. It cannot start with aliyun. It cannot start with http:// or https://. It cannot be a null string. The following limits apply to a tag value: It can be a maximum of 128 characters. It cannot start with aliyun. It cannot start with http:// or https://. It can be a null string. |
| InstanceTyp es.N | String | No | If you use the InstanceTypes.N parameter, ignore the InstanceType parameter. Valid values of N: 1 to 10, which indicates that up to 10 instance types can be added to a scaling configuration. In the InstanceTypes.N parameter, N indicates the priority of instance types in the current scaling configuration. The instance type with N set to 1 has the highest priority. A higher value of N indicates a lower priority. If an instance type with the highest priority cannot be used to create an instance, the instance type with the next highest priority is automatically used. |
| InstanceNam e | String | No | The name of the ECS instance that is created based on the current scaling configuration. |

Response parameters

| Parameter | Type | Description |
|---|---|---|
| ScalingConfigurationId | String | The ID of the scaling configuration. It is generated by the system and must be globally unique. |

Error codes For more information about errors common to all operations, see Client errors or Server errors.

| Description | Error code | Error message | HTTP status code |
|---|---|---|---|
| The error message returned because the specified scaling group does not exist under this account. | InvalidScalingGroupId.N otFound | The specified scaling group does not exist. | 404 |
| The error message returned because the specified scaling configuration name already exists. | InvalidScalingConfigurati onName.Duplicate | The specified value of parameter <parameter name> is duplicated. | 400 |
| The error message returned because the number of scaling configurations in the specified scaling group reaches the upper limit. | QuotaExceeded.Scaling Configuration | Scaling configuration quota exceeded in the specified scaling group. | 400 |
| The error message returned because the specified image does not exist under this account. | InvalidImageId.NotFoun d | The specified image does not exist. | 404 |
| The error message returned because the specified security group does not exist under this account. | InvalidSecurityGroupId.N otFound | The specified security group does not exist. | 404 |
| The error message returned because the specified instance type does not support the specified image. | InvalidImageId.Instance TypeMismatch | The specified image does not support the specified instance type. | 400 |

| Description | Error code | Error message | HTTP status code |
|---|---|---|---|
| The error message returned because the network type of the specified security group is different from that of the specified scaling group. | InvalidSecurityGroupId.In correctNetworkType | The network type of specified Security Group does not support this action. | 400 |
| The error message returned because the specified security group and the specified VSwitch are not in the same VPC. | InvalidSecurityGroupId.V PCMismatch | The specified security group and the specified virtual switch are not in the same VPC. | 400 |
| The error message returned because the number of ECS instances in the specified security group reaches the upper limit. | QuotaExceeded.Security GroupInstance | Instance quota exceeded in the specified security group. | 400 |
| The error message returned because the instance type of the specified scaling configuration is different from that of the current scaling configuration. | InstanceType.Mismatch | The specified scaling configuration and existing active scaling configuration have different instance type. | 400 |
| The error message returned because the total capacity of mounted ephemeral disks exceeds 2 TiB (2,048 GiB). | QuotaExceeded.Epheme ralDiskSize | Ephemeral disk size quota exceeded. | 403 |
| The error message returned because the type of the specified system disk conflicts with the data disk type. | InvalidParameter.Conflic t | The value of parameter <Parameter name> and parameter <Parameter name> are conflict. | 400 |
| The error message returned because you do not have the permission to create an ephemeral disk. | InvalidSystemDiskCateg ory.ValueUnauthorized | The system disk category is not authorized. | 403 |

| Description | Error code | Error message | HTTP status code |
|---|---|---|---|
| The error message returned because the specified snapshot does not exist. | InvalidDataDiskSnapshot Id.NotFound | Snapshot "XXX" does not exist. | 404 |
| The error message returned because the size of the specified snapshot exceeds the upper limit of the disk size. | InvalidDataDiskSnapshot Id.SizeNotSupported | The capacity of snapshot "XXX" exceeds the size limit of the specified disk category. | 400 |
| The error message returned because the specified snapshot was created on or before July 15, 2013. | InvalidSnapshot.TooOld | This operation is denied because the specified snapshot is created before 2013-07-15. | 403 |
| The error message returned because the mount point of the data disk is already occupied. | InvalidDevice.InUse | Device "XXX" has been occupied. | 403 |
| The error message returned because the name of the specified key pair does not exist. | InvalidKeyPairName.Not Found | The specified KeyPairName does not exist in our records. | 400 |
| The error message returned because you specify the KeyPairName in Windows OS. | InvalidParameter | The specified value of parameter KeyPairName is not valid. | 400 |
| The error message returned because you specify the RAM role name for a classic network-type instance. | InvalidNetworkType.For RAMRole | RAMRole can't be used For classic instance. | 400 |
| The error message returned when the specified RAM role name does not exist. | InvalidRamRole.NotFoun d | The specified RamRoleName does not exist. | 400 |
| The error message returned because the specified user data is not encoded in Base64 format. | InvalidUserData.Base64F ormatInvalid | The specified parameter UserData must be base64 encoded. | 400 |

| Description | Error code | Error message | HTTP status code |
|---|---|---|---|
| The error message returned when the size of the raw user data exceeds 16 KiB. | InvalidUserData.SizeExce eded | The specified parameter UserData exceeds the size. | 400 |

Examples Sample requests

```
http://ess.example.com/?Action=CreateScalingConfiguration &ScalingGroupId=AG6CQdPU8OKdwLjgZcJ**** &SecurityGroupId=sg-280ih**** &ImageId=centos6u5_64_20G_alia****.vhd &InstanceType=ecs.t1.xsmall &<Common request parameters>
```

Sample responses XML format

```xml
<CreateScalingConfigurationResponse>
    <RequestId>5CC0AD41-08ED-4559-A683-6F56355FE068</RequestId>
    <ScalingConfigurationId>eOs27Kb0oXvQcUYjEGel****</ScalingConfigurationId>
</CreateScalingConfigurationResponse>
```

JSON format `{`

```json
    "RequestId": "5CC0AD41-08ED-4559-A683-6F56355FE068",
    "ScalingConfigurationId": "eOs27Kb0oXvQcUYjEGel****",
```

`}`

##### 2.1.8.2 DescribeScalingConfigurations

You can call this operation to query scaling configurations. Description You can specify a scaling configuration ID or name to query a specific scaling configuration, or specify the scaling group ID to query all scaling configurations of the scaling group. Scaling configuration status (LifecycleState) can be set to either of the following: Active: The scaling configuration is active in a scaling group. Scaling groups use scaling configurations in the active state to automatically create ECS instances. Inactive: The scaling configuration is inactive in a scaling group. The scaling group does not use scaling configurations in the inactive state to automatically create ECS instances. Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeScalingConfigurations. |
| RegionId | String | Yes | The ID of the region where a scaling group to which a scaling configuration belongs is located. |
| ScalingGroupId | String | No | The ID of the scaling group. |
| ScalingConfigurationId. N | String | No | The ID of the scaling configuration. Valid values of N: 1 to 10. The IDs of inactive scaling configurations do not appear in the query result without any error reported. |
| ScalingConfigurationNa me.N | String | No | The name of the scaling configuration. Valid values of N: 1 to 10. The names of inactive scaling configurations do not appear in the query result and no errors are reported. |
| PageNumber | Integer | No | The number of the page to return. Pages start from page 1. Default value: 1. |
| PageSize | Integer | No | The number of entries to return on each page. Valid values: 1 to 50. Default value: 10. |

Response parameters

| Parameter | Type | Description |
|---|---|---|
| TotalCount | Integer | The total number of scaling configurations. |
| PageNumber | Integer | The page number of the returned page. |
| PageSize | Integer | The number of entries returned per page. |
| ScalingConfigurations | ScalingConfigurationSetType | A collection of scaling configuration information. |

ScalingConfigurationSetType is a collection of ScalingConfigurationItemType.

| Parameter | Type | Description |
|---|---|---|
| ScalingConfiguration | ScalingConfigurationItemType | The scaling configuration information. |

The following table describes the attributes of ScalingConfigurationItemType.

| Parameter | Type | Description |
|---|---|---|
| ScalingConfigurationId | String | The ID of the scaling configuration. |
| ScalingConfigurationName | String | The display name of the scaling configuration. |
| ScalingGroupId | String | The ID of the scaling group to which the scaling configuration belongs. |
| ImageId | String | The ID of the image file. |
| InstanceType | String | The ECS instance type. |
| SecurityGroupId | String | The ID of the security group. |
| InternetMaxBandwidthIn | Integer | The maximum inbound bandwidth from the Internet. Unit: Mbit/s. |
| InternetMaxBandwidthOut | Integer | The maximum outbound bandwidth to the Internet. Unit: Mbit/s. |
| SystemDisk.Category | Integer | The category of the system disk. |
| DataDisks | DataDiskSetType | A collection of data disk details. |
| LifecycleState | Integer | The lifecycle of the scaling configuration in the scaling group. Valid values: Active: The scaling configuration is active in a scaling group. Scaling groups use scaling configurations in the active state to automatically create ECS instances. Inactive: The scaling configuration is inactive in a scaling group. The scaling group does not use scaling configurations in the inactive state to automatically create ECS instances. |
| CreationTime | String | The time when the scaling configuration is created. |

DataDiskSetType is a collection of DataDiskItemTypes.

| Parameter | Type | Description |
|---|---|---|
| DataDisk | DataDiskItemType | The data disk information. |

The following table describes the attributes of DataDiskItemType.

| Parameter | Type | Description |
|---|---|---|
| Size | Integer | The size of the disk. |
| Category | Integer | The category of the disk. |
| SnapshotId | Integer | The ID of the snapshot used to create data disks. |
| Device | Integer | The data disk mounting point. |

Error codes For more information about errors common to all operations, see Client errors or Server errors. Examples Sample requests

```
http://ess.example.com/?Action=CreateScalingConfiguration &RegionId=cn-qingdao &PageSize=50 &<Common request parameters>
```

Sample responses XML format

```xml
<DescribeScalingConfigurationsResponse>
    <RequestId>804F240A-8D3E-40A1-BD68-6B333DEA2CA8</RequestId>
    <TotalCount>1</TotalCount>
    <PageNumber>1</PageNumber>
    <PageSize>50</PageSize>
    <ScalingConfigurations>
        <ScalingConfiguration>
            <CreationTime>2014-08-14T10:58Z</CreationTime>
            <ImageId>centos6u5_64_20G_alia****.vhd</ImageId>
            <InstanceType>ecs.t1.xsmall</InstanceType>
            <InternetChargeType>PayByBandwidth</InternetChargeType>
            <InternetMaxBandwidthIn>200</InternetMaxBandwidthIn>
            <InternetMaxBandwidthOut>0</InternetMaxBandwidthOut>
            <LifecycleState>Active</LifecycleState>
            <ScalingConfigurationId>bU5uZHcAgtzwcL4IeDea****</ScalingConfigurationId>
            <ScalingConfigurationName>c1908dd1-690f-4c9b-ab73-350f1f06****</ScalingConfigur
ationName>
            <ScalingGroupId>dE9YbOdCHqaFdFZHXVdD****</ScalingGroupId>
            <SecurityGroupId>sg-280ih****</SecurityGroupId>
            <SystemDiskCategory>cloud</SystemDiskCategory>
            <DataDisks>
              <DataDisk>
                <Size>200</Size>
                <Category>cloud</Category>
                <SnapshotId>s-280s7****</SnapshotId>
                <Device>/dev/xvdb</Device>
              </DataDisk>
            </DataDisks>
        </ScalingConfiguration>
    </ScalingConfigurations>
</DescribeScalingConfigurationsResponse>
```

JSON format `{`

```json
  "RequestId": "67E4324F-CE14-4C2C-9D60-5422641DB76F",
  "TotalCount": 1,
  "PageNumber": 1,
  "PageSize": 1,
  "ScalingConfigurations": {
    "ScalingConfiguration": [
```

`{`

```json
        "ScalingConfigurationId": "eqkz17cfW3clcPExOtL****",
        "SecurityGroupId": "sg-28oew****",
        "CreationTime": "2014-08-18T21:07Z",
        "SystemDiskCategory": "cloud",
        "InternetMaxBandwidthIn": 200,
        "InternetMaxBandwidthOut": 0,
        "LifecycleState": "Inactive",
        "InternetChargeType": "PayByBandwidth",
        "ImageId": "rhel5u7_64_20G_alia****.vhd",
        "InstanceType": "ecs.s2.small",
        "ScalingConfigurationName": "LxVdcO****",
        "ScalingGroupId": "dRsEAGdvbjR5c4SVc2bq****",
        "DataDisks":{
              "DataDisk":[{
                "Size":200,
                "Category": cloud,
                "SnapshotId": s-280s7****,
                "Device":" /dev/xvdb"
```

`}]` `}` `}` `]` `}` `}`

##### 2.1.8.3 DeleteScalingConfiguration

You can call this operation to delete a scaling configuration. Description A scaling configuration that is active in a scaling group cannot be deleted. If any ECS instances that are created by a scaling configuration are still in a scaling group, the scaling configuration cannot be deleted. Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DeleteScalingConfiguration. |

| Parameter | Type | Required | Description |
|---|---|---|---|
| ScalingConfigurationId | String | Yes | The ID of the scaling configuration. |

Response parameters For more information, see Common response parameters. Error codes For more information about common error codes, see Client errors or Server errors.

| Description | Error code | Error message | HTTP status code |
|---|---|---|---|
| The error message returned because the specified scaling configuration does not exist in the current account. | InvalidScalingConfigurationId.N otFound | The specified scaling configuration does not exist. | 404 |
| The error message returned because the specified scaling configuration is not in the Inactive state. | IncorrectScalingConfigurationLi fecycleState | The current lifecycle state of specified scaling configuration does not support this action. | 400 |
| The error message returned because the specified scaling configuration still has associated ECS instances. | InstanceInUse | You cannot delete a scaling configuration or scaling group while there is an instance associated with it. | 400 |

Examples Sample requests

```
http://ess.example.com/?Action=DeleteScalingConfiguration &ScalingConfigurationId=eOs27Kb0oXvQcUYjEGel**** &<Common request parameters>
```

Sample responses XML format

```xml
<DeleteScalingConfigurationResponse>
    <RequestId>61D30272-7111-44D9-BB45-FCB55E4A1410</RequestId>
</DeleteScalingConfigurationResponse>
```

JSON format `{`

```json
    "RequestId": "61D30272-7111-44D9-BB45-FCB55E4A1410"
```

`}`

#### 2.1.9 Scaling rules

##### 2.1.9.1 CreateScalingRule

You can call this operation to create a scaling rule. A scaling rule defines specific scaling actions, such as attaching or removing Elastic Compute Service (ECS) instances and determining the number of instances to be scaled. If the number of ECS instances in a scaling group is smaller than MinSize or greater than MaxSize after the execution of a rule, Auto Scaling automatically adjusts the number of ECS instances to be added or removed by executing the "Adjust scaling group instance number to MinSize" or "Adjust scaling group instance number to MaxSize" rule. Example 1: A scaling group has a MaxSize of 3, a TotalCapacity of 2, and a scaling rule of adding three ECS instances. When executing this scaling rule, Auto Scaling adds only one instance to the group to prevent TotalCapacity from exceeding MaxSize. (The values in the scaling rule are not changed.) Example 2: A scaling group has a MinSize of 2, a TotalCapacity of 3, and a scaling rule of removing five ECS instances. When executing this scaling rule, Auto Scaling removes only one instance from the group to prevent TotalCapacity from becoming smaller than MinSize. (The values in the scaling rule are not changed.) Description You can create scaling rules based on input parameters. When the AdjustmentType value is TotalCapacity, the number of ECS instances currently in the scaling group is adjusted to the specified value. The corresponding AdjustmentValue value cannot be less than 0. When the AdjustmentType value is QuantityChangeInCapacity or PercentChangeInCapacity, a positive number of the AdjustmentValue value indicates adding ECS instances, and a negative number of the AdjustmentValue value indicates removing ECS instances. When AdjustmentType is set to PercentChangeInCapacity, Auto Scaling rounds the number of ECS instances to be scaled to the nearest integer based on the formula: Number of ECS instances to be scaled = Current number of instances × Value of AdjustmentValue/100. When the cool-down time (Cooldown) is specified in a scaling rule, the specified time is applied to the scaling group after this rule is executed. Otherwise, the DefaultCooldown is applied to the scaling group. A scaling group can have a maximum of 10 scaling rules. The following APIs use the unique identifier of a scaling rule (ScalingRuleAri) returned by this operation: ExecuteScalingRule: You can call this operation to manually run a specified scaling rule by setting ScalingRuleAri to the identifier. CreateScheduledTask: You can call this operation to create a periodically executed task for a specified scaling rule by setting ScheduledAction to the identifier. Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to CreateScalingRule. |
| ScalingGroupId | String | Yes | The ID of the scaling group to which the scaling rule belongs. |
| AdjustmentType | String | Yes | The adjustment mode of the scaling rule. Valid values: QuantityChangeInCapacity: adds or removes a specified number of ECS instances. PercentChangeInCapacity: adds or removes a specified proportion of ECS instances. TotalCapacity: adds or removes ECS instances to ensure that the current scaling group has a specified number of ECS instances. |
| AdjustmentValue | Integer | Yes | The number of ECS instances that are added or released when scaling occurs. QuantityChangeInCapacity: (0, 100] U (-100, 0] PercentChangeInCapacity: [0, 10000] U [-10000, 0] TotalCapacity: [0, 100] |
| ScalingRuleName | String | No | The display name of the scaling rule. The name must be 2 to 40 characters in length. It must start with a letter or digit. It can contain digits, uppercase letters, lowercase letters, underscores ( ), hyphens (-), and _ periods (.). The name of a scaling rule must be unique within the scaling group that it belongs to. If you do not specify this parameter, the default value (ScalingRuleId) is used. |
| Cooldown | Integer | No | The cool-down time of the scaling rule. Valid values: 0 to 86,400. Unit: seconds. Default value: empty. |

Response parameters

| Parameter | Type | Description |
|---|---|---|
| ScalingRuleId | String | The globally unique scaling rule ID generated by the system. |
| ScalingRuleAri | String | The unique identifier of the scaling rule. |

Error code For more information about common error codes, see Client errors or Server errors.

| Error message | Error code | Description | HTTP status code |
|---|---|---|---|
| The error message returned when the specified scaling group does not exist under this account. | InvalidScalingGroupId.N otFound | The specified scaling group does not exist. | 404 |
| The error message returned when the scaling rule name already exists. | InvalidScalingRuleName. Duplicate | The specified value of parameter <parameter name> is duplicated. | 400 |
| The error message returned when the number of scaling rules in the specified scaling group reaches the upper limit. | QuotaExceeded.Scaling Rule | Scaling rule quota exceeded in the specified scaling group. | 400 |

Examples Sample request s

```
http://ess.example.com/?Action=CreateScalingRule &ScalingGroupId=AG6CQdPU8OKdwLjgZcJ**** &AdjustmentType=QuantityChangeInCapacity &AdjustmentValue=-10 &<Common request parameter>
```

Response examples XML format

```xml
<CreateScalingRuleResponse>
    <RequestId>570C84F4-A434-488A-AFA1-1E3213682B33</RequestId>
    <ScalingRuleId>eMKWG8SRNb9dBLAjweN****</ScalingRuleId>
    <ScalingRuleAri>ari:acs:ess:cn-qingdao:1344371:scalingrule/eMKWG8SRNb9dBLAjweN****</Sca
lingRuleAri> </CreateScalingRuleResponse>
```

JSON format `{`

```json
    "RequestId": "04F0F334-1335-436C-A1D7-6C044FE73368",
    "ScalingRuleId": "eMKWG8SRNb9dBLAjweN****",
    "ScalingRuleAri":"ari:acs:ess:cn-qingdao:1344371:scalingrule/eMKWG8SRNb9dBLAjweN****"
```

`}`

##### 2.1.9.2 ModifyScalingRule

You can modify a scaling rule. Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to ModifyScalingRule. |
| ScalingRuleId | String | Yes | The ID of the scaling rule. |
| AdjustmentType | String | No | The adjustment type of the scaling rule. Valid values: QuantityChangeInCapacity: adds or removes the specified number of ECS instances. PercentChangeInCapacity: adds or removes the specified proportion of ECS instances. TotalCapacity: adds or removes ECS instances to ensure that the current scaling group has the specified number of ECS instances. |
| AdjustmentValue | Integer | No | The number of ECS instances that are added or released when scaling occurs. Valid values: QuantityChangeInCapacity: (0, 100] U [-100, 0) PercentChangeInCapacity: [0, 10000] U [-10000, 0] TotalCapacity: [0, 100] |

| Parameter | Type | Required | Description |
|---|---|---|---|
| ScalingRuleName | String | No | The display name of the scaling rule. The name must be 2 to 40 characters in length. It must start with a letter or number. It can contain numbers, uppercase letters, lowercase letters, underscores ( ), _ hyphens (-), and periods (.). The name of a scaling rule must be unique within the scaling group that it belongs to. If you do not specify this parameter, the default value (ScalingRuleId) is used. |
| Cooldown | Integer | No | The cool-down time of the scaling rule. Valid values: 0 to 86,400. Unit: second. Default value: empty. |

Response parameters

| parameter | Type | Description |
|---|---|---|
| ScalingRuleId | String | The globally unique scaling rule ID generated by the system. |
| ScalingRuleAri | String | The unique identifier of the scaling rule. |

Error code For more information about common error codes, see Client errors or Server errors.

| Error message | Error code | Description | HTTP status code |
|---|---|---|---|
| The error message returned when the specified scaling group does not exist under this account. | InvalidScalingGroupId.N otFound | The specified scaling group does not exist. | 404 |
| The error message returned when the scaling rule name already exists. | InvalidScalingRuleName. Duplicate | The specified value of parameter <parameter name> is duplicated. | 400 |

| Error message | Error code | Description | HTTP status code |
|---|---|---|---|
| The error message returned when the number of scaling rules in the specified scaling group reach the upper limit. | QuotaExceeded.Scaling Rule | Scaling rule quota exceeded in the specified scaling group. | 400 |

Examples Sample request s

```
http://ess.example.com/?Action=CreateScalingRule &ScalingGroupId=AG6CQdPU8OKdwLjgZcJ**** &AdjustmentType=QuantityChangeInCapacity &AdjustmentValue=-10 &<Common request parameter>
```

Response examples XML format

```xml
<CreateScalingRuleResponse>
    <RequestId>570C84F4-A434-488A-AFA1-1E3213682B33</RequestId>
    <ScalingRuleId>eMKWG8SRNb9dBLAjweN****</ScalingRuleId>
    <ScalingRuleAri>ari:acs:ess:cn-qingdao:1344371:scalingrule/eMKWG8SRNb9dBLAjweN****</Sca
lingRuleAri> </CreateScalingRuleResponse>
```

JSON format `{`

```json
    "RequestId": "04F0F334-1335-436C-A1D7-6C044FE73368",
    "ScalingRuleId": "eMKWG8SRNb9dBLAjweN****",
    "ScalingRuleAri":"ari:acs:ess:cn-qingdao:1344371:scalingrule/eMKWG8SRNb9dBLAjweN****"
```

`}`

##### 2.1.9.3 DescribeScalingRules

You can query information about scaling rules. You can query all scaling rules in a scaling group by specifying the scaling group ID. Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeScalingRules. |

| eveloper Guide·API refer | ence |   | Auto Scalin |
|---|---|---|---|

| Parameter | Type | Required | Description |
|---|---|---|---|
| RegionId | String | Yes | The ID of the region where the scaling group to which a scaling rule belongs is located. |
| ScalingGroupId | String | No | The ID of the scaling group to which a scaling rule belongs. |
| ScalingRuleId.N | String | No | The ID of scaling rule N. N ranges from 1 to 10. The IDs of inactive scaling rules are ignored in the query result and no error is reported. |
| ScalingRuleName.N | String | No | The name of scaling rule N. N ranges from 1 to 10. The names of inactive scaling rules are ignored in the query result and no error is reported. |
| ScalingRuleAri.N | String | No | The unique identifier of scaling rule N. N ranges from 1 to 10. The unique identifiers of inactive scaling rules are ignored in the query result and no error is reported. |
| PageNumber | Integer | No | The page number of the scaling rule list. The initial value and default value are both 1. |
| PageSize | Integer | No | The number of lines per page in paged query. Maximum value: 50. Default value: 10. |

Response parameters

| parameter | Type | Description |
|---|---|---|
| TotalCount | Integer | The total number of scaling rules. |
| PageNumber | Integer | The number of the current page. |
| PageSize | Integer | The number of lines per page. |
| ScalingRules | ScalingRuleSetType | A collection of details about the scaling rules you queried. |

The ScalingRuleSetType is a collection of the ScalingRuleItemType.

| Parameter | Type | Description |
|---|---|---|
| ScalingRule | ScalingRuleItemType | The details of a scaling rule. |

The following table describes the attributes of ScalingRuleItemType.

| Parameter | Type | Description |
|---|---|---|
| ScalingRuleId | String | The ID of the scaling rule. |
| ScalingGroupId | String | The ID of a scaling group. |
| ScalingRuleName | String | The name of a scaling rule. |
| Cooldown | Integer | The cool-down time of the scaling rule. |
| AdjustmentType | String | The adjustment method of the scaling rule. |
| AdjustmentValue | Integer | The adjustment value of the scaling rule. |
| ScalingRuleAri | String | The unique identifier of the scaling rule. |

Error code For more information about common error codes, see Client errors or Server errors. Examples Sample request s

```
http://ess.example.com/?Action=DescribeScalingRules &RegionId=cn-qingdao &ScalingGroupId=AG6CQdPU8OKdwLjgZcJ**** &PageSize=50 &<Common request parameter>
```

Response examples XML format

```xml
<DescribeScalingRulesResponse>
    <PageNumber>1</PageNumber>
    <PageSize>50</PageSize>
    <ScalingRules>
        <ScalingRule>
            <AdjustmentType>QuantityChangeInCapacity</AdjustmentType>
            <AdjustmentValue>1</AdjustmentValue>
            <Cooldown>20</Cooldown>
            <ScalingGroupId>AG6CQdPU8OKdwLjgZcJ****</ScalingGroupId>
            <ScalingRuleAri>ari:acs:ess:cn-qingdao:1344371:scalingRule/eMKWG8SRNb9dBLAjweN*
***</ScalingRuleAri>
            <ScalingRuleId>eMKWG8SRNb9dBLAjweN****</ScalingRuleId>
            <ScalingRuleName>eMKWG8SRNb9dBLAjweN****</ScalingRuleName>
        </ScalingRule>
    </ScalingRules>
    <TotalCount>1</TotalCount>
    <RequestId>3306A40D-3412-4101-9F19-5F81E3055DAD</RequestId>
</DescribeScalingRulesResponse>
```

JSON format `{`

```json
  "RequestId": "B583BFEF-A779-427A-9B74-262DDD249702",
  "TotalCount": 1,
  "PageNumber": 1,
  "PageSize": 10,
  "ScalingRules": {
  "ScalingRule": [
```

`{`

```json
        "ScalingRuleId": "efcqrZdjlookc0UkE3dA****",
        "ScalingRuleAri": "ari:acs:ess:cn-qingdao:1344371:scalingRule/efcqrZdjlookc0UkE3dA*
***",
        "Cooldown": 500,
        "ScalingGroupId": "ccMvs9dcZlE5c9CtrwbX****",
        "AdjustmentType": "TotalCapacity",
        "ScalingRuleName": "KFJoxG****",
        "AdjustmentValue": 5
```

`}` `]` `}` `}`

##### 2.1.9.4 DeleteScalingRule

You can delete the specified scaling rule. Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DeleteScalingRule. |
| ScalingRuleId | String | Yes | The ID of the scaling rule. |

Response parameters For more information about response parameters, see Common response parameters. Error code For more information about common error codes, see Client errors or Server errors.

| Error message | Error code | Description | HTTP status code |
|---|---|---|---|
| The error message returned when the specified scaling rule does not exist under this account. | InvalidScalingRuleId.Not Found | The specified scaling rule does not exist. | 404 |

Examples Sample request s

```
http://ess.example.com/?Action=DeleteScalingRule &ScalingRuleId=eMKWG8SRNb9dBLAjweN**** &<Common request parameter>
```

Response examples XML format

```xml
<DeleteScalingRuleResponse>
    <RequestId>F0595173-CA3A-4597-B0D3-97A07A042B9C</RequestId>
</DeleteScalingRuleResponse>
```

JSON format `{`

```json
    "RequestId": "F0595173-CA3A-4597-B0D3-97A07A042B9C"
```

`}`

#### 2.1.10 Scaling tasks

##### 2.1.10.1 ExecuteScalingRule

You can run a specified scaling rule. You can call this operation to run a scaling rule. You can only call this operation when the scaling group is active. You can only call this operation when the scaling group is not currently undergoing any scaling activities. If the scaling group does not have any scaling activities in progress, the operation can be immediately run without the need to wait for the cooldown period to expire. When you call this operation successfully, Auto Scaling receives the request and the scaling activity can be run. However, this operation may be unsuccessful. You can use the returned ScalingActivityId parameter to view the status of the scaling activity. If the number of ECS instances to be added would leave the number of instances in the scaling group greater than MaxSize, the rule Total Capacity = MaxSize is applied. If the number of ECS instances to be removed would leave the number of instances in the scaling group less than MinSize, the rule Total Capacity = MinSize is applied. A maximum of 100 ECS instances can be scaled automatically over all groups in all regions. Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to ExecuteScalingRule. |
| ScalingRuleAri | String | Yes | The unique identifier of the scaling rule. |
| ClientToken | String | No | This parameter is used to ensure the idempotence of the request. The value of this parameter is generated by the client and is unique among different requests. The maximum length is 64 ASCII characters. For more information about the ClientToken, see Ensure idempotence. |

Response parameters

| parameter | Type | Description |
|---|---|---|
| ScalingActivityId | String | The ID of the scaling activity. |

Error code For more information about common error codes, see Client errors or Server errors.

| Error message | Error code | Description | HTTP status code |
|---|---|---|---|
| The error message returned when the specified scaling rule does not exist under this account. | InvalidScalingRuleAri.No tFound | The specified scaling rule Ari does not exist. | 404 |
| The error message returned when Auto Scaling does not have full authorization to Open API. | Forbidden.Unauthorized | A required authorization for the specified action is not supplied. | 403 |
| The error message returned when the scaling group to which the specified scaling rule belongs is inactive. | IncorrectScalingGroupSt atus | The current status of the specified scaling group does not support this action. | 400 |
| The error message returned when the scaling group to which the specified scaling rule belongs has a scaling activity. | ScalingActivityInProgres s | You cannot delete a scaling group or launch a new scaling activity while there is a scaling activity in progress for the specified scaling group. | 400 |
| The error message returned when the number of ECS instances under this account reach the upper limit. | QuotaExceed.Instance | Living instance quota exceeded. | 400 |
| The error message returned when the Server Load Balancer instance in the scaling group to which the specified scaling rule belongs is not active. | IncorrectLoadBalancerSt atus | The current status of the specified load balancer does not support this action. | 400 |
| The error message returned when the health check is not enabled for the SLB instance in the scaling group to which the specified scaling rule belongs. | IncorrectLoadBalancerH ealthCheck | The current health check type of the specified load balancer does not support this action. | 400 |

| Error message | Error code | Description | HTTP status code |
|---|---|---|---|
| The error message returned when the network type of the ECS instance connected to the specified SLB instance is different from that of the scaling group. | InvalidLoadBalancerId.In correctInstanceNetwork Type | The network type of the instance in the specified load balancer does not support this action. | 400 |
| The error message returned when the ECS instance connected to the SLB instance of the specified scaling group and the VSwitch are not in the same VPC. | InvalidLoadBalancerId.V PCMismatch | The specified virtual switch and the instance in the specified load balancer are not in the same VPC. | 400 |
| The error message returned when the RDS instance in the scaling group to which the specified scaling rule belongs is not running. | IncorrectDBInstanceStat us | The current status of DB instance "XXX" does not support this action. | 400 |
| The error message returned when the number of IP addresses in the RDS instance whitelist in the scaling group to which the scaling rule belongs reach the upper limit. | QuotaExceeded.DBInsta nceSecurityIP | Security IP quota exceeded in DB instance "XXX". | 400 |
| The error message returned when the number of ECS instances already added to the specified security group reach the upper limit. | QuotaExceeded.Security GroupInstance | Instance quota exceeded in the specified security group. | 400 |
| The error message returned when there is no change in the number of instances in the scaling group after the scaling rule is executed. | IncorrectCapacity.NoCha nge | To execute the specified scaling rule, the total capacity will not change. | 400 |

| Error message | Error code | Description | HTTP status code |
|---|---|---|---|
| The error message returned when the number of ECS instances of Auto Scaling reach the upper limit. | QuotaExceeded.ScalingI nstance | Scaling instance quota exceeded. | 400 |
| The error message returned when the ECS instance or disk of the specified type cannot be created in the specified region. | ResourceNotAvailable.E CS | The specified region or zone does not offer the specified disk or instance category. | 400 |

Examples Sample request s

```
http://ess.example.com/?Action=ExecuteScalingRule &ScalingRuleAri=ari:acs:ess:cn-qingdao:1344371:scalingRule/cCBpdYdQuBe2cUxOdu6**** &<Common request parameter>
```

Response examples XML format

```xml
<ExecuteScalingRuleResponse>
   <RequestId>262216B9-F9D4-4D16-BE9B-BD1C39A4F42B</RequestId>
   <ScalingActivityId>ebta5WbUzC8gcwUWvfch****</ScalingActivityId>
</ExecuteScalingRuleResponse>
```

JSON format `{`

```json
    "RequestId": "6469DCD0-13AC-487E-85A0-CE4922908FDE",
    "ScalingActivityId": "ebta5WbUzC8gcwUWvfch****"
```

`}`

##### 2.1.10.2 AttachInstances

You can call this operation to add Elastic Compute Service (ECS) instances to a specified scaling group. Description The restrictions on an added ECS instance are as follows: The added ECS instance and the scaling group must be in the same region. The added ECS instance must be running. The added ECS instance cannot be added to another scaling group. If the VSwitchId parameter is specified for a scaling group, Elastic Compute Service instances which reside in a classic network or in other VPCs cannot be added to the scaling group. If the VSwitchId parameter is not specified for a scaling group, ECS instances of the VPC network type cannot be added to the scaling group. This operation can only be called when the scaling group is active. This operation can only be called when the scaling group is not currently undergoing any scaling activities. If the scaling group does not have any scaling activities in progress, the operation can be immediately run without the need to wait for the cooldown period to expire. When this operation is called, Auto Scaling receives the request. However, it is not guaranteed that the scaling activity can be run as intended. You can use the returned ScalingActivityId parameter to view the status of the scaling activity. When the sum of the number of ECS instances currently in the scaling group (Total Capacity) and the number of instances to be added specified by this operation is greater than MaxSize, calling the operation fails. Manually added ECS instances are not associated with the active scaling configuration of the scaling group. Request parameters Request parameter description

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to AttachInstances. |
| ScalingGroupId | String | Yes | The ID of the scaling group. |
| InstanceId.N | String | Yes | The ID of the ECS instance. N ranges from 1 to 20. |

Response parameters

| parameter | Type | Description |
|---|---|---|
| ScalingActivityId | String | The ID of the scaling activity. |

Error code For more information about common error codes, see Client errors or Server errors.

| Error message | Error code | Description | HTTP status code |
|---|---|---|---|
| The error message returned when the specified scaling group does not exist under this account. | InvalidScalingGroupId.NotFound | The specified scaling group does not exist. | 404 |
| The error message returned when Auto Scaling does not have full authorization with Open API. | Forbidden.Unauthorized | A required authorization for the specified action is not supplied. | 403 |
| The error message returned when the specified scaling group is inactive. | IncorrectScalingGroupStatus | The current status of the specified scaling group does not support this action. | 400 |
| The error message returned when the specified ECS instance does not exist under this account. | InvalidInstanceId.NotFound | Instance "XXX" does not exist. | 404 |
| The error message returned when the specified Elastic Compute Service instance and the scaling group are not in the same region. | InvalidInstanceId. RegionMismatch | Instance "XXX" and the specified scaling group are not in the same Region. | 400 |
| The error message returned when the specified Elastic Compute Service instance type is different from that of the active scaling configuration. | InvalidInstanceId.InstanceTypeMismatc h | Instance "XXX" and existing active scaling configurations have different instance types. | 400 |
| The error message returned when the specified Elastic Compute Service instance is not running. | IncorrectInstanceStatus | The current status of instance "XXX" does not support this action. | 400 |

| Error message | Error code | Description | HTTP status code |
|---|---|---|---|
| The error message returned when the network type of the specified ECS instance is different from that of the scaling group. | InvalidInstanceId. NetworkTypeMismatch | The network type of instance "XXX" does not support this action. | 400 |
| The error message returned when the added ECS instance and the specified scaling group are not in the same Virtual Private Cloud. | InvalidInstanceId.VPCMismatch | Instance "XXX" and the specified scaling group are not in the same Virtual Private Cloud. | 400 |
| The error message returned when the specified ECS instance is added to another scaling group. | InvalidInstanceId.InUse | Instance "XXX" is already added to another scaling group. | 400 |
| The error message returned when the specified scaling group has a scaling activity in progress. | ScalingActivityInProgress | You cannot delete a scaling group or launch a new scaling activity while there is a scaling activity in progress for the specified scaling group. | 400 |
| The error message returned when the SLB instance in the specified scaling group is inactive. | IncorrectLoadBalancerStatus | The current status of the specified load balancer does not support this action. | 400 |
| The error message returned when the health check is not enabled for the specified SLB instance. | IncorrectLoadBalancerHealthCheck | The current health check type of specified load balancer does not support this action. | 400 |

| Error message | Error code | Description | HTTP status code |
|---|---|---|---|
| The error message returned when the network type of the ECS instance connected to the specified SLB instance is different from that of the scaling group. | InvalidLoadBalancerId.IncorrectInstance NetworkType | The network type of the instance in the specified load balancer does not support this action. | 400 |
| The error message returned when the Elastic Compute Service instance connected to the SLB instance of the specified scaling group and the VSwitch are not in the same VPC. | InvalidLoadBalancerId.VPCMismatch | The specified virtual switch and the instance in the specified load balancer are not in the same Virtual Private Cloud. | 400 |
| The error message returned when the RDS instance in the specified scaling group is not running. | IncorrectDBInstanceStatus | The current status of DB instance "XXX" does not support this action. | 400 |
| The error message returned when the number of IP addresses in the specified RDS instance whitelist reach the upper limit. | QuotaExceeded.DBInstanceSecurityIP | Security IP quota exceeded in DB instance "XXX". | 400 |
| The error message returned when the number of ECS instances in the specified security group reach the upper limit. | QuotaExceeded.SecurityGroupInstance | Instance quota exceeded in the specified security group. | 400 |

| Error message | Error code | Description | HTTP status code |
|---|---|---|---|
| The error message returned when the total number of ECS instances (Total Capacity) exceed MaxSize after an instance is added to the specified scaling group. | IncorrectCapacity.MaxSize | To add the instances, the total capacity will be greater than the MaxSize. | 400 |

Examples Sample request s

```
http://ess.example.com/?Action=AttachInstances &ScalingGroupId=AG6CQdPU8OKdwLjgZcJ**** &InstanceId. 1=i-28wt4**** &<Common request parameter>
```

Response examples XML format

```xml
<AttachInstancesResponse>
    <RequestId>DD0309B7-2613-4792-9B86-275906695253</RequestId>
    <ScalingActivityId>bybj9OcaOT4ucPMbFhcqHfA3</ScalingActivityId>
</AttachInstancesResponse>
```

JSON format `{`

```json
    "RequestId": "6469DCD0-13AC-487E-85A0-CE4922908FDE",
    "ScalingActivityId":"ebta5WbUzC8gcwUWvfch****"
```

`}`

##### 2.1.10.3 RemoveInstances

You can remove ECS instances from a specified scaling group. Description When an ECS instance automatically created by Auto Scaling is removed from a scaling group, the ECS instance is stopped and released. When a manually added ECS instance is removed from a scaling group, the ECS instance is neither stopped nor released. This operation can only be called when the scaling group is active. You can only call this operation when the scaling group does not currently have any scaling activities. If no scaling activity in the scaling group is in progress, the operation can be run immediately without waiting for cooldown to expire. When this operation is called, Auto Scaling receives the request. However, it is not guaranteed that the scaling activity can be run as intended. You can use the returned ScalingActivityId parameter to check the status of the scaling activity. When the difference between the number of ECS instances currently in the scaling group (Total Capacity) and the number of ECS instances to be removed is smaller than MinSize, calling the operation fails. Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to RemoveInstances. |
| ScalingGroupId | String | Yes | The ID of the scaling group. |
| InstanceId.N | String | Yes | The ID of the ECS instance. N ranges from 1 to 20. |

Response parameters

| Parameter | Type | Description |
|---|---|---|
| ScalingActivityId | String | The ID of the scaling activity. |

Error code For more information about common error codes, see Client errors or Server errors.

| Error message | Error code | Description | HTTP status code |
|---|---|---|---|
| The error message returned when the specified scaling group does not exist under this account. | InvalidScalingGroupId.N otFound | The specified scaling group does not exist. | 404 |
| The error message returned when the specified ECS instance does not exist in the scaling group. | InvalidInstanceId.NotFou nd | Instance "XXX" does not exist. | 404 |
| The error message returned when Auto Scaling does not have full authorization to Open API. | Forbidden.Unauthorized | The required authorization for the specified action is not supplied. | 403 |

| Error message | Error code | Description | HTTP status code |
|---|---|---|---|
| The error message returned when the specified scaling group is not active. | IncorrectScalingGroupSt atus | The current status of the specified scaling group does not support this action. | 400 |
| The error message returned when the specified scaling group is currently undergoing a scaling activity. | ScalingActivityInProgres s | You cannot delete a scaling group or launch a new scaling activity while there is a scaling activity in progress for the specified scaling group. | 400 |
| The error message returned when the SLB instance in the scaling group to which the specified scaling rule belongs is inactive. | IncorrectLoadBalancerSt atus | The current status of the specified load balancer does not support this action. | 400 |
| The error message returned when the RDS instance in the scaling group to which the specified scaling rule belongs is not running. | IncorrectDBInstanceStat us | The current status of DB instance "XXX" does not support this action. | 400 |
| The error message returned when the number of ECS instances to be removed will leave fewer total ECS instances than MinSize. | IncorrectCapacity.MinSiz e | To remove the instances, the total capacity will be lesser than the MinSize. | 400 |

Examples Sample request s

```
http://ess.example.com/?Action=RemoveInstances &ScalingGroupId=AG6CQdPU8OKdwLjgZcJ**** &InstanceId. 1=i-28wt4**** &<Common request parameter>
```

Response examples XML format

```xml
<RemoveInstancesResponse>
    <RequestId>DD0309B7-2613-4792-9B86-275906695253</RequestId>
    <ScalingActivityId>bybj9OcaOT4ucPMbFhcq****</ScalingActivityId>
</RemoveInstancesResponse>
```

JSON format `{`

```json
    "RequestId": "6469DCD0-13AC-487E-85A0-CE4922908FDE",
    "ScalingActivityId": "ebta5WbUzC8gcwUWvfch****"
```

`}`

##### 2.1.10.4 DetachInstances

You can call this operation to remove one or more Elastic Compute Service (ECS) instances from a scaling group. Description After an ECS instance is removed, it can either exist independent of any scaling group or be added to another scaling group. For more information about AttachInstances, see AttachInstances. Removing an ECS instance does not stop or release it. You can manually stop or release an ECS instance as needed. When calling this operation, you must take note of the following points: The specified scaling group must be enabled. The specified scaling group must not have any scaling activities in progress. If there is no scaling activity currently in progress in the scaling group, the operation can be immediately run without waiting for the cooldown period to expire. When this operation is called successfully, Auto Scaling receives the request. The scaling activity can be triggered, but it is not guaranteed that the scaling activity can be successfully run. You can use the ScalingActivityId parameter returned in the response to query the status of the scaling activity. The difference between the number of ECS instances currently in the specified scaling group and the number of ECS instances to be removed must not be smaller than MinSize. Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DetachInstances. |
| ScalingGroupId | String | Yes | The ID of the scaling group. |
| InstanceId.N | String | Yes | The ID of the ECS instance. N can be an integer from 1 to 20. |

Response parameters

| Parameter | Type | Description |
|---|---|---|
| RequestId | String | The request ID. |
| ScalingActivityId | String | The ID of the scaling activity. |

Examples Sample requests

```
http://ess.example.com/?Action=DetachInstances &ScalingGroupId=AG6CQdPU8OKdwLj**** &InstanceId. 1=i-28wt4**** & <Common request parameters>
```

Response examples XML f ormat

```xml
<DetachInstancesResponse>
    <RequestId>04F0F334-1335-436C-A1D7-6C044FE73368</RequestId>
    <ScalingActivityId>asa-xxxxxxxxx</ScalingActivityId>
</DetachInstancesResponse>
```

JSON f ormat `{`

```json
    "RequestId": "04F0F334-1335-436C-A1D7-6C044FE73368",
    "ScalingActivityId":"asa-****"
```

`}` Error code

| Error code | Error message | HTTP status code | Description |
|---|---|---|---|
| IncorrectScalingGroupSt atus | The current status of the specified scaling group does not support this action. | 400 | The error message returned when the specified scaling group is not enabled. |
| ScalingActivityInProgres s | You cannot delete a scaling group or launch a new scaling activity while there is a scaling activity in progress for the specified scaling group. | 400 | The error message returned when the specified scaling group currently has a scaling activity. |
| IncorrectLoadBalancerSt atus | The current status of the specified load balancer does not support this action. | 400 | The error message returned when the SLB instance is not active in the specified scaling group. |

| Error code | Error message | HTTP status code | Description |
|---|---|---|---|
| IncorrectDBInstanceStat us | The current status of DB instance "XXX" does not support this action. | 400 | The error message returned when the RDS instance in the specified scaling group is not running. |
| IncorrectCapacity.MinSiz e | To remove the instances, the total capacity will be lesser than the MinSize. | 400 | The error message returned when removing a number of ECS instances from a scaling group, which will cause the group to contain fewer ECS instances than the MinSize value. |
| Forbidden.Unauthorized | A required authorization for the specified action is not supplied. | 403 | The error message returned when you are not authorized to call this operation. |
| InvalidScalingGroupId.N otFound | The specified scaling group does not exist. | 404 | The error message returned when the specified scaling group does not exist. |
| InvalidInstanceId.NotFou nd | Instance "XXX" does not exist. | 404 | The error message returned when the specified ECS instance does not exist. |

#### 2.1.11 Scheduled tasks

##### 2.1.11.1 CreateScheduledTask

You can call this operation to create scheduled tasks based on specified input parameters. Description You can create a maximum of 20 scheduled tasks. When a scheduled task fails to trigger due to an ongoing scaling activity in a scaling group or the scaling group is disabled, the scheduled task will be retried for the duration of the launch expiration time. After the duration of the launch expiration time, a scheduled task that has failed to be triggered will be abandoned. If multiple tasks are scheduled at similar times to run scaling rules in the same group, the earliest task will run its scaling activity first. Other tasks will make attempts to execute their rules during their launch expiration time, but only one scaling activity can be run in a scaling group at a time. If the previous scaling activity is completed while another scheduled task is making triggering attempts during its launch expiration time, the scaling rule is executed and the corresponding scaling activity is triggered. Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to CreateScheduledTask. |
| RegionId | String | Yes | The ID of the region where the scheduled task is located. |
| ScheduledAction | String | Yes | The operations to be performed when the scheduled task is triggered. When you set this parameter, you must also enter the unique identifier of the scaling rule. |
| LaunchTime | String | Yes | The time at which the scheduled task is triggered. Specify the time in the ISO 8601 standard in the YYYY-MM- DDThh:mmZ format. The time must be in UTC. If the RecurrenceType parameter is specified, the task will be executed repeatedly at the time specified by LaunchTime. If the RecurrenceType parameter is not specified, the task is only executed once at the date and time specified by LaunchTime. You cannot enter a time point later than 90 days from the scheduled task creation or modification. |
| ScheduledTaskName | String | No | The display name of the scheduled task. The name must be 2 to 40 characters in length and can contain digits, letters, underscores ( ), hyphens (-), _ and periods (.). It must start with a letter or digit. The name of the scheduled task must be unique within the same region for the same Alibaba Cloud tenant account. If you do not specify this parameter, the default value is ScheduledScalingTaskId. |

| Parameter | Type | Required | Description |
|---|---|---|---|
| Description | String | No | The description of the scheduled task. The description must be 2 to 200 characters in length. |
| LaunchExpirationTime | Integer | No | The time period during which a failed scheduled task is retried. Default value: 600. Unit: seconds. Valid values: 0 to 21600. |
| RecurrenceType | String | No | The type of the scheduled task to be repeated. Valid values: Daily: The scheduled task is executed once after the specified number of days. Weekly: The scheduled task is executed on each specified day of a week. Monthly: The scheduled task is executed on each specified day of a month. If you set RecurrenceType, you must also set both RecurrenceEndTime and RecurrenceValue. |
| RecurrenceValue | String | No | The recurrence value of the scheduled task to be repeated. Daily: You can enter a single value ranging from 1 to 31. Weekly: You can enter multiple values corresponding to the days of the week. The values of Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, and Saturday are 0 to 6 in sequence. Separate multiple values with commas (,). Monthly: You can enter two values ranging from 1 to 31. The format is A-B. B must be greater than or equal to A. If you set RecurrenceValue, you must also set both RecurrenceEndTime and RecurrenceType. |

| Parameter | Type | Required | Description |
|---|---|---|---|
| RecurrenceEndTime | String | No | The end time of the scheduled task to be repeated. Specify the time in the ISO 8601 standard in the YYYY-MM-DDThh:mmZ format. The time must be in UTC. You cannot enter a time point later than 90 days from the scheduled task creation or modification. If you set RecurrenceEndTime, you must also set both RecurrenceValue and RecurrenceType. |
| TaskEnabled | Bool | No | Specifies whether to start the scheduled task. true: starts the scheduled task. false: stops the scheduled task. Default value: true. |

Response parameters

| Parameter | Type | Description |
|---|---|---|
| ScheduledTaskId | String | The globally unique ID of the scheduled task generated by the system. |

Error codes For more information about errors common to all operations, see Client errors or Server errors.

| Description | Error code | Error message | HTTP status code |
|---|---|---|---|
| The error message returned because the specified region does not exist. | InvalidRegionId.NotFoun d | The specified region does not exist. | 404 |
| The error message returned because the name of the scheduled task already exists. | InvalidScheduledTaskNa me.Duplicate | The specified value of parameter <parameter name> is duplicated. | 400 |

| Description | Error code | Error message | HTTP status code |
|---|---|---|---|
| The error message returned because the specified ScheduledAction parameter and the scheduled task are not in the same region. | ScheduledAction.Region Mismatch | The specified scheduled task and the specified scheduled action are not in the same Region. | 400 |
| The error message returned because the number of scheduled tasks created by you reaches the upper limit. | QuotaExceeded.Schedul edTask | Scheduled task quota exceeded. | 400 |

Examples Sample request s

```
http://ess.example.com/?Action=CreateScheduledTask &RegionId=cn-qingdao &LaunchTime=2014-08-17T16:52Z &RecurrenceType=Daily &RecurrenceValue=1 &RecurrenceEndTime=2014-08-17T16:55Z &ScheduledAction=ari:acs:ess:cn-qingdao:1344371:scalingRule/cCBpdYdQuBe2cUxOdu6**** &<Common request parameters>
```

Sample responses XML format

```xml
<CreateScheduledTaskResponse>
    <RequestId>0F02D931-2B12-44D7-A0E9-39925C13D15E</RequestId>
    <ScheduledTaskId>edRtShc57WGXdt8TlPbr****</ScheduledTaskId>
</CreateScheduledTaskResponse>
```

JSON format `{`

```json
    "RequestId": "04F0F334-1335-436C-A1D7-6C044FE73368",
    "ScheduledTaskId": "edRtShc57WGXdt8TlPbr****"
```

`}`

##### 2.1.11.2 ModifyScheduledTask

You can modify a scheduled task. Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to ModifyScheduledTask. |
| ScheduledTaskId | String | Yes | The ID of the scheduled task. |
| ScheduledTaskName | String | No | The display name of the scaling rule. The name must be 2 to 40 characters in length. It must start with a letter or number. It can contain numbers, uppercase letters, lowercase letters, underscores ( ), hyphens (-), _ and periods (.). The name of the scheduled task must be unique within the same region for the same Alibaba Cloud account. If you do not specify this parameter, the default value (ScheduledScalingTaskId) is used. |
| Description | String | No | The description of the scheduled task. It must be 2 to 200 characters in length. |
| ScheduledAction | String | No | The operation performed when the scheduled task is triggered. Enter the unique identifier of the scaling rule. |
| LaunchTime | String | No | The time at which the scheduled task is triggered. UTC time is used and complies with the ISO 8601 standard. The format is YYYY-MM- DDThh:mm:ssZ. If the RecurrenceType parameter is specified, the task will be executed repeatedly at the time specified by LaunchTime. If the RecurrenceType parameter is not specified, the task is only executed once at the time specified by LaunchTime. You cannot enter a time point later than 90 days from the date of the scheduled task creation or modification. |

| Parameter | Type | Required | Description |
|---|---|---|---|
| LaunchExpirationTime | Integer | No | You can retry the task during this time period after the scheduled task fails. Unit: second. Default value: 600. Valid values: [0, 21600]. |
| RecurrenceType | String | No | The type of the scheduled task to be repeated. Valid values: Daily: The scheduled task is executed once after the specified number of days. Weekly: The scheduled task is run on each specified day of the week. Monthly: The scheduled task is run on each specified day of the month. After the scheduled task is modified, RecurrenceType, RecurrenceValue, and RecurrenceEndTime must be valid. |

| Parameter | Type | Required | Description |
|---|---|---|---|
| RecurrenceValue | String | No | The value determining how often a scheduled task recurs. Daily: indicates the interval of days that a scheduled task is repeated on. You can enter a single value ranging from 1 to 31. Weekly: indicates which days of the week that a scheduled task is repeated on. You can enter multiple values separated by commas (,). You can specify numbers from 0 to 6 for days from Sunday to Saturday in sequence. Multiple values must be separated by commas (,). Monthly: You can enter two values ranging from 1 to 31. The format is A-B. B must be greater than or equal to A. After the scheduled task is modified, RecurrenceType, RecurrenceValue, and RecurrenceEndTime must be valid. |
| RecurrenceEndTime | String | No | The end time of the scheduled task to be repeated. UTC time is used and complies with the ISO 8601 standard. The format is YYYY-MM-DDThh:mmZ. You cannot enter a time point later than 90 days from the date of scheduled task creation or modification. After the scheduled task is modified, RecurrenceType, RecurrenceValue, and RecurrenceEndTime must be valid. |

| Parameter | Type | Required | Description |
|---|---|---|---|
| TaskEnabled | Bool | No | Indicates whether to start the scheduled task. true: indicates the task is started. false: indicates the task is stopped. Default value: true. |

Response parameters For more information about response parameters, see Common response parameters. Error code For more information about common error codes, see Client errors or Server errors.

| Error message | Error code | Description | HTTP status code |
|---|---|---|---|
| The error message returned when the specified scheduled task does not exist under this account. | InvalidScheduledTaskId. NotFound | The specified scheduled task does not exist. | 404 |
| The error message returned when the name of the scheduled task already exists. | InvalidScheduledTaskNa me.Duplicate | The specified value of parameter <parameter name> is duplicated. | 400 |
| The error message returned when the specified ScheduledAction parameter and the scheduled task are not in the same region. | ScheduledAction.Region Mismatch | The specified scheduled task and the specified scheduled action are not in the same Region. | 400 |

Examples Sample request s

```
http://ess.example.com/?Action=ModifyScheduledTask &ScheduledTaskId=edRtShc57WGXdt8TlPbr**** &LaunchTime=2014-08-18T10:52Z &RecurrenceEndTime=2014-08-20T16:55Z &<Common request parameter>
```

Response examples XML format

```xml
<ModifyScheduledTaskResponse>
    <RequestId>F9372E8D-C163-471F-BEB4-3A02B3CE176E</RequestId>
</ModifyScheduledTaskResponse>
```

JSON format `{`

```json
    "RequestId": "04F0F334-1335-436C-A1D7-6C044FE73368"
```

`}`

##### 2.1.11.3 DescribeScheduledTasks

You can query information about a scheduled task. You can query information about relevant scheduled tasks by specifying the ScheduledAction parameter. Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeScheduledTasks. |
| RegionId | String | Yes | The ID of the region where a scheduled task is located. |
| ScheduledTaskId.N | String | No | The ID of scheduled task N. N ranges from 1 to 20. The IDs of inactive scheduled tasks are ignored in the query result and no error is reported. |
| ScheduledTaskName.N | String | No | The display name of scheduled task N. N ranges from 1 to 20. The names of inactive scheduled tasks are ignored in the query result and no error is reported. |
| ScheduledAction.N | String | No | The operation performed when scheduled task N is triggered. N ranges from 1 to 20. Inactive operations are ignored in the query result and no error is reported. |
| PageNumber | Integer | No | The page number of the scheduled task list. The initial value and default value are both 1. |

| Parameter | Type | Required | Description |
|---|---|---|---|
| PageSize | Integer | No | The number of lines per page in paged query. Maximum value: 50. Default value: 10. |

Response parameters

| Parameter | Type | Description |
|---|---|---|
| TotalCount | Integer | The total number of scheduled tasks. |
| PageNumber | Integer | The number of the current page. |
| PageSize | Integer | The number of lines per page. |
| ScheduledTasks | ScheduledTaskSetType | A collection of details about the scheduled tasks you queried. |

ScheduledTaskSetType is a collection of ScheduledTaskItemType.

| Parameter | Type | Description |
|---|---|---|
| ScheduledTask | ScheduledTaskItemType | The details of the scheduled task. |

The following table describes the attributes of ScheduledTaskItemType.

| Parameter | Type | Description |
|---|---|---|
| ScheduledTaskId | String | The ID of the scheduled task. |
| ScheduledTaskName | String | The name of the scheduled task. |
| Description | String | The description of the scheduled task. |
| ScheduledAction | String | The operation performed when a scheduled task is triggered. |
| LaunchTime | String | The time at which the scheduled task is triggered. |
| LaunchExpirationTime | Integer | You can retry the task during this time period after the scheduled task fails. |
| RecurrenceType | String | The type of the scheduled task to be repeated. |
| RecurrenceValue | String | The recurring value of the scheduled task to be repeated. |
| RecurrenceEndTime | String | The end of the task recurrence period. |
| TaskEnabled | Bool | Indicates whether to enable a scheduled task. |

For more information about common error codes, see Client errors or Server errors. Examples Sample request s

```
http://ess.example.com/?Action=DescribeScheduledTasks &RegionId=cn-qingdao &ScheduledTaskId. 1=edRtShc57WGXdt8TlPbr**** &PageSize=50 &<Common request parameter>
```

Response examples XML format

```xml
<DescribeScheduledTasksResponse>
    <RequestId>B9B498DA-E836-45FF-83C7-1930492FDD5A</RequestId>
    <TotalCount>1</TotalCount>
    <PageNumber>1</PageNumber>
    <PageSize>50</PageSize>
    <ScheduledTasks>
        <ScheduledTask>
            <Description/>
            <LaunchExpirationTime>600</LaunchExpirationTime>
            <LaunchTime>2014-08-18T10:52Z</LaunchTime>
            <RecurrenceEndTime>2014-08-20T16:55Z</RecurrenceEndTime>
            <RecurrenceType>Daily</RecurrenceType>
            <RecurrenceValue>1</RecurrenceValue>
            <ScheduledAction>ari:acs:ess:cn-qingdao:1344371:scalingrule/cCBpdYdQuBe2cUxOdu6
****</ScheduledAction>
            <ScheduledTaskId>edRtShc57WGXdt8TlPbr****</ScheduledTaskId>
            <ScheduledTaskName>edRtShc57WGXdt8TlPbr****</ScheduledTaskName>
            <TaskEnabled>true</TaskEnabled>
        </ScheduledTask>
    </ScheduledTasks>
</DescribeScheduledTasksResponse>
```

JSON format `{`

```json
  "RequestId": "43434132-91C4-4264-8343-681130760A5C",
  "TotalCount": 1,
  "PageSize": 1,
  "PageNumber": 1,
  "ScheduledTasks": {
    "ScheduledTask": [
```

`{`

```json
        "TaskEnabled": true,
        "ScheduledTaskId": "b27CLSc8T478c2iqHr6****",
        "Description": "This is a scheduled task test.",
        "ScheduledTaskName": "9906a33f-14eb-42b8-8bdb-ee8cdf91****",
        "LaunchExpirationTime": 120,
        "RecurrenceType": "Daily",
        "RecurrenceEndTime": "2014-08-13T19:19Z",
        "LaunchTime": "2014-08-12T17:55Z",
        "RecurrenceValue": "1",
        "ScheduledAction": "ari:acs:ess:cn-qingdao:1344371:scalingrule/qGx9feK1giadmp3XKer*
***"
```

`}` `]` `}` `}`

##### 2.1.11.4 DeleteScheduledTask

You can call this operation to delete the specified scheduled task. Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DeleteScheduledTask. |
| ScheduledTaskId | String | Yes | The ID of the scheduled task. |

Response parameters For more information about response parameters, see Common response parameters. Error code For more information about common error codes, see Client errors or Server errors.

| Error message | Error code | Description | HTTP status code |
|---|---|---|---|
| The error message returned when the specified scheduled task does not exist under this account. | InvalidScheduledTaskId. NotFound | The specified scheduled task does not exist. | 404 |

Examples Sample request s

```
http://ess.example.com/?Action=DeleteScheduledTask &ScheduledTaskId=edRtShc57WGXdt8TlPbr**** &<Common request parameter>
```

Response examples XML format

```xml
<DeleteScheduledTaskResponse>
    <RequestId>7683D637-CF8A-41DC-85A8-E128061E65FC</RequestId>
</DeleteScheduledTaskResponse>
```

JSON format `{`

```json
    "RequestId": "04F0F334-1335-436C-A1D7-6C044FE73368"
```

`}`

#### 2.1.12 Error codes

##### 2.1.12.1 Client errors

Client error description

| Description | Error code | Error message | HTTP status code |
|---|---|---|---|
| The error message returned because a required parameter is not specified. | MissingParameter | The input parameter <parameter name> that is mandatory for processing this request is not supplied. | 400 |
| The error message returned because the specified parameter value is invalid. | InvalidParameter | The specified value of parameter <parameter name> is not valid. | 400 |

| Description | Error code | Error message | HTTP status code |
|---|---|---|---|
| The error message returned because the specified operation is invalid. | UnsupportedOperation | The specified action is not supported. | 400 |
| The error message returned because the specified version is invalid. | NoSuchVersion | The specified version does not exist. | 400 |
| The error message returned because the specified operation is denied by the throttling system. | Throttling | Request was denied due to request throttling. | 400 |
| The error message returned because the specified AccessKey pair is invalid. | InvalidAccessKeyId.NotF ound | The Access Key ID provided does not exist in our records. | 400 |
| The error message returned because the specified operation is forbidden. | Forbidden | Users are not authorized to operate on the specified resource. | 403 |
| The error message returned because the specified operation is denied by the risk control system. | Forbidden.RiskControl | This operation is forbidden by Aliyun Risk Control system. | 403 |
| The error message returned because the specified signature is invalid. | SignatureDoesNotMatch | The signature we calculated does not match the one you provided. | 403 |
| The error message returned because you are not authorized to call ESS API operations. | Forbidden.Unsubscribed | Do not have permission to access this API. | 403 |
| The error message returned because the real-name verification is not completed. | Forbidden.UserVerificati on | Your user account is not verified by Aliyun. | 403 |
| The error message returned because the specified region does not support ESS. | ResourceNotAvailable | Resource you requested is not available in this region or zone. | 400 |

##### 2.1.12.2 Server errors

Server error description

| Description | Error code | Error message | HTTPstatus code |
|---|---|---|---|
| The error message returned because the server fails to process this request. | InternalError | The request processing has failed due to some unknown error, exception or failure. | 500 |
| The error message returned because the server fails to process this request. | ServiceUnavailable | The request has failed due to a temporary failure of the server. | 503 |

#### 2.1.13 Ensure idempotence

If a request times out or an internal server error occurs when the ExecuteScalingRule operation is called to create or release ECS instances, the client may try to resend the request. In this case, the client provides the ClientToken parameter to prevent the server from creating or releasing more instances than intended. The ClientToken parameter also ensures that requests are idempotent. ClientToken is a unique and case-sensitive string that is generated by the client. The token can only contain ASCII characters and cannot exceed 64 characters in length. If the same ClientToken value is used to call the CreateInstance operation, the server will return identical request results with the same ScalingActivityId values. Therefore, when the request is resent due to an error, the same ClientToken value can ensure that only one scaling activity is created and the corresponding ScalingActivityId value is obtained. If the provided ClientToken has already been used but with different request parameters, ESS will return the `IdempotentParameterMismatch` error code.

> **Note:** You must specify the SignatureNonce, Timestamp, and Signature parameters again before the request is resent because ESS uses SignatureNonce to prevent replay attacks and Timestamp to mark the time of each request. Therefore, you must provide different SignatureNonce and Timestamp values. This also produces a different Signature value. Typically, you only need to configure the client to resend a request in the case of Error 503 (ServiceUnAvailable) or no response. If Error 200 is returned, a retry can obtain the same result as that of the previous request, but the server status is not affected. If Error 4xx or 500 is returned, the request cannot be retried unless the error message states T ry it lat er.
