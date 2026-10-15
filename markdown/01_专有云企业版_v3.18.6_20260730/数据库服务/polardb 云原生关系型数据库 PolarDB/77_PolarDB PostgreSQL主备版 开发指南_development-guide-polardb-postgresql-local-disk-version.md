---
title: "云原生关系型数据库 PolarDB PolarDB PostgreSQL主备版 开发指南"
product_version: "v3.18.6-SP2607"
doc_version: "20260729"
pdf_pages: 148
source_pdf: "77_PolarDB PostgreSQL主备版 开发指南_development-guide-polardb-postgresql-local-disk-version.pdf"
source_url: "https://apsara-doc.oss-cn-hangzhou.aliyuncs.com/apsara-pdf/enterprise/v_3_18_6_20260730/polardb/zh/development-guide-polardb-postgresql-local-disk-version.pdf"
converter: line-classifier (PyMuPDF)
---

# 云原生关系型数据库 PolarDB PolarDB PostgreSQL主备版 开发指南

PolarDB PostgreSQL主备版开发指云原生数据库

## API参考

### API概览

简单描述各个API。

**PolarDB实例管理**

| API | 描述 |
|---|---|
| CreateDBInstance | 创建实例。 |
| DeleteDBInstance | 释放实例。 |
| RestartDBInstance | 重启实例。 |
| DescribeDBInstanceAttribute | 查看实例属性。 |
| DescribeDBInstances | 查询实例列表。 |
| ModifyDBInstanceSpec | 变更实例配置。 |
| AllocateInstancePublicConnection | 申请外网连接地址。 |
| ReleaseInstancePublicConnection | 释放外网连接地址。 |
| SwitchDBInstanceNetType | 申请内网连接地址。 |
| DescribeDBInstanceNetInfo | 查看所有连接地址。 |
| ModifyDBInstanceConnectionString | 修改连接地址。 |
| ModifyDBInstanceConnectionMode | 修改PolarDB实例访问模式。 |
| ModifyDBInstanceNetworkType | 修改PolarDB实例网络类型。 |
| DescribeDBInstanceIPArrayList | 查看PolarDB实例IP白名单。 |
| ModifySecurityIps | 修改PolarDB实例IP白名单。 |

PolarDB PostgreSQL主备版开发指云原生数据库

| DescribeRegions | 查询PolarDB地域和可用区信息。 |
|---|---|
| DescribeDBInstanceHAConfig | 查询PolarDB可用区信息和数据复制状态 |
| MigrateToOtherZone | 迁移PolarDB实例可用区。 |
| PurgeDBInstanceLog | 清理PolarDB实例日志。 |
| UpgradeDBInstanceEngineVersion | 升级PolarDB实例版本。 |
| ModifyDBInstanceDescription | 修改PolarDB实例备注。 |
| ModifyDBInstanceMaintainTime | 修改PolarDB实例可维护时间。 |
| ModifyDBInstanceHAConfig | 修改PolarDB实例数据复制和高可用策略。 |
| SwitchDBInstanceHA | 切换PolarDB实例的主备。 |
| CreateReadonlyDBInstance | 创建PolarDB只读实例。 |
| DescribeDBInstanceSSL | 查询实例SSL链路。 |
| ModifyDBInstanceSSL | 修改实例SSL链路。 |
| DescribeDBInstanceTDE | 查询实例数据加密状态。 |
| ModifyDBInstanceTDE | 修改实例数据加密状态。 |

| API | 描述 |
|---|---|
| CreateDatabase | 创建数据库。 |
| DeleteDatabase | 删除数据库。 |
| DescribeDatabases | 查看数据库列表。 |

PolarDB PostgreSQL主备版开发指云原生数据库

| ModifyDBDescription | 修改数据库备注。 |
|---|---|

**PolarDB账号管理**

| API | 描述 |
|---|---|
| CreateAccount | 创建账号。 |
| DeleteAccount | 删除账号。 |
| DescribeAccounts | 查看账号列表。 |
| GrantAccountPrivilege | 授权账号权限。 |
| RevokeAccountPrivilege | 撤销账号权限。 |
| ModifyAccountDescription | 修改账号备注。 |
| ResetAccountPassword | 重置密码。 |
| ResetAccount | 重置账号。 |

**PolarDB备份恢复**

| API | 描述 |
|---|---|
| CreateBackup | 创建备份。 |
| CloneDBInstance | 克隆PolarDB实例。 |
| DescribeBackups | 查看备份列表。 |
| CreateTempDBInstance | 创建临时实例。 |
| DescribeBackupPolicy | 查看备份策略。 |
| DescribeLocalAvailableRecoveryTime | 查询备份可恢复时间范围。 |

PolarDB PostgreSQL主备版开发指云原生数据库

| ModifyBackupPolicy | 修改备份策略。 |
|---|---|
| RestoreDBInstance | 恢复备份集到实例。 |
| DeleteBackup | 删除数据备份文件。 |

**PolarDB插件管理**

| API | 描述 |
|---|---|
| CreateExtensions | 安装插件。 |
| DescribeExtensions | 查询插件详情。 |
| UpdateExtensions | 更新插件。 |
| DeleteExtensions | 卸载插件。 |

**PolarDB监控管理**

| API | 描述 |
|---|---|
| DescribeResourceUsage | 查看实例资源使用情况。 |
| DescribeDBInstancePerformance | 查看实例性能数据。 |
| DescribeDBInstanceMonitor | 查询监控行为。 |
| ModifyDBInstanceMonitor | 修改监控行为。 |

**PolarDB参数管理**

| API | 描述 |
|---|---|
| DescribeParameterTemplates | 查看数据库参数模板。 |
| DescribeParameters | 查看当前实例数据库参数运行列表。 |

PolarDB PostgreSQL主备版开发指云原生数据库

| ModifyParameter | 修改数据库参数列表。 |
|---|---|

**PolarDB日志管理**

| API | 描述 |
|---|---|
| DescribeSlowLogs | 查看慢日志列表。 |
| DescribeSlowLogRecords | 查看慢日志明细。 |
| DescribeErrorLogs | 查看错误日志。 |
| DescribeBinlogFiles | 查看BINLOG日志。 |
| DescribeSQLCollectorPolicy | 查询SQL审计功能是否开启。 |
| ModifySQLCollectorPolicy | 切换SQL采集状态。 |
| DescribeSQLLogRecords | 查询SQL审计日志。 |
| DescribeSQLLogFiles | 查询SQL审计文件列表。 |

**PolarDB数据迁移**

| API | 描述 |
|---|---|
| CreateUploadPathForSQLServer | 获取文件上传地址。 |
| DescribeFilesForSQLServer | 查看数据文件列表。 |
| DescribeImportsForSQLServer | 查看导入列表。 |
| ImportDatabaseBetweenInstances | 其他实例迁入。 |
| CancelImport | 取消迁移。 |

**PolarDB标签管理**

PolarDB PostgreSQL主备版开发指云原生数据库

| API | 描述 |
|---|---|
| AddTagsToResource | 绑定标签。 |
| DescribeTags | 查询标签。 |
| RemoveTagsFromResource | 解绑标签。 |

### 调用方式

#### 请求结构

本章介绍云数据库PolarDB API的请求结构。

**服务地址**

PolarDB API的服务接入地址为：polardb.example.com。关于如何获取产品的endpoint，参见获取 ASAPI的endpoint。

**通信协议**

支持通过HTTP或HTTPS通道进行请求通信。为了获得更高的安全性，推荐您使用HTTPS通道发送请求。

**请求方法**

支持HTTP GET方法发送请求，这种方式下请求参数需要包含在请求的URL中

**请求参数**

每个请求都需要指定要执行的操作，即Action参数（例如CreateDatabase），以及每个操作都需要包含的

**字符编码**

请求及返回结果都使用UTF-8字符集进行编码。

#### 公共参数

##### 公共请求参数

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| Format | Stri ng | 否 | 返回值的类型，支持JSON与XML。默认为XML。 |

PolarDB PostgreSQL主备版开发指云原生数据库

| Version | Stri ng | 是 | API版本号，为日期形式：YYYY-MM-DD，本版本对应为2024-01-30。 |
|---|---|---|---|
| AccessKeyId | Stri ng | 是 | 阿里云颁发给用户的访问服务所用的密钥ID。 |
| Signature | Stri ng | 是 | 签名结果串，关于签名的计算方法，请参见签名机制。 |
| SignatureMet hod | strin g | 是 | 签名方式，目前支持HMAC-SHA1。 |
| Timestamp | Stri ng | 是 | 请求的时间戳。日期格式按照ISO8601标准表示，并需要使用UTC时间。格式为：YYYY-MM-DDThh:mm:ssZ；例如，2013-08-15T12:00:00Z（为北京时间2013年8月15日20点0分0秒）。 |
| SignatureVer sion | Stri ng | 是 | 签名算法版本，目前版本是1.0。 |
| SignatureNo nce | Stri ng | 是 | 唯一随机数，用于防止网络重放攻击。用户在不同请求间要使用不同的随机数值。 |

**示例**

```
https://polardb.example.com/ ?Format=xml &Version=2024-01-30 &Signature=Pc5WB8gokVnxxxxx &SignatureMethod=HMAC-SHA1 &SignatureNonce=15215528852396 &SignatureVersion=1.0 &AccessKeyId=key-test &OwnerId=12345678 &Timestamp=2024-07-12T12:00:00Z
```

##### 公共返回参数

用户发送的每次接口调用请求，无论成功与否，系统都会返回一个唯一识别码RequestId给用户。

**示例**

PolarDB PostgreSQL主备版开发指云原生数据库

```xml
<?xml version="1.0" encoding="utf-8"?>
```

<!—结果的根结点`-->` <接口名称`+Response>` <!—返回请求标签`-->`

```xml
    <RequestId>4C4***38-****-****-****-*******6F216</RequestId>
```

<!—返回结果数据`-->` `</`接口名称`+Response>`

#### 返回结果

##### 成功结果

调用API服务后返回数据采用统一格式，返回的HTTP状态码为2xx，代表调用成功。 调用成功返回的数据格式主要有XML和JSON两种，外部系统可以在请求时传入参数来制定返回的数据格式，默认为XML格式。 本文档中的返回示例为了便于用户查看，做了格式化处理，实际返回结果是没有进行换行、缩进等处理的。 XML返回结果包括请求是否成功信息和具体的业务数据。示例如下： <!—结果的根结点`-->` <接口名称`+Response>` <!—返回请求标签`-->`

```xml
<RequestId>4C467B38-****-447D-****-AC04*******16</RequestId>
```

<!—返回结果数据`-->` `</`接口名称`+Response>` JSON示例：

```json
{ "RequestId": "4C467B38-****-447D-****-AC04*******16", /* 返回结果数据 */}
```

##### 错误结果

调用接口出错后，将不会返回结果数据。调用方可根据附表错误代码表来定位错误原因。 当调用出错时，HTTP请求返回一个4xx或5xx的HTTP状态码。 返回的消息体中是具体的错误代码及错误信息。 另外还包含一个全局唯一的请求IDRequestId和一个您该次请求访问的站点IDHostId。在调用方找不到错误原因，可以联系阿里云客服，并提供该HostId和RequestId，以便我们尽快帮您解决问题。 XML示例：

```xml
<Error> <RequestId>8906582E-****-****-A6C4-0E78*******5</RequestId> <HostId>polardb.example.com</HostId> <Code>UnsupportedOperation</Code> <Message>The specified action is not supported.</Message> </Error>
```

JSON示例： PolarDB PostgreSQL主备版开发指云原生数据库

```json
{ "RequestId": "7463B73D-****-4D19-****-6B8*******2EF", "HostId": "polardb.example.com", "Code": "UnsupportedOperation", "Message": "The specified action is not supported." }
```

### 实例管理

#### 创建实例

**描述**

创建一个PolarDB实例。实例规格，详见实例规格表。

**请求参数**

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| Action | Strin g | 是 | 系统规定参数，取值：CreateDBInstance。 |
| RegionId | Strin g | 是 | 数据中心，长度不超过50个字符；通过DescribeRegions查看可用的数据中心。 |
| ZoneId | Strin g | 否 | 可用区ID，通过DescribeRegions查看可用的可用区。 |
| Engine | Strin g | 是 | 数据库类型，取值：PolarDB PG。 _ |
| EngineVersion | Strin g | 是 | PolarDB PG数据库版本号，取值： _ 14 16 17 |
| DBInstanceClass | Strin g | 是 | 实例规格。 |
| DBInstanceStora ge | Integ er | 是 | 自定义存储空间，取值： MySQL双机高可用版为 [5,2000] 。 PolarDB高可用版为 [5,2000] 。 以上版本实例存储空间每5 GB进行递增。单位：GB。 |

PolarDB PostgreSQL主备版开发指云原生数据库

| DBInstanceNetT ype |  | Strin g | 是 | 实例的网络连接类型： Internet：公网 Intranet：私网 |  |  |  |
|---|---|---|---|---|---|---|---|
| DBInstanceDescr iption |  | Strin |  | 实例的描述或备注信息，用于标识或说明实例用途。 内容须以中文或英文字母开头，可包含中文、英文、数字、“ ”、 _ “-” ，长度为2~256字节，且不得以 http:// 或 https:// 开头。 |  |  |  |
|  |  |  |  |  |  | 中文、英文、数字、“ ”、 _ |  |
|  |  | g | 否 | “-” |  |  |  |
| SecurityIPList |  | Strin g | 是 | 允许访问该实例下所有数据库的IP白名单，以英文逗号（,）分隔，不可重复，最多1000个。支持格式包括：%、0.0.0.0/0、单个IP（如 10.23.12.24）或CIDR网段（如10.23.12.24/24，前缀长度范围为 1~32）。其中，0.0.0.0/0表示不限制访问来源。 |  |  |  |
| ClientToken |  | Strin g | 是 | 用于保证幂等性。 |  |  |  |
| InstanceNetwork Type |  | Strin g | 否 | VPC：创建VPC实例；Classic：创建Classic实例；不填，默认创建 Classic实例。 |  |  |  |
| ConnectionMode |  | Strin g | 否 | Performance为标准访问模式；Safty为高安全访问模式；默认为 PolarDB系统分配。 |  |  |  |
| VPCId |  | Strin g | 否 | VPC ID。 |  |  |  |
| VSwitchId |  | Strin g | 否 | VSwitch ID。 |  |  |  |
| PrivateIpAddress |  | Strin g | 否 | 用户可以指定VSwitchId下的vpcIp，如果不输入，系统自动分配。 |  |  |  |
| MultiAVZExPara m |  | Strin g | 否 | 包含主、备两个可用区信息的Json串。 |  |  |  |
| License mode _ |  | Strin g | 否 | 许可方式，默认值为BYOL。 |  |  |  |

PolarDB PostgreSQL主备版开发指云原生数据库

| bucketUrlOpatch Tool | Strin g | 是 | 手工输入。需要用户上传OPatch工具包，无需检查校验和。 说明文件名必须为p6880880 112000 Linux-x86- _ _ 64.zip。 该文件Oracle不定期更新，最新包无法提前获得校验和的值。 |
|---|---|---|---|
| DBName | Strin g | 否 | 数据库名。 |
| Port | Strin g | 否 | 监听端口。默认为1521，取值范围为 [1521,65500] 。 |
| CharacterSetNa me | Strin g | 否 | 可选择的字符集。 |
| DBNationalChara cterSet | Strin g | 否 | 国家字符集，取值： AL16UTF16（默认值） UTF8 |
| BackupRetention Period | Strin g | 否 | 备份保留周期，取值范围为1~7，单位：周。 |

**返回参数**

| 名称 | 类型 | 描述 |
|---|---|---|
| <公共返回参数> | - | 公共返回参数。 |
| DBInstanceId | String | 实例ID。 |
| OrderId | String | 订单ID。 |
| ConnectionString | String | 数据库连接地址。 |
| Port | String | 数据库连接端口。 |

**示例**

XML格式

**返回示例**

PolarDB PostgreSQL主备版开发指云原生数据库

```xml
<CreateDBInstanceResponse> <OrderId>100789370******</OrderId> <ConnectionString>rm-5ob3ye******.o.polardb.rds.inter.env17e.shuguang.com </ConnectionString> <DBInstanceId>polardb-****</DBInstanceId> <port>3433</port> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> </CreateDBInstanceResponse>
```

JSON格式

```json
{ "OrderId": "100789370******", "ConnectionString": "rm-5ob3ye******.o.polardb.rds.inter.env17e.shuguang.com", "DBInstanceId": "polardb-****", "Port": "3433", "RequestId": "1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC"}
```

#### 释放实例

**描述**

释放PolarDB实例接口调用要求如下： 实例状态为运行中。 实例没有被人为锁定。 实例类型包括主实例（按量付费类型）、只读实例、灾备实例和临时实例。

**请求参数**

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| Action | String | 是 | 系统规定参数，取值：DeleteDBInstance。 |
| DBInstanceI d | String | 是 | 实例ID。 |

**返回参数**

| 名称 | 类型 | 描述 |
|---|---|---|
| <公共返回参数> | - | 公共返回参数，具体请参见公共返回参数。 |

**示例**

**请求示例**

```
https://polardb.example.com/?Action=DeleteDBInstance &DBInstanceId=polardb-xxxxx
```

PolarDB PostgreSQL主备版开发指云原生数据库

**返回示例**

XML格式：

```xml
<DeleteDBInstanceResponse> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> </DeleteDBInstanceResponse>
```

JSON格式：

```json
{ "RequestId": "1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC" }
```

#### 重启实例

**描述**

重启实例一般在10s钟内完成。 如果当时有大量的事务需要提交或回滚，可能会延长1分钟左右。 操作必须满足以下条件，否则操作将失败： 实例使用中。 实例没有进行中的备份。

**请求参数**

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| Action | String | 是 | 系统规定参数，取值：RestartDBInstance。 |
| DBInstanceI d | String | 是 | 实例ID。 |

**返回参数**

| 名称 | 类型 | 描述 |
|---|---|---|
| <公共返回参数> | - | 公共返回参数，具体请参见公共返回参数。 |

**示例**

XML格式：

```xml
<RestartDBInstanceResponse> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> </RestartDBInstanceResponse>
```

JSON格式：

```json
{ "RequestId": "1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC"}
```

PolarDB PostgreSQL主备版开发指云原生数据库

#### 查看实例属性

**描述**

查看指定实例的详细属性。

**请求参数**

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| Action | String | 是 | 系统规定参数，取值：DescribeDBInstanceAttribute。 |
| DBInstanc eId | String | 是 | 实例ID，可以一次输入多个，以英文半角“,”分隔；最多传入30个。 |

**返回参数**

| 参数 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Items |  |  | DBInstanceAttribute的参数。 |
| DBInstanceId | String | rm-bpvxxxxx | 实例ID。 |
| DBInstanceType | String | Primary | 实例类型。取值范围： Primary：表示主实例。 Readonly：表示只读实例。 Guard：表示灾备实例。 Temp：表示临时实例。 |
| Category | String | Basic | 实例系列。取值范围： Basic：表示基础版。 Standard：表示高可用版。 Enterprise：表示金融版。 |
| InstanceNetwork Type | String | Classic | 实例的网络类型。取值范围： Classic：表示经典网络。 VPC：表示VPC网络。 |
| RegionId | String | cn-hangzhou | 地域的ID。 |

PolarDB PostgreSQL主备版开发指云原生数据库

| ZoneId | String | cn-hangzhou-a | 可用区的ID。 |
|---|---|---|---|
| ConnectionString | String | rm- 5obp******.o.pol ardb.rds.inter.en v17e.shuguang.c om | 连接地址。 |
| Port | String | 3433 | 应用访问端口。 |
| Engine | String | PolarDB PG _ | 数据库类型。 |
| EngineVersion | String | 16 | 数据库版本。 |
| DBInstanceClass Type | String | x | 实例规格族。取值范围： s：表示共享型。 x：表示通用型。 d：表示独享型。 h：表示独占物理机。 |
| DBInstanceClass | String | polardb.g4.4xlar ge.2 | 实例规格。 |
| DBInstanceMemo ry | Long | 240 | 实例内存，单位为MB。 |
| DBInstanceStora ge | Integer | 10 | 实例存储空间，单位为GB。 |
| DBInstanceNetTy pe | String | Internet | 实例的网络连接类型。取值范围： Internet：表示外网。 Intranet：表示内网。 |
| DBInstanceStatu s | String | Running | 实例状态，详见实例状态表。 |
| DBInstanceDescr iption | String | 测试实例 | 实例描述或备注。 |

PolarDB PostgreSQL主备版开发指云原生数据库

