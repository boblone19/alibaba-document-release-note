---
title: "Alibaba Cloud Apsara Stack Enterprise v3.16.2 Server Migration Center Developer Guide"
product_version: "V3.16.2"
doc_version: "20240305"
pdf_pages: 53
source_pdf: "045726f0a24eabff_Alibaba Cloud Apsara Stack Enterprise v3.16.2 Server Migration Center Developer Guide 20240305.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/v3.16.2%E7%89%88%E6%9C%AC%E6%96%87%E6%A1%A3/%E6%9C%8D%E5%8A%A1%E5%99%A8%E8%BF%81%E7%A7%BB%E4%B8%AD%E5%BF%83/Alibaba%20Cloud%20Apsara%20Stack%20Enterprise%20v3.16.2%20Server%20Migration%20Center%20Developer%20Guide%2020240305.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings)
---

# Alibaba Cloud Apsara Stack Enterprise v3.16.2 Server Migration Center Developer Guide

## Table of Contents

- 1 API reference
  - 1.1 List of operations by function
  - 1.2 Make API requests
    - 1.2.1 Request syntax
    - 1.2.2 Obtain the SMC endpoint
  - 1.3 Common parameters
  - 1.4 RAM authorization
  - 1.5 Migration sources
    - 1.5.1 DescribeSourceServers
    - 1.5.2 ModifySourceServerAttribute
    - 1.5.3 DeleteSourceServer
  - 1.6 Migration jobs
    - 1.6.1 CreateReplicationJob
    - 1.6.2 StartReplicationJob
    - 1.6.3 DescribeReplicationJobs
    - 1.6.4 ModifyReplicationJobAttribute
    - 1.6.5 StopReplicationJob
    - 1.6.6 DeleteReplicationJob
    - 1.6.7 CutOverReplicationJob

## 1 API reference

### 1.1 List of operations by function

This topic describes the API operations that are available in Server Migration Center (SMC).

**Migration sources**

| Operation | Description |
|---|---|
| DescribeSourceServers | Queries the information about migration sources. |
| ModifySourceServerAttribu te | Modifies the name and description of a migration source. |
| DeleteSourceServer | Deletes a migration source. |

**Migration jobs**

| Operation | Description |
|---|---|
| CreateReplicationJob | Creates a migration job. |
| StartReplicationJob | Starts a migration job. |
| DescribeReplicationJobs | Queries the information about migration jobs. |
| ModifyReplicationJobAttrib ute | Modifies the parameters of a migration job. |
| StopReplicationJob | Stops a migration job. |
| DeleteReplicationJob | Deletes a migration job. |
| CutOverReplicationJob | Stops an incremental migration job that is periodically executed. After you call this operation, the migration job is complete. |

### 1.2 Make API requests

#### 1.2.1 Request syntax

To send a Server Migration Center (SMC) API request, you must send an HTTP or HTTPS GET request to the SMC endpoint. You must add the request parameters that correspond to the API operation being called. After you call the API, the system returns a response. The request and response are encoded in UTF-8. SMC API operations use the RPC protocol. You can call SMC API operations by sending HTTP or HTTPS GET requests. The following request syntax is used:

```
https://Endpoint/?Action=xx&Parameters
```

Where:
**https**: the protocol that is used to send the request.
**Endpoint**: the endpoint of the SMC API. For more information about how to obtain the SMC
endpoint, see Obtain the SMC endpoint.
**Action**: the name of the operation being performed. For example, to create a migration job,
you must set the Action parameter to CreateReplicationJob.
**Parameters**: the request parameters for the operation. Separate multiple parameters with
ampersands ( `&` ). The following example demonstrates how to call the CreateReplicationJob operation in SMC:

```
https://smc.inter.example.com/?Action=CreateReplicationJob &SystemDiskSize=125 &Common request parameters
```

#### 1.2.2 Obtain the SMC endpoint

To migrate servers by using Server Migration Center (SMC), make sure that the migration sources can access the SMC endpoint. This topic describes how to obtain the SMC endpoint.

**Prerequisites**

The URL, username, and password that are required to log on to the Cloud Migration Center console are obtained from deployment engineers or administrators. A web browser is available. We recommend that you use Google Chrome.

**Procedure**

1. In the address bar of the web browser, enter the URL that is used to access the Cloud
Migration Center console and press the ENTER key.
2. Enter your username and password.
Obtain the username and password that are used to log on to the Cloud Migration Center console from an administrator.

**Note**

