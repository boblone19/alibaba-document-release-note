---
title: "DataHub Developer Guide 20260311"
product_version: "V3.18.6"
pdf_pages: 128
source_pdf: "c0bd6672062dd2db_Alibaba Cloud Apsara Stack V3.18.6 DataHub Developer Guide 20260311.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/v3.18.6%E7%89%88%E6%9C%AC%E6%96%87%E6%A1%A3/%E6%95%B0%E6%8D%AE%E6%80%BB%E7%BA%BF/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.6%20DataHub%20Developer%20Guide%2020260311.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes)
---

# DataHub Developer Guide 20260311

## Table of Contents

- 1 API reference
  - 1.1 ListUserSubscriptions
  - 1.2 GetTopicSchema
  - 1.3 CreateConnector
  - 1.4 ListTopicAction
  - 1.5 DeleteTopic
  - 1.6 UpdateConnectorState
  - 1.7 GetShardDetail
  - 1.8 SplitShard
  - 1.9 GetAlarmRule
  - 1.10 CreateKafkaGroup
  - 1.11 CreateTopic
  - 1.12 MergeShard
  - 1.13 ExtendShard
  - 1.14 GetConsumerPlan
  - 1.15 AddTopicSchema
  - 1.16 ListKafkaGroup
  - 1.17 ResetSubscriptionOffset
  - 1.18 ListSubscriptions
  - 1.19 ReloadConnector
  - 1.20 DeleteSubscription
  - 1.21 ListTopics
  - 1.22 GetSubscriptionOffset
  - 1.23 GetConnectorShardStatus
  - 1.24 GetTopicDataTrendByDay
  - 1.25 GetSchemaByOdps
  - 1.26 UpdateTopicsForKafkaGroup
  - 1.27 ListShards
  - 1.28 GetTopicMetric
  - 1.29 ListRegions
  - 1.30 ResetConnectorOffset
  - 1.31 AppendField
  - 1.32 GetConnector
  - 1.33 AddProjectVpcWhiteList
  - 1.34 GetTopic
  - 1.35 ListTopicSchema
  - 1.36 DeleteConnector
  - 1.37 ListConnectors
  - 1.38 CreateSubscription
  - 1.39 DeleteKafkaGroup
  - 1.40 GetKafkaGroup
  - 1.41 SampleShard
  - 1.42 GetUserStorage
  - 1.43 GetProject
  - 1.44 ListTopicsByKafkaGroup
  - 1.45 UpdateConnectorField
  - 1.46 ListProjects
  - 1.47 DeleteProject
  - 1.48 CreateProject
  - 1.49 CheckServiceLinkedRoleForDeleting
  - 1.50 DeleteProjectVpcWhiteList
  - 1.51 DeleteTopicSchema
  - 1.52 GetAssumeRole
  - 1.53 GetProjectVpcWhiteList
  - 1.54 InitializeDataImportProcess
- 2 SDK reference
  - 2.1 SDK overview
  - 2.2 Prerequisites
    - 2.2.1 Overview
    - 2.2.2 Obtain an AccessKey pair
    - 2.2.3 Obtain endpoints
  - 2.3 DataHub SDK for Java
    - 2.3.1 Overview
    - 2.3.2 Preparations
    - 2.3.3 Ingest tuple data
      - 2.3.3.1 Create a tuple topic
      - 2.3.3.2 Obtain the list of shards
      - 2.3.3.3 Write data into DataHub
      - 2.3.3.4 Consume data
    - 2.3.4 Ingest blob data
      - 2.3.4.1 Create a blob topic
      - 2.3.4.2 Obtain the list of shards
      - 2.3.4.3 Write data into DataHub
      - 2.3.4.4 Consume data
    - 2.3.5 Data ingestion methods
      - 2.3.5.1 Ingest data based on shard IDs
      - 2.3.5.2 Ingest data based on hash values
      - 2.3.5.3 Ingest data based on partition keys
    - 2.3.6 Create a DataConnector
      - 2.3.6.1 Create a DataConnector for MaxCompute
      - 2.3.6.2 Create a DataConnector for AnalyticDB or ApsaraDB RDS for MySQL
  - 2.4 DataHub SDK for Python
    - 2.4.1 Install DataHub SDK for Python
    - 2.4.2 Preparations
    - 2.4.3 Create topics
    - 2.4.4 Write records into DataHub and subscribe applications to records
- 3 Scalability
  - 3.1 Scenario
  - 3.2 Obtain shard details
  - 3.3 Split a shard
  - 3.4 Merge shards
- 4 Insert a column to a topic schema
  - 4.1 Insert a column

## 1 API reference

### 1.1 ListUserSubscriptions

You can call the ListUserSubscriptions operation to query information about user subscriptions. The ListUserSubscriptions operation does not have operation-specific request headers and uses only common request headers. For more information, see the Common request parameters topic.

| Paramet er name | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| RegionId | String | Query | Yes | cn-wuhan | The region ID. |
| ProjectNa me | String | Query | No | test pro _ | The project name. |
| TopicNam e | String | Query | No | test topic _ | The topic name. |

**Return data**

| Parameter name | Type | Example | Description |
|---|---|---|---|
| List | Array | - | The list. |
| -Type | String | test | The type. |
| -Comment | String | test | The note. |
| -State | Integer | 0 | The status. |
| -Application | String | test | The application. |
| -SubscriptionId | String | 219304s124 | The subscription ID. |
| -Creator | String | admin | The user who creates the subscription. |
| -ProjectName | String | test | The project name. |
| -TopicName | String | test | The topic name. |

| Developer Guide·A | PI reference |   | DataHu |
|---|---|---|---|
| Parameter name | Type | Example | Description |
| TotalCount | String | 100 | The total number of entries returned. |
| RequestId | String | 20240205113332e 90fc50b77cc9bf5 | The ID of the request. |
| PageSize | String | 1 | The number of entries per page. |
| PageCount | String | 10 | The total number of pages. |
| PageNumber | String | 10 | The page number of the returned page. |
| Success | Boolean | true | The status code returned. |

```json
http(s)://[Endpoint]/?Action=ListUserSubscriptions &RegionId=cn-wuhan
 "TotalCount":"100",
 "RequestId":"20240205113332e90fc50b77cc9bf5",
 "PageSize":"1",
 "PageCount":"10",
 "PageNumber":"10",
 "List":[
   "Comment":"test",
   "Type":"test",
   "SubscriptionId":"219304s124",
   "ProjectName":"test",
   "State":0,
   "Creator":"admin",
   "Application":"test",
   "TopicName":"test"
```

`],`

```xml
<TotalCount>100</TotalCount> <RequestId>20240205113332e90fc50b77cc9bf5</RequestId> <PageSize>1</PageSize> <PageCount>10</PageCount> <PageNumber>10</PageNumber> <List>
 <Comment>test</Comment>
 <Type>test</Type>
 <SubscriptionId>219304s124</SubscriptionId>
 <ProjectName>test</ProjectName>
 <State>0</State>
 <Creator>admin</Creator>
 <Application>test</Application>
 <TopicName>test</TopicName>
</List>
```

| HttpCo de | Error code | Error message | Description |
|---|---|---|---|
| 400 | InvalidParameter | InvalidParameter | %s |
| 400 | NoPermission | NoPermission | %s |
| 400 | ResourceAlreadyExi st | ResourceAlreadyExist | %s |
| 400 | ResourceNotFound | ResourceNotFound | %s |
| 500 | OdpsServiceError | OdpsServiceError | %s |
| 502 | ApiProxyServiceErr or | ApiProxyServiceError | %s |
| 502 | InternalServerError | InternalServerError | %s |

### 1.2 GetTopicSchema

Call the GetTopicSchema operation to retrieve the topic schema. The GetTopicSchema operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" topic.

| Paramet er name | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| RegionId | String | Query | Yes | cn-wuhan | The region ID. |

|   | Developer Gui | de·API re | ference |   |   | DataHu | b |
|---|---|---|---|---|---|---|---|

| Paramet er name | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| ProjectNa me | String | Query | Yes | test | The project name. |
| TopicNam e | String | Query | Yes | test | The topic name. |
| VersionId | String | Query | No | 1 | The schema version number. |

**Return data**

| Parameter name | Type | Example | Description |
|---|---|---|---|
| RecordSchema | String | {} | The schema structure. |
| Success | Boolean | true | The returned status code. |

```json
http(s)://[Endpoint]/?Action=GetTopicSchema &RegionId=cn-wuhan &ProjectName=test &TopicName=test
 "VersionId":"1",
 "RequestId":"",
 "CreateTime":"",
 "Creator":"",
 "RecordSchema":"{}",
<VersionId>1</VersionId> <RequestId /> <CreateTime /> <Creator /> <RecordSchema>{}</RecordSchema>
```

| HttpCo de | Error code | Error message | Description |
|---|---|---|---|
| 400 | InvalidParameter | InvalidParameter | %s |
| 400 | NoPermission | NoPermission | %s |
| 400 | ResourceAlreadyExi st | ResourceAlreadyExist | %s |
| 400 | ResourceNotFound | ResourceNotFound | %s |
| 500 | OdpsServiceError | OdpsServiceError | %s |
| 502 | ApiProxyServiceErr or | ApiProxyServiceError | %s |
| 502 | InternalServerError | InternalServerError | %s |

### 1.3 CreateConnector

You can call the CreateConnector operation to create a connector. The CreateConnector operation does not have operation-specific request headers and uses only common request headers. For more information, see the Common request parameters topic.

| Paramet er name | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| RegionId | String | Query | Yes | cn-wuhna | The region ID. |
| ProjectNa me | String | Query | Yes | test | The project name. |
| TopicNam e | String | Query | Yes | test01 | The topic name. |
| Type | String | Query | Yes | SINK ODPS _ | The synchronization type. |
| StartTime | String | Query | Yes | 12355234 | The start time. |
| ImportFiel ds | String | Query | No | f1 | The synchronization fields. |

| Paramet er name | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Config | String | Query | Yes | {} | The synchronization configuration. |

**Response parameters**

| Parameter name | Type | Example | Description |
|---|---|---|---|
| ProjectName | String | test | The project name. |
| Success | Boolean | true | The returned status code. |
| TopicName | String | test01 | The topic name. |
| ConnectorId | String | 5c806a2f-84a0- 47c3-8dda- d8fa2852de3u | The sync task ID. |

```json
http(s)://[Endpoint]/?Action=CreateConnector &RegionId=cn-wuhna &ProjectName=test &TopicName=test01 &Type=SINK_ODPS &StartTime=12355234 &Config={}
 "ProjectName":"test",
 "Success":true,
 "TopicName":"test01",
 "ConnectorId":"5c806a2f-84a0-47c3-8dda-d8fa2852de3u"
<ProjectName>test</ProjectName> <TopicName>test01</TopicName> <ConnectorId>5c806a2f-84a0-47c3-8dda-d8fa2852de3u</ConnectorId>
```

| HttpCo de | Error code | Error message | Description |
|---|---|---|---|
| 400 | InvalidParameter | InvalidParameter | %s |
| 400 | NoPermission | NoPermission | %s |
| 400 | ResourceAlreadyExi st | ResourceAlreadyExist | %s |
| 400 | ResourceNotFound | ResourceNotFound | %s |
| 500 | OdpsServiceError | OdpsServiceError | %s |
| 500 | VPCServiceError | VPCServiceError | %s |
| 500 | CreateServiceLinke dRoleError | CreateServiceLinkedRoleError | An error occurred while creating a service-linked role. Make sure that your account is granted the ram:CreateServiceLinkedRole permission. For more information, visit https://help.aliyun.com/docume nt detail/184766.html. _ |
| 502 | ApiProxyServiceErr or | ApiProxyServiceError | %s |
| 502 | InternalServerError | InternalServerError | %s |

### 1.4 ListTopicAction

Call the ListTopicAction operation to retrieve topic operations. The ListTopicAction operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" topic.

| Paramet er name | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| RegionId | String | Query | Yes | cn-wuhan | The region ID. |
| ProjectNa me | String | Query | Yes | test | The project name. |
| TopicNam e | String | Query | Yes | test | The topic name. |

**Return data**

| Parameter name | Type | Example | Description |
|---|---|---|---|
| List | Array | - | The list information. |
| - ResourceName | String | bigdata | The resource set. |
| -UserName | String | admin | The username. |
| -ActionType | String | delete | The type of operation or event. |
| -ExtraInfo | String | test | The additional information. |
| -CreateTime | Long | 2174018322141 | The time when the topic was created. |
| RequestId | String | 2024850120103 | The ID of the request. |
| Success | Boolean | true | The status code returned. |

```json
http(s)://[Endpoint]/?Action=ListTopicAction &RegionId=cn-wuhan &ProjectName=test &TopicName=test
 "RequestId":"2024850120103",
 "List":[
   "UserName":"admin",
   "ActionType":"delete",
   "ResourceName":"bigdata",
   "CreateTime":2174018322141,
   "ExtraInfo":"test"
```

`],`

```xml
<RequestId>2024850120103</RequestId> <List>
 <UserName>admin</UserName>
 <ActionType>delete</ActionType>
 <ResourceName>bigdata</ResourceName>
 <CreateTime>2174018322141</CreateTime>
 <ExtraInfo>test</ExtraInfo>
</List>
```

| HttpCo de | Error code | Error message | Description |
|---|---|---|---|
| 400 | InvalidParameter | InvalidParameter | %s |
| 400 | NoPermission | NoPermission | %s |
| 400 | ResourceAlreadyExi st | ResourceAlreadyExist | %s |
| 400 | ResourceNotFound | ResourceNotFound | %s |
| 500 | OdpsServiceError | OdpsServiceError | %s |
| 502 | ApiProxyServiceErr or | ApiProxyServiceError | %s |
| 502 | InternalServerError | InternalServerError | %s |

### 1.5 DeleteTopic

Calls the DeleteTopic operation to delete a topic. The DeleteTopic operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the Common parameters topic.

| Paramet er name | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| RegionId | String | Query | No | cn-wuhan | The region ID. |
| ProjectNa me | String | Query | Yes | test | The name of the project. |
| TopicNam e | String | Query | Yes | test | The name of the topic. |

**Response parameters**

| Parameter name | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 202485010243012 | The ID of the request. |
| Success | Boolean | true | The returned status code. |

```json
http(s)://[Endpoint]/?Action=DeleteTopic &ProjectName=test &TopicName=test
 "RequestId":"202485010243012",
<RequestId>202485010243012</RequestId>
```

| HttpCo de | Error code | Error message | Description |
|---|---|---|---|
| 400 | InvalidParameter | InvalidParameter | %s |
| 400 | NoPermission | NoPermission | %s |
| 400 | ResourceAlreadyExi st | ResourceAlreadyExist | %s |
| 400 | ResourceNotFound | ResourceNotFound | %s |
| 500 | OdpsServiceError | OdpsServiceError | %s |
| 502 | ApiProxyServiceErr or | ApiProxyServiceError | %s |
| 502 | InternalServerError | InternalServerError | %s |

### 1.6 UpdateConnectorState

Call the UpdateConnectorState operation to update the connector status. The UpdateConnectorState operation does not have operation-specific request headers and uses only common request headers. For more information, see the Common request parameters topic.

| Paramet er name | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| RegionId | String | Query | No | cn-wuhan | The region ID. |
| ProjectNa me | String | Query | Yes | test | The project name. |
| TopicNam e | String | Query | Yes | test | The topic name. |
| ConnectorI d | String | Query | Yes | 5c806a2f-84a0-47c3- 8dda-d8fa2852de92 | The connector ID. |
| State | Boole an | Query | Yes | STOPPED | The status of the synchronization. |

**Response parameters**

| Parameter name | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 202345012824310 3u | The ID of the request. |
| Success | Boolean | true | The returned status code. |

```
http(s)://[Endpoint]/?Action=UpdateConnectorState &ProjectName=test &TopicName=test &ConnectorId=5c806a2f-84a0-47c3-8dda-d8fa2852de92 &State=STOPPED
```

```json
 "RequestId":"2023450128243103u",
<RequestId>2023450128243103u</RequestId>
```

| HttpCo de | Error code | Error message | Description |
|---|---|---|---|
| 400 | InvalidParameter | InvalidParameter | %s |
| 400 | NoPermission | NoPermission | %s |
| 400 | ResourceAlreadyExi st | ResourceAlreadyExist | %s |
| 400 | ResourceNotFound | ResourceNotFound | %s |
| 500 | OdpsServiceError | OdpsServiceError | %s |
| 502 | ApiProxyServiceErr or | ApiProxyServiceError | %s |
| 502 | InternalServerError | InternalServerError | %s |

### 1.7 GetShardDetail

You can call the GetShardDetail operation to retrieve shard information. The GetShardDetail operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the Common parameters topic.

| Paramet er name | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| RegionId | String | Query | Yes | cn-wuhan | The region ID. |
| ProjectNa me | String | Query | Yes | test | The name of the project. |
| TopicNam e | String | Query | Yes | test | The name of the topic. |

| DataHub |   |   |   | Dev | eloper Guide·API referenc |
|---|---|---|---|---|---|

| Paramet er name | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| ShardIds | String | Query | Yes | 1 | The shard ID. |

**Return data**

| Parameter name | Type | Example | Description |
|---|---|---|---|
| List | Array | - | The returned list. |
| - LatestDataTim e | Long | 2024850282120 | The time when the data was last updated. |
| -RecordCount | Long | 1 | The number of records. |
| - LatestDataSeq uence | Long | 123 | The latest sequence. |
| -ShardId | String | 1 | The shard ID. |
| - OldestDataTim e | Long | 2024850282120 | The earliest time. |
| - OldestDataSeq uence | Long | 3 | The earliest point. |
| RequestId | String | 2024so03hs | The ID of the request. |
| Success | Boolean | true | The returned status code. |

```
http(s)://[Endpoint]/?Action=GetShardDetail &RegionId=cn-wuhan &ProjectName=test &TopicName=test &ShardIds=1
```

