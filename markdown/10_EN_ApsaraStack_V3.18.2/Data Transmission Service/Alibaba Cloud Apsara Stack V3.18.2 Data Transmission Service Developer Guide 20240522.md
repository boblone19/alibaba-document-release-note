---
title: "Alibaba Cloud Apsara Stack V3.18.2 Data Transmission Service Developer Guide 20240522"
product_version: "V3.18.2"
doc_version: "20240522"
pdf_pages: 215
source_pdf: "Alibaba Cloud Apsara Stack V3.18.2 Data Transmission Service Developer Guide 20240522.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/v3.18.2%E7%89%88%E6%9C%AC%E6%96%87%E6%A1%A3/%E6%95%B0%E6%8D%AE%E4%BC%A0%E8%BE%93DTS/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.2%20Data%20Transmission%20Service%20Developer%20Guide%2020240522.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes+edge-junk)
---

# Alibaba Cloud Apsara Stack V3.18.2 Data Transmission Service Developer Guide 20240522

## Table of Contents

- 1 API Reference
  - 1.1 Common parameters
  - 1.2 Request structure
  - 1.3 List of supported regions
  - 1.4 DTS API (new)
    - 1.4.1 CreateDtsInstance
    - 1.4.2 ConfigureDtsJob
    - 1.4.3 ConfigureSubscription
    - 1.4.4 StartDtsJob
    - 1.4.5 StartDtsJobs
    - 1.4.6 Manage consumer groups for change tracking tasks
      - 1.4.6.1 CreateConsumerChannel
      - 1.4.6.2 DescribeConsumerChannel
      - 1.4.6.3 ModifyConsumerChannel
      - 1.4.6.4 DeleteConsumerChannel
    - 1.4.7 SkipPreCheck
    - 1.4.8 Query DTS tasks
      - 1.4.8.1 DescribeDtsJobDetail
      - 1.4.8.2 DescribeDtsJobs
      - 1.4.8.3 CountJobByCondition
      - 1.4.8.4 DescribePreCheckStatus
      - 1.4.8.5 WhiteIpList
      - 1.4.8.6 DescribeSubscriptionMeta
    - 1.4.9 Modify DTS tasks
      - 1.4.9.1 ModifyDtsJob
      - 1.4.9.2 ModifySubscription
      - 1.4.9.3 ModifyDtsJobPassword
      - 1.4.9.4 ModifyDtsJobName
      - 1.4.9.5 UpgradeTwoWay
      - 1.4.9.6 TransferPayType
      - 1.4.9.7 TransferInstanceClass
      - 1.4.9.8 RenewInstance
    - 1.4.10 ResetDtsJob
    - 1.4.11 SuspendDtsJob
    - 1.4.12 SuspendDtsJobs
    - 1.4.13 StopDtsJob
    - 1.4.14 StopDtsJobs
    - 1.4.15 DeleteDtsJob
    - 1.4.16 DeleteDtsJobs
    - 1.4.17 SummaryJobDetail
    - 1.4.18 Manage alert rules
      - 1.4.18.1 CreateJobMonitorRule
      - 1.4.18.2 DescribeJobMonitorRule
    - 1.4.19 Query ETL tasks
      - 1.4.19.1 DescribeDtsEtlJobVersionInfo
      - 1.4.19.2 DescribeEtlJobLogs
    - 1.4.20 Additional parameters
      - 1.4.20.1 Objects of DTS tasks
      - 1.4.20.2 Reserve parameter description
  - 1.5 DTS API (soon-to-be-obsolete)
    - 1.5.1 Data migration
      - 1.5.1.1 CreateMigrationJob
      - 1.5.1.2 ConfigureMigrationJob
      - 1.5.1.3 StartMigrationJob
      - 1.5.1.4 ModifyMigrationObject
      - 1.5.1.5 SuspendMigrationJob
      - 1.5.1.6 DescribeMigrationJobs
      - 1.5.1.7 DescribeMigrationJobDetail
      - 1.5.1.8 DescribeMigrationJobStatus
      - 1.5.1.9 StopMigrationJob
      - 1.5.1.10 DeleteMigrationJob
    - 1.5.2 Data synchronization
      - 1.5.2.1 CreateSynchronizationJob
      - 1.5.2.2 ConfigureSynchronizationJob
      - 1.5.2.3 StartSynchronizationJob
      - 1.5.2.4 SuspendSynchronizationJob
      - 1.5.2.5 ResetSynchronizationJob
      - 1.5.2.6 ModifySynchronizationObject
      - 1.5.2.7 DescribeSynchronizationObjectModifyStatus
      - 1.5.2.8 SwitchSynchronizationEndpoint
      - 1.5.2.9 DescribeEndpointSwitchStatus
      - 1.5.2.10 ConfigureSynchronizationJobReplicatorCompare
      - 1.5.2.11 DescribeSynchronizationJobReplicatorCompare
      - 1.5.2.12 DescribeSynchronizationJobs
      - 1.5.2.13 DescribeInitializationStatus
      - 1.5.2.14 DescribeSynchronizationJobStatusList
      - 1.5.2.15 DescribeSynchronizationJobStatus
      - 1.5.2.16 DeleteSynchronizationJob
    - 1.5.3 Change tracking
      - 1.5.3.1 CreateSubscriptionInstance
      - 1.5.3.2 ConfigureSubscriptionInstance
      - 1.5.3.3 StartSubscriptionInstance
      - 1.5.3.4 ModifySubscriptionObject
      - 1.5.3.5 Manage consumer groups
        - 1.5.3.5.1 CreateConsumerGroup
        - 1.5.3.5.2 DescribeConsumerGroup
        - 1.5.3.5.3 ModifyConsumerGroupPassword
        - 1.5.3.5.4 DeleteConsumerGroup
        - 1.5.3.5.5 ModifyConsumptionTimestamp
      - 1.5.3.6 DescribeSubscriptionInstances
      - 1.5.3.7 DescribeSubscriptionInstanceStatus
      - 1.5.3.8 DeleteSubscriptionInstance
    - 1.5.4 Network settings
      - 1.5.4.1 DescribeDTSIP
      - 1.5.4.2 DescribeConnectionStatus
    - 1.5.5 Monitoring and alerting
      - 1.5.5.1 ConfigureMigrationJobAlert
      - 1.5.5.2 DescribeMigrationJobAlert
      - 1.5.5.3 ConfigureSubscriptionInstanceAlert
      - 1.5.5.4 DescribeSubscriptionInstanceAlert
      - 1.5.5.5 ConfigureSynchronizationJobAlert
      - 1.5.5.6 DescribeSynchronizationJobAlert
    - 1.5.6 Instance management
      - 1.5.6.1 ShieldPrecheck
    - 1.5.7 Tag management
      - 1.5.7.1 TagResources
      - 1.5.7.2 ListTagResources
      - 1.5.7.3 UntagResources
    - 1.5.8 Additional description of parameters
      - 1.5.8.1 MigrationObject
      - 1.5.8.2 SubscriptionObjects
      - 1.5.8.3 SynchronizationObjects
      - 1.5.8.4 MigrationReserved
- 2 Appendixes
  - 2.1 Use the ASAPI gateway to call API operations
  - 2.2 Use the ASAPI gateway to make API calls
    - 2.2.1 Obtain the endpoint of ASAPI
    - 2.2.2 Obtain the ASAPI SDK
  - 2.3 STS overview
    - 2.3.1 What is STS?
    - 2.3.2 AssumeRole

## 1 API Reference

### 1.1 Common parameters

This topic describes common parameters, including common request parameters and common response parameters. Common parameters are required in all API requests.

**Common request parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| Format | String | No | The format in which to return the response. Valid values: JSON and XML. Default value: XML. |
| Version | String | Yes | The version number of the API, in the format of YYYY-MM-DD. The current version number is 2020- 01-01. |
| AccessKeyID | String | Yes | The AccessKey ID provided to you by Alibaba Cloud. |
| Signature | String | Yes | The signature string of the current request. |
| SignatureMethod | String | Yes | The encryption method of the signature string. Set the value to HMAC-SHA1. |
| Timestamp | String | Yes | The timestamp of the request. Specify the time in the ISO 8601 standard in they yyy-MM- ddTHH:mm:ssZ format. The time must be in UTC. |
| SignatureVersion | String | Yes | The version of the signature encryption algorithm. Set the value to 1.0. |
| SignatureNonce | String | Yes | A unique random number that is used to prevent replay attacks. You must use different numbers for different requests. |

**Common response parameters**

Every response returns a unique request ID regardless of whether the call is successful.

**Sample responses**

Data Transmission Service (DTS) API uses standard HTTP status codes to indicate whether the call is successful. A 2xx status code indicates a successful call. A 4xx or 5xx status code indicates a failed call. Responses can be returned in the JSON or XML format. You can specify the response format in the request. The default response format is XML. For ease of reading, the sample responses are formatted. The actual responses do not include line breaks or indentations. Sample success responses XML format

```xml
<?xml version="1.0" encoding="utf-8"?> <!—Root node of the response--> <API operation name + Response>
    <!—Returned request tag-->
    <RequestId>4C467B38-3910-447D-87BC-AC049166F216</RequestId>
    <!—Returned result data-->
</API operation name + Response>
```

JSON format `{`

```json
    "RequestId": "4C467B38-3910-447D-87BC-AC049166F216",
    /* Returned result data */
```

`}` Sample error responses If an error occurs on your request, the system returns an HTTP status code 4xx or 5xx. The returned response body contains the specific error code and error message. The response body also contains the RequestId parameter that indicates the globally unique request ID and the HostId parameter that indicates the ID of the site that you requested to access.

> **Note:** You can troubleshoot an error based on the error code. For more information, see Error codes. If you cannot identify the cause of the error, you can contact the Alibaba Cloud customer service team and provide the returned HostId and RequestId for technical support.

XML format

```xml
<?xml version="1.0" encoding="UTF-8"?> <Error>
   <RequestId>8906582E-6722-409A-A6C4-0E7863B733A5</RequestId>
   <HostId>dts.aliyuncs.com</HostId>
   <Code>UnsupportedOperation</Code>
   <Message>The specified action is not supported.</Message>
</Error>
```

JSON format `{`

```json
    "RequestId": "7463B73D-35CC-4D19-A010-6B8D65D242EF",
    "HostId": "dts.aliyuncs.com",
    "Code": "UnsupportedOperation",
    "Message": "The specified action is not supported."
```

### 1.2 Request structure

Data Transmission Service (DTS) allows you to send URL-based requests by using the HTTP or HTTPS GET method. You must add the request parameters that correspond to the called API operation. After you call the API, the system returns a response.

**Endpoints**

| Region | Endpoint |
|---|---|
| China (Shanghai) | dts.cn-shanghai.aliyuncs.com |
| China (Qingdao) | dts.cn-qingdao.aliyuncs.com |
| China (Beijing) | dts.cn-beijing.aliyuncs.com |
| China (Zhangjiakou) | dts.cn-zhangjiakou.aliyuncs.com |
| China (Hohhot) | dts.cn-huhehaote.aliyuncs.com |
| China (Shenzhen) | dts.cn-shenzhen.aliyuncs.com |
| China (Hong Kong) | dts.cn-hongkong.aliyuncs.com |
| US (Virginia) | dts.us-east-1.aliyuncs.com |
| US (Silicon Valley) | dts.us-west-1.aliyuncs.com |

**Protocols**

You can send API requests over HTTP or HTTPS. To enhance security, we recommend that you send requests over HTTPS.

**Request methods**

You can use the HTTP GET method to send requests. If you use this method, you must include request parameters in the request URL.

**Request parameters**

In each request, you must specify the operation to be performed. For example, to create a data migration instance, you must set the Action parameter to CreateMigrationJob. Request parameters include both common parameters and operation-specific parameters.

**Encoding**

Requests and responses are encoded in UTF-8.

### 1.3 List of supported regions

This topic lists the regions that are supported by Data Transmission Service (DTS).

| Region | City | Region ID |
|---|---|---|
| China (Hangzhou) | Hangzhou | cn-hangzhou |
| China (Shanghai) | Shanghai | cn-shanghai |
| China (Qingdao) | Qingdao | cn-qingdao |
| China (Beijing) | Beijing | cn-beijing |
| China (Zhangjiakou) | Zhangjiakou | cn-zhangbei |
| China (Hohhot) | Hohhot | cn-huhehaote |
| China (Shenzhen) | Shenzhen | cn-shenzhen |
| China (Chengdu) | Chengdu | cn-chengdu |
| China (Hong Kong) | Hong Kong (China) | cn-hongkong |
| Singapore (Singapore) | Singapore | ap-southeast-1 |
| Australia (Sydney) | Sydney | ap-southeast-2 |
| Malaysia (Kuala Lumpur) | Kuala Lumpur | ap-southeast-3 |
| Indonesia (Jakarta) | Jakarta | ap-southeast-5 |
| India (Mumbai) | Mumbai | ap-south-1 |
| Japan (Tokyo) | Tokyo | ap-northeast-1 |
| US (Silicon Valley) | Silicon Valley | us-west-1 |
| US (Virginia) | Virginia | us-east-1 |
| Germany (Frankfurt) | Frankfurt | eu-central-1 |
| UK | London | eu-west-1 |
| UAE (Dubai) | Dubai | me-east-1 |
| China East 1 Finance | Hangzhou | cn-hangzhou-finance |
| China East 2 Finance | Shanghai | cn-shanghai-finance |
| China North 1 Finance | Qingdao | cn-qingdao-finance |
| China South 1 Finance | Shenzhen | cn-shenzhen-finance |

| China North 2 Ali Gov 1 | Beijing | cn-north-2-gov-1 |
|---|---|---|

### 1.4 DTS API (new)

#### 1.4.1 CreateDtsInstance

Purchases a Data Transmission Service (DTS) instance.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateDtsInstance | The operation that you want to perform. Set the value to CreateDtsInstance. |
| JobId | String | No | bi6e22ay243**** | The ID of the task. |
| InstanceClass | String | No | xxlarge | The instance class. Valid values for a data migration instance: xxlarge, xlarge, large, medium, and small Valid values for a data synchronization instance: large, medium, small, and micro |
| PayType | String | No | PrePaid | The billing method. Valid values: PrePaid: subscription PostPaid: pay-as-you-go Note This parameter is required. |
| Period | String | No | Month | The unit of the subscription duration. Valid values:Y ear and Month. Note This parameter is available and required only if the PayType parameter is set to PrePaid. |
| SyncArchitecture | String | No | oneway | The synchronization topology. Default value: oneway. Valid values: oneway: one-way synchronization bidirectional: two-way synchronization |
| AutoStart | Boolean | No | false | Specifies whether to automatically start the task after the purchase is complete. Valid values: false: no true: yes |
| UsedTime | Integer | No | 5 | The subscription duration. Note This parameter is available and required only if the PayType parameter is set to PrePaid. You can set the Period parameter to specify the unit of the subscription duration. |
| Quantity | Integer | No | 1 | The number of DTS instances that you want to purchase. Note You can purchase only a single instance at a time. |
| AutoPay | Boolean | No | false | Specifies whether to automatically renew the DTS instance when it expires. Valid values: false: no true: yes |
| Type | String | No | MIGRATION | The type of the DTS instance. Valid values: MIGRATION: data migration instance SYNC: data synchronization instance SUBSCRIBE: change tracking instance |

| DatabaseCount | Integer | No | 3 | The number of private custom ApsaraDB RDS instances in a PolarDB-X instance. Default value: 1. Note This parameter is required only if the SourceEndpointEngineName parameter is set to drds. |
|---|---|---|---|---|
| SourceRegion | String | No | cn-hangzhou | The region where the source instance resides. |
| DestinationRegion | String | No | cn-hangzhou | The region where the destination instance resides. |
| SourceEndpointEngineName | String | No | MYSQL | The database engine of the source instance. MySQL: ApsaraDB RDS for MySQL instance or self-managed MySQL database PolarDB: PolarDB for MySQL cluster polardbo: PolarDB for Oracle cluster _ polardbpg: PolarDB for PostgreSQL cluster _ Redis: ApsaraDB for Redis instance or self-managed Redis database DRDS: PolarDB-X 1.0 or PolarDB-X 2.0 instance PostgreSQL: self-managed PostgreSQL database odps: MaxCompute project oracle: self-managed Oracle database mongodb: ApsaraDB for MongoDB instance or self- managed MongoDB database tidb: TiDB database ADS: AnalyticDB for MySQL V2.0 cluster ADB30: AnalyticDB for MySQL V3.0 cluster Greenplum: AnalyticDB for PostgreSQL instance MSSQL: ApsaraDB RDS for SQL Server instance or self- managed SQL Server database kafka: Message Queue for Apache Kafka instance or self- managed Kafka cluster DataHub: DataHub project clickhouse: ApsaraDB for ClickHouse cluster DB2: self-managed Db2 for LUW database as400: AS/400 Tablestore: Tablestore instance Note The default value is MySQL. |
| DestinationEndpointEngineN ame | String | No | MySQL | The database engine of the destination instance. MySQL: ApsaraDB RDS for MySQL instance or self-managed MySQL database PolarDB: PolarDB for MySQL cluster polardbo: PolarDB for Oracle cluster _ polardbpg: PolarDB for PostgreSQL cluster _ Redis: ApsaraDB for Redis instance or self-managed Redis database DRDS: PolarDB-X 1.0 or PolarDB-X 2.0 instance PostgreSQL: self-managed PostgreSQL database odps: MaxCompute project oracle: self-managed Oracle database mongodb: ApsaraDB for MongoDB instance or self- managed MongoDB database tidb: TiDB database ADS: AnalyticDB for MySQL V2.0 cluster ADB30: AnalyticDB for MySQL V3.0 cluster Greenplum: AnalyticDB for PostgreSQL instance MSSQL: ApsaraDB RDS for SQL Server instance or self- managed SQL Server database kafka: Message Queue for Apache Kafka instance or self- managed Kafka cluster DataHub: DataHub project clickhouse: ApsaraDB for ClickHouse cluster DB2: self-managed Db2 for LUW database as400: AS/400 Tablestore: Tablestore instance Note The default value is MySQL. |
| ComputeUnit | Integer | No | 5 | The specifications of the extract, transform, and load (ETL) instance. The unit is compute unit (CU). One CU is equal to 1 vCPU and 4 GB of memory. The value of this parameter must be an integer greater than or equal to 2. |
| RegionId | String | No | cn-hangzhou | The region ID of the DTS instance. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| ErrCode | String | InternalError | The error code returned if the call failed. |
| ErrMessage | String | The request processing has failed due to some unknown error. | The error message returned if the call failed. |
| InstanceId | String | dtsbi6e22ay243**** | The ID of DTS instance. |
| JobId | String | bi6e22ay243**** | The ID of the task. |
| RequestId | String | C166D79D-436B-45F0-B5A5- 25E1**** | The ID of the request. |
| Success | String | true | Indicates whether the call was successful. |

**Examples**

Sample requests

```
http(s)://dts.aliyuncs.com/?Action=CreateDtsInstance &<Common request parameters>
```

Sample success responses

| XML | format |
|---|---|
| <CreateDtsInstanceResponse> <RequestId>C166D79D-436B-45F0-B5A5-25E1****</RequestId> <Success>true</Success> </CreateDtsInstanceResponse> |   |

| JSON | format |
|---|---|
| { "RequestId":"C166D79D-436B-45F0-B5A5-25E1****", "Success":"true" } |   |

#### 1.4.2 ConfigureDtsJob

Configures a data migration or data synchronization task. Before you configure a task, you must call the CreateDtsInstance operation to purchase a Data Transmission Service (DTS) instance.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ConfigureDtsJob | The operation that you want to perform. Set the value to ConfigureDtsJob. |
| DataInitialization | Boolean | Yes | true | Specifies whether to perform full data migration or full data synchronization. Default value: true. Valid values: true: performs full data migration or full data synchronization. false: does not perform full data migration or full data synchronization. |
| DataSynchronization | Boolean | Yes | true | Specifies whether to perform incremental data migration or incremental data synchronization. Default value: false. Valid values: false: does not perform incremental data migration or incremental data synchronization. true: performs incremental data migration or incremental data synchronization. |
| DbList | String | Yes | {"dtstest": {"name":"dtstest","all":true} } | The objects that you want to migrate or synchronize. The value is a JSON string. |

| DestinationEndpointInstance Type | String | Yes | EXPRESS | The destination instance of the task. Valid values: Alibaba Cloud database instance RDS: ApsaraDB RDS for MySQL instance, ApsaraDB RDS for SQLServer instance, ApsaraDB RDS for PostgreSQL instance, or ApsaraDB RDS for MariaDB TX instance PolarDB: PolarDB for MySQL cluster POLARDBX20: PolarDB-X 2.0 instance ADS: AnalyticDB for MySQL V2.0 cluster or AnalyticDB for MySQL V3.0 cluster MONGODB: ApsaraDB for MongoDB instance GREENPLUM: AnalyticDB for PostgreSQL instance DATAHUB: DataHub project REDIS: ApsaraDB for Redis instance Self-managed database OTHER: self-managed database with a public IP address ECS: self-managed database hosted on ECS EXPRESS: self-managed database connected over Express Connect CEN: self-managed database connected over Cloud Enterprise Network (CEN) DG: self-managed database connected over Database Gateway Note If the destination instance is a PolarDB for Oracle cluster, you must set this parameter to OTHER or EXPRESS because you can use only the PolarDB for Oracle cluster as a self-managed database connected over the Internet or Express Connect. If the destination instance is a Message Queue for Apache Kafka instance, you must set this parameter to ECS or EXPRESS because you can use only the Message Queue for Apache Kafka instance as a self-managed database connected over Elastic Compute Service (ECS) or Express Connect. If the destination instance is a self-managed database, you must deploy the network environment for the database. |
|---|---|---|---|---|
| DtsJobName | String | Yes | ApsaraDB RDS for MySQL to self-managed MySQL database connected over Express Connect | The name of the DTS instance. |
| JobType | String | Yes | SYNC | The type of the DTS task. Valid values: MIGRATION: data migration SYNC: data synchronization |
| SourceEndpointInstanceType | String | Yes | RDS | The source instance of this task. Valid values: Alibaba Cloud database instance RDS: ApsaraDB RDS for MySQL instance, ApsaraDB RDS for SQLServer instance, ApsaraDB RDS for PostgreSQL instance, or ApsaraDB RDS for MariaDB TX instance PolarDB: PolarDB for MySQL cluster POLARDBX20: PolarDB-X 2.0 instance MONGODB: ApsaraDB for MongoDB instance DISTRIBUTEDDMSLOGICDB: Data Management (DMS) _ logical database REDIS: ApsaraDB for Redis instance Self-managed database OTHER: self-managed database with a public IP address ECS: self-managed database hosted on ECS EXPRESS: self-managed database connected over Express Connect CEN: self-managed database connected over CEN DG: self-managed database connected over Database Gateway Note If the source instance is a PolarDB for Oracle cluster, you must set this parameter to OTHER or EXPRESS because you can use only the PolarDB for Oracle cluster as a self-managed database connected over the Internet or Express Connect. If your source database is a self-managed database, you must deploy the network environment for the database. |

| StructureInitialization | Boolean | Yes | true | Specifies whether to perform schema migration or schema synchronization. Default value: true. Valid values: true: performs schema migration or schema synchronization. false: does not perform schema migration or schema synchronization. |
|---|---|---|---|---|
| SourceEndpointInstanceID | String | No | rm-bp1imrtn6fq7h**** | The ID of the source instance. If the source instance is an Alibaba Cloud database instance, you must specify the ID of the database instance. For example, if the source instance is an ApsaraDB RDS for MySQL instance, you must specify the ID of the ApsaraDB RDS for MySQL instance. If the source instance is a self-managed database, the value of this parameter varies with the value of the SourceEndpointInstanceType parameter. If SourceEndpointInstanceType is set to ECS, you must specify the ID of the ECS instance. If SourceEndpointInstanceType is set to DG, you must specify the ID of the database gateway. If SourceEndpointInstanceType is set to EXPRESS or CEN, you must specify the ID of the VPC that is connected to the source database. Note If the value of the SourceEndpointInstanceType parameter is set to CEN, you must also specify the ID of the CEN instance in the Reserve parameter. |
| SourceEndpointEngineName | String | No | MYSQL | The database type of the source instance. MYSQL: ApsaraDB RDS for MySQL instance or self- managed MySQL database PolarDB: PolarDB for MySQL cluster POLARDBO: PolarDB for Oracle cluster _ POLARDBX20: PolarDB-X 2.0 instance ORACLE: self-managed Oracle database POSTGRESQL: ApsaraDB RDS for PostgreSQL instance or self-managed PostgreSQL database MSSQL: ApsaraDB RDS for SQL Server instance or self- managed SQL Server database MONGODB: ApsaraDB for MongoDB instance or self- managed MongoDB database DB2: self-managed Db2 for LUW database AS400: self-managed Db2 for i database DMSPOLARDB: DMS logical database HBASE: self-managed HBase database TERADATA: Teradata database REDIS: ApsaraDB for Redis instance or self-managed Redis database Note Default value: MYSQL. If the parameter is set to MONGODB, you must also specify the architecture type of the MongoDB database in the Reserve parameter. |
| SourceEndpointRegion | String | No | cn-hangzhou | The region ID of the source instance. Note If the source instance is an Alibaba Cloud database instance, this parameter is required. |
| SourceEndpointIP | String | No | 172.16.**.*** | The IP address of the source instance. Note If the SourceEndpointInstanceType parameter is set to OTHER, EXPRESS, DG, or CEN, this parameter is available and required. |
| SourceEndpointPort | String | No | 3306 | The port number of the source instance. Note If the source instance is a self-managed database, this parameter is available and required. |
| SourceEndpointOracleSID | String | No | testsid | The system ID (SID) of the Oracle database. Note If the SourceEndpointEngineName parameter is set to Oracle and the Oracle database is deployed in a non-RAC architecture, this parameter is available and required. |

| SourceEndpointDatabaseNa me | String | No | dtstestdatabase | The name of the database to which the objects to be migrated in the source instance belong. Note If the source instance is a PolarDB for Oracle cluster, a PostgreSQL database, or a MongoDB database, this parameter is available and required. |
|---|---|---|---|---|
| SourceEndpointUserName | String | No | dtstest | The database account of the source database. Note In most cases, this parameter is required. Data migration and data synchronization have different requirements for database permissions. |
| SourceEndpointPassword | String | No | Test123456 | The password of the source database account. |
| SourceEndpointOwnerID | String | No | 140692647406**** | The ID of the Alibaba Cloud account to which the source instance belongs. Note You can specify this parameter to migrate or synchronize data across different Alibaba Cloud accounts. In this case, you must specify the SourceEndpointRole parameter. |
| SourceEndpointRole | String | No | ram-for-dts | The name of the Resource Access Management (RAM) role configured for the Alibaba Cloud account that owns the source instance. Note This parameter is required if data is migrated or synchronized across Alibaba Cloud accounts. |
| DestinationEndpointInstanceI D | String | No | vpc-bp1opxu1zkhn00gzv**** | The ID of the destination instance. If the destination instance is an Alibaba Cloud database instance, you must specify the ID of the database instance. For example, if the source instance is an ApsaraDB RDS for MySQL instance, you must specify the ID of the ApsaraDB RDS for MySQL instance. If the destination instance is a self-managed database, the value of this parameter varies with the value of the DestinationEndpointInstanceType parameter. If SourceEndpointInstanceType is set to ECS, you must specify the ID of the ECS instance. If SourceEndpointInstanceType is set to DG, you must specify the ID of the database gateway. If SourceEndpointInstanceType is set to EXPRESS or CEN, you must specify the ID of the VPC that is connected to the source database. Note If the value of the SourceEndpointInstanceType parameter is set to CEN, you must also specify the ID of the CEN instance in the Reserve parameter. |

| DestinationEndpointEngineN ame | String | No | MySQL | The database type of the destination instance. MySQL: ApsaraDB RDS for MySQL instance or self-managed MySQL database PolarDB: PolarDB for MySQL cluster POLARDBO: PolarDB for Oracle cluster _ POLARDBX20: PolarDB-X 2.0 instance ORACLE: self-managed Oracle database POSTGRESQL: ApsaraDB RDS for PostgreSQL instance or self-managed PostgreSQL database MSSQL: ApsaraDB RDS for SQL Server instance or self- managed SQL Server database ADS: AnalyticDB for MySQL V2.0 cluster ADB30: AnalyticDB for MySQL V3.0 cluster MONGODB: ApsaraDB for MongoDB instance or self- managed MongoDB database GREENPLUM: AnalyticDB for PostgreSQL instance KAFKA: Message Queue for Apache Kafka instance or self- managed Kafka cluster DATAHUB: DataHub project DB2: self-managed Db2 for LUW database AS400: self-managed Db2 for i database REDIS: ApsaraDB for Redis instance or self-managed Redis database Note Default value: MYSQL. If the database type of the destination instance is set to KAFKA or MONGODB, you must also specify the database information in the Reserve parameter. |
|---|---|---|---|---|
| DestinationEndpointRegion | String | No | cn-hangzhou | The region ID of the destination instance. Note If the destination instance is an Alibaba Cloud database instance, the parameter is required. |
| DestinationEndpointIP | String | No | 172.16.**.*** | The IP address of the destination instance. Note If the DestinationEndpointInstanceType parameter is set to OTHER, EXPRESS, DG, or CEN, this parameter is available and required. |
| DestinationEndpointPort | String | No | 3306 | The port number of the destination instance. Note If the destination instance is a self-managed database, this parameter is available and required. |
| DestinationEndpointDataBas eName | String | No | dtstestdata | The name of the database to which the objects migrated to the destination instance belong. Note If the destination instance is a PolarDB for Oracle cluster, an AnalyticDB for PostgreSQL instance, a PostgreSQL database, or a MongoDB database, this parameter is available and required. |
| DestinationEndpointUserNam e | String | No | dtstest | The database account of the destination database. Note In most cases, this parameter is required. Data migration and data synchronization have different requirements for database permissions. |
| DestinationEndpointPasswor d | String | No | Test123456 | The password of the destination database account. |
| Reserve | String | No | { "srcInstanceId": "cen- 9kqshqum*******" } | The reserved parameter of DTS. The value is a JSON string. You can specify this parameter to add more configurations of the source or destination instance to the DTS task. For example, you can specify the data storage format of the destination Kafka database and the ID of the CEN instance. |
| Checkpoint | String | No | 1610540493 | The start offset of incremental data migration or data synchronization. The value is a UNIX timestamp. Unit: seconds. |

| DestinationEndpointOracleSI D | String | No | testsid | The SID of the Oracle database. Note If the DestinationEndpointEngineName parameter is set to Oracle and the Oracle database is deployed in a non-RAC architecture, this parameter is available and required. |
|---|---|---|---|---|
| DtsJobId | String | No | k2gm967v16f**** | The ID of the data migration, data synchronization, or change tracking task. Note You must specify at least one of the DtsJobId and DtsInstanceId parameters. You can call the DescribeDtsJobs operation to query the task ID. |
| DtsInstanceId | String | No | dtsk2gm967v16f**** | The ID of the data migration, data synchronization, or change tracking instance. Note You must specify at least one of the DtsJobId and DtsInstanceId parameters. You can call the DescribeDtsJobs operation to query the instance ID. |
| DelayPhone | String | No | 1361234****,1371234**** | The mobile numbers that receive latency-related alerts. Separate multiple mobile numbers with commas (,). Note This parameter is available only for China site (aliyun.com) users. Only mobile numbers in the Chinese mainland are supported. Up to 10 mobile numbers can be specified. International site (alibabacloud.com) users cannot receive alerts by using mobile phones, but can set alert rules for DTS tasks in the CloudMonitor console. |
| DelayRuleTime | Long | No | 10 | The threshold for triggering latency alerts. Unit: seconds. The value must be an INTEGER. You can set the threshold based on your business needs. To prevent jitters caused by network and database overloads, we recommend that you set the threshold to more than 10 seconds. Note If the DelayNotice parameter is set to true, this parameter is required. |
| DelayNotice | Boolean | No | true | Specifies whether to monitor the task latency. Valid values: true: monitors the task latency. false: does not monitor the task latency. |
| ErrorPhone | String | No | 1361234****,1371234**** | The mobile numbers that receive state-related alerts. Separate multiple mobile numbers with commas (,). Note This parameter is available only for China site (aliyun.com) users. Only mobile numbers in the Chinese mainland are supported. Up to 10 mobile numbers can be specified. International site (alibabacloud.com) users cannot receive alerts by using mobile phones, but can set alert rules for DTS tasks in the CloudMonitor console. |
| ErrorNotice | Boolean | No | true | Specifies whether to monitor the task state. Valid values: true: monitors the task state. false: does not monitor the task state. |
| SynchronizationDirection | String | No | Forward | The synchronization direction. Valid values: Forward: Data is synchronized from the source database to the destination database. Reverse: Data is synchronized form the destination database to the source database. Note Default value: Forward. The value Reverse takes effect only if the topology of the data synchronization task is two- way synchronization. |
| RegionId | String | No | cn-hangzhou | The region ID of the DTS instance. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| DtsInstanceId | String | dtsk2gm967v16f**** | The ID of the data migration, data synchronization, or change tracking instance. |
| DtsJobId | String | k2gm967v16f**** | The ID of the data migration, data synchronization, or change tracking task. |
| ErrCode | String | InternalError | The error code returned if the call failed. |
| ErrMessage | String | The request processing has failed due to some unknown error. | The error message returned if the call failed. |
| HttpStatusCode | String | 200 | The HTTP status code. |
| RequestId | String | 224DB9F7-3100-4899-AB9C- C938BCCB**** | The ID of the request. |
| Success | String | true | Indicates whether the call was successful. |

**Examples**

Sample requests

```
http(s)://dts.aliyuncs.com/?Action=ConfigureDtsJob &RegionId=cn-hangzhou &SourceEndpointInstanceType=RDS &DestinationEndpointInstanceType=EXPRESS &StructureInitialization=true &DataInitialization=true &DataSynchronization=true &DbList={"dtstest":{"name":"dtstest","all":true}} &JobType=SYNC &SourceEndpointInstanceID=rm-bp1imrtn6fq7h**** &SourceEndpointEngineName=MYSQL &SourceEndpointRegion=cn-hangzhou &SourceEndpointUserName=dtstest &SourceEndpointPassword=Test123456 &DestinationEndpointInstanceID=vpc-bp1opxu1zkhn00gzv**** &DestinationEndpointEngineName=MYSQL &DestinationEndpointIP=172.16.**.*** &DestinationEndpointRegion=cn-hangzhou &DestinationEndpointPort=3306 &DestinationEndpointUserName=dtstest &DestinationEndpointPassword=Test123456 &DtsJobId=k2gm967v16f**** &DtsInstanceId=dtsk2gm967v16f**** &DtsJobName=ApsaraDB RDS for MySQL to self-managed MySQL database connected over Express Connect &<Common request parameters>
```

Sample success responses

| XML | format |
|---|---|
| <ConfigureDtsJobResponse> <DtsJobId>k2gm967v16f****</DtsJobId> <RequestId>224DB9F7-3100-4899-AB9C-C938BCCB****</RequestId> <HttpStatusCode>200</HttpStatusCode> <DtsInstanceId>dtsk2gm967v16f****</DtsInstanceId> <Success>true</Success> </ConfigureDtsJobResponse> |   |

| JSON | format |
|---|---|
| { "DtsJobId":"k2gm967v16f****", "RequestId":"224DB9F7-3100-4899-AB9C-C938BCCB****", "HttpStatusCode":200, "DtsInstanceId":"dtsk2gm967v16f****", "Success":true } |   |

#### 1.4.3 ConfigureSubscription

Configures a change tracking task.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|

| Action | String | Yes | ConfigureSubscription | The operation that you want to perform. Set the value to ConfigureSubscription. |
|---|---|---|---|---|
| DbList | String | Yes | {"dtstest": {"name":"dtstest","all":true} } | The objects of the change tracking task. The value is a JSON string. |
| DtsJobName | String | Yes | MySQL Change Tracking | The name of the tracking task. Note We recommend that you specify a descriptive name that makes it easy to identify. You do not need to use a unique name. |
| RegionId | String | Yes | cn-hangzhou | The region where the Data Transmission Service (DTS) instance resides. |
| SubscriptionInstanceNetwork Type | String | Yes | classic | The network type of the change tracking task. Valid values: classic: classic network vpc: virtual private cloud (VPC) Note If you specify this parameter, the new version of the change tracking feature is used. Otherwise, the old version of this feature is used. The old version of the change tracking feature supports self-managed MySQL databases, ApsaraDB RDS for MySQL instances, and PolarDB- X 1.0 instances. The new version of the change tracking feature supports self-managed MySQL databases, ApsaraDB RDS for MySQL instances, PolarDB for MySQL clusters, and Oracle databases. If you set this parameter to vpc, you must also specify the SubscriptionInstanceVPCId and SubscriptionInstanceVSwitchID parameters. |
| DtsInstanceId | String | No | dtsy0zz3t13h7d**** | The ID of the change tracking instance. |
| DtsJobId | String | No | y0zz3t13h7d**** | The ID of the change tracking task. |
| SourceEndpointEngineName | String | No | MySQL | The engine of the source database. Valid values: MySQL and Oracle. Note If the source database is a self-managed database, this parameter is required. |
| SourceEndpointInstanceType | String | No | RDS | The type of the source instance. Valid values: RDS: ApsaraDB RDS for MySQL instance. PolarDB: PolarDB for MySQL cluster. DRDS: PolarDB-X 1.0 instance. LocalInstance: self-managed database with a public IP address. ECS: self-managed database hosted on Elastic Compute Service (ECS). Express: self-managed database connected over Express Connect. CEN: self-managed database connected over Cloud Enterprise Network (CEN). dg: self-managed database connected over Database Gateway. |
| SourceEndpointRegion | String | No | cn-hangzhou | The region where the source instance resides. Note If the source instance is a self-managed database with a public IP address, you can set the parameter to cn-hangzhou or the ID of the closest region. |
| SourceEndpointInstanceID | String | No | rm-bp1zc3iyqe3qw**** | The ID of the source instance. Note This parameter is available and required only if the source instance is an ApsaraDB RDS for MySQL instance, a PolarDB-X 1.0 instance, or a PolarDB for MySQL cluster. |
| SourceEndpointIP | String | No | 172.16.8*.*** | The endpoint of the source database. Note This parameter is available and required only if the source database is a self-managed database. |

| SourceEndpointPort | String | No | 3306 | The service port number of the source database. Note This parameter is available and required only if the source database is a self-managed database. |
|---|---|---|---|---|
| SourceEndpointOracleSID | String | No | testsid | The system ID (SID) of the Oracle database. Note This parameter is available and required only if the source database is a self-managed Oracle database and the Oracle database is deployed in a non- RAC architecture. |
| SourceEndpointDatabaseNa me | String | No | dtstestdata | The name of the source database. |
| SourceEndpointUserName | String | No | dtstest | The database account of the source instance. Note The permissions required for the database account to track data changes vary with the database engine. |
| SourceEndpointPassword | String | No | Test123456 | The password of the source database account. |
| SourceEndpointOwnerID | String | No | 140692647406**** | The ID of the Alibaba Cloud account to which the source instance belongs. Note This parameter is available and required only if you track data changes across different Alibaba Cloud accounts. |
| SourceEndpointRole | String | No | ram-for-dts | The authorized RAM role of the source instance. If the source instance does not belong to the Alibaba Cloud account that you use to configure the change tracking task, this parameter is required. In this case, you must allow the Alibaba Cloud account that you use to configure the change tracking task to access the source instance. |
| Reserve | String | No | { "srcInstanceId": "cen- 9kqshqum*******" } | The reserved parameter of DTS. The value is a JSON string. You can specify this parameter to add more configurations of the source or destination instance to the DTS task. For example, you can specify the data storage format of the destination Kafka database and the ID of the CEN instance. |
| Checkpoint | String | No | 1616902385 | The UNIX timestamp that represents the start of change tracking. Note You can use a search engine to obtain a UNIX timestamp converter. |
| SubscriptionInstanceVPCId | String | No | vpc-bp1vwnn14rqpyiczj**** | The ID of the VPC where the change tracking instance is deployed. Note This parameter is available and required only if the SubscriptionInstanceNetworkType parameter is set to vpc. |
| SubscriptionInstanceVSwitchI d | String | No | vsw- bp10df3mxae6lpmku**** | The ID of the vSwitch in the specified VPC. Note This parameter is available and required only if the SubscriptionInstanceNetworkType parameter is set to vpc. |
| SubscriptionDataTypeDDL | Boolean | No | true | Specifies whether to track DDL statements. Default value: true. Valid values: true: yes. false: no |
| SubscriptionDataTypeDML | Boolean | No | true | Specifies whether to track DML statements. Default value: true. Valid values: true: yes. false: no |

| DelayPhone | String | No | 1361234****,1371234**** | The mobile numbers that receive latency-related alerts. Separate multiple mobile numbers with commas (,). Note This parameter is available only for China site (aliyun.com) users. Only mobile numbers in the Chinese mainland are supported. Up to 10 mobile numbers can be specified. International site (alibabacloud.com) users cannot receive alerts by using mobile phones, but can set alert rules for DTS tasks in the CloudMonitor console. |
|---|---|---|---|---|
| DelayRuleTime | Long | No | 10 | The threshold for triggering latency alerts. Unit: seconds. The value must be an integer. You can set the threshold based on your business needs. To prevent jitters caused by network and database overloads, we recommend that you set the threshold to more than 10 seconds. Note If the DelayNotice parameter is set to true, this parameter is required. |
| DelayNotice | Boolean | No | true | Specifies whether to monitor the task latency. Valid values: true: yes false: no |
| ErrorPhone | String | No | 1361234****,1371234**** | The mobile numbers that receive state-related alerts. Separate multiple mobile numbers with commas (,). Note This parameter is available only for China site (aliyun.com) users. Only mobile numbers in the Chinese mainland are supported. Up to 10 mobile numbers can be specified. International site (alibabacloud.com) users cannot receive alerts by using mobile phones, but can set alert rules for DTS tasks in the CloudMonitor console. |
| ErrorNotice | Boolean | No | true | Specifies whether to monitor the task state. Valid values: true: yes false: no |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| DtsInstanceId | String | dtsy0zz3t13h7d**** | The ID of the change tracking instance. |
| DtsJobId | String | y0zz3t13h7d**** | The ID of the change tracking task. |
| ErrCode | String | InternalError | The error code returned if the call failed. |
| ErrMessage | String | The request processing has failed due to some unknown error. | The error message returned if the call failed. |
| HttpStatusCode | String | 200 | The HTTP status code. |
| RequestId | String | 1D6ECADF-C5E9-4C96-8811- 77602B31**** | The ID of the request. |
| Success | String | true | Indicates whether the call was successful. |

**Examples**

Sample requests

```
http(s)://dts.aliyuncs.com/?Action=ConfigureSubscription &DbList={"dtstest":{"name":"dtstest","all":true}} &DtsJobName=MySQL Change Tracking &JobType=SUBSCRIBE &SourceEndpointInstanceType=RDS &SubscriptionInstanceNetworkType=classic &SourceEndpointInstanceID=rm-bp1zc3iyqe3qw**** &SourceEndpointUserName=dtstest &SourceEndpointPassword=Test123456
```

| XML | format |
|---|---|
| <ConfigureSubscriptionResponse> <DtsJobId>y0zz3t13h7d****</DtsJobId> <RequestId>1D6ECADF-C5E9-4C96-8811-77602B31****</RequestId> <HttpStatusCode>200</HttpStatusCode> <DtsInstanceId>dtsy0zz3t13h7d****</DtsInstanceId> <Success>true</Success> </ConfigureSubscriptionResponse> |   |

| JSON | format |
|---|---|
| { "DtsJobId":"y0zz3t13h7d****", "RequestId":"1D6ECADF-C5E9-4C96-8811-77602B31****", "HttpStatusCode":200, "DtsInstanceId":"dtsy0zz3t13h7d****", "Success":true } |   |

#### 1.4.4 StartDtsJob

Starts a data migration, data synchronization, or change tracking task.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | StartDtsJob | The operation that you want to perform. Set the value to StartDtsJob. |
| DtsJobId | String | Yes | l3m1213ye7l**** | The ID of the data migration, data synchronization, or change tracking task. |
| DtsInstanceId | String | No | dtsl3m1213ye7l**** | The ID of the data migration, data synchronization, or change tracking instance. Note You can call the DescribeMigrationJobs, DescribeSubscriptionInstances, or DescribeSynchronizationJobs operation to query the instance ID. |
| SynchronizationDirection | String | No | Forward | The synchronization direction. Default value: Forward. Valid values: Forward: Data is synchronized from the source database to the destination database. Reverse: Data is synchronized from the destination database to the source database. Note You can set this parameter to Reverse to start the reverse synchronization task only if the topology is two-way synchronization. |
| RegionId | String | No | cn-hangzhou | The region where the Data Transmission Service (DTS) instance resides. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| DynamicCode | String | 403 | The dynamic error code. This parameter will be removed in the future. |
| DynamicMessage | String | DtsJobId | The dynamic part in the error message. The value of this parameter is used to replace the %s variable in the value of the ErrMessage parameter. Note If the return value of the ErrMessage parameter is The Value of Input Parameter %s is not valid and the return value of the DynamicMessage parameter is DtsJobId, the specified DtsJobId parameter is invalid. |
| ErrCode | String | InternalError | The error code returned if the call failed. |
| ErrMessage | String | The Value of Input Parameter %s is not valid. | The error message returned if the call failed. |
| HttpStatusCode | Integer | 200 | The HTTP status code. |
| RequestId | String | 601B6F25-21E7-4484-99D5- 3EF2625C**** | The ID of the request. |

| Success | Boolean | true | Indicates whether the call was successful. |
|---|---|---|---|

Sample requests

```
http(s)://dts.aliyuncs.com/?Action=StartDtsJob &DtsJobId=l3m1213ye7l**** &<Common request parameters>
```

Sample success responses

| XML | format |
|---|---|
| <StartDtsJobResponse> <RequestId>2D3B4615-923F-49AA-AF21-6D8E3967****</RequestId> <HttpStatusCode>200</HttpStatusCode> <Success>true</Success> </StartDtsJobResponse> |   |

| JSON | format |
|---|---|
| { "RequestId":"2D3B4615-923F-49AA-AF21-6D8E3967****", "HttpStatusCode":200, "Success":true } |   |

#### 1.4.5 StartDtsJobs

Starts multiple data migration or data synchronization tasks.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | StartDtsJobs | The operation that you want to perform. Set the value to StartDtsJobs. |
| DtsJobIds | String | Yes | l5o11f9029c**** | The ID of the data migration or data synchronization task. Note Separate multiple task IDs with commas (,). You can call the DescribeDtsJobs operation to query task IDs. |
| RegionId | String | No | cn-hangzhou | The region ID of the Data Transmission Service (DTS) instance. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| DynamicCode | String | 403 | The dynamic error code. This parameter will be removed in the future. |
| DynamicMessage | String | DtsJobId | The dynamic part in the error message. The value of this parameter is used to replace the %s variable in the value of the ErrMessage parameter. Note If the return value of the ErrMessage parameter is The Value of Input Parameter %s is not valid and the return value of the DynamicMessage parameter is DtsJobId, the specified DtsJobId parameter is invalid. |
| ErrCode | String | InternalError | The error code returned if the call failed. |
| ErrMessage | String | The Value of Input Parameter %s is not valid. | The error message returned if the call failed. |
| HttpStatusCode | Integer | 200 | The HTTP status code. |
| RequestId | String | AD823BD3-1BA6-4117-A536- 165CB280**** | The ID of the request. |
| Success | Boolean | true | Indicates whether the call was successful. |

```
http(s)://dts.aliyuncs.com/?Action=StartDtsJobs &DtsJobIds=l5o11f9029c**** &RegionId=cn-hangzhou
```

Sample success responses

| XML | format |
|---|---|
| <StartDtsJobsResponse> <RequestId>AD823BD3-1BA6-4117-A536-165CB280****</RequestId> <HttpStatusCode>200</HttpStatusCode> <Success>true</Success> </StartDtsJobsResponse> |   |

| JSON | format |
|---|---|
| { "RequestId": "AD823BD3-1BA6-4117-A536-165CB280****", "HttpStatusCode": 200, "Success": true } |   |

#### 1.4.6 Manage consumer groups for change tracking tasks

##### 1.4.6.1 CreateConsumerChannel

Creates a consumer group for a change tracking task. Downstream clients can use the consumer group to consume tracked data.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateConsumerChannel | The operation that you want to perform. Set the value to CreateConsumerChannel. |
| ConsumerGroupName | String | Yes | Consumer Group A | The name of the consumer group. The name can be up to 128 characters in length. We recommend that you use a descriptive name that makes it easy to identify. |
| ConsumerGroupPassword | String | Yes | Test123456 | The password of the consumer group. The password must contain at least two of the following character types: uppercase letters, lowercase letters, digits, and special characters. The password must be 8 to 32 characters in length. |
| ConsumerGroupUserName | String | Yes | dtstest | The username of the consumer group. A username can contain uppercase letters, lowercase letters, digits, and underscores (). _ A username can be up to 16 characters in length. |
| RegionId | String | Yes | cn-hangzhou | The region ID of the change tracking instance. |
| DtsInstanceId | String | No | dtsboss6pn1w****** | The ID of the change tracking instance. You can call the DescribeDtsJobs operation to query the instance ID. Note You must specify at least one of the DtsInstanceId and DtsJobId parameters. |
| DtsJobId | String | No | boss6pn1w****** | The ID of the change tracking task. You can call the DescribeDtsJobs operation to query the task ID. Note You must specify at least one of the DtsInstanceId and DtsJobId parameters. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| ConsumerGroupID | String | dtsor2y66j4219**** | The ID of the consumer group. You can specify this parameter on a downstream client when you consume tracked data. |
| ErrCode | String | InternalError | The error code returned if the call failed. |
| ErrMessage | String | The request processing has failed due to some unknown error. | The error message returned if the call failed. |

| HttpStatusCode | String | 200 | The HTTP status code. |
|---|---|---|---|
| RequestId | String | 5F566C5B-E5B0-4020-A531- FC6F5005**** | The ID of the request. |
| Success | String | true | Indicates whether the call was successful. |

**Examples**

Sample requests

```
http(s)://dts.aliyuncs.com/?Action=CreateConsumerChannel &ConsumerGroupName=Consumer Group A &ConsumerGroupPassword=Test123456 &ConsumerGroupUserName=dtstest &RegionId=cn-hangzhou &DtsInstanceId=dtsboss6pn1w******
```

Sample success responses

| XML | format |
|---|---|
| <CreateConsumerChannelResponse> <ConsumerGroupID>dtsor2y66j4219****</ConsumerGroupID> <RequestId>5F566C5B-E5B0-4020-A531-FC6F5005****</RequestId> <HttpStatusCode>200</HttpStatusCode> <Success>true</Success> </CreateConsumerChannelResponse> |   |

| JSON | format |
|---|---|
| { "ConsumerGroupID": "dtsor2y66j4219****", "RequestId": "5F566C5B-E5B0-4020-A531-FC6F5005****", "HttpStatusCode": 200, "Success": true } |   |

##### 1.4.6.2 DescribeConsumerChannel

Queries the details of a consumer group, including the consumer group ID, consumer group name, username, and message latency.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeConsumerChannel | The operation that you want to perform. Set the value to DescribeConsumerChannel. |
| RegionId | String | Yes | cn-hangzhou | The region ID of the Data Transmission Service (DTS) change tracking instance. |
| DtsInstanceId | String | No | dtsboss6pn1w****** | The ID of the change tracking instance. You can call the DescribeDtsJobs operation to query the instance ID. Note You must specify at least one of the DtsInstanceId and DtsJobId parameters. |
| DtsJobId | String | No | boss6pn1w****** | The ID of the change tracking task. You can call the DescribeDtsJobs operation to query the task ID. Note You must specify at least one of the DtsInstanceId and DtsJobId parameters. |
| PageSize | Integer | No | 20 | The number of entries to return on each page. Valid values:1 to 100. Default value: 20. |
| PageNumber | Integer | No | 1 | The number of the page to return. The value must be an integer that is greater than 0. Default value: 1. |
| ParentChannelId | String | No | dtsan5114c522qg08c | The parent task ID of the distributed task. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| ConsumerChannels | Array of ConsumerChannel |   | Details of the consumer groups. |

| ConsumerGroupId | String | dtsor2y66j4219**** | The ID of the consumer group. |
|---|---|---|---|
| ConsumerGroupName | String | Consumer Group A | The name of the consumer group. |
| ConsumerGroupUserNam e | String | dtstest | The account of the consumer group. |
| ConsumptionCheckpoint | String | 2021-06-20T12:00:00Z | The consumption checkpoint, which is the time when the latest data record was consumed by the change tracking client. The time is displayed in the yyyy-MM-ddTHH:mm:ssZ format in UTC. |
| MessageDelay | Long | 1500 | The message latency, which is the timestamp of the latest data consumed by the downstream client minus the timestamp of the latest data tracked by the change tracking task. The value is a UNIX timestamp. Unit: seconds. For example, the latest data in the source database is generated at 10:00. The change tracking task reads the data generated at 09:55, and the downstream client consumes the data generated at 09:30. In this case, the message latency is the UNIX timestamp difference between 09:55 and 09:30. Note If the return value of this parameter is -1, no client is connected to the consumer group. |
| UnconsumedData | Long | 186600 | The total number of unconsumed messages, which is the number of unconsumed data records plus the number of heartbeat messages. Note If the return value of this parameter is -1, no client is connected to the consumer group. |
| ErrCode | String | InternalError | The error code returned if the call failed. |
| ErrMessage | String | The request processing has failed due to some unknown error. | The error message returned if the call failed. |
| HttpStatusCode | String | 200 | The HTTP status code. |
| PageNumber | Integer | 1 | The page number of the returned page. |
| PageRecordCount | Integer | 20 | The maximum number of consumer groups that can be displayed on one page. |
| RequestId | String | D66140B3-C747-42B6-8315- BAF6490E**** | The ID of the request. |
| Success | String | true | Indicates whether the call was successful. |
| TotalRecordCount | Long | 1 | The total number of consumer groups. |

**Examples**

Sample requests

```
http(s)://dts.aliyuncs.com/?Action=DescribeConsumerChannel &RegionId=cn-hangzhou &DtsInstanceId=dtsboss6pn1w******
```

Sample success responses

| XML | format |
|---|---|
| <DescribeConsumerChannelResponse> <TotalRecordCount>1</TotalRecordCount> <PageRecordCount>20</PageRecordCount> <RequestId>D66140B3-C747-42B6-8315-BAF6490E****</RequestId> <PageNumber>1</PageNumber> <HttpStatusCode>200</HttpStatusCode> <ConsumerChannels> <ConsumptionCheckpoint></ConsumptionCheckpoint> <ConsumerGroupId>dtsor2y66j4219****</ConsumerGroupId> <ConsumerGroupUserName>dtstest</ConsumerGroupUserName> <ConsumerGroupName>Consumer Group A</ConsumerGroupName> <MessageDelay>-1</MessageDelay> <UnconsumedData>-1</UnconsumedData> </ConsumerChannels> <Success>true</Success> </DescribeConsumerChannelResponse> |   |

```json
 "TotalRecordCount": 1,
 "PageRecordCount": 20,
 "RequestId": "D66140B3-C747-42B6-8315-BAF6490E****",
 "PageNumber": 1,
 "HttpStatusCode": 200,
 "ConsumerChannels": [
```

`{`

```json
   "ConsumptionCheckpoint": "",
   "ConsumerGroupId": "dtsor2y66j4219****",
   "ConsumerGroupUserName": "dtstest",
   &ConsumerGroupName=Consumer Group A
   "MessageDelay": -1,
   "UnconsumedData": -1
```

`}` `],`

```json
 "Success": true
```

`}`

##### 1.4.6.3 ModifyConsumerChannel

Modifies the information of a consumer group, including the consumer group name, username, and password.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyConsumerChannel | The operation that you want to perform. Set the value to ModifyConsumerChannel. |
| ConsumerGroupId | String | Yes | dtsor2y66j4219**** | The ID of the consumer group. You can call the DescribeConsumerChannel operation to query the consumer group ID. |
| RegionId | String | Yes | cn-hangzhou | The region ID of the Data Transmission Service (DTS) change tracking instance. |
| DtsInstanceId | String | No | dtsboss6pn1w73**** | The ID of the change tracking instance. You can call the DescribeDtsJobs operation to query the instance ID. Note You must specify at least one of the DtsInstanceId and DtsJobId parameters. |
| DtsJobId | String | No | boss6pn1w73**** | The ID of the change tracking task. You can call the DescribeDtsJobs operation to query the task ID. Note You must specify at least one of the DtsInstanceId and DtsJobId parameters. |
| ConsumerGroupPassword | String | No | Test123456 | The new password of the consumer group. The password must contain at least two of the following character types: uppercase letters, lowercase letters, digits, and special characters. The password must be 8 to 32 characters in length. |
| ConsumerGroupUserName | String | No | dtstest | The new username of the consumer group. The username can contain uppercase letters, lowercase letters, digits, and underscores (). _ The username must be 1 to 16 characters in length. |
| ConsumerGroupName | String | No | Consumer Group B | The name of the consumer group after modification. The name cannot exceed 128 characters in length. We recommend that you use a descriptive name that makes it easy to identify. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| ErrCode | String | InternalError | The error code returned if the call failed. |
| ErrMessage | String | The request processing has failed due to some unknown error. | The error message returned if the call failed. |
| HttpStatusCode | String | 200 | The HTTP status code. |
| RequestId | String | 055CAF9B-C15D-4799-BB9E- E62D417**** | The ID of the request. |

| Success | String | true | Indicates whether the call was successful. |
|---|---|---|---|

Sample requests

```
http(s)://dts.aliyuncs.com/?Action=ModifyConsumerChannel &ConsumerGroupId=dtsor2y66j4219**** &RegionId=cn-hangzhou &DtsInstanceId=dtsboss6pn1w73**** &ConsumerGroupName=Consumer Group B
```

Sample success responses

| XML | format |
|---|---|
| <ModifyConsumerChannelResponse> <RequestId>055CAF9B-C15D-4799-BB9E-E62D417****</RequestId> <HttpStatusCode>200</HttpStatusCode> <Success>true</Success> </ModifyConsumerChannelResponse> |   |

| JSON | format |
|---|---|
| { "RequestId": "055CAF9B-C15D-4799-BB9E-E62D417****", "HttpStatusCode": 200, "Success": true } |   |

##### 1.4.6.4 DeleteConsumerChannel

Deletes a consumer group from a change tracking task.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteConsumerChannel | The operation that you want to perform. Set the value to DeleteConsumerChannel. |
| ConsumerGroupId | String | Yes | dtsktbb6jdn2****** | The ID of the consumer group. |
| RegionId | String | Yes | cn-hangzhou | The region ID of the Data Transmission Service (DTS) change tracking instance. |
| DtsInstanceId | String | No | dtsboss6pn1w73**** | The ID of the change tracking instance. Note You must specify at least one of the DtsInstanceId and DtsJobId parameters. |
| DtsJobId | String | No | boss6pn1w73**** | The ID of the change tracking task. Note You must specify at least one of the DtsInstanceId and DtsJobId parameters. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| ErrCode | String | InternalError | The error code returned if the call failed. |
| ErrMessage | String | The request processing has failed due to some unknown error. | The error message returned if the call failed. |
| HttpStatusCode | String | 200 | The HTTP status code. |
| RequestId | String | F9E00ABE-2AD9-40A9-8C3C- D817E648**** | The ID of the request. |
| Success | String | true | Indicates whether the call was successful. |

**Examples**

```
http(s)://dts.aliyuncs.com/?Action=DeleteConsumerChannel &ConsumerGroupId=dtsktbb6jdn2****** &RegionId=cn-hangzhou &DtsInstanceId=dtsboss6pn1w73****
```

Sample success responses

| XML | format |
|---|---|
| <DeleteConsumerChannelResponse> <RequestId>F9E00ABE-2AD9-40A9-8C3C-D817E648****</RequestId> <HttpStatusCode>200</HttpStatusCode> <Success>true</Success> </DeleteConsumerChannelResponse> |   |

| JSON | format |
|---|---|
| { "RequestId": "F9E00ABE-2AD9-40A9-8C3C-D817E648****", "HttpStatusCode": 200, "Success": true } |   |

#### 1.4.7 SkipPreCheck

Skips or stops skipping one or more precheck items.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | SkipPreCheck | The operation that you want to perform. Set the value to SkipPreCheck. |
| JobId | String | Yes | b4my3zg929a**** | The ID of the precheck task. You can call the DescribePreCheckStatus operation to query the task ID. |
| SkipPreCheckItems | String | Yes | CHECKSAMEOBJ _ _ | The shortened name of the precheck item. Valid values: CHECKSAMEOBJ: object name conflict _ _ CHECKSAMEUSER: username conflict _ _ CHECKSRC: source database version _ CHECKTOPOLOGY: topology type _ CHECKSERVERID: server ID of the source database _ _ Note Separate multiple shortened names with commas (,). |
| SkipPreCheckNames | String | Yes | CHECKSAMEOBJDETAIL _ _ _ | The name of the precheck item. This parameter corresponds to the SkipPreCheckItems parameter. Valid values: CHECKSAMEOBJDETAIL: object name conflict _ _ _ CHECKSAMEUSERDETAIL: username conflict _ _ _ CHECKSRCDETAIL: source database version _ _ CHECKTOPOLOGYDETAIL: topology type _ _ CHECKSERVERIDDETAIL: the server ID of the source _ _ _ database Note Separate multiple item names with commas (,). |
| Skip | Boolean | No | true | Specifies whether to skip the precheck item. Valid values: true: skips the precheck item. false: does not skip the precheck item. Note This parameter is required. |
| DtsJobId | String | No | c7412z57g8k**** | The ID of the data migration, data synchronization, or change tracking task. |
| RegionId | String | No | cn-hangzhou | The region ID of the Data Transmission Service (DTS) instance. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Code | String | 200 | The error code. This parameter will be removed in the future. |

| DynamicMessage | String | JobId | The dynamic part in the error message. The value of this parameter is used to replace the %s variable in the value of the ErrMessage parameter. Note If the specified JobId parameter is invalid, The Value of Input Parameter %s is not valid is returned for ErrMessage and JobId is returned for DynamicMessage. |
|---|---|---|---|
| ErrCode | String | InternalError | The error code returned if the call failed. |
| ErrMessage | String | The Value of Input Parameter %s is not valid. | The error message returned if the call failed. |
| HttpStatusCode | Integer | 200 | The HTTP status code. |
| MigrationJobId | String | kyri3z9w29a**** | The ID of the DTS task on which the precheck is performed. |
| RequestId | String | 8C498360-7892-433C-847A- BA71A850**** | The ID of the request. |
| ScheduleJobId | String | b4my3zg929a**** | The ID of the precheck task. |
| SkipItems | String | CHECKSAMEOBJ _ _ | The shortened name of the precheck item. |
| SkipNames | String | CHECKSAMEOBJDETAIL _ _ _ | The name of the precheck item. |
| Success | Boolean | true | Indicates whether the call was successful. |

**Examples**

Sample requests

```
http(s)://dts.aliyuncs.com/?Action=SkipPreCheck &JobId= b4my3zg929a**** &SkipPreCheckItems=CHECK_SAME_OBJ &SkipPreCheckNames=CHECK_SAME_OBJ_DETAIL &<Common request parameters>
```

Sample success responses

| XML | format |
|---|---|
| <SkipPreCheckResponse> <RequestId>8C498360-7892-433C-847A-BA71A850****</RequestId> <HttpStatusCode>200</HttpStatusCode> <Success>true</Success> <MigrationJobId>kyri3z9w29a****</MigrationJobId> <ScheduleJobId> b4my3zg929a****</ScheduleJobId> <SkipItems>CHECK_SAME_OBJ</SkipItems> <SkipNames>CHECK_SAME_OBJ_DETAIL</SkipNames> </SkipPreCheckResponse> |   |

| JSON | format |
|---|---|
| { "RequestId": "8C498360-7892-433C-847A-BA71A850****", "HttpStatusCode": 200, "Success": true, "MigrationJobId": "kyri3z9w29a****", "ScheduleJobId": " b4my3zg929a****", "SkipItems": "CHECK_SAME_OBJ", "SkipNames": "CHECK_SAME_OBJ_DETAIL" } |   |

#### 1.4.8 Query DTS tasks

##### 1.4.8.1 DescribeDtsJobDetail

Queries the details of a data migration, data synchronization, or change tracking task.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeDtsJobDetail | The operation that you want to perform. Set the value to DescribeDtsJobDetail. |

| DtsJobId | String | Yes | ta7w132u12h**** | The ID of the data migration, data synchronization, or change tracking task. |
|---|---|---|---|---|
| DtsInstanceID | String | No | dtsta7w132u12h**** | The ID of the data migration, data synchronization, or change tracking instance. |
| SynchronizationDirection | String | No | Forward | The synchronization direction. Valid values: Forward: Data is synchronized from the source database to the destination database. Reverse: Data is synchronized from the destination database to the source database. Note The default value is Forward. The value Reverse takes effect only if the topology of the data synchronization instance is two-way synchronization. |
| RegionId | String | No | cn-hangzhou | The region ID of the Data Transmission Service (DTS) task. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| AppName | String | new | Indicates whether the new change tracking feature is used. Note This parameter is returned only for change tracking instances of the new version. |
| BeginTimestamp | String | 2021-03-15T08:25:34Z | The start of the time range for change tracking. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC. |
| Checkpoint | Long | 1616405159 | The start offset of incremental data migration or data synchronization. The value is a UNIX timestamp. Unit: seconds. |
| Code | Integer | 200 | The error code. This parameter will be removed in the future. |
| ConsumptionCheckpoint | String | 2021-03-23T07:30:31Z | The consumption checkpoint of the change tracking instance. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC. |
| ConsumptionClient | String | 114.***.***.**:dts******** | The downstream client information, in the following format: <IP address of the downstream client>:<Random ID generated by DTS>. |
| CreateTime | String | 2021-03-16T08:01:19Z | The point in time when the task was created. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC. |
| DatabaseCount | Integer | 2 | The number of ApsaraDB RDS for MySQL instances that are attached to the source PolarDB-X 1.0 instance. |
| DbObject | String | {\"dtstestdata\": {\"all\":true,\"name\":\"dtstestdat a\",\"state\":\"normal\"}} | The objects of the data migration, data synchronization, or change tracking task. |
| Delay | Long | 0 | The latency of incremental data migration or synchronization. Note For data migration tasks, the unit of this parameter is milliseconds. For data synchronization tasks, the unit of this parameter is seconds. |
| DestNetType | String | CLASSIC | The network type of the consumer client. Valid values: CLASSIC: the classic network VPC: Virtual Private Cloud (VPC) |
| DestinationEndpoint | Struct |   | The connection settings of the destination instance. |
| DatabaseName | String | dtstestdata | The name of the database that contains the migrated objects in the destination instance. |
| EngineName | String | MySQL | The database engine of the destination instance. |
| InstanceID | String | rm-bp1imrtn6fq7h**** | The ID of the destination instance. |

| InstanceType | String | RDS | The type of the destination instance. |
|---|---|---|---|
| Ip | String | 172.16.88.*** | The endpoint of the destination instance. |
| OracleSID | String | testsid | The system ID (SID) of the Oracle database. Note This parameter is returned only if the EngineName parameter of the destination instance is set to Oracle and the Oracle database is deployed in a non-RAC architecture. |
| Port | String | 3306 | The database service port of the destination instance. |
| Region | String | cn-hangzhou | The region ID of the destination instance. |
| SslSolutionEnum | String | DISABLE | Indicates whether SSL encryption is enabled. Valid values: DISABLE: SSL encryption is disabled. ENABLEWITHCERTIFICATE: SSL encryption is enabled, and the _ _ CA certificate is uploaded. ENABLEONLY4MONGODBALTAS: SSL encryption is enabled _ _ _ _ for the connection to an AWS MongoDB Altas database. ENABLEONLY4KAFKASCRAMSHA256: SCRAM-SHA-256 is _ _ _ _ _ _ used to encrypt the connection to a Kafka cluster. |
| UserName | String | dtstest | The database account of the destination instance. |
| DtsInstanceID | String | dtsi03e3zty16i**** | The ID of the data migration, data synchronization, or change tracking instance. |
| DtsJobClass | String | xlarge | The instance class. |
| DtsJobDirection | String | Forward | The synchronization direction. Valid values: Forward: Data is synchronized from the source database to the destination database. Reverse: Data is synchronized from the destination database to the source database. Note This parameter is returned only if the topology of the data synchronization instance is two-way synchronization. |
| DtsJobId | String | i03e3zty16i**** | The ID of the data migration, data synchronization, or change tracking task. |
| DtsJobName | String | API test | The name of the data migration, data synchronization, or change tracking task. |
| DynamicMessage | String | DtsJobId | The dynamic part in the error message. The value of this parameter is used to replace the %s variable in the value of the ErrMessage parameter. Note If the return value of the ErrMessage parameter is The Value of Input Parameter %s is not valid and the return value of the DynamicMessage parameter is DtsJobId, the specified DtsJobId parameter is invalid. |
| EndTimestamp | String | 2021-03-26T14:03:21Z | The end of the time range for change tracking. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC. |
| ErrCode | String | InternalError | The error code returned if the call failed. |
| ErrMessage | String | The Value of Input Parameter %s is not valid. | The error message returned if the call failed. |

| ErrorMessage | String | DTS-070211: Connect Source DB failed. cause by [com.mysql.jdbc.exceptions.jdbc 4.MySQLNonTransientConnection Exception:Could not create connection to database server. Attempted reconnect 3 times. Giving up.] [com.mysql.jdbc.exceptions.jdbc 4.CommunicationsException:Com munications link failure\n\nThe last packet sent successfully to the server was 0 milliseconds ago. The driver has not received any packets from the server.] [java.net.ConnectException:Conn ection timed out (Connection timed out)] About more information in [https://yq.aliyun.com/articles/49 9178]. | The error message returned if the task failed. |
|---|---|---|---|
| EtlCalculator | String | { "cells ": [{\"shape\":\"edge\",\"attrs\": {\"line\": {\"stroke\":\"#b1b1b1\",\"stroke Width\":1,\"targetMarker\": {\"name\":\"block\",\"args\": {\"size\":\"8\"}},\"strokeDasharra y\":\"\"}},\"id\":\"cd1ec473-f9b9- 4e9b-a742- ac23f44299e1\",\"source\": {\"cell\":\"8b261182-bfab-4803- ad8e- 6bb08e3e0a99\",\"port\":\"out1\" },\"target\":{\"cell\":\"b36770df- f48c-4d6b-9644- 54c5e9242987\",\"port\":\"in1\"}, \"zIndex\":7 }] } | The operator information of the extract, transform, and load (ETL) task. Note This parameter is returned only when you query the details of an ETL task. |
| ExpireTime | String | 2021-06-16T08:01:19Z | The point in time when the instance expires. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC. Note This parameter is returned only if the value of the PayType parameter is PrePaid. |
| FinishTime | String | 2021-03-16T10:34:17Z | The end time of the task. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC. |
| GroupId | String | i03e3zty16i**** | The ID of the DTS task. |
| HttpStatusCode | Integer | 200 | The HTTP status code. |
| MigrationMode | Struct |   | The migration types or synchronization types. |
| DataExtractTransformLoa d | Boolean | false | Indicates whether data transformation is performed. Valid values: true: yes false: no |
| DataInitialization | Boolean | true | Indicates whether full data migration or synchronization is performed. Valid values: true: yes false: no |
| DataSynchronization | Boolean | true | Indicates whether incremental data migration or synchronization is performed. Valid values: true: yes false: no |
| StructureInitialization | Boolean | true | Indicates whether schema migration or schema synchronization is performed. Valid values: true: yes false: no |
| PayType | String | PrePaid | The billing method of the DTS instance. Valid values: PrePaid: subscription PostPaid: pay-as-you-go |
| RequestId | String | 29207299-7C41-493A-BA4F- 2FAC5DE4**** | The ID of the request. |

| Reserved | String | {\"srcHostPorts\":\"\",\"whitelist.d ms.online.ddl.enable\":false,\"filte rDDL\":false,\"sqlparser.dms.origi nal.ddl\":true,\"srcOracleType\":\" sid\",\"maxRetryTime\":43200,\"d estSSL\":\"0\",\"destOracleType\": \"sid\",\"srcSSL\":\"0\",\"dbListCas eChangeMode\":\"default\",\"Sour ceEngineVersion\":\"8.0.18\",\"src NetType\":\"VPC\",\"destNetType\ ":\"VPC\",\"srcVpcNetMappingInst \":\"172.16.1**.**:10803\",\"destV pcNetMappingInst\":\"172.16.1**. **:11077\",\"useJobTask\":\"1\"} | The reserved parameter of DTS. The value is a JSON string. You can specify this parameter to meet specific requirements. For example, use this parameter to specify whether to automatically start a precheck. |
|---|---|---|---|
| SourceEndpoint | Struct |   | The connection settings of the source instance. |
| AliyunUid | String | 140692647406**** | The ID of the Alibaba Cloud account to which the source ApsaraDB RDS instance belongs. |
| DatabaseName | String | dtstestdata | The name of the database that contains the objects to be migrated from the source instance. |
| EngineName | String | MySQL | The database engine of the source instance. |
| InstanceID | String | rm-bp1162kryivb8**** | The ID of the source instance. |
| InstanceType | String | RDS | The type of the source instance. |
| Ip | String | 172.16.88.*** | The endpoint of the source instance. |
| OracleSID | String | testsid | The SID of the Oracle database. Note This parameter is returned only if the EngineName parameter of the source instance is set to Oracle and the Oracle database is deployed in a non-RAC architecture. |
| Port | String | 3306 | The database service port of the source instance. |
| Region | String | cn-hangzhou | The region ID of the source instance. |
| RoleName | String | ram-for-dts | The name of the Resource Access Management (RAM) role configured for the Alibaba Cloud account that owns the source instance. |
| SslSolutionEnum | String | DISABLE | Indicates whether SSL encryption is enabled. Valid values: DISABLE: SSL encryption is disabled. ENABLEWITHCERTIFICATE: SSL encryption is enabled, and the _ _ CA certificate is uploaded. ENABLEONLY4MONGODBALTAS: SSL encryption is enabled _ _ _ _ for the connection to an AWS MongoDB Altas database. ENABLEONLY4KAFKASCRAMSHA256: SCRAM-SHA-256 is _ _ _ _ _ _ used to encrypt the connection to a Kafka cluster. |
| UserName | String | dtstest | The database account of the source instance. |
| Status | String | Migrating | The state of the data migration or data synchronization task. Valid values for a data migration task: NotStarted: The task is not started. Migrating: The task is in progress. Failed: The task failed. Finished: The task is complete. Valid values for a data synchronization task: NotStarted: The task is not started. Prechecking: The task is being prechecked. PrecheckFailed: The task failed to pass the precheck. Initializing: The task is being initialized. InitializeFailed: Initial synchronization failed. Synchronizing: The task is in progress. Failed: The task failed. Suspending: The task is paused. Modifying: The objects in the task are being modified. Finished: The task is complete. |

| SubscribeTopic | String | cnhangzhourmbp1162kryivb8* _ _ _ ***dtstestversion2 _ _ | The topic of the change tracking instance. Note This parameter is returned only if your change tracking instances are of the new version and you have called the CreateConsumerGroup operation to create a consumer group. |   |   |
|---|---|---|---|---|---|
| SubscriptionDataType | Struct |   | The types of operations that are tracked by the task. |   |   |
| Ddl | Boolean | true | Indicates whether DDL statements are tracked. Valid values: true: yes false: no |   |   |
| Dml | Boolean | true | Indicates whether DML statements are tracked. Valid values: true: yes false: no |   |   |
| SubscriptionHost | Struct |   | The endpoint of the change tracking instance. |   |   |
| PrivateHost | String | dts-cn-****- internal.aliyuncs.com:18002 | The private endpoint of the change tracking instance in the <Address>:<Port number> format. |   |   |
| PublicHost | String | dts-cn-****.aliyuncs.com:18001 | The public endpoint of the change tracking instance in the <Address>:<Port number> format. |   |   |
| VpcHost | String | dts-cn-****- vpc.aliyuncs.com:18003 | The VPC endpoint of the change tracking instance in the <Address>: <Port number> format. |   |   |
|   |   |   |   | <Address>: |   |
| Success | Boolean | true | Indicates whether the call was successful. |   |   |
| SynchronizationDirection | String | Forward | The synchronization direction. Valid values: Forward: Data is synchronized from the source database to the destination database. Reverse: Data is synchronized from the destination database to the source database. |   |   |

|   | <Port number> |
|---|---|

**Examples**

Sample requests

```
http(s)://dts.aliyuncs.com/?Action=DescribeDtsJobDetail &DtsJobId=ta7w132u12h**** &<Common request parameters>
```

Sample success responses `XML` format

```json
<DescribeDtsJobDetailResponse>
      <DtsJobName>API test</DtsJobName>
      <DtsInstanceID>dtsi03e3zty16i****</DtsInstanceID>
      <Delay>0</Delay>
      <MigrationMode>
            <DataInitialization>true</DataInitialization>
            <DataSynchronization>true</DataSynchronization>
            <StructureInitialization>true</StructureInitialization>
      </MigrationMode>
      <DtsJobClass>xlarge</DtsJobClass>
      <DtsJobId>i03e3zty16i****</DtsJobId>
      <HttpStatusCode>200</HttpStatusCode>
      <Status>Migrating</Status>
      <RequestId>29207299-7C41-493A-BA4F-2FAC5DE4****</RequestId>
      <DbObject>{"dtstestdata":{"all":true,"name":"dtstestdata","state":"normal"}}</DbObject>
      <CreateTime>2021-03-16T08:01:19Z</CreateTime>
      <PayType>PostPaid</PayType>
      <Checkpoint>1616405159</Checkpoint>
      <DestinationEndpoint>
            <UserName>dtstest</UserName>
            <InstanceID>rm-bp1imrtn6fq7h****</InstanceID>
            <SslSolutionEnum>DISABLE</SslSolutionEnum>
            <Port>3306</Port>
            <DatabaseName>dtstestdata</DatabaseName>
            <Region>cn-hangzhou</Region>
            <InstanceType>RDS</InstanceType>
            <EngineName>MySQL</EngineName>
      </DestinationEndpoint>
      <SourceEndpoint>
            <RoleName></RoleName>
            <UserName>dtstest</UserName>
            <InstanceID>rm-bp1162kryivb8****</InstanceID>
            <SslSolutionEnum>DISABLE</SslSolutionEnum>
            <Port>3306</Port>
            <AliyunUid>140692647406****</AliyunUid>
            <Region>cn-hangzhou</Region>
            <InstanceType>RDS</InstanceType>
            <EngineName>MySQL</EngineName>
      </SourceEndpoint>
      <Reserved>
{"srcHostPorts":"","whitelist.dms.online.ddl.enable":false,"filterDDL":false,"sqlparser.dms.original.ddl":true,"srcOracleType":"sid","maxRetryTim 3200,"destSSL":"0","destOracleType":"sid","srcSSL":"0","dbListCaseChangeMode":"default","SourceEngineVersion":"8.0.18","srcNetType":"VPC","destNe e":"VPC","srcVpcNetMappingInst":"172.16.1**.**:1****","destVpcNetMappingInst":"172.16.1**.**:1****","useJobTask":"1"}</Reserved> </DescribeDtsJobDetailResponse>
```

`JSON` format

```json
 "DtsJobName": "API test",
 "DtsInstanceID": "dtsi03e3zty16i****",
 "Success": true,
 "Delay": 0,
 "MigrationMode": {
  "DataInitialization": true,
  "DataSynchronization": true,
  "StructureInitialization": true
```

`},`

```json
 "DtsJobClass": "xlarge",
 "DtsJobId": "i03e3zty16i****",
 "HttpStatusCode": 200,
 "Status": "Migrating",
 "RequestId": "29207299-7C41-493A-BA4F-2FAC5DE4****",
 "DbObject": "{\"dtstestdata\":{\"all\":true,\"name\":\"dtstestdata\",\"state\":\"normal\"}}",
 "CreateTime": "2021-03-16T08:01:19Z",
 "PayType": "PostPaid",
 "Checkpoint": "1616405159",
 "DestinationEndpoint": {
  "UserName": "dtstest",
  "InstanceID": "rm-bp1imrtn6fq7h****",
  "SslSolutionEnum": "DISABLE",
  "Port": "3306",
  "DatabaseName": "dtstestdata",
  "Region": "cn-hangzhou",
  "InstanceType": "RDS",
  "EngineName": "MySQL"
```

`},`

```json
 "SourceEndpoint": {
  "RoleName": "",
  "UserName": "dtstest",
  "InstanceID": "rm-bp1162kryivb8****",
  "SslSolutionEnum": "DISABLE",
  "Port": "3306",
  "AliyunUid": "140692647406****",
  "Region": "cn-hangzhou",
  "InstanceType": "RDS",
  "EngineName": "MySQL"
```

`},`

```json
 "Reserved": "
{\"srcHostPorts\":\"\",\"whitelist.dms.online.ddl.enable\":false,\"filterDDL\":false,\"sqlparser.dms.original.ddl\":true,\"srcOracleType\":\"sid\ maxRetryTime\":43200,\"destSSL\":\"0\",\"destOracleType\":\"sid\",\"srcSSL\":\"0\",\"dbListCaseChangeMode\":\"default\",\"SourceEngineVersion\":\ .18\",\"srcNetType\":\"VPC\",\"destNetType\":\"VPC\",\"srcVpcNetMappingInst\":\"172.16.1**.**:1****\",\"destVpcNetMappingInst\":\"172.16.1**.**:1 \",\"useJobTask\":\"1\"}"
```

`}`

##### 1.4.8.2 DescribeDtsJobs

Queries the list of Data Transmission Service (DTS) tasks and the details of each task.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeDtsJobs | The operation that you want to perform. Set the value to DescribeDtsJobs. |
| Region | String | Yes | cn-hangzhou | The region where the DTS instance resides. |
| Type | String | No | instance | The query condition for the required tasks. Valid values: instance: queries by DTS instance ID. name: queries by DTS instance name. Fuzzy match is supported. srcRds: queries by ApsaraDB RDS instance ID. The ApsaraDB RDS instance is the source instance of a DTS task. rds: queries by ApsaraDB RDS instance ID. The ApsaraDB RDS instance is the destination instance of a DTS task. Note You must set the Params parameter to specify the query condition. |
| Params | String | No | dtspk3f13r731m**** | The content of the query condition. Note You must set the Type parameter to specify the query condition. |

| Status | String | No | Migrating | The state of the DTS task. Valid values for a data migration task: NotStarted: The task is not started. Prechecking: The task is in precheck. PrecheckFailed: The task failed to pass the precheck. PreCheckPass: The task passed the precheck. NotConfigured: The task is not configured. Migrating: The task is in progress. Suspending: The task is paused. MigrationFailed: The task failed. Finished: The task is complete. Retrying: The task is being retried. Upgrade: The task is being upgraded. Locked: The task is locked. Downgrade: The task is being downgraded. Valid values for a data synchronization task: NotStarted: The task is not started. Prechecking: The task is in precheck. PrecheckFailed: The task failed to pass the precheck. PreCheckPass: The task passed the precheck. NotConfigured: The task is not configured. Initializing: The task is being initialized. InitializeFailed: Initial synchronization failed. Synchronizing: The task is in progress. Failed: The task failed. Suspending: The task is paused. Modifying: The objects in the task are being modified. Finished: The task is complete. Retrying: The task is being retried. Upgrade: The task is being upgraded. Locked: The task is locked. Downgrade: The task is being downgraded. Valid values for a change tracking task: NotConfigured: The task is not configured. NotStarted: The task is not started. Prechecking: The task is in precheck. PrecheckFailed: The task failed to pass the precheck. PreCheckPass: The task passed the precheck. Starting: The task is being started. Normal: The task is running as expected. Retrying: The task is being retried. Abnormal: An exception occurred on the task. Upgrade: The task is being upgraded. Locked: The task is locked. Downgrade: The task is being downgraded. |
|---|---|---|---|---|
| OrderDirection | String | No | ASC | The order in which the returned DTS tasks are sorted. Default value: ASC. Valid values: ASC: sorts the DTS tasks in ascending order. DESC: sorts the DTS tasks in descending order. |
| OrderColumn | String | No | CreateTime | The basis on which the returned DTS tasks are sorted. Valid values: CreateTime: sorts the DTS tasks based on the points in time when they are created. FinishTime: sorts the DTS tasks based on the points in time when they are complete. Note You can also set the OrderDirection parameter to specify whether to sort the DTS tasks in ascending or descending order. |
| Tags | String | No | [ { \"key\": \"testK\", \"value\": \"testV\" } ] | The tags of the DTS task to be queried. Specify tags in the JSON format. Note You can call the ListTagResources operation to query the tag key and tag value. |
| PageSize | Integer | No | 30 | The number of entries to return on each page. Valid values: 30, 50, and 100. Default value: 30. |
| PageNumber | Integer | No | 1 | The number of the page to return. The value must be an integer that is greater than 0. Default value: 1. |

| JobType | String | No | MIGRATION | The type of the DTS task. Default value: MIGRATION. Valid values: MIGRATION: data migration SYNC: data synchronization SUBSCRIBE: change tracking |
|---|---|---|---|---|
| RegionId | String | No | cn-hangzhou | The region where the DTS instance resides. |
| GroupId | String | No | pk13r731m**** | The ID of the DTS task. Note In most cases, you do not need to specify this parameter. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| DtsJobList | Array of DtsJobStatus |   | The list of DTS tasks and the details of each task. |
| AppName | String | new | Indicates whether the new change tracking feature is used. Note This parameter is returned only for change tracking instances of the new version. |
| BeginTimestamp | String | 2021-03-15T08:25:34Z | The beginning of the time range for change tracking. The time is displayed in the yyyy-MM-ddTHH:mm:ssZ format in UTC. |
| Checkpoint | String | 1616899019 | The start offset of incremental data migration or data synchronization. The value is a UNIX timestamp. Unit: seconds. |
| ConsumptionCheckpoint | String | 2021-03-23T07:30:31Z | The consumption checkpoint of the change tracking instance. The time is displayed in the yyyy-MM-ddTHH:mm:ssZ format in UTC. |
| ConsumptionClient | String | 114...:dts****** | The downstream client information, in the following format: <IP address of the downstream client>:<Random ID generated by DTS>. |
| CreateTime | String | 2021-03-16T08:01:19Z | The point in time when the task was created. The time is displayed in the yyyy-MM-ddTHH:mm:ssZ format in UTC. |
| DataEtlStatus | Struct |   | The state of the extract, transform, and load (ETL) task. Valid values: Note This parameter is returned only if an ETL task is configured. |
| ErrorMessage | String | The task has failed for a long time and cannot be recovered. | The error message returned if the task failed. |
| Percent | String | 95 | The progress of the ETL task. |
| Progress | String | 0/0 | The number of entries that have been processed by the ETL task. |
| Status | String | Finished | The state of the ETL task. Valid values: NotStarted: The task is not started. Migrating: The task is in progress. Failed: The task failed. Finished: The task is complete. Catched: No latency occurred on the task. |
| DataInitializationStatus | Struct |   | The state of full data migration or synchronization. |
| ErrorMessage | String | java.lang.NumberFormatExceptio n: For input string: "" | The error message returned if full data migration or synchronization failed. |
| Percent | String | 100 | The progress of full data migration or synchronization. Unit: %. |
| Progress | String | 44755 | The number of entries that have been migrated during full data migration or synchronization. |

| Status | String | Finished | The state of full data migration or synchronization. Valid values: NotStarted: The task is not started. Migrating: The task is in progress. Failed: The task failed. Finished: The task is complete. |
|---|---|---|---|
| DataSynchronizationStatu s | Struct |   | The state of incremental data migration or synchronization. |
| ErrorMessage | String | The task has failed for a long time and cannot be recovered. | The error message returned if incremental data migration or synchronization failed. |
| NeedUpgrade | Boolean | true | Indicates whether the instance needs to be upgraded. Valid values: true: yes false: no Note To upgrade a DTS instance, call the TransferInstanceClass operation. |
| Percent | String | 95 | The progress of incremental data migration or synchronization. |
| Progress | String | 0/0 | The number of entries that have been migrated or synchronized during incremental data migration or synchronization. |
| Status | String | Catched | The state of incremental data migration or synchronization. Valid values: NotStarted: The task is not started. Migrating: The task is in progress. Failed: The task failed. Finished: The task is complete. Catched: No latency occurred on the task. |
| DbObject | String | {"dtstestdata": { "name": "dtstestdata", "all": true }} | The objects of the data migration, data synchronization, or change tracking task. |
| Delay | Long | 0 | The latency of incremental data migration or synchronization. Note For data migration tasks, the unit of this parameter is milliseconds. For data synchronization tasks, the unit of this parameter is seconds. |
| DestinationEndpoint | Struct |   | The connection settings of the destination instance. |
| DatabaseName | String | dtstestdata | The name of the database that contains the migrated objects in the destination instance. |
| EngineName | String | MySQL | The database engine of the destination instance. |
| InstanceID | String | rm-bp1imrtn6fq7h**** | The ID of the destination instance. |
| InstanceType | String | RDS | The type of the destination instance. |
| Ip | String | 172.16.88.*** | The endpoint of the destination instance. |
| OracleSID | String | testsid | The system ID (SID) of the Oracle database. Note This parameter is returned only if the EngineName parameter of the destination instance is set to Oracle and the Oracle database is deployed in a non-RAC architecture. |
| Port | String | 3306 | The database service port of the destination instance. |
| Region | String | cn-hangzhou | The region where the destination instance resides. |
| SslSolutionEnum | String | DISABLE | Indicates whether SSL encryption is enabled. Valid values: DISABLE: SSL encryption is disabled. ENABLEWITHCERTIFICATE: SSL encryption is enabled, and the _ _ CA certificate is uploaded. ENABLEONLY4MONGODBALTAS: SSL encryption is enabled _ _ _ _ for the connection to an AWS MongoDB Altas database. ENABLEONLY4KAFKASCRAMSHA256: SCRAM-SHA-256 is _ _ _ _ _ _ used to encrypt the connection to a Kafka cluster. |

| UserName | String | dtstest | The database account of the destination instance. |
|---|---|---|---|
| DtsInstanceID | String | dtsi03e3zty16i**** | The ID of the data migration, data synchronization, or change tracking instance. |
| DtsJobClass | String | large | The instance class. |
| DtsJobDirection | String | Forward | The synchronization direction. Valid values: Forward: Data is synchronized from the source database to the destination database. Reverse: Data is synchronized form the destination database to the source database. Note This parameter is returned only if the topology of the data synchronization instance is two-way synchronization. |
| DtsJobId | String | i03e3zty16i**** | The ID of the data migration, data synchronization, or change tracking task. |
| DtsJobName | String | RDSTORDSMIGRATION _ _ _ | The name of the data migration, data synchronization, or change tracking task. |
| EndTimestamp | String | 2021-03-26T14:03:21Z | The end of the time range for change tracking. The time is displayed in the yyyy-MM-ddTHH:mm:ssZ format in UTC. |
| ErrorMessage | String | DTS-070211: Connect Source DB failed. cause by [com.mysql.jdbc.exceptions.jdbc 4.MySQLNonTransientConnection Exception:Could not create connection to database server. Attempted reconnect 3 times. Giving up.] [com.mysql.jdbc.exceptions.jdbc 4.CommunicationsException:Com munications link failure\n\nThe last packet sent successfully to the server was 0 milliseconds ago. The driver has not received any packets from the server.] [java.net.ConnectException:Conn ection timed out (Connection timed out)] About more information in [https://yq.aliyun.com/articles/49 9178]. | The error message returned if the task failed. |
| ExpireTime | String | 2022-03-16T08:01:19Z | The point in time when the instance expires. The time is displayed in the yyyy-MM-ddTHH:mm:ssZ format in UTC. Note This parameter is returned only if the return value of the PayType parameter is PrePaid. |
| MigrationMode | Struct |   | The migration types or synchronization types. |
| DataInitialization | Boolean | true | Indicates whether full data migration or synchronization is performed. Valid values: true: yes false: no |
| DataSynchronization | Boolean | true | Indicates whether incremental data migration or synchronization is performed. Valid values: true: yes false: no |
| StructureInitialization | Boolean | true | Indicates whether schema migration or schema synchronization is performed. Valid values: true: yes false: no |
| OriginType | String | DTS | The source of the task. Valid values: PTS DMS DTS |
| PayType | String | PrePaid | The billing method of the DTS instance. Valid values: PrePaid: subscription PostPaid: pay-as-you-go |

| Performance | Struct |   | The performance information of the data migration or synchronization instance. |
|---|---|---|---|
| Flow | String | 1 | The size of data that is migrated or synchronized per second. Unit: MB/s. |
| Rps | String | 100 | The number of times SQL statements are migrated or synchronized per second, including BEGIN, COMMIT, DML, and DDL statements. DML statements include INSERT, DELETE, and UPDATE. |
| PrecheckStatus | Struct |   | The precheck state. |
| Detail | Array of PrecheckDetail |   | The result of each precheck item. |
| CheckItem | String | CHECKCONNSRC _ _ | The name of the precheck item. |
| CheckItemDescription | String | CHECKCONNSRCDETAIL _ _ _ | The description of the precheck item. |
| CheckResult | String | Success | The precheck result. Valid values: Success: The task passed the precheck. Failed: The task failed to pass the precheck. |
| FailedReason | String | Original error: Access denied for user 'dtstest'@'100.104.***.**' (using password: YES) | The error message returned if the task failed to pass the precheck. Note This parameter is returned only if the return value of the CheckResult parameter is Failed. |
| RepairMethod | String | CHECKERRORDESTCONNREP _ _ _ _ AIR2 | The method to fix the precheck failure. Note This parameter is returned only if the return value of the CheckResult parameter is Failed. |
| ErrorMessage | String | CHECK ERRORSAMEOBJ. __ _ _ | The cause of the precheck failure. |
| Percent | String | 100 | The precheck progress. Unit: %. |
| Status | String | Finished | The precheck result. Valid values: Success: The task passed the precheck. Failed: The task failed to pass the precheck. |
| Reserved | String | {\"srcHostPorts\":\"\",\"whitelist.d ms.online.ddl.enable\":false,\"filte rDDL\":false,\"sqlparser.dms.origi nal.ddl\":true,\"srcOracleType\":\" sid\",\"maxRetryTime\":43200,\"d estSSL\":\"0\",\"destOracleType\": \"sid\",\"srcSSL\":\"0\",\"dbListCas eChangeMode\":\"default\",\"Sour ceEngineVersion\":\"8.0.18\",\"src NetType\":\"VPC\",\"destNetType\ ":\"VPC\",\"srcVpcNetMappingInst \":\"172.16.1**.**:10803\",\"destV pcNetMappingInst\":\"172.16.1**. **:11077\",\"useJobTask\":\"1\"} | The reserved parameter of DTS. The value is a JSON string. You can specify this parameter to meet specific requirements. For example, use this parameter to specify whether to automatically start a precheck. |
| RetryState | Struct |   | The information about retries performed by DTS due to an exception. |
| ErrMessage | String | Unexpected error | The error message returned if these retries failed. |
| MaxRetryTime | Integer | 7200 | The maximum duration of a retry. Unit: seconds. |
| RetryCount | Integer | 5 | The number of retries. |
| RetryTarget | String | srcDB | The object on which these retries are performed. Valid values: srcDB: the source database destDB: the destination database innermodule: an internal module of DTS _ |
| RetryTime | Integer | 3600 | The time that has elapsed from the point in time when the first retry starts. Unit: seconds. |

| ReverseJob | Struct |   | The details of the data synchronization task in the reverse direction. Note This parameter is returned only for two-way data synchronization tasks. |
|---|---|---|---|
| Checkpoint | String | 1616980369 | The start offset of incremental data synchronization. The value is a UNIX timestamp. Unit: seconds. |
| CreateTime | String | 2021-03-16T08:01:19Z | The point in time when the task was created. The time is displayed in the yyyy-MM-ddTHH:mm:ssZ format in UTC. |
| DataInitializationStatus | Struct |   | The state of full data synchronization. |
| ErrorMessage | String | java.lang.NumberFormatExceptio n: For input string: "" | The error message returned if full data synchronization failed. |
| Percent | String | 100 | The progress of full data synchronization. Unit: %. |
| Progress | String | 43071 | The number of entries that have been synchronized during full data synchronization. |
| Status | String | Finished | The state of full data synchronization. Valid values: NotStarted: The task is not started. Migrating: The task is in progress. Failed: The task failed. Finished: The task is complete. |
| DataSynchronizationStatu s | Struct |   | The state of incremental data synchronization. |
| ErrorMessage | String | The task has failed for a long time and cannot be recovered. | The error message returned if incremental data synchronization failed. |
| NeedUpgrade | Boolean | true | Indicates whether the instance needs to be upgraded. Valid values: true: yes false: no Note To upgrade a DTS instance, call the TransferInstanceClass operation. |
| Percent | String | 100 | The progress of incremental data synchronization. Unit: %. |
| Progress | String | 20001 | The number of entries that have been migrated or synchronized during incremental data migration or synchronization. |
| Status | String | Migrating | The state of incremental data synchronization. |
| DbObject | String | {"dtstestdata": { "name": "dtstestdata", "all": true }} | The objects that you want to synchronize. The value is a JSON string and can contain regular expressions. For more information, see the Objects of DTS tasks topic. |
| Delay | Long | 0 | The latency of incremental data synchronization. Unit: seconds. |
| DestinationEndpoint | Struct |   | The connection settings of the destination instance. |
| DatabaseName | String | dtstestdata | The name of the database that contains the synchronized objects in the destination instance. |
| EngineName | String | MySQL | The database engine of the destination instance. |
| InstanceID | String | rm-bp1162kryivb8**** | The ID of the destination instance. |
| InstanceType | String | RDS | The type of the destination instance. |
| Ip | String | 172.16.88.*** | The endpoint of the destination instance. |
| OracleSID | String | testsid | The SID of the Oracle database. Note This parameter is returned only if the EngineName parameter of the destination instance is set to Oracle and the Oracle database is deployed in a non-RAC architecture. |

| Port | String | 3306 | The database service port of the destination instance. |
|---|---|---|---|
| Region | String | cn-hangzhou | The region where the destination instance resides. |
| SslSolutionEnum | String | DISABLE | Indicates whether SSL encryption is enabled. Valid values: DISABLE: SSL encryption is disabled. ENABLEWITHCERTIFICATE: SSL encryption is enabled, and the _ _ CA certificate is uploaded. ENABLEONLY4MONGODBALTAS: SSL encryption is enabled _ _ _ _ for the connection to an AWS MongoDB Altas database. ENABLEONLY4KAFKASCRAMSHA256: SCRAM-SHA-256 is _ _ _ _ _ _ used to encrypt the connection to a Kafka cluster. |
| UserName | String | dtstest | The database account of the destination instance. |
| DtsInstanceID | String | dtsi03e3zty16i**** | The ID of the data synchronization instance. |
| DtsJobClass | String | large | The instance class. |
| DtsJobDirection | String | Reverse | The synchronization direction. Reverse is returned. |
| DtsJobId | String | i03e3zty16i**** | The ID of the data synchronization task. |
| DtsJobName | String | RDSTORDSMIGRATION _ _ _ | The name of the data synchronization task. |
| ErrorMessage | String | DTS-070211: Connect Source DB failed. cause by [com.mysql.jdbc.exceptions.jdbc 4.MySQLNonTransientConnection Exception:Could not create connection to database server. Attempted reconnect 3 times. Giving up.] [com.mysql.jdbc.exceptions.jdbc 4.CommunicationsException:Com munications link failure\n\nThe last packet sent successfully to the server was 0 milliseconds ago. The driver has not received any packets from the server.] [java.net.ConnectException:Conn ection timed out (Connection timed out)] About more information in [https://yq.aliyun.com/articles/49 9178]. | The error message returned if the task failed. |
| ExpireTime | String | 2022-03-16T08:01:19Z | The point in time when the instance expires. The time is displayed in the yyyy-MM-ddTHH:mm:ssZ format in UTC. Note This parameter is returned only if the return value of the PayType parameter is PrePaid. |
| MigrationMode | Struct |   | The synchronization types. |
| DataInitialization | Boolean | true | Indicates whether full data synchronization is performed. Valid values: true: yes false: no |
| DataSynchronization | Boolean | true | Indicates whether incremental data synchronization is performed. Valid values: true: yes false: no |
| StructureInitialization | Boolean | true | Indicates whether schema synchronization is performed. Valid values: true: yes false: no |
| PayType | String | PostPaid | The billing method of the DTS instance. Valid values: PrePaid: subscription PostPaid: pay-as-you-go |
| Performance | Struct |   | The performance information of the data synchronization instance. |
| Flow | String | 1 | The size of data that is synchronized per second. Unit: MB/s. |

| Rps | String | 100 | The number of times SQL statements are synchronized per second, including BEGIN, COMMIT, DML, and DDL statements. DML statements include INSERT, DELETE, and UPDATE. |
|---|---|---|---|
| PrecheckStatus | Struct |   | The precheck state. |
| Detail | Array of PrecheckDetail |   | The result of each precheck item. |
| CheckItem | String | CHECKCONNSRC _ _ | The name of the precheck item. |
| CheckItemDescription | String | CHECKCONNSRCDETAIL _ _ _ | The description of the precheck item. |
| CheckResult | String | Success | The precheck result. Valid values: Success: The task passed the precheck. Failed: The task failed to pass the precheck. |
| FailedReason | String | Original error: Access denied for user 'dtstest'@'100.104.***.**' (using password: YES) | The error message returned if the task failed to pass the precheck. |
| RepairMethod | String | CHECKERRORDESTCONNREP _ _ _ _ AIR2 | The method to fix the precheck failure. |
| ErrorMessage | String | CHECK ERRORSAMEOBJ. __ _ _ | The cause of the precheck failure. |
| Percent | String | 100 | The precheck progress. Unit: %. |
| Status | String | Finished | The precheck result. Valid values: Success: The task passed the precheck. Failed: The task failed to pass the precheck. |
| Reserved | String | {\"srcHostPorts\":\"\",\"whitelist.d ms.online.ddl.enable\":false,\"filte rDDL\":false,\"sqlparser.dms.origi nal.ddl\":true,\"srcOracleType\":\" sid\",\"maxRetryTime\":43200,\"d estSSL\":\"0\",\"destOracleType\": \"sid\",\"srcSSL\":\"0\",\"dbListCas eChangeMode\":\"default\",\"Sour ceEngineVersion\":\"8.0.18\",\"src NetType\":\"VPC\",\"destNetType\ ":\"VPC\",\"srcVpcNetMappingInst \":\"172.16.1**.**:10803\",\"destV pcNetMappingInst\":\"172.16.1**. **:11077\",\"useJobTask\":\"1\"} | The reserved parameter of DTS. The value is a JSON string. You can specify this parameter to meet specific requirements. For example, use this parameter to specify whether to automatically start a precheck. |
| SourceEndpoint | Struct |   | The connection settings of the source instance. |
| DatabaseName | String | dtstestdata | The name of the database that contains the objects to be migrated from the source instance. |
| EngineName | String | MySQL | The database engine of the source instance. |
| InstanceID | String | rm-bp1imrtn6fq7h**** | The ID of the source instance. |
| InstanceType | String | RDS | The type of the source instance. |
| Ip | String | 172.16.88.*** | The endpoint of the source instance. |
| OracleSID | String | testsid | The SID of the Oracle database. Note This parameter is returned only if the EngineName parameter of the source instance is set to Oracle and the Oracle database is deployed in a non-RAC architecture. |
| Port | String | 3306 | The database service port of the source instance. |
| Region | String | cn-hangzhou | The region where the source instance resides. |

| SslSolutionEnum | String | DISABLE | Indicates whether SSL encryption is enabled. Valid values: DISABLE: SSL encryption is disabled. ENABLEWITHCERTIFICATE: SSL encryption is enabled, and the _ _ CA certificate is uploaded. ENABLEONLY4MONGODBALTAS: SSL encryption is enabled _ _ _ _ for the connection to an AWS MongoDB Altas database. ENABLEONLY4KAFKASCRAMSHA256: SCRAM-SHA-256 is _ _ _ _ _ _ used to encrypt the connection to a Kafka cluster. |
|---|---|---|---|
| UserName | String | dtstest | The database account of the source instance. |
| Status | String | Synchronizing | The state of the DTS instance. For more information about the valid values, see the description of the request parameter Status. |
| StructureInitializationStat us | Struct |   | The state of schema synchronization. |
| ErrorMessage | String | DTS-1020042 Execute sql error sql: ERROR: type "geometry" does not exist; | The error message returned if schema synchronization failed. |
| Percent | String | 100 | The progress of schema synchronization. Unit: %. |
| Progress | String | 1 | The number of tables whose schemas have been synchronized to the destination instance. |
| Status | String | Finished | The state of schema synchronization. Valid values: NotStarted: The task is not started. Migrating: The task is in progress. Failed: The task failed. Finished: The task is complete. |
| SourceEndpoint | Struct |   | The connection settings of the source instance. |
| DatabaseName | String | dtstestdata | The name of the database that contains the objects to be migrated from the source instance. |
| EngineName | String | MySQL | The database engine of the source instance. |
| InstanceID | String | rm-bp1162kryivb8**** | The ID of the source instance. |
| InstanceType | String | RDS | The type of the source instance. |
| Ip | String | 172.16.88.*** | The endpoint of the source instance. |
| OracleSID | String | testsid | The SID of the Oracle database. Note This parameter is returned only if the EngineName parameter of the source instance is set to Oracle and the Oracle database is deployed in a non-RAC architecture. |
| Port | String | 3306 | The database service port of the source instance. |
| Region | String | cn-hangzhou | The region where the source instance resides. |
| SslSolutionEnum | String | DISABLE | Indicates whether SSL encryption is enabled. Valid values: DISABLE: SSL encryption is disabled. ENABLEWITHCERTIFICATE: SSL encryption is enabled, and the _ _ CA certificate is uploaded. ENABLEONLY4MONGODBALTAS: SSL encryption is enabled _ _ _ _ for the connection to an AWS MongoDB Altas database. ENABLEONLY4KAFKASCRAMSHA256: SCRAM-SHA-256 is _ _ _ _ _ _ used to encrypt the connection to a Kafka cluster. |
| UserName | String | dtstest | The database account of the source instance. |
| Status | String | Migrating | The state of the DTS instance. For more information about the valid values, see the description of the request parameter Status. |
| StructureInitializationStat us | Struct |   | The state of schema migration or schema synchronization. |

| ErrorMessage | String | DTS-1020042 Execute sql error sql: ERROR: type "geometry" does not exist; | The error message returned if schema migration or schema synchronization failed. |
|---|---|---|---|
| Percent | String | 100 | The progress of schema migration or schema synchronization. Unit: %. |
| Progress | String | 1 | The number of tables whose schemas have been migrated or synchronized to the destination instance. |
| Status | String | Finished | The state of schema migration or schema synchronization. Valid values: NotStarted: The task is not started. Migrating: The task is in progress. Failed: The task failed. Finished: The task is complete. |
| TagList | Array of DtsTag |   | Details of the tags. |
| TagKey | String | testkey | The key of the value. |
| TagValue | String | testvalue | The value of the tag. |
| DynamicCode | String | 403 | The dynamic error code. This parameter will be removed in the future. |
| DynamicMessage | String | Type | The dynamic part in the error message. The value of this parameter is used to replace the %s variable in the value of the ErrMessage parameter. Note If the return value of the ErrMessage parameter is The Value of Input Parameter %s is not valid and the return value of the DynamicMessage parameter is Type, the specified Type parameter is invalid. |
| ErrCode | String | InternalError | The error code returned if the call failed. |
| ErrMessage | String | The Value of Input Parameter %s is not valid. | The error message returned if the call failed. |
| HttpStatusCode | Integer | 200 | The HTTP status code. |
| JobType | String | MIGRATION | The type of the DTS task. Valid values: MIGRATION: data migration SYNC: data synchronization SUBSCRIBE: change tracking |
| PageNumber | Integer | 2 | The page number of the returned page. |
| PageRecordCount | Integer | 20 | The maximum number of entries that can be displayed on the current page. |
| RequestId | String | 621BB4F8-3016-4FAA-8D5A- 5D3163CC**** | The ID of the request. |
| Success | Boolean | true | Indicates whether the call was successful. |
| TotalRecordCount | Integer | 15 | The total number of DTS tasks that meet the query conditions. |

**Examples**

Sample requests

```
http(s)://dts.aliyuncs.com/?Action=DescribeDtsJobs &Region=cn-hangzhou &<Common request parameters>
```

Sample success responses

| XML | format |
|---|---|
| <DescribeDtsJobsResponse> <TotalRecordCount>15</TotalRecordCount> <PageRecordCount>1</PageRecordCount> <DtsJobList> <Status>Migrating</Status> <DataInitializationStatus> <Status>Finished</Status> <Progress>44755</Progress> |   |

```xml
                  <Percent>100</Percent>
            </DataInitializationStatus>
            <DbObject>{"DTSTEST":{"name":"dtstest","all":true,"state":"normal","edit":false}}</DbObject>
            <CreateTime>2021-03-16T08:01:19Z</CreateTime>
            <DtsJobName>RDS_TO_RDS_MIGRATION</DtsJobName>
            <ReverseJob>
                  <PrecheckStatus></PrecheckStatus>
                  <DataInitializationStatus></DataInitializationStatus>
                  <DestinationEndpoint></DestinationEndpoint>
                  <SourceEndpoint></SourceEndpoint>
                  <Performance></Performance>
                  <MigrationMode></MigrationMode>
                  <StructureInitializationStatus></StructureInitializationStatus>
                  <DataSynchronizationStatus></DataSynchronizationStatus>
            </ReverseJob>
            <PayType>PrePaid</PayType>
            <DtsInstanceID>dtsi03e3zty16i****</DtsInstanceID>
            <Delay>0</Delay>
            <MigrationMode>
                  <DataInitialization>true</DataInitialization>
                  <DataSynchronization>true</DataSynchronization>
                  <StructureInitialization>true</StructureInitialization>
            </MigrationMode>
            <PrecheckStatus>
                  <Status>Finished</Status>
                  <Percent>100</Percent>
                  <Detail>
                        <CheckItem>CHECK_CONN_SRC</CheckItem>
                        <CheckResult>Success</CheckResult>
                        <CheckItemDescription>CHECK_CONN_SRC_DETAIL</CheckItemDescription>
                  </Detail>
                  <Detail>
                        <CheckItem>CHECK_CONN_DEST</CheckItem>
                        <CheckResult>Success</CheckResult>
                        <CheckItemDescription>CHECK_CONN_DEST_DETAIL</CheckItemDescription>
                  </Detail>
                  <Detail>
                        <CheckItem>CHECK_AUTH_SRC</CheckItem>
                        <CheckResult>Success</CheckResult>
                        <CheckItemDescription>CHECK_AUTH_SRC_DETAIL</CheckItemDescription>
                  </Detail>
                  <Detail>
                        <CheckItem>CHECK_AUTH_DEST</CheckItem>
                        <CheckResult>Success</CheckResult>
                        <CheckItemDescription>CHECK_AUTH_DEST_DETAIL</CheckItemDescription>
                  </Detail>
                  <Detail>
                        <CheckItem>CHECK_BINLOG_ON</CheckItem>
                        <CheckResult>Success</CheckResult>
                        <CheckItemDescription>CHECK_BINLOG_ON_DETAIL</CheckItemDescription>
                  </Detail>
                  <Detail>
                        <CheckItem>CHECK_BINLOG_MODE</CheckItem>
                        <CheckResult>Success</CheckResult>
                        <CheckItemDescription>CHECK_BINLOG_MODE_DETAIL</CheckItemDescription>
                  </Detail>
                  <Detail>
                        <CheckItem>CHECK_BINLOG_ROW_IMAGE</CheckItem>
                        <CheckResult>Success</CheckResult>
                        <CheckItemDescription>CHECK_BINLOG_ROW_IMAGE_DETAIL</CheckItemDescription>
                  </Detail>
                  <Detail>
                        <CheckItem>CHECK_SERVER_ID</CheckItem>
                        <CheckResult>Success</CheckResult>
                        <CheckItemDescription>CHECK_SERVER_ID_DETAIL</CheckItemDescription>
                  </Detail>
                  <Detail>
                        <CheckItem>CHECK_BINLOG_EXIST</CheckItem>
                        <CheckResult>Success</CheckResult>
                        <CheckItemDescription>CHECK_BINLOG_EXIST_DETAIL</CheckItemDescription>
                  </Detail>
                  <Detail>
                        <CheckItem>CHECK_ENGINE</CheckItem>
                        <CheckResult>Success</CheckResult>
                        <CheckItemDescription>CHECK_ENGINE_DETAIL</CheckItemDescription>
                  </Detail>
                  <Detail>
                        <CheckItem>CHECK_MYSQL_PASSOWRD_FORMAT</CheckItem>
                        <CheckResult>Success</CheckResult>
                        <CheckItemDescription>CHECK_MYSQL_PASSOWRD_FORMAT_DETAIL</CheckItemDescription>
                  </Detail>
                  <Detail>
                        <CheckItem>CHECK_SRC</CheckItem>
                        <CheckResult>Success</CheckResult>
                        <CheckItemDescription>CHECK_SRC_DETAIL</CheckItemDescription>
                  </Detail>
<Detail>
```

```json
eta
                        <CheckItem>CHECK_SAME_OBJ</CheckItem>
                        <CheckResult>Success</CheckResult>
                        <CheckItemDescription>CHECK_SAME_OBJ_DETAIL</CheckItemDescription>
                  </Detail>
                  <Detail>
                        <CheckItem>CHECK_SQL_MODE</CheckItem>
                        <CheckResult>Success</CheckResult>
                        <CheckItemDescription>CHECK_SQL_MODE_DETAIL</CheckItemDescription>
                  </Detail>
                  <Detail>
                        <CheckItem>CHECK_SAME_USER</CheckItem>
                        <CheckResult>Success</CheckResult>
                        <CheckItemDescription>CHECK_SAME_USER_DETAIL</CheckItemDescription>
                  </Detail>
                  <Detail>
                        <CheckItem>CHECK_TOPOLOGY</CheckItem>
                        <CheckResult>Success</CheckResult>
                        <CheckItemDescription>CHECK_TOPOLOGY_DETAIL</CheckItemDescription>
                  </Detail>
            </PrecheckStatus>
            <DtsJobClass>large</DtsJobClass>
            <Checkpoint>1616902385</Checkpoint>
            <DtsJobId>i03e3zty16i****</DtsJobId>
            <DestinationEndpoint>
                  <UserName>dtstest</UserName>
                  <InstanceID>rm-bp1imrtn6fq7h****</InstanceID>
                  <SslSolutionEnum>DISABLE</SslSolutionEnum>
                  <Port>3306</Port>
                  <DatabaseName></DatabaseName>
                  <Region>cn-hangzhou</Region>
                  <InstanceType>RDS</InstanceType>
                  <EngineName>MySQL</EngineName>
            </DestinationEndpoint>
            <SourceEndpoint>
                  <UserName>dtstest</UserName>
                  <InstanceID>rm-bp1162kryivb8****</InstanceID>
                  <SslSolutionEnum>DISABLE</SslSolutionEnum>
                  <Port>3306</Port>
                  <Region>cn-hangzhou</Region>
                  <InstanceType>RDS</InstanceType>
                  <EngineName>MySQL</EngineName>
            </SourceEndpoint>
            <TagList>
                  <TagKey>testkey</TagKey>
                  <TagValue>testvalue</TagValue>
            </TagList>
            <Performance></Performance>
            <Reserved>
{"srcHostPorts":"","whitelist.dms.online.ddl.enable":false,"filterDDL":false,"sqlparser.dms.original.ddl":true,"srcOracleType":"sid","maxRetryTim 3200,"destSSL":"0","destOracleType":"sid","srcSSL":"0","dbListCaseChangeMode":"default","SourceEngineVersion":"8.0.18","srcNetType":"VPC","destNe e":"VPC","srcVpcNetMappingInst":"172.16.1**.**:10803","destVpcNetMappingInst":"172.16.1**.**:11077","useJobTask":"1"}</Reserved>
            <StructureInitializationStatus>
                  <Status>Finished</Status>
                  <Progress>1</Progress>
                  <Percent>100</Percent>
            </StructureInitializationStatus>
            <DataSynchronizationStatus>
                  <Status>Catched</Status>
                  <Progress>0/0</Progress>
                  <Percent>95</Percent>
            </DataSynchronizationStatus>
      </DtsJobList>
      <RequestId>621BB4F8-3016-4FAA-8D5A-5D3163CC****</RequestId>
      <PageNumber>2</PageNumber>
      <HttpStatusCode>200</HttpStatusCode>
      <Success>true</Success>
</DescribeDtsJobsResponse>
```

| JSON | format |
|---|---|
| { "TotalRecordCount": 15, "PageRecordCount": 1, "DtsJobList": [ { "Status": "Migrating", "DataInitializationStatus": { "Status": "Finished", "Progress": "44755", "Percent": "100" }, "DbObject": "{\"DTSTEST\":{\"name\":\"dtstest\",\"all\":true,\"state\":\"normal\",\"edit\":false}}", "CreateTime": "2021-03-16T08:01:19Z", "DtsJobName": "RDS_TO_RDS_MIGRATION", "ReverseJob": { "PrecheckStatus": {}, |   |

```json
    "DataInitializationStatus": {},
    "DestinationEndpoint": {},
    "SourceEndpoint": {},
    "Performance": {},
    "MigrationMode": {},
    "StructureInitializationStatus": {},
    "DataSynchronizationStatus": {}
```

`},`

```json
   "PayType": "PrePaid",
   "DtsInstanceID": "dtsi03e3zty16i****",
   "Delay": 0,
   "MigrationMode": {
    "DataInitialization": true,
    "DataSynchronization": true,
    "StructureInitialization": true
```

`},`

```json
   "PrecheckStatus": {
    "Status": "Finished",
    "Percent": "100",
    "Detail": [
```

`{`

```json
      "CheckItem": "CHECK_CONN_SRC",
      "CheckResult": "Success",
      "CheckItemDescription": "CHECK_CONN_SRC_DETAIL"
```

`},` `{`

```json
      "CheckItem": "CHECK_CONN_DEST",
      "CheckResult": "Success",
      "CheckItemDescription": "CHECK_CONN_DEST_DETAIL"
```

`},` `{`

```json
      "CheckItem": "CHECK_AUTH_SRC",
      "CheckResult": "Success",
      "CheckItemDescription": "CHECK_AUTH_SRC_DETAIL"
```

`},` `{`

```json
      "CheckItem": "CHECK_AUTH_DEST",
      "CheckResult": "Success",
      "CheckItemDescription": "CHECK_AUTH_DEST_DETAIL"
```

`},` `{`

```json
      "CheckItem": "CHECK_BINLOG_ON",
      "CheckResult": "Success",
      "CheckItemDescription": "CHECK_BINLOG_ON_DETAIL"
```

`},` `{`

```json
      "CheckItem": "CHECK_BINLOG_MODE",
      "CheckResult": "Success",
      "CheckItemDescription": "CHECK_BINLOG_MODE_DETAIL"
```

`},` `{`

```json
      "CheckItem": "CHECK_BINLOG_ROW_IMAGE",
      "CheckResult": "Success",
      "CheckItemDescription": "CHECK_BINLOG_ROW_IMAGE_DETAIL"
```

`},` `{`

```json
      "CheckItem": "CHECK_SERVER_ID",
      "CheckResult": "Success",
      "CheckItemDescription": "CHECK_SERVER_ID_DETAIL"
```

`},` `{`

```json
      "CheckItem": "CHECK_BINLOG_EXIST",
      "CheckResult": "Success",
      "CheckItemDescription": "CHECK_BINLOG_EXIST_DETAIL"
```

`},` `{`

```json
      "CheckItem": "CHECK_ENGINE",
      "CheckResult": "Success",
      "CheckItemDescription": "CHECK_ENGINE_DETAIL"
```

`},` `{`

```json
      "CheckItem": "CHECK_MYSQL_PASSOWRD_FORMAT",
      "CheckResult": "Success",
      "CheckItemDescription": "CHECK_MYSQL_PASSOWRD_FORMAT_DETAIL"
```

`},` `{`

```json
      "CheckItem": "CHECK_SRC",
      "CheckResult": "Success",
      "CheckItemDescription": "CHECK_SRC_DETAIL"
```

`},` `{`

```json
      "CheckItem": "CHECK_SAME_OBJ",
      "CheckResult": "Success",
      "CheckItemDescription": "CHECK_SAME_OBJ_DETAIL"
```

`},`

```json
      "CheckItem": "CHECKSQLMODE",
```

```
_Q_
```

`,`

```json
      "CheckResult": "Success",
      "CheckItemDescription": "CHECK_SQL_MODE_DETAIL"
```

`},`

```json
      "CheckItem": "CHECK_SAME_USER",
      "CheckResult": "Success",
      "CheckItemDescription": "CHECK_SAME_USER_DETAIL"
```

`},` `{`

```json
      "CheckItem": "CHECK_TOPOLOGY",
      "CheckResult": "Success",
      "CheckItemDescription": "CHECK_TOPOLOGY_DETAIL"
```

`}` `]` `},`

```json
   "DtsJobClass": "large",
   "Checkpoint": "1616902385",
   "DtsJobId": "i03e3zty16i****",
   "DestinationEndpoint": {
    "UserName": "dtstest",
    "InstanceID": "rm-bp1imrtn6fq7h****",
    "SslSolutionEnum": "DISABLE",
    "Port": "3306",
    "DatabaseName": "",
    "Region": "cn-hangzhou",
    "InstanceType": "RDS",
    "EngineName": "MySQL"
```

`},`

```json
   "SourceEndpoint": {
    "UserName": "dtstest",
    "InstanceID": "rm-bp1162kryivb8****",
    "SslSolutionEnum": "DISABLE",
    "Port": "3306",
    "Region": "cn-hangzhou",
    "InstanceType": "RDS",
    "EngineName": "MySQL"
```

`},`

```json
   "TagList": [
```

`{`

```json
     "TagKey": "testkey",
     "TagValue": "testvalue"
```

`}` `],`

```json
   "Performance": {},
   "Reserved":
```

`"`

```json
{\"srcHostPorts\":\"\",\"whitelist.dms.online.ddl.enable\":false,\"filterDDL\":false,\"sqlparser.dms.original.ddl\":true,\"srcOracleType\":\"sid\ maxRetryTime\":43200,\"destSSL\":\"0\",\"destOracleType\":\"sid\",\"srcSSL\":\"0\",\"dbListCaseChangeMode\":\"default\",\"SourceEngineVersion\":\ .18\",\"srcNetType\":\"VPC\",\"destNetType\":\"VPC\",\"srcVpcNetMappingInst\":\"172.16.1**.**:10803\",\"destVpcNetMappingInst\":\"172.16.1**.**:1 \",\"useJobTask\":\"1\"}",
   "StructureInitializationStatus": {
    "Status": "Finished",
    "Progress": "1",
    "Percent": "100"
```

`},`

```json
   "DataSynchronizationStatus": {
    "Status": "Catched",
    "Progress": "0/0",
    "Percent": "95"
```

`}` `}` `],`

```json
 "RequestId": "621BB4F8-3016-4FAA-8D5A-5D3163CC****",
 "PageNumber": 2,
 "HttpStatusCode": 200,
 "Success": true
```

`}`

##### 1.4.8.3 CountJobByCondition

Counts the number of Data Transmission Service (DTS) tasks based on the specified conditions.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CountJobByCondition | The operation that you want to perform. Set the value to CountJobByCondition. |
| Region | String | Yes | cn-hangzhou | The region ID of the DTS instance. |

| RegionId | String | Yes | cn-hangzhou | The region ID of the DTS instance. The value of this parameter must be the same as that of Region. |
|---|---|---|---|---|
| Type | String | No | name | The type of the query condition. Valid values: name: queries DTS tasks based on the task name. rds: queries DTS tasks based on the destination instance ID. instance: queries DTS tasks based on the DTS instance ID. srcRds: queries DTS tasks based on the source instance ID. Note You must specify Params to specify the content of the query condition. |
| JobType | String | No | SYNC | The type of the DTS task. Valid values: MIGRATION: data migration task. SYNC: data synchronization task. SUBSCRIBE: change tracking task. |
| Params | String | No | dtspk3f13r731m**** | The content of the query condition. Note You must specify Type to specify the type of the query condition. |
| Status | String | No | Finished | The state of the DTS task. Valid values for a data migration task: NotStarted: The task is not started. Prechecking: The task is in precheck. PrecheckFailed: The task failed to pass the precheck. PreCheckPass: The task passed the precheck. NotConfigured: The task is not configured. Migrating: The task is in progress. Suspending: The task is paused. MigrationFailed: The task failed. Finished: The task is complete. Retrying: The task is being retried. Upgrade: The task is being upgraded. Locked: The task is locked. Downgrade: The task is being downgraded. Valid values for a data synchronization task: NotStarted: The task is not started. Prechecking: The task is in precheck. PrecheckFailed: The task failed to pass the precheck. PreCheckPass: The task passed the precheck. NotConfigured: The task is not configured. Initializing: Initial synchronization is in progress. InitializeFailed: Initial synchronization failed. Synchronizing: The task is in progress. Failed: The task failed. Suspending: The task is paused. Modifying: The objects in the task are being modified. Finished: The task is complete. Retrying: The task is being retried. Upgrade: The task is being upgraded. Locked: The task is locked. Downgrade: The task is being downgraded. Valid values for a change tracking task: NotConfigured: The task is not configured. NotStarted: The task is not started. Prechecking: The task is in precheck. PrecheckFailed: The task failed to pass the precheck. PreCheckPass: The task passed the precheck. Starting: The task is being started. Normal: The task is running as expected. Retrying: The task is being retried. Abnormal: The task is not running as expected. Upgrade: The task is being upgraded. Locked: The task is locked. Downgrade: The task is being downgraded. |
| GroupId | String | No | pk13r731m**** | The parent task ID of the DTS task. |

| SrcDbType | String | No | mongodb | The type of the source database. Valid values: MySQL: ApsaraDB RDS for MySQL instance or self-managed MySQL database. PolarDB: PolarDB for MySQL cluster. polardbo: PolarDB for Oracle cluster. _ polardbpg: PolarDB for PostgreSQL cluster. _ Redis: ApsaraDB for Redis instance or self-managed Redis database. DRDS: PolarDB-X 1.0 instance or PolarDB-X 2.0 instance. PostgreSQL: self-managed PostgreSQL database. odps: MaxCompute project. oracle: self-managed Oracle database. mongodb: ApsaraDB for MongoDB instance or self- managed MongoDB database. tidb: TiDB database. ADS: AnalyticDB for MySQL V2.0 cluster. ADB30: AnalyticDB for MySQL V3.0 cluster. Greenplum: AnalyticDB for PostgreSQL instance. MSSQL: ApsaraDB RDS for SQL Server instance or self- managed SQL Server database. kafka: Message Queue for Apache Kafka instance or self- managed Kafka cluster. DataHub: DataHub project. clickhouse: ApsaraDB for ClickHouse cluster. DB2: self-managed Db2 for LUW database. as400: AS/400. Tablestore: Tablestore instance. |
|---|---|---|---|---|
| DestDbType | String | No | mongodb | The type of the destination database. Valid values: MySQL: ApsaraDB RDS for MySQL instance or self-managed MySQL database. PolarDB: PolarDB for MySQL cluster. polardbo: PolarDB for Oracle cluster. _ polardbpg: PolarDB for PostgreSQL cluster. _ Redis: ApsaraDB for Redis instance or self-managed Redis database. DRDS: PolarDB-X 1.0 instance or PolarDB-X 2.0 instance. PostgreSQL: self-managed PostgreSQL database. odps: MaxCompute project. oracle: self-managed Oracle database. mongodb: ApsaraDB for MongoDB instance or self- managed MongoDB database. tidb: TiDB database. ADS: AnalyticDB for MySQL V2.0 cluster. ADB30: AnalyticDB for MySQL V3.0 cluster. Greenplum: AnalyticDB for PostgreSQL instance. MSSQL: ApsaraDB RDS for SQL Server instance or self- managed SQL Server database. kafka: Message Queue for Apache Kafka instance or self- managed Kafka cluster. DataHub: DataHub project. clickhouse: ApsaraDB for ClickHouse cluster. DB2: self-managed Db2 for LUW database. as400: AS/400. Tablestore: Tablestore instance. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| DynamicCode | String | 403 | The dynamic error code. This parameter will be removed in the future. |
| DynamicMessage | String | Type | The dynamic part in the error message. This parameter is used to replace the %s variable in the value of ErrMessage. Note For example, if the return value of ErrMessage is The Value of Input Parameter %s is not valid and the return value of DynamicMessage is Type, the specified value of Type is invalid. |
| ErrCode | String | InternalError | The error code returned if the request failed. |
| ErrMessage | String | The Value of Input Parameter %s is not valid. | The error message returned if the request failed. |
| HttpStatusCode | Integer | 200 | The HTTP status code. |
| RequestId | String | FC3BAAF2-74E3-4471-8EB5- 96202D6A**** | The request ID. |

| Success | Boolean | true | Indicates whether the request was successful. |
|---|---|---|---|
| TotalRecordCount | Long | 100 | The total number of DTS tasks that meet the specified conditions within your Alibaba Cloud account. |

**Examples**

Sample requests

```
http(s)://dts.aliyuncs.com/?Action=CountJobByCondition &Region=cn-hangzhou &RegionId=cn-hangzhou &<Common request parameters>
```

Sample success responses

| XML | format |
|---|---|
| <TotalRecordCount>6</TotalRecordCount> <RequestId>4586B7A9-73E0-57DC-8C0D-61D****</RequestId> <HttpStatusCode>200</HttpStatusCode> <Success>true</Success> |   |

| JSON | format |
|---|---|
| { "TotalRecordCount": 6, "RequestId": "4586B7A9-73E0-57DC-8C0D-61D****", "HttpStatusCode": 200, "Success": true } |   |

##### 1.4.8.4 DescribePreCheckStatus

Queries the state of a Data Transmission Service (DTS) subtask, including precheck, schema migration, initial schema synchronization, full data migration, initial full data synchronization, incremental data migration, or incremental data synchronization.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribePreCheckStatus | The operation that you want to perform. Set the value to DescribePreCheckStatus. |
| DtsJobId | String | Yes | i03e3zty16i**** | The ID of the data migration, data synchronization, or change tracking task. |
| JobCode | String | Yes | 01 | The task code that specifies the subtask type. Valid values: 01: precheck 02: schema migration or initial schema synchronization 03: full data migration or initial full data synchronization 04: incremental data migration or synchronization |
| StructType | String | Yes | before | The type of schema definition. Valid values: before: schema migration or initial schema synchronization after: DDL operations performed during incremental data migration or synchronization |
| PageNo | String | No | 1 | The number of the page to return. The value must be an integer that is greater than 0. Default value: 1. |
| PageSize | String | No | 30 | The number of entries to return on each page. Default value: 20. |
| RegionId | String | No | cn-beijing | The region ID of the DTS instance. |
| StructPhase | String | No | View | The filter item used to filter tables, views, and functions during schema migration. |
| Name | String | No | dewuprop | The filter item used to filter tables in fuzzy match. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| JobProgress | Array of ProgressInfo |   | The list of subtasks and the progress of each subtask. |

| BootTime | String | 2021-03-16T08:01:31.000+00:00 | The time when the subtask was started. The time is displayed in the yyyy-MM-ddTHH:mm:ssZ format in UTC. |
|---|---|---|---|
| CanSkip | Boolean | true | Indicates whether the subtask can be ignored if it fails. |
| DdlSql | String | CREATE TABLE `dtstestdata`.`order` (\n`orderid` int(11) COMMENT '' NOT NULL , \n`username` char(32) CHARSET `utf8` COLLATE `utf8generalci` _ _ COMMENT '' NULL , \n`ordertime` datetime COMMENT '' NULL , \n`commodity` varchar(32) CHARSET `utf8` COLLATE `utf8generalci` COMMENT '' _ _ NULL , \n`phonenumber` int(11) COMMENT '' NULL , \n`address` text CHARSET `utf8mb4` COLLATE `utf8mb4generalci` _ _ COMMENT '' NULL \n, PRIMARY KEY (`orderid`)) engine=InnoDB DEFAULT CHARSET=`gbk` DEFAULT COLLATE `gbkchineseci` ROWFORMAT= _ _ _ Dynamic comment = '' ;\n | The executed DDL statements. |
| DelaySeconds | Integer | 0 | The latency of incremental data migration or synchronization. Note For data migration tasks, the unit of this parameter is milliseconds. For data synchronization tasks, the unit of this parameter is seconds. |
| DestSchema | String | dtstestdatanew _ | The name of the database that contains the migrated objects in the destination instance. |
| DiffRow | Long | 1 | This parameter will be removed in the future. |
| ErrDetail | String | CHECK ERRORSAMEOBJDETAI __ _ _ _ L | The error details of the subtask failure. |
| ErrMsg | String | CHECK ERRORSAMEOBJ __ _ _ | The error message of the subtask failure. |
| FinishTime | String | 2021-03-16T08:01:34.000+00:00 | The time when the subtask was completed. The time is displayed in the yyyy-MM-ddTHH:mm:ssZ format in UTC. |
| Id | String | 5632 | The ID of the entry in the metadatabase. |
| IgnoreFlag | String | N | Indicates whether DTS ignores the subtask and proceeds with the next subtask. Valid values: N: no Y: yes |
| Item | String | CHECKCONNDEST _ _ | The shortened name of the subtask. |
| JobId | String | fj1c33ro168**** | The ID of the subtask. |
| Logs | Array of JobLog |   | The logs of subtask failures. |
| ErrData | String | CREATE TABLE `dtstestdata`.`customer` (\n`runoobid` int(10) unsigned _ autoincrement COMMENT '' NOT _ NULL , \n`runoobtitle` _ varchar(100) CHARSET `utf8` COLLATE `utf8generalci` _ _ COMMENT '' NOT NULL , \n`runoobauthor1216` _ varchar(40) CHARSET `utf8` COLLATE `utf8generalci` _ _ COMMENT '' NOT NULL , \n`submissiondate1216` date _ COMMENT '' NULL \n, PRIMARY KEY (`runoobid`)) _ engine=InnoDB AUTOINCREMENT=200001 _ DEFAULT CHARSET=`utf8` DEFAULT COLLATE `utf8generalci` ROWFORMAT= _ _ _ Dynamic comment = '' ;\n | The record of errors. |
| ErrMsg | String | DTS-1020042 Execute sql error sql: Table 'customer' already exists | The error message returned when an error occurs on the subtask. |
| ErrType | String | ForeignKey | The error type. |

| LogLevel | String | ERROR | The log level. |
|---|---|---|---|
| Names | String | CHECKCONNDESTDETAIL _ _ _ | The name of the subtask. |
| OrderNum | Integer | 10 | The serial number of the subtask. |
| ParentObj | String | demo | This parameter will be removed in the future. |
| RepairMethod | String | CHECK ERRORSAMEOBJREPAI __ _ _ _ R | The method to fix the subtask failure. |
| Skip | Boolean | false | Indicates whether the subtask is ignored if it fails. |
| SourceSchema | String | dtstestdata | The name of the database that contains the objects to be migrated from the source instance. |
| State | String | Success | The state of the subtask. Valid values: NotStarted: The subtask is not started. Checking: The subtask is in progress. Migrating: The subtask is in progress. Failed: The subtask failed. Warning: An exception occurred on the subtask. Success: The subtask is complete. |
| Sub | String | [] | The sub-item progress of the subtask. Note If [] is returned, the subtask has no sub-items. |
| TargetNames | String | order | The names of the objects to be migrated or synchronized. |
| Total | Integer | 1 | The total number of subtasks. |
| ErrorItem | Integer | 0 | The total number of subtask failures. |
| HttpStatusCode | Integer | 200 | The HTTP status code. |
| JobName | String | precheck | The name of the subtask. |
| Code | String | 01 | The task code that indicates the subtask type. Valid values: 01: precheck 02: schema migration or initial schema synchronization 03: full data migration or initial full data synchronization 04: incremental data migration or synchronization |
| RequestId | String | C096FA97-B6BA-4575-899D- 61E12B59**** | The ID of the request. |
| State | String | Finished | The state of the subtask. Valid values: NotStarted: The subtask is not started. Suspending: The subtask is paused. Checking: The subtask is in progress. Migrating: The subtask is in progress. Failed: The subtask failed. Catched: The subtask is in progress. Finished: The subtask is complete. |
| Success | Boolean | true | Indicates whether the call was successful. |
| Total | Integer | 0 | The total number of subtasks. |
| JobId | String | b4my3zg929a**** | The ID of the data migration or data synchronization task. |
| PageNumber | Long | 1 | The page number of the returned page. The value must be an integer that is greater than 0. Default value: 1. |
| PageRecordCount | Long | 20 | The number of entries returned per page. |
| SubDistributedJobStatus | Array of SubDistributedJobStatus |   | The state of the distributed subtask. |

| Code | String | 02 | The task code that indicates the subtask type. Valid values: 01: precheck 02: schema migration or initial schema synchronization 03: full data migration or initial full data synchronization 04: incremental data migration or synchronization |
|---|---|---|---|
| ErrorItem | Integer | 0 | The number of subtasks that failed. |
| JobId | String | n0gm1682j6563np | The ID of the subtask. |
| JobName | String | dts.step.struct.load | The name of distributed subtasks associated with the subtask. |
| JobProgress | Array of ProgressInfo |   | The list of subtasks and the progress of each subtask. |
| BootTime | String | 2022-03-30T03:36:11.000+00:00 | The time when the subtask was started. The time is displayed in the yyyy-MM-ddTHH:mm:ssZ format in UTC. |
| CanSkip | Boolean | false | Indicates whether the subtask can be ignored if it fails. Valid values: true: yes false: no |
| DdlSql | String | None | The executed DDL statements. |
| DelaySeconds | Integer | 0 | The latency of incremental data migration or synchronization. |
| DestSchema | String | databasetest | The name of the database that contains the migrated objects in the destination instance. |
| DiffRow | Long | 1 | This parameter will be removed in the future. |
| ErrDetail | String | The latency of incremental data migration or synchronization. | The error details of the subtask failure. |
| ErrMsg | String | ODPS project does not exist odps.`huijin | The error message of the subtask failure. |
| FinishTime | String | 2022-03-31T03:36:11.000+00:00 | The time when the subtask was completed. The time is displayed in the yyyy-MM-ddTHH:mm:ssZ format in UTC. |
| Id | String | 3890 | The ID of the entry in the metadatabase. |
| IgnoreFlag | String | N | Indicates whether DTS ignores the subtask and proceeds with the next subtask. Valid values: N: no Y: yes |
| Item | String | logincommontime _ _ | The name of the subtask. |
| JobId | String | l3m1213ye7l**** | The ID of the subtask. |
| Logs | Array of JobLog |   | The logs of subtask failures. |
| ErrData | String | CREATE TABLE `dtstestdata`.`customer` (\n`runoobid` int(10) unsigned _ autoincrement COMMENT '' NOT _ NULL , \n`runoobtitle` _ varchar(100) CHARSET `utf8` COLLATE `utf8generalci` _ _ COMMENT '' NOT NULL , \n`runoobauthor1216` _ varchar(40) CHARSET `utf8` COLLATE `utf8generalci` _ _ COMMENT '' NOT NULL , \n`submissiondate1216` date _ COMMENT '' NULL \n, PRIMARY KEY (`runoobid`)) _ engine=InnoDB AUTOINCREMENT=200001 _ DEFAULT CHARSET=`utf8` DEFAULT COLLATE `utf8generalci` ROWFORMAT= _ _ _ Dynamic comment = '' ;\n | The record of errors. |
| ErrMsg | String | get metric list fail | The error message. |

| ErrType | String | ForeignKey | The error type. |
|---|---|---|---|
| LogLevel | String | INFO | The log level. |
| Names | String | metricRuleTargets- 20180308houe | The name of the subtask. |
| OrderNum | Integer | 1 | The serial number of the subtask. |
| ParentObj | String | None | This parameter will be removed in the future. |
| RepairMethod | String | CHECK ERRORSAMEOBJREPAI __ _ _ _ R | The method used to fix a precheck failure. |
| Skip | Boolean | true | Indicates whether the subtask was skipped. Valid values: true: yes false: no |
| SourceSchema | String | databasetest | The name of the database that contains the objects to be migrated from the source instance. |
| State | String | Finished | The state of the subtask. Valid values: NotStarted: The subtask is not started. Suspending: The subtask is paused. Checking: The subtask is in progress. Migrating: The subtask is in progress. Failed: The subtask failed. Catched: The subtask is in progress. Finished: The subtask is complete. |
| Sub | String | [] | The sub-item progress of the subtask. Note If [] is returned, the subtask has no sub-items. |
| TargetNames | String | order | The names of the objects that are migrated or synchronized. |
| Total | Integer | 11 | The total number of returned entries. |
| State | String | Finished | The state of the subtask. Valid values: NotStarted: The subtask is not started. Suspending: The subtask is paused. Checking: The subtask is in progress. Migrating: The subtask is in progress. Failed: The subtask failed. Catched: The subtask is in progress. Finished: The subtask is complete. |
| Total | Integer | 11 | The total number of returned entries. |
| TotalRecordCount | Long | 100 | The total number of returned records. |

**Examples**

Sample requests

```
http(s)://dts.aliyuncs.com/?Action=DescribePreCheckStatus &DtsJobId=i03e3zty16i**** &JobCode=01 &StructType=before &<Common request parameters>
```

Sample success responses

| XML | format |
|---|---|
| <DescribePreCheckStatusResponse> <RequestId>C096FA97-B6BA-4575-899D-61E12B59****</RequestId> <State>Finished</State> <Total>0</Total> <HttpStatusCode>200</HttpStatusCode> <JobName>Precheck</JobName> <ErrorItem>0</ErrorItem> <Code>01</Code> <Success>true</Success> <JobProgress> <BootTime>2021-03-16T08:01:31.000+00:00</BootTime> |   |

```
Boot
```

`e`

```
608:0:3.00000:00/Boot
```

`e`

```xml
            <Names>CHECK_CONN_SRC_DETAIL</Names>
            <Item>CHECK_CONN_SRC</Item>
            <CanSkip>false</CanSkip>
            <DelaySeconds>0</DelaySeconds>
            <FinishTime>2021-03-16T08:01:31.000+00:00</FinishTime>
            <OrderNum>10</OrderNum>
            <IgnoreFlag>N</IgnoreFlag>
            <State>Success</State>
            <Skip>false</Skip>
            <JobId>fj1c33ro168****</JobId>
      </JobProgress>
      <JobProgress>
            <BootTime>2021-03-16T08:01:31.000+00:00</BootTime>
            <Names>CHECK_CONN_DEST_DETAIL</Names>
            <Item>CHECK_CONN_DEST</Item>
            <CanSkip>false</CanSkip>
            <DelaySeconds>0</DelaySeconds>
            <FinishTime>2021-03-16T08:01:31.000+00:00</FinishTime>
            <OrderNum>20</OrderNum>
            <IgnoreFlag>N</IgnoreFlag>
            <State>Success</State>
            <Skip>false</Skip>
            <JobId>fj1c33ro168****</JobId>
      </JobProgress>
      <JobProgress>
            <BootTime>2021-03-16T08:01:32.000+00:00</BootTime>
            <Names>CHECK_AUTH_SRC_DETAIL</Names>
            <Item>CHECK_AUTH_SRC</Item>
            <CanSkip>false</CanSkip>
            <DelaySeconds>0</DelaySeconds>
            <FinishTime>2021-03-16T08:01:33.000+00:00</FinishTime>
            <OrderNum>15</OrderNum>
            <IgnoreFlag>N</IgnoreFlag>
            <State>Success</State>
            <Skip>false</Skip>
            <JobId>fj1c33ro168****</JobId>
      </JobProgress>
      <JobProgress>
            <BootTime>2021-03-16T08:01:33.000+00:00</BootTime>
            <Names>CHECK_AUTH_DEST_DETAIL</Names>
            <Item>CHECK_AUTH_DEST</Item>
            <CanSkip>false</CanSkip>
            <DelaySeconds>0</DelaySeconds>
            <FinishTime>2021-03-16T08:01:33.000+00:00</FinishTime>
            <OrderNum>25</OrderNum>
            <IgnoreFlag>N</IgnoreFlag>
            <State>Success</State>
            <Skip>false</Skip>
            <JobId>fj1c33ro168****</JobId>
      </JobProgress>
      <JobProgress>
            <BootTime>2021-03-16T08:01:33.000+00:00</BootTime>
            <Names>CHECK_BINLOG_ON_DETAIL</Names>
            <Item>CHECK_BINLOG_ON</Item>
            <CanSkip>false</CanSkip>
            <DelaySeconds>0</DelaySeconds>
            <FinishTime>2021-03-16T08:01:33.000+00:00</FinishTime>
            <OrderNum>30</OrderNum>
            <IgnoreFlag>N</IgnoreFlag>
            <State>Success</State>
            <Skip>false</Skip>
            <JobId>fj1c33ro168****</JobId>
      </JobProgress>
      <JobProgress>
            <BootTime>2021-03-16T08:01:33.000+00:00</BootTime>
            <Names>CHECK_BINLOG_MODE_DETAIL</Names>
            <Item>CHECK_BINLOG_MODE</Item>
            <CanSkip>false</CanSkip>
            <DelaySeconds>0</DelaySeconds>
            <FinishTime>2021-03-16T08:01:33.000+00:00</FinishTime>
            <OrderNum>40</OrderNum>
            <IgnoreFlag>N</IgnoreFlag>
            <State>Success</State>
            <Skip>false</Skip>
            <JobId>fj1c33ro168****</JobId>
      </JobProgress>
      <JobProgress>
            <BootTime>2021-03-16T08:01:33.000+00:00</BootTime>
            <Names>CHECK_BINLOG_ROW_IMAGE_DETAIL</Names>
            <Item>CHECK_BINLOG_ROW_IMAGE</Item>
            <CanSkip>false</CanSkip>
            <DelaySeconds>0</DelaySeconds>
            <FinishTime>2021-03-16T08:01:33.000+00:00</FinishTime>
            <OrderNum>50</OrderNum>
            <IgnoreFlag>N</IgnoreFlag>
            <State>Success</State>
<Skip>false</Skip>
```

```xml
            <Skip>false</Skip>
            <JobId>fj1c33ro168****</JobId>
      </JobProgress>
      <JobProgress>
            <BootTime>2021-03-16T08:01:33.000+00:00</BootTime>
            <Names>CHECK_SERVER_ID_DETAIL</Names>
            <Item>CHECK_SERVER_ID</Item>
            <CanSkip>true</CanSkip>
            <DelaySeconds>0</DelaySeconds>
            <FinishTime>2021-03-16T08:01:34.000+00:00</FinishTime>
            <OrderNum>60</OrderNum>
            <IgnoreFlag>N</IgnoreFlag>
            <State>Success</State>
            <Skip>false</Skip>
            <JobId>fj1c33ro168****</JobId>
      </JobProgress>
      <JobProgress>
            <BootTime>2021-03-16T08:01:34.000+00:00</BootTime>
            <Names>CHECK_BINLOG_EXIST_DETAIL</Names>
            <Item>CHECK_BINLOG_EXIST</Item>
            <CanSkip>false</CanSkip>
            <DelaySeconds>0</DelaySeconds>
            <FinishTime>2021-03-16T08:01:34.000+00:00</FinishTime>
            <OrderNum>70</OrderNum>
            <IgnoreFlag>N</IgnoreFlag>
            <State>Success</State>
            <Skip>false</Skip>
            <JobId>fj1c33ro168****</JobId>
      </JobProgress>
      <JobProgress>
            <BootTime>2021-03-16T08:01:34.000+00:00</BootTime>
            <Names>CHECK_ENGINE_DETAIL</Names>
            <Item>CHECK_ENGINE</Item>
            <CanSkip>false</CanSkip>
            <DelaySeconds>0</DelaySeconds>
            <FinishTime>2021-03-16T08:01:34.000+00:00</FinishTime>
            <OrderNum>80</OrderNum>
            <IgnoreFlag>N</IgnoreFlag>
            <State>Success</State>
            <Skip>false</Skip>
            <JobId>fj1c33ro168****</JobId>
      </JobProgress>
      <JobProgress>
            <BootTime>2021-03-16T08:01:34.000+00:00</BootTime>
            <Names>CHECK_MYSQL_PASSOWRD_FORMAT_DETAIL</Names>
            <Item>CHECK_MYSQL_PASSOWRD_FORMAT</Item>
            <CanSkip>false</CanSkip>
            <DelaySeconds>0</DelaySeconds>
            <FinishTime>2021-03-16T08:01:34.000+00:00</FinishTime>
            <OrderNum>90</OrderNum>
            <IgnoreFlag>N</IgnoreFlag>
            <State>Success</State>
            <Skip>false</Skip>
            <JobId>fj1c33ro168****</JobId>
      </JobProgress>
      <JobProgress>
            <BootTime>2021-03-16T08:01:34.000+00:00</BootTime>
            <Names>CHECK_SRC_DETAIL</Names>
            <Item>CHECK_SRC</Item>
            <CanSkip>true</CanSkip>
            <DelaySeconds>0</DelaySeconds>
            <FinishTime>2021-03-16T08:01:34.000+00:00</FinishTime>
            <OrderNum>100</OrderNum>
            <IgnoreFlag>N</IgnoreFlag>
            <State>Success</State>
            <Skip>false</Skip>
            <JobId>fj1c33ro168****</JobId>
      </JobProgress>
      <JobProgress>
            <BootTime>2021-03-16T08:01:34.000+00:00</BootTime>
            <Names>CHECK_SAME_OBJ_DETAIL</Names>
            <Item>CHECK_SAME_OBJ</Item>
            <CanSkip>true</CanSkip>
            <DelaySeconds>0</DelaySeconds>
            <FinishTime>2021-03-16T08:01:34.000+00:00</FinishTime>
            <OrderNum>110</OrderNum>
            <IgnoreFlag>N</IgnoreFlag>
            <State>Success</State>
            <Skip>false</Skip>
            <JobId>fj1c33ro168****</JobId>
      </JobProgress>
      <JobProgress>
            <BootTime>2021-03-16T08:01:34.000+00:00</BootTime>
            <Names>CHECK_SQL_MODE_DETAIL</Names>
            <Item>CHECK_SQL_MODE</Item>
            <CanSkip>false</CanSkip>
            <DelaySeconds>0</DelaySeconds>
```

```xml
            <FinishTime>2021-03-16T08:01:34.000+00:00</FinishTime>
            <OrderNum>140</OrderNum>
            <IgnoreFlag>N</IgnoreFlag>
            <State>Success</State>
            <Skip>false</Skip>
            <JobId>fj1c33ro168****</JobId>
      </JobProgress>
      <JobProgress>
            <BootTime>2021-03-16T08:01:34.000+00:00</BootTime>
            <Names>CHECK_SAME_USER_DETAIL</Names>
            <Item>CHECK_SAME_USER</Item>
            <CanSkip>true</CanSkip>
            <DelaySeconds>0</DelaySeconds>
            <FinishTime>2021-03-16T08:01:34.000+00:00</FinishTime>
            <OrderNum>200</OrderNum>
            <IgnoreFlag>N</IgnoreFlag>
            <State>Success</State>
            <Skip>false</Skip>
            <JobId>fj1c33ro168****</JobId>
      </JobProgress>
      <JobProgress>
            <BootTime>2021-03-16T08:01:34.000+00:00</BootTime>
            <Names>CHECK_TOPOLOGY_DETAIL</Names>
            <Item>CHECK_TOPOLOGY</Item>
            <CanSkip>true</CanSkip>
            <DelaySeconds>0</DelaySeconds>
            <FinishTime>2021-03-16T08:01:35.000+00:00</FinishTime>
            <OrderNum>220</OrderNum>
            <IgnoreFlag>N</IgnoreFlag>
            <State>Success</State>
            <Skip>false</Skip>
            <JobId>fj1c33ro168****</JobId>
      </JobProgress>
</DescribePreCheckStatusResponse>
```

| JSON | format |
|---|---|
| { "RequestId": "C096FA97-B6BA-4575-899D-61E12B59****", "State": "Finished", "Total": 0, "HttpStatusCode": 200, "JobName": "Precheck", "ErrorItem": 0, "Code": "01", "Success": true, "JobProgress": [ { "Sub": [], "BootTime": "2021-03-16T08:01:31.000+00:00", "Logs": [], "Names": "CHECK_CONN_SRC_DETAIL", "Item": "CHECK_CONN_SRC", "CanSkip": false, "DelaySeconds": 0, "FinishTime": "2021-03-16T08:01:31.000+00:00", "OrderNum": 10, "IgnoreFlag": "N", "State": "Success", "Skip": false, "JobId": "fj1c33ro168****" }, { "Sub": [], "BootTime": "2021-03-16T08:01:31.000+00:00", "Logs": [], "Names": "CHECK_CONN_DEST_DETAIL", "Item": "CHECK_CONN_DEST", "CanSkip": false, "DelaySeconds": 0, "FinishTime": "2021-03-16T08:01:31.000+00:00", "OrderNum": 20, "IgnoreFlag": "N", "State": "Success", "Skip": false, "JobId": "fj1c33ro168****" }, { "Sub": [], "BootTime": "2021-03-16T08:01:32.000+00:00", "Logs": [], "Names": "CHECK_AUTH_SRC_DETAIL", "Item": "CHECK_AUTH_SRC", "CanSkip": false, "DelaySeconds": 0, "FinishTime": "2021-03-16T08:01:33.000+00:00", "OrderNum": 15 |   |

```json
   OrderNum: 15,
   "IgnoreFlag": "N",
   "State": "Success",
   "Skip": false,
   "JobId": "fj1c33ro168****"
```

`},` `{`

```json
   "Sub": [],
   "BootTime": "2021-03-16T08:01:33.000+00:00",
   "Logs": [],
   "Names": "CHECK_AUTH_DEST_DETAIL",
   "Item": "CHECK_AUTH_DEST",
   "CanSkip": false,
   "DelaySeconds": 0,
   "FinishTime": "2021-03-16T08:01:33.000+00:00",
   "OrderNum": 25,
   "IgnoreFlag": "N",
   "State": "Success",
   "Skip": false,
   "JobId": "fj1c33ro168****"
```

`},` `{`

```json
   "Sub": [],
   "BootTime": "2021-03-16T08:01:33.000+00:00",
   "Logs": [],
   "Names": "CHECK_BINLOG_ON_DETAIL",
   "Item": "CHECK_BINLOG_ON",
   "CanSkip": false,
   "DelaySeconds": 0,
   "FinishTime": "2021-03-16T08:01:33.000+00:00",
   "OrderNum": 30,
   "IgnoreFlag": "N",
   "State": "Success",
   "Skip": false,
   "JobId": "fj1c33ro168****"
```

`},` `{`

```json
   "Sub": [],
   "BootTime": "2021-03-16T08:01:33.000+00:00",
   "Logs": [],
   "Names": "CHECK_BINLOG_MODE_DETAIL",
   "Item": "CHECK_BINLOG_MODE",
   "CanSkip": false,
   "DelaySeconds": 0,
   "FinishTime": "2021-03-16T08:01:33.000+00:00",
   "OrderNum": 40,
   "IgnoreFlag": "N",
   "State": "Success",
   "Skip": false,
   "JobId": "fj1c33ro168****"
```

`},` `{`

```json
   "Sub": [],
   "BootTime": "2021-03-16T08:01:33.000+00:00",
   "Logs": [],
   "Names": "CHECK_BINLOG_ROW_IMAGE_DETAIL",
   "Item": "CHECK_BINLOG_ROW_IMAGE",
   "CanSkip": false,
   "DelaySeconds": 0,
   "FinishTime": "2021-03-16T08:01:33.000+00:00",
   "OrderNum": 50,
   "IgnoreFlag": "N",
   "State": "Success",
   "Skip": false,
   "JobId": "fj1c33ro168****"
```

`},` `{`

```json
   "Sub": [],
   "BootTime": "2021-03-16T08:01:33.000+00:00",
   "Logs": [],
   "Names": "CHECK_SERVER_ID_DETAIL",
   "Item": "CHECK_SERVER_ID",
   "CanSkip": true,
   "DelaySeconds": 0,
   "FinishTime": "2021-03-16T08:01:34.000+00:00",
   "OrderNum": 60,
   "IgnoreFlag": "N",
   "State": "Success",
   "Skip": false,
   "JobId": "fj1c33ro168****"
```

`},` `{`

```json
   "Sub": [],
   "BootTime": "2021-03-16T08:01:34.000+00:00",
   "Logs": [],
   "Names": "CHECK_BINLOG_EXIST_DETAIL",
   "Item": "CHECK_BINLOG_EXIST",
```

```json
   "CanSkip": false,
   "DelaySeconds": 0,
   "FinishTime": "2021-03-16T08:01:34.000+00:00",
   "OrderNum": 70,
   "IgnoreFlag": "N",
   "State": "Success",
   "Skip": false,
   "JobId": "fj1c33ro168****"
```

`},` `{`

```json
   "Sub": [],
   "BootTime": "2021-03-16T08:01:34.000+00:00",
   "Logs": [],
   "Names": "CHECK_ENGINE_DETAIL",
   "Item": "CHECK_ENGINE",
   "CanSkip": false,
   "DelaySeconds": 0,
   "FinishTime": "2021-03-16T08:01:34.000+00:00",
   "OrderNum": 80,
   "IgnoreFlag": "N",
   "State": "Success",
   "Skip": false,
   "JobId": "fj1c33ro168****"
```

`},` `{`

```json
   "Sub": [],
   "BootTime": "2021-03-16T08:01:34.000+00:00",
   "Logs": [],
   "Names": "CHECK_MYSQL_PASSOWRD_FORMAT_DETAIL",
   "Item": "CHECK_MYSQL_PASSOWRD_FORMAT",
   "CanSkip": false,
   "DelaySeconds": 0,
   "FinishTime": "2021-03-16T08:01:34.000+00:00",
   "OrderNum": 90,
   "IgnoreFlag": "N",
   "State": "Success",
   "Skip": false,
   "JobId": "fj1c33ro168****"
```

`},` `{`

```json
   "Sub": [],
   "BootTime": "2021-03-16T08:01:34.000+00:00",
   "Logs": [],
   "Names": "CHECK_SRC_DETAIL",
   "Item": "CHECK_SRC",
   "CanSkip": true,
   "DelaySeconds": 0,
   "FinishTime": "2021-03-16T08:01:34.000+00:00",
   "OrderNum": 100,
   "IgnoreFlag": "N",
   "State": "Success",
   "Skip": false,
   "JobId": "fj1c33ro168****"
```

`},` `{`

```json
   "Sub": [],
   "BootTime": "2021-03-16T08:01:34.000+00:00",
   "Logs": [],
   "Names": "CHECK_SAME_OBJ_DETAIL",
   "Item": "CHECK_SAME_OBJ",
   "CanSkip": true,
   "DelaySeconds": 0,
   "FinishTime": "2021-03-16T08:01:34.000+00:00",
   "OrderNum": 110,
   "IgnoreFlag": "N",
   "State": "Success",
   "Skip": false,
   "JobId": "fj1c33ro168****"
```

`},` `{`

```json
   "Sub": [],
   "BootTime": "2021-03-16T08:01:34.000+00:00",
   "Logs": [],
   "Names": "CHECK_SQL_MODE_DETAIL",
   "Item": "CHECK_SQL_MODE",
   "CanSkip": false,
   "DelaySeconds": 0,
   "FinishTime": "2021-03-16T08:01:34.000+00:00",
   "OrderNum": 140,
   "IgnoreFlag": "N",
   "State": "Success",
   "Skip": false,
   "JobId": "fj1c33ro168****"
```

`},`

```json
   "Sub": [],
   "BootTime": "2021-03-16T08:01:34.000+00:00",
```

```json
   "Logs": [],
   "Names": "CHECK_SAME_USER_DETAIL",
   "Item": "CHECK_SAME_USER",
   "CanSkip": true,
   "DelaySeconds": 0,
   "FinishTime": "2021-03-16T08:01:34.000+00:00",
   "OrderNum": 200,
   "IgnoreFlag": "N",
   "State": "Success",
   "Skip": false,
   "JobId": "fj1c33ro168****"
```

`},` `{`

```json
   "Sub": [],
   "BootTime": "2021-03-16T08:01:34.000+00:00",
   "Logs": [],
   "Names": "CHECK_TOPOLOGY_DETAIL",
   "Item": "CHECK_TOPOLOGY",
   "CanSkip": true,
   "DelaySeconds": 0,
   "FinishTime": "2021-03-16T08:01:35.000+00:00",
   "OrderNum": 220,
   "IgnoreFlag": "N",
   "State": "Success",
   "Skip": false,
   "JobId": "fj1c33ro168****"
```

`}` `]` `}`

##### 1.4.8.5 WhiteIpList

Queries the CIDR blocks of Data Transmission Service (DTS) servers. If the **source or destination instance** is a **self-managed database** or a **third-party cloud database**, you must call this operation to query the CIDR blocks of DTS servers. Then, you need to add the CIDR blocks of DTS servers to the firewall security settings of the source or destination instance. If the **source or destination database** is an **ApsaraDB database instance** (such as RDS instance and ApsaraDB for MongoDB instance) or a **self-**
**managed database hosted on Elastic Compute Service (ECS)**, you do not need to add the CIDR blocks. When you click **Set Whitelist and**
**Next** in the DTS console, DTS automatically adds the CIDR blocks of DTS servers to the security settings of the source or destination instance.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | WhiteIpList | The operation that you want to perform. Set the value to WhiteIpList. |
| Region | String | Yes | cn-hangzhou | The region ID of the source instance. Note If the source instance is a self-managed database with a public IP address or a third-party cloud database, you can set the parameter to cn-hangzhou or the ID of the closest region. |
| Type | String | Yes | vpc | Specifies how the self-managed database or third-party cloud database is connected to DTS. Valid values: internet: The database is connected to DTS over the Internet. vpc: The database is connected to DTS over Express Connect, VPN Gateway, or Smart Access Gateway. |
| DestinationRegion | String | No | cn-hangzhou | The region ID of the destination instance. Note If the destination instance is a self-managed database with a public IP address or a third-party cloud database, you can set the parameter to cn- hangzhou or the ID of the closest region. If the DTS task is a data migration or data synchronization task, this parameter is required. |
| RegionId | String | No | cn-hangzhou | The region ID of the DTS instance. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| DynamicCode | String | 403 | The dynamic error code. This parameter will be removed in the future. |

| DynamicMessage | String | Type | The dynamic part in the error message. The value of this parameter is used to replace the %s variable in the value of the ErrMessage parameter. |
|---|---|---|---|
| ErrCode | String | InternalError | The error code returned if the call failed. |
| ErrMessage | String | The Value of Input Parameter %s is not valid. | The error message returned if the call failed. |
| HttpStatusCode | Integer | 200 | The HTTP status code. |
| IpList | String | 10.151.12.0/24,47.102.181.0/24, 47.101.109.0/24,120.55.129.0/24 ,11.115.103.0/24,47.102.234.0/2 4 | The CIDR blocks of DTS servers. Multiple CIDR blocks are separated by commas (,). |
| RequestId | String | AD823BD3-1BA6-4117-A536- 165CB280**** | The ID of the request. |
| Success | Boolean | true | Indicates whether the call was successful. Valid values: true: The call was successful. false: The call failed. |

**Examples**

Sample requests

```
http(s)://dts.aliyuncs.com/?Action=WhiteIpList &Region=cn-hangzhou &Type=vpc &DestinationRegion=cn-hangzhou &<Common request parameters>
```

Sample success responses

| XML | format |
|---|---|
| <WhiteIpListResponse> <RequestId>AD823BD3-1BA6-4117-A536-165CB280****</RequestId> <HttpStatusCode>200</HttpStatusCode> <Success>true</Success> <IpList>10.151.12.0/24,47.102.181.0/24,47.101.109.0/24,120.55.129.0/24,11.115.103.0/24,47.102.234.0/24</IpList> </WhiteIpListResponse> |   |

| JSON | format |
|---|---|
| { "RequestId":"AD823BD3-1BA6-4117-A536-165CB280****", "HttpStatusCode":200, "Success":true, "IpList": "10.151.12.0/24,47.102.181.0/24,47.101.109.0/24,120.55.129.0/24,11.115.103.0/24,47.102.234.0/24" } |   |

##### 1.4.8.6 DescribeSubscriptionMeta

Queries the details of the subtasks in a distributed change tracking task for a PolarDB-X 1.0 instance. When Data Transmission Service (DTS) tracks data changes from a PolarDB-X 1.0 instance, data is distributed across the attached ApsaraDB RDS for MySQL instances. DTS runs a subtask for each ApsaraDB RDS for MySQL instance. You can call this operation to query the details of the subtasks in a distributed change tracking task. You can call the DescribeDtsJobs operation to query the ID of the change tracking instance and the ID of the consumer group.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeSubscriptionMeta | The operation that you want to perform. Set the value to DescribeSubscriptionMeta. |
| Sid | String | Yes | z38m91gg2****** | The ID of the consumer group. |
| DtsInstanceId | String | No | dtsbr4m9luv2****** | The ID of the distributed change tracking instance. |

| SubMigrationJobIds | Json | No | z38m91gg2****** | The IDs of all subtasks in the distributed change tracking task. Separate multiple subtask IDs with commas (,). Note You must specify at least one of the SubMigrationJobIds and Topics parameters. We recommend that you specify the SubMigrationJobIds parameter. |
|---|---|---|---|---|
| Topics | Json | No | cnhangzhourmbp1n0x0x5 _ _ _ tz******dtstestdataversion2 _ _ | The topics of all subtasks in the distributed change tracking task. Separate multiple topics with commas (,). Note You must specify at least one of the SubMigrationJobIds and Topics parameters. We recommend that you specify the SubMigrationJobIds parameter. |
| RegionId | String | No | cn-hangzhou | The region ID of the change tracking instance. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| ErrCode | String | InternalError | The error code returned if the call failed. |
| ErrMessage | String | The Value of Input Parameter %s is not valid. | The error message returned if the call failed. |
| HttpStatusCode | String | 200 | The HTTP status code. |
| RequestId | String | C12E7A51-09A4-5796-94BE- 08B6DA****** | The ID of the request. |
| SubscriptionMetaList | Array of SubscriptionMetaList |   | The details of the subtasks. |
| Checkpoint | Long | 1610524452 | The consumer offset of the subtask. It is a UNIX timestamp that is generated when the client consumes the first data record. Note You can use a search engine to obtain a UNIX timestamp converter. |
| DBList | String | {\"dtstestdata\": {\"name\":\"dtstestdata\",\"all\":f alse,\"Table\":{\"order\": {\"name\":\"order\",\"all\":true}} }} | The objects of the subtask. |
| DProxyUrl | String | dts-cn- hangzhou.aliyuncs.com:18001 | The endpoint and port number of the change tracking instance. |
| Sid | String | z38m91gg2****** | The consumer group ID of the subtask. |
| Topic | String | cnhangzhourmbp1n0x0x5tz*** _ _ _ ***dtstestdataversion2 _ _ | The topic of the subtask. |
| Success | String | true | Indicates whether the call was successful. |

**Examples**

Sample requests

```
http(s)://dts.aliyuncs.com/?Action=DescribeSubscriptionMeta &Sid=z38m91gg2****** &DtsInstanceId=dtsbr4m9luv2****** &SubMigrationJobIds=z38m91gg2****** &RegionId=cn-hangzhou &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeSubscriptionMetaResponse>
      <SubscriptionMetaList>
            <Checkpoint>1610524452</Checkpoint>
            <DBList>{\"dtstestdata\":{\"name\":\"dtstestdata\",\"all\":false,\"Table\":{\"order\":{\"name\":\"order\",\"all\":true}}}}</DBList>
            <DProxyUrl>dts-cn-hangzhou.aliyuncs.com:18001</DProxyUrl>
            <Topic>cn_hangzhou_rm_bp1n0x0x5tz******_dtstestdata_version2</Topic>
            <Sid>z38m91gg2******</Sid>
      </SubscriptionMetaList>
      <RequestId>C12E7A51-09A4-5796-94BE-08B6DA******</RequestId>
      <HttpStatusCode>200</HttpStatusCode>
      <Success>true</Success>
</DescribeSubscriptionMetaResponse>
```

| JSON | format |
|---|---|
| { "SubscriptionMetaList": [ { "Checkpoint": "1610524452", "DBList": "{\\\"dtstestdata\\\":{\\\"name\\\":\\\"dtstestdata\\\",\\\"all\\\":false,\\\"Table\\\":{\\\"order\\\": {\\\"name\\\":\\\"order\\\",\\\"all\\\":true}}}}", "DProxyUrl": "dts-cn-hangzhou.aliyuncs.com:18001", "Topic": "cn_hangzhou_rm_bp1n0x0x5tz******_dtstestdata_version2", "Sid": "z38m91gg2******" } ], "RequestId": "C12E7A51-09A4-5796-94BE-08B6DA*******", "HttpStatusCode": "200", "Success": "true" } |   |

#### 1.4.9 Modify DTS tasks

##### 1.4.9.1 ModifyDtsJob

Modifies the configurations of a data synchronization task.

**Request parameters**

| Parameter | Type | Position | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | String | Query | No | cn-hangzhou | The ID of the region in which the data synchronization instance resides. |
| DtsInstanceId | String | Query | Yes | dtsbi6e22ay243**** | The data synchronization instance ID. |
| SynchronizationDire ction | String | Query | No | Forward | The synchronization direction. Valid values: Forward Reverse Note Default value: Forward. This parameter is required only if the topology of the data synchronization instance is two-way synchronization. |
| ClientToken | String | Query | No | 0c593ea1-3bea-11e9-b96b-88e9fe63**** | The client token that is used to ensure the idempotence of the request. You can use the client to generate a client token. Make sure that a unique client token is used for each request. The ClientToken parameter can contain only ASCII characters and cannot exceed 64 characters in length. |
| AccessKeyId | String | Query | No | LTAI******************** | The AccessKey ID that is used to access services. |

| DbList | String | Body | No | {"dtstest":{"name":"dtstest","all":true}} | The objects of the data synchronization task after modification. Note Before you call the ModifyDtsJob operation, we recommend that you call the DescribeDtsJobDetail operation to query the current objects of the data synchronization task. Then, you can specify the new objects based on your business requirements. For example, if the current objects are Table A and Table B and you need to add Table C, you must specify Table A, Table B, and Table C for this parameter. |
|---|---|---|---|---|---|
| EtlOperatorColumn Reference | String | Body | No | { "configKeyMap": [ { "moduleCode": "03", "etlOperatorColumnReference": "etlOperatorColumnReference", "etlOperatorSetting": "etlOperatorSetting" }, { "moduleCode": "07", "etlOperatorColumnReference": "etlOperatorColumnReference", "etlOperatorSetting": "etlOperatorSetting" } ], "amp.increment.replicator.compare.all.colu mns.enable": false, "srcNetType": "VPC", "etlOperatorColumnReference": { "MODIFYTIME": [ _ { "datasynchron.testtiminguser000": _ _ _ "usercreatedate" _ _ }, { "datasynchron.testtiminguser001": _ _ _ "usercreatedate" _ _ }, { "datasynchron.testtiminguser002": _ _ _ "usercreatedate" _ _ }, { "datasynchron.testtiminguser003": _ _ _ "usercreatedate" _ _ } ] }, "destNetType": "VPC", "originalSrcDbInst": "sg-sit-db2- primary.mysql.polardb.rds.aliyuncs.com", "etlOperatorSetting": "adbtimetravel", _ _ "sjobUseJobTask": "1", "srcVpcNetMappingInst": "172.19.XXX.XXX:4261", "destVpcNetMappingInst": "172.19.XXX.XXX:4260", "useJobTask": "1" } | The operator that is related to the extract, transform, and load (ETL) feature and dedicated to T+1 business. |

**Response parameters**

| Parameter | Type | Examples | Description |
|---|---|---|---|
| DtsJobId | String | bi6e22a**** | The DTS task ID. |

| ErrCode | String | InternalError | The error code returned if the request failed. |
|---|---|---|---|
| ErrMessage | Boolean | true | The error message returned if the request failed. Note The data type of this parameter is String. Example: The request processing has failed due to some unknown error. |
| RequestId | String | 1D6ECADF-C5E9-4C96-8811- 77602B31**** | The request ID. |
| Status | String | 200 | The HTTP status code. |
| Success | Boolean | true | Indicates whether the request was successful. |

**Examples**

Sample requests

```
http(s)://dts.aliyuncs.com/?Action=ModifyDtsJob &DtsInstanceId=dtsbi6e22ay243**** &DbList={"dtstest":{"name":"dtstest","all":true}} &<Common request parameters>
```

Sample success responses

| JSON | format |
|---|---|
| { "Status":"200", "DtsJobId":"bi6e22a****", "RequestId":"1D6ECADF-C5E9-4C96-8811-77602B31****", "Success":true } |   |

| XML | format |
|---|---|
| <Status>200</Status> <DtsJobId>bi6e22a****</DtsJobId> <RequestId>1D6ECADF-C5E9-4C96-8811-77602B31****</RequestId> <Success>true</Success> |   |

##### 1.4.9.2 ModifySubscription

Modifies the objects of a change tracking task and the types of data changes to be tracked.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifySubscription | The operation that you want to perform. Set the value to ModifySubscription. |
| DbList | String | Yes | {"dtstest": {"name":"dtstest","all":true} } | The objects of the change tracking task after modification. The value is a JSON string. Note You can call the DescribeDtsJobDetail operation to query the original objects of the task. |
| DtsInstanceId | String | Yes | dtsboss6pn1w****** | The ID of the change tracking instance. You can call the DescribeDtsJobs operation to query the instance ID. |
| DtsJobId | String | Yes | boss6pn1w****** | The ID of the change tracking task. You can call the DescribeDtsJobs operation to query the task ID. |
| SubscriptionDataTypeDDL | Boolean | Yes | true | Specifies whether to track DDL statements. Valid values: true: yes false: no |
| SubscriptionDataTypeDML | Boolean | Yes | true | Specifies whether to track DML statements. Valid values: true: yes false: no |
| RegionId | String | No | cn-hangzhou | The region ID of the Data Transmission Service (DTS) instance. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| ErrCode | String | InternalError | The error code returned if the call failed. |
| ErrMessage | String | The request processing has failed due to some unknown error. | The error message returned if the call failed. |
| HttpStatusCode | String | 200 | The HTTP status code. |
| RequestId | String | 068FA72F-4800-4A54-90BB- 94806068**** | The ID of the request. |
| Success | String | true | Indicates whether the call was successful. |

**Examples**

Sample requests

```
http(s)://dts.aliyuncs.com/?Action=ModifySubscription &DbList={"dtstest":{"name":"dtstest","all":true}} &DtsInstanceId=dtsboss6pn1w****** &DtsJobId=boss6pn1w****** &SubscriptionDataTypeDDL=true &SubscriptionDataTypeDML=true
```

Sample success responses

| XML | format |
|---|---|
| <ModifySubscriptionResponse> <RequestId>068FA72F-4800-4A54-90BB-94806068****</RequestId> <HttpStatusCode>200</HttpStatusCode> <Success>true</Success> </ModifySubscriptionResponse> |   |

| JSON | format |
|---|---|
| { "RequestId": "068FA72F-4800-4A54-90BB-94806068****", "HttpStatusCode": 200, "Success": true } |   |

##### 1.4.9.3 ModifyDtsJobPassword

Changes the password of the source or destination database account.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyDtsJobPassword | The operation that you want to perform. Set the value to ModifyDtsJobPassword. |
| DtsJobId | String | Yes | l3m1213ye7l**** | The ID of the data migration, data synchronization, or change tracking task. |
| Endpoint | String | No | src | The database to which the password belongs. Valid values: src: source database dest: destination database Note This parameter is required. |
| UserName | String | No | dtstest | The account of the source or destination database. Note This parameter is required. |
| Password | String | No | Test123456 | The password of the account after change. Note This parameter is required and cannot be the same as the current password. |
| RegionId | String | No | cn-hangzhou | The region where the Data Transmission Service (DTS) instance resides. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Code | String | 200 | The error code. This parameter will be removed in the future. |
| DynamicMessage | String | DtsJobId | The dynamic part in the error message. The value of this parameter is used to replace the %s variable in the value of the ErrMessage parameter. Note If the return value of the ErrMessage parameter is The Value of Input Parameter %s is not valid and the return value of the DynamicMessage parameter is DtsJobId, the specified DtsJobId parameter is invalid. |
| ErrCode | String | InternalError | The error code returned if the call failed. |
| ErrMessage | String | The Value of Input Parameter %s is not valid. | The error message returned if the call failed. |
| HttpStatusCode | Integer | 200 | The HTTP status code. |
| RequestId | String | 8C498360-7892-433C-847A- BA71A850**** | The ID of the request. |
| Success | Boolean | true | Indicates whether the call was successful. |

**Examples**

Sample requests

```
http(s)://dts.aliyuncs.com/?Action=ModifyDtsJobPassword &DtsJobId=l3m1213ye7l**** &Endpoint=src &UserName=dtstest &Password=Test123456 &<Common request parameters>
```

Sample success responses

| XML | format |
|---|---|
| <ModifyDtsJobPasswordResponse> <RequestId>8C498360-7892-433C-847A-BA71A850****</RequestId> <HttpStatusCode>200</HttpStatusCode> <Success>true</Success> </ModifyDtsJobPasswordResponse> |   |

| JSON | format |
|---|---|
| { "RequestId": "8C498360-7892-433C-847A-BA71A850****", "HttpStatusCode": 200, "Success": true } |   |

##### 1.4.9.4 ModifyDtsJobName

Changes the name of a Data Transmission Service (DTS) task.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyDtsJobName | The operation that you want to perform. Set the value to ModifyDtsJobName. |
| DtsJobId | String | Yes | l3m1213ye7l**** | The ID of the data migration, data synchronization, or change tracking task. |
| DtsJobName | String | No | RDSTORDSMIGRATION _ _ _ | The DTS task name after modification. Note This parameter is required. We recommend that you specify a descriptive name that makes it easy to identify. You do not need to use a unique task name. |
| RegionId | String | No | cn-beijing | The region ID of the DTS task. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Code | String | 200 | The error code. This parameter will be removed in the future. |
| DynamicMessage | String | DtsJobId | The dynamic part in the error message. The value of this parameter is used to replace the %s variable in the value of the ErrMessage parameter. Note If the return value of the ErrMessage parameter is The Value of Input Parameter %s is not valid and the return value of the DynamicMessage parameter is DtsJobId, the specified DtsJobId parameter is invalid. |
| ErrCode | String | InternalError | The error code returned if the call failed. |
| ErrMessage | String | The Value of Input Parameter %s is not valid. | The error message returned if the call failed. |
| HttpStatusCode | Integer | 200 | The HTTP status code. |
| RequestId | String | 8C498360-7892-433C-847A- BA71A850**** | The ID of the request. |
| Success | Boolean | true | Indicates whether the call was successful. |

**Examples**

Sample requests

```
http(s)://dts.aliyuncs.com/?Action=ModifyDtsJobName &DtsJobId=l3m1213ye7l**** &DtsJobName=RDS_TO_RDS_MIGRATION &<Common request parameters>
```

Sample success responses

| XML | format |
|---|---|
| <ModifyDtsJobNameResponse> <RequestId>8C498360-7892-433C-847A-BA71A850****</RequestId> <HttpStatusCode>200</HttpStatusCode> <Success>true</Success> </ModifyDtsJobNameResponse> |   |

| JSON | format |
|---|---|
| { "RequestId": "8C498360-7892-433C-847A-BA71A850****", "HttpStatusCode": 200, "Success": true } |   |

##### 1.4.9.5 UpgradeTwoWay

Upgrades the synchronization topology of a data synchronization instance from one-way synchronization to two-way synchronization. This operation is supported only for pay-as-you-go data synchronization instances. When you call this operation, take note of the following items: The source and destination databases of the data synchronization task are both **MySQL** databases. The synchronization topology of the data synchronization task is **one-way synchronization**. The data synchronization task is in the **Synchronizing** state. The upgrade operation causes data synchronization latency of about 5 seconds. We recommend that you perform this operation during off-peak hours.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | UpgradeTwoWay | The operation that you want to perform. Set the value to UpgradeTwoWay. |
| InstanceClass | String | Yes | large | The instance class of the two-way synchronization task. Valid values: large, medium, micro, and small. |
| InstanceId | String | Yes | dtsh77p49x4k28**** | The ID of the data synchronization instance. You can call the DescribeDtsJobs operation to query the instance ID. |
| RegionId | String | No | cn-hangzhou | The region ID of the Data Transmission Service (DTS) instance. For more information, see List of supported regions. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| DynamicCode | String | 403 | The dynamic error code. This parameter will be removed in the future. |
| DynamicMessage | String | InstanceId | The dynamic part in the error message. The value of this parameter is used to replace the %s variable in the value of the ErrMessage parameter. Note If the return value of the ErrMessage parameter is The Value of Input Parameter %s is not valid and that of the DynamicMessage parameter is InstanceId, the specified InstanceId parameter is invalid. |
| ErrCode | String | InternalError | The error code returned if the call failed. |
| ErrMessage | String | The Value of Input Parameter %s is not valid. | The error message returned if the call failed. |
| HttpStatusCode | Integer | 200 | The HTTP status code. |
| RequestId | String | 2D3B4615-923F-49AA-AF21- 6D8E3967**** | The ID of the request. |
| Success | Boolean | true | Indicates whether the call was successful. Valid values: true: The call was successful. false: The call failed. |

**Examples**

Sample requests

```
http(s)://dts.aliyuncs.com/?Action=UpgradeTwoWay &InstanceClass=large &InstanceId=dtsh77p49x4k28**** &<Common request parameters>
```

Sample success responses

| XML | format |
|---|---|
| <StartDtsJobResponse> <RequestId>2D3B4615-923F-49AA-AF21-6D8E3967****</RequestId> <HttpStatusCode>200</HttpStatusCode> <Success>true</Success> </StartDtsJobResponse> |   |

| JSON | format |
|---|---|
| { "RequestId":"2D3B4615-923F-49AA-AF21-6D8E3967****", "HttpStatusCode":200, "Success":true } |   |

##### 1.4.9.6 TransferPayType

Changes the billing method or instance class of a Data Transmission Service (DTS) task. The billing method of subscription instances cannot be changed to pay-as-you-go. To prevent resource waste, determine whether you need to change the billing method of your resources. Data migration instances are all pay-as-you-go instances. You do not need to change the billing method of data migration instances. After you change the billing method from pay-as-you-go to subscription, the DTS instance is not affected.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | TransferPayType | The operation that you want to perform. Set the value to TransferPayType. |

| ChargeType | String | Yes | PostPaid | The billing method after change. Valid values: PrePaid: subscription PostPaid: pay-as-you-go Note The billing method of subscription instances cannot be changed to pay-as-you-go. To prevent resource waste, determine whether you need to change the billing method of your resources. If you do not need to change the billing method, specify the current billing method. |
|---|---|---|---|---|
| DtsJobId | String | Yes | o4nh3g7jg56**** | The ID of the data migration, data synchronization, or change tracking task. You can call the DescribeDtsJobs operation to query the task ID. |
| Period | String | No | Year | The billing cycle of the subscription instance. Valid values: Year Month Note This parameter is required only if you set the ChargeType parameter to PrePaid. |
| BuyCount | String | No | 5 | The subscription duration. Valid values when the Period parameter is set to Year: 1 to 5. Valid values when the Period parameter is set to Month: 1 to 60. Note This parameter is required only if you set the ChargeType parameter to PrePaid. |
| RegionId | String | No | cn-hangzhou | The region ID of the DTS instance. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| ChargeType | String | PostPaid | The billing method after change. Valid values: PrePaid: subscription PostPaid: pay-as-you-go |
| Code | String | 200 | The error code. This parameter will be removed in the future. |
| DtsJobId | String | o4nh3g7jg56**** | The ID of the task. |
| DynamicMessage | String | DtsJobId | The dynamic part in the error message. The value of this parameter is used to replace the %s variable in the value of the ErrMessage parameter. Note If the return value of the ErrMessage parameter is The Value of Input Parameter %s is not valid and the return value of the DynamicMessage parameter is DtsJobId, the specified DtsJobId parameter is invalid. |
| EndTime | String | 1614916318 | The expiration time of the subscription instance. The value is a UNIX timestamp. Note If the billing method of the DTS instance is changed to pay- as-you-go, the value of this parameter is empty. You can use a search engine to obtain a UNIX timestamp converter. |
| ErrCode | String | InternalError | The error code returned if the call failed. |
| ErrMessage | String | The Value of Input Parameter %s is not valid. | The error message returned if the call failed. |
| HttpStatusCode | Integer | 200 | The HTTP status code. |

| InstanceId | String | dtso4nh3g7jg56**** | The ID of DTS instance. |
|---|---|---|---|
| RequestId | String | 601B6F25-21E7-4484-99D5- 3EF2625C**** | The ID of the request. |
| Success | Boolean | true | Indicates whether the call was successful. Valid values: true: The call was successful. false: The call failed. |

**Examples**

Sample requests

```
http(s)://dts.aliyuncs.com/?Action=TransferPayType &ChargeType=PostPaid &DtsJobId=o4nh3g7jg56**** &Period=Year &BuyCount=5 &<Common request parameters>
```

Sample success responses

| XML | format |
|---|---|
| <TransferPayTypeResponse> <DtsJobId>o4nh3g7jg56****</DtsJobId> <RequestId>601B6F25-21E7-4484-99D5-3EF2625C****</RequestId> <InstanceId>dtso4nh3g7jg56****</InstanceId> <ChargeType>PostPaid</ChargeType> <HttpStatusCode>200</HttpStatusCode> <Success>true</Success> </TransferPayTypeResponse> |   |

| JSON | format |
|---|---|
| { "DtsJobId": "o4nh3g7jg56****", "RequestId": "601B6F25-21E7-4484-99D5-3EF2625C****", "InstanceId": "dtso4nh3g7jg56****", "ChargeType": "PostPaid", "HttpStatusCode": 200, "Success": true } |   |

##### 1.4.9.7 TransferInstanceClass

Upgrades or downgrades a Data Transmission Service (DTS) instance.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | TransferInstanceClass | The operation that you want to perform. Set the value to TransferInstanceClass. |
| DtsJobId | String | Yes | r4yr723m199**** | The ID of the data migration or data synchronization task. You can call the DescribeDtsJobs operation to query the task ID. |
| InstanceClass | String | Yes | large | The new instance class of the DTS instance. You can call the DescribeDtsJobDetail operation to query the original instance class of the DTS instance. DTS supports the following instance classes for a data migration instance: xxlarge, xlarge, large, medium, and small. DTS supports the following instance classes for a data synchronization instance: large, medium, small, and micro. |
| OrderType | String | Yes | UPGRADE | Specifies whether to upgrade or downgrade the DTS instance. Valid values: UPGRADE DOWNGRADE |
| RegionId | String | No | cn-hangzhou | The region ID of the DTS instance. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|

| ChargeType | String | POSTPAY | The billing method of the DTS instance. Valid values: POSTPAY: pay-as-you-go PREPAY: subscription |
|---|---|---|---|
| Code | String | 200 | The error code returned if the task failed. |
| DtsJobId | String | r4yr723m199**** | The ID of the data migration or data synchronization task. |
| DynamicMessage | String | DtsJobId | The dynamic part in the error message. This parameter is used to replace the %s variable in the ErrMessage parameter. Note If the return value of the ErrMessage parameter is The Value of Input Parameter %s is not valid and the return value of the DynamicMessage parameter is DtsJobId, the specified DtsJobId parameter is invalid. |
| EndTime | String | 2021-08-04T16:00:00.000+00:00 | The expiration time of the DTS instance. Note This parameter is returned only if the ChargeType parameter is set to PREPAY. |
| ErrCode | String | InternalError | The error code returned if the call failed. |
| ErrMessage | String | The request processing has failed due to some unknown error. | The error message returned if the call failed. |
| HttpStatusCode | Integer | 200 | The HTTP status code. |
| InstanceId | String | dtsr4yr723m199**** | The ID of DTS instance. |
| RequestId | String | 716DB03E-2D0B-4DC3-BC4C- F7A9EE21**** | The ID of the request. |
| Success | Boolean | true | Indicates whether the call was successful. Valid values: true: The call was successful. false: The call failed. |

**Examples**

Sample requests

```
http(s)://dts.aliyuncs.com/?Action=TransferInstanceClass &OrderType=UPGRADE &InstanceClass=large &DtsJobId=r4yr723m199**** &<Common request parameters>
```

Sample success responses

| XML | format |
|---|---|
| <TransferInstanceClassResponse> <DtsJobId>r4yr723m199****</DtsJobId> <RequestId>716DB03E-2D0B-4DC3-BC4C-F7A9EE21****</RequestId> <InstanceId>dtsr4yr723m199****</InstanceId> <ChargeType>POSTPAY</ChargeType> <HttpStatusCode>200</HttpStatusCode> <Success>true</Success> </TransferInstanceClassResponse> |   |

| JSON | format |
|---|---|
| { "DtsJobId": "r4yr723m199****", "RequestId": "716DB03E-2D0B-4DC3-BC4C-F7A9EE21****", "InstanceId": "dtsr4yr723m199****", "ChargeType": "POSTPAY", "HttpStatusCode": 200, "Success": true } |   |

##### 1.4.9.8 RenewInstance

Renews a Data Transmission Service (DTS) instance. This API operation is available only for subscription instances.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|

| Action | String | Yes | RenewInstance | The operation that you want to perform. Set the value to RenewInstance. |
|---|---|---|---|---|
| ChargeType | String | Yes | PREPAY | The billing method of the DTS instance. Set the value to PREPAY, which indicates the subscription billing method. |
| DtsJobId | String | Yes | qi0r643lc31**** | The ID of the data synchronization or change tracking task. You can call the DescribeDtsJobs operation to query the task ID. |
| Period | String | No | Month | The billing cycle of the subscription instance. Default value: Month. Valid values: Year Month |
| BuyCount | String | No | 1 | The subscription duration. Valid values when the Period parameter is set to Year: 1 to 5. Valid values when the Period parameter is set to Month: 1 to 60. |
| RegionId | String | No | cn-hangzhou | The region ID of the DTS instance. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| ChargeType | String | PREPAY | The billing method of the DTS instance. PREPAY is returned, which indicates the subscription billing method. |
| Code | String | 200 | The error code returned if the task failed. Note This parameter will be removed in the future. |
| DtsJobId | String | qi0r643lc31**** | The ID of the data synchronization or change tracking task. |
| DynamicMessage | String | DtsJobId | The dynamic part in the error message. This parameter is used to replace the %s variable in the ErrMessage parameter. Note If the return value of the ErrMessage parameter is The Value of Input Parameter %s is not valid and the return value of the DynamicMessage parameter is DtsJobId, the specified DtsJobId parameter is invalid. |
| EndTime | String | 2021-08-04T16:00:00.000+00:00 | The expiration time of the renewed instance. |
| ErrCode | String | InternalError | The error code returned if the call failed. |
| ErrMessage | String | The request processing has failed due to some unknown error. | The error message returned if the call failed. |
| HttpStatusCode | Integer | 200 | The HTTP status code. |
| InstanceId | String | dtsqi0r643lc31**** | The ID of DTS instance. |
| RequestId | String | 1112E255-0C38-4970-8159- 1D54AD92**** | The ID of the request. |
| Success | Boolean | true | Indicates whether the call was successful. Valid values: true: The call was successful. false: The call failed. |

**Examples**

Sample requests

```
http(s)://dts.aliyuncs.com/?Action=RenewInstance &ChargeType=PREPAY &DtsJobId=qi0r643lc31**** &Period=Month &BuyCount=1
```

```xml
<RenewInstanceResponse>
  <DtsJobId>qi0r643lc31****</DtsJobId>
  <EndTime>2021-08-04T16:00:00.000+00:00</EndTime>
  <RequestId>1112E255-0C38-4970-8159-1D54AD92****</RequestId>
  <InstanceId>dtsqi0r643lc31****</InstanceId>
  <ChargeType>PREPAY</ChargeType>
  <HttpStatusCode>200</HttpStatusCode>
  <Success>true</Success>
</RenewInstanceResponse>
```

| JSON | format |
|---|---|
| { "DtsJobId": "qi0r643lc31****", "EndTime": "2021-08-04T16:00:00.000+00:00", "RequestId": "1112E255-0C38-4970-8159-1D54AD92****", "InstanceId": "dtsqi0r643lc31****", "ChargeType": "PREPAY", "HttpStatusCode": 200, "Success": true } |   |

#### 1.4.10 ResetDtsJob

Reconfigures a data synchronization or change tracking task.

> **Note:** If you clear the configurations of a data synchronization or change tracking task, Data Transmission Service (DTS) deletes the task. Then, DTS creates another task. You must call the ConfigureDtsJob operation to configure the new task.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ResetDtsJob | The operation that you want to perform. Set the value to ResetDtsJob. |
| DtsJobId | String | Yes | l3m1213ye7l**** | The ID of the data synchronization or change tracking task. |
| DtsInstanceId | String | No | dtsl3m1213ye7l**** | The ID of the data synchronization or change tracking instance. |
| SynchronizationDirection | String | No | Forward | The synchronization direction. Valid values: Forward: Data is synchronized from the source database to the destination database. Reverse: Data is synchronized from the destination database to the source database. Note The default value is Forward. You can set this parameter to Reverse to reconfigure the reverse synchronization task only when the topology is two-way synchronization. |
| RegionId | String | No | cn-hangzhou | The region where the DTS instance resides. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| DynamicCode | String | 403 | The dynamic error code. This parameter will be removed in the future. |
| DynamicMessage | String | DtsJobId | The dynamic part in the error message. The value of this parameter is used to replace the %s variable in the value of the ErrMessage parameter. Note If the return value of the ErrMessage parameter is The Value of Input Parameter %s is not valid and the return value of the DynamicMessage parameter is DtsJobId, the specified DtsJobId parameter is invalid. |
| ErrCode | String | InternalError | The error code returned if the call failed. |
| ErrMessage | String | The Value of Input Parameter %s is not valid. | The error message returned if the call failed. |
| HttpStatusCode | Integer | 200 | The HTTP status code. |

| RequestId | String | 01B6F25-21E7-4484-99D5- 3EF2625C**** | The ID of the request. |
|---|---|---|---|
| Success | Boolean | true | Indicates whether the call was successful. |

**Examples**

Sample requests

```
http(s)://dts.aliyuncs.com/?Action=ResetDtsJob &DtsJobId=l3m1213ye7l**** &<Common request parameters>
```

Sample success responses

| XML | format |
|---|---|
| <ResetDtsJobResponse> <RequestId>01B6F25-21E7-4484-99D5-3EF2625C****</RequestId> <HttpStatusCode>200</HttpStatusCode> <Success>true</Success> </ResetDtsJobResponse> |   |

| JSON | format |
|---|---|
| { "RequestId":"01B6F25-21E7-4484-99D5-3EF2625C****", "HttpStatusCode":200, "Success":true } |   |

#### 1.4.11 SuspendDtsJob

Pauses a data migration, data synchronization, or change tracking task.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | SuspendDtsJob | The operation that you want to perform. Set the value to SuspendDtsJob. |
| DtsJobId | String | Yes | l3m1213ye7l**** | The ID of the data migration, data synchronization, or change tracking task. |
| DtsInstanceId | String | No | dtsl3m1213ye7l**** | The ID of the data migration, data synchronization, or change tracking instance. |
| SynchronizationDirection | String | No | Forward | The synchronization direction. Valid values: Forward: Data is synchronized from the source database to the destination database. Reverse: Data is synchronized from the destination database to the source database. Note The default value is Forward. You can set this parameter to Reverse to pause the reverse synchronization task only if the topology is two-way synchronization. |
| RegionId | String | No | cn-hangzhou | The region ID of the Data Transmission Service (DTS) instance. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| DynamicCode | String | 403 | The dynamic error code. This parameter will be removed in the future. |
| DynamicMessage | String | DtsJobId | The dynamic part in the error message. The value of this parameter is used to replace the %s variable in the value of the ErrMessage parameter. Note If the return value of the ErrMessage parameter is The Value of Input Parameter %s is not valid and the return value of the DynamicMessage parameter is DtsJobId, the specified DtsJobId parameter is invalid. |
| ErrCode | String | InternalError | The error code returned if the call failed. |

| ErrMessage | String | The Value of Input Parameter %s is not valid. | The error message returned if the call failed. |
|---|---|---|---|
| HttpStatusCode | Integer | 200 | The HTTP status code. |
| RequestId | String | 01B6F25-21E7-4484-99D5- 3EF2625C**** | The ID of the request. |
| Success | Boolean | true | Indicates whether the call was successful. |

**Examples**

Sample requests

```
http(s)://dts.aliyuncs.com/?Action=SuspendDtsJob &DtsJobId=l3m1213ye7l**** &<Common request parameters>
```

Sample success responses

| XML | format |
|---|---|
| <SuspendDtsJobResponse> <RequestId>01B6F25-21E7-4484-99D5-3EF2625C****</RequestId> <HttpStatusCode>200</HttpStatusCode> <Success>true</Success> </SuspendDtsJobResponse> |   |

| JSON | format |
|---|---|
| { "RequestId":"01B6F25-21E7-4484-99D5-3EF2625C****", "HttpStatusCode":200, "Success":true } |   |

#### 1.4.12 SuspendDtsJobs

Suspends multiple Data Transmission Service (DTS) tasks.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | SuspendDtsJobs | The operation that you want to perform. Set the value to SuspendDtsJobs. |
| DtsJobIds | String | Yes | hfi12iv4z7e**** | The ID of the data migration or data synchronization task. Note Separate multiple task IDs with commas (,). You can call the DescribeDtsJobs operation to query task IDs. |
| RegionId | String | No | cn-hangzhou | The region ID of the DTS instance. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| DynamicCode | String | 403 | The dynamic error code. This parameter will be removed in the future. |
| DynamicMessage | String | DtsJobId | The dynamic part in the error message. The value of this parameter is used to replace the %s variable in the value of the ErrMessage parameter. Note If the return value of the ErrMessage parameter is The Value of Input Parameter %s is not valid and the return value of the DynamicMessage parameter is DtsJobId, the specified DtsJobId parameter is invalid. |
| ErrCode | String | InternalError | The error code returned if the call failed. |
| ErrMessage | String | The Value of Input Parameter %s is not valid. | The error message returned if the call failed. |
| HttpStatusCode | Integer | 200 | The HTTP status code. |

| RequestId | String | AD823BD3-1BA6-4117-A536- 165CB280**** | The ID of the request. |
|---|---|---|---|
| Success | Boolean | true | Indicates whether the call was successful. |

**Examples**

Sample requests

```
http(s)://dts.aliyuncs.com/?Action=SuspendDtsJobs &DtsJobIds=hfi12iv4z7e**** &RegionId=cn-hangzhou &<Common request parameters>
```

Sample success responses

| XML | format |
|---|---|
| <StartDtsJobResponse> <RequestId>AD823BD3-1BA6-4117-A536-165CB280****</RequestId> <HttpStatusCode>200</HttpStatusCode> <Success>true</Success> </StartDtsJobResponse> |   |

| JSON | format |
|---|---|
| { "RequestId": "AD823BD3-1BA6-4117-A536-165CB280****", "HttpStatusCode": 200, "Success": true } |   |

#### 1.4.13 StopDtsJob

Stops a data migration, data synchronization, or change tracking task.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | StopDtsJob | The operation that you want to perform. Set the value to StopDtsJob. |
| DtsJobId | String | Yes | l3m1213ye7l**** | The ID of the data migration, data synchronization, or change tracking task. |
| DtsInstanceId | String | No | dtsl3m1213ye7l**** | The ID of the data migration, data synchronization, or change tracking instance. |
| SynchronizationDirection | String | No | Forward | The synchronization direction. Valid values: Forward: Data is synchronized from the source database to the destination database. Reverse: Data is synchronized from the destination database to the source database. Note The default value is Forward. You can set this parameter to Reverse to stop the reverse synchronization task only if the topology is two-way synchronization. |
| RegionId | String | No | cn-hangzhou | The region ID of the Data Transmission Service (DTS) instance. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| DynamicCode | String | 403 | The dynamic error code. This parameter will be removed in the future. |
| DynamicMessage | String | DtsJobId | The dynamic part in the error message. The value of this parameter is used to replace the %s variable in the value of the ErrMessage parameter. Note If the return value of the ErrMessage parameter is The Value of Input Parameter %s is not valid and the return value of the DynamicMessage parameter is DtsJobId, the specified DtsJobId parameter is invalid. |

| ErrCode | String | InternalError | The error code returned if the call failed. |
|---|---|---|---|
| ErrMessage | String | The Value of Input Parameter %s is not valid. | The error message returned if the call failed. |
| HttpStatusCode | Integer | 200 | The HTTP status code. |
| RequestId | String | 01B6F25-21E7-4484-99D5- 3EF2625C**** | The ID of the request. |
| Success | Boolean | true | Indicates whether the call was successful. |

**Examples**

Sample requests

```
http(s)://dts.aliyuncs.com/?Action=StopDtsJob &DtsJobId=l3m1213ye7l**** &<Common request parameters>
```

Sample success responses

| XML | format |
|---|---|
| <StopDtsJobResponse> <RequestId>01B6F25-21E7-4484-99D5-3EF2625C****</RequestId> <HttpStatusCode>200</HttpStatusCode> <Success>true</Success> </StopDtsJobResponse> |   |

| JSON | format |
|---|---|
| { "RequestId":"01B6F25-21E7-4484-99D5-3EF2625C****", "HttpStatusCode":200, "Success":true } |   |

#### 1.4.14 StopDtsJobs

Stops multiple data migration or data synchronization tasks.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | StopDtsJobs | The operation that you want to perform. Set the value to StopDtsJobs. |
| DtsJobIds | String | Yes | l5o11f9029c**** | The ID of the data migration or data synchronization task. Note Separate multiple task IDs with commas (,). You can call the DescribeDtsJobs operation to query task IDs. |
| RegionId | String | No | cn-hangzhou | The region ID of the DTS instance. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| DynamicCode | String | 403 | The dynamic error code. This parameter will be removed in the future. |
| DynamicMessage | String | DtsJobId | The dynamic part in the error message. The value of this parameter is used to replace the %s variable in the value of the ErrMessage parameter. Note If the return value of the ErrMessage parameter is The Value of Input Parameter %s is not valid and the return value of the DynamicMessage parameter is DtsJobId, the specified DtsJobId parameter is invalid. |
| ErrCode | String | InternalError | The error code returned if the call failed. |
| ErrMessage | String | The Value of Input Parameter %s is not valid. | The error message returned if the call failed. |

| HttpStatusCode | Integer | 200 | The HTTP status code. |
|---|---|---|---|
| RequestId | String | AD823BD3-1BA6-4117-A536- 165CB280**** | The ID of the request. |
| Success | Boolean | true | Indicates whether the call was successful. |

**Examples**

Sample requests

```
http(s)://dts.aliyuncs.com/?Action=StopDtsJobs &DtsJobIds=l5o11f9029c**** &RegionId=cn-hangzhou &<Common request parameters>
```

Sample success responses

| XML | format |
|---|---|
| <StopDtsJobResponse> <RequestId>AD823BD3-1BA6-4117-A536-165CB280****</RequestId> <HttpStatusCode>200</HttpStatusCode> <Success>true</Success> </StopDtsJobResponse> |   |

| JSON | format |
|---|---|
| { "RequestId": "AD823BD3-1BA6-4117-A536-165CB280****", "HttpStatusCode": 200, "Success": true } |   |

#### 1.4.15 DeleteDtsJob

Deletes a data migration, data synchronization, or change tracking task.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteDtsJob | The operation that you want to perform. Set the value to DeleteDtsJob. |
| DtsJobId | String | Yes | l3m1213ye7l**** | The ID of the data migration, data synchronization, or change tracking task. |
| DtsInstanceId | String | No | dtsl3m1213ye7l**** | The ID of the data migration, data synchronization, or change tracking instance. |
| SynchronizationDirection | String | No | Forward | The synchronization direction. Valid values: Forward: Data is synchronized from the source database to the destination database. Reverse: Data is synchronized from the destination database to the source database. Note Default value: Forward. You can set this parameter to Reverse to delete the reverse synchronization task only when the topology of the data synchronization task is two- way synchronization. |
| RegionId | String | No | cn-hangzhou | The region ID of the DTS instance. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| DynamicCode | String | 403 | The dynamic error code. This parameter will be removed in the future. |

| DynamicMessage | String | DtsJobId | The dynamic part in the error message. The value of this parameter is used to replace the %s variable in the value of the ErrMessage parameter. Note If the return value of the ErrMessage parameter is The Value of Input Parameter %s is not valid and the return value of the DynamicMessage parameter is DtsJobId, the specified DtsJobId parameter is invalid. |
|---|---|---|---|
| ErrCode | String | InternalError | The error code returned if the call failed. |
| ErrMessage | String | The Value of Input Parameter %s is not valid. | The error message returned if the call failed. |
| HttpStatusCode | Integer | 200 | The HTTP status code. |
| RequestId | String | 01B6F25-21E7-4484-99D5- 3EF2625C**** | The ID of the request. |
| Success | Boolean | true | Indicates whether the call was successful. |

**Examples**

Sample requests

```
http(s)://dts.aliyuncs.com/?Action=DeleteDtsJob &DtsJobId=l3m1213ye7l**** &<Common request parameters>
```

Sample success responses

| XML | format |
|---|---|
| <DeleteDtsJobResponse> <RequestId>01B6F25-21E7-4484-99D5-3EF2625C****</RequestId> <HttpStatusCode>200</HttpStatusCode> <Success>true</Success> </DeleteDtsJobResponse> |   |

| JSON | format |
|---|---|
| { "RequestId":"01B6F25-21E7-4484-99D5-3EF2625C****", "HttpStatusCode":200, "Success":true } |   |

#### 1.4.16 DeleteDtsJobs

Deletes multiple data migration, data synchronization, or change tracking tasks.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteDtsJobs | The operation that you want to perform. Set the value to DeleteDtsJobs. |
| DtsJobIds | String | Yes | l5o11f9029c**** | The ID of the data migration, data synchronization, or change tracking task. Note Separate multiple task IDs with commas (,). You can call the DescribeDtsJobs operation to query task IDs. |
| RegionId | String | No | cn-hangzhou | The region ID of the Data Transmission Service (DTS) instance. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| DynamicCode | String | 403 | The dynamic error code. This parameter will be removed in the future. |

| DynamicMessage | String | DtsJobId | The dynamic part in the error message. The value of this parameter is used to replace the %s variable in the value of the ErrMessage parameter. Note If the return value of the ErrMessage parameter is The Value of Input Parameter %s is not valid and the return value of the DynamicMessage parameter is DtsJobId, the specified DtsJobId parameter is invalid. |
|---|---|---|---|
| ErrCode | String | InternalError | The error code returned if the call failed. |
| ErrMessage | String | The Value of Input Parameter %s is not valid. | The error message returned if the call failed. |
| HttpStatusCode | Integer | 200 | The HTTP status code. |
| RequestId | String | AD823BD3-1BA6-4117-A536- 165CB280**** | The ID of the request. |
| Success | Boolean | true | Indicates whether the call was successful. |

**Examples**

Sample requests

```
http(s)://dts.aliyuncs.com/?Action=DeleteDtsJobs &DtsJobIds=l5o11f9029c**** &RegionId=cn-hangzhou &<Common request parameters>
```

Sample success responses

| XML | format |
|---|---|
| <DeleteDtsJobsResponse> <RequestId>AD823BD3-1BA6-4117-A536-165CB280****</RequestId> <HttpStatusCode>200</HttpStatusCode> <Success>true</Success> </DeleteDtsJobsResponse> |   |

| JSON | format |
|---|---|
| { "RequestId": "AD823BD3-1BA6-4117-A536-165CB280****", "HttpStatusCode": 200, "Success": true } |   |

#### 1.4.17 SummaryJobDetail

Queries the number of migrated or synchronized objects in a Data Transmission Service (DTS) task.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | SummaryJobDetail | The operation that you want to perform. Set the value to SummaryJobDetail. |
| DtsJobId | String | Yes | l3m1213ye7l**** | The ID of the data migration or data synchronization task. Note You must specify at least one of the DtsJobId and DtsInstanceId parameters. |
| JobCode | String | Yes | 02 | The phase of a data migration task. 02: indicates that the task is in the schema migration phase. 03: indicates that the task is in the incremental migration phase. |

| SynchronizationDirection | String | Yes | Forward | The synchronization direction of a data synchronization task. Forward: Data is synchronized from the source database to the destination database. Reverse: Data is synchronized from the destination database to the source database. Note The default value is Forward. You can set this parameter to Reverse to delete the reverse synchronization task only if the topology is two-way synchronization. |
|---|---|---|---|---|
| RegionId | String | No | cn-hangzhou | The region ID of the DTS instance. |
| DtsInstanceId | String | No | dtsl3m1213ye7l**** | The ID of the data migration or data synchronization instance. Note You must specify at least one of the DtsJobId and DtsInstanceId parameters. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Code | String | 200 | The error code. This parameter will be removed in the future. |
| HttpStatusCode | Integer | 200 | The HTTP status code. |
| JobId | String | l3m1213ye7l**** | The ID of the data migration or data synchronization task. |
| ProgressSummaryDetails | Array of ProgressSummaryDetail |   | The returned information about the migrated objects in arrays. Note The arrays are in the following format: [{"key":"Function","state":5,"totalCount":22}, {"key":"Procedure","state":5,"totalCount":26}, {"key":"Table","state":0,"totalCount":68}, {"key":"View","state":5,"totalCount":100}]. |
| Key | String | Table | The type of the migration object. Valid values: Table, Constraint, Index, View, Materialize View, Type, Synonym, Trigger, Function, Procedure, Package, Default, Rule, PlanGuide, and Sequence. |
| State | Integer | 0 | The state of the data migration task. Valid values: 0: The task is complete. 1: The task is waiting to start. 2: The task is being initialized. 3: The task is in progress. 4: An error occurred. 5: The task failed. |
| TotalCount | Long | 100 | The total number of migrated objects. |
| RequestId | String | 65EE90A6-9062-51B0-9997- 75F7E574**** | The ID of the request. |
| Success | Boolean | true | Indicates whether the call was successful. Valid values: true: The call was successful. false: The call failed. |

**Examples**

Sample requests

```
http(s)://dts.aliyuncs.com/?Action=SummaryJobDetail &DtsJobId=l3m1213ye7l**** &JobCode=02 &SynchronizationDirection=Forward &RegionId=cn-hangzhou &<Common request parameters>
```

Sample success responses `XML` format

```xml
<SummaryJobDetailResponse>
      <requestId>65EE90A6-9062-51B0-9997-75F7E574****</requestId>
      <progressSummaryDetails>
            <key>Function</key>
            <state>5</state>
            <totalCount>22</totalCount>
      </progressSummaryDetails>
      <progressSummaryDetails>
            <key>Procedure</key>
            <state>5</state>
            <totalCount>26</totalCount>
      </progressSummaryDetails>
      <progressSummaryDetails>
            <key>Table</key>
            <state>0</state>
            <totalCount>68</totalCount>
      </progressSummaryDetails>
      <progressSummaryDetails>
            <key>View</key>
            <state>5</state>
            <totalCount>100</totalCount>
      </progressSummaryDetails>
      <httpStatusCode>200</httpStatusCode>
</SummaryJobDetailResponse>
```

| JSON | format |
|---|---|
| { "requestId": "65EE90A6-9062-51B0-9997-75F7E574****", "success": true, "progressSummaryDetails": [ { "key": "Function", "state": 5, "totalCount": 22 }, { "key": "Procedure", "state": 5, "totalCount": 26 }, { "key": "Table", "state": 0, "totalCount": 68 }, { "key": "View", "state": 5, "totalCount": 100 } ], "httpStatusCode": 200 } |   |

#### 1.4.18 Manage alert rules

##### 1.4.18.1 CreateJobMonitorRule

Creates or modifies an alert rule for a Data Transmission Service (DTS) task. DTS provides the following metrics for DTS tasks:
**Latency**: DTS monitors the latency of a DTS task. If the latency of the task exceeds the specified threshold, an alert is triggered. The threshold is
specified in units of seconds.
**Status**: DTS monitors the status of a DTS task. If the state of the task changes to **Error** or **Restore**, an alert is triggered.
**Full Timeout**: DTS monitors the duration of a DTS task. If the duration of the task exceeds the specified threshold, an alert is triggered. The
threshold is specified in units of hours.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateJobMonitorRule | The operation that you want to perform. Set the value to CreateJobMonitorRule. |
| DtsJobId | String | Yes | i03e3zty16i**** | The ID of the data migration, data synchronization, or change tracking task. |

| Type | String | No | delay | The metric that is used to monitor the task. Valid values: delay: the Latency metric. error: the Status metric. fulltimeout: the Full Timeout metric. _ Default value: error. You must manually set this value. |
|---|---|---|---|---|
| State | String | No | Y | Specifies whether to enable the alert rule. Valid values: Y: enables the alert rule. N: disables the alert rule. Default value: Y. |
| Phone | String | No | 1361234****,1371234**** | The mobile numbers that receive alert notifications. Separate multiple mobile numbers with commas (,). Note This parameter is available only for users of the China site (aliyun.com). Only mobile numbers in the Chinese mainland are supported. You can specify up to 10 mobile numbers. Users of the international site (alibabacloud.com) cannot receive alerts by using mobile phones, but can configure alert rules for DTS tasks in the CloudMonitor console. |
| DelayRuleTime | Long | No | 11 | The threshold for triggering an alert. If Type is set to delay, the threshold must be an integer in units of seconds. You can specify the threshold based on your business requirements. To prevent jitters caused by network and database overloads, we recommend that you set the threshold to more than 10 seconds. If Type is set to fulltimeout, the threshold must be an _ integer in units of hours. Note You must specify this parameter if Type is set to delay or fulltimeout and State is set to Y. _ |
| RegionId | String | No | cn-hangzhou | The region ID of the DTS instance. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Code | String | 200 | The error code. This parameter will be removed in the future. |
| DtsJobId | String | i03e3zty16i**** | The ID of the data migration, data synchronization, or change tracking task. |
| DynamicMessage | String | DtsJobId | The dynamic part in the error message. This parameter is used to replace the %s variable in the value of ErrMessage. Note For example, if the return value of ErrMessage is The Value of Input Parameter %s is not valid and the return value of DynamicMessage is DtsJobId, the specified value of DtsJobId is invalid. |
| ErrCode | String | 403 | The error code returned if the request failed. |
| ErrMessage | String | The Value of Input Parameter %s is not valid. | The error message returned if the request failed. |
| HttpStatusCode | Integer | 200 | The HTTP status code. |
| RequestId | String | 8C498360-7892-433C-847A- BA71A850**** | The request ID. |
| Success | Boolean | true | Indicates whether the request was successful. Valid values: true false |

**Examples**

Sample requests

```
http(s)://dts.aliyuncs.com/?Action=CreateJobMonitorRule &DtsJobId=i03e3zty16i**** &Type=delay &State=Y &Phone=1361234****,1371234**** &DelayRuleTime=11 &<Common request parameters>
```

Sample success responses

| XML | format |
|---|---|
| <CreateJobMonitorRuleResponse> <RequestId>8C498360-7892-433C-847A-BA71A850****</RequestId> <HttpStatusCode>200</HttpStatusCode> <Success>true</Success> <DtsJobId>i03e3zty16i****</DtsJobId> </CreateJobMonitorRuleResponse> |   |

| JSON | format |
|---|---|
| { "RequestId":"8C498360-7892-433C-847A-BA71A850****", "HttpStatusCode":200, "Success":true, "DtsJobId":"i03e3zty16i****" } |   |

##### 1.4.18.2 DescribeJobMonitorRule

Queries the alert rules of a Data Transmission Service (DTS) task.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeJobMonitorRule | The operation that you want to perform. Set the value to DescribeJobMonitorRule. |
| DtsJobId | String | Yes | ta7w132u12h**** | The ID of the data migration, data synchronization, or change tracking task. You can call the DescribeDtsJobs operation to query the task ID. |
| RegionId | String | No | cn-hangzhou | The region ID of the DTS instance. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Code | String | 200 | The error code. This parameter will be removed in the future. |
| DtsJobId | String | ta7w132u12h**** | The ID of the data migration, data synchronization, or change tracking task. |
| DynamicMessage | String | DtsJobId | The dynamic part in the error message. This parameter is used to replace the %s variable in the value of ErrMessage. Note For example, if the return value of ErrMessage is The Value of Input Parameter %s is not valid and the return value of DynamicMessage is DtsJobId, the specified value of DtsJobId is invalid. |
| ErrCode | String | 403 | The error code returned if the request failed. |
| ErrMessage | String | The Value of Input Parameter %s is not valid. | The error message returned if the request failed. |
| HttpStatusCode | Integer | 200 | The HTTP status code. |
| MonitorRules | Array of MonitorRule |   | The alert rules of the DTS task. |
| DelayRuleTime | Long | 11 | The threshold for triggering an alert. If the request parameter Type of the CreateJobMonitorRule operation is set to delay, the unit of DelayRuleTime is seconds. If the request parameter Type of the CreateJobMonitorRule operation is set to fulltimeout, the unit of DelayRuleTime is hours. _ |

| Phone | String | 1361234****,1371234**** | The mobile numbers that receive alert notifications. Multiple mobile numbers are separated by commas (,). |
|---|---|---|---|
| State | String | Y | Indicates whether the alert rule is enabled. Valid values: Y: The alert rule is enabled. N: The alert rule is disabled. |
| Type | String | delay | The type of the alert rule. Valid values: delay: If the latency of the task exceeds the specified threshold, an alert is triggered. error: If an exception occurs, an alert is triggered. |
| RequestId | String | 0CA14388-DD89-4A7B-8CDD- 884A10CE**** | The request ID. |
| Success | Boolean | true | Indicates whether the request was successful. Valid values: true false |

**Examples**

Sample requests

```
http(s)://dts.aliyuncs.com/?Action=DescribeJobMonitorRule &DtsJobId=ta7w132u12h**** &<Common request parameters>
```

Sample success responses

| XML | format |
|---|---|
| <DtsJobId>ta7w132u12h****</DtsJobId> <RequestId>0CA14388-DD89-4A7B-8CDD-884A10CE****</RequestId> <HttpStatusCode>200</HttpStatusCode> <MonitorRules> <Type>delay</Type> <Phone>1361234****,1371234****</Phone> <State>Y</State> <DelayRuleTime>11</DelayRuleTime> </MonitorRules> <DynamicMessage>DtsJobId</DynamicMessage> <ErrMessage>The Value of Input Parameter %s is not valid.</ErrMessage> <Code>200</Code> <Success>true</Success> <ErrCode>403</ErrCode> |   |

| JSON | format |
|---|---|
| { "DtsJobId": "ta7w132u12h****", "RequestId": "0CA14388-DD89-4A7B-8CDD-884A10CE****", "HttpStatusCode": 200, "MonitorRules": { "Type": "delay", "Phone": "1361234****,1371234****", "State": "Y", "DelayRuleTime": 11 }, "DynamicMessage": "DtsJobId", "ErrMessage": "The Value of Input Parameter %s is not valid.", "Code": 200, "Success": true, "ErrCode": 403 } |   |

#### 1.4.19 Query ETL tasks

##### 1.4.19.1 DescribeDtsEtlJobVersionInfo

Queries the details of extract, transform, and load (ETL) tasks.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeDtsEtlJobVersionInfo | The operation that you want to perform. Set the value to DescribeDtsEtlJobVersionInfo. |
| PageSize | Integer | No | 20 | The number of rows to return on each page. Default value: 20 |

| PageNumber | Integer | No | 1 | The number of the page to return. Default value: 1. |
|---|---|---|---|---|
| DtsInstanceId | String | No | dtsggk12iwya1a**** | The ID of the Data Transmission Service (DTS) instance. You can call the DescribeDtsJobs operation to query the instance ID. |
| DtsJobId | String | No | l5512es7w15**** | The ID of the ETL task. You can call the DescribeDtsJobs operation to query the task ID. |
| RegionId | String | No | cn-hangzhou | The region ID of the DTS instance. You can call the DescribeRegions operation to query the most recent region list. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| DtsEtlJobVersionInfos | Array of DtsEtlJobVersionInfo |   | Details of the ETL tasks. |
| CreateTime | String | 1637229315000 | The timestamp when the ETL task is created. |
| Creator | String | 10000000 | The ID of the creator. |
| CreatorName | String | ***@****.com | The username of the creator. |
| DtsInstanceId | String | dtsg******gd | The ID of the DTS instance. |
| DtsJobId | String | l5512es7w15**** | The ID of the ETL task. |
| DtsJobName | String | testsql _ | The name of the ETL task. |
| ModifyTime | String | 1637230117000 | The timestamp when ETL task was modified. |
| SafeCheckpoint | String | 1637230117000 | The safe checkpoint of the ETL task. |
| Status | String | INFO | The log level. Valid values: ERROR, WARN, INFO, and DEBUG. |
| Version | Integer | 9 | The version number of the ETL task. |
| DynamicCode | String | 403 | The dynamic error code. |
| DynamicMessage | String | present environment is not support,so skip | The dynamic part in the error message. |
| ErrCode | String | InvalidJobId | The error code. This example indicates that the specified ETL task ID is invalid. |
| ErrMessage | String | The specified dts job id %s is not exists. | The error message. This example indicates that the specified ETL task ID is not found. In this case, the ETL task may be deleted. |
| HttpStatusCode | String | 200 | The HTTP status code. |
| PageNumber | Integer | 1 | The number of the page to return. Default value: 1. |
| Success | Boolean | true | Indicates whether the call was successful. If the call fails, false is returned. |
| RequestId | String | 224DB9F7-3100-4899-AB9C- C938BCCB43E7 | The ID of the request. |
| PageRecordCount | Integer | 20 | The number of records returned on the current page. |
| TotalRecordCount | Integer | 200 | The total number of records. |

```
http(s)://dts.aliyuncs.com/?Action=DescribeDtsEtlJobVersionInfo &pageSize=20 &pageNumber=0 &dtsInstanceId=dtsggk12iwya1a**** &DtsJobId=l5512es7w15**** &RegionId=cn-hangzhou &<Required parameters> &<Common request parameters>
```

Sample success responses

| XML | format |
|---|---|
| <DescribeDtsEtlJobVersionInfoResponse> <requestId>62E37CD4-586B-50A4-99AA-3E60D2485F6C</requestId> <success>true</success> <dtsEtlJobVersionInfos> <createTime>1637229315000</createTime> <creator>10000000</creator> <creatorName>***@****.com</creatorName> <dtsInstanceId>dtsggk12iwya1a****</dtsInstanceId> <dtsJobId>l5512es7w15****</dtsJobId> <dtsJobName>test_sql</dtsJobName> <modifyTime>1637230117000</modifyTime> <status>INFO</status> <version>9</version> </dtsEtlJobVersionInfos> <httpStatusCode>200</httpStatusCode> </DescribeDtsEtlJobVersionInfoResponse> |   |

| JSON | format |
|---|---|
| { "requestId": "62E37CD4-586B-50A4-99AA-3E60D2485F6C", "success": true, "dtsEtlJobVersionInfos": [ { "createTime": 1637229315000, "creator": "10000000", "creatorName": "***@****.com", "dtsInstanceId": "dtsggk12iwya1a****", "dtsJobId": "l5512es7w15****", "dtsJobName": "test_sql", "modifyTime": 1637230117000, "status": "INFO", "version": 9 } ], "httpStatusCode": 200 } |   |

##### 1.4.19.2 DescribeEtlJobLogs

Queries the logs of an extract, transform, and load (ETL) task.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeEtlJobLogs | The operation that you want to perform. Set the value to DescribeEtlJobLogs. |
| DtsJobId | String | Yes | l5512es7w15**** | The ID of the ETL task. You can call the DescribeDtsJobs operation to query the task ID. |
| RegionId | String | No | cn-hangzhou | The region ID of the Data Transmission Service (DTS) instance. You can call the DescribeRegions operation to query the most recent region list. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| DynamicCode | String | 403 | The dynamic part in the error message. |
| DynamicMessage | String | present environment is not support,so skip. | The dynamic part in the error message. |
| ErrCode | String | InvalidJobId | The error code. This example indicates that the specified ETL task ID is invalid. |

| ErrMessage | String | The specified dts job id %s is not exists. | The error message. This example indicates that the specified ETL task ID is not found. In this case, the ETL task may be deleted. |
|---|---|---|---|
| EtlRunningLogs | Array of EtlRunningLog |   | The logs of the ETL task. |
| Content | String | Starting DTS-ETL... | The state of the ETL task. |
| ContentKey | String | DTS-ETL | The module for which the logs are generated, such as the conversion module of ETL tasks. |
| EtlId | String | u**********5 | The ID of the ETL task. |
| LogDatetime | String | 1637306503000 | The timestamp when the log is generated. |
| Status | String | INFO | The log level. Valid values: ERROR, WARN, INFO, and DEBUG. |
| UserId | String | 121323*******454512 | The ID of the user. |
| HttpStatusCode | Integer | 200 | The HTTP status code. |
| RequestId | String | 224DB9F7-3100-4899-AB9C- C938BCCB43E7 | The ID of the request. |
| Success | Boolean | true | Indicates whether the call was successful. If the call fails, false is returned. |

**Examples**

Sample requests

```
http(s)://dts.aliyuncs.com/?Action=DescribeEtlJobLogs &DtsJobId=l5512es7w15**** &RegionId=cn-hangzhou &<Common request parameters>
```

Sample success responses

| XML | format |
|---|---|
| <DescribeEtlJobLogsResponse> <requestId>62E37CD4-586B-50A4-99AA-3E60D2485F6C</requestId> <success>true</success> <etlRunningLogs> <content>Starting DTS-ETL...</content> <contentKey>DTS-ETL</contentKey> <etlId>u**********5</etlId> <gmtCreate>1637306505000</gmtCreate> <id>941</id> <logDatetime>1637306503000</logDatetime> <status>INFO</status> </etlRunningLogs> <httpStatusCode>200</httpStatusCode> </DescribeEtlJobLogsResponse> |   |

| JSON | format |
|---|---|
| { "requestId": "62E37CD4-586B-50A4-99AA-3E60D2485F6C", "success": true, "etlRunningLogs": [ { "content": "Starting DTS-ETL...", "contentKey": "DTS-ETL", "etlId": "u**********5", "gmtCreate": 1637306505000, "id": 941, "logDatetime": 1637306503000, "status": "INFO" } ], "httpStatusCode": 200 } |   |

#### 1.4.20 Additional parameters

##### 1.4.20.1 Objects of DTS tasks

You can call the API operations of Data Transmission Service (DTS) to configure or query the objects of a data migration, data synchronization, or change tracking task. This topic describes the related API operations and provides object definitions and configuration examples.

**Related API operations and parameters**

| Operation | Description |
|---|---|
| ConfigureDtsJob ConfigureSubscription | You can use the request parameter DbList to specify the objects of a data migration, data synchronization, or change tracking task. |
| DescribeDtsJobDetail DescribeDtsJobs | You can query the objects of a data migration, data synchronization, or change tracking task and view the results in the value of the response parameter DbObject . |

**Object definitions**

The value of an object-related parameter is a JSON string. This section describes object-related parameters.

> **Note:** You can configure the italic content in the following sample code based on your business requirements.

If the objects consist of multiple databases, refer to the following parameter description to define these objects: `{`

```json
    "The name of Source Database 1.": {
        "name": "The database name that you want to use in the destination instance for Source Database 1.",
        "all": A value of true specifies that the entire database is used as the source object.
```

`},`

```json
    "The name of Source Database 2.": {
        "name": "The database name that you want to use in the destination instance for Source Database 2.",
        "all": A value of false specifies that the source object is not the entire database.,
        "Table": {
            "The name of Source Table A.": {
                "name": "The table name that you want to use in the destination instance for Source Table A.",
                "all": A value of true specifies that the entire table is used as the source object.,
                "dml_op": "The DML operations that you want to migrate or synchronize during incremental data migration or synchronization.",
                "ddl_op": "The DDL operations that you want to migrate or synchronize during incremental data migration or synchronization."
```

`}` `}` `},`

```json
    "The name of Source Database 3.": {
        "name": "The database name that you want to use in the destination instance for Source Database 3.",
        "all": A value of true specifies that the entire database is used as the source object.,
        "dml_op": "The DML operations that you want to migrate or synchronize during incremental data migration or synchronization.",
        "ddl_op": "The DDL operations that you want to migrate or synchronize during incremental data migration or synchronization."
```

`}` `}` If the objects are specific columns or include filter conditions, refer to the following parameter description to define these objects: `{`

```json
    "The name of the source database for the data migration, data synchronization, or change tracking task.": {
        "name": "The database name that you want to use in the destination instance for the source database.",
        "all": A value of false specifies that the source object is not the entire database.,
        "Table": {
            "The name of Source Table A.": {
                "name": "The table name that you want to use in the destination instance for Source Table A.",
                "all": A value of false specifies that the source object is not the entire table.,
                "filter": "id>10"
                "column": {
                    "id": {
                        "key": "PRI",
                        "name": "id",
                        "type": "int(11)",
                        "sharedKey": false,
                        "state": "checked"
```

`}` `},`

```json
                "shard": 12
```

`}` `},` `}` `}` If you migrate or synchronize objects to an AnalyticDB for MySQL or AnalyticDB for PostgreSQL instance, refer to the following parameter description to define these objects:

```json
    "The name of the source database that you want to migrate or synchronize.": {
        "name": "The database name that you want to use in the destination instance for the source database.",
        "all": Set the value to false. If the destination instance is an AnalyticDB for MySQL or AnalyticDB for PostgreSQL instance, you
must set the value to false regardless of whether the entire database or specific tables are used as the source objects. In this case, you m ust also specify the partition key that corresponds to each table.
        "Table": {
            "The name of Source Table A.": {
                "all": A value of true specifies that the entire table is used as the source object.,
                "name": "The table name that you want to use in the destination instance for Source Table A.",
                "primary_key": "The primary key. Example: id.",
                "type": "The type of the table. Example: dimension.",
```

`}`

```json
            "The name of Source Table B.": {
                "all": A value of true specifies that the entire table is used as the source object.,
                "name": "The table name that you want to use in the destination instance for Source Table B.",
                "part_key": "The partition key. Example: id.",
                "primary_key": "The primary key. Example: id.",
                "type": "The type of the table. Example: partition.",
```

`}` `}` `}` `}`

| Parameter | Description |
|---|---|
| name | The database name, table name, or column name that you want to use in the destination instance. For example, if you want to migrate data from a database named dtssource to a database named dtstarget, you must set the name parameter to dtstarget. |
| all | Specifies whether to select all tables or columns. Valid values: true Note If you select all tables or columns, you do not need to configure the information about specific tables or columns. false |
| Table | The information about the source table. |
| filter | The condition used to filter the source data. The filter condition takes effect only at the table level. For example, you can enter id>10 to migrate or synchronize only entries whose value in the id column is greater than 10. Note Filter conditions are unavailable for change tracking tasks. |
| column | The information about the source column. |
| key | Specifies whether to use the column as the primary key. Valid values: PRI : yes. Empty string: no. |
| sharedKey | Specifies whether to use the column as the shard key. Valid values: true false Note This parameter is required only if the source database is a Kafka instance. |
| type | The data type of the column. |
| state | The state of the column. For example, the checked state indicates that the column is selected. |
| shard | The number of shards in the source table. Note This parameter is required only if the source database is a Kafka instance. |
| dml_op | The DML operations that you want to migrate or synchronize during incremental data migration or synchronization. Valid values: i : INSERT. u : UPDATE. d : DELETE. If the value is empty, the task migrates or synchronizes all DML operations supported by DTS. none : The task does not migrate or synchronize DML operations during incremental data migration or synchronization. |

| ddl_op | The DDL operations that you want to migrate or synchronize during incremental data migration or synchronization. Valid values: ct : CREATE TABLE. at : ALTER TABLE. dt : DROP TABLE. rt : RENAME TABLE. tt : TRUNCATE TABLE. If the value is empty, the task migrates or synchronizes all DDL operations supported by DTS. none : The task does not migrate or synchronize DDL operations during incremental data migration or synchronization. |
|---|---|
| primary_key | The primary key. This parameter is available and required only if the destination instance is anA nalyticDB for MySQL or AnalyticDB for PostgreSQL instance. |
| part_key | The partition key. This parameter is available and required only if the destination instance is anA nalyticDB for MySQL or AnalyticDB for PostgreSQL instance. |
| type Important This type parameter is not the same as the type parameter that specifies the data type of a column. | If the destination instance is an AnalyticDB for MySQL or AnalyticDB for PostgreSQL instance, you must specify the type of each source table. Valid values: dimension: dimension table. partition: partitioned table. |

**Configuration examples**

Example 1: Replicate data from all tables in the dtstestdata database.

```json
{"dtstestdata": { "name": "dtstestdata", "all": true }}
```

Example 2: Replicate data from all tables in the dtstestdata database and change the database name to dtstestdata_new.

```json
{"dtstestdata": { "name": "dtstestdata_new", "all": true }}
```

Example 3: Replicate data from a table named customer in the dtstestdata database.

```json
{"dtstestdata": {
   "name": "dtstestdata",
   "all": false,
   "Table": {
     "customer": {
       "name": "customer",
       "all": true,
       "column": {
         "id": {
           "key": "PRI",
           "name": "id",
           "type": "int(11)",
           "sharedKey": false,
           "state": "checked"
```

`},`

```json
         "gmt_create": {
           "key": "",
           "name": "gmt_create",
           "type": "datetime",
           "sharedKey": false,
           "state": "checked"
```

`},`

```json
         "gmt_modify": {
           "key": "",
           "name": "gmt_modify",
           "type": "datetime",
           "sharedKey": false,
           "state": "checked"
```

`},`

```json
         "valid_time": {
           "key": "",
           "name": "valid_time",
           "type": "datetime",
           "sharedKey": false,
           "state": "checked"
```

`},`

```json
         "creator": {
           "key": "",
           "name": "creator",
           "type": "varchar(200)",
           "sharedKey": false,
           "state": "checked"
```

`}` `},`

```json
       "shard": 12
```

`}` `},` Example 4: Replicate data from specific columns of the customer and order tables in the dtstestdata database.

```json
{"dtstestdata": {
   "name": "dtstestdata",
   "all": false,
   "Table": {
     "customer": {
       "name": "customer",
       "all": false,
       "column": {
         "id": {
           "key": "PRI",
           "name": "id",
           "type": "int(11)",
           "sharedKey": false,
           "state": "checked"
```

`},`

```json
         "level": {
           "key": "",
           "name": "level",
           "type": "varchar(5000)",
           "sharedKey": false,
           "state": "checked"
```

`},`

```json
         "name": {
           "key": "",
           "name": "name",
           "type": "varchar(500)",
           "sharedKey": false,
           "state": "checked"
```

`},` `},`

```json
       "shard": 12
```

`},`

```json
     "order": {
       "name": "order",
       "all": false,
      "column": {
         "id": {
           "key": "PRI",
           "name": "id",
           "type": "int(11)",
           "sharedKey": false,
           "state": "checked"
```

`}` `},`

```json
       "shard": 12
```

`}` `},` `}` `}` Example 5: Replicate data from the customer, order, and commodity tables in the dtstestdata database to the destination AnalyticDB for MySQL or AnalyticDB for PostgreSQL instance.

```json
    "dtstestdata": {
        "name": "dtstestdatanew",
        "all": false,
        "Table": {
            "order": {
                "name": "ordernew",
                "all": true,
                "part_key": "id",
                "primary_key": "id",
                "type": "partition"
```

`},`

```json
            "customer": {
                "name": "customernew",
                "all": true,
                "primary_key": "id",
                "type": "dimension"
```

`},`

```json
            "commodity": {
                "name": "commoditynew",
                "all": false,
                "filter": "id>10",
                "column": {
                    "id": {
                        "key": "PRI",
                        "name": "id",
                        "type": "int(11)"
```

`}` `},`

```json
                "part_key": "id",
                "primary_key": "id",
                "type": "partition"
```

`}` `}` `}` `}`

**Supported regular expressions**

| Symbol | Rule description |
|---|---|
| Period (.) | Matches any single character except '\r\n'. |
| Asterisk (*) | Matches zero or more repetitions of the preceding sub-expression. For example, h.*llo matches strings such as hllo and heeeello. |
| Question mark (?) | Matches zero or one repetition of the preceding sub-expression. For example, h.?llo matches hllo and hello, but not haello. |
| Character set [characters] | Matches any single character included in the brackets. For example, h[ae]llo matches hallo and hello. |
| Negative character set [^characters] | Matches any single character except the characters included in the brackets. For example, h[ae]llo matches hcllo or hdllo, but not hallo or hello. |
| Character range [character1-character2] | Matches any characters within the range from character1 to character2. Examples: [0-9] and [a-z]. |

##### 1.4.20.2 Reserve parameter description

When you call an API operation to configure or query a Data Transmission Service (DTS) task, you must specify or query the Reserve parameter. The Reserve parameter allows you to view the configurations of the source or destination instance or add more configurations to the DTS task. For example, you can specify the data storage format of the destination Kafka instance or the ID of a Cloud Enterprise Network (CEN) instance. This topic describes the settings of the Reserve parameter in different scenarios.

**Related API operations**

**Settings of the Reserve parameter**

The value of the Reserve parameter is a JSON string. You can specify the Reserve parameter in the following scenarios:

> **Note:** If you specify a numeric value, you must enclose the value in double quotation marks (" ").

You can use the **Reserve** parameter to specify the processing mode of conflicting tables for a data migration or data synchronization task.

| Parameter | Required | Description |
|---|---|---|
| targetTableMode | Yes | The processing mode of conflicting tables. Valid values: 0: performs a precheck and reports errors. 2: ignores errors and proceeds. |

If the database type of the destination instance is Kafka, you can use the Reserve parameter to configure the information about the Kafka instance and the storage format in which data is shipped to the Kafka instance.

| Parameter | Required | Description |
|---|---|---|
| destTopic | Yes | The topic to which the objects migrated or synchronized to the destination Kafka instance belong. |
| destVersion | Yes | The engine version of the destination Kafka instance. Valid values:1 .0, 0.9, and 0.10. Note If the engine version of the destination Kafka instance is 1.0 or later, you must set the value to 1.0. |
| destSSL | Yes | Specifies whether to encrypt the connection to the destination Kafka instance. Valid values: 0: does not encrypt the connection. 3: encrypts the connection by using the SCRAM-SHA-256 algorithm. |
| dest.kafka.schema.registry.url | No | If you useKafka Schema Registry, you must enter the URL or IP address that is registered in Kafka Schema Registry for your Avro schemas. |
| sink.kafka.ddl.topic | No | The topic that is used to store the DDL information. If you do not specify this parameter, the DDL information is stored in the topic that is specified by destTopic. |
| kafkaRecordFormat | Yes | The storage format in which data is shipped to the destination Kafka instance. Valid values: canaljson: Canal is used to parse the incremental logs of the source _ database and transfer the incremental data to the destination Kafka instance in the Canal JSON format. dtsavro: Avro is a data serialization format into which data structures or _ objects can be converted to facilitate storage and transmission. shareplexjson: The data replication software SharePlex is used to read the _ data in the source database and write the data to the destination Kafka instance in the SharePlex JSON format. debezium: Debezium is a tool used to capture data changes. Debezium supports real-time streaming of data updates from the source PolarDB for Oracle cluster to the destination Kafka instance. |
| destKafkaPartitionKey | Yes | The policy that is used to synchronize data to Kafka partitions. Valid values: none: DTS synchronizes all data and DDL statements to Partition 0 of the destination topic. databasetable: DTS uses the database and table names as the partition key _ to calculate the hash value. Then, DTS synchronizes the data and DDL statements of each table to the corresponding partition of the destination topic. columns: DTS uses a table column as the partition key to calculate the hash value. By default, the primary key is used as the partition key. If a table does not have a primary key, the unique key is used as the partition key. DTS synchronizes each row to the corresponding partition of the destination topic. You can specify one or more columns as partition keys to calculate the hash value. |

Example: `{`

```json
    "destTopic": "dtstestdata",
    "destVersion": "1.0",
    "destSSL": "0",
    "dest.kafka.schema.registry.url": "http://12.1.12.3/api",
    "sink.kafka.ddl.topic": "dtstestdata",
    "kafkaRecordFormat": "canal_json",
    "destKafkaPartitionKey": "none"
```

`}` If the database type of the source or destination instance is MongoDB, you must use the Reserve parameter to specify the architecture type of the MongoDB database.

| Parameter | Required | Description | Example |
|---|---|---|---|
| srcEngineArchType | Yes | The architecture type of the source MongoDB database. Valid values: 0: standalone architecture. 1: replica set architecture. 2: sharded cluster architecture. | { "srcEngineArchType": "1" } |
| destEngineArchType | Yes | The architecture type of the destination MongoDB database. Valid values: 0: standalone architecture. 1: replica set architecture. 2: sharded cluster architecture. | { "destEngineArchType": "1" } |

If the source or destination instance is a self-managed database connected over CEN, you must use the Reserve parameter to specify the ID of the CEN instance.

| Parameter | Required | Description | Example |
|---|---|---|---|
| srcInstanceId | Yes | The ID of the CEN instance for the source instance. | { "srcInstanceId": "cen-9kqshqum*******" } |

| destInstanceId | Yes | The ID of the CEN instance for the destination instance. | { "destInstanceId": "cen-9kqshqum*******" } |
|---|---|---|---|

### 1.5 DTS API (soon-to-be-obsolete)

#### 1.5.1 Data migration

##### 1.5.1.1 CreateMigrationJob

Purchases a data migration instance.

> **Note:** This operation is of the old version. We recommend that you call the new API operation.

After you purchase a data migration instance, you must call the ConfigureMigrationJob operation to configure a data migration task.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateMigrationJob | The operation that you want to perform. Set the value to CreateMigrationJob. |
| MigrationJobClass | String | Yes | 2xlarge | The instance class of the data migration instance. Valid values: small, medium, large, xlarge, and 2xlarge. Note |
| Region | String | Yes | cn-hangzhou | The region where the data migration instance resides. |
| RegionId | String | No | cn-hangzhou | The region ID of the data migration instance. You do not need to specify this parameter because this parameter will be removed in the future. |
| ClientToken | String | No | 0c593ea1-3bea-11e9-b96b- 88e9fe63**** | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that the value is unique among different requests. The ClientToken parameter can contain only ASCII characters and cannot exceed 64 characters in length. |
| AccountId | String | No | 12323344**** | The ID of the Alibaba Cloud account. You do not need to specify this parameter because this parameter will be removed in the future. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| ErrCode | String | InternalError | The error code returned if the call failed. |
| ErrMessage | String | The request processing has failed due to some unknown error. | The error message returned if the call failed. |
| MigrationJobId | String | dtsi8911td9233**** | The ID of the data migration instance. |
| RequestId | String | C166D79D-436B-45F0-B5A5- 25E1959F**** | The ID of the request. |
| Success | String | true | Indicates whether the call was successful. |

**Examples**

Sample requests

```
http(s)://dts.aliyuncs.com/?Action=CreateMigrationJob &MigrationJobClass=2xlarge &Region=cn-hangzhou &<Common request parameters>
```

```xml
<CreateMigrationJobResponse>
      <RequestId>C166D79D-436B-45F0-B5A5-25E1959F****</RequestId>
      <MigrationJobId>dtsi8911td9233****</MigrationJobId>
</CreateMigrationJobResponse>
```

| JSON | format |
|---|---|
| { "RequestId": "C166D79D-436B-45F0-B5A5-25E1959F****", "Success": true, "MigrationJobId": "dtsi8911td9233****" } |   |

##### 1.5.1.2 ConfigureMigrationJob

Configures a data migration task. After you call this operation to configure a data migration task, the task will be automatically started. You do not need to call the StartMigrationJob operation to start the task. A data migration task may fail to be started due to precheck failures. You can call the DescribeMigrationJobStatus operation to query the error messages about the precheck failures. Then, you can fix the issue based on the error messages. After you fix the issue, you must call the StartMigrationJob operation to restart the data migration task.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ConfigureMigrationJob | The operation that you want to perform. Set the value to ConfigureMigrationJob. |
| DestinationEndpoint.Instance Type | String | Yes | RDS | The type of the destination database. Valid values: Note ECS: self-managed database hosted on Elastic Compute Service (ECS) LocalInstance: self-managed database with a public IP address RDS: ApsaraDB RDS instance DRDS: PolarDB-X instance MongoDB: ApsaraDB for MongoDB instance Redis: ApsaraDB for Redis instance PetaData: HybridDB for MySQL instance POLARDB: PolarDB for MySQL cluster or PolarDB for PostgreSQL cluster PolarDBo: PolarDB for Oracle cluster _ AnalyticDB: AnalyticDB for MySQL V3.0 cluster or AnalyticDB for MySQL V2.0 cluster Greenplum: AnalyticDB for PostgreSQL instance |
| MigrationJobId | String | Yes | dtsl3m1213ye7l**** | The ID of the data migration instance. You can call the DescribeMigrationJobs operation to query the instance ID. |
| MigrationJobName | String | Yes | MySQLTORDS _ _ | The name of the data migration task. The name can be up to 32 characters in length. We recommend that you specify a descriptive name that makes it easy to identify. You do not need to use a unique name. |
| MigrationMode.DataIntializati on | Boolean | Yes | true | Specifies whether to perform full data migration. Valid values: true: yes false: no Note Data Transmission Service (DTS) supports full data migration for specific database engines. |
| MigrationMode.DataSynchron ization | Boolean | Yes | true | Specifies whether to perform incremental data migration. Valid values: true: yes false: no Note DTS supports incremental data migration for specific database engines. |

| MigrationMode.StructureIntia lization | Boolean | Yes | true | Specifies whether to perform schema migration. Valid values: true: yes false: no Note DTS supports schema migration for specific database engines. |
|---|---|---|---|---|
| MigrationObject | String | Yes | [{"DBName":"dtstestdata","T ableIncludes": [{"TableName":"customer"}] }] | The objects that you want to migrate. The value is a JSON string and can contain regular expressions. |
| SourceEndpoint.InstanceTyp e | String | Yes | RDS | The engine type of the source database. Valid values: RDS: ApsaraDB RDS instance ECS: self-managed database hosted on ECS LocalInstance: self-managed database with a public IP address Express: self-managed database connected over Express Connect, VPN Gateway, or Smart Access Gateway dg: self-managed database connected over Database Gateway cen: self-managed database connected over Cloud Enterprise Network (CEN) MongoDB: ApsaraDB for MongoDB instance POLARDB: PolarDB for MySQL cluster or PolarDB for PostgreSQL cluster PolarDBo: PolarDB for Oracle cluster _ |
| RegionId | String | No | cn-hangzhou | The region ID of the data migration instance. Note The region ID of the data migration instance is the same as that of the destination database. |
| SourceEndpoint.InstanceID | String | No | rm-bp1i99e8l7913**** | The ID of the instance that hosts the source database. Note This parameter is available and required only if the SourceEndpoint.InstanceType parameter is set to RDS, ECS, Express, MongoDB, POLARDB, or PolarDBo. For example, if the _ SourceEndpoint.InstanceType parameter is set to ECS, you must specify the ID of the ECS instance. If the SourceEndpoint.InstanceType parameter is set to Express, you must specify the ID of the virtual private cloud (VPC). |
| SourceEndpoint.EngineName | String | No | MySQL | The engine type of the source database. Valid values: MySQL, TiDB, SQLServer, PostgreSQL, Oracle, MongoDB, Redis, POLARDB, and polardbpg. _ Note This parameter is available and required only if the DestinationEndpoint.InstanceType parameter is set to RDS, POLARDB, ECS, LocalInstance, or Express. |
| SourceEndpoint.Region | String | No | cn-hangzhou | The region ID of the source database. Note If the SourceEndpoint.InstanceType parameter is set to LocalInstance, you can enter cn- hangzhou or the ID of the region closest to the self- managed database. |
| SourceEndpoint.IP | String | No | 172.16.88.*** | The IP address of the source database. Note This parameter is available and required only if the SourceEndpoint.InstanceType parameter is set to LocalInstance or Express. |
| SourceEndpoint.Port | String | No | 3306 | The service port number of the source database. Note This parameter is available and required only if the SourceEndpoint.InstanceType parameter is set to ECS, LocalInstance, or Express. |
| SourceEndpoint.OracleSID | String | No | testsid | The system ID (SID) of the Oracle database. Note This parameter is available and required only if the SourceEndpoint.EngineName parameter is set to Oracle and the Oracle database is deployed in a non-RAC architecture. |

| SourceEndpoint.DatabaseNa me | String | No | dtstestdatabase | The name of the source database or the authentication database. Note This parameter is available and required only if the SourceEndpoint.EngineName parameter is set to PostgreSQL or MongoDB. If the SourceEndpoint.EngineName parameter is set to PostgreSQL, specify the name of the source database. If the SourceEndpoint.EngineName parameter is set to MongoDB, specify the name of the authentication database. |
|---|---|---|---|---|
| SourceEndpoint.UserName | String | No | dtstestaccount | The database account of the source database. Note The permissions required for the database account to migrate data vary with the database engine. |
| SourceEndpoint.Password | String | No | Test123456 | The password of the source database account. |
| SourceEndpoint.OwnerID | String | No | 140692647406**** | The ID of the Alibaba Cloud account to which the source instance belongs. Note This parameter is available and required only if you configure data migration across different Alibaba Cloud accounts. |
| SourceEndpoint.Role | String | No | ram-for-dts | The authorized Resource Access Management (RAM) role of the source instance. This parameter is required only if the source instance and the destination instance belong to different Alibaba Cloud accounts. You can use the RAM role to allow the Alibaba Cloud account that owns the destination instance to access the source instance. |
| DestinationEndpoint.Instance ID | String | No | rm-bp1r46452ai50**** | The ID of the destination instance. Note This parameter is available and required only if the DestinationEndpoint.InstanceType parameter is set to RDS, ECS, MongoDB, Redis, DRDS, PetaData, OceanBase, POLARDB, PolarDBo, _ AnalyticDB, or Greenplum. For example, if the DestinationEndpoint.InstanceType parameter is set to ECS, you must specify the ID of the ECS instance. |
| DestinationEndpoint.EngineN ame | String | No | MySQL | The engine type of the destination database. Valid values: MySQL, DRDS, SQLServer, PostgreSQL, PPAS, MongoDB, Redis, POLARDB, and polardbpg. _ Note This parameter is available and required only if the DestinationEndpoint.InstanceType parameter is set to RDS, POLARDB, ECS, LocalInstance, or Express. |
| DestinationEndpoint.Region | String | No | cn-hangzhou | The region ID of the destination database. Note If the DestinationEndpoint.InstanceType parameter is set to LocalInstance, you can enter cn- hangzhou or the ID of the region closest to the self- managed database. |
| DestinationEndpoint.IP | String | No | 172.16.88.*** | The IP address of the destination database. Note This parameter is available and required only if the DestinationEndpoint.InstanceType parameter is set to LocalInstance or Express. |
| DestinationEndpoint.Port | String | No | 3306 | The service port number of the destination database. Note This parameter is available and required only if the DestinationEndpoint.InstanceType parameter is set to ECS, LocalInstance, or Express. |

| DestinationEndpoint.DataBas eName | String | No | dtstestdatabase | The name of the destination database or the authentication database. Note This parameter is available and required only if the DestinationEndpoint.EngineName parameter is set to PostgreSQL, DRDS, or MongoDB. If the DestinationEndpoint.EngineName parameter is set to PostgreSQL or DRDS, specify the name of the destination database. If the DestinationEndpoint.EngineName parameter is set to MongoDB, specify the name of the authentication database. |
|---|---|---|---|---|
| DestinationEndpoint.UserNa me | String | No | dtstestaccount | The database account of the destination database. Note The permissions required for the database account to migrate data vary with the database engine. |
| DestinationEndpoint.Passwor d | String | No | Test123456 | The password of the destination database account. |
| MigrationReserved | String | No | { "autoStartModulesAfterConfi g": "none", "targetTableMode": 2 } | The reserved parameter of DTS. The value is a JSON string. You can specify this parameter to meet specific requirements, for example, whether to automatically start the precheck. |
| Checkpoint | String | No | 111 | The start offset of incremental data migration. The value is a UNIX timestamp. Unit: seconds. |
| AccountId | String | No | 12323344**** | The ID of the Alibaba Cloud account. You do not need to specify this parameter because this parameter will be removed in the future. |
| DestinationEndpoint.OracleSI D | String | No | testsid | The SID of the Oracle database. Note This parameter is available and required only if the DestinationEndpoint.EngineName parameter is set to Oracle and the Oracle database is deployed in a non-RAC architecture. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| ErrCode | String | InternalError | The error code returned if the call failed. |
| ErrMessage | String | The request processing has failed due to some unknown error. | The error message returned if the call failed. |
| RequestId | String | 40E35BD9-002E-4D63-9BE5- FBA48833**** | The ID of the request. |
| Success | String | true | Indicates whether the call was successful. |

**Examples**

Sample requests

```
http(s)://dts.aliyuncs.com/?Action=ConfigureMigrationJob &DestinationEndpoint.InstanceType=RDS &MigrationJobId=dtsl3m1213ye7l**** &MigrationJobName=MySQL_TO_RDS &MigrationMode.DataIntialization=true &MigrationMode.DataSynchronization=true &MigrationMode.StructureIntialization=true &MigrationObject=[{"DBName":"dtstestdata","TableIncludes":[{"TableName":"customer"}]}] &SourceEndpoint.InstanceType=RDS &<Common request parameters>
```

Sample success responses

| XML | format |
|---|---|
| <ConfigureMigrationJobResponse> <RequestId>40E35BD9-002E-4D63-9BE5-FBA48833****</RequestId> <Success>true</Success> </ConfigureMigrationJobResponse> |   |

```json
 "RequestId": "40E35BD9-002E-4D63-9BE5-FBA48833****",
 "Success": true
```

##### 1.5.1.3 StartMigrationJob

Starts a data migration task.

> **Note:** To call this operation, the data migration task must be in the Not Started, Paused, or Migration Failed state.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | StartMigrationJob | The operation that you want to perform. Set the value to StartMigrationJob. |
| MigrationJobId | String | Yes | dtss0611o8vv90**** | The ID of the data migration instance. You can call the DescribeMigrationJobs operation to query the instance ID. |
| RegionId | String | No | cn-hangzhou | The region ID of the data migration instance. |
| AccountId | String | No | 12323344**** | The ID of the Alibaba Cloud account. You do not need to specify this parameter because this parameter will be removed in the future. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| ErrCode | String | InternalError | The error code returned if the call failed. |
| ErrMessage | String | The request processing has failed due to some unknown error. | The error message returned if the call failed. |
| RequestId | String | FDC111B1-ACBF-457D-9656- 247FDEE9**** | The ID of the request. |
| Success | String | true | Indicates whether the call was successful. |

**Examples**

Sample requests

```
http(s)://dts.aliyuncs.com/?Action=StartMigrationJob &MigrationJobId=dtss0611o8vv90**** &<Common request parameters>
```

Sample success responses

| XML | format |
|---|---|
| <StartMigrationJobResponse> <RequestId>FDC111B1-ACBF-457D-9656-247FDEE9****</RequestId> <Success>true</Success> </StartMigrationJobResponse> |   |

| JSON | format |
|---|---|
| { "RequestId": "FDC111B1-ACBF-457D-9656-247FDEE9****", "Success": true } |   |

##### 1.5.1.4 ModifyMigrationObject

Modifies the objects to be migrated for a data migration instance that is not started.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyMigrationObject | The operation that you want to perform. Set the value to ModifyMigrationObject. |

| MigrationJobId | String | Yes | dtskfq1149w254**** | The ID of the data migration instance. You can call the DescribeMigrationJobs operation to query the instance ID. |
|---|---|---|---|---|
| MigrationObject | String | Yes | [{"DBName": "dtstestdata"}] | The objects that you want to migrate after modification. The value is a JSON string and can contain regular expressions. |
| RegionId | String | No | cn-hangzhou | The region ID of the instance. |
| ClientToken | String | No | 0c593ea1-3bea-11e9-b96b- 88e9fe63**** | The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |
| AccountId | String | No | 12323344**** | The ID of your Alibaba Cloud account. You do not need to specify this parameter because this parameter will be removed in the future. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| ErrCode | String | InternalError | The error code returned if the request failed. |
| ErrMessage | String | The request processing has failed due to some unknown error. | The error message returned if the request failed. |
| RequestId | String | DFF8D631-18BF-5768-934F- 55A6613*** | The request ID. |
| Success | String | true | Indicates whether the request was successful. |

**Examples**

Sample requests

```
http(s)://dts.aliyuncs.com/?Action=ModifyMigrationObject &MigrationJobId=dtskfq1149w254**** &MigrationObject=[{"DBName": "dtstestdata"}] &<Common request parameters>
```

Sample success responses

| XML | format |
|---|---|
| <RequestId>DFF8D631-18BF-5768-934F-55A6613***</RequestId> <Success>true</Success> |   |

| JSON | format |
|---|---|
| { "RequestId": "DFF8D631-18BF-5768-934F-55A6613***", "Success": true } |   |

##### 1.5.1.5 SuspendMigrationJob

Pauses a data migration task.

> **Note:** If a data migration task is performing incremental data migration, we recommend that you do not pause the task for more than 6 hours. Otherwise, you cannot call the StartMigrationJob operation to restart the task.
> If you select incremental data migration as the migration type for a pay-as-you-go instance, you are charged even when the task is paused. This is because Data Transmission Service (DTS) stops writing data to the destination database and continues to pull the logs of the source database so that the task can resume quickly after it is restarted. Therefore, data migration consumes resources such as the bandwidth of the source database.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | SuspendMigrationJob | The operation that you want to perform. Set the value to SuspendMigrationJob. |
| MigrationJobId | String | Yes | dtsj1x11y51g3b**** | The ID of the data migration instance. You can call the DescribeMigrationJobs operation to query the instance ID. |

| RegionId | String | No | cn-hangzhou | The region ID of the DTS instance. |
|---|---|---|---|---|
| ClientToken | String | No | 0c593ea1-3bea-11e9-b96b- 88e9fe63**** | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that the value is unique among different requests. The ClientToken value can contain only ASCII characters and cannot exceed 64 characters in length. |
| AccountId | String | No | 12323344**** | The ID of the Alibaba Cloud account. You do not need to specify this parameter because this parameter will be removed in the future. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| ErrCode | String | InternalError | The error code returned if the call failed. |
| ErrMessage | String | The request processing has failed due to some unknown error. | The error message returned if the call failed. |
| RequestId | String | C306C198-7807-409D-930A- D6CE6C32**** | The ID of the request. |
| Success | String | true | Indicates whether the call was successful. |

**Examples**

Sample requests

```
http(s)://dts.aliyuncs.com/?Action=SuspendMigrationJob &SynchronizationJobId=dtsj1x11y51g3b**** &<Common request parameters>
```

Sample success responses

| XML | format |
|---|---|
| <SuspendMigrationJobResponse> <RequestId>C306C198-7807-409D-930A-D6CE6C32****</RequestId> <Success>true</Success> </SuspendMigrationJobResponse> |   |

| JSON | format |
|---|---|
| { "RequestId": "C306C198-7807-409D-930A-D6CE6C32****", "Success": true } |   |

##### 1.5.1.6 DescribeMigrationJobs

Queries the list of data migration instances and the details of each instance.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeMigrationJobs | The operation that you want to perform. Set the value to DescribeMigrationJobs. |
| RegionId | String | No | cn-hangzhou | The region ID of the data migration instance. |
| PageSize | Integer | No | 30 | The number of entries to return on each page. Valid values: 30, 50, and 100. Default value: 30. |
| PageNum | Integer | No | 1 | The number of the page to return. The value must be an integer that is greater than 0. Default value: 1. |
| MigrationJobName | String | No | MySQL Migration | The name of the data migration task. Note Fuzzy match is supported. |
| AccountId | String | No | 12323344**** | The ID of the Alibaba Cloud account. You do not need to specify this parameter because this parameter will be removed in the future. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| ErrCode | String | InternalError | The error code returned if the call failed. |
| ErrMessage | String | The request processing has failed due to some unknown error. | The error message returned if the call failed. |
| MigrationJobs | Array of MigrationJob |   | The list of data migration instances and the details of each instance. |
| MigrationJob |   |   |   |
| DataInitialization | Struct |   | The details of full data migration. |
| ErrorMessage | String | java.lang.NumberFormatExceptio n: For input string: "" | The error message returned if full data migration failed. |
| Percent | String | 100 | The progress of full data migration. Unit: %. |
| Progress | String | 200001 | The number of entries that have been migrated during full data migration. |
| status | String | Finished | The state of full data migration. Valid values: NotStarted: The migration is not started. Migrating: The migration is in progress. Failed: The migration failed. Finished: The migration is complete. |
| DataSynchronization | Struct |   | The details of incremental data migration. |
| Delay | String | 0 | The latency of incremental data migration. Unit: seconds. |
| ErrorMessage | String | The task has failed for a long time and cannot be recovered. | The error message returned if incremental data migration failed. |
| Percent | String | 95 | The progress of incremental data migration. Unit: %. |
| status | String | Catched | The state of incremental data migration. Valid values: NotStarted: The migration is not started. Migrating: The migration is in progress. Failed: The migration failed. Finished: The migration is complete. Catched: The migration has no latency. |
| DestinationEndpoint | Struct |   | The connection settings of the destination instance. |
| DatabaseName | String | dtstestdata | The name of the database that contains the migrated objects in the destination instance. |
| EngineName | String | MySQL | The database type of the destination instance. |
| IP | String | 172.16.88.*** | The endpoint of the destination instance. |
| InstanceID | String | rm-bp1zc3iyqe3qw**** | The ID of the destination instance. |
| InstanceType | String | RDS | The type of the destination instance. |
| OracleSID | String | testsid | This parameter is returned only if the database type of the destination instance is Oracle. |
| Port | String | 3306 | The database service port of the destination instance. |
| UserName | String | dtstest | The database account of the destination instance. |
| MigrationJobClass | String | 2xlarge | The instance class of the data migration instance. Valid values: small, medium, large, xlarge, and 2xlarge. |
| MigrationJobID | String | dtson2z28evm33**** | The ID of the data migration instance. |
| MigrationJobName | String | MySQL Migration | The name of the data migration task. |

| MigrationJobStatus | String | Migrating | The state of the data migration task. Valid values: NotStarted: The migration is not started. Prechecking: The migration is in precheck. PrecheckFailed: The migration failed to pass the precheck. Migrating: The migration is in progress. Suspending: The migration is paused. MigrationFailed: The migration failed. Finished: The migration is complete. |
|---|---|---|---|
| MigrationMode | Struct |   | The migration type. |
| DataInitialization | Boolean | true | Indicates whether full data migration is performed. Valid values: true: yes false: no |
| DataSynchronization | Boolean | true | Indicates whether incremental data migration is performed. Valid values: true: yes false: no |
| StructureInitialization | Boolean | true | Indicates whether schema migration is performed. Valid values: true: yes false: no |
| MigrationObject | Array of SynchronousObject |   | The objects that are migrated by the task. |
| SynchronousObject |   |   |   |
| DatabaseName | String | dtstestdata | The name of the database that contains the objects to be migrated from the source instance. |
| TableList | List | customer | The names of the migrated tables. |
| WholeDatabase | String | false | Indicates whether an entire database is migrated. Valid values: true: yes false: no |
| PayType | String | PostPaid | The billing method of the data migration instance. The value is PostPaid (pay-as-you-go). |
| Precheck | Struct |   | The precheck details. |
| Percent | String | 100 | The precheck progress. Unit: %. |
| Status | String | Success | The precheck result. Valid values: Success: The task passed the precheck. Failed: The task failed to pass the precheck. |
| SourceEndpoint | Struct |   | The connection settings of the source instance. |
| DatabaseName | String | dtstestdata | The name of the database that contains the objects to be migrated from the source instance. |
| EngineName | String | MySQL | The database type of the source instance. |
| IP | String | 172.16.88.*** | The endpoint of the source instance. |
| InstanceID | String | rm-bp1i99e8l7913**** | The ID of the source instance. |
| InstanceType | String | RDS | The type of the source instance. |
| OracleSID | String | testsid | This parameter is returned only if the database type of the source instance is Oracle. |
| Port | String | 3306 | The database service port of the source instance. |
| UserName | String | dtstest | The database account of the source instance. |

| StructureInitialization | Struct |   | The details of schema migration. |
|---|---|---|---|
| ErrorMessage | String | DTS-1020042 Execute sql error sql: ERROR: type "geometry" does not exist; | The error message returned if schema migration failed. |
| Percent | String | 100 | The progress of schema migration. Unit: %. |
| Progress | String | 1 | The number of tables whose schemas have been migrated. |
| status | String | Finished | The state of schema migration. Valid values: NotStarted: The migration is not started. Migrating: The migration is in progress. Failed: The migration failed. Finished: The migration is complete. |
| PageNumber | Integer | 1 | The page number of the returned page. |
| PageRecordCount | Integer | 30 | The maximum number of entries that can be displayed on the current page. |
| RequestId | String | 0ED4846D-ED60-435D-88C0- 7EC0CE4D**** | The ID of the request. |
| Success | String | true | Indicates whether the call was successful. |
| TotalRecordCount | Long | 300 | The total number of data migration instances that belong to your Alibaba Cloud account. |

**Examples**

Sample requests

```
http(s)://dts.aliyuncs.com/?Action=DescribeMigrationJobs &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeMigrationJobsResponse>
      <TotalRecordCount>300</TotalRecordCount>
      <PageRecordCount>30</PageRecordCount>
      <RequestId>0ED4846D-ED60-435D-88C0-7EC0CE4D****</RequestId>
      <PageNumber>1</PageNumber>
      <MigrationJobs>
            <MigrationJob>
                  <DataSynchronization>
                        <Percent>95</Percent>
                        <Delay>0</Delay>
                        <status>Catched</status>
                  </DataSynchronization>
                  <Precheck></Precheck>
                  <InstanceCreateTime>2021-06-22T09:02:13Z</InstanceCreateTime>
                  <JobCreateTime>2021-06-22T08:53:55Z</JobCreateTime>
                  <MigrationJobName>MySQL Migration</MigrationJobName>
                  <PayType>PostPaid</PayType>
                  <MigrationJobStatus>Migrating</MigrationJobStatus>
                  <MigrationMode>
                        <DataInitialization>true</DataInitialization>
                        <DataSynchronization>true</DataSynchronization>
                        <StructureInitialization>true</StructureInitialization>
                  </MigrationMode>
                  <MigrationJobID>dtson2z28evm33****</MigrationJobID>
                  <MigrationObject>
                        <SynchronousObject>
                              <DatabaseName>dtstest</DatabaseName>
                              <WholeDatabase>false</WholeDatabase>
                              <TableList>
                                    <Table>customer</Table>
                              </TableList>
                        </SynchronousObject>
                  </MigrationObject>
                  <DataInitialization>
                        <Progress>200001</Progress>
                        <Percent>100</Percent>
                        <status>Finished</status>
                  </DataInitialization>
                  <DestinationEndpoint>
                        <UserName>dtstest</UserName>
                        <InstanceID>rm-bp1zc3iyqe3qw****</InstanceID>
                        <InstanceType>RDS</InstanceType>
                        <EngineName>MySQL</EngineName>
                  </DestinationEndpoint>
                  <MigrationJobClass>2xlarge</MigrationJobClass>
                  <SourceEndpoint>
                        <UserName>dtstest</UserName>
                        <InstanceID>rm-bp1i99e8l7913****</InstanceID>
                        <InstanceType>RDS</InstanceType>
                        <EngineName>MySQL</EngineName>
                  </SourceEndpoint>
                  <StructureInitialization>
                        <Progress>1</Progress>
                        <Percent>100</Percent>
                        <status>Finished</status>
                  </StructureInitialization>
            </MigrationJob>
      </MigrationJobs>
      <Success>true</Success>
</DescribeMigrationJobsResponse>
```

`JSON` format

```json
    "TotalRecordCount": 300,
    "PageRecordCount": 30,
    "RequestId": "0ED4846D-ED60-435D-88C0-7EC0CE4D****",
    "PageNumber": 1,
    "MigrationJobs": {
        "MigrationJob": [
```

`{`

```json
                "DataSynchronization": {
                    "Percent": "95",
                    "Delay": "0",
                    "status": "Catched"
```

`},`

```json
                "Precheck": {},
                "InstanceCreateTime": "2021-06-22T09:02:13Z",
                "JobCreateTime": "2021-06-22T08:53:55Z",
                "MigrationJobName": "MySQL Migration",
                "PayType": "PostPaid",
                "MigrationJobStatus": "Migrating",
                "MigrationMode": {
                    "DataInitialization": true,
                    "DataSynchronization": true,
                    "StructureInitialization": true
```

`},`

```json
                "MigrationJobID": "dtson2z28evm33****",
                "MigrationObject": {
                    "SynchronousObject": [
```

`{`

```json
                            "DatabaseName": "dtstest",
                            "WholeDatabase": false,
                            "TableList": {
                                "Table": [
                                    "customer"
```

`]` `}` `}` `]` `},`

```json
                "DataInitialization": {
                    "Progress": "200001",
                    "Percent": "100",
                    "status": "Finished"
```

`},`

```json
                "DestinationEndpoint": {
                    "UserName": "dtstest",
                    "InstanceID": "rm-bp1zc3iyqe3qw****",
                    "InstanceType": "RDS",
                    "EngineName": "MySQL"
```

`},`

```json
                "MigrationJobClass": "2xlarge",
                "SourceEndpoint": {
                    "UserName": "dtstest",
                    "InstanceID": "rm-bp1i99e8l7913****",
                    "InstanceType": "RDS",
                    "EngineName": "MySQL"
```

`},`

```json
                "StructureInitialization": {
                    "Progress": "1",
                    "Percent": "100",
                    "status": "Finished"
```

`}` `}` `]` `},`

```json
    "Success": true
```

`}`

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 500 | InternalError | The request processing has failed due to some unknown error. | The error message returned because an internal error has occurred. Try again later. |

##### 1.5.1.7 DescribeMigrationJobDetail

Queries the details of a data migration task. When you call this operation, the data migration task must be in the Migrating, Failed, Paused, or Finished state.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|

| Action | String | Yes | DescribeMigrationJobDetail | The operation that you want to perform. Set the value to DescribeMigrationJobDetail. |
|---|---|---|---|---|
| MigrationJobId | String | Yes | dtsta7w132u12h**** | The ID of the data migration instance. You can call the DescribeMigrationJobs operation to query the instance ID. |
| RegionId | String | No | cn-hangzhou | The region ID of the data migration instance. |
| PageSize | Integer | No | 30 | The number of entries to return on each page. Valid values: 30, 50, and 100. Default value: 30. |
| PageNum | Integer | No | 1 | The number of the page to return. The value must be an integer that is greater than 0. Default value: 1. |
| MigrationMode.StructureIniti alization | Boolean | No | true | Specifies whether to query the details of schema migration. Valid values: true: yes false: no Note The default value is false. |
| MigrationMode.DataInitializat ion | Boolean | No | true | Specifies whether to query the details of full data migration. Valid values: true: yes false: no Note The default value is false. |
| MigrationMode.DataSynchron ization | Boolean | No | true | Specifies whether to query the details of incremental data migration. Valid values: true: yes false: no Note The default value is false. |
| ClientToken | String | No | 0c593ea1-3bea-11e9-b96b- 88e9fe63**** | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that the value is unique among different requests. The ClientToken value can contain only ASCII characters and cannot exceed 64 characters in length. |
| AccountId | String | No | 12323344**** | The ID of the Alibaba Cloud account. You do not need to specify this parameter because this parameter will be removed in the future. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| DataSynchronizationDetai lList | Array of DataSynchronizationDetai l |   | The details of incremental data migration. |
| DataSynchronizationDetai l |   |   |   |
| DestinationOwnerDBNam e | String | dtstestdata | The name of the database that contains the migrated objects in the destination instance. |
| ErrorMessage | String | The task has failed for a long time and cannot be recovered. | The error message returned if incremental data migration failed. |
| SourceOwnerDBName | String | dtstestdata | The name of the database that contains the objects to be migrated from the source instance. |
| Status | String | Migrating | The state of incremental data migration. Valid values: NotStarted: The migration is not started. Migrating: The migration is in progress. Failed: The migration failed. Finished: The migration is complete. |
| TableName | String | customer | The names of tables to be migrated. |
| DataInitializationDetailList | Array of DataInitializationDetail |   | The details of full data migration. |

| DataInitializationDetail |   |   |   |
|---|---|---|---|
| DestinationOwnerDBNam e | String | dtstestdata | The name of the database that contains the migrated objects in the destination instance. |
| ErrorMessage | String | java.lang.NumberFormatExceptio n: For input string: "" | The error message returned if full data migration failed. |
| FinishRowNum | String | 200001 | The number of entries that have been migrated. |
| MigrationTime | String | 0.0 | The amount of time taken by full data migration. |
| SourceOwnerDBName | String | dtstestdata | The name of the database that contains the objects to be migrated from the source instance. |
| Status | String | Finished | The state of full data migration. Valid values: NotStarted: The migration is not started. Migrating: The migration is in progress. Failed: The migration failed. Finished: The migration is complete. |
| TableName | String | customer | The names of tables to be migrated. |
| TotalRowNum | String | 201477 | The total number of entries to be migrated by the task. |
| ErrCode | String | InternalError | The error code returned if the call failed. |
| ErrMessage | String | The request processing has failed due to some unknown error. | The error message returned if the call failed. |
| PageNumber | Integer | 1 | The page number of the returned page. |
| PageRecordCount | Integer | 30 | The number of entries returned per page. |
| RequestId | String | 0AE3CD0B-4148-426F-A90E- 952467CC**** | The ID of the request. |
| StructureInitializationDeta ilList | Array of StructureInitializationDeta il |   | The details of schema migration. |
| StructureInitializationDeta il |   |   |   |
| ConstraintList | Array of StructureInitializationDeta il |   | The constraints of objects to be migrated, such as indexes and foreign keys. Note This parameter is returned only if the ObjectType parameter is set to Table and the migration object has constraints. |
| StructureInitializationDeta il |   |   |   |
| DestinationOwnerDBNam e | String | dtstestdata | The name of the database that contains the migrated objects in the destination instance. |
| ErrorMessage | String | DTS-1020042 Execute sql error sql: ERROR: type "geometry" does not exist; | The error message returned if constraints failed to be created. |
| ObjectDefinition | String | CREATE SEQUENCE "public"."collectionsidseq" _ _ MINVALUE 1 MAXVALUE 9223372036854775807 START 249 INCREMENT BY 1 ; | The syntax to create constraints. |
| ObjectName | String | customer | The name of migration object. |
| ObjectType | String | Table | The type of the object. Table is returned. |
| SourceOwnerDBName | String | dtstestdata | The name of the database that contains the objects to be migrated from the source instance. |

| Status | String | Finished | The state of constraint creation. Valid values: NotStarted: The migration is not started. Migrating: The creation is in progress. Failed: The creation failed. Finished: The creation is complete. |
|---|---|---|---|
| DestinationOwnerDBNam e | String | dtstestdata | The name of the database that contains the migrated objects in the destination instance. |
| ErrorMessage | String | DTS-1020042 Execute sql error sql: DTS-1020042 Execute sql error sql: ERROR: column \"id\" named in key does not exist | The error message returned if schema migration failed. |
| ObjectDefinition | String | CREATE TABLE `dtstestdata`.`customer` (\n`runoobid` int(10) unsigned _ autoincrement COMMENT '' NOT _ NULL , \n`runoobtitle` _ varchar(100) CHARSET `utf8` COLLATE `utf8generalci` _ _ COMMENT '' NOT NULL , \n`runoobauthor1216` _ varchar(40) CHARSET `utf8` COLLATE `utf8generalci` _ _ COMMENT '' NOT NULL , \n`submissiondate1216` date _ COMMENT '' NULL \n, PRIMARY KEY (`runoobid`)) _ engine=InnoDB AUTOINCREMENT=200001 _ DEFAULT CHARSET=`utf8` DEFAULT COLLATE `utf8generalci` ROWFORMAT= _ _ _ Dynamic comment = '' ;\n | The schema of the migration object. |
| ObjectName | String | customer | The name of migration object. |
| ObjectType | String | Table | The type of the migration object. Valid values: Table, Constraint, Index, View, Materialize View, Type, Synonym, Trigger, Function, Procedure, Package, Default, Rule, PlanGuide, and Sequence. |
| SourceOwnerDBName | String | dtstestdata | The name of the database that contains the objects to be migrated from the source instance. |
| Status | String | Finished | The state of schema migration. Valid values: NotStarted: The migration is not started. Migrating: The migration is in progress. Failed: The migration failed. Finished: The migration is complete. |
| Success | String | true | Indicates whether the call was successful. |
| TotalRecordCount | Long | 1 | The total number of returned entries. |

**Examples**

Sample requests

```
http(s)://dts.aliyuncs.com/?Action=DescribeMigrationJobDetail &MigrationJobId=dtsta7w132u12h**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeMigrationJobDetailResponse>
      <DataSynchronizationDetailList>
            <DataSynchronizationDetail>
                  <Status>Migrating</Status>
                  <TableName>customer</TableName>
                  <SourceOwnerDBName>dtstestdata</SourceOwnerDBName>
                  <DestinationOwnerDBName>dtstestdata</DestinationOwnerDBName>
            </DataSynchronizationDetail>
      </DataSynchronizationDetailList>
      <RequestId>0AE3CD0B-4148-426F-A90E-952467CC****</RequestId>
      <DataInitializationDetailList>
            <DataInitializationDetail>
                  <Status>Finished</Status>
                  <TableName>customer</TableName>
                  <TotalRowNum>201477</TotalRowNum>
                  <MigrationTime>0.0</MigrationTime>
                  <SourceOwnerDBName>dtstestdata</SourceOwnerDBName>
                  <DestinationOwnerDBName>dtstestdata</DestinationOwnerDBName>
                  <FinishRowNum>200001</FinishRowNum>
            </DataInitializationDetail>
      </DataInitializationDetailList>
      <Success>true</Success>
      <StructureInitializationDetailList>
            <StructureInitializationDetail>
                  <Status>Finished</Status>
                  <ObjectType>Table</ObjectType>
                  <ObjectDefinition>CREATE TABLE `dtstestdata`.`customer` (
`runoob_id` int(10) unsigned auto_increment COMMENT '' NOT NULL , `runoob_title` varchar(100) CHARSET `utf8` COLLATE `utf8_general_ci` COMMENT '' NOT NULL , `runoob_author1216` varchar(40) CHARSET `utf8` COLLATE `utf8_general_ci` COMMENT '' NOT NULL , `submission_date1216` date COMMENT '' NULL , PRIMARY KEY (`runoob_id`)) engine=InnoDB AUTO_INCREMENT=200001 DEFAULT CHARSET=`utf8` DEFAULT COLLATE `utf8_general_ci` ROW_FORMAT= Dynamic comment = '' ; </ObjectDefinition>
                  <SourceOwnerDBName>dtstestdata</SourceOwnerDBName>
                  <DestinationOwnerDBName>dtstestdata</DestinationOwnerDBName>
                  <ObjectName>customer</ObjectName>
            </StructureInitializationDetail>
      </StructureInitializationDetailList>
</DescribeMigrationJobDetailResponse>
```

`JSON` format

```json
 "DataSynchronizationDetailList": {
  "DataSynchronizationDetail": [
    "Status": "Migrating",
    "TableName": "customer",
    "SourceOwnerDBName": "dtstestdata",
    "DestinationOwnerDBName": "dtstestdata"
```

`}` `]` `},`

```json
 "RequestId": "0AE3CD0B-4148-426F-A90E-952467CC****",
 "DataInitializationDetailList": {
  "DataInitializationDetail": [
```

`{`

```json
    "Status": "Finished",
    "TableName": "customer",
    "TotalRowNum": "201477",
    "MigrationTime": "0.0",
    "SourceOwnerDBName": "dtstestdata",
    "DestinationOwnerDBName": "dtstestdata",
    "FinishRowNum": "200001"
```

`}` `]` `},`

```json
 "Success": true,
 "StructureInitializationDetailList": {
  "StructureInitializationDetail": [
```

`{`

```json
    "Status": "Finished",
    "ObjectType": "Table",
    "ObjectDefinition": "CREATE TABLE `dtstestdata`.`customer` (\n`runoob_id`  int(10) unsigned   auto_increment  COMMENT ''   NOT NULL   , \n`
runoob_title` varchar(100) CHARSET `utf8` COLLATE `utf8_general_ci` COMMENT '' NOT NULL , \n`runoob_author1216` varchar(40) CHARSET `utf8` COLLATE `utf8_general_ci` COMMENT '' NOT NULL , \n`submission_date1216` date COMMENT '' NULL \n, PRIMARY KEY (`runoob_id`)) engine=InnoDB AUTO_INCREMENT=200001 DEFAULT CHARSET=`utf8` DEFAULT COLLATE `utf8_general_ci` ROW_FORMAT= Dynamic comment = '' ;\n",
    "SourceOwnerDBName": "dtstestdata",
    "DestinationOwnerDBName": "dtstestdata",
    "ObjectName": "customer"
```

`}` `]` `}` `}`

##### 1.5.1.8 DescribeMigrationJobStatus

Queries the state of a data migration task.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeMigrationJobStatus | The operation that you want to perform. Set the value to DescribeMigrationJobStatus. |
| MigrationJobId | String | Yes | dtsz2v12jfo309**** | The ID of the data migration instance. You can call the DescribeMigrationJobs operation to query the instance ID. |
| RegionId | String | No | cn-hangzhou | The region ID of the data migration instance. |
| ClientToken | String | No | 0c593ea1-3bea-11e9-b96b- 88e9fe63**** | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that the value is unique among different requests. The ClientToken value can contain only ASCII characters and cannot exceed 64 characters in length. |
| AccountId | String | No | 12323344**** | The ID of the Alibaba Cloud account. You do not need to specify this parameter because this parameter will be removed in the future. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| DataInitializationStatus | Struct |   | The state of full data migration. |
| ErrorMessage | String | java.lang.NumberFormatExceptio n: For input string: "" | The error message returned if full data migration failed. |
| Percent | String | 100 | The progress of full data migration. Unit: %. |

| Progress | String | 200001 | The number of entries that have been migrated during full data migration. |
|---|---|---|---|
| Status | String | Finished | The state of full data migration. Valid values: NotStarted: The migration is not started. Migrating: The migration is in progress. Failed: The migration failed. Finished: The migration is complete. |
| DataSynchronizationStatu s | Struct |   | The state of incremental data migration. |
| Checkpoint | String | 1612507847 | The UNIX timestamp generated when the latest incremental data is migrated. Unit: seconds. |
| Delay | String | 0 | The latency of incremental data migration. Unit: seconds. |
| ErrorMessage | String | The task has failed for a long time and cannot be recovered. | The error message returned if incremental data migration failed. |
| Percent | String | 95 | The progress of incremental data migration. Unit: %. |
| Status | String | Catched | The state of incremental data migration. Valid values: NotStarted: The migration is not started. Migrating: The migration is in progress. Failed: The migration failed. Finished: The migration is complete. Catched: The migration has no latency. |
| DestinationEndpoint | Struct |   | The connection settings of the destination instance. |
| DatabaseName | String | dtstestdata | The name of the database that contains the migrated objects in the destination instance. |
| EngineName | String | MySQL | The database engine of the destination instance. |
| IP | String | 172.16.88.*** | The IP address of the destination instance. |
| InstanceId | String | rm-bp1zc3iyqe3qw**** | The ID of the destination instance. |
| InstanceType | String | RDS | The type of the destination instance. |
| Port | String | 3306 | The database service port of the destination instance. |
| UserName | String | dtstest | The database account of the destination instance. |
| oracleSID | String | testsid | The system ID (SID) of the Oracle database. Note This parameter is returned only if the database engine of the destination instance is Oracle. |
| ErrCode | String | InternalError | The error code returned if the call failed. |
| ErrMessage | String | The request processing has failed due to some unknown error. | The error message returned if the call failed. |
| MigrationJobClass | String | 2xlarge | The instance class of the data migration instance. Valid values: small, medium, large, xlarge, and 2xlarge. |
| MigrationJobId | String | dtsz2v12jfo309**** | The ID of the data migration instance. |
| MigrationJobName | String | MySQL Migration | The name of the data migration task. |

| MigrationJobStatus | String | Migrating | The state of the data migration instance. Valid values: NotStarted: The task is not started. Prechecking: The task is in precheck. PrecheckFailed: The task failed to pass the precheck. Migrating: The task is in progress. Suspending: The task is paused. MigrationFailed: The task failed. Finished: The task is complete. |
|---|---|---|---|
| MigrationMode | Struct |   | The migration type. |
| dataInitialization | Boolean | true | Indicates whether full data migration is performed. Valid values: true: yes false: no |
| dataSynchronization | Boolean | true | Indicates whether incremental data migration is performed. Valid values: true: yes false: no |
| structureInitialization | Boolean | true | Indicates whether schema migration is performed. Valid values: true: yes false: no |
| MigrationObject | String | [{\"DBName\":\"dtstestdata\",\"Ta bleIncludes\": [{\"TableName\":\"customer\"}]}] | The objects that are migrated by the task. |
| PayType | String | PostPaid | The billing method of the data migration instance. PostPaid (pay-as- you-go) is returned. |
| PrecheckStatus | Struct |   | The precheck details. |
| Detail | Array of CheckItem |   | The result of each precheck item. |
| CheckItem |   |   |   |
| CheckStatus | String | Success | The precheck result. Valid values: Success: The task passed the precheck. Failed: The task failed to pass the precheck. |
| ErrorMessage | String | Original error: Access denied for user 'dtstest'@'100.104.***.**' (using password: YES) | The error message returned if the task failed to pass the precheck. Note This parameter is returned only if the return value of the CheckStatus parameter is Failed. |
| ItemName | String | CHECKCONNSRC _ _ | The name of the precheck item. |
| RepairMethod | String | CHECKERRORDESTCONNREP _ _ _ _ AIR2 | The method used to fix the precheck failure. Note This parameter is returned only if the return value of the CheckStatus parameter is Failed. |
| Percent | String | 100 | The precheck progress. Unit: %. |
| Status | String | Success | The precheck state. Valid values: NotStarted: The precheck is not started. Checking: The precheck is in progress. Failed: The precheck failed. Finished: The precheck is complete. |
| RequestId | String | A032E3B4-929B-48E9-97B9- 37587CBF**** | The ID of the request. |
| SourceEndpoint | Struct |   | The connection settings of the source instance. |
| DatabaseName | String | dtstestdatabase | The name of the database that contains the objects to be migrated from the source instance. |
| EngineName | String | MySQL | The database engine of the source instance. |
| IP | String | 172.16.88.*** | The IP address of the source instance. |

| InstanceId | String | rm-bp1i99e8l7913**** | The ID of the source instance. |
|---|---|---|---|
| InstanceType | String | RDS | The type of the source instance. RDS: ApsaraDB RDS instance ECS: self-managed database hosted on Elastic Compute Service (ECS) LocalInstance: self-managed database with a public IP address Express: self-managed database connected over Express Connect, VPN Gateway, or Smart Access Gateway MongoDB: ApsaraDB for MongoDB instance POLARDB: PolarDB for MySQL cluster (available only for the China site) |
| Port | String | 3306 | The database service port of the source instance. |
| UserName | String | dtstest | The database account of the source instance. |
| oracleSID | String | dtstestdatabase | The SID of the Oracle database. Note This parameter is returned only if the database engine of the source instance is Oracle. |
| StructureInitializationStat us | Struct |   | The state of schema migration. |
| ErrorMessage | String | DTS-1020042 Execute sql error sql: ERROR: type "geometry" does not exist; | The error message returned if schema migration failed. |
| Percent | String | 100 | The progress of schema migration. Unit: %. |
| Progress | String | 1 | The number of tables whose schemas have been migrated. |
| Status | String | Finished | The state of schema migration. Valid values: NotStarted: The migration is not started. Migrating: The migration is in progress. Failed: The migration failed. Finished: The migration is complete. |
| Success | String | true | Indicates whether the call was successful. |

**Examples**

Sample requests

```
http(s)://dts.aliyuncs.com/?Action=DescribeMigrationJobStatus &MigrationJobId=dtsta7w132u12h**** &<Common request parameters>
```

Sample success responses

| XML | format |
|---|---|
| <DescribeMigrationJobStatusResponse> <TaskId>z2v12jfo309****</TaskId> <DataInitializationStatus> <Status>Finished</Status> <Progress>200001</Progress> <Percent>100</Percent> </DataInitializationStatus> <RequestId>A032E3B4-929B-48E9-97B9-37587CBF****</RequestId> <MigrationJobName>MySQL Migration</MigrationJobName> <PayType>PostPaid</PayType> <MigrationJobStatus>Migrating</MigrationJobStatus> <Success>true</Success> <MigrationMode> <structureInitialization>true</structureInitialization> <dataSynchronization>true</dataSynchronization> <dataInitialization>true</dataInitialization> </MigrationMode> <MigrationJobId>dtsz2v12jfo309****</MigrationJobId> <PrecheckStatus> <Status>Finished</Status> <Percent>100</Percent> <Detail> <CheckItem> <CheckStatus>Success</CheckStatus> <ItemName>CHECK_CONN_SRC</ItemName> </CheckItem> <CheckItem> |   |

```xml
                        <CheckStatus>Success</CheckStatus>
                        <ItemName>CHECK_AUTH_SRC</ItemName>
                  </CheckItem>
                  <CheckItem>
                        <CheckStatus>Success</CheckStatus>
                        <ItemName>CHECK_CONN_DEST</ItemName>
                  </CheckItem>
                  <CheckItem>
                        <CheckStatus>Success</CheckStatus>
                        <ItemName>CHECK_AUTH_DEST</ItemName>
                  </CheckItem>
                  <CheckItem>
                        <CheckStatus>Success</CheckStatus>
                        <ItemName>CHECK_BINLOG_ON</ItemName>
                  </CheckItem>
                  <CheckItem>
                        <CheckStatus>Success</CheckStatus>
                        <ItemName>CHECK_BINLOG_MODE</ItemName>
                  </CheckItem>
                  <CheckItem>
                        <CheckStatus>Success</CheckStatus>
                        <ItemName>CHECK_BINLOG_ROW_IMAGE</ItemName>
                  </CheckItem>
                  <CheckItem>
                        <CheckStatus>Success</CheckStatus>
                        <ItemName>CHECK_SERVER_ID</ItemName>
                  </CheckItem>
                  <CheckItem>
                        <CheckStatus>Success</CheckStatus>
                        <ItemName>CHECK_BINLOG_EXIST</ItemName>
                  </CheckItem>
                  <CheckItem>
                        <CheckStatus>Success</CheckStatus>
                        <ItemName>CHECK_ENGINE</ItemName>
                  </CheckItem>
                  <CheckItem>
                        <CheckStatus>Success</CheckStatus>
                        <ItemName>CHECK_MYSQL_PASSOWRD_FORMAT</ItemName>
                  </CheckItem>
                  <CheckItem>
                        <CheckStatus>Success</CheckStatus>
                        <ItemName>CHECK_SRC</ItemName>
                  </CheckItem>
                  <CheckItem>
                        <CheckStatus>Success</CheckStatus>
                        <ItemName>CHECK_SQL_MODE</ItemName>
                  </CheckItem>
                  <CheckItem>
                        <CheckStatus>Success</CheckStatus>
                        <ItemName>CHECK_SAME_USER</ItemName>
                  </CheckItem>
            </Detail>
      </PrecheckStatus>
      <DestinationEndpoint>
            <UserName>dtstest</UserName>
            <InstanceId>rm-bp1zc3iyqe3qw****</InstanceId>
            <InstanceType>RDS</InstanceType>
            <EngineName>MySQL</EngineName>
      </DestinationEndpoint>
      <MigrationJobClass>2xlarge</MigrationJobClass>
      <SourceEndpoint>
            <UserName>dtstest</UserName>
            <InstanceId>rm-bp1i99e8l7913****</InstanceId>
            <InstanceType>RDS</InstanceType>
            <EngineName>MySQL</EngineName>
      </SourceEndpoint>
      <DataSynchronizationStatus>
            <Status>Catched</Status>
            <Checkpoint>1612507847</Checkpoint>
            <Percent>95</Percent>
            <Delay>0</Delay>
      </DataSynchronizationStatus>
      <StructureInitializationStatus>
            <Status>Finished</Status>
            <Progress>1</Progress>
            <Percent>100</Percent>
      </StructureInitializationStatus>
</DescribeMigrationJobStatusResponse>
```

| JSON | format |
|---|---|
| { "TaskId": "z2v12jfo309****", "DataInitializationStatus": { "Status": "Finished", "Progress": "200001", "Percent": "100" |   |

```
  Percent: 100
```

`},`

```json
 "RequestId": "A032E3B4-929B-48E9-97B9-37587CBF****",
 "MigrationJobName": "MySQL Migration",
 "PayType": "PostPaid",
 "MigrationJobStatus": "Migrating",
 "Success": true,
 "MigrationMode": {
  "structureInitialization": true,
  "dataSynchronization": true,
  "dataInitialization": true
```

`},`

```json
 "MigrationJobId": "dtsz2v12jfo309****",
 "PrecheckStatus": {
  "Status": "Finished",
  "Percent": "100",
  "Detail": {
   "CheckItem": [
```

`{`

```json
     "CheckStatus": "Success",
     "ItemName": "CHECK_CONN_SRC"
```

`},` `{`

```json
     "CheckStatus": "Success",
     "ItemName": "CHECK_AUTH_SRC"
```

`},` `{`

```json
     "CheckStatus": "Success",
     "ItemName": "CHECK_CONN_DEST"
```

`},` `{`

```json
     "CheckStatus": "Success",
     "ItemName": "CHECK_AUTH_DEST"
```

`},` `{`

```json
     "CheckStatus": "Success",
     "ItemName": "CHECK_BINLOG_ON"
```

`},` `{`

```json
     "CheckStatus": "Success",
     "ItemName": "CHECK_BINLOG_MODE"
```

`},` `{`

```json
     "CheckStatus": "Success",
     "ItemName": "CHECK_BINLOG_ROW_IMAGE"
```

`},` `{`

```json
     "CheckStatus": "Success",
     "ItemName": "CHECK_SERVER_ID"
```

`},` `{`

```json
     "CheckStatus": "Success",
     "ItemName": "CHECK_BINLOG_EXIST"
```

`},` `{`

```json
     "CheckStatus": "Success",
     "ItemName": "CHECK_ENGINE"
```

`},` `{`

```json
     "CheckStatus": "Success",
     "ItemName": "CHECK_MYSQL_PASSOWRD_FORMAT"
```

`},` `{`

```json
     "CheckStatus": "Success",
     "ItemName": "CHECK_SRC"
```

`},` `{`

```json
     "CheckStatus": "Success",
     "ItemName": "CHECK_SQL_MODE"
```

`},` `{`

```json
     "CheckStatus": "Success",
     "ItemName": "CHECK_SAME_USER"
```

`}` `]` `}` `},`

```json
 "DestinationEndpoint": {
  "UserName": "dtstest",
  "InstanceId": "rm-bp1zc3iyqe3qw****",
  "InstanceType": "RDS",
  "EngineName": "MySQL"
```

`},`

```json
 "MigrationJobClass": "2xlarge",
 "SourceEndpoint": {
  "UserName": "dtstest",
  "InstanceId": "rm-bp1i99e8l7913****",
```

```json
  "InstanceType": "RDS",
  "EngineName": "MySQL"
```

`},`

```json
 "DataSynchronizationStatus": {
  "Status": "Catched",
  "Checkpoint": "1612507847",
  "Percent": "95",
  "Delay": "0"
```

`},`

```json
 "StructureInitializationStatus": {
  "Status": "Finished",
  "Progress": "1",
  "Percent": "100"
```

`}` `}`

##### 1.5.1.9 StopMigrationJob

Stops a data migration task that is in the Migrating state.

> **Note:** After you call this operation to stop a data migration task, the state of the task changes to Finished and you cannot restart the task by calling the StartMigrationJob operation.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | StopMigrationJob | The operation that you want to perform. Set the value to StopMigrationJob. |
| MigrationJobId | String | Yes | dtsb2c11sxpi3j**** | The ID of the data migration instance. You can call the DescribeMigrationJobs operation to query the instance ID. |
| RegionId | String | No | cn-hangzhou | The region ID of the data migration instance. |
| ClientToken | String | No | 0c593ea1-3bea-11e9-b96b- 88e9fe63**** | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that the value is unique among different requests. The ClientToken value can contain only ASCII characters and cannot exceed 64 characters in length. |
| AccountId | String | No | 12323344**** | The ID of the Alibaba Cloud account. You do not need to specify this parameter because this parameter will be removed in the future. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| ErrCode | String | InternalError | The error code returned if the call failed. |
| ErrMessage | String | The request processing has failed due to some unknown error. | The error message returned if the call failed. |
| RequestId | String | C306C198-7807-409D-930A- D6CE6C32**** | The ID of the request. |
| Success | String | true | Indicates whether the call was successful. |

**Examples**

Sample requests

```
http(s)://dts.aliyuncs.com/?Action=StopMigrationJob &MigrationJobId=dtsb2c11sxpi3j**** &<Common request parameters>
```

Sample success responses

| XML | format |
|---|---|
| <StopMigrationJobResponse> <RequestId>C306C198-7807-409D-930A-D6CE6C32****</RequestId> <Success>true</Success> </StopMigrationJobResponse> |   |

```json
 "RequestId": "C306C198-7807-409D-930A-D6CE6C32****",
 "Success": true
```

##### 1.5.1.10 DeleteMigrationJob

Releases a data migration instance.

> **Note:** After a data migration instance is released, it cannot be recovered.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteMigrationJob | The operation that you want to perform. Set the value to DeleteMigrationJob. |
| MigrationJobId | String | Yes | dtsyiwe9b0gp2p**** | The ID of the data migration instance. You can call the DescribeMigrationJobs operation to query the instance ID. |
| RegionId | String | No | cn-hangzhou | The region ID of the data migration instance. |
| AccountId | String | No | 12323344**** | The ID of the Alibaba Cloud account. You do not need to specify this parameter because this parameter will be removed in the future. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| ErrCode | String | InternalError | The error code returned if the call failed. |
| ErrMessage | String | The request processing has failed due to some unknown error. | The error message returned if the call failed. |
| RequestId | String | F28A96B1-F897-4246-833B- 310A3345**** | The ID of the request. |
| Success | String | true | Indicates whether the call was successful. |

**Examples**

Sample requests

```
http(s)://dts.aliyuncs.com/?Action=DeleteMigrationJob &MigrationJobId=dtsyiwe9b0gp2p**** &<Common request parameters>
```

Sample success responses

| XML | format |
|---|---|
| <DeleteMigrationJobResponse> <RequestId>F28A96B1-F897-4246-833B-310A3345****</RequestId> <Success>true</Success> </DeleteMigrationJobResponse> |   |

| JSON | format |
|---|---|
| { "RequestId": "F28A96B1-F897-4246-833B-310A3345****", "Success": true } |   |

#### 1.5.2 Data synchronization

##### 1.5.2.1 CreateSynchronizationJob

Purchases a data synchronization instance. After you purchase a data synchronization instance, you must call the ConfigureSynchronizationJob operation to configure a data synchronization task. Then, the task is automatically started.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|

| Action | String | Yes | CreateSynchronizationJob | The operation that you want to perform. Set the value to CreateSynchronizationJob. |
|---|---|---|---|---|
| DestRegion | String | Yes | cn-hangzhou | The region ID of the destination database. Note If the SourceRegion parameter is set to the China (Hong Kong) region or a region outside the Chinese mainland, you must set the DestRegion parameter to the same region ID. |
| PayType | String | Yes | PostPaid | The billing method of the data synchronization instance. Default value: PostPaid. PrePaid: subscription PostPaid: pay-as-you-go |
| SourceRegion | String | Yes | cn-hangzhou | The region ID of the source database. |
| SynchronizationJobClass | String | Yes | small | The instance class of the data synchronization instance. Valid values: micro, small, medium, and large. |
| RegionId | String | No | cn-hangzhou | The region ID of the data synchronization instance. The region ID is the same as the value of the DestRegion parameter. |
| Topology | String | No | oneway | The synchronization topology. Valid values: oneway: one-way synchronization bidirectional: two-way synchronization Note The default value is oneway. This parameter can be set to bidirectional only when the SourceEndpoint.InstanceType and DestinationEndpoint.InstanceType parameters are set to MySQL, PolarDB, or Redis. |
| Period | String | No | Year | The billing cycle of the subscription instance. Valid values: Year Month Note This parameter is required only if you set the PayType parameter to PrePaid. |
| UsedTime | Integer | No | 1 | The subscription duration. Valid values when the Period parameter is set toY ear: 1 to 5. Valid values when the Period parameter is set toM onth: 1 to 60. Note This parameter is required only if you set the PayType parameter to PrePaid. |
| ClientToken | String | No | 0c593ea1-3bea-11e9-b96b- 88e9fe63**** | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that the value is unique among different requests. The ClientToken value can contain only ASCII characters and cannot exceed 64 characters in length. |
| SourceEndpoint.InstanceTyp e | String | No | MySQL | The type of the source instance. Valid values: MySQL: ApsaraDB RDS for MySQL instance or self-managed MySQL database PolarDB: PolarDB for MySQL cluster or PolarDB for Oracle cluster Redis: ApsaraDB for Redis instance DRDS: PolarDB-X 1.0 instance or PolarDB-X 2.0 instance Note The default value is MySQL. |

| DestinationEndpoint.Instance Type | String | No | MySQL | The type of the destination instance. Valid values: MySQL: ApsaraDB RDS for MySQL instance or self-managed MySQL database PolarDB: PolarDB for MySQL cluster or PolarDB for Oracle cluster Redis: ApsaraDB for Redis instance MaxCompute: MaxCompute project Note The default value is MySQL. |
|---|---|---|---|---|
| networkType | String | No | Intranet | The network type. Set the value to Intranet, which indicates a virtual private cloud (VPC). |
| AccountId | String | No | 12323344**** | The ID of the Alibaba Cloud account. You do not need to specify this parameter because this parameter will be removed in the future. |
| DBInstanceCount | Integer | No | 3 | If you set the SourceEndpoint.InstanceType parameter to DRDS, you must specify the DBInstanceCount parameter. This parameter specifies the number of internal ApsaraDB RDS instances attached to the source PolarDB-X instance. Default value: 1. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| ErrCode | String | InternalError | The error code returned if the call failed. |
| ErrMessage | String | The request processing has failed due to some unknown error. | The error message returned if the call failed. |
| RequestId | String | 9056C8B0-5799-493A-9655- 70F607B8**** | The ID of the request. |
| Success | String | true | Indicates whether the call was successful. |
| SynchronizationJobId | String | dtshvj11k25255**** | The ID of the data synchronization instance. |

**Examples**

Sample requests

```
http(s)://dts.aliyuncs.com/?Action=CreateSynchronizationJob &SourceRegion=cn-hangzhou &DestRegion=cn-hangzhou &SynchronizationJobClass=small &PayType=PostPaid &<Common request parameters>
```

Sample success responses

| XML | format |
|---|---|
| <CreateSynchronizationJobResponse> <SynchronizationJobId>dtshvj11k25255****</SynchronizationJobId> <RequestId>9056C8B0-5799-493A-9655-70F607B8****</RequestId> <Success>true</Success> </CreateSynchronizationJobResponse> |   |

| JSON | format |
|---|---|
| { "SynchronizationJobId": "dtshvj11k25255****", "RequestId": "9056C8B0-5799-493A-9655-70F607B8****", "Success": true } |   |

##### 1.5.2.2 ConfigureSynchronizationJob

Configures a data synchronization task. Before you call this operation, you must call the CreateSynchronizationJob operation to create a data synchronization instance.

> **Note:** After you call this operation to configure a data synchronization task, the task automatically starts and the precheck is performed. You do not need to call the StartSynchronizationJob operation to start the task.
> A data synchronization task may fail to be started due to precheck failures. In this case, call the DescribeSynchronizationJobStatus operation to query the state of the task. Then, you can change parameter settings based on the error messages about the precheck failures. After you fix the issue, you must call the StartSynchronizationJob operation to restart the data synchronization task.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ConfigureSynchronizationJob | The operation that you want to perform. Set the value to ConfigureSynchronizationJob. |
| DataInitialization | Boolean | Yes | true | Specifies whether to perform full data synchronization. Valid values: true: yes false: no Note The default value is true. |
| StructureInitialization | Boolean | Yes | true | Specifies whether to perform initial schema synchronization. Valid values: true: yes false: no Note The default value is true. |
| SynchronizationJobId | String | Yes | dtsz4ao1dor13d**** | The ID of the data synchronization instance. |
| SynchronizationObjects | String | Yes | [{"DBName":"dtstestdata","T ableIncludes": [{"TableName":"customer"}] }] | The objects that you want to synchronize. The value is a JSON string and can contain regular expressions. |
| RegionId | String | No | cn-hangzhou | The region ID of the data synchronization instance. |
| SynchronizationJobName | String | No | MySQL Synchronization | The name of the data synchronization task. Note We recommend that you specify a descriptive name that makes it easy to identify. You do not need to use a unique name. |
| SynchronizationDirection | String | No | Forward | The synchronization direction. Valid values: Forward: Data is synchronized from the source database to the destination database. Reverse: Data is synchronized from the destination database to the source database. Note The default value is Forward. The value Reverse takes effect only if the topology of the data synchronization instance is two-way synchronization. |
| SourceEndpoint.InstanceId | String | No | rm-bp1i99e8l7913**** | The ID of the source instance. |
| SourceEndpoint.InstanceTyp e | String | No | RDS | The type of the source instance. Valid values: RDS: ApsaraDB RDS instance Redis: ApsaraDB for Redis instance PolarDB: PolarDB for MySQL cluster or PolarDB for Oracle cluster ECS: self-managed database hosted on Elastic Compute Service (ECS) Express: self-managed database connected over Express Connect dg: self-managed database connected over Database Gateway cen: self-managed database connected over Cloud Enterprise Network (CEN) Note The default value is RDS. |

| SourceEndpoint.IP | String | No | 172.16.88.*** | The IP address of the source database. Note This parameter is available and required only if the SourceEndpoint.InstanceType parameter is set to ECS, Express, dg, or cen. |
|---|---|---|---|---|
| SourceEndpoint.Port | String | No | 3306 | The service port number of the source database. Note This parameter is available and required only if the SourceEndpoint.InstanceType parameter is set to ECS, Express, dg, or cen. |
| SourceEndpoint.UserName | String | No | dtstestaccount | The database account of the source database. Note This parameter is available and required only if the SourceEndpoint.InstanceType parameter is set to ECS, Express, dg, or cen. If the SourceEndpoint.InstanceType parameter is set to Redis, you do not need to specify the database account. The permissions required for the database account to synchronize data vary with the database engine. |
| SourceEndpoint.Password | String | No | Test123456 | The password of the source database account. Note This parameter is available and required only if the SourceEndpoint.InstanceType parameter is set to ECS, Express, dg, or cen. |
| DestinationEndpoint.Instance Id | String | No | rm-bp1r46452ai50**** | The ID of the destination instance. Note If the DestinationEndpoint.InstanceType parameter is set to MaxCompute or DataHub, you must specify the name of the MaxCompute project or the DataHub project. If the destination instance is an AnalyticDB for MySQL cluster, specify the ID of the AnalyticDB for MySQL cluster. |
| DestinationEndpoint.Instance Type | String | No | RDS | The type of the destination instance. Valid values: Redis: ApsaraDB for Redis instance RDS: ApsaraDB RDS instance PolarDB: PolarDB for MySQL cluster or PolarDB for Oracle cluster ECS: self-managed database hosted on ECS Express: self-managed database connected over Express Connect DataHub: DataHub project MaxCompute: MaxCompute project AnalyticDB: AnalyticDB for MySQL V3.0 cluster or AnalyticDB for MySQL V2.0 cluster Greenplum: AnalyticDB for PostgreSQL instance Note The default value is RDS. |
| DestinationEndpoint.IP | String | No | 172.16.88.*** | The IP address of the destination database. Note This parameter is available and required only if the DestinationEndpoint.InstanceType parameter is set to Express, dg, or cen. |
| DestinationEndpoint.Port | String | No | 3306 | The service port number of the destination database. Note This parameter is available and required only if the DestinationEndpoint.InstanceType parameter is set to ECS, Express, dg, or cen. |

| DestinationEndpoint.UserNa me | String | No | dtstestaccount | The database account of the destination database. Note The permissions required for the database account to synchronize data vary with the database engine. This parameter is available and required only if the DestinationEndpoint.InstanceType parameter is set to ECS, Express, dg, or cen. If the DestinationEndpoint.InstanceType parameter is set to RDS and the database version is MySQL 5.5 or MySQL 5.6, you do not need to specify the DestinationEndpoint.UserName or DestinationEndpoint.Password parameter. If the DestinationEndpoint.InstanceType parameter is set to Redis, you do not need to specify the DestinationEndpoint.UserName parameter. |
|---|---|---|---|---|
| DestinationEndpoint.Passwor d | String | No | Test654321 | The password of the destination database account. Note This parameter is available and required only if the DestinationEndpoint.InstanceType parameter is set to ECS, Express, dg, or cen. |
| SourceEndpoint.OwnerID | String | No | 140692647406**** | The ID of the Alibaba Cloud account to which the source instance belongs. Note You can specify this parameter to synchronize data across different Alibaba Cloud accounts. In this case, you must also specify the SourceEndpoint.Role parameter. |
| SourceEndpoint.Role | String | No | ram-for-dts | The name of the Resource Access Management (RAM) role configured for the Alibaba Cloud account that owns the source instance. Note This parameter is required if data is synchronized across Alibaba Cloud accounts. |
| PartitionKey.ModifyTimeYea _ r | Boolean | No | true | Specifies whether the incremental data table contains partitions defined by the modifytimeyear field. Valid values: _ true and false. Note This parameter is available only if the DestinationEndpoint.InstanceType parameter is set to MaxCompute. |
| PartitionKey.ModifyTimeMon _ th | Boolean | No | true | Specifies whether the incremental data table contains partitions defined by the modifytimemonth field. Valid _ values: true and false. Note This parameter is available only if the DestinationEndpoint.InstanceType parameter is set to MaxCompute. |
| PartitionKey.ModifyTimeDay _ | Boolean | No | true | Specifies whether the incremental data table contains partitions defined by the modifytimeday field. Valid values: _ true and false. Note This parameter is available only if the DestinationEndpoint.InstanceType parameter is set to MaxCompute. |
| PartitionKey.ModifyTimeHou _ r | Boolean | No | true | Specifies whether the incremental data table contains partitions defined by the modifytimehour field. Valid values: _ true and false. Note This parameter is available only if the DestinationEndpoint.InstanceType parameter is set to MaxCompute. |
| PartitionKey.ModifyTimeMin _ ute | Boolean | No | true | Specifies whether the incremental data table contains partitions defined by the modifytimeminute field. Valid _ values: true and false. Note This parameter is available only if the DestinationEndpoint.InstanceType parameter is set to MaxCompute. |

| MigrationReserved | String | No | { "autoStartModulesAfterConfi g": "none", "targetTableMode": 2 } | The reserved parameter of DTS. The value is a JSON string. You can specify this parameter to meet specific requirements, for example, whether to automatically start the precheck. Note If data is synchronized between ApsaraDB for Redis Enhanced Edition (Tair) instances, this parameter is available. |
|---|---|---|---|---|
| Checkpoint | String | No | 1610540493 | The synchronization checkpoint. |
| AccountId | String | No | 12323344**** | The ID of the Alibaba Cloud account. You do not need to specify this parameter because this parameter will be removed in the future. |
| SourceEndpoint.DatabaseNa me | String | No | dtstestdata | The name of the database that contains the objects to be synchronized from the source instance. |
| DestinationEndpoint.DataBas eName | String | No | dtstestdata | The name of the database that contains the synchronized objects in the destination instance. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| ErrCode | String | InternalError | The error code returned if the call failed. |
| ErrMessage | String | The request processing has failed due to some unknown error. | The error message returned if the call failed. |
| RequestId | String | 2690E467-7773-43BC-A009- 370EE2E7**** | The ID of the request. |
| Success | String | true | Indicates whether the call was successful. |

**Examples**

Sample requests

```
http(s)://dts.aliyuncs.com/?Action=ConfigureSynchronizationJob &DataInitialization=true &StructureInitialization=true &SynchronizationJobId=dtsz4ao1dor13d**** &SynchronizationObjects=[{"DBName":"dtstestdata","TableIncludes":[{"TableName":"customer"}]}] &<Common request parameters>
```

Sample success responses

| XML | format |
|---|---|
| <ConfigureSynchronizationJobResponse> <RequestId>2690E467-7773-43BC-A009-370EE2E7****</RequestId> <Success>true</Success> </ConfigureSynchronizationJobResponse> |   |

| JSON | format |
|---|---|
| { "RequestId": "2690E467-7773-43BC-A009-370EE2E7****", "Success": true } |   |

##### 1.5.2.3 StartSynchronizationJob

Starts a data synchronization task. When you call this operation, the data synchronization task must be in the NotStarted, Failed, or Suspending state. If you call this operation to start a task that is in the NotStarted state, the precheck is perform on the task.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | StartSynchronizationJob | The operation that you want to perform. Set the value to StartSynchronizationJob. |
| SynchronizationJobId | String | Yes | dtsf19100l2186**** | The ID of the data synchronization instance. You can call the DescribeSynchronizationJobs operation to query the instance ID. |

| RegionId | String | No | cn-hangzhou | The region ID of the Data Transmission Service (DTS) instance. |
|---|---|---|---|---|
| SynchronizationDirection | String | No | Forward | The synchronization direction. Valid values: Forward: Data is synchronized from the source database to the destination database. Reverse: Data is synchronized from the destination database to the source database. Note The default value is Forward. You can set this parameter to Reverse to start the reverse synchronization task only if the topology is two-way synchronization. |
| AccountId | String | No | 12323344**** | The ID of the Alibaba Cloud account. You do not need to specify this parameter because this parameter will be removed in the future. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| ErrCode | String | InternalError | The error code returned if the call failed. |
| ErrMessage | String | The request processing has failed due to some unknown error. | The error message returned if the call failed. |
| RequestId | String | FDC111B1-ACBF-457D-9656- 247FDEE9**** | The ID of the request. |
| Success | String | true | Indicates whether the call was successful. |

**Examples**

Sample requests

```
http(s)://dts.aliyuncs.com/?Action=StartSynchronizationJob &SynchronizationJobId=dtsf19100l2186**** &<Common request parameters>
```

Sample success responses

| XML | format |
|---|---|
| <StartSynchronizationJobresponse> <RequestId>FDC111B1-ACBF-457D-9656-247FDEE9****</RequestId> <Success>true</Success> </StartSynchronizationJobresponse> |   |

| JSON | format |
|---|---|
| { "RequestId": "FDC111B1-ACBF-457D-9656-247FDEE9****", "Success": true } |   |

##### 1.5.2.4 SuspendSynchronizationJob

Pauses a data synchronization task.

> **Note:** When you call this operation, the data synchronization task must be in the Synchronizing state.
> We recommend that you do not pause a data synchronization task for more than 6 hours. Otherwise, the task cannot be started again.
> If the billing method is pay-as-you-go, you are charged even if the task is paused. This is because Data Transmission Service (DTS) stops writing data to the destination database but continues to pull the logs of the source database so that the task can resume quickly after it is restarted. Therefore, the paused data synchronization task still consumes resources such as the bandwidth of the source database.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | SuspendSynchronizationJob | The operation that you want to perform. Set the value to SuspendSynchronizationJob. |
| SynchronizationJobId | String | Yes | dtsmr1q4mc2152**** | The ID of the data synchronization instance. You can call the DescribeSynchronizationJobs operation to query the instance ID. |

| RegionId | String | No | cn-hangzhou | The region ID of the data synchronization instance. |
|---|---|---|---|---|
| SynchronizationDirection | String | No | Forward | The synchronization direction. Valid values: Forward: Data is synchronized from the source database to the destination database. Reverse: Data is synchronized from the destination database to the source database. Note The default value is Forward. You can set this parameter to Reverse to pause the reverse synchronization task only if the topology is two-way synchronization. |
| AccountId | String | No | 12323344**** | The ID of the Alibaba Cloud account. You do not need to specify this parameter because this parameter will be removed in the future. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| ErrCode | String | InternalError | The error code returned if the call failed. |
| ErrMessage | String | The request processing has failed due to some unknown error. | The error message returned if the call failed. |
| RequestId | String | C306C198-7807-409D-930A- D6CE6C32**** | The ID of the request. |
| Success | String | true | Indicates whether the call was successful. |

**Examples**

Sample requests

```
http(s)://dts.aliyuncs.com/?Action=SuspendSynchronizationJob &SynchronizationJobId=dtsmr1q4mc2152**** &<Common request parameters>
```

Sample success responses

| XML | format |
|---|---|
| <SuspendSynchronizationJobResponse> <RequestId>C306C198-7807-409D-930A-D6CE6C32****</RequestId> <Success>true</Success> </SuspendSynchronizationJobResponse> |   |

| JSON | format |
|---|---|
| { "RequestId": "C306C198-7807-409D-930A-D6CE6C32****", "Success": true } |   |

##### 1.5.2.5 ResetSynchronizationJob

Clears the configurations of a data synchronization task.

> **Note:** If you clear the configurations of a data synchronization task, the task will be released. To start the task again, you must call the **ConfigureSynchronizationJob** operation to reconfigure the task.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ResetSynchronizationJob | The operation that you want to perform. Set the value to ResetSynchronizationJob. |
| SynchronizationJobId | String | Yes | dtsm761239l27m**** | The ID of the data synchronization instance. You can call the DescribeSynchronizationJobs operation to query the instance ID. |
| RegionId | String | No | cn-hangzhou | The region ID of the data synchronization instance. |

| SynchronizationDirection | String | No | Forward | The synchronization direction. Valid values: Forward: Data is synchronized from the source database to the destination database. Reverse: Data is synchronized from the destination database to the source database. Note The default value is Forward. You can set this parameter to Reverse to stop reverse synchronization only if the topology is two-way synchronization. |
|---|---|---|---|---|
| AccountId | String | No | 12323344**** | The ID of the Alibaba Cloud account. You do not need to specify this parameter because this parameter will be removed in the future. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| ErrCode | String | InternalError | The error code returned if the call failed. |
| ErrMessage | String | The request processing has failed due to some unknown error. | The error message returned if the call failed. |
| RequestId | String | FDC111B1-ACBF-457D-9656- 247FDEE9**** | The ID of the request. |
| Success | String | true | Indicates whether the call was successful. |

**Examples**

Sample requests

```
http(s)://dts.aliyuncs.com/?Action=ResetSynchronizationJob &SynchronizationJobId=dtsm761239l27m**** &<Common request parameters>
```

Sample success responses

| XML | format |
|---|---|
| <ResetSynchronizationJobResponse> <RequestId>FDC111B1-ACBF-457D-9656-247FDEE9****</RequestId> <Success>true</Success> </ResetSynchronizationJobResponse> |   |

| JSON | format |
|---|---|
| { "RequestId": "FDC111B1-ACBF-457D-9656-247FDEE9****", "Success": true } |   |

##### 1.5.2.6 ModifySynchronizationObject

Modifies the objects to be synchronized.

> **Note:** To call this operation, the data synchronization task must be in the NotStarted or Synchronizing state.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifySynchronizationObject | The operation that you want to perform. Set the value to ModifySynchronizationObject. |
| SynchronizationJobId | String | Yes | dtskfq1149w254**** | The ID of the data synchronization instance. You can call the DescribeSynchronizationJobs operation to query the instance ID. |
| SynchronizationObjects | String | Yes | [{"DBName": "dtstestdata"}] | The objects that you want to synchronize. The value is a JSON string and can contain regular expressions. |
| RegionId | String | No | cn-hangzhou | The region ID of the data synchronization instance. |

| SynchronizationDirection | String | No | Forward | The synchronization direction. Valid values: Forward: Data is synchronized from the source database to the destination database. Reverse: Data is synchronized from the destination database to the source database. Note The default value is Forward. This parameter is required only if the topology of the data synchronization instance is two-way synchronization. |
|---|---|---|---|---|
| AccountId | String | No | 12323344**** | The ID of the Alibaba Cloud account. You do not need to specify this parameter because this parameter will be removed in the future. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| ErrCode | String | InternalError | The error code returned if the call failed. |
| ErrMessage | String | The request processing has failed due to some unknown error. | The error message returned if the call failed. |
| RequestId | String | 902DDCDE-C755-4458-85DA- DF9A323C**** | The ID of the request. |
| Success | String | true | Indicates whether the call was successful. |
| TaskId | String | tl911uvi25z**** | The ID of the data synchronization task. If you want to call the DescribeSynchronizationObjectModifyStatus operation to query the state and progress of the task, this parameter is required. |

**Examples**

Sample requests

```
http(s)://dts.aliyuncs.com/?Action=ModifySynchronizationObject &SynchronizationJobId=dtskfq1149w254**** &SynchronizationObjects=[{"DBName": "dtstestdata"}] &<Common request parameters>
```

Sample success responses

| XML | format |
|---|---|
| <ModifySynchronizationObjectResponse> <TaskId>tl911uvi25z****</TaskId> <RequestId>902DDCDE-C755-4458-85DA-DF9A323C****</RequestId> <Success>true</Success> </ModifySynchronizationObjectResponse> |   |

| JSON | format |
|---|---|
| { "TaskId": "tl911uvi25z****", "RequestId": "902DDCDE-C755-4458-85DA-DF9A323C****", "Success": true } |   |

##### 1.5.2.7 DescribeSynchronizationObjectModifyStatus

Queries the state of the task that modifies the objects to be synchronized. Before you call this operation, you must call the ModifySynchronizationObject operation to obtain the task ID.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeSynchronizationObje ctModifyStatus | The operation that you want to perform. Set the value to DescribeSynchronizationObjectModifyStatus. |
| TaskId | String | Yes | k71r16fj13g**** | The task ID, which is returned after you call the ModifySynchronizationObject operation to modify the objects to be synchronized. |
| RegionId | String | No | cn-hangzhou | The region ID of the data synchronization instance. |

| ClientToken | String | No | 0c593ea1-3bea-11e9-b96b- 88e9fe63**** | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that the value is unique among different requests. The ClientToken value can contain only ASCII characters and cannot exceed 64 characters in length. |
|---|---|---|---|---|
| AccountId | String | No | 12323344**** | The ID of the Alibaba Cloud account. You do not need to specify this parameter because this parameter will be removed in the future. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| DataInitializationStatus | Struct |   | The state of full data synchronization. |
| ErrorMessage | String | java.lang.NumberFormatExceptio n: For input string: "" | The error message returned if full data synchronization failed. |
| Percent | String | 100 | The progress of full data synchronization. Unit: %. |
| Progress | String | 39754 | The number of entries that have been synchronized during full data synchronization. |
| Status | String | Finished | The state of full data synchronization. Valid values: NotStarted: The synchronization is not started. Migrating: The synchronization is in progress. Failed: The synchronization failed. Finished: The synchronization is complete. |
| DataSynchronizationStatu s | Struct |   | The state of incremental data synchronization. Note This parameter and the parameters it contains will be removed in the future. |
| Delay | String | 0 | The latency of incremental data synchronization. Unit: seconds. |
| ErrorMessage | String | The task has failed for a long time and cannot be recovered. | The error message returned if incremental data synchronization failed. |
| Percent | String | 100 | The progress of incremental data synchronization. Unit: %. |
| Status | String | Migrating | The state of incremental data synchronization. Valid values: NotStarted: The synchronization is not started. Migrating: The synchronization is in progress. Failed: The synchronization failed. Finished: The synchronization is complete. |
| ErrCode | String | InternalError | The error code returned if the call failed. |
| ErrMessage | String | The request processing has failed due to some unknown error. | The error message returned if the call failed. |
| ErrorMessage | String | DTS-070211: Connect Source DB failed. cause by [com.mysql.jdbc.exceptions.jdbc 4.MySQLNonTransientConnection Exception:Could not create connection to database server. Attempted reconnect 3 times. Giving up.] [com.mysql.jdbc.exceptions.jdbc 4.CommunicationsException:Com munications link failure\n\nThe last packet sent successfully to the server was 0 milliseconds ago. The driver has not received any packets from the server.] [java.net.ConnectException:Conn ection timed out (Connection timed out)] About more information in [https://yq.aliyun.com/articles/49 9178]. | The error message returned if the task failed to modify the objects to be synchronized. |
| PrecheckStatus | Struct |   | The precheck state. |
| Detail | Array of CheckItem |   | The result of each precheck item. |

| CheckStatus | String | Success | The precheck result. Valid values: Success: The task passed the precheck. Failed: The task failed to pass the precheck. |
|---|---|---|---|
| ErrorMessage | String | Original error: Access denied for user 'dtstest'@'100.104.xxx.xx' (using password: YES) | The error message returned if the task failed to pass the precheck. Note This parameter is returned only if the return value of the CheckStatus parameter is Failed. |
| ItemName | String | CHECKCONNSRC _ _ | The name of the precheck item. |
| RepairMethod | String | CHECKERRORDESTCONNREP _ _ _ _ AIR2 | The method used to fix a precheck failure. Note This parameter is returned only if the return value of the CheckStatus parameter is Failed. |
| Percent | String | 100 | The precheck progress. Unit: %. |
| Status | String | Finished | The precheck state. |
| RequestId | String | B38C644B-4395-4F6F-86E3- 592F26BE**** | The ID of the request. |
| Status | String | Finished | The state of the task that changes the objects to be synchronized. Valid values: NotStarted: The task is not started. Prechecking: The task is in precheck. PrecheckFailed: The task failed to pass the precheck. Migrating: The task is in progress. Failed: The task failed. Finished: The task is complete. |
| StructureInitializationStat us | Struct |   | The state of initial schema synchronization. |
| ErrorMessage | String | DTS-1020042 Execute sql error sql: Table 'customer' already exists | The error message returned if initial schema synchronization failed. |
| Percent | String | 100 | The progress of initial schema synchronization. Unit: %. |
| Progress | String | 1 | The number of tables whose schemas have been synchronized. |
| Status | String | Finished | The state of initial schema synchronization. Valid values: NotStarted: The synchronization is not started. Migrating: The synchronization is in progress. Failed: The synchronization failed. Finished: The synchronization is complete. |
| Success | String | true | Indicates whether the call was successful. |

**Examples**

Sample requests

```
http(s)://dts.aliyuncs.com/?Action=DescribeSynchronizationObjectModifyStatus &TaskId=k71r16fj13g**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<Status>Migrating</Status> <PrecheckStatus>
    <Status>Finished</Status>
    <Percent>100</Percent>
    <Detail>
        <CheckStatus>Success</CheckStatus>
        <ItemName>CHECK_CONN_SRC</ItemName>
    </Detail>
    <Detail>
        <CheckStatus>Success</CheckStatus>
        <ItemName>CHECK_CONN_DEST</ItemName>
    </Detail>
    <Detail>
        <CheckStatus>Success</CheckStatus>
        <ItemName>CHECK_AUTH_SRC</ItemName>
    </Detail>
    <Detail>
        <CheckStatus>Success</CheckStatus>
        <ItemName>CHECK_AUTH_DEST</ItemName>
    </Detail>
    <Detail>
        <CheckStatus>Success</CheckStatus>
        <ItemName>CHECK_BINLOG_ON</ItemName>
    </Detail>
    <Detail>
        <CheckStatus>Success</CheckStatus>
        <ItemName>CHECK_BINLOG_MODE</ItemName>
    </Detail>
    <Detail>
        <CheckStatus>Success</CheckStatus>
        <ItemName>CHECK_BINLOG_ROW_IMAGE</ItemName>
    </Detail>
    <Detail>
        <CheckStatus>Success</CheckStatus>
        <ItemName>CHECK_SERVER_ID</ItemName>
    </Detail>
    <Detail>
        <CheckStatus>Success</CheckStatus>
        <ItemName>CHECK_BINLOG_EXIST</ItemName>
    </Detail>
    <Detail>
        <CheckStatus>Success</CheckStatus>
        <ItemName>CHECK_ENGINE</ItemName>
    </Detail>
    <Detail>
        <CheckStatus>Success</CheckStatus>
        <ItemName>CHECK_MYSQL_PASSOWRD_FORMAT</ItemName>
    </Detail>
    <Detail>
        <CheckStatus>Success</CheckStatus>
        <ItemName>CHECK_SRC</ItemName>
    </Detail>
    <Detail>
        <CheckStatus>Success</CheckStatus>
        <ItemName>CHECK_SAME_OBJ</ItemName>
    </Detail>
    <Detail>
        <CheckStatus>Success</CheckStatus>
        <ItemName>CHECK_SQL_MODE</ItemName>
    </Detail>
    <Detail>
        <CheckStatus>Success</CheckStatus>
        <ItemName>CHECK_SAME_USER</ItemName>
    </Detail>
    <Detail>
        <CheckStatus>Success</CheckStatus>
        <ItemName>CHECK_TOPOLOGY</ItemName>
    </Detail>
</PrecheckStatus> <DataInitializationStatus>
    <Status>Finished</Status>
    <Progress>0</Progress>
    <Percent>100</Percent>
</DataInitializationStatus> <RequestId>0C3D6348-79D8-43F8-9788-60C30CCC****</RequestId> <Success>true</Success> <StructureInitializationStatus>
    <Status>Finished</Status>
    <Progress>0</Progress>
    <Percent>100</Percent>
</StructureInitializationStatus>
```

```json
 "Status": "Migrating",
 "PrecheckStatus": {
  "Status": "Finished",
  "Percent": "100",
  "Detail": [
```

`{`

```json
    "CheckStatus": "Success",
    "ItemName": "CHECK_CONN_SRC"
```

`},` `{`

```json
    "CheckStatus": "Success",
    "ItemName": "CHECK_CONN_DEST"
```

`},` `{`

```json
    "CheckStatus": "Success",
    "ItemName": "CHECK_AUTH_SRC"
```

`},` `{`

```json
    "CheckStatus": "Success",
    "ItemName": "CHECK_AUTH_DEST"
```

`},` `{`

```json
    "CheckStatus": "Success",
    "ItemName": "CHECK_BINLOG_ON"
```

`},` `{`

```json
    "CheckStatus": "Success",
    "ItemName": "CHECK_BINLOG_MODE"
```

`},` `{`

```json
    "CheckStatus": "Success",
    "ItemName": "CHECK_BINLOG_ROW_IMAGE"
```

`},` `{`

```json
    "CheckStatus": "Success",
    "ItemName": "CHECK_SERVER_ID"
```

`},` `{`

```json
    "CheckStatus": "Success",
    "ItemName": "CHECK_BINLOG_EXIST"
```

`},` `{`

```json
    "CheckStatus": "Success",
    "ItemName": "CHECK_ENGINE"
```

`},` `{`

```json
    "CheckStatus": "Success",
    "ItemName": "CHECK_MYSQL_PASSOWRD_FORMAT"
```

`},` `{`

```json
    "CheckStatus": "Success",
    "ItemName": "CHECK_SRC"
```

`},` `{`

```json
    "CheckStatus": "Success",
    "ItemName": "CHECK_SAME_OBJ"
```

`},` `{`

```json
    "CheckStatus": "Success",
    "ItemName": "CHECK_SQL_MODE"
```

`},` `{`

```json
    "CheckStatus": "Success",
    "ItemName": "CHECK_SAME_USER"
```

`},` `{`

```json
    "CheckStatus": "Success",
    "ItemName": "CHECK_TOPOLOGY"
```

`}` `]` `},`

```json
 "DataInitializationStatus": {
  "Status": "Finished",
  "Progress": "0",
  "Percent": "100"
```

`},`

```json
 "RequestId": "0C3D6348-79D8-43F8-9788-60C30CCC****",
 "Success": true,
 "StructureInitializationStatus": {
  "Status": "Finished",
  "Progress": "0",
  "Percent": "100"
```

##### 1.5.2.8 SwitchSynchronizationEndpoint

After a primary/secondary switchover is performed on the source or destination database, you can call the SwitchSynchronizationEndpoint operation to transfer the connection settings to Data Transmission Service (DTS). Then, DTS restarts the data synchronization task from the breakpoint. If the source or destination database is a self-managed MySQL database connected over the Internet, Elastic Compute Service (ECS) or Express Connect, you must call this operation to update the connection settings. If the source or destination database is hosted on an ApsaraDB instance (such as ApsaraDB RDS instance and ApsaraDB for MongoDB instance), DTS automatically updates the connection settings. You do not need to call this operation.

> **Note:** For two-way synchronization tasks, if a primary/secondary switchover is performed on the source or destination database, you must call this operation twice to update the connection settings.
> For example, if a primary/secondary switchover is performed on the destination database in the forward direction, you must call this operation twice. For the first call, set the **SynchronizationDirection** parameter to **Forward** and the **Endpoint.Type** parameter to **Destination** and configure the connection settings. For the second call, set the **SynchronizationDirection** parameter to **Reverse** and the **Endpoint.Type** parameter to **Source** and configure the connection settings.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | SwitchSynchronizationEndpoi nt | The operation that you want to perform. Set the value to SwitchSynchronizationEndpoint. |
| Endpoint.InstanceId | String | Yes | i-bp11haem1kpkhoup**** | The ID of the ECS instance or the virtual private cloud (VPC). Note If the Endpoint.InstanceType parameter is set to ECS, you must specify the ID of the ECS instance. If the Endpoint.InstanceType parameter is set to Express, you must specify the ID of the VPC. |
| Endpoint.InstanceType | String | Yes | ECS | The type of the instance after the switchover. Valid values: LocalInstance: self-managed database with a public IP address ECS: self-managed database hosted on ECS Express: self-managed database that is connected over Express Connect |
| Endpoint.Port | String | Yes | 3306 | The service port number of the database. |
| Endpoint.Type | String | Yes | Destination | Specifies whether to update the connection settings of the source instance or the destination instance. Valid values: Source: updates the connection settings of the source instance. Destination: updates the connection settings of the destination instance. |
| SynchronizationJobId | String | Yes | dtsexjk1alb116**** | The ID of the data synchronization instance. You can call the DescribeSynchronizationJobs operation to query the instance ID. |
| RegionId | String | No | cn-hangzhou | The region ID of the data synchronization instance. |
| SynchronizationDirection | String | No | Forward | The synchronization direction. Valid values: Forward: Data is synchronized from the source database to the destination database. Reverse: Data is synchronized from the destination database to the source database. Note The default value is Forward. The value Reverse takes effect only if the topology of the data synchronization instance is two-way synchronization. |
| Endpoint.IP | String | No | 172.15.185.*** | The IP address of the database after the switchover. Note You must specify the IP address only if the Endpoint.InstanceType parameter is set to Express. |
| SourceEndpoint.OwnerID | String | No | 14069264**** | The ID of the Alibaba Cloud account to which the source instance belongs. If the source and the destination instances belong to different Alibaba Cloud accounts, this parameter is required. |

| SourceEndpoint.Role | String | No | ram-for-dts | The authorized Resource Access Management (RAM) role of the source instance. If the source and the destination instances belong to different Alibaba Cloud accounts, this parameter is required. You can use the RAM role to authorize the Alibaba Cloud account that owns the destination instance to access the source instance. |
|---|---|---|---|---|
| AccountId | String | No | 12323344**** | The ID of the Alibaba Cloud account. You do not need to specify this parameter because this parameter will be removed in the future. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| ErrCode | String | InternalError | The error code returned if the call failed. |
| ErrMessage | String | The request processing has failed due to some unknown error. | The error message returned if the call failed. |
| RequestId | String | 3232F84C-C961-4811-B014- 4EA7A27C**** | The ID of the request. |
| Success | String | true | Indicates whether the call was successful. |
| TaskId | String | 11**** | The task ID. When you call the DescribeEndpointSwitchStatus operation to query the state of the task, you must specify the task ID. |

**Examples**

Sample requests

```
http(s)://dts.aliyuncs.com/?Action=SwitchSynchronizationEndpoint &Endpoint.InstanceId=i-bp11haem1kpkhoup**** &Endpoint.InstanceType=ECS &Endpoint.Port=3306 &Endpoint.Type=Destination &SynchronizationJobId=dtsexjk1alb116**** &<Common request parameters>
```

Sample success responses

| XML | format |
|---|---|
| <SwitchSynchronizationEndpointResponse> <RequestId>3232F84C-C961-4811-B014-4EA7A27C****</RequestId> <Success>true</Success> <TaskId>11****</TaskId> </SwitchSynchronizationEndpointResponse> |   |

| JSON | format |
|---|---|
| { "SwitchSynchronizationEndpointResponse": { "RequestId": "3232F84C-C961-4811-B014-4EA7A27C****", "Success": true, "TaskId": "11****" } } |   |

##### 1.5.2.9 DescribeEndpointSwitchStatus

Queries the state of the task that changes the database connection settings. This operation is always called after you call the SwitchSynchronizationEndpoint operation to change the database connection settings.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeEndpointSwitchStatu s | The operation that you want to perform. Set the value to DescribeEndpointSwitchStatus. |
| TaskId | String | Yes | 11**** | The task ID, which is returned after you call the SwitchSynchronizationEndpoint operation. |
| RegionId | String | No | cn-hangzhou | The region ID of the Data Transmission Service (DTS) instance. |

| ClientToken | String | No | 0c593ea1-3bea-11e9-b96b- 88e9fe63**** | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that the value is unique among different requests. The ClientToken value can contain only ASCII characters and cannot exceed 64 characters in length. |
|---|---|---|---|---|
| AccountId | String | No | 12323344**** | The ID of the Alibaba Cloud account. You do not need to specify this parameter because this parameter will be removed in the future. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| ErrCode | String | InternalError | The error code returned if the call failed. |
| ErrMessage | String | The request processing has failed due to some unknown error. | The error message returned if the call failed. |
| ErrorMessage | String | 400 | This parameter is no longer available. |
| RequestId | String | 0DD6B201-604B-4CAB-B6A8- 4B2953B5**** | The ID of the request. |
| Status | String | Finished | The state of the task. Valid values: NotStarted: The task is not started. Initializing: The task is being initialized. Switching: The task is in progress. Failed: The task failed. Finished: The task is complete. |
| Success | String | true | Indicates whether the call was successful. |

**Examples**

Sample requests

```
http(s)://dts.aliyuncs.com/?Action=DescribeEndpointSwitchStatus &TaskId=11**** &<Common request parameters>
```

Sample success responses

| XML | format |
|---|---|
| <SwitchSynchronizationEndpointResponse> <RequestId>0DD6B201-604B-4CAB-B6A8-4B2953B5****</RequestId> <Status>Finished</Status> <Success>true</Success> </SwitchSynchronizationEndpointResponse> |   |

| JSON | format |
|---|---|
| { "SwitchSynchronizationEndpointResponse": { "RequestId": "0DD6B201-604B-4CAB-B6A8-4B2953B5****", "Status": "Finished", "Success": true } } |   |

##### 1.5.2.10 ConfigureSynchronizationJobReplicatorCompare

Enables or disables image matching for a data synchronization instance. When you use Data Transmission Service (DTS) to synchronize data, other data sources may write data to the destination instance. In this case, data may become inconsistent between the source and destination instances. To ensure data consistency, you can enable image matching. After you call this operation, you can call the DescribeSynchronizationJobReplicatorCompare operation to query whether image matching is enabled for the data synchronization instance.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ConfigureSynchronizationJob ReplicatorCompare | The operation that you want to perform. Set the value to ConfigureSynchronizationJobReplicatorCompare. |
| SynchronizationJobId | String | Yes | dtsexjk1alb116**** | The ID of the data synchronization instance. |

| RegionId | String | No | cn-hangzhou | The region ID of the data synchronization instance. |
|---|---|---|---|---|
| SynchronizationDirection | String | No | Forward | The synchronization direction. Valid values: Forward: Data is synchronized from the source database to the destination database. Reverse: Data is synchronized from the destination database to the source database. Note The default value is Forward. This parameter is required only if the topology of the data synchronization instance is two-way synchronization. |
| SynchronizationReplicatorCo mpareEnable | Boolean | No | true | Specifies whether to enable image matching. Valid values: true: yes false: no |
| ClientToken | String | No | 0c593ea1-3bea-11e9-b96b- 88e9fe63**** | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that the value is unique among different requests. The ClientToken value can contain only ASCII characters and cannot exceed 64 characters in length. |
| AccountId | String | No | 12323344**** | The ID of the Alibaba Cloud account. You do not need to specify this parameter because this parameter will be removed in the future. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| ErrCode | String | InternalError | The error code returned if the call failed. |
| ErrMessage | String | The request processing has failed due to some unknown error. | The error message returned if the call failed. |
| RequestId | String | 86A8FF0F-FA92-449D-B559- 05CFF9F9**** | The ID of the request. |
| Success | String | true | Indicates whether the call was successful. |

**Examples**

Sample requests

```
http(s)://dts.aliyuncs.com/?Action=ConfigureSynchronizationJobReplicatorCompare &SynchronizationJobId=dtsexjk1alb116**** &<Common request parameters>
```

Sample success responses

| XML | format |
|---|---|
| <ConfigureSynchronizationJobReplicatorCompareResponse> <RequestId>86A8FF0F-FA92-449D-B559-05CFF9F9****</RequestId> <Success>true</Success> </ConfigureSynchronizationJobReplicatorCompareResponse> |   |

| JSON | format |
|---|---|
| { "RequestId": "86A8FF0F-FA92-449D-B559-05CFF9F9****", "Success": true } |   |

##### 1.5.2.11 DescribeSynchronizationJobReplicatorCompare

Queries whether image matching is enabled for a data synchronization instance.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeSynchronizationJobR eplicatorCompare | The operation that you want to perform. Set the value to DescribeSynchronizationJobReplicatorCompare. |

| SynchronizationJobId | String | Yes | dtsexjk1alb116**** | The ID of the data synchronization instance. You can call the DescribeSynchronizationJobs operation to query the instance ID. |
|---|---|---|---|---|
| RegionId | String | No | cn-hangzhou | The region ID of the data synchronization instance. |
| SynchronizationDirection | String | No | Forward | The synchronization direction. Valid values: Forward: Data is synchronized from the source database to the destination database. Reverse: Data is synchronized from the destination database to the source database. Note The default value is Forward. This parameter is required only if the topology of the data synchronization instance is two-way synchronization. |
| ClientToken | String | No | 0c593ea1-3bea-11e9-b96b- 88e9fe63**** | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that the value is unique among different requests. The ClientToken value can contain only ASCII characters and cannot exceed 64 characters in length. |
| AccountId | String | No | 12323344**** | The ID of the Alibaba Cloud account. You do not need to specify this parameter because this parameter will be removed in the future. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| ErrCode | String | InternalError | The error code returned if the call failed. |
| ErrMessage | String | The request processing has failed due to some unknown error. | The error message returned if the call failed. |
| RequestId | String | E6EB407F-C59F-4682-A682- A00FA6A2**** | The ID of the request. |
| Success | String | true | Indicates whether the call was successful. |
| SynchronizationReplicator CompareEnable | Boolean | true | Indicates whether image matching is enabled. Valid values: true: yes false: no |

**Examples**

Sample requests

```
http(s)://dts.aliyuncs.com/?Action=DescribeSynchronizationJobReplicatorCompare &SynchronizationJobId=dtsexjk1alb116**** &<Common request parameters>
```

Sample success responses

| XML | format |
|---|---|
| <DescribeSynchronizationJobReplicatorCompareResponse> <RequestId>E6EB407F-C59F-4682-A682-A00FA6A2****</RequestId> <SynchronizationReplicatorCompareEnable>true</SynchronizationReplicatorCompareEnable> <Success>true</Success> </DescribeSynchronizationJobReplicatorCompareResponse> |   |

| JSON | format |
|---|---|
| { "RequestId": "E6EB407F-C59F-4682-A682-A00FA6A2****", "SynchronizationReplicatorCompareEnable": true, "Success": true } |   |

##### 1.5.2.12 DescribeSynchronizationJobs

Queries the list of data synchronization instances and details of each instance.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|

| Action | String | Yes | DescribeSynchronizationJobs | The operation that you want to perform. Set the value to DescribeSynchronizationJobs. |
|---|---|---|---|---|
| RegionId | String | No | cn-hangzhou | The region ID of the data synchronization instance. |
| PageSize | Integer | No | 30 | The number of entries to return on each page. Valid values: 30, 50, and 100. Default value: 30. |
| PageNum | Integer | No | 1 | The number of the page to return. The value must be an integer that is greater than 0. Default value: 1. |
| SynchronizationJobName | String | No | MySQL Synchronization | The name of the data synchronization instance. Note Fuzzy match is supported. |
| ClientToken | String | No | 0c593ea1-3bea-11e9-b96b- 88e9fe63**** | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that the value is unique among different requests. The ClientToken value can contain only ASCII characters and cannot exceed 64 characters in length. |
| AccountId | String | No | 12323344**** | The ID of the Alibaba Cloud account. You do not need to specify this parameter because this parameter will be removed in the future. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| PageNumber | Integer | 1 | The page number of the returned page. |
| PageRecordCount | Integer | 30 | The number of entries returned per page. |
| RequestId | String | 92E1E99D-5224-4AD3-8C94- 23A3516B**** | The ID of the request. |
| SynchronizationInstances | Array of SynchronizationInstance |   | The list of data synchronization instances and details of each instance. |
| CreateTime | String | 2021-06-28 17:34:53.0 | The time when the data synchronization task was created. The time follows the ISO 8601 standard in the yyyy-MM-dd HH:mm:ss.0 format. The time is displayed in UTC. |
| DataInitialization | String | true | Indicates whether initial full data synchronization is performed. Valid values: true: yes false: no |
| DataInitializationStatus | Struct |   | The state of initial full data synchronization. |
| ErrorMessage | String | java.lang.NumberFormatExceptio n: For input string: "" | The error message returned if initial full data synchronization failed. |
| Percent | String | 100 | The progress of initial full data synchronization. Unit: %. |
| Progress | String | 200001 | The number of entries that have been synchronized during initial full data synchronization. |
| Status | String | Finished | The state of initial full data synchronization. Valid values: NotStarted: The synchronization is not started. Migrating: The synchronization is in progress. Failed: The synchronization failed. Finished: The synchronization is complete. |
| DataSynchronizationStatu s | Struct |   | The state of incremental data synchronization. Note This parameter is no longer available. |
| Delay | String | 0 | The latency of incremental data synchronization. Note This parameter is no longer available. |

| ErrorMessage | String | The task has failed for a long time and cannot be recovered. | The error message returned if incremental data synchronization failed. Note This parameter is no longer available. |
|---|---|---|---|
| Percent | String | 100 | The progress of incremental data synchronization. Unit: %. Note This parameter is no longer available. |
| Status | String | Finished | The state of incremental data synchronization. Note This parameter is no longer available. |
| Delay | String | 0 | The synchronization latency. Unit: seconds. |
| DestinationEndpoint | Struct |   | The connection settings of the destination instance. |
| EngineName | String | MySQL | The database engine of the destination instance. |
| IP | String | 172.16.88.*** | The IP address of the destination instance. |
| InstanceId | String | rm-bp162d4tp0500**** | The ID of the destination instance. |
| InstanceType | String | RDS | The type of the destination instance. |
| Port | String | 3306 | The database service port of the destination instance. |
| UserName | String | dtstest | The database account of the destination instance. |
| ErrorMessage | String | DTS-070211: Connect Source DB failed. cause by [com.mysql.jdbc.exceptions.jdbc 4.MySQLNonTransientConnection Exception:Could not create connection to database server. Attempted reconnect 3 times. Giving up.] [com.mysql.jdbc.exceptions.jdbc 4.CommunicationsException:Com munications link failure\n\nThe last packet sent successfully to the server was 0 milliseconds ago. The driver has not received any packets from the server.] [java.net.ConnectException:Conn ection timed out (Connection timed out)] About more information in [https://yq.aliyun.com/articles/49 9178]. | The error message returned if data synchronization failed. |
| ExpireTime | String | 2021-07-07T16:00:00Z | The time when the data synchronization instance expires. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC. Note This parameter is returned only if the value of the PayType parameter is PrePaid. |
| PayType | String | PrePaid | The billing method of the data synchronization instance. Valid values: PrePaid: subscription PostPaid: pay-as-you-go |
| Performance | Struct |   | The performance of the data synchronization instance. |
| FLOW | String | 1 | The size of data that is synchronized per second. Unit: MB/s. |
| RPS | String | 100 | The number of SQL statements that are synchronized per second, including BEGIN, COMMIT, DML, and DDL statements. DML statements include INSERT, DELETE, and UPDATE. |
| PrecheckStatus | Struct |   | The precheck state. |
| Detail | Array of CheckItem |   | The result of each precheck item. |

| CheckStatus | String | Success | The precheck result. Valid values: Success: The task passed the precheck. Failed: The task failed to pass the precheck. |
|---|---|---|---|
| ErrorMessage | String | Original error: Access denied for user 'dtstest'@'100.104.***.**' (using password: YES) | The error message returned if the task failed to pass the precheck. Note This parameter is returned only if the return value of the CheckStatus parameter is Failed. |
| ItemName | String | CHECKCONNSRC _ _ | The name of the precheck item. |
| RepairMethod | String | CHECKERRORDESTCONNREP _ _ _ _ AIR2 | The method used to fix the precheck failure. Note This parameter is returned only if the return value of the CheckStatus parameter is Failed. |
| Percent | String | 100 | The precheck progress. Unit: %. |
| Status | String | Success | The precheck result. Valid values: Success: The task passed the precheck. Failed: The task failed to pass the precheck. |
| SourceEndpoint | Struct |   | The connection settings of the source instance. |
| EngineName | String | MySQL | The database engine of the source instance. |
| IP | String | 172.16.88.*** | The IP address of the source instance. |
| InstanceId | String | rm-bp1i99e8l7913**** | The ID of the source instance. |
| InstanceType | String | RDS | The type of the source instance. |
| Port | String | 3306 | The database service port of the source instance. |
| UserName | String | dtstest | The database account of the source instance. |
| Status | String | synchronizing | The state of the data synchronization task. Valid values: NotStarted: The task is not started. Prechecking: The task is in precheck. PrecheckFailed: The task failed to pass the precheck. Initializing: The task is in initial synchronization. InitializeFailed: Initial synchronization failed. Synchronizing: The task is in progress. Failed: The task failed. Suspending: The task is paused. Modifying: The objects in the task are being modified. Finished: The task is complete. |
| StructureInitialization | String | true | Indicates whether schema synchronization is performed. Valid values: true: yes false: no |
| StructureInitializationStat us | Struct |   | The state of schema synchronization. |
| ErrorMessage | String | DTS-1020042 Execute sql error sql: ERROR: type "geometry" does not exist; | The error message returned if schema synchronization failed. |
| Percent | String | 100 | The progress of schema synchronization. Unit: %. |
| Progress | String | 1 | The number of tables whose schemas have been synchronized. |
| Status | String | Finished | The state of schema synchronization. Valid values: NotStarted: The synchronization is not started. Migrating: The synchronization is in progress. Failed: The synchronization failed. Finished: The synchronization is complete. |

| SynchronizationDirection | String | Forward | The synchronization direction. Valid values: Forward: Data is synchronized from the source database to the destination database. Reverse: Data is synchronized from the destination database to the source database. |
|---|---|---|---|
| SynchronizationJobClass | String | large | The class of the data synchronization instance. |
| SynchronizationJobId | String | dtsexjk1alb116**** | The ID of the data synchronization instance. |
| SynchronizationJobName | String | MySQL Synchronization | The name of the data synchronization instance. |
| SynchronizationObjects | Array of SynchronizationObject |   | The objects that are synchronized by the task. |
| NewSchemaName | String | newdtstestdatabase | The database name that is used in the destination instance. |
| SchemaName | String | dtstestdatabase | The name of the synchronized database. |
| TableExcludes | Array of TableExclude |   | The source tables that are excluded from the data synchronization task. |
| TableName | String | order | The name of the excluded table. |
| TableIncludes | Array of TableInclude |   | The tables that are synchronized by the task. |
| TableName | String | customer | The name of the synchronized table. |
| TotalRecordCount | Long | 100 | The total number of data synchronization instances that meet the requirements and belong to your Alibaba Cloud account. |

**Examples**

Sample requests

```
http(s)://dts.aliyuncs.com/?Action=DescribeSynchronizationJobs &Tag.1.Key=testkey1 &<Common request parameters>
```

Sample success responses

| XML | format |
|---|---|
| <DescribeSynchronizationJobsResponse> <TotalRecordCount>100</TotalRecordCount> <SynchronizationInstances> <Status>synchronizing</Status> <SynchronizationObjects> <SchemaName>dtstestdatabase</SchemaName> <NewSchemaName>newdtstestdatabase</NewSchemaName> </SynchronizationObjects> <DataInitializationStatus> <Status>Finished</Status> <Progress>200001</Progress> <Percent>100</Percent> </DataInitializationStatus> <SynchronizationJobName>MySQL Synchronization</SynchronizationJobName> <InstanceCreateTime>2021-06-28T09:36:32Z</InstanceCreateTime> <CreateTime>2021-06-28 17:34:53.0</CreateTime> <JobCreateTime>2021-06-28T09:34:53Z</JobCreateTime> <PayType>PostPaid</PayType> <Delay>0</Delay> <PrecheckStatus> <Status>Finished</Status> <Percent>100</Percent> <Detail> <CheckStatus>Success</CheckStatus> <ItemName>CHECK_CONN_SRC</ItemName> </Detail> <Detail> <CheckStatus>Success</CheckStatus> <ItemName>CHECK_AUTH_SRC</ItemName> </Detail> <Detail> <CheckStatus>Success</CheckStatus> <ItemName>CHECK_CONN_DEST</ItemName> </Detail> <Detail> <CheckStatus>Success</CheckStatus> |   |

```xml
                        <CheckStatus>Success</CheckStatus>
                        <ItemName>CHECK_AUTH_DEST</ItemName>
                  </Detail>
                  <Detail>
                        <CheckStatus>Success</CheckStatus>
                        <ItemName>CHECK_BINLOG_ON</ItemName>
                  </Detail>
                  <Detail>
                        <CheckStatus>Success</CheckStatus>
                        <ItemName>CHECK_BINLOG_MODE</ItemName>
                  </Detail>
                  <Detail>
                        <CheckStatus>Success</CheckStatus>
                        <ItemName>CHECK_BINLOG_ROW_IMAGE</ItemName>
                  </Detail>
                  <Detail>
                        <CheckStatus>Success</CheckStatus>
                        <ItemName>CHECK_SERVER_ID</ItemName>
                  </Detail>
                  <Detail>
                        <CheckStatus>Success</CheckStatus>
                        <ItemName>CHECK_BINLOG_EXIST</ItemName>
                  </Detail>
                  <Detail>
                        <CheckStatus>Success</CheckStatus>
                        <ItemName>CHECK_ENGINE</ItemName>
                  </Detail>
                  <Detail>
                        <CheckStatus>Success</CheckStatus>
                        <ItemName>CHECK_MYSQL_PASSOWRD_FORMAT</ItemName>
                  </Detail>
                  <Detail>
                        <CheckStatus>Success</CheckStatus>
                        <ItemName>CHECK_SRC</ItemName>
                  </Detail>
                  <Detail>
                        <CheckStatus>Success</CheckStatus>
                        <ItemName>CHECK_SAME_OBJ</ItemName>
                  </Detail>
                  <Detail>
                        <CheckStatus>Success</CheckStatus>
                        <ItemName>CHECK_SQL_MODE</ItemName>
                  </Detail>
                  <Detail>
                        <CheckStatus>Success</CheckStatus>
                        <ItemName>CHECK_SAME_USER</ItemName>
                  </Detail>
                  <Detail>
                        <CheckStatus>Success</CheckStatus>
                        <ItemName>CHECK_TOPOLOGY</ItemName>
                  </Detail>
            </PrecheckStatus>
            <SynchronizationJobId>dtsexjk1alb116lbf1</SynchronizationJobId>
            <DataInitialization>true</DataInitialization>
            <DestinationEndpoint>
                  <InstanceId>rm-bp162d4tp0500****</InstanceId>
                  <InstanceType>RDS</InstanceType>
                  <EngineName>MySQL</EngineName>
            </DestinationEndpoint>
            <SourceEndpoint>
                  <InstanceId>rm-bp1i99e8l7913****</InstanceId>
                  <InstanceType>RDS</InstanceType>
                  <EngineName>MySQL</EngineName>
            </SourceEndpoint>
            <StructureInitialization>true</StructureInitialization>
            <ExpireTime>2021-07-07T16:00:00Z</ExpireTime>
            <Performance>
                  <RPS>0</RPS>
                  <FLOW>0.00MB/s</FLOW>
            </Performance>
            <SynchronizationJobClass>large</SynchronizationJobClass>
            <DataSynchronizationStatus></DataSynchronizationStatus>
            <StructureInitializationStatus>
                  <Status>Finished</Status>
                  <Progress>1</Progress>
                  <Percent>100</Percent>
            </StructureInitializationStatus>
      </SynchronizationInstances>
      <PageRecordCount>30</PageRecordCount>
      <RequestId>92E1E99D-5224-4AD3-8C94-23A3516B****</RequestId>
      <PageNumber>1</PageNumber>
</DescribeSynchronizationJobsResponse>
```

| JSON | format |
|---|---|
| { "TotalRecordCount": 100, |   |

`,`

```json
 "SynchronizationInstances": [
   "Status": "synchronizing",
   "SynchronizationObjects": [
     "TableIncludes": [],
     "TableExcludes": [],
     "SchemaName": "dtstestdatabase",
     "NewSchemaName": "newdtstestdatabase"
```

`}` `],`

```json
   "DataInitializationStatus": {
    "Status": "Finished",
    "Progress": "200001",
    "Percent": "100"
```

`},`

```json
   "SynchronizationJobName": "MySQL Synchronization",
   "InstanceCreateTime": "2021-06-28T09:36:32Z",
            "CreateTime": "2021-06-28 17:34:53.0",
            "JobCreateTime": "2021-06-28T09:34:53Z",
   "PayType": "PostPaid",
   "Delay": "0",
   "PrecheckStatus": {
    "Status": "Finished",
    "Percent": "100",
    "Detail": [
```

`{`

```json
      "CheckStatus": "Success",
      "ItemName": "CHECK_CONN_SRC"
```

`},` `{`

```json
      "CheckStatus": "Success",
      "ItemName": "CHECK_AUTH_SRC"
```

`},` `{`

```json
      "CheckStatus": "Success",
      "ItemName": "CHECK_CONN_DEST"
```

`},` `{`

```json
      "CheckStatus": "Success",
      "ItemName": "CHECK_AUTH_DEST"
```

`},` `{`

```json
      "CheckStatus": "Success",
      "ItemName": "CHECK_BINLOG_ON"
```

`},` `{`

```json
      "CheckStatus": "Success",
      "ItemName": "CHECK_BINLOG_MODE"
```

`},` `{`

```json
      "CheckStatus": "Success",
      "ItemName": "CHECK_BINLOG_ROW_IMAGE"
```

`},` `{`

```json
      "CheckStatus": "Success",
      "ItemName": "CHECK_SERVER_ID"
```

`},` `{`

```json
      "CheckStatus": "Success",
      "ItemName": "CHECK_BINLOG_EXIST"
```

`},` `{`

```json
      "CheckStatus": "Success",
      "ItemName": "CHECK_ENGINE"
```

`},` `{`

```json
      "CheckStatus": "Success",
      "ItemName": "CHECK_MYSQL_PASSOWRD_FORMAT"
```

`},` `{`

```json
      "CheckStatus": "Success",
      "ItemName": "CHECK_SRC"
```

`},` `{`

```json
      "CheckStatus": "Success",
      "ItemName": "CHECK_SAME_OBJ"
```

`},` `{`

```json
      "CheckStatus": "Success",
      "ItemName": "CHECK_SQL_MODE"
```

`},`

```json
      "CheckStatus": "Success",
      "ItemName": "CHECK_SAME_USER"
```

`},`

```json
      "CheckStatus": "Success",
      "ItemName": "CHECK_TOPOLOGY"
```

`]` `},`

```json
   "SynchronizationJobId": "dtsexjk1alb116lbf1",
   "DataInitialization": true,
   "DestinationEndpoint": {
    "InstanceId": "rm-bp162d4tp0500****",
    "InstanceType": "RDS",
    "EngineName": "MySQL"
```

`},`

```json
   "SourceEndpoint": {
    "InstanceId": "rm-bp1i99e8l7913****",
    "InstanceType": "RDS",
    "EngineName": "MySQL"
```

`},`

```json
   "StructureInitialization": true,
   "ExpireTime": "2021-07-07T16:00:00Z",
            "Performance": {
    "RPS": "0",
    "FLOW": "0.00MB/s"
```

`},`

```json
   "SynchronizationJobClass": "large",
   "Tags": [],
   "DataSynchronizationStatus": {},
   "StructureInitializationStatus": {
    "Status": "Finished",
    "Progress": "1",
    "Percent": "100"
```

`}` `}` `],`

```json
 "PageRecordCount": 30,
 "RequestId": "92E1E99D-5224-4AD3-8C94-23A3516B****",
 "PageNumber": 1
```

`}`

##### 1.5.2.13 DescribeInitializationStatus

Queries the details of initial data synchronization, including the synchronization progress of schemas and historical data.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeInitializationStatus | The operation that you want to perform. Set the value to DescribeInitializationStatus. |
| SynchronizationJobId | String | Yes | dtsi76118o3w92**** | The ID of the data synchronization instance. You can call the DescribeSynchronizationJobs operation to query the instance ID. |
| RegionId | String | No | cn-hangzhou | The region ID of the data synchronization instance. |
| PageSize | Integer | No | 30 | The number of entries to return on each page. Valid values:1 to 100. Default value: 30. |
| PageNum | Integer | No | 1 | The number of the page to return. The value must be an integer that is greater than 0. Default value: 1. |
| AccountId | String | No | 12323344**** | The ID of the Alibaba Cloud account. You do not need to specify this parameter because this parameter will be removed in the future. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| DataInitializationDetails | Array of DataInitializationDetail |   | Details of initial full data synchronization. |
| DestinationOwnerDBNam e | String | dtstestdata | The name of the database to which the objects synchronized to the destination instance belong. |
| ErrorMessage | String | java.lang.NumberFormatExceptio n: For input string: "" | The error message returned if initial full data synchronization failed. |

| FinishRowNum | String | 9993 | The total number of rows that are actually synchronized. Note This parameter indicates the total number of actually synchronized rows. In contrast, the value of the TotalRowNum parameter is calculated based on the system tables in the source database. The values of the two parameters may be different due to time difference. |
|---|---|---|---|
| SourceOwnerDBName | String | dtstestdata | The name of the database to which the objects to be synchronized in the source instance belong. |
| Status | String | Finished | The state of initial full data synchronization. Valid values: NotStarted: The synchronization is not started. Migrating: The synchronization is in progress. Failed: The synchronization failed. Finished: The synchronization is complete. |
| TableName | String | customer | The name of the table to which the objects to be synchronized belong. |
| TotalRowNum | String | 9981 | The total number of rows that are supposed to be synchronized. Note The value of this parameter is calculated based on the system tables in the source database. In contrast, the FinishRowNum parameter indicates the total number of actually synchronized rows. The values of the two parameters may be different due to time difference. |
| UsedTime | String | 0.0 | The time spent on initial full data synchronization. |
| DataSynchronizationDetai ls | Array of DataSynchronizationDetai l |   | Details of incremental data synchronization. Note This parameter and the parameters it contains will be removed in the future. |
| DestinationOwnerDBNam e | String | dtstestdata | The name of the database to which the objects synchronized to the destination instance belong. |
| ErrorMessage | String | The task has failed for a long time and cannot be recovered. | The error message returned if incremental data synchronization failed. |
| SourceOwnerDBName | String | dtstestdata | The name of the database to which the objects to be synchronized in the source instance belong. |
| Status | String | Migrating | The state of incremental data synchronization. Valid values: NotStarted: The synchronization is not started. Migrating: The synchronization is in progress. Failed: The synchronization failed. Finished: The synchronization is complete. |
| TableName | String | customer | The name of the table to which the objects to be synchronized belong. |
| ErrCode | String | InternalError | The error code returned if the call failed. |
| ErrMessage | String | The request processing has failed due to some unknown error. | The error message returned if the call failed. |
| RequestId | String | 150DECD9-13FF-4929-A5DE- 855BE9CC**** | The ID of the request. |
| StructureInitializationDeta ils | Array of StructureInitializationDeta il |   | Details of initial schema synchronization. |
| Constraints | Array of StructureInitializationDeta il |   | The constraints of objects to be synchronized, such as indexes and foreign keys. Note This parameter is returned only if the ObjectType parameter is set to Table and the synchronization object has constraints. |
| DestinationOwnerDBNam e | String | dtstestdata | The name of the database to which the objects synchronized to the destination instance belong. |
| ErrorMessage | String | DTS-1020042 Execute sql error sql: ERROR: type "geometry" does not exist | The error message returned if constraints failed to be created. |

| ObjectDefinition | String | CREATE SEQUENCE "public"."collectionsidseq" _ _ MINVALUE 1 MAXVALUE 9223372036854775807 START 249 INCREMENT BY 1 ; | The syntax to create constraints. |
|---|---|---|---|
| ObjectName | String | customer | The name of the object. |
| ObjectType | String | Table | The type of the object. Table is returned. |
| SourceOwnerDBName | String | dtstestdata | The name of the database to which the objects to be synchronized in the source instance belong. |
| Status | String | Finished | The state of constraint creation. Valid values: NotStarted: The creation is not started. Migrating: The creation is in progress. Failed: The creation failed. Finished: The creation is complete. |
| DestinationOwnerDBNam e | String | dtstestdata | The name of the database to which the objects synchronized to the destination instance belong. |
| ErrorMessage | String | DTS-1020042 Execute sql error sql: Table 'customer' already exists | The error message returned if initial schema synchronization failed. |
| ObjectDefinition | String | CREATE TABLE `dtstestdata`.`customer` (\n`customerid` int(10) _ unsigned autoincrement _ COMMENT '' NOT NULL , \n`customertitle` varchar(100) _ CHARSET `utf8` COLLATE `utf8generalci` COMMENT '' _ _ NOT NULL , \n`customercompany1216` _ varchar(40) CHARSET `utf8` COLLATE `utf8generalci` _ _ COMMENT '' NOT NULL , \n`submissiondate1216` date _ COMMENT '' NULL \n, PRIMARY KEY (`customerid`)) _ engine=InnoDB AUTOINCREMENT=200001 _ DEFAULT CHARSET=`utf8` DEFAULT COLLATE `utf8generalci` ROWFORMAT= _ _ _ Dynamic comment = '' ;\n | The schema of the object. |
| ObjectName | String | customer | The name of the object. |
| ObjectType | String | Table | The type of the object. Valid values: Table, Constraint, Index, View, Materialize View, Type, Synonym, Trigger, Function, Procedure, Package, Default, Rule, PlanGuide, and Sequence. |
| SourceOwnerDBName | String | dtstestdata | The name of the database to which the objects to be synchronized in the source instance belong. |
| Status | String | Finished | The state of initial schema synchronization. Valid values: NotStarted: The synchronization is not started. Migrating: The synchronization is in progress. Failed: The synchronization failed. Finished: The synchronization is complete. |
| Success | String | true | Indicates whether the call was successful. |

**Examples**

Sample requests

```
http(s)://dts.aliyuncs.com/?Action=DescribeInitializationStatus &SynchronizationJobId=dtsi76118o3w92**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeInitializationStatusResponse>
      <StructureInitializationDetails>
            <Status>Finished</Status>
            <ObjectType>Table</ObjectType>
            <ObjectDefinition>CREATE TABLE `dtstestdata`.`customer` (
`customer_id` int(10) unsigned auto_increment COMMENT '' NOT NULL , `customer_title` varchar(100) CHARSET `utf8` COLLATE `utf8_general_ci` COMMENT '' NOT NULL , `customer_author1216` varchar(40) CHARSET `utf8` COLLATE `utf8_general_ci` COMMENT '' NOT NULL , `submission_date1216` date COMMENT '' NULL , PRIMARY KEY (`customer_id`)) engine=InnoDB AUTO_INCREMENT=200001 DEFAULT CHARSET=`utf8` DEFAULT COLLATE `utf8_general_ci` ROW_FORMAT= Dynamic comment = '' ; </ObjectDefinition>
            <SourceOwnerDBName>dtstestdata</SourceOwnerDBName>
            <DestinationOwnerDBName>dtstestdata</DestinationOwnerDBName>
            <ObjectName>customer</ObjectName>
      </StructureInitializationDetails>
      <RequestId>150DECD9-13FF-4929-A5DE-855BE9CC****</RequestId>
      <DataInitializationDetails>
            <Status>Finished</Status>
            <TableName>customer</TableName>
            <TotalRowNum>9981</TotalRowNum>
            <UsedTime>0.0</UsedTime>
            <SourceOwnerDBName>dtstestdata</SourceOwnerDBName>
            <DestinationOwnerDBName>dtstestdata</DestinationOwnerDBName>
            <FinishRowNum>9993</FinishRowNum>
      </DataInitializationDetails>
      <Success>true</Success>
</DescribeInitializationStatusResponse>
```

| JSON | format |
|---|---|
| { "StructureInitializationDetails": [ { "Status": "Finished", "ObjectType": "Table", "ObjectDefinition": "CREATE TABLE `dtstestdata`.`customer` (\n`customer_id` int(10) unsigned auto_increment COMMENT '' NOT NULL , \n `customer_title` varchar(100) CHARSET `utf8` COLLATE `utf8_general_ci` COMMENT '' NOT NULL , \n`customer_author1216` varchar(40) CHA RSET `utf8` COLLATE `utf8_general_ci` COMMENT '' NOT NULL , \n`submission_date1216` date COMMENT '' NULL \n, PRIMARY KEY (`cust omer_id`)) engine=InnoDB AUTO_INCREMENT=200001 DEFAULT CHARSET=`utf8` DEFAULT COLLATE `utf8_general_ci` ROW_FORMAT= Dynamic comment = '' ;\n", "SourceOwnerDBName": "dtstestdata", "DestinationOwnerDBName": "dtstestdata", "ObjectName": "customer" } ], "RequestId": "150DECD9-13FF-4929-A5DE-855BE9CC****", "DataInitializationDetails": [ { "Status": "Finished", "TableName": "customer", "TotalRowNum": "9981", "UsedTime": "0.0", "SourceOwnerDBName": "dtstestdata", "DestinationOwnerDBName": "dtstestdata", "FinishRowNum": "9993" } ], "Success": true } |   |

##### 1.5.2.14 DescribeSynchronizationJobStatusList

Queries the state of one or more data synchronization instances.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeSynchronizationJobS tatusList | The operation that you want to perform. Set the value to DescribeSynchronizationJobStatusList. |
| SynchronizationJobIdListJson Str | String | Yes | ["dtsexjk1alb116****","dtskfq 1149w254****"] | The IDs of these data synchronization instances. The value is a JSON array. You can call the DescribeSynchronizationJobs operation to query the instance IDs. |
| RegionId | String | No | cn-hangzhou | The region IDs of these data synchronization instances. |
| ClientToken | String | No | 0c593ea1-3bea-11e9-b96b- 88e9fe63**** | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that the value is unique among different requests. The ClientToken value can contain only ASCII characters and cannot exceed 64 characters in length. |

| AccountId | String | No | 12323344**** | The ID of the Alibaba Cloud account. You do not need to specify this parameter because this parameter will be removed in the future. |
|---|---|---|---|---|

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| ErrCode | String | InternalError | The error code returned if the call failed. |
| ErrMessage | String | The request processing has failed due to some unknown error. | The error message returned if the call failed. |
| PageNumber | Integer | 1 | The page number of the returned page. |
| PageRecordCount | Integer | 2 | The number of data synchronization instances returned per page. |
| RequestId | String | 1413460B-138A-48D1-836C- B24EDDC1**** | The ID of the request. |
| Success | String | true | Indicates whether the call was successful. |
| SynchronizationJobListSta tusList | Array of SynchronizationJobStatusI nfo |   | The states of the data synchronization tasks. |
| SynchronizationDirectionI nfoList | Array of SynchronizationDirectionI nfo |   | The synchronization direction details of these data synchronization tasks. |
| Checkpoint | String | 1610524452 | The UNIX timestamp generated when the latest entry was synchronized. Note You can use a search engine to obtain a UNIX timestamp converter. |
| Status | String | synchronizing | The state of the data synchronization task in this direction. Valid values: NotStarted: The task is not started. Prechecking: The task is in precheck. PrecheckFailed: The task failed to pass the precheck. Initializing: The task is performing initial synchronization. InitializeFailed: Initial synchronization failed. Synchronizing: The task is in progress. Failed: The task failed. Suspending: The task is paused. Modifying: The objects of the task are being modified. Finished: The task is complete. |
| SynchronizationDirection | String | Forward | The synchronization direction. Valid values: Forward: Data is synchronized from the source database to the destination database. Reverse: Data is synchronized from the destination database to the source database. |
| SynchronizationJobId | String | dtsexjk1alb116**** | The ID of the data synchronization instance. |
| TotalRecordCount | Long | 2 | The total number of returned data synchronization instances. |

**Examples**

Sample requests

```
http(s)://dts.aliyuncs.com/?Action=DescribeSynchronizationJobStatusList &SynchronizationJobIdListJsonStr=["dtsexjk1alb116****","dtskfq1149w254****"] &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeSynchronizationJobStatusListResponse>
      <TotalRecordCount>2</TotalRecordCount>
      <PageRecordCount>2</PageRecordCount>
      <RequestId>1413460B-138A-48D1-836C-B24EDDC1****</RequestId>
      <PageNumber>1</PageNumber>
      <SynchronizationJobListStatusList>
            <SynchronizationJobId>dtsexjk1alb116****</SynchronizationJobId>
            <SynchronizationDirectionInfoList>
                  <Status>synchronizing</Status>
                  <Checkpoint>1610524452</Checkpoint>
                  <SynchronizationDirection>Forward</SynchronizationDirection>
            </SynchronizationDirectionInfoList>
      </SynchronizationJobListStatusList>
      <SynchronizationJobListStatusList>
            <SynchronizationJobId>dtskfq1149w254****</SynchronizationJobId>
            <SynchronizationDirectionInfoList>
                  <Status>synchronizing</Status>
                  <Checkpoint>1610524457</Checkpoint>
                  <SynchronizationDirection>Forward</SynchronizationDirection>
            </SynchronizationDirectionInfoList>
      </SynchronizationJobListStatusList>
      <Success>true</Success>
</DescribeSynchronizationJobStatusListResponse>
```

| JSON | format |
|---|---|
| { "TotalRecordCount": 2, "PageRecordCount": 2, "RequestId": "1413460B-138A-48D1-836C-B24EDDC1****", "PageNumber": 1, "SynchronizationJobListStatusList": [ { "SynchronizationJobId": "dtsexjk1alb116****", "SynchronizationDirectionInfoList": [ { "Status": "synchronizing", "Checkpoint": "1610524452", "SynchronizationDirection": "Forward" } ] }, { "SynchronizationJobId": "dtskfq1149w254****", "SynchronizationDirectionInfoList": [ { "Status": "synchronizing", "Checkpoint": "1610524457", "SynchronizationDirection": "Forward" } ] } ], "Success": true } |   |

##### 1.5.2.15 DescribeSynchronizationJobStatus

Queries the state of a data synchronization instance.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeSynchronizationJobS tatus | The operation that you want to perform. Set the value to DescribeSynchronizationJobStatus. |
| SynchronizationJobId | String | Yes | dtsexjk1alb116**** | The ID of the data synchronization instance. You can call the DescribeSynchronizationJobs operation to query the instance ID. |
| RegionId | String | No | cn-hangzhou | The region ID of the data synchronization instance. |

| SynchronizationDirection | String | No | Forward | The synchronization direction. Valid values: Forward: Data is synchronized from the source database to the destination database. Reverse: Data is synchronized from the destination database to the source database. Note The default value is Forward. The value Reverse takes effect only if the topology of the data synchronization instance is two-way synchronization. |
|---|---|---|---|---|
| ClientToken | String | No | 0c593ea1-3bea-11e9-b96b- 88e9fe63**** | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that the value is unique among different requests. The ClientToken value can contain only ASCII characters and cannot exceed 64 characters in length. |
| AccountId | String | No | 12323344**** | The ID of the Alibaba Cloud account. You do not need to specify this parameter because this parameter will be removed in the future. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Checkpoint | String | 1610616144 | The UNIX timestamp generated when the latest entry was synchronized. Note You can use a search engine to obtain a UNIX timestamp converter. |
| DataInitialization | String | true | Indicates whether full data synchronization is performed. Valid values: true: yes false: no |
| DataInitializationStatus | Struct |   | The state of initial full data synchronization. |
| ErrorMessage | String | java.lang.NumberFormatExceptio n: For input string: "" | The error message returned if initial full data synchronization failed. |
| Percent | String | 100 | The progress of full data synchronization. Unit: %. |
| Progress | String | 200001 | The number of entries that have been synchronized during initial full data synchronization. |
| Status | String | Finished | The state of initial full data synchronization. Valid values: NotStarted: The synchronization is not started. Migrating: The synchronization is in progress. Failed: The synchronization failed. Finished: The synchronization is complete. |
| DataSynchronizationStatu s | Struct |   | The state of incremental data synchronization. |
| Checkpoint | String | 1610709865 | The UNIX timestamp generated when the latest entry was synchronized. |
| Delay | String | 0 | The latency of incremental data synchronization. Unit: seconds. |
| DelayMillis | Long | 856 | The latency of incremental data synchronization. Unit: milliseconds. |
| ErrorMessage | String | The task has failed for a long time and cannot be recovered. | The error message returned if incremental data synchronization failed. |
| Percent | String | 100 | The progress of incremental data synchronization. Unit: %. |
| Status | String | Finished | The state of incremental data synchronization. Valid values: NotStarted: The synchronization is not started. Migrating: The synchronization is in progress. Failed: The synchronization failed. Finished: The synchronization is complete. |
| Delay | String | 0 | The synchronization latency. Unit: seconds. |
| DelayMillis | Long | 506 | The synchronization latency. Unit: milliseconds. |

| DestinationEndpoint | Struct |   | The connection settings of the destination instance. |
|---|---|---|---|
| EngineName | String | MySQL | The database engine of the destination instance. |
| IP | String | 172.16.88.*** | The IP address of the destination instance. |
| InstanceId | String | rm-bp162d4tp0500**** | The ID of the destination instance. |
| InstanceType | String | RDS | The type of the destination instance. |
| Port | String | 3306 | The port number of the destination instance. |
| UserName | String | dtstest | The database account of the destination instance. |
| ErrCode | String | InternalError | The error code returned if the call failed. |
| ErrMessage | String | The request processing has failed due to some unknown error. | The error message returned if the call failed. |
| ErrorMessage | String | DTS-070211: Connect Source DB failed. cause by [com.mysql.jdbc.exceptions.jdbc 4.MySQLNonTransientConnection Exception:Could not create connection to database server. Attempted reconnect 3 times. Giving up.] [com.mysql.jdbc.exceptions.jdbc 4.CommunicationsException:Com munications link failure\n\nThe last packet sent successfully to the server was 0 milliseconds ago. The driver has not received any packets from the server.] [java.net.ConnectException:Conn ection timed out (Connection timed out)] About more information in [https://yq.aliyun.com/articles/49 9178]. | The error message returned if data synchronization failed. |
| ExpireTime | String | 2021-03-07T16:00:00Z | The time when the data synchronization instance expires. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC. Note This parameter is returned only if the value of the PayType parameter is PrePaid. |
| PayType | String | PrePaid | The billing method of the data synchronization instance. Valid values: PrePaid: subscription PostPaid: pay-as-you-go |
| Performance | Struct |   | The performance of the data synchronization instance. |
| FLOW | String | 1 | The size of data that is synchronized per second. Unit: MB/s. |
| RPS | String | 100 | The number of times SQL statements are synchronized per second, including BEGIN, COMMIT, DML, and DDL statements. DML statements include INSERT, DELETE, and UPDATE. |
| PrecheckStatus | Struct |   | The precheck state. |
| Detail | Array of CheckItem |   | The result of each precheck item. |
| CheckStatus | String | Success | The precheck result. Valid values: Success: The task passed the precheck. Failed: The task failed to pass the precheck. |
| ErrorMessage | String | Original error: Access denied for user 'dtstest'@'100.104.***.**' (using password: YES) | The error message returned if the task failed to pass the precheck. Note This parameter is returned only if the return value of the CheckStatus parameter is Failed. |
| ItemName | String | CHECKCONNSRC _ _ | The name of the precheck item. |

| RepairMethod | String | CHECKERRORDESTCONNREP _ _ _ _ AIR2 | The method used to fix the precheck failure. Note This parameter is returned only if the return value of the CheckStatus parameter is Failed. |
|---|---|---|---|
| Percent | String | 100 | The precheck progress. Unit: %. |
| Status | String | Success | The precheck result. Valid values: Success: The task passed the precheck. Failed: The task failed to pass the precheck. |
| RequestId | String | DACDF659-AFC6-4DC8-ADB8- 4569419A4**** | The ID of the request. |
| SourceEndpoint | Struct |   | The connection settings of the source instance. |
| EngineName | String | MySQL | The database engine of the source instance. |
| IP | String | 172.16.88.*** | The IP address of the source instance. |
| InstanceId | String | rm-bp1i99e8l7913**** | The ID of the source instance. |
| InstanceType | String | RDS | The type of the source instance. |
| Port | String | 3306 | The port number of the source instance. |
| UserName | String | dtstest | The database account of the source instance. |
| Status | String | synchronizing | The state of the data synchronization instance. Valid values: notStarted: The task is not started. prechecking: The task is in precheck. precheckFailed: The task failed to pass the precheck. initializing: The task is in initial data synchronization. initializeFailed: Initial data synchronization failed. synchronizing: The task is in progress. failed: The task failed. suspending: The task is paused. modifying: The objects of the task are being modified. finished: The task is complete. |
| StructureInitialization | String | true | Indicates whether schema synchronization is performed. Valid values: true: yes false: no |
| StructureInitializationStat us | Struct |   | The state of schema synchronization. |
| ErrorMessage | String | DTS-1020042 Execute sql error sql: ERROR: type "geometry" does not exist; | The error message returned if schema synchronization failed. |
| Percent | String | 100 | The progress of schema synchronization. Unit: %. |
| Progress | String | 1 | The number of tables whose schemas have been synchronized. |
| Status | String | Finished | The state of schema synchronization. Valid values: NotStarted: The synchronization is not started. Migrating: The synchronization is in progress. Failed: The synchronization failed. Finished: The synchronization is complete. |
| Success | String | true | Indicates whether the call was successful. |
| SynchronizationDirection | String | Forward | The synchronization direction. Valid values: Forward: Data is synchronized from the source database to the destination database. Reverse: Data is synchronized from the destination database to the source database. |
| SynchronizationJobClass | String | large | The instance class of the data synchronization instance. |

| SynchronizationJobName | String | MySQL Synchronization | The name of the data synchronization task. |
|---|---|---|---|
| SynchronizationJobId | String | dtsexjk1alb116**** | The ID of the data synchronization instance. |
| SynchronizationObjects | Array of SynchronizationObject |   | The objects that are synchronized by the task. |
| NewSchemaName | String | newdtstestdatabase | The database name that is used in the destination instance. |
| SchemaName | String | dtstestdatabase | The name of the synchronized database. |
| TableExcludes | Array of TableExclude |   | The source tables that are excluded from the data synchronization task. |
| TableName | String | order | The name of the excluded table. |
| TableIncludes | Array of TableInclude |   | The tables that are synchronized by the task. |
| TableName | String | customer | The name of the synchronized table. |

**Examples**

Sample requests

```
http(s)://dts.aliyuncs.com/?Action=DescribeSynchronizationJobStatus &SynchronizationJobId=dtsexjk1alb116**** &<Common request parameters>
```

Sample success responses

| XML | format |
|---|---|
| <DescribeSynchronizationJobStatusResponse> <TaskId>exjk1alb116****</TaskId> <SynchronizationObjects> <SchemaName>newdtstestdatabase</SchemaName> <NewSchemaName>dtstestdatabase</NewSchemaName> </SynchronizationObjects> <DataInitializationStatus> <Status>Finished</Status> <Progress>200001</Progress> <Percent>100</Percent> </DataInitializationStatus> <Delay>0</Delay> <Success>true</Success> <DelayMillis>0</DelayMillis> <DataInitialization>true</DataInitialization> <SynchronizationJobClass>large</SynchronizationJobClass> <Status>synchronizing</Status> <RequestId>DACDF659-AFC6-4DC8-ADB8-4569419A****</RequestId> <SynchronizationJobName>MySQL Synchronization</SynchronizationJobName> <PayType>PostPaid</PayType> <ErrMessage></ErrMessage> <PrecheckStatus> <Status>Finished</Status> <Percent>100</Percent> <Detail> <CheckStatus>Success</CheckStatus> <ItemName>CHECK_CONN_SRC</ItemName> </Detail> <Detail> <CheckStatus>Success</CheckStatus> <ItemName>CHECK_AUTH_SRC</ItemName> </Detail> <Detail> <CheckStatus>Success</CheckStatus> <ItemName>CHECK_CONN_DEST</ItemName> </Detail> <Detail> <CheckStatus>Success</CheckStatus> <ItemName>CHECK_AUTH_DEST</ItemName> </Detail> <Detail> <CheckStatus>Success</CheckStatus> <ItemName>CHECK_BINLOG_ON</ItemName> </Detail> <Detail> <CheckStatus>Success</CheckStatus> <ItemName>CHECK_BINLOG_MODE</ItemName> </Detail> <Detail> |   |

```xml
            <Detail>
                  <CheckStatus>Success</CheckStatus>
                  <ItemName>CHECK_BINLOG_ROW_IMAGE</ItemName>
            </Detail>
            <Detail>
                  <CheckStatus>Success</CheckStatus>
                  <ItemName>CHECK_SERVER_ID</ItemName>
            </Detail>
            <Detail>
                  <CheckStatus>Success</CheckStatus>
                  <ItemName>CHECK_BINLOG_EXIST</ItemName>
            </Detail>
            <Detail>
                  <CheckStatus>Success</CheckStatus>
                  <ItemName>CHECK_ENGINE</ItemName>
            </Detail>
            <Detail>
                  <CheckStatus>Success</CheckStatus>
                  <ItemName>CHECK_MYSQL_PASSOWRD_FORMAT</ItemName>
            </Detail>
            <Detail>
                  <CheckStatus>Success</CheckStatus>
                  <ItemName>CHECK_SRC</ItemName>
            </Detail>
            <Detail>
                  <CheckStatus>Success</CheckStatus>
                  <ItemName>CHECK_SAME_OBJ</ItemName>
            </Detail>
            <Detail>
                  <CheckStatus>Success</CheckStatus>
                  <ItemName>CHECK_SQL_MODE</ItemName>
            </Detail>
            <Detail>
                  <CheckStatus>Success</CheckStatus>
                  <ItemName>CHECK_SAME_USER</ItemName>
            </Detail>
            <Detail>
                  <CheckStatus>Success</CheckStatus>
                  <ItemName>CHECK_TOPOLOGY</ItemName>
            </Detail>
      </PrecheckStatus>
      <Checkpoint>1610616144</Checkpoint>
      <SynchronizationJobId>dtsexjk1alb116****</SynchronizationJobId>
      <DestinationEndpoint>
            <InstanceId>rm-bp1u40w1ip917****</InstanceId>
            <InstanceType>RDS</InstanceType>
            <EngineName>MySQL</EngineName>
      </DestinationEndpoint>
      <SourceEndpoint>
            <InstanceId>rm-bp1i99e8l7913****</InstanceId>
            <InstanceType>RDS</InstanceType>
            <EngineName>MySQL</EngineName>
      </SourceEndpoint>
      <StructureInitialization>true</StructureInitialization>
      <Performance>
            <RPS>0</RPS>
            <FLOW>0.00MB/s</FLOW>
      </Performance>
      <StructureInitializationStatus>
            <Status>Finished</Status>
            <Progress>1</Progress>
            <Percent>100</Percent>
      </StructureInitializationStatus>
</DescribeSynchronizationJobStatusResponse>
```

| JSON | format |
|---|---|
| { "TaskId": "exjk1alb116****", "SynchronizationObjects": [ { "TableIncludes": [], "TableExcludes": [], "SchemaName": "newdtstestdatabase", "NewSchemaName": "dtstestdatabase" } ], "DataInitializationStatus": { "Status": "Finished", "Progress": "200001", "Percent": "100" }, "Delay": "0", "Success": true, "DelayMillis": 0, "DataInitialization": true, "SynchronizationJobClass": "large", |   |

`y` `g` `,`

```json
 "Status": "synchronizing",
 "RequestId": "DACDF659-AFC6-4DC8-ADB8-4569419A****",
 "SynchronizationJobName": "MySQL Synchronization",
 "PayType": "PostPaid",
 "ErrMessage": "",
 "PrecheckStatus": {
  "Status": "Finished",
  "Percent": "100",
  "Detail": [
```

`{`

```json
    "CheckStatus": "Success",
    "ItemName": "CHECK_CONN_SRC"
```

`},` `{`

```json
    "CheckStatus": "Success",
    "ItemName": "CHECK_AUTH_SRC"
```

`},` `{`

```json
    "CheckStatus": "Success",
    "ItemName": "CHECK_CONN_DEST"
```

`},` `{`

```json
    "CheckStatus": "Success",
    "ItemName": "CHECK_AUTH_DEST"
```

`},` `{`

```json
    "CheckStatus": "Success",
    "ItemName": "CHECK_BINLOG_ON"
```

`},` `{`

```json
    "CheckStatus": "Success",
    "ItemName": "CHECK_BINLOG_MODE"
```

`},` `{`

```json
    "CheckStatus": "Success",
    "ItemName": "CHECK_BINLOG_ROW_IMAGE"
```

`},` `{`

```json
    "CheckStatus": "Success",
    "ItemName": "CHECK_SERVER_ID"
```

`},` `{`

```json
    "CheckStatus": "Success",
    "ItemName": "CHECK_BINLOG_EXIST"
```

`},` `{`

```json
    "CheckStatus": "Success",
    "ItemName": "CHECK_ENGINE"
```

`},` `{`

```json
    "CheckStatus": "Success",
    "ItemName": "CHECK_MYSQL_PASSOWRD_FORMAT"
```

`},` `{`

```json
    "CheckStatus": "Success",
    "ItemName": "CHECK_SRC"
```

`},` `{`

```json
    "CheckStatus": "Success",
    "ItemName": "CHECK_SAME_OBJ"
```

`},` `{`

```json
    "CheckStatus": "Success",
    "ItemName": "CHECK_SQL_MODE"
```

`},` `{`

```json
    "CheckStatus": "Success",
    "ItemName": "CHECK_SAME_USER"
```

`},` `{`

```json
    "CheckStatus": "Success",
    "ItemName": "CHECK_TOPOLOGY"
```

`}` `]` `},`

```json
 "Checkpoint": "1610616144",
 "SynchronizationJobId": "dtsexjk1alb116****",
 "DestinationEndpoint": {
  "InstanceId": "rm-bp1u40w1ip917****",
  "InstanceType": "RDS",
  "EngineName": "MySQL"
```

`},`

```json
 "SourceEndpoint": {
  "InstanceId": "rm-bp1i99e8l7913****",
  "InstanceType": "RDS",
  "EngineName": "MySQL"
```

`},`

```json
 "StructureInitialization": true,
 "Performance": {
  "RPS": "0",
  "FLOW": "0.00MB/s"
```

`},`

```json
 "StructureInitializationStatus": {
  "Status": "Finished",
  "Progress": "1",
  "Percent": "100"
```

`}` `}`

##### 1.5.2.16 DeleteSynchronizationJob

Releases a data synchronization instance.

> **Note:** After a data synchronization instance is released, it cannot be recovered.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteSynchronizationJob | The operation that you want to perform. Set the value to DeleteSynchronizationJob. |
| SynchronizationJobId | String | Yes | dtshn6107ve264**** | The ID of the data synchronization instance. You can call the DescribeSynchronizationJobs operation to query the instance ID. |
| RegionId | String | No | cn-hangzhou | The region ID of the data synchronization instance. |
| AccountId | String | No | 12323344**** | The ID of the Alibaba Cloud account. You do not need to specify this parameter because this parameter will be removed in the future. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| ErrCode | String | InternalError | The error code returned if the call failed. |
| ErrMessage | String | The request processing has failed due to some unknown error. | The error message returned if the call failed. |
| RequestId | String | C306C198-7807-409D-930A- D6CE6C32**** | The ID of the request. |
| Success | String | true | Indicates whether the call was successful. |

**Examples**

Sample requests

```
http(s)://dts.aliyuncs.com/?Action=DeleteSynchronizationJob &SynchronizationJobId=dtshn6107ve264**** &<Common request parameters>
```

Sample success responses

| XML | format |
|---|---|
| <DeleteSynchronizationJobResponse> <RequestId>C306C198-7807-409D-930A-D6CE6C32****</RequestId> <Success>true</Success> </DeleteSynchronizationJobResponse> |   |

| JSON | format |
|---|---|
| { "RequestId": "C306C198-7807-409D-930A-D6CE6C32****", "Success": true } |   |

#### 1.5.3 Change tracking

##### 1.5.3.1 CreateSubscriptionInstance

Purchases a change tracking instance.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateSubscriptionInstance | The operation that you want to perform. Set the value to CreateSubscriptionInstance. |
| Region | String | Yes | cn-hangzhou | The region ID of the change tracking instance. The region must be the same as that of the objects for change tracking. |
| RegionId | String | No | cn-hangzhou | The region ID of the change tracking instance. You do not need to specify this parameter because this parameter will be removed in the future. |
| SourceEndpoint.InstanceTyp e | String | No | MySQL | The type of the source instance. Valid values: MySQL, PolarDB, DRDS, and Oracle. Note The default value is MySQL. |
| PayType | String | No | Prepaid | The billing method of the change tracking instance. Default value: PostPaid. Postpaid: pay-as-you-go Prepaid: subscription |
| Period | String | No | Month | The billing cycle of the subscription instance. Valid values: Year Month Note This parameter is available and required only if you set the PayType parameter to PrePaid. |
| UsedTime | Integer | No | 12 | The subscription duration. Valid values when the Period parameter is set toY ear: 1 to 5. Valid values when the Period parameter is set toM onth: 1 to 60. Note This parameter is available and required only if you set the PayType parameter to PrePaid. |
| ClientToken | String | No | 0c593ea1-3bea-11e9-b96b- 88e9fe63**** | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that the value is unique among different requests. The ClientToken value can contain only ASCII characters and cannot exceed 64 characters in length. |
| AccountId | String | No | 12323344**** | The ID of the Alibaba Cloud account. You do not need to specify this parameter because this parameter will be removed in the future. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| ErrCode | String | InternalError | The error code returned if the call failed. |
| ErrMessage | String | The request processing has failed due to some unknown error. | The error message returned if the call failed. |
| RequestId | String | 4E9564C5-F99D-4176-A6BA- 2D7F2DC8**** | The ID of the request. |
| SubscriptionInstanceId | String | dtsfen11q2g23x**** | The ID of the change tracking instance. |
| Success | String | true | Indicates whether the call was successful. |

**Examples**

Sample requests

```
http(s)://dts.aliyuncs.com/?Action=CreateSubscriptionInstance &Region=cn-hangzhou &<Common request parameters>
```

```xml
<CreateSubscriptionInstanceResponse>
      <RequestId>4E9564C5-F99D-4176-A6BA-2D7F2DC8****</RequestId>
      <SubscriptionInstanceId>dtsfen11q2g23x****</SubscriptionInstanceId>
</CreateSubscriptionInstanceResponse>
```

| JSON | format |
|---|---|
| { "RequestId": "4E9564C5-F99D-4176-A6BA-2D7F2DC8****", "SubscriptionInstanceId": "dtsfen11q2g23x****", "Success": true } |   |

##### 1.5.3.2 ConfigureSubscriptionInstance

Configures a change tracking instance. Before you call this operation, you must call the CreateSubscriptionInstance operation to create a change tracking instance.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ConfigureSubscriptionInstanc e | The operation that you want to perform. Set the value to ConfigureSubscriptionInstance. |
| SubscriptionDataType.DDL | Boolean | Yes | true | Specifies whether to track DDL statements. Default value: true. Valid values: true: yes false: no |
| SubscriptionDataType.DML | Boolean | Yes | true | Specifies whether to track DML statements. Default value: true. Valid values: true: yes false: no |
| SubscriptionObject | String | Yes | [{ "DBName": "dtstestdata" }] | The objects whose changes you want to track. The value is a JSON string and can contain regular expressions. |
| SubscriptionInstanceId | String | Yes | dtshp8n2ze4r5x**** | The ID of the change tracking instance. |
| RegionId | String | No | cn-hangzhou | The region ID of the change tracking instance. |
| SubscriptionInstanceName | String | No | MySQL Change Tracking | The name of the change tracking instance. Note We recommend that you specify a descriptive name that makes it easy to identify. You do not need to use a unique name. |
| SourceEndpoint.InstanceTyp e | String | No | RDS | The type of the source instance. Valid values: RDS: ApsaraDB RDS for MySQL instance PolarDB: PolarDB for MySQL cluster LocalInstance: self-managed database with a public IP address ECS: self-managed database hosted on Elastic Compute Service (ECS) Express: self-managed database connected over Express Connect CEN: self-managed database connected over Cloud Enterprise Network (CEN) dg: self-managed database that is connected over Database Gateway Note The engine of a self-managed database can be MySQL or Oracle. You must call the CreateSubscriptionInstance operation to specify the engine type. |
| SourceEndpoint.InstanceID | String | No | rm-bp1zc3iyqe3qw**** | The ID of the source instance. Note This parameter is available and required only if the source instance is an ApsaraDB RDS for MySQL instance, a PolarDB-X 1.0 instance, or a PolarDB for MySQL cluster. |

| SourceEndpoint.IP | String | No | 172.16.88.*** | The IP address of the source database. Note This parameter is available and required only if the source database is a self-managed database. |
|---|---|---|---|---|
| SourceEndpoint.Port | String | No | 3306 | The service port number of the source database. Note This parameter is available and required only if the source database is a self-managed database. |
| SourceEndpoint.UserName | String | No | dtstestaccount | The database account of the source instance. Note The permissions required for the database account to track data changes vary with the database engine. |
| SourceEndpoint.Password | String | No | Test123456 | The password of the source database account. |
| SourceEndpoint.OracleSID | String | No | testsid | The system ID (SID) of the Oracle database. Note This parameter is available and required only if the source database is a self-managed Oracle database and the Oracle database is deployed in a non- RAC architecture. |
| SourceEndpoint.DatabaseNa me | String | No | dtstestdata | The name of the source database. |
| SourceEndpoint.OwnerID | String | No | 140692647406**** | The ID of the Alibaba Cloud account to which the source instance belongs. Note This parameter is available and required only if you track data changes across different Alibaba Cloud accounts. |
| SourceEndpoint.Role | String | No | ram-for-dts | The authorized Resource Access Management (RAM) role of the source instance. This parameter is required only if the source instance does not belong to the Alibaba Cloud account that you use to configure the change tracking task. In this case, you must allow the Alibaba Cloud account that you use to configure the change tracking task to access the source instance. |
| SubscriptionInstanceNetwork Type | String | No | vpc | The network type of the change tracking instance. Valid values: classic: classic network vpc: virtual private cloud (VPC) Note If you specify this parameter, the new version of the change tracking feature is used. Otherwise, the old version of this feature is used. The old version of the change tracking feature supports self-managed MySQL databases, ApsaraDB RDS for MySQL instances, and DRDS instances. The new version of the change tracking feature supports self-managed MySQL databases, ApsaraDB RDS for MySQL instances, PolarDB for MySQL clusters, and Oracle databases. If you set this parameter to vpc, you must also specify the SubscriptionInstanceVPCId and SubscriptionInstanceVSwitchID parameters. |
| SubscriptionInstance.VPCId | String | No | vpc-bp1vwnn14rqpyiczj**** | The ID of the VPC where the change tracking instance is deployed. Note This parameter is available and required only if the SubscriptionInstanceNetworkType parameter is set to vpc. |
| SubscriptionInstance.VSwitch Id | String | No | vsw- bp10df3mxae6lpmku**** | The ID of the vSwitch in the specified VPC. Note This parameter is available and required only if the SubscriptionInstanceNetworkType parameter is set to vpc. |
| AccountId | String | No | 12323344**** | The ID of the Alibaba Cloud account. You do not need to specify this parameter because this parameter will be removed in the future. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| ErrCode | String | InternalError | The error code returned if the call failed. |
| ErrMessage | String | The request processing has failed due to some unknown error. | The error message returned if the call failed. |
| RequestId | String | 0CC15092-8957-4532-B559- B4FB80AC**** | The ID of the request. |
| Success | String | true | Indicates whether the call was successful. |

**Examples**

Sample requests

```
http(s)://dts.aliyuncs.com/?Action=ConfigureSubscriptionInstance &SubscriptionDataType.DDL=true &SubscriptionDataType.DML=true &SubscriptionInstanceId=dtshp8n2ze4r5x**** &SubscriptionObject=[{"DBName":"dtstestdata","TableIncludes":[{"TableName":"customer"}]}] &<Common request parameters>
```

Sample success responses

| XML | format |
|---|---|
| <ConfigureSubscriptionInstanceResponse> <RequestId>0CC15092-8957-4532-B559-B4FB80AC****</RequestId> <Success>true</Success> </ConfigureSubscriptionInstanceResponse> |   |

| JSON | format |
|---|---|
| { "RequestId": "0CC15092-8957-4532-B559-B4FB80AC****", "Success": true } |   |

##### 1.5.3.3 StartSubscriptionInstance

Starts a change tracking instance. To call this operation, the change tracking task must be in the NotStarted or Failed state.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | StartSubscriptionInstance | The operation that you want to perform. Set the value to StartSubscriptionInstance. |
| SubscriptionInstanceId | String | Yes | dtso6m11cxt26q**** | The ID of the change tracking instance. You can call the DescribeSubscriptionInstances operation to query the instance ID. |
| RegionId | String | No | cn-hangzhou | The region ID pf the change tracking instance. |
| AccountId | String | No | 12323344**** | The ID of the Alibaba Cloud account. You do not need to specify this parameter because this parameter will be removed in the future. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| ErrCode | String | InternalError | The error code returned if the call failed. |
| ErrMessage | String | The request processing has failed due to some unknown error. | The error message returned if the call failed. |
| RequestId | String | B083F9AB-BE9B-4716-8AD3- CFA04391**** | The ID of the request. |
| Success | String | true | Indicates whether the call was successful. |
| TaskId | String | 11**** | The task ID. This parameter will be removed in the future. |

```
http(s)://dts.aliyuncs.com/?Action=StartSubscriptionInstance &SubscriptionInstanceId=dtso6m11cxt26q**** &<Common request parameters>
```

Sample success responses

| XML | format |
|---|---|
| <StartSubscriptionInstanceResponse> <TaskId>11****</TaskId> <RequestId>B083F9AB-BE9B-4716-8AD3-CFA04391****</RequestId> <Success>true</Success> </StartSubscriptionInstanceResponse> |   |

| JSON | format |
|---|---|
| { "TaskId": "11****", "RequestId": "B083F9AB-BE9B-4716-8AD3-CFA04391****", "Success": true } |   |

##### 1.5.3.4 ModifySubscriptionObject

Modifies the objects for a change tracking task. To call this operation, the change tracking task must be in the Normal, NotStarted, or Failed state.

> **Note:** If you call this operation to modify the objects of a change tracking task that is in the Normal state, Data Transmission Service (DTS) automatically calls StartSubscriptionInstance to restart the change tracking instance.
> If you call this operation to modify the objects of a change tracking task that is in the NotStarted or Failed state, DTS does not automatically restart the change tracking instance. You must call the StartSubscriptionInstance operation.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifySubscriptionObject | The operation that you want to perform. Set the value to ModifySubscriptionObject. |
| SubscriptionInstanceId | String | Yes | dtsl8zl9ek6292**** | The ID of the change tracking instance. You can call the DescribeSubscriptionInstances operation to query the instance ID. |
| SubscriptionObject | String | Yes | [{"DBName":"dtstestdata"}] | The objects whose changes you want to track. The value is a JSON string and can contain regular expressions. |
| RegionId | String | No | cn-hangzhou | The region ID of the change tracking instance. |
| AccountId | String | No | 12323344**** | The ID of the Alibaba Cloud account. You do not need to specify this parameter because this parameter will be removed in the future. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| ErrCode | String | InternalError | The error code returned if the call failed. |
| ErrMessage | String | The request processing has failed due to some unknown error. | The error message returned if the call failed. |
| RequestId | String | ABBACEFC-CBA9-4F80-A337- 42F202F5**** | The ID of the request. |
| Success | String | true | Indicates whether the call was successful. |

**Examples**

Sample requests

```
http(s)://dts.aliyuncs.com/?Action=ModifySubscriptionObject &SubscriptionInstanceId=dtsl8zl9ek6292**** &SubscriptionObject=[{"DBName":"dtstestdata"}]
```

| XML | format |
|---|---|
| <ModifySubscriptionObjectResponse> <RequestId>ABBACEFC-CBA9-4F80-A337-42F202F5****</RequestId> <Success>true</Success> </ModifySubscriptionObjectResponse> |   |

| JSON | format |
|---|---|
| { "RequestId": "ABBACEFC-CBA9-4F80-A337-42F202F5****", "Success": true } |   |

##### 1.5.3.5 Manage consumer groups

###### 1.5.3.5.1 CreateConsumerGroup

Creates a consumer group for a change tracking instance.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateConsumerGroup | The operation that you want to perform. Set the value to CreateConsumerGroup. |
| ConsumerGroupName | String | Yes | Test Consumer Group | The name of the consumer group. The name can be up to 128 characters in length. We recommend that you use a descriptive name that makes it easy to identify. |
| ConsumerGroupPassword | String | Yes | Test123456 | The password that corresponds to the username of the consumer group. The password must contain at least two of the following character types: uppercase letters, lowercase letters, digits, and special characters. The password must be 8 to 32 characters in length. |
| ConsumerGroupUserName | String | Yes | dtstest | The username of the consumer group. The username can contain uppercase letters, lowercase letters, digits, and underscores (). _ The username cannot exceed 16 characters in length. |
| SubscriptionInstanceId | String | Yes | dtsg2m10r1x15a**** | The ID of the change tracking instance. You can call the DescribeSubscriptionInstances operation to query the instance ID. |
| RegionId | String | No | cn-hangzhou | The region ID of the change tracking instance. |
| AccountId | String | No | 12323344**** | The ID of the Alibaba Cloud account. You do not need to specify this parameter because this parameter will be removed in the future. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| ConsumerGroupID | String | dtswc411cg617p**** | The ID of the consumer group. |
| ErrCode | String | InternalError | The error code returned if the call failed. |
| ErrMessage | String | The request processing has failed due to some unknown error. | The error message returned if the call failed. |
| RequestId | String | 6063641E-BAD1-4BA7-B70B- 26FFFD18**** | The ID of the request. |
| Success | String | true | Indicates whether the call was successful. |

**Examples**

Sample requests

```
http(s)://dts.aliyuncs.com/?Action=CreateConsumerGroup &ConsumerGroupName=Test Consumer Group &ConsumerGroupPassword=Test123456 &ConsumerGroupUserName=dtstest &SubscriptionInstanceId=dtsg2m10r1x15a**** &<Common request parameters>
```

Sample success responses

| XML | format |
|---|---|
| <CreateConsumerGroupResponse> <ConsumerGroupID>dtswc411cg617p****</ConsumerGroupID> <RequestId>6063641E-BAD1-4BA7-B70B-26FFFD18****</RequestId> <Success>true</Success> </CreateConsumerGroupResponse> |   |

| JSON | format |
|---|---|
| { "ConsumerGroupID": "dtswc411cg617p****", "RequestId": "6063641E-BAD1-4BA7-B70B-26FFFD18****", "Success": true } |   |

###### 1.5.3.5.2 DescribeConsumerGroup

Queries the details of consumer groups in a change tracking instance.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeConsumerGroup | The operation that you want to perform. Set this parameter to DescribeConsumerGroup. |
| SubscriptionInstanceId | String | Yes | dtso5xx5t9u19e**** | The ID of the change tracking instance. You can call the DescribeSubscriptionInstances operation to query the instance ID. |
| RegionId | String | No | cn-hangzhou | The region ID of the change tracking instance. |
| PageSize | Integer | No | 30 | The number of entries to return on each page. Valid values: 30, 50, and 100. Default value: 30. |
| PageNum | Integer | No | 1 | The number of the page to return. The value must be an integer that is greater than 0. Default value: 1. |
| AccountId | String | No | 12323344**** | The ID of the Alibaba Cloud account. You do not need to specify this parameter because this parameter will be removed in the future. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| ConsumerChannels | Array of DescribeConsumerChanne l |   | Details of the consumer groups. |
| DescribeConsumerChanne l |   |   |   |
| ConsumerGroupID | String | dtspis1110z232**** | The ID of the consumer group. |
| ConsumerGroupName | String | consumergrouptest | The name of the consumer group. |
| ConsumerGroupUserNam e | String | test | The username of the consumer group. |
| ConsumptionCheckpoint | String | 2019-10-02T12:00:00Z | The consumption checkpoint, which is the time when the latest data record was consumed by the change tracking client. The time is displayed in the yyyy-MM-ddTHH:mm:ssZ format in UTC. |

| MessageDelay | Long | 172714 | The message latency, which is calculated by using the following formula: Message latency = Current time - Timestamp of the earliest unconsumed message in the change tracking instance. Unit: seconds. Note If -1 is returned for this parameter, no client is connected to the consumer group. |
|---|---|---|---|
| UnconsumedData | Long | 186600 | The total number of unconsumed messages, which is calculated by using the following formula: Total number of unconsumed messages = Number of unconsumed data records + Number of heartbeat messages. Note If -1 is returned for this parameter, no client is connected to the consumer group. |
| ErrCode | String | InternalError | The error code returned if the call failed. |
| ErrMessage | String | The request processing has failed due to some unknown error. | The error message returned if the call failed. |
| PageNumber | Integer | 1 | The page number of the returned page. |
| PageRecordCount | Integer | 30 | The maximum number of consumer groups that can be displayed on one page. |
| RequestId | String | 4204E899-8193-4D7D-A4FB- 3A7F9063**** | The ID of the request. |
| Success | String | true | Indicates whether the call was successful. |
| TotalRecordCount | Integer | 1 | The total number of consumer groups. |

**Examples**

Sample requests

```
http(s)://dts.aliyuncs.com/?Action=DescribeConsumerGroup &SubscriptionInstanceId=dtso5xx5t9u19e**** &<Common request parameters>
```

Sample success responses

| XML | format |
|---|---|
| <DescribeConsumerGroupResponse> <TotalRecordCount>1</TotalRecordCount> <PageRecordCount>30</PageRecordCount> <RequestId>4204E899-8193-4D7D-A4FB-3A7F9063****</RequestId> <PageNumber>1</PageNumber> <ConsumerChannels> <DescribeConsumerChannel> <ConsumptionCheckpoint></ConsumptionCheckpoint> <ConsumerGroupID>dtspis1110z232gbm4</ConsumerGroupID> <ConsumerGroupUserName>test</ConsumerGroupUserName> <ConsumerGroupName>consumergrouptest</ConsumerGroupName> <MessageDelay>-1</MessageDelay> <UnconsumedData>-1</UnconsumedData> </DescribeConsumerChannel> </ConsumerChannels> <Success>true</Success> </DescribeConsumerGroupResponse> |   |

`JSON` format

```json
 "TotalRecordCount": 1,
 "PageRecordCount": 30,
 "RequestId": "4204E899-8193-4D7D-A4FB-3A7F9063****",
 "PageNumber": 1,
 "ConsumerChannels": {
  "DescribeConsumerChannel": [
```

`{`

```json
    "ConsumptionCheckpoint": "2019-10-02T12:00:00Z",
    "ConsumerGroupID": "dtspis1110z232gbm4",
    "ConsumerGroupUserName": "test",
    "ConsumerGroupName": "consumergrouptest",
    "MessageDelay": -1,
    "UnconsumedData": -1
```

`}` `]` `},`

```json
 "Success": true
```

`}`

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 500 | InternalError | The request processing has failed due to some unknown error. | The error message returned because an internal error has occurred. Try again later. |

###### 1.5.3.5.3 ModifyConsumerGroupPassword

Modifies the password of a consumer group.

> **Note:** This operation is applicable only to the new version of the change tracking feature. When you call ConfigureSubscriptionInstance to configure a change tracking task, the new version of the change tracking feature is used if you specify the **SubscriptionInstanceNetworkType** parameter. Otherwise, the old version of the change tracking feature is used.
> When you call this operation, the change tracking task must be in the NotStarted, Failed, Normal, or Abnormal state.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyConsumerGroupPassw ord | The operation that you want to perform. Set the value to ModifyConsumerGroupPassword. |
| ConsumerGroupID | String | Yes | dtswc411cg617p**** | The ID of the consumer group. You can call the DescribeConsumerGroup operation to query the consumer group ID. |
| consumerGroupNewPasswor d | String | Yes | Test654321 | The new password of the consumer group. The password must contain at least two of the following character types: uppercase letters, lowercase letters, digits, and special characters. The password must be 8 to 32 characters in length. |
| ConsumerGroupPassword | String | Yes | Test123456 | The current password of the consumer group. |
| SubscriptionInstanceId | String | Yes | dtsg2m10r1x15a**** | The ID of the change tracking instance. You can call the DescribeSubscriptionInstances operation to query the instance ID. |
| RegionId | String | No | cn-hangzhou | The region ID of the change tracking instance. |
| ConsumerGroupName | String | No | Test Consumer Group | The name of the consumer group. You can call the DescribeConsumerGroup operation to query the consumer group name. |
| ConsumerGroupUserName | String | No | dtstest | The username of the consumer group. You can call the DescribeConsumerGroup operation to query the username. |
| AccountId | String | No | 12323344**** | The ID of the Alibaba Cloud account. You do not need to specify this parameter because this parameter will be removed in the future. |

| Parameter | Type | Example | Description |
|---|---|---|---|

| ErrCode | String | InternalError | The error code returned if the call failed. |
|---|---|---|---|
| ErrMessage | String | The request processing has failed due to some unknown error. | The error message returned if the call failed. |
| RequestId | String | A06B5CFF-9576-4BC1-BE62- A3D43E1F**** | The ID of the request. |
| Success | String | true | Indicates whether the call was successful. |

**Examples**

Sample requests

```
http(s)://dts.aliyuncs.com/?Action=ModifyConsumerGroupPassword &ConsumerGroupID=dtswc411cg617p**** &consumerGroupNewPassword=Test654321 &ConsumerGroupPassword=Test123456 &SubscriptionInstanceId=dtsg2m10r1x15a**** &<Common request parameters>
```

Sample success responses

| XML | format |
|---|---|
| <ModifyConsumerGroupPasswordResponse> <RequestId>A06B5CFF-9576-4BC1-BE62-A3D43E1F****</RequestId> <Success>true</Success> </ModifyConsumerGroupPasswordResponse> |   |

| JSON | format |
|---|---|
| { "RequestId": "A06B5CFF-9576-4BC1-BE62-A3D43E1F****", "Success": true } |   |

###### 1.5.3.5.4 DeleteConsumerGroup

Deletes a consumer group.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteConsumerGroup | The operation that you want to perform. Set the value to DeleteConsumerGroup. |
| ConsumerGroupID | String | Yes | dtssb911ydd192**** | The ID of the consumer group. |
| SubscriptionInstanceId | String | Yes | dtsg2m10r1x15a**** | The ID of the change tracking instance. You can call the DescribeSubscriptionInstances operation to query the instance ID. |
| RegionId | String | No | cn-hangzhou | The region ID of the change tracking instance. |
| AccountId | String | No | 12323344**** | The ID of the Alibaba Cloud account. You do not need to specify this parameter because this parameter will be removed in the future. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| ErrCode | String | InternalError | The error code returned if the call failed. |
| ErrMessage | String | The request processing has failed due to some unknown error. | The error message returned if the call failed. |
| RequestId | String | 4D0ADAD5-DD97-41B6-B78F- D1961AB1**** | The ID of the request. |
| Success | String | true | Indicates whether the call was successful. |

```
http(s)://dts.aliyuncs.com/?Action=DeleteConsumerGroup &ConsumerGroupID=dtssb911ydd192**** &SubscriptionInstanceId=dtsg2m10r1x15a****
```

Sample success responses

| XML | format |
|---|---|
| <DeleteConsumerGroupResponse> <RequestId>4D0ADAD5-DD97-41B6-B78F-D1961AB1****</RequestId> <Success>true</Success> </DeleteConsumerGroupResponse> |   |

| JSON | format |
|---|---|
| { "RequestId": "4D0ADAD5-DD97-41B6-B78F-D1961AB1****", "Success": true } |   |

###### 1.5.3.5.5 ModifyConsumptionTimestamp

Modifies the consumption checkpoint of a change tracking instance.

> **Note:** This operation is applicable only to the old version of the change tracking feature. When you call ConfigureSubscriptionInstance to configure a change tracking task, the old version of the change tracking feature is used if you do not specify the **SubscriptionInstanceNetworkType** parameter. Otherwise, the new version of the change tracking feature is used.
> If you use the new version, you must set the consumption checkpoint on the change tracking client.
> When you call this operation, you must stop the change tracking client, and the change tracking task must be in the Normal state.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyConsumptionTimesta mp | The operation that you want to perform. Set the value to ModifyConsumptionTimestamp. |
| ConsumptionTimestamp | String | Yes | 2019-10-15T17:20:03Z | The consumption checkpoint. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC. |
| SubscriptionInstanceId | String | Yes | dtsg2m10r1x15a**** | The ID of the change tracking instance. You can call the DescribeSubscriptionInstances operation to query the instance ID. |
| RegionId | String | No | cn-hangzhou | The region ID of the change tracking instance. |
| AccountId | String | No | 12323344**** | The ID of the Alibaba Cloud account. You do not need to specify this parameter because this parameter will be removed in the future. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| ErrCode | String | InternalError | The error code returned if the call failed. |
| ErrMessage | String | The request processing has failed due to some unknown error. | The error message returned if the call failed. |
| RequestId | String | ABBACEFC-CBA9-4F80-A337- 42F202F5**** | The ID of the request. |
| Success | String | true | Indicates whether the call was successful. |

**Examples**

Sample requests

```
http(s)://dts.aliyuncs.com/?Action=ModifyConsumptionTimestamp &ConsumptionTimestamp=2019-10-15T17:20:03Z &SubscriptionInstanceId=dtsg2m10r1x15a****
```

```xml
<ModifyConsumptionTimestampResponse>
      <RequestId>ABBACEFC-CBA9-4F80-A337-42F202F5****</RequestId>
</ModifyConsumptionTimestampResponse>
```

| JSON | format |
|---|---|
| { "RequestId": "ABBACEFC-CBA9-4F80-A337-42F202F5****", "Success": true } |   |

##### 1.5.3.6 DescribeSubscriptionInstances

Queries the list of change tracking instances and details of each instance.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeSubscriptionInstance s | The operation that you want to perform. Set the value to DescribeSubscriptionInstances. |
| RegionId | String | No | cn-hangzhou | The region ID of the change tracking instance. |
| PageSize | Integer | No | 30 | The number of entries to return on each page. Valid values: 30, 50, and 100. Default value: 30. |
| PageNum | Integer | No | 1 | The number of the page to return. The value must be an integer that is greater than 0. Default value: 1. |
| SubscriptionInstanceName | String | No | MySQL Change Tracking | The name of the change tracking instance. Note If you specify this parameter, DTS returns all the change tracking instances that match the specified name. |
| ClientToken | String | No | 0c593ea1-3bea-11e9-b96b- 88e9fe63**** | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that the value is unique among different requests. The ClientToken value can contain only ASCII characters and cannot exceed 64 characters in length. |
| AccountId | String | No | 12323344**** | The ID of the Alibaba Cloud account. You do not need to specify this parameter because this parameter will be removed in the future. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| ErrCode | String | InternalError | The error code returned if the call failed. |
| ErrMessage | String | The request processing has failed due to some unknown error. | The error message returned if the call failed. |
| PageNumber | Integer | 1 | The page number of the returned page. |
| PageRecordCount | Integer | 30 | The number of entries returned per page. |
| RequestId | String | FC3BAAF2-74E3-4471-8EB5- 96202D6A**** | The ID of the request. |
| SubscriptionInstances | Array of SubscriptionInstance |   | The list of change tracking instances and details of each instance. |
| SubscriptionInstance |   |   |   |
| BeginTimestamp | String | 2021-06-21T08:25:43Z | The beginning of the time range for change tracking. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC. |
| ConsumptionCheckpoint | String | 2021-06-21T09:30:31Z | The consumption checkpoint of the change tracking instance. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC. |

| ConsumptionClient | String | 114.***.***.**:dts******** | The downstream client information in the following format: <IP address of the downstream client>:<Random ID generated by DTS>. |
|---|---|---|---|
| EndTimestamp | String | 2021-06-21T10:17:21Z | The end of the time range for change tracking. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC. |
| ErrorMessage | String | xxxxxxxx | The error message returned if change tracking failed. |
| PayType | String | PrePaid | The billing method of the change tracking instance. Valid values: PrePaid: subscription PostPaid: pay-as-you-go |
| SourceEndpoint | Struct |   | The connection settings of the source instance. |
| InstanceID | String | rm-bp1162kryivb8**** | The ID of the source instance. |
| InstanceType | String | RDS | The type of the source instance. Note This parameter is returned only for change tracking instances of the new version. |
| Status | String | Normal | The state of the change tracking instance. Valid values: NotStarted: The task is not started. Prechecking: The task is in precheck. PrecheckFailed: The task failed to pass the precheck. Starting: The task is being started. Normal: The task is running as expected. Abnormal: An exception occurred on the task. |
| SubscribeTopic | String | cnhangzhourmbp1162kryivb8* _ _ _ ***dtstestversion2 _ _ | The topic of the change tracking instance. Note This parameter is returned only if your change tracking instances are of the new version and you have called the CreateConsumerGroup operation to create a consumer group. |
| SubscriptionDataType | Struct |   | The types of operations that are tracked by the task. |
| DDL | Boolean | true | Indicates whether DDL statements are tracked. Valid values: true: yes false: no |
| DML | Boolean | true | Indicates whether DML statements are tracked. Valid values: true: yes false: no |
| SubscriptionHost | Struct |   | The endpoint of the change tracking instance. |
| PrivateHost | String | dts-cn-****- internal.aliyuncs.com:18002 | The private endpoint of the change tracking instance. The format is <Address>:<Port number> . |
| PublicHost | String | dts-cn-****.aliyuncs.com:18001 | The public endpoint of the change tracking instance. The format is <Address>:<Port number> . |
| VPCHost | String | dts-cn-****- vpc.aliyuncs.com:18003 | The virtual private cloud (VPC) endpoint of the change tracking instance. The format is <Address>:<Port number> . |
| SubscriptionInstanceID | String | rm-bp1162kryivb8**** | The ID of the change tracking instance. |
| SubscriptionInstanceNam e | String | MySQL Change Tracking | The name of the change tracking instance. |
| SubscriptionObject | Array of SynchronousObject |   | The objects for change tracking. |
| SynchronousObject |   |   |   |
| DatabaseName | String | dtstestdata | The name of the database to which the objects belong. |
| TableList | List | test1 | The name of the table to which the objects belong. |

| WholeDatabase | String | false | Indicates whether the data changes of the entire database are tracked. Valid values: true: yes false: no |
|---|---|---|---|
| Success | String | true | Indicates whether the call was successful. |
| TotalRecordCount | Long | 1 | The total number of change tracking instances that meet the requirements and belong to your Alibaba Cloud account. |

**Examples**

Sample requests

```
http(s)://dts.aliyuncs.com/?Action=DescribeSubscriptionInstances &Tag.1.Key=testkey1 &<Common request parameters>
```

Sample success responses

| XML | format |
|---|---|
| <DescribeSubscriptionInstancesResponse> <TotalRecordCount>1</TotalRecordCount> <PageRecordCount>30</PageRecordCount> <RequestId>FC3BAAF2-74E3-4471-8EB5-96202D6A****</RequestId> <PageNumber>1</PageNumber> <Success>true</Success> <SubscriptionInstances> <SubscriptionInstance> <Status>Normal</Status> <SubscriptionObject> <SynchronousObject> <DatabaseName>dtstestdata</DatabaseName> <WholeDatabase>false</WholeDatabase> <TableList> <Table>test1</Table> </TableList> </SynchronousObject> </SubscriptionObject> <SubscriptionDataType> <DML>true</DML> <DDL>true</DDL> </SubscriptionDataType> <SubscriptionInstanceName>MySQL Change Tracking</SubscriptionInstanceName> <SubscriptionHost> <PublicHost>dts-cn-hangzhou.aliyuncs.com:18001</PublicHost> <PrivateHost>dts-cn-hangzhou-internal.aliyuncs.com:18002</PrivateHost> <VPCHost>dts-cn-hangzhou-vpc.aliyuncs.com:18003</VPCHost> </SubscriptionHost> <SubscribeTopic>cn_hangzhou_rm_bp1162kryiv******_dtstest_version2</SubscribeTopic> <SourceEndpoint> <InstanceID>rm-bp1162kryivb8****</InstanceID> <InstanceType>RDS</InstanceType> </SourceEndpoint> <InstanceCreateTime>2021-06-21T10:17:21Z</InstanceCreateTime> <JobCreateTime>2021-06-21T10:17:21Z</JobCreateTime> <EndTimestamp>2021-06-21T10:17:21Z</EndTimestamp> <PayType>PrePaid</PayType> <SubscriptionInstanceID>dtsy0zz3t13h******</SubscriptionInstanceID> <BeginTimestamp>2021-06-21T08:25:43Z</BeginTimestamp> <Tags></Tags> </SubscriptionInstance> </SubscriptionInstances> </DescribeSubscriptionInstancesResponse> |   |

`JSON` format

```json
 "TotalRecordCount": 1,
 "PageRecordCount": 30,
 "RequestId": "FC3BAAF2-74E3-4471-8EB5-96202D6A****",
 "PageNumber": 1,
 "Success": true,
 "SubscriptionInstances": {
  "SubscriptionInstance": [
```

`{`

```json
    "Status": "Normal",
    "SubscriptionObject": {
     "SynchronousObject": [
```

`{`

```json
       "DatabaseName": "dtstestdata",
       "WholeDatabase": false,
       "TableList": {
        "Table": [
         "test1"
```

`]` `}` `}` `]` `},`

```json
    "SubscriptionDataType": {
     "DML": true,
     "DDL": true
```

`},`

```json
    "SubscriptionInstanceName": "MySQL Change Tracking",
    "SubscriptionHost": {
     "PublicHost": "dts-cn-hangzhou.aliyuncs.com:18001",
     "PrivateHost": "dts-cn-hangzhou-internal.aliyuncs.com:18002",
     "VPCHost": "dts-cn-hangzhou-vpc.aliyuncs.com:18003"
```

`},`

```json
    "SubscribeTopic": "cn_hangzhou_rm_bp1162kryiv******_dtstest_version2",
    "SourceEndpoint": {
     "InstanceID": "rm-bp1162kryivb8****",
     "InstanceType": "RDS"
```

`},`

```json
    "InstanceCreateTime": "2021-06-21T10:17:21Z",
    "JobCreateTime": "2021-06-21T10:17:21Z",
                "EndTimestamp": "2021-06-21T10:17:21Z",
    "PayType": "PrePaid",
    "SubscriptionInstanceID": "dtsy0zz3t13h******",
    "BeginTimestamp": "2021-06-21T08:25:43Z",
    "Tags": {
     "Tag": []
```

`}` `}` `]` `}` `}`

##### 1.5.3.7 DescribeSubscriptionInstanceStatus

Queries the state of a change tracking instance.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeSubscriptionInstance Status | The operation that you want to perform. Set the value to DescribeSubscriptionInstanceStatus. |
| SubscriptionInstanceId | String | Yes | dtsy0zz3t13h7d**** | The ID of the change tracking instance. You can call the DescribeSubscriptionInstances operation to query the instance ID. |
| RegionId | String | No | cn-hangzhou | The region ID of the change tracking instance. |
| AccountId | String | No | 12323344**** | The ID of the Alibaba Cloud account. You do not need to specify this parameter because this parameter will be removed in the future. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| BeginTimestamp | String | 2021-03-15T08:25:34Z | The beginning of the time range for change tracking. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC. |

| ConsumptionCheckpoint | String | 2021-03-23T07:30:31Z | The consumption checkpoint of the change tracking instance. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC. |
|---|---|---|---|
| ConsumptionClient | String | 114.***.***.**:dts******** | The downstream client information in the following format: <IP address of the downstream client>:<Random ID generated by DTS>. |
| EndTimestamp | String | 2021-03-26T14:03:21Z | The end of the time range for change tracking. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC. |
| ErrCode | String | InternalError | The error code returned if the call failed. |
| ErrMessage | String | The request processing has failed due to some unknown error. | The error message returned if the call failed. |
| ErrorMessage | String | ****** | The error message returned if change tracking failed. |
| ErrorMessage | String | ****** | The error message returned if change tracking failed. |
| PayType | String | PrePaid | The billing method of the change tracking instance. Valid values: PrePaid: subscription PostPaid: pay-as-you-go |
| RequestId | String | E0845D0A-6D36-4EEB-BE26- CF191E1A**** | The ID of the request. |
| SourceEndpoint | Struct |   | The connection settings of the source instance. |
| InstanceID | String | rm-bp1162kryivb8**** | The ID of the instance that hosts the source database. |
| InstanceType | String | RDS | The type of the source instance. Note This parameter is returned only for change tracking instances of the new version. |
| Status | String | Normal | The state of the change tracking instance. Valid values: NotStarted: The task is not started. Prechecking: The task is in precheck. PrecheckFailed: The task failed to pass the precheck. Starting: The task is being started. Normal: The task is running as expected. Abnormal: An exception occurred on the task. |
| SubscribeTopic | String | cnhangzhourmbp1162kryivb8* _ _ _ ***dtstestversion2 _ _ | The topic of the change tracking instance. Note This parameter is returned only if your change tracking instances are of the new version and you have called the CreateConsumerGroup operation to create a consumer group. |
| SubscriptionDataType | Struct |   | The types of operations that are tracked by the task. |
| DDL | Boolean | true | Indicates whether DDL statements are tracked. Valid values: true: yes false: no |
| DML | Boolean | true | Indicates whether DML statements are tracked. Valid values: true: yes false: no |
| SubscriptionHost | Struct |   | The endpoint of the change tracking instance. |
| PrivateHost | String | dts-cn-****- internal.aliyuncs.com:18002 | The private endpoint of the change tracking instance. The format is <Address>:<Port number> . |
| PublicHost | String | dts-cn-****.aliyuncs.com:18001 | The public endpoint of the change tracking instance. The format is <Address>:<Port number> . |

| VPCHost | String | dts-cn-****- vpc.aliyuncs.com:18003 | The virtual private cloud (VPC) endpoint of the change tracking instance. The format is <Address>:<Port number> . |
|---|---|---|---|
| SubscriptionInstanceID | String | rm-bp1162kryivb8**** | The ID of the change tracking instance. |
| SubscriptionInstanceNam e | String | API test | The name of the change tracking instance. |
| SubscriptionObject | Array of SynchronousObject |   | The objects for change tracking. |
| SynchronousObject |   |   |   |
| DatabaseName | String | dtstestdata | The name of the database to which the objects belong. |
| TableList | List | test1 | The name of the table to which the objects belong. |
| WholeDatabase | String | false | Indicates whether the data changes of the entire database are tracked. Valid values: true: yes false: no |
| Success | String | true | Indicates whether the call was successful. |

**Examples**

Sample requests

```
http(s)://dts.aliyuncs.com/?Action=DescribeSubscriptionInstanceStatus &SubscriptionInstanceId=dtsy0zz3t13h7d**** &<Common request parameters>
```

Sample success responses

| XML | format |
|---|---|
| <DescribeSubscriptionInstanceStatusResponse> <Status>Normal</Status> <TaskId>y0zz3t13h7d****</TaskId> <RequestId>E0845D0A-6D36-4EEB-BE26-CF191E1A****</RequestId> <SubscriptionHost> <PublicHost>dts-cn-****.aliyuncs.com:18001</PublicHost> <PrivateHost>dts-cn-****-internal.aliyuncs.com:18002</PrivateHost> <VPCHost>dts-cn-****-vpc.aliyuncs.com:18003</VPCHost> </SubscriptionHost> <EndTimestamp>2021-03-26T14:03:21Z</EndTimestamp> <PayType>PrePaid</PayType> <SubscriptionInstanceID>dtsy0zz3t13h7d****</SubscriptionInstanceID> <Success>true</Success> <SubscriptionObject> <SynchronousObject> <DatabaseName>dtstestdata</DatabaseName> <WholeDatabase>false</WholeDatabase> <TableList> <Table>test1</Table> </TableList> </SynchronousObject> </SubscriptionObject> <SubscriptionDataType> <DML>true</DML> <DDL>true</DDL> </SubscriptionDataType> <SubscriptionInstanceName>API test</SubscriptionInstanceName> <SubscribeTopic>cn_hangzhou_rm_bp1162kryivb8****_dtstest_version2</SubscribeTopic> <SourceEndpoint> <InstanceID>rm-bp1162kryivb8****</InstanceID> <InstanceType>RDS</InstanceType> </SourceEndpoint> <BeginTimestamp>2021-03-15T08:25:34Z</BeginTimestamp> </DescribeSubscriptionInstanceStatusResponse> |   |

`JSON` format

```json
 "Status": "Normal",
 "TaskId": "y0zz3t13h7d****",
 "RequestId": "E0845D0A-6D36-4EEB-BE26-CF191E1A****",
 "SubscriptionHost": {
  "PublicHost": "dts-cn-****.aliyuncs.com:18001",
  "PrivateHost": "dts-cn-****-internal.aliyuncs.com:18002",
  "VPCHost": "dts-cn-****-vpc.aliyuncs.com:18003"
```

`},`

```json
 "EndTimestamp": "2021-03-26T14:03:21Z",
 "PayType": "PrePaid",
 "SubscriptionInstanceID": "dtsy0zz3t13h7d****",
 "Success": true,
 "SubscriptionObject": {
  "SynchronousObject": [
```

`{`

```json
    "DatabaseName": "dtstestdata",
    "WholeDatabase": false,
    "TableList": {
     "Table": [
      "test1"
```

`]` `}` `}` `]` `},`

```json
 "SubscriptionDataType": {
  "DML": true,
  "DDL": true
```

`},`

```json
 "SubscriptionInstanceName": "API Test",
 "SubscribeTopic": "cn_hangzhou_rm_bp1162kryivb8****_dtstest_version2",
 "SourceEndpoint": {
  "InstanceID": "rm-bp1162kryivb8****",
  "InstanceType": "RDS"
```

`},`

```json
 "BeginTimestamp": "2021-03-15T08:25:34Z"
```

`}`

##### 1.5.3.8 DeleteSubscriptionInstance

Releases a change tracking instance.

> **Note:** After a change tracking instance is released, it cannot be recovered.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteSubscriptionInstance | The operation that you want to perform. Set the value to DeleteSubscriptionInstance. |
| SubscriptionInstanceId | String | Yes | dtsmxg11pfp231**** | The ID of the change tracking instance. You can call the DescribeSubscriptionInstances operation to query the instance ID. |
| RegionId | String | No | cn-hangzhou | The region ID of the change tracking instance. |
| AccountId | String | No | 12323344**** | The ID of the Alibaba Cloud account. You do not need to specify this parameter because this parameter will be removed in the future. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| ErrCode | String | InternalError | The error code returned if the call failed. |
| ErrMessage | String | The request processing has failed due to some unknown error. | The error message returned if the call failed. |
| RequestId | String | C306C198-7807-409D-930A- D6CE6C32**** | The ID of the request. |
| Success | String | true | Indicates whether the call was successful. |

```
http(s)://dts.aliyuncs.com/?Action=DeleteSubscriptionInstance &SubscriptionInstanceId=dtsmxg11pfp231****
```

Sample success responses

| XML | format |
|---|---|
| <DeleteSubscriptionInstanceResponse> <RequestId>C306C198-7807-409D-930A-D6CE6C32****</RequestId> <Success>true</Success> </DeleteSubscriptionInstanceResponse> |   |

| JSON | format |
|---|---|
| { "RequestId": "C306C198-7807-409D-930A-D6CE6C32****", "Success": true } |   |

#### 1.5.4 Network settings

##### 1.5.4.1 DescribeDTSIP

Queries the CIDR blocks of Data Transmission Service (DTS) servers. If the **source or destination instance** is an **on-premises self-managed database**, you must call this operation to query the CIDR blocks of DTS servers. Then, you need to add the CIDR blocks to the firewall security settings of the source or destination instance.

> **Note:** If the **source or destination database** is an **ApsaraDB instance** (such as ApsaraDB RDS instance and ApsaraDB for MongoDB instance) or a **self-managed database hosted on ECS**, you do not need to add the CIDR blocks. When you click **Set Whitelist and Next** in the DTS console, DTS automatically adds the CIDR blocks of DTS servers to the security settings of the source or destination instance.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeDTSIP | The operation that you want to perform. Set the value to DescribeDTSIP. |
| SourceEndpointRegion | String | Yes | cn-hangzhou | The region ID of the source instance. Note If the source instance is a self-managed database with a public IP address, you can set the parameter to cn-hangzhou or the ID of the closest region. |
| RegionId | String | No | cn-hangzhou | The region ID of the DTS instance. |
| DestinationEndpointRegion | String | No | cn-hangzhou | The region ID of the destination instance. Note If the destination instance is a self-managed database with a public IP address, you can set the parameter to cn-hangzhou or the ID of the closest region. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| DynamicCode | String | 500 | The internal error code. This parameter will be removed in the future. |
| DynamicMessage | String | 10.151.12.0/24,47.102.181.0/24, 47.101.109.0/24,120.55.129.0/24 ,11.115.103.0/24,47.102.234.0/2 4 | The CIDR blocks of DTS servers. |
| ErrCode | String | InternalError | The error code returned if the call failed. |
| ErrMessage | String | The request processing has failed due to some unknown error. | The error message returned if the call failed. |
| RequestId | String | 0C99C0BE-F312-40FA-ADFA- 4DC1166B**** | The ID of the request. |
| Success | String | true | Indicates whether the call was successful. |

```
http(s)://dts.aliyuncs.com/?Action=DescribeDTSIP &SourceEndpointRegion=cn-hangzhou
```

Sample success responses

| XML | format |
|---|---|
| <DescribeDTSIPResponse> <RequestId>0C99C0BE-F312-40FA-ADFA-4DC1166B****</RequestId> <DynamicMessage>10.151.12.0/24,47.102.181.0/24,47.101.109.0/24,120.55.129.0/24,11.115.103.0/24,47.102.234.0/24</DynamicMessage> <ErrMessage></ErrMessage> <Success>true</Success> <ErrCode></ErrCode> </DescribeDTSIPResponse> |   |

| JSON | format |
|---|---|
| { "RequestId": "0C99C0BE-F312-40FA-ADFA-4DC1166B****", "DynamicMessage": "10.151.12.0/24,47.102.181.0/24,47.101.109.0/24,120.55.129.0/24,11.115.103.0/24,47.102.234.0/24", "ErrMessage": "", "Success": true, "ErrCode": "" } |   |

##### 1.5.4.2 DescribeConnectionStatus

Queries the connectivity of Data Transmission Service (DTS) servers to the source and destination databases.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeConnectionStatus | The operation that you want to perform. Set the value to DescribeConnectionStatus. |
| DestinationEndpointArchitect ure | String | Yes | testsid | This parameter is required only if the SourceEndpointEngineName parameter is set to Oracle. Valid values: SID: non-RAC architecture RAC: Real Application Cluster (RAC) architecture Note This parameter is optional. The data type of this parameter is STRING. |
| DestinationEndpointInstance Type | String | Yes | PolarDBo _ | The type of the destination instance. Valid values: Note ECS: self-managed database hosted on Elastic Compute Service (ECS) LocalInstance: self-managed database with a public IP address RDS: ApsaraDB RDS instance DRDS: PolarDB-X instance MongoDB: ApsaraDB for MongoDB instance Redis: ApsaraDB for Redis instance PetaData: HybridDB for MySQL instance POLARDB: PolarDB for MySQL cluster PolarDBo: PolarDB for Oracle cluster _ AnalyticDB: AnalyticDB for MySQL V3.0 cluster or AnalyticDB for MySQL V2.0 cluster Greenplum: AnalyticDB for PostgreSQL instance |
| DestinationEndpointOracleSI D | String | Yes | testsid | This parameter is required only if the DestinationEndpointEngineName parameter is set to Oracle. Valid values: SID: non-RAC architecture RAC: RAC architecture Note This parameter is optional. The data type of this parameter is STRING. |
| SourceEndpointArchitecture | String | Yes | SID | This parameter is required only if the SourceEndpointEngineName parameter is set to Oracle. Valid values: SID: non-RAC architecture RAC: RAC architecture Note This parameter is optional. |

| SourceEndpointInstanceType | String | Yes | RDS | The type of the source instance. Valid values: RDS: ApsaraDB RDS instance LocalInstance: self-managed database with a public IP address ECS: self-managed database hosted on ECS Express: self-managed database connected over Express Connect dg: self-managed database connected over Database Gateway MongoDB: ApsaraDB for MongoDB instance POLARDB: PolarDB for MySQL cluster PolarDBo: PolarDB for Oracle cluster _ |
|---|---|---|---|---|
| SourceEndpointInstanceID | String | No | rm-bp1imrtn6fq7h**** | The ID of the source instance. |
| SourceEndpointEngineName | String | No | MySQL | The engine type of the source database. Valid values: MySQL, TiDB, SQLServer, PostgreSQL, Oracle, MongoDB, and Redis. Note The default value is MySQL. |
| SourceEndpointRegion | String | No | cn-hangzhou | The region ID of the source instance. |
| SourceEndpointIP | String | No | 172.16.88.*** | The IP address of the source database. Note This parameter is available and required only if the SourceEndpointInstanceType parameter is set to LocalInstance or Express. |
| SourceEndpointPort | String | No | 3306 | The service port number of the source database. Note This parameter is available and required only if the SourceEndpointInstanceType parameter is set to ECS, LocalInstance, or Express. |
| SourceEndpointOracleSID | String | No | testsid | The system ID (SID) of the Oracle database. Note This parameter is available and required only if the SourceEndpointEngineName parameter is set to Oracle and the Oracle database is deployed in a non-RAC architecture. |
| SourceEndpointDatabaseNa me | String | No | dtstestdata | The name of the source database or the authentication database. Note This parameter is available and required only if the SourceEndpointEngineName parameter is set to PostgreSQL or MongoDB or the SourceEndpointInstanceType parameter is set to PolarDBo. _ If the SourceEndpointEngineName parameter is set to PostgreSQL or DRDS, specify the name of the source database. If the SourceEndpointEngineName parameter is set to MongoDB, specify the name of the authentication database. If the SourceEndpointInstanceType parameter is set to PolarDBo, specify the name of the _ source database. |
| SourceEndpointUserName | String | No | dtstest | The database account of the source database. Note The permissions required for the database account to migrate or synchronize data vary with database engines. |
| SourceEndpointPassword | String | No | Test123456 | The password of the source database account. |
| DestinationEndpointInstanceI D | String | No | testsid | The ID of the destination instance. |
| DestinationEndpointEngineN ame | String | No | MySQL | The engine type of the destination database. Valid values: MySQL, DRDS, SQLServer, PostgreSQL, PPAS, MongoDB, and Redis. Note This parameter is available and required only if the DestinationEndpointInstanceType parameter is set to RDS, DRDS, ECS, LocalInstance, or Express. |

| DestinationEndpointRegion | String | No | cn-hangzhou | The region ID of the destination instance. |
|---|---|---|---|---|
| DestinationEndpointIP | String | No | 172.16.88.*** | The IP address of the destination database. Note This parameter is available and required only if the DestinationEndpointInstanceType parameter is set to LocalInstance or Express. |
| DestinationEndpointPort | String | No | 3306 | The service port number of the source database. Note This parameter is available and required only if the SourceEndpointInstanceType parameter is set to ECS, LocalInstance, or Express. |
| DestinationEndpointDatabas eName | String | No | dtstestdata | The name of the destination database or the authentication database. Note This parameter is available and required only if the DestinationEndpointInstanceType parameter is set to PolarDBo or the _ DestinationEndpointEngineName parameter is set to PostgreSQL, DRDS, or MongoDB. If the DestinationEndpointEngineName parameter is set to PostgreSQL or DRDS, specify the name of the destination database. If the DestinationEndpointEngineName parameter is set to MongoDB, specify the name of the authentication database. If the DestinationEndpointInstanceType parameter is set to PolarDBo, specify the name _ of the destination database. |
| DestinationEndpointUserNam e | String | No | dtstest | The database account of the destination database. Note The permissions required for the database account to migrate or synchronize data vary with database engines. |
| DestinationEndpointPasswor d | String | No | Test123456 | The password of the destination database account. |
| RegionId | String | No | cn-hangzhou | The region ID of the DTS instance. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| DestinationConnectionSta tus | Map | { "connectDetail": [ { "testName": "PolarDBo JDBC _ Connect", "testSuccess": true }, { "testName": "Ping ", "testSuccess": true }, { "testName": "Telnet ", "testSuccess": true } ], "connectRes": true, "connectAdvice": "" } | The connectivity results of DTS servers to the destination database. |
| ErrCode | String | InternalError | The error code returned if the call failed. |
| ErrMessage | String | The request processing has failed due to some unknown error. | The error message returned if the call failed. |
| RequestId | String | 0A47C784-70EF-4111-8677- 369CAA00**** | The ID of the request. |
| SourceConnectionStatus | Map | { "connectDetail": [ { "testName": "Oracle JDBC Connect", "testSuccess": true }, { "testName": "Ping ", "testSuccess": false }, { "testName": "Telnet ", "testSuccess": true } ], "connectRes": true, "connectAdvice": "" } | The connectivity results of DTS servers to the source database. |
| Success | String | true | Indicates whether the call was successful. |

**Examples**

Sample requests

```
http(s)://dts.aliyuncs.com/?Action=DescribeConnectionStatus &DestinationEndpointArchitecture=SID &DestinationEndpointInstanceType=PolarDB_o &DestinationEndpointOracleSID=testsid &SourceEndpointArchitecture=SID &SourceEndpointInstanceType=RDS &<Common request parameters>
```

Sample success responses

| XML | format |
|---|---|
| <DescribeConnectionStatusResponse> <RequestId>0A47C784-70EF-4111-8677-369CAA00****</RequestId> <SourceConnectionStatus> <connectDetail> <testName>Oracle JDBC Connect</testName> <testSuccess>true</testSuccess> </connectDetail> <connectDetail> <testName>Ping </testName> <testSuccess>false</testSuccess> </connectDetail> <connectDetail> <testName>Telnet </testName> <testSuccess>true</testSuccess> </connectDetail> <connectRes>true</connectRes> <connectAdvice></connectAdvice> </SourceConnectionStatus> <DestinationConnectionStatus> <connectDetail> <testName>PolarDB_o JDBC Connect</testName> <testSuccess>true</testSuccess> </connectDetail> <connectDetail> <testName>Ping </testName> <testSuccess>true</testSuccess> </connectDetail> <connectDetail> <testName>Telnet </testName> <testSuccess>true</testSuccess> </connectDetail> <connectRes>true</connectRes> <connectAdvice></connectAdvice> </DestinationConnectionStatus> <Success>true</Success> </DescribeConnectionStatusResponse> |   |

`JSON` format

```json
  "RequestId": "0A47C784-70EF-4111-8677-369CAA00****",
  "SourceConnectionStatus": {
    "connectDetail": [
        "testName": "Oracle JDBC Connect",
        "testSuccess": true
```

`},` `{`

```json
        "testName": "Ping ",
        "testSuccess": false
```

`},` `{`

```json
        "testName": "Telnet ",
        "testSuccess": true
```

`}` `],`

```json
    "connectRes": true,
    "connectAdvice": ""
```

`},`

```json
  "DestinationConnectionStatus": {
    "connectDetail": [
```

`{`

```json
        "testName": "PolarDB_o JDBC Connect",
        "testSuccess": true
```

`},` `{`

```json
        "testName": "Ping ",
        "testSuccess": true
```

`},` `{`

```json
        "testName": "Telnet ",
        "testSuccess": true
```

`}` `],`

```json
    "connectRes": true,
    "connectAdvice": ""
```

`},`

```json
  "Success": true
```

`}`

#### 1.5.5 Monitoring and alerting

##### 1.5.5.1 ConfigureMigrationJobAlert

Configures alert settings to monitor a data migration instance.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ConfigureMigrationJobAlert | The operation that you want to perform. Set the value to ConfigureMigrationJobAlert. |
| MigrationJobId | String | Yes | dtslb9113qq11n**** | The ID of the data migration instance. You can call the DescribeMigrationJobs operation to query the instance ID. |
| RegionId | String | No | cn-hangzhou | The ID of the region in which the data migration instance resides. |
| DelayAlertStatus | String | No | enable | Specifies whether to monitor the instance latency. Valid values: enable: monitors the instance latency. disable: does not monitor the instance latency Note Default value: enable. You must set at least one of the DelayAlertStatus and ErrorAlertStatus parameters. |

| DelayAlertPhone | String | No | 1361234****,1371234**** | The mobile numbers that receive latency-related alerts. Separate multiple mobile numbers with commas (,). Note This parameter is available for only users of the China site (aliyun.com). Only mobile numbers in the Chinese mainland are supported. You can specify up to 10 mobile numbers. International site (alibabacloud.com) users cannot receive alerts by using mobile numbers, but can set alert rules for Data Transmission Service (DTS) instances in the CloudMonitor console. |
|---|---|---|---|---|
| ErrorAlertStatus | String | No | enable | Specifies whether to monitor the instance status. Valid values: enable: monitors the instance status. disable: does not monitor the instance status. Note Default value: enable. You must set at least one of the ErrorAlertStatus and DelayAlertStatus parameters. If the instance that you monitor enters an abnormal state, an alert is triggered. |
| ErrorAlertPhone | String | No | 1361234****,1371234**** | The mobile numbers that receive status-related alerts. Separate multiple mobile numbers with commas (,). Note This parameter is available for only users of the China site (aliyun.com). Only mobile numbers in the Chinese mainland are supported. You can specify up to 10 mobile numbers. International site (alibabacloud.com) users cannot receive alerts by using mobile numbers, but can set alert rules for DTS instances in the CloudMonitor console. |
| DelayOverSeconds | String | No | 10 | The threshold for triggering latency-related alerts. Unit: seconds. The value must be an integer. You can set the threshold based on your business needs. To prevent jitters caused by network and database overloads, we recommend that you set the threshold to more than 10 seconds. Note If the DelayAlertStatus parameter is set to enable, this parameter must be set. |
| AccountId | String | No | 12323344**** | The ID of the Alibaba Cloud account. You do not need to set this parameter because this parameter will be removed in the future. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| ErrCode | String | InternalError | The error code returned if the request failed. |
| ErrMessage | String | The request processing has failed due to some unknown error. | The error message returned if the request failed. |
| RequestId | String | 0a2a047516051973705541561d* *** | The ID of the request. |
| Success | String | true | Indicates whether the request was successful. |

**Examples**

Sample requests

```
http(s)://dts.aliyuncs.com/?Action=ConfigureMigrationJobAlert &MigrationJobId=dtslb9113qq11n**** &DelayAlertStatus=enable &DelayOverSeconds=10 &<Common request parameters>
```

Sample success responses

```xml
<ConfigureMigrationJobAlertResponse>
      <RequestId>0a2a047516051973705541561d****</RequestId>
</ConfigureMigrationJobAlertResponse>
```

| JSON | format |
|---|---|
| { "RequestId": "0a2a047516051973705541561d****", "Success": true } |   |

##### 1.5.5.2 DescribeMigrationJobAlert

Queries the alert settings of a data migration instance.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeMigrationJobAlert | The operation that you want to perform. Set the value to DescribeMigrationJobAlert. |
| MigrationJobId | String | Yes | dtslb9113qq11n**** | The ID of the data migration instance. You can call the DescribeMigrationJobs operation to query the instance ID. |
| RegionId | String | No | cn-hangzhou | The ID of the region in which the data migration instance resides. |
| ClientToken | String | No | ETnLKlblzczshOTUbOCz**** | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must ensure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |
| AccountId | String | No | 12323344**** | The ID of the Alibaba Cloud account. You do not need to set this parameter because this parameter will be removed in the future. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| DelayAlertPhone | String | 1361234****,1371234**** | The mobile phone numbers that receive latency-related alerts. |
| DelayAlertStatus | String | enable | Indicates whether the instance latency is monitored. Valid values: enable: The instance latency is monitored. disable: The instance latency is not monitored. |
| ErrorAlertPhone | String | 1361234****,1371234**** | The mobile phone numbers that receive status-related alerts. |
| ErrCode | String | InternalError | The error code returned if the request failed. |
| ErrMessage | String | The request processing has failed due to some unknown error. | The error message returned if the request failed. |
| DelayOverSeconds | String | 10 | The threshold for triggering latency-related alerts. Unit: seconds. |
| ErrorAlertStatus | String | enable | Indicates whether the instance status is monitored. Valid values: enable: The instance status is monitored. disable: The instance status is not monitored. |
| MigrationJobId | String | lb9113qq11n**** | The ID of the data migration instance. |
| MigrationJobName | String | PolarDB MySQLtoRDS MySQL _ _ | The name of the data migration instance. |
| RequestId | String | 210ec21916055187057342533d* *** | The ID of the request. |
| Success | String | true | Indicates whether the request was successful. |

```
http(s)://dts.aliyuncs.com/?Action=DescribeMigrationJobAlert &MigrationJobId=dtslb9113qq11n****
```

Sample success responses

| XML | format |
|---|---|
| <DescribeMigrationJobAlertresponse> <RequestId>210ec21916055187057342533d****</RequestId> <DelayAlertPhone>1361234****,1371234****</DelayAlertPhone> <ErrorAlertStatus>enable</ErrorAlertStatus> <MigrationJobName>PolarDB MySQL_to_RDS MySQL</MigrationJobName> <DelayAlertStatus>enable</DelayAlertStatus> <DelayOverSeconds>10</DelayOverSeconds> <Success>true</Success> <MigrationJobId>lb9113qq11n****</MigrationJobId> </DescribeMigrationJobAlertresponse> |   |

| JSON | format |
|---|---|
| { "RequestId": "210ec21916055187057342533d****", "DelayAlertPhone": "1361234****,1371234****", "ErrorAlertStatus": "enable", "MigrationJobName": "PolarDB MySQL_to_RDS MySQL", "DelayAlertStatus": "enable", "DelayOverSeconds": "10", "Success": true, "MigrationJobId": "lb9113qq11n****" } |   |

##### 1.5.5.3 ConfigureSubscriptionInstanceAlert

Configures alert settings to monitor a change tracking instance.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ConfigureSubscriptionInstanc eAlert | The operation that you want to perform. Set the value to ConfigureSubscriptionInstanceAlert. |
| SubscriptionInstanceId | String | Yes | dtsl8zl9ek6292**** | The ID of the change tracking instance. You can call the DescribeSubscriptionInstances operation to query the instance ID. |
| RegionId | String | No | cn-hangzhou | The ID of the region in which the change tracking instance resides. |
| DelayAlertStatus | String | No | enable | Specifies whether to monitor the instance latency. Valid values: enable: monitors the instance status. disable: does not monitor the instance status. Note Default value: enable. You must set at least one of the DelayAlertStatus and ErrorAlertStatus parameters. |
| DelayAlertPhone | String | No | 1361234****,1371234**** | The mobile numbers that receive latency-related alerts. Separate multiple mobile numbers with commas (,). Note This parameter is available for only users of the China site (aliyun.com). Only mobile numbers in the Chinese mainland are supported. You can specify up to 10 mobile numbers. International site (alibabacloud.com) users cannot receive alerts by using mobile numbers, but can set alert rules for Data Transmission Service (DTS) instances in the CloudMonitor console. |

| ErrorAlertStatus | String | No | enable | Specifies whether to monitor the instance status. Valid values: enable: monitors the instance status. disable: does not monitor the instance status. Note Default value: enable. You must set at least one of the ErrorAlertStatus and DelayAlertStatus parameters. If the instance that you monitor enters an abnormal state, an alert is triggered. |
|---|---|---|---|---|
| ErrorAlertPhone | String | No | 1361234****,1371234**** | The mobile numbers that receive status-related alerts. Separate multiple mobile numbers with commas (,). Note This parameter is available for only users of the China site (aliyun.com). Only mobile numbers in the Chinese mainland are supported. You can specify up to 10 mobile numbers. International site (alibabacloud.com) users cannot receive alerts by using mobile numbers, but can set alert rules for DTS instances in the CloudMonitor console. |
| DelayOverSeconds | String | No | 10 | The threshold for triggering latency-related alerts. Unit: seconds. The value must be an integer. You can set the threshold based on your business needs. To prevent jitters caused by network and database overloads, we recommend that you set the threshold to more than 10 seconds. Note If the DelayAlertStatus parameter is set to enable, this parameter must be set. |
| AccountId | String | No | 12323344**** | The ID of the Alibaba Cloud account. You do not need to set this parameter because this parameter will be removed in the future. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| ErrCode | String | InternalError | The error code returned if the request failed. |
| ErrMessage | String | InternalError The request processing has failed due to some unknown error. | The error message returned if the request failed. |
| RequestId | String | 0a2a047516051973705541561d* *** | The ID of the request. |
| Success | String | true | Indicates whether the request was successful. |

**Examples**

Sample requests

```
http(s)://dts.aliyuncs.com/?Action=ConfigureSubscriptionInstanceAlert &SubscriptionInstanceId=dtsl8zl9ek6292**** &DelayAlertStatus=enable &DelayAlertPhone=1361234****,1371234**** &DelayOverSeconds=10 &<Common request parameters>
```

Sample success responses

| XML | format |
|---|---|
| <ConfigureSubscriptionInstanceAlertResponse> <RequestId>0a2a047516051973705541561d****</RequestId> <Success>true</Success> </ConfigureSubscriptionInstanceAlertResponse> |   |

| JSON | format |
|---|---|
| { "RequestId": "0a2a047516051973705541561d****", "Success": true } |   |

##### 1.5.5.4 DescribeSubscriptionInstanceAlert

Queries the alert settings of a change tracking instance.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeSubscriptionInstance Alert | The operation that you want to perform. Set the value to DescribeSubscriptionInstanceAlert. |
| SubscriptionInstanceId | String | Yes | dtsl8zl9ek6292**** | The ID of the change tracking instance. You can call the DescribeSubscriptionInstances operation to query the instance ID. |
| RegionId | String | No | cn-hangzhou | The ID of the region in which the change tracking instance resides. |
| ClientToken | String | No | ETnLKlblzczshOTUbOCz**** | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must ensure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |
| AccountId | String | No | 12323344**** | The ID of the Alibaba Cloud account. You do not need to set this parameter because this parameter will be removed in the future. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| DelayAlertPhone | String | 1361234****,1371234**** | The mobile phone numbers that receive latency-related alerts. |
| DelayAlertStatus | String | enable | Indicates whether the instance latency is monitored. Valid values: enable: The instance latency is monitored. disable: The instance latency is not monitored. |
| DelayOverSeconds | String | 10 | The threshold for triggering latency-related alerts, in seconds. The value is an integer. The recommended value is 10. |
| ErrCode | String | InternalError | The error code returned if the request failed. |
| ErrMessage | String | The request processing has failed due to some unknown error. | The error message returned if the request failed. |
| ErrorAlertPhone | String | 1361234****,1371234**** | The mobile phone numbers that receive status-related alerts. |
| ErrorAlertStatus | String | enable | Indicates whether the instance status is monitored. Valid values: enable: The instance status is monitored. disable: The instance status is not monitored. |
| RequestId | String | 210ec2e116055198849072222d* *** | The ID of the request. |
| SubscriptionInstanceID | String | dtsl8zl9ek6292**** | The ID of the change tracking instance. |
| SubscriptionInstanceNam e | String | test | The name of the change tracking instance. |
| Success | String | true | Indicates whether the request was successful. |

**Examples**

Sample requests

```
http(s)://dts.aliyuncs.com/?Action=DescribeSubscriptionInstanceAlert &SubscriptionInstanceId=dtsl8zl9ek6292**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeSubscriptionInstanceAlertResponse>
      <SubscriptionInstanceName>test</SubscriptionInstanceName>
      <RequestId>210ec2e116055198849072222d****</RequestId>
      <DelayAlertPhone>1361234****,1371234****</DelayAlertPhone>
      <ErrorAlertStatus>enable</ErrorAlertStatus>
      <DelayAlertStatus>enable</DelayAlertStatus>
      <DelayOverSeconds>10</DelayOverSeconds>
      <Success>true</Success>
</DescribeSubscriptionInstanceAlertResponse>
```

| JSON | format |
|---|---|
| { "SubscriptionInstanceName": "test", "RequestId": "210ec2e116055198849072222d****", "DelayAlertPhone": "1361234****,1371234****", "ErrorAlertStatus": "enable", "DelayAlertStatus": "enable", "DelayOverSeconds": "10", "Success": true } |   |

##### 1.5.5.5 ConfigureSynchronizationJobAlert

Configures alert settings to monitor a data synchronization instance.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ConfigureSynchronizationJob Alert | The operation that you want to perform. Set the value to ConfigureSynchronizationJobAlert. |
| SynchronizationJobId | String | Yes | dtskxz1170c10p**** | The ID of the data synchronization instance. You can call the DescribeSynchronizationJobs operation to query the instance ID. |
| RegionId | String | No | cn-hangzhou | The ID of the region in which the data synchronization instance resides. |
| SynchronizationDirection | String | No | Forward | The synchronization direction. Valid values: Forward: Data is synchronized from the source database to the destination database. Reverse: Data is synchronized form the destination database to the source database. Note Default value: Forward. |
| DelayAlertStatus | String | No | enable | Specifies whether to monitor the instance latency. Valid values: enable: monitors the instance latency. disable: does not monitor the instance latency. Note Default value: enable. You must set at least one of the DelayAlertStatus and ErrorAlertStatus parameters. |
| DelayAlertPhone | String | No | 1361234****,1371234**** | The mobile numbers that receive latency-related alerts. Separate multiple mobile numbers with commas (,). Note This parameter is available for only users of the China site (aliyun.com). Only mobile numbers in the Chinese mainland are supported. You can specify up to 10 mobile numbers. International site (alibabacloud.com) users cannot receive alerts by using mobile numbers, but can set alert rules for Data Transmission Service (DTS) instances in the CloudMonitor console. |

| ErrorAlertStatus | String | No | enable | Specifies whether to monitor the instance status. Valid values: enable: monitors the instance status. disable: does not monitor the instance status. Note Default value: enable. You must set at least one of the ErrorAlertStatus and DelayAlertStatus parameters. If the instance that you monitor enters an abnormal state, an alert is triggered. |
|---|---|---|---|---|
| ErrorAlertPhone | String | No | 1361234****,1371234**** | The mobile numbers that receive status-related alerts. Separate multiple mobile numbers with commas (,). Note This parameter is available for only users of the China site (aliyun.com). Only mobile numbers in the Chinese mainland are supported. You can specify up to 10 mobile numbers. International site (alibabacloud.com) users cannot receive alerts by using mobile numbers, but can set alert rules for DTS instances in the CloudMonitor console. |
| DelayOverSeconds | String | No | 10 | The threshold for triggering latency-related alerts. Unit: seconds. The value must be an integer. You can set the threshold based on your business needs. To prevent jitters caused by network and database overloads, we recommend that you set the threshold to more than 10 seconds. Note If the DelayAlertStatus parameter is set to enable, this parameter must be set. |
| AccountId | String | No | 12323344**** | The ID of the Alibaba Cloud account. You do not need to set this parameter because this parameter will be removed in the future. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| ErrCode | String | InternalError | The error code returned if the request failed. |
| ErrMessage | String | The request processing has failed due to some unknown error. | The error message returned if the request failed. |
| RequestId | String | 8EEE7858-7D41-4EDF-9435- AEED2A34**** | The ID of the request. |
| Success | String | true | Indicates whether the request was successful. |

**Examples**

Sample requests

```
http(s)://dts.aliyuncs.com/?Action=ConfigureSynchronizationJobAlert &SynchronizationJobId=dtskxz1170c10p**** &DelayAlertStatus=enable &DelayAlertPhone=1361234****,1371234**** &DelayOverSeconds=10 &<Common request parameters>
```

Sample success responses

| XML | format |
|---|---|
| <ConfigureSynchronizationJobAlertResponse> <RequestId>8EEE7858-7D41-4EDF-9435-AEED2A34****</RequestId> <Success>true</Success> </ConfigureSynchronizationJobAlertResponse> |   |

| JSON | format |
|---|---|
| { "RequestId": "8EEE7858-7D41-4EDF-9435-AEED2A34****", "Success": true } |   |

##### 1.5.5.6 DescribeSynchronizationJobAlert

Queries the alert settings of a data synchronization instance.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeSynchronizationJobA lert | The operation that you want to perform. Set the value to DescribeSynchronizationJobAlert. |
| SynchronizationJobId | String | Yes | dtskxz1170c10p**** | The ID of the data synchronization instance. You can call the DescribeSynchronizationJobs operation to query the instance ID. |
| RegionId | String | No | cn-hangzhou | The ID of the region in which the data synchronization instance resides. |
| SynchronizationDirection | String | No | Forward | The synchronization direction. Valid values: Forward: Data is synchronized from the source database to the destination database. Reverse: Data is synchronized from the destination database to the source database. Note Default value: Forward. |
| ClientToken | String | No | ETnLKlblzczshOTUbOCz**** | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must ensure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |
| AccountId | String | No | 12323344**** | The ID of the Alibaba Cloud account. You do not need to set this parameter because this parameter will be removed in the future. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| DelayAlertPhone | String | 1361234****,1371234**** | The mobile phone numbers that receive latency-related alerts. |
| DelayAlertStatus | String | enable | Indicates whether the instance latency is monitored. Valid values: enable: The instance latency is monitored. disable: The instance latency is not monitored. |
| DelayOverSeconds | String | 10 | The threshold for triggering latency-related alerts. Unit: seconds. |
| ErrCode | String | InternalError | The error code returned if the request failed. |
| ErrMessage | String | The request processing has failed due to some unknown error. | The error message returned if the request failed. |
| ErrorAlertPhone | String | 1361234****,1371234**** | The mobile phone numbers that receive status-related alerts. |
| ErrorAlertStatus | String | enable | Indicates whether the instance status is monitored. Valid values: enable: The instance latency is monitored. disable: The instance latency is not monitored. |
| RequestId | String | 210ec20e16055205968635339d* *** | The ID of the request. |
| Success | String | true | Indicates whether the request was successful. |
| SynchronizationDirection | String | Forward | The synchronization direction. Valid values: Forward: Data is synchronized from the source database to the destination database. Reverse: Data is synchronized from the destination database to the source database. Note This parameter is returned only if the topology of data synchronization is two-way synchronization. |
| SynchronizationJobId | String | kxz1170c10p**** | The ID of the data synchronization instance. |
| SynchronizationJobName | String | Polar MySQLTORDS MySQL _ _ | The name of the data synchronization instance. |

```
http(s)://dts.aliyuncs.com/?Action=DescribeSynchronizationJobAlert &SynchronizationJobId=dtskxz1170c10p****
```

Sample success responses

| XML | format |
|---|---|
| <DescribeSynchronizationJobAlertresponse> <SynchronizationJobId>kxz1170c10p****</SynchronizationJobId> <RequestId>210ec20e16055205968635339d****</RequestId> <SynchronizationJobName>Polar MySQL_TO_RDS MySQL</SynchronizationJobName> <DelayAlertPhone>1361234****,1371234****</DelayAlertPhone> <ErrorAlertStatus>enable</ErrorAlertStatus> <DelayAlertStatus>enable</DelayAlertStatus> <DelayOverSeconds>10</DelayOverSeconds> <Success>true</Success> </DescribeSynchronizationJobAlertresponse> |   |

| JSON | format |
|---|---|
| { "SynchronizationJobId": "kxz1170c10p****", "RequestId": "210ec20e16055205968635339d****", "SynchronizationJobName": "Polar MySQL_TO_RDS MySQL", "DelayAlertPhone": "1361234****,1371234****", "ErrorAlertStatus": "enable", "DelayAlertStatus": "enable", "DelayOverSeconds": "10", "Success": true } |   |

#### 1.5.6 Instance management

##### 1.5.6.1 ShieldPrecheck

Ignores the precheck items that a data migration or synchronization instance may fail to pass. After you successfully call this operation, you need to call the StartMigrationJob and StartSynchronizationJob operations. Then, Data Transmission Service (DTS) performs a precheck on your data migration or synchronization instance. After the precheck is passed, the instance automatically runs.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ShieldPrecheck | The operation that you want to perform. Set the value to ShieldPrecheck. |
| DtsInstanceId | String | Yes | dtsi76118o3w92**** | The ID of the data migration or data synchronization instance. You can call the DescribeMigrationJobs or DescribeSynchronizationJobs operation to query the instance ID. |
| PrecheckItems | String | Yes | CHECKSAMEOBJ _ _ | The precheck items that you want to ignore. Separate multiple items with commas (,). Supported items: CHECKSAMEOBJ: object name conflict _ _ CHECKSAMEUSER: username conflict _ _ CHECKSRC: source database version _ CHECKTOPOLOGY: topology type _ CHECKSERVERID: server ID of the source database _ _ |
| RegionId | String | No | cn-hangzhou | The ID of the region in which the data migration or synchronization instance resides. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| ErrCode | String | InternalError | The error code returned if the request failed. |
| ErrMessage | String | The request processing has failed due to some unknown error. | The error message returned if the request failed. |
| RequestId | String | 6F4B5BC4-34B1-49C9-9C8F- C8F16AC4**** | The ID of the request. |
| Success | Boolean | true | Indicates whether the request was successful. |

```
http(s)://dts.aliyuncs.com/?Action=ShieldPrecheck &DtsInstanceId=dtsi76118o3w92**** &PrecheckItems=CHECK_SAME_OBJ
```

Sample success responses

| XML | format |
|---|---|
| <ShieldPrecheck> <RequestId>6F4B5BC4-34B1-49C9-9C8F-C8F16AC4****</RequestId> <Success>true</Success> </ShieldPrecheck> |   |

| JSON | format |
|---|---|
| { "RequestId": "6F4B5BC4-34B1-49C9-9C8F-C8F16AC4****", "Success": true } |   |

#### 1.5.7 Tag management

##### 1.5.7.1 TagResources

Adds tags to one or more data migration, data synchronization, or change tracking instances. If you have a large number of instances, you can create multiple tags and add these tags to the instances. Then, you can filter these instances by tag. A tag consists of a key and a value. Each key must be unique in a region for an Alibaba Cloud account. Different keys can be mapped to the same value. If the tag that you specify does not exist, this tag is automatically created and added to the specified instance. If the key of the specified tag is the same as that of an existing tag, the specified tag overwrites the existing tag. You can add up to 20 tags to an instance. You can add tags to up to 50 instances in each request.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | TagResources | The operation that you want to perform. Set this parameter to TagResources. |
| RegionId | String | Yes | cn-hangzhou | The ID of the region in which the data migration, data synchronization, or change tracking instance resides. |
| ResourceId.N | RepeatList | Yes | dtsntk10k6r12v**** | The ID of the data migration, data synchronization, or change tracking instance. You can call the DescribeDtsJobs operation to query the instance ID. Note N specifies the serial number of the instance. For example, ResourceId.1 specifies the ID of the first instance and ResourceId.2 specifies the ID of the second instance. |
| ResourceType | String | Yes | ALIYUN::DTS::INSTANCE | The resource type. The parameter value is fixed to ALIYUN::DTS::INSTANCE. |
| Tag.N.Key | String | Yes | testkey1 | The key of the tag. Note N specifies the serial number of the tag. For example, Tag.1.Key specifies the key of the first tag and Tag.2.Key specifies the key of the second tag. The value of this parameter cannot be an empty string. |

| Tag.N.Value | String | Yes | testvalue1 | The value of the tag Note N specifies the serial number of the tag. For example, Tag.1.Value specifies the value of the first tag and Tag.2.Value specifies the value of the second tag. The value of this parameter can be an empty string. |
|---|---|---|---|---|

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| ErrCode | String | InternalError | The error code returned if the request failed. |
| ErrMessage | String | The request processing has failed due to some unknown error. | The error message returned if the request failed. |
| RequestId | String | 755D7B84-6813-42B0-BC9D- 2699CFEA**** | The ID of the request. |
| Success | Boolean | true | Indicates whether the request was successful. |

**Examples**

Sample requests

```
http(s)://dts.aliyuncs.com/?Action=TagResources &RegionId=cn-hangzhou &ResourceId.1=dtsntk10k6r12v**** &ResourceType=ALIYUN::DTS::INSTANCE &Tag.1.Key=testkey1 &Tag.1.Value=testvalue1 &<Common request parameters>
```

Sample success responses

| XML | format |
|---|---|
| <TagResourcesResponse> <RequestId>755D7B84-6813-42B0-BC9D-2699CFEA****</RequestId> <Success>true</Success> </TagResourcesResponse> |   |

| JSON | format |
|---|---|
| { "RequestId": "755D7B84-6813-42B0-BC9D-2699CFEA****", "Success": true } |   |

##### 1.5.7.2 ListTagResources

Queries the tags that are added to specific data migration, data synchronization, or change tracking instances, or queries the instances to which specific tags are added.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ListTagResources | The operation that you want to perform. Set the value to ListTagResources. |
| RegionId | String | Yes | cn-hangzhou | The ID of the region in which the data migration, data synchronization, or change tracking instance resides. |
| ResourceType | String | Yes | ALIYUN::DTS::INSTANCE | The resource type. The parameter value is fixed to ALIYUN::DTS::INSTANCE. |
| NextToken | String | No | 212db86sca4384811e0b5e8 707ec2**** | The query token. Note If a query does not return all results, you can specify the value of the NextToken response parameter in the next query to obtain more results. |

| ResourceId.N | RepeatList | No | dtsntk10k6r12v**** | The ID of the data migration, data synchronization, or change tracking instance. Note N specifies the serial number of the instance. For example, ResourceId.1 specifies the ID of the first instance and ResourceId.2 specifies the ID of the second instance. You can specify 1 to 50 instance IDs at a time. You must set at least one of the ResourceId.N and Tag.N.Key parameters. |
|---|---|---|---|---|
| Tag.N.Key | String | No | testkey1 | The key of the tag. Note N specifies the serial number of the tag. For example, Tag.1.Key specifies the key of the first tag and Tag.2.Key specifies the key of the second tag. You can specify 1 to 20 tag keys at a time. You must set at least one of the Tag.N.Key and ResourceId.N parameters and the specified parameter value cannot be an empty string. |
| Tag.N.Value | String | No | testvalue1 | The value of the tag Note N specifies the serial number of the tag. For example, Tag.1.Value specifies the value of the first tag and Tag.2.Value specifies the value of the second tag. You can specify 1 to 20 tag values at a time. The value of this parameter can be an empty string. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| ErrCode | String | InternalError | The error code returned if the request failed. |
| ErrMessage | String | The request processing has failed due to some unknown error. | The error message returned if the request failed. |
| NextToken | String | 212db86sca4384811e0b5e8707e c2**** | The query token. Note If a query does not return all results, you can specify the value of the NextToken response parameter in the next query to obtain more results. |
| RequestId | String | 609AD332-F2B1-48B7-BF43- 41FEE641**** | The ID of the request. |
| Success | Boolean | true | Indicates whether the request was successful. |
| TagResources | Array of TagResource |   | The information about the tags returned. |
| TagResource |   |   |   |
| ResourceId | String | dtsntk10k6r12v**** | The ID of the data migration, data synchronization, or change tracking instance. |
| ResourceType | String | ALIYUN::DTS::INSTANCE | The resource type. The parameter value is fixed to ALIYUN::DTS::INSTANCE. |
| TagKey | String | testkey1 | The key of the tag. |
| TagValue | String | testvalue1 | The tag value that is associated with the tag key. |

**Examples**

Sample requests

```
http(s)://dts.aliyuncs.com/?Action=ListTagResources &RegionId=cn-hangzhou &ResourceType=ALIYUN::DTS::INSTANCE &ResourceId.1=dtsntk10k6r12v**** &Tag.1.Key=testkey1 &Tag.1.Value=testvalue1
```

```xml
<ListTagResourcesResponse>
      <RequestId>609AD332-F2B1-48B7-BF43-41FEE641****</RequestId>
      <TagResources>
            <ResourceId>dtsntk10k6r12v****</ResourceId>
            <TagKey>testkey1</TagKey>
            <ResourceType>ALIYUN::DTS::INSTANCE</ResourceType>
            <TagValue>testvalue1</TagValue>
      </TagResources>
      <Success>true</Success>
</ListTagResourcesResponse>
```

| JSON | format |
|---|---|
| { "RequestId": "609AD332-F2B1-48B7-BF43-41FEE641****", "TagResources": [ { "ResourceId": "dtsntk10k6r12v****", "TagKey": "testkey1", "ResourceType": "ALIYUN::DTS::INSTANCE", "TagValue": "testvalue1" } ], "Success": true } |   |

##### 1.5.7.3 UntagResources

Removes tags from one or more data migration, data synchronization, or change tracking instances.

> **Note:** If a tag is removed from an instance and is not added to other instances, the tag is deleted.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | UntagResources | The operation that you want to perform. Set this parameter to UntagResources. |
| RegionId | String | Yes | cn-hangzhou | The ID of the region in which the data migration, data synchronization, or change tracking instances reside. |
| ResourceId.N | RepeatList | Yes | dtsntk10k6r12v**** | The ID of the data migration, data synchronization, or change tracking instance. You can call the DescribeDtsJobs operation to query the instance ID. Note N specifies the serial number of the instance. For example, ResourceId.1 specifies the ID of the first instance and ResourceId.2 specifies the ID of the second instance. You can specify 1 to 50 instance IDs at a time. |
| ResourceType | String | Yes | ALIYUN::DTS::INSTANCE | The resource type. The parameter value is fixed to ALIYUN::DTS::INSTANCE. |

| TagKey.N | RepeatList | No | testkey1 | The key of the tag. Note N specifies the serial number of the tag. For example, TagKey.1 specifies the key of the first tag and TagKey.2 specifies the key of the second tag. You can specify 1 to 20 tags at a time. The value of this parameter cannot be an empty string. You must set at least one of the TagKey.N andA ll parameters. If you specify both the TagKey.N and All parameters, only the TagKey.N parameter takes effect. |
|---|---|---|---|---|
| All | Boolean | No | false | Specifies whether to remove all tags from the specified instances. Valid values: true false: To remove only specific tags, you must set the TagKey.N parameter. Note You must set at least one of the All andT agKey.N parameters. If you specify both the All parameter and the TagKey.N parameter, the All parameter does not take effect. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| ErrCode | String | InternalError | The error code returned if the request failed. |
| ErrMessage | String | The request processing has failed due to some unknown error. | The error message returned if the request failed. |
| RequestId | String | ED3A8FE0-EEFA-4416-BC42- 34D61A52**** | The ID of the request. |
| Success | Boolean | true | Indicates whether the request was successful. |

**Examples**

Sample requests

```
http(s)://dts.aliyuncs.com/?Action=UntagResources &RegionId=cn-hangzhou &ResourceId.1=dtsntk10k6r12v**** &ResourceType=ALIYUN::DTS::INSTANCE &<Common request parameters>
```

Sample success responses

| XML | format |
|---|---|
| <UntagResourcesResponse> <RequestId>ED3A8FE0-EEFA-4416-BC42-34D61A52****</RequestId> <Success>true</Success> </UntagResourcesResponse> |   |

| JSON | format |
|---|---|
| { "RequestId": "ED3A8FE0-EEFA-4416-BC42-34D61A52****", "Success": true } |   |

#### 1.5.8 Additional description of parameters

##### 1.5.8.1 MigrationObject

When you call the ConfigureMigrationJob operation, you must set the MigrationObject parameter. This topic provides the definition and examples of the MigrationObject parameter.

**Related API operation**

**Definition of the MigrationObject parameter**

The value of the MigrationObject parameter is an array of JSON objects. Regular expressions are supported. The following script shows the parameter definition. `[` `{`

```json
        "DBName":"The name of the database that you want to migrate",
        "NewDBName":"The database name that you want to use in the destination instance",
        "SchemaName":"The name of the schema that you want to migrate",
        "NewSchemaName":"The schema name that you want to use in the destination instance",
        "AllTable": false,
        "TableIncludes":[
```

`{`

```json
                "TableName":"The name of the table that you want to migrate",
                "NewTableName":"The table name that you want to use in the destination instance",
                "FilterCondition":"where condition",
                "PrimaryKey":"The primary key columns of the table that you want to migrate. Separate multiple values with commas (,).",
                "PartKey":"The distribution columns of the table that you want to migrate. Separate multiple values with commas (,).",
                "ColumnIncludes":[
```

`{`

```json
                        "ColumnName":"The name of the column that you want to migrate from the source table",
                        "NewColumnName":"The column name that you want to use in the destination instance"
```

`}` `],`

```json
                "ColumnExcludes":[{
                    "ColumnName":"The name of the column that you do not want to migrate from the source table"
```

`}]` `}` `],`

```json
        "TableExcludes":[{
            "TableName":"The name of the table that you do not want to migrate"
```

`}]` `}` `]` Table 1. Additional description

| Parameter | Description |   |   |   |
|---|---|---|---|---|
| SchemaName | This parameter is available and must be set only if the engine type of the source database is SQL Server or PostgreSQL. |   |   |   |
| NewSchemaName | This parameter is available only if the engine type of the destination database is SQL Server or PostgreSQL. |   |   |   |
| ALLTABLE | Specifies whether to migrate all tables under the schema. The default value isf alse. You can change the value to true. If the value is false, you must set the TableIncludes and TableExcludes parameters. If the value is true, you must set the TableIncludes parameter. |   |   |   |
| PrimaryKey | This parameter is available and must be set only if the engine type of the destination database is AnalyticDB for MySQL or AnalyticDB for PostgreSQL. |   |   |   |
| PartKey | This parameter is available and must be set only if the engine type of the destination database is AnalyticDB for MySQL or AnalyticDB for PostgreSQL. |   |   |   |
| ColumnName and ColNewColumnNameumnName | You must make sure that the column names of the source table correspond to the column names of the destination table one by one. Otherwise, DTS may fail to identify the corresponding columns. |   |   |   |
| FilterCondition | The filter conditions. Only the data that meets the specified conditions is migrated to the destination database. Note A filter condition can be a standard SQL WHERE statement. You can use apostrophes (') in a filter condition if necessary. For example, you can enter address in('hangzhou','shanghai') . |   |   |   |
|   |   | address |   |   |

|   | in('hangzhou','shanghai') |
|---|---|

**Configuration examples**

Example 1: Migrate all tables in the dtstestdata database. `[{`

```json
    "DBName": "dtstestdata"
```

`}]` Example 2: Migrate all tables in the dtstestdata database to the mysqltest database of the destination instance. `[{`

```json
    "DBName": "dtstestdata",
    "NewDBName": "mysqltest"
```

`}]` Example 3: Migrate all tables in the dtstestdata database and the mysqltest database. `[{`

```json
    "DBName": "dtstestdata"
},{
    "DBName": "mysqltest"
```

`}]` Example 4: Migrate all tables in the dtstestdata database except the tables whose names are prefixed with "order." `[{`

```json
    "DBName": "dtstestdata",
    "AllTable": false,
    "TableExcludes": [{
        "TableName": "order.*"
```

`}]` `}]` Example 6: Migrate data with values greater than 100 in the ID column of the customer table in the dtstestdata database. `[{`

```json
    "SchemaName": "dtstestdata",
    "TableIncludes": [{
        "TableName": "customer",
        "FilterCondition": "id > 100"
```

`}]` `}]` Example 7: Migrate the ID and address columns of the customer table in the dtstestdata database. `[{`

```json
    "SchemaName": "dtstestdata",
    "TableIncludes": [{
        "TableName": "customer",
        "ColumnIncludes": [{
                "ColumnName": "id"
```

`},` `{`

```json
                "ColumnName": "address"
```

`}` `]` `}]` `}]` Example 8: Migrate the customer table in the dtstestdata database to AnalyticDB for MySQL or AnalyticDB for PostgreSQL, and set the primary key and distribution key to CREATE_TIME in the destination table. `[{`

```json
    "SchemaName": "dtstestdata",
    "TableIncludes": [{
        "TableName": "customer",
        "PrimaryKey":"CREATE_TIME",
        "PartKey":"CREATE_TIME",
```

`}]` `}]`

**Supported regular expressions**

| Symbol | Description |
|---|---|
| Period (.) | Matches any single character except '\r\n'. |
| Asterisk (*) | Matches zero or more repetitions of the preceding sub-expression. For example, h.*llo matches strings such as hllo and heeeello. |
| Question mark (?) | Matches zero or one repetition of the preceding sub-expression. For example, h.?llo matches hllo and hello, but not haello. |
| Character set [characters] | Matches any single character included in the brackets. For example, h[ae]llo matches hallo and hello. |
| Negative character set [^characters] | Matches any single character except the characters included in the brackets. For example, h[ae]llo matches hcllo or hdllo, but not hallo or hello. |
| Character range [character1-character2] | Matches any characters within the range from character1 to character2. Examples: [0-9] and [a-z]. |

##### 1.5.8.2 SubscriptionObjects

When you call the ConfigureSubscriptionInstance operation, you must set the SubscriptionObjects parameter. This topic provides the definition and examples of the SynchronizationObjects parameter.

**Related API operation**

**Definition of the SubscriptionObjects parameter**

The value of the SubscriptionObjects parameter is an array of JSON objects. Regular expressions are supported. The following script shows the parameter definition. `[{`

```json
    "DBName":"The name of the database from which you want to track data changes",
    "TableIncludes": [{
        "TableName":"The name of the table from which you want to track data changes",
    }],
    "TableExluces": [{
        "TableName": "The name of the table that you want to exclude from the change tracking instance",
```

`}]` `}]`

**Configuration examples**

Example 1: Track data changes from all tables in the dtstestdata database. `[{`

```json
    "DBName": "dtstestdata"
```

`}]` Example 2: Track data changes from all tables in the dtstestdata and mysqltest databases. `[{`

```json
    "DBName": "dtstestdata"
},{
    "DBName": "mysqltest"
```

`}]` Example 3: Track data changes from the customer and order tables in the dtstestdata database. `[{`

```json
    "DBName": "dtstestdata",
    "TableIncludes": [{
        "TableName": "customer"
    }, {
        "TableName": "order"
```

`}]` `}]` Example 4: Track data changes from all tables in the dtstestdata database except the tables whose names are prefixed with "order." `[{`

```json
    "DBName": "dtstestdata",
    "TableExcludes": [{
        "TableName": "order.*"
```

`}]` `}]`

**Supported regular expressions**

| Symbol | Description |
|---|---|
| Period (.) | Matches any single character except '\r\n'. |
| Asterisk (*) | Matches zero or more repetitions of the preceding sub-expression. For example, h.*llo matches strings such as hllo and heeeello. |
| Question mark (?) | Matches zero or one repetition of the preceding sub-expression. For example, h.?llo matches hllo and hello, but not haello. |
| Character set [characters] | Matches any single character included in the brackets. For example, h[ae]llo matches hallo and hello. |
| Negative character set [^characters] | Matches any single character except the characters included in the brackets. For example, h[ae]llo matches hcllo or hdllo, but not hallo or hello. |
| Character range [character1-character2] | Matches any characters within the range from character1 to character2, for example, [0-9] and [a-z]. |

##### 1.5.8.3 SynchronizationObjects

When you call the ConfigureSynchronizationJob or ModifySynchronizationObject operation, you must specify the SynchronizationObjects parameter. This topic provides the definition and examples of the SynchronizationObjects parameter.

**Related API operations**

**Definition of the SynchronizationObjects parameter**

The value of the SynchronizationObjects parameter is an array of JSON objects. Regular expressions are supported. The following script shows the parameter definition. `[{`

```json
    "DBName":"The name of the database that you want to synchronize",
    "NewDBName":"The database name that you want to use in the destination instance",
    "SchemaName":"The name of the schema that you want to synchronize",
    "NewSchemaName":"The schema name that you want to use in the destination instance",
    "AllTable": false,
    "TableIncludes":[{
    "TableName":"The name of the table that you want to synchronize",
    "NewTableName":"The table name that you want to use in the destination instance",
    "FilterCondition":"where condition",
    "PrimaryKey":"The primary key columns of the table that you want to synchronize. Separate multiple values with commas (,).",
    "PartKey":"The distribution columns of the table that you want to synchronize. Separate multiple values with commas (,).",
    "ColumnIncludes":[{
    "ColumnName":"The name of the column that you want to synchronize from the source table",
    "NewColumnName":"The column name that you want to use in the destination instance"
    }],
    "ColumnExcludes":[{
    "ColumnName":"The name of the column that you do not want to synchronize from the source table"
```

`}]`

```json
    }],
    "TableExcludes": [{
    "TableName":"The name of the table that you do not want to synchronize"
```

`}]` `}]`

**Additional description**

| Parameter | Description |   |   |   |
|---|---|---|---|---|
| SchemaName | This parameter is available and must be set only if the engine type of the source database is SQL Server or PostgreSQL. |   |   |   |
| NewSchemaName | This parameter is available only if the engine type of the destination database is SQL Server or PostgreSQL. |   |   |   |
| ALLTABLE | Specifies whether to synchronize all tables under the schema. The default value isf alse. You can change the value to true. If the value is false, you must set the TableIncludes and TableExcludes parameters. If the value is true, you must set the TableIncludes parameter. |   |   |   |
| PrimaryKey | This parameter is available and must be set only if the engine type of the destination database is AnalyticDB for MySQL or AnalyticDB for PostgreSQL. |   |   |   |
| PartKey | This parameter is available and must be set only if the engine type of the destination database is AnalyticDB for MySQL or AnalyticDB for PostgreSQL. |   |   |   |
| ColumnName and NewColumnName | You must make sure that the column names of the source table correspond to the column names of the destination table one by one. Otherwise, Data Transmission Service (DTS) may fail to identify the corresponding columns. |   |   |   |
| FilterCondition | The filter conditions. Only the data that meets the specified conditions is synchronized to the destination database. Note A filter condition can be a standard SQL WHERE statement. You can use apostrophes (') in a filter condition if necessary. For example, you can enter address in('hangzhou','shanghai') . |   |   |   |
|   |   | address |   |   |

|   | in('hangzhou','shanghai') |
|---|---|

**Configuration examples**

Example 1: Synchronize all tables in the dtstestdata database. `[{`

```json
    "DBName": "dtstestdata"
```

`}]` Example 2: Synchronize all tables in the dtstestdata database except the tables whose names are prefixed with "order." `[{`

```json
    "DBName": "dtstestdata",
    "AllTable": false,
    "TableExcludes": [{
        "TableName": "order.*"
```

`}]` `}]` Example 3: Synchronize the customer table in the dtstestdata database to AnalyticDB for MySQL or AnalyticDB for PostgreSQL, and set the primary key and distribution key to CREATE_TIME in the destination table. `[{`

```json
    "SchemaName": "dtstestdata",
    "TableIncludes": [{
        "TableName": "customer",
        "PrimaryKey":"CREATE_TIME",
        "PartKey":"CREATE_TIME",
```

`}]` `}]`

**Supported regular expressions**

| Symbol | Description |
|---|---|
| Period (.) | Matches any single character except '\r\n'. |
| Asterisk (*) | Matches zero or more repetitions of the preceding sub-expression. For example, h.*llo matches strings such as hllo and heeeello. |
| Question mark (?) | Matches zero or one repetition of the preceding sub-expression. For example, h.?llo matches hllo and hello, but not haello. |
| Character set [characters] | Matches any single character included in the brackets. For example, h[ae]llo matches hallo and hello. |
| Negative character set [^characters] | Matches any single character except the characters included in the brackets. For example, h[ae]llo matches hcllo or hdllo, but not hallo or hello. |
| Character range [character1-character2] | Matches any characters within the range from character1 to character2, for example, [0-9] and [a-z]. |

##### 1.5.8.4 MigrationReserved

When you call the ConfigureMigrationJob or ConfigureSynchronizationJob operation, you can set the MigrationReserved parameter to meet special requirements. For example, you can specify whether to automatically start a precheck.

**Limits**

To ensure that you can use this parameter, you must use the latest SDK version. For more information, see the following topics: Get started with SDK for Java Get started with SDK for Phython Get started with SDK for Go

**Related API operations**

**Definition of the MigrationReserved parameter**

The value of the MigrationReserved parameter is a JSON string. The following table describes the parameter definition.

| Parameter | Applicable API operations | Description |
|---|---|---|
| autoStartModulesAfterConfig | ConfigureMigrationJob ConfigureSynchronizationJob | Specifies whether to automatically start a precheck after the instance is configured. Valid values: all: After you configure the Data Transmission Service (DTS) instance, the precheck module and all subsequent modules are automatically started. none: After you configure the DTS instance, the precheck module and subsequent modules are not automatically started. In this case, you must manually start the instance. Default value: all. |
| targetTableMode | ConfigureMigrationJob ConfigureSynchronizationJob | Specifies whether to ignore schema name conflicts during the precheck. Valid values: 0: reports an error and stops the precheck if schema name conflicts are detected. 2: ignores schema name conflicts and continues the precheck. |
| srcRedisType | ConfigureSynchronizationJob | The value is fixed to enterprise, which indicates ApsaraDB for Redis Enhanced Edition (Tair) instance. Note This parameter is applicable to only data synchronization between ApsaraDB for Redis Enhanced Edition (Tair) instances. |
| destRedisType |   |   |

**Configuration example**

`{`

```json
  "autoStartModulesAfterConfig": "none",
  "targetTableMode": 2
```

`}`

## 2 Appendixes

### 2.1 Use the ASAPI gateway to call API operations

You can use the Apsara Stack API (ASAPI) gateway to call API operations of most Apsara Stack services. This topic describes how to call API operations by using the ASAPI gateway and provides links to references.

**Procedure**

1. Obtain the ASAPI SDK.
Before you use ASAPI to call an API operation, you must obtain the ASAPI SDK. For more information, see Obtain the ASAPI SDK.
2. Obtain the endpoint of ASAPI. For more information, see Obtain the endpoint of ASAPI.
3. Obtain an AccessKey pair.
Obtain the AccessKey pair that is required for calling an API operation.

> **Note:** We recommend that you use the AccessKey pair of a personal account to call the API operations of the Apsara Uni-manager Management Console and cloud services.

4. Obtain the region ID.
Obtain the region ID that is required for calling an API operation.
5. Obtain the organization ID and resource set ID.
You can call the GetOrganizationList operation to obtain the organization ID. For more information, see GetOrganizationList in Apsara Uni-manager M anagement Console Developer Guide. You can call the ListResourceGroup operation to obtain the resource set ID. For more information, see ListResourceGroup in Apsara Uni-manager Man agement Console Developer Guide.

> **Note:** When you call an API operation, you can specify the organization ID and resource set ID by using the <x-acs-organizationid> and <x-acs- resourcegroupid> parameters. This allows you to query specified resources.
> If you do not set the <x-acs-organizationid> parameter, the organization to which the current user belongs is used by default.
> If you do not set the <x-acs-resourcegroupid> parameter, it is empty by default. If you specify a resource set ID, you must also specify an organization ID.

6. Refer to the API reference.
Obtain the developer guide of the Apsara Stack service that you want to use. You can learn the features of API operations and how to call the API operations.
7. Use ASAPI SDK to call API operations.
After you complete the preceding steps, you can use the ASAPI SDK to call API operations. For more information about how to use SDKs for different languages, see the relevant topics. The following example shows how to call the DescribeInstances operation of Elastic Compute Service (ECS) by using SDK for Java:

```java
public static void main(String[] args) {
    ASClient client = new ASClient();
    // Specify the caller. The caller is recorded in logs.
    client.setSdkSource("autoTest");
    // Set request parameters.
    Map<String, Object> parameters = new HashMap<String, Object>();;
    parameters.put("Product", "Ecs");// Specify the POP code, which is the same as the POP code in the corresponding API directory.
    parameters.put("Action", "DescribeInstances"); // Specify the name of the API operation. Use the same letter case as the corresponding A
PI directory.
    parameters.put("Version", "2014-05-26"); // Specify the API version.
    // Specify the region ID that you obtained.
    parameters.put("RegionId", "xxx");
    // Specify your AccessKey ID and AccessKey secret.
    parameters.put("AccessKeyId", "xxx");
    parameters.put("AccessKeySecret", "xxx");
    // Add the parameters based on the API reference. Take note that the parameters are case-sensitive.
    parameters.put("PageNumber",1);
    parameters.put("PageSize",10);
    Map<String,String> headers=new HashMap<>();
    // Specify the organization ID in the Apsara Uni-manager Management Console.
    headers.put("x-acs-organizationid","3");
    // Specify the resource set ID in the Apsara Uni-manager Management Console.
    //headers.put("x-acs-resourcegroupid", "<your-resourcegroupid>");
    // Specify the endpoint of ASAPI.
    String endpoint="https://public.asapi.xxx.xxx/asapi/v3";
    // Initiate the request.
    String result = client.doPost(endpoint,headers, parameters);
    // Display the results.
    System.out.println(JSONObject.toJSONString(JSONObject.parseObject(result), SerializerFeature.PrettyFormat));
```

`}`

### 2.2 Use the ASAPI gateway to make API calls

#### 2.2.1 Obtain the endpoint of ASAPI

This topic describes three methods that you can use to obtain an endpoint of Apsara Stack API (ASAPI). This topic also describes how to verify the endpoi

**Methods**

**Method 1: Use Registration Vars of Services to obtain an endpoint**

1. Log on to the Apsara Infrastructure Management Console.
i. Log on to the Apsara Uni-manager Operations Console. ii. In the top navigation bar, click **Products**. iii. Choose **Platforms** > **Apsara Infrastructure Management Framework**.
2. In the left-side navigation pane, click **Reports**.
3. On the **All Reports** page, search for `Registration Vars of Services` . In the report list that appears, click the name of the report.
4. On the **Registration Vars of Services** page, click the
icon to the right of **Service** and enter `asapi` in the search box.
5. Find the asapi service, right-click the service in the **Service Registration** column, and then select **Show More** from the shortcut menu.
In the **Details** dialog box, obtain the value of **asapi.public.endpoint**.
6. Generate an endpoint for ASAPI in the following format:

```
https://<asapi.public.endpoint>/asapi/v3
```

**Method 2: Use cluster resources to generate an endpoint**

1. Log on to the Apsara Infrastructure Management Console.
2. Go to the cluster operations page.
i. In the left-side navigation pane, choose **Operations** > **Cluster Operations**. ii. In the **Cluster** search box, enter `ascm` . iii. In the **Actions** column, click **Operations**.
3. Obtain the domain value.
i. Click the **Cluster Resources** tab. ii. In the **Name** field, search for `asapi_dns_public` . iii. In the **Application Parameter** column, click **Details**. In the **Application Parameter** message, obtain the value of the **domain** parameter.
4. Generate an endpoint for ASAPI in the following format:

```
https://<domain>/asapi/v3
```

**Method 3: Concatenate strings to generate an endpoint**

You can concatenate strings to generate an endpoint in the following format:

```
https://public.asapi.<region>.<internet-domain>/asapi/v3
```

| Note 1. Replace <region> with your actual region ID. 2. Replace <internet- domain> with the root domain of your Apsara Stack service. To obtain the root domain, contact Apsara Stack O&M engineers. Make sure that you u domain parameter instead of the intranet-domain parameter. |   |   |   |   |
|---|---|---|---|---|
| Example: if the region value is | cn-****-****-d01 | and the internet-domain value is | inter.****.****.com | , |

the following endpoint is used as a reference:

```
https://public.asapi.cn-****-****-d01.inter.****.****.com/asapi/v3
```

**Verify the endpoint**

Enter the following code. If you cannot access the endpoint, the endpoint is unavailable. You can use the historical endpoint.

| curl https://public.asapi.${global:region}.${global:internet-domain}/api/version -k |   |
|---|---|
| Note ${global:region} and ${global:internet-domain} are variables. You must replace these variables with the actual values that you obtained. |   |

Available endpoint example: Unavailable endpoint example:

**Historical endpoint**

Only the HTTP protocol is supported. The historical endpoint is suffixed with `intranet-domain` and is in the following format:

| http://server.asapi.${global:region}.${global:intranet-domain}/asapi/v3 |   |
|---|---|
| Note ${global:region} and ${global:intranet-domain} are variables. You must replace these variables with the actual values that you obtained. |   |

**Procedure**

To obtain the actual values of the ${global:region}, ${global:internet-domain}, and ${global:intranet-domain} variables, perform the following steps:
1. In the address bar, enter region-id.aso.intranet-domain-id.com URL and press the Enter key.

> **Note:** You can select a language from the drop-down list in the upper-right corner of the current page.

2. Enter your username and password.

> **Note:** Obtain the username and password that are used to log on to the Apsara Uni- manager Operations Console from the deployment personnel or an administrator.

The first time that you log on to the Apsara Uni-manager Operations Console, change the password of your username as prompted. To enhance security, your password must meet the following requirements: The password contains uppercase and lowercase letters. The password contains digits. The password contains special characters, such as exclamation points (!), at signs (@), number signs (#), dollar signs ($), and percent signs (%). The password must be 10 to 20 characters in length.
3. Click **Log On** to log on to the **Apsara Uni-manager Operations Console**.
4. In the top navigation bar, choose **Products** > **Platforms** > **Apsara Infrastructure Management Framework** to go to the Apsara Infrastructure Ma
5. In the left-side navigation pane, choose **Operations** > **Cluster Operations**.
6. On the **Cluster Operations** page, enter **ascm-A** in the Cluster field and click the search icon. Click the cluster name in the **Cluster** column.
7. Click the **Cluster Configuration** tab.
8. On the **File Info** tab of **Cluster Configuration**, click **kv.conf**.
9. In the right window of the displayed page, press Ctrl+F to search for the values of the region, internet-domain, and intranet-domain parameters.
Replace ${global:region} with the obtained region value, ${global:internet-domain} with the obtained internetdomain value, and ${global:intranet-domain} with the obtained intranet-domain value.

> **Note:** Do not include ${global:} in the endpoint of ASAPI that you want to use.

#### 2.2.2 Obtain the ASAPI SDK

Apsara Stack API (ASAPI) is a unified portal provided by Apsara Stack. You can use ASAPI to connect to all Apsara Stack services. Apsara Stack provides SDKs for API calls.

**Public environment**

If you use the public environment, you can go to the Apsara Stack documentation page and download the ASAPI SDK in the **Other Resources** section at the lower part of the page.

**Private environment**

If you use the private environment, you must switch to the public environment and then go to the Apsara Stack documentation page. At the lower part of the page, download the ASAPI SDK in the **Other Resources** section. Table 1. ASAPI SDK for Java

| greopId | artifactId | version |
|---|---|---|
| com.alibaba | alicrypto-java-aliyun | 1.0.4 |
| com.alibaba | fastjson | 1.2.68 |
| org.bouncycastle | bcprov-jdk15to18 | 1.66 |
| org.bouncycastle | bcpkix-jdk15on | 1.65 |
| org.bouncycastle | bcprov-jdk15on | 1.65 |
| com.aliyun | gmsse | 1.1.0 |
| org.apache.commons | commons-lang3 | 3.0 |
| commons-codec | commons-codec | 1.11 |
| commons-logging | commons-logging | 1.2 |
| org.apache.httpcomponents | httpcore | 4.4.11 |
| org.apache.httpcomponents | httpclient | 4.5.7 |

Table 2. ASAPI SDK for Python

| Package | Version |
|---|---|
| aliyun-python-sdk-core | 2.13.35 |
| certifi | 2021.5.30 |
| cffi | 1.14.6 |
| charset-normalizer | 2.0.4 |
| cryptography | 3.4.8 |
| idna | 3.2 |
| jmespath | 0.10.0 |
| pycparser | 2.20 |
| requests | 2.26.0 |
| urllib3 | 1.26.6 |

> **Note:** You can use the version for each package listed in the preceding table or a later version.

### 2.3 STS overview

#### 2.3.1 What is STS?

Apsara Stack Security Token Service (STS) allows you to manage temporary credentials to your Apsara Stack resources. Resource Access Management (RAM) provides RAM users and roles. A RAM role does not have permanent identity credentials. A RAM role can be assumed for Apsara Stack resource access only by using an STS token. When an STS token is issued, you can specify a validity period and access permissions for the STS token.

**Use an STS token to assume a RAM role**

An authorized RAM user can use an AccessKey pair to call the AssumeRole operation. This way, the RAM user can obtain an STS token of a RAM role and use the STS token to access Apsara Stack resources.

**Benefits**

STS tokens reduce the risks of AccessKey pair leaks. An AccessKey pair is a long-term credential for a RAM user. STS tokens are temporary credentials. You can specify a validity period for an STS token. The token automatically becomes invalid when it expires. You do not need to rotate STS tokens on a regular basis. You can attach custom policies to STS tokens for flexible and fine-grained authorization.

#### 2.3.2 AssumeRole

Obtains a Security Token Service (STS) token to assume a RAM role. In this operation, an Alibaba Cloud account is used as the trusted entity of the Resource Access Management (RAM) role.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | AssumeRole | The operation that you want to perform. Set the value to AssumeRole. |
| RoleArn | String | Yes | acs:ram::123456789012****:r ole/adminrole | The Alibaba Cloud Resource Name (ARN) of the RAM role. The trusted entity of the RAM role is an Alibaba Cloud account. |
| RoleSessionName | String | Yes | alice | The custom name of the role session. You can specify the value of this parameter based on your business requirements. In most cases, this parameter is set to the identity of the user who calls the operation, such as the username. In ActionTrail logs, you can distinguish the users who assume the same RAM role to perform operations based on the value of the RoleSessionName parameter. This way, you can perform user-specific auditing. The value must be 2 to 64 characters in length and can contain letters, digits, periods (.), at signs (@), hyphens (-), and underscores (). _ |
| Policy | String | No | {"Statement": [{"Action": ["*"],"Effect": "Allow","Resource": ["*"]}],"Version":"1"} | The policy that specifies the permissions of the returned STS token. You can use this parameter to grant the STS token fewer permissions than the permissions granted to the RAM role. The value of the parameter must be 1 to 1,024 characters in length. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 6894B13B-6D71-4EF5-88FA- F32781734A7F | The ID of the request. |
| Credentials | None | None | The access credentials. |
| AccessKeyId | String | STS.L4aBSCSJVMuKg5U1**** | The AccessKey ID. |
| AccessKeySecret | String | ***************************************** | The AccessKey secret. |
| SecurityToken | String | ******** | The STS token. |
| Expiration | String | 2015-04-09T11:52:19Z | The time when the STS token expires. |
| AssumedRoleUser | None | None | The temporary identity that you use to assume the RAM role. |
| Arn | String | acs:ram::123456789012****:role/ adminrole/alice | The ARN of the temporary identity that you use to assume the RAM role. |
| AssumedRoleId | String | 34458433936495****:alice | The ID of the temporary identity that you use to assume the RAM role. |

**Examples**

**Add Project Object Model (POM) dependencies**

The Alibaba Cloud core library is required. Perform the following steps to add the Alibaba Cloud core library to POM:

```xml
    <dependency>
      <groupId>com.aliyun</groupId>
      <artifactId>aliyun-java-sdk-core</artifactId>
      <version>[4.4.9,5.0.0)</version>
    </dependency>
```

**Call an API operation to obtain the STS AccessKey triplet.**

In the following sample code, the `Sts::AssumeRole::2015-04-01` operation is used to obtain the triplet.

```java
package com.aliyuns.test; import com.alibaba.fastjson.JSONObject; import com.aliyuncs.CommonRequest; import com.aliyuncs.CommonResponse; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.exceptions.ServerException; import com.aliyuncs.http.FormatType; import com.aliyuncs.http.HttpClientConfig; import com.aliyuncs.http.MethodType; import com.aliyuncs.http.ProtocolType; import com.aliyuncs.profile.DefaultProfile; import org.apache.commons.lang3.StringUtils; public class STSAccessKeyDemo {
    public static void main(String[] args) {
        // Create and initialize a DefaultAcsClient instance.
        DefaultProfile profile = DefaultProfile.getProfile("<yourRegionID>", "<yourAccessKeyID>", "<yourAccessKeySecret>");
        HttpClientConfig clientConfig = HttpClientConfig.getDefault();
        clientConfig.setIgnoreSSLCerts(true);
        clientConfig.setProtocolType(ProtocolType.HTTPS);
        profile.setHttpClientConfig(clientConfig);
        IAcsClient client = new DefaultAcsClient(profile);
        CommonRequest request = new CommonRequest();
        // Replace "sts.aliyuns.com" with the actual endpoint of the STS token. In most cases, the STS token is in the following format: sts-v
pc.${global:region}.${global:internet-domain}.
        request.setSysDomain("sts.aliyuns.com");
        request.setSysProduct("Sts");
        request.setSysAction("AssumeRole");
        request.setSysVersion("2015-04-01");
        request.setSysMethod(MethodType.POST);
        request.setHttpContentType(FormatType.FORM);
        // Replace "<yourRoleSessionName>" with the alias that you specify in this API operation for the role session. It is a business
parameter.
        request.putQueryParameter("RoleSessionName", "<yourRoleSessionName>");
        // Replace "<yourRoleArn>" with the actual ARN that you obtain in the preceding step for the RAM role.
        request.putQueryParameter("RoleArn", "<yourRoleArn>");
        try {
            CommonResponse response = client.getCommonResponse(request);
            String assumeRole = response.getData();
            if (StringUtils.isEmpty(assumeRole)) return;
            JSONObject assumeRoleJson = JSONObject.parseObject(assumeRole);
            JSONObject credentials = assumeRoleJson.getJSONObject("Credentials");
            // Obtain the STS triplet.
            String stsAK = credentials.getString("AccessKeyId");
            String stsSK = credentials.getString("AccessKeySecret");
            String stsToken = credentials.getString("SecurityToken");
            System.out.println("stsAk: " + stsAK +"\nstsSk: " + stsSK + "\nstsToken: " + stsToken);
        } catch (ServerException e) {
            System.out.println(e.getErrCode());
            System.out.println(e.getErrMsg());
        } catch (ClientException e) {
            System.out.println(e.getErrCode());
            System.out.println(e.getErrMsg());
```

`}` `}` `}`

**Call examples**

In the following sample code, the `DescribeZones` operation in Elastic Compute Service (ECS) is used.

```java
package com.aliyuns.test; import com.aliyuncs.CommonRequest; import com.aliyuncs.CommonResponse; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.exceptions.ServerException; import com.aliyuncs.http.FormatType; import com.aliyuncs.http.HttpClientConfig; import com.aliyuncs.http.MethodType; import com.aliyuncs.http.ProtocolType; import com.aliyuncs.profile.DefaultProfile; public class DescribeZonesDemo {
    public static void main(String[] args) {
        // Replace "<yourRegionID>" with the actual region ID.
        // Replace "<yourStsAccesskey>" and "<yourStsAccessKeySecret>" with the AccessKey ID and secret in the STS triplet that you obtain in
the preceding step.
        DefaultProfile profile = DefaultProfile.getProfile("<yourRegionID>", "<yourStsAccessKey>", "<yourStsAccessKeySecret>");
        HttpClientConfig clientConfig = HttpClientConfig.getDefault();
        clientConfig.setIgnoreSSLCerts(true);
        clientConfig.setProtocolType(ProtocolType.HTTPS);
        profile.setHttpClientConfig(clientConfig);
        IAcsClient client = new DefaultAcsClient(profile);
        CommonRequest request = new CommonRequest();
        request.setSysDomain("ecs.aliyuns.com");
        request.setSysProduct("Ecs");
        request.setSysAction("DescribeZones");
        request.setSysVersion("2014-05-26");
        request.setSysMethod(MethodType.POST);
        request.setHttpContentType(FormatType.FORM);
        //Replace "<yourRegionID>" with the actual region ID.
        request.putHeadParameter("x-acs-regionid", "<yourRegionID>");
        // Replace "<yourStsToken>" with the STS token in the STS triplet that you obtain in the preceding step.
        request.putQueryParameter("SecurityToken", "<yourStsToken>");
        // Specify the resource set ID. It is optional.
        // request.putHeadParameter("x-acs-resourcegroupid", "<yourResourceGroupID>");
        // Specify the organization ID. It is required.
        request.putHeadParameter("x-acs-organizationid", "<yourOrganizationID>");
        try {
            CommonResponse response = client.getCommonResponse(request);
            System.out.println(response.getData());
        } catch (ServerException e) {
            System.out.println(e.getErrCode());
            System.out.println(e.getErrMsg());
        } catch (ClientException e) {
            System.out.println(e.getErrCode());
            System.out.println(e.getErrMsg());
```

`}` `}` `}`

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | InvalidParameter | The parameter RoleArn is wrongly formed. | The error message returned because the ARN format of the RAM role is invalid. |
| 400 | InvalidParameter.RoleArn | The parameter RoleArn is wrongly formed. | The error message returned because the ARN format of the RAM role is invalid. |
| 400 | InvalidParameter.RoleSessionName | The parameter RoleSessionName is wrongly formed. | The error message returned because the format of the RoleSessionName parameter is invalid. The value must be 2 to 64 characters in length and can contain letters, digits, periods (.), at signs (@), hyphens (-), and underscores (). _ |
| 400 | InvalidParameter.DurationSeconds | The Min/Max value of DurationSeconds is 15min/1hr. | The error message returned because the value of the DurationSeconds parameter is invalid. The value must be greater than or equal to 900 and less than or equal to the MaxSessionDuration value. |

| Data Transmission Servic | e | Dev | eloper Guide·Appendixes |   |
|---|---|---|---|---|
| HTTP status code | Error code | Error message | Description |   |
| 400 | InvalidParameter.PolicyGrammar | The parameter Policy has not passed grammar check. | The error message returned because the syntax of the specified policy is invalid. |   |
| 400 | InvalidParameter.PolicySize | The size of Policy must be smaller than 1024 bytes. | The error message returned because the length of the specified policy string exceeds the upper limit. The policy string can be up to 1,024 characters in length. |   |
| 403 | NoPermission | You are not authorized to do this action. You should be authorized by RAM. | The error message returned because the STS token does not have the required permissions. |   |
| 404 | EntityNotExist.Role | The specified Role not exists. | The error message returned because the specified RAM role does not exist. |   |
| 500 | InternalError | STS Server Internal Error happened. | The error message returned because an internal server error has occurred. |   |
