---
title: "Alibaba Cloud Apsara Stack Enterprise V3.12.0 Data Transmission Service Developer Guide 20220928"
product_version: "V3.12.0"
doc_version: "20220928"
pdf_pages: 92
source_pdf: "Alibaba Cloud Apsara Stack Enterprise V3.12.0 Data Transmission Service Developer Guide 20220928.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/01_ApsaraStackEnterprise/V3.12/%E6%95%B0%E6%8D%AE%E5%BA%93/Alibaba%20Cloud%20Apsara%20Stack%20Enterprise%20V3.12.0%20Data%20Transmission%20Service%20Developer%20Guide%2020220928.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes)
---

# Alibaba Cloud Apsara Stack Enterprise V3.12.0 Data Transmission Service Developer Guide 20220928

## Table of Contents

- 1 Developer Guide
  - 1.1 API reference
    - 1.1.1 Call OpenAPI
      - 1.1.1.1 API overview
    - 1.1.2 Data migration APIs
      - 1.1.2.1 ConfigureMigrationJob
        - 1.1.2.1.1 Overview
        - 1.1.2.1.2 Request parameters
        - 1.1.2.1.3 MigrationObject parameter definitions
        - 1.1.2.1.4 Response parameters
        - 1.1.2.1.5 Example
      - 1.1.2.2 CreateMigrationJob
        - 1.1.2.2.1 Overview
        - 1.1.2.2.2 Request parameters
        - 1.1.2.2.3 Response parameters
        - 1.1.2.2.4 Examples
      - 1.1.2.3 DeletetMigrationJob
        - 1.1.2.3.1 Overview
        - 1.1.2.3.2 Request parameters
        - 1.1.2.3.3 Response parameters
        - 1.1.2.3.4 Examples
      - 1.1.2.4 DescribeMigrationJobDetail
        - 1.1.2.4.1 Overview
        - 1.1.2.4.2 Request parameters
        - 1.1.2.4.3 Response parameters
        - 1.1.2.4.4 StructureInitializationDetail parameter definitions
        - 1.1.2.4.5 DataInitializationDetail parameter definitions
        - 1.1.2.4.6 DataSynchronizationDetail parameter definitions
        - 1.1.2.4.7 Examples
      - 1.1.2.5 DescribeMigrationJobStatus
        - 1.1.2.5.1 Overview
        - 1.1.2.5.2 Request parameters
        - 1.1.2.5.3 Response parameters
        - 1.1.2.5.4 Endpoint parameter definitions
        - 1.1.2.5.5 MigrationMode parameter definitions
        - 1.1.2.5.6 PrecheckStatus parameter definitions
        - 1.1.2.5.7 CheckItem parameter definitions
        - 1.1.2.5.8 StructureInitializationStatus parameter definitions
        - 1.1.2.5.9 DataInitializationStatus parameter definitions
        - 1.1.2.5.10 DataSynchronizationStatus parameter definitions
        - 1.1.2.5.11 Examples
      - 1.1.2.6 StartMigrationJob
        - 1.1.2.6.1 Overview
        - 1.1.2.6.2 Request parameters
        - 1.1.2.6.3 Response parameters
        - 1.1.2.6.4 Examples
      - 1.1.2.7 StopMigrationJob
        - 1.1.2.7.1 Overview
        - 1.1.2.7.2 Request parameters
        - 1.1.2.7.3 Response parameters
        - 1.1.2.7.4 Examples
      - 1.1.2.8 SuspendMigrationJob
        - 1.1.2.8.1 Overview
        - 1.1.2.8.2 Request parameters
        - 1.1.2.8.3 Response parameters
        - 1.1.2.8.4 Examples
    - 1.1.3 Data subscription APIs
      - 1.1.3.1 ConfigureSubscriptionInstance
        - 1.1.3.1.1 Overview
        - 1.1.3.1.2 Request parameters
        - 1.1.3.1.3 SubscriptionObject parameter definitions
        - 1.1.3.1.4 Response parameters
        - 1.1.3.1.5 Example
      - 1.1.3.2 CreateSubscriptionInstance
        - 1.1.3.2.1 Overview
        - 1.1.3.2.2 Request parameters
        - 1.1.3.2.3 Response parameters
        - 1.1.3.2.4 Examples
      - 1.1.3.3 DeleteSubscriptionInstance
        - 1.1.3.3.1 Overview
        - 1.1.3.3.2 Request parameters
        - 1.1.3.3.3 Response parameters
        - 1.1.3.3.4 Examples
      - 1.1.3.4 DescribeSubscriptionInstances
        - 1.1.3.4.1 Overview
        - 1.1.3.4.2 Request parameters
        - 1.1.3.4.3 Response parameters
        - 1.1.3.4.4 Examples
      - 1.1.3.5 DescribeSubscriptionInstanceStatus
        - 1.1.3.5.1 Overview
        - 1.1.3.5.2 Request parameters
        - 1.1.3.5.3 Response parameters
        - 1.1.3.5.4 Endpoint parameter definitions
        - 1.1.3.5.5 SubscriptionObject parameter definitions
        - 1.1.3.5.6 Examples
      - 1.1.3.6 ModifyComsumptionTimestamp
        - 1.1.3.6.1 Overview
        - 1.1.3.6.2 Request parameters
        - 1.1.3.6.3 Response parameters
        - 1.1.3.6.4 Examples
      - 1.1.3.7 ModifySubscriptionObject
        - 1.1.3.7.1 Overview
        - 1.1.3.7.2 Request parameters
        - 1.1.3.7.3 SubscriptionObject parameter definitions
        - 1.1.3.7.4 Response parameters
        - 1.1.3.7.5 Examples
      - 1.1.3.8 StartSubscriptionInstance
        - 1.1.3.8.1 Overview
        - 1.1.3.8.2 Request parameters
        - 1.1.3.8.3 Response parameters
        - 1.1.3.8.4 Examples
    - 1.1.4 Data synchronization APIs
      - 1.1.4.1 ConfigureSynchronizationJob
        - 1.1.4.1.1 Overview
        - 1.1.4.1.2 Request parameters
        - 1.1.4.1.3 Response parameters
        - 1.1.4.1.4 Example
      - 1.1.4.2 CreateSynchronizationJob
        - 1.1.4.2.1 Overview
        - 1.1.4.2.2 Request parameters
        - 1.1.4.2.3 Response parameters
        - 1.1.4.2.4 Examples
      - 1.1.4.3 DeleteSynchronizationJob
        - 1.1.4.3.1 Overview
        - 1.1.4.3.2 Request parameters
        - 1.1.4.3.3 Response parameters
        - 1.1.4.3.4 Examples
      - 1.1.4.4 DescribeDataLoadStatus
        - 1.1.4.4.1 Overview
        - 1.1.4.4.2 Request parameters
        - 1.1.4.4.3 Response parameters
        - 1.1.4.4.4 Examples
      - 1.1.4.5 DescribeSynchronizationJobStatus
        - 1.1.4.5.1 Overview
        - 1.1.4.5.2 Request parameters
        - 1.1.4.5.3 Response parameters
        - 1.1.4.5.4 PrecheckStatus parameter definitions
        - 1.1.4.5.5 CheckItem parameter definitions
        - 1.1.4.5.6 StructureInitializationStatus parameter definitions
        - 1.1.4.5.7 DataInitializationStatus parameter definitions
        - 1.1.4.5.8 DataSynchronizationStatus parameter definitions
        - 1.1.4.5.9 Performance parameter definitions
        - 1.1.4.5.10 Examples
      - 1.1.4.6 DescribeSynchronizationJobs
        - 1.1.4.6.1 Overview
        - 1.1.4.6.2 Request parameters
        - 1.1.4.6.3 Response parameters
        - 1.1.4.6.4 SynchronizationInstance parameter definitions
        - 1.1.4.6.5 PrecheckStatus parameter definitions
        - 1.1.4.6.6 CheckItem parameter definitions
        - 1.1.4.6.7 StructureInitializationStatus parameter definitions
        - 1.1.4.6.8 DataInitializationStatus parameter definitions
        - 1.1.4.6.9 DataSynchronizationStatus parameter definitions
        - 1.1.4.6.10 Performance parameter definitions
        - 1.1.4.6.11 Examples
      - 1.1.4.7 DescribeObjectModifyStatus
        - 1.1.4.7.1 Overview
        - 1.1.4.7.2 Request parameters
        - 1.1.4.7.3 Response parameters
        - 1.1.4.7.4 PrecheckStatus parameter definitions
        - 1.1.4.7.5 CheckItem parameter definitions
        - 1.1.4.7.6 StructureInitializationStatus parameter definitions
        - 1.1.4.7.7 DataInitializationStatus parameter definitions
        - 1.1.4.7.8 DataSynchronizationStatus parameter definitions
        - 1.1.4.7.9 Examples
      - 1.1.4.8 ModifySynchronizationObject
        - 1.1.4.8.1 Overview
        - 1.1.4.8.2 Request parameters
        - 1.1.4.8.3 Response parameters
        - 1.1.4.8.4 Examples
      - 1.1.4.9 StartSynchronizationJob
        - 1.1.4.9.1 Overview
        - 1.1.4.9.2 Request parameters
        - 1.1.4.9.3 Response parameters
        - 1.1.4.9.4 Examples
      - 1.1.4.10 SuspendSynchronizationJob
        - 1.1.4.10.1 Overview
        - 1.1.4.10.2 Request parameters
        - 1.1.4.10.3 Response parameters
        - 1.1.4.10.4 Examples
      - 1.1.4.11 DescribeSynchronizationJobStatusList
        - 1.1.4.11.1 Overview
        - 1.1.4.11.2 Request parameters
        - 1.1.4.11.3 Response parameters
        - 1.1.4.11.4 Examples
      - 1.1.4.12 ConfigureSynchronizationJobReplicatorCompare
        - 1.1.4.12.1 Overview
        - 1.1.4.12.2 Request parameters
        - 1.1.4.12.3 Response parameters
        - 1.1.4.12.4 Examples
      - 1.1.4.13 DescribeSynchronizationJobReplicatorCompare
        - 1.1.4.13.1 Overview
        - 1.1.4.13.2 Request parameters
        - 1.1.4.13.3 Response parameters
        - 1.1.4.13.4 Examples
  - 1.2 Call the Java SDK
    - 1.2.1 Quick start
    - 1.2.2 User manual
      - 1.2.2.1 Install the Java SDK
      - 1.2.2.2 Configure identity verification credentials
      - 1.2.2.3 Initiate a call
      - 1.2.2.4 Troubleshooting
      - 1.2.2.5 Errors and troubleshooting

## 1 Developer Guide

### 1.1 API reference

#### 1.1.1 Call OpenAPI

##### 1.1.1.1 API overview

This topic describes the APIs that DTS OpenAPI supports. Data migration APIs

| API | Description |
|---|---|
| ConfigureMigrationJob | Configures a migration task. |
| StartMigrationJob | Starts or restarts a migration task. |
| SuspendMigrationJob | Suspends a migration task. |
| StopMigrationJob | Stops a migration task. |
| DeleteMigrationJob | Deletes a migration task. |
| DescribeMigrationJobStatus | Queries the status of a migration task. |
| DescribeMigrationJobDetail | Queries the details of a migration task. |
| DescribeMigrationJobs | Queries the list of migration tasks. |

Data synchronization APIs

| API | Description |
|---|---|
| CreateSynchronizationJob | Purchases a synchronization instance. |
| ConfigureSynchronizationJob | Configures a synchronization task. |
| StartSynchronizationJob | Starts a synchronization task. |
| SuspendSynchronizationJob | Suspends a synchronization task. |
| DeleteSynchronizationJob | Deletes a synchronization task. |
| ModifySynchronizationObject | Modifies the list of objects to be synchronized. |
| DescribeObjectModifyStatus | Queries the modification status of the list of objects to be synchronized. |
| DescribeSynchronizationJobStatus | Queries the running status of a synchronization task. |

| eveloper Guide·Developer Guide | Data Transmission Servic |
|---|---|

| API | Description |
|---|---|
| DescribeSynchronizationJobs | Queries the list of synchronization tasks. |
| DescribeInitializationStatus | Queries the initialization status of a synchronization task. |

Data subscription APIs

| API | Description |
|---|---|
| CreateSubscriptionInstance | Purchases a subscription channel. |
| ConfigureSubscriptionInstance | Configures a subscription channel. |
| StartSubscriptionInstance | Starts a subscription task. |
| DeleteSubscriptionInstance | Releases a subscription channel. |
| DescribeSubscriptionInstanceStatus | Queries the status of a subscription channel. |
| DescribeSubscriptionInstances | Queries the list of subscription instances. |
| ModifySubscriptionObject | Modifies the list of objects to be subscribed. |
| ModifyConsumptionTimestamp | Modifies the consumption checkpoint. |

#### 1.1.2 Data migration APIs

##### 1.1.2.1 ConfigureMigrationJob

###### 1.1.2.1.1 Overview

You can call this operation to configure a data migration task, including the source and destination instances and the objects to be migrated. Before a migration task is started, you can call this operation repetitively to modify task configurations.

###### 1.1.2.1.2 Request parameters

| Parameter | Type | Requir ed | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to ConfigureMigrationJob. |
| MigrationJobId | String | Yes | The ID of the data migration task. |
| MigrationJobName | String | No | The name of the data migration task. |

| Data Transmission Service |   |   | Developer Guide·Developer Guid |
|---|---|---|---|

| Parameter | Type | Requir ed | Description |
|---|---|---|---|
| SourceEndpoint.InstanceTy pe | String | Yes | The type of the source instance. Valid values: RDS: an ApsaraDB for RDS instance ECS: a user-created database that is hosted on ECS LocalInstance: an on-premises database MongoDB: an ApsaraDB for MongoDB instance |
| SourceEndpoint.Region | String | Yes | The region where the source instance resides. If the source instance is a user-created database, you can select the region that is closest to your data center. Valid values: cn-hangzhou: the China (Hangzhou) region cn-shanghai: the China (Shanghai) region cn-qingdao: the China (Qingdao) region cn-beijing: the China (Beijing) region cn-zhangbei: the China (Zhangjiakou-Beijing Winter Olympics) region cn-shenzhen: the China (Shenzhen) region cn-hongkong: the China (Hong Kong) region us-west-1: the US (Silicon Valley) region us-east-1: the US (Virginia) region ap-southeast-1: the Singapore (Singapore) region cn-hangzhou-finance-1: the China East 1 Finance region cn-qingdao-finance-1: the China North 1 Finance region cn-shanghai-finance-1: the China East 2 Finance region cn-shenzhen-finance-1: the China South 1 Finance region me-east-1: the UAE (Dubai) region en-central-1: the Germany (Frankfurt) region |
| SourceEndpoint.InstanceId | String | No | The ID of the source instance. If you specify the value of the SourceEndpoint.InstanceType parameter as RDS, the value of the SourceEndpoint.InstanceId parameter is the ID of an RDS instance. If you specify the value of the SourceEndpoint.InstanceType parameter as ECS, the value of the SourceEndpoint.InstanceId parameter is the ID of an ECS instance. If you specify the value of the SourceEndpoint.InstanceType parameter as MongoDB, the value of the SourceEndpoint.InstanceId parameter is the ID of an ApsaraDB for MongoDB instance. |

| Parameter | Type | Requir ed | Description |
|---|---|---|---|
| SourceEndpoint.EngineNa me | String | No | The database type of the source instance. This parameter is required if the value of the SourceEndpoint.InstanceType parameter is not RDS. Valid values: MySQL, SQLServer, PostgreSQL, Oracle, MongoDB, and Redis. |
| SourceEndpoint.IP | String | No | The endpoint of the source instance. This parameter is required if the source instance is a user-created database. |
| SourceEndpoint.Port | String | No | The port on which the source instance is listening. This parameter is required if the source instance is a user- created database. |
| SourceEndpoint.OracleSID | String | No | The system ID (SID) of the source Oracle database. |
| SourceEndpoint.Database Name | String | No | The database name of the source instance. This parameter is used to establish a connection if the source instance is a PostgreSQL or MongoDB database. |
| SourceEndpoint.UserName | String | Yes | The username that is used to access the source instance. |
| SourceEndpoint.Password | String | Yes | The password that is used to access the source instance. |
| SourceEndpoint.OwnerID | String | Yes | The ID of the Apsara Stack tenant account to which the source RDS instance belongs. This parameter is available if the source and destination instances belong to different Apsara Stack tenant accounts. |
| SourceEndpoint.Role | String | Yes | The RAM role that the Apsara Stack tenant account of the source RDS instance assigns to the Apsara Stack tenant account of the destination instance. This parameter is available if the source and destination instances belong to different Apsara Stack tenant accounts. For more information about role permissions and how to grant permissions to a role, see Configure RAM authorization for cross-account data migration and synchronization. |
| DestinationEndpoint.Instan ceType | String | Yes | The type of the destination instance. Valid values: RDS: an RDS instance ECS: a user-created database that is hosted on ECS LocalInstance: an on-premises database MongoDB: an ApsaraDB for MongoDB instance Redis: a KVStore for Redis instance DRDS: a Cloud Native Distributed Database PolarDB-X instance (formerly known as DRDS) OceanBase: an ApsaraDB for OceanBase instance |

