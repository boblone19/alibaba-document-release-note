---
title: "ApsaraDB for POLARDB PolarDB for PostgreSQL (Primary_Secondary Edition) Developer Guide 20260630"
product_version: "V3.18.6"
pdf_pages: 158
source_pdf: "d51fbfeb3e3ce88d_Alibaba Cloud Apsara Stack V3.18.6 ApsaraDB for POLARDB PolarDB for PostgreSQL (Primary_Secondary Ed"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/v3.18.6%E7%89%88%E6%9C%AC%E6%96%87%E6%A1%A3/PolarDB%20PG%E6%9C%AC%E5%9C%B0%E7%9B%98/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.6%20ApsaraDB%20for%20POLARDB%20PolarDB%20for%20PostgreSQL%20%28Primary_Secondary%20Edition%29%20Developer%20Guide%2020260630.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings)
---

# ApsaraDB for POLARDB PolarDB for PostgreSQL (Primary_Secondary Edition) Developer Guide 20260630

## Table of Contents

- 1 API reference
  - 1.1 API overview
  - 1.2 Make API requests
    - 1.2.1 Request structure
    - 1.2.2 Common parameters
      - 1.2.2.1 Common request parameters
      - 1.2.2.2 Common response parameters
    - 1.2.3 Responses
      - 1.2.3.1 Sample success responses
      - 1.2.3.2 Sample error responses
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
    - 1.3.20 ModifyDBInstanceDescription
    - 1.3.21 ModifyDBInstanceMaintainTime
    - 1.3.22 ModifyDBInstanceHAConfig
    - 1.3.23 SwitchDBInstanceHA
    - 1.3.24 CreateReadOnlyDBInstance
    - 1.3.25 DescribeDBInstanceSSL
    - 1.3.26 ModifyDBInstanceSSL
    - 1.3.27 DescribeDBInstanceTDE
    - 1.3.28 ModifyDBInstanceTDE
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
    - 1.6.6 Query available point-in-time recovery range
    - 1.6.7 ModifyBackupPolicy
    - 1.6.8 RestoreDBInstance
    - 1.6.9 DeleteBackup
  - 1.7 Plugin management
    - 1.7.1 Uninstall a plugin
    - 1.7.2 Update a plugin
    - 1.7.3 Query details of a plugin
    - 1.7.4 Install plugins
  - 1.8 Monitoring management
    - 1.8.1 DescribeResourceUsage
    - 1.8.2 DescribeDBInstancePerformance
    - 1.8.3 DescribeDBInstanceMonitor
    - 1.8.4 ModifyDBInstanceMonitor
  - 1.9 Parameter management
    - 1.9.1 DescribeParameterTemplates
    - 1.9.2 DescribeParameters
    - 1.9.3 ModifyParameter
  - 1.10 Log management
    - 1.10.1 DescribeSlowLogs
    - 1.10.2 DescribeSlowLogRecords
    - 1.10.3 DescribeErrorLogs
    - 1.10.4 DescribeSQLCollectorPolicy
    - 1.10.5 ModifySQLCollectorPolicy
    - 1.10.6 DescribeSQLLogRecords
    - 1.10.7 DescribeSQLLogFiles
  - 1.11 Data migration
    - 1.11.1 CreateUploadPathForSQLServer
    - 1.11.2 ImportDatabaseBetweenInstances
    - 1.11.3 CancelImport
  - 1.12 Tag management
    - 1.12.1 AddTagsToResource
    - 1.12.2 DescribeTags
    - 1.12.3 RemoveTagsFromResource
  - 1.13 RAM authorization
  - 1.14 Appendix
    - 1.14.1 Client error codes
      - 1.14.1.1 Common errors
      - 1.14.1.2 Specific errors
    - 1.14.2 Error codes on the server
    - 1.14.3 Instance states
    - 1.14.4 Character set tables
- 2 SDK reference
  - 2.1 Obtain the SDK source code
  - 2.2 SDK for Java
    - 2.2.1 Use the SDK
      - 2.2.1.1 Use CommonRequest to call API operations
  - 2.3 SDK for Python
    - 2.3.1 Use the SDK
      - 2.3.1.1 Use CommonRequest to call API operations
  - 2.4 SDK for PHP
    - 2.4.1 Getting started
  - 2.5 SDK for C#
- 3 Obtain an endpoint
- 4 Obtain an AccessKey pair

## 1 API reference

### 1.1 API overview

The following tables list the API operations available for use in PolarDB.

**PolarDB instance management**

| API | Description |
|---|---|
| CreateDBInstance | Creates an instance. |
| DeleteDBInstance | Releases an instance. |
| RestartDBInstance | Restarts an instance. |
| DescribeDBInstanceAttribute | Views instance attributes. |
| DescribeDBInstances | Queries the list of instances. |
| ModifyDBInstanceSpec | Modifies the configurations of an instance. |
| AllocateInstancePublicConnection | Allocates a public endpoint for an instance. |
| ReleaseInstancePublicConnection | Releases the public endpoint of an instance. |
| SwitchDBInstanceNetType | Allocates an internal endpoint for an instance. |
| DescribeDBInstanceNetInfo | Queries the connection information of an instance. |
| ModifyDBInstanceConnectionString | Modifies the endpoint and port of an instance. |
| ModifyDBInstanceConnectionMode | Changes the access mode of a PolarDB instance. |
| ModifyDBInstanceNetworkType | Changes the network type of a PolarDB instance. |
| DescribeDBInstanceIPArrayList | Queries the IP address whitelist of a PolarDB instance. |

| ModifySecurityIps | Modifies the IP address whitelist of a PolarDB instance. |
|---|---|
| DescribeRegions | Queries available regions and zones. |
| DescribeDBInstanceHAConfig | Queries the zone information and data replication status of a PolarDB instance. |
| MigrateToOtherZone | Migrates a PolarDB instance from one zone to another zone. |
| PurgeDBInstanceLog | Clears logs of a PolarDB instance. |
| UpgradeDBInstanceEngineVersion | Upgrades the database version of a PolarDB instance. |
| ModifyDBInstanceDescription | Modifies the description of a PolarDB instance. |
| ModifyDBInstanceMaintainTime | Modifies the maintenance window of a PolarDB instance. |
| ModifyDBInstanceHAConfig | Modifies the data replication mode and high availability switching rules of a PolarDB instance. |
| SwitchDBInstanceHA | Switches between the primary and secondary PolarDB instances. |
| CreateReadonlyDBInstance | Creates a read-only PolarDB instance. |
| DescribeDBInstanceSSL | Queries the SSL connection of an instance. |
| ModifyDBInstanceSSL | Modifies the SSL connection of an instance. |

**PolarDB database management**

| API | Description |
|---|---|
| CreateDatabase | Creates a database. |
| DeleteDatabase | Deletes a database. |

| DescribeDatabases | Queries the list of databases. |
|---|---|
| ModifyDBDescription | Modifies the description of a database. |

**PolarDB account management**

| API | Description |
|---|---|
| CreateAccount | Creates an account. |
| DeleteAccount | Deletes an account. |
| DescribeAccounts | Queries the list of accounts. |
| GrantAccountPrivilege | Grants permissions to an account. |
| RevokeAccountPrivilege | Revokes permissions from an account. |
| ModifyAccountDescription | Modifies the description of an account. |
| ResetAccountPassword | Resets the password of an account. |
| ResetAccount | Resets the account. |

**PolarDB backup and restoration**

| API | Description |
|---|---|
| CreateBackup | Creates a backup. |
| CloneDBInstance | Clones a PolarDB instance. |
| DescribeBackups | Queries the list of backups. |
| CreateTempDBInstance | Creates a temporary instance. |
| DescribeBackupPolicy | Queries the backup policy configured for an instance. |

| DescribeLocalAvailableRecoveryTime | Queries the recoverable time range for backups. |
|---|---|
| ModifyBackupPolicy | Modifies the backup policy configured for an instance. |
| RestoreDBInstance | Restores an instance from a backup set. |
| DeleteBackup | Deletes the data backup files of an instance. |

**PolarDB plugin management**

| API | Description |
|---|---|
| CreateExtensions | Installs a plugin. |
| DescribeExtensions | Queries the details of a plugin. |
| UpdateExtensions | Updates a plugin. |
| DeleteExtensions | Uninstalls a plugin. |

**PolarDB monitoring management**

| API | Description |
|---|---|
| DescribeResourceUsage | Queries the resource usage of an instance. |
| DescribeDBInstancePerformance | Queries the performance metrics of an instance. |
| DescribeDBInstanceMonitor | Queries the monitoring settings of an instance. |
| ModifyDBInstanceMonitor | Modifies the monitoring settings of an instance. |

**PolarDB parameter management**

| API | Description |
|---|---|
| DescribeParameterTemplates | Queries the list of database parameter templates. |

| DescribeParameters | Queries the parameter settings of an instance. |
|---|---|
| ModifyParameter | Modifies the parameters of an instance. |

**PolarDB log management**

| API | Description |
|---|---|
| DescribeSlowLogs | Queries the list of slow query logs. |
| DescribeSlowLogRecords | Queries the details of slow query logs. |
| DescribeErrorLogs | Queries error logs. |
| DescribeBinlogFiles | Queries binlogs. |
| DescribeSQLCollectorPolicy | Checks whether the SQL audit feature is enabled. |
| ModifySQLCollectorPolicy | Enables or disables the SQL audit feature. |
| DescribeSQLLogRecords | Queries SQL audit logs. |
| DescribeSQLLogFiles | Queries the list of SQL audit log files. |

**PolarDB data migration**

| API | Description |
|---|---|
| ImportDatabaseBetweenInstances | Migrates data from an instance. |
| CancelImport | Cancels the migration from an instance. |

**PolarDB tag management**

| API | Description |
|---|---|
| AddTagsToResource | Adds tags. |

| DescribeTags | Queries tags. |
|---|---|
| RemoveTagsFromResource | Removes tags. |

### 1.2 Make API requests

#### 1.2.1 Request structure

This topic describes the request structure of the PolarDB API.

**Endpoints**

The endpoint of the PolarDB API is polardb.example.com. For more information about how to obtain the endpoint, see Obtain the endpoint of ASAPI.

**Protocols**

You can send API requests over HTTP or HTTPS. We recommend that you use HTTPS for enhanced security.

**Methods**

You can use the HTTP GET method to send API requests. When you use this method, you must include request parameters in the request URL.

**Parameters**

In each request, you must set the Action parameter to specify the operation that you want to perform, such as CreateDatabase. You must also specify common request parameters and operation-specific parameters.

**Encoding**

Requests and responses are both encoded in UTF-8.

#### 1.2.2 Common parameters

##### 1.2.2.1 Common request parameters

Common request parameters must be included in all PolarDB API requests.

| Parameter | Typ e | Requi red | Description |
|---|---|---|---|
| Format | Stri ng | No | The format in which to return the response. Valid values: JSON and XML. Default value: XML. |
| Version | Stri ng | Yes | The version number of the API. Specify the version number in the YYYY-MM-DD format. Set the value to 2024-01-30. |

| AccessKeyId | Stri ng | Yes | The AccessKey ID provided to you by Apsara Stack. |
|---|---|---|---|
| Signature | Stri ng | Yes | The signature string of the current request. For more information about how signatures are calculated, see Request signatures. |
| SignatureMet hod | strin g | Yes | The encryption method of the signature string. Set the value to HMAC-SHA1. |
| Timestamp | Stri ng | Yes | The timestamp of the request. Specify the time in the ISO 8601 standard in the YYYY-MM-DDThh:mm:ssZ format. The time must be in UTC. For example, 2013-08-15T12:00:00Z specifies August 15, 2013, 20:00:00 (UTC+8). |
| SignatureVer sion | Stri ng | Yes | The version of the signature encryption algorithm. Set the value to 1.0. |
| SignatureNo nce | Stri ng | Yes | A unique, random number used to prevent replay attacks. You must use different numbers for different requests. |

**Examples**

```
https://polardb.example.com/ ?Format=xml &Version=2024-01-30 &Signature=Pc5WB8gokVnxxxxx &SignatureMethod=HMAC-SHA1 &SignatureNonce=15215528852396 &SignatureVersion=1.0 &AccessKeyId=key-test &OwnerId=12345678 &Timestamp=2024-07-12T12:00:00Z
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

```xml
<!—Result root node--> <Operation name + Response> <!—Returned request tag--> <RequestId>4C467B38-****-447D-****-AC04*******16</RequestId> <!—Return result data--> </Operation name + Response>
```

JSON format

```json
{ "RequestId": "4C467B38-****-447D-****-AC04*******16", /* Return result data */}
```

##### 1.2.3.2 Sample error responses

If an error occurs when you call an API operation, no result data is returned. You can identify the cause of the error by referring to the error codes in Appendix. If an error occurs when you call an API operation, a 4XX or 5XX HTTP status code is returned. The returned message contains the specific error code and error message. The RequestId parameter uniquely identifies the request, and the HostId parameter indicates the ID of the site requested to be accessed. You can contact Apsara Stack technical support if the cause of the error cannot be found. We recommend that you provide the HostId and RequestId parameters to help technical support engineers resolve the issue at the earliest opportunity. XML format

```xml
<Error> <RequestId>8906582E-****-****-A6C4-0E78*******5</RequestId> <HostId>polardb.example.com</HostId> <Code>UnsupportedOperation</Code> <Message>The specified action is not supported.</Message> </Error>
```

JSON format

```json
{ "RequestId": "7463B73D-****-4D19-****-6B8*******2EF", "HostId": "polardb.example.com", "Code": "UnsupportedOperation", "Message": "The specified action is not supported."
```

`}`

### 1.3 Instance management

#### 1.3.1 CreateDBInstance

Creates a PolarDB instance. For more information about instance types, see Instance types in Appendix.

| Parameter | Type | Requir ed | Description |
|---|---|---|---|
| Action | Strin g | Yes | The operation that you want to perform. Set the value to CreateDBInstance. |
| RegionId | Strin g | Yes | The region ID of the instance. The ID can be up to 50 characters in length. You can call the DescribeRegions operation to query the most recent region list. |
| ZoneId | Strin g | No | The zone ID of the instance. You can call the DescribeRegions operation to query the most recent zone list. |
| Engine | Strin g | Yes | The database engine of the instance. Set the value to PolarDB PG. _ |
| EngineVersion | Strin g | Yes | The PolarDB PG database version of the instance. Valid _ values: 14 16 |
| DBInstanceClass | Strin g | Yes | The instance type of the instance. |

| DBInstanceStora ge | Integ er |   | Yes | The storage capacity of the instance. Valid values: MySQL High-availability Edition: 5 to 2000 PolarDB High-availability Edition: 5 to 2000 The capacity must be incremented by 5 GB. Unit: GB. |   |
|---|---|---|---|---|---|
| DBInstanceNetT ype | Strin g |   | Yes | The network connection type of the instance. Valid values: Internet Intranet |   |
| DBInstanceDescr iption | Strin g |   | No | The description of the instance, which is used to describe the purpose of the instance. The description must be 2 to 256 characters in length and cannot start with http:// or https:// . It must start with a letter and can contain letters, digits, underscores ( ), and hyphens (-) . _ |   |
|   |   |   |   |   | letters, digits, |
|   |   |   |   | underscores ( ), and hyphens (-) _ |   |
| SecurityIPList | Strin g |   | Yes | The IP addresses that are allowed to access all databases in the instance. You can add a maximum of 1,000 unduplicated IP addresses and separate them with commas (,). Supported formats include %, 0.0.0.0/0, a single IP address (such as 10.23.12.24), and a CIDR block (such as 10.23.12.24/24) with a prefix length ranging from 1 to 32. 0.0.0.0/0 indicates that access sources are not limited. |   |
| ClientToken | Strin g |   | Yes | The client token that is used to ensure the idempotence of the request. |   |
| InstanceNetwork Type | Strin g |   | No | The network type of the instance. Valid values: VPC and Classic. Default value: Classic. |   |
| ConnectionMode | Strin g |   | No | The access mode of the instance. Valid values: Performance and Safety. If no value is specified, the system assigns an access mode. |   |
| VPCId | Strin g |   | No | The virtual private cloud (VPC) ID. |   |
| VSwitchId | Strin g |   | No | The vSwitch ID. |   |
| PrivateIpAddress | Strin g |   | No | The VPC IP address that belongs to the specified vSwitch. If no value is specified, the system assigns a VPC IP address. |   |

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> | - | The common response parameters. |
| DBInstanceId | String | The instance ID. |
| OrderId | String | The order ID. |
| ConnectionString | String | The endpoint used to connect to the instance. |
| Port | String | The port used to connect to the instance. |

**Examples**

XML format

**Sample responses**

```xml
<CreateDBInstanceResponse> <OrderId>100789370******</OrderId> <ConnectionString>rm-5ob3ye******.o.polardb.rds.inter.env17e.shuguang.com </ConnectionString> <DBInstanceId>polardb-****</DBInstanceId> <port>3433</port> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> </CreateDBInstanceResponse>
```

JSON format

```json
{ "OrderId": "100789370******", "ConnectionString": "rm-5ob3ye******.o.polardb.rds.inter.env17e.shuguang.com", "DBInstanceId": "polardb-****", "Port": "3433", "RequestId": "1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC"}
```

#### 1.3.2 DeleteDBInstance

Releases a PolarDB instance. Before you call this operation, make sure that the following requirements are met: The instance is in the Running state. The instance is not manually locked. The instance is a pay-as-you-go primary instance, read-only instance, disaster recovery instance, or temporary instance.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DeleteDBInstance. |
| DBInstanceI d | String | Yes | The instance ID. |

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> | - | The common response parameters. For more information, see Common response parameters. |

**Examples**

**Sample requests**

```
https://polardb.example.com/?Action=DeleteDBInstance &DBInstanceId=polardb-xxxxx &Common request parameters
```

**Sample responses**

XML format

```xml
<DeleteDBInstanceResponse> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> </DeleteDBInstanceResponse>
```

JSON format

```json
{ "RequestId": "1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC" }
```

#### 1.3.3 RestartDBInstance

Restarts an instance. The instance will be restarted in 10 seconds. If a large number of transactions must be submitted or rolled back, the restart process may be delayed for a minute. Before you call this operation, make sure that the following requirements are met: The instance is in use. The instance does not have ongoing backup tasks.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to RestartDBInstance. |
| DBInstanceI d | String | Yes | The instance ID. |

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> | - | The common response parameters. For more information, see Common response parameters. |

**Examples**

XML format

```xml
<RestartDBInstanceResponse> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> </RestartDBInstanceResponse>
```

JSON format

```json
{ "RequestId": "1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC"}
```

#### 1.3.4 DescribeDBInstanceAttribute

Queries the attributes of instances.

| Paramete r | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeDBInstanceAttribute. |
| DBInstanc eId | String | Yes | The instance ID. You can specify up to 30 IDs at a time. Separate multiple IDs with commas (,). |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Items |   |   | The queried instance attributes. |
| DBInstanceId | String | rm-bpvxxxxx | The instance ID. |
| DBInstanceType | String | Primary | The type of the instance. Valid values: Primary: primary instance. Readonly: read-only instance. Guard: disaster recovery instance. Temp: temporary instance. |
| Category | String | Basic | The edition of the instance. Valid values: Basic: Basic Edition. Standard: High-availability Edition. Enterprise: Enterprise Edition. |
| InstanceNetwork Type | String | Classic | The network type of the instance. Valid values: Classic VPC |
| RegionId | String | cn-hangzhou | The region ID. |
| ZoneId | String | cn-hangzhou-a | The zone ID. |
| ConnectionString | String | rm- 5obp******.o.pol ardb.rds.inter.en v17e.shuguang.c om | The endpoint used to connect to the instance. |
| Port | String | 3433 | The port used to connect to the instance. |
| Engine | String | PolarDB PG _ | The database engine of the instance. |
| EngineVersion | String | 16 | The database engine version of the instance. |

| DBInstanceClass Type | String | x | The instance family. Valid values: s: shared instance. x: general-purpose instance. d: dedicated instance. h: dedicated host. |
|---|---|---|---|
| DBInstanceClass | String | polardb.g4.4xlar ge.2 | The instance type of the instance. |
| DBInstanceMemo ry | Long | 240 | The memory capacity of the instance. Unit: MB. |
| DBInstanceStora ge | Integer | 10 | The storage capacity of the instance. Unit: GB. |
| DBInstanceNetTy pe | String | Internet | The network connection type of the instance. Valid values: Internet Intranet |
| DBInstanceStatu s | String | Running | The state of the instance. For more information, see Instance states in Appendix. |
| DBInstanceDescr iption | String | Test instance _ | The description of the instance. |
| LockMode | String | Unlock | The lock mode of the instance. Valid values: Unlock: normal. ManualLock: manually locked. LockByExpiration: automatically locked upon expiration. LockByRestoration: automatically locked before instance rollback. LockByDiskQuota: automatically locked due to full disk space. |
| LockReason | String | No | The reason why the instance is locked. |
| DBMaxQuantity | Integer | 200 | The maximum number of databases that can be created in the instance. |
| AccountMaxQuan tity | Integer | 50 | The maximum number of accounts that can be created in the instance. |

| CreationTime | String | 2025-05- 30T12:11:4Z | The time when the instance was created. Format and example: YYYY-MM-DDThh:mm:ssZ 2025-05-30T12:11:4Z |
|---|---|---|---|
| ExpireTime | String | No | The expiration time of the instance. This parameter is not returned for pay-as-you-go instances. |
| MaintainTime | String | 00:00Z-02:00Z | The maintenance window of the instance. For example, 00:00Z-02:00Z indicates that the instance can be maintained from 00:00 to 02:00. 00:00Z-02:00Z |
| AvailabilityValue | String | 100.0% | The availability status of the instance. Unit: %. |
| MaxIOPS | Integer | 150 | The maximum IOPS. |
| MaxConnections | Integer | 60 | The maximum number of concurrent connections to the instance. |
| MasterInstanceId | String | null | The ID of the primary instance. If the value of this parameter is null, the instance is a primary instance. |
| IncrementSource DBInstanceId | String | null | The instance ID of the incremental data source. For example, the incremental data source of a disaster recovery instance or read-only instance is the primary instance, and the incremental data source of the primary instance is null. |
| GuardDBInstance Id | String | No | The ID of the disaster recovery instance attached to the instance. |
| TempDBInstance Id | String | No | The ID of the temporary instance attached to the instance. |
| ReadOnlyDBInsta nceIds |   | rr-xxxxx | The IDs of the read-only instances attached to the instance. |

| DBInstanceId | String | rm-bpxxxxx | The name of the instance. |
|---|---|---|---|
| VpcCloudInstanc eId | String | vpc-xxxxx | The virtual private cloud (VPC) ID. |
| ResourceGroupId | String | 365378**** | The resource group ID. |
| RequestId | String | 1AD222E9-E606- 4A42-BF6D- 8A4442913CEF | The request ID. |

DBInstanceAttribute parameters

**Note**

You can call the DescribeDBInstanceHAConfig operation to query the information about the primary and secondary instances.

**Examples**

**Sample requests**

```
https://polardb.example.com/?Action=DescribeDBInstanceAttribute &DBInstanceId=polardb-xxxxx &<Common request parameters>
```

JSON format

```json
{ "Items":
    { "DBInstanceAttribute":
        [ { "LockMode": "Unlock",
            "ConnectionString": "rm-
5obp******.o.polardb.rds.inter.env17e.shuguang.com",
            "CreationTime": "2025-05-30T12:11:4Z",
            "DBInstanceNetType": "Internet",
            "ReadOnlyDBInstanceIds": { "ReadOnlyDBInstanceId": [] },
            "MaxConnections": 60,
            "LockReason": "",
            "Engine": "PolarDB_PG",
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
            "EngineVersion": "16",
            "IncrementSourceDBInstanceId": "",
            "GuardDBInstanceId": "",
            "DBInstanceStorage": 10,
            "DBInstanceDescription": "",
            "DBInstanceId": "polardbfnjfquxxxxx",
            "PayType": "Postpaid",
            "ExpireTime": "",
            "MaintainTime": "",
            "DBInstanceClass": "polardb.g4.4xlarge.2",
            "SecurityIPList": "11.11.XX.XX",
            "Port": "3433" } ] },
    "RequestId": "1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC" }