| LockMode | String | Unlock | 实例锁定状态。取值范围： Unlock：表示正常。 ManualLock：表示手动触发锁定。 LockByExpiration：表示实例过期自动锁定。 LockByRestoration：表示实例回滚前的自动锁定。 LockByDiskQuota：表示实例空间满自动锁定。 |
|---|---|---|---|
| LockReason | String | 无 | 被锁定的原因。 |
| DBMaxQuantity | Integer | 200 | 一个实例下最多可以创建的数据库数量。 |
| AccountMaxQuan tity | Integer | 50 | 一个实例下最多可以创建的账号数量。 |
| CreationTime | String | 2025-05- 30T12:11:4Z | 创建时间格式为： YYYY-MM-DD’T’hh:mm:ssZ 2025-05-30T12:11:4Z |
| ExpireTime | String | 无 | 到期时间，按量付费实例无到期时间。 |
| MaintainTime | String | 00:00Z-02:00Z | 实例可维护时间，如表示0点到2点可进行例行维护。 00:00Z-02:00Z |
| AvailabilityValue | String | 100.0% | 查询当前实例的可用性状态，单位为百分比。 |
| MaxIOPS | Integer | 150 | 最大I/O请求次数，即IOPS。 |
| MaxConnections | Integer | 60 | 实例最大并发连接数。 |
| MasterInstanceId | String | null | 主实例的ID，如果没有返回此参数（即为null）则表示该实例是主实例。 |

PolarDB PostgreSQL主备版开发指云原生数据库

| IncrementSource DBInstanceId | String | null | 增量数据来源的实例ID，如灾备实例的增量数据来源是主实例，只读实例的增量数据来源是主实例， 主实例的增量数据来源是NULL。 |
|---|---|---|---|
| GuardDBInstance Id | String | 无 | 该实例如果挂载着灾备实例，即为灾备实例的ID。 |
| TempDBInstance Id | String | 无 | 该实例如果挂载着临时实例，即为临时实例的ID。 |
| ReadOnlyDBInsta nceIds |  | rr-xxxxx | 主实例下挂载的只读实例的ID列表。 |
| DBInstanceId | String | rm-bpxxxxx | 实例的名称。 |
| VpcCloudInstanc eId | String | vpc-xxxxx | 专有网络实例的ID。 |
| ResourceGroupId | String | 365378**** | 资源组ID。 |
| RequestId | String | 1AD222E9-E606- 4A42-BF6D- 8A4442913CEF | 请求ID。 |

DBInstanceAttribute的参数

**说明**

实例主备节点信息请通过另一接口DescribeDBInstanceHAConfig查询。

**示例**

**请求示例**

```
https://polardb.example.com/?Action=DescribeDBInstanceAttribute &DBInstanceId=polardb-xxxxx
```

**正常返回示例返回示例**

JSON格式： PolarDB PostgreSQL主备版开发指云原生数据库

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

**异常返回示例**

JSON格式：

```json
{ "Code":"UnsupportedOperation", "HostId":"polardb.aliyuncs.com", "Message":"The specified action is not supported.", "RequestId":"1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC"}
```

#### 查询实例列表

**描述**

查看实例列表或被RAM授权的实例列表。

**请求参数**

PolarDB PostgreSQL主备版开发指云原生数据库

| 参数 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeDBInst ances | 系统规定参数。取值：DescribeDBInstances |
| RegionId | String | 是 | cn-hangzhou | 地域的ID。 |
| ConnectionMode | String | 否 | Performance | 实例的访问模式。取值范围： Performance：表示标准访问模式。 Safety：表示高安全访问模式。 若不填，默认返回所有。 |
| DBInstanceType | String | 否 | Primary | 实例类型。取值范围： Primary：表示主实例。 Readonly：表示只读实例。 Guard：表示灾备实例。 Temp：表示临时实例。 若不填，默认返回所有。 |
| InstanceNetwork Type | String | 否 | Classic | 实例的网络类型。取值范围： VPC：表示VPC网络。 Classic：表示经典网络。 若不填，默认返回所有。 |
| PageNumber | Intege r | 否 | 1 | 页码。大于0且不超过Integer的最大值，默认值：1。 |
| PageSize | Intege r | 否 | 30 | 每页记录数。取值：30/50/100，默认值： 30。 |
| Tags | String | 否 | {“key1”:”value 1”} | 查询绑定有该标签的实例。传入值格式为JSON string，包括TagKey和TagValue，TagKey 不能为空，TagValue可以为空。格式示例： {“key1”:”value1”} 。 |

**返回参数**

| 参数 | 类型 | 示例值 | 描述 |
|---|---|---|---|

PolarDB PostgreSQL主备版开发指云原生数据库

| PageNumber | Integer | 1 | 页码。 |
|---|---|---|---|
| TotalRecordCount | Integer | 1 | 总记录数。 |
| PageRecordCount | Integer | 1 | 本页实例个数。 |
| Items |  |  | 由实例组成的数组。 |
| └DBInstanceId | String | rm-xxxxx | 实例ID。 |
| └DBInstanceDescriptio n | String | testforRemark s | 实例描述。 |
| └PayType | String | Postpaid | 计费方式。取值范围： Postpaid：表示按量付费 Prepaid：表示包年包月 |
| └DBInstanceType | String | Primary | 实例类型。取值范围： Primary：表示主实例 ReadOnly：表示只读实例 Guard：表示灾备实例 Temp：表示临时实例 |
| └InstanceNetworkType | String | Classic | 实例的网络类型。取值范围： Classic：表示经典网络 VPC：表示VPC网络 |
| └ConnectionMode | String | Performance | 访问模式。取值范围： Performance：表示标准访问模式 Safty：表示高安全访问模式 |
| └RegionId | String | cn-hangzhou | 地域的ID。 |
| └ExpireTime | String | 无 | 到期时间，按量付费实例无到期时间。 |
| └DBInstanceStatus | String | Intranet | 实例状态，详见实例状态表。 |
| └Engine | String | PolarDB PG _ | 数据库类型。 |

PolarDB PostgreSQL主备版开发指云原生数据库

| └DBInstanceNetType | String | Internet | 实例的网络连接类型。取值范围： Internet：表示外网 Intranet：表示内网 |
|---|---|---|---|
| └LockMode | String | Unlock | 实例的锁定状态。取值范围： Unlock：表示正常。 ManualLock：表示手动触发锁定。 LockByExpiration：表示实例过期自动锁定。 LockByRestoration：表示实例回滚前的自动锁定。 LockByDiskQuota：表示实例空间满自动锁定。 |
| └LockReason | String | 无 | 被锁定的原因。 |
| └MasterInstanceId | String | null | 主实例的ID，如果没有返回此参数（即为null）则表示该实例是主实例。 |
| └GuardDBInstanceId | String | 无 | 该实例如果挂载着灾备实例，即为灾备实例的ID。 |
| └TempDBInstanceId | String | 无 | 该实例如果挂载着临时实例，即为临时实例的ID。 |
| └VpcCloudInstanceId | String | vpc-xxxxx | 专有网络实例的ID。 |
| └ReadOnlyDBInstanceI ds |  |  | 无 |
| └DBInstanceId | String | rm-xxxxx | 实例ID。 |
| hostInfos | Array | 无 | 节点信息列表。 |
| └role | String | 0 | 节点角色。取值范围： 0：主节点。 1：备节点。 |
| └ip | String | 30** | 节点IP。 |
| └port | String | 10.XX.XX.14 | 节点实际端口。 |

PolarDB PostgreSQL主备版开发指云原生数据库

| RequestId | String | 1AD222E9- E606-4A42- BF6D- 8A4442913CEF | 请求ID。 |
|---|---|---|---|

**示例**

**请求示例**

```
https://polardb.example.com/?Action=DescribeDBInstances &RegionId=cn-hangzhou &Engine=PolarDB_PG
```

**正常返回示例**

XML格式：

```xml
<DescribeDBInstancesResponse> <PageRecordCount>2</PageRecordCount> <Items> <DBInstance> <DBInstanceDescription>testforRemarks</DBInstanceDescription> <ExpireTime>2014-10-10T16:00:00Z</ExpireTime> <DBInstanceId>polardbmjfirxxxxx</DBInstanceId> <DBInstanceNetType>Internet</DBInstanceNetType> <PayType>Prepaid</PayType> <DBInstanceStatus>Running</DBInstanceStatus> <DBInstanceType>Primary</DBInstanceType> <Engine>PolarDB_PG</Engine> <LockMode>Unlock</LockMode> <LockReason/> <RegionId>cn-hangzhou</RegionId> <ZoneId>cn-hangzhou-a</ZoneId> <MasterInstanceId/> <GuardDBInstanceId/> <TempDBInstanceId/> <ReadOnlyDBInstanceIds> <ReadOnlyDBInstanceId/> </ReadOnlyDBInstanceIds> </DBInstance> </Items> <PageNumber>1</PageNumber> <TotalRecordCount>2</TotalRecordCount> <RequestId>2553A660-E4EB-4AF4-A402-8AFF70A49143</RequestId> </DescribeDBInstancesResponse>
```

