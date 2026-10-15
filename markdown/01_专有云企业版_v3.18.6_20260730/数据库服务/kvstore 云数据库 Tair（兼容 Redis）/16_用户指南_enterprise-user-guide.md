---
title: "云数据库 Tair（兼容 Redis） 用户指南"
product_version: "v3.18.6-SP2607"
doc_version: "20260729"
pdf_pages: 159
source_pdf: "16_用户指南_enterprise-user-guide.pdf"
source_url: "https://apsara-doc.oss-cn-hangzhou.aliyuncs.com/apsara-pdf/enterprise/v_3_18_6_20260730/kvstore/zh/enterprise-user-guide.pdf"
converter: line-classifier (PyMuPDF)
---

# 云数据库 Tair（兼容 Redis） 用户指南

云数据库 Tair（兼容Redis）用户指

## 内核版本发布记录

本文为您介绍了云数据库 Tair（兼容 Redis）的内核版本发布情况。

**说明**

详细更新点及版本差异请参见《**Hotfix****版本说明书》**中**《云数据库** **Tair****（兼容** **Redis****）》**章节。

**发布日期：2026-07-30**

v3.18.6r-paas-kvstore-hotfeature-SP003提供云数据库 Tair（兼容 Redis）新内核版本升级：

| 产品 | 部署模式 | 版本/引擎 | 内核小版本 |
|---|---|---|---|
| 云数据库Tair（兼容 Redis） | 云原生 | 企业版7.0 | 26.5.0.0 |
|  | 经典 | 社区版7.0 | 0.2.13 |
|  | 经典 | 企业版5.0 | 5.0.72 |
|  | 经典 | 社区版6.0 | 0.2.28 |
|  | 经典 | 社区版5.0 | 5.2.28 |
|  | 经典 | 社区版4.0 | 1.9.20 |

云数据库 Tair（兼容Redis）用户指

## 什么是

云数据库 Tair（兼容 Redis）是兼容开源Redis协议标准的数据库服务，基于双机热备架构及集群架构，可满足高吞吐、低延迟及弹性变配等业务需求。

**功能特性**

支持云原生部署模式兼容更高的Redis版本，同时也具有更加灵活的架构配置。更多特性，请参见《产品简介》中功能特性章节。 在社区版的基础上推出企业级缓存服务产品，提供性能增强型供您选择。 支持String（字符串）、List（链表）、Set（集合）、Sorted Set（有序集合）、Hash（哈希表）、 Stream（流数据）等多种数据结构，同时支持Transaction（事务）、Pub/Sub（消息订阅与发布）等高级功能。

**支持的实例类型**

| 实例类型 | 简介 |
|---|---|
| 社区版 | 兼容开源Redis的高性能数据缓存服务，支持主从双副本、集群和读写分离架构。 |
| 企业版（性能增强型） | 在社区版的基础上开发的强化版Redis服务，推出性能增强型产品，采用多线程模型，集成阿里巴巴Tair的部分特性，支持多种Tair数据结构，对于部分特殊业务有很高的适用性。 |
| 云原生版 | 兼容Redis7.0版本，同时也具有更加灵活的架构配置。支持更灵活的副本管理、单副本模式、更大规格集群和读写分离能力。 |

云数据库 Tair（兼容Redis）用户指

## 使用限制

| 项目 | 说明 |
|---|---|
| List数据类型 | 没有List个数限制，单个元素最大值为512 MB，推荐List的元素个数小于 8192，value最大长度不超过1 MB。 |
| Set数据类型 | 没有Set个数限制，单个元素最大值为512 MB，推荐Set的元素个数小于 8192，value最大长度不超过1 MB。 |
| Sorted Set数据类型 | 没有Sorted Set个数限制，单个元素最大值为512 MB，推荐Sorted Set的元素个数小于8192， value最大长度不超过1 MB。 |
| Hash数据类型 | 没有field个数限制，单个元素最大值为512 MB，推荐元素个数小于8192，value 最大长度不超过1 MB。 |
| DB数限制 | 每个实例支持256个DB，建议通过拆分Redis的方式来使用多DB。 |
| 数据过期删除策略 | 主动过期：系统后台会周期性的检测，若发现已过期的key时，会将其删除，但不保证时效性。 被动过期：将在访问key时同步生效。当用户访问某个key时，若该key已经过期，则将其删除。 说明在Redis 4.0版本之前，删除大key会消耗较大资源，可能会导致业务抖动。 |
| 空闲连接回收机制 | 服务端不主动回收Redis空闲连接，由用户管理。 |
| 数据持久化策略 | 采用AOF FSYNC EVERYSEC方式，每秒fysnc。 _ _ |

云数据库 Tair（兼容Redis）用户指

## 企业版介绍与命令支持

### 企业版性能增强型介绍

云数据库 Tair（兼容 Redis）企业版性能增强型（简称性能增强型）适合并发量大、读写热点多，对性能要求较高的场景。相比社区版，性能增强型主要在多线程和多模块集成方面进行了优化。

**主要优势**

| 类别 | 说明 |
|---|---|
| 性能 | 读写性能达到同规格Redis社区版实例的3倍，能够更好地应对热点数据的高频读写。 相比原生Redis，高QPS场景下响应时间更短，性能表现更佳。 在大并发场景下运行稳定，可以极大地缓解突发大量请求导致的连接问题，从容应对业务高峰。 全量同步和增量同步在I/O线程中进行，提高同步速度。 |
| 自研模块 | 集成多个自研的Redis模块，包括CAS和CAD命令、TairString命令、TairHash命令、TairGIS命令、TairBloom命令、TairDoc命令，扩展了Redis的适用性，同时降低了复杂场景下业务的开发难度，让您专注于业务创新。 |
| 兼容性 | 100%兼容原生Redis，无需修改业务代码。 |
| 扩展性 | 支持主从和集群架构，可根据业务需求执行垂直扩容（升级规格）或水平扩容（升级为集群版）。 |

**适用场景**

适用于视频直播、电商秒杀和在线教育等场景，例如：

| 业务上遇到的问题 | 说明 |
|---|---|
| 社区版主从架构实例无法满足高QPS 需求。 | 使用Redis社区版主从实例在秒杀场景中构建缓存，部分热点Key的QPS要求高达20万以上，社区版实例无法满足业务高峰期的需求。 采用性能增强型（主从版）实例后，热门商品秒杀过程流畅，未发生性能问题。 |
| 需要沿用现有主从架构并提升实例性能。 | 由于集群版在存在一定的使用限制，需要保持现有的主从架构。 采用性能增强型（主从版）实例，在满足性能需求的同时保持了现有架构，避免升级至集群带来的限制，无需调整现有业务实现方式。 |

云数据库 Tair（兼容Redis）用户指

| 自建Redis集群分片多、成本高、性能损耗大。 | 随着业务的高速发展，自建Redis集群的分片数不断增加，导致管理维护成本上升，且带来了一定的性能损耗。 采用性能增强型（集群版）实例后，得益于其出色的性能，分片数缩减至原有的三分之一，降低了性能损耗，同时，云数据库提供丰富的管理功能帮助您便捷地管理集群。 |
|---|---|

**性能对比**

Redis社区版实例采用与原生Redis相同的单线程模型，每个数据节点支持8万到10万的QPS。 Redis性能增强型采用多线程模型，由I/O线程、Worker线程和辅助线程共同完成数据处理，单节点性能为社区版实例的3倍左右。 下表展示了不同架构下，社区版和企业版（性能增强型）实例的适用场景对比。

| 架构 | 实例类型 | 说明 |
|---|---|---|
| 标准架构（主从版） | 社区版 | 不适用于单节点QPS要求超过10万的场景。 |
|  | 企业版（性能增强型） | 可应用于QPS高于10万的场景。 |
| 集群架构（集群版） | 社区版 | 包含多个数据节点，每个节点的性能与主从版实例相似。当某个节点储存了热度较高的数据并面临大并发量的请求时，该节点中其它数据的读写可能受到影响，形成性能瓶颈。 |
|  | 企业版（性能增强型） | 能更好地应对热读写，降低维护成本。 |

### CAS和CAD命令

本文介绍云数据库 Tair（兼容 Redis）企业版性能增强型实例中新增的String增强类命令，包括CAS和 CAD。

**使用前提**

请注意，本文介绍的命令只有在满足以下条件时才能生效。 Redis实例为企业版性能增强型。 操作对象为性能增强型实例中的Redis String数据。

**说明**

性能增强型实例中可同时设置Redis String（即Redis原生String）和TairString，CAS和CAD只能对Redis String使用。

**命令列表**

表 1. String增强命令云数据库 Tair（兼容Redis）用户指

| 命令 | 语法 | 说明 |
|---|---|---|
| CAS | CAS <key> <oldvalue> <newvalue> | 当oldvalue和key的value相等时，修改value的值为 newvalue；不相等则不修改。 说明 CAS仅适用于操作Redis String类型的数据，如需对 TairString做相同的操作，请使用EXCAS。 |
| CAD | CAD <key> <value> | 当oldvalue和key的value相等时，删除该key；不相等则不删除。 说明 CAD仅适用于操作Redis String类型的数据，如需对 TairString做相同的操作，请使用EXCAD。 |

**CAS**

语法 CAS <key> <oldvalue> <newvalue> 时间复杂度 O(1) 命令描述 CAS（Compare And Set），查看某个key的value是否等于一个指定的值，如果相等，则将value修改为一个新的值；不相等则不修改。 参数及选项说明

| 参数/选项 | 说明 |
|---|---|
| key | String的key，用于指定作为命令调用对象的String。 |
| oldvalue | 用于跟key的现有value比较的值。 |
| newvalue | 当oldvalue和key的现有value相等时，将value修改为newvalue。 |

返回值成功：1。 key不存在：-1。 失败：0。 其它情况返回异常。 使用示例云数据库 Tair（兼容Redis）用户指

```
127.0.0.1:6379> SET foo bar
```

`OK`

```
127.0.0.1:6379> CAS foo baa bzz (integer) 0 127.0.0.1:6379> GET foo "bar" 127.0.0.1:6379> CAS foo bar bzz (integer) 1 127.0.0.1:6379> GET foo "bzz"
```

**CAD**

语法 CAD <key> <value> 时间复杂度 O(1) 命令描述 CAD（Compare And Delete），查看某个key的value是否等于一个指定的值，如果相等，删除该 key；不相等则不删除。 参数及选项说明

| 参数/选项 | 说明 |
|---|---|
| key | String的key，用于指定作为命令调用对象的String。 |
| value | 用于跟key的现有value比较的值。 |

返回值成功：1。 key不存在：-1。 失败：0。 其它情况返回异常。 使用示例

```
127.0.0.1:6379> SET foo bar
```

`OK`

```
127.0.0.1:6379> CAD foo bzz (integer) 0 127.0.0.1:6379> CAD not-exists xxx (integer) -1 127.0.0.1:6379> CAD foo bar (integer) 1 127.0.0.1:6379> GET foo (nil)
```

云数据库 Tair（兼容Redis）用户指

### TairString命令

本文介绍TairString数据支持的命令。

**TairString简介**

TairString是一种带版本号的string类型数据结构。Redis的String仅由key和value组成，而TairString不仅包含key和value，还携带了版本（version），可用于乐观锁等场景。除此之外，TairString在Redis String加减功能的基础上支持了边界设置，可以将**INCRBY**、**INCRBYFLOAT**的结果限制在一定的范围内，超出范围则提示错误。 主要特性： value携带版本号。 使用**INCRBY**、**INCRBYFLOAT**递增数据时可设置变更范围。 TairString与Redis原生String是两种不同的数据结构，相关命令不可混用。

**警告**

**使用前提**

请注意，本文介绍的命令只有在满足以下条件时才能生效。 Redis实例为企业版性能增强型。 操作对象为性能增强型实例中的TairString数据。 性能增强型实例中可同时设置Redis String（即Redis原生String）和TairString，本文

**说明**

的命令无法对Redis String使用。

**命令列表**

| 命令 | 语法 | 简介 |
|---|---|---|
| EXSET | EXSET <key> <value> [EX time] [PX time] [EXAT time] [PXAT time] [NX \| XX] [VER version \| ABS version] | 将value保存到key中。 |
| EXGET | EXGET <key> | 返回TairString的value和version。 |
| EXSETVER | EXSETVER <key> <version> | 直接对一个key设置version。 |
| EXINCRBY | EXINCRBY <key> <num> [EX time] [PX time] [EXAT time] [EXAT time] [PXAT time] [NX \| XX] [VER version \| ABS version] [MIN minval] [MAX maxval] | 对Key做自增自减操作，num的范围为long。 |
| EXINCRBYFLOAT | EXINCRBYFLOAT <key> <num> [EX time] [PX time] [EXAT time] [EXAT time] [PXAT time] [NX \| XX] [VER version \| ABS version] [MIN minval] [MAX maxval] | 对Key做自增自减操作，num的范围为double。 |
| EXCAS | EXCAS <key> <newvalue> <version> | 指定version将value更新，当引擎中的version和指定的相同时才更新成功，不成功会返回旧的value和 version。 |

|  |  | 云数据库 Tair（兼容Redis）用户指南·企业版介绍与命令支持 |
|---|---|---|

| EXCAD | EXCAD <key> <version> | 当指定version和引擎中version相等时候删除Key，否则失败。 |
|---|---|---|
| DEL | DEL <key> [key ...] | 使用原生Redis的DEL命令可以删除一条或多条 TairString数据。 |

**EXSET**

语法 EXSET <key> <value> [EX time] [PX time] [EXAT time] [EXAT time] [PXAT time] [NX | XX] [VER version | ABS version] 时间复杂度 O(1) 命令描述将value保存到key中。 参数及选项说明

| 参数或选项 | 说明 |
|---|---|
| key | TairString的key，用于指定作为命令调用对象的TairString。 |
| value | 需要为key设置的value。 |
| EX | 指定key的相对超时时间，单位为秒，为0表示立即过期。 |
| EXAT | 指定key的绝对超时时间，单位为秒，为0表示立即过期。 |
| PX | 指定key的相对超时时间，单位为毫秒，为0表示立即过期。 |
| PXAT | 指定key的绝对超时时间，单位为毫秒 ，为0表示立即过期。 |
| NX | 只在key不存在时写入。 |
| XX | 只在key存在时写入。 |
| VER | 版本号。 如果key存在，和当前版本号做比较： 如果相等，写入，且版本号加1。 如果不相等，返回异常。 如果key不存在或者key当前版本为0，忽略传入的版本号直接设置value，成功后版本号变为1。 |
| ABS | 绝对版本号。设置后，无论key当前的版本号是多少，完成写入并将key的版本号覆盖为该选项中设置的值。 |

返回值成功：OK。 其它情况返回异常。 使用示例云数据库 Tair（兼容Redis）用户指

```
127.0.0.1:6379> EXSET foo bar XX (nil) 127.0.0.1:6379> EXSET foo bar NX
```

`OK`

```
127.0.0.1:6379> EXSET foo bar NX (nil) 127.0.0.1:6379> EXGET foo
1) "bar"
2) (integer) 1
127.0.0.1:6379> EXSET foo bar1 VER 10 (error) ERR update version is stale 127.0.0.1:6379> EXSET foo bar1 VER 1
```

`OK`

```
127.0.0.1:6379> EXGET foo
1) "bar1"
2) (integer) 2
127.0.0.1:6379> EXSET foo bar2 ABS 100
```

`OK`

```
127.0.0.1:6379> EXGET foo
1) "bar2"
2) (integer) 100
```

**EXGET**

语法 EXGET <key> 时间复杂度 O(1) 命令描述获取TairString的value和version。 参数及选项说明 key：TairString的key，用于指定作为命令调用对象的TairString。 返回值成功：value+version。 其它情况返回异常。 使用示例

```
127.0.0.1:6379> EXSET foo bar ABS 100
```

`OK`

```
127.0.0.1:6379> EXGET foo
1) "bar"
2) (integer) 100
127.0.0.1:6379> DEL foo (integer) 1 127.0.0.1:6379> EXGET foo (nil)
```

**EXSETVER**

语法云数据库 Tair（兼容Redis）用户指 EXSETVER <key> <version> 时间复杂度 O(1) 命令描述直接对一个key设置version。 参数及选项说明

| 参数或选项 | 说明 |
|---|---|
| key | TairString的key，用于指定作为命令调用对象的TairString。 |
| version | 需要设置的版本号。 |

返回值成功：1。 key不存在：0。 其它情况返回异常。 使用示例

```
127.0.0.1:6379> EXSET foo bar
```

`OK`

```
127.0.0.1:6379> EXGET foo
1) "bar"
2) (integer) 1
127.0.0.1:6379> EXSETVER foo 2 (integer) 1 127.0.0.1:6379> EXGET foo
1) "bar"
2) (integer) 2
127.0.0.1:6379> EXSETVER not-exists 0 (integer) 0
```

**EXINCRBY**

语法 EXINCRBY |EXINCRBY <key> <num> [EX time] [PX time] [EXAT time] [EXAT time] [PXAT time] [NX | XX] [VER version | ABS version] [MIN minval] [MAX maxval] 时间复杂度 O(1) 命令描述对TairString的value做自增自减操作，num的范围为long。 参数及选项说明

| 参数或选项 | 说明 |
|---|---|
| key | TairString的key，用于指定作为命令调用对象的TairString。 |
| num | TairString自增的数值，必须为整数。 |
| EX | 指定key的相对超时时间，单位为秒，为0表示立即过期。 |

云数据库 Tair（兼容Redis）用户指

| EXAT | 指定key的绝对超时时间，单位为秒，为0表示立即过期。 |
|---|---|
| PX | 指定key的相对超时时间，单位为毫秒，为0表示立即过期。 |
| PXAT | 指定key的绝对超时时间，单位为毫秒 ，为0表示立即过期。 |
| NX | 只在key不存在时写入。 |
| XX | 只在key存在时写入。 |
| VER | 版本号。 如果key存在，和当前版本号做比较： 如果相等，进行自增，且版本号加1。 如果不相等，返回异常。 如果key不存在或者key当前版本为0，忽略传入的版本号并进行自增操作，成功后版本号变为1。 |
| ABS | 绝对版本号。设置后，无论key当前的版本号是多少，完成自增并将key的版本号覆盖为该选项中设置的值。 |
| MIN | TairString value的最小值。 |
| MAX | TairString value的最大值。 |

返回值成功：value的当前值。 其它情况返回异常。 使用示例

```
127.0.0.1:6379> EXINCRBY foo 100 (integer) 100 127.0.0.1:6379> EXINCRBY foo 100 MAX 150 (error) ERR increment or decrement would overflow 127.0.0.1:6379> FLUSHALL
```

`OK`

```
127.0.0.1:6379> EXINCRBY foo 100 (integer) 100 127.0.0.1:6379> EXINCRBY foo 100 MAX 150 (error) ERR increment or decrement would overflow 127.0.0.1:6379> EXINCRBY foo 100 MAX 300 (integer) 200 127.0.0.1:6379> EXINCRBY foo 100 MIN 500 (error) ERR increment or decrement would overflow 127.0.0.1:6379> EXINCRBY foo 100 MIN 500 MAX 100 (error) ERR min or max is specified, but not valid 127.0.0.1:6379> EXINCRBY foo 100 MIN 50 (integer) 300
```

**EXINCRBYFLOAT**

语法 EXINCRBYFLOAT |EXINCRBYFLOAT <key> <num> [EX time] [PX time] [EXAT time] [EXAT time] [PXAT time] [NX | XX] [VER version | ABS version] [MIN minval] [MAX maxval] 云数据库 Tair（兼容Redis）用户指时间复杂度 O(1) 命令描述对TairString的value做自增自减操作，num的范围为double。 参数及选项说明

| 参数或选项 | 说明 |
|---|---|
| key | TairString的key，用于指定作为命令调用对象的TairString。 |
| num | TairString自增的数值，类型为浮点数。 |
| EX | 指定key的相对超时时间，单位为秒，为0表示立即过期。 |
| EXAT | 指定key的绝对超时时间，单位为秒，为0表示立即过期。 |
| PX | 指定key的相对超时时间，单位为毫秒，为0表示立即过期。 |
| PXAT | 指定key的绝对超时时间，单位为毫秒 ，为0表示立即过期。 |
| NX | 当数据不存在时写入。 |
| XX | 当数据存在时写入。 |
| VER | 版本号。 如果key存在，和当前版本号做比较： 如果相等，进行自增，且版本号加1。 如果不相等，返回异常。 如果key不存在或者key当前版本为0，忽略传入的版本号并进行自增操作，成功后版本号变为1。 |
| ABS | 绝对版本号。设置后，无论key当前的版本号是多少，完成自增并将key的版本号覆盖为该选项中设置的值。 |
| MIN | TairString value的最小值。 |
| MAX | TairString value的最大值。 |

返回值成功：value的当前值。 其它情况返回异常。 使用示例云数据库 Tair（兼容Redis）用户指

```
127.0.0.1:6379> EXSET foo 100
```

`OK`

```
127.0.0.1:6379> EXINCRBYFLOAT foo 10.123 "110.123" 127.0.0.1:6379> EXINCRBYFLOAT foo 20 MAX 100 (error) ERR increment or decrement would overflow 127.0.0.1:6379> EXINCRBYFLOAT foo 20 MIN 100 "130.123" 127.0.0.1:6379> EXGET foo
1) "130.123"
2) (integer) 3
```

**EXCAS**

语法 EXCAS <key> <newvalue> <version> 时间复杂度 O(1) 命令描述当指定key的版本值和命令中设置的version相等时，将key的value修改为一个新的值；不相等则不修改。 参数及选项说明

| 参数或选项 | 说明 |
|---|---|
| key | TairString的key，用于指定作为命令调用对象的TairString。 |
| newvalue | 当version和key的现有版本值相等时，将value修改为newvalue。 |
| version | 用于跟key的现有版本值比较的值。 |

返回值成功：["OK", "", version]。返回值中间的""为无意义的空字符串，version为key当前的版本。 失败：["ERR update version is stale", value, version]。value和version为key当前的value和版本。 其它情况返回异常。 使用示例

```
127.0.0.1:6379> EXSET foo bar
```

`OK`

```
127.0.0.1:6379> EXCAS foo bzz 1
1) OK
```

`2)`

```
3) (integer) 2
127.0.0.1:6379> EXGET foo
1) "bzz"
2) (integer) 2
127.0.0.1:6379> EXCAS foo bee 1
1) ERR update version is stale
2) "bzz"
3) (integer) 2
```

云数据库 Tair（兼容Redis）用户指

**EXCAD**

语法 EXCAD <key> <version> 时间复杂度 O(1) 命令描述当指定key的版本值和命令中设置的version相等时删除Key。 参数及选项说明

| 参数或选项 | 说明 |
|---|---|
| key | TairString的key，用于指定作为命令调用对象的TairString。 |
| newvalue | 当version和key的现有版本值相等时，将value修改为newvalue。 |
| version | 用于跟key的现有版本值比较的值。 |

返回值成功：1。 key不存在：-1。 失败：0。 其它情况返回异常。 使用示例

```
127.0.0.1:6379> EXSET foo bar
```

`OK`

```
127.0.0.1:6379> EXGET foo
1) "bar"
2) (integer) 1
127.0.0.1:6379> EXCAD not-exists 1 (integer) -1 127.0.0.1:6379> EXCAD foo 0 (integer) 0 127.0.0.1:6379> EXCAD foo 1 (integer) 1 127.0.0.1:6379> EXGET foo (nil)
```

### TairHash命令

本文介绍TairHash数据支持的命令。

**TairHash简介**

TairHash是一种可为field设置过期时间和版本的hash类型数据结构。TairHash不但和Redis Hash一样支持丰富的数据接口和高处理性能，还改变了hash只能为key设置过期时间的限制，可以为field设置过期时间和版本，极大地提高了hash数据结构的灵活性，简化了很多场景下的业务开发工作。TairHash使用高效的Active Expire算法，可以在不对响应时间造成明显影响的前提下，更高效的完成对field的过期判断和删除。 主要特性： 云数据库 Tair（兼容Redis）用户指 field支持单独设置expire和version。 field支持高效active expire和passivity expire。 语法和原生Redis Hash数据类型类似。 支持高效的主动淘汰策略，会在一定程度上增加内存消耗。 TairHash与Redis中的原生Hash是两种不同的数据，相关命令不可混用。

**警告**

**使用前提**

请注意，本文介绍的命令只有在满足以下条件时才能生效。 Redis实例为企业版性能增强型。 操作对象为性能增强型实例中的TairHash数据。 性能增强型实例中可同时设置Redis Hash（即Redis原生Hash）和TairHash，本文的

**说明**

命令无法对Redis Hash使用。

**命令列表**

| 命令 | 语法 | 说明 |
|---|---|---|
| EXHSET | EXHSET <key> <field> <value> [EX time] [EXAT time] [PX time] [PXAT time] [NX/XX] [VER/ABS version] [NOACTIVE] | 向key指定的TairHash中插入一个field，如果 TairHash不存在则自动创建一个，如果field已经存在则覆盖其值。该命令会触发对field的被动淘汰检查。 |
| EXHMSET | EXHMSET <key> <field> <value> [field value...] | 同时向key指定的TairHash中插入多个field， 如果TairHash不存在则自动创建一个，如果 field已经存在则覆盖其值。该命令会触发对 field的被动淘汰。 |
| EXHPEXPIR EAT | EXHPEXPIREAT <key> <field> <milliseconds-timestamp> [VER/ABS version] [NOACTIVE] | 在key指定的TairHash中为一个field设置绝对过期时间，单位为毫秒。该命令会触发对field的被动淘汰。 |
| EXHPEXPIR E | EXHPEXPIRE <key> <field> <milliseconds> [NOACTIVE] | 在key指定的TairHash中为一个field设置相对过期时间，单位为毫秒。该命令会触发对field的被动淘汰。 |
| EXHEXPIRE AT | EXHEXPIREAT <key> <field> <timestamp> [NOACTIVE] | 在key指定的TairHash中为一个field设置绝对过期时间，单位为秒。该命令会触发对field的被动淘汰。 |
| EXHEXPIRE | EXHEXPIRE <key> <field> <seconds> [NOACTIVE] | 在key指定的TairHash中为一个field设置相对过期时间，单位为秒。该命令会触发对field的被动淘汰。 |
| EXHPTTL | EXHPTTL <key> <field> | 查看key指定的TairHash中一个field的剩余超时时间，单位为毫秒。该命令会触发对field的被动淘汰。 |
| EXHTTL | EXHTTL <key> <field> | 查看key指定的TairHash中一个field的剩余超时时间，单位为秒。该命令会触发对field的被动淘汰。 |
| EXHVER | EXHVER <key> <field> | 查看key指定的TairHash中一个field的当前版本号。该命令会触发对field的被动淘汰。 |

云数据库 Tair（兼容Redis）用户指

| EXHSETVE R | EXHSETVER <key> <field> <version> | 为key指定的TairHash中的一个field设置版本号。该命令会触发对field的被动淘汰。 |
|---|---|---|
| EXHINCRBY | EXHINCRBY <key> <field> <num> [EX time] [EXAT time] [PX time] [PXAT time] [VER/ABS version] [MIN minval] [MAX maxval] | 将key指定的TairHash中一个field的值加上整型value。如果TairHash不存在则自动新创建一个，如果指定的field不存在，则在加之前先将 field的值设置为0。同时还可以使用EX、 EXAT、PX或PXAT为field设置超时时间。该命令会触发对field的被动淘汰。 说明为Key的field设置了超时时间后，再次执行该命令时如果没有设置超时时间，该field将被设置为永不过期。 |
| EXHINCRBY FLOAT | EXHINCRBYFLOAT <key> <field> <value> [EX time] [EXAT time] [PX time] [PXAT time] [VER/ABS version] [MIN minval] [MAX maxval] | 将key指定的TairHash中一个field的值加上浮点型value。如果TairHash不存在则自动新创建一个，如果指定的field不存在，则在加之前先将 field的值设置为0。同时还可以使用EX、 EXAT、PX或PXAT为field设置超时时间。该命令会触发对field的被动淘汰。 说明为Key的field设置了超时时间后，再次执行该命令时如果没有设置超时时间，该field将被设置为永不过期。 |
| EXHGET | EXHGET <key> <field> | 获取key指定的TairHash中一个field的值，如果TairHash不存在或者field不存在，则返回 nil。该命令会触发对field的被动淘汰。 |
| EXHGETWI THVER | EXHGETWITHVER <key> <field> | 同时获取key指定的TairHash中一个field的值和版本，如果TairHash不存在或者field不存在，则返回nil。该命令会触发对field的被动淘汰。 |
| EXHMGET | EXHMGET <key> <field> [field ...] | 同时获取key指定的TairHash中多个field的值，如果TairHash不存在或者field不存在，则返回nil。该命令会触发对field的被动淘汰。 |
| EXHMGET WITHVER | EXHMGETWITHVER <key> <field> [field ...] | 同时获取key指定的TairHash中多个field的值和版本，如果TairHash不存在或者field不存在，则返回nil。该命令会触发对field的被动淘汰。 |
| EXHDEL | EXHDEL <key> <field> <field> <field> ... | 删除key指定的TairHash中的一个field，如果 TairHash不存在或者field不存在则返回0 ，成功删除返回1。该命令会触发对field的被动淘汰。 |
| EXHLEN | EXHLEN <key> [noexp] | 获取key指定的TairHash中field个数，该命令不会触发对过期field的被动淘汰，也不会将其过滤掉，所以结果中可能包含已经过期但还未被删除的field。如果只想返回当前没有过期的field 个数，可以在命令中设置noexp选项。 |
| EXHEXISTS | EXHEXISTS <key> <field> | 查询key指定的TairHash中是否存在对应的 field。该命令会触发对field的被动淘汰。 |
| EXHSTRLE N | EXHSTRLEN <key> <field> | 获取key指定的TairHash中一个field对应的 value的长度。该命令会触发对field的被动淘汰。 |

云数据库 Tair（兼容Redis）用户指

| EXHKEYS | EXHKEYS <key> | 获取key指定的TairHash中所有的field。该命令会过滤掉已经过期的field，但是为了尽快响应客户端，不会执行真正的删除操作。 |
|---|---|---|
| EXHVALS | EXHVALS <key> | 获取key指定的TairHash中所有field的值 。该命令会过滤掉已经过期的field，但是为了尽快响应客户端，不会执行真正的删除操作。 |
| EXHGETAL L | EXHGETALL <key> | 获取key指定的TairHash中所有的field及其 value。该命令会过滤掉已经过期的field，但是为了尽快响应客户端，不会执行真正的删除操作。 |
| EXHSCAN | EXHSCAN <key> <op> <subkey> [MATCH pattern] [COUNT count] | 扫描key指定的TairHash。扫描的方式（使用 op选项设置）可以为>、>=、<、<=、==、 ^、$。扫描的同时可以根据MATCH指定的 pattern对subkey进行正则过滤，还可以使用 COUNT对结果数目进行限制，如果不指定则默认值为10。该命令会过滤掉已经过期的field， 但是为了尽快响应客户端，不会执行真正的删除操作。 |
| DEL | DEL <key> [key ...] | 使用原生Redis的DEL命令可以删除一条或多条 TairHash数据。 |

