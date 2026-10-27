---
title: "Alibaba Cloud Apsara Stack Enterprise V3.12.0 API Gateway Developer Guide 20220928"
product_version: "V3.12.0"
doc_version: "20220928"
pdf_pages: 165
source_pdf: "Alibaba Cloud Apsara Stack Enterprise V3.12.0 API Gateway Developer Guide 20220928.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/01_ApsaraStackEnterprise/V3.12/%E5%BA%94%E7%94%A8%E6%9C%8D%E5%8A%A1/Alibaba%20Cloud%20Apsara%20Stack%20Enterprise%20V3.12.0%20API%20Gateway%20Developer%20Guide%2020220928.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes+edge-junk)
---

# Alibaba Cloud Apsara Stack Enterprise V3.12.0 API Gateway Developer Guide 20220928

## Table of Contents

- 1 Overview
- 2 List of operations by function
- 3 Use ASAPI to call APIs
  - 3.1 Overview
  - 3.2 Log on to the API Tool console
  - 3.3 View information about API operations
  - 3.4 Obtain the endpoint of ASAPI
  - 3.5 Obtain the core package for ASAPI
  - 3.6 Obtain an AccessKey pair
  - 3.7 Query the region ID
  - 3.8 API Gateway SDK for Java
  - 3.9 API Gateway SDK for Node.js
  - 3.10. (Optional) Use SDK for POP to call API operations on ASAPI
- 4 Request signatures
- 5 API group operations
  - 5.1 CreateApiGroup
  - 5.2 ModifyApiGroup
  - 5.3 DeleteApiGroup
  - 5.4 CreateApiStageVariable
  - 5.5 DeleteApiStageVariable
  - 5.6 DescribeApiGroup
  - 5.7 DescribeApiGroups
  - 5.8 DescribeApiStage
- 6 Domain name operations
  - 6.1 SetDomain
  - 6.2 SetDomainCertificate
  - 6.3 DescribeDomain
  - 6.4 DeleteDomain
  - 6.5 DeleteDomainCertificate
- 7 API management operations
  - 7.1 CreateApi
  - 7.2 ModifyApi
  - 7.3 DeployApi
  - 7.4 SwitchApi
  - 7.5 AbolishApi
  - 7.6 DeleteApi
  - 7.7 DescribeApi
  - 7.8 DescribeApiDoc
  - 7.9 DescribeApis
  - 7.10 DescribeApiHistory
  - 7.11 DescribeApiHistories
  - 7.12 DescribeDeployedApi
  - 7.13 DescribeDeployedApis
- 8 Plugin operations
  - 8.1 CreatePlugin
  - 8.2 ModifyPlugin
  - 8.3 DeletePlugin
  - 8.4 AttachPlugin
  - 8.5 DetachPlugin
  - 8.6 DescribePluginApis
  - 8.7 DescribePlugins
  - 8.8 DescribePluginsByApi
- 9 App management operations
  - 9.1 CreateApp
  - 9.2 ModifyApp
  - 9.3 ResetAppSecret
  - 9.4 DescribeAppAttributes
  - 9.5 DescribeAppSecurity
  - 9.6 DeleteApp
- 10 Authorization operations
  - 10.1 DescribeApps
  - 10.2 DescribeAuthorizedApis
  - 10.3 DescribeAuthorizedApps
  - 10.4 SetApisAuthorities
  - 10.5 SetAppsAuthorities
  - 10.6 RemoveApisAuthorities
  - 10.7 RemoveAppsAuthorities
- 11 Other operations
  - 11.1 DescribeRegions
  - 11.2 DescribeSystemParameters
- 12 Data types
  - 12.1 ApiGroupAttribute
  - 12.2 ApiHisItem
  - 12.3 ApiInfo
  - 12.4 ApiPluginSummary
  - 12.5 ApiSummary
  - 12.6 AppAttribute
  - 12.7 AppItem
  - 12.8 AuthorizedApi
  - 12.9 AuthorizedApp
  - 12.10 ConstantParameter
  - 12.11 CustomDomain
  - 12.12 DeployedApiItem
  - 12.13 DeployedInfo
  - 12.14 DomainItem
  - 12.15 ErrorCodeSample
  - 12.16 MonitorItem
  - 12.17 PluginAttribute
  - 12.18 Region
  - 12.19 RequestConfig
  - 12.20 RequestParameter
  - 12.21 ServiceConfig
  - 12.22 ServiceParameter
  - 12.23 ServiceParameterMap
  - 12.24 Special
  - 12.25 SpecialPolicy
  - 12.26 StageInfo
  - 12.27 SystemParameter
  - 12.28 SystemParamItem
- 13 Error codes

## 1 Overview

Welcome to use Alibaba Cloud API Gateway. You can use the APIs described in this document to perform relevant operations on API Gateway. Terms

| Term | Definition | Description |
|---|---|---|
| Region | Region | The region that you select to deploy an API. We recommend that you select the region to which your backend services belong. |
| API | Application Programming Interface | The API that you enter to deploy and provide external services or data. |
| Group | API group | A group of APIs. API providers must create an API group before providing API services. Each API group has one second-level domain and two runtime environments. An independent domain that has been ICP filed and resolved to the second-level domain must be bound to the API group. APIs in the same group can be accessed by using the bound independent domain. |
| SubDomain | Second-level domain | Each API group has a second-level domain. An independent domain must be resolved to the second-level domain, which can be accessed directly to call APIs in the test environment. |
| CustomDom ain | Custom domain | An independent domain that you bind to an API group. Before you bind your domain name to an API group, add a CNAME record to resolve your domain name to the second-level domain and make sure that the bound independent domain is ICP filed or transferred for ICP filing at Alibaba Cloud. If the APIs in the group support HTTPS, upload an SSL certificate for the domain name. |
| Stage | Runtime environment | The runtime environment of an API group. Each API group that you create has two runtime environments: test and production. Only APIs that have been published to an environment can be called. When you access the second-level domain of an API group, APIs in the test environment are called by default. |
| Signature | Backend signature key | An authentication key issued by an API provider to API Gateway. The backend signature key takes effect immediately after it is bound to APIs. After receiving API requests, API Gateway sends the requests with signature information contained to your backend service. The backend service parses the signature information and authenticates API Gateway. |

| Term | Definition | Description |
|---|---|---|
| TrafficContr ol | Throttling policy | The throttling policy that is applied to APIs. The throttling policy takes effect immediately after it is bound to APIs. The policy is used to perform API-, app-, and user-level throttling on API calls. You can also configure special throttling policies. For example, when an app or a user calls an API that is bound with a special throttling policy, access to the API is controlled based on the special throttling value. |
| Special | Special throttling policy | Configured under a throttling policy. Special throttling policies are used to control the access to bound APIs for specified apps or users. |
| APP | App | The app that you create as an identity to call an API provided by another user. When API Gateway receives a request, it uses the AppKey and AppSecret to verify the signature. |

by function

## 2 List of operations by function

API group management

| Operation | Description |
|---|---|
| CreateApiGroup | Creates an API group. |
| ModifyApiGroup | Modifies an API group. |
| DeleteApiGroup | Deletes an API group. |
| CreateApiStageVariable | Creates an environment variable. |
| DeleteApiStageVariable | Deletes an environment variable. |
| DescribeApiStage | Queries detailed information of a specified environment. |
| DescribeApiGroup | Queries detailed information of a specified API group. |
| DescribeApiGroups | Queries API groups. |

Domain name management

| Operation | Description |
|---|---|
| SetDomain | Binds a custom domain. |
| SetDomainCertificate | Uploads an SSL certificate for a specified custom domain. |
| DescribeDomain | Queries detailed information of a specified custom domain. |
| DeleteDomain | Deletes a specified custom domain. |
| DeleteDomainCertificate | Deletes the certificate of a specified domain name. |

API management

| Operation | Description |
|---|---|
| CreateApi | Creates an API. |
| ModifyApi | Modifies an API. |
| DeployApi | Publishes an API to a specified environment. |

by function

| Operation | Description |
|---|---|
| SwitchApi | Switches the runtime definition of an API in a specified environment. |
| AbolishApi | Unpublishes an API in a specified environment. |
| DeleteApi | Deletes the definition of a specified API. |
| DescribeApi | Queries detailed information of a specified API definition. |
| DescribeApis | Queries the APIs that belong to a certain definition. |
| DescribeApiDoc | Queries the descriptive documentation of an API in a specified environment. |
| DescribeDeployedApi | Queries the runtime definition of an API in a specified environment. |
| DescribeDeployedApis | Queries the APIs that are running in a specified environment. |
| DescribeApiHistory | Queries the definition of an API in a specified earlier version. |
| DescribeApiHistories | Queries the earlier versions of a specified API. |

Plugin management

| Operation | Description |
|---|---|
| CreatePlugin | Creates a plugin. |
| ModifyPlugin | Modifies a plugin. |
| DeletePlugin | Deletes a plugin. |
| AttachPlugin | Binds a plugin to an API. |
| DetachPlugin | Unbinds a plugin from an API. |
| DescribePluginApis | Queries the APIs to which a plugin is bound. |
| DescribePlugins | Queries plugins and their detailed information. |
| DescribePluginsByApi | Queries the plugins bound to an API. |

App management

| Operation | Description |
|---|---|
| CreateApp | Creates an app. |

| PI Gateway | by functio |
|---|---|
| Operation | Description |
| ModifyApp | Modifies an app. |
| ResetAppSecret | Resets the secret of a specified app. |
| DescribeAppAttributes | Queries apps and their basic information. |
| DescribeAppSecurity | Queries detailed information of a specified app key. |
| DeleteApp | Deletes an app. |

Authorization

| Operation | Description |
|---|---|
| DescribeApps | Queries the apps to which permissions can be granted. |
| DescribeAuthorizedApis | Queries the APIs that a specified app is authorized to call. |
| DescribeAuthorizedApps | Queries the apps that have access to a specified API. |
| SetApisAuthorities | Grants access permissions on multiple APIs to a specified app. |
| SetAppsAuthorities | Grants access permissions on a specified API to multiple apps. |
| RemoveApisAuthorities | Revokes the access permissions on multiple APIs from a specified app. |
| RemoveAppsAuthorities | Revokes the access permissions on a specified API from multiple apps. |

Other operations

| Operation | Description |
|---|---|
| DescribeRegions | Queries supported regions. |
| DescribeSystemParameters | Queries system parameters. |

APIs

## 3 Use ASAPI to call APIs

### 3.1 Overview

This topic describes the architecture and features of Apsara Stack API (ASAPI). ASAPI is a platform that integrates all features and is the only portal to connect to Apsara Stack. ASAPI can categorize, audit, and manage API operations. It can also assemble and customize existing operations and adapt to your operations. Each cloud service can call ASAPI for required data and features, which avoids inconsistent operations caused by different calling methods and separate encapsulation. This can ensure the operation program integrity and improve development efficiency and code portability. ASAPI allows you to manage and call operations in a centralized manner and customize development. ASAPI supports access to most cloud services deployed in Apsara Stack and supports passthrough or encapsulation of different backend APIs. This way, operations can be called using the same method. ASAPI allows you to use SDKs and API portals to call APIs registered on ASAPI, customize SDKs, and manage versions of Apsara Stack, services, and APIs. APIs

### 3.2 Log on to the API Tool console

