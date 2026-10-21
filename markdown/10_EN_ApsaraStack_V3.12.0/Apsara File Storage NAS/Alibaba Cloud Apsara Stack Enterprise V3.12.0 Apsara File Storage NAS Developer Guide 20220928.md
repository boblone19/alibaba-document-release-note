---
title: "Alibaba Cloud Apsara Stack Enterprise V3.12.0 Apsara File Storage NAS Developer Guide 20220928"
product_version: "V3.12.0"
doc_version: "20220928"
pdf_pages: 47
source_pdf: "Alibaba Cloud Apsara Stack Enterprise V3.12.0 Apsara File Storage NAS Developer Guide 20220928.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/01_ApsaraStackEnterprise/V3.12/%E5%AD%98%E5%82%A8/Alibaba%20Cloud%20Apsara%20Stack%20Enterprise%20V3.12.0%20Apsara%20File%20Storage%20NAS%20Developer%20Guide%2020220928.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes)
---

# Alibaba Cloud Apsara Stack Enterprise V3.12.0 Apsara File Storage NAS Developer Guide 20220928

## Table of Contents

- 1 Use ASAPI to call the Apsara Stack SDK
  - 1.1 Overview
  - 1.2 Log on to the API Tool console
  - 1.3 View the information about API operations
  - 1.4 Obtain the endpoint of ASAPI
  - 1.5 Obtain the core package for ASAPI
  - 1.6 Obtain an AccessKey pair
  - 1.7 Query the region ID
  - 1.8 SDK for Java
  - 1.9 SDK for Node.js
  - 1.10. (Optional) Use POP SDK to call ASAPI API operations
- 2 API reference
  - 2.1 List of operations by function
  - 2.2 Make API requests
    - 2.2.1 Common parameters
    - 2.2.2 Structure of a request
  - 2.3 Region
    - 2.3.1 DescribeRegions
  - 2.4 NAS instance
    - 2.4.1 CreateFileSystem
    - 2.4.2 DeleteFileSystem
    - 2.4.3 DescribeFileSystems
    - 2.4.4 ModifyFileSystem
  - 2.5 Mount point
    - 2.5.1 CreateMountTarget
    - 2.5.2 DeleteMountTarget
    - 2.5.3 DescribeMountTargets
    - 2.5.4 ModifyMountTarget
  - 2.6 Permission group
    - 2.6.1 CreateAccessGroup
    - 2.6.2 CreateAccessRule
    - 2.6.3 DeleteAccessGroup
    - 2.6.4 DeleteAccessRule
    - 2.6.5 DescribeAccessGroups
    - 2.6.6 DescribeAccessRules
    - 2.6.7 ModifyAccessGroup
    - 2.6.8 ModifyAccessRule
  - 2.7 Appendix: Error codes

he Apsara Stack SDK

## 1 Use ASAPI to call the Apsara Stack SDK

Stack SDK

### 1.1 Overview

This topic describes the architecture and features of Apsara Stack API (ASAPI). ASAPI is a platform that integrates all features and is the only portal to connect to Apsara Stack. ASAPI can categorize, audit, and manage API operations. It can also assemble and customize existing operations and adapt to your operations. Each cloud service can call ASAPI for required data and features, which avoids inconsistent operations caused by different calling methods and separate encapsulation. This can ensure the operation program integrity and improve development efficiency and code portability. ASAPI allows you to manage and call operations in a centralized manner and customize development. ASAPI supports access to most cloud services deployed in Apsara Stack and supports passthrough or encapsulation of different backend APIs. This way, operations can be called using the same method. ASAPI allows you to use SDKs and API portals to call APIs registered on ASAPI, customize SDKs, and manage versions of Apsara Stack, services, and APIs. he Apsara Stack SDK

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
operation name in the search box, and then click the search icon. he Apsara Stack SDK
4. View and remember the service name, API operation name, and API version.

### 1.4 Obtain the endpoint of ASAPI

