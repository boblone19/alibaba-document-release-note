---
title: "云原生关系型数据库 PolarDB PolarDB MySQL主备版 开发指南"
product_version: "v3.18.6-SP2607"
doc_version: "20260729"
pdf_pages: 146
source_pdf: "71_PolarDB MySQL主备版 开发指南_development-guide-polardb-mysql-local-disk-version.pdf"
source_url: "https://apsara-doc.oss-cn-hangzhou.aliyuncs.com/apsara-pdf/enterprise/v_3_18_6_20260730/polardb/zh/development-guide-polardb-mysql-local-disk-version.pdf"
converter: line-classifier (PyMuPDF)
---

# 云原生关系型数据库 PolarDB PolarDB MySQL主备版 开发指南

云原生数据库 I参考

## API参考

### API 概览

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

云原生数据库 I参考

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

云原生数据库 I参考

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
| ModifyBackupPolicy | 修改备份策略。 |

云原生数据库 I参考

| RestoreDBInstance | 恢复备份集到实例。 |
|---|---|
| DeleteBackup | 删除数据备份文件。 |

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
| ModifyParameter | 修改数据库参数列表。 |

**PolarDB日志管理**

| API | 描述 |
|---|---|
| DescribeSlowLogs | 查看慢日志列表。 |
| DescribeSlowLogRecords | 查看慢日志明细。 |
| DescribeErrorLogs | 查看错误日志。 |
| DescribeBinlogFiles | 查看BINLOG日志。 |

云原生数据库 I参考

| DescribeSQLCollectorPolicy | 查询SQL审计功能是否开启。 |
|---|---|
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

| API | 描述 |
|---|---|
| AddTagsToResource | 绑定标签。 |
| DescribeTags | 查询标签。 |
| RemoveTagsFromResource | 解绑标签。 |

### 调用方式

#### 请求结构

本章介绍云数据库PolarDB API的请求结构。

**服务地址**

云原生数据库 I参考 PolarDB API的服务接入地址为：polardb.example.com。关于如何获取产品的endpoint，参见获取 ASAPI的endpoint。

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
| Version | Stri ng | 是 | API版本号，为日期形式：YYYY-MM-DD，本版本对应为2024-01-30。 |
| AccessKeyId | Stri ng | 是 | 阿里云颁发给用户的访问服务所用的密钥ID。 |
| Signature | Stri ng | 是 | 签名结果串，关于签名的计算方法，请参见签名机制。 |
| SignatureMet hod | strin g | 是 | 签名方式，目前支持HMAC-SHA1。 |
| Timestamp | Stri ng | 是 | 请求的时间戳。日期格式按照ISO8601标准表示，并需要使用UTC时间。格式为：YYYY-MM-DDThh:mm:ssZ；例如，2013-08-15T12:00:00Z（为北京时间2013年8月15日20点0分0秒）。 |
| SignatureVer sion | Stri ng | 是 | 签名算法版本，目前版本是1.0。 |

云原生数据库 I参考

| SignatureNo nce | Stri ng | 是 | 唯一随机数，用于防止网络重放攻击。用户在不同请求间要使用不同的随机数值。 |
|---|---|---|---|

**示例**

```
https://polardb.example.com/ ?Format=xml &Version=2024-01-30 &Signature=Pc5WB8gokVnxxxxx &SignatureMethod=HMAC-SHA1 &SignatureNonce=15215528852396 &SignatureVersion=1.0 &AccessKeyId=key-test &OwnerId=12345678 &Timestamp=2024-07-12T12:00:00Z
```

##### 公共返回参数

用户发送的每次接口调用请求，无论成功与否，系统都会返回一个唯一识别码RequestId给用户。

**示例**

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

<!—返回结果数据`-->` `</`接口名称`+Response>` JSON示例： 云原生数据库 I参考

```json
{ "RequestId": "4C467B38-****-447D-****-AC04*******16", /* 返回结果数据 */}
```

##### 错误结果

调用接口出错后，将不会返回结果数据。调用方可根据附表错误代码表来定位错误原因。 当调用出错时，HTTP请求返回一个4xx或5xx的HTTP状态码。 返回的消息体中是具体的错误代码及错误信息。 另外还包含一个全局唯一的请求IDRequestId和一个您该次请求访问的站点IDHostId。在调用方找不到错误原因，可以联系阿里云客服，并提供该HostId和RequestId，以便我们尽快帮您解决问题。 XML示例：

```xml
<Error> <RequestId>8906582E-****-****-A6C4-0E78*******5</RequestId> <HostId>polardb.example.com</HostId> <Code>UnsupportedOperation</Code> <Message>The specified action is not supported.</Message> </Error>
```

JSON示例：

```json
{ "RequestId": "7463B73D-****-4D19-****-6B8*******2EF", "HostId": "polardb.example.com", "Code": "UnsupportedOperation", "Message": "The specified action is not supported." }
```

#### 签名机制

PolarDB服务会对每个访问的请求进行身份验证，所以无论使用HTTP还是HTTPS协议提交请求，都需要在请求中包含签名（Signature）信息。关于如何获取 Access Key，参见获取AccessKey。 PolarDB通过使用Access Key ID和Access Key Secret进行对称加密的方法来验证请求发送者的身份。 Access Key ID和Access Key Secret由阿里云官方颁发给访问者（可以通过阿里云官方网站申请和管理）： Access Key ID用于标识访问者的身份。 Access Key Secret是用于加密签名字符串和服务器端验证签名字符串的密钥，必须严格保密，只有阿里云和用户知道。 用户在访问时，按照如下方法对请求进行签名处理：
1. 使用请求参数构造规范化的请求字符串（Canonicalized Query String）。
i. 按照参数名称的字典顺序对请求中所有的请求参数进行排序。 所有的请求参数包括公共参数和请求接口的自定义参数，不包括公共请求参数中提到的Signature参数本身。

**说明**

当使用GET方法提交请求时，这些参数就是请求URI中的参数部分，即URI中“?”之后由“&”连接的部分。 云原生数据库 I参考 ii. 对每个请求参数的名称和值进行编码。 名称和值要使用UTF-8字符集进行URL编码。 URL编码的编码规则是： 对于字符 A-Z、a-z、0-9以及字符“-”、“_”、“.”、“~”不编码。 对于其他字符编码成“%XY”的格式。 其中XY是字符对应ASCII码的16进制表示，比如英文的双引号（”）对应的编码就是%22。 对于扩展的UTF-8字符，编码成“%XY%ZA…”的格式。 英文空格要被编码是%20，而不是加号（+）。

**说明**

一般支持URL编码的库，比如Java中的java.net.URLEncoder，都是按照“application/xwww-form-urlencoded”的MIME类型的规则进行编码的。 实现时可以直接使用这类方式进行编码，把编码后的字符串中加号（+）替换成%20、星号（*）替换成%2A、%7E替换回波浪号（~），即可得到上述规则描述的编码字符串。 iii. 对编码后的参数名称和值使用英文等号（=）进行连接。 iv. 将英文等号连接得到的字符串按参数名称的字典顺序依次使用&符号连接，即得到规范化请求字符串。
2. 使用上一步构造的规范化字符串按照下面的规则构造用于计算签名的字符串。

```
StringToSign= HTTPMethod + “&” + percentEncode(“/”) + ”&” + percentEncode(CanonicalizedQueryString)
```

HTTPMethod是用于提交请求的HTTP方法，比如GET。 percentEncode("/")是按照1.b中描述的URL编码规则对字符 "/"进行编码得到的值，即"%2F"。 percentEncode(CanonicalizedQueryString)是对1中构造的规范化请求字符串按1.b描述的URL编码规则编码后得到的字符串。
3. 按照RFC2104的定义，使用上述用于签名的字符串计算签名HMAC值。

**说明**

计算签名时使用的Key就是用户持有的Access Key Secret并加上一个"&”字符（ASCII:38），使用的哈希算法是SHA1。
4. 按照Base64编码规则把上面的HMAC值编码成字符串，即得到签名值（Signature）。
5. 将得到的签名值作为Signature参数添加到请求参数中，即完成对请求签名的过程。

**说明**

得到的签名值在作为最后的请求参数值提交给PolarDB服务器的时候，要和其他参数一样，按照 RFC3986的规则进行URL编码）。 以DescribeDBInstances为例，签名前的请求URL为： 云原生数据库 I参考

```
http://polardb.example.com/?TimeStamp=2013-06- 01T10:33:56Z&Format=XML&AccessKeyId=testid&Action=DescribeDBInstances&SignatureMethod=H C-SHA1&RegionId=region1&SignatureNonce=NwDAxvLU6tFE0DVb&Version=2014-08- 15&SignatureVersion=1.0
```

那么StringToSign就是：

```
GET&%2F&AccessKeyId%3Dtestid%26Action%3DDescribeDBInstances%26Format%3DXML%26RegionId%3 egion1%26SignatureMethod%3DHMAC- SHA1%26SignatureNonce%3DNwDAxvLU6tFE0DVb%26SignatureVersion%3D1.0%26TimeStamp%3D2013- 06-01T10%253A33%253A56Z%26Version%3D2014-08-15
```

假如使用的Access Key Id是“testid”，Access Key Secret是“testsecret”，用于计算HMAC的Key就是“testsecret&”，则计算得到的签名值是：

```
BIPOMlu8LXBeZtLQkJTw6iFvw1E=
```

签名后的请求URL为：此处增加了Signature参数。

```
http://polardb.example.com/?TimeStamp=2013-06- 01T10%3A33%3A56Z&Format=XML&AccessKeyId=testid&Action=DescribeDBInstances&SignatureMeth =HMAC-SH
```

### 实例管理

#### 创建实例

创建PolarDB数据库实例。

**请求头**

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| AccessKey Id | Strin g | Query | 否 | LTAI4G28PhwnizaSC**** **** | 访问密钥ID。 |
| Action | Strin g | Query | 否 | CreateDBInstance | 系统规定参数。取值： CreateDBInstance。 |
| OwnerId | Long | Query | 否 | 1234567890 | 鉴权相关的系统参数，不填。 |
| Resource OwnerAcc ount | Strin g | Query | 否 | test | 鉴权相关的系统参数，不填。 |
| Resource OwnerId | Long | Query | 否 | 345678912345 | 鉴权相关的系统参数，不填。 |

