---
title: "数据库备份DBS 开发指南"
product_version: "v3.18.6-SP2607"
doc_version: "20260729"
pdf_pages: 96
source_pdf: "06_开发指南_enterprise-developer-guide.pdf"
source_url: "https://apsara-doc.oss-cn-hangzhou.aliyuncs.com/apsara-pdf/enterprise/v_3_18_6_20260730/cbs/zh/enterprise-developer-guide.pdf"
converter: line-classifier (PyMuPDF)
---

# 数据库备份DBS 开发指南

## API参考

### API概览

数据库备份DBS提供以下相关API接口。

### 备份计划

| API | 描述 |
|---|---|
| CreateBackupPlan | 创建备份计划 |
| ConfigureBackupPlan | 配置备份计划 |
| StartBackupPlan | 启动备份计划 |
| StopBackupPlan | 暂停备份计划 |
| DescribeBackupPlanList | 查看备份计划 |
| ModifyBackupObjects | 修改备份对象 |
| ModifyBackupSourceEndpoint | 修改数据库备份源 |
| ModifyBackupPlanName | 修改备份计划名称 |
| ModifyBackupStrategy | 修改备份时间 |
| DescribeRestoreRangeInfo | 查看可恢复时间段详情 |
| DescribeBackupPlanBilling | 查看备份计划计费信息 |

### 备份任务

| API | 描述 |
|---|---|
| DescribeFullBackupList | 查看全量备份任务列表 |
| DescribeIncrementBackupList | 查看增量备份任务列表 |

### 恢复任务

| API | 描述 |
|---|---|
| CreateRestoreTask | 创建恢复任务 |
| StartRestoreTask | 启动恢复任务 |
| DescribeRestoreTaskList | 查看恢复任务列表 |

### 备份网关

| API | 描述 |
|---|---|
| DescribeBackupGatewayList | 查看备份网关列表 |

| API | 描述 |
|---|---|
| DescribeBackupSetDownloadTa skList | 查看备份集下载列表 |
| ModifyBackupSetDownloadRule s | 设置备份集下载规则 |
| CreateFullBackupSetDownload | 创建全量备份集下载任务 |
| CreateIncrementBackupSetDow nload | 创建增量备份集下载任务 |

**其他**

| API | 描述 |
|---|---|
| DescribeJobErrorCode | 查看任务标准化错误码信息 |
| DescribeNodeCidrList | 查看DBS运行节点网段 |
| DescribePreCheckProgressList | 查看预检查进度列表 |

### 备份计划

#### 创建备份计划

通过调用CreateBackupPlan创建一个DBS备份计划。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Region | Strin g | Query | 否 | cn-hangzhou | DBS地域。 专有云默认环境初始化地域。 |
| InstanceCl ass | Strin g | Query | 是 | micro | 规格，取值如下： small ：基础版 large ：高级版 |
| Database Type | Strin g | Query | 是 | MySQL | 数据库类型，取值如下： MySQL MSSQL Oracle MongoDB Redis |
| BackupMe thod | Strin g | Query | 是 | logical | 备份方式，取值如下： logical ：逻辑备份 physical ：物理备份 |
| Period | Strin g | Query | 否 | Month | 指定预付费实例类型。 此参数专有云API为固定取值，无需设置。 |
| UsedTime | Integ er | Query | 否 | 1 | 指定购买时长。 此参数专有云API为固定取值，无需设置。 |
| PayType | Strin g | Query | 否 | prepay | 支付方式，专有云下默认 prepay（预付费）。 |

| 开发指南·API参 | 考 |  |  |  | 数据库备份 |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Database Region | Strin g | Query | 否 | cn-hangzhou | 数据库地域。 |
| StorageRe gion | Strin g | Query | 否 | cn-hangzhou | 存储地域。 |
| InstanceT ype | Strin g | Query | 否 | RDS | 数据库实例类型，取值如下： RDS DDS Kvstore PolarDB ：仅支持 PolarDB-X。 Other ：通过IP:Port 直接输入。 |
| StorageTy pe | Strin g | Query | 否 | 无 | 该参数暂未开放使用。 |
| FromApp | Strin g | Query | 否 | OpenAPI | 用于备注请求来源，默认值为OpenAPI，无需手动设置。 |
| ClientToke n | Strin g | Query | 否 | KJSAHKJFHKJSHFKASHFKJ ADFHKD**** | 输入任意字符串，用于保证请求幂等性。 |
| RegionId | Strin g | Host | 否 | cn-hangzhou | 地域ID。 |
| OwnerId | Strin g | Query | 否 | 无。 | 该参数暂未开放使用。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 7BCF6D62-885F- 5A4A-91A1- 679760E7**** | 请求ID。 |
| HttpStatusCod e | Integer | 200 | HTTP状态码。 |
| BackupPlanId | String | dbsrhahrsu2**** | 备份计划ID。 |
| ErrMessage | String | The specified parameter %s value is not valid. | 错误信息。 |
| OrderId | String | 21437345592**** | 订单ID。 |

| 数据库备份 |  |  | 开发指南·API参考 |
|---|---|---|---|
| 参数名称 | 类型 | 示例 | 说明 |
| Success | Boolean | true | 请求是否成功，返回值如下： true ：请求成功 false ：请求失败 |
| ErrCode | String | Param.NotFound | 错误码。 |

**示例**

请求示例

```
http(s)://dbs-api.cn-hangzhou.aliyuncs.com/?Action=CreateBackupPlan &InstanceClass=micro &DatabaseType=MySQL &BackupMethod=logical
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"7BCF6D62-885F-5A4A-91A1-679760E7****",
 "HttpStatusCode":200,
 "BackupPlanId":"dbsrhahrsu2****",
 "ErrMessage":"The specified parameter %s value is not valid.",
 "OrderId":"21437345592****",
 "Success":true,
 "ErrCode":"Param.NotFound"
}
```

`XML` 格式

```xml
<RequestId>7BCF6D62-885F-5A4A-91A1-679760E7****</RequestId> <HttpStatusCode>200</HttpStatusCode> <BackupPlanId>dbsrhahrsu2****</BackupPlanId> <ErrMessage>The specified parameter %s value is not valid.</ErrMessage> <OrderId>21437345592****</OrderId> <Success>true</Success> <ErrCode>Param.NotFound</ErrCode>
```

#### 配置备份计划

调用ConfigureBackupPlan接口配置一个DBS备份计划。

**描述**

配置一个DBS备份计划。 创建备份计划（CreateBackupPlan）接口调用后，DBS实例会开始生产，一般需要等待

**说明**

5s，才能调用配置备份计划（ConfigureBackupPlan）接口。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ConfigureBacku pPlan | 系统规定参数。取值：ConfigureBackupPlan。 |
| BackupPlanId | String | 是 | dbstooi0******* | 备份计划ID。 |
| BackupPlanNam e | String | 是 | dbstooi0******* | 备份计划名称。 |
| SourceEndpointI nstanceType | String | 是 | rds | 数据库所在位置，取值如下： RDS ECS Express：通过专线/VPN网关/智能网关接入的数据库 Agent：通过备份网关接入的数据库 DDS：云MongoDB Other：通过IP:Port直连的数据库 |
| SourceEndpoint Region | String | 否 | cn-hangzhou | 数据库地域。 说明 SourceEndpointInstanceType 为RDS、ECS、DDS、Express、 Agent时，该参数必传。 |
| SourceEndpointI nstanceID | String | 否 | rm- uf6wjk5xxxxxxx xxx | 数据库实例ID。 说明 SourceEndpointInstanceType 为RDS、ECS、DDS、Express时， 该参数必传。 |

| SourceEndpointI P | String | 否 | rm- uf6wjk5xxxxxxx. mysql.rds.aliyun cs.com | 数据库连接地址。 说明 SourceEndpointInstanceType 为Express、Agent、Other时，该参数必传。 |
|---|---|---|---|---|
| SourceEndpointP ort | Integer | 否 | 3306 | 数据库端口。 说明 SourceEndpointInstanceType 为ECS、Express、Agent、Other 时，该参数必传。 |
| SourceEndpoint DatabaseName | String | 否 | testRds | 数据库名称。 说明数据库类型为PostgreSQL、MongoDB时， 该参数必传。 |
| SourceEndpoint UserName | String | 否 | testRds | 数据库账号。 说明数据库类型为Redis， 或者数据库所在位置为Agent且数据库类型为MSSQL时该参数非必须，其他场景均必传。 |
| SourceEndpointP assword | String | 否 | testPassword | 密码。 说明数据库类型为Redis， 或者数据库所在位置为Agent且数据库类型为MSSQL时该参数非必须，其他场景均必传。 |
| BackupGatewayI d | Long | 否 | 23313123312 | 备份网关ID。 说明 SourceEndpointInstanceType 为Agent时，该参数必传。 |
| OSSBucketName | String | 否 | TestOssBucket | OSS Bucket名称。 说明默认：系统自动生成新的名称。 |

| BackupObjects | String | 否 | [ { "DBName":"待备份库名", "SchemaName": "待备份 Schema 名", "TableIncludes": [{ "TableName":"待备份表表名" }], "TableExcludes": [{ "TableName":"待备份库名不需要备份表的表名" }] } ] | 备份对象。 |
|---|---|---|---|---|
| BackupPeriod | String | 否 | Monday | 全量备份周期，取值如下： Monday：周一 Tuesday：周二 Wednesday：周三 Thursday：周四 Friday：周五 Saturday：周六 Sunday：周日 |
| BackupStartTim e | String | 否 | 14:22 | 全量备份开始时间，格式为 HH:mmZ（UTC时间）。 |
| EnableBackupLo g | Boolean | 否 | true | 是否开启增量日志备份，取值如下： true：开启 false：关闭 |
| BackupRetentio nPeriod | Integer | 否 | 730 | 备份数据保留时间，取值：0~1825，默认为730。 |
| DuplicationInfre quentAccessPeri od | Integer | 否 | 180 | 转为低频访问存储时间，默认为180。 |
| DuplicationArchi vePeriod | Integer | 否 | 365 | 转为归档冷备存储时间，默认为365。 |
| SourceEndpoint OracleSID | String | 否 | test | Oracle SID名称，数据库类型为Oracle时，该参数必传。 |
| BackupStorageT ype | String | 否 | system | 内置存储类型。 说明专有云默认system ， 即备份数据存储在DBS的内置OSS 上。 |

| BackupSpeedLi mit | Long | 否 | 262144 | 磁盘IO限制，单位为KB/S。 |
|---|---|---|---|---|
| BackupStrategy Type | String | 否 | simple | 全量备份周期，取值如下： simple：周期备份，和 BackupPeriod、BackupStartTime配合使用。 manual：手动备份。 |
| CrossAliyunId | String | 否 | XXX | 不支持此参数使用。 |
| CrossRoleName | String | 否 | XXX | 不支持此参数使用。 |
| AutoStartBackup | Boolean | 否 | true | 是否开启备份。 |
| RegionId | String | 否 | cn-hangzhou | 地域ID。 |
| ClientToken | String | 否 | ETnLKlblzczshOT UbOCzxxxxxxx | 用于保证请求的幂等性，防止重复提交请求。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| BackupPlanId | String | dbstooi01ex**** | 备份计划ID。 |
| ErrCode | String | Param.NotFound | 错误码。 |
| ErrMessage | String | The specified parameter %s value is not valid. | 错误信息。 |
| HttpStatusCod e | Integer | 200 | HTTP状态码。 |
| RequestId | String | F1FB49D4-B504- 47F1-9F43- D7EAB33F**** | 请求ID。 |
| Success | Boolean | true | 请求是否成功，返回值如下： true：请求成功 false：请求失败 |

**示例**

请求示例

```
http(s)://dbs-api.cn-hangzhou.aliyuncs.com/?Action=ConfigureBackupPlan &BackupPlanId=dbstooi0******* &BackupPlanName=dbstooi0******* &SourceEndpointInstanceType=rds
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>F1FB49D4-B504-47F1-9F43-D7EAB33F****</RequestId> <HttpStatusCode>200</HttpStatusCode> <BackupPlanId>dbstooi01ex****</BackupPlanId> <ErrMessage>The specified parameter %s value is not valid.</ErrMessage> <Success>true</Success> <ErrCode>Param.NotFound</ErrCode>
```

`JSON` 格式

```json
{
    "RequestId": "F1FB49D4-B504-47F1-9F43-D7EAB33F****",
    "HttpStatusCode": 200,
    "BackupPlanId": "dbstooi01ex****",
    "ErrMessage": "The specified parameter %s value is not valid.",
    "Success": true,
    "ErrCode": "Param.NotFound"
}
```

#### 查看备份计划

调用DescribeBackupPlanList接口查看一个DBS备份计划。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeBackup PlanList | 系统规定参数。取值：DescribeBackupPlanList。 |
| BackupPlanId | String | 否 | dbstooi01ex**** | 备份计划ID，支持查询多个备份计划，使用（,）英文逗号分隔。 |
| Region | String | 否 | cn-hangzhou | DBS地域。 说明专有云默认环境初始化地域。 |