This topic describes how to obtain the endpoint of ASAPI in the Apsara Stack Operations console. Procedure
1. In the address bar, enter the URL region-id.aso.intranet-domain-id.com and press the Enter key.
Not e You can select a language from the drop-down list in the upper-right corner of the page.
2. Enter your username and password.
Not e Obtain the username and password for logging on to the ASO console from the deployment personnel or an administrator. When you log on to the ASO console for the first time, you must change the password of your username as prompted. To enhance security, a password must meet the following requirements: It must contain uppercase and lowercase letters. It must contain digits. It must contain special characters such as exclamation points (!), at signs (@), number signs (#), he Apsara Stack SDK dollar signs ($), and percent signs (%). It must be 10 to 20 characters in length.
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
ASAPI Management platform. he Apsara Stack SDK

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
he Apsara Stack SDK Not e An AccessKey pair is automatically allocated to a level-1 organization. Subordinate organizations use the same AccessKey pair as their level-1 organization. Obtain the AccessKey pair of a personal account To obtain the AccessKey pair of a personal account, perform the following operations:
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

This topic describes how to obtain and use Virtual Private Cloud (VPC) SDK for Java. Preparation You must have an authorized account and an AccessKey pair (AccessKey ID and AccessKey secret) to use VPC SDK for Java. For more information about how to obtain and view your AccessKey pair in the ASCM console, see Obtain an AccessKey pair. You have obtained the endpoint of Apsara Stack API (ASAPI). For more information about how to obtain the endpoint of ASAPI, see Obtain the endpoint of Asapi. he Apsara Stack SDK The version of VPC SDK for Java is JDK 1.6 or later. Add the dependency Add the dependency to pom.xml:

```xml
<dependency>
    <groupId>com.aliyun</groupId>
    <artifactId>asapi</artifactId>
    <version>0.0.1-SNAPSHOT</version>
    <scope>system</scope>
    <systemPath>${project.basedir}/lib/aliyun-java-sdk-asapi.jar</systemPath>
</dependency>
```

Use SDK for Java You can call ASAPI API operations by sending GET and POST requests. GET requests

```
 ASClient client = new ASClient();
// Form 1 String result = client.doGet(endpoint, parameters); // Form 2 String result = client.doRequest(endpoint, parameters);
```

POST requests he Apsara Stack SDK

```java
public class DescribeVpcs {
    public static void main(String[] args) {
        // Set the endpoint of ASAPI.
        String endpoint = "http://xxx/asapi/v3";
    // Set request parameters.
    Map<String, String> parameters = new HashMap<String, String>();
    // Set product parameters.
    parameters.put("Product", "vpc");            //The product name, which must be the sa
me as that displayed on the APIs page.
    parameters.put("Action", "DescribeVpcs");          // The API operation, which is cas
e-sensitive and must be the same as that on the APIs page.
    parameters.put("Version", "2016-04-28");      // The API version.
    // Set authorization parameters.
    parameters.put("AccessKeyId", "<your-access-key-id>");          // The AccessKey ID o
f the authorized account.
    parameters.put("AccessKeySecret", "<your-access-key-secret>");  // The AccessKey secr
et of the authorized account.
    // Set service parameters.
    parameters.put("username", "<your-username>");                  // The username used
to log on to the ASCM console.
    parameters.put("password", "<your-password>");                  // The password used
to log on to the ASCM console.
    JSONObject jsonObject = new JSONObject();
    jsonObject.put("RegionId", "cn-hangzhou-env12-d01");
    parameters.put("json", jsonObject.toJSONString());
    // Create an ASClient instance for initiating requests.
    ASClient client = new ASClient();
    // Add the request header.
    client.addHeader("x-acs-resourceGroupId", "112233");
    // Initiate the request and obtain the response.
    String result = client.doPost(endpoint, parameters);
```

### 1.9 SDK for Node.js

This topic describes how to obtain and use Virtual Private Cloud (VPC) SDK for Node.js. Preparation You must have an authorized account and an AccessKey pair (AccessKey ID and AccessKey secret) to use VPC SDK for Node.js. For more information, see Obtain an AccessKey pair. You have obtained the endpoint of Apsara Stack API (ASAPI). For more information about how to obtain the endpoint of ASAPI, see Obtain the endpoint of Asapi. You have obtained the region ID. For more information about how to query the region ID, see Query the region ID. Add the dependency
1. Install SDK for Node.js.

```
 tnpm install --save @ali/asapi-nodejs-sdk
```

2. If mocha.opts depends on Egg.js, configure mocha.opts as follows:
he Apsara Stack SDK

```
--recursive --colors --timeout 60000 --reporter mochawesome --require co-mocha --require egg-ts-helper/register --require espower-typescript/guess --require intelli-espower-loader
```

Use SDK for Node.js The following example shows the three main steps of calling SDK for Node.js:
1. Create an ASClient instance. When you create an ASClient instance, set the region ID, endpoint,
AccessKey ID, and AccessKey secret in the config.ts file. Example:

```
local: {
    regionId: 'obtained region ID',
    API_GATEWAY: 'obtained endpoint',
    accessKeyId: 'your AccessKey ID',
    accessKeySecret: 'your AccessKey secret',
```

`},`
2. Create an API request and configure the parameters.
3. Initiate the request and handle the responses or exceptions.

```
// Set the endpoint of ASAPI. const API_GATEWAY = "http://xxxx/asapi/v3" // Create an RPC client. const asapiClient = ctx.service.sdk.rpcClient; // Set request parameters. let params = {
    Action: 'DescribeVpcs',
    Product: 'vpc',
    regionId: 'cn-hangzhou-env12-d01',
    accessKeyId: 'xxxxxxx',
    accessKeySecret: 'xxxxxxx',
    Version: '2016-04-28'
```

};

```
// Set parameters in the request header. asapiClient.addHeader("x-acs-regionId", "cn-hangzhou-env12-d01"); // Initiate the request and obtain the response. const result = await asapiClient.doRequest(API_GATEWAY, params, {});
```

1.10. (Optional) Use POP SDK to call ASAPI API operations If an application used POP SDK to call Virtual Private Cloud (VPC), you must switch the gateway to Apsara Stack API (ASAPI). Procedure he Apsara Stack SDK
1. Switch the gateway to ASAPI and add common parameters required by the API operation to the
request header.
2. Add the Product Name field to the request header.
Example The following code provides an example on how to use POP SDK to call VPC OpenAPI.

```java
try {
    DefaultProfile clientProfile = DefaultProfile.getProfile(regionId, accessKeyId, accessK
eySecret);
    // Set the ASAPI gateway. Format: server.asapi.${intranet-domain}.
    clientProfile.addEndpoint(region, region, "vpc", "<ASAPI gateway>");
    DefaultAcsClient acsClient = new DefaultAcsClient(clientProfile);
    DescribeVpcsRequest request = new DescribeVpcsRequest();
    request.setSysRegionId(regionId); // Or setRegionId(regionId)
    // Set common parameters based on the information about the current user.
    request.putHeaderParameter("x-acs-organizationid", "<Department ID>");
    request.putHeaderParameter("x-acs-resourcegroupid", "<Resource group ID>");
    DescribeVpcsResponse result = (DescribeVpcsResponse) acsClient.getAcsResponse(request);
    System.out.println(result);
} catch (Exception e) {
    e.printStackTrace();
```

## 2 API reference

### 2.1 List of operations by function

lists the APIs provided by NAS. APIs