**EXHSET**

语法 EXHSET <key> <field> <value> [EX time] [EXAT time] [PX time] [PXAT time] [NX | XX] [VER/ABS version] [NOACTIVE] 时间复杂度 O(1) 命令描述向key指定的TairHash中插入一个field。如果TairHash不存在则自动创建一个，如果field已经存在则覆盖其值。 参数及选项说明

| 参数或选项 | 说明 |
|---|---|
| key | TairHash的key，用于指定作为命令调用对象的TairHash。 |
| field | TairHash中的一个元素，一个TairHash key可以有多个field。 |
| value | field对应的值，一个field只能有一个value。 |
| EX | 指定field的相对过期时间，单位为秒，为0表示不过期。 |
| EXAT | 指定field的绝对过期时间，单位为秒，为0表示不过期。 |
| PX | 指定field的相对过期时间，单位为毫秒，为0表示不过期。 |
| PXAT | 指定field的绝对过期时间，单位为毫秒 ，为0表示不过期。 |
| NX | 只在field不存在时插入。 |
| XX | 只在field存在时插入。 |

云数据库 Tair（兼容Redis）用户指

| VER | 版本号。 如果field存在，和当前版本号做比较： 如果相等，继续操作，且版本号加1。 如果不相等，返回异常。 如果field不存在或者field当前版本为0，忽略传入的版本号并继续操作，成功后版本号变为 1。 |
|---|---|
| ABS | 绝对版本号，不论field是否存在，可以在插入field时设置为本参数所指定的版本号。 |
| NOACTIVE | 在指定EX、EXAT、PX或PXAT选项时，设置NOACTIVE表示该field不使用active expiration 策略，这样可以降低内存占用。 |

返回值新建field并成功为它设置值：1。 field已经存在，成功覆盖旧值：0。 指定了XX且field不存在：-1。 指定了NX且field已经存在：-1。 指定了VER且版本和当前版本不匹配："ERR update version is stale"。 其它情况返回相应的异常信息。

**EXHGET**

语法 EXHGET <key> <field> 时间复杂度 O(1) 命令描述获取指定TairHash一个field的值。 参数及选项说明

| 参数或选项 | 说明 |
|---|---|
| key | TairHash的key，用于指定作为命令调用对象的TairHash。 |
| field | TairHash中的一个元素，一个TairHash key可以有多个field。 |

返回值 field存在且操作成功：field对应的值。 key不存在或者field不存在：nil。 其它情况返回相应的异常信息。

**EXHMSET**

语法 EXHMSET <key> <field> <value> [field value...] 时间复杂度 O(1) 命令描述云数据库 Tair（兼容Redis）用户指同时向key指定的TairHash中插入多个field，如果TairHash不存在则自动创建一个，如果field已经存在则覆盖其value。 参数及选项说明

| 参数或选项 | 说明 |
|---|---|
| key | TairHash的key，用于指定作为命令调用对象的TairHash。 |
| field | TairHash中的一个元素，一个TairHash key可以有多个field。 |
| value | field对应的值，一个field只能有一个value。 |

返回值成功：OK。 其它情况返回相应的异常信息。

**EXHPEXPIREAT**

语法 EXHPEXPIREAT <key> <field> <milliseconds-timestamp> [VER/ABS version] [NOACTIVE] 时间复杂度 O(1) 命令描述在key指定的TairHash中为一个field设置绝对过期时间，精确到毫秒。 参数及选项说明

| 参数或选项 | 说明 |
|---|---|
| key | TairHash的key，用于指定作为命令调用对象的TairHash。 |
| field | TairHash中的一个元素，一个TairHash key可以有多个field。 |
| milliseconds- timestamp | 精确到毫秒的时间戳。 |
| VER | 版本号。 如果field存在，和当前版本号做比较： 如果相等，继续操作，且版本号加1。 如果不相等，返回异常。 如果field不存在或者field当前版本为0，忽略传入的版本号并继续操作，成功后版本号变为 1。 |
| ABS | 绝对版本号，不论field是否存在，继续操作并将field的版本号设置为本参数所指定的值。 |
| NOACTIVE | 在指定EX、EXAT、PX或PXAT选项时，设置NOACTIVE表示该field不使用active expiration 策略，这样可以降低内存占用。 |

返回值 field存在且设置成功：1。 field不存在：0。 其它情况返回相应的异常信息。 云数据库 Tair（兼容Redis）用户指

**EXHPEXPIRE**

语法 EXHPEXPIRE <key> <field> <milliseconds> [VER/ABS version] [NOACTIVE] 时间复杂度 O(1) 命令描述在key指定的TairHash中为一个field设置相对过期时间，单位为毫秒。 参数及选项说明

| 参数或选项 | 说明 |
|---|---|
| key | TairHash的key，用于指定作为命令调用对象的TairHash。 |
| field | TairHash中的一个元素，一个TairHash key可以有多个field。 |
| milliseconds | 相对过期时间，单位为毫秒。 |
| VER | 版本号。 如果field存在，和当前版本号做比较： 如果相等，继续操作，且版本号加1。 如果不相等，返回异常。 如果field不存在或者field当前版本为0，忽略传入的版本号并继续操作，成功后版本号变为 1。 |
| ABS | 绝对版本号，不论field是否存在，继续操作并将field的版本号设置为本参数所指定的值。 |
| NOACTIVE | 在指定EX、EXAT、PX或PXAT选项时，设置NOACTIVE表示该field不使用active expiration 策略，这样可以降低内存占用。 |

返回值 field存在且设置成功：1。 field不存在：0。 其它情况返回相应的异常信息。

**EXHEXPIREAT**

语法 EXHEXPIREAT <key> <field> <timestamp> [VER/ABS version] [NOACTIVE] 时间复杂度 O(1) 命令描述在key指定的TairHash中为一个field设置绝对过期时间，精确到秒。 参数及选项说明

| 参数或选项 | 说明 |
|---|---|
| key | TairHash的key，用于指定作为命令调用对象的TairHash。 |
| field | TairHash中的一个元素，一个TairHash key可以有多个field。 |

云数据库 Tair（兼容Redis）用户指

| timestamp | 精确到秒的时间戳。 |
|---|---|
| VER | 版本号。 如果field存在，和当前版本号做比较： 如果相等，继续操作，且版本号加1。 如果不相等，返回异常。 如果field不存在或者field当前版本为0，忽略传入的版本号并继续操作，成功后版本号变为 1。 |
| ABS | 绝对版本号，不论field是否存在，继续操作并将field的版本号设置为本参数所指定的值。 |
| NOACTIVE | 在指定EX、EXAT、PX或PXAT选项时，设置NOACTIVE表示该field不使用active expiration 策略，这样可以降低内存占用。 |

返回值 field存在且设置成功：1。 field不存在：0。 其它情况返回相应的异常信息。

**EXHEXPIRE**

语法 EXHEXPIRE <key> <field> <seconds> 时间复杂度 O(1) 命令描述在key指定的TairHash中为一个field设置相对过期时间，单位为秒。 参数及选项说明

| 参数或选项 | 说明 |
|---|---|
| key | TairHash的key，用于指定作为命令调用对象的TairHash。 |
| field | TairHash中的一个元素，一个TairHash key可以有多个field。 |
| seconds | 相对过期时间，单位为秒。 |
| VER | 版本号。 如果field存在，和当前版本号做比较： 如果相等，继续操作，且版本号加1。 如果不相等，返回异常。 如果field不存在或者field当前版本为0，忽略传入的版本号并继续操作，成功后版本号变为 1。 |
| ABS | 绝对版本号，不论field是否存在，继续操作并将field的版本号设置为本参数所指定的值。 |
| NOACTIVE | 在指定EX、EXAT、PX或PXAT选项时，设置NOACTIVE表示该field不使用active expiration 策略，这样可以降低内存占用。 |

返回值 field存在且设置成功：1。 云数据库 Tair（兼容Redis）用户指 field不存在：0。 其它情况返回相应的异常信息。

**EXHPTTL**

语法 EXHPTTL <key> <field> 时间复杂度 O(1) 命令描述查看key指定的TairHash中一个field的过期时间，结果精确到毫秒。 参数及选项说明

| 参数或选项 | 说明 |
|---|---|
| key | TairHash的key，用于指定作为命令调用对象的TairHash。 |
| field | TairHash中的一个元素，一个TairHash key可以有多个field。 |

返回值 key或者field不存在：-2。 field存在但是没有设置过期时间：-1。 field存在且设置了过期时间：过期时间，单位为毫秒。 其它情况返回相应的异常信息。

**EXHTTL**

语法 EXHTTL <key> <field> 时间复杂度 O(1) 命令描述查看key指定的TairHash中一个field的过期时间，结果精确到秒。 参数及选项说明

| 参数或选项 | 说明 |
|---|---|
| key | TairHash的key，用于指定作为命令调用对象的TairHash。 |
| field | TairHash中的一个元素，一个TairHash key可以有多个field。 |

返回值 key或者field不存在：-2。 field存在但是没有设置过期时间：-1。 field存在且设置了过期时间：过期时间，单位为秒。 其它情况返回相应的异常信息。

**EXHVER**

语法云数据库 Tair（兼容Redis）用户指 EXHVER <key> <field> 时间复杂度 O(1) 命令描述查看key指定的TairHash中一个field的版本号。 参数及选项说明

| 参数或选项 | 说明 |
|---|---|
| key | TairHash的key，用于指定作为命令调用对象的TairHash。 |
| field | TairHash中的一个元素，一个TairHash key可以有多个field。 |

返回值 key不存在：-1。 field不存：-2。 查询成功：field的版本号。 其它情况返回相应的异常信息。

**EXHSETVER**

语法 EXHSETVER <key> <field> <version> 时间复杂度 O(1) 命令描述设置key指定的TairHash中一个field的版本号。 参数及选项说明

| 参数或选项 | 说明 |
|---|---|
| key | TairHash的key，用于指定作为命令调用对象的TairHash。 |
| field | TairHash中的一个元素，一个TairHash key可以有多个field。 |

返回值 TairHash或者field不存在：0。 设置成功：1。 其它情况返回相应的异常信息。

**EXHINCRBY**

语法 EXHINCRBY <key> <field> <num> [EX time] [EXAT time] [PX time] [PXAT time] [VER/ABS version] [MIN minval] [MAX maxval] 时间复杂度 O(1) 命令描述云数据库 Tair（兼容Redis）用户指将key指定的TairHash中一个field的value增加num，num为一个整数。如果TairHash不存在则自动新创建一个，如果指定的field不存在，则在加之前插入该field并将其值设置为0。该命令会触发对field的被动淘汰检查。 参数及选项说明

| 参数或选项 | 说明 |
|---|---|
| key | TairHash的key，用于指定作为命令调用对象的TairHash。 |
| field | TairHash中的一个元素，一个TairHash key可以有多个field。 |
| num | 需要为field的value增加的整数值。 |
| EX | 指定field的相对过期时间，单位为秒，为0表示不过期。 |
| EXAT | 指定field的绝对过期时间，单位为秒，为0表示不过期。 |
| PX | 指定field的相对过期时间，单位为毫秒，为0表示不过期。 |
| PXAT | 指定field的绝对过期时间，单位为毫秒 ，为0表示不过期。 |
| VER | 版本号。 如果field存在，和当前版本号做比较： 如果相等，完成递增，且版本号加1。 如果不相等，返回异常。 如果VER选项所携带的版本号为0，则不进行版本校验。 |
| ABS | 绝对版本号，不论field是否存在，完成递增并将field的版本号设置为本参数所指定的值，该值不能为0。 |
| MIN | value的最小值，小于该值则提示异常。 |
| MAX | value的最大值，大于该值则提示异常。 |
| NOACTIVE | 在设置了EX、EXAT、PX或PXAT选项的同时，如果设置了NOACTIVE，则该field不使用 active expiration策略，内存占用较小。 |

为Key的field设置了超时时间后，再次执行该命令时如果没有设置超时时间，该field将

**说明**

被设置为永不过期。 返回值成功：与num相加后value的值。 其它情况返回异常。

**EXHINCRBYFLOAT**

语法 EXHINCRBYFLOAT <key> <field> <num> [EX time] [EXAT time] [PX time] [PXAT time] [VER/ABS version] [MIN minval] [MAX maxval] 时间复杂度 O(1) 命令描述云数据库 Tair（兼容Redis）用户指将key指定的TairHash中一个field的value增加num，num为一个浮点数。如果TairHash不存在则自动新创建一个，如果指定的field不存在，则在加之前插入该field并将其值设置为0。该命令会触发对field的被动淘汰检查。 参数及选项说明

| 参数或选项 | 说明 |
|---|---|
| key | TairHash的key，用于指定作为命令调用对象的TairHash。 |
| field | TairHash中的一个元素，一个TairHash key可以有多个field。 |
| num | 需要为field的value增加的值，类型为浮点。 |
| EX | 指定field的相对过期时间，单位为秒，为0表示不过期。 |
| EXAT | 指定field的绝对过期时间，单位为秒，为0表示不过期。 |
| PX | 指定field的相对过期时间，单位为毫秒，为0表示不过期。 |
| PXAT | 指定field的绝对过期时间，单位为毫秒 ，为0表示不过期。 |
| VER | 版本号。 如果field存在，和当前版本号做比较： 如果相等，完成递增，且版本号加1。 如果不相等，返回异常。 如果VER选项所携带的版本号为0，则不进行版本校验。 |
| ABS | 绝对版本号，不论field是否存在，完成递增并将field的版本号设置为本参数所指定的值，该值不能为0。 |
| MIN | value的最小值，小于该值则提示异常。 |
| MAX | value的最大值，大于该值则提示异常。 |
| NOACTIVE | 在设置了EX、EXAT、PX或PXAT选项的同时，如果设置了NOACTIVE，则该field不使用 active expiration策略，内存占用较小。 |

为Key的field设置了超时时间后，再次执行该命令时如果没有设置超时时间，该field将

**说明**

被设置为永不过期。 返回值成功：与num相加后value的值。 其它情况返回异常。

**EXHGETWITHVER**

语法 EXHGETWITHVER <key> <field> 时间复杂度 O(1) 命令描述同时获取key指定的TairHash一个field的值和版本。 参数及选项说明云数据库 Tair（兼容Redis）用户指

| 参数或选项 | 说明 |
|---|---|
| key | TairHash的key，用于指定作为命令调用对象的TairHash。 |
| field | TairHash中的一个元素，一个TairHash key可以有多个field。 |

返回值 field存在且操作成功：field对应的值和版本。 key不存在或者field不存在：nil。 其它情况返回相应的异常信息。

**EXHMGET**

语法 EXHMGET <key> <field> [field ...] 时间复杂度 O(1) 命令描述同时获取key指定的TairHash多个field的值。 参数及选项说明

| 参数或选项 | 说明 |
|---|---|
| key | TairHash的key，用于指定作为命令调用对象的TairHash。 |
| field | TairHash中的一个元素，一个TairHash key可以有多个field。 |

返回值 key不存在：nil。 key存在且查询的所有field都存在：返回一个数组，数组的每一个元素对应一个field的value。 key存在且查询的field中有不存在的：返回一个数组，数组的每一个元素对应一个field的value，不存在的field对应的元素显示为nil。 其它情况返回相应的异常信息。

**EXHMGETWITHVER**

语法 EXHMGETWITHVER <key> <field> [field ...] 时间复杂度 O(1) 命令描述同时获取key指定的TairHash多个field的值和版本。 参数及选项说明

| 参数或选项 | 说明 |
|---|---|
| key | TairHash的key，用于指定作为命令调用对象的TairHash。 |
| field | TairHash中的一个元素，一个TairHash key可以有多个field。 |

云数据库 Tair（兼容Redis）用户指返回值 key不存在：nil。 key存在且查询的所有field都存在：返回一个数组，数组的每一个元素对应一个field的value和 version。 key存在且查询的field中有不存在的：返回一个数组，数组的每一个元素对应一个field的value和 version，不存在的field对应的元素显示为nil。 其它情况返回相应的异常信息。

**EXHDEL**

语法 EXHDEL <key> <field> <field> <field> ... 时间复杂度 O(1) 命令描述删除key指定的TairHash一个field。 参数及选项说明

| 参数或选项 | 说明 |
|---|---|
| key | TairHash的key，用于指定作为命令调用对象的TairHash。 |
| field | TairHash中的一个元素，一个TairHash key可以有多个field。 |

返回值 key不存在或者field不存在：0。 删除成功：1。 其它情况返回相应的异常信息。

**EXHLEN**

语法 EXHLEN <key> [noexp] 时间复杂度 O(1) 命令描述获取key指定的TairHash中field的个数，结果中可能存在已经过期但还未被删除的field。 参数及选项说明

| 参数或选项 | 说明 |
|---|---|
| key | TairHash的key，用于指定作为命令调用对象的TairHash。 |
| noexp | EXHLEN默认不会触发对过期field的被动淘汰，也不会将其过滤掉，所以结果中可能包含已经过期但还未被删除的field。如果只想返回当前没有过期的field个数，可以在命令中设置noexp选项。在设置noexp时： 因为要遍历整条TairHash数据，EXHLEN命令的响应时间将受到Tairhash大小的影响。 EXHLEN命令的返回结果中会过滤掉过期的field，但过期field不会被淘汰。 |

返回值云数据库 Tair（兼容Redis）用户指 key不存在或者field不存在：0。 成功：field个数。 其它情况返回相应的异常信息。

**EXHEXISTS**

语法 EXHEXISTS <key> <field> 时间复杂度 O(1) 命令描述查询key指定的TairHash中是否存在对应的field。 参数及选项说明

| 参数或选项 | 说明 |
|---|---|
| key | TairHash的key，用于指定作为命令调用对象的TairHash。 |
| field | TairHash中的一个元素，一个TairHash key可以有多个field。 |

返回值 key不存在或者field不存在：0。 field存在：1。 其它情况返回相应的异常信息。

**EXHSTRLEN**

语法 EXHSTRLEN <key> <field> 时间复杂度 O(1) 命令描述获取key指定的TairHash中一个field的value的长度。 参数及选项说明

| 参数或选项 | 说明 |
|---|---|
| key | TairHash的key，用于指定作为命令调用对象的TairHash。 |
| field | TairHash中的一个元素，一个TairHash key可以有多个field。 |

返回值 key不存在或者field不存在：0。 查询成功：value的长度。 其它情况返回相应的异常信息。

**EXHKEYS**

语法 EXHKEYS <key> 云数据库 Tair（兼容Redis）用户指时间复杂度 O(1) 命令描述获取key指定的TairHash中所有field。 参数及选项说明

| 参数或选项 | 说明 |
|---|---|
| key | TairHash的key，用于指定作为命令调用对象的TairHash。 |

返回值 key不存在：返回一个空数组。 key存在：返回一个数组，数组的每一位对应TairHash中的每一个field。 其它情况返回相应的异常信息。

**EXHVALS**

语法 EXHVALS <key> 时间复杂度 O(1) 命令描述获取key指定的TairHash中所有field的value。 参数及选项说明

| 参数或选项 | 说明 |
|---|---|
| key | TairHash的key，用于指定作为命令调用对象的TairHash。 |

返回值 key不存在：返回一个空数组。 key存在：返回一个数组，数组的每个元素对应TairHash中的一个field的value。 其它情况返回相应的异常信息。

**EXHGETALL**

语法 EXHGETALL <key> 时间复杂度 O(1) 命令描述获取key指定的TairHash中所有field和value。 参数及选项说明

| 参数或选项 | 说明 |
|---|---|
| key | TairHash的key，用于指定作为命令调用对象的TairHash。 |

返回值云数据库 Tair（兼容Redis）用户指 key不存在：返回一个空数组。 key存在：返回一个数组，数组的每个元素对应TairHash中的一对field和value。 其它情况返回相应的异常信息。

**EXHSCAN**

语法 EXHSCAN <key> <op> <subkey> [MATCH pattern] [COUNT count] 时间复杂度 O(1)、O(N) 命令描述扫描key指定的TairHash。 参数及选项说明

| 参数或选项 | 说明 |
|---|---|
| key | TairHash的key，用于指定作为命令调用对象的TairHash。 |
| op | 用于定位扫描的起点，可选值： >，表示从第一个大于subkey的field开始。 >=，表示从第一个大于等于subkey的field开始。 <，表示从第一个小于subkey的field开始。 <=，表示从第一个小于等于subkey的field开始。 ==，表示从第一个等于subkey的field开始。 ^，表示从第一个field开始。 $，表示从最后一个field开始。 |
| subkey | 用于与op选项搭配，设置扫描起始位置，当op为^或$时该值将被忽略。 |
| MATCH | 用于过滤扫描结果。 |

返回值 key不存在：返回一个空数组。 key存在：返回一个数组，数组的每个元素对应TairHash中的一对field和value。 其它情况返回相应的异常信息。

### TairGIS命令

TairGis是一种使用R-Tree做索引，支持地理信息系统GIS（Geographic Information System）相关接口的数据结构。Redis的原生GEO命令是使用GeoHash和Redis Sorted Set结构完成的，主要用于点的查询，TairGIS在此基础上还支持线、面的查询，功能更加强大。

**前提条件**

Redis实例为企业版性能增强型。 操作对象为性能增强型实例中的TairGIS数据。

**主要特性**

使用R-Tree作为索引存储。 支持点、线、面的相关查询（含相交查询）。 云数据库 Tair（兼容Redis）用户指兼容Redis的原生GEO命令。

**命令列表**

|  |  |  |  | 命令 | 语法 |  | 说明 |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  | GIS.ADD <area> |  | 在area中添加指定名称的多边形（可添加多个），多边 |  |  |  |
|  |  |  |  |  |  | GIS.ADD <area> | 形使用WKT（Well-known text）格式描述。 |  |  |  |
|  |  |  |  |  | <polygonName> <polygonWkt> |  |  |  |  |  |
|  |  |  |  |  |  |  |  | 说明 |  |  |
|  |  |  |  | GIS.ADD |  |  |  |  |  |  |
|  |  |  |  |  | [<polygonName> <polygonWkt> |  |  |  |  |  |
|  |  |  |  |  | ...] |  |  |  |  |  |
|  |  |  |  |  | GIS.GET <area> <polygonName> |  | 在area中查找指定名称的多边形的WKT信息。 |  |  |  |
|  |  |  |  |  |  | GIS.GET <area> |  |  |  |  |
|  |  |  |  | GIS.GET | <polygonName> |  |  |  |  |  |
|  |  |  |  |  | GIS.GETALL <area> [WITHOUTWKT] |  | 返回一个area中所有多边形的名称和WKT信息。 |  |  |  |
|  |  |  |  |  |  | GIS.GETALL <area> | 返 |  |  |  |
|  |  |  |  | GIS.GETALL | [WITHOUTWKT] |  |  |  |  |  |
|  |  |  |  |  | GIS.DEL <area> <polygonName> |  | 删除area中指定名称的多边形。 |  |  |  |
|  |  |  |  |  |  | GIS.DEL <area> |  |  |  |  |
|  |  |  |  | GIS.DEL | <polygonName> |  |  |  |  |  |
|  |  |  |  | DEL | DEL <key> [key ...] |  | 原生Redis命令，可以删除一条或多条TairGIS数据。 |  |  |  |
|  |  |  |  | GIS.CONTAIN | GIS.CONTAINS <area> <polygonWkt> [WITHOUTWKT] |  | 判断指定的点、线或面是否包含在area中的某个多边形内。 |  |  |  |
|  |  |  |  |  |  | GIS.CONTAINS <area> | 判断指定的点、线或面 |  |  |  |
|  |  |  |  | S | <polygonWkt> [WITHOUTWKT] |  |  |  |  |  |
|  |  |  |  | GIS.INTERSEC | GIS.INTERSECTS <area> <polygonWkt> |  | 判断给定点、线或面，和area中包含的多边形的相交情况。 |  |  |  |
|  |  |  |  |  |  | GIS.INTERSECTS <area> | 判断给 |  |  |  |
|  |  |  |  | TS | <polygonWkt> |  |  |  |  |  |
|  |  |  |  |  | GIS.SEARCH [RADIUS |  |  |  |  |  |
|  |  |  |  |  |  | GIS.SEARCH [RADIUS |  |  |  |  |
|  |  |  |  |  | longitude latitude distance |  |  |  |  |  |
|  |  |  |  |  | m\|km\|ft\|mi] [MEMBER field |  |  |  |  |  |
|  |  |  |  | GIS.SEARCH | distance m\|km\|ft\|mi] [GEOM |  | 查找给定经纬度及距离为半径范围内的点。 |  |  |  |
|  |  |  |  |  | geom] [COUNT count] |  |  |  |  |  |
|  |  |  |  |  | [ASC\|DESC] [WITHDIST] |  |  |  |  |  |
|  |  |  |  |  | [WITHOUTWKT] |  |  |  |  |  |
|  |  |  |  |  | GIS.WITHIN <area> <polygonWkt> [WITHOUTWKT] |  | 在area中搜索指定多边形内部的点、线或面。 |  |  |  |
|  |  |  |  |  |  | GIS.WITHIN <area> | 在area中搜索指定多 |  |  |  |
|  |  |  |  | GIS.WITHIN | <polygonWkt> [WITHOUTWKT] |  |  |  |  |  |

云数据库 Tair（兼容Redis）用户指

**通用参数说明**

| 参数 | 说明 |  |
|---|---|---|
| area | 一个几何区域。 |  |
| PolygonName | 一个多边形的名称。 |  |
|  | 一个多边形的描述信息，使用WKT（Well-known text）描述，支持如下类型： POINT：描述一个点的WKT信息，例如 'POINT (30 11)' 。 LINESTRING：描述一条线的WKT信息，例如 'LINESTRING (30 10, 40 40)' 。 POLYGON：描述一个多边形的WKT信息，例如 'POLYGON ((31 20, 29 20, 29 21, 31 31))' 。 说明不支持MULTIPOINT、MULTILINESTRING、MULTIPOLYGON、GEOMETRY和 COLLECTION。 |  |
| polygonWkt | 31 31))' |  |
| WITHOUTWKT | 用于控制是否返回多边形的WKT信息。在使用GIS.GETALL、GIS.CONTAINS、GIS.SEARCH和GIS.WITHIN命令时，如果加上该参数，则不返回多边形的WKT信息。 |  |

**GIS.ADD**

语法 GIS.ADD <area> <polygonName> <polygonWkt> [<polygonName> <polygonWkt>...] 时间复杂度（用于表示命令执行时间随数据规模增长的变化趋势） O(log n) 命令描述在area中添加指定名称的多边形（可添加多个），使用WKT（Well-known text）描述。 返回值成功：返回插入和更新成功的个数。 其它情况：返回相应的异常信息。 使用示例

```
127.0.0.1:6379> GIS.ADD hangzhou campus 'POLYGON ((30 10, 40 40, 20 40, 10 20, 30 10)
```

`)'`

```
(integer) 1
```

**GIS.GET**

语法

```
GIS.GET <area> <polygonName>
```

云数据库 Tair（兼容Redis）用户指时间复杂度 O(1) 命令描述在area中查找指定名称的多边形的WKT信息。 返回值成功：返回查询到的WKT。 area或polygonName不存在：返回nil。 其它情况：返回相应的异常信息。 使用示例

```
127.0.0.1:6379> GIS.ADD hangzhou campus 'POLYGON ((30 10, 40 40, 20 40, 10 20, 30 10)
```

`)'`

```
(integer) 1 127.0.0.1:6379> GIS.GET hangzhou campus "POLYGON((30 10,40 40,20 40,10 20,30 10))" 127.0.0.1:6379> GIS.GET hangzhou not-exists (nil) 127.0.0.1:6379> GIS.GET not-exists campus (nil)
```

**GIS.GETALL**

语法

```
GIS.GETALL <area> [WITHOUTWKT]
```

时间复杂度 O(n) 命令描述返回一个area中所有多边形的名称和WKT信息。如果设置了WITHOUTWKT选项，仅返回多边形的名称。 返回值成功：返回多边形的名称和WKT信息。如果设置了WITHOUTWKT选项，仅返回多边形的名称。 未查询到：返回nil。 其它情况：返回相应的异常信息。 使用示例

```
127.0.0.1:6379> GIS.ADD hangzhou campus 'POLYGON ((30 10, 40 40, 20 40, 10 20, 30 10)
```

`)'`

```
(integer) 1 127.0.0.1:6379> GIS.GETALL hangzhou
1) "campus"
2) "POLYGON((30 10,40 40,20 40,10 20,30 10))"
127.0.0.1:6379> GIS.GETALL hangzhou WITHOUTWKT
1) "campus"
```

**GIS.DEL**

语法云数据库 Tair（兼容Redis）用户指 GIS.DEL <area> <polygonName> 时间复杂度 O(log n) 命令描述删除area中指定名称的多边形。 返回值成功：OK。 area或polygonName不存在：返回nil。 其它情况：返回相应的异常信息。 使用示例

```
127.0.0.1:6379> GIS.ADD hangzhou campus 'POLYGON ((30 10, 40 40, 20 40, 10 20, 30 10)
```

`)'`

```
(integer) 1 127.0.0.1:6379> GIS.GET hangzhou campus "POLYGON((30 10,40 40,20 40,10 20,30 10))" 127.0.0.1:6379> GIS.DEL hangzhou not-exists (nil) 127.0.0.1:6379> GIS.DEL not-exists campus (nil) 127.0.0.1:6379> GIS.DEL hangzhou campus
```

`OK`

```
127.0.0.1:6379> GIS.GET hangzhou campus (nil)
```

**GIS.CONTAINS**

语法 GIS.CONTAINS <area> <polygonWkt> 时间复杂度最理想情况： 最差情况：log(n) 命令描述判断指定的点、线或面是否包含在area中的某个多边形内。 返回值成功：返回包含指定点、线或面的多边形的名称和WKT信息。如果设置了WITHOUTWKT选项，仅返回多边形的名称。 未查询到：返回nil。 其它情况：返回相应的异常信息。 使用示例云数据库 Tair（兼容Redis）用户指

```
127.0.0.1:6379> GIS.ADD hangzhou campus 'POLYGON ((30 10, 40 40, 20 40, 10 20, 30 10)
```

`)'`

```
(integer) 1 127.0.0.1:6379> GIS.CONTAINS hangzhou 'POINT (30 11)'
1) "0"
2) 1) "campus"
   2) "POLYGON((30 10,40 40,20 40,10 20,30 10))"
127.0.0.1:6379> GIS.CONTAINS hangzhou 'LINESTRING (30 10, 40 40)'
1) "0"
2) 1) "campus"
   2) "POLYGON((30 10,40 40,20 40,10 20,30 10))"
127.0.0.1:6379> GIS.CONTAINS hangzhou 'POLYGON ((31 20, 29 20, 29 21, 31 31))'
1) "0"
2) 1) "campus"
   2) "POLYGON((30 10,40 40,20 40,10 20,30 10))"
```