```

JSON format

```json
{ "Code":"UnsupportedOperation", "HostId":"polardb.aliyuncs.com", "Message":"The specified action is not supported.", "RequestId":"1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC"}
```

#### 1.3.5 DescribeDBInstances

Queries a list of instances or Resource Access Management (RAM)-authorized instances.

| Parameter | Type | Requi red | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeDBInst ances | The operation that you want to perform. Set the value to DescribeDBInstances. |
| RegionId | String | Yes | cn-hangzhou | The region ID. |
| ConnectionMode | String | No | Performance | The access mode of the instance. Valid values: Performance: standard access mode. Safety: secure access mode. If no value is specified, instances in both access modes are returned. |
| DBInstanceType | String | No | Primary | The type of the instance. Valid values: Primary: primary instance. Readonly: read-only instance. Guard: disaster recovery instance. Temp: temporary instance. If no value is specified, instances of all types are returned. |
| InstanceNetwork Type | String | No | Classic | The network type of the instance. Valid values: VPC Classic If no value is specified, instances of both network types are returned. |
| PageNumber | Intege r | No | 1 | The page number. Pages start from page 1. Default value: 1. |
| PageSize | Intege r | No | 30 | The number of entries per page. Valid values: 30, 50, and 100. Default value: 30. |
| Tags | String | No | No | The tags of the instance. Specify the value in the JSON format. Each tag is a key-value pair that consists of TagKey and TagValue. You must specify TagKey, and you can specify TagValue as needed. Example: {"key1":"value1"}. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| PageNumber | Integer | 1 | The page number. |
| TotalRecordCount | Integer | 1 | The total number of entries returned. |
| PageRecordCount | Integer | 1 | The number of entries per page. |
| Items |   |   | The queried instances. |
| └DBInstanceId | String | rm-xxxxx | The instance ID. |
| └DBInstanceDescriptio n | String | testforRemark s | The description of the instance. |
| └PayType | String | Postpaid | The billing method of the instance. Valid values: Postpaid: pay-as-you-go. Prepaid: subscription. |
| └ DBInstanceType | String | Primary | The type of the instance. Valid values: Primary: primary instance. Readonly: read-only instance. Guard: disaster recovery instance. Temp: temporary instance. |
| └InstanceNetworkType | String | Classic | The network type of the instance. Valid values: Classic VPC |
| └ConnectionMode | String | Performance | The access mode of the instance. Valid values: Performance: standard access mode. Safety: secure access mode. |
| └RegionId | String | cn-hangzhou | The region ID. |

| └ExpireTime | String | No | The expiration time of the instance. This parameter is not returned for pay-as-you-go instances. |
|---|---|---|---|
| └DBInstanceStatus | String | Intranet | The state of the instance. For more information, see Instance states in Appendix. |
| └Engine | String | PolarDB PG _ | The database engine of the instance. |
| └DBInstanceNetType | String | Internet | The network connection type of the instance. Valid values: Internet Intranet |
| └LockMode | String | Unlock | The lock mode of the instance. Valid values: Unlock: normal. ManualLock: manually locked. LockByExpiration: automatically locked upon expiration. LockByRestoration: automatically locked before instance rollback. LockByDiskQuota: automatically locked due to full disk space. |
| └LockReason | String | No | The reason why the instance is locked. |
| └MasterInstanceId | String | null | The ID of the primary instance. If the value of this parameter is null, the instance is a primary instance. |
| └GuardDBInstanceId | String | No | The ID of the disaster recovery instance attached to the instance. |
| └TempDBInstanceId | String | No | The ID of the temporary instance attached to the instance. |
| └VpcCloudInstanceId | String | vpc-xxxxx | The virtual private cloud (VPC) ID. |
| └ReadOnlyDBInstanceI ds |   |   | None |
| └DBInstanceId | String | rm-xxxxx | The instance ID. |

| RequestId | String | 1AD222E9- E606-4A42- BF6D- 8A4442913CEF | The request ID. |
|---|---|---|---|

**Examples**

**Sample requests**

```
https://polardb.example.com/?Action=DescribeDBInstances &RegionId=cn-hangzhou &Engine=PolarDB_PG &<Common request parameters>
```

XML format

```xml
<DescribeDBInstancesResponse> <PageRecordCount>2</PageRecordCount> <Items> <DBInstance> <DBInstanceDescription>testforRemarks</DBInstanceDescription> <ExpireTime>2014-10-10T16:00:00Z</ExpireTime> <DBInstanceId>polardbmjfirxxxxx</DBInstanceId> <DBInstanceNetType>Internet</DBInstanceNetType> <PayType>Prepaid</PayType> <DBInstanceStatus>Running</DBInstanceStatus> <DBInstanceType>Primary</DBInstanceType> <Engine>PolarDB_PG</Engine> <LockMode>Unlock</LockMode> <LockReason/> <RegionId>cn-hangzhou</RegionId> <ZoneId>cn-hangzhou-a</ZoneId> <MasterInstanceId/> <GuardDBInstanceId/> <TempDBInstanceId/> <ReadOnlyDBInstanceIds> <ReadOnlyDBInstanceId/> </ReadOnlyDBInstanceIds> </DBInstance> </Items> <PageNumber>1</PageNumber> <TotalRecordCount>2</TotalRecordCount> <RequestId>2553A660-E4EB-4AF4-A402-8AFF70A49143</RequestId> </DescribeDBInstancesResponse>
```

JSON format

```json
{ "Items":
    { "DBInstance":
        [ { "DBInstanceDescription":"testforRemarks",
            "DBInstanceId":"polardbmjfirxxxxx",
            "DBInstanceNetType":"Internet",
            "DBInstanceStatus":"Running",
            "DBInstanceType":"Primary",
            "Engine":"PolarDB_PG",
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
{ "Code":"UnsupportedOperation", "HostId":"polardb.aliyuncs.com", "Message":"The specified action is not supported.", "RequestId":"7463B73D-35CC-4D19-A010-6B8D65D242EF"}
```

#### 1.3.6 ModifyDBInstanceSpec

Modifies the configurations of an instance, such as the instance type or storage capacity. Before you call this operation, make sure that the following requirements are met: The instance is in the Running state. The instance does not have ongoing backup tasks. One of the DBInstanceClass and DBInstanceStorage parameters is specified. The new storage capacity is at least 1.1 times the used storage space. The instance is a primary instance or read-only instance.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|

| Action | String | Yes | ModifyDBInstanc eSpec | The operation that you want to perform. Set the value to ModifyDBInstanc eSpec. |
|---|---|---|---|---|
| DBInstanceId | String | Yes | rm-bpxxxx | The instance ID. |
| AccessKeyId | String | No | LTAIKw8gqxxxxx | The AccessKey ID provided to you by Apsara Stack. |
| ClientToken | String | No | ETnLKlblzczshOT UbOCziJZNwHlYB Q | The client token that is used to ensure the idempotence of the request. |
| DBInstanceClass | String | No | polardb.mys2.sm all | The instance type of the instance. For more information about instance types, see Instance types in Appendix. |
| DBInstanceStora ge | Integer | No | 20 | The storage capacity of the instance. Unit: GB. The capacity must be incremented by 5 GB. For more information, see the Instance types topic in PolarDB User Guide. |

| EffectiveTime | String | No | Immediate | The effective time. Valid values: Immediate: The configuration changes immediately take effect. MaintainTime: The configuration changes take effect within the maintenance window. Default value: Immediate. |
|---|---|---|---|---|
| OwnerAccount | String | No | testuser@aliyun. com | The Apsara Stack tenant account. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 1AD222E9-E606-4A42- BF6D-8A4442913CEF | The request ID. |

**Examples**

**Sample requests**

```
https://polardb.example.com/?Action=ModifyDBInstanceSpec &DBInstanceId=polardb-xxxxx &PayType=Postpaid &DBInstanceStorage=10 &Common request parameters
```

XML format

```xml
<ModifyDBInstanceSpecResponse> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> </ModifyDBInstanceSpecResponse>
```

JSON format

```json
{ "RequestId": "1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC" }
```

JSON format

```json
{ "Code":"UnsupportedOperation", "HostId":"polardb.aliyuncs.com", "Message":"The specified action is not supported.", "RequestId":"7463B73D-35CC-4D19-A010-6B8D65D242EF"}
```

#### 1.3.7 AllocateInstancePublicConnection

Applies for a public endpoint for an instance.

| Parameter | Typ e | Requir ed | Description |
|---|---|---|---|
| Action | Strin g | Yes | The operation that you want to perform. Set the value to AllocateInstancePublicConnection. |
| DBInstanceId | Strin g | Yes | The instance ID. |
| ConnectionString Prefix | Strin g | Yes | The prefix of the public endpoint. |
| Port | Strin g | Yes | The public port to be used by the instance. |

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> | - | The common response parameters. For more information, see Common response parameters. |

**Examples**

**Sample requests**

```
https://polardb.example.com/?Action=AllocateInstancePublicConnection &DBInstanceId=polardb-xxxxx &ConnectionStringPrefix=test0001 &Port=3306 &Common request parameters
```

**Sample responses**

XML format

```xml
<AllocateInstancePublicConnectionResponse> <RequestId>65BDA532-28AF-4122-AA39-B382721EEE64</RequestId> </AllocateInstancePublicConnectionResponse>
```

JSON format

```json
{ "RequestId": "65BDA532-28AF-4122-AA39-B382721EEE64"}
```

#### 1.3.8 ReleaseInstancePublicConnection

Releases the public endpoint of an instance.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set this parameter to ReleaseInstancePublicConnection. |
| DBInstanceId | String | Yes | The instance ID. |
| CurrentConnection String | String | Yes | The public endpoint. |

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> | - | The common response parameters. For more information, see Common response parameters. |

**Examples**

**Sample requests**

```
https://polardb.example.com/?Action=ReleaseInstancePublicConnection &DBInstanceId=polardb-xxxxx &CurrentConnectionString=test0001.mysql.polardb.example.com &Common request parameters
```

**Sample responses**

XML format

```xml
<ReleaseInstancePublicConnectionResponse> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> </ReleaseInstancePublicConnectionResponse>
```

JSON format

```json
{ "RequestId": "1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC" }
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

Queries the connection information of an instance.

| Parameter | Type | Requir ed | Description |
|---|---|---|---|
| Action | Strin g | Yes | The operation that you want to perform. Set the value to DescribeDBInstanceNetInfo. |

| DBInstanceI d | Strin g | Yes | The instance ID. |
|---|---|---|---|

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> |   | The common response parameters. For more information, see Common response parameters. |
| DBInstanceNetInfos | List<DBInstanceAttribute> | The connection information of the instance. |
| InstanceNetworkType | String | The network type of the instance. Valid values: VPC and Classic. |

DBInstanceNetInfo parameters

| Parameter | Type | Description |
|---|---|---|
| ConnectionString | String | The DNS connection string. |
| IPAddress | String | The IP address. |
| IPType | String | The type of the IP address. Valid values for classic network instances: Inner and Public. Valid values for virtual private cloud (VPC) instances: Private and Public. |
| Port | String | The port information. |
| VPCId | String | The VPC ID. |
| VSwitchId | String | The vSwitch ID. |

#### 1.3.11 ModifyDBInstanceConnectionString

Modifies the endpoint and port of an instance. PolarDB provides the internal and public endpoints for an instance and allows both endpoint types to coexist in a specific access mode.

| Parameter | Ty pe | Requi red | Description |
|---|---|---|---|
| Action | Str ing | Yes | The operation that you want to perform. Set the value to ModifyDBInstanceConnectionString. |
| DBInstanceId | Str ing | Yes | The instance ID. |
| CurrentConnection String | Str ing | Yes | The endpoint used by the instance. |
| ConnectionStringP refix | Str ing | No | The endpoint to be used by the instance. |
| Port | Str ing | No | The port to be used by the instance. |

This operation returns only common response parameters. For more information about common response parameters, see Common response parameters.

#### 1.3.12 ModifyDBInstanceConnectionMode

Changes the access mode of an instance. PolarDB supports the following access modes: Standard access mode Secure access mode

| Parameter | Typ e | Require d | Description |
|---|---|---|---|
| Action | Stri ng | Yes | The operation that you want to perform. Set the value to ModifyDBInstanceConnectionMode. |
| DBInstance Id | Stri ng | Yes | The instance ID. |
| Connection Mode | Stri ng | Yes | The access mode of the instance. Valid values: Performance and Safety. |

This operation returns only common response parameters. For more information about common response parameters, see Common response parameters.

#### 1.3.13 ModifyDBInstanceNetworkType

Switches the network type of an instance between virtual private cloud (VPC) and classic network.

**Note**

Only the classic network instances whose ConnectionMode is Safety can have their network type switched to VPC.

| Parameter | T y p e | Requi red | Description |
|---|---|---|---|
| Action | St ri n g | Yes | The operation that you want to perform. Set the value to ModifyDBInstanceNetworkType. |
| DBInstanceId | St ri n g | Yes | The instance ID. |
| InstanceNetwor kType | St ri n g | Yes | The network type of the instance. Valid values: VPC and Classic. |
| VPCId | St ri n g | No | The VPC ID. |
| VSwitchId | St ri n g | No | The VSwitch ID. This parameter is required if the value of VPCId is specified. |

| PrivateIpAddres s | St ri n g | No | The VPC IP address that belongs to the specified vSwitch. If no value is specified, the system assigns a VPC IP address. |
|---|---|---|---|

This operation returns only common response parameters. For more information about common response parameters, see Common response parameters.

#### 1.3.14 DescribeDBInstanceIPArrayList

Queries the IP address whitelist of an instance.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeDBInstanceIPArrayList. |
| DBInstanceI d | String | Yes | The instance ID. |

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> |   | The common response parameters. For more information, see Common response parameters. |
| Items | List<DBInstanceIP Array> | The queried IP address whitelist. |

DBInstanceIPArray parameters

| Parameter | Type | Description |
|---|---|---|
| DBInstanceIPArrayN ame | Strin g | The name of the IP address whitelist. |
| DBInstanceIPArrayAt tribute | Strin g | By default, this parameter is left empty. IP address whitelists with the hidden attribute are not displayed in the console. |

| SecurityIPList | Strin g | The IP addresses in the IP address whitelist. The IP address whitelist can contain a maximum of 1,000 IP addresses. Multiple IP addresses are separated by commas (,). Supported formats include 0.0.0.0/0, 10.23.12.24, and 10.23.12.24/24. 10.23.12.24 is an IP address. 10.23.12.24/24 is a CIDR block, in which the suffix /24 indicates the number of bits for the prefix of the IP address. The suffix ranges from 1 to 32. |
|---|---|---|

#### 1.3.15 ModifySecurityIps

Modifies the IP address whitelist of an instance. Before you call this operation, make sure that the following requirements are met: The instance is in the Running state. The instance is not locked by the system.

| Parameter | Ty pe | Requ ired | Description |
|---|---|---|---|
| Action | Str ing | Yes | The operation that you want to perform. Set this parameter to ModifySecurityIps. |
| DBInstanceId | Str ing | Yes | The instance ID. |
| SecurityIps | Str ing | No | The IP addresses in the IP address whitelist. You can add a maximum of 1,000 IP addresses and separate them with commas (,). Supported formats include 0.0.0.0/0, 10.23.12.24, and 10.23.12.24/24. 10.23.12.24 is an IP address. 10.23.12.24/24 is a CIDR block, in which the suffix /24 indicates the number of bits for the prefix of the IP address. The suffix ranges from 1 to 32. |
| DBInstanceIPArrayNa me | Str ing | No | The name of the IP address whitelist. If you do not enter a name, IP addresses are added to the default whitelist. |
| DBInstanceIPArrayAtt ribute | Str ing | No | By default, this parameter is left empty. IP address whitelists with the hidden attribute are not displayed in the console. |

This operation returns only common response parameters. For more information about common response parameters, see Common response parameters.

**Examples**

**Sample requests**

```
https://polardb.example.com/?Action=ModifySecurityIps &DBInstanceId=polardb-xxxxx &SecurityIps=192.168.1.2 &Common request parameters
```

**Sample responses**

XML format

```xml
<ModifySecurityIpsResponse> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> </ModifySecurityIpsResponse>
```

JSON format

```json
{ "RequestId": "1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC"}
```

#### 1.3.16 DescribeRegions

Queries available regions and zones. You must call the DescribeRegions operation to query available regions before you call the CreateDBInstance operation.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeRegions. |

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> | - | The common response parameters. For more information, see Common response parameters. |
| Regions | List<PolarDBRegion> | The queried regions. |

PolarDBRegion parameters

| Parameter | Type | Description |
|---|---|---|
| RegionId | String | The region ID. |
| ZoneId | String | The zone ID. |

**Examples**

**Sample requests**

```
https://polardb.example.com/?Action=DescribeRegions &Common request parameters
```

**Sample responses**

XML format

```xml
<DescribeRegionsResponse> <Regions> <PolarDBRegion> <RegionId>cn-hangzhou</RegionId> <ZoneId>cn-hangzhou-a</RegionId> </PolarDBRegion> <PolarDBRegion> <RegionId>cn-hangzhou</RegionId ><ZoneId>cn-hangzhou-b</ZoneId> </PolarDBRegion> </Regions> <RequestId>A36D9720-7902-42A4-B8B9-014A2135E6C3</RequestId> </DescribeRegionsResponse>
```

JSON format

```json
{ "Regions":
    { "PolarDBRegion":
        [ {"RegionId": "cn-hangzhou",
            "ZoneId":"cn-hangzhou-a"},
          {"RegionId": "cn-hangzhou",
            "ZoneId":"cn-hangzhou-b"},
             ]},
    "RequestId": "1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC"
```

`}`

#### 1.3.17 DescribeDBInstanceHAConfig

Queries the zone information and data replication status of an instance.

| Parameter | Type | Require d | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeDBInstanceHAConfig. |
| DBInstanceI d | String | Yes | The instance ID. |

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> |   | The common response parameters. For more information, see Common response parameters. |
| DBInstanceId | String | The instance ID. |
| SyncMode | String | The synchronization mode of the instance. Valid values: Semi-sync and Async. |
| HAMode | String | The high availability mode of the instance. Valid values: RPO: Data persistence prevails. RTO: Instance availability prevails. |
| HostInstanceInfos | List<NodeI nfo> | The information about the primary and secondary instances. |

NodeInfo parameters

| Parameter | Type | Description |
|---|---|---|
| NodeId | String | The unique ID of the primary or secondary instance. |
| NodeType | String | The role of the primary or secondary instance. Valid values: Master and Slave. |
| RegionId | String | The region ID. |
| ZoneId | String | The zone ID. |

| SyncStatus | String | The synchronization status of the instance. Valid values: NotAvailable: Synchronization is unavailable because a failure has occurred. Syncing: Synchronization is in process, with a probability of data loss during failovers. Synchronized: Synchronization is complete. NotSupport: Synchronization is not supported by the database engine or version. |
|---|---|---|
| LogSyncTime | String | The time when the secondary instance receives logs. |
| DataSyncTime | String | The time when the secondary instance receives data. |

#### 1.3.18 MigrateToOtherZone

Migrates an instance from one zone to another. For example, if Instance 1 resides in Hangzhou Zone A, you can call this operation to migrate the instance to Hangzhou Zone B.

**Note**

In cross-zone migration, instances must be migrated within the same region. For example, instances in a zone of the China (Hangzhou) region cannot be migrated to a zone of the China (Qingdao) region.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to MigrateToOtherZone. |
| DBInstanceId | String | Yes | The instance ID. |
| ZoneId | String | Yes | The zone ID of the instance. You can call the DescribeRegions operation to query available zones. |

This operation returns only common response parameters. For more information about common response parameters, see Common response parameters.

**Examples**

**Sample requests**

```
https://polardb.example.com/?Action=MigrateToOtherZone &DBInstanceId=polardb-xxxxx &ZoneId=cn-hangzhou-b &Common request parameters
```

**Sample responses**

XML format

```xml
<MigrateToOtherZoneResponse> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> </MigrateToOtherZoneResponse>
```

JSON format

```json
{ "RequestId": "1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC"}
```

#### 1.3.19 PurgeDBInstanceLog

Clears all binlogs of an instance.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to PurgeDBInstanceLog. |
| DBInstanceId | String | Yes | The instance ID. |

This operation returns only common response parameters. For more information about common response parameters, see Common response parameters.

**Examples**

**Sample requests**

```
https://polardb.example.com/?Action=PurgeDBInstanceLog &DBInstanceId=polardb-xxxxx &Common request parameters
```

**Sample responses**

XML format

```xml
<PurgeDBInstanceLogResponse> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> </PurgeDBInstanceLogResponse>
```

JSON format

```json
{ "RequestId": "1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC"}
```

#### 1.3.20 ModifyDBInstanceDescription

Modifies the description of an instance to help identify the instance. For example, you can modify the description of an instance to Alibaba_Cloud_testing_environment_instance.

| Parameter | Typ e | Requir ed | Description |
|---|---|---|---|
| Action | Strin g | Yes | The operation that you want to perform. Set the value to ModifyDBInstanceDescription. |
| DBInstanceId | Strin g | Yes | The instance ID. |
| DBInstanceDesc ription | Stin g | Yes | The description of the instance. |

This operation returns only common response parameters. For more information about common response parameters, see Common response parameters.

**Examples**

**Sample requests**

```
https://polardb.example.com/?Action=ModifyDBInstanceDescription &DBInstanceId=polardb-xxxxx &DBInstanceDescription=testdescribe &Common request parameters
```

**Sample responses**

XML format

```xml
<ModifyDBInstanceDescriptionResponse> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> </ModifyDBInstanceDescriptionResponse>
```

JSON format

```json
{ "RequestId": "1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC"}
```

#### 1.3.21 ModifyDBInstanceMaintainTime

Modifies the maintenance window of an instance. You can set the maintenance window to offpeak hours. Apsara Stack performs routine maintenance during the maintenance window to minimize the impacts on your business.

| Parameter | Type | Requir ed | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to ModifyDBInstanceMaintainTime. |
| DBInstanceI d | String | Yes | The instance ID. |
| MaintainTim e | String | Yes | The maintenance window of the instance. Valid values: 22:00Z-02:00Z 02:00Z-06:00Z 06:00Z-10:00Z 10:00Z-14:00Z 14:00Z-18:00Z 18:00Z-22:00Z |

This operation returns only common response parameters. For more information about common response parameters, see Common response parameters.

**Examples**

**Sample requests**

```
https://polardb.example.com/?Action=ModifyDBInstanceMaintainTime &DBInstanceId=polardb-xxxxx &MaintainTime=22:00Z-02:00Z &Common request parameters
```

**Sample responses**

XML format

```xml
<ModifyDBInstanceMaintainTimeResponse> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> </ModifyDBInstanceMaintainTimeResponse>
```

JSON format

```json
{ "RequestId": "1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC" }
```

#### 1.3.22 ModifyDBInstanceHAConfig

Modifies the data replication mode and high availability switching rules of an instance.

| Parameter | Type | Requir ed | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to ModifyDBInstanceHAConfig. |
| DBInstance Id | String | Yes | The instance ID. |
| SyncMode | String | Yes | The synchronization mode of the instance. Valid values: Semi- sync and Async. |
| HAMode | String | Yes | The high availability mode of the instance. Valid values: RPO: Data persistence prevails. RTO: Instance availability prevails. |

This operation returns only common response parameters. For more information about common response parameters, see Common response parameters.

#### 1.3.23 SwitchDBInstanceHA

Switches between the primary and secondary instances. PolarDB instances are composed of primary and secondary instances distributed across different servers. The primary instance bears the service traffic.

| Paramete r | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to SwitchDBInstanceHA. |

| DBInstanc eId | String | Yes | The instance ID. |
|---|---|---|---|
| NodeId | String | Yes | The unique ID of the primary or secondary instance. You can call the DescribeDBInstanceHAConfig operation to query the value of this parameter. |
| Force | String | Yes | Specifies whether to forcibly switch between the primary and secondary instances. Valid values: Yes and No. Default value: No. |

This operation returns only common response parameters. For more information about common response parameters, see Common response parameters.

#### 1.3.24 CreateReadOnlyDBInstance

Creates a read-only instance for a primary instance. Before you call this operation, make sure that the following requirements are met: The primary instance is in the Running state, but not in the Failover state. The read-only instance and the primary instance are in the same region. A primary instance can have up to five read-only instances.

| Parameter | Type | Requi red | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to CreateReadOnlyDBInstance. |
| RegionId | String | Yes | The region ID of the instance. The ID can be up to 50 characters in length. You can call the DescribeRegions operation to query the most recent region list. |
| ZoneId | String | Yes | The zone ID of the instance. You can call the DescribeRegions operation to query the most recent zone list. |
| DBInstanceId | String | Yes | The ID of the primary instance. |

| EngineVersion | String | Yes | The database engine version of the read-only instance. The read-only instance and the primary instance must run the same database engine version. Valid values: 14 16 |   |   |
|---|---|---|---|---|---|
| DBInstanceClass | String | Yes | The instance type of the instance. |   |   |
| DBInstanceStora ge | Intege r | Yes | The storage capacity of the instance. Valid values: 5 to 1000 . The capacity must be incremented by 5 GB. Unit: GB. |   |   |
|   |   |   |   | 5 to |   |
| DBInstanceDesc ription | String | No | The description of the instance. It must be 2 to 256 characters in length. The description cannot start with http:// or https://. The description can contain letters, digits, underscores ( ), _ and hyphens (-). It must start with a letter. |   |   |
| ClientToken | String | Yes | The client token that is used to ensure the idempotence of the request. |   |   |
| InstanceNetwork Type | String | No | VPC Classic Default value: Classic. |   |   |
| VPCId | String | No | The virtual private cloud (VPC) ID. |   |   |
| VSwitchId | String | No | The vSwitch ID. |   |   |
| PrivateIpAddress | String | No | The VPC IP address that belongs to the specified vSwitch. If no value is specified, the system assigns a VPC IP address. |   |   |

|   | 1000 |
|---|---|

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> | - | The common response parameters. |
| DBInstanceId | String | The instance ID. |
| OrderId | String | The order ID. |

| econdary Edition) e·API reference | Developer Gui | ApsaraDB for POLARDB |
|---|---|---|

| ConnectionStrin g | String | The endpoint used to connect to the instance. |
|---|---|---|
| Port | String | The port used to connect to the instance. |

**Examples**

**Sample requests**

```
https://polardb.example.com/?Action=CreateReadOnlyDBInstance &RegionId=cn-hangzhou &ZoneId=cn-hangzhou-b &DBInstanceId=polardb-xxxxx &EngineVersion=16 &DBInstanceClass=polardb.g4.4xlarge.2 &DBInstanceStorage=10 &PayType=Postpaid &ClientToken=ETnLK******
```

XML format

```xml
<CreateDBInstanceResponse> <OrderId>10078937023****</OrderId> <ConnectionString>rm-5obp******.o.polardb.rds.inter.env17e.shuguang.com </ConnectionString> <DBInstanceId>polardb-xxxxx</DBInstanceId> <port>3433</port> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> </CreateDBInstanceResponse>
```

JSON format

```json
{ "OrderId": "10078937023****", "ConnectionString": "rm-5obp******.o.polardb.rds.inter.env17e.shuguang.com", "DBInstanceId": "polardb-xxxxx", "Port": "3433", "RequestId": "1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC" }
```

#### 1.3.25 DescribeDBInstanceSSL

Queries the SSL link of an instance.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeDBInstanceSSL. |
| DBInstanceId | String | Yes | The instance ID. |

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> | - | The common response parameters. For more information, see Common response parameters. |
| ConnectionString | String | The endpoint that is protected by SSL encryption. |
| SSLExpireTime | String | The expiration time of the SSL certificate. The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ssZ format. |
| RequireUpdate | String | Indicates whether an immediate update is required. Valid values: Yes and No. |
| RequireUpdateRe ason | String | The reason why an update is required. |

#### 1.3.26 ModifyDBInstanceSSL

Modifies the SSL link of a PolarDB instance.

| Parameter | Typ e | Req uire d | Description |
|---|---|---|---|
| Action | Strin g | Yes | The operation that you want to perform. Set the value to ModifyDBInstanceSSL. |
| DBInstance Id | Strin g | Yes | The instance ID. |

| Connection String | Strin g | Yes | The connection string of the instance. Each instance can have only one connection string protected by the SSL certificate. The SSL certificate can be created or updated for the connection string. |
|---|---|---|---|

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> | - | For more information, see Common response parameters. |
| SSLExpireTime | String | The expiration time of the SSL certificate. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC. |

#### 1.3.27 DescribeDBInstanceTDE

Queries the Transparent Data Encryption (TDE) status of a PolarDB instance.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeDBInstanceTDE. |
| DBInstanceId | String | Yes | The instance ID. |

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> |   | For more information, see Common response parameters. |
| TDEStatus | String | The TDE status of the instance. Valid values: Enabled and Disabled. |
| Databases | List<DataBase> | The details of the database. |

DataBase

| Paramete r | Type | Description |
|---|---|---|
| DBName | String | The database name. |
| TDEStatus | String | The TDE status of the database. Valid values: Enabled and Disabled. |

#### 1.3.28 ModifyDBInstanceTDE

Modifies the Transparent Data Encryption (TDE) status of a PolarDB instance.

| Parameter | Type | Requi red | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to ModifyDBInstanceTDE. |
| DBInstanceId | String | Yes | The instance ID. |
| TDEStatus | String | Yes | Specifies whether to enable TDE for the instance. Valid values: Enabled and Disabled. |
| DBName | String | No | The database name. You can specify up to 50 database names in a single request. Separate multiple names with commas (,). |

For more information, see Common response parameters.

### 1.4 Database management

#### 1.4.1 CreateDatabase

Creates a database in an instance. Before you call this operation, make sure that the following requirements are met: The instance is in the running state. The instance is not locked. The maximum number of databases in the instance is not reached. The instance is a primary instance.

**Note**

This operation is not supported for PolarDB. You can create databases in PolarDB instances by executing a CREATE DATABASE statement.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to CreateDatabase. |
| DBInstanceI d | String | Yes | The instance ID. |
| DBName | String | Yes | The unique name of the database. The name can be up to 64 characters in length and can contain lowercase letters, digits, and underscores ( ). It must start with a letter. _ |
| CharacterSet Name | String | Yes | The character set that is used by the database. You can view the character set on the Databases tab of the instance details page. |
| DBDescriptio n | String | No | The description of the instance. It must be 2 to 256 characters in length. The description cannot start with http:// or https://. The description can contain letters, digits, underscores ( ), and hyphens (-). It must start with a letter. _ |

For more information, see Common response parameters.

**Examples**

**Sample requests**

```
https://polardb.example.com/?Action=CreateDatabase &CharacterSetName=GBK &DBName=testDB &DBInstanceId=polardb-xxxxx &<Common request parameters>
```

XML format

```xml
<CreateDatabaseResponse> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> </CreateDatabaseResponse>
```

JSON format

```json
{ "RequestID":"1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC" }
```

#### 1.4.2 DeleteDatabase

Deletes a database from an instance. Before you call this operation, make sure that the following requirements are met: The instance is in the running state. The instance is a primary instance.

**Note**

This operation is not supported for PolarDB. You can delete databases from PolarDB instances by executing a DROP DATABASE statement.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DeleteDatabase. |
| DBInstance Id | String | Yes | The instance ID. |
| DBName | String | Yes | The database name. |

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> | - | For more information, see Common response parameters. |

**Examples**

**Sample requests**

```
https://polardb.example.com/?Action=DeleteDatabase &DBName=testDB &DBInstanceId=polardb-xxxxx &<Common request parameters>
```

XML format

```xml
<DeleteDatabaseResponse> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> </DeleteDatabaseResponse>
```

JSON format

```json
{ "RequestId":"1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC" }
```

#### 1.4.3 DescribeDatabases

Queries a list of databases of an instance and the information about a database. If you specify invalid request parameters, an error message is returned and the returned data is empty.

| Parame ter | Type | Requ ired | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeDatabases. |
| DBInsta nceId | String | Yes | The instance ID. |
| DBName | String | No | The database name. |
| DBStatu s | String | No | The database status. Valid values: Creating Running Deleting |

| Parameter | Type | Description |
|---|---|---|

| <Common response parameters> | - | The common response parameters. For more information, see Common response parameters. |
|---|---|---|
| Databases | List<Database> | The list of databases. |

Parameters in Database

| Parameter | Type | Description |
|---|---|---|
| DBName | String | The database name. |
| DBInstanceId | String | The ID of the instance to which the database belongs. |
| Engine | String | The database engine of the instance to which the database belongs. |
| DBStatus | String | The database status. Valid values: Creating Running Deleting |
| CharacterSet Name | String | The character set that is used by the database. |
| DBDescription | String | The database description. |
| Accounts | List<AccountPrivileg eInfo> | The list of accounts. |
| Account | String | The account name. |
| AccountPrivile ge | String | The permissions of the account on the database. |

Parameters in AccountPrivilegeInfo

| Parameter | Type | Description |
|---|---|---|
| Account | String | The account name. |

| AccountPrivilege | String | The permissions of the account on the database. |
|---|---|---|

**Examples**

**Sample requests**

```
https://polardb.example.com/?Action=DescribeDatabases &DBInstanceId=polardb-xxxxx &<Common request parameters>
```

XML format

```xml
<DescribeDatabasesResponse> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> <Databases> <Database> <Engine>PolarDB_PG</Engine> <DBName>testdb</DBName> <CharacterSetName>utf8</CharacterSetName> <DBStatus>Creating</DBStatus> <DBInstanceId>polardb-xxxxx</DBInstanceId> <Accounts> <AccountPrivilegeInfo></AccountPrivilegeInfo> <Accounts> </Database> </Databases> </DescribeDatabasesResponse>
```

JSON format

```json
{ "RequestId": "1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC", "Databases":
    { "Database":
        [ { "Engine": "PolarDB_PG",
            "CharacterSetName": "utf8",
            "DBStatus": "Creating",
            "DBDescription": "",
            "DBInstanceId": "polardb-xxxxx",
            "Accounts": { " AccountPrivilegeInfo": [] },
            "DBName": "testdb" }] }
```

`}`

#### 1.4.4 ModifyDBDescription

Modifies the description of a database to help identify the database. For example, you can change the description of a database to Database A for the Alibaba Cloud testing environment.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to ModifyDBDescription. |
| DBInstanceId | String | Yes | The instance ID. |
| DBName | String | Yes | The database name. |
| DBDescription | String | Yes | The new description of the database. |

For more information, see Common response parameters.

**Examples**

**Sample requests**

```
https://polardb.example.com/?Action=ModifyDBDescription &DBInstanceId=polardb-xxxxx &DBInstanceDescription=testDBdescribe &<Common request parameters>
```

XML format

```xml
<ModifyDBDescriptionResponse> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> </ModifyDBDescriptionResponse>
```

JSON format

```json
{ "RequestId": "1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC" }
```

### 1.5 Account management

#### 1.5.1 CreateAccount

Creates an account for a database. In the same instance, one account can manage multiple databases by using different permissions. Before you call this operation, make sure that the following requirements are met: The instance is in the running state. The database is in the running state. The instance is not locked. The number of accounts that are created on the instance does not exceed the maximum number of accounts that are allowed for each instance.

| Parameter | Typ e | Req uire d | Description |
|---|---|---|---|
| Action | Strin g | Yes | The operation that you want to perform. Set the value to CreateAccount. |
| DBInstanceId | Strin g | Yes | The instance ID. |
| AccountName | Strin g | Yes | The unique name of the account. The name can be up to 16 characters in length and can contain lowercase letters, digits, and underscores ( ). It must start with a letter. For more information _ about invalid characters, see Forbidden keywords. |
| AccountPassw ord | Strin g | Yes | The password for the account. It must be 6 to 32 characters in length and can contain letters, digits, and underscores ( ). _ |
| AccountType | Strin g | No | The account type. Valid values: Normal and Super. Default value: Normal. PolarDB can have only one initial account. You must use the initial account to log on to the database and create other types of accounts. |
| AccountDescr iption | Strin g | No | The account description. It must be 2 to 256 characters in length. It must start with a letter and cannot start with http:// or https://. It can contain letters, digits, underscores ( ), and hyphens (-). _ |

For more information, see Common response parameters.

**Examples**

**Sample requests**

```
https://polardb.example.com/?Action=CreateAccount &AccountName=testacc02 &AccountPassword=pwxxxxx &DBInstanceId=rds-xxxxx &<Common request parameters>
```

XML format

```xml
<CreateAccountResponse> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> </CreateAccountResponse>
```

JSON format

```json
{ "RequestId":"1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC" }
```

#### 1.5.2 DeleteAccount

Deletes a database account of an instance. Before you call this operation, make sure that the instance is in the Running state.

| Parameter | Type | Require d | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DeleteAccount. |
| DBInstanceI d | String | Yes | The instance ID. |
| AccountNam e | String | Yes | The unique name of the account. The name can be up to 16 characters in length and can contain lowercase letters, digits, and underscores ( ). It must start with a letter. For _ more information about invalid characters, see Forbidden keywords. |

For more information, see Common response parameters.

**Examples**

**Sample requests**

```
https://polardb.example.com/?Action=DeleteAccount &DBInstanceId=rds-xxxxx &AccountName=testacc01 &<Common request parameters>
```

XML format

```xml
<DeleteAccountResponse> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> </DeleteAccountResponse>
```

JSON format

```json
{ "RequestID":"1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC" }
```

#### 1.5.3 DescribeAccounts

Queries a list of accounts for a database in an instance and the information about an account.

| Parameter | Typ e | Required | Description |
|---|---|---|---|
| Action | Stri ng | Yes | The operation that you want to perform. Set the value to DescribeAccounts. |
| DBInstance Id | Stri ng | Yes | The instance ID. |
| AccountNa me | Stri ng | Yes | The account name. |

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> |   | For more information, see Common response parameters. |
| Accounts | List<DBInstanceAccount > | The information about the account. |

DBInstanceAccount

| Parameter | Type | Description |
|---|---|---|
| DBInstanceId | String | The ID of the instance to which the account belongs. |

| AccountName | String | The account name. |
|---|---|---|
| AccountStatus | String | The status of the account. Valid values: Unavailable Available |
| AccountDescription | String | The account description. |
| DatabasePrivileges | List<DatabasePrivil ege> | The array that consists of DatabasePrivilege data. |
| AccountType | String | The account type. Valid values: Normal: a standard account Super: a super account |

DatabasePrivilege

| Parameter | Type | Description |
|---|---|---|
| DBName | String | The database name. |
| AccountPrivilege | String | The account name. |

**Examples**

**Sample requests**

```
https://polardb.example.com/?Action=DescribeAccounts &DBInstanceId=polardb-xxxxx &<Common request parameters>
```

XML format

```xml
<DescribeAccountsResponse> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> <Accounts> <DBInstanceAccount> <AccountName>PolarDB_PG</AccountName> <DBInstanceId>testdb</DBInstanceId> <AccountStatus>utf8</AccountStatus> <AccountDescription> </AccountDescription> <DatabasePrivileges> <DatabasePrivilege></DatabasePrivilege> </DatabasePrivileges> <DBInstanceAccount> </Accounts> </DescribeAccountsResponse>
```

JSON format

```json
{ "Accounts":
 { "DBInstanceAccount":
  [ { "AccountDescription": "",
   "DBInstanceId": "polardb-xxxxx",
   "DatabasePrivileges": { "DatabasePrivilege": [] },
   "AccountStatus": "Unavailable",
   "AccountName": "testaccount" } ] },
 "RequestId": "1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC" }
```

#### 1.5.4 GrantAccountPrivilege

Grants database access permissions to an account. An account can be associated with one or more databases. If the specified account already has access permissions on the specified database, the operation directly returns a success response. Before you call this operation, make sure that the instance is in the running state.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to GrantAccountPrivilege. |
| DBInstanceId | String | Yes | The instance ID. |
| AccountName | String | Yes | The account name. |

| DBName | String | Yes | The name of the database to be accessed by the account. |
|---|---|---|---|
| AccountPrivileg e | String | Yes | The permissions of the account. Valid values: ReadOnly and ReadWrite. |

For more information, see Common response parameters.

**Examples**

**Sample requests**

```
https://polardb.example.com/?Action=GrantAccountPrivilege &AccountName=testacc02 &AccountPrivilege=readwrite &DBName=testdb03 &DBInstanceId=polardb-xxxxx &<Common request parameters>
```

XML format

```xml
<GrantAccountPrivilegeResponse> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> </GrantAccountPrivilegeResponse>
```

JSON format

```json
{ "RequestId":"1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC"}
```

#### 1.5.5 RevokeAccountPrivilege

Revokes database access permissions from an account. Before you call this operation, make sure that the following requirements are met: The instance is in the running state. The database is in the running state.

| Paramete r | Type | Requi red | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to RevokeAccountPrivilege. |

| DBInstanc eId | String | Yes | The instance ID. |
|---|---|---|---|
| AccountNa me | String | Yes | The account name. |
| DBName | String | Yes | The database name. |

For more information, see Common response parameters.

**Examples**

**Sample requests**

```
https://polardb.example.com/?Action=RevokeAccountPrivilege &AccountName=testacc02 &DBName=testdb03 &DBInstanceId=polardb-xxxxx &<Common request parameters>
```

XML format

```xml
<RevokeAccountPrivilegeResponse> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> </RevokeAccountPrivilegeResponse>
```

JSON format

```json
{ "RequestId":"1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC"}
```

#### 1.5.6 ModifyAccountDescription

Modifies the description of an account to help identify the account. For example, you can change the description of an account to Account A for the Alibaba Cloud testing environment.

| Parameter | Typ e | Require d | Description |
|---|---|---|---|
| Action | Stri ng | Yes | The operation that you want to perform. Set the value to ModifyAccountDescription. |

| DBInstanceId | Stri ng | Yes | The instance ID. |
|---|---|---|---|
| AccountName | Stri ng | Yes | The unique name of the account. The name can be up to 16 characters in length and can contain lowercase letters, digits, and underscores ( ). It must start with a letter. For more _ information about invalid characters, see Forbidden keywords. |
| AccountDescr iption | Stri ng | Yes | The new description of the account. It must be 2 to 256 characters in length and cannot start with http:// or https://. It must start with a letter. It can contain letters, digits, underscores ( ), and hyphens (-). _ |

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> | - | For more information, see Common response parameters. |

**Examples**

**Sample requests**

```
https://polardb.example.com/?Action=ModifyAccountDescription &DBInstanceId=polardb-xxxxx &AccountName=testacc01 &AccountDescription=testAccoutdescribe &<Common request parameters>
```

XML format

```xml
<ModifyAccountDescription> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> </ModifyAccountDescription>
```

JSON format

```json
{ "RequestId": "1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC"}
```

#### 1.5.7 ResetAccountPassword

Resets the password of an account for an instance. Before you call this operation, make sure that the following requirements are met: The instance is in the running state and not locked.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | Strin g | Yes | The operation that you want to perform. Set the value to ResetAccountPassword. |
| DBInstanceId | Strin g | Yes | The instance ID. |
| AccountNam e | Strin g | Yes | The account name. |
| AccountPass word | Strin g | Yes | The new password of the account. It must be 6 to 32 characters in length and can contain letters, digits, and underscores ( ). _ |

For more information, see Common response parameters.

**Examples**

**Sample requests**

```
https://polardb.example.com/?Action=ResetAccountPassword &AccountName=testacc02 &AccountPassword=pwxxxxx &DBInstanceId=polardb-xxxxx &<Common request parameters>
```

XML format

```xml
<ResetAccountPasswordResponse> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> </ResetAccountPasswordResponse>
```

JSON format

```json
{ "RequestId":"1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC"}
```

#### 1.5.8 ResetAccount

You can call this operation to reset the initial account of an instance.

| 0 |   |   | > Document Version: 2026063 |
|---|---|---|---|

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

Creates a backup. You can create up to 10 backups for an instance in a single day. Before you call this operation, make sure that the following requirements are met: The instance is in the running state. The last backup is complete.

| Paramet er | Type | Req uire d | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set this parameter to CreateBackup. |
| DBInstanc eId | String | Yes | The instance ID. |
| BackupMe thod | String | No | The backup method. Valid values: Logical and Physical. Default value: Physical. Logical backup cannot be used for instances without databases. |

| BackupStr ategy | String | No | The logical backup range. Valid values: db: single-database backup. instance: instance backup. This parameter takes effect only when BackupMethod is set to Logical. |
|---|---|---|---|
| DBName | String | No | The name of the database for logical single-database backup. This parameter takes effect only when BackupMethod is set to Logical and BackupStrategy is set to db. |
| BackupTy pe | String | No | The backup type. Valid values: Auto: specifies whether it is a full backup or an incremental backup through automatic calculation. FullBackup: specifies a full backup. Default value: Auto. |

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> | - | For more information, see Common response parameters. |

**Examples**

**Sample requests**

```
https://polardb.example.com/?Action= CreateBackup &DBInstanceId=polardb-xxxxx &<Common request parameters>
```

XML format

```xml
<CreateBackupResponse> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> </CreateBackupResponse>
```

JSON format

```json
{ "RequestId":"1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC"}
```

#### 1.6.2 CloneDBInstance

Clones a new instance from an existing instance by using data from either a backup file or a specific point in time. The new instance inherits the whitelist, SQL audit, alert threshold, backup, and parameter settings from the original instance. The data in the new instance is the same as that in the backup file. The clone feature is available only for PolarDB for MySQL instances. The new instance handles database account information based on the following rules: If the original instance is cloned by using a privileged account, the new instance inherits that privileged account. If the original instance is cloned by using a standard account, the new instance inherits the account information from the backup file or the specified point in time.

| Parameter | Type | Requir ed | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to CloneDBInstance. |
| DBInstanceId | String | Yes | The instance ID. |
| BackupId | String | No | The ID of the backup set from which you want to clone a new instance. You can call the DescribeBackups operation to query backup set IDs. |
| RestoreTime | String | No | The point in time within the backup retention period from which you want to clone a new instance. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC. Example: 2011-06- 11T16:00:00Z. You must specify at least one of BackupId and RestoreTime. |
| DBInstanceClas s | String | No | The instance type. For more information, see Instance types in Appendix. If you do not specify this parameter, the new instance inherits the instance type from the original instance. |
| DBInstanceStor age | String | No | The disk capacity. Unit: GB. By default, the disk capacity of the new instance is the same as that of the original instance. Set the value to 3000 for PolarDB instances of the dedicated host instance family. Valid values for PolarDB instances of other instance families: 5 to 2000. The value must be in increments of 5 GB. |
| InstanceNetwor kType | String | No | The network type. Valid values: Classic and VPC. By default, the network type of the new instance is the same as that of the original instance. |
| VPCId | String | No | The virtual private cloud (VPC) ID. |
| VSwitichId | String | No | The vSwitch ID. |
| PrivateIpAddres s | String | No | The VPC IP address that belongs to the specified vSwitch. If no value is specified, the system assigns a VPC IP address. |

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> | - | For more information, see Common response parameters. |
| DBInstanceId | String | The instance ID. |
| OrderId | Integer | The order ID. |

#### 1.6.3 DescribeBackups

Queries the backup sets of an instance. Only backup sets in the Success state can be used for database restoration. PolarDB allows you to download backup files. A null value of DownloadLink indicates that no URL is available for downloading a backup file. A non-null value of DownloadLink provides a URL for downloading a backup file by using wget (enclose the URL in double quotation marks), a web browser, or a custom program. The URL expires at the time specified by LinkExpiredTime. Download the backup file before it expires. If you attempt to download a backup file by using an expired URL, the following error code is returned:

```xml
<?xml version="1.0" encoding="UTF-8" ?><Error><Code>AccessDenied</Code> <Message>Request has expired.</Message><Expires>2012-12-25T09:47:52.000Z</Expires><Se rverTime>2012-12-25T09:49:00.000Z</ServerTime> <RequestId>50D9768CA801C2F102005C70</RequestId><HostId>oss-test.aliyuninc.com</HostId></Error>
```

| Parameter | Type | Require d | Description |
|---|---|---|---|
| Action | Strin g | Yes | The operation that you want to perform. Set this parameter to DescribeBackups. |
| DBInstanceI d | Strin g | Yes | The instance ID. |

| BackupId | Integ er | No | The backup set ID. |
|---|---|---|---|
| BackupStatu s | Strin g | No | The backup set status. Valid values: Success and Failed. |
| BackupMode | Strin g | No | The backup mode. Valid values: Automated and Manual. |
| StartTime | Strin g | Yes | The beginning of the time range to query. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mmZ format. The time must be in UTC. Example: 2011-06-11T15:00Z. |
| EndTime | Strin g | Yes | The end of the time range to query. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mmZ format. The time must be in UTC. The end time must be later than the start time. Example: 2011-06-11T16:00Z. |
| PageSize | Integ er | No | The number of entries per page. Valid values: 30, 50, and 100. Default value: 30. |
| PageNumber | Integ er | No | The page number. Pages start from page 1. Default value: 1. |

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> |   | For more information, see Common response parameters. |
| TotalRecordCount | Integer | The total number of entries returned. |
| PageNumber | Integer | The page number. |
| PageRecordCount | Integer | The number of backup sets on the current page. |
| Items | List<Backup> | The list of backup files. |

#### 1.6.4 CreateTempDBInstance

**Note**

Creates a temporary instance from a backup set or a point in time within the last seven days. After the temporary instance is created, its accounts and databases inherit the data from the backup set. Before you call this operation, make sure that the following requirements are met: The instance is in the running state. The instance is not undergoing migration tasks. The instance is not locked. The backup set is complete.

| Parameter | Type | Requir ed | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to CreateTempDBInstance. |
| DBInstance Id | String | Yes | The instance ID. |
| BackupId | Integer | No | The backup set ID. |
| RestoreTim e | String | No | The point in time to which the temporary instance is to be restored. The time must be within the last seven days and at least 30 minutes before the current time. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC. Example: 2011-06-11T16:00:00Z. |

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> |   | For more information, see Common response parameters. |
| TempDBInstanceId | String | The temporary instance ID. |

**Examples**

**Sample requests**

```
https://polardb.example.com/?Action=CreateTempDBInstance &BackupId=90262 &DBInstanceId=polardb-xxxxx &<Common request parameters>
```

XML format

```xml
<CreateTempDBInstanceResponse> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> <TempDBInstanceId>sub-xxxxx</TempDBInstanceId> </CreateTempDBInstanceResponse>
```

JSON format

```json
{ "RequestId":"1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC", "TempDBInstanceId":"sub-xxxxx"}
```

#### 1.6.5 DescribeBackupPolicy

Queries the backup policy configured for an instance. PolarDB periodically backs up an instance based on the user-defined system configuration.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set this parameter to DescribeBackupPolicy. |
| DBInstanceId | String | Yes | The instance ID. |

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> |   | For more information, see Common response parameters. |
| BackupRetentionPeri od | String | The data backup retention period. Unit: days. Valid values: 1 to 30. |
| PreferredBackupTim e | String | The time range for backups, in UTC. Format: HH:mmZ- HH:mmZ. |

| PreferredBackupPeri od | String | The backup day. Valid values: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, and Sunday. |
|---|---|---|
| BackupLog | String | Indicates whether log backup is enabled. Valid values: Enable and Disabled. |
| LogBackupRetention Period | String | The log backup retention period. Unit: days. Valid values: 1 to 30. |

#### 1.6.6 Query available point-in-time recovery range

**range**

Use the DescribeLocalAvailableRecoveryTime operation to query the available time range for point-in-time recovery (PITR). This operation returns the earliest restorable time for an instance, which corresponds to the recovery point objective (RPO).

**Supported engines**

PolarDB for MySQL Cluster Edition PolarDB for PostgreSQL Primary/Standby Edition

**Request header**

This operation uses only common request headers. For more information, see common request parameters.

| Parameter | Type | In | Required | Example | Description |
|---|---|---|---|---|---|
| DBInstanc eId | Strin g | Quer y | Yes | rm-wq64n542y9j****** | The ID of the instance. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 9B7BFB11-C077- 4FE3-B051- F69CEB****** | The ID of the request. |
| Message | String | Successful | The response message. A value of Successful is returned on success; an error message is returned on failure. |

| Success | Boolean | true | Indicates whether the request was successful. Valid values: true: The request was successful. false: The request failed. |
|---|---|---|---|
| Data | Struct | {} | The response data. |
| - RecoveryEndTi me | String | 2026-01- 26T13:01:15Z | The latest time to which the instance can be restored. |
| - RecoveryBegin Time | String | 2026-01- 21T04:30:32Z | The earliest time to which the instance can be restored. |
| - DBInstanceNa me | String | rm- wq64n542y9j****** | The instance ID. |

**Examples**

Request example

```
http(s)://[Endpoint]/?Action=DescribeLocalAvailableRecoveryTime &DBInstanceId=rm-wq64n542y9j****** &<common request parameters>
```

Successful response example `JSON` format

```
HTTP/1.1 200 OK Content-Type:application/json
```

`{`

```json
 "RequestId":"9B7BFB11-C077-4FE3-B051-F69CEB******",
 "Message":"Successful",
 "Data":{
  "RecoveryEndTime":"2026-01-26T13:01:15Z",
  "RecoveryBeginTime":"2026-01-21T04:30:32Z",
  "DBInstanceName":"rm-wq64n542y9j******"
```

`},`

```json
 "Success":true
```

`}` `XML` format

```xml
<RequestId>9B7BFB11-C077-4FE3-B051-F69CEB******</RequestId> <Message>Successful</Message> <Data>
 <RecoveryEndTime>2026-01-26T13:01:15Z</RecoveryEndTime>
 <RecoveryBeginTime>2026-01-21T04:30:32Z</RecoveryBeginTime>
 <DBInstanceName>rm-wq64n542y9j******</DBInstanceName>
</Data> <Success>true</Success>
```

**Error codes**

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | InvalidDBInstanceN ame.NotFound | IInvalidDBInstanceName.NotFo und | The specified instance ID does not exist. |
| 400 | MissingUserID | MissingUserID | The request is missing a user id parameter. _ |
| 400 | MissingUID | MissingUID | The request is missing a uid parameter. |

#### 1.6.7 ModifyBackupPolicy

Modifies the backup policy configured for an instance. PolarDB periodically backs up an instance based on the user-defined system configuration.

| Parameter | Type | Requ ired | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set this parameter to ModifyBackupPolicy. |
| DBInstanceId | String | Yes | The instance ID. |
| PreferredBackupTim e | String | Yes | The time range for backups, in UTC. Format: HH:mmZ- HH:mmZ. |
| PreferredBackupPeri od | String | Yes | The backup day. Valid values: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, and Sunday. |

| BackupRetentionPeri od | String | No | The data backup retention period. Unit: days. Valid values: 1 to 30. Default value: 7. |
|---|---|---|---|
| BackupLog | String | No | Specifies whether to enable log backup. Valid values: Enable and Disabled. Default value: Enable. |
| LogBackupRetention Period | String | No | The log backup retention period. It cannot exceed BackupRetentionPeriod. Unit: days. Valid values: 1 to 30. This parameter takes effect only when BackupLog is set to Enable. This parameter is supported only for PolarDB for MySQL, PolarDB for PostgreSQL, or PolarDB for PPAS instances. |

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> | - | For more information, see Common response parameters. |

**Examples**

**Sample requests**

```
https://polardb.example.com/?Action=ModifyBackupPolicy &DBInstanceId=polardb-xxxxx &PreferredBackupTime=00:00Z-01:00Z &PreferredBackupPeriod=Monday &<Common request parameters>
```

XML format

```xml
<ModifyBackupPolicyResponse> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> </ModifyBackupPolicyResponse>
```

JSON format

```json
{ "RequestId":"1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC"}
```

#### 1.6.8 RestoreDBInstance

Restores an instance from a backup set. Before you call this operation, make sure that the following requirements are met: The instance is in the running state. The instance is not undergoing migration tasks. The instance is not locked. The backup set is complete.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to RestoreDBInstance. |
| DBInstanceId | String | Yes | The instance ID. |
| BackupId | Integer | Yes | The backup set ID. |

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> | - | For more information, see Common response parameters. |

**Examples**

**Sample requests**

```
https://polardb.example.com/?Action=RestoreDBInstance &BackupId=103312 &DBInstanceId=polardb-xxxxx &<Common request parameters>
```

XML format

```xml
<RestoreDBInstanceResponse> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> </RestoreDBInstanceResponse>
```

JSON format

```json
{"RequestId":"1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC"}
```

#### 1.6.9 DeleteBackup

Deletes data backup files that have been stored for longer than seven days or longer than the log backup retention period. This operation deletes only the specified backup sets of a specific instance. It does not delete the backup sets of associated instances, such as read-only, disaster recovery, or cloned instances. Before you call this operation, make sure that the instance is in the Running state.

| Paramete r | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DeleteBackup. |
| DBInstanc eId | String | Yes | The instance ID. |
| BackupId | String | Yes | The backup set ID. You can call the DescribeBackups operation to query backup set IDs. You can specify up to 100 backup set IDs in a single request. Separate multiple IDs with commas (,). Among the query results of DescribeBackups, you can delete only backup sets that are in the enabled state. |

For more information, see Common response parameters.

### 1.7 Plugin management

#### 1.7.1 Uninstall a plugin

Uninstalls a plugin.

**Request headers**

This operation uses common request headers. For more information, see Common request parameters.

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| Action | Strin g | Syst em | Yes | DeleteExtensions | The operation that you want to perform. Set the value to DeleteExtensions. |

| AccessKeyI d | Strin g | Quer y | No | LTAI4G28PhwnizaSC***** *** | The AccessKey ID of the account. |
|---|---|---|---|---|---|
| OwnerId | Long | Quer y | No | 123456**** | The system-defined parameter. The ID of the user account. |
| ResourceO wnerAccou nt | Strin g | Quer y | No | aliyun123 | The system-defined parameter. The ID of the resource owner account. |
| ResourceO wnerId | Long | Quer y | No | 123456**** | The ID of the user account to which the resource belongs. |
| ClientToke n | Strin g | Quer y | No | 6000170000591aed949d 0f54a343f1a4233c1e7d1 c5c****** | The client token that is used to ensure the idempotence of the request and prevent duplicate submissions. You must generate a unique value for this parameter for different requests. The value is case-sensitive and can contain up to 64 ASCII characters. |
| proxyId | Strin g | Quer y | No | 1 | The ID of the proxy mode. |
| ZoneId | Strin g | Quer y | No | cn-hangzhou-i | The ID of the zone to which the vSwitch belongs. |
| ResourceG roupId | Strin g | Quer y | No | rg-************ | The ID of the resource group to which the vSwitch belongs. |
| DBInstanc eId | Strin g | Quer y | Yes | pc-**************** | The ID of the instance. |

| Extensions | Strin g | Quer y | Yes | pase,hstore | The plug-ins to be uninstalled. Separate multiple plug-ins with commas (,). |
|---|---|---|---|---|---|
| DBNames | Strin g | Quer y | Yes | auto test db _ _ | The name of the database in the instance. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 9B7BFB11-C077- 4FE3-B051- F69CEB****** | The ID of the request. |
| Message | String | Successful | The returned message. |
| Success | Boolean | true | Indicates whether the request succeeded. Valid values: true: The request succeeded. false: The request failed. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DeleteExtensions &Action=DeleteExtensions &DBInstanceId=pc-**************** &Extensions=pase,hstore &DBNames=auto_test_db &Common request parameters
```

`JSON` format

```
HTTP/1.1 200 OK Content-Type:application/json
```

`{`

```json
 "RequestId":"9B7BFB11-C077-4FE3-B051-F69CEB******",
 "Message":"Successful",
 "Success":true
```

`}` `XML` format

```xml
<RequestId>9B7BFB11-C077-4FE3-B051-F69CEB******</RequestId> <Message>Successful</Message> <Success>true</Success>
```

**Error codes**

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | InvalidInnerParame ter | InvalidInnerParameter | The inner parameter is invalid. |
| 400 | InvalidDBInstanceE ngineType.Format | InvalidDBInstanceEngineType. Format | The DB instance engine type does not support this operation. |
| 400 | InvalidDBInstanceE ngineVersion.Form at | InvalidDBInstanceEngineVersio n.Format | The DB instance engine version does not support this operation. |
| 403 | IncorrectDBInstanc eState | IncorrectDBInstanceState | The current DB instance state does not support this operation. |
| 403 | IncorrectDBInstanc e | IncorrectDBInstance | The current DB instance does not support this operation. |
| 400 | InvalidParameters. Format | InvalidParameters.Format | The specified parameters are not valid. |
| 400 | ExtensionNum.Not Support | ExtensionNum.NotSupport | The current extension count exceeds the maximum supported extension count. |
| 400 | InvalidDBName.For mat | InvalidDBName.Format | The specified DB name is not valid. |
| 400 | EventTriggerExistIn CurDB | EventTriggerExistInCurDB | An event trigger exists in the current database. |
| 404 | InvalidAccountNam e.NotFound | InvalidAccountName.NotFound | The specified account name does not exist. |
| 403 | UnsupportDBOwne rForExtensionOps | UnsupportDBOwnerForExtensi onOps | The DBOwner does not support the specified extensions. |

| 400 | Extension.NotInstal l | Extension.NotInstall | The extensions are not installed. |
|---|---|---|---|
| 400 | Extension.Depende ncy | Extension.Dependency | The required extension list exists, but some extensions are missing. |
| 400 | -2001 | Extension.Dependency.Invalid | The required extension list exists, but some extensions are missing: %s |

#### 1.7.2 Update a plugin

Updates a plugin.

**Request headers**

This operation uses common request headers. For more information, see Common request parameters.

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| Action | Strin g | Syst em | Yes | UpdateExtensions | The operation that you want to perform. Set the value to UpdateExtensions. |
| AccessKeyI d | Strin g | Quer y | No | LTAI4G28PhwnizaSC***** *** | The AccessKey ID of the account. |
| OwnerId | Long | Quer y | No | 123456**** | The system-defined parameter. The ID of the user account. |
| ResourceO wnerAccou nt | Strin g | Quer y | No | aliyun123 | The system-defined parameter. The ID of the resource owner account. |
| ResourceO wnerId | Long | Quer y | No | 123456**** | The ID of the user account that owns the resource. |

| ClientToke n | Strin g | Quer y | No | 6000170000591aed949d 0f54a343f1a4233c1e7d1 c5c****** | The client token that is used to ensure the idempotence of the request and prevent duplicate submissions. You must generate a unique value for this parameter for different requests. The value is case-sensitive and can contain up to 64 ASCII characters. |
|---|---|---|---|---|---|
| proxyId | Strin g | Quer y | No | 1 | The ID of the proxy mode. |
| ZoneId | Strin g | Quer y | No | cn-hangzhou-i | The ID of the zone where the vSwitch resides. |
| ResourceG roupId | Strin g | Quer y | No | rg-********** | The ID of the resource group to which the vSwitch belongs. |
| DBInstanc eId | Strin g | Quer y | Yes | pc-**************** | The ID of the instance. |
| Extensions | Strin g | Quer y | Yes | postgres fdw _ | The plugins to be updated. Separate multiple plugins with commas (,). |
| DBNames | Strin g | Quer y | Yes | auto test db _ _ | The name of the database in the instance. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 9B7BFB11-C077- 4FE3-B051- F69CEB****** | The ID of the request. |
| Message | String | Successful | The returned message. true: The request succeeded. false: The request failed. |
| Success | Boolean | true | Indicates whether the request succeeded. Valid values: |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=UpdateExtensions &Action=UpdateExtensions &DBInstanceId=pc-**************** &Extensions=postgres_fdw &DBNames=auto_test_db &Common request parameters
```

`JSON` format

```
HTTP/1.1 200 OK Content-Type:application/json
```

`{`

```json
 "RequestId":"9B7BFB11-C077-4FE3-B051-F69CEB******",
 "Message":"Successful",
 "Success":true
```

`}` `XML` format

```xml
<RequestId>9B7BFB11-C077-4FE3-B051-F69CEB******</RequestId> <Message>Successful</Message> <Success>true</Success>
```

**Error codes**

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | InvalidInnerParame ter | InvalidInnerParameter | The inner parameter is invalid. |
| 400 | InvalidDBInstanceE ngineType.Format | InvalidDBInstanceEngineType. Format | The DB instance engine type does not support this operation. |
| 400 | InvalidDBInstanceE ngineVersion.Form at | InvalidDBInstanceEngineVersio n.Format | The DB instance engine version does not support this operation. |
| 403 | IncorrectDBInstanc eState | IncorrectDBInstanceState | The current DB instance state does not support this operation. |
| 403 | IncorrectDBInstanc e | IncorrectDBInstance | The current DB instance does not support this operation. |

| 400 | InvalidParameters. Format | InvalidParameters.Format | The specified parameters are not valid. |
|---|---|---|---|
| 400 | ExtensionNum.Not Support | ExtensionNum.NotSupport | The current extension count exceeds the maximum supported extension count. |
| 400 | InvalidDBName.For mat | InvalidDBName.Format | The specified DB name is not valid. |
| 404 | InvalidDBName.Not Found | InvalidDBName.NotFound | One or more of the specified DB names do not exist, or the DB status does not support the operation. |
| 400 | EventTriggerExistIn CurDB | EventTriggerExistInCurDB | An event trigger exists in the current DB. |
| 403 | UnsupportDBOwne rForExtensionOps | UnsupportDBOwnerForExtensi onOps | The DBOwner does not support the specified extensions. |
| 404 | InvalidDBName.Not Found | InvalidDBName.NotFound | One or more of the specified DB names do not exist, or the DB status does not support the operation. |
| 400 | Extension.NotInstal l | Extension.NotInstall | The extensions are not installed. |
| 403 | CurMinorVersionUn supportUpdateGive nExtension | CurMinorVersionUnsupportUpd ateGivenExtension | The current minor version does not support updating the given extension. |
| 400 | Extension.Depende ncy | Extension.Dependency | The database was not found. |

#### 1.7.3 Query details of a plugin

Queries details of an installed plugin.

**Request headers**

This operation uses common request headers. For more information, see Common request parameters.

| 0 |   |   |   | > D | ocument Version: 2026063 |
|---|---|---|---|---|---|

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| Action | Strin g | Syst em | Yes | DescribeExtensions | The operation that you want to perform. Set the value to DescribeExtensions. |
| AccessKeyI d | Strin g | Quer y | No | LTAI4G28PhwnizaSC***** *** | The AccessKey ID. |
| OwnerId | Long | Quer y | No | 123456**** | The system-defined parameter. The account ID of the user. |
| ResourceO wnerAccou nt | Strin g | Quer y | No | aliyun123 | The system-defined parameter. The account ID of the resource owner. |
| ResourceO wnerId | Long | Quer y | No | 123456**** | The account ID of the resource owner. |
| ClientToke n | Strin g | Quer y | No | 6000170000591aed949d 0f54a343f1a4233c1e7d1 c5c****** | The client token that is used to ensure the idempotence of the request and prevent duplicate submissions. You must generate a unique value for this parameter across different requests. The value is case-sensitive and can contain up to 64 ASCII characters. |
| proxyId | Strin g | Quer y | No | 1 | The ID of the proxy mode. |
| ZoneId | Strin g | Quer y | No | cn-hangzhou-i | The ID of the zone where the vSwitch is deployed. |
| ResourceG roupId | Strin g | Quer y | No | rg-************ | The ID of the resource group to which the vSwitch belongs. |
| DBInstanc eId | Strin g | Quer y | Yes | pc-**************** | The instance ID. |

| Extension Name | Strin g | Quer y | No | address standardizer _ | The name of the plugin. |
|---|---|---|---|---|---|
| DBName | Strin g | Quer y | Yes | testdb | The name of the database. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 9B7BFB11-C077- 4FE3-B051- F69CEB****** | The ID of the request. |
| Message | String | success | The returned message. |
| Success | Boolean | true | Indicates whether the request succeeded. Valid values: true: The request succeeded. false: The request failed. |
| Data | Struct | list | The list of plugins. |
| - UninstalledExt ensions | Array | Information about the plugins that are not installed in the specified database. | Information about the plugins that are not installed in the specified database. |
| --Name | String | jueming | The name of the plugin. |
| -- DefaultVersion | String | 7.7 | The default version of the plugin. |
| --Comment | String | test | The purpose of the plugin. |
| --Owner | String | admin | The user who owns the plugin. |
| --Priority | String | 1 | The priority of the plugin. |
| --Requires | String | ganos networking _ | The plugins on which this plugin depends during installation. |

| --Category | String | geography space, _ self develop _ | The type of the plugin. |
|---|---|---|---|
| --Restart | String | true | Indicates whether to restart the application. Valid values: true: Restart the application. false: Do not restart the application. |
| - InstalledExten sions | Array | Information about the plugins that are installed in the specified database. | Information about the plugins that are installed in the specified database. |
| --Name | String | jueming | The name of the plugin. |
| -- DefaultVersion | String | 7.7 | The default version of the plugin. |
| -- InstalledVersio n | String | 7.7 | The currently installed version of the plugin. |
| --Comment | String | test | The remarks. |
| --Owner | String | 9527952**** | The user who owns the plugin. |
| --Priority | String | 1 | The priority of the plugin. |
| --Requires | String | ganos networking _ | The plugins on which this plugin depends during installation. |
| --Category | String | geography space, _ self develop _ | The type of the plugin. |
| --Restart | String | true | Indicates whether to restart the application. Valid values: true: Restart the application. false: Do not restart the application. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeExtensions &Action=DescribeExtensions &DBInstanceId=pc-**************** &DBName=testdb &Common request parameters
```

`JSON` format

```
HTTP/1.1 200 OK Content-Type:application/json
```

`{`

```json
 "RequestId":"9B7BFB11-C077-4FE3-B051-F69CEB******",
 "Message":"success",
 "Data":{
  "UninstalledExtensions":[
```

`{`

```json
    "Comment":"test",
    "Owner":"admin",
    "Category":"geography_space, self_develop",
    "Requires":"ganos_networking",
    "Priority":"1",
    "DefaultVersion":"7.7",
    "Restart":"true",
    "Name":"jueming"
```

`}` `],`

```json
  "InstalledExtensions":[
```

`{`

```json
    "Comment":"test",
    "Owner":"9527952****",
    "Category":"geography_space, self_develop",
    "InstalledVersion":"7.7",
    "Requires":"ganos_networking",
    "Priority":"1",
    "DefaultVersion":"7.7",
    "Restart":"true",
    "Name":"jueming"
```

`}` `]` `},`

```json
 "Success":true
```

`}` `XML` format

```xml
<RequestId>9B7BFB11-C077-4FE3-B051-F69CEB******</RequestId> <Message>success</Message> <Data>
 <UninstalledExtensions>
  <Comment>test</Comment>
  <Owner>admin</Owner>
  <Category>geography_space, self_develop</Category>
  <Requires>ganos_networking</Requires>
  <Priority>1</Priority>
  <DefaultVersion>7.7</DefaultVersion>
  <Restart>true</Restart>
  <Name>jueming</Name>
 </UninstalledExtensions>
 <InstalledExtensions>
  <Comment>test</Comment>
  <Owner>9527952****</Owner>
  <Category>geography_space, self_develop</Category>
  <InstalledVersion>7.7</InstalledVersion>
  <Requires>ganos_networking</Requires>
  <Priority>1</Priority>
  <DefaultVersion>7.7</DefaultVersion>
  <Restart>true</Restart>
  <Name>jueming</Name>
 </InstalledExtensions>
</Data> <Success>true</Success>
```

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | InvalidInnerParame ter | InvalidInnerParameter | The inner parameter is invalid. |
| 400 | InvalidDBInstanceE ngineType.Format | InvalidDBInstanceEngineType. Format | The DB instance engine type does not support this operation. |
| 400 | InvalidDBInstanceE ngineVersion.Form at | InvalidDBInstanceEngineVersio n.Format | The DB instance engine version does not support this operation. |
| 403 | IncorrectDBInstanc eState | IncorrectDBInstanceState | The current DB instance state does not support this operation. |

| 403 | IncorrectDBInstanc e | IncorrectDBInstance | The current DB instance does not support this operation. |
|---|---|---|---|
| 400 | InvalidParameters. Format | InvalidParameters.Format | The specified parameters are not valid. |
| 404 | InvalidAccountNam e.NotFound | InvalidAccountName.NotFound | The specified account name does not exist. |
| 403 | IncorrectAccountLo ckState | IncorrectAccountLockState | The account is in a locked state. |
| 400 | InvalidDBName.For mat | InvalidDBName.Format | The specified DB name is not valid. |
| 400 | Extension.Depende ncy | Extension.Dependency | The database was not found. |
| 404 | InternalError.Exten sionConfigNotFoun d | InternalError.ExtensionConfigN otFound | The extension configuration was not found. |
| 400 | InternalError.Exten sionConfigEmpty | InternalError.ExtensionConfigE mpty | The extension configuration is empty. |

#### 1.7.4 Install plugins

Installs plugins.

**Request headers**

This operation uses common request headers. For more information, see Common request parameters.

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| Action | Strin g | Syst em | Yes | CreateExtensions | The operation that you want to perform. Set the value to CreateExtensions. |

| AccessKeyI d | Strin g | Quer y | No | LTAI4G28PhwnizaSC***** *** | The AccessKey ID of the account. |
|---|---|---|---|---|---|
| OwnerId | Long | Quer y | No | 123456**** | The system-defined parameter. The ID of the user account. |
| ResourceO wnerAccou nt | Strin g | Quer y | No | aliyun123 | The system-defined parameter. The ID of the resource owner account. |
| ResourceO wnerId | Long | Quer y | No | 123456**** | The ID of the user account that owns the resource. |
| ClientToke n | Strin g | Quer y | No | 6000170000591aed949d 0f54a343f1a4233c1e7d1 c5c****** | The client token that is used to ensure the idempotence of the request and prevent duplicate submissions. You must generate a unique value for this parameter across different requests. The value is case-sensitive and can contain up to 64 ASCII characters. |
| proxyId | Strin g | Quer y | No | 1 | The ID of the proxy mode. |
| ZoneId | Strin g | Quer y | No | cn-hangzhou-i | The ID of the zone where the vSwitch is deployed. |
| ResourceG roupId | Strin g | Quer y | No | rg-************ | The ID of the resource group to which the vSwitch belongs. |
| DBInstanc eId | Strin g | Quer y | Yes | pc-**************** | The ID of the cluster. |
| Extensions | Strin g | Quer y | No | address standardizer _ | The name of the plugin. Separate multiple plugins with commas (,). |
| DBNames | Strin g | Quer y | Yes | testdb01 | The name of the database on which you want to install the plugin. |

| SourceDB Name | Strin g | Quer y | No | testdb1 | This parameter is invalid. |
|---|---|---|---|---|---|
| AccountNa me | Strin g | Quer y | Yes | test acc _ | The name of the account. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 9B7BFB11-C077- 4FE3-B051- F69CEB****** | The ID of the request. |
| Message | String | Successful | The returned message. true: The request succeeded. false: The request failed. |
| Success | Boolean | true | Indicates whether the request succeeded. Valid values: |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=CreateExtensions &Action=CreateExtensions &DBInstanceId=pc-**************** &DBNames=testdb01 &AccountName=test_acc &Common request parameters
```

`JSON` format

```
HTTP/1.1 200 OK Content-Type:application/json
```

`{`

```json
 "RequestId":"9B7BFB11-C077-4FE3-B051-F69CEB******",
 "Message":"Successful",
 "Success":true
```

`}` `XML` format

```xml
<RequestId>9B7BFB11-C077-4FE3-B051-F69CEB******</RequestId> <Message>Successful</Message> <Success>true</Success>
```

**Error codes**

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | InvalidInnerParame ter | InvalidInnerParameter | The inner parameter is invalid. |
| 400 | InvalidDBInstanceE ngineType.Format | InvalidDBInstanceEngineType. Format | The DB instance engine type does not support this operation. |
| 400 | InvalidDBInstanceE ngineVersion.Form at | InvalidDBInstanceEngineVersio n.Format | The DB instance engine version does not support this operation. |
| 403 | IncorrectDBInstanc eState | IncorrectDBInstanceState | The current DB instance state does not support this operation. |
| 403 | IncorrectDBInstanc e | IncorrectDBInstance | The current DB instance does not support this operation. |
| 400 | InvalidParameters. Format | InvalidParameters.Format | The specified parameters are not valid. |
| 404 | InvalidAccountNam e.NotFound | InvalidAccountName.NotFound | The specified account name does not exist. |
| 403 | IncorrectAccountPri vilegeType | IncorrectAccountPrivilegeType | The current account privilege type does not support this operation. |
| 403 | IncorrectAccountLo ckState | IncorrectAccountLockState | The accountName is in a locked state. |
| 400 | InvalidSourceDb | InvalidSourceDb | The specified SourceDb is not valid. |
| 400 | InvalidDBName.For mat | InvalidDBName.Format | The specified DB name is not valid. |

| 400 | EventTriggerExistIn CurDB | EventTriggerExistInCurDB | An event trigger exists in the current DB. |
|---|---|---|---|
| 400 | ExtensionNum.Not Support | ExtensionNum.NotSupport | The current extension count exceeds the maximum supported extension count. |
| 400 | Extension.Depende ncy | Extension.Dependency | The database was not found. |
| 404 | InvalidDBName.Not Found | InvalidDBName.NotFound | One or more of the specified DB names do not exist, or the DB status does not support this operation. |
| 403 | UnsupportDBOwne rForExtensionOps | UnsupportDBOwnerForExtensi onOps | The DBOwner does not support the specified extensions. |
| 403 | CurMinorVersionPG 17UnsupportVector | CurMinorVersionPG17Unsuppo rtVector | The current minor version of pg17 does not support vector. |
| 403 | CurrentMinorVersio nUnsupportSpecifie dExtensions | CurrentMinorVersionUnsupport SpecifiedExtensions | The current minor version does not support the specified extensions. |
| 403 | PolarCsiExtensionN eedLogicalWalLeve l | PolarCsiExtensionNeedLogical WalLevel | The Polar CSI extension requires logical WAL level. |
| 404 | InternalError.Exten sionConfigNotFoun d | InternalError.ExtensionConfigN otFound | The extension configuration was not found. |
| 400 | InternalError.Exten sionConfigEmpty | InternalError.ExtensionConfigE mpty | The extension configuration is empty. |
| 400 | AccountNameOwne rNotDBOwner | AccountNameOwnerNotDBOw ner | The account name is not the owner of the database. |

### 1.8 Monitoring management

#### 1.8.1 DescribeResourceUsage

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
| BackupSize | Integer | The disk space that is used to store backup files. Unit: bytes. -1 indicates no space is used. |
| ColdBackupSize | Integer | The total space occupied by cold backup data. Unit: bytes. -1 indicates that no space is used. |
| SQLSize | Integer | The total space occupied by SQL data. Unit: bytes. -1 indicates that no space is used. |

#### 1.8.2 DescribeDBInstancePerformance

Queries the performance metrics of an instance over a period of time based on the performance parameters. The output format depends on the length of the query time range: If the query time range is less than or equal to one day, performance metrics are displayed at one-minute intervals. Queries with the time range from one to seven days are not supported. If the query time range is greater than seven days but less than or equal to 15 days, performance metrics are displayed at one-hour intervals. Queries with the time range greater than 15 days but less than 30 days are not supported. If the query time range is greater than or equal to 30 days but less than or equal to one year, performance metrics are displayed at one-day intervals.

**Note**

If the instance space usage key is MySQL_SpaceUsage, performance metric data can be queried only when the query time range is less than or equal to one day.

| Paramet er | Type | Requir ed | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeDBInstancePerformance. |
| DBInstan ceId | String | Yes | The instance ID. |
| Key | Intege r | Yes | The performance metrics. Separate multiple metrics with commas (,). |
| StartTime | String | Yes | The beginning of the time range to query. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mmZ format. The time must be in UTC. Example: 2012-06-11T15:00Z. |
| EndTime | String | Yes | The end of the time range to query. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mmZ format. The time must be in UTC. Example: 2012-06-11T15:00Z. |

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> | - | The common response parameters. |
| DBInstanceId | String | The instance ID. |
| Engine | String | The database engine. |
| StartTime | String | The beginning of the time range where the query was executed. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mmZ format. The time is displayed in UTC. Example: 2025-05-30T03:29Z . |

| EndTime | String | The end of the time range where the query was executed. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mmZ format. The time is displayed in UTC. The end time is later than the start time. Example: 2025-05-30T04:29Z . |
|---|---|---|
| PerformanceKey s | List<PerformanceKe y> | The list of performance metrics. Format: {perf1, perf2, perf3, …} . |

| {perf1, |   |
|---|---|

|   | perf2, perf3, …} |
|---|---|

**Examples**

**Sample requests**

```
https://polardb.example.com/?Action=DescribeDBInstancePerformance &DBInstanceId=polardb-xxxxx &key= PolarDB_PG_xxxxx &StartTime=2025-05-30T03:29Z &EndTime=2025-05-30T04:29Z &<Common request parameters>
```

XML format

```xml
<DescribeDBInstancePerformanceResponse> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> <DBInstanceID>polardb-xxxxx</DBInstanceID> <StartTime>2025-05-30T03:29Z</StartTime> <EndTime>2025-05-30T04:29Z</EndTime> <Engine>PolarDB_PG</Engine> <PerformanceKeys> <PerformanceKey> <Key>MySQL_xxxxx</Key> <Unit>KB</Unit> <ValueFormat>recv_k&amp;sent_k</ValueFormat> <Values><Values/> </PerformanceKey> </PerformanceKeys> </DescribeDBInstancePerformanceResponse>
```

JSON format

```json
{ "RequestId"1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC, "DBInstanceID": polardb-xxxxx, "StartTime": "2025-05-30T03:29Z", "EndTime": "2025-05-30T04:29Z", "Engine": "PolarDB_PG", "PerformanceKeys":
    { PerformanceKey[ {
        "Key": "PolarDB_PG_xxxxx",
        "Unit": "KB",
        "ValueFormat": "recv_k&sent_k",
        "Values": { "PerformanceValue":[] } } ] }}
```

#### 1.8.3 DescribeDBInstanceMonitor

You can call this operation to query the monitoring behavior of an instance.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeDBInstanceMonitor. |
| DBInstance Id | String | Yes | The instance ID. |

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> | - | For more information, see Common response parameters. |
| Period | String | The monitoring data collection interval. Unit: seconds. |

#### 1.8.4 ModifyDBInstanceMonitor

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

### 1.9 Parameter management

#### 1.9.1 DescribeParameterTemplates

Queries a list of parameter templates. The list includes parameter names, default parameter values, whether the parameters can be modified, whether the database must be restarted for the parameters to take effect, and regular expressions that act as parameter validation rules.

| Paramete r | Typ e | Requi red | Description |
|---|---|---|---|
| Action | Strin g | Yes | The operation that you want to perform. Set the value to DescribeParameterTemplates. |
| Engine | Strin g | Yes | The database engine. Set the value to PolarDB PG. _ |
| EngineVer sion | Strin g | Yes | The database engine version. Valid values: 14 16 |

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> | - | The common response parameters. |
| Engine | String | The database engine. |

| EngineVersion | String | The database engine version. |
|---|---|---|
| ParameterCount | Integer | The number of parameters. |
| Parameters | List<TemplateRecord > | The list of parameters. Format: {parameter1, parameter2, parameter3, ...} . |

|   |   | {parameter1, |
|---|---|---|
|   | parameter2, parameter3, ...} |   |

**Examples**

**Sample requests**

```
https://polardb.example.com/?Action=DescribeParameterTemplates &Engine=PolarDB_PG &EngineVersion=16 &<Common request parameters>
```

XML format

```xml
<DescribeParameterTemplatesResponse> <Engine>PolarDB_PG</Engine> <EngineVersion>16</EngineVersion> <ParameterCount>1</ParameterCount> <Parameters> <TemplateRecord> <CheckingCode>[0-100]</CheckingCode> <ForceRestart>True</ForceRestart> <Factor>1</Factor> <ParameterDescription>test</ParameterDescription> <ParameterName>fill factor</ParameterName> <ParameterValue>0</ParameterValue> <ForceModify>True</ForceModify> <Unit>INT</Unit> </TemplateRecord> </Parameters> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> </DescribeParameterTemplatesResponse>
```

JSON format

```json
{"Engine": "PolarDB_PG", "EngineVersion": "16", "ParameterCount":1, "Parameters":
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

#### 1.9.2 DescribeParameters

Queries the parameter settings of an instance.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeParameters. |
| DBInstanceId | String | Yes | The instance ID. |

| Parameter | Type |   | Description |   |   |
|---|---|---|---|---|---|
| <Common response parameters> | - |   | The common response parameters. |   |   |
| Engine | String |   | The database engine. |   |   |
| EngineVersion | String |   | The database engine version. |   |   |
| RunningParameters | List<DBInstanceParameter> |   | The list of active parameters. Format: {parameter1,parameter2,para meter3, ...} . |   |   |
|   |   |   |   | {parameter1,parameter2,para |   |
|   |   |   | meter3, ...} |   |   |

| ConfigParameters | List<DBInstanceParameter> | The list of parameters awaiting synchronization. Format: {parameter1,parameter2,para meter3, ...} . |   |
|---|---|---|---|

|   | meter3, ...} |
|---|---|

DBInstanceParameter

| Parameter | Type | Description |
|---|---|---|
| ParameterName | String | The parameter name. |
| ParameterValue | String | The parameter value. |
| ParameterDescription | String | The parameter description. |

**Examples**

**Sample requests**

```
https://polardb.example.com/?Action=DescribeParameters &DBInstanceId=polardb-xxxxx &<Common request parameters>
```

XML format

```xml
<DescribeParametersResponse> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> <Engine>PolarDB_PG</Engine > <EngineVersion>16</EngineVersion> <RunningParameters> <DBInstanceParameter> <ParameterDescription>test</ParameterDescription> <ParameterName>fill factor</ParameterName> <ParameterValue>0</ParameterValue> </DBInstanceParameter> </RunningParameters> <ConfigParameters> <DBInstanceParameter> <ParameterDescription>test1</ParameterDescription> <ParameterName>fill factor</ParameterName> <ParameterValue>50</ParameterValue> </DBInstanceParameter> </ConfigParameters> </DescribeParametersResponse>
```

JSON format

```json
{ "ConfigParameters": {
    "DBInstanceParameter": [ {
        "ParameterDescription": "test",
        "ParameterName": "fill factor",
        "ParameterValue": "50" } ] },
    "Engine": "PolarDB_PG",
    "EngineVersion": "16",
    "RunningParameters": {
        "DBInstanceParameter": [ {
            "ParameterDescription": "test1",
            "ParameterName": "fill factor",
            "ParameterValue": "0" } ] },
    "RequestId": "1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC"}
```

#### 1.9.3 ModifyParameter

Modifies the parameters of an instance. After you submit the parameter modification request, PolarDB starts a task to apply the new parameter values to the instance. If a database restart is required for a new parameter value to take effect, PolarDB restarts the database. Before you call this operation, make sure that the following requirements are met: The instance is in the running state. The instance is not locked. Parameter values fall into the following categories: Numeric range (1-65535): The minimum and maximum values are extracted by using regular expressions. Input parameters are validated against this range and must also be a multiple of a specific factor. Fixed values (utf8, gbk, and latin1): The valid values are extracted by using regular expressions. Input parameters are validated against these fixed values. Other: Values in this category must match a defined regular expression. Before the task is started, PolarDB performs the following parameter checks:
1. Checks whether the parameters exist.
2. Checks whether the parameters can be modified.
3. Checks whether the parameters are valid.
If a parameter is invalid, PolarDB returns the 400 HTTP status code and information about the invalid parameter.

```json
{"HttpStatusCode":400, "Code":"InvalidParameter.Format", "Message":"Specified parameter is not valid. [auto_increment_increment:a,character_set_client:41]"}
```

| Parameter | Type | Require d | Description |
|---|---|---|---|

| Action | String | Yes | The operation that you want to perform. Set the value to ModifyParameter. |
|---|---|---|---|
| DBInstanceI d | String | Yes | The instance ID. |
| Parameters | String | Yes | The JSON string of the parameters and their values. The parameter values must be of the string type. {"auto increment increment":"1", _ _ "character set client":"utf8"}. _ _ |
| Forcerestart | String | No | Specifies whether to forcibly restart the database. Valid values: true and false. If a parameter can take effect only after a database restart, Forcerestart must be set to true. Otherwise, the parameter modification does not take effect. Default value: false. |

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> | - | For more information, see Common response parameters. |

**Examples**

**Sample requests**

```
https://polardb.example.com/?Action=ModifyeParameter &DBInstanceId=polardb-xxxxx &Parameters={"key_buffer_size":"456","character_set_client":"gbk"} &<Common request parameters>
```

XML format

```xml
<ModifyeParameterResponse> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> </ModifyeParameterResponse>
```

JSON format

```json
{ "RequestId":"1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC",}
```

### 1.10 Log management

#### 1.10.1 DescribeSlowLogs

Queries the slow log summary of a database in an instance over a period of time. This operation supports pagination.

| Paramet er | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeSlowLogs. |
| DBInstan ceId | String | Yes | The instance ID. |
| StartTime | String | Yes | The beginning of the time range to query. Specify the date in the ISO 8601 standard in the yyyy-MM-ddZ format. The time must be in UTC. Example: 2011-05-30Z. |
| EndTime | String | Yes | The end of the time range to query. The end date must be later than the start date. Specify the date in the ISO 8601 standard in the yyyy-MM- ddZ format. The time must be in UTC. Example: 2011-05- 30Z. |
| DBName | String | No | The database name. |
| SortKey | String | No | The dimension based on which the system sorts the entries to return. Valid values: TotalExecutionCounts: in descending order of the total number of execution times. TotalQueryTimes: in descending order of the total execution duration. TotalLogicalReads: in descending order of the total number of logical reads. |
| PageSize | Integer | No | The number of entries per page. Valid values: 30, 50, and 100. Default value: 30. |
| PageNum ber | Integer | No | The page number. Pages start from page 1. Default value: 1. |

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> |   | The common response parameters. |
| Engine | String | The database engine. |
| StartTime | String | The beginning of the time range where the query was executed. The date follows the ISO 8601 standard in the yyyy-MM-ddZ format. The time is displayed in UTC. Example: 2025-05-30Z. |
| EndTime | String | The end of the time range where the query was executed. The date follows the ISO 8601 standard in the yyyy-MM-ddZ format. The time is displayed in UTC. Example: 2025-06-30Z. |
| TotalRecordCou nt | Integer | The total number of entries returned. |
| PageNumber | Integer | The page number. |
| PageRecordCou nt | Integer | The number of SQL statements on the current page. |
| Items | List<SQLSlow Log> | The list of slow logs. |

**Examples**

**Sample requests**

```
https://polardb.example.com/?Action=DescribeSlowLogs &DBInstanceId=polardb-xxxxx &StartTime=2025-05-30Z &EndTime=2025-06-30Z &SortKey= Totaxxxxx &<Common request parameters>
```

XML format

```xml
<DescribeSlowLogsResponse> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> <DBInstanceID>polardb-xxxxx</DBInstanceID> <Engine>PolarDB_PG</Engine> <StartTime>2025-05-30Z</StartTime> <EndTime>2025-06-30Z</EndTime> <TotalRecordCount>1</TotalRecordCount> <PageNumber>1</PageNumber> <PageRecordCount>1</PageRecordCount> <Items> <SQLSlowLog> <SQLText>update test.zxb set id=0 limit 1</SQLText> <MySQLTotalExecutionCounts>178</MySQLTotalExecutionCounts> <MySQLTotalExecutionTimes>189</MySQLTotalExecutionTimes> <TotalLogicalReadcounts>89</TotalLogicalReadcounts> <TotalPhysicalReadcounts>90</TotalPhysicalReadcounts> <ReportTime>2025-06-30Z</ReportTime> </SQLSlowLog> </Items> </DescribeSlowLogsResponse>
```

JSON format

```json
{ "RequestId":"1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC", "StartTime":"2025-05-30Z ", "EndTime":"2025-06-30Z ", "Engine":"PolarDB_PG", "PageNumber":1, "PageRecordCount":1, "TotalRecordCount":1, "Items":{
    "SQLSlowLog":[{
        "SQLText":"update test.zxb set id=0 limit 1",
        "MySQLTotalExecutionCounts":178,
        "MySQLTotalExecutionTimes":189,
        "TotalLogicalReadcounts":89,
        "TotalPhysicalReadcounts":90,
        "ReportTime":"2025-06-30Z" }]}}
```

#### 1.10.2 DescribeSlowLogRecords

Queries the slow log details of a database in an instance over a period of time.

| Paramet er | Type | Requir ed | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeSlowLogRecords. |

| DBInstan ceId | String | Yes | The instance ID. |
|---|---|---|---|
| StartTime | String | Yes | The beginning of the time range to query. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mmZ format. The time must be in UTC. Example: 2011-06-11T15:00Z. |
| EndTime | String | Yes | The end of the time range to query. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mmZ format. The time must be in UTC. The end time must be later than the start time. Example: 2011-06-11T16:00Z. |
| DBName | String | No | The database name. |
| PageSize | Integer | No | The number of entries per page. Valid values: 30, 50, and 100. Default value: 30. |
| PageNum ber | Integer | No | The page number. Pages start from page 1. Default value: 1. |

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> |   | The common response parameters. |
| Engine | String | The database engine. |
| TotalRecordCount | Integer | The total number of entries returned. |
| PageNumber | Integer | The page number. |
| PageRecordCount | Integer | The number of SQL statements on the current page. |
| Items | List<SQLSlowRecord> | - |

SQLSlowRecord

| Parameter | Type | Description |
|---|---|---|

| HostAddress |   | Strin g | The IP address of the host that is used to connect to the database. |   |
|---|---|---|---|---|
| DBName |   | Strin g | The database name. |   |
| SQLText |   | Strin g | The query statement. |   |
| QueryTimes |   | Long | The execution duration of the query. Unit: seconds. |   |
| LockTimes |   | Long | The lock duration of the query. Unit: seconds. |   |
| ParseRowCounts |   | Long | The number of rows parsed by the SQL statement. |   |
| ReturnRowCount s |   | Long | The number of entries returned. |   |
| ExecutionStartTi me |   | Strin g | The beginning of the time range where the query was executed. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC. Example: 2025-06-11 T15:00:08Z . |   |
|   |   |   | T15:00:08Z |   |

**Examples**

**Sample requests**

```
https://polardb.example.com/?Action=DescribeSlowLogRecords &DBInstanceId=rm-xxxxx &StartTime=2025-06-11 T15:00:08Z &EndTime=2025-06-11 T16:00:08Z &<Common request parameters>
```

XML format

```xml
<DescribeSlowLogRecordsResponse> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> <DBInstanceID>rm-xxxxx</DBInstanceID> <Engine>PolarDB_PG</Engine> <TotalRecordCount>1</TotalRecordCount> <PageNumber>1</PageNumber> <PageRecordCount>1</PageRecordCount> <Items> <SQLSlowRecord> <HostAddress>192.168.0.123</HostAddress> <DBName>test</DBName> <SQLText>update test.zxb set id=0 limit 1</SQLText> <QueryTimes>123</QueryTimes> <LockTimes>12</LockTimes> <ParseRowCounts>125</ParseRowCounts> <ReturnRowCounts>1</ReturnRowCounts> <ExecutionStartTime>2025-06-11T15:00:08Z</ExecutionStartTime> </SQLSlowRecord> </Items> </DescribeSlowLogRecordsResponse>
```

JSON format

```json
{ "RequestId":"1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC", "Engine":"PolarDB_PG", "PageNumber":1, "PageRecordCount":1, "TotalRecordCount":1, "Items":{
 "SQLSlowRecord":[{
  HostAddress:"192.168.0.123",
  DBName:"test",
  SQLText:"update test.zxb set id=0 limit 1",
  QueryTimes:"123",
  LockTimes:"12",
  ParseRowCounts:"125",
  ReturnRowCounts:"1",
  ExecutionStartTime:"2025-06-11T15:00:08Z"}]}}
```

#### 1.10.3 DescribeErrorLogs

Queries the error logs generated for an instance over a period of time.

| Paramete r | Ty pe | Requ ired | Description |
|---|---|---|---|
| Action | Stri ng | Yes | The operation that you want to perform. Set the value to DescribeErrorLogs. |

| DBInstanc eId | Stri ng | Yes | The instance ID. |
|---|---|---|---|
| StartTime | Stri ng | Yes | The beginning of the time range to query. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mmZ format. The time must be in UTC. Example: 2011-05-30T12:10Z. |
| EndTime | Stri ng | Yes | The end of the time range to query. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mmZ format. The time must be in UTC. The end time must be later than the start time. Example: 2011- 05-30T20:10Z. |
| PageSize | Inte ger | No | The number of entries per page. Valid values: 30, 50, and 100. Default value: 30. |
| PageNum ber | Inte ger | No | The page number. Pages start from page 1. Default value: 1. |

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> |   | For more information, see Common response parameters. |
| TotalRecordCount | Integer | The total number of entries returned. |
| PageNumber | Integer | The page number. |
| PageRecordCount | Integer | The number of error logs on the current page. |
| Items | List<ErrorLogs> | - |

ErrorLogs

| Parameter | Type | Description |
|---|---|---|
| ErrorInfo | String | The error log information. |
| CreateTime | String | The time when the error log was generated. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC. Example: 2011-05-30T12:11:4Z. |

**Examples**

**Sample requests**

```
https://polardb.example.com/?Action=DescribeErrorLogs &DBInstanceId=polardb-xxxxx &StartTime=2011-06-11T15:00Z &EndTime=2011-06-11T20:00Z &<Common request parameters>
```

XML format

```xml
<DescribeErrorLogsResponse> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> <TotalRecordCount>1</TotalRecordCount> <PageNumber>1</PageNumber> <PageRecordCount>1<PageRecordCount> <Items> <ErrorLog> <ErrorInfo>spid52 DBCC TRACEON 3499, server process ID (SPID) 52. This is an informat ional message only; no user action is required</ErrorInfo> <CreateTime>2013-06-04T15:00:00</CreateTime> </ErrorLog> </Items> </DescribeErrorLogsResponse>
```

JSON format

```json
{"RequestId":"1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC", "PageNumber":1, "TotalRecordCount":1, "PageRecordCount":1, "Items":{
 "ErrorLog":[{
  ErrorInfo:"spid52 DBCC TRACEON 3499, server process ID (SPID) 52. This is an inform
ational message only; no user action is required",
  CreateTime:"2013-06-04T15:00:00"}]}}
```

#### 1.10.4 DescribeSQLCollectorPolicy

Checks whether the SQL collection feature is enabled for a PolarDB instance.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeSQLCollectorPolicy. |

| DBInstanceId | String | Yes | The instance ID. |
|---|---|---|---|

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> |   | For more information, see Common response parameters. |
| SQLCollectorStatu s | String | Indicates whether the SQL collection feature is enabled. Valid values: Enable and Disabled. |

#### 1.10.5 ModifySQLCollectorPolicy

Enables or disables the SQL collection feature for an instance.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | Strin g | Yes | The operation that you want to perform. Set the value to ModifySQLCollectorPolicy. |
| DBInstanceId | Strin g | Yes | The instance ID. |
| SQLCollector Status | Strin g | Yes | Specifies whether to enable the SQL collection feature. Valid values: Enable and Disabled. |

For more information, see Common response parameters.

#### 1.10.6 DescribeSQLLogRecords

Queries the SQL audit logs of an instance.

| > Document V | ersion: | 20260630 | 11 |
|---|---|---|---|

| Paramete r | Typ e | Requi red | Description |
|---|---|---|---|
| Action | Stri ng | Yes | The operation that you want to perform. Set the value to DescribeSQLLogRecords. |
| DBInstanc eId | Stri ng | Yes | The instance ID. |
| Database | Stri ng | No | The database name. If you do not specify this parameter, the system queries the SQL audit logs of all databases. |
| User | Stri ng | No | The username. If you do not specify this parameter, the system queries the SQL audit logs of all users. |
| Form | Stri ng | No | The response format. Valid values: File and Stream. If this parameter is set to File, the system returns the SQL audit logs as a file. Only common parameters are returned. To obtain the file download URL, call the DescribeSQLLogFiles operation. If this parameter is set to Stream, the system returns the SQL audit logs as a data stream. Default value: Stream. |
| QueryKey words | Stri ng | No | The keywords that are used for the query. Separate multiple keywords with spaces. You can specify up to 10 keywords. |
| StartTime | Stri ng | Yes | The beginning of the time range to query. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC. |
| EndTime | Stri ng | Yes | The end of the time range to query. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC. The end time must be later than the start time. |
| PageSize | Inte ger | No | The number of entries per page. Valid values: 30, 50, 100, and 200. Default value: 100. |
| PageNumb er | Inte ger | No | The page number. Pages start from page 1. Default value: 1. |

| Parameter | Type | Description |
|---|---|---|

| <Common response parameters> | - | For more information, see Common response parameters. |
|---|---|---|
| TotalRecordCount | Integer | The total number of entries returned. |
| PageNumber | Integer | The page number. |
| PageRecordCount | Integer | The number of SQL audit logs on the current page. |
| Items | List<SQLRecord > | The list of SQL audit logs. |

SQLRecord

| Parameter | Type | Description |
|---|---|---|
| DBName | String | The database name. |
| AccountName | String | The account name. |
| HostAddress | String | The IP address of the client. |
| SQLText | String | The executed SQL statement. |
| TotalExecutionTimes | Long | The time that was consumed to execute the SQL statement. Unit: microseconds. |
| ReturnRowCounts | Long | The number of entries returned. |
| ThreadID | String | The thread ID. |
| ExecuteTime | String | The execution time. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC. Example: 2011-05-30T12:11:20Z. |

**Examples**

**Sample requests**

```
https://polardb.example.com/?Action=DescribeSQLLogRecords &DBInstanceId=polardb-xxxxx &StartTime=2011-06-11T15:00:00Z &EndTime=2013-06-05T15:00:00Z &<Common request parameters>
```

XML format

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

#### 1.10.7 DescribeSQLLogFiles

Queries a list of SQL audit log files of an instance.

| Parameter | Type | Require d | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeSQLLogFiles. |
| DBInstanceI d | String | Yes | The instance ID. |

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> |   | For more information, see Common response parameters. |
| TotalRecordCount | Interger | The total number of entries returned. |
| PageNumber | Interger | The page number. |
| PageRecordCount | Interger | The number of entries per page. |
| Items | List<LogFile> | The list of SQL audit log files. |

Parameters in LogFile

| Parameter | Type | Description |
|---|---|---|
| FileID | Interger | The ID of the SQL audit log file. |
| DBInstanceId | String | The instance ID. |
| LogStatus | String | The status of the SQL audit log file. Valid values: Success: The SQL audit log file was generated. Failed: The SQL audit log file failed to be generated. Generating: The SQL audit log file is being generated. |

| LogStartTime | String | The time when the first SQL statement recorded in the audit log file was executed. |
|---|---|---|
| LogEndTime | String | The time when the last SQL statement recorded in the audit log file was executed. |
| LogDownloadU RL | String | The URL for downloading the SQL audit log file. If no download URL is available, an empty string is returned. |
| LogSize | Long | The size of the SQL audit log file. Unit: bytes. |

### 1.11 Data migration

#### 1.11.1 CreateUploadPathForSQLServer

Creates a username and a password for the file server and generates the upload path. You can then use these credentials to upload your data files to the specified path. After the upload is complete, call the data import operation to migrate external data.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to CreateUploadPathForSQLServer. |
| DBInstanceId | String | Yes | The instance ID. |
| DBName | String | Yes | The database name. |

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> | - | For more information, see Common response parameters. |
| InternetFtpServer | String | The IP address of the file server on the public network. |
| InternetPort | Integer | The port of the file server on the public network. |

| IntranetFtpServer | String | The IP address of the file server on the internal network. |
|---|---|---|
| IntranetPort | Integer | The port of the file server on the internal network. |
| UserName | String | The username of the file server. |
| Password | String | The password of the file server. |
| FileName | String | The file name, with the extension. |

**Examples**

**Sample requests**

```
https://polardb.example.com/?Action= CreateUploadPathForSQLServer &DBInstanceId=polardb-xxxxx &DBName=testdb01 &<Common request parameters>
```

XML format

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

#### 1.11.2 ImportDatabaseBetweenInstances

Migrates data from a PolarDB instance. This operation is supported only for dedicated PolarDB for MySQL instances. PolarDB for MySQL instances support batch database migration. During migration, the source instance status changes to Migrating and the destination instance status changes to Importing Data. Database migration is performed between different instances that belong to the same user. Before you call this operation, make sure that the following requirements are met: The source instance is in the running state. The databases to be migrated in the source instance are in the running state. The destination instance is not locked. The reserved storage space of the destination instance is greater than the space calculated by the following formula: Space occupied by the destination instance - Database space of the destination instance + Database space of the source instance. Databases to be migrated exist in both the source and destination instances and are activated.

| Parameter | Type | Requi red | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to ImportDatabaseBetweenInstances. |
| DBInstanceId | String | Yes | The destination instance ID. |
| SourceDBInstan ceId | String | Yes | The ID of the source instance. It cannot be the same as that of the destination instance. |
| DBInfo | String | Yes | The information about the databases to be migrated. Specify this parameter in the JSON format. For PolarDB for MySQL instances, the parameter value is an array. Example: {"DBNames":["mydb","mydb2"]}. The names of the source and destination databases must be the same. In this example, data is migrated from the mydb and mydb2 databases. These databases must exist in both the source and destination instances. |

DBInfo

| Paramet er | Type | Required | Description |
|---|---|---|---|
| DBNames | List | Yes | The names of the databases to be migrated. Example: ["mydb","mydb2"]. |

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> |   | For more information, see Common response parameters. |
| ImportId | Integer | The destination instance ID. |

**Examples**

**Sample requests**

```
https://polardb.example.com/?Action=ImportDatabaseBetweenInstances &DBInstanceId=polardb-xxxxx &SourceDBInstanceId=polardb-xxxxx &{"DBNames":["mydb","mydb2"]} &<Common request parameters>
```

XML format

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

#### 1.11.3 CancelImport

Cancels a migration from a PolarDB for MySQL instance. Migrations from PolarDB for MySQL instances can be canceled.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to CancelImport. |
| DBInstanceId | String | Yes | The instance ID. |

| ImportId | Integer | Yes | The migration task ID. |
|---|---|---|---|

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> | - | For more information, see Common response parameters. |

**Examples**

**Sample requests**

```
https://polardb.example.com/?Action=CancelImport &DBInstanceId=polardb-xxxxx &ImportId=127562 &<Common request parameters>
```

XML format

```xml
<CancelImportResponse> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> </CancelImportResponse>
```

JSON format

```json
{"RequestId": "1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC" }
```

### 1.12 Tag management

#### 1.12.1 AddTagsToResource

Adds existing or newly created tags to instances. Each tag consists of a tag key and a tag value. The tag key cannot be blank, but the tag value can. The tag keys and tag values cannot start with aliyun. The tag keys and tag values are not case-sensitive. The maximum length of a tag key is 64 characters and the maximum length of a tag value is 128 characters. Each instance can have a maximum of 10 tags. Tag keys must be unique for each tag added to an instance. If tags with duplicate tag keys are added to an instance, the last tag added takes precedence.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to AddTagsToResource. |
| RegionId | String | Yes | The region ID. |
| DBInstanceId | String | Yes | The ID of the instance to which a tag is to be added. You can specify up to 30 instance IDs in a single request. Separate multiple IDs with commas (,) Format: instance1,instance2,instance3. |
| Tags | Json String | Yes | The tag to be added. Each tag consists of a tag key and a tag value. You can specify up to five tag pairs in a single request. The tag key is required, and the tag value is optional. Format example: {"key1":"value1","key2":""}. |

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> | - | For more information, see Common response parameters. |

#### 1.12.2 DescribeTags

Queries the tags that are added to a PolarDB instance within an account. If an instance ID is specified, all tags added to the instance are returned, regardless of other filter criteria. If only a tag key is specified, all matching tags are returned. If both a tag key and a tag value are specified, only tags that match both criteria are returned.

| Paramete r | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeTags. |

| RegionId | String | Yes | The region ID. |
|---|---|---|---|
| DBInstanc eId | String | No | The instance ID. If this parameter is specified, all the other filter criteria are ignored. |
| Tags | Json String | No | The tag to be queried. Each tag consists of a tag key and a tag value. The tag key is required, and the tag value is optional. Format: {"key1":"value1"}. |

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> | - | For more information, see Common response parameters. |
| Items | List<TagInfos> | The array that consists of tag data. |

TagInfos

| Parameter | Type | Description |
|---|---|---|
| TagKey | String | The tag key. |
| TagValue | String | The tag value. |
| DBInstanceIds | List<DBInstanceId> | The ID of the instance to which the tag is added. |

DBInstanceId

| Parameter | Type | Description |
|---|---|---|
| DBInstanceId | String | The instance ID. |

#### 1.12.3 RemoveTagsFromResource

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

### 1.13 RAM authorization

**Use RAM to authorize PolarDB resources**

All PolarDB instances that are created within an Apsara Stack tenant account are resources owned by that account. By default, an Apsara Stack tenant account has full permissions on resources that belong to the account. Resource Access Management (RAM) allows you to grant RAM users the access and management permissions on PolarDB resources owned by an Apsara Stack tenant account. If you do not want to use RAM, ignore this topic.

**PolarDB resource types that can be authorized in RAM**

For PolarDB, only instances can be authorized in RAM. The following table describes the Alibaba Cloud Resource Name (ARN) format in which resources are specified in authorization policies when you use RAM to authorize access to the resources.

| Resource type | ARN |
|---|---|

| Instance | acs:polardb:$regionid:$accountid:dbinstance/$dbinstanceid acs:polardb:$regionid:$accountid:dbinstance/ acs:polardb:::dbinstance/ |
|---|---|

Set the $regionid field to a region ID or an asterisk (*). Set the $dbinstanceid field to an instance ID or an asterisk (*). Set the $account-id field to the numerical ID of your Apsara Stack tenant account, which can be replaced by an asterisk (*).

**Operations that can be authorized in RAM**

In RAM, you can authorize a RAM user to call the following operations on PolarDB resources.

| Operation1 | Operation2 |
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
|---|---|
| CreateBackup | DescribeBackups |
| CreateTempDBInstance | DescribeBackupPolicy |
| ModifyBackupPolicy | DescribeResourceUsage |
| DescribeDBInstancePerformance | DescribeSlowLogs |
| DescribeSlowLogRecords | DescribeErrorLogs |
| DescribeBinlogFiles | DescribeSQLLogReports |
| DescribeSQLLogRecords | DescribeOptimizeAdviceOnStorage |
| DescribeOptimizeAdviceOnMissPK | DescribeOptimizeAdviceOnExcessIndex |

**Note**

All operations except DescribeRegions and DescribeParameterTemplates can be authorized.

**RAM authentication rules of API operations**

When you call PolarDB API operations to access resources as a RAM user, PolarDB checks with RAM whether the RAM user is granted the required permissions. The permissions to be checked are determined by the resources that are used by each PolarDB API operation. The following table describes the authentication rules for each API operation.

| Operation | Authentication rule |
|---|---|
| CreateDBInstance | acs:polardb:$regionid:$accountid:dbinstance/$dbinstance id |
| DeleteDBInstance | acs:polardb:$regionid:$accountid:dbinstance/$dbinstance id |
| DescribeDBInstances | acs:polardb:$regionid:$accountid:dbinstance/$dbinstance id |

| SwitchDBInstanceNetType | acs:polardb:$regionid:$accountid:dbinstance/$dbinstance id |
|---|---|
| ModifyDBInstanceDescription | acs:polardb:$regionid:$accountid:dbinstance/$dbinstance id |
| ModifyDBInstanceMaintainTime | acs:polardb:$regionid:$accountid:dbinstance/$dbinstance id |
| PurgeDBInstanceLog | acs:polardb:$regionid:$accountid:dbinstance/$dbinstance id |
| DeleteDatabase | acs:polardb:$regionid:$accountid:dbinstance/$dbinstance id |
| ModifyDBDescription | acs:polardb:$regionid:$accountid:dbinstance/$dbinstance id |
| CancelImport | acs:polardb:$regionid:$accountid:dbinstance/$dbinstance id |
| ResetAccountPassword | acs:polardb:$regionid:$accountid:dbinstance/$dbinstance id |
| RevokeAccountPrivilege | acs:polardb:$regionid:$accountid:dbinstance/$dbinstance id |
| DeleteAccount | acs:polardb:$regionid:$accountid:dbinstance/$dbinstance id |
| CreateBackup | acs:polardb:$regionid:$accountid:dbinstance/$dbinstance id |
| CreateTempDBInstance | acs:polardb:$regionid:$accountid:dbinstance/$dbinstance id |
| ModifyBackupPolicy | acs:polardb:$regionid:$accountid:dbinstance/$dbinstance id |
| DescribeDBInstancePerformance | acs:polardb:$regionid:$accountid:dbinstance/$dbinstance id |
| DescribeSlowLogRecords | acs:polardb:$regionid:$accountid:dbinstance/$dbinstance id |

| DescribeBinlogFiles | acs:polardb:$regionid:$accountid:dbinstance/$dbinstance id |
|---|---|
| DescribeSQLLogRecords | acs:polardb:$regionid:$accountid:dbinstance/$dbinstance id |
| DescribeOptimizeAdviceOnMissPK | acs:polardb:$regionid:$accountid:dbinstance/$dbinstance id |
| DescribeOptimizeAdviceOnMissIndex | acs:polardb:$regionid:$accountid:dbinstance/$dbinstance id |
| DescribeParameters | acs:polardb:$regionid:$accountid:dbinstance/$dbinstance id |
| CreatePrepaidDBInstanceForChannel | acs:polardb:$regionid:$accountid:dbinstance/$dbinstance id |
| ModifyPrepaidDBInstanceSpec | acs:polardb:$regionid:$accountid:dbinstance/$dbinstance id |
| CreatePostpaidDBInstanceForChannel | acs:polardb:$regionid:$accountid:dbinstance/$dbinstance id |
| ModifyPostpaidDBInstanceSpec | acs:polardb:$regionid:$accountid:dbinstance/$dbinstance id |
| DescribeDBInstanceAttribute | acs:polardb:$regionid:$accountid:dbinstance/$dbinstance id |
| RestartDBInstance | acs:polardb:$regionid:$accountid:dbinstance/$dbinstance id |
| ModifySecurityIps | acs:polardb:$regionid:$accountid:dbinstance/$dbinstance id |
| UpgradeDBInstanceEngineVersion | acs:polardb:$regionid:$accountid:dbinstance/$dbinstance id |
| CreateDatabase | acs:polardb:$regionid:$accountid:dbinstance/$dbinstance id |

| DescribeDatabases | acs:polardb:$regionid:$accountid:dbinstance/$dbinstance id |
|---|---|
| ImportDataBaseBetweenInstances | acs:polardb:$regionid:$accountid:dbinstance/$dbinstance id |
| CreateAccount | acs:polardb:$regionid:$accountid:dbinstance/$dbinstance id |
| GrantAccountPrivilege | acs:polardb:$regionid:$accountid:dbinstance/$dbinstance id |
| DescribeAccounts | acs:polardb:$regionid:$accountid:dbinstance/$dbinstance id |
| ModifyAccountDescription | acs:polardb:$regionid:$accountid:dbinstance/$dbinstance id |
| DescribeBackups | acs:polardb:$regionid:$accountid:dbinstance/$dbinstance id |
| DescribeBackupPolicy | acs:polardb:$regionid:$accountid:dbinstance/$dbinstance id |
| DescribeResourceUsage | acs:polardb:$regionid:$accountid:dbinstance/$dbinstance id |
| DescribeSlowLogs | acs:polardb:$regionid:$accountid:dbinstance/$dbinstance id |
| DescribeErrorLogs | acs:polardb:$regionid:$accountid:dbinstance/$dbinstance id |
| DescribeSQLLogReports | acs:polardb:$regionid:$accountid:dbinstance/$dbinstance id |
| DescribeOptimizeAdviceOnStorage | acs:polardb:$regionid:$accountid:dbinstance/$dbinstance id |
| DescribeOptimizeAdviceOnExcessIndex | acs:polardb:$regionid:$accountid:dbinstance/$dbinstance id |
| DescribeOptimizeAdviceByDBA | acs:polardb:$regionid:$accountid:dbinstance/$dbinstance id |

| ModifyeParameter | acs:polardb:$regionid:$accountid:dbinstance/$dbinstance id |
|---|---|

### 1.14 Appendix

#### 1.14.1 Client error codes

##### 1.14.1.1 Common errors

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

##### 1.14.1.2 Specific errors

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
|---|---|---|
| OperationDenied.DBInstanceType | The operation is not permitted due to type of instance. | 400 |
| OperationDenied.DBInstanceStorag eReduce | The operation is not permitted due to reduce storage. | 403 |
| OperationDenied.DBInstanceStatus | The operation is not permitted due to instance status. | 403 |
| DependencyViolation | The operation is not permitted due to instance mount read only or guard instance. | 403 |
| InvalidConnectionStringPrefix.Dupli cate | The connection string is not in the available range or occupied. | 400 |
| QuotaExceeded.SwitchTime | The quota of switch time exceed. | 400 |
| OperationDenied.LockMode | The operation is not permitted due to lock of instance. | 403 |
| InvalidSecurityIps.Duplicate | The quota of security ip exceeds. | 400 |
| OperationDenied.CurrentEngineVer sion | The operation is not permitted due to specified current version . | 400 |
| OperationDenied.ReadOnlyDBInstan ceLower | The operation is not permitted due to higher read only instance version . | 403 |
| OperationDenied.GuardDBInstanceL ower | The operation is not permitted due to higher guard instance version . | 403 |
| OperationDenied.MasterDBInstance State | The operation is not permitted due to status of master instance. | 403 |
| QuotaExceeded.DBName | The quota of db exceeds. | 400 |
| InvalidDBName.Duplicate | The Security db Name is not in the available range or occupied. | 400 |

| InvalidParameter.Keyword | The specified parameter "DBName" is keyword | 400 |
|---|---|---|
| OperationDenied.DBStatus | The operation is not permitted due to status of database. | 403 |
| OperationDenied.DBInstanceEngine | The operation is not permitted due to engine of instance. | 403 |
| FTPServiceUnavailable | The request has failed due to a temporary failure of the FTP server. | 403 |
| QuotaExceeded.Upload | The quota of file exceeds. | 403 |
| InvalidFileName.NotCompleted | The specified "FileName" is not completed . | 404 |
| InvalidFileName.NotAvailable | The specified "FileName" is not Available . | 404 |
| QuotaExceeded.FileSize | The quota of file size exceeds. | 403 |
| QuotaExceeded.DBInstanceStorage | The quota of instance storage exceeds. | 403 |
| InvalidDBInfo.Malformed | The specified parameter "DBInfo" is not valid or db not exist. | 400 |
| OperationDenied.Region | The operation is not permitted due to different region. | 403 |
| OperationDenied.Engine | The operation is not permitted due to different engine. | 403 |
| OperationDenied.DBInstanceId | The operation is not permitted due to DBInstanceId and SourceDBInstanceId is same. | 403 |
| InvalidTaskId.NotFound | The ImportId provided does not exist in our records. | 400 |
| OperationDenied.IncorrectTaskStat us | The operation is not permitted due to status of import. | 403 |
| InvalidAccountName.keyword | The specified parameter "AccountName" is a keyword. | 400 |

| InvalidAccountName.Duplicate | The Security db Name is not in the available range or occupied. | 400 |
|---|---|---|
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
|---|---|---|
| IncorrecttVpcId.Mismatch | The specified parameter "VpcId " is not valid. | 400 |
| IntranetNetTypeNotExists | Current DB instance net type does not support this operation. | 404 |
| InvalidDBInstanceName.NotFound | The DBInstanceId provided does not exist in our records. | 403 |
| InvalidConnectionMode.ValueNotSu pported | The specified parameter "ConnectionMode" is not valid. | 400 |
| InvalidConnectionString.Duplicate Specified | connection string already exists in the Aliyun PolarDB. | 403 |
| InvalidConnectionString.Duplicate Specified | connection string or port want to be modified is the same with current net type. | 400 |
| InvalidConnectionStringPrefix.Dupli cated | Specified connection string already exists in the Aliyun PolarDB. | 403 |
| InvalidCurrentConnectionString.Not Found | Specified current connection string doesn't exist. | 400 |
| InvalidDBInstanceId.NotFound | The DBInstanceId provided does not exist in our records. | 400 |
| InvalidDBInstanceId.QuotaExceeded | The quota of instance id exceeds. | 400 |
| InvalidDBInstanceNetType.NotFoun d | The Specified DB instance net type is not found. | 404 |
| InvalidDBinstanceNetType.ValueNot Support | The specified parameter "DBinstanceNetType" is not valid. | 400 |
| InvalidDBInstanceType.ValueNotSu pport | The specified parameter "DBInstanceType" is not valid. | 400 |
| InvalidEngineVersion.Malformed | The specified parameter "EngineVersion" is not valid. | 400 |

| InvalidInstanceNetworkType.ValueN otSupported | The specified parameter "InstanceNetworkType" is not valid. | 400 |
|---|---|---|
| InvalidParameter | The specified parameter "dbInstanceId" is not valid. | 400 |
| InvalidPort.Malformed | Specified port is not valid. | 400 |
| InvalidPrivateIpAddress.Duplicated | Specified private IP address is duplicated. | 400 |
| InvalidPrivateIpAddress.Mismatch | Specified private IP address is not in the CIDR block of virtual switch. | 400 |
| InvalidVPCId.NotFound | Specified virtual vpc is not found. | 400 |
| InvalidVSwitchId.Mismatch | Specified instance and virtual switch are not in the same zone. | 400 |
| InvalidVSwitchId.NotFound | Specified virtual switch is not found in specified VPC. | 400 |
| NetTypeExists | Specified net type already existed. | 400 |
| NetTypeExists | Specified public net type already existed. | 403 |
| OperationDenied.DBInstanceNetTyp e | The operation is not permitted due to net type of instance. | 403 |
| OperationDenied.DBInstanceStatus | The operation is not permitted due to status of instance. | 403 |
| OperationDenied.DBInstanceType | The operation is not permitted due to type of instance. | 403 |
| OperationDenied.LockMode | The operation is not permitted due to lock of instance. | 403 |
| OperationDenied.Switch | Specified instance cannot be switched. | 400 |
| OperationDenied.Switch | Specified instance cannot be switched to VPC. | 403 |

| OperationDenied.SwitchToVPC | Specified instance cannot be switched to VPC. | 403 |
|---|---|---|
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

#### 1.14.2 Error codes on the server

| Error code | Description | HTTP status code |
|---|---|---|
| ServiceUnavailabl e | The request has failed due to a temporary failure of the server. | 503 |
| InternalError | The request processing has failed due to some unknown error, exception or failure. | 500 |

#### 1.14.3 Instance states

| State | Description |
|---|---|
| Creating | The instance is being created. |
| Running | The instance is in the running state. |
| Deleting | The instance is being deleted. |
| Rebooting | The instance is being restarted. |
| DBInstanceClassChanging | The instance is being upgraded or downgraded. |
| TRANSING | Data is being migrated. |
| EngineVersionUpgrading | The engine version is being upgraded. |
| TransingToOthers | The data of the instance is being migrated to another PolarDB instance. |
| GuardDBInstanceCreating | A disaster recovery instance is being created. |
| Restoring | The instance is being restored from a backup. |

| Importing | Data is being imported into the instance. |
|---|---|
| ImportingFromOthers | Data is being imported into the instance from another PolarDB instance. |
| DBInstanceNetTypeChanging | The network type is being switched between the public network and internal network. |
| GuardSwitching | The instance is undergoing a switchover for disaster recovery. |
| INS CLONING _ | The instance is being cloned. |

#### 1.14.4 Character set tables

This topic describes character sets that are supported by PolarDB.

**Character sets supported by PolarDB for PostgreSQL**

| Character set | Character set | Character set |
|---|---|---|
| sql ascii _ | iso 8859 6 _ _ | win866 |
| euc jp _ | iso 8859 7 _ _ | win874 |
| euc cn _ | iso 8859 8 _ _ | win1250 |
| euc kr _ | latin1 | win1251 |
| euc tw _ | latin2 | win1252 |
| euc jis 2004 _ _ | latin3 | win1253 |
| utf8 | latin4 | win1254 |
| mule internal _ | latin5 | win1255 |
| gbk | latin6 | win1256 |
| gb18030 | latin7 | win1257 |

| koi8r | latin8 | win1258 |
|---|---|---|
| koi8u | latin9 |   |
| iso 8859 5 _ _ | latin10 |   |

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
i. In the left-side navigation pane, choose **Versions > SDK Tools**. ii. Click **Customize SDK** in the upper-right corner. iii. In the **Customize Apsara Stack SDK** dialog box that appears, select an Apsara Stack version, a service name, a service version, an SDK version, an API version, and an SDK language. iv. After you complete the configuration, click **Create SDK**. v. Click **Download** to download the SDK.

### 2.2 SDK for Java

#### 2.2.1 Use the SDK

##### 2.2.1.1 Use CommonRequest to call API operations

If you want to call the API operations of an Apsara Stack service that does not provide SDKs, you can use CommonRequest. You can use CommonRequest to call all API operations.

**Benefits**

CommonRequest provides the following benefits:
1. Lightweight: You need to only download the core package. You do not need to download
and install SDKs of Apsara Stack services.
2. Easy to use: You can call the newly released API operations of an Apsara Stack service
without the need to update the SDK for the service.
3. Fast iteration.

**Use CommonRequest**

If you want to send a CommonRequest request, you must obtain the values of the following parameters. You can obtain the values of the parameters from the API references of cloud services. domain: the endpoint of a service. Version: the version of the API. The version is in the YYYY-MM-DD format. You can obtain the API version from the common parameters in the API references of cloud services. Action: the name of the API operation that you want to call. You must obtain the value of the **Action** parameter and use `request.ApiName = "` `<Action>"` to specify the name of the operation. For example, to use CommonRequest to call the RunInstances operation, you must specify the operation name by using `request.ApiName = "RunInstances"` . You must obtain the value of the **PathPattern** parameter and use `request.PathPattern =` `"<PathPattern>"` to specify the RESTful path. For example, the **PathPattern** parameter of the API operation that is used to query all cluster instances is set to `/clusters` . When you initiate a CommonRequest request, you must specify the RESTful path by using `request.PathPattern = "/clusters"` .

**Example: Call an RPC API operation**

The following sample code shows how to use CommonRequest to call DescribeDBInstanceAttribute:

```java
import com.aliyuncs.CommonRequest; import com.aliyuncs.CommonResponse; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.exceptions.ServerException; import com.aliyuncs.profile.DefaultProfile; public class Sample {
    public static void main(String[] args) {
        // Create a DefaultAcsClient instance and initialize it.
        DefaultProfile profile = DefaultProfile.getProfile(
            "<your-region-id>",          // The ID of the region.
            "<your-access-key-id>",      // The AccessKey ID.
            "<your-access-key-secret>"); // The AccessKey secret.
        IAcsClient client = new DefaultAcsClient(profile);
        // Create an API request and configure parameters.
        CommonRequest request = new CommonRequest();
        request.setDomain("polardb-xxxxx.xxx.com");
        request.setVersion("2024-01-30");
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

`}` `}` `}`

**Example: Call a RESTful API operation**

The following sample code shows how to use CommonRequest to call the API operation to query all cluster instances:

```java
import com.aliyuncs.CommonRequest; import com.aliyuncs.CommonResponse; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.exceptions.ServerException; import com.aliyuncs.profile.DefaultProfile; public class Sample {
    public static void main(String[] args) {
        // Create a DefaultAcsClient instance and initialize it.
        DefaultProfile profile = DefaultProfile.getProfile(
            "<your-region-id>",          // The ID of the region.
            "<your-access-key-id>",      // The AccessKey ID.
            "<your-access-key-secret>"); // The AccessKey secret.
        IAcsClient client = new DefaultAcsClient(profile);
        // Create an API request and configure parameters.
        CommonRequest request = new CommonRequest();
        request.setDomain("polardb-xxxxx.xxx.com");
        request.setVersion("2024-01-30");
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

##### 2.3.1.1 Use CommonRequest to call API operations

If you want to call the API operations of an Apsara Stack service that does not provide SDKs, you can use CommonRequest. You can use CommonRequest to call all API operations.

**Characteristics of CommonRequest calling**

The CommonRequest calling method has the following characteristics: Light weight: You only need the core package to initiate the call, without downloading or installing the SDK of each product. Easy and convenient: You can call the latest API without updating the SDK. Fast iteration

**Use CommonRequest**

To initiate a CommonRequest request, you must obtain the values of the following parameters. You can obtain the values of these parameters from the API document of each product. Domain: the service address of a product Version: the version of the API, which is in the format of YYYY-MM-DD You can obtain the API version from the common parameters in the API document of each product. API information: the name of the API to be called. You must obtain the value of the **Action** parameter and use `request.ApiName = "` `<Action>"` to specify the API name. Take the RunInstances API as an example. You must use `request.ApiName =` `"RunInstances"` to specify the API name when initiating a CommonRequest request. You must obtain the value of the **PathPattern** parameter and use `request.PathPattern =` `"<PathPattern>"` to specify the RESTful path. For example, if the **PathPattern** value of the GetClusterList API is `/clusters` , you must use `request.PathPattern = "/clusters"` to specify the RESTful path when initiating a CommonRequest request.

**Example: Call an RPC API operation**

The following sample code shows how Python 2.x uses CommonRequest to call DescribeDBInstanceAttribute:

```bash
from aliyunsdkcore.client import AcsClient from aliyunsdkcore.request import CommonRequest client = AcsClient('{your_access_key_id}', '{your_access_key_secret}', '{your_region_id}') request = CommonRequest() request.set_domain('polardb-xxxxx.xxx.com') request.set_version('2024-01-30') request.set_action_name('DescribeDBInstanceAttribute')
# or:
# request = CommonRequest(domain='polardb.aliyuncs.com', version='2024-01-30', action_n
ame='DescribeDBInstanceAttribute') request.add_query_param('PageNumber', '1') request.add_query_param('PageSize', '30') response = client.do_action_with_exception(request)
```

**Example: Call a RESTful API operation**

The following sample code shows how Python 2.x uses CommonRequest to call the API operation to query all cluster instances:

```bash
from aliyunsdkcore.client import AcsClient from aliyunsdkcore.request import CommonRequest client = AcsClient('{your_access_key_id}', '{your_access_key_secret}', '{your_region_id}') request = CommonRequest() request.set_domain('polardb-xxxxx.xxx.com') request.set_version('2024-01-30') request.set_uri_pattern('/clusters')
# or:
# request = CommonRequest(domain='polardb.aliyuncs.com', version='2024-01-30', uri_patt
ern='/clusters') response = client.do_action_with_exception(request)
```

### 2.4 SDK for PHP

#### 2.4.1 Getting started

PolarDB SDK for PHP allows you to access PolarDB without performing complex programming operations. This topic describes how to obtain and use PolarDB SDK for PHP.

**Prerequisites**

An Apsara Stack tenant account that has the required permissions and an AccessKey pair that consists of an AccessKey ID and an AccessKey secret are obtained. For more information about how to obtain and view your AccessKey pair in the Apsara Uni-manager Management Console, see Obtain an AccessKey pair. For more information about how to obtain the endpoint of PolarDB, see Obtain an endpoint. PolarDB SDK for PHP is compatible with PHP 5.3, 5.4, 5.5, 5.6, 7.0, and 7.1. You can run the
**php -v** command to obtain your PHP version number.

**Install PolarDB SDK for PHP**

To install PolarDB SDK for PHP, perform the following steps:
1. Download the source code package of PolarDB SDK for PHP from the Apsara Stack official
website.
2. Add the PolarDB SDK for PHP reference to your code.
For example, if the source code package is downloaded to `/path/to/aliyun-openapi-php-` `sdk` , run the following command:

```
require_once '/path/to/aliyun-openapi-php-sdk/aliyun-php-sdk-core/Config.php';
```

**Use PolarDB SDK for PHP**

To use PolarDB SDK for PHP, perform the following steps:
1. Create a DefaultAcsClient instance and initialize the instance.
When you create and initialize a DefaultAcsClient instance, you must provide the values of the **Region ID**, ****************, and ******************** parameters.
2. Create an API request and specify the required parameters.
3. Initiate the API request and manage the response or exceptions.

```bash
<?php use PolarDB\Request\V20140526\DescribeDBInstanceAttributeRequest;
# Create a DefaultAcsClient instance and initialize the instance.
$clientProfile = DefaultProfile::getProfile(
    "<your-region-id>",                   # Your region ID.
    "<your-access-key-id>",               # Your AccessKey ID.
    "<your-access-key-secret>"            # Your AccessKey secret.
```

);

```bash
$client = new DefaultAcsClient($clientProfile);
# Set the endpoint of the service.
$profile->endpoint ="your-region-id", "your-region-id", "product", "endpoint";
# Create an API request and configure its parameters.
$request = new DescribeDBInstanceAttributeRequest(); $request->setPageSize(10);
# Initiate the request and handle the response.
try {
    $response = $client->getAcsResponse($request);
    print_r($response);
} catch(ServerException $e) {
    print "Error: " . $e->getErrorCode() . " Message: " . $e->getMessage() . "\n";
} catch(ClientException $e) {
    print "Error: " . $e->getErrorCode() . " Message: " . $e->getMessage() . "\n";
```

`}` ?>

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

You can obtain the endpoint of PolarDB in the Apsara Uni-manager Operations Console.

**Method 1**

1. Log on to the Apsara Uni-manager Operations Console.
For more information about how to log on to the Apsara Uni-manager Operations Console, see **Basic Apsara Stack operations > Apsara Stack Operations console > Log on to**
**the Apsara Stack Operations console** in **Operations and Maintenance Guide**.
2. In the left-side navigation pane, choose **Products > Product List > Apsara Stack O&M**.
3. Click **Apsara Infrastructure Management Framework** to go to the Apsara
Infrastructure Management Framework console.
4. In the top navigation bar, choose **Reports > System Reports**.
5. On the **System Reports** page, click **Registration Vars of Services**.
6. On the **Registration Vars of Services** page, find the polardb-yaochi row, right-click the
**Service Registration** column, and choose **Show More** from the shortcut menu.
7. In the **Details** dialog box, find the endpoint of PolarDB based on the key value of PolarDB,
which is polardb.openapi.endpoint.

**Method 2**

1. Log on to the Apsara Uni-manager Operations Console.
For more information about how to log on to the Apsara Uni-manager Operations Console, see **Basic Apsara Stack operations > Apsara Stack Operations console > Log on to**
**the Apsara Stack Operations console** in **Operations and Maintenance Guide**.
2. Click **Products** in the left-side navigation pane.
3. Choose **Apsara Infrastructure Management Framework** in the product list to go to the
Apsara Infrastructure Management Framework page.
4. Choose **Operations > Machine Operations**. The **Machine Operations** page appears.
5. Select a server and click **Terminal** to log on to the server.
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