| Number | Category | API | Description |
|---|---|---|---|
| 1 | Region | DescribeRegions | Returns all region IDs. |
| 2 | NAS | CreateFileSystem | Creates a NAS instance. |
| 3 | NAS | DeleteFileSystem | Deletes an existing NAS instance. |
| 4 | NAS | DescribeFileSystems | Returns the description of a NAS instance. |
| 5 | NAS | ModifyFileSystem | Modifies the information of a NAS instance. |
| 6 | Mount point | CreateMountTarget | Create a mount point. |
| 7 | Mount point | DeleteMountTarget | Deletes an existing mount point. |
| 8 | Mount point | DescribeMountTargets | Returns the description of a mount point. |
| 9 | Mount point | ModifyMountTarget | Modifies the attributes of a mount point. |
| 10 | Permission group | CreateAccessGroup | Creates a permission group. |
| 11 | Permission group | DeleteAccessGroup | Deletes an existing permission group. |
| 12 | Permission group | DescribeAccessGroups | Returns the description of a permission group. |
| 13 | Permission group | ModifyAccessGroup | Modifies the attributes of a permission group. |
| 14 | Permission group | CreateAccessRule | Creates a permission rule. |
| 15 | Permission group | DeleteAccessRule | Deletes an existing permission rule. |

| Number | Category | API | Description |
|---|---|---|---|
| 16 | Permission group | DescribeAccessRules | Returns the description of a permission rule. |
| 17 | Permission group | ModifyAccessRule | Modifies the attributes of a permission rule. |

### 2.2 Make API requests

#### 2.2.1 Common parameters

Common request parameters Common request parameters are available to all APIs. Common request parameters

| Name | Type | Required | Description |   |   |
|---|---|---|---|---|---|
| Format | String | No | The type of response. Valid values: JSON and XML. Default value: JSON. |   |   |
| Version | String | Yes | The API version, which is represented as a date in the format of YYYY-MM-DD . The current API version is 2017-06-26. |   |   |
| AccessKeyId | String | Yes | The AccessKey ID that is used to access services. For more information, see Obtain an AccessKey pair. |   |   |
| Signature | String | Yes | The string that represents signature. |   |   |
| SignatureMethod | String | Yes | The type of signature. Valid value: HMAC-SHA1. |   |   |
| Timestamp | String | Yes | The time when you send the request. Specify the time in the ISO 8601 standard in the YYYY- MM-DDThh:mm:ssZ format. The time must be in UTC. For example, 2017-05-26T12:00:00Z. |   |   |
|   |   |   |   | YYYY- |   |
| SignatureVersion | String | Yes | The version of the signature algorithm. The current version is 1.0. |   |   |

|   | MM-DDThh:mm:ssZ |
|---|---|

| Name | Type | Required | Description |
|---|---|---|---|
| SecurityToken | String | No | If Security Token Service (STS) credentials are required, you must specify this parameter. |
| SignatureNonce | String | No | A unique random number. This parameter is used to prevent replay attacks. You must use different random numbers for different requests. |

Sample request

```
GET https://nas.regionid.example.com/?Action=<Action> &Format=xml &Version=2017-06-26 &AccessKeyId=key-test &Signature=Pc5***%3D &SignatureMethod=HMAC-SHA1 &SignatureNonce=15215528852396 &SignatureVersion=1.0 &Timestamp=2012-06-01T12:00:00Z
```

Common response parameters Whenever you send an API request, a GUID that is included in the Request Id parameter will be returned to you regardless of whether the request is successful. Common response parameters

| Name | Type | Description |
|---|---|---|
| RequestId | Integer | The GUID generated by Alibaba Cloud for the request. |

Sample response

```xml
<An API name+Response>
  <! --Returned RequestId-->
  <RequestId> 6D9F62C5-BF52-447C-AA34-C77F7AFCCC12</RequestId>
  <! --Response parameters-->
</An API name+Response>
```

```json
  "RequestId": "4C467B38-3910-447D-87BC-AC049166F216",
  /* Response parameters*/
```

#### 2.2.2 Structure of a request

Endpoints The format of a NAS API endpoint is as follows:Generate the endpoint of ASAPI Protocols You can send API requests by using HTTP or HTTPS. We recommend that you use HTTPS to ensure high security. Request methods You can send requests by using the HTTP GET method. With this method, you must specify request parameters in the request URL. You must specify the required operation for the Action parameter of each request, such as `DescribeRegions` . Each operation must include common request parameters and other request parameters that are specific to an operation. Character encoding Requests or responses are all encoded by `UTF-8` .

### 2.3 Region

#### 2.3.1 DescribeRegions

Return all region IDs.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | TRUE | The operation that you want to perform. Set the value to DescribeRegions . |
| PageSize | Integer | FALSE | The number of regions that are displayed on each page. Default value: 10. |

| psara File Storage NAS |   | De | veloper Guide·API referenc |
|---|---|---|---|

| Parameter | Type | Required | Description |
|---|---|---|---|
| PageNumber | Integer | FALSE | The page number of the list, which starts from 1. |

| Parameter | Type | Description |
|---|---|---|
| TotalCount | Integer | The total number of returned region information records |
| PageSize | Integer | The number of regions that are displayed on each page |
| PageNumber | Integer | The page number of the list |
| Regions | RegionType | The region description |

Sample requests

```
GET https://nas.regionid.example.com/?Action=DescribeRegions &PageSize=2 &PageNumber=1
```

Sample responses

```xml
<DescribeRegionsResponse>
  <PageNumber>1</PageNumber>
  <TotalCount>4</TotalCount>
  <PageSize>2</PageSize>
  <RequestId>A70BEE5D-76D3-49FB-B58F-1F398211A5C3</RequestId>
  <Regions>
    <Region>
      <RegionId>cn-hangzhou</RegionId>
      <LocalName>China (Hangzhou)</LocalName>
    </Region>
    <Region>
      <RegionId>cn-shanghai</RegionId>
      <LocalName>China (Shanghai)</LocalName>
    </Region>
  </Regions>
</DescribeRegionsResponse>
```

