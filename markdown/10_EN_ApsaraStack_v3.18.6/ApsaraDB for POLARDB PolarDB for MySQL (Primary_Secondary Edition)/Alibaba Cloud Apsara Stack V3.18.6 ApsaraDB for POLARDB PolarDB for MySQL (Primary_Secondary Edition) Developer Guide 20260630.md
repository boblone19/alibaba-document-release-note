---
title: "ApsaraDB for POLARDB PolarDB for MySQL (Primary_Secondary Edition) Developer Guide 20260630"
product_version: "V3.18.6"
pdf_pages: 126
source_pdf: "2e5651216b3dfe30_Alibaba Cloud Apsara Stack V3.18.6 ApsaraDB for POLARDB PolarDB for MySQL (Primary_Secondary Edition"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/v3.18.6%E7%89%88%E6%9C%AC%E6%96%87%E6%A1%A3/PolarDB%20MySQL%E6%9C%AC%E5%9C%B0%E7%9B%98/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.6%20ApsaraDB%20for%20POLARDB%20PolarDB%20for%20MySQL%20%28Primary_Secondary%20Edition%29%20Developer%20Guide%2020260630.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings)
---

# ApsaraDB for POLARDB PolarDB for MySQL (Primary_Secondary Edition) Developer Guide 20260630

## Table of Contents

- 1 API reference
  - 1.1 List of operations by function
  - 1.2 Make API requests
    - 1.2.1 Request structure
    - 1.2.2 Common parameters
      - 1.2.2.1 Common request parameters
      - 1.2.2.2 Common response parameters
    - 1.2.3 Responses
      - 1.2.3.1 Sample success responses
      - 1.2.3.2 Error responses
    - 1.2.4 Request signatures
  - 1.3 Instance management
    - 1.3.1 CreateDBInstance
    - 1.3.2 DeleteDBInstance
    - 1.3.3 RestartDBInstance
    - 1.3.4 DescribeDBInstanceAttribute
    - 1.3.5 DescribeDBInstances
    - 1.3.6 ModifyDBInstanceSpec
    - 1.3.7 AllocateInstancePublicConnection
    - 1.3.8 ReleaseInstancePublicConnection
    - 1.3.9 SwitchDBInstanceNetType
    - 1.3.10 DescribeDBInstanceNetInfo
    - 1.3.11 ModifyDBInstanceConnectionString
    - 1.3.12 ModifyDBInstanceConnectionMode
    - 1.3.13 ModifyDBInstanceNetworkType
    - 1.3.14 DescribeDBInstanceIPArrayList
    - 1.3.15 ModifySecurityIps
    - 1.3.16 DescribeRegions
    - 1.3.17 DescribeDBInstanceHAConfig
    - 1.3.18 MigrateToOtherZone
    - 1.3.19 PurgeDBInstanceLog
    - 1.3.20 UpgradeDBInstanceEngineVersion
    - 1.3.21 ModifyDBInstanceDescription
    - 1.3.22 ModifyDBInstanceMaintainTime
    - 1.3.23 ModifyDBInstanceHAConfig
    - 1.3.24 SwitchDBInstanceHA
    - 1.3.25 CreateReadOnlyDBInstance
    - 1.3.26 DescribeDBInstanceSSL
    - 1.3.27 ModifyDBInstanceSSL
    - 1.3.28 DescribeDBInstanceTDE
    - 1.3.29 ModifyDBInstanceTDE
  - 1.4 Database management
    - 1.4.1 CreateDatabase
    - 1.4.2 DeleteDatabase
    - 1.4.3 DescribeDatabases
    - 1.4.4 ModifyDBDescription
  - 1.5 Account management
    - 1.5.1 CreateAccount
    - 1.5.2 DeleteAccount
    - 1.5.3 DescribeAccounts
    - 1.5.4 GrantAccountPrivilege
    - 1.5.5 RevokeAccountPrivilege
    - 1.5.6 ModifyAccountDescription
    - 1.5.7 ResetAccountPassword
    - 1.5.8 ResetAccount
  - 1.6 Backup and restoration
    - 1.6.1 CreateBackup
    - 1.6.2 CloneDBInstance
    - 1.6.3 DescribeBackups
    - 1.6.4 CreateTempDBInstance
    - 1.6.5 DescribeBackupPolicy
    - 1.6.6 ModifyBackupPolicy
    - 1.6.7 RestoreDBInstance
    - 1.6.8 DeleteBackup
  - 1.7 Monitoring management
    - 1.7.1 DescribeResourceUsage
    - 1.7.2 DescribeDBInstancePerformance
    - 1.7.3 DescribeDBInstanceMonitor
    - 1.7.4 ModifyDBInstanceMonitor
  - 1.8 Parameter management
    - 1.8.1 DescribeParameterTemplates
    - 1.8.2 DescribeParameters
    - 1.8.3 ModifyParameter
  - 1.9 Log management
    - 1.9.1 DescribeSlowLogs
    - 1.9.2 DescribeSlowLogRecords
    - 1.9.3 DescribeErrorLogs
    - 1.9.4 DescribeBinlogFiles
    - 1.9.5 DescribeSQLCollectorPolicy
    - 1.9.6 ModifySQLCollectorPolicy
    - 1.9.7 DescribeSQLLogRecords
    - 1.9.8 DescribeSQLLogFiles
  - 1.10 Data migration
    - 1.10.1 CreateUploadPathForSQLServer
    - 1.10.2 ImportDatabaseBetweenInstances
    - 1.10.3 CancelImport
  - 1.11 Tag management
    - 1.11.1 AddTagsToResource
    - 1.11.2 DescribeTags
    - 1.11.3 RemoveTagsFromResource
  - 1.12 RAM authorization
  - 1.13 Appendix
    - 1.13.1 Client error codes
      - 1.13.1.1 Common errors
      - 1.13.1.2 Specific errors
    - 1.13.2 Error codes on the server
    - 1.13.3 Instance states
    - 1.13.4 Performance parameters
    - 1.13.5 Forbidden keywords
- 2 SDK reference
  - 2.1 Obtain the SDK source code
  - 2.2 SDK for Java
    - 2.2.1 Use the SDK
      - 2.2.1.1 Use CommonRequest
  - 2.3 SDK for Python
    - 2.3.1 Use the SDK
      - 2.3.1.1 Use CommonRequest
  - 2.4 SDK for PHP
    - 2.4.1 Quick start
  - 2.5 SDK for C#
- 3 Obtain an endpoint
- 4 Obtain an AccessKey pair

## 1 API reference

### 1.1 List of operations by function

The following tables list the API operations available for use in PolarDB.

**Instance management**

| Operation | Description |
|---|---|
| CreateDBInstance | Creates an instance. |
| DeleteDBInstance | Releases an instance. |
| RestartDBInstance | Restarts an instance. |
| DescribeDBInstanceAttribute | Queries the attributes of instances. |
| DescribeDBInstances | Queries a list of instances. |
| ModifyDBInstanceSpec | Modifies the configurations of an instance. |
| AllocateInstancePublicConnection | Applies for a public endpoint for an instance. |
| ReleaseInstancePublicConnection | Releases the public endpoint of an instance. |
| SwitchDBInstanceNetType | Applies for an internal endpoint for an instance. |
| DescribeDBInstanceNetInfo | Queries the connection information of an instance. |
| ModifyDBInstanceConnectionString | Modifies the endpoint and port of an instance. |
| ModifyDBInstanceConnectionMode | Changes the access mode of an instance. |
| ModifyDBInstanceNetworkType | Changes the network type of an instance. |
| DescribeDBInstanceIPArrayList | Queries the IP address whitelist of an instance. |
| ModifySecurityIps | Modifies the IP address whitelist of an instance. |

| DescribeRegions | Queries available regions and zones. |
|---|---|
| DescribeDBInstanceHAConfig | Queries the zone information and data replication status of an instance. |
| MigrateToOtherZone | Migrates an instance from one zone to another. |
| PurgeDBInstanceLog | Clears all binlogs of an instance. |
| UpgradeDBInstanceEngineVersion | Updates the database version of an instance. |
| ModifyDBInstanceDescription | Modifies the description of an instance. |
| ModifyDBInstanceMaintainTime | Modifies the maintenance window of an instance. |
| ModifyDBInstanceHAConfig | Modifies the data replication mode and high availability switching rules of an instance. |
| SwitchDBInstanceHA | Switches between the primary and secondary instances. |
| CreateReadonlyDBInstance | Creates a read-only instance for a primary instance. |
| DescribeDBInstanceSSL | Queries the SSL link of an instance. |
| ModifyDBInstanceSSL | Modifies the SSL link of an instance. |

**Database management**

| Operation | Description |
|---|---|
| CreateDatabase | Creates a database. |
| DeleteDatabase | Deletes a database. |
| DescribeDatabases | Queries a list of databases. |
| ModifyDBDescription | Modifies the description of a database. |

**Account management**

| Operation | Description |
|---|---|
| CreateAccount | Creates an account. |
| DeleteAccount | Deletes an account. |
| DescribeAccounts | Queries a list of accounts. |
| GrantAccountPrivilege | Grants permissions to an account. |
| RevokeAccountPrivilege | Revokes permissions from an account. |
| ModifyAccountDescription | Modifies the description of an account. |
| ResetAccountPassword | Resets the password of an account. |
| ResetAccount | Resets the initial account of an instance. |

**Backup and restoration**

| Operation | Description |
|---|---|
| CreateBackup | Creates a backup. |
| CloneDBInstance | Clones a PolarDB instance. |
| DescribeBackups | Queries the backup sets of an instance. |
| CreateTempDBInstance | Creates a temporary instance. |
| DescribeBackupPolicy | Queries the backup policy configured for an instance. |
| ModifyBackupPolicy | Modifies the backup policy configured for an instance. |
| RestoreDBInstance | Restores an instance from a backup set. |

| DeleteBackup | Deletes the data backup files of an instance. |
|---|---|

**Monitoring management**

| Operation | Description |
|---|---|
| DescribeResourceUsage | Queries the resource usage of an instance. |
| DescribeDBInstancePerformance | Queries the performance metrics of an instance. |
| DescribeDBInstanceMonitor | Queries the monitoring behavior of an instance. |
| ModifyDBInstanceMonitor | Modifies the monitoring behavior of an instance. |

**Parameter management**

| Operation | Description |
|---|---|
| DescribeParameterTemplates | Queries a list of parameter templates. |
| DescribeParameters | Queries the parameter settings of an instance. |
| ModifyParameter | Modifies the parameters of an instance. |

**Log management**

| Operation | Description |
|---|---|
| DescribeSlowLogs | Queries the summary of slow query logs. |
| DescribeSlowLogRecords | Queries the details of slow query logs. |
| DescribeErrorLogs | Queries error logs. |
| DescribeBinlogFiles | Queries binlogs. |
| DescribeSQLCollectorPolicy | Checks whether the SQL audit feature is enabled. |

| ModifySQLCollectorPolicy | Enables or disables the SQL audit feature. |
|---|---|
| DescribeSQLLogRecords | Queries SQL audit logs. |
| DescribeSQLLogFiles | Queries a list of SQL audit log files. |

**Data migration**

| Operation | Description |
|---|---|
| ImportDatabaseBetweenInstances | Migrates data from an instance. |
| CancelImport | Cancels a migration from an instance. |

**Tag management**

| Operation | Description |
|---|---|
| AddTagsToResource | Adds tags. |
| DescribeTags | Queries tags. |
| RemoveTagsFromResource | Removes tags. |

### 1.2 Make API requests

#### 1.2.1 Request structure

This topic describes the request structure of Apsara DB for RDS API operations.

**Endpoints**

The endpoint of the Apsara DB for RDS API is rds.example.com. For information about how to obtain a service endpoint, see Obtain the endpoint of ASAPI.

**Protocols**

You can send requests over HTTP or HTTPS. We recommend that you use HTTPS for enhanced security.

**Methods**

You can use the HTTP GET method to send requests. When you use this method, you must include request parameters in the request URL.

**Parameters**

The action to be performed must be specified in the Action parameter of each request. Each operation request must include common request parameters and the specific request parameters of the operation called.

**Encoding**

All requests and responses are encoded in UTF-8.

#### 1.2.2 Common parameters

##### 1.2.2.1 Common request parameters

Common request parameters must be included in the request of each API.

| Parameter | Typ e | Requi red | Description |
|---|---|---|---|
| Format | Stri ng | No | The format of the response. Valid values: JSON and XML. Default value: XML. |
| Version | Stri ng | Yes | The API version. It is in the YYYY-MM-DD format. The current version is 2014-08-15. |
| AccessKeyId | Stri ng | Yes | The AccessKey ID provided to you by Alibaba Cloud. |
| Signature | Stri ng | Yes | The signature result string. For more information about the signature calculation method, see Request signatures. |
| SignatureMet hod | Stri ng | Yes | The algorithm used to create the request signature. Valid value: HMAC-SHA1. |
| Timestamp | Stri ng | Yes | The request timestamp. The timestamp follows the ISO 8601 standard and uses UTC. It is in the YYYY-MM-DDThh:mm:ssZ format. For example, 20:00:00, August 15, 2013, UTC+8 will be written as 2013-08-15T12:00:00Z. |
| SignatureVer sion | Stri ng | Yes | The signature algorithm version. The current version is 1.0. |
| SignatureNo nce | Stri ng | Yes | A unique, randomly generated number used to prevent network replay attacks. You must use a different random number for each request. |

**Example**

```
https://rds.example.com/ ? Format=xml &Version=2014-08-15 &Signature=Pc5WB8gokVnxxxxx &SignatureMethod=HMAC-SHA1 &SignatureNonce=15215528852396 &SignatureVersion=1.0 &AccessKeyId=key-test &OwnerId=12345678 &Timestamp=2014-10-10T12:00:00Z
```

##### 1.2.2.2 Common response parameters

Every response returns a unique request ID regardless of whether the call is successful.

**Example:**

```xml
<?xml version="1.0" encoding="utf-8"?> <!—Result root node--> <Operation name + Response>
    <!—Returned request tag-->
    <RequestId>4C4***38-****-****-****-*******6F216</RequestId>
    <!—Return result data-->
</Operation name + Response>
```

#### 1.2.3 Responses

##### 1.2.3.1 Sample success responses

The response data for API requests is displayed in a uniform format. In the response data, a 2xx HTTP status code indicates that the API operation is called. Responses can be returned in either the JSON or XML format. You can specify the response format in the request. The default response format is XML. The response examples in this section have been formatted with line breaks or indents for a clear view. The actual responses are not properly formatted as these examples. Responses in the XML format include the result of the request and the details of the operation. Examples:

```json
<!—Result root node--> <Operation name + Response> <!—Returned request tag--> <RequestId>4C467B38-****-447D-****-AC04*******16</RequestId> <!—Return result data--> </Operation name + Response> { "RequestId": "4C467B38-****-447D-****-AC04*******16", /* Return result data */}
```

##### 1.2.3.2 Error responses

When an error occurs during an API call, no result data is returned. You can locate the cause of the error by referencing Error codes in Appendix. When an error occurs on an HTTP request for an API operation, a 4xx or 5xx HTTP status code is returned. The response body includes the error code and error message. RequestId uniquely identifies the request and HostId indicates the ID of the site requested to be accessed. You can contact Alibaba Cloud customer service when the cause of the error cannot be found. We recommend that you provide HostId and RequestId to help us resolve the issue at the earliest opportunity.

```json
<Error> <RequestId>8906582E-****-****-A6C4-0E78*******5</RequestId> <HostId>rds.example.com</HostId> <Code>UnsupportedOperation</Code> <Message>The specified action is not supported. </Message> </Error> { "RequestId": "7463B73D-****-4D19-****-6B8*******2EF", "HostId": "rds.example.com", "Code": "UnsupportedOperation", "Message": "The specified action is not supported."
```

`}`

#### 1.2.4 Request signatures

ApsaraDB for RDS authenticates each access request. Therefore, a request must contain signature information regardless of whether it is sent over HTTP or HTTPS. For information about how to obtain an AccessKey pair (AccessKey ID and AccessKey secret), see Obtain an AccessKey pair. ApsaraDB for RDS implements symmetric encryption with an AccessKey pair to verify the identity of the request sender. The AccessKey pair is issued by Alibaba Cloud. You can apply for AccessKey pairs and manage them on the official Alibaba Cloud website. The AccessKey ID is used to verify the identity of the user. The AccessKey secret is used to encrypt and verify the signature string on the server. You must keep your AccessKey secret strictly confidential. Perform the following steps to sign an access request:
1. Use request parameters to construct a canonicalized query string.
i. Sort all of the request parameters in alphabetical order. The request parameters include all common and operation-specific parameters except Signature.

**Note**