| Parameter | Type | Requir ed | Description |
|---|---|---|---|
| DestinationEndpoint.Regio n | String | Yes | The region where the destination instance resides. If the destination instance is a user-created database, you can select the region that is closest to your data center. Valid values: cn-hangzhou: the China (Hangzhou) region cn-shanghai: the China (Shanghai) region cn-qingdao: the China (Qingdao) region cn-beijing: the China (Beijing) region cn-zhangbei: the China (Zhangjiakou-Beijing Winter Olympics) region cn-shenzhen: the China (Shenzhen) region cn-hongkong: the China (Hong Kong) region us-west-1: the US (Silicon Valley) region us-east-1: the US (Virginia) region ap-southeast-1: the Singapore (Singapore) region cn-hangzhou-finance-1: the China East 1 Finance region cn-qingdao-finance-1: the China North 1 Finance region cn-shanghai-finance-1: the China East 2 Finance region cn-shenzhen-finance-1: the China South 1 Finance region me-east-1: the UAE (Dubai) region en-central-1: the Germany (Frankfurt) region |

| Parameter | Type | Requir ed | Description |
|---|---|---|---|
| DestinationEndpoint.Instan ceID | String | No | The ID of the destination instance. If you specify the value of the DestinationEndpoint.InstanceType parameter as RDS, the value of the DestinationEndpoint.InstanceID parameter is the ID of an RDS instance. If you specify the value of the DestinationEndpoint.InstanceType parameter as ECS, the value of the DestinationEndpoint.InstanceID parameter is the ID of an ECS instance. If you specify the value of the DestinationEndpoint.InstanceType parameter as MongoDB, the value of the DestinationEndpoint.InstanceID parameter is the ID of an ApsaraDB for MongoDB instance. If you specify the value of the DestinationEndpoint.InstanceType parameter as Redis, the value of the DestinationEndpoint.InstanceID parameter is the ID of a KVStore for Redis instance. If you specify the value of the DestinationEndpoint.InstanceType parameter as DRDS, the value of the DestinationEndpoint.InstanceID parameter is the ID of a Cloud Native Distributed Database PolarDB-X instance. |
| DestinationEndpoint.Engin eName | String | No | The database type of the destination instance. This parameter is required if the destination instance is a user- created database. Valid values: MySQL, PostgreSQL, MongoDB, and Redis. |
| DestinationEndpoint.IP | String | No | The endpoint of the destination instance. This parameter is required if the destination instance is a user-created database. |
| DestinationEndpoint.Port | String | No | The port on which the destination instance is listening. This parameter is required if the destination instance is a user-created database. |
| DestinationEndpoint.Datab aseName | String | No | The database name of the destination instance used for establishing a connection. This parameter is required if the destination instance is a PostgreSQL, or MongoDB database. |
| DestinationEndpoint.UserN ame | String | Yes | The username that is used to access the destination instance. |
| DestinationEndpoint.Passw ord | String | Yes | The password that is used to access the destination instance. |

| Parameter | Type | Requir ed | Description |
|---|---|---|---|
| MigrationMode.StructureIn tialization | Boole an | Yes | Specifies whether the data migration task performs schema migration. Valid values: true: yes false: no |
| MigrationMode.DataIntializ ation | Boole an | Yes | Specifies whether the data migration task performs full data migration. Valid values: true: yes false: no |
| MigrationMode.DataSynchr onization | Boole an | Yes | Specifies whether the data migration task performs incremental data synchronization. Valid values: true: yes false: no |
| MigrationObject | List | Yes | The objects that you want to migrate. For more information, see the MigrationObject parameter definition topic. |

###### 1.1.2.1.3 MigrationObject parameter definitions

The MigrationObject parameters are defined as JSON strings. Certain regular expressions can be used in the object configuration. The MigrationObject parameter definitions are as follows:

```
MigrationObject:{
        DBName:'The name of the database to be migrated',
        NewDBName:"The mapped name of the database to be migrated in the destination instan
ce"
        SchemaName:'The name of the schema to be migrated',
        NewSchemaName:'The mapped name of the schema to be migrated in the destination inst
ance',
        TableIncludes:[{
                   TableName: 'The name of the table to be migrated',
                NewTableName:'The mapped name of the table to be migrated in the destinatio
n instance',
                FilterCondition:'where condition',
                ColumnIncludes:[{
                        ColumnName:'The name of the column that needs to be migrated in the
table',
                        NewColumnName:'The mapped name of the column that needs to be migra
ted in the destination instance'
```

`}]`

```
                ColumnExcludes:[{
                        ColumnName:'The name of the column that does not need to be migrate
d in the table'
```

`}]` `}]`

```
        TableExcludes:[{                                — The table that does not need to b
e migrated
                TableName:'The name of the table that does not need to be migrated in the d
atabase'
```

`}]` SchemaName and NewSchemaName are applicable only to SQLServer. DBName and NewDBName are used to specify the names of other databases. If you only specify DBName but do not specify lower levels of objects, all objects in the database are migrated. If you specify DBName and some lower levels of objects, the objects that are not specified are not migrated by default. You can use the following regular expressions to define different object names: A period (.) matches any single character except '\r\n'. An asterisk (*) matches zero or more occurrences of a subexpression which occurs before. h.*llo matches strings such as hllo and heeeello. A question mark (?) matches zero or one occurrence of a subexpression which occurs before. h.? llo matches hllo and hello, but not haello. The [characters] character set matches any character included in the braces. For example, h[aello] matches hallo and hello. The [^characters] negative character set does not match any character included in the braces. For example, h[^ae]llo matches hcllo and hdllo, but not hallo or hello. The [character1-character2] character range matches any character included in the range from character1 to character2, such as [0-9] and [a-z].

###### 1.1.2.1.4 Response parameters

| Name | Type | Description |
|---|---|---|
| Common response parameters | - | The request ID. |

###### 1.1.2.1.5 Example

The following example shows how to use the Java SDK to configure a migration task.

```java
private static void configureMigrationJob(String MigrationJobId){
        String MigrationJobName="jiangliutest";
        /*Source Endpoint*/
        String SourceEndpoint_InstanceType="RDS";
        String SourceEndpoint_Region="cn-hangzhou";
        String SourceEndpoint_InstanceId="rm-xxxxxxxxxxxxxxxxx";
        String SourceEndpoint_UserName="*******";
        String SourceEndpoint_Password="*******";
        /*Destination Endpoint*/
        String DestinationEndpoint_InstanceType="RDS";
        String DestinationEndpoint_InstanceId="rm-xxxxxxxxxxxxxxxxx";
        String DestinationEndpoint_UserName="******";
        String DestinationEndpoint_Password="******";
        Boolean MigrationMode_StructureIntialization=true;
        Boolean MigrationMode_DataIntialization=true;
        Boolean MigrationMode_DataSynchronization=true;
        String MigrationObject="[{\"DBName\":\"jiangliutest\",\"NewDBName\":\"jiangliutest\
","
                + "\"TableIncludes\":[{\"TableName\":\"t1\",\"NewTableName\":\"t1\"}]}]";
        ConfigureMigrationJobRequest request = new ConfigureMigrationJobRequest();
        request.setMigrationJobId(MigrationJobId);
        request.setMigrationJobName(MigrationJobName);
        request.setSourceEndpointRegion(SourceEndpoint_Region);
        request.setSourceEndpointInstanceType(SourceEndpoint_InstanceType);
        request.setSourceEndpointInstanceID(SourceEndpoint_InstanceId);
        request.setSourceEndpointUserName(SourceEndpoint_UserName);
        request.setSourceEndpointPassword(SourceEndpoint_Password);
        request.setDestinationEndpointInstanceType(DestinationEndpoint_InstanceType);
        request.setDestinationEndpointInstanceID(DestinationEndpoint_InstanceId);
        request.setDestinationEndpointUserName(DestinationEndpoint_UserName);
        request.setDestinationEndpointPassword(DestinationEndpoint_Password);
        request.setMigrationModeStructureIntialization(MigrationMode_StructureIntialization
```

);

```java
        request.setMigrationModeDataIntialization(MigrationMode_DataIntialization);
        request.setMigrationModeDataSynchronization(MigrationMode_DataSynchronization);
        request.setMigrationObject(MigrationObject);
            ConfigureMigrationJobResponse response = client.getAcsResponse(request);
            System.out.println("Configure "+ MigrationJobId+ " Succeed");
        } catch (Exception e) {
            // TODO: handle exception
            System.out.println("Configure "+MigrationJobId + " Failed!") ;
            System.out.println(e.toString());
```

##### 1.1.2.2 CreateMigrationJob

###### 1.1.2.2.1 Overview

You can call this operation to purchase a database migration instance. After the purchase, you need to call the ConfigureMigrationJob operation to configure a migration task.

###### 1.1.2.2.2 Request parameters

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to CreateMigrationJob. |
| Region | String | Yes | The region of the migration instance. Valid values: cn-hangzhou: Alibaba Cloud in Hangzhou cn-shanghai: Alibaba Cloud in Shanghai cn-qingdao: Alibaba Cloud in Qingdao cn-beijing: Alibaba Cloud in Beijing cn-zhangbei: Alibaba Cloud in Zhangbei cn-shenzhen: Alibaba Cloud in Shenzhen cn-hongkong: Alibaba Cloud in Hong Kong us-west-1: Alibaba Cloud in Western US us-east-1: Alibaba Cloud in Eastern US ap-southeast-1: Alibaba Cloud in Singapore cn-hangzhou-finance-1: Finance Cloud in Hangzhou cn-qingdao-finance-1: Finance Cloud in Qingdao cn-shanghai-finance-1: Finance Cloud in Shanghai cn-shenzhen-finance-1: Finance Cloud in Shenzhen me-east-1: Alibaba Cloud in Dubai en-central-1: Alibaba Cloud in Frankfurt |
| MigrationJo bClass | String | Yes | The migration task type. Valid values: small, medium, and large. For the testing performance of each instance type, see Data migration types. |
| ClientToken | String | No | The token used to ensure the idempotence of the request. It can be any string. |
| OwnerID | String | No | If a RAM user is used to call this operation, the value of OwnerID is the UID of the Apsara Stack tenant account to which this RAM user belongs. |

###### 1.1.2.2.3 Response parameters

| Name | Type | Description |
|---|---|---|
| MigrationJobId | String | The migration task ID. |

###### 1.1.2.2.4 Examples

The following code provides an example of how to use the Java SDK to purchase a migration instance.

```java
private static String createMigrationJob(String region,String migrationJobClass) {
            CreateMigrationJobRequest request=new CreateMigrationJobRequest();
            request.setRegion("cn-hangzhou");
            request.setMigrationJobClass("small");
                CreateMigrationJobResponse response = client.getAcsResponse(request);
                String MigrationJobId = response.getMigrationJobId();
                System.out.println("Create Migration Job succeed. The Migration Job Id is "
+MigrationJobId);
                return MigrationJobId;
            } catch (Exception e) {
                // TODO: handle exception
                System.out.println("Create Migration Job failed!" +e.toString());
                return null;
```

##### 1.1.2.3 DeletetMigrationJob

###### 1.1.2.3.1 Overview

You can call this operation to delete a migration task regardless of its status. After a migration task is deleted, you cannot query or manage it through OpenAPI or the console.

###### 1.1.2.3.2 Request parameters

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DeletetMigrationJob. |
| MigrationJobId | String | Yes | The migration task ID. |

###### 1.1.2.3.3 Response parameters

| Name | Type | Description |
|---|---|---|
| Common response parameters | - | The request ID. |

###### 1.1.2.3.4 Examples

The following code provides an example of how to use the Java SDK to delete a migration task.

```java
private static void deleteMigrationJob(String MigrationJobId) {
        DeleteMigrationJobRequest request = new DeleteMigrationJobRequest();
        DeleteMigrationJobResponse response = new DeleteMigrationJobResponse();
        request.setMigrationJobId(MigrationJobId);
            response = client.getAcsResponse(request);
            System.out.println("Delete Migration Job "+MigrationJobId+" Succeed!") ;
        } catch (Exception e) {
            // TODO: handle exception
            System.out.println("Delete Migration Job "+MigrationJobId+" Failed!") ;
            System.out.println(e.toString());
```

##### 1.1.2.4 DescribeMigrationJobDetail

###### 1.1.2.4.1 Overview

When a migration task is in the Migrating, MigrationFailed, Suspending, or Finished status, you can call this operation to query data migration details, including the migration status and progress of each object.

###### 1.1.2.4.2 Request parameters

| Description | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeMigrationJobDe tail. |
| MigrationJobId | String | Yes | The migration task ID. |
| MigrationMode.Structur eInitialization | Boolean | No | The schema migration details. |
| MigrationMode.DataIniti alization | Boolean | No | The full data migration details. |
| MigrationMode.DataSyn chronization | Boolean | No | The incremental data migration details. |

| Description | Type | Required | Description |
|---|---|---|---|
| PageSize | Integer | No | The number of records on each page. Valid values: 30, 50, and 100. Default value: 30. This parameter is required when only one of these three parameters is set to true: MigrationMode.Struct ureInitialization, MigrationMode.DataIn itialization, and MigrationMode.DataS ynchronization. |
| PageNum | Integer | No | The page number. It must be greater than 0 and smaller than or equal to the maximum value of Integer. Default value: 1. This parameter is required when only one of these three parameters is set to true: MigrationMode.Struct ureInitialization, MigrationMode.DataIn itialization, and MigrationMode.DataS ynchronization. |

###### 1.1.2.4.3 Response parameters

| Name | Type | Description |
|---|---|---|
| StructureInitializationDetails | List | The schema migration details. For more information, see StructureInitializationDetail parameter definitions. |
| DataInitializationDetails | List | The full data migration details. For more information, see DataInitializationDetail parameter definitions. |

| D | ata Transmission Service |   | Developer Guide·Developer Guid | e |
|---|---|---|---|---|

| Name | Type | Description |
|---|---|---|
| DataSynchronizationDetails | List | The incremental data migration details. For more information, see DataSynchronizationDetail parameter definitions. |

###### 1.1.2.4.4 StructureInitializationDetail parameter definitions

definitions

| Name | Type | Description |
|---|---|---|
| ObjectName | String | The name of the object to be migrated. |
| ObjectType | String | The type of the object to be migrated. Valid values: Table, Constraint, Index, View, MaterializeView, Type, Synonym, Trigger, Function, Procedure, Package, Default, Rule, and Plan Guide. |
| SourceOwnerDBName | String | The name of the source database from which the object is to be migrated. |
| DestinationOwnerDBName | String | The schema of the destination database to which the object is to be migrated. |
| Status | String | The migration status of the object to be migrated. |
| ErrorMessage | String | The reason why the object failed to be migrated. |
| ObjectDefinition | String | The schema definition of the object to be migrated. |
| Constraints | List | Constraints in which the object to be migrated participates. Constraints are active only when the object to be migrated is a table. The list of constraints includes indexes and foreign keys. |

###### 1.1.2.4.5 DataInitializationDetail parameter definitions

| Name | Type | Description |
|---|---|---|
| TableName | String | The name of the table to be migrated. |
| SourceOwnerDBName | String | The name of the source database from which the table is to be migrated. |
| DestinationOwnerDBName | String | The name of the destination database to which the table is to be migrated. |
| Status | String | The migration status of the table. |
| ErrorMessage | String | The reason why the table failed to be migrated. |
| TotalRowNum | String | The total number of records to be migrated in the table. |
| FinishRowNum | String | The number of records that have been migrated in the table. |
| UsedTime | String | The time that has been spent on migrating the table. Unit: second. |

###### 1.1.2.4.6 DataSynchronizationDetail parameter definitions

definitions

| Name | Type | Description |
|---|---|---|
| TableName | String | The name of the table to be migrated. |
| SourceOwnerDBName | String | The name of the source database from which the table is to be migrated. |
| DestinationOwnerDBName | String | The name of the destination database to which the table is to be migrated. |
| Status | String | The migration status of the table to be migrated. |
| ErrorMessage | String | The reason why the table failed to be migrated. |

###### 1.1.2.4.7 Examples

The following code provides an example of how to use the Java SDK to query migration task details.

```java
private static void describeMigrationJobDetail(String MigrationJobId) {
        DescribeMigrationJobDetailRequest request = new DescribeMigrationJobDetailRequest()
```

;