```json
 "RequestId":"2024so03hs",
 "List":[
   "ShardId":"1",
   "OldestDataTime":2024850282120,
   "OldestDataSequence":3,
   "LatestDataTime":2024850282120,
   "LatestDataSequence":123,
   "RecordCount":1
```

`],`

```xml
<RequestId>2024so03hs</RequestId> <List>
 <ShardId>1</ShardId>
 <OldestDataTime>2024850282120</OldestDataTime>
 <OldestDataSequence>3</OldestDataSequence>
 <LatestDataTime>2024850282120</LatestDataTime>
 <LatestDataSequence>123</LatestDataSequence>
 <RecordCount>1</RecordCount>
</List>
```

| HttpCo de | Error code | Error message | Description |
|---|---|---|---|
| 400 | InvalidParameter | InvalidParameter | %s |
| 400 | NoPermission | NoPermission | %s |
| 400 | ResourceAlreadyExi st | ResourceAlreadyExist | %s |
| 400 | ResourceNotFound | ResourceNotFound | %s |
| 500 | OdpsServiceError | OdpsServiceError | %s |
| 502 | ApiProxyServiceErr or | ApiProxyServiceError | %s |
| 502 | InternalServerError | InternalServerError | %s |

### 1.8 SplitShard

Calls the SplitShard operation to split a shard. The SplitShard operation does not have operation-specific request headers and uses only common request headers. For more information, see the Common request parameters topic.

| Paramet er name | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| RegionId | String | Query | No | cn-neimeng | The region ID. |
| ProjectNa me | String | Query | No | test pro _ | The project name. |
| TopicNam e | String | Query | No | test topic _ | The topic name. |
| ShardId | String | Query | No | 0 | The shard ID. |

**Response parameters**

| Parameter name | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 20240205113332c 90fc50b77cc9bf6 | The ID of the request. |
| Success | Boolean | true | The status of the request. |

```json
http(s)://[Endpoint]/?Action=SplitShard
 "RequestId":"20240205113332c90fc50b77cc9bf6",
<RequestId>20240205113332c90fc50b77cc9bf6</RequestId>
```

| HttpCo de | Error code | Error message | Description |
|---|---|---|---|
| 502 | InternalServerError | InternalServerError | %s |
| 400 | InvalidParameter | InvalidParameter | %s |
| 400 | NoPermission | NoPermission | %s |
| 500 | OdpsServiceError | OdpsServiceError | %s |
| 400 | ResourceAlreadyExi st | ResourceAlreadyExist | %s |
| 400 | ResourceNotFound | ResourceNotFound | %s |
| 502 | ApiProxyServiceErr or | ApiProxyServiceError | %s |

### 1.9 GetAlarmRule

Calls the GetAlarmRule operation to retrieve an alarm rule.

**Request header**

The GetAlarmRule operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" topic.

| Paramet er name | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| RegionId | String | Query | Yes | cn-wuhan | The region ID. |
| ProjectNa me | String | Query | Yes | test pro _ | The project name. |
| TopicNam e | String | Query | Yes | test topic _ | The topic name. |
| AlarmId | String | Query | Yes | 0473 | The alert ID. |

**Return data**

| Parameter name | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 20240205113332e 90fc50b77cc9bf5 | The ID of the request. |
| ProjectName | String | test pro _ | The project name. |

| Parameter name | Type | Example | Description |
|---|---|---|---|
| TopicName | String | test topic _ | The topic name. |
| Uid | String | 1230449303 | The UID information. |
| AlarmType | String | USER SUB READ D _ _ _ ELAY | The alert type. |
| Success | Boolean | true | The status code returned. |
| RegionId | String | cn-hang | The region ID. |
| CreateTime | Long | 1709871393001 | The time when the role is created. |
| UpdateTime | Long | 1709871393001 | The time when the role is updated. |
| Config | String | {} | The policy configuration information. |
| Rule | String | {} | The authorization rule. |

```
http(s)://[Endpoint]/?Action=GetAlarmRule &RegionId=cn-wuhan &ProjectName=test_pro &TopicName=test_topic &AlarmId=0473
```

```json
 "Uid":"1230449303",
 "RequestId":"20240205113332e90fc50b77cc9bf5",
 "ProjectName":"test_pro",
 "Config":"{}",
 "AlarmType":"USER_SUB_READ_DELAY",
 "CreateTime":1709871393001,
 "UpdateTime":1709871393001,
 "RegionId":"cn-hang",
 "Rule":"{}",
 "Success":true,
 "TopicName":"test_topic"
<Uid>1230449303</Uid> <RequestId>20240205113332e90fc50b77cc9bf5</RequestId> <ProjectName>test_pro</ProjectName> <Config>{}</Config> <AlarmType>USER_SUB_READ_DELAY</AlarmType> <CreateTime>1709871393001</CreateTime> <UpdateTime>1709871393001</UpdateTime> <RegionId>cn-hang</RegionId> <Rule>{}</Rule> <TopicName>test_topic</TopicName>
```

| HttpCo de | Error code | Error message | Description |
|---|---|---|---|
| 502 | ApiProxyServiceErr or | ApiProxyServiceError | %s |
| 502 | InternalServerError | InternalServerError | %s |
| 400 | InvalidParameter | InvalidParameter | %s |
| 400 | NoPermission | NoPermission | %s |
| 500 | OdpsServiceError | OdpsServiceError | %s |
| 400 | ResourceAlreadyExi st | ResourceAlreadyExist | %s |
| 400 | ResourceNotFound | ResourceNotFound | %s |

### 1.10 CreateKafkaGroup

You can call the CreateKafkaGroup operation to create a group. The CreateKafkaGroup operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the Common parameters topic.

| Paramet er | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| RegionId | String | Query | Yes | cn-wuhan | The region ID. |
| ProjectNa me | String | Query | Yes | test rpo _ | The project name. |
| GroupNam e | String | Query | Yes | test group _ | The group name. |
| Comment | String | Query | Yes | test comment _ | The group description. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 20240205113332e 90fc50b77cc9bf5 | The ID of the request. |
| Success | Boolean | true | The status. |

```json
http(s)://[Endpoint]/?Action=CreateKafkaGroup &RegionId=cn-wuhan &ProjectName=test_rpo &GroupName=test_group &Comment=test_comment
 "RequestId":"20240205113332e90fc50b77cc9bf5",
<RequestId>20240205113332e90fc50b77cc9bf5</RequestId>
```

| HttpCo de | Error code | Error message | Description |
|---|---|---|---|
| 400 | InvalidParameter | InvalidParameter | %s |
| 400 | NoPermission | NoPermission | %s |
| 400 | ResourceAlreadyExi st | ResourceAlreadyExist | %s |
| 400 | ResourceNotFound | ResourceNotFound | %s |
| 500 | OdpsServiceError | OdpsServiceError | %s |
| 502 | ApiProxyServiceErr or | ApiProxyServiceError | %s |
| 502 | InternalServerError | InternalServerError | %s |

### 1.11 CreateTopic

You can call the CreateTopic operation to create a topic. The CreateTopic operation does not have operation-specific request headers and uses only common request headers. For more information, see the Common request parameters topic.

| Paramet er name | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| RegionId | String | Query | Yes | cn-wu | The region ID. |
| ProjectNa me | String | Query | Yes | test pro _ | The project name. |
| TopicNam e | String | Query | Yes | test topic _ | The topic name. |
| RecordTyp e | String | Query | Yes | BLOB | The topic type. |
| RecordSch ema | String | Query | No | f1 | The record structure. |
| Comment | String | Query | Yes | test-comment | The description of the topic. |
| ShardCou nt | Integ er | Query | No | 10 | The total number of shards. |

| DataHub |   |   |   | Dev | eloper Guide·API referenc |
|---|---|---|---|---|---|

| Paramet er name | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Lifecycle | Integ er | Query | No | 3 | The lifecycle of the topic. |
| ExpandMo de | Boole an | Query | No | SPLIT EXTEND _ | The expansion mode. |
| EnableSch emaRegist ry | Boole an | Query | No | true | Specifies whether to enable multiple versions. |

**Return data**

| Parameter name | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 20240205113332e 90fc50b77cc9bf5 | The request ID. |
| ProjectName | String | test pro _ | The project name. |
| Success | Boolean | true | The status code returned. |
| TopicName | String | test topic _ | The topic name. |

```json
http(s)://[Endpoint]/?Action=CreateTopic &RegionId=cn-wu &ProjectName=test_pro &TopicName=test_topic &RecordType=BLOB &Comment=test-comment
 "RequestId":"20240205113332e90fc50b77cc9bf5",
 "ProjectName":"test_pro",
 "Success":true,
 "TopicName":"test_topic"
```

```xml
<RequestId>20240205113332e90fc50b77cc9bf5</RequestId> <ProjectName>test_pro</ProjectName> <TopicName>test_topic</TopicName>
```

| HttpCo de | Error code | Error message | Description |
|---|---|---|---|
| 400 | InvalidParameter | InvalidParameter | %s |
| 400 | NoPermission | NoPermission | %s |
| 400 | ResourceAlreadyExi st | ResourceAlreadyExist | %s |
| 400 | ResourceNotFound | ResourceNotFound | %s |
| 500 | OdpsServiceError | OdpsServiceError | %s |
| 502 | ApiProxyServiceErr or | ApiProxyServiceError | %s |
| 502 | InternalServerError | InternalServerError | %s |

### 1.12 MergeShard

You can call the MergeShard operation to merge shards. The MergeShard operation does not have operation-specific request headers and uses only common request headers. For more information, see Common parameters.

| Paramet er name | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| RegionId | String | Query | Yes | cn-wuhan | The region ID. |
| ProjectNa me | String | Query | Yes | test pro _ | The name of the project. |
| TopicNam e | String | Query | Yes | test topic _ | The name of the topic. |
| ShardId | String | Query | Yes | 1 | The shard ID. |
| NextShard Id | String | Query | Yes | 2 | The ID of the shard to be merged. |

**Response parameters**

| Parameter name | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 20240205113332e 90fc50b77cc9bf5 | The ID of the request. |
| Success | Boolean | true | The status code returned. |

```json
http(s)://[Endpoint]/?Action=MergeShard &RegionId=cn-wuhan &ProjectName=test_pro &TopicName=test_topic &ShardId=1 &NextShardId=2
 "RequestId":"20240205113332e90fc50b77cc9bf5",
<RequestId>20240205113332e90fc50b77cc9bf5</RequestId>
```

| HttpCo de | Error code | Error message | Description |
|---|---|---|---|
| 400 | InvalidParameter | InvalidParameter | %s |
| 400 | NoPermission | NoPermission | %s |
| 400 | ResourceAlreadyExi st | ResourceAlreadyExist | %s |
| 400 | ResourceNotFound | ResourceNotFound | %s |
| 500 | OdpsServiceError | OdpsServiceError | %s |
| 502 | InternalServerError | InternalServerError | %s |

| Developer Gui | de·API reference |   | DataHu |
|---|---|---|---|

| HttpCo de | Error code | Error message | Description |
|---|---|---|---|
| 502 | ApiProxyServiceErr or | ApiProxyServiceError | %s |

### 1.13 ExtendShard

You can call the ExtendShard operation to extend a shard. The ExtendShard operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" section of the Common parameters topic.

| Paramet er name | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| RegionId | String | Query | Yes | cn-wuhan | The region ID. |
| ProjectNa me | String | Query | Yes | test pro _ | The project name. |
| TopicNam e | String | Query | Yes | test topic _ | The topic name. |
| ShardCou nt | String | Query | Yes | 10 | The total number of shards. |

**Return data**

| Parameter name | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 20240205113332e 90fc50b77cc9bf5 | The request ID. |
| Success | Boolean | true | The returned status code. |

```
http(s)://[Endpoint]/?Action=ExtendShard &RegionId=cn-wuhan &ProjectName=test_pro &TopicName=test_topic &ShardCount=10
```

```json
 "RequestId":"20240205113332e90fc50b77cc9bf5",
<RequestId>20240205113332e90fc50b77cc9bf5</RequestId>
```

| HttpCo de | Error code | Error message | Description |
|---|---|---|---|
| 400 | InvalidParameter | InvalidParameter | %s |
| 400 | NoPermission | NoPermission | %s |
| 400 | ResourceAlreadyExi st | ResourceAlreadyExist | %s |
| 400 | ResourceNotFound | ResourceNotFound | %s |
| 500 | OdpsServiceError | OdpsServiceError | %s |
| 502 | InternalServerError | InternalServerError | %s |
| 502 | ApiProxyServiceErr or | ApiProxyServiceError | %s |

### 1.14 GetConsumerPlan

You can call the GetConsumerPlan operation to retrieve a collaborative consumption plan. The GetConsumerPlan operation does not have operation-specific request headers and uses only common request headers. For more information, see the documentation of common request parameters.

| Paramet er | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| RegionId | String | Query | Yes | cn-wuhan | The region ID. |
| ProjectNa me | String | Query | Yes | test pro _ | The project name. |

| Developer Gui | de·API re | ference |   |   | DataHu |
|---|---|---|---|---|---|

| Paramet er | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| TopicNam e | String | Query | Yes | test topic _ |   |
| Subscripti onId | String | Query | Yes | 1214SAFAGG | The subscription ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| WaitingShards | String | 3 | The number of shards waiting to be assigned. |
| OverShards | String | 1 | The inherited shards. |
| TransferShards | String | 2 | The shards being transferred. |
| ShardAssignm ents | Array | - | The shard information. |
| -ShardIds | String | 1 | The list of shards. |
| -ConsumerId | String | 3 | The consumer ID. |
| -IpAddress | String | 10.xx.xxx | The IP address. |
| -JoinTime | Long | 1709871393001 | The time when the consumer joined. |
| RequestId | String | 20240205113332e 90fc50b77cc9bf5 | The ID of the request. |
| Success | Boolean | true | The returned status code. |
| ConsumerCoun t | Integer | 33 | The total number of consumers. |

```
http(s)://[Endpoint]/?Action=GetConsumerPlan &RegionId=cn-wuhan &ProjectName=test_pro &TopicName=test_topic &SubscriptionId=1214SAFAGG
```

```json
 "OverShards":"1",
 "RequestId":"20240205113332e90fc50b77cc9bf5",
 "ConsumerCount":33,
 "WaitingShards":"3",
 "ShardAssignments":{
  "ConsumerId":"3",
  "IpAddress":"10.xx.xxx",
  "JoinTime":1709871393001,
  "ShardIds":"1"
```

`},`

```json
 "TransferShards":"2",
<OverShards>1</OverShards> <RequestId>20240205113332e90fc50b77cc9bf5</RequestId> <ConsumerCount>33</ConsumerCount> <WaitingShards>3</WaitingShards> <ShardAssignments>
 <ConsumerId>3</ConsumerId>
 <IpAddress>10.xx.xxx</IpAddress>
 <JoinTime>1709871393001</JoinTime>
 <ShardIds>1</ShardIds>
</ShardAssignments> <TransferShards>2</TransferShards>
```

| HttpCo de | Error code | Error message | Description |
|---|---|---|---|
| 502 | ApiProxyServiceErr or | ApiProxyServiceError | %s |
| 502 | InternalServerError | InternalServerError | %s |
| 400 | InvalidParameter | InvalidParameter | %s |
| 400 | NoPermission | NoPermission | %s |
| 500 | OdpsServiceError | OdpsServiceError | %s |
| 400 | ResourceAlreadyExi st | ResourceAlreadyExist | %s |
| 400 | ResourceNotFound | ResourceNotFound | %s |

### 1.15 AddTopicSchema

You can call the AddTopicSchema operation to add a topic schema. The AddTopicSchema operation does not have operation-specific request headers and uses only common request headers. For more information, see the Common request parameters topic.

| Paramet er name | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| RegionId | String | Query | Yes | cn-wuhan | The region ID. |
| ProjectNa me | String | Query | Yes | test | The project name. |
| TopicNam e | String | Query | Yes | test | The topic name. |
| RecordSch ema | String | Query | No | 1 | The table name. |

**Response parameters**

| Parameter name | Type | Example | Description |
|---|---|---|---|
| VersionId | String | 0 | The table version. |
| RequestId | String | 2038431830411 | The ID of the request. |
| Success | Boolean | true | The status code returned. |
| RecordSchema | String | [{a,f1}] | The table structure. |

```
http(s)://[Endpoint]/?Action=AddTopicSchema &RegionId=cn-wuhan &ProjectName=test &TopicName=test
```

```json
 "VersionId":"0",
 "RequestId":"2038431830411",
 "RecordSchema":"[{a,f1}]",
<VersionId>0</VersionId> <RequestId>2038431830411</RequestId> <RecordSchema>[{a,f1}]</RecordSchema>
```

| HttpCo de | Error code | Error message | Description |
|---|---|---|---|
| 400 | InvalidParameter | InvalidParameter | %s |
| 400 | NoPermission | NoPermission | %s |
| 400 | ResourceAlreadyExi st | ResourceAlreadyExist | %s |
| 400 | ResourceNotFound | ResourceNotFound | %s |
| 500 | OdpsServiceError | OdpsServiceError | %s |
| 502 | ApiProxyServiceErr or | ApiProxyServiceError | %s |
| 502 | InternalServerError | InternalServerError | %s |

### 1.16 ListKafkaGroup

Call the ListKafkaGroup operation to retrieve a list of Kafka groups. The ListKafkaGroup operation does not have operation-specific request headers and uses only common request headers. For more information, see the Common request parameters topic.

| Parameter name | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Quer y | Yes | cn-wuan | The region ID. |

| ProjectNa me | Strin g | Quer y | Yes | test | The project name. |
|---|---|---|---|---|---|
| PageSize | Integ er | Quer y | Yes | 1 | The number of entries per page. |
| PageNumb er | Integ er | Quer y | Yes | 1 | The page number. |

**Return data**