**GIS.INTERSECTS**

语法 GIS.INTERSECTS <area> <polygonWkt> 时间复杂度最理想情况： 最差情况：log(n) 命令描述判断指定的点、线或面，与area中的某个多边形的相交情况。 返回值成功：返回与指定点、线或面相交的多边形的名称和WKT信息。 未查询到：返回nil。 其它情况：返回相应的异常信息。 使用示例云数据库 Tair（兼容Redis）用户指

```
127.0.0.1:6379> GIS.ADD hangzhou campus 'POLYGON ((30 10, 40 40, 20 40, 10 20, 30 10)
```

`)'`

```
(integer) 1 127.0.0.1:6379> GIS.INTERSECTS hangzhou 'POINT (30 11)'
1) "0"
2) 1) "campus"
   2) "POLYGON((30 10,40 40,20 40,10 20,30 10))"
127.0.0.1:6379> GIS.INTERSECTS hangzhou 'LINESTRING (30 10, 40 40)'
1) "0"
2) 1) "campus"
   2) "POLYGON((30 10,40 40,20 40,10 20,30 10))"
127.0.0.1:6379> GIS.INTERSECTS hangzhou 'POLYGON ((30 10, 40 40, 20 40, 10 20, 30 10)
```

`)'`

```
1) "0"
2) 1) "campus"
   2) "POLYGON((30 10,40 40,20 40,10 20,30 10))"
127.0.0.1:6379>
```

**GIS.SEARCH**

语法

```
GIS.SEARCH [RADIUS longitude latitude distance m|km|ft|mi] [MEMBER field distance m|km|ft|mi] [GEOM geom] [COUNT count] [ASC|DESC] [WITHDIST] [WITHOUTWKT]
```

时间复杂度最理想情况： 最差情况：log(n) 命令描述查找给定经纬度及距离为半径范围内的点，支持下述可选参数： RADIUS：按照参数传递的经度、纬度和半径搜索，取值顺序为经度、纬度、半径、半径单位，例

```
如 RADIUS 15 37 200 km 。
```

MEMBER：从已经存在的多边形中获取经纬度并根据半径搜索，取值顺序为多边形名称、半径、半径单位，例如 `MEMBER Agrigento 100 km` 。 GEOM：按照WKT的格式设置搜索范围，可以是任意多边形，例如 `GIS.SEARCH Sicily "POINT`

```
(13.361389 38.115556)" 。
```

COUNT：用于限定返回的个数，例如 `COUNT 3` 。 ASC|DESC：用于控制返回信息按照距离排序，例如ASC表示根据中心位置，由近到远排序。 WITHDIST：用于控制是否返回距离。 WITHOUTWKT：用于控制是否返回多边形的WKT信息。 返回值成功：返回查询到的多边形名称和WKT信息。 云数据库 Tair（兼容Redis）用户指未查询到：返回nil。 其它情况：返回相应的异常信息。 使用示例

```
127.0.0.1:6379> GIS.ADD Sicily "Palermo" "POINT (13.361389 38.115556)" "Catania" "POI NT(15.087269 37.502669)" (integer) 2 127.0.0.1:6379> GIS.SEARCH Sicily RADIUS 15 37 200 km WITHDIST
1) "2"
2) 1) "Palermo"
   2) "POINT(13.361389 38.115556)"
   3) "190.4424"
   4) "Catania"
   5) "POINT(15.087269 37.502669)"
   6) "56.4413"
127.0.0.1:6379> GIS.SEARCH Sicily RADIUS 15 37 200 km WITHDIST WITHOUTWKT
1) "2"
2) 1) "Palermo"
   2) "190.4424"
   3) "Catania"
   4) "56.4413"
127.0.0.1:6379> GIS.SEARCH Sicily RADIUS 15 37 200 km WITHDIST WITHOUTWKT ASC
1) "2"
2) 1) "Catania"
   2) "56.4413"
   3) "Palermo"
   4) "190.4424"
127.0.0.1:6379> GIS.SEARCH Sicily RADIUS 15 37 200 km WITHDIST WITHOUTWKT ASC COUNT 1
1) "2"
2) 1) "Catania"
   2) "56.4413"
127.0.0.1:6379> GIS.ADD Sicily "Agrigento" "POINT (13.583333 37.316667)" (integer) 1 127.0.0.1:6379> GIS.SEARCH Sicily MEMBER Agrigento 100 km
1) "2"
2) 1) "Palermo"
   2) "POINT(13.361389 38.115556)"
   3) "Agrigento"
   4) "POINT(13.583333 37.316667)"
```

**GIS.WITHIN**

语法

```
GIS.WITHIN <area> <polygonWkt> [WITHOUTWKT]
```

时间复杂度最理想情况： 最差情况：log(n) 命令描述云数据库 Tair（兼容Redis）用户指在area中搜索指定的多边形内部的点、线或面。如果设置了WITHOUTWKT选项，仅返回多边形的名称。 返回值成功：成功则返回对应多边形的名称和WKT信息。 未查找到：返回null。 其它情况：返回相应的异常信息。 使用示例

```
127.0.0.1:6379> GIS.ADD hangzhou campus 'POINT (30 10)' (integer) 1 127.0.0.1:6379> GIS.ADD hangzhou campus1 'LINESTRING (30 10, 40 40)' (integer) 1 127.0.0.1:6379> GIS.WITHIN hangzhou 'POLYGON ((30 10, 40 40, 20 40, 10 20, 30 10))'
1) "2"
2) 1) "campus"
   2) "POINT(30 10)"
   3) "campus1"
   4) "LINESTRING(30 10,40 40)"
```

### TairBloom命令

本文介绍TairBloom数据支持的命令。

**TairBloom简介**

TairBloom是一种可动态扩容的布隆过滤器。TairBloom首先是一种概率性数据结构（space-efficient probabilistic data structure），主要使用较低的内存消耗来判断一个元素是否存在；其次，TairBloom 具有动态扩容的能力，可在扩容的同时维持误判率的稳定。 在传统的Redis数据结构中，可以使用Hash、Set、String的Bitset等实现类似功能，但这些实现方式不是内存占用量非常大，就是无法动态伸缩和保持误判率不变。因此，TairBloom非常适合需要高效判断大量数据是否存在且允许一定误判率的业务场景。业务可以直接使用TairBloom提供的Bloom Filter接口，无需二次封装，更无需在本地实现布隆过滤器的功能。 主要特性： 内存占用低。 可动态扩容。 可自定义的误判率（False Positive Rate）且在扩容时保持不变。

**使用前提**

请注意，本文介绍的命令只有在满足以下条件时才能生效。 Redis实例为企业版性能增强型。 操作对象为性能增强型实例中的TairBloom数据。

**命令列表**

| 命令 | 语法 | 说明 |
|---|---|---|
| BF.RESERVE | BF.RESERVE <key> <error rate> <capacity> _ | 创建一个大小为capacity，错误率为error rate的空的 _ TairBloom。 |
| BF.ADD | BF.ADD <key> <item> | 在key指定的TairBloom中添加一个元素item。 |

云数据库 Tair（兼容Redis）用户指

| BF.MADD | BF.MADD <key> <item> [item...] | 在key指定的TairBloom中一次性添加多个元素。 |
|---|---|---|
| BF.EXISTS | BF.EXISTS <key> <item> | 检查一个元素是否存在于key指定的TairBloom中。 |
| BF.MEXISTS | BF.MEXISTS <key> <item> [item...] | 同时检查多个元素是否存在于key指定的TairBloom中。 |
| BF.INSERT | BF.INSERT <key> [CAPACITY cap] [ERROR error] [NOCREATE] ITEMS <item...> | 在key指定的TairBloom中一次性添加多个元素，添加时可以指定大小和错误率，且可以控制在TairBloom不存在的时候是否自动创建。 |
| BF.DEBUG | BF.DEBUG <key> | 可以查看key指定的TairBloom内部信息，如当前层数和每一层的元素个数、错误率等。 |
| DEL | DEL <key> [key ...] | 使用原生Redis的DEL命令可以删除一条或多条 TairBloom数据。 说明已加入TairBloom数据中的元素无法单独删除，您可以使用DEL命令删除整条 TairBloom数据。 |

**BF.RESERVE**

语法 BF.RESERVE <key> <error_rate> <capacity> 时间复杂度 O(1) 命令描述创建一个大小为capacity，错误率为error_rate的空的TairBloom。 参数及选项说明

| 参数或选项 | 说明 |
|---|---|
| key | TairBloom的key，用于指定作为命令调用对象的TairBloom。 |
| error rate _ | 期望的错误率（False Positive Rate），该值必须介于0和1之间。该值越小，TairBloom的内存占用量越大，CPU使用率越高。 |
| capacity | TairBloom的初始容量，即期望添加到TairBloom中的元素的个数。 当实际添加的元素个数超过该值时，TairBloom将进行自动的扩容，该过程会导致性能有所下降，下降的程度是随着元素个数的指数级增长而线性下降的，这是因为TairBloom的扩容是通过增加Bloom Filter的层数来完成的。每增加一层，在查询的时候就可能会遍历多层Bloom Filter来完成，每一层的容量都是上一层的两倍。因此，如果对性能非常的敏感，需要在使用前充分评估要添加到TairBloom的元素个数，避免发生扩容操作。 |

返回值成功：OK。 其它情况返回相应的异常信息。

**BF.ADD**

语法 BF.ADD <key> <item> 云数据库 Tair（兼容Redis）用户指时间复杂度 O(log N) ，其中N是TairBloom的层数。 命令描述在key指定的TairBloom中添加一个元素。 参数及选项说明

| 参数或选项 | 说明 |
|---|---|
| key | TairBloom的key，用于指定作为命令调用对象的TairBloom。 |
| item | 需要添加到TairBloom的元素。 |

返回值元素一定不存在：1。 元素可能已经存在：0。 其它情况返回相应的异常信息。

**BF.MADD**

语法 BF.MADD <key> <item> [item...] 时间复杂度 O(log N) ，其中N是TairBloom的层数。 命令描述在key指定的TairBloom中添加多个元素。 参数及选项说明

| 参数或选项 | 说明 |
|---|---|
| key | TairBloom的key，用于指定作为命令调用对象的TairBloom。 |
| item | 需要添加到TairBloom的元素，可设置多个。 |

返回值成功：返回一个数组，数组的每一个元素可能为1或0，当item一定不存在时数组元素值为1，当item 可能已经存在时数组元素值为0。 其它情况返回相应的异常信息。

**BF.EXISTS**

语法 BF.EXISTS <key> <item> 时间复杂度 O(log N) ，其中N是TairBloom的层数。 命令描述检查一个元素是否存在于key指定的TairBloom中。 参数及选项说明

| 参数或选项 | 说明 |
|---|---|

云数据库 Tair（兼容Redis）用户指

| key | TairBloom的key，用于指定作为命令调用对象的TairBloom。 |
|---|---|
| item | 需要查询的元素。 |

返回值元素一定不存在：0。 元素可能存在：1。 其它情况返回相应的异常信息。

**BF.MEXISTS**

语法 BF.MEXISTS <key> <item> [item...] 时间复杂度 O(log N) ，其中N是TairBloom的层数。 命令描述同时检查多个元素是否存在于key指定的TairBloom中。 参数及选项说明

| 参数或选项 | 说明 |
|---|---|
| key | TairBloom的key，用于指定作为命令调用对象的TairBloom。 |
| item | 需要查询的元素，可设置多个。 |

返回值成功：返回一个数组，数组的每一个元素可能为1或0，当item一定不存在时数组元素值为0，当item 可能已经存在时数组元素值为1。 其它情况返回相应的异常信息。

**BF.INSERT**

语法 BF.INSERT <key> [CAPACITY cap] [ERROR error] [NOCREATE] ITEMS <item...> 时间复杂度 O(log N) ，其中N是TairBloom的层数。 命令描述在key指定的TairBloom中一次性添加多个元素，添加时可以指定大小和错误率，且可以控制在 TairBloom不存在的时候是否自动创建。 参数及选项说明

| 参数或选项 | 说明 |
|---|---|
| key | TairBloom的key，用于指定作为命令调用对象的TairBloom。 |

云数据库 Tair（兼容Redis）用户指

| CAPACITY | 指定TairBloom的容量，即期望添加到TairBloom中的元素的个数，当TairBloom已经存在时该值将被忽略。 当实际添加的元素个数超过该值时，TairBloom将进行自动的扩容，该过程会导致性能有所下降，下降的程度是随着元素个数的指数级增长而线性下降的，这是因为TairBloom的扩容是通过增加Bloom Filter的层数来完成的。每增加一层，在查询的时候就可能会遍历多层Bloom Filter来完成，每一层的容量都是上一层的两倍。因此，如果对性能非常的敏感，需要在使用前充分评估要添加到TairBloom的元素个数，避免发生扩容操作。 |
|---|---|
| ERROR | 期望的错误率（False Positive Rate），当TairBloom已经存在时该值将被忽略。该值必须介于0和1之间。该值越小，TairBloom的内存占用量越大，CPU使用率越高。 |
| NOCREATE | 设置该选项后，当指定的TairBloom不存在的时候不要自动创建该TairBloom。该参数不能与 CAPACITY和ERROR同时设置。 |
| ITEMS | 需要添加到TairBloom中的所有元素。 |

返回值成功：返回一个数组，数组的每一个元素可能为1或0，当item一定不存在时数组元素为1，当item可能已经存在时数组元素值为0。 其它情况返回相应的异常信息。

**BF.DEBUG**

语法 BF.DEBUG <key> 时间复杂度 O(log N) ，其中N是TairBloom的层数。 命令描述可以查看key指定的TairBloom内部信息，如当前层数和每一层的元素个数、错误率等。 参数及选项说明

| 参数或选项 | 说明 |
|---|---|
| key | TairBloom的key，用于指定作为命令调用对象的TairBloom。 |

返回值成功：返回一个数组，数组的每一个元素可能为1或0，当item一定不存在时数组元素为1，当item可能已经存在时数组元素值为0。 其它情况返回相应的异常信息。

**内存占用测试结果**

| 容量（元素的个数） | false positive:0.01 | false positive:0.001 | false positive:0.0001 |
|---|---|---|---|
| 100000 | 0.12 MB | 0.25 MB | 0.25 MB |
| 1000000 | 2 MB | 2 MB | 4 MB |
| 10000000 | 16 MB | 32 MB | 32 MB |
| 100000000 | 128 MB | 256 MB | 256 MB |

云数据库 Tair（兼容Redis）用户指

| 1000000000 | 2 GB | 2 GB | 4 GB |
|---|---|---|---|

### TairDoc命令

本文介绍TairDoc数据支持的命令。

**TairDoc简介**

TairDoc是一种文档数据结构，支持JSON数据的增删改查。 主要特性： 完整地支持JSON标准。 完全兼容RedisJSON。 支持JSONPointer和JSONPath两种语法。 文档作为二进制树存储，可以快速访问JSON数据的子元素。 支持JSON到XML或YAML格式的转换。

**使用前提**

请注意，本文介绍的命令只有在满足以下条件时才能生效。 Redis实例为企业版性能增强型。 操作对象为性能增强型实例中的TairDoc数据。

**命令列表**

| 命令 | 语法 | 说明 |
|---|---|---|
| JSON.SET | JSON.SET <key> <path> <json> [NX or XX] | 存储JSON的值在key的path中。对于不存在的 key，path必须是root。对于已经存在的key，当path 存在时，替换掉目前的JSON值。 |
| JSON.GET | JSON.GET <key> [PATH] [FORMAT <XML/YAML>] [ROOTNAME <root>] [ARRNAME <arr>] | 获取一个TairDoc在path中存储的JSON数据。 |
| JSON.DEL | JSON.DEL <key> [path] | 删除path对应的JSON数据。如果未指定path，则删除 key。不存在的key和不存在的path将会被忽略。 |
| JSON.TYPE | JSON.TYPE <key> [path] | 获取path对应的值的类型。 |
| JSON.NUMINC RBY | JSON.NUMINCRBY <key> [path] <value> | 将path对应的值增加value。path必须存在且path对应的值和value必须是都是int或double类型的值。 |
| JSON.STRAPP END | JSON.STRAPPEND <key> [path] <json-string> | 将json-string中的字符串添加到path对应的字符串类型的值中。如果未设置path，默认为root。 |
| JSON.STRLEN | JSON.STRLEN <key> [path] | 获取path对应值的长度。如果未设置path，默认为 root。 |
| JSON.ARRAPP END | JSON.ARRAPPEND <key> <path> <json> [<json> ...] | 将JSON插入到path对应的array最后，JSON可以是多个。 |
| JSON.ARRPOP | JSON.ARRPOP <key> <path> [index] | 移除并返回path对应的数组中index位置的元素。 |

云数据库 Tair（兼容Redis）用户指

| JSON.ARRINS ERT | JSON.ARRINSERT <key> <path> <index> <json> [<json> ...] | 将JSON插入到path对应的数组中，原有元素会往后移动。 |
|---|---|---|
| JSON.ARRLEN | JSON.ARRLEN <key> [path] | 获取path对应数组的长度。 |
| JSON.ARRTRI M | JSON.ARRTRIM <key> <path> <start> <stop> | 按照start和stop指定的范围修剪数组。 |
| DEL | DEL <key> [key ...] | 使用原生Redis的DEL命令可以删除一条或多条TairDoc 数据。 |

**JSON.SET**

语法 JSON.SET <key> <path> <json> [NX | XX] 时间复杂度 O(N) 命令描述存储JSON的值在key的path中。对于不存在的key，path必须是root。对于已经存在的key，当path存在时，替换掉目前的JSON值。 参数及选项说明

| 参数或选项 | 说明 |
|---|---|
| key | TairDoc的key，用于指定作为命令调用对象的TairDoc。 |
| path | TairDoc的path。 如果key不存在，path必须为root。 如果key存在，当path存在时，替换当前的JSON值。 |
| json | 如果key存在，当path存在时，用JSON替换TairDoc中当前的JSON数据。 |
| NX | 当path不存在时写入。 |
| XX | 当path存在时写入。 |

返回值成功：OK。 指定了NX或XX时失败：null。 其它情况返回相应的异常信息。 使用示例云数据库 Tair（兼容Redis）用户指

```
127.0.0.1:6379> JSON.SET doc . '{"foo": "bar", "baz" : 42}'
```

`OK`

```
127.0.0.1:6379> JSON.SET doc .foo '"flower"'
```

`OK`

```
127.0.0.1:6379> JSON.GET doc .foo "flower" 127.0.0.1:6379> JSON.SET doc .not-exists 123 XX 127.0.0.1:6379> JSON.SET doc .not-exists 123 NX
```

`OK`

```
127.0.0.1:6379> JSON.GET doc .not-exists
```

**JSON.GET**

语法 JSON.GET <key> <path> [FORMAT <XML | YAML>] [ROOTNAME <root>] [ARRNAME <arr>] 时间复杂度 O(N) 命令描述获取一个TairDoc在path中存储的JSON数据。 参数及选项说明

| 参数或选项 | 说明 |
|---|---|
| key | TairDoc的key，用于指定作为命令调用对象的TairDoc。 |
| path | TairDoc的path。 |
| FORMAT | 指定返回的JSON格式，支持XML或YAML。 |
| ROOTNAME | 指定XML语法ROOT元素的标签。 |
| ARRNAME | 指定XML语法ARRAY元素的标签。 |

返回值成功：返回path中存储的JSON。 其它情况返回相应的异常信息。 使用示例云数据库 Tair（兼容Redis）用户指

```
127.0.0.1:6379> JSON.SET doc . '{"foo": "bar", "baz" : 42}'
```

`OK`

```json
127.0.0.1:6379> JSON.GET doc {"foo":"bar","baz":42} 127.0.0.1:6379> JSON.GET doc .foo "bar" 127.0.0.1:6379> JSON.GET doc .not-exists ERR pointer illegal or array index error or object type is not array or map 127.0.0.1:6379> JSON.GET doc . format xml <?xml version="1.0" encoding="UTF-8"?><root><foo>bar</foo><baz>42</baz></root> 127.0.0.1:6379> JSON.GET doc . format xml rootname ROOT arrname ARRAY <?xml version="1.0" encoding="UTF-8"?><ROOT><foo>bar</foo><baz>42</baz></ROOT> 127.0.0.1:6379> JSON.GET doc . format yaml foo: bar baz: 42
```

**JSON.DEL**

语法 JSON.DEL <key> [path] 时间复杂度 O(N) 命令描述删除path对应的JSON数据。如果未指定path，则删除key。不存在的key和不存在的path将会被忽略。 参数及选项说明

| 参数或选项 | 说明 |
|---|---|
| key | TairDoc的key，用于指定作为命令调用对象的TairDoc。 |
| path | TairDoc的path。 |

返回值成功：1。 失败：0。 其它情况返回相应的异常信息。 使用示例云数据库 Tair（兼容Redis）用户指

```
127.0.0.1:6379> JSON.SET doc . '{"foo": "bar", "baz" : 42}'
```

`OK`

```json
127.0.0.1:6379> JSON.DEL doc .foo 127.0.0.1:6379> JSON.DEL doc .not-exists ERR old item is null for remove or replace 127.0.0.1:6379> JSON.DEL not-exists 127.0.0.1:6379> JSON.GET doc {"baz":42} 127.0.0.1:6379> JSON.DEL doc 127.0.0.1:6379> JSON.GET doc 127.0.0.1:6379>
```

**JSON.TYPE**

语法 JSON.TYPE <key> [path] 时间复杂度 O(N) 命令描述获取path对应的值的类型。 参数及选项说明

| 参数或选项 | 说明 |
|---|---|
| key | TairDoc的key，用于指定作为命令调用对象的TairDoc。 |
| path | TairDoc的path。 |

返回值成功：返回查询到的类型，可能的结果包括"boolean"、"null"、 "number"、"string"、"array"、 "object"、"raw"、"reference"、"const"。 key或者path不存在：null。 其它情况返回相应的异常信息。 使用示例

```
127.0.0.1:6379> JSON.SET doc . '{"foo": "bar", "baz" : 42}'
```

`OK`

```
127.0.0.1:6379> JSON.TYPE doc object 127.0.0.1:6379> JSON.TYPE doc .foo 127.0.0.1:6379> JSON.TYPE doc .baz number 127.0.0.1:6379> JSON.TYPE doc .not-exists 127.0.0.1:6379>
```

云数据库 Tair（兼容Redis）用户指

**JSON.NUMINCRBY**

语法 JSON.NUMINCRBY <key> [path] <value> 时间复杂度 O(N) 命令描述将path对应的值增加value。path必须存在且path对应的值和value必须是都是int或double类型的值。 参数及选项说明

| 参数或选项 | 说明 |
|---|---|
| key | TairDoc的key，用于指定作为命令调用对象的TairDoc。 |
| path | TairDoc的path。 |
| value | 需要为path的值增加的数值。 |

返回值成功：返回操作完成后path对应的值。 其它情况返回相应的异常信息。 使用示例

```
127.0.0.1:6379> JSON.SET doc . '{"foo": "bar", "baz" : 42}'
```

`OK`

```
127.0.0.1:6379> JSON.NUMINCRBY doc .baz 1 127.0.0.1:6379> JSON.NUMINCRBY doc .baz 1.5 44.5 127.0.0.1:6379> JSON.NUMINCRBY doc .foo 1 ERR node not exists or not number type 127.0.0.1:6379> JSON.NUMINCRBY doc .not-exists 1 ERR node not exists or not number type 127.0.0.1:6379>
```

**JSON.STRAPPEND**

语法 JSON.STRAPPEND <key> [path] <json-string> 时间复杂度 O(N) 命令描述将json-string中的字符串添加到path对应的字符串类型的值中。如果未设置path，默认为root。 参数及选项说明

| 参数或选项 | 说明 |
|---|---|
| key | TairDoc的key，用于指定作为命令调用对象的TairDoc。 |

云数据库 Tair（兼容Redis）用户指

| path | TairDoc的path。 |
|---|---|
| json-string | 需要添加到path对应值的字符串。 |

返回值成功：返回path对应的字符串扩展后的长度。 key不存在：-1。 其它情况返回相应的异常信息。 使用示例

```
127.0.0.1:6379> JSON.SET doc . '{"foo": "bar", "baz" : 42}'
```

`OK`

```
127.0.0.1:6379> JSON.STRAPPEND doc .foo rrrrr 127.0.0.1:6379> JSON.GET doc .foo "barrrrrr" 127.0.0.1:6379> JSON.STRAPPEND doc .not-exists ERR node not exists or not string type 127.0.0.1:6379> JSON.STRAPPEND not-exists abc
```

`-1`

**JSON.STRLEN**

语法 JSON.STRLEN <key> [path] 时间复杂度 O(N) 命令描述获取path对应值的长度。如果未设置path，默认为root。 参数及选项说明

| 参数或选项 | 说明 |
|---|---|
| key | TairDoc的key，用于指定作为命令调用对象的TairDoc。 |
| path | TairDoc的path。 |

返回值成功：返回path对应值的长度。 key不存在：-1。 其它情况返回相应的异常信息。 使用示例云数据库 Tair（兼容Redis）用户指

```
127.0.0.1:6379> JSON.SET doc . '{"foo": "bar", "baz" : 42}'
```

`OK`

```
127.0.0.1:6379> JSON.STRLEN doc .foo 127.0.0.1:6379> JSON.STRLEN doc .baz ERR node not exists or not string type 127.0.0.1:6379> JSON.STRLEN not-exists
```

`-1`

**JSON.ARRAPPEND**

语法 JSON.ARRAPPEND <key> <path> <json> [<json> ...] 时间复杂度 O(M*N)，M是需要插入的元素（json）数量，N是数组元素数量。 命令描述将JSON插入到path对应的array最后，JSON可以是多个。 参数及选项说明

| 参数或选项 | 说明 |
|---|---|
| key | TairDoc的key，用于指定作为命令调用对象的TairDoc。 |
| path | TairDoc的path。 |
| json | 需要插入的数据。 |

返回值成功：返回操作完成后array中元素数量。 key不存在：-1。 其它情况返回相应的异常信息。 使用示例

```
127.0.0.1:6379> JSON.SET doc . '{"id": [1,2,3]}'
```

`OK`

```
127.0.0.1:6379> JSON.GET doc .id [1,2,3] 127.0.0.1:6379> JSON.ARRAPPEND doc .id null false true 127.0.0.1:6379> JSON.GET doc .id [1,2,3,null,false,true] 127.0.0.1:6379> JSON.GET doc .id.2 127.0.0.1:6379> JSON.ARRAPPEND not-exists .a 1
```

`-1`

**JSON.ARRPOP**

语法 JSON.ARRPOP <key> <path> [index] 云数据库 Tair（兼容Redis）用户指时间复杂度 O(M*N)，M是key包含的子元素，N是数组元素数量。 命令描述移除并返回path对应的数组中index位置的元素。 参数及选项说明

| 参数或选项 | 说明 |
|---|---|
| key | TairDoc的key，用于指定作为命令调用对象的TairDoc。 |
| path | TairDoc的path。 |
| index | 数组的索引，不传默认为最后一个元素，负数表示反向取值。 |

返回值成功：返回数组相应的节点。 数组为空数组：‘ERR array index outflow’。 其它情况返回相应的异常信息。 使用示例

```
127.0.0.1:6379> JSON.SET doc . '{"id": [1,2,3]}'
```

`OK`

```
127.0.0.1:6379> JSON.ARRPOP doc .id 1 127.0.0.1:6379> JSON.GET doc .id [1,3] 127.0.0.1:6379> JSON.ARRPOP doc .id -1 127.0.0.1:6379> JSON.GET doc .id [1] 127.0.0.1:6379> JSON.ARRPOP doc .id 10 ERR array index outflow 127.0.0.1:6379> JSON.ARRPOP doc .id 127.0.0.1:6379> JSON.ARRPOP doc .id ERR array index outflow 127.0.0.1:6379>
```

**JSON.ARRINSERT**

语法 JSON.ARRINSERT <key> <path> <index> <json> [<json> ...] 时间复杂度 O(M*N)，M是要插入的元素（json）数量，N是数组元素数量。 命令描述将JSON插入到path对应的数组中，原有元素会往后移动。 参数及选项说明云数据库 Tair（兼容Redis）用户指

| 参数或选项 | 说明 |
|---|---|
| key | TairDoc的key，用于指定作为命令调用对象的TairDoc。 |
| path | TairDoc的path。 |
| index | 数组的索引，不传默认为最后一个元素，负数表示反向取值。 |
| json | 需要插入的数据。 |

返回值成功：返回操作完成后数组中元素的个数。 数组为空数组：‘ERR array index outflow’。 其它情况返回相应的异常信息。 使用示例

```
127.0.0.1:6379> JSON.SET doc . '{"id": [2,3,5]}'
```

`OK`

```
127.0.0.1:6379> JSON.ARRINSERT doc .id 0 0 1 127.0.0.1:6379> JSON.GET doc .id [0,1,2,3,5] 127.0.0.1:6379> JSON.ARRINSERT doc .id 4 4 127.0.0.1:6379> JSON.GET doc .id [0,1,2,3,4,5] 127.0.0.1:6379>
```

**JSON.ARRLEN**

语法 JSON.ARRLEN <key> [path] 时间复杂度 O(N) 命令描述获取path对应数组的长度。 参数及选项说明

| 参数或选项 | 说明 |
|---|---|
| key | TairDoc的key，用于指定作为命令调用对象的TairDoc。 |
| path | TairDoc的path。 |

返回值成功：数组的长度。 key不存在：-1。 其它情况返回相应的异常信息。 使用示例云数据库 Tair（兼容Redis）用户指

```
127.0.0.1:6379> JSON.SET doc . '{"id": [2,3,5]}'
```

`OK`

```
127.0.0.1:6379> JSON.ARRLEN doc .id 127.0.0.1:6379> JSON.ARRLEN not-exists
```

`-1`

**JSON.ARRTRIM**

语法 JSON.ARRTRIM <key> <path> <start> <stop> 时间复杂度 O(N) 命令描述按照start和stop指定的范围修剪数组。 参数及选项说明

| 参数或选项 | 说明 |
|---|---|
| key | TairDoc的key，用于指定作为命令调用对象的TairDoc。 |
| path | TairDoc的path。 |
| start | 修剪的开始位置，取值为从0开始的一个索引值，修剪后的数组包含该位置的元素。 |
| stop | 修剪的结束位置，取值为从0开始的一个索引值，修剪后的数组包含该位置的元素。 |

返回值成功：操作完成后数组的长度。 key不存在：-1。 其它情况返回相应的异常信息。 使用示例