JSON格式： PolarDB PostgreSQL主备版开发指云原生数据库

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
}
```

**异常返回示例**

JSON 格式：

```json
{ "Code":"UnsupportedOperation", "HostId":"polardb.aliyuncs.com", "Message":"The specified action is not supported.", "RequestId":"7463B73D-35CC-4D19-A010-6B8D65D242EF"}
```

#### 变更实例配置

**描述**

对实例规格或者存储空间进行配置变更，说明如下： 实例为运行中。 实例当前无正在运行的备份。 实例规格和存储空间必须指定一项。 降低磁盘空间配置，输入的磁盘空间不能小于实际使用空间大小的1.1倍。 当前只支持常规实例、只读实例变更配置，不支持灾备实例、临时实例。

**请求参数**

| 参数 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|

PolarDB PostgreSQL主备版开发指云原生数据库

| Action | String | 是 | ModifyDBInstanc eSpec | 系统规定参数。取值： ModifyDBInstanc eSpec |
|---|---|---|---|---|
| DBInstanceId | String | 是 | rm-bpxxxx | 实例ID。 |
| AccessKeyId | String | 否 | LTAIKw8gqxxxxx | 阿里云颁发给用户的访问服务所用的密钥ID。 |
| ClientToken | String | 否 | ETnLKlblzczshOT UbOCziJZNwHlYB Q | 用于保证幂等性。 |
| DBInstanceClass | String | 否 | polardb.mys2.sm all | 实例规格，详见实例规格表。 |
| DBInstanceStora ge | Integer | 否 | 20 | 自定义存储空间， 单位：GB。每5GB 进行递增，详情请参见 《云数据库 PolarDB > 用户指南中的实例规格》章节。 |
| EffectiveTime | String | 否 | Immediate | 生效时间。参数值如下：- Immediate：立即生效。- MaintainTime: 在可维护时间段内生效。若不传此参数，则默认为 Immediate。 |
| OwnerAccount | String | 否 | testuser@aliyun. com | 用户的主账号。 |

**返回参数**

| 参数 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 1AD222E9-E606-4A42- BF6D-8A4442913CEF | 请求ID。 |

**示例**

**请求示例**

PolarDB PostgreSQL主备版开发指云原生数据库

```
https://polardb.example.com/?Action=ModifyDBInstanceSpec &DBInstanceId=polardb-xxxxx &PayType=Postpaid &DBInstanceStorage=10
```

**正常返回示例返回示例**

XML格式：

```xml
<ModifyDBInstanceSpecResponse> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> </ModifyDBInstanceSpecResponse>
```

JSON格式：

```json
{ "RequestId": "1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC" }
```

**异常返回示例**

JSON格式：

```json
{ "Code":"UnsupportedOperation", "HostId":"polardb.aliyuncs.com", "Message":"The specified action is not supported.", "RequestId":"7463B73D-35CC-4D19-A010-6B8D65D242EF"}
```

#### 申请外网连接地址

**描述**

申请实例的外网连接地址。

**请求参数**

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| Action | Strin g | 是 | 系统规定参数，取值：AllocateInstancePublicConnection。 |
| DBInstanceId | Strin g | 是 | 实例ID。 |
| ConnectionString Prefix | Strin g | 是 | 外网连接地址的前缀。 |
| Port | Strin g | 是 | 外网端口。 |

PolarDB PostgreSQL主备版开发指云原生数据库

**返回参数**

| 名称 | 类型 | 描述 |
|---|---|---|
| <公共返回参数> | - | 公共返回参数，具体请参见公共返回参数。 |

**示例**

**请求示例**

```
https://polardb.example.com/?Action=AllocateInstancePublicConnection &DBInstanceId=polardb-xxxxx &ConnectionStringPrefix=test0001 &Port=3306
```

**返回示例**

XML格式：

```xml
<AllocateInstancePublicConnectionResponse> <RequestId>65BDA532-28AF-4122-AA39-B382721EEE64</RequestId> </AllocateInstancePublicConnectionResponse>
```

JSON格式：

```json
{ "RequestId": "65BDA532-28AF-4122-AA39-B382721EEE64"}
```

#### 释放外网连接地址

**描述**

释放实例的外网连接地址。

**请求参数**

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| Action | String | 是 | 系统规定参数，取值： ReleaseInstancePublicConnection。 |
| DBInstanceId | String | 是 | 实例ID。 |
| CurrentConnection String | String | 是 | 外网连接地址。 |

**返回参数**

PolarDB PostgreSQL主备版开发指云原生数据库

| 名称 | 类型 | 描述 |
|---|---|---|
| <公共返回参数> | - | 公共返回参数，具体请参见公共返回参数。 |

**示例**

**请求示例**

```
https://polardb.example.com/?Action=ReleaseInstancePublicConnection &DBInstanceId=polardb-xxxxx &CurrentConnectionString=test0001.mysql.polardb.example.com
```

**返回示例**

XML格式：

```xml
<ReleaseInstancePublicConnectionResponse> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> </ReleaseInstancePublicConnectionResponse>
```

JSON格式：

```json
{ "RequestId": "1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC" }
```

#### 申请内网连接地址（原内外网切换）

**描述**

用户在必要的时候，可以进行内外网切换，即原来是内网，则会切换到外网，反之亦然。切换后连接地址会发生变化，需要用户修改代码中的连接地址并重启应用。 必须满足以下条件，否则将修改失败： 实例当前状态为使用中。 24小时内切换次数低于20次。

**请求参数**

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| Action | String | 是 | 系统规定参数，取值：SwitchDBInstanceNetType。 |
| DBInstanceId | String | 是 | 实例ID。 |
| ConnectionString Prefix | String | 是 | 新的用户连接，用户连接DB的地（前辍），需惟一性检查，由小写字母数字，中划线组成，字母开头，长度不超过30个字符。 |

**返回参数**

#### 查看所有连接地址

PolarDB PostgreSQL主备版开发指云原生数据库

**描述**

查看指定实例的所有连接地址信息。

**请求参数**

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| Action | Strin g | 是 | 系统规定参数，取值：DescribeDBInstanceNetInfo。 |
| DBInstanceI d | Strin g | 是 | 实例ID。 |

**返回参数**

| 名称 | 类型 | 描述 |
|---|---|---|
| <公共返回参数> |  | 公共返回参数，具体请参见公共返回参数。 |
| DBInstanceNetInfos | List<DBInstanceAttribute> | 实例的连接信息。 |
| InstanceNetworkType | String | VPC：VPC实例； Classic：经典实例。 |

DBInstanceNetInfo的参数

| 名称 | 类型 | 描述 |
|---|---|---|
| ConnectionString | String | DNS连接串。 |
| IPAddress | String | IP地址。 |
| IPType | String | Classic实例可出现：“Inner”，“Public”； VPC实例可出现：“Private”，“Public”。 |
| Port | String | 端口信息。 |
| VPCId | String | VPC ID。 |
| VSwitchId | String | VSwitch ID。 |

PolarDB PostgreSQL主备版开发指云原生数据库

#### 修改连接地址

**描述**

目前PolarDB提供内外网两种连接地址，并能支持特定访问模式下的连接地址并存。

**请求参数**

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| Action | Str ing | 是 | 系统规定参数，取值：ModifyDBInstanceConnectionString。 |
| DBInstanceId | Str ing | 是 | 实例ID。 |
| CurrentConnection String | Str ing | 是 | 实例当前的某个连接串。 |
| ConnectionStringP refix | Str ing | 否 | 目标连接串。 |
| Port | Str ing | 否 | 目标端口。 |

**返回参数**

#### 修改PolarDB实例访问模式

**描述**

目前PolarDB提供两种访问模式： 标准访问模式。 高安全访问模式。

**请求参数**

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| Action | Stri ng | 是 | 系统规定参数，取值：ModifyDBInstanceConnectionMode。 |

PolarDB PostgreSQL主备版开发指云原生数据库

| DBInstance Id | Stri ng | 是 | 实例ID。 |
|---|---|---|---|
| Connection Mode | Stri ng | 是 | Performance为标准访问模式；Safe为高安全访问模式。 |

**返回参数**

#### 修改PolarDB实例网络类型

**描述**

将VPC PolarDB切换成Classic模式，或将Classic PolarDB切换成VPC模式。

**说明**

只有ConnectionMode为“Safety”的Classic实例才能切换成VPC模式。

**请求参数**

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| Action | St ri n g | 是 | 系统规定参数，取值：ModifyDBInstanceNetworkType。 |
| DBInstanceId | St ri n g | 是 | 实例ID。 |
| InstanceNetwor kType | St ri n g | 是 | VPC：VPC实例；Classic：Classic实例。 |
| VPCId | St ri n g | 否 | VPC ID。 |
| VSwitchId | St ri n g | 否 | VSwitch ID；若传入VPCID的值，则该参数必传。 |

PolarDB PostgreSQL主备版开发指云原生数据库

| PrivateIpAddres s | St ri n g | 否 | 用户可以指定VSwitchId下的vpcIp，如果不输入，系统通过vpcId和 VSwitchId 自动分配。 |
|---|---|---|---|

**返回参数**

#### 查看PolarDB实例IP白名单

**描述**

查询允许访问实例的IP名单。

**请求参数**

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| Action | String | 是 | 系统规定参数，取值：DescribeDBInstanceIPArrayList。 |
| DBInstanceI d | String | 是 | 实例ID。 |

**返回参数**

| 名称 | 类型 | 描述 |
|---|---|---|
| <公共返回参数> |  | 公共返回参数，具体请参见公共返回参数 。 |
| Items | List<DBInstanceIP Array> | 实例的IP白名单分组列表。 |

DBInstanceIPArray的参数

| 名称 | 类型 | 描述 |
|---|---|---|
| DBInstanceIPArrayN ame | Strin g | IP白名单分组的名字。 |
| DBInstanceIPArrayAt tribute | Strin g | 默认为空。为了区分不同的属性值，控制台不显示带有“hidden”标签的分组。 |

PolarDB PostgreSQL主备版开发指云原生数据库

| SecurityIPList | Strin g | IP白名单分组下的IP列表，最多1000个以逗号隔开，格式如下： 0.0.0.0/0，10.23.12.24（IP），或者10.23.12.24/24（CIDR模式，无类域间路由，/24表示了地址中前缀的长度，范围[1,32]）。 |
|---|---|---|

#### 修改PolarDB实例IP白名单

**描述**

修改允许访问实例的IP名单。 接口调用必须满足以下条件，否则将失败： 实例运行中。 实例没有被锁定。

**请求参数**

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| Action | Str ing | 是 | 系统规定参数，取值：ModifySecurityIps。 |
| DBInstanceId | Str ing | 是 | 实例ID。 |
| SecurityIps | Str ing | 否 | IP白名单分组下的IP列表，最多1000个以逗号隔开，格式如下： 0.0.0.0/0，10.23.12.24（IP），或者10.23.12.24/24（CIDR模式，无类域间路由，/24表示了地址中前缀的长度，范围[1,32]）。 |
| DBInstanceIPArrayNa me | Str ing | 否 | IP白名单分组的名字，如果不传默认操作“Default”分组。 |
| DBInstanceIPArrayAtt ribute | Str ing | 否 | 默认为空。以区分不同的属性值，控制台不显示带有“hidden”标签的分组。 |

**返回参数**

**示例**

**请求示例**

```
https://polardb.example.com/?Action=ModifySecurityIps &DBInstanceId=polardb-xxxxx &SecurityIps=192.168.1.2
```

**返回示例**

PolarDB PostgreSQL主备版开发指云原生数据库 XML格式：

```xml
<ModifySecurityIpsResponse> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> </ModifySecurityIpsResponse>
```

JSON格式：

```json
{ "RequestId": "1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC"}
```

#### 查询PolarDB地域和可用区信息

**描述**

查看该用户可选的PolarDB地域和可用区。 调用创建实例接口之前，先用该接口查询RegionId。

**请求参数**

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| Action | String | 是 | 系统规定参数，取值： DescribeRegions。 |

**返回参数**

| 名称 | 类型 | 描述 |
|---|---|---|
| <公共返回参数 > | - | 公共返回参数，具体请参见公共返回参数 。 |
| Regions | List<PolarDBRegion> | 返回Region列表。 |

PolarDBRegion

| 名称 | 类型 | 描述 |
|---|---|---|
| RegionId | String | 数据中心。 |
| ZoneId | String | 可用区。 |

**示例**

**请求示例**

PolarDB PostgreSQL主备版开发指云原生数据库

```
https://polardb.example.com/?Action=DescribeRegions
```

**返回示例**

XML格式：

```xml
<DescribeRegionsResponse> <Regions> <PolarDBRegion> <RegionId>cn-hangzhou</RegionId> <ZoneId>cn-hangzhou-a</RegionId> </PolarDBRegion> <PolarDBRegion> <RegionId>cn-hangzhou</RegionId ><ZoneId>cn-hangzhou-b</ZoneId> </PolarDBRegion> </Regions> <RequestId>A36D9720-7902-42A4-B8B9-014A2135E6C3</RequestId> </DescribeRegionsResponse>
```

JSON格式：

```json
{ "Regions":
    { "PolarDBRegion":
        [ {"RegionId": "cn-hangzhou",
            "ZoneId":"cn-hangzhou-a"},
          {"RegionId": "cn-hangzhou",
            "ZoneId":"cn-hangzhou-b"},
             ]},
    "RequestId": "1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC"
}
```

#### 查询PolarDB可用区信息和数据复制状态

**描述**

查询实例的可用区信息和数据复制状态。

**请求参数**

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| Action | String | 是 | 系统规定参数，取值：DescribeDBInstanceHAConfig。 |
| DBInstanceI d | String | 是 | 实例ID。 |

**返回参数**

PolarDB PostgreSQL主备版开发指云原生数据库

| 名称 | 类型 | 描述 |
|---|---|---|
| <公共返回参数> |  | 公共返回参数，具体请参见公共返回参数。 |
| DBInstanceId | String | 实例ID。 |
| SyncMode | String | Semi-sync：半同步；Async：异步。 |
| HAMode | String | RPO：数据持久性优先；RTO：实例可用性优先。 |
| HostInstanceInfos | List<NodeI nfo> | 主备节点信息。 |

NodeInfo的参数

| 名称 | 类型 | 描述 |
|---|---|---|
| NodeId | String | 主备节点的唯一标识。 |
| NodeType | String | Master：主节点；Slave：从节点。 |
| RegionId | String | 数据中心。 |
| ZoneId | String | 可用区。 |
| SyncStatus | String | NotAvailable：不可用，即发生故障；Syncing：同步中，切换可能会导致数据丢失；Synchronized：完成同步；NotSupport：引擎类型或者版本不支持。 |
| LogSyncTime | String | 备库收到的日志时间点。 |
| DataSyncTime | String | 备库当前的数据时间点。 |

#### 迁移PolarDB实例可用区

**描述**

支持将一个实例迁移至其他可用区。 例如实例1目前位于华东 1 （杭州）的cn-hangzhou-a的可用区，调用此接口可以将该实例迁移至杭州的 cn-hangzhou-b。 PolarDB PostgreSQL主备版开发指云原生数据库

**说明**

跨可用区迁移必须迁移至相同物理位置内的。如华东（杭州）可用区内的实例不支持迁移至华北 1（青岛）的可用区。

**请求参数**

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| Action | String | 是 | 系统规定参数。 取值：MigrateToOtherZone。 |
| DBInstanceId | String | 是 | 实例ID。 |
| ZoneId | String | 是 | 通过函数DescribeRegions查看可用的可用区。 |

**返回参数**

**示例**

**请求示例**

```
https://polardb.example.com/?Action=MigrateToOtherZone &DBInstanceId=polardb-xxxxx &ZoneId=cn-hangzhou-b
```

**返回示例**

XML格式：

```xml
<MigrateToOtherZoneResponse> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> </MigrateToOtherZoneResponse>
```

JSON格式：

```json
{ "RequestId": "1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC"}
```

#### 清理PolarDB实例日志

**描述**

对于MySQL类型的实例，将清空实例的所有BINLOG日志。

**请求参数**

PolarDB PostgreSQL主备版开发指云原生数据库

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| Action | String | 是 | 系统规定参数，取值：PurgeDBInstanceLog。 |
| DBInstanceId | String | 是 | 待收缩磁盘空间的实例。 |

**返回参数**

**示例**

**请求示例**

```
https://polardb.example.com/?Action=PurgeDBInstanceLog &DBInstanceId=polardb-xxxxx
```

**返回示例**

XML格式：

```xml
<PurgeDBInstanceLogResponse> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> </PurgeDBInstanceLogResponse>
```

JSON格式：

```json
{ "RequestId": "1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC"}
```

#### 修改PolarDB实例备注

**描述**

修改实例的备注名，用于方便用户记录该实例，比如为该实例修改备注名为阿里云测试环境实例。

**请求参数**

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| Action | Strin g | 是 | 系统规定参数，取值：ModifyDBInstanceDescription。 |
| DBInstanceId | Strin g | 是 | 实例ID。 |
| DBInstanceDesc ription | Stin g | 是 | 实例描述信息。 |

PolarDB PostgreSQL主备版开发指云原生数据库

**返回参数**

**示例**

**请求示例**

```
https://polardb.example.com/?Action=ModifyDBInstanceDescription &DBInstanceId=polardb-xxxxx &DBInstanceDescription=testdescribe
```

**返回示例**

XML格式：

```xml
<ModifyDBInstanceDescriptionResponse> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> </ModifyDBInstanceDescriptionResponse>
```

JSON格式：

```json
{ "RequestId": "1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC"}
```

#### 修改PolarDB实例可维护时间

**描述**

修改实例可例行维护的时间，您可以设置一个业务的一个低峰的时间段。 阿里云如果进行例行维护时间，会在您设置的可维护时间段内进行，对您的业务影响降到最低。

**请求参数**

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| Action | String | 是 | 系统规定参数，取值：ModifyDBInstanceMaintainTime。 |
| DBInstanceI d | String | 是 | 实例ID。 |
| MaintainTim e | String | 是 | 实例的维护时间，取值范围如下： 22:00Z-02:00Z：22点至凌晨2点。 02:00Z-06:00Z：凌晨2点至6点。 06:00-10:00：6点至10点。 10:00Z14:00Z：10点至14点。 14:00Z-18:00Z：14点至18点。 18:00Z-22:00Z：18点至22点。 |

PolarDB PostgreSQL主备版开发指云原生数据库

**返回参数**

**示例**

**请求示例**

```
https://polardb.example.com/?Action=ModifyDBInstanceMaintainTime &DBInstanceId=polardb-xxxxx &MaintainTime=22:00Z-02:00Z
```

**返回示例**

XML格式：

```xml
<ModifyDBInstanceMaintainTimeResponse> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> </ModifyDBInstanceMaintainTimeResponse>
```

JSON格式：

```json
{ "RequestId": "1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC" }
```

#### 修改PolarDB实例数据复制和高可用策略

**描述**

修改实例的数据复制模式和高可用切换策略。

**请求参数**

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| Action | String | 是 | 系统规定参数，取值：ModifyDBInstanceHAConfig。 |
| DBInstance Id | String | 是 | 实例ID。 |
| SyncMode | String | 是 | Semi-sync：半同步；Async：异步。 |
| HAMode | String | 是 | RPO：数据持久性优先；RTO：实例可用性优先。 |

**返回参数**

#### 切换PolarDB实例的主备库

**描述**

PolarDB PostgreSQL主备版开发指云原生数据库 PolarDB主实例是由分布在不同服务器上面的主库和备库组成的。可以通过API进行主备库切换，并由新的主库来承担业务流量。

**请求参数**

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| Action | String | 是 | 系统规定参数，取值：SwitchDBInstanceHA。 |
| DBInstanc eId | String | 是 | 实例ID。 |
| NodeId | String | 是 | 节点的唯一标识，可从DescribeDBInstanceHAConfig接口查询该值。 |
| Force | String | 是 | Yes：强制； No：非强制； 默认为非强制。 |

**返回参数**

#### 创建PolarDB只读实例

**描述**

为某个实例创建一个只读实例，实例要求必须满足以下条件，否则将创建失败。 主实例状态为使用中，且未处于容灾切换状态。 只读实例与主实例必须处于相同地域。 一个PolarDB实例，最多只能有5个只读实例。

**请求参数**

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| Action | String | 是 | 系统规定参数，取值：CreateReadOnlyDBInstance。 |
| RegionId | String | 是 | 数据中心，长度不超过50个字符；通过函数DescribeRegions查看可用的数据中心。 |
| ZoneId | String | 是 | 可用区id，通过函数DescribeRegions查看可用的可用区。 |
| DBInstanceId | String | 是 | 主实例ID。 |

PolarDB PostgreSQL主备版开发指云原生数据库

| EngineVersion | String | 是 | 数据库版本号。必须与主实例相同。取值： 14 16 |
|---|---|---|---|
| DBInstanceClass | String | 是 | 实例规格。 |
| DBInstanceStora ge | Intege r | 是 | 自定义存储空间，取值范围： [5,1000] 。每5G进行递增。单位：GB。 |
| DBInstanceDesc ription | String | 否 | 实例的描述或备注信息，不超过256个字节。 不能以 http:// , https:// 开头。 以中文、英文字母开头，可以包含中文、英文字符、” ”，” -”，数 _ 字字符长度2~256。 |
| ClientToken | String | 是 | 用于保证幂等性。 |
| InstanceNetwork Type | String | 否 | VPC：创建VPC实例。 Classic：创建Classic实例。 不填，默认创建Classic实例。 |
| VPCId | String | 否 | VPC ID。 |
| VSwitchId | String | 否 | VSwitch ID。 |
| PrivateIpAddress | String | 否 | 用户可以指定VSwitchId下的vpcIp，如果不输入，系统通过vpcId,和 VSwitchId自动分配。 |

**返回参数**

| 名称 | 类型 | 描述 |
|---|---|---|
| <公共返回参数> | - | 公共返回参数。 |
| DBInstanceId | String | 实例ID。 |
| OrderId | String | 订单ID。 |
| ConnectionStrin g | String | 数据库连接地址。 |

PolarDB PostgreSQL主备版开发指云原生数据库

| Port | String | 数据库连接端口。 |
|---|---|---|

**示例**

**请求示例**

```
https://polardb.example.com/?Action=CreateReadOnlyDBInstance &RegionId=cn-hangzhou &ZoneId=cn-hangzhou-b &DBInstanceId=polardb-xxxxx &EngineVersion=16 &DBInstanceClass=polardb.g4.4xlarge.2 &DBInstanceStorage=10 &PayType=Postpaid &ClientToken=ETnLK******
```

**返回示例**

XML格式：

```xml
<CreateDBInstanceResponse> <OrderId>10078937023****</OrderId> <ConnectionString>rm-5obp******.o.polardb.rds.inter.env17e.shuguang.com </ConnectionString> <DBInstanceId>polardb-xxxxx</DBInstanceId> <port>3433</port> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> </CreateDBInstanceResponse>
```

JSON格式：

```json
{ "OrderId": "10078937023****", "ConnectionString": "rm-5obp******.o.polardb.rds.inter.env17e.shuguang.com", "DBInstanceId": "polardb-xxxxx", "Port": "3433", "RequestId": "1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC" }
```

#### 查询实例SSL链路

**描述**

调用该接口查询PolarDB实例的SSL链路。

**请求参数**

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| Action | String | 是 | 系统规定参数，取值：DescribeDBInstanceSSL。 |
| DBInstanceId | String | 是 | 实例ID。 |

PolarDB PostgreSQL主备版开发指云原生数据库

**返回参数**

| 名称 | 类型 | 描述 |
|---|---|---|
| <公共返回参数> | - | 公共返回参数，请参见公共返回参数。 |
| ConnectionString | String | 受SSL保护的连接地址。 |
| SSLExpireTime | String | SSL过期的时间，格式为YYYY-MM-DD'T’hh:mm:ssZ。 |
| RequireUpdate | String | Yes：建议用户立即更新；No：不建议用户立即更新。 |
| RequireUpdateRe ason | String | 建议更新的原因。 |

#### 修改实例SSL链路

**描述**

调用改接口修改PolarDB实例SSL链路。

**请求参数**

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| Action | Strin g | 是 | 系统规定参数，取值：ModifyDBInstanceSSL。 |
| DBInstance Id | Strin g | 是 | 实例ID。 |
| Connection String | Strin g | 是 | 每个实例只能有一个连接地址受SSL保护。为目标连接地址创建或更新SSL证书。 |

**返回参数**

| 名称 | 类型 | 描述 |
|---|---|---|
| <公共返回参数> | - | 公共返回参数，具体请参见公共返回参数。 |
| SSLExpireTime | String | SSL过期的时间，格式为YYYY-MM-DD’T’hh:mm:ssZ。 |

PolarDB PostgreSQL主备版开发指云原生数据库

#### 查询实例数据加密状态

**描述**

调用该接口查询PolarDB实例的数据加密状态。

**请求参数**

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| Action | String | 是 | 系统规定参数，取值： DescribeDBInstanceTDE。 |
| DBInstanceId | String | 是 | 实例ID。 |

**返回参数**

| 名称 | 类型 | 描述 |
|---|---|---|
| <公共返回参数> |  | 公共返回参数，具体请参见公共返回参数 。 |
| TDEStatus | String | 实例级别的TDE状态，Enabled：TDE开启；Disabled：TDE关闭。 |
| Databases | List<DataBase> | 由Database组成的数据。 |

DataBase参数：

| 名称 | 类型 | 描述 |
|---|---|---|
| DBName | String | 数据库名称。 |
| TDEStatus | String | 数据库级别的TDE状态，Enabled：TDE开启；Disabled：TDE关闭。 |

#### 修改实例数据加密状态

**描述**

调用该接口修改PolarDB实例的数据加密状态。

**请求参数**

| 2 |  |  | > 文档版本：2026072 |
|---|---|---|---|

PolarDB PostgreSQL主备版开发指云原生数据库

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| Action | String | 是 | 系统规定参数，取值：ModifyDBInstanceTDE。 |
| DBInstanceId | String | 是 | 实例ID。 |
| TDEStatus | String | 是 | Enabled：TDE开启；Disabled：TDE关闭。 |
| DBName | String | 否 | 数据库名，可以一次输入多个，以英文半角“,”分隔；最多传入50 个。 |

**返回参数**

### 数据库管理

#### 创建数据库

**描述**

在某个实例下创建一个新的数据库，接口必须满足以下条件，否则将调用失败： 实例状态运行中。 实例没有被锁定。 没有超出实例最大数据库数量。 实例类型是主实例。

**说明**

PolarDB实例中用户有权限通过SQL做CREATE DATABASE操作，故此接口不支持PolarDB。

**请求参数**

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| Action | String | 是 | 系统规定参数，取值：CreateDatabase。 |
| DBInstanceI d | String | 是 | 实例ID。 |
| DBName | String | 是 | 数据库名，需唯一性检查，由小写字母，数字、下划线组成，字母开头，长度不超过64个字符。 |

PolarDB PostgreSQL主备版开发指云原生数据库

| CharacterSet Name | String | 是 | 字符集，可通过实例详情页的数据库管理页面查看。 |
|---|---|---|---|
| DBDescriptio n | String | 否 | 实例的描述或备注信息，不超过256个字节。 不能以 http:// , https:// 开头。 以中文、英文字母开头，可以包含中文、英文字符、” ”，” -”， _ 数字字符长度2~256。 |

**返回参数**

**示例**

**请求示例**

```
https://polardb.example.com/?Action=CreateDatabase &CharacterSetName=GBK &DBName=testDB &DBInstanceId=polardb-xxxxx
```

**返回示例**

XML格式：

```xml
<CreateDatabaseResponse> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> </CreateDatabaseResponse>
```

JSON格式：

```json
{ "RequestID":"1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC" }
```

#### 删除数据库

**描述**

用户可以删除实例下的的某个数据库。 接口必须满足以下条件，否则将调用失败： 实例状态运行中。 实例类型为主实例。

**说明**

PolarDB实例中用户有权限通过SQL做DROP DATABASE操作，因此接口不支持PolarDB。

**请求参数**

PolarDB PostgreSQL主备版开发指云原生数据库

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| Action | String | 是 | 系统规定参数，取值：DeleteDatabase。 |
| DBInstance Id | String | 是 | 实例ID。 |
| DBName | String | 是 | 数据库名称。 |

**返回参数**

| 名称 | 类型 | 描述 |
|---|---|---|
| <公共返回参数> | - | 公共返回参数，具体请参见公共返回参数。 |

**示例**

**请求示例**

```
https://polardb.example.com/?Action=DeleteDatabase &DBName=testDB &DBInstanceId=polardb-xxxxx
```

**返回示例**

XML格式：

```xml
<DeleteDatabaseResponse> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> </DeleteDatabaseResponse>
```

JSON格式：

```json
{ "RequestId":"1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC" }
```

#### 查看数据库列表

**描述**

查找指定实例、指定DB的DB列表信息。如果查找参数类型错误，返回错误提示，返回数据为空。

**请求参数**

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|

PolarDB PostgreSQL主备版开发指云原生数据库

| Action | String | 是 | 系统规定参数，取值：DescribeDatabases。 |
|---|---|---|---|
| DBInsta nceId | String | 是 | 实例ID。 |
| DBName | String | 否 | 数据库名称。 |
| DBStatu s | String | 否 | 数据库状态，取值范围： Creating：创建中 Running：使用中 Deleting：删除中 |

**返回参数**

| 名称 | 类型 | 描述 |
|---|---|---|
| <公共返回参数> | - | 公共返回参数，具体请参见公共返回参数。 |
| Databases | List<Database> | 由Database组成的数据。 |

DATABASE参数

| 名称 | 类型 | 描述 |
|---|---|---|
| DBName | String | 数据库名称。 |
| DBInstanceId | String | 数据库所属实例ID。 |
| Engine | String | 数据库实例类型。 |
| DBStatus | String | 数据库状态： Creating：创建中 Running：使用中 Deleting：删除中 |
| CharacterSet Name | String | 字符集。 |
| DBDescription | String | 数据库描述。 |

PolarDB PostgreSQL主备版开发指云原生数据库

| Accounts | List<AccountPrivileg eInfo> | 有Accounts组成的list。 |
|---|---|---|
| Account | String | 账号名称。 |
| AccountPrivile ge | String | 账号对该DB具有的权限。 |

AccountPrivilegeInfo参数

| 名称 | 类型 | 描述 |
|---|---|---|
| Account | String | 账号名称。 |
| AccountPrivilege | String | 账号对该DB具有的权限。 |

**示例**

**请求示例**

```
https://polardb.example.com/?Action=DescribeDatabases &DBInstanceId=polardb-xxxxx
```

**返回示例**

XML格式：

```xml
<DescribeDatabasesResponse> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> <Databases> <Database> <Engine>PolarDB_PG</Engine> <DBName>testdb</DBName> <CharacterSetName>utf8</CharacterSetName> <DBStatus>Creating</DBStatus> <DBInstanceId>polardb-xxxxx</DBInstanceId> <Accounts> <AccountPrivilegeInfo></AccountPrivilegeInfo> <Accounts> </Database> </Databases> </DescribeDatabasesResponse>
```

JSON格式： PolarDB PostgreSQL主备版开发指云原生数据库

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
            }
```

#### 修改数据库备注

**描述**

修改数据库名的备注名，用于方便用户记录该实例，比如为该实例修改备注名为“阿里云测试环境实例数据库A”。

**请求参数**

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| Action | String | 是 | 系统规定参数，取值： ModifyDBDescription。 |
| DBInstanceId | String | 是 | 实例ID。 |
| DBName | String | 是 | 数据库名称。 |
| DBDescription | String | 是 | 修改DB备注。 |

**返回参数**

**示例**

**请求示例**

```
https://polardb.example.com/?Action=ModifyDBDescription &DBInstanceId=polardb-xxxxx &DBInstanceDescription=testDBdescribe
```

**返回示例**

XML格式： PolarDB PostgreSQL主备版开发指云原生数据库

```xml
<ModifyDBDescriptionResponse> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> </ModifyDBDescriptionResponse>
```

JSON格式：

```json
{ "RequestId": "1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC" }
```

### 账号管理

#### 创建账号

**描述**

为数据库创建账号，同一个用户实例下，一个账号可以对多个数据库进行操作，同一账号对不同数据库权限可以不一致。 实例/数据库状态要求必须满足以下条件，否则将创建失败： 当前实例状态为运行中。 当前数据库状态为运行中。 当前实例没有被锁定。 没有超出单个实例内的最大账号数量。

