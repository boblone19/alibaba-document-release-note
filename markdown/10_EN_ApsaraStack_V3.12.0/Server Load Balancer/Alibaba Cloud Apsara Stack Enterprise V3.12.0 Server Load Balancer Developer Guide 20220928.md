---
title: "Alibaba Cloud Apsara Stack Enterprise V3.12.0 Server Load Balancer Developer Guide 20220928"
product_version: "V3.12.0"
doc_version: "20220928"
pdf_pages: 230
source_pdf: "Alibaba Cloud Apsara Stack Enterprise V3.12.0 Server Load Balancer Developer Guide 20220928.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/01_ApsaraStackEnterprise/V3.12/%E7%BD%91%E7%BB%9C/Alibaba%20Cloud%20Apsara%20Stack%20Enterprise%20V3.12.0%20Server%20Load%20Balancer%20Developer%20Guide%2020220928.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes+edge-junk)
---

# Alibaba Cloud Apsara Stack Enterprise V3.12.0 Server Load Balancer Developer Guide 20220928

## Table of Contents

- 1 Make SDK calls by using ASAPI
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
  - 2.1 List of operations by function
  - 2.2 Make API requests
  - 2.3 RAM authentication
  - 2.4 Common parameters
  - 2.5 CLB instances
    - 2.5.1 CreateLoadBalancer
    - 2.5.2 DeleteLoadBalancer
    - 2.5.3 ModifyLoadBalancerInstanceSpec
    - 2.5.4 ModifyLoadBalancerInternetSpec
    - 2.5.5 SetLoadBalancerName
    - 2.5.6 SetLoadBalancerStatus
    - 2.5.7 DescribeLoadBalancerAttribute
    - 2.5.8 DescribeLoadBalancers
    - 2.5.9 DescribeRegions
    - 2.5.10 DescribeZones
  - 2.6 Listener
    - 2.6.1 TCP listeners
      - 2.6.1.1 CreateLoadBalancerTCPListener
      - 2.6.1.2 SetLoadBalancerTCPListenerAttribute
      - 2.6.1.3 DescribeLoadBalancerTCPListenerAttribute
    - 2.6.2 UDP listeners
      - 2.6.2.1 CreateLoadBalancerUDPListener
      - 2.6.2.2 SetLoadBalancerUDPListenerAttribute
      - 2.6.2.3 DescribeLoadBalancerUDPListenerAttribute
    - 2.6.3 HTTP listeners
      - 2.6.3.1 CreateLoadBalancerHTTPListener
      - 2.6.3.2 SetLoadBalancerHTTPListenerAttribute
      - 2.6.3.3 DescribeLoadBalancerHTTPListenerAttribute
    - 2.6.4 HTTPS listeners
      - 2.6.4.1 CreateLoadBalancerHTTPSListener
      - 2.6.4.2 SetLoadBalancerHTTPSListenerAttribute
      - 2.6.4.3 DescribeLoadBalancerHTTPSListenerAttribute
      - 2.6.4.4 DescribeHealthStatus
    - 2.6.5 Access control
      - 2.6.5.1 SetListenerAccessControlStatus
      - 2.6.5.2 DescribeListenerAccessControlAttribute
      - 2.6.5.3 AddListenerWhiteListItem
      - 2.6.5.4 RemoveListenerWhiteListItem
    - 2.6.6 Forwarding rules
      - 2.6.6.1 CreateRules
      - 2.6.6.2 DeleteRules
      - 2.6.6.3 DescribeRules
      - 2.6.6.4 SetRule
      - 2.6.6.5 DescribeRuleAttribute
    - 2.6.7 DeleteLoadBalancerListener
    - 2.6.8 StopLoadBalancerListener
    - 2.6.9 StartLoadBalancerListener
  - 2.7 Server certificates
    - 2.7.1 UploadServerCertificate
    - 2.7.2 DeleteServerCertificate
    - 2.7.3 DescribeServerCertificates
    - 2.7.4 SetServerCertificateName
    - 2.7.5 UploadCACertificate
    - 2.7.6 DeleteCACertificate
    - 2.7.7 DescribeCACertificates
    - 2.7.8 SetCACertificateName
  - 2.8 Backend Servers
    - 2.8.1 AddBackendServers
    - 2.8.2 RemoveBackendServers
    - 2.8.3 SetBackendServers
  - 2.9 vServer Groups
    - 2.9.1 CreateVServerGroup
    - 2.9.2 SetVServerGroupAttribute
    - 2.9.3 AddVServerGroupBackendServers
    - 2.9.4 RemoveVServerGroupBackendServers
    - 2.9.5 ModifyVServerGroupBackendServers
    - 2.9.6 DeleteVServerGroup
    - 2.9.7 DescribeVServerGroups
    - 2.9.8 DescribeVServerGroupAttribute
  - 2.10 Primary/secondary Server Groups
    - 2.10.1 CreateMasterSlaveServerGroup
    - 2.10.2 DeleteMasterSlaveServerGroup
    - 2.10.3 DescribeMasterSlaveServerGroups
    - 2.10.4 DescribeMasterSlaveServerGroupAttribute
  - 2.11 Tags
    - 2.11.1 AddTags
    - 2.11.2 DescribeTags
    - 2.11.3 RemoveTags
  - 2.12 Error codes

using ASAPI

## 1 Make SDK calls by using ASAPI

### 1.1 Overview

This topic describes the architecture and features of Apsara Stack API (ASAPI). ASAPI is a platform that integrates all features and is the only portal to connect to Apsara Stack. ASAPI can categorize, audit, and manage API operations. It can also assemble and customize existing operations and adapt to your operations. Each cloud service can call ASAPI for required data and features, which avoids inconsistent operations caused by different calling methods and separate encapsulation. This can ensure the operation program integrity and improve development efficiency and code portability. ASAPI allows you to manage and call operations in a centralized manner and customize development. ASAPI supports access to most cloud services deployed in Apsara Stack and supports passthrough or encapsulation of different backend APIs. This way, operations can be called using the same method. ASAPI allows you to use SDKs and API portals to call APIs registered on ASAPI, customize SDKs, and manage versions of Apsara Stack, services, and APIs. using ASAPI

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
operation name in the search box, and then click the search icon. using ASAPI
4. View and remember the service name, API operation name, and API version.

### 1.4 Obtain the endpoint of ASAPI