| 云原生数据库 |  |  |  | PolarD | B MySQL主备版开发指南·A I参考 |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | Strin g | Query | 是 | cn-hangzhou | 地域ID。 |
| Engine | Strin g | Query | 是 | MySQL | 数据库类型，如下： MySQL PolarDB PG _ PolarDB PPAS _ |
| EngineVer sion | Strin g | Query | 是 | 8.0 | 数据库版本号，如下： MySQL：5.7、8.0。 PolarDB PG：14、 _ 16、17。 PolarDB PPAS：14、 _ 16、17。 |
| DBInstanc eClass | Strin g | Query | 是 | polar.mysql.x2.medium | 实例规格。 |
| DBInstanc eStorage | Integ er | Query | 是 | 20 | 自定义存储空间，取值范围 [5,2000] ，存储空间每5G进行递增。单位： GB。 |
| DBInstanc eStorageT ype | Strin g | Query | 否 | local ssd _ | 实例存储类型，不支持修改。 |
| SystemDB Charset | Strin g | Query | 否 | utf-8 | 数据库字符集类型。 |
| DBInstanc eNetType | Strin g | Query | 是 | Intranet | 目标实例的网络连接类型， 取值： Internet ：公网连接 Intranet ：内网连接 |
| DBInstanc eDescripti on | Strin g | Query | 否 | test | 实例描述。 |
| SecurityIP List | Strin g | Query | 是 | 10.***.***.*** | PolarDB集群白名单IP地址。 支持配置多个白名单IP 地址，多个IP地址之间使用英文逗号（,）分隔。 |

云原生数据库 I参考

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| ClientToke n | Strin g | Query | 否 | 6000170000591aed949 d0f54a343f1a4233c1e7 d1c5c****** | 用于保证请求的幂等性，防止重复提交请求。由客户端生成该参数值，保证在不同请求间唯一，大小写敏感、 不超过64个ASCII字符。 |
| PayType | Strin g | Query | 是 | Postpaid | 付费类型，取值范围如下： Postpaid ：按量付费 Prepaid ：预付费 （包年包月） |
| ZoneId | Strin g | Query | 否 | cn-hangzhou-i | 可用区ID。 您可以通过 DescribeRegions接口查看可选的可用区。 |
| InstanceN etworkTyp e | Strin g | Query | 否 | VPC | 存储层实例网络类型，取值： VPC ：专有网络 CLASSIC ：经典网络 |
| VPCId | Strin g | Query | 否 | vpc-********** | 交换机所属专有网络ID。 VpcId 和Dedicat edHostGroupId 参数至少输入一个。 |
| VSwitchId | Strin g | Query | 否 | vsw-********** | 虚拟交换机ID。 如果已选择VPCId，则 VSwitchId必选。 |
| PrivateIpA ddress | Strin g | Query | 否 | true | 实例私有IP地址。该IP地址必须为交换机 （ VSwitchId ）网段的空闲地址。 |
| OwnerAcc ount | Strin g | Query | 否 | test | 鉴权相关的系统参数，不填。 |
| Resource GroupId | Strin g | Query | 否 | rg-************ | 资源组ID。 |

云原生数据库 I参考

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| DBIsIgnor eCase | Strin g | Query | 否 | true | 表名是否区分大小写，取值： true ：不区分大小写 （默认）。 false ：区分大小写。 |
| DBName | Strin g | Query | 否 | testdb | 数据库名称。 |
| Port | Strin g | Query | 否 | 1521 | 监听端口。默认为1521， 取值范围为 [1521,65500] 。 |
| Character SetName | Strin g | Query | 否 | utf8 | 字符集。 |
| DBParam GroupId | Strin g | Query | 否 | mysql-sys-**** | 参数模板ID，可调用 DescribeParameterGrou ps查询。 对于PolarDB MySQL 主备版，如需创建内核版本为8.4的集群，请务必将参数模板配置为 mysql-sys- 01040401020200。 创建前请先参见《运维指南》中“开启 PolarDB MySQL 8.4 内核参数开关”教程， 在Apsara Uni- manager运维控制台启用对应开关，启用后调用API创建即可。若无运维平台操作权限， 请联系阿里云技术支持协助开启。 |
| IPVersionS electedTy pe | Strin g | Query | 否 | IPV4V6 | IP类型，取值如下： IPV4 （默认值）：仅分配IPv4地址。 IPV6 ：仅分配IPv6地址。 IPV4V6 ：同时分配 IPv4和IPv6地址。 |

云原生数据库 I参考

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| SecurityIP v6List | Strin g | Query | 否 | 2001:db8::1/24 | 该实例的IPv6白名单。多条记录请以英文逗号（,）隔开，不可重复，最多1000 条记录。支持如下两种格式： IP地址形式，例如： 2001:db8::1。 CIDR形式，例如： 2001:db8::1/24（无类域间路由，24表示了地址中前缀的长度，范围为 0~128）。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 9B7BFB11-C077- 4FE3-B051- F69CEB****** | 请求ID。 |
| DBInstanceId | String | POLARDB-cn- ************** | 节点ID。 |
| OrderId | String | 2035638******* | 订单ID。 仅当 Action 取值为CreateDBNodes 或ModifyDBNo deClass 时返回该参数。 |
| ConnectionStri ng | String | abc.polardb.rds.ali yuncs.com | 连接串。 |
| Port | String | 1521 | 链接地址的端口号。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=CreateDBInstance &RegionId=cn-hangzhou &Engine=MySQL &EngineVersion=8.0 &DBInstanceClass=polar.mysql.x2.medium &DBInstanceStorage=20 &DBInstanceNetType=Intranet &SecurityIPList=10.***.***.*** &PayType=Postpaid
```

正常返回示例云原生数据库 I参考 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "RequestId":"9B7BFB11-C077-4FE3-B051-F69CEB******",
 "DBInstanceId":"POLARDB-cn-**************",
 "Port":"1521",
 "OrderId":"2035638*******",
 "ConnectionString":"abc.polardb.rds.aliyuncs.com"
}
```

`XML` 格式