```json
  "TotalCount": 4,
  "PageSize": 2,
  "RequestId": "A70BEE5D-76D3-49FB-B58F-1F398211A5C3",
  "PageNumber": 1,
  "Regions": {
    "Region": [
        "RegionId":"cn-hangzhou",
        "LocalName": "China (Hangzhou)"
```

`},`

```json
        "RegionId": "cn-shanghai",
        "LocalName": "China (Shanghai)"
```

`]`

### 2.4 NAS instance

#### 2.4.1 CreateFileSystem

You can call this operation to create a file system.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set this value to CreateFileSystem . |
| StorageType | String | Yes | The type of the file system. Valid values: Performance and Capacity. |
| ProtocolType | String | Yes | The type of protocol used by the file system. |
| Description | String | No | The description of the file system. Space ( ) characters are not allowed. |

| Name | Type | Required | Description |
|---|---|---|---|
| VolumeSize | Long | No | The size of the file system to be created. Not e If you do not specify a value for this parameter, the default size of a Performance-type file system is 10 PB and the default size of a Capacity- type file system is 1 PB. |

| Name | Type | Description |
|---|---|---|
| FileSystemId | String | The new file system ID. |

Sample request

```
GET https://nas.regionid.example.com/?Action=CreateFileSystem &StorageType=Performance &ProtocolType=NFS &Description=balabala
```

Sample response

```json
<CreateFileSystemResponse>
  <FileSystemId>1ca404a666</FileSystemId>
  <RequestId>98696EF0-1607-4E9D-B01D-F20930B68845</RequestId>
</CreateFileSystemResponse>
  "RequestId": "98696EF0-1607-4E9D-B01D-F20930B68845",
  "FileSystemId": "1ca404a666"
```

#### 2.4.2 DeleteFileSystem

You can call this operation to delete an existing NAS instance.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | TRUE | The operation that you want to perform. Set the value to DeleteFileSystem . |
| FileSystemId | String | TRUE | The ID of the NAS instance to be deleted. |

None Sample requests

```
GET https://nas.regionid.example.com/?Action=DeleteFileSystem &FileSystemId=1ca404a348
```

Sample responses

```xml
<DeleteFileSystemResponse>
  <RequestId>9E15E394-38A6-457A-A62A-D9797C9A0262</RequestId>
</DeleteFileSystemResponse>
```

```json
  "RequestId": "9E15E394-38A6-457A-A62A-D9797C9A0262"
```

#### 2.4.3 DescribeFileSystems

You can call this operation to retrieve a list of file systems and the details of each file system.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set this value to DescribeFileSystem s . |
| FileSystemId | String | No | The file system ID. |
| PageSize | Integer | No | The number of file systems that are displayed on each page. Default value: 10. |
| PageNumber | Integer | No | The number of a page. The number starts at 1. |

|   |   | DescribeFileSystem |
|---|---|---|
|   | s |   |

| Name | Type | Description |
|---|---|---|
| TotalCount | Integer | The total number of file systems. |
| PageSize | Integer | The number of file systems that are displayed on each page. |
| PageNumber | Integer | The number of a page. |
| FileSystems | FileSystemType | The file system description. |
| VolumeSize | Long | The size of the file system to be created. Unit: GB |

Sample request

```
GET https://nas.regionid.example.com/?Action=DescribeFileSystems &FileSystemId=109c042666
```

Sample response

```xml
<DescribeFileSystemsResponse>
  <PageNumber>1</PageNumber>
  <TotalCount>1</TotalCount>
  <PageSize>1</PageSize>
  <RequestId>035B3A3A-E514-4B41-B906-5D906CFBD65F</RequestId>
  <FileSystems>
    <FileSystem>
      <FileSystemId>109c042666</FileSystemId>
      <ProtocolType>NFS</ProtocolType>
      <VolumeSize>10240</VolumeSize>
      <RegionId>cn-hangzhou</RegionId>
      <CreateTime>2017-05-27T15:43:06CST</CreateTime>
      <Destription/>
      <MountTargets>
        <MountTarget>
          <MountTargetDomain>109c042666-wjb85.regionid.nas.example.com</MountTargetDomain
```

`>`

```xml
        </MountTarget>
      </MountTargets>
      <StorageType>Performance</StorageType>
      <MeteredSize>1611661312</MeteredSize>
    </FileSystem>
  </FileSystems>
</DescribeFileSystemsResponse>
```

```json
  "FileSystems": {
    "FileSystem": [
        "StorageType": "Performance",
        "ProtocolType": "NFS",
        "CreateTime": "2017-05-27T15:43:06CST",
    "VolumeSize": "10240",
        "Destription": "",
        "MountTargets": {
          "MountTarget": {
              "MountTargetDomain": "109c042666-wjb85.regionid.nas.example.com"
```

`]` `},`

```json
        "FileSystemId": "109c042666",
        "RegionId": "cn-hangzhou",
        "MeteredSize": 1611661312
```

`]` `},`

```json
  "TotalCount": 1,
  "PageSize": 1,
  "RequestId": "035B3A3A-E514-4B41-B906-5D906CFBD65F",
  "PageNumber": 1
```

#### 2.4.4 ModifyFileSystem

You can call this operation to modify the NAS instance information.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | TRUE | The operation that you want to perform. Set the value to ModifyFileSystem . |
| FileSystemId | String | TRUE | The NAS instance ID. |
| Description | String | FALSE | The description. Space characters are not allowed. |

None Sample requests

```
GET https://nas.regionid.example.com/?Action=ModifyFileSystem &FileSystemId=1ca404a666
```

Sample responses

```json
<ModifyFileSystemResponse>
  <RequestId>5BC5CB97-9F28-42FE-84A4-0CD0DF4211C8</RequestId>
</ModifyFileSystemResponse>
  "RequestId": "5BC5CB97-9F28-42FE-84A4-0CD0DF4211C8"
```

### 2.5 Mount point

#### 2.5.1 CreateMountTarget