When you log on to the Cloud Migration Center console for the first time, you must change the password as prompted. For security purposes, your password must meet the minimum complexity requirements. The password must be 10 to 32 characters in length and must contain at least two of the following character types: Letters Digits Special characters, including exclamation points (!), at signs (@), number signs (#), dollar signs ($), and percent signs (%)
3. Click **Log on**.
4. In the left-side navigation pane, choose **Migration Tool Center > Server Migration**
**Center**.
5. In the upper-right corner of the page, click **SMC Endpoint Address** to obtain the SMC
endpoint.

### 1.3 Common parameters

Common parameters are the parameters that are required by all API operations of Server Migration Center (SMC), including common request parameters and common response parameters.

**Common request parameters**

The following common request parameters are applicable to scenarios in which GET requests are sent in URLs to call SMC API operations.

| Parameter | Type | Requir ed | Example | Description |   |   |
|---|---|---|---|---|---|---|
| AccessKeyId | String | Yes | LTAIp4**** | The AccessKey ID provided to you by Alibaba Cloud. |   |   |
| Signature | String | Yes | OLeaidS1JvxuMv nyHOwuJ%2BuX 5q**** | The signature string of the current request. |   |   |
| SignatureMetho d | String | Yes | HMAC-SHA1 | The encryption method of the signature string. Set the value to HMAC-SHA1. |   |   |
| SignatureVersio n | String | Yes | 1.0 | The version number of the signature algorithm. Set the value to 1.0. |   |   |
| SignatureNonce | String | Yes | 3ee8c1b8-****- 44af-****- 4e0ad82f**** | A unique, random number used to prevent replay attacks. You must use different numbers for different requests. |   |   |
| Timestamp | String | Yes | 2021-01- 01T12:00:00Z | The timestamp of the request. Specify the time in the ISO 8601 standard in the yyyy-MM- ddTHH:mm:ssZ format. The time must be in UTC. |   |   |
|   |   |   |   |   | yyyy-MM- |   |
| Version | String | Yes | 2019-06-01 | The version number of the API. Specify the value in the YYYY-MM- DD format. Set the value to 2019- 06-01. |   |   |
| Format | String | No | json | The format in which to return the response. Valid values: json and xml. Default value: json. |   |   |

| :00Z | ddTHH:mm:ssZ |
|---|---|

| 01 | DD |
|---|---|

**Sample requests**

```
https://smc.inter.example.com/ ?Format=xml &Version=2019-06-01 &Signature=OLeaidS1JvxuMvnyHOwuJ%2BuX5q**** &SignatureMethod=HMAC-SHA1 &SignatureNonce=3ee8c1b8-****-44af-****-4e0ad82f**** &SignatureVersion=1.0 &AccessKeyId=LTAIp4**** &Timestamp=2021-01-01T12:00:00Z ...
```

**Common response parameters**

Every response returns a unique `RequestId` regardless of whether the call is successful. The following table describes the RequestId parameter.

| Parameter | Type | Description |
|---|---|---|
| RequestId | String | The request ID. This parameter is returned regardless of whether the call is successful. |

### 1.4 RAM authorization

Before you can call API operations of Server Migration Center (SMC) as a Resource Access Management (RAM) user, an administrator must create a policy and attach the policy to the RAM user to grant permissions to the RAM user. Alibaba Cloud Resource Names (ARNs) are used to specify resources in RAM policies. The following table describes the ARNs of resources that each SMC API operation needs to access.

| Action | ARN |
|---|---|
| DescribeSourceServers | acs:smc:$regionid:$accountid:sourceServer/* |
| ModifySourceServerAttribute | acs:smc:$regionid:$accountid:sourceServer/$sourceId |
| DeleteSourceServer | acs:smc:$regionid:$accountid:sourceServer/$sourceId |
| CreateReplicationJob | acs:smc:$regionid:$accountid:sourceServer/$sourceId acs:smc:$regionid:$accountid:replicationJob/* |
| StartReplicationJob | acs:smc:$regionid:$accountid:replicationJob/$jobId |
| DescribeReplicationJobs | acs:smc:$regionid:$accountid:replicationJob/* |
| ModifyReplicationJobAttribute | acs:smc:$regionid:$accountid:replicationJob/$jobId |
| StopReplicationJob | acs:smc:$regionid:$accountid:replicationJob/$jobId |
| DeleteReplicationJob | acs:smc:$regionid:$accountid:replicationJob/$jobId |

### 1.5 Migration sources

#### 1.5.1 DescribeSourceServers

Queries the information about migration sources.

**Usage notes**

You can specify multiple request parameters to be queried. Specified parameters are evaluated by using the AND operator. Only the specified parameters are used as filter conditions.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeSource Servers | The operation that you want to perform. Set the value to DescribeSourceServers. |
| SourceId.N | RepeatL ist | No | s- bp1e2fsl57knvu ug**** | The ID of the migration source. You can specify multiple IDs. |
| JobId | String | No | j- bp19vlwm0tyigb mj**** | The ID of the migration job. |
| State | String | No | Available | The state of the migration source. Valid values: Unavailable: The migration source is inactive, or an error occurs in the migration source. Available: The migration source is active. InUse: The migration source is being migrated. Deleting: The migration source is being deleted from Server Migration Center (SMC). |
| Name | String | No | testSourceServe rName | The name of the migration source. The name must be 2 to 128 characters in length. It must start with a letter and cannot start with http:// or https://. The name can contain digits, colons (:), underscores ( ), and hyphens (-). _ By default, this parameter is left empty. |
| PageNumber | Integer | No | 1 | The page number. Pages start from page 1. Default value: 1. |

| PageSize | Integer | No | 10 | The number of entries per page. Valid values: 1 to 50 Default value: 10 |
|---|---|---|---|---|

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| PageNumber | Integer | 1 | The page number. |
| PageSize | Integer | 10 | The number of entries per page. |
| RequestId | String | 410E6073-66D0- 45D3-AB3E- 4DC3F5E42CAA | The request ID. |
| SourceServers | Array |   | The information about the migration sources returned. |
| SourceServer |   |   |   |
| AgentVersion | String | 1.5.2.3 | The version number of the SMC client. |
| Architecture | String | x86 64 _ | The system architecture of the migration source. |
| CreationTime | String | 2021-01- 01T12:00:00Z | The time when the migration source was created. |
| DataDisks | Array |   | The data disks on the migration source. |
| DataDisk |   |   |   |
| Index | Integer | 1 | The index number of the data disk. |
| Parts | Array |   | The information about data disk partitions. |
| Part |   |   |   |
| CanBlock | Boolean | false | Indicates whether block replication is enabled for the data disk partition. |
| Device | String | 1 0 _ | The device ID of the data disk partition. |

| Need | Boolean | false | Indicates whether the data disk partition must be selected. |
|---|---|---|---|
| Path | String | /home/data | The path of the data disk partition. |
| SizeBytes | Long | 21474836480 | The size of the data disk partition. Unit: bytes. |
| Path | String | /home/data | The path of the data disk. |
| Size | Integer | 20 | The size of the data disk. Unit: GiB. |
| Description | String | Server Source Imported By GotoAliyun. | The description of the migration source. |
| ErrorCode | String | SourceServer.Offlin e | The error code of the migration source. |
| HeartbeatRate | Integer | 30 | The interval at which heartbeats are sent from the SMC client. Unit: seconds. |
| JobId | String | j- bp19vlwm0tyigbmj **** | The ID of the most recent migration job. |
| KernelLevel | Integer | 1 | The kernel level of the migration source. |
| Name | String | SourceServerName | The name of the migration source. |
| Platform | String | OpenSUSE | The operating system of the migration source. |
| ReplicationDri ver | String | SMT | The replication driver used for migration. Default value: SMT. |
| SourceId | String | s- bp1e2fsl57knvuug* *** | The ID of the migration source. |
| State | String | InUse | The state of the migration source. |

| StatusInfo | String | {"error code": _ "S1", "error msg": _ "Rsync not found. Please install rsync."} | The status information of the migration source. This parameter is returned if the migration source is in the Unavailable state. The value of this parameter consists of key-value pairs in the JSON format. Sample keys: error code _ error msg _ |
|---|---|---|---|
| SystemDiskPar ts | Array |   | The information about system disk partitions. |
| SystemDiskPar t |   |   |   |
| CanBlock | Boolean | true | Indicates whether block replication is enabled for the system disk partition. |
| Device | String | 0 0 _ | The device ID of the system disk partition. |
| Need | Boolean | true | Indicates whether the system disk partition must be selected. |
| Path | String | /boot | The path of the system disk partition. |
| SizeBytes | Long | 254803968 | The size of the system disk partition. Unit: bytes. |
| SystemDiskSiz e | Integer | 40 | The system disk size of the migration source. Unit: GiB. |

| SystemInfo | String | {\"agent mode\":\" _ daemon\",\"agent t _ ype\":\"aliyun\",\"cli ent type\":\"\",\"cor _ es\":\"2\",\"cpu usa _ ge\":\"0.00\",\"host name\":\"ixxxxxxxx xx\",\"ipv4\":\"10.0. 0.1\",\"memory\":\" 8.00\",\"memory u _ sage\":\"3.61\"} | The system information of the migration source. The value of this parameter consists of key-value pairs in the JSON format. The key-value pairs are extensible and have fixed keys. The JSON string does not exceed 1 KB in size. Sample keys: AGENT MODE: the migration mode. _ HOSTNAME: the hostname. IPV4: the IPv4 address. IPV6: the IPv6 address. CORES: the number of CPU cores. CPU USAGE: the CPU utilization. _ MEMORY: the memory size. MEMORY USAGE: the memory usage. _ |
|---|---|---|---|
| TotalCount | Integer | 1 | The total number of migration sources returned. |

**Examples**

Sample requests

```
https://smc.inter.example.com/?Action=DescribeSourceServers &SourceId.1=s-bp1e2fsl57knvuug**** &<Common request parameters>
```

Sample success responses `XML` format

```json
<DescribeSourceServersReponse>
      <SourceServers>
            <SourceServer>
                  <Description>Server Source Imported By GotoAliyun. Hostname: ubuntu14
IP Address: 192.168.**.**</Description>
                  <SystemInfo>
{"agent_mode":"daemon","agent_type":"aliyun","client_type":"","cores":"1","cpu_info":""," u_usage":"0.00","hostname":"ubuntu14","ipv4":"192.168.**.**","memory":"1.00","memory_usag :"0.73"}</SystemInfo>
                  <Platform>Ubuntu</Platform>
                  <Architecture>x86_64</Architecture>
                  <AgentVersion>2.2.0</AgentVersion>
                  <SystemDiskSize>9</SystemDiskSize>
                  <SourceId>s-bp1e2fsl57knvuug****</SourceId>
                  <SystemDiskParts>
                        <SystemDiskPart>
                              <Path>/boot</Path>
                              <Device>0_0</Device>
                              <CanBlock>true</CanBlock>
                              <SizeBytes>254803968</SizeBytes>
                        </SystemDiskPart>
                        <SystemDiskPart>
                              <Path>/</Path>
                              <Device>0_1</Device>
                              <CanBlock>true</CanBlock>
                              <SizeBytes>9403629568</SizeBytes>
                        </SystemDiskPart>
                  </SystemDiskParts>
                  <Name>testSourceServerName</Name>
                  <KernelLevel>1</KernelLevel>
                  <ReplicationDriver>SMT</ReplicationDriver>
                  <State>Unavailable</State>
                  <CreationTime>2021-01-01T12:00:00Z</CreationTime>
                  <HeartbeatRate>30</HeartbeatRate>
                  <ErrorCode>SourceServer.Offline</ErrorCode>
                  <JobId>j-bp19vlwm0tyigbmj****</JobId>
            </SourceServer>
      </SourceServers>
      <TotalCount>1</TotalCount>
      <RequestId>410E6073-66D0-45D3-AB3E-4DC3F5E42CAA</RequestId>
      <PageSize>10</PageSize>
      <PageNumber>1</PageNumber>
</DescribeSourceServersReponse>
```

`JSON` format `{`

```json
  "SourceServers": {
    "SourceServer": [
```

`{`

```json
        "Description": "Server Source Imported By GotoAliyun. Hostname: ubuntu14 IP Add
ress: 192.168.**.**",
        "SystemInfo": "
{\"agent_mode\":\"daemon\",\"agent_type\":\"aliyun\",\"client_type\":\"\",\"cores\":\"1\" "cpu_info\":\"\",\"cpu_usage\":\"0.00\",\"hostname\":\"ubuntu14\",\"ipv4\":\"192.168.**.* ",\"memory\":\"1.00\",\"memory_usage\":\"0.73\"}",
        "Platform": "Ubuntu",
        "Architecture": "x86_64",
        "AgentVersion": "2.2.0",
        "SystemDiskSize": 9,
        "SourceId": "s-bp1e2fsl57knvuug****",
        "SystemDiskParts": {
          "SystemDiskPart": [
```

`{`

```json
              "Path": "/boot",
              "Device": "0_0",
              "CanBlock": true,
              "SizeBytes": 254803968
```

`},` `{`

```json
              "Path": "/",
              "Device": "0_1",
              "CanBlock": true,
              "SizeBytes": 9403629568
```

`}` `]` `},`

```json
        "Name": "testSourceServerName",
        "KernelLevel": 1,
        "ReplicationDriver": "SMT",
        "State": "Unavailable",
        "CreationTime": "2021-01-01T12:00:00Z",
        "HeartbeatRate": 30,
        "ErrorCode": "SourceServer.Offline",
        "JobId": "j-bp19vlwm0tyigbmj****"
```

`}` `]` `},`

```json
  "TotalCount": 1,
  "RequestId": "410E6073-66D0-45D3-AB3E-4DC3F5E42CAA",
  "PageSize": 10,
  "PageNumber": 1
```

`}`

#### 1.5.2 ModifySourceServerAttribute

Modifies the name and description of a migration source.

**Usage notes**

You can call this operation regardless of the status of the migration source.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifySourceSer verAttribute | The operation that you want to perform. Set the value to ModifySourceServerAttribute. |
| SourceId | String | Yes | s- bp17m1vi6x20c 6g6**** | The ID of the migration source. |
| Name | String | No | testSourceServe rName | The name of the migration source. The name must be 2 to 128 characters in length. It must start with a letter and cannot start with http:// or https://. The name can contain digits, colons (:), underscores ( ), and hyphens (-). _ By default, this parameter is left empty. |
| Description | String | No | This is a source server. | The description of the migration source. The description must meet the following requirements: The description must be 0 to 256 characters in length. It cannot start with http:// or https://. If you do not specify this parameter, the value of this parameter is an empty string. By default, this parameter is left empty. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3C83E | The request ID. |

**Examples**

Sample requests

```
https://smc.inter.example.com/?Action=ModifySourceServerAttribute &SourceId=s-bp17m1vi6x20c6g6**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DeleteReplicationJobResponse>
    <RequestId>473469C7-AA6F-4DC5-B3DB-A3DC0DE3C83E</RequestId>
</DeleteReplicationJobResponse>
```

`JSON` format `{`

```json
    "RequestId":"473469C7-AA6F-4DC5-B3DB-A3DC0DE3C83E"
```

`}`

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | SourceServerState. Invalid | The specified source server status is invalid. | The migration source is in an invalid state. |
| 400 | SourceServerName .Duplicate | The specified source server name already exists. Please modify the source server name. | The specified migration source name already exists. Specify another name. |
| 500 | InternalError | An error occurred while processing your request. Please try again. If the problem still exists, please submit a ticket. | An internal error occurred. Try again later. |

#### 1.5.3 DeleteSourceServer

Deletes a migration source.

**Usage notes**

If a migration job is created for the migration source and the migration job is in the Running state, the migration source cannot be deleted. If a migration job is created for the migration source but the migration job is not in the Running state, you can set the `Force` parameter to true to forcibly delete the migration source.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteSourceSer ver | The operation that you want to perform. Set the value to DeleteSourceServer. |

| SourceId | String | Yes | s- bp17m1vi6x20c 6g6**** | The ID of the migration source. |
|---|---|---|---|---|
| Force | Boolean | No | true | Specifies whether to forcibly delete the migration source. Valid values: true: forcibly deletes the migration source and the migration job created for the migration source, and releases the intermediate resources of the migration job. false: does not delete the migration source if a migration job is created for the migration source. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3C83E | The request ID. |

**Examples**

Sample requests

```
https://smc.inter.example.com/?Action=DeleteSourceServer &SourceId=s-bp17m1vi6x20c6g6**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DeleteReplicationJobResponse>
    <RequestId>473469C7-AA6F-4DC5-B3DB-A3DC0DE3C83E</RequestId>
</DeleteReplicationJobResponse>
```

`JSON` format `{`

```json
    "RequestId":"473469C7-AA6F-4DC5-B3DB-A3DC0DE3C83E"
```

`}`

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | SourceServerState. Invalid | The specified source server status is invalid. | The migration source is in an invalid state. |
| 400 | SourceServer.With RunningReplication Job | The specified source server has related replication jobs that are running. | A migration job is created for the migration source and is in the Running state. |
| 400 | ReplicationJob.Rela ted | The specified source server has related replication jobs. | A migration job is created for the migration source. |
| 500 | InternalError | An error occurred while processing your request. Please try again. If the problem still exists, please submit a ticket. | An internal error occurred. Try again later. |

### 1.6 Migration jobs

#### 1.6.1 CreateReplicationJob

Creates a migration job.

**Usage notes**

You can create migration jobs only for migration sources that are in the Available state. Each migration source can be associated with only one migration job that is in the Ready, Running, Stopped, Waiting, InError, or Expired state. You can create up to 100 migration jobs within each Apsara Stack account. If you migrate a source server to an image, you must specify the `ImageName` , `SystemDiskSize` , and `DataDisk` parameters. If you use a virtual private cloud (VPC) to migrate data, you must specify the `VSwitchId` parameter. The `VpcId` parameter is optional.

**Request headers**

This operation uses only common request headers and does not have operation-specific request headers. For more information, see the "Common request headers" topic.

**Request parameters**

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| AccessKey Id | Strin g | Query | No |   | This parameter is not supported. |

|   | Developer Gui | de·API re | ference |   |   | Server Migration Cente | r |
|---|---|---|---|---|---|---|---|

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| Action | Strin g | Query | Yes | CreateReplicationJob | The operation that you want to perform. Set the value to CreateReplicationJob. |
| OwnerId | Long | Query | No |   | This parameter is not supported. |
| Resource OwnerAcc ount | Strin g | Query | No |   | This parameter is not supported. |
| RegionId | Strin g | Query | Yes | cn-qingdao-env17-d01 | The ID of the region to which you want to migrate the source server. |
| ClientToke n | Strin g | Query | No | 123e4567-e89b-12d3- a456-426655440000 | The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see API reference > ECS API > Appendix > How to ensure idempotence in the ECS Developer Guide. |

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| Name | Strin g | Query | No | testMigrationTaskName | The name of the migration job. The name must meet the following requirements: The name must be unique. The name must be 2 to 128 characters in length. It must start with a letter and cannot start with http:// or https:// . It can contain letters, digits, colons (:), underscores ( ), and _ hyphens (-). |
| Descriptio n | Strin g | Query | No | This is a migration task _ _ _ _ | The description of the migration job. The description must be 2 to 128 characters in length. It must start with a letter and cannot start with http:// or https:// . It can contain letters, digits, colons (:), underscores ( ), and hyphens (-). _ |
| SourceId | Strin g | Query | Yes | s-bp1e2fsl57knvuug**** | The ID of the migration source. |

|   | http:// |
|---|---|
| https:// |   |

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| TargetTyp e | Strin g | Query | No | Image | The type of destination to which you want to migrate the source server. Valid values: Image: After the migration job is complete, SMC generates an Elastic Compute Service (ECS) image for the source server. Instance: After the migration job is complete, SMC migrates the source server to an ECS instance. If you set this parameter to Instance, you must specify the InstanceId parameter. |
| Scheduled StartTime | Strin g | Query | No | 2019-06-04T13:35:00Z | The time when you want to run the migration job. The time must meet the following requirements: The time must be specified in the ISO 8601 standard in the YYYY-MM- DDThh:mm:ssZ format. The time must be in UTC. For example, 2021-01- 01T12:00:00Z indicates 20:00:00 on January 1, 2021 (UTC+8). The time must be later than the current time and within 30 days after the current time. If you leave this parameter empty, SMC does not start the migration job. |

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| ValidTime | Strin g | Query | No | 2019-06-04T13:35:00Z | The time when the migration job expires. The value must indicate a point in time 7 to 90 days after the migration job is created. The time must be specified in the ISO 8601 standard in the YYYY-MM- DDThh:mm:ssZ format. The time must be in UTC. For example, 2021-01- 01T12:00:00Z indicates 20:00:00 on January 1, 2021 (UTC+8). If you leave this parameter empty, the migration job never expires. After a migration job expires, the state of the migration job changes to Expired. SMC retains the migration job for seven days after the migration job expires. After the migration job is retained for seven days, SMC deletes the migration job. |

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| ImageNa me | Strin g | Query | No | testAliCloudImageName | The name of the destination image. The name must meet the following requirements: The name must be unique in an Apsara Stack region. The name must be 2 to 128 characters in length. It must start with a letter and cannot start with http:// or https:// . It can contain letters, digits, colons (:), underscores ( ), and _ hyphens (-). If you specify an image name that already exists in the destination region, the migration job ID is appended to the image name as a suffix. Example: ImageNamej-****. _ |
| InstanceId | Strin g | Query | No | i-bp1f1dvfto1sigz5**** | The ID of the destination ECS instance. |
| SystemDis kSize | Integ er | Query | Yes | 80 | The system disk size of the destination ECS instance. Unit: GiB. Valid values: 20 to 500. The value must be greater than the used space of the system disk on the source server. For example, if the total size of the source system disk is 500 GiB and the used space is 100 GiB, the value of this parameter must be greater than 100 GiB. |

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| DataDisk | Repe atList | Query | No |   | The data disk information of the destination ECS instance. |
| Tag | Repe atList | Query | No |   | This parameter is not supported. |
| VpcId | Strin g | Query | No | vpc- bp1vwnn14rqpyiczj**** | The ID of the VPC for which an Express Connect circuit or a VPN gateway is configured. |
| VSwitchId | Strin g | Query | No | vsw- bp1ddbrxdlrcbim46**** | The ID of the vSwitch in the specified VPC. This parameter is required if you use a VPC to migrate data. |

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| Replicatio nParamet ers | Strin g | Query | No | {"bandwidth limit":0,"co _ mpress level":1,"checks _ um":true} | The parameters of the replication driver. The parameters must be specified as key-value pairs in the JSON format. The keys are fixed for each type of replication driver. The JSON string can be up to 2,048 characters in length. A replication driver is a tool that is used to replicate the data of a source server to an intermediate instance. The parameters vary based on the replication driver type. If you use a Server Migration Tool (SMT) driver, you can specify the following parameters: bandwidth limit: the _ maximum bandwidth for data transmission. compress level: the _ compression ratio of data to be transmitted. checksum: specifies whether to enable checksum verification. You can obtain the type of replication driver that is used by checking the SourceServers.Replicati onDriver parameter returned by the DescribeSourceServers operation. For more information, see Developer Guide > API reference > Migration sources > DescribeSourceServers. |

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| NetMode | Integ er | Query | No | 0 | The network mode for data transmission. Valid values: 0: Data is transmitted over the Internet. Make sure that the source server can access the Internet. 2: Data is transmitted over a VPC. If you specify this value, the VSwitchId parameter is required. You do not need to specify the VpcId parameter because the VPC ID can be retrieved based on the vSwitch ID. Default value: 0. |

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| RunOnce | Boole an | Query | No | true | Specifies whether to disable incremental migration for the source server. Default value: true. Valid values: true: creates a migration job that runs only once. Incremental data of the source server is not synchronized. false: creates an incremental migration job. In this case, you must specify the Frequency parameter. SMC synchronizes incremental data of the source server to Apsara Stack at the specified frequency. You can use an incremental migration job to synchronize incremental data from the source server to Apsara Stack without the need to interrupt your business. A full data image is generated at the point in time when the migration job is run for the source server. You can specify this parameter only when you create a migration job. The value of this parameter cannot be changed after the migration job is created. |

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| Frequency | Integ er | Query | No | 12 | The interval at which SMC synchronizes incremental data to Apsara Stack. Unit: hour. Valid values: 1 to 168. This parameter is required if you set the RunOnce parameter to false. By default, this parameter is left empty. |
| MaxNumb erOfImage ToKeep | Integ er | Query | No | 10 | The maximum number of images retained for the incremental migration job. Valid values: 1 to 10. This parameter is required if you set the RunOnce parameter to false. By default, this parameter is left empty. |

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| InstanceT ype | Strin g | Query | No | ecs.c6.large | The type of the intermediate instance. You can call the DescribeInstanceTypes operation of ECS to query the instance types provided by ECS. For more information, see API reference > ECS API > Instances > DescribeInstanceType s in the ECS Developer Guide. If you specify this parameter, SMC creates an intermediate instance of the specified instance type. If the specified instance type is unavailable, the migration job fails to be created. If you do not specify this parameter, SMC selects an available instance type in a specific order to create an intermediate instance. |
| LaunchTe mplateId | Strin g | Query | No |   | This parameter is not supported. |
| LaunchTe mplateVer sion | Strin g | Query | No |   | This parameter is not supported. |
| SystemDis kPart | Repe atList | Query | No |   | The information about system disk partitions. |
| InstanceR amRole | Strin g | Query | No | SMCAdmin | The name of the Resource Access Management (RAM) role that is assumed by the instance. |
| Container Namespac e | Strin g | Query | No |   | This parameter is not supported. |

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| Container Repositor y | Strin g | Query | No |   | This parameter is not supported. |
| Container Tag | Strin g | Query | No |   | This parameter is not supported. |
| LicenseTy pe | Strin g | Query | No | BYOL | The license type. Valid values: An empty value specifies no license. A value of BYOL specifies Bring Your Own License (BYOL). |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | C8B26B44-0189- 443E-9816- D951F596**** | The request ID. |
| JobId | String | j- bp17bclvg344jlyt** ** | The ID of the migration job. |

**Examples**

Sample requests

```
http(s)://smc.inter.example.com/?Action=CreateReplicationJob &Action=CreateReplicationJob &RegionId=cn-qingdao-env17-d01 &SourceId=s-bp1e2fsl57knvuug**** &SystemDiskSize=80 &Common request parameters
```

Sample success responses `JSON` format `{`

```json
 "RequestId":"C8B26B44-0189-443E-9816-D951F596****",
 "JobId":"j-bp17bclvg344jlyt****"
```

`}` `XML` format

```xml
<RequestId>C8B26B44-0189-443E-9816-D951F596****</RequestId> <JobId>j-bp17bclvg344jlyt****</JobId>
```

**Error codes**

| Http status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | SourceServerState. Invalid | SourceServerState.Invalid | The specified source server status is invalid. |
| 400 | ReplicationJobData DiskIndex.Invalid | ReplicationJobDataDiskIndex.In valid | The specified replication job contains data disk index not found in source server. |
| 400 | VSwitchIdVpcId.Mis match | VSwitchIdVpcId.Mismatch | The specified VSwitchId and VpcId does not match. |
| 400 | InvalidSecurityGrou pId.IncorrectNetwo rkType | InvalidSecurityGroupId.Incorre ctNetworkType | The network type of the specified security group does not support this action. |
| 400 | InvalidSecurityGrou pId.VPCMismatch | InvalidSecurityGroupId.VPCMis match | The specified security group and the specified virtual switch are not in the same VPC. |
| 400 | QuotaExceeded.Re plicationJob | QuotaExceeded.ReplicationJob | The maximum number of replication jobs is exceeded. Please submit a ticket to raise the quota. |
| 400 | ReplicationJobNam e.Duplicate | ReplicationJobName.Duplicate | The specified replication job name already exists. |
| 500 | InternalError | InternalError | An error occurred while processing your request. Try again. If the problem still exists, submit a ticket. |

#### 1.6.2 StartReplicationJob

Starts a migration job.

**Usage notes**

You can call this operation to start only a migration job that is in the **Ready**, **Stopped**, or
**InError** state.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|

| Action | String | Yes | StartReplicationJ ob | The operation that you want to perform. Set the value to StartReplicationJob. |
|---|---|---|---|---|
| JobId | String | Yes | j- bw526m1vi6x21 q**** | The ID of the migration job. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3C83E | The request ID. |

**Examples**

Sample requests

```
https://smc.inter.example.com/?Action=StartReplicationJob &JobId=j-bw526m1vi6x21q**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<StartReplicationJobResponse>
    <RequestId>473469C7-AA6F-4DC5-B3DB-A3DC0DE3C83E</RequestId>
</StartReplicationJobResponse>
```

`JSON` format `{`

```json
    "RequestId":"473469C7-AA6F-4DC5-B3DB-A3DC0DE3C83E"
```

`}`

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | ReplicationJob.Inval idStatus | The specified replication job status is invalid. | The migration job is in an invalid state. |

| 400 | SourceServerState. Invalid | The specified source server status is invalid. | The migration source is in an invalid state. |
|---|---|---|---|
| 500 | InternalError | An error occurred while processing your request. Please try again. If the problem still exists, please submit a ticket. | An internal error occurred. Try again later. |

#### 1.6.3 DescribeReplicationJobs

Queries the information about migration jobs.

**Usage notes**

You can specify multiple request parameters to be queried. Specified parameters are evaluated by using the AND operator. Only the specified parameters are used as filter conditions.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeReplicat ionJobs | The operation that you want to perform. Set the value to DescribeReplicationJobs. |
| SourceId.N | RepeatL ist | No | s- bp1e2fsl57knvu ug**** | The ID of the migration source. N indicates the sequence number of the ID. Valid values of N: 1 to 50. |
| JobId.N | RepeatL ist | No | j- bp19vlwm0tyigb mj**** | The ID of the migration job. N indicates the sequence number of the ID. Valid values of N: 1 to 50. |
| Name | String | No | testMigrationTas kName | The name of the migration job. |
| RegionId | String | No | cn-qingdao- env17-d01 | The ID of the region to which you want to migrate the migration source. |

| Status | String | No | Ready | The state of the migration job. Valid values: Ready: The migration job is not started. Running: The migration job is running. Stopped: The migration job is paused. InError: An error occurs in the migration job. Finished: The migration job is complete. Waiting: The migration job is waiting to run. Expired: The migration job expired. Deleting: The migration job is being deleted. |
|---|---|---|---|---|
| BusinessStatus | String | No | Preparing | The business status of the migration job. Valid values: Preparing: The migration is being prepared. Syncing: Data is being synchronized. Processing: The migration is in progress. Cleaning: Intermediate resources are being released. |
| PageNumber | Integer | No | 1 | The page number. Pages start from page 1. Default value: 1. |
| PageSize | Integer | No | 10 | The number of entries per page. Valid values: 1 to 50 Default value: 10 |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| PageNumber | Integer | 1 | The page number. |
| PageSize | Integer | 10 | The number of entries per page. |
| ReplicationJob s | Array of ReplicationJob |   | The details of the migration jobs. |
| ReplicationJob |   |   |   |

| BusinessStatu s | String | Preparing | The business status of the migration job. |
|---|---|---|---|
| CreationTime | String | 2014-07- 24T13:00:52Z | The time when the migration job was created. |
| DataDisks | Array of DataDisk |   | The information about the data disks on the destination Elastic Compute Service (ECS) instance. |
| DataDisk |   |   |   |
| Index | Integer | 1 | The index number of the data disk. |
| Parts | Array of Part |   | The information about data disk partitions. |
| Part |   |   |   |
| Block | Boolean | true | Indicates whether block replication is enabled for the data disk partition. |
| Device | String | 0 1 _ | The device ID of the data disk partition. |
| SizeBytes | Long | 21474836480 | The size of the data disk partition. Unit: bytes. |
| Size | Integer | 40 | The size of the data disk. Unit: GiB. |
| Description | String | This is my migration task. | The description of the migration job. |
| EndTime | String | 2019-06- 04T16:00:52Z | The time when the migration job was complete. |
| ErrorCode | String | InternalError | The error code. |
| Frequency | Integer | 15 | The interval at which the incremental migration job runs. Unit: hour. Valid values: 1 to 168. |
| ImageId | String | m- o6w3gy99qf89rkga **** | The ID of the destination image. |
| ImageName | String | testAliCloudImage Name | The name of the destination image. |

| InstanceId | String | i- bp1ff25rzvnul6kr** ** | The ID of the destination ECS instance. |
|---|---|---|---|
| InstanceRamR ole | String | SMCAdmin | The name of the Resource Access Management (RAM) role that is assigned to the instance. |
| InstanceType | String | ecs.sn1ne.large | The instance type of the intermediate instance. |
| JobId | String | j- bp19vlwm0tyigbmj **** | The ID of the migration job. |
| LaunchTempla teId | String | lt-launchtemplateid | The ID of the launch template. |
| LaunchTempla teVersion | String | 1 | The versions of the launch template. |
| LicenseType | String | BYOL | The type of license for the migration job. Valid values: An empty value indicates no license. A value of BYOL indicates Bring Your Own License (BYOL). |
| MaxNumberOfI mageToKeep | Integer | 8 | The maximum number of images retained for the incremental migration job. Valid values: 1 to 10. |
| Name | String | testMigrationTaskN ame | The name of the migration job. |
| NetMode | Integer | 0 | The type of network used for the migration. |
| Progress | Float | 55.45 | The progress of the migration job. |
| RegionId | String | cn-qingdao-env17- d01 | The ID of the region to which the migration source is migrated. |
| ReplicationJob Runs | Array of ReplicationJob Run |   | The execution records of the migration job. |
| ReplicationJob Run |   |   |   |
| EndTime | String | 2019-10- 04T13:35:00Z | The time when the migration job ended. |

| ImageId | String | m- o6w3gy99qf89rkga **** | The ID of the destination image. |
|---|---|---|---|
| StartTime | String | 2019-10- 01T13:35:00Z | The time when the migration job was started. |
| Type | String | Schedule | The method used to run the migration job. Valid values: Manual: The migration job was manually started. Schedule: The migration job was started at a scheduled time or at a specific interval. |
| ReplicationPar ameters | String | BandWidthLimit:0 | The string of key-value pairs configured for the replication driver. |
| RunOnce | Boolean | true | Indicates whether incremental migration is disabled for the migration source. Valid values: true: Incremental migration is disabled. A migration job runs only once after the job is created. false: Incremental migration is enabled. For an incremental migration job, Server Migration Center (SMC) migrates incremental data at the interval specified by the Frequency parameter. |
| ScheduledStar tTime | String | 2019-06- 04T13:35:00Z | The time when the migration job was scheduled to run. |
| SourceId | String | s- bp1e2fsl57knvuug* *** | The ID of the migration source. |
| StartTime | String | 2019-06- 04T14:40:52Z | The time when the migration job was started. |
| Status | String | Running | The state of the migration job. |
| StatusInfo | String | statusinfo | The status information about the migration job. |
| SystemDiskPar ts | Array of SystemDiskPar t |   | The information about system disk partitions. |

| SystemDiskPar t |   |   |   |
|---|---|---|---|
| Block | Boolean | true | Indicates whether block replication is enabled for the system disk partition. |
| Device | String | 0 1 _ | The device ID of the system disk partition. |
| SizeBytes | Long | 254803968 | The size of the system disk partition. Unit: bytes. |
| SystemDiskSiz e | Integer | 40 | The size of the system disk of the destination ECS instance. |
| TargetType | String | image | The type of the destination image. |
| TransitionInsta nceId | String | i- bp1ff25rzvnul6kr** ** | The ID of the intermediate instance. |
| VSwitchId | String | vsw- bp1ddbrxdlrcbim4 6**** | The ID of the vSwitch in the specified virtual private cloud (VPC). |
| ValidTime | String | 2019-06- 08T14:40:52Z | The time when the migration job expired. |
| VpcId | String | vpc- bp1vwnn14rqpyiczj **** | The ID of the VPC for which an Express Connect circuit or a VPN gateway is configured. |
| RequestId | String | 6E1187E8-843A- 4850-B97E- 2F17F00D48F7 | The request ID. |
| TotalCount | Integer | 5 | The total number of migration jobs returned. |

**Examples**

Sample requests

```
https://smc.inter.example.com/?Action=DescribeReplicationJobs &RegionId=cn-qingdao-env17-d01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeReplicationJobsResponse>
      <TotalCount>1</TotalCount>
      <ReplicationJobs>
            <ReplicationJob>
                  <Status>Running</Status>
                  <Progress>75</Progress>
                  <TransitionInstanceId>i-bp1ff25rzvnul6kr****</TransitionInstanceId>
                  <DataDisks>
                        <DataDisk>
                              <Parts>
                                    <Part>
                                          <Device>2_0</Device>
                                          <Block>true</Block>
                                          <SizeBytes>5334102016</SizeBytes>
                                    </Part>
                              </Parts>
                              <Size>20</Size>
                              <Index>2</Index>
                        </DataDisk>
                  </DataDisks>
                  <SystemDiskSize>20</SystemDiskSize>
                  <NetMode>0</NetMode>
                  <SourceId>s-bp1e2fsl57knvuug****</SourceId>
                  <SystemDiskParts>
                        <SystemDiskPart>
                              <Device>0_0</Device>
                              <Block>true</Block>
                              <SizeBytes>21466120192</SizeBytes>
                        </SystemDiskPart>
                  </SystemDiskParts>
                  <StartTime>2020-05-14T12:01:24Z</StartTime>
                  <BusinessStatus>Processing</BusinessStatus>
                  <Name>testMigrationTaskName</Name>
                  <ValidTime>2020-06-13T12:01:24Z</ValidTime>
                  <RunOnce>true</RunOnce>
                  <TargetType>Image</TargetType>
                  <CreationTime>2020-05-14T12:01:24Z</CreationTime>
                  <RegionId>cn-qingdao-env17-d01</RegionId>
                  <ErrorCode></ErrorCode>
                  <JobId>j-bp19vlwm0tyigbmj****</JobId>
            </ReplicationJob>
      </ReplicationJobs>
      <RequestId>6E1187E8-843A-4850-B97E-2F17F00D48F7</RequestId>
      <PageSize>10</PageSize>
      <PageNumber>1</PageNumber>
</DescribeReplicationJobsResponse>
```

`JSON` format `{`

```json
  "TotalCount": 1,
  "ReplicationJobs": {
    "ReplicationJob": [
```

`{` `{`

```json
        "Status": "Running",
        "Progress": 75.0,
        "TransitionInstanceId": "i-bp1ff25rzvnul6kr****",
        "DataDisks": {
          "DataDisk": [
```

`{`

```json
              "Parts": {
                "Part": [
```

`{`

```json
                    "Device": "2_0",
                    "Block": true,
                    "SizeBytes": 5334102016
```

`}` `]` `},`

```json
              "Size": 20,
              "Index": 2
```

`}` `]` `},`

```json
        "SystemDiskSize": 20,
        "NetMode": 0,
        "SourceId": "s-bp1e2fsl57knvuug****",
        "SystemDiskParts": {
          "SystemDiskPart": [
```

`{`

```json
              "Device": "0_0",
              "Block": true,
              "SizeBytes": 21466120192
```

`}` `]` `},`

```json
        "StartTime": "2020-05-14T12:01:24Z",
        "BusinessStatus": "Processing",
        "Name": "testMigrationTaskName",
        "ValidTime": "2020-06-13T12:01:24Z",
        "RunOnce": true,
        "TargetType": "Image",
        "CreationTime": "2020-05-14T12:01:24Z",
        "RegionId": "cn-qingdao-env17-d01",
        "ErrorCode": "",
        "JobId": "j-bp19vlwm0tyigbmj****"
```

`}` `]` `},`

```json
  "RequestId": "6E1187E8-843A-4850-B97E-2F17F00D48F7",
  "PageSize": 10,
  "PageNumber": 1
```

`}`

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 500 | InternalError | An error occurred while processing your request. Please try again. If the problem still exists, please submit a ticket. | An internal error occurred. Try again later. |
| 403 | Forbidden.Unautho rized | A required authorization for the specified action is not supplied. | You do not have the permissions on the specified resource. |

#### 1.6.4 ModifyReplicationJobAttribute

Modifies the parameters of a migration job.

**Usage notes**

Before you modify a migration job, take note of the following items: The `Name` and `Description` parameters can be modified throughout the lifecycle of a migration job. The `Frequency` and `MaxNumberOfImageToKeep` parameters can be modified only before a migration job is executed or when a migration job is in the `Waiting` state. Other parameters can be modified only before a migration job is executed.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyReplicatio nJobAttribute | The operation that you want to perform. Set the value to ModifyReplicationJobAttribute. |
| JobId | String | Yes | j- bp19vlwm0tyigb mj**** | The ID of the migration job. |
| Name | String | No | testMigrationTas kName | The name of the migration job. The name must meet the following requirements: The name must be unique. The name must be 2 to 128 characters in length and can contain letters, digits, colons (:), underscores ( ), and hyphens (-). It _ must start with a letter but cannot start with http:// or https:// . |

|   | http:// |
|---|---|
| https:// |   |

| Description | String | No | This is my migr _ _ _ ation task _ | The description of the migration job. The description must be 2 to 128 characters in length and can contain letters, digits, colons (:), underscores ( ), and hyphens (-). It must start _ with a letter but cannot start with http:// or https:// . |
|---|---|---|---|---|
| TargetType | String | No | Image | The type of destination to which the source server is migrated. You can modify the value only before the migration job starts. A value of Image indicates that SMC generates an Alibaba Cloud image for your source server after the migration is successful. You can use this image to create Elastic Compute Service (ECS) instances to implement migration to Alibaba Cloud. |
| ScheduledStartT ime | String | No | 2019-06- 04T13:35:00Z | The time when the migration job is executed. SMC starts the migration job at the specified time. Specify the time in the ISO 8601 standard in the YYYY-MM- DDThh:mm:ssZ format. The time must be in UTC. For example, 2021- 01-01T12:00:00Z indicates 20:00:00 on January 1, 2021 (UTC+8). Note If this parameter is not specified, SMC does not automatically start the migration job. You must call the StartReplicationJob operation to start the job. |

| ImageName | String | No | testAliCloudIma geName | The name of the destination image. The name must meet the following requirements: The name must be unique within an Alibaba Cloud region. The name must be 2 to 128 characters in length and can contain letters, digits, colons (:), underscores ( ), and hyphens (-). It _ must start with a letter but cannot start with http:// or https:// . Note If an image with the same name already exists in the current region when the migration job is executed, the system adds the job ID to the end of the image name in the format of ImageName-JobId by default. |
|---|---|---|---|---|
| InstanceId | String | No | i- bp1f1dvfto1sigz 5**** | The ID of the destination ECS instance. |
| SystemDiskSize | Integer | No | 50 | The system disk size of the destination ECS instance. Unit: GiB. Valid values: 20 to 500. Note The value must be greater than the used space of the system disk on the source server. For example, if the total size of the source system disk is 500 GiB and the used space is 100 GiB, the value of this parameter must be greater than 100 GiB. |
| SystemDiskPart. N.Device | String | No | 0 1 _ | The device ID of Partition N in the destination system disk. N indicates the sequence number of the partition. Set the value to the device ID of the corresponding partition on the source server. |

|   | http:// |
|---|---|
| https:// |   |

| SystemDiskPart. N.SizeBytes | Long | No | 254803968 | The size of Partition N in the destination system disk. Unit: bytes. The default value is equal to the size of the partition in the source system disk. Note The total size of all partitions in the destination system disk cannot exceed the size of the destination system disk. |
|---|---|---|---|---|
| SystemDiskPart. N.Block | Boolean | No | true | Specifies whether to enable block replication for Partition N in the destination system disk. Valid values: true false |
| DataDisk.N.Size | Integer | No | 100 | The size of Data Disk N on the destination ECS instance. Unit: GiB. Valid values: 20 to 32768. Note The size of a destination data disk must be greater than the size of data in the source data disk. For example, if the total size of the source data disk is 500 GiB and the used space is 100 GiB, the value of this parameter must be greater than 100 GiB. |

| DataDisk.N.Inde x | Integer | No | 1 | The index of Data Disk N on the destination ECS instance. Valid values: 1 to 16. The data disks on a destination ECS instance are arranged in a sequential order that starts from 1. Note To create a destination data disk, make sure that the corresponding source data disk exists on the source server. |
|---|---|---|---|---|
| DataDisk.N.Part. N.Device | String | No | 0 1 _ | The device ID of Partition N in the destination data disk. N indicates the sequence number of the partition. Set the value to the device ID of the corresponding partition on the source server. |
| DataDisk.N.Part. N.SizeBytes | Long | No | 254803968 | The size of Partition N in the destination data disk. Unit: bytes. The default value is equal to the size of the partition in the source data disk. Note The total size of all partitions in the destination data disk cannot exceed the size of the destination data disk. |
| DataDisk.N.Part. N.Block | Boolean | No | true | Specifies whether to enable block replication for Partition N in the destination data disk. Valid values: true false |
| Frequency | Integer | No | 10 | The interval at which the incremental migration job is executed. Unit: hour. Valid values: 1 to 168. |
| MaxNumberOfIm ageToKeep | Integer | No | 5 | The maximum number of images that are retained for the incremental migration job. Valid values: 1 to 10. |

| InstanceType | String | No | ecs.c5.large | The type of the intermediate instance. You can call the DescribeInstanceTypes operation of ECS to query the instance types provided by ECS. For more information, see ECS Developer Guide. If you specify this parameter, SMC creates an intermediate instance of the specified instance type. If the specified instance type is unavailable, the migration job fails to be created. If you do not specify this parameter, SMC selects an available instance type in a specific order to create an intermediate instance. |   |   |
|---|---|---|---|---|---|---|
| InstanceRamRol e | String | No | SMCAdmin | The name of the Resource Access Management (RAM) role that is assumed by the instance. |   |   |
| ValidTime | String | No | 2019-06- 04T13:35:00Z | The time when the migration job expires. The value must indicate a point in time 7 to 90 days after the migration job is created. This parameter can be modified only if the migration job is in the Ready, Running, Stopped, InError, or Waiting state. Specify the time in the ISO 8601 standard in the YYYY-MM- DDThh:mm:ssZ format. The time must be in UTC. For example, 2021-01-01T12:00:00Z indicates 20:00:00 on January 1, 2021 (UTC+8). If you do not specify this parameter, the migration job never expires. After a migration job expires, the job state changes to Expired. SMC retains the migration job for seven days after the job expires. After the job is retained for seven days, SMC deletes the migration job. |   |   |
|   |   |   |   |   | YYYY-MM- |   |

|   | DDThh:mm:ssZ |
|---|---|

**Response parameters**

| > Document Versi | on: 20240305 |   | 4 |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 1C488B66-B819- 4D14-8711- C4EAAA13AC01 | The request ID. |

**Examples**

Sample requests

```
https://smc.inter.example.com/?Action=ModifyReplicationJobAttribute &JobId=j-bp19vlwm0tyigbmj**** &Name=testMigrationTaskName &Description=This_is_my_migration_task &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DeleteReplicationJobResponse>
    <RequestId>1C488B66-B819-4D14-8711-C4EAAA13AC01</RequestId>
</DeleteReplicationJobResponse>
```

`JSON` format `{`

```json
    "RequestId":"1C488B66-B819-4D14-8711-C4EAAA13AC01"
```

`}`

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | DataDisk.Duplicate Index | The source server data disk cannot contain the same index. | The data disks of the migration source have duplicate indexes. |
| 400 | ReplicationJob.Inval idStatus | The specified replication job status is invalid. | The migration job is in an invalid state. |
| 400 | ReplicationJobData DiskIndex.Invalid | The specified replication job contains data disk index not found in source server. | The index of a data disk specified in the migration job does not exist in the migration source. |

| 400 | ReplicationJobNam e.Duplicate | The specified replication job name already exists. | The specified migration job name already exists. Specify another name for the migration job. |
|---|---|---|---|
| 500 | InternalError | An error occurred while processing your request. Please try again. If the problem still exists, please submit a ticket. | An internal error occurred. Try again later. |

#### 1.6.5 StopReplicationJob

Stops a migration job.

**Usage notes**

You can call this operation to stop only a running migration job in the Syncing state.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | StopReplicationJ ob | The operation that you want to perform. Set the value to StopReplicationJob. |
| JobId | String | Yes | j- bw526m1vi6x21 qh**** | The ID of the migration job. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3C83E | The request ID. |

**Examples**

Sample requests

```
https://smc.inter.example.com/?Action=StopReplicationJob &JobId=j-bw526m1vi6x21qh**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<StopReplicationJobResponse>
    <RequestId>473469C7-AA6F-4DC5-B3DB-A3DC0DE3C83E</RequestId>
</StopReplicationJobResponse>
```

`JSON` format `{`

```json
    "RequestId":"473469C7-AA6F-4DC5-B3DB-A3DC0DE3C83E"
```

`}`

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | ReplicationJob.Inval idStatus | The specified replication job status is invalid. | The migration job is in an invalid state. |
| 500 | InternalError | An error occurred while processing your request. Please try again. If the problem still exists, please submit a ticket. | An internal error occurred. Try again later. |

#### 1.6.6 DeleteReplicationJob

Deletes a migration job.

**Usage notes**

Deleted migration jobs cannot be restored. After a migration job is deleted, associated resources, such as the intermediate instance, are automatically released.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteReplicatio nJob | The operation that you want to perform. Set the value to DeleteReplicationJob. |
| JobId | String | Yes | j- bp17m1vi6x21q hqk**** | The ID of the migration job. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|

| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3C83E | The request ID. |
|---|---|---|---|

**Examples**

Sample requests

```
https://smc.inter.example.com/?Action=DeleteReplicationJob &JobId=j-bp17m1vi6x21qhqk**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DeleteReplicationJobResponse>
    <RequestId>473469C7-AA6F-4DC5-B3DB-A3DC0DE3C83E</RequestId>
</DeleteReplicationJobResponse>
```

`JSON` format `{`

```json
    "RequestId":"473469C7-AA6F-4DC5-B3DB-A3DC0DE3C83E"
```

`}`

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | ReplicationJob.Inval idStatus | The specified replication job status is invalid. | The migration job is in an invalid state. |
| 500 | InternalError | An error occurred while processing your request. Please try again. If the problem still exists, please submit a ticket. | An internal error occurred. Try again later. |

#### 1.6.7 CutOverReplicationJob

Stops an incremental migration job that is periodically executed. After you call this operation, the migration job is complete.

**Usage notes**

You can call this operation to stop and complete only an incremental migration job that is in the Waiting state.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|

| Action | String | Yes | CutOverReplicati onJob | The operation that you want to perform. Set the value to CutOverReplicationJob. |
|---|---|---|---|---|
| JobId | String | Yes | j- bp1fnx5y3djc4c op**** | The ID of the incremental migration job. |
| SyncData | Boolean | No | false | Specifies whether to migrate full data for the last time. Valid values: true: migrates full data for the last time. Then, the intermediate resources are automatically cleared, and the migration job is complete. false: does not migrate full data for the last time. The intermediate resources are directly cleared, and the migration job is complete. Default value: false. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3C83E | The request ID. |

**Examples**

Sample requests

```
https://smc.inter.example.com/?Action=CutOverReplicationJob &JobId=j-bp1fnx5y3djc4cop**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<CutOverReplicationJobReponse>
  <RequestId>473469C7-AA6F-4DC5-B3DB-A3DC0DE3C83E</RequestId>
</CutOverReplicationJobReponse>
```

`JSON` format `{`

```json
    "RequestId":"473469C7-AA6F-4DC5-B3DB-A3DC0DE3C83E"
```

`}`

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | ReplicationJob.Inval idStatus | The specified replication job status is invalid. | The migration job is in an invalid state. |
| 400 | SourceServerState. Invalid | The specified source server status is invalid. | The migration source is in an invalid state. |
| 500 | InternalError | An error occurred while processing your request. Please try again. If the problem still exists, please submit a ticket. | An internal error occurred. Try again later. If the error persists, submit a ticket. |