**请求参数**

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| Action | Strin g | 是 | 系统规定参数，取值：CreateAccount。 |
| DBInstanceId | Strin g | 是 | 实例ID。 |
| AccountName | Strin g | 是 | 操作账号，需要进行唯一性检查，由小写字母，数字、下划线组成，字母开头，长度不超过16个字符。其他非法字符，请参见禁用关键字表。 |
| AccountPassw ord | Strin g | 是 | 操作密码，由字母、数字或下划线组成，长度为6-32位。 |
| AccountType | Strin g | 否 | 取值为：Normal（普通账号），Super（高权限账号），默认为Normal。 PolarDB有且仅有一个初始账号，其他账号由初始账号连接数据库后创建。 |
| AccountDescr iption | Strin g | 否 | 账号备注，长度不超过256个字符。请注意：开头不能以http://或https:// 开头；必须以中文、英文字母作为开头。可以包含中文、英文字符、” ”，” _ -”，数字字符长度2~256位。 |

PolarDB PostgreSQL主备版开发指云原生数据库

**返回参数**

**示例**

**请求示例**

```
https://polardb.example.com/?Action=CreateAccount &AccountName=testacc02 &AccountPassword=pwxxxxx &DBInstanceId=rds-xxxxx
```

**返回示例**

XML格式：

```xml
<CreateAccountResponse> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> </CreateAccountResponse>
```

JSON格式：

```json
{ "RequestId":"1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC" }
```

#### 删除账号

**描述**

实例状态要求为运行中。

**请求参数**

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| Action | String | 是 | 系统规定参数，取值：DeleteAccount。 |
| DBInstanceI d | String | 是 | 实例ID。 |
| AccountNam e | String | 是 | 操作账号，需惟一性检查，由小写字母，数字、下划线组成，字母开头，长度不超过16个字符。其他非法字符，请参见禁用关键字表。 |

**返回参数**

**示例**

**请求示例**

PolarDB PostgreSQL主备版开发指云原生数据库

```
https://polardb.example.com/?Action=DeleteAccount &DBInstanceId=rds-xxxxx &AccountName=testacc01
```

**返回示例**

XML格式：

```xml
<DeleteAccountResponse> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> </DeleteAccountResponse>
```

JSON格式：

```json
{ "RequestID":"1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC" }
```

#### 查看账号列表

**描述**

查找指定实例、指定DB的账户列表信息或某个指定账号的信息。

**请求参数**

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| Action | Stri ng | 是 | 系统规定参数，取值：DescribeAccounts。 |
| DBInstance Id | Stri ng | 是 | 实例ID。 |
| AccountNa me | Stri ng | 是 | 账号名称。 |

**返回参数**

| 名称 | 类型 | 描述 |
|---|---|---|
| <公共返回参数> |  | 公共返回参数，具体请参见公共返回参数。 |
| Accounts | List<DBInstanceAccount > | 由Account组成的数组。 |

DBInstanceAccount参数 PolarDB PostgreSQL主备版开发指云原生数据库

| 名称 | 类型 | 描述 |
|---|---|---|
| DBInstanceId | String | 账号所属实例ID。 |
| AccountName | String | DB操作账号名称。 |
| AccountStatus | String | 账号状态： Unavailable：不可用 Available：可用 |
| AccountDescription | String | 账号备注信息。 |
| DatabasePrivileges | List<DatabasePrivil ege> | 由DatabasePrivilege组成的数组。 |
| AccountType | String | 账号类型： Normal：普通账号 Super：超级账号 |

DatabasePrivilege参数

| 名称 | 类型 | 描述 |
|---|---|---|
| DBName | String | 数据库名称。 |
| AccountPrivilege | String | DB操作账号名称。 |

**示例**

**请求示例**

```
https://polardb.example.com/?Action=DescribeAccounts &DBInstanceId=polardb-xxxxx
```

**返回示例**

XML格式： PolarDB PostgreSQL主备版开发指云原生数据库

```xml
<DescribeAccountsResponse> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> <Accounts> <DBInstanceAccount> <AccountName>PolarDB_PG</AccountName> <DBInstanceId>testdb</DBInstanceId> <AccountStatus>utf8</AccountStatus> <AccountDescription> </AccountDescription> <DatabasePrivileges> <DatabasePrivilege></DatabasePrivilege> </DatabasePrivileges> <DBInstanceAccount> </Accounts> </DescribeAccountsResponse>
```

JSON格式：

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

#### 授权账号权限

**描述**

授权账号访问数据库、权限：一个账号可关联一个或多个数据库。 如果指定的账号对指定数据库已经具有访问权限，则会直接返回成功。 实例状态要求：运行中。

**请求参数**

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| Action | String | 是 | 系统规定参数，取值：GrantAccountPrivilege。 |
| DBInstanceId | String | 是 | 实例ID。 |
| AccountName | String | 是 | 账号名称。 |
| DBName | String | 是 | 设置与该账号关联的数据库名数据库名称。 |

PolarDB PostgreSQL主备版开发指云原生数据库

| AccountPrivileg e | String | 是 | 账号权限，ReadOnly 只读，ReadWrite读写。 |
|---|---|---|---|

**返回参数**

**示例**

**请求示例**

```
https://polardb.example.com/?Action=GrantAccountPrivilege &AccountName=testacc02 &AccountPrivilege=readwrite &DBName=testdb03 &DBInstanceId=polardb-xxxxx
```

**返回示例**

XML格式：

```xml
<GrantAccountPrivilegeResponse> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> </GrantAccountPrivilegeResponse>
```

JSON格式：

```json
{ "RequestId":"1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC"}
```

#### 撤销账号权限

**描述**

可用该接口删除某个账号对DB的访问权限必须满足以下条件，否则将删除失败： 当前数据库实例状态为运行中。 当前数据库状态为运行中。

**请求参数**

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| Action | String | 是 | 系统规定参数，取值：RevokeAccountPrivilege。 |
| DBInstanc eId | String | 是 | 实例ID。 |
| AccountNa me | String | 是 | 账号名称。 |

PolarDB PostgreSQL主备版开发指云原生数据库

| DBName | String | 是 | 数据库名称。 |
|---|---|---|---|

**返回参数**

**示例**

**请求示例**

```
https://polardb.example.com/?Action=RevokeAccountPrivilege &AccountName=testacc02 &DBName=testdb03 &DBInstanceId=polardb-xxxxx
```

**返回示例**

XML格式：

```xml
<RevokeAccountPrivilegeResponse> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> </RevokeAccountPrivilegeResponse>
```

JSON格式：

```json
{ "RequestId":"1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC"}
```

#### 修改账号备注

**描述**

修改账号的备注名，以方便用户记录该实例，比如将该实例的备注名修改为“阿里云测试环境实例账号A”。

**请求参数**

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| Action | Stri ng | 是 | 系统规定参数，取值：ModifyAccountDescription。 |
| DBInstanceId | Stri ng | 是 | 实例ID。 |
| AccountName | Stri ng | 是 | 操作账号，需唯一性检查，由小写字母，数字、下划线组成，字母开头， 长度不超过16个字符。其他非法字符，请参见禁用关键字表。 |

PolarDB PostgreSQL主备版开发指云原生数据库

| AccountDescr iption | Stri ng | 是 | 修改账号备注。注：不能以http:// , https:// 开头。以中文、英文字母开头。可以包含中文、英文字符、” ”，” -”，数字字符长度2~256位。 _ |
|---|---|---|---|

**返回参数**

| 名称 | 类型 | 描述 |
|---|---|---|
| <公共返回参数> | - | 公共返回参数，具体请参见公共返回参数。 |

**示例**

**请求示例**

```
https://polardb.example.com/?Action=ModifyAccountDescription &DBInstanceId=polardb-xxxxx &AccountName=testacc01 &AccountDescription=testAccoutdescribe
```

**返回示例**

XML格式：

```xml
<ModifyAccountDescription> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> </ModifyAccountDescription>
```

JSON格式：

```json
{ "RequestId": "1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC"}
```

#### 重置密码

**描述**

重置账号的密码必须满足以下条件，否则将操作失败： 当前实例状态：运行中，没有被锁定。

**请求参数**

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| Action | Strin g | 是 | 系统规定参数，取值：ResetAccountPassword。 |
| DBInstanceId | Strin g | 是 | 实例ID。 |

PolarDB PostgreSQL主备版开发指云原生数据库

| AccountNam e | Strin g | 是 | 账号名称。 |
|---|---|---|---|
| AccountPass word | Strin g | 是 | 新密码，由字母、数字或下划线组成，长度为6~32位。 |

**返回参数**

**示例**

**请求示例**

```
https://polardb.example.com/?Action=ResetAccountPassword &AccountName=testacc02 &AccountPassword=pwxxxxx &DBInstanceId=polardb-xxxxx
```

**返回示例**

XML格式：

```xml
<ResetAccountPasswordResponse> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> </ResetAccountPasswordResponse>
```

JSON格式：

```json
{ "RequestId":"1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC"}
```

#### 重置账号

**描述**

重置实例的初始账号。

**请求参数**

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| Action | Strin g | 是 | 系统规定参数，取值：ResetAccount。 |
| DBInstanceI d | Strin g | 是 | 实例ID。 |
| AccountNam e | Strin g | 是 | 账号名称。 |
| AccountPass word | Strin g | 是 | 账号密码。 |

PolarDB PostgreSQL主备版开发指云原生数据库

**返回参数**

| 名称 | 类型 | 描述 |
|---|---|---|
| <公共返回参数> | - | 公共返回参数，具体请参见公共返回参数。 |

### 备份恢复

#### 创建备份

**描述**

可用来创建一个备份，限制一天之内一个实例创建备份不超过10个。 实例状态要求必须满足以下条件，否则将创建失败： 使用中。 上一次备份已经完成。

**请求参数**

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| Action | String | 是 | 系统规定参数，取值：CreateBackup。 |
| DBInstanc eId | String | 是 | 实例ID。 |
| BackupMe thod | String | 否 | Logical：逻辑备份；Physical：物理备份。默认值为Physical，逻辑备份不支持没有DB的实例。 |
| BackupStr ategy | String | 否 | 逻辑备份可选备份范围；db:单库备份；instance:全实例备份，只有在 BackupMethod=Logical的情况下，该入参才有效。 |
| DBName | String | 否 | 逻辑单库备份，数据库名称；只有在 BackupMethod=Logical&BackupStrategy=db的情况下，该入参才有效。 |
| BackupTy pe | String | 否 | Auto：自动计算是全量备份还是增量备份；FullBackup：全量备份。默认值为 Auto。 |

**返回参数**

| 名称 | 类型 | 描述 |
|---|---|---|
| <公共返回参数> | - | 公共返回参数，具体请参见公共返回参数。 |

PolarDB PostgreSQL主备版开发指云原生数据库

**示例**

**请求示例**

```
https://polardb.example.com/?Action= CreateBackup &DBInstanceId=polardb-xxxxx
```

**返回示例**

XML格式：

```xml
<CreateBackupResponse> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> </CreateBackupResponse>
```

JSON格式：

```json
{ "RequestId":"1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC"}
```

#### 克隆PolarDB实例

**描述**

基于现有实例的备份文件或指定时间点克隆出一个带有当时数据的新实例。 实例内的白名单设置、SQL审计设置、阈值报警设置、备份设置、参数设置将和当前实例状态保持一致。 实例内的数据信息与备份文件当前信息一致，克隆PolarDB实例暂时仅支持MySQL引擎。 实例内数据库账号信息克隆将遵循如下方式： 若在克隆时，主实例为高权限账号状态，则克隆出的实例带有该主实例的高权限账号信息。 若克隆时，主实例为普通权限账号状态，则克隆出的实例带有所使用备份文件或时间点当时的账号信息。

**请求参数**

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| Action | String | 是 | 系统规定参数，取值：CloneDBInstance。 |
| DBInstanceId | String | 是 | 实例ID。 |
| BackupId | String | 否 | 备份集ID，可通过查询备份列表接口DescribeBackups获取。 |
| RestoreTime | String | 否 | 用户指定备份保留周期内的任意时间点，如2011-06- 11T16:00:00Z。BackupId和RestoreTime两者至少传入一个。 |
| DBInstanceClas s | String | 否 | 实例规格，详见规格列表附录。可选参数，若不传入，则默认规格和主实例一致。 |

PolarDB PostgreSQL主备版开发指云原生数据库

| DBInstanceStor age | String | 否 | 磁盘空间，默认与主实例一致，单位GB。PolarDB独占物理机规格可传入范围为[3000，3000];其他规格可传入范围为[5,2000]。每5GB 递增。 |
|---|---|---|---|
| InstanceNetwor kType | String | 否 | 网络类型。VPC：创建VPC实例；Classic：创建Classic实例；默认与主实例网络类型一致。 |
| VPCId | String | 否 | VPC ID。 |
| VSwitichId | String | 否 | VSwitichId。 |
| PrivateIpAddres s | String | 否 | 用户可以指定VSwitchId下的vpcIp，如果不输入，系统自动分配。 |

**返回参数**

| 名称 | 类型 | 描述 |
|---|---|---|
| <公共返回参数> | - | 公共返回参数，具体请参见公共返回参数。 |
| DBInstanceId | String | 实例ID。 |
| OrderId | Integer | 订单号。 |

#### 查看备份列表

**描述**

查询实例的备份集。备份集的状态必须是“完成备份”，才能用于恢复。 PolarDB提供备份文件文件下载： 当DownloadLink为NULL时，表示PolarDB没有提供下载链接URL； 当DownloadLink不为NULL时，用户可以根据此URL，通过wget（请加双引号）、浏览器、编写程序下载备份文件，此URL已设置过期时间LinkExpiredTime，请在过期时间之前使用。 若过期，用户在下载时，将会出现如下错误码：

```xml
<?xml version="1.0" encoding="UTF-8" ?><Error><Code>AccessDenied</Code> <Message>Request has expired.</Message><Expires>2012-12-25T09:47:52.000Z</Expires><Se rverTime>2012-12-25T09:49:00.000Z</ServerTime> <RequestId>50D9768CA801C2F102005C70</RequestId><HostId>oss-test.aliyuninc.com</HostId></Error>
```

**请求参数**

PolarDB PostgreSQL主备版开发指云原生数据库

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| Action | Strin g | 是 | 系统规定参数，取值：DescribeBackups。 |
| DBInstanceI d | Strin g | 是 | 实例ID。 |
| BackupId | Integ er | 否 | 备份集ID。 |
| BackupStatu s | Strin g | 否 | 备份集状态，取值范围：Success：完成备份；Failed：备份失败。 |
| BackupMode | Strin g | 否 | 备份类型，取值范围：Automated：常规任务；Manual：临时任务。 |
| StartTime | Strin g | 是 | 查询开始时间，格式如：2011-06-11T15:00Z。 |
| EndTime | Strin g | 是 | 查询结束时间，格式如：2011-06-11T16:00Z，且大于查询开始时间。 |
| PageSize | Integ er | 否 | 每页记录数，取值：30/50/100默认值：30。 |
| PageNumber | Integ er | 否 | 页码，大于0，且不超过Integer的最大值；默认值：1。 |

**返回参数**

| 名称 | 类型 | 描述 |
|---|---|---|
| <公共返回参数> |  | 公共返回参数，具体请参见公共返回参数。 |
| TotalRecordCount | Integer | 总记录数。 |
| PageNumber | Integer | 页码。 |
| PageRecordCount | Integer | 本页备份集个数。 |

PolarDB PostgreSQL主备版开发指云原生数据库

| Items | List<Backup> | 由Backup组成的数组。 |
|---|---|---|

#### 创建临时实例

**描述**

**说明**

基于备份集或者7天内的一个时间点创建临时实例。临时实例创建成功后，账号，数据库将继承备份集数据。 实例状态必须满足以下条件，否则将操作失败： 运行中。 没有迁移任务。 没有被锁定。 当前实例备份集的状态为完成备份。

**请求参数**

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| Action | String | 是 | 系统规定参数，取值：CreateTempDBInstance。 |
| DBInstance Id | String | 是 | 实例名称。 |
| BackupId | Integer | 否 | 备份ID。 |
| RestoreTim e | String | 否 | 7天之内并且早于当前时间半小时以上的任意时间点，默认时区为UTC。 例如：2011-06-11T16:00:00Z。 |

**返回参数**

| 名称 | 类型 | 描述 |
|---|---|---|
| <公共返回参数> |  | 公共返回参数，具体请参见公共返回参数。 |
| TempDBInstanceId | String | 临时实例ID。 |

**示例**

**请求示例**

PolarDB PostgreSQL主备版开发指云原生数据库

```
https://polardb.example.com/?Action=CreateTempDBInstance &BackupId=90262 &DBInstanceId=polardb-xxxxx
```

**返回示例**

XML格式：

```xml
<CreateTempDBInstanceResponse> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> <TempDBInstanceId>sub-xxxxx</TempDBInstanceId> </CreateTempDBInstanceResponse>
```

JSON格式：

```json
{ "RequestId":"1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC", "TempDBInstanceId":"sub-xxxxx"}
```

#### 查看备份策略

**描述**

查看系统设置的备份策略，PolarDB系统将根据用户设置的系统配置，定期做实例备份。

**请求参数**

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| Action | String | 是 | 系统规定参数，取值：DescribeBackupPolicy。 |
| DBInstanceId | String | 是 | 实例ID。 |

**返回参数**

| 名称 | 类型 | 描述 |
|---|---|---|
| <公共返回参数> |  | 公共返回参数，具体请参见公共返回参数。 |
| BackupRetentionPeri od | String | 数据备份保留天数（1~30天）。 |
| PreferredBackupTim e | String | 数据备份时间，格式：HH:mmZ- HH:mm Z。 |

PolarDB PostgreSQL主备版开发指云原生数据库

| PreferredBackupPeri od | String | 数据备份周期：Monday：周一；Tuesday：周二；Wednesday：周三；Thursday：周四；Friday：周五；Saturday：周六；Sunday：周日。 |
|---|---|---|
| BackupLog | String | 日志备份状态，Enable：开启，Disabled：关闭。 |
| LogBackupRetention Period | String | 日志备份保留天数（1~30天）。 |

#### 查询备份可恢复时间范围

调用DescribeLocalAvailableRecoveryTime接口查询备份可恢复时间范围，即实例支持按时间点恢复的最早可恢复时间点（RPO）信息。

**适用引擎**

PolarDB MySQL集群版 PolarDB PostgreSQL主备版

**请求头**

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| DBInstanc eId | Strin g | Quer y | 是 | rm-wq64n542y9j****** | 实例ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 9B7BFB11-C077- 4FE3-B051- F69CEB****** | 请求ID。 |
| Message | String | Successful | 请求返回消息。 请求成功时该参数返回Successful，请求失败时会返回请求异常信息（如错误码等）。 |
| Success | Boolean | true | 请求结果。取值： true：请求成功。 false：请求失败。 |

PolarDB PostgreSQL主备版开发指云原生数据库

| Data | Struct | {} | 返回数据。 |
|---|---|---|---|
| - RecoveryEndTi me | String | 2026-01- 26T13:01:15Z | 恢复截止时间。 |
| - RecoveryBegin Time | String | 2026-01- 21T04:30:32Z | 备份可恢复的起始时间。 |
| - DBInstanceNa me | String | rm- wq64n542y9j****** | 实例名称。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeLocalAvailableRecoveryTime &DBInstanceId=rm-wq64n542y9j******
```

正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "RequestId":"9B7BFB11-C077-4FE3-B051-F69CEB******",
 "Message":"Successful",
 "Data":{
  "RecoveryEndTime":"2026-01-26T13:01:15Z",
  "RecoveryBeginTime":"2026-01-21T04:30:32Z",
  "DBInstanceName":"rm-wq64n542y9j******"
 },
 "Success":true
}
```

`XML` 格式

```xml
<RequestId>9B7BFB11-C077-4FE3-B051-F69CEB******</RequestId> <Message>Successful</Message> <Data>
 <RecoveryEndTime>2026-01-26T13:01:15Z</RecoveryEndTime>
 <RecoveryBeginTime>2026-01-21T04:30:32Z</RecoveryBeginTime>
 <DBInstanceName>rm-wq64n542y9j******</DBInstanceName>
</Data> <Success>true</Success>
```

PolarDB PostgreSQL主备版开发指云原生数据库

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | IInvalidDBInstance Name.NotFound | IInvalidDBInstanceName.NotFo und | The specified DB instance name does not exist. |
| 400 | MissingUserID | MissingUserID | The request is missing a user id parameter. _ |
| 400 | MissingUID | MissingUID | The request is missing a uid parameter. |

#### 修改备份策略

**描述**

**请求参数**

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| Action | String | 是 | 系统规定参数，取值：ModifyBackupPolicy。 |
| DBInstanceId | String | 是 | 实例ID。 |
| PreferredBackupTim e | String | 是 | 备份时间，格式：HH:mmZ- HH:mm Z。 |
| PreferredBackupPeri od | String | 是 | 备份周期：Monday：周一；Tuesday：周二；Wednesday：周三；Thursday：周四；Friday：周五；Saturday：周六； Sunday：周日。 |
| BackupRetentionPeri od | String | 否 | 数据备份保留天数（1~30天），默认为7。 |
| BackupLog | String | 否 | 默认为Enable，可改为Disabled。 |