If you use the GET method to send a request, the request parameters are included as part of the request URI. The request parameters in the URI are placed after a question mark (?) and separated by ampersands (&). ii. Encode the name and value of each request parameter. Parameter names and values must be encoded into a URL based on the UTF-8 character set. The following rules apply in the URL encoding process: Uppercase letters, lowercase letters, digits, and some special characters such as hyphens (-), underscores (_), periods (.), and tildes (~) do not need to be encoded. Other characters must be percent encoded in %XY format. XY represents the ASCII code of the characters in hexadecimal notation. For example, double quotation marks (") are encoded as %22. Extended UTF-8 characters are encoded in the %XY%ZA… format. Spaces must be encoded as %20. Do not encode spaces as plus signs (+).

**Note**

Most libraries that support URL encoding, such as java.net.URLEncoder, comply with the Multipurpose Internet Mail Extensions (MIME) encoding rules of application/x-www-form-urlencoded. If this encoding method is used, replace the plus signs (+) in the encoded strings with %20, the asterisks (*) with %2A, and %7E with a tilde (~) to conform to the encoding rules. iii. Connect the encoded parameter names and values by using equal signs (=). iv. Sort the equal sign-connected strings by their parameter names in alphabetical order and connect them with ampersands (&).
2. Create a string-to-sign from the encoded canonicalized query string based on the following
rules:

```
StringToSign= HTTPMethod + "&" + percentEncode("/") + "&" + percentEncode(CanonicalizedQueryString)
```

HTTPMethod: specifies the HTTP method used to make the request, such as GET. percentEncode("/"): specifies the encoded value for the forward slash (/) based on the URL encoding rules described in 1.b. The value is %2F. percentEncode(CanonicalizedQueryString): specifies the string encoded from the canonicalized query string constructed in Step 1 based on the URL encoding rules described in 1.b.
3. Calculate the HMAC value of the string-to-sign by using the AccessKey secret as the key.

**Note**

An ampersand (&) is added to the end of the key (ASCII: 38). The hashing algorithm used is SHA-1.
4. Encode the HMAC value in Base64 to obtain the signature string.
5. Add the signature string to the request as the Signature parameter.

**Note**

When the signature string is submitted to the RDS server as the final request parameter value, the string must be URL-encoded like other parameters based on rules defined in RFC 3986. The following code is the request URL without a signature for the DescribeDBInstances operation:

```
http://rds.example.com/?TimeStamp=2013-06- 01T10:33:56Z&Format=XML&AccessKeyId=testid&Action=DescribeDBInstances&SignatureMethod=H C-SHA1&RegionId=region1&SignatureNonce=NwDAxvLU6tFE0DVb&Version=2014-08- 15&SignatureVersion=1.0
```

The following code is the string-to-sign:

```
GET&%2F&AccessKeyId%3Dtestid%26Action%3DDescribeDBInstances%26Format%3DXML%26RegionId%3 egion1%26SignatureMethod%3DHMAC- SHA1%26SignatureNonce%3DNwDAxvLU6tFE0DVb%26SignatureVersion%3D1.0%26TimeStamp%3D2013- 06-01T10%253A33%253A56Z%26Version%3D2014-08-15
```

Assume that the AccessKey ID is testid, the AccessKey secret is testsecret, and the key used for HMAC calculation is testsecret&. The following signature string is obtained:

```
BIPOMlu8LXBeZtLQkJTw6iFvw1E=
```

The following code is the signed request URL that has the Signature parameter added:

```
http://rds.example.com/?TimeStamp=2013-06- 01T10%3A33%3A56Z&Format=XML&AccessKeyId=testid&Action=DescribeDBInstances&SignatureMeth =HMAC-SH
```

### 1.3 Instance management

#### 1.3.1 CreateDBInstance

You can call this operation to create an ApsaraDB for RDS instance. For information about instance types, see Instance types in Appendix.

| Parameter | Type | Requir ed | Description |
|---|---|---|---|
| Action | Strin g | Yes | The operation that you want to perform. Set the value to CreateDBInstance. |
| RegionId | Strin g | Yes | The region ID of the instance. It can be up to 50 characters in length. You can call the DescribeRegions operation to query the most recent region list. |
| ZoneId | Strin g | No | The zone ID of the instance. You can call the DescribeRegions operation to query the most recent zone list. |

| Engine | Strin g | Yes | The engine of the database. Valid values: MySQL SQLServer PostgreSQL POLARDB |
|---|---|---|---|
| EngineVersion | Strin g | Yes | The engine version of the database. Valid values: MySQL: 5.6 and 5.7 SQL Serve: 2008 R2, 2012 ent ha, 2012 std ha, _ _ _ _ 2016 ent ha, and 2016 std ha _ _ _ _ PostgreSQL: 9.4 and 10.0 PolarDB: 11 |
| DBInstanceClass | Strin g | Yes | The type of the instance. |
| DBInstanceStora ge | Integ er | Yes | The user-defined storage space. Valid values: MySQL High-availability Edition: 5 to 2000 PolarDB High-availability Edition: 5 to 2000 This value must be in 5 GB increments. Unit: GB. |
| DBInstanceNetT ype | Strin g | Yes | The network connection type of the instance. Valid values: Internet Intranet |
| DBInstanceDesc ription | Strin g | No | The description of the instance. It must be 2 to 256 characters in length and can contain letters, digits, underscores ( ), and hyphens (-). It must start with a letter _ and cannot start with http:// or https://. |
| SecurityIPList | Strin g | Yes | The list of IP addresses that are allowed to access all databases in the instance. You can add a maximum of 1,000 IP addresses and separate them with commas (,). Format: %, 0.0.0.0/0, 10.23.12.24 (IP address), or 10.23.12.24/24 (CIDR block, where /24 indicates the prefix of the CIDR block is 24- bit. You can replace 24 with a value ranging from 1 to 32.). 0.0.0.0/0 indicates that the instance can be accessed by all devices. |
| ClientToken | Strin g | Yes | The client token that is used to ensure the idempotence of the request. |
| InstanceNetwork Type | Strin g | No | The network type of the instance. Valid values: VPC and Classic. Default value: Classic. |
| ConnectionMode | Strin g | No | The access mode of the instance. Valid values: Standard and Safe. If no value is specified, the system automatically assigns an access mode. |
| VPCId | Strin g | No | The ID of the VPC. |
| VSwitchId | Strin g | No | The ID of the VSwitch. |

| PrivateIpAddress | Strin g | No | The VPC IP address that belongs to the specified VSwitch. If no value is specified, the system automatically assigns a VPC IP address. |
|---|---|---|---|

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> | - | For more information, see. |
| DBInstanceId | String | The ID of the instance. |
| OrderId | String | The ID of the order. |
| ConnectionString | String | The endpoint used to connect to the database. |
| Port | String | The port used to connect to the database. |

```json
<CreateDBInstanceResponse> <OrderId>100789370xxxxx</OrderId> <ConnectionString>xxxxx.mysql.rds.aliyuncs.com </ConnectionString> <DBInstanceId>rds-xxxxx</DBInstanceId> <port>3306</port> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> </CreateDBInstanceResponse> { "OrderId": "100789370230206", "ConnectionString": "rds-xxxxx.mysql.rds.aliyuncs.com", "DBInstanceId": "rds-xxxxx", "Port": "3306", "RequestId": "1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC"}
```

#### 1.3.2 DeleteDBInstance

You can call this operation to release an RDS instance. Before you call this operation, ensure that the following requirements are met: The instance is in the running state. The instance is not manually locked. The instance is a pay-as-you-go primary instance, read-only instance, disaster recovery instance, or temporary instance.

| Parameter | Type | Required | Description |
|---|---|---|---|

| Action | String | Yes | The operation that you want to perform. Set the value to DeleteDBInstance. |
|---|---|---|---|
| DBInstanceI d | String | Yes | The ID of the instance to be released. |

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> | - | For more information, see Common response parameters. |

**Sample requests**

```
https://rds.example.com/?Action=DeleteDBInstance &DBInstanceId=rds-xxxxx &<[Common request parameters]>
```

**Sample responses**

```json
<DeleteDBInstanceResponse> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> </DeleteDBInstanceResponse> { "RequestId": "1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC" }
```

#### 1.3.3 RestartDBInstance

You can call this operation to restart an RDS instance. The instance will be restarted in 10 seconds. If there are a large number of transactions that must be submitted or rolled back, the restart process may be delayed for a minute. Before you call this operation, ensure that the following requirements are met: The instance is in the running state. The instance is not performing a backup task.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to RestartDBInstance. |

| DBInstanceI d | String | Yes | The ID of the instance to be restarted. |
|---|---|---|---|

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> | - | For more information, see Common response parameters. |

```json
<RestartDBInstanceResponse> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> </RestartDBInstanceResponse> { "RequestId": "1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC"}
```

#### 1.3.4 DescribeDBInstanceAttribute

You can call this operation to query attributes of an instance.

| Paramete r | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeDBInstanceAttribute. |
| DBInstanc eId | String | Yes | The ID of the instance. Up to 30 IDs can be entered at a time. Separate multiple IDs with commas (,). |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Items |   |   | The array that consists of DBInstanceAttribute data. |
| └DBInstanceId | String | rm-bpvxxxxx | The ID of the instance. |
| └ DBInstanceType | String | Primary | The role of the instance. Valid values: Primary: primary instance Readonly: read-only instance Guard: disaster recovery instance Temp: temporary instance |

| └Category | String | Basic | The RDS edition of the instance. Valid values: Basic: Basic Edition Standard: High-availability Edition Enterprise: Enterprise Edition |
|---|---|---|---|
| └InstanceNetwor kType | String | Classic | The network type of the instance. Valid values: Classic VPC |
| └RegionId | String | cn-hangzhou | The region ID of the instance. |
| └ZoneId | String | cn-hangzhou-a | The zone ID of the instance. |
| └ConnectionStrin g | String | rds- xxxxx.mysql.rds. aliyuncs.com | The endpoint used to connect to the instance. |
| └Port | String | 3306 | The port used to connect to the instance. |
| └Engine | String | MySQL | The engine of the database. |
| └EngineVersion | String | 5.5 | The engine version of the database. |
| └DBInstanceClas sType | String | s | The family of the instance. Valid values: s: shared instance x: general-purpose instance d: dedicated instance h: dedicated host |
| └DBInstanceClas s | String | rds.mys2.small | The type of the instance. |
| └DBInstanceMem ory | Long | 240 | The memory capacity of the instance. Unit: MB. |
| └DBInstanceStor age | Integer | 10 | The storage space of the instance. Unit: GB. |
| └DBInstanceNetT ype | String | Internet | The network connection type of the instance. Valid values: Internet Intranet |
| └DBInstanceStat us | String | Running | The status of the instance. For more information, see Instance states in Appendix. |
| └DBInstanceDesc ription | String | Test instance | The description of the instance. |

| └LockMode | String | Unlock | The lock status of the instance. Valid values: Unlock: normal ManualLock: locked manually LockByExpiration: locked automatically upon expiration LockByRestoration: locked automatically before instance rollback LockByDiskQuota: locked automatically due to full disk space |
|---|---|---|---|
| └LockReason | String | None | The reason why the instance is locked. |
| └DBMaxQuantity | Integer | 200 | The maximum number of databases that can be created for an instance. |
| └AccountMaxQua ntity | Integer | 50 | The maximum number of accounts that can be created for an instance. |
| └CreationTime | String | 2011-05- 30T12:11:4Z | The time when the instance was created. The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ssZ format. Example: 2011-05-30T12:11:4Z . |
| └ExpireTime | String | None | The expiration time of the instance. This parameter is not returned for pay-as-you-go instances. |
| └MaintainTime | String | 00:00Z-02:00Z | The scheduled maintenance window of the instance. For example, 00:00Z-02:00Z indicates that routine maintenance can be performed from 00:00 to 02:00. |
| └AvailabilityValu e | String | 100.0% | The availability status of the instance. Unit: %. |
| └MaxIOPS | Integer | 150 | The maximum number of I/O operations per second (IOPS). |
| └MaxConnection s | Integer | 60 | The maximum number of concurrent connections to the instance. |
| └MasterInstanceI d | String | null | The ID of the primary instance. If this parameter is not returned (null), the instance is a primary instance. |

| └IncrementSourc eDBInstanceId | String | null | The instance ID of the incremental data source. For example, the incremental data source of a disaster recovery instance or read-only instance is the primary instance, and the incremental data source of the primary instance is null. |
|---|---|---|---|
| └GuardDBInstanc eId | String | None | The ID of the disaster recovery instance attached to the instance. |
| └TempDBInstanc eId | String | None | The ID of the temporary instance attached to the instance. |
| └ReadOnlyDBInst anceIds |   | rr-xxxxx | The IDs of the read-only instances attached to the instance. |
| └DBInstanceId | String | rm-bpxxxxx | The ID of the instance. |
| └VpcCloudInstan ceId | String | vpc-xxxxx | The ID of the VPC. |
| └ResourceGroupI d | String | 3653788125 | The ID of the resource group. |
| RequestId | String | 1AD222E9-E606- 4A42-BF6D- 8A4442913CEF | The ID of the request. |

DBInstanceAttribute parameters

**Note**

You can call the DescribeDBInstanceHAConfig operation to query information of the primary and secondary instances.

**Sample requests**

```
https://rds.example.com/?Action=DescribeDBInstanceAttribute &DBInstanceId=rds-xxxxx &<Common request parameters>
```

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

**Sample error responses**

```json
{ "Code":"UnsupportedOperation", "HostId":"rds.aliyuncs.com", "Message":"The specified action is not supported.", "RequestId":"1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC"}
```

#### 1.3.5 DescribeDBInstances

You can call this operation to query instances and RAM-authorized instances.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|

| Action | String | Yes | DescribeDBInsta nces | The operation that you want to perform. Set the valuer to DescribeDBInsta nces. |
|---|---|---|---|---|
| RegionId | String | Yes | cn-hangzhou | The region ID of the instance. |
| ConnectionMode | String | No | Performance | The access mode of the instance. Valid values: Performance: standard access mode Safe: safe access mode If no value is specified, instances in both access modes are returned. |
| DBInstanceType | String | No | Primary | The role of the instance. Valid values: Primary: primary instance Readonly: read-only instance Guard: disaster recovery instance Temp: temporary instance If no value is specified, instance of all roles are returned. |

| InstanceNetwork Type | String | No | Classic | The network type of the instance. Valid values: VPC: VPC instance Classic: classic network instance If no value is specified, instance of both network types are returned. |
|---|---|---|---|---|
| PageNumber | Integer | No | 1 | The number of the page to return. Pages start from page 1 but must be equal to or smaller than the maximum Integer value. Default value: 1. |
| PageSize | Integer | No | 30 | The number of entries to return on each page. Valid values: 30, 50, and 100. Default value: 30. |
| Tags | String | No | {“key1”:”value1” } | The tag of the instance, in the JSON format. The tag includes a key-value pair of TagKey and TagValue. TagValue can be left empty, but TagValue cannot. Example: {“key1”:”value1” }. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| PageNumber | Integer | 1 | The number of the page returned. |
| TotalRecordCount | Integer | 1 | The total number of entries. |
| PageRecordCount | Integer | 1 | The number of instances on the current page. |

| Items |   |   | The array that consists of instance data. |
|---|---|---|---|
| └DBInstanceId | String | rm-xxxxx | The ID of the instance. |
| └DBInstanceDescriptio n | String | testforRemarks | The description of the instance. |
| └PayType | String | Postpaid | The billing method of the instance. Valid values: Postpaid: pay-as- you-go Prepaid: subscription |
| └DBInstanceType | String | Primary | The role of the instance. Valid values: Primary: primary instance ReadOnly: read-only instance Guard: disaster recovery instance Temp: temporary instance |
| └InstanceNetworkType | String | Classic | The network type of the instance. Valid values: Classic: classic network instance VPC: VPC instance |
| └ConnectionMode | String | Performance | The access mode of the instance. Valid values: Performance: standard access mode Safe: safe access mode |
| └RegionId | String | cn-hangzhou | The region ID of the instance. |
| └ExpireTime | String | None | The expiration time of the instance. This parameter is not returned for pay-as- you-go instances. |
| └DBInstanceStatus | String | Intranet | The status of the instance. For more information, see Instance states in Appendix. |

| └Engine | String | MySQL | The type of the database. |
|---|---|---|---|
| └DBInstanceNetType | String | Internet | The network connection type of the instance. Valid values: Internet: public network Intranet: internal network |
| └LockMode | String | Unlock | The lock status of the instance. Valid values: Unlock: normal ManualLock: locked manually LockByExpiration: locked automatically upon expiration LockByRestoration: locked automatically before instance rollback LockByDiskQuota: locked automatically for full disk space |
| └LockReason | String | None | The reason why the instance is locked. |
| └MasterInstanceId | String | null | The ID of the primary instance. If this parameter is not returned (null), the instance is a primary instance. |
| └GuardDBInstanceId | String | None | The ID of the disaster recovery instance attached to the instance. |
| └TempDBInstanceId | String | None | The ID of the temporary instance attached to the instance. |
| └VpcCloudInstanceId | String | vpc-xxxxx | The ID of the VPC instance. |
| └ReadOnlyDBInstanceI ds |   |   | None |
| └DBInstanceId | String | rm-xxxxx | The ID of the instance. |
| RequestId | String | 1AD222E9-E606-4A42- BF6D-8A4442913CEF | The ID of the request. |

**Sample requests**

```xml
https://rds.example.com/?Action=DescribeDBInstances &RegionId=cn-hangzhou &Engine=MySQL &<Common request parameters> <DescribeDBInstancesResponse> <PageRecordCount>2</PageRecordCount> <Items> <DBInstance> <DBInstanceDescription>testforRemarks</DBInstanceDescription> <ExpireTime>2014-10-10T16:00:00Z</ExpireTime> <DBInstanceId>rdsmjfirxxxxx</DBInstanceId> <DBInstanceNetType>Internet</DBInstanceNetType> <PayType>Prepaid</PayType> <DBInstanceStatus>Running</DBInstanceStatus> <DBInstanceType>Primary</DBInstanceType> <Engine>MySQL</Engine> <LockMode>Unlock</LockMode> <LockReason/> <RegionId>cn-hangzhou</RegionId> <ZoneId>cn-hangzhou-a</ZoneId> <MasterInstanceId/> <GuardDBInstanceId/> <TempDBInstanceId/> <ReadOnlyDBInstanceIds> <ReadOnlyDBInstanceId/> </ReadOnlyDBInstanceIds> </DBInstance> </Items> <PageNumber>1</PageNumber> <TotalRecordCount>2</TotalRecordCount> <RequestId>2553A660-E4EB-4AF4-A402-8AFF70A49143</RequestId> </DescribeDBInstancesResponse>
```

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

`}`

**Sample error responses**

```json
{ "Code":"UnsupportedOperation", "HostId":"rds.aliyuncs.com", "Message":"The specified action is not supported.", "RequestId":"7463B73D-35CC-4D19-A010-6B8D65D242EF"}
```

#### 1.3.6 ModifyDBInstanceSpec

You can call this operation to change the type or storage space of an instance. Before you call this operation, make sure that the following requirements are met: The instance is in the running state. The instance is not performing a backup task. One of the instance type (DBInstanceClass) and storage space (DBInstanceStorage) parameters is specified in the request. When you downgrade the disk space configuration, the input disk space is no less than 1.1 times the actually used space. Only primary and read-only instances allow specification changes. Specifications of disaster recovery and temporary instances cannot be changed.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|

| Action | String | Yes | ModifyDBInstanc eSpec | The operation that you want to perform. Set the value to ModifyDBInstanc eSpec. |
|---|---|---|---|---|
| DBInstanceId | String | Yes | rm-bpxxxx | The ID of the instance. |
| AccessKeyId | String | No | LTAIKw8gqxxxxx | The AccessKey ID provided by Alibaba Cloud. |
| ClientToken | String | No | ETnLKlblzczshOT UbOCziJZNwHlYB Q | The client token that is used to ensure the idempotence of the request. |
| DBInstanceClass | String | No | rds.mys2.small | The type of the instance. For more information, see Instance types in Appendix. |
| DBInstanceStora ge | Integer | No | 20 | The user-defined storage space. Unit: GB. This value must be in 5 GB increments. For more information, see the Instance types topic in the User Guide of ApsaraDB for RDS. |
| EffectiveTime | String | No | Immediate | The time when the changes take effect. Valid values: Immediate and MaintainTime. Default value: Immediate. |
| OwnerAccount | String | No | testuser@aliyun. com | The Apsara Stack tenant account. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 1AD222E9-E606-4A42- BF6D-8A4442913CEF | The ID of the request. |

**Sample requests**

```json
https://rds.example.com/?Action=ModifyDBInstanceSpec &DBInstanceId=rds-xxxxx &PayType=Postpaid &DBInstanceStorage=10 &<Common request parameters> <ModifyDBInstanceSpecResponse> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> </ModifyDBInstanceSpecResponse> { "RequestId": "1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC" }
```

**Sample error responses**

```json
{ "Code":"UnsupportedOperation", "HostId":"rds.aliyuncs.com", "Message":"The specified action is not supported.", "RequestId":"7463B73D-35CC-4D19-A010-6B8D65D242EF"}
```

#### 1.3.7 AllocateInstancePublicConnection

You can call this operation to apply for a public endpoint for a specified instance.

| Parameter | Typ e | Requir ed | Description |
|---|---|---|---|
| Action | Strin g | Yes | The operation that you want to perform. Set the value to AllocateInstancePublicConnection. |
| DBInstanceId | Strin g | Yes | The ID of the instance for which the public endpoint is applied. |
| ConnectionString Prefix | Strin g | Yes | The endpoint to be used by the instance. |
| Port | Strin g | Yes | The external port to be used by the instance. |

| Parameter | Type | Description |
|---|---|---|

| <Common response parameters> | - | For more information, see Common response parameters. |
|---|---|---|

**Sample requests**

```
https://rds.example.com/?Action=AllocateInstancePublicConnection &DBInstanceId=rds-xxxxx &ConnectionStringPrefix=test0001 &Port=3306 &<Common request parameters>
```

**Sample responses**

```json
<AllocateInstancePublicConnectionResponse> <RequestId>65BDA532-28AF-4122-AA39-B382721EEE64</RequestId> </AllocateInstancePublicConnectionResponse> { "RequestId": "65BDA532-28AF-4122-AA39-B382721EEE64"}
```

#### 1.3.8 ReleaseInstancePublicConnection

You can call this operation to release the public endpoint of an instance.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to ReleaseInstancePublicConnection. |
| DBInstanceId | String | Yes | The ID of the instance whose public endpoint is released. |
| CurrentConnection String | String | Yes | The public endpoint. |

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> | - | For more information, see Common response parameters. |

**Sample requests**

```
https://rds.example.com/?Action=ReleaseInstancePublicConnection &DBInstanceId=rds-xxxxx &CurrentConnectionString=test0001.mysql.rds.example.com &<Common request parameters>
```

**Sample responses**

```json
<ReleaseInstancePublicConnectionResponse> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> </ReleaseInstancePublicConnectionResponse> { "RequestId": "1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC" }
```

#### 1.3.9 SwitchDBInstanceNetType

You can call this operation to switch the network type of an instance between internal and public networks. After switching, the endpoint of the instance changes. You must modify the endpoint in the code and restart the application. Before you call this operation, make sure that the following requirements are met: The instance is in the running state. The number of times that you have switched the instance between its internal and public endpoints within the last 24 hours does not reach 20.

| Parameter | Type | Require d | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to SwitchDBInstanceNetType. |
| DBInstanceId | String | Yes | The instance ID. |
| ConnectionString Prefix | String | Yes | The unique endpoint to be used. It can be up to 30 characters in length and can contain lowercase letters, digits, and hyphens (-). It must start with a letter. |

For more information, see Common response parameters.

#### 1.3.10 DescribeDBInstanceNetInfo

You can call this operation to query the connection information of a specified instance.

| Parameter | Type | Requir ed | Description |
|---|---|---|---|
| Action | Strin g | Yes | The operation that you want to perform. Set the value to DescribeDBInstanceNetInfo. |
| DBInstanceI d | Strin g | Yes | The ID of the instance whose connection information is queried. |

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

#### 1.3.11 ModifyDBInstanceConnectionString

You can call this operation to modify the endpoint and port of a connection string. RDS provides the internal and public endpoints and allows both types to coexist in a specific access mode.

| > Document Version: | 20260 | 630 | 3 |
|---|---|---|---|

| Parameter | Ty pe | Requi red | Description |
|---|---|---|---|
| Action | Str ing | Yes | The operation that you want to perform. Set the value to ModifyDBInstanceConnectionString. |
| DBInstanceId | Str ing | Yes | The ID of the instance whose connection string is modified. |
| CurrentConnection String | Str ing | Yes | The endpoint used by the instance. |
| ConnectionStringP refix | Str ing | No | The endpoint to be used by the instance. |
| Port | Str ing | No | The port to be used by the instance. |

This operation returns only common response parameters. For more information, see Common response parameters.

#### 1.3.12 ModifyDBInstanceConnectionMode

You can call this operation to modify the access mode of RDS instances. Two access modes are available for RDS: Standard access mode Safe access mode

| Parameter | Typ e | Require d | Description |
|---|---|---|---|
| Action | Stri ng | Yes | The operation that you want to perform. Set the value to ModifyDBInstanceConnectionMode. |
| DBInstance Id | Stri ng | Yes | The ID of the instance for which the access mode is modified. |
| Connection Mode | Stri ng | Yes | The access mode of the instance. Performance: standard access mode. Safe: safe access mode. |

This operation returns only common response parameters. For more information, see Common response parameters.

#### 1.3.13 ModifyDBInstanceNetworkType

You can call this operation to switch the network type of an RDS instance between VPC and classic network.

**Note**

Only the classic network instances with the ConnectionMode set to Safe can have their network type switched to VPC.

| Parameter | T y p e | Requi red | Description |
|---|---|---|---|
| Action | St ri n g | Yes | The operation that you want to perform. Set the value to ModifyDBInstanceNetworkType. |
| DBInstanceId | St ri n g | Yes | The ID of the instance for which the network type is modified. |
| InstanceNetwor kType | St ri n g | Yes | The network type of the instance. VPC: VPC instance. Classic: classic network instance. |
| VPCId | St ri n g | No | The ID of the VPC. |
| VSwitchId | St ri n g | No | The ID of the VSwitch. This parameter is required if the value of VPCId is specified. |
| PrivateIpAddres s | St ri n g | No | The VPC IP address that belongs to the specified VSwitch. If no value is specified, the system automatically assigns a VPC IP address based on VPCId and VSwitchId. |

This operation returns only common response parameters. For more information, see Common response parameters.

#### 1.3.14 DescribeDBInstanceIPArrayList

You can call this operation to query the IP whitelist of an instance.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeDBInstanceIPArrayList. |

| DBInstanceI d | String | Yes | The ID of the instance whose IP whitelist is queried. |
|---|---|---|---|

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> |   | Common response parameters. |
| Items | List<DBInstanceIP Array> | The array that consists of DBInstanceIPArray data. |

DBInstanceIPArray parameters

| Parameter | Type | Description |
|---|---|---|
| DBInstanceIPArrayN ame | Strin g | The name of the IP whitelist. |
| DBInstanceIPArrayAt tribute | Strin g | The attribute of the IP whitelist. Default value: null. Whitelists tagged with "hidden" are not displayed in the console. |
| SecurityIPList | Strin g | The IP addresses in an IP address whitelist. Separate multiple IP addresses with commas (,). You can add a maximum of 1,000 different IP addresses to a whitelist. Supported formats of IP addresses are IP addresses such as 0.0.0.0/0 and 10.23.12.24, or Classless Inter-Domain Routing (CIDR) blocks such as 10.23.12.24/24. /24 indicates the length of the IP address prefix. The IP address prefix can consist of 1 to 32 bits. |

#### 1.3.15 ModifySecurityIps

You can call this operation to modify the IP whitelist of an instance. Before you call this operation, ensure that the following requirements are met: The instance is in the running state. The instance is not locked by the system.

| Parameter | Ty pe | Requ ired | Description |
|---|---|---|---|
| Action | Stri ng | Yes | The operation that you want to perform. Set the value to ModifySecurityIps. |
| DBInstanceId | Stri ng | Yes | The ID of the instance whose IP whitelist is modified. |

| SecurityIps | Stri ng | No | The IP addresses in an IP address whitelist. Separate multiple IP addresses with commas (,). You can add a maximum of 1,000 different IP addresses to a whitelist. Supported formats of IP addresses are IP addresses such as 0.0.0.0/0 and 10.23.12.24, or Classless Inter-Domain Routing (CIDR) blocks such as 10.23.12.24/24. /24 indicates the length of the IP address prefix. The IP address prefix can consist of 1 to 32 bits. |
|---|---|---|---|
| DBInstanceIPArrayNa me | Stri ng | No | The name of the IP whitelist. If no value is specified, the whitelist named Default will be modified. |
| DBInstanceIPArrayAtt ribute | Stri ng | No | The attribute of the IP whitelist. Default value: null. Whitelists tagged with "hidden" are not displayed in the console. |

This operation returns only common response parameters. For more information, see Common response parameters.

**Sample requests**

```
https://rds.example.com/?Action=ModifySecurityIps &DBInstanceId=rds-xxxxx &SecurityIps=192.168.1.2 &<Common request parameters>
```

**Sample responses**

```json
<ModifySecurityIpsResponse> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> </ModifySecurityIpsResponse> { "RequestId": "1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC"}
```

#### 1.3.16 DescribeRegions

You can call this operation to query the available RDS regions and zones. Before you call the CreateInstance operation, call this operation to query region IDs.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeRegions. |

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> | - | Common response parameters. |
| Regions | List<RDSRegion> | The array that consists of RDSRegion data. |

RDSRegion parameters

| Parameter | Type | Description |
|---|---|---|
| RegionId | String | The region ID. |
| ZoneId | String | The zone ID. |

**Sample requests**

```
https://rds.example.com/?Action=DescribeRegions &<Common request parameters>
```

**Sample responses**

```json
<DescribeRegionsResponse> <Regions> <RDSRegion> <RegionId>cn-hangzhou</RegionId> <ZoneId>cn-hangzhou-a</RegionId> </RDSRegion> <RDSRegion> <RegionId>cn-hangzhou</RegionId ><ZoneId>cn-hangzhou-b</ZoneId> </RDSRegion> </Regions> <RequestId>A36D9720-7902-42A4-B8B9-014A2135E6C3</RequestId> </DescribeRegionsResponse> { "Regions":
    { "RDSRegion":
        [ {"RegionId": "cn-hangzhou",
            "ZoneId":"cn-hangzhou-a"},
          {"RegionId": "cn-hangzhou",
            "ZoneId":"cn-hangzhou-b"},
             ]},
    "RequestId": "1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC"
```

`}`

#### 1.3.17 DescribeDBInstanceHAConfig

You can call this operation to query the zone information and data replication status of instances.

| Parameter | Type | Require d | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeDBInstanceHAConfig. |
| DBInstanceI d | String | Yes | The ID of the instance. |

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
|---|---|---|

#### 1.3.18 MigrateToOtherZone

You can call this operation to migrate an instance from one zone to another. For example, if instance 1 is located in the Hangzhou Zone A zone of the China (Hangzhou) region, you can call this operation to migrate the instance to the Hangzhou Zone B zone of the China (Hangzhou) region.

**Note**

In cross-zone migration, instances must be migrated within the same region. For example, instances in a zone of the China (Hangzhou) region cannot be migrated to a zone of the China (Qingdao) region.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to MigrateToOtherZone. |
| DBInstanceId | String | Yes | The ID of the instance to be migrated. |
| ZoneId | String | Yes | The zone ID of the instance. You can call the DescribeRegions operation to query available zones. |

This operation returns only common response parameters. For more information, see Common response parameters.

**Sample requests**

```
https://rds.example.com/?Action=MigrateToOtherZone &DBInstanceId=rds-xxxxx &ZoneId=cn-hangzhou-b &<Common request parameters>
```

**Sample responses**

```json
<MigrateToOtherZoneResponse> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> </MigrateToOtherZoneResponse> { "RequestId": "1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC"}
```

#### 1.3.19 PurgeDBInstanceLog

You can call this operation to clear all binlogs for a MySQL instance.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to PurgeDBInstanceLog. |
| DBInstanceId | String | Yes | The ID of the instance for which all binlogs are cleared. |

This operation returns only common response parameters. For more information, see Common response parameters.

**Sample requests**

```json
https://rds.example.com/?Action=PurgeDBInstanceLog &DBInstanceId=rds-xxxxx &<Common request parameters> <PurgeDBInstanceLogResponse> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> </PurgeDBInstanceLogResponse> { "RequestId": "1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC"}
```

#### 1.3.20 UpgradeDBInstanceEngineVersion

You can call this operation to upgrade the database version of an instance. For example, you can upgrade the database version from MySQL 5.1 to MySQL 5.5. If a read-only or disaster recovery instance is attached to the primary instance, you must first upgrade the database version of the attached instance. Before you call this operation, ensure that the following requirements are met: The instance is in the running state. The specified database version must be later than the current database version of the target instance.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to UpgradeDBInstanceEn gineVersion. |
| DBInstanceId | String | Yes | The instance to be upgraded. |
| EngineVersion | String | Yes | The database version to be upgraded to. |

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> |   | For more information, see Common response parameters. |
| TaskId | Integer | The ID of the task. |

```json
https://rds.example.com/?Action=UpgradeDBInstanceEngineVersion &DBInstanceId=rds-xxxxx &EngineVersion=5.6 &<Common request parameters> <UpgradeDBInstanceEngineVersionResponse> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> <TaskId>124378</Taskid> </UpgradeDBInstanceEngineVersionResponse> {"RequestId": "1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC", "TaskId":”124378” }
```

#### 1.3.21 ModifyDBInstanceDescription

You can call this operation to modify the description of an instance to identify the instance easily. For example, you can modify the description of an instance to Alibaba Cloud testing environment instance.

| Parameter | Typ e | Requir ed | Description |
|---|---|---|---|
| Action | Strin g | Yes | The operation that you want to perform. Set the value to ModifyDBInstanceDescription. |
| DBInstanceId | Strin g | Yes | The ID of the instance whose description is modified. |
| DBInstanceDesc ription | Stin g | Yes | The description of the instance. |

This operation returns only common response parameters.

**Sample requests**

```
https://rds.example.com/?Action=ModifyDBInstanceDescription &DBInstanceId=rds-xxxxx &DBInstanceDescription=testdescribe &<Common request parameters>
```

**Sample responses**

```json
<ModifyDBInstanceDescriptionResponse> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> </ModifyDBInstanceDescriptionResponse> { "RequestId": "1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC"}
```

#### 1.3.22 ModifyDBInstanceMaintainTime

You can call this operation to modify the scheduled period for routine maintenance. You can set the maintenance window to an off-peak period. Alibaba Cloud performs routine maintenance during the maintenance window to minimize the impact on your services.

| Parameter | Type | Requir ed | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to ModifyDBInstanceMaintainTime. |
| DBInstanceI d | String | Yes | The ID of the instance whose maintenance window is modified. |

| MaintainTim e | String | Yes | The maintenance window of the instance. Valid values: 22:00Z-02:00Z 02:00Z-06:00Z 06:00Z-10:00Z 10:00Z-14:00Z 14:00Z-18:00Z 18:00Z-22:00Z |
|---|---|---|---|

This operation returns only common response parameters. For more information, see Common response parameters.

**Sample requests**

```
https://rds.example.com/?Action=ModifyDBInstanceMaintainTime &DBInstanceId=rds-xxxxx &MaintainTime=22:00Z-02:00Z &<Common request parameters>
```

**Sample responses**

```json
<ModifyDBInstanceMaintainTimeResponse> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> </ModifyDBInstanceMaintainTimeResponse> { "RequestId": "1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC" }
```

#### 1.3.23 ModifyDBInstanceHAConfig

You can call this operation to modify the instance data replication mode and high availability switching rules.

| Parameter | Type | Requir ed | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to ModifyDBInstanceHAConfig. |
| DBInstance Id | String | Yes | The ID of the instance. |

| SyncMode | String | Yes | The synchronization mode of the instance. Valid values: Semi- sync and Async. |
|---|---|---|---|
| HAMode | String | Yes | The HA mode of the instance. RPO: Data persistence is preferred. RTO: Instance availability is preferred. |

This operation returns only common response parameters.

#### 1.3.24 SwitchDBInstanceHA

You can call this operation to change the database used as the primary database. RDS instances are composed of primary and secondary databases distributed across different servers. The new primary database bears the service traffic.

| Paramete r | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to SwitchDBInstanceHA. |
| DBInstanc eId | String | Yes | The ID of the primary instance. |
| NodeId | String | Yes | The unique ID of the node. You can call the DescribeDBInstanceHAConfig operation to query the value of this parameter. |
| Force | String | Yes | Yes: forced. No: unforced. Default value: No. |

This operation returns only common response parameters. For more information, see Common response parameters.

#### 1.3.25 CreateReadOnlyDBInstance

You can call this operation to create a read-only instance for a primary RDS instance. Before you call this operation, make sure that the following requirements are met: The primary instance is in the running state, but not in the failover state. The read-only instance and the primary instance are in the same region. A primary RDS instance can have up to five read-only instances.

| Parameter | Type | Requi red | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to CreateReadOnlyDBInstance. |
| RegionId | String | Yes | The region ID of the instance. It can be up to 50 characters in length. You can call the DescribeRegions operation to query the most recent region list. |
| ZoneId | String | Yes | The zone ID of the instance. You can call the DescribeRegions operation to query the most recent zone list. |
| DBInstanceId | String | Yes | The ID of the primary instance. |
| EngineVersion | String | Yes | The engine version of the database. The read-only instance must run the same database engine version as the primary instance. Valid values: 5.6 5.7 |
| DBInstanceClass | String | Yes | The type of the instance. For more information, see |
| DBInstanceStora ge | Intege r | Yes | The user-defined storage space. Valid values: 5 to 1000. This value must be in 5 GB increments. Unit: GB. |
| DBInstanceDesc ription | String | No | The description of the instance. It can be up to 256 bytes in length and can contain letters, underscores ( ), and hyphens _ (-). The digits must be 2 to 256 characters in length. The description must start with a letter and cannot start with http:// or https://. |
| ClientToken | String | Yes | The client token that is used to ensure the idempotence of the request. |
| InstanceNetwork Type | String | No | The network type of the instance. Valid values: VPC and Classic. Default value: Classic. |
| VPCId | String | No | The ID of the VPC. |
| VSwitchId | String | No | The ID of the VSwitch. |
| PrivateIpAddress | String | No | The IP address of the VPC that belongs to VSwitchId. If no value is specified, the system automatically allocates a VPC IP address based on VPCId and VSwitchId. |

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> | - | For more information, see Common response parameters. |
| DBInstanceId | String | The ID of the instance. |
| OrderId | String | The ID of the order. |

| ConnectionStrin g | String | The endpoint used to connect to the database. |
|---|---|---|
| Port | String | The port used to connect to the database. |

**Sample requests**

```json
https://rds.example.com/?Action=CreateReadOnlyDBInstance &RegionId=cn-hangzhou &ZoneId=cn-hangzhou-b &DBInstanceId=rds-xxxxx &EngineVersion=5.6 &DBInstanceClass=rds.mys2.small &DBInstanceStorage=10 &PayType=Postpaid &ClientToken=ETnLKxxxxx &<[Common request parameters]> <CreateDBInstanceResponse> <OrderId>10078937xxxxx</OrderId> <ConnectionString>rds-xxxxx.mysql.rds.aliyuncs.com </ConnectionString> <DBInstanceId>rds-xxxxx</DBInstanceId> <port>3306</port> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> </CreateDBInstanceResponse> { "OrderId": "100789370230206", "ConnectionString": "rds-xxxxx.mysql.rds.aliyuncs.com", "DBInstanceId": "rds-xxxxx", "Port": "3306", "RequestId": "1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC" }
```

#### 1.3.26 DescribeDBInstanceSSL

You can call this operation to query the SSL link of an instance.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeDBInstanceSSL. |
| DBInstanceId | String | Yes | The ID of the instance. |

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> | - | For more information, see Common response parameters. |
| ConnectionString | String | The endpoint protected by the SSL certificate. |
| SSLExpireTime | String | The expiration time of the SSL certificate. The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ssZ format. |
| RequireUpdate | String | Indicates whether an immediate update is required. Valid values: Yes and No. |
| RequireUpdateRe ason | String | The reason why an update is recommended. |

#### 1.3.27 ModifyDBInstanceSSL

You can call this operation to modify the SSL link of an instance.

| Parameter | Typ e | Req uire d | Description |
|---|---|---|---|
| Action | Strin g | Yes | The operation that you want to perform. Set the value to ModifyDBInstanceSSL. |
| DBInstance Id | Strin g | Yes | The ID of the instance. |
| Connection String | Strin g | Yes | Each instance can only have one endpoint protected by the SSL certificate. The SSL certificate can be created or updated for the endpoint. |

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> | - | Common response parameters. |
| SSLExpireTime | String | The expiration time of the SSL certificate. The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ssZ format. |

#### 1.3.28 DescribeDBInstanceTDE

You can call this operation to query the TDE status of an instance.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeDBInstanceTDE. |
| DBInstanceId | String | Yes | The ID of the instance. |

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

#### 1.3.29 ModifyDBInstanceTDE

You can call this operation to modify the TDE status of an instance.

| Parameter | Type | Requi red | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to ModifyDBInstanceTDE. |
| DBInstanceId | String | Yes | The ID of the instance. |
| TDEStatus | String | Yes | The TDE status of the instance. Valid values: Enabled and Disabled. |
| DBName | String | No | The name of the database. Up to 50 names can be entered in a single request. Separate multiple names with commas (,). |

This operation returns only common response parameters. For more information, see Common response parameters.

### 1.4 Database management

#### 1.4.1 CreateDatabase

You can call this operation to create a new database in an instance. Before you call this operation, make sure that the following requirements are met: The instance is in the running state. The instance is not locked. The maximum number of databases in the instance is not reached. The instance is a primary instance.

**Note**

This operation is not supported on PolarDB. You can create databases in PolarDB instances by executing CREATE DATABASE statements.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to CreateDatabase. |
| DBInstanceI d | String | Yes | The ID of the instance. |
| DBName | String | Yes | The unique name of the database. The name can be up to 64 characters in length and can contain lowercase letters, digits, and underscores ( ). It must start with a letter. _ For information about invalid characters, see Forbidden keywords. |
| CharacterSet Name | String | Yes | The character set. Valid values: MySQL: utf8, gbk, latin1, and utf8mb4 SQL Server: Chinese PRC CI AS, Chinese PRC CS AS, _ _ _ _ _ _ SQL Latin1 General CP1 CI AS, _ _ _ _ _ SQL Latin1 General CP1 CS AS, and Chinese PRC BIN _ _ _ _ _ _ _ |
| DBDescriptio n | String | No | The description of the database. It must be 2 to 256 characters in length and can contain letters, digits, underscores ( ), and hyphens (-). _ It must start with a letter and cannot start with http:// or https://. |

This operation returns only common response parameters.

**Sample requests**

```json
https://rds.example.com/?Action=CreateDatabase &CharacterSetName=gbk &DBName=testDB &DBInstanceId=rds-xxxxx &<[Common request parameters]> <CreateDatabaseResponse> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> </CreateDatabaseResponse> { "RequestID":"1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC" }
```

#### 1.4.2 DeleteDatabase

You can call this operation to delete a database from an instance. Before you call this operation, make sure that the following requirements are met: The instance is in the running state. The instance is a primary instance.

**Note**

This operation is not supported on PolarDB. You can delete databases from PolarDB instances by executing DROP DATABASE statements.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DeleteDatabase. |
| DBInstance Id | String | Yes | The ID of the instance. |
| DBName | String | Yes | The name of the database. |

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> | - | Common response parameters. |

**Sample requests**

```json
https://rds.example.com/?Action=DeleteDatabase &DBName=testDB &DBInstanceId=rds-xxxxx &<[Common request parameters]> <DeleteDatabaseResponse> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> </DeleteDatabaseResponse> { "RequestId":"1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC" }
```

#### 1.4.3 DescribeDatabases

You can call this operation to query the databases of a specified instance or information of a specified database. If the request parameters are entered incorrectly, an error prompt is returned, and the returned data is empty.

**Note**

This operation is not supported on PolarDB.

| Parame ter | Type | Requ ired | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeDatabases. |
| DBInstan ceId | String | Yes | The ID of the instance. |
| DBName | String | No | The name of the database. |
| DBStatu s | String | No | The state of the database. Valid values: Creating, Running, and Deleting. |

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
| DBStatus | String | The status of the database. Valid values: Creating, Running, and Deleting. |
| CharacterSet Name | String | The character set. |
| DBDescription | String | The description of the database. |
| Accounts | List<AccountPrivileg eInfo> | The array that consists of AccountPrivilegeInfo data. |
| Account | String | The name of the account. |
| AccountPrivile ge | String | The permissions of the account on the database. |

AccountPrivilegeInfo parameters

| Parameter | Type | Description |
|---|---|---|
| Account | String | The name of the account. |
| AccountPrivilege | String | The permissions of the account on the database. |

**Sample requests**

```
https://rds.example.com/?Action=DescribeDatabases &DBInstanceId=rds-xxxxx &<Common request parameters>
```

```json
<DescribeDatabasesResponse> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> <Databases> <Database> <Engine>MySQL</Engine> <DBName>testdb</DBName> <CharacterSetName>utf8</CharacterSetName> <DBStatus>Creating</DBStatus> <DBInstanceId>rds-xxxxx</DBInstanceId> <Accounts> <AccountPrivilegeInfo></AccountPrivilegeInfo> <Accounts> </Database> </Databases> </DescribeDatabasesResponse> { "RequestId": "1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC", "Databases":
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

#### 1.4.4 ModifyDBDescription

You can call this operation to modify the description of a database to facilitate user records. For example, you can modify the description of a database to Database A for Alibaba Cloud testing environment.

**Note**

This operation is not supported on PolarDB.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to ModifyDBDescription. |
| DBInstanceId | String | Yes | The ID of the instance. |
| DBName | String | Yes | The name of the database. |
| DBDescription | String | Yes | The description of the database. |

This operation returns only common response parameters.

**Sample requests**

```json
https://rds.example.com/?Action=ModifyDBDescription &DBInstanceId=rds-xxxxx &DBInstanceDescription=testDBdescribe &<Common request parameters> <ModifyDBDescriptionResponse> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> </ModifyDBDescriptionResponse> { "RequestId": "1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC" }
```

### 1.5 Account management

#### 1.5.1 CreateAccount

In the same instance, one account can manage multiple databases by using different permissions. You can call this operation to create an account for a database. Before you call this operation, make sure that the following requirements are met: The instance is in the running state. The database is in the running state. The instance is not locked. The maximum number of accounts for a single instance is not reached.

| Parameter | Type | Req uire d | Description |
|---|---|---|---|
| Action | Strin g | Yes | The operation that you want to perform. Set the value to CreateAccount. |
| DBInstanceId | Strin g | Yes | The ID of the instance. |

| AccountName | Strin g | Yes | The unique name of the account. The name can be up to 16 characters in length and can contain lowercase letters, digits, and underscores ( ). It must start with a letter. For information about _ invalid characters, see Forbidden keywords. |
|---|---|---|---|
| AccountPassw ord | Strin g | Yes | The password for the account. It must be 6 to 32 characters in length and can contain letters, digits, and underscores ( ). _ |
| AccountType | Strin g | No | The type of the account. Valid values: Normal and Super. Default value: Normal. PolarDB can have only a single initial account. You must use the initial account to log on to the database and create other types of accounts. |
| AccountDescr iption | Strin g | No | The description of the account. It must be 2 to 256 characters in length and can contain letters, digits, underscores ( ), and _ hyphens (-). It must start with a letter and cannot start with http:// or https://. |

This operation returns only common response parameters.

**Sample requests**

```json
https://rds.example.com/?Action=CreateAccount &AccountName=testacc02 &AccountPassword=pwxxxxx &DBInstanceId=rds-xxxxx &<[Common request parameters]> <CreateAccountResponse> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> </CreateAccountResponse> { "RequestId":"1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC" }
```

#### 1.5.2 DeleteAccount

You can call this operation to delete a database account. The instance must be in the running state.

| Parameter | Type | Require d | Description |
|---|---|---|---|

| Action | String | Yes | The operation that you want to perform. Set the value to DeleteAccount. |
|---|---|---|---|
| DBInstanceI d | String | Yes | The ID of the instance to which the database belongs. |
| AccountNam e | String | Yes | The unique name of the account. The name can be up to 16 characters in length and can contain lowercase letters, digits, and underscores ( ). It must start with a letter. For _ more information about invalid characters, see Forbidden keywords. |

This operation returns only common response parameters.

**Sample requests**

```
https://rds.example.com/?Action=DeleteAccount &DBInstanceId=rds-xxxxx &AccountName=testacc01 &<[Common request parameters]>
```

**Sample responses**

```json
<DeleteAccountResponse> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> </DeleteAccountResponse> { "RequestID":"1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC" }
```

#### 1.5.3 DescribeAccounts

You can call this operation to query the account list information for a specified instance and database and the information of its associated accounts.

| Parameter | Typ e | Required | Description |
|---|---|---|---|
| Action | Stri ng | Yes | The operation that you want to perform. Set the value to DescribeAccounts. |
| DBInstance Id | Stri ng | Yes | The ID of the instance to which the database belongs. |
| AccountNa me | Stri ng | Yes | The name of the account. |

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> |   | For more information, see Common response parameters. |
| Accounts | List<DBInstanceAccount > | The array that consists of DBInstanceAccount data. |

DBInstanceAccount parameters

| Parameter | Type | Description |
|---|---|---|
| DBInstanceId | String | The ID of the instance to which the account belongs. |
| AccountName | String | The name of the database account. |
| AccountStatus | String | The account status. Valid values: Unavailable and Available. |
| AccountDescription | String | The description of the account. |
| DatabasePrivileges | List<DatabasePrivil ege> | The array that consists of DatabasePrivileges data. |
| AccountType | String | The type of the account. Valid values: Normal and Super. |

DatabasePrivilege parameters

| Parameter | Type | Description |
|---|---|---|
| DBName | String | The name of the database. |
| AccountPrivilege | String | The name of the database account. |

**Sample requests**

```
https://rds.example.com/?Action=DescribeAccounts &DBInstanceId=rds-xxxxx &<Common request parameters>
```

**Sample responses**

```json
<DescribeAccountsResponse> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> <Accounts> <DBInstanceAccount> <AccountName>MySQL</AccountName> <DBInstanceId>testdb</DBInstanceId> <AccountStatus>utf8</AccountStatus> <AccountDescription> </AccountDescription> <DatabasePrivileges> <DatabasePrivilege></DatabasePrivilege> </DatabasePrivileges> <DBInstanceAccount> </Accounts> </DescribeAccountsResponse> { "Accounts":
    { "DBInstanceAccount":
        [ { "AccountDescription": "",
            "DBInstanceId": "rds-xxxxx",
            "DatabasePrivileges": { "DatabasePrivilege": [] },
            "AccountStatus": "Unavailable",
            "AccountName": "testaccount" } ] },
    "RequestId": "1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC" }
```

#### 1.5.4 GrantAccountPrivilege

You can call this operation to grant database access permissions to accounts. A single account can be associated with one or more databases. If the specified account already has access permissions on the specified database, the operation directly returns a successful response. The instance must be in the running state.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to GrantAccountPrivilege. |
| DBInstanceId | String | Yes | The ID of the instance to which the database belongs. |
| AccountName | String | Yes | The name of the account. |
| DBName | String | Yes | The name of the database associated with the account. |
| AccountPrivileg e | String | Yes | The permissions of the account. Valid values: ReadOnly and ReadWrite. |

This operation returns only common response parameters. For more information, see Common response parameters.

**Sample requests**

```
https://rds.example.com/?Action=GrantAccountPrivilege &AccountName=testacc02 &AccountPrivilege=readwrite &DBName=testdb03 &DBInstanceId=rds-xxxxx &<Common request parameters>
```

**Sample responses**

```json
<GrantAccountPrivilegeResponse> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> </GrantAccountPrivilegeResponse> { "RequestId":"1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC"}
```

#### 1.5.5 RevokeAccountPrivilege

You can call this operation to revoke database access permissions from an account. Before you call this operation, ensure that the following requirements are met: The instance is in the running state. The database is in the running state.

| Paramete r | Type | Requi red | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to RevokeAccountPrivilege. |
| DBInstance Id | String | Yes | The ID of the instance to which the database belongs. |
| AccountNa me | String | Yes | The name of the account. |
| DBName | String | Yes | The name of the database. |

This operation returns only common response parameters. For more information, see Common response parameters.

**Sample requests**

```
https://rds.example.com/?Action=RevokeAccountPrivilege &AccountName=testacc02 &DBName=testdb03 &DBInstanceId=rds-xxxxx &<Common request parameters>
```

**Sample responses**

```json
<RevokeAccountPrivilegeResponse> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> </RevokeAccountPrivilegeResponse> { "RequestId":"1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC"}
```

#### 1.5.6 ModifyAccountDescription

You can call this operation to modify the description of an account to facilitate user records. For example, you can modify the description of an account to Account A for Alibaba Cloud testing environment.

| Parameter | Typ e | Require d | Description |
|---|---|---|---|
| Action | Stri ng | Yes | The operation that you want to perform. Set the value to ModifyAccountDescription. |
| DBInstanceId | Stri ng | Yes | The ID of the instance for which the account description is modified. |
| AccountName | Stri ng | Yes | The unique name of the account. The name can be up to 16 characters in length and can contain lowercase letters, digits, and underscores ( ). It must start with a letter. For more _ information about invalid characters, see Forbidden keywords. |
| AccountDescr iption | Stri ng | Yes | The description of the account. It can be up to 256 characters in length and can contain letters, digits, underscores ( ), and _ hyphens (-). It cannot start with http:// or https://. It must start with a letter. |

| Parameter | Type | Description |
|---|---|---|

| <Common response parameters> | - | Common response parameters. |
|---|---|---|

**Sample requests**

```
https://rds.example.com/?Action=ModifyAccountDescription &DBInstanceId=rds-xxxxx &AccountName=testacc01 &AccountDescription=testAccoutdescribe &<Common request parameters>
```

**Sample responses**

```json
<ModifyAccountDescription> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> </ModifyAccountDescription> { "RequestId": "1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC"}
```

#### 1.5.7 ResetAccountPassword

You can call this operation to reset the account password. Before you call this operation, ensure that the following requirements are met: The instance is in the running state and not locked by the system.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | Strin g | Yes | The operation that you want to perform. Set the value to ResetAccountPassword. |
| DBInstanceId | Strin g | Yes | The ID of the instance for which the account password is reset. |
| AccountNam e | Strin g | Yes | The name of the account. |
| AccountPass word | Strin g | Yes | The new password. It must be 6 to 32 characters in length and can contain letters, digits, and underscores ( ). _ |

This operation returns only common response parameters. For more information, see Common response parameters.

**Sample requests**

```
https://rds.example.com/?Action=ResetAccountPassword &AccountName=testacc02 &AccountPassword=pwxxxxx &DBInstanceId=rds-xxxxx &<Common request parameters>
```

**Sample responses**

```json
<ResetAccountPasswordResponse> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> </ResetAccountPasswordResponse> { "RequestId":"1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC"}
```

#### 1.5.8 ResetAccount

You can call this operation to reset the initial account of an instance.

| Parameter | Type | Requi red | Description |
|---|---|---|---|
| Action | Strin g | Yes | The operation that you want to perform. Set the value to ResetAccount. |
| DBInstanceI d | Strin g | Yes | The instance ID. |
| AccountNam e | Strin g | Yes | The account username. |
| AccountPass word | Strin g | Yes | The password. |

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> | - | For more information, see Common response parameters. |

### 1.6 Backup and restoration

#### 1.6.1 CreateBackup

You can call this operation to manually create a backup. Up to 10 backups can be created for an instance in a single day. Before you call this operation, ensure that the following requirements are met: The instance is in the running state. The most recent backup has been completed.

| Paramet er | Type | Req uire d | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to CreateBackup. |
| DBInstanc eId | String | Yes | The ID of the instance. |
| BackupMe thod | String | No | The backup method. Valid values: Logical and Physical. Default value: Physical. Logical backup cannot be used for instances without databases. SQL Server instances only support physical backup. |
| BackupStr ategy | String | No | The logical backup range. Valid values: db: single-database backup. instance: instance backup. This parameter is valid only when BackupMethod is set to Logical. |
| DBName | String | No | The name of the database for logical single-database backup. This parameter is valid only when BackupMethod is set to Logical and BackupStrategy is set to db. |
| BackupTy pe | String | No | The backup type. Valid values: Auto: specifies whether it is a full backup or an incremental backup through automatic calculation. FullBackup: specifies a full backup. Default value: Auto. |

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> | N/A | Common response parameters. |

**Sample requests**

```
https://rds.example.com/?Action= CreateBackup &DBInstanceId=rds-xxxxx &<Common request parameters>
```

```json
<CreateBackupResponse> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> </CreateBackupResponse> { "RequestId":"1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC"}
```

#### 1.6.2 CloneDBInstance

You can call this operation to clone a new instance with historical data based on the backup file of an existing instance or a specified time. The new instance will have the same whitelist, SQL audit, alert threshold, backup, and parameter settings as the existing instance. The data in the new instance is the same as historical data in the backup file. The clone feature can only be used with MySQL engines. Database account information is cloned differently for different account types: If the primary instance has a privileged account, instances that are cloned from it will also carry the same privileged account information. If the primary instance has only standard accounts, instances that are cloned from it will also carry the information of the account used when the backup file is generated or at the specified time.

| Parameter | Type | Requir ed | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to CloneDBInstance. |
| DBInstanceId | String | Yes | The ID of the instance. |
| BackupId | String | No | The ID of the backup set. You can call the DescribeBackups operation to query backup set IDs. |
| RestoreTime | String | No | A point in time within the backup retention period to obtain a backup set from. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. Example: 2011-06- 11T16:00:00Z. Either BackupId or RestoreTime is required. |
| DBInstanceClas s | String | No | Optional. The type of the instance. For more information, see Instance types in Appendix. If it is not specified, the new instance is of the same type as the primary instance. |
| DBInstanceStor age | String | No | The disk space. Unit: GB. This value must be in 5 GB increments and is the same as that of the primary instance by default. Valid values: RDS instances of the dedicated host type: 3000. RDS instances of other types: 5 to 2000. |
| InstanceNetwor kType | String | No | The network type of the instance. Valid values: Classic and VPC. This value is the same as that of the primary instance by default. |

| VPCId | String | No | The ID of the VPC. |
|---|---|---|---|
| VSwitchId | String | No | The ID of the VSwitch. |
| PrivateIpAddres s | String | No | The VPC IP address that belongs to the specified VSwitch. If no value is specified, the system automatically assigns a VPC IP address. |

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> | N/A | For more information, see Common response parameters. |
| DBInstanceId | String | The ID of the instance. |
| OrderId | Integer | The ID of the order. |

#### 1.6.3 DescribeBackups

You can call this operation to search for a set of instance backups. The set of backups must be in the Success state, indicating that they can be used to restore an instance. RDS provides backup files for you to download. When DownloadLink is NULL, RDS does not provide a download URL. When DownloadLink is not NULL, you can use this URL to download the backup file through Wget (with double quotation marks), a browser, or a user program. The expiration time for this URL is specified by LinkExpiredTime. Use it before the expiration time. If the BackupSet has expired, the following error code is displayed:

```xml
<? xml version="1.0" encoding="UTF-8" ? ><Error><Code>AccessDenied</Code><Message>Req uest has expired. </Message><Expires>2012-12-25T09:47:52.000Z</Expires> <ServerTime>2012-12-25T09:49:00.000Z</ServerTime> <RequestId>50D9768CA801C2F102005C70</RequestId><HostId>oss-test.aliyuninc.com</HostId></Error>
```

| Parameter | Type | Require d | Description |
|---|---|---|---|
| Action | Strin g | Yes | The operation that you want to perform. Set the value to DescribeBackups. |
| DBInstanceI d | Strin g | Yes | The ID of the instance for which the backup set is queried. |
| BackupId | Integ er | No | The ID of the backup set. |
| BackupStatu s | Strin g | No | The status of the backup set. Valid values: Success and Failed. |

| BackupMode | Strin g | No | The backup mode. Valid values: Automated and Manual. |
|---|---|---|---|
| StartTime | Strin g | Yes | The beginning of the time range where the query is performed. Specify the time in the yyyy-MM-ddTHH:mm:ssZ format. Example: 2011-06-11T15:00Z. |
| EndTime | Strin g | Yes | The end of the time range where the query is performed. Specify the time in the yyyy-MM-ddTHH:mm:ssZ format. Example: 2011-06-11T16:00Z. The end time must be later than the start time. |
| PageSize | Integ er | No | The number of entries to return on each page. Valid values: 30, 50, and 100. Default value: 30. |
| PageNumber | Integ er | No | The number of the page to return. Pages start from page 1 but must be equal to or smaller than the maximum Integer value. Default value: 1. |

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> |   | For more information, see Common response parameters. |
| TotalRecordCount | Interger | The total number of entries. |
| PageNumber | Integer | The number of the page returned. |
| PageRecordCount | Integer | The number of backup sets on the current page. |
| Items | List<Backup> | The array that consists of Backup data. |

#### 1.6.4 CreateTempDBInstance

**Note**

You can create a temporary instance based on a backup set or a point in time within the past seven days. When a temporary instance is created, accounts and databases inherit the backup set data. You can call this operation to create a temporary instance. Before you call this operation, ensure that the following requirements are met: The instance is in the running state. The instance is not undergoing any migration tasks. The instance is not locked by the system. The current status of the instance backup set is Success.

| Parameter | Type | Requir ed | Description |
|---|---|---|---|

| Action | String | Yes | The operation that you want to perform. Set the value to CreateTempDBInstance. |
|---|---|---|---|
| DBInstanceI d | String | Yes | The ID of the instance to be created. |
| BackupId | Integer | No | The ID of the backup set. |
| RestoreTim e | String | No | The restoration time of the backup set. It can be any time within the past seven days that is more than 30 minutes before the current time. Specify the time in the yyyy-MM- ddTHH:mm:ssZ format. The time must be in UTC. Example: 2011-06-11T16:00:00Z. |

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> |   | Common response parameters. |
| TempDBInstanceId | String | The ID of the temporary instance. |

**Sample requests**

```
https://rds.example.com/?Action=CreateTempDBInstance &BackupId=90262 &DBInstanceId=rds-xxxxx &<Common request parameters>
```

**Sample responses**

```json
<CreateTempDBInstanceResponse> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> <TempDBInstanceId>sub-xxxxx</TempDBInstanceId> </CreateTempDBInstanceResponse> { "RequestId":"1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC", "TempDBInstanceId":"sub-xxxxx"}
```

#### 1.6.5 DescribeBackupPolicy

You can call this operation to query the backup policy configured for the system. RDS periodically backs up an instance based on the user-defined system configuration.

| Parameter | Type | Required | Description |
|---|---|---|---|

| Action | String | Yes | The operation that you want to perform. Set the value to DescribeBackupPolicy. |
|---|---|---|---|
| DBInstanceId | String | Yes | The ID of the instance for which the backup policy is queried. |

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> |   | Common response parameters. |
| BackupRetentionPeri od | String | The data backup retention period. Unit: days. Valid values: 1 to 30. |
| PreferredBackupTim e | String | The backup time. The time is in the HH:mmZ to HH:mmZ format. |
| PreferredBackupPeri od | String | The backup day. Valid values: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, and Sunday. |
| BackupLog | String | The log backup status. Valid values: Enable and Disabled. |
| LogBackupRetention Period | String | The log backup retention period. Unit: days. Valid values: 1 to 30. |

#### 1.6.6 ModifyBackupPolicy

You can call this operation to modify a backup policy. RDS periodically backs up instances based on the user-defined system configuration.

| Parameter | Type | Requ ired | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to ModifyBackupPolicy. |
| DBInstanceId | String | Yes | The ID of the instance for which the backup policy is modified. |
| PreferredBackupTim e | String | Yes | The backup time. Format: HH:mmZ to HH:mmZ. |
| PreferredBackupPeri od | String | Yes | The backup day. Valid values: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, and Sunday. |
| BackupRetentionPeri od | String | No | The data backup retention period. Unit: days. Valid values: 1 to 30. Default value: 7. |
| BackupLog | String | No | The log backup status. Valid values: Enable and Disabled. Default value: Enable. |

| LogBackupRetention Period | String | No | The log backup retention period. It cannot exceed BackupRetentionPeriod. Unit: days. Valid values: 1 to 30. When you enable log backup, you can configure the log backup retention period. This operation is only supported on MySQL, PostgreSQL, and PPAS. |
|---|---|---|---|

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> | - | Common response parameters. |

**Sample requests**

```
https://rds.example.com/?Action=ModifyBackupPolicy &DBInstanceId=rds-xxxxx &PreferredBackupTime=00:00Z—01:00Z &PreferredBackupPeriod=Monday &<Common request parameters>
```

**Sample responses**

```json
<ModifyBackupPolicyResponse> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> </ModifyBackupPolicyResponse> { "RequestId":"1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC"}
```

#### 1.6.7 RestoreDBInstance

You can call this operation to overwrite the contents of an instance and restore a backup set to that instance. Before you call this operation, ensure that the following requirements are met: The instance is in the running state. The instance is not undergoing any migration tasks. The instance is not locked by the system. The current status of the instance backup set is Success.

| Parameter | Type | Required | Description |
|---|---|---|---|

| Action | String | Yes | The operation that you want to perform. Set the value to RestoreDBInstance. |
|---|---|---|---|
| DBInstanceId | String | Yes | The ID of the instance to which the backup set is restored. |
| BackupId | Integer | Yes | The ID of the backup set. |

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> | - | For more information, see Common response parameters. |

**Sample requests**

```
https://rds.example.com/?Action=RestoreDBInstance &BackupId=103312 &DBInstanceId=rds-xxxxx &<Common request parameters>
```

**Sample responses**

```json
<RestoreDBInstanceResponse> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> </RestoreDBInstanceResponse> {"RequestId":"1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC"}
```

#### 1.6.8 DeleteBackup

You can call this operation to delete data backup files that have been stored for longer than seven days or longer than the log backup retention period. This operation only deletes the specified backup sets for the target instance. It does not delete the backup sets for associated instances, such as read-only, disaster recovery, or cloned instances. Before you call this operation, make sure that the following requirements are met: The instance is in the running state. The database engine is MySQL or PolarDB.

| Paramete r | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DeleteBackup. |
| DBInstanc eId | String | Yes | The ID of the instance. |
| BackupId | String | Yes | The ID of the backup set. You can call theD escribeBackups operation to query the backup set IDs. You can enter up to 100 backup set IDs in a single request. Separate multiple IDs with commas (,). Among the query results of DescribeBackups, you can only delete the backup sets that are in the Enabled state. |

This operation returns only common response parameters. For more information, see Common response parameters.

### 1.7 Monitoring management

#### 1.7.1 DescribeResourceUsage

You can call this operation to query the disk space usage of an instance. When this operation is called, the system returns the amount of space occupied by the specified instance. The DBInstanceId parameter is used to obtain instance resource usage information.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeResourceUsage. |
| DBInstanceId | String | Yes | The instance ID. |

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> |   | For more information, see Common response parameters. |
| DBInstanceId | String | The instance ID. |
| Engine | String | The database engine. |
| DiskUsed | Integer | The total space occupied by data and log files. Unit: bytes. -1 indicates that no space is used. |
| DataSize | Integer | The storage that is used to store data files. Unit: bytes. A value of -1 indicates that no data files are stored. |

| LogSize | Integer | The disk space that is used to store log files. Unit: bytes. -1 indicates that no space is used. |
|---|---|---|
| BackupSize | Integer | The disk space that is used to store backup files. Unit: bytes. -1 indicates no space is used. |
| ColdBackupSize | Integer | The total space occupied by cold backup data. Unit: bytes. -1 indicates that no space is used. |
| SQLSize | Integer | The total space occupied by SQL data. Unit: bytes. -1 indicates that no space is used. |

#### 1.7.2 DescribeDBInstancePerformance

You can call this operation to query the performance metrics of an instance over a specified period of time based on the performance parameters. There are three output formats based on different query time ranges: When the query time range is less than or equal to one day, performance metrics are displayed at one-minute intervals. Queries with the time range from one to seven days are not supported. When the query time range is greater than seven days but less than or equal to 15 days, performance metrics are displayed at one-hour intervals. Queries with the time range greater than 15 days but less than 30 days are not supported. When the query time range is greater than or equal to 30 days but less than or equal to one year, performance metrics are displayed at one-day intervals.

**Note**

When the instance space usage key is MySQL_SpaceUsage or SQLServer_SpaceUsage, performance metrics can be queried only when the time range is less than or equal to one day.

| Paramet er | Type | Requir ed | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeDBInstancePerformance. |
| DBInstan ceId | String | Yes | The ID of the instance. |
| Key | Intege r | Yes | The performance metrics. Separate performance metrics with commas (,). For more information, see Performance parameters. |
| StartTime | String | Yes | The beginning of the time range to query. Specify the time in the ISO 8601 standard in the YYYY-MM-DDTHH:mmZ format. Example: 2012-06-11T15:00Z. |
| EndTime | String | Yes | The end of the time range to query. Specify the time in the ISO 8601 standard in the YYYY-MM-DDTHH:mmZ format. Example: 2012-06-11T15:00Z. |

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> | N/A | Common response parameters |
| DBInstanceId | String | The ID of the instance. |
| Engine | String | The engine of the database. |
| StartTime | String | The beginning of the time range where the query was executed. The time follows the ISO 8601 standard in the YYYY-MM-DDTHH:mmZ format. Example: 2011-05-30T03:29Z. |
| EndTime | String | The end of the time range where the query was executed. The time follows the ISO 8601 standard in the YYYY-MM-DDTHH:mmZ format. Example: 2011-05-30T03:29Z. The end time must be later than the start time. |
| PerformanceKey s | List<PerformanceKey> | The array that consists of PerformanceKey data. Format: {perf1, perf2, perf3, ...}. |

**Sample requests**

```xml
https://rds.example.com/?Action=DescribeDBInstancePerformance &DBInstanceId=rds-xxxxx &key= MySQL_xxxxx &StartTime=2013-01-11T15:00:00Z &EndTime=2013-06-05T15:00:00Z &<Common request parameters> <DescribeDBInstancePerformanceResponse> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> <DBInstanceID>rds-xxxxx</DBInstanceID> <StartTime>2013-01-11T15:00:00Z</StartTime> <EndTime>2013-10-17T15:00Z</EndTime> <Engine>MySQL</Engine> <PerformanceKeys> <PerformanceKey> <Key>MySQL_xxxxx</Key> <Unit>KB</Unit> <ValueFormat>recv_k&amp;sent_k</ValueFormat> <Values><Values/> </PerformanceKey> </PerformanceKeys> </DescribeDBInstancePerformanceResponse>
```

```json
{ "RequestId"1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC, "DBInstanceID": rds-xxxxx, "StartTime": "2012-06-11T15:00Z", "EndTime": "2013-10-17T15:00Z", "Engine": "MySQL", "PerformanceKeys":
    { PerformanceKey[ {
        "Key": "MySQL_xxxxx",
        "Unit": "KB",
        "ValueFormat": "recv_k&sent_k",
        "Values": { "PerformanceValue":[] } } ] }}
```

#### 1.7.3 DescribeDBInstanceMonitor

You can call this operation to query the monitoring behavior of an instance.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeDBInstanceMonitor. |
| DBInstance Id | String | Yes | The instance ID. |

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> | - | For more information, see Common response parameters. |
| Period | String | The monitoring data collection interval. Unit: seconds. |

#### 1.7.4 ModifyDBInstanceMonitor

You can call this operation to modify the monitoring behavior of an instance.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to ModifyDBInstanceMonitor. |
| DBInstanceId | String | Yes | The instance ID. |

| Period | String | Yes | The monitoring data collection interval. Unit: seconds. Valid values: 60 and 300. Default value: 300. |
|---|---|---|---|

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> | - | For more information, see Common response parameters. |

### 1.8 Parameter management

#### 1.8.1 DescribeParameterTemplates

You can call this operation to query the parameter template list. The list includes parameter names, default parameter values, whether they can be modified, whether the database must be restarted for the parameters to take effect, and regular expressions acting as parameter validation rules.

| Paramete r | Typ e | Requi red | Description |
|---|---|---|---|
| Action | Strin g | Yes | The operation that you want to perform. Set the value to DescribeParameterTemplates. |
| Engine | Strin g | Yes | The engine of the database. Valid values: mysql: MySQL mssql: SQL Server PostgreSQL: PostgreSQL POLARDB: PolarDB |
| EngineVer sion | Strin g | Yes | The engine version of the database. Valid values: MySQL: 5.6 and 5.7 SQL Server: 2008 R2 PostgreSQL: 9.4 and 10.0 PolarDB: 11 |

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> | - | Common response parameters. |
| Engine | String | The engine of the database. |

| EngineVersion | String | The engine version of the database. |
|---|---|---|
| ParameterCount | Integer | The number of parameters. |
| Parameters | List<TemplateRecord > | The array that consists of TemplateRecord data. Format: {parameter1, parameter2, parameter3, ...}. |

**Sample requests**

```json
https://rds.example.com/?Action=DescribeParameterTemplates &Engine=MySQL &EngineVersion=5.6 &<Common request parameters> <DescribeParameterTemplatesResponse> <Engine>mysql</Engine> <EngineVersion>5.6</EngineVersion> <ParameterCount>1</ParameterCount> <Parameters> <TemplateRecord> <CheckingCode>[0-100]</CheckingCode> <ForceRestart>True</ForceRestart> <Factor>1</Factor> <ParameterDescription>test</ParameterDescription> <ParameterName>fill factor</ParameterName> <ParameterValue>0</ParameterValue> <ForceModify>True</ForceModify> <Unit>INT</Unit> </TemplateRecord> </Parameters> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> </DescribeParameterTemplatesResponse> {"Engine": "mysql", "EngineVersion": "5.6", "ParameterCount":1, "Parameters":
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

#### 1.8.2 DescribeParameters

You can call this operation to query the current instance parameter configuration.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeParameters. |
| DBInstanceId | String | Yes | The ID of the instance. |

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> | N/A | Common response parameters. |
| Engine | String | The engine of the database. |
| EngineVersion | String | The engine version of the database. |
| RunningParameters | List<DBInstanceParameter> | The array that consists of running DBInstanceParameter data. Format: {parameter1,parameter2,param eter3, ...}. |
| ConfigParameters | List<DBInstanceParameter> | The array that consists of synchronizing DBInstanceParameter data. Format: {parameter1,parameter2,param eter3, ...}. |

Table 1. DBInstanceParameter parameters

| Parameter | Type | Description |
|---|---|---|
| ParameterName | String | The name of the parameter. |
| ParameterValue | String | The value of the parameter. |
| ParameterDescription | String | The description of the parameter. |

**Sample requests**

```json
https://rds.example.com/?Action=DescribeParameters &DBInstanceId=rds-xxxxx &<Common request parameters> <DescribeParametersResponse> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> <Engine>mysql</Engine > <EngineVersion>5.6</EngineVersion> <RunningParameters> <DBInstanceParameter> <ParameterDescription>test</ParameterDescription> <ParameterName>fill factor</ParameterName> <ParameterValue>0</ParameterValue> </DBInstanceParameter> </RunningParameters> <ConfigParameters> <DBInstanceParameter> <ParameterDescription>test1</ParameterDescription> <ParameterName>fill factor</ParameterName> <ParameterValue>50</ParameterValue> </DBInstanceParameter> </ConfigParameters> </DescribeParametersResponse> { "ConfigParameters": {
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

#### 1.8.3 ModifyParameter

You can call this operation to modify instance parameters. After you submit a request, RDS assigns a task to apply new parameters to the instance. If there are any parameter modifications that require the database to be restarted, RDS restarts the database. Before you call this operation, ensure that the following requirements are met: The instance is in the running state. The instance is not locked by the system. There are three types of parameter values: 1 to 65,535: indicates a numerical range. Regular identification is used to extract the minimum and maximum values. The input parameter is then verified based on the extracted minimum and maximum values. The parameter must be a multiple of a divisible factor. utf8 | gbk | latin1: indicates a set value determination rule. Regular identification is used to extract the fixed value. The input parameter is then verified based on these fixed values. Others: These must be implemented with regular expressions. Before assigning the task, RDS checks the parameter as follows:
1. Whether the parameter exist.
2. Whether the parameter can be modified.
3. Whether the parameter is valid.
If the parameter is invalid, RDS returns the 400 HTTP status code and information about the invalid parameter. Example:

```json
{"HttpStatusCode":400, "Code":"InvalidParameter.Format", "Message":"Specified parameter is not valid. [auto_increment_increment:a,character_set_client:41]"}
```

| Parameter | Type | Require d | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to ModifyParameter. |
| DBInstanceI d | String | Yes | The ID of the instance for which parameters are modified. |
| Parameters | String | Yes | The JSON string for the parameter and its value. The parameter value must be of the string type. {"auto increment increment":"1", _ _ "character set client":"utf8"}. _ _ |
| Forcerestart | String | No | Specifies whether to forcibly restart the database. Valid values: true and false. If a parameter can take effect only after database restart, Forcerestart must be set to true. Otherwise, the parameter modification will not take effect. Default value: false. |

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> | - | Common response parameters. |

**Sample requests**

```
https://rds.example.com/?Action=ModifyeParameter &DBInstanceId=rds-xxxxx &Parameters={"key_buffer_size":"456","character_set_client":"gbk"} &<Common request parameters>
```

**Sample responses**

```json
<ModifyeParameterResponse> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> </ModifyeParameterResponse> { "RequestId":"1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC",}
```

### 1.9 Log management

#### 1.9.1 DescribeSlowLogs

You can call this operation to query the slow log summary of the databases in a specified instance over a specified period of time. This operation supports paged query.

| Paramet er | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeSlowLogs. |
| DBInstan ceId | String | Yes | The ID of the instance. |
| StartTime | String | Yes | The beginning of the time range to query. Specify the date in the ISO 8601 standard in the YYYY-MM-DDZ format. Example: 2011-05-30Z. |
| EndTime | String | Yes | The end of the time range to query. The end date must be later than the start date. Specify the date in the ISO 8601 standard in the YYYY-MM- DDZ format. Example: 2011-05-30Z. |
| DBName | String | No | The name of the database. |

| SortKey | String | No | The basis on which query results are sorted. Valid values: TotalExecutionCounts: in descending order of execution times. TotalQueryTimes: in descending order of the total execution duration. TotalLogicalReads: in descending order of the total number of logical reads. TotalPhysicalReads: in descending order of the total number of physical reads. This parameter is applicable to SQL Server instances. It must be used when you query SQL Server Instances. |
|---|---|---|---|
| PageSize | Integer | No | The number of entries to return on each page. Valid values: 30, 50, and 100. Default value: 30. |
| PageNum ber | Integer | No | The number of the page to return. Pages start from page 1. Default value: 1. |

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> |   | Common response parameters. |
| Engine | String | The engine of the database. |
| StartTime | String | The beginning of the time range where the query was executed. The date follows the ISO 8601 standard in the YYYY-MM-DDZ format. Example: 2011-05-30Z. |
| EndTime | String | The end of the time range where the query was executed. The date follows the ISO 8601 standard in the YYYY-MM-DDZ format. Example: 2011-05-30Z. |
| TotalRecordCou nt | Integer | The total number of entries. |
| PageNumber | Integer | The page number of the returned page. |
| PageRecordCou nt | Integer | The number of SQL slow queries on the current page. |
| Items | List<SQLSlow Log> | The list of slow logs. |

**Sample requests**

```json
https://rds.example.com/?Action=DescribeSlowLogs &DBInstanceId=rds-xxxxx &StartTime=2011-06-11Z &EndTime=2011-12-11Z &SortKey= Totaxxxxx &<Common request parameters> <DescribeSlowLogsResponse> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> <DBInstanceID>rds-xxxxx</DBInstanceID> <Engine>MySQL</Engine> <StartTime>2011-06-11Z</StartTime> <EndTime>2011-12-11Z</EndTime> <TotalRecordCount>1</TotalRecordCount> <PageNumber>1</PageNumber> <PageRecordCount>1</PageRecordCount> <Items> <SQLSlowLog> <SQLText>update test.zxb set id=0 limit 1</SQLText> <MySQLTotalExecutionCounts>178</MySQLTotalExecutionCounts> <MySQLTotalExecutionTimes>189</MySQLTotalExecutionTimes> <TotalLogicalReadcounts>89</TotalLogicalReadcounts> <TotalPhysicalReadcounts>90</TotalPhysicalReadcounts> <ReportTime>2013-11-12Z</ReportTime> </SQLSlowLog> </Items> </DescribeSlowLogsResponse> { "RequestId":"1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC", "StartTime":"2011-06-11Z ", "EndTime":"2011-12-11Z ", "Engine":"MySQL", "PageNumber":1, "PageRecordCount":1, "TotalRecordCount":1, "Items":{
    "SQLSlowLog":[{
        "SQLText":”update test.zxb set id=0 limit 1”,
        "MySQLTotalExecutionCounts":178,
        "MySQLTotalExecutionTimes":189,
        "TotalLogicalReadcounts":89,
        "TotalPhysicalReadcounts":90,
        "ReportTime":"2013-11-12Z " }]}}