```java
        request.setMigrationJobId(MigrationJobId);
        request.setMigrationModeStructureInitialization(true);
        request.setMigrationModeDataInitialization(true);
        request.setMigrationModeDataSynchronization(true);
            DescribeMigrationJobDetailResponse response = client.getAcsResponse(request);
            System.out.println("Get Migration Detail of Migration Job " +MigrationJobId+" S
ucceed!") ;
            List<StructureInitializationDetail> struInitDetails= response.getStructureIniti
alizationDetailList();
            System.out.println("Structure Initialization Detail:");
            for (int i = 0; i < struInitDetails.size(); i++) {
                String objectName=struInitDetails.get(i).getObjectName();
                String SrcDBName=struInitDetails.get(i).getSourceOwnerDBName();
                String DestDBName = struInitDetails.get(i).getDestinationOwnerDBName();
                String Status=struInitDetails.get(i).getStatus();
                String errorMsg=struInitDetails.get(i).getErrorMessage();
                System.out.println("ObjectName:"+objectName+"; SRCDBName:"+SrcDBName+"; DES
TDBName:"
                        +DestDBName+"; Status:"+Status+"errorMsg:"+errorMsg);
            List<DataInitializationDetail> dataInitDetails = response.getDataInitialization
DetailList();
            System.out.println("Data Initialization Detail:");
            for (int i = 0; i < dataInitDetails.size(); i++) {
                String tblName=dataInitDetails.get(i).getTableName();
                String tbl_srcDBName=dataInitDetails.get(i).getSourceOwnerDBName();
                String tbl_destDBName=dataInitDetails.get(i).getDestinationOwnerDBName();
                String dataInitStatus=dataInitDetails.get(i).getStatus();
                String dataInitSumRows=dataInitDetails.get(i).getTotalRowNum();
                String dataInitFinishRows=dataInitDetails.get(i).getFinishRowNum();
                String dataUsedTime=dataInitDetails.get(i).getMigrationTime();
                String dataInitErrMSG = dataInitDetails.get(i).getErrorMessage();
                System.out.println("TableName:"+tblName+"; SRCDBName:"+tbl_srcDBName
                        +"; DESTDBName:"+tbl_destDBName+"; SumRows:"+dataInitSumRows+"; Fin
ishRows"
                        +"; UsedTime:"+dataUsedTime+"; ErrorMSG:"+dataInitErrMSG);
            List<DataSynchronizationDetail> dataSyncDetails = response.getDataSynchronizati
onDetailList();
            System.out.println("Data Synchronization Detail");
            for (int i = 0; i < dataSyncDetails.size(); i++) {
                String dataSyncTblName=dataSyncDetails.get(i).getTableName();
                String dataSyncSRCDBName=dataSyncDetails.get(i).getSourceOwnerDBName();
                String dataSyncDESTDBName = dataSyncDetails.get(i).getDestinationOwnerDBNam
e(); StringdataSyncStatus=dataSyncDetailsget(i)getStatus();
```

```java
                String dataSyncStatus = dataSyncDetails.get(i).getStatus();
                String dataSyncErrMsg = dataSyncDetails.get(i).getErrorMessage();
                System.out.println("TableName:"+dataSyncTblName+"; SRCDBName:"+dataSyncSRCD
BName
                        +"; DESTDBName:"+dataSyncDESTDBName+"; Status:"+dataSyncStatus+"; E
rrorMSG:"+dataSyncErrMsg);
        } catch (Exception e) {
            // TODO: handle exception
            System.out.println("Get Migration Detail of Migration Job " +MigrationJobId+" F
ailed!") ;
            System.out.println(e.toString());
```

##### 1.1.2.5 DescribeMigrationJobStatus

###### 1.1.2.5.1 Overview

You can call this operation to query the data migration status regardless of the migration task status. You can query the overall migration status of the task, the migration status of each migration stage (schema migration, full data migration, and incremental data migration), and the precheck status.

###### 1.1.2.5.2 Request parameters

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeMigrationJobSta tus. |
| MigrationJobId | String | Yes | The migration task ID. |

###### 1.1.2.5.3 Response parameters

| Name | Type | Description |
|---|---|---|
| MigrationJobId | String | The ID of the migration task. |
| MigrationJobName | String | The name of the migration task. |
| PayType | String | The billing method. |
| MigrationJobClass | String | The type of the migration instance. |

| Name | Type | Description |
|---|---|---|
| SourceEndpoint | Endpoint | The IP address for connecting to the source instance. For more information, see the parameter definition in section 1.2.5.4. |
| DestinationEndpoint | Endpoint | The IP address for connecting to the destination instance. For more information, see the parameter definition in section 1.2.5.4. |
| MigrationMode | MigrationMode | The migration type. For more information, see the parameter definition in section 1.2.5.5. |
| MigrationObjects | List | The objects to be migrated. |
| MigrationJobStatus | String | The status of the migration task. Valid values: NotStarted: The migration task is not started. Prechecking: The migration task is being prechecked. PrecheckFailed: The precheck fails. Migrating: Data is being migrated. Suspending: The migration task is suspended. MigrationFailed: The migration task fails. Finished: The migration task is complete. |
| PrecheckStatus | PrecheckStatus | The precheck status including the check progress and the specific state. For more information, see the parameter definition in section 1.2.5.6. |
| StructureInitializationStatus | StructureInitializationStatus | The status of schema migration including the migration progress and the specific state. For more information, see the parameter definition in section 1.2.5.8. |
| DataInitializationStatus | DataInitializationStatus | The status of full data migration including the migration progress and the specific state. For more information, see the parameter definition in section 1.2.5.9. |

| eveloper Guide·Developer Guide |   | Data Transmission Servic |
|---|---|---|
| Name | Type | Description |
| DataSynchronizationStatus | DataSynchronizationStatus | The status of incremental data migration including the migration progress and the specific state. For more information, see the parameter definition in section 1.2.5.10. |

###### 1.1.2.5.4 Endpoint parameter definitions

| Name | Type | Description |
|---|---|---|
| InstanceType | String | The instance type. |
| Region | String | The region of the source instance. |
| InstanceId | String | The instance ID. |
| EngineName | String | The database type. |
| IP | String | The database connection address. |
| Port | String | The listening port of the database. |
| UserName | String | The username to access the database. |
| OracleSID | String | The Oracle SID. |
| DatabaseName | String | The database name. |

###### 1.1.2.5.5 MigrationMode parameter definitions

| Name | Type | Description |
|---|---|---|
| StructureInitialization | String | Indicates whether to perform schema migration. |
| DataInitialization | String | Indicates whether to perform full data migration. |
| DataSynchronization | String | Indicates whether to perform incremental data migration. |

###### 1.1.2.5.6 PrecheckStatus parameter definitions

| Name | Type | Description |
|---|---|---|
| Status | String | The precheck status. |
| Percent | String | The precheck progress. Unit: %. |
| Detail | List | The check details of each precheck item. For more information, see CheckItem parameter definitions. |

###### 1.1.2.5.7 CheckItem parameter definitions

| Name | Type | Description |
|---|---|---|
| ItemName | String | The check item name. |
| CheckStatus | String | The check status. Valid values: NotStarted Checking Failed Finished |
| ErrorMessage | String | The cause of the error. |
| RepairMethod | String | The repair method. |

###### 1.1.2.5.8 StructureInitializationStatus parameter definitions

definitions

| Name | Type | Description |
|---|---|---|
| Status | String | The migration status. Valid values: NotStarted Migrating Failed Finished |
| ErrorMessage | String | The cause of the migration error. |
| Percent | String | The migration progress. Unit: %. |
| Progress | String | The number of tables that have been migrated. |

###### 1.1.2.5.9 DataInitializationStatus parameter definitions

| Name | Type | Description |
|---|---|---|
| Status | String | The migration status. Valid values: NotStarted Migrating Failed Finished |
| ErrorMessage | String | The cause of the migration error. |
| Percent | String | The migration progress. Unit: %. |
| Progress | String | The number of tables that have been migrated. |

###### 1.1.2.5.10 DataSynchronizationStatus parameter definitions

definitions

| Name | Type | Description |
|---|---|---|
| Status | String | The migration status. Valid values: NotStarted Migrating Failed Finished |
| ErrorMessage | String | The cause of the migration error. |
| Percent | String | The migration progress. Unit: %. |
| Delay | String | The migration latency. |

###### 1.1.2.5.11 Examples

The following code provides an example of how to use the Java SDK to query the status of a migration task.

```java
private static void describeMigrationJobStatus(String MigrationJobId){
        DescribeMigrationJobStatusRequest request = new DescribeMigrationJobStatusRequest()
```

;

```
        request.setMigrationJobId(MigrationJobId);
            DescribeMigrationJobStatusResponse response = client.getAcsResponse(request);
```

```java
            System.out.println("Get Status of Migration Job "+MigrationJobId+" Succeed!") ;
            String JobStatus=response.getMigrationJobStatus();
            /*Get the basic information of the migration job*/
            System.out.println("MigrationJobName:"+response.getMigrationJobName()
                    +"MigrationJobId:"+response.getMigrationJobId()
                    +"MigrationObjects:"+response.getMigrationObject()
                    +"; MigrationMode.StructureInitialization:" + response.getMigrationMode
().getStructureInitialization()
                    +"; MigrationMode.DataInitialization:"+response.getMigrationMode().getD
ataInitialization()
                    +"; MigrationMode.DataSynchronization:"+response.getMigrationMode().get
DataSynchronization()
                    +"; MigrationJobStatus:"+response.getMigrationJobStatus());
            /*Get the source endpoint of the migration job*/
            System.out.println("SourceEndpoint.InstanceType:"+response.getSourceEndpoint().
getInstanceType()
                    +"; SourceEndpoint.InstanceId:"+response.getSourceEndpoint().getInstanc
eId()
                    +"; SourceEndpoint.EngineName:"+response.getSourceEndpoint().getEngineN
ame()
                    +"; SourceEndpoint.IP:"+response.getSourceEndpoint().getIP()
                    +"; SourceEndpoint.Port"+response.getSourceEndpoint().getPort()
                    +"; SourceEndpoint.UserName:"+response.getSourceEndpoint().getUserName(
```

`)`

```java
                    +"; SourceEndpoint.DatabaseName:"+response.getSourceEndpoint().getDatab
aseName()
                    +"; SourceEndpoint.OracleSID:"+response.getSourceEndpoint().getOracleSI
D());
            /*Get the destination endpoint of the migration job*/
            System.out.println("DestinationEnpoint.InstanceType:"+response.getDestinationEn
dpoint().getInstanceType()
                    +"DestinationEndpoint.InstanceId:"+response.getDestinationEndpoint().ge
tInstanceId()
                    +"DestinationEndpint.EngineName:"+response.getDestinationEndpoint().get
EngineName()
                    +"DestinationEndpoint.IP:"+response.getDestinationEndpoint().getIP()
                    +"DestinationEndpoint:Port:"+response.getDestinationEndpoint().getPort(
```

`)`

```java
                    +"DestinationEndpoint.UserName:"+response.getDestinationEndpoint().getU
serName()
                    +"DestinationEndpoint.DatabaseName"+response.getDestinationEndpoint().g
etDatabaseName()
                    +"DestinationEndpoint.OracleSID:"+response.getDestinationEndpoint().get
OracleSID());
            /*Get Status of Precheck*/
                com.aliyuncs.dts.model.v20160801. DescribeMigrationJobStatusResponse.Preche
ckStatus precheckStatus = response.getPrecheckStatus();
                System.out.println("Get  Precheck Status of Migration Job "+MigrationJobId
+" Succeed!") ;
                System.out.println("Precheck Status:"+ precheckStatus.getStatus()+";Prechec
k Percent:"+precheckStatus.getPercent());
                List<CheckItem> checkItems = precheckStatus.getDetail();
                for (int i = 0; i < checkItems.size(); i++) {
```

```java
                    String checkItem=checkItems.get(i).getItemName();
                    String checkStatus = checkItems.get(i).getCheckStatus();
                    String repairMethod = checkItems.get(i).getRepairMethod();
                    String errorMessage =checkItems.get(i).getErrorMessage();
                    System.out.println("CheckItem:"+checkItem+"; CheckStatus:"+checkStatus
                            +"errorMessage:"+errorMessage+"; repairMethod:"+repairMethod);
            } catch (Exception e) {
                // TODO: handle exception
                System.out.println("Get  Precheck Status of Migration Job "+MigrationJobId
+" Failed!") ;
                System.out.println(e.toString());
            /*Get Status of Structure Migration*/
                StructureInitializationStatus strucInitStatus = new StructureInitialization
Status();
                strucInitStatus = response.getStructureInitializationStatus();
                String status = strucInitStatus.getStatus();
                String percent = strucInitStatus.getPercent();
                String progress = strucInitStatus.getProgress();
                String errorMsg = strucInitStatus.getErrorMessage();
                System.out.println("Get Structure Initialization Status of Migration Job "
+MigrationJobId+" Succeed!") ;
                System.out.println("Status:"+status+";percent:"+percent+"; progress:"+progr
ess+"; errorMsg:"+errorMsg);
            } catch (Exception e) {
                // TODO: handle exception
                System.out.println("Get Structure Initialization Status of Migration Job "
+MigrationJobId+" Failed!") ;
                System.out.println(e.toString());
            /*Get Status of Data Migration*/
                DataInitializationStatus dataInitStatus = new DataInitializationStatus();
                dataInitStatus = response.getDataInitializationStatus();
                String datainitstatus=dataInitStatus.getStatus();
                String datainitpercent = dataInitStatus.getPercent();
                String datainitprogress = dataInitStatus.getProgress();
                String datainiterrormsg = dataInitStatus.getErrorMessage();
                System.out.println("Get Data Initialization Status of Migration Job " +Migr
ationJobId+" Succeed!") ;
                System.out.println("Status:"+datainitstatus+";percent:"+datainitpercent+";
progress:"+datainitprogress+"; errorMsg:"+datainiterrormsg);
             } catch (Exception e) {
                // TODO: handle exception
                 System.out.println("Get Data Initialization Status of Migration Job " +Mig
rationJobId+" Failed!") ;
                 System.out.println(e.toString());
            /*Get Status of Data Synchronization*/
                DataSynchronizationStatus dataSyncStatus = new DataSynchronizationStatus();
                dataSyncStatus = response.getDataSynchronizationStatus();
```

```java
                String datasynstatus=dataSyncStatus.getStatus();
                String datasyncpercent=dataSyncStatus.getPercent();
                String datasyncdelay=dataSyncStatus.getDelay();
                String datasyncerrormsg=dataSyncStatus.getErrorMessage();
                System.out.println("Get Data Synchronization Status of Migration Job " +Mig
rationJobId+" Succeed!") ;
                System.out.println("Status:"+datasynstatus+";percent:"+datasyncpercent+"; d
elay:"+datasyncdelay+"; errorMsg:"+datasyncerrormsg);
            } catch (Exception e) {
                // TODO: handle exception
                System.out.println("Get Data Synchronization Status of Migration Job " +Mig
rationJobId+" Failed!") ;
                System.out.println(e.toString());
        } catch (Exception e) {
            // TODO: handle exception
            System.out.println("Get Status of Migration Job "+MigrationJobId+" Failed");
            System.out.println(e.toString());
```

##### 1.1.2.6 StartMigrationJob

###### 1.1.2.6.1 Overview

You can call this operation to start a migration task. When a migration task is in the NotStarted or MigrationFailed status, you can call this operation to start or restart it.

###### 1.1.2.6.2 Request parameters

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to StartMigrationJob. |
| MigrationJobId | String | Yes | The migration task ID. |

###### 1.1.2.6.3 Response parameters

| Name | Type | Description |
|---|---|---|
| <Common response parameters> | - | The request ID. |

###### 1.1.2.6.4 Examples

The following code provides an example of how to use the Java SDK to start a migration task.

```java
private static void startMigrationJob(String MigrationJobId){
        StartMigrationJobRequest request = new StartMigrationJobRequest();
        request.setMigrationJobId(MigrationJobId);
            StartMigrationJobResponse response = client.getAcsResponse(request);
            System.out.println("Start "+MigrationJobId+" Succeed");
        } catch (Exception e) {
            // TODO: handle exception
            System.out.println("Start "+MigrationJobId + " Failed");
            System.out.println(e.toString());
```

##### 1.1.2.7 StopMigrationJob

###### 1.1.2.7.1 Overview

You can call this operation to stop a migration task when it is in the Migrat ing status. Not e You cannot start a task that has been stopped.

###### 1.1.2.7.2 Request parameters

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to StopMigrationJob. |
| MigrationJobId | String | Yes | The migration task ID. |

###### 1.1.2.7.3 Response parameters

| Name | Type | Description |
|---|---|---|
| <Common response parameters> | - | The request ID. |

###### 1.1.2.7.4 Examples

The following code provides an example of how to use the Java SDK to stop a migration task.

```java
private static void stopMigrationJob(String MigrationJobId) {
        StopMigrationJobRequest request = new StopMigrationJobRequest();
            request.setMigrationJobId(MigrationJobId);
            StopMigrationJobResponse response = client.getAcsResponse(request);
            System.out.println("Stop Migration Job "+MigrationJobId+" Succeed!") ;
        } catch (Exception e) {
            // TODO: handle exception
            System.out.println("Stop Migration Job "+MigrationJobId+" Failed!") ;
            System.out.println(e.toString());
```