```
127.0.0.1:6379> JSON.SET doc . '{"id": [1,2,3,4,5,6]}'
```

`OK`

```
127.0.0.1:6379> JSON.ARRTRIM doc .id 3 4 127.0.0.1:6379> JSON.GET doc .id [4,5] 127.0.0.1:6379> JSON.ARRTRIM doc .id 3 4 ERR array index outflow 127.0.0.1:6379> JSON.ARRTRIM doc .id -2 -5 ERR array index outflow 127.0.0.1:6379>
```

**JSONPointer和JSONPath**

TairDoc在支持JSONPointer的基础上支持了JSONPath的部分语法，示例如下： 云数据库 Tair（兼容Redis）用户指

| JSONPointer | JSONPath |
|---|---|
| 127.0.0.1:6379> JSON.SET doc . '{"foo": "bar", "baz" : [1,2,3]}' OK 127.0.0.1:6379> JSON.GET doc .foo "bar" 127.0.0.1:6379> JSON.GET doc .baz[0] 1 | 127.0.0.1:6379> JSON.SET doc "" '{"foo": "bar", "baz" : [1,2,3]}' OK 127.0.0.1:6379> JSON.GET doc /foo "bar" 127.0.0.1:6379> JSON.GET doc /baz/0 1 |

具体的兼容方式如下表所示。

| 兼容项 | JSONPath | JSONPointer |
|---|---|---|
| 根元素 | . | “” |
| 获取元素 | .a.b.c | /a/b/c |
| 数组 | .a[2] | /a/2 |
| 整体获取 | .a["b.c"] | /a/b.c |
|  | .a['b.c'] | /a/b.c |

云数据库 Tair（兼容Redis）用户指

## 实例规格

云数据库 Tair（兼容 Redis）支持社区版和企业版（性能增强型），社区版实例支持标准、集群和读写分离架构，企业版实例支持标准和集群架构。本文介绍规格的详细信息（包含内存容量、连接数、带宽等）。

**通用规格与独享规格对比**

| 规格类型 | 特点 | 适用场景 |
|---|---|---|
| 独享规格 | 每个独享规格的集群独占所分配到的计算资源 （如CPU）。 不会与同一服务器上的其他集群共享计算资源，性能更加稳定可靠。 | 对性能稳定性要求高，以数据库为核心系统的业务场景，如金融、电商、政务和大中型互联网业务等。 |
| 通用规格 | 同一服务器上的不同集群，会互相充分利用彼此空闲的计算资源（如CPU）。 通过复用计算资源享受规模红利，性价比更高。 | 有降低成本诉求，追求高性价比的应用场景。 |

**带宽说明**

在网络带宽资源充足的情况下，云数据库 Tair（兼容 Redis）没有带宽限制；当资源不足时，实例的带宽限制才会生效。 集群实例的总带宽上限为2,048 MB/s。达到该上限后，即使选择拥有更多分片的规格，带宽也不会提高，建议总带宽不要超过25G带宽。 带宽分别应用于上行带宽和下行带宽，如果某规格的带宽为10 MB/s，则该规格实例的上下行带宽都是10 MB/s。 表中的带宽为Redis实例的内网带宽。外网带宽取决于内网带宽，同时受到Redis实例与客户端之间的网络带宽限制，建议使用内网连接方式，排除外网影响，发挥最大的带宽性能。

**云原生版**

单分片规格如下：实例总容量 = 分片规格 × 分片数量，分片数量支持2～128片。

**标准架构与集群架构直连模式的分片规格**

| 规格名称 | 规格代码 （API使用） | CPU核数 | 内存 （GB） | ESSD云盘 （GB） | 带宽 | 最大连接数 | QPS参考值 |
|---|---|---|---|---|---|---|---|
| 1 GB | tair.rdb.1 g | 10 | 1 | 5 | 768 Mbps（9 6 MB/s） | 30,000 | 300,000 |
| 2 GB | tair.rdb.2 g | 10 | 2 | 10 | 768 Mbps（9 6 MB/s） | 30,000 | 300,000 |

云数据库 Tair（兼容Redis）用户指

| 4 GB | tair.rdb.4 g | 10 | 4 | 20 | 768 Mbps（9 6 MB/s） | 40,000 | 300,000 |
|---|---|---|---|---|---|---|---|
| 8 GB | tair.rdb.8 g | 10 | 8 | 40 | 768 Mbps（9 6 MB/s） | 40,000 | 300,000 |
| 16 GB | tair.rdb.1 6g | 10 | 16 | 80 | 768 Mbps（9 6 MB/s） | 40,000 | 300,000 |
| 24 GB | tair.rdb.2 4g | 10 | 24 | 120 | 768 Mbps（9 6 MB/s） | 50,000 | 300,000 |
| 32 GB | tair.rdb.3 2g | 10 | 32 | 160 | 768 Mbps（9 6 MB/s） | 50,000 | 300,000 |
| 64 GB | tair.rdb.6 4g | 10 | 64 | 320 | 768 Mbps（9 6 MB/s） | 50,000 | 300,000 |

**集群架构代理模式与读写分离架构的分片规格**

| 规格名称 | 规格代码 （API使用） | CPU核数 | 内存 （GB） | ESSD云盘 （GB） | 带宽 | 最大连接数 | QPS参考值 |
|---|---|---|---|---|---|---|---|
| 1 GB | tair.rdb.w ith.proxy. 1g | 11 | 1 | 5 | 768 Mbps（9 6 MB/s） | 30,000 | 300,000 |
| 2 GB | tair.rdb.w ith.proxy. 2g | 11 | 2 | 10 | 768 Mbps（9 6 MB/s） | 30,000 | 300,000 |
| 4 GB | tair.rdb.w ith.proxy. 4g | 11 | 4 | 20 | 768 Mbps（9 6 MB/s） | 40,000 | 300,000 |
| 8 GB | tair.rdb.w ith.proxy. 8g | 11 | 8 | 40 | 768 Mbps（9 6 MB/s） | 40,000 | 300,000 |

云数据库 Tair（兼容Redis）用户指

| 16 GB | tair.rdb.w ith.proxy. 16g | 11 | 16 | 80 | 768 Mbps（9 6 MB/s） | 40,000 | 300,000 |
|---|---|---|---|---|---|---|---|
| 24 GB | tair.rdb.w ith.proxy. 24g | 11 | 24 | 120 | 768 Mbps（9 6 MB/s） | 50,000 | 300,000 |
| 32 GB | tair.rdb.w ith.proxy. 32g | 11 | 32 | 160 | 768 Mbps（9 6 MB/s） | 50,000 | 300,000 |
| 64 GB | tair.rdb.w ith.proxy. 64g | 11 | 64 | 320 | 768 Mbps（9 6 MB/s） | 50,000 | 300,000 |

**经典版**

**企业版（性能增强型）**

表 1. 标准版-双副本

| 规格 | InstanceClass （API 使用） | IO线程数 | 最大连接数 | 总带宽 （MB/s） |
|---|---|---|---|---|
| 256M主从性能增强版 | redis.amber.master.micro.multith read | 6 | 30,000 | 10 |
| 512M主从性能增强版 | redis.amber.master.2xmicro.mult ithread | 6 | 30,000 | 10 |
| 1G主从性能增强版 | redis.amber.master.small.multith read | 6 | 30,000 | 96 |
| 2G主从性能增强版 | redis.amber.master.mid.multithre ad | 6 | 30,000 | 96 |
| 4G主从性能增强版 | redis.amber.master.stand.multith read | 6 | 30,000 | 96 |
| 8G主从性能增强版 | redis.amber.master.large.multithr ead | 6 | 30,000 | 96 |
| 16G主从性能增强版 | redis.amber.master.2xlarge.multi thread | 6 | 30,000 | 96 |

云数据库 Tair（兼容Redis）用户指

| 32G主从性能增强版 | redis.amber.master.4xlarge.multi thread | 6 | 30,000 | 96 |
|---|---|---|---|---|
| 64G主从性能增强版 | redis.amber.master.8xlarge.multi thread | 6 | 30,000 | 96 |

表 2. 集群版

| 规格 | InstanceClass （API 使用） | IO线程数 | 分片数 | 最大连接数 | 每分片带宽 | 总带宽 （MB /s） |
|---|---|---|---|---|---|---|
| 2G集群性能增强版（2节点） | redis.amber.logic.shardin g.1g.2db.0rodb.6proxy.m ultithread | 6 | 2 | 50,00 0 | 96 | 192 |
| 4G集群性能增强版（2节点） | redis.amber.logic.shardin g.2g.2db.0rodb.6proxy.m ultithread | 6 | 2 | 50,00 0 | 96 | 192 |
| 8G集群性能增强版（4节点） | redis.amber.logic.shardin g.2g.4db.0rodb.12proxy. multithread | 6 | 4 | 120,0 00 | 96 | 384 |
| 16G集群性能增强版（8节点） | redis.amber.logic.shardin g.2g.8db.0rodb.24proxy. multithread | 6 | 8 | 240,0 00 | 96 | 768 |
| 32G集群性能增强版（8节点） | redis.amber.logic.shardin g.4g.8db.0rodb.24proxy. multithread | 6 | 8 | 240,0 00 | 96 | 768 |
| 64G集群性能增强版（8节点） | redis.amber.logic.shardin g.8g.8db.0rodb.24proxy. multithread | 6 | 8 | 240,0 00 | 96 | 768 |
| 32G集群性能增强版（16节点） | redis.amber.logic.shardin g.2g.16db.0rodb.48proxy .multithread | 6 | 16 | 480,0 00 | 96 | 1,536 |
| 64G集群性能增强版（16节点） | redis.amber.logic.shardin g.4g.16db.0rodb.48proxy .multithread | 6 | 16 | 480,0 00 | 96 | 1,536 |
| 128G集群性能增强版（16 节点） | redis.amber.logic.shardin g.8g.16db.0rodb.48proxy .multithread | 6 | 16 | 480,0 00 | 96 | 1,536 |

云数据库 Tair（兼容Redis）用户指

| 256G集群性能增强版（16 节点） | redis.amber.logic.shardin g.16g.16db.0rodb.48prox y.multithread | 6 | 16 | 480,0 00 | 96 | 1,536 |
|---|---|---|---|---|---|---|
| 512G集群性能增强版（32 节点） | redis.amber.logic.shardin g.16g.32db.0rodb.96prox y.multithread | 6 | 32 | 500,0 00 | 96 | 2,048 |
| 1024G集群性能增强版（64 节点） | redis.amber.logic.shardin g.16g.64db.0rodb.192pro xy.multithread | 6 | 64 | 500,0 00 | 96 | 2,048 |
| 2048G集群性能增强版 （128节点） | redis.amber.logic.shardin g.16g.128db.0rodb.384pr oxy.multithread | 6 | 128 | 500,0 00 | 96 | 2,048 |
| 4096G集群性能增强版 （256节点） | redis.amber.logic.shardin g.16g.256db.0rodb.768pr oxy.multithread | 6 | 256 | 500,0 00 | 96 | 2,048 |
| 8192G集群性能增强版 （256节点） | redis.amber.logic.shardin g.32g.256db.0rodb.768pr oxy.multithread | 6 | 256 | 500,0 00 | 96 | 2,048 |

**社区版**

表 3. 标准版-双副本

| 规格 | InstanceClass （API 使用） | 最大连接数 | 总带宽（MB/s） | 处理能力 |
|---|---|---|---|---|
| 256M主从版 | redis.master.micro.default | 10,000 | 10 | 单核 |
| 512M主从版 | redis.master.2xmicro.defa ult | 10,000 | 10 | 单核 |
| 1G主从版 | redis.master.small.default | 10,000 | 10 | 单核 |
| 2G主从版 | redis.master.mid.default | 10,000 | 16 | 单核 |
| 4G主从版 | redis.master.stand.default | 10,000 | 24 | 单核 |
| 8G主从版 | redis.master.large.default | 10,000 | 24 | 单核 |

云数据库 Tair（兼容Redis）用户指

| 16G主从版 | redis.master.2xlarge.defa ult | 10,000 | 32 | 单核 |
|---|---|---|---|---|
| 32G主从版 | redis.master.4xlarge.defa ult | 10,000 | 32 | 单核 |
| 64G主从版 | redis.master.8xlarge.defa ult | 10,000 | 48 | 单核 |

表 4. 集群版

| 规格 | InstanceClass （API 使用） | 分片数 | 最大连接数 | 总带宽 （MB/s ） | 处理能力 |
|---|---|---|---|---|---|
| 16G集群版 | redis.logic.sharding.2g.8db.0rodb.8pr oxy.default | 8 | 80,000 | 768 | 8核 |
| 32G集群版 | redis.logic.sharding.4g.8db.0rodb.8pr oxy.default | 8 | 80,000 | 768 | 8核 |
| 64G集群版 | redis.logic.sharding.8g.8db.0rodb.8pr oxy.default | 8 | 80,000 | 768 | 8核 |
| 128G集群版 | redis.logic.sharding.8g.16db.0rodb.16 proxy.default | 16 | 160,000 | 1,536 | 16核 |
| 256G集群版 | redis.logic.sharding.16g.16db.0rodb.1 6proxy.default | 16 | 160,000 | 1,536 | 16核 |
| 512G集群版 | redis.logic.sharding.16g.32db.0rodb.3 2proxy.default | 32 | 320,000 | 2,048 | 32核 |
| 1T集群版 | redis.logic.sharding.16g.64db.0rodb.6 4proxy.default | 64 | 500,000 | 2,048 | 64核 |
| 2T集群版 | redis.logic.sharding.16g.128db.0rodb. 128proxy.default | 128 | 500,000 | 2,048 | 128核 |
| 4T集群版 | redis.logic.sharding.16g.256db.0rodb. 256proxy.default | 256 | 500,000 | 2,048 | 256核 |

表 5. 读写分离版云数据库 Tair（兼容Redis）用户指

| 规格 | InstanceClass （API 使用） | 只读节点数 | 最大连接数 | 总带宽 | QPS |
|---|---|---|---|---|---|
| 1G读写分离版（1节点1只读） | redis.logic.splitrw.small. 1db.1rodb.4proxy.defau lt | 1 | 20,000 | 96 | 200,000 |
| 2G读写分离版（1节点1只读） | redis.logic.splitrw.mid.1 db.1rodb.4proxy.default | 1 | 20,000 | 192 | 200,000 |
| 4G读写分离版（1节点1只读） | redis.logic.splitrw.stand. 1db.1rodb.4proxy.defau lt | 1 | 20,000 | 192 | 200,000 |
| 8G读写分离版（1节点1只读） | redis.logic.splitrw.large. 1db.1rodb.4proxy.defau lt | 1 | 20,000 | 192 | 200,000 |
| 16G读写分离版（1节点1只读） | redis.logic.splitrw.2xlar ge.1db.1rodb.4proxy.de fault | 1 | 20,000 | 192 | 200,000 |
| 32G读写分离版（1节点1只读） | redis.logic.splitrw.4xlar ge.1db.1rodb.4proxy.de fault | 1 | 20,000 | 192 | 200,000 |
| 64G读写分离版（1节点1只读） | redis.logic.splitrw.8xlar ge.1db.1rodb.4proxy.de fault | 1 | 20,000 | 192 | 200,000 |
| 1G读写分离版（1节点3只读） | redis.logic.splitrw.small. 1db.3rodb.4proxy.defau lt | 3 | 40,000 | 192 | 400,000 |
| 2G读写分离版（1节点3只读） | redis.logic.splitrw.mid.1 db.3rodb.4proxy.default | 3 | 40,000 | 384 | 400,000 |
| 4G读写分离版（1节点3只读） | redis.logic.splitrw.stand. 1db.3rodb.4proxy.defau lt | 3 | 40,000 | 384 | 400,000 |
| 8G读写分离版（1节点3只读） | redis.logic.splitrw.large. 1db.3rodb.4proxy.defau lt | 3 | 40,000 | 384 | 400,000 |

云数据库 Tair（兼容Redis）用户指

| 16G读写分离版（1节点3只读） | redis.logic.splitrw.2xlar ge.1db.3rodb.4proxy.de fault | 3 | 40,000 | 384 | 400,000 |
|---|---|---|---|---|---|
| 32G读写分离版（1节点3只读） | redis.logic.splitrw.4xlar ge.1db.3rodb.4proxy.de fault | 3 | 40,000 | 384 | 400,000 |
| 64G读写分离版（1节点3只读） | redis.logic.splitrw.8xlar ge.1db.3rodb.4proxy.de fault | 3 | 40,000 | 384 | 400,000 |
| 1G读写分离版（1节点5只读） | redis.logic.splitrw.small. 1db.5rodb.6proxy.defau lt | 5 | 60,000 | 288 | 600,000 |
| 2G读写分离版（1节点5只读） | redis.logic.splitrw.mid.1 db.5rodb.6proxy.default | 5 | 60,000 | 576 | 600,000 |
| 4G读写分离版（1节点5只读） | redis.logic.splitrw.stand. 1db.5rodb.6proxy.defau lt | 5 | 60,000 | 576 | 600,000 |
| 8G读写分离版（1节点5只读） | redis.logic.splitrw.large. 1db.5rodb.6proxy.defau lt | 5 | 60,000 | 576 | 600,000 |
| 16G读写分离版（1节点5只读） | redis.logic.splitrw.2xlar ge.1db.5rodb.6proxy.de fault | 5 | 60,000 | 576 | 600,000 |
| 32G读写分离版（1节点5只读） | redis.logic.splitrw.4xlar ge.1db.5rodb.6proxy.de fault | 5 | 60,000 | 576 | 600,000 |
| 64G读写分离版（1节点5只读） | redis.logic.splitrw.8xlar ge.1db.5rodb.6proxy.de fault | 5 | 60,000 | 576 | 600,000 |

云数据库 Tair（兼容Redis）用户指

## 快速入门

### 开始使用云数据库Tair

本章节介绍如何从创建实例到登录数据库的一系列操作，帮助您快速地了解Tair实例的操作流程。 实例操作步骤的关键流程如下所示。 介绍如何登录到云数据库 Tair（兼容 Redis）控制台。

### 创建实例

阿里云数据库支持经典网络和专有网络两种网络类型，您可以创建不同网络下的Tair实例。 为了数据库的安全稳定，在开始使用实例前，您需要将访问数据库的 IP 地址或者 IP 段加到目标实例的白名单中。 修改密码（可选） 如果在创建实例时，没有设置实例的密码，用户需要在**实例信息**页面设置实例的密码。

### 连接实例

您可以使用支持Redis协议的客户端连接实例，也可以使用Redis原生的工具redis-cli连接实例。

### 登录云数据库Tair（兼容Redis）控制

**台**

本章节介绍如何登录到云数据库 Tair（兼容 Redis）控制台。

**前提条件**

登录Apsara Uni-manager运营控制台前，确认您已从部署人员处获取Apsara Uni-manager运营控制台的服务域名地址。 推荐使用Chrome浏览器。

**操作步骤**

1. 在浏览器地址栏中，输入Apsara Uni-manager运营控制台的服务域名地址，按回车键。
2. 输入正确的用户名及密码。
请向运营管理员获取登录控制台的用户名和密码。

**说明**

首次登录Apsara Uni-manager运营控制台时，需要修改登录用户名的密码，请按照提示完成密码修改。为提高安全性，密码长度必须为8~20位，且至少包含以下两种类型： 英文大写或小写字母（A~Z、a~z） 阿拉伯数字（0~9） 特殊符号（感叹号（！）、at（@）、井号（#）、美元符号（$）、百分号（%）等）
3. 单击**登录**。
4. 如果账号已激活MFA多因素认证，请根据以下两种情况进行操作：
云数据库 Tair（兼容Redis）用户指管理员强制开启MFA后的首次登录： a. 在绑定虚拟MFA设备页面中，按页面提示步骤绑定MFA设备。 b. 按照步骤2重新输入账号和密码，单击**登录**。 c. 输入6位MFA码后单击**认证**。 您已开启并绑定MFA： 输入6位MFA码后单击**认证**。

**说明**

绑定并开启MFA的操作请参见《**Apsara Uni-manager****运营控制台用户指南》**中的章节**《绑定**
**并开启虚拟****MFA****设备》**。
5. 在页面顶部的菜单栏中，选择**产品** > **数据库** > **云数据库** **Tair****（兼容** **Redis**）。

### 创建实例

本章节介绍如何通过控制台创建实例。

**操作步骤**

1. 登录云数据库Tair（兼容Redis）控制台。
2. 在左侧导航栏，单击**实例列表**。
3. 单击页面左上角**创建实例**。
4. 设置实例参数，下表按照部署模式分两表进行介绍。
表 1. 设置**经典**部署模式新实例参数

| 类别 | 配置 | 说明 |
|---|---|---|
| 基本配置 | 组织 | 选择实例所属组织。 |
|  | 资源集 | 选择实例所属资源集。 重要选择项目后，只有属于该资源集的成员才能使用该实例。 |
| 区域 | 地域 | 选择实例所属地域。 |
|  | 可用区类型 | 选择实例所属可用区，若选择双可用区即可实现同城容灾。 |
|  | 版本类型 | 社区版：兼容开源Redis协议标准、高性能的数据库服务。 企业版：基于社区版开发的Redis产品，读写性能可达到社区版的3倍，同时集成多个自研的Redis模块，扩展了Redis的适用性。更多信息，请参见企业版性能增强型介绍。 |

| 数据库 Tair（兼快速入门 |  |  |
|---|---|---|
| 规格配置 |  |  |
|  | 芯片架构 | 选择实例所属机器的芯片架构。 说明选择该配置时如提示未授权，请联系运营管理员对该账号执行授权。 |
|  | 引擎版本 | 选择实例的引擎版本，支持Redis 4.0、5.0、6.0和7.0。 |
|  | 架构类型 | 标准版：采用主从架构，能提供高性能的缓存服务，同时保证数据的高可用。 集群版：可轻松突破Redis自身单线程瓶颈，满足大容量、高性能的业务需求。 读写分离：可提供高可用、高性能、高灵活的读写分离服务，解决热点数据集中及高并发读取的业务需求，最大化地节约用户运维成本。 说明仅社区版支持读写分离架构。 |
|  | 节点类型 | 固定为高可用，即一主一从共两个节点，双机热备保障可用性。 |
|  | 规格类型 | 通用规格：多实例共享同一服务器资源，可动态复用空闲的计算资源（如 CPU），性价比更高。 独享规格：实例独占分配到的计算资源（如CPU），实现资源隔离，性能稳定强劲。 |
|  | 实例规格 | 选择实例的规格。 不同的实例规格提供的最大连接数和最大内网带宽不同，更多信息，请参见实例规格。 |
|  | 网络类型 | 经典网络：经典网络中的云服务在网络上不进行隔离，只能依靠云服务自身的安全组或白名单策略来阻挡非法访问。 专有网络VPC（Virtual Private Cloud）：专有网络帮助您在阿里云上构建出一个隔离的网络环境。您可以自定义专有网络里面的路由表、IP地址范围和网关。此外还可以通过专线或者VPN的方式将自建机房与阿里云专有网络内的云资源组合成一个虚拟机房，实现应用平滑上云。 说明若选择专有网络，请先创建好VPC，如何创建VPC请参见《VPC用户指南》中的《创建专有网络》和《创建交换机》章节。 |

云数据库 Tair（兼容Redis）用户指

|  | IP类型 | IPv4：仅分配IPv4地址，适用于纯IPv4网络环境。 IPv4/v6双栈：同时分配IPv4和IPv6地址，适用于需要同时支持IPv4与IPv6 客户端访问的混合网络场景。启用后需配置IPv6白名单以控制IPv6地址的访问权限。 说明如需配置该项参数需开启IPV6开关，具体操作，请参见《运维指南》中开启云数据库 Tair（兼容 Redis） IPV6开关章节。 如果提示未授权等信息，请参见租户组织对SLB服务授权操作。 |
|---|---|---|
| 网络 |  |  |
|  | 专有网络 vpc | 选择您的VPC。 说明当网络类型为专有网络时，需要填写该参数。 |
|  | 交换机 vswitch | 选择VPC下的交换机。 说明当网络类型为专有网络时，需要填写该参数。 |
|  | IPv4白名单 | 添加IPv4类型的IP地址，允许这些IP地址访问该Tair实例。 说明建议使用RFC私网地址作为专有网络的网段如 10.0.0.0/8，172.16.0.0/12，192.168.0.0/16 |
|  | IPv6白名单 | 添加IPv6类型的IP地址，允许这些IP地址访问该Tair实例。 说明 IPv6白名单地址说明支持以下格式： IPv6地址格式由8组16进制数组成，每组4个字符，用冒号“:”分隔。例如：2001:0db8:0000:0000:0000:0000:0000:0001，支持简写形式，如 2001:db8::1（连续的0段可用 :: 替代，但仅限一次）。 需附加前缀长度（/后接0~128的整数），例如 2001:db8::/32， 指定IP地址范围。 fc00::/7，ULA（唯一本地地址），类似IPv4 192.168 地址段；仅限私网使用。（推荐）。 ::/0，该地址为所有IPv6地址，不推荐生产环境使用。 fe80::/10，本地链路地址（Link-Local Address），类似IPv4的 169.254.x.x，局域网内设备的自动配置和直接通信，不推荐使用。 |

云数据库 Tair（兼容Redis）用户指

| 配置密码 | 实例名称 | 设置实例的名称，便于后续业务识别。 长度为2~128个字符。 以大小写字母或中文开头，可包含字母、数字、下划线（ ）和短划线（-）。 _ |
|---|---|---|
|  | 设置密码 | 您可以选择立即设置或选择创建后设置。 |
|  | 登录密码 | 设置访问实例的密码，密码要求如下： 长度为8~32个字符。 大写字母、小写字母、数字、特殊字符占三种。 特殊字符为 ! @ # $ % ^ & * ( ) + - =。 _ |
|  | 确认密码 | 再次输入访问实例的密码。 |
| 实例设置 | 创建数量 | 默认为1，支持批量创建多个相同配置的实例。 |

表 2. 设置**云原生**部署模式新实例参数

| 类别 | 配置 | 说明 |
|---|---|---|
| 部署模式 | 部署模式 | 选择云原生。 |
| 基本配置 | 组织 | 选择实例所属组织。 |
|  | 资源集 | 选择实例所属资源集。 重要选择项目后，只有属于该资源集的成员才能使用该实例。 |
| 区域 | 地域 | 选择实例所属地域。 |
|  | 可用区类型 | 选择实例所属可用区，若选择多可用区即可实现同城容灾。 |
|  | 版本类型 | 固定为企业版。 |
|  | 芯片架构 | 选择Redis实例所属机器的芯片架构。 说明选择该配置时如提示未授权，请联系运营管理员对该账号执行授权。 |

云数据库 Tair（兼容Redis）用户指

| 规格配置 |  |  |
|---|---|---|
|  | 引擎版本 | Redis的引擎版本，支持Redis 7.0。 |
|  | 架构类型 | 标准版：采用主从架构，能提供高性能的缓存服务，同时保证数据的高可用。 集群版：可轻松突破Redis自身单线程瓶颈，满足大容量、高性能的业务需求。 |
|  | 节点类型 | 高可用：即一主多备模式，保障可用性。 单节点：单节点类型采用单个数据库节点部署架构，没有可实时同步数据的备节点。 说明双可用区不支持单节点类型，如需单节点，请选择单可用区，架构类型选择标准版。 |
|  | 连接模式 | 代理模式：代理模式（Proxy）不仅能够使Redis Cluster的使用方式与Redis 标准版（主备）保持一致，同时额外提供了高级特性。 直连模式：连接、使用方式与原生Redis Cluster集群一致。 |
|  | 分片规格 | 选择实例的规格。 未开启集群模式时，实例为主备架构，分片规格等同于实例规格；开启集群模式后，实例将由多个分片构成，可设置分片数量。 |
|  | 分片数量 | 未开启集群模式时，该模块值为1（代表实例此时为主备架构）且不可选； 开启集群模式后，该模块代表实例的分片数量，实例总容量 = 分片规格 * 分片数量； 例：分片规格为2 GB，分片数量为4，则实例总容量为8 GB（由4个2 GB的分片构成）。 |
| 设置项：节点数量 \| 读写分离 | 读写分离 | 默认关闭，支持开启读写分离。 |
|  | 总节点数 | 选择节点数，默认2节点，最高支持10节点。 2节点，1主1备，开启读写分离功能后，备节点可读。 说明若实例为集群架构，假设节点数设置为3，则每个分片均为3节点。 |

云数据库 Tair（兼容Redis）用户指

| 网络 | 网络类型 | 经典网络：经典网络中的云服务在网络上不进行隔离，只能依靠云服务自身的安全组或白名单策略来阻挡非法访问。 专有网络VPC（Virtual Private Cloud）：专有网络帮助您在阿里云上构建出一个隔离的网络环境。您可以自定义专有网络里面的路由表、IP地址范围和网关。此外还可以通过专线或者VPN的方式将自建机房与阿里云专有网络内的云资源组合成一个虚拟机房，实现应用平滑上云。 说明若选择专有网络，请先创建好VPC，如何创建VPC请参见《VPC用户指南》中的《创建专有网络》和《创建交换机》章节。 |
|---|---|---|
|  | IP类型 | IPv4：仅分配IPv4地址，适用于纯IPv4网络环境。 IPv4/v6双栈：同时分配IPv4和IPv6地址，适用于需要同时支持IPv4与IPv6 客户端访问的混合网络场景。启用后需配置IPv6白名单以控制IPv6地址的访问权限。 说明如需配置该项参数需开启IPV6开关，具体操作，请参见《运维指南》中开启云数据库 Tair（兼容 Redis） IPV6开关章节。 |
|  | 专有网络 vpc | 选择您的VPC。 说明当网络类型为专有网络时，需要填写该参数。 |
|  | 交换机 vswitch | 选择VPC下的交换机。 说明当网络类型为专有网络时，需要填写该参数。 |
|  | IPv4白名单 | 添加IPv4类型的IP地址，允许这些IP地址访问该Tair实例。 说明建议使用RFC私网地址作为专有网络的网段如 10.0.0.0/8，172.16.0.0/12，192.168.0.0/16 |

云数据库 Tair（兼容Redis）用户指