You can call this operation to create a mount point.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | TRUE | The operation that you want to perform. Set the value to CreateMountTarget . |
| FileSystemId | String | TRUE | The NAS instance ID. |
| AccessGroupName | String | TRUE | The permission group name. |
| NetworkType | String | TRUE | The network type. Valid values: VPC and Classic. |
| VpcId | String | FALSE | The VPC ID. |
| VSwitchId | String | FALSE | The VSwitch ID. |

| Parameter | Type | Description |
|---|---|---|
| MountTargetDomain | String | The domain name of the mount point |

Sample requests

```
GET https://nas.regionid.example.com/?Action=CreateMountTarget &FileSystemId=174494b666 &AccessGroupName=classic-test
```

Sample responses

```json
<CreateMountTargetResponse>
  <RequestId>70EACC9C-D07A-4A34-ADA4-77506C42B023</RequestId>
  <MountTargetDomain>174494b666-xog95.regionid.nas.example.com</MountTargetDomain>
</CreateMountTargetResponse>
  "RequestId": "70EACC9C-D07A-4A34-ADA4-77506C42B023",
  "MountTargetDomain": "174494b666-xog95.regionid.nas.example.com"
```

#### 2.5.2 DeleteMountTarget

You can call this operation to delete an existing mount point.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | TRUE | The operation that you want to perform. Set the value to DeleteMountTarget . |
| FileSystemId | String | TRUE | The NAS instance ID. |
| MountTargetDomain | String | TRUE | The domain name of the mount point. |

None Sample requests

```
GET https://nas.regionid.example.com/?Action=DeleteMountTarget &FileSystemId=174494b666 &MountTargetDomain=174494b666-xog95.regionid.nas.example.com
```

Sample responses

```json
<DeleteMountTargetResponse>
  <RequestId>5BC5CB97-9F28-42FE-84A4-0CD0DF4211C8</RequestId>
</DeleteMountTargetResponse>
  "RequestId": "5BC5CB97-9F28-42FE-84A4-0CD0DF4211C8"
```

#### 2.5.3 DescribeMountTargets

You can call this operation to retrieve a list of mount points and the details of each mount point.

| Name | Type | Required |   | Description |   |   |
|---|---|---|---|---|---|---|
| Action | String | Yes |   | The operation that you want to perform. Set this value to DescribeMountTarge ts . |   |   |
|   |   |   |   |   | DescribeMountTarge |   |
|   |   |   |   | ts |   |   |
| FileSystemId | String | Yes |   | The file system ID. |   |   |
| MountTargetDomain | String | No |   | The name of the mount point. |   |   |
| PageSize | Integer | No |   | The number of mount points that are displayed on each page. Default value: 10. |   |   |

| A | psara File Storage NAS |   | De | veloper Guide·API referenc | e |
|---|---|---|---|---|---|

| Name | Type | Required | Description |
|---|---|---|---|
| PageNumber | Integer | No | The number of a page. The number starts at 1. |

| Name | Type | Description |
|---|---|---|
| TotalCount | Integer | The total number of mount points. |
| PageSize | Integer | The number of mount points that are displayed on each page. |
| PageNumber | Integer | The number of a page. |
| MountTargets | MountTargetType | A list of mount points and the details of each mount point. |

Sample request

```
GET https://nas.regionid.example.com/?Action=DescribeMountTargets &FileSystemId=1ca404a666
```

Sample response

```xml
<DescribeMountTargetsResponse>
  <PageNumber>1</PageNumber>
  <TotalCount>1</TotalCount>
  <PageSize>1</PageSize>
  <RequestId>3BAB90FD-B4A0-48DA-9F09-2B963510A0EF</RequestId>
  <MountTargets>
    <MountTarget>
      <Status>Active</Status>
      <NetworkType>Vpc</NetworkType>
      <VswId>vsw-2zevmwkwyztjuoffg****</VswId>
      <VpcId>vpc-2zesj9afh3y518k9o****</VpcId>
      <MountTargetDomain>1ca404a666-XXXXX.regionid.nas.example.com</MountTargetDomain>
      <AccessGroup>DEFAULT_VPC_GROUP_NAME</AccessGroup>
    </MountTarget>
  </MountTargets>
</DescribeMountTargetsResponse>
```

```json
  "TotalCount": 1,
  "PageSize": 1,
  "RequestId": "3BAB90FD-B4A0-48DA-9F09-2B963510A0EF",
  "PageNumber": 1,
  "MountTargets": {
    "MountTarget": [
        "Status": "Active",
        "VswId": "vsw-2zevmwkwyztjuoffg****",
        "VpcId": "vpc-2zesj9afh3y518k9o****",
        "MountTargetDomain": "1ca404a666-.regionid.nas.example.com",
        "NetworkType": "Vpc",
        "AccessGroup": "DEFAULT_VPC_GROUP_NAME"
```

`]`

#### 2.5.4 ModifyMountTarget

You can call this operation to modify the information of a mount point.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | TRUE | The operation that you want to perform. Set the value to ModifyMountTarget . |
| FileSystemId | String | TRUE | The NAS instance ID. |
| MountTargetDomain | String | TRUE | The domain name of the mount point. |
| AccessGroupName | String | FALSE | The permission group name. |
| Status | String | FALSE | The status. Valid values: Active and Inactive. |

None Sample requests

```
GET https://nas.regionid.example.com/?Action=ModifyMountTarget &FileSystemId=1ca404a666 &MountTargetDomain=1ca404a666 &Status=Inactive
```

Sample responses

```json
<ModifyMountTargetResponse>
  <RequestId>FF387D95-34C4-4879-B65A-99D1FA1B65CD</RequestId>
</ModifyMountTargetResponse>
  "RequestId": "FF387D95-34C4-4879-B65A-99D1FA1B65CD"
```

### 2.6 Permission group

#### 2.6.1 CreateAccessGroup