PolarDB PostgreSQL主备版开发指云原生数据库

| LogBackupRetention Period | String | 否 | 日志备份保留天数（1~30天，且不大于数据备份保留天数）。 当开启日志备份时，可设置日志备份文件的保留天数，目前仅支持 MySQL/ PolarDB PostgreSQL/ PolarDB PPAS引擎设置该值。 _ _ |
|---|---|---|---|

**返回参数**

| 名称 | 类型 | 描述 |
|---|---|---|
| <公共返回参数> | - | 公共返回参数，具体请参见公共返回参数。 |

**示例**

**请求示例**

```
https://polardb.example.com/?Action=ModifyBackupPolicy &DBInstanceId=polardb-xxxxx &PreferredBackupTime=00:00Z—01:00Z &PreferredBackupPeriod=Monday
```

**返回示例**

XML格式：

```xml
<ModifyBackupPolicyResponse> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> </ModifyBackupPolicyResponse>
```

JSON格式：

```json
{ "RequestId":"1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC"}
```

#### 恢复备份集到实例

**描述**

将备份集覆盖性恢复到实例。 实例状态必须满足以下条件，否则将操作失败： 运行中。 没有迁移任务。 没有被锁定。 当前实例备份集的状态为完成备份。

**请求参数**

PolarDB PostgreSQL主备版开发指云原生数据库

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| Action | String | 是 | 系统规定参数，取值： RestoreDBInstance。 |
| DBInstanceId | String | 是 | 实例ID。 |
| BackupId | Integer | 是 | 备份集ID。 |

**返回参数**

| 名称 | 类型 | 描述 |
|---|---|---|
| <公共返回参数> | - | 公共返回参数，具体请参见公共返回参数。 |

**示例**

**请求示例**

```
https://polardb.example.com/?Action=RestoreDBInstance &BackupId=103312 &DBInstanceId=polardb-xxxxx
```

**返回示例**

XML格式：

```xml
<RestoreDBInstanceResponse> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> </RestoreDBInstanceResponse>
```

JSON格式：

```json
{"RequestId":"1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC"}
```

#### 删除数据备份文件

**描述**

支持删除的备份集范围：数据备份存储时长大于日志备份保留周期且大于7天的数据备份文件，可删除，详情查看备份文件删除说明。 只删除自身的备份集，不会删除所关联实例（只读、灾备、克隆等）的备份集。 实例状态必须满足以下条件，否则将创建失败： 实例状态为运行中。

**请求参数**

PolarDB PostgreSQL主备版开发指云原生数据库

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| Action | String | 是 | 系统规定参数，取值：DeleteBackup。 |
| DBInstanc eId | String | 是 | 实例ID。 |
| BackupId | String | 是 | 备份集ID，可通过查看备份列表获取。支持传入多组值，以逗号隔开，单次最多传入100个。只支持删除查看备份列表中存储状态为Enable的备份集。 |

**返回参数**

### 插件管理

#### 卸载插件

卸载插件。

**请求头**

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Action | Strin g | Syst em | 是 | DeleteExtensions | 系统规定参数。取值： DeleteExtensions |
| AccessKeyI d | Strin g | Quer y | 否 | LTAI4G28PhwnizaSC***** *** | 账号的AccessKey ID。 |
| OwnerId | Long | Quer y | 否 | 123456**** | 系统规定参数。用户账号ID。 |
| ResourceO wnerAccou nt | Strin g | Quer y | 否 | aliyun123 | 系统规定参数。资源归属者账号ID。 |
| ResourceO wnerId | Long | Quer y | 否 | 123456**** | 资源所属用户账号ID。 |

PolarDB PostgreSQL主备版开发指云原生数据库

| ClientToke n | Strin g | Quer y | 否 | 6000170000591aed949d 0f54a343f1a4233c1e7d1 c5c****** | 用于保证请求的幂等性，防止重复提交请求。由客户端生成该参数值，保证在不同请求间唯一，大小写敏感、不超过 64个ASCII字符。 |
|---|---|---|---|---|---|
| proxyId | Strin g | Quer y | 否 | 1 | 代理模式ID。 |
| ZoneId | Strin g | Quer y | 否 | cn-hangzhou-i | 交换机所属可用区ID。 |
| ResourceG roupId | Strin g | Quer y | 否 | rg-************ | 交换机所属的资源组ID。 |
| DBInstanc eId | Strin g | Quer y | 是 | pc-**************** | 实例ID。 |
| Extensions | Strin g | Quer y | 是 | pase,hstore | 需要卸载的插件，多个插件间使用英文逗号（,）分隔。 |
| DBNames | Strin g | Quer y | 是 | auto test db _ _ | 实例数据库名。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 9B7BFB11-C077- 4FE3-B051- F69CEB****** | 请求ID。 |
| Message | String | Successful | 返回信息。 |
| Success | Boolean | true | 请求结果。取值： true：请求成功。 false：请求失败。 |

**示例**

请求示例 PolarDB PostgreSQL主备版开发指云原生数据库

```
http(s)://[Endpoint]/?Action=DeleteExtensions &Action=DeleteExtensions &DBInstanceId=pc-**************** &Extensions=pase,hstore &DBNames=auto_test_db
```

正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "RequestId":"9B7BFB11-C077-4FE3-B051-F69CEB******",
 "Message":"Successful",
 "Success":true
}
```

`XML` 格式

```xml
<RequestId>9B7BFB11-C077-4FE3-B051-F69CEB******</RequestId> <Message>Successful</Message> <Success>true</Success>
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidInnerParame ter | InvalidInnerParameter | Inner parameter is invalid. |
| 400 | InvalidDBInstanceE ngineType.Format | InvalidDBInstanceEngineType. Format | the DB instance engine type does not support this operation. |
| 400 | InvalidDBInstanceE ngineVersion.Form at | InvalidDBInstanceEngineVersio n.Format | the DB instance engine version does not support this operation. |
| 403 | IncorrectDBInstanc eState | IncorrectDBInstanceState | Current DB instance state does not support this operation. |
| 403 | IncorrectDBInstanc e | IncorrectDBInstance | Current DB instance does not support this operation. |

PolarDB PostgreSQL主备版开发指云原生数据库

| 400 | InvalidParameters. Format | InvalidParameters.Format | Specified parameters is not valid. |
|---|---|---|---|
| 400 | ExtensionNum.Not Support | ExtensionNum.NotSupport | Current extension count exceeds the maximum supported extension count. |
| 400 | InvalidDBName.For mat | InvalidDBName.Format | Specified DB name is not valid. |
| 400 | EventTriggerExistIn CurDB | EventTriggerExistInCurDB | Event trigger exists in current DB. |
| 404 | InvalidAccountNam e.NotFound | InvalidAccountName.NotFound | Specified account name does not exist. |
| 403 | UnsupportDBOwne rForExtensionOps | UnsupportDBOwnerForExtensi onOps | DBOwner does not support specified extensions. |
| 400 | Extension.NotInstal l | Extension.NotInstall | extensions not installed |
| 400 | Extension.Depende ncy | Extension.Dependency | required extension list existed, but had missing extensions |
| 400 | -2001 | Extension.Dependency.Invalid | required extension list existed, but had missing extensions: %s |

#### 更新插件

更新已安装插件。

**请求头**

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Action | Strin g | Syst em | 是 | UpdateExtensions | 系统规定参数。取值： UpdateExtensions |
| AccessKeyI d | Strin g | Quer y | 否 | LTAI4G28PhwnizaSC***** *** | 账号的AccessKey ID。 |

PolarDB PostgreSQL主备版开发指云原生数据库

| OwnerId | Long | Quer y | 否 | 123456**** | 系统规定参数。用户账号ID。 |
|---|---|---|---|---|---|
| ResourceO wnerAccou nt | Strin g | Quer y | 否 | aliyun123 | 系统规定参数。资源归属者账号ID。 |
| ResourceO wnerId | Long | Quer y | 否 | 123456**** | 资源所属用户账号ID。 |
| ClientToke n | Strin g | Quer y | 否 | 6000170000591aed949d 0f54a343f1a4233c1e7d1 c5c****** | 用于保证请求的幂等性，防止重复提交请求。由客户端生成该参数值，保证在不同请求间唯一，大小写敏感、不超过 64个ASCII字符。 |
| proxyId | Strin g | Quer y | 否 | 1 | 代理模式ID。 |
| ZoneId | Strin g | Quer y | 否 | cn-hangzhou-i | 交换机所属可用区ID。 |
| ResourceG roupId | Strin g | Quer y | 否 | rg-********** | 交换机所属的资源组ID。 |
| DBInstanc eId | Strin g | Quer y | 是 | pc-**************** | 实例ID。 |
| Extensions | Strin g | Quer y | 是 | postgres fdw _ | 需要更新的插件，多个插件间使用英文逗号（,）分隔。 |
| DBNames | Strin g | Quer y | 是 | auto test db _ _ | 实例数据库名。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 9B7BFB11-C077- 4FE3-B051- F69CEB****** | 请求ID。 |
| Message | String | Successful | 返回信息。 |

PolarDB PostgreSQL主备版开发指云原生数据库

| Success | Boolean | true | 请求结果。取值： true：请求成功 false：请求失败 |
|---|---|---|---|

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=UpdateExtensions &Action=UpdateExtensions &DBInstanceId=pc-**************** &Extensions=postgres_fdw &DBNames=auto_test_db
```

正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "RequestId":"9B7BFB11-C077-4FE3-B051-F69CEB******",
 "Message":"Successful",
 "Success":true
}
```

`XML` 格式

```xml
<RequestId>9B7BFB11-C077-4FE3-B051-F69CEB******</RequestId> <Message>Successful</Message> <Success>true</Success>
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidInnerParame ter | InvalidInnerParameter | Inner parameter is invalid. |
| 400 | InvalidDBInstanceE ngineType.Format | InvalidDBInstanceEngineType. Format | the DB instance engine type does not support this operation. |
| 400 | InvalidDBInstanceE ngineVersion.Form at | InvalidDBInstanceEngineVersio n.Format | the DB instance engine version does not support this operation. |

PolarDB PostgreSQL主备版开发指云原生数据库

| 403 | IncorrectDBInstanc eState | IncorrectDBInstanceState | Current DB instance state does not support this operation. |
|---|---|---|---|
| 403 | IncorrectDBInstanc e | IncorrectDBInstance | Current DB instance does not support this operation. |
| 400 | InvalidParameters. Format | InvalidParameters.Format | Specified parameters is not valid. |
| 400 | ExtensionNum.Not Support | ExtensionNum.NotSupport | Current extension count exceeds the maximum supported extension count. |
| 400 | InvalidDBName.For mat | InvalidDBName.Format | Specified DB name is not valid. |
| 404 | InvalidDBName.Not Found | InvalidDBName.NotFound | Specified one or more DB name does not exist or DB status does not support. |
| 400 | EventTriggerExistIn CurDB | EventTriggerExistInCurDB | Event trigger exists in current DB. |
| 403 | UnsupportDBOwne rForExtensionOps | UnsupportDBOwnerForExtensi onOps | DBOwner does not support specified extensions. |
| 404 | InvalidDBName.Not Found | InvalidDBName.NotFound | Specified one or more DB name does not exist or DB status does not support. |
| 400 | Extension.NotInstal l | Extension.NotInstall | extensions not installed |
| 403 | CurMinorVersionUn supportUpdateGive nExtension | CurMinorVersionUnsupportUpd ateGivenExtension | Current minor version does not support update given extension. |
| 400 | Extension.Depende ncy | Extension.Dependency | Database not found. |

#### 查询插件详情

查询已安装的插件。

**请求头**

PolarDB PostgreSQL主备版开发指云原生数据库

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Action | Strin g | Syst em | 是 | DescribeExtensions | 系统规定参数。取值： DescribeExtensions |
| AccessKeyI d | Strin g | Quer y | 否 | LTAI4G28PhwnizaSC***** *** | 访问密钥ID。 |
| OwnerId | Long | Quer y | 否 | 123456**** | 系统规定参数。用户账号ID。 |
| ResourceO wnerAccou nt | Strin g | Quer y | 否 | aliyun123 | 系统规定参数。资源归属者账号ID。 |
| ResourceO wnerId | Long | Quer y | 否 | 123456**** | 资源所属用户账号ID。 |
| ClientToke n | Strin g | Quer y | 否 | 6000170000591aed949d 0f54a343f1a4233c1e7d1 c5c****** | 用于保证请求的幂等性，防止重复提交请求。由客户端生成该参数值，保证在不同请求间唯一，大小写敏感、不超过 64个ASCII字符。 |
| proxyId | Strin g | Quer y | 否 | 1 | 代理模式ID。 |
| ZoneId | Strin g | Quer y | 否 | cn-hangzhou-i | 交换机所属可用区ID。 |
| ResourceG roupId | Strin g | Quer y | 否 | rg-************ | 交换机所属的资源组ID。 |
| DBInstanc eId | Strin g | Quer y | 是 | pc-**************** | 实例ID。 |
| Extension Name | Strin g | Quer y | 否 | address standardizer _ | 插件名称。 |
| DBName | Strin g | Quer y | 是 | testdb | 数据库名称。 |

PolarDB PostgreSQL主备版开发指云原生数据库

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 9B7BFB11-C077- 4FE3-B051- F69CEB****** | 请求ID。 |
| Message | String | success | 返回信息。 |
| Success | Boolean | true | 请求结果。取值： true：请求成功。 false：请求失败。 |
| Data | Struct | list | 插件列表。 |
| - UninstalledExt ensions | Array | 指定数据库下未安装插件信息。 | 指定数据库下未安装插件信息。 |
| --Name | String | jueming | 插件名称。 |
| -- DefaultVersion | String | 7.7 | 插件默认版本。 |
| --Comment | String | test | 插件用途。 |
| --Owner | String | admin | 插件所属用户。 |
| --Priority | String | 1 | 插件优先级。 |
| --Requires | String | ganos networking _ | 此插件安装时所依赖的插件。 |
| --Category | String | geography space, _ self develop _ | 插件类型。 |
| --Restart | String | true | 是否重启应用。取值： true：重启 false：不重启 |

PolarDB PostgreSQL主备版开发指云原生数据库

| - InstalledExten sions | Array | 指定数据库下已安装插件信息。 | 指定数据库下已安装插件信息。 |
|---|---|---|---|
| --Name | String | jueming | 插件名称。 |
| -- DefaultVersion | String | 7.7 | 插件默认版本。 |
| -- InstalledVersio n | String | 7.7 | 插件当前安装的版本。 |
| --Comment | String | test | 备注信息。 |
| --Owner | String | 9527952**** | 插件所属用户。 |
| --Priority | String | 1 | 插件优先级。 |
| --Requires | String | ganos networking _ | 此插件安装时所依赖的插件。 |
| --Category | String | geography space, _ self develop _ | 插件类型。 |
| --Restart | String | true | 是否重启应用。取值： true：重启 false：不重启 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeExtensions &Action=DescribeExtensions &DBInstanceId=pc-**************** &DBName=testdb
```

正常返回示例 `JSON` 格式 PolarDB PostgreSQL主备版开发指云原生数据库

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "RequestId":"9B7BFB11-C077-4FE3-B051-F69CEB******",
 "Message":"success",
 "Data":{
  "UninstalledExtensions":[
   {
    "Comment":"test",
    "Owner":"admin",
    "Category":"geography_space, self_develop",
    "Requires":"ganos_networking",
    "Priority":"1",
    "DefaultVersion":"7.7",
    "Restart":"true",
    "Name":"jueming"
   }
```

`],`

```json
  "InstalledExtensions":[
   {
    "Comment":"test",
    "Owner":"9527952****",
    "Category":"geography_space, self_develop",
    "InstalledVersion":"7.7",
    "Requires":"ganos_networking",
    "Priority":"1",
    "DefaultVersion":"7.7",
    "Restart":"true",
    "Name":"jueming"
   }
```

]

```json
 },
 "Success":true
}
```

`XML` 格式 PolarDB PostgreSQL主备版开发指云原生数据库

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

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidInnerParame ter | InvalidInnerParameter | Inner parameter is invalid. |
| 400 | InvalidDBInstanceE ngineType.Format | InvalidDBInstanceEngineType. Format | the DB instance engine type does not support this operation. |
| 400 | InvalidDBInstanceE ngineVersion.Form at | InvalidDBInstanceEngineVersio n.Format | the DB instance engine version does not support this operation. |
| 403 | IncorrectDBInstanc eState | IncorrectDBInstanceState | Current DB instance state does not support this operation. |
| 403 | IncorrectDBInstanc e | IncorrectDBInstance | Current DB instance does not support this operation. |

PolarDB PostgreSQL主备版开发指云原生数据库

| 400 | InvalidParameters. Format | InvalidParameters.Format | Specified parameters is not valid. |
|---|---|---|---|
| 404 | InvalidAccountNam e.NotFound | InvalidAccountName.NotFound | Specified account name does not exist. |
| 403 | IncorrectAccountLo ckState | IncorrectAccountLockState | accountName is in a locked state. |
| 400 | InvalidDBName.For mat | InvalidDBName.Format | Specified DB name is not valid. |
| 400 | Extension.Depende ncy | Extension.Dependency | Database not found. |
| 404 | InternalError.Exten sionConfigNotFoun d | InternalError.ExtensionConfigN otFound | Extension config not found. |
| 400 | InternalError.Exten sionConfigEmpty | InternalError.ExtensionConfigE mpty | Extension config is empty. |

#### 安装插件

安装插件。

**请求头**

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Action | Strin g | Syst em | 是 | CreateExtensions | 系统规定参数。取值： CreateExtensions |
| AccessKeyI d | Strin g | Quer y | 否 | LTAI4G28PhwnizaSC***** *** | 账号的AccessKey ID。 |
| OwnerId | Long | Quer y | 否 | 123456**** | 系统规定参数。用户账号ID。 |
| ResourceO wnerAccou nt | Strin g | Quer y | 否 | aliyun123 | 系统规定参数。资源归属者账号ID。 |

PolarDB PostgreSQL主备版开发指云原生数据库

| ResourceO wnerId | Long | Quer y | 否 | 123456**** | 资源所属用户账号ID。 |
|---|---|---|---|---|---|
| ClientToke n | Strin g | Quer y | 否 | 6000170000591aed949d 0f54a343f1a4233c1e7d1 c5c****** | 用于保证请求的幂等性，防止重复提交请求。由客户端生成该参数值，保证在不同请求间唯一，大小写敏感、不超过 64个ASCII字符。 |
| proxyId | Strin g | Quer y | 否 | 1 | 代理模式ID。 |
| ZoneId | Strin g | Quer y | 否 | cn-hangzhou-i | 交换机所属可用区ID。 |
| ResourceG roupId | Strin g | Quer y | 否 | rg-************ | 交换机所属的资源组ID。 |
| DBInstanc eId | Strin g | Quer y | 是 | pc-**************** | 集群ID。 |
| Extensions | Strin g | Quer y | 否 | address standardizer _ | 插件名称，多个插件间使用英文逗号（,）分隔。 |
| DBNames | Strin g | Quer y | 是 | testdb01 | 待安装插件的数据库名。 |
| SourceDB Name | Strin g | Quer y | 否 | testdb1 | 无效参数。 |
| AccountNa me | Strin g | Quer y | 是 | test acc _ | 账号名。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 9B7BFB11-C077- 4FE3-B051- F69CEB****** | 请求ID。 |
| Message | String | Successful | 返回信息。 |

PolarDB PostgreSQL主备版开发指云原生数据库

| Success | Boolean | true | 请求结果。取值： true：请求成功。 false：请求失败。 |
|---|---|---|---|

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=CreateExtensions &Action=CreateExtensions &DBInstanceId=pc-**************** &DBNames=testdb01 &AccountName=test_acc
```

正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "RequestId":"9B7BFB11-C077-4FE3-B051-F69CEB******",
 "Message":"Successful",
 "Success":true
}
```

`XML` 格式

```xml
<RequestId>9B7BFB11-C077-4FE3-B051-F69CEB******</RequestId> <Message>Successful</Message> <Success>true</Success>
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidInnerParame ter | InvalidInnerParameter | Inner parameter is invalid. |
| 400 | InvalidDBInstanceE ngineType.Format | InvalidDBInstanceEngineType. Format | the DB instance engine type does not support this operation. |
| 400 | InvalidDBInstanceE ngineVersion.Form at | InvalidDBInstanceEngineVersio n.Format | the DB instance engine version does not support this operation. |

PolarDB PostgreSQL主备版开发指云原生数据库