This topic describes how to obtain the endpoint of ASAPI in the Apsara Stack Operations console. Procedure
1. In the address bar, enter the URL region-id.aso.intranet-domain-id.com and press the Enter key.
Not e You can select a language from the drop-down list in the upper-right corner of the page.
2. Enter your username and password.
Not e Obtain the username and password for logging on to the ASO console from the deployment personnel or an administrator. When you log on to the ASO console for the first time, you must change the password of your username as prompted. To enhance security, a password must meet the following requirements: It must contain uppercase and lowercase letters. It must contain digits. It must contain special characters such as exclamation points (!), at signs (@), number signs (#), using ASAPI dollar signs ($), and percent signs (%). It must be 10 to 20 characters in length.
3. Click Log On to go to the ASO console.
4. In the left-side navigation pane, choose Product s > Product List > Apsara Inf rast ruct ure
Management Framework to go to the Apsara Infrastructure Management Framework console.
5. In the left-side navigation pane of the Apsara Infrastructure Management Framework console, click
Report s.
6. On the All Report s page, search for Regist rat ion Vars of Services. Click Regist rat ion Vars of
Services.
7. On the Regist rat ion Vars of Services page, move the pointer over Service and click the
icon next to it. In the dialog box that appears, search for asapi.
8. Right-click the Service Regist rat ion column corresponding to ASAPI and select Show More.
9. In the Det ails dialog box, the value of asapi.gat eway.endpoint is the logon URL of the Apsara
ASAPI Management platform. using ASAPI

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
using ASAPI Not e An AccessKey pair is automatically allocated to a level-1 organization. Subordinate organizations use the same AccessKey pair as their level-1 organization. Obtain the AccessKey pair of a personal account To obtain the AccessKey pair of a personal account, perform the following operations:
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

This topic describes how to obtain and use Apsara Stack SDK for Java. Prerequisites You must have an authorized account and an AccessKey pair (AccessKey ID and AccessKey secret) to use Apsara Stack SDK for Java. For more information about how to obtain and view your AccessKey pair in the ASCM console, see Obtain an AccessKey pair. You have obtained the endpoint of Asapi. For more information about how to obtain the endpoint of Asapi, see Obtain the endpoint of Asapi. using ASAPI Apsara Stack SDK for Java supports JDK 1.6 and later. Add dependencies Add dependencies to pom.xml:

```xml
<dependency>
    <groupId>com.aliyun</groupId>
    <artifactId>asapi</artifactId>
    <version>0.0.1-SNAPSHOT</version>
    <scope>system</scope>
    <systemPath>${project.basedir}/lib/aliyun-java-sdk-asapi.jar</systemPath>
</dependency>
```

Use Apsara Stack SDK for Java You can call API operations on Asapi by using GET and POST requests. GET requests

```
 ASClient client = new ASClient();
// Form 1 String result = client.doGet(endpoint, parameters); // Form 2 String result = client.doRequest(endpoint, parameters);
```

POST requests using ASAPI

```
// Obtain the endpoint of Asapi. String endpoint = "http://xxx/asapi/v3"; // Set request parameters. Map<String, String> parameters = new HashMap<String, String>(); // Set parameters for the product. parameters.put("Product", "ascm"); // The product name must be the same as the name displayed in the corresponding API directory. parameters.put("Action", "AddUser"); // The API name must be in the same case as that in the API directory. parameters.put("Version", "2019-05-10"); // The API version. // Set authorization-related parameters. parameters.put("AccessKeyId", "<your-access-key-id>"); // The AccessKey ID of th e authorized account. parameters.put("AccessKeySecret", "<your-access-key-secret>"); // The AccessKey secret o f the authorized account. // Set business parameters. parameters.put("username", "<your-username>"); // The username used to l og on to the ASCM console. parameters.put("password", "<your-password>"); // The password used to l og on to the ASCM console. JSONObject jsonObject = new JSONObject(); jsonObject.put("param1", "json parameter 1"); jsonObject.put("param2", "json parameter 2"); parameters.put("json", jsonObject.toJSONString()); // Create an ASClient instance for initiating requests. ASClient client = new ASClient(); // Add request headers. client.addHeader("x-acs-resourceGroupId", "112233"); // Initiate the request and obtain the response. String result = client.doPost(endpoint, parameters);
```

### 1.9 SDK for Node.js

This topic describes how to obtain and use Apsara Stack SDK for Node.js. Prerequisites You must have an authorized account and an AccessKey pair (AccessKey ID and AccessKey secret) to use Apsara Stack SDK for Node.js. For more information, see Obtain an AccessKey pair. You have obtained the endpoint of Asapi. For more information about how to query the endpoint of Asapi, see Obtain the endpoint of Asapi. You have obtained the region ID. For more information about how to query the region ID, see Query the region ID. Add dependencies
1. Install Apsara Stack SDK for Node.js.

```
 tnpm install --save @ali/asapi-nodejs-sdk
```

2. If mocha.opts depends on eggjs, you must configure mocha.opts.
using ASAPI

```
--recursive --colors --timeout 60000 --reporter mochawesome --require co-mocha --require egg-ts-helper/register --require espower-typescript/guess -- require intelli-espower-loader
```

Use SDK for Node.js The following example shows how to use Apsara Stack SDK for Node.js:
1. Create a client instance. To create a client instance, you must set the region ID, endpoint,
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
3. Initiate the request and handle any responses or exceptions.

```
// Speciofy the Asapi endpoint. const API_GATEWAY = "http://xxxx/asapi/v3" // Create the rpc client. const asapiClient = ctx.service.sdk.rpcClient // Set request parameters. let params = {
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

If an application used the POP SDK to call cloud services, you must switch the gateway to ASAPI by performing the following operations: Procedure Reference the following sample code and add required common parameters and the Product Name field to the request header. Use the code to switch the gateway to ASAPI. using ASAPI Not e Different services use different endpoints in the POP SDK. However, ASAPI provides only one endpoint. You cannot identify the service to which an API operation belongs based on the API operation name and the version number. For example, both ECS and KVStore for Redis provide the DescribeInstances API operation of the 2015-01-01 version. Sample code The following sample code shows how to use POP SDK to call ECS ASAPI.

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

### 2.1 List of operations by function

Instance operations

| Operation | Description |
|---|---|
| CreateLoadBalancer | Creates an SLB instance. |
| DeleteLoadBalancer | Deletes an SLB instance. |
| SetLoadBalancerStatus | Sets the status of an SLB instance. |
| SetLoadBalancerName | Modifies the name of an SLB instance. |
| DescribeLoadBalancers | Queries created SLB instances. |
| DescribeLoadBalancerAttribute | Queries detailed information of a specified SLB instance. |
| DescribeRegions | Queries available regions. |
| DescribeZones | Queries the zone information of a specified region. |

Listener operations

| Operation | Description |
|---|---|
| T CP list eners |   |
| CreateLoadBalancerTCPListener | Creates a TCP listener. |
| SetLoadBalancerTCPListenerAttribute | Modifies the configurations of a TCP listener. |
| DescribeLoadBalancerTCPListenerAttribute | Queries the configurations of a TCP listener. |
| UDP list eners |   |
| CreateLoadBalancerUDPListener | Creates a UDP listener. |
| SetLoadBalancerUDPListenerAttribute | Modifies the configurations of a UDP listener. |
| DescribeLoadBalancerUDPListenerAttribute | Queries the configurations of a UDP listener. |
| HT T P list eners |   |

| D | eveloper Guide·API reference Server Load Balance | r |
|---|---|---|

| Operation | Description |
|---|---|
| CreateLoadBalancerHTTPListener | Creates an HTTP listener. |
| SetLoadBalancerHTTPListenerAttribute | Modifies the configurations of an HTTP listener. |
| DescribeLoadBalancerHTTPListenerAttribute | Queries the configurations of an HTTP listener. |
| HT T PS list eners |   |
| CreateLoadBalancerHTTPSListener | Creates an HTTPS listener. |
| SetLoadBalancerHTTPSListenerAttribute | Modifies the configurations of an HTTPS listener. |
| DescribeLoadBalancerHTTPSListenerAttribute | Queries the configurations of an HTTPS listener. |
| General list ener operat ions |   |
| StartLoadBalancerListener | Enables a listener. |
| DeleteLoadBalancerListener | Deletes a listener. |
| StopLoadBalancerListener | Disables a listener. |
| Access cont rol |   |
| SetListenerAccessControlStatus | Enables or disables access control for a specified listener. |
| DescribeListenerAccessControlAttribute | Queries the access control configurations of a specified listener. |
| AddListenerWhiteListItem | Adds an IP address to the whitelist of a specified listener. |
| RemoveListenerWhiteListItem | Removes an IP address from the whitelist of a specified listener. |
| Forwarding rules |   |
| CreateRules | Adds forwarding rules to a specified HTTP or HTTPS listener. |
| DeleteRules | Deletes forwarding rules. |
| DescribeRules | Queries the configured forwarding rules of a specified listener. |
| SetRule | Modifies the target VServer group of a specified forwarding rule. |

| S | erver Load Balancer | Developer Guide·API referenc | e |
|---|---|---|---|

| Operation | Description |
|---|---|
| DescribeRuleAttribute | Queries detailed information of a specified forwarding rule. |

Back-end server operations

| Operation | Description |
|---|---|
| AddBackendServers | Adds back-end servers. |
| RemoveBackendServers | Removes back-end servers. |
| SetBackendServers | Sets the weights of back-end servers. |
| VServer groups |   |
| CreateVServerGroup | Creates a VServer group and adds back- end servers to the VServer group. |
| SetVServerGroupAttribute | Modifies the configurations of a VServer group. |
| AddVServerGroupBackendServers | Adds back-end servers to a specified VServer group. |
| RemoveVServerGroupBackendServers | Removes back-end servers from a specified VServer group. |
| ModifyVServerGroupBackendServers | Replaces back-end servers in a specified VServer group. |
| DeleteVServerGroup | Deletes a specified VServer group. |
| DescribeVServerGroups | Queries created VServer groups. |
| DescribeVServerGroupAttribute | Queries detailed information of a specified VServer group. |
| Primary/secondary server groups |   |
| CreateMasterSlaveServerGroup | Creates a primary/secondary server group. |
| DeleteMasterSlaveServerGroup | Deletes a primary/secondary server group. |
| DescribeMasterSlaveServerGroupAttribute | Queries detailed information of a specified primary/secondary server group. |
| DescribeMasterSlaveServerGroups | Queries created primary/secondary server groups. |

Tag operations

| Operation | Description |
|---|---|
| AddTags | Adds tags to a specified SLB instance. |
| DescribeTags | Queries created tags. |
| RemoveTags | Removes tags from a specified SLB instance. |

### 2.2 Make API requests

To send an SLB API request, you must send an HTTP GET request to the SLB endpoint and add the request parameters that correspond to the API operation being called. After you call the API, the system returns a response. The request and response are encoded in UTF-8. Request syntax SLB API operations use the RPC protocol. You can call SLB API operations by sending HTTP GET requests. Use the following request syntax:

```
http://Endpoint/?Action=xx&Parameters
```

where: Endpoint: The endpoint of the SLB API is `slb.example.com` . Not e `example.com` is a custom domain name. You can contact the system administrator to obtain the domain name. For more information, see Generate the endpoint of ASAPI. Action: Name of the operation being performed. For example, to query created SLB instances, you must set the Action parameter to DescribeLoadBalancers. Version: Version of the API that you want to use. The current SLB API version is 2014-05-15. Parameters: Request parameters for the operation. Separate multiple parameters with ampersands (&). Request parameters include common parameters and operation-specific parameters. Common parameters are used for all SLB API calls regardless of the operation. For more information, see Common parameters. The following example demonstrates how to call the DescribeLoadBalancers operation in SLB. Not e The examples in this topic have been formatted for ease of reading.

```
https://slb.example.com/?Action=DescribeLoadBalancers &Format=xml &Version=2014-05-15 &Signature=xxxx%xxxx%3D &SignatureMethod=HMAC-SHA1 &SignatureNonce=15215528852396 &SignatureVersion=1.0 &AccessKeyId=key-test &TimeStamp=2016-02-23T12:46:24Z
```

… API authorization To keep your account secure, we recommend that you call SLB API operations as a RAM user. To call SLB API operations as a RAM user, you must create and add an authorization policy that grants permissions to call specific API operations. For more information about the SLB resources and API operations that can be authorized, see RAM authentication. Request signature You must sign all API requests to ensure security. Apsara stack uses the request signature to verify the identity of the API caller. SLB implements symmetric encryption with an AccessKey pair to verify the identity of the request sender. An AccessKey pair is an identity credential issued to Apsara Stack tenant accounts and RAM users. It is similar to the pair of a logon username and password. An AccessKey pair consists of an AccessKey ID and an AccessKey secret. The AccessKey ID is used to verify the identity of the user, whereas the AccessKey secret is used to encrypt and verify the signature string. You must keep your AccessKey secret confidential. For more information, see Obtain an AccessKey pair. To call an RPC API operation, you must add the signature to the SLB API request in the following format: https://endpoint/?SignatureVersion=1.0&SignatureMethod=HMAC- SHA1&Signature=xxxx%xxxx%3D&SignatureNonce=3ee8c1b8-83d3-44af-a94f-4e0ad82fd6cf Take the DescribeLoadBalancers operation as an example. If the AccessKey ID is `testid` and the AccessKey secret is `testsecret` , the following original request URL is obtained:

```
http://slb.example.com/?Action=DescribeLoadBalancers &TimeStamp=2016-02-23T12:46:24Z &Format=XML &AccessKeyId=testid &SignatureMethod=HMAC-SHA1 &SignatureNonce=3ee8c1b8-83d3-44af-a94f-4e0ad82fd6cf &Version=2014-05-26 &SignatureVersion=1.0
```

Perform the following operations to calculate the signature:
1. Use the request parameters to create a string-to-sign.

```
GET&%2F&AccessKeyId%3Dtestid&Action%3DDescribeLoadBalancers&Format%3DXML&SignatureMetho d%3DHMAC-SHA1&SignatureNonce%3D3ee8c1b8-83d3-44af-a94f-4e0ad82fd6cf&SignatureVersion%3D 1.0&TimeStamp%3D2016-02-23T12%253A46%253A24Z&Version%3D2014-05-15
```

2. Calculate the HMAC value of the string-to-sign.
Append an ampersand (&) to the AccessKey secret as the key for calculating the HMAC value. In this example, the key is `testsecret&` .

```
CT9X0VtwR86fNWSnsc6v8YG****E=
```

3. Add the signature string to the request as the Signature parameter.

```
http://slb.example.com/?Action=DescribeLoadBalancers &TimeStamp=2016-02-23T12:46:24Z &Format=XML &AccessKeyId=testid &SignatureMethod=HMAC-SHA1 &SignatureNonce=3ee8c1b8-83d3-44af-a94f-4e0ad82fd6cf &Version=2014-05-15 &SignatureVersion=1.0 &Signature=xxxx%xxxx%3D
```

### 2.3 RAM authentication

Before calling an SLB API as a RAM user, you must use an Alibaba Cloud account to create an authorization policy to assign permissions to the RAM user. In the authorization policy, you must use an Alibaba Cloud Resource Name (ARN) as the unique identifier of the resource. Available SLB resources The following table describes the ARN format for different types of SLB resources.

| Resource type | ARN format |
|---|---|
| LoadBalancer | acs:slb:$regionid:$accountid:loadbalancer/$loadbalancerid |
|   | acs:slb:$regionid:$accountid:loadbalancer/* |
|   | acs:slb:*:$accountid:loadbalancer/* |
|   | acs:slb:*:*:loadbalancer/* |
| Certificate | acs:slb:$regionid:$accountid:certificate/$servercertificateId |
|   | acs:slb:$regionid:$accountid:certificate/* |

$regionid/accoutid/servercertificateId is the resource ID. `*` indicates the corresponding resources. SLB APIs The following table lists the APIs that can be authorized and their corresponding ARN formats.

| API | ARN format |   |   |
|---|---|---|---|
| CreateLoadBalancer | acs:slb:$regionid:$accountid:loadbalancer/* |   |   |
|   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance rid |   |   |
|   |   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance |   |
| ModifyLoadBalancerInternetSpec | rid |   |   |
|   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance rid |   |   |
|   |   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance |   |
| DeleteLoadBalancer | rid |   |   |
|   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance rid |   |   |
|   |   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance |   |
| SetLoadBalancerStatus | rid |   |   |
|   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance rid |   |   |
|   |   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance |   |
| SetLoadBalancerName | rid |   |   |
| DescribeLoadBalancers | acs:slb:$regionid:$accountid:loadbalancer/* |   |   |
|   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance rid |   |   |
|   |   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance |   |
| DescribeLoadBalancerAttribute | rid |   |   |
| DescribeRegions | acs:slb:*:$accountid:* |   |   |
| UploadServerCertificate | acs:slb:%s:%s:certificate/* |   |   |
| DeleteServerCertificate | acs:slb:%s:%s:certificate/% |   |   |
| DescribeServerCertificate | acs:slb:%s:%s:certificate/% |   |   |
| SetServerCertificateName | acs:slb:%s:%s:certificate/% |   |   |
| DescribeServerCertificates | acs:slb:%s:%s:certificate/* |   |   |
|   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance rid |   |   |
|   |   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance |   |
| CreateLoadBalancerHTTPListener | rid |   |   |
|   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance rid |   |   |
|   |   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance |   |
| CreateLoadBalancerHTTPSListener | rid |   |   |
|   | acs:slb:%s:%s:certificate/% |   |   |
|   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance rid |   |   |
|   |   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance |   |
| CreateLoadBalancerTCPListener | rid |   |   |
|   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance rid |   |   |
|   |   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance |   |
| CreateLoadBalancerUDPListener | rid |   |   |
|   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance rid |   |   |
|   |   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance |   |
| DeleteLoadBalancerListener | rid |   |   |
|   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance rid |   |   |
|   |   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance |   |
| StartLoadBalancerListener | rid |   |   |

| eveloper Guide·API reference | Server Load Balance |
|---|---|

| API | ARN format |   |   |
|---|---|---|---|
|   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance rid |   |   |
|   |   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance |   |
| StopLoadBalancerListener | rid |   |   |
| SetLoadBalancerHTTPListenerAttribut | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance rid |   |   |
|   |   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance |   |
| e | rid |   |   |
|   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance rid |   |   |
|   |   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance |   |
| SetLoadBalancerHTTPSListenerAttrib | rid |   |   |
| ute |   |   |   |
|   | acs:slb:%s:%s:certificate/% |   |   |
|   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance rid |   |   |
|   |   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance |   |
| SetLoadBalancerTCPListenerAttribute | rid |   |   |
|   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance rid |   |   |
|   |   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance |   |
| SetLoadBalancerUDPListenerAttribute | rid |   |   |
| DescribeLoadBalancerHTTPListenerAt | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance rid |   |   |
|   |   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance |   |
| tribute | rid |   |   |
| DescribeLoadBalancerHTTPSListenerA | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance rid |   |   |
|   |   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance |   |
| ttribute | rid |   |   |
| DescribeLoadBalancerTCPListenerAttr | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance rid |   |   |
|   |   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance |   |
| ibute | rid |   |   |
| DescribeLoadBalancerUDPListenerAttr | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance rid |   |   |
|   |   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance |   |
| ibute | rid |   |   |
|   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance rid |   |   |
|   |   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance |   |
| AddBackendServers | rid |   |   |
|   | acs:ecs:$regionid:$accountid:instance/$instanceid |   |   |
|   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance rid |   |   |
|   |   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance |   |
| RemoveBackendServers | rid |   |   |
|   | acs:ecs:$regionid:$accountid:instance/$instanceid |   |   |
|   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance rid |   |   |
|   |   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance |   |
| SetBackendServers | rid |   |   |
|   | acs:ecs:$regionid:$accountid:instance/$instanceid |   |   |
|   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance rid |   |   |
|   |   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance |   |
| DescribeHealthStatus | rid |   |   |
|   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance rid |   |   |
|   |   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance |   |
|   | rid |   |   |
| CreateVServerGroup |   |   |   |
|   | acs:ecs:$regionid:$accountid:instance/$instanceid |   |   |

| erver Load Balancer | Developer Guide·API reference ARN format acs:slb:$regionid:$accountid:loadbalancer/$loadbalance rid acs:slb:$regionid:$accountid:loadbalancer/$loadbalance rid acs:slb:$regionid:$accountid:loadbalancer/$loadbalance rid acs:slb:$regionid:$accountid:loadbalancer/$loadbalance rid acs:slb:$regionid:$accountid:loadbalancer/$loadbalance rid acs:ecs:$regionid:$accountid:instance/$instanceid acs:slb:$regionid:$accountid:loadbalancer/$loadbalance rid acs:ecs:$regionid:$accountid:instance/$instanceid acs:slb:$regionid:$accountid:loadbalancer/$loadbalance rid acs:ecs:$regionid:$accountid:instance/$instanceid |   |   |
|---|---|---|---|
|   | Developer Guide·API referenc |   |   |
| API | ARN format |   |   |
|   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance rid |   |   |
|   |   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance |   |
| SetVServerGroupAttribute | rid |   |   |
|   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance rid |   |   |
|   |   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance |   |
| DeleteVServerGroup | rid |   |   |
|   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance rid |   |   |
|   |   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance |   |
| DescribeVServerGroups | rid |   |   |
|   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance rid |   |   |
|   |   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance |   |
| DescribeVServerGroupAttribute | rid |   |   |
|   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance rid |   |   |
|   |   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance |   |
| AddVServerGroupBackendServers | rid |   |   |
|   | acs:ecs:$regionid:$accountid:instance/$instanceid |   |   |
|   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance rid |   |   |
|   |   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance |   |
| RemoveVServerGroupBackendServers | rid |   |   |
|   | acs:ecs:$regionid:$accountid:instance/$instanceid |   |   |
|   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance rid |   |   |
|   |   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance |   |
| ModifyVServerGroupBackendServers | rid |   |   |
|   | acs:ecs:$regionid:$accountid:instance/$instanceid |   |   |

### 2.4 Common parameters

Common request parameters Common request parameters are request parameters that you must use when you call any API. Common request parameters

| Name | Type | Required | Description |
|---|---|---|---|
| Format | String | No | The format of the response. Valid values: JSON (default) \| XML |
| Version | String | Yes | The API version in the format of YYYY-MM-DD . Valid values: 2014-05-15 |
| AccessKeyId | String | Yes | The AccessKey ID that is used to access a service. |
| Signature | String | Yes | The signature result string. |

| Developer Guide·API re | ference |   | Server Load Balance |
|---|---|---|---|

| Name | Type | Required | Description |
|---|---|---|---|
| SignatureMethod | String | Yes | The algorithm used to create the request signature. Valid values: HMAC-SHA1 |
| Timestamp | String | Yes | The request timestamp. The timestamp uses UTC and it complies with the ISO 8601 standard. The timestamp format is YYYY-MM-DDThh:mm:ssZ . For example, 20:00:00 on January 1st, 2013 in China Standard Time (UTC +8) would be written as 2013-01- 10T12:00:00Z. |
| SignatureVersion | String | Yes | The signature algorithm version. Valid value: 1.0 |
| SignatureNonce | String | Yes | A unique random number that is used to prevent network replay attacks. You must use different random numbers for different requests. |

Example

```
http://slb.example.com/?Action=DescribeLoadBalancers &TimeStamp=2014-05-19T10%3A33%3A56Z &Format=xml &AccessKeyId=testid &Action=DescribeLoadBalancerAttribute &SignatureMethod=Hmac-SHA1 &LoadBalancerId=loadBalancerID &SignatureNonce=NwDAxvLU6tFE0DVb &Version=2014-05-15 &SignatureVersion=1.0 &Signature=Signature
```

Common response parameters API responses use a unified format. The 2xx HTTP status code indicates a successful invocation. The 4xx or 5xx HTTP status code indicates a failed invocation. The responses can be returned in JSON or XML format. The XML format is used by default. You can specify the format when calling an API. Each time a request is sent to call an API, the system returns a unique identifier RequestId, regardless of whether the invocation is successful. XML format

```xml
<? xml version="1.0" encoding="utf-8"? >
    <!—Result root node-->
    <API name+Response>
        <!—Returned request tag-->
        <RequestId>4C467B38-3910-447D-87BC-AC049166F216</RequestId>
        <!—Returned result-->
    </API name+Response>
```

JSON format `{`

```json
    "RequestId": "4C467B38-3910-447D-87BC-AC049166F216",
    /*Returned result*/
```

`}`

### 2.5 CLB instances

#### 2.5.1 CreateLoadBalancer

Creates a Server Load Balancer (SLB) instance. Before you call this operation, take note of the following information: Before you create an SLB instance, call the DescribeAvailableResource operation to query the resources available for purchase in the region where you want to create the SLB instance. You are charged for the SLB instances that you create. For more information, see Create an SLB instance. If you do not set the LoadBalancerSpec parameter, a shared-resource SLB instance is created. We recommend that you set the LoadBalancerSpec parameter to specify the specification of the SLB instance. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateLoadBalan cer | The operation that you want to perform. Set the value to Creat eLoadBalancer. |
| RegionId | String | Yes | cn-east- hangzhou-01 | The ID of the region where you want to create the SLB instance. You can call the DescribeRegions operation to query region IDs. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| AddressType | String | No | internet | The network type of the SLB instance. Valid values: int ernet and int ranet . int ernet : After an Internet-facing SLB instance is created, the system allocates a public IP address to the SLB instance. Then, the SLB instance can forward requests from the Internet. int ranet : After an internal-facing SLB instance is created, the system allocates a private IP address to the SLB instance. Then, the SLB instance can forward only internal requests. |
| InternetChargeTy pe | String | No | paybytraffic | The billing method of the Internet- facing SLB instance. Set the value to |
| Bandwidth | Integer | No | 10 | The maximum bandwidth of the listener. Unit: Mbit/s. Valid values: -1 and 1 t o 5120. -1: For a pay-by-data-transfer Internet-facing SLB instance, you can set the value to -1. This indicates that the maximum bandwidth is not limited. 1 to 5120: For a pay-by-bandwidth Internet-facing SLB instance, you can specify the maximum bandwidth of each listener. The sum of maximum bandwidth values of all listeners cannot exceed the maximum bandwidth of the SLB instance. For more information, see Bandwidth of a shared-resource SLB instance. |
| ClientToken | String | No | 5A2CFF0E-5718- 45B5-9D4D- 70B3FF3898 | This parameter is used to ensure the idempotence of the request. You can use the client to generate the value, but you must ensure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| LoadBalancerNa me | String | No | abc | The name of the SLB instance. The name must be 1 to 80 characters in length, and can contain digits, periods (.), underscores ( ), and _ hyphens (-). It must start with a letter. If this parameter is not set, the system automatically assigns a name to the SLB instance. |
| VpcId | String | No | vpc- bp1aevy8sofi8mh 1***** | The ID of the virtual private cloud (VPC) to which the SLB instance belongs. |
| VSwitchId | String | No | vsw- bp12mw1f8k3jgy ***** | The ID of the vSwitch to which the internal-facing SLB instance belongs. The vSwitch must be deployed in a VPC. To create an internal-facing SLB instance that is deployed in a VPC, you must set this parameter. If this parameter is set, the value of the AddessT ype parameter is set to int ranet by default. |
| MasterZoneId | String | No | cn-hangzhou-b | The ID of the primary zone to which the SLB instance belongs. You can call the DescribeZone operation to query information about the primary and secondary zones in a region. |
| SlaveZoneId | String | No | cn-hangzhou-d | The ID of the secondary zone to which the SLB instance belongs. You can call the DescribeZone operation to query information about the primary and secondary zones in a region. |
| access key id _ _ | String | No | 111 | The AccessKey ID. |
| Tags | String | No | test | The tags that are added to the SLB instance. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| EnableVpcVipFlo w | String | No | 1 | The flow log. |
| LoadBalancerSpe c | String | No | slb.s2.small | Two types of SLB instances are available: shared-resource SLB instances and guaranteed- performance SLB instances. You can create guaranteed- performance SLB instances of different specifications. Valid values: slb.s1.small slb.s2.small slb.s3.small slb.s2.medium For more information about specifications of guaranteed- performance SLB instances, see Guaranteed-performance SLB instances. |
| AddressIPVersion | String | No | ipv4 | The IP protocol that is used by the SLB instance. Valid values: ipv4 and ipv6. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| LoadBalancerId | String | lb-hddhfjg******* | The ID of the SLB instance. |
| Address | String | 42.250.**. ** | The IP address that is allocated to the SLB instance. |
| VpcId | String | vpc-25dvzy9***** | The ID of the VPC to which the SLB instance belongs. |
| VSwitchId | String | vsw-255ecr*** | The ID of the vSwitch to which the SLB instance belongs. |
| LoadBalancerN ame | String | abc | The name of the SLB instance. |
| AddressIPVersi on | String | ipv4 | The IP protocol used by the SLB instance. |

| S | erver Load Balanc | er |   | Developer Guide·API referenc | e |
|---|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| NetworkType | String | classic | The type of network where the SLB instance is deployed. vpc: indicates that the SLB instance is deployed in a VPC. classic: indicates that the SLB instance is deployed in a classic network. |
| RequestId | String | 365F4154-92F6- 4AE4-92F8- 7FF34B540710 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/? Action=CreateLoadBalancer &RegionId=cn-east-hangzhou-01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<CreateLoadBalancerResponse>
    <NetworkType>vpc</NetworkType>
   <LoadBalancerName>abc</LoadBalancerName>
   <Address>192.168.0. **</Address>
   <ResourceGroupId>rg-acfmxazb***</ResourceGroupId>
   <RequestId>AB197CF0-D9E9-4475-A89D-35DBCCF13BBE</RequestId>
   <AddressIPVersion>ipv4</AddressIPVersion>
   <LoadBalancerId>lb-bp1b6c719dfa0***</LoadBalancerId>
   <VSwitchId>vsw-bp12mw1f8k3jgygk9****</VSwitchId>
   <VpcId>vpc-bp1aevy8sofi8mh1q***</VpcId>
</CreateLoadBalancerResponse>
```

`JSON` format

```json
{"LoadBalancerName":"abc", "VpcId":"vpc-25dvzy9*****", "Address":"42.250. **. **", "RequestId":"365F4154-92F6-4AE4-92F8-7FF34B540710", "NetworkType":"classic", "AddressIPVersion":"ipv4", "VSwitchId":"vsw-255ecr***", "LoadBalancerId":"lb-hddhfjg*******"}
```

#### 2.5.2 DeleteLoadBalancer

Deletes a pay-as-you-go Server Load Balancer (SLB) instance. Not e After you delete an SLB instance, the listeners configured for the SLB instance and the tags added to the SLB instance are deleted. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteLoadBalan cer | The operation that you want to perform. Set the value to Delet eLoadBalancer. |
| LoadBalancerId | String | Yes | lb- bp1h66tp5uat8** ****** | The ID of the SLB instance. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | CEF72CEB-54B6- 4AE8-B225- F876FF7BA984 | The ID of the request. |

If the SLB instance that you want to delete has deletion protection enabled, the system reports an error in the following formats: JSON format `{`

```json
 "RequestId": "7B7AB375-1EA6-4A18-9D1C-F258F2D57638",
 "HostId": "slb.aliyuncs.com",
 "Code": "OperationDenied.DeleteProtectionIsOn",
 "Message": "The loadbalancer can't be deleted due to DeleteProtection is enabled."
```

`}` XML format

```xml
   <? xml version="1.0" encoding="UTF-8" ? >
        <DeleteLoadBabalancerResponse>
 <RequestId>7B7AB375-1EA6-4A18-9D1C-F258F2D57638</RequestId>
 <HostId>slb.aliyuncs.com</HostId>
 <Code>OperationDenied.DeleteProtectionIsOn</Code>
 <Message>The loadbalancer can't be deleted due to DeleteProtection is enabled. </Message
```

`>`

```
       </DeleteLoadBabalancerResponse>
```

Examples Sample requests

```
http(s)://[Endpoint]/? Action=DeleteLoadBalancer &LoadBalancerId=lb-bp1h66tp5uat8******** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DeleteLoadBabalancerResponse>
   <RequestId>E3F602B8-A162-4683-A7EC-49364E597259</RequestId>
</DeleteLoadBabalancerResponse>
```

`JSON` format `{`

```json
    "RequestId": "0D9B7343-AC1F-498C-A18A-78FE14A7C3A3"
```

`}`

#### 2.5.3 ModifyLoadBalancerInstanceSpec

Modifies the specification of a Server Load Balancer (SLB) instance. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyLoadBalan cerInstanceSpec | The operation that you want to perform. Set the value to Modif yLoadBalancerInst anceSpec. |
| LoadBalancerId | String | Yes | lb- bp1b6c719df**** ***** | The ID of the SLB instance. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| LoadBalancerSpe c | String | Yes | slb.s2.small | The specification of the SLB instance. Valid values: slb.s1.small slb.s2.small slb.s2.medium slb.s3.small slb.s3.medium slb.s3.large The supported specifications vary by region. For more information about specifications of guaranteed- performance SLB instances, see Guaranteed-performance SLB instances. Not e When you change a shared-resource SLB instance to a guaranteed-performance SLB instance, service disruptions may occur. The SLB instance may stop providing services for 10 to 30 seconds. Therefore, we recommend that you modify the configuration during off-peak hours. In addition, you can use Global Server Load Balancing (GSLB) to switch your workloads to another SLB instance before you modify the configuration. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 365F4154-92F6- 4AE4-92F8- 7FF34B540710 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/? Action=ModifyLoadBalancerInstanceSpec &LoadBalancerId=lb-bp1b6c719df********* &LoadBalancerSpec=slb.s2.small &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ModifyLoadBalancerInstanceSpecResponse>
     <RequestId>D456A34A-6E40-4379-8DAF-9175760FE215</RequestId>
  </ModifyLoadBalancerInstanceSpecResponse>
```

`JSON` format `{`

```json
    "RequestId": "D456A34A-6E40-4379-8DAF-9175760FE215"
```

`}`

#### 2.5.4 ModifyLoadBalancerInternetSpec

Modifies the billing method of an Internet-facing Server Load Balancer (SLB) instance. After you change the maximum bandwidth of a pay-by-bandwidth SLB instance, the change immediately takes effect. After you change the billing method of an SLB instance from pay-by-data-transfer to pay-bybandwidth, the new billing method takes effect at 00:00 the following day. After you change the billing method of an SLB instance from pay-by-bandwidth to pay-by-datatransfer, the new billing method takes effect at 00:00 the following day. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyLoadBalan cerInternetSpec | The operation that you want to perform. Set the value to Modif yLoadBalancerInt ernet Spec. |
| LoadBalancerId | String | Yes | lb- bp1b6c719dfa08 ex****** | The ID of the SLB instance. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Bandwidth | Integer | No | 10 | The maximum bandwidth of the Internet-facing SLB instance that is billed on a pay-by-bandwidth basis. Unit: Mbit/s. Valid values: 1 t o 5000. The maximum bandwidth varies based on the region where the SLB instance is created. Not e You do not need to set this parameter for pay-by- data-transfer SLB instances. The value of Int ernet ChargeT ype is paybyt raf f ic. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | CEF72CEB-54B6- 4AE8-B225- F876FF7BA984 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/? Action=ModifyLoadBalancerInternetSpec &LoadBalancerId=lb-bp1b6c719dfa08ex****** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ModifyLoadBalancerInternetSpecResponse>
      <RequestId>E4DD2D80-8DC0-4A2E-BFBA-BE983A31AFED</RequestId>
</ModifyLoadBalancerInternetSpecResponse>
```

`JSON` format `{`

```json
    "RequestId": "E4DD2D80-8DC0-4A2E-BFBA-BE983A31AFED"
```

`}`

#### 2.5.5 SetLoadBalancerName

Modifies the name of a Server Load Balancer (SLB) instance. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | SetLoadBalancer Name | The operation that you want to perform. Set the value to Set LoadBalancerName. |
| LoadBalancerId | String | Yes | lb- bp1b6c719dfa08 e****** | The ID of the SLB instance. |
| LoadBalancerNa me | String | Yes | lb-instance-test | The name of the SLB instance. The name must be 2 to 128 characters in length, and can contain letters, digits, periods (.), underscores ( ), and _ hyphens (-). |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | CEF72CEB-54B6- 4AE8-B225- F876FF7BA984 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/? Action=SetLoadBalancerName &LoadBalancerId=lb-bp1b6c719dfa08e****** &LoadBalancerName=abc1 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<SetLoadBalancerStatusResponse>
   <RequestId>3C7F675E-9F82-4806-BA47-FF57E3ACC850</RequestId>
</SetLoadBalancerStatusResponse>
```

`JSON` format `{`

```json
    "RequestId": "3C7F675E-9F82-4806-BA47-FF57E3ACC850"
```

`}`

#### 2.5.6 SetLoadBalancerStatus

Sets the state of a Server Load Balancer (SLB) instance. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | SetLoadBalancer Status | The operation that you want to perform. Set the value to Set LoadBalancerSt at us. |
| LoadBalancerId | String | Yes | lb- bp1b6c719dfa08 e****** | The ID of the SLB instance. |
| LoadBalancerStat us | String | Yes | active | The state of the SLB instance. Valid values: act ive and inact ive. act ive (default) When an SLB instance is in the active state, listeners of the SLB instance can forward inbound traffic based on the forwarding rules. inact ive When an SLB instance is in the inact ive state, listeners of the SLB instance do not forward inbound traffic. Not e If all listeners of an SLB instance are deleted, the SLB instance automatically switches to the inact ive state. |
| access key id _ _ | String | No | acc- hp34s2h0xx1ht4n wo**** | The AccessKey ID. |
| Tags | String | No | {"tagKey":"Key1", "tagValue":"Valu e1"} | The key and value of the tag. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | CEF72CEB-54B6- 4AE8-B225- F876FF7BA984 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/? Action=SetLoadBalancerStatus &LoadBalancerId=lb-bp1b6c719dfa08e****** &LoadBalancerStatus=active &<Common request parameters>
```

Sample success responses `XML` format

```xml
<SetLoadBalancerStatusResponse>
     <RequestId>E6DDFE22-F019-4F34-B8DD-FD14973450A6</RequestId>
  </SetLoadBalancerStatusResponse>
```

`JSON` format `{`

```json
    "RequestId": "E6DDFE22-F019-4F34-B8DD-FD14973450A6"
```

`}`

#### 2.5.7 DescribeLoadBalancerAttribute

Queries detailed information about a specified Server Load Balancer (SLB) instance. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeLoadBala ncerAttribute | The operation that you want to perform. Set the value to DescribeLoadBalancerAt t ribut e. |
| LoadBalancerId | String | Yes | lb- bp1b6c719dfa08 ex***** | The ID of the SLB instance. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| LoadBalancerId | String | lb-dhhd****** | The ID of the SLB instance to be queried. |
| RegionId | String | cn-hangzhou | The ID of the region where the SLB instance is created. |
| RegionIdAlias | String | cn-hangzhou | The alias of the region where the SLB instance is created. |
| LoadBalancerN ame | String | abc | The name of the SLB instance. |
| LoadBalancerSt atus | String | active | The state of the SLB instance. Valid values: inact ive: The SLB instance is stopped. SLB instances in the inactive state do not forward traffic. act ive: The SLB instance runs as expected. A newly created SLB instance is in the act ive state by default. locked: The SLB instance is locked. SLB instances may be locked by Apsara Stack due to overdue payments or other reasons. |
| Address | String | 42.**. **.6 | The IP address of the SLB instance. |
| AddressType | String | internet | The type of IP addresses that the SLB instance uses. |
| NetworkType | String | vpc | The type of network where the SLB instance is deployed. |
| VpcId | String | vpc-25dvzy9f8***** | The ID of the virtual private cloud (VPC) to which the internal-facing SLB instance belongs. |
| Bandwidth | Integer | 5 | The maximum bandwidth of the Internet- facing SLB instance that is billed on a pay- by-bandwidth basis. |
| CreateTime | String | 2017-08- 31T02:49:05Z | The time when the SLB instance was created. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| ListenerPorts | List | 80 | The list of frontend ports that are used by the SLB instance. |
| ListenerPortsAn dProtocol | Array of ListenerPortAn dProtocol |   | The list of frontend ports and protocols that are used by the SLB instance. |
| ListenerPortAn dProtocol |   |   |   |
| ListenerPort | Integer | 443 | The frontend port that is used by the SLB instance. |
| ListenerProtoco l | String | https | The frontend protocol that is used by the SLB instance. |
| BackendServers | Array of BackendServer |   | The list of backend servers that are added to the SLB instance. |
| BackendServer |   |   |   |
| ServerId | String | i-djghr2**** | The ID of the backend server. |
| Weight | Integer | 90 | The weight of the backend server. |
| ServerIp | String | 192.168.0.1 | The IP address of the backend server. |
| Type | String | ecs | The type of the backend server. |
| MasterZoneId | String | cn-hangzhou-b | The ID of the primary zone to which the SLB instance belongs. |
| AutoReleaseTi me | Long | 1513947075 | The timestamp generated when the SLB instance was released. |
| CreateTimeSta mp | Long | 1504147745000 | The timestamp generated when the SLB instance was created. |
| EndTime | String | 2999-09- 08T16:00:00Z | The time when the SLB instance was stopped. |

| D | eveloper Guide·AP | I reference |   | Server Load Balance | r |
|---|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| EndTimeStamp | Long | 32493801600000 | The timestamp generated when the SLB instance was stopped. |
| InternetCharge Type | String | paybybandwidth | The billing method of the Internet-facing SLB instance. Valid values: paybybandwidt h and paybyt raf f ic. paybybandwidt h: pay-by-bandwidth paybyt raf f ic (default): pay-by-data- transfer |
| ListenerPortsAn dProtocal | Array of ListenerPortAn dProtocal |   | The port and protocol of the listener. |
| ListenerPortAn dProtocal |   |   |   |
| ListenerPort | Integer | 443 | The frontend port that is used by the SLB instance. |
| ListenerProtoca l | String | http | The frontend protocol that is used by the SLB instance. |
| LoadBalancerS pec | String | slb.s2.small | The specification of the SLB instance. |
| PayType | String | PrePay | The billing method of the SLB instance. Valid values: PayOnDemand and PrePay. |
| RequestId | String | 365F4154-92F6- 4AE4-92F8- 7FF34B540710 | The ID of the request. |
| SlaveZoneId | String | cn-hangzhou-d | The ID of the secondary zone to which the SLB instance belongs. |
| VSwitchId | String | vsw-255ecrwq5***** | The ID of the vSwitch to which the internal- facing SLB instance belongs. |

Examples Sample requests

```
http(s)://[Endpoint]/? Action=DescribeLoadBalancerAttribute &LoadBalancerId=lb-bp1b6c719dfa08ex***** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeLoadBalancerAttributeResponse>
      <CreateTimeStamp>1541679713000</CreateTimeStamp>
   <RegionIdAlias>cn-hangzhou</RegionIdAlias>
   <BackendServers>
      <BackendServer>
         <ServerId>i-bp1c3zrr37ablp8ujo7v</ServerId>
         <Weight>100</Weight>
         <Type>ecs</Type>
      </BackendServer>
   </BackendServers>
   <HasReservedInfo>false</HasReservedInfo>
   <ListenerPorts></ListenerPorts>
   <InternetChargeType>paybytraffic</InternetChargeType>
   <VSwitchId>vsw-bp12mw1f8k3*********</VSwitchId>
   <VpcId>vpc-bp1aevy8sofi8mh*****</VpcId>
   <SlaveZoneId>cn-hangzhou-d</SlaveZoneId>
   <LoadBalancerSpec>slb.s2.small</LoadBalancerSpec>
   <NetworkType>vpc</NetworkType>
   <ListenerPortsAndProtocol></ListenerPortsAndProtocol>
   <PayType>PayOnDemand</PayType>
   <Bandwidth>5120</Bandwidth>
   <LoadBalancerName>abc1</LoadBalancerName>
   <ResourceGroupId>rg-acfmxazb4p*****</ResourceGroupId>
   <AddressIPVersion>ipv4</AddressIPVersion>
   <LoadBalancerId>lb-bp1b6c719dfa08e*****</LoadBalancerId>
   <EndTimeStamp>32493801600000</EndTimeStamp>
   <MasterZoneId>cn-hangzhou-b</MasterZoneId>
   <ListenerPortsAndProtocal></ListenerPortsAndProtocal>
   <Address>192.168.0.1</Address>
   <RegionId>cn-hangzhou</RegionId>
   <RequestId>35D745B3-1567-4855-9EF1-F5CED3C1670C</RequestId>
   <CreateTime>2018-11-08T12:21:53Z</CreateTime>
   <AddressType>intranet</AddressType>
   <EndTime>2999-09-08T16:00:00Z</EndTime>
   <LoadBalancerStatus>active</LoadBalancerStatus>
</DescribeLoadBalancerAttributeResponse>
```

`JSON` format `{`

```json
    "CreateTimeStamp": 1541679713000,
    "RegionIdAlias": "cn-hangzhou",
    "BackendServers": {
        "BackendServer": [
```

`{`

```json
                "ServerId": "i-bp1c3zrr37ab*****",
                "Weight": 100,
                "Type": "ecs"
```

`}` `]` `},`

```json
    "HasReservedInfo": "false",
    "ListenerPorts": {
        "ListenerPort": [ ]
```

`},`

```json
    "InternetChargeType": "paybytraffic",
    "VSwitchId": "vsw-bp12mw1f8k******",
    "VpcId": "vpc-bp1aevy8sofi8mh******",
    "SlaveZoneId": "cn-hangzhou-d",
    "LoadBalancerSpec": "slb.s2.small",
    "NetworkType": "vpc",
    "ListenerPortsAndProtocol": {
        "ListenerPortAndProtocol": [ ]
```

`},`

```json
    "PayType": "PayOnDemand",
    "Bandwidth": 5120,
    "LoadBalancerName": "abc1",
    "ResourceGroupId": "rg-acfmxazb*****",
    "AddressIPVersion": "ipv4",
    "LoadBalancerId": "lb-bp1b6c719dfa08*****",
    "EndTimeStamp": 32493801600000,
    "MasterZoneId": "cn-hangzhou-b",
    "ListenerPortsAndProtocal": {
        "ListenerPortAndProtocal": [ ]
```

`},`

```json
    "Address": "192.168.0.1",
    "RegionId": "cn-hangzhou",
    "RequestId": "35D745B3-1567-4855-9EF1-F5CED3C1670C",
    "CreateTime": "2018-11-08T12:21:53Z",
    "AddressType": "intranet",
    "EndTime": "2999-09-08T16:00:00Z",
    "LoadBalancerStatus": "active"
```

`}`

#### 2.5.8 DescribeLoadBalancers

Queries Server Load Balancer (SLB) instances. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeLoadBala ncers | The operation that you want to perform. Set the value to DescribeLoadBalancers. |
| RegionId | String | Yes | cn-east- hangzhou-01 | The ID of the region where the SLB instance is created. You can query region IDs from the Regions and zones list or by calling the DescribeRegions operation. |
| ServerId | String | No | vm-23** | The ID of the backend server that is added to the SLB instance. |
| LoadBalancerId | String | No | lb- bp1b6c719dfa*** **** | The ID of the SLB instance. You can specify up to 10 SLB instance IDs in each request. Separate multiple IDs with commas (,). |
| LoadBalancerNa me | String | No | abc1 | The name of the SLB instance. You can specify up to 10 SLB instance names in each request. Separate multiple names with commas (,). |
| ServerIntranetAd dress | String | No | 10.80.102.** | The private IP address of the backend server that is added to the SLB instance. You can specify multiple IP addresses to query SLB instances. Separate multiple IP addresses with commas (,). |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| AddressType | String | No | intranet | The network type of the SLB instance. Valid values: int ranet and int ernet . int ernet : After an Internet-facing SLB instance is created, the system allocates a public IP address to the SLB instance. Then, the SLB instance can forward requests from the Internet. int ranet : After an internal-facing SLB instance is created, the system allocates a private IP address to the SLB instance. Then, the SLB instance can forward only internal requests. |
| InternetChargeTy pe | String | No | paybybandwidth | The billing method of an Internet- facing SLB instance. Valid values: paybybandwidt h and paybyt raf f ic. paybybandwidt h: pay-by- bandwidth. paybyt raf f ic: pay-by-data- transfer. Not e If this parameter is not set, the billing method of the SLB instance remains unchanged. |
| VpcId | String | No | vpc- bp1aevy8sof***** *** | The ID of the virtual private cloud (VPC) to which the SLB instance belongs. |
| VSwitchId | String | No | vsw- bp12mw1f8k3*** **** | The ID of the vSwitch to which the SLB instance belongs. |
| NetworkType | String | No | vpc | The type of network where the internal-facing SLB instance is deployed. Valid values: vpc and classic. vpc: a VPC classic: a classic network |
| Address | String | No | 192.168.0.1 | The IP address that the SLB instance uses to provide services. |

| erver Load Balancer |   |   |   | Developer Guide·API referenc |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| MasterZoneId | String | No | cn-hangzhou-b | The ID of the primary zone to which the SLB instance belongs. |
| SlaveZoneId | String | No | cn-hangzhou-d | The ID of the secondary zone to which the SLB instance belongs. Multiple zones are not supported for users whose workloads are deployed on Alibaba Finance Cloud. |
| Tags | String | No | {"tagKey":"Key1", "tagValue":"Valu e1"} | The tags that are added to the SLB instances. The tags must be key-value pairs that are contained in a JSON dictionary. You can specify up to 10 tags in each request. |
| PayType | String | No | PayOnDemand | The billing method of the SLB instance. Valid values: PayOnDemand and PrePay. PayOnDemand: pay-as-you-go PrePay: subscription |
| AddressIPVersion | String | No | ipv4 | The IP version. Valid values: ipv4 and ipv6. Not e IPv6 instances are supported in the following zones, and the instances must be guaranteed-performance SLB instances. Hangzhou Zone E and Hangzhou Zone F in China (Hangzhou), Beijing Zone F and Beijing Zone G in China (Beijing), Nantong Zone D and Nantong Zone E in China (Nantong), Zhangjiakou Zone A and Zhangjiakou Zone B in China (Zhangjiakou), and Shenzhen Zone D and Shenzhen Zone E in China (Shenzhen). |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| LoadBalancers | Array of LoadBalancer |   | The list of SLB instances. |
| LoadBalancer |   |   |   |
| LoadBalancerId | String | lb- hjfng*************** | The ID of the SLB instance. |
| LoadBalancerN ame | String | def | The name of the SLB instance. |
| LoadBalancerSt atus | String | active | The state of the SLB instance. Valid values: inact ive: The listeners of the SLB instance do not forward traffic when the SLB instance is in the inactive state. act ive: After the SLB instance is created, it is in the active state by default. locked: The SLB instance is locked. |
| Address | String | 100.**. **.28 | The IP address of the SLB instance. |
| RegionId | String | cn-east-hangzhou- 01 | The ID of the region where the SLB instance is created. |
| RegionIdAlias | String | cn-hangzhou | The name of the region where the SLB instance is created. |
| AddressType | String | intranet | The network type of the SLB instance. |
| VSwitchId | String | vsw-255ecr****** | The ID of the vSwitch to which the internal- facing SLB instance belongs. |
| VpcId | String | vpc-25dvzy9f8****** | The ID of the VPC to which the internal- facing SLB instance belongs. |
| NetworkType | String | vpc | The type of network where the internal- facing SLB instance is deployed. Valid values: vpc: a VPC classic: a classic network |
| CreateTime | String | 2017-08- 31T02:49:05Z | The time when the SLB instance was created. |

| erver Load Balanc | er |   | Developer Guide·API referenc |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| MasterZoneId | String | cn-hangzhou-b | The ID of the primary zone where the SLB instance is deployed. |
| SlaveZoneId | String | cn-hangzhou-d | The ID of the secondary zone where the SLB instance is deployed. |
| AddressIPVersi on | String | ipv4 | The IP version. Valid values: ipv4 and ipv6. |
| CreateTimeSta mp | Long | 1504147745000 | The timestamp when the SLB instance was created. |
| InternetCharge Type | String | paybybandwidth | The billing method of the Internet-facing SLB instance. Valid values: 4: paybyt raf f ic. This indicates that the Internet-facing SLB instance is billed on a pay-by-data-transfer basis. This is the default value. Not e If the value of the PayType parameter is set to PrePay, only pay-by- bandwidth is supported. |
| PayType | String | PrePay | The billing method of the SLB instance. Valid values: PayOnDemand and PrePay. |
| RequestId | String | 365F4154-92F6- 4AE4-92F8- 7FF34B540710 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/? Action=DescribeLoadBalancers &RegionId=cn-east-hangzhou-01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeLoadBalancersResponse>
      <PageNumber>1</PageNumber>
   <TotalCount>1</TotalCount>
   <PageSize>50</PageSize>
   <LoadBalancers>
      <LoadBalancer>
         <CreateTimeStamp>1541679713000</CreateTimeStamp>
         <LoadBalancerName>abc1</LoadBalancerName>
         <RegionIdAlias>cn-hangzhou</RegionIdAlias>
         <ResourceGroupId>rg-acfmxaz*******y</ResourceGroupId>
         <AddressIPVersion>ipv4</AddressIPVersion>
         <LoadBalancerId>lb-bp1b6c********fuca5</LoadBalancerId>
         <VSwitchId>vsw-bp12mw1f********bmlj</VSwitchId>
         <InternetChargeType>4</InternetChargeType>
         <VpcId>vpc-bp1aevy8*********5cm</VpcId>
         <SlaveZoneId>cn-hangzhou-d</SlaveZoneId>
         <NetworkType>vpc</NetworkType>
         <MasterZoneId>cn-hangzhou-b</MasterZoneId>
         <CreateTime>2018-11-08T20:21Z</CreateTime>
         <Address>192.168.0. **</Address>
         <RegionId>cn-hangzhou</RegionId>
         <AddressType>intranet</AddressType>
         <PayType>PayOnDemand</PayType>
         <LoadBalancerStatus>active</LoadBalancerStatus>
      </LoadBalancer>
   </LoadBalancers>
   <RequestId>1C7445CB-C21C-4C19-9A3C-65C3190D1944</RequestId>
</DescribeLoadBalancersResponse>
```

`JSON` format

```json
{"RequestId":"365F4154-92F6-4AE4-92F8-7FF34B540710","LoadBalancers":[{"Address":"100.98.28.
**","VSwitchId":"vsw-255ecr******","CreateTime":"2017-08-31T02:49:05Z","AddressIPVersion":"
ipv4","LoadBalancerId":"lb-hjfng***************","PayType":"PrePay","SlaveZoneId":"cn-hangz hou-d","InternetChargeType":"paybybandwidth","RegionIdAlias":"cn-hangzhou","LoadBalancerNam e":"def","VpcId":"vpc-25dvzy9f8******","NetworkType":"vpc","RegionId":"cn-hangzhou","Addres sType":"intranet","LoadBalancerStatus":"active","MasterZoneId":"cn-hangzhou-b","CreateTimeS tamp":"1504147745000"}]}
```

#### 2.5.9 DescribeRegions

Queries regions. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeRegions | The operation that you want to perform. Set the value to DescribeRegions. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| Regions | Array of Region |   | The list of regions. |
| Region |   |   |   |
| RegionId | String | cn-beijing | The ID of the region. |
| LocalName | String | China(Beijing) | The name of the region. |
| RequestId | String | 1651FBB6-4FBF- 49FF-A9F5- DF5D696C7EC6 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/? Action=DescribeRegions &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RequestId>1651FBB6-4FBF-49FF-A9F5-DF5D696C7EC6</RequestId> <Regions>
    <Region>
        <RegionId>cn-beijing</RegionId>
        <LocalName>China(Beijing)</LocalName>
    </Region>
</Regions>
```

`JSON` format

```json
{"RequestId":"1651FBB6-4FBF-49FF-A9F5-DF5D696C7EC6","Regions":{"Region":[{"RegionId":"cn-be ijing","LocalName":"China(Beijing)"}]}}
```

Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | InvalidParameter | Illegal parameter, query.namespace is not auth. | The error message returned because the service is unauthorized. Acquire the permissions and try again. |

#### 2.5.10 DescribeZones

Queries zones in a specified region. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeZones | The operation that you want to perform. Set the value to DescribeZones. |
| RegionId | String | Yes | cn-east- hangzhou-01 | The ID of the region where the Server Load Balancer (SLB) instance is created. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| Zones | Array of Zone |   | The list of zones. |
| Zone |   |   |   |
| ZoneId | String | cn-hangzhou-b | The ID of the zone. |
| LocalName | String | Hangzhou Zone | The name of the zone. |
| SlaveZones | Array of SlaveZone |   | The list of secondary zones. |
| SlaveZone |   |   |   |
| ZoneId | String | cn-hangzhou-g | The ID of the secondary zone. |
| LocalName | String | Hangzhou Zone G | The name of the secondary zone. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | A48D35FF-440A- 4BC0-A4A2- A9BF69B7E43A | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/? Action=DescribeZones &RegionId=cn-east-hangzhou-01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeZonesResponse>
  <RequestId>3FF183FF-F4AA-40E8-8B5D-90788C6799C2</RequestId>
   <Zones>
      <Zone>
         <SlaveZones>
            <SlaveZone>
               <ZoneId>cn-hangzhou-g</ZoneId>
               <LocalName>Hangzhou Zone G</LocalName>
            </SlaveZone>
            <SlaveZone>
               <ZoneId>cn-hangzhou-d</ZoneId>
               <LocalName>Hangzhou Zone D</LocalName>
            </SlaveZone>
         </SlaveZones>
         <ZoneId>cn-hangzhou-b</ZoneId>
         <LocalName>Hangzhou Zone B</LocalName>
      </Zone>
      <Zone>
         <SlaveZones>
            <SlaveZone>
               <ZoneId>cn-hangzhou-e</ZoneId>
               <LocalName>Hangzhou Zone E</LocalName>
            </SlaveZone>
         </SlaveZones>
         <ZoneId>cn-hangzhou-d</ZoneId>
         <LocalName>Hangzhou Zone D</LocalName>
      </Zone>
      <Zone>
         <SlaveZones>
            <SlaveZone>
               <ZoneId>cn-hangzhou-f</ZoneId>
               <LocalName>Hangzhou Zone F</LocalName>
            </SlaveZone>
            <SlaveZone>
               <ZoneId>cn-hangzhou-d</ZoneId>
               <LocalName>Hangzhou Zone D</LocalName>
```

`g` `/`

```xml
            </SlaveZone>
         </SlaveZones>
         <ZoneId>cn-hangzhou-e</ZoneId>
         <LocalName>Hangzhou Zone E</LocalName>
      </Zone>
      <Zone>
         <SlaveZones>
            <SlaveZone>
               <ZoneId>cn-hangzhou-e</ZoneId>
               <LocalName>Hangzhou Zone E</LocalName>
            </SlaveZone>
         </SlaveZones>
         <ZoneId>cn-hangzhou-f</ZoneId>
         <LocalName>Hangzhou Zone F</LocalName>
      </Zone>
      <Zone>
         <SlaveZones>
            <SlaveZone>
               <ZoneId>cn-hangzhou-h</ZoneId>
               <LocalName>Hangzhou Zone H</LocalName>
            </SlaveZone>
            <SlaveZone>
               <ZoneId>cn-hangzhou-b</ZoneId>
               <LocalName>Hangzhou Zone B</LocalName>
            </SlaveZone>
         </SlaveZones>
         <ZoneId>cn-hangzhou-g</ZoneId>
         <LocalName>Hangzhou Zone G</LocalName>
      </Zone>
      <Zone>
         <SlaveZones>
            <SlaveZone>
               <ZoneId>cn-hangzhou-g</ZoneId>
               <LocalName>Hangzhou Zone G</LocalName>
            </SlaveZone>
         </SlaveZones>
         <ZoneId>cn-hangzhou-h</ZoneId>
         <LocalName>Hangzhou Zone H</LocalName>
      </Zone>
   </Zones>
</DescribeZonesResponse>
```

`JSON` format `{`

```json
    "DescribeZonesResponse": {
        "RequestId": "3FF183FF-F4AA-40E8-8B5D-90788C6799C2",
        "Zones": {
            "Zone": [
```

`{`

```json
                    "SlaveZones": {
                        "SlaveZone": [
```

`{` `"Z`

```
Id"
```

`"` `h` `h` `"`

```json
                                "ZoneId": "cn-hangzhou-g",
                                "LocalName": "Hangzhou Zone G"
```

`},` `{`

```json
                                "ZoneId": "cn-hangzhou-d",
                                "LocalName": "Hangzhou Zone D"
```

`}` `]` `},`

```json
                    "ZoneId": "cn-hangzhou-b",
                    "LocalName": "Hangzhou Zone B"
```

`},` `{`

```json
                    "SlaveZones": {
                        "SlaveZone": {
                            "ZoneId": "cn-hangzhou-e",
                            "LocalName": "Hangzhou Zone E"
```

`}` `},`

```json
                    "ZoneId": "cn-hangzhou-d",
                    "LocalName": "Hangzhou Zone D"
```

`},` `{`

```json
                    "SlaveZones": {
                        "SlaveZone": [
```

`{`

```json
                                "ZoneId": "cn-hangzhou-f",
                                "LocalName": "Hangzhou Zone F"
```

`},` `{`

```json
                                "ZoneId": "cn-hangzhou-d",
                                "LocalName": "Hangzhou Zone D"
```

`}` `]` `},`

```json
                    "ZoneId": "cn-hangzhou-e",
                    "LocalName": "Hangzhou Zone E"
```

`},` `{`

```json
                    "SlaveZones": {
                        "SlaveZone": {
                            "ZoneId": "cn-hangzhou-e",
                            "LocalName": "Hangzhou Zone E"
```

`}` `},`

```json
                    "ZoneId": "cn-hangzhou-f",
                    "LocalName": "Hangzhou Zone F"
```

`},` `{`

```json
                    "SlaveZones": {
                        "SlaveZone": [
```

`{`

```json
                                "ZoneId": "cn-hangzhou-h",
                                "LocalName": "Hangzhou Zone H"
```

`}` `},` `{`

```json
                                "ZoneId": "cn-hangzhou-b",
                                "LocalName": "Hangzhou Zone B"
```

`}` `]` `},`

```json
                    "ZoneId": "cn-hangzhou-g",
                    "LocalName": "Hangzhou Zone G"
```

`},` `{`

```json
                    "SlaveZones": {
                        "SlaveZone": {
                            "ZoneId": "cn-hangzhou-g",
                            "LocalName": "Hangzhou Zone G"
```

`}` `},`

```json
                    "ZoneId": "cn-hangzhou-h",
                    "LocalName": "Hangzhou Zone H"
```

`}` `]` `}` `}` `}` Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | InvalidParameter | Illegal parameter, query.namespace is not auth. | The error message returned because you are unauthorized to perform the operation. Acquire the required permissions first. |

### 2.6 Listener

#### 2.6.1 TCP listeners

##### 2.6.1.1 CreateLoadBalancerTCPListener

Creates a TCP listener. Not e Newly created listeners are in the Stopped state. After a listener is created, you can call the StartLoadBalancerListener operation to enable the listener to forward traffic. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateLoadBalan cerTCPListener | The operation that you want to perform. Set the value to Creat eLoadBalancerT CPList ener. |
| Bandwidth | Integer | Yes | -1 | The maximum bandwidth of the listener. Unit: Mbit/s. Valid values: 1 t o 5120 and -1. -1: For a pay-by-data-transfer Internet-facing Server Load Balancer (SLB) instance, you can set the value to -1. This indicates that the maximum bandwidth is unlimited. 1 to 5120: For a pay-by-bandwidth Internet-facing SLB instance, you can specify the maximum bandwidth of each listener. The sum of maximum bandwidth values of all listeners cannot exceed the maximum bandwidth of the SLB instance. |
| ListenerPort | Integer | Yes | 80 | The frontend port that is used by the SLB instance. Valid values: 1 t o 65535. |
| LoadBalancerId | String | Yes | lb- bp1b6c719dfa08 ex****** | The ID of the SLB instance. |
| BackendServerPor t | Integer | No | 80 | The backend port that is used by the SLB instance. Valid values: 1 t o 65535. If the VServerGroupId parameter is not set, this parameter is required. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Scheduler | String | No | wrr | The scheduling algorithm. Valid values: wrr (default): Backend servers that have higher weights receive more requests than those that have lower weights. wlc: Requests are distributed based on the combination of the weights and number of connections to backend servers. If two backend servers have the same weight, the backend server that has fewer connections receives more requests. rr: Requests are distributed to backend servers in sequence. sch: Specifies consistent hashing based on source IP addresses. Requests from the same source IP address are distributed to the same backend server. t ch: Specifies consistent hashing based on four factors: source IP address, destination IP address, source port number, and destination port number. Requests that contain the same preceding information are distributed to the same backend server. Not e Only guaranteed- performance SLB instances support sch and tch. |
| PersistenceTimeo ut | Integer | No | 0 | The timeout period of session persistence. Valid values: 0 t o 3600. Unit: seconds. Default value: 0. By default, session persistence is disabled. |
| HealthyThreshold | Integer | No | 4 | Specifies the number of consecutive health check successes required before a backend server is declared healthy (from f ail to success). Valid values: 2 t o 10. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| UnhealthyThresh old | Integer | No | 4 | Specifies the number of consecutive health check failures required before a backend server is declared unhealthy (from success to f ail). Valid values: 2 t o 10. |
| HealthCheckConn ectTimeout | Integer | No | 100 | The timeout period of a health check response. Valid values: 1 t o 300. Unit: seconds. Default value: 5. |
| HealthCheckConn ectPort | Integer | No | 80 | The port that is used for health checks. Valid values: 1 t o 65535. If you do not set this parameter, the port of the backend server is used for health checks. |
| healthCheckInterv al | Integer | No | 3 | The interval between two consecutive health checks. Valid values: 1 t o 50. Unit: seconds. |
| HealthCheckDom ain | String | No | 172.10.**. ** | The domain name that is used for health checks. Valid values: $ ip: The private IP address of the _ backend server. If the $ ip _ parameter is set or the HealthCheckDomain parameter is not set, SLB uses the private IP addresses of backend servers as the domain names for health checks. domain: The domain name must be 1 to 80 characters in length, and can contain only letters, digits, periods (.), and hyphens (-). |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| HealthCheckURI | String | No | /test/index.html | The URL that is used for health checks. The value must be 1 to 80 characters in length, and can contain letters, digits, hyphens (-), forward slashes (/), periods (.), percent signs (%), number signs (#), and ampersands (&). The URL must not be a single forward slash (/) and it must start with a forward slash (/). You can set this parameter when the TCP listener requires HTTP health checks. If you do not set this parameter, TCP health checks are performed. |
| HealthCheckHttpC ode | String | No | http 2xx,http 3x _ _ x | The HTTP status code that indicates a successful health check. Separate multiple HTTP status codes with commas (,). Valid values: ht t p 2xx, ht t p 3xx, _ _ ht t p 4xx, and ht t p 5xx Default _ _ value: http 2xx. _ |
| HealthCheckType | String | No | tcp | The type of health check. Valid values: t cp and ht t p. Default value: tcp. |
| VServerGroupId | String | No | rsp-cige6j***** | The ID of the vServer group. |
| MasterSlaveServe rGroupId | String | No | rsp-0bfucw***** | The ID of the primary/secondary server group. Not e You cannot specify both the vServer group ID and the primary/secondary server group ID. |
| EstablishedTimeo ut | Integer | No | 500 | The timeout period of connections. Valid values: 10 t o 900. Unit: seconds. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Description | String | No | CreateListeners. | The description of the listener. The description must be 1 to 80 characters in length, and can contain letters, digits, hyphens (-), forward slashes (/), periods (.), and underscores ( ). It can also contain _ Chinese characters. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | CEF72CEB-54B6- 4AE8-B225- F876FF7BA984 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/? Action=CreateLoadBalancerTCPListener &Bandwidth=-1 &ListenerPort=80 &LoadBalancerId=lb-bp1b6c719dfa08ex****** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<CreateLoadBalancerTCPListenerResponse>
     <RequestId>CEF72CEB-54B6-4AE8-B225-F876FF7BA984</RequestId>
</CreateLoadBalancerTCPListenerResponse>
```

`JSON` format

```json
{"RequestId":" CEF72CEB-54B6-4AE8-B225-F876FF7BA984"}
```

Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | Abs.VServerGroupId AndMasterSlaveServ erGroupId.MissMatch | The parameters VServerGroupId or MasterSlaveServerGroupId miss match. | The error message returned because the server group ID that is specified in the VServerGroupId or MasterSlaveServerGroupId parameter is not found. |

##### 2.6.1.2 SetLoadBalancerTCPListenerAttribute

Modifes the configurations of a TCP listener. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | SetLoadBalancer TCPListenerAttrib ute | The operation that you want to perform. Set the value to Set LoadBalancerT CPList enerAt t rib ut e. |
| ListenerPort | Integer | Yes | 80 | The frontend port that is used by the Server Load Balancer (SLB) instance. Valid values: 1 to 65535. |
| LoadBalancerId | String | Yes | lb- bp1ygod3yctvg1 y****** | The ID of the SLB instance. |
| Bandwidth | Integer | No | 43 | The maximum bandwidth of the listener. Unit: Mbit/s. Valid values: -1 and 1 t o 5120. -1: For a pay-by-data-transfer Internet-facing SLB instance, you can set the value to -1. This indicates that the maximum bandwidth is not limited. 1 t o 5120: For a pay-by-bandwidth Internet-facing SLB instance, you can specify the maximum bandwidth of each listener. The sum of maximum bandwidth values of all listeners cannot exceed the maximum bandwidth of the SLB instance. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Scheduler | String | No | wrr | The scheduling algorithm. Valid values: wrr: Backend servers that have higher weights receive more requests than those that have lower weights. wlc: Requests are distributed based on the combination of the weights and number of connections to backend servers. If two backend servers have the same weight, the backend server that has fewer connections receives more requests. rr: Requests are distributed to backend servers in sequence. sch: Specifies consistent hashing based on source IP addresses. Requests from the same source IP address are distributed to the same backend server. t ch: Specifies consistent hashing based on four factors: source IP address, destination IP address, source port number, and destination port number. Requests that contain the same preceding information are distributed to the same backend server. Not e Only guaranteed- performance SLB instances support sch and tch. |
| PersistenceTimeo ut | Integer | No | 0 | The timeout period of session persistence. Valid values: 0 to 3600. Unit: seconds. Default value: 0. This indicates that session persistence is disabled. |
| HealthyThreshold | Integer | No | 4 | Specifies the number of times that an unhealthy backend server must consecutively pass health checks before it is declared healthy (from f ail to success). Valid values: 2 to 10. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| UnhealthyThresh old | Integer | No | 4 | Specifies the number of times that a healthy backend server must consecutively fail health checks before it is declared unhealthy (from success to f ail). Valid values: 2 to 10. |
| HealthCheckConn ectTimeout | Integer | No | 100 | The timeout period for a health check response. If a backend Elastic Compute Service (ECS) instance does not send an expected response within the specified period of time, the ECS instance is considered unhealthy. Valid values: 1 to 300. Unit: seconds. Not e If the value of the Healt hCheckConnect T imeout parameter is smaller than that of the Healt hCheckInt erval parameter, the value of the HCT imeout parameter is ignored and the value of the Healt hCheckInt erval parameter is regarded the waiting period. |
| HealthCheckConn ectPort | Integer | No | 8080 | The port that is used for health checks. Valid values: 1 to 65535. If this parameter is not set, the port specified in BackendServerPort is used for health checks. |
| HealthCheckInterv al | Integer | No | 5 | The interval between two consecutive health checks. Valid values: 1 to 50. Unit: seconds. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| HealthCheckDom ain | String | No | 172.16.**. ** | The domain name that is used for health checks. You can set this parameter when the TCP listener requires HTTP health checks. If you do not set this parameter, TCP health checks are performed. $ ip: The private IP address of the _ backend server. If you do not set this parameter or set the parameter to $ ip, the SLB _ instance uses the private IP address of each backend server as the domain name for health checks. domain: The domain name must be 1 to 80 characters in length. It can contain only letters, digits, periods (.), and hyphens (-). |
| HealthCheckURI | String | No | /test/index.html | The URL that is used for health checks. The URL must be 1 to 80 characters in length, and can contain letters, digits, hyphens (-), forward slashes (/), periods (.), percent signs (%), question marks (?), number signs (#), and ampersands (&). The URL must not be a single forward slash (/). However, it must start with a forward slash (/). You can set this parameter when the TCP listener requires HTTP health checks. If you do not set this parameter, TCP health checks are performed. ) |
| HealthCheckHttpC ode | String | No | http 2xx _ | The HTTP status code that indicates a successful health check. Separate multiple HTTP status codes with commas (,). Valid values: ht t p 2xx, ht t p 3xx, _ _ ht t p 4xx, and ht t p 5xx. _ _ |
| HealthCheckType | String | No | tcp | The type of health check. Valid values: t cp and ht t p. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| SynProxy | String | No | enable | Specifies whether to enable SynProxy to protect backend servers against attacks. We recommend that you use the default value for this parameter. Valid values: enable and disable. |
| MaxConnection | Integer | No | 20 | The maximum number of connections. |
| Tags | String | No | {"tagKey":"Key1", "tagValue":"Valu e1"} | The key and value of the tag. |
| VServerGroup | String | No | on | Specifies whether to use a vServer group. Valid values: on and of f . The value of VserverGroup and the value of Mast erSlaveServerGroup cannot be set to on at the same time. |
| VServerGroupId | String | No | rsp-cige6j5***** | The ID of the vServer group. |
| MasterSlaveServe rGroupId | String | No | rsp-cige****** | The ID of the primary/secondary server group. Not e You cannot specify the vServer group ID and primary/secondary server group ID at the same time. |
| MasterSlaveServe rGroup | String | No | on | Specifies whether to use a primary/secondary server group. Valid values: on and of f . The value of VserverGroup and the value of Mast erSlaveServerGroup cannot be set to on at the same time. |
| EstablishedTimeo ut | Integer | No | 500 | The timeout period of connections. Valid values: 10 to 900. Unit: seconds. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Description | String | No | test | The description of the TCP listener. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | CEF72CEB-54B6- 4AE8-B225- F876FF7BA984 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/? Action=SetLoadBalancerTCPListenerAttribute &ListenerPort=80 &LoadBalancerId=lb-bp1ygod3yctvg1y****** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<SetLoadBalancerTCPListenerAttributeResponse>
     <RequestId>59B41B53-BC4B-481A-9D8D-2A0D20B3FCD1</RequestId>
</SetLoadBalancerTCPListenerAttributeResponse>
```

`JSON` format `{`

```json
    "RequestId": "59B41B53-BC4B-481A-9D8D-2A0D20B3FCD1"
```

`}`

##### 2.6.1.3 DescribeLoadBalancerTCPListenerAttribute

Queries the configurations of a TCP listener. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeLoadBala ncerTCPListenerA ttribute | The operation that you want to perform. Set the value to DescribeLoadBalancerT CPList enerA t t ribut e. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| ListenerPort | Integer | Yes | 80 | The frontend port that is used by the Server Load Balancer (SLB) instance. Valid values: 1 t o 65535. |
| LoadBalancerId | String | Yes | lb- bp1ygod3yctvg1 y****** | The ID of the SLB instance. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| ListenerPort | Integer | 80 | The frontend port that is used by the SLB instance. |
| BackendServerP ort | Integer | 80 | The backend port that is used by the SLB instance. Not e When the SLB instance uses a vServer group, this parameter is not displayed. |
| Bandwidth | Integer | -1 | The maximum bandwidth of the listener. |
| Status | String | stopped | The state of the listener. Valid values: running and st opped. running: indicates that the listener runs as expected. st opped: indicates that the listener is stopped. |
| SynProxy | String | enable | Indicates whether SynProxy is enabled. SynProxy is a feature that protects SLB from attacks. We recommend that you use the default value for this parameter. Valid values: Enable: SynProxy is enabled. Disable: SynProxy is disabled. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Scheduler | String | wrr | The scheduling algorithm. Valid values: wrr (default): Backend servers with higher weights receive more requests than those with lower weights. wlc: Requests are distributed based on the combination of the weights and number of connections to backend servers. If two backend servers have the same weight, the backend server that has fewer connections receives more requests. rr: Requests are distributed to backend servers in sequence. |
| PersistenceTim eout | Integer | 0 | Indicates whether session persistence is enabled. When the value is set to 0, it indicates that session persistence is disabled. |
| HealthCheckTy pe | String | tcp | The health check method that is used by the TCP listener. Valid values: t cp and ht t p. |
| HealthCheck | String | on | Indicates whether health checks are enabled. Valid values: on and of f . |
| HealthyThresho ld | Integer | 4 | The healthy threshold. |
| UnhealthyThres hold | Integer | 4 | The unhealthy threshold. |
| HealthCheckCo nnectPort | Integer | 8080 | The port that is used for health checks. |
| HealthCheckInt erval | Integer | 5 | The interval between two consecutive health checks. Unit: seconds. |
| HealthCheckDo main | String | www.domain.com | The domain name that is used for health checks. |

| Parameter | Type |   | Example | Description |   |   |
|---|---|---|---|---|---|---|
| HealthCheckURI | String |   |   | The URL that is used for health checks. The value must be 1 to 80 characters in length, and can contain letters, digits, hyphens (-), forward slashes (/), |   |   |
|   |   |   |   |   | hyphens (-), forward slashes (/), |   |
|   |   | ing | /test/index.html | periods (.), %? number signs (#), and |   |   |
|   |   |   |   | ampersands (&) |   |   |
| HealthCheckHtt pCode | String |   | http 2xx _ | The HTTP status code that indicates a successful health check. Valid values: ht t p 2xx, ht t p 3xx, ht t p 4xx, and _ _ _ ht t p 5xx. Default value: http 2xx. _ _ |   |   |
| VServerGroupId | String |   | rsp-cige6******8 | The ID of the associated vServer group. |   |   |
| Description | String |   | Description. | The description of the listener. The description must be 1 to 80 characters in length, and can contain letters and Chinese characters, digits, hyphens (-), forward slashes (/), periods (.), and underscores ( ). _ It can also contain Chinese characters. |   |   |
| EstablishedTim eout | Integer |   | 500 | The timeout period of connections. Valid values: 10 t o 900. Unit: seconds. |   |   |
| HealthCheckCo nnectTimeout | Integer |   | 100 | The timeout period. |   |   |
| MasterSlaveSer verGroupId | String |   | rsp-0bfucw***** | The ID of the primary/secondary server group that is associated with the listener. |   |   |
| MaxConnection | Integer |   | 10 | The maximum number of connections. |   |   |
| RequestId | String |   | 365F4154-92F6- 4AE4-92F8- 7FF34B540710 | The ID of the request. |   |   |

Examples Sample requests

```
http(s)://[Endpoint]/? Action=DescribeLoadBalancerTCPListenerAttribute &ListenerPort=80 &LoadBalancerId=lb-bp1ygod3yctvg1y****** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeLoadBalancerTCPListenerAttributeResponse>
     <HealthCheckHttpCode>http_2xx,http_3xx</HealthCheckHttpCode>
   <PersistenceTimeout>0</PersistenceTimeout>
   <HealthCheckType>tcp</HealthCheckType>
   <HealthyThreshold>3</HealthyThreshold>
   <Scheduler>wrr</Scheduler>
   <UnhealthyThreshold>3</UnhealthyThreshold>
   <Bandwidth>-1</Bandwidth>
   <Description>tcp_80</Description>
   <AclStatus>off</AclStatus>
   <HealthCheckURI>/</HealthCheckURI>
   <HealthCheck>on</HealthCheck>
   <HealthCheckConnectTimeout>5</HealthCheckConnectTimeout>
   <ListenerPort>80</ListenerPort>
   <Status>running</Status>
   <EstablishedTimeout>900</EstablishedTimeout>
   <HealthCheckDomain></HealthCheckDomain>
   <HealthCheckInterval>2</HealthCheckInterval>
   <RequestId>9A113A8C-BB8F-475E-9533-7819ECA2FFC1</RequestId>
   <BackendServerPort>80</BackendServerPort>
    </DescribeLoadBalancerTCPListenerAttributeResponse>
```

`JSON` format `{`

```json
    "HealthCheckHttpCode": "http_2xx,http_3xx",
    "PersistenceTimeout": 0,
    "HealthCheckType": "tcp",
    "HealthyThreshold": 3,
    "Scheduler": "wrr",
    "UnhealthyThreshold": 3,
    "Bandwidth": -1,
    "Description": "tcp_80",
    "AclStatus": "off",
    "HealthCheckURI": "/",
    "HealthCheck": "on",
    "HealthCheckConnectTimeout": 5,
    "ListenerPort": 80,
    "Status": "running",
    "EstablishedTimeout": 900,
    "HealthCheckDomain": "",
    "HealthCheckInterval": 2,
    "RequestId": "9A113A8C-BB8F-475E-9533-7819ECA2FFC1",
    "BackendServerPort": 80
```

`}`

#### 2.6.2 UDP listeners

##### 2.6.2.1 CreateLoadBalancerUDPListener

Creates a UDP listener. Not e You cannot view the source IP addresses of network traffic if you create UDP listeners for a Server Load Balancer (SLB) instance that is deployed in a classic network. In addition, newly created listeners are in the st opped state. After a listener is created, you must call the StartLoadBalancerListener operation to enable the listener. This way, the listener can forward network traffic. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateLoadBalan cerUDPListener | The operation that you want to perform. Set the value to Creat eLoadBalancerUDPList ener. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Bandwidth | Integer | Yes | 34 | The maximum bandwidth of the listener. Unit: Mbit/s. Set the value to -1. -1: For a pay-by-data-transfer Internet-facing SLB instance, you can set the value to -1. This indicates that the maximum bandwidth is not limited. |
| ListenerPort | Integer | Yes | 80 | The frontend port that is used by the SLB instance. Valid values: 1 t o 65535. |
| LoadBalancerId | String | Yes | lb- bp1ygod3yctvg1 y7****** | The ID of the SLB instance. |
| BackendServerPor t | Integer | No | 80 | The backend port that is used by the SLB instance. Valid values: 1 t o 65535. If the VServerGroupId parameter is not set, this parameter is required. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Scheduler | String | No | wrr | The scheduling algorithm. Valid values: wrr (default): Backend servers that have higher weights receive more requests than those that have lower weights. wlc: Requests are distributed based on the combination of the weights and number of connections to backend servers. If two backend servers have the same weight, the backend server that has fewer connections receives more requests. rr: Requests are distributed to backend servers in sequence. sch: Specifies consistent hashing that is based on source IP addresses. Requests from the same source IP address are distributed to the same backend server. t ch: Specifies consistent hashing that is based on four factors: source IP address, destination IP address, source port number, and destination port number. Requests that contain the same preceding information are distributed to the same backend server. qch: Specifies consistent hashing that is based on QUIC connection IDs. Requests that contain the same QUIC connection ID are distributed to the same backend server. Not e Only guaranteed- performance SLB instances support the sch, tch, and qch consistent hashing algorithms. |
| HealthyThreshold | Integer | No | 4 | Specifies the number of consecutive health check successes required before a backend server is declared healthy (from f ail to success). Valid values: 2 t o 10. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| UnhealthyThresh old | Integer | No | 4 | Specifies the number of consecutive health check failures required before a backend server is declared unhealthy (from success to f ail). Valid values: 2 t o 10. |
| HealthCheckConn ectTimeout | Integer | No | 100 | The timeout period of a health check response. If the backend Elastic Compute Service (ECS) instance does not send an expected response within the specified period of time, the health check fails. Valid values: 1 t o 300. Unit: seconds. |
| HealthCheckConn ectPort | Integer | No | 80 | The port that is used for health checks. Valid values: 1 t o 65535. If you do not specify this parameter, the backend port is used to send health check probes. |
| healthCheckInterv al | Integer | No | 3 | The interval between two consecutive health checks. Valid values: 1 t o 50. Unit: seconds. |
| healthCheckReq | String | No | hello | Specifies the request string for UDP listener health checks. The request string must be 1 to 500 characters in length, and can contain only letters and digits. |
| healthCheckExp | String | No | ok | Specifies the response string for UDP listener health checks. The response string must be 1 to 500 characters in length, and can contain only letters and digits. |
| VServerGroupId | String | No | rsp-cige6j****8 | The ID of the vServer group. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| MasterSlaveServe rGroupId | String | No | rsp-0bfucwu**** | The ID of the primary/secondary server group. Not e You cannot specify both the vServer group ID and primary/secondary server group ID. |
| Description | String | No | test | The description of the listener. The description must be 1 to 80 characters in length, and can contain letters, digits, hyphens (-), forward slashes (/), periods (.), and underscores ( ). It can also contain _ Chinese characters. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | CEF72CEB-54B6- 4AE8-B225- F876FF7BA984 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/? Action=CreateLoadBalancerUDPListener &Bandwidth=34 &ListenerPort=80 &LoadBalancerId=lb-bp1ygod3yctvg1y7****** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<CreateLoadBalancerUDPListenerResponse>
      <RequestId>06F00FBB-3D9E-4CCE-9D43-1A6946A75456</RequestId>
</CreateLoadBalancerUDPListenerResponse>
```

`JSON` format `{`

```json
    "RequestId": "06F00FBB-3D9E-4CCE-9D43-1A6946A75456"
```

`}` Error codes

| HttpCode | Error code | Error message | Required |
|---|---|---|---|
| 400 | Abs.VServerGroupId AndMasterSlaveServ erGroupId.MissMatch | The parameters VServerGroupId or MasterSlaveServerGroupId miss match. | The error message returned because the vServerGroupId parameter or the MasterSlaveServerGroupId parameter that is returned does not match the parameter that is specified in the request. |

##### 2.6.2.2 SetLoadBalancerUDPListenerAttribute

Modifies the configurations of a UDP listener. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | SetLoadBalancer UDPListenerAttrib ute | The operation that you want to perform. Set the value to Set LoadBalancerUDPList enerAt t rib ut e. |
| ListenerPort | Integer | Yes | 80 | The frontend port that is used by the Server Load Balancer (SLB) instance. Valid values: 1 to 65535. |
| LoadBalancerId | String | Yes | lb- bp1rtfnodmywb4 3ecu4sf-c**** | The ID of the SLB instance. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Bandwidth | Integer | No | -1 | The maximum bandwidth of the listener. Unit: Mbit/s. Valid values: 1 t o 5120 and -1. -1: For a pay-by-data-transfer Internet-facing SLB instance, you can set the value to -1. This indicates that the maximum bandwidth is not limited. 1 t o 5120: For a pay-by-bandwidth Internet-facing SLB instance, you can specify the maximum bandwidth of each listener. The sum of maximum bandwidth values of all listeners cannot exceed the maximum bandwidth of the SLB instance. For more information, see Bandwidth of a shared-resource SLB instance. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Scheduler | String | No | wrr | The scheduling algorithm. Valid values: wrr: Backend servers that have higher weights receive more requests than those that have lower weights. wlc: Requests are distributed based on the combination of the weights and number of connections to backend servers. If two backend servers have the same weight, the backend server that has fewer connections receives more requests. rr: Requests are distributed to backend servers in sequence. sch: Specifies consistent hashing that is based on source IP addresses. Requests from the same source IP address are distributed to the same backend server. t ch: Specifies consistent hashing that is based on four factors: source IP address, destination IP address, source port number, and destination port number. Requests that contain the same preceding information are distributed to the same backend server. qch: Specifies consistent hashing that is based on QUIC connection IDs. Requests that contain the same QUIC connection ID are distributed to the same backend server. Not e Only guaranteed- performance SLB instances support sch, tch, and qch. |
| HealthyThreshold | Integer | No | 4 | Specifies the number of consecutive health check successes required before a backend server is declared healthy (from f ail to success). Valid values: 2 to 10. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| UnhealthyThresh old | Integer | No | 4 | Specifies the number of consecutive health check failures required before a backend server is declared unhealthy (from success to f ail). Valid values: 2 to 10. |
| HealthCheckConn ectTimeout | Integer | No | 100 | The time period to wait for a health check response. If the backend Elastic Compute Service (ECS) instance does not send an expected response within the specified period of time, the health check fails. Valid values: 1 to 300. Not e If the value of the Healt hCheckConnect T imeout parameter is smaller than that of the Healt hCheckInt erval parameter, the value of the Healt hCheckConnect T imeout parameter is ignored and the value of the Healt hCheckInt erval parameter is regarded as the waiting period. |
| HealthCheckConn ectPort | Integer | No | 80 | The port that is used for health checks. Valid values: 1 to 65535. |
| HealthCheckInterv al | Integer | No | 5 | The interval between two consecutive health checks. Valid values: 1 to 50. Unit: seconds. |
| healthCheckReq | String | No | hello | The request string for UDP listener health checks. The string must be 1 to 500 characters in length and can contain only letters and digits. |
| healthCheckExp | String | No | ok | The response string for UDP listener health checks. The string must be 1 to 500 characters in length and can contain only letters and digits. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| MaxConnection | Integer | No | 10 | The maximum number of connections. |
| Tags | String | No | {"tagKey":"Key1", "tagValue":"Valu e1"} | The key and value of the tag. |
| VServerGroup | String | No | on | Specifies whether to use a vServer group. Valid values: on and of f . Not e The value of VserverGroup and the value of Mast erSlaveServerGroup cannot be set to on at the same time. |
| VServerGroupId | String | No | rsp-cige6****** | The ID of the vServer group. |
| MasterSlaveServe rGroupId | String | No | rsp-0bfuc***** | The ID of the primary/secondary server group. Not e You cannot specify the vServer group ID and primary/secondary server group ID at the same time. |
| MasterSlaveServe rGroup | String | No | on | Specifies whether to use a primary/secondary server group. Valid values: on and of f . The value of VserverGroup and the value of Mast erSlaveServerGroup cannot be set to on at the same time. |
| Description | String | No | test | The description of the listener. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | CEF72CEB-54B6- 4AE8-B225- F876FF7BA984 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/? Action=SetLoadBalancerUDPListenerAttribute &ListenerPort=80 &LoadBalancerId=lb-bp1rtfnodmywb43ecu4sf-c**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<SetLoadBalancerUDPListenerAttributeResponse>
     <RequestId>A0F0643E-D653-4F6F-A67F-205B2A92BE18</RequestId>
</SetLoadBalancerUDPListenerAttributeResponse>
```

`JSON` format `{`

```json
    "RequestId": "A0F0643E-D653-4F6F-A67F-205B2A92BE18"
```

`}`

##### 2.6.2.3 DescribeLoadBalancerUDPListenerAttribute

Queries the configurations of a UDP listener. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeLoadBala ncerUDPListenerA ttribute | The operation that you want to perform. Set the value to DescribeLoadBalancerUDPList ener At t ribut e. |
| ListenerPort | Integer | No | 80 | The frontend port that is used by the Server Load Balancer (SLB) instance. Valid values: 1 t o 65535. |
| LoadBalancerId | String | Yes | lb- bp1rtfnodmywb4 3e**** | The ID of the SLB instance. |
| access key id _ _ | String | No | acc- hp34s2h0xx1ht4n wo**** | The AccessKey ID. |

| erver Load Balancer |   |   |   | Developer Guide·API referenc |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Tags | String | No | {"tagKey":"Key1", "tagValue":"Valu e1"} | The key and value of the tag. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| ListenerPort | Integer | 80 | The frontend port that is used by the SLB instance. |
| BackendServerP ort | Integer | 53 | The backend port that is used by the SLB instance. Not e If the listener is associated with a vServer group, this parameter is not returned. |
| Bandwidth | Integer | -1 | The bandwidth limit of the listener. Unit: Mbit/s. Valid values: -1: For a pay-by-data-transfer Internet- facing SLB instance, -1 is used. This indicates that the bandwidth of the listener is unlimited. 1 to 5120: For a pay-by-bandwidth Internet-facing SLB instance, you can specify a bandwidth limit for each listener. The sum of bandwidth limits that you set for all listeners cannot exceed the bandwidth limit of the SLB instance. |
| Status | String | stopped | The state of the listener. Valid values: running and st opped. running: The listener runs as expected. st opped: The listener is disabled. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Scheduler | String | wrr | The scheduling algorithm. Valid values: wrr (default): Backend servers with higher weights receive more requests than backend servers with lower weights. wlc: Requests are forwarded based on the weight and number of connections to each backend server. If two backend servers have the same weight, the backend server that has fewer connections is expected to receive more requests. rr: Requests are distributed to backend servers in sequence. |
| HealthCheck | String | on | Indicates whether health checks are enabled. Valid values: on and of f . |
| HealthyThresho ld | Integer | 4 | The number of times that a backend server must consecutively pass health checks before it is declared healthy. |
| UnhealthyThres hold | Integer | 4 | The number of times that a backend server must consecutively fail health checks before it is declared unhealthy. |
| HealthCheckCo nnectTimeout | Integer | 100 | The timeout period for a health check response. |
| HealthCheckCo nnectPort | Integer | 8080 | The port that is used for health checks. Not e This parameter takes effect only when the Healt hCheck parameter is set to on. |
| HealthCheckInt erval | Integer | 5 | The interval between two consecutive health checks. Unit: seconds. |
| VServerGroupId | String | rsp-cige6j**** | The ID of the vServer group that is associated with the listener. |

| erver Load Balanc | er |   | Developer Guide·API referenc |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| Description | String | AccessControlDescri ption. | The description of access control. |
| HealthCheckExp | String | ok | The response string for UDP listener health checks. |
| HealthCheckRe q | String | hello | The request string for UDP listener health checks. |
| MasterSlaveSer verGroupId | String | rsp-0bfucw**** | The ID of the primary/secondary server group that is associated with the listener. |
| MaxConnection | Integer | 20 | The maximum number of connections. |
| PersistenceTim eout | Integer | 0 | The timeout period of session persistence. Unit: seconds. Valid values: 0 t o 3600. The default value is 0, which indicates that session persistence is disabled. |
| RequestId | String | 365F4154-92F6- 4AE4-92F8- 7FF34B540710 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=DescribeLoadBalancerUDPListenerAttribute &ListenerPort=80 &LoadBalancerId=lb-bp1rtfnodmywb43e**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<MaxConnection>20</MaxConnection> <Status>stopped</Status> <VServerGroupId>rsp-cige6j****</VServerGroupId> <ListenerPort>80</ListenerPort> <Description>AccessControlDescription </Description> <HealthCheckInterval>5</HealthCheckInterval> <RequestId>365F4154-92F6-4AE4-92F8-7FF34B540710</RequestId> <UnhealthyThreshold>4</UnhealthyThreshold> <Scheduler>wrr</Scheduler> <HealthCheckConnectTimeout>100</HealthCheckConnectTimeout> <HealthCheck>on</HealthCheck> <BackendServerPort>53</BackendServerPort> <PersistenceTimeout>0</PersistenceTimeout> <HealthCheckReq>hello</HealthCheckReq> <HealthCheckConnectPort>8080</HealthCheckConnectPort> <HealthCheckExp>ok</HealthCheckExp> <HealthyThreshold>4</HealthyThreshold> <Bandwidth>-1</Bandwidth> <MasterSlaveServerGroupId>rsp-0bfucw****</MasterSlaveServerGroupId>
```

`JSON` format `{`

```json
    "MaxConnection": 20,
    "Status": "stopped",
    "VServerGroupId": "rsp-cige6j****",
    "ListenerPort": 80,
    "Description": "AccessControlDescription",
    "HealthCheckInterval": 5,
    "RequestId": "365F4154-92F6-4AE4-92F8-7FF34B540710",
    "UnhealthyThreshold": 4,
    "Scheduler": "wrr",
    "HealthCheckConnectTimeout": 100,
    "HealthCheck": "on",
    "BackendServerPort": 53,
    "PersistenceTimeout": 0,
    "HealthCheckReq": "hello",
    "HealthCheckConnectPort": 8080,
    "HealthCheckExp": "ok",
    "HealthyThreshold": 4,
    "Bandwidth": -1,
    "MasterSlaveServerGroupId": "rsp-0bfucw****"
```

`}`

#### 2.6.3 HTTP listeners

##### 2.6.3.1 CreateLoadBalancerHTTPListener

Creates an HTTP listener. Not e A newly created listener is in the st opped state. After a listener is created, call the `StartLoadBalancerListener` operation to enable the listener to forward network traffic. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateLoadBalan cerHTTPListener | The operation that you want to perform. Set the value to Creat eLoadBalancerHT T PList ener. |
| Bandwidth | Integer | Yes | -1 | The bandwidth limit of the listener. Unit: Mbit/s. Valid values: -1: If you set the value to -1, the bandwidth of the listener is unlimited. 1 t o 5120: the bandwidth limit of the listener. The sum of the bandwidth limits of all listeners added to a Server Load Balancer (SLB) instance does not exceed the bandwidth limit of the SLB instance. Not e This parameter is available only in the Chinese mainland. |
| HealthCheck | String | Yes | on | Specifies whether to enable health checks. Valid values: on and of f . |
| ListenerPort | Integer | Yes | 80 | The frontend port that is used by the SLB instance. Valid values: 1 t o 65535. |
| LoadBalancerId | String | Yes | lb- bp1c9vixxjh92q83 tw**** | The ID of the SLB instance. |

| Parameter | Type | Required | Example | Description |   |   |
|---|---|---|---|---|---|---|
| StickySession | String | Yes | off | Specifies whether to enable session persistence. Valid values: on and of f . |   |   |
| BackendServerPor t | Integer | No | 80 | The backend port that is used by the SLB instance. Valid values: 1 t o 65535. Not e If the VServerGroupId parameter is not set, this parameter is required. |   |   |
| XForwardedFor | String | No | on | Specifies whether to use the X- Forwarded-For header to retrieve client IP addresses. Set the value to on. |   |   |
|   |   |   |   |   | X- |   |
| Scheduler | String | No | wrr | The scheduling algorithm. Valid values: wrr (default): Backend servers with higher weights receive more requests than backend servers with lower weights. wlc: Requests are forwarded based on the weight and number of connections to each backend server. If two backend servers have the same weight, the backend server that has fewer connections is expected to receive more requests. rr: Requests are distributed to backend servers in sequence. |   |   |

|   | Forwarded-For |
|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| StickySessionTyp e | String | No | insert | The method that is used to handle a cookie. Valid values: insert : inserts a cookie. SLB inserts a cookie (SERVERID) into the first HTTP or HTTPS response that is sent to a client. The next request from the client carries this cookie, and the listener will forward this request to the recorded backend server. server: rewrites a cookie. When SLB detects a user-defined cookie, it overwrites the original cookie with the user-defined cookie. The next request from the client carries the user-defined cookie, and the listener will distribute this request to the recorded backend server. Not e This parameter is required if the St ickySession parameter is set to on. |
| CookieTimeout | Integer | No | 500 | The timeout period of a cookie. Valid values: 1 t o 86400. Unit: seconds. Not e If St ickySession is set to on and St ickySessionT ype is set to insert , this parameter is required. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Cookie | String | No | B490B5EBF6F3CD4 02E515D22BCDA1 598 | The cookie to be configured on a backend server. It must be 1 to 200 characters in length, and can contain only ASCII characters and digits. It cannot contain commas (,), semicolons (;), or space characters. It cannot start with a dollar sign ($). Not e This parameter is required if the St ickySession parameter is set to on and the St ickySessionT ype parameter is set to server. |
| HealthCheckDom ain | String | No | 172.XX.XX.6 | The domain name that is used for health checks. Valid values: $ ip: the private IP address of a _ backend server. If you do not set this parameter or set the parameter to $ ip, the SLB instance uses the _ private IP address of each backend server for health checks. domain: The domain name must be 1 to 80 characters in length, and can contain only letters, digits, periods (.), and hyphens (-). Not e This parameter takes effect only when the Healt hCheck parameter is set to on. |

| Parameter | Type | Required | Example | Description |   |   |
|---|---|---|---|---|---|---|
| HealthCheckURI | String | No | /test/index.html | The URI used for health checks. It must be 1 to 80 characters in length and can contain only letters, digits, and the following special characters: - / . % ? # & . The URL cannot be a single forward slash (/) but it must start with a forward slash (/). Not e This parameter takes effect only when the Healt hCheck parameter is set to on. |   |   |
|   |   |   |   |   | - / |   |
| HealthyThreshold | Integer | No | 4 | The number of times that an unhealthy backend server must consecutively pass health checks before it is declared healthy. In this case, the health status is changed from f ail to success. Valid values: 2 t o 10. Not e This parameter takes effect only when the Healt hCheck parameter is set to on. |   |   |
| UnhealthyThresh old | Integer | No | 4 | The number of times that a healthy backend server must consecutively fail health checks before it is declared unhealthy. In this case, the health status is changed from success to f ail. Valid values: 2 t o 10. Not e This parameter takes effect only when the Healt hCheck parameter is set to on. |   |   |

|   | . % ? # & |
|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| HealthCheckTime out | Integer | No | 3 | The timeout period of a health check. If a backend Elastic Compute Service (ECS) instance does not send an expected response within the specified timeout period, the health check fails. This parameter takes effect only when the Healt hCheck parameter is set to on. Valid values: 1 t o 300. Unit: seconds. Not e If the value of the Healt hCheckT imeout parameter is smaller than that of the Healt hCheckInt erval parameter, the timeout period specified by the Healt hCheckT imeout parameter is ignored and the value of the Healt hCheckInt erval parameter is used as the timeout period. |
| HealthCheckConn ectPort | Integer | No | 80 | The backend port that is used for health checks. Valid values: 1 t o 65535. Not e This parameter takes effect only when the Healt hCheck parameter is set to on. |
| HealthCheckInterv al | Integer | No | 5 | The interval between two consecutive health checks. Valid values: 1 t o 50. Unit: seconds. Not e This parameter takes effect only when the Healt hCheck parameter is set to on. |

| Parameter | Type | Required | Example | Description |   |   |
|---|---|---|---|---|---|---|
| HealthCheckHttpC ode | String | No | http 2xx,http 3x _ _ x | The HTTP status code for a successful health check. Separate multiple HTTP status codes with commas (,). Default value: ht t p 2xx. _ Valid values: ht t p 2xx, ht t p 3xx, _ _ ht t p 4xx, and ht t p 5xx. _ _ Not e This parameter takes effect only when the Healt hCheck parameter is set to on. |   |   |
| MaxConnection | Integer | No | 20 | The maximum number of connections. |   |   |
| access key id _ _ | String | No | acc- hp34s2h0xx1ht4n wo**** | The AccessKey ID. |   |   |
| VServerGroupId | String | No | rsp-cige6j**** | The ID of the vServer group. |   |   |
| Tags | String | No | null | The key and value of the tag. |   |   |
| XForwardedFor S _ LBIP | String | No | on | Specifies whether to use the SLB- IP header to retrieve client IP addresses. Valid values: on and of f . Default value: off. |   |   |
| XForwardedFor S _ LBID | String | No | on | Specifies whether to use the SLB- ID header to retrieve the ID of the SLB instance. Valid values: on and of f . Default value: off. |   |   |
| XForwardedFor p _ roto | String | No | on | Specifies whether to use the X- Forwarded-Proto header to retrieve the listener protocol. Valid values: on and of f . Default value: off. |   |   |
|   |   |   |   |   | X- |   |

|   | IP |
|---|---|

|   | ID |
|---|---|

|   | Forwarded-Proto |
|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Gzip | String | No | on | Specifies whether to enable gzip compression to compress specific types of files. Default value: on. Valid values: on and of f . Default value: off. |
| IdleTimeout | Integer | No | 3 | The timeout period of an idle connection. Valid values: 1 to 60. Default value: 15. Unit: seconds. If no request is received within the specified timeout period, SLB closes the connection. When another request is received, SLB establishes a new connection. |
| RequestTimeout | Integer | No | 6 | The timeout period of a request. Valid values: 1 to 180. Unit: seconds. Default value: 60. If no response is received from the backend server within the specified timeout period, SLB sends an HTTP 504 error code to the client. |
| ListenerForward | String | No | off | Specifies whether to enable HTTP-to- HTTPS redirection. Valid values: on and of f . |
| ForwardPort | Integer | No | 443 | The listening port that is used to redirect HTTP requests to HTTPS. |
| Description | String | No | ListenerDescriptio n | The description of the listener. The description must be 1 to 80 characters in length, and can contain letters, digits, hyphens (-), forward slashes (/), periods (.), and underscores ( ). Chinese characters are _ supported. |

|   | 504 |
|---|---|

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | CEF72CEB-54B6- 4AE8-B225- F876FF7BA984 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=CreateLoadBalancerHTTPListener &Bandwidth=-1 &HealthCheck=on &ListenerPort=80 &LoadBalancerId=lb-bp1c9vixxjh92q83tw**** &StickySession=off &<Common request parameters>
```

Sample success responses `XML` format

```xml
<CreateLoadBalancerHTTPListenerResponse>
   <RequestId>1FF504CB-BFFF-4508-A51A-58A416604FC8</RequestId>
</CreateLoadBalancerHTTPListenerResponse>
```

`JSON` format `{`

```json
    "RequestId": "1FF504CB-BFFF-4508-A51A-58A416604FC8"
```

`}`

##### 2.6.3.2 SetLoadBalancerHTTPListenerAttribute

Modifies the configurations of an HTTP listener. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | SetLoadBalancer HTTPListenerAttri bute | The operation that you want to perform. Set the value to Set LoadBalancerHT T PList enerAt t ri but e. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| ListenerPort | Integer | Yes | 80 | The frontend port that is used by the Server Load Balancer (SLB) instance. Valid values: 1 to 65535. |
| LoadBalancerId | String | Yes | lb- bp1qjwo61pqz3a h***** | The ID of the SLB instance. |
| Bandwidth | Integer | No | -1 | The maximum bandwidth of the listener. Unit: Mbit/s. Valid values: 1 t o 5120 and -1. -1: For a pay-by-data-transfer Internet-facing SLB instance, you can set the value to -1. This indicates that the maximum bandwidth is not limited. |
| XForwardedFor | String | No | on | Specifies whether to use the X- Forwarded-For header to obtain the real IP address of the client. Set the value to on. |
| Scheduler | String | No | wrr | The scheduling algorithm. Valid values: wrr: Backend servers that have higher weights receive more requests than those that have lower weights. wlc: Requests are distributed based on the combination of the weights and number of connections to backend servers. If two backend servers have the same weight, the backend server that has fewer connections receives more requests. rr: Requests are distributed to backend servers in sequence. |
| StickySession | String | No | on | Specifies whether to enable session persistence. Valid values: on and of f . |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| StickySessionTyp e | String | No | insert | The method that is used to handle a cookie. Valid values: insert : insets a cookie. SLB inserts a cookie (SERVERID) into the first HTTP or HTTPS response that is sent to a client. The next request from the client will contain this cookie, and the listener will distribute this request to the recorded backend server. server: rewrites a cookie. When SLB detects a user-defined cookie, it overwrites the original cookie with the user-defined cookie. The next request from the client will contain the user-defined cookie, and the listener will distribute the request to the recorded backend server. Not e If you set the St ickySession parameter to on, you must specify a value for this parameter. |
| CookieTimeout | Integer | No | 500 | The timeout period of a cookie. Valid values: 1 to 86400. Unit: seconds. Not e If you set the St ickySession parameter to on and the St ickySessionT ype parameter to insert , this parameter is required. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Cookie | String | No | B490B5EBF6F3CD4 02E515D22BCDA1 598 | The cookie to be configured on the backend server. The value must be 1 to 200 characters in length, and can contain only ASCII letters and digits. It cannot contain commas (,), semicolons (;), or spaces. It cannot start with a dollar sign ($). Not e If you set the St ickySession parameter to on and the St ickySessionT ype parameter to server, this parameter is required. |
| HealthCheck | String | No | on | Specifies whether to enable health checks. Valid values: on and of f . |
| HealthCheckDom ain | String | No | 172.16.**. ** | The domain name that is used for health checks. Valid values: $ ip: The private IP address of the _ backend server. If the $ ip _ parameter is specified or the HealthCheckDomain parameter is not specified, the SLB instance uses the private IP address of the backend server as the domain name for health checks. domain: The domain name must be 1 to 80 characters in length. It can contain only letters, digits, periods (.), and hyphens (-). Not e This parameter takes effect only when the Healt hCheck parameter is set to on. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| HealthCheckURI | String | No | /test/index.html | The URL that is used for health checks. The value must be 1 to 80 characters in length, and can contain only letters, digits, hyphens (-), forward slashes (/), periods (.), percent signs (%), question marks (?), number signs (#), and ampersands (&). The URL must not be a single forward slash (/) and it must start with a forward slash (/). Not e This parameter takes effect only when the Healt hCheck parameter is set to on. |
| HealthyThreshold | Integer | No | 4 | Specifies the number of consecutive health check successes required before a backend server is declared healthy (from f ail to success). Valid values: 2 to 10. Not e This parameter takes effect only when the Healt hCheck parameter is set to on. |
| UnhealthyThresh old | Integer | No | 4 | Specifies the number of consecutive health check failures required before a backend server is declared unhealthy (from success to f ail). Valid values: 2 to 10. Not e This parameter takes effect only when the Healt hCheck parameter is set to on. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| HealthCheckTime out | Integer | No | 3 | The timeout period for a health check response. If a backend server does not respond within the specified timeout period, the health check fails. This parameter takes effect only when the Healt hCheck parameter is set to on. Valid values: 1 to 300. Unit: seconds. Not e If the value of the Healt hCHeckT imeout parameter is smaller than that of the Healt hCheckInt erval parameter, the value of the Healt hCHeckT imeout parameter is ignored and the value of the Healt hCheckInt erval parameter is regarded as the waiting period. |
| HealthCheckInterv al | Integer | No | 5 | The interval between two consecutive health checks. Valid values: 1 to 50. Unit: seconds. Not e This parameter takes effect only when the Healt hCheck parameter is set to on. |
| HealthCheckConn ectPort | Integer | No | 8080 | The port that is used for health checks. Valid values: 1 to 65535. Not e This parameter takes effect only when the Healt hCheck parameter is set to on. |

| Parameter | Type | Required | Example | Description |   |   |
|---|---|---|---|---|---|---|
| HealthCheckHttpC ode | String | No | http 2xx _ | The HTTP status code that indicates a successful health check. Separate multiple HTTP status codes with commas (,). Valid values: ht t p 2xx, ht t p 3xx, _ _ ht t p 4xx, and ht t p 5xx. _ _ Not e This parameter takes effect only when the Healt hCheck parameter is set to on. |   |   |
| MaxConnection | Integer | No | 10 | The maximum number of connections. |   |   |
| VServerGroup | String | No | on | Specifies whether to use a vServer group. Valid values: on and of f . |   |   |
| VServerGroupId | String | No | rsp-cige6j***** | The ID of the vServer group. |   |   |
| Tags | String | No | {"tagKey":"Key1", "tagValue":"Valu e1"} | The key and value of the tag. |   |   |
| XForwardedFor S _ LBIP | String | No | on | Specifies whether to use the SLB- IP header to obtain the real IP address of the client. Valid values: on and of f . |   |   |
| XForwardedFor S _ LBID | String | No | on | Specifies whether to use the SLB- ID header to obtain the ID of the SLB instance. Valid values: on and of f . |   |   |
| XForwardedFor p _ roto | String | No | on | Specifies whether to use the X- Forwarded-Proto header to obtain the listener protocol of the SLB instance. Valid values: on and of f . |   |   |
|   |   |   |   |   | X- |   |

|   | IP |
|---|---|

|   | ID |
|---|---|

|   | Forwarded-Proto |
|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Gzip | String | No | on | Specifies whether to enable gzip compression to compress files of a specific type. Valid values: on and of f . |
| IdleTimeout | Integer | No | 12 | The timeout period of an idle connection. Unit: seconds. Valid values: 1 to 60. Default value: 15. If no request is received during the specified timeout period, the SLB instance closes the connection. When another request is received, the SLB instance establishes a new connection. |
| RequestTimeout | Integer | No | 3 | The timeout period of a request. Unit: seconds. Valid values: 1 to 180. Default value: 60. If no response is received from the backend server during the request timeout period, SLB sends an HTTP 504 error code to the client. |
| Description | String | No | test | The description of the listener. |

|   | 504 |
|---|---|

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | CEF72CEB-54B6- 4AE8-B225- F876FF7BA984 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/? Action=SetLoadBalancerHTTPListenerAttribute &ListenerPort=80 &LoadBalancerId=lb-bp1qjwo61pqz3ah***** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<SetLoadBalancerHTTPListenerAttributeResponse>
      <RequestId>CEF72CEB-54B6-4AE8-B225-F876FF7BA984</RequestId>
</SetLoadBalancerHTTPListenerAttributeResponse>
```

`JSON` format

```json
{"RequestId":" CEF72CEB-54B6-4AE8-B225-F876FF7BA984"
```

`}`

##### 2.6.3.3 DescribeLoadBalancerHTTPListenerAttribute

Queries the configurations of an HTTP listener. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeLoadBala ncerHTTPListener Attribute | The operation that you want to perform. Set the value to DescribeLoadBalancerHT T PList ene rAt t ribut e. |
| ListenerPort | Integer | Yes | 80 | The frontend port that is used by the Server Load Balancer (SLB) instance. Valid values: 1 t o 65535. |
| LoadBalancerId | String | Yes | lb- bp1o94dp5**** | The ID of the SLB instance. |
| access key id _ _ | String | No | acc- hp34s2h0xx1ht4n wo**** | The AccessKey ID. |
| Tags | String | No | null | The key and value of the tag. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| ListenerPort | Integer | 80 | The frontend port that is used by the SLB instance. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Bandwidth | Integer | -1 | The bandwidth limit of the listener. Unit: Mbit/s. Valid values: -1: If this parameter is set to -1, the bandwidth of the listener is unlimited. 1 t o 5120: the bandwidth limit of the listener. The sum of the bandwidth limits of all listeners added to an SLB instance does not exceed the bandwidth limit of the SLB instance. Not e This parameter is available only in mainland China. |
| Status | String | stopped | The status of the listener. Valid values: running and st opped. running: The listener runs as expected. st opped: The listener is disabled. |
| XForwardedFor | String | on | Indicates whether the X-Forwarded-For header is used to retrieve client IP addresses. Valid values: on and of f . |
| Scheduler | String | wrr | The scheduling algorithm. Valid values: wrr, wlc, and rr. wrr (default): Backend servers with higher weights receive more requests than backend servers with lower weights. wlc: Requests are forwarded based on the weight and number of connections to each backend server. If two backend servers have the same weight, the backend server that has fewer connections is expected to receive more requests. rr: Requests are distributed to backend servers in sequence. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| StickySession | String | on | Indicates whether session persistence is enabled. Valid values: on and of f . Default value: off. |
| StickySessionTy pe | String | insert | The method that is used to handle a cookie. Valid values: insert and server. insert : inserts a cookie. SLB inserts a cookie (SERVERID) into the first HTTP or HTTPS response that is sent to a client. The next request from the client carries this cookie, and the listener will forward this request to the recorded backend server. server: rewrites a cookie. When SLB detects a user-defined cookie, it overwrites the original cookie with the user- defined cookie. The next request from the client carries the user-defined cookie, and the listener will distribute this request to the recorded backend server. Not e This parameter is required if the St ickySession parameter is set to on. |
| CookieTimeout | Integer | 500 | The timeout period of a cookie. |
| Cookie | String | B490B5EBF6F3CD402 E515D22BCDA1598 | The cookie that is configured on a backend server. The cookie is 1 to 200 characters in length, and can contain only ASCII letters and digits. It cannot contain commas (,), semicolons (;), or space characters. It does not start with a dollar sign ($). |
| HealthCheck | String | on | Indicates whether health checks are enabled. Valid values: on and of f . |
| HealthCheckDo main | String | www.example.com | The domain name that is used for health checks. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| HealthCheckURI | String | /test/index.html | The URI used for health checks. It is 1 to 80 characters in length, and can contain letters, digits, hyphens (-), forward slashes (/), periods (.), percent signs (%), question marks (?), number signs (#), and ampersands (&). The URL is not a single forward slash (/) but it starts with a forward slash (/). ) |
| HealthyThresho ld | Integer | 4 | The healthy threshold. |
| UnhealthyThres hold | Integer | 4 | The unhealthy threshold. |
| HealthCheckTi meout | Integer | 3 | The timeout period of a health check response. Valid values: 1 to 300. Unit: seconds. |
| HealthCheckInt erval | Integer | 5 | The interval between two consecutive health checks. Valid values: 1 to 50. Unit: seconds. |
| HealthCheckHtt pCode | String | http 2xx _ | The HTTP status code that indicates a successful health check. Multiple HTTP status codes are separated with commas (,). Valid values: ht t p 2xx (default), ht t p 3xx, _ _ ht t p 4xx, and ht t p 5xx. _ _ Not e This parameter takes effect only when the Healt hCheck parameter is set to on. |
| HealthCheckCo nnectPort | Integer | 8080 | The port that is used for health checks. Not e This parameter takes effect only when the Healt hCheck parameter is set to on. |
| VServerGroupId | String | rsp-cige6j**** | The ID of the server group that is associated with the listener. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Gzip | String | on | Indicates whether gzip compression is enabled to compress specific types of files. Valid values: on and of f . |
| BackendServerP ort | Integer | 80 | The backend port that is used by the SLB instance. |
| Description | String | test | The description of the HTTP listener. The description is 1 to 80 characters in length, and can contain letters, digits, hyphens (-), forward slashes (/), periods (.), and underscores ( ). _ |
| ForwardPort | Integer | 80 | The listener port that is used to redirect HTTP requests to HTTPS. Not e If the List enerForward parameter is set to of f , this parameter is not returned. |
| IdleTimeout | Integer | 2 | The timeout period of an idle connection. Unit: seconds. Valid values: 1 t o 60. Default value: 15. If no request is received within the specified timeout period, SLB closes the connection. When another request is received, SLB establishes a new connection. |
| ListenerForwar d | String | on | Indicates whether HTTP-to-HTTPS redirection is enabled. Valid values: on: enabled of f : disabled |
| MaxConnection | Integer | 10 | The maximum number of connections. |
| RequestId | String | 365F4154-92F6- 4AE4-92F8- 7FF34B540710 | The ID of the request. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestTimeou t | Integer | 34 | The timeout period of a request. Unit: seconds. Valid values: 1 t o 180. Default value: 60. If no response is received from a backend server within the request timeout period, SLB returns an HTTP 504 error code to the client. |
| SecurityStatus | String | on | The security status. Valid values: on and of f . |
| XForwardedFor SLBID _ | String | on | Indicates whether the SLB-ID header is used to retrieve the ID of the SLB instance. |
| XForwardedFor SLBIP _ | String | on | Indicates whether the SLB-IP header is used to retrieve client IP addresses. |
| XForwardedFor proto _ | String | on | Indicates whether the X-Forwarded- Proto header is used to retrieve the listener protocol. |

|   | Proto |
|---|---|

Examples Sample requests

```
http(s)://[Endpoint]/?Action=DescribeLoadBalancerHTTPListenerAttribute &ListenerPort=80 &LoadBalancerId=lb-bp1o94dp5********* &<Common request parameters>
```

Sample success responses `XML` format

```xml
<MaxConnection>10</MaxConnection> <CookieTimeout>500</CookieTimeout> <VServerGroupId>rsp-cige6j****</VServerGroupId> <Description>test</Description> <UnhealthyThreshold>4</UnhealthyThreshold> <HealthCheckURI>/test/index.html</HealthCheckURI> <Scheduler>wrr</Scheduler> <HealthCheck>on</HealthCheck> <IdleTimeout>2</IdleTimeout> <BackendServerPort>80</BackendServerPort> <XForwardedFor_SLBID>on</XForwardedFor_SLBID> <HealthCheckConnectPort>8080</HealthCheckConnectPort> <SecurityStatus>on</SecurityStatus> <Bandwidth>-1</Bandwidth> <Gzip>on</Gzip> <StickySessionType>insert </StickySessionType> <XForwardedFor_SLBIP>on</XForwardedFor_SLBIP> <HealthCheckHttpCode>http_2xx</HealthCheckHttpCode> <Cookie>B490B5EBF6F3CD402E515D22BCDA1598</Cookie> <Status>stopped</Status> <RequestTimeout>34</RequestTimeout> <ListenerPort>80</ListenerPort> <HealthCheckInterval>5</HealthCheckInterval> <RequestId>365F4154-92F6-4AE4-92F8-7FF34B540710</RequestId> <HealthCheckTimeout>3</HealthCheckTimeout> <ListenerForward>on</ListenerForward> <StickySession>on</StickySession> <ForwardPort>80</ForwardPort> <HealthyThreshold>4</HealthyThreshold> <XForwardedFor>on</XForwardedFor> <HealthCheckDomain>www.example.com</HealthCheckDomain> <XForwardedFor_proto>on</XForwardedFor_proto>
```

`JSON` format `{`

```json
    "MaxConnection": 10,
    "CookieTimeout": 500,
    "VServerGroupId": "rsp-cige6j****",
    "Description": "test",
    "UnhealthyThreshold": 4,
    "HealthCheckURI": "/test/index.html",
    "Scheduler": "wrr",
    "HealthCheck": "on",
    "IdleTimeout": 2,
    "BackendServerPort": 80,
    "XForwardedFor_SLBID": "on",
    "HealthCheckConnectPort": 8080,
    "SecurityStatus": "on",
    "Bandwidth": -1,
    "Gzip": "on",
    "StickySessionType": "insert",
    "XForwardedFor_SLBIP": "on",
    "HealthCheckHttpCode": "http_2xx",
    "Cookie": "B490B5EBF6F3CD402E515D22BCDA1598",
    "Status": "stopped",
    "RequestTimeout": 34,
    "ListenerPort": 80,
    "HealthCheckInterval": 5,
    "RequestId": "365F4154-92F6-4AE4-92F8-7FF34B540710",
    "HealthCheckTimeout": 3,
    "ListenerForward": "on",
    "StickySession": "on",
    "ForwardPort": 80,
    "HealthyThreshold": 4,
    "XForwardedFor": "on",
    "HealthCheckDomain": "www.example.com",
    "XForwardedFor_proto": "on"
```

`}`

#### 2.6.4 HTTPS listeners

##### 2.6.4.1 CreateLoadBalancerHTTPSListener

Creates an HTTPS listener. Not e Newly created listeners are in the Stopped state. After a listener is created, you must call the StartLoadBalancerListener operation to enable the listener to forward traffic. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateLoadBalan cerHTTPSListener | The operation that you want to perform. Set the value to Creat eLoadBalancerHT T PSList ener. |
| Bandwidth | Integer | Yes | -1 | The value that indicates the maximum bandwidth of the listener. Unit: Mbit/s. Valid values: -1 and 1 t o 5120. -1: For a pay-by-data-transfer Internet-facing Server Load Balancer (SLB) instance, you can set the value to -1. This indicates that the maximum bandwidth is not limited. 1 to 5120: For a pay-by-bandwidth Internet-facing SLB instance, you can specify a value as the maximum bandwidth for each listener. The sum of maximum bandwidth values that you set for all listeners cannot exceed the maximum bandwidth of the SLB instance. |
| HealthCheck | String | Yes | on | Specifies whether to enable health checks. Valid values: on and of f . |
| ListenerPort | Integer | Yes | 80 | The frontend port that is used by the SLB instance. Valid values: 1 t o 65535. |
| LoadBalancerId | String | Yes | lb- bp1o94dp5i6earr ***** | The ID of the SLB instance. |
| StickySession | String | Yes | on | Specifies whether to enable session persistence. Valid values: on and of f . |
| BackendServerPor t | Integer | No | 80 | The backend port that is used by the SLB instance. Valid values: 1 t o 65535. If the VServerGroupId parameter is not set, this parameter is required. |

| Parameter | Type | Required | Example | Description |   |   |
|---|---|---|---|---|---|---|
| XForwardedFor | String | No | on | Specifies whether to use the X- Forwarded-For header to obtain the real IP address of the client. Set the value to on. |   |   |
|   |   |   |   |   | X- |   |
| Scheduler | String | No | wrr | The scheduling algorithm. Valid values: wrr (default): Backend servers that have higher weights receive more requests than those that have lower weights. wlc: Requests are distributed based on the combination of the weights and number of connections to backend servers. If two backend servers have the same weight, the backend server that has fewer connections receives more requests. rr: Requests are distributed to backend servers in sequence. |   |   |
| StickySessionTyp e | String | No | insert | The method that is used to handle a cookie. If you set the StickySession parameter to on, you must specify this parameter. Valid values: insert and server. insert : inserts a cookie. SLB inserts a cookie (SERVERID) into the first HTTP or HTTPS response that is sent to a client. The next request from the client will contain this cookie, and the listener will distribute this request to the recorded backend server. server: rewrites a cookie. When the SLB instance detects a user-defined cookie, it rewrites the original cookie with the user-defined cookie. The next request from the client contains the user-defined cookie, and the listener distributes the request to the recorded backend server. |   |   |

|   | Forwarded-For |
|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| CookieTimeout | Integer | No | 500 | The timeout period of a cookie. Valid values: 1 t o 86400. Unit: seconds. Not e If you set the St ickySession parameter to on and the St ickySessionT ype parameter to insert , this parameter is required. |
| Cookie | String | No | B490B5EBF6F3CD4 02E515D22BCDA1 598 | The cookie to be configured on the backend server. The value must be 1 to 200 characters in length, and can contain only ASCII letters and digits. It cannot contain commas (,), semicolons (;), or spaces. It cannot start with a dollar sign ($). Not e If you set the St ickySession parameter to on and the St ickySessionT ype parameter to server, this parameter is required. |
| HealthCheckDom ain | String | No | 172.16.**. ** | The domain name that is used for health checks. Valid values: $ ip: The private IP address of the _ backend server. If you do not set this parameter or set the parameter to $ ip, the SLB instance uses the _ private IP address of each backend server as the domain name for health checks. domain: The domain name must be 1 to 80 characters in length. It can contain only letters, digits, periods (.), and hyphens (-). Not e This parameter takes effect only when the Healt hCheck parameter is set to on. |

| Parameter |   | Type | Required |   | Example | Description |   |   |
|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   | The URL that is used for health checks. The value must be 1 to 80 characters in length, and can contain only letters, digits, hyphens (-), forward |   |   |
|   |   |   |   |   |   |   | hyphens (-), forward |   |
|   |   |   |   |   |   | slashes (/), periods (.), %? |   |   |
|   |   |   |   |   |   | number signs (#), and ampersands |   |   |
|   |   |   |   |   |   | (&) |   |   |
| HealthCheckURI |   | String | No |   | /test/index.html |   |   |   |
| HealthyThreshold |   | Integer | No |   | 4 | The number of consecutive health check successes required before a backend server is declared healthy (from f ail to success). Valid values: 2 t o 10. Not e This parameter takes effect only when the Healt hCheck parameter is set to on. |   |   |
| UnhealthyThresh old |   | Integer | No |   | 4 | The number of consecutive health check failures required before a backend server is declared unhealthy (from success to f ail). Valid values: 2 t o 10. Not e This parameter takes effect only when the Healt hCheck parameter is set to on. |   |   |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| HealthCheckTime out | Integer | No | 3 | The timeout period for a health check response. If a backend Elastic Compute Service (ECS) instance does not respond within the specified time period, the health check fails. This parameter takes effect only when the Healt hCheck parameter is set to on. Valid values: 1 t o 300. Unit: seconds. If the value of the Healt hCHeckT imeout parameter is smaller than that of the Healt hCheckInt erval parameter, the value of the Healt hCHeckT imeout parameter is ignored and the value of the Healt hCheckInt erval parameter is regarded as the waiting period. Not e This parameter takes effect only when the Healt hCheck parameter is set to on. |
| HealthCheckConn ectPort | Integer | No | 8080 | The port that is used for health checks. Valid values: 1 t o 65535. Not e This parameter takes effect only when the Healt hCheck parameter is set to on. |
| HealthCheckInterv al | Integer | No | 5 | The interval between two consecutive health checks. Valid values: 1 t o 50 . Unit: seconds. Not e This parameter takes effect only when the Healt hCheck parameter is set to on. |

| Parameter | Type | Required | Example | Description |   |   |
|---|---|---|---|---|---|---|
| HealthCheckHttpC ode | String | No | http 2xx _ | The HTTP status code that indicates a successful health check. Separate multiple HTTP status codes with commas (,). Default value: ht t p 2xx. _ Valid values: ht t p 2xx, ht t p 3xx, _ _ ht t p 4xx, and ht t p 5xx. _ _ Not e This parameter takes effect only when the Healt hCheck parameter is set to on. |   |   |
| ServerCertificateI d | String | No | idkp-123-cn-test- 01** | The ID of the server certificate. |   |   |
| VServerGroupId | String | No | rsp- cige6j5e7p***** | The ID of the vServer group. |   |   |
| CACertificateId | String | No | 139a00604ad-cn- east-hangzh***** | The ID of the CA certificate. Two-factor authentication: uploads a CA certificate and a server certificate. Single-factor authentication: uploads only a server certificate. |   |   |
| XForwardedFor S _ LBIP | String | No | on | Specifies whether to use the SLB- IP header to obtain the real IP address of the client. Valid values: on and of f . Default value: off. |   |   |
| XForwardedFor S _ LBID | String | No | on | Specifies whether to use the SLB- ID header to obtain the ID of the SLB instance. Valid values: on and of f . Default value: off. |   |   |
| XForwardedFor p _ roto | String | No | on | Specifies whether to use the X- Forwarded-Proto header to obtain the listener protocol of the SLB instance. Valid values: on and of f . Default value: off. |   |   |
|   |   |   |   |   | X- |   |

|   | IP |
|---|---|

|   | ID |
|---|---|

|   | Forwarded-Proto |
|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Gzip | String | No | on | Specifies whether to enable gzip compression to compress files of a specific type. Valid values: on and of f . Default value: off. |
| IdleTimeout | Integer | No | 12 | The timeout period of an idle connection. Valid values: 1 t o 60. Default value: 15. Unit: seconds. If no request is received during the specified timeout period, the SLB instance closes the connection. When another request is received, the SLB instance establishes a new connection. |
| RequestTimeout | Integer | No | 23 | The timeout period of a request. Valid values: 1 t o 180. Default value: 60. Unit: seconds. If no response is received from the backend server during the request timeout period, the SLB instance sends an HTTP 504 error code to the client. |
|   |   |   |   | You can specify the TLSCipherPolicy parameter only for a guaranteed- performance SLB instance. Each security policy includes TLS protocol versions and cipher suites available for HTTPS. The following security policies are supported. For more information about the differences, see Differences in TLS security policies. t ls cipher policy 1 0: _ _ _ _ Supported TLS versions: TLSv1.0, TLSv1.1, and TLSv1.2. Supported cipher suites: ECDHE- RSA-AES128-GCM-SHA256, ECDHE- RSA-AES256-GCM-SHA384, ECDHE- RSA-AES128-SHA256, ECDHE-RSA- AES256-SHA384, AES128-GCM- SHA256, AES256-GCM-SHA384, AES128-SHA256, AES256-SHA256, ECDHE-RSA-AES128-SHA, ECDHE- RSA-AES256-SHA, AES128-SHA, AES256-SHA, and DES-CBC3-SHA. |

| Parameter | Type | Required | Example | t ls cipher policy 1 1: Descri_ption _ _ _ Supported TLS versions: TLSv1.1 |
|---|---|---|---|---|
| TLSCipherPolicy | String | No | tls cipher policy _ _ _ 1 1 _ | and TLSv1.2. Supported cipher suites: ECDHE- RSA-AES128-GCM-SHA256, ECDHE- RSA-AES256-GCM-SHA384, ECDHE- RSA-AES128-SHA256, ECDHE-RSA- AES256-SHA384, AES128-GCM- SHA256, AES256-GCM-SHA384, AES128-SHA256, AES256-SHA256, ECDHE-RSA-AES128-SHA, ECDHE- RSA-AES256-SHA, AES128-SHA, AES256-SHA, and DES-CBC3-SHA. |
|   |   |   |   | t ls cipher policy 1 2 _ _ _ _ Supported TLS version: TLSv1.2. Supported cipher suites: ECDHE- RSA-AES128-GCM-SHA256, ECDHE- RSA-AES256-GCM-SHA384, ECDHE- RSA-AES128-SHA256, ECDHE-RSA- AES256-SHA384, AES128-GCM- SHA256, AES256-GCM-SHA384, AES128-SHA256, AES256-SHA256, ECDHE-RSA-AES128-SHA, ECDHE- RSA-AES256-SHA, AES128-SHA, AES256-SHA, and DES-CBC3-SHA. t ls cipher policy 1 2 st rict _ _ _ _ _ Supported TLS version: TLSv1.2. Supported cipher suites: ECDHE- RSA-AES128-GCM-SHA256, ECDHE- RSA-AES256-GCM-SHA384, ECDHE- RSA-AES128-SHA256, ECDHE-RSA- AES256-SHA384, ECDHE-RSA- AES128-SHA, and ECDHE-RSA- AES256-SHA. |
| Description | String | No | CreateListeners | The description of the listener. The description must be 1 to 80 characters in length, and can contain Chinese characters, letters, digits, hyphens (-), forward slashes (/), periods (.), and underscores ( ). _ |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | CEF72CEB-54B6- 4AE8-B225- F876FF7BA984 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/? Action=CreateLoadBalancerHTTPSListener &Bandwidth=-1 &HealthCheck=on &ListenerPort=80 &LoadBalancerId=lb-bp1o94dp5i6earr***** &StickySession=on &<Common request parameters>
```

Sample success responses `XML` format

```xml
<CreateLoadBalancerHTTPSListenerResponse>
   <RequestId>CEF72CEB-54B6-4AE8-B225-F876FF7BA984</RequestId>
</CreateLoadBalancerHTTPSListenerResponse>
```

`JSON` format

```json
{"RequestId":" CEF72CEB-54B6-4AE8-B225-F876FF7BA984"
```

`}`

##### 2.6.4.2 SetLoadBalancerHTTPSListenerAttribute

Modifies the configurations of an HTTPS listener. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | SetLoadBalancer HTTPSListenerAtt ribute | The operation that you want to perform. Set the value to Set LoadBalancerHT T PSList enerAt t ribut e. |
| ListenerPort | Integer | Yes | 80 | The frontend port that is used by the Server Load Balancer (SLB) instance. Valid values: 1 t o 65535. |
| LoadBalancerId | String | Yes | lb- sjhfdji************* *** | The ID of the SLB instance. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Bandwidth | Integer | No | -1 | Specify the maximum bandwidth of the listener. Valid values: 1 t o 5120 and -1. -1: If you set the value to -1, it indicates that the maximum bandwidth is unlimited. 1 t o 5120: If you set the value to a number from 1 to 5120, the number that you specify indicates the maximum bandwidth of the listener. The sum of maximum bandwidth values of all listeners cannot exceed the maximum bandwidth of the SLB instance. |
| XForwardedFor | String | No | on | Specifies whether to use the X- Forwarded-For header to obtain the real IP address of the client. Valid values: on and of f . |
| Scheduler | String | No | wrr | The scheduling algorithm. Valid values: wrr (default): Backend servers that have higher weights receive more requests than those that have lower weights. wlc: Requests are distributed based on the combination of the weights and number of connections to backend servers. If two backend servers have the same weight, the backend server that has fewer connections receives more requests. rr: Requests are distributed to backend servers in sequence. |
| StickySession | String | No | on | Specifies whether to enable session persistence. Valid values: on and of f . |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| StickySessionTyp e | String | No | insert | The method that is used to handle a cookie. Valid values: insert : inserts a cookie. SLB inserts a cookie (ServerId) into the first HTTP or HTTPS response that is sent to a client. The next request from the client will contain this cookie, and the listener will distribute this request to the recorded backend server. server: rewrites a cookie. When SLB detects a user-defined cookie, it overwrites the original cookie with the user-defined cookie. The next request from the client will contain the user-defined cookie, and the listener will distribute the request to the recorded backend server. Not e If you set the St ickySession parameter to on, you must specify a value for this parameter. |
| CookieTimeout | Integer | No | 500 | The timeout period of a cookie. Valid values: 1 t o 86400. Unit: seconds. Not e If you set the St ickySession parameter to on and the St ickySessionT ype parameter to insert , this parameter is required. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Cookie | String | No | B490B5EBF6F3CD4 02E515D22BCDA1 598 | The cookie to be configured on the backend server. The value must be 1 to 200 characters in length, and can contain only ASCII characters and digits. It cannot contain commas (,), semicolons (;), or spaces. It cannot start with a dollar sign ($). Not e If you set the St ickySession parameter to on and the St ickySessionT ype parameter to server, this parameter is required. |
| HealthCheck | String | No | on | Specifies whether to enable health checks. Valid values: on and of f . |
| HealthCheckDom ain | String | No | 172.16.**. ** | The domain name that is used for health checks. Valid values: $ ip: The private IP address of the _ backend server. If the $ ip _ parameter is set or the HealthCheckDomain parameter is not set, SLB uses the private IP addresses of backend servers as the domain names for health checks. domain: The domain name must be 1 to 80 characters in length. It can contain only letters, digits, periods (.), and hyphens (-). Not e This parameter takes effect only when the Healt hCheck parameter is set to on. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| HealthCheckURI | String | No | /test/index.html | The URL that is used for health checks. The value must be 1 to 80 characters in length, and can contain letters, digits, hyphens (-), forward slashes (/), periods (.), percent signs (%), question marks (?), number signs (#), ampersands (&), and semicolons (;). The URL must not be a single forward slash (/) and it must start with a forward slash (/). Not e This parameter takes effect only when the Healt hCheck parameter is set to on. |
| HealthyThreshold | Integer | No | 4 | Specifies the number of consecutive health check successes required before a backend server is declared healthy (from f ail to success). Valid values: 2 t o 10. Not e This parameter takes effect only when the Healt hCheck parameter is set to on. |
| UnhealthyThresh old | Integer | No | 4 | Specifies the number of consecutive health check failures required before a backend server is declared unhealthy (from success to f ail). Valid values: 2 t o 10. Not e This parameter takes effect only when the Healt hCheck parameter is set to on. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| HealthCheckTime out | Integer | No | 3 | The timeout period for a health check response. If the backend Elastic Compute Service (ECS) instance does not send an expected response within the specified period of time, the health check fails. Valid values: 1 t o 300. Unit: seconds. Not e If the value of the Healt hCheckT imeout parameter is smaller than that of the Healt hCheckInt erval parameter, the value of the Healt hCheckT imeout parameter is ignored and the value of the Healt hCheckInt erval parameter is regarded the timeout period. This parameter takes effect only when the Healt hCheck parameter is set to on. |
| HealthCheckInterv al | Integer | No | 5 | The interval between two consecutive health checks. Valid values: 1 t o 50. Unit: seconds. Not e This parameter takes effect only when the Healt hCheck parameter is set to on. |
| HealthCheckConn ectPort | Integer | No | 8080 | The port that is used for health checks. Valid values: 1 t o 65535. Not e This parameter takes effect only when the Healt hCheck parameter is set to on. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| HealthCheckHttpC ode | String | No | http 2xx,http 3x _ _ x | The HTTP status code that indicates a successful health check. Separate multiple HTTP status codes with commas (,). Valid values: ht t p 2xx, ht t p 3xx, _ _ ht t p 4xx, and ht t p 5xx. _ _ Not e This parameter takes effect only when the Healt hCheck parameter is set to on. |
| ServerCertificateI d | String | No | idkp-123-cn- te****** | The ID of the server certificate. |
| CACertificateId | String | No | 139a00604ad-cn- east-******** | The ID of the CA certificate. If both the CA certificate and the server certificate are uploaded, two- factor authentication is used. If you upload only the server certificate, single-factor authentication is used. |
| VServerGroup | String | No | on | Specifies whether to use a vServer group. Valid values: on and of f . |
| VServerGroupId | String | No | rsp-cige6j******* | The ID of the vServer group. |
| Tags | String | No | loadbalancerhttp s**** | The tags. |
| XForwardedFor S _ LBIP | String | No | on | Specifies whether to use the SLB- IP header to obtain the real IP address of the client. Valid values: on and of f . |
| XForwardedFor S _ LBID | String | No | on | Specifies whether to use the SLB- ID header to obtain the ID of the SLB instance. Valid values: on and of f . |

|   | IP |
|---|---|

|   | ID |
|---|---|

|   | Parameter | Type | Required | Example | Description |   |   |
|---|---|---|---|---|---|---|---|
|   | XForwardedFor p _ roto | String | No | on | Specifies whether to use the X- Forwarded-Proto header to obtain the listener protocol of the SLB instance. Valid values: on and of f . |   |   |
|   |   |   |   |   |   | X- |   |
|   | Gzip | String | No | on | Specifies whether to enable gzip compression to compress files of a specific type. Valid values: on and of f . |   |   |
|   | IdleTimeout | Integer | No | 23 | The timeout period of an idle connection. Unit: seconds. Valid values: 1 t o 60. Default value: 15. If no request is received during the specified timeout period, the SLB instance closes the connection. When another request is received, the SLB instance establishes a new connection. |   |   |
|   | RequestTimeout | Integer | No | 223 | The timeout period of a request. Unit: seconds. Valid values: 1 t o 180. Default value: 60. If no response is received from the backend server during the request timeout period, SLB sends an HTTP 504 error code to the client. |   |   |
|   |   |   |   |   | You can specify the TLSCipherPolicy parameter only for a guaranteed- performance SLB instance. Each security policy includes TLS protocol versions and cipher suites that are available for HTTPS. You can select a security policy based on your requirements. The following security policies are supported: t ls cipher policy 1 0: _ _ _ _ Supported TLS versions: TLSv1.0, TLSv1.1, and TLSv1.2. |   |   |

|   | Forwarded-Proto |
|---|---|

| Parameter | Type | Required | Example | Supported cipher suites: ECDHE- Description RSA-AES128-GCM-SHA256, ECDHE- |
|---|---|---|---|---|
|   |   |   |   | RSA-AES256-GCM-SHA384, ECDHE- RSA-AES128-SHA256, ECDHE-RSA- AES256-SHA384, AES128-GCM- SHA256, AES256-GCM-SHA384, AES128-SHA256, AES256-SHA256, |
| TLSCipherPolicy | String | No | tls cipher policy _ _ _ 1 2 _ | ECDHE-RSA-AES128-SHA, ECDHE- RSA-AES256-SHA, AES128-SHA, AES256-SHA, and DES-CBC3-SHA. t ls cipher policy 1 1: _ _ _ _ Supported TLS versions: TLSv1.1 and TLSv1.2. Supported cipher suites: ECDHE- RSA-AES128-GCM-SHA256, ECDHE- RSA-AES256-GCM-SHA384, ECDHE- RSA-AES128-SHA256, ECDHE-RSA- AES256-SHA384, AES128-GCM- SHA256, AES256-GCM-SHA384, AES128-SHA256, AES256-SHA256, ECDHE-RSA-AES128-SHA, ECDHE- RSA-AES256-SHA, AES128-SHA, AES256-SHA, and DES-CBC3-SHA. t ls cipher policy 1 2 _ _ _ _ Supported TLS version: TLSv1.2. Supported cipher suites: ECDHE- RSA-AES128-GCM-SHA256, ECDHE- RSA-AES256-GCM-SHA384, ECDHE- RSA-AES128-SHA256, ECDHE-RSA- AES256-SHA384, AES128-GCM- SHA256, AES256-GCM-SHA384, AES128-SHA256, AES256-SHA256, ECDHE-RSA-AES128-SHA, ECDHE- RSA-AES256-SHA, AES128-SHA, AES256-SHA, and DES-CBC3-SHA. t ls cipher policy 1 2 st rict _ _ _ _ _ Supported TLS version: TLSv1.2. Supported cipher suites: ECDHE- RSA-AES128-GCM-SHA256, ECDHE- RSA-AES256-GCM-SHA384, ECDHE- RSA-AES128-SHA256, ECDHE-RSA- AES256-SHA384, ECDHE-RSA- AES128-SHA, and ECDHE-RSA- AES256-SHA. |

|   | Parameter | Type |   | Required | Example |   | Description |   |
|---|---|---|---|---|---|---|---|---|
|   | Description | String |   | No | ListenerDescriptio n |   | The description of the listener. The description must be 2 to 256 characters in length. It can contain Chinese characters and special characters in the following string: ^ |   |
|   |   |   |   |   |   |   |   | ^ |
|   |   |   |   |   |   |   | ( [ ^ \ x 0 0 - \ x f f ] \| [ \ |   |
|   |   |   |   |   |   |   | w . , ; / @ - ] ) { 2 , 2 5 6 } |   |
|   |   |   |   |   |   |   | $ |   |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | CEF72CEB-54B6- 4AE8-B225- F876FF7BA984 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/? Action=SetLoadBalancerHTTPSListenerAttribute &ListenerPort=80 &LoadBalancerId=lb-sjhfdji**************** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<SetLoadBalancerHTTPSListenerAttributeResponse>
    <RequestId>CEF72CEB-54B6-4AE8-B225-F876FF7BA984</RequestId>
</SetLoadBalancerHTTPSListenerAttributeResponse>
```

`JSON` format `{`

```json
 "RequestId":" CEF72CEB-54B6-4AE8-B225-F876FF7BA984"
```

`}`

##### 2.6.4.3 DescribeLoadBalancerHTTPSListenerAttribute

Queries the configurations of an HTTPS listener. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeLoadBala ncerHTTPSListene rAttribute | The operation that you want to perform. Set the value to DescribeLoadBalancerHT T PSList en erAt t ribut e. |
| ListenerPort | Integer | Yes | 80 | The frontend port that is used by the Server Load Balancer (SLB) instance. Valid values: 1 t o 65535. |
| LoadBalancerId | String | Yes | lb- bp1mxu5r8lau*** **** | The ID of the SLB instance. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| ListenerPort | Integer | 80 | The frontend port that is used by the SLB instance. |
| BackendServerP ort | Integer | 80 | The backend port that is used by the SLB instance. |
| Bandwidth | Integer | -1 | The maximum bandwidth of the listener. |
| Status | String | stopped | The state of the listener. Valid Values: running and st opped. |
| XForwardedFor | String | on | Indicates whether the X-Forwarded-For header is used to identify the real IP address of a client. Valid values: on and of f . |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Scheduler | String | wrr | The scheduling algorithm. Valid values: wrr, wlc, and rr. wrr (default): Backend servers that have higher weights receive more requests than those that have lower weights. wlc: Requests are distributed based on the combination of the weights and number of connections to backend servers. If two backend servers have the same weight, the backend server that has fewer connections receives more requests. rr: Requests are distributed to backend servers in sequence. |
| StickySession | String | on | Indicates whether session persistence is enabled. Valid values: on and of f . |

| Parameter | Type | Example | Description |
|---|---|---|---|
| StickySessionTy pe | String | insert | The method that is used to handle a cookie. If the StickySession parameter is set to on, this parameter is required. Valid values: insert and server. insert : inserts a cookie. SLB inserts a cookie (SERVERID) into the first HTTP or HTTPS response that is sent to a client. The next request from the client will contain this cookie, and the listener will distribute this request to the recorded backend server. server: rewrites a cookie. When SLB detects a user-defined cookie, it overwrites the original cookie with the user-defined cookie. The next request from the client will contain the user- defined cookie, and the listener will distribute the request to the recorded backend server. Not e If you set the St ickySession parameter to on, this parameter is required. |
| CookieTimeout | Integer | 500 | The timeout period of a cookie. |
| Cookie | String | B490B5EBF6F3CD402 E515D22BCDA1598 | The cookie that is configured on the backend server. |
| HealthCheck | String | on | Indicates whether health checks are enabled. Valid values: on and of f . |
| HealthCheckDo main | String | www.test.com | The domain name that is used for health checks. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| HealthCheckURI | String | /test/index.html | The URL that is used for health checks. The value must be 1 to 80 characters in length, and can contain letters, digits, hyphens (-), forward slashes (/), periods (.), percent signs (%), question marks (?), number signs (#), and ampersands (&). The URL must not be a single forward slash (/) but it must start with a forward slash (/). |
| HealthyThresho ld | Integer | 4 | The healthy threshold. |
| UnhealthyThres hold | Integer | 4 | The unhealthy threshold. |
| HealthCheckTi meout | Integer | 3 | The timeout period of each health check response. Unit: seconds. |
| HealthCheckInt erval | Integer | 5 | The interval between two consecutive health checks. Unit: seconds. Valid values: 1 t o 50. Unit: seconds. |
| HealthCheckHtt pCode | String | http 2xx _ | The HTTP status code that indicates a successful health check. Multiple status codes are separated with commas (,). Valid values: ht t p 2xx (default), ht t p 3xx, _ _ ht t p 4xx, and ht t p 5xx. _ _ |
| HealthCheckCo nnectPort | Integer | 8080 | The port that is used for health checks. Not e This parameter takes effect only when the Healt hCheck parameter is set to on. |
| ServerCertificat eId | String | idkp-123-cn-test- 0** | The ID of the server certificate. |
| CACertificateId | String | idkp-234-cn-test- 0** | The ID of the CA certificate. |
| VServerGroupId | String | rsp-cige6j5e******** | The ID of the associated vServer group. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Gzip | String | on | Indicates whether gzip compression is enabled. Valid values: on and of f . |
| Description | String | ListenerDescription | The description of the listener. The description must be 2 to 256 characters in length. It can contain only Chinese characters and special characters in the following string: /^([^\x00-\xff]\|[\w.,;/@-]){2,256}$/. |
| IdleTimeout | Integer | 23 | The timeout period of an idle connection. Unit: seconds. Valid values: 1 to 60. Default value: 15. If no request is received during the specified timeout period, the SLB instance closes the connection. When another request is received, the SLB instance establishes a new connection. |
| MaxConnection | Integer | 10 |   |
| RequestId | String | 365F4154-92F6- 4AE4-92F8- 7FF34B540710 | The ID of the request. |
| RequestTimeou t | Integer | 43 | The timeout period of a request. Unit: seconds. Valid values: 1 to 180. Default value: 60. If the backend server does not respond within the specified timeout period, the SLB instance returns an HTTP 504 error code to the client. |
| SecurityStatus | String | on | The security status. Valid values: on and of f . |
|   |   |   | The security policy. You can specify the TLSCipherPolicy parameter only for a guaranteed-performance SLB instance. Each security policy offers different TLS protocol versions and cipher suites for HTTPS. |

| Developer Guide·AP | I reference |   | Server Load Balance |
|---|---|---|---|
| Parameter | Type | Example | The following security policies are Description supported. For more information about the |
| TLSCipherPolicy | String | tls cipher policy 1 _ _ _ _ 0 | differences, see Differences in TLS security policies. You can specify a security policy based on your requirements. Valid values: t ls cipher policy 1 0: _ _ _ _ Supported TLS versions: TLSv1.0, TLSv1.1, and TLSv1.2. Supported cipher suites: ECDHE-RSA- AES128-GCM-SHA256, ECDHE-RSA-AES256- GCM-SHA384, ECDHE-RSA-AES128-SHA256, ECDHE-RSA-AES256-SHA384, AES128-GCM- SHA256, AES256-GCM-SHA384, AES128- SHA256, AES256-SHA256, ECDHE-RSA- AES128-SHA, ECDHE-RSA-AES256-SHA, AES128-SHA, AES256-SHA, and DES-CBC3- SHA. t ls cipher policy 1 1: _ _ _ _ Supported TLS versions: TLSv1.1 and TLSv1.2. Supported cipher suites: ECDHE-RSA- AES128-GCM-SHA256, ECDHE-RSA-AES256- GCM-SHA384, ECDHE-RSA-AES128-SHA256, ECDHE-RSA-AES256-SHA384, AES128-GCM- SHA256, AES256-GCM-SHA384, AES128- SHA256, AES256-SHA256, ECDHE-RSA- AES128-SHA, ECDHE-RSA-AES256-SHA, AES128-SHA, AES256-SHA, and DES-CBC3- SHA. t ls cipher policy 1 2 _ _ _ _ Supported TLS version: TLSv1.2. Supported cipher suites: ECDHE-RSA- AES128-GCM-SHA256, ECDHE-RSA-AES256- GCM-SHA384, ECDHE-RSA-AES128-SHA256, ECDHE-RSA-AES256-SHA384, AES128-GCM- SHA256, AES256-GCM-SHA384, AES128- SHA256, AES256-SHA256, ECDHE-RSA- AES128-SHA, ECDHE-RSA-AES256-SHA, AES128-SHA, AES256-SHA, and DES-CBC3- SHA. t ls cipher policy 1 2 st rict _ _ _ _ _ Supported TLS version: TLSv1.2. Supported cipher suites: ECDHE-RSA- AES128-GCM-SHA256, ECDHE-RSA-AES256- GCM-SHA384, ECDHE-RSA-AES128-SHA256, ECDHE-RSA-AES256-SHA384, ECDHE-RSA- AES128-SHA, and ECDHE-RSA-AES256-SHA. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| XForwardedFor SLBID _ | String | on | Indicates whether the SLB-ID header is used to obtain the ID of the SLB instance. Valid values: on and of f . |
| XForwardedFor SLBIP _ | String | on | Indicates whether the SLB-IP header is used to obtain the real IP address of the client. Valid values: on and of f . |
| XForwardedFor proto _ | String | on | Indicates whether the X-Forwarded- Proto header is used to obtain the listener protocol of the SLB instance. Valid values: on and of f . |

|   | Proto |
|---|---|

Examples Sample requests

```
http(s)://[Endpoint]/? Action=DescribeLoadBalancerHTTPSListenerAttribute &ListenerPort=80 &LoadBalancerId=lb-bp1mxu5r8lau******* &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeLoadBalancerHTTPSListenerAttributeResponse>
   <RequestId>11F52428-64ED-40F7-98C2-DBB6D0BB0AD7</RequestId>
      <HealthCheckHttpCode>http_2xx,http_3xx</HealthCheckHttpCode>
      <HealthCheckTimeout>5</HealthCheckTimeout>
      <ServerCertificateId>1231579xxxxxxxx_15dbf6ff26f_1991415478_2054196746</ServerCertifi
cateId>
      <XForwardedFor_SLBID>off</XForwardedFor_SLBID>
      <Gzip>on</Gzip>
      <HealthyThreshold>3</HealthyThreshold>
      <Scheduler>wrr</Scheduler>
      <StickySession>off</StickySession>
      <UnhealthyThreshold>3</UnhealthyThreshold>
      <XForwardedFor_SLBIP>off</XForwardedFor_SLBIP>
      <XForwardedFor_proto>off</XForwardedFor_proto>
      <Bandwidth>-1</Bandwidth>
      <HealthCheckURI>/</HealthCheckURI>
      <VServerGroupId>rsp-0xiju72x******</VServerGroupId>
      <HealthCheck>on</HealthCheck>
      <ListenerPort>443</ListenerPort>
      <Status>running</Status>
      <XForwardedFor>on</XForwardedFor>
      <HealthCheckDomain></HealthCheckDomain>
      <HealthCheckInterval>2</HealthCheckInterval>
      <BackendServerPort>443</BackendServerPort>
</DescribeLoadBalancerHTTPSListenerAttributeResponse>
```

`JSON` format `{`

```json
    "RequestId": "11F52428-64ED-40F7-98C2-DBB6D0BB0AD7",
    "HealthCheckHttpCode": "http_2xx,http_3xx",
    "HealthCheckTimeout": 5,
    "ServerCertificateId": "1231579xxxxxxxx_15dbf6ff26f_1991415478_2054196746",
    "XForwardedFor_SLBID": "off",
    "Gzip": "on",
    "HealthyThreshold": 3,
    "Scheduler": "wrr",
    "StickySession": "off",
    "UnhealthyThreshold": 3,
    "XForwardedFor_SLBIP": "off",
    "XForwardedFor_proto": "off",
    "Bandwidth": -1,
    "HealthCheckURI": "/",
    "VServerGroupId": "rsp-0xiju72x******",
    "HealthCheck": "on",
    "ListenerPort": 443,
    "Status": "running",
    "XForwardedFor": "on",
    "HealthCheckDomain": "",
    "HealthCheckInterval": 2,
    "BackendServerPort": 443
```

`}`

##### 2.6.4.4 DescribeHealthStatus

Queries the health status of backend servers. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeHealthSt atus | The operation that you want to perform. Set the value to DescribeHealt hSt at us. |
| LoadBalancerId | String | Yes | lb- bp1qjwo61pqz3a h**** | The ID of the Server Load Balancer (SLB) instance. |
| ListenerPort | Integer | No | 80 | The frontend port that is used by the SLB instance. Valid values: 1 t o 65535. Not e If you do not specify this parameter, the health status of all ports is returned. |
| access key id _ _ | String | No | ack- hp34s2h0xx1ht4n wo**** | The AccessKey ID. |
| Tags | String | No | null | The key and value of the tag. |
| RegionId | String | Yes | cn-hangzhou | The ID of the region where the SLB instance is deployed. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| BackendServers | Array of BackendServer |   | The list of backend servers. |
| BackendServer |   |   |   |
| ServerId | String | i- bp1h5u3fv54ytf**** | The ID of the Elastic Compute Service (ECS) instance or elastic network interface (ENI). |

| Developer Guide·AP | I reference |   | Server Load Balance |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| ServerHealthSt atus | String | abnormal | The health status of the backend server. Valid values: normal: The backend server is healthy. abnormal: The backend server is unhealthy. unavailable: The health check is not completed. |
| ListenerPort | Integer | 80 | The frontend port that is used by the SLB instance. |
| port | Integer | 80 | The listening port. Valid values: 1 t o 65535. |
| RequestId | String | 365F4154-92F6- 4AE4-92F8- 7FF34B540710 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=DescribeHealthStatus &LoadBalancerId=lb-bp1qjwo61pqz3ah**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeHealthStatusResponse>
  <RequestId>E69BA4CE-2B55-45EC-94CA-E47B16759459</RequestId>
  <BackendServers>
        <BackendServer>
              <ListenerPort>80</ListenerPort>
              <ServerId>i-bp1h5u3fv54ytf0******</ServerId>
              <Port>80</Port>
              <ServerIp>192.168.0.**</ServerIp>
              <ServerHealthStatus>abnormal</ServerHealthStatus>
              <Protocol>http</Protocol>
        </BackendServer>
        <BackendServer>
              <ListenerPort>8080</ListenerPort>
              <ServerId>i-bp1h5u3fv54ytf0******</ServerId>
              <Port>80</Port>
              <ServerIp>192.168.0.**</ServerIp>
              <ServerHealthStatus>abnormal</ServerHealthStatus>
              <Protocol>tcp</Protocol>
        </BackendServer>
  </BackendServers>
</DescribeHealthStatusResponse>
```

`JSON` format `{`

```json
    "RequestId": "E69BA4CE-2B55-45EC-94CA-E47B16759459",
    "BackendServers": {
        "BackendServer": [
```

`{`

```json
                "ListenerPort": 80,
                "ServerId": "i-bp1h5u3fv54ytf*****",
                "Port": 80,
                "ServerIp": "192.168.**.**",
                "ServerHealthStatus": "abnormal",
                "Protocol": "http"
```

`},` `{`

```json
                "ListenerPort": 8080,
                "ServerId": "i-bp1h5u3fv54ytf0******",
                "Port": 80,
                "ServerIp": "192.168.**.**",
                "ServerHealthStatus": "abnormal",
                "Protocol": "tcp"
```

`}` `]` `}` `}`

#### 2.6.5 Access control

##### 2.6.5.1 SetListenerAccessControlStatus

Enables or disables the whitelist of a specified listener. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | SetListenerAcces sControlStatus | The operation that you want to perform. Set the value to Set List enerAccessCont rolSt at us. |
| AccessControlSta tus | String | Yes | open white list _ _ | Specifies whether to enable the whitelist. Valid values: open whit e list : enables the _ _ whitelist. close: disables the whitelist. Not e After the whitelist is enabled, if no IP address is added to the whitelist, Server Load Balancer (SLB) instance cannot distribute network traffic. |
| ListenerPort | Integer | Yes | 80 | The frontend port that is used by the SLB instance. Valid values: 1 t o 65535. |
| LoadBalancerId | String | Yes | lb- bp1b6c719dfa08 ex***** | The ID of the SLB instance. |
| access key id _ _ | String | No | acc- hp34s2h0xx1ht4n wo**** | The AccessKey ID. |
| Tags | String | No | {"tagKey":"Key1", "tagValue":"Valu e1"} | The key and value of the tag. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | CEF72CEB-54B6- 4AE8-B225- F876FF7BA984 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/? Action=SetListenerAccessControlStatus &AccessControlStatus=open_white_list &ListenerPort=80 &LoadBalancerId=lb-bp1b6c719dfa08ex***** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<SetListenerAccessControlStatusResponse>
    <RequestId>CEF72CEB-54B6-4AE8-B225-F876FF7BA984</RequestId>
</SetListenerAccessControlStatusResponse>
```

`JSON` format

```json
{"RequestId":" CEF72CEB-54B6-4AE8-B225-F876FF7BA984"}
```

##### 2.6.5.2 DescribeListenerAccessControlAttribute

Queries the information about the whitelist of a listener. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeListenerA ccessControlAttri bute | The operation that you want to perform. Set the value to DescribeList enerAccessCont rolAt t r ibut e. |
| ListenerPort | Integer | Yes | 80 | The frontend port that is used by the Server Load Balancer (SLB) instance. Valid values: 1 t o 65535. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| LoadBalancerId | String | Yes | lb- 8vb86hxixo8****** *6jaz | The ID of the SLB instance. |
| Tags | String | No | listeneraccesscon trolslb**** | The tags. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| AccessControlS tatus | String | open white list _ _ | Indicates whether the whitelist is enabled. Valid values: open whit e list : the whitelist is _ _ enabled. close: the whitelist is disabled. |
| SourceItems | String | 192.168.0.1 | The IP addresses or CIDR blocks that are added to the whitelist. |
| RequestId | String | 365F4154-92F6- 4AE4-92F8- 7FF34B540710 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/? Action=DescribeListenerAccessControlAttribute &ListenerPort=80 &LoadBalancerId=lb-8vb86hxixo8*******6jaz &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeListenerAccessControlAttributeResponse>
   <RequestId>365F4154-92F6-4AE4-92F8-7FF34B540710</RequestId>
   <AccessControlStatus>open_white_list</AccessControlStatus>
   <SourceItems>192.168.0.1</SourceItems>
</DescribeListenerAccessControlAttributeResponse>
```

`JSON` format

```json
{"AccessControlStatus":"open_white_list", "RequestId":"365F4154-92F6-4AE4-92F8-7FF34B540710", "SourceItems":"192.168.0.1"}
```

##### 2.6.5.3 AddListenerWhiteListItem

Adds an IP address to the whitelist of a specified listener. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | AddListenerWhite ListItem | The operation that you want to perform. Set the value to AddList enerWhit eList It em. |
| ListenerPort | Integer | Yes | 80 | The frontend port that is used by the Server Load Balancer (SLB) instance. Valid values: 1 t o 65535. |
| LoadBalancerId | String | Yes | 139a00604ad-cn- east-hangzhou- 01 | The ID of the SLB instance. |
| SourceItems | String | Yes | 1.1.1.1,1.1.1.0/21 | The access control list. This parameter takes effect only when AccessCont rolSt at us of the listener is set to open whit e list . _ _ Separate multiple IP addresses or CIDR blocks with commas (,). You cannot enter 0.0.0.0 or 0.0.0.0/0. You can call the SetListenerAccessControlStatus operation to set the value of the AccessControlStatus parameter to close. This indicates that access control is disabled. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | CEF72CEB-54B6- 4AE8-B225- F876FF7BA984 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/? Action=AddListenerWhiteListItem &ListenerPort=80 &LoadBalancerId=139a00604ad-cn-east-hangzhou-01 &SourceItems=1.1.1.1,1.1.1.0/21 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<AddListenerWhiteListItemResponse>
  <RequestId>CEF72CEB-54B6-4AE8-B225-F876FF7BA984</RequestId>
</AddListenerWhiteListItemResponse>
```

`JSON` format

```json
{"RequestId":"CEF72CEB-54B6-4AE8-B225-F876FF7BA984"}
```

##### 2.6.5.4 RemoveListenerWhiteListItem

Removes IP addresses from the whitelist of a listener. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | RemoveListenerW hiteListItem | The operation that you want to perform. Set the value to RemoveList enerWhit eList It em. |
| ListenerPort | Integer | Yes | 80 | The listening port. Valid values: 1 t o 65535. |
| LoadBalancerId | String | Yes | lb- bp1b6c719dfa08 ex***** | The ID of the Server Load Balancer (SLB) instance. |
| SourceItems | String | Yes | 192.168.0.1/24 | The IP addresses or CIDR blocks to be removed. Separate multiple IP addresses or CIDR blocks with commas (,). Not e If all of the IP addresses in the whitelist are removed, the listener no longer forwards requests. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | CEF72CEB-54B6- 4AE8-B225- F876FF7BA984 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/? Action=RemoveListenerWhiteListItem &ListenerPort=80 &LoadBalancerId=lb-bp1b6c719dfa08ex***** &SourceItems=192.168.0.1 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RemoveListenerWhiteListItemResponse>
    <RequestId>CEF72CEB-54B6-4AE8-B225-F876FF7BA984</RequestId>
</RemoveListenerWhiteListItemResponse>
```

`JSON` format

```json
{"RequestId":" CEF72CEB-54B6-4AE8-B225-F876FF7BA984"}
```

#### 2.6.6 Forwarding rules

##### 2.6.6.1 CreateRules

Creates forwarding rules for a specified HTTP or HTTPS listener. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateRules | The operation that you want to perform. Set the value to Creat eRules. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| ListenerPort | Integer | Yes | 443 | The port on which the Server Load Balancer (SLB) instance listens. Valid values: 1 t o 65535. |
| LoadBalancerId | String | Yes | lb- bp1ca0zt07t934 w****** | The ID of the SLB instance. |
| RegionId | String | Yes | cn-east- hangzhou-01 | The ID of the region where the SLB instance is created. You can call the DescribeRegions operation to query region IDs. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| RuleList | String | Yes | [{"RuleName":"Ru le2","Domain":"te st.com","VServer GroupId":"rsp- bp114ni******"}] | The forwarding rules to be added. A maximum of 10 forwarding rules can be added in each request. Each forwarding rule contains the following parameters: RuleName: Required. The value must be of the STRING type. The name of the forwarding rule. The name must be 1 to 40 characters in length, and can contain only letters, digits, hyphens (-), forward slashes (/), periods (.), and underscores ( ). _ Forwarding rule names must be unique within each listener. Domain: Optional. The value must be of the STRING type. The domain name to be associated with the forwarding rule. You must specify this parameter or Url. URL: Optional. The value must be of the STRING type. The URL must be 1 to 80 characters in length, and can contain only letters, digits, hyphens (-), forward slashes (/), periods (.), percent signs (%), question marks (?), number signs (#), and ampersands (&). The URL must not be a single forward slash (/). However, it must start with a forward slash (/). You must specify the URL or Domain. VServerGroupId: Required. The value must be of the STRING type. The ID of the destination vServer group to be specified in the forwarding rule. You must specify the domain name or URL. You can also specify both. The combination of domain name and URL must be unique within a listener. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| Rules | Array of Rule |   | The list of forwarding rules. |
| Rule |   |   |   |

| Developer Guide·AP | I reference |   | Server Load Balance |
|---|---|---|---|
| Parameter | Type | Example | Description |
| RuleId | String | rule-bp12jzy0***** | The ID of the forwarding rule. |
| RuleName | String | Rule2 | The name of the forwarding rule. |
| RequestId | String | 9DEC9C28-AB05- 4DDF-9A78- 6B08EC9CE18C | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/? Action=CreateRules &ListenerPort=443 &LoadBalancerId=lb-bp1ca0zt07t934w****** &RegionId=cn-east-hangzhou-01 &RuleList=[{"RuleName":"Rule2","Domain":"test.com","VServerGroupId":"rsp-bp114ni******"}] &<Common request parameters>
```

Sample success responses `XML` format

```xml
<CreateRulesResponse>
   <RequestId>D63E42FB-F963-4EE5-9B32-05602BF351F3</RequestId>
   <Rules>
      <Rule>
         <RuleId>rule-bp12jzy******</RuleId>
         <RuleName>Rule3</RuleName>
      </Rule>
   </Rules>
</CreateRulesResponse>
```

`JSON` format `{`

```json
    "RequestId": "D63E42FB-F963-4EE5-9B32-05602BF351F3",
    "Rules": {
        "Rule": [
```

`{`

```json
                "RuleId": "rule-bp12jzy******",
                "RuleName": "Rule3"
```

`}` `]` `}` `}`

##### 2.6.6.2 DeleteRules

Deletes forwarding rules. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteRules | The operation that you want to perform. Set the value to Delet eRules. |
| RegionId | String | Yes | cn-east- hangzhou-01 | The ID of the region where the Server Load Balancer (SLB) instance is created. You can call the DescribeRegions operation to query region IDs. |
| RuleIds | String | Yes | ["rule- bp1z9ce******","r ule- bp1tuc******4"] | The list of forwarding rules that you want to delete. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 9DEC9C28-AB05- 4DDF-9A78- 6B08EC9CE18C | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/? Action=DeleteRules &RegionId=cn-east-hangzhou-01 &RuleIds=["rule-bp1z9ce******","rule-bp1tuc******4"] &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DeleteRulesResponse>
      <RequestId>9DEC9C28-AB05-4DDF-9A78-6B08EC9CE18C</RequestId>
</DeleteRulesResponse>
```

`JSON` format

```json
{"RequestId":"9DEC9C28-AB05-4DDF-9A78-6B08EC9CE18C"}
```

##### 2.6.6.3 DescribeRules

Queries forwarding rules that are configured for a specified listener. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeRules | The operation that you want to perform. Set the value to DescribeRules. |
| ListenerPort | Integer | Yes | 90 | The frontend listener port that is used by the Server Load Balancer (SLB) instance. Valid values: 1 t o 65535. |
| LoadBalancerId | String | Yes | lb- bp1ca0zt07t934* ***** | The ID of the SLB instance. |
| RegionId | String | Yes | cn-east- hangzhou-01 | The ID of the region where the SLB instance is created. You can call the DescribeRegions operation to query region IDs. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 9DEC9C28-AB05- 4DDF-9A78- 6B08EC9CE18C | The ID of the request. |
| Rules | Array of Rule |   | The list of forwarding rules. |
| Rule |   |   |   |
| RuleId | String | rule-tybqi6****** | The ID of the forwarding rule. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RuleName | String | Rule2 | The name of the forwarding rule. The name must be 1 to 80 characters in length and can contain only letters, digits, hyphens (-), forward slashes (/), periods (.), and underscores ( ). _ Not e Forwarding rule names must be unique within each listener. |
| Domain | String | test.com | The request domain name specified in the forwarding rule. |
| Url | String | /cache | The request URL specified in the forwarding rule. |
| VServerGroupId | String | rsp-6cejjzl****** | The ID of the destination vServer group specified in the forwarding rule. |

Examples Sample requests

```
http(s)://[Endpoint]/? Action=DescribeRules &ListenerPort=90 &LoadBalancerId=lb-bp1ca0zt07t934****** &RegionId=cn-east-hangzhou-01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeRulesResponse>
   <RequestId>11D87D83-741B-4F8A-8AAD-FD6867FDE7B2</RequestId>
   <Rules>
      <Rule>
         <Url>/image</Url>
         <Domain>example.com</Domain>
         <VServerGroupId>rsp-bp114ni*****</VServerGroupId>
         <RuleId>rule-bp1supb******</RuleId>
         <RuleName>auto_named_rule</RuleName>
         <ListenerSync>on</ListenerSync>
      </Rule>
      <Rule>
         <Domain>test.com</Domain>
         <VServerGroupId>rsp-bp114nim******</VServerGroupId>
         <RuleId>rule-bp1efem*****</RuleId>
         <RuleName>Rule2</RuleName>
         <ListenerSync>on</ListenerSync>
      </Rule>
      <Rule>
         <Domain>test2.com</Domain>
         <VServerGroupId>rsp-bp114n******</VServerGroupId>
         <RuleId>rule-bp12jz******</RuleId>
         <RuleName>Rule3</RuleName>
         <ListenerSync>on</ListenerSync>
      </Rule>
   </Rules>
</DescribeRulesResponse>
```

`JSON` format `{`

```json
    "RequestId": "11D87D83-741B-4F8A-8AAD-FD6867FDE7B2",
    "Rules": {
        "Rule": [
```

`{`

```json
                "Url": "/image",
                "Domain": "example.com",
                "VServerGroupId": "rsp-bp114ni******",
                "RuleId": "rule-bp1supbx*****",
                "RuleName": "auto_named_rule",
                "ListenerSync": "on"
```

`},` `{`

```json
                "Domain": "test.com",
                "VServerGroupId": "rsp-bp114ni******",
                "RuleId": "rule-bp1efemp****",
                "RuleName": "Rule2",
                "ListenerSync": "on"
```

`},` `{`

```json
                "Domain": "test2.com",
                "VServerGroupId": "rsp-bp114ni******",
                "RuleId": "rule-bp12jzy*******",
                "RuleName": "Rule3",
                "ListenerSync": "on"
```

`}` `]` `}` `}`

##### 2.6.6.4 SetRule

Modifies the forwarding rule of a specified vServer group. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | SetRule | The operation that you want to perform. Set the value to Set Rule. |
| RegionId | String | Yes | cn-east- hangzhou-01 | The ID of the region where the Server Load Balancer (SLB) instance is created. You can call the DescribeRegions operation to query region IDs. |
| RuleId | String | Yes | rule-tybqi6****** | The ID of the forwarding rule. |

| Developer Guide·API r | eference |   |   | Server Load Balance |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| VServerGroupId | String | Yes | rsp-cige6****** | The ID of the vServer group with which the forwarding rule is associated. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 9DEC9C28-AB05- 4DDF-9A78- 6B08EC9CE18C | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/? Action=SetRule &RegionId=cn-east-hangzhou-01 &RuleId=rule-tybqi6****** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<SetRuleResponse>
      <RequestId>9DEC9C28-AB05-4DDF-9A78-6B08EC9CE18C</RequestId>
</SetRuleResponse>
```

`JSON` format

```json
{"RequestId":"9DEC9C28-AB05-4DDF-9A78-6B08EC9CE18C"}
```

##### 2.6.6.5 DescribeRuleAttribute

Queries the configurations of a specified forwarding rule. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeRuleAttri bute | The operation that you want to perform. Set the value to DescribeRuleAt t ribut e. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| RegionId | String | Yes | cn-east- hangzhou-01 | The ID of the region where the Server Load Balancer (SLB) instance is created. You can call the DescribeRegions operation to query region IDs. |
| RuleId | String | Yes | rule- bp1efemp9suk5* *** | The ID of the forwarding rule. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RuleName | String | Rule1 | The name of the forwarding rule. |
| LoadBalancerId | String | lb- bp1ca0zt07t934wxe zyxo**** | The ID of the SLB instance. |
| ListenerPort | String | 90 | The port on which the SLB instance listens. |
| Domain | String | test.com | The domain name that is configured in the forwarding rule. |
| Url | String | /cache | The URL that is configured in the forwarding rule. |
| VServerGroupId | String | rsp-cige6j5e7p**** | The ID of the vServer group that is associated with the forwarding rule. |
| RequestId | String | 9DEC9C28-AB05- 4DDF-9A78- 6B08EC9CE18C | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/? Action=DescribeRuleAttribute &RegionId=cn-east-hangzhou-01 &RuleId=rule-bp1efemp9suk5**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeRuleAttributeResponse>
   <Domain>test.com</Domain>
   <VServerGroupId>rsp-bp114nimo4kl9****</VServerGroupId>
   <LoadBalancerId>lb-bp1ca0zt07t934wxezyxo****</LoadBalancerId>
   <RuleName>Rule1</RuleName>
   <ListenerPort>90</ListenerPort>
   <RequestId>DB3C28EE-9A6C-4FFA-8759-4ED8346A675E</RequestId>
   <ListenerSync>on</ListenerSync>
</DescribeRuleAttributeResponse>
```

`JSON` format

```json
{"ListenerPort":"90","VServerGroupId":"rsp-cige6j5e7p****","RequestId":"9DEC9C28-AB05-4DDF- 9A78-6B08EC9CE18C","LoadBalancerId":"lb-bp1ca0zt07t934wxezyxo****","Domain":"test.com","Rul eName":"Rule1","Url":"/cache"}
```

#### 2.6.7 DeleteLoadBalancerListener

Deletes a listener. Not e You can delete only listeners that are in the st opped or running state. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteLoadBalan cerListener | The operation that you want to perform. Set the value to Delet eLoadBalancerList ener. |
| ListenerPort | Integer | Yes | 80 | The frontend port that is used by the Server Load Balancer (SLB) instance. Valid values: 1 t o 65535. |
| LoadBalancerId | String | Yes | lb- bp13jaf5qli5xm** ****** | The ID of the SLB instance. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | CEF72CEB-54B6- 4AE8-B225- F876FF7BA984 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/? Action=DeleteLoadBalancerListener &ListenerPort=80 &LoadBalancerId=lb-bp13jaf5qli5xm******** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DeleteLoadBalancerListenerResponse>
     <RequestId>791D8B68-AE0F-4174-AF54-088C8B3C5D54</RequestId>
  </DeleteLoadBalancerListenerResponse>
```

`JSON` format `{`

```json
    "RequestId": "791D8B68-AE0F-4174-AF54-088C8B3C5D54"
```

`}`

#### 2.6.8 StopLoadBalancerListener

Disables a listener. When you call this operation, take note of the following items: If the operation is successful, the listener switches to the Stopped state. You cannot call the operation when the Server Load Balancer (SLB) instance to which the listener belongs is in the Locked state. Not e After a listener is disabled, it stops forwarding requests to the associated backend servers. This may cause service interruption. Proceed with caution. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | StopLoadBalance rListener | The operation that you want to perform. Set the value to St opLoadBalancerList ener. |
| ListenerPort | Integer | Yes | 80 | The frontend port that is used by the SLB instance. Valid values: 1 to 65535. |
| LoadBalancerId | String | Yes | lb- bp13jaf5qli5xmgl ****** | The ID of the SLB instance. |
| Tags | String | No | {"tagKey":"Key1", "tagValue":"Valu e1"} | The key and value of the tag. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | CEF72CEB-54B6- 4AE8-B225- F876FF7BA984 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/? Action=StopLoadBalancerListener &ListenerPort=80 &LoadBalancerId=lb-bp13jaf5qli5xmgl****** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<StopLoadBalancerListenerResponse>
     <RequestId>21D2B318-650E-4B0B-A3B5-693D462247B3</RequestId>
  </StopLoadBalancerListenerResponse>
```

`JSON` format `{`

```json
    "RequestId": "21D2B318-650E-4B0B-A3B5-693D462247B3"
```

`}`

#### 2.6.9 StartLoadBalancerListener

Starts a listener. When you call this operation, take note of the following items: You can call the operation only when the listener is in the Stopped state. If the operation is successful, the state of the listener changes to Starting. You cannot call the operation when the Server Load Balancer (SLB) instance to which the listener belongs is in the Locked state. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | StartLoadBalance rListener | The operation that you want to perform. Set the value to St art LoadBalancerList ener. |
| ListenerPort | Integer | Yes | 80 | The frontend port that is used by the SLB instance. Valid values: 1 to 65535. |
| LoadBalancerId | String | Yes | lb- bp13jaf5qli5***** **** | The ID of the SLB instance. |
| Tags | String | No | {"tagKey":"Key1", "tagValue":"Valu e1"} | The key and value of the tag. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | CEF72CEB-54B6- 4AE8-B225- F876FF7BA984 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/? Action=StartLoadBalancerListener &ListenerPort=80 &LoadBalancerId=lb-bp13jaf5qli5********* &<Common request parameters>
```

Sample success responses `XML` format

```xml
<StartLoadBalancerListenerResponse>
     <RequestId>CC000321-00F2-49B8-9BCA-60D822414960</RequestId>
  </StartLoadBalancerListenerResponse>
```

`JSON` format `{`

```json
    "RequestId": "CC000321-00F2-49B8-9BCA-60D822414960"
```

`}`

### 2.7 Server certificates

#### 2.7.1 UploadServerCertificate

Uploads a server certificate. You can upload only one server certificate and its private key in each request. The request is successful only when the server certificate and its private key are both uploaded. If the server certificate or its private key is not uploaded, the request fails. After a server certificate and its private key are uploaded, the fingerprints of all server certificates that belong to your account are returned. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | UploadServerCert ificate | The operation that you want to perform. Set the value to UploadServerCert if icat e. |
| RegionId | String | Yes | cn-east- hangzhou-01 | The ID of the region where the server certificate is created. You can call the DescribeRegions operation to query region IDs. |
| AliCloudCertificat eId | String | No | 730912673****** _ 15d97e7709a 71 _ 445759hr 7892*** _ *** | The ID of the server certificate that is issued by Apsara Stack SSL Certificates Service. This parameter is required if you use a server certificate that is issued by Apsara Stack SSL Certificates Service. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| AliCloudCertificat eName | String | No | testcertkey | The name of the server certificate that is issued by Apsara Stack SSL Certificates Service. |
| ServerCertificate | String | No | test | The public key certificate that you want to upload. Not e This parameter is required if you use a server certificate that is issued by a third- party certificate authority (CA). |
| PrivateKey | String | No | wmsa***** | The private key of the server certificate that you want to upload. Not e This parameter is required if you use a server certificate that is issued by a third- party CA. |
| ServerCertificateN ame | String | No | mycert01 | The name of the server certificate that you want to upload. The name must be 1 to 80 characters in length. It must start with a letter or Chinese character. It can contain digits, periods (.), underscores ( ), and _ hyphens (-). |
| Tags | String | No | ServerCertificate* **** | The tag that you want to add to the server certificate. |
| StandardType | String | No | ServerCertificate | The type of the server certificate. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| ServerCertificat eId | String | xxxxidkp-123-cn- test****** | The ID of the server certificate. |
| ServerCertificat eName | String | mycert01 | The name of the server certificate. |

| Developer Guide·AP | I reference |   | Server Load Balance |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| Fingerprint | String | 01:DF:AB:** | The fingerprint of the server certificate. |
| AliCloudCertific ateId | String | 730912xxxxx 15d97 _ e7709a 71445759hr _ 7******* _ | The ID of the server certificate if the server certificate is issued by Apsara Stack SSL Certificates Service. |
| AliCloudCertific ateName | String | testcert*** | The name of the server certificate if the server certificate is issued by Apsara Stack SSL Certificates Service. |
| IsAliCloudCertifi cate | Integer | 0 | Indicates whether the server certificate is issued by Apsara Stack SSL Certificates Service. Valid values: 0: The server certificate is issued by a third-party CA. 1: The server certificate is issued by Apsara Stack SSL Certificates Service. |
| RegionId | String | cn-east-hangzhou- 01 | The ID of the region where the server certificate is created. |
| RegionIdAlias | String | hangzhou |   |
| RequestId | String | 365F4154-92F6- 4AE4-92F8- 7FF34B540710 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/? Action=UploadServerCertificate &RegionId=cn-east-hangzhou-01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<UploadServerCertificateResponse>
  <RegionIdAlias>cn-east-hangzhou-01</RegionIdAlias>
  <Fingerprint>01:DF:AB:**</Fingerprint>
  <AliCloudCertificateName>testcert***</AliCloudCertificateName>
  <RequestId>365F4154-92F6-4AE4-92F8-7FF34B540710</RequestId>
  <IsAliCloudCertificate>0</IsAliCloudCertificate>
  <ServerCertificateId>xxxxidkp-123-cn-test******</ServerCertificateId>
  <ServerCertificateName>mycert01</ServerCertificateName>
  <RegionId>cn-hangzhou</RegionId>
  <AliCloudCertificateId>730912xxxxx_15d97e7709a_71445759hr_7*******</AliCloudCertificateId
```

`>`

```
</UploadServerCertificateResponse>
```

`JSON` format

```json
{"RegionIdAlias":"cn-east-hangzhou-01","Fingerprint":"01:DF:AB:**","AliCloudCertificateName ":"testcert***","RequestId":"365F4154-92F6-4AE4-92F8-7FF34B540710","IsAliCloudCertificate": "0","ServerCertificateId":"xxxxidkp-123-cn-test******","ServerCertificateName":"mycert01"," RegionId":"cn-hangzhou","AliCloudCertificateId":"730912xxxxx_15d97e7709a_71445759hr_7****** *"}
```

#### 2.7.2 DeleteServerCertificate

Deletes a server certificate. Not e You cannot delete a server certificate that is in use. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteServerCerti ficate | The operation that you want to perform. Set the value to Delet eServerCert if icat e. |
| ServerCertificateI d | String | Yes | 123157****** 166 _ f8204689 171476 _ 3408 7099******* _ | The ID of the server certificate. |
| RegionId | String | Yes | cn-east- hangzhou-01 | The ID of the region where the Server Load Balancer (SLB) instance is created. You can call the DescribeRegions operation to query region IDs. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | CEF72CEB-54B6- 4AE8-B225- F876FF7BA984 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/? Action=DeleteServerCertificate &ServerCertificateId=123157******_166f8204689_1714763408_7099******* &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DeleteServerCertificateResponse>
    <RequestId>CEF72CEB-54B6-4AE8-B225-F876FF7BA984</RequestId></DeleteServerCertificateRes
ponse>
```

`JSON` format `{`

```json
"RequestId":" CEF72CEB-54B6-4AE8-B225-F876FF7BA984"
```

`}`

#### 2.7.3 DescribeServerCertificates

Queries a server certificate. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeServerCer tificate | The operation that you want to perform. Set the value to DescribeServerCert if icat es. |
| ServerCertificateI d | String | Yes | 12315790****** * _ *****204689 1714 _ 763408 7099814 _ 30 | The ID of the server certificate. |
| RegionId | String | Yes | cn-east- hangzhou-01 | The ID of the region where the Server Load Balancer (SLB) instance is deployed. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| Fingerprint | String | 68:08:1a:f8:2c:97:6 9:a3:**:**:**:**:4b: ca:4f:5d:ee:a5:ef:0 d | The fingerprint of the server certificate. |
| RegionId | String | cn-ease-hangzhou- 01 | The ID of the region where the SLB instance is created. You can call the DescribeRegions operation to query region IDs. |
| RegionIdAlias | String | cn-hangzhou | The name of the region where the server certificate is created. |
| RequestId | String | 365F4154-92F6- 4AE4-92F8- 7FF34B540710 | The ID of the request. |
| ServerCertificat eId | String | 123157****** ******4 _ 689 1714763408 70 _ _ 9981430-cn-east- hangzhou-02 | The ID of the server certificate. |
| ServerCertificat eName | String | slb | The name of the server certificate. |
| StandardType | String | ServerCertificate | The type of the server certificate. |

Examples Sample requests

```
http(s)://[Endpoint]/? Action=DescribeServerCertificate &ServerCertificateId=12315790******_******204689_1714763408_709981430 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeServerCertificateResponse>
  <RegionIdAlias>cn-hangzhou</RegionIdAlias>
  <Fingerprint>68:08:1a:f8:2c:97:69:a3:**:**:**:**:4b:ca:4f:5d:ee:a5:ef:0d</Fingerprint>
  <RequestId>365F4154-92F6-4AE4-92F8-7FF34B540710</RequestId>
  <ServerCertificateName>slb</ServerCertificateName>
  <ServerCertificateId>123157******_******4689_1714763408_709981430-cn-east-hangzhou-02</Se
rverCertificateId>
  <RegionId>cn-ease-hangzhou-01</RegionId>
  <StandardType>ServerCertificate</StandardType>
</DescribeServerCertificateResponse>
```

`JSON` format

```json
{"RegionIdAlias":"cn-hangzhou", "Fingerprint":"68:08:1a:f8:2c:97:69:a3:**:**:**:**:4b:ca:4f:5d:ee:a5:ef:0d", "RequestId":"365F4154-92F6-4AE4-92F8-7FF34B540710", "ServerCertificateName":"slb", "ServerCertificateId":"123157******_******4689_1714763408_709981430-cn-east-hangzhou-02", "RegionId":"cn-ease-hangzhou-01", "StandardType":"ServerCertificate"}
```

#### 2.7.4 SetServerCertificateName

Sets the name of a server certificate. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | SetServerCertifica teName | The operation that you want to perform. Set the value to Set ServerCert if icat eName. |
| RegionId | String | Yes | cn-east- hangzhou-01 | The ID of the region where the Server Load Balancer (SLB) instance is created. You can call the DescribeRegions operation to query region IDs. |
| ServerCertificateI d | String | Yes | 139a*******-cn- east-hangzhou- 01 | The ID of the server certificate. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| ServerCertificateN ame | String | Yes | slb- servercertificate- cn-east- hangzhou***** | The name of the server certificate. The name must be 1 to 80 characters in length. It must start with letters or Chinese characters. It can contain letters, digits, periods (.), underscores ( ), and hyphens (-). _ |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | CEF72CEB-54B6- 4AE8-B225- F876FE7BA984 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/? Action=SetServerCertificateName &RegionId=cn-east-hangzhou-01 &ServerCertificateId=139a*******-cn-east-hangzhou-01 &ServerCertificateName=slb-servercertificate-cn-east-hangzhou***** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<SetServerCertificateNameResponse>
      <RequestId>CEF72CEB-54B6-4AE8-B225-F876FE7BA984</RequestId>
</SetServerCertificateNameResponse>
```

`JSON` format

```json
{"RequestId":" CEF72CEB-54B6-4AE8-B225-F876FE7BA984"
```

`}`

#### 2.7.5 UploadCACertificate

Uploads a CA certificate. You can upload only one CA certificate in each call. After a CA certificate is uploaded, the ID, name, and fingerprint of the certificate are returned. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | UploadCACertific ate | The operation that you want to perform. Set the value to UploadCACert if icat e. |
| RegionId | String | Yes | cn-east- hangzhou-01 | The ID of the region where the Server Load Balancer (SLB) instance is created. You can call the DescribeRegions operation to query region IDs. |
| CACertificate | String | Yes | test | The CA certificate that you want to upload. |
| CACertificateNam e | String | No | mycacert01 | The name of the CA certificate. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| CACertificateId | String | 139a00604ad-cn- east-hangzh***** | The ID of the CA certificate. |
| CACertificateNa me | String | mycacert01 | The name of the CA certificate. |
| Fingerprint | String | 02:DF:AB:ED | The fingerprint of the CA certificate. |
| RequestId | String | 365F4154-92F6- 4AE4-92F8- 7FF34B540710 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/? Action=UploadCACertificate &RegionId=cn-east-hangzhou-01 &CACertificate=test &<Common request parameters>
```

Sample success responses `XML` format

```xml
<UploadCACertificateResponse>
  <Fingerprint>02:DF:AB:ED</Fingerprint>
  <RequestId>365F4154-92F6-4AE4-92F8-7FF34B540710</RequestId>
  <CACertificateId>139a00604ad-cn-east-hangzh*****</CACertificateId>
  <CACertificateName>mycacert01</CACertificateName>
</UploadCACertificateResponse>
```

`JSON` format

```json
{"Fingerprint":"02:DF:AB:ED","RequestId":"365F4154-92F6-4AE4-92F8-7FF34B540710","CACertific ateId":"139a00604ad-cn-east-hangzh*****","CACertificateName":"mycacert01"}
```

#### 2.7.6 DeleteCACertificate

Deletes a CA certificate. Not e You cannot delete a CA certificate that is being used. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteCACertifica te | The operation that you want to perform. Set the value to Delet eCACert if icat e. |
| RegionId | String | Yes | cn-east- hangzhou-01 | The ID of the region where the Server Load Balancer (SLB) instance is created. You can call the DescribeRegions operation to query region IDs. |
| CACertificateId | String | Yes | 123157908**** 1 _ 5c73d77203 - _ 986300114 - _ 2110544xxx | The ID of the CA certificate. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | CEF72CEB-54B6- 4AE8-B225- F876FF7BA984 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/? Action=DeleteCACertificate &RegionId=cn-east-hangzhou-01 &CACertificateId=123157908****_15c73d77203_-986300114_-2110544xxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DeleteCACertificateResponse>
         <RequestId>CEFxxxxx72CEB-54B6-4AE8-B225-F876FF7BA984</RequestId>
 </DeleteCACertificateResponse>
```

`JSON` format `{`

```json
    "RequestId": " CEFxxxx72CEB-54B6-4AE8-B225-F876FF7BA984"
```

`}`

#### 2.7.7 DescribeCACertificates

Queries CA certificates. Not e For security reasons, only fingerprints and names of the CA certificates are returned, the content of the CA certificates is not returned. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeCACertifi cates | The operation that you want to perform. Set the value to DescribeCACert if icat es. |
| RegionId | String | Yes | cn-east- hangzhou-01 | The region where the CA certificates are created. You can call the DescribeRegions operation to query region IDs. |
| CACertificateId | String | No | 139a006*****-cn- east-hangzhou- 02 | The ID of the CA certificate. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| CACertificates | Array of CACertificate |   | Information about the CA certificate. |
| CACertificate |   |   |   |
| CACertificateId | String | 139a006****-cn- east-hangzhou-02 | The ID of the CA certificate. |
| CACertificateNa me | String | test | The name of the CA certificate. |
| RegionId | String | cn-east-hangzhou- 01 | The region where the CA certificate is created. |
| Fingerprint | String | AC:BE:FD | The fingerprint of the CA certificate. |
| RequestId | String | 365F4154-92F6- 4AE4-92F8- 7FF34B540710 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/? Action=DescribeCACertificates &RegionId=cn-east-hangzhou-01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeCACertificateResponse>
  <RequestId>365F4154-92F6-4AE4-92F8-7FF34B540710</RequestId>
  <CACertificates>
        <CACertificateName>test</CACertificateName>
        <Fingerprint>AC:BE:FD</Fingerprint>
        <RegionId>cn-east-hangzhou-01</RegionId>
        <CACertificateId>139a006****-cn-east-hangzhou-02</CACertificateId>
  </CACertificates>
</DescribeCACertificateResponse>
```

`JSON` format

```json
{"RequestId":"365F4154-92F6-4AE4-92F8-7FF34B540710", "CACertificates":[
    {"CACertificateName":"test",
    "Fingerprint":"AC:BE:FD",
    "RegionId":"cn-east-hangzhou-01",
    "CACertificateId":"139a006****-cn-east-hangzhou-02"
```

`}` `]` `}`

#### 2.7.8 SetCACertificateName

Sets the name of a CA certificate. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | SetCACertificateN ame | The operation that you want to perform. Set the value to Set CACert if icat eName. |
| RegionId | String | Yes | cn-east- hangzhou-01 | The ID of the region where the Server Load Balancer (SLB) instance is created. You can call the DescribeRegions operation to query region IDs. |
| CACertificateId | String | Yes | 139a0******-cn- east-hangzhou- 01 | The ID of the CA certificate. |
| CACertificateNam e | String | Yes | mycacert02 | The name of the CA certificate. The name must be 1 to 80 characters in length. It must start with letters. It can contain letters, digits, periods (.), underscores ( ), and hyphens (-). _ |
| access key id _ _ | String | No | acc- hp34s2h0xx1ht4n wo**** | The AccessKey ID. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | CEF72CEB-54B6- 4AE8-B225- F876FE7BA984 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/? Action=SetCACertificateName &RegionId=cn-east-hangzhou-01 &CACertificateId=139a0******-cn-east-hangzhou-01 &CACertificateName=mycacert02 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<SetCACertificateNameResponse>
      <RequestId>CEF72CEB-54B6-4AE8-B225-F876FE7BA984</RequestId>
</SetCACertificateNameResponse>
```

`JSON` format

```json
{"RequestId":" CEF72CEB-54B6-4AE8-B225-F876FE7BA984"
```

`}`

### 2.8 Backend Servers

#### 2.8.1 AddBackendServers

Adds backend servers. Not e If multiple identical Elastic Compute Service (ECS) instances are specified in a request, only the first ECS instance is added. The other ECS instances are ignored. If the backend server that you add is identical to one of the existing backend servers that are associated with a listener, an error is reported. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | AddBackendServe rs | The operation that you want to perform. Set the value to AddBackendServers. |

| Parameter |   | Type | Required |   | Example |   | Description |   |   |   |
|---|---|---|---|---|---|---|---|---|---|---|
| LoadBalancerId |   | String | Yes |   | lb- 2ze7o5h52g02kk zz****** |   | The ID of the Server Load Balancer (SLB) instance. |   |   |   |
| BackendServers |   | String | Yes |   | [{ "ServerId": "eni- xxxxxxxxx", "Weight": "100", "Type": "eni", "ServerIp": "192.168. **. **", "Port":"80","Desc ription":"test- 112" },{ "ServerId": "eni- xxxxxxxxx", "Weight": "100", "Type": "eni", "ServerIp": "172.166. **. **", "Port":"80","Desc |   | The list of backend servers that you want to add to the SLB instance. The following parameters are used to specify the backend servers: ServerId: Required. Specify the instance ID of the backend server. The value is of the STRING type. You can specify the ID of an ECS instance or an elastic network interface (ENI). If ServerId is set to the ID of an ENI, the T ype parameter is required. Weight : The weight of the backend server. Valid values: 0 t o 100. Default value: 100. Not e The SLB instance does not forward requests to the backend server whose weight is set to 0. Descript ion: Optional. This value is of the STRING type. The description must be 1 to 80 characters in length, and can contain letters, digits, hyphens (-), forward slashes (/), periods (.), and underscores ( ). It _ can also contain Chinese characters. T ype: The type of the backend server. Valid values: ecs: an ECS instance. This is the default value. eni: an ENI. ServerIp: The IP address of the ECS instance or ENI. Examples: ECS instance: [{ "ServerId": "i |   |   |   |
|   |   |   |   |   |   |   |   |   | [{ "ServerId": "i |   |
|   |   |   |   |   |   | 172.166. **. **", Port":"80","Desc | -xxxxxxxxx", "Weight": "100", |   |   |   |
|   |   |   |   |   | ription":"test- |   | "Type": "ecs", "Port": "80", " |   |   |   |
|   |   |   |   |   | 113" }] |   | Description": "test-112" }]. |   |   |   |
|   |   |   |   |   |   |   | ENI: | [{ "ServerId": "eni-xxxx |   |   |
|   |   |   |   |   |   |   | xxxxx", "Weight": "100", "Type |   |   |   |

|   | Para | meter | Type |   | Required | Example |   | ": "eni", "ServerIp": "192.168 Description |   |
|---|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   |   | . **. **", "Port":"80","Descri |   |
|   |   |   |   |   |   |   |   | ption":"test-112" }] |   |
|   |   |   |   |   |   |   |   |   | [{ |
|   |   |   |   |   |   |   |   | "ServerId": "eni-xxxxxxxxx", " |   |
|   |   |   |   |   |   |   |   | Weight": "100", "Type": "eni", |   |
|   |   |   |   |   |   |   |   | "ServerIp": "192.168. **. **", |   |
|   |   |   |   |   |   |   |   | "Port":"80","Description":"tes |   |
|   |   |   |   |   |   |   |   | t-112" },{ "ServerId": "eni-xx |   |
|   |   |   |   |   |   |   |   | xxxxxxx", "Weight": "100", "Ty |   |
|   |   |   |   |   |   |   |   | pe": "eni", "ServerIp": "172.1 |   |
|   |   |   |   |   |   |   |   | 66. **. **", "Port":"80","Desc |   |
|   |   |   |   |   |   |   |   | ription":"test-113" }] |   |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| LoadBalancerId | String | lb- 2ze7o5h52g02kkzz* *** | The ID of the SLB instance. |
| BackendServers | Array of BackendServer |   | The list of backend servers. |
| BackendServer |   |   |   |
| ServerId | String | i- 2zej4lxhjoq1icu***** | The ID of the ECS instance or ENI. |
| Weight | String | 100 | The weight of the backend server. Valid values: 0 t o 100. Default value: 100. If the value is set to 0, the SLB instance does not forward requests to the backend server. |
| Description | String | BackendServer | The description of the backend server. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 34B82C81-F13B- 4EEB-99F6- A048C67CC830 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/? Action=AddBackendServers &LoadBalancerId=lb-2ze7o5h52g02kkzz****** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<AddBackendServersResponse>
    <BackendServers>
        <BackendServer>
            <ServerId>i-2zej4lxhjoq1icu*****</ServerId>
            <Weight>100</Weight>
            <Type>ecs</Type>
        </BackendServer>
        <BackendServer>
            <ServerId>i-2ze1u9ywulp5pbv*****</ServerId>
            <Weight>100</Weight>
            <Type>ecs</Type>
        </BackendServer>
    </BackendServers>
    <RequestId>34B82C81-F13B-4EEB-99F6-A048C67CC830</RequestId>
    <LoadBalancerId>lb-2ze7o5h52g02kkzz*****</LoadBalancerId>
</AddBackendServersResponse>
```

`JSON` format

```json
{"RequestId":"34B82C81-F13B-4EEB-99F6-A048C67CC830","LoadBalancerId":"lb-2ze7o5h52g02kkzz**
**","BackendServers":[{"ServerId":"i-2zej4lxhjoq1icu*****","Description":"BackendServer","V
pcId":"vpc-***","ServerIp":"172.168. *. *","Weight":"100"}]}
```

#### 2.8.2 RemoveBackendServers

Removes backend servers. Not e If the backend server that you want to remove does not belong to the specified Server Load Balancer (SLB) instance, the request fails. However, the system does not report an error. Request parameters

| Parameter |   | Type |   | Required | Example |   |   | Description |   |   |   |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Action |   | String |   | Yes | RemoveBackendS ervers |   |   | The operation that you want to perform. Set the value to RemoveBackendServers. |   |   |   |
| BackendServers |   | String |   | Yes | [{"ServerId":"i- 2zej4lxhjoq***", "Type": "ecs","Weight":"1 00"}] |   |   | The configurations of the backend server to be removed. Valid values: ServerId: Required. Specify the ID of the backend server. This parameter is of the STRING type. Weight : Required. Specify the weight of the backend server. This parameter is of the INTEGER type. Valid values: 0 t o 100. T ype: Specify the type of the backend server. Valid values: ecs: an Elastic Compute Service (ECS) instance (default) eni: an elastic network interface (ENI) Not e You can specify up to 20 backend servers in each request. Examples: Remove an ECS instance: [{"Serve |   |   |   |
|   |   |   |   |   |   |   |   |   |   | [{"Serve |   |
|   |   |   |   |   |   |   |   | rId":"i-2zej4lxhjoq***", "Type |   |   |   |
|   |   |   |   |   |   |   |   | ": "ecs","Weight":"100"}] |   |   |   |
|   |   |   |   |   |   |   |   | Remove an ENI: | [{"ServerId":"e |   |   |
|   |   |   |   |   |   |   |   | ni-2ze1sdp5***","Type": "eni", |   |   |   |
|   |   |   |   |   |   |   |   | "Weight":"100"}] |   |   |   |
| LoadBalancerId |   | String |   | Yes | lb- bp1qjwo61pqz3a hl***** |   |   | The ID of the SLB instance. |   |   |   |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| LoadBalancerId | String | lb- bp1vjkb671z53****** * | The ID of the SLB instance. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| BackendServers | Array of BackendServer |   | The list of backend servers. |
| BackendServer |   |   |   |
| ServerId | String | i-jjgjgjgggd****** | The ID of the backend server. |
| Weight | Integer | 100 | The weight of the backend server. Valid values: 0 t o 100. |
| RequestId | String | 365F4154-92F6- 4AE4-92F8- 7FF34B540710 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/? Action=RemoveBackendServers &BackendServers=[{"ServerId":"i-2zej4lxhjoq***", "Type": "ecs","Weight":"100"}] &LoadBalancerId=lb-bp1qjwo61pqz3ahl***** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RemoveBackendServersResponse>
  <RequestId>365F4154-92F6-4AE4-92F8-7FF34B540710</RequestId>
  <LoadBalancerId>lb-bp1vjkb671z53cy******</LoadBalancerId>
  <BackendServers>
        <BackendServer>
              <ServerId>i-jjgjgjg*****</ServerId>
              <Weight>100</Weight>
        </BackendServer>
        <BackendServer>
              <ServerId>i-jjgjgituitu****</ServerId>
              <Weight>100</Weight>
        </BackendServer>
  </BackendServers>
</RemoveBackendServersResponse>
```

`JSON` format `{`

```json
    "RemoveBackendServers": {
        "RequestId": "365F4154-92F6-4AE4-92F8-7FF34B540710",
        "LoadBalancerId": "lb-bp1vjkb671z53cy******",
        "BackendServers": {
            "BackendServer": [
```

`{`

```json
                    "ServerId": "i-jjgjgjg*****",
                    "Weight": 100
```

`},` `{`

```json
                    "ServerId": "i-jjgjgituitu****",
                    "Weight": 100
```

`}` `]` `}` `}` `}`

#### 2.8.3 SetBackendServers

Sets the weights of backend servers. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | SetBackendServer s | The operation that you want to perform. Set the value to Set BackendServers. |
| LoadBalancerId | String | Yes | lb- bp1qjwo61pqz3a ****** | The ID of the Server Load Balancer (SLB) instance. |
|   |   |   |   | The list of backend servers that you want to add to the SLB instance. The value of this parameter must be of the STRING type and in the JSON format. You can specify up to 20 elements in each request. ServerId: Required. Specify the ID of the backend server. This parameter is of the STRING type. Port : Required. Specify the port that is used by the backend server. This parameter is of the INTEGER type. Valid values: 1 to 65535. Weight : Required. Specify the |

|   | Parameter |   |   | Type |   | Required |   | Example |   |   | weight of the backend server. This Description parameter is of the INTEGER type. |   |   |   |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   |   |   |   |   | Valid values: 0 to 100. Descript ion: Optional. The |   |   |   |   |
|   | BackendServers |   |   | String |   | Yes |   | [{ "ServerId": "i- xxxxxxxxx", "Weight": "100", "Type": "ecs", "Port":"80","Desc ription":"test- 112" }] |   |   | description of the backend server. This parameter is of the STRING type. The description must be 1 to 80 characters in length, and can contain letters, digits, hyphens (-), forward slashes (/), periods (.), and underscores ( ). It can also contain _ Chinese characters. T ype: The instance type of the backend server. This parameter is of the STRING type. Valid values: ecs (default): an Elastic Compute Service (ECS) instance eni: an elastic network interface (ENI) ServerIp: the IP address of an ECS instance or ENI. Examples: ECS instance: [{ "ServerId": "i |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   | [{ "ServerId": "i |   |   |
|   |   |   |   |   |   |   |   |   |   |   | -xxxxxxxxx", "Weight": "100", |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | "Type": "ecs", "Port": "80", " |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | Description": "test-112" }]. |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | ENI: | [{ "ServerId": "eni-xxxx |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | xxxxx", "Weight": "100", "Type |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | ": "eni", "ServerIp": "192.168 |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | . **. **", "Port":"80","Descri |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | ption":"test-112" }] |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   | [{ |   |
|   |   |   |   |   |   |   |   |   |   |   | "ServerId": "eni-xxxxxxxxx", " |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | Weight": "100", "Type": "eni", |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | "ServerIp": "192.168. **. **", |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | "Port":"80","Description":"tes |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | t-112" },{ "ServerId": "eni-xx |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | xxxxxxx", "Weight": "100", "Ty |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | pe": "eni", "ServerIp": "172.1 |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | 66. **. **", "Port":"80","Desc |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | ription":"test-113" }] |   |   |   |   |

| Parameter |   | Type | Required |   | Example |   |   | Description |   |
|---|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   |   | Not e The backend servers |   |
| Response parameters |   |   |   |   |   |   |   | that you add to an SLB instance must be in the Running state. You |   |
| Parameter | Type |   |   | Example |   | Descri |   | can add up to 20 backend servers pttioon an SLB instance in each request. |   |
| LoadBalancerId | String |   |   | lb- bp1qjwo61pqz3a*** *** |   | The ID |   | In addition, you can specify ENIs as backend servers for only ogf utahrea SnLteBe inds-tpaenrcfoe.rmance SLB instances. |   |
| BackendServers | Array of BackendServer |   |   |   |   | The list of backend servers. |   |   |   |
| BackendServer |   |   |   |   |   |   |   |   |   |
| ServerId | String |   |   | eni-hg231** |   | The ID of the ECS instance. |   |   |   |
| Weight | String |   |   | 100 |   | The weight of the backend server. |   |   |   |
| Description | String |   |   | BackendServer |   | The description of the backend server. |   |   |   |
| Type | String |   |   | ecs |   | The type of backend server. Valid values: ecs: an ECS instance. This is the default value. eni: an ENI. |   |   |   |
| RequestId | String |   |   | 365F4154-92F6- 4AE4-92F8- 7FF34B540710 |   | The ID of the request. |   |   |   |

Examples Sample requests

```
http(s)://[Endpoint]/? Action=SetBackendServers &LoadBalancerId=lb-bp1qjwo61pqz3a****** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<SetBackendServersResponse>
      <RequestId>365F4154-92F6-4AE4-92F8-7FF34B540710</RequestId>
      <LoadBalancerId>lb-dhf13*******</LoadBalancerId>
      <BackendServers>
            <BackendServer>
                  <ServerId>eni-hg231**</ServerId>
                  <Weight>100</Weight>
                              <Type>eni</Type>
            </BackendServer>
            <BackendServer>
                  <ServerId>eni-hfhf***</ServerId>
                  <Weight>100</Weight>
                              <Type>eni</Type>
            </BackendServer>
      </BackendServers>
</SetBackendServersResponse>
```

`JSON` format

```json
{"RequestId":"365F4154-92F6-4AE4-92F8-7FF34B540710","LoadBalancerId":"lb-bp1qjwo61pqz3a****
**","BackendServers":[{"Type":"ecs","ServerId":"i-xxxxxxxxx","Description":"BackendServer",
"VpcId":"vpc-**","ServerIp":"192.168. *. *","Weight":"100"}]}
```

### 2.9 vServer Groups

#### 2.9.1 CreateVServerGroup

Creates a vServer group and adds backend servers to the vServer group. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateVServerGro up | The operation that you want to perform. Set the value to Creat eVServerGroup. |
| LoadBalancerId | String | Yes | lb- bp1qjwo61pqz3a hl****** | The ID of the Server Load Balancer (SLB) instance. |
| RegionId | String | Yes | cn-east- hangzhou-01 | The ID of the region where the SLB instance is deployed. |

|   | Parameter |   | Type | Required | Example |   | Description |   |
|---|---|---|---|---|---|---|---|---|
|   | VServerGroupNa me |   | String | No | Group1 |   | The name of the vServer group. The name must be 1 to 80 characters in length, and can contain letters and Chinese characters, digits, hyphens (-), forward slashes (/), periods (.), and underscores ( ). _ |   |
|   | BackendServers |   | String | No | [{ "ServerId": "eni- xxxxxxxxx", "Weight": "100", "Type": "eni", "ServerIp": "192.168. **. **", "Port":"80","Desc ription":"test- 112" }, { "ServerId": "eni- xxxxxxxxx", "Weight": "100", "Type": "eni", "ServerIp": "192.168. **. **", "Port":"80","Desc ription":"test- 112" }] |   | The list of backend servers to be added. The value of this parameter must be of the STRING type and in the JSON format. You can specify up to 20 elements in each request. ServerId: Required. Specify the ID of an Elastic Compute Service (ECS) instance or an elastic network interface (ENI). This parameter is of the STRING type. Port : Required. Specify the port that is used by the backend server. This parameter is of the INTEGER type. Valid values: 1 to 65535. Weight : Required. Specify the weight of the backend server. This parameter is of the INTEGER type. Valid values: 0 to 100. Descript ion: Required. Specify the description of the backend server. This parameter is of the STRING type. The description must be 1 to 80 characters in length, and can contain letters, digits, hyphens (-), forward slashes (/), periods (.), and underscores ( ). It can also contain _ Chinese characters. T ype: Required. Specify the instance type of the backend server. This parameter is of the STRING type. Valid values: ecs (default): an ECS instance eni: an ENI ServerIp: The IP address of an ECS instance or ENI. Examples: ECS instance: [{ "ServerId": "i |   |
|   |   |   |   |   |   |   |   | [{ "ServerId": "i |
|   |   |   |   |   |   |   | -xxxxxxxxx", "Weight": "100", |   |
|   |   |   |   |   |   |   | "Type": "ecs", "Port": "80", " |   |

|   | Parameter |   | Type |   | Required |   | Example |   | Description": "test-112" }]. Description |   |   |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   |   |   | ENI: | [{ "ServerId": "eni-xxxx |   |   |
|   |   |   |   |   |   |   |   |   | xxxxx", "Weight": "100", "Type |   |   |   |
|   |   |   |   |   |   |   |   |   | ": "eni", "ServerIp": "192.168 |   |   |   |
|   |   |   |   |   |   |   |   |   | . **. **", "Port":"80","Descri |   |   |   |
|   |   |   |   |   |   |   |   |   | ption":"test-112" }] |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | [{ |   |
|   |   |   |   |   |   |   |   |   | "ServerId": "eni-xxxxxxxxx", " |   |   |   |
|   |   |   |   |   |   |   |   |   | Weight": "100", "Type": "eni", |   |   |   |
|   |   |   |   |   |   |   |   |   | "ServerIp": "192.168. **. **", |   |   |   |
|   |   |   |   |   |   |   |   |   | "Port":"80","Description":"tes |   |   |   |
|   |   |   |   |   |   |   |   |   | t-112" },{ "ServerId": "eni-xx |   |   |   |
|   |   |   |   |   |   |   |   |   | xxxxxxx", "Weight": "100", "Ty |   |   |   |
|   |   |   |   |   |   |   |   |   | pe": "eni", "ServerIp": "172.1 |   |   |   |
|   |   |   |   |   |   |   |   |   | 66. **. **", "Port":"80","Desc |   |   |   |
|   |   |   |   |   |   |   |   |   | ription":"test-113" }] |   |   |   |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| VServerGroupId | String | rsp-cige6****** | The ID of the vServer group. |
| BackendServers | Array of BackendServer |   | The list of backend servers. |
| BackendServer |   |   |   |
| ServerId | String | vm-2**** | The ID of the ECS instance or ENI. |
| Port | Integer | 70 | The port that is used by the backend server. |
| Weight | Integer | 100 | The weight of the backend server. |
| Description | String | VServerGroup | The description of the vServer group. |
| ServerType | String | ECS |   |
| Type | String | Type | The type of backend server. Valid values: ecs (default): an ECS instance eni: an ENI |
| RequestId | String | 9DEC9C28-AB05- 4DDF-9A78- 6B08EC9CE18C | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/? Action=CreateVServerGroup &LoadBalancerId=lb-bp1qjwo61pqz3ahl****** &RegionId=cn-east-hangzhou-01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<CreateVServerGroupResponse>
  <VServerGroupId>rsp-bp1i4c******</VServerGroupId>
  <RequestId>3EBBDBAE-8E8B-438F-A109-95C2FDB2C333</RequestId>
  <BackendServers>
        <BackendServer>
              <Type>ecs</Type>
              <ServerId>i-bp1ds2yjlk66********</ServerId>
              <Description>test-11244</Description>
              <Port>80</Port>
              <Weight>100</Weight>
        </BackendServer>
  </BackendServers>
</CreateVServerGroupResponse>
```

`JSON` format `{`

```json
  "VServerGroupId": "rsp-bp1i4c3******",
  "RequestId": "3EBBDBAE-8E8B-438F-A109-95C2FDB2C333",
  "BackendServers": {
    "BackendServer": [
```

`{`

```json
        "Type": "ecs",
        "ServerId": "i-bp1ds2yjlk666******",
        "Description": "test-11244",
        "Port": 80,
        "Weight": 100
```

`}` `]` `}` `}`

#### 2.9.2 SetVServerGroupAttribute

Modifies the configurations of a vServer group. You can call the operation to modify only configurations such as the weight and port of a backend server. If you want to modify backend servers in a specified vServer group, call the ModifyVServerGroupBackendServers operation. If you want to add backend servers, call the AddVServerGroupBackendServers operation. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | SetVServerGroup Attribute | The operation that you want to perform. Set the value to Set VServerGroupAt t ribut e. |
| RegionId | String | Yes | cn-east- hangzhou-01 | The ID of the region where the Server Load Balancer (SLB) instance is deployed. |
| VServerGroupId | String | Yes | rsp-cige6****** | The ID of the vServer group. |
| VServerGroupNa me | String | No | vserver-group- test | The name of the vServer group. |
| BackendServers | String | No | [{ "ServerId": "eni- xxxxxxxxx", "Weight": "100", "Type": "eni", "ServerIp": "192.168. **. **", "Port":"80","Desc ription":"test- 112" },{ | The backend servers in the vServer group. You can add up to 20 backend servers in each request. ServerId: Required. Specify the instance ID of the backend server or elastic network interface (ENI). This parameter is of the STRING type. Port : Required. Specify the port that is used by the backend server. This parameter is of the INTEGER type. Valid values: 1 to 65535. Weight : Required. Specify the weight of the backend server. This parameter is of the INTEGER type. Valid values: 0 to 100. Descript ion: Optional. Specify the description of the backend server. This parameter is of the STRING type. The description must be 1 to 80 characters in length, and can contain letters, digits, hyphens (-), forward slashes (/), periods (.), and underscores ( ). It can also contain _ Chinese characters. T ype: Specify the instance type of the backend server. Valid values: * |

|   | BackendServers Parameter |   |   | String Type |   | No Required |   | "ServerId": "eni- Example xxxxxxxxx", |   |   | ecs: an Elastic Compute Service Description (ECS) instance. This is the default |   |   |   |   |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   |   | "Weight": "100", "Type": "eni", "ServerIp": "172.166. **. **", "Port":"80","Desc ription":"test- 113" }] |   |   | value. eni: an ENI. ServerIp: the IP address of the ECS instance or ENI. Examples: ECS instance: [{ "ServerId": "i |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   | [{ "ServerId": "i |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | -xxxxxxxxx", "Weight": "100", |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | "Type": "ecs", "Port": "80", " |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | Description": "test-112" }]. |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | ENI: | [{ "ServerId": "eni-xxxx |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | xxxxx", "Weight": "100", "Type |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | ": "eni", "ServerIp": "192.168 |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | . **. **", "Port":"80","Descri |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | ption":"test-112" }] |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | [{ |   |
|   |   |   |   |   |   |   |   |   |   |   | "ServerId": "eni-xxxxxxxxx", " |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | Weight": "100", "Type": "eni", |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | "ServerIp": "192.168. **. **", |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | "Port":"80","Description":"tes |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | t-112" },{ "ServerId": "eni-xx |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | xxxxxxx", "Weight": "100", "Ty |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | pe": "eni", "ServerIp": "172.1 |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | 66. **. **", "Port":"80","Desc |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | ription":"test-113" }] |   |   |   |   |   |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| VServerGroupId | String | rsp-cige6****** | The ID of the vServer group. |
| VServerGroupN ame | String | Group1 | The name of the vServer group. |
| BackendServers | Array of BackendServer |   | The list of backend servers. |
| BackendServer |   |   |   |
| ServerId | String | i-bp1ek6yd7jvkx***** | The ID of the ECS instance or ENI. |
| Port | Integer | 70 | The port that is used by the backend server. |
| Weight | Integer | 100 | The weight of the backend server. |

|   | Developer Guide·AP | I reference |   | Server Load Balance | r |
|---|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| Description | String | The description of the vServer group. | The description of the vServer group. |
| Type | String | ecs | The type of the backend server. Valid values: ecs: an ECS instance. This is the default value. eni: an ENI. |
| RequestId | String | 9DEC9C28-AB05- 4DDF-9A78- 6B08EC9CE18C | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/? Action=SetVServerGroupAttribute &RegionId=cn-east-hangzhou-01 &VServerGroupId=rsp-cige6****** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<SetVServerGroupAttributeResponse>
  <BackendServers>
        <BackendServer>
              <ServerId>i-bp1ek6yd7jvkx*****</ServerId>
              <Port>80</Port>
              <Weight>100</Weight>
              <Type>ecs</Type>
        </BackendServer>
  </BackendServers>
  <RequestId>A4FDF333-F904-4540-88FC-ED6F87AEFFCB</RequestId>
  <VServerGroupId>rsp-bp1d2e3*****</VServerGroupId>
  <VServerGroupName>test1</VServerGroupName>
</SetVServerGroupAttributeResponse>
```

`JSON` format

```json
{"VServerGroupId":"rsp-cige6******","RequestId":"9DEC9C28-AB05-4DDF-9A78-6B08EC9CE18C","VSe rverGroupName":"Group1","BackendServers":[{"Type":"ecs","ServerId":"i-bp1ek6yd7jvkx*****"," Description":"VServerGroupDescription.","VpcId":"vpc-bp****","ServerRegionId":"cn-east-hang zhou-01","Port":"70","ServerIp":"192.168. **. **","VbrId":"vbr-bp1jcg5cmxjbl9xgc****","Weig ht":"100"}]}
```

#### 2.9.3 AddVServerGroupBackendServers

Adds backend servers to a specified vServer group. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | AddVServerGroup BackendServers | The operation that you want to perform. Set the value to AddVServerGroupBackendServers. |
| BackendServers | String | Yes | [{ "ServerId": "eni- xxxxxxxxx", "Weight": "100", "Type": "eni", "ServerIp": "192.168.0.1*", "Port":"80","Desc ription":"test- 112" },{ "ServerId": "eni- xxxxxxxxx", "Weight": "100", "Type": "eni", "ServerIp": "172.166. **. **", "Port":"80","Desc ription":"test- 113" }] | The list of backend servers that you want to add to the vServer group. You can specify up to 20 backend servers in each request. The following parameters are used to specify a list of backend servers: ServerId: The ID of the backend server. You can specify the ID of an Elastic Compute Service (ECS) instance or an elastic network interface (ENI). Port : Required. The port that is used by the backend server. Valid values: 1 t o 65535. Weight : The weight of the backend server. Valid values: 0 t o 100. Default value: 100. If the value is set to 0, no requests are forwarded to the backend server. T ype: The type of backend server. Valid values: ecs: an ECS instance. This is the default value. eni: an ENI. Descript ion: Optional. The description of the backend server. This parameter is of the STRING type. The description must be 1 to 80 characters in length, and can contain letters, digits, hyphens (-), forward slashes (/), periods (.), and underscores ( ). It can also contain _ Chinese characters. ServerIp: The IP address of an ECS instance or ENI. Examples: |

|   | Parameter |   |   | Type |   | Required |   | Example |   |   | ECS instance: |   | [{ "ServerId": "i |   |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   |   |   | xample |   | Description -xxxxxxxxx", "Weight": "100", |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | "Type": "ecs", "Port": "80", " |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | Description": "test-112" }]. |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | ENI: | [{ "ServerId": "eni-xxxx |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | xxxxx", "Weight": "100", "Type |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | ": "eni", "ServerIp": "192.168 |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | . **. **", "Port":"80","Descri |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | ption":"test-112" }] |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   | [{ |   |
|   |   |   |   |   |   |   |   |   |   |   | "ServerId": "eni-xxxxxxxxx", " |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | Weight": "100", "Type": "eni", |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | "ServerIp": "192.168. **. **", |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | "Port":"80","Description":"tes |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | t-112" },{ "ServerId": "eni-xx |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | xxxxxxx", "Weight": "100", "Ty |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | pe": "eni", "ServerIp": "172.1 |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | 66. **. **", "Port":"80","Desc |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | ription":"test-113" }] |   |   |   |   |
|   | RegionId |   |   | String |   | Yes |   | cn-east- hangzhou-01 |   |   | The ID of the region where the Server Load Balancer (SLB) instance is created. |   |   |   |   |
|   | VServerGroupId |   |   | String |   | Yes |   | rsp-cige6****** |   |   | The ID of the vServer group. |   |   |   |   |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| VServerGroupId | String | rsp-cige6j****** | The ID of the vServer group. |
| BackendServers | Array of BackendServer |   | The list of backend servers. |
| BackendServer |   |   |   |
| ServerId | String | vm-231 | The ID of the ECS instance or ENI. |
| Port | Integer | 70 | The port that is used by the backend server. |
| Weight | Integer | 100 | The weight of the backend server. |
| Description | String | test | The description of the vServer group. |

| erver Load Balanc | er |   | Developer Guide·API referenc |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| Type | String | ecs | The type of backend server. Valid values: ecs (default): an ECS instance eni: an ENI |
| RequestId | String | 9DEC9C28-AB05- 4DDF-9A78- 6B08EC9CE18C | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/? Action=AddVServerGroupBackendServers &BackendServers=[{ "ServerId": "eni-xxxxxxxxx", "Weight": "100", "Type": "eni", "ServerIp": "192.168.0.1*", "Port":"80","Description":"test-112" },{ "ServerId": "eni-xxxxxxxxx", "Weig ht": "100", "Type": "eni", "ServerIp": "172.166. **. **", "Port":"80","Description":"test-1 13" }] &RegionId=cn-east-hangzhou-01 &VServerGroupId=rsp-cige6****** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<AddVServerGroupBackendServersResponse>
  <VServerGroupId>rsp-cige6j******</VServerGroupId>
  <RequestId>9DEC9C28-AB05-4DDF-9A78-6B08EC9CE18C</RequestId>
  <BackendServers>
        <Type>ecs</Type>
        <Description>test</Description>
        <ServerId>vm-231</ServerId>
        <Weight>100</Weight>
        <Port>70</Port>
  </BackendServers>
</AddVServerGroupBackendServersResponse>
```

`JSON` format

```json
{"VServerGroupId":"rsp-cige6j******", "RequestId":"9DEC9C28-AB05-4DDF-9A78-6B08EC9CE18C", "BackendServers":[
    {"Type":"ecs","Description":"test","ServerId":"vm-231","Weight":"100","Port":"70"}
```

`]` `}`

#### 2.9.4 RemoveVServerGroupBackendServers

Removes a backend server from a specified vServer group. Not e If one or more backend servers specified by BackendServers do not exist in the vServer group, the backend servers are ignored and no error message is returned. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | RemoveVServerGr oupBackendServe rs | The operation that you want to perform. Set the value to RemoveVServerGroupBackendServ ers. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| BackendServers | String | Yes | [{ "ServerId": "eni- xxxxxxxxx", "Weight": "100", "Type": "eni", "ServerIp": "192.168. **. **", "Port":"80","Desc ription":"test- 112" },{ "ServerId": "eni- xxxxxxxxx", "Weight": "100", "Type": "eni", "ServerIp": "172.166. **. **", "Port":"80","Desc ription":"test- 113" }] | The list of backend servers that you want to remove from the vServer group. A vServer group can contain a maximum of 20 backend servers in each request. The value of this parameter must be of the STRING type and in the JSON format. You can specify up to 20 elements in each request. ServerId: Required. Specify the ID of an Elastic Compute Service (ECS) instance or elastic network interface (ENI). This parameter is of the STRING type. Port : Required. Specify the port that is used by the backend server. This parameter is of the INTEGER type. Valid values: 1 t o 65535. Weight : Required. Specify the weight of the backend server. This parameter is of the INTEGER type. Valid values: 0 t o 100. Descript ion: Optional. The description of the backend server. This parameter is of the STRING type. The description must be 1 to 80 characters in length, and can contain letters, digits, hyphens (-), forward slashes (/), periods (.), and underscores ( ). It can also contain _ Chinese characters. T ype: The instance type of the backend server. This parameter is of the STRING type. Valid values: ecs: an ECS instance. This is the default value. eni: an ENI. ServerIp: The IP address of an ECS instance or ENI. |
| RegionId | String | Yes | cn-east- hangzhou-01 | The ID of the region where the Server Load Balancer (SLB) instance is created. |
| VServerGroupId | String | Yes | rsp-cige6****** | The ID of the vServer group. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| VServerGroupId | String | rsp-cige6j***** | The ID of the vServer group. |
| BackendServers | Array of BackendServer |   | The list of backend servers. |
| BackendServer |   |   |   |
| ServerId | String | vm-230 | The ID of the ECS instance or ENI. |
| Port | Integer | 80 | The port that is used by the backend server. |
| Weight | Integer | 100 | The weight of the backend server. |
| RequestId | String | 9DEC9C28-AB05- 4DDF-9A78- 6B08EC9CE18C | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/? Action=RemoveVServerGroupBackendServers &BackendServers=[{ "ServerId": "eni-xxxxxxxxx", "Weight": "100", "Type": "eni", "ServerIp": "192.168. **. **", "Port":"80","Description":"test-112" },{ "ServerId": "eni-xxxxxxxxx", "W eight": "100", "Type": "eni", "ServerIp": "172.166. **. **", "Port":"80","Description":"tes t-113" }] &RegionId=cn-east-hangzhou-01 &VServerGroupId=rsp-cige6****** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RemoveVServerGroupBackendServersResponse>
   <RequestId>9DEC9C28-AB05-4DDF-9A78-6B08EC9CE18C</RequestId>
   <VServerGroupId>rsp-cige6******</VServerGroupId>
   <BackendServers>
      <BackendServer>
         <ServerId>vm-231</ServerId>
         <Port>70</Port>
         <Weight>100</Weight>
                              <Type>ecs</Type>
      </BackendServer>
   </BackendServers>
</RemoveVServerGroupBackendServersResponse>
```

`JSON` format `{`

```json
  "RemoveVServerGroupBackendServersResponse": {
    "RequestId": "9DEC9C28-AB05-4DDF-9A78-6B08EC9CE18C",
    "VServerGroupId": "rsp-cige6******",
    "BackendServers": {
      "BackendServer": {
        "ServerId": "vm-231",
        "Port": "70",
        "Weight": "100",
        "Type": "ecs"
```

`}` `}` `}` `}`

#### 2.9.5 ModifyVServerGroupBackendServers

Replaces backend servers in a specified vServer group. You can call this operation to replace the backend servers in a specified vServer group. To modify the configurations of the backend servers, such as their weights, see SetVServerGroupAttribute. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyVServerGro upBackendServer s | The operation that you want to perform. Set the value to Modif yVServerGroupBackendServer s. |
| RegionId | String | Yes | cn-east- hangzhou-01 | The ID of the region where the Server Load Balancer (SLB) instance is created. |
| VServerGroupId | String | Yes | rsp-cige6j****** | The ID of the vServer group. |
|   |   |   |   | The list of backend servers to be replaced. The value of this parameter must be of the STRING type and in the JSON format. You can specify up to 20 elements in each request. ServerId: Required. Specify the ID of the backend server. This parameter is of the STRING type. |

|   | Parameter |   |   | Type |   | Required |   | Example |   |   | Port : Required. Specify the port Description that is used by the backend server. |   |   |   |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|   | OldBackendServer s |   |   | String |   | No |   | [{ "ServerId": "i- xxxxxxxxx", "Weight": "100", "Type": "ecs", "Port":"80","Desc ription":"test- 112" }] |   |   | This parameter is of the INTEGER type. Valid values: 1 t o 65535. Weight : Required. Specify the weight of the backend server. This parameter is of the INTEGER type. Valid values: 0 t o 100. Descript ion: Optional. Specify the description of the backend server. This parameter is of the STRING type. The description must be 1 to 80 characters in length, and can contain letters, digits, hyphens (-), forward slashes (/), periods (.), and underscores ( ). It can also contain _ Chinese characters. T ype: The instance type of the backend server. This parameter is of the STRING type. Valid values: ecs: an Elastic Compute Service (ECS) instance. This is the default value. eni: an elastic network interface (ENI). ServerIp: The IP address of an ECS instance or ENI. Examples: ECS instance: [{ "ServerId": "i |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   | [{ "ServerId": "i |   |   |
|   |   |   |   |   |   |   |   |   |   |   | -xxxxxxxxx", "Weight": "100", |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | "Type": "ecs", "Port": "80", " |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | Description": "test-112" }]. |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | ENI: | [{ "ServerId": "eni-xxxx |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | xxxxx", "Weight": "100", "Type |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | ": "eni", "ServerIp": "192.168 |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | . **. **", "Port":"80","Descri |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | ption":"test-112" }] |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   | [{ |   |
|   |   |   |   |   |   |   |   |   |   |   | "ServerId": "eni-xxxxxxxxx", " |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | Weight": "100", "Type": "eni", |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | "ServerIp": "192.168. **. **", |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | "Port":"80","Description":"tes |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | t-112" },{ "ServerId": "eni-xx |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | xxxxxxx", "Weight": "100", "Ty |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | pe": "eni", "ServerIp": "172.1 |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | 66. **. **", "Port":"80","Desc |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | ription":"test-113" }] |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | The list of new backend servers. |   |   |   |   |

|   | erver Load Balancer |   |   |   |   |   |   |   |   |   | Developer Guide·API referenc |   |   |   |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|   | Parameter |   |   | Type |   | Required |   | Example |   |   | You can specify a maximum of 20 Description backend servers for a vServer group in |   |   |   |   |
|   | NewBackendServ ers |   |   | String |   | No |   | [{ "ServerId": "eni- xxxxxxxxx", "Weight": "100", "Type": "eni", "ServerIp": "192.168. **. **", "Port":"80","Desc ription":"test- 112" },{ "ServerId": "eni- xxxxxxxxx", "Weight": "100", "Type": "eni", "ServerIp": "172.166. **. **", "Port":"80","Desc ription":"test- 113" }] |   |   | each request. The value of this parameter must be of the STRING type and in the JSON format. You can specify up to 20 elements in each request. ServerId: Required. Specify the ID of the backend server. This parameter is of the STRING type. Port : Required. Specify the port that is used by the backend server. This parameter is of the INTEGER type. Valid values: 1 t o 65535. Weight : Required. Specify the weight of the backend server. This parameter is of the INTEGER type. Valid values: 0 t o 100. Descript ion: Optional. Specify the description of the backend server. This parameter is of the STRING type. The description can contain letters, digits, hyphens (-), forward slashes (/), periods (.), and underscores ( ). It can also contain _ Chinese characters. T ype: The instance type of the backend server. This parameter is of the STRING type. Valid values: ecs: an ECS instance. This is the default value. eni: an ENI. ServerIp: The IP address of an ECS instance or ENI. Examples: ECS instance: [{ "ServerId": "i |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   | [{ "ServerId": "i |   |   |
|   |   |   |   |   |   |   |   |   |   |   | -xxxxxxxxx", "Weight": "100", |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | "Type": "ecs", "Port": "80", " |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | Description": "test-112" }]. |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | ENI: | [{ "ServerId": "eni-xxxx |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | xxxxx", "Weight": "100", "Type |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | ": "eni", "ServerIp": "192.168 |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | . **. **", "Port":"80","Descri |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | ption":"test-112" }] |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   | [{ |   |
|   |   |   |   |   |   |   |   |   |   |   | "ServerId": "eni-xxxxxxxxx", " |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | Weight": "100", "Type": "eni", |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | "ServerIp": "192.168. **. **", |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | "Port":"80","Description":"tes |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | t-112" },{ "ServerId": "eni-xx |   |   |   |   |
|   | Document Version: |   |   | 20220928 |   |   |   |   |   |   | 19 |   |   |   |   |

|   |   |   |   | xxxxxxx", "Weight": "100", "Ty |
|---|---|---|---|---|
| Parameter | Type | Required | Example | Description |
|   |   |   |   | pe": "eni", "ServerIp": "172.1 |
|   |   |   |   | 66. **. **", "Port":"80","Desc |
|   |   |   |   | ription":"test-113" }] |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| VServerGroupId | String | rsp-cige6j****** | The ID of the vServer group. |
| BackendServers | Array of BackendServer |   | The list of backend servers. |
| BackendServer |   |   |   |
| ServerId | String | vm-236 | The ID of the ECS instance or ENI. |
| Port | Integer | 70 | The port that is used by the backend server. |
| Weight | Integer | 100 | The weight of the backend server. |
| RequestId | String | 9DEC9C28-AB05- 4DDF-9A78- 6B08EC9CE18C | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/? Action=ModifyVServerGroupBackendServers &RegionId=cn-east-hangzhou-01 &VServerGroupId=rsp-cige6j****** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ModifyVServerGroupBackendServersResponse>
  <VServerGroupId>rsp-cige6j******</VServerGroupId>
  <RequestId>9DEC9C28-AB05-4DDF-9A78-6B08EC9CE18C</RequestId>
  <BackendServers>
        <ServerId>vm-236</ServerId>
        <Weight>100</Weight>
        <Port>70</Port>
  </BackendServers>
</ModifyVServerGroupBackendServersResponse>
```

`JSON` format

```json
{"VServerGroupId":"rsp-cige6j******","RequestId":"9DEC9C28-AB05-4DDF-9A78-6B08EC9CE18C","Ba ckendServers":[{"ServerId":"vm-236","Weight":"100","Port":"70"}]}
```

#### 2.9.6 DeleteVServerGroup

Deletes a vServer group. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteVServerGro up | The operation that you want to perform. Set the value to Delet eVServerGroup. |
| RegionId | String | Yes | cn-hangzhou | The ID of the region where the Server Load Balancer (SLB) instance is created. |
| VServerGroupId | String | Yes | rsp-cige6j***** | The ID of the vServer group. Not e You cannot delete a vServer group that is being used. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 9DEC9C28-AB05- 4DDF-9A78- 6B08EC9CE18C | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/? Action=DeleteVServerGroup &RegionId=cn-hangzhou &VServerGroupId=rsp-cige6j***** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DeleteVServerGroupResponse>
   <RequestId>9DEC9C28-AB05-4DDF-9A78-6B08EC9CE18C</RequestId>
</DeleteVServerGroupResponse>
```

`JSON` format `{`

```json
"RequestId":"9DEC9C28-AB05-4DDF-9A78-6B08EC9CE18C"
```

`}`

#### 2.9.7 DescribeVServerGroups

Queries the vServer groups of a Server Load Balancer (SLB) instance. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeVServerG roups | The operation that you want to perform. Set the value to DescribeVServerGroups. |
| LoadBalancerId | String | Yes | lb- bp1o94dp5i6ea** ***** | The ID of the SLB instance. |
| RegionId | String | Yes | cn-east- hangzhou-01 | The ID of the region where the SLB instance is deployed. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| VServerGroups | Array of VServerGroup |   | The list of backend servers. |
| VServerGroup |   |   |   |
| VServerGroupId | String | rsp-bp1oygn****** | The ID of the vServer group. |
| VServerGroupN ame | String | k8s/31065/nginx- ingress-lb/kube- system/clust****" | The name of the vServer group. |
| RequestId | String | 9DEC9C28-AB05- 4DDF-9A78- 6B08EC9CE18C | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/? Action=DescribeVServerGroups &LoadBalancerId=lb-bp1o94dp5i6ea******* &RegionId=cn-east-hangzhou-01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeVServerGroupsResponse>
  <VServerGroups>
        <VServerGroup>
              <VServerGroupId>rsp-bp1oygn******</VServerGroupId>
              <VServerGroupName>k8s/31065/nginx-ingress-lb/kube-system/clust****</VServerGr
oupName>
              <AssociatedObjects>
                    <Listeners>
            </Listeners>
                    <Rules>
            </Rules>
              </AssociatedObjects>
        </VServerGroup>
        <VServerGroup>
              <VServerGroupId>rsp-bp1i6sn******</VServerGroupId>
              <VServerGroupName>k8s/31605/nginx-ingress-lb/kube-system/clusterid</VServerGr
oupName>
              <AssociatedObjects>
                    <Listeners>
            </Listeners>
                    <Rules>
            </Rules>
              </AssociatedObjects>
        </VServerGroup>
        <VServerGroup>
              <VServerGroupId>rsp-bp1f85n******</VServerGroupId>
              <VServerGroupName>VSG1</VServerGroupName>
              <AssociatedObjects>
                    <Listeners>
            </Listeners>
                    <Rules>
            </Rules>
              </AssociatedObjects>
        </VServerGroup>
  </VServerGroups>
  <RequestId>31ADDBCD-275F-4C37-B0A3-5DFC8564E686</RequestId>
</DescribeVServerGroupsResponse>
```

`JSON` format `{`

```json
 "VServerGroups": {
  "VServerGroup": [
```

`{`

```json
    "VServerGroupId": "rsp-bp1oygn******",
    "VServerGroupName": "k8s/31065/nginx-ingress-lb/kube-system/clust****",
    "AssociatedObjects": {
     "Listeners": {
      "Listener": []
```

`},`

```json
     "Rules": {
      "Rule": []
```

`}` `}` `},` `{`

```json
    "VServerGroupId": "rsp-bp1i6sn******",
    "VServerGroupName": "k8s/31605/nginx-ingress-lb/kube-system/clusterid",
    "AssociatedObjects": {
     "Listeners": {
      "Listener": []
```

`},`

```json
     "Rules": {
      "Rule": []
```

`}` `}` `},` `{`

```json
    "VServerGroupId": "rsp-bp1f85n******",
    "VServerGroupName": "VSG1",
    "AssociatedObjects": {
     "Listeners": {
      "Listener": []
```

`},`

```json
     "Rules": {
      "Rule": []
```

`}` `}` `}` `]` `},`

```json
 "RequestId": "31ADDBCD-275F-4C37-B0A3-5DFC8564E686"
```

`}`

#### 2.9.8 DescribeVServerGroupAttribute

Queries detailed information about a vServer group. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeVServerG roupAttribute | The operation that you want to perform. Set the value to DescribeVServerGroupAt t ribut e. |
| RegionId | String | Yes | cn-east- hangzhou-01 | The ID of the region where the Server Load Balancer (SLB) instance is created. |
| VServerGroupId | String | Yes | rsp-cige6****** | The ID of the vServer group. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| VServerGroupId | String | rsp-cige6***** | The ID of the vServer group. |
| VServerGroupN ame | String | Group1 | The name of the vServer group. The name must be 1 to 80 characters in length, and can contain Chinese characters, letters, digits, hyphens (-), forward slashes (/), periods (.), and underscores ( ). _ |
| BackendServers | Array of BackendServer |   | The list of backend servers. |
| BackendServer |   |   |   |
| ServerId | String | vm-233 | The ID of the Elastic Compute Service (ECS) instance. |
| Port | Integer | 90 | The port that is used by the backend server. |
| Weight | Integer | 100 | The weight of the backend server. |
| Description | String | vServerGroupDescrip tion. | The description of the vServer group. |
| ServerType | String | ecs |   |
| Type | String | ecs | The type of the backend server. Valid values: ecs (default): an ECS instance eni: an elastic network interface (ENI) |

| Developer Guide·AP | I reference |   | Server Load Balance |
|---|---|---|---|
| Parameter | Type | Example | Description |

| RequestId | String | 9DEC9C28-AB05- 4DDF-9A78- 6B08EC9CE18C | The ID of the request. |
|---|---|---|---|

Examples Sample requests

```
http(s)://[Endpoint]/? Action=DescribeVServerGroupAttribute &RegionId=cn-east-hangzhou-01 &VServerGroupId=rsp-cige6****** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeVServerGroupAttributeResponse>
   <RequestId>9DEC9C28-AB05-4DDF-9A78-6B08EC9CE18C</RequestId>
   <VServerGroupId>rsp-cige6******</VServerGroupId>
   <VServerGroupName>Group1</VServerGroupName>
   <BackendServers>
      <BackendServer>
         <ServerId>vm-232</ServerId>
         <Port>80</Port>
         <Weight>100</Weight>
      </BackendServer>
      <BackendServer>
         <ServerId>vm-233</ServerId>
         <Port>90</Port>
         <Weight>100</Weight>
      </BackendServer>
   </BackendServers>
</DescribeVServerGroupAttributeResponse>
```

`JSON` format

```json
{"VServerGroupId":"rsp-cige6*****","RequestId":"9DEC9C28-AB05-4DDF-9A78-6B08EC9CE18C","VSer verGroupName":"Group1","BackendServers":[{"ServerType":"ecs","Type":"ecs","ServerId":"vm-23 3","Description":"vServerGroupDescription.","VpcId":"vpc-**","Port":"90","ServerIp":"192.16
8. *. *","Weight":"100"}]}
```

### 2.10 Primary/secondary Server Groups

Groups

#### 2.10.1 CreateMasterSlaveServerGroup

Creates a primary/secondary server group. A primary/secondary server group contains only two Elastic Compute Service (ECS) instances. One of the instances serves as the primary server. The other instance serves as the secondary server. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateMasterSlav eServerGroup | The operation that you want to perform. Set the value to Creat eMast erSlaveServerGroup. |
| LoadBalancerId | String | Yes | lb- bp1hv944r69al4j* ***** | The ID of the Server Load Balancer (SLB) instance. |
| RegionId | String | Yes | cn-east- hangzhou-01 | The ID of the region where the SLB instance is created. |
| MasterSlaveServe rGroupName | String | No | sg- atstuj3rtopty**** | The name of the primary/secondary server group. |
|   |   |   |   | The list of backend servers in the primary/secondary server group. The value of this parameter must be of the STRING type and in the JSON format. You can specify up to 20 elements for this parameter in each request. ServerId: Required. Specify the instance ID of the backend server. This parameter is of the STRING type. Port : Required. Specify the port that is used by the backend server. This parameter is of the INTEGER type. Valid values: 1 t o 65535. Weight : Required. Specify the weight of the backend server. This parameter is of the INTEGER type. Valid values: 0 t o 100. |

| Parameter |   |   | Type | Required |   | Example |   | Descript ion: Optional. Specify the Description description of the backend server. |   |   |   |
|---|---|---|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   |   | This parameter is of the STRING type. The description must be 1 to 80 characters in length, and can contain letters, digits, hyphens (-), forward slashes (/), periods (.), and underscores ( ). The description can _ contain Chinese characters. |   |   |   |
| MasterSlaveBacke ndServers |   |   | String | No |   | [{ "ServerId": "i- xxxxxxxxx", "Weight": "100", "Type": "ecs", "Port":"80","Serv erType":"Master" ,"Description":"te st-112" }, { "ServerId": "i- xxxxxxxxx", "Weight": "100", "Type": "ecs", "Port":"80","Serv erType":"Slave"," Description":"tes t-112" }] |   | ServerT ype: Specify the type of the backend server. This parameter is of the STRING type. Valid values: Mast er: primary server Slave: secondary server T ype: Specify the instance type of the backend server. This parameter is of the STRING type. Valid values: ecs: an ECS instance. This is the default value. eni: an elastic network interface (ENI). ServerIp: the IP address of the ECS instance or ENI. A primary/secondary server group can contain a maximum of two backend servers. If you do not set this parameter, an empty primary/secondary server group is created. Examples: ECS instance: [{ "ServerId": "i |   |   |   |
|   |   |   |   |   |   |   |   |   |   | [{ "ServerId": "i |   |
|   |   |   |   |   |   |   |   | -xxxxxxxxx", "Weight": "100", |   |   |   |
|   |   |   |   |   |   |   |   | "Type": "ecs", "Port": "80", " |   |   |   |
|   |   |   |   |   |   |   |   | ServerType": "Master", "Descri |   |   |   |
|   |   |   |   |   |   |   |   | ption": "test-112" }, { "Serve |   |   |   |
|   |   |   |   |   |   |   |   | rId": "i-xxxxxxxxx", "Weight": |   |   |   |
|   |   |   |   |   |   |   |   | "100", "Type": "ecs", "Port":" |   |   |   |
|   |   |   |   |   |   |   |   | 80","ServerType":"Slave","Desc |   |   |   |
|   |   |   |   |   |   |   |   | ription":"test-112" }] |   |   |   |
|   |   |   |   |   |   |   |   | ENI: | [{ "ServerId": "eni-xxxx |   |   |
|   |   |   |   |   |   |   |   | xxxxx", "Weight": "100", "Type |   |   |   |
|   |   |   |   |   |   |   |   | ": "eni", "Port": "80", "Serve |   |   |   |
|   |   |   |   |   |   |   |   | rType": "Master", "Description |   |   |   |
|   |   |   |   |   |   |   |   | ": "test-112" }, { "ServerId": |   |   |   |
|   |   |   |   |   |   |   |   | "eni-xxxxxxxxx", "Weight": "10 |   |   |   |
|   |   |   |   |   |   |   |   | 0", "Type": "eni", "ServerIp": |   |   |   |
|   |   |   |   |   |   |   |   | "192.168. **. **", "Port":"80" |   |   |   |
|   |   |   |   |   |   |   |   | ,"ServerType":"Slave","Descrip |   |   |   |
|   |   |   |   |   |   |   |   | tion":"test-112" }] |   |   |   |

|   | Parameter | Type |   | Required | Example |   | ENI with multiple IP addresses: |   | [{ |   |
|---|---|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   | Description "ServerId": "eni-xxxxxxxxx", " |   |   |   |
|   |   |   |   |   |   |   | Weight": "100", "Type": "eni", |   |   |   |
|   |   |   |   |   |   |   | "ServerIp": "192.168. **. **", |   |   |   |
|   |   |   |   |   |   |   | "Port":"80","ServerType":"Mast |   |   |   |
|   |   |   |   |   |   |   | er","Description":"test-112" } |   |   |   |
|   |   |   |   |   |   |   | , { "ServerId": "eni-xxxxxxxxx |   |   |   |
|   |   |   |   |   |   |   | ", "Weight": "100", "Type": "e |   |   |   |
|   |   |   |   |   |   |   | ni","ServerIp": "192.168. **. |   |   |   |
|   |   |   |   |   |   |   | **", "Port":"80","ServerType": |   |   |   |
|   |   |   |   |   |   |   | "Slave","Description":"test-11 |   |   |   |
|   |   |   |   |   |   |   | 2" }] |   |   |   |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| MasterSlaveSer verGroupId | String | rsp-cige6j****** | The ID of the primary/secondary server group. |
| MasterSlaveBac kendServers | Array of MasterSlaveBac kendServer |   | The list of backend servers in the primary/secondary server group. |
| MasterSlaveBac kendServer |   |   |   |
| ServerId | String | vm-2h**** | The ID of the ECS instance or ENI that you want to add. |
| Port | Integer | 90 | The port that is used by the backend server. |
| Weight | Integer | 100 | The weight of the backend server. |
| ServerType | String | Slave | The type of the backend server. Valid values: Mast er and Slave. Default value: Master. |
| Description | String | Primary/SecondaryS erverGroupdDescript ion. | The description of the primary/secondary server group. The description must be 1 to 80 characters in length, and can contain letters and Chinese characters, digits, hyphens (-), forward slashes (/), periods (.), and underscores ( ). _ |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Type | String | ecs | The type of the backend server. Valid values: ecs: an ECS instance. This is the default value. eni: an ENI. |
| RequestId | String | 9DEC9C28-AB05- 4DDF-9A78- 6B08EC9CE18C | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/? Action=CreateMasterSlaveServerGroup &LoadBalancerId=lb-bp1hv944r69al4j****** &RegionId=cn-east-hangzhou-01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<CreateMasterSlaveServerGroupResponse>
      <RequestId>9DEC9C28-AB05-4DDF-9A78-6B08EC9CE18C</RequestId>
      <MasterSlaveServerGroupId>rsp-cige******</MasterSlaveServerGroupId>
      <MasterSlaveBackendServers>
            <MasterSlaveBackendServers>
               <ServerId>vm-gtgt***</ServerId>
               <Port>80</Port>
               <Weight>100</Weight>
         <ServerType>Master</ServerType>
            </MasterSlaveBackendServers>
            <MasterSlaveBackendServers>
               <ServerId>vm-tygtyg****</ServerId>
               <Port>90</Port>
               <Weight>100</Weight>
         <ServerType>Slave</ServerType>
            </MasterSlaveBackendServers>
      </MasterSlaveBackendServers>
</CreateMasterSlaveServerGroupResponse>
```

`JSON` format

```json
{"RequestId":"9DEC9C28-AB05-4DDF-9A78-6B08EC9CE18C","MasterSlaveServerGroupId":"rsp-cige6j*
*****","MasterSlaveBackendServers":[{"ServerType":"Slave","Type":"ecs","ServerId":"vm-2h***
*","Description":"The description of the primary/secondary server group.","VpcId":"vpc-***" ,"Port":"90","ServerIp":"vm-***","Weight":"100"}]}
```

Error codes

| HttpCode | Error code | Error message | Required |
|---|---|---|---|
| 400 | BACKEND SERVERS N _ _ UM MUST BE TWO _ _ _ | Backend servers num must be 2. | The error message returned because only two backend servers can be specified. |
| 400 | BACKEND SERVERS H _ _ AVE SAME PORT AN _ _ _ D SERVERID _ | Backend servers have same port and serverId. | The error message returned because a backend server with the same port and server ID already exists. |
| 400 | BACKEND SERVERS C _ _ AN ONLY CONTAIN _ _ _ ONE MASTER AND O _ _ _ NE SLAVE _ | Backend servers can only contain one master and one slave. | The error message returned because a primary/secondary server group can contain only one primary server and one secondary server. |
| 400 | BACKEND SERVER ID _ _ CAN NOT EMPTY _ _ _ | Backend server id can not empty. | The error message returned because the backend server ID is required. |
| 400 | INVALID SERVER TYP _ _ E | Invalid server type. | The error message returned because the specified backend server type is invalid. |
| 400 | BACKEND SERVER PO _ _ RT CAN NOT EMPTY _ _ _ | Backend server port can not empty. | The error message returned because the port that is used by the backend server is required. |
| 400 | RealServerPortNotSu pport | Real server port not support. | The error message returned because the port that is used by the backend server is invalid. |

#### 2.10.2 DeleteMasterSlaveServerGroup

Deletes a specified primary/secondary server group. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteMasterSlav eServerGroup | The operation that you want to perform. Set the value to Delet eMast erSlaveServerGroup. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| MasterSlaveServe rGroupId | String | Yes | rsp-cige6****** | The ID of the primary/secondary server group. Not e You cannot delete a primary/secondary server group that is in use. |
| RegionId | String | Yes | cn-east- hangzhou-01 | The ID of the region where the Server Load Balancer (SLB) instance is deployed. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 9DEC9C28-AB05- 4DDF-9A78- 6B08EC9CE18C | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/? Action=DeleteMasterSlaveServerGroup &MasterSlaveServerGroupId=rsp-cige6****** &RegionId=cn-east-hangzhou-01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DeleteMasterSlaveServerGroupResponse>
   <RequestId>9DEC9C28-AB05-4DDF-9A78-6B08EC9CE18C</RequestId>
</DeleteMasterSlaveServerGroupResponse>
```

`JSON` format `{`

```json
"RequestId":"9DEC9C28-AB05-4DDF-9A78-6B08EC9CE18C"
```

`}`

#### 2.10.3 DescribeMasterSlaveServerGroups

Queries backend servers in a primary/secondary server group. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeMasterSl aveServerGroups | The operation that you want to perform. Set the value to DescribeMast erSlaveServerGroups. |
| LoadBalancerId | String | Yes | lb- bp14zi0n66zpg6 o****** | The ID of the Server Load Balancer (SLB) instance. |
| RegionId | String | Yes | cn-east- hangzhou-01 | The ID of the region where the SLB instance is deployed. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| MasterSlaveSer verGroups | Array of MasterSlaveSer verGroup |   | The list of backend servers in the primary/secondary server group. |
| MasterSlaveSer verGroup |   |   |   |
| MasterSlaveSer verGroupId | String | rsp-0bfuc****** | The ID of the primary/secondary server group. |
| MasterSlaveSer verGroupName | String | Group3 | The name of the primary/secondary server group. |
| RequestId | String | 9DEC9C28-AB05- 4DDF-9A78- 6B08EC9CE18C | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/? Action=DescribeMasterSlaveServerGroups &LoadBalancerId=lb-bp14zi0n66zpg6o****** &RegionId=cn-east-hangzhou-01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeMasterSlaveServerGroupsResponse>
      <RequestId>2631BB5E-B576-4925-BDED-07A66D23E5DE</RequestId>
      <MasterSlaveServerGroups>
     <MasterSlaveServerGroup>
        <MasterSlaveServerGroupId>rsp-bp1ro3mw******</MasterSlaveServerGroupId>
        <MasterSlaveServerGroupName>test</MasterSlaveServerGroupName>
     </MasterSlaveServerGroup>
      </MasterSlaveServerGroups>
</DescribeMasterSlaveServerGroupsResponse>
```

`JSON` format `{`

```json
    "RequestId": "265989FE-136B-4D6A-B549-FD40E7",
    "MasterSlaveServerGroups": {
        "MasterSlaveServerGroup": [
```

`{`

```json
                "MasterSlaveServerGroupId": "rsp-bp1nly******",
                "MasterSlaveServerGroupName": "Primary/SecondaryServerGroup1",
                "AssociatedObjects": {
                    "Listeners": {
                        "Listener": [ ]
```

`}` `}` `}` `]` `}` `}`

#### 2.10.4 DescribeMasterSlaveServerGroupAttribute

Queries detailed information about a primary/secondary server group. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeMasterSl aveServerGroupA ttribute | The operation that you want to perform. Set the value to DescribeMast erSlaveServerGroupA t t ribut e. |
| MasterSlaveServe rGroupId | String | Yes | rsp-cige6j****** | The ID of the primary/secondary server group. |

| erver Load Balancer |   |   |   | Developer Guide·API referenc |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| RegionId | String | Yes | cn-hangzhou | The ID of the region where the Server Load Balancer (SLB) instance is deployed. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| MasterSlaveSer verGroupId | String | rsp-cige6****** | The ID of the primary/secondary server group. |
| MasterSlaveSer verGroupName | String | Group1 | The name of the primary/secondary server group. |
| MasterSlaveBac kendServers | Array of MasterSlaveBac kendServer |   | The backend servers in the primary/secondary server group. |
| MasterSlaveBac kendServer |   |   |   |
| ServerId | String | vm-hrf****** | The ID of the Elastic Compute Service (ECS) instance or elastic network interface (ENI). |
| Port | Integer | 90 | The port that is used by the backend server. |
| Weight | Integer | 100 | The weight of the backend server. |
| ServerType | String | Slave | The type of backend server. Valid values: Mast er and Slave. Default value: Master. |
| Description | String | Primary/SecondaryS erverGroupDescripti on. | The description of the primary/secondary server group. |
| Type | String | ecs | The type of backend server. Valid values: ecs: an ECS instance. This is the default value. eni: an ENI. |
| RequestId | String | 9DEC9C28-AB05- 4DDF-9A78- 6B08EC9CE18C | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/? Action=DescribeMasterSlaveServerGroupAttribute &MasterSlaveServerGroupId=rsp-cige6j****** &RegionId=cn-hangzhou &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeMasterSlaveServerGroupAttributeResponse>
    <RequestId>9DEC9C28-AB05-4DDF-9A78-6B08EC9CE18C</RequestId>
    <MasterSlaveServerGroupId>rsp-cige6******</MasterSlaveServerGroupId>
    <MasterSlaveBackendServers>
          <MasterSlaveBackendServers>
                <ServerId>vm-sshssh****</ServerId>
                <Port>80</Port>
                <Weight>100</Weight>
                <ServerType>Master</ServerType>
          </MasterSlaveBackendServers>
          <MasterSlaveBackendServers>
                <ServerId>vm-ffff*****</ServerId>
                <Port>90</Port>
                <Weight>100</Weight>
                <ServerType>Slave</ServerType>
          </MasterSlaveBackendServers>
    </MasterSlaveBackendServers>
</DescribeMasterSlaveServerGroupAttributeResponse>
```

`JSON` format `{`

```json
  "DescribeMasterSlaveServerGroupAttributeResponse": {
    "RequestId": "9DEC9C28-AB05-4DDF-9A78-6B08EC9CE18C",
    "MasterSlaveServerGroupId": "rsp-cige6******",
    "MasterSlaveBackendServers": {
      "MasterSlaveBackendServers": [
```

`{`

```json
          "ServerId": "vm-sshssh****",
          "Port": "80",
          "Weight": "100",
          "ServerType": "Master"
```

`},` `{`

```json
          "ServerId": "vm-ffff*****",
          "Port": "90",
          "Weight": "100",
          "ServerType": "Slave"
```

`}` `]` `}` `}` `}`

### 2.11 Tags

#### 2.11.1 AddTags

Adds tags to a Server Load Balancer (SLB) instance. When you call this operation, take note of the following items: You can add up to 10 tags to an SLB instance. You can specify up to five tags in each request. All tags and keys added to an SLB instance must be unique. If you add a tag that has the same key as an existing tag but with a different value, the new tag overwrites the existing tag. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | AddTags | The operation that you want to perform. Set the value to AddT ags. |
| LoadBalancerId | String | Yes | lb- bp1b6c719dfa08 ex***** | The ID of the SLB instance. |

|   | Developer Guide·API r | eference |   |   | Server Load Balance | r |
|---|---|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| RegionId | String | Yes | cn-east- hangzhou-01 | The ID of the region where the SLB instance is created. |
| Tags | String | Yes | [{"TagKey":"Key1" ,"TagValue":"Val ue1"}, {"TagKey":"Key2", "TagValue":"Valu e2"}] | The list of tags to be added. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 365F4154-92F6- 4AE4-92F8- 7FF34B540710 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/? Action=AddTags &LoadBalancerId=lb-bp1b6c719dfa08ex***** &RegionId=cn-east-hangzhou-01 &Tags=[{"TagKey":"Key1","TagValue":"Value1"},{"TagKey":"Key2","TagValue":"Value2"}] &<Common request parameters>
```

Sample success responses `XML` format

```xml
<AddTagsResponse>
   <RequestId>365F4154-92F6-4AE4-92F8-7FF34B540710</RequestId>
</AddTagsResponse>
```

`JSON` format `{`

```json
  "RequestId":"365F4154-92F6-4AE4-92F8-7FF34B540710"
```

`}`

#### 2.11.2 DescribeTags

Queries a list of tags. When you call this operation, take note of the following items: You can query tags by instance ID, tag key, and tag value. If the operation is successful, the system returns all tags that match the specified conditions. If the logical relationship among the specified conditions is `AND` , only tags that match all of the specified conditions are returned. If the Tagkey parameter is specified and the Tagvalue parameter is not specified, all tags that contain the specified tag key are returned. If you have specified the Tagvalue parameter in a request, you must also specify the Tagkey parameter in this request. If you specify both the Tagkey and Tagvalue parameters, tags with the specified key-value pair are returned. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeTags | The operation that you want to perform. Set the value to DescribeT ags. |
| RegionId | String | Yes | cn-east- hangzhou-01 | The ID of the region where the Server Load Balancer (SLB) instance is created. |
| LoadBalancerId | String | No | lb- bp1b6c719dfa08 ex***** | The ID of the SLB instance. |
| Tags | String | No | [{"TagKey":"Key1" ,"TagValue":"Val ue1"}, {"TagKey":"Key2", "TagValue":"Valu e2"}] | The list of tags to be queried. |
| DistinctKey | Boolean | No | false | Specifies whether the tag is DistinctKey. Valid values: t rue and f alse. |
| PageSize | Integer | No | 50 | The number of entries to return on each page. Default value: 50. Maximum value: 100. |
| PageNumber | Integer | No | 1 | The number of the page to return. Minimum value: 1. Default value: 1. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| TagSets | Array of TagSet |   | The list of tags. |
| TagSet |   |   |   |
| TagKey | String | test | The key of the tag. |
| TagValue | String | api | The value of the tag. |
| InstanceCount | Integer | 10 | The number of instances to which the tag is added. |
| PageSize | Integer | 50 | The number of entries returned on each page. Default value: 50. Maximum value: 100. |
| PageNumber | Integer | 1 | The number of the returned page. Minimum value: 1. Default value: 1. |
| TotalCount | Integer | 1 | The total number of instances that are returned after the tags are matched against the specified conditions. |
| RequestId | String | 365F4154-92F6- 4AE4-92F8- 7FF34B540710 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/? Action=DescribeTags &RegionId=cn-east-hangzhou-01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeTagsResponse>
   <RequestId>365F4154-92F6-4AE4-92F8-7FF34B540710</RequestId>
    <TagSets>
            <TagSet>
                  <TagKey>test</TagKey>
                  <TagValue>api</TagValue>
            </TagSet>
      </TagSets>
   <PageSize>50</PageSize>
   <PageNumber>1</PageNumber>
   <TotalCount>1</TotalCount>
</DescribeTagsResponse>
```

`JSON` format `{`

```json
    "RequestId": "365F4154-92F6-4AE4-92F8-7FF34B540710",
    "TagSets": {
        "TagSet": [
```

`{`

```json
                "TagKey": "test",
                "TagValue": "api"
```

`}` `],`

```json
        "PageNumber": 1,
        "PageSize": 50,
        "TotalCount": 1
```

`}` `}`

#### 2.11.3 RemoveTags

Removes tags that are added to a Server Load Balancer (SLB) instance. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | RemoveTags | The operation that you want to perform. Set the value to RemoveT ags. |
| LoadBalancerId | String | Yes | lb- bp1b6c719dfa08 ex***** | The ID of the SLB instance. |
| RegionId | String | Yes | cn-east- hangzhou-01 | The ID of the region where the SLB instance is created. |

| Developer Guide·API r | eference |   |   | Server Load Balance |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Tags | String | Yes | [{"TagKey":"Key1" ,"TagValue":"Val ue1"}, {"TagKey":"Key2", "TagValue":"Valu e2"}] | The list of tags that you want to remove. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 365F4154-92F6- 4AE4-92F8- 7FF34B540710 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/? Action=RemoveTags &LoadBalancerId=lb-bp1b6c719dfa08ex***** &RegionId=cn-east-hangzhou-01 &Tags=[{"TagKey":"Key1","TagValue":"Value1"},{"TagKey":"Key2","TagValue":"Value2"}] &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RemoveTagsResponse>
   <RequestId>365F4154-92F6-4AE4-92F8-7FF34B540710</RequestId>
</RemoveTagsResponse>
```

`JSON` format

```json
{ "RequestId": "365F4154-92F6-4AE4-92F8-7FF34B540710" }
```

### 2.12 Error codes

|   | Error code |   |   |   | Error message |   |   | HTTP status code | Description |
|---|---|---|---|---|---|---|---|---|---|
|   | CertificateAndPriv |   |   |   | Certificate and |   |   |   | The error message returned when the certificate is already in use by other listeners. |
|   |   |   |   |   |   | Certificate and |   |   | The |
|   |   | CertificateAndPriv |   |   |   | Certificate |   |   |   |
|   |   |   | ficateAndPriv |   | PrivateKey I |   |   |   |   |
|   |   |   |   |   |   |   |   | 40 |   |
|   | ateKeyIsRefered |   | sRefered |   |   |   |   |   |   |
|   |   |   |   |   | Refered. |   |   |   |   |

|   |   |   |   |   |   | Error code |   |   |   |   |   |   |   |   |   |   |   | Error message |   |   |   |   | HTTP status code |   | Description |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   | CertificateNotMatc |   |   |   |   |   |   |   |   |   |   |   | Certificate and |   |   |   |   |   |   | The error message returned when the certificate and private key do not match. |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | Certificate and |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   | CertificateNotMatc |   |   |   |   |   |   |   |   |   |   |   | Certifi |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | ficateNotMatc |   |   |   |   |   |   | key does |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | 400 |   |   |   |
|   |   |   |   |   |   | hPrivateKey |   |   |   |   | eKey |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | match. |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | No health- |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | No health- |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | ch |   |   | ecked Listener |   |   |   | The error message returne |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   | enerNot |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | to |   |   | the specified |   | 404 |   | the heal |   |
|   |   |   |   |   |   | Found |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | port of the Load |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | Balancer. |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | User not |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | User not |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | authorized to |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | operate on the |   |   |   |   |   |   | The error message returned when |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The error message returned |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | specified |   |   |   |   |   |   | you do not have permission |   |
|   |   |   |   |   |   |   | Forbbiden.SubUser |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | 403 |   | you do not have |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | resource as your |   |   |   |   |   |   | operate the reso |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | account is |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | created by |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | another user. |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   | Forbidden |   |   |   |   |   |   |   |   |   |   |   | User not |   |   |   |   |   |   | The error message returned when you do not have permission to operate the resource. |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | User not |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | authorized to |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The error me |   |
|   |   |   |   |   |   |   |   | Forbidden |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | operate on the |   |   |   |   | 403 |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | specified |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | resource. |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   | IncorrectListenerA |   |   |   |   |   |   |   |   |   |   |   | Current |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | Current |   |   |   |   |   | The error message returned when |   |
|   |   |   |   |   |   |   | IncorrectList |   |   |   |   |   |   |   | enerA |   |   | listener access |   |   |   |   |   |   | The error message returned w |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | the current access control stat |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | the current a |   |
|   |   |   |   |   |   |   | ccessControlStatusSt |   |   |   |   |   |   |   |   |   |   | co |   | ntrol status |   |   | 500 |   | the listener d |   |
|   |   |   |   |   |   | atus |   |   |   |   |   |   |   |   |   |   |   | does not support |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | this operation. |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The request |   |   |   |   |   |   | The error message returned when an unknown internal error occurs. |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The request |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | processing has |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The error message re |   |
|   |   |   |   |   |   |   | InternalError |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | failed due to |   |   |   |   | 400 |   | unkn |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | backend service |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | exception. |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The request |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The request |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | processing has |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   | InternalInvokeErro |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | failed due to |   |   |   |   |   |   | The error message re |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | 500 |   |   |   |
|   |   |   |   |   |   | r |   |   |   |   |   |   |   |   |   |   |   | some unknown |   |   |   |   |   |   | unkno |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | error, exception |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | or failure. |   |   |   |   |   |   |   |   |

|   |   |   |   | Error code |   |   |   |   |   |   |   |   |   |   | Error message |   |   |   | HTTP status code | Description |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | Specified |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | Specified |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | LoadBalancer |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | instance's |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The error message returned when |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | addresstype is |   |   |   |   | the network types of the backend |   |
|   |   |   |   |   | InvalidBackendServ |   |   |   |   |   |   |   |   |   |   |   |   |   |   | the network types of the backen |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | private, so it |   |   | is | 400 | server and the SLB instance do no |   |
|   |   |   |   | ers.Inconsistent |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | server and t |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | forbidden to add |   |   |   |   | match. |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | ecs vpc |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | backendservers |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | for now. |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | All |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | All |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | BackendServers on |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The error message returned when |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The error message returned when |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | one Specified |   |   |   |   | the ECS instances acting as backend |   |
|   |   |   |   |   |   |   | InvalidBackendServ |   |   |   |   |   |   |   |   |   |   |   |   | the ECS instances ac |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | LoadBalancer h |   |   | ave | 400 | servers for the SLB |   |
|   |   |   |   | ers.Inconsistent |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | to be in the same |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | vpc or all |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | classic |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The request |   |   |   |   | The error message returned when you do not have permission to operate. |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The request |   |   |   | The error me |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | identity was not |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | 400 |   |   |
|   |   |   |   | InvalidIdentity | InvalidIdentity |   |   |   |   | entity |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | allowed |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | operated. |   |   |   |   |   |   |
|   |   |   |   | InvalidLoadBalance |   |   |   |   |   |   |   |   |   |   |   |   |   |   | 404 | The error message returned when the specified SLB instance does not exist. |   |
|   |   |   |   |   | InvalidLoadBalance |   |   |   |   |   |   |   |   |   |   | LoadBala | ncerId |   | 404 |   |   |
|   |   |   |   | rId.NotF |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   | ound |   |   |   |   |   |   | does not exist. |   |   |   |   |   |   |
|   |   |   |   | InvalidParameter |   |   |   |   |   |   |   |   |   |   | The specified |   |   |   |   | The error message returned when the format of the specified certificate is incorrect. |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The specified |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | parameter |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The erro |   |
|   |   |   |   |   | InvalidParameter |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | ServerCertificate |   |   |   | 404 |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | format is |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | error. |   |   |   |   |   |   |
|   |   |   |   | InvalidParameter |   |   |   |   |   |   |   |   |   |   | The specified |   |   |   |   | The error message returned when the certificate value is not specified. |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The specified |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | parameter |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | 404 | The |   |
|   |   |   |   |   | InvalidParameter |   |   |   | Parameter |   |   |   |   |   |   |   |   |   | 404 |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | ServerCertificate |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | Id is empty. |   |   |   |   |   |   |
|   |   |   |   | InvalidParameter |   |   |   |   |   |   |   |   |   |   | The specified |   |   |   |   | The error message returned when the specified server certificate ID is invalid. |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The specified |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | parameter |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The error me |   |
|   |   |   |   |   | InvalidParameter |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | ServerCertificate |   |   |   | 404 | th |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | Id is not |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | supported. |   |   |   |   |   |   |
|   |   |   |   | InvalidParameter |   |   |   |   |   |   |   |   |   |   | The specified |   |   |   |   | The error message returned when the values of the certificate and the private key are not specified. |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The specified |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | parameter |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The erro |   |
|   |   |   |   |   | InvalidParameter |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | ServerCertificate |   |   |   | 404 |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | or Key is |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | empty. |   |   |   |   |   |   |

|   |   |   |   |   | Error code |   |   |   |   | Error message |   | HTTP status code | Description |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   |   |   |   | The specified |   |   | The error message returned when the format of the specified private key is incorrect. |   |
|   |   |   |   |   |   |   |   |   |   |   | The specified |   | The error |   |
|   |   |   |   |   |   |   |   |   |   | parameter key |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   | 404 |   |   |
|   |   |   |   |   | InvalidParameter | InvalidParameter | Parameter |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | format is |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | error. |   |   |   |   |
|   |   |   |   |   | InvalidParameter |   |   |   |   | Specified |   |   | The error message returned when the specified region is not supported. |   |
|   |   |   |   |   |   |   |   |   |   |   | Specified |   |   |   |
|   |   |   |   |   |   | InvalidPara |   | meter |   | region is not |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   | 404 |   |   |
|   |   |   |   |   |   |   |   |   |   | supported. |   |   |   |   |
|   |   |   |   |   | InvalidParameter |   |   |   |   | Port is not Integer. |   | 400 | The error message returned when the specified port number is not an integer or is not in the range of 1 to 65535. |   |
|   |   |   |   |   | InvalidParameter |   |   |   |   | The specified |   | 400 | The error message returned when the specified port number is not an integer or is not in the range of 1 to 65535. |   |
|   |   |   |   |   |   |   |   |   |   |   | The specified |   |   |   |
|   |   |   |   |   |   | Invalid | Parameter |   |   | port is not |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | valid. |   |   |   |   |
|   |   |   |   |   | InvalidParameter |   |   |   |   | The specified |   |   | The error message returned when the specified instance bandwidth is invalid. |   |
|   |   |   |   |   |   |   |   |   |   |   | The specified |   | Th |   |
|   |   |   |   |   |   | Invalid | Parameter |   |   | bandwidth is not |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   | 400 |   |   |
|   |   |   |   |   |   |   |   |   |   | valid. |   |   |   |   |
|   |   |   |   |   | InvalidParameter |   |   |   |   | Specified |   |   | The error message returned when the specified parameter is invalid. |   |
|   |   |   |   |   |   |   |   |   |   |   | Specified |   | The |   |
|   |   |   |   |   |   | InvalidPara |   | meter |   | parameter Check |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   | 400 |   |   |
|   |   |   |   |   |   |   |   |   |   | is not valid. |   |   |   |   |
|   |   |   |   |   | InvalidParameter |   |   |   |   | The specified |   |   | The error message returned when the specified value of HealthCheckHttpCode is invalid. |   |
|   |   |   |   |   |   |   |   |   |   |   | The specified |   |   |   |
|   |   |   |   |   |   |   |   |   |   | parameter |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   | The erro |   |
|   |   |   |   |   |   | InvalidParameter |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | HealthCheckHttpCo |   | 400 |   |   |
|   |   |   |   |   |   |   |   |   |   | de is not |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | valid. |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | The specified |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | The specified |   |   |   |
|   |   |   |   |   |   |   |   |   |   | parameter |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   | The error message returned when |   |
|   |   |   |   |   |   |   |   |   |   | bandwidth is not |   |   | the specified value of Band |   |
|   |   |   |   |   | InvalidParameter | InvalidParameter |   |   |   |   |   | 400 |   |   |
|   |   |   |   |   |   |   |   |   |   | valid, out of the |   |   | exceeds |   |
|   |   |   |   |   |   |   |   |   |   | instance total |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | bandwidth. |   |   |   |   |
|   |   |   |   |   | InvalidParameter |   |   |   |   | The specified |   |   | The error message returned when the specified value of Bandwidth is invalid. |   |
|   |   |   |   |   |   |   |   |   |   |   | The specified |   | The error me |   |
|   |   |   |   |   |   |   |   |   |   | parameter |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   | 400 |   |   |
|   |   |   |   |   |   | InvalidParameter | Parameter |   |   |   |   | 400 |   |   |
|   |   |   |   |   |   |   |   |   |   | bandwidth is not |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | valid. |   |   |   |   |
|   |   |   |   |   | InvalidParameter |   |   |   |   | The specified |   |   | The error message returned when the specified health check parameter is invalid. |   |
|   |   |   |   |   |   |   |   |   |   |   | The specified |   | The error messa |   |
|   |   |   |   |   |   |   |   |   |   | parameter |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   | 400 |   |   |
|   |   |   |   |   |   | InvalidParameter | Parameter |   |   |   |   | 400 |   |   |
|   |   |   |   |   |   |   |   |   |   | HealthCheck is |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | not valid. |   |   |   |   |

|   | Port is not | 40 |
|---|---|---|
| Integer. |   |   |

|   |   |   |   | Error code |   |   |   |   | Error message |   | HTTP status code | Description |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|   |   |   |   | InvalidParameter |   |   |   |   | The specified |   |   | The error message returned when the specified value of SourceItem is invalid. |
|   |   |   |   |   |   |   |   |   |   | The specified |   | The error mess |
|   |   |   |   |   |   |   |   |   | parameter |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | 400 |   |
|   |   |   |   |   | InvalidParameter | Parameter |   |   |   |   | 400 |   |
|   |   |   |   |   |   |   |   |   | SourceItem is not |   |   |   |
|   |   |   |   |   |   |   |   |   | valid. |   |   |   |
|   |   |   |   | InvalidParameter |   |   |   |   | The specified |   |   | The error message returned when the specified protocol type is invalid. |
|   |   |   |   |   |   |   |   |   |   | The specified |   | T |
|   |   |   |   |   | Invalid | Parameter |   |   | protocol is not |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | 40 |   |
|   |   |   |   |   |   |   |   |   | valid. |   |   |   |
|   |   |   |   | InvalidParameter |   |   |   |   | RS Pool is empty. |   | 400 | The error message returned when there are no available backend servers. |
|   |   |   |   | InvalidParameter |   |   |   |   | RS Pool doesn't exist. |   | 400 | The error message returned when there are no available backend servers. |
|   |   |   |   | InvalidParameter |   |   |   |   | Illegal user ID. |   | 400 | The error message returned when the user ID is invalid. |
|   |   |   |   | InvalidParameter |   |   |   |   | User ID is null |   | 400 | The error message returned when the user ID field is empty. |
|   |   |   |   | InvalidParameter |   |   |   |   | The specified |   |   | The error message returned when the SLB instance type is invalid. |
|   |   |   |   |   |   |   |   |   |   | The specified |   | The error m |
|   |   |   |   |   | Invalid | Parameter |   |   | parameter lb type _ |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | 400 |   |
|   |   |   |   |   |   |   |   |   | is not valid. |   |   |   |
|   |   |   |   | InvalidParameter |   |   |   |   | The specified |   |   | The error message returned when the specified value of Mode is invalid. |
|   |   |   |   |   |   |   |   |   |   | The specified |   | The error |
|   |   |   |   |   | Invalid | Parameter |   |   | parameter mode is |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | 400 |   |
|   |   |   |   |   |   |   |   |   | not valid.. |   |   |   |
|   |   |   |   | InvalidParameter |   |   |   |   | The specified |   |   | The error message returned when the specified value of AccessControlStatus is invalid. |
|   |   |   |   |   |   |   |   |   |   | The specified |   |   |
|   |   |   |   |   |   |   |   |   | parameter |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   | The erro |
|   |   |   |   |   | InvalidParameter |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   | AccessControlStat |   | 400 |   |
|   |   |   |   |   |   |   |   |   | us is not |   |   |   |
|   |   |   |   |   |   |   |   |   | valid. |   |   |   |
|   |   |   |   | InvalidParameter |   |   |   |   | The specified |   |   | The error message returned when the specified value of SourceItem is invalid. |
|   |   |   |   |   |   |   |   |   |   | The specified |   | The error messa |
|   |   |   |   |   |   |   |   |   | parameter |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | 400 |   |
|   |   |   |   |   | InvalidParameter | Parameter |   |   |   |   | 400 |   |
|   |   |   |   |   |   |   |   |   | SourceItems is |   |   |   |
|   |   |   |   |   |   |   |   |   | not valid. |   |   |   |
|   |   |   |   | InvalidParameter |   |   |   |   | The specified |   |   | The error message returned when the specified value of BackendServers is invalid. |
|   |   |   |   |   |   |   |   |   |   | The specified |   | The error message |
|   |   |   |   |   |   |   |   |   | parameter |   |   | T |
|   |   |   |   |   |   |   |   |   |   |   | 404 | th |
|   |   |   |   |   | InvalidParameter | Parameter |   |   |   |   | 404 |   |
|   |   |   |   |   |   |   |   |   | BackendServers is |   |   |   |
|   |   |   |   |   |   |   |   |   | not valid. |   |   |   |
|   |   |   |   | InvalidParameter |   |   |   |   | Specified |   |   | The error message returned when the specified parameter is invalid. |
|   |   |   |   |   |   |   |   |   |   | Specified |   |   |
|   |   |   |   |   | InvalidPara |   | meter |   | parameter is not |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | 400 |   |
|   |   |   |   |   |   |   |   |   | valid. |   |   |   |

|   | RS Pool is |
|---|---|
| empty. |   |

|   | RS Pool doesn't | 400 |
|---|---|---|
| exist. |   |   |

|   | Illegal user |
|---|---|
| ID. |   |

|   | User ID is |
|---|---|
| null |   |

| erver Load Balancer |   |   | Developer Guide·API referenc |
|---|---|---|---|

|   |   |   | Error code |   |   |   | Error message |   | HTTP status code | Description |
|---|---|---|---|---|---|---|---|---|---|---|
|   |   |   | InvalidParameter |   |   |   | The specified |   |   | The error message returned when the specified value of Domain is invalid. |
|   |   |   |   |   |   |   |   | The specified |   | The error m |
|   |   |   |   | Invalid | Parameter |   | parameter Domain |   |   |   |
|   |   |   |   |   |   |   |   |   | 400 |   |
|   |   |   |   |   |   |   | is not valid. |   |   |   |
|   |   |   | InvalidParameter |   |   |   | The specified |   |   | The error message returned when the specified value of URI is invalid. |
|   |   |   |   |   |   |   |   | The specified |   | The err |
|   |   |   |   | Invalid | Parameter |   | parameter URI is |   |   |   |
|   |   |   |   |   |   |   |   |   | 400 |   |
|   |   |   |   |   |   |   | not valid. |   |   |   |
|   |   |   | InvalidParameter |   |   |   | The specified |   |   | The error message returned when the specified value of Scheduler is invalid. |
|   |   |   |   |   |   |   |   | The specified |   | The error me |
|   |   |   |   |   |   |   | parameter |   |   |   |
|   |   |   |   |   |   |   |   |   | 400 |   |
|   |   |   |   | InvalidParameter | Parameter |   |   |   | 400 |   |
|   |   |   |   |   |   |   | Scheduler is not |   |   |   |
|   |   |   |   |   |   |   | valid. |   |   |   |
|   |   |   | InvalidParameter |   |   |   | The specified |   |   | The error message returned when the specified value of ListenerStatus is invalid. |
|   |   |   |   |   |   |   |   | The specified |   | The error message |
|   |   |   |   |   |   |   | parameter |   |   | T |
|   |   |   |   |   |   |   |   |   | 400 | th |
|   |   |   |   | InvalidParameter | Parameter |   |   |   | 400 |   |
|   |   |   |   |   |   |   | ListenerStatus is |   |   |   |
|   |   |   |   |   |   |   | not valid. |   |   |   |
|   |   |   | InvalidParameter |   |   |   | The specified |   |   | The error message returned when the specified value of PersistenceTimeout is invalid. |
|   |   |   |   |   |   |   |   | The specified |   | The error message return |
|   |   |   |   |   |   |   | parameter |   |   | The err |
|   |   |   |   |   |   |   |   |   | 400 | the spe |
|   |   |   |   | InvalidParameter | Parameter |   |   |   | 400 |   |
|   |   |   |   |   |   |   | PersistenceTimeou |   |   |   |
|   |   |   |   |   |   |   | t is not valid. |   |   |   |
|   |   |   | InvalidParameter |   |   |   | The specified |   |   | The error message returned when the specified value of ConnectPort is invalid. |
|   |   |   |   |   |   |   |   | The specified |   | The error messa |
|   |   |   |   |   |   |   | parameter |   |   |   |
|   |   |   |   |   |   |   |   |   | 400 |   |
|   |   |   |   | InvalidParameter | Parameter |   |   |   | 400 |   |
|   |   |   |   |   |   |   | ConnectPort is |   |   |   |
|   |   |   |   |   |   |   | not valid. |   |   |   |
|   |   |   | InvalidParameter |   |   |   | The specified |   |   | The error message returned when the specified value of ConnectTimeout is invalid. |
|   |   |   |   |   |   |   |   | The specified |   | The error messag |
|   |   |   |   |   |   |   | parameter |   |   | T |
|   |   |   |   |   |   |   |   |   | 400 | t |
|   |   |   |   | InvalidParameter | Parameter |   |   |   | 400 |   |
|   |   |   |   |   |   |   | ConnectTimeou is |   |   |   |
|   |   |   |   |   |   |   | not valid. |   |   |   |
|   |   |   | InvalidParameter |   |   |   | The specified |   |   | The error message returned when the specified value of StickySessionType is invalid. |
|   |   |   |   |   |   |   |   | The specified |   | The error message retu |
|   |   |   |   |   |   |   | parameter |   |   | The e |
|   |   |   |   |   |   |   |   |   | 400 | the s |
|   |   |   |   | InvalidParameter | Parameter |   |   |   | 400 |   |
|   |   |   |   |   |   |   | StickySessionType |   |   |   |
|   |   |   |   |   |   |   | is not valid. |   |   |   |
|   |   |   | InvalidParameter |   |   |   | The specified |   |   | The error message returned when the specified value of HealthyThreshold is invalid. |
|   |   |   |   |   |   |   |   | The specified |   | The error message ret |
|   |   |   |   |   |   |   | parameter |   |   | The |
|   |   |   |   |   |   |   |   |   | 400 | the |
|   |   |   |   | InvalidParameter | Parameter |   |   |   | 400 |   |
|   |   |   |   |   |   |   | HealthyThreshold |   |   |   |
|   |   |   |   |   |   |   | is not valid. |   |   |   |
|   |   |   | InvalidParameter |   |   |   | The specified |   |   | The error message returned when the specified value of UnhealthyThreshold is invalid. |
|   |   |   |   |   |   |   |   | The specified |   | The error message return |
|   |   |   |   |   |   |   | parameter |   |   | The err |
|   |   |   |   |   |   |   |   |   | 400 | the spe |
|   |   |   |   | InvalidParameter | Parameter |   |   |   | 400 |   |
|   |   |   |   |   |   |   | UnhealthyThreshol |   |   |   |
|   |   |   |   |   |   |   | d is not valid. |   |   |   |

|   |   |   |   |   |   | Error code |   |   |   |   |   |   |   |   | Error message |   |   |   |   | HTTP status code | Description |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   | InvalidParameter |   |   |   |   |   |   |   |   | The specified |   |   |   |   |   | The error message returned when the specified value of Interval is invalid. |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The specified |   |   |   |   | The error m |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | parameter |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | 400 |   |   |
|   |   |   |   |   |   |   | InvalidParameter |   |   | Parameter |   |   |   |   |   |   |   |   |   | 40 |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | Interval is not |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | valid. |   |   |   |   |   |   |   |
|   |   |   |   |   |   | InvalidParameter |   |   |   |   |   |   |   |   | The specified |   |   |   |   |   | The error message returned when the specified value of XForwardedFor is invalid. |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The specified |   |   |   |   | The error messag |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | parameter |   |   |   |   |   | T |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | 400 | t |   |
|   |   |   |   |   |   |   | InvalidParameter |   |   | Parameter |   |   |   |   |   |   |   |   |   | 400 |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | XForwardedFor is |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | not valid. |   |   |   |   |   |   |   |
|   |   |   |   |   |   | InvalidParameter |   |   |   |   |   |   |   |   | The specified |   |   |   |   |   | The error message returned when the specified value of IsPublicAddress is invalid. |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The specified |   |   |   |   | The error message r |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | parameter |   |   |   |   |   | Th |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | 400 | the |   |
|   |   |   |   |   |   |   | InvalidParameter |   |   | Parameter |   |   |   |   |   |   |   |   |   | 400 |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | IsPublicAddress |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | is not valid. |   |   |   |   |   |   |   |
|   |   |   |   |   |   | InvalidRegionId.No tFound |   |   |   |   |   |   |   |   | Specified region does not exist. |   |   |   |   | 404 | The error message returned when the specified region does not exist. |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | A specified |   |   |   |   |   | The error message returned when the specified backend server ID is invalid. |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | A specified |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | serv |   |   |   | er ID is not |   | The error messag |   |
|   |   |   |   |   |   |   | InvalidServerId.Ma |   |   |   | rverId.Ma |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | vali |   |   |   |   | 400 |   |   |
|   |   |   |   |   |   | lformed |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | control ip chain |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | fail. |   |   |   |   |   |   |   |
|   |   |   |   |   |   | InvalidServerId.No |   |   |   |   |   |   |   |   | The specified |   |   |   |   |   | The error message returned when the specified backend server does not exist. |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The specified |   |   |   |   |   |   |
|   |   |   |   |   |   |   | InvalidServerId.No |   |   |   |   |   |   |   |   | Th |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | ServerId.No |   |   |   |   | ser |   |   |   |   |   |   |   |
|   |   |   |   |   |   | tFound |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | found. |   |   |   |   |   |   |   |
|   |   |   |   |   |   | InvalidWeight.Malf |   |   |   |   |   |   |   |   | A specified |   |   |   |   | 400 | The error message returned when the specified value of weight is invalid. |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | A specified |   |   |   |   |   |   |
|   |   |   |   |   |   |   | InvalidWeight.Malf |   |   |   |   |   |   |   |   | A |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | ight.Malf |   |   |   | we |   |   |   |   |   |   |   |
|   |   |   |   |   |   | ormed |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | valid. |   |   |   |   |   |   |   |
|   |   |   |   |   |   | IpNotAvailable |   |   |   |   |   |   |   |   | The specified |   |   |   |   |   | The error message returned when the specified value of Address is invalid. |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The specified |   |   |   |   | The error m |   |
|   |   |   |   |   |   |   | IpNotAv |   |   | ailable |   |   |   |   | parameter Address |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | 400 |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | is not valid. |   |   |   |   |   |   |   |
|   |   |   |   |   |   | ListenerAlreadyExi |   |   |   |   |   |   |   |   | There is |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | There is |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | already a |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The error message returned when |   |
|   |   |   |   |   |   |   | Lis | tenerAlreadyExi |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | listener bound to |   |   |   |   | there is already a listene |   |
|   |   |   |   |   |   | sts |   |   |   |   |   |   |   |   |   |   |   |   |   | 400 |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | the port on the |   |   |   |   |   | the |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | specified load |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | balancer. |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | No Listener to |   |   |   |   |   | The error message returned when the specified listener does not exist. |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | No Listener to |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | the specified |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | 404 | The |   |
|   |   |   |   |   |   | ListenerNotFound | ListenerNotFound |   |   | rNotFound |   |   |   |   |   |   |   |   |   | 404 |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | port of the Load |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | Balancer. |   |   |   |   |   |   |   |

| InvalidRegionId.No | Spe |
|---|---|

|   |   |   |   | Error code |   |   |   |   |   | Error message |   | HTTP status code | Description |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   |   |   |   | The input |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | The input |   |   |   |
|   |   |   |   |   |   |   |   |   |   | parameter Cookie |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   | The error message returned when |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   | The error message returned w |   |
|   |   |   |   |   |   |   |   |   |   | that is mandatory |   |   | the Cookie parameter is not |   |
|   |   |   |   |   | MissingParameter |   |   |   |   |   |   | 400 | the Cook |   |
|   |   |   |   |   |   |   |   |   |   | for processing |   |   | specified |   |
|   |   |   |   |   |   |   |   |   |   | this request is |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | not supplied. |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | The input |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | The input |   |   |   |
|   |   |   |   |   |   |   |   |   |   | parameter |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | BackendServerPort |   |   | The error message returned when |   |
|   |   |   |   |   | MissingParameter |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | that is mandatory |   | 400 | the BackendServerPort param |   |
|   |   |   |   |   |   |   |   |   |   | for processing |   |   | not speci |   |
|   |   |   |   |   |   |   |   |   |   | this request is |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | not supplied. |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | The input |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | The input |   |   |   |
|   |   |   |   |   |   |   |   |   |   | parameter |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | LoadBalancerId |   |   | The error message returned when |   |
|   |   |   |   |   | MissingParameter |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | that is mandatory |   | 400 | the LoadBalancerId paramete |   |
|   |   |   |   |   |   |   |   |   |   | for processing |   |   | specified |   |
|   |   |   |   |   |   |   |   |   |   | this request is |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | not supplied. |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | The input |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | The input |   |   |   |
|   |   |   |   |   |   |   |   |   |   | parameter |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | RegionId that is |   |   | The error message returned when |   |
|   |   |   |   |   | MissingParameter |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | mandatory for |   | 400 | the RegionId param |   |
|   |   |   |   |   |   |   |   |   |   | processing this |   |   | spec |   |
|   |   |   |   |   |   |   |   |   |   | request is not |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | supplied. |   |   |   |   |
|   |   |   |   | MissingParameter |   |   |   |   |   | The combination |   |   | The error message returned when a required parameter is not specified. |   |
|   |   |   |   |   |   |   |   |   |   |   | The combination |   |   |   |
|   |   |   |   |   |   |   |   |   |   | of some |   |   |   |   |
|   |   |   |   |   | MissingParameter |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | parameters |   | 400 |   |   |
|   |   |   |   |   |   |   |   |   |   | violates the |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | spec. |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | The input |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | The input |   |   |   |
|   |   |   |   |   |   |   |   |   |   | parameter |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | OwnerId,OwnerAcco |   |   | The error message returned when |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   | The error message returned whe |   |
|   |   |   |   |   |   |   |   |   |   | unt that is |   |   | OwnerAccount and OwnerId are n |   |
|   |   |   |   |   | MissingParameter |   |   |   |   |   |   | 403 | OwnerAccount and |   |
|   |   |   |   |   |   |   |   |   |   | mandatory for |   |   | specified. |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   | spec |   |
|   |   |   |   |   |   |   |   |   |   | processing this |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | request is not |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | supplied. |   |   |   |   |
|   |   |   |   | PrivateKeyEncrypti on |   |   |   |   |   | Key has Encrypted . |   | 400 | The error message returned when the private key is encrypted. |   |

| PrivateKeyEncrypti |   |   | Key has | 4 |
|---|---|---|---|---|

|   |   |   |   |   |   | Error code |   |   |   |   |   |   |   |   |   |   |   |   | Error message |   |   |   | HTTP status code | Description |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   | ProcessingSameRequ |   |   |   |   |   |   |   |   |   |   |   |   | The same |   |   |   |   | The error message returned when the same request is being processed. You can try again later. |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The same |   |   |   | The error message ret |   |
|   |   |   |   |   |   |   |   | ProcessingSa |   |   |   |   |   |   |   | meRequ |   |   |   |   |   |   |   | The error |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | request is being |   |   | 400 | the same |   |
|   |   |   |   |   |   | est |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | 400 |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | processed. Please |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | try later. |   |   |   |   |   |   |
|   |   |   |   |   |   | ServerCertificateI |   |   |   |   |   |   |   |   |   |   |   |   | Specified |   |   |   |   | The error message returned when the specified certificate does not exist. |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | Specified |   |   |   | The error m |   |
|   |   |   |   |   |   |   |   | ServerCerti |   |   |   |   |   |   | ficateI |   |   |   | ServerCe |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | rtificate | 404 |   |   |
|   |   |   |   |   |   | d.NotFound |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | Id does not |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | exist. |   |   |   |   |   |   |
|   |   |   |   |   |   | ServiceUnavailable |   |   |   |   |   |   |   |   |   |   |   |   | The request has |   |   |   |   | The error message returned when the service is unavailable. |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The request has |   |   |   |   |   |
|   |   |   |   |   |   |   |   | Servic |   |   |   | eUnavailable |   |   |   |   |   |   | failed due to a |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | 503 | The error mes |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | 503 |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | temporary failure |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | of the server. |   |   |   |   |   |   |
|   |   |   |   |   |   | ServiceUnavailable |   |   |   |   |   |   |   |   |   |   |   |   | The specified |   |   |   |   | The error message returned when the specified instance name is already being used. |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The specified |   |   |   | The error mes |   |
|   |   |   |   |   |   |   |   | ServiceUnavailable |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   | Unavailable |   |   |   |   |   | loadbalancer name |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | 503 |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | has been used. |   |   |   |   |   |   |
|   |   |   |   |   |   | TcpNotSupportForHy |   |   |   |   |   |   |   |   |   |   |   |   | Hybrid type |   |   |   |   | The error message returned when a TCP listener cannot be created. |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | Hybrid type |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | loa |   | dbalancer |   |   | The error m |   |
|   |   |   |   |   |   |   |   | TcpNotSupportForHy |   |   |   |   |   | ortForHy |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | doe |   |   |   | 400 |   |   |
|   |   |   |   |   |   | bridLb | bridLb |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | TCP type |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | listener. |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The total |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The total |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | number of input |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The error message returned |   |
|   |   |   |   |   |   |   |   | TooManyBackendServ |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The error |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | real servers |   |   | 400 | you are try |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | 400 |   |   |
|   |   |   |   |   |   | ers |   |   |   |   |   |   |   |   |   |   |   |   | exceeds max |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | supported number: |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | 20. |   |   |   |   |   |   |
|   |   |   |   |   |   | TooManyBackendServ |   |   |   |   |   |   |   |   |   |   |   |   | The backend |   |   |   |   | The error message returned when the specified number of backend servers exceeds the limit. |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The backend |   |   |   | The error messag |   |
|   |   |   |   |   |   |   |   | TooManyBac |   |   |   |   |   | kendServ |   |   |   |   |   |   |   |   |   | T |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | server parameter |   |   | 400 | th |   |
|   |   |   |   |   |   | ers |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | 4 |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | has too many |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | entries. |   |   |   |   |   |   |
|   |   |   |   |   |   | UnsupportedOperati on |   |   |   |   |   |   |   |   |   |   |   |   | The |   |   |   |   | The error message returned when the SLB instance does not support the operation. |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The |   |   |   | The error mes |   |
|   |   |   |   |   |   |   |   | UnsupportedOperat |   |   |   |   |   |   |   |   | i |   |   |   |   |   |   | The erro |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | Loadbalancer |   |   | 400 | the SLB |   |
|   |   |   |   |   |   | on |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | 400 |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | doesn't support |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | this function. |   |   |   |   |   |   |
|   |   |   |   |   |   | UnsupportedOperati |   |   |   |   |   |   |   |   |   |   |   |   | The specified |   |   |   |   | The error message returned when the specified operation is not supported. |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The specified |   |   |   | The |   |
|   |   |   |   |   |   |   |   | UnsupportedOperati |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   | rtedOperati |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | 400 |   |   |
|   |   |   |   |   |   | on |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | supported. |   |   |   |   |   |   |

|   |   |   |   |   | Error code |   |   |   |   |   |   |   |   |   |   |   | Error message |   | HTTP status code | Description |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The specified |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The specified |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | port has been |   |   |   |   |
|   |   |   |   |   |   |   | UnsupportedOperati |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | assigned one type |   |   | The error message returned when |   |
|   |   |   |   |   | ononfixedprotocolpor |   |   |   |   |   |   |   |   |   |   |   | of protocol, and |   | 400 | the specified port does not s |   |
|   |   |   |   |   | t |   |   |   |   |   |   |   |   |   |   |   | this protocol |   |   | the operat |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | doesn't support |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | this operation. |   |   |   |   |
|   |   |   |   |   | UnsupportedParamet er |   |   |   |   |   |   |   |   |   |   |   | The parameter is not supported. |   | 400 | The error message returned when the input parameter is not supported. |   |
|   |   |   |   |   | VipNotMatchRspool |   |   |   |   |   |   |   |   |   |   |   | The vip |   |   | The error message returned when the protocol type of the listener and the application protocol of the backend server do not match. |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The vip |   | The err |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | protocol is not |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | 400 |   |   |
|   |   |   |   |   |   |   | VipNotMatchRspool |   |   |   |   |   | pool |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | match with |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | Rspool. |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The total |   |   | The error message returned when you are trying to add more than 50 listeners at a time. |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The total |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | number of input |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The error message return |   |
|   |   |   |   |   |   |   |   |   |   |   |   | istener |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | listeners exceeds |   | 400 | you are |   |
|   |   |   |   |   | s |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | max supported |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | number: 50. |   |   |   |   |
|   |   |   |   |   | InvalidParameter |   |   |   |   |   |   |   |   |   |   |   | The specified |   |   | The error message returned when the specified resource does not exist. |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The specified |   | The |   |
|   |   |   |   |   |   |   | Invalid |   |   |   | Parameter |   |   |   |   |   | resource does not |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | 400 |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | exist. |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The specified |   |   | The error message returned when the specified instance is currently under configuration. You can try again later. |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The specified |   | The error message returned w |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | loadbalancer is |   |   | The error me |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | the specified |   |
|   |   |   |   |   |   |   |   |   |   |   | Unavailable |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | configuring, |   | 503 |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | please retry |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | later. |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | Obtain Ip Fail, |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | Obtain Ip Fail, |   | The error message returned when |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | please make sure |   |   | The error message retur |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | the IP address cannot be |   |
|   |   |   |   |   |   |   |   |   |   | ceUnavailable |   |   |   |   |   |   |   |   |   | the IP |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | the ECS exists |   | 503 | Verify |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | and the status is |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | running. |   |   |   |   |
|   |   |   |   |   | ServiceUnavailable |   |   |   |   |   |   |   |   |   |   |   | The specified |   |   | The error message returned when the specified region does not support VPCs. |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The specified |   | Th |   |
|   |   |   |   |   |   |   | ServiceUnavailable |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | Unavailable |   |   |   |   |   | region not |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | 503 |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | support VPC. |   |   |   |   |
|   |   |   |   |   | InvalidParameter |   |   |   |   |   |   |   |   |   |   |   | The specified |   |   | The error message returned when the specified VPC instance has been deleted. |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The specified |   | The error messag |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | vpc cloud |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | 400 |   |   |
|   |   |   |   |   |   |   | InvalidParameter |   |   |   | Parameter |   |   |   |   |   |   |   | 400 |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | instance has been |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | deleted. |   |   |   |   |

|   |   |   |   | The parameter |   |
|---|---|---|---|---|---|
| UnsupportedParamet |   |   |   |   |   |
|   |   | rtedParamet |   |   |   |
|   |   |   | supported. |   |   |