| Parameter name | Type | Example | Description |
|---|---|---|---|
| List | Array | - | The returned list. |
| -TopicList | String | [a] | The topic list. |
| -GroupName | String | test | The group name. |
| -Comment | String | test | The note. |
| -Creator | String | 23551 | The user who creates the snapshot. |
| -CreateTime | Long | 14957492821 | The time when the group was created. |
| - LastModifyTim e | Long | 14957492821 | The last modification time. |
| RequestId | String | 202450182021 | The ID of the request. |
| Success | Boolean | true | The return value. |
| TotalCount | Long | 1 | The total number of entries. |
| PageSize | Integer | 1 | The number of entries per page. |
| PageCount | Integer | 11 | The page number of the returned page. |
| PageNumber | Integer | 22 | The page number. |

```json
http(s)://[Endpoint]/?Action=ListKafkaGroup &RegionId=cn-wuan &ProjectName=test &PageSize=1 &PageNumber=1
 "TotalCount":1,
 "RequestId":"202450182021",
 "PageSize":1,
 "PageCount":11,
 "PageNumber":22,
 "List":[
   "GroupName":"test",
   "Comment":"test",
   "CreateTime":14957492821,
   "TopicList":"[a]",
   "Creator":"23551",
   "LastModifyTime":14957492821
```

`],`

```xml
<TotalCount>1</TotalCount> <RequestId>202450182021</RequestId> <PageSize>1</PageSize> <PageCount>11</PageCount> <PageNumber>22</PageNumber> <List>
 <GroupName>test</GroupName>
 <Comment>test</Comment>
 <CreateTime>14957492821</CreateTime>
 <TopicList></TopicList>
 <Creator>23551</Creator>
 <LastModifyTime>14957492821</LastModifyTime>
</List>
```

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | InvalidParameter | InvalidParameter | %s |
| 400 | NoPermission | NoPermission | %s |
| 400 | ResourceAlreadyExi st | ResourceAlreadyExist | %s |
| 400 | ResourceNotFound | ResourceNotFound | %s |
| 500 | OdpsServiceError | OdpsServiceError | %s |
| 502 | ApiProxyServiceErr or | ApiProxyServiceError | %s |
| 502 | InternalServerError | InternalServerError | %s |

2019-11-20

### 1.17 ResetSubscriptionOffset

Call the ResetSubscriptionOffset operation to reset the subscription offset. The ResetSubscriptionOffset operation does not have operation-specific request headers and uses only common request headers. For more information, see the Common request parameters topic.

| Paramet er name | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| ProjectNa me | String | Query | Yes | test pro _ | The name of the project. |
| TopicNam e | String | Query | Yes | test topic _ | The name of the topic. |
| Subscripti onId | String | Query | Yes | 1688026989418N073J | The subscription ID. |
| StartTime | Long | Query | Yes | 1709871393001 | The start time. |

**Response parameters**

| Parameter name | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 20240205113332e 90fc50b77cc9bf5 | The ID of the request. |
| Success | Boolean | true | The returned status code. |

```json
http(s)://[Endpoint]/?Action=ResetSubscriptionOffset &ProjectName=test_pro &TopicName=test_topic &SubscriptionId=1688026989418N073J &StartTime=1709871393001
 "RequestId":"20240205113332e90fc50b77cc9bf5",
<RequestId>20240205113332e90fc50b77cc9bf5</RequestId>
```

| HttpCo de | Error code | Error message | Description |
|---|---|---|---|
| 502 | ApiProxyServiceErr or | ApiProxyServiceError | %s |
| 502 | InternalServerError | InternalServerError | %s |
| 400 | InvalidParameter | InvalidParameter | %s |
| 400 | NoPermission | NoPermission | %s |
| 500 | OdpsServiceError | OdpsServiceError | %s |
| 400 | ResourceAlreadyExi st | ResourceAlreadyExist | %s |

| Developer Gui | de·API reference |   | DataHu |
|---|---|---|---|

| HttpCo de | Error code | Error message | Description |
|---|---|---|---|
| 400 | ResourceNotFound | ResourceNotFound | %s |

### 1.18 ListSubscriptions

You can call the ListSubscriptions operation to query the list of subscription IDs. The ListSubscriptions operation does not have operation-specific request headers and uses only common request headers. For more information, see the Common request parameters topic.

| Paramet er | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| PageNumb er | Integ er | Query | Yes | 1 | The page number. |
| PageSize | Integ er | Query | Yes | 10 | The number of entries returned per page. |
| RegionId | String | Query | Yes | cn-wuhan | The region ID. |
| ProjectNa me | String | Query | Yes | test pro _ | The project name. |
| TopicNam e | String | Query | Yes | test topic _ | The topic name. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| List | Array | - | The list information. |
| -SubscriptionId | String | 1688026989418N0 73J | The subscription ID. |
| -State | Integer | 1 | The subscription status. |
| -Application | String | test | The subscription application. |
| -Type | String | USER | The subscription type. |
| -Creator | String | admin | The creator. |

| DataHub |   |   | Developer Guide·API referenc |
|---|---|---|---|
| Parameter | Type | Example | Description |
| -Comment | String | comment | The subscription description. |
| RequestId | String | 20240205113332e 90fc50b77cc9bf5 | The ID of the request. |
| PageNumber | String | 1 | The page number. |
| PageCount | String | 10 | The number of pages. |
| TotalCount | String | 100 | The total number. |
| PageSize | String | 10 | The number of entries per page. |
| Success | Boolean | true | The status code returned. |

```json
http(s)://[Endpoint]/?Action=ListSubscriptions &PageNumber=1 &PageSize=10 &RegionId=cn-wuhan &ProjectName=test_pro &TopicName=test_topic
 "TotalCount":"100",
 "RequestId":"20240205113332e90fc50b77cc9bf5",
 "PageCount":"10",
 "PageSize":"10",
 "PageNumber":"1",
 "List":{
  "Comment":"comment",
  "Type":"USER",
  "SubscriptionId":"1688026989418N073J",
  "State":1,
  "Creator":"admin",
  "Application":"test"
```

`},`

```xml
<TotalCount>100</TotalCount> <RequestId>20240205113332e90fc50b77cc9bf5</RequestId> <PageCount>10</PageCount> <PageSize>10</PageSize> <PageNumber>1</PageNumber> <List>
 <Comment>comment</Comment>
 <Type>USER</Type>
 <SubscriptionId>1688026989418N073J</SubscriptionId>
 <State>1</State>
 <Creator>admin</Creator>
 <Application>test</Application>
</List>
```

| HttpCo de | Error code | Error message | Description |
|---|---|---|---|
| 502 | ApiProxyServiceErr or | ApiProxyServiceError | %s |
| 502 | InternalServerError | InternalServerError | %s |
| 400 | InvalidParameter | InvalidParameter | %s |
| 400 | NoPermission | NoPermission | %s |
| 500 | OdpsServiceError | OdpsServiceError | %s |
| 400 | ResourceAlreadyExi st | ResourceAlreadyExist | %s |
| 400 | ResourceNotFound | ResourceNotFound | %s |

### 1.19 ReloadConnector

Call the ReloadConnector operation to restart a connector. The ReloadConnector operation does not have operation-specific request headers and uses only common request headers. For more information, see the Common request parameters topic.

| Paramet er name | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| ProjectNa me | String | Query | Yes | test pro _ | The name of the project. |

|   | DataHub |   |   |   | Dev | eloper Guide·API referenc | e |
|---|---|---|---|---|---|---|---|

| Paramet er name | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| TopicNam e | String | Query | Yes | test topic _ | The name of the topic. |
| ConnectorI d | String | Query | Yes | 21414215FFGG | The connector ID. |
| ShardId | String | Query | Yes | 1 | The shard ID. |

**Response parameters**

| Parameter name | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 20240205113332e 90fc50b77cc9bf5 | The request ID. |
| Success | String | true | The returned status code. |

```json
http(s)://[Endpoint]/?Action=ReloadConnector &ProjectName=test_pro &TopicName=test_topic &ConnectorId=21414215FFGG &ShardId=1
 "RequestId":"20240205113332e90fc50b77cc9bf5",
 "Success":"true"
<RequestId>20240205113332e90fc50b77cc9bf5</RequestId>
```

| HttpCo de | Error code | Error message | Description |
|---|---|---|---|
| 400 | InvalidParameter | InvalidParameter | %s |

| Developer Gui | de·API reference |   | DataHu |
|---|---|---|---|

| HttpCo de | Error code | Error message | Description |
|---|---|---|---|
| 400 | NoPermission | NoPermission | %s |
| 400 | ResourceAlreadyExi st | ResourceAlreadyExist | %s |
| 400 | ResourceNotFound | ResourceNotFound | %s |
| 500 | OdpsServiceError | OdpsServiceError | %s |
| 502 | ApiProxyServiceErr or | ApiProxyServiceError | %s |
| 502 | InternalServerError | InternalServerError | %s |

### 1.20 DeleteSubscription

You can call the DeleteSubscription operation to delete a subscription. The DeleteSubscription operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the Common parameters topic.

| Paramet er name | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| RegionId | String | Query | Yes | cn-wuan | The region ID. |
| ProjectNa me | String | Query | Yes | project test _ | The name of the project. |
| TopicNam e | String | Query | Yes | test topic _ | The name of the topic. |
| Subscripti onId | String | Query | Yes | 12323535ID | The subscription ID. |

**Return data**

| Parameter name | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 20240205113332e 90fc50b77cc9bf5 | The ID of the request. |
| Success | Boolean | true | The returned status code. |

```json
http(s)://[Endpoint]/?Action=DeleteSubscription &RegionId=cn-wuan &ProjectName=project_test &TopicName=test_topic &SubscriptionId=12323535ID
 "RequestId":"20240205113332e90fc50b77cc9bf5",
<RequestId>20240205113332e90fc50b77cc9bf5</RequestId>
```

| HttpCo de | Error code | Error message | Description |
|---|---|---|---|
| 400 | InvalidParameter | InvalidParameter | %s |
| 400 | NoPermission | NoPermission | %s |
| 400 | ResourceAlreadyExi st | ResourceAlreadyExist | %s |
| 400 | ResourceNotFound | ResourceNotFound | %s |
| 500 | OdpsServiceError | OdpsServiceError | %s |
| 502 | ApiProxyServiceErr or | ApiProxyServiceError | %s |
| 502 | InternalServerError | InternalServerError | %s |

### 1.21 ListTopics

You can call the ListTopics operation to query a list of topics. The ListTopics operation does not have operation-specific request headers and uses only common request headers. For more information, see the Common request parameters topic.

| Paramet er | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| PageNumb er | Integ er | Query | Yes | 1 | The page number. |
| RegionId | String | Query | Yes | cn-uw | The region ID. |
| ProjectNa me | String | Query | Yes | test pro _ | The project name. |
| PageSize | Integ er | Query | Yes | 1 | The number of entries per page. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| List | Array | - | The list information. |
| -TopicName | String | test topic _ | The topic name. |
| -Creator | String | admin | The creator. |
| -Comment | String | test comment _ | The description of the topic. |
| -ShardCount | Integer | 1 | The total number of shards. |
| -RecordType | String | BLOB | The record type. |
| -Lifecycle | Integer | 3 | The lifecycle of the topic. |
| -CreateTime | Long | 1709871393001 | The creation timestamp. |
| -UpdateTime | Long | 1709871393001 | The update timestamp. |
| -Storage | Long | 1024 | The storage capacity. |
| RequestId | String | 20240205113332e 90fc50b77cc9bf5 | The request ID. |
| PageNumber | String | 1 | The page number. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| PageCount | String | 12 | The total number of pages. |
| TotalCount | String | 12 | The total number of entries. |
| PageSize | String | 1 | The number of entries per page. |
| Success | Boolean | true | The status code returned. |

```json
http(s)://[Endpoint]/?Action=ListTopics &PageNumber=1 &RegionId=cn-uw &ProjectName=test_pro &PageSize=1
 "TotalCount":"12",
 "RequestId":"20240205113332e90fc50b77cc9bf5",
 "PageCount":"12",
 "PageSize":"1",
 "PageNumber":"1",
 "List":{
  "Comment":"test_comment",
  "Storage":1024,
  "RecordType":"BLOB",
  "Lifecycle":3,
  "CreateTime":1709871393001,
  "UpdateTime":1709871393001,
  "Creator":"admin",
  "TopicName":"test_topic",
  "ShardCount":1
```

`},`

```xml
<TotalCount>12</TotalCount> <RequestId>20240205113332e90fc50b77cc9bf5</RequestId> <PageCount>12</PageCount> <PageSize>1</PageSize> <PageNumber>1</PageNumber> <List>
 <Comment>test_comment</Comment>
 <Storage>1024</Storage>
 <RecordType>BLOB</RecordType>
 <Lifecycle>3</Lifecycle>
 <CreateTime>1709871393001</CreateTime>
 <UpdateTime>1709871393001</UpdateTime>
 <Creator>admin</Creator>
 <TopicName>test_topic</TopicName>
 <ShardCount>1</ShardCount>
</List>
```

| HttpCo de | Error code | Error message | Description |
|---|---|---|---|
| 502 | ApiProxyServiceErr or | ApiProxyServiceError | %s |
| 502 | InternalServerError | InternalServerError | %s |
| 400 | InvalidParameter | InvalidParameter | %s |
| 400 | NoPermission | NoPermission | %s |
| 500 | OdpsServiceError | OdpsServiceError | %s |
| 400 | ResourceAlreadyExi st | ResourceAlreadyExist | %s |
| 400 | ResourceNotFound | ResourceNotFound | %s |
| 400 | ResourceOffline | ResourceOffline | %s |

### 1.22 GetSubscriptionOffset

You can call the GetSubscriptionOffset operation to retrieve subscription offsets. The GetSubscriptionOffset operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" topic.

| Paramet er | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| RegionId | String | Query | Yes | cn-wuhan | The region ID. |
| ProjectNa me | String | Query | Yes | test pro _ | The project name. |
| TopicNam e | String | Query | Yes | test topic _ | The topic name. |
| Subscripti onId | String | Query | Yes | 1688026989418N073J | The subscription ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| List | Array | - | The list information. |
| -ShardId | String | 1 | The shard ID. |
| -Timestamp | Long | 1709871393001 | The timestamp. |
| -Sequence | Long | 1253 | The sequence. |
| RequestId | String | 20240205113332e 90fc50b77cc9bf5 | The ID of the request. |
| Success | Boolean | true | The status code returned. |

```
http(s)://[Endpoint]/?Action=GetSubscriptionOffset &RegionId=cn-wuhan &ProjectName=test_pro &TopicName=test_topic &SubscriptionId=1688026989418N073J
```

```json
 "RequestId":"20240205113332e90fc50b77cc9bf5",
 "List":{
  "ShardId":"1",
  "Sequence":1253,
  "Timestamp":1709871393001
```

`},`

```xml
<RequestId>20240205113332e90fc50b77cc9bf5</RequestId> <List>
 <ShardId>1</ShardId>
 <Sequence>1253</Sequence>
 <Timestamp>1709871393001</Timestamp>
</List>
```

| HttpCo de | Error code | Error message | Description |
|---|---|---|---|
| 502 | ApiProxyServiceErr or | ApiProxyServiceError | %s |
| 502 | InternalServerError | InternalServerError | %s |
| 400 | InvalidParameter | InvalidParameter | %s |
| 400 | NoPermission | NoPermission | %s |
| 500 | OdpsServiceError | OdpsServiceError | %s |
| 400 | ResourceAlreadyExi st | ResourceAlreadyExist | %s |
| 400 | ResourceNotFound | ResourceNotFound | %s |

### 1.23 GetConnectorShardStatus

Call the GetConnectorShardStatus operation to retrieve the connector shard status. The GetConnectorShardStatus operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the Common parameters topic.

| Paramet er name | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| RegionId | String | Query | Yes | cn-wuhan | The region ID. |
| ProjectNa me | String | Query | Yes | test pro _ | The project name. |
| TopicNam e | String | Query | Yes | test topic _ | The topic name. |
| ConnectorI d | String | Query | Yes | 5c806a2f-84a0-47c3- 8dda-d8fa2852de9c | The connector ID. |

**Response parameters**

| Parameter name | Type | Example | Description |
|---|---|---|---|
| List | Array | - | The list information. |
| -ShardId | String | 0 | The shard ID. |
| - CurrentTimest amp | Long | 1709871393001 | The current time. |
| - CurrentSequen ce | Long | 0 | The current sequence. |
| -State | String | RUNNING | The shard synchronization status. |
| -DiscardCount | Long | 3 | The amount of dirty data. |
| - LastErrorMess age | String | - | The synchronization error message. |
| RequestId | String | 20240205113332e 90fc50b77cc9bf5 | The ID of the request. |
| DelayTime | Long | 1709871393001 | The latency. |
| Success | Boolean | true | The returned status code. |

```json
http(s)://[Endpoint]/?Action=GetConnectorShardStatus &RegionId=cn-wuhan &ProjectName=test_pro &TopicName=test_topic &ConnectorId=5c806a2f-84a0-47c3-8dda-d8fa2852de9c
 "RequestId":"20240205113332e90fc50b77cc9bf5",
 "List":{
  "ShardId":"0",
  "LastErrorMessage":"",
  "DiscardCount":3,
  "CurrentTimestamp":1709871393001,
  "State":"RUNNING",
  "CurrentSequence":0
```

`},`

```json
 "DelayTime":1709871393001,
<RequestId>20240205113332e90fc50b77cc9bf5</RequestId> <List>
 <ShardId>0</ShardId>
 <LastErrorMessage  />
 <DiscardCount>3</DiscardCount>
 <CurrentTimestamp>1709871393001</CurrentTimestamp>
 <State>RUNNING</State>
 <CurrentSequence>0</CurrentSequence>
</List> <DelayTime>1709871393001</DelayTime>
```

