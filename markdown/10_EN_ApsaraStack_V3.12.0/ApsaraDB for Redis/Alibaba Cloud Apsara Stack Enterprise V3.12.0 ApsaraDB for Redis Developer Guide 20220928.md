---
title: "Alibaba Cloud Apsara Stack Enterprise V3.12.0 ApsaraDB for Redis Developer Guide 20220928"
product_version: "V3.12.0"
doc_version: "20220928"
pdf_pages: 81
source_pdf: "Alibaba Cloud Apsara Stack Enterprise V3.12.0 ApsaraDB for Redis Developer Guide 20220928.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/01_ApsaraStackEnterprise/V3.12/%E6%95%B0%E6%8D%AE%E5%BA%93/Alibaba%20Cloud%20Apsara%20Stack%20Enterprise%20V3.12.0%20ApsaraDB%20for%20Redis%20Developer%20Guide%2020220928.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes)
---

# Alibaba Cloud Apsara Stack Enterprise V3.12.0 ApsaraDB for Redis Developer Guide 20220928

## Table of Contents

- 1 Call Apsara Stack SDK by using ASAPI
  - 1.1 Overview
  - 1.2 Log on to the API Tool console
  - 1.3 View the information about API operations
  - 1.4 Obtain the endpoint of ASAPI
  - 1.5 Obtain the core package for ASAPI
  - 1.6 Obtain an AccessKey pair
  - 1.7 Query the region ID
  - 1.8 SDK for Java
  - 1.9 SDK for Node.js
  - 1.10 Use the POP SDK to call ASAPI
- 2 API reference
  - 2.1 API overview
  - 2.2 Request syntax
  - 2.3 Common parameters
  - 2.4 Responses
  - 2.5 Request signatures
  - 2.6 RAM-based authorization
    - 2.6.1 Grant resource permissions to a RAM user
    - 2.6.2 Authorized resource types in RAM
    - 2.6.3 Operation permissions granted to a RAM user
    - 2.6.4 API authentication rules
  - 2.7 Manage the lifecycle
    - 2.7.1 CreateInstance
    - 2.7.2 DeleteInstance
    - 2.7.3 ModifyInstanceSpec
  - 2.8 Manage instances
    - 2.8.1 DescribeInstanceAttribute
    - 2.8.2 DescribeInstances
    - 2.8.3 DescribeRegions
    - 2.8.4 DescribeSecurityIps
    - 2.8.5 FlushInstance
    - 2.8.6 ModifyInstanceAttribute
    - 2.8.7 ModifyInstanceMaintainTime
    - 2.8.8 ModifyInstanceNetExpireTime
    - 2.8.9 ModifySecurityIps
    - 2.8.10 SwitchNetwork
  - 2.9 Backup and recovery
    - 2.9.1 CreateBackup
    - 2.9.2 ModifyBackupPolicy
    - 2.9.3 DescribeBackupPolicy
    - 2.9.4 DescribeBackups
    - 2.9.5 RestoreInstance
  - 2.10 Manage monitoring
    - 2.10.1 DescribeMonitorItems
    - 2.10.2 DescribeHistoryMonitorValues
  - 2.11 Manage parameters
    - 2.11.1 DescribeInstanceConfig
    - 2.11.2 ModifyInstanceConfig
  - 2.12 Appendixes
    - 2.12.1 Instance types
    - 2.12.2 Error codes
    - 2.12.3 Instance configurations

SDK by using ASAPI

## 1 Call Apsara Stack SDK by using ASAPI

using ASAPI

### 1.1 Overview

This topic describes the architecture and features of Apsara Stack API (ASAPI). ASAPI is a platform that integrates all features and is the only portal to connect to Apsara Stack. ASAPI can categorize, audit, and manage API operations. It can also assemble and customize existing operations and adapt to your operations. Each cloud service can call ASAPI for required data and features, which avoids inconsistent operations caused by different calling methods and separate encapsulation. This can ensure the operation program integrity and improve development efficiency and code portability. SDK by using ASAPI ASAPI allows you to manage and call operations in a centralized manner and customize development. ASAPI supports access to most cloud services deployed in Apsara Stack and supports passthrough or encapsulation of different backend APIs. This way, operations can be called using the same method. ASAPI allows you to use SDKs and API portals to call APIs registered on ASAPI, customize SDKs, and manage versions of Apsara Stack, services, and APIs.

### 1.2 Log on to the API Tool console