|  | IPv6白名单 | 添加IPv6类型的IP地址，允许这些IP地址访问该Tair实例。 说明 IPv6白名单地址说明支持以下格式： IPv6地址格式由8组16进制数组成，每组4个字符，用冒号“:”分隔。例如：2001:0db8:0000:0000:0000:0000:0000:0001，支持简写形式，如 2001:db8::1（连续的0段可用 :: 替代，但仅限一次）。 需附加前缀长度（/后接0~128的整数），例如 2001:db8::/32， 指定IP地址范围。 fc00::/7，ULA（唯一本地地址），类似IPv4 192.168 地址段；仅限私网使用。（推荐）。 ::/0，该地址为所有IPv6地址，不推荐生产环境使用。 fe80::/10，本地链路地址（Link-Local Address），类似IPv4的 169.254.x.x，局域网内设备的自动配置和直接通信，不推荐使用。 |
|---|---|---|
| 配置密码 | 实例名称 | 设置实例的名称，便于后续业务识别。 长度为2~128个字符。 以大小写字母或中文开头，可包含字母、数字、下划线（ ）和短划线（-）。 _ |
|  | 设置密码 | 您可以选择立即设置或选择创建后设置。 |
|  | 登录密码 | 设置访问实例的密码，密码要求如下： 长度为8~32个字符。 大写字母、小写字母、数字、特殊字符占三种。 特殊字符为 ! @ # $ % ^ & * ( ) + - =。 _ |
|  | 确认密码 | 再次输入访问实例的密码。 |
| 实例设置 | 创建数量 | 默认为1，支持批量创建多个相同配置的实例。 |

5. 在最终创建实例前，请在页面右侧**配置概览**面板检查实例的整体配置，确保符合您的要求。
如果配额不足，可单击**管理**进行配置。具体操作，请参见**《统一云管平台****用户指南》**中的**《配额管理》**章节。
6. 完成上述参数配置后，单击**提交**。

### 设置白名单

为了数据库的安全稳定，在开始使用云数据库 Tair（兼容 Redis）实例前，您需要将访问数据库的IP地址或者IP段加到目标实例的白名单中。

**背景信息**

云数据库 Tair（兼容Redis）用户指

**说明**

正确使用白名单可以让实例得到高级别的访问安全保护，建议您定期维护白名单。

**操作步骤**

1. 登录云数据库Tair（兼容Redis）控制台。
2. 在**实例列表**页，单击目标实例ID。
3. 在左侧导航栏，选择**安全设置**。
4. 单击左上角**新建白名单分组**。
5. 在**新增白名单分组（最大支持****50****个分组）**页面填写相关信息。

| 名称 | 描述 |
|---|---|
| 分组名称 | 分组名长度为2~32个字符。支持小写字母、数字以及下划线（ ），只能以小写字母开头，以字母或数字结 _ 尾。 |
| 类型 | 支持选择IPv4或IPv6。 说明仅云原生版本7.0以及经典架构社区版7.0支持 IPv6。 |

云数据库 Tair（兼容Redis）用户指

| 组内白名单 | 白名单IP地址配置说明 IP地址以英文逗号分隔，不可重复，最多1000 个。 支持格式： IPv4：10.23.12.24（具体IP）、 10.23.12.24/24（CIDR模式，前缀长度 1~32） IPv6：2001:db8::1（具体IP）、 2001:db8::/32（CIDR模式，前缀长度 1~128） 说明特殊说明：前缀长度设置为/0（如 0.0.0.0/0 或 ::/0）表示允许所有IP地址访问该实例，存在高安全风险，请谨慎设置。 示例允许单个IPv6地址： 2001:db8:85a3::8a2e:370:7334 允许IPv6 CIDR段： 240e:390:a100::/44 放通所有IP（高风险）：::/0 或 0.0.0.0/0 |
|---|---|
| 导入文件（.txt） | 支持批量导入IP地址。 |

云数据库 Tair（兼容Redis）用户指

| 加载ECS内网IP | i. 单击加载ECS私网IP。 ii. 根据业务需求选中对应的IP地址。 说明为便于定位目标IP地址，您可以将鼠标指针悬浮在对应的IP地址上，系统将展示该IP地址所属的ECS 实例ID和名称。 |
|---|---|

6. 单击**确定**。

### 连接实例

本文以redis-cli连接为例，帮助您快速连接实例。

**说明**

如需了解其他连接方式，请参见连接指南。

**前提条件**

ECS实例与Redis实例同属于经典网络。 已将ECS实例的内网IP地址添加至Redis实例的白名单中。具体操作，请参见设置白名单。 ECS实例的操作系统为Linux，且已安装原生Redis，安装方法，请参见Redis社区版官网。

**操作步骤**

1. 登录ECS设备的命令行，然后执行如下格式的命令连接至Redis实例：

```
src/redis-cli -h <hostname> -p <port>
```

表 1. 参数说明

| 参数 | 获取方式 |
|---|---|
| <hostname> | Redis实例的内网连接地址，可在实例信息页面中的连接信息区域框中获取。 |
| <port> | Redis实例的端口号，默认为6379。 |

命令示例

```
src/redis-cli -h r-bp1zxszhcgatnx****.redis.rds.aliyuncs.com -p 6379
```

2. 执行下述格式的命令完成密码验证：
云数据库 Tair（兼容Redis）用户指

```
AUTH <password>
```

<password>：账号的密码，在创建实例时已设置，如果忘记密码，可重置密码，具体操作，请参见修改密码。 命令示例：

```
AUTH testaccount:Rp829dlwa
```

验证成功后，返回如下结果： `OK` 云数据库 Tair（兼容Redis）用户指

## 实例管理

### 修改密码

如果您忘记密码、需要修改旧密码，或者在创建实例时没有设置密码，您可以重新设置实例的密码。

**操作步骤**

1. 登录云数据库Tair（兼容Redis）控制台。
2. 在**实例列表**页，单击目标实例ID。
3. 在**账号管理**页，单击右上角**修改密码**。
4. 在弹出的对话框中，输入旧密码和新密码。

**说明**

如果您忘记旧密码，在该对话框中单击**忘记旧密码**，然后设置新密码。 密码长度为8~32位。 密码需包含大写字母、小写字母、数字和特殊字符中的至少三种，支持的特殊字符

```
为 !@#$%^&*()_+-= 。
```

5. 单击**确定**。

### 设置白名单

为了数据库的安全稳定，在开始使用Redis实例前，您需要将访问数据库的IP地址或者IP段加到目标实例的白名单中。

**背景信息**

**说明**

正确使用白名单可以让Redis得到高级别的访问安全保护，建议您定期维护白名单。

**操作步骤**

1. 登录云数据库Tair（兼容Redis）控制台。
2. 在**实例列表**页，单击目标实例ID。
3. 在左侧导航栏，单击**白名单设置**。
4. 找到目标白名单分组，单击**修改**。

**说明**

您也可以单击**添加白名单分组**创建一个新的分组。分组名称长度为2~32个字符，由小写字母、数字或下划线组成，需以小写字母开头，以小写字母或数字结尾。
5. 在弹出的对话框中，根据要执行的操作，选择下述操作步骤：

| 要执行的操作 | 操作步骤 |
|---|---|

云数据库 Tair（兼容Redis）用户指

| 手动修改白名单 | 手动填写IP地址或IP地址段。 图 1. 手动修改白名单说明 IP地址以英文逗号分隔，不可重复，最多1000个。支持格式为 10.23.12.24（具体IP地址）、10.23.12.24/24（CIDR模式，即无类域间路由，/24表示地址中前缀的长度，范围为1~32）。 地址中的前缀长度设置为0（例如0.0.0.0/0、127.0.0.1/0）表示允许所有IP 地址访问该实例，存在高安全风险，请谨慎设置。 |
|---|---|
| 加载ECS实例的内网IP地址为白名单 | i. 单击加载ECS私网IP。 ii. 根据业务需求选中对应的IP地址。 图 2. 加载ECS内网IP地址说明为便于定位目标IP地址，您可以将鼠标指针悬浮在对应的IP地址上，系统将展示该IP 地址所属的ECS实例ID和名称。 |
| 清除白名单分组 | 当某个白名单分组中的所有IP地址均需要移除且需要保留该分组时，您可以单击清除白名单分组来完成该操作。 |

6. 单击**确定**。
云数据库 Tair（兼容Redis）用户指

### 变更配置

本文介绍如何变更Tair（兼容Redis）实例配置。

**注意事项**

业务影响：变配操作完成后，系统将自动执行数据迁移和切换。切换过程中会出现秒级的连接闪断。 执行时机：为避免影响业务正常运行，强烈建议您在业务低峰期执行本操作。 前置准备：请确保您的应用程序具备重连机制，以应对短暂的连接中断。

**操作步骤**

1. 登录云数据库Tair（兼容Redis）控制台。
2. 在**实例列表**页，选择目标实例，单击操作列中的**变更配置**。
3. 在跳转到的页面中，选择需要的配置。

| 配置 | 说明 |
|---|---|
| 版本类型 | 支持选择企业版或社区版。 说明仅社区版5.0实例支持配置该参数。 |
| 芯片架构 | 选择目标芯片类型。 |
| 架构类型 | 选择实例的架构类型。 标准版：采用主备架构，不仅能提供高性能的缓存服务，还支持数据高可靠。 集群版：可轻松突破Redis自身单线程瓶颈，满足大容量、高性能的业务需求。 读写分离：可提供高可用、高性能、高灵活的读写分离服务，解决热点数据集中及高并发读取的业务需求，最大化地节约用户运维成本。 |
| 实例规格 | 选择实例的规格。 不同的实例规格提供的最大连接数和最大内网带宽不同。 |
| 最大带宽变配策略 | 支持选择与新规格变配一致或保持当前最大带宽。 说明仅部署模式为经典支持该配置。 |

4. 单击**提交**。

**补充说明**

变配时长：具体耗时取决于实例的数据量大小及网络状况，通常在几分钟到几十分钟不等。 监控观察：变配完成后，建议立即观察实例的监控指标（如 CPU 使用率、连接数、延迟等），确保新配置满足业务预期。 云数据库 Tair（兼容Redis）用户指

### 节点管理

本文为您介绍在节点管理中如何开启读写分离功能和修改备节点数量。

**前提条件**

实例需同时满足以下条件： 实例类型为高可用。

**开启读写分离**

1. 登录云数据库Tair（兼容Redis）控制台。
2. 在**实例列表**页，单击目标实例ID。
3. 在左侧导航栏，单击**节点管理**。
4. 打开**读写分离**开关。
5. 在弹出的面板中，确认实例配置信息。
6. 单击**确定**。

**增删备节点**

1. 登录云数据库Tair（兼容Redis）控制台。
2. 在**实例列表**页，单击目标实例ID。
3. 在左侧导航栏，单击**节点管理**。
4. 在**节点分布（可用区）**区域，单击**修改**。
5. 在弹出的面板中，增加或减少备节点数量。
6. 单击**确定**，完成增删备节点。

### 转云原生部署模式

**云原生**部署模式兼容更高的Redis版本，同时也具有更加灵活的架构配置，您可以参考本文将**经典**版实例转
换为**云原生**版实例。

**重要**

实例执行切换时会出现1次30秒内的连接闪断，请确保应用具有重连机制。 为保障变配后的新实例能快速追平原实例的增量数据，同时规避因DNS缓存引起的数据双写， 在变配过程中，通常情况下实例会出现1分钟内的只读状态，而在写入量较大的场景下只读状态的时间可能增加，因此建议在业务低峰期进行变配。

**注意事项**

转换后，实例ID、实例连接地址、账号密码、IP白名单配置等均保持不变，实例中的数据不会丢失。 目前仅支持企业版5.0转云原生版，若原实例为其他版本，需先将实例升级大版本至企业版 5.0，再执行本操作。

**说明**

如果Tair5有公网地址不支持转云原生版。 云数据库 Tair（兼容Redis）用户指

**操作步骤**

1. 登录云数据库Tair（兼容Redis）控制台。
2. 在**实例列表**页，单击目标实例ID。
3. 在基础信息页面右上角，单击**转云原生**。
4. 在变更实例页面，填写芯片架构、实例规格、分片数量等基本信息。
5. 单击**提交**，等待实例状态变为**使用中**，代表转换成功。

### 管理分片数量

本文为您介绍如何增加或减少分片数量。

**注意事项**

分片数量调整只支持集群版，标准版不支持分片调整。 实例的总分片数最少为2个，单次操作的分片数上限为64个。 在增加分片时，实例会自动进行数据重平衡，但如果单次增加的分片数过少，会导致重平衡速度过慢、扩容效率低。建议单次增加的分片数不少于当前总分片数的1/6（向上取整），例如： 当前实例为8分片，建议增加分片数不少于2个（8/6=1.33，向上取整为2）。 当前实例为64分片，建议增加分片数不少于11个。 当前实例为100分片，建议增加分片数不少于17个。

**操作步骤**

1. 登录云数据库Tair（兼容Redis）控制台。
2. 在**实例列表**页，单击目标实例ID。
3. 在页面右上角，选择**分片调整**，根据业务选择**增加分片数量**或**减少分片数量**。
增加分片 a. 单击**增加分片**，在弹出框中，设置分片的数量。支持增加1~64个。 b. 单击**确定**。 删除分片

**重要**

删除分片会降低实例的总容量和实例性能，同时也会造成对应分片上的连接强制断开，请谨慎执行。如需执行，请确保应用具备重连机制。 a. 输入要删除的分片数量并选择删除策略。 删除策略支持**立即删除**和**可维护时间内执行**（推荐）。 b. 单击**确定**。分片立即删除，数据自动迁移至其他分片。

### 设置可维护时间段

您可以修改默认的可维护时间段，使云数据库 Tair（兼容 Redis）实例在业务低峰期间进行维护。

**背景信息**

在阿里云平台上，为保云数据库 Tair（兼容 Redis）实例的稳定性，后端系统会不定期对实例、机器进行维护操作。 云数据库 Tair（兼容Redis）用户指实例维护当天，为保障整个维护过程的稳定性，实例会在所设置的可运维时间前一段时间，进入实例维护中的状态，当实例处于该状态时，数据库本身正常的数据访问不会受到任何影响，但控制台上涉及该实例的变更类的功能均暂无法使用（如变更配置），查询类如性能监控等可以正常查阅。

**说明**

在进入实例所设置的可运维时间后，实例在维护期间可能会发生闪断，建议您尽量选择业务低峰期为运维时间段。

**操作步骤**

1. 登录云数据库Tair（兼容Redis）控制台。
2. 在**实例列表**页，单击目标实例ID。
3. 在**配置信息**区域框中，单击**可维护时间段**右侧的**修改**。
4. 选择可维护时间段。

**说明**

时间段以北京时间为基准。

### 迁移可用区

您可以将实例迁移至同一地域内的其他可用区。迁移可用区后，实例的所有属性、规格配置和连接地址都不会改变。

**前提条件**

迁移的目标可用区和当前实例的可用区处于同一地域。 专有网络的实例在操作迁移可用区之前，请确保目标可用区已创建相应的虚拟交换机，如需创建请参见**《专有网络****VPC****用户指南》**中的**《创建专有网络》**和**《创建交换机》**章节。 实例不可具备公网连接地址，如果已申请了公网连接地址，请先释放。

**注意事项**

迁移所需时间和网络、任务队列、数据量大小等多种因素有关，请在业务低峰期执行迁移可用区操作。

**操作步骤**

1. 登录云数据库Tair（兼容Redis）控制台。
2. 在**实例列表**页，单击目标实例ID。
3. 在**基本信息**区域框中，单击**迁移可用区**。
4. 根据实例网络类型，在**迁移可用区**页面，配置对应的参数。
云数据库 Tair（兼容Redis）用户指专有网络

| 参数 | 参数说明 |
|---|---|
| 可用区类型 | 选择迁移的可用区类型，支持单可用区和双可用区。 |
| 切换后主可用区 | 目标主可用区。 |
| 切换后备可用区 | 目标备可用区。 说明仅选择双可用区时支持该配置。 |
| 切换后 VSwitch | 目标VSwitch。 |
| 切换时间 | 选择开始迁移可用区的时间。 立即切换：参数配置完成后，系统立即开始迁移可用区任务。 可维护时间段内切换：在维护时间段迁移可用区。维护时间段设置，请参见设置可维护时间段。 |

云数据库 Tair（兼容Redis）用户指经典网络

| 参数 | 参数说明 |
|---|---|
| 可用区类型 | 选择迁移的可用区类型，支持单可用区和双可用区。 |
| 切换后主可用区 | 目标主可用区。 |
| 切换后备可用区 | 目标备可用区。 说明仅选择双可用区时支持该配置。 |
| 切换时间 | 选择开始迁移可用区的时间。 立即切换：参数配置完成后，系统立即开始迁移可用区任务。 可维护时间段内切换：在维护时间段迁移可用区。维护时间段设置，请参见设置可维护时间段。 |

5. 单击**确定**。
切换完成后，可在基本信息，可用区一栏查看切换详情。

### 迁移网络可用区

您可以将实例网络迁移至同一地域内的其他可用区。迁移网络可用区后，实例的所有属性、规格配置等信息都不会改变。 云数据库 Tair（兼容Redis）用户指

**注意事项**

切换过程会导致现有数据库连接断开，必须确保应用具备自动重连机制。 务必在业务低峰期执行，避免产生其他故障问题。 建议遵循“先切换数据主备角色，确认数据可用后，再切换网络可用区”的顺序。 确认目标可用区网络资源充足，且安全组/白名单策略允许新机房的应用访问。

**操作步骤**

1. 登录云数据库Tair（兼容Redis）控制台。
2. 在**实例列表**页，单击目标实例ID。
3. 在**基本信息**区域框中，单击**迁移网络可用区**。
4. 在**迁移网络可用区**页面，配置对应的参数。
专有网络

| 参数 | 参数说明 |
|---|---|
| 实例网络目标可用区 | 目标网络可用区。 |
| 切换后 VSwitch | 目标VSwitch。 |

云数据库 Tair（兼容Redis）用户指

| 切换时间 | 选择开始迁移网络可用区的时间。 立即切换：参数配置完成后，系统立即开始迁移网络可用区任务。 可维护时间段内切换：在维护时间段迁移网络可用区。维护时间段设置，请参见设置可维护时间段。 |
|---|---|

经典网络

| 参数 | 参数说明 |
|---|---|
| 实例网络目标可用区 | 目标网络可用区。 |
| 切换时间 | 选择开始迁移网络可用区的时间。 立即切换：参数配置完成后，系统立即开始迁移网络可用区任务。 可维护时间段内切换：在维护时间段迁移网络可用区。维护时间段设置，请参见设置可维护时间段。 |

5. 单击**确定**。

### 大版本升级

云数据库 Tair（兼容 Redis）新版本实例通常具备更高性能、更安全稳定、更多功能等特性，同时新版本实例可以获得更好的技术支持。若您希望使用新版本实例，无需额外创建实例，您可以在控制台升级实例的大版本。

**升级影响**

在申请资源、升级备库或同步数据阶段，对实例服务无影响。 云数据库 Tair（兼容Redis）用户指在实例切换或主备切换阶段，实例将存在60秒以内的只读状态（等待数据完全同步），同时会发生秒级的连接闪断，请在业务低峰期进行升级。 升级完成后，源实例的实例ID、连接地址、数据、白名单配置以及已创建的账号密码配置等均不会改变， 请您确保应用程序具备重连机制。

**注意事项**

若实例已创建DTS任务，会导致升级失败，请暂停DTS任务后重试。 若经典版实例，架构类型为集群架构，且申请了直连模式地址，请释放直连地址后重试。 若云原生集群架构实例的连接模式为直连模式，则无法升级大版本。 若实例未释放经典网络，会导致升级失败，请释放经典网络后重试（释放经典网络后无法再申请，推荐使用更快、更安全的VPC网络）。 升级大版本可能会导致实例内存使用量略有变化（约为-10%至10%），具体变化取决于不同版本存储元数据的差异。建议在升级大版本之前，确保实例内存使用量低于80%，以避免升级后实例内存达到较高水平。

**操作步骤**

1. 登录云数据库Tair（兼容Redis）控制台。
2. 在**实例列表**页，单击目标实例ID。
3. 在**实例信息**页，配置信息区域内，单击**版本**右侧**升级**中的**大版本升级**。

**说明**

4. 在**大版本升级**对话框，选择升级的目标版本和执行时间。

**说明**

实例版本升级或主备切换时，实例将产生60秒以内的只读状态和秒级的连接闪断。推荐您选择**可维护**
**时间内执行**，系统会在实例的可维护时间段内执行实例切换操作，可最大限度地降低影响。
5. 单击**确定**。

### 升级小版本

云数据库 Tair（兼容 Redis）不断对内核进行深度优化，修复安全漏洞，提升服务稳定性。您可以在控制台上一键将内核升级至最新版本。

**背景信息**

**说明**

请在业务低峰期进行升级，并确保应用程序具备重连机制。 系统会自动检测实例的内核版本，如果当前版本已经是最新版本，控制台**基本信息**页的**小版本升** 级按钮将呈现为灰色状态。

**操作步骤**

1. 登录云数据库Tair（兼容Redis）控制台。
2. 在**实例列表**页，单击目标实例ID。
云数据库 Tair（兼容Redis）用户指
3. 在**实例信息**页，配置信息区域内，单击**版本**右侧**升级**中的**小版本升级**。
4. 在**小版本升级**对话框，单击**立即升级**。
操作完成后，您可以在**基本信息**页中查看实例状态，实例的状态显示为小版本升级中。等状态变回使用中，即表示升级完成。

### 设置SSL加密

为提高链路的安全性，您可以启用SSL（Secure Sockets Layer）加密，然后安装SSL CA证书到您的应用服务。SSL加密功能在传输层对网络连接进行加密，在提升通信数据安全性的同时，保证数据的完整性。

**注意事项**

本操作将触发重启实例，实例会出现秒级的连接闪断，请在业务低峰期执行该操作并确保应用具备重连机制。 SSL加解密会消耗CPU资源，可能导致实例CPU使用率上升及读写延迟轻微增加，需确保实例当前CPU水位有足够缓冲空间。 开启SSL加密会增加连接建立时的握手延迟，可能会增加整体网络响应时间，建议必要时再开启。 云端证书有效期为1年，到期前将通过多渠道提醒并自动更新，支持配置计划时间自定义更新时段。

**前提条件**

实例需为以下类型之一： Tair（兼容Redis）经典版集群架构实例（4.0、5.0、6.0、7.0）。 Tair（兼容Redis）云原生版7.0实例。 对于云原生版7.0实例，您需要先完成TLS加密开关的开启，具体操作请参见《云数据库Tair（兼容 Redis）运维指南》中“开启云数据库 Tair（兼容 Redis） TLS（SSL）加密开关”章节完成配置。

**操作步骤**

**步骤一**

1. 登录云数据库Tair（兼容Redis）控制台。
2. 在**实例列表**页，单击目标实例ID。
3. 在左侧导航栏，单击**TLS(SSL)****设置**。

**步骤二**

请根据实例类型，选择对应的配置方式。

**云原生版实例**

本章节适用于云原生版7.0实例。

## 使用限制

连接中断风险：开启required（强制加密）模式后，所有未配置SSL/TLS的明文连接请求将被立即拒绝。 请务必确保所有客户端应用已完成证书配置及连接串更新，否则将导致业务连接大面积失败。 性能损耗预警：强制TLS加密会增加CPU计算开销，可能导致实例CPU使用率上升及读写延迟轻微增加。 建议在开启前评估实例当前CPU水位，预留足够的性能缓冲空间。 兼容性要求：云原生版7.0仅支持TLS 1.2及以上版本。若客户端或驱动不支持TLS 1.2及以上版本，将无法建立连接，需升级客户端。 云数据库 Tair（兼容Redis）用户指
1. 在TLS(SSL)配置页面，配置相关信息。

| 名称 | 描述 |
|---|---|
| 选择配置模式 | 简化模式：无需配置客户端证书等信息。适用于基础 SSL加密需求，快速配置。 完整模式：需要配置ACL和证书，提供最高安全级别。 说明需选择TLS最低版本：默认版本为TLSv1.2，还支持TLSv1、TLSv1.1、TLSv1.3。 |
| 选择证书类型 | 选择SSL证书的来源，使用云端证书以获得更好的安全性和便利性。 |
| 选择要保护的连接串 | 选择一个需要启用SSL加密的数据库连接串，可以选择内网连接串。 |

2. 单击**启用****SSL****加密**。

**说明**

完成操作后，需等待一段时间后，系统才能显示操作结果。 您还可通过**修改有效期**、**下载****CA****证书**和**版本名称**等按钮执行相关的操作。

**经典版集群架构实例**

云数据库 Tair（兼容Redis）用户指本章节适用于经典版集群架构4.0、5.0、6.0、7.0实例。
1. 在**TLS(SSL)****设置**页，单击**SSL****证书信息**右侧的滑块。

**说明**

2. 完成开通。
完成操作后，需等待一段时间后，系统才能显示操作结果。 您还可通过右上方的**更新证书**和**下载****CA****证书**等按键执行相关的操作。 TLS 最低版本默认版本为TLSv1.2，还支持TLSv1和TLSv1.1。

**关闭SSL加密**

1. 登录云数据库Tair（兼容Redis）控制台。
2. 在**实例列表**页，单击目标实例ID。
3. 在左侧导航栏，单击**TLS(SSL)****设置**。
4. 在**TLS(SSL)****设置**页，单击滑块关闭SSL加密。

### 开启透明数据加密TDE

云数据库 Tair（兼容 Redis）支持透明数据加密TDE（Transparent Data Encryption），可对RDB数据文件执行加密和解密。您可以通过控制台启用TDE功能，对RDB数据进行自动加密和解密，以满足提升数据安全性及合规需要。

**前提条件**

实例为企业版。 已部署密钥管理服务（KMS）。

**背景信息**

云数据库 Tair（兼容 Redis）的TDE功能可以将RDB数据文件在写入磁盘之前进行加密，从磁盘读入内存时进行解密，具有不额外占用存储空间、无需更改客户端应用程序等优势。 图 1. TDE加密

**影响**

由于开启TDE功能后无法关闭，在开启前，需要评估对业务的影响，具体如下： 暂不支持缓存分析操作。 暂不支持通过DTS或Redis-shake执行迁移或同步数据。

**注意事项**

云数据库 Tair（兼容Redis）用户指 TDE的开启粒度为实例级别，不支持Key（键）或DB（库）粒度的控制。 TDE加密对象为数据落盘文件（即RDB备份文件，如dump.rdb）。 TDE所使用的密钥，由密钥管理服务KMS（Key Management Service）统一生成和管理，云数据库 Redis不提供加密所需的密钥和证书。

**操作步骤**

1. 登录云数据库Tair（兼容Redis）控制台。
2. 在**实例列表**页，单击目标实例ID。
3. 在左侧导航栏，单击**TDE****设置**。
4. 打开**TDE****状态**右侧的开关。
5. 在弹出的对话框中，选择**使用自动生成密钥**或**使用自定义密钥**，然后单击**确定**。

**说明**

如果您的阿里云账号首次为实例开启TDE功能，请根据页面弹出的提示完成授权 （授权的角色为**AliyunRdsInstanceEncryptionDefaultRole**），授权完成后才可以使用相关密钥服务。 关于自定义密钥的创建方法，请参见**《密钥管理服务》用户手册**的**创建密钥**章节。 设置完成后，实例状态改为**TDE****修改中**，当实例状态转变为**运行中**表示操作完成。

### 清除数据

您可以在控制台清除Redis实例中的数据，可选的清除对象为所有数据或过期数据。

**操作步骤**

1. 登录云数据库Tair（兼容Redis）控制台。
2. 在**实例列表**页，单击目标实例ID。
3. 在**实例信息**页，单击页面右上角**清除数据**。
4. 在弹出的对话框中，选择待清除的对象：
**所有数据**：此操作将执行**FLUSHALL**命令清除该实例所有数据，清除后数据无法找回。
**过期数据**：此操作将执行**SCAN**命令批量清除该实例的所有过期数据，清除后数据无法找回。您可选

**警告**

通过该功能清除的数据无法找回且即刻生效，同时会对线上业务造成影响，请谨慎执行。推荐在执行清除前对Redis实例的数据进行备份，具体操作，请参见手动备份。
5. 单击**确定**。

**说明**

如选择为清除**所有数据**，单击**确定**后，您还可以选择是否备份数据。

### 释放实例

根据业务需求，您可以随时释放Tair实例，本文介绍如何释放Tair实例。 云数据库 Tair（兼容Redis）用户指根据业务需求，您可以随时释放Tair实例，本文介绍如何释放Tair实例

**操作步骤**

1. 登录云数据库Tair（兼容Redis）控制台。
2. 在**实例列表**页，选择目标实例**操作**列的**释放**。

**警告**

建议您在释放实例前先备份数据，谨慎进行后续步骤。
3. 在**释放实例**对话框中单击**释放**。
释放后，实例会在回收站保留一段时间，您可在回收站中对实例进行解锁、重建操作，更多信息请参见实例回收站管理。

### 实例回收站管理

实例回收站展示已释放的实例，支持恢复、立即销毁等操作。

**注意事项**

实例释放后将在回收站保留7天，超过保留期将永久销毁且不可恢复。 恢复将通过克隆原实例数据并新建实例完成，并非恢复至原实例。 恢复后原有数据保持不变，但连接地址（域名）可能发生变更，恢复完成后需确认新的连接地址并更新客户端配置。 公网地址不会自动恢复。

**操作步骤**

1. 登录云数据库Tair（兼容Redis）控制台。
2. 在左侧导航栏，单击**回收站**。
3. 在回收站的实例列表中，执行**恢复**或**立即销毁**操作。
**恢复**：将原实例的所有数据和部分配置（端口号等）恢复到新创建的实例中，但您需要重新配置**可用**
区、**网络类型**和**IP****类型**等信息。

**说明**

如果**网络类型**为**专有网络**，则还需配置专有网络VPC和交换机VSwitch。
**立即销毁**：彻底删除实例及其数据备份。

**警告**

销毁实例会同时销毁该实例的所有备份，包括常规数据备份、归档备份和日志备份，且销毁后无法恢复，请谨慎操作。

### 账号管理

云数据库 Tair（兼容 Redis）支持在一个实例中创建20个账号，您可以根据使用情况给这些账号设置相应的权限，从而更加灵活地管理实例，最大限度地避免误操作。

**前提条件**

云数据库 Tair（兼容Redis）用户指实例的引擎版本为Redis 4.0或以上。

**说明**

非Redis4.0版本实例只有默认账号，默认账号在创建实例时同时创建，如果需要修改默认账号密码，请参见修改密码。

**背景信息**

账号管理支持创建账号、删除账号、重置密码、修改权限等功能。创建账号后，当连接上数据库时，即可在命令行中使用账号及相应权限对数据库进行操作。

**创建账号**

1. 登录云数据库Tair（兼容Redis）控制台。
2. 在**实例列表**页，单击目标实例ID。
3. 在**实例信息**页，单击左侧导航栏中**账号管理**。

**说明**

4. 在**账号管理**页，单击右侧的**创建账号**。
5. 在弹出的对话框中，进行如下设置并单击**确定**。