| HttpCo de | Error code | Error message | Description |
|---|---|---|---|
| 502 | ApiProxyServiceErr or | ApiProxyServiceError | %s |
| 502 | InternalServerError | InternalServerError | %s |
| 400 | InvalidParameter | InvalidParameter | %s |
| 400 | NoPermission | NoPermission | %s |
| 500 | OdpsServiceError | OdpsServiceError | %s |

| DataHub |   |   | Developer Guide·API referenc |
|---|---|---|---|
| HttpCo de | Error code | Error message | Description |
| 400 | ResourceAlreadyExi st | ResourceAlreadyExist | %s |
| 400 | ResourceNotFound | ResourceNotFound | %s |

### 1.24 GetTopicDataTrendByDay

You can call the GetTopicDataTrendByDay operation to retrieve the read and write traffic of a topic. The GetTopicDataTrendByDay operation does not have operation-specific request headers and uses only common request headers. For more information, see Common parameters.

| Paramet er name | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| RegionId | String | Query | Yes | cn-wujan | The ID of the region. |
| ProjectNa me | String | Query | Yes | test pro _ | The name of the project. |
| TopicNam e | String | Query | Yes | test topic _ | The name of the topic. |

**Response parameters**

| Parameter name | Type | Example | Description |
|---|---|---|---|
| List | Array | - | The list information. |
| -Day | String | 2021-11-20 | The date. |
| -Size | Float | 1024 | The size. |
| RequestId | String | 20240205113332e 90fc50b77cc9bf5 | The ID of the request. |
| Success | Boolean | true | The returned status code. |

```json
http(s)://[Endpoint]/?Action=GetTopicDataTrendByDay &RegionId=cn-wujan &ProjectName=test_pro &TopicName=test_topic
 "RequestId":"20240205113332e90fc50b77cc9bf5",
 "List":{
  "Size":1024.0,
  "Day":"2021-11-20"
```

`},`

```xml
<RequestId>20240205113332e90fc50b77cc9bf5</RequestId> <List>
 <Size>1024</Size>
 <Day>2021-11-20</Day>
</List>
```

| HttpCo de | Error code | Error message | Description |
|---|---|---|---|
| 400 | InvalidParameter | InvalidParameter | %s |
| 400 | NoPermission | NoPermission | %s |
| 400 | ResourceAlreadyExi st | ResourceAlreadyExist | %s |
| 400 | ResourceNotFound | ResourceNotFound | %s |
| 500 | OdpsServiceError | OdpsServiceError | %s |
| 502 | ApiProxyServiceErr or | ApiProxyServiceError | %s |
| 502 | InternalServerError | InternalServerError | %s |

### 1.25 GetSchemaByOdps

Call the GetSchemaByOdps operation to obtain the structure of an ODPS table. The GetSchemaByOdps operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the Common parameters topic.

| Paramet er name | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| RegionId | String | Query | Yes | cn-wuhan | The region ID. |
| Project | String | Query | Yes | test database _ | The ODPS database. |
| Table | String | Query | Yes | table name _ | The ODPS table. |
| AccessId | String | Query | Yes | accessId | The AccessId. |
| AccessKey | String | Query | Yes | accessKey | The AccessKey. |

**Response parameters**

| Parameter name | Type | Example | Description |
|---|---|---|---|
| List | Array | - | The list information. |
| -Name | String | atest | The name of a field. |
| -Type | String | int | The type of a field. |
| -AllowNull | Boolean | true | Specifies whether the field can be null. |
| -Comment | String | test comment _ | The description of the field. |
| RequestId | String | 20240205113332e 90fc50b77cc9bf5 | The ID of the request. |
| Success | Boolean | true | The returned status code. |

```json
http(s)://[Endpoint]/?Action=GetSchemaByOdps &RegionId=cn-wuhan &Project=test_database &Table=table_name &AccessId=accessId &AccessKey=accessKey
 "RequestId":"20240205113332e90fc50b77cc9bf5",
 "List":{
  "Comment":"test_comment",
  "Type":"int",
  "AllowNull":true,
  "Name":"atest"
```

`},`

```xml
<RequestId>20240205113332e90fc50b77cc9bf5</RequestId> <List>
 <Comment>test_comment</Comment>
 <Type>int</Type>
 <AllowNull>true</AllowNull>
 <Name>atest</Name>
</List>
```

| HttpCo de | Error code | Error message | Description |
|---|---|---|---|
| 502 | ApiProxyServiceErr or | ApiProxyServiceError | %s |
| 502 | InternalServerError | InternalServerError | %s |
| 400 | InvalidParameter | InvalidParameter | %s |
| 400 | NoPermission | NoPermission | %s |
| 500 | OdpsServiceError | OdpsServiceError | %s |
| 400 | ResourceAlreadyExi st | ResourceAlreadyExist | %s |
| 400 | ResourceNotFound | ResourceNotFound | %s |

### 1.26 UpdateTopicsForKafkaGroup

You can call the UpdateTopicsForKafkaGroup operation to update the topic list of a Kafka group. The UpdateTopicsForKafkaGroup operation does not have operation-specific request headers and uses only common request headers. For more information, see the Common parameters topic.

| Paramet er name | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| RegionId | String | Query | Yes | 20240205113332e90fc5 0b77cc9bf5 | The region ID. |
| ProjectNa me | String | Query | Yes | test pro _ | The name of the project. |
| GroupNam e | String | Query | Yes | test gro _ | The name of the group. |
| UpdateKaf kaGroupM ode | String | Query | Yes | ADD | The update mode of the Kafka group. |
| KafkaGrou pTopicList | Array | Query | Yes | test topic _ | The list of topics included in the group. |

**Response parameters**

| Parameter name | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 20240205113332e 90fc50b77cc9bf5 | The ID of the request. |
| Success | Boolean | true | The status code returned. |

```
http(s)://[Endpoint]/?Action=UpdateTopicsForKafkaGroup &RegionId=20240205113332e90fc50b77cc9bf5 &ProjectName=test_pro &GroupName=test_gro &UpdateKafkaGroupMode=ADD &KafkaGroupTopicList=test_topic
```

```json
 "RequestId":"20240205113332e90fc50b77cc9bf5",
<RequestId>20240205113332e90fc50b77cc9bf5</RequestId>
```

| HttpCo de | Error code | Error message | Description |
|---|---|---|---|
| 400 | InvalidParameter | InvalidParameter | %s |
| 400 | NoPermission | NoPermission | %s |
| 400 | ResourceAlreadyExi st | ResourceAlreadyExist | %s |
| 400 | ResourceNotFound | ResourceNotFound | %s |
| 500 | OdpsServiceError | OdpsServiceError | %s |
| 502 | ApiProxyServiceErr or | ApiProxyServiceError | %s |
| 502 | InternalServerError | InternalServerError | %s |

### 1.27 ListShards

You can call the ListShards operation to retrieve a list of shards. The ListShards operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" section of the Common parameters topic.

| Paramet er | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| RegionId | String | Query | Yes | cn-wuhan | The region ID. |
| ProjectNa me | String | Query | Yes | project test _ | The project name. |
| TopicNam e | String | Query | Yes | topic test _ | The topic name. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| List | Array | [] | The list of shards. |
| -ShardId | String | 1 | The shard ID. |
| -State | String | active | The shard status. |
| -RightShardId | String | 1 | The rightmost partition in the query result. |
| -LeftShardId | String | 2 | The leftmost partition in the query result. |
| RequestId | String | 20240205113332e 90fc50b77cc9bf5 | The request ID. |
| Success | Boolean | true | The status code returned. |

```json
http(s)://[Endpoint]/?Action=ListShards &RegionId=cn-wuhan &ProjectName=project_test &TopicName=topic_test
 "RequestId":"20240205113332e90fc50b77cc9bf5",
 "List":[
   "ShardId":"1",
   "RightShardId":"1",
   "State":"active",
   "LeftShardId":"2"
```

`],`

```xml
<RequestId>20240205113332e90fc50b77cc9bf5</RequestId> <List>
 <ShardId>1</ShardId>
 <RightShardId>1</RightShardId>
 <State>active</State>
 <LeftShardId>2</LeftShardId>
</List>
```

| HttpCo de | Error code | Error message | Description |
|---|---|---|---|
| 502 | InternalServerError | InternalServerError | %s |
| 400 | InvalidParameter | InvalidParameter | %s |
| 400 | NoPermission | NoPermission | %s |
| 500 | OdpsServiceError | OdpsServiceError | %s |
| 400 | ResourceAlreadyExi st | ResourceAlreadyExist | %s |
| 400 | ResourceNotFound | ResourceNotFound | %s |
| 502 | ApiProxyServiceErr or | ApiProxyServiceError | %s |
| 400 | ResourceOffline | ResourceOffline | %s |

### 1.28 GetTopicMetric

Call the GetTopicMetric operation to retrieve topic metric information. The GetTopicMetric operation does not have operation-specific request headers and uses only common request headers. For more information, see the Common request parameters topic.

| Paramet er | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| RegionId | String | Query | Yes | cn-han | The region ID. |
| ProjectNa me | String | Query | Yes | test pro _ | The project name. |
| StartTime | Long | Query | Yes | 1709871393001 | The start time. |

| Paramet er | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| EndTime | Long | Query | Yes | 1709871393002 | The end time. |
| Type | String | Query | Yes | BLOB | The topic type. |
| TopicNam e | String | Query | Yes | test pro _ | The topic name. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 20240205113332e 90fc50b77cc9bf5 | The request ID. |
| Success | Boolean | true | The status code returned. |

```json
http(s)://[Endpoint]/?Action=GetTopicMetric &RegionId=cn-han &ProjectName=test_pro &StartTime=1709871393001 &EndTime=1709871393002 &Type=BLOB &TopicName=test_pro
 "RequestId":"20240205113332e90fc50b77cc9bf5",
 "List":{
  "Read":"",
  "Write":"",
  "Ts":""
```

`},`

```xml
<RequestId>20240205113332e90fc50b77cc9bf5</RequestId> <List>
 <Read  />
 <Write  />
 <Ts  />
</List>
```

| HttpCo de | Error code | Error message | Description |
|---|---|---|---|
| 502 | ApiProxyServiceErr or | ApiProxyServiceError | %s |
| 502 | InternalServerError | InternalServerError | %s |
| 400 | InvalidParameter | InvalidParameter | %s |
| 400 | NoPermission | NoPermission | %s |
| 500 | OdpsServiceError | OdpsServiceError | %s |
| 400 | ResourceAlreadyExi st | ResourceAlreadyExist | %s |
| 400 | ResourceNotFound | ResourceNotFound | %s |

### 1.29 ListRegions

Call the ListRegions operation to obtain a list of regions. The ListRegions operation does not have operation-specific request headers and uses only common request headers. For more information, see the Common request parameters topic.

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| List | Array | - | The list information. |
| -RegionId | String | cn-wu | The ID of the region. |
| RequestId | String | 20240205113332e 90fc50b77cc9bf5 | The ID of the request. |
| Success | Boolean | true | The status code returned. |

```json
 "RequestId":"20240205113332e90fc50b77cc9bf5",
 "List":{
  "-Domain":{
   "Vpc":"",
   "Private":"",
   "Public":""
```

`},`

```json
  "RegionId":"cn-wu"
```

`},`

```xml
<RequestId>20240205113332e90fc50b77cc9bf5</RequestId> <List>
 <-Domain>
  <Vpc  />
  <Private  />
  <Public  />
 </-Domain>
 <RegionId>cn-wu</RegionId>
</List>
```

| HttpCo de | Error code | Error message | Description |
|---|---|---|---|
| 502 | ApiProxyServiceErr or | ApiProxyServiceError | %s |
| 502 | InternalServerError | InternalServerError | %s |
| 400 | InvalidParameter | InvalidParameter | %s |
| 400 | NoPermission | NoPermission | %s |
| 500 | OdpsServiceError | OdpsServiceError | %s |
| 400 | ResourceAlreadyExi st | ResourceAlreadyExist | %s |
| 400 | ResourceNotFound | ResourceNotFound | %s |

### 1.30 ResetConnectorOffset

You can call the ResetConnectorOffset operation to reset the connector offset. The ResetConnectorOffset operation does not have operation-specific request headers and uses only common request headers. For more information, see Common parameters.

| Paramet er name | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| ProjectNa me | String | Query | Yes | test pro _ | The name of the project. |
| TopicNam e | String | Query | Yes | test topic _ | The name of the topic. |
| ConnectorI d | String | Query | Yes | DSFHJFP132484 | The connector ID. |
| StartTime | Long | Query | Yes | 1709871393001 | The start time. |

**Return data**

| Parameter name | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 20240205113332e 90fc50b77cc9bf5 | The request ID. |

```json
http(s)://[Endpoint]/?Action=ResetConnectorOffset &ProjectName=test_pro &TopicName=test_topic &ConnectorId=DSFHJFP132484 &StartTime=1709871393001
 "RequestId":"20240205113332e90fc50b77cc9bf5"
<RequestId>20240205113332e90fc50b77cc9bf5</RequestId>
```

| HttpCo de | Error code | Error message | Description |
|---|---|---|---|
| 400 | InvalidParameter | InvalidParameter | %s |
| 400 | NoPermission | NoPermission | %s |
| 400 | ResourceAlreadyExi st | ResourceAlreadyExist | %s |
| 400 | ResourceNotFound | ResourceNotFound | %s |
| 500 | OdpsServiceError | OdpsServiceError | %s |
| 502 | ApiProxyServiceErr or | ApiProxyServiceError | %s |
| 502 | InternalServerError | InternalServerError | %s |

### 1.31 AppendField

You can call the AppendField operation to add fields. The AppendField operation does not have operation-specific request headers and uses only common request headers. For more information, see the Common request parameters topic.

| Paramet er | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| RegionId | String | Query | Yes | cn-wuhan | The region ID. |
| ProjectNa me | String | Query | Yes | test pro _ | The project name. |
| TopicNam e | String | Query | Yes | test topic _ | The topic name. |
| Fields | String | Query | Yes | f1 | Add fields. |

**Return data**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 20240205113332e 90fc50b77cc9bf5 | The region ID. |
| Success | Boolean | true | The returned status code. |
| ProjectName | String | test pro _ | The project name. |

| Developer Guide·A | PI reference |   | DataHu |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| TopicName | String | test topic _ | The topic name. |

Sample request

```
http(s)://[Endpoint]/?Action=AppendField &RegionId=cn-wuhan &ProjectName=test_pro &TopicName=test_topic &Fields=f1
```

Sample success response

```json
 "RequestId":"20240205113332e90fc50b77cc9bf5",
 "ProjectName":"test_pro",
 "Success":true,
 "TopicName":"test_topic"
<RequestId>20240205113332e90fc50b77cc9bf5</RequestId> <ProjectName>test_pro</ProjectName> <TopicName>test_topic</TopicName>
```

| HttpCo de | Error code | Error message | Description |
|---|---|---|---|
| 400 | InvalidParameter | InvalidParameter | %s |
| 400 | NoPermission | NoPermission | %s |
| 400 | ResourceAlreadyExi st | ResourceAlreadyExist | %s |
| 400 | ResourceNotFound | ResourceNotFound | %s |
| 500 | OdpsServiceError | OdpsServiceError | %s |
| 502 | ApiProxyServiceErr or | ApiProxyServiceError | %s |
| 502 | InternalServerError | InternalServerError | %s |

### 1.32 GetConnector

Call the GetConnector operation to retrieve connector information. The GetConnector operation does not have operation-specific request headers and uses only common request headers. For more information, see the Common request parameters topic.

| Paramet er | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| RegionId | String | Query | Yes | cn-wuhan | The region ID. |
| ProjectNa me | String | Query | Yes | test pro _ | The project name. |
| TopicNam e | String | Query | Yes | test topic _ | The topic name. |
| ConnectorI d | String | Query | Yes | FJA1324R41 | The connector ID. |

**Return data**

| Parameter | Type | Example | Description |
|---|---|---|---|
| DoneTime | String | 2024-03-08 12:00:00 | The time when the task was marked as done. |
| Type | String | SINK ODPS _ | The synchronization type. |
| RequestId | String | 20240205113332e 90fc50b77cc9bf5 | The request ID. |
| State | String | RUNNING | The status of the synchronization. |
| Config | String | {} | The synchronization configuration information. |
| ConnectorReco rdSchema | String | {f1,f2} | The connector fields. |
| TopicRecordSc hema | String | {f1,f2} | The topic table fields. |
| ImportFields | String | f1 | Import fields. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| ConnectorId | String | UFNSNL37981 | The connector ID. |
| CreateTime | String | 20240205113332e 90fc50b77cc9bf5 | The creation timestamp. |
| Creator | String | admin | The creator. |
| Success | Boolean | true | The status code returned. |

```json
http(s)://[Endpoint]/?Action=GetConnector &RegionId=cn-wuhan &ProjectName=test_pro &TopicName=test_topic &ConnectorId=FJA1324R41
 "DoneTime":"2024-03-08 12:00:00",
 "Type":"SINK_ODPS",
 "RequestId":"20240205113332e90fc50b77cc9bf5",
 "State":"RUNNING",
 "Config":"{}",
 "ImportFields":"f1",
 "CreateTime":"20240205113332e90fc50b77cc9bf5",
 "ConnectorRecordSchema":"{f1,f2}",
 "Creator":"admin",
 "TopicRecordSchema":"{f1,f2}",
 "Success":true,
 "ConnectorId":"UFNSNL37981"
```

```xml
<DoneTime>2024-03-08 12:00:00</DoneTime> <Type>SINK_ODPS</Type> <RequestId>20240205113332e90fc50b77cc9bf5</RequestId> <State>RUNNING</State> <Config>{}</Config> <ImportFields>f1</ImportFields> <CreateTime>20240205113332e90fc50b77cc9bf5</CreateTime> <ConnectorRecordSchema>{f1,f2}</ConnectorRecordSchema> <Creator>admin</Creator> <TopicRecordSchema>{f1,f2}</TopicRecordSchema> <ConnectorId>UFNSNL37981</ConnectorId>
```