You can log on to the API Tool console through the Apsara Stack Cloud Management (ASCM) console. Prerequisites Before you log on to the Apsara Uni-manager Management Console, the endpoint of the console is obtained from the deployment staff. We recommend that you use Google Chrome. Procedure
1. Enter the URL of the Apsara Uni-manager Management Console in the address bar and press the
Enter key.
2. Enter your username and password.
Obtain the username and password that you use to log on to the Apsara Uni-manager Management Console from the operations administrator. Not e The first time that you log on to the Apsara Uni-manager Management Console, you must change the password of your account. For security purposes, your password must meet the minimum complexity requirements. The password must be 10 to 32 characters in length and must contain at least two of the following character types: Uppercase or lowercase letters Digits Special characters, including exclamation points (!), at signs (@), number signs (#), dollar signs ($), and percent signs (%)
3. Click Log On.
4. In the top navigation bar, choose Product s > Ot hers > API T ool.

### 1.3 View the information about API operations

operations You must obtain a service name, API operation name, and API version. All the information is required when you use SDKs. Procedure
1. Log on to the API Tool console.
2. In the left-side navigation pane, click API f old.
3. On the API Direct ory page, select the target service from the drop-down list, enter the API
SDK by using ASAPI operation name in the search box, and then click the search icon.
4. View and remember the service name, API operation name, and API version.

### 1.4 Obtain the endpoint of ASAPI

You can obtain the endpoint of Apsara Stack API (ASAPI) in the Apsara Stack Operations (ASO) console. Procedure
1. In the address bar, enter the URL region-id.aso.intranet-domain-id.com and press the Enter key.
Not e You can select a language from the drop-down list in the upper-right corner of the page.
2. Enter your username and password.
Not e Obtain the username and password for logging on to the ASO console from the deployment personnel or an administrator. When you log on to the ASO console for the first time, you must change the password of your username as prompted. To enhance security, a password must meet the following requirements: It must contain uppercase and lowercase letters. It must contain digits. SDK by using ASAPI It must contain special characters such as exclamation points (!), at signs (@), number signs (#), dollar signs ($), and percent signs (%). It must be 10 to 20 characters in length.
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
of the Apsara ASAPI Management platform. SDK by using ASAPI

### 1.5 Obtain the core package for ASAPI

ASAPI Apsara Stack uses Apsara Stack API (ASAPI) as a unified portal for all Apsara Stack products that are connected to ASAPI. ASAPI also provides SDKs to call product APIs. For more information about how to obtain the core package for ASAPI, see Apsara Stack documentation.

### 1.6 Obtain an AccessKey pair

An AccessKey pair consists of an AccessKey ID and an AccessKey secret. The AccessKey pair is used to implement symmetric encryption to verify the identity of the requester. The AccessKey ID is used to identify a user. The AccessKey secret is used to encrypt the signature string. This topic describes how to obtain the AccessKey pair of an organization. Prerequisites Only operations administrators and level-1 organization administrators can obtain the AccessKey pair of an organization. Obtain the AccessKey pair of an organization To obtain the AccessKey pair of an organization, perform the following operations:
1. Log on to the Apsara Stack Cloud Management (ASCM) console as an administrator.
2. In the top navigation bar, click Ent erprise.
3. In the left-side navigation pane of the Ent erprise page, click Organizat ions.
4. In the Organizations navigation tree, click the
icon on the right of the organization to be added.
5. Select AccessKey.
6. In the message that appears, view the AccessKey pair of the organization.
SDK by using ASAPI Not e An AccessKey pair is automatically allocated to a level-1 organization. Subordinate organizations use the same AccessKey pair as their level-1 organization. Obtain the AccessKey pair of a personal account To obtain the AccessKey pair of a personal account, perform the following operations:
1. Log on to the ASCM console as an administrator.
2. In the upper-right corner of the homepage, move the pointer over the profile picture and click User
Inf ormat ion.
3. In the Apsara St ack AccessKey Pair section of the User Information page, view your AccessKey
pair. Not e The AccessKey pair consists of an AccessKey ID and an AccessKey secret. They allow you to access Apsara Stack resources with full permissions for your account. You must keep them confidential.

### 1.7 Query the region ID

You must specify the region ID when you call Apsara Stack SDK for Node.js. You must query the region ID in the Apsara Stack Cloud Management (ASCM) console. Procedure
1. Log on to the ASCM console as an administrator.
2. In the upper-right corner of the homepage, move the pointer over the profile picture and click User
Inf ormat ion.
3. In the Apsara St ack AccessKey Pair section, you can view the region ID.

### 1.8 SDK for Java

This topic describes how to obtain and use Apsara Stack SDK for Java. Preparations You must have an authorized account and an AccessKey pair (AccessKey ID and AccessKey secret) to use the Apsara Stack SDK for Java. For more information about how to obtain and view your AccessKey pair in the ASCM console, see Obtain an AccessKey pair. You have obtained the endpoint of Apsara Stack API (ASAPI). For more information, see Obtain the endpoint of Asapi. SDK by using ASAPI The version of Apsara Stack SDK for Java is JDK 1.6 or later. Add the dependency Add the dependency to pom.xml:

```xml
<dependency>
    <groupId>com.aliyun</groupId>
    <artifactId>asapi</artifactId>
    <version>0.0.1-SNAPSHOT</version>
    <scope>system</scope>
    <systemPath>${project.basedir}/lib/aliyun-java-sdk-asapi.jar</systemPath>
</dependency>
```

Use Apsara Stack SDK for Java You can call API operations on ASAPI by using GET and POST requests. GET requests

```
 ASClient client = new ASClient();
// Method 1 String result = client.doGet(endpoint, parameters); // Method 2 String result = client.doRequest(endpoint, parameters);
```

POST requests SDK by using ASAPI

```
// Obtain the endpoint of ASAPI. String endpoint = "http://xxx/asapi/v3"; // Set request parameters. Map<String, String> parameters = new HashMap<String, String>(); // Set product parameters. parameters.put("Product", "ascm"); // The product name. It must be the same as that displayed on the APIs page. parameters.put("Action", "AddUser"); // The API operation. It is case-sensitive and must be the same as that on the APIs page. parameters.put("Version", "2019-05-10"); // The API version. // Set authorization parameters. parameters.put("AccessKeyId", "<your-access-key-id>"); // The AccessKey ID of th e authorized account. parameters.put("AccessKeySecret", "<your-access-key-secret>"); // The AccessKey secret o f the authorized account. // Set business parameters. parameters.put("username", "<your-username>"); // The username that is u sed to log on to the ASCM console. parameters.put("password", "<your-password>"); // The password that is u sed to log on to the ASCM console. JSONObject jsonObject = new JSONObject(); jsonObject.put("param1", "json parameter 1"); jsonObject.put("param2", "json parameter 2"); parameters.put("json", jsonObject.toJSONString()); // Create a client to initiate requests. ASClient client = new ASClient(); // Add the request header. client.addHeader("x-acs-resourceGroupId", "112233"); // Initiate the request and obtain the response. String result = client.doPost(endpoint, parameters);
```

### 1.9 SDK for Node.js

This topic describes how to obtain and use Apsara Stack SDK for Node.js. Preparations You must have an authorized account and an AccessKey pair (AccessKey ID and AccessKey secret) to use the Apsara Stack SDK for Node.js. For more information, see Obtain an AccessKey pair. You have obtained the endpoint of ASAPI. For more information, see Generate the endpoint of ASAPI. You have obtained the region ID. For more information, see Query the region ID. Add the dependency
1. Install Apsara Stack SDK for Node.js.

```
 tnpm install --save @ali/asapi-nodejs-sdk
```

2. If mocha.opts is based on eggjs, you must configure mocha.opts.
SDK by using ASAPI

```
--recursive --colors --timeout 60000 --reporter mochawesome --require co-mocha --require egg-ts-helper/register --require espower-typescript/guess --require intelli-espower-loader
```

Use SDK for Node.js The following example shows how to use Apsara Stack SDK for Node.js:
1. Create a client instance. To create a client instance, you must set the region ID, endpoint,
AccessKey ID, and AccessKey secret in the config.ts file. Example:

```
local: {
    regionId: 'the region ID',
    API_GATEWAY: 'the endpoint',
    accessKeyId: 'your AccessKey ID',
    accessKeySecret: 'your AccessKey secret',
```

`},`
2. Create an API request and configure parameters.
3. Initiate the request and handle responses or exceptions.

```
// Specify the ASAPI endpoint. const API_GATEWAY = "http://xxxx/asapi/v3" // Create an rpc client. const asapiClient = ctx.service.sdk.rpcClient; // Set request parameters. let params = {
    Action: 'TestAPI',
    Product: 'test',
    regionId: 'cn-qingdao-env12-d01',
    accessKeyId: 'xxxxxxx',
    accessKeySecret: 'xxxxxxx',
    Version: '2018-01-22',
```

};

```
// Set parameters in the request header. asapiClient.addHeader("x-acs-regionId", "cn-hangzhou"); // Initiate the request and obtain the response. const result = await asapiClient.doRequest(API_GATEWAY, params, {});
```

### 1.10 Use the POP SDK to call ASAPI

If an application used the POP SDK to call cloud services, you must switch the gateway to ASAPI by performing the following operations: Procedure Reference the following sample code and add required common parameters and the Product Name field to the request header. Use the code to switch the gateway to ASAPI. SDK by using ASAPI Not e Different services use different endpoints in the POP SDK. However, ASAPI provides only one endpoint. You cannot identify the service to which an API operation belongs based on the API operation name and the version number. For example, both ECS and KVStore for Redis provide the DescribeInstances API operation of the 2015-01-01 version. Sample code The following sample code shows how to use POP SDK to call ECS ASAPI.

```java
 try {
            DefaultProfile clientProfile = DefaultProfile.getProfile(regionId, accessKeyId,
accessKeySecret);
            // Set the ASAPI gateway. Format: server.asapi.${intranet-domain}.
            clientProfile.addEndpoint(region, region, "ecs", "<ASAPI gateway>");
            DefaultAcsClient acsClient = new DefaultAcsClient(clientProfile);
            DescribeImagesRequest request = new DescribeImagesRequest();
            request.setSysRegionId(regionId); // Or setRegionId(regionId)
            // Set common parameters based on the information about the current user.
            rrequest.putHeaderParameter("x-acs-organizationid", "<Organization ID>");
            request.putHeaderParameter("x-acs-resourcegroupid", "<Resource group ID>");
            request.putHeaderParameter("x-ascm-product-name", "<Service name>");
            request.putHeaderParameter("x-ascm-product-version", "<API version");
            request.putHeaderParameter("x-ascm-product-ak", "<AccessKey ID>");
            request.putHeaderParameter("x-ascm-product-sk", "<AccessKey Secret>");
            DescribeImagesResponse result = (DescribeImagesResponse) acsClient.getAcsRespon
se(request);
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

`}` Header parameters

| Parameter | Description |
|---|---|
| x-ascm-product -name | The name of the service to which the API operation belongs. |
| x-ascm-product -version | The API version. |
| x-ascm-product -ak | The AccessKey ID of the organization in the ASCM console. |
| x-ascm-product -sk | The AccessKey secret of the organization in the ASCM console. |

## 2 API reference

### 2.1 API overview

Instance lifecycle management API operations

| Operation | Description |
|---|---|
| CreateInstance | Creates an instance. |
| DeleteInstance | Releases an instance. |
| ModifyInstanceSpec | Changes the specifications of a specified instance. |

Instance management API operations

| Operation | Description |
|---|---|
| DescribeInstanceAttribute | Queries detailed information about instances. |
| DescribeInstances | Queries basic information about instances. |
| DescribeRegions | Queries available regions. |
| DescribeSecurityIps | Queries the IP whitelist that allows connections to a specified instance from specified IP addresses or CIDR blocks. |
| FlushInstance | Clears an instance. |
| ModifyInstanceAttribute | Sets the attribute for a specified instance. |
| ModifyInstanceMaintainTime | Changes maintenance time for a specified instance. |
| ModifySecurityIps | Changes the whitelist for a specified instance. |
| ModifyInstanceNetExpireTime | Changes the period for retaining a domain name of a specified classic network. |
| SwitchNetwork | Changes the type of a network. |

Backup and recovery API operations

| Operation | Description |
|---|---|
| CreateBackup | Creates a backup. |
| ModifyBackupPolicy | Changes a backup policy. |
| DescribeBackupPolicy | Queries backup policies. |

|   | Developer Guide·API reference | ApsaraDB for Redi | s |
|---|---|---|---|

| Operation | Description |
|---|---|
| DescribeBackups | Queries available backups. |
| RestoreInstance | Restore a specified instance based on a specified backup set. |

Monitoring management API operations

| Operation | Description |
|---|---|
| DescribeMonitorItems | Queries available monitoring metrics. |
| DescribeHistoryMonitorValues | Queries historical monitoring data. |

Parameter management API operations

| Operation | Description |
|---|---|
| DescribeInstanceConfig | Queries parameters of a specified instance. |
| ModifyInstanceConfig | Changes parameters of a specified instance. |

### 2.2 Request syntax

Endpoint The endpoint of KVStore for Redis APIs is `r-kvstore.`example.com. For more information about how to obtain the endpoint, see Generate the endpoint of ASAPI. Not e example.com is a domain name that is customized for a project. You can obtain the domain name from the administrator. Protocol You can send requests over HTTP or HTTPS. To enhance data security, we recommend that you send API requests by using HTTPS. Request method You can send requests by using the HTTP GET method. This method requires that you specify request parameters in the request URL. Request parameters You must specify the Action parameter (such as CreateInstance) for each request. You must also specify common request parameters and specific request parameters that are required by each action. Encoding The request and response are both encoded in UTF-8.

### 2.3 Common parameters

Common request parameters must be included in all API requests. Common request parameters Common request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| Format | String | Yes | The type of the returned value. Valid values: JSON and XML. Default value: XML |
| Version | String | Yes | The version of the API. Specify the version in the YYYY- MM-DD format. The current version is 2015-01-01. |
| AccessKeyId | String | Yes | The AccessKey ID provided by Alibaba Cloud. |
| Signature | String | Yes | The signature string of the current request. For more information about how signatures are calculated, see Request signatures. |
| SignatureMetho d | String | Yes | The encryption method of the signature string. Set the value to HMAC-SHA1. |
| Timestamp | String | Yes | The timestamp of the request. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC. For example, you can set the parameter to 2016-01-01T12:00:00Z. This specifies 20:00:00, January 1, 2016, UTC+08:00. |
| SignatureVersio n | String | Yes | The version of the signature algorithm. The current version is 1.0. |
| SignatureNonce | String | Yes | The unique random number that is used to prevent replay attacks. You must use different random numbers for different requests. |

```
https:// r-kvstore.example.com/ ? Format=json &Version=2015-01-01 &Signature=Pc5xxxxxxxxxxxxxxxxxx &SignatureMethod=HMAC-SHA1 &SignatureNonce=15215528852396 &SignatureVersion=1.0 &AccessKeyId=key-test &Timestamp=2016-01-01T12:00:00Z
```

Common response parameters Each time you call an API operation, the system returns a globally unique ID (RequestId). This is regardless of whether the request is successful.

```xml
<? xml version="1.0" encoding="utf-8"? > <!-The root of the response--> <Operation name+Response> <!—The returned request tag--> <RequestId>4C4fdsf38-3910-447D-87AD-AC078932216</RequestId> <!—The returned result--> </Operation name+Response>
```

### 2.4 Responses

After you call an API operation, KVStore for Redis returns data in the same format. In the response, an HTTP status code in the `2xx` format indicates that the call is successful. An HTTP status code in the `4xx` or `5xx` format indicates that the call failed. The system returns responses for successful calls in XML or JSON format. You can specify the response format in request parameters. The system uses the XML format by default. Not e The response examples in this topic have been formatted with line breaks or indents to provide a clear view. The responses in your actual running environments are not properly formatted as these examples. Sample success response The response in XML format includes a message that indicates whether the call is successful and the specific service data. An example is as follows:

```xml
<? xml version="1.0" encoding="utf-8"? > <!—The root node of the response--> <Operation name+Response> <!—The request ID returned--> <RequestId>4C4fdsf38-3910-447D-87AD-AC078932216</RequestId> <!—The result data returned--> </Operation name+Response>
```

JSON format `{`

```json
"RequestId": "4C4fdsf38-3910-447D-87AD-AC078932216", /* The result data returned */
```

`}` Sample error response When an error occurs during an API call, no result data is returned. You can locate the cause of the error by referencing the attached list of error codes. If an error occurs when you call an operation over HTTP, an HTTP status code in the `4xx` or `5xx` format is returned. The returned message body includes the specific error code and error message. The message body also contains a globally unique request ID called RequestId and a target site ID called HostId. If you cannot locate the cause, request Apsara Stack customer service, and provide the HostId and RequestId for troubleshooting.

```xml
<? xml version="1.0" encoding="UTF-8"? > <Error> <RequestId>8906582E-6722-409A-A6C4-0E7863B733A5</RequestId> <HostId> r-kvstore.example.com</HostId> <Code>UnsupportedOperation</Code> <Message>The specified action is not supported. </Message> </Error>
```

JSON format `{`

```json
"RequestId": "7463B73D-35CC-4D19-A010-6B8D65D242EF", "HostId": " r-kvstore.example.com", "Code": "UnsupportedOperation", "Message": "The specified action is not supported."
```

`}`

### 2.5 Request signatures

KVStore for Redis authenticates each access request. You need to include a signature when you submit an HTTP or HTTPS request. KVStore for Redis authenticates the request sender identity by using symmetric encryption based on an AccessKey pair that consists of an AccessKey ID and an AccessKey secret. An AccessKey ID and an AccessKey secret are issued to you by Alibaba Cloud. You can apply for and manage them on the Alibaba Cloud website. The AccessKey ID is used to verify the identity of the user. The AccessKey secret is used to encrypt and verify the signature string. You must keep your AccessKey secret strictly confidential. For more information about how to obtain the AccessKey pair, see Obtain an AccessKey pair. Sign a request Perform the following steps to sign an API request:
1. Create a canonicalized query string by using request parameters.
i. To construct a canonicalized query string, sort all request parameters by name in alphabetic order. These parameters include common request parameters and customized API request parameters. However, this does not include the Signature parameter. Not e When you use the GET method to submit requests, you specify these parameters in the request URI that follow the question mark (?) and are connected with the ampersand (&). ii. Encode the name and value of each request parameter. Perform URL encoding on the names and values by using the UTF-8 character set. The following section shows the URL encoding rules: Uppercase letters (A-Z), lowercase letters (a-z), numbers (0-9), hyphens (-), underscores (_), periods (.), and tildes (~) are not encoded. Encode other characters in the %XY format, where `XY` specifies the ASCII code of the characters in the hexadecimal format. For example, double quotation marks (") are encoded as %22 . Extended UTF-8 characters are encoded in the %XY%ZA format. Spaces must be encoded as %20 . Do not encode spaces as plus signs (+).

| Not e Libraries that support URL encoding, such as java.net.URLEncoder, follow the Multipurpose Internet Mail Extensions (MIME) encoding rules of application/x-www-form-u rlencoded . If this encoding method is used, replace the plus signs (+) in the encoded strings with %20 , the asterisks (*) with %2A , and %7E with a tilde (~) to conform to the encoding rules. |   |   |
|---|---|---|
|   | application/x-www-form-u |   |

| rlencoded |   |
|---|---|
|   | %20 |

iii. Connect the encoded parameter name and value with an equal sign (=). iv. Sort the key-value pairs connected by equal signs (=) in alphabetical order and separate them with ampersands (&).
2. Create a string-to-sign from the encoded canonicalized query string that is obtained in the
preceding step based on the following rules:

```
 StringToSign=
 HTTPMethod + "&" +
 percentEncode("/") + "&" +
 percentEncode(CanonicalizedQueryString)