```xml
<RequestId>9B7BFB11-C077-4FE3-B051-F69CEB******</RequestId> <DBInstanceId>POLARDB-cn-**************</DBInstanceId> <Port>1521</Port> <OrderId>2035638*******</OrderId> <ConnectionString>abc.polardb.rds.aliyuncs.com</ConnectionString>
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidIzNo.NotSup ported | InvalidZoneId.NotSupported | The Specified vpc Zone not supported. |
| 400 | InvalidZone.NotSup ported | InvalidZone.NotSupported | The Specified Zone not supported. |
| 500 | InsufficientResourc eCapacity | InsufficientResourceCapacity | %s |
| 500 | IncorrectEngineVer sion | IncorrectEngineVersion | Current DB instance engine version does not support this operation. |
| 500 | InvalidCpuType | InvalidCpuType | Specified parameter CpuType is not valid. |
| 500 | InvalidDBInstanceS torage.Format | InvalidDBInstanceStorage.For mat | The specified DBInstanceStorage is invalid. |
| 500 | VPC CLOUD INSTA _ _ NCEIP USED _ | VPC CLOUD INSTANCEIP USE _ _ _ D | the vpc cloudinstanceIp is use. |
| 500 | SUBNET IP EXHAU _ _ STED | SUBNET IP EXHAUSTED _ _ | error subnet ip exhaust |
| 400 | UnsupportedTdeEn ableOnInstanceCre ation | UnsupportedTdeEnableOnInsta nceCreation | The Specified TDE is not supported |
| 400 | SpecifiedMinorVersi onProcessFailed | SpecifiedMinorVersionProcessF ailed | Specified minor version process failed. |

云原生数据库 I参考

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

云原生数据库 I参考重启实例一般在10s钟内完成。 如果当时有大量的事务需要提交或回滚，可能会延长1分钟左右。 操作必须满足以下条件，否则操作将失败： 实例使用中。 实例没有进行中的备份。

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

#### 查看实例属性

**描述**

查看指定实例的详细属性。

**请求参数**

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| Action | String | 是 | 系统规定参数，取值：DescribeDBInstanceAttribute。 |

云原生数据库 I参考

| DBInstanc eId | String | 是 | 实例ID，可以一次输入多个，以英文半角“,”分隔；最多传入30个。 |
|---|---|---|---|

**返回参数**

| 参数 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Items |  |  | DBInstanceAttribute的参数。 |
| └DBInstanceId | String | rm-bpvxxxxx | 实例ID。 |
| └DBInstanceType | String | Primary | 实例类型。取值范围： Primary：表示主实例。 Readonly：表示只读实例。 Guard：表示灾备实例。 Temp：表示临时实例。 |
| └Category | String | Basic | 实例系列。取值范围： Basic：表示基础版。 Standard：表示高可用版。 Enterprise：表示金融版。 |
| └InstanceNetwor kType | String | Classic | 实例的网络类型。取值范围： Classic：表示经典网络。 VPC：表示VPC网络。 |
| └RegionId | String | cn-hangzhou | 地域的ID。 |
| └ZoneId | String | cn-hangzhou-a | 可用区的ID。 |
| └ConnectionStrin g | String | polardb- xxxxx.mysql.pol ardb.aliyuncs.co m | 连接地址。 |
| └Port | String | 3306 | 应用访问端口。 |
| └Engine | String | MySQL | 数据库类型。 |
| └EngineVersion | String | 5.5 | 数据库版本。 |

云原生数据库 I参考

| └DBInstanceClas sType | String | s | 实例规格族。取值范围： s：表示共享型。 x：表示通用型。 d：表示独享型。 h：表示独占物理机。 |
|---|---|---|---|
| └DBInstanceClas s | String | polardb.mys2.s mall | 实例规格。 |
| └DBInstanceMem ory | Long | 240 | 实例内存，单位为MB。 |
| └DBInstanceStor age | Integer | 10 | 实例存储空间，单位为GB。 |
| └DBInstanceNetT ype | String | Internet | 实例的网络连接类型。取值范围： Internet：表示外网。 Intranet：表示内网。 |
| └DBInstanceStat us | String | Running | 实例状态，详见实例状态表。 |
| └DBInstanceDesc ription | String | 测试实例 | 实例描述或备注。 |
| └LockMode | String | Unlock | 实例锁定状态。取值范围： Unlock：表示正常。 ManualLock：表示手动触发锁定。 LockByExpiration：表示实例过期自动锁定。 LockByRestoration：表示实例回滚前的自动锁定。 LockByDiskQuota：表示实例空间满自动锁定。 |
| └LockReason | String | 无 | 被锁定的原因。 |
| └DBMaxQuantity | Integer | 200 | 一个实例下最多可以创建的数据库数量。 |
| └AccountMaxQua ntity | Integer | 50 | 一个实例下最多可以创建的账号数量。 |

云原生数据库 I参考

| └CreationTime | String | 2011-05- 30T12:11:4Z | 创建时间格式为： YYYY-MM-DD’T’hh:mm:ssZ 2011-05-30T12:11:4Z |
|---|---|---|---|
| └ExpireTime | String | 无 | 到期时间，按量付费实例无到期时间。 |
| └MaintainTime | String | 00:00Z-02:00Z | 实例可维护时间，如表示0点到2点可进行例行维护。 00:00Z-02:00Z |
| └AvailabilityValu e | String | 100.0% | 查询当前实例的可用性状态，单位为百分比。 |
| └MaxIOPS | Integer | 150 | 最大I/O请求次数，即IOPS。 |
| └MaxConnection s | Integer | 60 | 实例最大并发连接数。 |
| └MasterInstanceI d | String | null | 主实例的ID，如果没有返回此参数（即为null）则表示该实例是主实例。 |
| └IncrementSourc eDBInstanceId | String | null | 增量数据来源的实例ID，如灾备实例的增量数据来源是主实例，只读实例的增量数据来源是主实例， 主实例的增量数据来源是NULL。 |
| └GuardDBInstanc eId | String | 无 | 该实例如果挂载着灾备实例，即为灾备实例的ID。 |
| └TempDBInstanc eId | String | 无 | 该实例如果挂载着临时实例，即为临时实例的ID。 |
| └ReadOnlyDBInst anceIds |  | rr-xxxxx | 主实例下挂载的只读实例的ID列表。 |
| └DBInstanceId | String | rm-bpxxxxx | 实例的名称。 |
| └VpcCloudInstan ceId | String | vpc-xxxxx | 专有网络实例的ID。 |

云原生数据库 I参考

| └ResourceGroupI d | String | 3653788125 | 资源组ID。 |
|---|---|---|---|
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

JSON格式： 云原生数据库 I参考

```json
{ "Items":
    { "DBInstanceAttribute":
        [ { "LockMode": "Unlock",
            "ConnectionString": "polardb-xxxxx.mysql.polardb.aliyuncs.com",
            "CreationTime": "2024-07-13T10:28:48Z",
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
            "DBInstanceId": "polardbfnjfquxxxxx",
            "PayType": "Postpaid",
            "ExpireTime": "",
            "MaintainTime": "",
            "DBInstanceClass": "polardb.mys2.small",
            "SecurityIPList": "11.11.11.11",
            "Port": "3306" } ] },
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

云原生数据库 I参考

| 参数 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeDBInsta nces | 系统规定参数。取值： DescribeDBInsta nces |
| RegionId | String | 是 | cn-hangzhou | 地域的ID。 |
| ConnectionMode | String | 否 | Performance | 实例的访问模式。 取值范围： Performance： 表示标准访问模式。 Safty：表示高安全访问模式。 若不填，默认返回所有。 |
| DBInstanceType | String | 否 | Primary | 实例类型。取值范围： Primary：表示主实例。 Readonly：表示只读实例。 Guard：表示灾备实例。 Temp：表示临时实例。 若不填，默认返回所有。 |
| InstanceNetwork Type | String | 否 | Classic | 实例的网络类型。 取值范围： VPC：表示VPC 网络。 Classic：表示经典网络。 若不填，默认返回所有。 |
| PageNumber | Integer | 否 | 1 | 页码。大于0且不超过Integer的最大值，默认值：1。 |
| PageSize | Integer | 否 | 30 | 每页记录数。取值：30/50/100， 默认值：30。 |

云原生数据库 I参考

| Tags | String | 否 | {“key1”:”value1” } | 查询绑定有该标签的实例。传入值格式为JSON string， 包括TagKey和 TagValue，TagKe y不能为空，TagValue可以为空。格式示例： {“key1”:”value1 ”}。 |
|---|---|---|---|---|

**返回参数**

| 参数 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| PageNumber | Integer | 1 | 页码。 |
| TotalRecordCount | Integer | 1 | 总记录数。 |
| PageRecordCount | Integer | 1 | 本页实例个数。 |
| Items |  |  | 由实例组成的数组。 |
| └DBInstanceId | String | rm-xxxxx | 实例ID。 |
| └DBInstanceDescriptio n | String | testforRemarks | 实例描述。 |
| └PayType | String | Postpaid | 计费方式。取值范围： Postpaid：表示按时付费 Prepaid：表示包年包月 |
| └DBInstanceType | String | Primary | 实例类型。取值范围： Primary：表示主实例 ReadOnly：表示只读实例 Guard：表示灾备实例 Temp：表示临时实例 |

云原生数据库 I参考

| └InstanceNetworkType | String | Classic | 实例的网络类型。取值范围： Classic：表示经典网络 VPC：表示VPC网络 |
|---|---|---|---|
| └ConnectionMode | String | Performance | 访问模式。取值范围： Performance：表示标准访问模式 Safty：表示高安全访问模式 |
| └RegionId | String | cn-hangzhou | 地域的ID。 |
| └ExpireTime | String | 无 | 到期时间，按量付费实例无到期时间。 |
| └DBInstanceStatus | String | Intranet | 实例状态，详见实例状态表。 |
| └Engine | String | MySQL | 数据库类型。 |
| └DBInstanceNetType | String | Internet | 实例的网络连接类型。取值范围： Internet：表示外网 Intranet：表示内网 |
| └LockMode | String | Unlock | 实例的锁定状态。取值范围： Unlock：表示正常。 ManualLock：表示手动触发锁定。 LockByExpiration： 表示实例过期自动锁定。 LockByRestoration ：表示实例回滚前的自动锁定。 LockByDiskQuota： 表示实例空间满自动。 |
| └LockReason | String | 无 | 被锁定的原因。 |

云原生数据库 I参考

| └MasterInstanceId | String | null | 主实例的ID，如果没有返回此参数（即为null）则表示该实例是主实例。 |
|---|---|---|---|
| └GuardDBInstanceId | String | 无 | 该实例如果挂载着灾备实例，即为灾备实例的ID。 |
| └TempDBInstanceId | String | 无 | 该实例如果挂载着临时实例，即为临时实例的ID。 |
| └VpcCloudInstanceId | String | vpc-xxxxx | 专有网络实例的ID。 |
| └ReadOnlyDBInstanceI ds |  |  | 无 |
| └DBInstanceId | String | rm-xxxxx | 实例ID。 |
| hostInfos | Array | 无 | 节点信息列表。 |
| └role | String | 0 | 节点角色。取值范围： 0：主节点。 1：备节点。 |
| └ip | String | 30** | 节点IP。 |
| └port | String | 10.XX.XX.14 | 节点实际端口。 |
| RequestId | String | 1AD222E9-E606-4A42- BF6D-8A4442913CEF | 请求ID。 |

**示例**

**请求示例**

```
https://polardb.example.com/?Action=DescribeDBInstances &RegionId=cn-hangzhou &Engine=MySQL
```

**正常返回示例**

XML格式： 云原生数据库 I参考

```xml
<DescribeDBInstancesResponse> <PageRecordCount>2</PageRecordCount> <Items> <DBInstance> <DBInstanceDescription>testforRemarks</DBInstanceDescription> <ExpireTime>2014-10-10T16:00:00Z</ExpireTime> <DBInstanceId>polardbmjfirxxxxx</DBInstanceId> <DBInstanceNetType>Internet</DBInstanceNetType> <PayType>Prepaid</PayType> <DBInstanceStatus>Running</DBInstanceStatus> <DBInstanceType>Primary</DBInstanceType> <Engine>MySQL</Engine> <LockMode>Unlock</LockMode> <LockReason/> <RegionId>cn-hangzhou</RegionId> <ZoneId>cn-hangzhou-a</ZoneId> <MasterInstanceId/> <GuardDBInstanceId/> <TempDBInstanceId/> <ReadOnlyDBInstanceIds> <ReadOnlyDBInstanceId/> </ReadOnlyDBInstanceIds> </DBInstance> </Items> <PageNumber>1</PageNumber> <TotalRecordCount>2</TotalRecordCount> <RequestId>2553A660-E4EB-4AF4-A402-8AFF70A49143</RequestId> </DescribeDBInstancesResponse>
```

JSON格式： 云原生数据库 I参考

```json
{ "Items":
    { "DBInstance":
        [ { "DBInstanceDescription":"testforRemarks",
            "DBInstanceId":"polardbmjfirxxxxx",
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

云原生数据库 I参考

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

云原生数据库 I参考

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

云原生数据库 I参考

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

云原生数据库 I参考

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

云原生数据库 I参考

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

云原生数据库 I参考

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

云原生数据库 I参考

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

云原生数据库 I参考

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

云原生数据库 I参考

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

云原生数据库 I参考 XML格式：

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

云原生数据库 I参考

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

云原生数据库 I参考

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

支持将一个实例迁移至其他可用区。 例如实例1目前位于华东 1 （杭州）的cn-hangzhou-a的可用区，调用此接口可以将该实例迁移至杭州的 cn-hangzhou-b。 云原生数据库 I参考

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

云原生数据库 I参考

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

#### 升级PolarDB实例版本

**描述**

针对实例进行数据库版本升级，如将数据库版本从MySQL5.1升级至MySQL5.5。 如果主实例下挂载着只读实例或者灾备实例，请先升级只读实例或者灾备实例的数据库版本。 操作必须满足以下条件，否则操作将失败： 实例为运行中。 输入的数据库版本号必须大于当前实例的版本号。

**请求参数**

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| Action | String | 是 | 系统规定参数，取值： UpgradeDBInstanceEn gineVersion。 |

云原生数据库 I参考

| DBInstanceId | String | 是 | 待升降级的实例。 |
|---|---|---|---|
| EngineVersion | String | 是 | 待升级到的数据库版本。 |

**返回参数**

| 名称 | 类型 | 描述 |
|---|---|---|
| <公共返回参数> |  | 公共返回参数，具体请参见公共返回参数 。 |
| TaskId | Integer | 任务ID。 |

**示例**

**请求参数**

```
https://polardb.example.com/?Action=UpgradeDBInstanceEngineVersion DBInstanceId=rm-xxxxxx &EngineVersion=5.6
```

**返回参数**

XML格式：

```xml
<UpgradeDBInstanceEngineVersionResponse> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> <TaskId>124378</Taskid> </UpgradeDBInstanceEngineVersionResponse>
```

JSON格式：

```json
{"RequestId": "1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC", "TaskId":”124378” }
```

#### 修改PolarDB实例备注

**描述**

修改实例的备注名，用于方便用户记录该实例，比如为该实例修改备注名为阿里云测试环境实例。

**请求参数**

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| Action | Strin g | 是 | 系统规定参数，取值：ModifyDBInstanceDescription。 |

云原生数据库 I参考

| DBInstanceId | Strin g | 是 | 实例ID。 |
|---|---|---|---|
| DBInstanceDesc ription | Stin g | 是 | 实例描述信息。 |

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

云原生数据库 I参考

| MaintainTim e | String | 是 | 实例的维护时间，取值范围如下： 22:00Z-02:00Z：22点至凌晨2点。 02:00Z-06:00Z：凌晨2点至6点。 06:00-10:00：6点至10点。 10:00Z14:00Z：10点至14点。 14:00Z-18:00Z：14点至18点。 18:00Z-22:00Z：18点至22点。 |
|---|---|---|---|

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

云原生数据库 I参考

| HAMode | String | 是 | RPO：数据持久性优先；RTO：实例可用性优先。 |
|---|---|---|---|

**返回参数**

#### 切换PolarDB实例的主备库

**描述**

PolarDB主实例是由分布在不同服务器上面的主库和备库组成的。可以通过API进行主备库切换，并由新的主库来承担业务流量。

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

为某个实例创建一个只读实例实例状态要求：必须满足以下条件，否则将创建失败。 主实例状态为使用中，且未处于容灾切换状态。 只读实例与主实例必须处于相同的region。 一个PolarDB实例，最多只能有5个只读实例。

**请求参数**

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|

云原生数据库 I参考

| Action | String | 是 | 系统规定参数，取值：CreateReadOnlyDBInstance。 |
|---|---|---|---|
| RegionId | String | 是 | 数据中心，长度不超过50个字符；通过函数DescribeRegions查看可用的数据中心。 |
| ZoneId | String | 是 | 可用区id，通过函数DescribeRegions查看可用的可用区。 |
| DBInstanceId | String | 是 | 主实例ID。 |
| EngineVersion | String | 是 | 数据库版本号。必须与主实例相同。取值： 5.6 5.7 |
| DBInstanceClass | String | 是 | 实例规格。详情请参见。 |
| DBInstanceStora ge | Intege r | 是 | 自定义存储空间，取值范围：[5,1000]。每5G进行递增。单位： GB。 |
| DBInstanceDesc ription | String | 否 | 实例的描述或备注信息，不超过256个字节；注：不能以http:// , https:// 开头。以中文、英文字母开头。可以包含中文、英文字符、 ” ”，” -”，数字字符长度2~256。 _ |
| ClientToken | String | 是 | 用于保证幂等性。 |
| InstanceNetwork Type | String | 否 | VPC：创建VPC实例；Classic：创建Classic实例；不填，默认创建 Classic实例。 |
| VPCId | String | 否 | VPC ID。 |
| VSwitchId | String | 否 | VSwitch ID。 |
| PrivateIpAddress | String | 否 | 用户可以指定VSwitchId下的vpcIp，如果不输入，系统通过vpcId,和 VSwitchId 自动分配。 |

**返回参数**

| 名称 | 类型 | 描述 |
|---|---|---|
| <公共返回参数> | - | 公共返回参数，具体请参见公共返回参数。 |
| DBInstanceId | String | 实例ID。 |

云原生数据库 I参考

| OrderId | String | 订单ID。 |
|---|---|---|
| ConnectionStrin g | String | 数据库连接地址。 |
| Port | String | 数据库连接端口。 |

**示例**

**请求示例**

```
https://polardb.example.com/?Action=CreateReadOnlyDBInstance &RegionId=cn-hangzhou &ZoneId=cn-hangzhou-b &DBInstanceId=polardb-xxxxx &EngineVersion=5.6 &DBInstanceClass=polardb.mys2.small &DBInstanceStorage=10 &PayType=Postpaid &ClientToken=ETnLKxxxxx
```

**返回示例**

XML格式：

```xml
<CreateDBInstanceResponse> <OrderId>10078937xxxxx</OrderId> <ConnectionString>polardb-xxxxx.mysql.polardb.aliyuncs.com </ConnectionString> <DBInstanceId>polardb-xxxxx</DBInstanceId> <port>3306</port> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> </CreateDBInstanceResponse>
```

JSON格式：

```json
{ "OrderId": "100789370230206", "ConnectionString": "polardb-xxxxx.mysql.polardb.aliyuncs.com", "DBInstanceId": "polardb-xxxxx", "Port": "3306", "RequestId": "1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC" }
```

#### 查询实例SSL链路

**描述**

调用该接口查询PolarDB实例的SSL链路。

**请求参数**

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|

云原生数据库 I参考

| Action | String | 是 | 系统规定参数，取值：DescribeDBInstanceSSL。 |
|---|---|---|---|
| DBInstanceId | String | 是 | 实例ID。 |

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

云原生数据库 I参考

| <公共返回参数> | - | 公共返回参数，具体请参见公共返回参数。 |
|---|---|---|
| SSLExpireTime | String | SSL过期的时间，格式为YYYY-MM-DD’T’hh:mm:ssZ。 |

#### 查询实例数据加密状态

调用DescribeDBInstanceTDE查询PolarDB数据库实例的透明数据加密（TDE）配置。

**请求头**

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Action | Strin g | Query | 否 | DescribeDBInstanceTDE | 系统规定参数。取值： DescribeDBInstanceTDE 。 |
| DBInstanc eId | Strin g | Query | 是 | pc-**************** | 实例ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Databases | Array | [{"name":"test"}] | 查询到的数据库列表。 |
| -DBName | String | test db _ | 数据库名称。 |
| -TDEStatus | String | Enabled | 是否开通TDE加密，取值： Enabled ：开通 Disabled ：关闭 |
| RequestId | String | 9B7BFB11-C077- 4FE3-B051- F69CEB****** | 请求ID。 |

云原生数据库 I参考

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| EncryptAlgorit hm | String | AES 256 CBC _ _ | 加密算法： AUTO ：自动加密。 TKIP ：临时密钥完整性协议。 AES 256 CBC ：AES-256-CBC 是一种 _ _ 采用 256 位长密钥的高强度对称加密算法， 它通过将数据分块并结合前一个密文块进行链式异或运算（需配合随机初始化向量），有效隐藏数据模式以抵御攻击，从而提供极高的安全性。 SM4 ：是一种采用 128 位密钥和分组长度的对称加密算法。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeDBInstanceTDE &DBInstanceId=pc-****************
```

正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "TDEStatus":"Enabled",
 "Databases":[
  {
   "TDEStatus":"Enabled",
   "DBName":"test_db"
  }
```

`],`

```json
 "RequestId":"9B7BFB11-C077-4FE3-B051-F69CEB******",
 "EncryptAlgorithm":"AES"
}
```

`XML` 格式

```xml
<TDEStatus>Enabled</TDEStatus> <Databases>
 <TDEStatus>Enabled</TDEStatus>
 <DBName>test_db</DBName>