You can call this operation to create a permission group.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | TRUE | The operation that you want to perform. Set the value to CreateAccessGroup . |
| AccessGroupName | String | TRUE | The permission group name. |
| AccessGroupType | String | TRUE | The permission group type. Valid values: VPC and Classic. |
| Description | String | FALSE | The permission group description. It is the same as the permission group name by default. |

| Parameter | Type | Description |
|---|---|---|
| AccessGroupName | String | The permission group name |

Sample requests

```
GET https://nas.regionid.example.com/?Action=CreatAccessGroup &AccessGroupName=classic-test &AccessGroupType=Classic &Description=classic test access group
```

Sample responses

```json
<CreateAccessGroupResponse>
  <RequestId>55C5FFD6-BF99-41BD-9C66-FFF39189F4F8</RequestId>
  <AccessGroupName>classic-test</AccessGroupName>
</CreateAccessGroupResponse>
  "RequestId": "55C5FFD6-BF99-41BD-9C66-FFF39189F4F8",
  "AccessGroupName ": "classic-test"
```

#### 2.6.2 CreateAccessRule

You can call this operation to create a permission rule.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | TRUE | The operation that you want to perform. Set the value to CreateAccessRule . |
| AccessGroupName | String | TRUE | The permission group name. |

| Parameter | Type | Required | Description |
|---|---|---|---|
| SourceCidrIp | String | TRUE | The IP address or address segment. |
| RWAccessType | String | FALSE | The access permission type. Valid values: RDWR (default) RDONLY |
| UserAccessType | String | FALSE | The user permission type. Valid values: no squash (default) _ root squash _ all squash _ |
| Priority | Integer | FALSE | The priority. Valid values: 1 to 100. Default value: 1. |

| Parameter | Type | Description |
|---|---|---|
| AccessRuleId | String | The rule serial number |

Sample requests

```
GET https://nas.regionid.example.com/?Action=CreatAccessRule &AccessGroupName=classic-test &SourceCidrIp=10.0.0.1/32
```

Sample responses

```xml
<CreateAccessRuleResponse>
  <AccessRuleId>1</AccessRuleId>
  <RequestId>A323836B-5BC6-45A6-8048-60675C23EE2A</RequestId>
</CreateAccessRuleResponse>
```

```json
  "RequestId": "A323836B-5BC6-45A6-8048-60675C23EE2A",
  "AccessRuleId": "1"
```

#### 2.6.3 DeleteAccessGroup

You can call this operation to delete an existing permission group.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | TRUE | The operation that you want to perform. Set the value to DeleteAccessGroup . |
| AccessGroupName | String | TRUE | The permission group name. |

None Sample requests

```
GET https://nas.regionid.example.com/?Action=DeleteAccessGroup &AccessGroupName=classic-test
```

Sample responses

```json
<DeleteAccessGroupResponse>
  <RequestId>5BC5CB97-9F28-42FE-84A4-0CD0DF4211C8</RequestId>
</DeleteAccessGroupResponse>
  "RequestId": "9E15E394-38A6-457A-A62A-D9797C9A0262"
```

#### 2.6.4 DeleteAccessRule

You can call this operation to delete an existing permission rule.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | TRUE | The operation that you want to perform. Set the value to DeleteAccessRule . |
| AccessGroupName | String | TRUE | The permission group name. |
| AccessRuleId | String | TRUE | The rule serial number. |

None Sample requests

```
GET https://nas.regionid.example.com/?Action=CreatAccessRule &AccessGroupName=classic-test &AccessRuleId=1
```

Sample responses

```json
<DeleteAccessRuleResponse>
  <RequestId>5B4511A7-C99E-4071-AA8C-32E2529DA963</RequestId>
</DeleteAccessRuleResponse>
  "RequestId": "5B4511A7-C99E-4071-AA8C-32E2529DA963",
```

#### 2.6.5 DescribeAccessGroups

You can call this operation to return the description of a permission group.

| Parameter | Type | Required |   | Description |   |   |
|---|---|---|---|---|---|---|
| Action | String | TRUE |   | The operation that you want to perform. Set the value to DescribeAccessGrou ps . |   |   |
|   |   |   |   |   | DescribeAccessGrou |   |
|   |   |   |   | ps |   |   |
| AccessGroupName | String | FALSE |   | The permission group name. |   |   |
| PageSize | Integer | FALSE |   | The number of permission groups that are displayed on each page. Default value: 10. |   |   |
| PageNumber | Integer | FALSE |   | The page number of the list, which starts from 1. |   |   |

| Parameter | Type | Description |
|---|---|---|
| TotalCount | Integer | The total number of permission groups |
| PageSize | Integer | The number of permission groups that are displayed on each page |
| PageNumber | Integer | The page number of the list |
| AccessGroups | String | The permission group description |

Sample requests

```
GET https://nas.regionid.example.com/?Action=DescribeAccessGroups
```

Sample responses

```json
<DescribeAccessGroupsResponse>
  <PageNumber>1</PageNumber>
  <TotalCount>2</TotalCount>
  <PageSize>2</PageSize>
  <RequestId>3E569F4A-F743-490B-AC01-A8088F5C17A1</RequestId>
  <AccessGroups>
    <AccessGroup>
      <Description>DEFAULT ACCESS GROUP NAME</Description>
      <RuleCount>1</RuleCount>
      <AccessGroupType>Vpc</AccessGroupType>
      <AccessGroupName>DEFAULT_VPC_GROUP_NAME</AccessGroupName>
      <MountTargetCount>8</MountTargetCount>
    </AccessGroup>
    <AccessGroup>
      <Description>This is a classic test access group~</Description>
      <RuleCount>0</RuleCount>
      <AccessGroupType>Classic</AccessGroupType>
      <AccessGroupName>classic-test</AccessGroupName>
      <MountTargetCount>0</MountTargetCount>
    </AccessGroup>
  </AccessGroups>
</DescribeAccessGroupsResponse>
  "AccessGroups": {
    "AccessGroup": [
        "RuleCount": 1,
        "AccessGroupType": "Vpc",
        "Description": "DEFAULT ACCESS GROUP NAME",
        "AccessGroupName": "DEFAULT_VPC_GROUP_NAME",
        "MountTargetCount": 8
```