| 设置 | 说明 |
|---|---|
| 账号 | 账号需以字母开头，由小写字母、数字、下划线组成，长度不超过16个字符。 |
| 权限设置 | 设置该账号所拥有的权限，分为只读、读写和复制三种。拥有复制权限的账号在连接Redis实例时可以使用SYNC/PSYNC命令。 说明目前仅4.0以上的Redis标准版实例支持创建有复制权限的账号。 |
| 密码 | 设置该账号的密码。密码长度为8~32个字符，需至少包含大写字母、小写字母、数字和特殊字符中的三种。支持的特殊字符为： !@#$%^&*()+-= 。 _ |
| 确认密码 | 再次输入密码进行确认。 |
| 备注说明 | 填入账号的备注信息。 |

### 重启实例

您可以在控制台的实例列表中重启Redis实例。

**操作步骤**

云数据库 Tair（兼容Redis）用户指
1. 登录云数据库Tair（兼容Redis）控制台。
2. 在目标实例的**操作**列，选择**重启实例**。

**警告**

重启过程中实例会发生秒级闪断，请您在业务低峰期重启，并确保应用程序具备重连机制。
3. 在弹出的对话框中，选择重启时间，勾选**我已了解重启风险**并单击**确认**。
立即重启：单击确认后实例重启。 可维护时间窗重启：在设置的可维护时间段重启。

### 导出实例列表

**操作步骤**

1. 登录云数据库Tair（兼容Redis）控制台。
2. 在**实例列表**页，单击右上方的导出实例列表
图标。
3. 在**导出资源列表**对话框勾选需要导出的信息，之后单击**确认**。
单击**确认**后，浏览器开始下载.csv格式的实例列表，您可以用文本编辑工具查看该文

**说明**

件。

### 管理标签

在实例数量较多的情况下，您可以创建多个标签，为实例绑定不同的标签对其进行分类，后续可通过标签筛选实例。

**注意事项**

标签由一对键值组成，键在同账号同地域下唯一，值无此限制。

**说明**

一个键可以有0到多个值。 每个实例最多可以绑定20个标签。 单次绑定或者解绑的标签数量不能超过20个。

**新建标签**

1. 登录云数据库Tair（兼容Redis）控制台。
2. 选中要批量添加标签的实例，单击实例列表下方的**批量绑定标签**。
3. 在**标签键**和**标签值**下方的文本框中输入需要绑定的标签键和标签值。
如果您需要绑定已有标签，也可以单击对应文本框，在下拉列表中选择已有标签键和标签值。
4. 单击**确定**。

**根据标签筛选实例**

云数据库 Tair（兼容Redis）用户指
1. 登录云数据库Tair（兼容Redis）控制台。
2. 在**实例列表**页面，单击**高级筛选**。
3. 在**标签筛选**右侧，下拉选择需要筛选的**标签键**和**标签值**。

**说明**

新建标签或更新现有标签后，需要先刷新页面才能在标签列表中看到更新后的标签。 如需清除筛选，单击已选中标签右侧的图标。
4. 单击**搜索**。

### Lua脚本支持与限制

云数据库 Tair（兼容 Redis）实例支持Lua相关命令。

**Lua命令支持**

Lua脚本的使用进一步提升了Redis的性能。通过内嵌对Lua环境的支持，Redis解决了长久以来不能高效地处理CAS（check-and-set）命令的缺点，并且可以通过组合使用多个命令，轻松实现以前很难实现或者不能高效实现的模式。

**说明**

如果发现无法执行Eval相关命令，例如提示 `ERR command eval not support for normal user` ，

**Lua使用限制**

为了保证脚本里面的所有操作都在相同slot进行，云数据库Redis集群版本会对Lua脚本做如下限制： 所有key都应该由KEYS数组来传递，**redis.call/pcall**中调用的Redis命令，key的位置必须是KEYS array（不能使用Lua变量替换KEYS），否则直接返回错误信息：

```
-ERR bad lua script for redis cluster, all the keys that the script uses should be pa ssed using the KEYS array\r\n
```

所有key必须在一个slot上，否则返回错误信息：

```
-ERR eval/evalsha command keys must be in same slot\r\n
```

调用必须要带有key，否则直接返回错误信息：

```
-ERR for redis cluster, eval/evalsha number of keys can't be negative or zero\r\n
```

不支持发布订阅命令，包括**PSUBSCRIBE**、**PUBSUB**、**PUBLISH**、**PUNSUBSCRIBE**、**SUBSCRIBE**和**UNSUBSCRIBE**。 不支持UNPACK函数。

**说明**

如果用户能够在代码中确保所有操作都在相同slot，且希望打破Redis集群的Lua限制，可以在控制台将script_check_enable修改为0，则后端不会对脚本进行校验。 云数据库 Tair（兼容Redis）用户指

## 连接指南

### 查看连接地址

您可以在控制台上查看Tair实例的私网和公网连接地址。

**注意事项**

Tair实例的VIP地址在服务维护或者变动时可能发生变化，建议在业务中使用连接地址访问Tair实例，确保连接的可用性。

**操作步骤**

1. 登录云数据库Tair（兼容Redis）控制台。
2. 在**实例列表**页，单击目标实例ID。
3. 在**连接信息**区域框，可查看到实例的私网连接地址和公网连接地址。

**说明**

实例默认提供私网连接地址，如需公网连接地址，请手动申请。具体操作，请参见申请连接地址。

**开启或关闭IPv6**

1. 登录云数据库Tair（兼容Redis）控制台。
2. 在**实例列表**页，单击目标实例ID。
3. 在连接信息区域，打开或关闭**是否应用了****IPv6**列下的开关。

**重要**

关闭IPv6连接地址后，通过IPv6地址访问数据库的业务连接将会中断，可能对正在运行的业务造成影响。请确认当前没有业务通过IPv6地址连接数据库后再进行操作。
4. 单击**确定**。

### 申请连接地址

**操作步骤**

1. 登录云数据库Tair（兼容Redis）控制台。
2. 在**实例列表**页，单击目标实例ID。
3. 在**连接信息**区域框中，选择目标**网络类型**，在**操作**列单击**申请连接地址**。
4. 在弹出的对话框中，输入自定义的连接地址和端口，然后单击**确定**。
云数据库 Tair（兼容Redis）用户指

**说明**

自定义连接地址由字母，数字组成，小写字母开头，长度为8~64个字符。 自定义端口范围为1024~65535，默认为6379。 申请连接地址后需要将访问的IP地址添加到白名单才可以访问Redis实例，添加白名单请参
5. 在**实例信息**页，查看**连接信息**的连接地址。

**说明**

如果不再需要连接地址，单击相关连接地址右侧的**释放连接地址**按钮释放该地址。

### 修改连接地址

云数据库 Tair（兼容 Redis）支持修改实例的内网和外网连接地址。更换实例时，您可以将新实例的连接地址修改为原实例的连接地址，无需对应用程序进行其它修改。

**前提条件**

实例状态为运行中。

**操作步骤**

1. 登录云数据库Tair（兼容Redis）控制台。
2. 在**实例列表**页，单击目标实例ID。
3. 在**实例信息**页，单击**连接信息**右侧的**修改连接地址**。
4. 在**修改连接地址**对话框，配置以下信息。

| 配置 | 说明 |
|---|---|
| 连接类型 | 选择私网地址和公网地址。 |
| 连接地址 | 设置连接地址前缀。 由小写字母、数字组成。 以小写字母开头。 长度为8~64个字符。 |
| 端口 | 设置端口，可设置范围为1024~65535。 说明公网地址的端口号修改生效大约需要10分钟，请生效后刷新页面查看最新端口号信息。 |

5. 在**修改连接地址**对话框，选择**连接类型**，修改**连接地址**的前缀和**端口**，之后单击**确定**。
云数据库 Tair（兼容Redis）用户指

**说明**

自定义前缀需由小写英文字母和数字组成，以小写字母开头，长度为8~64字符。 自定义端口范围为1024~65535，默认为6379。

### 使用直连模式连接实例

如果您申请直连访问地址，您可以将原生Redis集群架构无缝迁移到该实例中。云数据库 Tair（兼容 Redis）的直连地址支持原生Redis Cluster协议，在该模式下，客户端将直接与数据服务器进行连接，服务的响应速度非常快。

**前提条件**

使用Jedis、PhpRedis等支持Redis Cluster的客户端。

**说明**

使用不支持Redis Cluster的客户端，可能因客户端无法重定向请求到正确的分片而获取不到需要的数据。 您可以在Redis官网的客户端列表里查找更多支持Redis Cluster的客户端。 客户端所在的ECS与实例在同一VPC网络（相同VPC ID）。

**背景信息**

开启直连访问时，云数据库 Tair（兼容 Redis）会为该集群中所有数据分片的master节点分配一个虚拟 IP（VIP）地址。客户端在首次向直连地址发送请求前会通过DNS服务器解析直连地址，解析结果会是集群中一个随机数据分片的VIP。获取到VIP后，客户端即可通过Redis Cluster协议操作该集群中的数据。下图展示了直连模式下集群的服务架构。

|  | DN |
|---|---|
|  | andom |

ECS

**First time**

**VIP 2**

**VIP N**

**VIP 1**

**Data Shard 1**

**Data Shard 2**

**Data Shard N**

Master 1 Master 2 Master N ... HA HA HA Replica 1 Replica 2 Replica N

**注意事项**

云数据库 Tair（兼容Redis）用户指由于部署架构的不同，相对标准架构来说，集群架构的实例在原生Redis命令的支持上有一定的区别（例如Lua存在使用限制等）。 直连模式支持使用**SELECT**命令切换DB，但部分Redis Cluster客户端（例如stackExchange.redis） 不支持**SELECT**命令，如果使用该类客户端则只能使用DB0。 直连地址仅支持通过阿里云内网访问。 直连方式仅限集群版本。 使用集群架构直连地址连接实例。

**重要**

使用直连地址连接时必须添加-c参数，否则会导致连接失败。

```
./redis-cli -h r-bp1zxszhcgatnx****.redis.rds.aliyuncs.com -p 6379 -c
```

完成密码验证。

```
AUTH testaccount:Rp829dlwa
```

**Jedis**

本示例的Jedis版本为4.3.0，更多信息请参见Jedis。 使用自定义连接池（推荐） 云数据库 Tair（兼容Redis）用户指

```java
import redis.clients.jedis.*; import java.util.HashSet; import java.util.Set; public class DirectTest {
    private static final int DEFAULT_TIMEOUT = 2000;
    private static final int DEFAULT_REDIRECTIONS = 5;
    private static final ConnectionPoolConfig config = new ConnectionPoolConfig();
    public static void main(String args[]) {
```

`//` 最大连接数，由于直连模式为客户端直接连接某个数据库分片，需要保证：业务机器数 `* MaxTotal` < 单个数据库分片的最大连接数。

```
        config.setMaxTotal(30);
```

`//` 最大空闲连接数, 根据业务需要设置。

```
        config.setMaxIdle(20);
        config.setMinIdle(15);
```

`//` 开通直连访问时申请到的直连地址。`String host = "r-`

```
bp1xxxxxxxxxxxx.redis.rds.aliyuncs.com";
        int port = 6379;
```

`//` 实例的密码。String password = "xxxxx";

```
        Set<HostAndPort> jedisClusterNode = new HashSet<HostAndPort>();
        jedisClusterNode.add(new HostAndPort(host, port));
        JedisCluster jc = new JedisCluster(jedisClusterNode, DEFAULT_TIMEOUT,
DEFAULT_TIMEOUT, DEFAULT_REDIRECTIONS,
            password, "clientName", config);
        jc.set("key", "value");
        jc.get("key");
```

jc.close(); // 当应用退出，需销毁资源时，调用此方法。此方法会断开连接、释放资源。

```
    }
}
```

使用默认连接池云数据库 Tair（兼容Redis）用户指

```java
import redis.clients.jedis.ConnectionPoolConfig; import redis.clients.jedis.HostAndPort; import redis.clients.jedis.JedisCluster; import java.util.HashSet; import java.util.Set; public class DirectTest{
    private static final int DEFAULT_TIMEOUT = 2000;
    private static final int DEFAULT_REDIRECTIONS = 5;
    private static final ConnectionPoolConfig DEFAULT_CONFIG = new
ConnectionPoolConfig();
    public static void main(String args[]){
```

`//` 开通直连访问时申请到的直连地址。`String host = "r-`

```
bp1xxxxxxxxxxxx.redis.rds.aliyuncs.com";
        int port = 6379;
        String password = "xxxx";
        Set<HostAndPort>  jedisClusterNode = new HashSet<HostAndPort>();
        jedisClusterNode.add(new HostAndPort(host, port));
        JedisCluster jc = new JedisCluster(jedisClusterNode, DEFAULT_TIMEOUT,
DEFAULT_TIMEOUT,
            DEFAULT_REDIRECTIONS,password, "clientName", DEFAULT_CONFIG);
        jc.set("key","value");
        jc.get("key");
```

jc.close(); // 当应用退出，需销毁资源时，调用此方法。此方法会断开连接、释放资源。

```
    }
}
```

**PhpRedis**

本示例的PhpRedis版本为5.3.7，更多信息请参见PhpRedis。

```
<?php// 直连地址和连接端口。$array = ['r-bp1xxxxxxxxxxxx.redis.rds.aliyuncs.com:6379'];
```

`//` 连接密码。$pwd = "xxxx";

```
 // 使用密码连接集群。$obj_cluster = new RedisCluster(NULL, $array, 1.5, 1.5, true, $pwd);
```

`//` 输出连接结果。var_dump($obj_cluster);

```
 if ($obj_cluster->set("foo", "bar") == false) {
     die($obj_cluster->getLastError());
 }
 $value = $obj_cluster->get("foo");
 echo $value;
```

?>

**redis-py**

本示例的Python版本为3.9、redis-py版本为4.4.1，更多信息请参见redis-py。 云数据库 Tair（兼容Redis）用户指

```bash
# !/usr/bin/env python# -*- coding: utf-8 -*-from redis.cluster import RedisCluster
```

# 分别将`host`和`port`的值替换为实例的连接地址、端口号。

```
host = 'r-bp10noxlhcoim2****.redis.rds.aliyuncs.com'
```

`port = 6379#` 分别将`user`和`pwd`的值替换为实例的账号和密码。

```
user = 'testaccount' pwd = 'Rp829dlwa' rc = RedisCluster(host=host, port=port, username=user, password=pwd)
```

# 连接建立后即可执行数据库操作，下述代码为您提供`SET`与`GET`的使用示例。

```python
rc.set('foo', 'bar') print(rc.get('foo'))
```

**Spring Data Redis**

本示例使用Maven方式进行构建，您也可以手动下载Lettuce或Jedis客户端。
1. 添加下述Maven依赖。

```xml
<?xml version="1.0" encoding="UTF-8"?> <project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0
https://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <parent>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-parent</artifactId>
        <version>2.4.2</version>
        <relativePath/> <!-- lookup parent from repository -->
    </parent>
    <groupId>com.aliyun.tair</groupId>
    <artifactId>spring-boot-example</artifactId>
    <version>0.0.1-SNAPSHOT</version>
    <name>spring-boot-example</name>
    <description>Demo project for Spring Boot</description>
    <properties>
        <java.version>1.8</java.version>
    </properties>
    <dependencies>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-test</artifactId>
            <scope>test</scope>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-data-redis</artifactId>
        </dependency>
        <dependency>
            <groupId>redis.clients</groupId>
            <artifactId>jedis</artifactId>
</dependency>
```

云数据库 Tair（兼容Redis）用户指

```xml
        </dependency>
        <dependency>
            <groupId>io.lettuce</groupId>
            <artifactId>lettuce-core</artifactId>
            <version>6.3.0.RELEASE</version>
        </dependency>
        <dependency>
            <groupId>io.netty</groupId>
            <artifactId>netty-transport-native-epoll</artifactId>
            <version>4.1.100.Final</version>
            <classifier>linux-x86_64</classifier>
        </dependency>
    </dependencies>
    <build>
        <plugins>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
            </plugin>
        </plugins>
    </build>
</project>
```

2. 在Spring Data Redis编辑器中输入下述代码，然后根据注释提示修改代码。
本示例的Spring Data Redis版本为2.4.2。 （推荐）Spring Data Redis With Jedis

```
@Bean
     JedisConnectionFactory redisConnectionFactory() {
         List<String> clusterNodes = Arrays.asList("r-
bp10noxlhcoim2****.redis.rds.aliyuncs.com:6379");
         RedisClusterConfiguration redisClusterConfiguration = new
RedisClusterConfiguration(clusterNodes);
         redisClusterConfiguration.setUsername("user");
         redisClusterConfiguration.setPassword("password");
         JedisPoolConfig jedisPoolConfig = new JedisPoolConfig();
```

`//` 最大空闲连接数，由于直连模式为客户端直接连接某个数据库分片，需要保证：业务机器数 `* Ma` `xTotal <` 单个数据库分片的最大连接数。

```
         jedisPoolConfig.setMaxTotal(30);
```

`//` 最大空闲连接数, 根据业务需要设置。

```
         jedisPoolConfig.setMaxIdle(20);
```

`//` 关闭 testOn[Borrow|Return]，防止产生额外的 `PING`

```
         jedisPoolConfig.setTestOnBorrow(false);
         jedisPoolConfig.setTestOnReturn(false);
         return new JedisConnectionFactory(redisClusterConfiguration,
jedisPoolConfig);
     }
```

Spring Data Redis With Lettuce

**重要**

云数据库 Tair（兼容Redis）用户指 Lettuce 默认配置可能导致实例变更时应用延迟增加和无法访问等问题。 Lettuce 的版本应大于等于 6.3.0.RELEASE。 云数据库 Tair（兼容Redis）用户指

```
     /**
```

`* TCP_KEEPALIVE`打开，并且配置三个参数分别为:

```
     *  TCP_KEEPIDLE = 30
     *  TCP_KEEPINTVL = 10
     *  TCP_KEEPCNT = 3
     */private static final int TCP_KEEPALIVE_IDLE = 30;
    /**
```

`* TCP_USER_TIMEOUT`参数可以避免在故障宕机场景下，`Lettuce`持续超时的问题。

```
     * refer: https://github.com/lettuce-io/lettuce-core/issues/2082
     */private static final int TCP_USER_TIMEOUT = 30;
    @Beanpublic LettuceConnectionFactory redisConnectionFactory() {
        List<String> clusterNodes = Arrays.asList("r-
bp10noxlhcoim2****.redis.rds.aliyuncs.com:6379");
        RedisClusterConfiguration redisClusterConfiguration = new
RedisClusterConfiguration(clusterNodes);
        redisClusterConfiguration.setUsername("user");
        redisClusterConfiguration.setPassword("password");
        // Config TCP KeepAliveSocketOptions socketOptions =
SocketOptions.builder()
            .keepAlive(KeepAliveOptions.builder()
                .enable()
                .idle(Duration.ofSeconds(TCP_KEEPALIVE_IDLE))
                .interval(Duration.ofSeconds(TCP_KEEPALIVE_IDLE / 3))
                .count(3)
                .build())
            .tcpUserTimeout(TcpUserTimeoutOptions.builder()
                .enable()
                .tcpUserTimeout(Duration.ofSeconds(TCP_USER_TIMEOUT))
                .build())
            .build();
        ClusterTopologyRefreshOptions topologyRefreshOptions =
ClusterTopologyRefreshOptions.builder()
            .enablePeriodicRefresh(Duration.ofSeconds(60))
            .dynamicRefreshSources(false)
            .enableAllAdaptiveRefreshTriggers()
            .adaptiveRefreshTriggersTimeout(Duration.ofSeconds(15)).build();
        LettuceClientConfiguration lettuceClientConfiguration =
LettuceClientConfiguration.builder().
            clientOptions(ClusterClientOptions.builder()
                .socketOptions(socketOptions)
                .validateClusterNodeMembership(false)
                .topologyRefreshOptions(topologyRefreshOptions).build()).build();
        return new LettuceConnectionFactory(redisClusterConfiguration,
lettuceClientConfiguration);
    }
```

**.Net**

云数据库 Tair（兼容Redis）用户指本示例的.Net版本为6.0，StackExchange.Redis版本为2.6.90。

```
using StackExchange.Redis; class RedisConnSingleton {
```

`//` 分别设置实例的连接地址、端口号和用户名、密码。`private static ConfigurationOptions config`

```
urationOptions = ConfigurationOptions.Parse("rbp10noxlhcoim2****.redis.rds.aliyuncs.com:6379,user=testaccount,password=Rp829dlwa,connec imeout=2000");
    //the lock for singletonprivate static readonly object Locker = new object();
    //singletonprivate static ConnectionMultiplexer redisConn;
    //singletonpublic static ConnectionMultiplexer getRedisConn()
    {
        if (redisConn == null)
        {
            lock (Locker)
            {
                if (redisConn == null || !redisConn.IsConnected)
                {
                    redisConn = ConnectionMultiplexer.Connect(configurationOptions);
                }
            }
        }
        return redisConn;
    }
} class Program {
    static void Main(string[] args)
    {
        ConnectionMultiplexer cm = RedisConnSingleton.getRedisConn();
        var db = cm.GetDatabase();
        db.StringSet("key", "value");
        String ret = db.StringGet("key");
        Console.WriteLine("get key: " + ret);
    }
}
```

**node-redis**

本示例的Node.js版本为19.4.0、node-redis版本为4.5.1。 云数据库 Tair（兼容Redis）用户指

```java
import { createCluster } from 'redis';
```

`//` 分别设置实例的端口号、连接地址、账号、密码，`//` 注意，在`url`中配置用户和密码之后，还需要在`defaults`中设置全局用户和密码，`//` 用于其余节点的认证，否则将出现`NOAUTH`的错误。`const cluster = createCluster(`

```
{
    rootNodes: [{
        url: 'redis://testaccount:Rp829dlwa@r-
bp10noxlhcoim2****.redis.rds.aliyuncs.com:6379'
    }],
    defaults: {
        username: 'testaccount',
        password: 'Rp829dlwa'
    }
}); cluster.on('error', (err) => console.log('Redis Cluster Error', err)); await cluster.connect(); await cluster.set('key', 'value'); const value = await cluster.get('key'); console.log('get key: %s', value); await cluster.disconnect();
```

**Go-redis**

本示例的Go版本为1.19.7、Go-redis版本为9.5.1。

**重要**

请使用Go-redis v9.0及以上版本。 云数据库 Tair（兼容Redis）用户指

```java
package main import (
 "context""fmt""github.com/go-redis/redis/v9"
```

)

```
var ctx = context.Background() func main() {
 rdb := redis.NewClusterClient(&redis.ClusterOptions{
  Addrs:    []string{"r-bp10noxlhcoim2****.redis.rds.aliyuncs.com:6379"},
  Username: "testaccount",
  Password: "Rp829dlwa",
 })
 err := rdb.Set(ctx, "key", "value", 0).Err()
 if err != nil {
  panic(err)
 }
 val, err := rdb.Get(ctx, "key").Result()
 if err != nil {
  panic(err)
 }
 fmt.Println("key", val)
}
```

**Lettuce**

**重要**

Lettuce 默认配置可能导致实例变更时应用延迟增加和无法访问等问题。 Lettuce 的版本应大于等于 6.3.0.RELEASE。
1. 添加下述Maven依赖。

```xml
        <dependency>
            <groupId>io.lettuce</groupId>
            <artifactId>lettuce-core</artifactId>
            <version>6.3.0.RELEASE</version>
        </dependency>
        <dependency>
            <groupId>io.netty</groupId>
            <artifactId>netty-transport-native-epoll</artifactId>
            <version>4.1.65.Final</version>
            <classifier>linux-x86_64</classifier>
        </dependency>
```

2. 添加下述代码，并根据注释提示修改代码。

```java
import io.lettuce.core.RedisURI; import io.lettuce.core.SocketOptions; import io.lettuce.core.cluster.ClusterClientOptions;
```

云数据库 Tair（兼容Redis）用户指

```java
import io.lettuce.core.cluster.ClusterTopologyRefreshOptions; import io.lettuce.core.cluster.RedisClusterClient; import io.lettuce.core.cluster.api.StatefulRedisClusterConnection; import java.time.Duration; public class ClusterDemo {
    /**
```

`* TCP_KEEPALIVE` 打开，并且配置三个参数分别为：

```
     *  TCP_KEEPIDLE = 30
     *  TCP_KEEPINTVL = 10
     *  TCP_KEEPCNT = 3
     */private static final int TCP_KEEPALIVE_IDLE = 30;
    /**
```

`* TCP_USER_TIMEOUT`可以避免在故障宕机场景下`Lettuce`持续超时的问题。

```
     * refer: https://github.com/lettuce-io/lettuce-core/issues/2082
     */private static final int TCP_USER_TIMEOUT = 30;
    public static void main(String[] args) throws Exception {
```

`//` 分别将`host`、`port`和`password`的值替换为实际的实例信息。`String host = "r-`

```
bp1ln3c4kopj3l****.redis.rds.aliyuncs.com";
        int port = 6379;
        String password = "Da****3";
        RedisURI redisURI = RedisURI.Builder.redis(host)
                .withPort(port)
                .withPassword(password)
                .build();
        ClusterTopologyRefreshOptions refreshOptions =
ClusterTopologyRefreshOptions.builder()
                .enablePeriodicRefresh(Duration.ofSeconds(60))
                .dynamicRefreshSources(false)
                .enableAllAdaptiveRefreshTriggers()
                .adaptiveRefreshTriggersTimeout(Duration.ofSeconds(15)).build();
        // Config TCP KeepAliveSocketOptions socketOptions = SocketOptions.builder()
                .keepAlive(SocketOptions.KeepAliveOptions.builder()
                        .enable()
                        .idle(Duration.ofSeconds(TCP_KEEPALIVE_IDLE))
                        .interval(Duration.ofSeconds(TCP_KEEPALIVE_IDLE/3))
                        .count(3)
                        .build())
                .tcpUserTimeout(SocketOptions.TcpUserTimeoutOptions.builder()
                        .enable()
                        .tcpUserTimeout(Duration.ofSeconds(TCP_USER_TIMEOUT))
                        .build())
                .build();
        RedisClusterClient redisClient = RedisClusterClient.create(redisURI);
        redisClient.setOptions(ClusterClientOptions.builder()
                .socketOptions(socketOptions)
                .validateClusterNodeMembership(false)
```

t l Rf

```
hOti (
```

f

```
hOti )bild())
```

云数据库 Tair（兼容Redis）用户指

```java
                .topologyRefreshOptions(refreshOptions).build());
        StatefulRedisClusterConnection<String, String> connection =
redisClient.connect();
        connection.sync().set("key", "value");
        System.out.println(connection.sync().get("key"));
    }
}
```

3. 执行上述代码，预期会返回如下结果：

```
value
```

Lettuce 相关参数说明如下：

| 参数 | 默认配置 | 说明 | 修改配置 |
|---|---|---|---|
| enablePeriodicRefr esh(Duration refreshPeriod) | 关闭 | 启用后将进行周期性集群拓扑刷新。 | 建议配置为 60s。 开启此配置可以使不活跃的长连接也能及时更新本地拓扑。 |
| dynamicRefreshSo urces(boolean dynamicRefreshSo urces) | true | 为 true 时，使用 Cluster Nodes 命令返回的所有节点进行集群拓扑刷新；为 false 时，使用指定节点地址。 | 如无特殊需求，应配置为 false。 启用此选项会向所有节点发送 CLUSTER NODES 命令， 增加服务端压力。此外，在变配期间，使用 endpoint 地址更新拓扑通常更为迅速可靠。 |
| enableAllAdaptiveR efreshTriggers() | 关闭 | 启用后，当收到 MOVED 消息时，会自动刷新集群拓扑。 | 必须启用。 启用此配置才能确保拓扑变更后 Lettuce 能及时更新本地拓扑。 |
| adaptiveRefreshTri ggersTimeout(Dura tion timeout) | 30s | 限制集群拓扑刷新频率，在指定时间内仅允许一次刷新。 | 建议配置为 15s。 由于集群中多个节点的拓扑变更并非原子操作，Lettuce 触发的初次拓扑刷新可能会失败，因此需要快速进行后续刷新以确保拓扑正确更新。当应用数量较少时，由于不会有大量客户端同时发送 CLUSTER NODES 命令，可以适当降低该值，以实现更快的拓扑表收敛时间。 |
| validateClusterNod eMembership(bool ean validateClusterNod eMembership) | true | 在拓扑变化时，Lettuce 使用 MOVED 将命令重定向到正确的节点。启用此配置后，只允许将命令重定向到 CLUSTER NODES 输出中已知的节点。 | 必须配置为 false。 配置为 false 可以防止在集群拓扑变更后，本地拓扑刷新完成前无法访问新增节点。 |

云数据库 Tair（兼容Redis）用户指

### 使用客户端程序连接

云数据库 Tair（兼容 Redis）与原生Redis完全兼容，连接数据库的方式也基本相同，您可以根据自身应用特点选用任何兼容Redis协议的客户端程序。本文列举一些常见的客户端程序的代码示例，帮助您快速连接。

**前提条件**

已将ECS实例的内网IP地址或本地主机的外网IP地址加入实例白名单，具体操作，请参见设置白名单。

**获取连接信息**

| 需获取的信息 | 获取方式 |
|---|---|
| 实例的连接地址 | 可在实例信息页面中的连接信息区域框中获取到。 说明 Redis实例支持多种连接地址，推荐使用专有网络连接，可获得更高的安全性和更低的网络延迟。 |
| 端口号 | 端口号默认为6379。 |
| 实例的账号（部分客户端程序无需设置） | 实例默认会创建一个以实例ID命名的账号（例如r-bp10noxlhcoim2****）。 |
| 账号的密码 | 在创建实例时已设置，如果忘记密码，可重置密码，具体操作，请参见修改密码。 |

**常见客户端程序**

关于实例支持的客户端列表，请参见Redis Clients。 Jedis客户端 PhpRedis客户端 redis-py客户端 C或C++客户端 .net客户端 node-redis客户端 C#客户端StackExchange.Redis

**Jedis客户端**

1. 下载并安装Jedis客户端。具体操作，请参见Jedis使用说明。
2. 根据业务需求选择连接方式。
JedisPool连接池连接（推荐） 云数据库 Tair（兼容Redis）用户指 a. 打开Eclipse客户端，创建一个Project并配置pom文件，具体内容如下：

```xml
<dependency> <groupId>redis.clients</groupId> <artifactId>jedis</artifactId> <version>2.7.2</version> <type>jar</type> <scope>compile</scope> </dependency>
```

b. 在Project中输入下述代码添加相关应用。

```java
import org.apache.commons.pool2.PooledObject; import org.apache.commons.pool2.PooledObjectFactory; import org.apache.commons.pool2.impl.DefaultPooledObject; import org.apache.commons.pool2.impl.GenericObjectPoolConfig; import redis.clients.jedis.HostAndPort; import redis.clients.jedis.Jedis; import redis.clients.jedis.JedisPool; import redis.clients.jedis.JedisPoolConfig;
```

c. 根据Jedis客户端版本，在Project中输入下述代码，然后根据注释提示修改代码。

**说明**