```

In this example, `HTTPMethod` specifies the HTTP method that is used to submit the request, such as GET. `percentEncode("/")` is the value ( %2F ) as the result of encoding the slash sign (/) based on the URL encoding rule described in Step 1.b. `percentEncode(CanonicalizedQueryString)` is the string that results from encoding the canonicalized query string described in Step 1 based on the URL encoding rules described in Step 1.b.
3. As defined in RFC 2104, use the preceding signature string to calculate the signature into an HMAC
value. Not e The key that is used for calculating the signature is your AccessKey secret followed by an ampersand (&) (ASCII:38). The SHA1 algorithm is used for the calculation.
4. Encode the HMAC value in Base64 to obtain the signature string.
5. Add the signature string to the request as the Signature parameter.
Not e When you submit the signature string to the KVStore for Redis instance as the final request parameter value, perform URL encoding on this parameter based on RFC 3986 rules. This is the same method that is used to process other parameters. Example DescribeDrdsInstances is used in this example. The following section shows the canonicalized query string:

```
http://r-kvstore.example.com/?Timestamp=2013-06-01T10:33:56Z&Format=XML&AccessKeyId=testid& Action=DescribeInstances&SignatureMethod=HMAC-SHA1&RegionId=region1&SignatureNonce=NwDAxvLU 6tFE0DVb&Version=2015-01-01&SignatureVersion=1.0
```

The following section shows the calculated StringToSign:

```
GET&%2F&AccessKeyId%3Dtestid&Action%3DDescribeInstances&Format%3DXML&RegionId%3Dregion1&Sig natureMethod%3DHMAC-SHA1&SignatureNonce%3DNwDAxvLU6tFE0DVb&SignatureVersion%3D1.0&Timestamp %3D2013-06-01T10%253A33%253A56Z&Version%3D2015-01-01
```

| In this example, if the AccessKey ID is testid used for HMAC calculation is testsecret& . T BIxxxxxxxxxxxxxxxxxxxxxx= . | testid |
|---|---|
| BIxxxxxxxxxxxxxxxxxxxxxx= |   |

In this example, if the AccessKey ID is `testid` and the AccessKey secret is `testsecret` , the key The following section shows the signed request URL that includes the Signature parameter:

```
http://r-kvstore.example.com/?Timestamp=2013-06-01T10%3A33%3A56Z&Format=XML&AccessKeyId=tes tid&Action=DescribeInstances&SignatureMethod=HMAC-SHA1&RegionId=region1&SignatureNonce=NwDA xvLU6tFE0DVb&SignatureVersion=1.0&Version=2015-01-01&Signature=BIPOMlxxxxxxxxxxxxxxxxxxu8LX BeZtLQkJTw6iFvw1E%3D
```

### 2.6 RAM-based authorization

#### 2.6.1 Grant resource permissions to a RAM user

The instances that you create by using your Alibaba Cloud account are the resources owned by the account. An account has the full operation permissions on the resources under this account by default. Alibaba Cloud Resource Access Management (RAM) allows you to grant the access and management permissions on resources under a cloud account to RAM users. Not e Ignore this topic if you do not use Resource Access Management (RAM).

#### 2.6.2 Authorized resource types in RAM

KVStore for Redis only supports RAM authorization for Redis instances. The following table lists the description of resources when you use RAM to authorize access permissions to these resources.

| Resource | Resource description in authorization policy |
|---|---|
| Instance | acs:kvstore:$regionid:$accountid:instance/$instanc eid acs:kvstore:$regionid:$accountid:instance/ acs:kvstore:::instance/ |

All $regionids must be the ID of a region or an asterisk ( `*` ). All $instanceids must be the ID of an instance or an asterisk ( `*` ). Similarly, $account-id is the numerical ID of your Apsara Stack tenant account, which can be replaced by an asterisk ( `*` ).

#### 2.6.3 Operation permissions granted to a RAM user

user You are authorized to call the following API operations to manage the specified resource as a Resource Access Management (RAM) user: RenewInstance RenewMultiInstance TransformToPrePaid

#### 2.6.4 API authentication rules

When you use API operations to access resources as a Resource Access Management (RAM) user, the system queries the RAM service and checks whether the RAM user is granted the required permissions. Each API operation determines the resources for permission check according to the involved resources and the semantics of the API operation. The following table lists the authentication rules corresponding to different API operations. Authentication rules

| Operation | Authentication rule |
|---|---|
| CreateDBInstance | acs:kvstore:$regionid:$accountid:instance/$instanc eid |
| DeleteInstance | acs:kvstore:$regionid:$accountid:instance/$instanc eid |
| ModifyInstanceSpec | acs:kvstore:$regionid:$accountid:instance/$instanc eid |
| RenewInstance | acs:kvstore:$regionid:$accountid:instance/$instanc eid |
| RenewMultiInstance | acs:kvstore:$regionid:$accountid:instance/$instanc eid |
| TransformToPrePaid | acs:kvstore:$regionid:$accountid:instance/$instanc eid |
| ModifyInstanceAttribute | acs:kvstore:$regionid:$accountid:instance/$instanc eid |
| FlushInstance | acs:kvstore:$regionid:$accountid:instance/$instanc eid |
| DescribeInstances | acs:kvstore:$regionid:$accountid:instance/$instanc eid |
| DescribeInstanceAttribute | acs:kvstore:$regionid:$accountid:instance/$instanc eid |
| ModifyInstanceMaintainTime | acs:kvstore:$regionid:$accountid:instance/$instanc eid |
| ModifySecurityIps | acs:kvstore:$regionid:$accountid:instance/$instanc eid |
| SwitchNetwork | acs:kvstore:$regionid:$accountid:instance/$instanc eid |
| ModifyInstanceNetExpireTime | acs:kvstore:$regionid:$accountid:instance/$instanc eid |
| CreateBackup | acs:kvstore:$regionid:$accountid:instance/$instanc eid |
| ModifyBackupPolicy | acs:kvstore:$regionid:$accountid:instance/$instanc eid |

| eveloper Guide·API reference | ApsaraDB for Redi |
|---|---|
| Operation | Authentication rule |
| DescribeBackupPolicy | acs:kvstore:$regionid:$accountid:instance/$instanc eid |
| DescribeBackups | acs:kvstore:$regionid:$accountid:instance/$instanc eid |
| RestoreInstance | acs:kvstore:$regionid:$accountid:instance/$instanc eid |
| DescribeHistoryMonitorValues | acs:kvstore:$regionid:$accountid:instance/$instanc eid |
| DescribeInstanceConfig | acs:kvstore:$regionid:$accountid:instance/$instanc eid |
| ModifyInstanceConfig | acs:kvstore:$regionid:$accountid:instance/$instanc eid |

### 2.7 Manage the lifecycle

#### 2.7.1 CreateInstance

You can call this operation to create an instance. For more information, see Instance specifications. Request parameters Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| <Common request parameters> | - | Yes | For more information, see Common parameters. |
| Action | String | Yes | The operation that you want to perform. Set this parameter to CreateInstance. |

| Parameter | Type |   |   | Required |   | Description |   |   |   |   |
|---|---|---|---|---|---|---|---|---|---|---|
| InstanceName | String |   |   | No |   | The name of the instance. The name must be 2 to 128 characters in length and must start with a letter. The name cannot contain special characters or spaces. Special characters include @ / : = ” < > { } [ ] |   |   |   |   |
| Password | String |   |   | No |   | The password of the instance. The password must be a string of 8 to 30 characters in length and must contain uppercase letters, lowercase letters, and digits. Not e Special characters are not supported, such as ! < > ( ) [ |   |   |   |   |
|   |   |   |   |   |   |   | Not e Special characters are not supported, such as ! < > ( ) [ |   |   |   |
|   |   |   |   |   |   |   |   | ! < > ( ) [ |   |   |
|   |   |   |   |   |   |   | ] { } , ` ~ . - |   |   |   |
|   |   |   |   |   |   |   | @ # $ % ^ & * _ |   |   |   |
| InstanceClass | String |   |   | Yes |   | The type of the requested KVStore for Redis instance. For more information, see Instance specifications. |   |   |   |   |
| RegionId | String |   |   | Yes |   | The region ID of the instance. You can query available data regions by calling the DescribeRegions operation. |   |   |   |   |
| ZoneId | String |   |   | No |   | The zone ID of the instance. You can call DescribeRegions to view available zones. |   |   |   |   |

| Parameter | Type | Required | Description |
|---|---|---|---|
| ChargeType | String | No | The billing method of the instance. Valid values: PrePaid and PostPaid. Default value: PostPaid. |
| Period | Long | No | The billing period of the instance. If you set the ChargeType parameter to PrePaid, you must also specify the Period parameter. Unit: month. Valid values: 1-9, 12, 24, and 36. |
| Token | String | No | The client token that is used to ensure the idempotence of requests. The value of this parameter is generated by the client and must be unique among different requests. The value is case-sensitive and can be up to 64 ASCII characters in length. For more information, see How to ensure idempotence. |
| NetworkType | String | No | The type of the network. Default value: Classic. Valid values: Classic VPC |
| VpcId | String | No | The ID of the VPC to which the instance belongs. |
| VSwitchId | String | No | The ID of the VSwitch. |
| PrivateIp | String | No | The private IP address of the instance. |