| PageSize | Integer | 否 | 30 | 每页的记录数，取值为30、50、100。 说明默认每页记录数为30。 |
|---|---|---|---|---|
| PageNum | Integer | 否 | 1 | 页码，大于等于0且不超过Integer的最大值，默认值为：0。 |
| BackupPlanNam e | String | 否 | test123 | 备份计划名称。 |
| BackupPlanStatu s | String | 否 | wait | 备份计划状态，取值如下： wait：未配置 init：未启动（预检查失败） running：运行中 stop：失败 pause：暂停 locked：锁定中 check pass：预检查通过 _ |
| RegionId | String | 否 | cn-hangzhou | 地域ID。 |
| ClientToken | String | 否 | ASDASDASDSAD ASFCZXVZ | 任意字符串，用于保证请求幂等性。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| ErrCode | String | Param.NotFound | 错误码。 |
| ErrMessage | String | The specified parameter %s value is not valid. | 错误信息。 |
| HttpStatusCod e | Integer | 200 | HTTP状态码。 |
| Items | Array of BackupPlanDe tail |  | 备份计划详情。 |
| BackupPlanDe tail |  |  |  |
| BackupGatewa yId | Long | 827362187368736 | 备份网关ID。 |

| BackupMethod | String | logical | 备份方式，返回值如下： logical：逻辑备份 physical：物理备份 |
|---|---|---|---|
| BackupObjects | String | [ { \"DBName\":\"待备份库名\", \"SchemaName\":\" 待备份 Schema 名\", \"TableIncludes\": [{ \"TableName\":\"待备份表表名\" }], \"TableExcludes\": [{ \"TableName\":\"待备份库名不需要备份表的表名\" }] } ] | 备份对象。 |
| BackupPeriod | String | Monday | 全量备份周期，取值如下： Monday：周一 Tuesday：周二 Wednesday：周三 Thursday：周四 Friday：周五 Saturday：周六 Sunday：周日 |
| BackupPlanCr eateTime | Long | 1582527713000 | 备份计划创建时间。 |
| BackupPlanId | String | dbstooi01e**** | 备份计划ID。 |
| BackupPlanNa me | String | test123 | 备份计划名称。 |
| BackupPlanSta tus | String | init | 备份计划状态，返回值如下： wait：未配置 init：未启动（预检查失败） running：运行中 stop：失败 pause：暂停 locked：锁定中 check pass：预检查通过 _ |
| BackupRetenti onPeriod | Integer | 365 | 备份数据保留时间，取值：0~1825（天）。 |
| BackupSetDow nloadDir | String | */test/test123 | 备份集下载服务器目录。 |

| BackupSetDow nloadFullDataF ormat | String | SQL | 备份集下载全量数据格式，返回值如下： Native SQL CSV JSON |
|---|---|---|---|
| BackupSetDow nloadGatewayI d | Long | 123123 | 备份集下载备份网关ID。 |
| BackupSetDow nloadIncremen tDataFormat | String | SQL | 备份集下载增量数据格式，返回值如下： Native SQL CSV JSON |
| BackupSetDow nloadTargetTy pe | String | agent | 备份集下载目标类型。 唯一取值：agent，表示已安装备份网关。 |
| BackupStartTi me | String | 14:22 | 全量备份开始时间，返回格式为 HH:mm 。例 _ _ 如： 14:22 。 _ _ |
| BackupStorag eType | String | simple | 全量备份周期，返回值如下： simple：周期备份，与BackupPeriod、 BackupStartTime配合使用 manual：手动备份说明默认simple。 |
| BeginTimesta mpForRestore | Long | 1554560477000 | 可数据库恢复时间段的开始时间。 |
| CrossAliyunId | String | 2xxx7778xxxxxxxx xx | 不支持返回此参数。 |
| CrossRoleNam e | String | test123 | 不支持返回此参数。 |
| DuplicationArc hivePeriod | Integer | 365 | 转为归档冷备存储时间（天）。 |
| DuplicationInfr equentAccess Period | Integer | 180 | 转为低频访问存储时间（天）。 |
| EnableBackup Log | Boolean | true | 是否已开启增量日志备份，取值： true：开启 false：关闭 |

| EndTimestamp ForRestore | Long | 1554560477000 | 可数据库恢复时间段的结束时间。 |
|---|---|---|---|
| ErrMessage | String | can not connect to oracle instance orcl with user dbs | 预检查任务异常信息。 |
| InstanceClass | String | micro | 规格，返回值如下： micro：入门型 small：低配型 medium：中配型 large：高配型 |
| OSSBucketNa me | String | dbs-backup- 1857XXXXX489 | OSS Bucket名称。 |
| OSSBucketReg ion | String | cn-hangzhou | OSS Bucket地域。 |
| OpenBackupS etAutoDownlo ad | Boolean | true | 是否已开启自动备份集下载功能，返回值如下： true false |
| SourceEndpoin tDatabaseNam e | String | test | 数据库名称。 |
| SourceEndpoin tInstanceID | String | test | 数据库实例ID。 |
| SourceEndpoin tInstanceType | String | RDS | 数据库所在位置，返回值如下： RDS ECS Express：通过专线/VPN网关/智能网关接入的数据库 Agent：通过备份网关接入的数据库 DDS：云MongoDB Other：通过IP:Port直连的数据库 |
| SourceEndpoin tIpPort | String | 100.*.*.10:33204 | 数据库连接地址。 |
| SourceEndpoin tOracleSID | String | test | Oracle SID名称。 |
| SourceEndpoin tRegion | String | cn-hangzhou | 数据库地域。 |
| SourceEndpoin tUserName | String | test | 数据库账号。 |

| PageNum | Integer | 1 | 页码。 |
|---|---|---|---|
| PageSize | Integer | 30 | 每页的记录数。 |
| RequestId | String | 4F1888AC-1138- 4995-B9FE- D2734F61**** | 请求ID。 |
| Success | Boolean | true | 请求是否成功，返回值如下： true：请求成功 false：请求失败 |
| TotalElements | Integer | 100 | 总备份计划数。 |
| TotalPages | Integer | 4 | 总页数。 |

**示例**

请求示例

```
http(s)://dbs-api.cn-hangzhou.aliyuncs.com/?Action=DescribeBackupPlanList &BackupPlanId=dbstooi01ex****
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<PageSize>30</PageSize> <RequestId>4F1888AC-1138-4995-B9FE-D2734F61****</RequestId> <PageNum>0</PageNum> <HttpStatusCode>200</HttpStatusCode> <TotalElements>1</TotalElements> <Items>
    <BackupPlanDetail>
        <BackupPlanName>dbXXXXX7ltj</BackupPlanName>
        <BackupMethod>logical</BackupMethod>
        <BackupPlanCreateTime>1583000</BackupPlanCreateTime>
        <BackupPeriod>MONDAY</BackupPeriod>
        <BackupObjects>[     {         "DBName":"待备份库名",         "SchemaName":"待备份
Schema 名", "TableIncludes":[{ "TableName":"待备份表表名" }],
```

`"TableExcludes":[{ "TableName":"`待备份库名不需要备份表的表名`" }] } ]<`

```xml
/BackupObjects>
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

`JSON` 格式

```json
{
 "PageSize": 30,
 "RequestId": "4F1888AC-1138-4995-B9FE-D2734F61****",
 "PageNum": 0,
 "HttpStatusCode": 200,
 "TotalElements": 1,
 "Items": {
  "BackupPlanDetail": [
   {
    "BackupPlanName": "dbXXXXX7ltj",
    "BackupMethod": "logical",
    "BackupPlanCreateTime": 1583000,
    "BackupPeriod": "MONDAY",
    "BackupObjects": "[     {         \"DBName\":\"待备份库名\",         \"SchemaName\":\"
待备份 Schema 名\", \"TableIncludes\":[{ \"TableName\":\"待备份表表名\"
```

}], \"TableExcludes\":[{ \"TableName\":\"待备份库名不需要备份表的表名\"

```json
}] } ]",
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
   }
```

]

```json
 },
 "TotalPages": 1,
 "Success": true
}
```

#### 启动备份计划

调动StartBackupPlan接口启动一个DBS备份计划。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | StartBackupPlan | 系统规定参数。取值：StartBackupPlan。 |

| BackupPlanId | String | 是 | dbstooi01****** | 备份计划ID。 |
|---|---|---|---|---|
| RegionId | String | 否 | cn-hangzhou | 地域ID。 |
| ClientToken | String | 否 | ETnLKlblzczshOT UbOCzxxxxxxx | 用于保证请求的幂等性，防止重复提交请求。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| BackupPlanId | String | dbstooi01****** | 备份计划ID。 |
| CreatedFullBa ckupsetId | String | dbs1hvb0wwwe*** * | 创建备份计划的ID。 |
| ErrCode | String | Param.NotFound | 错误码。 |
| ErrMessage | String | The specified parameter %s value is not valid. | 错误信息。 |
| HttpStatusCod e | Integer | 200 | HTTP状态码。 |
| RequestId | String | D6E068C3-25BC- 455A-85FE- 45F0B22E**** | 请求ID。 |
| Success | Boolean | true | 请求是否成功，返回值如下： true：请求成功 false：请求失败 |

**示例**

请求示例

```
http(s)://dbs-api.cn-hangzhou.aliyuncs.com/?Action=StartBackupPlan &BackupPlanId=dbstooi01******
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>D6E068C3-25BC-455A-85FE-45F0B22E****</RequestId> <HttpStatusCode>200</HttpStatusCode> <BackupPlanId>dbstooi01******</BackupPlanId> <Success>true</Success>
```

`JSON` 格式

```json
{
 "RequestId": "D6E068C3-25BC-455A-85FE-45F0B22E****",
 "HttpStatusCode": 200,
 "BackupPlanId": "dbstooi01******",
 "Success": true
}
```

#### 暂停备份计划

调用StopBackupPlan接口暂停一个DBS备份计划。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | StopBackupPlan | 系统规定参数。取值：StopBackupPlan。 |
| BackupPlanId | String | 是 | dbstooi01**** | 备份计划ID。 |
| StopMethod | String | 是 | ALL | 暂停方式，取值： ALL：暂停备份计划、全量数据备份任务、增量日志备份任务、恢复任务 PLAN：仅暂停备份计划 |
| RegionId | String | 否 | cn-hangzhou | 地域ID。 |
| ClientToken | String | 否 | ETnLKlblzczshOT UbOCzxxxxxxx | 用于保证请求的幂等性，防止重复提交请求。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| BackupPlanId | String | dbs1h****usfa | 备份计划ID。 |
| ErrCode | String | Param.NotFound | 错误码。 |
| ErrMessage | String | The specified parameter %s value is not valid. | 错误信息。 |
| HttpStatusCod e | Integer | 200 | HTTP状态码。 |

| RequestId | String | D6E068C3-25BC- 455A-85FE- 45F0B22E**** | 请求ID。 |
|---|---|---|---|
| Success | Boolean | true | 请求是否成功，返回值如下： true：请求成功 false：请求失败 |

**示例**

请求示例

```
http(s)://dbs-api.cn-hangzhou.aliyuncs.com/?Action=StopBackupPlan &BackupPlanId=dbstooi01**** &StopMethod=ALL
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>D6E068C3-25BC-455A-85FE-45F0B22E****</RequestId> <HttpStatusCode>200</HttpStatusCode> <BackupPlanId>dbs1h****usfa</BackupPlanId> <Success>true</Success>
```

`JSON` 格式

```json
{
    "RequestId": "D6E068C3-25BC-455A-85FE-45F0B22E****",
    "HttpStatusCode": 200,
    "BackupPlanId": "dbs1h****usfa",
    "Success": true
}
```

#### 修改备份对象

调用ModifyBackupObjects接口，修改一个DBS备份计划的备份对象。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ModifyBackupOb jects | 系统规定参数。取值：ModifyBackupObjects。 |

| BackupObjects | String | 是 | [ { "DBName":"17x xx92xxxx374", "SchemaName": "gy9xnj8xxxxxx" , "TableIncludes": [{ "TableName":"te st1" }], "TableExcludes": [{ "TableName":"te st2" }] } ] | 备份对象。更多详情请参见请求参数补充说明。 |
|---|---|---|---|---|
| BackupPlanId | String | 是 | dbs1h****usfa | 备份计划ID，可通过调用DescribeBackupPlanList接口获取该参数的值。 |
| RegionId | String | 否 | cn-hangzhou | 地域ID。 |
| ClientToken | String | 否 | ETnLKlblzczshOT UbOCzxxxxxxx | 用于保证请求的幂等性，防止重复提交请求。 |

**请求参数补充说明**

BackupObjects的定义格式为JSON字符串，定义如下： [

```
    {
```

`"DBName":"`待备份库名`",` `"SchemaName":"`待备份 `Schema` 名`",`

```json
        "TableIncludes":[{
```

`"TableName":"`待备份表表名"

```json
        }],
        "TableExcludes":[{
```

`"TableName":"`待备份库名不需要备份表的表名"

```
        }]
    }
```

] 当用户只配置了 `DBName` ，不配置其他子对象的规则，那么表示迁移这个数据库下面的所有对象。 当用户配置了 `DBName` ，且配置了部分对象的规则，那么不配置的对象默认不迁移。各种对象名的定义可以支持如下的正则表达式： 点号 . ：表示匹配除 \r\n 之外的任何单个字符。 星号 * ：表示匹配前面子表达式任意次， `h.llo` 匹配 `hll` o、 `heeeello` 等字符串。 问号 ? ：表示匹配前面子表达式零次或1次， h.?llo 匹配 `hllo` 、 `hello` ，但不能匹配 `haello` 。

|  | [characters] |
|---|---|
| hallo |  |

负值字符集合 [^characters] ：表示不匹配方括号内任意一个字符，例如 h[^ae]llo 匹配 `hcllo` 、 `hdllo` ，但是不能匹配 `hallo` 、 `hello` 。

| 范围 | [character1-character2] |  |  |  |
|---|---|---|---|---|
| [0-9] |  |  |  |  |
|  |  | 、 | [a-z] | 。 |

`SchemaName` 和 `NewSchemaName` 只用于MSSQL，其他数据库的库名定义使

**说明**

用 `DBName` 和 `NewDBName` 参数。

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| BackupPlanId | String | dbs1h****usfa | 备份计划ID。 |
| ErrCode | String | Param.NotFound | 错误码。 |
| ErrMessage | String | The specified parameter %s value is not valid. | 错误信息。 |
| HttpStatusCod e | Integer | 200 | HTTP状态码。 |
| NeedPrecheck | Boolean | true | 本次修改是否会触发预检查。如果返回值为 true，则需要再调用StartBackupPlan接口启动备份计划。 |
| RequestId | String | D6E068C3-25BC- 455A-85FE- 45F0B22E**** | 请求ID。 |
| Success | Boolean | true | 请求是否成功，返回值如下： true：请求成功 false：请求失败 |

**示例**

请求示例

```
http(s)://dbs-api.cn-hangzhou.aliyuncs.com/?Action=ModifyBackupObjects &BackupObjects=[ { "DBName":"17xxx92xxxx374", "SchemaName":"gy9xnj8xxxxxx", "TableInclu des":[{ "TableName":"test1" }], "TableExcludes":[{ "TableName":"test2" }] } ] &BackupPlanId=dbs1h****usfa
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>D6E068C3-25BC-455A-85FE-45F0B22E****</RequestId> <HttpStatusCode>200</HttpStatusCode> <BackupPlanId>dbs1h****usfa</BackupPlanId> <Success>true</Success>
```

`JSON` 格式

```json
{
 "RequestId": "D6E068C3-25BC-455A-85FE-45F0B22E****",
 "HttpStatusCode": 200,
 "BackupPlanId": "dbs1h****usfa",
 "Success": true
}
```

#### 修改数据库备份源

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ModifyBackupSo urceEndpoint | 系统规定参数。取值：ModifyBackupSourceEndpoin t。 |
| BackupPlanId | String | 是 | dbs1h****usfa | 备份计划ID，可通过调用DescribeBackupPlanList接口获取该参数的值。 |
| SourceEndpointI nstanceType | String | 是 | RDS | 数据库所在位置，取值如下： RDS ECS Express：通过专线/VPN网关/智能网关接入的数据库 Agent：通过备份网关接入的数据库 DDS：云MongoDB Other：通过IP:Port直连的数据库 |
| SourceEndpoint Region | String | 否 | cn-hangzhou | 数据库地域。 说明 SourceEndpointInstanceType 为RDS、ECS、DDS、Express、 Agent时，该参数必传。 |

| SourceEndpointI nstanceID | String | 否 | rm- bp1p8c29479jvX XXX | 数据库实例ID。 说明 SourceEndpointInstanceType 为RDS、ECS、DDS、Express时， 该参数必传。 |
|---|---|---|---|---|
| SourceEndpointI P | String | 否 | 100.*.*.10:3320 4 | 数据库连接地址。 说明 SourceEndpointInstanceType 为Express、Agent、Other时该参数必传。 |
| SourceEndpointP ort | Integer | 否 | 3306 | 数据库端口。 说明 SourceEndpointInstanceType 为ECS、Express、Agent、Other 时，该参数必传。 |
| SourceEndpoint DatabaseName | String | 否 | test | 数据库名称。 说明数据库类型为PostgreSQL、Mongo DB时，该参数必传。 数据库所在位置为Agent且数据库类型为MSSQL时， 该参数必传。 |
| SourceEndpoint UserName | String | 否 | test | 数据库账号。 说明数据库类型为Redis， 或者数据库所在位置为Agent且数据库类型为MSSQL时该参数非必须， 其他场景均必传。 |
| SourceEndpointP assword | String | 否 | test | 密码。 说明数据库类型为Redis， 或者数据库所在位置为Agent且数据库类型为MSSQL时该参数非必须， 其他场景均必传。 |
| BackupGatewayI d | Long | 否 | 21321323213 | 备份网关 ID。SourceEndpointInstanceType 为Agent时，该参数必传。 |

| BackupObjects | String | 否 | [{ "DBName":"待备份库名", "SchemaName": "待备份 Schema 名", "TableIncludes": [{ "TableName":"待备份表表名" }], "TableExcludes": [{"TableName":" 待备份库名不需要备份表的表名" }] } ] | 备份对象。当数据库所在位置为Agent 时，该参数非必须，其他场景均必传。 |
|---|---|---|---|---|
| SourceEndpoint OracleSID | String | 否 | test | Oracle SID名称。数据库类型为Oracle 时，该参数必传。 |
| CrossAliyunId | String | 否 | 2xxx7778xxxxxx xxxx | 跨阿里云账号备份的UID。 |
| CrossRoleName | String | 否 | test123 | 跨阿里云账号备份的RAM角色名称。 |
| RegionId | String | 否 | cn-hangzhou | 地域ID。 |
| ClientToken | String | 否 | ETnLKlblzczshOT UbOCzxxxxxxx | 用于保证请求的幂等性，防止重复提交请求。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| BackupPlanId | String | dbs1h****usfa | 备份计划ID。 |
| ErrCode | String | Param.NotFound | 错误码。 |
| ErrMessage | String | The specified parameter %s value is not valid. | 错误信息。 |
| HttpStatusCod e | Integer | 200 | HTTP状态码。 |
| NeedPrecheck | Boolean | false | 本次修改是否会触发预检查，返回值如下： true false 说明如果返回值为true，则需要再调用StartBackupPlan接口启动备份计划。 |

| RequestId | String | D6E068C3-25BC- 455A-85FE- 45F0B22E**** | 请求ID。 |
|---|---|---|---|
| Success | Boolean | true | 请求是否成功，返回值如下： true：请求成功 false：请求失败 |

**示例**

请求示例

```
http(s)://dbs-api.cn-hangzhou.aliyuncs.com/?Action=ModifyBackupSourceEndpoint &BackupPlanId=dbs1h****usfa &SourceEndpointInstanceType=RDS
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>D6E068C3-25BC-455A-85FE-45F0B22E****</RequestId> <HttpStatusCode>200</HttpStatusCode> <BackupPlanId>dbs1h****usfa</BackupPlanId> <NeedPrecheck>false</NeedPrecheck> <Success>true</Success>
```

`JSON` 格式

```json
{
 "RequestId": "D6E068C3-25BC-455A-85FE-45F0B22E****",
 "HttpStatusCode": 200,
 "BackupPlanId": "dbs1h****usfa",
 "NeedPrecheck": false,
 "Success": true
}
```

#### 修改备份计划名称

调用ModifyBackupPlanName接口，修改一个备份计划名称。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ModifyBackupPl anName | 系统规定参数。取值：ModifyBackupPlanName。 |

| BackupPlanId | String | 是 | dbstooi0**** | 备份计划ID，可通过调用DescribeBackupPlanList接口获取该参数的值。 |
|---|---|---|---|---|
| BackupPlanNam e | String | 是 | dbstooi0**** | 备份计划名称，可通过调用DescribeBackupPlanList接口获取该参数的值。 |
| RegionId | String | 否 | cn-hangzhou | 地域ID。 |
| ClientToken | String | 否 | ETnLKlblzczshOT UbOCzxxxxxxx | 用于保证请求的幂等性，防止重复提交请求。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| BackupPlanId | String | dbstooi0**** | 备份计划ID。 |
| ErrCode | String | Param.NotFound | 错误码。 |
| ErrMessage | String | The specified parameter %s value is not valid. | 错误信息。 |
| HttpStatusCod e | Integer | 200 | HTTP状态码。 |
| RequestId | String | D6E068C3-25BC- 455A-85FE- 45F0B22E**** | 请求ID。 |
| Success | Boolean | true | 请求是否成功，返回值如下： true：请求成功 false：请求失败 |

**示例**

请求示例

```
http(s)://dbs-api.cn-hangzhou.aliyuncs.com/?Action=ModifyBackupPlanName &BackupPlanId=dbstooi0**** &BackupPlanName=dbstooi0****
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>D6E068C3-25BC-455A-85FE-45F0B22E****</RequestId> <HttpStatusCode>200</HttpStatusCode> <BackupPlanId>dbstooi0****</BackupPlanId> <Success>true</Success>
```

`JSON` 格式

```json
{
 "RequestId": "D6E068C3-25BC-455A-85FE-45F0B22E****",
 "HttpStatusCode": 200,
 "BackupPlanId": "dbstooi0****",
 "Success": true
}
```

#### 修改备份时间

调用ModifyBackupStrategy接口，修改一个DBS备份计划的备份时间。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ModifyBackupStr ategy | 系统规定参数。取值：ModifyBackupStrategy。 |
| BackupPeriod | String | 是 | Monday | 全量备份周期，取值如下： Monday：周一 Tuesday：周二 Wednesday：周三 Thursday：周四 Friday：周五 Saturday：周六 Sunday：周日 |
| BackupPlanId | String | 是 | dbstooi01**** | 备份计划ID，可通过调用DescribeBackupPlanList接口获取该参数的值。 |
| BackupStartTim e | String | 否 | 14:22 | 全量备份开始时间，格式为 HH:mmZ （UTC时间）。 _ _ |

| BackupStrategy Type | String | 否 | simple | 全量备份周期，取值如下： simple：周期备份，和 BackupPeriod、BackupStartTime配合使用。 manual ：手动备份。 说明默认为simple。 |
|---|---|---|---|---|
| RegionId | String | 否 | cn-hangzhou | 地域ID。 |
| ClientToken | String | 否 | ETnLKlblzczshOT UbOCzxxxxxxx | 用于保证请求的幂等性，防止重复提交请求。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| BackupPlanId | String | dbstooi01**** | 备份计划ID。 |
| ErrCode | String | Param.NotFound | 错误码。 |
| ErrMessage | String | The specified parameter %s value is not valid. | 错误信息。 |
| HttpStatusCod e | Integer | 200 | HTTP状态码。 |
| NeedPrecheck | Boolean | false | 本次修改是否会触发预检查，返回值如下： true false 说明如果返回值为true，则需要再调用StartBackupPlan接口启动备份计划。 |
| RequestId | String | D6E068C3-25BC- 455A-85FE- 45F0B22E**** | 请求ID。 |
| Success | Boolean | true | 请求是否成功，返回值如下： true：请求成功 false：请求失败 |

**示例**

请求示例

```
http(s)://dbs-api.cn-hangzhou.aliyuncs.com/?Action=ModifyBackupStrategy &BackupPeriod=Monday &BackupPlanId=dbstooi01****
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>D6E068C3-25BC-455A-85FE-45F0B22E****</RequestId> <HttpStatusCode>200</HttpStatusCode> <BackupPlanId>dbstooi01****</BackupPlanId> <NeedPrecheck>false</NeedPrecheck> <Success>true</Success>
```

`JSON` 格式

```json
{
 "RequestId": "D6E068C3-25BC-455A-85FE-45F0B22E****",
 "HttpStatusCode": 200,
 "BackupPlanId": "dbstooi01****",
 "NeedPrecheck": false,
 "Success": true
}
```

#### 查看可恢复时间段详情

调用DescribeRestoreRangeInfo接口，查看一个备份计划可恢复时间段详情。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeRestore RangeInfo | 系统规定参数。取值：DescribeRestoreRangeInfo。 |
| BackupPlanId | String | 是 | dbstooi0**** | 备份计划ID，可通过调用DescribeBackupPlanList接口获取该参数的值。 |
| BeginTimestamp ForRestore | Long | 是 | 1554560477000 | 查询可恢复开始时间，取值： 1554560477000。 |
| EndTimestampF orRestore | Long | 是 | 1554560477000 | 查询可恢复结束时间，取值： 1554560477000。 |
| RegionId | String | 否 | cn-hangzhou | 地域ID。 |

| ClientToken | String | 否 | ETnLKlblzczshOT UbOCzxxxxxxx | 用于保证请求的幂等性，防止重复提交请求。 |
|---|---|---|---|---|
| RecentlyRestore | Boolean | 否 | true | 是否开启最近恢复。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| ErrCode | String | Param.NotFound | 错误码。 |
| ErrMessage | String | The specified parameter %s value is not valid. | 错误信息。 |
| HttpStatusCod e | Integer | 200 | HTTP状态码。 |
| Items | Array of DBSRecoverRa nge |  | 可恢复时间段信息。 |
| DBSRecoverRa nge |  |  |  |
| BeginTimesta mpForRestore | Long | 1554560477000 | 可恢复开始时间，取值：1554560477000。 |
| EndTimestamp ForRestore | Long | 1554560477000 | 可恢复结束时间，取值：1554560477000。 |
| FullBackupList | Array of FullBackupDet ail |  | 当RangeType为point时，该字段展示这个时间段范围内所有的权利。备份点信息。 |
| FullBackupDet ail |  |  |  |
| BackupSetId | String | dbs1hvb***** | 备份集ID。 |
| EndTime | Long | 1554560477000 | 全量备份结束时间。取值：1554560477000。 |
| StartTime | Long | 1554560477000 | 全量备份开始时间。取值：1554560477000。 |
| RangeType | String | point | 可恢复时间段类型，返回值如下： point：该时间段为全量备份离散时间点。 range：该时间段为连续备份时间段，可指定任意时间。 |
| SourceEndpoin tInstanceID | String | rm-bp1p8c***** | 数据库实例ID。 |

| SourceEndpoin tInstanceType | String | rm-bp1p8c***** | 数据库所在位置。 |
|---|---|---|---|
| RequestId | String | 7A851299-A739- 4801-B4BC- FC30A535**** | 请求ID。 |
| Success | Boolean | false | 请求是否成功，返回值如下： true：请求成功 false：请求失败 |

**示例**

请求示例

```
http(s)://dbs-api.cn-hangzhou.aliyuncs.com/?Action=DescribeRestoreRangeInfo &BackupPlanId=dbstooi0**** &BeginTimestampForRestore=1554560477000 &EndTimestampForRestore=1554560477000
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

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

`JSON` 格式

```json
{
    "HttpStatusCode": 200,
    "RequestId": "7A851299-A739-4801-B4BC-FC30A535****",
    "Items": {
        "DBSRecoverRange": {
            "BeginTimestampForRestore": 1554560477000,
            "EndTimestampForRestore": 1554560477000,
            "FullBackupList": [
                {
                    "FullBackupDetail": {
                        "BackupSetId": "dbs1hvb*****",
                        "EndTime": 1554560477000,
                        "StartTime": 1554560477000
                    }
                }
```

`],`

```json
            "RangeType": "point",
            "SourceEndpointInstanceID": "rm-bp1p8c*****",
            "SourceEndpointInstanceType": "rm-bp1p8c*****"
        }
    }
}
```

#### 查看备份计划计费信息

调用DescribeBackupPlanBilling接口，查看备份计划计费信息。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeBackup PlanBilling | 系统规定参数。取值：DescribeBackupPlanBilling。 |
| BackupPlanId | String | 是 | dbssl67c7mx*** * | 备份网关ID，可通过调用DescribeBackupPlanList接口获取该参数的值。 |
| RegionId | String | 否 | cn-hangzhou | 地域ID。 |
| ClientToken | String | 否 | ETnLKlblzczshOT UbOCzxxxxxxxx xx | 用于保证请求的幂等性，防止重复提交请求。由客户端生成该参数值，要保证在不同请求间唯一，最大值不超过64个ASCII 字符，且该参数值中不能包含非ASCII字符。 |
| ShowStorageTyp e | Boolean | 否 | true | 是否展示存储类型。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| ErrCode | String | InvalidParameter | 错误码。 |
| ErrMessage | String | This backupPlan can't support this action | 错误信息。 |
| HttpStatusCod e | Integer | 200 | HTTP状态码。 |
| Item | Struct |  | 备份计划计费信息列表。 |
| BuyChargeTyp e | String | PREPAY | 实例类型，返回值如下： PREPAY POSTPAY |
| BuyCreateTim estamp | Long | 1634700238000 | 实例购买时间，格式为时间戳。 |
| BuyExpiredTi mestamp | Long | 1716220800000 | 实例到期时间。 说明该参数仅在BuyChargeType 选择PREPAY时显示。 |
| BuySpec | String | small | 实例规格。 |
| ContStorageSi ze | Long | 60391430 | 实例增量备份数据内置存储量。 |
| FullStorageSiz e | Long | 450 | 实例全量备份数据内置存储量。 |
| IsExpired | Boolean | false | 实例是否过期。 说明该参数仅在BuyChargeType 选择PREPAY时显示。 |
| IsFreeBytesUnl imited | Boolean | false | 实例是否为无备份流量上限规格。 |
| PaiedBytes | Long | 0 | 当月付费备份流量合计。 |
| QuotaEndTime stamp | Long | 1640966400000 | 免费备份流量计费周期结束时间。 |
| QuotaStartTim estamp | Long | 1638288000000 | 免费备份流量计费周期开始时间。 |

| TotalFreeBytes | Long | 858993459200 | 当月免费备份总流量。 说明该参数仅在BuyChargeType 选择PREPAY且IsFreeBytesUnlimited为 false时显示。 |
|---|---|---|---|
| UsedFullBytes | Long | 0 | 当月付费全量备份流量。 |
| UsedIncremen tBytes | Long | 35389201 | 当月付费增量备份流量。 |
| RequestId | String | B38B76CB-DCA0- 5B84-A4D6- 7BDC7FBF**** | 请求参数ID。 |
| Success | Boolean | true | 请求是否成功，返回值如下： true：请求成功 false：请求失败 |

**示例**

请求示例

```
http(s)://dbs-api.cn-hangzhou.aliyuncs.com/?Action=DescribeBackupPlanBilling &BackupPlanId=dbssl67c7mx****
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

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

`JSON` 格式

```json
{
    "Item": {
        "IsExpired": false,
        "BuyExpiredTimestamp": 1716220800000,
        "FullStorageSize": 450,
        "BuyCreateTimestamp": 1634700238000,
        "IsFreeBytesUnlimited": false,
        "ContStorageSize": 60391430,
        "BuySpec": "small",
        "BuyChargeType": "PREPAY"
    },
    "RequestId": "B38B76CB-DCA0-5B84-A4D6-7BDC7FBF****",
    "HttpStatusCode": 200,
    "Success": true
}
```

### 备份任务

#### 查看全量备份任务列表

调用DescribeFullBackupList接口查看DBS全量备份任务列表。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeFullBac kupList | 系统规定参数。取值：DescribeFullBackupList。 |
| BackupPlanId | String | 是 | dbstooi01**** | 备份计划ID，可通过调用DescribeBackupPlanList接口获取该参数的值。 |
| PageSize | Integer | 否 | 30 | 每页的记录数，取值30/50/100。 说明默认每页记录数为30。 |
| PageNum | Integer | 否 | 1 | 页码，大于等于0且不超过Integer的最大值，默认值为0。 |
| RegionId | String | 否 | cn-hangzhou | 地域ID。 |
| ClientToken | String | 否 | ETnLKlblzczshOT UbOCzxxxxxxx | 用于保证请求的幂等性，防止重复提交请求。 |

| ShowStorageTyp e | Boolean | 否 | true | 是否显示存储类型。 说明默认true。 |
|---|---|---|---|---|
| BackupSetId | String | 否 | 1ibh2f5u**** | 备份集ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| ErrCode | String | Param.NotFound | 错误码。 |
| ErrMessage | String | The specified parameter %s value is not valid. | 错误信息。 |
| HttpStatusCod e | Integer | 200 | HTTP状态码。 |
| Items | Array of FullBackupFile |  | 全量备份任务详情。 |
| FullBackupFile |  |  |  |
| BackupObjects | String | [{\"DBName\":\"tes t\"}] | 备份对象。 |
| BackupSetExpi redTime | Long | 1646813439000 | 备份集保留到期时间。取值1554560477000。 |
| BackupSetId | String | 1ibh2f5u**** | 备份集ID。 |
| BackupSize | Long | 151 | 备份大小。 |
| BackupStatus | String | finish | 备份任务状态，返回值如下： schedule：初始化中 running：运行中 finish：完成 stop：失败 pause：暂停 |
| CreateTime | Long | 1583740896000 | 任务开始时间。取值：1554560477000。 |
| EndTime | Long | 1583741465000 | 备份结束时间。取值：1554560477000。 |
| ErrMessage | String | NULL | 错误信息。 |

| FinishTime | Long | 1583741466000 | 任务结束时间。取值：1554560477000。 |
|---|---|---|---|
| SourceEndpoin tIpPort | String | 100.X.X.10:33204 | 数据库连接地址。 |
| StartTime | Long | 1583741439000 | 备份开始时间。取值：1554560477000。 |
| StorageMetho d | String | Standard | 存储类型，返回值如下： Standard：标准存储 IA：低频访问存储 Archive：归档存储 UNKNOWN：未知，通常是任务未完成时的状态 |
| PageNum | Integer | 1 | 页码。 |
| PageSize | Integer | 10 | 每页的记录数。 |
| RequestId | String | 636BC118-6080- 4119-A6B5- C199CEC1**** | 请求ID。 |
| Success | Boolean | true | 请求是否成功，返回值如下： true：请求成功 false：请求失败 |
| TotalElements | Integer | 1 | 总全量备份任务数。 |
| TotalPages | Integer | 1 | 总页数。 |

**示例**

请求示例

```
http(s)://dbs-api.cn-hangzhou.aliyuncs.com/?Action=DescribeFullBackupList &BackupPlanId=dbstooi01****
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

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

`JSON` 格式

```json
{
 "RequestId": "636BC118-6080-4119-A6B5-C199CEC1****",
 "PageSize": 30,
 "PageNum": 0,
 "HttpStatusCode": 200,
 "TotalElements": 1,
 "TotalPages": 1,
 "Items": {
  "FullBackupFile": [
   {
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
   }
```

]

```json
 },
 "Success": true
}
```

#### 查看增量备份任务列表

调用DescribeIncrementBackupList接口查看DBS增量备份任务列表。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeIncrem entBackupList | 系统规定参数。取值：DescribeIncrementBackupList 。 |
| BackupPlanId | String | 是 | dbsqdss5tmh*** * | 备份计划ID，可通过调用DescribeBackupPlanList接口获取该参数的值。 |
| PageSize | Integer | 否 | 30 | 每页的记录数，取值30/50/100。 说明默认每页记录数为30。 |
| PageNum | Integer | 否 | 1 | 页码，大于等于0且不超过Integer的最大值，默认值为0。 |
| RegionId | String | 否 | cn-hangzhou | 地域ID。 |
| ClientToken | String | 否 | ETnLKlblzczshOT UbOCzxxxxxxx | 用于保证请求的幂等性，防止重复提交请求。 |
| ShowStorageTyp e | Boolean | 否 | true | 是否显示存储类型。 说明默认true。 |
| StartTimestamp | Long | 否 | 1570701361528 | 开始备份时间。 |
| EndTimestamp | Long | 否 | 1570701361528 | 结束备份时间。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| ErrCode | String | Param.NotFound | 错误码。 |
| ErrMessage | String | The specified parameter %s value is not valid. | 错误信息。 |

| HttpStatusCod e | Integer | 200 | HTTP状态码。 |
|---|---|---|---|
| Items | Array of IncrementBac kupFile |  | 增量备份任务详情。 |
| IncrementBac kupFile |  |  |  |
| BackupSetExpi redTime | Long | 1710468872000 | 备份集保留到期时间。取值1554560477000。 |
| BackupSetId | String | mysql-bin.00**** | 备份集ID。 |
| BackupSetJobI d | String | 1hv5g9wk4**** | 备份集的JobID。 |
| BackupSize | Long | 412032 | 备份大小。 |
| BackupStatus | String | COMPLETED | 备份任务状态，返回值如下： INIT：未启动 FILLING：备份中 COMPLETED：完成 UNCOMPLETED：未完成 |
| EndTime | Long | 1647396866000 | 备份结束时间。取值：1554560477000。 |
| SourceEndpoin tIpPort | String | 172.XX.103.1:43XX | 数据库连接地址。 |
| StartTime | Long | 1647375263000 | 备份开始时间。取值：1554560477000。 |
| StorageMetho d | String | Standard | 存储类型，返回值如下： Standard：标准存储 IA：低频访问存储 Archive：归档存储 UNKNOWN：未知，通常是任务未完成时的状态 |
| PageNum | Integer | 0 | 页码。 |
| PageSize | Integer | 30 | 每页的记录数。 |
| RequestId | String | 8D26CA51-35B8- 5155-8818- F40C2F27**** | 请求ID。 |

| Success | Boolean | true | 请求是否成功，返回值如下： true：请求成功 false：请求失败 |
|---|---|---|---|
| TotalElements | Integer | 138 | 增量备份任务总数。 |
| TotalPages | Integer | 5 | 总页数。 |

**示例**

请求示例

```
http(s)://dbs-api.cn-hangzhou.aliyuncs.com/?Action=DescribeIncrementBackupList &BackupPlanId=dbsqdss5tmh****
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

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

`JSON` 格式

```json
{
    "RequestId": "8D26CA51-35B8-5155-8818-F40C2F27****",
    "PageSize": 30,
    "PageNum": 0,
    "HttpStatusCode": 200,
    "TotalElements": 138,
    "TotalPages": 5,
    "Items": {
        "IncrementBackupFile": [
            {
                "SourceEndpointIpPort": "172.XX.103.1:43XX",
                "EndTime": 1647396866000,
                "BackupSetJobId": "1hv5g9wk4****",
                "BackupSize": 412032,
                "StartTime": 1647375263000,
                "BackupSetExpiredTime": 1710468872000,
                "BackupSetId": "mysql-bin.00****",
                "BackupStatus": "COMPLETED"
            }
```

]

```json
    },
    "Success": true
}
```

### 恢复任务

#### 创建恢复任务

调用CreateRestoreTask接口，创建DBS恢复任务。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | CreateRestoreTa sk | 系统规定参数。取值：CreateRestoreTask。 |
| BackupPlanId | String | 是 | dbs1hvb0ww*** * | 备份计划ID，可通过调用DescribeBackupPlanList接口获取该参数的值。 |

| DestinationEndp ointInstanceTyp e | String | 是 | RDS | 数据库所在位置，取值如下： RDS ECS Express：通过专线/VPN网关/智能网关接入的数据库 Agent：通过备份网关接入的数据库 DDS：云MongoDB Other：通过IP:Port直连的数据库 |
|---|---|---|---|---|
| RestoreTaskNam e | String | 是 | test | 恢复任务名称。 |
| DestinationEndp ointRegion | String | 否 | 100.X.X.10:3320 4 | 数据库地域。 说明 DestinationEndpointInstance Type为RDS、ECS、DDS、Expr ess、Agent时，该参数必传。 |
| DestinationEndp ointInstanceID | String | 否 | rm- bp1p8c29***** | 数据库实例ID。 说明 DestinationEndpointInstance Type为RDS、ECS、DDS、Expr ess时，该参数必传。 |
| DestinationEndp ointIP | String | 否 | rm- bpXXXXX9jv8px ero.mysql.rds.ali yuncs.com | 数据库连接地址。 说明 DestinationEndpointInstance Type为Express、Agent、Othe r，该参数必传。 |
| DestinationEndp ointPort | Integer | 否 | 3306 | 数据库端口。 说明 DestinationEndpointInstance Type为Express、Agent、Othe r、ECS，该参数必传。 |
| DestinationEndp ointDatabaseNa me | String | 否 | test | 数据库名称。 说明数据库类型为PostgreSQL、MongoDB时， 该参数必传。 |

| DestinationEndp ointUserName | String | 否 | test | 数据库账号。 说明数据库类型为Redis， 或者数据库所在位置为Agent且数据库类型为MSSQL时该参数非必须，其他场景均必传。 |
|---|---|---|---|---|
| DestinationEndp ointPassword | String | 否 | Test | 密码。 说明数据库类型为Redis， 或者数据库所在位置为Agent且数据库类型为MSSQL时该参数非必须，其他场景均必传。 |
| BackupGatewayI d | Long | 否 | 43123424 | 备份网关ID。 说明 DestinationEndpointInstance Type为Agent时，该参数必传。 |
| RestoreObjects | String | 否 | [ { "DBName":"待恢复库名", "NewDBName":" 目标待恢复库名", "SchemaName": "待恢复 Schema 名", "NewSchemaNa me":"目标待恢复 Schema 名"}] | 恢复对象。 说明详见下面的RestoreObjects参数定义，当数据库所在位置为Agent时，该参数非必须，其他场景均必传。 |
| RestoreTime | Long | 否 | 1554560477000 | 恢复时间。 |
| BackupSetId | String | 否 | dbs1hvb0wXXX XX | 恢复所使用的全量备份集ID，和 RestoreTime互斥。 |
| DestinationEndp ointOracleSID | String | 否 | test | Oracle SID名称。 说明数据库类型为Oracle 时，该参数必传。 |

| RestoreDir | String | 否 | test | DestinationEndpointInstanceTyp e为Agent且备份计划为MySQL时必传。 |
|---|---|---|---|---|
| RestoreHome | String | 否 | test | 数据库程序目录。 |
| Stages | String | 否 | XXX | 不涉及此参数。 |
| DuplicateConflic t | String | 否 | failure | 同名对象冲突处理方式，取值如下： failure：遇到同名对象则失败（默认值） renamenew：遇到同名对象则重命名 |
| CrossAliyunId | String | 否 | XXX | 不支持此参数使用。 |
| CrossRoleName | String | 否 | XXX | 不支持此参数使用。 |
| RegionId | String | 否 | cn-hangzhou | 地域ID。 |
| ClientToken | String | 否 | ETnLKlblzczshOT UbOCzxxxxxxx | 用于保证请求的幂等性，防止重复提交请求。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| ErrCode | String | InvalidParameterV alid | 错误码。 |
| ErrMessage | String | Need one of the parameter: [RestoreTime, BackupSetId] -> [RestoreTime, BackupSetId] | 错误信息。 |
| HttpStatusCod e | Integer | 200 | HTTP状态码。 |
| RequestId | String | 60AF7C5D-EF4D- 4D48-8FD5- C0823FDF**** | 请求ID。 |
| RestoreTaskId | String | s102h***** | 恢复任务ID。 |
| Success | Boolean | true | 请求是否成功，返回值如下： true：请求成功 false：请求失败 |

**示例**

请求示例

```
http(s)://dbs-api.cn-hangzhou.aliyuncs.com/?Action=CreateRestoreTask &BackupPlanId=dbs1hvb0ww**** &DestinationEndpointInstanceType=RDS &RestoreTaskName=test
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RestoreTaskId>s102h*****</RestoreTaskId> <RequestId>60AF7C5D-EF4D-4D48-8FD5-C0823FDF****</RequestId> <HttpStatusCode>200</HttpStatusCode> <Success>true</Success>
```

`JSON` 格式

```json
{
 "RestoreTaskId": "s102h*****",
 "RequestId": "60AF7C5D-EF4D-4D48-8FD5-C0823FDF****",
 "HttpStatusCode": 200,
 "Success": true
}
```

#### 启动恢复任务

调用StartRestoreTask接口，启动一个DBS恢复任务。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | StartRestoreTas k | 系统规定参数。取值：StartRestoreTask。 |
| RestoreTaskId | String | 是 | s102h7rf**** | 恢复任务ID，可通过调用CreateRestoreTask接口获取该参数的值。 |
| RegionId | String | 否 | cn-hangzhou | 地域ID。 |
| ClientToken | String | 否 | ETnLKlblzczshOT UbOCzxxxxxxx | 用于保证请求的幂等性，防止重复提交请求。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| ErrCode | String | Param.NotFound | 错误码。 |
| ErrMessage | String | The specified parameter %s value is not valid. | 错误信息。 |
| HttpStatusCod e | Integer | 200 | HTTP状态码。 |
| RequestId | String | 60AF7C5D-EF4D- 4D48-8FD5- C0823FDF**** | 请求ID。 |
| RestoreTaskId | String | s102h7rf**** | 恢复任务ID。 |
| Success | Boolean | true | 请求是否成功，返回值如下： true：请求成功 false：请求失败 |

**示例**

请求示例

```
http(s)://dbs-api.cn-hangzhou.aliyuncs.com/?Action=StartRestoreTask &RestoreTaskId=s102h7rf****
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RestoreTaskId>s102h7rf****</RestoreTaskId> <RequestId>60AF7C5D-EF4D-4D48-8FD5-C0823FDF****</RequestId> <HttpStatusCode>200</HttpStatusCode> <Success>true</Success>
```

`JSON` 格式

```json
{
 "RestoreTaskId": "s102h7rf****",
 "RequestId": "60AF7C5D-EF4D-4D48-8FD5-C0823FDF****",
 "HttpStatusCode": 200,
 "Success": true
}
```

#### 查看恢复任务列表

调用DescribeRestoreTaskList接口，查看DBS恢复任务列表。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeRestore TaskList | 系统规定参数。取值：DescribeRestoreTaskList。 |
| BackupPlanId | String | 否 | dbssl67c7mx*** * | 备份计划ID。 |
| RestoreTaskId | String | 否 | s102h7rf**** | 恢复任务ID，支持多个查询，用（,）英文逗号分隔。 |
| PageSize | Integer | 否 | 30 | 每页的记录数，取值30/50/100。 说明默认每页记录数为30。 |
| PageNum | Integer | 否 | 1 | 页码，大于等于0且不超过Integer的最大值，默认值为0。 |
| RegionId | String | 否 | cn-hangzhou | 地域ID。 |
| ClientToken | String | 否 | ETnLKlblzczshOT UbOCzxxxxxxx | 用于保证请求的幂等性，防止重复提交请求。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| ErrCode | String | Param.NotFound | 错误码。 |
| ErrMessage | String | The specified parameter %s value is not valid. | 错误信息。 |
| HttpStatusCod e | Integer | 200 | HTTP状态码。 |
| Items | Array of RestoreTaskD etail |  | 备份计划详情。 |
| RestoreTaskD etail |  |  |  |
| BackupGatewa yId | Long | 0 | 备份网关ID。 |
| BackupPlanId | String | dbssl67c7mx**** | 备份计划ID。 |

| BackupSetId | String | 1jy2oe65x**** | 恢复所使用的全量备份集ID。 |
|---|---|---|---|
| ContinuousRes toreProgress | Integer | 100 | 增量日志恢复进度。 |
| CrossAliyunId | String | 2xxx7778xxxxxxxx xx | 跨阿里云账号备份的UID。 |
| CrossRoleNam e | String | test123 | 跨阿里云账号备份的RAM角色名称。 |
| DestinationEn dpointDatabas eName | String | test | 数据库名称。 |
| DestinationEn dpointInstance ID | String | rm- uf6d8gt9vwvrc**** | 数据库实例ID。 |
| DestinationEn dpointInstance Type | String | RDS | 数据库所在位置，取值如下： RDS ECS Express：通过专线/VPN网关/智能网关接入的数据库 Agent：通过备份网关接入的数据库 DDS：云MongoDB Other：通过IP:Port直连的数据库 |
| DestinationEn dpointIpPort | String | 127.XX.0.1:33XX | 数据库连接地址。 |
| DestinationEn dpointOracleSI D | String | test | Oracle SID名称。 |
| DestinationEn dpointRegion | String | cn-hangzhou | 数据库地域。 |
| DestinationEn dpointUserNa me | String | test | 数据库账号。 |
| ErrMessage | String | NULL | 错误信息。 |
| FullDataRestor eProgress | Integer | 100 | 全量数据恢复进度。 |
| FullStruAfterR estoreProgress | Integer | 100 | 全量结构后置恢复进度。 |
| FullStruforeRe storeProgress | Integer | 100 | 全量结构前置恢复进度。 |

| RestoreDir | String | 100.X.X.10:33204 | 恢复路径。 |
|---|---|---|---|
| RestoreObject s | String | [{ \"DBName\":\"test\ " } ] | 恢复对象。 |
| RestoreStatus | String | running | 恢复任务状态，返回值如下： init：未启动或预检查失败 running：运行中 stop：失败 pause：暂停 check pass：预检查通过 _ |
| RestoreTaskCr eateTime | Long | 1554560477000 | 恢复任务创建时间。 |
| RestoreTaskFi nishTime | Long | 1554560477000 | 恢复任务完成时间。 |
| RestoreTaskId | String | 1jefy7ewt**** | 恢复任务ID。 |
| RestoreTaskN ame | String | cbs34s6**** | 恢复任务名称。 |
| RestoreTime | Long | 1636567334000 | 恢复时间。 |
| PageNum | Integer | 0 | 页码。 |
| PageSize | Integer | 30 | 每页的记录数。 |
| RequestId | String | 1A999262-DB3F- 5368-AA6E- 61AFDA8E**** | 请求ID。 |
| Success | Boolean | true | 请求是否成功，返回值如下： true：请求成功 false：请求失败 |
| TotalElements | Integer | 2 | 总恢复任务数。 |
| TotalPages | Integer | 1 | 总页数。 |

**示例**

请求示例

```
http(s)://dbs-api.cn-hangzhou.aliyuncs.com/?Action=DescribeRestoreTaskList
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

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

`JSON` 格式

| { "RequestId": "1A999262-DB3F-5368-AA6E-61AFDA8E****", "PageSize": 30, "PageNum": 0, "HttpStatusCode": 200, "TotalElements": 2, "TotalPages": 1, "Items": { "RestoreTaskDetail": [ { "RestoreDir": "", "FullStruAfterRestoreProgress": 0, "FullStruforeRestoreProgress": 0, "BackupSetId": "1jy2oe65x****", "RestoreStatus": "check pass", _ "DestinationEndpointInstanceType": "RDS", "RestoreTime": 1636567334000, "DestinationEndpointRegion": "cn-hangzhou", "FullDataRestoreProgress": 0, "RestoreTaskId": "1jefy7ewt****", "DestinationEndpointIpPort": "127.XX.0.1:33XX", "DestinationEndpointUserName": "", "RestoreObjects": " [{\"DBName\":\"rds1 wyp\",\"NewDBName\":\"rds1 wyp\"}]", _ _ "RestoreTaskName": "cbs34s6****", "BackupPlanId": "dbssl67c7mx****", "RestoreTaskCreateTime": 1636623886000, "BackupGatewayId": 0 }, { "RestoreDir": "", "FullStruAfterRestoreProgress": 100, "FullStruforeRestoreProgress": 100, "BackupSetId": "sl67c7mx****", "RestoreStatus": "finish", "DestinationEndpointInstanceType": "RDS", "RestoreTime": 1634720897000, "DestinationEndpointRegion": "cn-shanghai", "FullDataRestoreProgress": 100, "RestoreTaskId": "vbhy7r7o****", "ContinuousRestoreProgress": 100, "DestinationEndpointIpPort": "172.XX.0.1:46XX", "DestinationEndpointUserName": "rdsdt dbsacct", _ "RestoreObjects": " [{\"DBName\":\"rds1 wyp\",\"NewDBName\":\"rds1 wyp\"}]", _ _ "RestoreTaskName": "cbs4225****", "BackupPlanId": "dbssl67c7mx****", "RestoreTaskCreateTime": 1634721021000, "BackupGatewayId": 0, "DestinationEndpointInstanceID": "rm-uf6d8gt9vwvrc****", "RestoreTaskFinishTime": 1634721478000 } ] }, |  |
|---|---|
| 9 > 文档版本：2026072 |  |

```json
    "Success": true
}
```

### 备份网关

#### 查看备份网关列表

调用DescribeBackupGatewayList接口，查看DBS备份网关列表。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeBackup GatewayList | 系统规定参数。取值：DescribeBackupGatewayList 。 |
| Region | String | 是 | cn-hangzhou | DBS地域。 说明专有云默认环境初始化地域。 |
| Identifier | String | 否 | 7213527653217 | 备份网关唯一标识，支持多个查询，用 （,）英文逗号分隔。 |
| PageSize | Integer | 否 | 30 | 每页的记录数，取值30、50、100。 说明默认每页记录数为30。 |
| PageNum | Integer | 否 | 1 | 页码，大于等于0且不超过Integer的最大值，默认值为0。 |
| RegionId | String | 否 | cn-hangzhou | 地域ID。 |
| ClientToken | String | 否 | ETnLKlblzczshOT UbOCzxxxxxxx | 用于保证请求的幂等性，防止重复提交请求。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| ErrCode | String | Param.NotFound | 错误码。 |

| ErrMessage | String | The specified parameter %s value is not valid. | 错误信息。 |
|---|---|---|---|
| HttpStatusCod e | Integer | 200 | HTTP状态码。 |
| Items | Array of BackupGatewa y |  | 备份网关详情。 |
| BackupGatewa y |  |  |  |
| BackupGatewa yCreateTime | Long | 1554560477000 | 备份网关创建时间。 |
| BackupGatewa yId | String | 2321313*** | 备份网关ID。 |
| BackupGatewa yStatus | String | ONLINE | 备份网关状态，返回值如下： ONLINE：在线 OFFLINE：离线 STOPPED：停止 UPGRADING：升级中 |
| DisplayName | String | test | 备份网关显示名称。 |
| Identifier | String | sgdsaj**** | 备份网关唯一标识。 |
| LastHeartbeat Time | Long | 1554560477000 | 上次心跳汇报时间。 |
| Region | String | cn-hangzhou | 地域。 |
| SourceEndpoin tHostname | String | test | 安装备份网关的主机名称。 |
| SourceEndpoin tInternetIP | String | XX.XX.XX.XX | 安装备份网关的主机公网IP。 |
| SourceEndpoin tIntranetIP | String | XX.XX.XX.XX | 安装备份网关的主机私网IP。 |
| PageNum | Integer | 1 | 页码。 |
| PageSize | Integer | 30 | 每页的记录数。 |
| RequestId | String | 46361705-8531- 492F-807E- A97E482D**** | 请求ID。 |

| Success | Boolean | true | 请求是否成功，返回值如下： true：请求成功 false：请求失败 |
|---|---|---|---|
| TotalElements | Integer | 0 | 总备份网关数。 |
| TotalPages | Integer | 1 | 总页数。 |

**示例**

请求示例

```
http(s)://dbs-api.cn-hangzhou.aliyuncs.com/?Action=DescribeBackupGatewayList &Region=cn-hangzhou
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<PageSize>30</PageSize> <RequestId>46361705-8531-492F-807E-A97E482D****</RequestId> <PageNum>0</PageNum> <HttpStatusCode>200</HttpStatusCode> <TotalElements>0</TotalElements> <Items> </Items> <TotalPages>0</TotalPages> <Success>true</Success>
```

`JSON` 格式

```json
{
 "PageSize": 30,
 "RequestId": "46361705-8531-492F-807E-A97E482D****",
 "PageNum": 0,
 "HttpStatusCode": 200,
 "TotalElements": 0,
 "Items": {
  "BackupGateway": []
 },
 "TotalPages": 0,
 "Success": true
}
```

### 备份集下载

#### 查看备份集下载列表

调用DescribeBackupSetDownloadTaskList接口查看DBS备份集下载列表。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeBackup SetDownloadTas kList | 系统规定参数。取值：DescribeBackupSetDownload TaskList。 |
| BackupPlanId | String | 否 | dbssl67c7mx*** * | 备份计划ID，可通过调用DescribeBackupPlanList接口获取该参数的值。 |
| BackupSetDownl oadTaskId | String | 否 | dbstooi01e***** | 备份集下载任务ID。 |
| PageSize | Integer | 否 | 30 | 每页的记录数，取值30/50/100。 说明默认每页记录数为30。 |
| PageNum | Integer | 否 | 1 | 页码，大于等于0且不超过Integer的最大值，默认值为0。 |
| RegionId | String | 否 | cn-hangzhou | 地域ID。 |
| ClientToken | String | 否 | ETnLKlblzczshOT UbOCzxxxxxxx | 用于保证请求的幂等性，防止重复提交请求。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| ErrCode | String | Param.NotFound | 错误码。 |
| ErrMessage | String | The specified parameter %s value is not valid. | 错误信息。 |
| HttpStatusCod e | Integer | 200 | HTTP状态码。 |
| Items | Array of BackupSetDow nloadTaskDeta il |  | 备份计划详情。 |
| BackupSetDow nloadTaskDeta il |  |  |  |

| BackupGatewa yId | Long | 123 | 备份集备份网关，仅自动下载有值。 |
|---|---|---|---|
| BackupPlanId | String | sl67c7mx**** | 备份计划ID。 |
| BackupSetCod e | String | 1h7zrxja0**** | 源备份集编码。 全量：同BackupSetId。 增量：增量文件名。 |
| BackupSetDat aFormat | String | CSV | 备份集下载数据格式，返回值如下： Native SQL CSV JSON |
| BackupSetDat aSize | Long | 151 | 备份集数据大小。 |
| BackupSetDbT ype | String | MySQL | 数据库类型。 |
| BackupSetDow nloadCreateTi me | Long | 1641545488000 | 创建时间。 |
| BackupSetDow nloadDir | String | dbs test _ | 备份集下载服务器目录，仅自动下载有值。 |
| BackupSetDow nloadFinishTi me | Long | 1641545557000 | 完成时间。 |
| BackupSetDow nloadInternetU rl | String | //dbs-137XXX-cn- hangzhou- 1hr5cpbtm****.oss -cn- hangzhou.XXX.com /example345 | 备份集公网下载地址，仅手工下载类型且转换完成的有值。 |
| BackupSetDow nloadIntranetU rl | String | //dbs-137XXX-cn- hangzhou- 1hr5cpbtm****.oss -cn-hangzhou- internal.XXX.com/e xample123 | 备份集内网下载地址，仅手工下载类型且转换完成的有值。 |
| BackupSetDow nloadStatus | String | finish | 备份集下载状态，返回值如下： init：初始化 warning：失败 catched：异常 running：转换中 failed：失败 finish：完成 |

| BackupSetDow nloadTargetTy pe | String | agent | 备份集下载目标类型，仅自动下载有值。 说明 agent表示已安装备份网关。 |
|---|---|---|---|
| BackupSetDow nloadTaskId | String | sl9gpu86*** | 备份集下载任务ID。 |
| BackupSetDow nloadTaskNam e | String | 1h7zrxja0****- ManualFull | 备份集下载任务名称。 |
| BackupSetDow nloadWay | String | manual | 下载类型，返回值如下： manual：手工 auto ：自动 |
| BackupSetId | String | 1h7zrxja0**** | 源备份集ID。 |
| BackupSetJobT ype | String | cbs backup sub fu _ _ _ ll | 源备份集任务类型，返回值如下： cbs backup sub full：逻辑全量任务 _ _ _ cbs backup sub cont：逻辑增量任务 _ _ _ |
| ErrMessage | String | java.lang.IndexOut OfBoundsException . | 异常信息。 |
| PageNum | Integer | 0 | 页码。 |
| PageSize | Integer | 30 | 每页的记录数。 |
| RequestId | String | FB9C5B62-15CA- 5B72-B0F5- F0BDD165**** | 请求ID。 |
| Success | Boolean | true | 请求是否成功，返回值如下： true：请求成功 false：请求失败 |
| TotalElements | Integer | 1 | 总备份集下载记录数。 |
| TotalPages | Integer | 1 | 总页数。 |

**示例**

请求示例

```
http(s)://dbs-api.cn-hangzhou.aliyuncs.com/?Action=DescribeBackupSetDownloadTaskList &BackupPlanId = dbssl67c7mx****
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

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

`JSON` 格式

```json
{
    "RequestId": "FB9C5B62-15CA-5B72-B0F5-F0BDD165****",
    "PageSize": 30,
    "PageNum": 0,
    "HttpStatusCode": 200,
    "TotalElements": 1,
    "TotalPages": 1,
    "Items": {
        "BackupSetDownloadTaskDetail": [
            {
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
            }
```

]

```json
    },
    "Success": true
}
```

#### 设置备份集下载规则

调用ModifyBackupSetDownloadRules接口可以开启、修改、关闭自动下载功能。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ModifyBackupSe tDownloadRules | 系统规定参数。取值：ModifyBackupSetDownloadR ules。 |
| BackupPlanId | String | 是 | dbstooi01**** | 备份计划ID，可通过调用DescribeBackupPlanList接口获取该参数的值。 |
| OpenAutoDownl oad | Boolean | 否 | false | 是否开启自动下载，默认false。 |

| BackupGatewayI d | Long | 否 | 123123123 | 备份集下载备份网关ID。 |
|---|---|---|---|---|
| FullDataFormat | String | 否 | CSV | 备份集下载全量数据格式，取值如下：： Native SQL CSV JSON 说明默认CSV。 |
| IncrementDataF ormat | String | 否 | Native | 备份集下载增量数据格式，取值如下： Native SQL CSV JSON 说明默认Native。 |
| BackupSetDownl oadDir | String | 否 | test | 备份集下载服务器目录。 |
| BackupSetDownl oadTargetType | String | 否 | agent | 备份集下载目标类型 。 说明默认agent，表示已安装备份网关，目前仅此项。 |
| BackupSetDownl oadTargetTypeL ocation | String | 否 | local | 备份集下载目标目录类型，如果是开启自动下载，则必填此项，取值如下： local nas ftp minio 说明默认为local。 |
| RegionId | String | 否 | cn-hangzhou | 地域ID。 |
| ClientToken | String | 否 | ETnLKlblzczshOT UbOCzxxxxxxx | 用于保证请求的幂等性，防止重复提交请求。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| BackupPlanId | String | dbstooi01e**** | 备份计划ID。 |

| ErrCode | String | Param.NotFound | 错误码。 |
|---|---|---|---|
| ErrMessage | String | The specified parameter %s value is not valid. | 错误信息。 |
| HttpStatusCod e | Integer | 200 | HTTP状态码。 |
| RequestId | String | D6E068C3-25BC- 455A-85FE- 45F0B22E**** | 请求ID。 |
| Success | Boolean | true | 请求是否成功，返回值如下： true：请求成功 false：请求失败 |

**示例**

请求示例

```
http(s)://dbs-api.cn-hangzhou.aliyuncs.com/?Action=ModifyBackupSetDownloadRules &BackupPlanId=dbstooi01****
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>D6E068C3-25BC-455A-85FE-45F0B22E****</RequestId> <HttpStatusCode>200</HttpStatusCode> <BackupPlanId>dbstooi01e****</BackupPlanId> <Success>true</Success>
```

`JSON` 格式

```json
{
  "RequestId": "D6E068C3-25BC-455A-85FE-45F0B22E****",
  "HttpStatusCode": 200,
  "BackupPlanId": "dbstooi01e****",
  "Success": true
}
```

#### 创建全量备份集下载任务

调用CreateFullBackupSetDownload接口，创建并启动全量备份集下载任务。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|

| Action | String | 是 | CreateFullBacku pSetDownload | 系统规定参数。取值：CreateFullBackupSetDownloa d。 |
|---|---|---|---|---|
| BackupSetId | String | 是 | dbs1hv***** | 全量备份集ID，可通过调用DescribeBackupSetDownloadTa skList接口获取该参数。 |
| BackupSetDataF ormat | String | 否 | SQL | 全量备份集下载格式，取值如下： Native SQL CSV JSON 说明默认下载格式为CSV。 |
| RegionId | String | 否 | cn-hangzhou | 地域ID。 |
| ClientToken | String | 否 | ETnLKlblzczshOT UbOCzxxxxxxx | 用于保证请求的幂等性，防止重复提交请求。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| BackupSetDow nloadTaskId | String | dbstooi01e***** | 备份集下载任务ID。 |
| ErrCode | String | Param.NotFound | 错误码。 |
| ErrMessage | String | The specified parameter %s value is not valid. | 错误信息。 |
| HttpStatusCod e | Integer | 200 | HTTP状态码。 |
| RequestId | String | D6E068C3-25BC- 455A-85FE- 45F0B22E**** | 请求ID。 |
| Success | Boolean | true | 请求是否成功，返回值如下： true：请求成功 false：请求失败 |

**示例**

请求示例

```
http(s)://dbs-api.cn-hangzhou.aliyuncs.com/?Action=CreateFullBackupSetDownload &BackupSetId=dbs1hv*****
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<BackupSetDownloadTaskId>dbstooi01e*****</BackupSetDownloadTaskId> <RequestId>D6E068C3-25BC-455A-85FE-45F0B22E****</RequestId> <HttpStatusCode>200</HttpStatusCode> <ErrMessage>The specified parameter %s value is not valid.</ErrMessage> <Success>true</Success> <ErrCode>Param.NotFound</ErrCode>
```

`JSON` 格式

```json
{
    "BackupSetDownloadTaskId": "dbstooi01e*****",
    "RequestId": "D6E068C3-25BC-455A-85FE-45F0B22E****",
    "HttpStatusCode": 200,
    "ErrMessage": "The specified parameter %s value is not valid.",
    "Success": true,
    "ErrCode": "Param.NotFound"
}
```

#### 创建增量备份集下载任务

调用CreateIncrementBackupSetDownload接口，创建并启动增量备份集下载任务。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | CreateIncrement BackupSetDownl oad | 系统规定参数。取值：CreateIncrementBackupSetD ownload。 |
| BackupSetId | String | 是 | dbstooi01e***** | 增量备份集ID，可通过调用DescribeBackupSetDownloadTa skList接口获取该参数的值。 |
| BackupSetName | String | 是 | test | 增量文件名称。 |

| BackupSetDataF ormat | String | 否 | Native | 增量备份集下载格式，取值如下： Native SQL CSV JSON 说明默认下载格式为 Native。 |
|---|---|---|---|---|
| RegionId | String | 否 | cn-hangzhou | 地域ID。 |
| ClientToken | String | 否 | ETnLKlblzczshOT UbOCzxxxxxxx | 用于保证请求的幂等性，防止重复提交请求。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| BackupSetDow nloadTaskId | String | dbstooi01e***** | 备份集下载任务ID。 |
| ErrCode | String | Param.NotFound | 错误码。 |
| ErrMessage | String | The specified parameter %s value is not valid. | 错误信息。 |
| HttpStatusCod e | Integer | 200 | HTTP状态码。 |
| RequestId | String | D6E068C3-25BC- 455A-85FE- 45F0B22E**** | 请求ID。 |
| Success | Boolean | true | 请求是否成功，返回值如下： true：请求成功 false：请求失败 |

**示例**

请求示例

```
http(s)://dbs-api.cn-hangzhou.aliyuncs.com/?Action=CreateIncrementBackupSetDownload &BackupSetId=dbstooi01e***** &BackupSetName=test
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>D6E068C3-25BC-455A-85FE-45F0B22E****</RequestId> <HttpStatusCode>200</HttpStatusCode> <BackupSetDownloadTaskId>dbstooi01e*****</BackupSetDownloadTaskId> <Success>true</Success>
```

`JSON` 格式

```json
{
  "RequestId": "D6E068C3-25BC-455A-85FE-45F0B22E****",
  "HttpStatusCode": 200,
  "BackupSetDownloadTaskId": "dbstooi01e*****",
  "Success": true
}
```

### 其他

#### 查看任务标准化错误码信息

调用DescribeJobErrorCode接口，查看DBS任务标准化错误码信息。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeJobError Code | 系统规定参数。取值：DescribeJobErrorCode。 |
| TaskId | String | 是 | dbstooi0**** | 全量备份或者恢复任务ID。 |
| Language | String | 否 | en | 错误信息语言，可选en、cn。 说明默认en。 |
| RegionId | String | 否 | cn-hangzhou | 地域ID。 |
| ClientToken | String | 否 | ETnLKlblzczshOT UbOCzxxxxxxx | 用于保证请求的幂等性，防止重复提交请求。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| ErrCode | String | Param.NotFound | 错误码。 |

| ErrMessage | String | The specified parameter %s value is not valid. | 错误信息。 |
|---|---|---|---|
| HttpStatusCod e | Integer | 200 | HTTP状态码。 |
| Item | Struct |  | 错误码信息。 |
| ErrorCode | String | failed | 错误码。 |
| ErrorMessage | String | Describe preCheck progress failed. | 标准化错误信息。 |
| JobId | String | tooi0**** | 全量备份或者恢复任务ID。 |
| JobState | String | init | 任务状态。 |
| JobType | String | testId | DBS内部任务类型ID。 |
| Language | String | en | 错误信息语言。 |
| RequestId | String | 1FC2F86D-AFF4- 4ED9-BB25- ADDE196C**** | 请求ID。 |
| Success | Boolean | true | 请求是否成功，返回值如下： true：请求成功 false：请求失败 |

**示例**

请求示例

```
http(s)://dbs-api.cn-hangzhou.aliyuncs.com/?Action=DescribeJobErrorCode &TaskId=dbstooi0****
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<Item>
    <Language>en</Language>
    <JobId>tooi0****</JobId>
</Item> <RequestId>1FC2F86D-AFF4-4ED9-BB25-ADDE196C****</RequestId> <HttpStatusCode>200</HttpStatusCode> <Success>true</Success>
```

`JSON` 格式

```json
{
 "Item": {
  "Language": "en",
  "JobId": "tooi0****"
 },
 "RequestId": "1FC2F86D-AFF4-4ED9-BB25-ADDE196C****",
 "HttpStatusCode": 200,
 "Success": true
}
```

#### 查看DBS运行节点网段

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeNodeCi drList | 系统规定参数。取值：DescribeNodeCidrList。 |
| Region | String | 是 | cn-hangzhou | DBS地域。 说明专有云默认环境初始化地域。 |
| RegionId | String | 否 | cn-hangzhou | 地域ID。 |
| ClientToken | String | 否 | ETnLKlblzczshOT UbOCzxxxxxxx | 用于保证请求的幂等性，防止重复提交请求。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| ErrCode | String | Param.NotFound | 错误码。 |
| ErrMessage | String | The specified parameter %s value is not valid. | 错误信息。 |
| HttpStatusCod e | Integer | 200 | HTTP状态码。 |

| InternetIPs | List | "10.X.X.0/24" | 公网网段。 |
|---|---|---|---|
| IntranetIPs | List | "10.X.X.0/24" | 内网网段。 |
| RequestId | String | 5B352E69-E7B1- 4EA7-BB8E- 29FFE969**** | 请求ID。 |
| Success | Boolean | true | 请求是否成功，返回值如下： true：请求成功 false：请求失败 |

**示例**

请求示例

```
http(s)://dbs-api.cn-hangzhou.aliyuncs.com/?Action=DescribeNodeCidrList &Region=cn-hangzhou
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

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

`JSON` 格式

```json
{
 "RequestId": "5B352E69-E7B1-4EA7-BB8E-29FFE969****",
 "InternetIPs": {
  "InternetIP": [
   "118.X.X.0/24",
   "47.X.X.0/24"
```

]

```json
 },
 "HttpStatusCode": 200,
 "IntranetIPs": {
  "IntranetIP": [
   "10.X.X.0/24",
   "10.X.X.0/24",
   "10.X.X.0/24"
```

]

```json
 },
 "Success": true
}
```

#### 查看预检查进度列表

调用DescribePreCheckProgressList接口，查看备份计划预检查进度和恢复任务预检查进度。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribePreChe ckProgressList | 系统规定参数。取值：DescribePreCheckProgressLis t。 |
| BackupPlanId | String | 否 | dbstooi01**** | 备份计划ID。 |
| RestoreTaskId | String | 否 | dbasdsa**** | 恢复任务ID。 |
| RegionId | String | 否 | cn-hangzhou | 地域ID。 |
| ClientToken | String | 否 | ETnLKlblzczshOT UbOCzxxxxxxx | 用于保证请求的幂等性，防止重复提交请求。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| ErrCode | String | Param.NotFound | 错误码。 |

| Items | Array of PreCheckProgr essDetail |  | 进度明细列表。 |
|---|---|---|---|
| PreCheckProgr essDetail |  |  |  |
| BootTime | Long | 1583734969000 | 启动时间，取值：1554560477000。 |
| ErrMsg | String | java.lang.RuntimeE xception: Could not find any schema ...... | 异常信息。 |
| FinishTime | Long | 1583734969000 | 完成时间，取值：1554560477000。 |
| Item | String | CHECK OTHER _ | 检查项编码。 |
| JobId | String | uvk8f6fx**** | 进度ID。 |
| Names | String | CHECK OTHER _ | 检查项分组。 |
| OrderNum | String | 10 | 序号。 |
| State | String | warning | 进度状态，返回值如下： init：初始化 warning：失败 catched：异常 running：运行中 failed：失败 finish：完成 |
| HttpStatusCod e | Integer | 200 | HTTP状态码。 |
| ErrMessage | String | The specified parameter %s value is not valid. | 错误信息。 |
| Progress | Integer | 100 | 预检查进度，取值范围：0~100。 |
| RequestId | String | C4A45FE1-A903- 470D-B113- F12A4DF9**** | 请求ID。 |

| Status | String | failed | 预检查状态，返回值如下： running：运行中 failed：失败 finish：完成 |
|---|---|---|---|
| Success | Boolean | true | 请求是否成功，返回值如下： true：请求成功 false：请求失败 |

**示例**

请求示例

```
http(s)://dbs-api.cn-hangzhou.aliyuncs.com/?Action=DescribePreCheckProgressList
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

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

`JSON` 格式

```json
{
 "Status": "failed",
 "Progress": 20,
 "RequestId": "C4A45FE1-A903-470D-B113-F12A4DF9****",
 "HttpStatusCode": 200,
 "Items": {
  "PreCheckProgressDetail": [
   {
    "Names": "CHECK_MYSQL_PASSOWRD_FORMAT_DETAIL",
    "Item": "CHECK_MYSQL_PASSOWRD_FORMAT",
    "OrderNum": "90",
    "State": "init",
    "BootTime": 1583734969000,
    "JobId": "uvk8f6fx****"
   }
```

]

```json
 },
 "ErrMessage": "java.lang.RuntimeException: Could not find any schema ......",
 "Success": true
}
```

#### PhysicalDeleteResource

物理删除数据库备份服务中的资源。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | Strin g | Query | 否 | cn-hangzhou | 地域ID。 |
| Interrupt | Boole an | Query | 否 | false | 是否中断 |
| Invoker | Strin g | Query | 是 | admin | 调用者 |
| Pk | Strin g | Query | 是 | 259258662544****** | Unknown。 |
| Bid | Strin g | Query | 是 | 26842 | bid |
| Hid | Long | Query | 是 | 1001 | 唯一识别号 |
| Country | Strin g | Query | 是 | CN | 所属国家，默认：CN。 |

| 开发指南·API参 | 考 |  |  |  | 数据库备份 |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| TaskIdenti fier | Strin g | Query | 是 | 001 | 任务标识符 |
| TaskExtra Data | Strin g | Query | 是 | {"retry count": 3, _ "timeout": 60, "priority": "high"} | 任务额外数据 |
| GmtWake up | Strin g | Query | 是 | 08:00 | 唤醒时间 |
| Success | Boole an | Query | 否 | TRUE | 请求是否成功。 |
| Message | Strin g | Query | 否 | ***** | 成功为空，失败返回错误信息。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Interrupt | Boolean | false | 是否中断 |
| Invoker | String | admin | 调用者 |
| Pk | String | 172824053450759 0 | 灾备云实例主键。 |
| Bid | String | 26842 | 请求标识 |
| Hid | Long | 123456 | 唯一识别号 |
| Country | String | 中国 | 国家或地区。 |
| TaskIdentifier | String | 示例值 | 任务标识符 |
| TaskExtraData | String | {"retry count": 3, _ "timeout": 60, "priority": "high"} | 任务额外数据 |
| GmtWakeup | String | 08:00 | 唤醒时间 |
| Success | Boolean | true | 返回状态。 成功：true。 失败：false。 |

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Message | String | success | 附加信息。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=PhysicalDeleteResource &Invoker=admin &Pk=259258662544****** &Bid=26842 &Hid=1001 &Country=CN &TaskIdentifier=001 &TaskExtraData={"retry_count": 3, "timeout": 60, "priority": "high"} &GmtWakeup=
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "GmtWakeup":"",
 "Hid":"",
 "Invoker":"admin",
 "TaskIdentifier":"示例值",
 "Message":"success",
 "TaskExtraData":"{\"retry_count\": 3, \"timeout\": 60, \"priority\": \"high\"}",
 "Country":"中国",
 "Pk":"1728240534507590",
 "Bid":"26842",
 "Interrupt":false,
 "Success":true
}
```

#### LogicalDeleteResource

逻辑删除数据库备份服务中的指定资源。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | Strin g | Query | 否 | cn-hangzhou | 地域ID。 |

| ·API |  |  |  |  |  |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Interrupt | Boole an | Query | 否 | false | 是否中断 |
| Invoker | Strin g | Query | 是 | admin | 调用者 |
| Pk | Strin g | Query | 是 | 259258662544****** | Unknown。 |
| Bid | Strin g | Query | 是 | 26842 | bid |
| Hid | Long | Query | 是 | 9999 | 唯一识别号 |
| Country | Strin g | Query | 是 | CN | 所属国家，默认：CN。 |
| TaskIdenti fier | Strin g | Query | 是 | EX12345 | 任务标识符 |
| TaskExtra Data | Strin g | Query | 是 | {"retryCount": 3, "timeout": 60} | 任务额外数据 |
| GmtWake up | Strin g | Query | 是 | 08:00 | 唤醒时间 |
| Success | Boole an | Query | 否 | TRUE | 请求是否成功。 |
| Message | Strin g | Query | 否 | ***** | 成功为空，失败返回错误信息。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Interrupt | Boolean | false | 是否中断 |
| Invoker | String | admin | 调用者 |
| Pk | String | 172824053450759 0 | 灾备云实例主键。 |
| Bid | String | 26842 | 请求标识 |
| Hid | Long | 123456 | 唯一识别号 |
| Country | String | 中国 | 国家或地区。 |

| 数据库备份 |  |  | 开发指南·API参考 |
|---|---|---|---|
| 参数名称 | 类型 | 示例 | 说明 |
| TaskIdentifier | String | 示例值 | 任务标识符 |
| TaskExtraData | String | {"retryCount": 3, "timeout": 60} | 任务额外数据 |
| GmtWakeup | String | 07:30 | 唤醒时间 |
| Success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| Message | String | success | 附加信息。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=LogicalDeleteResource &Invoker=admin &Pk=259258662544****** &Bid=26842 &Hid=9999 &Country=CN &TaskIdentifier=EX12345 &TaskExtraData={"retryCount": 3, "timeout": 60} &GmtWakeup=
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "GmtWakeup":"07:30",
 "Hid":"",
 "Invoker":"admin",
 "TaskIdentifier":"示例值",
 "Message":"success",
 "TaskExtraData":"{\"retryCount\": 3, \"timeout\": 60}",
 "Country":"中国",
 "Pk":"1728240534507590",
 "Bid":"26842",
 "Interrupt":false,
 "Success":true
}
```

#### DescribeOssStsToken

提供OSS STS Token以实现安全的对象存储访问。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| BackupPla nId | Strin g | Query | 否 | dbstooi01xxxx | 备份计划ID，可通过调用DescribeBackupPlanLi st接口获取该参数的值。 |
| Identifier | Strin g | Query | 否 | temperature | 要查询的事件标识符。 对于弱校验，设备的事件Identifier ，可在控制台中设备所属的产品的功能定义中查看；也可以调用QueryThingModel， 从返回的物模型信息中查看。 对于免校验，必须与设备事件上报时自定义的identifier 一致。 |
| RegionId | Strin g | Host | 否 | cn-hangzhou | 地域ID。 |
| Resource OwnerId | Long | Query | 否 | 345678912345 | 鉴权相关的系统参数，不填。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | 请求ID。 |
| Success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| Message | String | success | 附加信息。 |
| Code | String | 200 | 接口状态或POP错误码。 |

| 数据库备份 |  |  | 开发指南·API参考 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| HttpStatusCod e | Integer | 200 | HTTP状态码。 |
| AccessKeyId | String | 0wNEpMMlzy7s**** | 访问密钥ID。 |
| AccessKeySecr et | String | lml2H****** | 访问密钥。 |
| SecurityToken | String | ******** | STS 安全令牌。 |
| OssPrefix | String | test-prefix/hello- prefix | OSS前缀，与Bucket 、pathFormat 一同组成投递的文件路径。例如 test- prefix 或 test/prefix 。 格式要求：可使用 / 分隔各部分，每个部分都必须满足以下条件： 1. 由大小写字母、数字、下划线（ ）、短划线 _ （-） 、半角句号（.）组成 2. 长度不超过253字符 3. 必须以大小写字母或者数字开头 |
| EnvMode | String | Production | 表示当前环境为生产环境，是正式对外提供服务的环境。 |
| ClientType | String | 1 | 客户端类型。 |

|  | test- |
|---|---|
| test/prefix |  |

|  | prefix |
|---|---|

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeOssStsToken
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
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
}
```

#### DescribeBackupInstances

查询数据库备份实例列表。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | Strin g | Query | 否 | cn-hangzhou | 地域ID。 |
| BackupPla nId | Strin g | Query | 否 | dbstooi01xxxx | 备份计划ID，可通过调用DescribeBackupPlanLi st接口获取该参数的值。 |
| Resource OwnerId | Long | Query | 否 | 345678912345 | 鉴权相关的系统参数，不填。 |
| Resource RegionId | Strin g | Query | 否 | cn-hangzhou | 资源所属地域。 |
| PageNum ber | Integ er | Query | 否 | 1 | 页码。 |
| PageSize | Integ er | Query | 否 | 10 | 分页查询时设置的每页行数。 默认值：10。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| BackupInstanc es | Array | ["backup1", "backup2", "backup3"] | 表示一组备份实例的名称或标识列表，用于记录或管理多个备份副本。 |
| -Id | String | 1 | 角色ID。 |
| -Name | String | test | 指标名称。 |
| -JobId | String | 72dcd26b-f12d- 4c27-b3af- 18f6aed5**** | 异步任务ID。 |
| -RegionId | String | cn-hangzhou | 地域ID。 |
| -PayType | String | Postpaid | 实例付费方式，取值： Postpaid：按量付费； Prepaid：包年包月。 |
| -CreateTime | String | 2022 | 创建时间。 |
| -ExpireTime | String | 2018-08- 24T09:55:41Z | 过期时间 |
| -DbType | String | MySQL | 数据库类型。 |
| -ConnectionStr | String | jdbc:mysql://localh ost:3306/mydb? user=root&passwo rd=123456 | 用于连接本地MySQL数据库的连接字符串，指向名为mydb的数据库，使用用户名root和密码 123456进行认证 |
| -OssBucket | String | liveBucket**** | OSS存储Bucket名称。 |
| -Status | String | 1 | 状态。 |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | 请求ID。 |
| Success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| Message | String | success | 附加信息。 |
| TotalBackupIn stanceCount | Integer | 5 | 表示当前系统中总共存在的备份实例数量为5 个。 |

| 开发指南·API参考 |  |  | 数据库备份 |
|---|---|---|---|
| 参数名称 | 类型 | 示例 | 说明 |
| PageNumber | Integer | 1 | 页码。 |
| PageSize | Integer | 10 | 每页行数。 |
| TotalPages | Integer | 1 | 总页数。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeBackupInstances
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"F0A8A039-930D-5EC1-97C8-************",
 "Message":"success",
 "TotalBackupInstanceCount":5,
 "PageSize":10,
 "PageNumber":1,
 "BackupInstances":[
  {
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
  }
```

`],`

```json
 "TotalPages":1,
 "Success":true
}
```

#### ConfigureDuplicaitonBackupPlan

配置数据库复制备份计划。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Bid | Strin g | Query | 是 | 26842 | bid |
| Database Type | Strin g | Query | 是 | MySQL | 指定要查询的数据库类型， 取值： MySQL Oracle PostgreSQL SQLServer |
| StorageRe gion | Strin g | Query | 是 | cn-hangzhou | 存储地域。 当PayType 为pos tpay 时，该参数必选。 |
| Database Region | Strin g | Query | 是 | cn-hangzhou | 数据库地域。 当PayType 为pos tpay 时，该参数必选。 |
| BackupPla nName | Strin g | Query | 是 | dbstooi0******* | 备份计划名称。 |
| SourceEn dpointInst anceID | Strin g | Query | 是 | rm-bp1imrtn6fq7h**** | 数据库实例ID，可通过调用DescribeBackupPlanLi st接口获取该参数的值。 SourceEndpoint .InstanceType 为 RDS 、ECS 、D DS 、Express 时，该参数必传。 |
| RegionId | Strin g | Host | 否 | cn-hangzhou | 地域ID。 |
| Resource OwnerId | Long | Query | 是 | 345678912345 | 鉴权相关的系统参数，不填。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | 请求ID。 |

| 开发指南·API参考 |  |  | 数据库备份 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| Message | String | success | 附加信息。 |
| BackupPlanId | String | dbs1h****usfa | 备份计划ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=ConfigureDuplicaitonBackupPlan &Bid=26842 &DatabaseType=MySQL &StorageRegion=cn-hangzhou &DatabaseRegion=cn-hangzhou &BackupPlanName=dbstooi0******* &SourceEndpointInstanceID=rm-bp1imrtn6fq7h**** &ResourceOwnerId=345678912345
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"F0A8A039-930D-5EC1-97C8-************",
 "Message":"success",
 "BackupPlanId":"dbs1h****usfa",
 "Success":true
}
```

#### CheckResource

用于验证数据库备份服务中资源的可用性及状态。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | Strin g | Query | 否 | cn-hangzhou | 地域ID。 |

| 数据库备份 |  |  |  |  | 开发指南·API参考 |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Interrupt | Boole an | Query | 否 | false | 是否中断 |
| Invoker | Strin g | Query | 是 | admin | 调用者 |
| Pk | Strin g | Query | 是 | 259258662544****** | Unknown。 |
| Bid | Strin g | Query | 是 | 26842 | bid |
| Hid | Long | Query | 是 | 1001 | 唯一识别号 |
| Country | Strin g | Query | 是 | CN | 所属国家，默认：CN。 |
| TaskIdenti fier | Strin g | Query | 是 | 001 | 任务标识符 |
| TaskExtra Data | Strin g | Query | 是 | {"retry count": 3, _ "timeout": 60} | 任务额外数据 |
| GmtWake up | Strin g | Query | 是 | 08:00 | 唤醒时间 |
| Success | Boole an | Query | 否 | TRUE | 请求是否成功。 |
| Message | Strin g | Query | 否 | ***** | 成功为空，失败返回错误信息。 |
| Level | Long | Query | 否 | 1 | 级别。 |
| Url | Strin g | Query | 否 | https://img.alicdn.com/tf s/TB1Wo7eXAvoK1RjSZF DXXXY3pXa-2512- 3509.jpg | 本字段和body字段二选一，不可同时透传或同时为空。 图片链接（长度不超 2048，不支持 base64）。 |
| Prompt | Strin g | Query | 否 | 我不理解您的意思，请再说一遍 | 提示信息 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Interrupt | Boolean | false | 是否中断 |

| 开发指南·API参考 |  |  | 数据库备份 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Invoker | String | admin | 调用者 |
| Pk | String | 172824053450759 0 | 灾备云实例主键。 |
| Bid | String | 26842 | 请求标识 |
| Hid | Long | 123456 | 唯一识别号 |
| Country | String | 中国 | 国家或地区。 |
| TaskIdentifier | String | USER LOGIN _ | 任务标识符 |
| TaskExtraData | String | {"retry count": 3, _ "timeout": 300} | 任务额外数据 |
| GmtWakeup | String | 08:00 | 唤醒时间 |
| Success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| Message | String | success | 附加信息。 |
| Level | Long | 0 | 包括 FATAL、ERROR、WARNING 和 CRITICAL。 |
| Url | String | http://temp- testbucket.oss-cn- shanghai.aliyuncs. com/aivideocensor/ ****.jpg | 视频截图的地址。 |
| Prompt | String | OK | 提示信息 |

**示例**

请求示例

```
&Invoker=admin &Pk=259258662544****** &Bid=26842 &Hid=1001 &Country=CN &TaskIdentifier=001 &TaskExtraData={"retry_count": 3, "timeout": 60} &GmtWakeup=
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "GmtWakeup":"08:00",
 "Hid":"",
 "TaskIdentifier":"USER_LOGIN",
 "Message":"success",
 "Interrupt":false,
 "Success":true,
 "Url":"http://temp-testbucket.oss-cn-shanghai.aliyuncs.com/aivideocensor/****.jpg",
 "Invoker":"admin",
 "TaskExtraData":"{\"retry_count\": 3, \"timeout\": 300}",
 "Country":"中国",
 "Level":0,
 "Prompt":"OK",
 "Pk":"1728240534507590",
 "Bid":"26842"
}
```

## SDK参考

### SDK概览

**SDK最新版本号**

1.0.13

**SDK支持列表**

PHP Composer：https://packagist.org/packages/alibabacloud/sdk SDK Github：https://github.com/aliyun/openapi-sdk-php Python Pypi：https://pypi.org/project/aliyun-python-sdk-dbs/ SDK Github：https://github.com/aliyun/aliyun-openapi-python-sdk Java Maven：https://oss.sonatype.org/#nexus-search;quick~aliyun-java-sdk-dbs SDK Github：https://github.com/aliyun/aliyun-openapi-java-sdk C++ SDK Github：https://github.com/aliyun/aliyun-openapi-cpp-sdk Go SDK Github：https://github.com/aliyun/alibaba-cloud-sdk-go C# Nuget：https://www.nuget.org/packages/aliyun-net-sdk-dbs/ SDK Github：https://github.com/aliyun/aliyun-openapi-net-sdk

### 通过Maven依赖使用DBS JAVA

**SDK**

DBS Java SDK主要包括两个核心包，aliyun-java-sdk-core 和 aliyun-java-sdk-dbs, 其中aliyun-javasdk-core的主要作用是为DBS提供Endpoint的自动路由，aliyun-java-sdk-dbs 这个包包含了DBS所有功能的相关类。这2个包的版本号可以选取当前Maven仓库内的最新版本。

**Maven配置**

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

**初始化Client**

`//profile`用来声明`Access Key ID`、`Access Key Secret`以及`DBS`实例的地域信息

