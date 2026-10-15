---
title: "Alibaba Cloud Apsara Stack v3.18.6-2607 Database Backup Developer Guide 20260828"
product_version: "V3.18.6_2607"
doc_version: "20260828"
pdf_pages: 114
source_pdf: "Alibaba Cloud Apsara Stack v3.18.6-2607 Database Backup Developer Guide 20260828.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/3816%202607/pdf%203/%E6%95%B0%E6%8D%AE%E5%BA%93%E5%A4%87%E4%BB%BD%20DBS/Alibaba%20Cloud%20Apsara%20Stack%20v3.18.6-2607%20Database%20Backup%20Developer%20Guide%2020260828.pdf"
converter: pdf2md (PyMuPDF line classifier)
---

# Alibaba Cloud Apsara Stack v3.18.6-2607 Database Backup Developer Guide 20260828

## API reference

### List of operations by function

The following tables list the API operations that are available for use in Database Backup (DBS).

**Backup schedule**

| Operation | Description |
|---|---|
| CreateBackupPlan | Creates a backup schedule |
| ConfigureBackupPlan | Configures a backup schedule |
| StartBackupPlan | Starts a backup schedule |
| StopBackupPlan | Stops a backup schedule |
| DescribeBackupPlanList | Queries backup schedules |
| ModifyBackupObjects | Modifies backup objects |
| ModifyBackupSourceEndpoint | Modifies the information about a backup source |
| ModifyBackupPlanName | Changes the name of a backup schedule |
| ModifyBackupStrategy | Modifies the backup time settings |
| DescribeRestoreRangeInfo | Queries the details of time ranges to which you can restore data |
| DescribeBackupPlanBilling | Queries the billing information of a backup schedule |

**Backup task**

| Operation | Description |
|---|---|
| DescribeFullBackupList | Queries full backup tasks |
| DescribeIncrementBackupList | Queries incremental backup tasks |

**Restore task**

| Operation | Description |
|---|---|
| CreateRestoreTask | Creates a restore task |
| StartRestoreTask | Starts a restore task |
| DescribeRestoreTaskList | Queries restore tasks |

**Backup gateway**

| Operation | Description |
|---|---|
| DescribeBackupGatewayList | Queries backup gateways |

**Backup set download**

| Operation | Description |
|---|---|
| DescribeBackupSetDownloadTa skList | Queries backup set download tasks |
| ModifyBackupSetDownloadRule s | Configures download rules for backup sets |
| CreateFullBackupSetDownload | Creates a full backup set download task |
| CreateIncrementBackupSetDow nload | Creates an incremental backup set download task |

**Others**

| Operation | Description |
|---|---|
| DescribeJobErrorCode | Queries the standard error information of a DBS task |
| DescribeNodeCidrList | Queries the CIDR blocks of nodes on which DBS is running |
| DescribePreCheckProgressList | Queries the precheck progress of items |

### Backup schedule

#### CreateBackupPlan

Creates a backup schedule.

**Request header**

The CreateBackupPlan operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common headers" section of the "Common parameters" topic.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| Region | Strin g | Quer y | No | cn-hangzhou | The region where Database Backup (DBS) is activated. |
| InstanceCl ass | Strin g | Quer y | Yes | micro | The specification of the backup schedule. Valid values: small large |
| DatabaseT ype | Strin g | Quer y | Yes | MySQL | The type of the database engine. Valid values: MySQL MSSQL Oracle MongoDB Redis |
| BackupMet hod | Strin g | Quer y | Yes | logical | The backup method of the backup schedule. Valid values: logical: logical backup physical: physical backup |
| Period | Strin g | Quer y | No | Month | Specifies whether to use yearly subscription or monthly subscription. |

| UsedTime | Integ er | Quer y | No | 1 | The subscription duration. |
|---|---|---|---|---|---|
| PayType | Strin g | Quer y | No | prepay | The billing method. If you call this operation in Apsara Stack, set the value to prepay. |
| DatabaseR egion | Strin g | Quer y | No | cn-hangzhou | The region where the database is deployed. |
| StorageRe gion | Strin g | Quer y | No | cn-hangzhou | The region where the data is stored. |
| InstanceTy pe | Strin g | Quer y | No | RDS | The type of the database instance. Valid values: RDS DDS Kvstore PolarDB Other: a database instance that is connected by using an IP address and a port number specified in the IP address:Port number format |
| StorageTy pe | Strin g | Quer y | No | None | This parameter is not publicly available. |
| FromApp | Strin g | Quer y | No | OpenAPI | The source of the request. The value is automatically set to OpenAPI and does not need to be changed. Default value: OpenAPI. |
| ClientToke n | Strin g | Quer y | No | KJSAHKJFHKJSHFKASHFKJ ADFHKD**** | The client token that is used to ensure the idempotence of the request. |
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |
| OwnerId | Strin g | Quer y | No | None | This parameter is not publicly available. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 7BCF6D62-885F- 5A4A-91A1- 679760E7**** | The request ID. |
| HttpStatusCod e | Integer | 200 | The HTTP status code. |
| BackupPlanId | String | dbsrhahrsu2**** | The ID of the backup schedule. |
| ErrMessage | String | The specified parameter %s value is not valid. | The error message. |
| OrderId | String | 21437345592**** | The order ID. |
| Success | Boolean | true | Indicates whether the operation is successful. Valid values: true: The operation is successful. false: The operation failed. |
| ErrCode | String | Param.NotFound | The error code. |

**Examples**

Sample requests

```
http(s)://dbs-api.cn-hangzhou.aliyuncs.com/?Action=CreateBackupPlan &InstanceClass=micro &DatabaseType=MySQL &BackupMethod=logical &<Common request parameters>
```

Sample success responses `JSON` format `{`

```json
 "RequestId":"7BCF6D62-885F-5A4A-91A1-679760E7****",
 "HttpStatusCode":200,
 "BackupPlanId":"dbsrhahrsu2****",
 "ErrMessage":"The specified parameter %s value is not valid.",
 "OrderId":"21437345592****",
 "Success":true,
 "ErrCode":"Param.NotFound"
```

`}` `XML` format

```xml
<RequestId>7BCF6D62-885F-5A4A-91A1-679760E7****</RequestId> <HttpStatusCode>200</HttpStatusCode> <BackupPlanId>dbsrhahrsu2****</BackupPlanId> <ErrMessage>The specified parameter %s value is not valid.</ErrMessage> <OrderId>21437345592****</OrderId> <Success>true</Success> <ErrCode>Param.NotFound</ErrCode>
```

Dbs 2019-03-06 Creates a backup schedule

#### ConfigureBackupPlan

Configures a Database Backup (DBS) backup schedule.

**Usage notes**

**Note**

In most cases, if you initiate a request to configure a backup schedule, DBS requires approximately five seconds to respond to your request.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ConfigureBacku pPlan | The operation that you want to perform. Set the value to ConfigureBackupPlan. |
| BackupPlanId | String | Yes | dbstooi0******* | The ID of the backup schedule. |
| BackupPlanNam e | String | Yes | dbstooi0******* | The name of the backup schedule. |

| SourceEndpointI nstanceType | String | Yes | rds | The location of the database. Valid values: RDS ECS Express: The database is connected to DBS by using Express Connect, VPN Gateway, or Smart Access Gateway. Agent: The database is connected to DBS over a DBS backup gateway. DDS: The database is an ApsaraDB for MongoDB (MongoDB) database. Other: The database is connected to DBS by using the IP address and port of the database. |
|---|---|---|---|---|
| SourceEndpoint Region | String | No | cn-hangzhou | The ID of the region where the database is deployed. Note If you specify RDS, ECS, DDS, Express, or Agent as the value of SourceEndpointInstanceType , you must specify this parameter. |
| SourceEndpointI nstanceID | String | No | rm- uf6wjk5xxxxxxx xxx | The ID of the database instance. Note If you specify RDS, ECS, DDS, or Express as the value of SourceEndpointInstanceType , you must specify this parameter. |
| SourceEndpointI P | String | No | rm- uf6wjk5xxxxxxx. mysql.rds.aliyun cs.com | The endpoint of the database. Note If you specify Express, Agent, or Other as the value of SourceEndpointInstanceType , you must specify this parameter. |

| SourceEndpointP ort | Integer | No | 3306 | The port of the database. Note If you specify ECS, Express, Agent, or Other as the value of SourceEndpointInstanceType , you must specify this parameter. |
|---|---|---|---|---|
| SourceEndpoint DatabaseName | String | No | testRds | The name of the database. Note If the database runs the PostgreSQL engine or MongoDB engine, you must specify this parameter. |
| SourceEndpoint UserName | String | No | testRds | The username of the database account. Note If the database runs the Redis engine or if the database is connected to DBS over a DBS backup gateway and runs the MSSQL engine, this parameter is optional. In other cases, you must specify this parameter. |
| SourceEndpointP assword | String | No | testPassword | The password of the database account. Note If the database runs the Redis engine or if the database is connected to DBS over a DBS backup gateway and runs the MSSQL engine, this parameter is optional. In other cases, you must specify this parameter. |

| BackupGatewayI d | Long | No | 23313123312 | The ID of the backup gateway. Note If you set the value of SourceEndpointInstanceType to Agent, you must specify this parameter. |
|---|---|---|---|---|
| OSSBucketName | String | No | TestOssBucket | The name of the Object Storage Service (OSS) bucket. Note By default, the system automatically generates a name for the OSS bucket. |
| BackupObjects | String | No | [{ "DBName":"Nam e of the database that you want to back up", "SchemaName": "Name of the schema that you want to back up", "TableIncludes": [{ "TableName":"N ame of the table that you want to back up" }], "TableExcludes": [{"TableName":" Name of the table that you want to exclude during the backup" }] } ] | The objects that you want to back up. |
| BackupPeriod | String | No | Monday | The full backup cycle. Valid values: Monday Tuesday Wednesday Thursday Friday Saturday Sunday |

| BackupStartTim e | String | No | 14:22 | The start time of the full backup. Specify the value in the HH:mmZ format (UTC). |
|---|---|---|---|---|
| EnableBackupLo g | Boolean | No | true | Specifies whether to enable the incremental log backup feature. Valid values: true false |
| BackupRetentio nPeriod | Integer | No | 730 | The number of days for which the backup data is retained. Valid values: 0 to 1825. Default value: 730. |
| DuplicationInfre quentAccessPeri od | Integer | No | 180 | The number of days after which the storage class of the backup data is changed to Infrequent Access (IA). Default value: 180. |
| DuplicationArchi vePeriod | Integer | No | 365 | The number of days after which the storage class of the backup data is changed to Archive. Default value: 365. |
| SourceEndpoint OracleSID | String | No | test | The system ID (SID) of the Oracle database. If the database runs the Oracle engine, you must specify this parameter. |
| BackupStorageT ype | String | No | system | The built-in storage type. Note If you deploy your business in Apsara Stack, use the default value system. The default value specifies that the system stores backup data in the built-in OSS buckets of DBS. |
| BackupSpeedLi mit | Long | No | 262144 | The I/O limit for the disk. Unit: KB/s. |

| BackupStrategy Type | String | No | simple | The full backup cycle. Valid values: simple: scheduled backup. If you specify this value as the value of BackupStrategyType, you must specify BackupPeriod and BackupStartTime. manual: manual backup. |
|---|---|---|---|---|
| CrossAliyunId | String | No | XXX | This parameter is not supported. |
| CrossRoleName | String | No | XXX | This parameter is not supported. |
| AutoStartBackup | Boolean | No | true | Specifies whether to enable the backup feature. |
| RegionId | String | No | cn-hangzhou | The ID of the region. |
| ClientToken | String | No | ETnLKlblzczshOT UbOCzxxxxxxx | The client token that is used to ensure the idempotence of the request. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| BackupPlanId | String | dbstooi01ex**** | The ID of the backup schedule. |
| ErrCode | String | Param.NotFound | The error code. |
| ErrMessage | String | The specified parameter %s value is not valid. | The error message. |
| HttpStatusCod e | Integer | 200 | The HTTP status code. |
| RequestId | String | F1FB49D4-B504- 47F1-9F43- D7EAB33F**** | The request ID. |
| Success | Boolean | true | Indicates whether the operation is successful. Valid values: true: successful false: failed |

**Examples**

Sample requests

```
http(s)://dbs-api.cn-hangzhou.aliyuncs.com/?Action=ConfigureBackupPlan &BackupPlanId=dbstooi0******* &BackupPlanName=dbstooi0******* &SourceEndpointInstanceType=rds &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RequestId>F1FB49D4-B504-47F1-9F43-D7EAB33F****</RequestId> <HttpStatusCode>200</HttpStatusCode> <BackupPlanId>dbstooi01ex****</BackupPlanId> <ErrMessage>The specified parameter %s value is not valid.</ErrMessage> <Success>true</Success> <ErrCode>Param.NotFound</ErrCode>
```

`JSON` format `{`

```json
    "RequestId": "F1FB49D4-B504-47F1-9F43-D7EAB33F****",
    "HttpStatusCode": 200,
    "BackupPlanId": "dbstooi01ex****",
    "ErrMessage": "The specified parameter %s value is not valid.",
    "Success": true,
    "ErrCode": "Param.NotFound"
```

`}`

#### DescribeBackupPlanList

Queries backup schedules.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeBackup PlanList | The operation that you want to perform. Set the value to DescribeBackupPlanList. |
| BackupPlanId | String | No | dbstooi01ex**** | The ID of the backup schedule that you want to query. Separate multiple IDs with commas (,). |