| HttpCo de | Error code | Error message | Description |
|---|---|---|---|
| 400 | InvalidParameter | InvalidParameter | %s |
| 400 | NoPermission | NoPermission | %s |
| 400 | ResourceAlreadyExi st | ResourceAlreadyExist | %s |
| 400 | ResourceNotFound | ResourceNotFound | %s |
| 500 | OdpsServiceError | OdpsServiceError | %s |
| 502 | ApiProxyServiceErr or | ApiProxyServiceError | %s |
| 502 | InternalServerError | InternalServerError | %s |

### 1.33 AddProjectVpcWhiteList

You can call the AddProjectVpcWhiteList operation to add a project whitelist. The AddProjectVpcWhiteList operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" section of the Common parameters topic.

| Paramet er | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| RegionId | String | Query | Yes | cn wuhan _ | The region ID. |
| ProjectNa me | String | Query | Yes | test pro _ | The project name. |

| Developer Gu | ide·API re | ference |   |   | DataHu |
|---|---|---|---|---|---|

| Paramet er | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| VpcIds | String | Query | Yes | 123455 | The list of VPCs. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 20240205113332e 90fc50b77cc9bf5 | The request ID. |
| Success | Boolean | true | The status code returned. |

```json
http(s)://[Endpoint]/?Action=AddProjectVpcWhiteList &RegionId=cn_wuhan &ProjectName=test_pro &VpcIds=123455
 "RequestId":"20240205113332e90fc50b77cc9bf5",
<RequestId>20240205113332e90fc50b77cc9bf5</RequestId>
```

| HttpCo de | Error code | Error message | Description |
|---|---|---|---|
| 502 | ApiProxyServiceErr or | ApiProxyServiceError | %s |
| 502 | InternalServerError | InternalServerError | %s |
| 400 | InvalidParameter | InvalidParameter | %s |
| 400 | NoPermission | NoPermission | %s |

| DataHub |   |   | Developer Guide·API referenc |
|---|---|---|---|

| HttpCo de | Error code | Error message | Description |
|---|---|---|---|
| 500 | OdpsServiceError | OdpsServiceError | %s |
| 400 | ResourceAlreadyExi st | ResourceAlreadyExist | %s |
| 400 | ResourceNotFound | ResourceNotFound | %s |

### 1.34 GetTopic

Call the GetTopic operation to retrieve topic information. This operation uses common request headers without special request headers. For more information, see the common request parameters document.

| Paramet er | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| RegionId | String | Query | Yes | cn wuhan _ | The region ID. |
| ProjectNa me | String | Query | Yes | test pro _ | The project name. |
| TopicNam e | String | Query | Yes | test topic _ | The topic name. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Comment | String | comment | The topic description. |
| RequestId | String | 20240205113332e 90fc50b77cc9bf5 | The request ID. |
| ProjectName | String | test pro _ | The project name. |
| CreateTime | String | 1709871393001 | The creation time. |
| ExpandMode | Boolean | SPLIT EXTEND _ | The extension mode. |
| Lifecycle | Integer | 3 | The lifecycle. |
| Creator | String | admin | The creator. |

| Developer Guide·A | PI reference |   | DataHu |
|---|---|---|---|
| Parameter | Type | Example | Description |
| Success | Boolean | true | The request status. |
| TopicName | String | test topic _ | The topic name. |
| ShardCount | Integer | 10 | The number of shards. |
| Storage | Long | 1024 | The storage capacity. |
| RecordType | String | BLOB | The record type. |
| UpdateTime | String | 1709871393001 | The update time. |
| RecordSchema | String | {f1} | The schema field. |
| EnableSchema Registry | Boolean | true | Indicates whether multiple versions are enabled. |

```
http(s)://[Endpoint]/?Action=GetTopic &RegionId=cn_wuhan &ProjectName=test_pro &TopicName=test_topic
```

```json
 "Comment":"comment",
 "EnableSchemaRegistry":true,
 "RequestId":"20240205113332e90fc50b77cc9bf5",
 "ProjectName":"test_pro",
 "CreateTime":"1709871393001",
 "ExpandMode":false,
 "Lifecycle":3,
 "Creator":"admin",
 "Success":true,
 "TopicName":"test_topic",
 "ShardCount":10,
 "Storage":1024,
 "RecordType":"BLOB",
 "UpdateTime":"1709871393001",
 "RecordSchema":"{f1}"
<Comment>comment</Comment> <EnableSchemaRegistry>true</EnableSchemaRegistry> <RequestId>20240205113332e90fc50b77cc9bf5</RequestId> <ProjectName>test_pro</ProjectName> <CreateTime>1709871393001</CreateTime> <ExpandMode>false</ExpandMode> <Lifecycle>3</Lifecycle> <Creator>admin</Creator> <TopicName>test_topic</TopicName> <ShardCount>10</ShardCount> <Storage>1024</Storage> <RecordType>BLOB</RecordType> <UpdateTime>1709871393001</UpdateTime> <RecordSchema>{f1}</RecordSchema>
```

| HttpCo de | Error code | Error message | Description |
|---|---|---|---|
| 400 | InvalidParameter | InvalidParameter | %s |
| 400 | NoPermission | NoPermission | %s |
| 400 | ResourceAlreadyExi st | ResourceAlreadyExist | %s |
| 400 | ResourceNotFound | ResourceNotFound | %s |
| 500 | OdpsServiceError | OdpsServiceError | %s |
| 502 | ApiProxyServiceErr or | ApiProxyServiceError | %s |

| Developer Gui | de·API reference |   | DataHu |
|---|---|---|---|

| HttpCo de | Error code | Error message | Description |
|---|---|---|---|
| 502 | InternalServerError | InternalServerError | %s |

### 1.35 ListTopicSchema

Call the ListTopicSchema operation to retrieve a list of topic schemas. The ListTopicSchema operation does not have operation-specific request headers and uses only common request headers. For more information, see the Common request parameters topic.

| Paramet er | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| PageNumb er | Integ er | Query | Yes | 1 | The page number. |
| RegionId | String | Query | Yes | cn-wuahn | The region ID. |
| ProjectNa me | String | Query | Yes | test pro _ | The project name. |
| PageSize | Integ er | Query | Yes | 10 | The number of entries per page. |
| TopicNam e | String | Query | Yes | test topic _ | The topic name. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| List | Array | - | The list information. |
| -VersionId | String | 1 | The version ID. |
| - RecordSchema | String | {f1,f2} | The schema fields. |
| -Creator | String | admin | The creator. |
| -CreateTime | Long | 1709871393001 | The creation time. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 20240205113332e 90fc50b77cc9bf5 | The request ID. |
| Success | Boolean | true | The status code returned. |
| PageNumber | String | 1 | The number of entries per page. |
| PageSize | String | 10 | The page number. |
| TotalCount | String | 10 | The total number of entries in the list. |
| PageCount | String | 10 | The total number of returned pages. |

```json
http(s)://[Endpoint]/?Action=ListTopicSchema &PageNumber=1 &RegionId=cn-wuahn &ProjectName=test_pro &PageSize=10 &TopicName=test_topic
 "TotalCount":"10",
 "RequestId":"20240205113332e90fc50b77cc9bf5",
 "PageSize":"10",
 "PageCount":"10",
 "PageNumber":"1",
 "List":{
  "VersionId":"",
  "CreateTime":"",
  "Creator":"",
  "RecordSchema":""
```

`},`

```xml
<TotalCount>10</TotalCount> <RequestId>20240205113332e90fc50b77cc9bf5</RequestId> <PageSize>10</PageSize> <PageCount>10</PageCount> <PageNumber>1</PageNumber> <List>
 <VersionId  />
 <CreateTime  />
 <Creator  />
 <RecordSchema  />
</List>
```

| HttpCo de | Error code | Error message | Description |
|---|---|---|---|
| 400 | InvalidParameter | InvalidParameter | %s |
| 400 | NoPermission | NoPermission | %s |
| 400 | ResourceAlreadyExi st | ResourceAlreadyExist | %s |
| 400 | ResourceNotFound | ResourceNotFound | %s |
| 400 | ResourceOffline | ResourceOffline | %s |
| 500 | OdpsServiceError | OdpsServiceError | %s |
| 502 | ApiProxyServiceErr or | ApiProxyServiceError | %s |
| 502 | InternalServerError | InternalServerError | %s |

### 1.36 DeleteConnector

Calls the DeleteConnector operation to delete a connector.

**Request header**

The DeleteConnector operation does not have operation-specific request headers and uses only common request headers. For more information, see the Common request parameters topic.

| Paramet er | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| RegionId | String | Query | No | cn wuhan _ | The region ID. |
| ProjectNa me | String | Query | Yes | test pro _ | The name of the project. |

| DataHub |   |   |   | Dev | eloper Guide·API referenc |
|---|---|---|---|---|---|
| Paramet er | Typ e | Positi on | Require d | Example | Description |
| TopicNam e | String | Query | Yes | test topic _ | The name of the topic. |
| ConnectorI d | String | Query | Yes | 2039401Fk | The connector ID. |

**Return data**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 20240205113332e 90fc50b77cc9bf5 | The ID of the request. |
| Success | String | true | The request status. |

```json
http(s)://[Endpoint]/?Action=DeleteConnector &ProjectName=test_pro &TopicName=test_topic &ConnectorId=2039401Fk
 "RequestId":"20240205113332e90fc50b77cc9bf5",
 "Success":"true"
<RequestId>20240205113332e90fc50b77cc9bf5</RequestId>
```

| HttpCo de | Error code | Error message | Description |
|---|---|---|---|
| 400 | InvalidParameter | InvalidParameter | %s |
| 400 | NoPermission | NoPermission | %s |
| 400 | ResourceAlreadyExi st | ResourceAlreadyExist | %s |

|   | Developer Gui | de·API reference |   | DataHu | b |
|---|---|---|---|---|---|

| HttpCo de | Error code | Error message | Description |
|---|---|---|---|
| 400 | ResourceNotFound | ResourceNotFound | %s |
| 500 | OdpsServiceError | OdpsServiceError | %s |
| 502 | ApiProxyServiceErr or | ApiProxyServiceError | %s |
| 502 | InternalServerError | InternalServerError | %s |

### 1.37 ListConnectors

Call the ListConnectors operation to view connector list information. The ListConnectors operation does not have operation-specific request headers and uses only common request headers. For more information, see the Common request parameters topic.

| Paramet er | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| PageNumb er | Integ er | Query | Yes | 1 | The page number. |
| PageSize | Integ er | Query | Yes | 1 | The number of entries to return on each page. |
| RegionId | String | Query | Yes | cn-wu | The region ID. |
| ProjectNa me | String | Query | Yes | test project _ | The project name. |
| TopicNam e | String | Query | Yes | test topic _ | The topic name. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| List | Array | - | The list information. |
| -ConnectorId | String | 29FFSJ12410 | The connector ID. |
| -Type | String | SINK ODPS _ | The synchronization type. |
| -State | String | RUNNING | The status of the synchronization. |

| DataHub |   |   | Developer Guide·API referenc |
|---|---|---|---|
| Parameter | Type | Example | Description |
| -Creator | String | admin | The user who creates the snapshot. |
| -CreateTime | String | 1709871393001 | The creation timestamp. |
| -SubscriptionId | String | 213SSFJANFSAN | The subscription ID. |
| RequestId | String | 20240205113332e 90fc50b77cc9bf5 | The request ID. |
| PageNumber | String | 1 | The page number. |
| PageCount | String | 1 | The number of entries per page. |
| TotalCount | String | 10 | The total number of events. |
| PageSize | String | 1 | The page number of the returned page. |
| Success | Boolean | true | The status code returned. |

```
http(s)://[Endpoint]/?Action=ListConnectors &PageNumber=1 &PageSize=1 &RegionId=cn-wu &ProjectName=test_project &TopicName=test_topic
```

```json
 "TotalCount":"",
 "RequestId":"20240205113332e90fc50b77cc9bf5",
 "PageCount":"1",
 "PageSize":"1",
 "PageNumber":"1",
 "List":{
  "Type":"SINK_ODPS",
  "SubscriptionId":"213SSFJANFSAN",
  "State":"RUNNING",
  "CreateTime":"1709871393001",
  "Creator":"admin",
  "ConnectorId":"29FFSJ12410"
```

`},`

```xml
<TotalCount /> <RequestId>20240205113332e90fc50b77cc9bf5</RequestId> <PageCount>1</PageCount> <PageSize>1</PageSize> <PageNumber>1</PageNumber> <List>
 <Type>SINK_ODPS</Type>
 <SubscriptionId>213SSFJANFSAN</SubscriptionId>
 <State>RUNNING</State>
 <CreateTime>1709871393001</CreateTime>
 <Creator>admin</Creator>
 <ConnectorId>29FFSJ12410</ConnectorId>
</List>
```

| HttpCo de | Error code | Error message | Description |
|---|---|---|---|
| 502 | ApiProxyServiceErr or | ApiProxyServiceError | %s |
| 502 | InternalServerError | InternalServerError | %s |
| 400 | InvalidParameter | InvalidParameter | %s |
| 400 | NoPermission | NoPermission | %s |
| 500 | OdpsServiceError | OdpsServiceError | %s |
| 400 | ResourceAlreadyExi st | ResourceAlreadyExist | %s |
| 400 | ResourceNotFound | ResourceNotFound | %s |

### 1.38 CreateSubscription

You can call the CreateSubscription operation to create a subscription. The CreateSubscription operation does not have operation-specific request headers and uses only common request headers. For more information, see the Common request parameters topic.

| Paramet er | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| RegionId | String | Query | Yes | cn-wu | The region ID. |
| ProjectNa me | String | Query | Yes | test pro _ | The project name. |
| TopicNam e | String | Query | Yes | test topic _ | The topic name. |
| Applicatio n | String | Query | Yes | test | The subscription application. |
| Comment | String | Query | Yes | test sub _ | The subscription description. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| SubscriptionId | String | 2390FFDMDAB | The subscription ID. |
| RequestId | String | 20240205113332e 90fc50b77cc9bf5 | The ID of the request. |
| ProjectName | String | test pro _ | The project name. |
| Success | String | true | The returned status code. |
| TopicName | String | test topic _ | The topic name. |

```json
http(s)://[Endpoint]/?Action=CreateSubscription &RegionId=cn-wu &ProjectName=test_pro &TopicName=test_topic &Application=test &Comment=test_sub
 "SubscriptionId":"2390FFDMDAB",
 "RequestId":"20240205113332e90fc50b77cc9bf5",
 "ProjectName":"test_pro",
 "Success":"true",
 "TopicName":"test_topic"
<SubscriptionId>2390FFDMDAB</SubscriptionId> <RequestId>20240205113332e90fc50b77cc9bf5</RequestId> <ProjectName>test_pro</ProjectName> <TopicName>test_topic</TopicName>
```

| HttpCo de | Error code | Error message | Description |
|---|---|---|---|
| 400 | InvalidParameter | InvalidParameter | %s |
| 400 | NoPermission | NoPermission | %s |
| 400 | ResourceAlreadyExi st | ResourceAlreadyExist | %s |
| 400 | ResourceNotFound | ResourceNotFound | %s |
| 500 | OdpsServiceError | OdpsServiceError | %s |
| 502 | ApiProxyServiceErr or | ApiProxyServiceError | %s |
| 502 | InternalServerError | InternalServerError | %s |

### 1.39 DeleteKafkaGroup

You can call the DeleteKafkaGroup operation to delete a Kafka group. The DeleteKafkaGroup operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" section of the Common parameters topic.

| Paramet er | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| RegionId | String | Query | Yes | cn-wuhan | The region ID. |
| ProjectNa me | String | Query | Yes | project name _ | The project name. |
| GroupNam e | String | Query | Yes | group name _ | The group name. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 20240205113332e 90fc50b77cc9bf5 | The request ID. |
| Success | Boolean | true | The status code returned. |

```json
http(s)://[Endpoint]/?Action=DeleteKafkaGroup &RegionId=cn-wuhan &ProjectName=project_name &GroupName=group_name
 "RequestId":"20240205113332e90fc50b77cc9bf5",
<RequestId>20240205113332e90fc50b77cc9bf5</RequestId>
```

| HttpCo de | Error code | Error message | Description |
|---|---|---|---|
| 400 | InvalidParameter | InvalidParameter | %s |
| 400 | NoPermission | NoPermission | %s |
| 400 | ResourceAlreadyExi st | ResourceAlreadyExist | %s |
| 400 | ResourceNotFound | ResourceNotFound | %s |
| 500 | OdpsServiceError | OdpsServiceError | %s |
| 502 | ApiProxyServiceErr or | ApiProxyServiceError | %s |
| 502 | InternalServerError | InternalServerError | %s |

### 1.40 GetKafkaGroup

Call the GetKafkaGroup operation to retrieve Kafka group information. The GetKafkaGroup operation does not have operation-specific request headers and uses only common request headers. For more information, see the Common request parameters topic.

| Paramet er | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| RegionId | String | Query | Yes | cn hangzhou _ | The region ID. |
| ProjectNa me | String | Query | Yes | test pro _ | The project name. |
| GroupNam e | String | Query | Yes | test pro _ | The group name. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| TopicList | String | - | The topic list. |
| RequestId | String | 20240205113332e 90fc50b77cc9bf5 | The ID of the request. |
| Success | Boolean | true | Indicates whether the request was successful. |

|   | DataHub |   |   | Developer Guide·API referenc | e |
|---|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| ProjectName | String | test pro _ | The project name. |
| GroupName | String | test gro _ | The group name. |
| Comment | String | test comment _ | The description. |
| Creator | String | admin | The user who creates the group. |
| CreateTime | Long | 1709871393001 | The time when the group was created. |
| LastModifyTim e | Long | 1709871393001 | The last modification time. |