```
IClientProfile profile = DefaultProfile.getProfile("cn-hangzhou", "accsessKeyId", "acce ssSecret");
```

`//`通过`profile`初始化一个`client`对象

```
IAcsClient client = new DefaultAcsClient(profile);
```

`//`声明一个`request`对象

```
CreateBackupPlanRequest req = new CreateBackupPlanRequest();
```

`//`以下为`request`的参数设置，例如`CreateBackupPlan`需要`Region`、`DatabaseType`、 `//InstanceClass`、`BackupMethod`、`Period`、`UsedTime`这几个参数

```
req.setRegion("cn-hangzhou"); req.setDatabaseType("MySQL"); req.setInstanceClass("small"); req.setBackupMethod("logical"); req.setPeriod("Month"); req.setUsedTime(1);
```

`//`通过`client`来获得对应`request`的响应

```
CreateBackupPlanResponse response = client.getAcsResponse(req);
```

`//`调用`response`中对应的`get`方法获得返回的参数值，如获取备份计划`ID`

```
String backupPlanId=response.getBackupPlanId();
```

### 获取AccessKey

**获取部门Accesskey**

获取部门Accesskey的方法如下：
1. 管理员登录Apsara Stack控制台。
2. 进入**云管控中心** > **用户中心** > **部门管理**页面。
3. 选择待获取Accesskey的部门，单击**获取****accesskey**，可以获取到该部门AccessKey。
一级部门的Accesskey为系统自动分配，下级部门使用一级部门的Accesskey。

**说明**

**获取个人账号Accesskey**

获取个人账号Accesskey的方法如下：
1. 管理员登录Apsara Stack控制台。
2. 在系统界面右上角，单击当前登录用户的头像，选择**个人信息**。
系统会显示当前用户的AccessKey ID。
3. 在********************栏中单击**显示**，查看AccessKey Secret信息。