`},`

```json
        "RuleCount": 0,
        "AccessGroupType": "Classic",
        "Description": "This is a classic test access group~",
        "AccessGroupName": "classic-test",
        "MountTargetCount": 0
```

`]` `},`

```json
  "TotalCount": 2,
  "PageSize": 2,
  "RequestId": "2514F97E-FFF0-4A1F-BF04-729CEAC64B6F",
  "PageNumber": 1
```

#### 2.6.6 DescribeAccessRules

You can call this operation to retrieve a list of permission group rules and the details of each rule.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set this value to DescribeAccessRule s . |
| AccessGroupName | String | Yes | The name of the permission group. |
| AccessRuleId | String | No | The rule ID. |
| PageSize | Integer | No | The number of rules that are displayed on each page. Default value: 10. |
| PageNumber | Integer | No | The number of a page. The number starts at 1. |

|   |   | DescribeAccessRule |
|---|---|---|
|   | s |   |

| Name | Type | Description |
|---|---|---|
| TotalCount | Integer | The total number of rules. |
| PageSize | Integer | The number of rules that are displayed on each page. |
| PageNumber | Integer | The number of a page. |
| AccessRules | AccessRules | The description of a rule. |

Sample request

```
GET https://nas.regionid.example.com/?Action=DescribeAccessRules &AccessGroupName=classic-test
```

Sample response

```json
<DescribeAccessRulesResponse>
  <AccessRules>
    <AccessRule>
      <SourceCidrIp>10.0.XX.XX/32</SourceCidrIp>
      <AccessRuleId>1</AccessRuleId>
      <RWAccess>RDWR</RWAccess>
      <UserAccess>no_squash</UserAccess>
      <Priority>1</Priority>
    </AccessRule>
  </AccessRules>
  <PageNumber>1</PageNumber>
  <TotalCount>1</TotalCount>
  <PageSize>1</PageSize>
  <RequestId>86D89E82-4297-4343-8E1E-A2495B35CC70</RequestId>
</DescribeAccessRulesResponse>
  "TotalCount": 1,
  "PageSize": 1,
  "RequestId": "86D89E82-4297-4343-8E1E-A2495B35CC70",
  "PageNumber": 1,
  "AccessRules": {
    "AccessRule": [
        "RWAccess": "RDWR",
        "UserAccess": "no_squash",
        "Priority": 1,
        "SourceCidrIp": "10.0.XX.XX/32",
        "AccessRuleId": "1"
```

`]`

#### 2.6.7 ModifyAccessGroup

You can call this operation to modify a permission group.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | TRUE | The operation that you want to perform. Set the value to ModifyAccessGroup . |

| Parameter | Type | Required | Description |
|---|---|---|---|
| AccessGroupName | String | TRUE | The permission group name. |
| Description | String | FALSE | The permission group description. |

None Sample requests

```
GET https://nas.regionid.example.com/?Action=ModifyAccessGroup &AccessGroupName=classic-test &Description=classic-test
```

Sample responses

```json
<ModifyAccessGroupResponse>
  <RequestId>ED2AE737-9D50-4CA4-B0DA-31BD610C2363</RequestId>
</ModifyAccessGroupResponse>
  "RequestId": "ED2AE737-9D50-4CA4-B0DA-31BD610C2363"
```

#### 2.6.8 ModifyAccessRule

You can call this operation to delete a permission rule.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | TRUE | The operation that you want to perform. Set the value to ModifyAccessRule . |
| AccessGroupName | String | TRUE | The permission group name. |

| psara File Storage NAS |   | De | veloper Guide·API referenc |
|---|---|---|---|

| Parameter | Type | Required | Description |
|---|---|---|---|
| AccessRuleId | String | TRUE | The rule serial number. |
| SourceCidrIp | String | FALSE | The IP address or address segment. |
| RWAccessType | String | FALSE | The access permission type. |
| UserAccessType | String | FALSE | The user permission type. |
| Priority | Integer | FALSE | The priority. Valid values: 1 to 100. Default value: 1. |

None Sample requests

```
GET https://nas.regionid.example.com/?Action=ModifyAccessRule &AccessGroupName=classic-test &AccessRuleId=1 &SourceCidrIp=192.168.0.1 &RWAccessType=RDWR &UserAccessType=all_squash
```

Sample responses

```json
<ModifyAccessRuleResponse>
  <RequestId>6299428C-3861-435D-AE54-9B330A0007C8</RequestId>
</ModifyAccessRuleResponse>
  "RequestId": "6299428C-3861-435D-AE54-9B330A0007C8",
```

### 2.7 Appendix: Error codes

An error code consists of four components, as listed in . Error codes

| Component | Description |
|---|---|
| HttpCode | The HTTP response code that complies with HTTP syntax |
| Code | The error code |
| Message | The error message |
| Advice | The recommended solution |

Error codes

| HTTP status code | Code | Message | Advice |
|---|---|---|---|
| 500 | InternalError | A system internal error occurred. | Please try again later. |
| 503 | ServiceUnavailable | This service is unavailable right now. | Please try again later. |
| 504 | ServiceTimeout | Service request timed out. | Please try again later. |
| 503 | SubRam.CheckFailed | The sub user ram check has failed due to some internal error. | Please try again later. |
| 503 | VpcRam.CheckFailed | The Vpc ram check has failed due to some internal error. | Please try again later. |
| 503 | VpcSubRam.CheckFailed | The Vpc sub user ram check has failed due to some internal error. | Please try again later. |
| 400 | MissingParameter.caller Uid | Request parameter missing: callerUid is not specified. | Add the callerUid request parameter. |
| 400 | MissingParameter.Regio nId | Request parameter missing: RegionId of the domain name is not specified. | Add the RegionId field to the domain name. |
| 400 | MissingParameter.VSwit chId | Request parameter missing: VSwitchId is not specified. | Add the VSwitchId request parameter. |
| 400 | MissingParameter.VpcId | Request parameter missing: VpcId is not specified. | Add the VpcId request parameter. |