| 403 | IncorrectDBInstanc eState | IncorrectDBInstanceState | Current DB instance state does not support this operation. |
|---|---|---|---|
| 403 | IncorrectDBInstanc e | IncorrectDBInstance | Current DB instance does not support this operation. |
| 400 | InvalidParameters. Format | InvalidParameters.Format | Specified parameters is not valid. |
| 404 | InvalidAccountNam e.NotFound | InvalidAccountName.NotFound | Specified account name does not exist. |
| 403 | IncorrectAccountPri vilegeType | IncorrectAccountPrivilegeType | Current account privilege type does not support this operation. |
| 403 | IncorrectAccountLo ckState | IncorrectAccountLockState | accountName is in a locked state. |
| 400 | InvalidSourceDb | InvalidSourceDb | Specified SourceDb is not valid. |
| 400 | InvalidDBName.For mat | InvalidDBName.Format | Specified DB name is not valid. |
| 400 | EventTriggerExistIn CurDB | EventTriggerExistInCurDB | Event trigger exists in current DB. |
| 400 | ExtensionNum.Not Support | ExtensionNum.NotSupport | Current extension count exceeds the maximum supported extension count. |
| 400 | Extension.Depende ncy | Extension.Dependency | Database not found. |
| 404 | InvalidDBName.Not Found | InvalidDBName.NotFound | Specified one or more DB name does not exist or DB status does not support. |
| 403 | UnsupportDBOwne rForExtensionOps | UnsupportDBOwnerForExtensi onOps | DBOwner does not support specified extensions. |
| 403 | CurMinorVersionPG 17UnsupportVector | CurMinorVersionPG17Unsuppo rtVector | Current minor version of pg17 does not support vector. |

PolarDB PostgreSQL主备版开发指云原生数据库

| 403 | CurrentMinorVersio nUnsupportSpecifie dExtensions | CurrentMinorVersionUnsupport SpecifiedExtensions | Current minor version does not support specified extensions. |
|---|---|---|---|
| 403 | PolarCsiExtensionN eedLogicalWalLeve l | PolarCsiExtensionNeedLogical WalLevel | Polar Csi Extension Need Logical Wal Level |
| 404 | InternalError.Exten sionConfigNotFoun d | InternalError.ExtensionConfigN otFound | Extension config not found. |
| 400 | InternalError.Exten sionConfigEmpty | InternalError.ExtensionConfigE mpty | Extension config is empty. |
| 400 | AccountNameOwne rNotDBOwner | AccountNameOwnerNotDBOw ner | The account name is not the owner of DB. |

### 监控管理

#### 查看实例资源使用情况

**描述**

查看实例的资源利用信息。返回用户的某个实例的已用空间大小。 通过DBInstanceId来获取实例资源使用情况。

**请求参数**

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| Action | String | 是 | 系统规定参数，取值： DescribeResourceUsage。 |
| DBInstanceId | String | 是 | 实例ID。 |

**返回参数**

| 名称 | 类型 | 描述 |
|---|---|---|
| <公共返回参数> |  | 公共返回参数，具体请参见公共返回参数。 |
| DBInstanceId | String | 实例ID。 |
| Engine | String | 数据库类型。 |
| DiskUsed | Integer | 已用空间（DataSize+LogSize），单位：Byte，-1表示没有数据。 |
| DataSize | Integer | 数据文件占用空间，单位：Byte，-1表示没有数据。 |

PolarDB PostgreSQL主备版开发指云原生数据库

| LogSize | Integer | 日志占用空间，单位：Byte，-1表示没有数据。 |
|---|---|---|
| BackupSize | Integer | 备份占用空间，单位：Byte，-1表示没有数据。 |
| ColdBackupSize | Integer | 冷备的存储量，单位：Byte，-1表示没有数据。 |
| SQLSize | Integer | SQL的存储量，单位：Byte，-1表示没有数据。 |

#### 查看实例性能数据

**描述**

根据性能参数查看某个用户实例，某时间段范围内的性能监控数据。 根据查询时间范围的不同，有如下3种输出形式： 当查询时间范围小于等于1天，按分钟描点性能值。 当查询时间范围1天到7天不支持，暂不支持。 当查询时间范围大于7天小于等于15天，按小时描点性能值。 当查询时间范围大于15天小于30天，暂不支持。 当查询时间范围大于等于30天小于等于1年时，按天描点。

**说明**

实例空间占用Key为MySQL_SpaceUsage，仅支持查询1天内的监控数据，即第1种输出形式。

**请求参数**

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| Action | String | 是 | 系统规定参数，取值：DescribeDBInstancePerformance。 |
| DBInstan ceId | String | 是 | 实例ID。 |
| Key | Intege r | 是 | 性能指标，多个使用半角逗号（,）。 |
| StartTime | String | 是 | 查询开始时间，格式如：2012-06-11T15:00Z。 |
| EndTime | String | 是 | 查询结束时间，格式如：2012-06-11T15:00Z。 |

**返回参数**

| 名称 | 类型 | 描述 |
|---|---|---|

PolarDB PostgreSQL主备版开发指云原生数据库

| <公共返回参数> | - | 公共返回参数。 |  |  |
|---|---|---|---|---|
| DBInstanceId | String | 实例ID。 |  |  |
| Engine | String | 数据库类型。 |  |  |
| StartTime | String | 查询开始时间，格式： YYYY-MM-DD'T'HH:mmZ ，如 2025- 05-30T03:29Z 。 |  |  |
|  |  |  | 2025- |  |
| EndTime | String | 查询结束时间，格式： YYYY-MM-DD'T'HH:mmZ ，如 2025- 05-30T04:29Z ，大于查询开始时间。 |  |  |
|  |  |  | 2025- |  |
| PerformanceKey s | List<PerformanceKe y> | 数组格式： {perf1, perf2, perf3, …} 。 |  |  |

|  | 05-30T03:29Z |
|---|---|

|  | 05-30T04:29Z |
|---|---|

**示例**

**请求示例**

```
https://polardb.example.com/?Action=DescribeDBInstancePerformance &DBInstanceId=polardb-xxxxx &key= PolarDB_PG_xxxxx &StartTime=2025-05-30T03:29Z &EndTime=2025-05-30T04:29Z
```

**返回示例**

XML格式：

```xml
<DescribeDBInstancePerformanceResponse> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> <DBInstanceID>polardb-xxxxx</DBInstanceID> <StartTime>2025-05-30T03:29Z</StartTime> <EndTime>2025-05-30T04:29Z</EndTime> <Engine>PolarDB_PG</Engine> <PerformanceKeys> <PerformanceKey> <Key>MySQL_xxxxx</Key> <Unit>KB</Unit> <ValueFormat>recv_k&amp;sent_k</ValueFormat> <Values><Values/> </PerformanceKey> </PerformanceKeys> </DescribeDBInstancePerformanceResponse>
```

JSON格式： PolarDB PostgreSQL主备版开发指云原生数据库

```json
{ “RequestId”1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC, "DBInstanceID": polardb-xxxxx, "StartTime": "2025-05-30T03:29Z", "EndTime": "2025-05-30T04:29Z", "Engine": "PolarDB_PG", "PerformanceKeys":
    { PerformanceKey[ {
        "Key": "PolarDB_PG_xxxxx",
        "Unit": "KB",
        "ValueFormat": "recv_k&sent_k",
        "Values": { "PerformanceValue":[] } } ] }}
```

#### 查询监控行为

**描述**

描述监控的行为。

**请求参数**

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| Action | String | 是 | 系统规定参数，取值：DescribeDBInstanceMonitor。 |
| DBInstance Id | String | 是 | 实例ID。 |

**返回参数**

| 名称 | 类型 | 描述 |
|---|---|---|
| <公共返回参数> | - | 公共返回参数，具体请参见公共返回参数。 |
| Period | String | 监控的采集间隔，单位为秒。 |

#### 修改监控行为

**描述**

修改监控的行为。

**请求参数**

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| Action | String | 是 | 系统规定参数，取值：ModifyDBInstanceMonitor。 |
| DBInstanceId | String | 是 | 实例ID。 |
| Period | String | 是 | 监控的采集间隔，60或300（默认为300秒）。 |

**返回参数**

PolarDB PostgreSQL主备版开发指云原生数据库

| 名称 | 类型 | 描述 |
|---|---|---|
| <公共返回参数> | - | 公共返回参数，具体请参见公共返回参数。 |

### 参数管理

#### 查看数据库参数模板

**描述**

该接口返回参数模板列表，包含内容：参数名，参数默认值，是否可修改，是否需要重启才能生效，参数校验规则（正则表达式）。

**请求参数**

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| Action | Strin g | 是 | 系统规定参数，取值：DescribeParameterTemplates。 |
| Engine | Strin g | 是 | 数据库类型，取值：PolarDB PG。 _ |
| EngineVer sion | Strin g | 是 | 数据库版本，取值： 14 16 |

**返回参数**

| 名称 |  | 类型 | 描述 |  |  |
|---|---|---|---|---|---|
| <公共返回参数> |  | - | 公共返回参数。 |  |  |
| Engine |  | String | 数据库类型。 |  |  |
| EngineVersion |  | String | 数据库版本号。 |  |  |
| ParameterCount |  | Integer | 参数个数。 |  |  |
| Parameters |  | List<TemplateRecord | 参数列表，格式： {parameter1, parameter2, parameter3, …} 。 |  |  |
|  |  |  |  | {parameter1, parameter2, |  |
|  |  | > | parameter3, …} |  |  |

PolarDB PostgreSQL主备版开发指云原生数据库

**示例**

**请求示例**

```
https://polardb.example.com/?Action=DescribeParameterTemplates &Engine=PolarDB_PG &EngineVersion=16
```

**返回示例**

XML格式：

```xml
<DescribeParameterTemplatesResponse> <Engine>PolarDB_PG</Engine> <EngineVersion>16</EngineVersion> <ParameterCount>1</ParameterCount> <Parameters> <TemplateRecord> <CheckingCode>[0-100]</CheckingCode> <ForceRestart>True</ForceRestart> <Factor>1</Factor> <ParameterDescription>test</ParameterDescription> <ParameterName>fill factor</ParameterName> <ParameterValue>0</ParameterValue> <ForceModify>True</ForceModify> <Unit>INT</Unit> </TemplateRecord> </Parameters> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> </DescribeParameterTemplatesResponse>
```

JSON格式：

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

#### 查看当前实例数据库参数运行列表

**描述**

该接口返回用户某个实例当前的参数配置。 PolarDB PostgreSQL主备版开发指云原生数据库

**请求参数**

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| Action | String | 是 | 系统规定参数，取值：DescribeParameters。 |
| DBInstanceId | String | 是 | 实例ID。 |

**返回参数**

| 名称 | 类型 |  | 描述 |  |  |
|---|---|---|---|---|---|
| <公共返回参数> | - |  | 公共返回参数。 |  |  |
| Engine | String |  | 数据库类型。 |  |  |
| EngineVersion | String |  | 数据库版本号。 |  |  |
| RunningParameters | List<DBInstanceParameter> |  | 当前运行的参数列表，格式为 {parameter1,parameter2,pa rameter3, …} 。 |  |  |
|  |  |  |  | {parameter1,parameter2,pa |  |
|  |  |  | rameter3, …} |  |  |
| ConfigParameters | List<DBInstanceParameter> |  | 正在同步的参数列表，格式为 {parameter1,parameter2,pa rameter3,…} 。 |  |  |

|  |  | {parameter1,parameter2,pa |  |
|---|---|---|---|
|  | rameter3,…} |  |  |

表 1. DBInstanceParameter参数

| 名称 | 类型 | 描述 |
|---|---|---|
| ParameterName | String | 参数名。 |
| ParameterValue | String | 参数值。 |
| ParameterDescription | String | 参数描述。 |

**示例**

**请求示例**

```
https://polardb.example.com/?Action=DescribeParameters &DBInstanceId=polardb-xxxxx
```

PolarDB PostgreSQL主备版开发指云原生数据库

**返回示例**

XML格式：

```xml
<DescribeParametersResponse> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> <Engine>PolarDB_PG</Engine > <EngineVersion>16</EngineVersion> <RunningParameters> <DBInstanceParameter> <ParameterDescription>test</ParameterDescription> <ParameterName>fill factor</ParameterName> <ParameterValue>0</ParameterValue> </DBInstanceParameter> </RunningParameters> <ConfigParameters> <DBInstanceParameter> <ParameterDescription>test1</ParameterDescription> <ParameterName>fill factor</ParameterName> <ParameterValue>50</ParameterValue> </DBInstanceParameter> </ConfigParameters> </DescribeParametersResponse>
```

JSON格式：

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

#### 修改数据库参数列表

**描述**

用户可以修改实例参数，提交请求后，PolarDB将下达任务，新修改的参数应用到实例。如果所提交的参数中，有需要重启数据库的，PolarDB将重启数据库。 必须满足以下条件，否则调用失败： 当前实例状态：使用中。 当前实例锁定模式：正常。 参数值有如下3类： [1-65535]，表示数字范围，通过正则识别，从而提取出最小值和最大值。然后根据最小值和最大值对输入参数进行验证，另外，还需要是整除因子的倍数。 PolarDB PostgreSQL主备版开发指云原生数据库 [utf8|gbk|latin1]，表示固定的取值规则，通过正则识别，从而提取出固定的取值。然后根据这些固定的取值对输入参数进行验证。 其他，这种情况符合正则表达式。 下达任务之前，PolarDB将会进行参数检查，步骤如下：
1. 检查参数是否存在。
2. 检查参数是否可修改。
3. 检查参数是否合法。
若参数非法，PolarDB返回400错误，并返回非法的参数信息，如下所示：

```json
{"HttpStatusCode":400, "Code":"InvalidParameter.Format", "Message":"Specified parameter is not valid. [auto_increment_increment:a,character_set_client:41]"}
```

**请求参数**

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| Action | String | 是 | 系统规定参数，取值：ModifyParameter。 |
| DBInstanceI d | String | 是 | 实例ID。 |
| Parameters | String | 是 | 参数及其值的JSON串， 参数的值都是字符串类型， {"auto increment increment":"1", _ _ "character set client":"utf8"}。 _ _ |
| Forcerestart | String | 否 | true：强制重启（若修改的参数当中，有需要重启的参数，则必须传入true，否则修改将不生效）；false：不强制重启。默认不强制重启。 |

**返回参数**

| 名称 | 类型 | 描述 |
|---|---|---|
| <公共返回参数> | - | 公共返回参数，具体请参见公共返回参数。 |

**示例**

**请求示例**

PolarDB PostgreSQL主备版开发指云原生数据库

```
https://polardb.example.com/?Action=ModifyeParameter &DBInstanceId=polardb-xxxxx &Parameters={"key_buffer_size":"456","character_set_client":"gbk"}
```

**返回示例**

XML格式：

```xml
<ModifyeParameterResponse> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> </ModifyeParameterResponse>
```

JSON格式：

```json
{ "RequestId":"1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC",}
```

### 日志管理

#### 查看慢日志列表

**描述**

用户可以查询某日期范围内、某个用户实例下、某个DB的慢查询汇总情况，支持分页查询。

**请求参数**

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| Action | String | 是 | 系统规定参数，取值：DescribeSlowLogs。 |
| DBInstan ceId | String | 是 | 实例ID。 |
| StartTime | String | 是 | 查询开始日期，格式：YYYY-MM-DDZ，如2011-05-30Z。 |
| EndTime | String | 是 | 查询结束日期，不能小于查询开始日期。 格式：YYYY-MM-DDZ，如2011-05-30Z。 |
| DBName | String | 否 | 数据库名称。 |
| SortKey | String | 否 | 排序依据，取值： TotalExecutionCounts：总执行次数最多。 TotalQueryTimes：总执行时间最多。 TotalLogicalReads：总逻辑读最多。 |

PolarDB PostgreSQL主备版开发指云原生数据库

| PageSize | Integer | 否 | 每页记录数，取值：30/50/100，默认值：30。 |
|---|---|---|---|
| PageNum ber | Integer | 否 | 页码大于0，且不超过Integer的最大值；默认值：1。 |

**返回参数**

| 名称 | 类型 | 描述 |
|---|---|---|
| <公共返回参数> |  | 公共返回参数。 |
| Engine | String | 数据库类型。 |
| StartTime | String | 查询开始日期，格式：YYYY-MM-DDZ，如2025-05-30Z。 |
| EndTime | String | 查询结束日期，格式：YYYY-MM-DDZ，如2025-06-30Z。 |
| TotalRecordCou nt | Integer | 总记录数。 |
| PageNumber | Integer | 页码。 |
| PageRecordCou nt | Integer | 本页SQL语句个数。 |
| Items | List<SQLSlow Log> | 慢日志语句列表。 |

**示例**

**请求示例**

```
https://polardb.example.com/?Action=DescribeSlowLogs &DBInstanceId=polardb-xxxxx &StartTime=2025-05-30Z &EndTime=2025-06-30Z &SortKey= Totaxxxxx
```

**返回示例**

XML格式： PolarDB PostgreSQL主备版开发指云原生数据库

```xml
<DescribeSlowLogsResponse> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> <DBInstanceID>polardb-xxxxx</DBInstanceID> <Engine>PolarDB_PG</Engine> <StartTime>2025-05-30Z</StartTime> <EndTime>2025-06-30Z</EndTime> <TotalRecordCount>1</TotalRecordCount> <PageNumber>1</PageNumber> <PageRecordCount>1</PageRecordCount> <Items> <SQLSlowLog> <SQLText>update test.zxb set id=0 limit 1</SQLText> <MySQLTotalExecutionCounts>178</MySQLTotalExecutionCounts> <MySQLTotalExecutionTimes>189</MySQLTotalExecutionTimes> <TotalLogicalReadcounts>89</TotalLogicalReadcounts> <TotalPhysicalReadcounts>90</TotalPhysicalReadcounts> <ReportTime>2025-06-30Z</ReportTime> </SQLSlowLog> </Items> </DescribeSlowLogsResponse>
```

JSON格式：

```json
{ "RequestId":"1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC", "StartTime":"2025-05-30Z ", "EndTime":"2025-06-30Z ", "Engine":"PolarDB_PG", "PageNumber":1, "PageRecordCount":1, "TotalRecordCount"：1, "Items":{
    "SQLSlowLog":[{
        "SQLText":”update test.zxb set id=0 limit 1”,
        "MySQLTotalExecutionCounts":178,
        "MySQLTotalExecutionTimes":189,
        "TotalLogicalReadcounts":89,
        "TotalPhysicalReadcounts":90,
        "ReportTime":"2025-06-30Z" }]}}
```

#### 查看慢日志明细

**描述**

用户可以查询某日期范围内、某个用户实例下、某个DB的慢查询明细。

**请求参数**

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| Action | String | 是 | 系统规定参数，取值：DescribeSlowLogRecords。 |

PolarDB PostgreSQL主备版开发指云原生数据库

| DBInstan ceId | String | 是 | 实例ID。 |
|---|---|---|---|
| StartTime | String | 是 | 查询开始日期，格式：YYYY-MM-DD’T’HH:mmZ，如2011-06- 11T15:00Z。 |
| EndTime | String | 是 | 查询结束日期，不能小于查询开始日期，格式：YYYY-MM- DD’T’HH:mmZ，如2011-06-11T16:00Z。 |
| DBName | String | 否 | 数据库名称。 |
| PageSize | Integer | 否 | 每页记录数，取值：30/50/100，默认值：30。 |
| PageNum ber | Integer | 否 | 页码大于0，且不超过Integer的最大值；默认值：1。 |

**返回参数**

| 名称 | 类型 | 描述 |
|---|---|---|
| <公共返回参数> |  | 公共返回参数。 |
| Engine | String | 数据库类型。 |
| TotalRecordCount | Integer | 总记录数。 |
| PageNumber | Integer | 页码。 |
| PageRecordCount | Integer | 本页SQL语句个数。 |
| Items | List<SQLSlowRecord> | - |

SQLSlowLog参数

| 名称 | 类型 | 描述 |
|---|---|---|
| HostAddress | Strin g | 用户连接数据库的主机地址。 |
| DBName | Strin g | 数据库名称。 |

PolarDB PostgreSQL主备版开发指云原生数据库

| SQLText |  | Strin g | 查询语句。 |  |  |
|---|---|---|---|---|---|
| QueryTimes |  | Long | 执行时长，单位：秒。 |  |  |
| LockTimes |  | Long | 锁定时长，单位：秒。 |  |  |
| ParseRowCounts |  | Long | 解析行数。 |  |  |
| ReturnRowCount s |  | Long | 返回行数。 |  |  |
| ExecutionStartTi me |  | Strin | 执行开始时间；格式： YYYY-MM-DD THH:mm:ss Z ，如 2025-06-11 T15:00:08Z 。 |  |  |
|  |  |  |  | 2025-06-11 |  |
|  |  | g | T15:00:08Z |  |  |

