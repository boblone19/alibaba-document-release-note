---
title: "Alibaba Cloud Apsara Stack Enterprise V3.12.0 ApsaraDB for RDS Developer Guide 20220928"
product_version: "V3.12.0"
doc_version: "20220928"
pdf_pages: 143
source_pdf: "Alibaba Cloud Apsara Stack Enterprise V3.12.0 ApsaraDB for RDS Developer Guide 20220928.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/01_ApsaraStackEnterprise/20230221/Alibaba%20Cloud%20Apsara%20Stack%20Enterprise%20V3.12.0%20ApsaraDB%20for%20RDS%20Developer%20Guide%2020220928.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes+edge-junk)
---

# Alibaba Cloud Apsara Stack Enterprise V3.12.0 ApsaraDB for RDS Developer Guide 20220928

## Table of Contents

- 1 Use ASAPI to call Apsara Stack SDKs
  - 1.1 Overview
  - 1.2 Log on to the API Tool console
  - 1.3 View the information about API operations
  - 1.4 Obtain the endpoint of ASAPI
  - 1.5 Obtain the core package for ASAPI
  - 1.6 Obtain an AccessKey pair
  - 1.7 Query the region ID
  - 1.8 Call SDK for Java
  - 1.9 Call SDK for Node.js
  - 1.10. (Optional) Use POP SDK to call ASAPI
- 2 API reference
  - 2.1 List of operations by function
  - 2.2 Make API requests
    - 2.2.1 Request structure
    - 2.2.2 Common parameters
      - 2.2.2.1 Common request parameters
      - 2.2.2.2 Common response parameters
    - 2.2.3 Responses
      - 2.2.3.1 Success responses
      - 2.2.3.2 Sample error responses
    - 2.2.4 Request signatures
  - 2.3 Instance management
    - 2.3.1 CreateDBInstance
    - 2.3.2 DeleteDBInstance
    - 2.3.3 RestartDBInstance
    - 2.3.4 DescribeDBInstanceAttribute
    - 2.3.5 DescribeDBInstances
    - 2.3.6 ModifyDBInstanceSpec
    - 2.3.7 DescribeDBInstanceNetInfo
    - 2.3.8 ModifyDBInstanceConnectionString
    - 2.3.9 ModifyDBInstanceNetworkType
    - 2.3.10 DescribeDBInstanceIPArrayList
    - 2.3.11 ModifySecurityIps
    - 2.3.12 DescribeRegions
    - 2.3.13 DescribeDBInstanceHAConfig
    - 2.3.14 MigrateToOtherZone
    - 2.3.15 PurgeDBInstanceLog
    - 2.3.16 ModifyDBInstanceDescription
    - 2.3.17 ModifyDBInstanceMaintainTime
    - 2.3.18 ModifyDBInstanceHAConfig
    - 2.3.19 SwitchDBInstanceHA
    - 2.3.20 CreateReadOnlyDBInstance
    - 2.3.21 DescribeDBInstanceSSL
    - 2.3.22 ModifyDBInstanceSSL
    - 2.3.23 DescribeDBInstanceTDE
    - 2.3.24 ModifyDBInstanceTDE
  - 2.4 Database management
    - 2.4.1 CreateDatabase
    - 2.4.2 DeleteDatabase
    - 2.4.3 DescribeDatabases
    - 2.4.4 ModifyDBDescription
  - 2.5 Account management
    - 2.5.1 CreateAccount
    - 2.5.2 DeleteAccount
    - 2.5.3 DescribeAccounts
    - 2.5.4 GrantAccountPrivilege
    - 2.5.5 RevokeAccountPrivilege
    - 2.5.6 ModifyAccountDescription
    - 2.5.7 ResetAccountPassword
    - 2.5.8 ResetAccount
  - 2.6 Backup and restoration
    - 2.6.1 CreateBackup
    - 2.6.2 CloneDBInstance
    - 2.6.3 DescribeBackups
    - 2.6.4 CreateTempDBInstance
    - 2.6.5 DescribeBackupPolicy
    - 2.6.6 ModifyBackupPolicy
    - 2.6.7 RestoreDBInstance
    - 2.6.8 DeleteBackup
  - 2.7 Monitoring management
    - 2.7.1 DescribeResourceUsage
    - 2.7.2 DescribeDBInstancePerformance
    - 2.7.3 DescribeDBInstanceMonitor
    - 2.7.4 ModifyDBInstanceMonitor
  - 2.8 Parameter management
    - 2.8.1 DescribeParameterTemplates
    - 2.8.2 DescribeParameters
    - 2.8.3 ModifyParameter
  - 2.9 Log management
    - 2.9.1 DescribeSlowLogs
    - 2.9.2 DescribeSlowLogRecords
    - 2.9.3 DescribeErrorLogs
    - 2.9.4 DescribeBinlogFiles
    - 2.9.5 DescribeSQLCollectorPolicy
    - 2.9.6 ModifySQLCollectorPolicy
    - 2.9.7 DescribeSQLLogRecords
    - 2.9.8 DescribeSQLLogFiles
  - 2.10 Data migration
    - 2.10.1 CreateUploadPathForSQLServer
    - 2.10.2 DescribeFilesForSQLServer
    - 2.10.3 ImportDatabaseBetweenInstances
    - 2.10.4 CancelImport
  - 2.11 Tag management
    - 2.11.1 AddTagsToResource
    - 2.11.2 DescribeTags
    - 2.11.3 RemoveTagsFromResource
  - 2.12 RAM authorization
  - 2.13 Appendix
    - 2.13.1 Error codes on the client
      - 2.13.1.1 Common errors
      - 2.13.1.2 Specific errors
    - 2.13.2 Error codes on the server
    - 2.13.3 Instance states
    - 2.13.4 Performance parameters
    - 2.13.5 Forbidden keywords
    - 2.13.6 Instance types

Apsara Stack SDKs

## 1 Use ASAPI to call Apsara Stack SDKs

SDKs

### 1.1 Overview

This topic describes the architecture and features of Apsara Stack API (ASAPI). ASAPI is a platform that integrates all features and is the only portal to connect to Apsara Stack. ASAPI can categorize, audit, and manage API operations. It can also assemble and customize existing operations and adapt to your operations. Each cloud service can call ASAPI for required data and features, which avoids inconsistent operations caused by different calling methods and separate encapsulation. This can ensure the operation program integrity and improve development efficiency and code portability. Apsara Stack SDKs ASAPI allows you to manage and call operations in a centralized manner and customize development. ASAPI supports access to most cloud services deployed in Apsara Stack and supports passthrough or encapsulation of different backend APIs. This way, operations can be called using the same method. ASAPI allows you to use SDKs and API portals to call APIs registered on ASAPI, customize SDKs, and manage versions of Apsara Stack, services, and APIs.

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
Apsara Stack SDKs operation name in the search box, and then click the search icon.
4. View and remember the service name, API operation name, and API version.

### 1.4 Obtain the endpoint of ASAPI