| Parameter | Type | Required | Description |
|---|---|---|---|
| SrcDBInstanceId | String | No | If an instance created based on a backup set generated by another instance is valid, specifies the ID of the instance that generates the backup set. |
| BackupId | String | No | If an instance created based on a backup set generated by another instance is valid, specifies the ID of the generated backup set. You can call DescribeBackups to query the value of BackupId. |
| InstanceType | String | No | The category of the instance. Valid values: Redis and Memcache. Default value: Redis. |

Response parameters Response parameters

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> | - | For more information, see Common parameters. |
| InstanceId | String | The ID of the instance, which is globally unique. |
| InstanceName | String | The name of the instance. |

Not e Due to the compatibility with earlier versions, this topic does not describe some returned fields such as Config and Region for the operation. Alibaba Cloud will delete these fields as needed in the future. Sample requests

```
https://r-kvstore.example.com ? <Common request parameters> &Action=CreateInstance &RegionId=cn-hangzhou &Password=Qa123456 &InstanceClass= redis.master.small.default
```

Sample responses `{`

```json
"InstanceId":"73xxxxxxxxxxx", "InstanceName":"73xxxxxxxxxxx"
```

`}`

#### 2.7.2 DeleteInstance

You can call this operation to delete a specified instance. This instance that you want to release must be in the following status: The instance is in the running state. The instance is not locked. Not e You cannot delete a subscription instance until the instance expires. Request parameters Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| <Common request parameters> | - | Yes | For more information, see Common parameters. |
| Action | String | Yes | The operation that you want to perform. Set this parameter to DeleteInstance. |
| InstanceId | String | Yes | The globally unique ID of the specified instance. |

Response parameters Response parameters

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> | - | For more information, see Common parameters. |

Sample request

```
https://r-kvstore.example.com ? <Common request parameters> &Action=DeleteInstance &InstanceId=657xxxxxxxxxxxxx
```

Sample response `{`

```json
"RequestId" : "C2225574-1D93-4F8A-B1D5-39FCBAA40660"
```

`}`

#### 2.7.3 ModifyInstanceSpec

You can call this operation to change the specifications of a specified instance. For more information about instance specifications, see Instance types. Request parameters Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| <Common request parameters> | - | Yes | For more information, see Common parameters. |
| Action | String | Yes | The operation that you want to perform. Set this parameter to ModifyInstanceSpec. |
| InstanceId | String | Yes | The globally unique ID of the specified instance. |
| InstanceClass | String | Yes | The type of the specified instance. For more information, see Instance types. |

Response parameters Response parameters

| Parameter | Type | Description |
|---|---|---|
| <Common request parameters> | - | For more information, see Common parameters. |

| Developer Guide·API reference |   | ApsaraDB for Redi |
|---|---|---|

| Parameter | Type | Description |
|---|---|---|
| OrderId | String | The ID of the order that you have placed. |

Sample request

```
https://r-kvstore.example.com ? <Common request parameters> &Action=ModifyInstanceSpec &InstanceId=736538d0a6894665 &InstanceClass= redis.master.mid.default
```

Sample response `{`

```json
"OrderId" : "201294900260011" "RequestId" : "283746AF-82B3-4BFF-88CC-BF34CDE2732"
```

`}`

### 2.8 Manage instances

#### 2.8.1 DescribeInstanceAttribute

You can call this operation to query details of a specified instance. Request parameters Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| <Common request parameters> | - | Yes | For more information, see Common requests. |
| Action | String | Yes | The operation that you want to perform. Set this parameter to DescribeInstanceAttribu te. |
| InstanceId | String | Yes | The globally unique ID of the specified instance. |

Response parameters Response parameters

| Parameter | Type | Description |
|---|---|---|
| Instances | List | The array that contains the DBInstanceAttribute values. |

DBInstanceAttribute parameters

| Parameter | Type | Description |
|---|---|---|
| InstanceId | String | The globally unique ID of the instance that was queried. |
| InstanceName | String | The name of the instance that was queried. |
| Capacity | Long | The capacity that you have requested for the instance that was queried, in MB. |
| InstanceClass | String | The type of the instance that was queried. |
| Bandwidth | Long | The bandwidth limit of the instance that was queried, in Mbit/s. |
| Connections | Long | The maximum number of connections to the instance that was queried. |
| ConnectionDomain | String | The domain name of the instance that was queried. This domain name only supports connections over an internal network. |
| Port | Int | The port of the instance that was queried. |
| RegionId | String | The region where the instance that was queried was located. For more information, see DescribeRegions. |
| ZoneId | String | The ID of the zone under the RegionId of the instance that was queried. For more information, see DescribeRegions. |

| Parameter | Type | Description |   |   |
|---|---|---|---|---|
| InstanceStatus | String | The status of the instance that was queried. Possible values: Normal: the instance that was queried was normal. Creating: the instance that was queried was being created. Changing: the instance that was queried was being changed. Inactive: the instance that was queried was disabled. |   |   |
| ChargeType | String | The billing method of the instance that was queried. Possible values: PrePaid and PostPaid. |   |   |
| CreateTime | String | The time when the instance that was queried was created. The time follows the ISO 8601 standard in the YYYY-MM- DDThh:mm:ssZ format. The time is displayed in UTC time format. |   |   |
|   |   |   | YYYY-MM- |   |
| EndTime | String | The time when the subscription instance that was queried was about to expire. The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ssZ format. The time is displayed in UTC time format. |   |   |
| NetworkType | String | The type of the network where the instance that was queried was located. Possible values: CLASSIC or VPC. |   |   |
| VpcId | String | The ID of the VPC where the instance that was queried was located. |   |   |
| VSwitchId | String | The ID of the VSwitch for the instance that was queried. |   |   |
| PrivateIpAddress | String | The private IP address of the instance that was queried. |   |   |

|   | DDThh:mm:ssZ |
|---|---|

| Parameter | Type | Description |
|---|---|---|
| MaintainStartTime | String | The time when maintenance can be started. |
| MaintainEndTime | String | The time when maintenance can be ended. |
| SecurityIPList | String | The IP whitelist for the instance that was queried. |
| AvailabilityValue | String | The availability metrics of the current month for the instance that was queried. |

Not e Due to the compatibility with earlier versions, this topic does not describe some returned fields such as Config and Region for the operation. Alibaba Cloud will delete these fields as needed in the future. In this case, do not rely on the returned fields that this topic has not described when you call this operation. Sample request

```
https://r-kvstore.example.com ? <Common request parameters> &Action=DescribeInstanceAttribute &InstanceId=7xxxxxxxxxxx
```

Sample response `{` `{`

```json
    "Instances" : {
        " DBInstanceAttribute " : [{
                "Bandwidth" : 128,
                "Capacity" : 512,
                "ConnectionDomain" : "de5d88e34d004211.m.cnhzalicm10pub001.r-kvstore.exampl
e.com.com",
                "Connections" : 300,
                "ZoneId" : "cn-qingdao-b",
                "InstanceId" : "dexxxxxxxxxx",
                "InstanceName" : "xxxxxx",
                "InstanceStatus" : "Available",
                 "InstanceClass" : "redis.master.mid.default",
                "Port" : 11211,
                "QPS" : 4500,
                "RegionId" : "cn-qingdao",
                 "ChargType":"PostPaid",
                  "NetworkType":"ClASSSIC"
                "MaintainStartTime": "02:00Z",
                 "MaintainEndTime": "06:00Z",
                 "SecurityIPList":"192.168.0.1",
                  "AvailabilityValue":"100%"
```

`}]` `}`

```json
"RequestId" : "283746AF-82B3-4BFF-88CC-BF34CDE2732"
```

`}`

#### 2.8.2 DescribeInstances

You can call this operation to query one or more instances under a specified account. Request parameters Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| <Common request parameters> | - | - | See Common parameters. |
| Action | String | Yes | The operation that you want to perform. Set this parameter to DescribeInstances. |

| Parameter | Type | Required | Description |
|---|---|---|---|
| InstanceIds | String | No | The globally unique ID of the target instance. This parameter is required when you specify an instance ID. To query multiple instances, separate the identifiers of these instances with commas (,). If the parameter value is left blank, the system queries all instances under the specified account by default. |
| InstanceStatus | String | No | The instance status of the specified instance: Valid values: Normal: the specified instance is normal. Creating: the specified instance is being created. Changing: the specified instance is being changed. Inactive: the specified instance is disabled. |
| ChargeType | String | No | The billing method of the specified instance. Valid values: PrePaid: the subscription billing method. PostPaid: the pay-as- you-go billing method. |
| RegionId | String | Yes | You can call the DescribeRegions operation to query the RegionId value. |

| Parameter | Type | Required | Description |
|---|---|---|---|
| InstanceType | String | No | The type of the engine for the specified instance. Valid values: Memcache: specifies an instance of Memcache type. Redis: specifies an instance of Redis type. |
| PageNumber | Integer | No | The number of the page to return. Pages start from page 1. Default value: 1. |
| PageSize | Integer | No | The number of entries to return on each page. Valid values: 1 to 50. Default value: 10. |
| NetworkType | String | No | The type of the network where the specified instance is located. Valid values: CLASSIC: specifies an instance in a classic network. VPC: specifies an instance in a VPC. |

Response parameters Response parameters

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> | - | For more information, see Common parameters. |
| Instances | List | The array that contains the instances that were queried. |
| TotalCount | Integer | The total number of instances that were queried. |
| PageNumber | Integer | The number of the page returned. |
| PageSize | Integer | The number of entries returned on each page. |

Instance parameters

| Parameter | Type | Description |
|---|---|---|
| InstanceId | String | The globally unique ID of the instance that was queried. |
| InstanceName | String | The name of the instance that was queried. |
| Capacity | Long | The capacity that you have requested for the instance that was queried, in MB. |
| InstanceClass | String | The type of the instance that was queried. |
| Bandwidth | Long | The bandwidth limit of the instance that was queried, in Mbit/s. |
| Connections | Long | The maximum number of connections to the instance that was queried. |
| ConnectionDomain | String | The domain name of the instance that was queried. This domain name only supports connections over an internal network. |
| Port | Int | The port of the instance that was queried. |
| UserName | String | The username of the instance that was queried. |
| RegionId | String | The region where the instance that was queried was located. |
| ZoneId | String | The ID of the zone under the RegionId of the instance that was queried. |

| Parameter | Type | Description |   |   |
|---|---|---|---|---|
| InstanceStatus | String | The status of the instance that was queried. Possible values: Normal: the instance that was queried was normal. Creating: the instance that was queried was being created. Changing: the instance that was queried was being changed. Inactive: the instance that was queried was disabled. Transforming: the instance that was queried was being transformed. BackupRecovering: the instance that was queried was being backed up and restored. MinorVersionUpgrading: the minor version of the instance that was queried was being upgraded. |   |   |
| ChargeType | String | The billing method of the instance that was queried. Possible values: PrePaid and PostPaid. |   |   |
| CreateTime | String | The time when the instance that was queried was created. The time follows the ISO 8601 standard in the YYYY-MM- DDThh:mm:ssZ format. The time is displayed in UTC time format. |   |   |
|   |   |   | YYYY-MM- |   |
| EndTime | String | The time when the subscription instance that was queried was about to expire. The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ssZ format. The time is displayed in UTC time format. |   |   |
| NetworkType | String | The type of the network where the instance that was queried was located. Possible values: CLASSIC or VPC. |   |   |