</Databases> <RequestId>9B7BFB11-C077-4FE3-B051-F69CEB******</RequestId> <EncryptAlgorithm>AES</EncryptAlgorithm>
```

#### 修改实例数据加密状态

云原生数据库 I参考

**描述**

调用该接口修改PolarDB实例的数据加密状态。

**请求参数**

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

云原生数据库 I参考

| DBInstanceI d | String | 是 | 实例ID。 |
|---|---|---|---|
| DBName | String | 是 | 数据库名，需惟一性检查，由小写字母，数字、下划线组成，字母开头， 长度不超过64个字符。其他非法字符，详见禁用关键字表。 |
| CharacterSet Name | String | 是 | 字符集，取值范围限定如下字符集： MySQL类型：utf8、gbk、latin1、utf8mb4 SQL Server类型：Chinese PRC CI AS、 _ _ _ Chinese PRC CS AS、SQL Latin1 General CP1 CI AS、 _ _ _ _ _ _ _ _ SQL Latin1 General CP1 CS AS、Chinese PRC BIN _ _ _ _ _ _ _ |
| DBDescriptio n | String | 否 | 数据库描述，不超过256个字符；注：不能以http：// , https:// 开头。以中文、英文字母开头。 可以包含中文、英文字符、” ”，” -”，数字字符长度2~256。 _ |

**返回参数**

**示例**

**请求示例**

```
https://polardb.example.com/?Action=CreateDatabase &CharacterSetName=gbk &DBName=testDB &DBInstanceId=polardb-xxxxx
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

用户可以删除实例下的的某个数据库。 接口必须满足以下条件，否则将调用失败： 云原生数据库 I参考实例状态运行中。 实例类型为主实例。

**说明**

PolarDB实例中用户有权限通过SQL做DROP DATABASE操作，因此接口不支持PolarDB。

**请求参数**

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

云原生数据库 I参考查找指定实例、指定DB的DB列表信息。如果查找参数类型错误，返回错误提示，返回数据为空。