This topic describes how to obtain the endpoint of ASAPI in the Apsara Stack Operations console. Procedure
1. In the address bar, enter the URL region-id.aso.intranet-domain-id.com and press the Enter key.
Not e You can select a language from the drop-down list in the upper-right corner of the page.
2. Enter your username and password.
Not e Obtain the username and password for logging on to the ASO console from the deployment personnel or an administrator. When you log on to the ASO console for the first time, you must change the password of your username as prompted. To enhance security, a password must meet the following requirements: It must contain uppercase and lowercase letters. It must contain digits. Apsara Stack SDKs It must contain special characters such as exclamation points (!), at signs (@), number signs (#), dollar signs ($), and percent signs (%). It must be 10 to 20 characters in length.
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
ASAPI Management platform. Apsara Stack SDKs

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
Apsara Stack SDKs Not e An AccessKey pair is automatically allocated to a level-1 organization. Subordinate organizations use the same AccessKey pair as their level-1 organization. Obtain the AccessKey pair of a personal account To obtain the AccessKey pair of a personal account, perform the following operations:
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

### 1.8 Call SDK for Java

This topic describes how to obtain and use Apsara Stack SDK for Java. Prerequisites An authorized account and an AccessKey pair (AccessKey ID and AccessKey secret) are obtained. For more information about how to obtain and view your AccessKey pair in the ASCM console, see Obtain an AccessKey pair. The endpoint of ASAPI is obtained. For more information about how to obtain the endpoint of ASAPI, see Obtain the endpoint of Asapi. Apsara Stack SDKs Java Development Kit (JDK) 1.6 or later is obtained. Add dependencies Add dependencies to pom.xml:

```xml
<dependency>
    <groupId>com.aliyun</groupId>
    <artifactId>asapi</artifactId>
    <version>0.0.1-SNAPSHOT</version>
    <scope>system</scope>
    <systemPath>${project.basedir}/lib/aliyun-java-sdk-asapi.jar</systemPath>
</dependency>
```

Use Apsara Stack SDK for Java You can use GET and POST to call ASAPI API operations. GET requests

```
 ASClient client = new ASClient();
// Form 1 String result = client.doGet(endpoint, parameters); // Form 2 String result = client.doRequest(endpoint, parameters);
```

POST requests Apsara Stack SDKs

```
// Set the endpoint of ASAPI. String endpoint = "http://xxx/asapi/v3"; // Set request parameters. Map<String, String> parameters = new HashMap<String, String>(); // Set parameters for the product. parameters.put("Product", "rds"); // The product name must be the same as the name displayed in the corresponding API directory. parameters.put("Action", "CreateDBInstance"); // The API name must be in the sam e case as that in the API directory. parameters.put("Version", "2019-05-10"); // The API version. // Set authorization-related parameters. parameters.put("AccessKeyId", "<your-access-key-id>"); // The AccessKey ID of th e authorized account. parameters.put("AccessKeySecret", "<your-access-key-secret>"); // The AccessKey secret o f the authorized account. // Set business parameters. parameters.put("username", "<your-username>"); // The username used to l og on to the ASCM console. parameters.put("password", "<your-password>"); // The password used to l og on to the ASCM console. JSONObject jsonObject = new JSONObject(); jsonObject.put("param1", "json parameter 1"); jsonObject.put("param2", "json parameter 2"); parameters.put("json", jsonObject.toJSONString()); // Create an ASClient object for initiating requests. ASClient client = new ASClient(); // Add a request header. client.addHeader("x-acs-resourceGroupId", "112233"); // Initiate the request and obtain the response. String result = client.doPost(endpoint, parameters);
```

### 1.9 Call SDK for Node.js

This topic describes how to obtain and use Apsara Stack SDK for Node.js. Prerequisites An authorized account and an AccessKey pair (AccessKey ID and AccessKey secret) are obtained. For more information, see Obtain an AccessKey pair. The endpoint of Apsara Stack API (ASAPI) is obtained. For more information, see Obtain the endpoint of Asapi. The region ID is obtained. For more information about how to query the region ID, see Query the region ID. Add dependencies
1. Install Apsara Stack SDK for Node.js.

```
 tnpm install --save @ali/asapi-nodejs-sdk
```

2. Add the following configurations to mocha.opts if mocha.opts depends on eggjs:
Apsara Stack SDKs

```
--recursive --colors --timeout 60000 --reporter mochawesome --require co-mocha --require egg-ts-helper/register --require espower-typescript/guess --require intelli-espower-loader
```

Use SDK for Node.js The following example shows how to call Apsara Stack SDK for Node.js:
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
// Specify the ASAPI endpoint. const API_GATEWAY = "http://xxxx/asapi/v3" // Create the rpc client. const asapiClient = ctx.service.sdk.rpcClient; // Set request parameters. let params = {
    Action: 'CreateDBInstance',
    Product: 'rds',
    regionId: 'cn-qingdao-env12-d01',
    accessKeyId: 'xxxxxxx',
    accessKeySecret: 'xxxxxxx',
    Version: '2018-01-22',
```

};

```
// Set parameters in the request header. asapiClient.addHeader("x-acs-regionId", "cn-hangzhou"); // Initiate the request and obtain the response. const result = await asapiClient.doRequest(API_GATEWAY, params, {});
```

1.10. (Optional) Use POP SDK to call ASAPI This topic describes how to switch the gateway to ASAPI if an application uses POP SDK to call cloud products. Procedure Apsara Stack SDKs
1. Switch the gateway to ASAPI and add common parameters required by the API operation to the
request header, so that the API operation can be called in a transparent manner.
2. Add the Product Name field to the request header.
Not e Each product uses a unique endpoint in POP SDK. However, ASAPI provides only one domain name. You cannot identify the product to which an API operation belongs based on the API operation name and the version number. For example, both ECS and KVStore for Redis provide the DescribeInstances API operation of the 2015-01-01 version. Sample code An API operation of ECS is called in the following example:

```java
         try {
            CreateDBInstanceResponse response = client.getAcsResponse(request);
            System.out.println(new Gson().toJson(response));
        } catch (ServerException e) {
            e.printStackTrace();
        } catch (ClientException e) {
            System.out.println("ErrCode:" + e.getErrCode());
            System.out.println("ErrMsg:" + e.getErrMsg());
            System.out.println("RequestId:" + e.getRequestId());
```

`}`

## 2 API reference

### 2.1 List of operations by function

The following tables list API operations available for use in RDS. RDS instance management

| Operation | Description |
|---|---|
| CreateDBInstance | Creates an RDS instance. |
| DeleteDBInstance | Releases an RDS instance. |
| RestartDBInstance | Restarts an RDS instance. |
| DescribeDBInstanceAttribute | Queries the details of an RDS instance. |
| DescribeDBInstances | Queries the instance list. |
| ModifyDBInstanceSpec | Modifies the RDS instance type. |
| AllocateInstancePublicConnection | Applies for a public endpoint. |
| ReleaseInstancePublicConnection | Releases a public endpoint. |
| SwitchDBInstanceNetType | Applies for an internal endpoint. |
| DescribeDBInstanceNetInfo | Queries all endpoints. |
| ModifyDBInstanceConnectionString | Modifies an endpoint. |
| ModifyDBInstanceConnectionMode | Changes the RDS instance access mode. |
| ModifyDBInstanceNetworkType | Changes the RDS instance network type. |
| DescribeDBInstanceIPArrayList | Queries the IP whitelist of an RDS instance. |
| ModifySecurityIps | Modifies the IP whitelist of an RDS instance. |
| DescribeRegions | Queries the RDS region and zone information. |
| DescribeDBInstanceHAConfig | Queries the RDS zone information and data replication status. |
| MigrateToOtherZone | Migrates an RDS instance from one zone to another. |
| PurgeDBInstanceLog | Clears the logs of an RDS instance. |
| UpgradeDBInstanceEngineVersion | Upgrades the RDS instance version. |
| ModifyDBInstanceDescription | Modifies the description of an RDS instance. |

| D | eveloper Guide·API reference | ApsaraDB for RD | S |
|---|---|---|---|

| Operation | Description |
|---|---|
| ModifyDBInstanceMaintainTime | Modifies the maintenance window of an RDS instance. |
| ModifyDBInstanceHAConfig | Modifies the data replication and high availability polices of an RDS instance. |
| SwitchDBInstanceHA | Switches between the primary and secondary RDS instances. |
| CreateReadonlyDBInstance | Creates a read-only RDS instance. |
| DescribeDBInstanceSSL | Queries the SSL link of an RDS instance. |
| ModifyDBInstanceSSL | Modifies the SSL link of an RDS instance. |
| DescribeDBInstanceTDE | Queries the TDE status of an RDS instance. |
| ModifyDBInstanceTDE | Modifies the TDE status of an RDS instance. |

RDS database management

| Operation | Description |
|---|---|
| CreateDatabase | Creates a database. |
| DeleteDatabase | Deletes a database. |
| DescribeDatabases | Queries the database list. |
| ModifyDBDescription | Modifies the description of a database. |

RDS account management

| Operation | Description |
|---|---|
| CreateAccount | Creates an account. |
| DeleteAccount | Deletes an account. |
| DescribeAccounts | Queries the account list. |
| GrantAccountPrivilege | Grants permissions to an account. |
| RevokeAccountPrivilege | Revokes permissions from an account. |
| ModifyAccountDescription | Modifies the description of an account. |
| ResetAccountPassword | Resets the password of an account. |
| ResetAccount | Resets an account. |

RDS backup and restoration

| Operation | Description |
|---|---|
| CreateBackup | Creates a backup. |
| CloneDBInstance | Clones an RDS instance. |
| DescribeBackups | Queries the backup instance list. |
| CreateTempDBInstance | Creates a temporary instance. |
| DescribeBackupPolicy | Queries a backup policy. |
| ModifyBackupPolicy | Modifies a backup policy. |
| RestoreDBInstance | Restores a backup set to an instance. |
| DeleteBackup | Deletes data backup files. |

RDS monitoring management

| Operation | Description |
|---|---|
| DescribeResourceUsage | Queries the resource usage of an instance. |
| DescribeDBInstancePerformance | Queries the performance data of an instance. |
| DescribeDBInstanceMonitor | Queries the monitoring behaviors of an instance. |
| ModifyDBInstanceMonitor | Modifies the monitoring behaviors of an instance. |

RDS parameter management

| Operation | Description |
|---|---|
| DescribeParameterTemplates | Queries a database parameter template. |
| DescribeParameters | Queries the running database parameter list of the current instance. |
| ModifyParameter | Modifies the database parameter list. |

RDS log management

| Operation | Description |
|---|---|
| DescribeSlowLogs | Queries the slow log list. |
| DescribeSlowLogRecords | Queries slow log details. |
| DescribeErrorLogs | Queries error logs. |

| eveloper Guide·API reference | ApsaraDB for RD |
|---|---|

| Operation | Description |
|---|---|
| DescribeBinlogFiles | Queries binlogs. |
| DescribeSQLCollectorPolicy | Queries the SQL collection status. |
| ModifySQLCollectorPolicy | Changes the SQL collection status. |
| DescribeSQLLogRecords | Queries the SQL audit logs of an RDS instance. |
| DescribeSQLLogFiles | Queries the SQL audit file list. |

RDS data migration

| Operation | Description |
|---|---|
| ImportDatabaseBetweenInstances | Migrates data from other instances. |
| CancelImport | Cancels an import task. |

RDS tag management

| Operation | Description |
|---|---|
| AddTagsToResource | Binds a tag. |
| DescribeTags | Queries tags. |
| RemoveTagsFromResource | Unbinds a tag. |

### 2.2 Make API requests

#### 2.2.1 Request structure

This topic describes the request structure of Apsara DB for RDS API operations. Endpoints The endpoint of the Apsara DB for RDS API is rds.example.com. For information about how to obtain a service endpoint, see Obtain the endpoint of ASAPI. Protocols You can send requests over HTTP or HTTPS. We recommend that you use HTTPS for enhanced security. Methods You can use the HTTP GET method to send requests. When you use this method, you must include request parameters in the request URL. Parameters The action to be performed must be specified in the Action parameter of each request. Each operation request must include common request parameters and the specific request parameters of the operation called. Encoding All requests and responses are encoded in UTF-8.

#### 2.2.2 Common parameters

##### 2.2.2.1 Common request parameters

Common request parameters must be included in the request of each API.

| Parameter | Typ e | Require d | Description |
|---|---|---|---|
| Format | Strin g | No | The format of the response. Valid values: JSON and XML. Default value: XML. |
| Version | Strin g | Yes | The API version. It is in the YYYY-MM-DD format. The current version is 2014-08-15. |
| AccessKeyId | Strin g | Yes | The AccessKey ID provided to you by Alibaba Cloud. |
| Signature | Strin g | Yes | The signature result string. For more information about the signature calculation method, see Request signatures. |
| SignatureMet hod | Strin g | Yes | The algorithm used to create the request signature. Valid value: HMAC-SHA1. |
| Timestamp | Strin g | Yes | The request timestamp. The timestamp follows the ISO 8601 standard and uses UTC. It is in the YYYY-MM-DDThh:mm:ssZ format. For example, 20:00:00, August 15, 2013, UTC+8 will be written as 2013- 08-15T12:00:00Z. |
| SignatureVersi on | Strin g | Yes | The signature algorithm version. The current version is 1.0. |
| SignatureNon ce | Strin g | Yes | A unique, randomly generated number used to prevent network replay attacks. You must use a different random number for each request. |

Example

```
https://rds.example.com/ ? Format=xml &Version=2014-08-15 &Signature=Pc5WB8gokVnxxxxx &SignatureMethod=HMAC-SHA1 &SignatureNonce=15215528852396 &SignatureVersion=1.0 &AccessKeyId=key-test &OwnerId=12345678 &Timestamp=2014-10-10T12:00:00Z
```

##### 2.2.2.2 Common response parameters

The system returns a unique RequestId for each API request, regardless of whether the API operation is successful. Example

```xml
<? xml version="1.0" encoding="utf-8"? > <!—Result root node--> <API name + response>
    <!—Returned request tag-->
    <RequestId>4C4***38-****-****-****-*******6F216</RequestId>
    <!—Response data-->
</API name + response>
```

#### 2.2.3 Responses

##### 2.2.3.1 Success responses

The response data for API requests is displayed in a uniform format. In the response data, a 2xx HTTP status code indicates that the API operation is called. The response data for called API operations is returned in either the XML or JSON format. You can add parameters to an API request to specify the format of the response data. Response data uses the XML format by default. Sample responses in this topic are formatted with line breaks or indents for a clear view. The actual responses are not formatted in the same manner as these examples. Responses in the XML format include information about whether the call is successful, and details specific to the operation. Example:

```xml
<!—Result root node--> <API name + response> <!—Response request tag--> <RequestId>4C467B38-****-447D-****-AC04*******16</RequestId> <!—Response data--> </API name + response>
```

JSON format

```json
{ "RequestId": "4C467B38-****-447D-****-AC04*******16", /* Response Data */}
```

##### 2.2.3.2 Sample error responses

If an error occurs when you call an API operation, no result is returned. You can locate the cause of the error by referencing Error codes in Appendix. When an error occurs on an HTTP request for an API operation, a 4xx or 5xx HTTP status code is returned. The returned body includes the specific error code and message. The response body also contains the RequestId and HostId parameters. The RequestId parameter indicates the globally unique identifier (GUID) of the request, and the HostId parameter indicates the ID of the site that you accessed with the request. You can contact Alibaba Cloud Customer Services when the cause of the error cannot be found. We recommend that you provide HostId and RequestId to help us resolve the issue at the earliest opportunity. XML format

```xml
<Error> <RequestId>8906582E-****-****-A6C4-0E78*******5</RequestId> <HostId>rds.example.com</HostId> <Code>UnsupportedOperation</Code> <Message>The specified action is not supported. </Message> </Error>
```

JSON format

```json
{ "RequestId": "7463B73D-****-4D19-****-6B8*******2EF", "HostId": "rds.example.com", "Code": "UnsupportedOperation", "Message": "The specified action is not supported."
```

`}`

#### 2.2.4 Request signatures

ApsaraDB for RDS authenticates each access request. Therefore, a request must contain signature information regardless of whether it is sent over HTTP or HTTPS. For information about how to obtain an AccessKey pair (AccessKey ID and AccessKey secret), see Obtain an AccessKey pair. ApsaraDB for RDS implements symmetric encryption with an AccessKey pair to verify the identity of the request sender. The AccessKey pair is issued by Alibaba Cloud. You can apply for AccessKey pairs and manage them on the official Alibaba Cloud website. The AccessKey ID is used to verify the identity of the user. The AccessKey secret is used to encrypt and verify the signature string on the server. You must keep your AccessKey secret strictly confidential. Perform the following steps to sign an access request:
1. Use request parameters to construct a canonicalized query string.
i. Sort all of the request parameters in alphabetical order. The request parameters include all common and operation-specific parameters except Signature. Not e If you use the GET method to send a request, the request parameters are included as part of the request URI. The request parameters in the URI are placed after a question mark (?) and separated by ampersands (&). ii. Encode the name and value of each request parameter. Parameter names and values must be encoded into a URL based on the UTF-8 character set. The following rules apply in the URL encoding process: Uppercase letters, lowercase letters, digits, and some special characters such as hyphens (-), underscores (_), periods (.), and tildes (~) do not need to be encoded. Other characters must be percent encoded in %XY format. XY represents the ASCII code of the characters in hexadecimal notation. For example, double quotation marks (") are encoded as %22. Extended UTF-8 characters are encoded in the %XY%ZA… format. Spaces must be encoded as %20. Do not encode spaces as plus signs (+). Not e Most libraries that support URL encoding, such as java.net.URLEncoder, comply with the Multipurpose Internet Mail Extensions (MIME) encoding rules of application/x-www-form-urlencoded. If this encoding method is used, replace the plus signs (+) in the encoded strings with %20, the asterisks (*) with %2A, and %7E with a tilde (~) to conform to the encoding rules. iii. Connect the encoded parameter names and values by using equal signs (=). iv. Sort the equal sign-connected strings by their parameter names in alphabetical order and connect them with ampersands (&).
2. Create a string-to-sign from the encoded canonicalized query string based on the following rules:

```
StringToSign= HTTPMethod + "&" + percentEncode("/") + "&" + percentEncode(CanonicalizedQueryString)
```

HTTPMethod: specifies the HTTP method used to make the request, such as GET. percentEncode("/"): specifies the encoded value for the forward slash (/) based on the URL encoding rules described in 1.b. The value is %2F. percentEncode(CanonicalizedQueryString): specifies the string encoded from the canonicalized query string constructed in Step 1 based on the URL encoding rules described in 1.b.
3. Calculate the HMAC value of the string-to-sign by using the AccessKey secret as the key.
Not e An ampersand (&) is added to the end of the key (ASCII: 38). The hashing algorithm used is SHA-1.
4. Encode the HMAC value in Base64 to obtain the signature string.
5. Add the signature string to the request as the Signature parameter.
Not e When the signature string is submitted to the RDS server as the final request parameter value, the string must be URL-encoded like other parameters based on rules defined in RFC 3986. The following code is the request URL without a signature for the DescribeDBInstances operation:

```
http://rds.example.com/?TimeStamp=2013-06-01T10:33:56Z&Format=XML&AccessKeyId=testid&Ac tion=DescribeDBInstances&SignatureMethod=HMAC-SHA1&RegionId=region1&SignatureNonce=NwDA xvLU6tFE0DVb&Version=2014-08-15&SignatureVersion=1.0
```

The following code is the string-to-sign:

```
GET&%2F&AccessKeyId%3Dtestid%26Action%3DDescribeDBInstances%26Format%3DXML%26RegionId%3 Dregion1%26SignatureMethod%3DHMAC-SHA1%26SignatureNonce%3DNwDAxvLU6tFE0DVb%26SignatureV ersion%3D1.0%26TimeStamp%3D2013-06-01T10%253A33%253A56Z%26Version%3D2014-08-15
```

Assume that the AccessKey ID is testid, the AccessKey secret is testsecret, and the key used for HMAC calculation is testsecret&. The following signature string is obtained:

```
BIPOMlu8LXBeZtLQkJTw6iFvw1E=
```

The following code is the signed request URL that has the Signature parameter added:

```
http://rds.example.com/?TimeStamp=2013-06-01T10%3A33%3A56Z&Format=XML&AccessKeyId=testi d&Action=DescribeDBInstances&SignatureMethod=HMAC-SH
```

### 2.3 Instance management

#### 2.3.1 CreateDBInstance

Description You can call this operation to create an ApsaraDB for RDS instance. For information about instance types, see Instance types in Appendix. Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | Strin g | Yes | The operation that you want to perform. Set the value to CreateDBInstance. |

| Parameter | Type | Required | Description |
|---|---|---|---|
| RegionId | Strin g | Yes | The region ID of the instance. It can be up to 50 characters in length. You can call the DescribeRegions operation to query the most recent region list. |
| ZoneId | Strin g | No | The zone ID of the instance. You can call the DescribeRegions operation to query the most recent zone list. |
| Engine | Strin g | Yes | The engine of the database. Valid values: MySQL SQLServer PostgreSQL POLARDB |
| EngineVersion | Strin g | Yes | The engine version of the database. Valid values: MySQL: 5.6 and 5.7 SQL Serve: 2008 R2, 2012 ent ha, 2012 std ha, 2016 ent ha, _ _ _ _ _ _ and 2016 std ha _ _ PostgreSQL: 9.4 and 10.0 PolarDB: 11 |
| DBInstanceClass | Strin g | Yes | The type of the instance. |
| DBInstanceStorag e | Integ er | Yes | The user-defined storage space. Valid values: MySQL High-availability Edition: 5 to 2000 PolarDB High-availability Edition: 5 to 2000 This value must be in 5 GB increments. Unit: GB. |
| DBInstanceNetTy pe | Strin g | Yes | The network connection type of the instance. Valid values: Internet Intranet |
| DBInstanceDescri ption | Strin g | No | The description of the instance. It must be 2 to 256 characters in length and can contain letters, digits, underscores ( ), and _ hyphens (-). It must start with a letter and cannot start with http:// or https://. |
| SecurityIPList | Strin g | Yes | The list of IP addresses that are allowed to access all databases in the instance. You can add a maximum of 1,000 IP addresses and separate them with commas (,). Format: %, 0.0.0.0/0, 10.23.12.24 (IP address), or 10.23.12.24/24 (CIDR block, where /24 indicates the prefix of the CIDR block is 24-bit. You can replace 24 with a value ranging from 1 to 32.). 0.0.0.0/0 indicates that the instance can be accessed by all devices. |

| Parameter | Type | Required | Description |
|---|---|---|---|
| ClientToken | Strin g | Yes | The client token that is used to ensure the idempotence of the request. |
| InstanceNetwork Type | Strin g | No | The network type of the instance. Valid values: VPC and Classic. Default value: Classic. |
| ConnectionMode | Strin g | No | The access mode of the instance. Valid values: Standard and Safe. If no value is specified, the system automatically assigns an access mode. |
| VPCId | Strin g | No | The ID of the VPC. |
| VSwitchId | Strin g | No | The ID of the VSwitch. |
| PrivateIpAddress | Strin g | No | The VPC IP address that belongs to the specified VSwitch. If no value is specified, the system automatically assigns a VPC IP address. |

Response parameters

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> | - | For more information, see. |
| DBInstanceId | String | The ID of the instance. |
| OrderId | String | The ID of the order. |
| ConnectionString | String | The endpoint used to connect to the database. |
| Port | String | The port used to connect to the database. |

Examples XML format Sample success responses

```xml
<CreateDBInstanceResponse> <OrderId>100789370xxxxx</OrderId> <ConnectionString>xxxxx.mysql.rds.aliyuncs.com </ConnectionString> <DBInstanceId>rds-xxxxx</DBInstanceId> <port>3306</port> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> </CreateDBInstanceResponse>
```

JSON format

```json
{ "OrderId": "100789370230206", "ConnectionString": "rds-xxxxx.mysql.rds.aliyuncs.com", "DBInstanceId": "rds-xxxxx", "Port": "3306", "RequestId": "1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC"}
```

#### 2.3.2 DeleteDBInstance

Description You can call this operation to release an RDS instance. Before you call this operation, ensure that the following requirements are met: The instance is in the running state. The instance is not manually locked. The instance is a pay-as-you-go primary instance, read-only instance, disaster recovery instance, or temporary instance. Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DeleteDBInstance. |
| DBInstanceId | String | Yes | The ID of the instance to be released. |

Response parameters

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> | - | For more information, see Common response parameters. |

Examples Sample request s

```
https://rds.example.com/?Action=DeleteDBInstance &DBInstanceId=rds-xxxxx &<[Common request parameters]>
```

Sample responses XML format

```xml
<DeleteDBInstanceResponse> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> </DeleteDBInstanceResponse>
```

JSON format

```json
{ "RequestId": "1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC" }
```

#### 2.3.3 RestartDBInstance

Description You can call this operation to restart an RDS instance. The instance will be restarted in 10 seconds. If there are a large number of transactions that must be submitted or rolled back, the restart process may be delayed for a minute. Before you call this operation, ensure that the following requirements are met: The instance is in the running state. The instance is not performing a backup task. Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to RestartDBInstance. |
| DBInstanceId | String | Yes | The ID of the instance to be restarted. |

Response parameters

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> | - | For more information, see Common response parameters. |

Examples XML format

```xml
<RestartDBInstanceResponse> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> </RestartDBInstanceResponse>
```

JSON format

```json
{ "RequestId": "1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC"}
```

#### 2.3.4 DescribeDBInstanceAttribute

Description You can call this operation to query attributes of an instance.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeDBInstanceAttribute. |
| DBInstanceI d | String | Yes | The ID of the instance. Up to 30 IDs can be entered at a time. Separate multiple IDs with commas (,). |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| Items |   |   | The array that consists of DBInstanceAttribute data. |
| └DBInstanceId | String | rm-bpvxxxxx | The ID of the instance. |
| └ DBInstanceType | String | Primary | The role of the instance. Valid values: Primary: primary instance Readonly: read-only instance Guard: disaster recovery instance Temp: temporary instance |
| └Category | String | Basic | The RDS edition of the instance. Valid values: Basic: Basic Edition Standard: High-availability Edition Enterprise: Enterprise Edition |
| └InstanceNetwor kType | String | Classic | The network type of the instance. Valid values: Classic VPC |
| └RegionId | String | cn-hangzhou | The region ID of the instance. |
| └ZoneId | String | cn-hangzhou-a | The zone ID of the instance. |
| └ConnectionStrin g | String | rds- xxxxx.mysql.rds.al iyuncs.com | The endpoint used to connect to the instance. |
| └Port | String | 3306 | The port used to connect to the instance. |
| └Engine | String | MySQL | The engine of the database. |
| └EngineVersion | String | 5.5 | The engine version of the database. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| └DBInstanceClass Type | String | s | The family of the instance. Valid values: s: shared instance x: general-purpose instance d: dedicated instance h: dedicated host |
| └DBInstanceClass | String | rds.mys2.small | The type of the instance. |
| └DBInstanceMem ory | Long | 240 | The memory capacity of the instance. Unit: MB. |
| └DBInstanceStora ge | Integer | 10 | The storage space of the instance. Unit: GB. |
| └DBInstanceNetT ype | String | Internet | The network connection type of the instance. Valid values: Internet Intranet |
| └DBInstanceStatu s | String | Running | The status of the instance. For more information, see Instance states in Appendix. |
| └DBInstanceDescr iption | String | Test instance | The description of the instance. |
| └LockMode | String | Unlock | The lock status of the instance. Valid values: Unlock: normal ManualLock: locked manually LockByExpiration: locked automatically upon expiration LockByRestoration: locked automatically before instance rollback LockByDiskQuota: locked automatically due to full disk space |
| └LockReason | String | None | The reason why the instance is locked. |
| └DBMaxQuantity | Integer | 200 | The maximum number of databases that can be created for an instance. |
| └AccountMaxQua ntity | Integer | 50 | The maximum number of accounts that can be created for an instance. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| └CreationTime | String | 2011-05- 30T12:11:4Z | The time when the instance was created. The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ssZ format. Example: 2011-05-30T12:11:4Z . |
| └ExpireTime | String | None | The expiration time of the instance. This parameter is not returned for pay-as-you-go instances. |
| └MaintainTime | String | 00:00Z-02:00Z | The scheduled maintenance window of the instance. For example, 00:00Z-02:00Z indicates that routine maintenance can be performed from 00:00 to 02:00. |
| └AvailabilityValue | String | 100.0% | The availability status of the instance. Unit: %. |
| └MaxIOPS | Integer | 150 | The maximum number of I/O operations per second (IOPS). |
| └MaxConnections | Integer | 60 | The maximum number of concurrent connections to the instance. |
| └MasterInstanceI d | String | null | The ID of the primary instance. If this parameter is not returned (null), the instance is a primary instance. |
| └IncrementSourc eDBInstanceId | String | null | The instance ID of the incremental data source. For example, the incremental data source of a disaster recovery instance or read-only instance is the primary instance, and the incremental data source of the primary instance is null. |
| └GuardDBInstanc eId | String | None | The ID of the disaster recovery instance attached to the instance. |
| └TempDBInstanc eId | String | None | The ID of the temporary instance attached to the instance. |
| └ReadOnlyDBInst anceIds |   | rr-xxxxx | The IDs of the read-only instances attached to the instance. |
| └DBInstanceId | String | rm-bpxxxxx | The ID of the instance. |

| psaraDB for RDS |   |   | Developer Guide·API referenc |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| └VpcCloudInstan ceId | String | vpc-xxxxx | The ID of the VPC. |
| └ResourceGroupI d | String | 3653788125 | The ID of the resource group. |
| RequestId | String | 1AD222E9-E606- 4A42-BF6D- 8A4442913CEF | The ID of the request. |

DBInstanceAttribute parameters Not e You can call the DescribeDBInstanceHAConfig operation to query information of the primary and secondary instances. Examples Sample request s

```
https://rds.example.com/?Action=DescribeDBInstanceAttribute &DBInstanceId=rds-xxxxx &<Common request parameters>
```

Sample success responses JSON format

```json
{ "Items":
    { "DBInstanceAttribute":
        [ { "LockMode": "Unlock",
            "ConnectionString": "rds-xxxxx.mysql.rds.aliyuncs.com",
            "CreationTime": "2014-10-10T10:28:48Z",
            "DBInstanceNetType": "Internet",
            "ReadOnlyDBInstanceIds": { "ReadOnlyDBInstanceId": [] },
            "MaxConnections": 60,
            "LockReason": "",
            "Engine": "MySQL",
            "AvailabilityValue": "100.0%",
            "AccountMaxQuantity": 50,
            "DBMaxQuantity": 200,
            "RegionId": "cn-hangzhou",
            "TempDBInstanceId": "",
            "DBInstanceMemory": 240,
            "MaxIOPS": 150,
            "DBInstanceType": "Primary",
            "DBInstanceStatus": "Running",
            "MasterInstanceId": "",
            "EngineVersion": "5.6",
            "IncrementSourceDBInstanceId": "",
            "GuardDBInstanceId": "",
            "DBInstanceStorage": 10,
            "DBInstanceDescription": "",
            "DBInstanceId": "rdsfnjfquxxxxx",
            "PayType": "Postpaid",
            "ExpireTime": "",
            "MaintainTime": "",
            "DBInstanceClass": "rds.mys2.small",
            "SecurityIPList": "11.11.11.11",
            "Port": "3306" } ] },
    "RequestId": "1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC" }
```

JSON format

```json
{ "Code":"UnsupportedOperation", "HostId":"rds.aliyuncs.com", "Message":"The specified action is not supported.", "RequestId":"1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC"}
```

#### 2.3.5 DescribeDBInstances

Description You can call this operation to query instances and RAM-authorized instances.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeDBInstanc es | The operation that you want to perform. Set the valuer to DescribeDBInstanc es. |
| RegionId | String | Yes | cn-hangzhou | The region ID of the instance. |
| ConnectionMode | String | No | Performance | The access mode of the instance. Valid values: Performance: standard access mode Safe: safe access mode If no value is specified, instances in both access modes are returned. |
| DBInstanceType | String | No | Primary | The role of the instance. Valid values: Primary: primary instance Readonly: read- only instance Guard: disaster recovery instance Temp: temporary instance If no value is specified, instance of all roles are returned. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| InstanceNetworkT ype | String | No | Classic | The network type of the instance. Valid values: VPC: VPC instance Classic: classic network instance If no value is specified, instance of both network types are returned. |
| PageNumber | Integer | No | 1 | The number of the page to return. Pages start from page 1 but must be equal to or smaller than the maximum Integer value. Default value: 1. |
| PageSize | Integer | No | 30 | The number of entries to return on each page. Valid values: 30, 50, and 100. Default value: 30. |
| Tags | String | No | {“key1”:”value 1”} | The tag of the instance, in the JSON format. The tag includes a key-value pair of TagKey and TagValue. TagValue can be left empty, but TagValue cannot. Example: {“key1”:”value 1”}. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| PageNumber | Integer | 1 | The number of the page returned. |
| TotalRecordCount | Integer | 1 | The total number of entries. |
| PageRecordCount | Integer | 1 | The number of instances on the current page. |
| Items |   |   | The array that consists of instance data. |
| └DBInstanceId | String | rm-xxxxx | The ID of the instance. |
| └DBInstanceDescription | String | testforRemarks | The description of the instance. |
| └PayType | String | Postpaid | The billing method of the instance. Valid values: Postpaid: pay-as- you-go Prepaid: subscription |
| └DBInstanceType | String | Primary | The role of the instance. Valid values: Primary: primary instance ReadOnly: read-only instance Guard: disaster recovery instance Temp: temporary instance |
| └InstanceNetworkType | String | Classic | The network type of the instance. Valid values: Classic: classic network instance VPC: VPC instance |

| Parameter | Type | Example | Description |
|---|---|---|---|
| └ConnectionMode | String | Performance | The access mode of the instance. Valid values: Performance: standard access mode Safe: safe access mode |
| └RegionId | String | cn-hangzhou | The region ID of the instance. |
| └ExpireTime | String | None | The expiration time of the instance. This parameter is not returned for pay-as- you-go instances. |
| └DBInstanceStatus | String | Intranet | The status of the instance. For more information, see Instance states in Appendix. |
| └Engine | String | MySQL | The type of the database. |
| └DBInstanceNetType | String | Internet | The network connection type of the instance. Valid values: Internet: public network Intranet: internal network |
| └LockMode | String | Unlock | The lock status of the instance. Valid values: Unlock: normal ManualLock: locked manually LockByExpiration: locked automatically upon expiration LockByRestoration: locked automatically before instance rollback LockByDiskQuota: locked automatically for full disk space |

| Parameter | Type | Example | Description |
|---|---|---|---|
| └LockReason | String | None | The reason why the instance is locked. |
| └MasterInstanceId | String | null | The ID of the primary instance. If this parameter is not returned (null), the instance is a primary instance. |
| └GuardDBInstanceId | String | None | The ID of the disaster recovery instance attached to the instance. |
| └TempDBInstanceId | String | None | The ID of the temporary instance attached to the instance. |
| └VpcCloudInstanceId | String | vpc-xxxxx | The ID of the VPC instance. |
| └ReadOnlyDBInstanceId s |   |   | None |
| └DBInstanceId | String | rm-xxxxx | The ID of the instance. |
| RequestId | String | 1AD222E9-E606-4A42- BF6D-8A4442913CEF | The ID of the request. |

Examples Sample request s

```
https://rds.example.com/?Action=DescribeDBInstances &RegionId=cn-hangzhou &Engine=MySQL &<Common request parameters>
```

Sample success responses XML format

```xml
<DescribeDBInstancesResponse> <PageRecordCount>2</PageRecordCount> <Items> <DBInstance> <DBInstanceDescription>testforRemarks</DBInstanceDescription> <ExpireTime>2014-10-10T16:00:00Z</ExpireTime> <DBInstanceId>rdsmjfirxxxxx</DBInstanceId> <DBInstanceNetType>Internet</DBInstanceNetType> <PayType>Prepaid</PayType> <DBInstanceStatus>Running</DBInstanceStatus> <DBInstanceType>Primary</DBInstanceType> <Engine>MySQL</Engine> <LockMode>Unlock</LockMode> <LockReason/> <RegionId>cn-hangzhou</RegionId> <ZoneId>cn-hangzhou-a</ZoneId> <MasterInstanceId/> <GuardDBInstanceId/> <TempDBInstanceId/> <ReadOnlyDBInstanceIds> <ReadOnlyDBInstanceId/> </ReadOnlyDBInstanceIds> </DBInstance> </Items> <PageNumber>1</PageNumber> <TotalRecordCount>2</TotalRecordCount> <RequestId>2553A660-E4EB-4AF4-A402-8AFF70A49143</RequestId> </DescribeDBInstancesResponse>
```

JSON format

```json
{ "Items":
    { "DBInstance":
        [ { "DBInstanceDescription":"testforRemarks",
            "DBInstanceId":"rdsmjfirxxxxx",
            "DBInstanceNetType":"Internet",
            "DBInstanceStatus":"Running",
            "DBInstanceType":"Primary",
            "Engine":"MySQL",
            "ExpireTime":"2014-10-10T16:00:00Z",
            "GuardDBInstanceId ":"",
            "LockMode":"Unlock",
            "LockReason":"",
            "MasterInstanceId":"",
            "PayType":"Prepaid",
            "ReadOnlyDBInstanceIds":{ "ReadOnlyDBInstanceId":[] },
            "RegionId":"cn-hangzhou",
            "TempDBInstanceId":"",
            "ZoneId":"cn-hangzhou-a" },
        ] },
    "PageNumber":1,
    "PageRecordCount":2,
    "RequestId":"2553A660-E4EB-4AF4-A402-8AFF70A49143",
    "TotalRecordCount":2
```

`}` JSON format

```json
{ "Code":"UnsupportedOperation", "HostId":"rds.aliyuncs.com", "Message":"The specified action is not supported.", "RequestId":"7463B73D-35CC-4D19-A010-6B8D65D242EF"}
```

#### 2.3.6 ModifyDBInstanceSpec

Description You can call this operation to change the type or storage space of an instance. Before you call this operation, make sure that the following requirements are met: The instance is in the running state. The instance is not performing a backup task. One of the instance type (DBInstanceClass) and storage space (DBInstanceStorage) parameters is specified in the request. When you downgrade the disk space configuration, the input disk space is no less than 1.1 times the actually used space. Only primary and read-only instances allow specification changes. Specifications of disaster recovery and temporary instances cannot be changed.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyDBInstance Spec | The operation that you want to perform. Set the value to ModifyDBInstance Spec. |
| DBInstanceId | String | Yes | rm-bpxxxx | The ID of the instance. |
| AccessKeyId | String | No | LTAIKw8gqxxxxx | The AccessKey ID provided by Alibaba Cloud. |
| ClientToken | String | No | ETnLKlblzczshOTU bOCziJZNwHlYBQ | The client token that is used to ensure the idempotence of the request. |
| DBInstanceClass | String | No | rds.mys2.small | The type of the instance. For more information, see Instance types in Appendix. |
| DBInstanceStorage | Integer | No | 20 | The user-defined storage space. Unit: GB. This value must be in 5 GB increments. For more information, see the Instance types topic in the User Guide of ApsaraDB for RDS. |
| EffectiveTime | String | No | Immediate | The time when the changes take effect. Valid values: Immediate and MaintainTime. Default value: Immediate. |
| OwnerAccount | String | No | testuser@aliyun.c om | The Apsara Stack tenant account. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 1AD222E9-E606-4A42- BF6D-8A4442913CEF | The ID of the request. |

Examples Sample request s

```
https://rds.example.com/?Action=ModifyDBInstanceSpec &DBInstanceId=rds-xxxxx &PayType=Postpaid &DBInstanceStorage=10 &<Common request parameters>
```

Sample success responses XML format

```xml
<ModifyDBInstanceSpecResponse> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> </ModifyDBInstanceSpecResponse>
```

JSON format

```json
{ "RequestId": "1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC" }
```

JSON format

```json
{ "Code":"UnsupportedOperation", "HostId":"rds.aliyuncs.com", "Message":"The specified action is not supported.", "RequestId":"7463B73D-35CC-4D19-A010-6B8D65D242EF"}
```

#### 2.3.7 DescribeDBInstanceNetInfo

Description You can call this operation to query the connection information of a specified instance. Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeDBInstanceNetInfo. |
| DBInstanceId | String | Yes | The ID of the instance whose connection information is queried. |

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> |   | For more information, see Common response parameters. |
| DBInstanceNetInfos | List<DBInstanceAttribute> | The array that consists of DBInstanceAttribute data. |
| InstanceNetworkType | String | VPC: VPC instance Classic: classic network instance |

DBInstanceNetInfo parameters

| Parameter | Type | Description |
|---|---|---|
| ConnectionString | String | The DNS connection string. |
| IPAddress | String | The IP address. |
| IPType | String | Valid values for classic network instances: Inner and Public. Valid values for VPC instances: Private and Public. |
| Port | String | The port information. |
| VPCId | String | The ID of the VPC. |
| VSwitchId | String | The ID of the VSwitch. |

#### 2.3.8 ModifyDBInstanceConnectionString

Description You can call this operation to modify the endpoint and port of a connection string. ApsaraDB for RDS provides the internal and public endpoints and allows both types to coexist in a specific access mode. Request parameters

| Parameter | Ty pe | Requir ed | Description |
|---|---|---|---|
| Action | Stri ng | Yes | The operation that you want to perform. Set the value to ModifyDBInstanceConnectionString. |
| DBInstanceId | Stri ng | Yes | The ID of the instance. |
| CurrentConnectionS tring | Stri ng | Yes | The endpoint used by the instance. |

| psaraDB for RDS |   |   | Developer Guide·API referenc |
|---|---|---|---|
| Parameter | Ty pe | Requir ed | Description |
| ConnectionStringPr efix | Stri ng | No | The endpoint to be used by the instance. |
| Port | Stri ng | No | The port to be used by the instance. |

Response parameters This operation returns only common response parameters. For more information, see Common response parameters.

#### 2.3.9 ModifyDBInstanceNetworkType

Description You can call this operation to switch the network type of an RDS instance between VPC and classic network. Not e Only the classic network instances with the ConnectionMode set to Safe can have their network type switched to VPC. Request parameters

| Parameter | Ty p e | Requir ed | Description |
|---|---|---|---|
| Action | St rin g | Yes | The operation that you want to perform. Set the value to ModifyDBInstanceNetworkType. |
| DBInstanceId | St rin g | Yes | The ID of the instance for which the network type is modified. |
| InstanceNetwork Type | St rin g | Yes | The network type of the instance. VPC: VPC instance. Classic: classic network instance. |
| VPCId | St rin g | No | The ID of the VPC. |
| VSwitchId | St rin g | No | The ID of the VSwitch. This parameter is required if the value of VPCId is specified. |

| Parameter | Ty p e | Requir ed | Description |
|---|---|---|---|
| PrivateIpAddress | St rin g | No | The VPC IP address that belongs to the specified VSwitch. If no value is specified, the system automatically assigns a VPC IP address based on VPCId and VSwitchId. |

Response parameters This operation returns only common response parameters. For more information, see Common response parameters.

#### 2.3.10 DescribeDBInstanceIPArrayList

Description You can call this operation to query the IP whitelist of an instance. Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeDBInstanceIPArrayList. |
| DBInstanceId | String | Yes | The ID of the instance whose IP whitelist is queried. |

Response parameters

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> |   | Common response parameters. |
| Items | List<DBInstanceIPAr ray> | The array that consists of DBInstanceIPArray data. |

DBInstanceIPArray parameters

| Parameter | Type | Description |
|---|---|---|
| DBInstanceIPArrayNam e | String | The name of the IP whitelist. |
| DBInstanceIPArrayAttri bute | String | The attribute of the IP whitelist. Default value: null. Whitelists tagged with "hidden" are not displayed in the console. |

| Parameter | Type | Description |
|---|---|---|
| SecurityIPList | String | The IP addresses in an IP address whitelist. Separate multiple IP addresses with commas (,). You can add a maximum of 1,000 different IP addresses to a whitelist. Supported formats of IP addresses are IP addresses such as 0.0.0.0/0 and 10.23.12.24, or Classless Inter-Domain Routing (CIDR) blocks such as 10.23.12.24/24. /24 indicates the length of the IP address prefix. The IP address prefix can consist of 1 to 32 bits. |

#### 2.3.11 ModifySecurityIps

Description You can call this operation to modify the IP whitelist of an instance. Before you call this operation, ensure that the following requirements are met: The instance is in the running state. The instance is not locked by the system. Request parameters

| Parameter | Ty pe | Requir ed | Description |
|---|---|---|---|
| Action | Stri ng | Yes | The operation that you want to perform. Set the value to ModifySecurityIps. |
| DBInstanceId | Stri ng | Yes | The ID of the instance whose IP whitelist is modified. |
| SecurityIps | Stri ng | No | The IP addresses in an IP address whitelist. Separate multiple IP addresses with commas (,). You can add a maximum of 1,000 different IP addresses to a whitelist. Supported formats of IP addresses are IP addresses such as 0.0.0.0/0 and 10.23.12.24, or Classless Inter-Domain Routing (CIDR) blocks such as 10.23.12.24/24. /24 indicates the length of the IP address prefix. The IP address prefix can consist of 1 to 32 bits. |
| DBInstanceIPArrayNam e | Stri ng | No | The name of the IP whitelist. If no value is specified, the whitelist named Default will be modified. |
| DBInstanceIPArrayAttri bute | Stri ng | No | The attribute of the IP whitelist. Default value: null. Whitelists tagged with "hidden" are not displayed in the console. |

Response parameters This operation returns only common response parameters. For more information, see Common response parameters. Examples Sample request s

```
https://rds.example.com/?Action=ModifySecurityIps &DBInstanceId=rds-xxxxx &SecurityIps=192.168.1.2 &<Common request parameters>
```

Sample responses XML format

```xml
<ModifySecurityIpsResponse> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> </ModifySecurityIpsResponse>
```

JSON format

```json
{ "RequestId": "1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC"}
```

#### 2.3.12 DescribeRegions

Description You can call this operation to query the available RDS regions and zones. Before you call the CreateInstance operation, call this operation to query region IDs. Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeRegions. |

Response parameters

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> | - | Common response parameters. |
| Regions | List<RDSRegion> | The array that consists of RDSRegion data. |

RDSRegion parameters

| Parameter | Type | Description |
|---|---|---|
| RegionId | String | The region ID. |
| ZoneId | String | The zone ID. |

Examples Sample request s

```
https://rds.example.com/?Action=DescribeRegions &<Common request parameters>
```

Sample responses XML format

```xml
<DescribeRegionsResponse> <Regions> <RDSRegion> <RegionId>cn-hangzhou</RegionId> <ZoneId>cn-hangzhou-a</RegionId> </RDSRegion> <RDSRegion> <RegionId>cn-hangzhou</RegionId ><ZoneId>cn-hangzhou-b</ZoneId> </RDSRegion> </Regions> <RequestId>A36D9720-7902-42A4-B8B9-014A2135E6C3</RequestId> </DescribeRegionsResponse>
```

JSON format

```json
{ "Regions":
    { "RDSRegion":
        [ {"RegionId": "cn-hangzhou",
            "ZoneId":"cn-hangzhou-a"},
          {"RegionId": "cn-hangzhou",
            "ZoneId":"cn-hangzhou-b"},
             ]},
    "RequestId": "1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC"
```

`}`

#### 2.3.13 DescribeDBInstanceHAConfig

Description You can call this operation to query the zone information and data replication status of instances. Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeDBInstanceHAConfig. |
| DBInstanceId | String | Yes | The ID of the instance. |

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> |   | For more information about common response parameters, see Common response parameters. |
| DBInstanceId | String | The ID of the instance. |
| SyncMode | String | The synchronization mode. Valid values: Semi-sync and Async. |
| HAMode | String | The high availability mode. RPO: Data persistence is preferred. RTO: Instance availability is preferred. |
| HostInstanceInfos | List<NodeI nfo> | The array that consists of NodeInfo data. |

NodeInfo parameters

| Parameter | Type | Description |
|---|---|---|
| NodeId | String | The unique ID of the primary or secondary instance. |
| NodeType | String | The role of the instance. Master: primary node. Slave: secondary node. |
| RegionId | String | The region ID of the instance. |
| ZoneId | String | The zone ID of the instance. |
| SyncStatus | String | The synchronization status of the instance. NotAvailable: A failure has occurred and synchronization is unavailable. Syncing: Synchronization is in process, with a probability of data loss during failovers. Synchronized: Synchronization is completed. NotSupport: Synchronization is not supported by the engine type or version. |
| LogSyncTime | String | The time when the secondary instance receives logs. |
| DataSyncTime | String | The time when the secondary instance receives data. |

#### 2.3.14 MigrateToOtherZone

Description You can call this operation to migrate an instance from one zone to another. For example, if instance 1 is located in the Hangzhou Zone A zone of the China (Hangzhou) region, you can call this operation to migrate the instance to the Hangzhou Zone B zone of the China (Hangzhou) region. Not e In cross-zone migration, instances must be migrated within the same region. For example, instances in a zone of the China (Hangzhou) region cannot be migrated to a zone of the China (Qingdao) region. Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to MigrateToOtherZone. |
| DBInstanceId | String | Yes | The ID of the instance to be migrated. |
| ZoneId | String | Yes | The zone ID of the instance. You can call the DescribeRegions operation to query available zones. |

Response parameters This operation returns only common response parameters. For more information, see Common response parameters. Examples Sample request s

```
https://rds.example.com/?Action=MigrateToOtherZone &DBInstanceId=rds-xxxxx &ZoneId=cn-hangzhou-b &<Common request parameters>
```

Sample responses XML format

```xml
<MigrateToOtherZoneResponse> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> </MigrateToOtherZoneResponse>
```

JSON format

```json
{ "RequestId": "1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC"}
```

#### 2.3.15 PurgeDBInstanceLog

Description You can call this operation to clear all binlogs for a MySQL instance.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to PurgeDBInstanceLog. |
| DBInstanceId | String | Yes | The ID of the instance for which all binlogs are cleared. |

Response parameters This operation returns only common response parameters. For more information, see Common response parameters. Examples Sample request s

```
https://rds.example.com/?Action=PurgeDBInstanceLog &DBInstanceId=rds-xxxxx &<Common request parameters>
```

Sample success responses XML format

```xml
<PurgeDBInstanceLogResponse> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> </PurgeDBInstanceLogResponse>
```

JSON format

```json
{ "RequestId": "1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC"}
```

#### 2.3.16 ModifyDBInstanceDescription

Description You can call this operation to modify the description of an instance to identify the instance easily. For example, you can modify the description of an instance to Alibaba Cloud testing environment instance. Request parameters

| Parameter | Type | Require d | Description |
|---|---|---|---|
| Action | Strin g | Yes | The operation that you want to perform. Set the value to ModifyDBInstanceDescription. |
| DBInstanceId | Strin g | Yes | The ID of the instance whose description is modified. |
| DBInstanceDescri ption | Sting | Yes | The description of the instance. |

This operation returns only common response parameters. Examples Sample request s

```
https://rds.example.com/?Action=ModifyDBInstanceDescription &DBInstanceId=rds-xxxxx &DBInstanceDescription=testdescribe &<Common request parameters>
```

Sample responses XML format

```xml
<ModifyDBInstanceDescriptionResponse> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> </ModifyDBInstanceDescriptionResponse>
```

JSON format

```json
{ "RequestId": "1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC"}
```

#### 2.3.17 ModifyDBInstanceMaintainTime

Description You can call this operation to modify the scheduled period for routine maintenance. You can set the maintenance window to an off-peak period. Alibaba Cloud performs routine maintenance during the maintenance window to minimize the impact on your services. Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to ModifyDBInstanceMaintainTime. |
| DBInstanceId | String | Yes | The ID of the instance whose maintenance window is modified. |

| Parameter | Type | Required | Description |
|---|---|---|---|
| MaintainTime | String | Yes | The maintenance window of the instance. Valid values: 22:00Z-02:00Z 02:00Z-06:00Z 06:00Z-10:00Z 10:00Z-14:00Z 14:00Z-18:00Z 18:00Z-22:00Z |

Response parameters This operation returns only common response parameters. For more information, see Common response parameters. Examples Sample request s

```
https://rds.example.com/?Action=ModifyDBInstanceMaintainTime &DBInstanceId=rds-xxxxx &MaintainTime=22:00Z-02:00Z &<Common request parameters>
```

Sample responses XML format

```xml
<ModifyDBInstanceMaintainTimeResponse> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> </ModifyDBInstanceMaintainTimeResponse>
```

JSON format

```json
{ "RequestId": "1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC" }
```

#### 2.3.18 ModifyDBInstanceHAConfig

Description You can call this operation to modify the instance data replication mode and high availability switching rules. Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to ModifyDBInstanceHAConfig. |
| DBInstanceI d | String | Yes | The ID of the instance. |
| SyncMode | String | Yes | The synchronization mode of the instance. Valid values: Semi-sync and Async. |
| HAMode | String | Yes | The HA mode of the instance. RPO: Data persistence is preferred. RTO: Instance availability is preferred. |

Response parameters This operation returns only common response parameters.

#### 2.3.19 SwitchDBInstanceHA

Description You can call this operation to change the database used as the primary database. RDS instances are composed of primary and secondary databases distributed across different servers. The new primary database bears the service traffic. Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to SwitchDBInstanceHA. |
| DBInstanceI d | String | Yes | The ID of the primary instance. |
| NodeId | String | Yes | The unique ID of the node. You can call the DescribeDBInstanceHAConfig operation to query the value of this parameter. |
| Force | String | Yes | Yes: forced. No: unforced. Default value: No. |

Response parameters This operation returns only common response parameters. For more information, see Common response parameters.

#### 2.3.20 CreateReadOnlyDBInstance

You can call this operation to create a read-only instance for a primary RDS instance. Before you call this operation, make sure that the following requirements are met: The primary instance is in the running state, but not in the failover state. The read-only instance and the primary instance are in the same region. A primary RDS instance can have up to five read-only instances. Request parameters

| Parameter | Type | Require d | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to CreateReadOnlyDBInstance. |
| RegionId | String | Yes | The region ID of the instance. It can be up to 50 characters in length. You can call the DescribeRegions operation to query the most recent region list. |
| ZoneId | String | Yes | The zone ID of the instance. You can call the DescribeRegions operation to query the most recent zone list. |
| DBInstanceId | String | Yes | The ID of the primary instance. |
| EngineVersion | String | Yes | The engine version of the database. The read-only instance must run the same database engine version as the primary instance. Valid values: 5.6 5.7 |
| DBInstanceClass | String | Yes | The type of the instance. For more information, see |
| DBInstanceStorag e | Intege r | Yes | The user-defined storage space. Valid values: 5 to 1000. This value must be in 5 GB increments. Unit: GB. |
| DBInstanceDescri ption | String | No | The description of the instance. It can be up to 256 bytes in length and can contain letters, underscores ( ), and hyphens (-). _ The digits must be 2 to 256 characters in length. The description must start with a letter and cannot start with http:// or https://. |
| ClientToken | String | Yes | The client token that is used to ensure the idempotence of the request. |
| InstanceNetwork Type | String | No | The network type of the instance. Valid values: VPC and Classic. Default value: Classic. |
| VPCId | String | No | The ID of the VPC. |
| VSwitchId | String | No | The ID of the VSwitch. |

| psaraDB for RDS |   |   | Developer Guide·API referenc |
|---|---|---|---|

| Parameter | Type | Require d | Description |
|---|---|---|---|
| PrivateIpAddress | String | No | The IP address of the VPC that belongs to VSwitchId. If no value is specified, the system automatically allocates a VPC IP address based on VPCId and VSwitchId. |

Response parameters

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> | - | For more information, see Common response parameters. |
| DBInstanceId | String | The ID of the instance. |
| OrderId | String | The ID of the order. |
| ConnectionStrin g | String | The endpoint used to connect to the database. |
| Port | String | The port used to connect to the database. |

Examples Sample request s

```
https://rds.example.com/?Action=CreateReadOnlyDBInstance &RegionId=cn-hangzhou &ZoneId=cn-hangzhou-b &DBInstanceId=rds-xxxxx &EngineVersion=5.6 &DBInstanceClass=rds.mys2.small &DBInstanceStorage=10 &PayType=Postpaid &ClientToken=ETnLKxxxxx &<[Common request parameters]>
```

Sample success responses XML format

```xml
<CreateDBInstanceResponse> <OrderId>10078937xxxxx</OrderId> <ConnectionString>rds-xxxxx.mysql.rds.aliyuncs.com </ConnectionString> <DBInstanceId>rds-xxxxx</DBInstanceId> <port>3306</port> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> </CreateDBInstanceResponse>
```

JSON format

```json
{ "OrderId": "100789370230206", "ConnectionString": "rds-xxxxx.mysql.rds.aliyuncs.com", "DBInstanceId": "rds-xxxxx", "Port": "3306", "RequestId": "1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC" }
```

#### 2.3.21 DescribeDBInstanceSSL

Description You can call this operation to query the SSL link of an instance. Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeDBInstanceSSL. |
| DBInstanceId | String | Yes | The ID of the instance. |

Response parameters

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> | - | For more information, see Common response parameters. |
| ConnectionString | String | The endpoint protected by the SSL certificate. |
| SSLExpireTime | String | The expiration time of the SSL certificate. The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ssZ format. |
| RequireUpdate | String | Indicates whether an immediate update is required. Valid values: Yes and No. |
| RequireUpdateRea son | String | The reason why an update is recommended. |

#### 2.3.22 ModifyDBInstanceSSL

Description You can call this operation to modify the SSL link of an instance. Request parameters

| Parameter | Type | Requ ired | Description |
|---|---|---|---|
| Action | Strin g | Yes | The operation that you want to perform. Set the value to ModifyDBInstanceSSL. |
| DBInstanceI d | Strin g | Yes | The ID of the instance. |
| ConnectionS tring | Strin g | Yes | Each instance can only have one endpoint protected by the SSL certificate. The SSL certificate can be created or updated for the endpoint. |

Response parameters

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> | - | Common response parameters. |
| SSLExpireTime | String | The expiration time of the SSL certificate. The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ssZ format. |

#### 2.3.23 DescribeDBInstanceTDE

Description You can call this operation to query the TDE status of an instance. Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeDBInstanceTDE. |
| DBInstanceId | String | Yes | The ID of the instance. |

Response parameters

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> |   | For more information, see Common response parameters. |
| TDEStatus | String | The TDE status of the instance. Valid values: Enabled and Disabled. |
| Databases | List<DataBase> | The array that consists of Database data. |

Database parameters:

| Parameter | Type | Description |
|---|---|---|
| DBName | String | The name of the database. |
| TDEStatus | String | The TDE status of the database. Valid values: Enabled and Disabled. |

#### 2.3.24 ModifyDBInstanceTDE

Description You can call this operation to modify the TDE status of an instance. Request parameters

| Parameter | Type | Require d | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to ModifyDBInstanceTDE. |
| DBInstanceId | String | Yes | The ID of the instance. |
| TDEStatus | String | Yes | The TDE status of the instance. Valid values: Enabled and Disabled. |
| DBName | String | No | The name of the database. Up to 50 names can be entered in a single request. Separate multiple names with commas (,). |

Response parameters This operation returns only common response parameters. For more information, see Common response parameters.

### 2.4 Database management

#### 2.4.1 CreateDatabase

Description You can call this operation to create a new database in an instance. Before you call this operation, make sure that the following requirements are met: The instance is in the running state. The instance is not locked. The maximum number of databases in the instance is not reached. The instance is a primary instance. Not e This operation is not supported on PolarDB. You can create databases in PolarDB instances by executing CREATE DATABASE statements.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to CreateDatabase. |
| DBInstanceId | String | Yes | The ID of the instance. |
| DBName | String | Yes | The unique name of the database. The name can be up to 64 characters in length and can contain lowercase letters, digits, and underscores ( ). It must start with a letter. _ For information about invalid characters, see Forbidden keywords. |
| CharacterSet Name | String | Yes | The character set. Valid values: MySQL: utf8, gbk, latin1, and utf8mb4 SQL Server: Chinese PRC CI AS, Chinese PRC CS AS, _ _ _ _ _ _ SQL Latin1 General CP1 CI AS, _ _ _ _ _ SQL Latin1 General CP1 CS AS, and Chinese PRC BIN _ _ _ _ _ _ _ |
| DBDescription | String | No | The description of the database. It must be 2 to 256 characters in length and can contain letters, digits, underscores ( ), and hyphens (-). _ It must start with a letter and cannot start with http:// or https://. |

Response parameters This operation returns only common response parameters. Examples Sample request s

```
https://rds.example.com/?Action=CreateDatabase &CharacterSetName=gbk &DBName=testDB &DBInstanceId=rds-xxxxx &<[Common request parameters]>
```

Sample success responses XML format

```xml
<CreateDatabaseResponse> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> </CreateDatabaseResponse>
```

JSON format

```json
{ "RequestID":"1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC" }
```

#### 2.4.2 DeleteDatabase

Description You can call this operation to delete a database from an instance. Before you call this operation, make sure that the following requirements are met: The instance is in the running state. The instance is a primary instance. Not e This operation is not supported on PolarDB. You can delete databases from PolarDB instances by executing DROP DATABASE statements. Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DeleteDatabase. |
| DBInstanceI d | String | Yes | The ID of the instance. |
| DBName | String | Yes | The name of the database. |

Response parameters

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> | - | Common response parameters. |

Examples Sample request s

```
https://rds.example.com/?Action=DeleteDatabase &DBName=testDB &DBInstanceId=rds-xxxxx &<[Common request parameters]>
```

Sample success responses XML format

```xml
<DeleteDatabaseResponse> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> </DeleteDatabaseResponse>
```

JSON format

```json
{ "RequestId":"1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC" }
```

#### 2.4.3 DescribeDatabases

Description You can call this operation to query the databases of a specified instance or information of a specified database. If the request parameters are entered incorrectly, an error prompt is returned, and the returned data is empty. Not e This operation is not supported on PolarDB. Request parameters

| Paramete r | Type | Requir ed | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeDatabases. |
| DBInstanc eId | String | Yes | The ID of the instance. |
| DBName | String | No | The name of the database. |
| DBStatus | String | No | The state of the database. Valid values: Creating, Running, and Deleting. |

Response parameters

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> | - | Common response parameters. |
| Databases | List<Database> | The array that consists of Database data. |

Database parameters

| Parameter | Type | Description |
|---|---|---|
| DBName | String | The name of the database. |
| DBInstanceId | String | The ID of the instance to which the database belongs. |
| Engine | String | The engine of the database. |

| Developer Guide·A | PI reference | ApsaraDB for RD |
|---|---|---|

| Parameter | Type | Description |
|---|---|---|
| DBStatus | String | The status of the database. Valid values: Creating, Running, and Deleting. |
| CharacterSetN ame | String | The character set. |
| DBDescription | String | The description of the database. |
| Accounts | List<AccountPrivilegeI nfo> | The array that consists of AccountPrivilegeInfo data. |
| Account | String | The name of the account. |
| AccountPrivileg e | String | The permissions of the account on the database. |

AccountPrivilegeInfo parameters

| Parameter | Type | Description |
|---|---|---|
| Account | String | The name of the account. |
| AccountPrivilege | String | The permissions of the account on the database. |

Examples Sample request s

```
https://rds.example.com/?Action=DescribeDatabases &DBInstanceId=rds-xxxxx &<Common request parameters>
```

Sample success responses XML format

```xml
<DescribeDatabasesResponse> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> <Databases> <Database> <Engine>MySQL</Engine> <DBName>testdb</DBName> <CharacterSetName>utf8</CharacterSetName> <DBStatus>Creating</DBStatus> <DBInstanceId>rds-xxxxx</DBInstanceId> <Accounts> <AccountPrivilegeInfo></AccountPrivilegeInfo> <Accounts> </Database> </Databases> </DescribeDatabasesResponse>
```

JSON format

```json
{ "RequestId": "1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC", "Databases":
    { "Database":
        [ { "Engine": "MySQL",
            "CharacterSetName": "utf8",
            "DBStatus": "Creating",
            "DBDescription": "",
            "DBInstanceId": "rds-xxxxx",
            "Accounts": { " AccountPrivilegeInfo": [] },
            "DBName": "testdb" }] }
```

`}`

#### 2.4.4 ModifyDBDescription

Description You can call this operation to modify the description of a database to facilitate user records. For example, you can modify the description of a database to Database A for Alibaba Cloud testing environment. Not e This operation is not supported on PolarDB. Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to ModifyDBDescription. |
| DBInstanceId | String | Yes | The ID of the instance. |
| DBName | String | Yes | The name of the database. |

|   | Developer Guide·API | reference |   | ApsaraDB for RD | S |
|---|---|---|---|---|---|

| Parameter | Type | Required | Description |
|---|---|---|---|
| DBDescription | String | Yes | The description of the database. |

Response parameters This operation returns only common response parameters. Examples Sample request s

```
https://rds.example.com/?Action=ModifyDBDescription &DBInstanceId=rds-xxxxx &DBInstanceDescription=testDBdescribe &<Common request parameters>
```

Sample success responses XML format

```xml
<ModifyDBDescriptionResponse> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> </ModifyDBDescriptionResponse>
```

JSON format

```json
{ "RequestId": "1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC" }
```

### 2.5 Account management

#### 2.5.1 CreateAccount

Description In the same instance, one account can manage multiple databases by using different permissions. You can call this operation to create an account for a database. Before you call this operation, make sure that the following requirements are met: The instance is in the running state. The database is in the running state. The instance is not locked. The maximum number of accounts for a single instance is not reached.

| Parameter | Type | Requi red | Description |
|---|---|---|---|
| Action | Strin g | Yes | The operation that you want to perform. Set the value to CreateAccount. |
| DBInstanceId | Strin g | Yes | The ID of the instance. |
| AccountName | Strin g | Yes | The unique name of the account. The name can be up to 16 characters in length and can contain lowercase letters, digits, and underscores ( ). It must start with a letter. For information about invalid _ characters, see Forbidden keywords. |
| AccountPassw ord | Strin g | Yes | The password for the account. It must be 6 to 32 characters in length and can contain letters, digits, and underscores ( ). _ |
| AccountType | Strin g | No | The type of the account. Valid values: Normal and Super. Default value: Normal. PolarDB can have only a single initial account. You must use the initial account to log on to the database and create other types of accounts. |
| AccountDescri ption | Strin g | No | The description of the account. It must be 2 to 256 characters in length and can contain letters, digits, underscores ( ), and hyphens (-). _ It must start with a letter and cannot start with http:// or https://. |

Response parameters This operation returns only common response parameters. Examples Sample request s

```
https://rds.example.com/?Action=CreateAccount &AccountName=testacc02 &AccountPassword=pwxxxxx &DBInstanceId=rds-xxxxx &<[Common request parameters]>
```

Sample success responses XML format

```xml
<CreateAccountResponse> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> </CreateAccountResponse>
```

JSON format

```json
{ "RequestId":"1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC" }
```

#### 2.5.2 DeleteAccount

Description You can call this operation to delete a database account. The instance must be in the running state. Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DeleteAccount. |
| DBInstanceId | String | Yes | The ID of the instance to which the database belongs. |
| AccountNam e | String | Yes | The unique name of the account. The name can be up to 16 characters in length and can contain lowercase letters, digits, and underscores ( ). It must start with a letter. For more _ information about invalid characters, see Forbidden keywords. |

Response parameters This operation returns only common response parameters. Examples Sample request s

```
https://rds.example.com/?Action=DeleteAccount &DBInstanceId=rds-xxxxx &AccountName=testacc01 &<[Common request parameters]>
```

Sample responses XML format

```xml
<DeleteAccountResponse> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> </DeleteAccountResponse>
```

JSON format

```json
{ "RequestID":"1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC" }
```

#### 2.5.3 DescribeAccounts

Description You can call this operation to query the accounts for a specified instance and database or the information of a specified account.

| Parameter | Typ e | Required | Description |
|---|---|---|---|
| Action | Strin g | Yes | The operation that you want to perform. Set the value to DescribeAccounts. |
| DBInstanceI d | Strin g | Yes | The ID of the instance. |
| AccountNa me | Strin g | Yes | The name of the account. |

Response parameters

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> |   | Common response parameters. |
| Accounts | List<DBInstanceAccount> | The array that consists of DBInstanceAccount data. |

DBInstanceAccount parameters

| Parameter | Type | Description |
|---|---|---|
| DBInstanceId | String | The ID of the instance to which the account belongs. |
| AccountName | String | The name of the database account. |
| AccountStatus | String | The account status. Valid values: Unavailable and Available. |
| AccountDescription | String | The description of the account. |
| DatabasePrivileges | List<DatabasePrivileg e> | The array that consists of DatabasePrivileges data. |
| AccountType | String | The type of the account. Valid values: Normal and Super. |

DatabasePrivilege parameters

| Parameter | Type | Description |
|---|---|---|
| DBName | String | The name of the database. |
| AccountPrivilege | String | The name of the database account. |

Examples Sample request s

```
https://rds.example.com/?Action=DescribeAccounts &DBInstanceId=rds-xxxxx &<Common request parameters>
```

Sample responses XML format

```xml
<DescribeAccountsResponse> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> <Accounts> <DBInstanceAccount> <AccountName>MySQL</AccountName> <DBInstanceId>testdb</DBInstanceId> <AccountStatus>utf8</AccountStatus> <AccountDescription> </AccountDescription> <DatabasePrivileges> <DatabasePrivilege></DatabasePrivilege> </DatabasePrivileges> <DBInstanceAccount> </Accounts> </DescribeAccountsResponse>
```

JSON format

```json
{ "Accounts":
    { "DBInstanceAccount":
        [ { "AccountDescription": "",
            "DBInstanceId": "rds-xxxxx",
            "DatabasePrivileges": { "DatabasePrivilege": [] },
            "AccountStatus": "Unavailable",
            "AccountName": "testaccount" } ] },
    "RequestId": "1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC" }
```

#### 2.5.4 GrantAccountPrivilege

Description You can call this operation to grant database access permissions to accounts. A single account can be associated with one or more databases. If the specified account already has access permissions on the specified database, the operation directly returns a successful response. The instance must be in the running state. Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to GrantAccountPrivilege. |
| DBInstanceId | String | Yes | The ID of the instance to which the database belongs. |
| AccountName | String | Yes | The name of the account. |
| DBName | String | Yes | The name of the database associated with the account. |
| AccountPrivilege | String | Yes | The permissions of the account. Valid values: ReadOnly and ReadWrite. |

Response parameters This operation returns only common response parameters. For more information, see Common response parameters. Examples Sample request s

```
https://rds.example.com/?Action=GrantAccountPrivilege &AccountName=testacc02 &AccountPrivilege=readwrite &DBName=testdb03 &DBInstanceId=rds-xxxxx &<Common request parameters>
```

Sample responses XML format

```xml
<GrantAccountPrivilegeResponse> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> </GrantAccountPrivilegeResponse>
```

JSON format

```json
{ "RequestId":"1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC"}
```

#### 2.5.5 RevokeAccountPrivilege

Description You can call this operation to revoke database access permissions from an account. Before you call this operation, ensure that the following requirements are met: The instance is in the running state. The database is in the running state.

| Parameter | Type | Requir ed | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to RevokeAccountPrivilege. |
| DBInstanceI d | String | Yes | The ID of the instance to which the database belongs. |
| AccountNa me | String | Yes | The name of the account. |
| DBName | String | Yes | The name of the database. |

Response parameters This operation returns only common response parameters. For more information, see Common response parameters. Examples Sample request s

```
https://rds.example.com/?Action=RevokeAccountPrivilege &AccountName=testacc02 &DBName=testdb03 &DBInstanceId=rds-xxxxx &<Common request parameters>
```

Sample responses XML format

```xml
<RevokeAccountPrivilegeResponse> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> </RevokeAccountPrivilegeResponse>
```

JSON format

```json
{ "RequestId":"1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC"}
```

#### 2.5.6 ModifyAccountDescription

Description You can call this operation to modify the description of an account to facilitate user records. For example, you can modify the description of an account to Account A for Alibaba Cloud testing environment. Request parameters

| Parameter | Typ e | Required | Description |
|---|---|---|---|
| Action | Strin g | Yes | The operation that you want to perform. Set the value to ModifyAccountDescription. |
| DBInstanceId | Strin g | Yes | The ID of the instance for which the account description is modified. |
| AccountName | Strin g | Yes | The unique name of the account. The name can be up to 16 characters in length and can contain lowercase letters, digits, and underscores ( ). It must start with a letter. For more information _ about invalid characters, see Forbidden keywords. |
| AccountDescri ption | Strin g | Yes | The description of the account. It can be up to 256 characters in length and can contain letters, digits, underscores ( ), and hyphens _ (-). It cannot start with http:// or https://. It must start with a letter. |

Response parameters

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> | - | Common response parameters. |

Examples Sample request s

```
https://rds.example.com/?Action=ModifyAccountDescription &DBInstanceId=rds-xxxxx &AccountName=testacc01 &AccountDescription=testAccoutdescribe &<Common request parameters>
```

Sample responses XML format

```xml
<ModifyAccountDescription> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> </ModifyAccountDescription>
```

JSON format

```json
{ "RequestId": "1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC"}
```

#### 2.5.7 ResetAccountPassword

You can call this operation to reset the account password. Before you call this operation, ensure that the following requirements are met: The instance is in the running state and not locked by the system. Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to ResetAccountPassword. |
| DBInstanceId | String | Yes | The ID of the instance for which the account password is reset. |
| AccountName | String | Yes | The name of the account. |
| AccountPass word | String | Yes | The new password. It must be 6 to 32 characters in length and can contain letters, digits, and underscores ( ). _ |

Response parameters This operation returns only common response parameters. For more information, see Common response parameters. Examples Sample request s

```
https://rds.example.com/?Action=ResetAccountPassword &AccountName=testacc02 &AccountPassword=pwxxxxx &DBInstanceId=rds-xxxxx &<Common request parameters>
```

Sample responses XML format

```xml
<ResetAccountPasswordResponse> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> </ResetAccountPasswordResponse>
```

JSON format

```json
{ "RequestId":"1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC"}
```

#### 2.5.8 ResetAccount

Description You can call this operation to reset the initial account of an instance.

| Parameter | Type | Requir ed | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to ResetAccount. |
| DBInstanceId | String | Yes | The ID of the instance. |
| AccountNam e | String | Yes | The name of the account. |
| AccountPass word | String | Yes | The password of the account. |

Response parameters

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> | - | Common response parameters. |

### 2.6 Backup and restoration

#### 2.6.1 CreateBackup

Description You can call this operation to manually create a backup. Up to 10 backups can be created for an instance in a single day. Before you call this operation, ensure that the following requirements are met: The instance is in the running state. The most recent backup has been completed. Request parameters

| Parameter | Type | Requ ired | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to CreateBackup. |
| DBInstance Id | String | Yes | The ID of the instance. |
| BackupMet hod | String | No | The backup method. Valid values: Logical and Physical. Default value: Physical. Logical backup cannot be used for instances without databases. SQL Server instances only support physical backup. |

| Parameter | Type | Requ ired | Description |
|---|---|---|---|
| BackupStr ategy | String | No | The logical backup range. Valid values: db: single-database backup. instance: instance backup. This parameter is valid only when BackupMethod is set to Logical. |
| DBName | String | No | The name of the database for logical single-database backup. This parameter is valid only when BackupMethod is set to Logical and BackupStrategy is set to db. |
| BackupTyp e | String | No | The backup type. Valid values: Auto: specifies whether it is a full backup or an incremental backup through automatic calculation. FullBackup: specifies a full backup. Default value: Auto. |

Response parameters

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> | N/A | Common response parameters. |

Examples Sample request s

```
https://rds.example.com/?Action= CreateBackup &DBInstanceId=rds-xxxxx &<Common request parameters>
```

Sample success responses XML format

```xml
<CreateBackupResponse> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> </CreateBackupResponse>
```

JSON format

```json
{ "RequestId":"1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC"}
```

#### 2.6.2 CloneDBInstance

Description You can call this operation to clone a new instance with historical data based on the backup file of an existing instance or a specified time. The new instance will have the same whitelist, SQL audit, alert threshold, backup, and parameter settings as the existing instance. The data in the new instance is the same as historical data in the backup file. The clone feature can only be used with MySQL engines. Database account information is cloned differently for different account types: If the primary instance has a privileged account, instances that are cloned from it will also carry the same privileged account information. If the primary instance has only standard accounts, instances that are cloned from it will also carry the information of the account used when the backup file is generated or at the specified time. Request parameters

| Parameter | Type | Require d | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to CloneDBInstance. |
| DBInstanceId | String | Yes | The ID of the instance. |
| BackupId | String | No | The ID of the backup set. You can call the DescribeBackups operation to query backup set IDs. |
| RestoreTime | String | No | A point in time within the backup retention period to obtain a backup set from. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. Example: 2011-06- 11T16:00:00Z. Either BackupId or RestoreTime is required. |
| DBInstanceClass | String | No | Optional. The type of the instance. For more information, see Instance types in Appendix. If it is not specified, the new instance is of the same type as the primary instance. |
| DBInstanceStora ge | String | No | The disk space. Unit: GB. This value must be in 5 GB increments and is the same as that of the primary instance by default. Valid values: RDS instances of the dedicated host type: 3000. RDS instances of other types: 5 to 2000. |
| InstanceNetwork Type | String | No | The network type of the instance. Valid values: Classic and VPC. This value is the same as that of the primary instance by default. |
| VPCId | String | No | The ID of the VPC. |
| VSwitchId | String | No | The ID of the VSwitch. |
| PrivateIpAddress | String | No | The VPC IP address that belongs to the specified VSwitch. If no value is specified, the system automatically assigns a VPC IP address. |

Response parameters

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> | N/A | For more information, see Common response parameters. |
| DBInstanceId | String | The ID of the instance. |

| eveloper Guide·API referen | ce | ApsaraDB for RD |
|---|---|---|

| Parameter | Type | Description |
|---|---|---|
| OrderId | Integer | The ID of the order. |

#### 2.6.3 DescribeBackups

Description You can call this operation to search for a set of instance backups. The set of backups must be in the Success state, indicating that they can be used to restore an instance. RDS provides backup files for you to download. When DownloadLink is NULL, RDS does not provide a download URL. When DownloadLink is not NULL, you can use this URL to download the backup file through Wget (with double quotation marks), a browser, or a user program. The expiration time for this URL is specified by LinkExpiredTime. Use it before the expiration time. If the BackupSet has expired, the following error code is displayed:

```
<? xml version="1.0" encoding="UTF-8" ? ><Error><Code>AccessDenied</Code><Message>Request has expired. </Message><Expires>2012-12-25T09:47:52.000Z</Expires><ServerTime>2012-12-25T 09:49:00.000Z</ServerTime><RequestId>50D9768CA801C2F102005C70</RequestId><HostId>oss-test .aliyun-inc.com</HostId></Error>
```

Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | Strin g | Yes | The operation that you want to perform. Set the value to DescribeBackups. |
| DBInstanceId | Strin g | Yes | The ID of the instance for which the backup set is queried. |
| BackupId | Integ er | No | The ID of the backup set. |
| BackupStatus | Strin g | No | The status of the backup set. Valid values: Success and Failed. |
| BackupMode | Strin g | No | The backup mode. Valid values: Automated and Manual. |
| StartTime | Strin g | Yes | The beginning of the time range where the query is performed. Specify the time in the yyyy-MM-ddTHH:mm:ssZ format. Example: 2011-06-11T15:00Z. |
| EndTime | Strin g | Yes | The end of the time range where the query is performed. Specify the time in the yyyy-MM-ddTHH:mm:ssZ format. Example: 2011-06- 11T16:00Z. The end time must be later than the start time. |

| Parameter | Type | Required | Description |
|---|---|---|---|
| PageSize | Integ er | No | The number of entries to return on each page. Valid values: 30, 50, and 100. Default value: 30. |
| PageNumber | Integ er | No | The number of the page to return. Pages start from page 1 but must be equal to or smaller than the maximum Integer value. Default value: 1. |

Response parameters

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> |   | For more information, see Common response parameters. |
| TotalRecordCount | Interger | The total number of entries. |
| PageNumber | Integer | The number of the page returned. |
| PageRecordCount | Integer | The number of backup sets on the current page. |
| Items | List<Backup> | The array that consists of Backup data. |

#### 2.6.4 CreateTempDBInstance

Description Not e You can create a temporary instance based on a backup set or a point in time within the past seven days. When a temporary instance is created, accounts and databases inherit the backup set data. You can call this operation to create a temporary instance. Before you call this operation, ensure that the following requirements are met: The instance is in the running state. The instance is not undergoing any migration tasks. The instance is not locked by the system. The current status of the instance backup set is Success. Request parameters

| Parameter | Type | Require d | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to CreateTempDBInstance. |
| DBInstanceId | String | Yes | The ID of the instance to be created. |

| Developer Guide | ·API referenc | e | ApsaraDB for RD |
|---|---|---|---|

| Parameter | Type | Require d | Description |
|---|---|---|---|
| BackupId | Integer | No | The ID of the backup set. |
| RestoreTime | String | No | The restoration time of the backup set. It can be any time within the past seven days that is more than 30 minutes before the current time. Specify the time in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC. Example: 2011-06-11T16:00:00Z. |

Response parameters

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> |   | Common response parameters. |
| TempDBInstanceId | String | The ID of the temporary instance. |

Examples Sample request s

```
https://rds.example.com/?Action=CreateTempDBInstance &BackupId=90262 &DBInstanceId=rds-xxxxx &<Common request parameters>
```

Sample responses XML format

```xml
<CreateTempDBInstanceResponse> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> <TempDBInstanceId>sub-xxxxx</TempDBInstanceId> </CreateTempDBInstanceResponse>
```

JSON format

```json
{ "RequestId":"1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC", "TempDBInstanceId":"sub-xxxxx"}
```

#### 2.6.5 DescribeBackupPolicy

Description You can call this operation to query the backup policy configured for the system. RDS periodically backs up an instance based on the user-defined system configuration.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeBackupPolicy. |
| DBInstanceId | String | Yes | The ID of the instance for which the backup policy is queried. |

Response parameters

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> |   | Common response parameters. |
| BackupRetentionPerio d | String | The data backup retention period. Unit: days. Valid values: 1 to 30. |
| PreferredBackupTime | String | The backup time. The time is in the HH:mmZ to HH:mmZ format. |
| PreferredBackupPerio d | String | The backup day. Valid values: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, and Sunday. |
| BackupLog | String | The log backup status. Valid values: Enable and Disabled. |
| LogBackupRetentionP eriod | String | The log backup retention period. Unit: days. Valid values: 1 to 30. |

#### 2.6.6 ModifyBackupPolicy

Description You can call this operation to modify a backup policy. RDS periodically backs up instances based on the user-defined system configuration. Request parameters

| Parameter | Type | Requir ed | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to ModifyBackupPolicy. |
| DBInstanceId | String | Yes | The ID of the instance for which the backup policy is modified. |
| PreferredBackupTime | String | Yes | The backup time. Format: HH:mmZ to HH:mmZ. |
| PreferredBackupPerio d | String | Yes | The backup day. Valid values: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, and Sunday. |

| Parameter | Type | Requir ed | Description |
|---|---|---|---|
| BackupRetentionPerio d | String | No | The data backup retention period. Unit: days. Valid values: 1 to 30. Default value: 7. |
| BackupLog | String | No | The log backup status. Valid values: Enable and Disabled. Default value: Enable. |
| LogBackupRetentionP eriod | String | No | The log backup retention period. It cannot exceed BackupRetentionPeriod. Unit: days. Valid values: 1 to 30. When you enable log backup, you can configure the log backup retention period. This operation is only supported on MySQL, PostgreSQL, and PPAS. |

Response parameters

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> | - | Common response parameters. |

Examples Sample request s

```
https://rds.example.com/?Action=ModifyBackupPolicy &DBInstanceId=rds-xxxxx &PreferredBackupTime=00:00Z—01:00Z &PreferredBackupPeriod=Monday &<Common request parameters>
```

Sample responses XML format

```xml
<ModifyBackupPolicyResponse> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> </ModifyBackupPolicyResponse>
```

JSON format

```json
{ "RequestId":"1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC"}
```

#### 2.6.7 RestoreDBInstance

Description You can call this operation to overwrite the contents of an instance and restore a backup set to that instance. Before you call this operation, ensure that the following requirements are met: The instance is in the running state. The instance is not undergoing any migration tasks. The instance is not locked by the system. The current status of the instance backup set is Success. Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to RestoreDBInstance. |
| DBInstanceId | String | Yes | The ID of the instance to which the backup set is restored. |
| BackupId | Integer | Yes | The ID of the backup set. |

Response parameters

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> | - | For more information, see Common response parameters. |

Examples Sample request s

```
https://rds.example.com/?Action=RestoreDBInstance &BackupId=103312 &DBInstanceId=rds-xxxxx &<Common request parameters>
```

Sample responses XML format

```xml
<RestoreDBInstanceResponse> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> </RestoreDBInstanceResponse>
```

JSON format

```json
{"RequestId":"1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC"}
```

#### 2.6.8 DeleteBackup

You can call this operation to delete data backup files that have been stored for longer than seven days or longer than the log backup retention period. This operation only deletes the specified backup sets for the target instance. It does not delete the backup sets for associated instances, such as read-only, disaster recovery, or cloned instances. Before you call this operation, make sure that the following requirements are met: The instance is in the running state. The database engine is MySQL or PolarDB. Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DeleteBackup. |
| DBInstanceI d | String | Yes | The ID of the instance. |
| BackupId | String | Yes | The ID of the backup set. You can call the DescribeBackups operation to query the backup set IDs. You can enter up to 100 backup set IDs in a single request. Separate multiple IDs with commas (,). Among the query results of DescribeBackups, you can only delete the backup sets that are in the Enabled state. |

Response parameters This operation returns only common response parameters. For more information, see Common response parameters.

### 2.7 Monitoring management

#### 2.7.1 DescribeResourceUsage

Description You can call this operation to query the resource usage information of an instance. When this operation is called, the system returns the amount of space occupied by the specified instance. DBInstanceId is used to obtain instance resource usage information. Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeResourceUsage. |
| DBInstanceId | String | Yes | The ID of the instance for which the resource usage information is queried. |

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> |   | Common response parameters. |
| DBInstanceId | String | The ID of the instance for which the resource usage information was queried. |
| Engine | String | The type of the database. |
| DiskUsed | Integer | The total space occupied by both data files and log files. Unit: Byte. -1 indicates no data. |
| DataSize | Integer | The disk space that is used to store user data. Unit: Byte. -1 indicates no data. |
| LogSize | Integer | The disk space that is used to store log files. Unit: Byte. -1 indicates no data. |
| BackupSize | Integer | The total space occupied by backup data. Unit: Byte. -1 indicates no data. |
| ColdBackupSize | Integer | The total space occupied by cold backup data. Unit: Byte. -1 indicates no data. |
| SQLSize | Integer | The total space occupied by SQL data. Unit: Byte. -1 indicates no data. |

#### 2.7.2 DescribeDBInstancePerformance

Description You can call this operation to query the performance metrics of an instance over a specified period of time based on the performance parameters. There are three output formats based on different query time ranges: When the query time range is less than or equal to one day, performance metrics are displayed at one-minute intervals. Queries with the time range from one to seven days are not supported. When the query time range is greater than seven days but less than or equal to 15 days, performance metrics are displayed at one-hour intervals. Queries with the time range greater than 15 days but less than 30 days are not supported. When the query time range is greater than or equal to 30 days but less than or equal to one year, performance metrics are displayed at one-day intervals. Not e When the instance space usage key is MySQL_SpaceUsage or SQLServer_SpaceUsage, performance metrics can be queried only when the time range is less than or equal to one day.

| Parameter | Type | Require d | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeDBInstancePerformance. |
| DBInstanc eId | String | Yes | The ID of the instance. |
| Key | Intege r | Yes | The performance metrics. Separate performance metrics with commas (,). For more information, see Performance parameters. |
| StartTime | String | Yes | The beginning of the time range to query. Specify the time in the ISO 8601 standard in the YYYY-MM-DDTHH:mmZ format. Example: 2012- 06-11T15:00Z. |
| EndTime | String | Yes | The end of the time range to query. Specify the time in the ISO 8601 standard in the YYYY-MM-DDTHH:mmZ format. Example: 2012-06- 11T15:00Z. |

Response parameters

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> | N/A | Common response parameters |
| DBInstanceId | String | The ID of the instance. |
| Engine | String | The engine of the database. |
| StartTime | String | The beginning of the time range where the query was executed. The time follows the ISO 8601 standard in the YYYY-MM-DDTHH:mmZ format. Example: 2011-05-30T03:29Z. |
| EndTime | String | The end of the time range where the query was executed. The time follows the ISO 8601 standard in the YYYY-MM-DDTHH:mmZ format. Example: 2011- 05-30T03:29Z. The end time must be later than the start time. |
| PerformanceKeys | List<PerformanceKey> | The array that consists of PerformanceKey data. Format: {perf1, perf2, perf3, ...}. |

Examples Sample request s

```
https://rds.example.com/?Action=DescribeDBInstancePerformance &DBInstanceId=rds-xxxxx &key= MySQL_xxxxx &StartTime=2013-01-11T15:00:00Z &EndTime=2013-06-05T15:00:00Z &<Common request parameters>
```

Sample success responses XML format

```xml
<DescribeDBInstancePerformanceResponse> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> <DBInstanceID>rds-xxxxx</DBInstanceID> <StartTime>2013-01-11T15:00:00Z</StartTime> <EndTime>2013-10-17T15:00Z</EndTime> <Engine>MySQL</Engine> <PerformanceKeys> <PerformanceKey> <Key>MySQL_xxxxx</Key> <Unit>KB</Unit> <ValueFormat>recv_k&amp;sent_k</ValueFormat> <Values><Values/> </PerformanceKey> </PerformanceKeys> </DescribeDBInstancePerformanceResponse>
```

JSON format

```json
{ "RequestId"1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC, "DBInstanceID": rds-xxxxx, "StartTime": "2012-06-11T15:00Z", "EndTime": "2013-10-17T15:00Z", "Engine": "MySQL", "PerformanceKeys":
    { PerformanceKey[ {
        "Key": "MySQL_xxxxx",
        "Unit": "KB",
        "ValueFormat": "recv_k&sent_k",
        "Values": { "PerformanceValue":[] } } ] }}
```

#### 2.7.3 DescribeDBInstanceMonitor

Description You can call this operation to query the monitoring behavior of an instance. Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeDBInstanceMonitor. |

| Developer Guide | ·API referen | ce | ApsaraDB for RD |
|---|---|---|---|
| Parameter | Type | Required | Description |
| DBInstanceI d | String | Yes | The ID of the instance for which the monitoring behavior is queried. |

Response parameters

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> | - | Common response parameters. |
| Period | String | The monitoring period. Unit: seconds. |

#### 2.7.4 ModifyDBInstanceMonitor

Description You can call this operation to modify the monitoring behavior of an instance. Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to ModifyDBInstanceMonitor. |
| DBInstanceId | String | Yes | The ID of the instance for which the monitoring behavior is modified. |
| Period | String | Yes | The monitoring period. Unit: seconds. Valid values: 60 and 300. Default value: 300. |

Response parameters

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> | - | For more information, see Common response parameters. |

### 2.8 Parameter management

#### 2.8.1 DescribeParameterTemplates

Description You can call this operation to query the parameter template list. The list includes parameter names, default parameter values, whether they can be modified, whether the database must be restarted for the parameters to take effect, and regular expressions acting as parameter validation rules.

| Parameter | Type | Requir ed | Description |
|---|---|---|---|
| Action | Strin g | Yes | The operation that you want to perform. Set the value to DescribeParameterTemplates. |
| Engine | Strin g | Yes | The engine of the database. Valid values: mysql: MySQL mssql: SQL Server PostgreSQL: PostgreSQL POLARDB: PolarDB |
| EngineVersi on | Strin g | Yes | The engine version of the database. Valid values: MySQL: 5.6 and 5.7 SQL Server: 2008 R2 PostgreSQL: 9.4 and 10.0 PolarDB: 11 |

Response parameters

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> | - | Common response parameters. |
| Engine | String | The engine of the database. |
| EngineVersion | String | The engine version of the database. |
| ParameterCount | Integer | The number of parameters. |
| Parameters | List<TemplateRecord> | The array that consists of TemplateRecord data. Format: {parameter1, parameter2, parameter3, ...}. |

Examples Sample request s

```
https://rds.example.com/?Action=DescribeParameterTemplates &Engine=MySQL &EngineVersion=5.6 &<Common request parameters>
```

Sample success responses XML format

```xml
<DescribeParameterTemplatesResponse> <Engine>mysql</Engine> <EngineVersion>5.6</EngineVersion> <ParameterCount>1</ParameterCount> <Parameters> <TemplateRecord> <CheckingCode>[0-100]</CheckingCode> <ForceRestart>True</ForceRestart> <Factor>1</Factor> <ParameterDescription>test</ParameterDescription> <ParameterName>fill factor</ParameterName> <ParameterValue>0</ParameterValue> <ForceModify>True</ForceModify> <Unit>INT</Unit> </TemplateRecord> </Parameters> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> </DescribeParameterTemplatesResponse>
```

JSON format

```json
{"Engine": "mysql", "EngineVersion": "5.6", "ParameterCount":1, "Parameters":
    { "TemplateRecord": [ {
        "ParameterDescription": "test",
        "ForceRestart": "True",
        "CheckingCode": "[0-100]"
        "Factor":"1",
        "ParameterName":"fill factor",
        "ParameterValue":"0",
        "ForceModify":"True",
        "Unit":"INT" } ] },
"RequestId": "1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC"}
```

#### 2.8.2 DescribeParameters

Description You can call this operation to query the current instance parameter configuration. Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeParameters. |
| DBInstanceId | String | Yes | The ID of the instance. |

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> | N/A | Common response parameters. |
| Engine | String | The engine of the database. |
| EngineVersion | String | The engine version of the database. |
| RunningParameters | List<DBInstanceParameter> | The array that consists of running DBInstanceParameter data. Format: {parameter1,parameter2,paramete r3, ...}. |
| ConfigParameters | List<DBInstanceParameter> | The array that consists of synchronizing DBInstanceParameter data. Format: {parameter1,parameter2,paramete r3, ...}. |

DBInstanceParameter parameters

| Parameter | Type | Description |
|---|---|---|
| ParameterName | String | The name of the parameter. |
| ParameterValue | String | The value of the parameter. |
| ParameterDescription | String | The description of the parameter. |

Examples Sample request s

```
https://rds.example.com/?Action=DescribeParameters &DBInstanceId=rds-xxxxx &<Common request parameters>
```

Sample success responses XML format

```xml
<DescribeParametersResponse> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> <Engine>mysql</Engine > <EngineVersion>5.6</EngineVersion> <RunningParameters> <DBInstanceParameter> <ParameterDescription>test</ParameterDescription> <ParameterName>fill factor</ParameterName> <ParameterValue>0</ParameterValue> </DBInstanceParameter> </RunningParameters> <ConfigParameters> <DBInstanceParameter> <ParameterDescription>test1</ParameterDescription> <ParameterName>fill factor</ParameterName> <ParameterValue>50</ParameterValue> </DBInstanceParameter> </ConfigParameters> </DescribeParametersResponse>
```

JSON format

```json
{ "ConfigParameters": {
    "DBInstanceParameter": [ {
        "ParameterDescription": "test",
        "ParameterName": "fill factor",
        "ParameterValue": "50" } ] },
    "Engine": "mysql",
    "EngineVersion": "5.6",
    "RunningParameters": {
        "DBInstanceParameter": [ {
            "ParameterDescription": "test1",
            "ParameterName": "fill factor",
            "ParameterValue": "0" } ] },
    "RequestId": "1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC"}
```

#### 2.8.3 ModifyParameter

Description You can call this operation to modify instance parameters. After you submit a request, RDS assigns a task to apply new parameters to the instance. If there are any parameter modifications that require the database to be restarted, RDS restarts the database. Before you call this operation, ensure that the following requirements are met: The instance is in the running state. The instance is not locked by the system. There are three types of parameter values: 1 to 65,535: indicates a numerical range. Regular identification is used to extract the minimum and maximum values. The input parameter is then verified based on the extracted minimum and maximum values. The parameter must be a multiple of a divisible factor. utf8 | gbk | latin1: indicates a set value determination rule. Regular identification is used to extract the fixed value. The input parameter is then verified based on these fixed values. Others: These must be implemented with regular expressions. Before assigning the task, RDS checks the parameter as follows:
1. Whether the parameter exist.
2. Whether the parameter can be modified.
3. Whether the parameter is valid.
If the parameter is invalid, RDS returns the 400 HTTP status code and information about the invalid parameter. Example:

```json
{"HttpStatusCode":400, "Code":"InvalidParameter.Format", "Message":"Specified parameter is not valid.[auto_increment_increment:a,character_set_c lient:41]"}
```

Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to ModifyParameter. |
| DBInstanceId | String | Yes | The ID of the instance for which parameters are modified. |
| Parameters | String | Yes | The JSON string for the parameter and its value. The parameter value must be of the string type. {"auto increment increment":"1", _ _ "character set client":"utf8"}. _ _ |
| Forcerestart | String | No | Specifies whether to forcibly restart the database. Valid values: true and false. If a parameter can take effect only after database restart, Forcerestart must be set to true. Otherwise, the parameter modification will not take effect. Default value: false. |

Response parameters

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> | - | Common response parameters. |

Examples Sample request s

```
https://rds.example.com/?Action=ModifyeParameter &DBInstanceId=rds-xxxxx &Parameters={"key_buffer_size":"456","character_set_client":"gbk"} &<Common request parameters>
```

Sample responses XML format

```xml
<ModifyeParameterResponse> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> </ModifyeParameterResponse>
```

JSON format

```json
{ "RequestId":"1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC",}
```

### 2.9 Log management

#### 2.9.1 DescribeSlowLogs

Description You can call this operation to query the slow log summary of the databases in a specified instance over a specified period of time. This operation supports paged query. Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeSlowLogs. |
| DBInstanc eId | String | Yes | The ID of the instance. |
| StartTime | String | Yes | The beginning of the time range to query. Specify the date in the ISO 8601 standard in the YYYY-MM-DDZ format. Example: 2011- 05-30Z. |
| EndTime | String | Yes | The end of the time range to query. The end date must be later than the start date. Specify the date in the ISO 8601 standard in the YYYY-MM-DDZ format. Example: 2011-05-30Z. |
| DBName | String | No | The name of the database. |

| Parameter | Type | Required | Description |
|---|---|---|---|
| SortKey | String | No | The basis on which query results are sorted. Valid values: TotalExecutionCounts: in descending order of execution times. TotalQueryTimes: in descending order of the total execution duration. TotalLogicalReads: in descending order of the total number of logical reads. TotalPhysicalReads: in descending order of the total number of physical reads. This parameter is applicable to SQL Server instances. It must be used when you query SQL Server Instances. |
| PageSize | Integer | No | The number of entries to return on each page. Valid values: 30, 50, and 100. Default value: 30. |
| PageNum ber | Integer | No | The number of the page to return. Pages start from page 1. Default value: 1. |

Response parameters

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> |   | Common response parameters. |
| Engine | String | The engine of the database. |
| StartTime | String | The beginning of the time range where the query was executed. The date follows the ISO 8601 standard in the YYYY-MM-DDZ format. Example: 2011-05-30Z. |
| EndTime | String | The end of the time range where the query was executed. The date follows the ISO 8601 standard in the YYYY-MM-DDZ format. Example: 2011-05-30Z. |
| TotalRecordCou nt | Integer | The total number of entries. |
| PageNumber | Integer | The page number of the returned page. |
| PageRecordCoun t | Integer | The number of SQL slow queries on the current page. |
| Items | List<SQLSlowL og> | The list of slow logs. |

Examples Sample request s

```
https://rds.example.com/?Action=DescribeSlowLogs &DBInstanceId=rds-xxxxx &StartTime=2011-06-11Z &EndTime=2011-12-11Z &SortKey= Totaxxxxx &<Common request parameters>
```

Sample success responses XML format

```xml
<DescribeSlowLogsResponse> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> <DBInstanceID>rds-xxxxx</DBInstanceID> <Engine>MySQL</Engine> <StartTime>2011-06-11Z</StartTime> <EndTime>2011-12-11Z</EndTime> <TotalRecordCount>1</TotalRecordCount> <PageNumber>1</PageNumber> <PageRecordCount>1</PageRecordCount> <Items> <SQLSlowLog> <SQLText>update test.zxb set id=0 limit 1</SQLText> <MySQLTotalExecutionCounts>178</MySQLTotalExecutionCounts> <MySQLTotalExecutionTimes>189</MySQLTotalExecutionTimes> <TotalLogicalReadcounts>89</TotalLogicalReadcounts> <TotalPhysicalReadcounts>90</TotalPhysicalReadcounts> <ReportTime>2013-11-12Z</ReportTime> </SQLSlowLog> </Items> </DescribeSlowLogsResponse>
```

JSON format

```json
{ "RequestId":"1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC", "StartTime":"2011-06-11Z ", "EndTime":"2011-12-11Z ", "Engine":"MySQL", "PageNumber":1, "PageRecordCount":1, "TotalRecordCount":1, "Items":{
    "SQLSlowLog":[{
        "SQLText":”update test.zxb set id=0 limit 1”,
        "MySQLTotalExecutionCounts":178,
        "MySQLTotalExecutionTimes":189,
        "TotalLogicalReadcounts":89,
        "TotalPhysicalReadcounts":90,
        "ReportTime":"2013-11-12Z " }]}}
```

#### 2.9.2 DescribeSlowLogRecords

p You can call this operation to query the slow log details of the databases in a specified instance over a specified period of time. This operation is only supported on MySQL instances. Request parameters

| Parameter | Type | Require d | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeSlowLogRecords. |
| DBInstanc eId | String | Yes | The ID of the instance to which the database belongs. |
| StartTime | String | Yes | The beginning of the time range where the query is performed. Specify the time in the yyyy-MM-ddTHH:mm:ssZ format. Example: 2011-06- 11T15:00Z. |
| EndTime | String | Yes | The end of the time range where the query is performed. Specify the time in the yyyy-MM-ddTHH:mm:ssZ format. Example: 2011-06- 11T16:00Z. |
| DBName | String | No | The name of the database. |
| PageSize | Integer | No | The number of entries to return on each page. Valid values: 30, 50, and 100. Default value: 30. |
| PageNum ber | Integer | No | The number of the page to return. Pages start from page 1 but must be equal to or smaller than the maximum Integer value. Default value: 1. |

Response parameters

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> |   | Common response parameters. |
| Engine | String | The type of the database. |
| TotalRecordCount | Integer | The total number of entries. |
| PageNumber | Integer | The number of the page returned. |
| PageRecordCount | Integer | The number of SQL slow queries on the current page. |
| Items | List<SQLSlowRecord> | - |

SQLSlowLog parameters

| Parameter | Type | Description |
|---|---|---|
| HostAddress | String | The host address to connect the database. |

| Developer Guide·API r | eference | ApsaraDB for RD |
|---|---|---|
| Parameter | Type | Description |
| DBName | String | The name of the database. |
| SQLText | String | The query statement. |
| QueryTimes | Long | The execution time of the slow query. Unit: seconds. |
| LockTimes | Long | The lock time of the slow query. Unit: seconds. |
| ParseRowCounts | Long | The number of entries parsed. |
| ReturnRowCounts | Long | The number of entries returned. |
| ExecutionStartTim e | String | The beginning of the time range where the query was executed. The time is in the yyyy-MM-ddTHH:mm:ssZ format. Example: 2011-06-11T15:00:08Z. |

Examples Sample request s

```
https://rds.example.com/?Action=DescribeSlowLogRecords &DBInstanceId=rds-xxxxx &StartTime=2011-06-11T15:00Z &EndTime=2011-06-11T16:00Z &<Common request parameters>
```

Sample responses XML format

```xml
<DescribeSlowLogRecordsResponse> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> <DBInstanceID>rds-xxxxx</DBInstanceID> <Engine>MySQL</Engine> <TotalRecordCount>1</TotalRecordCount> <PageNumber>1</PageNumber> <PageRecordCount>1</PageRecordCount> <Items> <SQLSlowRecord> <HostAddress>192.168.0.123</HostAddress> <DBName>test</DBName> <SQLText>update test.zxb set id=0 limit 1</SQLText> <QueryTimes>123</QueryTimes> <LockTimes>12</LockTimes> <ParseRowCounts>125</ParseRowCounts> <ReturnRowCounts>1</ReturnRowCounts> <ExecutionStartTime>2011-06-11T15:00:08Z</ExecutionStartTime> </SQLSlowRecord> </Items> </DescribeSlowLogRecordsResponse>
```

JSON format

```json
{ "RequestId":"1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC", "Engine":"MySQL", "PageNumber":1, "PageRecordCount":1, "TotalRecordCount":1, "Items":{
    "SQLSlowRecord":[{
        HostAddress:”192.168.0.123”,
        DBName:”test”,
        SQLText:”update test.zxb set id=0 limit 1”,
        QueryTimes:”123”,
        LockTimes:”12”,
        ParseRowCounts:”125”,
        ReturnRowCounts:”1”,
        ExecutionStartTime:”2011-06-11T15:00:08Z”}]}}
```

#### 2.9.3 DescribeErrorLogs

Description You can call this operation to query the error logs generated for an instance over a specified period of time. Request parameters

| Parameter | Typ e | Requir ed | Description |
|---|---|---|---|
| Action | Stri ng | Yes | The operation that you want to perform. Set the value to DescribeErrorLogs. |
| DBInstanceI d | Stri ng | Yes | The ID of the instance for which error logs are queried. |
| StartTime | Stri ng | Yes | The beginning of the time range where the query is performed. Specify the time in the yyyy-MM-ddTHH:mm:ssZ format. Example: 2011-05- 30T12:10Z. |
| EndTime | Stri ng | Yes | The end of the time range where the query is performed. Specify the time in the yyyy-MM-ddTHH:mm:ssZ format. Example: 2011-05-30T20:10Z. |
| PageSize | Inte ger | No | The number of entries to return on each page. Valid values: 30, 50, and 100. Default value: 30. |
| PageNumb er | Inte ger | No | The number of the page to return. Pages start from page 1 but must be equal to or smaller than the maximum Integer value. Default value: 1. |

Response parameters

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> |   | Common response parameters. |
| TotalRecordCount | Integer | The total number of entries. |
| PageNumber | Integer | The number of the page returned. |
| PageRecordCount | Integer | The number of error logs on the current page. |
| Items | List<ErrorLogs> | - |

ErrorLogs parameters

| Parameter | Type | Description |
|---|---|---|
| ErrorInfo | String | The error log information. |
| CreateTime | String | The time when the error log was generated. The time is in the yyyy-MM- ddTHH:mm:ssZ format. Example: 2011-05-30T12:11:4Z. |

Examples Sample request s

```
https://rds.example.com/?Action=DescribeErrorLogs. &DBInstanceId=rds-xxxxx &StartTime=2011-06-11T15:00Z &EndTime=2011-06-11T20:00Z &<Common request parameters>
```

Sample responses XML format

```xml
<DescribeErrorLogsResponse> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> <TotalRecordCount>1</TotalRecordCount> <PageNumber>1</PageNumber> <PageRecordCount>1<PageRecordCount> <Items> <ErrorLog> <ErrorInfo>spid52 DBCC TRACEON 3499, server process ID (SPID) 52. This is an informationa l message only; no user action is required</ErrorInfo> <CreateTime>2013-06-04T15:00:00</CreateTime> </ErrorLog> </Items> </DescribeErrorLogsResponse>
```

JSON format

```json
{"RequestId":"1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC", "PageNumber":1, "TotalRecordCount":1, "PageRecordCount":1, "Items":{
    "ErrorLog":[{
        ErrorInfo:”spid52 DBCC TRACEON 3499, server process ID (SPID) 52. This is an info
rmational message only; no user action is required”,
        CreateTime:”2013-06-04T15:00:00”}]}}
```

#### 2.9.4 DescribeBinlogFiles

Description You can call this operation to query binlogs of a MySQL instance. This operation supports querying by page. RDS provides binlog files for you to download. When the DownloadLink is NULL, RDS does not provide a download URL. When DownloadLink is not NULL, you can use this URL to download the backup file through Wget (with double quotation marks), a browser, or a user program. The expiration time for this URL is specified by LinkExpiredTime. Use it before the expiration time. If the BackupSet has expired, the following error code is displayed:

```xml
<Error> <Code>AccessDenied</Code> <Message>Request has expired. </Message> <Expires>2012-12-25T09:47:52.000Z</Expires> <ServerTime>2012-12-25T09:49:00.000Z</ServerTime> <RequestId>50D9768CA801C2F102005C70</RequestId> <HostId>oss-test.aliyun-inc.com</HostId> </Error>
```

Request parameters

| Parameter | Type | Require d | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeBinlogFiles. |
| DBInstanceId | String | Yes | The ID of the instance for which binlogs are queried. |
| StartTime | String | Yes | The beginning of the time range where the query is performed. Specify the time in the yyyy-MM-ddTHH:mm:ssZ format. |
| EndTime | String | Yes | The end of the time range where the query is performed. Specify the time in the yyyy-MM-ddTHH:mm:ssZ format. The end time must be later than the start time. |
| PageSize | Integer | No | The number of entries to return on each page. Valid values: 30, 50, and 100. Default value: 30. |

| eveloper Guide· | API referen | ce | ApsaraDB for RD |
|---|---|---|---|

| Parameter | Type | Require d | Description |
|---|---|---|---|
| PageNumber | Integer | No | The number of the page to return. Pages start from page 1 but must be equal to or smaller than the maximum Integer value. Default value: 1. |

Response parameters

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> | - | Common response parameters. |
| TotalRecordCount | Integer | The total number of binlog files. |
| PageNumber | Integer | The number of the page returned. |
| PageRecordCount | Integer | The number of binlog files on the current page. |
| Items | List<BinLogFile> | - |

BinLogFile parameters

| Parameter | Type | Description |
|---|---|---|
| FileSize | Long | The size of a binlog file. Unit: Byte. |
| LogBeginTime | String | The beginning of the time range where the binlog was executed. |
| LogEndTime | String | The end of the time range where the binlog was executed. |
| DownloadLink | String | The HTTP-compliant download URL. If this parameter is set to NULL, no download URL exists. |
| HostInstanceID | String | The ID of the instance to which the binlog belongs. This parameter indicates whether the binlog is from the primary or secondary instance. |
| LinkExpiredTime | String | The URL expiration time. The time is in the yyyy-MM- ddTHH:mm:ssZ format. Example: 2011-06-11T15:00:00Z. |

Examples Sample request s

```
https://rds.example.com/?Action=DescribeBinlogFiles &DBInstanceId=rds-xxxxx &StartTime=2011-06-11T15:00:00Z &EndTime=2013-06-05T15:00:00Z &<Common request parameters>
```

Sample responses XML format

```xml
<DescribeBinlogFilesResponse> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> <TotalRecordCount>1</TotalRecordCount> <PageNumber>1</PageNumber> <PageRecordCount>1<PageRecordCount> <Items> <BinLogFile> <FileSize>123</FileSize> <LogBeginTime>2013-06-01T15:00:00Z</LogBeginTime> <LogEndTime>2013-06-02T18:00:00Z</LogEndTime> <DownloadLink>http://rdslog-real.oss.aliyuncs.com/custins47742/hostins46770/mysql-bin. 00 0120.zip?spm=0.0.0.0.eMQKjs&OSSAccessKeyId=c9gzsqpauxxxxx&Expires=1384916927&Signature=07 TMgM3xxxxx</DownloadLink> <LinkExpiredTime>2013-06-09T18:00:00Z</LinkExpiredTime> </BinLogFile> </Items> </DescribeBinlogFilesResponse>
```

JSON format

```json
{ "RequestId":"66816822-CEC1-4C8D-AB26-2530A7D4DCA5", "PageNumber":1, "TotalRecordCount":1, "PageRecordCount":1, "Items":{
    "BinLogFile":[{
        FileSize:”123”,
        LogBeginTime:”2013-06-01T15:00:00Z”,
        LogEndTime:”2013-06-02T18:00:00Z”,
        DownloadLink:”http://rdslog-real.oss.aliyuncs.com/custinsxxxxx/hostinsxxxxx/mysql
-bin. 000120.zip?spm=0.0.0.0.eMQKjs&OSSAccessKeyId=c9gzsqpauxxxxx&Expires=1384916927&Sign ature=07TMgM3xxxxx”,
        LinkExpiredTime”2013-06-09T18:00:00Z”}]}}
```

#### 2.9.5 DescribeSQLCollectorPolicy

Description You can call this operation to check whether SQL collection is enabled for a specified RDS instance. Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeSQLCollectorPolicy. |
| DBInstanceId | String | Yes | The ID of the instance for which SQL collection is enabled or disabled. |

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> |   | Common response parameters. |
| SQLCollectorStatu s | String | Indicates whether SQL collection is enabled. Valid values: Enable and Disabled. |

#### 2.9.6 ModifySQLCollectorPolicy

Description You can call this operation to enable or disable SQL collection for the specified RDS instance. Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to ModifySQLCollectorPolicy. |
| DBInstanceId | String | Yes | The ID of the instance for which SQL collection is enabled or disabled. |
| SQLCollectorS tatus | String | Yes | Specifies whether to enable SQL collection. Valid values: Enable and Disabled. |

Response parameters This operation returns only common response parameters.

#### 2.9.7 DescribeSQLLogRecords

Description You can call this operation to query the SQL audit logs generated for an instance. Request parameters

| Parameter | Typ e | Requir ed | Description |
|---|---|---|---|
| Action | Strin g | Yes | The operation that you want to perform. Set the value to DescribeSQLLogRecords. |
| DBInstanceI d | Strin g | Yes | The ID of the instance for which SQL audit logs are queried. |

| A | psaraDB for RD | S |   | Developer Guide·API referenc | e |
|---|---|---|---|---|---|

| Parameter | Typ e | Requir ed | Description |
|---|---|---|---|
| Database | Strin g | No | The name of the database. All databases are selected by default. |
| User | Strin g | No | The name of the user. All users are selected by default. |
| Form | Strin g | No | The file generation form for audit logs. Valid values: File and Stream. If this parameter is set to File, only common parameters are returned, and you must call the DescribeSQLLogFiles operation to obtain the final download file address. If this parameter is set to Stream, data streams are returned. Default value: Stream. |
| QueryKeyw ords | Strin g | No | The keywords used for query. Up to 10 keywords can be entered at a time. Separate multiple keywords with spaces. |
| StartTime | Strin g | Yes | The beginning of the time range where the query is performed. Specify the time in the yyyy-MM-ddTHH:mm:ssZ format. |
| EndTime | Strin g | Yes | The end of the time range where the query is performed. Specify the time in the yyyy-MM-ddTHH:mm:ssZ format. The end time must be later than the start time. |
| PageSize | Inte ger | No | The number of entries to return on each page. Valid values: 30, 50, 100, and 200. Default value: 100. |
| PageNumb er | Inte ger | No | The number of the page to return. Pages start from page 1 but must be equal to or smaller than the maximum Integer value. Default value: 1. |

Response parameters

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> | - | Common response parameters. |
| TotalRecordCount | Integer | The total number of entries. |
| PageNumber | Integer | The number of the page returned. |
| PageRecordCount | Integer | The number of SQL logs on the current page. |
| Items | List<SQLRecord> | The array that consists of SQLRecord data. |

SQLRecord parameters

| Parameter | Type | Description |
|---|---|---|
| DBName | String | The name of the database. |
| AccountName | String | The name of the account. |

|   | Developer Guide·API refer | ence | ApsaraDB for RD | S |
|---|---|---|---|---|

| Parameter | Type | Description |
|---|---|---|
| HostAddress | String | The IP address of the client. |
| SQLText | String | The SQL statement. |
| TotalExecutionTimes | Long | The amount of time taken to execute the operation. Unit: microseconds. |
| ReturnRowCounts | Long | The number of entries returned. |
| ThreadID | String | The thread ID. |
| ExecuteTime | String | The execution time. The time is in the yyyy-MM-ddTHH:mm:ssZ format. Example: 2011-05-30T12:11:20Z. |

Examples Sample request s

```
https://rds.example.com/?Action=DescribeSQLLogRecords &DBInstanceId=rds-xxxxx &StartTime=2011-06-11T15:00:00Z &EndTime=2013-06-05T15:00:00Z &<Common request parameters>
```

Sample responses XML format

```xml
<DescribeSQLLogRecordsResponse> <PageNumber>1</PageNumber>
    <RequestId>08A3B71B-FE08-4B03-974F-CC7EA6DB1828</RequestId>
    <TotalRecordCounts>1</TotalRecordCounts>
    <SQLItems>
        <SQLItem>
            <ReturnRowCounts>34</ReturnRowCounts>
            <TotalExecutionTimes>12</TotalExecutionTimes>
            <HostAddress>192.168.xx.xx</HostAddress>
            <ExecuteTime>2011-06-11T15:00:23Z</ExecuteTime>
            <SQLText>update test.zxb set id=0 limit 1</SQLText>
            <AccountName>accounttest</AccountName>
            <DBName>test</DBName>
        </SQLItem>
    </SQLItems>
    <ItemsCounts>1</ItemsCounts>
</DescribeSQLLogRecordsResponse>
```

JSON format

```json
{"PageNumber":1,
    "RequestId":"08A3B71B-FE08-4B03-974F-CC7EA6DB1828",
    "TotalRecordCounts":1,
    "SQLItems":{
        "SQLItem":[
```

`{`

```json
                "ReturnRowCounts":34,
                "TotalExecutionTimes":12,
                "HostAddress":"192.168.xx.xx",
                "ExecuteTime":"2011-06-11T15:00:23Z",
                "SQLText":"update test.zxb set id=0 limit 1",
                "AccountName":"accounttest",
                "DBName":"test"
```

`}` `]` `},`

```json
    "ItemsCounts":1
```

`}`

#### 2.9.8 DescribeSQLLogFiles

Description You can call this operation to query SQL audit files. Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeSQLLogFiles. |
| DBInstanceId | String | Yes | The ID of the instance for which SQL audit files are queried. |

Response parameters

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> |   | Common response parameters. |
| TotalRecordCount | Integer | The total number of entries. |
| PageNumber | Integer | The number of the page returned. |
| PageRecordCount | Integer | The number of entries on the current page. |
| Items | List<LogFile> | The array that consists of audit file data. |

LogFile parameters

| Parameter | Type | Description |
|---|---|---|
| FileID | Integer | The ID of an audit log file. |
| DBInstanceId | String | The ID of the instance for which SQL audit files were queried. |
| LogStatus | String | The status of SQL audit files. Valid values: Success Failed Generating |
| LogStartTime | String | The beginning of the time range where the audit log was executed. |
| LogEndTime | String | The end of the time range where the audit log was executed. |
| LogDownloadUR L | String | The file download URL. If the download URL is unavailable, this parameter will be empty. |
| LogSize | Long | The size of an audit log file. Unit: Byte. |

### 2.10 Data migration

#### 2.10.1 CreateUploadPathForSQLServer

Description You can call this operation to create the account and password of the file server and the file path. Based on this information, you can upload data files. After the upload is complete, you can migrate external data. Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to CreateUploadPathForSQLServer. |
| DBInstanceId | String | Yes | The ID of the instance. |
| DBName | String | Yes | The name of the database. |

Response parameters

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> | - | Common response parameters. |
| InternetFtpServer | String | The IP address of the file server on the public network. |

| A | psaraDB for RDS |   | Developer Guide·API referenc | e |
|---|---|---|---|---|

| Parameter | Type | Description |
|---|---|---|
| InternetPort | Integer | The port of the file server on the public network. |
| IntranetFtpServer | String | The IP address of the file server on the internal network. |
| IntranetPort | Integer | The port of the file server on the internal network. |
| UserName | String | The username used to log on to the file server. |
| Password | String | The password used to log on to the file server. |
| FileName | String | The name of the data file with the extension. |

Examples Sample request s

```
https://rds.example.com/?Action= CreateUploadPathForSQLServer &DBInstanceId=rds-xxxxx &DBName=testdb01 &<Common request parameters>
```

Sample success responses XML format

```xml
<CreateUploadPathForSQLServerResponse> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> <InternetFtpServer>10.230.239.1</InternetFtpServer> <InternetPort>3021</InternetPort> <IntranetFtpServer></IntranetFtpServer> <UserName>userxxx</UserName> <Password>pwxxxxx</Password> <FileName>testdb01_xxxxx.bak</FileName> </CreateUploadPathForSQLServerResponse>
```

JSON format

```json
{"RequestId":"1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC",
 "InternetFtpServer ":"10.230.239.1",
 "InternetPort":3021,
 "IntranetFtpServer":"",
 "UserName":"userxxx",
 "Password":"pwxxxxx",
 "FileName":"testdb01_xxxxx.bak"}
```

#### 2.10.2 DescribeFilesForSQLServer

Description You can call this operation to query files on the file server. SQLServer users can obtain their accounts to upload data files to the file server by calling the CreateUploadPathForSQLServer operation. After the data files are uploaded, RDS updates their status. You can also call this operation to check whether the data files are available. If they are available, you can import data and obtain the information about the import process. Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeFilesForSQLServer. |
| DBInstanceId | String | Yes | The ID of the instance for which files are queried. |
| StartTime | String | Yes | The beginning of the time range where the query is performed. Specify the time in the yyyy-MM- ddTHH:mm:ssZ format. Example: 2011-06-11T15:00Z. |
| EndTime | String | Yes | The end of the time range where the query is performed. Specify the time in the yyyy-MM-ddTHH:mm:ssZ format. Example: 2011-06-11T16:00Z. The end time must be later than the start time. |
| PageSize | Integer | No | The number of entries to return on each page. Valid values: 30, 50, and 100. Default value: 30. |
| PageNumber | Integer | No | The number of the page to return. Pages start from page 1 but must be equal to or smaller than the maximum Integer value. Default value: 1. |

Response parameters

| Parameter | Type | Description |
|---|---|---|
| DBInstanceId | String | The ID of the instance for which files were queried. |
| TotalRecordCount | Integer | The total number of entries. |
| PageNumber | Integer | The number of the page returned. |
| PageRecordCount | Integer | The number of SQL slow queries on the current page. |
| Items | List<SQLServerUploadFile> | - |

SQLServerUploadFile parameters

| Parameter | Type | Description |
|---|---|---|
| DBName | String | The name of the database. |

| A | psaraDB for RDS |   | Developer Guide·API referenc | e |
|---|---|---|---|---|

| Parameter | Type | Description |
|---|---|---|
| FileName | String | The name of the data file, with the extension. |
| FileSize | Long | The size of the data file. Unit: bytes. |
| InternetFtpS erver | String | The file server. |
| InternetPort | Integer | The port of the file server on the public network. |
| IntranetFtpse rver | String | The IP address of the file server on the internal network. |
| Intranetport | Integer | The port of the file server on the internal network. |
| UserName | String | The username used to log on to the file server. |
| Password | String | The password used to log on to the file server. |
| FileStatus | String | The file status. Valid values: Unavailable, Available, NotStarted, Uploading, UploadFailed, Virus, Deleted, and Success. |
| CreationTime | String | The time when the FTP file was created. The time is in the yyyy-MM- ddThh:mmZ format. Example: 2011-05-30 T12:11:4Z. |

Examples Sample request s

```
https://rds.example.com/?Action=DescribeFilesForSQLServer &DBInstanceId=rds-xxxxx &StartTime=2014-06-11T15:00Z &EndTime=2014-06-11T16:00Z &<Common request parameter>
```

Sample responses XML format

```xml
<DescribeFilesForSQLServerResponse> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> <TotalRecordCount>1</TotalRecordCount> <PageNumber>1</PageNumber> <PageRecordCount>1</PageRecordCount> <Items> <SQLServerUploadFile> <DBName>testdb01</DBName> <FileName>testdb01_xxxxx.bak</FileName> <FileSize>1243435</FileSize> <InternetFtpServer>10.xxx. 239.1</InternetFtpServer> <InternetPort>3021</InternetPort> <IntranetFtpServer></IntranetFtpServer> <UserName>userxxx</UserName> <Password>pwxxxxx</Password> <FileStatus>Success</FileStatus> <CreationTime>2014-06-11T15:02:40Z</CreationTime> </SQLServerUploadFile> </Items> </DescribeFilesForSQLServerResponse>
```

JSON format

```json
{"PageNumber":1, "TotalRecordCount":1, "PageRecordCount":1, "Items":{
 "SQLServerUploadFile":[{
  "DBName":"testdb01",
  "FileName":"testdb01_xxxxx.bak",
  "FileSize ":"1243435",
  "InternetFtpServer":"10.xxx. 239.1",
  "InternetPort":3021,
  "IntranetFtpServer":"",
  "UserName":"userxxx",
  "Password":"pwxxxxx",
  "FileStatus":"Success",
  "CreationTime":"2014-06-11T15:02:40Z"} ]},
"RequestId": "1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC"}
```

#### 2.10.3 ImportDatabaseBetweenInstances

Description You can call this operation to migrate data from one ApsaraDB for RDS instance to another. This operation is only supported on dedicated ApsaraDB RDS for MySQL instances. ApsaraDB RDS for MySQL instances support batch database migration. During migration, the source instance status changes to Migrating and the destination instance status changes to Importing Data. Database migration is performed between different instances that belong to the same user. Before you call this operation, make sure that the following requirements are met: The instance is in the running state. The database is in the running state. The destination instance is not locked by the system. The reserved storage space of the destination instance is greater than the space calculated by the formula: Space occupied by the destination instance - Database space of the destination instance + Database space of the source instance. Databases to be migrated exist in both the source and destination instances and are activated. ApsaraDB RDS for SQL Server instances support batch database migration. During migration, the source instance status changes to Migrating and the destination instance status changes to Importing Data. Database migration is performed between different instances that belong to the same user. Before you call this operation, make sure that the following requirements are met: The instance is in the running state. The database is in the running state. The destination instance is not locked by the system. The reserved storage space of the destination instance is greater than the space calculated by the formula: Space occupied by the destination instance - Database space of the destination instance + Database space of the source instance. Request parameters

| Parameter | Type | Require d | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to ImportDatabaseBetweenInstances. |
| DBInstanceId | String | Yes | The ID of the instance. |
| SourceDBInstanc eId | String | Yes | The ID of the source instance. It cannot be the same as that of the destination instance. |
| DBInfo | String | Yes | The information of the database to be migrated. Specify this parameter in the JSON format. For ApsaraDB RDS for MySQL instances, the parameter value is an array. Example: {"DBNames":["mydb","mydb2"]}. The names of the source and destination databases must be the same. In this example, data is migrated from the mydb and mydb2 databases. These databases must exist in both the source and destination instances. |

DBInfo parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| DBNames | List | Yes | The names of databases to be migrated. Example: ["mydb","mydb2"]. |

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> |   | For more information, see Common response parameters. |
| ImportId | Integer | The ID of the destination instance. |

Examples Sample request s

```
https://rds.example.com/?Action=ImportDatabaseBetweenInstances &DBInstanceId=rds-xxxxx &SourceDBInstanceId=rds-xxxxx &{"DBNames":["mydb","mydb2"]} &<Common request parameters>
```

Sample success responses XML format

```xml
<ImportDatabaseBetweenInstancesResponse>
 <ImportId>2122321</ImportId>
 <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId>
 </ImportDatabaseBetweenInstancesResponse>
```

JSON format

```json
{"ImportId":2122321",
 RequestId":"1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC"}
```

#### 2.10.4 CancelImport

Description You can call this operation to cancel migration tasks from ApsaraDB RDS for MySQL instances. Migration tasks from MySQL instances can be canceled. Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to CancelImport. |
| DBInstanceId | String | Yes | The ID of the instance. |
| ImportId | Integer | Yes | The migration task ID. |

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> | - | Common response parameters. |

Examples Sample request s

```
https://rds.example.com/?Action=CancelImport &DBInstanceId=rds-xxxxx &ImportId=127562 &<Common request parameters>
```

Sample success responses XML format

```xml
<CancelImportResponse> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> </CancelImportResponse>
```

JSON format

```json
{"RequestId": "1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC" }
```

### 2.11 Tag management

#### 2.11.1 AddTagsToResource

Description You can call this operation to bind existing or newly created tags to instances. Before you call this operation, ensure that the following requirements are met: Each tag is composed of a TagKey and a TagValue. The TagKey cannot be blank, but the TagValue can. The values of TagKey and TagValue cannot start with aliyun. The values of TagKey and TagValue are not case sensitive. The maximum length of TagKey is 64 characters and the maximum length of TagValue is 128 characters. Each instance can only be bound to a maximum of 10 tags. Each tag bound to the same instance must have a unique TagKey. If tags with duplicate TagKeys are bound to the same instance, the tag bound last overwrites the existing tag. Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to AddTagsToResource. |
| RegionId | String | Yes | The region ID of the instance for which a tag is be bound. |
| DBInstanceId | String | Yes | The ID of the instance for which a tag is be bound. Up to 30 IDs can be entered in a single request. Separate multiple IDs with commas (,) Format: instance1,instance2,instance3. |
| Tags | JSON string | Yes | The tag pair to be bound. This parameter must include a TagKey, but does not need to include a corresponding TagValue. Up to five tag pairs can be entered in a single request. The TagKey is required, and TagValue is optional. Format: {“key1”:”value1”,“key2”:””}. |

Response parameters

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> | - | Common response parameters. |

#### 2.11.2 DescribeTags

Description You can call this operation to view the bound tag information of an RDS instance belonging to the current account. This operation must meet the following requirements: If a specified instance ID is provided, all tags bound to this instance are queried and the other filter criteria are ignored. If the TagKey of a key is provided without a TagValue, the results of all tags matching the TagKey criteria are returned. If both TagKey and TagValue are provided, only the results that match both parameters are returned. Request parameters

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeTags. |
| RegionId | String | Yes | The region ID of the instance. |

| psaraDB for RD | S |   | Developer Guide·API referenc |
|---|---|---|---|

| Name | Type | Required | Description |
|---|---|---|---|
| DBInstanceI d | String | No | The name of the instance. If this parameter is provided, all the other filter criteria are ignored. |
| Tags | Json string | No | The tag pair. This parameter must include a TagKey, but does not need to include a corresponding TagValue. The TagKey cannot be blank, but the TagValue can. Format: {"key1":"value1 "}. |

Response parameters

| Name | Type | Description |
|---|---|---|
| <Common response parameters> | - | Common response parameters. |
| Items | List<TagInfos> | The array that consists of tag data. |

TagInfos parameters

| Name | Type | Description |
|---|---|---|
| TagKey | String | The TagKey. |
| TagValue | String | The TagValue. |
| DBInstanceIds | List<DBInstanceId> | The IDs of instances bound to this tag. |

DBInstanceIds parameters

| Name | Type | Description |
|---|---|---|
| DBInstanceId | String | The name of the instance. |

#### 2.11.3 RemoveTagsFromResource

Description You can call this operation to unbind tags from an instance. This operation must meet the following requirements: A maximum of 10 tags can be unbound in a single request. If a tag is unbound from all of its bound instances, the tag itself is automatically deleted. If the TagKey of a key is provided without a TagValue, all tags matching the TagKey criteria are unbound.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to RemoveTagsFromResource. |
| RegionId | String | Yes | The region ID of the instance. |
| DBInstanceId | String | Yes | The name of the instance. |
| Tags | Json string | Yes | The tag pair to be unbound. This parameter must include a TagKey, but does not need to include a corresponding TagValue. The TagKey cannot be blank, but the TagValue can. Format: {"key1":"value1 "}. |

Response parameters

| Name | Type | Description |
|---|---|---|
| <Common response parameters> | - | Common response parameters. |

### 2.12 RAM authorization

Use RAM for RDS resource authorization All RDS instances created through an Apsara Stack tenant account are resources owned by that account. By default, you have full operation permissions on the resources under your account. Resource Access Management (RAM) allows you to grant RAM users the access and management permissions on RDS resources owned by an Apsara Stack tenant account. If you do not need to use RAM, ignore this topic. Resource types in RAM The only type of RDS resources that can be authorized through RAM is dbinstance. The following table lists the resource description method when the resources are authorized through RAM.

| Resource | Resource description in authorization policy |
|---|---|
| Instance | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid acs:rds:$regionid:$accountid:dbinstance/ acs:rds:::dbinstance/ |

The $regionid field must be the ID of a region or an asterisk (*). The $instanceid field must be the ID of an instance or an asterisk (*). Similarly, $account-id is the numerical ID of your Apsara Stack tenant account, which can be replaced by an asterisk (*). Authorization operations in RAM In RAM, the following operations can be authorized to an RDS resource.

| Operation 1 | Operation 2 |
|---|---|
| CreateDBInstance | ModifyDBInstanceSpec |
| DeleteDBInstance | CreateReadonlyDBInstance |
| DescribeDBInstances | DescribeDBInstanceAttribute |
| SwitchDBInstanceNetType | RestartDBInstance |
| ModifyDBInstanceDescription | ModifySecurityIps |
| ModifyDBInstanceMaintainTime | UpgradeDBInstanceEngineVersion |
| PurgeDBInstanceLog | CreateDatabase |
| DeleteDatabase | DescribeDatabases |
| ModifyDBDescription | ModifyeParameter |
| DescribeParameters | DescribeOptimizeAdviceByDBA |
| DescribeOptimizeAdviceOnMissIndex | ImportDataBaseBetweenInstances |
| CancelImport | CreateAccount |
| ResetAccountPassword | GrantAccountPrivilege |
| RevokeAccountPrivilege | DescribeAccounts |
| DeleteAccount | ModifyAccountDescription |
| CreateBackup | DescribeBackups |
| CreateTempDBInstance | DescribeBackupPolicy |
| ModifyBackupPolicy | DescribeResourceUsage |
| DescribeDBInstancePerformance | DescribeSlowLogs |
| DescribeSlowLogRecords | DescribeErrorLogs |
| DescribeBinlogFiles | DescribeSQLLogReports |
| DescribeSQLLogRecords | DescribeOptimizeAdviceOnStorage |
| DescribeOptimizeAdviceOnMissPK | DescribeOptimizeAdviceOnExcessIndex |

Not e All operations except DescribeRegions and DescribeParameterTemplates can be authorized. RAM authentication rules of API operations When you call API operations to access resources as a RAM user, the RDS backend checks whether the RAM user is granted the required permissions by querying RAM. The permissions to be checked are determined by the resources used by the API operation. The following table lists the authentication rules for each API operation.

| Operation | Authentication rule |
|---|---|
| CreateDBInstance | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| DeleteDBInstance | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| DescribeDBInstances | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| SwitchDBInstanceNetType | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| ModifyDBInstanceDescription | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| ModifyDBInstanceMaintainTime | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| PurgeDBInstanceLog | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| DeleteDatabase | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| ModifyDBDescription | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| CancelImport | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| ResetAccountPassword | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| RevokeAccountPrivilege | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| DeleteAccount | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| CreateBackup | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| CreateTempDBInstance | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| ModifyBackupPolicy | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| DescribeDBInstancePerformance | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| DescribeSlowLogRecords | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| DescribeBinlogFiles | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| DescribeSQLLogRecords | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| DescribeOptimizeAdviceOnMissPK | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |

| psaraDB for RDS | Developer Guide·API referenc |
|---|---|

| Operation | Authentication rule |
|---|---|
| DescribeOptimizeAdviceOnMissIndex | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| DescribeParameters | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| CreatePrepaidDBInstanceForChannel | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| ModifyPrepaidDBInstanceSpec | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| CreatePostpaidDBInstanceForChannel | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| ModifyPostpaidDBInstanceSpec | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| DescribeDBInstanceAttribute | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| RestartDBInstance | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| ModifySecurityIps | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| UpgradeDBInstanceEngineVersion | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| CreateDatabase | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| DescribeDatabases | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| ImportDataBaseBetweenInstances | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| CreateAccount | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| GrantAccountPrivilege | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| DescribeAccounts | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| ModifyAccountDescription | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| DescribeBackups | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| DescribeBackupPolicy | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| DescribeResourceUsage | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| DescribeSlowLogs | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| DescribeErrorLogs | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| DescribeSQLLogReports | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| DescribeOptimizeAdviceOnStorage | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| DescribeOptimizeAdviceOnExcessIndex | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| DescribeOptimizeAdviceByDBA | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |

| eveloper Guide·API reference | ApsaraDB for RD |
|---|---|

| Operation | Authentication rule |
|---|---|
| ModifyeParameter | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |

### 2.13 Appendix

#### 2.13.1 Error codes on the client

##### 2.13.1.1 Common errors

| Error code | Error message | HTTP status code |
|---|---|---|
| MissingParameter | The input parameter "parameter name" that is mandatory for processing this request is not supplied. | 400 |
| InvalidParameter | The specified parameter "Action or Version" is not valid. | 400 |
| InvalidAccessKeyId.NotFou nd | The Access Key ID provided does not exist in our records. | 404 |
| IncompleteSignature | The request signature does not conform to Aliyun standards. | 400 |
| IllegalTimestamp | The input parameter "Timestamp" that is mandatory for processing this request is not supplied. | 400 |
| InvalidOwnerId | The specified OwnerId is not valid. | 400 |
| InvalidOwnerAccount | The specified OwnerAccount is not valid. | 400 |
| InvalidOwner | OwnerId and OwnerAccount can't be used at one API access. | 400 |
| Throttling | Request was denied due to request throttling. | 400 |
| InvalidAction | The specified action is not valid. | 403 |
| ActionUnauthorized | The specified action is not available for you | 403 |
| UnsupportedHTTPMethod | This http method not supported. | 403 |
| UnsupportedParameter | The parameter "<parameter name>" is not supported. | 400 |
| Forbidden.InstanceNotFou nd | The specified Instance is not found. | 404 |
| Forbidden.RAM | User not authorized to operate on the specified resource, or this API doesn't support RAM. | 403 |
| Forbedden.NotSupportRA M | This action does not support accessed by RAM mode. | 403 |

| psaraDB for RDS | Developer Guide | ·API referenc |
|---|---|---|

| Error code | Error message | HTTP status code |
|---|---|---|
| Forbidden.RiskControl | This operation is forbidden by Aliyun Risk Control system. | 403 |
| InsufficientBalance | Your account does not have enough balance. | 400 |
| Forbidden.Authentication | This operation is forbidden by Aliyun Realname Authentication system. | 403 |
| Invalid<parameter name>.ValueNotSupporte d | The specified parameter “parameter name” is not valid. | 400 |
| Invalid<parameter name>.Malformed | The specified parameter "parameter name n" is not valid. | 400 |
| InvalidParameter | The specified parameter " parameter name n " is not valid. | 400 |

##### 2.13.1.2 Specific errors

| Error code | Error message | HTTP status code |
|---|---|---|
| InvalidRegionId.NotFound | The DBInstanceId provided does not exist in our records. | 404 |
| InvalidSecurityIPList.Duplicate | The Security IP address is not in the available range or occupied. | 400 |
| InvalidSecurityIPListLength.Malformed | The quota of security ip exceeds. | 400 |
| InvalidEngineVersionInRegion.NotAvail able | The EngineVersion in the Region is not available. | 403 |
| InvaildEngineInRegion.NotAvailable | The Engine in the Region is not available. | 403 |
| InvaildDBInstanceClassInRegion.NotAv ailable | The DBInstanceClass in the Region is not available. | 403 |
| OperationDenied | The resource is out of usage. | 403 |
| RegionUnauthorized | There is no authority to create instance in the specified region. | 403 |
| QuotaExceeded.CreateInstance | The quota of create instance exceeds. | 403 |
| InvalidDBInstanceId.NotFound | The DBInstanceId provided does not exist in our records. | 404 |

| Error code | Error message | HTTP status code |
|---|---|---|
| MissingParameter | The input parameters "DBInstanceClass" and "DBInstanceStorage" all blank or no change. | 400 |
| OperationDenied.DBInstanceType | The operation is not permitted due to type of instance. | 400 |
| OperationDenied.DBInstanceStorageR educe | The operation is not permitted due to reduce storage. | 403 |
| OperationDenied.DBInstanceStatus | The operation is not permitted due to instance status. | 403 |
| DependencyViolation | The operation is not permitted due to instance mount read only or guard instance. | 403 |
| InvalidConnectionStringPrefix.Duplicat e | The connection string is not in the available range or occupied. | 400 |
| QuotaExceeded.SwitchTime | The quota of switch time exceed. | 400 |
| OperationDenied.LockMode | The operation is not permitted due to lock of instance. | 403 |
| InvalidSecurityIps.Duplicate | The quota of security ip exceeds. | 400 |
| OperationDenied.CurrentEngineVersion | The operation is not permitted due to specified current version. | 400 |
| OperationDenied.ReadOnlyDBInstance Lower | The operation is not permitted due to higher read only instance version. | 403 |
| OperationDenied.GuardDBInstanceLow er | The operation is not permitted due to higher guard instance version. | 403 |
| OperationDenied.MasterDBInstanceSta te | The operation is not permitted due to status of master instance. | 403 |
| QuotaExceeded.DBName | The quota of db exceeds. | 400 |
| InvalidDBName.Duplicate | The Security db Name is not in the available range or occupied. | 400 |
| InvalidParameter.Keyword | The specified parameter "DBName" is keyword | 400 |
| OperationDenied.DBStatus | The operation is not permitted due to status of database. | 403 |
| OperationDenied.DBInstanceEngine | The operation is not permitted due to engine of instance. | 403 |

| psaraDB for RDS | Developer Guid | e·API referenc |
|---|---|---|

| Error code | Error message | HTTP status code |
|---|---|---|
| FTPServiceUnavailable | The request has failed due to a temporary failure of the FTP server. | 403 |
| QuotaExceeded.Upload | The quota of file exceeds. | 403 |
| InvalidFileName.NotCompleted | The specified "FileName" is not completed. | 404 |
| InvalidFileName.NotAvailable | The specified "FileName" is not Available. | 404 |
| QuotaExceeded.FileSize | The quota of file size exceeds. | 403 |
| QuotaExceeded.DBInstanceStorage | The quota of instance storage exceeds. | 403 |
| InvalidDBInfo.Malformed | The specified parameter "DBInfo" is not valid or db not exist. | 400 |
| OperationDenied.Region | The operation is not permitted due to different region. | 403 |
| OperationDenied.Engine | The operation is not permitted due to different engine. | 403 |
| OperationDenied.DBInstanceId | The operation is not permitted due to DBInstanceId and SourceDBInstanceId is same. | 403 |
| InvalidTaskId.NotFound | The ImportId provided does not exist in our records. | 400 |
| OperationDenied.IncorrectTaskStatus | The operation is not permitted due to status of import. | 403 |
| InvalidAccountName.keyword | The specified parameter "AccountName" is a keyword. | 400 |
| InvalidAccountName.Duplicate | The Security db Name is not in the available range or occupied. | 400 |
| QuotaExceeded.AccountName | The quota of account exceeds. | 403 |
| OperationDenied.AccountStatus | The operation is not permitted due to status of account. | 403 |
| InvalidDBName.NotFound | The DBName provided does not exist in our records. | 404 |
| OperationDenied.AccountType | The operation is not permitted due to type of account. | 403 |
| OperationDenied.BackupJobExists | The operation is not permitted due to backup job exist. | 403 |

| D | eveloper Guide·API reference | A | psaraDB for RD | S |
|---|---|---|---|---|

| Error code | Error message | HTTP status code |
|---|---|---|
| OperationDenied.NoDatabase | The operation is not permitted due to no database. | 403 |
| InvalidStartTimeAndEndTime.Malform ed | The end time must be greater than the start time | 400 |
| OperationDenied.BackupJobExists | The operation is not permitted due to backup job exist. | 403 |
| InvalidBackupId.NotFound | The BackupId provided does not exist in our records. | 404 |
| OperationDenied.NotFoundBackup | The operation is not permitted due to no backup. | 403 |
| OperationDenied.BackupStatus | The operation is not permitted due to type of backup. | 403 |
| OperationDenied.BackupMethod | The operation is not permitted method of backup. | 403 |
| OperationDenied.TempDBInstanceExis ts | The operation is not permitted due to temp instance exist. | 403 |
| Forbidden.Authentication | The operation is forbidden by Aliyun Realname Authentication System. | 403 |
| IncorrectDBInstanceConnType | Current DB instance conn type does not support this operation. | 404 |
| IncorrecttVpcId.Mismatch | The specified parameter "VpcId" is not valid. | 400 |
| IntranetNetTypeNotExists | Current DB instance net type does not support this operation. | 404 |
| InvalidDBInstanceName.NotFound | The DBInstanceId provided does not exist in our records. | 403 |
| InvalidConnectionMode.ValueNotSupp orted | The specified parameter "ConnectionMode" is not valid. | 400 |
| InvalidConnectionString.Duplicate Specified | connection string already exists in the Aliyun RDS. | 403 |
| InvalidConnectionString.Duplicate Specified | connection string or port want to be modified is the same with current net type. | 400 |
| InvalidConnectionStringPrefix.Duplicat ed | Specified connection string already exists in the Aliyun RDS. | 403 |
| InvalidCurrentConnectionString.NotFo und | Specified current connection string doesn't exist. | 400 |

| A | psaraDB for RDS | Developer Guid | e·API referenc | e |
|---|---|---|---|---|

| Error code | Error message | HTTP status code |
|---|---|---|
| InvalidDBInstanceId.NotFound | The DBInstanceId provided does not exist in our records. | 400 |
| InvalidDBInstanceId.QuotaExceeded | The quota of instance id exceeds. | 400 |
| InvalidDBInstanceNetType.NotFound | The Specified DB instance net type is not found. | 404 |
| InvalidDBinstanceNetType.ValueNotSu pport | The specified parameter "DBinstanceNetType" is not valid. | 400 |
| InvalidDBInstanceType.ValueNotSupp ort | The specified parameter "DBInstanceType" is not valid. | 400 |
| InvalidEngineVersion.Malformed | The specified parameter "EngineVersion" is not valid. | 400 |
| InvalidInstanceNetworkType.ValueNot Supported | The specified parameter "InstanceNetworkType" is not valid. | 400 |
| InvalidParameter | The specified parameter "dbInstanceId" is not valid. | 400 |
| InvalidPort.Malformed | Specified port is not valid. | 400 |
| InvalidPrivateIpAddress.Duplicated | Specified private IP address is duplicated. | 400 |
| InvalidPrivateIpAddress.Mismatch | Specified private IP address is not in the CIDR block of virtual switch. | 400 |
| InvalidVPCId.NotFound | Specified virtual vpc is not found. | 400 |
| InvalidVSwitchId.Mismatch | Specified instance and virtual switch are not in the same zone. | 400 |
| InvalidVSwitchId.NotFound | Specified virtual switch is not found in specified VPC. | 400 |
| NetTypeExists | Specified net type already existed. | 400 |
| NetTypeExists | Specified public net type already existed. | 403 |
| OperationDenied.DBInstanceNetType | The operation is not permitted due to net type of instance. | 403 |
| OperationDenied.DBInstanceStatus | The operation is not permitted due to status of instance. | 403 |
| OperationDenied.DBInstanceType | The operation is not permitted due to type of instance. | 403 |

| eveloper Guide·API reference | A | psaraDB for RD |
|---|---|---|

| Error code | Error message | HTTP status code |
|---|---|---|
| OperationDenied.LockMode | The operation is not permitted due to lock of instance. | 403 |
| OperationDenied.Switch | Specified instance cannot be switched. | 400 |
| OperationDenied.Switch | Specified instance cannot be switched to VPC. | 403 |
| OperationDenied.SwitchToVPC | Specified instance cannot be switched to VPC. | 403 |
| OperationDenied | The resource is out of usage. | 403 |
| OperationDenied | The vpc cloudinstanceIp is use, please check params. | 406 |
| OperationDenied | The vpc service is error, please check params. | 400 |
| PARAMETER ERROR _ | The vpc request parameter may not be null. | 406 |
| PARAMETER MUST NOT NULL _ _ _ | The parameter must not be null. | 406 |
| PublicConnectionExists | PublicConnection exists. | 403 |
| bpcIzNoNotEqualsRdsMultIzNo | Specified vpc IzNo not equal rds IzNo. | 400 |
| OperationDenied.DBInstanceStatus | The operation is not permitted due to status of instance. | 403 |
| OperationDenied.DBInstanceType | The operation is not permitted due to type of instance. | 403 |
| OperationDenied.LockMode | The operation is not permitted due to lock of instance. | 403 |
| OperationDenied.Switch | Specified instance cannot be switched. | 400 |
| OperationDenied.SwitchToVPC | Specified instance cannot be switched to VPC. | 403 |
| OperationDenied | The resource is out of usage. | 403 |
| OperationDenied | The vpc cloudinstanceIp is use, please check params. | 406 |
| OperationDenied | The vpc service is error, please check params. | 400 |
| PARAMETER ERROR _ | The vpc request parameter may not be null. | 406 |
| PARAMETER MUST NOT NULL _ _ _ | The parameter must not be null. | 406 |
| PublicConnectionExists | PublicConnection exists. | 403 |

| psaraDB for RDS | Developer Guid | e·API referenc |
|---|---|---|

| Error code | Error message | HTTP status code |
|---|---|---|
| bpcIzNoNotEqualsRdsMultIzNo | Specified vpc IzNo not equal rds IzNo. | 400 |

#### 2.13.2 Error codes on the server

| Error code | Error message | HTTP status code |
|---|---|---|
| ServiceUnavailable | The request has failed due to a temporary failure of the server. | 503 |
| InternalError | The request processing has failed due to some unknown error, exception or failure. | 500 |

#### 2.13.3 Instance states

| State | Description |
|---|---|
| Creating | An instance is being created. |
| Running | An instance is in the running state. |
| Deleting | An instance is being deleted. |
| Rebooting | An instance is being restarted. |
| DBInstanceClassChanging | An instance is being upgraded or downgraded. |
| TRANSING | Data is being migrated. |
| EngineVersionUpgrading | Engine version is being upgraded. |
| TransingToOthers | Data is being migrated to other RDS instances. |
| GuardDBInstanceCreating | A disaster recovery instance is being created. |
| Restoring | A backup is being restored. |
| Importing | Data is being imported. |
| ImportingFromOthers | Data is being imported from other RDS instances. |
| DBInstanceNetTypeChanging | The network type is being switched between Intranet and Internet. |
| GuardSwitching | The instance is undergoing disaster recover failover. |
| INS CLONING _ | The instance is being cloned. |

#### 2.13.4 Performance parameters

ApsaraDB RDS for MySQL

| API parameter | Description |
|---|---|
| MySQL NetworkTraffic _ | The average inbound traffic to a MySQL instance per second and average outbound traffic from a MySQL instance per second. Unit: KB. |
| MySQL QPSTPS _ | The average number of SQL statements executed per second and average number of transactions per second. |
| MySQL Sessions _ | The number of active connections and total number of current connections. |
| MySQL InnoDBBufferRatio _ | The read hit rate of the InnoDB buffer pool, utilization of the InnoDB buffer pool, and percentage of dirty data blocks in the InnoDB buffer pool. |
| MySQL InnoDBDataReadWrit _ en | The average volume of data that InnoDB reads per second and average volume of data that InnoDB writes per second. Unit: KB. |
| MySQL InnoDBLogRequests _ | The average number of reads from the InnoDB buffer pool per second and average number of writes to the InnoDB buffer pool per second. |
| MySQL InnoDBLogWrites _ | The average number of log write requests per second, average number of physical writes to log files per second, and average number of fsync() writes to log files per second. |
| MySQL TempDiskTableCreat _ es | The number of temporary tables automatically created in the hard drive during MySQL statement execution. |
| MySQL MyISAMKeyBufferRati _ o | The average key buffer utilization of MyISAM per second, average key buffer read hit rate of MyISAM per second, and average key buffer write hit rate of MyISAM per second. |
| MySQL MyISAMKeyReadWrite _ s | The average number of data reads from the buffer pool by MyISAM per second, average number of data writes to the buffer pool by MyISAM per second, average number of data reads from the hard disk by MyISAM per second, and average number of data writes to the hard disk by MyISAM per second. |
| MySQL COMDML _ | The average number of DELETE statements executed per second, average number of INSERT statements executed per second, average number of INSERT SELECT statements executed per second, average number of _ REPLACE statements executed per second, and average number of REPLACE SELECT statements executed per second, average number of _ SELECT statements executed per second, and average number of UPDATE statements executed per second. |
| MySQL RowDML _ | The average number of rows read from the InnoDB table per second, average number of rows updated in the InnoDB table per second, average number of rows deleted from the InnoDB table per second, average number of rows inserted into the InnoDB table per second, and average number of physical writes to log files per second. |

| API parameter | Description |
|---|---|
| MySQL MemCpuUsage _ | The CPU utilization and memory usage of a MySQL Instance within the entire operating system. |
| MySQL IOPS _ | The IOPS of a MySQL instance. |
| MySQL DetailedSpaceUsage _ | The disk space occupied by a MySQL instance, including ins size (total _ space), data size (data space), log size (log space), tmp size (temporary _ _ _ space), and other size (system space). _ |
| slavestat | The latency of read-only instances. |

#### 2.13.5 Forbidden keywords

ApsaraDB RDS for MySQL

| Parameter field | Keyword description |
|---|---|

| Parameter field | Keyword description |
|---|---|
| DBName/ AccountName | admin,aurora,replicator,xtrabak,root(MySQL5.5/5.6),mysql,test,eagleye,information schema,guest,add,analyze,asc,between,blob,call,c _ hange,check,condition,continue,cross,current timestamp,database,day microsecon _ _ d,dec,default,desc,distinct,double,e ach,enclosed,exit,fetch,float8,foreign,goto,having,hour minute,ignore,infile,insensiti _ ve,int1,int4,interval,iterate,keys,lea ding,like,lines,localtimestamp,longblob,low priority,mediumint,minute microsecon _ _ d,modifies,no write to binlog,on, _ _ _ optionally,out,precision,purge,read,references,rename,require,revoke,schema,select ,set,spatial,sqlexception,sql big re _ _ sult,ssl,table,tinyblob,to,true,unique,update,using,utc timestamp,varchar,when,wit _ h,xor,all,and,asensitive,bigint,both,c ascade,char,collate,connection,convert,current date,current user,databases,day mi _ _ _ nute,decimal,delayed,describe,dis tinctrow,drop,else,escaped,explain,float,for,from,grant,high priority,hour second,in _ _ ,inner,insert,int2,int8,into,join,kill,le ave,limit,load,lock,longtext,match,mediumtext,minute second,natural,null,optimize _ ,or,outer,primary,raid0,reads,regex p,repeat,restrict,right,schemas,sensitive,show,specific,sqlstate,sql calc found row _ _ _ s,starting,terminated,tinyint,trailing, undo,unlock,usage,utc date,values,varcharacter,where,write,year month,alter,as,be _ _ fore,binary,by,case,character,colu mn,constraint,create,current time,cursor,day hour,day second,declare,delete,deter _ _ _ ministic,div,dual,elseif,exists,false, float4,force,fulltext,group,hour microsecond,if,index,inout,int,int3,integer,is,key,lab _ el,left,linear,localtime,long,loop,me diumblob,middleint,mod,not,numeric,option,order,outfile,procedure,range,real,rele ase,replace,return,rlike,second mi _ crosecond,separator,smallint,sql,sqlwarning,sql small result,straight join,then,tinyt _ _ _ ext,trigger,union,unsigned,use,utc _ time,varbinary,varying,while,x509,zerofill,galaxy |

#### 2.13.6 Instance types

Instances of different editions, versions, and types each performs differently from one another. ApsaraDB RDS for MySQL instance types

| Edition | Versi on | Instanc e family | Instance type | CPU and memory | Maxi mum conn ectio ns | Maxi mum IOPS | Disk space | Zone- disaste r recover y deploy ment |
|---|---|---|---|---|---|---|---|---|
| High- availabi lity Edition | 5.6/5 .7 | Dedicat ed instanc e (X8) | mysql.x8.mediu m.2 | 2 cores, 16 GB | 2,500 | 4,500 | 50GB- 1,000GB (in 5 GB increment s) | Single- data center deploy ment and dual- data center deploy ment |
|   |   |   | mysql.x8.large.2 | 4 cores, 32 GB | 5,000 | 9,000 | 50 GB to 1,000 GB (in 5 GB increment s) |   |
|   |   |   | mysql.x8.xlarge.2 | 8 cores, 64 GB | 10,00 0 | 18,00 0 | 500GB- 3,000GB (in 5 GB increment s) |   |
|   |   |   | mysql.x8.2xlarge. 2 | 16 cores, 128 GB | 20,00 0 | 36,00 0 | 500GB- 3,000GB (in 5 GB increment s) |   |
|   |   | Dedicat | mysql.x4.large.2 | 4 cores, 16 GB | 2,500 | 4,500 | 50GB- 1,000GB (in 5 GB increment s) |   |
|   |   |   | mysql.x4.xlarge.2 | 8 cores, 32 GB | 5,000 | 9,000 | 500GB- 3,000GB (in 5 GB increment s) |   |

|   |   |   | Apsar |   |   |   |   |   |
|---|---|---|---|---|---|---|---|---|
| Edition | Versi on | Dedicat ed instanc eIn s(Xta4n)c e family | Instance type | CPU and memory | Maxi mum conn ectio ns | Maxi mum IOPS | Disk space | Zone- disaste r recover y deploy ment |
|   |   |   | mysql.x4.2xlarge. 2 | 16 cores, 64 GB | 10,00 0 | 18,00 0 | 500GB- 3,000GB (in 5 GB increment s) |   |
|   |   |   | mysql.x4.4xlarge. 2 | 32 cores,128 GB | 20,00 0 | 36,00 0 | 1,000GB- 3,000GB (in 5 GB increment s) |   |
|   |   | Dedicat ed host | rds.mysql.st.d13 | 30 cores, 220 GB | 64,00 0 | 20,00 0 | 1,000GB- 3,000GB (in 5 GB increment s) |   |
|   |   | Dedicat ed instanc e (with high CPU) | mysql.x4.large.2 5 | 4 cores, 16 GB | 2,500 | 4,500 | 50GB- 1,000GB (in 5 GB increment s) |   |
|   |   |   | mysql.x4.xlarge.2 5 | 8 cores, 32 GB | 5,000 | 9,000 | 500GB- 3,000GB (in 5 GB increment s) |   |
|   |   |   | mysql.x4.2xlarge. 25 | 16 cores, 64 GB | 10,00 0 | 18,00 0 | 500GB- 3,000GB (in 5 GB increment s) |   |

|   |   |   | Developer Guide·A |   |   |   |   |   |
|---|---|---|---|---|---|---|---|---|
| Edition | Versi on | Instanc e family | Instance type | CPU and memory | Maxi mum conn ectio ns | Maxi mum IOPS | Disk space | Zone- disaste r recover y deploy ment |
|   |   |   | mysql.x4.4xlarge. 25 | 32 cores, 128 GB | 20,00 0 | 36,00 0 | 1,000GB- 3,000GB (in 5 GB increment s) |   |
| Enterpri se Edition | 5.7 |   |   |   |   |   |   | Single- data center Enterpr ise Edition and triple- data center disaste r recover y deploy ment |
|   |   | Dedicat ed instanc e (with high memor y) | mysql.x8.mediu m.25 | 2 cores, 16 GB | 2,500 | 4,500 | 50GB- 1,000GB (in 5 GB increment s) |   |
|   |   |   | mysql.x8.large.2 5 | 4 cores, 32 GB | 5,000 | 9,000 | 50GB- 1,000GB (in 5 GB increment s) |   |
|   |   |   | mysql.x8.xlarge.2 5 | 8 cores, 64 GB | 10,00 0 | 18,00 0 | 500GB- 3,000GB (in 5 GB increment s) |   |
|   |   |   | mysql.x8.2xlarge. 25 | 16 cores, 128 GB | 20,00 0 | 36,00 0 | 500GB- 3,000GB (in 5 GB increment s) |   |
|   |   |   | mysql.x8.4xlarge. 25 | 32 cores, 256 GB | 40,00 0 | 72,00 0 | 1,000GB- 3,000GB (in 5 GB increment s) |   |

|   |   |   | Apsar |   |   |   |   |   |
|---|---|---|---|---|---|---|---|---|
| Edition | Versi on | Instanc e family | Instance type | CPU and memory | Maxi mum conn ectio ns | Maxi mum IOPS | Disk space | Zone- disaste r recover y deploy ment |
|   |   | Dedicat ed host | mysql.st.12xlarg e.25 | 90 cores, 720 GB | 150,0 00 | 140,0 00 | 1,000GB- 6,000GB (in 5 GB increment s) |   |
|   |   |   | mysqlro.x8.medi um.1 | 2 cores, 16 GB | 2,500 | 4,500 | 50GB- 1,000GB (in 5 GB increment s) |   |
|   |   |   | mysqlro.x8.large. 1 | 4 cores, 32 GB | 5,000 | 9,000 | 50GB- 1,000GB (in 5 GB increment s) |   |
|   |   | Dedicat ed instanc e (X8) |   |   |   |   |   |   |
|   |   |   | mysqlro.x8.xlarg e.1 | 8 cores, 64 GB | 10,00 0 | 18,00 0 | 500GB- 3,000GB (in 5 GB increment s) |   |
|   |   |   | mysqlro.x8.2xlar ge.1 | 16 cores, 128 GB | 20,00 0 | 36,00 0 | 500GB- 3,000GB (in 5 GB increment s) |   |
|   |   |   | mysqlro.x8.4xlar ge.1 | 32 cores, 256 GB | 40,00 0 | 72,00 0 | 1,000GB- 6,000GB (in 5 GB increment s) |   |

|   |   |   | Developer Guide·A |   |   |   |   |   |
|---|---|---|---|---|---|---|---|---|
| Edition Read- only instanc | Versi on 5.6/5 .7 | Instanc e family | Instance type | CPU and memory | Maxi mum conn ectio ns | Maxi mum IOPS | Disk space | Zone- Single- disaste data r center recover deploy y ment deploy and ment dual- |
| e |   |   | mysqlro.x8.8xlar ge.1 | 64 cores, 512 GB | 80,00 0 | 14,40 0 | 1,000GB- 6,000GB (in 5 GB increment s) | data center deploy ment |
|   |   |   | mysqlro.x4.large. 1 | 4 cores, 16 GB | 2,500 | 4,500 | 50GB- 1,000GB (in 5 GB increment s) |   |
|   |   |   | mysqlro.x4.xlarg e.1 | 8 cores, 32 GB | 5,000 | 9,000 | 50GB- 1,000GB (in 5 GB increment s) |   |
|   |   | Dedicat ed instanc e (X4) |   |   |   |   |   |   |
|   |   |   | mysqlro.x4.2xlar ge.1 | 16 cores, 64 GB | 10,00 0 | 18,00 0 | 500GB- 3,000GB (in 5 GB increment s) |   |
|   |   |   | mysqlro.x4.4xlar ge.1 | 32 cores,128 GB | 20,00 0 | 36,00 0 | 500GB- 3,000GB (in 5 GB increment s) |   |
|   |   | Dedicat ed host | rds.mysql.st.v52 | 90 cores, 720 GB | 150,0 00 | 140,0 00 | 1,000GB- 6,000GB (in 5 GB increment s) |   |

ApsaraDB RDS for SQL Server instance types

| Edition | Versi on | Instanc e family | Instance type | CPU and memory | Maxi mum conn ectio ns | Maxi mum IOPS | Disk space | Zone- disaste r recover y deploy ment |
|---|---|---|---|---|---|---|---|---|
|   | 2008 R2 | Dedicat ed instanc e | mssql.x8.mediu m.2 | 2 cores, 16 GB | 2,500 | 4,500 | 250GB | Single- data center deploy ment and dual- data center deploy ment. This instanc e type is not availab le in new data centers , and does not suppor t V5 servers . |
|   |   |   | mssql.x8.large.2 | 4 cores, 32 GB | 5,000 | 9,000 | 500GB |   |
|   |   |   | mssql.x8.xlarge.2 | 8 cores, 64 GB | 10,00 0 | 18,00 0 | 1,000GB |   |
|   |   |   | mssql.x8.2xlarge. 2 | 16 cores, 128 GB | 20,00 0 | 36,00 0 | 2,000GB |   |
|   |   | Dedicat ed host | rds.mssql.st.d13 | 30 cores, 220 GB | 64,00 0 | 20,00 0 | 2TB |   |
|   |   |   | mssql.x4.mediu m.e2 | 2 cores, 8 GB |   |   |   |   |
|   |   |   | mssql.x8.mediu m.e2 | 2 cores, 16 GB |   |   |   |   |
|   |   |   | mssql.x4.large.e 2 | 4 cores, 16 GB |   |   |   |   |
|   |   |   | mssql.x8.large.e 2 | 4 cores, 32 GB |   |   |   |   |
|   |   |   | mssql.x4.xlarge.e 2 | 8 cores, 32 GB |   |   |   |   |
|   |   |   | mssql.x8.xlarge.e 2 | 8 cores, 64 GB |   |   |   |   |

| Edition | 2012 EE: 2012 Veenrsti _ _ hoan 2016 EE: | Instanc e Dfaemdiiclyat ed instanc | Instance type | CPU and memory | Maxi mum conn ectio ns | Maxi mum IOPS | Disk space | Zone- disaste r recover y deploy ment |
|---|---|---|---|---|---|---|---|---|
|   |   | e |   |   |   |   |   |   |
| High- availabi lity Edition | 2016 ent _ _ ha |   | mssql.x4.2xlarge. e2 | 16 cores, 64 GB | Not limite d | Depe nden t on the perfo rman ce of cloud disks | 20GB- 4,000GB | Single- data center deploy ment |
|   |   |   | mssql.x8.2xlarge. e2 | 16 cores, 128 GB |   |   |   |   |
|   |   |   | mssql.x4.3xlarge. e2 | 24 cores, 96 GB |   |   |   |   |
|   |   |   | mssql.x4.4xlarge. e2 | 32 cores,128 GB |   |   |   |   |
|   |   |   | mssql.x8.4xlarge. e2 | 32 cores, 256 GB |   |   |   |   |
|   |   |   | mssql.x8.7xlarge. e2 | 56 cores, 480 GB |   |   |   |   |
|   |   |   | mssql.x4.8xlarge. e2 | 64 cores, 256 GB |   |   |   |   |
|   |   |   | mssql.x8.8xlarge. e2 | 64 cores, 512 GB |   |   |   |   |
|   | 2012 SE: 2012 std _ _ ha 2016 SE: 2016 std _ _ ha | Dedicat ed instanc e | mssql.x4.mediu m.s2 | 2 cores, 8 GB |   |   |   |   |
|   |   |   | mssql.x8.mediu m.s2 | 2 cores, 16 GB |   |   |   |   |
|   |   |   | mssql.x4.large.s2 | 4 cores, 16 GB |   |   |   |   |
|   |   |   | mssql.x8.large.s2 | 4 cores, 32 GB |   |   |   |   |
|   |   |   | mssql.x4.xlarge.s 2 | 8 cores, 32 GB |   |   |   |   |
|   |   |   | mssql.x8.xlarge.s 2 | 8 cores, 64 GB |   |   |   |   |
|   |   |   | mssql.x4.2xlarge. s2 | 16 cores, 64 GB |   |   |   |   |

| Edition | Versi on | Instanc e family | Instance type | CPU and memory | Maxi mum conn ectio ns | Maxi mum IOPS | Disk space | Zone- disaste r recover y deploy ment |
|---|---|---|---|---|---|---|---|---|
|   |   |   | mssql.x8.2xlarge. s2 | 16 cores, 128 GB |   |   |   |   |
|   |   |   | mssql.x4.3xlarge. s2 | 24 cores, 96 GB |   |   |   |   |

PolarDB instance types

| Edition | Version | Instance family | Instance type | CPU and memory | Maximu m connecti ons | Maximu m IOPS | Disk space | Zone- disaster recovery deploy ment |
|---|---|---|---|---|---|---|---|---|
| High- availabili ty Edition | 11 | Dedicat ed instance | polardb. x4.small .2 | 1 core, 4 GB | 200 | 5,000 | 250GB | Single- data center deploy ment and dual- data center |
|   |   |   | polardb. x4.medi um.2 | 2 cores, 8 GB | 400 | 10,000 |   |   |
|   |   |   | polardb. x8.medi um.2 | 2 cores, 16 GB | 2,500 | 15,000 |   |   |
|   |   |   | polardb. x4.large. 2 | 4 cores, 16 GB | 2,500 | 20,000 | 250GB- 500GB (in 5 GB increme nts) |   |
|   |   |   | polardb. x8.large. 2 | 4 cores, 32 GB | 5,000 | 30,000 |   |   |
|   |   |   | polardb. x4.xlarg e.2 | 8 cores, 32 GB | 5,000 | 40,000 | 500GB- 1,000GB (in 5 GB increme nts) |   |
|   |   |   | polardb. x8.xlarg e.2 | 8 cores, 64 GB | 10,000 | 60,000 |   |   |
|   |   |   |   |   |   |   | ment Versio |   |

|   |   |   | Devel |   |   |   |   |   |
|---|---|---|---|---|---|---|---|---|
| Edition | Version | Instance family | Instance type | CPU and memory | Maximu m connecti ons | Maximu m IOPS | Disk space | deploy Zone- ment disaster recovery deploy ment |
|   |   |   | polardb. x4.2xlar ge.2 | 16 cores, 64 GB | 10,000 | 80,000 | 1,000GB - 2,000GB (in 5 GB increme nts) |   |
|   |   |   | polardb. x8.2xlar ge.2 | 16 cores, 128 GB | 12,000 | 120,000 |   |   |
|   |   |   | polardb. x4.4xlar ge.2 | 32 cores, 128 GB | 12,000 | 160,000 | 2,000GB - 3,000GB (in 5 GB increme nts) |   |
|   |   |   | polardb. x8.4xlar ge.2 | 32 cores, 256 GB | 12,000 | 240,000 |   |   |
|   |   | Dedicat ed host | rds.pola rdb.st.h 43 | 60 cores, 470 GB | 12,000 | 450,000 | 6,000GB |   |

ApsaraDB RDS for PostgreSQL instance types

| Edition | Version | Instance family | Instance type | CPU and memory | Maximu m connecti ons | Maximu m IOPS | Disk space | Zone- disaster recovery deploy ment |
|---|---|---|---|---|---|---|---|---|
| High- availabili ty Edition or read- | 9.4/10 | Dedicat ed instance (with high capacity ) | pg.x8.m edium.2 | 2 cores, 16 GB | 2,500 | 4,500 | 20GB- 6,000GB | Single- data center deploy ment and dual- |
|   |   |   | pg.x8.la rge.2 | 4 cores, 32 GB | 5,000 | 9,000 |   |   |
|   |   |   | pg.x8.xl arge.2 | 8 cores, 64 GB | 10,000 | 18,000 |   |   |
|   |   |   | pg.x8.2x large.2 | 16 cores, 128 GB | 12,000 | 36,000 |   |   |
|   |   |   | pg.x4.la rge.2 | 4 cores, 16 GB | 2,500 | 4,500 |   |   |
|   |   |   | pg.x4.xl arge.2 | 8 cores, 32 GB | 5,000 | 9,000 |   |   |

|   |   | rence |   |   |   |   |   |   |
|---|---|---|---|---|---|---|---|---|
| only instance Edition | Version | Dedicat ed iInnssttaannccee (fwamithily high CPU) | Instance type | CPU and memory | Maximu m connecti ons | Maximu m IOPS | (in 5 GB increme nDtissk) space | data Zone- center disaster deploy recovery ment deploy ment |
|   |   |   | pg.x4.2x large.2 | 16 cores, 64 GB | 10,000 | 18,000 |   |   |
|   |   |   | pg.x4.4x large.2 | 32 cores, 128 GB | 12,000 | 36,000 |   |   |
|   |   | Dedicat ed host | rds.pg.s t.h43 | 60 cores, 470 GB | 4,000 | 50,000 |   |   |