|   | DDThh:mm:ssZ |
|---|---|

| Parameter | Type | Description |
|---|---|---|
| VpcId | String | The ID of the VPC where the instance that was queried was located. |
| VSwitchId | String | The ID of the VSwitch for the instance that was queried. |
| PrivateIpAddr | String | The private IP address of the instance that was queried. |

Not e Due to the compatibility with earlier versions, this topic does not describe some returned fields such as Config for the operation. Alibaba Cloud will delete these fields as needed in the future. In this case, do not rely on the returned fields that this topic has not described when you call this operation. Sample request

```
https://r-kvstore.example.com ? <Common request parameters> &Action=DescribeInstances &PageNumber=1 &PageSize=10 &InstanceId=dexxxxxxxxxx1
```

Sample response `{`

```json
    "Instances" : {
        "Instance" : [{
                "Bandwidth" : 128,
                "Capacity" : 512,
                "ConnectionDomain" : "de5d88e34d004211.m.cnhzalicm10pub001.r-kvstore.exampl
e.com",
                "Connections" : 300,
                "ZoneId" : "cn-qingdao-b",
                "InstanceId" : "dexxxxxxxxxx1",
                "InstanceName" : "xxxxxx",
                "InstanceStatus" : "Available",
                 "InstanceClass" : "redis.master.mid.default",
                "Port" : 11211,
                "RegionId" : "cn-qingdao",
                "UserName" : "xxxxxxxxxx"
                "NetworkType":"CLASSSIC"
"ChargeType":" PostPaid"
```

`}` `]` `},`

```json
    "PageNumber" : 1,
    "PageSize" : 10,
    "TotalCount" : 1,
    "RequestId" : "969D0A1D-C91A-4837-9F70-49785DF9BDCE"
```

`}`

#### 2.8.3 DescribeRegions

You can call this operation to query regions where you can create instances. Request parameters Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| <Common request parameters> | - | Yes | For more information, see Common parameters. |
| Action | String | Yes | The operation that you want to perform. Set this parameter to DescribeRegions. |

Response parameters Response parameters

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> | - | For more information, see Common parameters. |
| RegionIds | List | The RegionIds parameter is a list. Every element in this list consists of the RegionId and ZoneIds. ZoneIds is a string, and multiple ZoneId values are separated with commas (,). |

Sample request

```
https://r-kvstore.example.com ? <Common request parameters> &Action=DescribeRegions
```

Sample response `{`

```json
    "RequestId":"535A88D3-5408-4B29-AFD4-07319D97EBC4",
    "RegionIds":
```

`{` `{`

```json
                "ZoneIds":"cn-qingdao-b",
                "RegionId":"cn-qingdao",
```

`},` `{`

```json
                "ZoneIds":"cn-shenzhen-a",
                "RegionId":"cn-shenzhen",
```

`},` `{`

```json
                "ZoneIds":"cn-hangzhou-d,cn-hangzhou-b",
                "RegionId":"cn-hangzhou"
```

`},` `{`

```json
                "ZoneIds":"cn-beijing-a",
                "RegionId":"cn-beijing"
```

`}` `}` `}`

#### 2.8.4 DescribeSecurityIps

You can call this operation to query the list of IP addresses or CIDR blocks that you can use to connect to an instance. Request parameters Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| <Common request parameters> | - | Yes | For more information, see Common parameters. |
| Action | String | Yes | The operation that you want to perform. Set this parameter to DescribeSecurityIps. |
| InstanceId | String | Yes | The name of the specified instance. |

Response parameters Response parameters

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> | - | For more information, see Common parameters. |
| SecurityIpGroups | List | The list of whitelisted IP addresses or CIDR blocks for the instance that was queried. |

SecurityIpGroups parameters SecurityIpGroups parameters

| Parameter | Type | Description |
|---|---|---|
| SecurityIpGroupName | String | The name of the IP whitelist that was queried. |

| Parameter | Type | Description |   |
|---|---|---|---|
| SecurityIpList | String | The list of whitelisted IP addresses or CIDR blocks that were queried. A maximum of 1,000 IP addresses or CIDR blocks are displayed. IP addresses or CIDR blocks are separated with commas (,), such as 0.0.0.0/0,10.23.12.24 (IPv4 addresses) or 10.23.12.24/24 (Classless Inter-Domain Routing or CIDR notation). In the CIDR notation, 10.23.12.24 represents the IPv4 address 10.23.12.24. Its subnet mask is 255.255.255.0. The slash (/) and the following number 24 represent 24 leading 1 bits in the subnet mask and its associated routing prefix. The length of the routing prefix ranges from 1 to 32. |   |

Sample request

```
https://r-kvstore.example.com/ ? <Common request parameters> &Action= DescribeSecurityIps &InstanceId=6xxxxxxxxxxxxxx
```

Sample response `{`

```
" SecurityIpGroups " : { " SecurityIpGroup" : [{ " SecurityIpGroupName" : "ipsecuritytest" , " SecurityIpList " : "10.xx.xx. 24"
```

`}` `]` `},`

```json
"RequestId" : "969D0A1D-C91A-4837-9F70-49785DF9BDCE"
```

`}`

#### 2.8.5 FlushInstance

You can call this operation to clear data stored on an instance. The cleared data cannot be restored. This is an asynchronous operation. After you call this operation, the system returns the result immediately. The system clears data in the background. Request parameters Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| <Common request parameters> | - | - | For more information, see Common parameters. |
| Action | String | Yes | The operation that you want to perform. Set this parameter to FlushInstance. |
| InstanceId | String | Yes | The globally unique ID of the specified instance. |

Response parameters Response parameters

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> | - | For more information, see Common parameters. |

Sample request

```
https://r-kvstore.example.com ? <Common request parameters> &Action= FlushInstance &InstanceId=65xxxxxxxx
```

Sample response `{`

```json
"RequestId" : "96893674-E50C-495D-AB0E-2F12C1E0FD45"
```

`}`

#### 2.8.6 ModifyInstanceAttribute