##### 1.1.2.8 SuspendMigrationJob

###### 1.1.2.8.1 Overview

You can call this operation to suspend a migration task when it is in the Migrating status. Note that if a task has been suspended for more than 6 hours after it enters the incremental data migration stage, you may fail to restart it through the StartMigrationJob operation.

###### 1.1.2.8.2 Request parameters

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to SuspendMigrationJob. |
| MigrationJobId | String | Yes | The migration task ID. |

###### 1.1.2.8.3 Response parameters

| Name | Type | Description |
|---|---|---|
| <Common response parameters> | - | The request ID. |

###### 1.1.2.8.4 Examples

The following code provides an example of how to use the Java SDK to suspend a migration task.

```java
private static void suspendMigrationJob(String MigrationJobId){
        SuspendMigrationJobRequest request = new SuspendMigrationJobRequest();
        request.setMigrationJobId(MigrationJobId);
            SuspendMigrationJobResponse response = client.getAcsResponse(request);
            System.out.println("Suspend "+ MigrationJobId + " Succeed");
        } catch (Exception e) {
            // TODO: handle exception
            System.out.println("Suspend "+MigrationJobId +"Failed");
            System.out.println(e.toString());
```

#### 1.1.3 Data subscription APIs

##### 1.1.3.1 ConfigureSubscriptionInstance

###### 1.1.3.1.1 Overview

You can call this operation to modify the configurations of a change tracking task, such as instance connection details and objects for change tracking. You can call this operation multiple times to modify the configurations of a task before the task is started. Only the changes of RDS for MySQL instances can be tracked.

###### 1.1.3.1.2 Request parameters

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to ConfigureSubscriptionInsta nce. |
| SubscriptionInstanceId | String | Yes | The ID of the subscription channel to be configured. |
| SubscriptionInstanceNa me | String | No | The name of a subscription channel that can distinguish it from other subscription channels. |
| SourceEndpoint.Instance Type | String | No | The type of the subscription instance. Valid value: RDS. Default value: RDS. |
| SourceEndpoint.Instance Id | String | Yes | The RDS instance ID. |

| Data Transmission Service |   | Dev | eloper Guide·Developer Guid |
|---|---|---|---|

| Name | Type | Required | Description |
|---|---|---|---|
| SubscriptionDataType.D DL | Boolean | Yes | Indicates whether to subscribe to schema updates made through DDL. Valid values: true (yes) and false (no). Default value: true. |
| SubscriptionDataType.D ML | Boolean | Yes | Indicates whether to subscribe to data updates made through DML. Valid values: true (yes) and false (no). Default value: true. |
| SubscriptionObjects | List | Yes | The listening port of the source instance. This parameter is required when the source instance is a user-created database. For more information, see SubscriptionObject parameter definitions. |

###### 1.1.3.1.3 SubscriptionObject parameter definitions

The SubscriptionObject parameters are defined as JSON strings. Certain regular expressions can be used in the object configuration. The SubscriptionObject parameter definitions are as follows:

```
SubscriptionObject:{
        DBName:"The name of the database to be subscribed",
        TableIncludes:[{
                   TableName: "The name of the table to be migrated"
```

`}]` SubscriptionObject indicates the whitelist of objects to be subscribed. You can use the following regular expressions to define different object names: A period (.) matches any single character except '\r\n'. An asterisk (*) matches zero or more occurrences of a subexpression which occurs before. h.*llo matches strings such as hllo and heeeello. A question mark (?) matches zero or one occurrence of a subexpression which occurs before. h.? llo matches hllo and hello, but not haello. The [characters] character set matches any character included in the braces. For example, h[aello] matches hallo and hello. The [^characters] negative character set does not match any character included in the braces. For example, h[^ae]llo matches hcllo and hdllo, but not hallo or hello. The [character1-character2] character range matches any character included in the range from character1 to character2, such as [0-9] and [a-z].

###### 1.1.3.1.4 Response parameters

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID of the request. |
| Success | String | Indicates whether the request is successful. Valid values: true and false. |
| ErrCode | String | The error code. |
| ErrMessage | String | The detailed error message. |

###### 1.1.3.1.5 Example

This topic describes how to use the Java SDK to configure a migration task.

```java
private static void configureSbeJob(String MigrationJobId){
        String MigrationJobName="jiangliutest";
        /*Source Endpoint*/
        String SourceEndpoint_InstanceId="rm-xxxxxxxxxxxxxxxxx";
        String SourceEndpoint_InstanceType="rds";
        Boolean MigrationMode_SubscriptionDataTypeDML=true;
        Boolean MigrationMode_SubscriptionDataTypeDDL=true;
        String MigrationObjects="[{\"DBName\":\"jiangliutest\","
                + "\"TableIncludes\":[{\"TableName\":\"t1\"}]}]";
        ConfigureSubscriptionInstanceRequest request = new ConfigureSubscriptionInstanceReq
uest();
        request.setMigrationJobId(MigrationJobId);
        request.setMigrationJobName(MigrationJobName);
        request.setSubscriptionInstanceId(jobId);
        request.setSubscriptionDataTypeDDL(MigrationMode_SubscriptionDataTypeDDL);
        request.setSubscriptionDataTypeDML(MigrationMode_SubscriptionDataTypeDML);
        request.setSourceEndpointInstanceType(SourceEndpoint_InstanceType);
        request.setSourceEndpointInstanceID(SourceEndpoint_InstanceId);
        request.setMigrationObject(MigrationObjects);
            ConfigureSubscriptionInstanceResponse response = client.getAcsResponse(request)
```

;

```java
            System.out.println("Configure "+ MigrationJobId+ " Succeed");
        } catch (Exception e) {
            // TODO: handle exception
            System.out.println("Configure "+MigrationJobId + " Failed!") ;
            System.out.println(e.toString());
```

##### 1.1.3.2 CreateSubscriptionInstance

###### 1.1.3.2.1 Overview

You can call this operation to purchase a database incremental subscription instance. After the purchase, you need to call the ConfigureSubscriptionInstance operation to configure a subscription task.

###### 1.1.3.2.2 Request parameters

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to CreateSubscriptionInstance. |
| Region | String | Yes | The region of the subscription instance. Valid values: cn-hangzhou: Alibaba Cloud in Hangzhou cn-shanghai: Alibaba Cloud in Shanghai cn-qingdao: Alibaba Cloud in Qingdao cn-beijing: Alibaba Cloud in Beijing cn-zhangbei: Alibaba Cloud in Zhangbei cn-shenzhen: Alibaba Cloud in Shenzhen cn-hongkong: Alibaba Cloud in Hong Kong us-west-1: Alibaba Cloud in Western US us-east-1: Alibaba Cloud in Eastern US ap-southeast-1: Alibaba Cloud in Singapore cn-hangzhou-finance-1: Finance Cloud in Hangzhou cn-qingdao-finance-1: Finance Cloud in Qingdao cn-shanghai-finance-1: Finance Cloud in Shanghai cn-shenzhen-finance-1: Finance Cloud in Shenzhen me-east-1: Alibaba Cloud in Dubai en-central-1: Alibaba Cloud in Frankfurt |
| ClientToken | String | No | The token used to ensure the idempotence of the request. It can be any string. |
| OwnerID | String | No | If a RAM user is used to call this operation, the value of OwnerID is the UID of the Apsara Stack tenant account to which this RAM user belongs. |

###### 1.1.3.2.3 Response parameters

| Name | Type | Description |
|---|---|---|
| SubscriptionInstanceId | String | The subscription channel ID. This is the GUID of a subscription channel. |

###### 1.1.3.2.4 Examples

The following code provides an example of how to use the Java SDK to purchase a migration instance.

```java
private String create() throws Exception {
        CreateSubscriptionInstanceRequest request = new CreateSubscriptionInstanceRequest()
```

;

```java
        request.setRegion("cn-hangzhou");
        request.setPayType("postpaid");
        CreateSubscriptionInstanceResponse response = client.getAcsResponse(request);
        if(response == null){
            throw new Exception("create fail");
        System.out.println("CreateSubscriptionInstanceRequest, result :"+response.getSubscr
iptionInstanceId());
        return response.getSubscriptionInstanceId();
```

##### 1.1.3.3 DeleteSubscriptionInstance

###### 1.1.3.3.1 Overview

You can call this operation to delete a subscription channel regardless of its status. After a subscription task is deleted, you cannot query or manage it through OpenAPI or the console.

###### 1.1.3.3.2 Request parameters

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DeleteSubscriptionInsta nce. |
| SubscriptionInstanceId | String | Yes | The ID of the subscription channel to be released. |

###### 1.1.3.3.3 Response parameters

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID of the request. |
| Success | String | Indicates whether the request is successful. Valid values: true and false. |
| ErrCode | String | The error code. |
| ErrMessage | String | The detailed error message. |

###### 1.1.3.3.4 Examples

The following code provides an example of how to use the Java SDK to delete a subscription task.

```java
private static void deleteMigrationJob(String MigrationJobId) {
        DeleteMigrationJobRequest request = new DeleteMigrationJobRequest();
        DeleteMigrationJobResponse response = new DeleteMigrationJobResponse();
        request.setMigrationJobId(MigrationJobId);
            response = client.getAcsResponse(request);
            System.out.println("Delete Migration Job "+MigrationJobId+" Succeed!") ;
        } catch (Exception e) {
            // TODO: handle exception
            System.out.println("Delete Migration Job "+MigrationJobId+" Failed!") ;
            System.out.println(e.toString());
```

##### 1.1.3.4 DescribeSubscriptionInstances

###### 1.1.3.4.1 Overview

You can call this operation to query the list of subscription channels that your Apsara Stack tenant account has access to. Data subscription channels in any status are returned.

###### 1.1.3.4.2 Request parameters

| Description | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeSubscriptionInst ances. |

| Description | Type | Required | Description |
|---|---|---|---|
| PageSize | Integer | No | The number of records on each page. Valid values: 30, 50, and 100. Default value: 30. |
| PageNum | Integer | No | The page number. It must be greater than 0 and smaller than or equal to the maximum value of Integer. Default value: 1. |

###### 1.1.3.4.3 Response parameters

| Name | Type | Description |
|---|---|---|
| SubscriptionInstances | List | The subscription channel details. For more information, see DescribeSubscriptionInstanceStat us. |
| PageNumber | Integer | The page number. |
| TotalRecrodCount | Integer | The total number of records. |
| PageRecordCount | Integer | The number of records on the page. |

###### 1.1.3.4.4 Examples

The following code provides an example of how to use the Java SDK to query the list of subscription instances.

```java
 public List<SubscriptionInstance> list(String jobName) throws ClientException {
        DescribeSubscriptionInstancesRequest request = new DescribeSubscriptionInstancesReq
uest();
        request.setPageNum(1);
        request.setPageSize(20);
        if(jobName! =null) {
            request.setSubscriptionInstanceName(jobName);
        DescribeSubscriptionInstancesResponse response = client.getAcsResponse(request);
        System.out.println("page no: "+response.getPageNumber());
        System.out.println("page size: "+response.getPageRecordCount());
        System.out.println("size: "+ response.getSubscriptionInstances().size());
        return response.getSubscriptionInstances();
```

##### 1.1.3.5 DescribeSubscriptionInstanceStatus

###### 1.1.3.5.1 Overview

You can call this operation to query the status of a subscription channel regardless of the subscription task status. You can query the channel configuration information, channel status, and downstream consumption status.

###### 1.1.3.5.2 Request parameters

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeSubscriptionInst anceStatus. |
| SubscriptionInstanceId | String | Yes | The subscription channel ID. |

###### 1.1.3.5.3 Response parameters

| Name | Type | Description |
|---|---|---|
| SubscriptionInstanceId | String | The subscription channel ID. |
| SubscriptionInstanceName | String | The subscription channel name. |
| PayType | String | The billing method. |
| SourceEndpoint | Endpoint | The endpoint to access the source instance specified in the subscription task. For more information, see Endpoint parameter definitions. |
| SubscriptionDataType.DDL | Boolean | Indicates whether the data to be subscribed contains schema updates made through DDL. Valid values: true (yes) and false (no). |
| SubscriptionDataType.DML | Boolean | Indicates whether the data to be subscribed contains data updates made through DML. Valid values: true (yes) and false (no). |
| SubscriptionObjects | List | The objects to be subscribed, listed in a SubscriptionObject array. For more information, see SubscriptionObject parameter definitions. |

| Name | Type | Description |
|---|---|---|
| Status | String | The subscription channel status. Valid values: NotStarted, Prechecking, PrecheckFailed, Starting, Normal, and Abnormal. |
| ErrorMessage | String | The cause of the channel error. |
| ConsumptionCheckpoint | String | The consumption checkpoint of the downstream SDK connected to the subscription channel. The date format follows the ISO8601 standard. It is in the UTC format of YYYY-MM-DDThh:mm:ssZ. For example, 2017- 08-15T12:00:00Z (or 20:00:00, August 15, 2017, China Standard Time). |
| BeginTimestamp | String | The start time of the timestamp range of the data stored in the subscription channel. The date format follows the ISO8601 standard. It is in the UTC format of YYYY-MM- DDThh:mm:ssZ. For example, 2017-08- 15T12:00:00Z (or 20:00:00, August 15, 2017, China Standard Time). |
| EndTimestamp | String | The end time of the timestamp range of the data stored in the subscription channel. The date format follows the ISO8601 standard. It is in the UTC format of YYYY-MM- DDThh:mm:ssZ. For example, 2017-08- 15T12:00:00Z (or 20:00:00, August 15, 2017, China Standard Time). |
| ConsumptionClient | String | The downstream client information, in the following format: IP address of the downstream client:Random ID generated by DTS. |

###### 1.1.3.5.4 Endpoint parameter definitions

| Name | Type | Description |
|---|---|---|
| InstanceType | String | The instance type. |
| Region | String | The region of the source instance. |
| InstanceId | String | The instance ID. |
| EngineName | String | The database type. |
| IP | String | The connection address of the database. |

| Data Transmission Service |   | Developer Guide·Developer Guid |
|---|---|---|

| Name | Type | Description |
|---|---|---|
| Port | String | The listening port of the database. |
| UserName | String | The username to access the database. |
| OracleSID | String | The Oracle SID. |
| DatabaseName | String | The database name. |

###### 1.1.3.5.5 SubscriptionObject parameter definitions

| Name | Type | Description |
|---|---|---|
| databaseName | String | The name of the database from which the list of objects are to be subscribed. |
| tableList | List | The names of the tables to be subscribed. |
| wholeDatabase | Boolean | Indicates whether to subscribe to the whole database. |

###### 1.1.3.5.6 Examples

The following code provides an example of how to use the Java SDK to query the status of a subscription channel.

```java
 private void describe(String jobId) throws ClientException {
        DescribeSubscriptionInstanceStatusRequest request = new DescribeSubscriptionInstanc
eStatusRequest();
        request.setSubscriptionInstanceId(jobId);
        DescribeSubscriptionInstanceStatusResponse response = client.getAcsResponse(
            request);
        System.out.println(response.getStatus());
        System.out.println(response.getBeginTimestamp());
        System.out.println(response.getEndTimestamp());
        System.out.println(response.getConsumptionCheckpoint());
```

##### 1.1.3.6 ModifyComsumptionTimestamp

###### 1.1.3.6.1 Overview

You can call this operation to modify the consumption checkpoint only when the subscription channel is in the Normal status and the consumption client is stopped.

###### 1.1.3.6.2 Request parameters

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to ModifyComsumptionTimestamp. |
| SubscriptionInsta nceId | String | Yes | The ID of the subscription channel for which the consumption checkpoint needs to be modified. |
| ConsumptionTim estamp | String | Yes | The timestamp of the modified consumption checkpoint. The timestamp format follows the ISO8601 standard. The UTC time is used. Format: yyyy-MM-ddTHH:mm:ssZ. For example, 2013-08-15T12:00:00Z indicates 20:00:00 on Tuesday, August 15, 2013 Beijing Time). |

###### 1.1.3.6.3 Response parameters

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID of the request. |
| Success | String | Indicates whether the request is successful. Valid values: true and false. |
| ErrCode | String | The error code. |
| ErrMessage | String | The detailed error message. |

###### 1.1.3.6.4 Examples

The following code provides an example of how to use the Java SDK to modify the consumption checkpoint.

```java
private void modifyTimestamp(String jobId,String ts) throws ClientException {
        ModifyConsumptionTimestampRequest request = new ModifyConsumptionTimestampRequest()
```

;

```java
        request.setSubscriptionInstanceId(jobId);
        //ts
        request.setConsumptionTimestamp(ts);
        ModifyConsumptionTimestampResponse response = client.getAcsResponse(request);
        System.out.println("modify timestamp ,result:" + response.getSuccess());
```

##### 1.1.3.7 ModifySubscriptionObject

###### 1.1.3.7.1 Overview