```

#### 1.9.2 DescribeSlowLogRecords

You can call this operation to query the slow log details of the databases in a specified instance over a specified period of time. This operation is only supported on MySQL instances.

| Paramet er | Type | Requir ed | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeSlowLogRecords. |
| DBInstan ceId | String | Yes | The ID of the instance to which the database belongs. |
| StartTime | String | Yes | The beginning of the time range where the query is performed. Specify the time in the yyyy-MM-ddTHH:mm:ssZ format. Example: 2011-06-11T15:00Z. |
| EndTime | String | Yes | The end of the time range where the query is performed. Specify the time in the yyyy-MM-ddTHH:mm:ssZ format. Example: 2011- 06-11T16:00Z. |
| DBName | String | No | The name of the database. |
| PageSize | Integer | No | The number of entries to return on each page. Valid values: 30, 50, and 100. Default value: 30. |
| PageNum ber | Integer | No | The number of the page to return. Pages start from page 1 but must be equal to or smaller than the maximum Integer value. Default value: 1. |

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
| HostAddress | Strin g | The host address to connect the database. |
| DBName | Strin g | The name of the database. |

| SQLText | Strin g | The query statement. |
|---|---|---|
| QueryTimes | Long | The execution time of the slow query. Unit: seconds. |
| LockTimes | Long | The lock time of the slow query. Unit: seconds. |
| ParseRowCounts | Long | The number of entries parsed. |
| ReturnRowCount s | Long | The number of entries returned. |
| ExecutionStartTi me | Strin g | The beginning of the time range where the query was executed. The time is in the yyyy-MM-ddTHH:mm:ssZ format. Example: 2011-06- 11T15:00:08Z. |

**Sample requests**

```
https://rds.example.com/?Action=DescribeSlowLogRecords &DBInstanceId=rds-xxxxx &StartTime=2011-06-11T15:00Z &EndTime=2011-06-11T16:00Z &<Common request parameters>
```

**Sample responses**

```xml
<DescribeSlowLogRecordsResponse> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> <DBInstanceID>rds-xxxxx</DBInstanceID> <Engine>MySQL</Engine> <TotalRecordCount>1</TotalRecordCount> <PageNumber>1</PageNumber> <PageRecordCount>1</PageRecordCount> <Items> <SQLSlowRecord> <HostAddress>192.168.0.123</HostAddress> <DBName>test</DBName> <SQLText>update test.zxb set id=0 limit 1</SQLText> <QueryTimes>123</QueryTimes> <LockTimes>12</LockTimes> <ParseRowCounts>125</ParseRowCounts> <ReturnRowCounts>1</ReturnRowCounts> <ExecutionStartTime>2011-06-11T15:00:08Z</ExecutionStartTime> </SQLSlowRecord> </Items> </DescribeSlowLogRecordsResponse>
```

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

#### 1.9.3 DescribeErrorLogs

You can call this operation to query the error logs generated for an instance over a specified period of time.

| Paramete r | Ty pe | Requ ired | Description |
|---|---|---|---|
| Action | Stri ng | Yes | The operation that you want to perform. Set the value to DescribeErrorLogs. |
| DBInstanc eId | Stri ng | Yes | The ID of the instance for which error logs are queried. |
| StartTime | Stri ng | Yes | The beginning of the time range where the query is performed. Specify the time in the yyyy-MM-ddTHH:mm:ssZ format. Example: 2011-05- 30T12:10Z. |
| EndTime | Stri ng | Yes | The end of the time range where the query is performed. Specify the time in the yyyy-MM-ddTHH:mm:ssZ format. Example: 2011-05- 30T20:10Z. |
| PageSize | Inte ger | No | The number of entries to return on each page. Valid values: 30, 50, and 100. Default value: 30. |
| PageNum ber | Inte ger | No | The number of the page to return. Pages start from page 1 but must be equal to or smaller than the maximum Integer value. Default value: 1. |

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> |   | Common response parameters. |
| TotalRecordCount | Integer | The total number of entries. |

| PageNumber | Integer | The number of the page returned. |
|---|---|---|
| PageRecordCount | Integer | The number of error logs on the current page. |
| Items | List<ErrorLogs> | - |

ErrorLogs parameters

| Parameter | Type | Description |
|---|---|---|
| ErrorInfo | String | The error log information. |
| CreateTime | String | The time when the error log was generated. The time is in the yyyy- MM-ddTHH:mm:ssZ format. Example: 2011-05-30T12:11:4Z. |

**Sample requests**

```
https://rds.example.com/?Action=DescribeErrorLogs. &DBInstanceId=rds-xxxxx &StartTime=2011-06-11T15:00Z &EndTime=2011-06-11T20:00Z &<Common request parameters>
```

**Sample responses**

```json
<DescribeErrorLogsResponse> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> <TotalRecordCount>1</TotalRecordCount> <PageNumber>1</PageNumber> <PageRecordCount>1<PageRecordCount> <Items> <ErrorLog> <ErrorInfo>spid52 DBCC TRACEON 3499, server process ID (SPID) 52. This is an informat ional message only; no user action is required</ErrorInfo> <CreateTime>2013-06-04T15:00:00</CreateTime> </ErrorLog> </Items> </DescribeErrorLogsResponse> {"RequestId":"1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC", "PageNumber":1, "TotalRecordCount":1, "PageRecordCount":1, "Items":{
    "ErrorLog":[{
        ErrorInfo:”spid52 DBCC TRACEON 3499, server process ID (SPID) 52. This is an
informational message only; no user action is required”,
        CreateTime:”2013-06-04T15:00:00”}]}}