**示例**

**请求示例**

```
https://polardb.example.com/?Action=DescribeSlowLogRecords &DBInstanceId=rm-xxxxx &StartTime=2025-06-11 T15:00:08Z &EndTime=2025-06-11 T16:00:08Z
```

**返回示例**

XML格式：

```xml
<DescribeSlowLogRecordsResponse> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> <DBInstanceID>rm-xxxxx</DBInstanceID> <Engine>PolarDB_PG</Engine> <TotalRecordCount>1</TotalRecordCount> <PageNumber>1</PageNumber> <PageRecordCount>1</PageRecordCount> <Items> <SQLSlowRecord> <HostAddress>192.168.0.123</HostAddress> <DBName>test</DBName> <SQLText>update test.zxb set id=0 limit 1</SQLText> <QueryTimes>123</QueryTimes> <LockTimes>12</LockTimes> <ParseRowCounts>125</ParseRowCounts> <ReturnRowCounts>1</ReturnRowCounts> <ExecutionStartTime>2025-06-11T15:00:08Z</ExecutionStartTime> </SQLSlowRecord> </Items> </DescribeSlowLogRecordsResponse>
```

PolarDB PostgreSQL主备版开发指云原生数据库 JSON格式：

```json
{ "RequestId":"1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC", "Engine":"PolarDB_PG", "PageNumber":1, "PageRecordCount":1, "TotalRecordCount":1, "Items":{
 "SQLSlowRecord":[{
  HostAddress:”192.168.0.123”,
  DBName:”test”,
  SQLText:”update test.zxb set id=0 limit 1”,
  QueryTimes:”123”,
  LockTimes:”12”,
  ParseRowCounts:”125”,
  ReturnRowCounts:”1”,
  ExecutionStartTime:”2025-06-11T15:00:08Z”}]}}
```

#### 查看错误日志

**描述**

查看实例某段时间内的错误日志。

**请求参数**

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| Action | Stri ng | 是 | 系统规定参数，取值：DescribeErrorLogs。 |
| DBInstanc eId | Stri ng | 是 | 实例ID。 |
| StartTime | Stri ng | 是 | 查询开始时间，格式：YYYY-MM-DD’T’HH:mmZ，如2011-05-30T12:10Z。 |
| EndTime | Stri ng | 是 | 查询结束时间，必须大于查询开始时间格式：YYYY-MM-DD’T’HH:mmZ，如 2011-05-30T20:10Z。 |
| PageSize | Inte ger | 否 | 每页记录数，取值：30/50/100，默认值：30。 |
| PageNum ber | Inte ger | 否 | 页码大于0，且不超过Integer的最大值；默认值：1。 |

**返回参数**

PolarDB PostgreSQL主备版开发指云原生数据库

| 名称 | 类型 | 描述 |
|---|---|---|
| <公共返回参数> |  | 公共返回参数，具体请参见公共返回参数。 |
| TotalRecordCount | Integer | 总记录数。 |
| PageNumber | Integer | 页码。 |
| PageRecordCount | Integer | 本页错误日志个数。 |
| Items | List<ErrorLogs> | - |

ErrorLogs参数

| 名称 | 类型 | 描述 |
|---|---|---|
| ErrorInfo | String | 错误日志信息。 |
| CreateTime | String | 生成时间，格式：YYYY-MM-DD’T’HH:mm:ssZ，如2011-05-30 T12:11:4Z。 |

**示例**

**请求示例**

```
https://polardb.example.com/?Action=DescribeErrorLogs &DBInstanceId=polardb-xxxxx &StartTime=2011-06-11T15:00Z &EndTime=2011-06-11T20:00Z
```

**返回示例**

XML格式： PolarDB PostgreSQL主备版开发指云原生数据库

```xml
<DescribeErrorLogsResponse> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> <TotalRecordCount>1</TotalRecordCount> <PageNumber>1</PageNumber> <PageRecordCount>1<PageRecordCount> <Items> <ErrorLog> <ErrorInfo>spid52 DBCC TRACEON 3499, server process ID (SPID) 52. This is an informat ional message only; no user action is required</ErrorInfo> <CreateTime>2013-06-04T15:00:00</CreateTime> </ErrorLog> </Items> </DescribeErrorLogsResponse>
```

JSON格式：

```json
{"RequestId":"1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC", "PageNumber":1, "TotalRecordCount":1, "PageRecordCount":1, "Items":{
 "ErrorLog":[{
  ErrorInfo:”spid52 DBCC TRACEON 3499, server process ID (SPID) 52. This is an inform
ational message only; no user action is required”,
  CreateTime:”2013-06-04T15:00:00”}]}}
```

#### 查询SQL审计功能是否开启

**描述**

查询指定PolarDB实例的SQL采集功能是否打开。

**请求参数**

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| Action | String | 是 | 系统规定参数，取值： DescribeSQLCollectorPolicy。 |
| DBInstanceId | String | 是 | 实例ID。 |

**返回参数**

| 名称 | 类型 | 描述 |
|---|---|---|
| <公共返回参数> |  | 公共返回参数，具体请参见公共返回参数。 |

PolarDB PostgreSQL主备版开发指云原生数据库

| SQLCollectorStatu s | String | Enable：SQL采集开启；Disabled：SQL采集关闭。 |
|---|---|---|

#### 切换SQL采集状态

**描述**

开启或关闭指定PolarDB实例的SQL采集功能。

**请求参数**

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| Action | Strin g | 是 | 系统规定参数，取值：ModifySQLCollectorPolicy。 |
| DBInstanceId | Strin g | 是 | 实例ID。 |
| SQLCollector Status | Strin g | 是 | Enable：SQL采集开启。 Disabled：SQL采集关闭。 |

**返回参数**

#### 查询SQL审计日志

**描述**

查询实例的SQL审计日志。

**请求参数**

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| Action | Stri ng | 是 | 系统规定参数，取值：DescribeSQLLogRecords。 |
| DBInstanc eId | Stri ng | 是 | 实例ID。 |
| Database | Stri ng | 否 | 数据库名称，默认为所有数据库。 |

PolarDB PostgreSQL主备版开发指云原生数据库

| User | Stri ng | 否 | 用户名称，默认为所有用户。 |
|---|---|---|---|
| Form | Stri ng | 否 | File，触发审计日志文件的生成，若传入这个值，则只返回公共参数，需再调用查询SQL审计文件列表接口获取文件的最终下载地址；Stream，返回数据流。默认为Stream。 |
| QueryKey words | Stri ng | 否 | 关键字查询，多个关键字以空格分隔，不超过10个关键字。 |
| StartTime | Stri ng | 是 | 查询开始时间，格式如：yyyy-MM-dd'`T'HH:mm:ssZ。 |
| EndTime | Stri ng | 是 | 查询结束时间，格式如：yyyy-MM-dd'T'HH:mm:ssZ，且大于查询开始时间。 |
| PageSize | Inte ger | 否 | 每页记录数，取值：30/50/100/200；默认值：100。 |
| PageNumb er | Inte ger | 否 | 页码大于0，且不超过Integer的最大值；默认值：1。 |

**返回参数**

| 名称 | 类型 | 描述 |
|---|---|---|
| <公共返回参数> | - | 公共返回参数，具体请参见公共返回参数。 |
| TotalRecordCount | Integer | 总记录数。 |
| PageNumber | Integer | 页码。 |
| PageRecordCount | Integer | 本页SQL日志明细个数。 |
| Items | List<SQLRecord > | SQL审计日志列表。 |

SQLRecord参数

| 名称 | 类型 | 描述 |
|---|---|---|
| DBName | String | 数据库名称。 |

PolarDB PostgreSQL主备版开发指云原生数据库

| AccountName | String | 账号名。 |
|---|---|---|
| HostAddress | String | 客户端IP地址。 |
| SQLText | String | SQL语句。 |
| TotalExecutionTimes | Long | 消耗时间，单位：微秒。 |
| ReturnRowCounts | Long | 返回记录数。 |
| ThreadID | String | 线程ID。 |
| ExecuteTime | String | 执行时间；格式：yyyy-MM-dd’T’HH:mm:ssZ，如2011-05-30 T12:11:20Z。 |

**示例**

**请求示例**

```
https://polardb.example.com/?Action=DescribeSQLLogRecords &DBInstanceId=polardb-xxxxx &StartTime=2011-06-11T15:00:00Z &EndTime=2013-06-05T15:00:00Z
```

**返回示例**

XML格式：

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

JSON格式： PolarDB PostgreSQL主备版开发指云原生数据库

```json
{"PageNumber":1,
    "RequestId":"08A3B71B-FE08-4B03-974F-CC7EA6DB1828",
    "TotalRecordCounts":1,
    "SQLItems":{
        "SQLItem":[
            {
                "ReturnRowCounts":34,
                "TotalExecutionTimes":12,
                "HostAddress":"192.168.xx.xx",
                "ExecuteTime":"2011-06-11T15:00:23Z",
                "SQLText":"update test.zxb set id=0 limit 1",
                "AccountName":"accounttest",
                "DBName":"test"
            }
```

]

```json
    },
    "ItemsCounts":1
}
```

#### 查询SQL审计文件列表

**描述**

**请求参数**

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| Action | String | 是 | 系统规定参数，取值：DescribeSQLLogFiles。 |
| DBInstanceI d | String | 是 | 实例ID。 |

**返回参数**

| 名称 | 类型 | 描述 |
|---|---|---|
| <公共返回参数> |  | 公共返回参数，具体请参见公共返回参数。 |
| TotalRecordCount | Interger | 总记录数。 |
| PageNumber | Interger | 页码。 |
| PageRecordCount | Interger | 本页记录数。 |

PolarDB PostgreSQL主备版开发指云原生数据库

| Items | List<LogFile> | 由审计文件组成的数组。 |
|---|---|---|

LogFile参数

| 名称 | 类型 | 描述 |
|---|---|---|
| FileID | Interger | 文件ID。 |
| DBInstanceId | String | 实例ID。 |
| LogStatus | String | SQL审计文件状态： Success：已生成； Failed：生成失败； Generating：生成中。 |
| LogStartTime | String | SQL起始时间。 |
| LogEndTime | String | SQL结束时间。 |
| LogDownloadU RL | String | 下载链接的地址。若当前不可下载，则为空串。 |
| LogSize | Long | 日志文件大小，单位：Byte。 |

### 数据迁移

#### 获取文件上传地址

**描述**

创建文件服务器的账号和密码，及上传的文件路径信息，用户根据此信息，可上传数据文件，待上传完成， 调用导入数据接口，进行外部数据迁移操作。

**请求参数**

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| Action | String | 是 | 系统规定参数，取值： CreateUploadPathForSQLServer。 |
| DBInstanceId | String | 是 | 实例ID。 |

PolarDB PostgreSQL主备版开发指云原生数据库

| DBName | String | 是 | 数据库名称。 |
|---|---|---|---|

**返回参数**

| 名称 | 类型 | 描述 |
|---|---|---|
| <公共返回参数> | - | 公共返回参数，具体请参见公共返回参数。 |
| InternetFtpServer | String | 外网文件服务器。 |
| InternetPort | Integer | 外网文件服务器端口。 |
| IntranetFtpServer | String | 内网服务器地址。 |
| IntranetPort | Integer | 内网服务器端口。 |
| UserName | String | 文件服务器账号。 |
| Password | String | 文件服务器账号密码。 |
| FileName | String | 文件名，带扩展名。 |

**示例**

**请求示例**

```
https://polardb.example.com/?Action= CreateUploadPathForSQLServer &DBInstanceId=polardb-xxxxx &DBName=testdb01
```

**返回示例**

XML格式：

```xml
<CreateUploadPathForSQLServerResponse> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> <InternetFtpServer>10.230.239.1</InternetFtpServer> <InternetPort>3021</InternetPort> <IntranetFtpServer></IntranetFtpServer> <UserName>userxxx</UserName> <Password>pwxxxxx</Password> <FileName>testdb01_xxxxx.bak</FileName> </CreateUploadPathForSQLServerResponse>
```

JSON格式： PolarDB PostgreSQL主备版开发指云原生数据库

```json
{"RequestId":"1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC",
 "InternetFtpServer ":"10.230.239.1",
 "InternetPort":3021,
 "IntranetFtpServer":"",
 "UserName":"userxxx",
 "Password":"pwxxxxx",
 "FileName":"testdb01_xxxxx.bak"}
```

#### 其他实例迁入

**描述**

从其他PolarDB实例迁入，支持MySQL的专享型实例。 对于MySQL实例，支持批量DB迁入。迁移过程中，源实例的状态处于“迁移中”，目标实例的状态处于“数据导入中”。 满足以下条件，适用于不同实例间（实例都属于同一个用户）的数据库迁移： 实例状态：运行中。 实例的数据库状态：运行中。 目标实例锁定模式：正常。 目标实例的存储空间 > 目标实例的使用空间－目标实例DB的空间+源实例DB的空间待迁移数据库在源实例和目标实例都必须存在，而且处于激活状态。

**请求参数**

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| Action | String | 是 | 系统规定参数，取值：ImportDatabaseBetweenInstances。 |
| DBInstanceId | String | 是 | 实例ID。 |
| SourceDBInstan ceId | String | 是 | 源实例ID，不能与待迁移实例相同。 |
| DBInfo | String | 是 | 待迁移实例的数据库信息，JSON格式。 对于MySQL实例，值为数组，示例：{"DBNames": ["mydb","mydb2"]}。MySQL类型要求源数据库和目的数据库名称必须一致，示例中的意思是两个数据库（mydb和mydb2）进行数据迁移，源实例和目的实例都有这两个数据库。 |

DBInfo参数

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|

PolarDB PostgreSQL主备版开发指云原生数据库

| DBNames | List | 是 | 待迁移的数据库名称列表，如["mydb","mydb2"]。 |
|---|---|---|---|

**返回参数**

| 名称 | 类型 | 描述 |
|---|---|---|
| <公共返回参数> |  | 公共返回参数，具体请参见公共返回参数。 |
| ImportId | Integer | 导入实例ID。 |

**示例**

**请求示例**

```
https://polardb.example.com/?Action=ImportDatabaseBetweenInstances &DBInstanceId=polardb-xxxxx &SourceDBInstanceId=polardb-xxxxx &{"DBNames":["mydb","mydb2"]}
```

**返回示例**

XML格式：

```xml
<ImportDatabaseBetweenInstancesResponse>
 <ImportId>2122321</ImportId>
 <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId>
 </ImportDatabaseBetweenInstancesResponse>
```

JSON格式：

```json
{"ImportId":2122321",
 RequestId":"1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC"}
```

#### 取消迁移

**描述**

支持取消其他PolarDB迁入（MySQL类型）的迁移任务。 支持取消MySQL类型的迁移任务。

**请求参数**

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| Action | String | 是 | 系统规定参数，取值：CancelImport。 |

PolarDB PostgreSQL主备版开发指云原生数据库

| DBInstanceId | String | 是 | 实例ID。 |
|---|---|---|---|
| ImportId | Integer | 是 | 迁移ID。 |

**返回参数**

| 名称 | 类型 | 描述 |
|---|---|---|
| <公共返回参数> | - | 公共返回参数，具体请参见公共返回参数。 |

**示例**

**请求示例**

```
https://polardb.example.com/?Action=CancelImport &DBInstanceId=polardb-xxxxx &ImportId=127562
```

**返回示例**

XML格式：

```xml
<CancelImportResponse> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> </CancelImportResponse>
```

JSON格式：

```json
{"RequestId": "1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC" }
```

### 标签管理

#### 绑定标签

**描述**

为实例绑定已有的或新创建的标签。 每个标签（Tag)由标签键（TagKey)和标签值（TagValue)组成，TagKey不能为空，TagValue可以为空。 TagKey，TagValue的值不允许以aliyun开头。 TagKey，TagValue不区分大小写。 TagKey 最长为64字符，TagValue 最长为128字符每个实例最多绑定10个Tag，每个实例绑定的TagKey不能重复。若绑定带有重复TagKey的Tag，则最后绑定的Tag将覆盖已绑定的Tag。

**请求参数**

PolarDB PostgreSQL主备版开发指云原生数据库

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| Action | String | 是 | 系统规定参数，取值：AddTagsToResource。 |
| RegionId | String | 是 | 地域。 |
| DBInstanceId | String | 是 | 实例ID，支持传入多个实例ID进行批量操作，最多传入30个。 格式示例：instance1,instance2,instance3 |
| Tags | Json String | 是 | 需要绑定的Tag列表，包括TagKey和TagValue，单次最多支持传入5组值。TagKey不能为空，TagValue可以为空。 格式示例：{“key1”:”value1”,“key2”:””} |

**返回参数**

| 名称 | 类型 | 描述 |
|---|---|---|
| <公共返回参数> | - | 公共返回参数，具体请参见公共返回参数 。 |

#### 查询标签

**描述**

查询账号下绑定PolarDB实例的标签信息。 如果传入指定实例ID，则查询该实例下所有标签，其他过滤条件失效。 若查询标签时仅传入标签键（TagKey)，未传入标签值（TagValue)，则返回所有符合标签键条件的结果。 若同时传入标签键和标签值，则只返回两个条件都符合的结果。

**请求参数**

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| Action | String | 是 | 系统规定参数，取值：DescribeTags。 |
| RegionId | String | 是 | 地域。 |
| DBInstanc eId | String | 否 | 实例ID，传入这个参数，其他过滤条件失效。 |

PolarDB PostgreSQL主备版开发指云原生数据库

| Tags | Json String | 否 | 需要查询的Tag列表，包括TagKey和TagValue。TagKey不能为空，TagValue可以为空。 格式示例：{“key1”:”value1”} |
|---|---|---|---|

**返回参数**

| 名称 | 类型 | 描述 |
|---|---|---|
| <公共返回参数> | - | 公共返回参数，具体请参见公共返回参数 。 |
| Items | List<TagInfos> | 由Tag信息组成的数组。 |

TagInfos

| 名称 | 类型 | 描述 |
|---|---|---|
| TagKey | String | 标签键。 |
| TagValue | String | 标签值。 |
| DBInstanceIds | List<DBInstanceId> | 该标签所绑定的实例ID。 |

DBInstanceId

| 名称 | 类型 | 描述 |
|---|---|---|
| DBInstanceId | String | 实例名称。 |

#### 解绑标签

**描述**

为实例解绑已绑定的标签。 单次最多支持解绑10个标签。 若一个标签所绑定的实例全都解绑，则该标签自动删除。 在解绑标签是仅传入标签键（TagKey)，未传入标签值（TagValue),则解绑符合TagKey条件的标签。

**请求参数**

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| Action | String | 是 | 系统规定参数，取值：RemoveTagsFromResource。 |

PolarDB PostgreSQL主备版开发指云原生数据库

| RegionId | String | 是 | 地域。 |
|---|---|---|---|
| DBInstanceI d | String | 是 | 实例ID。 |
| Tags | Json String | 是 | 需要解绑的Tag，包括TagKey和TagValue。TagKey不能为空，TagValue可以为空。 格式示例：{“key1”:”value1”} |

**返回参数**

| 名称 | 类型 | 描述 |
|---|---|---|
| <公共返回参数> | - | 公共返回参数，具体请参见公共返回参数 。 |

### 如何使用RAM授权

**使用RAM实现PolarDB资源授权**

您通过云账号创建的PolarDB实例，都是该账号自己拥有的资源。默认情况下，账号对自己的资源拥有完整的操作权限。 使用阿里云的RAM（Resource Access Management）服务，您可以将您云账号下PolarDB资源的访问及管理权限授予RAM中子用户。 如果您不需要使用RAM，请略过此章节。

**RAM中可授权的PolarDB资源类型**

目前，可以在RAM中进行授权的资源类型仅一种：dbinstance。在通过RAM进行授权时，资源的描述方式如下：

| 资源类型 | 授权策略中的资源描述方式 |
|---|---|
| Instance | acs:polardb:$regionid:$accountid:dbinstance/$dbinstanceid acs:polardb:$regionid:$accountid:dbinstance/ acs:polardb:::dbinstance/ |

其中：所有$regionid应为某个region的id，或者”*“。所有$dbinstanceid应为某个instance的id，或者“*”。以此类推，$account-id是您云账号的数字ID，可以用”*“代替。

**RAM中可对PolarDB资源进行授权的Action**

在RAM中，可以对一个PolarDB资源进行以下Action的授权。

| Action1 | Action2 |
|---|---|
| CreateDBInstance | ModifyDBInstanceSpec |

PolarDB PostgreSQL主备版开发指云原生数据库