When the subscription channel is in the NotStarted, Failed, Normal or Abnormal status, you can call this operation to modify the list of objects to be subscribed. If the subscription channel is in the Normal status, you call this operation to modify the list of objects to be subscribed. After that, DTS calls the StartSubscriptionInstance operation directly to start the subscription channel. If the subscription channel is in the NotStarted, Failed, or Abnormal status, you call this operation to modify the list of objects to be subscribed. After that, you need to call the StartSubscriptionInstance operation to start the subscription channel if you want to.

###### 1.1.3.7.2 Request parameters

| Description | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to ModifySubscriptionObject. |
| SubscriptionInstanceI d | String | Yes | The ID of the subscription channel for the list of objects to be modified. |
| SubscriptionObjects | List | Yes | The new list of objects to be subscribed after the modification. For more information, see SubscriptionObject parameter definitions. |

###### 1.1.3.7.3 SubscriptionObject parameter definitions

The SubscriptionObject parameters are defined as JSON strings. Certain regular expressions can be used in the object configuration. The SubscriptionObject parameter definitions are as follows:

```
SubscriptionObject:{
        DBName:"The name of the database to be subscribed",
        TableIncludes:[{
                   TableName: "The name of the table to be migrated"
```

`}]` SubscriptionObject indicates the whitelist of objects to be subscribed. You can use the following regular expressions to define different object names: A period (.) matches any single character except '\r\n'. An asterisk (*) matches zero or more occurrences of a subexpression which occurs before. h.*llo matches strings such as hllo and heeeello. A question mark (?) matches zero or one occurrence of a subexpression which occurs before. h.? llo matches hllo and hello, but not haello. The [characters] character set matches any character included in the braces. For example, h[aello] matches hallo and hello. The [^characters] negative character set does not match any character included in the braces. For example, h[^ae]llo matches hcllo and hdllo, but not hallo or hello. The [character1-character2] character range matches any character included in the range from character1 to character2, such as [0-9] and [a-z].

###### 1.1.3.7.4 Response parameters

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID of the request. |
| Success | String | Indicates whether the request is successful. Valid values: true and false. |
| ErrCode | String | The error code. |
| ErrMessage | String | The detailed error message. |

###### 1.1.3.7.5 Examples

The following code provides an example of how to use the Java SDK to modify the list of objects to be subscribed.

```java
private void modifyObject(String jobId) throws ClientException {
        ModifySubscriptionObjectRequest request = new ModifySubscriptionObjectRequest();
        request.setSubscriptionInstanceId(jobId);
        String sbeObject = "[{\n"
                           + "\"DBName\":\"miyuntest\","
                           + "\"TableIncludes\":["
                           + "{\"TableName\":\"t1\"},"
                           + "{\"TableName\":\"t2\"},"
                           + "{\"TableName\":\"t3\"}"
                           + "]"
                           + "}]";
        request.setSubscriptionObject(sbeObject);
        ModifySubscriptionObjectResponse response = client.getAcsResponse(request);
        System.out.println(response.getSuccess());
```

##### 1.1.3.8 StartSubscriptionInstance

###### 1.1.3.8.1 Overview

You can call this operation to start a subscription channel only when the channel is in the NotStarted, Failed, or Suspending status.

###### 1.1.3.8.2 Request parameters

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to StartSubscriptionInstanc e. |
| SubscriptionInstanceId | String | Yes | The ID of the subscription channel to be started. |

###### 1.1.3.8.3 Response parameters

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID of the request. |
| Success | String | Indicates whether the request is successful. Valid values: true and false. |
| ErrCode | String | The error code. |
| ErrMessage | String | The detailed error message. |

###### 1.1.3.8.4 Examples

The following code provides an example of how to use the Java SDK to start a subscription task.

```java
private static void startSbeJob(String MigrationJobId){
        StartSubscriptionInstanceRequest request = new StartSubscriptionInstanceRequest();
        request.setSubscriptionInstanceId(jobId);
            StartSubscriptionInstanceResponse response = client.getAcsResponse(request);
            System.out.println("Start "+MigrationJobId+" Succeed");
        } catch (Exception e) {
            // TODO: handle exception
            System.out.println("Start "+MigrationJobId + " Failed");
            System.out.println(e.toString());
```

#### 1.1.4 Data synchronization APIs

##### 1.1.4.1 ConfigureSynchronizationJob

###### 1.1.4.1.1 Overview

After you call the CreateSynchronizationJob operation to purchase a synchronization instance, you can call this operation to configure a synchronization task, provided that the synchronization task is not configured.

###### 1.1.4.1.2 Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to ConfigureSynchronizationJob. |
| Synchronizati onJobId | String | Yes | The ID of the data synchronization task. |
| Synchronizati onJobName | String | No | The name of the data synchronization task. |
| SourceEndpoi nt.InstanceId | String | Yes | The ID of the source instance. |
| SourceEndpoi nt.OwnerID | String | No | The ID of the Apsara Stack tenant account to which the source instance belongs. This parameter is available if the source and destination instances belong to different Apsara Stack tenant accounts. |
| SourceEndpoi nt.Role | String | No | The RAM role that the Apsara Stack tenant account of the source instance assigns to the Apsara Stack tenant account of the destination instance. This parameter is available if the source and destination instances belong to different Apsara Stack tenant accounts. |
| DestinationEn dpoint.Instan ceId | String | Yes | The ID of the destination instance. If the destination instance is a MaxCompute or DataHub instance, the parameter indicates the project. If the destination instance is an AnalyticDB instance, the parameter indicates the database name. |
| Synchronizati onObjects | List | Yes | The objects that you want to synchronize. |

| Parameter | Type | Required | Description |
|---|---|---|---|
| StructureIniti alization | Boolean | No | Specifies whether to perform initial schema synchronization. Valid values: true: yes false: no Default value: true. |
| DataInitializat ion | Boolean | No | Specifies whether to perform initial full data synchronization. Valid values: true: yes false: no Default value: true. |
| PartitionKey. ModifyTime _ Year | Boolean | No | Specifies whether the incremental data table is partitioned by year. This parameter is available if the destination instance is a MaxCompute instance. Valid values: true: The partition of the incremental data table is a yearly partition. false: The incremental data table does not support yearly partitions. Default value: true. |
| PartitionKey. ModifyTime _ Month | Boolean | No | Specifies whether the incremental data table is partitioned by month. This parameter is available if the destination instance is a MaxCompute instance. Valid values: true: The incremental data table supports monthly partitions. false: The incremental data table does not support monthly partitions. Default value: true. |
| PartitionKey. ModifyTime _ Day | Boolean | No | Specifies whether the incremental data table is partitioned by day. This parameter is available if the destination instance is a MaxCompute instance. Valid values: true: The incremental data table supports daily partitions. false: The incremental data table does not support daily partitions. Default value: true. |
| PartitionKey. ModifyTime _ Hour | Boolean | No | Specifies whether the incremental data table is partitioned by hour. This parameter is available if the destination instance is a MaxCompute instance. Valid values: true: The incremental data table supports hourly partitions. false: The incremental data table does not support hourly partitions. Default value: true. |

| Parameter | Type | Required | Description |
|---|---|---|---|
| PartitionKey. ModifyTime _ Minute | Boolean | No | Specifies whether the incremental data table is partitioned by minute. This parameter is available if the destination instance is a MaxCompute instance. Valid values: true: The incremental data table supports minute partitions. false: The incremental data table does not support minute partitions. A minute partition is generated every 15 minutes. |
| Checkpoint | String | No | The start offset of incremental data synchronization. The value is a Unix timestamp. |

###### 1.1.4.1.3 Response parameters

| Name | Type | Description |
|---|---|---|
| <Common response parameters> | - | The request ID. |

###### 1.1.4.1.4 Example

This topic describes how to use the Java SDK to configure a synchronization task.

```java
public void configureSyncJobRDS2RDS(String SyncJobId,DefaultAcsClient client) {
        ConfigureSynchronizationJobRequest request = new ConfigureSynchronizationJobRequest
();
        request.setSynchronizationJobId(SyncJobId);
        request.setSynchronizationJobName("jiangliu_test_rds2rds_sync");
        request.setSourceEndpointInstanceId("rm-axxxxxxxxxxxxxxxxx");
        request.setDestinationEndpointInstanceId("rm-bxxxxxxxxxxxxxxxxx");
        request.setStructureInitialization(true);
        request.setDataInitialization(true);
        String SyncObject="[{\"DBName\":\"jiangliutest\",\"NewDBName\":\"jiangliutest\","
                + "\"TableIncludes\":[{\"TableName\":\"t1\",\"NewTableName\":\"t1\"}]}]";
        request.setSynchronizationObjects(SyncObject);
        ConfigureSynchronizationJobResponse response = new ConfigureSynchronizationJobRespo
nse();
            response = client.getAcsResponse(request);
            System.out.println("Configure Sync Job Succeed!") ;
        } catch (Exception e) {
            // TODO: handle exception
            System.out.println("Configure Sync Job Failed");
            System.out.println(e.toString());
```

##### 1.1.4.2 CreateSynchronizationJob

###### 1.1.4.2.1 Overview

You can call this operation to purchase a data synchronization instance. After the purchase, you need to call the ConfigureSynchronizationJob operation to configure the instance. If your synchronization instance adopts the Pay-As-You-Go billing method, you will be charged only when you have called the ConfigureSynchronizationJob operation and started the synchronization task.

###### 1.1.4.2.2 Request parameters

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to CreateSynchronizationJob. |
| SourceRegion | String | Yes | The region of the source instance specified in the synchronization task. Valid values: cn-hangzhou: Alibaba Cloud in Hangzhou cn-shanghai: Alibaba Cloud in Shanghai cn-qingdao: Alibaba Cloud in Qingdao cn-beijing: Alibaba Cloud in Beijing cn-zhangbei: Alibaba Cloud in Zhangbei cn-shenzhen: Alibaba Cloud in Shenzhen cn-hongkong: Alibaba Cloud in Hong Kong us-west-1: Alibaba Cloud in Western US us-east-1: Alibaba Cloud in Eastern US ap-southeast-1: Alibaba Cloud in Singapore cn-hangzhou-finance-1: Finance Cloud in Hangzhou cn-qingdao-finance-1: Finance Cloud in Qingdao cn-shanghai-finance-1: Finance Cloud in Shanghai cn-shenzhen-finance-1: Finance Cloud in Shenzhen me-east-1: Alibaba Cloud in Dubai en-central-1: Alibaba Cloud in Frankfurt |
| SourceEndpoin t.InstanceType | String | No | The type of the source instance specified in the synchronization task. Valid value: RDS. Default value: RDS. |
| DestinationEnd point.Instance Type | String | No | The type of the destination instance specified in the synchronization task. Valid values: RDS, MaxCompute, and DataHub. Default value: RDS. |

| Name | Type | Required | Description |
|---|---|---|---|
| SourceRegion | String | Yes | The region of the destination instance specified in the synchronization task. Valid values: cn-hangzhou: Alibaba Cloud in Hangzhou cn-shanghai: Alibaba Cloud in Shanghai cn-qingdao: Alibaba Cloud in Qingdao cn-beijing: Alibaba Cloud in Beijing cn-zhangbei: Alibaba Cloud in Zhangbei cn-shenzhen: Alibaba Cloud in Shenzhen cn-hongkong: Alibaba Cloud in Hong Kong us-west-1: Alibaba Cloud in Western US us-east-1: Alibaba Cloud in Eastern US ap-southeast-1: Alibaba Cloud in Singapore cn-hangzhou-finance-1: Finance Cloud in Hangzhou cn-qingdao-finance-1: Finance Cloud in Qingdao cn-shanghai-finance-1: Finance Cloud in Shanghai cn-shenzhen-finance-1: Finance Cloud in Shenzhen me-east-1: Alibaba Cloud in Dubai en-central-1: Alibaba Cloud in Frankfurt |
| NetworkType | String | No | The type of the data transmission network used for cross-region synchronization. Valid values: Internet and Intranet. Default value: Internet. |
| Synchronizatio nJobClass | String | No | The synchronization task type. Valid values: micro, small, medium, and large. Default value: small. |
| PayType | String | Yes | The billing method. Valid values: Postpaid and Prepaid. |
| Period | String | No | Indicates whether to subscribe to the instance on a yearly or monthly basis. This parameter is required when PayType is set to Prepaid. Valid values: Year and Month. |
| UsedTime | String | No | The duration of the subscription, in months. This parameter is required when Period is set to Month. Set the value to an integer greater than 0. |
| ClientToken | String | No | The token used to ensure the idempotence of the request. It can be any string. |

###### 1.1.4.2.3 Response parameters

| Name | Type | Description |
|---|---|---|
| SynchronizationJobId | String | The GUID of the synchronization task. |

###### 1.1.4.2.4 Examples

The following code provides an example of how to use the Java SDK to purchase a synchronization instance.

```java
public class DataSyncTest {
    public String createSyncJob(DefaultAcsClient client) {
        CreateSynchronizationJobRequest request = new CreateSynchronizationJobRequest();
        request.setSourceRegion("cn-hangzhou");
        request.setDestRegion("cn-hangzhou");
        request.setSynchronizationJobClass("micro");
        request.setPayType("Postpaid");
        request.setClientToken("createsyncjob_1");
        CreateSynchronizationJobResponse response = new CreateSynchronizationJobResponse();
            response = client.getAcsResponse(request);
            String DataSyncId  = response.getSynchronizationJobId();
            System.out.println("Create Synchronization Job Succeed! Synchronization Job Id
is "+DataSyncId);
            return DataSyncId;
        } catch (Exception e) {
            // TODO: handle exception
            System.out.println("Create Synchronization Job Failed!") ;
            return null;
```

##### 1.1.4.3 DeleteSynchronizationJob

###### 1.1.4.3.1 Overview

You can call this operation to delete a synchronization task regardless of the synchronization task status. After a synchronization task is released, you cannot query or manage it through OpenAPI or the console.

###### 1.1.4.3.2 Request parameters

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DeleteSynchronizationJo b. |

| Developer Guide·Developer | Guide |   | Data Transmission Servic |
|---|---|---|---|

| Name | Type | Required | Description |
|---|---|---|---|
| SynchronizationJobId | String | Yes | The synchronization task ID. |

###### 1.1.4.3.3 Response parameters

| Name | Type | Description |
|---|---|---|
| <Common response parameters> | - | The request ID. |

###### 1.1.4.3.4 Examples

The following code provides an example of how to use the Java SDK to delete a synchronization task.

```java
public void deleteSyncJob(String SyncJobId,DefaultAcsClient client) {
        DeleteSynchronizationJobRequest request = new DeleteSynchronizationJobRequest();
        request.setSynchronizationJobId(SyncJobId);
        DeleteSynchronizationJobResponse response = new DeleteSynchronizationJobResponse();
            response = client.getAcsResponse(request);
            System.out.println("Delete Sync Job "+SyncJobId+ " Succeed!") ;
        } catch (Exception e) {
            // TODO: handle exception
            System.out.println("Delete Sync Job "+SyncJobId+ " Failed!") ;
```

##### 1.1.4.4 DescribeDataLoadStatus

###### 1.1.4.4.1 Overview

You can call this operation to query initial synchronization details regardless of the synchronization task status.

###### 1.1.4.4.2 Request parameters

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeDataLoadStatu s. |

| Name | Type | Required | Description |
|---|---|---|---|
| SynchronizationJobId | String | Yes | The synchronization task ID. |
| StructureInitialization | Boolean | No | The schema initialization details. |
| DataInitialization | Boolean | No | The full data initialization details. |
| DataSynchronization | Boolean | No | The incremental data initialization details. |
| PageSize | Integer | No | The number of records on each page. Valid values: 30, 50, and 100. Default value: 30. This parameter is required when only one of these three parameters is set to true: StructureInitialization, DataInitialization, and DataSynchronization. |
| PageNum | Integer | No | The page number. It must be greater than 0 and smaller than or equal to the maximum value of Integer. Default value: 1. This parameter is required when only one of these three parameters is set to true: StructureInitialization, DataInitialization, and DataSynchronization. |

###### 1.1.4.4.3 Response parameters

| Name | Type | Description |
|---|---|---|
| <Common response parameters> | - | The request ID. |

###### 1.1.4.4.4 Examples

The following code provides an example of how to use the Java SDK to query the initial synchronization details.

```
public void descInitStatus(String SyncJobId, DefaultAcsClient client) { DescribeInitializationStatusRequestrequest=newDescribeInitializationStatusReque
```