```

#### 1.9.4 DescribeBinlogFiles

You can call this operation to query binlogs of a MySQL instance. This operation supports querying by page. RDS provides binlog files for you to download. When the DownloadLink is NULL, RDS does not provide a download URL. When DownloadLink is not NULL, you can use this URL to download the backup file through Wget (with double quotation marks), a browser, or a user program. The expiration time for this URL is specified by LinkExpiredTime. Use it before the expiration time. If the BackupSet has expired, the following error code is displayed:

```xml
<Error> <Code>AccessDenied</Code> <Message>Request has expired. </Message> <Expires>2012-12-25T09:47:52.000Z</Expires> <ServerTime>2012-12-25T09:49:00.000Z</ServerTime> <RequestId>50D9768CA801C2F102005C70</RequestId> <HostId>oss-test.aliyun-inc.com</HostId> </Error>
```

| Parameter | Type | Requir ed | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeBinlogFiles. |
| DBInstanceI d | String | Yes | The ID of the instance for which binlogs are queried. |
| StartTime | String | Yes | The beginning of the time range where the query is performed. Specify the time in the yyyy-MM-ddTHH:mm:ssZ format. |
| EndTime | String | Yes | The end of the time range where the query is performed. Specify the time in the yyyy-MM-ddTHH:mm:ssZ format. The end time must be later than the start time. |
| PageSize | Integer | No | The number of entries to return on each page. Valid values: 30, 50, and 100. Default value: 30. |
| PageNumbe r | Integer | No | The number of the page to return. Pages start from page 1 but must be equal to or smaller than the maximum Integer value. Default value: 1. |

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> | - | Common response parameters. |
| TotalRecordCount | Integer | The total number of binlog files. |
| PageNumber | Integer | The number of the page returned. |

| PageRecordCount | Integer | The number of binlog files on the current page. |
|---|---|---|
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

**Sample requests**

```
https://rds.example.com/?Action=DescribeBinlogFiles &DBInstanceId=rds-xxxxx &StartTime=2011-06-11T15:00:00Z &EndTime=2013-06-05T15:00:00Z &<Common request parameters>
```

**Sample responses**

```json
<DescribeBinlogFilesResponse> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> <TotalRecordCount>1</TotalRecordCount> <PageNumber>1</PageNumber> <PageRecordCount>1<PageRecordCount> <Items> <BinLogFile> <FileSize>123</FileSize> <LogBeginTime>2013-06-01T15:00:00Z</LogBeginTime> <LogEndTime>2013-06-02T18:00:00Z</LogEndTime> <DownloadLink>http://rdslog-real.oss.aliyuncs.com/custins47742/hostins46770/mysql-bin . 000120.zip? spm=0.0.0.0.eMQKjs&OSSAccessKeyId=c9gzsqpauxxxxx&Expires=1384916927&Signature=07TMgM3xx x</DownloadLink> <LinkExpiredTime>2013-06-09T18:00:00Z</LinkExpiredTime> </BinLogFile> </Items> </DescribeBinlogFilesResponse> { "RequestId":"66816822-CEC1-4C8D-AB26-2530A7D4DCA5", "PageNumber":1, "TotalRecordCount":1, "PageRecordCount":1, "Items":{
    "BinLogFile":[{
        FileSize:”123”,
        LogBeginTime:”2013-06-01T15:00:00Z”,
        LogEndTime:”2013-06-02T18:00:00Z”,
        DownloadLink:”http://rdslog-
real.oss.aliyuncs.com/custinsxxxxx/hostinsxxxxx/mysql-bin. 000120.zip? spm=0.0.0.0.eMQKjs&OSSAccessKeyId=c9gzsqpauxxxxx&Expires=1384916927&Signature=07TMgM3xx x”,
        LinkExpiredTime”2013-06-09T18:00:00Z”}]}}