关于如何获取Redis实例的连接地址和密码，请参见获取连接信息。 云数据库 Tair（兼容Redis）用户指 Jedis 2.7.2版本

```
JedisPoolConfig config = new JedisPoolConfig();
```

`//`最大空闲连接数，需自行评估，不超过`Redis`实例的最大连接数

```
config.setMaxIdle(200);
```

`//`最大连接数，需自行评估，不超过`Redis`实例的最大连接数

```
config.setMaxTotal(300); config.setTestOnBorrow(false); config.setTestOnReturn(false); String host = "*.aliyuncs.com"; String password = "密码"; JedisPool pool = new JedisPool(config, host, 6379, 3000, password); Jedis jedis = null; try { jedis = pool.getResource(); /// ... do stuff here ... for example jedis.set("foo", "bar"); String foobar = jedis.get("foo"); jedis.zadd("sose", 0, "car"); jedis.zadd("sose", 0, "bike"); Set<String> sose = jedis.zrange("sose", 0, -1); } finally { if (jedis != null) { jedis.close(); } } /// ... when closing your application: pool.destroy();
```

云数据库 Tair（兼容Redis）用户指 Jedis 2.6或Jedis 2.5版本

```
JedisPoolConfig config = new JedisPoolConfig();
```

`//`最大空闲连接数，需自行评估，不超过`Redis`实例的最大连接数

```
config.setMaxIdle(200);
```

`//`最大连接数，需自行评估，不超过`Redis`实例的最大连接数

```
config.setMaxTotal(300); config.setTestOnBorrow(false); config.setTestOnReturn(false); String host = "*.aliyuncs.com"; String password = "密码"; JedisPool pool = new JedisPool(config, host, 6379, 3000, password); Jedis jedis = null; boolean broken = false; try {
     jedis = pool.getResource();
     /// ... do stuff here ... for example
     jedis.set("foo", "bar");
     String foobar = jedis.get("foo");
     jedis.zadd("sose", 0, "car");
     jedis.zadd("sose", 0, "bike");
     Set<String> sose = jedis.zrange("sose", 0, -1);
} catch(Exception e) {
     broken = true;
} finally { if (broken) {
     pool.returnBrokenResource(jedis);
} else if (jedis != null) {
     pool.returnResource(jedis);
 }
}
```

Jedis单连接（不推荐，单次超时后无法自动恢复） 打开Eclipse客户端，创建一个Project，输入下述代码，然后根据注释提示修改代码。

**说明**

关于如何获取Redis实例的连接地址和密码，请参见获取连接信息。 云数据库 Tair（兼容Redis）用户指

```java
import redis.clients.jedis.Jedis; public class jedistest { public static void main(String[] args) { try {
```

String host = "xx.kvstore.aliyuncs.com";//控制台显示访问地址

```
     int port = 6379;
     Jedis jedis = new Jedis(host, port);
```

`//`鉴权信息

```
     jedis.auth("password");//password
     String key = "redis";
     String value = "aliyun-redis";
```

`//select db`默认为0

```
     jedis.select(1);
```

`//set`一个`key`

```java
     jedis.set(key, value);
     System.out.println("Set Key " + key + " Value: " + value);
```

`//get` 设置进去的`key`

```java
     String getvalue = jedis.get(key);
     System.out.println("Get Key " + key + " ReturnValue: " + getvalue);
     jedis.quit();
     jedis.close();
} catch (Exception e) {
 e.printStackTrace();
 }
} }
```

3. 运行上述Project，在Eclipse的控制台输出如下运行结果则表示您已成功连接至云数据库Redis。

```
Set Key redis Value aliyun-redis Get Key redis ReturnValue aliyun-redis
```

**PhpRedis客户端**

1. 下载并安装PhpRedis客户端。具体操作，请参见PhpRedis使用说明。
2. 在PHP编辑器中输入下述代码，然后根据注释提示修改代码。

**说明**

关于如何获取Redis实例的连接地址、账号和密码，请参见获取连接信息。 云数据库 Tair（兼容Redis）用户指

```
<?php
```

`/*` 这里替换为连接的实例连接地址和端口 `*/`

```
 $host = "r-bp10noxlhcoim2****.redis.rds.aliyuncs.com";
 $port = 6379;
```

`/*` 这里替换为实例`ID`和实例的密码 `*/`

```
 $user = "test_username";
 $pwd = "test_password";
 $redis = new Redis();
 if ($redis->connect($host, $port) == false) {
         die($redis->getLastError());
   }
 if ($redis->auth($pwd) == false) {
         die($redis->getLastError());
  }
```

`/*` 认证后就可以进行数据库操作，详情请参见`https://github.com/phpRedis/phpredis */`

```
 if ($redis->set("foo", "bar") == false) {
         die($redis->getLastError());
 }
 $value = $redis->get("foo");
 echo $value;
```

?>
3. 执行上述代码即可完成连接。
更多信息，请参见官方文档。

**redis-py客户端**

1. 下载并安装redis-py客户端。具体操作，请参见redis-py使用说明。
2. 在Python编辑器中输入下述代码，然后根据注释提示修改代码。

**说明**

关于如何获取Redis实例的连接地址和密码，请参见获取连接信息。

```java
#!/usr/bin/env python
#-*- coding: utf-8 -*-
import redis
```

#替换`host`的值为实例的连接地址，替换`port`的值为端口。

```
host = 'localhost' port = 6379
```

#这里替换为实例`password`

```
pwd = 'test_password' r = redis.StrictRedis(host=host, port=port, password=pwd)
```

#连接建立后就可以进行数据库操作，详情请参见`https://github.com/andymccurdy/redis-py`

```
r.set('foo', 'bar'); print r.get('foo')
```

3. 执行上述代码即可完成连接。

**C或C++客户端**

1. 执行下述命令，下载并编译安装Ｃ客户端。
云数据库 Tair（兼容Redis）用户指

```bash
git clone https://github.com/redis/hiredis.git cd hiredis make sudo make install
```

2. 在C或C++编辑器中输入下述代码，然后根据注释提示修改代码。

**说明**

关于如何获取Redis实例的连接地址和密码，请参见获取连接信息。

```
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <hiredis.h>
int main(int argc, char **argv) { unsigned int j; redisContext *c; redisReply *reply; if (argc < 4) {
        printf("Usage: example xxx.kvstore.aliyuncs.com 6379 instance_id
password\n");
        exit(0);
} const char *hostname = argv[1]; const int port = atoi(argv[2]); const char *instance_id = argv[3]; const char *password = argv[4]; struct timeval timeout = { 1, 500000 }; // 1.5 seconds c = redisConnectWithTimeout(hostname, port, timeout); if (c == NULL || c->err) { if (c) {
        printf("Connection error: %s\n", c->errstr);
        redisFree(c);
} else {
        printf("Connection error: can't allocate redis context\n");
} exit(1); } /* AUTH */ reply = redisCommand(c, "AUTH %s", password); printf("AUTH: %s\n", reply->str); freeReplyObject(reply); /* PING server */ reply = redisCommand(c,"PING"); printf("PING: %s\n", reply->str); freeReplyObject(reply); /* Set a key */ reply = redisCommand(c,"SET %s %s", "foo", "hello world"); printf("SET: %s\n", reply->str); freeReplyObject(reply); /* Set a key using binary safe API */ reply = redisCommand(c,"SET %b %b", "bar", (size_t) 3, "hello", (size_t) 5); printf("SET(binaryAPI):%s\n" reply->str);
```

云数据库 Tair（兼容Redis）用户指

```
printf(SET (binary API): %s\n, reply>str); freeReplyObject(reply); /* Try a GET and two INCR */ reply = redisCommand(c,"GET foo"); printf("GET foo: %s\n", reply->str); freeReplyObject(reply); reply = redisCommand(c,"INCR counter"); printf("INCR counter: %lld\n", reply->integer); freeReplyObject(reply); /* again ... */ reply = redisCommand(c,"INCR counter"); printf("INCR counter: %lld\n", reply->integer); freeReplyObject(reply); /* Create a list of numbers, from 0 to 9 */ reply = redisCommand(c,"DEL mylist"); freeReplyObject(reply); for (j = 0; j < 10; j++) {
        char buf[64];
        snprintf(buf,64,"%d",j);
        reply = redisCommand(c,"LPUSH mylist element-%s", buf);
        freeReplyObject(reply);
    }
/* Let's check what we have inside the list */ reply = redisCommand(c,"LRANGE mylist 0 -1"); if (reply->type == REDIS_REPLY_ARRAY) {
        for (j = 0; j < reply->elements; j++) {
        printf("%u) %s\n", j, reply->element[j]->str);
} } freeReplyObject(reply); /* Disconnects and frees the context */ redisFree(c); return 0; }
```

3. 编译上述代码。

```
gcc -o example -g example.c -I /usr/local/include/hiredis -lhiredis
```

4. 测试运行，完成连接。

```
 example xxx.kvstore.aliyuncs.com 6379 instance_id password
```

**.net客户端**

**警告**

如果您的Redis实例为集群版，且需要执行切换或选择数据库的操作（即使用多数据库功能），您必须先将**cluster_compat_enable**参数设置为0（即关闭原生Redis Cluster语法兼容），然后重启客户端应用，否则将提示报错： Multiple databases are not supported on this server; cannot `switch to database` 。具体操作，请参见参数设置。
1. 执行下述命令，下载.net客户端。
云数据库 Tair（兼容Redis）用户指

```
 git clone https://github.com/ServiceStack/ServiceStack.Redis
```

2. 在.net 客户端中新建.net项目。
3. 添加客户端引用，引用文件在库文件的ServiceStack.Redis/lib/tests中。
4. 在新建的.net项目中输入如下代码，然后根据注释提示修改代码。更多信息，请参见接口说明。

**说明**

关于如何获取Redis实例的连接地址和密码，请参见获取连接信息。

```
using System;
 using System.Collections.Generic;
 using System.Linq;
 using System.Text;
 using System.Threading.Tasks;
 using ServiceStack.Redis;
 namespace ServiceStack.Redis.Tests
 {
         class Program
 {
 public static void RedisClientTest()
 {
         string host = "127.0.0.1";/*访问host地址*/
         string password = "password";/*密码*/
         RedisClient redisClient = new RedisClient(host, 6379, password);
         string key = "test-aliyun";
         string value = "test-aliyun-value";
         redisClient.Set(key, value);
         string listKey = "test-aliyun-list";
         System.Console.WriteLine("set key " + key + " value " + value);
         string getValue =
System.Text.Encoding.Default.GetString(redisClient.Get(key));
         System.Console.WriteLine("get key " + getValue);
         System.Console.Read();
 }
 public static void RedisPoolClientTest()
 {
         string[] testReadWriteHosts = new[] {
         "redis://password@127.0.0.1:6379"/*redis://密码@访问地址:端口*/
 };
 RedisConfig.VerifyMasterConnections = false;//需要设置
 PooledRedisClientManager redisPoolManager = new PooledRedisClientManager(10/*连接池个
```

数`*/, 10/*`连接池超时时间*/, testReadWriteHosts);

```
 for (int i = 0; i < 100; i++){
         IRedisClient redisClient = redisPoolManager.GetClient();//获取连接
         RedisNativeClient redisNativeClient = (RedisNativeClient)redisClient;
         redisNativeClient.Client = null;//ApsaraDB for Redis不支持client setname所以这
```

里需要显示的把`client`对象置为`null`

```
 try
 {
         string key = "test-aliyun1111";
         string value = "test-aliyun-value1111";
         redisClient.Set(key, value);
```

云数据库 Tair（兼容Redis）用户指 `y,`

```
         string listKey = "test-aliyun-list";
         redisClient.AddItemToList(listKey, value);
         System.Console.WriteLine("set key " + key + " value " + value);
         string getValue = redisClient.GetValue(key);
         System.Console.WriteLine("get key " + getValue);
         redisClient.Dispose();//
 }catch (Exception e)
 {
         System.Console.WriteLine(e.Message);
 }
 }
         System.Console.Read();
 }
 static void Main(string[] args)
 {
```

`//`单链接模式

```
         RedisClientTest();
```

`//`连接池模式

```
         RedisPoolClientTest();
 }
 }
 }
```

**node-redis客户端**

1. 下载并安装node-redis。

```
npm install hiredis redis
```

2. 在node-redis客户端中输入下述代码，然后根据注释提示修改代码。

**说明**

关于如何获取Redis实例的连接地址和密码，请参见获取连接信息。

```
 var redis = require("redis"),
 client = redis.createClient(<port>, <"host">, {detect_buffers: true});
 client.auth("password", redis.print)
```

参数说明： <port>：Redis实例的服务端口，默认为6379。 <"host">：Redis实例的连接地址。 配置示例：

```
var redis = require("redis"), client = redis.createClient(6379, "r-abcdefg.redis.rds.aliyuncs.com", {detect_buffers: true}); client.auth("password", redis.print)
```

3. 执行上述代码完成连接。
4. 使用数据库。
云数据库 Tair（兼容Redis）用户指 `//` 写入数据

```
 client.set("key", "OK");
```

`//` 获取数据，返回`String`

```
 client.get("key", function (err, reply) {
 console.log(reply.toString()); // print `OK`
 });
```

`//` 如果传入一个`Buffer`，返回也是一个`Buffer`

```
 client.get(new Buffer("key"), function (err, reply) {
 console.log(reply.toString()); // print `<Buffer 4f 4b>`
 });
 client.quit();
```

**C#客户端StackExchange.Redis**

**警告**

如果您的Redis实例为集群版，且需要执行切换或选择数据库的操作（即使用多数据库功能），您必须

|  | RedisCommandException: Multiple databases are not supported |
|---|---|
| on this server; cannot switch to database: 1 |  |

1. 下载并安装StackExchange.Redis。
2. 添加引用。

```
using StackExchange.Redis;
```

3. 初始化ConnectionMultiplexer。
ConnectionMultiplexer是StackExchange.Redis的核心，它被整个应用程序共享和重用，应该设置为单例，它的初始化如下：

**说明**

关于如何获取Redis实例的连接地址和密码，请参见获取连接信息。 ConfigurationOptions包含很多选项，例如keepAlive、connectRetry、name，详情请参见ConfigurationOptions。 云数据库 Tair（兼容Redis）用户指

```java
 // redis config
 private static ConfigurationOptions configurationOptions =
ConfigurationOptions.Parse("127.0.0.1:6379,password=xxx,connectTimeout=2000");
  //the lock for singleton
 private static readonly object Locker = new object();
  //singleton
 private static ConnectionMultiplexer redisConn;
 //singleton
 public static ConnectionMultiplexer getRedisConn()
 {
     if (redisConn == null)
     {
         lock (Locker)
         {
             if (redisConn == null || !redisConn.IsConnected)
             {
                 redisConn = ConnectionMultiplexer.Connect(configurationOptions);
             }
         }
     }
     return redisConn;
 }
```

4. 由于GetDatabase()返回的对象是轻量级的，每次用的时候从ConnectionMultiplexer对象中获取即
可。

```
 redisConn = getRedisConn();
 var db = redisConn.GetDatabase();
```

5. 通过客户端程序操作Redis数据库。

**说明**

下文列出常见数据接口的demo示例，和原生API略有不同。 云数据库 Tair（兼容Redis）用户指

```
//set get string strKey = "hello"; string strValue = "world"; bool setResult = db.StringSet(strKey, strValue); Console.WriteLine("set " + strKey + " " + strValue + ", result is " + setResult); //incr string counterKey = "counter"; long counterValue = db.StringIncrement(counterKey); Console.WriteLine("incr " + counterKey + ", result is " + counterValue); //expire db.KeyExpire(strKey, new TimeSpan(0, 0, 5)); Thread.Sleep(5 * 1000); Console.WriteLine("expire " + strKey + ", after 5 seconds, value is " + db.StringGe t(strKey)); //mset mget KeyValuePair<RedisKey, RedisValue> kv1 = new KeyValuePair<RedisKey, RedisValue>("ke y1", "value1"); KeyValuePair<RedisKey, RedisValue> kv2 = new KeyValuePair<RedisKey, RedisValue>("ke y2", "value2"); db.StringSet(new KeyValuePair<RedisKey, RedisValue>[] {kv1,kv2}); RedisValue[] values = db.StringGet(new RedisKey[] {kv1.Key, kv2.Key}); Console.WriteLine("mget " + kv1.Key.ToString() + " " + kv2.Key.ToString() + ", resu lt is " + values[0] + "&&" + values[1]);
```

Hash

```
string hashKey = "myhash"; //hset db.HashSet(hashKey,"f1","v1"); db.HashSet(hashKey,"f2", "v2"); HashEntry[] values = db.HashGetAll(hashKey); //hgetall Console.Write("hgetall " + hashKey + ", result is"); for (int i = 0; i < values.Length;i++) {
  HashEntry hashEntry = values[i];
  Console.Write(" " + hashEntry.Name.ToString() + " " +
hashEntry.Value.ToString()); } Console.WriteLine();
```

List 云数据库 Tair（兼容Redis）用户指

```
//list key string listKey = "myList"; //rpush db.ListRightPush(listKey, "a"); db.ListRightPush(listKey, "b"); db.ListRightPush(listKey, "c"); //lrange RedisValue[] values = db.ListRange(listKey, 0, -1); Console.Write("lrange " + listKey + " 0 -1, result is "); for (int i = 0; i < values.Length; i++) {
 Console.Write(values[i] + " ");
} Console.WriteLine();
```

Set

```
//set key string setKey = "mySet"; //sadd db.SetAdd(setKey, "a"); db.SetAdd(setKey, "b"); db.SetAdd(setKey, "c"); //sismember bool isContains = db.SetContains(setKey, "a"); Console.WriteLine("set " + setKey + " contains a is " + isContains );
```

Sorted Set

```
string sortedSetKey = "myZset"; //sadd db.SortedSetAdd(sortedSetKey, "xiaoming", 85); db.SortedSetAdd(sortedSetKey, "xiaohong", 100); db.SortedSetAdd(sortedSetKey, "xiaofei", 62); db.SortedSetAdd(sortedSetKey, "xiaotang", 73); //zrevrangebyscore RedisValue[] names = db.SortedSetRangeByRank(sortedSetKey, 0, 2, Order.Ascending); Console.Write("zrevrangebyscore " + sortedSetKey + " 0 2, result is "); for (int i = 0; i < names.Length; i++) {
  Console.Write(names[i] + " ");
} Console.WriteLine();
```

### 使用redis-cli连接

redis-cli是原生Redis自带的命令行工具，您可以使用redis-cli连接云数据库Redis，并进行数据管理。

**前提条件**

ECS实例与Redis实例同属于经典网络。 已将ECS实例的内网IP地址添加至Redis实例的白名单中。具体操作，请参见设置白名单。 ECS实例的操作系统为Linux，且已安装原生Redis，安装方法，请参见Redis社区版官网。 云数据库 Tair（兼容Redis）用户指

**操作步骤**

1. 登录ECS设备的命令行，然后执行如下格式的命令连接至Redis实例：

```
src/redis-cli -h <hostname> -p <port>
```

表 1. 参数说明

| 参数 | 获取方式 |
|---|---|
| <hostname> | Redis实例的内网连接地址，可在实例信息页面中的连接信息区域框中获取。 |
| <port> | Redis实例的端口号，默认为6379。 |

命令示例

```
src/redis-cli -h r-bp1zxszhcgatnx****.redis.rds.aliyuncs.com -p 6379
```

2. 执行下述格式的命令完成密码验证：

```
AUTH <password>
```

<password>：账号的密码，在创建实例时已设置，如果忘记密码，可重置密码，具体操作，请参见修改密码。 命令示例：

```
AUTH testaccount:Rp829dlwa
```

验证成功后，返回如下结果： `OK` 云数据库 Tair（兼容Redis）用户指

## 性能监控

### 查看监控数据

您可以查询过去一个月内指定时间段的Redis监控数据。

**操作步骤**

1. 登录云数据库Tair（兼容Redis）控制台。
2. 在**实例列表**页，单击目标实例ID。
3. 在左侧导航栏，单击**性能监控**。
4. 根据实例的架构类型，选择执行下述步骤：
若实例为主备架构：您仅需关注主节点的监控指标即可。 若实例为集群、读写分离架构： 您可以在**实例全局**中查询集群、读写分离架构实例的整体性能。实例全局的监控指标为各子节点的聚合数据，不同监控指标的聚合方式不同（求平均值、求和等），例如实例全局的CPU使用率为所有子节点CPU使用率的平均值。 您可以在**数据节点**中查询到各个数据节点的监控指标。 同时，若实例带有Proxy节点，您也可以在**实例全局**或**代理节点**中查询Proxy的整体性能或各个Proxy 节点的监控指标。

**说明**

支持查询最近1个月的监控数据，查询时间跨度不允许超过7天。 为避免对实例的运行产生影响，同时保障性能监控页面中趋势图的展示效果，在选择不同时间范围时，趋势图的数据展示粒度有所不同。 对于读写分离架构实例，聚合监控指标暂不包含只读节点的监控指标。 云数据库 Tair（兼容Redis）用户指

## 云监控

### 查看监控大盘指标

云监控（CloudMonitor，CMS）页面提供了丰富的性能监控项和秒级监控频率，方便您掌握集群或实例的运行状态并通过细粒度的监控数据快速定位运维问题。

**监控大盘**

1. 登录Apsara Uni-manager运营控制台。
2. 在顶部菜单栏，单击**产品** > **数据库**，选择目标数据库产品。
3. 您可以通过如下两种方式查看云监控信息。
i. 方式一 a. 在目标列表页面，单击目标实例或集群ID。 b. 在左侧导航栏中，选择**云监控**。 ii. 方式二 a. 在目标列表页面，单击目标实例监控列下的图标。 b. 查看相关监控数据。
4. 您可以根据业务需求选择查看所需的监控信息，相关监控指标请参见**《云监控****CMS****用户指南》**中**云监控**
**指标说明**-**数据库**章节。

**说明**

在**时间粒度**下拉框，您可以根据业务需求选择查看监控信息的时间段，支持查看**最近**1**分钟**到**最近****30** 天的数据。

### 报警历史

当报警发生后，可以查看报警历史信息。支持导出并下载报警历史信息，便于在本地进行数据分析。

**操作步骤**

1. 登录Apsara Uni-manager运营控制台。
2. 在顶部菜单栏，单击**产品** > **数据库**，选择目标数据库产品。
3. 在目标列表页面，单击目标实例或集群ID。
4. 在左侧导航栏，单击**云监控**，选择**报警服务** > **报警历史**。
5. （可选）在**报警历史**页面，可通过**规则****ID**、**规则名称**、**报警级别**和时间来筛选报警历史记录。
6. 在报警历史页面，执行以下操作。

| 操作任务 | 操作步骤 |
|---|---|

云数据库 Tair（兼容Redis）用户指

| 查看报警历史 | 在报警历史列表中，可以直接查看目标报警历史的产品名称、故障实例、发生时间、规则名称、状态、等级和通知对象。单击目标报警历史对应规格名称，可以查看报警规则详情。 说明报警历史默认支持查询最近2天的数据。 |
|---|---|
| 导出报警历史 | i. 在报警历史页面，单击页面右上方的 。 ii. 在导出任务对话框中，设置时间选择和任务名称后，单击确定。 |

### 报警规则

#### 创建报警规则

**背景信息**

报警规则在生效时间内，根据默认的探测频率检测报警指标是否超出所设定的阈值，一旦检测到云产品监控指标超出阈值（出现异常），按照设定的报警联系人或其他报警信息处理平台进行告警。

**说明**

最小报警探测频率为每分钟一次。

**操作步骤**

1. 登录Apsara Uni-manager运营控制台。
2. 在顶部菜单栏，单击**产品** > **数据库**，选择目标数据库产品。
3. 在目标列表页面，单击目标实例或集群ID。
4. 在左侧导航栏，单击**云监控**，选择**报警服务** > **报警规则**。
5. 单击列表上方的**创建报警规则**。
6. 在**创建报警规则**面板中，根据实际需要设置相应配置项。

| 配置项 | 说明 |
|---|---|
| 云产品选择 | 默认，无需选择。 |
| 资源范围 | 报警规则关联资源的范围，支持以下几类。不同云产品可选择的范围类型存在一定差异。 实例维度：选择当前组织资源集下的一个或多个目标实例。 资源集维度：选择当前组织和地域下的目标资源集。 应用分组维度：选择当前组织和地域下的应用分组。 全部资源：默认不支持选择。 |

云数据库 Tair（兼容Redis）用户指

| 资源选择 | 根据资源范围的选择，选择具体的资源实例、资源集或应用分组。 |
|---|---|
| 报警规则描述 | 报警规则的主体。当监控数据满足报警条件时，触发报警规则。 规则描述设置方法： i. 单击创建报警规则。 ii. 在创建报警规则面板，设置规则名称、指标维度、监控指标、阈值及报警级别等。 说明指标维度仅在资源范围选择实例维度时才会显示。 iii. 单击确认。 |
| 通道沉默周期 | 报警发生后未恢复正常，间隔多久重复发送一次报警通知。取值：5分钟、15分钟、30分钟、1小时、3小时、6小时、12小时和24小时。 当某监控指标超出报警阈值时触发报警，如果监控指标在通道沉默周期内持续超过报警阈值，在通道沉默周期内不会重复发送报警通知；如果监控指标在通道沉默周期后仍未恢复正常，则云监控将再次发送报警通知。 例如，当通道沉默周期设置为12小时时，如果超出报警阈值的监控指标在首次触发报警后12 小时仍未恢复正常，云监控将再次发送报警通知。 |
| 生效时间 | 报警规则的生效时间。报警规则只在生效时间内检查监控数据是否超出报警阈值。 |
| 报警回调 | 用于接收云监控通过POST请求推送报警消息的回调地址。 说明报警回调地址必须是云监控可访问的域名地址，仅支持HTTP协议，不支持填写IP。 |
| 无数据处理方法 | 无监控数据时报警的处理方式。 不做任何处理发送无数据报警 |
| 报警联系人 | 选择报警信息发送的用户组或用户。 默认的云账号报警联系人组是一个空账号，可用于测试报警规则的有效性。 |

7. 单击**确定**。

**规则描述配置项说明**

| 配置项 | 说明 |
|---|---|
| 规则名称 | 填写报警规则名称。 |

云数据库 Tair（兼容Redis）用户指

| 监控指标 | 从当前报警规则所选择的云产品的所有监控指标中，选择目标指标项。各云产品的监控指标详情可参见云产品监控指标说明。 |
|---|---|
| 指标维度 | 指除实例ID之外的其他维度。仅在资源范围选择实例维度时才会显示。 |
| 阈值及报警级别（单位：%） | 报警级别分为紧急、警告和普通。 监控数据的聚合值类型可以选择平均值、最小值和最大值。 监控数据的周期可以选择连续、连续5个周期、连续10个周期、连续15个周期、连续30个周期、连续60个周期。 实际监控数据与报警阈值之间的比较关系，支持 “>”、“ >=”、“<”、“<= ”、“=”、 “!=”、“同比昨天同时间上涨”、“同比昨天同时间下降”、“环比上周期上涨”、“环比上周期下降”、“比上周期增量”、“比上周期降量”的选择。还支持设置阈值和触发次数，当监控数据达到设置的阈值的触发次数时，产生报警。 |

**规则配置示例**

为数据库实例创建一个名为example的报警规则，用于监控目标数据库实例的CPU使用率，当CPU使用率峰值（最大值）在五个探测周期内有三次大于等于70%的情况时触发报警，且报警级别为紧急。 适用于此场景的规则描述配置如下图所示。 云数据库 Tair（兼容Redis）用户指

#### 管理报警规则

在报警规则列表中，可以对报警规则进行修改、禁用、启用、删除等操作。

**操作步骤**

1. 登录Apsara Uni-manager运营控制台。
2. 在顶部菜单栏，单击**产品** > **数据库**，选择目标数据库产品。
3. 在目标列表页面，单击目标实例或集群ID。
4. 在左侧导航栏，单击**云监控**，选择**报警服务** > **报警规则**。
5. 选择目标报警规则，执行相关操作。

| 操作任务 | 操作步骤 |
|---|---|
| 查看报警规则详情 | 单击目标报警规则操作列的详情，在报警规则/报警历史/故障资源面板中可查看报警规则的详细信息。 |
| 判断规则有效性 | 单击目标报警规则有效性列的点击巡检，在有效性列可查看巡检结果。 说明若巡检结果异常，可单击检测结果，在弹出的面板中查看告警规则执行异常检测、告警规则加载检测、无效报警规则检测和告警规则回调检测结果。 单击重新检测，可重新检测规则有效性。 |
| 查看规则执行记录 | 单击目标报警规则规则执行记录列的查看规则执行记录，在报警规则执行记录面板中，可通过时间范围筛选执行记录。 |
| 修改报警规则 | i. 单击目标报警规则操作列的编辑。 ii. 在修改报警规则面板中，修改报警规则。相关配置参数说明请参见《创建报警规则》。 iii. 修改完成后，单击确定。 |
| 禁用报警规则 | 当需要手动停止云产品的服务，进行维护或升级时，可以禁用报警规则，避免因人为变更而收到大量且无用的报警通知。 说明请先确认报警规则的状态为正常后，再进行禁用。 单个禁用 a. 单击目标报警规则操作列的图标，单击禁用。 b. 在禁用报警规则对话框中，单击确定。 批量禁用 a. 选中目标报警规则前的复选框，然后单击列表左下角的禁用。 b. 在禁用报警规则对话框，单击确定。 |

云数据库 Tair（兼容Redis）用户指

| 启用报警规则 | 完成云产品的维护或升级后，可以重新启用已被禁用的报警规则。 说明请先确认报警规则的状态为已禁用后，再进行禁用。 单个启用 a. 单击目标报警规则操作列的启用。 b. 在启用报警规则对话框中，单击确定。 批量启用 a. 选中目标报警规则前的复选框，然后单击列表左下角的启用。 b. 在启用报警规则对话框，单击确定。 |
|---|---|
| 删除报警规则 | 单个删除 a. 单击目标报警规则操作列的图标，单击删除。 b. 在删除报警规则对话框中，单击确定。 批量删除 a. 选中目标报警规则前的复选框，然后单击列表左下角的删除。 b. 在删除报警规则对话框中，单击确定。 |

云数据库 Tair（兼容Redis）用户指

## 参数管理

### 设置参数

云数据库 Tair（兼容 Redis）允许用户自定义部分实例参数。通过本文，您可以了解相关参数的说明以及在控制台修改各参数值的通用方法。

**注意事项**

为最大程度保障Redis实例的稳定运行，目前仅开放部分参数，如果某个参数未在本文中列出，即不支持设置该参数。 部分参数在提交修改后会自动重启实例（重启过程中实例会发生秒级闪断）。在控制台设置参数时，您需要关注目标参数的**重启生效**列。

**操作步骤**