```java
        DescribeInitializationStatusRequest request  new DescribeInitializationStatusReque
st();
        request.setSynchronizationJobId(SyncJobId);
        DescribeInitializationStatusResponse response = new DescribeInitializationStatusRes
ponse();
            response = client.getAcsResponse(request);
            System.out.println("Describe Initialization Detail of Synchronization Job "+Syn
cJobId+" Succeed!") ;
            List<StructureInitializationDetail> strucInitDetails  = response.getStructureIn
itializationDetails();
            List<DataInitializationDetail> dataInitDetails  = response.getDataInitializatio
nDetails();
            List<com.aliyuncs.dts.model.v20160801. DescribeInitializationStatusResponse.Dat
aSynchronizationDetail> dataSynchronizationDetails = response.getDataSynchronizationDetails ();
            System.out.println("Structure Initialization Detail:");
            for (int i = 0; i < strucInitDetails.size(); i++) {
                System.out.println("ObjectName:"+strucInitDetails.get(i).getObjectName()
                        +"; ObjectType:"+strucInitDetails.get(i).getObjectType()
                        +"; SRCDBName:"+strucInitDetails.get(i).getSourceOwnerDBName()
                        +"; DESTDBName:"+strucInitDetails.get(i).getDestinationOwnerDBName(
```

`)`

```java
                        +"; Status:"+strucInitDetails.get(i).getStatus()
                        +"; ErrMSG:"+strucInitDetails.get(i).getErrorMessage());
            System.out.println("Data Initialization Detail:");
            for (int i = 0; i < dataInitDetails.size(); i++) {
                System.out.println("TableName:"+dataInitDetails.get(i).getTableName()
                        +"; SRCDBName:"+dataInitDetails.get(i).getSourceOwnerDBName()
                        +"; DESTDBName:"+dataInitDetails.get(i).getDestinationOwnerDBName()
                        +"; Status:"+dataInitDetails.get(i).getStatus()
                        +"; TotalRows:"+dataInitDetails.get(i).getTotalRowNum()
                        +"; FinishedRows:"+dataInitDetails.get(i).getFinishRowNum()
                        +"; UsedTime:"+dataInitDetails.get(i).getUsedTime()
                        +"; ErroMSG:"+dataInitDetails.get(i).getErrorMessage());
            System.out.println("Data Synchronization Detail:");
            for (int i = 0; i < dataSynchronizationDetails.size(); i++) {
                System.out.println("TableName:"+dataSynchronizationDetails.get(i).getTableN
ame()
                        +"; SRCDBName:"+dataSynchronizationDetails.get(i).getSourceOwnerDBN
ame()
                        +"; DESTDBName:"+dataSynchronizationDetails.get(i).getDestinationOw
nerDBName()
                        +"; Status:"+dataSynchronizationDetails.get(i).getStatus()
                        +"; ErrMSG:"+dataSynchronizationDetails.get(i).getErrorMessage());
        } catch (Exception e) {
            // TODO: handle exception
            System.out.println("Describe Initialization Status of Synchronization Job "+Syn
cJobId+" Failed!") ;
            System.out.println(e.toString());
```

##### 1.1.4.5 DescribeSynchronizationJobStatus

###### 1.1.4.5.1 Overview

You can call this operation to query the status and running details of a synchronization task regardless of its status.

###### 1.1.4.5.2 Request parameters

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeSynchronization JobStatus. |
| SynchronizationJobId | String | Yes | The ID of the synchronization instance. |
| SynchronizationDirectio n | String | No | The synchronization direction. Valid values: Forward and Reverse. Default value: Forward. |

###### 1.1.4.5.3 Response parameters

| Name | Type | Description |
|---|---|---|
| SynchronizationJobId | String | The synchronization task ID. |
| SynchronizationJobName | String | The synchronization task name. |
| SynchronizationJobClass | String | The synchronization task type. |
| PayType | String | The billing method. |
| ExpireTime | String | The expiration time, in the format of YYYY-MM-DDT hh:mm:ssZ, such as 2011- 06-09T 12:11:11Z. |
| SourceEndpoint | SourceEndpoint | The endpoint to access the source instance specified in the synchronization task. |
| DestinationEndpoint | DestinationEndpoint | The endpoint to access the destination instance specified in the synchronization task. |

| eveloper Guide·Developer Guide |   | Data Transmission Servic |
|---|---|---|

| Name | Type | Description |
|---|---|---|
| SynchronizationObjects | List | The objects to be synchronized. |
| StructureInitialization | String | Indicates whether to perform schema initialization. |
| DataInitialization | String | Indicates whether to perform full data initialization. |
| Status | String | The synchronization task status. Valid values: NotStarted, Prechecking, PrecheckFailed, Initializating, InitializeFailed, Synchronizing, Failed, Suspending, Modifying, and Finished. |
| ErrorMessage | String | The cause of the synchronization error. |
| PrecheckStatus | PrecheckStatus | The precheck status. For more information, see PrecheckStatus parameter definitions. |
| StructureInitializationStatus | StructureInitializationStat us | The schema initialization status. For more information, see StructureInitializationStatus parameter definitions. |
| DataInitializationStatus | DataInitializationStatus | The full data initialization status. For more information, see DataInitializationStatus parameter definitions. |
| DataSynchronizationStatus | DataSynchronizationStat us | The incremental data initialization status. For more information, see DataSynchronizationStatus parameter definitions. |
| Delay | String | The synchronization latency. Unit: second. |
| Performance | String | The synchronization performance. For more information, see Performance parameter definitions. |

###### 1.1.4.5.4 PrecheckStatus parameter definitions

| Name | Type | Description |
|---|---|---|
| Status | String | The precheck status. |
| Percent | String | The precheck progress. Unit: %. |

| Name | Type | Description |
|---|---|---|
| Detail | List | The check details of each precheck item. For more information, see CheckItem parameter definitions. |

###### 1.1.4.5.5 CheckItem parameter definitions

| Name | Type | Description |
|---|---|---|
| ItemName | String | The check item name. |
| CheckStatus | String | The check status. Valid values: NotStarted Checking Failed Finished |
| ErrorMessage | String | The cause of the error. |
| RepairMethod | String | The repair method. |

###### 1.1.4.5.6 StructureInitializationStatus parameter definitions

definitions

| Name | Type | Description |
|---|---|---|
| Status | String | The migration status. Valid values: NotStarted Migrating Failed Finished |
| ErrorMessage | String | The cause of the migration error. |
| Percent | String | The migration progress. Unit: %. |
| Progress | String | The number of tables that have been migrated. |

###### 1.1.4.5.7 DataInitializationStatus parameter definitions

| Name | Type | Description |
|---|---|---|
| Status | String | The migration status. Valid values: NotStarted Migrating Failed Finished |
| ErrorMessage | String | The cause of the migration error. |
| Percent | String | The migration progress. Unit: %. |
| Progress | String | The number of tables that have been migrated. |

###### 1.1.4.5.8 DataSynchronizationStatus parameter definitions

definitions

| Name | Type | Description |
|---|---|---|
| Status | String | The migration status. Valid values: NotStarted Migrating Failed Finished |
| ErrorMessage | String | The cause of the migration error. |
| Percent | String | The migration progress. Unit: %. |
| Delay | String | The migration latency. Unit: second. |

###### 1.1.4.5.9 Performance parameter definitions

| Name | Type | Description |
|---|---|---|
| TPS | String | The number of records that are synchronized per second. |
| Flow | String | The data traffic that is synchronized per second. Unit: Mbit/s. |

###### 1.1.4.5.10 Examples

The following code provides an example of how to use the Java SDK to query the status of a synchronization task.

```java
public void descSyncJobStatus(String SyncJobId,DefaultAcsClient client) {
        DescribeSynchronizationJobStatusRequest request = new DescribeSynchronizationJobSta
tusRequest();
        request.setSynchronizationJobId(SyncJobId);
        DescribeSynchronizationJobStatusResponse response = new DescribeSynchronizationJobS
tatusResponse();
            response = client.getAcsResponse(request);
            /*Get Sync Configure of the Sync Job*/
            System.out.println("SyncJobId:"+response.getSynchronizationJobId()
                    +"SyncJobName:"+response.getSynchronizationJobName()
                    +"; PayType:"+response.getPayType()+"; ExpireTime:"+response.getExpireT
ime()
                    +"; SyncClass:"+response.getSynchronizationJobClass()
                    +"; StrucInit:"+response.getStructureInitialization()
                    +"; DataInit:"+response.getDataInitialization()+"; Status:"+response.ge
tStatus()
                    +"; Delay:"+response.getDelay()
                    +"; ErrMSG:"+response.getErrorMessage());
            /*Get Sync Objects of the Sync Job*/
            System.out.println("Sync Objects:");
            List<SynchronizationObject> syncObjects = response.getSynchronizationObjects();
            /*Get the Source Endpoint of the synchronization job*/
            SourceEndpoint sourceEndpoint = response.getSourceEndpoint();
            System.out.println("InstanceType:"+sourceEndpoint.getInstanceType()
                    +"InstanceId:"+sourceEndpoint.getInstanceId());
            /*Get the Destination Endpoint of the synchronization job*/
            DestinationEndpoint destinationEndpoint = new DestinationEndpoint();
            System.out.println("Instance Type:"+destinationEndpoint.getInstanceType()
                    +destinationEndpoint.getInstanceId());
            // Get Sync Object of the synchronization job
            System.out.println("SyncObject:"+org.json.JSONObject.valueToString(syncObjects)
```

);

```java
            // Get Precheck Status of the synchronization job
                com.aliyuncs.dts.model.v20160801. DescribeSynchronizationJobStatusResponse.
PrecheckStatus precheckStatus = response.getPrecheckStatus();
                System.out.println("Get Precheck Status for Sync Job Succeed");
                System.out.println("Precheck Status:"+response.getPrecheckStatus().getStatu
s()
                        +";  Precheck Percent:"+response.getPrecheckStatus().getPercent());
                List<com.aliyuncs.dts.model.v20160801. DescribeSynchronizationJobStatusResp
onse.PrecheckStatus.CheckItem> precheckDetails= precheckStatus.getDetail();
                for (int i = 0; i < response.getPrecheckStatus().getDetail().size(); i++) {
                    System.out.println("CheckItem:"+response.getPrecheckStatus().getDetail(
).get(i).getCheckStatus()
                            +"; ErrorMSG:"+response.getPrecheckStatus().getDetail().get(i).
getErrorMessage()
```

`+"`

```
RepairMethod"+responsegetPrecheckStats()getDetail()get
```

```java
                            +"; RepairMethod:"+response.getPrecheckStatus().getDetail().get
(i).getRepairMethod());
            } catch (Exception e) {
                // TODO: handle exception
                System.out.println("Get Precheck Status for Sync Job Failed");
            // Get Structure Initialization Status of the synchronization job
                System.out.println("Get Structure Initialization Status Succeed!") ;
                System.out.println("Structure Init Status:"+response.getStructureInitializa
tionStatus().getStatus()
                        +"; Percent:"+response.getStructureInitializationStatus().getPercen
t()
                        +"; Progress:"+response.getStructureInitializationStatus().getProgr
ess()
                        +"; ErrMSG:"+response.getStructureInitializationStatus().getErrorMe
ssage());
            } catch (Exception e) {
                // TODO: handle exception
                System.out.println("Get Structure Init Status Failed!") ;
            // Get Data Initialization Status of the synchronization job
                System.out.println("Get Data Initialization Status Succeed!") ;
                System.out.println("Data Init Status:"+response.getDataInitializationStatus
().getStatus()
                        +"; Percent:"+response.getDataInitializationStatus().getPercent()
                        +"; Progress:"+response.getDataInitializationStatus().getProgress()
                        +"; ErrMSG:"+response.getDataInitializationStatus().getErrorMessage
());
            } catch (Exception e) {
                // TODO: handle exception
                System.out.println("Get Data Init Status Failed!") ;
                System.out.println(e.toString());
            //Get Data Sync Status
                com.aliyuncs.dts.model.v20160801. DescribeSynchronizationJobStatusResponse.
DataSynchronizationStatus dataSyncStatus = response.getDataSynchronizationStatus();
                System.out.println("Get Data Synchronization Status Succeed!") ;
                System.out.println("Data Sync Status:"+response.getDataSynchronizationStatu
s().getStatus()
                        +"; Percent:"+response.getDataSynchronizationStatus().getPercent()
                        +"; Delay:"+response.getDataSynchronizationStatus().getDelay()
                        +"; ErrMSG:"+response.getDataSynchronizationStatus().getErrorMessag
e());
            } catch (Exception e) {
                // TODO: handle exception
                System.out.println("Get Data Sync Status Failed!") ;
                System.out.println(e.toString());
            //Get Performance
            System.out.println("TPS:"+response.getPerformance().getRPS()
+"Flow:"+responsegetPerformance()getRPS());
```

```java
                    +Flow:+response.getPerformance().getRPS());
        } catch (Exception e) {
            // TODO: handle exception
            System.out.println("Describe Status of Data Sync Job "+ SyncJobId + "Failed");
            System.out.println(e.toString());
```

##### 1.1.4.6 DescribeSynchronizationJobs

###### 1.1.4.6.1 Overview

You can call this operation to query the status and details of all synchronization tasks under the current account.

###### 1.1.4.6.2 Request parameters

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeSynchronization Jobs. |
| PageSize | Integer | No | The number of records on each page. Valid values: 30, 50, and 100. Default value: 30. |
| PageNum | Integer | No | The page number. It must be greater than 0 and smaller than or equal to the maximum value of Integer. Default value: 1. |

###### 1.1.4.6.3 Response parameters

| Name | Type | Description |
|---|---|---|
| PageNumber | Integer | The page number. |
| TotalRecordCount | Integer | The total number of records. |
| PageRecordCount | Integer | The number of records on the page. |

| Name | Type | Description |
|---|---|---|
| SynchronizationInstances | List | The synchronization task status. For more information, see SynchronizationInstance parameter definitions. |

###### 1.1.4.6.4 SynchronizationInstance parameter definitions

| Name | Type | Description |
|---|---|---|
| SynchronizationJobId | String | The synchronization task ID. |
| SynchronizationJobName | String | The synchronization task name. |
| SynchronizationJobClass | String | The synchronization task type. |
| PayType | String | The billing method. |
| ExpireTime | String | The expiration time, in the format of YYYY-MM-DDT hh:mm:ssZ, such as 2011-06-09T 12:11:11Z. |
| SourceEndpoint | SourceEndpoint | The endpoint to access the source instance specified in the synchronization task. |
| DestinationEndpoint | DestinationEndpoint | The endpoint to access the destination instance specified in the synchronization task. |
| SynchronizationObjects | List | The objects to be synchronized. |
| StructureInitialization | String | Indicates whether to perform schema initialization. |
| DataInitialization | String | Indicates whether to perform full data initialization. |

| Name | Type | Description |
|---|---|---|
| Status | String | The synchronization task status. Valid values: NotStarted Prechecking PrecheckFailed Initializating InitializeFailed Synchronizing Failed Suspending Modifying Finished |
| ErrorMessage | String | The cause of the synchronization error. |
| PrecheckStatus | PrecheckStatus | The precheck status. For more information, see PrecheckStatus parameter definitions. |
| StructureInitializationStatus | StructureInitializationStatus | The schema initialization status. For more information, see StructureInitializationStatus parameter definitions. |
| DataInitializationStatus | DataInitializationStatus | The full data initialization status. For more information, see DataInitializationStatus parameter definitions. |
| DataSynchronizationStatus | DataSynchronizationStatus | The incremental data initialization status. For more information, see DataSynchronizationStatus parameter definitions. |
| Delay | String | The synchronization latency. Unit: second. |
| Performance | String | The synchronization performance. For more information, see Performance parameter definitions. |

###### 1.1.4.6.5 PrecheckStatus parameter definitions

| Name | Type | Description |
|---|---|---|
| Status | String | The precheck status. |
| Percent | String | The precheck progress. Unit: %. |
| Detail | List | The check details of each precheck item. For more information, see CheckItem parameter definitions. |

###### 1.1.4.6.6 CheckItem parameter definitions

| Name | Type | Description |
|---|---|---|
| ItemName | String | The check item name. |
| CheckStatus | String | The check status. Valid values: NotStarted Checking Failed Finished |
| ErrorMessage | String | The cause of the error. |
| RepairMethod | String | The repair method. |

###### 1.1.4.6.7 StructureInitializationStatus parameter definitions

definitions

| Name | Type | Description |
|---|---|---|
| Status | String | The migration status. Valid values: NotStarted Migrating Failed Finished |
| ErrorMessage | String | The cause of the migration error. |
| Percent | String | The migration progress. Unit: %. |
| Progress | String | The number of tables that have been migrated. |

###### 1.1.4.6.8 DataInitializationStatus parameter definitions

| Name | Type | Description |
|---|---|---|
| Status | String | The migration status. Valid values: NotStarted Migrating Failed Finished |
| ErrorMessage | String | The cause of the migration error. |
| Percent | String | The migration progress. Unit: %. |
| Progress | String | The number of tables that have been migrated. |

###### 1.1.4.6.9 DataSynchronizationStatus parameter definitions

definitions

| Name | Type | Description |
|---|---|---|
| Status | String | The migration status. Valid values: NotStarted Migrating Failed Finished |
| ErrorMessage | String | The cause of the migration error. |
| Percent | String | The migration progress. Unit: %. |
| Delay | String | The migration latency. Unit: second. |

###### 1.1.4.6.10 Performance parameter definitions