```

#### 1.9.5 DescribeSQLCollectorPolicy

You can call this operation to check whether SQL collection is enabled for a specified RDS instance.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeSQLCollectorPolicy. |
| DBInstanceId | String | Yes | The ID of the instance for which SQL collection is enabled or disabled. |

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> |   | Common response parameters. |
| SQLCollectorStatu s | String | Indicates whether SQL collection is enabled. Valid values: Enable and Disabled. |

#### 1.9.6 ModifySQLCollectorPolicy

You can call this operation to enable or disable SQL collection for the specified RDS instance.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | Strin g | Yes | The operation that you want to perform. Set the value to ModifySQLCollectorPolicy. |
| DBInstanceId | Strin g | Yes | The ID of the instance for which SQL collection is enabled or disabled. |
| SQLCollector Status | Strin g | Yes | Specifies whether to enable SQL collection. Valid values: Enable and Disabled. |

This operation returns only common response parameters.

#### 1.9.7 DescribeSQLLogRecords

You can call this operation to query the SQL audit logs generated for an instance.

| Paramete r | Typ e | Requi red | Description |
|---|---|---|---|
| Action | Stri ng | Yes | The operation that you want to perform. Set the value to DescribeSQLLogRecords. |
| DBInstanc eId | Stri ng | Yes | The ID of the instance for which SQL audit logs are queried. |
| Database | Stri ng | No | The name of the database. All databases are selected by default. |
| User | Stri ng | No | The name of the user. All users are selected by default. |

| Form | Stri ng | No | The file generation form for audit logs. Valid values: File and Stream. If this parameter is set to File, only common parameters are returned, and you must call the DescribeSQLLogFiles operation to obtain the final download file address. If this parameter is set to Stream, data streams are returned. Default value: Stream. |
|---|---|---|---|
| QueryKey words | Stri ng | No | The keywords used for query. Up to 10 keywords can be entered at a time. Separate multiple keywords with spaces. |
| StartTime | Stri ng | Yes | The beginning of the time range where the query is performed. Specify the time in the yyyy-MM-ddTHH:mm:ssZ format. |
| EndTime | Stri ng | Yes | The end of the time range where the query is performed. Specify the time in the yyyy-MM-ddTHH:mm:ssZ format. The end time must be later than the start time. |
| PageSize | Inte ger | No | The number of entries to return on each page. Valid values: 30, 50, 100, and 200. Default value: 100. |
| PageNumb er | Inte ger | No | The number of the page to return. Pages start from page 1 but must be equal to or smaller than the maximum Integer value. Default value: 1. |

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> | - | Common response parameters. |
| TotalRecordCount | Integer | The total number of entries. |
| PageNumber | Integer | The number of the page returned. |
| PageRecordCount | Integer | The number of SQL logs on the current page. |
| Items | List<SQLRecord > | The array that consists of SQLRecord data. |

SQLRecord parameters

| Parameter | Type | Description |
|---|---|---|
| DBName | String | The name of the database. |
| AccountName | String | The name of the account. |
| HostAddress | String | The IP address of the client. |
| SQLText | String | The SQL statement. |
| TotalExecutionTimes | Long | The amount of time taken to execute the operation. Unit: microseconds. |
| ReturnRowCounts | Long | The number of entries returned. |
| ThreadID | String | The thread ID. |

| ExecuteTime | String | The execution time. The time is in the yyyy-MM- ddTHH:mm:ssZ format. Example: 2011-05-30T12:11:20Z. |
|---|---|---|

**Sample requests**

```
https://rds.example.com/?Action=DescribeSQLLogRecords &DBInstanceId=rds-xxxxx &StartTime=2011-06-11T15:00:00Z &EndTime=2013-06-05T15:00:00Z &<Common request parameters>
```

**Sample responses**

```json
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
</DescribeSQLLogRecordsResponse> {"PageNumber":1,
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

#### 1.9.8 DescribeSQLLogFiles

You can call this operation to query SQL audit files.

| Parameter | Type | Require d | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeSQLLogFiles. |
| DBInstanceI d | String | Yes | The ID of the instance for which SQL audit files are queried. |

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
| LogDownloadU RL | String | The file download URL. If the download URL is unavailable, this parameter will be empty. |
| LogSize | Long | The size of an audit log file. Unit: Byte. |

### 1.10 Data migration

#### 1.10.1 CreateUploadPathForSQLServer

You can call this operation to create the account and password of the file server and the file path. Based on this information, you can upload data files. After the upload is complete, you can migrate external data.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to CreateUploadPathForSQLServer. |
| DBInstanceId | String | Yes | The ID of the instance. |
| DBName | String | Yes | The name of the database. |

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> | - | Common response parameters. |
| InternetFtpServer | String | The IP address of the file server on the public network. |
| InternetPort | Integer | The port of the file server on the public network. |
| IntranetFtpServer | String | The IP address of the file server on the internal network. |
| IntranetPort | Integer | The port of the file server on the internal network. |
| UserName | String | The username used to log on to the file server. |
| Password | String | The password used to log on to the file server. |
| FileName | String | The name of the data file with the extension. |

**Sample requests**

```
https://rds.example.com/?Action= CreateUploadPathForSQLServer &DBInstanceId=rds-xxxxx &DBName=testdb01 &<Common request parameters>
```

```json
<CreateUploadPathForSQLServerResponse> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> <InternetFtpServer>10.230.239.1</InternetFtpServer> <InternetPort>3021</InternetPort> <IntranetFtpServer></IntranetFtpServer> <UserName>userxxx</UserName> <Password>pwxxxxx</Password> <FileName>testdb01_xxxxx.bak</FileName> </CreateUploadPathForSQLServerResponse> {"RequestId":"1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC",
 "InternetFtpServer ":"10.230.239.1",
 "InternetPort":3021,
 "IntranetFtpServer":"",
 "UserName":"userxxx",
 "Password":"pwxxxxx",
 "FileName":"testdb01_xxxxx.bak"}
```

#### 1.10.2 ImportDatabaseBetweenInstances

You can call this operation to migrate data from one ApsaraDB for RDS instance to another. This operation is only supported on dedicated ApsaraDB RDS for MySQL instances. ApsaraDB RDS for MySQL instances support batch database migration. During migration, the source instance status changes to Migrating and the destination instance status changes to Importing Data. Database migration is performed between different instances that belong to the same user. Before you call this operation, make sure that the following requirements are met: The instance is in the running state. The database is in the running state. The destination instance is not locked by the system. The reserved storage space of the destination instance is greater than the space calculated by the formula: Space occupied by the destination instance - Database space of the destination instance + Database space of the source instance. Databases to be migrated exist in both the source and destination instances and are activated. ApsaraDB RDS for SQL Server instances support batch database migration. During migration, the source instance status changes to Migrating and the destination instance status changes to Importing Data. Database migration is performed between different instances that belong to the same user. Before you call this operation, make sure that the following requirements are met: The instance is in the running state. The database is in the running state. The destination instance is not locked by the system. The reserved storage space of the destination instance is greater than the space calculated by the formula: Space occupied by the destination instance - Database space of the destination instance + Database space of the source instance.

| Parameter | Type | Requi red | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to ImportDatabaseBetweenInstances. |
| DBInstanceId | String | Yes | The ID of the instance. |
| SourceDBInstan ceId | String | Yes | The ID of the source instance. It cannot be the same as that of the destination instance. |
| DBInfo | String | Yes | The information of the database to be migrated. Specify this parameter in the JSON format. For ApsaraDB RDS for MySQL instances, the parameter value is an array. Example: {"DBNames":["mydb","mydb2"]}. The names of the source and destination databases must be the same. In this example, data is migrated from the mydb and mydb2 databases. These databases must exist in both the source and destination instances. |

DBInfo parameters

| Paramet er | Type | Required | Description |
|---|---|---|---|
| DBNames | List | Yes | The names of databases to be migrated. Example: ["mydb","mydb2"]. |

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> |   | For more information, see Common response parameters. |
| ImportId | Integer | The ID of the destination instance. |

**Sample requests**

```
https://rds.example.com/?Action=ImportDatabaseBetweenInstances &DBInstanceId=rds-xxxxx &SourceDBInstanceId=rds-xxxxx &{"DBNames":["mydb","mydb2"]} &<Common request parameters>
```

```json
<ImportDatabaseBetweenInstancesResponse>
 <ImportId>2122321</ImportId>
 <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId>
 </ImportDatabaseBetweenInstancesResponse>
{"ImportId":2122321",
 RequestId":"1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC"}
```

#### 1.10.3 CancelImport

You can call this operation to cancel migration tasks from ApsaraDB RDS for MySQL instances. Migration tasks from MySQL instances can be canceled.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to CancelImport. |
| DBInstanceId | String | Yes | The ID of the instance. |
| ImportId | Integer | Yes | The migration task ID. |

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> | - | Common response parameters. |

**Sample requests**

```xml
https://rds.example.com/?Action=CancelImport &DBInstanceId=rds-xxxxx &ImportId=127562 &<Common request parameters> <CancelImportResponse> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> </CancelImportResponse>
```

```json
{"RequestId": "1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC" }
```

### 1.11 Tag management

#### 1.11.1 AddTagsToResource

You can call this operation to bind existing or newly created tags to instances. Before you call this operation, ensure that the following requirements are met: Each tag is composed of a TagKey and a TagValue. The TagKey cannot be blank, but the TagValue can. The values of TagKey and TagValue cannot start with aliyun. The values of TagKey and TagValue are not case sensitive. The maximum length of TagKey is 64 characters and the maximum length of TagValue is 128 characters. Each instance can only be bound to a maximum of 10 tags. Each tag bound to the same instance must have a unique TagKey. If tags with duplicate TagKeys are bound to the same instance, the tag bound last overwrites the existing tag.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to AddTagsToResource. |
| RegionId | String | Yes | The region ID of the instance for which a tag is be bound. |
| DBInstanceId | String | Yes | The ID of the instance for which a tag is be bound. Up to 30 IDs can be entered in a single request. Separate multiple IDs with commas (,) Format: instance1,instance2,instance3. |
| Tags | JSON string | Yes | The tag pair to be bound. This parameter must include a TagKey, but does not need to include a corresponding TagValue. Up to five tag pairs can be entered in a single request. The TagKey is required, and TagValue is optional. Format: {“key1”:”value1”,“key2”:””}. |

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> | - | Common response parameters. |

#### 1.11.2 DescribeTags

You can call this operation to view the bound tag information of an RDS instance belonging to the current account. This operation must meet the following requirements: If a specified instance ID is provided, all tags bound to this instance are queried and the other filter criteria are ignored. If the TagKey of a key is provided without a TagValue, the results of all tags matching the TagKey criteria are returned. If both TagKey and TagValue are provided, only the results that match both parameters are returned.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeTags. |
| RegionId | String | Yes | The region ID of the instance. |
| DBInstanc eId | String | No | The name of the instance. If this parameter is provided, all the other filter criteria are ignored. |
| Tags | Json string | No | The tag pair. This parameter must include a TagKey, but does not need to include a corresponding TagValue. The TagKey cannot be blank, but the TagValue can. Format: {"key1":"value1 "}. |

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
|---|---|---|

#### 1.11.3 RemoveTagsFromResource

You can call this operation to remove tags from an instance. This operation must meet the following requirements: A maximum of 10 tags can be removed in a single request. If a tag is removed from all instances to which the tag is added, the tag is automatically deleted. If the TagKey of a key is provided without a TagValue, all tags matching the TagKey are removed.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to RemoveTagsFromResource. |
| RegionId | String | Yes | The region ID. |
| DBInstanceI d | String | Yes | The instance ID. |
| Tags | Json String | Yes | The tag pair to be removed. This parameter must include a TagKey, but does not need to include a corresponding TagValue. The tag key is required, and the tag value is optional. Format: {"key1":"value1"}. |

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> | - | For more information, see Common response parameters. |

### 1.12 RAM authorization

**Use RAM for RDS resource authorization**

All RDS instances created through an Apsara Stack tenant account are resources owned by that account. By default, you have full operation permissions on the resources under your account. Resource Access Management (RAM) allows you to grant RAM users the access and management permissions on RDS resources owned by an Apsara Stack tenant account. If you do not need to use RAM, ignore this topic.

**Resource types in RAM**

The only type of RDS resources that can be authorized through RAM is dbinstance. The following table lists the resource description method when the resources are authorized through RAM.

| Resource | Resource description in authorization policy |
|---|---|
| Instance | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid acs:rds:$regionid:$accountid:dbinstance/ acs:rds:::dbinstance/ |

The $regionid field must be the ID of a region or an asterisk (*). The $instanceid field must be the ID of an instance or an asterisk (*). Similarly, $account-id is the numerical ID of your Apsara Stack tenant account, which can be replaced by an asterisk (*).

**Authorization operations in RAM**

In RAM, the following operations can be authorized to an RDS resource.

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
|---|---|
| DescribeSlowLogRecords | DescribeErrorLogs |
| DescribeBinlogFiles | DescribeSQLLogReports |
| DescribeSQLLogRecords | DescribeOptimizeAdviceOnStorage |
| DescribeOptimizeAdviceOnMissPK | DescribeOptimizeAdviceOnExcessIndex |

**Note**

All operations except DescribeRegions and DescribeParameterTemplates can be authorized.

**RAM authentication rules of API operations**

When you call API operations to access resources as a RAM user, the RDS backend checks whether the RAM user is granted the required permissions by querying RAM. The permissions to be checked are determined by the resources used by the API operation. The following table lists the authentication rules for each API operation.

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
|---|---|
| DescribeSQLLogRecords | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| DescribeOptimizeAdviceOnMissPK | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
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

| ModifyeParameter | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
|---|---|

### 1.13 Appendix

#### 1.13.1 Client error codes

##### 1.13.1.1 Common errors

| Error code | Description | HTTP status code |
|---|---|---|
| MissingParameter | The input parameter "parameter name" that is mandatory for processing this request is not supplied. | 400 |
| InvalidParameter | The specified parameter "Action or Version" is not valid. | 400 |
| InvalidAccessKeyId.NotFo und | The Access Key ID provided does not exist in our records. | 404 |
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
| Forbidden.InstanceNotFo und | The specified Instance is not found. | 404 |
| Forbidden.RAM | User not authorized to operate on the specified resource, or this API doesn't support RAM. | 403 |
| Forbedden.NotSupportRA M | This action does not support accessed by RAM mode. | 403 |
| Forbidden.RiskControl | This operation is forbidden by Aliyun Risk Control system. | 403 |
| InsufficientBalance | Your account does not have enough balance. | 400 |

| Forbidden.Authentication | This operation is forbidden by Aliyun Realname Authentication system. | 403 |
|---|---|---|
| Invalid<parameter name>.ValueNotSupport ed | The specified parameter "parameter name" is not valid. | 400 |
| Invalid<parameter name>.Malformed | The specified parameter "parameter name n" is not valid. | 400 |
| InvalidParameter | The specified parameter " parameter name n " is not valid. | 400 |

##### 1.13.1.2 Specific errors

| Error code | Error message | HTTP status code |
|---|---|---|
| InvalidRegionId.NotFound | The DBInstanceId provided does not exist in our records. | 404 |
| InvalidSecurityIPList.Duplicate | The Security IP address is not in the available range or occupied. | 400 |
| InvalidSecurityIPListLength.Malform ed | The quota of security ip exceeds. | 400 |
| InvalidEngineVersionInRegion.NotAv ailable | The EngineVersion in the Region is not available. | 403 |
| InvaildEngineInRegion.NotAvailable | The Engine in the Region is not available. | 403 |
| InvaildDBInstanceClassInRegion.Not Available | The DBInstanceClass in the Region is not available. | 403 |
| OperationDenied | The resource is out of usage. | 403 |
| RegionUnauthorized | There is no authority to create instance in the specified region. | 403 |
| QuotaExceeded.CreateInstance | The quota of create instance exceeds. | 403 |
| InvalidDBInstanceId.NotFound | The DBInstanceId provided does not exist in our records. | 404 |
| MissingParameter | The input parameters "DBInstanceClass" and "DBInstanceStorage" all blank or no change. | 400 |
| OperationDenied.DBInstanceType | The operation is not permitted due to type of instance. | 400 |
| OperationDenied.DBInstanceStorag eReduce | The operation is not permitted due to reduce storage. | 403 |
| OperationDenied.DBInstanceStatus | The operation is not permitted due to instance status. | 403 |

| DependencyViolation | The operation is not permitted due to instance mount read only or guard instance. | 403 |
|---|---|---|
| InvalidConnectionStringPrefix.Dupli cate | The connection string is not in the available range or occupied. | 400 |
| QuotaExceeded.SwitchTime | The quota of switch time exceed. | 400 |
| OperationDenied.LockMode | The operation is not permitted due to lock of instance. | 403 |
| InvalidSecurityIps.Duplicate | The quota of security ip exceeds. | 400 |
| OperationDenied.CurrentEngineVer sion | The operation is not permitted due to specified current version. | 400 |
| OperationDenied.ReadOnlyDBInstan ceLower | The operation is not permitted due to higher read only instance version. | 403 |
| OperationDenied.GuardDBInstanceL ower | The operation is not permitted due to higher guard instance version. | 403 |
| OperationDenied.MasterDBInstance State | The operation is not permitted due to status of master instance. | 403 |
| QuotaExceeded.DBName | The quota of db exceeds. | 400 |
| InvalidDBName.Duplicate | The Security db Name is not in the available range or occupied. | 400 |
| InvalidParameter.Keyword | The specified parameter "DBName" is keyword | 400 |
| OperationDenied.DBStatus | The operation is not permitted due to status of database. | 403 |
| OperationDenied.DBInstanceEngine | The operation is not permitted due to engine of instance. | 403 |
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
|---|---|---|
| InvalidTaskId.NotFound | The ImportId provided does not exist in our records. | 400 |
| OperationDenied.IncorrectTaskStat us | The operation is not permitted due to status of import. | 403 |
| InvalidAccountName.keyword | The specified parameter "AccountName" is a keyword. | 400 |
| InvalidAccountName.Duplicate | The Security db Name is not in the available range or occupied. | 400 |
| QuotaExceeded.AccountName | The quota of account exceeds. | 403 |
| OperationDenied.AccountStatus | The operation is not permitted due to status of account. | 403 |
| InvalidDBName.NotFound | The DBName provided does not exist in our records. | 404 |
| OperationDenied.AccountType | The operation is not permitted due to type of account. | 403 |
| OperationDenied.BackupJobExists | The operation is not permitted due to backup job exist. | 403 |
| OperationDenied.NoDatabase | The operation is not permitted due to no database. | 403 |
| InvalidStartTimeAndEndTime.Malfor med | The end time must be greater than the start time | 400 |
| OperationDenied.BackupJobExists | The operation is not permitted due to backup job exist. | 403 |
| InvalidBackupId.NotFound | The BackupId provided does not exist in our records. | 404 |
| OperationDenied.NotFoundBackup | The operation is not permitted due to no backup. | 403 |
| OperationDenied.BackupStatus | The operation is not permitted due to type of backup. | 403 |
| OperationDenied.BackupMethod | The operation is not permitted method of backup. | 403 |
| OperationDenied.TempDBInstanceE xists | The operation is not permitted due to temp instance exist. | 403 |
| Forbidden.Authentication | The operation is forbidden by Aliyun Realname Authentication System. | 403 |
| IncorrectDBInstanceConnType | Current DB instance conn type does not support this operation. | 404 |
| IncorrecttVpcId.Mismatch | The specified parameter "VpcId" is not valid. | 400 |

| IntranetNetTypeNotExists | Current DB instance net type does not support this operation. | 404 |
|---|---|---|
| InvalidDBInstanceName.NotFound | The DBInstanceId provided does not exist in our records. | 403 |
| InvalidConnectionMode.ValueNotSu pported | The specified parameter "ConnectionMode" is not valid. | 400 |
| InvalidConnectionString.Duplicate Specified | connection string already exists in the Aliyun RDS. | 403 |
| InvalidConnectionString.Duplicate Specified | connection string or port want to be modified is the same with current net type. | 400 |
| InvalidConnectionStringPrefix.Dupli cated | Specified connection string already exists in the Aliyun RDS. | 403 |
| InvalidCurrentConnectionString.Not Found | Specified current connection string doesn't exist. | 400 |
| InvalidDBInstanceId.NotFound | The DBInstanceId provided does not exist in our records. | 400 |
| InvalidDBInstanceId.QuotaExceeded | The quota of instance id exceeds. | 400 |
| InvalidDBInstanceNetType.NotFoun d | The Specified DB instance net type is not found. | 404 |
| InvalidDBinstanceNetType.ValueNot Support | The specified parameter "DBinstanceNetType" is not valid. | 400 |
| InvalidDBInstanceType.ValueNotSu pport | The specified parameter "DBInstanceType" is not valid. | 400 |
| InvalidEngineVersion.Malformed | The specified parameter "EngineVersion" is not valid. | 400 |
| InvalidInstanceNetworkType.ValueN otSupported | The specified parameter "InstanceNetworkType" is not valid. | 400 |
| InvalidParameter | The specified parameter "dbInstanceId" is not valid. | 400 |
| InvalidPort.Malformed | Specified port is not valid. | 400 |
| InvalidPrivateIpAddress.Duplicated | Specified private IP address is duplicated. | 400 |
| InvalidPrivateIpAddress.Mismatch | Specified private IP address is not in the CIDR block of virtual switch. | 400 |
| InvalidVPCId.NotFound | Specified virtual vpc is not found. | 400 |
| InvalidVSwitchId.Mismatch | Specified instance and virtual switch are not in the same zone. | 400 |
| InvalidVSwitchId.NotFound | Specified virtual switch is not found in specified VPC. | 400 |
| NetTypeExists | Specified net type already existed. | 400 |

| NetTypeExists | Specified public net type already existed. | 403 |
|---|---|---|
| OperationDenied.DBInstanceNetTyp e | The operation is not permitted due to net type of instance. | 403 |
| OperationDenied.DBInstanceStatus | The operation is not permitted due to status of instance. | 403 |
| OperationDenied.DBInstanceType | The operation is not permitted due to type of instance. | 403 |
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
|---|---|---|
| bpcIzNoNotEqualsRdsMultIzNo | Specified vpc IzNo not equal rds IzNo. | 400 |

#### 1.13.2 Error codes on the server

| Error code | Description | HTTP status code |
|---|---|---|
| ServiceUnavailabl e | The request has failed due to a temporary failure of the server. | 503 |
| InternalError | The request processing has failed due to some unknown error, exception or failure. | 500 |

#### 1.13.3 Instance states

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

#### 1.13.4 Performance parameters

**ApsaraDB RDS for MySQL**

| API parameter | Description |
|---|---|
| MySQL NetworkTraffic _ | The average inbound traffic to a MySQL instance per second and average outbound traffic from a MySQL instance per second. Unit: KB. |
| MySQL QPSTPS _ | The average number of SQL statements executed per second and average number of transactions per second. |
| MySQL Sessions _ | The number of active connections and total number of current connections. |
| MySQL InnoDBBufferRatio _ | The read hit rate of the InnoDB buffer pool, utilization of the InnoDB buffer pool, and percentage of dirty data blocks in the InnoDB buffer pool. |
| MySQL InnoDBDataReadW _ riten | The average volume of data that InnoDB reads per second and average volume of data that InnoDB writes per second. Unit: KB. |
| MySQL InnoDBLogRequest _ s | The average number of reads from the InnoDB buffer pool per second and average number of writes to the InnoDB buffer pool per second. |
| MySQL InnoDBLogWrites _ | The average number of log write requests per second, average number of physical writes to log files per second, and average number of fsync() writes to log files per second. |
| MySQL TempDiskTableCre _ ates | The number of temporary tables automatically created in the hard drive during MySQL statement execution. |
| MySQL MyISAMKeyBufferR _ atio | The average key buffer utilization of MyISAM per second, average key buffer read hit rate of MyISAM per second, and average key buffer write hit rate of MyISAM per second. |
| MySQL MyISAMKeyReadWr _ ites | The average number of data reads from the buffer pool by MyISAM per second, average number of data writes to the buffer pool by MyISAM per second, average number of data reads from the hard disk by MyISAM per second, and average number of data writes to the hard disk by MyISAM per second. |
| MySQL COMDML _ | The average number of DELETE statements executed per second, average number of INSERT statements executed per second, average number of INSERT SELECT statements executed per second, average _ number of REPLACE statements executed per second, and average number of REPLACE SELECT statements executed per second, average _ number of SELECT statements executed per second, and average number of UPDATE statements executed per second. |
| MySQL RowDML _ | The average number of rows read from the InnoDB table per second, average number of rows updated in the InnoDB table per second, average number of rows deleted from the InnoDB table per second, average number of rows inserted into the InnoDB table per second, and average number of physical writes to log files per second. |
| MySQL MemCpuUsage _ | The CPU utilization and memory usage of a MySQL Instance within the entire operating system. |
| MySQL IOPS _ | The IOPS of a MySQL instance. |

| MySQL DetailedSpaceUsag _ e | The disk space occupied by a MySQL instance, including ins size (total _ space), data size (data space), log size (log space), tmp size _ _ _ (temporary space), and other size (system space). _ |
|---|---|
| slavestat | The latency of read-only instances. |

#### 1.13.5 Forbidden keywords

**PolarDB for MySQL**

| Parameter | Keyword description |
|---|---|
| DBName/ AccountName | admin, aurora, replicator, xtrabak, root(MySQL5.5/5.6), mysql, test, eagleye, information schema, guest, add, analyze, asc, between, blob, call, c _ hange,check,condition,continue,cross,current timestamp,database,day micros _ _ econd,dec,default,desc,distinct,double,e ach,enclosed,exit,fetch,float8,foreign,goto,having,hour minute,ignore,infile,inse _ nsitive,int1,int4,interval,iterate,keys,lea ding,like,lines,localtimestamp,longblob,low priority,mediumint,minute microse _ _ cond,modifies,no write to binlog,on, _ _ _ optionally,out,precision,purge,read,references,rename,require,revoke,schema,s elect,set,spatial,sqlexception,sql big re _ _ sult,ssl,table,tinyblob,to,true,unique,update,using,utc timestamp,varchar,when, _ with,xor,all,and,asensitive,bigint,both,c ascade,char,collate,connection,convert,current date,current user,databases,da _ _ y minute,decimal,delayed,describe,dis _ tinctrow,drop,else,escaped,explain,float,for,from,grant,high priority,hour secon _ _ d,in,inner,insert,int2,int8,into,join,kill,le ave,limit,load,lock,longtext,match,mediumtext,minute second,natural,null,opti _ mize,or,outer,primary,raid0,reads,regex p,repeat,restrict,right,schemas,sensitive,show,specific,sqlstate,sql calc found r _ _ _ ows,starting,terminated,tinyint,trailing, undo,unlock,usage,utc date,values,varcharacter,where,write,year month,alter, _ _ as,before,binary,by,case,character,colu mn,constraint,create,current time,cursor,day hour,day second,declare,delete, _ _ _ deterministic,div,dual,elseif,exists,false, float4,force,fulltext,group,hour microsecond,if,index,inout,int,int3,integer,is,key _ ,label,left,linear,localtime,long,loop,me diumblob,middleint,mod,not,numeric,option,order,outfile,procedure,range,real,r elease,replace,return,rlike,second mi _ crosecond,separator,smallint,sql,sqlwarning,sql small result,straight join,then,t _ _ _ inytext,trigger,union,unsigned,use,utc _ time,varbinary,varying,while,x509,zerofill,galaxy |

DK reference

## 2 SDK reference

### 2.1 Obtain the SDK source code

You can use SDK tools to customize SDK for a specific programming language.

**Prerequisites**

The URL of the Apsara Stack Operations Console is obtained. The URL is in the format of http://${region-id}.aso.${intranet-domain-id}.com. A web browser is available. We recommend that you use Google Chrome.

**Procedure**

1. Log in to the Apsara Uni-manager Operations Console.
i. In the address bar of the web browser, enter the URL of the Apsara Uni-manager Operations Console: http://${region-id}.aso.${intranet-domain-id}.com. Then, press the Enter key. ii. On the login page, enter your username and password. iii. Click **Log On** to access the **Apsara Uni-manager Operations Console** .
2. Log in to the Apsara ASAPI Management platform. In the left-side navigation pane, click
**Products > Opsapi** to log in to the **Apsara ASAPI Management platform**.
3. Download the SDK source code.
DK reference i. In the left-side navigation pane, choose **Versions > SDK Tools**. ii. Click **Customize SDK** in the upper-right corner. iii. In the **Customize Apsara Stack SDK** dialog box that appears, select an Apsara Stack version, a service name, a service version, an SDK version, an API version, and an SDK language. iv. After you complete the configuration, click **Create SDK**. v. Click **Download** to download the SDK.

### 2.2 SDK for Java

#### 2.2.1 Use the SDK

##### 2.2.1.1 Use CommonRequest

If no SDK is provided for the service API that you want to call, you can use CommonRequest to make API requests. You can use CommonRequest to call any API operations.

**Features**

CommonRequest has the following features:
1. Lightweight: You only need to download the core package. You do not need to download
and install the service SDKs.
2. Easy to use: You can call the latest API operations without the need to update the SDKs.
3. Fast iteration.

**Use CommonRequest**

To use CommonRequest to initiate a request, you need to set the following parameters. You can obtain the values of the following parameters from the API documentation: domain: the endpoint of the service. version: the version of the API. It is in the YYYY-MM-DD format. DK reference You can obtain the version of the API from the common parameters in the API documents of services. Operation: the operation that you want to perform. You need to obtain the **Action** parameter, and specify the operation in `request.ApiName =`

```
"<Action>" .
```

For example, to initiate a CommonRequest request for RunInstances, use `request.ApiName`

```
= "RunInstances" .
```

You must obtain the value of the **PathPattern** parameter, and use `request.PathPattern =` `"<PathPattern>"` to specify the RESTful path. For example, the **PathPattern** parameter of the API operation for querying all cluster instances is set to `/clusters` . When you initiate a CommonRequest request, you must specify the RESTful path by using `request.PathPattern = "/clusters"` .

**Example: Call an RPC API operation**

The following sample code shows how to use the CommonRequest method to call DescribeDBInstanceAttribute:

```java
import com.aliyuncs.CommonRequest; import com.aliyuncs.CommonResponse; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.exceptions.ServerException; import com.aliyuncs.profile.DefaultProfile; public class Sample {
    public static void main(String[] args) {
        // Create a DefaultAcsClient instance and initialize it.
        DefaultProfile profile = DefaultProfile.getProfile(
            "<your-region-id>", // The region ID.
            "<your-access-key-id>", // The AccessKey ID.
            "<your-access-key-secret>"); // The AccessKey secret.
        IAcsClient client = new DefaultAcsClient(profile);
        // Create an API request and configure its parameters.
        CommonRequest request = new CommonRequest();
        request.setDomain("rm-xxxxx.xxx.com");
        request.setVersion("2014-05-26");
        request.setAction("DescribeDBInstanceAttribute");
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

`}` `}` `}` DK reference

**Example: Call a RESTful API operation**

The following sample code shows how to use the CommonRequest method to call the API operation to list all cluster instances:

```java
import com.aliyuncs.CommonRequest; import com.aliyuncs.CommonResponse; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.exceptions.ServerException; import com.aliyuncs.profile.DefaultProfile; public class Sample {
    public static void main(String[] args) {
        // Create a DefaultAcsClient instance and initialize it.
        DefaultProfile profile = DefaultProfile.getProfile(
            "<your-region-id>", // The region ID.
            "<your-access-key-id>",      // The AccessKey ID.
            "<your-access-key-secret>"); // The AccessKey secret.
        IAcsClient client = new DefaultAcsClient(profile);
        // Create an API request and configure its parameters.
        CommonRequest request = new CommonRequest();
        request.setDomain("rm-xxxxx.xxx.com");
        request.setVersion("2015-12-15");
        request.setUriPattern("/clusters");
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

### 2.3 SDK for Python

#### 2.3.1 Use the SDK

##### 2.3.1.1 Use CommonRequest

If no SDK is provided for the service API that you want to call, you can use CommonRequest to make API requests. You can use CommonRequest to call any API operations.

**Characteristics of CommonRequest calling**

The CommonRequest calling method has the following characteristics: Light weight: You only need the core package to initiate the call, without downloading or installing the SDK of each product. DK reference Easy and convenient: You can call the latest API without updating the SDK. Fast iteration

**Use CommonRequest**

To initiate a CommonRequest request, you must obtain the values of the following parameters. You can obtain the values of these parameters from the API document of each product. Domain: the service address of a product Version: the version of the API, which is in the format of YYYY-MM-DD You can obtain the API version from the common parameters in the API document of each product. API information: the name of the API to be called. You must obtain the value of the **Action** parameter and use `request.ApiName = "` `<Action>"` to specify the API name. Take the RunInstances API as an example. You must use `request.ApiName =` `"RunInstances"` to specify the API name when initiating a CommonRequest request. You must obtain the value of the **PathPattern** parameter and use `request.PathPattern =` `"<PathPattern>"` to specify the RESTful path. For example, if the **PathPattern** value of the GetClusterList API is `/clusters` , you must use `request.PathPattern = "/clusters"` to specify the RESTful path when initiating a CommonRequest request.

**Example: Call an RPC API operation**

The following sample code shows how Python 2.x uses the CommonRequest method to call DescribeDBInstanceAttribute:

```bash
from aliyunsdkcore.client import AcsClient from aliyunsdkcore.request import CommonRequest client = AcsClient('{your_access_key_id}', '{your_access_key_secret}', '{your_region_id}') request = CommonRequest() request.set_domain('rm-xxxxx.xxx.com') request.set_version('2014-05-26') request.set_action_name('DescribeDBInstanceAttribute')
# or:
# request = CommonRequest(domain='rds.aliyuncs.com', version='2014-05-26',
action_name='DescribeDBInstanceAttribute') request.add_query_param('PageNumber', '1') request.add_query_param('PageSize', '30') response = client.do_action_with_exception(request)
```

**Example: Call a RESTful API operation**

The following sample code shows how Python 2.x uses the CommonRequest method to call the operation to list all cluster instances: DK reference

```bash
from aliyunsdkcore.client import AcsClient from aliyunsdkcore.request import CommonRequest client = AcsClient('{your_access_key_id}', '{your_access_key_secret}', '{your_region_id}') request = CommonRequest() request.set_domain('rm-xxxxx.xxx.com') request.set_version('2015-12-15') request.set_uri_pattern('/clusters')
# or:
# request = CommonRequest(domain='rds.aliyuncs.com', version='2014-05-26',
uri_pattern='/clusters') response = client.do_action_with_exception(request)
```

### 2.4 SDK for PHP

#### 2.4.1 Quick start

### 2.5 SDK for C#

**Environment preparations**

framework 2.0+

**Download link**

Download the source code of SDK for C# from https://github.com/aliyun/aliyun-openapi-netsdk.

**Install the SDK**

1. Compile the source code of SDK for C# into a DLL file.
2. Right-click your Visual Studio project and choose **Add Reference > Browse**. If you are
using MonoDevelop, follow the MonoDevelop instructions to import the DLL file.
3. Select the DLL file and click **OK**. Then, you can use SDK for C# in your project.

## 3 Obtain an endpoint

You can obtain the endpoint of PolarDB for MySQL V2.0 in the Apsara Uni-manager Operations Console.

**Method 1**

1. Log on to the Apsara Stack Operations console.
For more information about how to log on to the console, see **Operations and**
**Maintenance Guide.** Specifically, navigate in the guide as follows: **Operations of basic**
**platforms > Apsara Stack Operations (ASO) > Log on to Apsara Stack Operations** .
2. In the left-side navigation pane, choose **Products > Product List > Apsara Stack O&M**.
3. Click **Apsara Infrastructure Management Framework** to go to the Apsara
Infrastructure Management Framework console.
4. In the top navigation bar, choose **Reports > System Reports**.
5. On the **System Reports** page, click **Registration Vars of Services**.
6. On the **Registration Vars of Services** page, find the polardb-yaochi row, right-click the
**Service Registration** column, and select **Show More** from the shortcut menu.
7. In the **Details** dialog box, find the endpoint of PolarDB based on the key value of PolarDB,
which is polardb.openapi.endpoint.

**Method 2**

1. Log on to Apsara Stack Operations.
For how to log on to Apsara Stack Operations, see **Operations of basic platforms >**
**Apsara Stack Operations > Log on to Apsara Stack Operations** in **Operations**
**Guide** .
2. Click **Products** in the left-side navigation pane.
3. Choose **Apsara Infrastructure Management Framework** in the product list to go to the
Apsara Infrastructure Management Framework page.
4. Choose **Operations > Machine Operations**. The **Machine Operations** page appears.
5. Select a machine and then click **Terminal** to log on to the machine.
6. Run the command **curl -l**

**"http://127.0.0.1:7070/api/v3/column/c.sr.service_registration,c.sr.id?**

**c.sr.service_registration"** to obtain JSON data.
7. Find the endpoint of PolarDB based on the service ID (polardb-yaochi) and key value (polard
b.openapi.endpoint) of PolarDB.

## 4 Obtain an AccessKey pair

You can obtain an AccessKey pair in the Apsara Uni-manager Management Console.

**Obtain the AccessKey pair of an organization**

To obtain the AccessKey pair of an organization, perform the following operations:
1. Log on to the ASCM console as an administrator.
2. In the top navigation bar, click **Enterprise**.
3. In the left-side navigation pane of the **Enterprise** page, click **Organizations**.
4. In the Organizations structure, click the
icon on the right of the organization to be added.
5. Choose **AccessKey** from the shortcut menu.
6. In the AccessKey dialog box that appears, view the AccessKey pair of the organization.

**Note**

An AccessKey pair is automatically allocated to a level-1 organization. Subordinate organizations use the same AccessKey pair as their level-1 organization.

**Obtain the AccessKey pair of a personal account**

To obtain the AccessKey pair of a personal account, perform the following operations:
1. Log on to the ASCM console as an administrator.
2. In the upper-right corner of the homepage, move the pointer over the user profile picture
and click **User Information**.
3. In the **Apsara Stack AccessKey Pair** section of the User Information page, view your
AccessKey pair.

**Note**

The AccessKey pair is made up of the AccessKey ID and AccessKey secret. These credentials provide you full permissions on Apsara Stack resources. You must keep the AccessKey pair confidential.