**请求参数**

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| Action | String | 是 | 系统规定参数，取值：DescribeDatabases。 |
| DBInsta nceId | String | 是 | 实例ID。 |
| DBName | String | 否 | 数据库名称。 |
| DBStatu s | String | 否 | 数据库状态，取值范围Creating：创建中；Running：使用中；Deleting：删除中。 |

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
| DBStatus | String | 数据库状态Creating：创建中；Running：使用中；Deleting：删除中。 |
| CharacterSet Name | String | 字符集。 |
| DBDescription | String | 数据库描述。 |

云原生数据库 I参考

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
<DescribeDatabasesResponse> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> <Databases> <Database> <Engine>MySQL</Engine> <DBName>testdb</DBName> <CharacterSetName>utf8</CharacterSetName> <DBStatus>Creating</DBStatus> <DBInstanceId>polardb-xxxxx</DBInstanceId> <Accounts> <AccountPrivilegeInfo></AccountPrivilegeInfo> <Accounts> </Database> </Databases> </DescribeDatabasesResponse>
```

JSON格式： 云原生数据库 I参考

```json
{ "RequestId": "1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC", "Databases":
    { "Database":
        [ { "Engine": "MySQL",
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

XML格式： 云原生数据库 I参考

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

云原生数据库 I参考

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

云原生数据库 I参考

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

DBInstanceAccount参数云原生数据库 I参考

| 名称 | 类型 | 描述 |
|---|---|---|
| DBInstanceId | String | 账号所属实例ID。 |
| AccountName | String | DB操作账号名称。 |
| AccountStatus | String | 账号状态，Unavailable:不可用；Available:可用。 |
| AccountDescription | String | 账号备注信息。 |
| DatabasePrivileges | List<DatabasePrivil ege> | 由DatabasePrivilege组成的数组。 |
| AccountType | String | 取值为：Normal（普通账号）， Super（超级账号）。 |

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

XML格式： 云原生数据库 I参考

```xml
<DescribeAccountsResponse> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> <Accounts> <DBInstanceAccount> <AccountName>MySQL</AccountName> <DBInstanceId>testdb</DBInstanceId> <AccountStatus>utf8</AccountStatus> <AccountDescription> </AccountDescription> <DatabasePrivileges> <DatabasePrivilege></DatabasePrivilege> </DatabasePrivileges> <DBInstanceAccount> </Accounts> </DescribeAccountsResponse>
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

云原生数据库 I参考

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

云原生数据库 I参考

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

云原生数据库 I参考

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

云原生数据库 I参考

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

云原生数据库 I参考

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

云原生数据库 I参考

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

云原生数据库 I参考

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

云原生数据库 I参考

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

云原生数据库 I参考

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

云原生数据库 I参考

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

云原生数据库 I参考

| PreferredBackupPeri od | String | 数据备份周期：Monday：周一；Tuesday：周二；Wednesday：周三；Thursday：周四；Friday：周五；Saturday：周六；Sunday：周日。 |
|---|---|---|
| BackupLog | String | 日志备份状态，Enable：开启，Disabled：关闭。 |
| LogBackupRetention Period | String | 日志备份保留天数（1~30天）。 |

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
| LogBackupRetention Period | String | 否 | 日志备份保留天数（1~30天，且不大于数据备份保留天数）。 当开启日志备份时，可设置日志备份文件的保留天数，目前仅支持 MySQL/ PolarDB PostgreSQL/ PolarDB PPAS引擎设置该值。 _ _ |

**返回参数**

云原生数据库 I参考

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

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| Action | String | 是 | 系统规定参数，取值： RestoreDBInstance。 |
| DBInstanceId | String | 是 | 实例ID。 |

云原生数据库 I参考

| BackupId | Integer | 是 | 备份集ID。 |
|---|---|---|---|

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

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| Action | String | 是 | 系统规定参数，取值：DeleteBackup。 |
| DBInstanc eId | String | 是 | 实例ID。 |

云原生数据库 I参考

| BackupId | String | 是 | 备份集ID，可通过查看备份列表获取。支持传入多组值，以逗号隔开，单次最多传入100个。只支持删除查看备份列表中存储状态为Enable的备份集。 |
|---|---|---|---|

**返回参数**

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
| LogSize | Integer | 日志占用空间，单位：Byte，-1表示没有数据。 |
| BackupSize | Integer | 备份占用空间，单位：Byte，-1表示没有数据。 |
| ColdBackupSize | Integer | 冷备的存储量，单位：Byte，-1表示没有数据。 |
| SQLSize | Integer | SQL的存储量，单位：Byte，-1表示没有数据。 |

#### 查看实例性能数据

**描述**

云原生数据库 I参考根据性能参数查看某个用户实例，某时间段范围内的性能监控数据。 根据查询时间范围的不同，有如下3种输出形式： 当查询时间范围小于等于1天，按分钟描点性能值。 当查询时间范围1天到7天不支持，暂不支持。 当查询时间范围大于7天小于等于15天，按小时描点性能值。 当查询时间范围大于15天小于30天，暂不支持。 当查询时间范围大于等于30天小于等于1年时，按天描点。

**说明**

实例空间占用Key为MySQL_SpaceUsage，仅支持查询1天内的监控数据，即第1种输出形式。

**请求参数**

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| Action | String | 是 | 系统规定参数，取值：DescribeDBInstancePerformance。 |
| DBInstan ceId | String | 是 | 实例ID。 |
| Key | Integ er | 是 | 性能指标，多个用英文半角“,”分隔，请参见性能参数表。 |
| StartTime | String | 是 | 查询开始时间，格式如：2012-06-11T15:00Z。 |
| EndTime | String | 是 | 查询结束时间，格式如：2012-06-11T15:00Z。 |

**返回参数**

| 名称 | 类型 | 描述 |
|---|---|---|
| <公共返回参数> | - | 公共返回参数，具体请参见公共返回参数。 |
| DBInstanceId | String | 实例ID。 |
| Engine | String | 数据库类型。 |
| StartTime | String | 查询开始时间，格式：YYYY-MM-DD'T'HH:mmZ，如 2011-05-30T03:29Z。 |

云原生数据库 I参考

| EndTime | String | 查询结束时间，格式：YYYY-MM-DD'T'HH:mmZ，如 2011-05-30T03:29Z，大于查询开始时间。 |
|---|---|---|
| PerformanceKey s | List<PerformanceKey> | 数组格式：{perf1, perf2, perf3, …}。 |

**示例**

**请求示例**

```
https://polardb.example.com/?Action=DescribeDBInstancePerformance &DBInstanceId=polardb-xxxxx &key= MySQL_xxxxx &StartTime=2013-01-11T15:00:00Z &EndTime=2013-06-05T15:00:00Z
```

**返回示例**

XML格式：

```xml
<DescribeDBInstancePerformanceResponse> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> <DBInstanceID>polardb-xxxxx</DBInstanceID> <StartTime>2013-01-11T15:00:00Z</StartTime> <EndTime>2013-10-17T15:00Z</EndTime> <Engine>MySQL</Engine> <PerformanceKeys> <PerformanceKey> <Key>MySQL_xxxxx</Key> <Unit>KB</Unit> <ValueFormat>recv_k&amp;sent_k</ValueFormat> <Values><Values/> </PerformanceKey> </PerformanceKeys> </DescribeDBInstancePerformanceResponse>
```

JSON格式：

```json
{ “RequestId”1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC, "DBInstanceID": polardb-xxxxx, "StartTime": "2012-06-11T15:00Z", "EndTime": "2013-10-17T15:00Z", "Engine": "MySQL", "PerformanceKeys":
    { PerformanceKey[ {
        "Key": "MySQL_xxxxx",
        "Unit": "KB",
        "ValueFormat": "recv_k&sent_k",
        "Values": { "PerformanceValue":[] } } ] }}
```

#### 查询监控行为

云原生数据库 I参考

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

| 名称 | 类型 | 描述 |
|---|---|---|
| <公共返回参数> | - | 公共返回参数，具体请参见公共返回参数。 |

### 参数管理

#### 查询参数模板列表

查看目标地域的参数模板列表。

**请求头**

**请求参数**

云原生数据库 I参考

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| AccessKey Id | Strin g | Query | 否 | LTAI4G28PhwnizaSC**** **** | 访问密钥ID。 |
| Action | Strin g | Query | 否 | DescribeParameterGrou ps | 系统规定参数。取值： DescribeParameterGrou ps。 |
| OwnerId | Long | Query | 否 | 123456**** | 鉴权相关的系统参数，无需填写。 |
| Resource OwnerAcc ount | Strin g | Query | 否 | test | 鉴权相关的系统参数，无需填写。 |
| Resource OwnerId | Long | Query | 否 | 34567891**** | 鉴权相关的系统参数，无需填写。 |
| RegionId | Strin g | Query | 是 | cn-hangzhou | 地域ID。 |
| EngineVer sion | Strin g | Query | 否 | 8.0 | 数据库版本号。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |  |  |
|---|---|---|---|---|---|
| ParameterGro ups | Array | group1 | 参数模板列表。 |  |  |
| - ParameterGro upType | Integer | 1 | 参数模板类型。返回值如下： 0 ：系统默认模板 1 ：用户自定义模板 2 ：系统自动备份模板（应用模板后系统会自动备份之前的参数设置为模板） |  |  |
| -Created | String | 0 | 参数模板创建时间，格式为 yyyy-MM- ddTHH:mm:ssZ （UTC时间）。 |  |  |
|  |  |  |  | yyyy-MM- |  |
| -Modified | String | 19723574**** | 修改时间。 |  |  |
| - ParameterGro upName | String | test | 参数模板名称。 |  |  |
| -ParamCounts | Integer | 2 | 参数模板内的参数数量。 |  |  |

|  | ddTHH:mm:ssZ |
|---|---|

| 云原生数据库 |  |  | PolarDB MySQL主备版开发指南·A |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| - ParameterGro upDesc | String | testgroup | 参数模板描述。 |
| -ForceRestart | Integer | 1 | 应用该参数模板是否需要重启集群。返回值如下： 0 ：不需要重启 1 ：需要重启 |
| -Engine | String | polardb mysql _ | 数据库引擎类型。 |
| -EngineVersion | String | 8.0 | 数据库引擎版本号。 |
| - ParamGroupId | String | rpg-sys- 01040401010200 | 参数模板ID。 |
| - ParameterGro upId | Integer | 1 | 参数模板ID。 |
| RequestId | String | 9B7BFB11-C077- 4FE3-B051- F69CEB****** | 请求ID。 |
| SignalForOpti mizeParams | Boolean | false | 目标地域是否有参数模板。返回值如下： true ：无参数模板 false ：有参数模板该参数已废弃，不建议使用。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeParameterGroups &RegionId=cn-hangzhou
```

正常返回示例 `JSON` 格式云原生数据库 I参考

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "ParameterGroups":[
  {
   "Modified":"19723574****",
   "EngineVersion":"8.0",
   "ParameterGroupId":1,
   "ParameterGroupName":"test",
   "ForceRestart":1,
   "ParameterGroupType":1,
   "ParamCounts":2,
   "ParameterGroupDesc":"testgroup",
   "Engine":"polardb_mysql",
   "ParamGroupId":"rpg-sys-01040401010200",
   "Created":"0"
  }
```

`],`

```json
 "RequestId":"9B7BFB11-C077-4FE3-B051-F69CEB******",
 "SignalForOptimizeParams":false
}
```

`XML` 格式

```xml
<ParameterGroups>
  <Modified>19723574****</Modified>
  <EngineVersion>8.0</EngineVersion>
  <ParameterGroupId>1</ParameterGroupId>
  <ParameterGroupName>test</ParameterGroupName>
  <ForceRestart>1</ForceRestart>
  <ParameterGroupType>1</ParameterGroupType>
  <ParamCounts>2</ParamCounts>
  <ParameterGroupDesc>testgroup</ParameterGroupDesc>
  <Engine>polardb_mysql</Engine>
  <ParamGroupId>rpg-sys-01040401010200</ParamGroupId>
  <Created>0</Created>
</ParameterGroups> <RequestId>9B7BFB11-C077-4FE3-B051-F69CEB******</RequestId> <SignalForOptimizeParams>false</SignalForOptimizeParams>
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidRegionId.Mal formed | InvalidRegionId.Malformed | The specified parameter RegionId is not valid. |

#### 查看数据库参数模板

**描述**

云原生数据库 I参考该接口返回参数模板列表，包含内容：参数名，参数默认值，是否可修改，是否需要重启才能生效，参数校验规则（正则表达式）。

**请求参数**

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| Action | Strin g | 是 | 系统规定参数，取值：DescribeParameterTemplates。 |
| Engine | Strin g | 是 | 数据库类型，取值： mysql。 PolarDB PG。 _ PolarDB PPAS。 _ |
| EngineVer sion | Strin g | 是 | 数据库版本，取值： MySQL数据库：5.6、8.0。 PolarDB PG数据库：14。 _ PolarDB PPAS数据库：14。 _ |

**返回参数**

| 名称 | 类型 | 描述 |
|---|---|---|
| <公共返回参数> | - | 公共返回参数，具体请参见公共返回参数。 |
| Engine | String | 数据库类型。 |
| EngineVersion | String | 数据库版本号。 |
| ParameterCount | Integer | 参数个数。 |
| Parameters | List<TemplateRecord > | 参数列表，格式：{parameter1, parameter2, parameter3, …}。 |

**示例**

**请求示例**

```
https://polardb.example.com/?Action=DescribeParameterTemplates &Engine=MySQL &EngineVersion=5.6
```

云原生数据库 I参考

**返回示例**

XML格式：

```xml
<DescribeParameterTemplatesResponse> <Engine>mysql</Engine> <EngineVersion>5.6</EngineVersion> <ParameterCount>1</ParameterCount> <Parameters> <TemplateRecord> <CheckingCode>[0-100]</CheckingCode> <ForceRestart>True</ForceRestart> <Factor>1</Factor> <ParameterDescription>test</ParameterDescription> <ParameterName>fill factor</ParameterName> <ParameterValue>0</ParameterValue> <ForceModify>True</ForceModify> <Unit>INT</Unit> </TemplateRecord> </Parameters> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> </DescribeParameterTemplatesResponse>
```

JSON格式：

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

#### 查看当前实例数据库参数运行列表

**描述**

该接口返回用户某个实例当前的参数配置。

**请求参数**

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| Action | String | 是 | 系统规定参数，取值：DescribeParameters。 |

云原生数据库 I参考

| DBInstanceId | String | 是 | 实例ID。 |
|---|---|---|---|

**返回参数**

| 名称 | 类型 | 描述 |
|---|---|---|
| <公共返回参数> | - | 公共返回参数，具体请参见公共返回参数。 |
| Engine | String | 数据库类型。 |
| EngineVersion | String | 数据库版本号。 |
| RunningParameters | List<DBInstanceParameter> | 当前运行的参数列表，格式为 {parameter1,parameter2,param eter3, …}。 |
| ConfigParameters | List<DBInstanceParameter> | 正在同步的参数列表，格式为 {parameter1,parameter2,param eter3,…}。 |

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

**返回示例**

XML格式： 云原生数据库 I参考

```xml
<DescribeParametersResponse> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> <Engine>mysql</Engine > <EngineVersion>5.6</EngineVersion> <RunningParameters> <DBInstanceParameter> <ParameterDescription>test</ParameterDescription> <ParameterName>fill factor</ParameterName> <ParameterValue>0</ParameterValue> </DBInstanceParameter> </RunningParameters> <ConfigParameters> <DBInstanceParameter> <ParameterDescription>test1</ParameterDescription> <ParameterName>fill factor</ParameterName> <ParameterValue>50</ParameterValue> </DBInstanceParameter> </ConfigParameters> </DescribeParametersResponse>
```

JSON格式：

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

#### 修改数据库参数列表

**描述**

用户可以修改实例参数，提交请求后，PolarDB将下达任务，新修改的参数应用到实例。如果所提交的参数中，有需要重启数据库的，PolarDB将重启数据库。 必须满足以下条件，否则调用失败： 当前实例状态：使用中。 当前实例锁定模式：正常。 参数值有如下3类： [1-65535]，表示数值范围，通过正则识别，从而提取出最小值和最大值。然后根据最小值和最大值对输入参数进行验证，另外，还需要是整除因子的倍数。 [utf8|gbk|latin1]，表示固定的取值规则，通过正则识别，从而提取出固定的取值。然后根据这些固定的取值对输入参数进行验证。 其他，这种情况符合正则表达式。 云原生数据库 I参考下达任务之前，PolarDB将会进行参数检查，步骤如下：
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
| Forcerestart | String | 否 | true：强制重启（若修改的参数当中，有需要重启的参数，则必须传入true，否则修改将不生效）； false：不强制重启。默认不强制重启。 |

**返回参数**

| 名称 | 类型 | 描述 |
|---|---|---|
| RequestId | String | 请求ID。 |

**示例**

**请求示例**

```
https://polardb.example.com/?Action=ModifyParameter &DBInstanceId=polardb-xxxxx &Parameters={"key_buffer_size":"456","character_set_client":"gbk"}
```

**返回示例**

云原生数据库 I参考 XML格式：

```xml
<ModifyParameterResponse> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> </ModifyParameterResponse>
```

JSON格式：

```json
{ "RequestId":"1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC",}
```

### 日志管理

#### 查看慢日志列表

**描述**

用户可以查询某日期范围内、某个用户实例下、某个DB的慢查询汇总情况。 支持分页查询。

**请求参数**

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| Action | String | 是 | 系统规定参数，取值：DescribeSlowLogs。 |
| DBInstan ceId | String | 是 | 实例ID。 |
| StartTime | String | 是 | 查询开始日期，格式：YYYY-MM-DDZ，如2011-05-30Z。 |
| EndTime | String | 是 | 查询结束日期，不能小于查询开始日期。 格式：YYYY-MM-DDZ，如2011-05-30Z。 |
| DBName | String | 否 | 数据库名称。 |
| SortKey | String | 否 | 排序依据，取值： TotalExecutionCounts:总执行次数最多。 TotalQueryTimes:总执行时间最多。 TotalLogicalReads:总逻辑读最多。 |
| PageSize | Integer | 否 | 每页记录数，取值：30/50/100，默认值：30。 |
| PageNum ber | Integer | 否 | 页码大于0，且不超过Integer的最大值；默认值：1。 |

云原生数据库 I参考

**返回参数**

| 名称 | 类型 | 描述 |
|---|---|---|
| <公共返回参数> |  | 公共返回参数，具体请参见公共返回参数。 |
| Engine | String | 数据库类型。 |
| StartTime | String | 查询开始日期，格式：YYYY-MM-DDZ，如2011-05-30Z。 |
| EndTime | String | 查询结束日期，格式：YYYY-MM-DDZ，如2011-05-30Z。 |
| TotalRecordCou nt | Integer | 总记录数。 |
| PageNumber | Integer | 页码。 |
| PageRecordCou nt | Integer | 本页SQL语句个数。 |
| Items | List<SQLSlow Log> | 慢日志语句列表。 |

**示例**

**请求示例**

```
https://polardb.example.com/?Action=DescribeSlowLogs &DBInstanceId=polardb-xxxxx &StartTime=2011-06-11Z &EndTime=2011-12-11Z &SortKey= Totaxxxxx
```

**返回示例**

XML格式： 云原生数据库 I参考

```xml
<DescribeSlowLogsResponse> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> <DBInstanceID>polardb-xxxxx</DBInstanceID> <Engine>MySQL</Engine> <StartTime>2011-06-11Z</StartTime> <EndTime>2011-12-11Z</EndTime> <TotalRecordCount>1</TotalRecordCount> <PageNumber>1</PageNumber> <PageRecordCount>1</PageRecordCount> <Items> <SQLSlowLog> <SQLText>update test.zxb set id=0 limit 1</SQLText> <MySQLTotalExecutionCounts>178</MySQLTotalExecutionCounts> <MySQLTotalExecutionTimes>189</MySQLTotalExecutionTimes> <TotalLogicalReadcounts>89</TotalLogicalReadcounts> <TotalPhysicalReadcounts>90</TotalPhysicalReadcounts> <ReportTime>2013-11-12Z</ReportTime> </SQLSlowLog> </Items> </DescribeSlowLogsResponse>
```

JSON格式：

```json
{ "RequestId":"1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC", "StartTime":"2011-06-11Z ", "EndTime":"2011-12-11Z ", "Engine":"MySQL", "PageNumber":1, "PageRecordCount":1, "TotalRecordCount"：1, "Items":{
    "SQLSlowLog":[{
        "SQLText":”update test.zxb set id=0 limit 1”,
        "MySQLTotalExecutionCounts":178,
        "MySQLTotalExecutionTimes":189,
        "TotalLogicalReadcounts":89,
        "TotalPhysicalReadcounts":90,
        "ReportTime":"2013-11-12Z " }]}}
```

#### 查看慢日志明细

**描述**

用户可以查询某日期范围内、某个用户实例下、某个DB的慢查询明细，仅支持MySQL数据库。

**请求参数**

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| Action | String | 是 | 系统规定参数，取值：DescribeSlowLogRecords。 |

云原生数据库 I参考

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
| <公共返回参数> |  | 公共返回参数，具体请参见公共返回参数。 |
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

云原生数据库 I参考

| SQLText | Strin g | 查询语句。 |
|---|---|---|
| QueryTimes | Long | 执行时长，单位：秒。 |
| LockTimes | Long | 锁定时长，单位：秒。 |
| ParseRowCounts | Long | 解析行数。 |
| ReturnRowCount s | Long | 返回行数。 |
| ExecutionStartTi me | Strin g | 执行开始时间；格式：YYYY-MM-DD’T’HH:mm:ss Z，如2011-06-11 T15:00:08Z。 |

**示例**

**请求示例**

```
https://polardb.example.com/?Action=DescribeSlowLogRecords &DBInstanceId=rm-xxxxx &StartTime=2011-06-11T15:00Z &EndTime=2011-06-11T16:00Z
```

**返回示例**

XML格式：

```xml
<DescribeSlowLogRecordsResponse> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> <DBInstanceID>rm-xxxxx</DBInstanceID> <Engine>MySQL</Engine> <TotalRecordCount>1</TotalRecordCount> <PageNumber>1</PageNumber> <PageRecordCount>1</PageRecordCount> <Items> <SQLSlowRecord> <HostAddress>192.168.0.123</HostAddress> <DBName>test</DBName> <SQLText>update test.zxb set id=0 limit 1</SQLText> <QueryTimes>123</QueryTimes> <LockTimes>12</LockTimes> <ParseRowCounts>125</ParseRowCounts> <ReturnRowCounts>1</ReturnRowCounts> <ExecutionStartTime>2011-06-11T15:00:08Z</ExecutionStartTime> </SQLSlowRecord> </Items> </DescribeSlowLogRecordsResponse>
```

云原生数据库 I参考 JSON格式：

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

云原生数据库 I参考

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

XML格式： 云原生数据库 I参考

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

#### 查看BINLOG日志

**描述**

查询实例的BINLOG文件（仅限MySQL数据库实例），支持分页。PolarDB提供Binlog文件下载。 当DownloadLink为NULL时，表示PolarDB没有提供下载链接URL； 当DownloadLink不为NULL时，用户可以根据此URL，通过wget（请加双引号）、浏览器、编写程序下载备份文件，此URL已设置过期时间LinkExpiredTime，请在过期时间之前使用。 若过期，用户在下载时，将会出现如下错误码：

```xml
<Error> <Code>AccessDenied</Code> <Message>Request has expired.</Message> <Expires>2012-12-25T09:47:52.000Z</Expires> <ServerTime>2012-12-25T09:49:00.000Z</ServerTime> <RequestId>50D9768CA801C2F102005C70</RequestId> <HostId>oss-test.aliyun-inc.com</HostId> </Error>
```

**请求参数**

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|

云原生数据库 I参考

| Action | String | 是 | 系统规定参数，取值：DescribeBinlogFiles。 |
|---|---|---|---|
| DBInstanceI d | String | 是 | 实例ID。 |
| StartTime | String | 是 | 查询开始时间，格式：yyyy-MM-dd’T’HH:mm:ssZ。 |
| EndTime | String | 是 | 查询结束时间，格式：yyyy-MM-dd’T’HH:mm:ssZ，且大于查询开始时间。 |
| PageSize | Intege r | 否 | 每页记录数，取值：30/50/100，默认值：30。 |
| PageNumbe r | Intege r | 否 | 页码，大于0，且不超过Integer的最大值，默认值：1。 |

**返回参数**

| 名称 | 类型 | 描述 |
|---|---|---|
| <公共返回参数> | - | 公共返回参数，具体请参见公共返回参数。 |
| TotalRecordCount | Integer | Binlog文件总数。 |
| PageNumber | Integer | 页码。 |
| PageRecordCount | Integer | 本页Binlog文件个数。 |
| Items | List<BinLogFile> | - |

BinLogFile参数

| 名称 | 类型 | 描述 |
|---|---|---|
| FileSize | Long | Binglog文件大小，单位：Byte。 |
| LogBeginTime | String | Binglog文件记录的开始时间。 |
| LogEndTime | String | Binglog文件记录的结束时间。 |

云原生数据库 I参考

| DownloadLink | String | 支持HTTP协议的下载链接URL，NULL表示没有下载链接 |
|---|---|---|
| HostInstanceID | String | Binlog所在实例编号，用户区分该Binlog日志产生于主实例或从实例。 |
| LinkExpiredTime | String | URL过期时间，格式如：2011-06-11T15:00:00Z。 |

**示例**

**请求示例**

```
https://polardb.example.com/?Action=DescribeBinlogFiles &DBInstanceId=polardb-xxxxx &StartTime=2011-06-11T15:00:00Z &EndTime=2013-06-05T15:00:00Z
```

**返回示例**

XML格式：

```xml
<DescribeBinlogFilesResponse> <RequestId>1E3D5A1E0-67CA-43DA-24BC-EAF2D5A1E4DC</RequestId> <TotalRecordCount>1</TotalRecordCount> <PageNumber>1</PageNumber> <PageRecordCount>1<PageRecordCount> <Items> <BinLogFile> <FileSize>123</FileSize> <LogBeginTime>2013-06-01T15:00:00Z</LogBeginTime> <LogEndTime>2013-06-02T18:00:00Z</LogEndTime> <DownloadLink>http://polardblogreal.oss.aliyuncs.com/custinsxxxxx/hostinsxxxxx/mysql-bin.000120.zip? spm=0.0.0.0.eMQKjs&OSSAccessKeyId=c9gzsqpauxxxxx&Expires=1384916927&Signature=07TMgM3xx x</DownloadLink> <LinkExpiredTime>2013-06-09T18:00:00Z</LinkExpiredTime> </BinLogFile> </Items> </DescribeBinlogFilesResponse>
```

JSON格式： 云原生数据库 I参考

```json
{ "RequestId":"66816822-CEC1-4C8D-AB26-2530A7D4DCA5", "PageNumber":1, "TotalRecordCount":1, "PageRecordCount":1, "Items":{
 "BinLogFile":[{
  FileSize:”123”,
  LogBeginTime:”2013-06-01T15:00:00Z”,
  LogEndTime:”2013-06-02T18:00:00Z”,
  DownloadLink:”http://polardblog-
real.oss.aliyuncs.com/custinsxxxxx/hostinsxxxxx/mysql-bin.000120.zip? spm=0.0.0.0.eMQKjs&OSSAccessKeyId=c9gzsqpauxxxxx&Expires=1384916927&Signature=07TMgM3xx x”,
  LinkExpiredTime”2013-06-09T18:00:00Z”}]}}
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
| SQLCollectorStatu s | String | Enable：SQL采集开启；Disabled：SQL采集关闭。 |

#### 切换SQL采集状态

**描述**

开启或关闭指定PolarDB实例的SQL采集功能。

**请求参数**

云原生数据库 I参考

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
| User | Stri ng | 否 | 用户名称，默认为所有用户。 |
| Form | Stri ng | 否 | File，触发审计日志文件的生成，若传入这个值，则只返回公共参数，需再调用查询SQL审计文件列表接口获取文件的最终下载地址；Stream，返回数据流。默认为Stream。 |
| QueryKey words | Stri ng | 否 | 关键字查询，多个关键字以空格分隔，不超过10个关键字。 |

云原生数据库 I参考

| StartTime | Stri ng | 是 | 查询开始时间，格式如：yyyy-MM-dd'`T'HH:mm:ssZ。 |
|---|---|---|---|
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
| AccountName | String | 账号名。 |
| HostAddress | String | 客户端IP地址。 |
| SQLText | String | SQL语句。 |
| TotalExecutionTimes | Long | 消耗时间，单位：微秒。 |

云原生数据库 I参考

| ReturnRowCounts | Long | 返回记录数。 |
|---|---|---|
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

JSON格式： 云原生数据库 I参考

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

云原生数据库 I参考

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

云原生数据库 I参考

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

JSON格式： 云原生数据库 I参考

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

云原生数据库 I参考

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

云原生数据库 I参考

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

云原生数据库 I参考

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

云原生数据库 I参考

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

云原生数据库 I参考

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

云原生数据库 I参考

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

云原生数据库 I参考

| DescribeBinlogFiles | DescribeSQLLogReports |
|---|---|
| DescribeSQLLogRecords | DescribeOptimizeAdviceOnStorage |
| DescribeOptimizeAdviceOnMissPK | DescribeOptimizeAdviceOnExcessIndex |
| DescribeOptimizeAdviceOnMissIndex | DescribeOptimizeAdviceByDBA |
| DescribeParameters | ModifyParameter |

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

云原生数据库 I参考

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

云原生数据库 I参考

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

云原生数据库 I参考

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
| ModifyParameter | acs:polardb:$regionid:$accountid:dbinstance/$dbinstance id |

云原生数据库 I参考

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

云原生数据库 I参考

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

云原生数据库 I参考

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

云原生数据库 I参考

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

云原生数据库 I参考

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

云原生数据库 I参考

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

云原生数据库 I参考

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

云原生数据库 I参考

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

| olarDB MySQL主备版开发指南·AP 参考 |  | 云原生数据库 |
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

云原生数据库 I参考

| DBInstanceNetTypeChanging | 内外网切换中。 |
|---|---|
| GuardSwitching | 容灾切换中。 |
| INS CLONING _ | 实例克隆中。 |

#### 性能参数表

**云数据库MySQL版**

| API参数名 | 含义 |
|---|---|
| MySQL NetworkTraffic _ | MySQL实例平均每秒钟的输入流量，MySQL实例平均每秒钟的输出流量。单位为 KB。 |
| MySQL QPSTPS _ | 平均每秒SQL语句执行次数，平均每秒事务数。 |
| MySQL Sessions _ | 当前活跃连接数，当前总连接数。 |
| MySQL InnoDBBufferRatio _ | InnoDB缓冲池的读命中率，InnoDB缓冲池的利用率，InnoDB缓冲池脏块的百分率。 |
| MySQL InnoDBDataReadW _ riten | InnoDB平均每秒钟读取的数据量，InnoDB平均每秒钟写入的数据量。单位为 KB。 |
| MySQL InnoDBLogRequest _ s | 平均每秒向InnoDB缓冲池的读次数，平均每秒向InnoDB缓冲池的写次数。 |
| MySQL InnoDBLogWrites _ | 平均每秒日志写请求数，平均每秒向日志文件的物理写次数，平均每秒向日志文件完成的fsync()写数量。 |
| MySQL TempDiskTableCre _ ates | MySQL执行语句时在硬盘上自动创建的临时表的数量。 |
| MySQL MyISAMKeyBufferR _ atio | MyISAM平均每秒Key Buffer利用率，MyISAM平均每秒Key Buffer读命中率，MyISAM平均每秒Key Buffer写命中率。 |
| MySQL MyISAMKeyReadWr _ ites | MyISAM平均每秒钟从缓冲池中的读取次数，MyISAM平均每秒钟从缓冲池中的写入次数，MyISAM平均每秒钟从硬盘上读取的次数，MyISAM平均每秒钟从硬盘上写入的次数。 |

云原生数据库 I参考

| MySQL COMDML _ | 平均每秒Delete语句执行次数，平均每秒Insert语句执行次数， 平均每秒 Insert Select语句执行次数，平均每秒Replace语句执行次数，平均每秒 _ Replace Select语句执行次数，平均每秒Select语句执行次数，平均每秒Update _ 语句执行次数。 |
|---|---|
| MySQL RowDML _ | 平均每秒从InnoDB表读取的行数，平均每秒从InnoDB表更新的行数，平均每秒从 InnoDB表删除的行数，平均每秒从InnoDB表插入的行数，平均每秒向日志文件的物理写次数。 |
| MySQL MemCpuUsage _ | MySQL实例CPU使用率（占操作系统总数），MySQL实例内存使用率（占操作系统总数）。 |
| MySQL IOPS _ | MySQL实例的IOPS（每秒IO请求次数）。 |
| MySQL DetailedSpaceUsag _ e | MySQL实例空间占用详情：ins size实例总空间使用量；data size数据空间； _ _ log size日志空间；tmp size临时空间；other size系统空间。 _ _ _ |
| slavestat | 只读实例延迟。 |

#### 禁用关键字表

**云数据库MySQL版**

| 参数字段 | 关键字描述 |
|---|---|

云原生数据库 I参考

| DBName/ AccountName | admin,aurora,replicator,xtrabak,root（MySQL5.5/5.6）,mysql,test,eagleye,infor mation schema,guest,add,analyze,asc,between,blob,call,c _ hange,check,condition,continue,cross,current timestamp,database,day micros _ _ econd,dec,default,desc,distinct,double,e ach,enclosed,exit,fetch,float8,foreign,goto,having,hour minute,ignore,infile,inse _ nsitive,int1,int4,interval,iterate,keys,lea ding,like,lines,localtimestamp,longblob,low priority,mediumint,minute microse _ _ cond,modifies,no write to binlog,on, _ _ _ optionally,out,precision,purge,read,references,rename,require,revoke,schema,s elect,set,spatial,sqlexception,sql big re _ _ sult,ssl,table,tinyblob,to,true,unique,update,using,utc timestamp,varchar,when, _ with,xor,all,and,asensitive,bigint,both,c ascade,char,collate,connection,convert,current date,current user,databases,da _ _ y minute,decimal,delayed,describe,dis _ tinctrow,drop,else,escaped,explain,float,for,from,grant,high priority,hour secon _ _ d,in,inner,insert,int2,int8,into,join,kill,le ave,limit,load,lock,longtext,match,mediumtext,minute second,natural,null,opti _ mize,or,outer,primary,raid0,reads,regex p,repeat,restrict,right,schemas,sensitive,show,specific,sqlstate,sql calc found r _ _ _ ows,starting,terminated,tinyint,trailing, undo,unlock,usage,utc date,values,varcharacter,where,write,year month,alter, _ _ as,before,binary,by,case,character,colu mn,constraint,create,current time,cursor,day hour,day second,declare,delete, _ _ _ deterministic,div,dual,elseif,exists,false, float4,force,fulltext,group,hour microsecond,if,index,inout,int,int3,integer,is,key _ ,label,left,linear,localtime,long,loop,me diumblob,middleint,mod,not,numeric,option,order,outfile,procedure,range,real,r elease,replace,return,rlike,second mi _ crosecond,separator,smallint,sql,sqlwarning,sql small result,straight join,then,t _ _ _ inytext,trigger,union,unsigned,use,utc _ time,varbinary,varying,while,x509,zerofill,galaxy |
|---|---|

**云数据库SQL Server版**

| 参数字段 | 关键字描述 |
|---|---|

云原生数据库 I参考

| DBName/ AccountName | root,admin,eagleye,master,aurora,sa,sysadmin,administrator,mssqld,public,security admin,serveradmin,setupadmin,pr ocessadmin,diskadmin,dbcreator,bulkadmin,tempdb,msdb,model,distribution,mssqls ystemresource,guest,add,except, percent,all,exec,plan,alter,execute,precision,and,exists,primary,any,exit,print,as,fetc h,proc,asc,file,procedure,authorizati on,fillfactor,public,backup,for,raiserror,begin,foreign,read,between,freetext,readtext, break,freetexttable,reconfigure,br owse,from,references,bulk,full,replication,by,function,restore,cascade,goto,restrict,c ase,grant,return,check,group,rev oke,checkpoint,having,right,close,holdlock,rollback,clustered,identity,rowcount,coale sce,identity insert,rowguidcol,coll _ ate,identitycol,rule,column,if,save,commit,in,schema,compute,index,select,constrain t,inner,session user,contains,insert, _ set,containstable,intersect,setuser,continue,into,shutdown,convert,is,some,create,jo in,statistics,cross,key,system user, _ current,kill,table,current date,left,textsize,current time,like,then,current timestamp, _ _ _ lineno,to,current user,load,top,cur _ sor,national,tran,database,nocheck,transaction,dbcc,nonclustered,trigger,deallocate ,not,truncate,declare,null,tsequal, default,nullif,union,delete,of,unique,deny,off,update,desc,offsets,updatetext,disk,on, use,distinct,open,user,distributed, opendatasource,values,double,openquery,varying,drop,openrowset,view,dummy,op enxml,waitfor,dump,option,when, else,or,where,end,order,while,errlvl,outer,with,escape,over,writetext,galaxy |
|---|---|

云原生数据库 K参考

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
云原生数据库 K参考 i. 在左侧导航栏中，选择**版本管理** **> SDK****工具**。 ii. 单击页面顶部右上角**SDK****按需定制**。 iii. 在弹出的**专有云****SDK****定制**页面，从左到右依次选择对应的专有云版本、产品名称、产品版本、SDK版本、API版本和SDK语言。 iv. 填写完成后，单击**创建****SDK**。 v. 单击**下载**，下载对应的SDK。

### Java SDK调用

#### 使用手册

##### 使用CommonRequest进行调用

当您要调用的某个产品的API没有提供SDK时，可以采用泛用型的API调用方式（CommonRequest）。使用CommonRequest调用方式可实现任意Open API接口的调用。

**CommonRequest调用特点**

CommonRequest的特点如下：
1. 轻量：只需Core包即可发起调用，无需下载安装各产品的SDK。
2. 简便：无需更新SDK即可调用最新发布的API。
3. 快速迭代。
发起一次CommonRequest请求，您需要获取以下几个参数的值。您可以在各产品的API文档中获取以下参数的值。 域名（domain）：该产品的服务地址。 API版本（version）：该API的版本号，格式为YYYY-MM-DD。 您可以在各产品的API文档的公共参数部分获取API版本。 云原生数据库 K参考接口信息：要调用的接口名称。 您需要获取**Action**参数，使用 `request.ApiName = "<Action>"` 的方式来指定API名称。 例如RunInstances接口，在发起CommonRequest请求时，需要使用 `request.ApiName =` `"RunInstances"` 来指定API名称。 您需要获取**PathPattern**参数，使用 `request.PathPattern = "<PathPattern>"` 的方式来指定 RESTful路径。 例如查看所有集群实例的API的**PathPattern**为 `/clusters` ，在发起CommonRequest请求时，要使用 `request.PathPattern = "/clusters"` 指定RESTful路径。

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

以下代码展示了如何使用CommonRequest的方式调用的查看所有集群实例接口： 云原生数据库 K参考

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
云原生数据库 K参考发起一次CommonRequest请求，您需要获取以下几个参数的值。您可以在各产品的API文档中获取以下参数的值。 域名(domain)：该产品的服务地址。 API版本(version)：该API的版本号，格式为YYYY-MM-DD。 您可以在各产品的API文档的公共参数部分获取API版本。 接口信息：要调用的接口名称。 您需要获取**Action**参数，使用 `request.ApiName`

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

以下代码展示了Python2.x如何使用CommonRequest的方式调用的查看所有集群实例接口： 云原生数据库 K参考

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
云原生数据库 K参考

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
云原生数据库

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
云原生数据库
6. 在机器中执行如下命令：**curl -l**

**"http://127.0.0.1:7070/api/v3/column/c.sr.service_registration,c.sr.id?**

**c.sr.service_registration"**，获取json数据。
7. 根据PolarDB产品的ID（polardb-yaochi）和key值（polardb.openapi.endpoint），找到PolarDB的
endpoint。 云原生数据库

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