1. 登录云数据库Tair（兼容Redis）控制台。
2. 在**实例列表**页，单击目标实例ID。
3. 在左侧导航栏，单击**参数设置**。
4. 修改参数。
当前支持如下3种方式修改参数，关于参数和参数值的说明，请参见附录：参数说明。

**警告**

部分参数在提交修改后会自动重启实例（重启过程中实例会发生秒级闪断，请谨慎操作），详情请参见目标参数的**重启生效**列。 修改单个参数： a. 找到目标参数，单击其**操作**列的**修改**。 b. 单击**确定**。 批量修改： a. 单击**批量修改**。 b. 在目标参数的**参数运行值**列，修改参数。 c. 完成修改后，单击页面下方的**确认修改**。 从文件导入： 若您希望将其他实例的参数配置应用至当前实例，您可以选择此方式。使用该功能前，您需要提前访问源实例的**参数设置**页面，单击页面右上方图标，下载源实例的参数配置文件。

**说明**

请将参数配置文件导入至同版本、同架构的实例中，否则部分参数将无法生效。 a. 单击**从文件导入**。 b. 在**批量导入**面板，单击图标，上传目标文件。 云数据库 Tair（兼容Redis）用户指 c. 在**参数详情**区域，确认并勾选待修改的参数。

**说明**

您可以开启**只展示有变化参数**开关，快速过滤与当前**参数运行值**不同的参数。 d. 单击**确认修改**。

**附录：参数说明**

表 1. 参数说明

| 参数 | 说明 |
|---|---|
| #no loose check-whitelist- _ _ always | 开启VPC免密访问后默认不检查客户端IP是否在Redis白名单中，此时如果将该参数的值设置为yes，则白名单在VPC免密模式下依然生效。可选值： yes，表示开启。 no，默认值，表示关闭。 |
| #no loose disabled-commands _ _ | 设置禁用命令，多个命令通过英文逗号（,）隔开，目前可禁用的命令有：FLUSHALL、FLUSHDB、KEYS、HGETALL、EVAL、EVALSHA 、SCRIPT。 |
| #no loose sentinel-enabled _ _ | 开启或关闭哨兵（Sentinel）兼容模式，可选值： yes，表示开启。 no，默认值，表示关闭。 |
| client-output-buffer-limit pubsub | 限制对发布订阅客户端的输出缓冲，参数值格式为 <hard limit> <soft limit> <soft seconds> 。 hard limit：当某客户端的输出缓冲区占用内存达到或超过hard limit的限制时，断开该客户端的连接。hard limit值的单位为Byte。 soft limit和soft seconds：当某客户端的输出缓冲区占用内存达到或超过 soft limit的限制，且该状态持续时间大于等于soft seconds限定的秒数， 断开该客户端的连接。soft limit值的单位为Byte，soft seconds值的单位为s。 |
| dynamic-hz | 开启或关闭动态hz，可选值： yes，默认值，表示开启。 no，表示关闭。 |
| hash-max-ziplist-entries | 哈希对象同时满足以下两个条件时， 使用ziplist编码。 1. 哈希对象保存的所有键值对的键和值的字符串长度的字节数都小于hash- max-ziplist-value的值。 2. 哈希对象保存的键值对数量小于hash-max-ziplist-entries的值。 |

|  | limit> <soft seconds> |
|---|---|

云数据库 Tair（兼容Redis）用户指

| hash-max-ziplist-value | 哈希对象同时满足以下两个条件时， 使用ziplist编码。 1. 哈希对象保存的所有键值对的键和值的字符串长度的字节数都小于hash- max-ziplist-value的值。 2. 哈希对象保存的键值对数量小于hash-max-ziplist-entries的值。 |
|---|---|
| hotkey-threshold | TopKey统计功能中热Key的QPS阈值，默认为5000，取值范围为[100- 65535]。 |
| hz | 设置Redis后台任务执行频率，例如清除过期键任务。取值范围为1~500，默认值为10，即每秒执行10次。该值越大，CPU资源消耗越多，但在过期键较多的情况下清理频率也更高，同时Redis能够更精确地处理超时。建议取值不要超过100。 |
| lazyfree-lazy-eviction | 是否开启基于lazyfree的驱逐功能，可选值： yes，表示开启。 no，默认值，表示不开启。 |
| lazyfree-lazy-expire | 是否开启基于lazyfree的过期key删除功能，可选值： yes，默认值，表示开启。 no，表示不开启。 |
| lazyfree-lazy-server-del | DEL命令是否基于lazyfree异步删除数据，可选值： yes，默认值，表示开启。 no，表示不开启。 |
| list-compress-depth | 列表中两端不被压缩的节点个数，取值范围0~65535。 0：默认值，表示都不压缩。 1：表示list两端各有1个节点不压缩，中间的节点压缩。 2：表示list两端各有2个节点不压缩，中间的节点压缩。 3：表示list两端各有3个节点不压缩，中间的节点压缩。 其后依此类推。 |

云数据库 Tair（兼容Redis）用户指

| list-max-ziplist-size | 取正值表示按照数据项个数来限定每个quicklist节点上的ziplist长度。例如，当该参数配置为5时，每个quicklist节点的ziplist最多包含5个数据项。 取负值表示按照占用字节数来限定每个quicklist节点上的ziplist长度。此时，该值只能取-1到-5这五个值，每个值含义如下。 -5：每个quicklist节点上的ziplist大小不能超过64Kb（注：1kb = 1024 bytes）。 -4：每个quicklist节点上的ziplist大小不能超过32Kb。 -3：每个quicklist节点上的ziplist大小不能超过16Kb。 -2：每个quicklist节点上的ziplist大小不能超过8Kb（Redis默认值）。 -1：每个quicklist节点上的ziplist大小不能超过4 Kb。 |
|---|---|
| maxmemory-policy | 设置缓存满后Redis删除内容的策略，您可以在如下八种策略中进行选择。 LRU表示最近最少使用的。LFU表示最不常用的。LRU，LFU和volatile-ttl都是使用近似随机算法实现的。 volatile-lru：只从设置失效（expire set）的key中选择最近最少使用的 key进行删除。 allkeys-lru：优先删除掉最近最少使用的key。 volatile-lfu：只从设置失效（expire set）的key中选择最不常用的key进行删除。 allkeys-lfu：优先删除掉最不常用的key。 volatile-random：只从设置失效（expire set）的key中，随机选择一些 key进行删除。 allkeys-random：随机选择一些key进行删除。 volatile-ttl：只从设置失效（expire set）的key中，选出存活时间 （TTL）最短的key进行删除。 noeviction：不删除任何key，只是在写操作时返回错误。 |
| notify-keyspace-events | notify-keyspace-events的参数可以是以下字符的任意组合，它指定了服务器该发送哪些类型的通知。 字符：发送的通知。 K：键空间通知，所有通知以 keyspace@<db> 为前缀。 __ __ E：键事件通知，所有通知以 keyevent@<db> 为前缀。 __ __ g：DEL、EXPIRE、RENAME等类型无关的通用命令的通知。 l：列表命令的通知。 s：集合命令的通知。 h：哈希命令的通知。 z：有序集合命令的通知。 x：过期事件。每当有过期键被删除时发送。 e：驱逐（evict）事件。每当有键因为maxmemory政策而被删除时发送。 A：参数g$lshzxe的别名。 |

云数据库 Tair（兼容Redis）用户指

| set-max-intset-entries | 当Set集合内的数据符合以下条件时，会使用intset编码。 1. 当集合内所有数据都是整数对象。 2. 都是基数为10的整数，范围为64位有符号整数。 |
|---|---|
| slowlog-log-slower-than | 设置是否记录慢查询日志： 当取值为负时，不记录任何操作。 当取值为0时，记录所有操作。 当取值为正时，只有当操作执行时间大于设置值，操作才被记录。 单位为微秒（μs），取值范围0~10000000，默认值10000。 |
| slowlog-max-len | 慢日志最多保存记录条数，取值范围100~10000，默认值1024。 |
| stream-node-max-bytes | Stream中每个宏节点（Macro Node）能够占用的最大内存，取值范围： 0~999,999,999,999,999。0表示无限制。 |
| stream-node-max-entries | Stream中每个宏节点中可存储条目的最大数量，取值范围： 0~999,999,999,999,999。0表示无限制。 |
| timeout | 在客户端连接空闲时长达到指定值时关闭连接。单位为秒（s），取值范围： 0~100000。0表示不开启。 |
| zset-max-ziplist-entries | 排序集合对象同时满足以下两个条件时， 使用ziplist编码。 1. 排序集合对象保存的所有键值对的键和值的字符串长度的字节数都小于 zset-max-ziplist-value的值。 2. 排序集合对象保存的键值对数量小于zset-max-ziplist-entries的值。 |
| zset-max-ziplist-value | 排序集合对象同时满足以下两个条件时， 使用ziplist编码。 1. 排序集合对象保存的所有键值对的键和值的字符串长度的字节数都小于 zset-max-ziplist-value的值。 2. 排序集合对象保存的键值对数量小于zset-max-ziplist-entries的值。 |
| list-max-ziplist-entries | 链表对象同时满足以下两个条件时， 使用ziplist编码。 1. 链表对象保存的所有元素的字符串长度的字节数都小于list-max-ziplist- value的值。 2. 链表集合对象保存的元素数量小于list-max-ziplist-entries的值。 |
| list-max-ziplist-value | 链表对象同时满足以下两个条件时， 使用ziplist编码。 1. 链表对象保存的所有元素的字符串长度的字节数都小于list-max-ziplist- value的值。 2. 链表集合对象保存的元素数量小于list-max-ziplist-entries的值。 |

云数据库 Tair（兼容Redis）用户指

| cluster compat enable _ _ | 开启或关闭原生Redis cluster语法兼容，可选值： 0，表示关闭。 1，默认值，表示开启。 |
|---|---|
| script check enable _ _ | 检查Lua脚本涉及的key是否在相同slot，可选值： 0，表示不检查。 1，默认值，表示检查。 |
| ptod enabled _ | 控制是否将客户端的真实IP地址通过代理层（Proxy）透传到底层的数据库 （DB）。 0，表示不透传。 1，默认值，表示透传。 |

**说明**

用于调整Redis数据节点最大连接数的maxclients参数不支持自定义，默认值为10000。

### 使用参数模板

**新建自定义参数模板**

1. 登录云数据库Tair（兼容Redis）控制台。
2. 在左侧导航栏选择**参数模板**。
3. 单击左上角**创建参数模板**。
4. 设置如下参数。

| 参数 | 说明 |
|---|---|
| 模板名称 | 模板的名称。由英文字母、数字、小数点（.）或下划线（ ）组成，以字母开头，不 _ 能包含中文，长度为8~64个字符。 |
| 组织 | 选择该参数模板归属的组织，用于权限隔离和管理。 |
| 资源集 | 选择该参数模板归属的资源集，用于资源的分组管理。 |
| 实例架构类型 | 支持标准版和集群版/读写分离。 |
| 数据库引擎 | 选择Redis。 |
| 数据库版本 | 支持4.0、5.0、6.0和7.0。 |

云数据库 Tair（兼容Redis）用户指

| 描述 | 备注该模板的相关信息，便于后续管理。长度为0~200个字符。 |
|---|---|
| 添加配置 | 配置参数名和参数值等信息。 |

5. 单击**确定**。

**应用参数模板**

1. 登录云数据库Tair（兼容Redis）控制台。
2. 在左侧导航栏选择**参数模板**。
3. 找到要应用的模板，单击其右侧**操作**列的**应用到实例**。
4. 在左侧实例列表中选择需要应用参数模板的实例，单击
移动到右侧，并检查参数修改情况。

**重要**

将参数模板应用到多个实例时，需确认参数适用于目标实例，请谨慎操作。
5. 单击**确定**。

**复制参数模板**

1. 登录云数据库Tair（兼容Redis）控制台。
2. 在左侧导航栏选择**参数模板**。
3. 单击参数模板右侧**操作**列下的**克隆**，并设置以下参数。

| 参数 | 说明 |
|---|---|
| 模板名称 | 模板的名称。由英文、数字、小数点（.）或下划线（ ）组成，以字母开头，不能包 _ 含中文，长度为8~64个字符。 |
| 描述 | 备注该模板的相关信息，便于后续管理。长度为0~200个字符。 |
| 添加配置 | 默认为原参数模板中的参数配置项，您也可以根据需要重新进行配置。 说明如果您需要添加某个参数，请单击添加配置。 如果您需要修改某个参数的配置值，请在该参数右侧的配置值输入框中重新输入。 如果您需要删除某个参数，请单击该参数右侧的删除。 |

4. 单击**确定**。
云数据库 Tair（兼容Redis）用户指

**更多操作**

除上述操作外，还支持如下功能：
1. 登录云数据库Tair（兼容Redis）控制台。
2. 在左侧导航栏选择**参数模板**。
3. 您可以对参数模板进行如下操作：
查看参数模板。 单击参数模板右侧**操作**列下的**查看**，查看该参数模板的基本信息和参数信息。 删除参数模板。

**说明**

删除参数模板不会影响已经应用该模板的实例。 单击参数模板右侧**操作**列下的**删除**，在弹出的对话框中单击**确定**。 云数据库 Tair（兼容Redis）用户指

## 备份与恢复

### 自动备份

由于越来越多的应用将Redis作为持久化存储，所以需要常规的备份机制保证数据误操作之后，具备数据快速恢复的能力。阿里云采用在备节点上执行RDB快照备份，备份期间对您的实例访问不会产生性能影响，并且提供了控制台的快捷操作可以让您进行个性化的备份设置。

**操作步骤**

1. 登录云数据库Tair（兼容Redis）控制台。
2. 在**实例列表**页，单击目标实例ID。
3. 在左侧导航栏，单击**备份与恢复**。
4. 单击右上角**备份设置**。
5. 设置备份周期和备份时间段。
**保留天数**：备份文件的保留天数支持7-730天之间，请合理设置保留天数，设置过大的存储时长会占用
更多的备份存储容量。
**备份周期**：可以设置为一星期中的某一天或者某几天，默认为每天备份一次。
**备份时间**：可以设置为任意时段，以小时为单位，建议设置为业务的低峰期。
6. 单击**确定**。

### 手动备份

您可以在控制台上随时发起手动备份。

**操作步骤**

1. 登录云数据库Tair（兼容Redis）控制台。
2. 在**实例列表**页，单击目标实例ID。
3. 在左侧导航栏，单击**备份与恢复**。
4. 单击页面右上角的**手动创建备份**。
5. 单击**确定**。

**说明**

您可以在**备份设置**页面中，查看到已完成的备份数据（备份数据的保留时间支持7-730天之间，请合理设置保留天数）。

### 下载备份

如果您需要更长时间的数据存档，可以直接在控制台上复制链接将数据库备份文件自行下载到本地进行长时间存储。

**操作步骤**

1. 登录云数据库Tair（兼容Redis）控制台。
2. 在**实例列表**页，单击目标实例ID。
3. 在左侧导航栏，单击**备份与恢复**。
云数据库 Tair（兼容Redis）用户指
4. 找到目标备份文件，单击其**操作**列的**备份下载**。

**说明**

当实例为集群架构时，为保障数据一致性，您需要下载同一时间点中该实例每个数据分片的备份文件。

### 数据恢复

云数据库 Tair（兼容 Redis）支持将指定备份集的数据恢复至当前实例。

**前提条件**

实例为主从或集群架构。

**操作步骤**

1. 登录云数据库Tair（兼容Redis）控制台。
2. 在**实例列表**页，单击目标实例ID。
3. 在左侧导航栏，单击**备份与恢复**。
4. 根据实例的架构，选择下述操作步骤：
主从架构：找到目标备份集，单击其**操作**列的**数据恢复**。 集群架构：选择同一时间点中，所有数据分片对应的备份集，然后单击右上角的**数据恢复**。

**警告**

由于数据恢复操作有较高的风险，请充分验证数据正确性之后，再进行数据恢复操作。
5. 在弹出的对话框中，阅读提示并单击**继续执行恢复操作**。
您也可以执行克隆实例操作，将备份数据恢复到新创建的实例上，具体操作，请参见克隆实例。

### 克隆实例

云数据库 Tair（兼容 Redis）支持从指定的备份集创建新实例，新实例中的数据将和该备份集中的数据一致，可用于数据恢复、快速部署业务或数据验证等场景。

**前提条件**

实例为主从或集群架构。

**操作步骤**

1. 登录云数据库Tair（兼容Redis）控制台。
2. 在**实例列表**页，单击目标实例ID。
3. 在左侧导航栏，单击**备份与恢复**。
4. 找到目标备份集，单击其**操作**列的**克隆实例**。

**说明**

实例为集群架构时，您需要选择同一时间点中，所有数据分片对应的备份集。
5. 在弹出的对话框中，单击**确定**。
云数据库 Tair（兼容Redis）用户指
6. 在跳转到的页面中，设置新实例的相关配置并单击**提交**。

**说明**

新实例的相关配置说明，请参见创建实例。 云数据库 Tair（兼容Redis）用户指

## CloudDBA

### 性能趋势

CloudDBA的性能趋势功能可以监控Redis实例在某个时间段的基础性能及其运行趋势，包括CPU使用率、 使用内存量、QPS（每秒访问次数）、总连接数、响应时间、网络流量、Key命中信息等。

**操作步骤**

1. 登录云数据库Tair（兼容Redis）控制台。
2. 在**实例列表**页，单击目标实例ID。
3. 在左侧导航栏，单击**CloudDBA >** **性能趋势**。
4. 性能趋势目前支持如下查看方式，您可以根据需求选择：

**说明**

如果实例为集群版，本页面还会展示节点列表信息（展示近1小时性能数据），单击节点ID可展示指定节点的详细数据。

### 性能趋势

单击**性能趋势**页签，设置时间段和更多指标，然后单击**查看**。

**说明**

**联动图表**默认开启，如果您将光标悬置于CPU图表上来查看Redis实例9点时的CPU性能指
标，其他多个图表也会显示该实例在9点时的性能指标数据。 单击图表右上方的**含义？**和**详情**，查看性能指标含义和性能趋势大图。

**性能趋势对比查看**

单击**性能趋势对比查看**页签，设置任意两个时间段，配置更多指标，然后单击**查看**，对比两个时间段的性能趋势。

**自定义图表**

以上两种查看方式显示了Redis实例的基础性能指标，如仅需展现其中部分基础指标，您可以自定义性

### Top Key统计

云数据库 Tair（兼容Redis）用户指当Tair和Redis内存使用率升高或CPU使用率升高时，您可以使用**Top Key****统计**功能快速找到大Key和热 Key。本功能支持展示实例中实时和历史的大Key、热Key信息，包括元素数量多的Key、访问频次高的热 Key，帮助您有效解决实例性能问题。

**大Key和热Key的统计排名机制**

为避免对数据库造成额外的资源占用，本功能仅会统计客户端操作（读、写）过的Key，并仅保留和展示每种Key类型的Top数量，而不会实时扫描数据库中的所有Key。同时，在实例重启后或HA切换后，原先统计的TopKey信息将被清空，统计将重新开始，因此**长时间未操作过的****Key****可能不会被纳入统计**。如需了解数

| Key类型 | 统计机制 | 展示说明 |
|---|---|---|
| 热Key | Key的QPS超过5000时，被记录为热Key。 可通过设置参数 hotkey-threshold 自定义 QPS阈值。 | 在同一时间内，系统最多展示前50个热Key，支持实时展示其精确QPS。 |
| 大 Key（元素数量多的Key） | Key的字符串长度（仅限String类型）或元素数量 （如Hash中的field数、Set中的member数等） 达到阈值（默认2000）及以上时，被统计为大 Key。 说明仅支持兼容Redis 5.0及以上版本的实例。 | 最多展示每个数据类型排名前3的大Key，当Key 的元素数量相同时优先展示先写入的Key。 |

本功能支持统计的数据结构如下： Redis原生数据结构：String、List、Hash、Set、Zset、Stream Tair自研数据结构：TairString、TairHash、TairGIS、TairBloom、TairDoc、TairCpc、TairZset、 TairRoaring、TairTS、TairSearch

**操作步骤**

1. 登录云数据库Tair（兼容Redis）控制台。
2. 在**实例列表**页，单击目标实例ID。
3. 在左侧导航栏，单击**CloudDBA > Top Key****统计**。
4. 根据业务需求，选择查询实时数据或历史数据。
如果实例为集群架构或读写分离架构，您还可以在**当前节点**下拉框中选择要展示数据的节点。 查询历史数据时，支持查询最近4天的大Key和热Key信息，且最大查询时间范围不能超过3小时。 可通过设置参数 `hotkey-threshold` 自定义QPS阈值。

### 自定义性能趋势图表

默认性能趋势显示了Redis实例的基础性能指标，您也可以在自定义性能趋势图表中，选择仅展示部分基础性能指标，以便有针对性地监控和分析实例的性能及运行趋势。本文档介绍了如何在监控大盘中自定义创建 Redis实例的性能趋势图表。

**操作步骤**

1. 登录云数据库Tair（兼容Redis）控制台。
2. 在**实例列表**页，单击目标实例ID。
云数据库 Tair（兼容Redis）用户指
3. 在左侧导航栏，单击**CloudDBA >** **性能趋势**。
4. 单击**自定义图表**页签。
5. 单击**新增监控大盘**，填写大盘名称并单击**确认**。
6. 单击+**添加图表**或**新增监控图表**。如下图所示，选中需要查看的指标，单击**确定**。
7. **可选：**通过查看、修改和删除操作，管理监控大盘。
选择目标监控大盘并设置时间段，然后单击**查看**。 修改监控大盘单击如下所示图标，根据需求进行修改或删除图表。 删除监控大盘单击**操作大盘** > **删除监控大盘**。

### 实时性能

在CloudDBA中可以实时查看Redis实例的性能，包括CPU使用率、内存使用信息、QPS（每秒访问次数）、网络流量、Server信息、Key信息、Client信息、连接信息等。

**操作步骤**

云数据库 Tair（兼容Redis）用户指
1. 登录云数据库Tair（兼容Redis）控制台。
2. 在**实例列表**页，单击目标实例ID。
3. 在左侧导航栏，单击**CloudDBA >** **实时性能**。
4. 根据业务需求，选择实时性能的展示方式：
页面上方实时显示实例性能指标，包括Server信息、Key信息、内存信息、Client信息、连接信息；页面下方以**实时图表**和**实时表格**的形式显示详细的性能指标。

**说明**

为方便您实时查看性能的变化，性能指标的值每5秒自动刷新一次，剩余刷新次数可在右上角显示。 您也可以单击**暂停**停止刷新。

| 展示方式 | 介绍 |
|---|---|
| 实时图表 | 以曲线图的形式显示实例的实时性能指标，如Key信息、Key命中信息、Key命中率、CPU 使用率、内存信息、QPS、网络流量。 |
| 实时表格 | 以表格的形式显示实例的Key命中信息、Key命中率、QPS、Memory（内存信息）、CPU 使用率、Network（网络流量）、Client信息、连接信息等性能。实时的性能值每5秒新增一行，最多显示999行。 |

云数据库 Tair（兼容Redis）用户指

### 实例会话

通过实例会话，您可以实时查看Redis实例与客户端间的会话信息，包括客户端信息，所执行的命令和已连接的时长等，还可以根据业务需求终止异常会话。

**操作步骤**

1. 登录云数据库Tair（兼容Redis）控制台。
2. 在**实例列表**页，单击目标实例ID。
3. 在左侧导航栏，单击**CloudDBA >** **实例会话**。
4. 根据业务需求，选择下述步骤对实例会话进行管理：
查看会话：页面默认展示了所有会话的详细信息，您可以将鼠标放置在对应的参数名称上查看其含义。

**说明**

您可以在**搜索会话**文本框中输入关键字来过滤会话信息。 如需刷新实例会话信息，可以单击左上角的**刷新**或者开启**自动刷新**（每30秒自动刷新一次）。 终止会话：选择目标会话或按shif键可以选择多个目标会话，单击右上角的**kill****选中会话**或者直接点击**kill****全部会话**，可以终止选中或全部会话。

**警告**

请勿终止系统级的会话，否则可能引发一些不可预料的结果。 查看会话统计：会话统计记录了实例会话的总客户端数，活跃客户端数，来源（客户端的地址）数量。

**说明**

在**按照来源统计**区域框的表格中，单击客户端地址右侧的编辑图标即可修改来源的别名。在总数栏中单击数值，可查看访问来源地址的详细信息。

### 慢请求

慢请求问题会极大地影响Redis服务的稳定性。您可在CloudDBA中查看慢日志详细信息，来监控和分析慢请求问题。

**操作步骤**

1. 登录云数据库Tair（兼容Redis）控制台。
2. 在**实例列表**页，单击目标实例ID。
3. 在左侧导航栏，单击**CloudDBA >** **慢请求**。
4. 查看实例的慢请求日志信息。
云数据库 Tair（兼容Redis）用户指

**说明**

您可以选择要展示的日志条数或在搜索文本框中输入关键字进行过滤。

### 离线全量Key分析

通过离线全量Key分析功能来分析Redis的备份文件，可以快速发现实例中的BigKey（大Key），帮助您掌握Key在内存中的占用和分布、Key过期时间等信息，为您的优化操作提供数据支持，帮助您避免因Key倾斜引发的内存不足、性能下降等问题。

**操作步骤**

1. 登录云数据库Tair（兼容Redis）控制台。
2. 在**实例列表**页，单击目标实例ID。
3. 在左侧导航栏，单击**CloudDBA >** **离线全量****Key****分析**。
页面默认展示最近一天缓存分析结果列表，您可以根据需求选择其他时间段。
4. 在该页面，单击页面右侧的**立即分析**。
5. 在弹出的对话框中，设置分析的节点和方式。
云数据库 Tair（兼容Redis）用户指

| 参数 | 说明 |
|---|---|
| 选择分析节点 | 选择需要执行缓存分析的节点ID。 说明您可以选择分析整个实例，也可以只选中某个节点进行分析。当选择分析整个实例时，若该实例的节点数超过8个，系统仅对内存使用量前8的节点进行分析。 |
| 分析方式 | 您可以选择分析方式为使用上一个备份文件或新建备份，并使用最新的备份进行分析。 |

6. 单击**确定**。
系统执行分析并展示分析状态，您可以单击**刷新**以更新分析状态。
7. 找到已完成的分析任务，单击其**操作**列的**详情**展示详细的分析结果。
**基本信息**：展示实例基本属性和缓存分析方法等信息。
**相关节点**：展示实例内各节点的内存情况和Key统计信息。

**说明**

当实例为集群，且选择的分析节点为整个实例时，**详情**页才会展示**相关节点**信息并提供节点选择的功能。 云数据库 Tair（兼容Redis）用户指
**详情**：展示实例或节点的Key内存占有情况、Key数量分布情况、Key中元素的内存占用和分布情况、
Key过期时间分布、大Key排名等信息。

### 诊断实例

云数据库 Tair（兼容 Redis）集成了DAS的诊断报告功能，可针对指定时间段的实例运行状况发起诊断， 帮助您从性能水位、访问倾斜情况、慢日志等多方面评估实例的健康状况，快速定位实例的异常情况。

**操作步骤**

1. 登录云数据库Tair（兼容Redis）控制台。
2. 在**实例列表**页，单击目标实例ID。
3. 在左侧导航栏，单击**CloudDBA >** **诊断报告**。
4. 单击**发起诊断**。
5. 在弹出的对话框中，选择诊断的时间范围并单击**确定**。

**说明**

诊断时间的选择范围不能超过一天，选择的时间范围越小，诊断报告中展示的性能指标的粒度更细。
6. 等待诊断分析完成后（可刷新该页面查看分析进度），单击**操作**列的**查看报告**。
诊断报告将展示实例的ID、规格、类型及可用区等基本信息，同时提供实例关键性能指标的统计信息及其状态。此外，报告还将列出发生慢请求次数排名前十的数据节点及其对应的慢请求信息。 云数据库 Tair（兼容Redis）用户指

## 报警设置

**背景信息**

监控报警是通过阿里云监控产品实现的。通过阿里云监控产品，您可以设置监控项，并在触发监控项的报警规则时，通知报警联系组中的所有联系人。您可以维护报警监控项对应的报警联系组，以便发生报警时，能及时通知到相关联系人。

**操作步骤**

1. 登录云数据库Redis控制台。
2. 在**实例列表**页，单击目标实例ID。
3. 在**实例信息**页，单击左侧导航栏中**报警设置**。
4. 在**报警设置**页，单击页面右侧**报警设置**，跳转到**云监控**控制台。
5. 在**云监控**页，您可以**新建报警规则**。
6. 设置完报警规则后，单击**确定**即可。

**说明**

设置完成后，您可以在云监控控制台的**报警规则**页面修改、禁用、删除报警规则，并查看报警历史记录。 云数据库 Tair（兼容Redis）用户指

## 审计日志

您可以通过Tair的SQL审计功能查看SQL明细、定期审计SQL。

**注意事项**

SQL审计的保存时间为30天。 SQL审计导出的文件可以保存2天，超过2天的文件会被系统定时清理。

**说明**

如果不需要使用审计日志时，可单击左上角**关闭审计日志**，读审计与写审计也支持单独开关。

**查看SQL审计信息**

1. 登录云数据库Tair（兼容Redis）控制台。
2. 在**实例列表**页面，单击目标实例ID或者单击实例右侧**操作**列下的**管理**，打开**基本信息**页面。
3. 在左侧菜单栏中，单击**审计日志**。
在审计页面您可以通过时间范围、数据库用户、关键词搜索、客户端IP、执行时长或按Top SQL 耗时排序等条件查询SQL信息。

**导出SQL审计数据**

1. 登录云数据库Tair（兼容Redis）控制台。
2. 在**实例列表**页面，单击目标实例ID或者单击实例右侧**操作**列下的**管理**，打开**基本信息**页面。
3. 在左侧菜单栏中，单击**审计日志**。
4. 单击**更多**，选择**创建导出数据任务**，在弹框中单击**确定**，导出目标时间段的数据。
导出完成后，可以单击**查看导出文件列表**，查看已导出的数据。 云数据库 Tair（兼容Redis）用户指

## 附录

### 租户组织对SLB服务授权操作

本文为您介绍如何完成SLB服务授权操作，帮助您快速解决问题。

**重要**

若您的业务场景需要申请创建并使用IPv6实例，必须确保当前租户组织已显式授予数据库产品访问SLB 服务的权限。若未完成此授权操作，则无法成功创建IPv6实例。

**操作步骤**

1. 登录Apsara Uni-manager运营控制台。
2. 在页面顶部的菜单栏中，单击**配置**。
3. 在左侧导航栏，单击**RAM****服务角色**。
4. 在RAM服务角色页面，单击左上角**创建****RAM****服务角色**。
**服务名称**选择**负载均衡****SLB**，**授权组织名称**选择需要授权的组织即可。
5. 单击**确定**，完成授权。