| HTTP status code | Code | Message | Advice |
|---|---|---|---|
| 400 | InvalidParameter.Storag eType | Invalid request parameter: StorageType is invalid. | Set StorageType to Performance or Capacity. |
| 400 | InvalidParameter.Protoc alType | Invalid request parameter: ProtocalType is invalid. | Set ProtocalType to NFS. |
| 400 | InvalidParameter.Descri ption | Invalid request parameter: Description contains invalid characters. | Set Description to a string that contains English letters and special characters such as at signs (@), number signs (#), dollar signs ($), underscores ( ), _ plus signs (+), and hyphens (-). |
| 404 | InvalidFileSystem.NotFo und | The specified NAS instance does not exist. | The specified NAS instance does not exist or has been deleted. |
| 403 | InvalidFileSystem.Alread yExisted | The specified NAS instance already exists. | Call DescribeFileSystems and specify the NAS instance ID to view the instance information. |
| 404 | InvalidMountTarget.Not Found | The specified mount point does not exist. | The specified mount point does not exist or has been deleted. |
| 404 | InvalidAccessGroup.Not Found | The specified permission group does not exist. | The specified permission group does not exist or has been deleted. |
| 403 | InvalidAccessGroup.Alre adyExisted | The specified permission group already exists. | Call DescribeMountTargets and specify the permission group to view its information. |
| 403 | InvalidAccessGroup.Alre adyAttached | The specified permission group has been bound to a mount point. | Unbind the permission group from the mount point before deleting the permission group. |
| 404 | InvalidAccessRule.NotFo und | The specified permission rule does not exist. | The specified permission rule does not exist or has been deleted. |

| eveloper Guide·API refere | nce |   | Apsara File Storage NA |
|---|---|---|---|

| HTTP status code | Code | Message | Advice |
|---|---|---|---|
| 404 | InvalidLocatin.NotFound | The specified location does not exist. | The requested location does not exist or is not providing services. |
| 404 | InvalidRegionId.NotFoun d | The specified region does not exist. | The requested region does not exist or is not providing services. |
| 404 | InvalidAZone.NotFound | The specified zone does not exist. | The requested zone does not exist or is not providing services. |
| 404 | InvalidVpc.NotFound | The specified VPC does not exist. | Create a VPC first. |
| 404 | InvalidVip.NotFound | The specified VIP does not exist. | Make sure that there are available IP addresses in your VPC. |
| 404 | InvalidLBid.NotFound | The specified LBid does not exist. | Please try again later. |
| 404 | InvalidVpcTunnelId.NotF ound | The specified VPC tunnelId does not exist. | Check the VPC information first. |
| 404 | InvalidVpc.CreationFaile d | The specified vpc instance creation failed. | Make sure that the VPC information is correct and there is an available IP address for the VPC, and then try again. |
| 403 | OperationDenied.Defaul tAccessGroupCannotDel ete | Operation not allowed: The default permission group cannot be deleted. | You can only edit custom permission groups. |
| 403 | OperationDenied.Defaul tAccessGroupCannotMo dify | Operation not allowed: The default permission group cannot be modified. | You can only edit custom permission groups. |
| 403 | OperationDenied.Netwo rkTypeNotMatched | Operation not allowed: The mount point network type does not match the AccessGroupType. | Make sure that the NetworkType of the mount point and the AccessGroupType of the permission group are consistent. |

| HTTP status code | Code | Message | Advice |
|---|---|---|---|
| 403 | OperationDenied.Mount TargetNotEmpty | Operation not allowed: The specified NAS instance already has a mount point. Delete the existing mount point first. | Delete the existing mount points first. |
| 403 | OperationDenied.FileSys temCountsExceeded | The number of NAS instances has already reached the upper limit (a user can create a maximum of 10 NAS instances). | To raise the limit, contact technical support. |
| 403 | OperationDenied.Mount TargetCountsExceeded | The number of mount points has already reached the upper limit (a maximum of two mount points can be created for each NAS instance). | To raise the limit, contact technical support. |
| 403 | OperationDenied.Access GroupCountsExceeded | The number of permission groups has already reached the upper limit. | To raise the limit, contact technical support. |
| 403 | OperationDenied.Access RuleCountsExceeded | The number of permission rules has already reached the upper limit. | To raise the limit, contact technical support. |
| 403 | Forbidden.InvalidUserTy pe | No permission: The user type is invalid. | Sorry, this API does not support your account type. |
| 403 | Forbbiden.Ram | User not authorized to operate on the specified resource, or this API doesn’t support RAM. | Access RAM to grant required NAS permissions. |
| 403 | NotQualified | No public beta qualification yet | Please initiate an application for a trial of the related features. If your application fails to be approved, contact the technical support. |

Error response examples

```json
<Error>
  <RequestId>B71B4C68-6C6B-4D4B-AD70-8951BD7D188E</RequestId>
  <HostId>nas.regionid.example.com</HostId>
  <Code>InvalidFileSystem.NotFound</Code>
  <Message>The specified NAS instance does not exist.</Message>
</Error>
  "RequestId": "B71B4C68-6C6B-4D4B-AD70-8951BD7D188E",
  "HostId": " nas.regionid.example.com ",
  "Code": "InvalidFileSystem.NotFound",
  "Message": "The specified NAS instance does not exist."
```