| Name | Type | Description |
|---|---|---|
| TPS | String | The number of records that are synchronized per second. |

| Name | Type | Description |
|---|---|---|
| Flow | String | The data traffic that is synchronized per second. Unit: Mbit/s. |

###### 1.1.4.6.11 Examples

The following code provides an example of how to use the Java SDK to query the list of synchronization tasks.

```java
public void descSyncJobs(DefaultAcsClient client) {
        DescribeSynchronizationJobsRequest request = new DescribeSynchronizationJobsRequest
();
        DescribeSynchronizationJobsResponse response = new DescribeSynchronizationJobsRespo
nse();
            response = client.getAcsResponse(request);
            System.out.println("Describe all Synchronization Jobs Succeed!") ;
            List<SynchronizationInstance> syncInstances=response.getSynchronizationInstance
s();
            System.out.println("Total num of Synchronization Jobs:"+syncInstances.size());
            for (SynchronizationInstance syncInstance : syncInstances) {
                System.out.println("SyncJobId:"+syncInstance.getSynchronizationJobId()
                        +"; SyncJobName:"+syncInstance.getSynchronizationJobName()
                        +"; PayType:"+syncInstance.getPayType()
                        +"; InstanceClass:"+syncInstance.getSynchronizationJobClass()
                        +"; StrucInit:"+syncInstance.getStructureInitialization()
                        +"; DataInit:"+syncInstance.getDataInitialization()
                        +"; Status:"+syncInstance.getStatus()
                        +"; ErrMSG:"+syncInstance.getErrorMessage()
                        +"; Delay:"+syncInstance.getDelay());
                System.out.println("SourceEndpointInstanceType:"+syncInstance.getSourceEndp
oint().getInstanceType()
                        +"SourceEnpointInstanceId:"+syncInstance.getSourceEndpoint().getIns
tanceId());
                System.out.println("DestEndpointInstanceType:"+syncInstance.getDestinationE
ndpoint().getInstanceType()
                        +"DestEndpointInstanceId:"+syncInstance.getDestinationEndpoint().ge
tInstanceId());
                // Get Precheck Status
                    com.aliyuncs.dts.model.v20160801. DescribeSynchronizationJobsResponse.S
ynchronizationInstance.PrecheckStatus precheckStatus = syncInstance.getPrecheckStatus();
                    System.out.println("Get Precheck Status for Sync Job Succeed");
                    System.out.println("Precheck Status:"+syncInstance.getPrecheckStatus().
getStatus()
                            +"Precheck Percent:"+syncInstance.getPrecheckStatus().getPercen
t());
                    for (int j = 0; j < syncInstance.getPrecheckStatus().getDetail().size()
; j++) {
                        System.out.println("CheckItem:"+syncInstance.getPrecheckStatus().ge
tDetail().get(j).getCheckStatus()
```

`g` `j` `g`

```java
                                +"; ErrorMSG:"+syncInstance.getPrecheckStatus().getDetail()
.get(j).getErrorMessage()
                                +"; RepairMethod:"+syncInstance.getPrecheckStatus().getDeta
il().get(j).getRepairMethod());
                } catch (Exception e) {
                    // TODO: handle exception
                    System.out.println("Get Precheck Status for Sync Job Failed");
                // Get Structure Initialization Status
                    System.out.println("Get Structure Initialization Status Succeed!") ;
                    System.out.println("Structure Init Status:"+syncInstance.getStructureIn
itializationStatus().getStatus()
                            +"; Percent:"+syncInstance.getStructureInitializationStatus().g
etPercent()
                            +"; Progress:"+syncInstance.getStructureInitializationStatus().
getProgress()
                            +"; ErrMSG:"+syncInstance.getStructureInitializationStatus().ge
tErrorMessage());
                } catch (Exception e) {
                    // TODO: handle exception
                    System.out.println("Get Structure Initialization Status Failed!") ;
                // Get Data Initialization Status
                    System.out.println("Get Data Init Status Succeed!") ;
                    System.out.println("Data Init Status:"+syncInstance.getDataInitializati
onStatus().getStatus()
                            +"; Percent:"+syncInstance.getDataInitializationStatus().getPer
cent()
                            +"; Progress:"+syncInstance.getDataInitializationStatus().getPr
ogress()
                            +"; ErrMSG:"+syncInstance.getDataInitializationStatus().getErro
rMessage());
                } catch (Exception e) {
                    // TODO: handle exception
                    System.out.println("Get Data Init Status Failed!") ;
                    System.out.println(e.toString());
                //Get Data Synchronization Status
                    System.out.println("Get Data Synchronization Status Succeed!") ;
                    System.out.println("Data Sync Status:"+syncInstance.getDataSynchronizat
ionStatus().getStatus()
                            +"; Percent:"+syncInstance.getDataSynchronizationStatus().getPe
rcent()
                            +"; Delay:"+syncInstance.getDataSynchronizationStatus().getDela
y()
                            +"; ErrMSG:"+syncInstance.getDataSynchronizationStatus().getErr
orMessage());
                } catch (Exception e) {
                    // TODO: handle exception
                    System.out.println("Get Data Sync Status Failed!") ;
```

```java
                    System.out.println(e.toString());
        } catch (Exception e) {
            // TODO: handle exception
            System.out.println("Desc all Sync Jobs Failed!") ;
            System.out.println(e.toString());
```

##### 1.1.4.7 DescribeObjectModifyStatus

###### 1.1.4.7.1 Overview

After you call the ModifySynchronizationObject operation to modify the list of objects to be synchronized, you can call this operation to query the modification status and progress.

###### 1.1.4.7.2 Request parameters

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeObjectModifySt atus. |
| TaskId | String | Yes | The ID of the task for modifying the list of objects to be synchronized. It is the response parameter of the ModifySynchronizationO bject operation. |

###### 1.1.4.7.3 Response parameters

| Name | Type | Description |
|---|---|---|

| Name | Type | Description |
|---|---|---|
| Status | String | The modification status of the list of objects to be synchronized. Valid values: NotStarted Prechecking PrecheckFailed Migrating Failed Finished |
| ErrorMessage | String | The reason why the list of objects to be synchronized failed to be modified. |
| PrecheckStatus | PrecheckStatus | The precheck status. For more information, see PrecheckStatus parameter definitions. |
| StructureInitializationSt atus | StructureInitializationSt atus | The schema initialization status. For more information, see StructureInitializationStatus parameter definitions. |
| DataInitializationStatus | DataInitializationStatus | The full data initialization status. For more information, see DataInitializationStatus parameter definitions. |
| DataSynchronizationSta tus | DataSynchronizationSta tus | The incremental data initialization status. For more information, see DataSynchronizationStatus parameter definitions. |

###### 1.1.4.7.4 PrecheckStatus parameter definitions

| Name | Type | Description |
|---|---|---|
| Status | String | The precheck status. |
| Percent | String | The precheck progress. Unit: %. |
| Detail | List | The check details of each precheck item. For more information, see CheckItem parameter definitions. |

###### 1.1.4.7.5 CheckItem parameter definitions

| Name | Type | Description |
|---|---|---|
| ItemName | String | The check item name. |

| eveloper Guide·Developer Guide |   | Data Transmission Servic |
|---|---|---|

| Name | Type | Description |
|---|---|---|
| CheckStatus | String | The check status. Valid values: NotStarted Checking Failed Finished |
| ErrorMessage | String | The cause of the error. |
| RepairMethod | String | The repair method. |

###### 1.1.4.7.6 StructureInitializationStatus parameter definitions

definitions

| Name | Type | Description |
|---|---|---|
| Status | String | The migration status. Valid values: NotStarted Migrating Failed Finished |
| ErrorMessage | String | The cause of the migration error. |
| Percent | String | The migration progress. Unit: %. |
| Progress | String | The number of tables that have been migrated. |

###### 1.1.4.7.7 DataInitializationStatus parameter definitions

| Name | Type | Description |
|---|---|---|
| Status | String | The migration status. Valid values: NotStarted Migrating Failed Finished |
| ErrorMessage | String | The cause of the migration error. |
| Percent | String | The migration progress. Unit: %. |

| Data Transmission Service |   | Developer Guide·Developer Guid |
|---|---|---|

| Name | Type | Description |
|---|---|---|
| Progress | String | The number of tables that have been migrated. |

###### 1.1.4.7.8 DataSynchronizationStatus parameter definitions

definitions

| Name | Type | Description |
|---|---|---|
| Status | String | The migration status. Valid values: NotStarted Migrating Failed Finished |
| ErrorMessage | String | The cause of the migration error. |
| Percent | String | The migration progress. Unit: %. |
| Delay | String | The migration latency. |

###### 1.1.4.7.9 Examples

The following code provides an example of how to use the Java SDK to query the status of a task for modifying the list of objects to be synchronized.

```
public void descObjectModifyStatus(String SyncJobId,String TaskId,DefaultAcsClient client)
```

`{`

```java
        DescribeSynchronizationObjectModifyStatusRequest request = new DescribeSynchronizat
ionObjectModifyStatusRequest();
        request.setTaskId(TaskId);
        DescribeSynchronizationObjectModifyStatusResponse response = new DescribeSynchroniz
ationObjectModifyStatusResponse();
            response = client.getAcsResponse(request);
            System.out.println("Describe Sync Object Modify Status Succeed!") ;
            String status=response.getStatus();
            PrecheckStatus precheckStatus = response.getPrecheckStatus();
            StructureInitializationStatus strucInitStatus=response.getStructureInitializati
onStatus();
            DataInitializationStatus dataInitStatus=response.getDataInitializationStatus();
            DataSynchronizationStatus dataSyncStatus = response.getDataSynchronizationStatu
s();
            String errorMSG=response.getErrorMessage();
            //Get Precheck Status
            System.out.println("The precheck status of SYNC Job "+SyncJobId);
            String precheckstatus=precheckStatus.getStatus();
```

`g``p` `_` `p` `g`

```java
();
            String precheck_percent=precheckStatus.getPercent();
            System.out.println("Precheck Status:"+precheckStatus.getStatus()
                    +"; Precheck Percent:"+precheckStatus.getPercent());
            System.out.println("Precheck Detail:");
            for (int i = 0; i < precheckStatus.getDetail().size(); i++) {
                String ItemName=precheckStatus.getDetail().get(i).getItemName();
                String CheckStatus=precheckStatus.getDetail().get(i).getCheckStatus();
                String CheckErrorMsg=precheckStatus.getDetail().get(i).getErrorMessage();
                String RepairMethod = precheckStatus.getDetail().get(i).getRepairMethod();
                System.out.println("CheckItme:"+ItemName+"; Status:"+CheckStatus+"; ErrorMS
G:"+CheckErrorMsg
                        +"; RepairMethod:"+RepairMethod);
            // Get the status of the structure Initialization
            String strucInit_Status=strucInitStatus.getStatus();
            String strucInit_percent=strucInitStatus.getPercent();
            String strucInit_progress=strucInitStatus.getProgress();
            String strucInit_ErrMsg=strucInitStatus.getErrorMessage();
            System.out.println("The Structure Init Status of SYNC Job "+SyncJobId);
            System.out.println("Status:"+strucInit_Status+"; Percent:"+strucInit_percent
                    +"; Progress:"+strucInit_progress+"; ErrMSG:"+strucInit_ErrMsg);
            // Get the status of the data Initialization
            String dataInit_Status=dataInitStatus.getStatus();
            String dataInit_Percent = dataInitStatus.getPercent();
            String dataInit_Progress = dataInitStatus.getProgress();
            String dataInit_ErrMSG = dataInitStatus.getErrorMessage();
            System.out.println("The data Init Status of SYNC Job "+SyncJobId);
            System.out.println("Status:"+dataInit_Status+"; Percent:"+dataInit_Percent
                    +"; Progress:"+dataInit_Progress+"; ErrMSG:"+dataInit_ErrMSG);
            // Get the status of the data synchronization
            String dataSync_Status=dataSyncStatus.getStatus();
            String dataSync_Percent=dataSyncStatus.getPercent();
            String dataSync_Delay=dataSyncStatus.getDelay();
            String dataSync_ErrMSG=dataSyncStatus.getErrorMessage();
            System.out.println("The data Init Status of SYNC Job "+SyncJobId);
            System.out.println("Status:"+dataSync_Status+"; Percent:"+dataSync_Percent
                    +"; Delay:"+dataSync_Delay+"; ErrMSG:"+dataSync_ErrMSG);
        } catch (Exception e) {
            // TODO: handle exception
            System.out.println("Describe Synchronization Objects Modify Status Failed");
            System.out.println(e.toString());
```

##### 1.1.4.8 ModifySynchronizationObject

###### 1.1.4.8.1 Overview

When a synchronization task is in the NotStarted, Synchronizing, Failed, or Suspending status, you can call this operation to modify the list of objects to be synchronized. After that, you can call the DescribeObjectModifyStatus operation to query the detailed modification status of the list of objects to be synchronized.

###### 1.1.4.8.2 Request parameters

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to ModifySynchronizationO bject. |
| SynchronizationJobId | String | Yes | The ID of the synchronization task. |
| SynchronizationObjects | List | Yes | The list of modified objects to be synchronized. |

###### 1.1.4.8.3 Response parameters

| Name | Type | Description |
|---|---|---|
| TaskId | String | The ID of the task for modifying the list of objects to be synchronized. You can call the DescribeObjectModifyStatus operation based on this ID to query the modification status. |

###### 1.1.4.8.4 Examples

The following code provides an example of how to use the Java SDK to modify the list of objects to be synchronized.

```java
public String modifySyncObjects(String SyncJobId,DefaultAcsClient client) {
        String SyncObject="[{\"DBName\":\"jiangliutest\",\"NewDBName\":\"jiangliutest\","
                + "\"TableIncludes\":[{\"TableName\":\"t2\",\"NewTableName\":\"t2\"}]}]";
        ModifySynchronizationObjectRequest request = new ModifySynchronizationObjectRequest
();
        request.setSynchronizationJobId(SyncJobId);
        request.setSynchronizationObjects(SyncObject);
        ModifySynchronizationObjectResponse response = new ModifySynchronizationObjectRespo
nse();
            response = client.getAcsResponse(request);
            String TaskId=response.getTaskId();
            System.out.println("Modify Sync Job "+SyncJobId+" Succeed! Modify task Id:"+Tas
kId);
            return TaskId;
        } catch (Exception e) {
            // TODO: handle exception
            System.out.println("Modify Sync Job "+ SyncJobId +" Failed!") ;
            System.out.println(e.toString());
            return null;
```

##### 1.1.4.9 StartSynchronizationJob

###### 1.1.4.9.1 Overview

When a synchronization task is in the NotStarted, Failed, or Suspending status, you can call this operation to start the synchronization task.

###### 1.1.4.9.2 Request parameters

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to StartSynchronizationJob . |
| SynchronizationJobId | String | Yes | The synchronization task ID. |

###### 1.1.4.9.3 Response parameters

| Name | Type | Description |
|---|---|---|
| <Common response parameters> | - | The request ID. |

###### 1.1.4.9.4 Examples

The following code provides an example of how to use the Java SDK to start a synchronization task.

```java
public void startSyncJob(String SyncJobId,DefaultAcsClient client) {
        StartSynchronizationJobRequest request  = new StartSynchronizationJobRequest();
        request.setSynchronizationJobId(SyncJobId);
        StartSynchronizationJobResponse response = new StartSynchronizationJobResponse();
            response = client.getAcsResponse(request);
            System.out.println("Start Sync Job "+SyncJobId+" Succeed!") ;
        } catch (Exception e) {
            // TODO: handle exception
            System.out.println("Start Sync Job "+SyncJobId+ " Failed");
            System.out.println(e.toString());
```

##### 1.1.4.10 SuspendSynchronizationJob

###### 1.1.4.10.1 Overview

When a synchronization task is in the Synchronizing status, you can call this operation to suspend the synchronization task. If a synchronization task has been suspended for over 6 hours, it may fail to be started.

###### 1.1.4.10.2 Request parameters

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to SuspendSynchronization Job. |
| SynchronizationJobId | String | Yes | The synchronization task ID. |

###### 1.1.4.10.3 Response parameters

| Name | Type | Description |
|---|---|---|
| <Common response parameters> | - | The request ID. |

###### 1.1.4.10.4 Examples

The following code provides an example of how to use the Java SDK to suspend a synchronization task.

```
public void suspendSyncJob(String SyncJobId,DefaultAcsClient client) {
        SuspendSynchronizationJobRequest request = new SuspendSynchronizationJobRequest();
        request.setSynchronizationJobId(SyncJobId);
        SuspendSynchronizationJobResponse response = new SuspendSynchronizationJobResponse(
```

);

```java
            response = client.getAcsResponse(request);
            System.out.println("Suspend Sync Job "+SyncJobId+ " Succeed!") ;
        } catch (Exception e) {
            // TODO: handle exception
            System.out.println("Suspend Sync Job "+SyncJobId+" Failed");
            System.out.println(e.toString());
```