You can log on to the API Tool console through the Apsara Stack Cloud Management (ASCM) console. Prerequisites Before you log on to the Apsara Uni-manager Management Console, the endpoint of the console is obtained from the deployment staff. We recommend that you use Google Chrome. Procedure
1. Enter the URL of the Apsara Uni-manager Management Console in the address bar and press the
Enter key.
2. Enter your username and password.
Obtain the username and password that you use to log on to the Apsara Uni-manager Management Console from the operations administrator. Not e The first time that you log on to the Apsara Uni-manager Management Console, you must change the password of your account. For security purposes, your password must meet the minimum complexity requirements. The password must be 10 to 32 characters in length and must contain at least two of the following character types: Uppercase or lowercase letters Digits Special characters, including exclamation points (!), at signs (@), number signs (#), dollar signs ($), and percent signs (%)
3. Click Log On.
4. In the top navigation bar, choose Product s > Ot hers > API T ool.

### 3.3 View information about API operations

operations This topic describes how to view information about API operations. The following information is required when you use an SDK: product name, API operation name, and API operation version. Procedure
1. Log on to the API Tool console.
2. Click API f old in the left-side navigation pane.
3. On the API Direct ory page, select the required product from the drop-down list in the upper-left
corner, enter a keyword of API operation names in the search box, and click the search icon. APIs
4. View and record the required product name, API operation name, and API operation version.

### 3.4 Obtain the endpoint of ASAPI

You can obtain the endpoint of Apsara Stack API (ASAPI) in the Apsara Stack Operations (ASO) console. Procedure
1. In the address bar, enter the URL region-id.aso.intranet-domain-id.com and press the Enter key.
Not e You can select a language from the drop-down list in the upper-right corner of the page.
2. Enter your username and password.
Not e Obtain the username and password for logging on to the ASO console from the deployment personnel or an administrator. When you log on to the ASO console for the first time, you must change the password of your username as prompted. To enhance security, a password must meet the following requirements: APIs It must contain uppercase and lowercase letters. It must contain digits. It must contain special characters such as exclamation points (!), at signs (@), number signs (#), dollar signs ($), and percent signs (%). It must be 10 to 20 characters in length.
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
of the Apsara ASAPI Management platform. APIs

### 3.5 Obtain the core package for ASAPI

ASAPI Apsara Stack uses Apsara Stack API (ASAPI) as a unified portal for all Apsara Stack products that are connected to ASAPI. ASAPI also provides SDKs to call product APIs. For more information about how to obtain the core package for ASAPI, see Apsara Stack documentation.

### 3.6 Obtain an AccessKey pair

An AccessKey pair consists of an AccessKey ID and an AccessKey secret. The AccessKey pair is used to implement symmetric encryption to verify the identity of the requester. The AccessKey ID is used to identify a user. The AccessKey secret is used to encrypt the signature string. This topic describes how to obtain the AccessKey pair of an organization. Prerequisites Only operations administrators and level-1 organization administrators can obtain the AccessKey pair of an organization. Obtain the AccessKey pair of an organization To obtain the AccessKey pair of an organization, perform the following operations:
1. Log on to the Apsara Stack Cloud Management (ASCM) console as an administrator.
2. In the top navigation bar, click Ent erprise.
3. In the left-side navigation pane of the Ent erprise page, click Organizat ions.
4. In the Organizations navigation tree, click the
icon on the right of the organization to be added.
5. Select AccessKey.
6. In the message that appears, view the AccessKey pair of the organization.
APIs Not e An AccessKey pair is automatically allocated to a level-1 organization. Subordinate organizations use the same AccessKey pair as their level-1 organization. Obtain the AccessKey pair of a personal account To obtain the AccessKey pair of a personal account, perform the following operations:
1. Log on to the ASCM console as an administrator.
2. In the upper-right corner of the homepage, move the pointer over the profile picture and click User
Inf ormat ion.
3. In the Apsara St ack AccessKey Pair section of the User Information page, view your AccessKey
pair. Not e The AccessKey pair consists of an AccessKey ID and an AccessKey secret. They allow you to access Apsara Stack resources with full permissions for your account. You must keep them confidential.

### 3.7 Query the region ID

You must specify the region ID when you call Apsara Stack SDK for Node.js. You must query the region ID in the Apsara Stack Cloud Management (ASCM) console. Procedure
1. Log on to the ASCM console as an administrator.
2. In the upper-right corner of the homepage, move the pointer over the profile picture and click User
Inf ormat ion.
3. In the Apsara St ack AccessKey Pair section, you can view the region ID.

### 3.8 API Gateway SDK for Java

This topic describes how to obtain and use API Gateway SDK for Java. Prerequisites You must have an Apsara Stack tenant account and an AccessKey pair (AccessKey ID and AccessKey secret) to use API Gateway SDK for Java. For more information about how to obtain and view your AccessKey pair in the ASCM console, see Obtain an AccessKey pair. For more information about how to obtain the endpoint of the Apsara Stack API (ASAPI), see Obtain the endpoint of Asapi. APIs JDK 1.6 or later is required for Apsara Stack API Gateway SDK for Java. Add a dependency Add the following dependency to pom.xml:

```xml
<dependency>
    <groupId>com.aliyun</groupId>
    <artifactId>asapi</artifactId>
    <version>0.0.3-RELEASE</version>
</dependency>
```

Usage You can call API operations on ASAPI by sending GET and POST requests. GET requests

```
 ASClient client = new ASClient();
// Form 1 String result = client.doGet(endpoint, parameters); // Form 2 String result = client.doRequest(endpoint, parameters);
```

POST requests APIs

```
// Obtain the endpoint of ASAPI. String endpoint = "http://xxx/asapi/v3"; // Configure request parameters. Map<String, String> parameters = new HashMap<String, String>(); // Configure product- and API operation-related parameters. parameters.put("Product", "CloudAPI"); //The product name, which must be the s ame as that displayed on the API Directory page. parameters.put("Action", "CreateApiGroup"); //The API operation, which is case-s ensitive and must be the same as that displayed on the API Directory page. parameters.put("Version", "2016-07-14"); //The API operation version. // Configure authorization-related parameters. parameters.put("AccessKeyId", "<your-access-key-id>"); // The AccessKey ID of th e authorized account. parameters.put("AccessKeySecret", "<your-access-key-secret>"); // The AccessKey secret o f the authorized account. parameters.put("RegionId", "<Region>"); // The region ID. // Configure business parameters. parameters.put("GroupName", "testGroup"); parameters.put("Description", "test"); // Create an ASClient instance for initiating requests. ASClient client = new ASClient(); // Add request headers. client.addHeader("x-acs-regionid", "<your-regionid>"); client.addHeader("x-acs-resourcegroupid", "<your-resourcegroupid>"); client.addHeader("x-acs-organizationid", "<your-organizationid>"); // The organization I
```

`D.`

```
client.addHeader("x-acs-instanceid", "<your-instanceid>"); // Initiate the request and obtain the response. String result = client.doPost(endpoint, parameters);
```

Header parameters

| Parameter | Description |
|---|---|
| x-acs-regionid | The region ID. For more information about how to obtain a region ID, see Query the region ID. |
| x-acs-organizat ionid | The ID of the organization in the ASCM console. |
| x-acs-resourcegroupid | The ID of the resource set in the ASCM console. |
| x-acs-inst anceid | The ID of the instance for which you want to change settings. This parameter is not required for API operations that are used to create resources. |

### 3.9 API Gateway SDK for Node.js

This topic describes how to obtain and use API Gateway SDK for Node.js. Prerequisites You must have an Apsara Stack tenant account and an AccessKey pair (AccessKey ID and AccessKey APIs secret) to use API Gateway SDK for Node.js. For more information, see Obtain an AccessKey pair. For more information about how to obtain the endpoint of the Apsara Stack API (ASAPI), see Obtain the endpoint of Asapi. For more information about how to obtain the region ID, see Query the region ID. Add a dependency
1. Install API Gateway SDK for Node.js.

```
 tnpm install --save @ali/asapi-nodejs-sdk
```

2. If mocha.opts depends on Egg.js, configure mocha.opts.

```
--recursive --colors --timeout 60000 --reporter mochawesome --require co-mocha --require egg-ts-helper/register --require espower-typescript/guess --require intelli-espower-loader
```

Usage The following example shows the three main steps of using API Gateway SDK for Node.js:
1. Create an ASClient instance. To create an ASClient instance, specify the region ID, endpoint,
AccessKey ID, and AccessKey secret in the config.ts file. Example:

```
local: {
    regionId: 'obtained region ID',
    API_GATEWAY: 'obtained endpoint',
    accessKeyId: 'your AccessKey ID',
    accessKeySecret: 'your AccessKey secret',
```

`},`
2. Create an API request and configure parameters.
3. Initiate the API request and handle the response or exception.
APIs

```
// Specify the endpoint of ASAPI. const API_GATEWAY = "http://xxxx/asapi/v3" // Create an RPC client. const asapiClient = ctx.service.sdk.rpcClient; // Configure parameters. let params = {
    Action: 'CreateApiGroup',
    Product: 'CloudAPI',
    regionId: 'cn-qingdao-env12-d01',
    accessKeyId: 'xxxxxxx',
    accessKeySecret: 'xxxxxxx',
    Version: '2016-07-14',
    GroupName: 'TestGroup',
    Description: 'Test'
```

};

```
// Configure parameters in the request header. asapiClient.addHeader("x-acs-regionId", "cn-qingdao-env12-d01"); // Initiate the request and obtain the response. const result = await asapiClient.doRequest(API_GATEWAY, params, {});
```

3.10. (Optional) Use SDK for POP to call API operations on ASAPI If an app used SDK for POP to call API operations, you must switch API Gateway to Apsara Stack API (ASAPI) to call these operations. Procedure Add required common parameters and the Product Name field to a request header based on product requirements. Then execute code to switch API Gateway to ASAPI. Not e Different products use different endpoints in SDK for POP. However, ASAPI provides only one domain name. You cannot use the API operation name and the version number to identify the product to which an API operation belongs. For example, both ECS and KVStore for Redis provide the DescribeInstances operation of the 2015-01-01 version. Code samples The following code provides an example on how to use SDK for POP to call API operations. APIs

```java
 try {
            DefaultProfile clientProfile = DefaultProfile.getProfile(regionId, accessKeyId,
accessKeySecret);
            //Set the ASAPI gateway. Format: server.asapi.${intranet-domain}.
            clientProfile.addEndpoint(region, region, "CloudAPI", "<ASAPI gateway>");
            DefaultAcsClient acsClient = new DefaultAcsClient(clientProfile);
            DescribeApiGroupsRequest request = new DescribeApiGroupsRequest();
            request.setSysRegionId(regionId); // or setRegionId(regionId)
            // Configure common parameters based on the information about the current user.
            request.putHeaderParameter("x-acs-organizationid", "<Organization ID>");
            request.putHeaderParameter("x-acs-resourcegroupid", "<Resource group ID>");
            request.putHeaderParameter("x-ascm-product-name", "CloudAPI");
            request.putHeaderParameter("x-ascm-product-version", "2016-07-14");
            request.putHeaderParameter("x-ascm-product-ak", "<AccessKey ID>");
            request.putHeaderParameter("x-ascm-product-sk", "<AccessKey Secret>");
            DescribeApiGroupsResponse result = (DescribeApiGroupsResponse) acsClient.getAcs
Response(request);
            List<DescribeApiGroupsResponse.ApiGroupAttribute> apiGroupAttributes = result.g
etApiGroupAttributes();
            for (DescribeApiGroupsResponse.ApiGroupAttribute group: apiGroupAttributes) {
                System.out.println(group.getGroupId);
                System.out.println(group.getGroupName);
                System.out.println(group.getSubDomain);
```

`}`

```
        } catch (Exception e) {
            e.printStackTrace();
```

`}` Header parameters

| Parameter | Description |
|---|---|
| x-ascm-product -name | The product name. |
| x-ascm-product -version | The API operation version. |
| x-ascm-product -ak | The AccessKey ID of the organization in the ASCM console. |
| x-ascm-product -sk | The AccessKey secret of the organization in the ASCM console. |

s

## 4 Request signatures

API Gateway authenticates each access request. Therefore, a request must contain signature information regardless of whether it is submitted using HTTP or HTTPS. API Gateway performs symmetric encryption by using an AccessKey ID and an AccessKey Secret to verify the identity of a requester. The AccessKey ID and AccessKey Secret are issued to visitors by Alibaba Cloud (visitors can apply for and manage them on the official Alibaba Cloud website). The AccessKey ID indicates the identity of the visitor. The AccessKey Secret is used to encrypt signature strings and verify signature strings sent by the server. Keep your AccessKey Secret confidential. You can perform the following steps to sign a request:
1. Use request parameters to construct a canonicalized query string.
To construct a canonicalized query string, sort all request parameters by name in alphabetical order. These parameters include common request parameters and customized API request parameters, but do not include the Signature parameter. Not e If you send a request by using the `GET` method, the request parameters are included as a part of the request URL. These parameters follow the question mark (?) in the request URL and are connected with ampersands (&). Encode the name and value of each request parameter The parameter names and values must be encoded using UTF-8. The URL encoding rules are described as follows: Uppercase and lowercase letters, digits, hyphens (-), underscores (_), periods (.), and tildes (~) are not encoded. Other characters are encoded as %XY, where XY is the hexadecimal representation of the character in ASCII. For example, double quotation marks (") are encoded as %22. Extended UTF-8 characters are encoded in the %XY%ZA… format. A space is encoded as %20, rather than the plus sign (+). Not e Most libraries that support URL encoding, such as java.net.URLEncoder, comply with the MIME encoding rules of application/x-www-form-urlencoded. If this encoding method is used, replace the plus signs (+) in the encoded strings with %20, the asterisks (*) with %2A, and %7E with a tilde (~) to conform to the encoding rules. Connect the encoded parameter names and values with equal signs (=). Sort the equal sign-connected strings by their parameter names alphabetically and connect them with ampersands (&).
2. Use the created canonicalized query string to construct a signature string based on the following
rule:

```
StringToSign= HTTPMethod + “&” + percentEncode(“/”) + ”&” + percentEncode(CanonicalizedQueryString)
```

In the preceding example, s `HTTPMethod` indicates that an HTTP-style request such as `GET` is submitted. `percentEncode("/")` is the encoded value (%2F) of a forward slash (/). The encoding follows the URL encoding rules described in the preceding step. `percentEncode(CanonicalizedQueryString)` is the string constructed using the canonicalized query string. The encoding follows the URL encoding rules described in the preceding step.
3. Use the signature string to calculate the HMAC value of the signature as defined by RFC 2104.
> **Note:** The key used to calculate the signature is your AccessKey Secret with an ampersand (&) appended to it. SHA1 is used to calculate the signature.

4. Encode the HMAC value into a string based on the Base64 encoding rules. This encoded string is the
signature value.
5. Add this signature value as the value of the Signature parameter to the request parameters. You
have now completed the request signing process. Not e The obtained signature value must be encoded based on RFC 3986 URL encoding specification before it can be submitted to the API Gateway server as a request parameter value. Taking DescribeRegions as an example, the request URL placed before the signature is as follows:

```
http://apigateway.[ RegionId].aliyuncs.com?Format=json&AccessKeyId=testid&Action=DescribeRe gions&SignatureMethod=Hmac-SHA1&SignatureNonce=d48e931b-90c9-49c7-ac86-a70dd3607c88&Signatu reVersion=1.0&Version=2016-07-14&Timestamp=2016-09-27T09%3A08%3A30Z
```

The StringToSign placed after the signature is as follows:

```
GET&%2F&AccessKeyId%3Dtestid%26Action%3DDescribeRegions%26Format%3Djson%26SignatureMethod%3 DHmac-SHA1%26SignatureNonce%3Dd48e931b-90c9-49c7-ac86-a70dd3607c88%26SignatureVersion%3D1.0 %26Timestamp%3D2016-09-27T09%253A08%253A30Z%26Version%3D2016-07-14
```

If the AccessKey ID is testid, the AccessKey Secret is testsecret, the key used for HMAC calculation is testsecret&. The calculated signature is DRdMb%2F1m7PeToGRBApTl3wThyOg%3D . The signed request URL with the Signature parameter added is as follows:

```
http://apigateway.[ RegionId].aliyuncs.com?Signature=DRdMb%2F1m7PeToGRBApTl3wThyOg%3D&Forma t=json&AccessKeyId=testid&Action=DescribeRegions&SignatureMethod=Hmac-SHA1&SignatureNonce=d 48e931b-90c9-49c7-ac86-a70dd3607c88&SignatureVersion=1.0&Version=2016-07-14&Timestamp=2016- 09-27T09%3A08%3A30Z
```

ns

## 5 API group operations

### 5.1 CreateApiGroup

Description You can call this operation to create an API group. You must create an API group before creating an API. An API group is a basic attribute of an API. This operation is intended for API providers. A second-level domain name is automatically allocated to the API group for testing purposes. An API group has a region attribute. After you create an API and select a group for the API, the corresponding region is also selected. We recommend that you select the same region to which your back-end services belong to reduce network delay. After you create an API group, you can bind a custom domain name to the group. The QPS limit on this operation is 50 per user. Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set this parameter to CreateApiGroup. |
| GroupName | String | Yes | The name of the API group to be created. The name must be globally unique. The name must be 4 to 50 characters in length. It must start with a letter and can contain letters, digits, and underscores ( ). _ |
| Description | String | Yes | The description of the API group to be created. The description can contain a maximum of 180 characters in length. |

Response parameters

| Parameter | Type | Description |
|---|---|---|
| RequestId | String | The ID of the request. |
| GroupID | String | The ID of the API group. This ID is generated by the system and is globally unique. |
| GroupName | String | The name of the API group. |
| SubDomain | String | The second-level domain name bound to the API group. This domain name is used to test API calls. |
| Description | String | The description of the API group. |

Examples ns Sample request s

```
http://apigateway.cn-hangzhou.aliyuncs.com?Action=CreateApiGroup &GroupName=Weather &Descri ption=The weather informations. &<Common request parameters>
```

Sample responses XML format

```xml
<CreateApiGroupResponse>
    <RequestId>FF3B7D81-66AE-47E0-BF69-157DCF187514</RequestId>
    <GroupId>523e8dc7bbe04613b5b1d726c2a7889d</GroupId>
    <GroupName>Weather</GroupName>
    <SubDomain>523e8dc7bbe04613b5b1d726c2a7889d-cn-hangzhou.alicloudapi.com</SubDomain>
    <Description>The weather informations</Description>
</CreateApiGroupResponse>
```

JSON format `{`

```json
  "RequestId": "FF3B7D81-66AE-47E0-BF69-157DCF187514",
  "GroupId": "523e8dc7bbe04613b5b1d726c2a7889d",
  "GroupName": "Weather",
  "SubDomain": "523e8dc7bbe04613b5b1d726c2a7889d-cn-hangzhou.alicloudapi.com",
  "Description": "The weather informations"
```

`}`

### 5.2 ModifyApiGroup

Description You can call this operation to modify the name or description of an existing API group. This operation is intended for API providers. The QPS limit on this operation is 50 per user. Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set this parameter to ModifyApiGroup. |
| GroupId | String | Yes | The ID of the API group to be modified. This ID is generated by the system and is globally unique. |
| GroupName | String | No | The name of the API group to be modified. The name must be globally unique. It must be 4 to 50 characters in length. It must start with a letter and can contain letters, digits, and underscores ( ). If _ this parameter is not specified, the name cannot be modified. |

ns

| Parameter | Type | Required | Description |
|---|---|---|---|
| Description | String | No | The description of the API group to be modified. The description can contain a maximum of 180 characters in length. If this parameter is not specified, the description cannot be modified. |

Response parameters

| Parameter | Type | Description |
|---|---|---|
| RequestId | String | The ID of the request. |
| GroupID | String | The ID of the API group. This ID is generated by the system and is globally unique. |
| GroupName | String | The name of the API group. |
| SubDomain | String | The second-level domain name that is automatically allocated to the API group. |
| Description | String | The description of the API group. |

Examples Sample request s

```
http://apigateway.cn-hangzhou.aliyuncs.com?Action=ModifyApiGroup &Description=New weather i nformations. &GroupId=523e8dc7bbe04613b5b1d726c2a7889d &GroupName=NewWeather &<Common reque st parameters>
```

Sample responses XML format

```xml
<ModifyApiGroupResponse>
    <RequestId>4CF287C6-CE5B-477B-BE27-C48F99EADBC8</RequestId>
    <GroupId>523e8dc7bbe04613b5b1d726c2a7889d</GroupId>
    <GroupName>NewWeather</GroupName>
    <SubDomain>523e8dc7bbe04613b5b1d726c2a7889d-cn-hangzhou.alicloudapi.com</SubDomain>
    <Description>New weather informations. </Description>
</ModifyApiGroupResponse>
```

JSON format `{`

```json
    "RequestId": "4CF287C6-CE5B-477B-BE27-C48F99EADBC8",
    "GroupId": "523e8dc7bbe04613b5b1d726c2a7889d",
    "GroupName": "NewWeather",
    "SubDomain":"523e8dc7bbe04613b5b1d726c2a7889d-cn-hangzhou.alicloudapi.com"
    "Description": "New weather informations."
```

ns

### 5.3 DeleteApiGroup

Description You can call this operation to delete a specified API group. This operation is intended for API providers. An API group containing APIs cannot be deleted. To delete the API group, you must first delete its APIs. After an API group has been deleted, the second-level domain name assigned to the API group is automatically invalidated. If the specified API group does not exist, a successful response will still appear. The QPS limit on this operation is 50 per user. Request parameters

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DeleteApiGroup. |
| GroupId | String | Yes | The API group ID, which is generated by the system and globally unique. |

Response parameters

| Name | Type | Description |
|---|---|---|
| RequestId | String | The request ID. |

Examples Sample request

```
http://apigateway.cn-hangzhou.aliyuncs.com?Action=DeleteApiGroup &GroupId=523e8dc7bbe04613b5b1d726c2a7889d &<Common request parameters>
```

Sample responses XML format

```xml
<DeleteApiGroupResponse>
    <RequestId>E8515BA6-81CD-4191-A7CF-C4FCDD3C0D99</RequestId>
</DeleteApiGroupResponse>
```

JSON format `{`

```json
    "RequestId": "E8515BA6-81CD-4191-A7CF-C4FCDD3C0D99"
```

ns

### 5.4 CreateApiStageVariable

Description You can call this operation to add a variable to a specified environment. This operation is intended for API providers. Request parameters

| Name | Type | Requi red | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to CreateApiStageVariable. |
| GroupId | String | Yes | The ID of the API group. |
| StageId | String | Yes | The ID of the runtime environment. |
| VariableName | String | Yes | The name of the variable to be added. This parameter is case- sensitive. |
| VariableValue | String | No | The value of the variable to be added. |

Response parameters

| Name | Type | Description |
|---|---|---|
| RequestId | String | The request ID. |

Examples Sample request

```
http://apigateway.cn-hangzhou.aliyuncs.com?Action=CreateApiStageVariable &GroupId=523e8dc7bbe04613b5b1d726c2a7889d &StageId=6EF60BEC-0242-43AF-BB20-270359FB54A7 &VariableName=serverName &VariableValue=api.domain.com &<Common request parameters>
```

Sample responses XML format

```xml
<CreateApiStageVariableResponse>
    <RequestId>03442A3D-3B7D-434C-8A95-A5FEB999B529</RequestId>
</CreateApiStageVariableResponse>
```

JSON format ns

```json
    "RequestId": "03442A3D-3B7D-434C-8A95-A5FEB999B529"
```

### 5.5 DeleteApiStageVariable

Description You can call this operation to delete a variable in a specified environment. This operation is intended for API providers. Request parameters

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DeleteApiStageVariable. |
| GroupId | String | Yes | The ID of the API group. |
| StageId | String | Yes | The ID of the runtime environment. |
| VariableName | String | Yes | The name of the variable to be deleted. This parameter is case-sensitive. |

Response parameters

| Name | Type | Description |
|---|---|---|
| RequestId | String | The request ID. |

Examples Sample request

```
http://apigateway.cn-hangzhou.aliyuncs.com?Action=DeleteApiStageVariable &GroupId=523e8dc7bbe04613b5b1d726c2a7889d &StageId=6EF60BEC-0242-43AF-BB20-270359FB54A7 &VariableName=serverName &<Common request parameters>
```

Sample responses XML format

```xml
<DeleteApiStageVariableResponse>
    <RequestId>03442A3D-3B7D-434C-8A95-A5FEB969B529</RequestId>
</DeleteApiStageVariableResponse>
```

JSON format ns

```json
    "RequestId": "03442A3D-3B7D-434C-8A95-A5FEB969B529"
```

### 5.6 DescribeApiGroup

Description You can call this operation to query details about an API group, including the automatically generated second-level domain name, custom domain name, and SSL certificate. This operation is intended for API providers. Request parameters

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeApiGroup. |
| GroupId | String | Yes | The API group ID, which is generated by the system and globally unique. |

Response parameters

| Name | Type | Description |
|---|---|---|
| RequestId | String | The request ID. |
| GroupID | String | The API group ID, which is generated by the system and globally unique. |
| GroupName | String | The name of the API group. |
| SubDomain | String | The second-level domain name automatically assigned to the API group. |
| Description | String | The description of the API group. |
| CreatedTime | String | The creation time (UTC) of the API group. |
| ModifiedTime | String | The last modification time (UTC) of the API group. |
| RegionId | String | The region to which the API group belongs. |
| Status | String | The status of the API group. NORMAL: The API group is normal. DELETE: The API group has been deleted. |

ns

| Name | Type | Description |
|---|---|---|
| BillingStatus | String | The billing status of the API group. NORMAL: The API group is normal. LOCKED: The API group is locked due to overdue payments. |
| IllegalStatus | String | The validity status of the API group. Valid values: NORMAL: The API group is normal. LOCKED: The API group is locked because it is not valid. |
| TrafficLimit | Integer | The upper QPS limit of the API group. The default value is 500. You can increase the upper limit by submitting an application. |
| CustomDomains | CustomDomain | The custom domain name information. |
| StageItems | StageInfo | The runtime environment information. |

Examples Sample request

```
http://apigateway.cn-hangzhou.aliyuncs.com?Action=DescribeApiGroup &GroupId=523e8dc7bbe04613b5b1d726c2a7889d &<Common request parameters>
```

Sample responses XML format ns

```xml
<DescribeApiGroupResponse>
    <RequestId>03442A3D-3B7D-434C-8A95-A5FEB989B519</RequestId>
    <GroupId>523e8dc7bbe04613b5b1d726c2a7889d</GroupId>
    <GroupName>NewWeather</GroupName>
    <SubDomain>927d50c0f2e54b359919923d908bb015-cn-hangzhou.alicloudapi.com</SubDomain>
    <Description>New weather informations. </Description>
    <CreatedTime>2016-08-01T06:53:02Z</CreatedTime>
    <ModifiedTime>2016-08-01T06:54:32Z</ModifiedTime>
    <RegionId>cn-hangzhou</RegionId>
    <Status>NORMAL</Status>
    <BillingStatus>NORMAL</BillingStatus>
    <IllegalStatus>NORMAL</IllegalStatus>
    <TrafficLimit>500</TrafficLimit>
    <CustomDomains>
        <CustomDomain>
            <DomainName>api.demo.com</DomainName>
            <CertificateId>6EF60BEC-0242-43AF-BB20-270359FB54A7</CertificateId>
            <CertificateName>myCertificate</CertificateName>
            <DomainNameResolution>RESOLVED</DomainNameResolution>
            <DomainStatus>BINDING</DomainStatus>
        </CustomDomain>
    </CustomDomains>
    <StageItems>
        <StageInfo>
            <StageId>123e8dc7bbe01613b5b1d726c2a7887e</StageId>
            <StageName>RELEASE</StageName>
            <Description>MYRELEASE</Description>
        </StageInfo>
        <StageInfo>
            <StageId>123e8dc7bbe01613b5b1d726c2a7888e</StageId>
            <StageName>TEST</StageName>
            <Description>MYTEST</Description>
        </StageInfo>
    </StageItems>
</DescribeApiGroupResponse>
```

JSON format ns

```json
    "RequestId": "03442A3D-3B7D-434C-8A95-A5FEB989B519",
    "GroupId": "523e8dc7bbe04613b5b1d726c2a7889d",
    "GroupName": "NewWeather",
    "SubDomain": "927d50c0f2e54b359919923d908bb015-cn-hangzhou.alicloudapi.com",
    "Description": "New weather informations.",
    "CreatedTime": "2016-08-01T06:53:02Z",
    "ModifiedTime": "2016-08-01T06:54:32Z",
    "RegionId": "cn-hangzhou",
    "Status": "NORMAL",
    "BillingStatus": "NORMAL",
    "IllegalStatus": "NORMAL",
    "TrafficLimit": "500",
    "CustomDomains": {
      "CustomDomain": {
        "DomainName": "api.demo.com",
        "CertificateId": "6EF60BEC-0242-43AF-BB20-270359FB54A7",
        "CertificateName": "myCertificate",
        "DomainNameResolution": "RESOLVED",
        "DomainStatus": "BINDING"
```

`}` `},`

```json
    "StageItems": {
      "StageInfo": [
```

`{`

```json
          "StageId": "123e8dc7bbe01613b5b1d726c2a7887e",
          "StageName": "RELEASE",
          "Description": "MYRELEASE"
```

`},` `{`

```json
          "StageId": "123e8dc7bbe01613b5b1d726c2a7888e",
          "StageName": "TEST",
          "Description": "MYTEST"
```

`}` `]` `}` `}`

### 5.7 DescribeApiGroups

Description You can call this operation to query existing API groups and their basic information. This operation is intended for API providers. Request parameters

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeApiGroups. |

| A | PI Gateway |   |   | Developer Guide·API group operati n | o s |
|---|---|---|---|---|---|

| Name | Type | Required | Description |
|---|---|---|---|
| GroupId | String | No | The API group ID, which is generated by the system and globally unique. |
| GroupName | String | No | The name of the API group. |
| PageNumber | Integer | No | The specific page number that you want to query. The default value is 1. The starting number is 1. |
| PageSize | Integer | No | The number of rows per page. The maximum value is 100. The default value is 10. |

Response parameters

| Name | Type | Description |
|---|---|---|
| RequestId | String | The request ID. |
| TotalCount | Integer | The total number of rows. |
| PageNumber | Integer | The specified page number. |
| PageSize | Integer | The specified number of rows returned per page. |
| ApiGroupAttributes | ApiGroupAttribute | The returned group set. |

Examples Sample request

```
http://apigateway.cn-hangzhou.aliyuncs.com?Action=DescribeApiGroups &<Common request parameters>
```

Sample responses XML format ns

```xml
<DescribeApiGroupsResponse>
    <RequestId>D6E46F10-F26C-4AA0-BB69-FE2743D9AE62</RequestId>
    <TotalCount>2</TotalCount>
    <PageSize>10</PageSize>
    <PageNumber>1</PageNumber>
        <ApiGroupAttributes>
            <ApiGroupAttribute>
                <GroupId>be6d2abcc0dd4f749fc2d2edd6567164</GroupId>
                <GroupName>Traffic</GroupName>
                <SubDomain>be6d2abcc0dd4f749fc2d2edd6567164-cn-hangzhou.alicloudapi.com</
SubDomain>
                <Description>TrafficInformations. </Description>
                  <CreatedTime>2016-08-01T08:45:15Z</CreatedTime>
                  <ModifiedTime>2016-08-01T08:45:15Z</ModifiedTime>
                  <RegionId>cn-hangzhou</RegionId>
                  <TrafficLimit>500</TrafficLimit>
                  <BillingStatus>NORMAL</BillingStatus>
                  <IllegalStatus>NORMAL</IllegalStatus>
            </ApiGroupAttribute>
            <ApiGroupAttribute>
                <GroupId>927d50c0f2e54b359919923d908bb015</GroupId>
                <GroupName>NewWeather</GroupName>
                  <SubDomain>927d50c0f2e54b359919923d908bb015-cn-hangzhou.alicloudapi.com
</SubDomain>
                  <Description>NewWeatherInformations. </Description>
                  <CreatedTime>2016-08-01T06:54:32Z</CreatedTime>
                  <ModifiedTime>2016-08-01T06:54:32Z</ModifiedTime>
                  <RegionId>cn-hangzhou</RegionId>
                  <TrafficLimit>500</TrafficLimit>
                  <BillingStatus>NORMAL</BillingStatus>
                  <IllegalStatus>NORMAL</IllegalStatus>
            </ApiGroupAttribute>
        </ApiGroupAttributes>
</DescribeApiGroupsResponse>
```

JSON format ns

```json
    "RequestId": "D6E46F10-F26C-4AA0-BB69-FE2743D9AE62",
    "TotalCount": "2",
    "PageSize": "10",
    "PageNumber": "1",
    "ApiGroupAttributes": {
      "ApiGroupAttribute": [
```

`{`

```json
          "GroupId": "be6d2abcc0dd4f749fc2d2edd6567164",
          "GroupName": "Traffic",
          "SubDomain": "be6d2abcc0dd4f749fc2d2edd6567164-cn-hangzhou.alicloudapi.com",
          "Description": "TrafficInformations.",
          "CreatedTime": "2016-08-01T08:45:15Z",
          "ModifiedTime": "2016-08-01T08:45:15Z",
          "RegionId": "cn-hangzhou",
          "TrafficLimit": "500",
          "BillingStatus": "NORMAL",
          "IllegalStatus": "NORMAL"
```

`},` `{`

```json
          "GroupId": "927d50c0f2e54b359919923d908bb015",
          "GroupName": "NewWeather",
          "SubDomain": "927d50c0f2e54b359919923d908bb015-cn-hangzhou.alicloudapi.com",
          "Description": "NewWeatherInformations.",
          "CreatedTime": "2016-08-01T06:54:32Z",
          "ModifiedTime": "2016-08-01T06:54:32Z",
          "RegionId": "cn-hangzhou",
          "TrafficLimit": "500",
          "BillingStatus": "NORMAL",
          "IllegalStatus": "NORMAL"
```

`}` `]` `}` `}`

### 5.8 DescribeApiStage

Description You can call this operation to query details about a specified runtime environment of an API group. This operation is intended for API providers. Request parameters

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeApiStage. |
| GroupId | String | Yes | The ID of the API group. |
| StageId | String | Yes | The ID of the runtime environment. |

ns Response parameters Response paramet ers

| Name | Type | Description |
|---|---|---|
| RequestId | String | The request ID. |
| GroupID | String | The ID of the API group. |
| StageID | String | The ID of the runtime environment. |
| StageName | String | The name of the runtime environment. |
| Description | String | The description of the runtime environment. |
| CreatedTime | String | The creation time (UTC) of the runtime environment. |
| ModifiedTime | String | The last modification time (UTC) of the runtime environment. |
| Variables | VariableItem | The variable information. |

Examples Sample request

```
http://apigateway.cn-hangzhou.aliyuncs.com?Action=DescribeApiStage &GroupId=523e8dc7bbe04613b5b1d726c2a7889d &StageId=6EF60BEC-0242-43AF-BB20-270359FB54A7 &<Common request parameters>
```

Sample responses XML format ns

```xml
<DescribeApiStageResponse>
    <RequestId>03442A3D-3B7D-434C-8A95-A5FEB989B529</RequestId>
    <GroupId>523e8dc7bbe04613b5b1d726c2a7889d</GroupId>
    <StageID>123e8dc7bbe01613b5b1d726c2a7887e</StageID>
    <StageName>RELEASE</StageName>
    <Description>myRELEASE</Description>
    <CreatedTime>2016-08-01T06:53:02Z</CreatedTime>
    <ModifiedTime>2016-08-01T06:54:32Z</ModifiedTime>
    <Status>NORMAL</Status>
    <BillingStatus>NORMAL</BillingStatus>
    <IllegalStatus>NORMAL</IllegalStatus>
    <TrafficLimit>500</TrafficLimit>
    <Variables>
        <VariableItem>
            <VariableName>serverName</VariableName>
            <VariableValue>api.domain.com</VariableValue>
        </VariableItem>
        <VariableItem>
            <VariableName>version</VariableName>
            <VariableValue>v1.0</VariableValue>
        </VariableItem>
    </Variables>
</DescribeApiStageResponse>
```

JSON format `{`

```json
    "RequestId": "03442A3D-3B7D-434C-8A95-A5FEB989B529",
    "GroupId": "523e8dc7bbe04613b5b1d726c2a7889d",
    "StageID": "123e8dc7bbe01613b5b1d726c2a7887e",
    "StageName": "RELEASE",
    "Description": "myRELEASE",
    "CreatedTime": "2016-08-01T06:53:02Z",
    "ModifiedTime": "2016-08-01T06:54:32Z",
    "Status": "NORMAL",
    "BillingStatus": "NORMAL",
    "IllegalStatus": "NORMAL",
    "TrafficLimit": "500",
    "Variables": {
      "VariableItem": [
```

`{`

```json
          "VariableName": "serverName",
          "VariableValue": "api.domain.com"
```

`},` `{`

```json
          "VariableName": "version",
          "VariableValue": "v1.0"
```

`}` `]` `}` `}` ations

## 6 Domain name operations

### 6.1 SetDomain

Description You can call this operation to bind a custom domain name to a specified API group. This operation is intended for API providers. Before you bind an independent domain name to an API group, you must resolve the domain name. You can add a CNAME record to resolve the domain name to the second-level domain name of the group. Alternatively, you can add an A record to resolve the domain name to the IP address of the second-level domain name server. To bind the independent domain name of another group to the current group, you must resolve the independent domain name and then bind it to the current group. If HTTPS is used, you must also bind the SSL certificate and specify the CertificateName, CertificateBody, and PrivateKey parameters. You can then upload the SSL certificate. For more information, see SetDomainCertificate. Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to SetDomain. |
| GroupId | String | Yes | The ID of the API group to which the domain name is to be bound. This ID is generated by the system and is globally unique. |
| DomainName | String | Yes | The custom domain name. |
| CertificateName | String | No | The name of the SSL certificate. |
| CertificateBody | String | No | The certificate body. |
| PrivateKey | String | No | The private key of the certificate. |

Response parameters

| Parameter | Type | Description |
|---|---|---|
| RequestId | String | The ID of the request. |
| GroupID | String | The ID of the API group to which the domain name is bound. This ID is generated by the system and is globally unique. |
| DomainName | String | The custom domain name. |

| PI Gateway |   | Developer Guide·Domain name ope |
|---|---|---|

ations

| Parameter | Type | Description |
|---|---|---|
| SubDomain | String | The second-level domain name bound to the API group. This domain name is used to test API calls. |
| DomainBindingStatus | String | The binding status of the custom domain name. The value BINDING indicates that the domain name has been bound. |

Examples Sample request s

```
https://apigateway.cn-hangzhou.aliyuncs.com/?Action=SetDomain &GroupId=927d50c0f2e54b359919923d908bb015 &DomainName=api.demo.com &<Common request parameters>
```

Sample success responses XML format

```xml
<SetDomainResponse>
    <RequestId>6EF60BEC-0242-43AF-BB20-270359FB54A7</RequestId>
    <GroupId>927d50c0f2e54b359919923d908bb015</GroupId>
    <DomainName>api.demo.com</DomainName>
    <SubDomain>927d50c0f2e54b359919923d908bb015-cn-hangzhou.alicloudapi.com</SubDomain>
    <DomainBindingStatus>BINDING</DomainBindingStatus>
</SetDomainResponse>
```

JSON format `{`

```json
    "RequestId": "6EF60BEC-0242-43AF-BB20-270359FB54A7",
    "GroupId": "927d50c0f2e54b359919923d908bb015",
    "DomainName": "api.abcdef.com",
    "SubDomain": "927d50c0f2e54b359919923d908bb015-cn-hangzhou.alicloudapi.com",
    "DomainBindingStatus": "BINDING"
```

`}`

### 6.2 SetDomainCertificate

Description You can call this operation to upload an SSL certificate for a specific custom domain name. This operation is intended for API providers. The SSL certificate must match the custom domain name. HTTPS-based API services will be available after the SSL certificate has been bound. Request parameters ations

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to SetDomainCertificate. |
| GroupId | String | Yes | The ID of the API group that you want to add an SSL certificate to. This ID is generated by the system and globally unique. |
| DomainName | String | Yes | The custom domain name. |
| CertificateName | String | Yes | The SSL certificate name. |
| CertificateBody | String | Yes | The content of the SSL certificate. |
| CertificatePrivateKey | String | Yes | The private key of the SSL certificate. |

Response parameters

| Name | Type | Description |
|---|---|---|
| RequestId | String | The request ID. |

Examples Sample request ations

```
https://apigateway.cn-hangzhou.aliyuncs.com/?Action=SetDomainCertificate &GroupId=927d50c0f2e54b359919923d908bb015 &DomainName=api.demo.com &CertificateName＝test_cert &CertificateBody＝-----BEGIN CERTIFICATE----- MIICaTCCAdICCQDLDvXtNkCrHjANBgkqhkiG9w0BAQUFADB5MQswCQYDVQQGEwJD TjELMAkGA1UECBMCWkoxCzAJBgNVBAcTAkhaMQ0wCwYDVQQKEwR0ZXN0MQ0wCwYD VQQLEwR0ZXN0MRQwEgYDVQQDEwthcGkuaWxhZC5jbjEcMBoGCSqGSIb3DQEJARYN dGVzdEB0ZXN0LmNvbTAeFw0xNjAzMzEwMzMxMTBaFw0yNjAzMjkwMzMxMTBaMHkx CzAJBgNVBAYTAkNOMQswCQYDVQQIEwJaSjELMAkGA1UEBxMCSFoxDTALBgNVBAoT BHRlc3QxDTALBgNVBAsTBHRlc3QxFDASBgNVBAMTC2FwaS5pbGFkLmNuMRwwGgYJ KoZIhvcNAQkBFg10ZXN0QHRlc3QuY29tMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCB iQKBgQDFfPttxLedyMF+tk/9VIGIIQ90LEx6JwfuKX38aO8zlN3+KxU7kMXBLYN7 kB7yZDsHBo87wlxXXPg7FO+3HjEcWAy8FgBFNfrnLLjXEK23Lrkn/3AdVulQ+eEi oVfOokQ1PO7GYFZSo8UFvBzol2An/f2Sd/bey713/rIUVgUd7wIDAQABMA0GCSqG SIb3DQEBBQUAA4GBAAqj2TQ8jzbmN5IDM8fMOARKLQQK8qTgkrHMAMEq7PJwNRtK A05enhbgZKJVkYhYk5nccWb3XZuklm6KX/ImWM1zfxi9EjvdD6Xkvxd9RpdZwlod zu6LnGpfi0YFiIBY301sFp0ACPudUvE1tVckrqM/ONPNhHWEnkAT9DF84hEN -----END CERTIFICATE----- &CertificatePrivateKey＝-----BEGIN RSA PRIVATE KEY----- MIICXAIBAAKBgQDFfPttxLedyMF+tk/9VIGIIQ90LEx6JwfuKX38aO8zlN3+KxU7 kMXBLYN7kB7yZDsHBo87wlxXXPg7FO+3HjEcWAy8FgBFNfrnLLjXEK23Lrkn/3Ad VulQ+eEioVfOokQ1PO7GYFZSo8UFvBzol2An/f2Sd/bey713/rIUVgUd7wIDAQAB AoGAeBxKgvlYv5Mg8+MIBUhHO7b3wi1LGiPw882yfTiI+vM4jORBFqg3TgVTaWw/ FicVq3E23h6YsN2vb6eNH+8x6DtGGZFiaWqIubWGEFenct8GPnlNY6JnxDdLMoGT K0P0r4qMZD5gSRs4sGR/wcGdbCGvSaFrzEConLmsaSlgLTkCQQD5KVwvchG/pai0 o13LJ9F4TVSegt8roH6QO0SuEb4GiKqUlY+Q1+PIBMHS1VciBJGyAWreLJkZnfKK g80cDL6VAkEAyuiPBt4u9dc68qet9vgVAYBI95vyCvg2u+MdVJKFYKaqNEDXbeyV qsrlsJ46LCAsQiLpzdEyrOioGiW3yNo9cwJBAKkn0EMR0UToJcIFSy8aaFahQXqf 5P1MZ8BpzHXU68qpzA02AJLYTvdDa4dEeXRJ39QWrEQLySEgH0K0unJ5oIUCQDtp Ln+vTIa091CXYit+5f+jhTni0lL97GDFFhBuOllbU1irZ6iK7iOs9uXo3lWPMgZH XLfjuffAw3+sbYyEwhsCQEtkrLCYEi5PQ4Z2RjonIBWWgXs+hDkd6qe5QM4Asr5t SDX2p8U+SnvvzJ3HuLM2ZB3D8duKJHCrKwOjX7nlXHo= -----END RSA PRIVATE KEY----- &<Common request parameters>
```

Sample responses XML format

```xml
<SetDomainCertificateResponse>
    <RequestId>6EF60BEC-0242-43AF-BB20-270359FB54A7</RequestId>
</SetDomainCertificateResponse>
```

JSON format `{`

```json
    "RequestId": "6EF60BEC-0242-43AF-BB20-270359FB54A7",
```

`}`

### 6.3 DescribeDomain

ations You can call this operation to query details about the custom domain name bound to an API group. The details include the automatically assigned second-level domain name, custom domain name, and SSL certificate. This operation is intended for API providers. Request parameters

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeDomain. |
| GroupId | String | Yes | The ID of the API group to which the domain name to be queried is bound. This ID is generated by the system and globally unique. |
| DomainName | String | Yes | The custom domain name. |

Response parameters

| Name | Type | Description |
|---|---|---|
| RequestId | String | The request ID. |
| GroupID | String | The ID of the API group to which the deleted domain name is bound. This ID is generated by the system and globally unique. |
| DomainName | String | The custom domain name. |
| SubDomain | String | The second-level domain name automatically assigned to the API group. |
| CertificateId | String | The SSL certificate ID, which is automatically generated by the system. |
| CertificateName | String | The SSL certificate name. |
| CertificateBody | String | The content of the SSL certificate. |
| CertificatePrivateKey | String | The private key of the SSL certificate. |
| DomainBindingStatus | String | The binding status of the custom domain name. Valid values: BINDING: The domain name has been bound. BOUND: The domain name has not been bound. |

ations

| Name | Type | Description |
|---|---|---|
| DomainCNAMEStatus | String | The domain name resolution status. Valid values: RESOLVED: The domain name has been resolved. UNRESOLVED: The domain name has not been resolved. |

Examples Sample request

```
https://apigateway.cn-hangzhou.aliyuncs.com/?Action=DescribeDomain &GroupId=927d50c0f2e54b359919923d908bb015 &DomainName=api.demo.com &<Common request parameters>
```

Sample responses XML format

```xml
<DescribeDomainResponse>
    <RequestId>6EF60BEC-0242-43AF-BB20-270359FB54A7</RequestId>
    <GroupId>927d50c0f2e54b359919923d908bb015</GroupId>
    <SubDomain>927d50c0f2e54b359919923d908bb015-cn-hangzhou.alicloudapi.com</SubDomain>
    <DomainName>api.demo.com</DomainName>
    <CertificateId>6EF60BEC-0242-43AF-BB20-270359FB54A7</CertificateId>
    <CertificateName>myCertificate</CertificateName>
    <CertificateBody>.. </CertificateBody>
    <CertificatePrivateKey>.. </CertificatePrivateKey>
    <DomainBindingStatus>BINDING</DomainBindingStatus>
    <DomainCNAMEStatus>RESOLVED</DomainCNAMEStatus>
</DescribeDomainResponse>
```

JSON format `{`

```json
    "RequestId": "6EF60BEC-0242-43AF-BB20-270359FB54A7",
    "GroupId": "927d50c0f2e54b359919923d908bb015",
    "SubDomain": "927d50c0f2e54b359919923d908bb015-cn-hangzhou.alicloudapi.com",
    "DomainName": "api.demo.com",
    "CertificateId":"6EF60BEC-0242-43AF-BB20-270359FB54A7",
    "CertificateName": "myCertificate",
    "CertificateBody":"..",
    "CertificatePrivateKey":"..",
    "DDomainBindingStatus": "BINDING",
    "DomainCNAMEStatus": "RESOLVED"
```

`}`

### 6.4 DeleteDomain

ations You can call this operation to unbind the custom domain name from a specified API group. This operation is intended for API providers. If the specified domain name does not exist, a successful response will still appear. Unbinding the domain name of an API group will affect acces to the APIs in the group. Exercise caution when using this operation. Request parameters

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DeleteDomain. |
| GroupId | String | Yes | The ID of the API group to which the domain name to be deleted is bound. This ID is generated by the system and globally unique. |
| DomainName | String | Yes | The custom domain name. |

Response parameters

| Name | Type | Description |
|---|---|---|
| RequestId | String | The request ID. |

Examples Sample request

```
https://apigateway.cn-hangzhou.aliyuncs.com/?Action=DeleteDomain &GroupId=927d50c0f2e54b359919923d908bb015 &DomainName=api.demo.com &<Common request parameters>
```

Sample responses XML format

```xml
<DeleteDomainResponse>
    <RequestId>6EF60BEC-0242-43AF-BB20-270359FB54A7</RequestId>
</DeleteDomainResponse>
```

JSON format `{`

```json
    "RequestId": "6EF60BEC-0242-43AF-BB20-270359FB54A7"
```

`}`

### 6.5 DeleteDomainCertificate

ations p You can call this operation to delete the SSL certificate of a specific domain name. This operation is intended for API providers. If the specified SSL certificate does not exist, a successful response will still appear. If the specified API group does not exist, the InvalidGroupId.NotFound error is returned. HTTPS access is not supported after the SSL certificate has been deleted. Exercise caution when using this API. Request parameters

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DeleteDomainCertificate. |
| GroupId | String | Yes | The ID of the API group containing the SSL certificate that you want to delete. This ID is generated by the system and globally unique. |
| DomainName | String | Yes | The custom domain name. |
| CertificateId | String | Yes | The ID of the SSL certificate that you want to delete. It is automatically generated by the system and globally unique. |

Response parameters

| Name | Type | Description |
|---|---|---|
| RequestId | String | The request ID. |

Examples Sample request

```
https://apigateway.cn-hangzhou.aliyuncs.com/?Action=DeleteDomainCertificate &GroupId=927d50c0f2e54b359919923d908bb015 &DomainName=api.demo.com &CertificateId=6EF60BEC-0242-43AF-BB20-270359FB54A7 &<Common request parameters>
```

Sample responses XML format

```xml
<DeleteDomainCertificateResponse>
    <RequestId>6EF60BEC-0242-43AF-BB20-270359FB54A7</RequestId>
</DeleteDomainCertificateResponse>
```

JSON format ations

```json
    "RequestId": "6EF60BEC-0242-43AF-BB20-270359FB54A7"
```

## 7 API management operations

### 7.1 CreateApi

Description You can call this operation to create an API. This operation is intended for API providers. The name of each API within the same group must be unique. Each request path within the same group must be unique. A group can contain up to 200 APIs. The QPS limit on this operation is 50 per user. Request parameters

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to CreateApi. |
| GroupId | String | Yes | The ID of the API group that you want to create an API in. |
| ApiName | String | Yes | The name of the API that you want to create, which is unique within the API group. The name must be 4 to 50 characters in length. It must start with a letter and can contain letters, numbers, and underscores ( ). _ |
| Visibility | String | Yes | Indicates whether the API is public. Valid values: PUBLIC: Indicates the API is public. In Apsara Stack, this value is invalid and the visibility of all APIs is fixed as PRIVATE. PRIVATE: Indicates the API is private. |
| Description | String | Yes | The API description, which cannot exceed 180 characters. |

| Name | Type | Required | Description |
|---|---|---|---|
| AuthType | String | Yes | The API security authorization type. Valid values: APP: Only authorized applications can call the API. ANONYMOUS: The API can be called anonymously. In such a mode, you must note the following: Anyone who can obtain this API service information will have the permission to call this API. API Gateway does not authenticate callers and cannot set user-specific throttling policies. If you make this API public, set API-based throttling policies. We do not recommend making APIs wit h anonymous aut hent icat ion available in t he Alibaba Cloud Market place. API Gateway cannot bill callers separately or control the number of calls. Before you add a group containing such APIs to the Marketplace, we recommend that you move them to another group, set their Visibility to PRIVATE, or set their AuthType to APP. APPOPENID: The third-party OpenID Connect account authentication method is used, allowing only authorized applications to call the API. If this method is selected, the OpenIdConnectConfig parameter is required. |
| OpenIdConnectConfig | String | Yes | The OpenID Connect configuration items. For more information, see ApiAttributesType.md#OpenIdConnectConfi g. |
| RequestConfig | String | Yes | The configuration items for an API request sent by a consumer to API Gateway. For more information, see ApiAttributesType.md#RequestConfig. |
| ServiceConfig | String | Yes | The configuration items for an API request sent by API Gateway to a backend service. For more information, see ApiAttributesType.md#ServiceConfig. |
| RequestParameters | String | Yes | The parameter description for an API request sent by a consumer to API Gateway. For more information, see ApiAttributesType.md#RequestParamters. |

| PI Gateway |   |   | Developer Guide·API management operation |
|---|---|---|---|

| Name | Type | Required | Description |
|---|---|---|---|
| ServiceParameters | String | Yes | The parameter description for an API request sent by API Gateway to a backend service. For more information, see ApiAttributesType.md#ServiceParameters. |
| ServiceParametersMap | String | Yes | The mappings between parameters of a request sent by a consumer to API Gateway and parameters of a request sent by API Gateway to a backend service. For more information, see ApiAttributesType.md#ServiceParametersM ap. |
| ResultType | String | Yes | The format of the response from the backend service. Valid values: JSON, TEXT, BINARY, XML, and HTML. |
| ResultSample | String | Yes | The sample response from the backend service. |
| FailResultSample | String | No | The sample error response from the backend service. |
| ErrorCodeSamples | String | No | The sample error code returned by the backend service. For more information, see ApiAttributesType.md#ErrorCodeSamples. |

Response parameters

| Name | Type | Description |
|---|---|---|
| RequestId | String | The ID of the current API creation request. |
| ApiId | String | The ID of the API being created. |

Examples Sample request

```
https://ecs.aliyuncs.com/?Action=CreateApi &GroupId=08ae4aa0f95e4321849ee57f4e0b3077 &ApiName=ApiName &Visibility=PUBLIC &Description=Api description &AuthType=APP &RequestConfig={"RequestProtocol":"HTTP","RequestHttpMethod":"GET","RequestPath":"/v3/getUs erTest/[userId]","BodyFormat":"FORM","PostBodyDescription":""} &ServiceConfig={"ServiceProtocol":"HTTP","ServiceHttpMethod":"GET","ServiceAddress":"http:/ /www.customerdomain.com","ServiceTimeout":"1000","ServicePath":"/v3/getUserTest/[userId]"} &RequestParameters=[{"ParameterType":"Number","Required":"OPTIONAL","isHide":false,"ApiPara meterName":"age","DefaultValue":"20","DemoValue":"20","Description":"Age","MinValue":18,"Ma xValue":100,"Location":"Head"},{"ParameterType":"String","Required":"OPTIONAL","isHide":fal se,"ApiParameterName":"sex","DefaultValue":"boy","DemoValue":"boy","Description":"Gender"," EnumValue":"boy,girl","Location":"Query"},{"ParameterType":"Number","Required":"REQUIRED"," isHide":false,"ApiParameterName":"userId","MaxLength":10,"MinValue":10000000,"MaxValue":100 000000,"Location":"Path"},{"ApiParameterName":"CaClientIp","ParameterLocation":{"name":"Hea d","orderNumber":0},"Location":"Head","ParameterType":"String","Required":"REQUIRED","Descr iption":"Client IP address"},{"ApiParameterName":"constance","ParameterLocation":{"name":"H ead","orderNumber":0},"Location":"Head","ParameterType":"String","Required":"REQUIRED","Def aultValue":"constance","Description":"constance"}] &ServiceParameters=[{"ServiceParameterName":"age","Location":"Head","Type":"Number","Parame terCatalog":"REQUEST"},{"ServiceParameterName":"sex","Location":"Query","Type":"String","Pa rameterCatalog":"REQUEST"},{"ServiceParameterName":"userId","Location":"Path","Type":"Numbe r","ParameterCatalog":"REQUEST"},{"ServiceParameterName":"clientIp","Location":"Head","Type ":"String","ParameterCatalog":"SYSTEM"},{"ServiceParameterName":"constance","Location":"Hea d","Type":"String","ParameterCatalog":"CONSTANT"}] &ServiceParametersMap=[{"ServiceParameterName":"age","RequestParameterName":"age"},{"Servic eParameterName":"sex","RequestParameterName":"sex"},{"ServiceParameterName":"userId","Reque stParameterName":"userId"},{"ServiceParameterName":"clientIp","RequestParameterName":"CaCli entIp"},{"ServiceParameterName":"constance","RequestParameterName":"constance"}] &ResultType=HTML &ResultSample=200 &<Common request parameters>
```

Sample responses XML format

```xml
<CreateApiResponse>
    <RequestId>CEF72CEB-54B6-4AE8-B225-F876FF7BA984</RequestId>
    <ApiId>8afff6c8c4c6447abb035812e4d66b65</ApiId>
</CreateApiResponse>
```

JSON format `{`

```json
    "RequestId":"6C87A26A-6A18-4B8E-8099-705278381A2C",
    "ApiId":"8afff6c8c4c6447abb035812e4d66b65"
```

`}`

### 7.2 ModifyApi

You can call this operation to modify the definition of a specified API. This operation is intended for API providers. When you modify an API name, ensure that the name of each API within the same group is unique. When you modify the request path, ensure that each request path within the same group is unique. The QPS limit on this operation is 50 per user. Request parameters

| Name | Type | Requ ired | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to ModifyApi. |
| GroupId | String | Yes | The ID of the specified API group. |
| ApiId | String | Yes | The ID of the API that you want to modify. |
| ApiName | String | Yes | The name of the API that you want to modify, which is unique within the API group. The name must be 4 to 50 characters in length. It must start with a letter and can contain letters, numbers, and underscores ( ). _ |
| Visibility | String | Yes | Indicates whether the API is public. Valid values: PUBLIC: Indicates the API is public. In Apsara Stack, this value is invalid and the visibility of all APIs is fixed as PRIVATE. PRIVATE: Indicates the API is private. |
| Description | String | Yes | The API description, which cannot exceed 180 characters. |
| AuthType | String | Yes | The API security authorization type. Valid values: APP: Only authorized applications can call the API. ANONYMOUS: The API can be called anonymously. In such a mode, you must note the following: Anyone who can obtain this API service information will have the permission to call this API. API Gateway does not authenticate callers and cannot set user-specific throttling policies. If you make this API public, set API-based throttling policies. We do not recommend making APIs wit h anonymous aut hent icat ion available in t he Alibaba Cloud Market place. API Gateway cannot bill callers separately or control the number of calls. Before you add a group containing such APIs to the Marketplace, we recommend that you move them to another group, set their Visibility to PRIVATE, or set their AuthType to APP. APPOPENID: The third-party OpenID Connect account authentication method is used, allowing only authorized applications to call the API. If this method is selected, the OpenIdConnectConfig parameter is required. |

| Name | Type | Requ ired | Description |
|---|---|---|---|
| OpenIdConnec tConfig | String | Yes | The OpenID Connect configuration items. For more information, see ApiAttributesType.md#OpenIdConnectConfig. |
| RequestConfi g | String | Yes | The configuration items for an API request sent by a consumer to API Gateway. For more information, see ApiAttributesType.md#RequestConfig. |
| ServiceConfig | String | Yes | The configuration items for an API request sent by API Gateway to a backend service. For more information, see ApiAttributesType.md#ServiceConfig. |
| RequestPara meters | String | Yes | The parameter description for an API request sent by a consumer to API Gateway. For more information, see ApiAttributesType.md#RequestParamters. |
| ServiceParam eters | String | Yes | The parameter description for an API request sent by API Gateway to a backend service. For more information, see ApiAttributesType.md#ServiceParameters. |
| ServiceParam etersMap | String | Yes | The mappings between parameters of a request sent by a consumer to API Gateway and parameters of a request sent by API Gateway to a backend service. For more information, see ApiAttributesType.md#ServiceParametersMap. |
| ResultType | String | Yes | The format of the response from the backend service. Valid values: JSON, TEXT, BINARY, XML, and HTML. |
| ResultSample | String | Yes | The sample response from the backend service. |
| FailResultSam ple | String | No | The sample error response from the backend service. |
| ErrorCodeSam ples | String | No | The sample error code returned by the backend service. For more information, see ApiAttributesType.md#ErrorCodeSamples. |

Response parameters

| Name | Type | Description |
|---|---|---|
| RequestId | String | The ID of the current API creation request. |

Examples Sample request

```
https://ecs.aliyuncs.com/?Action=ModifyApi &GroupId=08ae4aa0f95e4321849ee57f4e0b3077 &ApiName=ApiName &ApiId=8afff6c8c4c6447abb035812e4d66b65 &Visibility=PUBLIC &Description=Api description &AuthType=APP &RequestConfig={"RequestProtocol":"HTTP","RequestHttpMethod":"GET","RequestPath":"/v3/getUs erTest/[userId]","BodyFormat":"FORM","PostBodyDescription":""} &ServiceConfig={"ServiceProtocol":"HTTP","ServiceHttpMethod":"GET","ServiceAddress":"http:/ /www.customerdomain.com","ServiceTimeout":"1000","ServicePath":"/v3/getUserTest/[userId]"} &RequestParameters=[{"ParameterLocation":{"name":"Head","orderNumber":1},"ParameterType":"N umber","Required":"OPTIONAL","isHide":false,"ApiParameterName":"age","DefaultValue":"20","D emoValue":"20","Description":"Age","MinValue":18,"MaxValue":100,"Location":"Head"},{"Parame terLocation":{"name":"Query","orderNumber":2},"ParameterType":"String","Required":"OPTIONAL ","isHide":false,"ApiParameterName":"sex","DefaultValue":"boy","DemoValue":"boy","Descripti on":"Gender","EnumValue":"boy,girl","Location":"Query"},{"ParameterLocation":{"name":"Param eter Path","orderNumber":3},"ParameterType":"Number","Required":"REQUIRED","isHide":false," ApiParameterName":"userId","MaxLength":10,"MinValue":10000000,"MaxValue":100000000,"Locatio n":"Path"},{"ApiParameterName":"CaClientIp","ParameterLocation":{"name":"Head","orderNumber ":0},"Location":"Head","ParameterType":"String","Required":"REQUIRED","Description":"Client IP address"},{"ApiParameterName":"constance","ParameterLocation":{"name":"Head","orderNumbe r":0},"Location":"Head","ParameterType":"String","Required":"REQUIRED","DefaultValue":"cons tance","Description":"constance"}] &ServiceParameters=[{"ServiceParameterName":"age","Location":"Head","Type":"Number","Parame terCatalog":"REQUEST"},{"ServiceParameterName":"sex","Location":"Query","Type":"String","Pa rameterCatalog":"REQUEST"},{"ServiceParameterName":"userId","Location":"Path","Type":"Numbe r","ParameterCatalog":"REQUEST"},{"ServiceParameterName":"clientIp","Location":"Head","Type ":"String","ParameterCatalog":"SYSTEM"},{"ServiceParameterName":"constance","Location":"Hea d","Type":"String","ParameterCatalog":"CONSTANT"}] &ServiceParametersMap=[{"ServiceParameterName":"age","RequestParameterName":"age"},{"Servic eParameterName":"sex","RequestParameterName":"sex"},{"ServiceParameterName":"userId","Reque stParameterName":"userId"},{"ServiceParameterName":"clientIp","RequestParameterName":"CaCli entIp"},{"ServiceParameterName":"constance","RequestParameterName":"constance"}] &ResultType=HTML &ResultSample=200 &<Common request parameters>
```

Sample responses XML format

```xml
<ModifyApiResponse>
    <RequestId>CEF72CEB-54B6-4AE8-B225-F876FF7BA984</RequestId>
</ModifyApiResponse>
```

JSON format `{`

```json
    "RequestId":"6C87A26A-6A18-4B8E-8099-705278381A2C"
```

`}`

### 7.3 DeployApi

Description You can call this operation to publish an API to a specified runtime environment. This operation is intended for API providers. Only the API that you have defined and published to a runtime environment can be called. An API is published to a cluster in under 5 seconds. The QPS limit on this operation is 50 per user. Request parameters

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DeployApi. |
| GroupId | String | Yes | The ID of the API group. |
| ApiId | String | Yes | The ID of the API. |
| StageName | String | Yes | The name of the runtime environment. Valid values: RELEASE. TEST. |
| Description | String | Yes | The description of the current publication. |

Response parameters

| Name | Type | Description |
|---|---|---|
| RequestId | String | The request ID. |

Examples Sample request

```
https://apigateway.cn-qingdao.aliyuncs.com/?Action=DeployApi &GroupId=63be9002440b4778a61122f14c2b2bbb &ApiId=d6f679aeb3be4b91b3688e887ca1fe16 &StageName=release &Description=for_test1 &<Common request parameters>
```

Sample responses XML format

```xml
<DeployApiResponse>
    <RequestId>CEF72CEB-54B6-4AE8-B225-F876FF7BZ015</RequestId>
</DeployApiResponse>
```

JSON format `{`

```json
    "RequestId":"CEF72CEB-54B6-4AE8-B225-F876FF7BZ015"
```

`}`

### 7.4 SwitchApi

Description You can call this operation to switch the API definition running in the specified runtime environment to a historical version. This operation is intended for API providers. The historical version can be obtained through the DescribeHistoryApis API. Only APIs that have been published more than once have historical versions to switch to. This operation can only be performed on running APIs. Use caution when performing this operation because the operation cannot be undone after it has been completed and takes effect within 5 seconds. The switch operation is in essence a publish operation, and the reason for this operation must be provided. Request parameters

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to SwitchApi. |
| GroupId | String | Yes | The ID of the API group. |
| ApiId | String | Yes | The ID of the API. |
| StageName | String | Yes | The name of the runtime environment. Valid values: RELEASE. TEST. |
| HistoryVersion | String | Yes | The historical version you want to use. |
| Description | String | Yes | The description of the switch operation. |

Response parameters

| Name | Type | Description |
|---|---|---|
| RequestId | String | The request ID. |

Examples Sample request

```
https://apigateway.cn-qingdao.aliyuncs.com/?Action=SwitchApi &GroupId=63be9002440b4778a61122f14c2b2bbb &ApiId=d6f679aeb3be4b91b3688e887ca1fe16 &StageName=release &HistoryVersion=20160705104552292 &Description=for_demo &<Common request parameters>
```

Sample responses XML format

```xml
<SwitchApiResponse>
    <RequestId>CEF72CEB-54B6-4AE8-B225-F876FF7BZ001</RequestId>
</SwitchApiResponse>
```

JSON format `{`

```json
    "RequestId":"CEF72CEB-54B6-4AE8-B225-F876FF7BZ001"
```

`}`

### 7.5 AbolishApi

Description You can call this operation to unpublish a specified API from a specified runtime environment. This operation is intended for API providers and is the opposite of DeployApi. An API can be unpublished from a specified runtime environment in under 5 seconds. An unpublished API cannot be called in the specified runtime environment. Request parameters

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to AbolishApi. |
| GroupId | String | Yes | The ID of the API group. |
| ApiId | String | Yes | The ID of the API. |

| Name | Type | Required | Description |
|---|---|---|---|
| StageName | String | Yes | The name of the runtime environment. Valid values: RELEASE. TEST. |

Response parameters

| Name | Type | Description |
|---|---|---|
| RequestId | String | The request ID. |

Examples Sample request

```
https://apigateway.cn-qingdao.aliyuncs.com/?Action=AbolishApi &GroupId=63be9002440b4778a61122f14c2b2bbb &ApiId=d6f679aeb3be4b91b3688e887ca1fe16 &StageName=RELEASE &<Common request parameters>
```

Sample responses XML format

```xml
<AbolishApiResponse>
    <RequestId>CEF72CEB-54B6-4AE8-B225-F876FF7BZ016</RequestId>
</AbolishApiResponse>
```

JSON format `{`

```json
    "RequestId":"CEF72CEB-54B6-4AE8-B225-F876FF7BZ016"
```

`}`

### 7.6 DeleteApi

Description You can call this operation to delete the definition of a specified API. This operation is intended for API providers and cannot be undone after it has been completed. An API running in the runtime environment must be unpublished before being deleted. The QPS limit on this operation is 50 per user. Request parameters

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DeleteApi. |
| GroupId | String | Yes | The ID of the API group. |
| ApiId | String | Yes | The ID of the API. |

Response parameters

| Name | Type | Description |
|---|---|---|
| RequestId | String | The request ID. |

Examples Sample request

```
https://apigateway.cn-qingdao.aliyuncs.com/?Action=DeleteApi &GroupId=63be9002440b4778a61122f14c2b2bbb &ApiId=d6f679aeb3be4b91b3688e887ca1fe16 &<Common request parameters>
```

Sample responses XML format

```xml
<DeleteApiResponse>
    <RequestId>CEF72CEB-54B6-4AE8-B225-F876FF7BZ017</RequestId>
</DeleteApiResponse>
```

JSON format `{`

```json
    "RequestId":"CEF72CEB-54B6-4AE8-B225-F876FF7BZ017"
```

`}`

### 7.7 DescribeApi

Description You can call this operation to query API definitions. This operation is intended for API providers. This operation allows you to query the definition of a specified API. Request parameters

| Name | Type | Required | Description |
|---|---|---|---|

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeApi. |
| GroupId | String | Yes | The ID of the API group. |
| ApiId | String | Yes | The ID of the API. |

Response parameters

| Name | Type | Description |
|---|---|---|
| RequestId | String | The request ID. |
| RegionId | String | The region to which the API belongs. |
| ApiId | String | The ID of the API. |
| ApiName | String | The name of the API, which is unique in the group. |
| GroupId | String | The ID of the API group. |
| GroupName | String | The name of the API group. |
| Visibility | String | Indicates whether the API is public. Valid values: PUBLIC: indicates the API is public. In Apsara Stack, this value is invalid and the visibility of all APIs is fixed as PRIVATE. PRIVATE: indicates the API is private. |
| AuthType | String | The security authorization method. Valid values: APP: Only authorized applications can call the API. ANONYMOUS: The API can be called anonymously. In such a mode, you must note the following: Anyone who can obtain this API service information will have the permission to call this API. API Gateway does not authenticate callers and cannot set user-specific throttling policies. If you make this API public, set API-based throttling policies. We do not recommend making APIs wit h anonymous aut hent icat ion available in t he Alibaba Cloud Market place. API Gateway cannot bill callers separately or control the number of calls. Before you add a group containing such APIs to the Marketplace, we recommend that you move them to another group, set their Visibility to PRIVATE, or set their AuthType to APP. APPOPENID: The third-party OpenID Connect account authentication method is used, allowing only authorized applications to call the API. If this method is selected, the OpenIdConnectConfig parameter is required. |

| Name | Type | Description |
|---|---|---|
| ResultType | String | The format of the response from the backend service. Valid values: JSON, TEXT, BINARY, XML, and HTML. |
| ResultSample | String | The sample response returned by the backend service. |
| FailResultSamp le | String | The sample response returned when the backend service fails. |
| CreateTime | String | The creation time of the API. |
| ModifyTime | String | The last modification time of the API. |
| Description | String | The description of the API. |
| ErrorCodeSam ples | ErrorCodeSample | The sample error code returned by the backend service. For more information, see ApiAttributesType.md#ErrorCodeSamples. |
| SystemParame ters | SystemParamete r | The system parameters sent by API Gateway to a backend service. For more information, see ApiAttributesType.md#SystemParameters. |
| ConstantPara meters | ConstantParamet er | The constant parameters sent by API Gateway to a backend service. For more information, see ApiAttributesType.md#ConstantParameters. |
| RequestParam etersObject | RequestParamet er | The description of parameters of an API request sent by a caller to API Gateway. For more information, see ApiAttributesType.md#RequestParamters. |
| ServiceParame tersObject | ServiceParameter | The description of parameters of an API request sent by API Gateway to a backend service. For more information, see ApiAttributesType.md#ServiceParameters. |
| ParametersMa pObject | ServiceParameter Map | The mappings between parameters of a request sent by a caller to API Gateway and parameters of a request sent by API Gateway to a backend service. For more information, see ApiAttributesType.md#ServiceParametersMap. |
| DeployedInfos | DeployedInfo | The publishing status of the API. For more information, see ApiAttributesType.md#DeployedInfos. |
| RequestConfig | RequestConfig | The configuration items of an API request sent by a caller to API Gateway. For more information, see ApiAttributesType.md#RequestConfig. |
| ServiceConfig | ServiceConfig | The configuration items of an API request sent by API Gateway to a backend service. For more information, see ApiAttributesType.md#ServiceConfig. |
| OpenIdConnect Config | OpenIdConnectC onfig | The configuration items of the third-party OpenID Connect account authentication method. For more information, see ApiAttributesType.md#OpenIdConnectConfig. |

Examples Sample request

```
https://ecs.aliyuncs.com/?Action=DescribeApi &GroupId=08ae4aa0f95e4321849ee57f4e0b3077 &ApiId=8afff6c8c4c6447abb035812e4d66b65 &<Common request parameters>
```

Sample responses XML format

```xml
<DescribeApiResponse>
    <RequestId>D0FF585F-7966-40CF-BC60-75DB070B23D5</RequestId>
    <RegionId>cn-qingdao</RegionId>
    <Description>Api description</Description>
    <ApiName>ApiName</ApiName>
    <CreatedTime>2016-07-28T09:50:43Z</CreatedTime>
    <GroupName>ApiTest</GroupName>
    <ModifiedTime>2016-07-28T13:13:12Z</ModifiedTime>
    <ServiceParametersObject>
        <ServiceParam>
            <ServiceParameterName>age</ServiceParameterName>
            <Type>Number</Type>
            <Location>head</Location>
        </ServiceParam>
        <ServiceParam>
            <ServiceParameterName>sex</ServiceParameterName>
            <Type>String</Type>
            <Location>query</Location>
        </ServiceParam>
        <ServiceParam>
            <ServiceParameterName>userId</ServiceParameterName>
            <Type>Number</Type>
            <Location>path</Location>
        </ServiceParam>
        <ServiceParam>
            <ServiceParameterName>clientIp</ServiceParameterName>
            <Type>String</Type>
            <Location>head</Location>
        </ServiceParam>
        <ServiceParam>
            <ServiceParameterName>constance</ServiceParameterName>
            <Type>String</Type>
            <Location>head</Location>
        </ServiceParam>
    </ServiceParametersObject>
    <ConstantParameters>
        <ConstantParameter>
            <ServiceParameterName>constance</ServiceParameterName>
            <Description>constance</Description>
            <Location>HEAD</Location>
            <ConstantValue>constance</ConstantValue>
</ConstantParameter>
```

```xml
        </ConstantParameter>
    </ConstantParameters>
    <GroupId>08ae4aa0f95e4321849ee57f4e0b3077</GroupId>
    <SystemParameters>
        <SystemParameter>
            <ServiceParameterName>clientIp</ServiceParameterName>
            <Description>Client IP address</Description>
            <DemoValue>192.168.1.1</DemoValue>
            <Location>HEAD</Location>
            <ParameterName>CaClientIp</ParameterName>
        </SystemParameter>
    </SystemParameters>
    <RequestParametersObject>
        <RequestParam>
            <Required>OPTIONAL</Required>
            <MinValue>18</MinValue>
            <Description>Age</Description>
            <DemoValue>20</DemoValue>
            <ParameterType>NUMBER</ParameterType>
            <ApiParameterName>age</ApiParameterName>
            <DocShow>PUBLIC</DocShow>
            <DefaultValue>20</DefaultValue>
            <Location>HEAD</Location>
            <MaxValue>100</MaxValue>
            <DocOrder>0</DocOrder>
        </RequestParam>
        <RequestParam>
            <Required>OPTIONAL</Required>
            <Description>Gender</description>
            <DemoValue>boy</DemoValue>
            <ParameterType>STRING</ParameterType>
            <ApiParameterName>sex</ApiParameterName>
            <DocShow>PUBLIC</DocShow>
            <DefaultValue>boy</DefaultValue>
            <Location>QUERY</Location>
            <EnumValue>boy,girl</EnumValue>
            <DocOrder>0</DocOrder>
        </RequestParam>
        <RequestParam>
            <Required>REQUIRED</Required>
            <MinValue>10000000</MinValue>
            <ParameterType>NUMBER</ParameterType>
            <ApiParameterName>userId</ApiParameterName>
            <DocShow>PUBLIC</DocShow>
            <Location>regionid</Location>
            <MaxValue>100000000</MaxValue>
            <DocOrder>0</DocOrder>
        </RequestParam>
    </RequestParametersObject>
    <DeployedInfos>
        <DeployedInfo>
            <DeployedStatus>NONDEPLOYED</DeployedStatus>
            <StageName>TEST</StageName>
        </DeployedInfo>
<DeployedInfo>
```

```xml
        <DeployedInfo>
            <DeployedStatus>NONDEPLOYED</DeployedStatus>
            <StageName>RELEASE</StageName>
        </DeployedInfo>
    </DeployedInfos>
    <ServiceConfig>
        <ServiceProtocol>HTTP</ServiceProtocol>
        <ServiceTimeout>1000</ServiceTimeout>
        <ServiceAddress>http://www.customerdomain.com</ServiceAddress>
        <ServicePath>/v3/getUserTest/[userId]</ServicePath>
        <ServiceHttpMethod>GET</ServiceHttpMethod>
        <Mock>FALSE</Mock>
    </ServiceConfig>
    <RequestId>D0FF585F-7966-40CF-BC60-75DB070B23D5</RequestId>
    <RegionId>cn-qingdao</RegionId>
    <RequestConfig>
        <RequestHttpMethod>GET</RequestHttpMethod>
        <RequestProtocol>HTTP</RequestProtocol>
        <RequestPath>/v3/getUserTest/[userId]</RequestPath>
    </RequestConfig>
    <Visibility>PUBLIC</Visibility>
    <ParametersMapObject>
        <ServiceParameterMap>
            <ServiceParameterName>sex</ServiceParameterName>
            <RequestParameterName>sex</RequestParameterName>
        </ServiceParameterMap>
        <ServiceParameterMap>
            <ServiceParameterName>age</ServiceParameterName>
            <RequestParameterName>age</RequestParameterName>
        </ServiceParameterMap>
        <ServiceParameterMap>
            <ServiceParameterName>userId</ServiceParameterName>
            <RequestParameterName>userId</RequestParameterName>
        </ServiceParameterMap>
    </ParametersMapObject>
    <ErrorCodeSamples>
        <ErrorCodeSample>
            <Code>400</Code>
            <Message>Missing the parameter UserId</Message>
            <Description>The UserId parameter is missing from the request</Description>
        </ErrorCodeSample>
    </ErrorCodeSamples>
    <ApiId>8afff6c8c4c6447abb035812e4d66b65</ApiId>
    <AuthType>APP</AuthType>
    <ResultType>HTML</ResultType>
    <ResultSample>200</ResultSample>
    <FailResultSample>400</FailResultSample>
    <OpenIdConnectConfig>
        <publicKey>EB1837F8693CCED0BF750B3AD48467BEB569E780A14591CF92</publicKey>
        <openIdApiType>IDTOKEN</openIdApiType>
        <publicKeyId>88483727556929326703309904351185815489</publicKeyId>
    </OpenIdConnectConfig>
</DescribeApiResponse>
```

JSON format

```json
    "RequestId":D0FF585F-7966-40CF-BC60-75DB070B23D5,
    "RegionId":cn-qingdao,
    "Description": "billingTest001",
    "ApiName": "billingTest001",
    "CreatedTime": "2016-07-01T09:18:20Z",
    "GroupName": "billingTest",
    "ModifiedTime": "2016-07-21T03:52:12Z",
    "ServiceParametersObject": {
        "ServiceParam": [
```

`{`

```json
                "ServiceParameterName": "headerParam",
                "Type": "String",
                "Location": "head"
```

`},` `{`

```json
                "ServiceParameterName": "queryparam",
                "Type": "String",
                "Location": "query"
```

`},` `{`

```json
                "ServiceParameterName": "NumberParam",
                "Type": "Number",
                "Location": "query"
```

`},` `{`

```json
                "ServiceParameterName": "type",
                "Type": "String",
                "Location": "path"
```

`},` `{`

```json
                "ServiceParameterName": "clientIp",
                "Type": "String",
                "Location": "head"
```

`},` `{`

```json
                "ServiceParameterName": "constantParam",
                "Type": "String",
                "Location": "query"
```

`}` `]` `},`

```json
    "ConstantParameters": {
        "ConstantParameter": [
```

`{`

```json
                "ServiceParameterName": "constantParam",
                "Description": "constant",
                "Location": "QUERY",
                "ConstantValue": "constant"
```

`]` `},` `"G`

```
Id" "43f3050b95469bb685bdd29571b1"
```

```json
    "GroupId": "4a3f3050b9c5469bb685bdd29e571be1",
    "SystemParameters": {
        "SystemParameter": [
                "ServiceParameterName": "clientIp",
                "Description": "Client IP address",
                "DemoValue": "192.168.1.1",
                "Location": "HEAD",
                "ParameterName": "CaClientIp"
```

`}` `]` `},`

```json
    "RequestParametersObject": {
        "RequestParam": [
```

`{`

```json
                "Required": "OPTIONAL",
                "Description": "head param",
                "DemoValue": "headparm",
                "ParameterType": "STRING",
                "ApiParameterName": "headerParam",
                "DocShow": "PUBLIC",
                "DefaultValue": "",
                "Location": "HEAD",
                "EnumValue": "head",
                "DocOrder": 0
```

`},` `{`

```json
                "Required": "REQUIRED",
                "ParameterType": "STRING",
                "ApiParameterName": "queryparam",
                "DocShow": "PUBLIC",
                "DefaultValue": "",
                "Location": "QUERY",
                "DocOrder": 0
```

`},` `{`

```json
                "Required": "OPTIONAL",
                "MinValue": 1,
                "Description": "number param",
                "DemoValue": "10",
                "ParameterType": "NUMBER",
                "ApiParameterName": "NumberParam",
                "DocShow": "PUBLIC",
                "DefaultValue": "10",
                "Location": "QUERY",
                "MaxValue": 100,
                "DocOrder": 0
```

`},` `{`

```json
                "Required": "REQUIRED",
                "ParameterType": "STRING",
                "ApiParameterName": "type",
                "DocShow": "PUBLIC",
                "Location": "PATH",
"DocOrder":0
```

```
                DocOrder: 0
```

`]` `},`

```json
    "DeployedInfos": {
        "DeployedInfo": [
```

`{`

```json
                "DeployedStatus": "NONDEPLOYED",
                "StageName": "TEST",
```

`},` `{`

```json
                "DeployedStatus": "DEPLOYED",
                "StageName": "RELEASE",
                "EffectiveVersion": "20160721115223375"
```

`}` `]` `},`

```json
    "ServiceConfig": {
        "ServiceProtocol": "HTTP",
        "ServiceTimeout": 10000,
        "ServiceAddress": "http://120.55.69.157:8080",
        "ServicePath": "/web/cloudapi/[type]",
        "ServiceHttpMethod": "POST",
        "Mock": "CLOSED"
```

`},`

```json
    "RequestId": "415F037A-94C2-4100-B17A-F3C514CA1391",
    "RegionId": "cn-qingdao",
    "RequestConfig": {
        "RequestHttpMethod": "POST",
        "RequestProtocol": "HTTP",
        "PostBodyDescription": "fwefwef",
        "BodyFormat": "STREAM",
        "RequestPath": "/api/billing/test/[type]"
```

`},`

```json
    "Visibility": "PUBLIC",
    "ParametersMapObject": {
        "ServiceParameterMap": [
```

`{`

```json
                "ServiceParameterName": "headerParam",
                "RequestParameterName": "headerParam"
```

`},` `{`

```json
                "ServiceParameterName": "queryparam",
                "RequestParameterName": "queryparam"
```

`},` `{`

```json
                "ServiceParameterName": "NumberParam",
                "RequestParameterName": "NumberParam"
```

`},` `{`

```json
                "ServiceParameterName": "type",
                "RequestParameterName": "type"
```

`]` `},` `},`

```json
    "ErrorCodeSamples": {
        "ErrorCodeSample": [
                "Code": "400",
                "Message": "Missing the parameter UserId",
                "Description": "The UserId parameter is missing from the request"
```

`}` `]` `},`

```json
    "ApiId": "e77fd9257b1d436a806fe23c649300a0",
    "AuthType": "APP",
    "ResultType": "JSON",
    "ResultSample": "fwef",
    "FailResultSample": "400",
    "OpenIdConnectConfig": {
        "publicKey": "EB1837F8693CCED0BF750B3AD48467BEB569E780A14591CF92",
        "openIdApiType": "IDTOKEN",
        "publicKeyId": "88483727556929326703309904351185815489"
```

`}` `}`

### 7.8 DescribeApiDoc

Description You can call this operation to query documentation of a specified API. For API callers, the specified API must be a public or authorized private API that has been published to a runtime environment. When you call this operation as an API caller, the service information, parameter definitions, and other details of the API you specify are returned. When you call this operation as an API provider, the definition of the specified API running in the specified runtime environment is returned. The returned definition takes effect in the runtime environment, and may be different from the definition of the API you modify. Before you call this operation as an API provider, ensure that the API to be queried is a public one or that your application has been authorized to call the API, because authentication on API callers is required. Request parameters

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeApiDoc. |
| GroupId | String | Yes | The ID of the API group. |
| ApiId | String | Yes | The ID of the API. |

| Name | Type | Required | Description |
|---|---|---|---|
| StageName | String | No | The name of the runtime environment. Valid values: RELEASE. TEST. If this parameter is not specified, the default value is release. |

Response parameters

| Name | Type | Description |
|---|---|---|
| RequestId | String | The request ID. |
| RegionId | String | The region to which the API belongs. |
| GroupId | String | The ID of the API group. |
| GroupName | String | The name of the API group. |
| StageName | String | The name of the runtime environment. Valid values: RELEASE. TEST. |
| ApiId | String | The ID of the API. |
| ApiName | String | The API name. |
| Description | String | The description of the API. |
| Visibility | String | Indicates whether the API is public. Valid values: PUBLIC and PRIVATE. |
| AuthType | String | The security authentication method. Valid values: APP, ANONYMOUS, and APPOPENID, indicating respectively Alibaba Cloud application authentication, anonymous authentication, and third-party OpenID Connect account authentication. |
| ResultType | String | The response type. |
| ResultSample | String | The sample response. |
| FailResultSample | String | The sample response returned when the backend service fails. |
| ErrorCodeSamples | ErrorCodeSampl e | The sample error code returned by the backend service. For more information, see ApiAttributesType.md#ErrorCodeSamples. |
| RequestConfig | RequestConfig | The returned API frontend definition information. It is an array consisting of RequestConfig data. |
| RequestParamete rs | RequestParamet er | The returned frontend input parameters in the API. It is an array consisting of RequestParameter data. |

Examples Sample request

```
https://apigateway.cn-qingdao.aliyuncs.com/?Action=DescribeApiDoc &GroupId=0009db9c828549768a200320714b8930 &ApiId=3b81fd160f5645e097cc8855d75a1cf6 &<Common request parameters>
```

Sample responses XML format

```xml
<DescribeApiDocResponse>
    <RequestId>CEF72CEB-54B6-4AE8-B225-F876FF7BZ014</RequestId>
    <RegionId>cn-qingdao</RegionId>
    <GroupId>0009db9c828549768a200320714b8930</GroupId>
    <GroupName>myGroup2</GroupName>
    <StageName>RELEASE</StageName>
    <ApiId>3b81fd160f5645e097cc8855d75a1cf6</ApiId>
    <ApiName>creatobject</ApiName>
    <Description>Create an object</Description>
    <Visibility>public</Visibility>
    <AuthType>APP</AuthType>
    <ResultType>application/json</ResultType>
    <ResultSample></ResultSample>
    <FailResultSample></FailResultSample>
    <ErrorCodeSamples>
        <ErrorCodeSample>
            <Code>400</Code>
            <Message>Missing the parameter UserId</Message>
            <Description>The UserId parameter is missing from the request</Description>
        </ErrorCodeSample>
    </ErrorCodeSamples>
    <RequestConfig>
        <RequestProtocol>HTTP</RequestProtocol>
        <RequestHttpMethod>GET</RequestHttpMethod>
        <RequestPath>/mypath/creatobject</RequestPath>
        <BodyFormat>FORM</BodyFormat>
        <PostBodyDescription>Object</PostBodyDescription>
    </RequestConfig>
    <RequestParameters>
        <RequestParameter>
            <ApiParameterName>RequestKey1</ApiParameterName>
            <Location>QUERY</Location>
            <ParameterType>String</ParameterType>
            <Required>REQUIRED</Required>
            <DefaultValue></DefaultValue>
            <DemoValue>demo1</DemoValue>
            <MaxValue></MaxValue>
            <MinValue></MinValue>
            <MaxLength>100</MaxLength>
            <MinLength>3</MinLength>
            <RegularExpression></RegularExpression>
<JsonScheme></JsonScheme>
```

```xml
            <JsonScheme></JsonScheme>
            <EnumValue></EnumValue>
            <DocShow>PUBLIC</DocShow>
            <DocOrder>1</DocOrder>
            <Description>Desc1</Description>
        </RequestParameter>
        <RequestParameter>
            <ApiParameterName>RequestKey2</ApiParameterName>
            <Location>QUERY</Location>
            <ParameterType>Number</ParameterType>
            <Required>OPTIONAL</Required>
            <DefaultValue></DefaultValue>
            <DemoValue>12</DemoValue>
            <MaxValue>120</MaxValue>
            <MinValue>100</MinValue>
            <MaxLength></MaxLength>
            <MinLength></MinLength>
            <RegularExpression></RegularExpression>
            <JsonScheme></JsonScheme>
            <EnumValue></EnumValue>
            <DocShow>PUBLIC</DocShow>
            <DocOrder>2</DocOrder>
            <Description>Desc2</Description>
        </RequestParameter>
    </RequestParameters>
</DescribeApiDocResponse>
```

JSON format `{`

```json
    "RequestId": "CEF72CEB-54B6-4AE8-B225-F876FF7BZ014",
    "RegionId": "cn-qingdao",
    "GroupId": "0009db9c828549768a200320714b8930",
    "GroupName": "myGroup2",
    "StageName": "RELEASE",
    "ApiId": "3b81fd160f5645e097cc8855d75a1cf6",
    "ApiName": "creatobject",
    "Description": "Create an object",
    "Visibility": "public",
    "AuthType": "APP",
    "ResultType": "application/json",
    "ResultSample": "200",
    "FailResultSample": "400",
    "ErrorCodeSamples": {
        "ErrorCodeSample": [
```

`{`

```json
                "Code": "400",
                "Message": "Missing the parameter UserId",
                "Description": "The UserId parameter is missing from the request"
```

`}` `]` `},`

```json
    "RequestConfig": {
      "RequestProtocol": "HTTP",
      "RequestHttpMethod": "GET",
```

```json
      "RequestPath": "/mypath/creatobject",
      "BodyFormat": "FORM",
      "PostBodyDescription": "Object"
```

`},`

```json
    "RequestParameters": {
      "RequestParameter": [
```

`{`

```json
          "ApiParameterName": "RequestKey1",
          "Location": "QUERY",
          "ParameterType": "String",
          "Required": "REQUIRED",
          "DemoValue": "demo1",
          "MaxLength": "100",
          "MinLength": "3",
          "DocShow": "PUBLIC",
          "DocOrder": "1",
          "Description": "Desc1"
```

`},` `{`

```json
          "ApiParameterName": "RequestKey2",
          "Location": "QUERY",
          "ParameterType": "Number",
          "Required": "OPTIONAL",
          "DemoValue": "12",
          "MaxValue": "120",
          "MinValue": "100",
          "DocShow": "PUBLIC",
          "DocOrder": "2",
          "Description": "Desc2"
```

`}` `]` `}` `}`

### 7.9 DescribeApis

Description You can call this operation to query the list of APIs. This operation is intended for API providers. The list of all APIs under the definition and their brief information are returned.

> **Note:** This API returns the most recently edited API definitions. These may be different from the definitions of those APIs currently published to the runtime environment. Request parameters


| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeApis. |

| Developer Guide·API m perations | anagement |   | API Gatewa |
|---|---|---|---|

| Name | Type | Required | Description |
|---|---|---|---|
| GroupId | String | No | The ID of the API group. |
| ApiId | String | No | The ID of the API. |
| ApiName | String | No | The name of the API. |
| PageSize | Integer | No | The number of rows per page. The maximum value is 100. The default value is 10. |
| PageNumber | Integer | No | The specific page number that you want to query. The default value is 1. The starting number is 1. |

Response parameters

| Name | Type | Description |
|---|---|---|
| RequestId | String | The request ID. |
| TotalCount | Integer | The total number of returned results. |
| PageNumber | Integer | The specified page number. |
| PageSize | Integer | The specified number of rows returned per page. |
| ApiSummarys | ApiSummary | The returned API definition. It is an array consisting of ApiSummary data. |

Examples Sample request

```
https://apigateway.cn-qingdao.aliyuncs.com/?Action=DescribeApis &ApiName=weather &pageSize=15 &pageNumber=3 &<Common request parameters>
```

Sample responses XML format

```xml
<DescribeApisResponse>
    <ApiSummarys>
        <ApiSummary>
            <RegionId>cn-qingdao</RegionId>
            <GroupId>63be9002440b4778a61122f14c2b2bbb</GroupId>
            <GroupName>myGroup3</GroupName>
            <ApiId>c076144d7878437b8f82fb85890ce6a0</ApiId>
            <ApiName>Query the list of objects</ApiName>
            <Visibility>public</Visibility>
            <Description>Query the list of objects by pages</Description>
            <CreatedTime>2016-06-20T18:18:25Z</CreatedTime>
            <ModifiedTime>2016-07-23T08:28:48Z</ModifiedTime>
        </ApiSummary>
        <ApiSummary>
            <RegionId>cn-qingdao</RegionId>
            <GroupId>1084f9034c744137901057206b39d2b6</GroupId>
            <GroupName>myGroup2</GroupName>
            <ApiId>5af418828f0344a3b588c0cc1331a3bc</ApiId>
            <ApiName>Create an object</ApiName>
            <Visibility>public</Visibility>
            <Description>Create an object</Description>
            <CreatedTime>2016-05-20T18:18:25Z</CreatedTime>
            <ModifiedTime>2016-07-23T08:28:48Z</ModifiedTime>
        </ApiSummary>
    </ApiSummarys>
    <PageNumber>3</PageNumber>
    <PageSize>15</PageSize>
    <TotalCount>32</TotalCount>
    <RequestId>CEF72CEB-54B6-4AE8-B225-F876FF7BZ002</RequestId>
</DescribeApisResponse>
```

JSON format

```json
    "ApiSummarys": {
      "ApiSummary": [
```

`{`

```json
          "RegionId": "cn-qingdao",
          "GroupId": "63be9002440b4778a61122f14c2b2bbb",
          "GroupName": "myGroup3",
          "ApiId": "c076144d7878437b8f82fb85890ce6a0",
          "ApiName": "Query the list of objects",
          "Visibility": "public",
          "Description": "Query the list of objects by pages",
          "CreatedTime": "2016-06-20T18:18:25Z",
          "ModifiedTime": "2016-07-23T08:28:48Z"
```

`},` `{`

```json
          "RegionId": "cn-qingdao",
          "GroupId": "1084f9034c744137901057206b39d2b6",
          "GroupName": "myGroup2",
          "ApiId": "5af418828f0344a3b588c0cc1331a3bc",
          "ApiName": "Create an object",
          "Visibility": "public",
          "Description": "Create an object",
          "CreatedTime": "2016-05-20T18:18:25Z",
          "ModifiedTime": "2016-07-23T08:28:48Z"
```

`}` `]` `},`

```json
    "PageNumber": "3",
    "PageSize": "15",
    "TotalCount": "32",
    "RequestId": "CEF72CEB-54B6-4AE8-B225-F876FF7BZ002"
```

`}`

### 7.10 DescribeApiHistory

Description You can call this operation to query the details of a specified historical version of a specified API definition. This operation is intended for API providers. API Gateway records the time and definition of an API every time the API is published. You can use the version number obtained from other operations to query definition details at a certain publication. Request parameters

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeApiHistory. |
| GroupId | String | Yes | The ID of the API group. |

| PI Gateway |   |   | Developer Guide·API management operation |
|---|---|---|---|

| Name | Type | Required | Description |
|---|---|---|---|
| ApiId | String | Yes | The ID of the API. |
| StageName | String | Yes | The name of the runtime environment. Valid values: RELEASE. TEST. |
| HistoryVersion | String | Yes | The specified historical version number that you want to query. This can be obtained through the DescribeHistoryApis API. |

Response parameters

| Name | Type | Description |
|---|---|---|
| RequestId | String | The request ID. |
| RegionId | String | The region to which the API belongs. |
| GroupId | String | The ID of the API group. |
| GroupName | String | The name of the API group. |
| StageName | String | The name of the runtime environment. Valid values: RELEASE. TEST. |
| ApiId | String | The ID of the API. |
| ApiName | String | The name of the API. |
| Description | String | The description of the API. |
| HistoryVersion | String | The version of the API definition. |
| Status | String | Indicates whether the API of the corresponding version is valid. Valid values: ENABLE (valid) and DISABLE (invalid). |
| Visibility | String | Indicates whether the API is public. Valid values: PUBLIC and PRIVATE. |
| AuthType | String | The security authentication method. Valid values: APP, ANONYMOUS, and APPOPENID, indicating respectively Alibaba Cloud application authentication, anonymous authentication, and third-party OpenID Connect account authentication. |
| ResultType | String | The response type. |
| ResultSample | String | The sample response. |
| FailResultSamp le | String | The sample response returned when the backend service fails. |

| Developer Guide·A perations | PI management | API Gatewa |
|---|---|---|

| Name | Type | Description |
|---|---|---|
| DeployedTime | String | The publishing time (UTC) of the API. |
| ErrorCodeSam ples | ErrorCodeSam ple | The sample error code returned by the backend service. For more information, see ApiAttributesType.md#ErrorCodeSamples. |
| RequestConfig | RequestConfi g | The returned API frontend definition information. It is an array consisting of RequestConfig data under a definition. |
| ServiceConfig | ServiceConfig | The returned information on the backend service called through the API. It is an array consisting of ServiceConfig data. |
| SystemParame ters | SystemParam eter | The returned system parameters input when a backend service is called through the API. It is an array consisting of SystemParameter data. |
| ConstantPara meters | ConstantPara meter | The returned constant parameters input when a backend service is called through the API. It is an array consisting of ConstantParameter data. |
| RequestParam eters | RequestPara meter | The returned frontend input parameters in the API. It is an array consisting of RequestParameter data. |
| ServiceParame ters | ServiceParam eter | The returned constant parameters input when a backend service is called through the API. It is an array consisting of ServiceParameter data. |
| ServiceParame tersMap | ServiceParam eterMap | The returned mappings between frontend and backend parameters in the API. It is an array consisting of ServiceParameterMap data. |
| OpenIdConnect Config | OpenIdConnec tConfig | The configuration items of the third-party OpenID Connect account authentication method. For more information, see ApiAttributesType.md#OpenIdConnectConfig. |

Examples Sample request

```
https://apigateway.cn-qingdao.aliyuncs.com/?Action=DescribeApiHistory &GroupId=0009db9c828549768a200320714b8930 &ApiId=3b81fd160f5645e097cc8855d75a1cf6 &StageName=RELEASE &HistoryVersion=20160314220059844 &<Common request parameters>
```

Sample responses XML format

```xml
<DescribeApiHistoryResponse>
    <RequestId>CEF72CEB-54B6-4AE8-B225-F876FF7BZ004</RequestId>
    <RegionId>cn-qingdao</RegionId>
    <GroupId>0009db9c828549768a200320714b8930</GroupId>
    <GroupName>myGroup2</GroupName>
    <StageName>RELEASE</StageName>
```

`g` `/` `g`

```xml
    <ApiId>3b81fd160f5645e097cc8855d75a1cf6</ApiId>
    <ApiName>creatobject</ApiName>
    <Description>Create an object</Description>
    <HistoryVersion>20160314220059844</HistoryVersion>
    <Status>DISABLE</Status>
    <Visibility>public</Visibility>
    <AuthType>APP</AuthType>
    <ResultType>application/json</ResultType>
    <ResultSample></ResultSample>
    <FailResultSample></FailResultSample>
    <DeployedTime>2016-07-23T08:28:48Z</DeployedTime>
    <RequestConfig>
        <RequestProtocol>HTTP</RequestProtocol>
        <RequestHttpMethod>GET</RequestHttpMethod>
        <RequestPath>/mypath/creatobject</RequestPath>
        <BodyFormat>FORM</BodyFormat>
        <PostBodyDescription>Object</PostBodyDescription>
    </RequestConfig>
    <ServiceConfig>
        <ServiceProtocol>HTTP/HTTPS</ServiceProtocol>
        <ServiceAddress>http://api.a.com:8080</ServiceAddress>
        <ServiceHttpMethod>GET</ServiceHttpMethod>
        <ServicePath>/object/add</ServicePath>
        <ServiceTimeout>2000</ServiceTimeout>
    </ServiceConfig>
    <SystemParameters>
        <SystemParameter>
            <ParameterName>CaRequestId</ParameterName>
            <ServiceParameterName>RequestId</ServiceParameterName>
            <Location>HEAD</Location>
            <DemoValue>0A964636-F7A3-4F1A-92D7-135584A6397F</DemoValue>
            <Description>Request ID</Description>
        </SystemParameter>
        <SystemParameter>
            <ParameterName>CaAppId</ParameterName>
            <ServiceParameterName>AppId</ServiceParameterName>
            <Location>QUERY</Location>
            <DemoValue>0A964636-F7A3-4F1A-92D7-135584A6398F</DemoValue>
            <Description>Requester application ID</Description>
        </SystemParameter>
    </SystemParameters>
    <ConstantParameters>
        <ConstantParameter>
            <ServiceParameterName>ConstantKey1</ServiceParameterName>
            <ConstantValue>helloworld</ConstantValue>
            <Location>QUERY</Location>
            <Description>Desc</Description>
        </ConstantParameter>
    </ConstantParameters>
    <RequestParameters>
        <RequestParameter>
            <ApiParameterName>RequestKey1</ApiParameterName>
            <Location>QUERY</Location>
            <ParameterType>String</ParameterType>
```

```xml
            <Required>REQUIRED</Required>
            <DefaultValue></DefaultValue>
            <DemoValue>demo1</DemoValue>
            <MaxValue></MaxValue>
            <MinValue></MinValue>
            <MaxLength>100</MaxLength>
            <MinLength>3</MinLength>
            <RegularExpression></RegularExpression>
            <JsonScheme></JsonScheme>
            <EnumValue></EnumValue>
            <DocShow>PUBLIC</DocShow>
            <DocOrder>1</DocOrder>
            <Description>Desc1</Description>
        </RequestParameter>
        <RequestParameter>
            <ApiParameterName>RequestKey2</ApiParameterName>
            <Location>QUERY</Location>
            <ParameterType>Number</ParameterType>
            <Required>OPTIONAL</Required>
            <DefaultValue></DefaultValue>
            <DemoValue>12</DemoValue>
            <MaxValue>120</MaxValue>
            <MinValue>100</MinValue>
            <MaxLength></MaxLength>
            <MinLength></MinLength>
            <RegularExpression></RegularExpression>
            <JsonScheme></JsonScheme>
            <EnumValue></EnumValue>
            <DocShow>PUBLIC</DocShow>
            <DocOrder>2</DocOrder>
            <Description>Desc2</Description>
        </RequestParameter>
    </RequestParameters>
    <ErrorCodeSamples>
        <ErrorCodeSample>
            <Code>400</Code>
            <Message>Missing the parameter UserId</Message>
            <Description>The UserId parameter is missing from the request</Description>
        </ErrorCodeSample>
    </ErrorCodeSamples>
    <ServiceParameters>
        <ServiceParameter>
            <ServiceParameterName>ServiceKey1</ServiceParameterName>
            <Location>QUERY</Location>
            <ParameterType>String</ParameterType>
        </ServiceParameter>
        <ServiceParameter>
            <ServiceParameterName>ServiceKey2</ServiceParameterName>
            <Location>QUERY</Location>
            <ParameterType>Number</ParameterType>
        </ServiceParameter>
    </ServiceParameters>
    <ServiceParametersMap>
        <ServiceParameterMap>
```

```xml
            <ServiceParameterName>RequestKey1</ServiceParameterName>
            <RequestParameterName>ServiceKey1</RequestParameterName>
        </ServiceParameterMap>
        <ServiceParameterMap>
            <ServiceParameterName>RequestKey2</ServiceParameterName>
            <RequestParameterName>ServiceKey2</RequestParameterName>
        </ServiceParameterMap>
    </ServiceParametersMap>
    <OpenIdConnectConfig>
        <publicKey>EB1837F8693CCED0BF750B3AD48467BEB569E780A14591CF92</publicKey>
        <openIdApiType>IDTOKEN</openIdApiType>
        <publicKeyId>88483727556929326703309904351185815489</publicKeyId>
    </OpenIdConnectConfig>
</DescribeApiHistoryResponse>
```

JSON format `{`

```json
    "RequestId": "CEF72CEB-54B6-4AE8-B225-F876FF7BZ004",
    "RegionId": "cn-qingdao",
    "GroupId": "0009db9c828549768a200320714b8930",
    "GroupName": "myGroup2",
    "StageName": "RELEASE",
    "ApiId": "3b81fd160f5645e097cc8855d75a1cf6",
    "ApiName": "creatobject",
    "Description": "Create an object",
    "HistoryVersion": "20160314220059844",
    "Status": "DISABLE",
    "Visibility": "public",
    "AuthType": "APP",
    "ResultType": "application/json",
    "ResultSample": "200",
    "FailResultSample": "400",
    "DeployedTime": "2016-07-23T08:28:48Z",
    "RequestConfig": {
      "RequestProtocol": "HTTP",
      "RequestHttpMethod": "GET",
      "RequestPath": "/mypath/creatobject",
      "BodyFormat": "FORM",
      "PostBodyDescription": "Object"
```

`},`

```json
    "ServiceConfig": {
      "ServiceProtocol": "HTTP/HTTPS",
      "ServiceAddress": "http://api.a.com:8080",
      "ServiceHttpMethod": "GET",
      "ServicePath": "/object/add",
      "ServiceTimeout": "2000"
```

`},`

```json
    "SystemParameters": {
      "SystemParameter": [
```

`{`

```json
          "ParameterName": "CaRequestId",
          "ServiceParameterName": "RequestId",
          "Location": "HEAD",
"DemoValue":"0A964636-F7A3-4F1A-92D7-135584A6397F"
```

```json
          DemoValue: 0A964636F7A34F1A92D7135584A6397F,
          "Description": "Request ID"
```

`},`

```json
          "ParameterName": "CaAppId",
          "ServiceParameterName": "AppId",
          "Location": "QUERY",
          "DemoValue": "0A964636-F7A3-4F1A-92D7-135584A6398F",
          "Description": "Requester application ID"
```

`}` `]` `},`

```json
    "ConstantParameters": {
      "ConstantParameter": {
        "ServiceParameterName": "ConstantKey1",
        "ConstantValue": "helloworld",
        "Location": "QUERY",
        "Description": "Desc"
```

`}` `},`

```json
    "RequestParameters": {
      "RequestParameter": [
```

`{`

```json
          "ApiParameterName": "RequestKey1",
          "Location": "QUERY",
          "ParameterType": "String",
          "Required": "REQUIRED",
          "DemoValue": "demo1",
          "MaxLength": "100",
          "MinLength": "3",
          "DocShow": "PUBLIC",
          "DocOrder": "1",
          "Description": "Desc1"
```

`},` `{`

```json
          "ApiParameterName": "RequestKey2",
          "Location": "QUERY",
          "ParameterType": "Number",
          "Required": "OPTIONAL",
          "DemoValue": "12",
          "MaxValue": "120",
          "MinValue": "100",
          "DocShow": "PUBLIC",
          "DocOrder": "2",
          "Description": "Desc2"
```

`}` `]` `},`

```json
    "ErrorCodeSamples": {
        "ErrorCodeSample": [
```

`{`

```json
                "Code": "400"
                "Message": "Missing the parameter UserId",
                "Description": "The UserId parameter is missing from the request"
```

`]` `},`

```json
    "ServiceParameters": {
      "ServiceParameter": [
```

`{`

```json
          "ServiceParameterName": "ServiceKey1",
          "Location": "QUERY",
          "ParameterType": "String"
```

`},` `{`

```json
          "ServiceParameterName": "ServiceKey2",
          "Location": "QUERY",
          "ParameterType": "Number"
```

`}` `]` `},`

```json
    "ServiceParametersMap": {
      "ServiceParameterMap": [
```

`{`

```json
          "ServiceParameterName": "RequestKey1",
          "RequestParameterName": "ServiceKey1"
```

`},` `{`

```json
          "ServiceParameterName": "RequestKey2",
          "RequestParameterName": "ServiceKey2"
```

`}` `]` `},`

```json
    "OpenIdConnectConfig": {
        "publicKey": "EB1837F8693CCED0BF750B3AD48467BEB569E780A14591CF92",
        "openIdApiType": "IDTOKEN",
        "publicKeyId": "88483727556929326703309904351185815489"
```

`}` `}`

### 7.11 DescribeApiHistories

Description You can call this operation to query the list of historical versions of a specified API. This operation is intended for API providers. Only APIs which have been published have a historical version record. This operation allows you to obtain the API historical versions which can be used to call other APIs. Request parameters

| Name | Type | Requ ired | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeApisHistories. |

| D o | eveloper Guide·A perations | PI management |   | API Gatewa | y |
|---|---|---|---|---|---|

| Name | Type | Requ ired | Description |
|---|---|---|---|
| GroupId | String | Yes | The ID of the API group. |
| ApiId | String | No | The ID of the API. |
| ApiName | String | No | The name of the API. |
| StageName | String | No | The name of the runtime environment. Valid values: RELEASE. TEST. |
| PageSize | Integer | No | The number of rows per page. The maximum value is 100. The default value is 10. |
| PageNumber | Integer | No | The specific page number that you want to query. The default value is 1. The starting number is 1. |

Response parameters

| Name | Type | Description |
|---|---|---|
| RequestId | String | The request ID. |
| TotalCount | Integer | The total number of returned results. |
| PageNumber | Integer | The specified page number. |
| PageSize | Integer | The specified number of rows returned per page. |
| ApiHisItems | ApiHisItem | The returned API information. It is an array consisting of ApiHisItem data. |

Examples Sample request

```
https://apigateway.cn-qingdao.aliyuncs.com/?Action=DescribeApiHistories &ApiName=weather &pageSize=15 &pageNumber=3 &<Common request parameters>
```

Sample responses XML format

```xml
<DescribeApiHistoriesResponse>
    <ApiHisItems>
        <ApiHisItem>
            <RegionId>cn-qingdao</RegionId>
            <GroupId>63be9002440b4778a61122f14c2b2bbb</GroupId>
            <GroupName>myGroup3</GroupName>
            <ApiId>c076144d7878437b8f82fb85890ce6a0</ApiId>
            <ApiName>Query the list of objects</ApiName>
            <StageName>release</StageName>
            <HistoryVersion>20160705104552292</HistoryVersion>
            <Status>DISABLE</Status>
            <Description>Query the list of objects by pages</Description>
            <DeployedTime>2016-07-23T08:28:48Z</DeployedTime>
        </ApiHisItem>
        <ApiHisItem>
            <RegionId>cn-qingdao</RegionId>
            <GroupId>1084f9034c744137901057206b39d2b6</GroupId>
            <GroupName>myGroup2</GroupName>
            <ApiId>5af418828f0344a3b588c0cc1331a3bc</ApiId>
            <ApiName>Create an object</ApiName>
            <StageName>release</StageName>
            <HistoryVersion>20160705104552393</HistoryVersion>
            <Status>DISABLE</Status>
            <Description>Create an object</Description>
            <DeployedTime>2016-07-20T08:28:48Z</DeployedTime>
        </ApiHisItem>
    </ApiHisItems>
    <PageNumber>3</PageNumber>
    <PageSize>15</PageSize>
    <TotalCount>32</TotalCount>
    <RequestId>CEF72CEB-54B6-4AE8-B225-F876FF7BZ003</RequestId>
</DescribeApiHistoriesResponse>
```

JSON format

```json
    "ApiHisItems": {
        "ApiHisItem": [
```

`{`

```json
                "RegionId": "cn-qingdao",
                "GroupId": "63be9002440b4778a61122f14c2b2bbb",
                "GroupName": "myGroup3",
                "ApiId": "c076144d7878437b8f82fb85890ce6a0",
                "ApiName": "Query the list of objects",
                "StageName": "release",
                "HistoryVersion": "20160705104552292",
                "Status": "DISABLE",
                "Description": "Query the list of objects by pages",
                "DeployedTime": "2016-07-23T08:28:48Z"
```

`},` `{`

```json
                "RegionId": "cn-qingdao",
                "GroupId": "1084f9034c744137901057206b39d2b6",
                "GroupName": "myGroup2",
                "ApiId": "5af418828f0344a3b588c0cc1331a3bc",
                "ApiName": "Create an object",
                "StageName": "release",
                "HistoryVersion": "20160705104552393",
                "Status": "DISABLE",
                "Description": "Create an object",
                "DetachedTime": "2014-07-23T08:28:48Z",
```

`}` `]` `},`

```json
    "PageNumber": 3,
      "PageSize": 15,
      "TotalCount": 32,
    "RequestId":"CEF72CEB-54B6-4AE8-B225-F876FF7BZ003"
```

`}`

### 7.12 DescribeDeployedApi

Description You can call this operation to query the running definition of an API in a specified runtime environment. This operation is intended for API providers. This operation allows you to query the API definition that has been published to and is running in a specified environment. This definition may be different from the API definition being modified. A modified API definition can overwrite the definition running in a runtime environment only after the modified definition is published to the runtime environment. Request parameters

| Name | Type | Required | Description |
|---|---|---|---|

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeDeployedApi. |
| GroupId | String | Yes | The ID of the API group. |
| ApiId | String | Yes | The ID of the API. |
| StageName | String | Yes | The name of the runtime environment. Valid values: RELEASE. TEST. |

Response parameters

| Name | Type | Description |
|---|---|---|
| RequestId | String | The request ID. |
| RegionId | String | The region to which the API belongs. |
| GroupId | String | The ID of the API group. |
| GroupName | String | The name of the API group. |
| StageName | String | The name of the runtime environment. Valid values: RELEASE. TEST. |
| ApiId | String | The ID of the API. |
| ApiName | String | The name of the API. |
| Description | String | The description of the API. |
| Visibility | String | Indicates whether the API is public. Valid values: PUBLIC and PRIVATE. |
| AuthType | String | The security authentication method. Valid values: APP, ANONYMOUS, and APPOPENID, indicating respectively Alibaba Cloud application authentication, anonymous authentication, and third-party OpenID Connect account authentication. |
| ResultType | String | The response type. |
| ResultSample | String | The sample response. |
| FailResultSample | String | The sample response returned when the backend service fails. |
| DeployedTime | String | The publishing time (UTC) of the API. |

| D o | eveloper Guide·API ma perations | nagement | API Gatewa | y |
|---|---|---|---|---|

| Name | Type | Description |
|---|---|---|
| ErrorCodeSamples | ErrorCodeSample | The sample error code returned by the backend service. For more information, see ApiAttributesType.md#ErrorCodeSamples. |
| RequestConfig | RequestConfig | The returned API frontend definition information. It is an array consisting of RequestConfig data. |
| ServiceConfig | ServiceConfig | The returned information of the backend service called through the API. It is an array consisting of ServiceConfig data. |
| SystemParameters | SystemParameter | The returned system parameters input when a backend service is called through the API. It is an array consisting of SystemParameter data. |
| ConstantParameters | ConstantParameter | The returned constant parameters input when a backend service is called through the API. It is an array consisting of ConstantParameter data. |
| RequestParameters | RequestParameter | The returned frontend input parameters in the API. It is an array consisting of RequestParameter data. |
| ServiceParameters | ServiceParameter | The returned constant parameters input when a backend service is called through the API. It is an array consisting of ServiceParameter data. |
| ServiceParametersM ap | ServiceParameterM ap | The returned mappings between frontend and backend parameters in the API. It is an array consisting of ServiceParameterMap data. |
| OpenIdConnectConfi g | OpenIdConnectConf ig | The configuration items of the third-party OpenID Connect account authentication method. For more information, see ApiAttributesType.md#OpenIdConnectConfig. |

Examples Sample request

```
https://apigateway.cn-qingdao.aliyuncs.com/?Action=DescribeDeployedApi &GroupId=0009db9c828549768a200320714b8930 &ApiId=3b81fd160f5645e097cc8855d75a1cf6 &StageName=RELEASE &<Common request parameters>
```

Sample responses XML format

```xml
<DescribeDeployedApiResponse>
    <RequestId>CEF72CEB-54B6-4AE8-B225-F876FF7BZ004</RequestId>
    <RegionId>cn-qingdao</RegionId>
    <GroupId>0009db9c828549768a200320714b8930</GroupId>
    <GroupName>myGroup2</GroupName>
```

```xml
    <StageName>RELEASE</StageName>
    <ApiId>3b81fd160f5645e097cc8855d75a1cf6</ApiId>
    <ApiName>creatobject</ApiName>
    <Description>Create an object</Description>
    <Visibility>public</Visibility>
    <AuthType>APP</AuthType>
    <ResultType>application/json</ResultType>
    <ResultSample></ResultSample>
    <FailResultSample></FailResultSample>
    <DeployedTime>2016-07-23T08:28:48Z</DeployedTime>
    <RequestConfig>
        <RequestProtocol>HTTP</RequestProtocol>
        <RequestHttpMethod>GET</RequestHttpMethod>
        <RequestPath>/mypath/creatobject</RequestPath>
        <BodyFormat>FORM</BodyFormat>
        <PostBodyDescription>Object</PostBodyDescription>
    </RequestConfig>
    <ServiceConfig>
        <ServiceProtocol>HTTP/HTTPS</ServiceProtocol>
        <ServiceAddress>http://api.a.com:8080</ServiceAddress>
        <ServiceHttpMethod>GET</ServiceHttpMethod>
        <ServicePath>/object/add</ServicePath>
        <ServiceTimeout>2000</ServiceTimeout>
        <Mock>FALSE</Mock>
    </ServiceConfig>
    <SystemParameters>
        <SystemParameter>
            <ParameterName>CaRequestId</ParameterName>
            <ServiceParameterName>RequestId</ServiceParameterName>
            <Location>HEAD</Location>
            <DemoValue>0A964636-F7A3-4F1A-92D7-135584A6397F</DemoValue>
            <Description>Request ID</Description>
        </SystemParameter>
        <SystemParameter>
            <ParameterName>CaAppId</ParameterName>
            <ServiceParameterName>AppId</ServiceParameterName>
            <Location>regionid</Location>
            <DemoValue>0A964636-F7A3-4F1A-92D7-135584A6398F</DemoValue>
            <Description>Requester application ID</Description>
        </SystemParameter>
    </SystemParameters>
    <ConstantParameters>
        <ConstantParameter>
            <ServiceParameterName>ConstantKey1</ServiceParameterName>
            <ConstantValue>helloworld</ConstantValue>
            <Location>regionid</Location>
            <Description>Test</Description>
        </ConstantParameter>
    </ConstantParameters>
    <RequestParameters>
        <RequestParameter>
            <ApiParameterName>RequestKey1</ApiParameterName>
            <Location>regionid</Location>
            <ParameterType>String</ParameterType>
```

```xml
            <Required>REQUIRED</Required>
            <DefaultValue></DefaultValue>
            <DemoValue>demo1</DemoValue>
            <MaxValue></MaxValue>
            <MinValue></MinValue>
            <MaxLength>100</MaxLength>
            <MinLength>3</MinLength>
            <RegularExpression></RegularExpression>
            <JsonScheme></JsonScheme>
            <EnumValue></EnumValue>
            <DocShow>PUBLIC</DocShow>
            <DocOrder>1</DocOrder>
            <Description>Desc1</Description>
        </RequestParameter>
        <RequestParameter>
            <ApiParameterName>RequestKey2</ApiParameterName>
            <Location>QUERY</Location>
            <ParameterType>Number</ParameterType>
            <Required>OPTIONAL</Required>
            <DefaultValue></DefaultValue>
            <DemoValue>12</DemoValue>
            <MaxValue>120</MaxValue>
            <MinValue>100</MinValue>
            <MaxLength></MaxLength>
            <MinLength></MinLength>
            <RegularExpression></RegularExpression>
            <JsonScheme></JsonScheme>
            <EnumValue></EnumValue>
            <DocShow>PUBLIC</DocShow>
            <DocOrder>2</DocOrder>
            <Description>Desc2</Description>
        </RequestParameter>
    </RequestParameters>
    <ServiceParameters>
        <ServiceParameter>
            <ServiceParameterName>ServiceKey1</ServiceParameterName>
            <Location>QUERY</Location>
            <ParameterType>String</ParameterType>
        </ServiceParameter>
        <ServiceParameter>
            <ServiceParameterName>ServiceKey2</ServiceParameterName>
            <Location>QUERY</Location>
            <ParameterType>Number</ParameterType>
        </ServiceParameter>
    </ServiceParameters>
    <ServiceParametersMap>
        <ServiceParameterMap>
            <ServiceParameterName>RequestKey1</ServiceParameterName>
            <RequestParameterName>ServiceKey1</RequestParameterName>
        </ServiceParameterMap>
        <ServiceParameterMap>
            <ServiceParameterName>RequestKey2</ServiceParameterName>
            <RequestParameterName>ServiceKey2</RequestParameterName>
        </ServiceParameterMap>
```

`/`

```xml
    </ServiceParametersMap>
    <ErrorCodeSamples>
        <ErrorCodeSample>
            <Code>400</Code>
            <Message>Missing the parameter UserId</Message>
            <Description>The UserId parameter is missing from the request</Description>
        </ErrorCodeSample>
    </ErrorCodeSamples>
    <OpenIdConnectConfig>
        <publicKey>EB1837F8693CCED0BF750B3AD48467BEB569E780A14591CF92</publicKey>
        <openIdApiType>IDTOKEN</openIdApiType>
        <publicKeyId>88483727556929326703309904351185815489</publicKeyId>
    </OpenIdConnectConfig>
</DescribeDeployedApiResponse>
```

JSON format `{`

```json
    "RequestId": "CEF72CEB-54B6-4AE8-B225-F876FF7BZ004",
    "RegionId": "cn-qingdao",
    "GroupId": "0009db9c828549768a200320714b8930",
    "GroupName": "myGroup2",
    "StageName": "RELEASE",
    "ApiId": "3b81fd160f5645e097cc8855d75a1cf6",
    "ApiName": "creatobject",
    "Description": "Create an object",
    "Visibility": "public",
    "AuthType": "APP",
    "ResultType": "application/json",
    "DeployedTime": "2016-07-23T08:28:48Z",
    "RequestConfig": {
      "RequestProtocol": "HTTP",
      "RequestHttpMethod": "GET",
      "RequestPath": "/mypath/creatobject",
      "BodyFormat": "FORM",
      "PostBodyDescription": "Object"
```

`},`

```json
    "ServiceConfig": {
      "ServiceProtocol": "HTTP/HTTPS",
      "ServiceAddress": "http://api.a.com:8080",
      "ServiceHttpMethod": "GET",
      "ServicePath": "/object/add",
      "ServiceTimeout": "2000",
      "Mock": "FALSE"
```

`},`

```json
    "SystemParameters": {
      "SystemParameter": [
```

`{`

```json
          "ParameterName": "CaRequestId",
          "ServiceParameterName": "C",
          "Location": "HEAD",
          "DemoValue": "0A964636-F7A3-4F1A-92D7-135584A6397F",
          "Description": "Request ID"
```

`},`

```json
          "ParameterName": "CaAppId",
          "ServiceParameterName": "AppId",
          "Location": "QUERY",
          "DemoValue": "0A964636-F7A3-4F1A-92D7-135584A6398F",
          "Description": "Requester application ID"
```

`}` `]` `},`

```json
    "ConstantParameters": {
      "ConstantParameter": {
        "ServiceParameterName": "ConstantKey1",
        "ConstantValue": "helloworld",
        "Location": "QUERY",
        "Description": "Desc"
```

`}` `},`

```json
    "RequestParameters": {
      "RequestParameter": [
```

`{`

```json
          "ApiParameterName": "RequestKey1",
          "Location": "QUERY",
          "ParameterType": "String",
          "Required": "REQUIRED",
          "DemoValue": "demo1",
          "MaxLength": "100",
          "MinLength": "3",
          "DocShow": "PUBLIC",
          "DocOrder": "1",
          "Description": "Desc1"
```

`},` `{`

```json
          "ApiParameterName": "RequestKey2",
          "Location": "QUERY",
          "ParameterType": "Number",
          "Required": "OPTIONAL",
          "DemoValue": "12",
          "MaxValue": "120",
          "MinValue": "100",
          "DocShow": "PUBLIC",
          "DocOrder": "2",
          "Description": "Desc2"
```

`}` `]` `},`

```json
    "ServiceParameters": {
      "ServiceParameter": [
```

`{`

```json
          "ServiceParameterName": "ServiceKey1",
          "Location": "QUERY",
          "ParameterType": "String"
```

`},`

```json
          "ServiceParameterName": "ServiceKey2",
          "Location": "QUERY",
```

```json
          "ParameterType": "Number"
```

`]` `},`

```json
    "ServiceParametersMap": {
      "ServiceParameterMap": [
```

`{`

```json
          "ServiceParameterName": "RequestKey1",
          "RequestParameterName": "ServiceKey1"
```

`},` `{`

```json
          "ServiceParameterName": "RequestKey2",
          "RequestParameterName": "ServiceKey2"
```

`}` `]` `},`

```json
    "ErrorCodeSamples": {
        "ErrorCodeSample": [
```

`{`

```json
                "Code": "400",
                "Message": "Missing the parameter UserId",
                "Description": "The UserId parameter is missing from the request"
```

`}` `]` `},`

```json
    "OpenIdConnectConfig": {
        "publicKey": "EB1837F8693CCED0BF750B3AD48467BEB569E780A14591CF92",
        "openIdApiType": "IDTOKEN",
        "publicKeyId": "88483727556929326703309904351185815489"
```

`}` `}`

### 7.13 DescribeDeployedApis

Description You can call this operation to query the list of APIs that have been published to and are running in a specified runtime environment. This operation is intended for API providers. Request parameters

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeDeployedApis. |
| GroupId | String | No | The ID of the API group. |

| Name | Type | Required | Description |
|---|---|---|---|
| StageName | String | Yes | The name of the runtime environment. Valid values: RELEASE. TEST. |
| ApiId | String | No | The ID of the API. |
| ApiName | String | No | The name of the API. |
| PageSize | Integer | No | The number of rows per page. The maximum value is 100. The default value is 10. |
| PageNumber | Integer | No | The specific page number that you want to query. The default value is 1. The starting number is 1. |

Response parameters

| Name | Type | Description |
|---|---|---|
| RequestId | String | The request ID. |
| TotalCount | Integer | The total number of returned results. |
| PageNumber | Integer | The specified page number. |
| PageSize | Integer | The specified number of rows returned per page. |
| DeployedApis | DeployedApiItem | The returned API information. It is an array consisting of DeployedApiItem data. |

Examples Sample request

```
https://apigateway.cn-qingdao.aliyuncs.com/?Action=DescribeDeployedApis &ApiName=weather &pageSize=15 &pageNumber=3 &<Common request parameters>
```

Sample responses XML format

```xml
<DescribeDeployedApisResponse>
    <DeployedApis>
        <DeployedApiItem>
            <RegionId>cn-qingdao</RegionId>
            <GroupId>63be9002440b4778a61122f14c2b2bbb</GroupId>
            <GroupName>myGroup3</GroupName>
            <ApiId>c076144d7878437b8f82fb85890ce6a0</ApiId>
            <ApiName>Query the list of objects</ApiName>
            <StageName>release</StageName>
            <Visibility>public</Visibility>
            <Description>Query the list of objects by pages</Description>
            <DeployedTime>2016-07-23T08:28:48Z</DeployedTime>
        </DeployedApiItem>
        <DeployedApiItem>
            <RegionId>cn-qingdao</RegionId>
            <GroupId>1084f9034c744137901057206b39d2b6</GroupId>
            <GroupName>myGroup2</GroupName>
            <ApiId>5af418828f0344a3b588c0cc1331a3bc</ApiId>
            <ApiName>Create an object</ApiName>
            <StageName>release</StageName>
            <Visibility>public</Visibility>
            <Description>Create an object</Description>
            <DeployedTime>2016-07-20T08:28:48Z</DeployedTime>
        </DeployedApiItem>
    </DeployedApis>
    <PageNumber>3</PageNumber>
    <PageSize>15</PageSize>
    <TotalCount>32</TotalCount>
    <RequestId>CEF72CEB-54B6-4AE8-B225-F876FF7BZ002</RequestId>
</DescribeDeployedApisResponse>
```

JSON format

```json
    "DeployedApis": {
        "DeployedApiItem": [
```

`{`

```json
                "RegionId": "cn-qingdao",
                "GroupId": "63be9002440b4778a61122f14c2b2bbb",
                "GroupName": "myGroup3",
                "ApiId": "c076144d7878437b8f82fb85890ce6a0",
                "ApiName": "Query the list of objects",
                "StageName": "release",
                "Visibility": "public",
                "Description": "Query the list of objects by pages",
                "DeployedTime": "2016-07-23T08:28:48Z"
```

`},` `{`

```json
                "RegionId": "cn-qingdao",
                "GroupId": "1084f9034c744137901057206b39d2b6",
                "GroupName": "myGroup2",
                "ApiId": "5af418828f0344a3b588c0cc1331a3bc",
                "ApiName": "Create an object",
                "StageName": "release",
                "Visibility": "public",
                "Description": "Create an object",
                "DeployedTime": "2016-07-20T08:28:48Z"
```

`}` `]` `},`

```json
    "PageNumber": 3,
      "PageSize": 15,
      "TotalCount": 32,
    "RequestId":"CEF72CEB-54B6-4AE8-B225-F876FF7BZ002"
```

`}`

## 8 Plugin operations

### 8.1 CreatePlugin

You can call this operation to create a plugin. Features such as throttling and IP address-based access control are integrated into API Gateway as plugins. More plugins such as cross-origin resource sharing (CORS) and caching plugins will be added to the plugin system in the future. You can call this operation to create various types of plugins. Rules of Use For each type of plugin, only one plugin of such type can be bound to an API. A plugin can only be bound to an API in the same region. Plugin policies and APIs are separately managed. The plugin policies take effect only after you call the AttachPlugin operation to bind a plugin to a specified API in a specified environment. Before you bind a plugin to an API, you must publish the API. A plugin can be bound, unbound, and updated with immediate effect. You do not need to re-publish an API. We recommend that you first test these APIs that may pose high security risks. If an API is unpublished, the relationship between the API and the plugin bound to the API will not change. When the API is re-published, the plugin remains bound to the API. If a plugin is bound to an API, the plugin cannot be deleted. Request parameters

| Parameter | Type | Requi red | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to CreatePlugin. |
| PluginName | String | Yes | The name of the plugin to be created. The name must be 4 to 50 characters in length and can contain only uppercase and lowercase letters, digits, and underscores ( ). The name cannot _ start with an underscore ( ). _ |
| PluginType | String | Yes | The type of the plugin to be created. Valid values: ipControl: IP address-based access control trafficControl: throttling backendSignature: backend signature jwtAuth : JWT authentication (OpenID Connect) cors: cross-origin resource sharing caching: caching routing: backend routing errorMapping: error code mapping accessControl: access control |

| Parameter | Type | Requi red | Description |
|---|---|---|---|
| PluginData | String | Yes | The definition statement of the plugin. JSON and YAML formats are supported. For more information, see the PluginData template. |
| Description | String | No | The description of the plugin. The description can contain a maximum of 200 characters in length. |

PluginData template You can choose the JSON or YAML format to configure your plugins. The two formats have the same schema. You can use the yaml to json tool to convert the configuration format of a plugin. The following example shows a template in YAML format: Throttling plugins

```
--unit: SECOND # The unit of time. Valid values: SECOND, MINUTE, HOUR, and DAY. apiDefault: 1000 # The default API-level throttling threshold. userDefault: 30 # Optional. The default user-level throttling threshold. If you se t this threshold to 0, user-level throttling is not performed. The user-level throttling threshold cannot be greater than the API-level throttling threshold. appDefault: 30 # Optional. The default app-level throttling threshold. If you set this threshold to 0, app-level throttling is not performed. The app-level throttling thre shold cannot be greater than the user-level throttling threshold. specials: # Optional. The special throttling settings. You can set throttlin g thresholds for special apps or users in a throttling policy.
  - type: "APP"        # The special throttling type. The value APP indicates that thrott
ling is performed for special apps based on their AppKeys.
    policies:
      - key: 10123123  # The app ID. You can obtain the ID of an app from the app details
page. To go to this page, click Consume APIs and then APPs in the left-side navigation pa ne of the API Gateway console and click the name of the app.
        value: 10      # The special throttling threshold for the app. This threshold can
not be greater than the user-level throttling threshold in the throttling policy.
      - key: 10123123  # The app ID.
        value: 10      # The special throttling threshold for the app. This threshold can
not be greater than the user-level throttling threshold in the throttling policy.
```

IP address-based access control plugins

```
--type: ALLOW # The type of access control. You can set this parameter to ALLOW to apply a whitelist or to REFUSE to apply a blacklist. items:
  - blocks:          # The IP address segment.
      - 78.11.12.2   # Specifies an IP address.
      - 61.3.9.0/24  # Specifies a CIDR block.
    appId: 219810    # Optional. If you specify this parameter, this IP address-based acc
ess control policy applies only to the app specified by this parameter.
  - blocks:          # The IP address segment.
      - 79.11.12.2   # Specifies an IP address.
```

Backend signature plugins

```
--type: APIGW_BACKEND key: SampleKey secret: SampleSecret
```

JWT authentication

```
--parameter: X-Token # The parameter from which the JWT is read. It corresponds to a parameter in an API request. parameterLocation: header # The location from which the JWT is read. Valid values: query and header. This parameter is optional if Request Mode for the bound API is set to Reques t Parameter Mapping(Filter Unknown Parameters) or Request Parameter Mapping(Passthrough U nknown Parameters). It is required if Request Mode for the bound API is set to Request Pa rameter Passthrough. claimParameters: # The claims to be converted into parameters. API Gateway maps JWT claims to backend parameters.
- claimName: aud           # The name of the JWT claim, which can be public or private.
  parameterName: X-Aud     # The name of the backend parameter, to which the JWT claim is
mapped.
  location: header         # The location of the backend parameter, to which the JWT clai
m is mapped. Valid values: query, header, path, and formData.
- claimName: userId        # The name of the JWT claim, which can be public or private.
  parameterName: userId    # The name of the backend parameter, to which the JWT claim is
mapped.
  location: query          # The location of the backend parameter, to which the JWT clai
m is mapped. Valid values: query, header, path, and formData. preventJtiReplay: false # Controls whether to enable the anti-replay check for jti. De fault value: false.
```

`#`

```bash
# Public key in the JWK
jwk:
  kty: RSA
  e: AQAB
  use: sig
  kid: O8fpdhrViq2zaaaBEWZITz     # If only one JWK is configured, kid is optional. If th
e JWT includes kid, API Gateway checks the consistency of kid.
  alg: RS256
  n: qSVxcknOm0uCq5vGsOmaorPDzHUubBmZZ4UXj-9do7w9X1uKFXAnqfto4TepSNuYU2bA_-tzSLAGBsR-BqvT
6w9SjxakeiyQpVmexxnDw5WZwpWenUAcYrfSPEoNU-0hAQwFYgqZwJQMN8ptxkd0170PFauwACOx4Hfr-9FPGy8NC oIO4MfLXzJ3mJ7xqgIZp3NIOGXz-GIAbCf13ii7kSStpYqN3L_zzpvXUAos1FJ9IPXRV84tIZpFVh2lmRh0h8ImKvI42dwlD_hOIzayL1Xno2R0T-d5AwTSdnep7g-Fwu8-sj4cCRWq3bd61Zs2QOJ8iustH0vSRMYdP5oYQ
```

CORS plugins

```
--allowOrigins: "api.foo.com" # The allowed origins. Separate origins with commas (,). Default value: *. allowMethods: "GET,POST,PUT,DELETE,HEAD,OPTIONS,PATCH" # The allowed HTTP methods. allowHeaders: "Authorization,Accept,Accept-Ranges,Cache-Control,Range,Date,Content-Type,C ontent-Length,Content-MD5,User-Agent,X-Ca-Signature,X-Ca-Signature-Headers,X-Ca-Signature -Method,X-Ca-Key,X-Ca-Timestamp,X-Ca-Nonce,X-Ca-Stage,X-Ca-Request-Mode,x-ca-deviceid" exposeHeaders: "Content-MD5,Server,Date,Latency,X-Ca-Request-Id,X-Ca-Error-Code,X-Ca-Erro r-Message" maxAge: 172800 allowCredentials: true # Controls whether cookies are allowed.
```

Caching plugins

```
--varyByApp: false # Controls whether to match and serve cached responses based on the app IDs of API callers. Default value: false. varyByParameters: # Controls whether to match and serve cached responses based on the values of specific parameters.
  - userId            # The name of a backend parameter. If the backend parameter is mapp
ed to a parameter with a different name, set this parameter to the mapped parameter name. varyByHeaders: # Controls whether to match and serve cached responses based on dif ferent request headers.
  - Accept            # Cached responses are matched and served based on the Accept heade
```

`r.`

```
clientCacheControl: # API Gateway determines how to process the Cache-Control headers o f client requests based on the clientCacheControl settings.
  mode: "app"         # Valid values: off, all, and apps. Default value: off. off indicat
es that API Gateway ignores the Cache-Control headers of all client requests. all indicat es that API Gateway processes the Cache-Control headers of all client requests. apps indi cates that API Gateway processes only the Cache-Control headers of client requests whose app IDs are included in the configured apps list.
  apps:               # A list of app IDs. If mode is set to app, API Gateway processes o
nly the Cache-Control headers of client requests whose app IDs are in this list.
    - 1992323         # A sample app ID. It is not an AppKey.
    - 1239922         # A sample app ID. It is not an AppKey.
cacheableHeaders: # The cacheable response headers. By default, API Gateway caches on ly the Content-Type and Content-Length headers of backend responses.
  - X-Customer-Token  # The name of the cacheable response header.
```

Backend routing plugins

```bash
--routes:
# Responses that are no longer supported are returned to clients of an earlier version. C
lientVersion is a custom parameter in the API.
- name: MockForOldClient
  condition: "$ClientVersion < '2.0.5'"
  backend:
    type: "MOCK"
    statusCode: 400
    mockBody: "This version is not supported!!!"
# Blue-green release scenarios: Five percent of requests are routed to the backend of a b
lue-green release.
- name: BlueGreenPercent05
  condition: "Random() < 0.05"
  backend:
    type: "HTTP"
    address: "https://beta-version.api.foo.com"
  constant-parameters:
  - name: x-route-blue-green
    location: header
    value: "route-blue-green"
```

Error code mapping plugins

```bash
---
# The parameters that are involved in mapping.
parameters:
  statusCode: "StatusCode"
  resultCode: "BodyJsonField:$.result_code"
  resultId: "BodyJsonField:$.req_msg_id"
# The mapping condition.
errorCondition: "$statusCode = 200 and $resultCode <> 'OK'"
# The parameter in an error response that is used to specify the error code and hit mappi
ng rules. errorCode: "resultCode"
# Mapping rules.
mappings:
  - code: "ROLE_NOT_EXISTS"
    statusCode: 404
    errorMessage: "Role Not Exists, RequestId=${resultId}"
  - code: "INVALID_PARAMETER"
    statusCode: 400
    errorMessage: "Invalid Parameter, RequestId=${resultId}"
# The default mapping rule.
defaultMapping:
  statusCode: 500
  errorMessage: "Unknown Error, ${resultCode}, RequestId=${ResultId}"
```

Access control plugins

```
---
```

`#`

```bash
# Assume that the API request path is /{userId}/... in this example.
# JWT authentication is enabled for APIs. Two claims, userId and userType, are available
in the JWT.
# The following plugin verification conditions apply:
# - If userType is set to admin, requests in all paths are allowed.
# - If userType is set to user, only the requests in the same /{userId} path are allowed.
parameters:
  userId: "Token:userId"
  userType: "Token:userType"
  pathUserId: "path:userId"
```

`#`

```xml
# Rules are defined based on the preceding parameters. For each API request, the plugin c
hecks the rules in sequence. If a condition in a rule is met, the result is true and the action that is specified by ifTrue is performed. If a condition in a rule is not met, the result is false and the action that is specified by ifFalse is performed.
# The action ALLOW indicates that the request is allowed. The action DENY indicates that
the request is denied and an error code is returned to the client. After the ALLOW or DEN Y action is performed, the plugin does not check the remaining conditions.
# If neither the ALLOW nor DENY action is performed, the plugin proceeds to check the nex
t condition. rules:
  - name: admin
    condition: "$userType = 'admin'"
    ifTrue: "ALLOW"
  - name: user
    condition: "$userId = $pathUserId"
    ifFalse: "DENY"
    statusCode: 403
    errorMessage: "Path not match ${userId} vs /${pathUserId}"
    responseHeaders:
      Content-Type: application/xml
    responseBody: |
      <Reason>Path not match ${userId} vs /${pathUserId}</Reason>
```

Circuit breaker plugins

```xml
--timeoutThreshold: 15 # The threshold for the number of times when timeout occu rs at the backend. windowInSeconds: 30 # The time window to check the number of times when timeo ut occurs at the backend. openTimeoutSeconds: 15 # The period of time during which the circuit breaker sta ys open after it trips. downgradeBackend: # The backend to which API requests are directed when the circuit breaker is open.
  type: mock
  statusCode: 302
  body: |
    <result>
      <errorCode>I's a teapot</errorCode>
    </result>
```

Response parameters

| Parameter | Type | Description |
|---|---|---|
| RequestId | String | The ID of the request. |
| PluginId | String | The unique ID of the plugin. |

Examples Sample request s

```
http://apigateway.cn-qingdao.aliyuncs.com/?Action=CreatePlugin &PluginName=NewCors &PluginType=cors &PluginData="Plugin definition" &Description="createPlugin" &<Common request parameters>
```

Sample responses XML format

```xml
<CreatePluginResponse>
   <RequestId>CEF72CEB-54B6-4AE8-B225-F876FF7BA984</RequestId>
   <PluginId>285bb759342649a1b70c2093a772e087</PluginId>
</CreatePluginResponse>
```

JSON format `{`

```json
    "RequestId":"EF924FE4-2EDD-4CD3-89EC-34E4708574E7",
    "PluginId" :"1f3bde29b43d4d53989248327ff737f2"
```

`}`

### 8.2 ModifyPlugin

Description You can call this operation to modify the configurations of a custom plug-in. This operation is intended for API providers. The modified configuration takes effect immediately. The name of the plug-in must be unique. Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set this parameter to ModifyPlugin. |

| Developer Guide·P | lugin operations |   | API Gatewa |
|---|---|---|---|

| Parameter | Type | Required | Description |
|---|---|---|---|
| PluginId | String | Yes | The ID of the plug-in to be modified. |
| PluginName | String | No | The name of the plug-in to be modified. The name must be 4 to 50 characters in length and can contain uppercase and lowercase letters, digits, and underscores ( ). It cannot start with an underscore. _ |
| PluginData | String | No | The definition statement of the plug-in. For more information about the format, see the "PluginData template" section of the CreatePlugin topic. |
| Description | String | No | Description |

Response parameters

| Parameter | Type | Description |
|---|---|---|
| RequestId | String | The ID of the request. |

Examples Sample request s

```
http://apigateway.cn-qingdao.aliyuncs.com/?Action=ModifyPlugin &PluginId=a96926e82f994915a8da40a119374537 &PluginName=modifyCors &PluginData="Plugin definition" &Description="modify plugin first" &<Common request parameters>
```

Sample responses XML format

```xml
<ModifyPluginResponse>
    <RequestId>CEF72CEB-54B6-4AE8-B225-F876FF7BZ004</RequestId>
</ModifyPluginResponse>
```

JSON format `{`

```json
    "RequestId":"CEF72CEB-54B6-4AE8-B225-F876FF7BZ004",
```

`}`

### 8.3 DeletePlugin

You can call this operation to delete a specified custom plug-in. This operation is intended for API providers. If the plug-in is bound to an API, you must unbind the plug-in from the API before deleting the plugin. Otherwise, an error is reported. Request parameters

| Parameter | Type | Requi red | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set this parameter to DeletePlugin. |
| PluginId | String | Yes | The ID of the plug-in to be deleted. |

Response parameters

| Parameter | Type | Description |
|---|---|---|
| RequestId | String | The ID of the request. |

Examples Sample request s

```
https://apigateway.cn-qingdao.aliyuncs.com/?Action=DeletePlugin &PluginId=9a3f1a5279434f2ba74ccd91c295af9f &<Common request parameters>
```

Sample responses XML format

```xml
<DeletePluginResponse>
    <RequestId>CEF72CEB-54B6-4AE8-B225-F876FF7BZ004</RequestId>
</DeletePluginResponse>
```

JSON format `{`

```json
    "RequestId":"CEF72CEB-54B6-4AE8-B225-F876FF7BZ004",
```

`}`

### 8.4 AttachPlugin

Description You can call this operation to bind a plug-in to an API. This operation is intended for API providers. You can only bind plug-ins to published APIs. The plug-in takes effect immediately after it is bound to an API. If you bind a different plug-in to an API, this plug-in takes effect immediately. Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set this parameter to AttachPlugin. |
| PluginId | String | Yes | The ID of the plug-in to be bound to the API. |
| ApiIds | String | Yes | The ID of the API to which the plug-in is bound. |
| StageName | String | Yes | The name of the runtime environment to which the API is deployed. Valid values: RELEASE: the release environment PRE: the pre-release environment TEST: the test environment |

Response parameters

| Parameter | Type | Description |
|---|---|---|
| RequestId | String | The ID of the request. |

Examples Sample request s

```
http://apigateway.cn-qingdao.aliyuncs.com/Action=AttachPlugin &PluginId=9a3f1a5279434f2ba74ccd91c295af9f &ApiId=8afff6c8c4c6447abb035812e4d66b65 &StageName=RELEASE
```

Sample responses XML format

```xml
<AttachPluginResponse>
   <RequestId>CEF72CEB-54B6-4AE8-B225-F876FF7BA984</RequestId>
</AttachPluginResponse>
```

JSON format `{`

```json
    "RequestId": "CEF72CEB-54B6-4AE8-B225-F876FF7BZ004"
```

### 8.5 DetachPlugin

Description You can call this operation to unbind a plug-in from an API. This operation is intended for API providers. This operation is used to unbind a plug-in from an API. A plug-in can be unbound from an API with immediate effect. Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set this parameter to DetachPlugin. |
| PluginId | String | Yes | The ID of the plug-in to be unbound. |
| ApiIds | String | Yes | The ID of the API from which the plug-in is unbound. |
| StageName | String | Yes | The name of the runtime environment to which the API is deployed. Valid values: RELEASE: the release environment PRE: the pre-release environment TEST: the test environment |

Response parameters

| Parameter | Type | Description |
|---|---|---|
| RequestId | String | The ID of the request. |

Examples Sample request s

```
http://apigateway.cn-qingdao.aliyuncs.com/?Action=DetachPlugin &PluginId=9a3f1a5279434f2ba74ccd91c295af9f &ApiId=8afff6c8c4c6447abb035812e4d66b65 &StageName=RELEASE &<Common request parameters>
```

Sample responses XML format

```xml
<DetachPluginResponse>
    <RequestId>CEF72CEB-54B6-4AE8-B225-F876FF7BZ004</RequestId>
</DetachPluginResponse>
```

JSON format `{`

```json
    "RequestId": "CEF72CEB-54B6-4AE8-B225-F876FF7BZ004"
```

`}`

### 8.6 DescribePluginApis

Description You can call this operation to query detailed information of the APIs to which a specified plug-in is bound. This operation is intended for API providers. This operation is used to query detailed information of the APIs to which a specified plug-in is bound. This operation supports pagination. The returned APIs to which a plug-in is bound may be unpublished. Request parameters

| Parameter | Type | Requi red | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set this parameter to DescribePluginApis. |
| PluginId | String | Yes | The ID of the plug-in for the query. |
| PageSize | Integer | No | The number of entries to return on each page. Maximum value: 100. Default value: 10. |
| PageNumber | Integer | No | The number of the page to return. Pages start from page 1. Default value: 1. |

Response parameters

| Parameter | Type | Description |
|---|---|---|
| RequestId | String | The ID of the request. |
| TotalCount | Integer | The total number of returned entries. |
| PageSize | Integer | The number of entries returned on each page. |
| PageNumber | Integer | The number of the page returned. |

| Parameter | Type | Description |
|---|---|---|
| ApiSummarys | ApiPluginSummary | The returned API information. It is an array consisting of ApiPluginSummary data. |

Examples Sample request s

```
http://apigateway.cn-qingdao.aliyuncs.com/?Action=DescribePluginApis &PluginId=a96926e82f994915a8da40a119374537 &<Common request parameters>
```

Sample responses XML format

```xml
<DescribePluginApisResponse>
   <RequestId>46373DC4-19F1-4DC8-8C31-1107289BB5E0</RequestId>
   <TotalCount>20</TotalCount>
   <PageSize>10</PageSize>
   <PageNumber>1</PageNumber>
   <ApiSummarys>
      <ApiPluginSummary>
          <ApiId>9a3f1a5279434f2ba74ccd91c295af9f</ApiId>
          <ApiName>firstAPI</ApiName>
          <RegionId>cn-qingdao</RegionId>
          <StageName>RELEASE</StageName>
          <GroupId>46c79e78dfab4521a5f737faa805c4e1</GroupId>
          <GroupName>firstGroup</GroupName>
          <Description>Description</Description>
      </ApiPluginSummary>
   </ApiSummarys>
</DescribePluginApisResponse>
```

JSON format

```json
   "RequestId": "2DF14872-77CE-43A4-AB47-C4F128E5AA31",
   "TotalCount": "1",
   "PageNumber": "1",
   "PageSize": "10",
   "ApiSummarys": {
        "ApiPluginSummary": [{
            "ApiId":"9a3f1a5279434f2ba74ccd91c295af9f",
            "ApiName":"firstAPI",
            "RegionId":"cn-qingdao",
            "StageName":"RELEASE",
            "GroupId":"46c79e78dfab4521a5f737faa805c4e1",
            "GroupName": "firstGroup"，
            "Description": "Description",
```

`}]` `},` `}`

### 8.7 DescribePlugins

Description You can call this operation to query the details of API Gateway plug-ins that meet specified query conditions. This operation supports pagination. This operation allows you to query by business type. This operation allows you to query by ID. This operation allows you to query by name. Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set this parameter to DescribePlugins. |
| PluginId | String | No | The ID of the plug-in to query. |
| PluginName | String | No | The name of the plug-in to query. |
| PluginType | String | No | The type of the plug-in to query. Valid values: ipControl: IP address-based access control trafficControl: throttling backendSignature: back-end signature |
| PageSize | Integer | No | The number of entries to return on each page. Maximum value: 100. Default value: 10. |

| Parameter | Type | Required | Description |
|---|---|---|---|
| PageNumber | Integer | No | The number of the page to return. Pages start from page 1. Default value: 1. |

Response parameters

| Parameter | Type | Description |
|---|---|---|
| RequestId | String | The ID of the request. |
| TotalCount | Integer | The total number of returned entries. |
| PageNumber | Integer | The number of the page returned. |
| PageSize | Integer | The number of entries returned on each page. |
| Plugins | PluginAttrubite | The returned plug-in information. It is an array consisting of PluginAttribute data. |

Examples Sample request s

```
http://apigateway.cn-qingdao.aliyuncs.com/?Action=DescribePlugins &PluginId=a96926e82f994915a8da40a119374537 &PluginName=testPlugin &PluginType=ipControl &<Common request parameters>
```

Sample responses XML format

```xml
<DescribePluginsResponse>
   <RequestId>46373DC4-19F1-4DC8-8C31-1107289BB5E0</RequestId>
   <TotalCount>20</TotalCount>
   <PageSize>10</PageSize>
   <PageNumber>1</PageNumber>
   <Plugins>
      <PluginAttribute>
          <PluginId>9a3f1a5279434f2ba74ccd91c295af9f</PluginId>
          <PluginName>firstPlugin</PluginName>
          <RegionId>cn-qingdao</RegionId>
          <PluginType>trafficControl</PluginType>
          <PluginData>{"unit":"MINUTE","apiDefault":20}</PluginData>
          <Description>Throttling</Description>
          <CreatedTime>2019-01-11T09:29:58Z</CreatedTime>
          <ModifiedTime>2019-01-11T09:29:58Z</ModifiedTime>
      </PluginAttribute>
   </Plugins>
</DescribePluginsResponse>
```

JSON format `{`

```json
   "RequestId": "46373DC4-19F1-4DC8-8C31-1107289BB5E0",
   "TotalCount": "1",
   "PageNumber": "1",
   "PageSize": "10",
   "Plugins": {
        "PluginAttribute": [{
            "PluginId":"9a3f1a5279434f2ba74ccd91c295af9f",
            "PluginName":"firstPlugin",
            "RegionId":"cn-qingdao",
            "PluginType":"trafficControl",
            "PluginData":"{\"unit\":\"MINUTE\",\"apiDefault\":20}",
            "Description": "throttling"，
            "CreatedTime":"2019-01-11T09:29:58Z",
            "ModifiedTime":"2019-01-11T09:29:58Z"
```

`}]` `}` `}`

### 8.8 DescribePluginsByApi

Description You can call this operation to query plug-ins that are bound to a specified API. The API must have been published to an environment. This API is intended for API providers. This operation is used to query plug-ins that are bound to a specified API in a specific environment. Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribePluginsByApi. |
| GroupId | String | Yes | The ID of the group to which the API to be queried belongs. |
| ApiId | String | Yes | The ID of the API to be queried. |
| StageName | String | Yes | The runtime environment of the API. Valid values: RELEASE PRE: the pre-release environment TEST: the test environment |

Response parameters

| Parameter | Type | Description |
|---|---|---|
| RequestId | String | The ID of the request. |
| TotalCount | Integer | The total number of returned entries. |
| PageNumber | Integer | The page number of the returned page. |
| PageSize | Integer | The number of entries returned per page. |
| Plugins | PluginAttribute | The returned plug-in information. It is an array consisting of PluginAttribute data. |

Examples Sample request s

```
http://apigateway.example.com/?Action=DescribePluginsByApi
 &ApiId=93f4ead4080c4b2da70b7f81f50ae459
 &GroupId=3c7a38392e764718ad7673e7b7f535d4
 &StageName=RELEASE
 &<Common request parameters>
```

Sample success responses XML format

```xml
<DescribePluginsByApiResponse>
   <RequestId>46373DC4-19F1-4DC8-8C31-1107289BB5E0</RequestId>
   <TotalCount>20</TotalCount>
   <PageSize>10</PageSize>
   <PageNumber>1</PageNumber>
   <Plugins>
      <PluginAttribute>
          <PluginId>9a3f1a5279434f2ba74ccd91c295af9f</PluginId>
          <PluginName>firstPlugin</PluginName>
          <RegionId>cn-qingdao</RegionId>
          <PluginType>trafficControl</PluginType>
          <PluginData>{"unit":"MINUTE","apiDefault":20}</PluginData>
          <Description>Throttling</Description>
          <CreatedTime>2019-01-11T09:29:58Z</CreatedTime>
          <ModifiedTime>2019-01-11T09:29:58Z</ModifiedTime>
      </PluginAttribute>
   </Plugins>
</DescribePluginsByApiResponse>
```

JSON format `{`

```json
   "RequestId": "46373DC4-19F1-4DC8-8C31-1107289BB5E0",
   "TotalCount": "1",
   "PageNumber": "1",
   "PageSize": "10",
   "Plugins": {
        "PluginAttribute": [{
            "PluginId":"9a3f1a5279434f2ba74ccd91c295af9f",
            "PluginName":"firstPlugin",
            "RegionId":"cn-qingdao",
            "PluginType":"trafficControl",
            "PluginData":"{\"unit\":\"MINUTE\",\"apiDefault\":20}",
            "Description": "throttling",
            "CreatedTime":"2019-01-11T09:29:58Z",
            "ModifiedTime":"2019-01-11T09:29:58Z"
```

`}]` `}` `}`

## 9 App management operations

### 9.1 CreateApp

Description You can call this operation to create an application. An application is used to call third-party APIs. This operation is intended for API callers. Each application has a key pair that is used for identity authentication when an API is called. An application must be authorized to call an API. Each application has only one key pair. You can reset the key pair as needed. The QPS limit on this operation is 50 per user. Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set this parameter to CreateApp. |
| AppName | String | Yes | The name of the application. The name must be globally unique. We recommend that you add a special identifier to ensure that the name is unique. The name must be 4 to 15 characters in length. It must start with a letter and can contain letters, digits, and underscores ( ). _ |
| Description | String | No | The description of the application. The description can contain a maximum of 180 characters in length. |

Response parameters

| Parameter | Type | Description |
|---|---|---|
| RequestId | String | The ID of the request. |
| AppId | Long | The unique ID of the application. |

Examples Sample request s

```
https://apigateway.cn-qingdao.aliyuncs.com/?Action=CreateApp &AppName=CreateAppTest &Description=test &<Common request parameters>
```

Sample responses XML format

```xml
<CreateAppResponse>
    <AppId>20112314518278</AppId>
    <RequestId>CEF72CEB-54B6-4AE8-B225-F876FF7BZ015</RequestId>
</CreateAppResponse>
```

JSON format `{`

```json
    "AppId":20112314518278,
    "RequestId":"BA20890E-75C7-41BC-9C8B-73276B58F550"
```

`}`

### 9.2 ModifyApp

Description You can call this operation to modify the basic information of a specific application. This operation is intended for API callers. AppName or Description can be modified. If these parameters are not specified, no modifications are made and the operation will directly return a successful response. The QPS limit on this operation is 50 per user. Request parameters

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to ModifyApp. |
| AppId | Long | Yes | The application ID. |
| AppName | String | No | The application name, which is globally unique. We recommend that you add a special identifier to ensure the name is unique. The name must be 4 to 15 characters in length. It must start with a letter and can contain letters, numbers, and underscores ( ). _ This parameter is optional. |
| Description | String | No | The API description, which cannot exceed 180 characters. This parameter is optional. |

Response parameters

| Name | Type | Description |
|---|---|---|
| RequestId | String | The request ID. |

Examples Sample request

```
https://apigateway.cn-qingdao.aliyuncs.com/?Action=ModifyApp &AppId=20112314518278 &Description=modidyTest &<Common request parameters>
```

Sample responses XML format

```xml
<ModifyAppResponse>
    <RequestId>CEF72CEB-54B6-4AE8-B225-F876FF7BZ015</RequestId>
</ModifyAppResponse>
```

JSON format `{`

```json
    "RequestId":"CEF72CEB-54B6-4AE8-B225-F876FF7BZ015"
```

`}`

### 9.3 ResetAppSecret

Description You can call this operation to reset the secret of a specific application. This operation is intended for API callers. A new secret is automatically generated after you have called this operation. This secret cannot be customized. The results returned by this operation do not contain the application secret. You can obtain the secret by calling DescribeAppSecurity. Request parameters

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to ResetAppSecret. |
| AppKey | String | Yes | The application key that is used for calling an API. |

Response parameters

| Name | Type | Description |
|---|---|---|
| RequestId | String | The request ID. |

Examples Sample request

```
https://apigateway.cn-qingdao.aliyuncs.com/?Action=ResetAppSecret &AppKey=60030986 &<Common request parameters>
```

Sample responses XML format

```xml
<ResetAppSecretResponse>
    <RequestId>CEF72CEB-54B6-4AE8-B225-F876FF7BZ015</RequestId>
</ResetAppSecretResponse>
```

JSON format `{`

```json
    "RequestId":"CEF72CEB-54B6-4AE8-B225-F876FF7BZ015"
```

`}`

### 9.4 DescribeAppAttributes

Description You can call this operation to query applications and their basic information. This operation is intended for API callers. The AppId parameter is optional in requests. Request parameters

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeAppAttributes. |
| AppId | Long | No | The application ID. |
| PageSize | Integer | No | The number of rows per page. The maximum value is 100. The default value is 10. |
| PageNumber | Integer | No | The specific page number that you want to query. The default value is 1. The starting number is 1. |

Response parameters

| Name | Type | Description |
|---|---|---|
| RequestId | String | The request ID. |
| TotalCount | Integer | The total number of rows. |
| PageNumber | Integer | The specified page number. |

| PI Gateway |   | Developer Guide·App management |
|---|---|---|

| Name | Type | Description |
|---|---|---|
| PageSize | Integer | The specified number of rows returned per page. |
| Apps | AppAttribute | The returned application information. It is an array consisting of AppAttribute data. |

Examples Sample request

```
https://apigateway.cn-qingdao.aliyuncs.com/?Action=DescribeAppAttributes &AppId=20112314518278 &pageSize=10 &pageNumber=1 &<Common request parameters>
```

Sample responses XML format

```xml
<DescribeAppAttributesResponse>
    <RequestId>CEF72CEB-54B6-4AE8-B225-F876FF7BZ015</RequestId>
      <TotalCount>1</TotalCount>
    <PageSize>10</PageSize>
    <PageNumber>1</PageNumber>
    <Apps>
        <AppAttribute>
            <AppId>20112314518278</AppId>
            <AppName>CreateApptest</AppName>
            <Description>APP test</Description>
            <CreatedTime>2016-07-31T04:10:19Z</CreatedTime>
            <ModifiedTime>2016-07-31T04:10:19Z</ModifiedTime>
        </AppAttribute>
    </Apps>
</DescribeAppAttributesResponse>
```

JSON format

```json
    "TotalCount":1,
    "PageSize":10,
    "PageNumber":1,
    "RequestId":"8883AC74-259D-4C0B-99FC-0B7F9A588B2F",
    "Apps":
```

`{`

```json
        "AppAttribute":
```

`[` `{`

```json
                "AppId":20112314518278,
                "AppName":"CreateApptest",
                "Description":"APP test",
                "CreatedTime":"2016-07-31T04:10:19Z",
                "ModifiedTime":"2016-07-31T04:10:19Z"
```

`}` `]` `}` `}`

### 9.5 DescribeAppSecurity

Description You can call this operation to query the key of a specified application. The key is used for authentication when you call an API. This operation is intended for API callers. Request parameters

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeAppSecurity. |
| AppId | Long | Yes | The application ID. |

Response parameters

| Name | Type | Description |
|---|---|---|
| RequestId | String | The request ID. |
| AppKey | String | The application key. |
| AppSecret | String | The application secret. |
| CreatedTime | String | The creation time (UTC) of the key, which is the same as the application creation time. |
| ModifiedTime | String | The modification time (UTC) of the key. |

Examples Sample request

```
https://apigateway.cn-qingdao.aliyuncs.com/?Action=DescribeAppSecurity &AppId=20112314518278 &<Common request parameters>
```

Sample responses XML format

```xml
<DescribeAppSecurityResponse>
    <RequestId>CEF72CEB-54B6-4AE8-B225-F876FF7BZ015</RequestId>
    <AppKey>60030986</AppKey>
    <AppSecret>c1ae97aaa7e45f21d10824bc44678fee</AppSecret>
    <CreatedTime>2016-07-31T04:10:19Z</CreatedTime>
    <ModifiedTime>2016-07-31T04:10:19Z</ModifiedTime>
</DescribeAppSecurityResponse>
```

JSON format `{`

```json
    "RequestId":"CEF72CEB-54B6-4AE8-B225-F876FF7BZ015",
    "AppKey":"60030986",
    "AppSecret":"c1ae97aaa7e45f21d10824bc44678fee",
    "CreatedTime":"2016-07-31T04:10:19Z",
    "ModifiedTime":"2016-07-31T04:10:19Z"
```

`}`

### 9.6 DeleteApp

Description You can call this operation to delete a specified application. This operation is intended for API callers. After deletion, the application and its API authorization cannot be restored. The QPS limit on this operation is 50 per user. Request parameters

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DeleteApp. |
| AppId | Long | Yes | The application ID. |

Response parameters

| Name | Type | Description |
|---|---|---|
| RequestId | String | The request ID. |

Examples Sample request

```
https://apigateway.cn-qingdao.aliyuncs.com/?Action=DeleteApp &AppId=20112314518278 &<Common request parameters>
```

Sample responses XML format

```xml
<DeleteAppResponse>
    <RequestId>CEF72CEB-54B6-4AE8-B225-F876FF7BZ015</RequestId>
</DeleteAppResponse>
```

JSON format `{`

```json
    "RequestId":"CEF72CEB-54B6-4AE8-B225-F876FF7BZ015"
```

`}` ations

## 10 Authorization operations

### 10.1 DescribeApps

Description You can call this operation to query which applications you are able to grant permissions to. You can then grant permissions based on the obtained application information. This operation is intended for API providers. API providers can use the application IDs or their Apsara Stack tenant accounts to query application information. Each provider can call this operation for a maximum of 200 times every day in a region. Request parameters

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeApps. |
| AppId | Long | No | The application ID. |
| AppOwner | String | No | The Apsara Stack tenant account ID of the application owner. |
| PageSize | Integer | No | The number of rows per page. The maximum value is 100. The default value is 10. |
| PageNumber | Integer | No | The specific page number that you want to query. The default value is 1. The starting number is 1. |

Response parameters

| Name | Type | Description |
|---|---|---|
| RequestId | String | The request ID. |
| TotalCount | Integer | The total number of rows. |
| PageNumber | Integer | The specified page number. |
| PageSize | Integer | The specified number of rows returned per page. |
| Apps | AppItem | The returned application information. It is an array consisting of AppItem data. |

Examples Sample request ations

```
https://apigateway.cn-qingdao.aliyuncs.com/?Action=DescribeApps &AppId=20112314518278 &pageSize=10 &pageNumber=1 &<Common request parameters>
```

Sample responses XML format

```xml
<DescribeAppsResponse>
    <RequestId>CEF72CEB-54B6-4AE8-B225-F876FF7BZ015</RequestId>
      <TotalCount>1</TotalCount>
    <PageSize>10</PageSize>
    <PageNumber>1</PageNumber>
    <Apps>
        <AppItem>
            <AppId>20112314518278</AppId>
            <AppName>CreateApptest</AppName>
            <Description>APP test</Description>
        </AppItem>
    </Apps>
</DescribeAppsResponse>
```

JSON format `{`

```json
    "TotalCount":1,
    "PageSize":10,
    "PageNumber":1,
    "RequestId":"8883AC74-259D-4C0B-99FC-0B7F9A588B2F",
    "Apps":
```

`{`

```json
        "AppItem":
```

`[` `{`

```json
                "AppId":20112314518278,
                "AppName":"CreateApptest",
                "Description":"APP test"                    }
```

`]` `}` `}`

### 10.2 DescribeAuthorizedApis

Description You can call this operation to query the APIs that a specified application can call. This operation is intended for API callers. The specified application can call all APIs included in the responses. Request parameters ations

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeAuthorizedApis. |
| AppId | Long | Yes | The application ID, which is generated by the system and globally unique. |
| PageNumber | Integer | No | The specific page number that you want to query. The default value is 1. The starting number is 1. |
| PageSize | Integer | No | The number of rows per page. The maximum value is 100. The default value is 10. |

Response parameters

| Name | Type | Description |
|---|---|---|
| RequestId | String | The request ID. |
| TotalCount | Integer | The total number of rows. |
| PageSize | Integer | The specified number of rows returned per page. |
| PageNumber | Integer | The specified page number. |
| AuthorizedApis | AuthorizedApi | The authorized API set. |

Examples Sample request

```
http://apigateway.cn-hangzhou.aliyuncs.com?Action=DescribeAuthorizedApis &AppId＝2386789 &<Common request parameters>
```

Sample responses XML format ations

```xml
<DescribeAuthorizedApisResponse>
    <PageNumber>1</PageNumber>
    <TotalCount>2</TotalCount>
    <PageSize>10</PageSize>
    <RequestId>D6E46F10-F26C-4AA0-BB69-FE2743D9AE62</RequestId>
    <AuthorizedApis>
        <AuthorizedApi>
            <RegionId>cn-hangzhou</RegionId>
            <GroupId>523e8dc7bbe04613b5b1d726c2a7889d</GroupId>
            <GroupName>Weather</GroupName>
            <StageName>RELEASE</StageName>
            <Operator>PROVIDER</Operator>
            <ApiId>baacc592e63a4cb6a41920d9d3f91f38</ApiId>
            <ApiName>AreaWeather</ApiName>
            <AuthorizationSource>CONSOLE</AuthorizationSource>
            <Description>Queries weather based on the region name</Description>
            <AuthorizedTime>2016-07-21T06:17:20Z</AuthorizedTime>
        </AuthorizedApi>
        <AuthorizedApi>
            <RegionId>cn-hangzhou</RegionId>
            <GroupId>523e8dc7bbe04613b5b1d726c2a7889d</GroupId>
            <GroupName>Weather</GroupName>
            <StageName>RELEASE</StageName>
            <Operator>CONSUMER</Operator>
            <ApiId>baacc592e63a4cb6a41920d9d3f89g76</ApiId>
            <ApiName>Area</ApiName>
            <AuthorizationSource>API</AuthorizationSource>
            <Description>Queries regions</Description>
            <AuthorizedTime>2016-07-21T06:17:20Z</AuthorizedTime>
        </AuthorizedApi>
    </AuthorizedApis>
</DescribeAuthorizedApisResponse>
```

JSON format ations

```json
"PageNumber": "1", "TotalCount": "2", "PageSize": "10", "RequestId": "D6E46F10-F26C-4AA0-BB69-FE2743D9AE62", "AuthorizedApis": {
  "AuthorizedApi": [
```

`{`

```json
      "RegionId": "cn-hangzhou",
      "GroupId": "523e8dc7bbe04613b5b1d726c2a7889d",
      "GroupName": "Weather",
      "StageName": "RELEASE",
      "Operator": "Provider",
      "ApiId": "baacc592e63a4cb6a41920d9d3f91f38",
      "ApiName": "AreaWeather",
      "AuthorizationSource": "CONSOLE",
      "Description": "Queries weather based on the region name",
      "AuthorizedTime": "2016-07-21T06:17:20Z"
```

`},` `{`

```json
      "RegionId": "cn-hangzhou",
      "GroupId": "523e8dc7bbe04613b5b1d726c2a7889d",
      "GroupName": "Weather",
      "StageName": "RELEASE",
      "Operator": "CONSUMER",
      "ApiId": "baacc592e63a4cb6a41920d9d3f89g76",
      "ApiName": "Area",
      "AuthorizationSource": "API",
      "Description": "Queries regions",
      "AuthorizedTime": "2016-07-21T06:17:20Z"
```

`}` `]` `}` `}`

### 10.3 DescribeAuthorizedApps

Description You can call this operation to query which applications currently have access to a specified API. This operation is intended for API providers. All applications included in the responses have access to the specified API. Request parameters

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeAuthorizedApps. |

ations

| Name | Type | Required | Description |
|---|---|---|---|
| GroupId | String | Yes | The API group ID, which is generated by the system and globally unique. |
| ApiId | String | Yes | The API ID, which is generated by the system and globally unique. |
| StageName | String | No | The name of the runtime environment. Valid values: RELEASE TEST |
| PageNumber | Integer | No | The specific page number that you want to query. The default value is 1. The starting number is 1. |
| PageSize | Integer | No | The number of rows per page. The maximum value is 100. The default value is 10. |

Response parameters

| Name | Type | Description |
|---|---|---|
| RequestId | String | The request ID. |
| TotalCount | Integer | The total number of rows. |
| PageNumber | Integer | The specified page number. |
| PageSize | Integer | The specified number of rows returned per page. |
| AuthorizedApps | AuthorizedApp | The returned group set. |

Examples Sample request

```
http://apigateway.cn-hangzhou.aliyuncs.com?Action=DescribeAuthorizedApps &GroupId＝523e8dc7bbe04613b5b1d726c2a7889d &ApiId＝baacc592e63a4cb6a41920d9d3f91f38 &<Common request parameters>
```

Sample responses XML format ations

```xml
<DescribeAuthorizedAppsResponse>
    <TotalCount>2</TotalCount>
    <PageNumber>1</PageNumber>
    <PageSize>10</PageSize>
    <RequestId>D6E46F10-F26C-4AA0-BB69-FE2743D9AE62</RequestId>
    <AuthorizedApps>
        <AuthorizedApp>
            <StageName>RELEASE</StageName>
            <AppId>2386789</AppId>
            <AppName>Weather app</AppName>
            <Operator>PROVIDER</Operator>
            <AuthorizationSource>CONSOLE</AuthorizationSource>
            <Description>Queries weather based on the region name</Description>
            <AuthorizedTime>2016-07-21T06:17:20Z</AuthorizedTime>
        </AuthorizedApp>
        <AuthorizedApp>
            <StageName>TEST</StageName>
            <AppId>2386789</AppId>
            <AppName>Weather app</AppName>
            <Operator>CONSUMER</Operator>
            <AuthorizationSource>API</AuthorizationSource>
            <Description>Queries weather based on the region name</Description>
            <AuthorizedTime>2016-07-21T06:17:20Z</AuthorizedTime>
        </AuthorizedApp>
    </AuthorizedApps>
</DescribeAuthorizedAppsResponse>
```

JSON format ations

```json
"TotalCount": "2", "PageNumber": "1", "PageSize": "10", "RequestId": "D6E46F10-F26C-4AA0-BB69-FE2743D9AE62", "AuthorizedApps": {
  "AuthorizedApp": [
```

`{`

```json
      "StageName": "RELEASE",
      "AppId": 2386789,
      "AppName": "Weather app",
      "Operator": "PROVIDER",
      "AuthorizationSource": "CONSOLE",
      "Description": "Queries weather based on the region name",
      "AuthorizedTime": "2016-07-21T06:17:20Z"
```

`},` `{`

```json
      "StageName": "TEST",
      "AppId": 2386789,
      "AppName": "Weather app",
      "Operator": "CONSUMER",
      "AuthorizationSource": "API",
      "Description": "Queries weather based on the region name",
      "AuthorizedTime": "2016-07-21T06:17:20Z"
```

`}` `]` `}` `}`

### 10.4 SetApisAuthorities

Description You can call this operation to grant access permissions on multiple APIs to a specified application. In this case, multiple APIs map to a single application. This operation is intended for API providers and callers. API providers can authorize any applications to call their APIs. API callers can authorize their own applications to call APIs they have purchased. Request parameters

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to SetApisAuthorities. |
| GroupId | String | Yes | The API group ID, which is generated by the system and globally unique. |

ations

| Name | Type | Required | Description |
|---|---|---|---|
| StageName | String | Yes | The name of the runtime environment. Valid values: RELEASE TEST |
| AppId | Long | Yes | The application ID, which is generated by the system and globally unique. |
| ApiIds | String | No | The API ID for the specified operation. Separate multiple API IDs with commas (,). A maximum of 100 API IDs can be entered. |
| Description | String | No | The authorization description. |

Response parameters

| Name | Type | Description |
|---|---|---|
| RequestId | String | The request ID. |

Examples Sample request

```
http://apigateway.cn-hangzhou.aliyuncs.com?Action=SetApisAuthorities &GroupId＝523e8dc7bbe04613b5b1d726c2a7889d &StageName＝RELEASE &AppId＝2386789 &ApiIds＝baacc592e63a4cb6a41920d9d3f91f38,jkscc489e63a4cb6a41920d9d3f92d78 &<Common request parameters>
```

Sample responses XML format

```xml
<SetApisAuthoritiesResponse>
    <RequestId>D6E46F10-F26C-4AA0-BB69-FE2743D9AE62</RequestId>
</SetApisAuthoritiesResponse>
```

JSON format `{`

```json
    "RequestId": "D6E46F10-F26C-4AA0-BB69-FE2743D9AE62",
```

`}`

### 10.5 SetAppsAuthorities

You can call this operation to grant access permissions on a specified API to multiple applications. In this case, multiple applications map to a single API. ations This operation is intended for API providers and callers. API providers can authorize any applications to call their APIs. API callers can authorize their own applications to call APIs they have purchased. Request parameters

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to SetAppsAuthorities. |
| GroupId | String | Yes | The API group ID, which is generated by the system and globally unique. |
| StageName | String | Yes | The name of the runtime environment. Valid values: RELEASE TEST |
| ApiId | String | Yes | The API ID, which is generated by the system and globally unique. |
| AppIds | String | Yes | The application ID for the specified operation. Separate multiple application IDs with commas (,). A maximum of 100 application IDs can be entered. |
| Description | String | No | The authorization description. |

Response parameters

| Name | Type | Description |
|---|---|---|
| RequestId | String | The request ID. |

Examples Sample request

```
http://apigateway.cn-hangzhou.aliyuncs.com?Action=SetAppsAuthorities &GroupId＝523e8dc7bbe04613b5b1d726c2a7889d &StageName＝RELEASE &ApiId＝baacc592e63a4cb6a41920d9d3f91f38 &AppIds＝2386789,3389798 &<Common request parameters>
```

Sample responses XML format

```xml
<SetAppsAuthoritiesResponse>
    <RequestId>D6E46F10-F26C-4AA0-BB69-FE2743D9AE62</RequestId>
</SetAppsAuthoritiesResponse>
```

ations JSON format

```json
    "RequestId": "D6E46F10-F26C-4AA0-BB69-FE2743D9AE62",
```

`}`

### 10.6 RemoveApisAuthorities

Description You can call this operation to revoke the access permissions on multiple APIs from a specified application. In this case, multiple APIs map to a single application. This operation is intended for API providers and callers. Before you revoke access permissions, check by whom the permissions were granted. API providers can only revoke permissions granted by a Provider, and API callers can only revoke permissions granted by a Consumer. Request parameters

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to RemoveApisAuthorities. |
| GroupId | String | Yes | The API group ID, which is generated by the system and globally unique. |
| StageName | String | Yes | The name of the runtime environment. Valid values: RELEASE TEST |
| ApiIds | String | Yes | The API ID for the specified operation. Separate multiple API IDs with commas (,). A maximum of 100 API IDs can be entered. |
| AppId | Long | Yes | The application ID, which is generated by the system and globally unique. |

Response parameters

| Name | Type | Description |
|---|---|---|
| RequestId | String | The request ID. |

Examples Sample request ations

```
http://apigateway.cn-hangzhou.aliyuncs.com?Action=RemoveApisAuthorities &GroupId＝523e8dc7bbe04613b5b1d726c2a7889d &StageName＝RELEASE &ApiId＝baacc592e63a4cb6a41920d9d3f91f38,jkscc489e63a4cb6a41920d9d3f92d78 &AppId＝2386789 &<Common request parameters>
```

Sample responses XML format

```xml
<RemoveApisAuthoritiesResponse>
    <RequestId>D6E46F10-F26C-4AA0-BB69-FE2743D9AE62</RequestId>
</RemoveApisAuthoritiesResponse>
```

JSON format `{`

```json
    "RequestId": "D6E46F10-F26C-4AA0-BB69-FE2743D9AE62",
```

`}`

### 10.7 RemoveAppsAuthorities

Description You can call this operation to revoke the access permissions on a specified API from multiple applications. In this case, multiple applications map to a single API. This operation is intended for API providers and callers. Before you revoke access permissions, check by whom the permissions were granted. API providers can only revoke permissions granted by a Provider, and API callers can only revoke permissions granted by a Consumer. Request parameters

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to RemoveAppsAuthorities. |
| GroupId | String | Yes | The API group ID, which is generated by the system and globally unique. |
| StageName | String | Yes | The name of the runtime environment. Valid values: RELEASE TEST |
| ApiId | String | Yes | The API ID, which is generated by the system and globally unique. |

ations

| Name | Type | Required | Description |
|---|---|---|---|
| AppIds | String | Yes | The application IDs for the specified operation. Separate multiple application IDs with commas (,). A maximum of 100 application IDs can be entered. |

Response parameters

| Name | Type | Description |
|---|---|---|
| RequestId | String | The request ID. |

Examples Sample request

```
http://apigateway.cn-hangzhou.aliyuncs.com?Action=RemoveAppsAuthorities &GroupId=523e8dc7bbe04613b5b1d726c2a7889d &StageName＝RELEASE &ApiId＝baacc592e63a4cb6a41920d9d3f91f38 &AppIds＝2386789,3286798 &<Common request parameters>
```

Sample responses XML format

```xml
<RemoveAppsAuthoritiesResponse>
    <RequestId>D6E46F10-F26C-4AA0-BB69-FE2743D9AE62</RequestId>
</RemoveAppsAuthoritiesResponse>
```

JSON format `{`

```json
    "RequestId": "D6E46F10-F26C-4AA0-BB69-FE2743D9AE62",
```

`}`

## 11 Other operations

### 11.1 DescribeRegions

Description You can call this operation to query supported regions. This operation is intended for API providers and callers. Request parameters

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeRegions. |

Response parameters

| Name | Type | Description |
|---|---|---|
| RequestId | String | The request ID. |
| Regions | Region | The returned region information. It is an array consisting of Region data. |

Examples Sample request

```
https://apigateway.cn-qingdao.aliyuncs.com/?Action=DescribeRegions &<Common request parameters>
```

Sample responses XML format

```xml
<DescribeRegionsResponse>
    <RequestId>36BBBAD4-1CFB-489F-841A-8CA52EEA787E</RequestId>
    <Regions>
        <Region>
            <RegionId>cn-qingdao</RegionId>
            <EndPoint>apigateway.cn-qingdao.aliyuncs.com</EndPoint>
            <LocalName>China (Qingdao)</LocalName>
        </Region>
        <Region>
            <RegionId>cn-hangzhou</RegionId>
            <EndPoint>apigateway.cn-hangzhou.aliyuncs.com</EndPoint>
            <LocalName>China (Hangzhou)</LocalName>
        </Region>
        <Region>
            <RegionId>cn-beijing</RegionId>
            <EndPoint>apigateway.cn-beijing.aliyuncs.com</EndPoint>
            <LocalName>China (Beijing)</LocalName>
        </Region>
        <Region>
            <RegionId>cn-shenzhen</RegionId>
            <EndPoint>apigateway.cn-shenzhen.aliyuncs.com</EndPoint>
            <LocalName>China (Shenzhen)</LocalName>
        </Region>
    </Regions>
</DescribeRegionsResponse>
```

JSON format

```json
    "RequestId": "36BBBAD4-1CFB-489F-841A-8CA52EEA787E",
    "Regions": {
        "Region": [
```

`{`

```json
                "RegionId": "cn-qingdao",
                "EndPoint": "apigateway.cn-qingdao.aliyuncs.com",
                "LocalName": "China (Qingdao)"
```

`},` `{`

```json
                "RegionId": "cn-hangzhou",
                "EndPoint": "apigateway.cn-hangzhou.aliyuncs.com",
                "LocalName": "China (Hangzhou)"
```

`},` `{`

```json
                "RegionId": "cn-beijing"
                "EndPoint": "apigateway.cn-beijing.aliyuncs.com",
                "LocalName": "China (Beijing)"
```

`},` `{`

```json
                "RegionId": "cn-shenzhen",
                "EndPoint": "apigateway.cn-shenzhen.aliyuncs.com",
                "LocalName": "China (Shenzhen)"
```

`}` `]` `}` `}`

### 11.2 DescribeSystemParameters

Description You can call this operation to query configurable system parameters. This API is intended for API providers. The response of this API contains the system parameters that are optional in API definitions. Request parameters

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeSystemParameters. |

Response parameters

| Name | Type | Description |
|---|---|---|
| RequestId | String | The ID of the current request. |

| Name | Type | Description |
|---|---|---|
| SystemParams | Array | The returned information about system parameters. It is an array consisting of SystemParamItem data. |

Examples Sample request

```
https://apigateway.cn-qingdao.aliyuncs.com/?Action=DescribeSystemParameters &<Common request parameters>
```

Sample responses XML format

```xml
<DescribeSystemParametersResponse>
    <RequestId>0CCDF65E-6050-412D-AD68-FA3D9196836C</RequestId>
    <SystemParameters>
        <SystemParameter>
            <Description>Client IP address</Description>
            <DemoValue>192.168.1.1</DemoValue>
            <ParamName>CaClientIp</ParamName>
            <ParamType>string</ParamType>
        </SystemParameter>
        <SystemParameter>
            <Description>Request domain name</Description>
            <DemoValue>api.aliyun.com</DemoValue>
            <ParamName>CaDomain</ParamName>
            <ParamType>string</ParamType>
        </SystemParameter>
        <SystemParameter>
            <Description>Request time (UTC)</Description>
            <DemoValue>2016-01-30T03:53:16Z</DemoValue>
            <ParamName>CaRequestHandleTime</ParamName>
            <ParamType>string</ParamType>
        </SystemParameter>
        <SystemParameter>
            <Description>ConsumerAppId</Description>
            <DemoValue>123456</DemoValue>
            <ParamName>CaAppId</ParamName>
            <ParamType>string</ParamType>
        </SystemParameter>
        <SystemParameter>
            <Description>RequestId</Description>
            <DemoValue>7157EBD9-4684-4827-B3B0-9B32D186819B</DemoValue>
            <ParamName>CaRequestId</ParamName>
            <ParamType>string</ParamType>
        </SystemParameter>
        <SystemParameter>
            <Description>Http Schema</Description>
            <DemoValue>https</DemoValue>
            <ParamName>CaHttpSchema</ParamName>
            <ParamType>string</ParamType>
        </SystemParameter>
        <SystemParameter>
            <Description>Proxy</Description>
            <DemoValue>AliCloudApiGateway</DemoValue>
            <ParamName>CaProxy</ParamName>
            <ParamType>string</ParamType>
        </SystemParameter>
    </SystemParameters>
</DescribeSystemParametersResponse>
```

JSON format

```json
    "RequestId": "0CCDF65E-6050-412D-AD68-FA3D9196836C",
    "SystemParameters": {
        "SystemParameter": [
```

`{`

```json
                "Description": "Client IP address",
                "DemoValue": "192.168.1.1",
                "ParamName": "CaClientIp",
                "ParamType": "string"
```

`},` `{`

```json
                "Description": "Request domain name",
                "DemoValue": "api.aliyun.com",
                "ParamName": "CaDomain",
                "ParamType": "string"
```

`},` `{`

```json
                "Description": "Request time (UTC)",
                "DemoValue": "2016-01-30T03:53:16Z",
                "ParamName": "CaRequestHandleTime",
                "ParamType": "string"
```

`},` `{`

```json
                "Description": "ConsumerAppId",
                "DemoValue": "123456",
                "ParamName": "CaAppId",
                "ParamType": "string"
```

`},` `{`

```json
                "Description": "RequestId",
                "DemoValue": "7157EBD9-4684-4827-B3B0-9B32D186819B",
                "ParamName": "CaRequestId",
                "ParamType": "string"
```

`},` `{`

```json
                "Description": "Http Schema",
                "DemoValue": "https",
                "ParamName": "CaHttpSchema",
                "ParamType": "string"
```

`},` `{`

```json
                "Description": "Proxy",
                "DemoValue": "AliCloudApiGateway",
                "ParamName": "CaProxy",
                "ParamType": "string"
```

`}` `]` `}` `}`

## 12 Data types

### 12.1 ApiGroupAttribute

Description The information about a specified API group. Node name Subnodes

| Name | Type | Description |
|---|---|---|
| GroupId | String | The API group ID, which is generated by the system and globally unique. |
| GroupName | String | The name of the API group. |
| SubDomain | String | The second-level domain name that corresponds to the API group and is used by the CNAME of the custom domain name. |
| Description | String | The description of the API group. |
| CreatedTime | String | The creation time (UTC) of the API group. |
| ModifiedTime | String | The last modification time (UTC) of the API group. |
| RegionId | String | The region to which the API group belongs. |
| TrafficLimit | Integer | The upper QPS limit of the API group. The default value is 500. You can increase the upper limit by submitting an application. |
| BillingStatus | String | The billing status of the API group. Valid values: NORMAL: The API group is normal. LOCKED: The API group is locked due to overdue payments. |
| IllegalStatus | String | The validity status of the API group. Valid values: NORMAL: The API group is normal. LOCKED: The API group is locked because it is not valid. |

### 12.2 ApiHisItem

The information about a published API. Node name Subnodes

| Name | Type | Description |
|---|---|---|
| RegionId | String | The region to which the API belongs. |
| GroupId | String | The ID of the API group. |
| GroupName | String | The name of the API group. |
| StageName | String | The name of the runtime environment. Valid values: RELEASE TEST |
| ApiId | String | The ID of the API. |
| ApiName | String | The name of the API. |
| Description | String | The description of the API. |
| HistoryVersion | String | The history version of the API. |
| Status | String | Indicates whether an API version is effective. Valid values: ONLINE and OFFLINE. |
| DeployedTime | String | The publishing time (UTC) of the API. |

### 12.3 ApiInfo

Description The information about a published API. Node name Subnodes

| Name | Type | Description |
|---|---|---|
| RegionId | String | The region to which the API belongs. |
| GroupId | String | The ID of the API group. |
| GroupName | String | The name of the API group. |

| Name | Type | Description |
|---|---|---|
| StageName | String | The name of the runtime environment. Valid values: RELEASE TEST |
| ApiId | String | The ID of the API. |
| ApiName | String | The name of the API. |
| Description | String | The API description. |
| Visibility | String | Indicates whether the API is public. Valid values: PUBLIC PRIVATE |
| BoundTime | String | The binding time of the API. |

### 12.4 ApiPluginSummary

Description The summary of an API that is bound to a plug-in. Node name Subnodes

| Name | Type | Description |
|---|---|---|
| RegionId | String | The region where the API is located. |
| GroupId | String | The ID of the group to which the API belongs. |
| GroupName | String | The name of the group to which the API belongs. |
| ApiId | String | The ID of the API. |
| ApiName | String | The name of the API. |
| Description | String | The description of the API. |
| StageName | String | The name of the stage. |

### 12.5 ApiSummary

Description The API summary information. Node name Subnodes

| Name | Type | Description |
|---|---|---|
| RegionId | String | The region to which the API belongs. |
| GroupId | String | The ID of the API group. |
| GroupName | String | The name of the API group. |
| ApiId | String | The ID of the API. |
| ApiName | String | The name of the API. |
| Description | String | The description of the API. |
| Visibility | String | Indicates whether the API is public. Valid values: PUBLIC PRIVATE |
| CreatedTime | String | The creation time (UTC) of the API. |
| ModifiedTime | String | The modification time (UTC) of the API. |

### 12.6 AppAttribute

Description The application information. Node name Subnodes

| Name | Type | Description |
|---|---|---|
| AppId | Long | The application ID. |

| eveloper Guide·Data types |   | API Gatewa |
|---|---|---|

| Name | Type | Description |
|---|---|---|
| AppName | String | The application name. |
| Description | String | The application description. |
| CreatedTime | String | The creation time (UTC) of the application. |
| ModifiedTime | String | The modification time (UTC) of the application. |

### 12.7 AppItem

Description The application information. Node name Subnodes

| Name | Type | Description |
|---|---|---|
| AppId | Long | The application ID. |
| AppName | String | The application name. |
| Description | String | The application description. |

### 12.8 AuthorizedApi

Description The mappings between applications and an API. Node name Subnodes

| Name | Type | Description |
|---|---|---|
| RegionId | String | The region to which the API belongs. |
| GroupId | String | The API group ID, which is generated by the system and globally unique. |
| GroupName | String | The name of the API group. |

| PI Gateway |   | Developer Guide·Data type |
|---|---|---|

| Name | Type | Description |
|---|---|---|
| StageName | String | The name of the runtime environment. Valid values: RELEASE TEST |
| Operator | String | The authorizer. Valid values: PROVIDER: API owner CONSUMER: API caller |
| ApiId | String | The unique identifier of the API, which is automatically generated by the system. |
| ApiName | String | The name of the API. |
| AuthorizationSource | String | The authorization source. Valid values: CONSOLE API |
| Description | String | The authorization description. |
| AuthorizedTime | String | The authorization time (UTC). |

### 12.9 AuthorizedApp

Description The application authorization information of APIs. Node name Subnodes

| Name | Type | Description |
|---|---|---|
| StageName | String | The name of the runtime environment. Valid values: RELEASE TEST |
| AppId | Long | The application ID, which is generated by the system and globally unique. |
| AppName | String | The name of the application. |
| Operator | String | The authorizer. Valid values: PROVIDER: API provider CONSUMER: API caller |

| eveloper Guide·Data typ | es | API Gatewa |
|---|---|---|
| Name | Type | Description |
| AuthorizationSource | String | The authorization source. Valid values: CONSOLE API |
| Description | String | The authorization description. |
| AuthorizedTime | String | The authorization time (UTC). |

### 12.10 ConstantParameter

Description The information about constant input parameters. Node name Subnodes

| Name | Type | Description |
|---|---|---|
| ServiceParameterName | String | The name of the backend parameter. |
| ConstantValue | String | The parameter value. |
| Location | String | The parameter location. Valid values: BODY, HEAD, QUERY, and PATH. |
| Description | String | The description of the parameter. |

### 12.11 CustomDomain

Description The domain name information. Node name Subnodes

| Name | Type | Description |
|---|---|---|
| DomainName | String | The domain name. |
| CertificateId | String | The unique ID of the SSL certificate, which is automatically generated by the system. |

| PI Gateway |   | Developer Guide·Data type |
|---|---|---|
| Name | Type | Description |
| CertificateName | String | The SSL certificate name. |
| DomainCNAMEStatus | String | The domain name resolution status. Valid values: RESOLVED UNRESOLVED |
| DomainBindingStatus | String | The binding status of the custom domain name. Valid values: BINDING: The domain name has been bound. BOUND: The domain name has not been bound. |

### 12.12 DeployedApiItem

Description The information about a published API. Node name Subnodes

| Name | Type | Description |
|---|---|---|
| RegionId | String | The region to which the API belongs. |
| GroupId | String | The ID of the API group. |
| GroupName | String | The name of the API group. |
| StageName | String | The name of the runtime environment. Valid values: RELEASE TEST |
| ApiId | String | The ID of the API. |
| ApiName | String | The name of the API. |
| Description | String | The description of the API. |
| Visibility | String | Indicates whether the API is public. Valid values: PUBLIC PRIVATE |
| DeployedTime | String | The publising time (UTC) of the API. |

### 12.13 DeployedInfo

Description The information about API publishing. Node name Subnodes

| Name | Type | Description |
|---|---|---|
| StageName | String | The name of the runtime environment. Valid values: RELEASE and TEST. |
| EffectiveVersion | String | The effective version. |
| DeployedStatus | String | The deployment status. Valid values: DEPLOYED and NONDEPLOYED. |

### 12.14 DomainItem

Description The domain name used to call an API. Node name Subnodes

| Name | Type | Description |
|---|---|---|
| DomainName | String | The domain name used to call an API. |

### 12.15 ErrorCodeSample

Description The sample error codes. Node name Subnodes

| Name | Type | Description |
|---|---|---|
| Code | String | The error code. |
| Message | String | The error message. |
| Description | String | The error description. |

### 12.16 MonitorItem

Description The monitoring metric information. Node name Subnodes

| Name | Type | Description |
|---|---|---|
| ItemTime | String | The time of the monitoring metric. The time format follows the ISO 8601 standard and UTC time is used. The format is YYYY-MM- DDThh:mm:ssZ. |
| ItemValue | String | The value corresponding to the monitoring metric. |

### 12.17 PluginAttribute

Description The details of a plug-in. Node name Subnodes

| Name | Type | Description |
|---|---|---|
| PluginId | String | The ID of the plug-in. |
| PluginType | String | The type of the plug-in. |
| PluginName | String | The name of the plug-in. |
| PluginData | String | The definition statement of the plug-in. |

| eveloper Guide·Data types |   | API Gatewa |
|---|---|---|

| Name | Type | Description |
|---|---|---|
| RegionId | String | The region where the plug-in is located. |
| Description | String | The description of the plug-in. |
| CreatedTime | String | The time when the plug-in was created. The time is displayed in GMT. |
| ModifiedTime | String | The time when the plug-in was modified. The time is displayed in GMT. |

### 12.18 Region

Description The region information. Node name Subnodes

| Name | Type | Description |
|---|---|---|
| RegionId | String | The region ID. |
| LocalName | String | The region name. |
| Endpoint | String | The domain name, such as gateway.cn-hangzhou.aliyuncs.com. |

### 12.19 RequestConfig

Description The frontend information. Node name Subnodes

| Name | Type | Description |
|---|---|---|
| RequestProtoc ol | String | The protocol type supported by the API. Valid values: HTTP and HTTPS. Separate multiple values with commas (,), such as "HTTP,HTTPS". |

| A | PI Gateway |   | Developer Guide·Data type | s |
|---|---|---|---|---|

| Name | Type | Description |
|---|---|---|
| RequestHttpMe thod | String | The HTTP method. Valid values: GET, POST, DELETE, PUT, HEADER, TRACE, PATCH, CONNECT, and OPTIONS. |
| RequestPath | String | The API path. For example, in API address http://api.a.com： 8080/object/add?key1=value1&key2=value2, RequestPath is /object/add. |
| BodyFormat | String | The server data transmission method used for POST and PUT requests. Valid values: FORM and STREAM. FORM indicates that data in key-value pairs is transmitted as forms. STREAM indicates that data is transmitted as byte streams. |
| PostBodyDescri ption | String | The description of the request body. |

### 12.20 RequestParameter

Description The information about frontend input parameters. Node name Subnodes

| Name | Type | Description |
|---|---|---|
| ApiParameterName | String | Parameter |
| Location | String | The parameter location. Valid values: BODY, HEAD, QUERY, and PATH. |
| ParameterType | String | The parameter type. Valid values: String, Int, Long, Float, Double, and Boolean. |
| Required. | String | Indicates whether the parameter is required. Valid values: REQUIRED and OPTIONAL. |
| DefaultValue | String | The default value. |
| DemoValue | String | An example of the parameter value. |
| MaxValue | Long | The maximum parameter value when ParameterType is set to Int, Long, Float, or Double. |
| MinValue | Long | The minimum parameter value when ParameterType is set to Int, Long, Float, or Double. |

| Name | Type | Description |
|---|---|---|
| MaxLength | Long | The maximum parameter length when ParameterType is set to String. |
| MinLength | Long | The minimum parameter length when ParameterType is set to String. |
| RegularExpression | String | The regular expression used for parameter validation when ParameterType is set to String. |
| JsonScheme | String | The JSON Schema used for JSON validation when ParameterType is set to String. |
| EnumValue | String | The hash values that can be entered when ParameterType is set to Int, Long, Float, Double, or String. Separate different values with commas (,), such as 1,2,3,4,9 or A,B,C,E,F. |
| DocShow | String | Indicates whether the document is public. Valid values: PUBLIC and PRIVATE. |
| DocOrder | Integer | The order in the document. |
| Description | String | The description of the parameter. |

### 12.21 ServiceConfig

Description The information about a backend service call. Node name Subnodes

| Name | Type | Description |
|---|---|---|
| ServiceProtoc ol | String | The protocol used by the backend service. Valid values: HTTP and HTTPS. |
| ServiceAddres s | String | The address used to call the backend service. For example, in the backend service address http://api.a.com:8080/object/add? key1=value1&key2=value2, ServiceAddress is http://api.a.com:8080. |
| ServicePath | String | The path used to call the backend service. For example, in the backend service address http://api.a.com:8080/object/add? key1=value1&key2=value2, ServicePath is /object/add. |
| ServiceHttpMe thod | String | The HTTP method used to call a backend service. Valid values: GET, POST, DELETE, PUT, HEADER, TRACE, PATCH, CONNECT, and OPTIONS. |

| PI Gateway |   | Developer Guide·Data type |
|---|---|---|

| Name | Type | Description |
|---|---|---|
| ServiceTimeou t | String | The timeout period of the backend service, in millisecond. |
| Mock | String | Indicates whether the Mock mode is enabled. Valid values: TRUE and FALSE. |
| MockResult | String | The result returned when the Mock mode is enabled. |

### 12.22 ServiceParameter

Description The information about input parameters for a backend service call. Node name Subnodes

| Name | Type | Description |
|---|---|---|
| ServiceParameterName | String | The name of the backend parameter. |
| Location | String | The parameter location. Valid values: BODY, HEAD, QUERY, and PATH. |
| ParameterType | String | The type of the backend parameter. Valid values: STRING, NUMBER, and BOOLEAN. |

### 12.23 ServiceParameterMap

Description The mappings between frontend input parameters and backend input parameters. Node name Subnodes

| Name | Type | Description |
|---|---|---|
| ServiceParameter Name | String | The name of the backend parameter. |

| Name | Type | Description |
|---|---|---|
| RequestParamete rName | String | The name of the corresponding frontend input parameter. It must be included in RequestParametersObject and matches ApiParameterName in RequestParameter data. |

### 12.24 Special

Description The special throttling policy. Node name Subnodes

| Name | Type | Description |
|---|---|---|
| SpecialKey | String | The AppId or user account corresponding to SpecialType. |
| TrafficValue | Integer | The throttling value. |

### 12.25 SpecialPolicy

Description The information about a special throttling policy. Node name Subnodes

| Name | Type | Description |
|---|---|---|
| SpecialType | String | The type of the special throttling policy. Valid values: APP USER |
| Specials | Array | The returned information about a special throttling policy. It is an array consisting of Special data. |

### 12.26 StageInfo

The runtime environment information. Node name Subnodes

| Name | Type | Description |
|---|---|---|
| StageId | String | The ID of the runtime environment. |
| StageName | String | The name of the runtime environment. |
| Description | String | The description of the runtime environment. |

### 12.27 SystemParameter

Description The system input parameter. Node name Subnodes

| Name | Type | Description |
|---|---|---|
| ParameterName | String | The name of the system parameter. Valid values: CaClientIp, CaDomain, CaRequestHandleTime, CaAppId, CaRequestId, CaHttpSchema, and CaProxy. |
| ServiceParameter Name | String | The name of the corresponding backend parameter. |
| Location | String | The parameter location. Valid values: BODY, HEAD, QUERY, and PATH. |
| DemoValue | String | An example of the parameter value. |
| Description | String | The description of the system parameter. |

### 12.28 SystemParamItem

Description The information about a specified system parameter. Node name Subnodes

| Name | Type | Description |
|---|---|---|
| ParamName | String | The name of the system parameter. |
| ParamType | String | The type of the system parameter. |
| DemoValue | String | An example of the parameter value. |
| Description | String | The description of the system parameter. |

## 13 Error codes

When you call an API management operation, such as CreateAPI, ModifyAPI, or DeleteAPI, error codes that are listed in the following tables may be reported. Server errors The reported HTTP status code is 5XX, which indicates that services are unavailable. We recommend that you call the API operation again.

| Error code | Error message | HTTP status code | Description | Solution |
|---|---|---|---|---|
| ServiceUnavailable | The request has failed due to a temporary failure of the server. | 503 | The error message returned because an API response times out. | Try again later. |
| InternalError | The request processing has failed due to some unknown error, exception or failure. | 500 | The error message returned because an internal error has occurred. | Submit a ticket for consulting. |

Client errors The reported HTTP status code is 4XX, which indicates a business error. The business error can be a parameter error, an error due to access control, or a business logic error. You need to carefully view error information before you troubleshoot issues.

| Error code | Error message | HTTP status code | Description | Solution |
|---|---|---|---|---|
| Repeated%s | The specified %s is repeated. | 400 | The error message returned because the parameter has been used. (%s is a placeholder. A specified parameter name or prompt will be provided when you call an API operation.) | Modify the parameter and try again later. |
| RepeatedCommit | Resubmit request. | 400 | The error message returned because the request has been submitted. | Do not repeatedly submit the same request . |

| Error code | Error message | HTTP status code | Description | Solution |
|---|---|---|---|---|
| Missing%s | The %s is mandatory for this action. | 400 | The error message returned because the %s parameter is not specified. | Specify the %s parameter as prompted and try again later. |
| MissingAppIdOrAp pOwner | AppId or AppOwner must have a valid value. | 400 | The error message returned because the AppId or AppOwner parameter is not specified. | Specify the AppId or AppOwner parameter, or both of them. |
| Invalid%s | The specified parameter %s value is not valid. | 400 | The error message returned because the specified %s parameter is invalid. | View parameter configuration limits, modify the parameter as prompted, and try again later. |
| NotFound%s | Cannot find resource according to your specified %s. | 400 | The error message returned because no resources can be found based on the settings of the specified %s parameter. | Check whether the %s parameter is correctly specified. |
| InvalidFormat%s | The specified parameter %s value is not well formatted. | 400 | The error message returned because the value of the %s parameter is in an invalid format. | View requirements for the format of the parameter value, modify the format, and try again later. |
| Duplicate%s | The specified parameter %s value is duplicate. | 400 | The error message returned because the specified %s parameter has been used. | Change the parameter value and try again later. |
| DependencyViolati on%s | The specified %s has %s definitions. | 400 | The error message returned because the parameter dependency is invalid. | Remove the dependency and then delete the parameter. A parameter that others are dependent on cannot be deleted. |

| Error code | Error message | HTTP status code | Description | Solution |
|---|---|---|---|---|
| Forbidden%s | Not allowed to operate on the specified %s. | 403 | The error message returned because you are not allowed to perform specified operations. | Obtain the permissions to perform specified operations. |
| NoPermission | User is not authorized to operate on the specified resource. | 403 | The error message returned because you are not authorized to perform operations on the specified resource. | Grant permissions of operations on the specified resource. |
| ExceedLimit%s | The specified %s count exceeds the limit. | 400 | The error message returned because the number of APIs, API groups, or apps created under your Alibaba Cloud account exceeds the quota. | Adjust the number. |
| UserNotFound | The specified user can not be found. | 404 | The error message returned because the specified user does not exist. |   |
| Invalid%s.LengthLi mit | The parameter %s length exceeds the limit. | 400 | The error message returned because the value of the %s parameter exceeds the upper limit in length. | Change the parameter value and try again later. |
| InvalidApiDefault | The ApiDefault value exceeds limit. | 400 | The error message returned because the value of the ApiDefault parameter exceeds the threshold. | Change the parameter value. Maximum value: 100000000. |

| Error code | Error message | HTTP status code | Description | Solution |
|---|---|---|---|---|
| InvalidAppDefault | The AppDefault value must smaller than the UserDefault and ApiDefault. | 400 | The error message returned because the value of the AppDefault parameter does not meet requirements. | Change the value of the AppDefault parameter. The value must be less than that of the ApiDefault parameter and also less than that of the UserDefault parameter. |
| InvalidUserDefault | The UserDefault value must bigger than the AppDefault and smaller than the ApiDefault. | 400 | The error message returned because the value of the UserDefault parameter does not meet requirements. | Change the value of the UserDefault parameter. The value must be greater than that of the AppDefault parameter but less than that of the ApiDefault parameter. |
| InvalidParamMappi ng | Parameters must be fully mapped. | 400 | The error message returned because the parameter mapping is invalid. | When you create an API, map each request parameter to a backend parameter. |
| EqualSignature | The new signature is the same as the old. | 400 | The error message returned because the new backend signature key is the same as the old one. | Modify the new backend signature key. Make sure that the newly configured key- secret pair is different from the old one. |
| CertificateNotMatc h | The domain does not match the one in the certificate. | 400 | The error message returned because the specified domain name does not match the domain name in the certificate. | Make sure that the specified domain name matches the domain name in the certificate. |

| Error code | Error message | HTTP status code | Description | Solution |
|---|---|---|---|---|
| CertificateKeyNot Match | The certificate private key does not match the public key. | 400 | The error message returned because the public and private keys in the certificate do not match. | Check the certificate to match the public and private keys in the certificate. |

Common client errors The reported HTTP status code is 4XX, which indicates a business error and may be reported when you call APIs of Alibaba Cloud services. The business error can be an invalid request format, an incorrect request method, missing required parameters, an invalid parameter value format, an invalid signature, or an error due to throttling. You need to carefully view error information before you troubleshoot issues.

| Description | Error code | Error message | HTTP status code | Solution |
|---|---|---|---|---|
| The specified API cannot be found. | InvalidApi.NotFoun d | Specified api is not found,please check your url and method. | 404 | Check whether the specified API operation name is valid. The name is case-sensitive. |
| A required parameter is not specified. | Missing{Parameter Name} | {ParameterName} is mandatory for this action. | 400 | Specify the required parameter. |
| The AccessKey ID cannot be found. | InvalidAccessKeyId .NotFound | Specified access key is not found. | 404 | Check whether a valid AccessKey ID is used when you call an API operation. |
| The AccessKey ID is disabled. | InvalidAccessKeyId .Inactive | Specified access key is disabled. | 400 | Check whether the AccessKey pair is available. |
| The format of the date or timestamp is invalid. | InvalidTimeStamp. Format | Specified time stamp or date value is not well formatted. | 400 | Check the format. |
| The difference between the client time and server time exceeds 15 minutes. | InvalidTimeStamp. Expired | Specified time stamp or date value is expired. | 400 | Check the timestamp. |

| Description | Error code | Error message | HTTP status code | Solution |
|---|---|---|---|---|
| The SignatureNonce setting is repeated. | SignatureNonceUs ed | Specified signature nonce was used already. | 400 | Check whether the SignatureNonce setting is repeated when you call an API operation at the client. |
| The returned parameter value is in an invalid format. | InvalidParameter.F ormat | Specified parameter format is not valid. | 400 | Specify the parameter only in the XML or JSON format. |
| The parameter value verification fails. | Invalid{Parameter Name} | Specified parameter {ParameterName} is not valid. | 400 | Check the parameter value. |
| The HTTP request method is not supported. | UnsupportedHTTP Method | Specified signature is not matched with our calculation. | 400 | Check the request method. |
| The signature method is not supported. | InvalidSignatureMe thod | Specified signature method is not valid. | 400 | Specify an available signature method. This parameter can be left empty. |
| The signature verification fails. | SignatureDoesNot Match | Specified signature is not matched with our calculation. | 400 | Check the signature and resolve the issue accordingly. |
| The user-level call frequency exceeds the threshold. | Throttling.User | Request was denied due to user flow control. | 400 | Reduce the call frequency. |
| The API-level call frequency exceeds the threshold. | Throttling.API | Request was denied due to api flow control. | 400 | Reduce the call frequency. |
| The AccessKey ID is missing. | MissingSecurityTo ken | SecurityToken is mandatory for this action. | 400 | Check whether you specify a valid AccessKey ID. |