```json
http(s)://[Endpoint]/?Action=GetKafkaGroup &RegionId=cn_hangzhou &ProjectName=test_pro &GroupName=test_pro
 "GroupName":"test_gro",
 "Comment":"test_comment",
 "RequestId":"20240205113332e90fc50b77cc9bf5",
 "ProjectName":"test_pro",
 "CreateTime":1709871393001,
 "TopicList":"",
 "Creator":"admin",
 "LastModifyTime":1709871393001,
```

```xml
<GroupName>test_gro</GroupName> <Comment>test_comment</Comment> <RequestId>20240205113332e90fc50b77cc9bf5</RequestId> <ProjectName>test_pro</ProjectName> <CreateTime>1709871393001</CreateTime> <TopicList /> <Creator>admin</Creator> <LastModifyTime>1709871393001</LastModifyTime>
```

| HttpCo de | Error code | Error message | Description |
|---|---|---|---|
| 400 | InvalidParameter | InvalidParameter | %s |
| 400 | NoPermission | NoPermission | %s |
| 400 | ResourceAlreadyExi st | ResourceAlreadyExist | %s |
| 400 | ResourceNotFound | ResourceNotFound | %s |
| 500 | OdpsServiceError | OdpsServiceError | %s |
| 502 | ApiProxyServiceErr or | ApiProxyServiceError | %s |
| 502 | InternalServerError | InternalServerError | %s |

### 1.41 SampleShard

Call the SampleShard operation to sample a shard. The SampleShard operation does not have operation-specific request headers and uses only common request headers. For more information, see the Common request parameters topic.

| Paramet er | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| RegionId | String | Query | No | cn-wuhan | The region ID. |
| ProjectNa me | String | Query | Yes | test pro _ | The name of the project. |
| TopicNam e | String | Query | Yes | topic name _ | The name of the topic. |
| ShardId | String | Query | Yes | 0 | The shard ID. |

| DataHub |   |   |   | Dev | eloper Guide·API referenc |
|---|---|---|---|---|---|

| Paramet er | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| StartTime | Long | Query | Yes | 1709871393001 | The start time. |
| RecordCou nt | Long | Query | Yes | 100 | The number of records. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RecordList | String | {} | The list of records. |
| RequestId | String | 20240205113332e 90fc50b77cc9bf5 | The request ID. |
| RecordSchema | String | {f1,f2} | The record schema. |
| Success | String | ture | The returned status code. |

```json
http(s)://[Endpoint]/?Action=SampleShard &ProjectName=test_pro &TopicName=topic_name &ShardId=0 &StartTime=1709871393001 &RecordCount=100
 "RecordList":"{}",
 "RequestId":"20240205113332e90fc50b77cc9bf5",
 "RecordSchema":"{f1,f2}",
 "Success":"ture"
<RecordList>{}</RecordList> <RequestId>20240205113332e90fc50b77cc9bf5</RequestId> <RecordSchema>{f1,f2}</RecordSchema> <Success>ture</Success>
```

| HttpCo de | Error code | Error message | Description |
|---|---|---|---|
| 400 | InvalidParameter | InvalidParameter | %s |
| 400 | NoPermission | NoPermission | %s |
| 400 | ResourceAlreadyExi st | ResourceAlreadyExist | %s |
| 400 | ResourceNotFound | ResourceNotFound | %s |
| 500 | OdpsServiceError | OdpsServiceError | %s |
| 502 | ApiProxyServiceErr or | ApiProxyServiceError | %s |
| 502 | InternalServerError | InternalServerError | %s |

### 1.42 GetUserStorage

You can call the GetUserStorage operation to retrieve the storage capacity of a project. The GetUserStorage operation does not have operation-specific request headers and uses only common request headers. For more information, see the Common request parameters section of the Common parameters topic.

| Paramet er name | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| RegionId | String | Query | Yes | cn hangzhou _ | The region ID. |
| ProjectNa me | String | Query | Yes | test pro _ | The name of the project. |

**Response parameters**

| Parameter name | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 20240205113332e 90fc50b77cc9bf5 | The ID of the request. |
| ProjectName | String | test pro _ | The name of the project. |
| CreateTime | String | 1709871393001 | The creation time. |

| Parameter name | Type | Example | Description |
|---|---|---|---|
| UpdateTime | String | 1709871393001 | The update time. |
| Comment | String | test pro _ | The description. |
| Creator | String | admin | The creator. |
| Success | Boolean | true | The status of the response. |
| Storage | Long | 1024 | The storage information. |

```json
http(s)://[Endpoint]/?Action=GetProject &RegionId=cn_hangzhou &ProjectName=test_pro
 "Comment":"test_pro",
 "Storage":1024,
 "RequestId":"20240205113332e90fc50b77cc9bf5",
 "ProjectName":"test_pro",
 "CreateTime":"1709871393001",
 "UpdateTime":"1709871393001",
 "Creator":"admin",
<Comment>test_pro</Comment> <Storage>1024</Storage> <RequestId>20240205113332e90fc50b77cc9bf5</RequestId> <ProjectName>test_pro</ProjectName> <CreateTime>1709871393001</CreateTime> <UpdateTime>1709871393001</UpdateTime> <Creator>admin</Creator>
```

| HttpCo de | Error code | Error message | Description |
|---|---|---|---|
| 502 | ApiProxyServiceErr or | ApiProxyServiceError | %s |
| 502 | InternalServerError | InternalServerError | %s |
| 400 | InvalidParameter | InvalidParameter | %s |
| 400 | NoPermission | NoPermission | %s |
| 500 | OdpsServiceError | OdpsServiceError | %s |
| 400 | ResourceAlreadyExi st | ResourceAlreadyExist | %s |
| 400 | ResourceNotFound | ResourceNotFound | %s |

### 1.43 GetProject

Call the GetProject operation to retrieve project information. The GetProject operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the Common parameters topic.

| Paramet er name | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| RegionId | String | Query | Yes | cn-wihan | The region ID. |
| ProjectNa me | String | Query | Yes | test ro _ | The name of the project. |

**Response parameters**

| Parameter name | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 20240205113332e 90fc50b77cc9bf5 | The ID of the request. |
| ProjectName | String | test pro _ | The name of the project. |
| CreateTime | String | 1709871393001 | The time when the project was created. |
| UpdateTime | String | 1709871393001 | The update time. |

| DataHub |   |   | Developer Guide·API referenc |
|---|---|---|---|

| Parameter name | Type | Example | Description |
|---|---|---|---|
| Comment | String | test comment _ | The note. |
| Creator | String | admin | The creator. |
| Success | Boolean | true | The returned status code. |
| Storage | Long | 1024 | The storage information. |

```json
http(s)://[Endpoint]/?Action=GetProject &RegionId=cn-wihan &ProjectName=test_ro
 "Comment":"test_comment",
 "Storage":1024,
 "RequestId":"20240205113332e90fc50b77cc9bf5",
 "ProjectName":"test_pro",
 "CreateTime":"1709871393001",
 "UpdateTime":"1709871393001",
 "Creator":"admin",
<Comment>test_comment</Comment> <Storage>1024</Storage> <RequestId>20240205113332e90fc50b77cc9bf5</RequestId> <ProjectName>test_pro</ProjectName> <CreateTime>1709871393001</CreateTime> <UpdateTime>1709871393001</UpdateTime> <Creator>admin</Creator>
```

| HttpCo de | Error code | Error message | Description |
|---|---|---|---|
| 502 | ApiProxyServiceErr or | ApiProxyServiceError | %s |
| 502 | InternalServerError | InternalServerError | %s |
| 400 | InvalidParameter | InvalidParameter | %s |
| 400 | NoPermission | NoPermission | %s |
| 500 | OdpsServiceError | OdpsServiceError | %s |
| 400 | ResourceAlreadyExi st | ResourceAlreadyExist | %s |
| 400 | ResourceNotFound | ResourceNotFound | %s |

### 1.44 ListTopicsByKafkaGroup

You can call the ListTopicsByKafkaGroup operation to query the list of topics in a Kafka group. The ListTopicsByKafkaGroup operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the Common parameters topic.

| Paramet er name | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| RegionId | String | Query | Yes | cn-hangzhou | The region ID. |
| ProjectNa me | String | Query | Yes | test project _ | The name of the project. |
| GroupNam e | String | Query | Yes | test group _ | The name of the group. |
| PageSize | Integ er | Query | Yes | 1 | The number of entries per page. |
| PageNumb er | Integ er | Query | Yes | 10 | The page number. |

**Response parameters**

| Parameter name | Type | Example | Description |
|---|---|---|---|
| List | String | - | The list information. |

| DataHub |   |   | Developer Guide·API referenc |
|---|---|---|---|

| Parameter name | Type | Example | Description |
|---|---|---|---|
| RequestId | String | B9CC4E36-8E16- 5628-BC69- C9DC167648CF | The request ID. |
| Success | Boolean | true | The returned status code. |
| TotalCount | Long | 100 | The total number of entries. |
| PageSize | Integer | 1 | The number of entries per page. |
| PageCount | Integer | 10 | The total number of pages. |
| PageNumber | Integer | 10 | The page number. |

```json
http(s)://[Endpoint]/?Action=ListTopicsByKafkaGroup &RegionId=cn-hangzhou &ProjectName=test_project &GroupName=test_group &PageSize=1 &PageNumber=
 "TotalCount":100,
 "RequestId":"B9CC4E36-8E16-5628-BC69-C9DC167648CF",
 "PageSize":1,
 "PageCount":"",
 "PageNumber":10,
 "List":"",
```

```xml
<TotalCount>100</TotalCount> <RequestId>B9CC4E36-8E16-5628-BC69-C9DC167648CF</RequestId> <PageSize>1</PageSize> <PageCount /> <PageNumber>10</PageNumber> <List />
```

| HttpCo de | Error code | Error message | Description |
|---|---|---|---|
| 400 | InvalidParameter | InvalidParameter | %s |
| 400 | NoPermission | NoPermission | %s |
| 400 | ResourceAlreadyExi st | ResourceAlreadyExist | %s |
| 400 | ResourceNotFound | ResourceNotFound | %s |
| 500 | OdpsServiceError | OdpsServiceError | %s |
| 502 | ApiProxyServiceErr or | ApiProxyServiceError | %s |
| 502 | InternalServerError | InternalServerError | %s |

### 1.45 UpdateConnectorField

You can call the UpdateConnectorField operation to update synchronization fields. The UpdateConnectorField operation does not have operation-specific request headers and uses only common request headers. For more information, see the Common parameters topic.

| Paramet er | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| RegionId | String | Query | Yes | cn-wuhan | The region ID. |
| ProjectNa me | String | Query | Yes | test pro _ | The project name. |
| GroupNam e | String | Query | Yes | test group _ | The group name. |
| PageSize | Integ er | Query | Yes | 1 | The number of entries per page. |

| DataHub |   |   |   | Dev | eloper Guide·API referenc |
|---|---|---|---|---|---|

| Paramet er | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| PageNumb er | Integ er | Query | Yes | 10 | The page number. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| List | String | - | The list information. |
| RequestId | String | 20240205113332e 90fc50b77cc9bf5 | The ID of the request. |
| Success | Boolean | true | The status code returned. |
| TotalCount | Long | 100 | The total number. |
| PageSize | Integer | 1 | The number of entries per page. |
| PageCount | Integer | 10 | The total number of pages. |
| PageNumber | Integer | 10 | The page number. |

```
http(s)://[Endpoint]/?Action=CheckServiceLinkedRoleForDeleting &RegionId=cn-wuhan &ProjectName=test_pro &GroupName=test_group &PageSize=1 &PageNumber=10
```

```json
 "TotalCount":100,
 "RequestId":"20240205113332e90fc50b77cc9bf5",
 "PageSize":1,
 "PageCount":10,
 "PageNumber":10,
 "List":"",
<TotalCount>100</TotalCount> <RequestId>20240205113332e90fc50b77cc9bf5</RequestId> <PageSize>1</PageSize> <PageCount>10</PageCount> <PageNumber>10</PageNumber> <List />
```

| HttpCo de | Error code | Error message | Description |
|---|---|---|---|
| 400 | InvalidParameter | InvalidParameter | %s |
| 400 | NoPermission | NoPermission | %s |
| 400 | ResourceAlreadyExi st | ResourceAlreadyExist | %s |
| 400 | ResourceNotFound | ResourceNotFound | %s |
| 500 | OdpsServiceError | OdpsServiceError | %s |
| 502 | ApiProxyServiceErr or | ApiProxyServiceError | %s |
| 502 | InternalServerError | InternalServerError | %s |

### 1.46 ListProjects

Call the ListProjects operation to retrieve a list of projects. The ListProjects operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" topic.

**Request syntax**

```
  GET /projects HTTP/1.1
```

| Paramet er name | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| PageNumb er | Integ er | Query | Yes | 0 | The page number to return. |
| RegionId | String | Query | Yes | cn-wuhan | The region ID. |
| PageSize | Integ er | Query | Yes | 10 | The number of entries per page. |

**Response parameters**

| Parameter name | Type | Example | Description |
|---|---|---|---|
| List | Array |   | The list information. |
| -ProjectName | String | test project _ | The name of the project. |
| -Creator | String | admin | The user who creates the project. |
| -Comment | String | Remarks | The description. |
| -CreateTime | Long | 1704692006131 | The time when the project was created. |
| -UpdateTime | Long | 1704692006131 | The time when the project was updated. |
| RequestId | String | 201805081749219 9d6650a00000039 | The ID of the request. |
| PageNumber | String | 0 | The page number returned. |
| PageCount | String | 10 | The total number of pages. |
| TotalCount | String | 100 | The total number of entries. |
| PageSize | String | 10 | The number of entries per page. |
| Success | Boolean | true | The status code returned. |

```json
http(s)://[Endpoint]/?Action=ListProjects &PageNumber= &RegionId= &PageSize=
 "TotalCount":"100",
 "RequestId":"2018050817492199d6650a00000039",
 "PageCount":"10",
 "PageSize":"10",
 "PageNumber":"0",
 "List":{
  "Comment":"Description",
  "ProjectName":"test_project",
  "CreateTime":1704692006131,
  "UpdateTime":1704692006131,
  "Creator":"admin"
```

`},`

```xml
<TotalCount>100</TotalCount> <RequestId>2018050817492199d6650a00000039</RequestId> <PageCount>10</PageCount> <PageSize>10</PageSize> <PageNumber>0</PageNumber> <List>
 <Comment>Description</Comment>
 <ProjectName>test_project</ProjectName>
 <CreateTime>1704692006131</CreateTime>
 <UpdateTime>1704692006131</UpdateTime>
 <Creator>admin</Creator>
</List>
```

### 1.47 DeleteProject

Call the DeleteProject operation to delete a project. The DeleteProject operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" section of the Common parameters topic.

| Paramet er | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| RegionId | String | Query | Yes | cn-hangzhou | The region ID. |
| ProjectNa me | String | Query | Yes | test project _ | The project name. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 201805081749219 9d6650a00000039 | The request ID. |
| Success | Boolean | true | The status code returned. |

```json
http(s)://[Endpoint]/?Action=DeleteProject &RegionId=cn-hangzhou &ProjectName=test_project
 "RequestId":"2018050817492199d6650a00000039",
<RequestId>2018050817492199d6650a00000039</RequestId>
```

### 1.48 CreateProject

You can call the CreateProject operation to create a project. The CreateProject operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" section of the Common parameters topic.

| Paramet er name | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| RegionId | String | Query | Yes | cn-wuhan | The region ID. |
| ProjectNa me | String | Query | Yes | test project _ | The project name. |
| Comment | String | Query | Yes | test comment _ | The project description. |

**Return data**

| Parameter name | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 201805081749219 9d6650a00000039 | The ID of the request. |
| Success | Boolean | true | The returned status code. |
| ProjectName | String | test project _ | The project name. |

```json
http(s)://[Endpoint]/?Action=CreateProject &RegionId=cn-wuhan &ProjectName=test_project &Comment=test_comment
 "RequestId":"2018050817492199d6650a00000039",
 "ProjectName":"test_project",
<RequestId>2018050817492199d6650a00000039</RequestId> <ProjectName>test_project</ProjectName>
```

### 1.49 CheckServiceLinkedRoleForDeleting

Calls the CheckServiceLinkedRoleForDeleting operation to check the service-linked role. The CheckServiceLinkedRoleForDeleting operation does not have operation-specific request headers and uses only common request headers. For more information, see the Common request parameters topic.

| Paramet er | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| RoleArn | String | Query | No | acs:ram::123456789012 ****:role/adminrole | The Alibaba Cloud Resource Name (ARN) of the specified role. |
| ServiceNa me | String | Query | No | service | The name of the service. |
| SPIRegionI d | String | Query | No | cn-wuhan | The region ID. |
| DeletionTa skId | String | Query | No | 1204 | The ID of the task. |
| AccountId | String | Query | No | 23845049102 | The account ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RoleUsages | Array |   |   |
| -Resources | Normal | test datahub _ | The resource set. |
| -Region | String | cn-wuhan | The region ID. |
| RequestId | String | 201805081749219 9d6650a00000039 | The ID of the request. |
| Deletable | Boolean | true | Indicates whether the role can be deleted. Valid values: true: The role can be deleted. false: The role cannot be deleted. |

```json
http(s)://[Endpoint]/?Action=CreateProject
 "RequestId":"2018050817492199d6650a00000039",
 "Deletable":true,
 "RoleUsages":{
  "Region":"cn-wuhan",
  "Resources":"test_datahub"
<RequestId>2018050817492199d6650a00000039</RequestId> <Deletable>true</Deletable> <RoleUsages>
 <Region>cn-wuhan</Region>
 <Resources>test_datahub</Resources>
</RoleUsages>
```

### 1.50 DeleteProjectVpcWhiteList

You can call the DeleteProjectVpcWhiteList operation to delete a project whitelist. The DeleteProjectVpcWhiteList operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the Common parameters topic.