| Region | String | No | cn-hangzhou | The region where DBS is activated. Note If you deploy your business in Apsara Stack, set the value to the environment initialization region. |
|---|---|---|---|---|
| PageSize | Integer | No | 30 | The number of entries per page. Valid values: 30, 50, and 100. Note Default value: 30. |
| PageNum | Integer | No | 1 | The page number. The value must be an integer that is greater than or equal to 0. Default value: 0. |
| BackupPlanNam e | String | No | test123 | The name of the backup schedule. |
| BackupPlanStatu s | String | No | wait | The status of the backup schedule. Valid values: wait: The backup schedule is not configured. init: The backup schedule is not started and fails to pass the precheck. Running: The backup schedule is running. stop: The backup schedule failed. pause: The backup schedule is paused. locked: The backup schedule is locked. check pass: The backup schedule _ passes the precheck. |
| RegionId | String | No | cn-hangzhou | The region ID. |
| ClientToken | String | No | ASDASDASDSAD ASFCZXVZ | The client token that is used to ensure the idempotence of the request. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| ErrCode | String | Param.NotFound | The response code. |
| ErrMessage | String | The specified parameter %s value is not valid. | The error message. |
| HttpStatusCod e | Integer | 200 | The HTTP status code. |
| Items | Array of BackupPlanDe tail |   | The details of the backup schedules. |
| BackupPlanDe tail |   |   |   |
| BackupGatewa yId | Long | 827362187368736 | The ID of the backup gateway. |
| BackupMethod | String | logical | The method that is used to generate the backup set. Valid values: logical: logical backup physical: physical backup |
| BackupObjects | String | [ { \"DBName\":\"Nam e of the database that you want to back up\", \"SchemaName\":\" Name of the schema that you want to back up\", \"TableIncludes\": [{ \"TableName\":\"Na me of the table that you want to back up\" }], \"TableExcludes\": [{ \"TableName\":\"Na me of the table that you want to exclude during the backup\" }] } ] | The objects that are backed up. |

| BackupPeriod | String | Monday | The full backup cycle. Valid values: Monday Tuesday Wednesday Thursday Friday Saturday Sunday |
|---|---|---|---|
| BackupPlanCr eateTime | Long | 1582527713000 | The time when the backup schedule was created. |
| BackupPlanId | String | dbstooi01e**** | The ID of the backup schedule. |
| BackupPlanNa me | String | test123 | The name of the backup schedule. |
| BackupPlanSta tus | String | init | The status of the backup schedule. Valid values: wait: The backup schedule is not configured. init: The backup schedule is not started and fails to pass the precheck. Running: The backup schedule is running. stop: The backup schedule failed. pause: The backup schedule is paused. locked: The backup schedule is locked. check pass: The backup schedule _ passes the precheck. |
| BackupRetenti onPeriod | Integer | 365 | The number of days for which the backup data is retained. Valid values: 0 to 1825. |
| BackupSetDow nloadDir | String | */test/test123 | The server directory to which the backup set is downloaded. |

| BackupSetDow nloadFullDataF ormat | String | SQL | The format in which the full backup set is downloaded. Valid values: Native SQL CSV JSON |
|---|---|---|---|
| BackupSetDow nloadGatewayI d | Long | 123123 | The ID of the backup gateway that is used to download backup sets. |
| BackupSetDow nloadIncremen tDataFormat | String | SQL | The format in which the incremental backup set is downloaded. Valid values: Native SQL CSV JSON |
| BackupSetDow nloadTargetTy pe | String | agent | The type of the destination server to which the backup set is downloaded. The value is agent, which indicates a server on which a backup gateway is installed. |
| BackupStartTi me | String | 14:22 | The start time of the full backup. The time is displayed in the HH:mm format. _ _ Example: 14:22 . _ _ |
| BackupStorag eType | String | simple | The day of each week when the full backup task runs. Valid values: simple: scheduled backup. If you set the value to simple, you must also specify BackupPeriod and BackupStartTime. manual: manual backup Note Default value: simple. |
| BeginTimesta mpForRestore | Long | 1554560477000 | The beginning of the time range during which the database can be restored. |
| CrossAliyunId | String | 2xxx7778xxxxxxxx xx | This parameter is not supported. |

| CrossRoleNam e | String | test123 | This parameter is not supported. |
|---|---|---|---|
| DuplicationArc hivePeriod | Integer | 365 | The number of days after which the storage class of the backup data is changed to Archive. |
| DuplicationInfr equentAccess Period | Integer | 180 | The number of days after which the storage class of the backup data is changed to Infrequent Access (IA). |
| EnableBackup Log | Boolean | true | Indicates whether incremental log backup is enabled. Valid values: true false |
| EndTimestamp ForRestore | Long | 1554560477000 | The end of the time range during which the database can be restored. |
| ErrMessage | String | can not connect to oracle instance orcl with user dbs | The error message returned about the precheck. |
| InstanceClass | String | micro | The specifications of the backup schedule. Valid values: micro small medium large |
| OSSBucketNa me | String | dbs-backup- 1857XXXXX489 | The name of the Object Storage Service (OSS) bucket. |
| OSSBucketReg ion | String | cn-hangzhou | The region of the OSS bucket. |
| OpenBackupS etAutoDownlo ad | Boolean | true | Indicates whether the automatic backup set download feature is enabled. Valid values: true false |
| SourceEndpoin tDatabaseNam e | String | test | The name of the database. |

| SourceEndpoin tInstanceID | String | test | The ID of the database instance. |
|---|---|---|---|
| SourceEndpoin tInstanceType | String | RDS | The location of the database. Valid values: RDS ECS Express: The database is connected to DBS by using Express Connect, VPN Gateway, or Smart Access Gateway. Agent: The database is connected to DBS over a DBS backup gateway. DDS: The database is a MongoDB database. Other: The database is connected to DBS by using the IP address and port of the database. |
| SourceEndpoin tIpPort | String | 100.*.*.10:33204 | The endpoint of the database. |
| SourceEndpoin tOracleSID | String | test | The system ID (SID) of the Oracle database. |
| SourceEndpoin tRegion | String | cn-hangzhou | The ID of the region where the database is deployed. |
| SourceEndpoin tUserName | String | test | The username of the database account. |
| PageNum | Integer | 1 | The page number. |
| PageSize | Integer | 30 | The number of entries per page. |
| RequestId | String | 4F1888AC-1138- 4995-B9FE- D2734F61**** | The request ID. |
| Success | Boolean | true | Indicates whether the operation is successful. Valid values: true: successful false: failed |
| TotalElements | Integer | 100 | The total number of backup schedules. |

| TotalPages | Integer | 4 | The total number of pages returned. |
|---|---|---|---|

**Examples**

Sample requests

```
http(s)://dbs-api.cn-hangzhou.aliyuncs.com/?Action=DescribeBackupPlanList &BackupPlanId=dbstooi01ex**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<PageSize>30</PageSize> <RequestId>4F1888AC-1138-4995-B9FE-D2734F61****</RequestId> <PageNum>0</PageNum> <HttpStatusCode>200</HttpStatusCode> <TotalElements>1</TotalElements> <Items>
    <BackupPlanDetail>
        <BackupPlanName>dbXXXXX7ltj</BackupPlanName>
        <BackupMethod>logical</BackupMethod>
        <BackupPlanCreateTime>1583000</BackupPlanCreateTime>
        <BackupPeriod>MONDAY</BackupPeriod>
        <BackupObjects>[     {         "DBName":"Name of the database that you want to b
ack up", "SchemaName":"Name of the schema that you want to back up", "Ta bleIncludes":[{ "TableName":"Name of the table that you want to back up" }], "TableExcludes":[{ "TableName":"Name of the table that you want to exclude during the backup" }] } ]</BackupObjects>
        <SourceEndpointInstanceID>rm-bp1p8XXXXXv8pxe</SourceEndpointInstanceID>
        <InstanceClass>medium</InstanceClass>
        <OSSBucketRegion>cn-hangzhou</OSSBucketRegion>
        <SourceEndpointRegion>cn-hangzhou</SourceEndpointRegion>
        <SourceEndpointIpPort>100.X.X.10:33204</SourceEndpointIpPort>
        <DuplicationArchivePeriod>365</DuplicationArchivePeriod>
        <OSSBucketName>dbs-backup-1857XXXXX489</OSSBucketName>
        <BackupPlanStatus>init</BackupPlanStatus>
        <BackupStartTime>14:22</BackupStartTime>
        <EnableBackupLog>true</EnableBackupLog>
        <BackupPlanId>dbXXXXXx7ltj</BackupPlanId>
        <BackupRetentionPeriod>730</BackupRetentionPeriod>
        <SourceEndpointInstanceType>RDS</SourceEndpointInstanceType>
        <SourceEndpointUserName>test</SourceEndpointUserName>
        <DuplicationInfrequentAccessPeriod>180</DuplicationInfrequentAccessPeriod>
    </BackupPlanDetail>
</Items> <TotalPages>1</TotalPages> <Success>true</Success>
```

`JSON` format `{`

```json
 "PageSize": 30,
 "RequestId": "4F1888AC-1138-4995-B9FE-D2734F61****",
 "PageNum": 0,
 "HttpStatusCode": 200,
 "TotalElements": 1,
 "Items": {
  "BackupPlanDetail": [
```

`{`

```json
    "BackupPlanName": "dbXXXXX7ltj",
    "BackupMethod": "logical",
    "BackupPlanCreateTime": 1583000,
    "BackupPeriod": "MONDAY",
    "BackupObjects": "[     {         \"DBName\":\"Name of the database that you want
to back up\", \"SchemaName\":\"Name of the schema that you want to back up\", \"TableIncludes\":[{ \"TableName\":\"Name of the table that you want to back up\" }], \"TableExcludes\":[{ \"TableName\":\"Name of t he table that you want to exclude during the backup\" }] } ]",
    "SourceEndpointInstanceID": "rm-bp1p8XXXXXv8pxe",
    "InstanceClass": "medium",
    "OSSBucketRegion": "cn-hangzhou",
    "SourceEndpointRegion": "cn-hangzhou",
    "SourceEndpointIpPort": "100.X.X.10:33204",
    "DuplicationArchivePeriod": 365,
    "OSSBucketName": "dbs-backup-1857XXXXX489",
    "BackupPlanStatus": "init",
    "BackupStartTime": "14:22",
    "EnableBackupLog": true,
    "BackupPlanId": "dbXXXXXx7ltj",
    "BackupRetentionPeriod": 730,
    "SourceEndpointInstanceType": "RDS",
    "SourceEndpointUserName": "test",
    "DuplicationInfrequentAccessPeriod": 180
```

`}` `]` `},`

```json
 "TotalPages": 1,
 "Success": true
```

`}`

#### StartBackupPlan

Starts a backup schedule.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|

| Action | String | Yes | StartBackupPlan | The operation that you want to perform. Set the value to StartBackupPlan. |
|---|---|---|---|---|
| BackupPlanId | String | Yes | dbstooi01****** | The ID of the backup schedule. |
| RegionId | String | No | cn-hangzhou | The region ID. |
| ClientToken | String | No | ETnLKlblzczshOT UbOCzxxxxxxx | The client token that is used to ensure the idempotence of the request. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| BackupPlanId | String | dbstooi01****** | The ID of the backup schedule. |
| CreatedFullBa ckupsetId | String | dbs1hvb0wwwe*** * | The ID of the full backup set. |
| ErrCode | String | Param.NotFound | The error code. |
| ErrMessage | String | The specified parameter %s value is not valid. | The error message. |
| HttpStatusCod e | Integer | 200 | The HTTP status code. |
| RequestId | String | D6E068C3-25BC- 455A-85FE- 45F0B22E**** | The request ID. |
| Success | Boolean | true | Indicates whether the operation is successful. Valid values: true: successful false: failed |

**Examples**

Sample requests

```
http(s)://dbs-api.cn-hangzhou.aliyuncs.com/?Action=StartBackupPlan &BackupPlanId=dbstooi01****** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RequestId>D6E068C3-25BC-455A-85FE-45F0B22E****</RequestId> <HttpStatusCode>200</HttpStatusCode> <BackupPlanId>dbstooi01******</BackupPlanId> <Success>true</Success>
```

`JSON` format `{`

```json
 "RequestId": "D6E068C3-25BC-455A-85FE-45F0B22E****",
 "HttpStatusCode": 200,
 "BackupPlanId": "dbstooi01******",
 "Success": true
```

`}`

#### StopBackupPlan

Stops a backup schedule.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | StopBackupPlan | The operation that you want to perform. Set the value to StopBackupPlan. |
| BackupPlanId | String | Yes | dbstooi01**** | The ID of the backup schedule. |
| StopMethod | String | Yes | ALL | The operation scope. Valid values: ALL: stops the backup schedule, full data backup tasks, incremental log backup tasks, and restore tasks. PLAN: stops only the backup schedule. |
| RegionId | String | No | cn-hangzhou | The region ID. |

| ClientToken | String | No | ETnLKlblzczshOT UbOCzxxxxxxx | The client token that is used to ensure the idempotence of the request. |
|---|---|---|---|---|

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| BackupPlanId | String | dbs1h****usfa | The ID of the backup schedule. |
| ErrCode | String | Param.NotFound | The error code. |
| ErrMessage | String | The specified parameter %s value is not valid. | The error message. |
| HttpStatusCod e | Integer | 200 | The HTTP status code. |
| RequestId | String | D6E068C3-25BC- 455A-85FE- 45F0B22E**** | The request ID. |
| Success | Boolean | true | Indicates whether the operation is successful. Valid values: true: successful false: failed |

**Examples**

Sample requests

```
http(s)://dbs-api.cn-hangzhou.aliyuncs.com/?Action=StopBackupPlan &BackupPlanId=dbstooi01**** &StopMethod=ALL &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RequestId>D6E068C3-25BC-455A-85FE-45F0B22E****</RequestId> <HttpStatusCode>200</HttpStatusCode> <BackupPlanId>dbs1h****usfa</BackupPlanId> <Success>true</Success>
```

`JSON` format `{`

```json
    "RequestId": "D6E068C3-25BC-455A-85FE-45F0B22E****",
    "HttpStatusCode": 200,
    "BackupPlanId": "dbs1h****usfa",
    "Success": true
```

`}`

#### ModifyBackupObjects

Modifies the backup objects of a backup schedule.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyBackupOb jects | The operation that you want to perform. Set the value to ModifyBackupObjects. |
| BackupObjects | String | Yes | [ { "DBName":"17x xx92xxxx374", "SchemaName": "gy9xnj8xxxxxx" , "TableIncludes": [{ "TableName":"te st1" }], "TableExcludes": [{ "TableName":"te st2" }] } ] | The objects that you want to back up. For more information, see Additional description of request parameters. |
| BackupPlanId | String | Yes | dbs1h****usfa | The ID of the backup schedule whose backup objects you want to modify. You can call the DescribeBackupPlanList operation to query the ID of the backup schedule. |
| RegionId | String | No | cn-hangzhou | The region ID. |
| ClientToken | String | No | ETnLKlblzczshOT UbOCzxxxxxxx | The client token that is used to ensure the idempotence of the request. |

**Additional description of request parameters**

The backup objects that are defined in a JSON string in the following format: `[` `{`

```json
        "DBName":"Name of the database that you want to back up",
        "SchemaName":"Name of the schema that you want to back up",
        "TableIncludes":[{
         "TableName":"Name of the table that you want to back up"
        }],
        "TableExcludes":[{
            "TableName":"Name of the table that you want to exclude during the backup"
```

`}]` `}` `]` If you specify only the `DBName` parameter and do not specify lower levels of objects, all objects in the database are backed up. If you specify the `DBName` parameter and some lower levels of objects, only the specified objects are backed up by default. You can use the following regular expressions to define different object names: A period ( `.` ) matches any single character except \r or \n . An asterisk ( `*` ) matches zero or more occurrences of a subexpression which occurs before. `h.llo` matches strings such as `hllo` and `heeeello` .

| ion mark | ( ? mat |
|---|---|
| h.?llo |   |

A question mark ( ? ) matches zero or one occurrence of a subexpression which occurs before. h.?llo matches `hllo` and `hello` , but does not match `haello` .

| cter class | [characters] |   | ma |
|---|---|---|---|
| h[aello] |   |   |   |
|   |   | matches |   |

The character class `[characters]` matches any character included in the braces. For

| er set |   | does no |
|---|---|---|
| h[^ae]llo |   | hcllo |
|   | matches |   |

`hallo` or `hello` .

| er range | [character1-character2] |   |
|---|---|---|
| character1 to character2 |   |   |
|   |   | , such a |

**Note**

The `SchemaName` and `NewSchemaName` parameters are used only for MS SQL databases. The `DBName` and `NewDBName` parameters are used to define the names of other databases.

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| BackupPlanId | String | dbs1h****usfa | The ID of the backup schedule. |
| ErrCode | String | Param.NotFound | The error code. |

| ErrMessage | String | The specified parameter %s value is not valid. | The error message. |
|---|---|---|---|
| HttpStatusCod e | Integer | 200 | The HTTP status code. |
| NeedPrecheck | Boolean | true | Indicates whether a precheck is triggered. If true is returned, you must call the StartBackupPlan operation again to start the backup schedule. |
| RequestId | String | D6E068C3-25BC- 455A-85FE- 45F0B22E**** | The request ID. |
| Success | Boolean | true | Indicates whether the operation is successful. Valid values: true: successful false: failed |

**Examples**

Sample requests

```
http(s)://dbs-api.cn-hangzhou.aliyuncs.com/?Action=ModifyBackupObjects &BackupObjects=[ { "DBName":"17xxx92xxxx374", "SchemaName":"gy9xnj8xxxxxx", "TableInclu des":[{ "TableName":"test1" }], "TableExcludes":[{ "TableName":"test2" }] } ] &BackupPlanId=dbs1h****usfa &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RequestId>D6E068C3-25BC-455A-85FE-45F0B22E****</RequestId> <HttpStatusCode>200</HttpStatusCode> <BackupPlanId>dbs1h****usfa</BackupPlanId> <Success>true</Success>
```

`JSON` format `{`

```json
 "RequestId": "D6E068C3-25BC-455A-85FE-45F0B22E****",
 "HttpStatusCode": 200,
 "BackupPlanId": "dbs1h****usfa",
 "Success": true
```

`}`

#### ModifyBackupSourceEndpoint

Modifies the information about a data source

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyBackupSo urceEndpoint | The operation that you want to perform. Set the value to ModifyBackupSourceEndpoint. |
| BackupPlanId | String | Yes | dbs1h****usfa | The ID of the backup schedule. You can call the DescribeBackupPlanList operation to query the ID of the backup schedule. |
| SourceEndpointI nstanceType | String | Yes | RDS | The location of the database. Valid values: RDS ECS Express: a database that is connected to DBS by using Express Connect, VPN Gateway, or Smart Access Gateway. Agent: a database that is connected to DBS over a DBS backup gateway. DDS: an ApsaraDB for MongoDB (MongoDB) database. Other: a database that is connected to DBS by using the IP address and port of the database. |
| SourceEndpoint Region | String | No | cn-hangzhou | The region where the database is deployed. Note If you specify RDS, ECS, DDS, Express, or Agent as the value of SourceEndpointInstanceType , you must specify this parameter. |

| SourceEndpointI nstanceID | String | No | rm- bp1p8c29479jvX XXX | The ID of the database instance. Note If you specify RDS, ECS, DDS, or Express as the value of SourceEndpointInstanceType , you must specify this parameter. |
|---|---|---|---|---|
| SourceEndpointI P | String | No | 100.*.*.10:3320 4 | The endpoint of the database. Note If you specify Express, Agent, or Other as the value of SourceEndpointInstanceType , you must specify this parameter. |
| SourceEndpointP ort | Integer | No | 3306 | The port of the database. Note If you specify ECS, Express, Agent, or Other as the value of SourceEndpointInstanceType , you must specify this parameter. |
| SourceEndpoint DatabaseName | String | No | test | The name of the database. Note If the database runs the PostgreSQL engine or MongoDB engine, you must specify this parameter. If you specify Agent as the value of SourceEndpointInstan ceType and the database is an SQL Server database, you must specify this parameter. |

| SourceEndpoint UserName | String | No | test | The username of the database account. Note If you specify Agent as the value of SourceEndpointInstanceType and the database is an SQL Server database or a Redis database, this parameter is optional. In other cases, you must specify this parameter. |
|---|---|---|---|---|
| SourceEndpointP assword | String | No | test | The password of the database account. Note If you specify Agent as the value of SourceEndpointInstanceType and the database is an SQL Server database or a Redis database, this parameter is optional. In other cases, you must specify this parameter. |
| BackupGatewayI d | Long | No | 21321323213 | The ID of the backup gateway. If you specify Agent as the value of SourceEndpointInstanceType, you must specify this parameter. |

| BackupObjects | String | No | [{ "DBName":"Nam e of the database that you want to back up", "SchemaName": "Name of the schema that you want to back up", "TableIncludes": [{ "TableName":"N ame of the table that you want to back up" }], "TableExcludes": [{"TableName":" Name of the table that you want to exclude during the backup" }] } ] | The objects that you want to back up. If you specify Agent as the value of SourceEndpointInstanceType, this parameter is optional. In other cases, you must specify this parameter. |
|---|---|---|---|---|
| SourceEndpoint OracleSID | String | No | test | The system ID (SID) of the Oracle database. If the database is an Oracle database, you must specify this parameter. |
| CrossAliyunId | String | No | 2xxx7778xxxxxx xxxx | The user ID of the account that is used to perform backups accounts. |
| CrossRoleName | String | No | test123 | The name of the Resource Access Management (RAM) role that is used to perform backups across accounts. |
| RegionId | String | No | cn-hangzhou | The region ID. |
| ClientToken | String | No | ETnLKlblzczshOT UbOCzxxxxxxx | The client token that is used to ensure the idempotence of the request. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| BackupPlanId | String | dbs1h****usfa | The ID of the backup schedule. |
| ErrCode | String | Param.NotFound | The error code. |

| ErrMessage | String | The specified parameter %s value is not valid. | The error message. |
|---|---|---|---|
| HttpStatusCod e | Integer | 200 | The HTTP status code. |
| NeedPrecheck | Boolean | false | Indicates whether a precheck is triggered. Valid values: true false Note If true is returned, you must call the StartBackupPlan operation again to start the backup schedule. |
| RequestId | String | D6E068C3-25BC- 455A-85FE- 45F0B22E**** | The request ID. |
| Success | Boolean | true | Indicates whether the operation is successful. Valid values: true: successful false: failed |

**Examples**

Sample requests

```
http(s)://dbs-api.cn-hangzhou.aliyuncs.com/?Action=ModifyBackupSourceEndpoint &BackupPlanId=dbs1h****usfa &SourceEndpointInstanceType=RDS &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RequestId>D6E068C3-25BC-455A-85FE-45F0B22E****</RequestId> <HttpStatusCode>200</HttpStatusCode> <BackupPlanId>dbs1h****usfa</BackupPlanId> <NeedPrecheck>false</NeedPrecheck> <Success>true</Success>
```

`JSON` format `{`

```json
 "RequestId": "D6E068C3-25BC-455A-85FE-45F0B22E****",
 "HttpStatusCode": 200,
 "BackupPlanId": "dbs1h****usfa",
 "NeedPrecheck": false,
 "Success": true
```

`}`

#### ModifyBackupPlanName

Changes the name of a backup schedule.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyBackupPl anName | The operation that you want to perform. Set the value to ModifyBackupPlanName. |
| BackupPlanId | String | Yes | dbstooi0**** | The ID of the backup schedule. You can call the DescribeBackupPlanList operation to query the ID of the backup schedule. |
| BackupPlanNam e | String | Yes | dbstooi0**** | The name of the backup schedule. You can call the DescribeBackupPlanList operation to query the name of the backup schedule. |
| RegionId | String | No | cn-hangzhou | The region ID. |
| ClientToken | String | No | ETnLKlblzczshOT UbOCzxxxxxxx | The client token that is used to ensure the idempotence of the request. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| BackupPlanId | String | dbstooi0**** | The ID of the backup schedule. |
| ErrCode | String | Param.NotFound | The error code. |

| ErrMessage | String | The specified parameter %s value is not valid. | The error message. |
|---|---|---|---|
| HttpStatusCod e | Integer | 200 | The HTTP status code. |
| RequestId | String | D6E068C3-25BC- 455A-85FE- 45F0B22E**** | The request ID. |
| Success | Boolean | true | Indicates whether the operation is successful. Valid values: true: successful false: failed |

**Examples**

Sample requests

```
http(s)://dbs-api.cn-hangzhou.aliyuncs.com/?Action=ModifyBackupPlanName &BackupPlanId=dbstooi0**** &BackupPlanName=dbstooi0**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RequestId>D6E068C3-25BC-455A-85FE-45F0B22E****</RequestId> <HttpStatusCode>200</HttpStatusCode> <BackupPlanId>dbstooi0****</BackupPlanId> <Success>true</Success>
```

`JSON` format `{`

```json
 "RequestId": "D6E068C3-25BC-455A-85FE-45F0B22E****",
 "HttpStatusCode": 200,
 "BackupPlanId": "dbstooi0****",
 "Success": true
```

`}`

#### ModifyBackupStrategy

Modifies the backup time of a backup schedule.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyBackupStr ategy | The operation that you want to perform. Set the value to ModifyBackupStrategy. |
| BackupPeriod | String | Yes | Monday | The full backup cycle. Valid values: Monday Tuesday Wednesday Thursday Friday Saturday Sunday |
| BackupPlanId | String | Yes | dbstooi01**** | The ID of the backup schedule. You can call the DescribeBackupPlanList operation to query the ID of the backup schedule. |
| BackupStartTim e | String | No | 14:22 | The start time of the full backup. Specify the value in the HH:mmZ format in UTC. |
| BackupStrategy Type | String | No | simple | The full backup policy. Valid values: simple: scheduled backup. If you specify this value as the value of BackupStrategyType, you must also specify BackupPeriod and BackupStartTime. manual: manual backup. Note Default value: simple. |
| RegionId | String | No | cn-hangzhou | The region ID. |
| ClientToken | String | No | ETnLKlblzczshOT UbOCzxxxxxxx | The client token that is used to ensure the idempotence of the request. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| BackupPlanId | String | dbstooi01**** | The ID of the backup schedule. |
| ErrCode | String | Param.NotFound | The error code. |
| ErrMessage | String | The specified parameter %s value is not valid. | The error message. |
| HttpStatusCod e | Integer | 200 | The HTTP status code. |
| NeedPrecheck | Boolean | false | Indicates whether a precheck is triggered. Valid values: true false Note If true is returned, you must call the StartBackupPlan operation again to start the backup schedule. |
| RequestId | String | D6E068C3-25BC- 455A-85FE- 45F0B22E**** | The request ID. |
| Success | Boolean | true | Indicates whether the operation is successful. Valid values: true: successful false: failed |

**Examples**

Sample requests

```
http(s)://dbs-api.cn-hangzhou.aliyuncs.com/?Action=ModifyBackupStrategy &BackupPeriod=Monday &BackupPlanId=dbstooi01**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RequestId>D6E068C3-25BC-455A-85FE-45F0B22E****</RequestId> <HttpStatusCode>200</HttpStatusCode> <BackupPlanId>dbstooi01****</BackupPlanId> <NeedPrecheck>false</NeedPrecheck> <Success>true</Success>
```

`JSON` format `{`

```json
 "RequestId": "D6E068C3-25BC-455A-85FE-45F0B22E****",
 "HttpStatusCode": 200,
 "BackupPlanId": "dbstooi01****",
 "NeedPrecheck": false,
 "Success": true
```

`}`

#### DescribeRestoreRangeInfo

Queries the details of time ranges to which you can restore data in a specified backup schedule.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeRestore RangeInfo | The operation that you want to perform. Set the value to DescribeRestoreRangeInfo. |
| BackupPlanId | String | Yes | dbstooi0**** | The ID of the backup schedule. You can call the DescribeBackupPlanList operation to query the ID of the backup schedule. |
| BeginTimestamp ForRestore | Long | Yes | 1554560477000 | The beginning of the time range to which you can restore data. Set the value to 1554560477000. |
| EndTimestampF orRestore | Long | Yes | 1554560477000 | The end of the time range to which you can restore data. Set the value to 1554560477000. |
| RegionId | String | No | cn-hangzhou | The region ID. |

| ClientToken | String | No | ETnLKlblzczshOT UbOCzxxxxxxx | The client token that is used to ensure the idempotence of the request. |
|---|---|---|---|---|
| RecentlyRestore | Boolean | No | true | Specifies whether to query the most recent point in time to which you can restore data. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| ErrCode | String | Param.NotFound | The error code. |
| ErrMessage | String | The specified parameter %s value is not valid. | The error message. |
| HttpStatusCod e | Integer | 200 | The HTTP status code. |
| Items | Array of DBSRecoverRa nge |   | The details of the time range to which you can restore data. |
| DBSRecoverRa nge |   |   |   |
| BeginTimesta mpForRestore | Long | 1554560477000 | The beginning of the time range to which you can restore data, such as 1554560477000. |
| EndTimestamp ForRestore | Long | 1554560477000 | The end of the time range to which you can restore data, such as 1554560477000. |
| FullBackupList | Array of FullBackupDet ail |   | If you set RangeType to point, this parameter is returned. The value of this parameter describes information about all backup points in the time range. The details of the backup point. |
| FullBackupDet ail |   |   |   |
| BackupSetId | String | dbs1hvb***** | The ID of the backup set. |

| EndTime | Long | 1554560477000 | The time when the full backup ended, such as 1554560477000. |
|---|---|---|---|
| StartTime | Long | 1554560477000 | The time when the full backup started, such as 1554560477000. |
| RangeType | String | point | The type of the time range to which you can restore data. point: The time range contains discrete points in time at which full backups were performed. range: The time range is a period of time for which continuous backup was performed. You can specify any point in time in the time range to restore data. |
| SourceEndpoin tInstanceID | String | rm-bp1p8c***** | The ID of the database instance. |
| SourceEndpoin tInstanceType | String | rm-bp1p8c***** | The location of the database instance. |
| RequestId | String | 7A851299-A739- 4801-B4BC- FC30A535**** | The request ID. |
| Success | Boolean | false | Indicates whether the operation is successful. Valid values: true: successful false: failed |

**Examples**

Sample requests

```
http(s)://dbs-api.cn-hangzhou.aliyuncs.com/?Action=DescribeRestoreRangeInfo &BackupPlanId=dbstooi0**** &BeginTimestampForRestore=1554560477000 &EndTimestampForRestore=1554560477000 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<HttpStatusCode>200</HttpStatusCode> <RequestId>7A851299-A739-4801-B4BC-FC30A535****</RequestId> <Items>
    <DBSRecoverRange>
        <BeginTimestampForRestore>1554560477000</BeginTimestampForRestore>
        <EndTimestampForRestore>1554560477000</EndTimestampForRestore>
        <FullBackupList>
            <FullBackupDetail>
                <BackupSetId>dbs1hvb*****</BackupSetId>
                <EndTime>1554560477000</EndTime>
                <StartTime>1554560477000</StartTime>
            </FullBackupDetail>
        </FullBackupList>
        <RangeType>point</RangeType>
        <SourceEndpointInstanceID>rm-bp1p8c*****</SourceEndpointInstanceID>
        <SourceEndpointInstanceType>rm-bp1p8c*****</SourceEndpointInstanceType>
    </DBSRecoverRange>
</Items>
```

`JSON` format `{`

```json
    "HttpStatusCode": 200,
    "RequestId": "7A851299-A739-4801-B4BC-FC30A535****",
    "Items": {
        "DBSRecoverRange": {
            "BeginTimestampForRestore": 1554560477000,
            "EndTimestampForRestore": 1554560477000,
            "FullBackupList": [
```

`{`

```json
                    "FullBackupDetail": {
                        "BackupSetId": "dbs1hvb*****",
                        "EndTime": 1554560477000,
                        "StartTime": 1554560477000
```

`}` `}` `],`

```json
            "RangeType": "point",
            "SourceEndpointInstanceID": "rm-bp1p8c*****",
            "SourceEndpointInstanceType": "rm-bp1p8c*****"
```

`}` `}` `}`

#### DescribeBackupPlanBilling

Queries the billing information of a backup schedule.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeBackup PlanBilling | The operation that you want to perform. Set the value to DescribeBackupPlanBilling. |
| BackupPlanId | String | Yes | dbssl67c7mx*** * | The ID of the backup gateway. You can call the DescribeBackupPlanList operation to query the ID of the backup gateway. |
| RegionId | String | No | cn-hangzhou | The region ID. |
| ClientToken | String | No | ETnLKlblzczshOT UbOCzxxxxxxxx xx | The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |
| ShowStorageTyp e | Boolean | No | true | Specifies whether the storage type is displayed. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| ErrCode | String | InvalidParameter | The error code. |
| ErrMessage | String | This backupPlan can't support this action | The error message. |
| HttpStatusCod e | Integer | 200 | The HTTP status code. |
| Item | Struct |   | The billing information of the backup schedule. |

| BuyChargeTyp e | String | PREPAY | The billing method of the instance. Valid values: PREPAY POSTPAY |
|---|---|---|---|
| BuyCreateTim estamp | Long | 1634700238000 | The timestamp that indicates when the instance was purchased. |
| BuyExpiredTi mestamp | Long | 1716220800000 | The expiration time of the instance. Note This parameter is available only if you set BuyChargeType to PREPAY. |
| BuySpec | String | small | The instance type. |
| ContStorageSi ze | Long | 60391430 | The size of the built-in storage for storing incremental backup data. |
| FullStorageSiz e | Long | 450 | The size of the built-in storage for storing full backup data. |
| IsExpired | Boolean | false | Indicates whether the instance has expired. Note This parameter is available only if you set BuyChargeType to PREPAY. |
| IsFreeBytesUnl imited | Boolean | false | Indicates whether the instance has no backup traffic limit. |
| PaiedBytes | Long | 0 | The total paid backup traffic in the current month. |
| QuotaEndTime stamp | Long | 1640966400000 | The timestamp that indicates when the billing cycle of free backup traffic ends. |
| QuotaStartTim estamp | Long | 1638288000000 | The timestamp that indicates when the billing cycle of free backup traffic starts. |

| TotalFreeBytes | Long | 858993459200 | The total free backup traffic in the current month. Note This parameter is available only if you set BuyChargeType to PREPAY and the value of IsFreeBytesUnlimited is false. |
|---|---|---|---|
| UsedFullBytes | Long | 0 | The paid full backup traffic in the current month. |
| UsedIncremen tBytes | Long | 35389201 | The paid incremental backup traffic in the current month. |
| RequestId | String | B38B76CB-DCA0- 5B84-A4D6- 7BDC7FBF**** | The request ID. |
| Success | Boolean | true | Indicates whether the operation is successful. Valid values: true: successful false: failed |

**Examples**

Sample requests

```
http(s)://dbs-api.cn-hangzhou.aliyuncs.com/?Action=DescribeBackupPlanBilling &BackupPlanId=dbssl67c7mx**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<Item>
    <IsExpired>false</IsExpired>
    <BuyExpiredTimestamp>1716220800000</BuyExpiredTimestamp>
    <FullStorageSize>450</FullStorageSize>
    <BuyCreateTimestamp>1634700238000</BuyCreateTimestamp>
    <IsFreeBytesUnlimited>false</IsFreeBytesUnlimited>
    <ContStorageSize>60391430</ContStorageSize>
    <BuySpec>small</BuySpec>
    <BuyChargeType>PREPAY</BuyChargeType>
</Item> <RequestId>B38B76CB-DCA0-5B84-A4D6-7BDC7FBF****</RequestId> <HttpStatusCode>200</HttpStatusCode> <Success>true</Success>
```

`JSON` format `{`

```json
    "Item": {
        "IsExpired": false,
        "BuyExpiredTimestamp": 1716220800000,
        "FullStorageSize": 450,
        "BuyCreateTimestamp": 1634700238000,
        "IsFreeBytesUnlimited": false,
        "ContStorageSize": 60391430,
        "BuySpec": "small",
        "BuyChargeType": "PREPAY"
```

`},`

```json
    "RequestId": "B38B76CB-DCA0-5B84-A4D6-7BDC7FBF****",
    "HttpStatusCode": 200,
    "Success": true
```

`}`

### Backup task

#### DescribeFullBackupList

Queries full backup tasks.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeFullBac kupList | The operation that you want to perform. Set the value to DescribeFullBackupList. |
| BackupPlanId | String | Yes | dbstooi01**** | The ID of the backup schedule. You can call the DescribeBackupPlanList operation to query the ID of the backup schedule. |
| PageSize | Integer | No | 30 | The number of entries per page. Valid values: 30, 50, and 100. Note Default value: 30. |
| PageNum | Integer | No | 1 | The page number. The value must be a positive integer. Default value: 0. |

| RegionId | String | No | cn-hangzhou | The region ID. |
|---|---|---|---|---|
| ClientToken | String | No | ETnLKlblzczshOT UbOCzxxxxxxx | The client token that is used to ensure the idempotence of the request. |
| ShowStorageTyp e | Boolean | No | true | Specifies whether to return the storage class. Note Default value: true. |
| BackupSetId | String | No | 1ibh2f5u**** | The ID of the backup set. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| ErrCode | String | Param.NotFound | The error code. |
| ErrMessage | String | The specified parameter %s value is not valid. | The error message. |
| HttpStatusCod e | Integer | 200 | The HTTP status code. |
| Items | Array of FullBackupFile |   | The details of the full backup task. |
| FullBackupFile |   |   |   |
| BackupObjects | String | [{\"DBName\":\"tes t\"}] | The objects that are backed up. |
| BackupSetExpi redTime | Long | 1646813439000 | The point in time when the backup set expired, such as 1554560477000. |
| BackupSetId | String | 1ibh2f5u**** | The ID of the backup set. |
| BackupSize | Long | 151 | The size of the backup set. |

| BackupStatus | String | finish | The status of the full backup task. Valid values: schedule: The backup task is being initialized. running: The backup task is running. finish: The backup task is completed. stop: The backup schedule failed. pause: The backup task is paused. |
|---|---|---|---|
| CreateTime | Long | 1583740896000 | The start time of the task, such as 1554560477000. |
| EndTime | Long | 1583741465000 | The end time of the backup, such as 1554560477000. |
| ErrMessage | String | NULL | The error message. |
| FinishTime | Long | 1583741466000 | The end time of the task, such as 1554560477000. |
| SourceEndpoin tIpPort | String | 100.X.X.10:33204 | The endpoint of the database. |
| StartTime | Long | 1583741439000 | The start time of the backup, such as 1554560477000. |
| StorageMetho d | String | Standard | The storage class. Valid values: Standard: The storage class is Standard. IA: The storage class is Infrequent Access (IA). Archive: The storage class is Archive. UNKNOWN: The storage class is unknown. This value is returned because the task is not completed. |
| PageNum | Integer | 1 | The page number. |
| PageSize | Integer | 10 | The number of entries per page. |
| RequestId | String | 636BC118-6080- 4119-A6B5- C199CEC1**** | The request ID. |

| Success | Boolean | true | Indicates whether the operation is successful. Valid values: true: successful false: failed |
|---|---|---|---|
| TotalElements | Integer | 1 | The total number of full backup tasks. |
| TotalPages | Integer | 1 | The total number of pages. |

**Examples**

Sample requests

```
http(s)://dbs-api.cn-hangzhou.aliyuncs.com/?Action=DescribeFullBackupList &BackupPlanId=dbstooi01**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RequestId>636BC118-6080-4119-A6B5-C199CEC1****</RequestId> <PageSize>30</PageSize> <PageNum>0</PageNum> <HttpStatusCode>200</HttpStatusCode> <TotalElements>1</TotalElements> <TotalPages>1</TotalPages> <Items>
    <FullBackupFile>
        <SourceEndpointIpPort>100.X.X.10:33204</SourceEndpointIpPort>
        <StorageMethod>Standard</StorageMethod>
        <BackupObjects>[{"DBName":"test_y"}]</BackupObjects>
        <EndTime>1583741465000</EndTime>
        <FinishTime>1583741466000</FinishTime>
        <BackupSize>151</BackupSize>
        <CreateTime>1583740896000</CreateTime>
        <StartTime>1583741439000</StartTime>
        <BackupSetExpiredTime>1646813439000</BackupSetExpiredTime>
        <BackupSetId>1ibh2f5u****</BackupSetId>
        <BackupStatus>finish</BackupStatus>
    </FullBackupFile>
</Items> <Success>true</Success>
```

`JSON` format `{`

```json
 "RequestId": "636BC118-6080-4119-A6B5-C199CEC1****",
 "PageSize": 30,
 "PageNum": 0,
 "HttpStatusCode": 200,
 "TotalElements": 1,
 "TotalPages": 1,
 "Items": {
  "FullBackupFile": [
```

`{`

```json
    "SourceEndpointIpPort": "100.X.X.10:33204",
    "StorageMethod": "Standard",
    "BackupObjects": "[{\"DBName\":\"test_y\"}]",
    "EndTime": 1583741465000,
    "FinishTime": 1583741466000,
    "BackupSize": 151,
    "CreateTime": 1583740896000,
    "StartTime": 1583741439000,
    "BackupSetExpiredTime": 1646813439000,
    "BackupSetId": "1ibh2f5u****",
    "BackupStatus": "finish"
```

`}` `]` `},`

```json
 "Success": true
```

`}`

#### DescribeIncrementBackupList

Queries incremental backup tasks.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeIncrem entBackupList | The operation that you want to perform. Set the value to DescribeIncrementBackupList. |
| BackupPlanId | String | Yes | dbsqdss5tmh*** * | The ID of the backup schedule. You can call the DescribeBackupPlanList operation to obtain the ID of the backup schedule. |

| PageSize | Integer | No | 30 | The number of entries per page. Valid values: 30, 50, and 100. Note Default value: 30. |
|---|---|---|---|---|
| PageNum | Integer | No | 1 | The page number. The value must be a positive integer. Default value: 0. |
| RegionId | String | No | cn-hangzhou | The region ID. |
| ClientToken | String | No | ETnLKlblzczshOT UbOCzxxxxxxx | The client token that is used to ensure the idempotence of the request. |
| ShowStorageTyp e | Boolean | No | true | Specifies whether to return the storage class. Note Default value: true. |
| StartTimestamp | Long | No | 1570701361528 | The start time of the backup. |
| EndTimestamp | Long | No | 1570701361528 | The end time of the backup. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| ErrCode | String | Param.NotFound | The error code. |
| ErrMessage | String | The specified parameter %s value is not valid. | The error message. |
| HttpStatusCod e | Integer | 200 | The HTTP status code. |
| Items | Array of IncrementBac kupFile |   | The details of the incremental backup task. |

| IncrementBac kupFile |   |   |   |
|---|---|---|---|
| BackupSetExpi redTime | Long | 1710468872000 | The point in time when the backup set expired, such as 1554560477000. |
| BackupSetId | String | mysql-bin.00**** | The ID of the backup set. |
| BackupSetJobI d | String | 1hv5g9wk4**** | The ID of the backup task. |
| BackupSize | Long | 412032 | The size of the backup set. |
| BackupStatus | String | COMPLETED | The status of the incremental backup task. Valid values: INIT: The backup task is being initialized. FILLING: The backup task is running. COMPLETED: The backup task is completed. UNCOMPLETED: The backup task is not completed. |
| EndTime | Long | 1647396866000 | The end time of the backup, such as 1554560477000. |
| SourceEndpoin tIpPort | String | 172.XX.103.1:43XX | The endpoint of the database. |
| StartTime | Long | 1647375263000 | The start time of the backup, such as 1554560477000. |
| StorageMetho d | String | Standard | The storage class. Valid values: Standard: The storage class is Standard. IA: The storage class is Infrequent Access (IA). Archive: The storage class is Archive. UNKNOWN: The storage class is unknown. This value is returned because the task is not completed. |
| PageNum | Integer | 0 | The page number. |

| PageSize | Integer | 30 | The number of entries per page. |
|---|---|---|---|
| RequestId | String | 8D26CA51-35B8- 5155-8818- F40C2F27**** | The request ID. |
| Success | Boolean | true | Indicates whether the operation is successful. Valid values: true: successful false: failed |
| TotalElements | Integer | 138 | The total number of incremental backup tasks. |
| TotalPages | Integer | 5 | The total number of pages. |

**Examples**

Sample requests

```
http(s)://dbs-api.cn-hangzhou.aliyuncs.com/?Action=DescribeIncrementBackupList &BackupPlanId=dbsqdss5tmh**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RequestId>8D26CA51-35B8-5155-8818-F40C2F27****</RequestId> <PageSize>30</PageSize> <PageNum>0</PageNum> <HttpStatusCode>200</HttpStatusCode> <TotalElements>138</TotalElements> <TotalPages>5</TotalPages> <Items>
    <IncrementBackupFile>
        <SourceEndpointIpPort>172.XX.103.1:43XX</SourceEndpointIpPort>
        <EndTime>1647396866000</EndTime>
        <BackupSetJobId>1hv5g9wk4****</BackupSetJobId>
        <BackupSize>412032</BackupSize>
        <StartTime>1647375263000</StartTime>
        <BackupSetExpiredTime>1710468872000</BackupSetExpiredTime>
        <BackupSetId>mysql-bin.00****</BackupSetId>
        <BackupStatus>COMPLETED</BackupStatus>
    </IncrementBackupFile>
</Items> <Success>true</Success>
```

`JSON` format `{`

```json
    "RequestId": "8D26CA51-35B8-5155-8818-F40C2F27****",
    "PageSize": 30,
    "PageNum": 0,
    "HttpStatusCode": 200,
    "TotalElements": 138,
    "TotalPages": 5,
    "Items": {
        "IncrementBackupFile": [
```

`{`

```json
                "SourceEndpointIpPort": "172.XX.103.1:43XX",
                "EndTime": 1647396866000,
                "BackupSetJobId": "1hv5g9wk4****",
                "BackupSize": 412032,
                "StartTime": 1647375263000,
                "BackupSetExpiredTime": 1710468872000,
                "BackupSetId": "mysql-bin.00****",
                "BackupStatus": "COMPLETED"
```

`}` `]` `},`

```json
    "Success": true
```

`}`

### Restore task

#### CreateRestoreTask

Creates a restore task.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateRestoreTa sk | The operation that you want to perform. Set the value to CreateRestoreTask. |
| BackupPlanId | String | Yes | dbs1hvb0ww*** * | The ID of the backup schedule. You can call the DescribeBackupPlanList operation to query the ID of the backup schedule. |

| DestinationEndp ointInstanceTyp e | String | Yes | RDS | The location of the database. Valid values: RDS ECS Express: The database is connected to DBS by using Express Connect, VPN Gateway, or Smart Access Gateway. Agent: The database is connected to DBS over a DBS backup gateway. DDS: The database is an ApsaraDB for MongoDB (MongoDB) database. Other: The database is connected to DBS by using the IP address and port of the database. |
|---|---|---|---|---|
| RestoreTaskNam e | String | Yes | test | The name of the restore task. |
| DestinationEndp ointRegion | String | No | 100.X.X.10:3320 4 | The region where the database is deployed. Note If you set DestinationEndpointInstance Type to RDS, ECS, DDS, Express, or Agent, you must specify this parameter. |
| DestinationEndp ointInstanceID | String | No | rm- bp1p8c29***** | The ID of the database instance. Note If you set DestinationEndpointInstance Type to RDS, ECS, DDS, or Express, you must specify this parameter. |
| DestinationEndp ointIP | String | No | rm- bpXXXXX9jv8px ero.mysql.rds.ali yuncs.com | The endpoint of the database. Note If you set DestinationEndpointInstance Type to Express, Agent, or Other, you must specify this parameter. |

| DestinationEndp ointPort | Integer | No | 3306 | The port of the database. Note If you set DestinationEndpointInstance Type to Express, Agent, Other, or ECS, you must specify this parameter. |
|---|---|---|---|---|
| DestinationEndp ointDatabaseNa me | String | No | test | The name of the database. Note If the database runs the PostgreSQL engine or MongoDB engine, you must specify this parameter. |
| DestinationEndp ointUserName | String | No | test | The username of the database account. Note If the database is an SQL Server database that is connected to DBS over a DBS backup gateway or a Redis database, this parameter is optional. In other cases, you must specify this parameter. |
| DestinationEndp ointPassword | String | No | Test | The password of the database account. Note If the database is an SQL Server database that is connected to DBS over a DBS backup gateway or a Redis database, this parameter is optional. In other cases, you must specify this parameter. |

| BackupGatewayI d | Long | No | 43123424 | The ID of the backup gateway. Note If you set DestinationEndpointInstance Type to Agent, you must specify this parameter. |
|---|---|---|---|---|
| RestoreObjects | String | No | [ { "DBName":"Nam e of the database that you want to use for restoration", "NewDBName":" Name of the destination database that you want to restore", "SchemaName": "Name of the schema that you want to use for restoration", "NewSchemaNa me":"Name of the destination schema that you want to restore"}] | The objects that are involved in restoration. Note If you set DestinationEndpointInstance Type to Agent, this parameter is optional. In other cases, you must specify this parameter. |
| RestoreTime | Long | No | 1554560477000 | The point in time when you want the restore task to run. |
| BackupSetId | String | No | dbs1hvb0wXXX XX | The ID of the full backup set that is used to restore data. This parameter is mutually exclusive with RestoreTime. |

| DestinationEndp ointOracleSID | String | No | test | The system ID (SID) of the Oracle database. Note If the database is an Oracle database, you must specify this parameter. |
|---|---|---|---|---|
| RestoreDir | String | No | test | If you set DestinationEndpointInstanceTyp e to Agent and the backup object of the backup schedule is a MySQL database, you must specify this parameter. |
| RestoreHome | String | No | test | The program directory of the database. |
| Stages | String | No | XXX | This parameter is not required. |
| DuplicateConflic t | String | No | failure | The method that is used to process objects with the same name. Valid values: failure (default): The restore task fails if the system detects objects with the same name. renamenew: The restore task renames objects with the same name starting from the second occurrence. |
| CrossAliyunId | String | No | XXX | This parameter is not supported. |
| CrossRoleName | String | No | XXX | This parameter is not supported. |
| RegionId | String | No | cn-hangzhou | The region ID. |
| ClientToken | String | No | ETnLKlblzczshOT UbOCzxxxxxxx | The client token that is used to ensure the idempotence of the request. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|

| ErrCode | String | InvalidParameterV alid | The error code. |
|---|---|---|---|
| ErrMessage | String | Need one of the parameter: [RestoreTime, BackupSetId] -> [RestoreTime, BackupSetId] | The error message. |
| HttpStatusCod e | Integer | 200 | The HTTP status code. |
| RequestId | String | 60AF7C5D-EF4D- 4D48-8FD5- C0823FDF**** | The request ID. |
| RestoreTaskId | String | s102h***** | The ID of the restore task. |
| Success | Boolean | true | Indicates whether the operation is successful. Valid values: true: successful false: failed |

**Examples**

Sample requests

```
http(s)://dbs-api.cn-hangzhou.aliyuncs.com/?Action=CreateRestoreTask &BackupPlanId=dbs1hvb0ww**** &DestinationEndpointInstanceType=RDS &RestoreTaskName=test &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RestoreTaskId>s102h*****</RestoreTaskId> <RequestId>60AF7C5D-EF4D-4D48-8FD5-C0823FDF****</RequestId> <HttpStatusCode>200</HttpStatusCode> <Success>true</Success>
```

`JSON` format `{`

```json
 "RestoreTaskId": "s102h*****",
 "RequestId": "60AF7C5D-EF4D-4D48-8FD5-C0823FDF****",
 "HttpStatusCode": 200,
 "Success": true
```

`}`

#### StartRestoreTask

Starts a restore task.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | StartRestoreTas k | The operation that you want to perform. Set the value to StartRestoreTask. |
| RestoreTaskId | String | Yes | s102h7rf**** | The ID of the restore task. You can call the CreateRestoreTask operation to query the ID of the restore task. |
| RegionId | String | No | cn-hangzhou | The region ID. |
| ClientToken | String | No | ETnLKlblzczshOT UbOCzxxxxxxx | The client token that is used to ensure the idempotence of the request. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| ErrCode | String | Param.NotFound | The error code. |
| ErrMessage | String | The specified parameter %s value is not valid. | The error message. |
| HttpStatusCod e | Integer | 200 | The HTTP status code. |

| RequestId | String | 60AF7C5D-EF4D- 4D48-8FD5- C0823FDF**** | The request ID. |
|---|---|---|---|
| RestoreTaskId | String | s102h7rf**** | The ID of the restore task. |
| Success | Boolean | true | Indicates whether the operation is successful. Valid values: true: successful false: failed |

**Examples**

Sample requests

```
http(s)://dbs-api.cn-hangzhou.aliyuncs.com/?Action=StartRestoreTask &RestoreTaskId=s102h7rf**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RestoreTaskId>s102h7rf****</RestoreTaskId> <RequestId>60AF7C5D-EF4D-4D48-8FD5-C0823FDF****</RequestId> <HttpStatusCode>200</HttpStatusCode> <Success>true</Success>
```

`JSON` format `{`

```json
 "RestoreTaskId": "s102h7rf****",
 "RequestId": "60AF7C5D-EF4D-4D48-8FD5-C0823FDF****",
 "HttpStatusCode": 200,
 "Success": true
```

`}`

#### DescribeRestoreTaskList

Queries restore tasks.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|

| Action | String | Yes | DescribeRestore TaskList | The operation that you want to perform. Set the value to DescribeRestoreTaskList. |
|---|---|---|---|---|
| BackupPlanId | String | No | dbssl67c7mx*** * | The ID of the backup schedule. |
| RestoreTaskId | String | No | s102h7rf**** | The ID of the restore task. Separate multiple IDs with commas (,). |
| PageSize | Integer | No | 30 | The number of entries per page. Valid values: 30, 50, and 100. Note Default value: 30. |
| PageNum | Integer | No | 1 | The page number. The value must be a positive integer. Default value: 0. |
| RegionId | String | No | cn-hangzhou | The region ID. |
| ClientToken | String | No | ETnLKlblzczshOT UbOCzxxxxxxx | The client token that is used to ensure the idempotence of the request. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| ErrCode | String | Param.NotFound | The error code. |
| ErrMessage | String | The specified parameter %s value is not valid. | The error message. |
| HttpStatusCod e | Integer | 200 | The HTTP status code. |
| Items | Array of RestoreTaskD etail |   | The details of the backup schedules. |
| RestoreTaskD etail |   |   |   |

| BackupGatewa yId | Long | 0 | The ID of the backup gateway. |
|---|---|---|---|
| BackupPlanId | String | dbssl67c7mx**** | The ID of the backup schedule. |
| BackupSetId | String | 1jy2oe65x**** | The ID of the full backup set that is used in the restore task. |
| ContinuousRes toreProgress | Integer | 100 | The restore progress of the incremental log files. |
| CrossAliyunId | String | 2xxx7778xxxxxxxx xx | The user ID of the account that is used to perform backups across Alibaba Cloud accounts. |
| CrossRoleNam e | String | test123 | The name of the Resource Access Management (RAM) role that is used to perform backups across Alibaba Cloud accounts. |
| DestinationEn dpointDatabas eName | String | test | The name of the database. |
| DestinationEn dpointInstance ID | String | rm- uf6d8gt9vwvrc**** | The ID of the database instance. |
| DestinationEn dpointInstance Type | String | RDS | The location of the database. Valid values: RDS ECS Express: The database is connected to DBS by using Express Connect, VPN Gateway, or Smart Access Gateway. Agent: The database is connected to DBS over a DBS backup gateway. DDS: The database is an ApsaraDB for MongoDB (MongoDB) database. Other: The database is connected to DBS by using the IP address and port of the database. |
| DestinationEn dpointIpPort | String | 127.XX.0.1:33XX | The endpoint of the database. |

| DestinationEn dpointOracleSI D | String | test | The system ID (SID) of the Oracle database. |
|---|---|---|---|
| DestinationEn dpointRegion | String | cn-hangzhou | The region where the database is deployed. |
| DestinationEn dpointUserNa me | String | test | The username of the database account. |
| ErrMessage | String | NULL | The error message. |
| FullDataRestor eProgress | Integer | 100 | The restore progress of the full backup data. |
| FullStruAfterR estoreProgress | Integer | 100 | The progress of schema restore after full data restore. |
| FullStruforeRe storeProgress | Integer | 100 | The progress of schema restore before full data restore. |
| RestoreDir | String | 100.X.X.10:33204 | The path to which you want to restore data. |
| RestoreObject s | String | [{ \"DBName\":\"test\ " } ] | The objects that you want to restore. |
| RestoreStatus | String | running | The status of the restore task. Valid values: init: The restore task is not started or does not pass the precheck. Running: The restore task is running. stop: The restore task fails. pause: The restore task is paused. check pass: The restore task passes _ the precheck. |
| RestoreTaskCr eateTime | Long | 1554560477000 | The time when the restore task was created. |

| RestoreTaskFi nishTime | Long | 1554560477000 | The time when the restore task was completed. |
|---|---|---|---|
| RestoreTaskId | String | 1jefy7ewt**** | The ID of the restore task. |
| RestoreTaskN ame | String | cbs34s6**** | The name of the restore task. |
| RestoreTime | Long | 1636567334000 | The point in time when the restore task was executed. |
| PageNum | Integer | 0 | The page number. |
| PageSize | Integer | 30 | The number of entries per page. |
| RequestId | String | 1A999262-DB3F- 5368-AA6E- 61AFDA8E**** | The request ID. |
| Success | Boolean | true | Indicates whether the operation is successful. Valid values: true: successful false: failed |
| TotalElements | Integer | 2 | The total number of restore tasks. |
| TotalPages | Integer | 1 | The total number of pages. |

**Examples**

Sample requests

```
http(s)://dbs-api.cn-hangzhou.aliyuncs.com/?Action=DescribeRestoreTaskList &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RequestId>1A999262-DB3F-5368-AA6E-61AFDA8E****</RequestId> <PageSize>30</PageSize> <PageNum>0</PageNum> <HttpStatusCode>200</HttpStatusCode> <TotalElements>2</TotalElements> <TotalPages>1</TotalPages> <Items>
    <RestoreTaskDetail>
        <RestoreDir/>
        <FullStruAfterRestoreProgress>0</FullStruAfterRestoreProgress>
        <FullStruforeRestoreProgress>0</FullStruforeRestoreProgress>
        <BackupSetId>1jy2oe65x****</BackupSetId>
        <RestoreStatus>check_pass</RestoreStatus>
        <DestinationEndpointInstanceType>RDS</DestinationEndpointInstanceType>
        <RestoreTime>1636567334000</RestoreTime>
        <DestinationEndpointRegion>cn-hangzhou</DestinationEndpointRegion>
        <FullDataRestoreProgress>0</FullDataRestoreProgress>
        <RestoreTaskId>1jefy7ewt****</RestoreTaskId>
        <DestinationEndpointIpPort>127.XX.0.1:33XX</DestinationEndpointIpPort>
        <DestinationEndpointUserName/>
        <RestoreObjects>[{"DBName":"rds1_wyp","NewDBName":"rds1_wyp"}]</RestoreObjects>
        <RestoreTaskName>cbs34s6****</RestoreTaskName>
        <BackupPlanId>dbssl67c7mx****</BackupPlanId>
        <RestoreTaskCreateTime>1636623886000</RestoreTaskCreateTime>
        <BackupGatewayId>0</BackupGatewayId>
    </RestoreTaskDetail>
    <RestoreTaskDetail>
        <RestoreDir/>
        <FullStruAfterRestoreProgress>100</FullStruAfterRestoreProgress>
        <FullStruforeRestoreProgress>100</FullStruforeRestoreProgress>
        <BackupSetId>sl67c7mx****</BackupSetId>
        <RestoreStatus>finish</RestoreStatus>
        <DestinationEndpointInstanceType>RDS</DestinationEndpointInstanceType>
        <RestoreTime>1634720897000</RestoreTime>
        <DestinationEndpointRegion>cn-shanghai</DestinationEndpointRegion>
        <FullDataRestoreProgress>100</FullDataRestoreProgress>
        <RestoreTaskId>vbhy7r7o****</RestoreTaskId>
        <ContinuousRestoreProgress>100</ContinuousRestoreProgress>
        <DestinationEndpointIpPort>172.XX.0.1:46XX</DestinationEndpointIpPort>
        <DestinationEndpointUserName>rdsdt_dbsacct</DestinationEndpointUserName>
        <RestoreObjects>[{"DBName":"rds1_wyp","NewDBName":"rds1_wyp"}]</RestoreObjects>
        <RestoreTaskName>cbs4225****</RestoreTaskName>
        <BackupPlanId>dbssl67c7mx****</BackupPlanId>
        <RestoreTaskCreateTime>1634721021000</RestoreTaskCreateTime>
        <BackupGatewayId>0</BackupGatewayId>
        <DestinationEndpointInstanceID>rm-uf6d8gt9vwvrc****
</DestinationEndpointInstanceID>
        <RestoreTaskFinishTime>1634721478000</RestoreTaskFinishTime>
    </RestoreTaskDetail>
</Items> <Success>true</Success>
```

`JSON` format

| { "RequestId": "1A999262-DB3F-5368-AA6E-61AFDA8E****", "PageSize": 30, "PageNum": 0, "HttpStatusCode": 200, "TotalElements": 2, "TotalPages": 1, "Items": { "RestoreTaskDetail": [ { "RestoreDir": "", "FullStruAfterRestoreProgress": 0, "FullStruforeRestoreProgress": 0, "BackupSetId": "1jy2oe65x****", "RestoreStatus": "check pass", _ "DestinationEndpointInstanceType": "RDS", "RestoreTime": 1636567334000, "DestinationEndpointRegion": "cn-hangzhou", "FullDataRestoreProgress": 0, "RestoreTaskId": "1jefy7ewt****", "DestinationEndpointIpPort": "127.XX.0.1:33XX", "DestinationEndpointUserName": "", "RestoreObjects": " [{\"DBName\":\"rds1 wyp\",\"NewDBName\":\"rds1 wyp\"}]", _ _ "RestoreTaskName": "cbs34s6****", "BackupPlanId": "dbssl67c7mx****", "RestoreTaskCreateTime": 1636623886000, "BackupGatewayId": 0 }, { "RestoreDir": "", "FullStruAfterRestoreProgress": 100, "FullStruforeRestoreProgress": 100, "BackupSetId": "sl67c7mx****", "RestoreStatus": "finish", "DestinationEndpointInstanceType": "RDS", "RestoreTime": 1634720897000, "DestinationEndpointRegion": "cn-shanghai", "FullDataRestoreProgress": 100, "RestoreTaskId": "vbhy7r7o****", "ContinuousRestoreProgress": 100, "DestinationEndpointIpPort": "172.XX.0.1:46XX", "DestinationEndpointUserName": "rdsdt dbsacct", _ "RestoreObjects": " [{\"DBName\":\"rds1 wyp\",\"NewDBName\":\"rds1 wyp\"}]", _ _ "RestoreTaskName": "cbs4225****", "BackupPlanId": "dbssl67c7mx****", "RestoreTaskCreateTime": 1634721021000, "BackupGatewayId": 0, "DestinationEndpointInstanceID": "rm-uf6d8gt9vwvrc****", "RestoreTaskFinishTime": 1634721478000 } ] }, |   |
|---|---|
| 9 > Document Version: 20260828 |   |

```json
    "Success": true
```

`}`

### Backup gateway

#### DescribeBackupGatewayList

Queries backup gateways.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeBackup GatewayList | The operation that you want to perform. Set the value to DescribeBackupGatewayList. |
| Region | String | Yes | cn-hangzhou | The region where DBS is activated. Note If you deploy your business in Apsara Stack, set the value to the environment initialization region. |
| Identifier | String | No | 7213527653217 | The unique identifier of the backup gateway. Separate multiple identifiers with commas (,). |
| PageSize | Integer | No | 30 | The number of entries per page. Valid values: 30, 50, and 100. Note Default value: 30. |
| PageNum | Integer | No | 1 | The page number. The value must be 0 or a positive integer. Default value: 0. |
| RegionId | String | No | cn-hangzhou | The region ID. |

| ClientToken | String | No | ETnLKlblzczshOT UbOCzxxxxxxx | The client token that is used to ensure the idempotence of the request. |
|---|---|---|---|---|

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| ErrCode | String | Param.NotFound | The error code. |
| ErrMessage | String | The specified parameter %s value is not valid. | The error message. |
| HttpStatusCod e | Integer | 200 | The HTTP status code. |
| Items | Array of BackupGatewa y |   | The details of the backup gateways. |
| BackupGatewa y |   |   |   |
| BackupGatewa yCreateTime | Long | 1554560477000 | The time when the backup gateway was created. |
| BackupGatewa yId | String | 2321313*** | The ID of the backup gateway. |
| BackupGatewa yStatus | String | ONLINE | The status of the backup gateway. Valid values: ONLINE OFFLINE STOPPED UPGRADING |
| DisplayName | String | test | The display name of the backup gateway. |
| Identifier | String | sgdsaj**** | The unique identifier of the backup gateway. |

| LastHeartbeat Time | Long | 1554560477000 | The time when the last heartbeat was reported. |
|---|---|---|---|
| Region | String | cn-hangzhou | The region ID of the backup gateway. |
| SourceEndpoin tHostname | String | test | The name of the host on which the backup gateway is installed. |
| SourceEndpoin tInternetIP | String | XX.XX.XX.XX | The public IP address of the host on which the backup gateway is installed. |
| SourceEndpoin tIntranetIP | String | XX.XX.XX.XX | The private IP address of the host on which the backup gateway is installed. |
| PageNum | Integer | 1 | The page number. |
| PageSize | Integer | 30 | The number of entries per page. |
| RequestId | String | 46361705-8531- 492F-807E- A97E482D**** | The request ID. |
| Success | Boolean | true | Indicates whether the operation is successful. Valid values: true: successful false: failed |
| TotalElements | Integer | 0 | The total number of backup gateways. |
| TotalPages | Integer | 1 | The total number of pages. |

**Examples**

Sample requests

```
http(s)://dbs-api.cn-hangzhou.aliyuncs.com/?Action=DescribeBackupGatewayList &Region=cn-hangzhou &<Common request parameters>
```

Sample success responses `XML` format

```xml
<PageSize>30</PageSize> <RequestId>46361705-8531-492F-807E-A97E482D****</RequestId> <PageNum>0</PageNum> <HttpStatusCode>200</HttpStatusCode> <TotalElements>0</TotalElements> <Items> </Items> <TotalPages>0</TotalPages> <Success>true</Success>
```

`JSON` format `{`

```json
 "PageSize": 30,
 "RequestId": "46361705-8531-492F-807E-A97E482D****",
 "PageNum": 0,
 "HttpStatusCode": 200,
 "TotalElements": 0,
 "Items": {
  "BackupGateway": []
```

`},`

```json
 "TotalPages": 0,
 "Success": true
```

`}`

### Backup set download

#### DescribeBackupSetDownloadTaskList

Queries backup set download tasks.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeBackup SetDownloadTas kList | The operation that you want to perform. Set the value to DescribeBackupSetDownloadTas kList. |
| BackupPlanId | String | No | dbssl67c7mx*** * | The ID of the backup schedule. You can call the DescribeBackupPlanList operation to query the ID of the backup schedule. |
| BackupSetDownl oadTaskId | String | No | dbstooi01e***** | The ID of the backup set download task. |

| PageSize | Integer | No | 30 | The number of entries per page. Valid values: 30, 50, and 100. Note Default value: 30. |
|---|---|---|---|---|
| PageNum | Integer | No | 1 | The page number. The value must be a positive integer. Default value: 0. |
| RegionId | String | No | cn-hangzhou | The region ID. |
| ClientToken | String | No | ETnLKlblzczshOT UbOCzxxxxxxx | The client token that is used to ensure the idempotence of the request. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| ErrCode | String | Param.NotFound | The error code. |
| ErrMessage | String | The specified parameter %s value is not valid. | The error message. |
| HttpStatusCod e | Integer | 200 | The HTTP status code. |
| Items | Array of BackupSetDow nloadTaskDeta il |   | The details of the backup schedules. |
| BackupSetDow nloadTaskDeta il |   |   |   |
| BackupGatewa yId | Long | 123 | The backup gateway that is used to download the backup set. This parameter is available only if you set BackupSetDownloadWay to auto. |
| BackupPlanId | String | sl67c7mx**** | The ID of the backup schedule. |

| BackupSetCod e | String | 1h7zrxja0**** | The code of the backup set. Full: the code is the same as the ID of the backup set. Incremental: the code is the same as the name of the backup set. |
|---|---|---|---|
| BackupSetDat aFormat | String | CSV | The format in which the backup set is downloaded. Valid values: Native SQL CSV JSON |
| BackupSetDat aSize | Long | 151 | The size of the data in the backup set. |
| BackupSetDbT ype | String | MySQL | The type of the database engine. |
| BackupSetDow nloadCreateTi me | Long | 1641545488000 | The time when the backup set download task was created. |
| BackupSetDow nloadDir | String | dbs test _ | The server directory to which the backup set is downloaded. This parameter is available only if you set BackupSetDownloadWay to auto. |
| BackupSetDow nloadFinishTi me | Long | 1641545557000 | The time when the backup set download was completed. |
| BackupSetDow nloadInternetU rl | String | //dbs-137XXX-cn- hangzhou- 1hr5cpbtm****.oss -cn- hangzhou.XXX.com /example345 | The public download URL of the backup set. This parameter is available only if you set BackupSetDownloadWay to manual and the conversion is completed. |
| BackupSetDow nloadIntranetU rl | String | //dbs-137XXX-cn- hangzhou- 1hr5cpbtm****.oss -cn-hangzhou- internal.XXX.com/e xample123 | The internal download URL of the backup set. This parameter is available only if you set BackupSetDownloadWay to manual and the conversion is completed. |

| BackupSetDow nloadStatus | String | finish | The status of the backup set download task. Valid values: init: The backup set download task is initialized. warning: An alert is reported for the backup set download task. catched: An exception occurred in the backup set download task. running: The backup set download task is running. failed: The backup set download task failed. finish: The backup set download task is completed. |
|---|---|---|---|
| BackupSetDow nloadTargetTy pe | String | agent | The type of the destination server to which the backup set is downloaded. This parameter is available only if you set BackupSetDownloadWay to auto. Note A value of agent indicates a server on which a backup gateway is installed. |
| BackupSetDow nloadTaskId | String | sl9gpu86*** | The ID of the backup set download task. |
| BackupSetDow nloadTaskNam e | String | 1h7zrxja0****- ManualFull | The name of the backup set download task. |
| BackupSetDow nloadWay | String | manual | The method in which the backup set is downloaded. Valid values: manual: The backup set is manually downloaded. auto: The backup set is automatically downloaded. |
| BackupSetId | String | 1h7zrxja0**** | The ID of the source backup set. |
| BackupSetJobT ype | String | cbs backup sub fu _ _ _ ll | The type of the backup set download task. Valid values: cbs backup sub full: logical full _ _ _ backup set download cbs backup sub cont: logical _ _ _ incremental backup set download |

| ErrMessage | String | java.lang.IndexOut OfBoundsException . | The error message. |
|---|---|---|---|
| PageNum | Integer | 0 | The page number. |
| PageSize | Integer | 30 | The number of entries per page. |
| RequestId | String | FB9C5B62-15CA- 5B72-B0F5- F0BDD165**** | The request ID. |
| Success | Boolean | true | Indicates whether the operation is successful. Valid values: true: successful false: failed |
| TotalElements | Integer | 1 | The total number of backup set download tasks. |
| TotalPages | Integer | 1 | The total number of pages. |

**Examples**

Sample requests

```
http(s)://dbs-api.cn-hangzhou.aliyuncs.com/?Action=DescribeBackupSetDownloadTaskList &BackupPlanId = dbssl67c7mx**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RequestId>FB9C5B62-15CA-5B72-B0F5-F0BDD165****</RequestId> <PageSize>30</PageSize> <PageNum>0</PageNum> <HttpStatusCode>200</HttpStatusCode> <TotalElements>1</TotalElements> <TotalPages>1</TotalPages> <Items>
    <BackupSetDownloadTaskDetail>
        <BackupSetDbType>MySQL</BackupSetDbType>
        <BackupSetDownloadCreateTime>1641545488000</BackupSetDownloadCreateTime>
        <BackupSetDownloadTaskName>1h7zrxja0****-ManualFull</BackupSetDownloadTaskName>
        <BackupSetDownloadWay>manual</BackupSetDownloadWay>
        <BackupSetCode>1h7zrxja0****</BackupSetCode>
        <BackupSetId>1h7zrxja0****</BackupSetId>
        <BackupSetDownloadStatus>finish</BackupSetDownloadStatus>
        <BackupSetDownloadIntranetUrl>//dbs-137XXX-cn-hangzhou-1hr5cpbtm****.oss-cn-han
gzhou-internal.XXX.com/example123</BackupSetDownloadIntranetUrl>
        <BackupSetDownloadInternetUrl>//dbs-137XXX-cn-hangzhou-1hr5cpbtm****.oss-cn-han
gzhou.XXX.com/example345</BackupSetDownloadInternetUrl>
        <BackupSetDownloadTaskId>sl9gpu86***</BackupSetDownloadTaskId>
        <BackupSetDownloadFinishTime>1641545557000</BackupSetDownloadFinishTime>
        <BackupSetJobType>cbs_backup_sub_full</BackupSetJobType>
        <BackupSetDataFormat>CSV</BackupSetDataFormat>
        <BackupPlanId>sl67c7mx****</BackupPlanId>
        <BackupSetDataSize>151</BackupSetDataSize>
    </BackupSetDownloadTaskDetail>
</Items> <Success>true</Success>
```

`JSON` format `{`

```json
    "RequestId": "FB9C5B62-15CA-5B72-B0F5-F0BDD165****",
    "PageSize": 30,
    "PageNum": 0,
    "HttpStatusCode": 200,
    "TotalElements": 1,
    "TotalPages": 1,
    "Items": {
        "BackupSetDownloadTaskDetail": [
```

`{`

```json
                "BackupSetDbType": "MySQL",
                "BackupSetDownloadCreateTime": 1641545488000,
                "BackupSetDownloadTaskName": "1h7zrxja0****-ManualFull",
                "BackupSetDownloadWay": "manual",
                "BackupSetCode": "1h7zrxja0****",
                "BackupSetId": "1h7zrxja0****",
                "BackupSetDownloadStatus": "finish",
                "BackupSetDownloadIntranetUrl": "//dbs-137XXX-cn-hangzhou-1hr5cpbtm****.
oss-cn-hangzhou-internal.XXX.com/example123",
                "BackupSetDownloadInternetUrl": "//dbs-137XXX-cn-hangzhou-1hr5cpbtm****.
oss-cn-hangzhou.XXX.com/example345",
                "BackupSetDownloadTaskId": "sl9gpu86***",
                "BackupSetDownloadFinishTime": 1641545557000,
                "BackupSetJobType": "cbs_backup_sub_full",
                "BackupSetDataFormat": "CSV",
                "BackupPlanId": "sl67c7mx****",
                "BackupSetDataSize": 151
```

`}` `]` `},`

```json
    "Success": true
```

`}`

#### Configures download rules for backup

**sets.**

You can call the ModifyBackupSetDownloadRules operation to enable, modify, or disable the automatic download feature.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyBackupSe tDownloadRules | The operation that you want to perform. Set the value to ModifyBackupSetDownloadRules. |

| BackupPlanId | String | Yes | dbstooi01**** | The ID of the backup schedule. You can call the DescribeBackupPlanList operation to query the ID of the backup schedule. |
|---|---|---|---|---|
| OpenAutoDownl oad | Boolean | No | false | Specifies whether to enable the automatic download feature. Default value: false. |
| BackupGatewayI d | Long | No | 123123123 | The ID of the backup gateway that is used to download the backup set. |
| FullDataFormat | String | No | CSV | The format in which the full backup set is downloaded. Valid values: Native SQL CSV JSON Note Default value: CSV. |
| IncrementDataF ormat | String | No | Native | The format in which the incremental backup set is downloaded. Valid values: Native SQL CSV JSON Note Default value: Native. |
| BackupSetDownl oadDir | String | No | test | The server directory to which the backup set is downloaded. |
| BackupSetDownl oadTargetType | String | No | agent | The type of the destination server to which the backup set is downloaded. Note Default value: agent. The default value specifies that a backup gateway is installed. |

| BackupSetDownl oadTargetTypeL ocation | String | No | local | The type of the destination directory to which the backup set is downloaded. If the automatic download feature is enabled, you must specify this parameter. Valid values: local nas ftp minio Note Default value: local. |
|---|---|---|---|---|
| RegionId | String | No | cn-hangzhou | The region ID. |
| ClientToken | String | No | ETnLKlblzczshOT UbOCzxxxxxxx | The client token that is used to ensure the idempotence of the request. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| BackupPlanId | String | dbstooi01e**** | The ID of the backup schedule. |
| ErrCode | String | Param.NotFound | The error code. |
| ErrMessage | String | The specified parameter %s value is not valid. | The error message. |
| HttpStatusCod e | Integer | 200 | The HTTP status code. |
| RequestId | String | D6E068C3-25BC- 455A-85FE- 45F0B22E**** | The request ID. |

| Success | Boolean | true | Indicates whether the operation is successful. Valid values: true: successful false: failed |
|---|---|---|---|

Sample requests

```
http(s)://dbs-api.cn-hangzhou.aliyuncs.com/?Action=ModifyBackupSetDownloadRules &BackupPlanId=dbstooi01**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RequestId>D6E068C3-25BC-455A-85FE-45F0B22E****</RequestId> <HttpStatusCode>200</HttpStatusCode> <BackupPlanId>dbstooi01e****</BackupPlanId> <Success>true</Success>
```

`JSON` format `{`

```json
  "RequestId": "D6E068C3-25BC-455A-85FE-45F0B22E****",
  "HttpStatusCode": 200,
  "BackupPlanId": "dbstooi01e****",
  "Success": true
```

`}`

#### CreateFullBackupSetDownload

Creates and starts a full backup set download task.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateFullBacku pSetDownload | The operation that you want to perform. Set the value to CreateFullBackupSetDownload. |

| BackupSetId | String | Yes | dbs1hv***** | The ID of the full backup set. You can call the DescribeBackupSetDownloadTas kList operation to query the ID of the full backup set. |
|---|---|---|---|---|
| BackupSetDataF ormat | String | No | SQL | The format in which the full backup set is downloaded. Valid values: Native SQL CSV JSON Note Default value: CSV. |
| RegionId | String | No | cn-hangzhou | The region ID. |
| ClientToken | String | No | ETnLKlblzczshOT UbOCzxxxxxxx | The client token that is used to ensure the idempotence of the request. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| BackupSetDow nloadTaskId | String | dbstooi01e***** | The ID of the backup set download task. |
| ErrCode | String | Param.NotFound | The error code. |
| ErrMessage | String | The specified parameter %s value is not valid. | The error message. |
| HttpStatusCod e | Integer | 200 | The HTTP status code. |
| RequestId | String | D6E068C3-25BC- 455A-85FE- 45F0B22E**** | The request ID. |

| Success | Boolean | true | Indicates whether the operation is successful. Valid values: true: successful false: failed |
|---|---|---|---|

**Examples**

Sample requests

```
http(s)://dbs-api.cn-hangzhou.aliyuncs.com/?Action=CreateFullBackupSetDownload &BackupSetId=dbs1hv***** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<BackupSetDownloadTaskId>dbstooi01e*****</BackupSetDownloadTaskId> <RequestId>D6E068C3-25BC-455A-85FE-45F0B22E****</RequestId> <HttpStatusCode>200</HttpStatusCode> <ErrMessage>The specified parameter %s value is not valid.</ErrMessage> <Success>true</Success> <ErrCode>Param.NotFound</ErrCode>
```

`JSON` format `{`

```json
    "BackupSetDownloadTaskId": "dbstooi01e*****",
    "RequestId": "D6E068C3-25BC-455A-85FE-45F0B22E****",
    "HttpStatusCode": 200,
    "ErrMessage": "The specified parameter %s value is not valid.",
    "Success": true,
    "ErrCode": "Param.NotFound"
```

`}`

#### CreateIncrementBackupSetDownload

Creates and starts an incremental backup set download task.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateIncrement BackupSetDownl oad | The operation that you want to perform. Set the value to CreateIncrementBackupSetDownl oad. |

| BackupSetId | String | Yes | dbstooi01e***** | The ID of the incremental backup set. You can call the DescribeBackupSetDownloadTas kList operation to query the ID of the incremental backup set. |
|---|---|---|---|---|
| BackupSetName | String | Yes | test | The name of the incremental backup set. |
| BackupSetDataF ormat | String | No | Native | The format in which the incremental backup set is downloaded. Valid values: Native SQL CSV JSON Note Default value: Native. |
| RegionId | String | No | cn-hangzhou | The region ID. |
| ClientToken | String | No | ETnLKlblzczshOT UbOCzxxxxxxx | The client token that is used to ensure the idempotence of the request. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| BackupSetDow nloadTaskId | String | dbstooi01e***** | The ID of the backup set download task. |
| ErrCode | String | Param.NotFound | The error code. |
| ErrMessage | String | The specified parameter %s value is not valid. | The error message. |
| HttpStatusCod e | Integer | 200 | The HTTP status code. |
| RequestId | String | D6E068C3-25BC- 455A-85FE- 45F0B22E**** | The request ID. |

| Success | Boolean | true | Indicates whether the operation is successful. Valid values: true: successful false: failed |
|---|---|---|---|

**Examples**

Sample requests

```
http(s)://dbs-api.cn-hangzhou.aliyuncs.com/?Action=CreateIncrementBackupSetDownload &BackupSetId=dbstooi01e***** &BackupSetName=test &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RequestId>D6E068C3-25BC-455A-85FE-45F0B22E****</RequestId> <HttpStatusCode>200</HttpStatusCode> <BackupSetDownloadTaskId>dbstooi01e*****</BackupSetDownloadTaskId> <Success>true</Success>
```

`JSON` format `{`

```json
  "RequestId": "D6E068C3-25BC-455A-85FE-45F0B22E****",
  "HttpStatusCode": 200,
  "BackupSetDownloadTaskId": "dbstooi01e*****",
  "Success": true
```

`}`

### Others

#### Queries the standard error information

**of a DBS task.**

You can call the DescribeJobErrorCode operation to query the standard error information of a Database Backup (DBS) task.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|

| Action | String | Yes | DescribeJobError Code | The operation that you want to perform. Set the value to DescribeJobErrorCode. |
|---|---|---|---|---|
| TaskId | String | Yes | dbstooi0**** | The ID of the full backup or restore task. |
| Language | String | No | en | The language of the error message. Valid values: en and cn. Note Default value: en. |
| RegionId | String | No | cn-hangzhou | The region ID. |
| ClientToken | String | No | ETnLKlblzczshOT UbOCzxxxxxxx | The client token that is used to ensure the idempotence of the request. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| ErrCode | String | Param.NotFound | The error code. |
| ErrMessage | String | The specified parameter %s value is not valid. | The error message. |
| HttpStatusCod e | Integer | 200 | The HTTP status code. |
| Item | Struct |   | The item for which the error is reported. |
| ErrorCode | String | failed | The error code. |
| ErrorMessage | String | Describe preCheck progress failed. | The standard error message. |
| JobId | String | tooi0**** | The ID of the full backup or restore task. |
| JobState | String | init | The task status. |

| JobType | String | testId | The ID of the internal DBS task type. |
|---|---|---|---|
| Language | String | en | The language of the error message. |
| RequestId | String | 1FC2F86D-AFF4- 4ED9-BB25- ADDE196C**** | The request ID. |
| Success | Boolean | true | Indicates whether the operation is successful. Valid values: true: successful false: failed |

**Examples**

Sample requests

```
http(s)://dbs-api.cn-hangzhou.aliyuncs.com/?Action=DescribeJobErrorCode &TaskId=dbstooi0**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<Item>
    <Language>en</Language>
    <JobId>tooi0****</JobId>
</Item> <RequestId>1FC2F86D-AFF4-4ED9-BB25-ADDE196C****</RequestId> <HttpStatusCode>200</HttpStatusCode> <Success>true</Success>
```

`JSON` format `{`

```json
 "Item": {
  "Language": "en",
  "JobId": "tooi0****"
```

`},`

```json
 "RequestId": "1FC2F86D-AFF4-4ED9-BB25-ADDE196C****",
 "HttpStatusCode": 200,
 "Success": true
```

`}`

#### DescribeNodeCidrList

Queries the CIDR blocks of nodes on which DBS is running.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeNodeCi drList | The operation that you want to perform. Set the value to DescribeNodeCidrList. |
| Region | String | Yes | cn-hangzhou | The region where DBS is activated. Note If you deploy your business in Apsara Stack, set the value to the environment initialization region. |
| RegionId | String | No | cn-hangzhou | The region ID. |
| ClientToken | String | No | ETnLKlblzczshOT UbOCzxxxxxxx | The client token that is used to ensure the idempotence of the request. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| ErrCode | String | Param.NotFound | The error code. |
| ErrMessage | String | The specified parameter %s value is not valid. | The error message. |
| HttpStatusCod e | Integer | 200 | The HTTP status code. |
| InternetIPs | List | "10.X.X.0/24" | The public CIDR blocks. |
| IntranetIPs | List | "10.X.X.0/24" | The internal CIDR blocks. |
| RequestId | String | 5B352E69-E7B1- 4EA7-BB8E- 29FFE969**** | The request ID. |

| Success | Boolean | true | Indicates whether the operation is successful. Valid values: true: successful false: failed |
|---|---|---|---|

**Examples**

Sample requests

```
http(s)://dbs-api.cn-hangzhou.aliyuncs.com/?Action=DescribeNodeCidrList &Region=cn-hangzhou &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RequestId>5B352E69-E7B1-4EA7-BB8E-29FFE969****</RequestId> <InternetIPs>
    <InternetIP>118.X.X.0/24</InternetIP>
    <InternetIP>47.X.X.0/24</InternetIP>
</InternetIPs> <HttpStatusCode>200</HttpStatusCode> <IntranetIPs>
    <IntranetIP>10.X.X.0/24</IntranetIP>
    <IntranetIP>10.X.X.0/24</IntranetIP>
    <IntranetIP>10.X.X.0/24</IntranetIP>
</IntranetIPs> <Success>true</Success>
```

`JSON` format `{`

```json
 "RequestId": "5B352E69-E7B1-4EA7-BB8E-29FFE969****",
 "InternetIPs": {
  "InternetIP": [
   "118.X.X.0/24",
   "47.X.X.0/24"
```

`]` `},`

```json
 "HttpStatusCode": 200,
 "IntranetIPs": {
  "IntranetIP": [
   "10.X.X.0/24",
   "10.X.X.0/24",
   "10.X.X.0/24"
```

`]` `},`

```json
 "Success": true
```

`}`

#### DescribePreCheckProgressList

Queries the precheck progress of a backup schedule or a restore task.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribePreChe ckProgressList | The operation that you want to perform. Set the value to DescribePreCheckProgressList. |
| BackupPlanId | String | No | dbstooi01**** | The ID of the backup schedule. |
| RestoreTaskId | String | No | dbasdsa**** | The ID of the restore task. |
| RegionId | String | No | cn-hangzhou | The region ID. |
| ClientToken | String | No | ETnLKlblzczshOT UbOCzxxxxxxx | The client token that is used to ensure the idempotence of the request. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| ErrCode | String | Param.NotFound | The error code. |
| Items | Array of PreCheckProgr essDetail |   | The details of the precheck progress. |
| PreCheckProgr essDetail |   |   |   |
| BootTime | Long | 1583734969000 | The start time of the precheck, such as 1554560477000. |
| ErrMsg | String | java.lang.RuntimeE xception: Could not find any schema ...... | The error message. |

| FinishTime | Long | 1583734969000 | The end time of the precheck, such as 1554560477000. |
|---|---|---|---|
| Item | String | CHECK OTHER _ | The name of the precheck item. |
| JobId | String | uvk8f6fx**** | The ID of the job for the precheck item. |
| Names | String | CHECK OTHER _ | The name of the group to which the precheck item belongs. |
| OrderNum | String | 10 | The sequence number of the precheck item. |
| State | String | warning | The progress of the precheck item. Valid values: init: The item is initialized. warning: An alert is reported. catched: An exception occurred. running: The precheck is in progress. failed: The precheck failed. finish: The precheck is completed. |
| HttpStatusCod e | Integer | 200 | The HTTP status code. |
| ErrMessage | String | The specified parameter %s value is not valid. | The error message. |
| Progress | Integer | 100 | The progress of the precheck task. Valid values: 0 to 100. |
| RequestId | String | C4A45FE1-A903- 470D-B113- F12A4DF9**** | The request ID. |
| Status | String | failed | The status of the precheck. Valid values: running: The precheck is in progress. failed: The precheck failed. finish: The precheck is completed. |

| Success | Boolean | true | Indicates whether the operation is successful. Valid values: true: successful false: failed |
|---|---|---|---|

**Examples**

Sample requests

```
http(s)://dbs-api.cn-hangzhou.aliyuncs.com/?Action=DescribePreCheckProgressList &<Common request parameters>
```

Sample success responses `XML` format

```xml
<Status>failed</Status> <Progress>20</Progress> <RequestId>C4A45FE1-A903-470D-B113-F12A4DF9****</RequestId> <HttpStatusCode>200</HttpStatusCode> <Items>
    <PreCheckProgressDetail>
        <Names>CHECK_MYSQL_PASSOWRD_FORMAT_DETAIL</Names>
        <Item>CHECK_MYSQL_PASSOWRD_FORMAT</Item>
        <OrderNum>90</OrderNum>
        <State>init</State>
        <BootTime>1583734969000</BootTime>
        <JobId>uvk8f6fx****</JobId>
    </PreCheckProgressDetail>
</Items> <ErrMessage>java.lang.RuntimeException: Could not find any schema ......</ErrMessage> <Success>true</Success>
```

`JSON` format `{`

```json
 "Status": "failed",
 "Progress": 20,
 "RequestId": "C4A45FE1-A903-470D-B113-F12A4DF9****",
 "HttpStatusCode": 200,
 "Items": {
  "PreCheckProgressDetail": [
```

`{`

```json
    "Names": "CHECK_MYSQL_PASSOWRD_FORMAT_DETAIL",
    "Item": "CHECK_MYSQL_PASSOWRD_FORMAT",
    "OrderNum": "90",
    "State": "init",
    "BootTime": 1583734969000,
    "JobId": "uvk8f6fx****"
```

`}` `]` `},`

```json
 "ErrMessage": "java.lang.RuntimeException: Could not find any schema ......",
 "Success": true
```

`}`

#### PhysicalDeleteResource

Physically deletes resources from Database Backup.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

**Request parameters**

| Parame ter name | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Query | No | cn-hangzhou | The ID of the region. |
| Interrupt | Boole an | Query | No | false | Specifies whether to interrupt the task. |
| Invoker | Strin g | Query | Yes | admin | The invoker of the operation. |
| Pk | Strin g | Query | Yes | 259258662544****** | Unknown. |
| Bid | Strin g | Query | Yes | 26842 | Bid |
| Hid | Long | Query | Yes | 1001 | The unique ID. |

| Developer Gui | de ·API r | eference |   |   | Database Backu |
|---|---|---|---|---|---|

| Parame ter name | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Country | Strin g | Query | Yes | CN | The country. The default value is CN. |
| TaskIdenti fier | Strin g | Query | Yes | 001 | The task identifier. |
| TaskExtra Data | Strin g | Query | Yes | {"retry count": 3, _ "timeout": 60, "priority": "high"} | The extra data for the task. |
| GmtWake up | Strin g | Query | Yes | 08:00 | The wakeup time. |
| Success | Boole an | Query | No | TRUE | Indicates whether the request was successful. |
| Message | Strin g | Query | No | ***** | This parameter is left empty if the request is successful. An error message is returned if the request fails. |

**Returned Data**

| Parameter Name | Type | Example | Description |
|---|---|---|---|
| Interrupt | Boolean | false | Indicates whether the task was interrupted. |
| Invoker | String | admin | The invoker of the operation. |
| Pk | String | 172824053450759 0 | The primary key of the disaster recovery cloud instance. |
| Bid | String | 26842 | The request ID. |
| Hid | Long | 123456 | The unique ID. |
| Country | String | China | The country or region. |
| TaskIdentifier | String | ExampleValue | The task identifier. |

| Database Backup |   |   | Developer Guide ·API referenc |
|---|---|---|---|

| Parameter Name | Type | Example | Description |
|---|---|---|---|
| TaskExtraData | String | {"retry count": 3, _ "timeout": 60, "priority": "high"} | The extra data for the task. |
| GmtWakeup | String | 08:00 | The wakeup time. |
| Success | Boolean | true | The returned status. Success: true. false: The request failed. |
| Message | String | success | The additional information. |

**Examples**

Request example

```
http(s)://[Endpoint]/?Action=PhysicalDeleteResource &Invoker=admin &Pk=259258662544****** &Bid=26842 &Hid=1001 &Country=CN &TaskIdentifier=001 &TaskExtraData={"retry_count": 3, "timeout": 60, "priority": "high"} &GmtWakeup= &<Common request parameters>
```

Response example `JSON` format `{`

```json
 "GmtWakeup":"",
 "Hid":"",
 "Invoker":"admin",
 "TaskIdentifier":"ExampleValue",
 "Message":"success",
 "TaskExtraData":"{\"retry_count\": 3, \"timeout\": 60, \"priority\": \"high\"}",
 "Country":"China",
 "Pk":"1728240534507590",
 "Bid":"26842",
 "Interrupt":false,
 "Success":true
```

`}`

#### LogicalDeleteResource

Logically deletes a specified resource in Database Backup.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

**Request parameters**

| Parame ter Name | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Query | No | cn-hangzhou | The region ID. |
| Interrupt | Boole an | Query | No | false | Specifies whether to interrupt the task. |
| Invoker | Strin g | Query | Yes | admin | The invoker of the API operation. |
| Pk | Strin g | Query | Yes | 259258662544****** | Unknown. |
| Bid | Strin g | Query | Yes | 26842 | Bid |
| Hid | Long | Query | Yes | 9999 | The unique ID. |
| Country | Strin g | Query | Yes | CN | The country. The default value is CN. |
| TaskIdenti fier | Strin g | Query | Yes | EX12345 | The task identifier. |
| TaskExtra Data | Strin g | Query | Yes | {"retryCount": 3, "timeout": 60} | The extra data for the task. |
| GmtWake up | Strin g | Query | Yes | 08:00 | The wakeup time. |
| Success | Boole an | Query | No | TRUE | Indicates whether the request was successful. |
| Message | Strin g | Query | No | ***** | If the request is successful, this parameter is empty. If the request fails, an error message is returned. |

**Response data**

| Parameter Name | Type | Example | Description |
|---|---|---|---|
| Interrupt | Boolean | false | Indicates whether the task was interrupted. |
| Invoker | String | admin | The invoker of the API operation. |
| Pk | String | 172824053450759 0 | The primary key of the disaster recovery cloud instance. |
| Bid | String | 26842 | Request ID |
| Hid | Long | 123456 | The unique ID. |
| Country | String | China | The country or region. |
| TaskIdentifier | String | example value _ | The task identifier. |
| TaskExtraData | String | {"retryCount": 3, "timeout": 60} | The extra data for the task. |
| GmtWakeup | String | 07:30 | The wakeup time. |
| Success | Boolean | true | The status that is returned. Success: true. failed: false |
| Message | String | success | The additional information. |

**Examples**

Sample request

```
http(s)://[Endpoint]/?Action=LogicalDeleteResource &Invoker=admin &Pk=259258662544****** &Bid=26842 &Hid=9999 &Country=CN &TaskIdentifier=EX12345 &TaskExtraData={"retryCount": 3, "timeout": 60} &GmtWakeup= &<Common request parameters>
```

Sample response `JSON` format `{`

```json
 "GmtWakeup":"07:30",
 "Hid":"",
 "Invoker":"admin",
 "TaskIdentifier":"example_value",
 "Message":"success",
 "TaskExtraData":"{\"retryCount\": 3, \"timeout\": 60}",
 "Country":"China",
 "Pk":"1728240534507590",
 "Bid":"26842",
 "Interrupt":false,
 "Success":true
```

`}`

#### DescribeOssStsToken

Returns a Security Token Service (STS) token for secure access to Object Storage Service (OSS).

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

**Request parameters**

| Parame ter Name | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| BackupPla nId | Strin g | Query | No | dbstooi01xxxx | The ID of the backup schedule. To obtain this parameter, call the DescribeBackupPlanList operation. |

| Parame ter Name | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Identifier | Strin g | Query | No | temperature | The identifier of the event to query. For weak verification, you can view the device's event Identifier under the product's feature definition in the console, or call QueryThingModel and view the identifier in the returned Thing Specification Language model. identifier For no verification: Use the same custom identifier that the device uses to report the event. |
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |
| Resource OwnerId | Long | Query | No | 345678912345 | This is a system parameter related to authentication. Do not specify this parameter. |

**Returned Data**

| Parameter Name | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The ID of the request. |
| Success | Boolean | true | The return status. The operation was successful. Failed: false. |
| Message | String | success | Additional information. |
| Code | String | 200 | The status of the API call or a POP error code. |

| Developer Guide · | API reference |   | Database Backu |
|---|---|---|---|

| Parameter Name | Type | Example | Description |
|---|---|---|---|
| HttpStatusCod e | Integer | 200 | The HTTP status code. |
| AccessKeyId | String | 0wNEpMMlzy7s**** | The AccessKey ID. |
| AccessKeySecr et | String | lml2H****** | The AccessKey secret. |
| SecurityToken | String | ******** | The STS security token. |
| OssPrefix | String | test-prefix/hello- prefix | The prefix for the OSS object. This prefix, along with the bucket name and path format, forms the full path of the delivered file. For example, test-prefix or test/prefix . The prefix can contain forward slashes (/) as separators. Each part of the prefix must meet the following requirements: 1. Contains only uppercase letters, lowercase letters, digits, underscores ( ), hyphens (-), and periods (.). _ 2. Is no more than 253 characters long. 3. Starts with a letter or a digit. |
| EnvMode | String | Production | The environment type. A value of `Production` indicates the production environment, which provides live services. |
| ClientType | String | 1 | The client type. |

**Examples**

Sample request

```
http(s)://[Endpoint]/?Action=DescribeOssStsToken &Common request parameters
```

Sample response `JSON` format `{`

```json
 "SecurityToken":"********",
 "ClientType":"1",
 "RequestId":"F0A8A039-930D-5EC1-97C8-************",
 "Message":"success",
 "AccessKeyId":"0wNEpMMlzy7s****",
 "EnvMode":"Production",
 "AccessKeySecret":"lml2H******",
 "HttpStatusCode":200,
 "OssPrefix":"test-prefix/hello-prefix",
 "Code":"200",
 "Success":true
```

`}`

#### DescribeBackupInstances

Queries a list of database backup instances.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

**Request parameters**

| Parame ter Name | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Query | No | cn-hangzhou | The region ID. |
| BackupPla nId | Strin g | Query | No | dbstooi01xxxx | The ID of the backup schedule. Call the DescribeBackupPlanList operation to obtain the value of this parameter. |
| Resource OwnerId | Long | Query | No | 345678912345 | A system parameter for authentication. You do not need to specify this parameter. |
| Resource RegionId | Strin g | Query | No | cn-hangzhou | The region where the resource resides. |
| PageNum ber | Integ er | Query | No | 1 | The page number. |

| Developer Gui | de ·API r | eference |   |   | Database Backu |
|---|---|---|---|---|---|

| Parame ter Name | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| PageSize | Integ er | Query | No | 10 | The number of entries to return on each page. Default value: 10. |

**Returned data**

| Parameter Name | Type | Example | Description |
|---|---|---|---|
| BackupInstanc es | Array | ["backup1", "backup2", "backup3"] | Specifies a list of names or identifiers for a group of backup instances, used to record or manage multiple backup replicas. |
| -Id | String | 1 | The ID of the role. |
| -Name | String | test | Metric name. |
| -JobId | String | 72dcd26b-f12d- 4c27-b3af- 18f6aed5**** | The ID of the asynchronous task. |
| -RegionId | String | cn-hangzhou | The region ID. |
| -PayType | String | Postpaid | The billing method of the instance. Valid values: Postpaid: pay-as-you-go. Prepaid: subscription. |
| -CreateTime | String | 2022 | The time when the instance was created. |
| -ExpireTime | String | 2018-08- 24T09:55:41Z | The expiration time. |
| -DbType | String | MySQL | The database type. |
| -ConnectionStr | String | jdbc:mysql://localh ost:3306/mydb? user=root&passwo rd=123456 | A connection string to the local MySQL database `mydb` with the username `root` and password `123456`. |
| -OssBucket | String | liveBucket**** | The name of the OSS bucket. |
| -Status | String | 1 | The status. |

| Database Backup |   |   | Developer Guide ·API referenc |
|---|---|---|---|

| Parameter Name | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Success | Boolean | true | The status that is returned. Success: true. Failed: false. |
| Message | String | success | Additional information. |
| TotalBackupIn stanceCount | Integer | 5 | Indicates that the current system contains a total of five backup instances. |
| PageNumber | Integer | 1 | The page number. |
| PageSize | Integer | 10 | The number of entries returned per page. |
| TotalPages | Integer | 1 | The total number of pages. |

**Examples**

Sample request

```
http(s)://[Endpoint]/?Action=DescribeBackupInstances &<Common request parameters>
```

Sample response `JSON` format `{`

```json
 "RequestId":"F0A8A039-930D-5EC1-97C8-************",
 "Message":"success",
 "TotalBackupInstanceCount":5,
 "PageSize":10,
 "PageNumber":1,
 "BackupInstances":[
```

`{`

```json
   "Status":"1",
   "CreateTime":"2022",
   "OssBucket":"liveBucket****",
   "Id":"1",
   "RegionId":"cn-hangzhou",
   "PayType":"Postpaid",
   "ConnectionStr":"jdbc:mysql://localhost:3306/mydb?user=root&password=123456",
   "ExpireTime":"2018-08-24T09:55:41Z",
   "JobId":"72dcd26b-f12d-4c27-b3af-18f6aed5****",
   "DbType":"MySQL",
   "Name":"test"
```

`}` `],`

```json
 "TotalPages":1,
 "Success":true
```

`}`

#### ConfigureDuplicaitonBackupPlan

Configures a database replication backup schedule.

**Request headers**

This operation uses common request headers. For more information, see Common request parameters.

**Request parameters**

| Parame ter Name | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Bid | Strin g | Query | Yes | 26842 | The business ID. |
| Database Type | Strin g | Query | Yes | MySQL | The type of the database. Valid values: MySQL Oracle PostgreSQL SQLServer |

| Parame ter Name | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| StorageRe gion | Strin g | Query | Yes | cn-hangzhou | The storage region. This parameter is required if you set PayType to postpay . |
| Database Region | Strin g | Query | Yes | cn-hangzhou | The region of the database. This parameter is required if you set PayType to postpay . |
| BackupPla nName | Strin g | Query | Yes | dbstooi0******* | The name of the backup schedule. |
| SourceEn dpointInst anceID | Strin g | Query | Yes | rm-bp1imrtn6fq7h**** | The ID of the database instance. You can call the DescribeBackupPlanList operation to obtain the value of this parameter. This parameter is required if SourceEndpoint .InstanceType is set to RDS , ECS , DDS , or Express . |
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |
| Resource OwnerId | Long | Query | Yes | 345678912345 | A system parameter for authentication. Do not specify this parameter. |

**Returned data**

| Parameter Name | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Success | Boolean | true | The returned status. The operation was successful. The operation did not fail. |
| Message | String | success | Additional information. |
| BackupPlanId | String | dbs1h****usfa | The ID of the backup schedule. |

**Examples**

Request example

```
http(s)://[Endpoint]/?Action=ConfigureDuplicationBackupPlan &Bid=26842 &DatabaseType=MySQL &StorageRegion=cn-hangzhou &DatabaseRegion=cn-hangzhou &BackupPlanName=dbstooi0******* &SourceEndpointInstanceID=rm-bp1imrtn6fq7h**** &ResourceOwnerId=345678912345 &<Common request parameters>
```

Response example `JSON` format `{`

```json
 "RequestId":"F0A8A039-930D-5EC1-97C8-************",
 "Message":"success",
 "BackupPlanId":"dbs1h****usfa",
 "Success":true
```

`}`

#### CheckResource

Checks the availability and status of resources in Database Backup.

**Request header**

This operation uses common request headers. For more information, see Common request parameters.

**Request parameters**

| Parame ter name | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Query | No | cn-hangzhou | The region ID. |
| Interrupt | Boole an | Query | No | false | Specifies whether to interrupt the task. |
| Invoker | Strin g | Query | Yes | admin | The invoker of the operation. |
| Pk | Strin g | Query | Yes | 259258662544****** | Unknown. |
| Bid | Strin g | Query | Yes | 26842 | The bid. |
| Hid | Long | Query | Yes | 1001 | The unique identification number. |
| Country | Strin g | Query | Yes | CN | The country. Default value: CN. |
| TaskIdenti fier | Strin g | Query | Yes | 001 | The task identifier. |
| TaskExtra Data | Strin g | Query | Yes | {"retry count": 3, _ "timeout": 60} | The extra data for the task. |
| GmtWake up | Strin g | Query | Yes | 08:00 | The wakeup time. |
| Success | Boole an | Query | No | TRUE | Indicates whether the request was successful. |
| Message | Strin g | Query | No | ***** | If the request is successful, this parameter is empty. If the request fails, an error message is returned. |
| Level | Long | Query | No | 1 | The level. |

| Parame ter name | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Url | Strin g | Query | No | https://img.alicdn.com/tf s/TB1Wo7eXAvoK1RjSZF DXXXY3pXa-2512- 3509.jpg | Specify either this parameter or the body parameter. Do not specify both or leave both empty. The image URL. The URL cannot exceed 2,048 characters in length and cannot be a Base64-encoded string. |
| Prompt | Strin g | Query | No | I do not understand what you mean. Please say it again. | The prompt message. |

**Response parameters**

| Parameter name | Type | Example | Description |
|---|---|---|---|
| Interrupt | Boolean | false | Indicates whether the task is interrupted. |
| Invoker | String | admin | The invoker of the operation. |
| Pk | String | 172824053450759 0 | The primary key of the disaster recovery cloud instance. |
| Bid | String | 26842 | The request ID. |
| Hid | Long | 123456 | The unique identification number. |
| Country | String | China | The country or region. |
| TaskIdentifier | String | USER LOGIN _ | The task identifier. |
| TaskExtraData | String | {"retry count": 3, _ "timeout": 300} | The extra data for the task. |
| GmtWakeup | String | 08:00 | The wakeup time. |

| Parameter name | Type | Example | Description |
|---|---|---|---|
| Success | Boolean | true | Returns the status. The operation was successful. failed: false |
| Message | String | success | The additional information. |
| Level | Long | 0 | The level. Valid values include FATAL, ERROR, WARNING, and CRITICAL. |
| Url | String | http://temp- testbucket.oss-cn- shanghai.aliyuncs. com/aivideocensor/ ****.jpg | The URL of the video screenshot. |
| Prompt | String | OK | The prompt message. |

**Examples**

Request example

```
http(s)://[Endpoint]/?Action=CheckResource &Invoker=admin &Pk=259258662544****** &Bid=26842 &Hid=1001 &Country=CN &TaskIdentifier=001 &TaskExtraData={"retry_count": 3, "timeout": 60} &GmtWakeup= &<Common request parameters>
```

Successful response example `JSON` format `{`

```json
 "GmtWakeup":"08:00",
 "Hid":"",
 "TaskIdentifier":"USER_LOGIN",
 "Message":"success",
 "Interrupt":false,
 "Success":true,
 "Url":"http://temp-testbucket.oss-cn-shanghai.aliyuncs.com/aivideocensor/****.jpg",
 "Invoker":"admin",
 "TaskExtraData":"{\"retry_count\": 3, \"timeout\": 300}",
 "Country":"China",
 "Level":0,
 "Prompt":"OK",
 "Pk":"1728240534507590",
 "Bid":"26842"
```

`}`

## SDK reference

### SDK overview

**Latest SDK version**

1.0.13

**Supported languages**

PHP Composer: https://packagist.org/packages/alibabacloud/sdk Code of DBS SDK for PHP: https://github.com/aliyun/openapi-sdk-php Python PyPI: https://pypi.org/project/aliyun-python-sdk-dbs/ Code of DBS SDK for Python: https://github.com/aliyun/aliyun-openapi-python-sdk Java Maven: https://oss.sonatype.org/#nexus-search;quick~aliyun-java-sdk-dbs Code of DBS SDK for Java: https://github.com/aliyun/aliyun-openapi-java-sdk C++ Code of DBS SDK for C++: https://github.com/aliyun/aliyun-openapi-cpp-sdk Go Code of DBS SDK for Go: https://github.com/aliyun/aliyun-openapi-java-sdk C# Nuget: https://www.nuget.org/packages/aliyun-net-sdk-dbs/ Code of DBS SDK for C#: https://github.com/aliyun/aliyun-openapi-java-sdk

### Use DBS SDK for Java based

**on Maven dependencies**

Database Backup (DBS) SDK for Java includes two core kits: aliyun-java-sdk-core and aliyunjava-sdk-dbs. The aliyun-java-sdk-core kit automatically routes requests to the DBS endpoint. The aliyun-java-sdk-dbs kit consists of related classes of all DBS features. You can use the latest versions of the two kits in the current Maven repository.

**Maven configuration**

```xml
<dependency>
    <groupId>com.aliyun</groupId>
    <artifactId>aliyun-java-sdk-dbs</artifactId>
    <version>1.0.11</version>
</dependency> <dependency>
    <groupId>com.aliyun</groupId>
    <artifactId>aliyun-java-sdk-core</artifactId>
    <version>4.4.0</version>
</dependency>
```

**Initialize a client**

```
// Use the profile to declare the AccessKey ID, AccessKey secret, and the region of the DBS backup schedule. IClientProfile profile = DefaultProfile.getProfile("cn-hangzhou", "accsessKeyId", "acce ssSecret"); // Use the profile to initialize a client object. IAcsClient client = new DefaultAcsClient(profile);
```

**Example of calling the CreateBackupPlan operation**

```
// Declare a request object. CreateBackupPlanRequest req = new CreateBackupPlanRequest(); // Configure the request parameters. For example, to call the CreateBackupPlan operatio n, you must configure the Region, DatabaseType, InstanceClass, BackupMethod, Period, and UsedTime parameters. req.setRegion("cn-hangzhou"); req.setDatabaseType("MySQL"); req.setInstanceClass("small"); req.setBackupMethod("logical"); req.setPeriod("Month"); req.setUsedTime(1); // Receive the response to the request by using the client. CreateBackupPlanResponse response = client.getAcsResponse(req); // Call the GET method in the response to retrieve the returned parameter values, such as the backup schedule ID. String backupPlanId=response.getBackupPlanId();
```

### Obtains an AccessKey pair

You can obtain the AccessKey pair on the Apsara Stack console.

**Obtain an AccessKey pair of a department**

Follow these steps:
1. Log on to the Apsara Stack console as an administrator.
2. In the top navigation bar, click the
icon, and then choose **User Center > Department**
**Management**.
3. Select a department and click **Create AccessKey** to obtain an AccessKey pair of this
department.

**Note**

The AccessKey pair is automatically allocated to a level-1 department. The sub-departments use the same AccessKey pair as their level-1 department.

**Obtain an AccessKey pair of a personal account**

Follow these steps:
1. Log on to the Apsara Stack console as an administrator.
2. In the upper-right corner of the Web page, click your avatar and select **Personal**
**Information**.
The system displays your AccessKey ID.
3. Click **Show** under **AccessKey Secret** to view the AccessKey Secret.