##### 1.1.4.11 DescribeSynchronizationJobStatusList

###### 1.1.4.11.1 Overview

You can call the DescribeSynchronizationJobStatusList operation to query the status and offset of one or more data synchronization tasks.

###### 1.1.4.11.2 Request parameters

| Parameter | Type | Required |   | Description |   |   |
|---|---|---|---|---|---|---|
| Action | String | Yes |   | The operation that you want to perform. Set the value to DescribeSynchronization JobStatusList. |   |   |
| SynchronizationJobIdList JsonStr | String | Yes |   | The IDs of one or more data synchronization tasks. The value is a JSON array, for example, ["dtsl08l48c313r0b k3"] . |   |   |
|   |   |   |   |   | ["dtsl08l48c313r0b |   |
|   |   |   |   | k3"] |   |   |

###### 1.1.4.11.3 Response parameters

| Parameter | Type | Description |
|---|---|---|
| SynchronizationJobListStatusList | list | The list of data synchronization instances. |
| SynchronizationJobId | String | The ID of the instance. |
| SynchronizationDirectionInfoList | list | The status and offset of one or more data synchronization tasks. |

| Data Transmission Service |   | Developer Guide·Developer Guid |
|---|---|---|
| Parameter | Type | Description |
| SynchronizationDirection | String | The synchronization direction. |
| Status | String | The status of the data synchronization task. |
| Checkpoint | String | The offset of the data synchronization task. The value is a Unix timestamp. |

###### 1.1.4.11.4 Examples

The following sample code shows how to use the Java SDK to query the status and offset of a data synchronization task.

```java
import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.exceptions.ServerException; import com.aliyuncs.profile.DefaultProfile; import com.google.gson.Gson; import java.util.*; import com.aliyuncs.dts.model.v20180801.*; public class DescribeSynchronizationJobStatusList {
    public static void main(String[] args) {
        DefaultProfile profile = DefaultProfile.getProfile("<region>", "<accessKeyId>", "<a
ccessSecret>");
        IAcsClient client = new DefaultAcsClient(profile);
        DescribeSynchronizationJobStatusListRequest request = new DescribeSynchronizationJo
bStatusListRequest();
        request.setRegionId("<region>");
        request.setSynchronizationJobIdListJsonStr("[\"dts********\"]");
            DescribeSynchronizationJobStatusListResponse response = client.getAcsResponse(r
equest);
            System.out.println(new Gson().toJson(response));
        } catch (ServerException e) {
            e.printStackTrace();
        } catch (ClientException e) {
            System.out.println("ErrCode:" + e.getErrCode());
            System.out.println("ErrMsg:" + e.getErrMsg());
            System.out.println("RequestId:" + e.getRequestId());
```

##### 1.1.4.12 ConfigureSynchronizationJobReplicatorCompare

###### 1.1.4.12.1 Overview

You can call the ConfigureSynchronizationJobReplicatorCompare operation to enable or disable image matching for a data synchronization task.

###### 1.1.4.12.2 Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to ConfigureSynchronizatio nJobReplicatorCompare. |
| SynchronizationJobId | String | Yes | The ID of the data synchronization task. |
| SynchronizationReplicat orCompareEnable | Boolean | Yes | Specifies whether to enable image matching. Valid values: true false |
| SynchronizationDirectio n | String | No | The synchronization direction. Valid values: Forward Reverse: indicates Reverse synchronization. Not e Default value: Forward. |

###### 1.1.4.12.3 Response parameters

| Parameter | Type | Description |
|---|---|---|
| Success | Boolean | Indicates whether the operation is successful. Valid values: true: The operation is successful. false: The operation failed. |

###### 1.1.4.12.4 Examples

The following sample code shows how to use the Java SDK to enable image matching for a data synchronization task.

```java
import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.exceptions.ServerException; import com.aliyuncs.profile.DefaultProfile; import com.google.gson.Gson; import java.util.*; import com.aliyuncs.dts.model.v20180801.*; public class ConfigureSynchronizationJobReplicatorCompare {
    public static void main(String[] args) {
        DefaultProfile profile = DefaultProfile.getProfile("<region>", "<accessKeyId>", "<a
ccessSecret>");
        IAcsClient client = new DefaultAcsClient(profile);
        ConfigureSynchronizationJobReplicatorCompareRequest request = new ConfigureSynchron
izationJobReplicatorCompareRequest();
        request.setRegionId("<region>");
        request.setSynchronizationJobId("dts********");
        request.putQueryParameter("SynchronizationReplicatorCompareEnable", "true");
            ConfigureSynchronizationJobReplicatorCompareResponse response = client.getAcsRe
sponse(request);
            System.out.println(new Gson().toJson(response));
        } catch (ServerException e) {
            e.printStackTrace();
        } catch (ClientException e) {
            System.out.println("ErrCode:" + e.getErrCode());
            System.out.println("ErrMsg:" + e.getErrMsg());
            System.out.println("RequestId:" + e.getRequestId());
```

##### 1.1.4.13 DescribeSynchronizationJobReplicatorCompare

###### 1.1.4.13.1 Overview

You can call the DescribeSynchronizationJobReplicatorCompare operation to query whether image matching is enabled for a data synchronization task.

###### 1.1.4.13.2 Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeSynchronization JobReplicatorCompare. |
| SynchronizationJobId | String | Yes | The ID of the data synchronization task. |
| SynchronizationDirectio n | String | No | The synchronization direction. Valid values: Forward Reverse Not e Default value: Forward. |

###### 1.1.4.13.3 Response parameters

| Parameter | Type | Description |
|---|---|---|
| SynchronizationReplicatorCompar eEnable | Boolean | Indicates whether image matching is enabled. Valid values: true: Image matching is enabled. false: Image matching is disabled. |

###### 1.1.4.13.4 Examples

The following sample code shows how to use the Java SDK to query whether image matching is enabled.

```java
import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.exceptions.ServerException; import com.aliyuncs.profile.DefaultProfile; import com.google.gson.Gson; import java.util.*; import com.aliyuncs.dts.model.v20180801.*; public class DescribeSynchronizationJobReplicatorCompare {
    public static void main(String[] args) {
        DefaultProfile profile = DefaultProfile.getProfile("<region>", "<accessKeyId>", "<a
ccessSecret>");
        IAcsClient client = new DefaultAcsClient(profile);
        DescribeSynchronizationJobReplicatorCompareRequest request = new DescribeSynchroniz
ationJobReplicatorCompareRequest();
        request.setRegionId("<region>");
        request.setSynchronizationJobId("dts********");
            DescribeSynchronizationJobReplicatorCompareResponse response = client.getAcsRes
ponse(request);
            System.out.println(new Gson().toJson(response));
        } catch (ServerException e) {
            e.printStackTrace();
        } catch (ClientException e) {
            System.out.println("ErrCode:" + e.getErrCode());
            System.out.println("ErrMsg:" + e.getErrMsg());
            System.out.println("RequestId:" + e.getRequestId());
```

### 1.2 Call the Java SDK

#### 1.2.1 Quick start

This topic describes how to obtain and call the DTS Java SDK. Install the Apsara Stack Java SDK If you use Apache Maven to manage Java projects, you only need to import the JAR file to pom.xml of the project. To use the development kit of Alibaba Cloud products, you must install the SDK core library and the product SDK. The SDK core library version is 3.2.8, and the DTS SDK version is 2.0.3.

```xml
<dependency>
    <groupId>com.aliyun</groupId>
    <artifactId>aliyun-java-sdk-core</artifactId>
    <version>3.2.8</version>
</dependency> <dependency>
    <groupId>com.aliyun</groupId>
    <artifactId>aliyun-java-sdk-dts</artifactId>
    <version>2.0.3-SNAPSHOT</version>
</dependency>
```

Use the Java SDK The DTS SDK includes two core kits: aliyun-java-sdk-core-inner and aliyun-java-sdk-dts. The aliyun-javasdk-core-inner kit automatically routes requests to the DTS endpoint. The aliyun-java-sdk-dts kit includes the related classes of all DTS functions. The following uses CreateMigrationJob, the method that uses the DTS Java SDK to create a data migration task, to describe the complete process of using the SDK. The aliyun-java-sdk-dts kit includes all classes used.
1. Create an object of IClientProfile named profile. This object stores the Access Key ID, Access Key
Secret, and default region information.

```
IClientProfile profile = DefaultProfile.getProfile("cn-hangzhou", accsessKeyId, accessS ecret);
```

2. Create the DefaultAcsClient object. All subsequent responses are obtained from DefaultAcsClient.

```
client = new DefaultAcsClient(profile);
```

3. Create a request for the corresponding method. The request class is named in the format of API
method name + Request. For example, the name of the API method used to create a migration task is CreateMigrationJob, so the corresponding request class name is CreateMigrationJobRequest. You can use a constructor to create a default class.

```
CreateMigrationJobRequest request=new CreateMigrationJobRequest();
```

4. Use the setXxx method of the request class to configure information that must be provided in API
parameters. For example, configure the region and specification of a migration task.

```
request.setRegion("cn-hangzhou"); request.setMigrationJobClass("small");
```

5. Use the DefaultAcsClient object to obtain a response to the corresponding request.

```
ConfigureMigrationJobResponse response = client.getAcsResponse(request);
```

6. Call the getXxx method in the response to obtain a returned parameter value, such as the
migration task ID.

```
String MigrationJobId = response.getMigrationJobId();
```

7. The call process is now completed.

#### 1.2.2 User manual

##### 1.2.2.1 Install the Java SDK

This topic describes how to install and use the DTS Java SDK. The Apsara Stack Java SDK supports JDK V1.6 and later. You can install the latest JDK version by importing the JAR file. You can click here to download the DTS JAR file. If you are using Eclipse or IntelliJ, you can install the DTS Java SDK directly by importing the JAR file. The installation method is as follows: In Eclipse To install the DTS Java SDK in Eclipse, follow these steps: i. Copy the downloaded `aliyun-java-sdk-`dts-2.0.3`.jar` file to your project folder. ii. In Eclipse, right click the project, and then select Propert ies. iii. In the dialog box that appears, choose Java Build Pat h > Libraries > Add JARs to add the downloaded JAR files. iv. Click Apply and Close. In IntelliJ To install the DTS Java SDK in IntelliJ, follow these steps: i. Copy the downloaded `aliyun-java-sdk-`dts-2.0.3`.jar` file to your project folder. ii. Open your project in IntelliJ, and choose File > Project St ruct ure . iii. Click Apply and then OK.

##### 1.2.2.2 Configure identity verification credentials

When using the Apsara Stack SDK to access Apsara Stack services, you must provide an authorized account for identity verification. Currently, the Java SDK supports identity verification based on the AccessKey. When an Access Key is used as the access credential, you need to configure the credential during client initialization. Not ice Do not disclose any code that may contain your AccessKey. For example, do not commit the code to public GitHub projects. Otherwise, your Apsara Stack tenant account may be compromised.

```
DefaultProfile profile = DefaultProfile.getProfile(
    "<your-region-id>",          // The region ID.
    "<your-access-key-id>",      // The AccessKey ID of the authorized account.
    "<your-access-key-secret>"); // The AccessKey Secret of the authorized account.
```

##### 1.2.2.3 Initiate a call

This topic describes how to use the DTS Java SDK to initiate a request. Procedure
1. Create an AcsClient instance.

```
IAcsClient client = new DefaultAcsClient(profile);
```

2. Create a request.
A request class name is in the format of ${apiName}Request , where ${apiName} indicates the API name, such as CreateMigrationJobRequest. When the SDKs of multiple services are used, different requests may have the same name. Distinguish the requests by service package.

```
CreateMigrationJobRequest request=new CreateMigrationJobRequest();
```

3. Initiate a call and handle the response.

```java
                        ConfigureMigrationJobResponse response = client.getAcsResponse(
request);
                        System.out.println("Configure "+ MigrationJobId+ " Succeed");
                        } catch (Exception e) {
                        // TODO: handle exception
                        System.out.println("Configure "+MigrationJobId + " Failed!") ;
                        System.out.println(e.toString());
```

In normal cases, all response fields are deserialized into the response. You can directly call `respons` `e.getXXX()` to obtain the response fields. However, if an exception occurs or you want to obtain the original HTTP response, you can use the `doAction()` method to obtain the original response.

```
HttpResponse response = client.doAction(request);
```

##### 1.2.2.4 Troubleshooting

The Java SDK returns corresponding errors when errors occur on the server side or the SDK side. These errors contain detailed error information, including the error code and the error message. In normal cases, you do not need to solve the errors returned by the Java SDK. You only need to handle the errors returned by the server. `ServerException` is the error returned by the server. `ClientException` is the error returned by the SDK side. For example, when the following error occurs, you have to modify the AccessKey ID based on the error message.

```
com.aliyuncs.exceptions.ClientException: InvalidAccessKeyId.NotFound : Specified access key is not found.
```

If you want to handle the errors returned by the Java SDK, refer to the following example to write your code:

```java
    FooResponse response = client.getAcsResponse(request);
    // The following code is used to solve returned errors:
    // ...
}catch (ServerException e){
    // You can add your own error handling logic here
    // For example, display the error message
    System.out.println("ErrorCode=" + e.getErrCode());
    System.out.println("ErrorMessage=" + e.getErrMsg());
    // If you cannot solve the error, submit a ticket and provide the request ID to Alibaba
technical support personnel.
    System.out.println("ResponseId=" + e.getRequestId());
}catch (ClientException e){
    // You can add your own error handling logic here.
    // For example, display the error message.
    System.out.println("ErrorCode=" + e.getErrCode());
    System.out.println("ErrorMessage=" + e.getErrMsg());
```

##### 1.2.2.5 Errors and troubleshooting

The following are some common errors you may experience when using the Apsara Stack SDK.

|   |   | Error code |   |   |   |   | Error message |   |   | Cause | Solution |
|---|---|---|---|---|---|---|---|---|---|---|---|
|   |   | SDK.CanNotReso |   |   |   |   | Can not |   |   |   | Check whether the provided region ID and endpoint are correct. After obtaining the correct endpoint, run the following code to set the endpoint: DefaultProfile.addEndpoint("you r-region-id", "your-region-id", "product", "endpoint""); |
|   |   |   |   |   |   |   |   | Can not |   | The SDK cannot | and endpoint ar the correct endp |
|   |   |   |   |   |   |   | resolve |   |   |   | the co |
|   |   |   |   |   |   |   |   |   |   | automatically | code |
|   |   |   | SD | K.CanNotReso |   |   |   |   |   | obtain the |   |
|   |   |   |   |   |   |   | endpoint, |   |   | endpoint of the |   |
|   |   | lveEndpoint |   |   |   |   |   |   |   | endpoint |   |
|   |   |   |   |   |   |   | please check |   |   | called pr |   |
|   |   |   |   |   |   |   | the user |   |   |   |   |
|   |   |   |   |   |   |   | guide |   |   |   |   |

|   |   |   | Error code |   |   |   |   |   |   |   | Error message |   |   |   |   | Cause |   | Solution |   |   |   |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|   |   |   | SDK.JsonUnmars halError |   |   |   |   |   |   |   | Failed to |   |   |   |   | SDK response deserialization fails. In most cases, it is because the response structure received by the SDK does not conform to the API metadata. For example, the fields do not match or the format is incorrect. |   | You can use the client.doAction(request) method to obtain the original HTTP response. |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   | Failed to |   |   |   | structure rec |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   | Faile |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   | nUnmars |   | unmars |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   | halError |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   | halError |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | response |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | The request |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   | The request |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | timed out 4 |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | times(3 for retry), |   |   |   |   | The request has |   | In scenarios such as low n we recommend that you i |   |   |   |   |
|   |   |   |   |   | SDK.TimeoutErr |   |   |   |   |   |   |   |   |   |   | timed out and all |   | we reco |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | retry attempts |   | timeout |   |   |   |   |
|   |   |   | or |   |   |   |   |   |   |   |   |   |   |   |   | retry attempts |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | should have the |   |   |   |   | have failed. |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | hav |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | threshold raised a |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | little? |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | Your request |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   | Your request |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | is denied as |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | lack of ssl |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | protect.Recomme |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | Add the following code before sending a |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | nd:https://erro |   |   |   |   | The o | peration |   |   |   |   |   |
|   |   |   |   |   | SDK.ServerErro |   |   |   |   |   |   |   |   |   |   |   |   | request: |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | r- |   |   |   |   | only accepts |   |   |   |   |   |   |
|   |   |   | r: |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | center |   | .a |   |   | HTTPS requests |   |   | request.setProtocol(ProtocolTyp |   |   |   |
|   |   |   | InvalidProtocol |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | om/sta |   |   |   |   | but not HTTP |   |   | e.HTTPS) |   |   |   |
|   |   |   | .NeedSsl |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | h? |   |   |   |   | requests. |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | Keyword=Invalid |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | Protocol.NeedSs |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | l&source=PopGw |   |   |   |   |   |   |   |   |   |   |   |