| Paramet er name | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| RegionId | String | Query | Yes | cn-hangzhou | The region ID. |
| ProjectNa me | String | Query | Yes | test | The name of the project. |
| VpcIds | String | Query | Yes | 235112 | The list of VPC IDs. |

**Returned data**

| Parameter name | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 201805081749219 9d6650a00000039 | The ID of the request. |
| Success | Boolean | true | The returned status code. |

```json
http(s)://[Endpoint]/?Action=DeleteProjectVpcWhiteList &RegionId=cn-hangzhou &ProjectName=test &VpcIds=235112
 "RequestId":"2018050817492199d6650a00000039",
<RequestId>2018050817492199d6650a00000039</RequestId>
```

### 1.51 DeleteTopicSchema

You can call the DeleteTopicSchema operation to delete a topic schema. The DeleteTopicSchema operation does not have operation-specific request headers and uses only common request headers. For more information, see the Common request parameters topic.

| Paramet er | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| RegionId | String | Query | No | testhangzhou | The region ID. |
| ProjectNa me | String | Query | Yes | project test _ | The name of the project. |

| Paramet er | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| TopicNam e | String | Query | Yes | test topic _ | The name of the topic. |
| VersionId | String | Query | Yes | 1 | The version ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Success | Boolean | true | Indicates whether the request was successful. |
| RequestId | String | 201805081749219 9d6650a00000039 | The ID of the request. |

```
http(s)://[Endpoint]/?Action=DeleteTopicSchema &ProjectName=project_test &TopicName=test_topic &VersionId=1
```

Sample success response

```json
 "RequestId":"2018050817492199d6650a00000039",
<RequestId>2018050817492199d6650a00000039</RequestId>
```

### 1.52 GetAssumeRole

You can call the GetAssumeRole operation to retrieve a role. The GetAssumeRole operation does not have operation-specific request headers and uses only common request headers. For more information, see the documentation of common request parameters.

| Paramet er | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| RegionId | String | Query | No | cn-wuhan | The region ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 201805081749219 9d6650a00000039 | The request ID. |
| RoleId | String | 1293021 | The ID of the role. |
| HasAssumeRol e | String | admin | The role hash. |
| Success | Boolean | true | The status code returned. |

```json
http(s)://[Endpoint]/?Action=GetAssumeRole
 "RequestId":"2018050817492199d6650a00000039",
 "HasAssumeRole":"admin",
 "RoleId":"1293021",
<RequestId>2018050817492199d6650a00000039</RequestId> <HasAssumeRole>admin</HasAssumeRole> <RoleId>1293021</RoleId>
```

### 1.53 GetProjectVpcWhiteList

Calls the GetProjectVpcWhiteList operation to retrieve the project whitelist. The GetProjectVpcWhiteList operation does not have operation-specific request headers and uses only common request headers. For more information, see the Common request parameters topic.

| Paramet er | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| RegionId | String | Query | Yes | cn-wuhan | The region ID. |
| ProjectNa me | String | Query | Yes | test project _ | The project name. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| VpcWhiteList | String | 12378 | The VPC list. |
| RequestId | String | 201805081749219 9d6650a00000039 | The ID of the request. |
| ProjectName | String | test project _ | The project name. |
| CreateTime | String | 154110235 | The time when the whitelist was created. |
| UpdateTime | String | 154110236 | The time when the whitelist was updated. |
| Comment | String | comment | The remarks. |
| Creator | String | admin | The user who creates the whitelist. |
| Success | Boolean | true | The status code returned. |

```
http(s)://[Endpoint]/?Action=GetProjectVpcWhiteList &RegionId=cn-wuhan &ProjectName=test_project
```

```json
 "Comment":"comment",
 "RequestId":"2018050817492199d6650a00000039",
 "ProjectName":"test_project",
 "CreateTime":"154110235",
 "UpdateTime":"154110236",
 "Creator":"admin",
 "VpcWhiteList":"12378",
<Comment>comment</Comment> <RequestId>2018050817492199d6650a00000039</RequestId> <ProjectName>test_project</ProjectName> <CreateTime>154110235</CreateTime> <UpdateTime>154110236</UpdateTime> <Creator>admin</Creator> <VpcWhiteList>12378</VpcWhiteList>
```

### 1.54 InitializeDataImportProcess

You can call the InitializeDataImportProcess operation to initialize a process. The InitializeDataImportProcess operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" section of the Common parameters topic.

| Paramet er | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| RegionId | String | Query | Yes | cn-wuhan | The ID of the region. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 201805081749219 9d6650a00000039 | The ID of the request. |
| Success | Boolean | true | The status code returned. |
| TaskId | String | 12 | The ID of the task. |

```json
http(s)://[Endpoint]/?Action=InitializeDataImportProcess &RegionId=cn-wuhan
 "TaskId":"12",
 "RequestId":"2018050817492199d6650a00000039",
<TaskId>12</TaskId> <RequestId>2018050817492199d6650a00000039</RequestId>
```

## 2 SDK reference

### 2.1 SDK overview

This topic describes the SDKs that are provided by DataHub.

| Package name | Description |
|---|---|
| aliyun-sdk-datahub | The SDK is used to perform basic operations in DataHub. The SDK package provides API operations on basic objects in DataHub, including projects, topics, and shards. |

DataHub provides SDKs for Java, Python, Go, and C++. The following sections describe how to use DataHub SDKs for Java and Python.

### 2.2 Prerequisites

#### 2.2.1 Overview

Before you use MaxCompute SDKs, you must prepare the required environment. Create an Alibaba Cloud account that is authorized to access MaxCompute and obtain an AccessKey pair that consists of an AccessKey ID and an AccessKey secret. Obtain the endpoint of MaxCompute.

#### 2.2.2 Obtain an AccessKey pair

You can obtain an AccessKey pair in the Apsara Stack console.

**Obtain the AccessKey pair of a department**

To obtain the AccessKey pair of a department, perform the following steps:
1. Log on to the Apsara Stack console as an administrator.
2. In the left-side navigation pane, choose **User Center > Department Management**
3. On the Department Management page that appears, select the department whose
AccessKey pair you want to obtain and click **Get AccessKey**.

> **Note:** The AccessKey pair of a level-1 department is automatically generated by the system. Departments at lower levels of the hierarchy share the AccessKey pair of the level-1 department.

**Obtain the AccessKey pair of an individual account**

To obtain the AccessKey pair of an individual account, perform the following steps:
1. Log on to the Apsara Stack console as an administrator.
2. In the upper-right corner of the homepage, click the profile picture and then click **User**
**Information**.
On the page that appears, find the AccessKey ID in the AccessKey Pair section.
3. Click the **Show** icon in the ******************** column to view the AccessKey secret.

#### 2.2.3 Obtain endpoints

You can obtain the endpoints of DataHub in the Apsara Uni-manager Management Console.

**Procedure**

1. Open your Google Chrome browser.
2. In the address bar, enter the endpoint of the Apsara Uni-manager Management Console.
Press the ENTER key.
3. Enter your username and password.
4. Click **Log On** to go to the home page.
5. In the top navigation bar, choose **Products > Data Development and Services**.
6. Click **DataHub**. The DataHub console appears.
7. Obtain the DataHub endpoints in the **General Information** section on the right.

### 2.3 DataHub SDK for Java

#### 2.3.1 Overview

You do not need to download the DataHub SDK for Java. You only need to configure the SDK as a Maven dependency in a pom.xml file. Add the following dependency configuration to the pom.xml file:

```xml
<dependency>
    <groupId>com.aliyun.datahub</groupId>
    <artifactId>aliyun-sdk-datahub</artifactId>
    <version>2.9.2-public</version>
</dependency>
```

> **Note:** If you use DataHub V3.8.1 or earlier, use the preceding dependency configuration, where the SDK version is 2.9.2.

```xml
<dependency>
    <groupId>com.aliyun.datahub</groupId>
    <artifactId>aliyun-sdk-datahub</artifactId>
    <version>2.13.1-public</version>
</dependency>
```

> **Note:** If you use DataHub V3.8.1 or later, use the preceding dependency configuration, where the SDK version is 2.13.1.

#### 2.3.2 Preparations

To access DataHub, you must have an account that is authorized to access DataHub, the AccessKey for the account, and an endpoint of DataHub. If you are using Apsara Stack V2, obtain the endpoint from the CMDB system. If you are using Apsara Stack V3, obtain the endpoint from the Apsara Infrastructure Management Framework console. The sample code is shown as follows:

```
String accessId = "Your AccessId"; String accessKey = "Your AccessKey"; String endpoint = "http://XXXXXX"; // Specify the endpoint you have obtained. AliyunAccount account = new AliyunAccount(accessId, accessKey); DatahubConfiguration conf = new DatahubConfiguration(account, endpoint);
```

The following example shows how to initialize a DataHub client:

```
DatahubClient client = new DatahubClient(conf);
```

> **Note:** After the DataHub client is initialized, you can call the DatahubClient operation to access DataHub. You can use this client to perform all operations on DataHub because the client is thread-safe.

#### 2.3.3 Ingest tuple data

##### 2.3.3.1 Create a tuple topic

The sample code is shown as follows:

```
RecordSchema schema = new RecordSchema(); schema.addField(new Field("a", FieldType.STRING)); schema.addField(new Field("b", FieldType.BIGINT)); int shardCount = 5; int lifeCycle = 3; String topicName = "topic_example"; String topicDesc = "topic_example_desc"; client.createTopic(projectName, topicName, shardCount, lifeCycle, RecordType.TUPLE, sche ma, topicDesc); // Wait until the shards are in Active status. client.waitForShardReady(projectName, topicName);
```

> **Note:** In the sample code, lifeCycle indicates the time-to-live of each record in the topic.

##### 2.3.3.2 Obtain the list of shards

The sample code is shown as follows:

```
ListShardResult listShardResult = client.listShard(projectName, topicName);
```

##### 2.3.3.3 Write data into DataHub

The sample code is shown as follows:

```
List<RecordEntry> recordEntries = new ArrayList<RecordEntry>(); // Write into DataHub starting from any active shard returned by listShardResult. In thi s example, start from the first active shard. String shardId = listShardResult.getShards().get(0).getShardId(); RecordEntry entry = new RecordEntry(schema); entry.setString(0, "Test"); entry.setBigint(1, 5L); entry.setShardId(shardId); recordEntries.add(entry); PutRecordsResult result = client.putRecords(projectName, topicName, recordEntries); if (result.getFailedRecordCount() ! = 0) {
    List<ErrorEntry> errors = result.getFailedRecordError();
    // Process records failed to be written into DataHub.
    for (ErrorEntry e : result.getFailedRecordError()) {
       if (! e.getErrorcode().equals(“MalformedRecord”)) { // Retry the operation except
that the MalformedRecord, NoSuchProject, and NoSuchTopic errors occur.}
```

> **Note:** A request body size cannot exceed 4 MB. For more information, see Data ingestion methods.

##### 2.3.3.4 Consume data

You can use this SDK to obtain the cursor that points to the first record to be consumed. The cursor type can be **OLDEST**, **LATEST**, or **SYSTEM_TIME**. OLDEST: the cursor that points to the earliest record in DataHub. LATEST: the cursor that points to the latest record in DataHub. SYSTEM_TIME: the cursor that points to the first record ingested after the specified time. The sample code is shown as follows:

```java
GetCursorResult cursorRs = client.getCursor(projectName, topicName, shardId, GetCursorRequest.CursorType.OLDEST); // If you want to obtain the cursor that points to the earliest record ingested during t he last 24 hours, set CursorType to SYSTEM_TIME and set SYSTEM_TIME to System.currentTimeMillis() - 24 * 3600 * 1000 /* ms */. int limit = 100; String cursor = cursorRs.getCursor(); while (true) {
    try {
        GetBlobRecordsResult recordRs = client.getBlobRecords(projectName, topicName,
shardId, cursor, limit);
        List<BlobRecordEntry> recordEntries = recordRs.getRecords();
        if (recordEntries.size() == 0) {
            // Data has not been updated. Try again later.
            try {
                Thread.sleep(1000);
            } catch (InterruptedException e) {
                e.printStackTrace();
        // The cursor that points to the next record to be consumed is obtained.
        cursor = recordRs.getNextCursor();
    } catch (InvalidCursorException ex) {
        // The cursor is invalid or has expired. Specify another record as the beginning
of consumption.
        cursorRs = client.getCursor(projectName, topicName, shardId,
GetCursorRequest.CursorType.OLDEST);
        cursor = cursorRs.getCursor();
    } catch (DatahubClientException ex) {
        // An error occurred while obtaining the cursor. Try again.
        System.out.printf(ex.getMessage());
        ex.printStackTrace();
```

#### 2.3.4 Ingest blob data

##### 2.3.4.1 Create a blob topic

The sample code is shown as follows:

```
int shardCount = 5; int lifeCycle = 3; String topicName = "topic_example"; String topicDesc = "topic_example_desc"; client.createTopic(projectName, topicName, shardCount, lifeCycle, RecordType.BLOB, topic Desc); // Wait until the shards are in Active status. client.waitForShardReady(projectName, topicName);
```

##### 2.3.4.2 Obtain the list of shards

The sample code is shown as follows:

```
ListShardResult listShardResult = client.listShard(projectName, topicName);
```

##### 2.3.4.3 Write data into DataHub

The sample code is shown as follows:

```
List<BlobRecordEntry> recordEntries = new ArrayList<BlobRecordEntry>(); // Write into DataHub starting from any active shard returned by listShardResult. In thi s example, start from the first active shard. String shardId = listShardResult.getShards().get(0).getShardId(); String data = String.valueOf(System.currentTimeMillis()); BlobRecordEntry entry = new BlobRecordEntry(); entry.setData(data.getBytes()); entry.setShardId(shardId); recordEntries.add(entry); PutBlobRecordsResult result = client.putBlobRecords(projectName, topicName, recordEntries); if (result.getFailedRecordCount() ! = 0) {
    List<ErrorEntry> errors = result.getFailedRecordError();
    // Retry the operation except that the MalformedRecord, NoSuchProject, and
NoSuchTopic errors occur.
```

> **Note:** A request body size cannot exceed 4 MB.

##### 2.3.4.4 Consume data

The sample code is shown as follows:

```java
GetCursorResult cursorRs = client.getCursor(projectName, topicName, shardId, GetCursorRequest.CursorType.OLDEST); // If you want to obtain the cursor that points to the earliest record ingested during t he last 24 hours, set CursorType to SYSTEM_TIME and set SYSTEM_TIME to System.currentTimeMillis() - 24 * 3600 * 1000 /* ms */. int size = 100; String endCursor = cursorRes.GetCursor(); while (true) {
    try {
        GetBlobRecordsResult recordRs = client.getBlobRecords(projectName, topicName,
shardId, cursor, limit);
        List<BlobRecordEntry> recordEntries = recordRs.getRecords();
        if(records.size() == 0) {
            // Data has not been updated. Try again later.
            try {
                Thread.sleep(1000);
            } catch (InterruptedException e) {
                e.printStackTrace();
        // The cursor that points to the next record to be consumed is obtained.
        cursor = recordRs.getNextCursor();
    } catch (InvalidCursorException ex) {
        // The cursor is invalid or has expired. Specify another record as the beginning
of consumption.
        cursorRs = client.getCursor(projectName, topicName, shardId,
GetCursorRequest.CursorType.OLDEST);
        cursor = cursorRs.getCursor();
    } catch (DatahubClientException ex) {
        // An error occurred while obtaining the cursor. Try again.
        System.out.println(response.getMessage());
        e.printStackTrace();
```

> **Note:** Before being consumed, blob records that have been base64 encoded during ingestion must be decoded.

#### 2.3.5 Data ingestion methods

##### 2.3.5.1 Ingest data based on shard IDs

By using this method, you can write data into a specific shard and ensure that data is written into each shard in a specified order. The sample code is shown as follows:

```
// Create a client. Account account = new AliyunAccount("your access id", "your access key"); DatahubConfiguration conf = new DatahubConfiguration(account, "datahub endpoint"); DatahubClient client = new DatahubClient(conf); // Specify records to be ingested by DataHub. RecordSchema schema = client.getTopic("projectName", "topicName").getRecordSchema(); List<RecordEntry> recordEntries = new ArrayList<~>(); RecordEntry entry = new RecordEntry(schema); for (int i=0; i<entry.getFieldCount(); i++) {
    entry.setBigint(i, 1);
// Write into DataHub starting from any active shard returned by listShardResult. In thi s example, start from the first active shard. String shardId = listShardResult.getShards().get(0).getShardId(); entry.setShardId(shardId); recordEntries.add(entry); // Write data into DataHub. PutRecordsResult result = client.putRecords("projectName", "topicName", recordEntries);
```

##### 2.3.5.2 Ingest data based on hash values

Specify a 128-bit hash value produced by MD5 message-digest algorithm. Use the hash value to map associated records to a shard based on the hash key range of the shards. You cannot specify the ingestion order of records by using this method. The sample code is shown as follows:

```
// Create a client. Account account = new AliyunAccount("your access id", "your access key"); DatahubConfiguration conf = new DatahubConfiguration(account, "datahub endpoint"); DatahubClient client = new DatahubClient(conf); // Specify records to be ingested by DataHub. RecordSchema schema = client.getTopic("projectName", "topicName").getRecordSchema(); List<RecordEntry> recordEntries = new ArrayList<~>(); RecordEntry entry = new RecordEntry(schema); for (int i=0; i<entry.getFieldCount(); i++) {
    entry.setBigint(i, 1);
entry.setHashKey("7FFFFFFFFFFFFFFD7FFFFFFFFFFFFFFD"); recordEntries.add(entry); // Write the data into DataHub. PutRecordsResult result = client.putRecords("projectName", "topicName", recordEntries);
```

##### 2.3.5.3 Ingest data based on partition keys

Specify a partition key as a string. DataHub creates an MD5 hash from the string and maps the records to shards based on the hash key range of the shards. You do not need to provide hash values by using this method. The sample code is shown as follows:

```
// Create a client. Account account = new AliyunAccount("your access id", "your access key"); DatahubConfiguration conf = new DatahubConfiguration(account, "datahub endpoint"); DatahubClient client = new DatahubClient(conf); // Specify records to be ingested by DataHub. RecordSchema schema = client.getTopic("projectName", "topicName").getRecordSchema(); List<RecordEntry> recordEntries = new ArrayList<~>(); RecordEntry entry = new RecordEntry(schema); for (int i=0; i<entry.getFieldCount(); i++) {
    entry.setBigint(i, 1);
entry.setPartitionKey("TestPartitionKey"); recordEntries.add(entry); // Write the data into DataHub. PutRecordsResult result = client.putRecords("projectName", "topicName", recordEntries);
```

#### 2.3.6 Create a DataConnector

##### 2.3.6.1 Create a DataConnector for MaxCompute

The sample code is shown as follows:

```java
public void createDataConnector () {
    // Create a DataConnector for MaxCompute
    // Configure the destination MaxCompute table.
    String odpsProject = "datahub_test";
    String odpsTable = "test_table";
    String odpsEndpoint = "http://service-all.ext.odps.example.com/api";
    String tunnelEndpoint = "http://dt-all.ext.odps.example.com";
    OdpsDesc odpsDesc = new OdpsDesc();
    odpsDesc.setProject(odpsProject);
    odpsDesc.setTable(odpsTable);
    odpsDesc.setOdpsEndpoint(odpsEndpoint);
    odpsDesc.setTunnelEndpoint(tunnelEndpoint);
    odpsDesc.setAccessId(accessId);
    odpsDesc.setAccessKey(accessKey);
    odpsDesc.setPartitionMode(OdpsDesc.PartitionMode.USER_DEFINE);
    // Select some or all columns in the topic to be archived to MaxCompute. The
MaxCompute table must have the same columns in the same order as selected.
    List<String> jobIds = new ArrayList<String>();
    columnFields.add("f1");
    // By default, the partition mode is set to UserDefine.
    // If you set the partition mode to SYSTEM_TIME or EVENT_TIME, you must complete the
following configuration.
    // The configuration begins.
    int timeRange = 15;  // The partitioning interval, in minutes. Minimum value: 15.
    odpsDesc.setPartitionMode(OdpsDesc.PartitionMode.SYSTEM_TIME);
    odpsDesc.setTimeRange(timeRange);
    Map<String, String> partitionConfig = new LinkedHashMap<String, String>();
    // The partition key must be in the %Y%m%d%H%M format.
    partitionConfig.put("pt", "%Y%m%d");
    partitionConfig.put("ct", "%H%M");
    odpsDesc.setPartitionConfig(partitionConfig);
    // The configuration ends.
    client.createDataConnector(projectName, topicName, ConnectorType.SINK_ODPS,
columnFields, odpsDesc);
    // You can obtain the DataConnector status periodically, such as every 15 minutes, t
o check whether all shards are being archived properly to the destination platform.
    String shard = "0";
    GetDataConnectorShardStatusResult getDataConnectorShardStatusResult =
        client.getDataConnectorShardStatus(projectName, topicName,
ConnectorType.SINK_ODPS, shard);
    System.out.println(getDataConnectorShardStatusResult.getCurSequence());
    System.out.println(getDataConnectorShardStatusResult.getLastErrorMessage());
```

##### 2.3.6.2 Create a DataConnector for AnalyticDB or ApsaraDB RDS for MySQL

**ApsaraDB RDS for MySQL**

Sample code:

```java
public void createADSDataConnector () {
    // Create a DataConnector for AnalyticDB or ApsaraDB RDS for MySQL.
    // Configure the destination table.
    String dbHost = "127.0.0.1";
    int dbPort = 3306;
    String dbName = "db";
    String user = "123";
    String password = "123";
    String tableName = "table";
    DatabaseDesc desc = new DatabaseDesc();
    desc.setHost(dbHost);
    desc.setPort(dbPort);
    desc.setDatabase(dbName);
    desc.setUser(user);
    desc.setPassword(password);
    desc.setTable(tableName);
    // The maximum size of records that can be written to DataHub at a time. Unit: Byte.
    desc.setMaxCommitSize(512L);
    // Specify whether to ignore errors and continue the process.
    desc.setIgnore(true);
    // Select several or all columns in the topic to be synchronized to AnalyticDB or
ApsaraDB RDS for MySQL. The destination table must have the columns in the same order as selected.
    List<String> columnFields = new ArrayList<String>();
    columnFields.add("f1");
    client.createDataConnector(projectName, topicName, ConnectorType.SINK_ADS,
columnFields, desc);
    // Alternative: client.createDataConnector(projectName, topicName,
ConnectorType.SINK_MYSQL, columnFields, odpsDesc);
    // You can obtain the DataConnector status periodically, such as every 15 minutes, t
o check whether all shards are being properly synchronized to the destination table.
    String shard = "0";
    GetDataConnectorShardStatusResult getDataConnectorShardStatusResult =
        client.getDataConnectorShardStatus(projectName, topicName,
ConnectorType.SINK_ADS, shard);
    System.out.println(getDataConnectorShardStatusResult.getCurSequence());
    System.out.println(getDataConnectorShardStatusResult.getLastErrorMessage());
```

> **Note:** You cannot create DataConnectors for services that reside in virtual private clouds (VPCs) by using the SDK. You must create this type of DataConnectors in the DataHub console.

### 2.4 DataHub SDK for Python

#### 2.4.1 Install DataHub SDK for Python

Run the following commands to install DataHub SDK for Python.

**Quick installation**

```bash
$ sudo pip install pydatahub
```

**Install by using source code**

```bash
$ git clone https://github.com/aliyun/aliyun-datahub-sdk-python.git $ cd aliyun-datahub-sdk-python $ sudo python setup.py install
```

**Verify the installation**

```bash
$ python -c "from datahub import DataHub"
```

#### 2.4.2 Preparations

To access DataHub, you must have an account that is authorized to access DataHub, the AccessKey for the account, and an endpoint of DataHub. If you are using Apsara Stack V2, obtain the endpoint from the CMDB system. If you are using Apsara Stack V3, obtain the endpoint from the Apsara Infrastructure Management Framework console. The following example shows how to initialize DataHub configurations:

```java
import sys import traceback from datahub import DataHub from datahub.utils import Configer from datahub.models import Topic, RecordType, FieldType, RecordSchema, BlobRecord, Tuple Record, CursorType from datahub.errors import DatahubException, ObjectAlreadyExistException access_id = ***your access id*** access_key = ***your access key*** endpoint = ***your datahub server endpoint*** dh = DataHub(access_id, access_key, endpoint)
```

#### 2.4.3 Create topics

**Create a tuple topic**

You must specify a schema for a tuple topic. The following data types are supported: Table 1. Tuple data types

| Type | Description | Value range |
|---|---|---|
| Bigint | An 8-byte signed integer. Note Do not use the minimum value (- 9223372036854775808) because this is a system reserved value. | -9223372036854775807 to 9223372036854775807 |
| String | A string. Only UTF-8 encoding is supported. | The size of a string must not exceed 1 MB. |

| Boolean | One of two possible values. | Valid values: True and False, true and false, or 0 and 1. |
|---|---|---|
| Double | An 8-byte double-precision floating point. | -1.0 10 308 to 1.0 10 308 |
| TimeStamp | A timestamp. | It is accurate to milliseconds. |

The sample code is shown as follows:

```
topic = Topic(name=topic_name) topic.project_name = project_name topic.shard_count = 3 topic.life_cycle = 7 topic.record_type = RecordType.TUPLE topic.record_schema = RecordSchema.from_lists(['bigint_field', 'string_field', 'double_field', 'bool_field', 'time_field'], [Fie ldType.BIGINT, FieldType.STRING, FieldType.DOUBLE, FieldType.BOOLEAN, FieldType.TIMESTAMP]) try:
    dh.create_topic(topic)
    print "create topic success!"
    print "=======================================\n\n"
except ObjectAlreadyExistException, e:
    print "topic already exist!"
    print "=======================================\n\n"
except Exception, e:
    print traceback.format_exc()
    sys.exit(-1)
```

**Create a blob topic**

In a blob topic, a chunk of binary data is stored as a record. Records written into DataHub are Base64 encoded. The sample code is shown as follows:

```
topic = Topic(name=topic_name) topic.project_name = project_name topic.shard_count = 3 topic.life_cycle = 7 topic.record_type = RecordType.BLOB try:
    dh.create_topic(topic)
    print "create topic success!"
    print "=======================================\n\n"
except ObjectAlreadyExistException, e:
    print "topic already exist!"
    print "=======================================\n\n"
except Exception, e:
    print traceback.format_exc()
    sys.exit(-1)
```

#### 2.4.4 Write records into DataHub and subscribe applications to records

**subscribe applications to records**

**Obtain the list of shards**

You can use this SDK to obtain all shards in the topic.

```
shards = dh.list_shards(project_name, topic_name)
```

> **Note:** A list is returned and each entry in the list describes a shard in terms of the ID, status, starting hash key, and ending hash key.

**Write records into DataHub**

You can use this SDK to write records into a topic in DataHub.

```
failed_indexs = dh.put_records(project_name, topic_name, records)
```

> **Note:** The records request parameter is a list and each entry in the list represents a record. All records must be of the same data type, either tuple or blob. The subscript of the records that fail to be written into DataHub are returned.

The following sample code shows how to write tuple records into DataHub:

```
try:
    #Wait until all shards are in Active status.
    dh.wait_shards_ready(project_name, topic_name)
    print "shards all ready!!!"
    print "=======================================\n\n"
    topic = dh.get_topic(topic_name, project_name)
    print "get topic suc! topic=%s" % str(topic)
    if topic.record_type ! = RecordType.TUPLE:
        print "topic type illegal!"
        sys.exit(-1)
    print "=======================================\n\n"
    shards = dh.list_shards(project_name, topic_name)
    for shard in shards:
        print shard
    print "=======================================\n\n"
    records = []
    record0 = TupleRecord(schema=topic.record_schema, values=[1, 'yc1', 10.01, True, 145
5869335000000])
    record0.shard_id = shards[0].shard_id
    record0.put_attribute('AK', '47')
    records.append(record0)
    record1 = TupleRecord(schema=topic.record_schema)
    record1['bigint_field'] = 2
    record1['string_field'] = 'yc2'
    record1['double_field'] = 10.02
    record1['bool_field'] = False
    record1['time_field'] = 1455869335000011
    record1.shard_id = shards[1].shard_id
    records.append(record1)
    record2 = TupleRecord(schema=topic.record_schema)
    record2['bigint_field'] = 3
    record2['string_field'] = 'yc3'
    record2['double_field'] = 10.03
    record2['bool_field'] = False
    record2['time_field'] = 1455869335000013
    record2.shard_id = shards[2].shard_id
    records.append(record2)
    failed_indexs = dh.put_records(project_name, topic_name, records)
    print "put tuple %d records, failed list: %s" %(len(records), failed_indexs)
    #If you specify the failed_indexs parameter, we recommend that you retry writing the
failed records into DataHub.
    print "=======================================\n\n"
except DatahubException, e:
    print traceback.format_exc()
    sys.exit(-1)
else:
    sys.exit(-1)
```

**Obtain the cursor of a record**

You can use this SDK to obtain the cursor of a record. Valid values: **OLDEST**, **LATEST**, and
**SYSTEM_TIME**.
OLDEST: the cursor that points to the earliest record in DataHub. LATEST: the cursor that points to the latest record in DataHub. SYSTEM_TIME: the cursor that points to the first record ingested after the specified time.

```
cursor = dh.get_cursor(project_name, topic_name, CursorType.OLDEST, shard_id)
```

> **Note:** If you select SYSTEM_TIME, this SDK returns the cursor that points to the record ingested at the specified time. If no record is ingested at the specified time, the first record ingested after the time is returned.

**Consume records**

You can use this SDK to specify the cursor that points to a record where the consumption begins and specify the upper limit of records to be consumed. If fewer records exist than the specified limit, the actual number of records are returned.

```
dh.get_records(topic, shard_id, cursor, 10)
```

The following sample code shows how to consume tuple records:

```
try:
    #Wait until all shards are in Active status.
    dh.wait_shards_ready(project_name, topic_name)
    print "shards all ready!!!"
    print "=======================================\n\n"
    topic = dh.get_topic(topic_name, project_name)
    print "get topic suc! topic=%s" % str(topic)
    if topic.record_type ! = RecordType.TUPLE:
        print "topic type illegal!"
        sys.exit(-1)
    print "=======================================\n\n"
    cursor = dh.get_cursor(project_name, topic_name, CursorType.OLDEST, '0')
    while True:
        (record_list, record_num, next_cursor) = dh.get_records(topic, '0', cursor, 10)
        for record in record_list:
            print record
        if 0 == record_num:
            time.sleep(1)
        cursor = next_cursor
except DatahubException, e:
    print traceback.format_exc()
    sys.exit(-1)
else:
    sys.exit(-1)
```

## 3 Scalability

### 3.1 Scenario

DataHub can scale flexibly to increase or decrease the number of shards in a cluster. This allows you to handle traffic surges or save resource costs based on actual business conditions. For example, if the topic throughput cannot handle a surge in the service load during Double 11, you can split existing shards to up to 256 to increase the throughput to 256 MB/s. As the service load decreases after Double 11, you can reduce the number of shards as needed by performing the merge operation.

### 3.2 Obtain shard details

You can call the ListShard operation to obtain details about all shards. The sample response is shown as follows:

```json
    "ShardId": "string",
    "State": "string",
    "ClosedTime": uint64,
    "BeginHashKey": "string",
    "EndHashKey": "string",
    "ParentShardIds": [string,string,],
    "LeftShardId": "string",
    "RightShardId": "string"
```

### 3.3 Split a shard

You can split a shard by using an SDK or in the console. You can specify the shard by setting a shard ID and a 128-bit hash key value. After the shard is split into two child shards, the IDs and key values of the child shards are returned. The status of the parent shard is changed to Deactivated. For example, before the split operation, the parent shard details are shown as follows:

```
ShardId:0 Status:ACTIVE BeginHashKey:00000000000000000000000000000000 EndHashKey:FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
```

Split the shard by using an SDK:

```
String shardId = "0"; SplitShardRequest req = new SplitShardRequest(projectName, topicName, shardId, "AAAAAAAA AAAAAAAAAAAAAAAAAAAAAAAA"); SplitShardResult resp = client.splitShard(req);
```

After the split operation, the parent shard turns into the following three shards:

```
ShardId:0 Status:Deactivated BeginHashKey:00000000000000000000000000000000 EndHashKey:FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF ShardId:1 Status:ACTIVE BeginHashKey:00000000000000000000000000000000 EndHashKey:AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA ShardId:2 Status:ACTIVE BeginHashKey:AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA EndHashKey:FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
```

### 3.4 Merge shards

You can merge two adjacent shards by using an SDK or in the console. Shards are considered adjacent if the union of the hash key ranges for the two shards forms a contiguous set with no gaps. After the two shards are merged, the ID and key value of the new shard are returned. The statuses of the two parent shards change to Deactivated. For example, before the merge operation, the details of the two parent shards are as follows:

```
ShardId:0 Status:ACTIVE BeginHashKey:00000000000000000000000000000000 EndHashKey:7FFFFFFFFFFFFFFF7FFFFFFFFFFFFFFF ShardId:1 Status:ACTIVE BeginHashKey:7FFFFFFFFFFFFFFF7FFFFFFFFFFFFFFF EndHashKey:FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
```

Merge the two shards by using an SDK:

```
String shardId = "0"; String adjacentShardId = "1"; MergeShardRequest req = new MergeShardRequest(projectName, topicName, shardId, adjacentS hardId); MergeShardResult resp = client.mergeShard(req);
```

After the merge operation, the parent shards turn into the following three shards:

```
ShardId:0 Status:Deactivated BeginHashKey:00000000000000000000000000000000 EndHashKey:7FFFFFFFFFFFFFFF7FFFFFFFFFFFFFFF ShardId:1 Status:Deactivated BeginHashKey:7FFFFFFFFFFFFFFF7FFFFFFFFFFFFFFF EndHashKey:FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF ShardId:2 Status:ACTIVE BeginHashKey:00000000000000000000000000000000 EndHashKey:FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
```

> **Note:** After merge or split operations are performed, the statuses of the parent shards change to Deactivated. New data cannot be written into deactivated shards, whereas existing data in deactivated shards can still be consumed. A deactivated shard cannot be split into two shards or merged with any other shards. When the time-to-live of the records in a deactivated shard expires, the shard is deleted.
> If a DataConnector is configured for a deactivated shard, the DataConnector will be stopped after all records in the shard are copied to the destination platform. The DataConnector is automatically deleted after the shard is deleted.
> The new shard can only be used after its status is changed to Active. It requires less than five seconds for the status to change to Active.

to a topic schema

## 4 Insert a column to a topic schema

**schema**

### 4.1 Insert a column

This section describes how to insert columns to a topic schema. The sample code is shown as follows:

```
// Specify a DataHub account. Account account = new AliyunAccount("your access id", "your access key"); DatahubConfiguration conf = new DatahubConfiguration(account, "datahub endpoint"); DatahubClient client = new DatahubClient(conf); // Insert a bigint column to the topic schema. client.appendField(new AppendFieldRequest(projectName, topicName, new Field("test", Fiel dType.BIGINT))); // If you have created a DataConnector for MaxCompute, call the following operation. client.appendDataConnectorField(new AppendDataConnectorFieldRequest(projectName, topicNa me, ConnectorType.SINK_ODPS, "test"));
```

> **Note:** DataHub supports inserting columns only. Modifying or deleting columns is not supported.
> The operation can only be performed on a DataConnector for MaxCompute: **Insert a** **column in MaxCompute > Insert a corresponding column in DataHub >** **Modify the corresponding DataConnector configuration**.