| DeleteDBInstance | CreateReadonlyDBInstance |
|---|---|
| DescribeDBInstances | DescribeDBInstanceAttribute |
| SwitchDBInstanceNetType | RestartDBInstance |
| ModifyDBInstanceDescription | ModifySecurityIps |
| ModifyDBInstanceMaintainTime | UpgradeDBInstanceEngineVersion |
| PurgeDBInstanceLog | CreateDatabase |
| DeleteDatabase | DescribeDatabases |
| ModifyDBDescription | CreateUploadPathForSQLServer |
| DescribeFilesForSQLServer | ImportDataForSQLServer |
| DescribeImportsForSQLServer | ImportDataBaseBetweenInstances |
| CancelImport | CreateAccount |
| ResetAccountPassword | GrantAccountPrivilege |
| RevokeAccountPrivilege | DescribeAccounts |
| DeleteAccount | ModifyAccountDescription |
| CreateBackup | DescribeBackups |
| CreateTempDBInstance | DescribeBackupPolicy |
| ModifyBackupPolicy | DescribeResourceUsage |
| DescribeDBInstancePerformance | DescribeSlowLogs |
| DescribeSlowLogRecords | DescribeErrorLogs |

PolarDB PostgreSQL主备版开发指云原生数据库

| DescribeBinlogFiles | DescribeSQLLogReports |
|---|---|
| DescribeSQLLogRecords | DescribeOptimizeAdviceOnStorage |
| DescribeOptimizeAdviceOnMissPK | DescribeOptimizeAdviceOnExcessIndex |
| DescribeOptimizeAdviceOnMissIndex | DescribeOptimizeAdviceByDBA |
| DescribeParameters | ModifyeParameter |

**说明**

除了DescribeRegions，DescribeParameterTemplates参数外，其他接口都可以鉴权。

**授权访问鉴权规则**

当子用户通过PolarDB API进行资源访问时，PolarDB后台向RAM进行权限检查，以确保调用者拥有响应权限。每个不同的PolarDB API会根据涉及到的资源以及API的语义来确定需要检查哪些资源的权限。每个API 的鉴权规则见下表：

| Action | 鉴权规则 |
|---|---|
| CreateDBInstance | acs:polardb:$regionid:$accountid:dbinstance/$dbinstance id |
| DeleteDBInstance | acs:polardb:$regionid:$accountid:dbinstance/$dbinstance id |
| DescribeDBInstances | acs:polardb:$regionid:$accountid:dbinstance/$dbinstance id |
| SwitchDBInstanceNetType | acs:polardb:$regionid:$accountid:dbinstance/$dbinstance id |
| ModifyDBInstanceDescription | acs:polardb:$regionid:$accountid:dbinstance/$dbinstance id |
| ModifyDBInstanceMaintainTime | acs:polardb:$regionid:$accountid:dbinstance/$dbinstance id |
| PurgeDBInstanceLog | acs:polardb:$regionid:$accountid:dbinstance/$dbinstance id |

PolarDB PostgreSQL主备版开发指云原生数据库

| DeleteDatabase | acs:polardb:$regionid:$accountid:dbinstance/$dbinstance id |
|---|---|
| ModifyDBDescription | acs:polardb:$regionid:$accountid:dbinstance/$dbinstance id |
| DescribeFilesForSQLServer | acs:polardb:$regionid:$accountid:dbinstance/$dbinstance id |
| DescribeImportsForSQLServer | acs:polardb:$regionid:$accountid:dbinstance/$dbinstance id |
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
| DescribeSQLLogRecords | acs:polardb:$regionid:$accountid:dbinstance/$dbinstance id |

PolarDB PostgreSQL主备版开发指云原生数据库

| DescribeOptimizeAdviceOnMissPK | acs:polardb:$regionid:$accountid:dbinstance/$dbinstance id |
|---|---|
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
| CreateUploadPathForSQLServer | acs:polardb:$regionid:$accountid:dbinstance/$dbinstance id |
| ImportDataForSQLServer | acs:polardb:$regionid:$accountid:dbinstance/$dbinstance id |

PolarDB PostgreSQL主备版开发指云原生数据库

| ImportDataBaseBetweenInstances | acs:polardb:$regionid:$accountid:dbinstance/$dbinstance id |
|---|---|
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

PolarDB PostgreSQL主备版开发指云原生数据库

### 附表

#### 客户端错误代码表

##### 公共错误

| 错误代码 | 描述 | HTTP状态码 |
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

PolarDB PostgreSQL主备版开发指云原生数据库

| Invalid<parameter name>.ValueNotSupport ed | The specified parameter “parameter name” is not valid. | 400 |
|---|---|---|
| Invalid<parameter name>.Malformed | The specified parameter "parameter name n" is not valid. | 400 |
| InvalidParameter | The specified parameter " parameter name n " is not valid. | 400 |

##### 特定错误

| 错误代码 | 描述 | HTTP状态码 |
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

PolarDB PostgreSQL主备版开发指云原生数据库

| OperationDenied.DBInstanceType | The operation is not permitted due to type of instance. | 400 |
|---|---|---|
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

PolarDB PostgreSQL主备版开发指云原生数据库

| OperationDenied.DBStatus | The operation is not permitted due to status of database. | 403 |
|---|---|---|
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

PolarDB PostgreSQL主备版开发指云原生数据库

| QuotaExceeded.AccountName | The quota of account exceeds. | 403 |
|---|---|---|
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

PolarDB PostgreSQL主备版开发指云原生数据库

| IncorrecttVpcId.Mismatch | The specified parameter "VpcId " is not valid. | 400 |
|---|---|---|
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

PolarDB PostgreSQL主备版开发指云原生数据库

| InvalidParameter | The specified parameter "dbInstanceId" is not valid. | 400 |
|---|---|---|
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
| OperationDenied | The resource is out of usage. | 403 |

PolarDB PostgreSQL主备版开发指云原生数据库

| OperationDenied | The vpc cloudinstanceIp is use, please check params. | 406 |
|---|---|---|
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
| bpcIzNoNotEqualsRdsMultIzNo | Specified vpc IzNo not equal rds IzNo. | 400 |

| 云原生数据库 | PolarDB PostgreS | QL主备版开发指南·API参考 |
|---|---|---|

#### 服务器端错误代码表

| 错误代码 | 描述 | HTTP状态码 |
|---|---|---|
| ServiceUnavailabl e | The request has failed due to a temporary failure of the server. | 503 |
| InternalError | The request processing has failed due to some unknown error, exception or failure. | 500 |

#### 实例状态表

| 状态 | 说明 |
|---|---|
| Creating | 创建中。 |
| Running | 使用中。 |
| Deleting | 删除中。 |
| Rebooting | 重启中。 |
| DBInstanceClassChanging | 升降级中。 |
| TRANSING | 迁移中。 |
| EngineVersionUpgrading | 迁移版本中。 |
| TransingToOthers | 迁移数据到其他PolarDB中。 |
| GuardDBInstanceCreating | 生产灾备实例中。 |
| Restoring | 备份恢复中。 |
| Importing | 数据导入中。 |
| ImportingFromOthers | 从其他PolarDB实例导入数据中。 |

PolarDB PostgreSQL主备版开发指云原生数据库

| DBInstanceNetTypeChanging | 内外网切换中。 |
|---|---|
| GuardSwitching | 容灾切换中。 |
| INS CLONING _ | 实例克隆中。 |

#### 字符集表

本文为您介绍PolarDB支持的字符集表。

**PolarDB PostgreSQL版支持的字符集**

| 字符集 | 字符集 | 字符集 |
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
| koi8u | latin9 |  |
| iso 8859 5 _ _ | latin10 |  |

PolarDB PostgreSQL主备版开发指云原生数据库

## SDK参考

### 获取SDK源代码

您可以通过SDK工具，按需定制所需的SDK语言。

**前提条件**

已获取Apsara Stack运维系统的访问地址。Apsara Stack运维系统访问地址格式为http://${regionid}.aso.${intranet-domain-id}.com。 推荐使用Chrome浏览器。

**操作步骤**

1. 登录Apsara Stack运维系统。
i. 在浏览器地址栏中，输入Apsara Stack运维系统的访问地址 http://${region-id}.aso.${intranetdomain-id}.com，按下回车键。 ii. 输入正确的用户名及密码。 iii. 单击**登录**，进入**Apsara Stack****运维系统**页面。
2. 登录阿里云专有云运维API平台。在页面左侧导航栏中，单击**产品运维管理** **> Opsapi**，进入**专有云运维**
**API**平台。
3. 下载SDK源代码。
PolarDB PostgreSQL主备版开发指云原生数据库 i. 在左侧导航栏中，选择**版本管理** **> SDK****工具**。 ii. 单击页面顶部右上角**SDK****按需定制**。 iii. 在弹出的**专有云****SDK****定制**页面，从左到右依次选择对应的专有云版本、产品名称、产品版本、SDK版本、API版本和SDK语言。 iv. 填写完成后，单击**创建****SDK**。 v. 单击**下载**，下载对应的SDK。

### Java SDK调用

#### 使用手册

##### 使用CommonRequest进行调用

当您要调用的某个产品的API没有提供SDK时，可以采用泛用型的API调用方式（CommonRequest）。使用CommonRequest调用方式可实现任意Open API接口的调用。

**CommonRequest调用特点**

CommonRequest的特点如下：
1. 轻量：只需Core包即可发起调用，无需下载安装各产品的SDK。
2. 简便：无需更新SDK即可调用最新发布的API。
3. 快速迭代。
发起一次CommonRequest请求，您需要获取以下几个参数的值。您可以在各产品的API文档中获取以下参数的值。 域名（domain）：该产品的服务地址。 API版本（version）：该API的版本号，格式为YYYY-MM-DD。 您可以在各产品的API文档的公共参数部分获取API版本。 PolarDB PostgreSQL主备版开发指云原生数据库接口信息：要调用的接口名称。 您需要获取**Action**参数，使用 `request.ApiName = "<Action>"` 的方式来指定API名称。 例如RunInstances接口，在发起CommonRequest请求时，需要使用 `request.ApiName =` `"RunInstances"` 来指定API名称。 您需要获取**PathPattern**参数，使用 `request.PathPattern = "<PathPattern>"` 的方式来指定 RESTful路径。 例如查看所有集群实例的API的**PathPattern**为 `/clusters` ，在发起CommonRequest请求时，要使用 `request.PathPattern = "/clusters"` 指定RESTful路径。

**示例：调用RPC风格的API**

以下代码展示了如何使用CommonRequest的方式调用的DescribeDBInstanceAttribute接口：

```java
import com.aliyuncs.CommonRequest; import com.aliyuncs.CommonResponse; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.exceptions.ServerException; import com.aliyuncs.profile.DefaultProfile; public class Sample {
    public static void main(String[] args) {
```

`//` 创建`DefaultAcsClient`实例并初始化

```
        DefaultProfile profile = DefaultProfile.getProfile(
            "<your-region-id>",          // 您的地域ID
            "<your-access-key-id>",      // 您的AccessKey ID
            "<your-access-key-secret>"); // 您的AccessKey Secret
        IAcsClient client = new DefaultAcsClient(profile);
```

`//` 创建`API`请求并设置参数

```java
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
        }
    }
}
```

**示例：调用RESTful风格的API**

以下代码展示了如何使用CommonRequest的方式调用的查看所有集群实例接口： PolarDB PostgreSQL主备版开发指云原生数据库

```java
import com.aliyuncs.CommonRequest; import com.aliyuncs.CommonResponse; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.exceptions.ServerException; import com.aliyuncs.profile.DefaultProfile; public class Sample {
    public static void main(String[] args) {
```

`//` 创建`DefaultAcsClient`实例并初始化

```
        DefaultProfile profile = DefaultProfile.getProfile(
            "<your-region-id>",          // 您的地域ID
            "<your-access-key-id>",      // 您的AccessKey ID
            "<your-access-key-secret>"); // 您的AccessKey Secret
        IAcsClient client = new DefaultAcsClient(profile);
```

`//` 创建`API`请求并设置参数

```java
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
        }
    }
}
```

### Python SDK调用

#### 使用手册

##### 使用CommonRequest进行调用

当您要调用的某个产品的API没有提供SDK时，可以采用泛用型的API调用方式（CommonRequest）。使用CommonRequest调用方式可实现任意Open API接口的调用。

**CommonRequest调用特点**

CommonRequest的特点如下：
1. 轻量：只需Core包即可发起调用，无需下载安装各产品的SDK。
2. 简便：无需更新SDK即可调用最新发布的API。
3. 快速迭代。
PolarDB PostgreSQL主备版开发指云原生数据库发起一次CommonRequest请求，您需要获取以下几个参数的值。您可以在各产品的API文档中获取以下参数的值。 域名(domain)：该产品的服务地址。 API版本(version)：该API的版本号，格式为YYYY-MM-DD。 您可以在各产品的API文档的公共参数部分获取API版本。 接口信息：要调用的接口名称。 您需要获取**Action**参数，使用 `request.ApiName`

```
                            =
```

`"<Action>"` 的方式来指定API名称。 例如RunInstances接口，在发起CommonRequest请求时，需要使用 `request.ApiName` `= "RunInstances"` 来指定API名称。 您需要获取**PathPattern**参数，使用 `request.PathPattern`

```
                            =
```

`"<PathPattern>"` 的方式来指定RESTful路径。

|  | /clusters |  | ，在发起Comm |
|---|---|---|---|
| request.PathPattern |  |  |  |
|  |  | 指定RESTful路径。 |  |

**示例：调用RPC风格的API**

以下代码展示了Python2.x如何使用CommonRequest的方式调用的DescribeDBInstanceAttribute接口：

```bash
from aliyunsdkcore.client import AcsClient from aliyunsdkcore.request import CommonRequest client = AcsClient('{your_access_key_id}', '{your_access_key_secret}', '{your_region_id}') request = CommonRequest() request.set_domain('polardb-xxxxx.xxx.com') request.set_version('2024-01-30') request.set_action_name('DescribeDBInstanceAttribute')
# or:
# request = CommonRequest(domain='polardb.aliyuncs.com', version='2024-01-30', action_n
ame='DescribeDBInstanceAttribute') request.add_query_param('PageNumber', '1') request.add_query_param('PageSize', '30') response = client.do_action_with_exception(request)
```

**示例：调用RESTful风格的API**

以下代码展示了Python2.x如何使用CommonRequest的方式调用的查看所有集群实例接口： PolarDB PostgreSQL主备版开发指云原生数据库

```bash
from aliyunsdkcore.client import AcsClient from aliyunsdkcore.request import CommonRequest client = AcsClient('{your_access_key_id}', '{your_access_key_secret}', '{your_region_id}') request = CommonRequest() request.set_domain('polardb-xxxxx.xxx.com') request.set_version('2024-01-30') request.set_uri_pattern('/clusters')
# or:
# request = CommonRequest(domain='polardb.aliyuncs.com', version='2024-01-30', uri_patt
ern='/clusters') response = client.do_action_with_exception(request)
```

### PHP SDK调用

#### 快速开始

阿里云PHP SDK让您不用复杂编程即可访问。本操作介绍如何获取阿里云PolarDB PHP SDK并开始调用。

**环境准备**

使用PHP SDK前，您需要一个授权账号以及一对AccessKey ID和AccessKey Secret。参见获取 Accesskey在ASCM控制台上获取和查看您的AccessKey。 阿里云PHP SDK适用于PHP的5.3、5.4、5.5、5.6、7.0和7.1版本。（您可以通过**php -v**命令来获得当前使用的PHP版本号。）

**安装阿里云 PHP SDK**

完成以下操作安装PHP SDK：
1. 从专有云官网下载PHP SDK的源代码。
2. 添加PHP SDK引用。
假设PHP SDK下载后的路径为 `/path/to/aliyun-openapi-php-sdk` 。

```
require_once '/path/to/aliyun-openapi-php-sdk/aliyun-php-sdk-core/Config.php';
```

**使用PHP SDK**

以下这个代码示例展示了调用阿里云PHP SDK的3个主要步骤：
1. 创建并初始化DefaultAcsClient实例。
在创建DefaultAcsClient实例并初始化时，您需要提供**Region ID**、**AccessKey ID**和**AccessKey**
**Secret**这三个参数的值。
2. 创建API请求并设置参数。
3. 发起请求并处理应答或异常。
PolarDB PostgreSQL主备版开发指云原生数据库

```
<?php use PolarDB\Request\V20140526\DescribeDBInstanceAttributeRequest;
```

# 创建`DefaultAcsClient`实例并初始化

```
$clientProfile = DefaultProfile::getProfile(
    "<your-region-id>",                   # 您的 Region ID
    "<your-access-key-id>",               # 您的 AccessKey ID
    "<your-access-key-secret>"            # 您的 AccessKey Secret
); $client = new DefaultAcsClient($clientProfile);
```

# 设置当前产品的`endpoint`

```
$profile->endpoint ="your-region-id", "your-region-id", "product", "endpoint";
```

# 创建`API`请求并设置参数

```
$request = new DescribeDBInstanceAttributeRequest(); $request->setPageSize(10);
```

# 发起请求并处理返回

```
try {
    $response = $client->getAcsResponse($request);
    print_r($response);
} catch(ServerException $e) {
    print "Error: " . $e->getErrorCode() . " Message: " . $e->getMessage() . "\n";
} catch(ClientException $e) {
    print "Error: " . $e->getErrorCode() . " Message: " . $e->getMessage() . "\n";
}
```

?>

### C# SDK调用

**环境准备**

framework 2.0+

**下载 SDK**

下载 C# SDK 的源代码：https://github.com/aliyun/aliyun-openapi-net-sdk

**安装 SDK**

1. 从上面的下载链接下载相应产品 C# SDK 的源代码，并编译成为 .dll 文件。
2. 右击您的 Visual Studio 项目，然后单击**添加引用** > **浏览**（如果您用的是 MonoDevelop，请自行按照
相应导入 .dll 的方法导入这个.dll文件）。
3. 选择上述的 .dll 文件，单击**确定**按钮，然后您就可以在工程中使用阿里云 C# SDK 了。
PolarDB PostgreSQL主备版开发指云原生数据库

## 获取endpoint

您可以通过Apsara Stack运维系统获取产品的endpoint。

**方式一**

1. 登录Apsara Stack运维系统。
登录Apsara Stack运维系统相关操作，请参见**《运维指南》**中**基础平台运维** **> Apsara Stack****运维系** 统 > **登录****Apsara Stack****运维系统**章节的描述。
2. 在页面左侧导航栏中，选择**产品运维管理** > **产品列表** > **云平台运维**。
3. 单击**天基**，跳转至天基portal。
4. 在顶部菜单栏中，选择**报表** > **系统报表**。
5. 在**系统报表**详情页面，单击**服务注册变量**。
6. 在**服务注册变量**详情页面，找到polardb-yaochi行，右击对应的**Service Registration**列单元格，选
择**显示更多**。
7. 在弹出的**详情**提示框中，根据PolarDB产品的key值（polardb.openapi.endpoint），找到PolarDB的
endpoint。

**方式二**

1. 登录Apsara Stack运维系统。
登录Apsara Stack运维系统相关操作，请参考**《运维指南》**中**基础平台运维** **> Apsara Stack****运维系** 统 > **登录****Apsara Stack****运维系统**章节的描述。
2. 在页面左侧导航栏中，选择菜单，进入**产品运维管理**产品列表页面。
3. 单击**天基**，跳转至天基portal。
4. 在顶部菜单栏中，选择**运维** > **机器运维**，进入**机器运维**页面。
5. 在机器列表中，选择任意一台机器，单击**Terminal**，登录到机器。
PolarDB PostgreSQL主备版开发指云原生数据库
6. 在机器中执行如下命令：**curl -l**

**"http://127.0.0.1:7070/api/v3/column/c.sr.service_registration,c.sr.id?**

**c.sr.service_registration"**，获取json数据。
7. 根据PolarDB产品的ID（polardb-yaochi）和key值（polardb.openapi.endpoint），找到PolarDB的
endpoint。 PolarDB PostgreSQL主备版开发指云原生数据库

## 获取Accesskey

**获取组织AccessKey**

获取组织AccessKey的方法如下：
1. 管理员登录ASCM控制台。
2. 在页面顶部菜单栏上，单击**企业**。
3. 在**企业**页面的左侧导航栏中，单击**组织管理**。
4. 在组织结构中，单击要添加的上级组织后面的
。
5. 在弹出的下拉菜单中，选择**获取组织****Accesskey**。
6. 在弹出的对话框中，查看组织Accesskey信息。
一级组织的AccessKey为系统自动分配，下级组织使用一级组织的AccessKey。

**说明**

**获取个人账号AccessKey**

获取个人账号AccessKey的方法如下：
1. 管理员登录ASCM控制台。
2. 在系统界面右上角，单击当前登录用户的头像，选择**个人信息**。
3. 在**阿里云****AccessKey**模块，您可以查看个人账户的AccessKey信息。
Accesskey ID和AccessKey Secret是您访问云资源时的密钥，具有该账号完整的权

**说明**

限，请您妥善保管。