You can call this operation to modify attributes of an instance, such as the name or the password of the instance. Request parameters Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| <Common request parameters> | - | - | For more information, see Common parameters. |
| Action | String | Yes | The operation that you want to perform. Set this parameter to ModifyInstanceAttribute . |
| InstanceId | String | Yes | The globally unique ID of the specified instance. |
| InstanceName | String | No | The instance name that you want to change to. The name must be a string of 2 to 128 characters in length and must start with an uppercase or lowercase letter or Chinese character. Special characters, such as at signs (@), slashes (/), colons (:), equal signs (=), quotation marks ("), angle brackets (<>), braces ({}), brackets ([]), and spaces, are not supported. |

| Parameter | Type | Required | Description |
|---|---|---|---|
| NewPassword | String | No | The password of the specified instance. The password must be a string of 8 to 30 characters in length and must contain uppercase letters, lowercase letters, and numbers. Not e Special characters, such as exclamation points (!), angle brackets (<>), parentheses (()), brackets ([]), braces ({}), commas (,), backticks (`), tildes (~), periods (.), hyphens (-), underscores ( ), at _ signs (@), number signs (#), dollar signs ($), percent signs (%), carets (^), ampersands (&), and asterisks (*), are not supported. |

Response parameters Response parameters

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> | - | For more information, see Common parameters. |

Sample request

```
https://r-kvstore.example.com ? <Common request parameters> &Action= ModifyInstanceAttribute &InstanceId=65xxxxxxxxxx &NewPassword=Qa12345678 &InstanceName=TestInstance
```

Sample response `{`

```json
"RequestId" : "E3B35BEA-9EB0-402C-88CF-C46CCCC1EE59"
```

`}`

#### 2.8.7 ModifyInstanceMaintainTime

You can call this operation to modify maintenance time for an instance. Alibaba Cloud may perform routine maintenance for the instance during the specified maintenance time. Request parameters Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| <Common request parameters> | - | Yes | For more information, see Common parameters. |
| Action | String | Yes | The operation that you want to perform. Set this parameter to ModifyInstanceMaintain Time. |
| InstanceId | String | Yes | The globally unique ID of the specified instance. |
| MaintainStartTime | String | Yes | The start time of the maintenance to be performed. |
| MaintainEndTime | String | Yes | The end time of the maintenance to be performed. |

Response parameters Response parameters

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> | - | For more information, see Common parameters. |

Sample request

```
https://r-kvstore.example.com ? <Common request parameters> &Action=ModifyInstanceMaintainTime &InstanceId=65xxxxxxxxx & MaintainStartTime=02:00Z & MaintainEndTime=06:00Z
```

Sample response `{`

```json
"RequestId" : "A099747A-0826-499D-9422-381C07337F73"
```

`}`

#### 2.8.8 ModifyInstanceNetExpireTime

You can call this operation to prolong the maximum period where the IP address in a classic network is retained if you switch an instance from the classic network to a Virtual Private Cloud (VPC) and retain the IP address in the classic network. Request parameters Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| <Common request parameters> | - | Yes | For more information, see Common parameters. |
| Action | String | Yes | The operation that you want to perform. Set this parameter to ModifyInstanceNetExpir eTime. |
| InstanceId | String | Yes | The globally unique ID of the specified instance. |
| ConnectionString | String | Yes | The domain name of the specified classic network. |
| ClassicExpiredDays | String | Yes | The maximum number of days where the IP address in a specified classic network is retained. Valid values: 14, 30, 60, and 120. |

Response parameters Response parameters

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> | - | For more information, see Common parameters. |

Sample request

```
https://r-kvstore.example.com ? <Common request parameters> &Action= ModifyInstanceNetExpireTime &ConectionString= fdafas32323ed.redis.rds.aliyuncs.com &InstanceId=fdxxxxxxxxxx & ClassicExpiredDays=120
```

Sample response `{`

```json
"RequestId" : "AAAF99B1-69ED-4E80-8CD5-272C09E46ACF"
```

`}`

#### 2.8.9 ModifySecurityIps

You can call this operation to set the IP whitelist for an instance, so that only authorized ECS IP addresses or CIDR blocks can be used to connect to the instance. Request parameters Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| <Common request parameters> | - | Yes | For more information, see Common parameters. |
| Action | String | Yes | The operation that you want to perform. Set this parameter to ModifySecurityIps. |
| InstanceId | String | Yes | The globally unique ID of the specified instance. |

| Parameter | Type | Required | Description |
|---|---|---|---|
| SecurityIps | String | Yes | The list of whitelisted IP addresses or CIDR blocks that you want to modify. |
| SecurityIpGroupName | String | Yes | The name of the specified whitelist group. |

Response parameters Response parameters

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> | - | For more information, see Common parameters. |

Sample request

```
https://r-kvstore.example.com ? <Common request parameters> &Action= ModifySecurityIps &InstanceId=65xxxxxxxxxxx &SecurityIps=1.x.x. 1,2.x.x. 2 &SecurityIpGroupName=testgroup
```

Sample response `{`

```json
"RequestId" : "AAAF99B1-69ED-4E80-8CD5-272C09E46ACF"
```

`}`

#### 2.8.10 SwitchNetwork

You can call this operation to switch the network type of an instance. You can switch an instance from a classic network to a Virtual Private Cloud (VPC). Request parameters Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|

| Parameter | Type | Required | Description |
|---|---|---|---|
| <Common request parameters> | - | Yes | For more information, see Common parameters. |
| Action | String | Yes | The operation that you want to perform. Set this parameter to SwitchNetwork. |
| InstanceId | String | Yes | The globally unique ID of the specified instance. |
| TargetNetworkType | String | Yes | The type of the network that you want to switch to. VPC Classic You can only switch from a classic network to a VPC. In this case, set this parameter to VPC. |
| VpcId | String | No | The ID of the VPC that you want to switch to. |
| VSwitchId | String | No | The ID of the VSwitch ID for the VPC that you want to switch to. This parameter is required if you have set VpcId. |
| RetainClassic | String | No | Specifies whether to retain the IP address in the classic network. Valid values: True: the classic network IP address is retained. False: the classic network IP address is not retained. Default value: False. |

| Parameter | Type | Required | Description |
|---|---|---|---|
| ClassicExpiredDays | String | No | The maximum number of days where the IP address in the classic network are retained. Unit: days. Valid values: 14, 30, 60, and 120. This parameter is required if you have set RetainClassic to True. |

Response parameters Response parameters

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> | - | For more information, see Common parameters. |

Sample request

```
https://r-kvstore.example.com ? <Common request parameters> &Action= SwitchNetwork &InstanceId=fdaxxxxxxxxxx & TargetNetworkType=VPC &VpcId=fadsfa &VSwitchId=131ed &RetainClassic=True &ClassicExpiredDays=30
```

Sample response `{`

```json
"RequestId" : "AAAF99B1-69ED-4E80-8CD5-272C09E46ACF"
```

`}`

### 2.9 Backup and recovery

#### 2.9.1 CreateBackup

You can call this operation to create a backup. This is an asynchronous operation. After you call this operation, the system returns the result immediately. The system creates the backup in the background. Request parameters Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| <Common request parameters> | - | Yes | For more information, see Common parameters. |
| Action | String | Yes | The operation that you want to perform. Set this parameter to CreateBackup. |
| InstanceId | String | Yes | The ID of the specified instance. |

Response parameters Response parameters

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> | - | For more information, see Common parameters. |

Sample request

```
https://r-kvstore.example.com ? <Common request parameters> &Action= CreateBackup &InstanceId= de5d8xxxxxxxxxx
```

Sample response `{`

```json
"RequestId" : "5C97648D-C85F-4D58-A71F-7B6750856BF7"
```

`}`

#### 2.9.2 ModifyBackupPolicy

You can call this operation to modify a backup policy. Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| <Common request parameters> | - | Yes | For more information, see Common parameters. |
| Action | String | Yes | The operation that you want to perform. Set the value to ModifyBackupPolicy. |
| InstanceId | String | Yes | The ID of the instance to which the backup file belongs. |
| PreferredBackupTime | String | Yes | The period of time to execute backup. Specify the time in the HH:mmZ-HH:mmZ format. |
| PreferredBackupPeriod | String | Yes | The period of data backup. Valid values: Monday Tuesday Wednesday Thursday Friday Saturday Sunday |

Response parameters Response parameters

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> | - | For more information, see Common parameters. |

Sample requests

```
https://r-kvstore.example.com ? <Common request parameters> &Action= ModifyBackupPolicy &InstanceId= de5xxxxxxxxxx &PreferredBackupTime=00:00Z-04:00Z &PreferredBackupPeriod= Saturday
```

Sample responses `{`

```json
"RequestId" : "5C97648D-C85F-4D58-A71F-7B6750856BF7”
```

`}`

#### 2.9.3 DescribeBackupPolicy

You can call this operation to query a backup policy that you have specified. You can query the backup details of an instance, such as the backup cycle and backup time. Request parameters Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| <Common request parameters> | - | Yes | For more information, see Common parameters. |
| Action | String | Yes | The operation that you want to perform. Set this parameter to DescribeBackupPolicy. |
| InstanceId | String | Yes | The ID of the specified instance. |

Response parameters Response parameters

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> | - | For more information, see Common parameters. |
| BackupRetentionPeriod | String | The maximum number of days where backups of the specified instance were retained. |
| PreferredBackupTime | String | The time of the backup for the specified instance in the HH:mmZ-HH:mm Z format. |

| Parameter | Type | Description |
|---|---|---|
| PreferredBackupPeriod | String | The backup cycle for the specified instance. Possible values: Monday Tuesday Wednesday Thursday Friday Saturday Sunday |
| PreferredNextBackupTime | String | The time of the next backup for the specified instance. |

Sample request

```
https://r-kvstore.example.com ? <Common request parameters> &Action= DescribeBackupPolicy &InstanceId= de5d8xxxxxxxxxxxxxx
```

Sample response `{`

```json
"BackupRetentionPeriod":"7" "PreferredBackupTime":"06:00Z-07:00Z" "PreferredNextBackupTime":"2017-10-19T06:16Z" "PreferredBackupPeriod":"Monday,Tuesday,Wednesday,Thursday,Friday,Saturday,Sunday" "RequestId" : "5C97648D-C85F-4D58-A71F-7B6750856BF7"
```

`}`

#### 2.9.4 DescribeBackups

You can call this operation to query the details of a backup file, such as the backup start time, file size, backup mode, and download address. Request parameters Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|

| Parameter | Type | Required | Description |
|---|---|---|---|
| <Common request parameters> | - | Yes | For more information, see Common parameters. |
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeBackups. |
| InstanceId | String | Yes | The ID of the instance to which the backup file belongs. |
| BackupId | String | No | The ID of the backup set. |
| PageSize | String | Yes | The number of entries to return on each page. Valid values: 30, 50, and 100. |
| PageNumber | String | Yes | The number of the page to return. Valid values: any non-zero positive integer. |
| StartTime | String | Yes | The beginning of the time range to query. |
| End time. | String | Yes | The end of the time range to query. |

Response parameters Response parameters

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> | - | For more information, see Common parameters. |
| Backups | List | An array consisting of Backup data. |
| PageNumber | Integer | The number of the returned page. |
| TotalCount | Integer | The total number of backups. |
| PageSize | Integer | The number of entries returned on each page. |

Backup parameter structure Backup parameter structure

| Parameter | Type | Description |
|---|---|---|
| BackupId | String | The ID of the backup set. |
| BackupDBNames | String | The name of the database that is backed up. |
| BackupStatus | String | The status of the backup set. Success Failed |
| BackupStartTime | String | The beginning of the time range where the data was backed up. |
| BackupEndTime | String | The end of the time range where the data was backed up. |
| BackupType | String | The type of the backup. Valid values: FullBackup IncrementalBackup |
| BackupMode | String | The mode of the backup. Valid values: Automated Manual |
| BackupMethod | String | The method of the backup. Valid values: Logical Physical |
| BackupDownloadURL | String | The download URL of the backup file. |
| BackupSize | String | The size of the backup set. |

Sample requests

```
https://r-kvstore.example.com ? <Common request parameters> &Action= DescribeBackups &InstanceId= de5xxxxxxxxxxxxx &PageNumber=1 &PageSize=10 &InstanceId=de5xxxxxxxxxxxxx
```

Sample responses `{` `{`

```json
    " Backups " : {
        "Backup " : [{
           “BackupId":"111111111"，
           "BackupDBNames":"all"，
          "BackupStatus":"Success",
         "BackupType":"FullBackup",
"BackupStartTime":"2017-10-18T10:34:52Z"， "BackupEndTime":"2017-10-18T10:36:06Z"， "BackupMode":"Manual"， "BackupMethod":"Physical"， "BackupDownloadURL":"https://rdsxxx-st-v2.oss-cn-shenzhen.example.com/custins11111111/xxxxx xxxx_data_20171018183408.rdb"， "BackupSize":"1024"
```

`}` `]` `},`

```json
    "PageNumber" : 1,
    "PageSize" : 10,
    "TotalCount" : 1,
"RequestId" : "5C97648D-C85F-4D58-A71F-7111111111117"
```

`}`

#### 2.9.5 RestoreInstance

You can call this operation to restore data to a primary instance based on a backup set. Not e Calling this operation will cause overwriting data on the specified instance with backup data. Proceed with caution. Request parameters Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| <Common request parameters> | - | Yes | For more information, see Common parameters. |
| Action | String | Yes | The operation that you want to perform. Set this parameter to RestoreInstance. |

| Parameter | Type | Required | Description |
|---|---|---|---|
| InstanceId | String | Yes | The ID of the specified instance. |
| BackupId | String | Yes | Backup set ID |

Response parameters Response parameters

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> | - | For more information, see Common parameters. |

Sample request

```
https://r-kvstore.example.com ? <Common request parameters> &Action= RestoreInstance &InstanceId= de5dxxxxxxxxxxxx &BackupId=fdaxxxxxx
```

Sample response `{`

```json
"RequestId" : "AFA391BF-808F-4DA6-80A2-A382108A0945"
```

`}`

### 2.10 Manage monitoring

#### 2.10.1 DescribeMonitorItems

You can call this operation to query available monitoring metrics. The result is returned in the <parameter:unit> format. Request parameters Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| <Common request parameters> | - | Yes | For more information, see Common parameters. |

| psaraDB for Redis |   | De | veloper Guide·API referenc |
|---|---|---|---|

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set this parameter to DescribeMonitorItems. |

Response parameters Response parameters

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> | - | For more information, see Common parameters. |
| MonitorItems | List | The list of monitoring metrics that were queried. |

Sample request

```
https://r-kvstore.example.com ? <Common request parameters> &Action=DescribeMonitorItems
```

Sample response `{`

```json
    "MonitorItems" : {
        "MonitorItem" : [{
                "MonitorKey" : "GetQ",
                "Unit" : "Counts/s"
            }, {
                "MonitorKey" : "Flush",
                "Unit" : "Counts/s"
            }, {
                "MonitorKey" : "UsedMemCache",
                "Unit" : "Bytes"
            }, {
                "MonitorKey" : "ReplaceQ",
                "Unit" : "Counts/s"
```

`}` `]` `},`

```json
    "RequestId" : "B906A893-58A3-4644-AC2D-A2C9B08706C1"
```

`}`

#### 2.10.2 DescribeHistoryMonitorValues

You can call this operation to query historical monitoring data of an instance. Request parameters Request parameters

| Parameter | Type | Required |   | Description |   |   |
|---|---|---|---|---|---|---|
| <Common request parameters> | - | Yes |   | For more information, see Common parameters. |   |   |
| Action | String | Yes |   | The operation that you want to perform. Set this parameter to DescribeHistoryMonitorV alues. |   |   |
| InstanceId | String | Yes |   | The ID of the specified instance. |   |   |
| StartTime | String | Yes |   | The beginning of the time range where the historical monitoring data is queried. Specify the time in the ISO 8601 standard in the YYYY- MM-DDThh:mm:ssZ format. The time must be in UTC time format. |   |   |
|   |   |   |   |   | YYYY- |   |
|   |   |   |   | MM-DDThh:mm:ssZ |   |   |
| EndTime | String | Yes |   | The end of the time range where the historical monitoring data is queried. Specify the time in the ISO 8601 standard in the YYYY- MM-DDThh:mm:ssZ format. The time must be in UTC time format. The value of EndTime must be greater than or equal to that of StartTime. |   |   |
|   |   |   |   |   | YYYY- |   |
|   |   |   |   | MM-DDThh:mm:ssZ |   |   |
| IntervalForHistory | String | Yes |   | The interval for collecting monitoring data. Monitoring samples were collected every N minutes. Valid values: 01m, 05m, 15m, and 60m. |   |   |

| Parameter | Type | Required | Description |
|---|---|---|---|
| MonitorKeys | String | No | The key of the specified metric. You can call the DescribeMonitorItems operation to query the value of this parameter. |

Response parameters Response parameters

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> | - | For more information, see Common parameters. |
| MonitorHistory | String | The monitoring data returned in the JSON format. For more information, see DescribeMonitorItems. Not e To improve the data transmission efficiency, only metrics whose values are not 0 have been returned. All metrics that are not displayed have been set to the default value 0. |

Sample request

```
https://r-kvstore.example.com ? <Common request parameters> &Action= DescribeHistoryMonitorValues &InstanceId= de5xxxxxxxxxxxx &EndTime=2014-11-27T12%3A02%3A00Z &StartTime=2014-11-27T12%3A00%3A00Z &IntervalForHistory=01m
```

Sample response `{`

```json
"MonitorHistory" : "{"2014-11-27T12:00:00Z":{"IsConnectControl":false,"IsFlowControl":false,"ItemCount":1,"Quo taConnection":500,"QuotaFlow":15360,"QuotaMemCache":1073741824,"QuotaQps":9000,"UsedMemCach e":14}, "2014-11-27T12:01:00Z":{"IsConnectControl":false,"IsFlowControl":false,"ItemCount":1,"Quota Connection":500,"QuotaFlow":15360,"QuotaMemCache":1073741824,"QuotaQps":9000,"UsedMemCache" :14}, "2014-11-27T12:02:00Z":{"IsConnectControl":false,"IsFlowControl":false,"ItemCount":1,"Quota Connection":500,"QuotaFlow":15360,"QuotaMemCache":1073741824,"QuotaQps":9000,"UsedMemCache" :14} }", "RequestId" : "5C97648D-C85F-4D58-A71F-7B6750856BF7"
```

`}`

### 2.11 Manage parameters

#### 2.11.1 DescribeInstanceConfig

You can call this operation to query parameters of an instance. Request parameters Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| <Common request parameters> | - | Yes | For more information, see Common parameters. |
| Action | String | Yes | The operation that you want to perform. Set this parameter to DescribeInstanceConfig. |
| InstanceId | String | Yes | The ID of the specified instance. |

Response parameters Response parameters

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> | - | For more information, see Common parameters. |

| Parameter | Type | Description |
|---|---|---|
| Config | String | The parameters of the specified instance that was queried. For more information, see Instance configurations. |

Sample request

```
https://r-kvstore.example.com ? <Common request parameters> &Action= DescribeInstanceConfig &InstanceId= de5dxxxxxxxxxxxx
```

Sample response `{`

```json
"Config":"{"EvictionPolicy":"volatile-lru","hash-max-ziplist-entries":512, "hash-max-ziplist-value":64,"list-max-ziplist-entries":512, "list-max-ziplist-value":64,"set-max-intset-entries":512, "zset-max-ziplist-entries":128,"zset-max-ziplist-value":64}, "RequestId":"59A58517-F8FF-44E5-B90F-F386DB3E4AB8"
```

`}`

#### 2.11.2 ModifyInstanceConfig

You can call this operation to modify a parameter of an instance. Request parameters Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| <Common request parameters> | - | Yes | For more information, see Common parameters. |
| Action | String | Yes | The operation that you want to perform. Set this parameter to ModifyInstanceConfig. |
| InstanceId | String | Yes | The ID of the specified instance. |

| Parameter | Type | Required | Description |
|---|---|---|---|
| Config | String | Yes | The parameter of the specified instance that you want to modify. The value of this parameter must be in the JSON string format. For more information, see Instance configurations. |

Response parameters Response parameters

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> | - | For more information, see Common parameters. |

Sample request

```
https://r-kvstore.example.com ? <Common request parameters> &Action= ModifyInstanceConfig &InstanceId= de5xxxxxxxxxxxx &Config={"hash-max-ziplist-entries":"512"}
```

Sample response `{`

```json
"RequestId":"59A58517-F8FF-44E5-B90F-F386DB3E4AB8"
```

`}`

### 2.12 Appendixes

#### 2.12.1 Instance types

Types of KVStore for Redis instances Standard plan

| Instance type | Service code | Maximum number of connections | Maximum bandwidth (MB) | Processing capability | Description | Zone- disaster recovery deploymen t |
|---|---|---|---|---|---|---|
| 1 GB standard primary/se condary edition for zone- disaster recovery | redis.logic.sha rding.drrediss db1g. 1db. 0rodb. 4proxy.defaul t | 10,000 | 10 | Single-core | Primary/sec ondary instance for zone- disaster recovery | Deployed across two zones in one region |
| 2 GB standard primary/se condary edition for zone- disaster recovery | redis.logic.sha rding.drrediss db2g. 1db. 0rodb. 4proxy.defaul t | 10,000 | 16 | Single-core | Primary/sec ondary instance for zone- disaster recovery | Deployed across two zones in one region |
| 4 GB standard primary/se condary edition for zone- disaster recovery | redis.logic.sha rding.drrediss db4g. 1db. 0rodb. 4proxy.defaul t | 10,000 | 24 | Single-core | Primary/sec ondary instance for zone- disaster recovery | Deployed across two zones in one region |
| 8 GB standard primary/se condary edition for zone- disaster recovery | redis.logic.sha rding.drrediss db8g. 1db. 0rodb. 4proxy.defaul t | 10,000 | 24 | Single-core | Primary/sec ondary instance for zone- disaster recovery | Deployed across two zones in one region |
| 16 GB standard primary/se condary edition for zone- disaster recovery | redis.logic.sha rding.drrediss db16g. 1db. 0rodb. 4proxy.defaul t | 10,000 | 32 | Single-core | Primary/sec ondary instance for zone- disaster recovery | Deployed across two zones in one region |

| Instance type | Service code | Maximum number of connections | Maximum bandwidth (MB) | Processing capability | Description | Zone- disaster recovery deploymen t |
|---|---|---|---|---|---|---|
| 32 GB standard primary/se condary edition for zone- disaster recovery | redis.logic.sha rding.drrediss db32g. 1db. 0rodb. 4proxy.defaul t | 10,000 | 32 | Single-core | Primary/sec ondary instance for zone- disaster recovery | Deployed across two zones in one region |

Premium plan

| Instance type | Service code | Maximum number of connections | Maximum bandwidth (MB) | Processing capability | Description | Zone- disaster recovery deploymen t |
|---|---|---|---|---|---|---|
| 1 GB advanced primary/se condary edition | redis.master.s mall.special2x | 20,000 | 48 | Single-core | Primary/sec ondary instance | Deployed in one zone |
| 2 GB advanced primary/se condary edition | redis.master. mid.special2x | 20,000 | 48 | Single-core | Primary/sec ondary instance | Deployed in one zone |
| 4 GB advanced primary/se condary edition | redis.master.s tand. special2x | 20,000 | 48 | Single-core | Primary/sec ondary instance | Deployed in one zone |
| 8 GB advanced primary/se condary edition | redis.master.l arge.special1x | 20,000 | 48 | Single-core | Primary/sec ondary instance | Deployed in one zone |
| 16 GB advanced primary/se condary edition | redis.master. 2xlarge.specia l1x | 20,000 | 48 | Single-core | Primary/sec ondary instance | Deployed in one zone |

| Instance type | Service code | Maximum number of connections | Maximum bandwidth (MB) | Processing capability | Description | Zone- disaster recovery deploymen t |
|---|---|---|---|---|---|---|
| 32 GB advanced primary/se condary edition | redis.master. 4xlarge. special1x | 20,000 | 48 | Single-core | Primary/sec ondary instance | Deployed in one zone |

Cluster edition

| Instance type | Service code | Maximum number of connection s | Maximum bandwidth (MB) | Processing capability | Description |
|---|---|---|---|---|---|
| 16 GB cluster edition | redis.sharding.small.def ault | 80,000 | 384 | 4-core | High- performance cluster instance |
| 32 GB cluster edition | redis.sharding.mid.defa ult | 80,000 | 384 | 8-core | High- performance cluster instance |
| 64 GB cluster edition | redis.sharding.large.def ault | 80,000 | 384 | 8-core | High- performance cluster instance |
| 128 GB cluster edition | redis.sharding. 2xlarge.default | 160,000 | 768 | 16-core | High- performance cluster instance |
| 256 GB cluster edition | redis.sharding. 4xlarge.default | 160,000 | 768 | 16-core | High- performance cluster instance |

Cluster edition for zone-disaster recovery

| Instance type | Service code | Maximum number of connections | Maximum bandwidth (MB) | Processing capability | Descriptio n |
|---|---|---|---|---|---|
| 16 GB cluster edition for zone- disaster recovery | redis.logic.sharding.drredi smdb16g. 8db. 0rodb. 8proxy.default | 80,000 | 384 | 8-core | Cluster instance for zone- disaster recovery |
| 32 GB cluster edition for zone- disaster recovery | redis.logic.sharding.drredi smdb32g. 8db. 0rodb. 8proxy.default | 80,000 | 384 | 8-core | Cluster instance for zone- disaster recovery |
| 64 GB cluster edition for zone- disaster recovery | redis.logic.sharding.drredi smdb64g. 8db. 0rodb. 8proxy.default | 80,000 | 384 | 8-core | Cluster instance for zone- disaster recovery |
| 128 GB cluster edition for zone- disaster recovery | redis.logic.sharding.drredi smdb128g. 16db. 0rodb. 16proxy.default | 160,000 | 768 | 16-core | Cluster instance for zone- disaster recovery |
| 256 GB cluster edition for zone- disaster recovery | redis.logic.sharding.drredi smdb256g. 16db. 0rodb. 16proxy.default | 160,000 | 768 | 16-core | Cluster instance for zone- disaster recovery |

#### 2.12.2 Error codes

| Description | Error code | Error message | HTTP status code |
|---|---|---|---|
| The error message returned because RAM users are not authorized to call the API operation. | Forbidden.RAM | User not authorized to operate on the specified resource, or this API doesn't support RAM. | 403 |
| The error message returned because the operation is unavailable for RAM users. | Forbedden.NotSupport RAM | This action does not support accessed by RAM mode. | 403 |

| psaraDB for Redis |   | De | veloper Guide·API referenc |
|---|---|---|---|

| Description | Error code | Error message | HTTP status code |
|---|---|---|---|
| The error message returned because an exception or error occurs on the server. | ServiceUnavailable | The request has failed due to a temporary failure of the server. | 503 |
| The error message returned because the instance status that you specified does not exist. | InvalidStatus.NotFound | The Status provided does not exist in our records. | 404 |
| The error message returned because the specified value of the parameter is invalid. | InvalidParameter | The specified parameter InstanceName is not valid. | 400 |
| The error message returned because you are not authorized to call the administrator- specific API operations. | Forbbiden.NotAdminUse r | User not authorized to operate on the specified API as you are not the | 403 |
| The error message returned because the parameter is missing. | MissingParameter | Specified parameter is missing. | 400 |
| The error message returned because neither InstanceName nor NewPassword is specified. | MissingParameter | InstanceName/NewPass word at least one is mandatory for this action. | 400 |
| The error message returned because OwnerId is not specified for this operation. | MissingParameter | The input parameter OwnerId, OwnerAccount that is mandatory for processing this request | 403 |
| The error message returned because the specified Token parameter is invalid. | InvalidToken.Malformed | The Specified parameter "Token" is not valid. | 400 |
| The error message returned because the specified InstanceName parameter is invalid. | InvalidInstanceName.Ma lformed | The Specified parameter "InstanceName" is not valid. | 400 |
| The error message returned because the specified Password parameter is invalid. | InvalidPassword.Malfor med | The Specified parameter "Password" is not valid." | 400 |

| Description | Error code | Error message | HTTP status code |
|---|---|---|---|
| The error message returned because the specified Instances parameter is invalid. | InvalidInstances.Malfor med | The Specified parameter "Instances" is not valid. | 400 |
| The error message returned because the specified StartTime parameter is invalid. | InvalidStartTime.Malfor med | The Specified parameter "StartTime" is not valid. | 400 |
| The error message returned because the specified EndTime parameter is invalid. | InvalidEndTime.Malform ed | The Specified parameter "EndTime" is not valid. | 400 |
| The error message returned because the specified InstanceIds parameter is invalid. | InvalidInstanceIds.Malfo rmed | The Specified parameter "InstanceIds" is not valid. | 400 |
| The error message returned because your balance is insufficient to perform the current operation. | InsufficientBalance | Your account does not have enough balance. | 400 |
| The error message returned because your account fails to pass the real-name authentication. | RealNameAuthenticatio nError | Your account has not passed the real-name authentication yet. | 403 |
| The error message returned because your instance quota has been exhausted. | QuotaExcee | Living afterpay instances quota exceeded. | 400 |
| The error message returned because the capacity configuration is invalid. | InvalidCapacity.NotFoun d | The Capacity provided does not exist in our records. | 400 |
| The error message returned because the ClientToken parameter used for this request has already been used for a different request. | IdempotentParameterMi smatch | Request uses a client token in a previous request but is not identical to that request. | 400 |

| Description | Error code | Error message | HTTP status code |
|---|---|---|---|
| The error message returned because the inventory of instances in the specified zone is insufficient. | QuotaNotEnough | Quota not enough in this zone. | 400 |
| The error message returned because you are not authorized to call the order-class API operations. | Forbbiden.SubUser | The specified action is not available for you. | 403 |
| The error message returned because the Apsara Stack risk control system denies this access request. | Forbidden.RiskControl | This operation is forbidden by Aliyun Risk Control system. | 403 |
| The error message returned because the specified region does not exist. | InvalidRegion.NotFound | The RegionId or ZoneId provided does not exist in our records. | 404 |
| The error message returned because the specified ZoneId parameter is invalid. | InvalidZoneId.NotFound | The ZoneId provided is invalid. | 400 |
| The error message returned because the ID of the instance does not exist. | InvalidInstanceId.NotFou nd | The InstanceId provided does not exist in our records. | 404 |
| The error message returned because the password is incorrect. | IncorrectPassword | The Password provided is not correct. | 400 |
| The error message returned because the service is unavailable. | ServiceNotSupported | The specified service is not supported. | 400 |
| The error message returned because a renewal and configuration change order has not taken effect. | HasRenewChangeOrder | This instance has a renewChange order. | 400 |
| The error message returned because an internal error occured. | InternalError | The request processing has failed due to some unknown error. | 500 |

| Description | Error code | Error message | HTTP status code |
|---|---|---|---|
| The error message returned because the specified backup time is invalid. | InvalidPreferredBackupT ime | Specified preferred backup time is not valid. | 400 |
| The error message returned because the specified backup type is invalid. | InvalidBackupType.Form at | Specified backup type is not valid. | 400 |
| The error message returned because the specified backup method is invalid. | InvalidBackupMethod.Fo rmat | Specified backup method is not valid. | 400 |
| The error message returned because the backup task already exists. | BackupJobExists | A backup job already exists in the specified DB instance. | 400 |
| The error message returned because the maximum number of daily backup operations has been reached. | BackupTimesExceeded | Exceeding the daily backup times of this DB instance. | 400 |
| The error message returned because no parameters are specified. | ParameterLeastAssociat e | Must input at least one optional parameter. | 400 |
| The error message returned because the specified backup period is invalid. | InvalidBackupRetentionP eriod.Malformed | Specified backup retention period is not valid. | 400 |
| The error message returned because the specified next backup time is invalid. | InvalidPreferredBackupT ime.Format | Specified preferred backup time is not valid. | 400 |
| The error message returned because the specified backup period is invalid. | InvalidPreferredBackupP eriod.Malformed | Specified backup period is not valid. | 400 |
| The error message returned because the operation is not supported by the current instance type. | IncorrectDBInstanceTyp e | Current DB instance type does not support this operation | 400 |

| Description | Error code | Error message | HTTP status code |
|---|---|---|---|
| The error message returned because the specified key is invalid. | InvalidKey.Malformed | Specified key is not valid. | 400 |
| The error message returned because the nonce signature is used and cannot be used again. | SignatureNonceUsed | Specified signature nonce was used already. | 400 |
| The error message returned because no virtual IP address can be assigned. | AllocateVpcIp.NotEnoug h | Ip resource is not enough | 400 |
| The error message returned because instances of the specified type cannot be created in the zone. | Zone.NotSupport | Specified zone does not support creating with instance class. | 400 |
| The error message returned because the code for the instance type is invalid. | MissingClassCode | Capacity or InstanceClass is mandatory for this action. | 400 |
| The error message returned because the specified instance type is not supported. | InvalidDBInstanceClass.N otFound | Specified DB instance class is not found. | 404 |
| The error message returned because the instance is locked. | IncorrectDBInstanceLock Mode | Current DB instance lock mode does not support this operation. | 400 |
| The error message returned because the ID of the backup set does not exist. | InvalidBackupSetID.NotF ound | Specified backup set ID does not exist. | 400 |
| The error message returned because the operation is not supported while the instance is in the current state. | IncorrectDBInstanceStat e | Current DB instance state does not support this operation. | 400 |
| The error message returned when the available resource capacity in the specified instance is insufficient. | InsufficientResourceCap acity | There is insufficient capacity available for the requested instance. | 400 |

| Description | Error code | Error message | HTTP status code |
|---|---|---|---|
| The error message returned because the specified end time is invalid. | InvalidEndTime.Format | Specified end time is not valid. | 400 |
| The error message returned because the specified duration for reserving a classic IP address is invalid. | InvalidClassicExpiredDay s.Format | The specified classicExpiredDays format is not valid. | 400 |
| The error message returned because the operation is not supported while the backup set is in the current state. | IncorrectBackupSetStat e | Current backup set state does not support operations. | 400 |
| The error message returned when the specified whitelist is not correct in format. | InvalidSecurityIPList.For mat | Specified security IP list format is not valid. | 400 |

#### 2.12.3 Instance configurations

KVStore for Redis instance configurations

| Parameter | Description | Value |
|---|---|---|

| Parameter | Description | Value |
|---|---|---|
| maxmemory-policy | The eviction policy that a KVStore for Redis instance uses to evict data when the memory exceeds the threshold. KVStore for Redis supports six data eviction policies. | VolatileLRU: only evicts original data that has Time To Live (TTL) configured based on the Least Recently Used (LRU) algorithm. VolatileTTL: only evicts data that has TTL configured based on the TTL values in ascending order. AllKeysLRU: evicts original data based on the LRU algorithm. VolatileRandom: only evicts original data that has TTL configured randomly. AllKeysRandom: evicts original data randomly. NoEviction: evicts no data, but returns an error message when you write new data to the instance. |
| hash-max-ziplist-entries | A hash object uses ziplist encoding only if the hash object meets both of the following conditions: The number of key-value pairs stored in the hash object is smaller than or equal to the value of list-max-ziplist- entries. The string lengths of keys and values in all key-value pairs stored in the hash object are smaller than or equal to the value of list-max-ziplist-value. | Default value: 512. |

| Parameter | Description | Value |
|---|---|---|
| hash-max-ziplist-value | A hash object uses ziplist encoding only if the hash object meets both of the following conditions: The number of key-value pairs stored in the hash object is smaller than or equal to the value of list-max-ziplist- entries. The string lengths of keys and values in all key-value pairs stored in the hash object are smaller than or equal to the value of list-max-ziplist-value. | Default value: 64. |
| list-max-ziplist-entries | A list object uses ziplist encoding only if the list object meets both of the following conditions: The number of key-value pairs stored in the list object is smaller than or equal to the value of list-max-ziplist- entries. The string lengths of keys and values in all key-value pairs stored in the list object are smaller than or equal to the value of list-max-ziplist-value. | Default value: 512. |
| list-max-ziplist-value | A list object uses ziplist encoding only if the list object meets both of the following conditions: The number of key-value pairs stored in the list object is smaller than or equal to the value of list-max-ziplist- entries. The string lengths of keys and values in all key-value pairs stored in the list object are smaller than or equal to the value of list-max-ziplist-value. | Default value: 64. |
| set-max-intset-entries | A set object uses intset encoding only if: the number of entries is smaller than or equal to the value of set-max-intset-entries and all entries are decimal integers. | Default value: 512. |

| Parameter | Description | Value |
|---|---|---|
| zset-max-ziplist-entries | A zset object uses ziplist encoding only if the zset object meets both of the following conditions: The number of key-value pairs stored in the zset object is smaller than or equal to the value of zset-max-ziplist- entries. The string lengths of keys and values in all key-value pairs stored in the zset object are smaller than or equal to the value of zset-max-ziplist- value. | Default value: 128. |
| zset-max-ziplist-value | A zset object uses ziplist encoding only if the zset object meets both of the following conditions: The number of key-value pairs stored in the zset object is smaller than or equal to the value of zset-max-ziplist- entries. The string lengths of keys and values in all key-value pairs stored in the zset object are smaller than or equal to the value of zset-max-ziplist- value. | Default value: 64. |

| Parameter | Description | Value |
|---|---|---|
| notify-keyspace-events | The keyspace notifications allow clients to subscribe to channels or modes to receive events where Redis datasets were modified in some way. | K: the keyspace notifications. All notifications are prefixed with \ keyspace\@ \ . __ _ _ E: the keyevent notifications. All notifications are prefixed with keyevent@ . __ __ g: the notifications about general commands that are non-type specific, such as DEL, EXPIRE, and RENAME. $: the string command notifications. l: the list command notifications. s: the set command notifications. h: the hash command notifications. z: the sorted set command notifications. x: the expiration events. The system sends an expiration event after the system deletes an expired key. e: the eviction events. The system sends an eviction event after the system evicts a key according to the maxmemory policy. A: the alias for g$lshzxe. |
