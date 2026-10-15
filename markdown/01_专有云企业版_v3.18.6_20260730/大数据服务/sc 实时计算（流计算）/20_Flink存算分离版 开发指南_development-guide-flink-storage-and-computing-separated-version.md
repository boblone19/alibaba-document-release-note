---
title: "实时计算（流计算） Flink存算分离版 开发指南"
product_version: "v3.18.6-SP2607"
doc_version: "20260730"
pdf_pages: 746
source_pdf: "20_Flink存算分离版 开发指南_development-guide-flink-storage-and-computing-separated-version.pdf"
source_url: "https://apsara-doc.oss-cn-hangzhou.aliyuncs.com/apsara-pdf/enterprise/v_3_18_6_20260730/sc/zh/development-guide-flink-storage-and-computing-separated-version.pdf"
converter: line-classifier (PyMuPDF)
---

# 实时计算（流计算） Flink存算分离版 开发指南

实时计算（流计算）

## 连接器

### 支持的连接器

本文为您介绍实时计算Flink版支持的表类型的定义和支持的连接器（包括内置连接器和自定义连接器）。

**表类型定义**

阿里云实时计算Flink版通过Flink SQL定义表对上下游存储进行映射或者使用Datastream API进行连接来实现读写。支持以下几种Flink SQL表类型的定义：

**源表（Source Table）**

Flink作业的数据输入表，是计算的驱动来源。 必须作为驱动表来推进后续计算。产生的记录决定了计算链的触发。 通常是需要进行转换计算的大规模业务数据，量级可以达到千万级甚至亿级别。 以流式数据的形式输入，表示连续不断的新数据，可以来自消息队列、数据库变更日志等。 包含需要Join和关联的关键字段，如用户ID、订单ID等业务主键。

**结果表（Sink Table）**

Flink作业输出的结果数据表。 存储着经过计算转换后的最终结果数据，如聚合结果、过滤后的数据等。 可以输出到数据库、消息队列、文件等外部系统，用于后续的分析。 是整个作业处理链的最终产出和输出，存储了计算的输出。

**内置连接器**

各引擎版本及内置连接器详细说明如下，具体以控制台界面显示为准。

**VVR引擎版本：vvr-11.5.0-flink-1.20**

| 数据源 | 连接器名称 | 支持源表 | 支持结果表 |
|---|---|---|---|
| 云原生数据仓库 AnalyticDB MySQL版 3.0 | adb3.0 | × | √ |
| 云原生数据仓库 AnalyticDB PostgreSQL | adbpg | × | √ |
| Blackhole | blackhole | × | √ |
| ClickHouse | clickhouse | × | √ |
| 云数据库 HBase | cloudhbase | × | √ |

实时计算（流计算）

| Datagen | datagen | √ | × |
|---|---|---|---|
| 数据总线 DataHub | datahub | √ | √ |
| Elasticsearch | elasticsearch | √ | × |
| 模拟数据生成 Faker | faker | √ | × |
| 对象存储 OSS | filesystem | √ | √ |
| 实时数仓 Hologres | hologres | √ | √ |
| Iceberg | iceberg | √ | √ |
| 时序数据库 InfluxDB | influxdb | × | √ |
| JDBC | jdbc | √ | √ |
| 消息队列 Kafka | kafka | √ | √ |
| 云原生多模数据库 Lindorm | lindorm | √ | √ |
| 云数据库 MongoDB 说明支持数据摄入 YAML。 | mongodb | √ | √ |
| 消息队列 RocketMQ | mq | √ | √ |
| MySQL 说明支持数据摄入 YAML。 | mysql | √ | √ |

实时计算（流计算）

| 大数据计算服务 MaxCompute 说明支持数据摄入 YAML。 | odps | √ | √ |
|---|---|---|---|
| 表格存储 OTS | ots | × | √ |
| Apache Paimon | paimon | √ | √ |
| Postgres CDC | postgres-cdc | √ | × |
| Print | print | × | √ |
| 云数据库 RDS MySQL 版 | rds | × | √ |
| 云数据库 Redis | redis | × | √ |
| 日志服务 SLS | sls | √ | √ |
| StarRocks | starrocks | √ | √ |
| 云原生内存数据库 Tair | tair | × | √ |
| Upsert Kafka | upsert-kafka | √ | √ |

**VVR引擎版本：vvr-8.0.7-flink-1.17**

| 数据源 | 连接器名称 | 支持源表 | 支持结果表 |
|---|---|---|---|
| 云原生数据仓库 AnalyticDB MySQL版 3.0 | adb3.0 | × | √ |
| 云原生数据仓库 AnalyticDB PostgreSQL 版（ADB PG） | adbpg | × | √ |
| Blackhole | blackhole | × | √ |

实时计算（流计算）

| ClickHouse | clickhouse | × | √ |
|---|---|---|---|
| 云数据库HBase | cloudhbase | × | √ |
| Datagen | datagen 说明用于调试的连接器， 可以周期性地生成 Datagen源表对应类型的随机数据。 | √ | × |
| 数据总线DataHub | datahub | √ | √ |
| elasticsearch 说明仅6.x & 7.x版本支持。 | elasticsearch | √ | √ |
| 模拟数据生成Faker | faker | √ | × |
| 实时数仓Hologres | hologres | √ | √ |
| Hudi | hudi | √ | √ |
| Iceberg | iceberg | √ | √ |
| 时序数据库InfluxDB 说明仅1.x版本支持。 | influxdb | × | √ |
| JDBC | jdbc | √ | √ |
| 消息队列Kafka 说明仅0.11及以上版本支持。 | kafka | √ | √ |

实时计算（流计算）

| 云原生多模数据库 Lindorm | lindorm | × | √ |
|---|---|---|---|
| 云数据库 MongoDB | mongodb | √ | √ |
| mongodb-cdc 说明仅9.6及以上版本确认。 | mongodb-cdc | √ | × |
| 消息队列 RocketMQ | mq | √ | √ |
| MySQL 说明仅5.6/5.7/8.0版本支持。 | mysql 说明支持连接RDS MySQL版、 PolarDB MySQL版及自建MySQL。 | √ | √ |
| MySQL-CDC 说明仅5.6/5.7/8.0版本支持。 | mysql-cdc | √ | × |
| 大数据计算服务 MaxCompute | odps | √ | √ |
| 表格存储 Tablestore（OTS） | ots | × | √ |
| Apache Paimon 说明仅0.9版本支持。 | paimon | √ | √ |

实时计算（流计算）

| Postgres CDC 说明仅9.6及以上版本支持。 | postgres-cdc | √ | × |
|---|---|---|---|
| Print | print 说明 Print是用于调试的连接器，允许接收并打印一定数量的输入记录。 | × | √ |
| 云数据库 RDS MySQL 版 | rds | × | √ |
| 云数据库Tair（Redis开源版） | redis | × | √ |
| 日志服务SLS | sls | √ | √ |
| StarRocks | starrocks | √ | √ |
| 云数据库Tair（Tair企业版） | tair | × | √ |
| Upsert Kafka 说明仅0.11及以上版本支持。 | upsertkafka | √ | √ |

**VVR引擎版本：vvr-6.0.7-flink-1.15**

| 数据源 | 连接器名称 | 支持源表 | 支持结果表 |
|---|---|---|---|
| 云原生数据仓库 AnalyticDB MySQL版 3.0 | adb3.0 | × | √ |

实时计算（流计算）

| 云原生数据仓库 AnalyticDB PostgreSQL 版（ADB PG） | adbpg | × | √ |
|---|---|---|---|
| Blackhole | blackhole | × | √ |
| ClickHouse | clickhouse | × | √ |
| 云数据库HBase | cloudhbase | × | √ |
| Datagen | datagen 说明用于调试的连接器， 可以周期性地生成 Datagen源表对应类型的随机数据。 | √ | × |
| 数据总线DataHub | datahub | √ | √ |
| elasticsearch 说明仅6.x & 7.x版本支持。 | elasticsearch | √ | √ |
| 模拟数据生成Faker | faker | √ | × |
| 实时数仓Hologres | hologres | √ | √ |
| Hudi | hudi | √ | √ |
| Iceberg | iceberg | √ | √ |
| 时序数据库InfluxDB 说明仅1.x版本支持。 | influxdb | × | √ |
| JDBC | jdbc | √ | √ |

实时计算（流计算）

| 消息队列Kafka | kafka | √ | √ |
|---|---|---|---|
| 云原生多模数据库 Lindorm | lindorm | × | √ |
| 云数据库 MongoDB | mongodb | × | √ |
| 消息队列 RocketMQ | mq | √ | √ |
| MySQL 说明仅5.6/5.7/8.0版本支持。 | mysql 说明支持连接RDS MySQL版、 PolarDB MySQL版及自建MySQL。 | √ | √ |
| 大数据计算服务 MaxCompute | odps | √ | √ |
| 表格存储 Tablestore（OTS） | ots | √ | √ |
| Apache Paimon 说明仅0.9版本支持。 | paimon | √ | √ |
| Postgres CDC 说明仅9.6及以上版本支持。 | postgres-cdc | √ | × |
| Print | print 说明 Print是用于调试的连接器，允许接收并打印一定数量的输入记录。 | × | √ |

实时计算（流计算）

| 云数据库 RDS MySQL 版 | rds | × | √ |
|---|---|---|---|
| 云数据库Tair（Redis开源版） | redis | × | √ |
| 日志服务SLS | sls | √ | √ |
| StarRocks | starrocks | √ | √ |
| 云数据库Tair（Tair企业版） | tair | × | √ |
| Upsert Kafka 说明仅0.11及以上版本支持。 | upsertkafka | √ | √ |

**VVR引擎版本：vvr-4.0.18-flink-1.13**

| 数据源 | 连接器名称 | 支持源表 | 支持结果表 |
|---|---|---|---|
| 云原生数据仓库 AnalyticDB MySQL版 3.0 | adb3.0 | × | √ |
| 云原生数据仓库 AnalyticDB PostgreSQL 版（ADB PG） | adbpg | × | √ |
| Blackhole | blackhole | × | √ |
| ClickHouse | clickhouse | × | √ |
| 云数据库HBase | cloudhbase | × | √ |

实时计算（流计算）

| Datagen | datagen 说明用于调试的连接器， 可以周期性地生成 Datagen源表对应类型的随机数据。 | √ | × |
|---|---|---|---|
| 数据总线DataHub | datahub | √ | √ |
| elasticsearch 说明仅6.x & 7.x版本支持。 | elasticsearch | √ | √ |
| 模拟数据生成Faker | faker | √ | × |
| 实时数仓Hologres | hologres | √ | √ |
| Hudi | hudi | √ | √ |
| Iceberg | iceberg | √ | √ |
| 时序数据库InfluxDB | influxdb | × | √ |
| 消息队列Kafka | kafka | √ | √ |
| 云原生多模数据库 Lindorm | lindorm | × | √ |
| 云数据库 MongoDB | mongodb | × | √ |
| 消息队列 RocketMQ | mq | √ | √ |
| MySQL | mysql 说明支持连接RDS MySQL版、 PolarDB MySQL版及自建MySQL。 | √ | √ |

实时计算（流计算）

| MySQL-CDC | mysql-cdc | √ | × |
|---|---|---|---|
| 大数据计算服务 MaxCompute | odps | √ | √ |
| 表格存储 Tablestore（OTS） | ots | × | √ |
| Postgres CDC | postgres-cdc | √ | × |
| Print | print 说明 Print是用于调试的连接器，允许接收并打印一定数量的输入记录。 | × | √ |
| random | random | √ | × |
| 云数据库 RDS MySQL 版 | rds | × | √ |
| 云数据库Tair（Redis开源版） | redis | × | √ |
| 日志服务SLS | sls | √ | √ |
| Upsert Kafka | upsertkafka | √ | √ |

**自定义连接器**

在使用Flink SQL开发作业时，需要使用SQL连接器连接您的源表和结果表。Flink支持云上常用的多种类型的连接器，但相对于目前大数据常用的技术栈而言，仍然只是较少的一部分，为了支持您可以使用更多类型的连接器，我们支持您自定义连接器后上传使用。详细操作请参见《**Flink****存算分离版****用户指南》** > **《管理**
**自定义连接器》**。

### Datagen

**背景信息**

Datagen是主要用于调试的连接器，可以周期性地生成Datagen源表对应类型的随机数据。如果您在开发或测试时，需要使用一些测试数据来快速验证业务逻辑，您可以使用Datagen连接器来生成随机数据。 Datagen支持计算列语法Computed Column syntax，使它可以灵活地生成数据。 实时计算（流计算）

| 类别 | 详情 |
|---|---|
| 支持类型 | 源表 |
| 运行模式 | 批模式和流模式 |
| 数据格式 | 暂不适用 |
| 特有监控指标 | 暂无 |
| API种类 | SQL |
| 是否支持更新或删除结果表数据 | 不涉及 |

**语法结构**

```
  name VARCHAR,
  score BIGINT
) WITH ( );
```

**WITH参数**

| 参数 | 说明 | 数据类型 | 是否必填 | 默认值 | 备注 |
|---|---|---|---|---|---|
| connector | 源表类型。 | String | 是 | 无 | 固定值为 datagen 。 |
| rows-per- second | 生成随机数据的速率。 | Long | 否 | 10000 （条/ 秒） | 无。 |
| number-of- rows | 生成数据的总条数。 | Long | 否 | 无 | 默认生成的是无界数据源表。如果任意字段生成器类型为序列生成器，则当某一字段的序列全部生成后，Source结束，生成有界表。 |
| fields. <field>.kin d | 为<field>生成数据的生成器类型。 | String | 否 | random | 参数可选值： random：随机生成器。 sequence：序列生成器。 关于生成器详情请参见生成器。 |

实时计算（流计算）

| fields. <field>.mi n | 生成随机数的最小值。 | 与<field> 类型相同 | 否 | <field> 类型的最小值 | 在fields.<field>.kind参数设置为random时，该参数配置有效。只支持数字类型。 |
|---|---|---|---|---|---|
| fields. <field>.ma x | 生成随机数的最大值。 | 与<field> 类型相同 | 否 | <field> 类型的最大值 | 同fields.<field>.min。 |
| fields. <field>.ma x-past | 生成随机时间戳时，相对于本地机器当前时间戳的最大过去时间。 | Duration | 否 | 0 | 只支持时间戳类型。 |
| fields. <field>.len gth | 生成随机字符串的长度或者生成集合的容量。 | Integer | 否 | 100 | 支持以下任意一种类型： char varchar binary varbinary string array map multiset |
| fields. <field>.sta rt | 序列生成器的起始值。 | 与<field> 类型相同 | 否 | 无 | 在fields.<field>.kind参数设置为sequence时，该参数配置有效。 |
| fields. <field>.en d | 序列生成器的结束值。 | 与<field> 类型相同 | 否 | 无 | 在fields.<field>.kind参数设置为sequence时，该参数配置有效。 |

**说明**

参数中的<field>需要替换为您在DDL中定义的目标字段名。

**生成器**

随机生成器（random）：生成随机值。您可以指定随机生成数据的最大值和最小值。 序列生成器（sequence）：在一定范围内生成有序值，当生成序列达到结束值时结束，因此使用序列生成器将生成有界表。您可以指定序列的起始值和结束值。 各种数据类型支持的生成器如下所示。

| 类型 | 支持的生成器 | 备注 |
|---|---|---|

实时计算（流计算）

| BOOLEAN | random | 无。 |
|---|---|---|
| CHAR | random/sequence | 无。 |
| VARCHAR | random/sequence | 无。 |
| BINARY | random/sequence | 无。 |
| VARBINARY | random/sequence | 无。 |
| STRING | random/sequence | 无。 |
| DECIMAL | random/sequence | 无。 |
| TINYINT | random/sequence | 无。 |
| SMALLINT | random/sequence | 无。 |
| INT | random/sequence | 无。 |
| BIGINT | random/sequence | 无。 |
| FLOAT | random/sequence | 无。 |
| DOUBLE | random/sequence | 无。 |
| DATE | random | 始终使用本地机器的当前日期。 |
| TIME | random | 始终使用本地机器的当前时间。 |
| TIMESTAMP | random | 在相对于本地机器当前时间戳的最大过去时间范围内生成。 |
| TIMESTAMP LTZ _ | random | 同TIMESTAMP。 |
| ROW | random | 生成随机子字段。 |
| ARRAY | random | 生成随机元素。 |

实时计算（流计算）

| MAP | random | 生成随机（key,value）。 |
|---|---|---|
| MULTISET | random | 生成随机元素。 |

**使用示例**

```
 id INT,
 score INT
) WITH (
 'connector' = 'datagen',
 'fields.id.kind'='sequence',
 'fields.id.start'='1',
 'fields.id.end'='50',
 'fields.score.kind'='random',
 'fields.score.min'='70',
 'fields.score.max'='100'
);
```

### Blackhole

**背景信息**

Blackhole是主要用于调试的连接器，允许接收所有的输入记录。如果您在注册其他类型的连接器结果表时报错，但不确定是系统问题还是结果表WITH参数错误，您可以将WITH参数修改为**'connector' =**
**'blackhole'**后，单击**深度检查**。如果不再报错，则证明系统没有问题，您需要确认修改WITH参数。
测试作业运行阶段是否存在某阶段有性能消耗，以排除插入数据环节的影响。 测试中间UDF输出的正确性，此时可以直接使用Blackhole链接器，而无需使用其他实质性的结果表。

| 类别 | 详情 |
|---|---|
| 支持类型 | 结果表 |
| 运行模式 | 批模式和流模式 |
| 数据格式 | 暂不适用 |
| 特有监控指标 | 暂无 |

实时计算（流计算）

| API种类 | SQL |
|---|---|
| 是否支持更新或删除结果表数据 | 是 |

**语法结构**

```
  name VARCHAR,
  score BIGINT
) WITH ( );
```

您也可以基于现有的表模式使用 `LIKE` 子句来创建，如下所示。

```
CREATE TABLE blackhole_sink WITH ('connector' = 'blackhole') LIKE table_source (EXCLUDING ALL);
```

**WITH参数**

| 参数 | 说明 | 数据类型 | 是否必填 | 默认值 | 备注 |
|---|---|---|---|---|---|
| connector | 结果表类型 | String | 是 | 无 | 固定值为 blackhole 。 |

**使用示例**

```
CREATE TEMPORARY TABLE table_source(
  name VARCHAR,
  score BIGINT
) WITH (
  ...
);
  name VARCHAR,
  score BIGINT
) WITH ( ); INSERT INTO blackhole_sink SELECT * from table_source;
```

### print

**背景信息**

实时计算（流计算） Print是用于调试的连接器，允许接收并打印一定数量的输入记录。如果您想观察SQL的中间结果，或者观察最终输出结果，可以给SQL语句添加Print结果表，即将WITH参数修改为**'connector'='print'**后，单击运行，在JobManager的日志中观察打印出的结果信息。

| 类别 | 详情 |
|---|---|
| 支持类型 | 结果表 |
| 运行模式 | 批模式和流模式 |
| 数据格式 | 暂不适用 |
| 特有监控指标 | 暂无 |
| API种类 | SQL |
| 是否支持更新或删除结果表数据 | 是 |

**前提条件**

因为Print结果表数据输出为Info日志，所以如果您需要查看Print结果表的结果数据，则需要将日志级别调至Info，否则无法查到结果数据。 Taskmanager.out日志展示数据限制为2000条。如果您有排查脏数据或特定数据等需求，建议在 Where条件中指定业务场景相关条件后，进行Print操作，以避免因为数据条数限制导致无法排查。

**语法结构**

```
  a INT,
  b varchar
) WITH (
  'connector'='print',
  'logger'='true'
);
```

您也可以基于现有的表模式使用 `LIKE` 子句来创建，代码示例如下。

```
CREATE TABLE print_table WITH ('connector' = 'print') LIKE table_source (EXCLUDING ALL)
```

**WITH参数**

| 参数 | 说明 | 数据类型 | 是否必填 | 默认值 | 备注 |
|---|---|---|---|---|---|

实时计算（流计算）

| connector | 表类型。 | String | 是 | 无 | 固定值为print。 |
|---|---|---|---|---|---|
| logger | 控制台是否显示数据结果。 | Boolean | 否 | false | 取值如下： false（默认值）：不显示。 true：显示。 |
| print- identifier | 数据结果标识。 | String | 否 | 无 | 在日志中通过数据结果标识检索信息。 |
| sink.parall elism | 结果表并行度。 | Int | 否 | 上游并行度 | 无。 |

**使用示例**

```
CREATE TABLE table_source(
  name VARCHAR,
  score BIGINT
) WITH (
  ...
);
  name VARCHAR,
  score BIGINT
) WITH ( ); INSERT INTO print_sink SELECT * from table_source;
```

### 模拟数据生成Faker

**背景信息**

模拟数据生成Faker是系统内置的连接器，它根据表中每个字段提供的Java Faker表达式生成测试数据。当您在开发或测试时，需要使用一些测试数据来验证业务逻辑时，推荐您使用模拟数据生成连接器。 模拟数据生成连接器支持的信息如下。

| 类别 | 详情 |
|---|---|
| 支持类型 | 源表 |
| 运行模式 | 批模式和流模式 |

实时计算（流计算）

| 数据格式 | 不适用 |
|---|---|
| 特有监控指标 | 无 |
| API种类 | SQL |
| 是否支持更新或删除结果表数据 | 不涉及 |

**使用限制**

仅支持部分数据类型，包括CHAR(n)、VARCHAR(n)、STRING、TINYINT、SMALLINT、INT、BIGINT、 FLOAT、DOUBLE、DECIMAL、BOOLEAN、TIMESTAMP、ARRAY、MAP、MULTISET和ROW。

**语法结构**

```
CREATE TABLE faker_source (
  `name` STRING,
  `age` INT
) WITH (
  'connector' = 'faker',
  'fields.name.expression' = '#{superhero.name}',
  'fields.age.expression' = '#{number.numberBetween ''0'',''1000''}'
);
```

**WITH参数**

| 参数 | 说明 | 数据类型 | 是否必填 | 默认值 | 备注 |
|---|---|---|---|---|---|
| connector | 表类型。 | String | 是 | 无 | 固定值为faker。 |
| fields. <field>.expression | 生成该字段值的Java Faker表达式。 | String | 是 | 无 | 详情请参见字段表达式。 |
| fields.<field>.null- rate | 该字段值为空的占比。 | Float | 否 | 0.0 | 无 |
| fields. <field>.length | ARRAY、MAP或 MULTISET集合类型的大小。 | Integer | 否 | 1 | 无 |
| number-of-rows | 生成的数据行数。 | Integer | 否 | -1 | 如果设置了该参数，则源表是有界的，否则是无界的。 |
| rows-per-second | 生成数据的速率。 | Integer | 否 | 10000 | 默认值为10000条/秒。 |

实时计算（流计算）

**使用示例**

```
CREATE TEMPORARY TABLE heros_source (
  `character_id` INT,
  `name` STRING,
  `power` STRING,
  `phone_number` STRING,
  `age` INT,
  `address` STRING,
  `score` MAP<STRING, INT>,
  `work_locations` ARRAY<STRING>,
  `spells` MULTISET<STRING>,
  `house-points` ROW<`house` STRING, `points` INT>,
  `user_ip` STRING,
  `request_url` STRING,
  `status_code` STRING,
  `sys_time` AS PROCTIME(),
  `event_time` TIMESTAMP(3),
) WITH (
  'connector' = 'faker',
  'fields.character_id.expression' = '#{number.numberBetween ''0'',''10000''}',
  'fields.name.expression' = '#{superhero.name}',
  'fields.power.expression' = '#{superhero.power}',
  'fields.power.null-rate' = '0.05',
  'fields.phone_number.expression' = '#{PhoneNumber.cellPhone}',
  'fields.age.expression' = '#{number.numberBetween ''0'',''1000''}',
  'fields.address.expression' ='#{harry_potter.location}',
  'fields.score.key.expression' = '#{harry_potter.character}',
  'fields.score.value.expression' = '#{number.numberBetween ''10'',''100''}',
  'fields.score.length' = '2',
  'fields.work_locations.expression' = '#{harry_potter.location}',
  'fields.work_locations.length' = '2',
  'fields.spells.expression' = '#{harry_potter.spell}',
  'fields.spells.length' = '2',
  'fields.house-points.house.expression' = '#{harry_potter.house}',
  'fields.house-points.points.expression' = '#{number.numberBetween ''10'',''100''}',
  'fields.user_ip.expression' = '#{Internet.publicIpV4Address}',
  'fields.request_url.expression' = '#{Internet.url}',
  'fields.status_code.expression' = '#{regexify ''(200|201|204|400|401|403|301){1}''}',
  'fields.event_time.expression' = '#{Date.future ''365'',''DAYS''}',
  'number-of-rows' = '30'
);
  `character_id` INT,
  `name` STRING,
  `power` STRING,
  `phone_number` STRING,
  `age` INT,
  `address` STRING,
  `score` MAP<STRING, INT>,
  `work_locations` ARRAY<STRING>,
  `spells` MULTISET<STRING>,
`hosepoints`ROW<`hose`STRING `points`INT>
```

实时计算（流计算）

```
  house-points ROW<house STRING, points INT>,
  `user_ip` STRING,
  `request_url` STRING,
  `status_code` STRING,
  `sys_time` TIMESTAMP,
  `event_time` TIMESTAMP(3)
) WITH ( ); INSERT INTO blackhole_sink SELECT * FROM heros_source;
```

**字段表达式**

操作方法使用模拟数据生成连接器时，DDL中定义的每个字段，都需要在WITH语句中提供具体的表达式。表达式的固定格式为**'fields.<field>.expression' = '#{className.methodName ''parameter'',**
**...}'**。相关的参数说明如下表所示。

| 参数 | 说明 |
|---|---|
| field | 表示DDL中具体的字段名。 |
| className | 表示Faker类的类名。 Java Faker提供了大约80个Faker类用于生成您需要的字段表达式，您可以根据需要选择对应的类。 说明 Faker类的类名不区分大小写。 |
| methodName | 表示方法名。 说明方法名不区分大小写。 |
| parameter | 表示方法的入参。 说明方法的入参需要使用两个半角单引号（' ）括起来。 多个参数使用半角逗号（,）进行分隔。 |

示例本文结合Java Faker API文档和语法结构部分中的age字段表达式**'fields.age.expression' = '#**
**{number.numberBetween ''0'',''1000''}'** 为例，为您介绍如何为DDL中的字段正确地生成SQL
表达式。 实时计算（流计算） i. 在Java Faker API文档中，找到Number类。 ii. 在Number类中找到numberBetween方法，并查看其方法描述。 numberBetween方法表示返回指定数字范围的值。 iii. 根据类名Number和方法名numberBetween传入方法的参数0和1000，生成age字段的SQL表达式**'fields.age.expression' = '#{number.numberBetween ''0'',''1000''}'** 。 表示生成的age字段的值在0到1000范围内。

### Iceberg

**背景信息**

实时计算（流计算） Apache Iceberg是一种开放的数据湖表格格式。您可以借助Apache Iceberg快速地在HDFS或者云端OSS 上构建自己的数据湖存储服务，并借助开源大数据生态的Flink、Spark、Hive、Presto等计算引擎来实现数据湖的分析。

| 类别 | 详情 |
|---|---|
| 支持类型 | 源表和结果表 |
| 运行模式 | 批模式和流模式 |
| 数据格式 | 暂不适用 |
| 特有监控指标 | 暂无 |
| API种类 | SQL |
| 是否支持更新或删除结果表数据 | 是 |

**特色功能**

基于HDFS或者对象存储构建低成本的轻量级数据湖存储服务。 完善的ACID语义。 支持历史版本回溯。 支持高效的数据过滤。 支持Schema Evolution。 支持Partition Evolution。 支持和自建Hive Metastore配合使用。

**说明**

您可以借助Flink高效的容错能力和流处理能力，把海量的日志行为数据实时导入到Apache Iceberg数据湖内，再借助Flink或者其他分析引擎来实现数据价值的提取。

**使用限制**

**说明**

仅实时计算引擎VVR 8.0.7及以上版本支持v2表格式。

**语法结构**

实时计算（流计算）

```
  id    BIGINT,
  data  STRING
  PRIMARY KEY(`id`) NOT ENFORCED
```

)

```
 PARTITIONED BY (data)
 WITH (
 'connector' = 'iceberg',
  ...
);
```

**WITH参数**

**通用（源表）**

| 数据是否必默认参数说明类型填值 Strin connector 源表类型是无 g catalog- Catalog名 Strin 是无 name 称 g catalog- Strin defa 数据库名称是 database g ult 分布式文件 Strin io-impl 系统的实现是无 g 类名阿里云对象存储服务 Strin oss.endpoint 否无 OSS的 g Endpoint access.ke y.id：VVR 8.0.6及以阿里云账号下版本的 Strin 是无 access- AccessKey g key-id： ID VVR 8.0.7 及以上版本 | 参数 | 说明 |  | 数据类型 | 是否必填 | 默认值 | 备注 |  |  |
|---|---|---|---|---|---|---|---|---|---|
|  | connector | 源表类型 |  | Strin g | 是 | 无 | 固定值为 iceberg 。 |  |  |
|  | catalog- name | Catalog名称 |  | Strin g | 是 | 无 | 请填写为自定义的英文名。 |  |  |
|  | catalog- database | 数据库名称 |  | Strin g | 是 | defa ult | 对应在DLF上创建的数据库名称，例如dlf db。 _ |  |  |
|  | io-impl | 分布式文件系统的实现类名 |  | Strin | 是 | 无 | 固定值为 org.apache.iceberg.aliyun.oss.OSSF ileIO 。 |  |  |
|  |  |  |  |  |  |  |  | org.apache.iceberg.aliyun.oss.OSSF |  |
|  |  |  | 名 | g |  |  | ileIO |  |  |
|  | oss.endpoint | 阿里云对象存储服务 OSS的 Endpoint |  | Strin g | 否 | 无 | 推荐您为oss.endpoint参数配置OSS的VPC Endpoint。例如，如果您选择的地域为cn- hangzhou地域，则oss.endpoint需要配置为 oss-cn-hangzhou-internal.aliyuncs.com。 |  |  |
|  | access.ke y.id：VVR 8.0.6及以下版本 access- key-id： VVR 8.0.7 及以上版本 | 阿里云账号的 AccessKey ID |  | Strin g | 是 | 无 | 无。 |  |  |

实时计算（流计算）

| access.ke y.secret： VVR 8.0.6 及以下版本阿里云账号的 Strin access- AccessKey g 是无 key- Secret secret： VVR 8.0.7 及以上版本 Catalog的 Strin catalog-impl 是无 Class类名 g 表数据存放 Strin warehouse 在OSS的路是无 g 径阿里云账号 Strin dlf.catalog-id 是无的账号ID g DLF服务的 Strin dlf.endpoint 是无 Endpoint g DLF服务的 Strin dlf.region-id 是无地域名 g 仅当使 Hive 用Hive Strin uri metastore Catalo 无 g 的thrift URI g时，必填。 |  |  |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|
|  | access.ke y.secret： VVR 8.0.6 及以下版本 access- key- secret： VVR 8.0.7 及以上版本 | 阿里云账号的 AccessKey Secret |  | Strin g | 是 | 无 |  |  |  |
|  | catalog-impl | Catalog的 Class类名 |  | Strin | 是 | 无 | 固定值为 org.apache.iceberg.aliyun.dlf.DlfC atalog 。 |  |  |
|  |  |  |  |  |  |  |  | org.apache.iceberg.aliyun.dlf.DlfC |  |
|  |  |  | ass类名 | g |  |  | atalog |  |  |
|  | warehouse | 表数据存放在OSS的路径 |  | Strin g | 是 | 无 | 无。 |  |  |
|  | dlf.catalog-id | 阿里云账号的账号ID |  | Strin g | 是 | 无 | 无。 |  |  |
|  | dlf.endpoint | DLF服务的 Endpoint |  | Strin g | 是 | 无 | 推荐您为dlf.endpoint参数配置DLF的VPC Endpoint。例如，如果您选择的地域为cn- hangzhou地域，则dlf.endpoint参数需要配置为dlf-vpc.cn- hangzhou.aliyuncs.com。 |  |  |
|  | dlf.region-id | DLF服务的地域名 |  | Strin g | 是 | 无 | 请和dlf.endpoint选择的地域保持一致。 |  |  |
|  | uri | Hive metastore 的thrift URI |  | Strin g | 仅当使用Hive Catalo g时，必填。 | 无 | 配合自建Hive Metastore使用。 |  |  |

**结果表独有**

| 参数 | 说明 | 数据类型 | 是否必填 | 默认值 | 备注 |
|---|---|---|---|---|---|
| write.oper ation | 写入操作模式 | Strin g | 否 | upsert | upsert（默认）：数据更新。 insert：数据追加写入。 bulk insert：批量写入（不更新）。 _ |

实时计算（流计算）

| hive sync. _ enable | 是否开启同步元数据到Hive 功能 | boole an | 否 | false | 参数取值如下： true：开启 false（默认值）：不开启。 |
|---|---|---|---|---|---|
| hive sync. _ mode | Hive数据同步模式 | Strin g | 否 | hms | hms（默认值）：采用Hive Metastore或者DLF Catalog时，需要设置hms。 jdbc：采用jdbc Catalog时，需要设置为jdbc。 |
| hive sync. _ db | 同步到 Hive的数据库名称 | Strin g | 否 | 当前 Table在 Catalo g中的数据库名 | 无。 |
| hive sync. _ table | 同步到 Hive的表名称 | Strin g | 否 | 当前 Table名 | 无。 |
| dlf.catalog .region | DLF服务的地域名 | Strin g | 否 | 无 | 说明仅当hive sync.mode设置 _ 为 hms 时，dlf.catalog.region参数设置才生效。 请和dlf.catalog.endpoint选择的地域保持一致。 |
| dlf.catalog .endpoint | DLF服务的 Endpoi nt | Strin g | 否 | 无 | 说明仅当hive sync.mode设置为hms _ 时，dlf.catalog.endpoint参数设置才生效。 推荐您为dlf.catalog.endpoint参数配置DLF的VPC Endpoint。例如，如果您选择的地域为cn-hangzhou地域， 则dlf.catalog.endpoint参数需要配置为dlf-vpc.cn- hangzhou.aliyuncs.com。 |

**类型映射**

| Iceberg字段类型 | Flink字段类型 |
|---|---|
| BOOLEAN | BOOLEAN |
| INT | INT |

实时计算（流计算）

| LONG | BIGINT |
|---|---|
| FLOAT | FLOAT |
| DOUBLE | DOUBLE |
| DECIMAL(P,S) | DECIMAL(P,S) |
| DATE | DATE |
| TIME | TIME 说明 Iceberg时间戳精度为微秒，Flink时间戳精度为毫秒。在使用 Flink读取Iceberg数据时，时间精度会对齐到毫秒。 |
| TIMESTAMP | TIMESTAMP |
| TIMESTAMPTZ | TIMESTAMP LTZ _ |
| STRING | STRING |
| FIXED(L) | BYTES |
| BINARY | VARBINARY |
| STRUCT<...> | ROW |
| LIST<E> | LIST |
| MAP<K,V> | MAP |

**代码示例**

请确认您已创建了OSS Bucket和DLF数据库。

**说明**

在创建DLF数据库**选择路径**时，建议按照${warehouse}/${database_name}.db格式填写。例如， 如果warehouse地址为oss://iceberg-test/warehouse，数据库的名称为dlf_db，则dlf_db的OSS路实时计算（流计算）

**结果表示例**

```
  id    BIGINT,
  data  STRING
) WITH ( );
  id    BIGINT,
  data  STRING
) WITH (
  'connector' = 'iceberg',
  'catalog-name' = '<yourCatalogName>',
  'catalog-database' = '<yourDatabaseName>',
  'io-impl' = 'org.apache.iceberg.aliyun.oss.OSSFileIO',
  'oss.endpoint' = '<yourOSSEndpoint>',
  'access.key.id' = '${secret_values.ak_id}',
  'access.key.secret' = '${secret_values.ak_secret}',
  'catalog-impl' = 'org.apache.iceberg.aliyun.dlf.DlfCatalog',
  'warehouse' = '<yourOSSWarehousePath>',
  'dlf.catalog-id' = '<yourCatalogId>',
  'dlf.endpoint' = '<yourDLFEndpoint>',
  'dlf.region-id' = '<yourDLFRegionId>'
); INSERT INTO dlf_iceberg SELECT * FROM datagen;
```

**源表示例**

使用Hive Catalog，配合自建Hive Metastore（HMS）使用。 您需要保证Flink与HMS集群网络互通，数据将存储在 `oss://<bucket>/<path>/<database-` `name>/flink_table` 目录下。

```
CREATE TEMOPORY TABLE flink_table (
  id   BIGINT,
  data STRING
) WITH (
  'connector'='iceberg',
  'catalog-name'='<yourCatalogName>',
  'catalog-database'='<yourDatabaseName>',
  'uri'='thrift://<ip>:<post>',
  'warehouse'='oss://<bucket>/<path>',
  'io-impl'='org.apache.iceberg.aliyun.oss.OSSFileIO',
  'access-key-id'='<aliyun ak>',
  'access-key-secret'='<aliyun sk>',
  'oss.endpoint'='<yourOSSEndpoint>'
);
```

实时计算（流计算）

```
  id    BIGINT,
  data  STRING
) WITH (
  'connector' = 'iceberg',
  'catalog-name' = '<yourCatalogName>',
  'catalog-database' = '<yourDatabaseName>',
  'io-impl' = 'org.apache.iceberg.aliyun.oss.OSSFileIO',
  'oss.endpoint' = '<yourOSSEndpoint>',
  'access.key.id' = '${secret_values.ak_id}',
  'access.key.secret' = '${secret_values.ak_secret}',
  'catalog-impl' = 'org.apache.iceberg.aliyun.dlf.DlfCatalog',
  'warehouse' = '<yourOSSWarehousePath>',
  'dlf.catalog-id' = '<yourCatalogId>',
  'dlf.endpoint' = '<yourDLFEndpoint>',
  'dlf.region-id' = '<yourDLFRegionId>'
);
  id    BIGINT,
  data  STRING
) WITH (
  'connector' = 'iceberg',
  'catalog-name' = '<yourCatalogName>',
  'catalog-database' = '<yourDatabaseName>',
  'io-impl' = 'org.apache.iceberg.aliyun.oss.OSSFileIO',
  'oss.endpoint' = '<yourOSSEndpoint>',
  'access.key.id' = '${secret_values.ak_id}',
  'access.key.secret' = '${secret_values.ak_secret}',
  'catalog-impl' = 'org.apache.iceberg.aliyun.dlf.DlfCatalog',
  'warehouse' = '<yourOSSWarehousePath>',
  'dlf.catalog-id' = '<yourCatalogId>',
  'dlf.endpoint' = '<yourDLFEndpoint>',
  'dlf.region-id' = '<yourDLFRegionId>'
); BEGIN STATEMENT SET; INSERT INTO src_iceberg VALUES (1, 'AAA'), (2, 'BBB'), (3, 'CCC'), (4, 'DDD'), (5, 'E EE'); INSERT INTO dst_iceberg SELECT * FROM src_iceberg; END;
```

### Postgres CDC

Postgres CDC可用于依次读取PostgreSQL数据库全量快照数据和变更数据，保证不多读一条也不少读一条数据。即使发生故障，也能采用Exactly Once方式处理。本文为您介绍如何使用Postgres CDC连接器。

**背景信息**

实时计算（流计算）

| 类别 | 详情 |
|---|---|
| 支持类型 | 源表说明您可以使用JDBC作为结果表和维表连接器。 |
| 运行模式 | 仅支持流模式 |
| 数据格式 | 暂不适用 |
| 特有监控指标 | currentFetchEventTimeLag：数据产生到拉取到Source Operator的间隔。 currentEmitEventTimeLag：数据产生到离开Source Operator的间隔。 sourceIdleTime：source至今有多久不产生新数据。 说明 currentFetchEventTimeLag与currentEmitEventTimeLag指标仅在增量阶段有效，全量阶段该值恒为0。 |
| API种类 | SQL |
| 是否支持更新或删除结果表数据 | 不涉及 |

**特色功能**

Postgres CDC连接器接入CDC增量快照框架（实时计算引擎VVR 8.0.6及以上版本）。Postgres CDC读取历史全量数据后，自动切换到WAL变更日志读取，保证不多读也不少读数据。即使发生故障，也能保证 Exactly Once语义处理数据。Postgres CDC源表提供了并发读取全量数据，无锁读取和断点续传的能力。 作为源表，功能与优势详情如下： 流批一体，支持读取全量和增量数据，无需维护两套流程。 支持并发读取全量数据，性能水平扩展。 全量读取无缝切换增量读取，自动缩容，节省计算资源。 全量阶段读取支持断点续传，更稳定。 无锁读取全量数据，不影响线上业务。

**前提条件**

Postgres CDC连接器通过PostgreSQL数据库的逻辑复制读取CDC变更流数据，需要满足以下条件： wal_level参数的值需设置为logical，即在预写式日志WAL（Write-ahead logging）中增加支持逻辑编码所需的信息。 执行 ALTER TABLE schema.table REPLICA IDENTITY FULL; 命令设置订阅表的REPLICA IDENTITY为 FULL（发出的插入和更新操作事件包含表中所有列的旧值），以保障该表数据同步的一致性。 实时计算（流计算）

**说明**

REPLICA IDENTITY是PostgreSQL特有的表级设置，它决定了逻辑解码插件在发生（INSERT）和更新（UPDATE）事件时，是否包含涉及的表列的旧值。REPLICA IDENTITY取值含义详情请参见REPLICA IDENTITY。 需要确保max_wal_senders和max_replication_slots的参数值均大于当前数据库复制槽已使用数与 Flink作业所需要的slot数量。 确保账户系统权限为SUPERUSER或者同时拥有LOGIN和REPLICATION权限，并且具有订阅表的 SELECT权限用于全量数据查询。

**说明**

阿里云RDS PostgreSQL、Amazon RDS PostgreSQL或者自建PostgreSQL上相应的配置可能有差异.

**注意事项**

**请及时管理Replication Slot，以免出现磁盘空间浪费的问题。**

为了防止在Flink作业重启过程中由于Checkpoint对应的WAL（Write-Ahead Log）段被清除而引发数据丢失，Flink作业不会自动移除Replication Slot。因此，如果确认特定的Flink作业不会再次启动，应当手动删除相关的Replication Slot，以释放其占用的资源。另外，如果PostgreSQL的Replication Slot的确认位点长时间不向前推进，PostgreSQL不会清理该槽位点之后的WAL条目，这可能会导致未使用的WAL 积累而占用过多的磁盘空间。

**开启增量快照时，Postgres CDC连接器必须开启Checkpoint，并且Source表必须声明主键。**

**Source多并发读取全量数据时会创建多个临时的Replication Slot。**

不开启增量快照读取的PostgreSQL CDC Source仅支持单一并发，因此只需要一个全局Slot。当开启增量快照时，PostgreSQL CDC Source在全量阶段所需的最大Slot数量为 `Source`数量 * 并发数 `+ 1` 。 进入增量阶段后，系统自动回收在全量阶段创建的Slot，仅保留一个全局Slot。如果Slot数量有限，需要控制全量阶段的并发数量，这样做的缺点是会降低读取速度。如果下游算子或存储支持幂等性，可以启用 `scan.incremental.snapshot.backfill.skip = true` 以跳过全量阶段的日志读取，这样做的缺点是仅能提供至少一次（At-Least Once）的语义保证。如果SQL要做聚合、关联等操作，不建议跳过全量阶段日志的读取。 不开启增量快照时，Postgres CDC连接器不支持在全表扫描阶段执行Checkpoint。 不开启增量快照时，如果您的作业在全表扫描阶段触发Checkpoint，则可能由于Checkpoint超时导致作业Failover。因此，建议您在**其他配置**中配置如下参数，避免在全量同步阶段由于Checkpoint超时导致 Failover。

```
execution.checkpointing.interval: 10min execution.checkpointing.tolerable-failed-checkpoints: 100 restart-strategy: fixed-delay restart-strategy.fixed-delay.attempts: 2147483647
```

相关的参数说明详情如下表所示。

| 参数 | 说明 | 备注 |
|---|---|---|
| execution.check pointing.interval | Checkpoint的时间间隔。 | 单位是Duration类型，例如10min或30s。 |

实时计算（流计算）

| execution.check pointing.tolerabl e-failed- checkpoints | 容忍Checkpoint失败的次数。 | 该参数的取值与Checkpoint调度间隔时间的乘积就是允许的快照读取时间。 说明如果表特别大，建议将该参数值配置得大一些。 |
|---|---|---|
| restart-strategy | 重启策略。 | 参数取值如下： fixed-delay：固定延迟重启策略。 failure-rate：故障率重启策略。 exponential-delay：指数延迟重启策略。 详情请参见Restart Strategies。 |
| restart- strategy.fixed- delay.attempts | 固定延迟重启策略下， 尝试重启的最大次数。 | 无。 |

**语法结构**

```
  shipment_id INT,
  order_id INT,
  origin STRING,
  destination STRING,
  is_arrived BOOLEAN
) WITH (
  'connector' = 'postgres-cdc',
  'hostname' = '<yourHostname>',
  'port' = '5432',
  'username' = '<yourUserName>',
  'password' = '<yourPassWord>',
  'database-name' = '<yourDatabaseName>',
  'schema-name' = '<yourSchemaName>',
  'table-name' = '<yourTableName>'
);
```

**WITH参数**

| 参数 | 说明 | 数据类型 | 是否必填 | 默认值 | 备注 |
|---|---|---|---|---|---|
| connect or | 表类型。 | STRI NG | 是 | 无 | 固定值为 postgres-cdc 。 |

实时计算（流计算）

| hostna me | Postgres数据库的IP地址或者 Hostname。 | STRI NG | 是 | 无 | 无。 |
|---|---|---|---|---|---|
| userna me | Postgres数据库服务的用户名。 | STRI NG | 是 | 无 | 无。 |
| passwor d | Postgres数据库服务的密码。 | STRI NG | 是 | 无 | 无。 |
| databas e-name | 数据库名称。 | STRI NG | 是 | 无 | 数据库名称支持正则表达式以读取多个数据库的数据。 |
| schema -name | Postgres Schema名称。 | STRI NG | 是 | 无 | Schema名称支持正则表达式以读取多个Schema的数据。 |
| table- name | Postgres表名。 | STRI NG | 是 | 无 | 表名支持正则表达式去读取多个表的数据。 |
| port | Postgres数据库服务的端口号。 | INTE GER | 否 | 5432 | 无。 |
| decodin g.plugin .name | Postgres Logical Decoding插件名称。 | STRI NG | 否 | deco derb ufs | 根据Postgres服务上安装的插件确定。支持的插件列表如下： decoderbufs（默认值） pgoutput wal2json wal2json rds _ wal2json streaming _ wal2json rds streaming _ _ |

实时计算（流计算）

| slot.na me | 逻辑解码槽的名字。 |  | STRI | 8.0. 1版本之前为非必填， | 8.0.1 版本之前默认值为 flink | 建议每个表都设置 slot.name 参数，以避免出现 PSQLException: ERROR: replication slot "debezium" is active for PID 974 报错。 |  |
|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  | PSQLException: ERROR: replication |
|  |  | 字。 | NG | 从 8.0. | ，从 8.0.1 | slot "debezium" is active for PID 974 |  |
|  |  |  |  | 1版本开始为必填 | 版本开始无默认值 |  |  |
| debeziu m.* | Debezium属性参数。 |  | STRI NG | 否 | 无 | 更细粒度控制Debezium客户端的行为。例如 'debezium.snapshot.mode' = 'never' ， 详情请参见配置属性。 |  |
| scan.inc rement al.snaps hot.ena bled | 是否开启增量快照。 |  | BOO LEA N | 否 | false | 参数取值如下： false（默认值）：不开启增量快照。 true：开启增量快照。 说明此功能为实验性功能。仅实时计算引擎8.0.6及以上版本支持该参数。 |  |
| scan.sta rtup.mo de | 消费数据时的启动模式。 |  | STRI NG | 否 | initial | 参数取值如下： initial（默认）：在第一次启动时，会先扫描历史全量数据，然后读取最新的WAL日志数据。 latest-offset：在第一次启动时，不会扫描历史全量数据，直接从WAL日志的末尾（最新的WAL日志处）开始读取，即只读取该连接器启动以后的最新变更。 snapshot：先扫描历史全量数据，再读取全量阶段新产生的WAL日志，最终作业会停止。 |  |
| changel og- mode | 用于编码流更改的变更日志 （Changelog ）模式。 |  | Strin g | 否 | all | 支持的Changelog模式包括： ALL：支持所有类型，包括INSERT、DELETE、 UPDATE BEFORE和UPDATE AFTER。 _ _ UPSERT：仅支持Upsert类型，包括INSERT、 DELETE和UPDATE AFTER。 _ |  |
| heartbe at.interv al.ms | 发送心跳包的时间间隔。 |  | Dura tion | 否 | 30s | 单位为毫秒。 Postgres CDC连接器主动向数据库发送心跳包来保证推进Slot的偏移量。当表变更不频繁时，设置该值可以及时回收WAL日志。 |  |

实时计算（流计算）

| scan.inc rement al.snaps hot.chu nk.key- column | 指定某一列作为快照阶段切分分片的切分列。 |  | STRI NG | 否 | 无 | 默认从主键中选择第一列。 |  |
|---|---|---|---|---|---|---|---|
| scan.inc rement al.close- idle- reader.e nabled | 是否在快照结束后关闭空闲的Reader。 |  | Bool | 否 | false | 该配置生效需要设置 execution.checkpointing.checkpoints- after-tasks-finish.enabled 为true。 |  |
|  |  |  |  |  |  |  | execution.checkpointing.checkpoints- |
|  |  | 的Reader。 | ean |  |  | after-tasks-finish.enabled |  |
| scan.inc rement al.snaps hot.bac kfill.skip | 是否跳过全量阶段的日志读取。 |  | Bool ean | 否 | false | 参数取值如下： true：跳过。 增量阶段从低水位线开始读取日志。 如果下游算子或存储支持幂等性，建议跳过全量阶段日志的读取，这样做的优点是能够减少WAL Slot数量，缺点是仅能提供至少一次（At-Least Once）的语义保证 false：不跳过。 全量阶段读取分片时，会读取低水位线和高水位线之间的日志来保证一致性。 如果SQL要做聚合、关联等操作，不建议跳过全量阶段日志的读取。 |  |

**类型映射**

| Postgres CDC字段类型 | Flink字段类型 |
|---|---|
| SMALLINT | SMALLINT |
| INT2 |  |
| SMALLSERIAL |  |
| SERIAL2 |  |
| INTEGER | INT |
| SERIAL |  |

实时计算（流计算）

| BIGINT | BIGINT |
|---|---|
| BIGSERIAL |  |
| REAL | FLOAT |
| FLOAT4 |  |
| FLOAT8 | DOUBLE |
| DOUBLE PRECISION |  |
| NUMERIC(p, s) | DECIMAL(p, s) |
| DECIMAL(p, s) |  |
| BOOLEAN | BOOLEAN |
| DATE | DATE |
| TIME [(p)] [WITHOUT TIMEZONE] | TIME [(p)] [WITHOUT TIMEZONE] |
| TIMESTAMP [(p)] [WITHOUT TIMEZONE] | TIMESTAMP [(p)] [WITHOUT TIMEZONE] |
| CHAR(n) | STRING |
| CHARACTER(n) |  |
| VARCHAR(n) |  |
| CHARACTER VARYING(n) |  |
| TEXT |  |
| BYTEA | BYTES |

**使用示例**

实时计算（流计算）

```
CREATE TABLE source (
  id INT NOT NULL,
  name STRING,
  description STRING,
  weight DECIMAL(10,3)
) WITH (
  'connector' = 'postgres-cdc',
  'hostname' = '<host name>',
  'port' = '<port>',
  'username' = '<user name>',
  'password' = '<password>',
  'database-name' = '<database name>',
  'schema-name' = '<schema name>',
  'table-name' = '<table name>'
); SELECT * FROM source;
```

### 时序数据库InfluxDB

**背景信息**

时序数据库InfluxDB®版是一款专门处理高写入和查询负载的时序数据库，用于存储大规模的时序数据并进行实时分析，包括来自DevOps监控、应用指标和IoT传感器上的数据。 InfluxDB连接器支持的信息如下。

| 类别 | 详情 |
|---|---|
| 支持类型 | 结果表 |
| 运行模式 | 流模式 |
| 数据格式 | Point |
| 特有监控指标 | numRecordsOut numRecordsOutPerSecond currentSendTime |
| API种类 | SQL |
| 是否支持更新或删除结果表数据 | 否 |

**前提条件**

实时计算（流计算） 已创建InfluxDB的数据库。

**语法结构**

```
CREATE TABLE stream_test_influxdb(
 `metric` VARCHAR,
 `timestamp` BIGINT,
 `tag_value1` VARCHAR,
 `field_fieldValue1` DOUBLE
) WITH (
  'connector' = 'influxdb',
  'url' = 'http://service.cn.influxdb.aliyuncs.com:****',
  'database' = '<yourDatabaseName>',
  'username' = '<yourDatabaseUserName>',
  'password' = '<yourDatabasePassword>',
  'batchSize' ='300',
  'retentionPolicy' = 'autogen',
  'ignoreErrorData' = 'false'
);
```

建表默认格式： 第0列：metric（VARCHAR），必填。 第1列：timestamp（BIGINT），必填，单位为毫秒。 第2列：tag_value1（VARCHAR），必填，最少填写一个。 第3列：field_fieldValue1（DOUBLE），必填，最少填写一个。 写入多个field_fieldValue时，您需要按照如下格式填写。

```
field_fieldValue1 类型, field_fieldValue2 类型, ... field_fieldValueN 类型
```

示例如下。

```
field_fieldValue1 DOUBLE, field_fieldValue2 INTEGER, ... field_fieldValueNINTEGER
```

**说明**

结果表中只支持**metric**、**timestamp**、**tag_***和**field_***，不能出现其他的字段。

**WITH参数**

| 参数 | 说明 | 是否必填 | 备注 |
|---|---|---|---|
| connector | 结果表类型。 | 是 | 固定值为influxdb。 |

实时计算（流计算）

| url | InfluxDB的服务地址。 | 是 | 请联系阿里云运维工程师获取。 |
|---|---|---|---|
| database | InfluxDB的数据库名称。 | 是 | 例如db-flink。 |
| username | 数据库的用户名。 | 是 | 需要对目标数据库有写权限。 |
| password | 数据库的密码。 | 是 | 无。 |
| batchSize | 批量提交的记录条数。 | 否 | 默认每次批量提交300条记录。 |
| retentionPoli cy | 保留策略。 | 否 | 如果您不配置该参数时，该参数会被默认填写为每个数据库的默认保留策略autogen。 |
| ignoreErrorD ata | 是否忽略异常数据。 | 否 | 参数取值如下： true：忽略异常数据。 false（默认值）：不忽略异常数据。 |

**类型映射**

| InfluxDB字段类型 | Flink版字段类型 |
|---|---|
| BOOLEAN | BOOLEAN |
| INT | INT |
| BIGINT | BIGINT |
| FLOAT | FLOAT |
| DECIMAL | DECIMAL |
| DOUBLE | DOUBLE |
| DATE | DATE |
| TIME | TIME |

实时计算（流计算）

| TIMESTAMP | TIMESTAMP |
|---|---|
| VARCHAR | VARCHAR |

**使用示例**

```
CREATE TEMPORARY TABLE datahub_source(
 `metric` VARCHAR,
 `timestamp` BIGINT,
 `filedvalue` DOUBLE,
 `tagvalue` VARCHAR
) WITH (
  'connector' = 'datagen',
  'fields.metric.length' = '3',
  'fields.tagvalue.length' = '3',
  'fields.timestamp.min' = '1587539547000',
  'fields.timestamp.max' = '1619075547000',
  'fields.filedvalue.min' = '1',
  'fields.filedvalue.max' = '100000',
  'rows-per-second' = '50'
); CREATE TEMPORARY TABLE influxdb_sink(
  `metric` VARCHAR,
  `timestamp` BIGINT,
  `field_fieldValue1` DOUBLE,
  `tag_value1` VARCHAR
) WITH (
  'connector' = 'influxdb',
  'url' = 'https://***********.influxdata.tsdb.aliyuncs.com:****',
  'database' = '<yourDatabaseName>',
  'username' = '<yourDatabaseUserName>',
  'password' = '<yourDatabasePassword>',
  'batchSize' ='100',
  'retentionPolicy' = 'autogen',
  'ignoreErrorData' = 'false'
); INSERT INTO influxdb_sink SELECT
  `metric`,
  `timestamp`,
  `filedvalue`,
  `tagvalue`
FROM datahub_source;
```

### 表格存储Tablestore（OTS）

**背景信息**

实时计算（流计算） 表格存储Tablestore（又名OTS）面向海量结构化数据提供Serverless表存储服务，同时针对物联网场景深度优化提供一站式的IoTstore解决方案。适用于海量账单、IM消息、物联网、车联网、风控和推荐等场景中的结构化数据存储，提供海量数据低成本存储、毫秒级的在线数据查询和检索以及灵活的数据分析能力。 Tablestore连接器支持的信息如下。

| 类别 | 详情 |
|---|---|
| 运行模式 | 流模式 |
| API种类 | SQL |
| 支持类型 | 维表和结果表 |
| 数据格式 | 暂不支持 |
| 特有监控指标 | 维表：无结果表 numBytesOut numBytesOutPerSecond numRecordsOut numRecordsOutPerSecond currentSendTime |
| 是否支持更新或删除结果表数据 | 是 |

**前提条件**

已购买Tablestore实例并创建表。

**语法结构**

结果表实时计算（流计算）

```
CREATE TABLE ots_sink (
  name VARCHAR,
  age BIGINT,
  birthday BIGINT,
  primary key(name,age) not enforced
) WITH (
  'connector'='ots',
  'instanceName'='<yourInstanceName>',
  'tableName'='<yourTableName>',
  'accessId'='${ak_id}',
  'accessKey'='${ak_secret}',
  'endPoint'='<yourEndpoint>',
  'valueColumns'='birthday'
);
```

**说明**

Tablestore结果表必须定义有Primary Key，输出数据以Update方式追加Tablestore表。 维表

```
CREATE TABLE ots_dim (
  id int,
  len int,
  content STRING
) WITH (
  'connector'='ots',
  'endPoint'='<yourEndpoint>',
  'instanceName'='<yourInstanceName>',
  'tableName'='<yourTableName>',
  'accessId'='${ak_id}',
  'accessKey'='${ak_secret}'
);
```

**WITH参数**

通用

| 参数 | 说明 | 数据类型 | 是否必填 | 默认值 | 备注 |
|---|---|---|---|---|---|
| connector | 表类型。 | String | 是 | 无 | 固定值为 ots 。 |
| instanceNam e | 实例名。 | String | 是 | 无 | 无。 |
| endPoint | 实例访问地址。 | String | 是 | 无 | 请联系阿里云运维工程师获取。 |
| tableName | 表名。 | String | 是 | 无 | 无。 |

实时计算（流计算）

| accessId | 阿里云账号或者 RAM用户的 AccessKey ID。 | String | 是 | 无 | 无。 |
|---|---|---|---|---|---|
| accessKey | 阿里云账号或者 RAM用户的 AccessKey Secret。 | String | 是 | 无 | 无。 |
| connectTime out | 连接器连接 Tablestore的超时时间。 | Integer | 否 | 30000 | 单位为毫秒。 |
| socketTimeo ut | 连接器连接 Tablestore的 Socket超时时间。 | Integer | 否 | 30000 | 单位为毫秒。 |
| ioThreadCou nt | IO线程数量。 | Integer | 否 | 4 | 无。 |
| callbackThre adPoolSize | 回调线程池大小。 | Integer | 否 | 4 | 无。 |

结果表独有

| 参数 | 说明 | 数据类型 | 是否必填 | 默认值 | 备注 |
|---|---|---|---|---|---|
| retryIntervalMs | 重试间隔时间。 | Intege r | 否 | 1000 | 单位为毫秒。 |
| maxRetryTimes | 最大重试次数。 | Intege r | 否 | 10 | 无。 |
| valueColumns | 插入字段的列名。 | String | 是 | 无 | 多个字段以英文逗号（,）分割，例如ID或NAME。 |
| bufferSize | 流入多少条数据后开始输出。 | Intege r | 否 | 5000 | 无。 |
| batchWriteTimeo utMs | 写入超时的时间。 | Intege r | 否 | 5000 | 单位为毫秒。表示如果缓存中的数据在等待batchWriteTimeoutMs 秒后，依然没有达到输出条件，系统会自动输出缓存中的所有数据。 |

实时计算（流计算）

| batchSize | 一次批量写入的条数。 | Intege r | 否 | 100 | 最大值为200。 |
|---|---|---|---|---|---|
| ignoreDelete | 是否忽略DELETE 操作。 | Boole an | 否 | False | 无。 |
| autoIncrementKe y | 当结果表中包含主键自增列时，通过该参数指定主键自增列的列名称。 | String | 否 | 无 | 当结果表没有主键自增列时， 请不要设置此参数。 说明仅实时计算引擎VVR 8.0.4及以上版本支持该参数。 |
| overwriteMode | 数据覆盖模式。 | Enum | 否 | PUT | 支持两种模式： PUT UPDATE 分别对应数据以PUT方式和 UPDATE方式写入到 Tablestore表。 限制：动态列模式下只支持 UPDATE模式。 |
| defaultTimestam pInMillisecond | 默认时间戳。 | Long | 否 | -1 | 支持设定写入Tablestrore数据的默认时间戳。若不指定，则会写入系统当前的毫秒时间戳。 |
| dynamicColumn Sink | 是否开启动态列模式。 | Boole an | 否 | false | 动态列模式适用于在表定义中无需指定列名，根据作业运行情况动态插入数据列的场景。 建表语句中主键需要定义为前若干列，最后两列中前一列的值作为列名变量，且类型必须为String，后一列的值作为该列对应的值。 限制：动态列模式下不支持主键自增列，overwriteMode必须设置为UPDATE。 |
| checkSinkTableM eta | 是否检查结果表元数据。 | Boole an | 否 | true | 若设置为true，会检查 Tablestore表的主键列和此处的建表语句中指定的主键是否一致。 |
| enableRequestC ompression | 数据写入过程中是否开启数据压缩。 | Boole an | 否 | false | 无。 |

维表独有实时计算（流计算）

| 参数 | 说明 | 数据类型 | 是否必填 | 默认值 | 备注 |
|---|---|---|---|---|---|
| retryIntervalMs | 重试间隔时间。 | Integ er | 否 | 1000 | 单位为毫秒。 |
| maxRetryTimes | 最大重试次数。 | Integ er | 否 | 10 | 无。 |
| cache | 缓存策略。 | String | 否 | ALL | 目前Tablestore维表支持以下三种缓存策略： None：无缓存。 LRU：缓存维表里的部分数据。源表的每条数据都会触发系统先在Cache中查找数据，如果没有找到，则去物理维表中查找。 需要配置相关参数：缓存大小（cacheSize）和缓存更新时间间隔 （cacheTTLMs）。 ALL（默认值）：缓存维表里的所有数据。在Job运行前，系统会将维表中所有数据加载到Cache中，之后所有的维表查找数据都会通过 Cache进行。如果在Cache 中无法找到数据，则KEY不存在，并在Cache过期后重新加载一遍全量Cache。 适用于远程表数据量小且 MISS KEY（源表数据和维表JOIN时，ON条件无法关联）特别多的场景。需要配置相关参数：缓存更新时间间隔cacheTTLMs，更新时间黑名单cacheReloadTimeBl ackList。 说明因为系统会异步加载维表数据，所以在使用 CACHE ALL时，需要增加维表JOIN节点的内存，增加的内存大小为远程表数据量的两倍。 |
| cacheSize | 缓存大小。 | Integ er | 否 | 无 | 当缓存策略选择LRU时，可以设置缓存大小。 |

实时计算（流计算）

| cacheTTLMs | 缓存失效时间。 | Integ er | 否 | 无 | 单位为毫秒。cacheTTLMs配置和cache有关： 如果cache配置为None， 则cacheTTLMs可以不配置，表示缓存不超时。 如果cache配置为LRU，则 cacheTTLMs为缓存超时时间。默认不过期。 如果cache配置为ALL，则 cacheTTLMs为缓存加载时间。默认不重新加载。 |
|---|---|---|---|---|---|
| cacheEmpty | 是否缓存空结果。 | Boole an | 否 | 无 | true：缓存 false：不缓存 |
| cacheReloadTim eBlackList | 更新时间黑名单。 在缓存策略选择为 ALL时，启用更新时间黑名单，防止在此时间内做 Cache更新（例如双11场景）。 | String | 否 | 无 | 格式为2017-10-24 14:00 -> 2017-10-24 15:00,2017-11-10 23:30 -> 2017-11-11 08:00。分隔符的使用情况如下所示： 用英文逗号（,）来分隔多个黑名单。 用箭头（->）来分割黑名单的起始结束时间。 |
| async | 是否异步返回数据。 | Boole an | 否 | false | true：表示异步返回数据。 异步返回数据默认是无序的，可通过 asyncResultOrder参数进行配置。 false（默认值）：表示不进行异步返回数据。 |
| asyncResultOrd er | 异步返回数据时， 结果是否需要保序。 | String | 否 | unorder ed | unordered（默认值）：表示异步返回数据无序。 ordered：表示异步返回数据有序。 说明仅VVR 8.0.0及以上版本支持该参数。 |

**类型映射**

| Flink字段类型 | Tablestore字段类型 |
|---|---|

实时计算（流计算）

| BINARY | BINARY |
|---|---|
| VARBINARY |  |
| CHAR | STRING |
| VARCHAR |  |
| TINYINT | INTEGER |
| SMALLINT |  |
| INTEGER |  |
| BIGINT |  |
| FLOAT | DOUBLE |
| DOUBLE |  |
| BOOLEAN | BOOLEAN |

**使用示例**

```
CREATE TEMPORARY TABLE ots_sink (
  `order` VARCHAR,
  orderid VARCHAR,
  customerid VARCHAR,
  customername VARCHAR,
  PRIMARY KEY (`order`,orderid) NOT ENFORCED
) WITH (
  'connector'='ots',
  'endPoint'='<yourEndpoint>',
  'instanceName'='flink-sink',
  'tableName'='flink_sink_table',
  'accessId'='${ak_id}',
  'accessKey'='${ak_secret}',
  'valueColumns'='customerid,customername',
  'autoIncrementKey'='${auto_increment_primary_key_name}'
);
```

### ClickHouse

实时计算（流计算）

**背景信息**

ClickHouse是一个用于联机分析（OLAP）的列式数据库管理系统。ClickHouse连接器支持的信息如下。

| 类别 | 详情 |
|---|---|
| 支持类型 | 结果表 |
| 运行模式 | 批模式和流模式 |
| 数据格式 | 暂不适用 |
| 特有监控指标 | numRecordsOut numRecordsOutPerSecond currentSendTime |
| API种类 | SQL |
| 是否支持更新或删除结果表数据 | 当Flink结果表的DDL上指定了Primary Key，且参数 ignoreDelete设置为false 时，则支持更新或删除结果表数据，但性能会显著下降。 |

**特色功能**

**前提条件**

已配置白名单。

**使用限制**

暂不支持配置sink.parallelism参数。 仅Flink计算引擎VVR 8.0.7及以上版本支持使用balance的策略来均匀地将数据写入ClickHouse的本地表。

**语法结构**

实时计算（流计算）

```
  id INT,
  name VARCHAR,
  age BIGINT,
  rate FLOAT
) WITH (
  'connector' = 'clickhouse',
  'url' = '<yourUrl>',
  'userName' = '<yourUsername>',
  'password' = '<yourPassword>',
  'tableName' = '<yourTablename>',
  'maxRetryTimes' = '3',
  'batchSize' = '8000',
  'flushIntervalMs' = '1000'
  'ignoreDelete' = 'true',
  'shardWrite' = 'false',
  'writeMode' = 'partition',
  'shardingKey' = 'id'
);
```

**WITH参数**

| 参数 | 说明 | 数据类型 | 是否必填 | 默认值 | 备注 |
|---|---|---|---|---|---|
| connecto r | 结果表类型。 | String | 是 | 无 | 固定值为clickhouse。 |
| url | ClickHouse的JDBC 连接地址。 | String | 是 | 无 | 请联系阿里云运维工程师获取。 如果不写数据库名称，则使用默认的 default数据库。 说明如果您要将数据写入ClickHouse 分布式表，则URL为该分布式表所在节点的JDBC URL。 |
| userNam e | ClickHouse的用户名。 | String | 是 | 无 | 无。 |
| password | ClickHouse的密码。 | String | 是 | 无 | 无。 |
| tableNa me | ClickHouse的表名称。 | String | 是 | 无 | 无。 |

实时计算（流计算）

| maxRetr yTimes | 向结果表插入数据失败后的最大尝试次数。 | Int | 否 | 3 | 无。 |
|---|---|---|---|---|---|
| batchSiz e | 一次批量写入的数据条数。 | Int | 否 | 100 | 如果缓存中的数据条数达到了batchSize参数值，或者等待时间超过flushIntervalMs后，系统将会自动将缓存中的数据写入ClickHouse 表中。 |
| flushInte rvalMs | 清空缓存的时间间隔。 | Long | 否 | 1000 | 单位为毫秒。 |
| ignoreDe lete | 是否忽略Delete消息。 | Boolean | 否 | true | 参数取值如下： true（默认值）：忽略。 false：不忽略。 如果为false，并且在DDL中声明了 Primary Key，则会使用 ClickHouse的ALTER语句来删除数据。 说明如果设置 ignoreDelete=false，则无法支持以partition的方式写 ClickHouse分布表的本地表，所以就不能再设置writeMode为 partition。 |

实时计算（流计算）

| shardWri te | 对于ClickHouse分布式表，是否直接写 ClickHouse的本地表。 | Boolean | 否 | false | 参数取值如下： false（默认值）：先写 ClickHouse的分布式表，再由分布式表写入对应的本地表。此时 tableName应为分布式表的名称。 true：跳过分布式表，直接将数据写到该ClickHouse分布式表对应的本地表。 如果需要提高写ClickHouse分布式表的吞吐量，则建议将该值设置为 true。 如果您需要在URL中手动指定要将数据写到哪些节点的本地表中。此时tableName应该为本地表的名字。代码示例如下： 'url' = 'jdbc:clickhouse://192 .XX.XX.1:8123,192.XX.X X.2:8123/default' 'tableName' = 'local table' _ 如果您不需要手动指定本地表的节点，可以通过同时设置 inferLocalTable参数来让Flink 自动推测本地表的节点。此时，tableName应该为分布式表的名字，且url为该分布式表所在节点的JDBC URL。代码示例如下： 'url' = 'jdbc:clickhouse://192 .XX.XX.1:8123/default' // 分布式表所在节点的 JDBC URL 'tableName' = 'distribute table' _ |
|---|---|---|---|---|---|

实时计算（流计算）

| inferLoca lTable | 对于写ClickHouse 分布式表，是否尝试推测分布式表的本地表信息，然后直接写入本地表中。 | Boolean | 否 | false | 参数取值如下： false（默认值）：如果是写 ClickHouse分布式表，并且在参数 url中只指定了一个节点，则不会尝试推测分布式表对应的本地表信息，而是依然会直接写入分布式表，再由分布式表写入对应的本地表。 true：Flink将尝试推测分布式表的本地表信息，并直接写入对应的本地表。此时需要 shardWrite参数也同步设置为 true，tableName 设置为分布式表的名字，并且url设置为该分布式表所在节点的JDBC URL。 说明对于写ClickHouse非分布式表， 可直接忽略该参数。 |
|---|---|---|---|---|---|
| writeMod e | 对于ClickHouse分布式表，采用何种策略写ClickHouse的本地表。 | Enum | 否 | defau lt | 参数取值如下： default（默认值）：表示总是写入到第一个节点的本地表。 partition：表示将数据按key写到同一个节点的本地表。 random：表示随机写到某个节点的本地表。 balance：表示采用round-robin 的方式，均匀地将数据写入到本地表节点中。 说明如果设置了 writeMode=partition，请确保配置项ignoreDelete为true。 |
| sharding Key | 按何种key将数据写到同一个节点的本地表。 | default | 否 | 无 | 当writeMode取值为partition 时，shardingKey值必填，可包含多个字段，多个字段以英文逗号（,） 分隔。 |

实时计算（流计算）

| exactlyO nce | 是否开启 exactlyOnce语义。 | Boolean | 否 | false | 参数取值如下： true：开启。 false（默认值）：不开启。 说明目前仅支持写EMR的 ClickHouse的Exactly Once语义。所以只有当您写EMR的ClickHouse 时，才能将 exactlyOnce设置为 true。 不支持以partition策略写ClickHouse的本地表的Exactly Once语义。 所以如果exactlyOnce 设置为true， 则writeMode不能设置为partition。 |
|---|---|---|---|---|---|

**类型映射**

| Flink字段类型 | ClickHouse字段类型 |
|---|---|
| BOOLEAN | UInt8 / Boolean 说明 ClickHouse v21.12及以上版本支持Boolean类型。如果您使用的ClickHouse是v21.12 以下版本，Flink的Boolean类型则对应ClickHouse的UInt8类型。 |
| TINYINT | Int8 |
| SMALLINT | Int16 |
| INTEGER | Int32 |
| BIGINT | Int64 |
| BIGINT | UInt32 |
| FLOAT | Float32 |
| DOUBLE | Float64 |

实时计算（流计算）

| CHAR | FixedString |
|---|---|
| VARCHAR | String |
| BINARY | FixedString |
| VARBINARY | String |
| DATE | Date |
| TIMESTAMP(0) | DateTime |
| TIMESTAMP(x) | Datetime64(x) |
| DECIMAL | DECIMAL |
| ARRAY | ARRAY |
|  | Nested |

**说明**

ClickHouse暂不支持Flink的TIME、MAP、MULTISET和ROW类型。 对于ClickHouse的Nested类型，需要将其映射成Flink的ARRAY类型，例如：

```
CREATE TABLE visits (
  StartDate Date,
  Goals Nested
  (
    ID UInt32,
    OrderID String
```

)

```
  ...
);
```

需要映射为：

```
CREATE TABLE visits (
  StartDate DATE,
  `Goals.ID` ARRAY<LONG>,
  `Goals.OrderID` ARRAY<STRING>
);
```

实时计算（流计算）

**说明**

ClickHouse的DateTime类型可以精确到秒，Datetime64可以精确到纳秒。对于VVR-6.0.6之前的版本，因为ClickHouse官方提供的JDBC写Datetime64数据类型会出现精度丢失，只能精确到秒的问题，所以通过Flink只能写入秒级别的TIMESTAMP，即TIMESTAMP(0)。VVR-6.0.6及之后的版本修复了这个精度丢失问题，通过Flink可以正常写Datetime64类型的数据。

**使用示例**

```
  id INT,
  name VARCHAR,
  age BIGINT,
  rate FLOAT
) WITH (
  'connector' = 'datagen',
  'rows-per-second' = '50'
);
  id INT,
  name VARCHAR,
  age BIGINT,
  rate FLOAT
) WITH (
  'connector' = 'clickhouse',
  'url' = '<yourUrl>',
  'userName' = '<yourUsername>',
  'password' = '<yourPassword>',
  'tableName' = '<yourTablename>'
); SELECT
  id,
  name,
  age,
  rate
FROM clickhouse_source;
```

假设您已经有三个本地表，表名为local_table_test，分别在192.XX.XX.1、192.XX.XX.2和 192.XX.XX.3节点上。然后基于这三个本地表，创建了一个分布式表distributed_table_test。 实时计算（流计算） 此时，如果您希望Flink可以直接写本地表，并且可以按照某个key将相同key的数据写到同一个节点的本地表中，则DDL代码示例如下。

```
  id INT,
  name VARCHAR,
  age BIGINT,
  rate FLOAT
) WITH (
  'connector' = 'datagen',
  'rows-per-second' = '50'
);
  id INT,
  name VARCHAR,
  age BIGINT,
  rate FLOAT
) WITH (
  'connector' = 'clickhouse',
  'url' =
'jdbc:clickhouse://192.XX.XX.1:8123,192.XX.XX.2:8123,192.XX.XX.3:8123/default',
  'userName' = '<yourUsername>',
  'password' = '<yourPassword>',
  'tableName' = 'local_table_test',
  'shardWrite' = 'true',
  'writeMode' = 'partition',
  'shardingKey' = 'name'
); SELECT
  id,
  name,
  age,
  rate
FROM clickhouse_source;
```

实时计算（流计算） 此时，如果您不想手动指定本地表的节点，可以让Flink来自动推测本地表节点，DDL代码示例如下：

```
  id INT,
  name VARCHAR,
  age BIGINT,
  rate FLOAT
) WITH (
  'connector' = 'datagen',
  'rows-per-second' = '50'
);
  id INT,
  name VARCHAR,
  age BIGINT,
  rate FLOAT
) WITH (
  'connector' = 'clickhouse',
```

`'url' = 'jdbc:clickhouse://192.XX.XX.1:8123/default', --` 分布式表所在节点对应的`JDBC U` `RL`。

```
  'userName' = '<yourUsername>',
  'password' = '<yourPassword>',
```

`'tableName' = 'distributed_table_test', --`为分布式表的名字。

```
  'shardWrite' = 'true',
  'inferLocalTable' = 'true', --需设置inferLocalTable为true。
  'writeMode' = 'partition',
  'shardingKey' = 'name'
); SELECT
  id,
  name,
  age,
  rate
FROM clickhouse_source;
```

### Elasticsearch

**背景信息**

阿里云Elasticsearch兼容开源Elasticsearch的功能，以及Security、Machine Learning、Graph、APM 等商业功能，致力于数据分析、数据搜索等场景服务。为您提供企业级权限管控、安全监控告警、自动报表生成等场景服务。

| 类别 | 详情 |
|---|---|
| 支持类型 | 源表、维表和结果表 |

实时计算（流计算）

| 运行模式 | 批模式和流模式 |
|---|---|
| 数据格式 | JSON |
| 特有监控指标 | 源表 pendingRecords numRecordsIn numRecordsInPerSecond numBytesIn numBytesInPerSecond 维表：无结果表 ( VVR 6.0.6及以上 ) numRecordsOut numRecordsOutPerSecond |
| API种类 | Datastream和SQL |

**前提条件**

**使用限制**

仅支持全量Elasticsearch源表，不支持增量Elasticsearch源表。

**语法结构**

源表

```
  name STRING,
  location STRING,
  value FLOAT
) WITH (
  'connector' ='elasticsearch',
  'endPoint' = '<yourEndPoint>',
  'indexName' = '<yourIndexName>'
);
```

维表实时计算（流计算）

```
CREATE TABLE es_dim(
```

`field1 STRING, --`作为`JOIN`时的`Key`，必须为`STRING`类型。

```
  field2 FLOAT,
  field3 BIGINT,
  PRIMARY KEY (field1) NOT ENFORCED
) WITH (
  'connector' ='elasticsearch',
  'endPoint' = '<yourEndPoint>',
  'indexName' = '<yourIndexName>'
);
```

**说明**

如果指定主键，则维表JOIN时的Key（字段）有且只能有一个，且必须为Elasticsearch对应索引的文档ID。 如果不指定主键，则维表JOIN时的Key可以有一个或多个，需要为Elasticsearch对应索引的文档中的字段。 对于String类型，为了保持兼容性，默认会对表中字段名增加.keyword后缀。如果因此无法匹配到Elasticsearch中的Text字段，可以将配置项ignoreKeywordSuffix配置为true。 结果表

```
CREATE TABLE es_sink(
  user_id   STRING,
  user_name   STRING,
  uv BIGINT,
  pv BIGINT,
  PRIMARY KEY (user_id) NOT ENFORCED
) WITH (
  'connector' = 'elasticsearch-7', -- 如果是Elasticsearch 6.x版本,填写elasticsearch-6
  'hosts' = '<yourHosts>',
  'index' = '<yourIndex>'
);
```

**说明**

Elasticsearch结果表会根据是否定义了主键，确定是在upsert模式或append模式下工作。 如果定义了主键，则主键必须为文档ID，Elasticsearch结果表将在upsert模式下工作，该模式可以处理包含UPDATE和DELETE的消息。 如果未定义主键，Elasticsearch将自动生成随机的文档ID，Elasticsearch结果表将在append模式工作，该模式只能消费INSERT消息。 某些类型（例如BYTES、ROW、ARRAY和MAP等）由于没有对应的字符串表示形式，所以不允许其作为主键字段。 DDL中的字段均对应Elasticsearch文档中的字段，不支持将文档ID等Meta信息写入 Elasticsearch结果表中，因为文档ID等Meta信息由Elasticsearch实例侧维护。

**WITH参数**

源表实时计算（流计算）

| 参数 | 说明 | 数据类型 | 是否必填 | 默认值 | 备注 |
|---|---|---|---|---|---|
| connector | 源表类型。 | String | 是 | 无 | 固定值为elasticsearch。 |
| endPoint | Server地址。 | String | 是 | 无 | 请联系阿里云运维工程师获取。 |
| indexName | 索引名称。 | String | 是 | 无 | 无。 |
| accessId | Elasticsearch 实例的用户名。 | String | 否 | 无 | 默认为空，不进行权限验证。如果定义了accessId，则必须定义非空的accessKey。 |
| accessKey | Elasticsearch 实例的密码。 | String | 否 | 无 |  |
| typeNames | Type名称。 | String | 否 | doc _ | Elasticsearch 7.0以上版本不建议设置该参数。 |
| batchSize | 每个scroll请求从 Elasticsearch 集群获取的最大文档数。 | Int | 否 | 2000 | 无。 |
| keepScrollA liveSecs | scroll上下文保留的最长时间。 | Int | 否 | 3600 | 单位为秒。 |

结果表

| 参数 | 说明 | 数据类型 | 是否必填 |  | 默认值 | 备注 |
|---|---|---|---|---|---|---|
| connector | 结果表类型。 | String | 是 |  |  | 固定值为 elasticsearch- 6 、 elasticsearch- 7 或 elasticsearch-8 。 |
|  |  |  |  |  | 无 | 6 |
|  |  |  |  |  |  | 7 |
| hosts | Server地址。 | String | 是 |  | 无 | 请联系阿里云运维工程师获取。 |

|  | elasticsearch- |
|---|---|
| elasticsearch- |  |
| elasticsearch-8 |  |

实时计算（流计算）

| index | 索引名称。 | String |  |  |  |  |  | Elasticsearch结果表同时支持静态索引和动态索引。在使用静态和动态索引时， 您需要注意以下几点： 如果使用静态索引，则索引选项值应为纯字符串，例如 myusers ，所有记录都将被写入 myusers 索引。 如果使用动态索引，可以使用 {field name} 引用记录中的字 _ 段值以动态生成目标索引。您还可以使用 {field name\|date format st _ _ _ ring} 将TIMESTAMP、DATE和 TIME类型的字段值转换为 date format string 指定的 _ _ 格式。 date format string 与 _ _ Java的DateTimeFormatter兼容。例如，如果设置为 myusers- {log ts\|yyyy-MM-dd} ，则 _ log ts字段值为 2020-03-27 _ 12:25:55 的记录将被写入 myusers-2020-03-27 索引。 |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  | {field name\|date format st _ _ _ |  |  |  |
|  |  |  | ng | 是 |  | 无 |  | ring} |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  | myusers- |  |  |
|  |  |  |  |  |  |  |  | {log ts\|yyyy-MM-dd} _ |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  | ，则 |  |
| document- type | 文档类型。 | String |  | elas tics earc h- 6： 必填 elas tics earc h- 7： 不支持 |  |  |  | 当连接器类型为 elasticsearch- 6 时，此处参数取值需要和 Elasticsearch侧的type参数取值保持一致。 |  |  |  |  |
|  |  |  |  |  | las | 无 |  | 6 |  |  |  |  |
| username | 用户名。 | String |  | 否 |  | 空 |  | 默认为空，不进行权限验证。如果定义了 username，则必须定义非空的 password。 |  |  |  |  |
| password | 密码。 | String |  | 否 |  | 空 |  |  |  |  |  |  |
| document- id.key- delimiter | 文档ID的分隔符。 | String |  | 否 |  | _ |  | 在Elasticsearch结果表中，主键用于计算Elasticsearch的文档ID。 Elasticsearch结果表通过使用document-id.key-delimiter指定的键分隔符，按照DDL中定义的顺序连接所有主键字段，从而为每一行生成一个文档ID字符串。 说明文档ID为最多512个字节但不包含空格的字符串。 |  |  |  |  |

|  | _ 12:25:55 |  |
|---|---|---|

实时计算（流计算）

| failure- handler | Elasticsea rch请求失败时的故障处理策略。 | String | 否 | fail | 可选策略如下： fail（默认值）：如果请求失败，则作业失败。 ignore：忽略失败并删除请求。 retry-rejected：重新添加由于队列容量满而失败的请求。 custom class name：用于使用 ActionRequestFailureHandler子类进行故障处理。 |
|---|---|---|---|---|---|
| sink.flush- on- checkpoint | 是否在 checkpoi nt时执行 flush。 | Boolean | 否 | true | true：默认值。 false：禁用该功能后，在 Elasticsearch进行Checkpoint时， 连接器将不等待确认所有pending请求是否已完成，故连接器不会为请求提供 At-least-once保证。 |
| sink.bulk- flush.backo ff.strategy | 如果由于临时请求错误导致flush 操作失败， 则设置sink.b ulk- flush.ba ckoff.str ategy指定重试策略。 | Enum | 否 | DISABL ED | DISABLED（默认值）：不执行重试， 即第一次请求错误后失败。 CONSTANT：常量回退，即每次回退等待时间相同。 EXPONENTIAL：指数回退，即每次回退等待时间指数递增。 |
| sink.bulk- flush.backo ff.max- retries | 最大回退重试次数。 | Int | 否 | 无 | 无。 |
| sink.bulk- flush.backo ff.delay | 每次回退尝试之间的延迟。 | Duratio n | 否 | 无 | 对于CONSTANT回退策略：该值为每次重试之间的延迟。 对于EXPONENTIAL回退策略：该值为初始基准延迟。 |
| sink.bulk- flush.max- actions | 每个批量请求的最大缓冲操作数。 | Int | 否 | 1000 | 0表示禁用该功能。 |
| sink.bulk- flush.max- size | 存放请求的缓冲区内存最大值。 | String | 否 | 2 MB | 单位为MB，默认值为2 MB，0 MB表示禁用该功能。 |

实时计算（流计算）

| sink.bulk- flush.interv al | flush的间隔。 | Duratio n | 否 | 1s | 单位为秒，默认值为1s，0s表示禁用该功能。 |
|---|---|---|---|---|---|
| connection. path-prefix | 要添加到每个REST通信中的前缀字符串。 | String | 否 | 空 | 无。 |
| retry-on- conflict | 更新操作中，允许因版本冲突异常而重试的最大次数。 超过该次数后将抛出异常导致作业失败。 | Int | 否 | 0 | 该参数仅在定义了主键的情况下生效。 |
| routing- fields | 指定一个或多个ES字段名称，用来将文档路由到 ElasticSe arch的指定分片中。 | String | 否 | 无 | 多个字段名以分号（;）进行分割。如果某个字段数据为空，则该字段会被置为 null。 说明仅实时计算引擎VVR 8.0.6及以上版本，且elasticsearch-7和 elasticsearch-8支持该参数。 |

维表

| 参数 | 说明 | 数据类型 | 是否必填 | 默认值 | 备注 |
|---|---|---|---|---|---|
| connector | 维表类型。 | Stri ng | 是 | 无 | 固定值为elasticsearch。 |
| endPoint | Server地址。 | Stri ng | 是 | 无 | 请联系阿里云运维工程师获取。 |
| indexName | 索引名称。 | Stri ng | 是 | 无 | 无。 |
| accessId | Elasticsearc h实例的用户名。 | Stri ng | 否 | 无 | 默认为空，不进行权限验证。如果定义了accessId，则必须定义非空的accessKey。 |

| k存算分离版开发指南·连接器 |  |  |  |  |  |
|---|---|---|---|---|---|
|  |  |  |  |  | 实时计算（流计算） |
|  |  |  |  |  | 重要为了避免您的用户名和密码信息泄露，建议您使用变量的方式填写。 |
| accessKey | Elasticsearc h实例的密码。 | Stri ng | 否 | 无 |  |
| typeNames | Type名称。 | Stri ng | 否 | do _ c | Elasticsearch 7.0以上版本不建议设置该参数。 |
| maxJoinRo ws | 单行数据Join 的最多行数。 | Inte ger | 否 | 102 4 | 无。 |
| cache | 缓存策略。 | Stri ng | 否 | ALL | 支持以下三种缓存策略： ALL：缓存维表里的所有数据。在Job运行前， 系统会将维表中的所有数据加载到Cache中， 之后所有的维表查找数据都会通过Cache进行。如果在Cache中无法找到数据，则KEY不存在，并在Cache过期后重新加载一遍全量 Cache。 LRU：缓存维表里的部分数据。源表的每条数据都会触发系统先在Cache中查找数据。如果没有找到，则去物理维表中查找。 None：无缓存。 |
| cacheSize | 缓存大小，即缓存多少行数据。 | Lon g | 否 | 100 000 | 仅当cache选择LRU缓存策略时，cacheSize参数生效。 |
| cacheTTLM s | 缓存失效的超时时间。 | Lon g | 否 | Lon g.M AX _ VAL UE | 单位为毫秒。cacheTTLMs配置和cache配置有关： 如果cache配置为LRU，则cacheTTLMs为缓存失效的超时时间，默认不过期。 如果cache配置为ALL，则cacheTTLMs为设置缓存重新加载的间隔时间，默认不重新加载。 |
| ignoreKey wordSuffix | 是否忽略自动为String字段添加的.keyword 后缀。 | Bool ean | 否 | fals e | 为了保证兼容性，Flink将Elasticsearch中的 Text类型转换为String，并默认在String类型字段名后增加.keyword后缀。 参数取值如下： true：忽略。 如果因此无法匹配到Elasticsearch中的Text 类型字段，需要将该参数配置为true。 false：不忽略。 |

实时计算（流计算）

| cacheEmpt y | 是否缓存物理维表中查找结果为空的结果。 | Bool ean | 否 | tru e | 仅当cache选择LRU缓存策略时，cacheEmpty参数生效。 |
|---|---|---|---|---|---|

**类型映射**

Flink以JSON来解析Elasticsearch数据，详情请参见数据类型映射关系。

**使用示例**

源表示例

```
  name STRING,
  location STRING,
  `value` FLOAT
) WITH (
  'connector' ='elasticsearch',
  'endPoint' = '<yourEndPoint>',
  'accessId' = '${secret_values.ak_id}',
  'accessKey' = '${secret_values.ak_secret}',
  'indexName' = '<yourIndexName>',
  'typeNames' = '<yourTypeName>'
);
  name STRING,
  location STRING,
  `value` FLOAT
) WITH ( ); SELECT name, location, `value` FROM elasticsearch_source;
```

维表示例实时计算（流计算）

```
  id STRING,
  data STRING,
  proctime as PROCTIME()
) WITH ( ); CREATE TEMPORARY TABLE es_dim (
  id STRING,
  `value` FLOAT,
  PRIMARY KEY (id) NOT ENFORCED
) WITH (
  'connector' ='elasticsearch',
  'endPoint' = '<yourEndPoint>',
  'accessId' = '${secret_values.ak_id}',
  'accessKey' = '${secret_values.ak_secret}',
  'indexName' = '<yourIndexName>',
  'typeNames' = '<yourTypeName>'
);
  id STRING,
  data STRING,
  `value` FLOAT
) WITH ( ); SELECT e.*, w.* JOIN es_dim FOR SYSTEM_TIME AS OF e.proctime AS w ON e.id = w.id;
```

结果表示例实时计算（流计算）

```
  id STRING,
  name STRING,
  uv BIGINT
) WITH ( ); CREATE TEMPORARY TABLE es_sink (
  user_id STRING,
  user_name STRING,
  uv BIGINT,
```

`PRIMARY KEY (user_id) NOT ENFORCED --` 主键可选，如果定义了主键，则作为文档`ID`，否则文档`ID`将为随机值。

```
) WITH (
  'connector' = 'elasticsearch-6',
  'hosts' = '<yourHosts>',
  'index' = '<yourIndex>',
  'document-type' = '<yourElasticsearch.types>',
  'username' ='${secret_values.ak_id}',
  'password' ='${secret_values.ak_secret}'
); INSERT INTO es_sink SELECT id, name, uv FROM datagen_source;
```

### Upsert Kafka

**背景信息**

Upsert Kafka连接器支持以upsert方式从Kafka topic中读取数据并将数据写入Kafka topic。 作为源表，此连接器可以将Kafka中存储的数据转换为changelog流，其中每条数据记录代表一个更新或删除事件。更准确地说，数据记录中的value被解释为同一key的最后一个value的UPDATE，如果有这个 key，如果不存在相应的key，则该更新被视为INSERT。用表来类比，changelog流中的数据记录被解释为UPSERT，也称为INSERT或UPDATE，因为任何具有相同key的现有行都被覆盖。另外，value为空的消息将会被视作为DELETE消息。 作为结果表，此连接器可以消费上游计算逻辑产生的changelog流。它会将INSERT或UPDATE_AFTER 数据作为正常的Kafka消息写入，并将DELETE数据以value为空的Kafka消息写入，表示对应key的消息被删除。Flink将根据主键列的值对数据进行分区，从而保证主键上的消息有序，因此同一主键上的更新或删除消息将落在同一分区中。

| 类别 | 详情 |
|---|---|
| 支持类型 | 源表和结果表 |
| 运行模式 | 流模式 |

实时计算（流计算）

| 数据格式 | avro、avro-confluent、csv、json和raw |
|---|---|
| 特有监控指标 | 源表 numRecordsIn numRecordsInPerSecond numBytesIn numBytesInPerScond currentEmitEventTimeLag currentFetchEventTimeLag sourceIdleTime pendingRecords 结果表 numRecordsOut numRecordsOutPerSecond numBytesOut numBytesOutPerSecond currentSendTime |
| API种类 | SQL |
| 是否支持更新或删除结果表数据 | 是 |

**前提条件**

已创建Kafka集群。

**使用限制**

仅支持读取和写入Apache Kafka 0.10及以上版本的数据。 仅支持Apache Kafka 2.8版本的客户端配置项，详情请参见Apache Kafka消费者和生产者配置项文档。 Upsert Kafka结果表在使用精确一次语义时，写入的Kafka集群必须开启事务功能，且仅支持Apache Kafka 0.11及以上版本的集群。

**语法结构**

实时计算（流计算）

```
user_region STRING, pv BIGINT, uv BIGINT, PRIMARY KEY(user_region) NOT ENFORCED )WITH( 'connector'='upsert-kafka', 'topic'='<yourTopicName>', 'properties.bootstrap.servers'='...', 'key.format'='avro', 'value.format'='avro' );
```

**WITH参数**

通用

| 参数 | 说明 | 数据类型 |  | 是否必填 | 默认值 | 备注 |  |
|---|---|---|---|---|---|---|---|
| connector | 表类型。 | String |  | 是 | 无 | 固定值为upsert-kafka。 |  |
| properties.boo tstrap.servers | Kafka broker 地址。 | String |  | 是 | 无 | 请联系阿里云运维工程师获取。 |  |
| properties.* | 对Kafka客户端的直接配置。 | String |  |  |  | 后缀名必须是Kafka官方文档中定义的生产者和消费者配置。 Flink会将properties.前缀移除，并将剩余的配置传递给Kafka客户端。 例如可以通过 'properties.allow.auto.cr eate.topics' = 'false' 来禁用自动创建topic。 不能通过该方式修改以下配置，因为它们会被Kafka连接器覆盖： key.deserializer value.deserializer |  |
|  |  |  |  |  |  |  | 'properties.allow.auto.cr |
|  |  |  | tring | 否 | 无 | eate.topics' = 'false' |  |

实时计算（流计算）

| key.format | 读取或写入 Kafka消息key 部分时使用的格式。 | String | 是 | 无 | 当使用该配置时，key.fields或key.fields- prefix配置是必填的。 参数取值如下： csv json avro debezium-json canal-json maxwell-json avro-confluent raw |
|---|---|---|---|---|---|
| key.fields- prefix | 为所有Kafka消息key部分指定自定义前缀，以避免与消息 value部分格式字段重名。 | String | 否 | 无 | 该配置项仅用于源表和结果表的列名区分，解析和生成Kafka消息key部分时，该前缀会被移除。 说明使用该配置时，value.fields- include必须配置为 EXCEPT KEY。 _ |
| value.format | 读取或写入 Kafka消息 value部分时使用的格式。 | String | 是 | 无 | 该配置等同于format，因此format和value.format 只能配置其中一个，如果同时配置两个会产生冲突。 |
| value.fields- include | 在解析或生成 Kafka消息 value部分时， 是否要包含消息 key部分对应的字段。 | String | 是 | ALL | 参数取值如下： ALL（默认值）：所有列都会作为 Kafka消息value部分处理。 EXCEPT KEY：除去key.fields定 _ 义的字段，剩余字段作为Kafka消息value部分处理。 |
| topic | 读取或写入 topic名称。 | String | 是 | 无 | 无。 |

结果表

| 参数 | 说明 | 数据类型 | 是否必填 | 默认值 | 备注 |
|---|---|---|---|---|---|
| sink.parallelis m | Kafka结果表算子的并发数。 | Integer | 否 | 上游算子的并发，由框架决定 | 无。 |

实时计算（流计算）

| sink.buffer- flush.max- rows | 缓存刷新前，最多能缓存多少条记录。 | Integer | 否 |  | 0（未开启） | 当结果表收到很多同key上的更新时，缓存将保留同key的最后一条记录，因此结果表缓存能帮助减少发往 Kafka topic的数据量，以及避免发送潜在的tombstone消息。 说明如果要开启结果表缓存，需要同时设置sink.buffer- flush.max- rows和sink.buffer- flush.interval两个选项为大于零的值。 |  |  |
|---|---|---|---|---|---|---|---|---|
| sink.buffer- flush.interval | 缓存刷新的间隔时间。 | Durati on | 否 |  |  | 单位可以为毫秒（ms）、秒（s）、 分钟（min）或小时（h）。例如 'sink.buffer- flush.interval'='1 s' 。 当结果表收到很多同key上的更新时，缓存将保留同key的最后一条记录，因此结果表缓存能帮助减少发往 Kafka topic的数据量，以及避免发送潜在的tombstone消息。 说明如果要开启结果表缓存，需要同时设置sink.buffer- flush.max- rows和sink.buffer- flush.interval两个选项为大于零的值。 |  |  |
|  |  |  |  |  |  |  | 'sink.buffer- |  |
|  |  |  |  |  |  | flush.interval'='1 s' |  |  |
|  |  |  |  |  | 0（未开启） |  |  |  |

**使用示例**

源表创建Kafka数据源表，源表中包含网站用户的浏览数据。

```
CREATE TABLE pageviews( user_id BIGINT, page_id BIGINT, viewtime TIMESTAMP, user_region STRING, WATERMARK FOR viewtime AS viewtime - INTERVAL '2' SECOND )WITH( 'connector'='kafka', 'topic'='<yourTopicName>', 'properties.bootstrap.servers'='...', 'format'='json' );
```

结果表实时计算（流计算）

```
CREATE TABLE pageviews_per_region( user_region STRING, pv BIGINT, uv BIGINT, PRIMARY KEY(user_region) NOT ENFORCED )WITH( 'connector'='upsert-kafka', 'topic'='<yourTopicName>', 'properties.bootstrap.servers'='...', 'key.format'='avro', 'value.format'='avro' );
```

将统计网站用户的浏览数据写入结果表中。

```
INSERT INTO pageviews_per_region SELECT user_region, COUNT(*), COUNT(DISTINCTuser_id) FROM pageviews GROUP BY user_region;
```

### 云原生数据仓库AnalyticDB

**PostgreSQL版（ADB PG）**

本文为您介绍如何使用AnalyticDB PostgreSQL连接器。

**背景信息**

云原生数据仓库AnalyticDB PostgreSQL版是一种大规模并行处理（MPP）数据仓库服务，可提供海量数据在线分析服务。 AnalyticDB PostgreSQL版支持的信息如下。

| 类别 | 详情 |
|---|---|
| 支持类型 | 维表和结果表 |
| 运行模式 | 流模式和批模式 |
| 数据格式 | 暂不适用 |

实时计算（流计算）

| 特有监控指标 | 结果表： numRecordsOut numRecordsOutPerSecond numBytesOut numBytesOutPerSecond currentSendTime 维表：无 |
|---|---|
| API种类 | SQL |
| 是否支持更新或删除结果表数据 | 是 |

**前提条件**

已设置白名单。 已创建AnalyticDB PostgreSQL实例并创建表。

**使用限制**

暂不支持自建的PostgreSQL。 仅Flink实时计算引擎VVR 6.0.0及以上版本支持云原生数据仓库AnalyticDB PostgreSQL版连接器。 仅Flink实时计算引擎VVR 8.0.1及以上版本支持云原生数据仓库AnalyticDB PostgreSQL版7.0版本。

**语法结构**

```
CREATE TABLE adbpg_table (
 id INT,
 len INT,
 content VARCHAR，
 PRIMARY KEY(id)
) WITH (
 'connector'='adbpg',
 'url'='jdbc:postgresql://yourAddress:yourPortId/yourDatabaseName',
 'tableName'='yourDatabaseTableName',
 'userName'='yourDatabaseUserName',
 'password'='yourDatabasePassword'
);
```

**WITH参数**

| 类型 | 参数 | 说明 | 数据类型 | 是否必填 | 默认值 | 备注 |
|---|---|---|---|---|---|---|
|  | connector | 表类型。 | String | 是 | 无 | 固定值为adbpg。 |

| link存算分 | 离版开发指南·连接器实时计算（流计算） |  |  |  |  |  |
|---|---|---|---|---|---|---|
| 通用 |  |  |  |  |  |  |
|  | url | JDBC连接地址。 | String | 是 | 无 | 请联系阿里云运维工程师获取。 |
|  | tableName | 表名。 | String | 是 | 无 | 无。 |
|  | userName | 用户名。 | String | 是 | 无 | 无。 |
|  | password | 密码。 | String | 是 | 无 | 无。 |
|  | maxRetryTi mes | 写入数据失败后，重试写入的最大次数。 | Integ er | 否 | 3 | 无。 |
|  | targetSchem a | Schema名称。 | String | 否 | public | 无。 |
|  | caseSensitiv e | 大小写是否敏感。 | String | 否 | false | 参数取值如下： true：大小写敏感。 false（默认值）：大小写不敏感。 |
|  | connectionM axActive | 连接池的最大连接数。 | Integ er | 否 | 5 | 系统会自动释放与数据库服务的空闲连接。 重要此参数设置过大可能会导致服务端连接数出现异常。 |
|  | retryWaitTim e | 重试的时间间隔。 | Integ er | 否 | 100 | 单位毫秒。 |
|  | batchSize | 一次批量写入的数据条数。 | Integ er | 否 | 500 | 无。 |
|  | flushInterval Ms | 清空缓存的时间间隔。 | Integ er | 否 | 无 | 如果缓存中的数据在等待指定时间后，依然没有达到输出条件，系统会自动输出缓存中的所有数据。单位毫秒。 |
|  | writeMode | 第一次尝试写入时的写入方式。 | String | 否 | insert | 参数取值如下： insert（默认值）：直接插入， 冲突时参考conflictMode。 upsert：冲突时自动update， 只能用于有主键的表。 |

|  | 流计算） |  |  |  |  | Flink存算分离版开发指南·连接器 |
|---|---|---|---|---|---|---|
| 结果表独有 |  |  |  |  |  |  |
|  | conflictMode | 当Insert写入出现主键冲突或者唯一索引冲突时的处理策略。 | String | 否 | strict | 参数取值如下： strict（默认值）：冲突时报错。 ignore：冲突时忽略。 update：冲突时自动更新，可用于无主键表，执行效率较低。 upsert：冲突时自动更新，只能用于有主键表。 |
| 维表独有 | maxJoinRow s | 单行数据Join 的最多行数。 | Integ er | 否 | 1024 | 无。 |
|  | cache | 缓存策略。 | String | 否 | ALL | 支持以下三种缓存策略： ALL（默认值）：缓存维表里的所有数据。在Job运行前，系统会将维表中所有数据加载到 Cache中，之后所有的维表查找数据都会通过Cache进行。 如果在Cache中无法找到数据，则KEY不存在，并在 Cache过期后重新加载一遍全量Cache。 LRU：缓存维表里的部分数据。源表的每条数据都会触发系统先在Cache中查找数据。 如果没有找到，则去物理维表中查找。 None：无缓存。 |
|  | cacheSize | 缓存大小，即缓存多少行数据。 | Long | 否 | 1000 00 | 仅当选择LRU缓存策略时，cacheSize参数生效。 |

实时计算（流计算）

|  | cacheTTLMs | 缓存失效的超时时间。 | Long | 否 | Long. MAX _ VALU E | cacheTTLMs配置和cache配置有关： 如果cache配置为LRU， 则cacheTTLMs为缓存失效的超时时间。默认不过期。 如果cache配置为ALL， 则cacheTTLMs为设置缓存重新加载的间隔时间，默认不重新加载。 单位为毫秒。 |
|---|---|---|---|---|---|---|

**类型映射**

| 云原生数据仓库AnalyticDB PostgreSQL版字段类型 | Flink字段类型 |
|---|---|
| boolean | boolean |
| smallint | int |
| int | int |
| bigint | bigint |
| float | double |
| varchar | varchar |
| text | varchar |
| timestamp | timestamp |
| date | date |

**使用示例**

结果表实时计算（流计算）

```
 `name` VARCHAR,
 `age` INT
```

)

```
WITH ( ); CREATE TEMPORARY TABLE adbpg_sink (
 name VARCHAR,
 age INT
) WITH (
 'connector'='adbpg',
 'url'='jdbc:postgresql://yourAddress:yourPortId/yourDatabaseName',
 'tableName'='yourDatabaseTableName',
 'userName'='yourDatabaseUserName',
 'password'='yourDatabasePassword'
); INSERT INTO adbpg_sink SELECT * FROM datagen_source;
```

维表实时计算（流计算）

```
 a INT,
 b BIGINT,
 c STRING,
 `proctime` AS PROCTIME()
```

)

```
WITH ( }; CREATE TEMPORARY TABLE adbpg_dim (
 a INT,
 b VARCHAR,
 c VARCHAR
) WITH (
 'connector'='adbpg',
 'url'='jdbc:postgresql://yourAddress:yourPortId/yourDatabaseName',
 'tableName'='yourDatabaseTableName',
 'userName'='yourDatabaseUserName',
 'password'='yourDatabasePassword'
);
 a INT,
 b STRING
```

)

```
WITH ( ); FROM datagen_source AS T JOIN adb_dim FOR SYSTEM_TIME AS OF T.proctime AS H ON T.a = H.a;
```

### 云原生数据仓库AnalyticDB

**MySQL版（ADB）3.0**

**背景信息**

云原生数据仓库AnalyticDB MySQL版3.0是融合数据库、大数据技术于一体的云原生企业级数据仓库服务。AnalyticDB MySQL版支持高吞吐的数据实时增删改、低延时的实时分析和复杂ETL，兼容上下游生态工具，可用于构建企业级报表系统、数据仓库和数据服务引擎。

| 类别 | 详情 |
|---|---|

实时计算（流计算）

| 支持类型 | 维表和结果表 |
|---|---|
| 运行模式 | 流模式和批模式 |
| 数据格式 | 暂不适用 |
| 特有监控指标 | 暂无 |
| API种类 | SQL |
| 是否支持更新或删除结果表数据 | 是 |

**前提条件**

已设置白名单。

**语法结构**

```
CREATE TEMPORARY TABLE adb_table (
  `id` INT,
  `num` BIGINT,
  PRIMARY KEY (`id`) NOT ENFORCED
) WITH (
  'connector' = 'adb3.0',
  'url' = '<yourUrl>',
  'userName' = '<yourUsername>',
  'password' = '<yourPassword>',
  'tableName' = '<yourTablename>'
);
```

**重要**

**Flink DDL中定义的主键必须和AnalyticDB MySQL数据库物理表中的主键保持一致，主键一致包**

**括是否存在主键和主键名称一致。如果不一致，会影响数据正确性。**

**WITH参数**

通用

| 参数 | 说明 | 数据类型 | 是否必填 | 默认值 | 备注 |
|---|---|---|---|---|---|
| connector | 结果表类型。 | String | 是 | 无 | 固定值为adb3.0。 |

实时计算（流计算）

| url | JDBC连接地址。 | String | 是 | 无 | 请联系阿里云运维工程师获取。 |
|---|---|---|---|---|---|
| userName | 用户名。 | String | 是 | 无 | 无。 |
| password | 密码。 | String | 是 | 无 | 无。 |
| tableName | 表名。 | String | 是 | 无 | 无。 |
| maxRetryTi mes | 写入或读取数据失败后，重试的最大次数。 | Integer | 否 | 10 | 无。 |

结果表独有

| 参数 | 说明 | 数据类型 | 是否必填 | 默认值 | 备注 |
|---|---|---|---|---|---|
| batch Size | 一次批量写入的条数。 | Integ er | 否 | 1000 | 需指定主键后，该参数才生效。 |
| buffer Size | 内存中缓存的数据条数。batch Size或buf ferSize任一到达阈值都会触发写入。 | Integ er | 否 | 1000 | 需指定主键后，该参数才生效。 |
| flushI nterv alMs | 清空缓存的时间间隔。 表示如果缓存中的数据在等待指定时间后，依然没有达到输出条件， 系统会自动输出缓存中的所有数据。 | Integ er | 否 | 3000 | 单位为毫秒。 |
| ignor eDele te | 是否忽略 Delete操作。 | Boole an | 否 | false | 参数取值如下： true：忽略Delete操作。 false：接受Delete操作。 |

实时计算（流计算）

| replac eMod e | DDL中定义了主键的情况下，是否采用 replace into语法插入数据。 |  | Boole an |  |  |  |  | 该参数取值如下： true：采用 replace into 语法插入数据。 false：采用 insert into on duplicate key update 语法插入数据。 说明仅AnalyticDB MySQL 3.1.3.5及以上版本支持该参数。 此参数仅在DDL中定义了主键时才生效，插入数据时采用的语法详情如下： DDL中定义了主键且 replaceMode=true，采用 replace into 语法插入数据。 DDL中定义了主键且 replaceMode=false，采用 insert into on duplicate key update 语法插入数据。 DDL中没有定义主键，采用 insert into 语法插入数据。 |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  |  | replace into |  |  |  |
|  |  |  |  |  |  |  |  |  |  | insert into on duplicate |  |  |  |
|  |  |  |  |  |  |  |  | key update |  |  |  |  |  |
|  |  |  |  |  | 否 |  | true |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  | 说明仅AnalyticDB MySQL 3.1.3.5及以上版本支持该参数。 此参数仅在DDL中定义了主键时才生效，插入数据时采用的语法详情如下： DDL中定义了主键且 replaceMode=true，采用 replace into 语法插入数据。 DDL中定义了主键且 replaceMode=false，采用 insert into on duplicate key update 语法插入数据。 DDL中没有定义主键，采用 insert into 语法插入数据。 |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  | insert into on |  |  |
|  |  |  |  |  |  |  |  |  | duplicate key |  |  |  |  |
|  |  |  |  |  |  |  |  |  | update |  |  |  |  |
| exclu deUp dateC olumn s | 表示更新主键值相同的数据时，忽略指定字段的更新。 |  |  |  |  |  |  | 如果忽略指定的字段为多个时，则需要使用英文逗号 （,）分割。例如 excludeUpdateColumns=column1,column2 。 说明仅在replaceMode=false时，该参数才生效。在replaceMode=true时，对应字段会被更新为null。 要忽略的多个字段需要写在一行中，不能换行。 |  |  |  |  |  |
|  |  |  | String |  | 否 |  | 空字符串 |  |  |  |  |  |  |
| conne ction MaxA ctive | 线程池大小。 |  | Integ er |  | 否 |  | 40 | 无。 |  |  |  |  |  |

维表独有

| 参数 | 说明 | 数据类型 | 是否必填 | 默认值 | 备注 |
|---|---|---|---|---|---|

实时计算（流计算）

| cache | 缓存策略。 | String | 否 | ALL | 云原生数据仓库AnalyticDB MySQL版3.0维表支持以下三种缓存策略： None：无缓存。 LRU：缓存维表里的部分数据。源表的每条数据都会触发系统先在Cache中查找数据，如果没有找到，则去物理维表中查找。 ALL（默认值）：缓存维表里的所有数据。在Job运行前，系统会将维表中所有数据加载到Cache中， 之后所有的维表查找数据都会通过Cache进行。如果在Cache中无法找到数据，则KEY不存在，并在 Cache过期后重新加载一遍全量Cache。 适用于远程表数据量小且MISS KEY在源表数据和维表JOIN时，ON条件无法关联特别多的场景。 说明如果使用CACHE ALL时，请注意节点内存大小，防止出现OOM。 因为系统会异步加载维表数据，所以在使用CACHE ALL时，需要增加维表 JOIN节点的内存，增加的内存大小为远程表数据量的两倍。 |
|---|---|---|---|---|---|
| cacheSi ze | 缓存大小，即缓存多少行数据。 | Integ er | 否 | 100000 | cacheSize配置和cache为LRU有关。当cache配置为LRU时，必须配置cacheSize参数。 |
| cacheT TLMs | 缓存超时时间，单位为毫秒。 | Integ er | 否 | Long.M AX VAL _ UE | cacheTTLMs配置和cache配置为LRU或ALL有关： 如果cache配置为LRU，则cacheTTLMs为缓存失效的超时时间。默认值为 Long.MAX VALUE ，即代表缓存不过期。 _ 如果cache配置为ALL，则cacheTTLMs为物理表数据被重新加载的间隔时间。默认值为 Long.MAX VALUE ，即代表不重新加载物理 _ 表数据。 说明如果cache配置为None，则cacheTTLMs不用配置。因为cache配置为None，表示没有缓存，因此不用配置缓存超时时间。 |
| maxJoin Rows | 主表中每一条数据查询维表时，匹配后最多返回的结果数。 | Integ er | 否 | 1024 | 如果您可以预估一条数据对应的维表数据最多为n 条，则可以设置maxJoinRows='n'，以确保实时计算匹配处理效率。 说明进行Join时，主表输入一条数据，对应维表匹配后返回的结果总数受该参数限制。 |

实时计算（流计算）

**类型映射**

| 云原生数据仓库AnalyticDB MySQL版3.0字段类型 | Flink字段类型 |
|---|---|
| BOOLEAN | BOOLEAN |
| TINYINT | TINYINT |
| SMALLINT | SMALLINT |
| INT | INT |
| BIGINT | BIGINT |
| FLOAT | FLOAT |
| DOUBLE | DOUBLE |
| DECIMAL(p, s) 或NUMERIC(p, s) | DECIMAL(p, s) |
| VARCHAR | STRING |
| BINARY | BYTES |
| DATE | DATE |
| TIME | TIME |
| DATETIME | TIMESTAMP |
| TIMESTAMP | TIMESTAMP |
| POINT | STRING |

**使用示例**

结果表实时计算（流计算）

```
  `name` VARCHAR,
  `age` INT
) WITH ( ); CREATE TEMPORARY TABLE adb_sink (
  `name` VARCHAR,
  `age` INT
) WITH (
  'connector' = 'adb3.0',
  'url' = '<yourUrl>',
  'userName' = '<yourUsername>',
  'password' = '<yourPassword>',
  'tableName' = '<yourTablename>'
); INSERT INTO adb_sink SELECT * FROM datagen_source;
```

维表

```
  `a` INT,
  `b` VARCHAR,
  `c` STRING,
  `proctime` AS PROCTIME()
) WITH ( ); CREATE TEMPORARY TABLE adb_dim (
  `a` INT,
  `b` VARCHAR,
  `c` VARCHAR
) WITH (
  'connector' = 'adb3.0',
  'url' = '<yourUrl>',
  'userName' = '<yourUsername>',
  'password' = '<yourPassword>',
  'tableName' = '<yourTablename>'
);
  `a` INT,
  `b` VARCHAR
) WITH ( ); FROM datagen_source AS T JOIN adb_dim FOR SYSTEM_TIME AS OF T.proctime AS H ON T.a = H.a;
```

实时计算（流计算）

### 云数据库HBase

**背景信息**

云数据库HBase是低成本、高扩展、云智能的大数据NoSQL，兼容标准HBase访问协议，提供低成本存储、高扩展吞吐、智能数据处理等核心优势，是为淘宝推荐、花呗风控、广告投放、监控大屏、菜鸟物流轨迹、支付宝账单、手淘消息等众多阿里巴巴核心服务提供支撑的数据库，具备PB规模、高并发、秒级伸缩、 毫秒响应、跨机房高可用、全托管、全球分布等企业能力。 HBase连接器支持的信息如下：

| 类别 | 详情 |
|---|---|
| 支持类型 | 维表和结果表 |
| 运行模式 | 流模式 |
| 数据格式 | 暂不支持 |
| 特有监控指标 | 维表支持的监控指标：无。 结果表支持的监控指标：numBytesOut、numBytesOutPerSecond、 numRecordsOut、numRecordsOutPerSecond、currentSendTime。 |
| API种类 | SQL |
| 是否支持更新或删除结果表数据 | 是 |

**前提条件**

已设置白名单。 已购买HBase集群并创建表。

**注意事项**

**语法结构**

实时计算（流计算）

```
CREATE TABLE hbase_table(
  rowkey INT,
  family1 ROW<q1 INT>,
  family2 ROW<q2 STRING, q3 BIGINT>,
  family3 ROW<q4 DOUBLE, q5 BOOLEAN, q6 STRING>
) WITH (
  'connector'='cloudhbase',
  'table-name'='<yourTableName>',
  'zookeeper.quorum'='<yourZookeeperQuorum>'
);
```

HBase的列族（Column Family）必须声明为ROW类型，列族名即该ROW的字段名。例如，DDL定义中声明了family1、family2和family3三个列族。 HBase列族中的列（Column）与对应ROW中嵌套的每个字段对应，列名即字段名。例如，DDL定义中列族family2声明了q2和q3两列。 除了类型为ROW的字段外，只能有一个原始类型（Atomic Type）的字段（例如STRING或BIGINT）， 该字段将被视作HBase的行键（Row Key），例如DDL定义中的Rowkey。 必须将HBase的行键定义为结果表的主键（Primary Key），如果没有显示定义主键，默认使用行键作为主键。 结果表中不需要将HBase表的所有列族和列都进行声明，只声明需要的即可。

**WITH参数**

通用

| 参数 | 说明 | 数据类型 | 是否必填 | 默认值 | 备注 |
|---|---|---|---|---|---|
| connector | 表类型。 | Strin g | 是 | 无 | 固定值为 cloudhbase 。 |
| table- name | HBase表名。 | Strin g | 是 | 无 | 无。 |
| zookeeper .znode.qu orum | HBase的zookeeper住址。 | Strin g | 是 | 无 | 无。 |
| zookeeper .znode.par ent | HBase在zookeeper中的根目录。 | Strin g | 否 | /hbase | 仅在HBase标准版中生效。 |
| userName | 用户名。 | Strin g | 否 | 无 | 仅在HBase增强版中生效。 |
| password | 密码。 | Strin g | 否 | 无 | 仅在HBase增强版中生效。 |

实时计算（流计算）

| haclient.cl uster.id | HBase高可用实例ID。 |  | Strin g | 否 | 无 | 只有访问同城主备实例时才需要配置仅在HBase增强版中生效。 |
|---|---|---|---|---|---|---|
| retires.nu mber | HBase客户端的重试次数。 |  | Inte ger | 否 | 31 | 无。 |
| null-string- literal | HBase字段类型为字符串时，如果Flink字段数据为 null，则将该字段赋值为 null-string- literal ，并写入 HBase。 |  | Strin g | 否 | null | 无。 |
|  |  | null-string- |  |  |  |  |
|  | literal |  |  |  |  |  |

结果表独有

| 参数 | 说明 | 数据类型 | 是否必填 | 默认值 | 备注 |
|---|---|---|---|---|---|
| sink.buffer- flush.max- size | 写入HBase前，内存中缓存的数据量（字节）大小。调大该值有利于提高HBase写入性能，但会增加写入延迟和内存使用。 | Strin g | 否 | 2MB | 支持字节单位B、KB、MB和 GB，不区分大小写。设置为0 表示不进行缓存。 |
| sink.buffer- flush.max- rows | 写入HBase前，内存中缓存的数据条数。调大该值有利于提高HBase写入性能，但会增加写入延迟和内存使用。 | Integ er | 否 | 1000 | 设置为0表示不进行缓存。 |
| sink.buffer- flush.interv al | 将缓存数据周期性写入到 HBase的间隔，可以控制写入 HBase的延迟。 | Durat ion | 否 | 1s | 支持时间单位ms、s、min、h 和d。设置为0表示关闭定期写入。 |
| dynamic.ta ble | 是否使用支持动态列的HBase 表。 | Boole an | 否 | false | 参数取值如下： true：使用支持动态列的 HBase表。 false：不使用支持动态列的 HBase表。 |
| sink.ignore- delete | 是否忽略撤回消息。 | Boole an | 否 | false | 参数取值如下： true：忽略撤回消息。 false：不忽略撤回消息。 |

实时计算（流计算）

| sink.sync- write | 是否同步写入HBase。 | Boole an | 否 | true | 参数取值如下： true：同步写，保证顺序， 会牺牲一定性能。 false：异步写，不保证顺序，性能更好。 |
|---|---|---|---|---|---|
| sink.buffer- flush.batch- rows | 同步写入HBase时内存中缓存的数据条数，调大该值有利于提高HBase写入性能，但会增加写入延迟和内存使用。 | Integ er | 否 | 100 | 仅当sink.sync-write为true 时生效。 |

维表独有

| 参数 | 说明 | 数据类型 | 是否必填 | 默认值 | 备注 |
|---|---|---|---|---|---|
| cache | 缓存策略。 | Strin g | 否 | ALL | 目前云数据库HBase版维表支持以下三种缓存策略： None：无缓存。 LRU：缓存维表里的部分数据。源表的每条数据都会触发系统先在Cache中查找数据，如果没有找到，则去物理维表中查找。 说明需要配置相关参数：缓存大小 （cacheSize）和缓存更新时间间隔 （cacheTTLMs）。 ALL（默认值）：缓存维表里的所有数据。在 Job运行前，系统会将维表中所有数据加载到 Cache中，之后所有的维表查找数据都会通过 Cache进行。如果在Cache中无法找到数据， 则KEY不存在，并在Cache过期后重新加载一遍全量Cache。 说明适用于远程表数据量小且MISS KEY（源表数据和维表JOIN时，ON条件无法关联）特别多的场景。需要配置相关参数：缓存更新时间间隔cacheTTLMs，更新时间黑名单cacheReloadTimeBlackList。 因为系统会异步加载维表数据，所以在使用 CACHE ALL时，需要增加维表JOIN节点的内存， 增加的内存大小为远程表数据量的两倍。 |
| cache Size | 缓存大小。 | Long | 否 | 1000 0 | 当缓存策略选择LRU时，可以设置缓存大小。 |

实时计算（流计算）

| cache TTLM s | 缓存失效时间， 单位为毫秒。 | Long | 否 | 无 | cacheTTLMs配置和cache有关： 如果cache配置为None，则cacheTTLMs可以不配置，表示缓存不超时。 如果cache配置为LRU，则cacheTTLMs为缓存超时时间。默认不过期。 如果cache配置为ALL，则cacheTTLMs为缓存加载时间。默认不重新加载。 |
|---|---|---|---|---|---|
| cache Empt y | 是否缓存空结果。 | Boole an | 否 | true | 无。 |
| cache Reloa dTim eBlac kList | 更新时间黑名单。在缓存策略选择为ALL时，启用更新时间黑名单，防止在此时间内做Cache更新（例如双11场景）。 | Strin g | 否 | 无 | 格式为2017-10-24 14:00 -> 2017-10-24 15:00,2017-11-10 23:30 -> 2017-11-11 08:00。分隔符的使用情况如下所示： 用英文逗号（,）来分隔多个黑名单。 用箭头（->）来分割黑名单的起始结束时间。 |
| cache Scan Limit | 读取全量HBase 数据，RPC（Rem ote Procedure Call Protocol） 服务端一次返回给客户端的行数。 | Integ er | 否 | 100 | 缓存策略选择ALL时启用。 |

**类型映射**

Flink中的数据类型在HBase中通过 `org.apache.hadoop.hbase.util.Bytes` 转换成字节数组，解码过程有以下两种情况： 对于Flink的非字符串类型，如果HBase中的值为空字节数组，则解码为null。 对于Flink的字符串类型，如果HBase中的值为 `null-string-literal` 字节数组，则解码为null。

| Flink SQL类型 | 写入Bytes时CloudHBase转换函数 | 从CloudHBase读取Bytes的转换函数 |
|---|---|---|
| CHAR | byte[] toBytes(String s) | String toString(byte[] b) |
| VARCHAR |  |  |
| STRING |  |  |
| BOOLEAN | byte[] toBytes(boolean b) | boolean toBoolean(byte[] b) |

实时计算（流计算）

|  | BINARY | byte[] |  |  | byte[] |  |  |
|---|---|---|---|---|---|---|---|
|  | VARBINARY |  |  |  |  |  |  |
|  | DECIMAL | byte[] toBytes(BigDecimal v) |  |  | BigDecimal toBigDecimal(byte[] b) |  |  |
|  | TINYINT | new byte[] { val } |  |  | bytes[0] |  |  |
|  | SMALLINT | byte[] toBytes(short val) |  |  | short toShort(byte[] bytes) |  |  |
|  | INT | byte[] toBytes(int val) |  |  | int toInt(byte[] bytes) |  |  |
|  | BIGINT | byte[] toBytes(long val) |  |  | long toLong(byte[] bytes) |  |  |
|  | FLOAT | byte[] toBytes(float val) |  |  | float toFloat(byte[] bytes) |  |  |
|  | DOUBLE | byte[] toBytes(double val) |  |  | double toDouble(byte[] bytes) |  |  |
|  | DATE | 将日期转换成自1970.01.01以来的天数，用 int表示，并通过 byte[] toBytes(int val) 转换成字节数组。 |  |  | HBase字节数组通过 int toInt(byte[] bytes) 转换成int，表示自1970.01.01以来的天数。 |  |  |
|  |  | val) |  |  |  |  |  |
|  | TIME | 将时间转换成自00:00:00以来的毫秒数，用 int表示，并通过 byte[] toBytes(int val) 转换成字节数组。 |  |  | HBase字节数组通过 int toInt(byte[] bytes) 转换成int，表示自00:00:00以来的毫秒数。 |  |  |
|  |  | val) |  |  |  |  |  |
|  | TIMESTAMP | 将时间戳转换成自1970-01-01 00:00:00以来的毫秒数，用long表示，并通过 byte[] toBytes(long val) 转换成字节数组。 |  |  | HBase字节数组通过 long toLong(byte[] bytes) ，表示自 1970-01-01 00:00:00以来的毫秒数。 |  |  |
|  |  |  |  |  |  | long |  |
|  |  |  | byt | e[] | toLong(byte[] b |  |  |
|  |  |  |  |  |  | ytes) |  |

| int toInt(byte[] |  |
|---|---|

| byte[ | ] toBytes(int | by | tes) |
|---|---|---|---|

| int toInt(byte[] |  |
|---|---|

| byte[ | ] toBytes(int | by | tes) |
|---|---|---|---|

|  | toBytes(long val) |
|---|---|

**代码示例**

维表示例。 实时计算（流计算）

```
  a INT,
  b BIGINT,
  c STRING,
  `proc_time` AS PROCTIME()
) WITH ( ); CREATE TEMPORARY TABLE hbase_dim (
  rowkey INT,
  family1 ROW<col1 INT>,
  family2 ROW<col1 STRING, col2 BIGINT>,
  family3 ROW<col1 DOUBLE, col2 BOOLEAN, col3 STRING>
) WITH (
  'connector' = 'cloudhbase',
  'table-name' = '<yourTableName>',
  'zookeeper.quorum' = '<yourZookeeperQuorum>'
);
  a INT,
  f1c1 INT,
  f3c3 STRING
) WITH ( );
     SELECT a, family1.col1 as f1c1,  family3.col3 as f3c3 FROM datagen_source
JOIN hbase_dim FOR SYSTEM_TIME AS OF datagen_source.`proc_time` as h ON datagen_source.a = h.rowkey;
```

结果表示例。 实时计算（流计算）

```
  rowkey INT,
  f1q1 INT,
  f2q1 STRING,
  f2q2 BIGINT,
  f3q1 DOUBLE,
  f3q2 BOOLEAN,
  f3q3 STRING
) WITH ( ); CREATE TEMPORARY TABLE hbase_sink (
  rowkey INT,
  family1 ROW<q1 INT>,
  family2 ROW<q1 STRING, q2 BIGINT>,
  family3 ROW<q1 DOUBLE, q2 BOOLEAN, q3 STRING>,
  PRIMARY KEY (rowkey) NOT ENFORCED
) WITH (
  'connector'='cloudhbase',
  'table-name'='<yourTableName>',
  'zookeeper.quorum'='<yourZookeeperQuorum>'
); INSERT INTO hbase_sink SELECT rowkey, ROW(f1q1), ROW(f2q1, f2q2), ROW(f3q1, f3q2, f3q3) FROM datagen_source;
```

结果动态表示例。

```
  id INT,
  f1hour STRING,
  f1deal BIGINT,
  f2day STRING,
  f2deal BIGINT
) WITH ( ); CREATE TEMPORARY TABLE hbase_sink (
  rowkey INT,
  f1 ROW<`hour` STRING, deal BIGINT>,
  f2 ROW<`day` STRING, deal BIGINT>
) WITH (
  'connector'='cloudhbase',
  'table-name'='<yourTableName>',
  'zookeeper.quorum'='<yourZookeeperQuorum>',
  'dynamic.table'='true'
); INSERT INTO hbase_sink SELECT id, ROW(f1hour, f1deal), ROW(f2day, f2deal) FROM datagen_source;
```

当**dynamic.table**参数值为true时，表示使用支持动态列的HBase表。 实时计算（流计算） 每个列族对应的ROW中必须声明两个字段：第1个字段的值表示动态列，第2个字段的值表示动态列的值。 如果datagen_source表存在一条数据，代表ID为1的商品，在10:00-11:00点之间的成交额是100， 在2020年7月26日当天的成交额是10000，则HBase中将插入行键为1的行，其中**f1:10**为 100，**f2:2020-7-26**为10000。

### 云原生多模数据库Lindorm

**背景信息**

Lindorm是面向物联网、互联网、车联网等设计和优化的云原生多模超融合数据库，是日志、监控、账单、 广告、社交、出行、风控等场景首选数据库，也是为阿里巴巴核心业务提供支撑的数据库之一。 具备以下特性： 支持宽表、时序、文本、对象、流、空间等多种数据的统一访问和融合处理。 兼容SQL、HBase/Cassandra/S3、TSDB、HDFS、Solr、Kafka等多种标准接口和无缝集成三方生态工具。 Lindorm连接器支持的信息如下。

| 类别 | 详情 |
|---|---|
| 支持类型 | 维表和结果表 |
| 运行模式 | 仅支持流模式 |
| 数据格式 | 暂不适用 |
| 特有监控指标 | 维表：无结果表： numBytesOut numBytesOutPerSecond numRecordsOut numRecordsOutPerSecond |
| API种类 | SQL |
| 支持的Lindorm引擎 | 宽表引擎 |
| 是否支持更新或删除结果表数据 | 是 |

**前提条件**

已经创建了Lindorm宽表引擎以及数据表。 实时计算（流计算） Lindorm集群与Flink集群处于网络连通的环境下，例如在同一个VPC下。

**语法结构**

```
CREATE TABLE white_list ( id varchar, name varchar, age int, PRIMARY KEY (id) NOT ENFORCED ) WITH ( 'connector' = 'lindorm', 'seedserver' = '<yourSeedServer>', 'namespace' = '<yourNamespace>', 'username' = '<yourUsername>', 'password' = '<yourPassword>', 'tableName' = '<yourTableName>', 'columnFamily' = '<yourColumnFamily>' );
```

**WITH参数**

| 类型 | 参数 | 说明 | 数据类型 | 是否必填 | 默认值 | 备注 |
|---|---|---|---|---|---|---|
| 通用 | connecto r | 表类型。 | Strin g | 是 | 无 | 固定值为lindorm。 |
|  | seedserv er | Lindorm服务器的连接地址。 | Strin g | 是 | 无 | 请联系阿里云运维工程师获取。 |
|  | namespa ce | Lindorm的命名空间。 | Strin g | 是 | 无 | 无。 |
|  | usernam e | 连接Lindorm所用到的用户名。 | Strin g | 是 | 无 | 无。 |
|  | passwor d | 连接Lindorm所用到的密码。 | Strin g | 是 | 无 | 无。 |
|  | tableNa me | Lindorm表名。 | Strin g | 是 | 无 | 无。 |
|  | columnF amily | Lindorm表的列族名。 | Strin g | 是 | 无 | 如果创建Lindorm表时未指定列族名，则填写默认列族名f。 |
|  | retryInte rvalMs | 读取或写入失败时，再次重试读取的时间间隔。 | Integ er | 否 | 1000 | 单位为毫秒。 |
| 05 | > 文档版本：2026073 |  |  |  |  |  |

实时计算（流计算）

|  | maxRetr yTimes | 最大尝试次数。 | Integ er | 否 | 5 | 无。 |
|---|---|---|---|---|---|---|
| 结果表独有 | bufferSiz e | 一次批量写入数据的条数。 | Integ er | 否 | 500 | 无。 |
|  | flushInte rvalMs | 当数据量比较少时，多长时间写入一次。 | Integ er | 否 | 2000 | 单位为毫秒。 |
|  | ignoreDe lete | 是否忽略Delete 操作。 | Bool ean | 否 | false | 参数取值如下： true：忽略。 false（默认）：不忽略。 |
|  | dynamic ColumnS ink | 是否开启动态表模式。 | Bool ean | 否 | false | 参数取值如下： true：开启动态表模式。 false（默认）：不开启动态表模式。 说明实时计算引擎VVR 6.0.2及以上版本支持该参数。 |
| 维表独有 | partition edJoin | 是否额外使用 JoinKey进行分区。 | Bool ean | 否 | false | 参数取值如下： true：用JoinKey进行分区，将数据分发到Join节点，提高缓存命中率。 false（默认值）：不使用JoinKey 进行分区。 |
|  | shuffleE mptyKey | 遇到空Key时， 是否将Key为空的记录随机向下游Shuffle。 | Bool ean | 否 | false | 参数取值如下： true：随机往下游做Shuffle。 false（默认值）：从下游中编号为 0的并发开始做Shuffle，即从第一个并发开始。 |
|  | cache | 缓存策略。 | Strin g | 否 | None | 目前Lindorm支持以下两种缓存策略： None（默认值）：无缓存。 LRU：只保留最近使用的数据。 需要配置相关参数：缓存大小 （cacheSize）和缓存失效超时时间 （cacheTTLMs）。 |

实时计算（流计算）

|  | cacheSiz e | 缓存数据的行数。 | Integ er | 否 | 1000 | 当选择LRU缓存策略后，使用本参数可以设置缓存大小。 |
|---|---|---|---|---|---|---|
|  | cacheTT LMs | 缓存失效超时时间。 | Integ er | 否 | 无 | 单位为毫秒。当选择LRU缓存策略后，可以设置缓存失效的超时时间， 默认不过期。 |
|  | cacheEm pty | 是否缓存join结果为空的数据。 | Bool ean | 否 | true | 无。 |
|  | async | 是否异步返回数据。 | Bool ean | 否 | false | 参数取值如下： true：表示异步返回数据。 false（默认值）：表示不进行异步返回数据。 |
|  | asyncLin dormRpc Timeout Ms | 在异步请求数据时的超时时间。 | Integ er | 否 | 3000 00 | 单位毫秒。 |

**动态表模式**

动态表模式适用于在表定义中并未指定列名的情况，根据作业运行情况动态创建数据列并插入的场景。例如统计每天每小时的交易量，以天作为主键，小时作为列，每个小时的数据都是动态生成的，示例如下。

| 主键 | 列名：0点 | 列名：1点 |
|---|---|---|
| 2025-06-01 | 45 | 32 |
| 2025-06-02 | 76 | 34 |

动态表需要遵循特殊的DDL定义。其主键需要定义为前若干列，最后两列中前一列的值作为列名变量，最后一列的值作为该列对应的值，且要求最后两列的类型均为varchar。代码示例如下。 实时计算（流计算）

```
CREATE TABLE lindorm_dynamic_output( pk1varchar, pk2varchar, pk3varchar, c1varchar, c2varchar, PRIMARYKEY(pk1,pk2,pk3)notenforced ) WITH ( 'connector' = 'lindorm', 'seedserver' = '<yourSeedServer>', 'namespace' = '<yourNamespace>', 'username' = '<yourUsername>', 'password' = '<yourPassword>', 'tableName' = '<yourTableName>', 'columnFamily' = '<yourColumnFamily>' );
```

上述定义中，pk1、pk2、pk3为主键，c1、c2为动态表模式所必须的两列且一定为最后两列，不可存在其他的非主键的列。每次写入数据时，会在主键<pk1, pk2, pk3>对应的条目中添加或更改一列，列名为c1 的值，该列的值为c2的值。每次一条数据来临时，只会添加或更改一列对应的值，其他列的值不会改变。

**类型映射**

Lindorm中数据均为二进制形式，通过Flink某个字段类型来转换或解析二进制的Bytes方法如下。

| Flink SQL 类型 | 转换为写入的Bytes使用的方法 | 从Lindorm读取Bytes之后的解析 |
|---|---|---|
| CHAR | org.apache.flink.table.data.StringD ata::toBytes | org.apache.flink.table.data.StringData::fromByte s |
| VARCHAR |  |  |
| BOOLEAN | com.alibaba.lindorm.client.core.util s.Bytes::toBytes(boolean) | com.alibaba.lindorm.client.core.utils.Bytes::toBig Decimal |
| BINARY | 直接为bytes的形式。 | 直接返回bytes。 |
| VARBINARY |  |  |
| DECIMAL | com.alibaba.lindorm.client.core.util s.Bytes::toBytes(BigDecimal) | com.alibaba.lindorm.client.core.utils.Bytes::toBig Decimal |
| TINYINT | 直接将数据封装成byte[]的第一个 byte。 | 直接返回bytes[0]。 |
| SMALLINT | com.alibaba.lindorm.client.core.util s.Bytes::toBytes(short) | com.alibaba.lindorm.client.core.utils.Bytes::toSh ort |

实时计算（流计算）

| INT | com.alibaba.lindorm.client.core.util s.Bytes::toBytes(int) | com.alibaba.lindorm.client.core.utils.Bytes::toInt |
|---|---|---|
| BIGINT | com.alibaba.lindorm.client.core.util s.Bytes::toBytes(long) | com.alibaba.lindorm.client.core.utils.Bytes::toLo ng |
| FLOAT | com.alibaba.lindorm.client.core.util s.Bytes::toBytes(float) | com.alibaba.lindorm.client.core.utils.Bytes::toFlo at |
| DOUBLE | com.alibaba.lindorm.client.core.util s.Bytes::toBytes(double) | com.alibaba.lindorm.client.core.utils.Bytes::toDo uble |
| DATE | 获取自1970.01.01以来的天数后，调用 com.alibaba.lindorm.client.core.util s.Bytes::toBytes(int)。 | com.alibaba.lindorm.client.core.utils.Bytes::toInt 得到自1970.01.01以来的天数。 |
| TIME | 获取自当天00:00:00以来的毫秒数后， 调用 com.alibaba.lindorm.client.core.util s.Bytes::toBytes(int)。 | com.alibaba.lindorm.client.core.utils.Bytes::toInt 得到自当天00:00:00以来的毫秒数。 |
| TIMESTAMP | 获取自1970.01.01 00:00:00以来的毫秒数后，调用 com.alibaba.lindorm.client.core.util s.Bytes::toBytes(long)。 | com.alibaba.lindorm.client.core.utils.Bytes::toLo ng得到自1970.01.01 00:00:00以来的毫秒数。 |

**代码示例**

实时计算（流计算）

```
CREATE TEMPORARY TABLE example_source(
 id INT,
 proc_time AS PROCTIME()
) WITH (
 'connector' = 'datagen',
 'number-of-rows' = '10',
 'fields.id.kind' = 'sequence',
 'fields.id.start' = '0',
 'fields.id.end' = '9'
); CREATE TEMPORARY TABLE lindorm_hbase_dim(
 `id` INT,
 `name` VARCHAR,
 `birth` VARCHAR,
 PRIMARY KEY (id) NOT ENFORCED
) WITH (
 'connector'='lindorm',
 'tablename'='${lindorm_dim_table}',
 'seedserver'='${lindorm_seed_server}',
 'namespace'='default',
 'username'='${lindorm_username}',
 'password'='${lindorm_username}'
); CREATE TEMPORARY TABLE lindorm_hbase_sink(
 `id` INT,
 `name` VARCHAR,
 `birth` VARCHAR,
 PRIMARY KEY (id) NOT ENFORCED
) WITH (
 'connector'='lindorm',
 'tablename'='${lindorm_sink_table}',
 'seedserver'='${lindorm_seed_server}',
 'namespace'='default',
 'username'='${lindorm_username}',
 'password'='${lindorm_username}'
); INSERT INTO lindorm_hbase_sink SELECT example_source.id as id, lindorm_hbase_dim.name as name, lindorm_hbase_dim.birth as birth FROM example_source JOIN lindorm_hbase_dim FOR SYSTEM_TIME AS OF PROCTIME() ON example_source.id = lindorm_hbase_dim.id;
```

### 云消息队列RocketMQ版

**重要**

实时计算（流计算） 鉴于云消息队列 RocketMQ 版 4.x标准版当前最高可达每秒5千条消息的限速机制，使用该版作为实时计算Flink版对接的消息中间件，可能会导致Flink作业运行不稳定。因此，在选择消息中间件时，如果您正在或计划通过标准版RocketMQ与Flink对接，请您谨慎评估。如果业务场景允许，请考虑使用 Kafka、日志服务（SLS）或DataHub等其他中间件进行替代。如果您确实需要使用云消息队列 RocketMQ 版 4.x标准版处理大规模的消息，也请同时与RocketMQ产品取得联系申请提升限速上限。

**背景信息**

云消息队列RocketMQ版是阿里云基于Apache RocketMQ构建的低延迟、高并发、高可用和高可靠的分布式消息中间件。其既可为分布式应用系统提供异步解耦和削峰填谷的能力，同时也具备互联网应用所需的海量消息堆积、高吞吐和可靠重试等特性。 RocketMQ连接器支持的信息如下。

| 类别 | 详情 |
|---|---|
| 支持类型 | 源表和结果表 |
| 运行模式 | 仅支持流模式 |
| 数据格式 | CSV和二进制格式 |
| 特有监控指标 | 源表 numRecordsIn numRecordsInPerSecond numBytesIn numBytesInPerScond currentEmitEventTimeLag currentFetchEventTimeLag sourceIdleTime 结果表 numRecordsOut numRecordsOutPerSecond numBytesOut numBytesOutPerSecond currentSendTime |
| API种类 | Datastream（仅支持RocketMQ 4.x）和SQL |
| 是否支持更新或删除结果表数据 | 不支持删除结果表数据，只支持插入和更新数据。 |

**特色功能**

RocketMQ源表和结果表支持属性字段，具体如下。 实时计算（流计算） 源表属性字段

| 字段名 | 字段类型 | 说明 |
|---|---|---|
| topic | VARCHAR METADATA VIRTUAL | 消息Topic。 |
| queue-id | INT METADATA VIRTUAL | 消息队列ID。 |
| queue-offset | BIGINT METADATA VIRTUAL | 消息队列的消费位点。 |
| msg-id | VARCHAR METADATA VIRTUAL | 消息ID。 |
| store- timestamp | TIMESTAMP(3) METADATA VIRTUAL | 消息存储时间。 |
| born- timestamp | TIMESTAMP(3) METADATA VIRTUAL | 消息生成时间。 |
| keys | VARCHAR METADATA VIRTUAL | 消息Keys。 |
| tags | VARCHAR METADATA VIRTUAL | 消息Tags。 |

结果表属性字段

| 字段名 | 字段类型 | 说明 |
|---|---|---|
| keys | VARCHAR METADATA | 消息Keys。 |
| tags | VARCHAR METADATA | 消息Tags。 |

**前提条件**

已创建了RocketMQ资源。

**使用限制**

仅Flink实时计算引擎VVR 8.0.3及以上版本支持5.x版本的RocketMQ。 在Flink实时计算引擎VVR 6.0.2以下版本，源表的并发度必须小于等于RocketMQ topic的分区数，在实时计算引擎VVR 6.0.2及以上版本解除该限制。您可以提前设置大于分区数的并发度，不需要因 RocketMQ的缩容而手动调整作业并发度。 RocketMQ连接器使用Pull Consumer消费，所有的子任务分担消费。

**语法结构**

实时计算（流计算）

```
CREATE TABLE mq_source(
  x varchar,
  y varchar,
  z varchar
) WITH (
  'connector' = 'mq5',
  'topic' = '<yourTopicName>',
  'endpoint' = '<yourEndpoint>',
  'consumerGroup' = '<yourConsumerGroup>'
);
```

**WITH参数**

通用

| 参数 | 说明 | 数据类型 | 是否必填 | 默认值 | 备注 |
|---|---|---|---|---|---|
| connect or | connector类型。 | String | 是 | 无 | RocketMQ 4.x固定值为 mq 。 RocketMQ 5.x固定值为 mq5 。 |
| endPoin t | EndPoint地址 | String | 是 | 无 | 请联系阿里云运维工程师获取。 |
| topic | topic名称。 | String | 是 | 无 | 无。 |
| accessId | 4.x：阿里云账号的 AccessKey ID。 5.x： RocketMQ实例用户名 | String | RocketMQ 4.x：是 RocketMQ 5.x：否 | 无 | 无。 |
| accessK ey | 4.x: 阿里云账号的AccessKey Secret。 5.x:实例密码 | String | RocketMQ 4.x：是 RocketMQ 5.x：否 | 无 | 无。 |

实时计算（流计算）

| tag | 订阅或写入的标签 | String | 否 | 无 | RocketMQ作为源表时， 只能读取单个tag。 RocketMQ作为结果表时，支持设置多个tag， 以逗号（,）进行分隔。 说明当作为结果表时，仅支持RocketMQ 4.x。 RocketMQ 5.x请使用结果表属性字段来指定写出消息的 tag。 |
|---|---|---|---|---|---|
| encodin g | 编码格式。 | String | 否 | UTF-8 | 无。 |
| instance ID | RocketMQ实例 ID。 | String | 否 | 无 | 如果RocketMQ实例无独立命名空间，则不可以使用instanceID参数。 如果RocketMQ实例有独立命名空间， 则instanceID参数必选。 说明仅RocketMQ 4.x支持该参数，RocketMQ 5.x不需要配置该参数。 |

源表独有

| 参数 | 说明 | 数据类型 | 是否必填 | 默认值 | 备注 |
|---|---|---|---|---|---|
| consumerGr oup | Consumer 组名。 | String | 是 | 无 | 无。 |
| pullInterval Ms | 上游没有数据可供消费时，source 的休眠时间。 | Int | 是 | 无 | 单位为毫秒。 目前没有限流机制，无法设置读取 RocketMQ的速率。 说明仅RocketMQ 4.x支持该参数，RocketMQ 5.x不需要配置该参数。 |
| timeZone | 时区。 | String | 否 | 无 | 例如，Asia/Shanghai。 |

实时计算（流计算）

| startTimeMs | 启动时间点。 | Long | 否 | 无 | 时间戳，单位为毫秒。 |
|---|---|---|---|---|---|
| startMessag eOffset | 消息开始的偏移量。 | Int | 否 | 无 | 如果填写该参数，则优先以 startMessageOffset 的位点开始加载数据。 |
| lineDelimite r | 解析Block 时，行分隔符。 | String | 否 | \n | 无。 |
| fieldDelimite r | 字段分隔符。 | String | 否 | \u000 1 | 根据MQ终端的模式，分隔符分别为： 在只读模式下（默认模式），分隔符为 \u0001 。该模式下，分隔符不可见。 在编辑模式下，分隔符为 ^A 。 |
| lengthCheck | 单行字段条数检查策略。 | Int | 否 | NONE | 取值如下： NONE：默认值。 解析出的字段数大于定义字段数时，按从左到右的顺序，取定义字段数量的数据。 解析出的字段数小于定义字段数时，跳过这行数据。 SKIP：解析出的字段数和定义字段数不同时跳过数据。 EXCEPTION：解析出的字段数和定义字段数不同时提示异常。 PAD：按从左到右顺序填充。 解析出的字段数大于定义字段数时，按从左到右的顺序，取定义字段数量的数据。 解析出的字段数小于定义字段数时，在行尾用Null填充缺少的字段。 说明 SKIP、EXCEPTION和PAD为可选值。 |
| columnError Debug | 是否打开调试开关。 | Boolea n | 否 | false | 如果设置为true，则打印解析异常的Log。 |
| pullBatchSiz e | 每次拉取消息的最大数量。 | Int | 否 | 64 | 仅实时计算引擎VVR 8.0.7及以上版本支持该参数。 |

结果表独有实时计算（流计算）

| 参数 | 说明 | 数据类型 | 是否必填 | 默认值 | 备注 |
|---|---|---|---|---|---|
| producerG roup | 写入的群组。 | String | 是 | 无 | 无。 |
| retryTimes | 写入的重试次数。 | Int | 否 | 10 | 无。 |
| sleepTime Ms | 重试间隔时间。 | Long | 否 | 5000 | 无。 |
| partitionFi eld | 指定字段名，将该字段作为分区列。 | String | 否 | 无 | 如果 mode 为 partition ，则该参数必填。 |

**类型映射**

| Flink字段类型 | 云消息队列RocketMQ字段类型 |
|---|---|
| VARCHAR | STRING |

**代码示例**

源表示例实时计算（流计算） CSV格式假设您的一条CSV格式消息记录如下。

```
1,name,male 2,name,female
```

**说明**

一条RocketMQ消息可以包括零条到多条数据记录，记录之间使用 \n 分隔。 Flink作业中，声明RocketMQ数据源表的DDL如下。 RocketMQ 5.x

```
CREATE TABLE mq_source(
  id varchar,
  name varchar,
  gender varchar,
  topic varchar metadata virtual
) WITH (
  'connector' = 'mq5',
  'topic' = 'mq-test',
  'endpoint' = '<yourEndpoint>',
  'consumerGroup' = 'mq-group',
  'fieldDelimiter' = ','
);
```

RocketMQ 4.x

```
CREATE TABLE mq_source(
  id varchar,
  name varchar,
  gender varchar,
  topic varchar metadata virtual
) WITH (
  'connector' = 'mq',
  'topic' = 'mq-test',
  'endpoint' = '<yourEndpoint>',
  'pullIntervalMs' = '1000',
  'accessId' = '${secret_values.ak_id}',
  'accessKey' = '${secret_values.ak_secret}',
  'consumerGroup' = 'mq-group',
  'fieldDelimiter' = ','
);
```

实时计算（流计算） 二进制格式 RocketMQ 5.x

```
CREATE TEMPORARY TABLE source_table (
  mess varbinary
) WITH (
  'connector' = 'mq5',
  'endpoint' = '<yourEndpoint>',
  'topic' = 'mq-test',
  'consumerGroup' = 'mq-group'
); CREATE TEMPORARY TABLE out_table (
  commodity varchar
) WITH ( ); INSERT INTO out_table select
  cast(mess as varchar)
FROM source_table;
```

RocketMQ 4.x

```
CREATE TEMPORARY TABLE source_table (
  mess varbinary
) WITH (
  'connector' = 'mq',
  'endpoint' = '<yourEndpoint>',
  'pullIntervalMs' = '500',
  'accessId' = '${secret_values.ak_id}',
  'accessKey' = '${secret_values.ak_secret}',
  'topic' = 'mq-test',
  'consumerGroup' = 'mq-group'
); CREATE TEMPORARY TABLE out_table (
  commodity varchar
) WITH ( ); INSERT INTO out_table select
  cast(mess as varchar)
FROM source_table;
```

结果表示例实时计算（流计算） 创建结果表 RocketMQ 5.x

```
CREATE TABLE mq_sink (
  id INTEGER,
  len BIGINT,
  content VARCHAR
) WITH (
  'connector'='mq5',
  'endpoint'='<yourEndpoint>',
  'topic'='<yourTopicName>',
  'producerGroup'='<yourGroupName>'
);
```

RocketMQ 4.x

```
CREATE TABLE mq_sink (
  id INTEGER,
  len BIGINT,
  content VARCHAR
) WITH (
  'connector'='mq',
  'endpoint'='<yourEndpoint>',
  'accessId'='${secret_values.ak_id}',
  'accessKey'='${secret_values.ak_secret}',
  'topic'='<yourTopicName>',
  'producerGroup'='<yourGroupName>'
);
```

**说明**

如果您的MQ消息为二进制格式，则DDL中只能定义一个字段，且字段类型必须为 VARBINARY。 实时计算（流计算） 创建将 `keys` 和 `tags` 字段指定为RocketMQ消息的key和tag的结果表 RocketMQ 5.x

```
CREATE TABLE mq_sink (
  id INTEGER,
  len BIGINT,
  content VARCHAR,
  keys VARCHAR METADATA,
  tags VARCHAR METADATA
) WITH (
  'connector'='mq5',
  'endpoint'='<yourEndpoint>',
  'topic'='<yourTopicName>',
  'producerGroup'='<yourGroupName>'
);
```

RocketMQ 4.x

```
CREATE TABLE mq_sink (
  id INTEGER,
  len BIGINT,
  content VARCHAR,
  keys VARCHAR METADATA,
  tags VARCHAR METADATA
) WITH (
  'connector'='mq',
  'endpoint'='<yourEndpoint>',
  'accessId'='${secret_values.ak_id}',
  'accessKey'='${secret_values.ak_secret}',
  'topic'='<yourTopicName>',
  'producerGroup'='<yourGroupName>'
);
```

**DataStream API**

**重要**

仅RocketMQ 4.x支持DataStream API。 通过DataStream的方式读写数据时，则需要使用对应的DataStream连接器连接Flink。

| 时计算引擎VVR提供 | MetaQSource |  |
|---|---|---|
| MetaQOutputFormat |  | ，用于写入R |

```
/**
 * A demo that illustrates how to consume messages from RocketMQ, convert
 * messages, then produce messages to RocketMQ.
```

`*/`

```java
public class RocketMQDataStreamDemo2 {
    public static final String ENDPOINT = "<yourEndpoint>";
    public static final String ACCESS_ID = "<accessID>";
    public static final String ACCESS_KEY = "<accessKey>";
    public static final String INSTANCE_ID = "<instanceID>";
    public static final String SOURCETOPIC = "<sourceTopicName>";
```

实时计算（流计算） p g _ p

```
    public static final String CONSUMER_GROUP = "<consumerGroup>";
    public static final String SINK_TOPIC = "<sinkTopicName>";
    public static final String PRODUCER_GROUP = "<producerGroup>";
    public static void main(String[] args) throws Exception {
        // Sets up the streaming execution environment
        Configuration config = new Configuration();
       // This is only required for local testing
        config.setString("classloader.parent-first-patterns.additional",
"com.alibaba.ververica.connectors.metaq.source.reader.deserializer.MetaQRecordDeserializat nSchema;com.alibaba.ververica.connector.mq.shaded.");
        final StreamExecutionEnvironment env =
StreamExecutionEnvironment.getExecutionEnvironment(config);
        // Creates and adds RocketMQ source.
        env.fromSource(createRocketMQSource(), WatermarkStrategy.noWatermarks(), "source
```

`")`

```java
                // Converts message body to upper case.
                .map(RocketMQDataStreamDemo2::convertMessages)
                // Creates and adds RocketMQ sink.
                .addSink(new OutputFormatSinkFunction<>(createRocketMQOutputFormat()))
                .name(RocketMQDataStreamDemo2.class.getSimpleName());
        // Compiles and submits job.
        env.execute("RocketMQ connector end-to-end DataStream demo");
    }
    private static MetaQSource<MessageExt> createRocketMQSource() {
        Properties mqProperties = createMQProperties();
        return new MetaQSource<>(SOURCE_TOPIC,
                CONSUMER_GROUP,
                null, // always null
                null, // tag of the messages to consumer
                Long.MAX_VALUE, // stop timestamp in milliseconds
                -1, // Start timestamp in milliseconds. Set to -1 to disable starting fr
om offset.
                0, // Start offset.
                300_000, // Partition discover interval.
                mqProperties,
                Boundedness.CONTINUOUS_UNBOUNDED,
                new MyDeserializationSchema());
    }
    private static MetaQOutputFormat createRocketMQOutputFormat() {
        return new MetaQOutputFormat.Builder()
                .setTopicName(SINK_TOPIC)
                .setProducerGroup(PRODUCER_GROUP)
                .setMqProperties(createMQProperties())
                .build();
    }
    private static Properties createMQProperties() {
        Properties properties = new Properties();
```

实时计算（流计算）

```java
        properties.put(PROPERTY_ONS_CHANNEL, "ALIYUN");
        properties.put(NAMESRV_ADDR, ENDPOINT);
        properties.put(PROPERTY_ACCESSKEY, ACCESS_ID);
        properties.put(PROPERTY_SECRETKEY, ACCESS_KEY);
        properties.put(PROPERTY_ROCKET_AUTH_ENABLED, true);
        properties.put(PROPERTY_INSTANCE_ID, INSTANCE_ID);
        return properties;
    }
    private static List<MessageExt> convertMessages(MessageExt messages) {
        return Collections.singletonList(messages);
    }
    public static class MyDeserializationSchema implements
MetaQRecordDeserializationSchema<MessageExt> {
        @Override
        public void deserialize(List<MessageExt> list, Collector<MessageExt> collector)
{
            for (MessageExt messageExt : list) {
                collector.collect(messageExt);
            }
        }
        @Override
        public TypeInformation<MessageExt> getProducedType() {
            return TypeInformation.of(MessageExt.class);
        }
    }
}
    }
}
```

### 云数据库Redis

**背景信息**

阿里云数据库Redis是兼容开源Redis协议标准、提供内存加硬盘混合存储的数据库服务，基于高可靠双机热备架构及可平滑扩展的集群架构，充分满足高吞吐、低延迟及弹性变配的业务需求。 Redis连接器支持的信息如下。

| 类别 | 详情 |
|---|---|
| 支持类型 | 维表和结果表 |
| 支持模式 | 流模式 |
| 数据格式 | String |

实时计算（流计算）

| 特有监控指标 | 维表：无结果表： numBytesOut numRecordsOutPerSecond numBytesOutPerSecond currentSendTime |
|---|---|
| API 种类 | SQL |
| 是否支持更新或删除结果表数据 | 是 |

**前提条件**

已设置白名单。

**使用限制**

目前Redis连接器是仅提供Best Effort语义，无法保证数据的Exactly Once，需要您自行保证语义上的幂等性。 维表使用限制有： 仅支持读取Redis数据存储中STRING和HASHMAP类型的数据。 维表的字段必须为STRING，且必须声明且只能声明一个主键。 维表JOIN时，ON条件必须包含主键的等值条件。

**语法结构**

```
CREATE TABLE redis_table (
  col1 STRING,
  col2 STRING,
  PRIMARY KEY (col1) NOT ENFORCED -- 必填。
) WITH (
  'connector' = 'redis',
  'host' = '<yourHost>',
```

`'mode' = 'STRING' --` 结果表时必填。

```
);
```

**WITH参数**

通用

| 参数 | 说明 | 数据类型 | 是否必填 | 默认值 | 备注 |
|---|---|---|---|---|---|
| connec tor | 表类型。 | String | 是 | 无 | 固定值为redis。 |

实时计算（流计算）

| host | Redis Server连接地址。 | String | 是 |  | 无 | 请联系阿里云运维工程师获取。 |  |  |
|---|---|---|---|---|---|---|---|---|
| port | Redis Server连接端口。 | Int | 否 |  | 6379 | 无。 |  |  |
| passw ord | Redis数据库密码。 | String | 否 |  | 空字符串，表示不进行校验。 | 无。 |  |  |
| dbNu m | 选择操作的数据库编号。 | Int | 否 |  | 0 | 无。 |  |  |
| cluster Mode | Redis集群是否为集群模式。 | Boolea n | 否 |  | false | 无。 |  |  |
| hostAn dPorts | Redis集群的主机和端口号。 说明如果启用了集群模式，且不需要连接高可用，可以通过host和 port配置项只配置其中一台主机，也可以只配置该项。该配置项的优先级高于独立的host和 port配置项。 | String | 否 |  | 空 | 如果 ClusterMode = true ，同时需要支持Jedis 到自建Redis集群连接的高可用，必须配置该项。配置格式为字符串： "host1:port1,host2 :port2" 。 |  |  |
|  |  |  |  |  |  |  | "host1:port1,host2 |  |
|  |  |  |  |  |  | :port2" |  |  |
| key- prefix | 表主键值的前缀。 | String | 否 |  | 无 | 配置后，Redis维表和结果表的主键字段值在查询或者写入 Redis时会被自动添加前缀， 该前缀是由键前缀（key- prefix）和其后的前缀分隔符 （key-prefix-delimiter）组成。 说明仅实时计算引擎VVR 8.0.7及以上版本支持该参数。 |  |  |
| key- prefix- delimit er | 表主键值与表主键值前缀之间的分隔符。 | String | 否 |  | 无 |  |  |  |

|  |  | ClusterMode = |
|---|---|---|
|  | true |  |

结果表独有

| 参数 | 说明 | 数据类型 | 是否必填 | 默认值 | 备注 |
|---|---|---|---|---|---|

实时计算（流计算）

| mode | 对应Redis的数据结构。 | Strin g | 是 | 无 | 云数据库Redis版结果表支持5种Redis数据结构，其DDL必须按指定格式定义且主键必须被定义。 |
|---|---|---|---|---|---|
| flatten Hash | 是否按照多值模式写入 HASHMAP 类型数据。 | Boole an | 否 | false | 参数取值如下： true：按照多值模式写入。此时，您需要在 DDL中声明多个非主键字段，主键字段值对应 key，每个非主键字段的字段名对应一个 field，字段值对应该field的value。 false：按照单值模式写入。此时您需要在DDL 中声明三个字段，第一个主键字段的字段值对应key，第二个非主键字段的字段值对应 field，第三个非主键字段的字段值对应 value。 说明该参数仅在mode参数取值为 HASHMAP时生效。 仅实时计算引擎VVR 8.0.7及以上版本支持该参数。 |
| ignore Delete | 是否忽略 Retraction 消息。 | Boole an | 否 | false | 参数取值如下： true：收到Retraction消息时，忽略 Retraction消息。 false：收到Retraction消息时，同时删除数据对应的key及已插入的数据。 |
| expirat ion | 为写入数据对应的Key设置TTL。 | Long | 否 | 0，代表不设置 TTL。 | 如果该参数的值大于0，则写入数据对应的Key会被设置相应的TTL，单位为毫秒。 |

维表独有

| 参数 | 说明 | 数据类型 | 是否必填 | 默认值 | 备注 |
|---|---|---|---|---|---|

实时计算（流计算）

| mode | 读取Redis的数据类型。 | String | 否 | STRIN G | 参数取值如下： STRING：不指定时，默认以STRING类型读取。 HASHMAP：当指定mode为HASHMAP 时，将按照多值模式读取HASHMAP类型数据。 此时DDL需要声明多个非主键字段，主键字段值对应key，每个非主键字段的字段名对应field，字段值对应value。 说明仅实时计算引擎VVR 8.0.7及以上版本支持该参数。 如果您需要以单值模式读取 HASHMAP类型数据时，请配置hashName参数。 |
|---|---|---|---|---|---|
| hashN ame | 单值模式读取 HASHMAP类型数据时使用的key。 | String | 否 | 无 | 如果您未指定mode参数，还希望以单值模式读取HASHMAP类型数据。此时，您需要配置hashName。 此时DDL仅需要声明两个字段，第一个主键字段的字段值对应field，第二个非主键字段的字段值对应value。 |
| cache | 缓存策略。 | String | 否 | None | 云数据库Redis维表支持以下缓存策略： None（默认值）：无缓存。 LRU：缓存维表里的部分数据。源表的每条数据都会触发系统先在Cache中查找数据，如果没有找到，则去物理维表中查找。 ALL：缓存维表里的所有数据。在Job运行前，系统会将维表中所有数据加载到 Cache中，之后所有的维表查找数据都会通过Cache进行。如果在Cache中无法找到数据，则KEY不存在。全量的Cache有一个过期时间，过期后会重新加载一遍全量Cache。 重要仅实时计算引擎VVR 8.0.3及以上版本支持ALL缓存策略。 ALL缓存策略目前仅支持单值模式读取hashmap类型数据 （即hashName参数不为空，mode参数为空时）。 需要配置相关参数：缓存大小 （cacheSize）和缓存更新时间间隔（cacheTTLMs）。 |

实时计算（流计算）

| cache Size | 缓存大小。 | Long | 否 | 1000 0 | 当选择LRU缓存策略时，需要设置缓存大小。 |
|---|---|---|---|---|---|
| cache TTLMs | 缓存超时时长，单位为毫秒。 | Long | 否 | 无 | cacheTTLMs配置和cache有关： 如果cache配置为None，则 cacheTTLMs可以不配置，表示缓存不超时。 如果cache配置为LRU，则cacheTTLMs 为缓存超时时间。默认不过期。 如果cache配置为ALL，则cacheTTLMs 为缓存加载时间。默认不重新加载。 |
| cache Empty | 是否缓存空结果。 | Boole an | 否 | true | 无。 |
| cache Reloa dTime Black List | 更新时间黑名单。在缓存策略选择为ALL 时，启用更新时间黑名单，防止在此时间内做Cache更新（例如双11场景）。 | String | 否 | 无 | 格式为2017-10-24 14:00 -> 2017- 10-24 15:00，2017-11-10 23:30 -> 2017-11-11 08:00。分隔符的使用情况如下所示： 用英文逗号（,）来分隔多个黑名单。 用箭头（->）来分割黑名单的起始结束时间。 |

**Redis结果表数据结构格式**

| 类型 | 格式 | Redis插入数据的命令 |
|---|---|---|
| STRING类型 | DDL为两列： 第1列为key，STRING类型。 第2列为value，STRING类型。 | set key value |
| LIST类型 | DDL为两列： 第1列为key，STRING类型。 第2列为value，STRING类型。 | lpush key value |
| SET类型 | DDL为两列： 第1列为key，STRING类型。 第2列为value，STRING类型。 | sadd key value |
|  | 默认情况下，DDL为三列： 第1列为key，STRING类型。 第2列为field，STRING类型。 第3列为value，STRING类型。 | hmset key field value |

|  | 实时计算（流计算） |  |  |  |  |  |
|---|---|---|---|---|---|---|
|  | HASHMAP类型 |  |  |  |  |  |
|  |  | flattenHash参数配置为true时，DDL支持多列，以4列的情况为例： 第1列为key，STRING类型。 第2列的字段名（假设为col1）对应一个 field，字段值（假设为value1）对应该 field的value，STRING类型。 第3列的字段名（假设为col2）对应一个 field，字段值（假设为value2）对应该 field的value，STRING类型。 第4列的字段名（假设为col3）对应一个 field，字段值（假设为value3）对应该 field的value，STRING类型。 |  | hmset key col1 value1 col2 value2 col3 value3 |  |  |
|  |  |  |  |  | hmset key col1 value1 col2 value2 |  |
|  |  |  | 第3列的字段名（假设为col2）对应一个 | col3 value3 |  |  |
|  | SORTEDSET类型 | DDL为三列： 第1列为key，STRING类型。 第2列为score，DOUBLE类型。 第3列为value，STRING类型。 |  | zadd key score value |  |  |

**类型映射**

| 类型 | Redis字段类型 | Flink字段类型 |
|---|---|---|
| 通用 | STRING | STRING |
| 结果表独有 | SCORE | DOUBLE |

**说明**

因为Redis的SCORE类型应用于SORTEDSET（有序集合），所以需要手动为每个Value设置一个 DOUBLE类型的SCORE，Value才能按照该SCORE从小到大进行排序。

**使用示例**

结果表类数据在代例中结表中列的值会作为实时计算（流计算） 写入STRING类型数据：在代码示例中， `redis_sink` 结果表中 `col1` 列的值会作为 key， `col2` 列的值会作为value写入到redis中。

```
  col1 STRING,
  col2 STRING
) WITH (
  'connector' = 'datagen',
  'number-of-rows' = '100'
); CREATE TEMPORARY TABLE redis_sink (
  col1 STRING,
  col2 STRING,
  PRIMARY KEY (col1) NOT ENFORCED
) WITH (
  'connector' = 'redis',
  'mode' = 'STRING',
  'host' = '<yourHost>',
  'port' = '<yourPort>',
  'password' = '<yourPassword>'
); INSERT INTO redis_sink SELECT * FROM datagen_source;
```

实时计算（流计算） 单值模式写入HASHMAP类型数据：在代码示例中， `redis_sink` 结果表中的 `col1` 列的值会作为 key， `col2` 列的值会作为field， `col3` 列的值会作为value写入到Redis中。

```
  col1 STRING,
  col2 STRING,
  col3 STRING
) WITH (
  'connector' = 'datagen',
  'number-of-rows' = '100'
); CREATE TEMPORARY TABLE redis_sink (
  col1 STRING,
  col2 STRING,
  col3 STRING
  PRIMARY KEY (col1) NOT ENFORCED
) WITH (
  'connector' = 'redis',
  'mode' = 'HASHMAP',
  'host' = '<yourHost>',
  'port' = '<yourPort>',
  'password' = '<yourPassword>'
); INSERT INTO redis_sink SELECT * FROM datagen_source;
```

实时计算（流计算） 多值模式写入HASHMAP类型数据：在代码示例中， `redis_sink` 结果表中的 `col1` 列的值会作为 key， `col2` 列的值会作为field为col2的value， `col3` 列的值会作为field为col3的 value， `col4` 列的值会作为field为col4的value，写入到Redis中。

```
  col1 STRING,
  col2 STRING,
  col3 STRING,
  col4 STRING
) WITH (
  'connector' = 'datagen',
  'number-of-rows' = '100'
); CREATE TEMPORARY TABLE redis_sink (
  col1 STRING,
  col2 STRING,
  col3 STRING,
  col4 STRING
  PRIMARY KEY (col1) NOT ENFORCED
) WITH (
  'connector' = 'redis',
  'mode' = 'HASHMAP',
  'flattenHash' = 'true',
  'host' = '<yourHost>',
  'port' = '<yourPort>',
  'password' = '<yourPassword>'
); INSERT INTO redis_sink SELECT * FROM datagen_source;
```

维表读类数据在代例中维表中的列的值对应列的实时计算（流计算） 读取STRING类型数据：在代码示例中， `redis_dim` 维表中的 `col1` 列的值对应key， `col2` 列的值对应value。

```
  col1 STRING,
  proctime as PROCTIME()
) WITH (
  'connector' = 'datagen',
  'number-of-rows' = '100'
); CREATE TEMPORARY TABLE redis_dim (
  col1 STRING,
  col2 STRING,
  PRIMARY KEY (col1) NOT ENFORCED
) WITH (
  'connector' = 'redis',
  'host' = '<yourHost>',
  'port' = '<yourPort>',
  'password' = '<yourPassword>'
);
  col1 STRING,
  col2 STRING,
  col3 STRING
) WITH ( ); SELECT t1.col1, t2.col1, t2.col2 JOIN redis_dim FOR SYSTEM_TIME AS OF t1.proctime AS t2 ON t1.col1 = t2.col1;
```

实时计算（流计算） 单值模式读取HASHMAP类型数据：在代码示例中， `hashName` 参数的值testKey为 key， `redis_dim` 维表中的 `col1` 列的值对应field， `col2` 列的值对应value。

```
  col1 STRING,
  proctime as PROCTIME()
) WITH (
  'connector' = 'datagen',
  'number-of-rows' = '100'
); CREATE TEMPORARY TABLE redis_dim (
  col1 STRING,
  col2 STRING,
  PRIMARY KEY (col1) NOT ENFORCED
) WITH (
  'connector' = 'redis',
  'host' = '<yourHost>',
  'port' = '<yourPort>',
  'password' = '<yourPassword>',
  'hashName' = 'testkey'
);
  col1 STRING,
  col2 STRING,
  col3 STRING
) WITH ( ); SELECT t1.col1, t2.col1, t2.col2 JOIN redis_dim FOR SYSTEM_TIME AS OF t1.proctime AS t2 ON t1.col1 = t2.col1;
```

实时计算（流计算） 多值模式读取HASHMAP类型数据：在代码示例中， `redis_dim` 维表中的 `col1` 列的值对应 key， `col2` 列的值对应field为col2的value， `col3` 列的值对应field为col3的value， `col4` 列的值对应field为col4的value。

```
  col1 STRING,
  proctime as PROCTIME()
) WITH (
  'connector' = 'datagen',
  'number-of-rows' = '100'
); CREATE TEMPORARY TABLE redis_dim (
  col1 STRING,
  col2 STRING,
  col3 STRING,
  col4 STRING
  PRIMARY KEY (col1) NOT ENFORCED
) WITH (
  'connector' = 'redis',
  'host' = '<yourHost>',
  'port' = '<yourPort>',
  'password' = '<yourPassword>',
  'mode' = 'HASHMAP'
);
  col1 STRING,
  col2 STRING,
  col3 STRING,
  col4 STRING
) WITH ( ); SELECT t1.col1, t2.col2, t2.col3, t2.col4 JOIN redis_dim FOR SYSTEM_TIME AS OF t1.proctime AS t2 ON t1.col1 = t2.col1;
```

### 云数据库Tair

本文为您介绍如何使用云原生内存数据库Tair连接器。

**背景信息**

云原生内存数据库Tair是阿里云国产自研的云原生内存数据库。在完全兼容Redis的基础上，提供了丰富的数据模型和企业级能力来帮助客户构建实时在线场景。同时，Tair与新型存储介质——持久内存的高效结合，相比内存，成本降低30%以上，并能做到数据持久化和提供近似于内存的性能。 Tair连接器支持的信息如下。

| 类别 | 详情 |
|---|---|

| link存算分离版开发指南·连接器 | 实时计算（流计算） |
|---|---|

| 支持类型 | 结果表 |
|---|---|
| 运行模式 | 仅支持流模式 |
| 数据格式 | String |
| 特有监控指标 | numBytesSend numBytesSendPerSecond numRecordsSend numRecordsSendPerSecond numRecordSendErrors currentSendTime |
| API种类 | SQL |
| 是否支持更新或者删除结果表数据 | 是 |

**前提条件**

已设置白名单。 已创建云原生内存数据库Tair实例。

**使用限制**

云原生内存数据库Tair连接器不支持配置多个host。 仅Flink计算引擎VVR 6.0.6及以上版本支持云原生内存数据库Tair连接器。

**语法结构**

云原生内存数据库Tair在兼容Redis数据结构STRING、LIST、SET、HASHMAP和SORTEDSET的基础上， 支持所有Tair自研数据结构。 DDL语句定义示例如下。

```
CREATE TABLE tair_table (
  a STRING,
  b STRING,
  PRIMARY KEY (a) NOT ENFORCED -- 必填。
) WITH (
  'connector'= 'tair',
  'host' = '<yourHost>'
);
```

实时计算（流计算）

**说明**

云原生内存数据库Tair兼容Redis数据结构。

**WITH参数**

| 参数 | 说明 | 数据类型 | 是否必填 | 默认值 | 备注 |
|---|---|---|---|---|---|
| connector | 表类型。 | String | 是 | 无 | 固定值为tair。 |
| host | Tair Server连接地址。 | String | 是 | 无 | 请联系阿里云运维工程师获取。 |
| mode | 对应Tair数据结构。 | String | 是 | 无 | 参数取值如下： string list set hashmap sortedset tairstring tairhash tairzset tairbloom tairdoc tairsearch tairts taircpc tairroaring tairgis tairvector Tair支持的数据结构包括Redis原生数据结构和Tair自研数据结构。 说明仅Flink计算引擎VVR 8.0.1 及以上版本支持TairTs、 TairCpc、TairRoaring、 TairVector和TairGis。 云原生内存数据库Tair结果表支持Tair自研数据结构，其 DDL必须按指定格式定义且主键必须被定义。 |

实时计算（流计算）

| port | Tair Server连接端口。 | Int | 否 | 637 9 | 无。 |
|---|---|---|---|---|---|
| password | Tair数据库密码。 | String | 否 | 空字符串 | 空字符串表示不进行校验。 |
| dbNum | 目标数据库编号。 | Int | 否 | 0 | 无。 |
| clusterMode | 是否为集群模式。 | Boole an | 否 | false | 参数取值如下： true：集群模式 false：单机模式 |
| ignoreDelet e | 是否忽略 Retraction消息。 | Boole an | 否 | false | 参数取值如下： false（默认值）：收到Retraction时， 同时删除数据对应的key及已插入的数据。 true：收到Retraction时，同时保留数据对应的key及已插入的数据。 |
| expiration | 为写入数据对应的 key设置TTL。 | Long | 否 | 0 | 0表示未设置TTL。如果该参数的值大于0， 则写入数据对应的Key会被设置相应的 TTL，单位为毫秒。 |
| expirationAt | 为写入数据对应的 key设置绝对过期时间。 | Long | 否 | 0 | 单位为毫秒，默认值为0，代表不设过期时间。 如果该参数的值大于0且expiration参数为 0，则写入数据对应的Key会被设置相应的绝对过期时间。 |
| incrMode | 对应Tair的sink模式。 | String | 否 | Non e | 参数取值如下： None（默认值）：代表插入操作。 int：代表incrby操作，incr的值由 incrValue给出，为固定值。 float：代表incrbyfloat操作，incr的值由incrValue给出，为固定值。 dynamic int：代表incrby操作，incr _ 的值由incrValue对应的列给出。 dynamic float：代表incrbyfloat操 _ 作，incr的值由incrValue对应的列给出。 |

实时计算（流计算）

| incrValue | incrMode下incr的值。 | String | 否 | 无 | 参数取值如下： incrMode为None时，不会设置。 incrMode为int或float时，incrValue为 incr的值。 incrMode为dynamic int或 _ dynamic float时，incrValue为DDL中 _ incr值所在列的列名。 |
|---|---|---|---|---|---|
| fieldExpireM ode | tairhash结构field 级别或tairts结构 Skey级别的过期模式。 | String | 否 | Non e | 参数取值如下： None：不会过期。 millisecond：相对过期时间，过期时间由fieldExpireValue给出，为固定值。 说明 tairtsSkey级别的过期模式取值只支持为millisecond。 unixtime：绝对过期时间，过期时间由 fieldExpireValue给出，为固定值。 dynamic millisecond：相对过期时 _ 间，过期时间由 fieldExpireValue对应的列给出。 dynamic unixtime：绝对过期时间， _ 过期时间由fieldExpireValue对应的列给出。 |
| fieldExpireV alue | tairhash结构 field级别或tairts 结构Skey级别过期时间。 | String | 否 | 无 | 参数取值如下： fieldExpireMode为 None，fieldExpireValue标识不会设置过期时间。 fieldExpireMode为millisecond或 unixtime时，fieldExpireValue为过期时间的值。 fieldExpireMode为 dynamic millisecond或 _ dynamic unixtime _ 时，fieldExpireValue为DDL中过期时间所在列的列名。 |

**类型映射**

| Flink字段类型 | Tair字段类型 |
|---|---|
| VARCHAR | STRING |
| DOUBLE | DOUBLE |

**Tair自研数据结构格式**

实时计算（流计算）

| 类型 | 格式 | 操作命令 |
|---|---|---|
| TairString | incrMode为None时，DDL为2列： 第1列为key，STRING类型。 第2列为value，STRING类型。 | exset key value |
|  | incrMode为int或float时，DDL为1列，第1列为key，STRING类型。 | exincrby/exincrbyfloat key incrValue |
|  | incrMode为dynamic int或dynamic float _ _ 时，DDL为2列： 第1列为key，STRING类型。 第2列为incrValue，STRING类型。 | exincrby/exincrbyfloat key incrValue |
| TairHash | incrMode为None时，DDL为3列： 第1列为key，STRING类型。 第2列为field，STRING类型。 第3列为field对应的value，STRING 类型。 | exhset key field value |
|  | incrMode为int或float时，DDL为2列： 第1列为key，STRING类型。 第2列为field，STRING类型。 | exhincrby/exincrbyfloat key field incrValue |
|  | incrMode为dynamic int或dynamic float _ _ 时，DDL为3列： 第1列为key，STRING类型。 第2列为field，STRING类型。 第3列为field对应的incrValue，STRING类型。 | exhincrby/exincrbyfloat key field incrValue |
| TairZset | incrMode为None时，Tairzset支持多维度的排序能力，最大支持256维的 double类型的分值排序，所以DDL介于 3列和258列之间。 第1列为key，STRING类型。 第2列为member，STRING类型。 后续不定列数为score，DOUBLE类型。 | exzadd key score member 说明如果您需实现多维度排序，则各维度的score 格式必须相同。 |
|  | incrMode为int或float时，DDL为2列： 第1列为key，STRING类型。 第2列为member，STRING类型。 | exzincyby key member incrValue |

实时计算（流计算）

|  | incrMode为dynamic int或dynamic float _ _ 时，DDL为3列： 第1列为key，STRING类型。 第2列为member，STRING类型。 第3列为incrValue，STRING类型。 | exzincyby key member incrValue |
|---|---|---|
| TairBloo m | 只支持incrMode为None模式。 第一次插入时会自动创建一个默认容量 （capacity）为100，错误率（error rate） _ 为0.01的Tairbloom。DDL为2列： 第1列为key，STRING类型。 第2列为item，STRING类型。 | BF.ADD key item |
| TairDoc | 只支持incrMode为None模式，DDL为3列： 第1列为key，STRING类型。 第2列为path，STRING类型。 第3列为json，STRING类型。 | JSON.SET key path json |
| TairSearc h | incrMode为None时，DDL为4列： 第1列为index，STRING类型。 第2列为docid，STRING类型。 第3列是document，STRING类型，必须是 JSON文档。 第4列为mappings，STRING类型。 | TFT.ADDDOC index document docid 说明插入数据前需要先创建索引并添加映射，命令如下。 TFT.CREATEINDEX index mappings |
|  | incrMode为int或float时，DDL为4列： 第1列为index，STRING类型。 第2列为docid，STRING类型。 第3列是field，STRING类型。 第4列为mappings，STRING类型。 | 文档操作命令如下。 TFT.INCRLONGDOCFIELD/TFT.INCRFLOATDO CFIELD index doc id field increment _ 说明插入数据前需要先创建索引并添加映射，命令如下。 TFT.CREATEINDEX index mappings |

实时计算（流计算）

|  | incrMode为dynamic int或dynamic float _ _ 时，DDL为5列： 第1列为index，STRING类型。 第2列为docid，STRING类型。 第3列是field，STRING类型。 第4列为mappings，STRING类型。 第5列为incrValue，STRING类型。 | 文档操作命令如下。 TFT.INCRLONGDOCFIELD/TFT.INCRFLOATDO CFIELD index doc id field increment _ 说明插入数据前需要先创建索引并添加映射，命令如下。 TFT.CREATEINDEX index mappings |
|---|---|---|
| TairCpc | incrMode为只支持为None模式。DDL为2 列： 第1列为key，STRING类型。 第2列为item，STRING类型。 | CPC.UPDATE key item |
| TairGis | incrMode只支持为None模式。DDL为3列： 第1列为key，STRING类型。 第2列为polygonName （多边形的名字），STRING类型。 第3列为polygonWkt（多边形的 WKT（Well-known text）描述），STRING类型。 | GIS.ADD area polygonName polygonWkt |
| TairRoari ng | incrMode只支持为None模式。DDL为3列： 第一列为key，STRING类型。 第二列为offset，指定的偏移量，BIGINT类型。 第三列为value，取值为0或1，BIGINT类型。 | TR.SETBIT key offset value |

实时计算（流计算）

| TairVecto r | incrMode只支持为None模式。DDL为6列： 第1列为index name（索引的名 _ 字），STRING类型。 第2列为key（该记录的主键），STRING类型。 第3列为vector data（向量数 _ 据），STRING类型。 第4列为dims（向量维度），INT类型。 第5列为algorithm（构建、查询索引的算法），STRING类型。 第6列为distance method（计算向量距离 _ 函数），STRING类型。 | TVS.HSET index name key VECTOR _ vector data _ 说明插入数据前需要先创建索引并添加映射，命令如下。 TVS.CREATEINDEX index name dims _ algorithm distance method _ |
|---|---|---|
| TairTs | incrMode为None时，DDL为4列： 第1列为Pkey（一组时间线），STRING类型。 第2列为 Skey（一条时间线），STRING类型。 第3列为timestamp，STRING 类型。 第4列为value，STRING类型。 | EXTS.S.RAW MODIFY Pkey Skey _ timestamp value |
|  | incrMode为float时，DDL为3列： 第1列为Pkey，STRING类型。 第2列为Skey，STRING类型。 第3列为timestamp，STRING 类型。 | EXTS.S.RAW INCRBY Pkey Skey _ timestamp incrValue |
|  | incrMode为dynamic float时，DDL 为4列： _ 第1列为Pkey，STRING类型。 第2列为Skey，STRING类型。 第3列为timestamp，STRING类型。 第4列为timestamp（第三列的值）对应的 incrValue，STRING类型。 | EXTS.S.RAW INCRBY Pkey Skey _ timestamp incrValue |

**使用示例**

普通模式插入结果数据示例实时计算（流计算）

```json
  v STRING,
  p STRING
) WITH ( ); CREATE TEMPORARY TABLE tair_output (
  index_name STRING,
  doc_id STRING,
  doc STRING,
  mapping STRING,
  PRIMARY KEY(index_name) NOT ENFORCED
) WITH (
  'connector' = 'tair',
  'mode' = 'tairsearch',
  'host' = '${tairHost}',
  'port' = '${tairPort}',
  'password' = '${password}'
); INSERT INTO tair_output SELECT 'index' as index,v,p,'{"mappings":{"_source":{"enabled":true},"properties": {"product_id":{"type":"keyword","ignore_above":128},"product_name": {"type":"text"}}}}' as mapping FROM datagen_stream;
```

incr模式插入结果数据示例

```
  v STRING,
  p STRING
) WITH ( ); CREATE TEMPORARY TABLE tair_output (
  key STRING,
  step STRING,
  PRIMARY KEY (key) NOT ENFORCED
) WITH (
  'connector' = 'tair',
  'mode' = 'tairstring',
  'host' = '${tairHost}',
  'port' = '${tairPort}',
  'password' = '${password}',
  'incrMode' = 'dynamic_float',
  'incrValue' = 'step'
); INSERT INTO tair_output SELECT * FROM datagen_stream;
```

实时计算（流计算）

```
  v STRING,
  p STRING
) WITH ( ); CREATE TEMPORARY TABLE tair_output (
  key STRING,
  PRIMARY KEY (key) NOT ENFORCED
) WITH (
  'connector' = 'tair',
  'mode' = 'tairstring',
  'host' = '${tairHost}',
  'port' = '${tairPort}',
  'password' = '${password}',
  'incrMode' = 'float',
  'incrValue' = '11.11'
); INSERT INTO tair_output SELECT v FROM datagen_stream;
```

fieldExpire模式写入结果表数据示例

```
  v STRING,
  p STRING,
  s STRING
) WITH ( ); CREATE TEMPORARY TABLE tair_ouput (
 key STRING,
 field STRING,
 value STRING,
 PRIMARY KEY (key) NOT ENFORCED
) WITH (
  'connector' = 'tair',
  'mode' = 'tairhash',
  'host' = '${tairHost}',
  'port' = '${tairPort}',
  'password' = '${password}',
  'fieldExpireMode' = 'millisecond',
  'fieldExpireValue' = '1000'
); INSERT INTO tair_output SELECT v, p, s FROM datagen_stream;
```

实时计算（流计算）

### 云数据库RDS MySQL版

RDS MySQL基于阿里巴巴的MySQL源码分支，经过双十一高并发、大数据量的考验，拥有优良的性能。 RDS MySQL支持实例管理、账号管理、数据库管理、备份恢复、白名单、透明数据加密以及数据迁移等基本功能。

| 类别 | 详情 |
|---|---|
| 支持类型 | 结果表和维表 |
| 运行模式 | 流模式与批模式 |
| 数据格式 | 暂不适用 |
| 特有监控指标 | 维表：无结果表 numRecordsOut numRecordsOutPerSecond numBytesOut numBytesOutPerSecond currentSendTime numRecordsOutErrors |
| API种类 | SQL |
| 是否支持更新或删除结果表数据 | 是 |

**前提条件**

已设置IP白名单。

**使用限制**

语义上可以保证At-Least-Once，在结果表有主键的情况下，幂等可以保证数据的正确性。 推荐您使用最新版本的Flink（例如6.x以上），以获取最新的性能与稳定性优化。

**语法结构**

结果表实时计算（流计算）

```
CREATE TABLE rds_sink(
  id INT,
  num BIGINT,
  PRIMARY KEY(id) NOT ENFORCED
) WITH (
  'connector'='rds',
  'tableName'='your-table-name',
  'userName'='your-user-name',
  'password'='your-password',
  'url'='your-url'
);
```

| 说明 Flink RDS连接器写入数据库结果表原理：针对Flink Sink输出数据，拼接成一行SQL语句， 然后执行。对于没有主键的结果表，会执行 INSERT INTO table name (column1, _ |  |  |  |  |
|---|---|---|---|---|
|  |  | INSERT INTO table name (column1, _ |  |  |
| column2, ...) VALUES (value1, value2, ...)； |  |  | 语句。对于包含主键的结果表，会执 |  |
| 行 | INSERT INTO table name (column1, column2, ...) VALUES (value1, value2, ...) _ |  |  |  |
| ON DUPLICATE KEY UPDATE column1 = VALUES(column1), column2 = VALUES(column2), |  |  |  |  |
| ...; |  |  |  |  |

如果在RDS MySQL云数据库定义了自增主键，在Flink DDL中不应该声明该自增字段。数据写入过程中，数据库会自动填补该自增字段。Flink RDS连接器仅支持写入和删除带自增字段的数据，不支持更新。 维表

```
CREATE TABLE rds_dim(
 id1 INT,
 id2 VARCHAR
) WITH (
  'connector'='rds',
  'tableName'='your-table-name',
  'userName'='your-user-name',
  'password'='your-password',
  'url'='your-url'
  'cache'='NONE'
);
```

**WITH参数**

通用

| 参数 | 说明 | 数据类型 | 是否必填 | 默认值 | 备注 |
|---|---|---|---|---|---|
| connect or | 表类型。 | String | 是 | 无。 | 固定值为rds。 |
| tableNa me | 表名。 | String | 是 | 无。 | 无。 |

实时计算（流计算）

| userNa me | 用户名。 | String | 是 | 无。 | 无。 |
|---|---|---|---|---|---|
| passwor d | 密码。 | String | 是 | 无。 | 无。 |
| url | 表地址。 | String | 是 | 无。 | 请联系阿里云运维工程师获取。 |
| maxRet ryTimes | 查询维表或者写数据到结果表失败后，最多重试次数。 | Integer | 否 | 10 | 无。 |

结果表独有

| 参数 | 说明 | 数据类型 | 是否必填 | 默认值 | 备注 |
|---|---|---|---|---|---|
| batchSize | 一次批量写入的条数。 | Integer | 否 | 4096 | 无。 |
| bufferSize | 内存中缓存的最大数据条数。 batchSize 或 bufferSize 任一到达阈值都会触发数据写操作。 | Integer | 否 | 10000 | 需指定主键后，该参数才生效。 |
| flushInter valMs | flush内存缓冲区的时间间隔。表示如果缓存中的数据在等待指定时间后，依然没有达到输出条件 （batchSi ze或 bufferSize ），系统会自动写出缓存中的所有数据到结果表。 | Integer | 否 | 2000 | 在默认值为0的版本中，如果不配置该参数，可能导致少量数据永远无法写出到结果表。建议您采用更高版本的 Flink。 |

实时计算（流计算）

| ignoreDel ete | 是否忽略数据Delete 操作。 | Boolean | 否 | false | Flink SQL可能会生成数据 Delete操作，在多个输出节点根据主键同时更新同一张结果表的不同字段的场景下，可能导致数据结果不正确。 例如一个任务在删除了一条数据后，另一个任务又只更新了这条数据的部分字段， 其余未被更新的字段由于被删除，其值会变成null或默认值。通过将ignoreDelete设置为true，可以避免数据删除操作。 |
|---|---|---|---|---|---|
| connectio nMaxActiv e | 数据库连接池大小 | Integer | 否 | 40 | 如果出现获取连接超时的问题，可能是连接池不够用，可适当增大连接池的大小。 如果数据库能支持的最大并发连接比较小，可适当减小连接池大小或者减小作业节点并行度。 |

维表独有

| 参数 | 说明 | 数据类型 | 是否必填 | 默认值 | 备注 |
|---|---|---|---|---|---|
| cache | 维表缓存策略。 | Strin g | 否 | ALL | Flink RDS MySQL连接器支持None、LRU和ALL三种缓存策略。 |
| cacheSize | 缓存大小。 | Integ er | 否 | 100000 | 当选择LRU缓存策略后， 需要设置缓存大小。 当选择NONE或ALL缓存策略时，不必设置缓存大小。 |
| cacheTTL Ms | 缓存超时时间。 | Long | 否 | 如果cache配置为 NONE，则cacheTTLMs 可以不配置，表示缓存不超时。 如果cache配置为LRU， 则cacheTTLMs为缓存超时时间。默认不过期。 如果cache配置为ALL， 则cacheTTLMs为缓存加载时间。默认不重新加载。 | 单位为毫秒。 |

实时计算（流计算）

| maxJoinR ows | 主表中每一条数据查询维表时，匹配后最多返回的结果数。 | Integ er | 否 | 1024 | 进行Join时，主表输入一条数据，对应维表匹配后，会返回的结果总数受该参数限制。 如果您可以预估一条数据对应的维表数据最多为n条，则可以设置 maxJoinRows='n' ， 以确保实时计算匹配处理效率。 |
|---|---|---|---|---|---|

**类型映射**

| Flink字段类型 | RDS MySQL字段类型 |
|---|---|
| BOOLEAN | BOOLEAN |
| TINYINT | TINYINT |
| TINYINT(1) 说明仅维表支持该映射。 | BOOLEAN |
| SMALLINT | SMALLINT |
| SMALLINT | TINYINT UNSIGNED |
| INT | INT |
| INT | SMALLINT UNSIGNED |
| BIGINT | BIGINT |
| BIGINT | INT UNSIGNED |
| DECIMAL(20,0) | BIGINT UNSIGNED |
| FLOAT | FLOAT |
| DECIMAL | DECIMAL |

实时计算（流计算）

| DOUBLE | DOUBLE |
|---|---|
| DATE | DATE |
| TIME | TIME |
| TIMESTAMP | TIMESTAMP |
| VARCHAR | VARCHAR |
| VARBINARY | VARBINARY |

**使用示例**

结果表

```
 `name` VARCHAR,
 `age` INT
) WITH ( ); CREATE TEMPORARY TABLE rds_sink(
 `name` VARCHAR,
 `age` INT
) WITH (
  'connector'='rds',
  'password'='your-password',
  'tableName'='your-tablename',
  'url'='your-url',
  'userName'='your-username'
); INSERT INTO rds_sink SELECT * FROM datagen_source;
```

维表实时计算（流计算）

```
 a INT,
 b BIGINT,
 c STRING,
 `proctime` AS PROCTIME()
) WITH ( ); CREATE TEMPORARY TABLE rds_dim(
 a INT,
 b VARCHAR,
 c VARCHAR
) WITH (
 'connector'='rds',
 'password'='<yourPassword>',
 'tableName'='<yourTablename>',
 'url'='jdbc:mysql://xxx',
 'userName'='<yourUsername>'
);
 a INT,
 b STRING
) WITH ( ); SELECT T.a, H.b FROM datagen_source AS T JOIN rds_dim FOR SYSTEM_TIME AS OF T.`proctime` AS H ON T.a=H.a;
```

### JDBC

本文为您介绍如何使用JDBC连接器。

**背景信息**

此连接器为开源Flink的JDBC连接器，JDBC连接器提供了对MySQL、PostgreSQL和Oracle等常见的数据库读写支持。JDBC连接器支持的信息如下。

| 类别 | 详情 |
|---|---|
| 支持类型 | 源表、维表和结果表 |
| 运行模式 | 流模式和批模式 |
| 数据格式 | 暂不适用 |

实时计算（流计算）

| 特有监控指标 | 暂无 |
|---|---|
| API种类 | SQL |
| 是否支持更新或删除结果表数据 | 是 |

**前提条件**

连接的数据库和表都已被创建。

**使用限制**

仅实时计算引擎VVR 6.0.1及以上版本支持JDBC连接器。 JDBC源表为Bounded Source，表中数据读取完，对应的Task就会结束。如果需要捕获实时变更数据， 则请使用CDC连接器。 使用JDBC结果表连接PostgreSQL数据库时，需要数据库版本为PostgreSQL 9.5及以上。因为DDL中定义主键的情况下，PostgreSQL采用ON CONFLICT语法进行插入或更新，此语法需要PostgreSQL 9.5及以上版本才支持。 Flink中只提供了开源JDBC连接器的实现，不包含具体的数据库的Driver。在使用JDBC连接器时，需要手动上传目标数据库Driver的JAR包作为附加依赖文件。目前支持的Driver如下表所示。

| Driver | Group Id | Artifact Id |
|---|---|---|
| MySQL | mysql | mysql-connector-java |
| Oracle | com.oracle.database.jdbc | ojdbc8 |
| PostgreSQL | org.postgresql | postgresql |

如果您采用非列表中的JDBC Driver，则其正确性和可用性需要您自行充分测试并保证。 JDBC连接器在向MySQL结果表写入数据时，会将接收到的每条数据拼接成一条SQL去执行。对于包含主键的MySQL结果表，会拼接执行 `INSERT INTO table_name (column1, column2, ...) VALUES`

```
(value1, value2, ...) ON DUPLICATE KEY UPDATE column1 = VALUES(column1), column2 =
```

VALUES(column2), ...; 语句。需要注意的是，如果物理表存在除主键外的唯一索引约束，当插入两条主键不同但唯一索引相同的记录时，下游数据会因为唯一索引冲突导致数据覆盖引发数据丢失。

**语法结构**

实时计算（流计算）

```
CREATE TABLE jdbc_table (
  `id` BIGINT,
  `name` VARCHAR,
   PRIMARY KEY (id) NOT ENFORCED
) WITH (
  'connector' = 'jdbc',
  'url' = 'jdbc:xxx',
  'table-name' = '<yourTable>',
  'username' = '<yourUsername>',
  'password' = '<yourPassword>'
);
```

**WITH参数**

通用

| 参数 | 说明 | 数据类型 | 是否必填 | 默认值 | 备注 |
|---|---|---|---|---|---|
| connector | 表类型。 | String | 是 | 无 | 固定值为jdbc。 |
| url | 数据库的URL。 | String | 是 | 无 | 无。 |
| table-name | JDBC表的名称。 | String | 是 | 无 | 无。 |
| username | JDBC用户名称。 | String | 否 | 无 | 如果指定了username和 password中的任一参数，则两者必须都被指定。 |
| password | JDBC用户密码。 | String | 否 | 无 |  |

源表独有

| 参数 | 说明 | 数据类型 | 是否必填 | 默认值 | 备注 |
|---|---|---|---|---|---|
| scan.partitio n.column | 对输入进行分区的列名。 | String | 否 | 无 | 该列必须是数值类型、日期类型和时间戳类型等。关于分区扫描的详情请参见Partitioned Scan。 |
| scan.partitio n.num | 分区数。 | Integer | 否 | 无 | 无。 |
| scan.partitio n.lower- bound | 第一个分区的最小值。 | Integer | 否 | 无 | 无。 |

实时计算（流计算）

| scan.partitio n.upper- bound | 最后一个分区的最大值。 | Integer | 否 | 无 | 无。 |
|---|---|---|---|---|---|
| scan.fetch- size | 每次循环读取时，从数据库中获取的行数。 | Integer | 否 | 0 | 如果指定的值为0，则该配置项会被忽略。 |
| scan.auto- commit | 是否开启auto- commit。 | Boolea n | 否 | true | 无。 |

结果表独有

| 参数 | 说明 | 数据类型 | 是否必填 | 默认值 | 备注 |
|---|---|---|---|---|---|
| sink.buffer- flush.max- rows | flush数据前，缓存记录的最大值。 | Integer | 否 | 100 | 您可以设置为0来禁用它，即不再缓存记录，直接flush数据。 |
| sink.buffer- flush.interva l | flush数据的时间间隔。数据在Flink中缓存的时间超过该参数指定的时间后，异步线程将flush数据到数据库中。 | Duratio n | 否 | 1 s | 您可以设置为0来禁用它，即不再缓存记录，直接flush数据。 说明如果您需要完全异步地处理缓存的flush事件，则可以将sink.buffer- flush.max-rows设置为 0，并配置适当的flush时间间隔。 |
| sink.max- retries | 写入记录到数据库失败后的最大重试次数。 | Integer | 否 | 3 | 无。 |

维表独有

| 参数 | 说明 | 数据类型 | 是否必填 | 默认值 | 备注 |
|---|---|---|---|---|---|
| lookup.cach e.max-rows | 指定缓存的最大行数。如果超过该值， 则最老的行记录将会过期，会被新的记录替换掉。 | Integer | 否 | 无 | 默认情况下，维表Cache是未开启的。您可以设置lookup.cache.max- rows和lookup.cache.ttl参数来启用维表Cache。启用缓存时，采用的是LRU策略缓存。 |
| 文档版本：20260730 |  |  |  |  | 15 |

|  |  |  |  |  | 实时计算（流计算） |
|---|---|---|---|---|---|
| lookup.cach e.ttl | 指定缓存中每行记录的最大存活时间。如果某行记录超过该时间，则该行记录将会过期。 | Duratio n | 否 | 无 |  |
| lookup.cach e.caching- missing-key | 是否缓存空的查询结果。 | Boolea n | 否 | true | 参数取值如下： true（默认值）：缓存空的查询结果。 false：不缓存空的查询结果。 |
| lookup.max- retries | 查询数据库失败的最大重试次数。 | Integer | 否 | 3 | 无。 |

PostgreSQL独有

| 参数 | 说明 | 数据类型 | 是否必填 | 默认值 | 备注 |
|---|---|---|---|---|---|
| source.exte nd- type.enable d | 作为源表和维表时， 是否允许读取JSONB 和UUID拓展类型，并映射到Flink支持的类型。 | Boolea n | 否 | false | 参数取值如下： true：支持读取和映射拓展类型。 false（默认值）：不支持读取和映射拓展类型。 |

**类型映射**

| MySQL类型 | Oracle类型 | PostgreSQL类型 | FlinkSQL类型 |
|---|---|---|---|
| TINYINT | 无 | 无 | TINYINT |
| SMALLINT TINYINT UNSIGNED | 无 | SMALLINT INT2 SMALLSERIAL SERIAL2 | SMALLINT |
| INT MEDIUMINT SMALLINT UNSIGNED | 无 | INTEGER SERIAL | INT |
| BIGINT INT UNSIGNED | 无 | BIGINT BIGSERIAL | BIGINT |

实时计算（流计算）

| BIGINT UNSIGNED | 无 | 无 | DECIMAL(20, 0) |
|---|---|---|---|
| BIGINT | 无 | BIGINT | BIGINT |
| FLOAT | BINARY FLOAT _ | REAL FLOAT4 | FLOAT |
| DOUBLE DOUBLE PRECISION | BINARY DOUBLE _ | FLOAT8 DOUBLE PRECISION | DOUBLE |
| NUMERIC(p, s) DECIMAL(p, s) | SMALLINT FLOAT(s) DOUBLE PRECISION REAL NUMBER(p, s) | NUMERIC(p, s) DECIMAL(p, s) | DECIMAL(p, s) |
| BOOLEAN TINYINT(1) | 无 | BOOLEANcan | BOOLEAN |
| DATE | DATE | DATE | DATE |
| TIME [(p)] | DATE | TIME [(p)] [WITHOUT TIMEZONE] | TIME [(p)] [WITHOUT TIMEZONE] |
| DATETIME [(p)] | TIMESTAMP [(p)] [WITHOUT TIMEZONE] | TIMESTAMP [(p)] [WITHOUT TIMEZONE] | TIMESTAMP [(p)] [WITHOUT TIMEZONE] |
| CHAR(n) VARCHAR(n) TEXT | CHAR(n) VARCHAR(n) CLOB | CHAR(n) CHARACTER(n) VARCHAR(n) CHARACTER VARYING(n) TEXT JSONB UUID | STRING |

实时计算（流计算）

| BINARY VARBINARY BLOB | RAW(s) BLOB | BYTEA | BYTES |
|---|---|---|---|
| 无 | 无 | ARRAY | ARRAY |

**使用示例**

源表

```
CREATE TEMPORARY TABLE jdbc_source (
  `id` INT,
  `name` VARCHAR
) WITH (
  'connector' = 'jdbc',
  'url' = 'jdbc:xxx',
  'table-name' = '<yourTable>',
  'username' = '<yourUsername>',
  'password' = '<yourPassword>'
);
  `id` INT,
  `name` VARCHAR
) WITH ( ); INSERT INTO blackhole_sink SELECT * FROM jdbc_source ;
```

结果表

```
  `name` VARCHAR,
  `age` INT
) WITH ( ); CREATE TEMPORARY TABLE jdbc_sink (
  `name` VARCHAR,
  `age` INT
) WITH (
  'connector' = 'jdbc',
  'url' = 'jdbc:xxxx',
  'table-name' = '<yourTable>',
  'username' = '<yourUsername>',
  'password' = '<yourPassword>'
); INSERT INTO jdbc_sink SELECT * FROM datagen_source;
```

实时计算（流计算） 维表

```
 `id` INT,
 `data` BIGINT,
 `proctime` AS PROCTIME()
) WITH ( ); CREATE TEMPORARY TABLE jdbc_dim (
  `id` INT,
  `name` VARCHAR
) WITH (
  'connector' = 'jdbc',
  'url' = 'jdbc:xxx',
  'table-name' = '<yourTable>',
  'username' = '<yourUsername>',
  'password' = '<yourPassword>'
);
  `id` INT,
  `data` BIGINT,
  `name` VARCHAR
) WITH ( ); SELECT T.`id`,T.`data`, H.`name` JOIN jdbc_dim FOR SYSTEM_TIME AS OF T.proctime AS H ON T.id = H.id;
```

### MongoDB

**背景信息**

MongoDB是一个面向文档的非结构化数据库，能够简化应用程序的开发及扩展。MongoDB连接器支持的信息如下：

| 类别 | 详情 |
|---|---|
| 支持类型 | 源表、维表和结果表 |
| 运行模式 | 仅支持流模式 |

实时计算（流计算）

| 特有监控指标 | 源表 numBytesIn numBytesInPerSecond numRecordsIn numRecordsInPerSecond numRecordsInErrors currentFetchEventTimeLag currentEmitEventTimeLag watermarkLag sourceIdleTime 维表和结果表：无。 |
|---|---|
| API 种类 | DataStream和SQL |
| 是否支持更新或删除结果表数据 | 是 |

**特色功能**

MongoDB的CDC源表，即MongoDB的流式源表，会先读取数据库的历史全量数据，并平滑切换到 oplog读取上，保证不多读一条也不少读一条。即使发生故障，也能保证通过Exactly Once语义处理数据。MongoDB CDC支持通过Change Stream API高效地捕获MongoDB的数据库和集合中的文档变更，监控文档的插入、修改、替换、删除事件，并将其转换为Flink能够处理的Changelog数据流。作为源表，支持以下功能特性： 支持利用MongoDB 3.6新增的Change Stream API，更高效地监控变化。 精确一次处理：在作业任何阶段失败都能保证Exactly-once语义。 支持全增量一体化监测：支持快照阶段完成后自动切换为增量读取阶段。 支持多种启动模式： initial模式：在第一次启动时对受监视的数据库表执行初始快照，并继续读取最新的oplog。 latest-offset模式：首次启动时，从不对受监视的数据库表执行快照，连接器仅从oplog 的结尾处开始读取，这意味着连接器只能读取在连接器启动之后的数据更改。 timestamp：跳过快照阶段，从指定的时间戳开始读取oplog事件，需要MongoDB >= 4.0。

**前提条件**

CDC源表 CDC连接器支持通过副本集或分片集架构模式读取阿里云云数据库MongoDB版的数据，也支持读取自使用MongoDB CDC连接器的基础功能时，必须开启待监控的MongoDB数据库的副本集（Replica Set）功能，详情请参见Replication。 如需使用Full Changelog事件流功能，则需开启MongoDB数据库的前像后像（Pre- and Postimages）记录功能，详情请参见Document Preimages。 实时计算（流计算） 如果启用了MongoDB的鉴权功能，则需要使用具有以下数据库权限的MongoDB用户： splitVector权限 listCollections权限 collStats权限 find权限 changeStream权限 config.collections和config.chunks集合的访问权限维表和结果表已设置IP白名单

**使用限制**

CDC源表结果表实时计算Flink VVR 8.0.5以下版本仅支持插入数据。 实时计算Flink VVR 8.0.5及以上版本，结果表中声明主键时，支持插入、更新和删除数据，未声明主键时仅支持插入数据。 维表

**语法结构**

```
CREATE TABLE tableName(
  _id STRING,
  [columnName dataType,]*
  PRIMARY KEY(_id) NOT ENFORCED
) WITH (
  'connector' = 'mongodb',
  'hosts' = 'localhost:27017',
  'username' = 'mongouser',
  'password' = '${secret_values.password}',
  'database' = 'testdb',
  'collection' = 'testcoll'
```

)

**说明**

在创建CDC源表时，您必须声明 `_id STRING` 列，并将其作为唯一的主键。

**WITH参数**

通用实时计算（流计算）

| 参数 | 说明 | 数据类型 | 是否必填 | 默认值 | 备注 |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|
| connector | 连接器名称。 | String | 是 | 无 | 作为源表： 实时计算引擎VVR 8.0.4及之前版本，填写为mongodb-cdc。 实时计算引擎VVR 8.0.5及之后版本，填写为mongodb或mongodb- cdc。 作为维表或结果表时，固定值为 mongodb。 |  |  |  |  |
| uri | MongoDB连接uri。 | String | 否 | 无 | 说明参数 uri 与 hosts 必须指定其中之一。若指定 uri ，则无需指定 scheme 、 hosts 、 use rname 、 password 、 conne ctor.options 。当两者均指定时将使用 uri 进行连接。 |  |  |  |  |
|  |  |  |  |  |  |  | use |  |  |
|  |  |  |  |  |  | conne |  |  |  |
| hosts | MongoDB所在的主机名称。 | String | 否 | 无 | 可以使用英文逗号（ , ）分隔提供多个主机名。 |  |  |  |  |
| scheme | MongoDB使用的连接协议。 | String | 否 | mong odb | 可选的取值包括： mongodb ：代表使用默认的 MongoDB协议进行连接 mongodb+srv ：代表使用DNS SRV记录协议进行连接 |  |  |  |  |
| username | 连接到 MongoDB时使用的用户名。 | String | 否 | 无 | 开启身份验证功能时，必须配置该参数。 |  |  |  |  |
| password | 连接到 MongoDB时使用的密码。 | String | 否 | 无 | 开启身份验证功能时，必须配置该参数。 |  |  |  |  |
| database | MongoDB数据库名称。 | String | 否 | 无 | 作为源表时，数据库名称支持正则表达式匹配。 不配置该参数代表监控全部数据库。 |  |  |  |  |

|  |  |  |  | scheme |  |  |
|---|---|---|---|---|---|---|
|  |  |  | rname |  |  |  |
|  |  |  |  |  | 、 |  |

实时计算（流计算）

| collection | MongoDB集合名称。 | String | 否 | 无 | 作为源表时，集合名称支持正则表达式匹配。 重要如果您要监控的集合名称中包含正则表达式特殊字符，则必须提供完全限定的名字空间（数据库名称. 集合名称），否则无法捕获对应集合的变更。 不配置该参数代表监控全部集合。 |
|---|---|---|---|---|---|
| connectio n.options | MongoDB侧的连接参数。 | String | 否 | 无 | 使用 & 分隔的 key=value 式额外连接参数。例如 connectTimeoutMS=12000&socketTi meoutMS=13000。 |

源表独有

| 参数 | 说明 | 数据类型 | 是否必填 | 默认值 | 备注 |
|---|---|---|---|---|---|
| scan.start up.mode | MongoDB CDC的启动模式。 | String | 否 | initia l | 参数取值如下： initial：从初始位点开始拉取全部数据。 latest-offset：从当前位点开始拉取变更数据。 timestamp：从指定的时间戳开始拉取变更数据。 详情请参见Startup Properties。 |
| scan.start up.timest amp- millis | 指定位点消费的起始时间戳。 | Long | 取决于 scan.startup. mode的取值： initial：否 latest- offset：否 timestamp ：是 | 无 | 参数格式为自Linux Epoch时间戳以来的毫秒数。 仅适用于 timestamp 启动模式。 |
| initial.sna pshotting. queue.siz e | 进行初始快照时的队列大小限制。 | Integer | 否 | 102 40 | 仅在 scan.startup.mode 选项设置为 initial 时生效。 |
| batch.siz e | 游标的批处理大小。 | Integer | 否 | 102 4 | 无。 |

实时计算（流计算）

| poll.max. batch.siz e | 同一批处理的最多变更文档数量。 | Integer | 否 | 102 4 | 此参数控制流处理时一次拉取最多变更文档的个数。取值越大，连接器内部分配的缓冲区越大。 |
|---|---|---|---|---|---|
| poll.await .time.ms | 两次拉取数据之间的时间间隔。 | Integer | 否 | 100 0 | 单位为毫秒。 |
| heartbeat .interval. ms | 发送心跳包的时间间隔。 | Integer | 否 | 0 | 单位为毫秒。 MongoDB CDC连接器主动向数据库发送心跳包来保证回溯状态最新。设置为0代表永不发送心跳包。 重要对于更新不频繁的集合，强烈建议设定此选项。 |
| scan.incr emental.s napshot.e nabled | 是否启用并行模式进行初始快照。 | Boolean | 否 | false | 实验性功能。 |
| scan.incr emental.s napshot.c hunk.size. mb | 并行模式读取快照时的分片大小。 | Integer | 否 | 64 | 实验性功能。 单位为MB。 仅在启用并行快照时生效。 |
| scan.full- changelo g | 产生完整的 Full Changelog 事件流。 | Boolean | 否 | false | 实验性功能。 说明 MongoDB数据库需要为6.0及以上版本，并且已开启前像后像功能，开启方法请参见Document Preimages。 |
| scan.flatt en- nested- columns. enabled | 是否将以 . 分隔的字段名解析为嵌套BSON 文档读取。 | Boolean | 否 | false | 若开启，在如下示例的BSON文档中， col 字段在schema中名称为 nested.col 。 {"nested":{"col":true}} 说明仅VVR 8.0.5及以上版本支持该参数。 |

实时计算（流计算）

| scan.prim itive-as- string | 是否将BSON 文档中的原始类型都解析为字符串类型。 | Boolean | 否 | false | 说明仅VVR 8.0.5及以上版本支持该参数。 |
|---|---|---|---|---|---|

维表独有

| 参数 | 说明 | 数据类型 | 是否必填 | 默认值 | 备注 |
|---|---|---|---|---|---|
| lookup.cac he | Cache策略。 | String | 否 | NON E | 目前支持以下两种缓存策略： None：无缓存。 Partial：只在外部数据库中查找数据时缓存。 |
| lookup.ma x-retries | 查询数据库失败的最大重试次数。 | Integer | 否 | 3 | 无。 |
| lookup.retr y.interval | 如果查询数据库失败，重试的时间间隔。 | Duratio n | 否 | 1s | 无。 |
| lookup.part ial- cache.expir e-after- access | 缓存中的记录最长保留时间。 | Duratio n | 否 | 无 | 支持时间单位ms、s、min、h和d。 使用该配置时 lookup.cache 必须设置为 PARTIAL 。 |
| lookup.part ial- cache.expir e-after- write | 在记录写入缓存后该记录的最大保留时间。 | Duratio n | 否 | 无 | 使用该配置时 lookup.cache 必须设置为 PARTIAL 。 |
| lookup.part ial- cache.max- rows | 缓存的最大条数。超过该值， 最旧的行将过期。 | Long | 否 | 无 | 使用该配置时 lookup.cache 必须设置为 PARTIAL 。 |
| lookup.part ial- cache.cach e-missing- key | 在物理表中未关联到数据时，是否缓存空记录。 | Boolean | 否 | True | 使用该配置时 lookup.cache 必须设置为 PARTIAL 。 |

|  | lookup.cache |
|---|---|
| PARTIAL |  |

|  | lookup.cache |
|---|---|
| PARTIAL |  |

|  | lookup.cache |
|---|---|
| PARTIAL |  |

|  | lookup.cache |
|---|---|
| PARTIAL |  |

结果表独有实时计算（流计算）

| 参数 | 说明 | 数据类型 | 是否必填 | 默认值 | 备注 |
|---|---|---|---|---|---|
| sink.buffer- flush.max- rows | 每次按批写入数据时的最大记录数。 | Integer | 否 | 1000 | 无。 |
| sink.buffer- flush.interv al | 写入数据的刷新间隔。 | Duration | 否 | 1s | 无。 |
| sink.deliver y- guarantee | 写入数据时的语义保证。 | String | 否 | at- least- once | 可选的取值包括： none at-least-once 说明目前不支持exactly- once。 |
| sink.max- retries | 写入数据库失败时的最大重试次数。 | Integer | 否 | 3 | 无。 |
| sink.retry.i nterval | 写入数据库失败时的重试时间间隔。 | Duration | 否 | 1s | 无。 |
| sink.parall elism | 自定义sink并行度。 | Integer | 否 | 空 | 无。 |

**类型映射**

CDC源表

| BSON类型 | Flink SQL类型 |
|---|---|
| Int32 | INT |
| Int64 | BIGINT |
| Double | DOUBLE |
| Decimal128 | DECIMAL(p, s) |
| Boolean | BOOLEAN |

实时计算（流计算）

| Date Timestamp | DATE |
|---|---|
| Date Timestamp | TIME |
| DateTime | TIMESTAMP(3) TIMESTAMP LTZ(3) _ |
| Timestamp | TIMESTAMP(0) TIMESTAMP LTZ(0) _ |
| String ObjectId UUID Symbol MD5 JavaScript Regex | STRING |
| Binary | BYTES |
| Object | ROW |
| Array | ARRAY |
| DBPointer | ROW<$ref STRING, $id STRING> |
| GeoJSON | Point: ROW<type STRING, coordinates ARRAY<DOUBLE>> Line: ROW<type STRING, coordinates ARRAY<ARRAY< DOUBLE>>> |

维表和结果表

| BSON类型 | Flink SQL类型 |
|---|---|
| Int32 | INT |
| Int64 | BIGINT |
| Double | DOUBLE |

实时计算（流计算）

| Decimal128 | DECIMAL |
|---|---|
| Boolean | BOOLEAN |
| DateTime | TIMESTAMP LTZ(3) _ |
| Timestamp | TIMESTAMP LTZ(0) _ |
| String ObjectId | STRING |
| Binary | BYTES |
| Object | ROW |
| Array | ARRAY |

**使用示例**

CDC源表实时计算（流计算）

```
CREATE TEMPORARY TABLE mongo_source (
  `_id` STRING, --must be declared
  name STRING,
  weight DECIMAL,
  tags ARRAY<STRING>,
  price ROW<amount DECIMAL, currency STRING>,
  suppliers ARRAY<ROW<name STRING, address STRING>>,
  db_name STRING METADATA FROM 'database_name' VIRTUAL,
  collection_name STRING METADATA VIRTUAL,
  op_ts TIMESTAMP_LTZ(3) METADATA VIRTUAL,
  PRIMARY KEY(_id) NOT ENFORCED
) WITH (
  'connector' = 'mongodb',
  'hosts' = 'dds-bp169b982fc25****.mongodb.rds.aliyuncs.com:3717,dds-
bp169b982fc25****.mongodb.rds.aliyuncs.com:3717,',
  'username' = 'root',
  'password' = '${secret_values.password}',
  'database' = 'flinktest',
  'collection' = 'flinkcollection',
  'scan.incremental.snapshot.enabled' = 'true',
  'scan.full-changelog' = 'true'
); CREATE TEMPORARY TABLE productssink (
  name STRING,
  weight DECIMAL,
  tags ARRAY<STRING>,
  price_amount DECIMAL,
  suppliers_name STRING,
  db_name STRING,
  collection_name STRING,
  op_ts TIMESTAMP_LTZ(3)
) WITH (
  'connector' = 'print',
  'logger' = 'true'
); INSERT INTO productssink SELECT
  name,
  weight,
  tags,
  price.amount,
  suppliers[1].name,
  db_name,
  collection_name,
  op_ts
FROM
  mongo_source;
```

维表实时计算（流计算）

```
  id STRING,
  a int,
  b BIGINT,
  `proctime` AS PROCTIME()
) WITH ( ); CREATE TEMPORARY TABLE mongo_dim (
  `_id` STRING,
  name STRING,
  weight DECIMAL,
  tags ARRAY<STRING>,
  price ROW<amount DECIMAL, currency STRING>,
  suppliers ARRAY<ROW<name STRING, address STRING>>,
  PRIMARY KEY(_id) NOT ENFORCED
) WITH (
  'connector' = 'mongodb',
  'hosts' = 'dds-bp169b982fc25****.mongodb.rds.aliyuncs.com:3717,dds-
bp169b982fc25****.mongodb.rds.aliyuncs.com:3717,',
  'username' = 'root',
  'password' = '${secret_values.password}',
  'database' = 'flinktest',
  'collection' = 'flinkcollection',
  'lookup.cache' = 'PARTIAL',
  'lookup.partial-cache.expire-after-access' = '10min',
  'lookup.partial-cache.expire-after-write' = '10min',
  'lookup.partial-cache.max-rows' = '100'
);
  name STRING,
  weight DECIMAL,
  tags ARRAY<STRING>,
  price_amount DECIMAL,
  suppliers_name STRING
) WITH (
  'connector' = 'print',
  'logger' = 'true'
); SELECT
  T.id,
  T.a,
  T.b,
  H.name
FROM
  datagen_source AS T JOIN mongo_dim FOR SYSTEM_TIME AS OF T.`proctime` AS H ON T.id
= H._id;
```

结果表实时计算（流计算）

```
  `_id` STRING,
  name STRING,
  weight DECIMAL,
  tags ARRAY<STRING>,
  price ROW<amount DECIMAL, currency STRING>,
  suppliers ARRAY<ROW<name STRING, address STRING>>
) WITH ( ); CREATE TEMPORARY TABLE mongo_sink (
  `_id` STRING,
  name STRING,
  weight DECIMAL,
  tags ARRAY<STRING>,
  price ROW<amount DECIMAL, currency STRING>,
  suppliers ARRAY<ROW<name STRING, address STRING>>,
  PRIMARY KEY(_id) NOT ENFORCED
) WITH (
  'connector' = 'mongodb',
  'hosts' = 'dds-bp169b982fc25****.mongodb.rds.aliyuncs.com:3717,dds-
bp169b982fc25****.mongodb.rds.aliyuncs.com:3717,',
  'username' = 'root',
  'password' = '${secret_values.password}',
  'database' = 'flinktest',
  'collection' = 'flinkcollection'
); INSERT INTO mongo_sink SELECT * FROM datagen_source;
```

**元数据**

| 元数据key | 元数据类型 | 描述 |
|---|---|---|
| database name _ | STRING NOT NULL | 包含该文档的数据库名。 |
| collection name _ | STRING NOT NULL | 包含该文档的集合名。 |
| op ts _ | TIMESTAMP LTZ(3) _ NOT NULL | 该文档在数据库中的变更时间，如果该文档来自表的存量历史数据而不是从ChangeStream中获取，则该值总是0。 |

MongoDB 6.0 之前的版本默认不会提供变更前文档及被删除文档的数据，在未开启变更前后像记录功能时，利用已有信息只能实现 Upsert 语义（即缺失了 Update Before 数据条目）。但在 Flink 中许多有用的算子操作都依赖完整的 Insert、Update Before、Update After、Delete 变更流。 实时计算（流计算） 为了补充缺失的变更前事件，目前 Flink SQL Planner 会自动为 Upsert 类型的数据源生成一个 ChangelogNormalize 节点，该节点会在 Flink 状态中缓存所有文档的当前版本快照，在遇到被更新或删除的文档时，查表即可得知变更前的状态，但该算子节点需要存储体积巨大的状态数据。 MongoDB 6.0版本支持开启数据库的前像后像（Pre- and Post-images）记录功能，详情可参考Document Preimages。开启该功能后，MongoDB会在每次变更发生时，在一个特殊的集合中记录文档变更前后的完整状态。此时在作业中启用 `scan.full-changelog` 配置项，MongoDB CDC会从变更文档记录中生成Update After记录，从而支持产生完整事件流，消除了对ChangelogNormalize节点的依赖。

**Mongo CDC DataStream API**

**重要**

通过DataStream的方式读写数据时，则需要使用对应的DataStream连接器连接Flink。 创建DataStream API程序并使用MongoDBSource。代码示例如下：

```
  .hosts("mongo.example.com:27017")
  .username("mongouser")
  .password("mongopasswd")
  .databaseList("testdb")
  .collectionList("testcoll")
  .startupOptions(StartupOptions.initial())
  .deserializer(new JsonDebeziumDeserializationSchema())
  .build();
```

**说明**

在使用DataStream API时，若要启用增量快照功能，请在构造MongoDBSource数据源时，使

```
用 com.ververica.cdc.connectors.mongodb.source 包中的 MongoDBSource#builder() ；否则，使用 com.ververica.cdc.connectors.mongodb 中的 MongoDBSource#builder() 。
```

| 参数 | 说明 |
|---|---|
| hosts | 需要连接的MongoDB数据库的主机名称。 |

实时计算（流计算）

| username | MongoDB数据库服务的用户名。 说明若MongoDB服务器未启用鉴权，则无需配置此参数。 |
|---|---|
| password | MongoDB数据库服务的密码。 说明若MongoDB服务器未启用鉴权，则无需配置此参数。 |
| databaseList | 需要监控的MongoDB数据库名称。 说明数据库名称支持正则表达式以读取多个数据库的数据，您可以使用 .* 匹配所有数据库。 |
| collectionList | 需要监控的MongoDB集合名称。 说明集合名称支持正则表达式以读取多个集合的数据，您可以使用 .* 匹配所有集合。 |
| startupOptions | 选择MongoDB CDC的启动模式。 合法的取值包括： StartupOptions.initial() 从初始位点开始拉取全部数据 StartupOptions.latest-offset() 从当前位点开始拉取变更数据 StartupOptions.timestamp() 从指定的时间戳开始拉取变更数据详情请参见Startup Properties。 |
| deserializer | 反序列化器，将SourceRecord类型记录反序列化到指定类型。参数取值如下： MongoDBConnectorDeserializationSchema：将Upsert模式下产生的SourceRecord转成Flink Table API或SQL API内部数据结构RowData。 MongoDBConnectorFullChangelogDeserializationSchema：将Full Changelog模式下产生的SourceRecord转成Flink Table或SQL内部数据结构RowData。 JsonDebeziumDeserializationSchema：将SourceRecord转成JSON格式的String。 |

实时计算（流计算）

### 数据总线DataHub

**背景信息**

阿里云流数据处理平台DataHub是流式数据（Streaming Data）的处理平台，提供对流式数据的发布 （Publish）、订阅（Subscribe）和分发功能，让您可以轻松构建基于流式数据的分析和应用。

**说明**

DataHub兼容Kafka协议，因此您可以使用Kafka连接器（不包括Upsert Kafka）来访问DataHub。 DataHub连接器支持的信息如下。

| 类别 | 详情 |
|---|---|
| 支持类型 | 结果表和源表 |
| 运行模式 | 流模式和批模式 |
| 数据格式 | 暂不适用 |
| 特有监控指标 | 暂无 |
| API种类 | Datastream和SQL |
| 是否支持更新或删除目标 Topic数据 | 不支持更新和删除目标Topic数据，只支持插入数据。 |

**语法结构**

```
CREATE TEMPORARY TABLE datahub_input (
  `time` BIGINT,
  `sequence`  STRING METADATA VIRTUAL,
  `shard-id` BIGINT METADATA VIRTUAL,
  `system-time` TIMESTAMP METADATA VIRTUAL
) WITH (
  'connector' = 'datahub',
  'subId' = '<yourSubId>',
  'endPoint' = '<yourEndPoint>',
  'project' = '<yourProjectName>',
  'topic' = '<yourTopicName>',
  'accessId' = '${secret_values.ak_id}',
  'accessKey' = '${secret_values.ak_secret}'
);
```

**WITH参数**

实时计算（流计算） 通用

| 参数 | 说明 | 数据类型 | 是否必填 | 默认值 | 备注 |
|---|---|---|---|---|---|
| connector | 表类型。 | String | 是 | 无 | 固定值为datahub。 |
| endPoint | 消费端点信息。 | String | 是 | 无 | 请联系阿里云运维工程师获取。 |
| project | 项目。 | String | 是 | 无 | 无。 |
| topic | 主题。 | String | 是 | 无 | 如果您填写的topic是blob类型（一种无类型的非结构化数据的存储方式），则在Flink消费时，表定义中必须有且只有一个 VARBINARY类型的字段。 |
| accessId | 阿里云账号的 AccessKey ID。 | String | 是 | 无 | 无。 |
| accessKey | 阿里云账号的 AccessKey Secret。 | String | 是 | 无 | 无。 |
| retryTime out | 最大持续重试时间。 | Integer | 否 | 18000 00 | 单位毫秒，通常不作修改。 |
| retryInterv al | 重试间隔。 | Integer | 否 | 1000 | 单位毫秒，通常不作修改。 |
| enableSch emaRegist ry | 是否打开 Schema注册。 | Boolean | 否 | false | 您需要设置为true。 |
| Compress Type | 读写的压缩策略。 | String | 否 | lz4 | lz4 （默认值）：使用lz4压缩。 deflate：使用deflate压缩。 ""（空字符串）：表示关闭数据压缩。 说明仅VVR 6.0.5及以上版本支持指定 CompressType参数。 |

源表独有实时计算（流计算）

| 参数 | 说明 | 数据类型 | 是否必填 | 默认值 | 备注 |
|---|---|---|---|---|---|
| subId | 订阅ID。 | String | 是 | 无 | 无。 |
| maxFetchS ize | 单次读取条数。 | Integer | 否 | 50 | 影响读性能的参数，调大可以增加吞吐。 |
| maxBuffer Size | 异步读取的最大缓存数据条数。 | Integer | 否 | 50 | 影响读性能的参数，调大可以增加吞吐。 |
| fetchLates tDelay | 数据源没有数据时，sleep 的时间。 | Integer | 否 | 500 | 单位毫秒。在数据源频繁没有数据的情况下，影响吞吐，建议调小。 |
| lengthChe ck | 单行字段条数检查策略。 | String | 否 | NONE | NONE（默认值）： 解析出的字段数大于定义字段数时，按从左到右的顺序，取定义字段数量的数据。 解析出的字段数小于定义字段数时，跳过该行数据。 SKIP：解析出的字段数和定义字段数不同时跳过该行数据。 EXCEPTION：解析出的字段数和定义字段数不同时提示异常。 PAD：按从左到右顺序填充。 解析出的字段数大于定义字段数时，按从左到右的顺序，取定义字段数量的数据。 解析出的字段数小于定义字段数时，按从左到右的顺序，在行尾用Null填充缺少的字段。 |
| columnErr orDebug | 是否打开调试开关。 | Boolean | 否 | false | false（默认值）：关闭调试功能。 true：打开调试开关，打印解析异常的日志。 |
| startTime | 消费日志的开始时间。 | String | 否 | 当前时间 | 格式为yyyy-MM-dd hh:mm:ss。 |
| endTime | 消费日志的结束时间。 | String | 否 | 无 | 格式为yyyy-MM-dd hh:mm:ss。 |

结果表独有实时计算（流计算）

| 参数 | 说明 | 数据类型 | 是否必填 | 默认值 | 备注 |
|---|---|---|---|---|---|
| batchCount | 每次批量写入数据的数量。 | Integer | 否 | 500 | 影响写性能，调大可以增加吞吐，但是会增大延迟。 |
| batchSize | 每次批量写入数据的大小。 | Integer | 否 | 5120 00 | 单位Byte，影响写性能，调大可以增加吞吐，但是会增大延迟。 |
| flushInterval | 攒批写入数据的时间。 | Integer | 否 | 5000 | 单位毫秒，影响写性能，调大可以增加吞吐，但是增大延迟。 |
| hashFields | 指定列名后， 相同列的值会写入到同一个 Shard。 | String | 否 | null， 即随机写 | 可以指定多个列值，用逗号(,)分割，例如 hashFields=a,b 。 |
| timeZone | 数据的时区。 | String | 否 | 无 | 影响TimeStamp等带时区数据的转换。 |
| schemaVersi on | 向注册的 Schema里写入的 version。 | Integer | 否 | -1 | 您需要指定该参数。 |

**类型映射**

| Flink字段类型 | DataHub字段类型 |
|---|---|
| TINYINT | TINYINT |
| BOOLEAN | BOOLEAN |
| INTEGER | INTEGER |
| BIGINT | BIGINT |
| BIGINT | TIMESTAMP |
| TIMESTAMP |  |
| FLOAT | FLOAT |

实时计算（流计算）

| DOUBLE | DOUBLE |
|---|---|
| DECIMAL | DECIMAL |
| VARCHAR | STRING |
| SMALLINT | SMALLINT |
| VARBINARY | BLOB |

**属性字段**

| 字段名 | 字段类型 | 说明 |
|---|---|---|
| shard-id | BIGINT METADATA VIRTUAL | Shard的ID。 |
| sequence | STRING METADATA VIRTUAL | 数据顺序。 |
| system-time | TIMESTAMP METADATA VIRTUAL | 系统时间。 |

**使用示例**

源表实时计算（流计算）

```
CREATE TEMPORARY TABLE datahub_input (
  `time` BIGINT,
  `sequence`  STRING METADATA VIRTUAL,
  `shard-id` BIGINT METADATA VIRTUAL,
  `system-time` TIMESTAMP METADATA VIRTUAL
) WITH (
  'connector' = 'datahub',
  'subId' = '<yourSubId>',
  'endPoint' = '<yourEndPoint>',
  'project' = '<yourProjectName>',
  'topic' = '<yourTopicName>',
  'accessId' = '${secret_values.ak_id}',
  'accessKey' = '${secret_values.ak_secret}'
); CREATE TEMPORARY TABLE test_out (
  `time` BIGINT,
  `sequence`  STRING,
  `shard-id` BIGINT,
  `system-time` TIMESTAMP
) WITH (
  'connector' = 'print',
  'logger' = 'true'
); INSERT INTO test_out SELECT
  `time`,
  `sequence` ,
  `shard-id`,
  `system-time`
FROM datahub_input;
```

结果表实时计算（流计算）

```
CREATE TEMPORARY table datahub_source(
  name VARCHAR
) WITH (
  'connector'='datahub',
  'endPoint'='<endPoint>',
  'project'='<yourProjectName>',
  'topic'='<yourTopicName>',
  'subId'='<yourSubId>',
  'accessId'='${secret_values.ak_id}',
  'accessKey'='${secret_values.ak_secret}',
  'startTime'='2018-06-01 00:00:00'
); CREATE TEMPORARY table datahub_sink(
  name varchar
) WITH (
  'connector'='datahub',
  'endPoint'='<endPoint>',
  'project'='<yourProjectName>',
  'topic'='<yourTopicName>',
  'accessId'='${secret_values.ak_id}',
  'accessKey'='${secret_values.ak_secret}',
  'batchSize'='512000',
  'batchCount'='500'
); INSERT INTO datahub_sink SELECT
  LOWER(name)
from datahub_source;
```

**Datastream API**

**重要**

通过DataStream的方式读写数据时，则需要使用对应的DataStream连接器连接Flink。

**DataHub源表**

Flink提供了SourceFunction的实现类DatahubSourceFunction来读取DataHub表数据。以下为读取 DataHub表数据的示例。 实时计算（流计算）

```
StreamExecutionEnvironment env = StreamExecutionEnvironment.getExecutionEnvironment(); env.setParallelism(1);
```

`//DataHub`连接配置。

```xml
DatahubSourceFunction datahubSource =
    new DatahubSourceFunction(
    <yourEndPoint>,
    <yourProjectName>,
    <yourTopicName>,
    <yourSubId>,
    <yourAccessId>,
    <yourAccessKey>,
    "public",
```

`<enableSchemaRegistry>, //` 是否开启`schemaRegistry`，一般填`false`即可。

```java
    <yourStartTime>,
    <yourEndTime>
    );
datahubSource.setRequestTimeout(30 * 1000); datahubSource.enableExitAfterReadFinished(); env.addSource(datahubSource)
    .map((MapFunction<RecordEntry, Tuple2<String, Long>>) this::getStringLongTuple2)
    .print();
env.execute(); private Tuple2<String, Long> getStringLongTuple2(RecordEntry recordEntry) {
    Tuple2<String, Long> tuple2 = new Tuple2<>();
    TupleRecordData recordData = (TupleRecordData) (recordEntry.getRecordData());
    tuple2.f0 = (String) recordData.getField(0);
    tuple2.f1 = (Long) recordData.getField(1);
    return tuple2;
}
```

**DataHub结果表**

Flink提供了OutputFormatSinkFunction的实现类DatahubSinkFunction将数据写入DataHub。以下为将数据写入DataHub的示例。 实时计算（流计算）

```
StreamExecutionEnvironment env = StreamExecutionEnvironment.getExecutionEnvironment();
```

`//DataHub`连接配置。

```xml
env.generateSequence(0, 100)
    .map((MapFunction<Long, RecordEntry>) aLong -> getRecordEntry(aLong, "default:"))
    .addSink(
    new DatahubSinkFunction<>(
       <yourEndPoint>,
       <yourProjectName>,
       <yourTopicName>,
       <yourSubId>,
       <yourAccessId>,
       <yourAccessKey>,
       "public",
```

`<enableSchemaRegistry>, //` 是否开启`schemaRegistry`，一般填`false`即可。 `<schemaVersion> //` 如果开启了`schemaRegistry`，写入的时候需要指定`schemaVersion`，其他情况填 0即可。

```java
       );
env.execute(); private RecordEntry getRecordEntry(Long message, String s) {
    RecordSchema recordSchema = new RecordSchema();
    recordSchema.addField(new Field("f1", FieldType.STRING));
    recordSchema.addField(new Field("f2", FieldType.BIGINT));
    recordSchema.addField(new Field("f3", FieldType.DOUBLE));
    recordSchema.addField(new Field("f4", FieldType.BOOLEAN));
    recordSchema.addField(new Field("f5", FieldType.TIMESTAMP));
    recordSchema.addField(new Field("f6", FieldType.DECIMAL));
    RecordEntry recordEntry = new RecordEntry();
    TupleRecordData recordData = new TupleRecordData(recordSchema);
    recordData.setField(0, s + message);
    recordData.setField(1, message);
    recordEntry.setRecordData(recordData);
    return recordEntry;
}
```

**XML**

Maven中央库中已经放置了DataHub DataStream连接器。

```xml
<dependency>
    <groupId>com.alibaba.ververica</groupId>
    <artifactId>ververica-connector-datahub</artifactId>
    <version>${vvr-version}</version>
</dependency>
```

### StarRocks

**背景信息**

StarRocks是新一代极速全场景MPP（Massively Parallel Processing）数据仓库，致力于构建极速和统 StarRocks兼容MySQL协议，可以使用MySQL客户端和常用BI工具对接StarRocks来分析数据。 实时计算（流计算） 对数据表进行水平划分并以多副本存储。 集群规模可以灵活伸缩，支持10 PB级别的数据分析。 支持MPP框架，并行加速计算。 支持多副本，具有弹性容错能力。 Flink连接器内部的结果表是通过缓存并批量由Stream Load导入实现，源表是通过批量读取数据实现。

| 类别 | 详情 |
|---|---|
| 支持类型 | 源表、维表和结果表 |
| 运行模式 | 流模式和批模式 |
| 数据格式 | JSON和CSV |
| 特有监控指标 | 暂无 |
| API种类 | Datastream和SQL |
| 是否支持更新或删除结果表数据 | 是 |

**特色功能**

EMR的StarRocks支持CTAS&CDAS功能，CTAS可以实现单表的结构和数据同步，CDAS可以实现整库同步或者同一库中的多表结构和数据同步。

**前提条件**

已创建StarRocks集群，包括EMR的StarRocks或基于ECS的云上自建StarRocks。

**使用限制**

StarRocks连接器仅支持at-least-once和exactly-once语义。

**语法结构**

实时计算（流计算）

```
CREATE TABLE USER_RESULT(
 name VARCHAR,
 score BIGINT
 ) WITH (
 'connector' = 'starrocks',
 'jdbc-url'='jdbc:mysql://fe1_ip:query_port,fe2_ip:query_port,fe3_ip:query_port?xxxxx',
 'load-url'='fe1_ip:http_port;fe2_ip:http_port;fe3_ip:http_port',
 'database-name' = 'xxx',
 'table-name' = 'xxx',
 'username' = 'xxx',
 'password' = 'xxx'
 );
```

**WITH参数**

| 类型 | 参数 | 说明 | 数据类型 | 是否必填 | 默认值 | 备注 |
|---|---|---|---|---|---|---|
| 通用 | connector | 表类型。 | Strin g | 是 | 无 | 固定值为starrocks。 |
|  | jdbc-url | JDBC连接的URL。 | Strin g | 是 | 无 | 请联系阿里云运维工程师获取。 |
|  | database- name | StarRocks数据库名称。 | Strin g | 是 | 无 | 无。 |
|  | table-name | StarRocks表名称。 | Strin g | 是 | 无 | 无。 |
|  | username | StarRocks连接用户名。 | Strin g | 是 | 无 | 无。 |
|  | password | StarRocks连接密码。 | Strin g | 是 | 无 | 无。 |
|  | starrocks.cr eate.table. properties | StarRocks表属性。 | Strin g | 否 | 无 | 设置数据表初始属性，如引擎、副本数等。例如，'starrocks.create.table. properties' = 'buckets 8'，'starrocks.create.table. properties' = 'replication num=1'。 _ |
|  | scan-url | 数据扫描的url。 | Strin g | 否 | 无 | 请联系阿里云运维工程师获取。 |

| 实时计算（ | 流计算） Flink存算分离版开发指南·连接器 |  |  |  |  |  |
|---|---|---|---|---|---|---|
| 源表独有 |  |  |  |  |  |  |
|  | scan.conne ct.timeout- ms | flink-connector- starrocks连接 StarRocks的时间上限。 超过该时间上限，将报错。 | Strin g | 否 | 1000 | 单位为毫秒。 |
|  | scan.param s.keep- alive-min | 查询任务的保活时间。 | Strin g | 否 | 10 | 无。 |
|  | scan.param s.query- timeout-s | 查询任务的超时时间。 如果超过该时间，仍未返回查询结果，则停止查询任务。 | Strin g | 否 | 600 | 单位为秒。 |
|  | scan.param s.mem- limit-byte | BE节点中单个查询的内存上限。 | Strin g | 否 | 1073 7418 24（ 1 GB） | 单位为字节。 |
|  | scan.max- retries | 查询失败时的最大重试次数。 超过该数量上限，则将报错。 | Strin g | 否 | 1 | 无。 |
| 结果表独有 | load-url | 数据导入的URL。 | Strin g | 是 | 无 | 请联系阿里云运维工程师获取。 |
|  | sink.seman tic | 数据写入语义。 | Strin g | 否 | at- least - once | 取值如下： at-least-once（默认值）：至少一次。 exactly-once：恰好一次。 |
|  | sink.buffer- flush.max- bytes | Buffer可容纳的最大数据量。 | Strin g | 否 | 9437 1840 （90 MB） | 取值范围为64 MB~10 GB。 |
|  | sink.buffer- flush.max- rows | Buffer可容纳的最大数据行数。 | Strin g | 否 | 5000 00 | 取值范围为 64,000~5000,000。 |
|  | sink.buffer- flush.interv al-ms | Buffer刷新时间间隔。 | Strin g | 否 | 3000 00 | 取值范围为1000毫秒 ~3600000毫秒。 |

实时计算（流计算）

|  | sink.max- retries | 最大重试次数。 | Strin g | 否 | 1 | 取值范围为0~10。 |
|---|---|---|---|---|---|---|
|  | sink.connec t.timeout- ms | 连接到starrocks的超时时间。 | Strin g | 否 | 1000 | 取值范围为100~60000。单位为毫秒。 |
|  | sink.proper ties.* | 结果表属性。 | Strin g | 否 | 无 | Stream Load的参数控制 Stream Load导入行为。例如，参数 sink.properties.format表示 Stream Load所导入的数据格式，如CSV或者JSON。 |
| 维表独有 | lookup.cac he.enabled | 是否启用维表缓存机制。 | Bool ean | 否 | true | 取值如下： true：启用。首次读取表数据后缓存至内存，后续请求在缓存有效期内直接使用内存数据，减少IO开销。 false：关闭。每次查询均直接访问数据源。 |

**类型映射**

| StarRocks字段类型 | Flink字段类型 |
|---|---|
| NULL | NULL |
| BOOLEAN | BOOLEAN |
| TINYINT | TINYINT |
| SMALLINT | SMALLINT |
| INT | INT |
| BIGINT | BIGINT |
| LARGEINT | STRING |
| FLOAT | FLOAT |
| DOUBLE | DOUBLE |

实时计算（流计算）

| DATE | DATE |
|---|---|
| DATETIME | TIMESTAMP |
| DECIMAL | DECIMAL |
| DECIMALV2 | DECIMAL |
| DECIMAL32 | DECIMAL |
| DECIMAL64 | DECIMAL |
| DECIMAL128 | DECIMAL |
| CHAR | CHAR |
| VARCHAR | STRING |

**代码示例**

实时计算（流计算）

```
CREATE TEMPORARY TABLE IF NOT EXISTS `runoob_tbl_source` (
  `runoob_id` BIGINT NOT NULL,
  `runoob_title` STRING NOT NULL,
  `runoob_author` STRING NOT NULL,
  `submission_date` DATE NULL
) WITH (
  'connector' = 'starrocks',
  'jdbc-url' = 'jdbc:mysql://ip:9030',
  'scan-url' = 'ip:18030',
  'database-name' = 'db_name',
  'table-name' = 'table_name',
  'password' = 'xxxxxxx',
  'username' = 'xxxxx'
); CREATE TEMPORARY TABLE IF NOT EXISTS `runoob_tbl_sink` (
  `runoob_id` BIGINT NOT NULL,
  `runoob_title` STRING NOT NULL,
  `runoob_author` STRING NOT NULL,
  `submission_date` DATE NULL
  PRIMARY KEY(`runoob_id`)
  NOT ENFORCED
) WITH (
  'jdbc-url' = 'jdbc:mysql://ip:9030',
  'connector' = 'starrocks',
  'load-url' = 'ip:18030',
  'database-name' = 'db_name',
  'table-name' = 'table_name',
  'password' = 'xxxxxxx',
  'username' = 'xxxx',
  'sink.buffer-flush.interval-ms' = '5000'
); INSERT INTO runoob_tbl_sink SELECT * FROM runoob_tbl_source;
```

### 日志服务SLS

**背景信息**

日志服务是针对日志类数据的一站式服务。日志服务可以帮助您快捷地完成数据采集、消费、投递以及查询分析，提升运维和运营效率，建立海量日志处理能力。 SLS连接器支持的信息如下。

| 类别 | 详情 |
|---|---|
| 支持类型 | 源表和结果表 |
| 运行模式 | 仅支持流模式 |

实时计算（流计算）

| 特有监控指标 | 暂不适用 |
|---|---|
| 数据格式 | 暂无 |
| API种类 | SQL |
| 是否支持更新或删除结果表数据 | 不支持更新和删除结果表数据，只支持插入数据。 |

**特色功能**

SLS连接器源表支持直接读取消息的属性字段，支持的属性字段如下。

| 字段名 | 字段类型 | 字段说明 |
|---|---|---|
| source __ __ | STRING METADATA VIRTUAL | 消息源。 |
| topic __ __ | STRING METADATA VIRTUAL | 消息主题。 |
| timestamp __ __ | BIGINT METADATA VIRTUAL | 日志时间。 |
| tag __ __ | MAP<VARCHAR, VARCHAR> METADATA VIRTUAL | 消息TAG。 对于属性 " tag : receive time ":"1616742274" ， ' __ __ __ _ __ __ receive time ' 和'1616742274'会被作为KV对，记录在 _ __ Map中，在SQL中通过 tag [' receive time '] 的 __ __ __ _ __ 方式访问。 |

|  |  | " tag : receive time ":"1616742274" __ __ __ _ __ |
|---|---|---|
|  | receive time ' _ __ |  |

**前提条件**

已创建日志服务Project和Logstore。

**使用限制**

SLS连接器仅保证At-Least-Once语义。 建议不要设置Source并发度大于Shard个数，不仅会造成资源浪费，且在8.0.5及更低版本中，如果后续 Shard数目发生变化，自动Failover功能可能会失效，造成部分Shard不被消费。

**语法结构**

实时计算（流计算）

```
CREATE TABLE sls_table(
  a INT,
  b INT,
  c VARCHAR
) WITH (
  'connector' = 'sls',
  'endPoint' = '<yourEndPoint>',
  'project' = '<yourProjectName>',
  'logStore' = '<yourLogStoreName>',
  'accessId' = '${secret_values.ak_id}',
  'accessKey' = '${secret_values.ak_secret}'
);
```

**WITH参数**

通用

| 参数 | 说明 | 数据类型 | 是否必填 | 默认值 | 备注 |
|---|---|---|---|---|---|
| connector | 表类型。 | String | 是 | 无 | 固定值sls。 |
| endPoint | EndPoint地址。 | String | 是 | 无 | 请联系阿里云运维工程师获取。 |
| project | SLS项目名称。 | String | 是 | 无 | 无。 |
| logStore | SLS LogStore 或 metricstore 名称。 | String | 是 | 无 | logStore和metricstore是相同的消费方式。 |
| accessId | 阿里云账号的 AccessKey ID。 | String | 是 | 无 | 无。 |
| accessKey | 阿里云账号的 AccessKey Secret。 | String | 是 | 无 | 无。 |

源表独有

| 参数 | 说明 | 数据类型 | 是否必填 | 默认值 | 备注 |
|---|---|---|---|---|---|

实时计算（流计算）

| startTi me | 消费日志的开始时间。 | String | 否 | 当前时间 | 格式为yyyy-MM-dd hh:mm:ss。 说明 startTime和stopTime基于SLS中的 receive time 属性，而非 __ _ __ timestamp 属性。 __ __ |
|---|---|---|---|---|---|
| stopTim e | 消费日志的结束时间。 | String | 否 | 无 | 格式为yyyy-MM-dd hh:mm:ss。 说明如期望日志消费到结尾时退出Flink程序，需要同时设置 exitAfterFinish=true。 |
| consum erGroup | 消费组名称。 | String | 否 | 无 | 消费组用于记录消费进度。您可以自定义消费组名，无固定格式。 说明不支持通过相同的消费组进行多作业的协同消费。不同的Flink作业应该设置不同的消费组。如果不同的Flink作业使用相同的消费组，它们将会消费全部数据。这是因为在Flink消费SLS的数据时，并不会经过SLS消费组进行分区分配，因此导致各个消费者独立消费各自的消息，即使消费组是相同的。 |
| consum eFromC heckpoi nt | 是否从指定的消费组中保存的 Checkpoin t开始消费日志。 | String | 否 | false | 参数取值如下： true：必须同时指定消费组，Flink程序会从消费组中保存的Checkpoint开始消费日志，如果该消费组没有对应的 Checkpoint，则从startTime配置值开始消费。 false（默认值）：不从指定的消费组中保存的Checkpoint开始消费日志。 说明仅实时计算引擎VVR 6.0.5及以上版本支持该参数。 |
| directM ode | 是否使用 SLS的直连模式。 | String | 否 | false | 参数取值如下： true：使用该功能。 false（默认）：禁用该功能。 |
| maxRet ries | 读取SLS失败后重试次数。 | String | 否 | 3 | 无。 |

实时计算（流计算）

| batchG etSize | 单次请求读取 logGroup 的个数。 | String |  | 否 | 100 | batchGetSize设置不能超过1000，否则会报错。 |  |
|---|---|---|---|---|---|---|---|
| exitAfte rFinish | 在数据消费完成后，Flink程序是否退出。 | String |  | 否 | false | 参数取值如下： true：数据消费完后，Flink程序退出。 false（默认）：数据消费完后，Flink程序不退出。 |  |
| query | SLS消费预处理语句。 | String |  |  |  | 通过使用query参数，您可以在消费SLS数据之前对其进行过滤，以避免将所有数据都消费到Flink中，从而实现节约成本和提高处理速度的目的。 例如 'query' = '*\| where request method = ''GET''' 表示在 _ Flink读取SLS数据前，先匹配出 request method字段值等于get的数据。 _ query需使用日志服务SPL语言。 重要仅实时计算引擎VVR 8.0.1及以上版本支持该参数。 公测阶段免费，后续可能会在产生日志服务SLS费用。 |  |
|  |  |  |  |  |  |  | 'query' = '*\| where |
|  |  |  |  |  |  | request method = ''GET''' _ |  |
|  |  |  |  | 否 | 无 |  |  |

结果表独有

| 参数 | 说明 | 数据类型 | 是否必填 | 默认值 | 备注 |
|---|---|---|---|---|---|
| topicField | 指定字段名，该字段的值会覆盖 topic 属性字段 __ __ 的值，表示日志的主题。 | String | 否 | 无 | 该参数值是表中已存在的字段之一。 |
| timeField | 指定字段名，该字段的值会覆盖 timestamp 属 __ __ 性字段的值，表示日志写入时间。 | String | 否 | 当前时间 | 该参数值是表中已存在的字段之一， 且字段类型必须为INT。如果未指定，则默认填充当前时间。 |

实时计算（流计算）

| sourceFiel d | 指定字段名，该字段的值会覆盖 source 属性字 __ __ 段的值，表示日志的来源地，例如产生该日志机器的IP地址。 | String | 否 | 无 | 该参数值是表中已存在的字段之一。 |
|---|---|---|---|---|---|
| partitionFi eld | 指定字段名，数据写入时会根据该列值计算Hash值，Hash值相同的数据会写入同一个shard。 | String | 否 | 无 | 如果未指定，则每条数据会随机写入当前可用的Shard中。 |
| buckets | 当指定 partitionField时， 根据Hash值重新分组的个数。 | String | 否 | 64 | 该参数的取值范围是[1, 256]，且必须是2的整数次幂。同时，buckets 个数应当大于等于Shard个数，否则会出现部分Shard没有数据写入的情况。 说明仅实时计算引擎VVR 6.0.5及以上版本支持该参数。 |
| flushInter valMs | 触发数据写入的时间周期。 | String | 否 | 2000 | 单位为毫秒。 |
| writeNullP roperties | 是否将null值作为空字符串写入SLS。 | Boolean | 否 | true | 参数取值如下： true（默认值）：将null值作为空字符串写入日志。 false：计算结果为null的字段不会写入到日志中。 说明仅实时计算引擎VVR 8.0.6及以上版本支持该参数。 |

**类型映射**

| Flink字段类型 | SLS字段类型 |
|---|---|
| BOOLEAN |  |
| VARBINARY |  |

|  | 实时计算（流计算） |
|---|---|
|  | STRING |
| VARCHAR |  |
| TINYINT |  |
| INTEGER |  |
| BIGINT |  |
| FLOAT |  |
| DOUBLE |  |
| DECIMAL |  |

**代码示例**

```
CREATE TEMPORARY TABLE sls_input(
  `time` BIGINT,
  url STRING,
  dt STRING,
  float_field FLOAT,
  double_field DOUBLE,
  boolean_field BOOLEAN,
  `__topic__` STRING METADATA VIRTUAL,
  `__source__` STRING METADATA VIRTUAL,
  `__timestamp__` STRING METADATA VIRTUAL,
   __tag__ MAP<VARCHAR, VARCHAR> METADATA VIRTUAL,
  proctime as PROCTIME()
) WITH (
  'connector' = 'sls',
  'endpoint' ='cn-hangzhou.log.aliyuncs.com',
  'accessId' = '${secret_values.ak_id}',
  'accessKey' = '${secret_values.ak_secret}',
  'starttime' = '2023-08-30 00:00:00',
  'project' ='sls-test',
  'logstore' ='sls-input'
); CREATE TEMPORARY TABLE sls_sink(
  `time` BIGINT,
  url STRING,
  dt STRING,
  float_field FLOAT,
  double_field DOUBLE,
  boolean_field BOOLEAN,
  `__topic__` STRING,
  `__source__` STRING,
```

`

```
` BIGINT ,
```

实时计算（流计算） `__`

```
p__
```

,

```
  receive_time BIGINT
) WITH (
  'connector' = 'sls',
  'endpoint' ='cn-hangzhou.log.aliyuncs.com',
  'accessId' = '${ak_id}',
  'accessKey' = '${ak_secret}',
  'project' ='sls-test',
  'logstore' ='sls-output'
); INSERT INTO sls_sink SELECT
 `time`,
  url,
  dt,
  float_field,
  double_field,
  boolean_field,
  `__topic__` ,
  `__source__` ,
  `__timestamp__` ,
  cast(__tag__['__receive_time__'] as bigint) as receive_time
FROM sls_input;
```

**DataStream API**

**重要**

通过DataStream的方式读写数据时，则需要使用对应的DataStream连接器连接Flink，Maven中央库中已经放置了SLS DataStream连接器。 读取SLS 实时计算引擎VVR提供SourceFunction的实现类SlsSourceFunction，用于读取SLS，读取SLS的示例如下。

```java
public class SlsDataStreamSource {
    public static void main(String[] args) throws Exception {
        // Sets up the streaming execution environment
        final StreamExecutionEnvironment env =
StreamExecutionEnvironment.getExecutionEnvironment();
        // Creates and adds SLS source and sink.
        env.addSource(createSlsSource())
                .map(SlsDataStreamSource::convertMessages)
                .print();
        env.execute("SLS Stream Source");
    }
    private static SlsSourceFunction createSlsSource() {
        SLSAccessInfo accessInfo = new SLSAccessInfo();
        accessInfo.setEndpoint("yourEndpoint");
        accessInfo.setProjectName("yourProject");
```

f

```
("
```

S `")` 实时计算（流计算）

```java
        accessInfo.setLogstore("yourLogStore");
        accessInfo.setAccessId("yourAccessId");
        accessInfo.setAccessKey("yourAccessKey");
        // The batch get size must be given.
        accessInfo.setBatchGetSize(10);
        // Optional parameters
        accessInfo.setConsumerGroup("yourConsumerGroup");
        accessInfo.setMaxRetries(3);
        // time to start consuming, set to current time.
        int startInSec = (int) (new Date().getTime() / 1000);
        // time to stop consuming, -1 means never stop.
        int stopInSec = -1;
        return new SlsSourceFunction(accessInfo, startInSec, stopInSec);
    }
    private static List<String> convertMessages(SourceRecord input) {
        List<String> res = new ArrayList<>();
        for (FastLogGroup logGroup : input.getLogGroups()) {
            int logsCount = logGroup.getLogsCount();
            for (int i = 0; i < logsCount; i++) {
                FastLog log = logGroup.getLogs(i);
                int fieldCount = log.getContentsCount();
                for (int idx = 0; idx < fieldCount; idx++) {
                    FastLogContent f = log.getContents(idx);
                    res.add(String.format("key: %s, value: %s", f.getKey(),
f.getValue()));
                }
            }
        }
        return res;
    }
}
```

写入SLS 提供OutputFormat的实现类SLSOutputFormat，用于写入SLS。写入SLS的示例如下。 实时计算（流计算）

```java
public class SlsDataStreamSink {
    public static void main(String[] args) throws Exception {
        StreamExecutionEnvironment env =
StreamExecutionEnvironment.getExecutionEnvironment();
        env.fromSequence(0, 100)
                .map((MapFunction<Long, SinkRecord>) aLong -> getSinkRecord(aLong))
                .addSink(createSlsSink())
                .name(SlsDataStreamSink.class.getSimpleName());
        env.execute("SLS Stream Sink");
    }
    private static OutputFormatSinkFunction createSlsSink() {
        Configuration conf = new Configuration();
        conf.setString(SLSOptions.ENDPOINT, "yourEndpoint");
        conf.setString(SLSOptions.PROJECT, "yourProject");
        conf.setString(SLSOptions.LOGSTORE, "yourLogStore");
        conf.setString(SLSOptions.ACCESS_ID, "yourAccessId");
        conf.setString(SLSOptions.ACCESS_KEY, "yourAccessKey");
        SLSOutputFormat outputFormat = new SLSOutputFormat(conf);
        return new OutputFormatSinkFunction<>(outputFormat);
    }
    private static SinkRecord getSinkRecord(Long seed) {
        SinkRecord record = new SinkRecord();
        LogItem logItem = new LogItem((int) (System.currentTimeMillis() / 1000));
        logItem.PushBack("level", "info");
        logItem.PushBack("name", String.valueOf(seed));
        logItem.PushBack("message", "it's a test message for " + seed.toString());
        record.setContent(logItem);
        return record;
    }
}
```

### 流式数据湖仓Paimon

流式数据湖仓Paimon连接器推荐配合Paimon Catalog使用，本文为您介绍如何使用流式数据湖仓Paimon 连接器。

**背景信息**

Apache Paimon是一种流批统一的湖存储格式，支持高吞吐的写入和低延迟的查询。目前阿里云开源大数据平台E-MapReduce常见的计算引擎（例如Flink、Spark、Hive或Trino）都与Paimon有着较为完善的集成度。您可以借助Apache Paimon快速地在HDFS或者云端OSS上构建自己的数据湖存储服务，并接入上述计算引擎实现数据湖的分析，详情请参见Apache Paimon。

| 类别 | 详情 |
|---|---|
| 支持类型 | 源表、维表和结果表 |

实时计算（流计算）

| 运行模式 | 流模式和批模式 |
|---|---|
| 数据格式 | 暂不支持 |
| 特有监控指标 | 暂无 |
| API种类 | SQL |
| 是否支持更新或删除结果表数据 | 是 |

**特色功能**

目前Apache Paimon提供以下核心能力： 基于HDFS或者对象存储构建低成本的轻量级数据湖存储服务。 支持在流模式与批模式下读写大规模数据集。 支持分钟级到秒级数据新鲜度的批查询和OLAP查询。 支持消费与产生增量数据，可作为传统的离线数仓和新型的流式数仓的各级存储。 支持预聚合数据，降低存储成本与下游计算压力。 支持回溯历史版本的数据。 支持高效的数据过滤。 支持表结构变更。

**语法结构**

如果您在Paimon Catalog中创建Paimon表，则无需指定 `connector` 参数，此时创建Paimon表的语法结构如下。

```
CREATE TABLE `<your-paimon-catalog>`.`<your-db>`.paimon_table (
  id BIGINT,
  data STRING,
  PRIMARY KEY (id) NOT ENFORCED
) WITH (
  ...
);
```

**说明**

如果您已在Paimon Catalog中创建了Paimon表，后续无需再次创建表即可直接使用。 如果您在其他Catalog中创建Paimon临时表，则需要指定connector参数与Paimon表的存储路径path， 此时创建Paimon表的语法结构如下。 实时计算（流计算）

```
CREATE TEMPORARY TABLE paimon_table (
  id BIGINT,
  data STRING,
  PRIMARY KEY (id) NOT ENFORCED
) WITH (
  'connector' = 'paimon',
  'path' = '<path-to-paimon-table-files>',
```

`'auto-create' = 'true', --` 如果指定路径不存在`Paimon`表数据文件，则会自动创建文件。

```
  ...
);
```

**WITH参数**

| 参数 | 说明 | 数据类型 | 是否必填 | 默认值 | 备注 |
|---|---|---|---|---|---|
| connect or | 表类型。 | String | 否 | 无 | 如果在Paimon Catalog中创建Paimon表， 则无需填写。 如果在其他Catalog中创建Paimon临时表， 则固定值为 paimon 。 |
| path | 表存储路径。 | String | 否 | 无 | 如果在Paimon Catalog中创建Paimon表， 则无需填写。 如果在其他Catalog中创建Paimon临时表， 则为表在HDFS或OSS中的存储目录。 |
| auto- create | 创建Paimon临时表时，若指定路径不存在Paimon 表文件，是否自动创建文件。 | Boolean | 否 | fals e | 参数取值如下： false（默认）：如果指定路径不存在Paimon 表文件，则报错。 true：如果指定路径不存在，则Flink系统自动创建Paimon表文件。 |
| bucket | 每个分区的分桶数。 | Integer | 否 | 1 | 写入Paimon表的数据将按 bucket-key 打散至每个bucket中。 说明建议每个Bucket的数据量在5 GB以下。 |

实时计算（流计算）

| bucket- key | 分桶关键列。 | String |  |  |  | 指定将写入Paimon表的数据按哪些列的值打散至不同的Bucket中。 列名之间用英文逗号（,）分隔，例如 'bucket-key' = 'order id,cust id' 会将数据按order id _ _ _ 列和cust id列的值进行打散。 _ 说明如果该参数未填写，则按primary key进行打散。 如果Paimon表未指定primary key，则按所有列的值进行打散。 |  |
|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  | 'bucket-key' = |
|  |  |  |  |  |  | 'order id,cust id' _ _ |  |
|  |  |  |  | 否 | 无 |  |  |
| changel og- produce r | 增量数据产生机制。 | String |  | 否 | non e | Paimon可以为任意输入数据流产生完整的增量数据（所有的update after数据都有对应的 _ update before数据），方便下游消费者。增量 _ 数据产生机制的可选值如下： none（默认值）：不额外产生增量数据。下游仍然可以流读Paimon表，但读到的增量数据是不完整的（只有update after数据，没 _ 有对应的update before数据）。 _ input：将输入数据流双写至增量数据文件中，作为增量数据。 full-compaction：每次Full Compaction产生完整的增量数据。 lookup：每次commit snapshot前产生完整的增量数据。 |  |
| full- compac tion.del ta- commit s | Full Compaction最大间隔。 | Integer |  | 否 | 无 | 该参数指定了每commit snapshot多少次之后，一定会进行一次Full Compaction。 |  |
| lookup. cache- max- memor y-size | Paimon维表的内存缓存大小。 | String |  | 否 | 256 MB | 该参数值会同时影响维表缓存大小和lookup changelog-producer的缓存大小，两个机制的缓存大小都由该参数配置。 |  |
| merge- engine | 相同primary key数据的合并机制。 | String |  | 否 | ded upli cate | 参数取值如下： deduplicate：仅保留最新一条。 partial-update：用最新数据中非null的列更新相同primary key的现有数据，其它列保持不变。 aggregation：通过指定聚合函数进行预聚合。 |  |

实时计算（流计算）

| partial- update. ignore- delete | 在partial- update合并机制中，是否忽略 delete消息。 | Boolean | 否 | fals e | 参数取值如下： true：忽略delete消息。 false：碰到delete消息，Flink系统会报错。 说明并非所有场景下忽略delete消息都是正确的，您需要结合自己的实际场景配置该参数。 |
|---|---|---|---|---|---|
| partitio n.defaul t-name | 分区默认名称。 | String | 否 | D __ EFA ULT PA _ RTIT ION _ _ | 如果分区列的值为null或空字符串，将会采用该默认名称作为分区名。 |
| partitio n.expira tion- check- interval | 多久检查一次分区过期。 | String | 否 | 1h | 无。 |
| partitio n.expira tion- time | 分区的过期时长。 | String | 否 | 无 | 当一个分区的存活时长超过该值时，该分区将会过期，默认永不过期。 |
| partitio n.timest amp- formatt er | 将时间字符串转换为时间戳的格式串。 | String | 否 | 无 | 设置从分区值提取分区存活时长的格式。 |
| partitio n.timest amp- pattern | 将分区值转换为时间字符串的格式串。 | String | 否 | 无 | 设置从分区值提取分区存活时长的格式。 |
| scan.bo unded. waterm ark | 当Paimon源表产生的数据的 watermark超过该值时，Paimon 源表将会结束产生数据。 | Long | 否 | 无 | 无。 |
| scan.m ode | 指定Paimon源表的消费位点。 | String | 否 | defa ult | 无。 |

实时计算（流计算）

| scan.sn apshot- id | 指定Paimon源表从哪个snapshot 开始消费。 | Integer | 否 | 无 | 无。 |
|---|---|---|---|---|---|
| scan.ti mestam p-millis | 指定Paimon源表从哪个时间点开始消费。 | Integer | 否 | 无 | 无。 |
| snapsh ot.num- retaine d.max | 至多保留几个最新Snapshot不过期。 | Integer | 否 | 214 748 364 7 | 只要满足该配置或snapshot.time-retained其中之一，并同时满足snapshot.num- retained.min，就会触发Snapshot过期。 |
| snapsh ot.num- retaine d.min | 至少保留几个最新Snapshot不过期。 | Integer | 否 | 10 | 无。 |
| snapsh ot.time- retaine d | Snapshot产生多久以后会过期。 | String | 否 | 1h | 只要满足该配置或snapshot.num- retained.max其中之一，并同时满足 snapshot.num-retained.min，就会触发 snapshot过期。 |
| write- mode | Paimon表的写入模式。 | String | 否 | cha nge- log | 参数取值如下： change-log：Paimon表支持根据primary key进行数据的插入、删除和更新。 append-only：Paimon表只接受数据的插入，且不支持primary key。该模式比 change-log模式更加高效。 |
| scan.inf er- paralleli sm | 是否自动推断 Paimon源表的并发度。 | Boolean | 否 | fals e | 参数取值如下： true：将会根据分桶数自动推断Paimon源表的并发度。 false：按VVP配置的默认并发。如果是专家模式就按用户配置的并发。 |
| scan.pa rallelis m | Paimon源表的并发度。 | Integer | 否 | 无 | 无。 |
| sink.par allelism | Paimon结果表的并发度。 | Integer | 否 | 无 | 无。 |

**说明**

更多配置项详情请参见Apache Paimon官方文档。

**特色功能详解**

实时计算（流计算）

**数据新鲜度与一致性保证**

Paimon结果表使用两阶段提交协议，在每次Flink作业的checkpoint期间提交写入的数据，因此数据新鲜度即为Flink作业的checkpoint间隔。每次提交将会产生至多两个snapshot。 当两个Flink作业同时写入一张Paimon表时，如果两个作业的数据没有写入同一个分桶，则能保证 serializable级别的一致性。如果两个作业的数据写入了同一个分桶，则只能保证snapshot isolation级别的一致性。也就是说，表中的数据可能混合了两个作业的结果，但不会有数据丢失。

**数据合并机制**

当Paimon结果表收到多条具有相同primary key的数据时，为了保持primary key的唯一性，Paimon结果表会将这些数据合并成一条数据。通过指定 `merge-engine` 参数，您可以指定数据合并的具体行为。数据合并机制详情如下表所示。

|  | 合并机制 | 详情 |  |
|---|---|---|---|
|  | 去重 （Deduplic ate） | 去重机制（deduplicate）是默认的数据合并机制。对于多条具有相同primary key的数据，Paimon 结果表仅会保留最新一条数据，并丢弃其它具有primary key的数据。 说明如果最新一条数据是一条delete消息，所有具有该primary key的数据都将被丢弃。 |  |
|  | 部分更新 （Partial Update） | 通过指定部分更新机制（partial-update），您可以通过多条消息对数据进行逐步更新，并最终得到完整的数据。具体来说，具有相同primary key的新数据将会覆盖原来的数据，但值为null的列不会进行覆盖。 例如，假设Paimon结果表按顺序收到了以下三条数据： <1, 23.0, 10, NULL> <1, NULL, NULL, 'This is a book'> <1, 25.2, NULL, NULL> 第一列是primary key，则最终结果为<1, 25.2, 10, 'This is a book'>。 说明如果需要流读partial-update的结果，必须将 changelog-producer 参数设置为 lookup或full-compaction。 partial-update无法处理delete消息。您可以设置 partial-update.ignore- delete 参数以忽略delete消息。 |  |
|  |  |  | delete |

| partial-update.ignore- |  |
|---|---|

实时计算（流计算）

|  | 预聚合 （Aggregat ion） | 部分场景下，可能只关心聚合后的值。预聚合机制（aggregation）将具有相同primary key的数据根据您指定的聚合函数进行聚合。对于不属于primary key的每一列，都需要通过 fields. <field-name>.aggregate-function 指定一个聚合函数，否则该列将默认使用 last non null value 聚合函数。例如，考虑以下Paimon表的定义。 _ _ _ CREATE TABLE MyTable ( product id BIGINT, _ price DOUBLE, sales BIGINT, PRIMARY KEY (product id) NOT ENFORCED _ ) WITH ( 'merge-engine' = 'aggregation', 'fields.price.aggregate-function' = 'max', 'fields.sales.aggregate-function' = 'sum' ); price列将会根据max函数进行聚合，而sales列将会根据sum函数进行聚合。给定两条输入数据 <1, 23.0, 15>和 <1, 30.2, 20>，最终结果为<1, 30.2, 35>。当前支持的聚合函数与对应的数据类型如下： sum：支持DECIMAL、TINYINT、SMALLINT、INTEGER、BIGINT、FLOAT和DOUBLE。 min和max：支持DECIMAL、TINYINT、SMALLINT、INTEGER、BIGINT、FLOAT、 DOUBLE、DATE、TIME、TIMESTAMP和TIMESTAMP LTZ。 _ last value和last non null value：支持所有数据类型。 _ _ _ _ listagg：支持STRING。 bool and和bool or：支持BOOLEAN。 _ _ 说明只有sum函数支持回撤与删除数据，其它聚合函数不支持回撤与删除。如果您需要某些列忽略回撤与删除消息，可以设置 'fields.${field name}.ignore- _ retract'='true' 。 如果需要流读aggregation的结果，必须将 changelog-producer 参数设置为 lookup或full-compaction。 |  |
|---|---|---|---|
|  |  |  | retract'='true' |

|  | <field-name>.aggregate-function |
|---|---|

| 'fields.${field name}.ignore- _ |  |  |
|---|---|---|

**增量数据产生机制**

通过changelog-producer参数设置相应的增量数据产生机制，Paimon可以为任意输入数据流产生完整的增量数据（所有的update_after数据都有对应的update_before数据）。以下列举了所有的增量数据产生机制。

| 机制 | 详情 |
|---|---|

实时计算（流计算）

| None | 设置 changelog-producer 为none（默认值）后，此时，对于同一个primary key，下游的 Paimon源表只能看到数据的最新情况。但这些最新情况无法让下游消费者方便地了解完整的增量数据， 从而进行正确的计算。因为它只能确定对应数据是否被删除了，或最新数据是什么，无法得知更改之前的数据是什么。 例如，假设下游消费者需要计算某一列的总和，如果消费者只看到了最新数据5，它无法断定该如何更新总和。因为如果之前的数据是4，它应该将总和增加1；如果之前的数据是6，它应该将总和减去1。此类消费者对update before较为敏感，建议不要将增量数据产生机制配置为None，但是其他增量数据产生 _ 机制会带来性能损耗。 说明如果您的下游是数据库之类的对update before数据不敏感的消费者，则可以将增量数据产生机制 _ 配置为None。因此，建议您根据实际需要配置增量数据产生机制。 |
|---|---|
| Input | 设置 changelog-producer 为input后，Paimon结果表会将输入数据流双写至增量数据文件中，作为增量数据。 因此，只有当输入数据流本身是完整的增量数据时（例如CDC数据），才能使用这一增量数据产生机制。 |
| Lookup | 设置 changelog-producer 为lookup后，Paimon结果表会通过一种类似于维表的点查机制，在每次commit snapshot之前产生本次snapshot对应的完整增量数据。无论输入数据是否为完整的增量数据，这一增量数据产生机制均能产生完整的增量数据。 与下文的Full Compaction机制相比，Lookup机制产生增量数据的时效性更好，但总体来看耗费的资源更多。 推荐在对增量数据的新鲜度有较高要求（例如分钟级）的情况下使用。 |
| Full Compac tion | 设置 changelog-producer 为full-compaction后，Paimon结果表会在每一次full compaction时产生完整的增量数据。无论输入数据是否为完整的增量数据，这一增量数据产生机制均能产生完整的增量数据。Full compaction的时间间隔由 full-compaction.delta-commits 参数指定。 与上文的Lookup机制相比，Full Compaction机制产生增量数据的时效性更差，但它利用了数据的full compaction过程，不产生额外计算，因此总体来看耗费的资源更少。 推荐在对增量数据的新鲜度要求不高（例如小时级）的情况下使用。 |

**写入模式**

Paimon表目前支持的写入模式如下。

| 模式 | 详情 |
|---|---|
| Change- log | change-log写入模式是Paimon表的默认写入模式。该写入模式支持根据primary key对数据进行插入、删除与更新，您也可以在该写入模式下使用上文提到的数据合并机制与增量数据产生机制。 |

实时计算（流计算）

| Append- only | append-only写入模式仅支持数据的插入，且不支持primary key。该模式比change-log模式更加高效，可在对数据新鲜度要求一般的场景下（例如分钟级新鲜度）作为消息队列的替代品。 关于append-only写入模式的详细介绍，请参见Apache Paimon官方文档。在使用append-only写入模式时，需要注意以下两点： 建议您根据实际需求设置 bucket-key 参数，否则Paimon表将根据所有列的值进行分桶，计算效率较低。 append-only写入模式可在一定程度上保证数据的产出顺序，具体的产出顺序为： i. 如果两条数据来自不同的分区，若设置了 scan.plan-sort-partition 参数，则分区值较小的数据将首先产出。否则来自较早创建的分区的数据将首先产出。 ii. 如果两条数据来自同一分区的同一分桶，则较早写入的数据将首先产出。 iii. 如果两条数据来自同一分区的不同分桶，由于不同分桶由不同的并发进行处理，因此不保证两条数据的产出顺序。 |
|---|---|

**作为CTAS和CDAS的目标端**

Paimon表支持实时同步单表或整库级别的数据，在同步过程之中如果上游的表结构发生了变更也会实时同步到Paimon表中。

### 大数据计算服务MaxCompute

本文为您介绍大数据计算服务MaxCompute连接器的语法结构、WITH参数和使用示例等。

**背景信息**

大数据计算服务MaxCompute（原名ODPS）是一种快速、完全托管的EB级数据仓库解决方案，致力于批量结构化数据的存储和计算，提供海量数据仓库的解决方案及分析建模服务。 MaxCompute连接器支持的信息如下。

| 类别 | 详情 |
|---|---|
| 支持类型 | 源表、维表和结果表 |
| 运行模式 | 流模式和批模式 |
| 数据格式 | 暂不支持 |

实时计算（流计算）

| 特有监控指标 | 源表 numRecordsIn：源表当前读取到的数据总条数。 numRecordsInPerSecond：源表当前每秒读取的数据条数。 numBytesIn：源表当前读取到的数据总字节数（解压缩后）。 numBytesInPerSecond：源表当前每秒读取的数据字节数（解压缩后）。 结果表 numRecordsOut：结果表当前写出的数据总条数。 numRecordsOutPerSecond：结果表当前每秒写出的数据条数。 numBytesOut：结果表当前写出的数据总字节数（压缩前）。 numBytesOutPerSecond：结果表当前每秒写出的数据字节数（压缩前）。 维表 dim.odps.cacheSize：维表缓存的数据条数。 |
|---|---|
| API种类 | Datastream和SQL |
| 是否支持更新或删除结果表数据 | Batch Tunnel和Stream Tunnel模式仅支持插入数据，Upsert Tunnel模式支持插入、更新和删除数据。 |

**前提条件**

已创建MaxCompute表。

**使用限制**

MaxCompute连接器仅支持At Least Once语义。

**说明**

At Least Once语义会保证数据不缺失，但在少部分情况下，可能会将重复数据写入 MaxCompute。不同的MaxCompute Tunnel出现重复数据的情况不同。 默认情况下源表为全量模式，仅会读取partition参数中指定的分区，在读完所有数据后结束运行，状态转换为finished，不会监控是否有新分区产生。 如果您需要持续监控新分区，请通过WITH参数中指定startPartition使用增量源表模式。

**说明**

维表每次更新时都会检查最新分区，不受这一限制。 在源表开始运行后，向分区里添加的新数据不会被读取，请在分区数据完整的情况下运行作业。

**语法结构**

实时计算（流计算）

```
CREATE TABLE odps_source(
  id INT,
  user_name VARCHAR,
  content VARCHAR
) WITH (
  'connector' = 'odps',
  'endpoint' = '<yourEndpoint>',
  'tunnelEndpoint' = '<yourTunnelEndpoint>',
  'project' = '<yourProjectName>',
  'schemaName' = '<yourSchemaName>',
  'tableName' = '<yourTableName>',
  'accessId' = '${secret_values.ak_id}',
  'accessKey' = '${secret_values.ak_secret}',
  'partition' = 'ds=2018****'
);
```

**WITH参数**

通用

| 参数 | 说明 | 数据类型 | 是否必填 | 默认值 | 备注 |
|---|---|---|---|---|---|
| connector | 表类型。 | Strin g | 是 | 无 | 固定值为odps。 |
| endpoint | MaxCom pute服务地址。 | Strin g | 是 | 无 | 请联系阿里云运维工程师获取。 |
| tunnelEndp oint | MaxCom pute Tunnel服务的连接地址。 | Strin g | 否 | 无 | 请联系阿里云运维工程师获取。 |
| project | MaxCom pute项目名称。 | Strin g | 是 | 无 | 无。 |
| schemaNam e | MaxCom pute Schema 名称。 | Strin g | 否 | 无 | 仅当MaxCompute项目开启Schema功能时，需填写该值为MaxCompute表所属Schema名。 说明仅实时计算引擎VVR 8.0.6及以上版本支持该参数。 |

实时计算（流计算）

| tableName | MaxCom pute表名。 | Strin g | 是 | 无 | 无。 |
|---|---|---|---|---|---|
| accessId | MaxCom pute AccessKe y ID。 | Strin g | 是 | 无 | 无。 |
| accessKey | MaxCom pute AccessKe y Secret。 | Strin g | 是 | 无 | 无。 |
| partition | MaxCom pute分区名。 | Strin g | 否 | 无 | 对于非分区表和增量源表无需填写。 |
| compressAl gorithm | MaxCom pute Tunnel使用的压缩算法。 | Strin g | 否 | VVR 4.0.13 及以上版本：ZLIB VVR 6.0.1 及以上版本： SNAPPY | 参数取值如下： RAW（无压缩） ZLIB SNAPPY SNAPPY相比ZLIB能带来明显的吞吐提升。在测试场景下，吞吐提升约50%。 |
| quotaName | MaxCom pute独享数据传输服务的 quota名称。 | Strin g | 否 | 无 | 设置该值来使用独享的MaxCompute数据传输服务。 重要仅实时计算引擎VVR 8.0.3 及以上版本支持该参数。 设置该值时，必须删除 tunnelEndpoint参数，否则仍将使用 tunnelEndpoint中指定的数据通道。 |

源表独有

| 参数 | 说明 | 数据类型 | 是否必填 | 默认值 | 备注 |
|---|---|---|---|---|---|

实时计算（流计算）

|  |  |  |  |  |  |  | 如果读取的分区数量超过了该参数，则会出现报错 The number of matched |  |  |
|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  | The number of matched |  |
|  |  |  |  |  |  |  | partitions exceeds the default |  |  |
|  |  |  |  |  |  |  | limit |  |  |
|  | maxPartiti onCount | 可以读取的最大分区数量。 | Integer |  | 否 | 100 |  |  |  |

增量源表独有增量源表通过间歇轮询MaxCompute服务器获取所有的分区信息来发现新增的分区，读取新分区时要求分区内数据已写入完毕。通过startPartition可以指定起始点位，但注意只读取**字典序**大于等于起始点位的分区，例如分区 `year=2023,month=10` 字典序小于分区 `year=2023,month=9` ，对于这种类型的分区声明可以通过加0补齐的方式来保证字典序正确，例如 `year=2023,month=09` 。

| 参数 | 说明 | 数据类型 | 是否必填 | 默认值 | 备注 |
|---|---|---|---|---|---|
| startPartiti on | 增量读取的起始 MaxComp ute分区点位（包含）。 | String | 是 | 无 | 使用该参数后启用增量源表模式，将忽略 partition参数。 多级分区必须按分区级别从大到小声明每个分区列的值。 |
| subscribeI ntervalInS ec | 轮询 MaxComp ute获取分区列表的时间间隔。 | Integer | 否 | 30 | 单位为秒。 |

实时计算（流计算）

| modifiedT ableOpera tion | 读取分区过程中遇到分区数据被修改时的处理。 | Enum (NONE, SKIP) | 否 | NONE | 由于下载session被保存在检查点中，每次从检查点恢复时尝试从该session恢复读取进度，而该session由于分区数据被修改不可用，Flink任务会陷入不断重启。此时您可以设置该参数，参数取值如下： NONE：需要您修改startPartition参数使其大于不可用分区，并从无状态启动作业。 SKIP：若不希望无状态启动，可将模式修改为SKIP，Flink尝试从检查点恢复 session时将跳过不可用的分区。 重要 NONE和SKIP模式下，被修改分区中已读取的数据不会被撤回，未读取的数据将不会被读取。 |
|---|---|---|---|---|---|

结果表独有

| 参数 | 说明 | 数据类型 | 是否必填 | 默认值 | 备注 |
|---|---|---|---|---|---|
| useStrea mTunnel | 是否使用 MaxCo mpute Stream Tunnel 上传数据。 | Boolean | 否 | false | 参数取值如下： true：使用MaxCompute Stream Tunnel上传数据。 false：使用MaxCompute Batch Tunnel上传数据。 |
| flushInterv alMs | MaxCo mpute Tunnel Writer缓冲区 flush间隔。 | Long | 否 | 30000（30 秒） | MaxCompute Sink写入记录时，先将数据存储到MaxCompute的缓冲区中，等缓冲区溢出或者每隔一段时间 （flushIntervalMs），再把缓冲区里的数据写到目标MaxCompute表。 对于Stream Tunnel，flush的数据立即可见；对于Batch Tunnel，数据flush后仍需要等待checkpoint完成后才可见，建议设置该参数为0来关闭定时flush。 单位为毫秒。 说明本参数可以与batchSize一同使用，满足任一条件即会Flush数据。 |

实时计算（流计算）

| batchSize | MaxCo mpute Tunnel Writer缓冲区 flush的大小。 | Long | 否 |  | 67108864 （64 MB） | MaxCompute Sink写入记录时，先将数据存储到MaxCompute的缓冲区中，等缓冲区达到一定大小（batchSize），再把缓冲区里的数据写到目标MaxCompute表。 单位为字节。 说明本参数可以与flushIntervalMs一同使用，满足任一条件即会Flush数据。 |  |  |
|---|---|---|---|---|---|---|---|---|
| numFlush Threads | MaxCo mpute Tunnel Writer缓冲区 flush的线程数。 | Integer | 否 |  | 1 | 每个MaxCompute Sink并发将创建 numFlushThreads个线程用于flush数据。 当该值大于1时，将允许不同分区的数据并发 Flush，提升Flush的效率。 |  |  |
| dynamicP artitionLi mit | 写入动态分区的最大数量。 | Integer | 否 |  |  | 当结果表在两次Checkpoint之间写入的动态分区数量超过了dynamicPartitionLimit， 则会出现报错 Too many dynamic partitions 。 重要由于一次性写入大量分区会给 MaxCompute服务带来一定压力，同时也会导致结果表flush和作业 Checkpoint变慢。因此当报错出现时，您需要确认是否需要写入这么多分区。如果确实需要，需要手动调大 dynamicPartitionLimit参数。 |  |  |
|  |  |  |  |  |  |  | Too many dynamic |  |
|  |  |  |  |  |  | partitions |  |  |
|  |  |  |  |  | 100 |  |  |  |
| retryTime s | 向 MaxCo mpute服务器请求最大重试次数。 | Integer | 否 |  | 3 | 创建session、提交session、flush数据时可能存在短暂的MaxCompute服务不可用时， 会根据该配置进行重试。 |  |  |
| sleepMillis | 重试间隔时间。 | Integer | 否 |  | 1000 | 单位为毫秒。 |  |  |

实时计算（流计算）

| enableUps ert | 是否使用 MaxCo mpute Upsert Tunnel 上传数据。 | Boolean | 否 | false | 参数取值如下： true：使用Upsert Tunnel，处理Flink中的INSERT、UPDATE AFTER和DELETE _ 数据。 false：根据useStreamTunnel参数使用 Batch Tunnel或Stream Tunnel，处理 Flink中的INSERT、UPDATE AFTER数 _ 据。 重要若Upsert模式下 MaxCompute sink提交时出现报错、失败、耗时长等情况，建议限制sink节点的并发数在10以内。 仅实时计算引擎VVR 8.0.6及以上版本支持该参数。 |
|---|---|---|---|---|---|
| upsertAsy ncCommit | Upsert模式下在提交 session 时是否使用异步模式。 | Boolean | 否 | false | 参数取值如下： true：使用异步模式，提交耗时更短，但提交完成时写入的数据非立即可读。 false：默认为同步模式，提交时将等待服务侧处理完session。 说明仅实时计算引擎VVR 8.0.6及以上版本支持该参数。 |
| upsertCo mmitTime outMs | Upsert模式下提交 session 超时时间。 | Integer | 否 | 120000 （120秒） | 仅实时计算引擎VVR 8.0.6及以上版本支持该参数。 |

维表独有 MaxCompute维表在作业启动时从指定的分区拉取全量数据，partition参数支持使用max_pt()等函数。 当缓存过期重新加载时会重新解析partition参数拉取最新的分区，使用max_two_pt()时维表可拉取两个分区，其他情况下只支持指定单个分区。

| 参数 | 说明 | 数据类型 | 是否必填 | 默认值 | 备注 |
|---|---|---|---|---|---|

实时计算（流计算）

| cache | 缓存策略。 |  | String | 是 | 无 | 目前MaxCompute维表仅支持 ALL 策略， 必须显式声明。 适用于远程表数据量小且MISS KEY（源表数据和维表JOIN时，ON条件无法关联）特别多的场景。 ALL策略：缓存维表里的所有数据。在Job运行前，系统会将维表中所有数据加载到Cache中， 之后所有的维表查询都会通过Cache进行。如果在Cache中无法找到数据，则KEY不存在，并在 Cache过期后重新加载一遍全量Cache。 说明因为系统会异步加载维表数据，所以在使用CACHE ALL时，需要增加维表JOIN节点的内存，增加的内存大小为远程表数据量的至少4 倍，具体值与MaxCompute存储压缩算法有关。 如果MaxCompute维表数据量较大，可以考虑使用 SHUFFLE HASH注解将维表数据 _ 均匀分散到各个并发中。 在使用超大MaxCompute维表时，如果JVM频繁GC导致作业异常，且在增加维表JOIN节点的内存仍无改善的情况下，建议改为支持 LRU Cache策略的KV型维表，例如云数据库Hbase版维表。 |  |
|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  | 如果维表数据量超过了cacheSize，则会出现报错 Row count of table <table-name> |  |
|  |  |  |  |  |  |  | Row count of table <table-name> |
|  |  |  |  |  |  | partition <partition-name> exceeds |  |
|  |  |  |  |  |  | maxRowCount limit |  |
| cache Size | 最多缓存的数据条数。 |  | Long | 否 | 100000 |  |  |
| cache TTLMs | 缓存超时时间，也就是缓存更新的间隔时间。 |  | Long | 否 | Long.MAX VALUE（ _ 相当于永不更新） | 单位为毫秒。 |  |
| cache Reloa dTime BlackL ist | 更新时间黑名单。 在该参数规定的时间段内不会更新缓存。 |  | String | 否 | 无 | 用于防止缓存在关键时间段（例如活动流量峰值期间）更新导致作业不稳定。 |  |

实时计算（流计算）

| maxLo adRetr ies | 缓存更新时（包含作业启动时初次拉取数据） 最多尝试次数，超过该次数后作业运行失败。 | Integ er | 否 | 10 | 无。 |
|---|---|---|---|---|---|

**类型映射**

| MaxCompute类型 | Flink类型 |
|---|---|
| BOOLEAN | BOOLEAN |
| TINYINT | TINYINT |
| SMALLINT | SMALLINT |
| INT | INTEGER |
| BIGINT | BIGINT |
| FLOAT | FLOAT |
| DOUBLE | DOUBLE |
| DECIMAL(precision, scale) | DECIMAL(precision, scale) |
| CHAR(n) | CHAR(n) |
| VARCHAR(n) | VARCHAR(n) |
| STRING | STRING |
| BINARY | BYTES |
| DATE | DATE |
| DATETIME | TIMESTAMP(3) |

实时计算（流计算）

| TIMESTAMP | TIMESTAMP(9) |
|---|---|
| ARRAY | ARRAY |
| MAP | MAP |
| STRUCT | ROW |
| JSON | STRING |

**重要**

当MaxCompute物理表中同时存在嵌套的复合类型字段（ARRAY、MAP或STRUCT）和JSON类型字段时，需要在创建MaxCompute物理表时指定 `tblproperties('columnar.nested.type'='true')` ， 才能被Flink正确读写。

**使用示例**

**SQL**

源表示例全量读取

```
CREATE TEMPORARY TABLE odps_source (
  cid VARCHAR,
  rt DOUBLE
) WITH (
  'connector' = 'odps',
  'endpoint' = '<yourEndpointName>',
  'project' = '<yourProjectName>',
  'tableName' = '<yourTableName>',
  'accessId' = '${secret_values.ak_id}',
  'accessKey' = '${secret_values.ak_secret}',
  'partition' = 'ds=201809*'
);
  cid VARCHAR,
  invoke_count BIGINT
) WITH ( ); SELECT
   cid,
   COUNT(*) AS invoke_count
FROM odps_source GROUP BY cid;
```

实时计算（流计算） 增量读取

```
CREATE TEMPORARY TABLE odps_source (
  cid VARCHAR,
  rt DOUBLE
) WITH (
  'connector' = 'odps',
  'endpoint' = '<yourEndpointName>',
  'project' = '<yourProjectName>',
  'tableName' = '<yourTableName>',
  'accessId' = '${secret_values.ak_id}',
  'accessKey' = '${secret_values.ak_secret}',
  'startPartition' = 'yyyy=2018,MM=09,dd=05' -- 从20180905对应分区开始读取
);
  cid VARCHAR,
  invoke_count BIGINT
) WITH ( ); SELECT cid, COUNT(*) AS invoke_count FROM odps_source GROUP BY cid;
```

结果表示例实时计算（流计算） 写入固定分区

```
  id INT,
  len INT,
  content VARCHAR
) WITH ( ); CREATE TEMPORARY TABLE odps_sink (
  id INT,
  len INT,
  content VARCHAR
) WITH (
  'connector' = 'odps',
  'endpoint' = '<yourEndpoint>',
  'project' = '<yourProjectName>',
  'tableName' = '<yourTableName>',
  'accessId' = '${secret_values.ak_id}',
  'accessKey' = '${secret_values.ak_secret}',
  'partition' = 'ds=20180905' -- 写入固定分区ds=20180905。
); INSERT INTO odps_sink SELECT
  id, len, content
FROM datagen_source;
```

写入动态分区实时计算（流计算）

```
  id INT,
  len INT,
  content VARCHAR,
  c TIMESTAMP
) WITH ( ); CREATE TEMPORARY TABLE odps_sink (
  id  INT,
  len INT,
  content VARCHAR,
```

`ds VARCHAR --`需要显式声明动态分区列。

```
) WITH (
  'connector' = 'odps',
  'endpoint' = '<yourEndpoint>',
  'project' = '<yourProjectName>',
  'tableName' = '<yourTableName>',
  'accessId' = '${secret_values.ak_id}',
  'accessKey' = '${secret_values.ak_secret}',
```

`'partition' = 'ds' --`不写分区的值，表示根据`ds`字段的值写入不同分区。

```
); INSERT INTO odps_sink SELECT
   id,
   len,
   content,
FROM datagen_source;
```

维表示例一对一维表实时计算（流计算）

```
  k INT,
  v VARCHAR
) WITH ( ); CREATE TEMPORARY TABLE odps_dim (
  k INT,
  v VARCHAR,
```

`PRIMARY KEY (k) NOT ENFORCED --` 一对一维表需要声明主键。

```
) WITH (
  'connector' = 'odps',
  'endpoint' = '<yourEndpoint>',
  'project' = '<yourProjectName>',
  'tableName' = '<yourTableName>',
  'accessId' = '${secret_values.ak_id}',
  'accessKey' = '${secret_values.ak_secret}',
  'partition' = 'ds=20180905',
  'cache' = 'ALL'
);
  k VARCHAR,
  v1 VARCHAR,
  v2 VARCHAR
) WITH ( ); SELECT k, s.v, d.v INNER JOIN odps_dim FOR SYSTEM_TIME AS OF PROCTIME() AS d ON s.k = d.k;
```

实时计算（流计算） 一对多维表

```
  k INT,
  v VARCHAR
) WITH ( ); CREATE TEMPORARY TABLE odps_dim (
  k INT,
  v VARCHAR
```

`--` 一对多维表无需声明主键。

```
) WITH (
  'connector' = 'odps',
  'endpoint' = '<yourEndpoint>',
  'project' = '<yourProjectName>',
  'tableName' = '<yourTableName>',
  'accessId' = '${secret_values.ak_id}',
  'accessKey' = '${secret_values.ak_secret}',
  'partition' = 'ds=20180905',
  'cache' = 'ALL'
);
  k VARCHAR,
  v1 VARCHAR,
  v2 VARCHAR
) WITH ( ); SELECT k, s.v, d.v INNER JOIN odps_dim FOR SYSTEM_TIME AS OF PROCTIME() AS d ON s.k = d.k;
```

**重要**

通过DataStream的方式读写数据时，则需要使用对应的DataStream连接器连接Flink。 Maven中央库中已经放置了MaxCompute DataStream连接器。 为了保护知识产权，从实时计算引擎VVR6.0.6版本起，此连接器在本地调试单次运行作业的时间为30分钟，30分钟后作业会报错并退出。 若您在Flink开发控制台提交作业后，出现类似的MaxCompute相关类ClassNotFound问题， 请下载Maven中央库中对应版本中后缀为uber.jar的文件，添加为作业的附加依赖。以1.15vvr-6.0.6版本为例，需下载的文件为该仓库目录下的verveica-connector-odps-1.15-vvr- 6.0.6-uber.jar。 MaxCompute连接器的Maven依赖包含了构建全量源表、增量源表、结果表和维表的所需要的类。 实时计算（流计算）

```xml
<dependency>
    <groupId>com.alibaba.ververica</groupId>
    <artifactId>ververica-connector-odps</artifactId>
    <version>${connector.version}</version>
</dependency>
```

在DataStream中使用MaxCompute连接器推荐使用SQL声明MaxCompute表，通过Table/DataStream 相互转换来连接MaxCompute表和数据流。 连接源表

```
StreamExecutionEnvironment env = StreamExecutionEnvironment.getExecutionEnvironment(); StreamTableEnvironment tEnv = StreamTableEnvironment.create(env); tEnv.executeSql(String.join(
    "\n",
    "CREATE TEMPORARY TABLE IF NOT EXISTS odps_source (",
    "  cid VARCHAR,",
    "  rt DOUBLE",
    ") WITH (",
    "  'connector' = 'odps',",
    "  'endpoint' = '<yourEndpointName>',",
    "  'project' = '<yourProjectName>',",
    "  'tableName' = '<yourTableName>',",
    "  'accessId' = '<yourAccessId>',",
    "  'accessKey' = '<yourAccessPassword>',",
    "  'partition' = 'ds=201809*'",
    ")");
DataStream<Row> source = tEnv.toDataStream(tEnv.from("odps_source")); source.print(); env.execute("odps source");
```

连接结果表实时计算（流计算）

```
StreamExecutionEnvironment env = StreamExecutionEnvironment.getExecutionEnvironment(); StreamTableEnvironment tEnv = StreamTableEnvironment.create(env); tEnv.executeSql(String.join(
    "\n",
    "CREATE TEMPORARY TABLE IF NOT EXISTS odps_sink (",
    "  cid VARCHAR,",
    "  rt DOUBLE",
    ") WITH (",
    "  'connector' = 'odps',",
    "  'endpoint' = '<yourEndpointName>',",
    "  'project' = '<yourProjectName>',",
    "  'tableName' = '<yourTableName>',",
    "  'accessId' = '<yourAccessId>',",
    "  'accessKey' = '<yourAccessPassword>',",
    "  'partition' = 'ds=20180905'",
    ")");
DataStream<Row> data = env.fromElements(
    Row.of("id0", 3.),
    Row.of("id1", 4.));
tEnv.fromDataStream(data).insertInto("odps_sink").execute();
```

### 消息队列Kafka

**背景信息**

Apache Kafka是一款开源的分布式消息队列系统，广泛用于高性能数据处理、流式分析、数据集成等大数据领域。Kafka连接器基于开源Apache Kafka客户端，为阿里云实时计算Flink提供高性能的数据吞吐、多种数据格式的读写和精确一次语义的支持。

| 类别 | 详情 |
|---|---|
| 支持类型 | 源表和结果表 |
| 运行模式 | 流模式 |

实时计算（流计算）

| 数据格式 | CSV JSON Apache Avro Confluent Avro Debezium JSON Canal JSON Maxwell JSON Raw 说明以上支持的数据格式都有其对应的配置项，可直接在WITH参数中使用，详情请参见Flink 社区文档。 |
|---|---|
| 特有监控指标 | 源表 numRecordsIn numRecordsInPerSecond numBytesIn numBytesInPerScond currentEmitEventTimeLag currentFetchEventTimeLag sourceIdleTime pendingRecords 结果表 numRecordsOut numRecordsOutPerSecond numBytesOut numBytesOutPerSecond currentSendTime |
| API种类 | SQL和Datastream |
| 是否支持更新或删除结果表数据 | 不支持更新和删除结果表数据，只支持插入数据。 说明如果您需要更新和删除结果表数据，相关功能请参见Upsert Kafka。 |

**前提条件**

您可以根据需求选择以下任意一种方式连接集群： 实时计算（流计算） Flink工作空间与Kafka集群处于同一VPC内，且云消息队列 Kafka 版已对Flink开放白名单。

**重要**

写入阿里云Kafka的限制： 阿里云Kafka不支持zstd压缩格式写入。 阿里云Kafka不支持幂等和事务写入，无法使用Kafka结果表提供的精确一次语义exactlyonce semantic功能。在使用**实时计算引擎****VVR 8.0.0** 及以上时，需要在**结果表**中添加配置项 `properties.enable.idempotence=false` 以关闭幂等写入功能。 连接自建Apache Kafka集群自建Apache Kafka集群版本在0.11及以上。 Flink与自建Apache Kafka集群之间的网络已打通。 仅支持Apache Kafka 2.8版本的客户端配置项，详情请参见Apache Kafka消费者和生产者配置项文档。

**使用限制**

**VVR版本与Kafka集群的版本限制**

| Kafka集群版本 | VVR版本 |
|---|---|
| 1.x版本 | 6.x版本 |
| 2.x版本，3.x版本 | 6.x版本，8.x版本 |

**CREATE TABLE AS（CTAS）的使用限制**

仅支持JSON格式的类型推导和schema变更，其它数据格式暂不支持。 仅支持Kafka中value部分的类型推导和表结构变更。如果您需要同步Kafka key部分的列，则需要您手动在DDL中进行指定。

**网络连接排查**

如果您的Flink作业在启动时出现 `Timed out waiting for a node assignment` 错误，一般是Flink和 Kafka之间的网络连通问题导致的。 Kafka客户端与服务端建立连接的过程如下所示。
1. 客户端使用您指定的bootstrap.servers地址连接Kafka服务端，Kafka服务端根据配置向客户端返回集群
中各台broker的元信息，包括各台broker的连接地址。
2. 客户端使用第一步broker返回的连接地址连接各台broker进行读取或写入。
如果Kafka服务端没有正确配置，客户端在第一步收到的连接地址有误，即使**bootstrap.servers**配置的地址可以连接上，也无法正常读取或写入数据。该问题经常在Flink与Kafka之间存在代理、端口转发、专线等网络转发机制时发生。 您可以按照以下步骤检查Kafka集群是否配置正确。
1. 使用Zookeeper命令行工具（zkCli.sh或zookeeper-shell.sh）登录到您Kafka所使用的Zookeeper集
群。 根据您的集群实情执行确的命来获您的信息通常以使实时计算（流计算）
2. 根据您的集群实际情况执行正确的命令，来获取您的Kafka broker元信息。通常可以使用 `get`
`/brokers/ids/0` 命令来获取Kafka broker元信息。Kafka broker的连接地址位于endpoints字段中， 该地址即为上述连接过程中服务端向客户端返回的连接地址，信息如下图所示。
3. 使用ping或telnet等命令来测试endpoint中显示的地址与Flink的连通性。如果无法连通该地址，请联系
您的Kafka运维修改Kafka配置，为Flink单独配置listeners和advertised.listeners。

**说明**

更多关于Kafka客户端与服务端的连接信息，请参见Troubleshoot Connectivity。

**语法结构**

```
CREATE TABLE KafkaTable (
  `user_id` BIGINT,
  `item_id` BIGINT,
  `behavior` STRING,
  `ts` TIMESTAMP_LTZ(3) METADATA FROM 'timestamp' VIRTUAL
) WITH (
  'connector' = 'kafka',
  'topic' = 'user_behavior',
  'properties.bootstrap.servers' = 'localhost:9092',
  'properties.group.id' = 'testGroup',
  'scan.startup.mode' = 'earliest-offset',
  'format' = 'csv'
```

)

**元信息列**

您可以在源表和结果表中定义元信息列，以获取或写入Kafka消息的元信息。例如，当WITH参数中定义了多个topic时，如果在Kafka源表中定义了元信息列，那么Flink读取到的数据就会被标识是从哪个topic中读取的数据。元信息列的使用示例如下。 实时计算（流计算）

```
CREATE TABLE kafka_source (
```

`--`读取消息所属的`topic`作为`record_topic`字段

```
  `record_topic` STRING NOT NULL METADATA FROM 'topic' VIRTUAL,
```

`--`读取`ConsumerRecord`中的时间戳作为`ts`字段

```
  `ts` TIMESTAMP_LTZ(3) METADATA FROM 'timestamp' VIRTUAL,
```

`--`读取消息的`offset`作为`record_offset`字段

```
  `record_offset` BIGINT NOT NULL METADATA FROM 'offset' VIRTUAL,
  ...
) WITH (
  'connector' = 'kafka',
  ...
); CREATE TABLE kafka_sink (
```

`--`将`ts`字段中的时间戳作为`ProducerRecord`的时间戳写入`Kafka`

```
  `ts` TIMESTAMP_LTZ(3) METADATA FROM 'timestamp' VIRTUAL,
  ...
) WITH (
  'connector' = 'kafka',
  ...
);
```

下表列出了Kafka源表和结果表所支持的元信息列。

| Key | 数据类型 | 说明 | 源表或结果表 |
|---|---|---|---|
| topic | STRING NOT NULL METADATA VIRTUAL | Kafka消息所在的Topic名称。 | 源表 |
| partition | INT NOT NULL METADATA VIRTUAL | Kafka消息所在的Partition ID。 | 源表 |
| headers | MAP<STRING, BYTES> NOT NULL METADATA VIRTUAL | Kafka消息的消息头（header）。 | 源表和结果表 |
| leader-epoch | INT NOT NULL METADATA VIRTUAL | Kafka消息的Leader epoch。 | 源表 |
| offset | BIGINT NOT NULL METADATA VIRTUAL | Kafka消息的偏移量（offset）。 | 源表 |
| timestamp | TIMESTAMP(3) WITH LOCAL TIME ZONE NOT NULL METADATA VIRTUAL | Kafka消息的时间戳。 | 源表和结果表 |

实时计算（流计算）

| timestamp- type | STRING NOT NULL METADATA VIRTUAL | Kafka消息的时间戳类型： NoTimestampType：消息中没有定义时间戳。 CreateTime：消息产生的时间。 LogAppendTime：消息被添加到 Kafka Broker的时间。 | 源表 |
|---|---|---|---|

**WITH参数**

通用

| 参数 | 说明 |  | 数据类型 | 是否必填 | 默认值 | 备注 |  |
|---|---|---|---|---|---|---|---|
| connector | 表类型。 |  | String | 是 | 无 | 固定值为kafka。 |  |
| properties.b ootstrap.ser vers | Kafka broker 地址。 |  | String | 是 | 无 | 格式为host:port,host:port,host:port， 以英文逗号（,）分割。 |  |
| properties.* | 对Kafka客户端的直接配置。 |  |  |  |  | 后缀名必须是Kafka官方文档中定义的生产者和消费者配置。 Flink会将properties.前缀移除，并将剩余的配置传递给Kafka客户端。例如可以通过 'properties.allow.auto.create. topics'='false' 来禁用自动创建 topic。 不能通过该方式修改以下配置，因为它们会被Kafka连接器覆盖： key.deserializer value.deserializer |  |
|  |  |  |  |  |  |  | 'properties.allow.auto.create. |
|  |  | 户 | String | 否 | 无 | topics'='false' |  |
| format | 读取或写入 Kafka消息 value部分时使用的格式。 |  | String | 否 | 无 | 支持的格式 csv json avro debezium-json canal-json maxwell-json avro-confluent raw 说明更多format参数设置请参见Format 参数。 |  |

实时计算（流计算）

| key.format | 读取或写入 Kafka消息 key部分时使用的格式。 | String | 否 | 无 | 支持的格式 csv json avro debezium-json canal-json maxwell-json avro-confluent raw 说明使用该配置时，key.options配置是必填的。 |
|---|---|---|---|---|---|
| key.fields | Kafka消息 key部分对应的源表或结果表字段。 | String | 否 | 无 | 多个字段名以分号（;）分隔。例如 field1;field2 |
| key.fields- prefix | 为所有Kafka 消息key部分指定自定义前缀，以避免与消息value部分格式字段重名。 | String | 否 | 无 | 该配置项仅用于源表和结果表的列名区分， 解析和生成Kafka消息key部分时，该前缀会被移除。 说明使用该配置时，value.fields- include必须配置为EXCEPT KEY。 _ |
| value.format | 读取或写入 Kafka消息 value部分时使用的格式。 | String | 否 | 无 | 该配置等同于format，因此format和value.format 只能配置其中一个，如果同时配置两个会产生冲突 |
| value.fields- include | 在解析或生成 Kafka消息 value部分时，是否要包含消息key部分对应的字段。 | String | 否 | ALL | 参数取值如下： ALL（默认值）：所有列都会作为Kafka 消息value部分处理。 EXCEPT KEY：除去key.fields定义的 _ 字段，剩余字段作为Kafka消息value部分处理。 |

源表

| 参数 | 说明 | 数据类型 | 是否必填 | 默认值 | 备注 |
|---|---|---|---|---|---|

实时计算（流计算）

| topic | 读取的topic 名称。 |  | String | 否 | 无 | 以英文分号 (;) 分隔多个topic名称，例如 topic-1和topic-2。 说明 topic和topic-pattern两个选项只能指定其中一个。 |  |
|---|---|---|---|---|---|---|---|
| topic- pattern | 匹配读取 topic名称的正则表达式。 所有匹配该正则表达式的 topic在作业运行时均会被读取。 |  | String | 否 | 无 | topic和topic-pattern两个选项只能指定其中一个。 |  |
| properties.g roup.id | 消费组ID。 |  | String | 否 | KafkaS ource- {源表表名} | 如果指定的group id为首次使用，则必须将properties.auto.offset.reset设置为earliest或latest以指定首次启动位点。 |  |
| scan.startup .mode | Kafka读取数据的启动位点。 |  | String | 否 | group- offsets | 取值如下： earliest-offset：从Kafka最早分区开始读取。 latest-offset：从Kafka最新位点开始读取。 group-offsets（默认值）：从指定的properties.group.id已提交的位点开始读取。 timestamp： 从scan.startup.timestamp- millis指定的时间戳开始读取。 specific-offsets： 从scan.startup.specific- offsets指定的偏移量开始读取。 说明该参数在作业无状态启动时生效。作业在从checkpoint重启或状态恢复时，会优先使用状态中保存的进度恢复读取。 |  |
| scan.startup .specific- offsets | specific- offsets启动模式下，指定每个分区的启动偏移量。 |  | String | 否 | 无 | 例如 partition:0,offset:42;partiti on:1,offset:300 |  |
|  |  |  |  |  |  |  | partition:0,offset:42;partiti |
|  |  |  |  |  |  | on:1,offset:300 |  |

实时计算（流计算）

| scan.startup .timestamp- millis | timestamp 启动模式下， 指定启动位点时间戳。 |  | Long | 否 | 无 | 单位为毫秒。 |  |  |
|---|---|---|---|---|---|---|---|---|
| scan.topic- partition- discovery.in terval | 动态检测 Kafka topic 和partition 的时间间隔。 |  | Durati on | 否 | 5分钟 | 分区检查间隔默认为5分钟。需要显式地设置分区检查间隔为非正数才能关闭此功能。开启动态分区发现后，Kafka Source 可以自动地发现新增的分区并自动读取对应分区上的数据。在topic- pattern模式下，不仅读取已有topic的新增分区数据，也会读取符合正则匹配的新增topic的所有分区数据。 说明在实时计算引擎VVR 6.0.x版本中， 动态分区检测默认为关闭。自8.0版本起该功能默认打开，检测间隔默认设置为5分钟。 |  |  |
| scan.header -filter | 根据Kafka数据是否包含指定的消息头 （Header） 对数据进行条件过滤。 |  |  |  |  | Header key和value使用冒号（:）分隔，多个header条件之间使用逻辑运算符 （&、\|）连接，支持取反逻辑运算符 （!）。例如 depart:toy\|depart:book&!env:t est 表示保留header中包含 depart=toy或depart=book，且不包含 env=test的Kafka数据。 说明仅实时计算引擎VVR 8.0.6 及以上版本支持配置该参数。 暂不支持括号运算。 逻辑运算顺序为从左至右。 Header value会以UTF-8 格式转换为字符串，与参数指定的header value进行比较。 |  |  |
|  |  |  |  |  |  |  | depart:toy\|depart:book&!env:t |  |
|  |  |  |  |  |  | est |  |  |
|  |  |  | String | 否 | 无 |  |  |  |

实时计算（流计算）

|  | scan.check. |  | 是否检查通过 propert |  |  | 否 | false | 参数取值如下： true：在启动作业前检查消费者组是否有重复，如有重复作业将会报错，避免与现有的消费者组产生冲突。 false：直接启动作业，不检查消费者组冲突。 说明仅VVR 6.0.4及以后版本支持该参数。 |
|---|---|---|---|---|---|---|---|---|
|  |  |  |  | propert |  |  |  |  |
|  |  | heck. | ies.group. |  |  |  |  |  |
|  | duplicated.g roup.id | ated.g |  |  |  |  |  |  |
|  |  |  | id |  |  |  |  |  |

结果表

| 参数 | 说明 | 数据类型 | 是否必填 | 默认值 | 备注 |
|---|---|---|---|---|---|
| topic | 写入的topic名称。 | String | 是 | 无 | 无 |
| sink.partitio ner | 从Flink并发到 Kafka分区的映射模式。 | String | 否 | defau lt | 取值如下： default（默认值）：使用Kafka默认的分区模式 fixed：每个Flink并发对应一个固定的 Kafka分区。 round-robin：Flink并发中的数据将被轮流分配至Kafka的各个分区。 自定义分区映射模式：如果fixed和 round-robin不满足您的需求，您可以创建一个FlinkKafkaPartitioner的子类来自定义分区映射模式。例如 org.mycompany.MyPartitioner |
| sink.deliver y-guarantee | Kafka结果表的语义模式。 | String | 否 | at- least- once | 取值如下： none：不保证任何语义，数据可能会丢失或重复。 at-least-once（默认值）：保证数据不丢失，但可能会重复。 exactly-once：使用Kafka事务保证数据不会丢失和重复。 说明在使用exactly-once语义时，sink.transactional-id- prefix是必填的。 |

实时计算（流计算）

| sink.transac tional-id- prefix | 在exactly- once语义下使用的Kafka事务ID前缀。 | String | 否 | 无 | 只有sink.delivery-guarantee配置为 exactly-once时该配置才会生效。 |
|---|---|---|---|---|---|
| sink.paralleli sm | Kafka结果表算子的并发数。 | Intege r | 否 | 无 | 上游算子的并发，由框架决定。 |

CTAS同步数据源

| 参数 | 说明 | 数据类型 | 是否必填 |  | 默认值 | 备注 |  |  |
|---|---|---|---|---|---|---|---|---|
| json.infer- schema.flat ten-nested- columns.en able | 是否递归式地展开 JSON中的嵌套列。 | Boolean | 否 |  |  | 参数取值如下： true：递归式展开。对于被展开的列，Flink使用索引该值的路径作为名字。例如，对于 JSON {"nested": {"col": true}} 中的列col，它展开后的名字为nested.col。 false（默认值）：将嵌套类型当作 String处理。 |  |  |
|  |  |  |  |  |  |  | JSON {"nested": |  |
|  |  |  |  |  | false | {"col": true}} |  |  |
| json.infer- schema.pri mitive-as- string | 是否推导所有基本类型为 String类型。 | Boolean | 否 |  | false | 参数取值如下： true：推导所有基本类型为String。 false：按照基本规则进行推导。 |  |  |

所有Kafka consumer和producer支持的配置项均可在配置前添加 `properties.` 前缀后在WITH参数中使用。例如需要配置Kafka consumer或producer的超时时间**request.timeout.ms**为60000毫秒，则可以在WITH参数中配置 `'properties.request.timeout.ms'='60000'` 。Kafka consumer和 Kafka producer的配置项详情请参见Apache Kafka官方文档。

**安全与认证**

如果您的Kafka集群要求安全连接或认证，请将相关的安全与认证配置添加 `properties.` 前缀后设置在 WITH参数中。配置Kafka表以使用PLAIN作为SASL机制，并提供JAAS配置的示例如下。 实时计算（流计算）

```
CREATE TABLE KafkaTable (
  `user_id` BIGINT,
  `item_id` BIGINT,
  `behavior` STRING,
  `ts` TIMESTAMP_LTZ(3) METADATA FROM 'timestamp'
) WITH (
  'connector' = 'kafka',
  ...
  'properties.security.protocol' = 'SASL_PLAINTEXT',
  'properties.sasl.mechanism' = 'PLAIN',
  'properties.sasl.jaas.config' =
'org.apache.flink.kafka.shaded.org.apache.kafka.common.security.plain.PlainLoginModule required username="username" password="password";'
```

) 使用SASL_SSL作为安全协议，并使用SCRAM-SHA-256作为SASL机制的示例如下。

```
CREATE TABLE KafkaTable (
  `user_id` BIGINT,
  `item_id` BIGINT,
  `behavior` STRING,
  `ts` TIMESTAMP_LTZ(3) METADATA FROM 'timestamp'
) WITH (
  'connector' = 'kafka',
  ...
  'properties.security.protocol' = 'SASL_SSL',
```

`/*SSL`配置`*/` `/*`配置服务端提供的`truststore (CA` 证书) 的路径`*/`

```
  'properties.ssl.truststore.location' = '/flink/usrlib/kafka.client.truststore.jks',
  'properties.ssl.truststore.password' = 'test1234',
```

`/*`如果要求客户端认证，则需要配置`keystore (`私钥) 的路径`*/`

```
  'properties.ssl.keystore.location' = '/flink/usrlib/kafka.client.keystore.jks',
  'properties.ssl.keystore.password' = 'test1234',
```

`/*`客户端验证服务器地址的算法，空值表示禁用服务器地址验证`*/`

```
  'properties.ssl.endpoint.identification.algorithm' = '',
```

`/*SASL`配置`*/` `/*`将`SASL`机制配置为`as SCRAM-SHA-256*/`

```
  'properties.sasl.mechanism' = 'SCRAM-SHA-256',
```

`/*`配置`JAAS*/`

```
  'properties.sasl.jaas.config' =
'org.apache.flink.kafka.shaded.org.apache.kafka.common.security.scram.ScramLoginModule required username="username" password="password";'
```

) 示例中提到的CA证书和私钥可使用实时计算控制台的资源上传功能上传至平台，上传后文件存放在/flink/usrlib目录下。例如，需要使用的CA证书文件名为my-truststore.jks，则上传后您可以在WITH参

```
数中指定 'properties.ssl.truststore.location' = '/flink/usrlib/my-truststore.jks' 来使用该
```

证书。 实时计算（流计算）

**说明**

上文中的示例仅适用于大多数配置情况。在配置Kafka连接器前，请与您的Kafka服务端运维人员联系，以获取正确的安全与认证配置信息。 与开源Flink不同，实时计算Flink版的SQL编辑器默认已经对双引号（"）进行转义处理，因此您在配置 `properties.sasl.jaas.config` 时无需对用户名和密码中的双引号（"）添加额外的转义符（\）。

**源表起始位点**

**启动模式**

Kafka源表可通过配置**scan.startup.mode**来指定初始读取位点： 最早位点（earliest-offset）：从当前分区的最早位点开始读取。 最末尾位点（latest-offset）：从当前分区的最末尾位点开始读取。 已提交位点（group-offsets）：从指定group id的已提交位点开始读取，group id通过**properties.group.id**指定。 指定时间戳（timestamp）：从时间戳大于等于指定时间的第一条消息开始读取，时间戳通过**scan.startup.timestamp-millis**指定。 特定位点（specific-offsets）：从您指定的分区位点开始消费，位点通过**scan.startup.specific-**
**offsets**指定。

**说明**

如果您不指定启动位点，则默认会从已提交位点（group-offsets）启动消费。
**scan.startup.mode**只针对无状态启动的作业生效，有状态作业启动时会从状态中存储的位
点开始消费。 代码示例如下： 实时计算（流计算）

```
CREATE TEMPORARY TABLE kafka_source (
  ...
) WITH (
  'connector' = 'kafka',
  ...
```

`--`从最早位点开始消费

```
  'scan.startup.mode' = 'earliest-offset',
```

`--`从最末尾位点开始消费

```
  'scan.startup.mode' = 'latest-offset',
```

`--`从消费者组`"my-group"`的已提交位点开始消费

```
  'properties.group.id' = 'my-group',
  'scan.startup.mode' = 'group-offsets',
```

`'properties.auto.offset.reset' = 'earliest', --` 如果 `"my-group"` 为首次使用，则从最早位点开始消费 `'properties.auto.offset.reset' = 'latest', --` 如果 `"my-group"` 为首次使用，则从最末尾位点开始消费 `--`从指定的毫秒时间戳`1655395200000`开始消费

```
  'scan.startup.mode' = 'timestamp',
  'scan.startup.timestamp-millis' = '1655395200000',
```

`--`从指定位点开始消费

```
  'scan.startup.mode' = 'specific-offsets',
  'scan.startup.specific-offsets' = 'partition:0,offset:42;partition:1,offset:300'
);
```

**起始位点优先级**

源表起始位点的优先级为：
1. Checkpoint或Savepoint中存储的位点。
2. 您在实时计算控制台指定的启动时间。
3. 您在WITH参数中通过**scan.startup.mode**指定的启动位点。
4. 未指定**scan.startup.mode**的情况下使用**group-offsets**。
在以上任何一个步骤中，如果位点过期或Kafka集群发生问题等原因导致位点无效，则会使用**properties.auto.offset.reset**指定的策略进行位点重置，如果您未设置该配置项，则会产生异常要求您介入。 一种常见情况是使用全新的group id开始消费。首先源表会向Kafka集群查询该group的已提交位点，由于该group id是第一次使用，不会查询到有效位点，所以会通过**properties.auto.offset.reset**参数配置的策略进行重置。因此在使用全新group id进行消费时，必须配置**properties.auto.offset.reset**来指定位点重置策略。

**源表位点提交**

Kafka源表只在checkpoint成功后将当前消费位点提交至Kafka集群。如果您的checkpoint间隔设置较长，您在Kafka集群侧观察到的消费位点会有延迟。在进行checkpoint时，Kafka源表会将当前读取进度存储在状态中，并不依赖于提交到集群上的位点进行故障恢复，提交位点仅仅是为了在Kafka侧能够监控到读取进度，位点提交失败不会对数据正确性产生任何影响。

**结果表自定义分区器**

如果内置的Kafka Producer分区模式无法满足您的需求，您可以实现自定义分区模式将数据写入对应的分区。自定义分区器需要继承FlinkKafkaPartitioner，开发完成后编译JAR包，使用资源上传功能上传至实时计算控制台。上传并引用完成后，请在WITH参数中设置**sink.partitioner**参数，参数值为分区器完整的类路径，如 `org.mycompany.MyPartitioner` 。 实时计算（流计算） Kafka是一种只能添加数据的消息队列系统，无法进行数据的更新和删除操作，因此在流式SQL计算中无法处理上游的CDC变更数据和聚合、联合等算子的回撤逻辑。如果您需要将含有变更或回撤类型的数据写入为了方便您将上游数据库中一个或多个数据表中的变更数据批量同步到Kafka中，您可以使用Kafka JSON catalog。如果您的Kafka中存储的数据格式为JSON，使用Kafka JSON catalog可以省去定义schema和 WITH参数的步骤。

**作为CTAS数据源**

CTAS语句支持将消息队列Kafka，且format为JSON的表作为数据源。在数据同步过程中，如果某些字段并未出现在预定义的表结构中，Flink会尝试自动推导该列的类型。如果自动推导的类型不能满足您的使用需求，您也可以通过辅助推导的方式对某些列的解析类型进行声明。

**说明**

关于JSON Format的详细描述，详情请参见JSON Format。 类型推导在类型推导过程中，Flink默认只展开JSON文本中的第一层数据，根据其类型和数值，按照基本规则进行类型推导。类型映射基本规则如下表所示。

| JSON类型 | Flink SQL类型 |
|---|---|
| BOOLEAN | BOOLEAN |
| STRING | DATE、TIMESTAMP、TIMESTAMP LTZ、TIME或 STRING _ |
| INT或LONG | BIGINT |
| BIGINT | DECIMAL或STRING 说明 Flink中DECIMAL的类型存在精度限制。因此，如果整数的实际取值超过了DECIMAL类型最大精度，Flink会自动推导其类型为STRING，避免精度的损失。 |
| FLOAT、DOUBLE或BIG DECIMAL | DOUBLE |
| ARRAY | STRING |
| OBJECT | STRING |

示例实时计算（流计算） JSON文本

```json
{
  "id": 101,
  "name": "VVP",
  "properties": {
```

`"owner": "`阿里云`",`

```json
    "engine": "Flink"
  }
```

`"type": ["`大数据`"]`

```
}
```

Flink写入到下游存储的表信息为

| id | name | properties | type |
|---|---|---|---|
| 101 | VVP | { "owner": "阿里云", "engine": "Flink" } | ["大数据"] |

辅助推导当基本规则不符合您的实际需要时，您可以在源表的DDL中声明特定列的解析类型。通过该方式，Flink会优先使用您声明的列类型去解析目标字段。针对以下示例，Flink会使用DECIMAL的方式去解析price字段，而不是使用默认的基本规则将其转换为DOUBLE类型。

```
CREATE TABLE evolvingKafkaSource (
  price DECIMAL(18, 2)
) WITH (
  'connector' = 'kafka',
  'properties.bootstrap.servers' = 'localhost:9092',
  'topic' = 'evolving_kafka_demo',
  'scan.startup.mode' = 'earliest-offset',
  'format' = 'json'
);
```

但是，当您在DDL中指定的类型和实际数据中的类型不一致时，可以按照以下方式进行处理： 在声明的类型比实际类型更宽泛时，以声明的类型自动去解析。例如，声明为DOUBLE，遇到的数据类型为BIGINT，则会以DOUBLE类型去解析。 实时计算（流计算） 在实际的类型比声明的类型更为宽泛或者两种类型不兼容时，由于当前CTAS不支持类型变更，因此会报错提示您相关信息，您需要重新启动作业并声明准确的类型去解析数据。 类型的宽泛的程度以及兼容性如下图所示。

**说明**

上图表示越靠近根节点，其类型越宽泛。如果两个类型在不同的分支上，则表示这两个类型不兼容。 不支持辅助推导复杂类型，包括ROW、ARRAY、MAP和MULTISET。 对于复杂类型，Flink在默认情况下会处理为STRING。 通常，Kafka topic中的JSON文本带有嵌套结构。如果您需要提取JSON文本中的嵌套列，则可以通过以下两种方式： 在源表DDL中声明 `'json.infer-schema.flatten-nested-columns.enable'='true'` ，来展开嵌套列中的所有元素至顶层。通过该方式，所有的嵌套列都会被依次展开。为了避免列名冲突，Flink采用索引到该列的路径作为展开后列名字。

**重要**

目前不支持解决列名冲突。如果发生列名冲突，请在源表的DDL中声明json.ignore-parse-errors为 true，来忽略存在冲突的数据。 在DDL中CTAS语法中添加计算列 `rowkey` AS JSON_VALUE(`properties`, `$.rowkey`) ，来指定要展开的列。

**使用示例**

**示例一：从Kafka中读取数据后写入Kafka**

从名称为源表的Topic中读取Kafka数据，再写入名称为结果表的Topic，数据使用CSV格式。 实时计算（流计算）

```
CREATE TEMPORARY TABLE kafka_source (
  id INT,
  name STRING,
  age INT
) WITH (
  'connector' = 'kafka',
  'topic' = 'source',
  'properties.bootstrap.servers' = '<yourKafkaBrokers>',
  'properties.group.id' = '<yourKafkaConsumerGroupId>',
  'format' = 'csv'
); CREATE TEMPORARY TABLE kafka_sink (
  id INT,
  name STRING,
  age INT
) WITH (
  'connector' = 'kafka',
  'topic' = 'sink',
  'properties.bootstrap.servers' = '<yourKafkaBrokers>',
  'properties.group.id' = '<yourKafkaConsumerGroupId>',
  'format' = 'csv'
); INSERT INTO kafka_sink SELECT id, name, age FROM kafka_source;
```

**示例二：同步表结构以及数据**

将Kafka Topic中的消息实时同步到Hologres中。在该情况下，您可以将Kafka消息的offset和partition id 作为主键，从而保证在Failover时，Hologres中不会有重复消息。

```
CREATE TEMPORARY TABLE kafkaTable (
  `offset` INT NOT NULL METADATA,
  `part` BIGINT NOT NULL METADATA FROM 'partition',
  PRIMARY KEY (`part`, `offset`) NOT ENFORCED
) WITH (
  'connector' = 'kafka',
  'properties.bootstrap.servers' = '<yourKafkaBrokers>',
  'topic' = 'kafka_evolution_demo',
  'scan.startup.mode' = 'earliest-offset',
  'format' = 'json',
  'json.infer-schema.flatten-nested-columns.enable' = 'true'
```

`--`可选，将嵌套列全部展开。

```
); CREATE TABLE IF NOT EXISTS hologres.kafka.`sync_kafka` WITH (
  'connector' = 'hologres'
) AS TABLE vvp.`default`.kafkaTable;
```

**示例三：同步表结构以及Kafka消息的key和value数据**

Kafka消息中的key部分已经存储了相关信息，您可以同时同步Kafka中的key和value。 实时计算（流计算）

```
CREATE TEMPORARY TABLE kafkaTable (
  `key_id` INT NOT NULL,
  `val_name` VARCHAR(200)
) WITH (
  'connector' = 'kafka',
  'properties.bootstrap.servers' = '<yourKafkaBrokers>',
  'topic' = 'kafka_evolution_demo',
  'scan.startup.mode' = 'earliest-offset',
  'key.format' = 'json',
  'value.format' = 'json',
  'key.fields' = 'key_id',
  'key.fields-prefix' = 'key_',
  'value.fields-prefix' = 'val_',
  'value.fields-include' = 'EXCEPT_KEY'
); CREATE TABLE IF NOT EXISTS hologres.kafka.`sync_kafka`( WITH (
  'connector' = 'hologres'
) AS TABLE vvp.`default`.kafkaTable;
```

**说明**

Kafka消息中的key部分不支持表结构变更和类型推导，需要您手动声明。

**示例四：同步表结构和数据并进行计算**

在同步Kafka数据到Hologres时，往往需要一些轻量级的计算。

```
CREATE TEMPORARY TABLE kafkaTable (
  `distinct_id` INT NOT NULL,
  `properties` STRING,
  `timestamp` TIMESTAMP_LTZ METADATA,
  `date` AS CAST(`timestamp` AS DATE)
) WITH (
  'connector' = 'kafka',
  'properties.bootstrap.servers' = '<yourKafkaBrokers>',
  'topic' = 'kafka_evolution_demo',
  'scan.startup.mode' = 'earliest-offset',
  'key.format' = 'json',
  'value.format' = 'json',
  'key.fields' = 'key_id',
  'key.fields-prefix' = 'key_'
); CREATE TABLE IF NOT EXISTS hologres.kafka.`sync_kafka` WITH (
   'connector' = 'hologres'
) AS TABLE vvp.`default`.kafkaTable ADD COLUMN
  `order_id` AS COALESCE(JSON_VALUE(`properties`, '$.order_id'), 'default');
```

`--`使用`COALESCE`处理空值情况。 实时计算（流计算）

**Datastream API**

**重要**

通过DataStream的方式读写数据时，则需要使用对应的DataStream连接器连接Flink，Maven中央库中已经放置了Kafka DataStream连接器。 构建Kafka Source Kafka Source提供了构建类来创建Kafka Source的实例。我们将通过以下示例代码为您介绍如何构建 Kafka Source来消费input-topic最早位点的数据，消费组名称为my-group，并将Kafka消息体反序列化为字符串。

```
KafkaSource<String> source = KafkaSource.<String>builder()
    .setBootstrapServers(brokers)
    .setTopics("input-topic")
    .setGroupId("my-group")
    .setStartingOffsets(OffsetsInitializer.earliest())
    .setValueOnlyDeserializer(new SimpleStringSchema())
    .build();
env.fromSource(source, WatermarkStrategy.noWatermarks(), "Kafka Source");
```

在构建KafkaSource时，必须指定以下参数。

| 参数 | 说明 |
|---|---|
| Bootst rapSer vers | Kafka Broker地址，通过setBootstrapServers(String)方法配置。 |
| GroupI d | 消费者组ID，通过setGroupId(String)方法配置。 |
| Topics 或 Partitio n | 订阅的Topic或Partition名称。Kafka Source提供了以下三种Topic或Partition的订阅方式： Topic列表，订阅Topic列表中所有Partition。 KafkaSource.builder().setTopics("topic-a","topic-b") 正则表达式匹配，订阅与正则表达式所匹配的Topic下的所有Partition。 KafkaSource.builder().setTopicPattern("topic.*") Partition列表，订阅指定的Partition。 final HashSet<TopicPartition> partitionSet = new HashSet<> (Arrays.asList( new TopicPartition("topic-a", 0), // Partition 0 of topic "topic-a" new TopicPartition("topic-b", 5))); // Partition 5 of topic "topic-b" KafkaSource.builder().setPartitions(partitionSet) |

实时计算（流计算）

| Deseri alizer | 解析Kafka消息的反序列化器。 反序列化器通过setDeserializer(KafkaRecordDeserializationSchema)来指定，其中 KafkaRecordDeserializationSchema定义了如何解析Kafka的ConsumerRecord。如果只解析 Kafka消息中的消息体（Value）的数据，则您可以通过以下任何一种方式实现： 使用Flink提供的KafkaSource构建类中的setValueOnlyDeserializer(DeserializationSchema)方法，其中DeserializationSchema定义了如何解析Kafka消息体中的二进制数据。 使用Kafka提供的解析器，包括多种实现类。例如，您可以使用StringDeserializer来将Kafka消息体解析成字符串。 import org.apache.kafka.common.serialization.StringDeserializer; KafkaSource.<String>builder() .setDeserializer(KafkaRecordDeserializationSchema.valueOnly(StringDeseria izer.class)); 说明如果需要完整地解析ConsumerRecord，则需要您自己实现 KafkaRecordDeserializationSchema接口。 |
|---|---|

在使用Kafka DataStream连接器时，您还需要了解以下Kafka属性： 实时计算（流计算） 起始消费位点 Kafka Source能够通过位点初始化器（OffsetsInitializer）来指定从不同的偏移量开始消费。内置的位点初始化器包括以下内容。

| 位点初始化器 | 代码设置 |  |  |
|---|---|---|---|
| 从最早位点开始 | KafkaSource.builder().setStartingOffsets(OffsetsInitializer.earlies ()) |  |  |
|  |  | KafkaSource.builder().setStartingOffsets(OffsetsInitializer.earlies | t |
| 消费。 | ()) |  |  |
| 从最末尾位点开 | KafkaSource.builder().setStartingOffsets(OffsetsInitializer.latest( ) |  |  |
|  |  | KafkaSource.builder().setStartingOffsets(OffsetsInitializer.latest( | ) |
| 始消费。 | ) |  |  |
| 从时间戳大于等于指定时间的数 | KafkaSource.builder().setStartingOffsets(OffsetsInitializer.timesta p(1592323200000L)) |  |  |
|  |  | KafkaSource.builder().setStartingOffsets(OffsetsInitializer.timesta |  |
| 据开始消费，单 | p(1592323200000L)) |  |  |
| 位为毫秒。 |  |  |  |
| 从消费组提交的位点开始消费， | KafkaSource.builder().setStartingOffsets(OffsetsInitializer.committ dOffsets(OffsetResetStrategy.EARLIEST)) |  |  |
|  |  | KafkaSource.builder().setStartingOffsets(OffsetsInitializer.committ |  |
| 如果提交位点不存在，使用最早 | dOffsets(OffsetResetStrategy.EARLIEST)) |  |  |
| 位点。 |  |  |  |
| 从消费组提交的位点开始消费， | KafkaSource.builder().setStartingOffsets(OffsetsInitializer.committ dOffsets()) |  |  |
|  |  | KafkaSource.builder().setStartingOffsets(OffsetsInitializer.committ | e |
| 不指定位点重置 | dOffsets()) |  |  |
| 策略。 |  |  |  |

**说明**

如果以上内置的初始化器不能满足需求，您也可以自己实现自定义的位点初始化器。 如果您未指定位点初始化器，则默认使用OffsetsInitializer.earliest()，即最早位点。 流模式和批模式 Kafka Source支持流式和批式两种运行模式。默认情况下，Kafka Source设置为以流模式运行，因此作业永远不会停止，直到Flink作业失败或被取消。如果要配置Kafka Source在批模式下运行，您可以使用setBounded(OffsetsInitializer)指定停止偏移量，当所有分区都达到其停止偏移量时，Kafka Source会退出运行。

**说明**

通常，流模式下Kafka Source没有停止偏移量。为了方便对代码进行调试，流模式下您也可以使用setUnbounded(OffsetsInitializer) 指定停止偏移量。请留意指定流模式和批模式停止偏移量的方法名（setUnbounded和setBounded）是不同的。 实时计算（流计算） 动态分区检查为了在不重启Flink作业的情况下，处理Topic扩容或新建Topic等场景，您可以在提供的Topic或 Partition订阅模式下，启用动态分区检查功能。

**说明**

默认开启动态分区检查功能，分区检查间隔默认为5分钟。需要显式地设置分区检查间隔为非正数才能关闭此功能。代码示例如下。

```
KafkaSource.builder()
    .setProperty("partition.discovery.interval.ms", "10000") // 每10秒检查一次新分
```

区。 事件时间和水印 Kafka Source默认使用Kafka消息中的时间戳作为事件时间。您可以自定义水印策略（Watermark Strategy）以从消息中提取事件时间，并向下游发送水印。

```
env.fromSource(kafkaSource, new CustomWatermarkStrategy(), "Kafka Source With Custo
```

如果您需要了解自定义水印策略（Watermark Strategy），请参见Generating Watermarks。 消费位点提交 Kafka Source在Checkpoint完成时，提交当前的消费位点，以保证Flink的Checkpoint状态和Kafka Broker上的提交位点一致。如果未开启Checkpoint，Kafka Source依赖于Kafka Consumer内部的位点定时自动提交逻辑，自动提交功能由enable.auto.commit和auto.commit.interval.ms两个 Kafka Consumer配置项进行配置。

**说明**

Kafka Source不依赖于Broker上提交的位点来恢复失败的作业。提交位点只是为了上报Kafka Consumer和消费组的消费进度，以在Broker端进行监控。 实时计算（流计算） 其他属性除了上述属性之外，您还可以使用setProperties(Properties) 和setProperty(String, String) 为 Kafka Source和Kafka Consumer设置任意属性。KafkaSource通常有以下配置项。

| 配置项 | 说明 |
|---|---|
| client.id.pr efix | 指定用于Kafka Consumer的客户端ID前缀。 |
| partition.d iscovery.in terval.ms | 定义Kafka Source检查新分区的时间间隔。 说明 partition.discovery.interval.ms会在批模式下被覆盖为-1。 |
| register.co nsumer.m etrics | 指定是否在Flink中注册Kafka Consumer的指标。 |
| 其他Kafka Consumer配置 | Kafka Consumer的配置详情，请参见Apache Kafka。 重要 Kafka Connector会强制覆盖部分您手动配置的参数项，覆盖详情如下： key.deserializer始终被覆盖为ByteArrayDeserializer。 value.deserializer始终被覆盖为ByteArrayDeserializer。 auto.offset.reset.strategy被覆盖为 OffsetsInitializer#getAutoOffsetResetStrategy()。 |

以下示例为您展示如何配置Kafka Consumer，以使用PLAIN作为SASL机制并提供JAAS配置。

```
KafkaSource.builder()
    .setProperty("sasl.mechanism", "PLAIN")
    .setProperty("sasl.jaas.config",
"org.apache.kafka.common.security.plain.PlainLoginModule required username=\"username\" password=\"password\";")
```

实时计算（流计算） 监控 Kafka Source在Flink中注册指标，用于监控和诊断。 指标范围 Kafka source reader的所有指标都注册在KafkaSourceReader指标组下，KafkaSourceReader 是operator指标组的子组。与特定主题分区相关的指标注册在KafkaSourceReader.topic. <topic_name>.partition.<partition_id>指标组中。 例如Topic "my-topic"、分区1的当前消费位点（currentOffset）注册在 <some_parent_groups>.operator.KafkaSourceReader.topic.mytopic.partition.1.currentOffset。成功提交位点的次数（commitsSucceeded）注册在 <some_parent_groups>.operator.KafkaSourceReader.commitsSucceeded。 指标列表

| 指标名称 | 描述 | 范围 |
|---|---|---|
| currentOffset | 当前消费位点 | TopicPartition |
| committedOffset | 当前提交位点 | TopicPartition |
| commitsSucceeded | 成功提交的次数 | KafkaSourceReader |
| commitsFailed | 失败的提交次数 | KafkaSourceReader |

Kafka Consumer指标 Kafka Consumer的指标注册在指标组KafkaSourceReader.KafkaConsumer。例如Kafka Consumer指标records-consumed-total注册在 <some_parent_groups>.operator.KafkaSourceReader.KafkaConsumer.recordsconsumed-total。 您可以使用配置项register.consumer.metrics配置是否注册Kafka消费者的指标。默认此选项设置为true。对于Kafka Consumer的指标，您可以参见Apache Kafka。 构建Kafka Producer Flink Kafka Producer可以实现将流数据写入一个或多个Kafka Topic。

```
DataStream<String> stream = ... Properties properties = new Properties(); properties.setProperty("bootstrap.servers", "localhost:9092"); FlinkKafkaProducer<String> myProducer = new FlinkKafkaProducer<>(
        "my-topic",                  // target topic
        new SimpleStringSchema(),    // serialization schema
        properties,                  // producer config
        FlinkKafkaProducer.Semantic.EXACTLY_ONCE); // fault-tolerance
stream.addSink(myProducer);
```

您需要配置以下参数。 实时计算（流计算）

| 参数 | 说明 |
|---|---|
| Topic | 数据写入的默认Topic名称。 |
| 数据序列化 | 用于将数据序列化的SerializationSchema或KafkaSerializationSchema。 Flink Kafka Producer需要知道如何将Java或Scala对象转换为二进制数据，KafkaSerializationSchema允许用户指定如何进行数据的序列化。ProducerRecord<byte[], byte[]> serialize(T element, Long timestamp)方法会在每条数据流入的时候调用，来生成 ProducerRecord写入Kafka。 用户可以对每条数据如何写入Kafka进行细粒度地控制。通过ProducerRecord可以进行以下操作： 设置写入的Topic名称。 定义消息键（Key）。 指定数据写入的Partition。 |
| Kafka 客户端属性 | bootstrap.servers必填，以逗号分隔的Kafka Broker列表。 |
| 容错语义 | 启用Flink的Checkpoint后，Flink Kafka Producer可以保证精确一次的语义。除了启用Flink的 Checkpoint外，您还可以通过Semantic参数来指定不同的容错语义，Semantic参数详情如下： Semantic.NONE：Flink不做任何保证，数据可能会丢失或重复。 Semantic.AT LEAST ONCE（默认设置）：保证不会丢失任何数据，但可能会重复。 _ _ Semantic.EXACTLY ONCE：使用Kafka事务提供精确一次的语义保证。 _ |

**EXACTLY_ONCE语义注意事项**

当使用事务写入Kafka时，请为所有消费Kafka数据的应用配置isolation.level参数。该参数取值如下： read_committed：只读取已提交的数据。 read_uncommitted（默认值）：可以读取未提交的数据。 Semantic.EXACTLY_ONCE模式依赖于在从某个Checkpoint恢复后，且在该Checkpoint开始之前所提交的事务。如果Flink作业崩溃与完成重启之间的时间大于Kafka的事务超时时间，则会有数据丢失，因为 Kafka会自动中止超过超时时间的事务。因此，请根据您的预期停机时间适当地配置您的事务超时。 Kafka Broker默认的transaction.max.timeout.ms设置为15分钟，Producer设置的事务超时不能超过 Broker指定的时间。Flink Kafka Producer默认会将Kafka Producer配置中的 transaction.timeout.ms属性设置为1小时，因此在使用Semantic.EXACTLY_ONCE模式前，需要增加 Broker端的transaction.max.timeout.ms值。 Semantic.EXACTLY_ONCE模式为在Flink Kafka Producer实例中使用一个固定大小的Kafka Producer池。每个Checkpoint会使用池中的一个Kafka Producer。如果并发的Checkpoint数量超过 Producer池的大小，Flink Kafka Producer会抛出异常并使整个作业失败。请相应地配置Producer池大小和最大并发的Checkpoint数量。 Semantic.EXACTLY_ONCE会尽可能清除阻止Consumer从Kafka topic中读取数据的残留事务。但如果Flink作业在第一个 Checkpoint之前就出现故障，则在重启该作业后并不会保留重启前Producer池的信息。因此，在第一个Checkpoint完成之前缩减Flink作业的并行度是不安全的，即使要缩减并行度，也不能小于FlinkKafkaProducer.SAFE_SCALE_DOWN_FACTOR。 对于在read_committed模式下运行的Kafka Consumer，任何未结束（既未中止也未完成）的事务都将阻塞对该Kafka Topic的所有读取。如果您按照以下步骤进行了操作： 实时计算（流计算） i. 用户开启事务1并通过该事务写入了一些数据。 ii. 用户开启事务2并通过该事务写入了更多的数据。 iii. 用户提交事务2。 即使来自事务2的数据已经提交，在事务1提交或中止之前，事务2的数据对消费者是不可见的。因此： 在Flink作业正常工作期间，您可以预期写入Kafka topic的数据会有延迟，约为Checkpoint的平均间隔。 在Flink作业失败的情况下，该作业正在写入的Topic将会阻塞Consumer的读取，直到作业重新启动或事务超时。

### 实时数仓Hologres

**背景信息**

实时数仓Hologres是一站式实时数据仓库引擎，支持海量数据实时写入、实时更新、实时分析，支持标准 SQL（兼容PostgreSQL协议），支持PB级数据多维分析（OLAP）与即席分析（Ad Hoc），支持高并发低延迟的在线数据服务（Serving），与MaxCompute、Flink、DataWorks深度融合，提供离在线一体化全栈数仓解决方案。Hologres连接器支持的信息如下。

| 类别 | 详情 |
|---|---|
| 支持类型 | 源表、维表和结果表 |
| 运行模式 | 流模式和批模式 |
| 数据格式 | 暂不支持 |
| 特有监控指标 | 源表： numRecordsIn numRecordsInPerSecond 结果表： numRecordsOut numRecordsOutPerSecond currentSendTime |
| API种类 | Datastream和SQL |
| 是否支持更新或删除结果表数据 | 是 |

**特色功能**

**源表**

实时计算（流计算）

| 功能 | 详情 |
|---|---|
| 实时消费Hologres | 支持作为非Binlog Source读取Hologres全量数据。 支持实时消费Hologres的Binlog数据。 支持非CDC模式消费。 支持CDC模式消费。 支持全增量一体源表消费。 |

**结果表**

| 功能 | 详情 |
|---|---|
| 流式语义 | 支持写入Changelog消息。 |
| 宽表Merge与局部更新功能 | 只更新修改部分的数据，而非整行更新。 |
| 作为CTAS和CDAS的目标端 | 支持实时同步单表、整库的数据以及相应的表结构变更到Hologres表中。 |
| 插入部分列说明仅实时计算引擎VVR 6.0.7及以上版本支持。 | 支持将Flink INSERT DML中指定的列名下推给连接器，从而仅更新指定的列。 |

**前提条件**

已创建Hologres表。

**使用限制**

通用： Hologres连接器不支持访问Hologres外部表。 源表独有： Flink默认以批模式读取Hologres源表数据，即只扫描一次Hologres全表，扫描结束，消费结束，新到 Hologres源表的数据不会被读取。从VVR 6.0.3版本开始，Hologres源表在批模式读取时支持filter下推，详见源表独有参数 `enable_filter_push_down` 。 实时计算引擎8.0以下版本Hologres CDC模式暂不支持定义Watermark。如果您需要进行窗口聚合， 您可以采用非窗口聚合的方式。 结果表独有：无。 维表独有： 维表建议使用主键作为Join条件，对于此类主键点查的维表，创建Hologres表时建议选择行存模式，列存模式对于点查场景性能开销较大。选择行存模式创建维表时必须设置主键，并且将主键设置为 Clustering Key才可以工作。 实时计算（流计算） 如果业务需要，无法使用主键作为Join条件，对于此类非主键点查的维表（即一对多的查询），创建 Hologres表时建议选择列存模式，并合理设置分布键Distribution Key以及Event Time Column（Segment Key）以优化查询性能。

**注意事项**

**使用了rpc模式时，VVR版本升级注意事项：**

Hologres 2.0版本下线了rpc（用于维表与结果表）模式，全面转为jdbc相关模式（目前包括jdbc、 jdbc_fixed和jdbc_copy等），rpc模式不会对同一批次中相同主键的数据做去重，如果业务场景需要保留完整的数据，切换为jdbc模式后，可以通过设置'jdbcWriteBatchSize'='1'防止去重，或者升级到VVR 8.0.5版本配置deduplication.enabled参数为false。 如果您作业中存在使用了rpc模式读写Hologres的情况，此时如果您需要将VVR 4.x升级到VVR 6.x或 VVR 8.x，请按照以下情况进行处理： 升级到VVR 6.0.4～6.0.6版本，可能会抛出异常。推荐维表和结果表使用jdbc_fixed或jdbc模式。 升级到VVR 6.0.7及以上版本，无需您做任何处理，Flink系统会自动替换rpc为jdbc相关模式。

**使用binlog源表且未指定jdbc模式时，VVR版本升级注意事项：**

Hologres 2.0版本开始有限支持holohub（用于Binlog源表）模式，Hologres 2.1版本彻底下线了 holohub模式，全面转为jdbc模式。 如果您作业中存在消费binlog源表的情况，而且binlog源表未通过sdkmode='jdbc'指定jdbc模式，默认会使用holohub模式。此时如果您需要将VVR 4.x升级到VVR 6.x或VVR 8.x，请按照以下情况进行处理： 如果Hologres版本是2.0。 升级到VVR 6.0.7～VVR 8.0.3版本，仍然可以继续使用holohub模式。 升级到VVR 8.0.4及以上版本，可能抛出权限不足的异常，需要特别配置用户权限。 如果Hologres版本是2.1。 升级到VVR 6.0.7～VVR 8.0.4版本，可能无法正常消费Binlog，建议升级到VVR 8.0.5。 升级到VVR 8.0.5及以上版本，无需您做任何处理，Flink系统会自动替换holohub模式为jdbc模式。

**语法结构**

```
CREATE TABLE hologres_table (
  name VARCHAR,
  age BIGINT,
  birthday BIGINT,
  PRIMARY KEY (name) NOT ENFORCED
) WITH (
  'connector' = 'hologres',
  'dbname' = '<yourDBName>',
  'tablename' = '<yourTableName>',
  'username' = '${secret_values.ak_id}',
  'password' = '${secret_values.ak_secret}',
  'endpoint' = '<yourEndpoint>',
  'sdkmode' = 'jdbc'
);
```

**WITH参数**

通用实时计算（流计算）

| 参数 | 说明 | 数据类型 | 是否必填 |  | 默认值 | 备注 |  |
|---|---|---|---|---|---|---|---|
| connect or | 表类型。 | String | 是 |  | 无 | 固定值为 hologres 。 |  |
| dbname | 数据库名称。 | String | 是 |  |  | Hologres V2.0版本推出了全新的弹性高可用实例形态，将计算资源分解为不同的计算组（Virtual Warehouse），更好的服务于高可用部署。不同的计算组使用相同的Endpoint，您可以通过在dbname参数后添加特定的后缀来指定连接某个计算组。例如某张维表希望连接特定的计算组read warehouse，可以通 _ 过 'dbname' = 'db test@read warehouse' 方式指定。 _ _ 说明仅JDBC相关模式支持使用计算组，详见源表、维表和结果表WITH参数中的sdkMode参数。 |  |
|  |  |  |  |  |  |  | _ 'dbname' = |
|  |  |  |  |  | 无 | 'db test@read warehouse' _ _ |  |
| tablena me | 表名称。 | String | 是 |  | 无 | 如果Schema不为Public时，则tablename需要填写为 schema.tableName。 |  |
| userna me | 用户名，请填写阿里云账号的 AccessKe y ID。 | String | 是 |  | 无 | 无。 |  |
| passwo rd | 密码，请填写阿里云账号的 AccessKe y Secret。 | String | 是 |  | 无 | 无。 |  |
| endpoin t | Hologres 服务地址。 | String | 是 |  | 无 | 请联系阿里云运维工程师获取。 |  |

实时计算（流计算）

| connect ion.ssl. mode |  | 是否启用 SSL（Sec ure Sockets Layer）传输加密，以及启用采用何种模式。 | String | 否 | disa ble | 参数取值如下： disable（默认值）：不启用传输加密。 require：启用SSL，只对数据链路加密。 verify-ca：启用SSL，加密数据链路，同时使用CA 证书验证Hologres服务端的真实性。 verify-full：启用SSL，加密数据链路，使用CA证书验证Hologres服务端的真实性，同时比对证书内的 CN或DNS与连接时配置的Hologres连接地址是否一致。 说明 VVR 8.0.5及以上版本开始支持此参数。 Hologres自1.1版本起支持SSL传输加密的require模式，2.1版本起新增支持 verify-ca和verify-full模式。 当配置为verify-ca或者verify-full时，需要同时配置connection.ssl.root- cert.location参数。 |  |  |
|---|---|---|---|---|---|---|---|---|
| connect ion.ssl.r oot- cert.loc ation |  | 当传输加密模式需要证书时，配置证书的路径。 | String | 否 | 无 | 当connection.ssl.mode配置为verify-ca或者verify- full时，需要同时配置CA证书的路径。证书可以使用实时计算控制台的资源上传功能上传至平台，上传后文件存放在/flink/usrlib目录下。例如，需要使用的CA证书文件名为certificate.crt，则上传后参数取值应该为 '/flink/usrlib/certificate.crt'。 说明 VVR 8.0.5及以上版本开始支持此参数。 |  |  |
| jdbcRet ryCount |  | 当连接故障时，写入和查询的重试次数。 | Intege r | 否 | 10 | 无。 |  |  |
| jdbcRet rySleepI nitMs |  | 每次重试的固定等待时 | Long | 否 | 100 | 实际重试的等待时间的计算公式为 jdbcRetrySleepInitMs+retry*jdbcRetrySle epStepMs 。单位为毫秒。 |  |  |
|  |  |  |  |  |  |  | jdbcRetrySleepInitMs+retry*jdbcRetrySle |  |
|  | s | 间。 |  |  | 0 | epStepMs |  |  |
| jdbcRet rySleep StepMs |  | 每次重试的累加等待时 | Long | 否 | 500 | 实际重试的等待时间的计算公式为 jdbcRetrySleepInitMs+retry*jdbcRetrySle epStepMs 。单位为毫秒。 |  |  |
|  |  |  |  |  |  |  | jdbcRetrySleepInitMs+retry*jdbcRetrySle |  |
|  | Ms | 间。 |  |  | 0 | epStepMs |  |  |
| jdbcCon nection MaxIdle Ms |  | JDBC连接的空闲时间。 | Long | 否 | 600 00 | 超过这个空闲时间，连接就会断开释放掉。单位为毫秒。 |  |  |

实时计算（流计算）

| jdbcMet aCache TTL | 本地缓存 TableSch ema信息的过期时间。 | Long | 否 | 600 00 | 单位为毫秒。 |
|---|---|---|---|---|---|
| jdbcMet aAutoR efreshF actor | 如果缓存的剩余时间小于触发时间，则系统会自动刷新缓存。 | Intege r | 否 | 4 | 缓存的剩余时间计算方法：缓存的剩余时间=缓存的过期时间 - 缓存已经存活的时间。缓存自动刷新后，则从 0开始重新计算缓存的存活时间。 触发时间计算方法：jdbcMetaCacheTTL/jdbcMetaAutoRefres hFactor两个参数的比值。 |
| type- mappin g.timest amp- converti ng.lega cy | Flink和 Hologres 之间是否进行时间类型的相互转换。 | Boole an | 否 | true | 参数取值如下： true：不进行相互转换。时区转换将采用运行环境中的JVM时区。 false（推荐）：进行相互转换。时区转换将使用 Flink所配置的时区。 说明仅实时计算引擎VVR 8.0.6及以上版本支持该参数。 property-version=0时，默认值为 true；property-version=1时，默认值为false。 |
| proper ty- versio n | Connecto r参数版本。 | Intege r | 否 | 0 | 可填的值为0和1，默认值为0。 说明仅VVR 8.0.6及以上版本支持配置该参数。 在不同参数版本里，可用的参数集合和参数的默认值可能不同。如果存在区别，区别详情会在参数的说明部分描述。 推荐使用参数版本1。 |

源表独有

| 参数 | 说明 | 数据类型 | 是否必填 | 默认值 | 备注 |
|---|---|---|---|---|---|
| field deli _ miter | 导出数据时， 不同行之间使用的分隔符。 | String | 否 | "\u0002" | 无。 |

实时计算（流计算）

| binlog | 是否消费 Binlog数据。 | Boole an | 否 | false | 参数取值如下： true：消费Binlog数据。 false（默认值）：不消费Binlog数据。 说明实时计算引擎VVR 8.0.6及以上版本支持多版本默认值。 property-version=0时，默认值为false。 property-version=1时，默认值为true。 |
|---|---|---|---|---|---|
|  |  |  |  |  | 参数取值如下： holohub（默认值）：使用holohub模式消费binlog。 jdbc：使用jdbc模式消费binlog。 jdbc fixed: 使用fixed jdbc模式消费 _ binlog，与jdbc模式的区别在于不受连接数限制。 |

实时计算（流计算）

| sdkMode | SDK模式。 | String | 否 | holohub | 说明 VVR 6.0.3及以下版本：不支持配置该参数。 VVR 6.0.4～6.0.6版本：推荐使用默认配置，即holohub。 VVR 6.0.7及以上版本：推荐配置为jdbc。 Hologres实例为2.0 以下版本，Flink系统采用您配置的参数值。 Hologres实例为2.0 及以上版本，由于 Hologres 2.0版本下线了holohub服务， 此时如果您配置了 holohub，Flink系统自动切换为jdbc。但是如果您配置为 jdbc，Flink系统采用 jdbc。 VVR 8.0.4～8.0.5： Hologres实例为2.0 版本，Flink系统自动切换为jdbc。可能存在权限不足等问题。 Hologres实例为2.1 及以上版本，Flink系 |  |  |
|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  | 说明 VVR 6.0.3及以下版本：不支持配置该参数。 VVR 6.0.4～6.0.6版本：推荐使用默认配置，即holohub。 VVR 6.0.7及以上版本：推荐配置为jdbc。 Hologres实例为2.0 以下版本，Flink系统采用您配置的参数值。 Hologres实例为2.0 及以上版本，由于 Hologres 2.0版本下线了holohub服务， 此时如果您配置了 holohub，Flink系统自动切换为jdbc。但是如果您配置为 jdbc，Flink系统采用 jdbc。 VVR 8.0.4～8.0.5： Hologres实例为2.0 版本，Flink系统自动切换为jdbc。可能存在权限不足等问题。 Hologres实例为2.1 及以上版本，Flink系 |  |
|  |  |  |  |  |  | 统自动切换为jdbc。 VVR 8.0.6及以上版本： Hologres实例为 2.1.27及以上版本，Flink系统自动切换为jdbc fixed模 _ 式。 Hologres实例为 2.1.0～2.1.26版本，Flink系统自动切换为jdbc模式。 Hologres实例为2.0 版本，Flink系统会尝试使用jdbc模式，如果存在权限不足等异常，会自动选择 holohub模式启动。 |  |

实时计算（流计算）

| jdbcBinl ogSlotNa me | JDBC模式的 binlog源表的 Slot名称。 | String | 否 | 无 | 仅在sdkMode配置为jdbc时生效，如果用户未配置，连接器会默认创建一个Slot来使用。 说明 Hologres实例2.1版本起，不再需要配置此参数，连接器也不会尝试自动创建。 |
|---|---|---|---|---|---|
| binlogM axRetryT imes | 读取Binlog数据出错后的重试次数。 | Intege r | 否 | 60 | 无。 |
| binlogRe tryInterv alMs | 读取Binlog数据出错后的重试时间间隔。 | Long | 否 | 2000 | 单位为毫秒。 |
| binlogBa tchRead Size | 批量读取 Binlog的数据行数。 | Intege r | 否 | 100 | 无。 |
| cdcMode | 是否采用CDC 模式读取 Binlog数据。 | Boole an | 否 | false | 参数取值如下： true：CDC模式读取Binlog数据。 false（默认值）：非CDC模式读取 Binlog数据。 说明实时计算引擎VVR 8.0.6及以上版本支持多版本默认值。 property-version=0时，默认值为false。 property-version=1时，默认值为true。 |
| upsertSo urce | 源表是否使用 upsert类型的 Changelog。 | Boole an | 否 | false | 仅在CDC模式下生效。参数取值如下： true：仅支持Upsert类型，包括 INSERT、DELETE和UPDATE AFTER。 _ false（默认值）：支持所有类型，包括 INSERT、DELETE、UPDATE BEFORE _ 和UPDATE AFTER。 _ 说明如果下游包含回撤算子（例如使用 ROW NUMBER OVER WINDOW去 _ 重），则需要设置upsertSource为 true，此时源表会以Upsert方式从 Hologres中读取数据。 |

实时计算（流计算）

| binlogSt artupMo de | Binlog数据消费模式。 | String | 否 | earliest Offset | 参数取值如下： initial：先全量消费数据，再读取Binlog 开始增量消费。 earliestOffset（默认值）：从最早的 Binlog开始消费。 timestamp：从设置的startTime开始消费Binlog。 说明如果设置了startTime或者在启动界面选择了启动时间，则 binlogStartupMode强制使用 timestamp模式，其他消费模式不生效，即startTime参数优先级更高。 说明实时计算引擎VVR 8.0.6及以上版本支持多版本默认值。 property-version=0时，默认值为false。 property-version=1时，默认值为true。 |
|---|---|---|---|---|---|
| startTim e | 启动位点的时间。 | String | 否 | 无 | 格式为yyyy-MM-dd hh:mm:ss。如果没有设置该参数，且作业没有从State恢复， 则从最早的Binlog开始消费Hologres数据。 |
| jdbcScan FetchSiz e | 扫描时攒批大小。 | Intege r | 否 | 256 | 无。 |
| jdbcScan Timeout Seconds | 扫描操作超时时间。 | Intege r | 否 | 60 | 单位为秒。 |
| jdbcScan Transact ionSessi onTimeo utSecon ds | 扫描操作所在事务的超时时间。 | Intege r | 否 | 600秒 （0表示不超时） | 对应Hologres的GUC参数 idle in transaction session timeout。 _ _ _ _ |

实时计算（流计算）

| enable fi _ lter pus _ h down _ | 全量读取阶段是否进行filter 下推。 | Boole an | 否 | false | 参数取值如下： false（默认值）：不进行filter下推。 true：读取全量数据时，将支持的过滤条件下推到Hologres执行。包括非Binlog Source全量读取以及Binlog Source使用全增量一体化消费模式时的全量阶段。 重要实时计算引擎Flink1.15-vvr-6.0.3 到Flink1.15-vvr-6.0.5默认会进行 filter下推，但如果作业使用了 hologres维表，且写入的DML中包含有对维表非主键字段的过滤条件时，维表的filter会被错误的下推， 可能导致维表join出现错误结果。因此推荐使用实时计算引擎Flink1.15- vvr-6.0.6及以上版本，并在源表增加此参数来开启过滤条件下推功能。 |
|---|---|---|---|---|---|

结果表独有

| 参数 | 说明 | 数据类型 | 是否必填 | 默认值 | 备注 |
|---|---|---|---|---|---|
|  |  |  |  |  | 参数取值如下： jdbc：默认值，表示使用jdbc模式进行写入。 jdbc copy：是否使用fixed copy方式写入。 _ fixed copy是hologres1.3新增的能力，相比通过insert 方法（jdbc模式）进行写入，fixed copy方式可以更高的吞吐（因为是流模式），更低的数据延时，更低的客户端内存消耗（因为不攒批）。但此模式暂不支持delete 数据，也不支持写入分区父表，不支持 ignoreNullWhenUpdate参数。 rpc：表示使用rpc模式进行写入，与useRpcMode参数一致，与jdbc模式的区别在于不占用连接数，并且不支持写入Hologres的JSONB、RoarinBitmap类型。 jdbc fixed（beta功能）：表示使用fixed jdbc方式进 _ 行写入， 需要Hologres引擎版本大于等于1.3，与jdbc模式的区别在于不占用连接数，不支持写入Hologres的 Jsonb，RoarinBitmap类型。 |

实时计算（流计算）

| sdkM ode | SDK模式。 | String | 否 | jdbc | 说明 VVR 6.0.3以下版本：不支持配置该参数。 VVR 6.0.4～VVR 6.0.6版本：推荐配置为 jdbc。 VVR 6.0.7～VVR 8.0.1版本：推荐配置为 jdbc。 如果Hologres实例为2.0以下版本，Flink系统采用您配置的参数值。 如果Hologres实例为2.0及以上版本，由于Hologres 2.0及以上版本下线了rpc服务，此时如果您将该参数配置为rpc，Flink系统将自动切换该参数值为jdbc fixed，但是如果您配 _ 置为其他值，Flink系统将采用您配置的参数值。 rpc模式不会对同一批次中相同主键 |
|---|---|---|---|---|---|
|  |  |  |  |  | 的数据做去重，如果业务场景需要保留完整的数据，切换为jdbc模式后， 可以通过设置'jdbcWriteBatchSize'='1'防止去重。 VVR 8.0.3及以上版本：推荐配置为jdbc。 自此版本开始，无论Hologres实例版本，都不再支持rpc模式，如果选择rpc模式，将自动切换该参数值为jdbc fixed且设 _ 置'jdbcWriteBatchSize'='1'防止去重。 VVR 8.0.5及以上版本：推荐配置为jdbc。 如果选择rpc模式，将自动切换该参数值为 jdbc fixed且设置deduplication.enabled参 _ 数为false防止去重。 |
| bulkl oad | 是否采用 bulklo ad写入。 | Boole an | 否 | false | 仅在sdkMode设置为jdbc copy时生效。bulkload写入目 _ 前仅适用于无主键表或者主键保证不重复的有主键表（主键重复会抛出异常），相比默认的jdbc copy，写入使用更少 _ 的Hologres资源。 说明仅实时计算引擎VVR 8.0.5及以上版本且Hologres实例为2.1及以上版本支持该参数。 |

实时计算（流计算）

| useR pcMo de | 是否通过RPC 方式使用 Holog res连接器。 | Boole an | 否 | false | 参数取值如下： true：使用RPC方式使用Hologres连接器。 与sdkMode参数设置为rpc效果相同，通过RPC方式会降低SQL连接数。 false（默认值）：使用JDBC方式使用Hologres连接器。 通过JDBC方式会占用SQL连接，导致JDBC连接数增加。 说明 Hologres 2.0版本下线了rpc模式，推荐使用 sdkMode参数来选择jdbc或者jdbc fixed模 _ 式。 实时计算引擎VVR 6.0.7及VVR 8.0.1版本在检测到Hologres实例是2.0及以上版本时，会自动切换rpc模式为jdbc fixed模式。 _ 实时计算引擎VVR 8.0.3及以上版本会自动切换rpc模式为jdbc fixed模式。 _ rpc模式不会对同一批次中相同主键的数据做去重，如果业务场景需要保留完整的数据变化记录，推荐使用实时计算引擎VVR 8.0.5及以上版本，jdbc模式可以配置 deduplication.enabled参数为false不进行去重。 property-version=1时，该参数下线。 |
|---|---|---|---|---|---|
| muta tetyp e | 数据写入模式。 | String | 否 | insert orign ore | 实时计算引擎VVR 8.0.6及以上版本支持多版本默认值。 property-version=0时，默认值为 insertorignore。 property-version=1时，默认值为 insertorupdate。 |
| partit ionro uter | 是否写入分区表。 | Boole an | 否 | false | 无。 |
| creat epart table | 当写入分区表时，是否根据分区值自动创建不存在的分区表。 | Boole an | 否 | false | RPC模式下，如果分区值中存在短划线（-），暂不支持自动创建分区表。 说明 Hologres实例1.3.22及以上版本开始支持使用Date类型做分区键。实时计算引擎VVR 8.0.3及以上版本，支持使用Date类型做分区键时自动创建分区表。 请确保分区值不会出现脏数据，否则会创建错误的分区表导致Failover，建议慎用该参数。 当sdk mode设置为jdbc copy时，不支持写 _ _ 入分区父表。 |

实时计算（流计算）

| ignor edele te | 是否忽略撤回消息。 | Boole an | 否 | true | 仅在使用实时数仓Hologres时生效。 实时计算引擎VVR 8.0.6及以上版本支持多版本默认值。 property-version=0时，默认值为true。 property-version=1时，默认值为false。 |
|---|---|---|---|---|---|
| conn ectio nSize | 单个 Flink 结果表任务所创建的 JDBC 连接池大小。 | Intege r | 否 | 3 | 如果作业性能不足，建议您增加连接池大小。连接池大小和数据吞吐成正比。 |
| jdbc Write Batch Size | JDBC 模式，H ologr es Sink 节点数据攒批条数 （不是来一条数据处理一条，而是攒一批再处理）的最大值。 | Intege r | 否 | 256 | 单位为数据行数。 说明 jdbcWriteBatchSize、jdbcWriteBatchByteS ize和jdbcWriteFlushInterval三者之间为或的关系。如果同时设置了这三个参数，则满足其中一个， 就进行写入结果数据。 |
| jdbc Write Batch ByteS ize | JDBC 模式，H ologr es Sink 节点数据攒批字节数 （不是来一条数据处理一条，而是攒一批再处理）的最大值。 | Long | 否 | 2097 152（ 2*10 24*1 024） 字节， 即2 MB | jdbcWriteBatchSize、jdbcWriteBatchByteSize和 jdbcWriteFlushInterval三者之间为或的关系。如果同时设置了这三个参数，则满足其中一个，就进行写入结果数据。 |

实时计算（流计算）

| jdbc Write FlushI nterv al | JDBC 模式，H ologr es Sink 节点数据攒批写入 Holog res的最长等待时间。 | Long | 否 | 1000 0 | 单位为毫秒。 jdbcWriteBatchSize、jdbcWriteBatchByteSize和 jdbcWriteFlushInterval三者之间为或的关系。如果同时设置了这三个参数，则满足其中一个，就进行写入结果数据。 |
|---|---|---|---|---|---|
| ignor eNull When Upda te | 当 mutat etype ='ins ertOr Updat e'时， 是否忽略更新写入数据中的 Null 值。 | Boole an | 否 | false | 取值说明如下： false（默认值）：将Null值写到Hologres结果表里。 true：忽略更新写入数据中的Null值。 说明当sdk mode设置为jdbc copy时，不支持此参数。 _ _ |
| conn ectio nPool Name | 连接池名称。 同一个 Task Mana ger 中，配置相同名称的连接池的表可以共享连接池。 | String | 否 | 无 | 取值为非 'default' 的任意字符串。如果多个表设置相同的连接池，则这些使用相同连接池的表的connectionSize参数也需要相同。 说明 VVR 4.0.12～VVR 8.0.3版本：默认不共享，每个表使用自己的连接池。 VVR 8.0.4以上版本：同一个作业中 endpoint相同的表会默认共享连接池。作业中表数量较多时连接数可能相对不足影响性能，这种情况下推荐为不同的表设置不同的 connectionPoolName。 此参数可以按需配置，比如作业中有维表 A，B以及结果表C，D，E五张hologres表， 可以A表和B表使用'pool1'，C表和D表使用'pool2'，E表流量较大，单独使用'pool3'。 |

实时计算（流计算）

| jdbcE nable Defa ultFor NotN ullCol umn | 如果将 Null值写入 Holog res表中Not Null且无默认值的字段，是否允许连接器帮助填充一个默认值。 | Boole an | 否 |  | true | 参数取值如下： true（默认值）：允许连接器填充默认值并写入，规则如下。 如果字段是String类型，则默认写为空（""）。 如果字段是Number类型，则默认写为0。 如果是Date、timestamp或timestamptz时间类型字段，则默认写为1970-01-01 00:00:00。 false：不填充默认值，写Null到Not Null字段时，会抛出异常。 |  |
|---|---|---|---|---|---|---|---|
| remo ve- u000 0-in- text.e nable d | 如果写入时字符串类型包含 \u000 0非法字符， 是否允许连接器帮助去除。 | Boole an | 否 |  |  | 参数取值如下： false（默认值）：连接器不对数据进行操作，但碰到脏数据时写入可能抛出如下异常， ERROR: invalid byte sequence for encoding "UTF8": 0x00 此时需要在源表提前处理脏数据，或者在SQL中定义脏数据处理逻辑。 true：连接器会帮助去除字符串类型中的\u0000，防止写入抛出异常。 |  |
|  |  |  |  |  |  |  | ERROR: invalid |
|  |  |  |  |  | false | byte sequence for encoding "UTF8": 0x00 |  |
| partia l- insert .enab led | 是否只插入 INSER T语句中定义的字段。 | Boole an | 否 |  | false | 参数取值如下： false（默认值）：无论INSERT语句中声明了哪些字段， 都会更新结果表DDL中定义的所有字段，对于未在 INSERT语句中声明的字段，会被更新为null。 true：将INSERT语句中定义的字段下推给连接器，从而可以只对声明的字段进行更新或插入。 说明仅实时计算引擎VVR 6.0.7及以上版本支持该参数。 此参数仅在mutatetype参数配置为 InsertOrUpdate时生效。 |  |

实时计算（流计算）

| dedu plicat ion.e nable d | jdbc及 jdbc f _ ixed 模式写入攒批过程中，是否进行去重。 | Boole an | 否 | true | 参数取值如下： true（默认值）：如果一批数据中有主键相同的数据， 默认进行去重，只保留最后一条到达的数据。以两个字段，其中第一个字段为主键的数据举例： INSERT (1,'a') 和 INSERT (1,'b') 两条记录先后到达，去重之后只保留后到达的 (1,'b') 写入Hologres结果表中。 Hologres结果表中已经存在记录 (1,'a') ，此时 DELETE (1,'a') 和 INSERT (1,'b') 两条记录先后到达，只保留后到达的 (1,'b') 写入 hologres中，表现为直接更新，而不是先删除再插入。 false：在攒批过程中不进行去重，如果发现新到的数据和目前攒批的数据中存在主键相同的情况，先将攒批数据写入，写入完成之后再继续写入新到的数据。 说明仅实时计算引擎VVR 8.0.5及以上版本支持该参数。 不允许攒批去重时，极端情况下（例如所有数据的主键都相同）写入会退化为不攒批的单条写入，对性能有一定影响。 |
|---|---|---|---|---|---|

维表独有

| 参数 | 说明 | 数据类型 | 是否必填 | 默认值 | 备注 |
|---|---|---|---|---|---|

实时计算（流计算）

| sdkMo de | SDK 模式。 | Strin g | 否 | jdbc | 参数取值如下： jdbc（默认值）：表示使用jdbc模式进行查询， 支持主键点查和非主键的查询，但是非主键的查询对性能影响较大，查询较慢。 rpc：表示使用rpc模式进行点查，与 useRpcMode参数一致，仅支持主键点查，即维表的主键字段必须与Flink Join On的字段完全匹配，与jdbc模式的区别在于不占用连接数，不支持读取Hologres的Jsonb，RoarinBitmap类型。 jdbc fixed：（beta功能，需要hologres引擎版 _ 本大于等于1.3）表示使用fixed jdbc方式进行点查，与jdbc模式的区别在于不占用连接数，且不支持读取Hologres的Jsonb，RoarinBitmap类型。仅支持主键点查，即维表的主键字段必须与 Flink Join On的字段完全匹配。 说明 VVR 6.0.3以下版本：不支持配置该参数。 VVR 6.0.4～VVR 6.0.6版本：推荐配置为jdbc。 在VVR 6.0.6版本，SDK模式选择为 jdbc时，如果维表字符串类型的查询结果中包含null值，可能抛出空指针异常，此时推荐您使用rpc模式绕过。 VVR 6.0.7及VVR 8.0.1：推荐配置为 jdbc。 如果Hologres实例为2.0以下版本，Flink系统将采用您配置的参数值。 如果Hologres实例为2.0及以上版本，由于Hologres 2.0 及以上版本下线了rpc服务， 此时如果您将该参数配置为了 rpc，Flink系统自动将参数值切换为jdbc fixed。但是如果 _ 您配置为其他值，Flink系统将采用您配置的参数值。 VVR 8.0.3及以上版本：推荐配置为 jdbc。 自此版本开始，无论 Hologres实例版本，都不再支持rpc模式，如果选择rpc模式，将自动切换该参数值为 jdbc fixed。 _ |
|---|---|---|---|---|---|

实时计算（流计算）

| useRp cMode | 是否通过 RPC 方式使用 Holog res连接器。 | Bool ean | 否 | false | 参数取值如下： true：使用RPC方式使用Hologres连接器。与 sdkMode参数设置为rpc效果相同。通过RPC方式会降低SQL连接数。 false（默认值）：使用JDBC方式使用Hologres 连接器。 通过JDBC方式会占用SQL连接，导致JDBC链接数增加。 说明 Hologres 2.0版本下线了rpc了服务，推荐使用sdkMode参数来选择 jdbc或者jdbc fixed模式。 _ 实时计算引擎VVR 6.0.7及VVR 8.0.1 版本在检测到Hologres实例是2.0及以上版本时，会自动切换rpc模式为 jdbc fixed模式。 _ 实时计算引擎VVR 8.0.3及以上版本会自动切换rpc模式为jdbc fixed模 _ 式。 |
|---|---|---|---|---|---|
| conne ctionSi ze | 单个 Flink 维表任务所创建的 JDBC 连接池大小。 | Integ er | 否 | 3 | 如果作业性能不足，建议您增加连接池大小。连接池大小和数据吞吐成正比。 |
| conne ctionP oolNa me | 连接池名称。 同一个 Task Mana ger 中， 配置相同名称的连接池的表可以共享连接池。 | Strin g | 否 | 无 | 取值为非 'default' 的任意字符串。如果多个表设置相同的连接池，则这些使用相同连接池的表的connectionSize参数也需要相同。 您可以按需配置此参数，例如作业中有维表A，B以及结果表C，D，E五张hologres表，可以A表和B表使用pool1，C表和D表使用pool2，E表流量较大， 单独使用pool3。 说明 VVR 4.0.12～VVR 8.0.3版本：默认不共享，每个表使用自己的连接池。 VVR 8.0.4以上版本：同一个作业中 Endpoint相同的表会默认共享连接池。作业中表数量较多时连接数可能相对不足影响性能，这种情况下推荐为不同的表设置不同的 connectionPoolName。 |

实时计算（流计算）

| jdbcR eadBa tchSiz e | 点查 Holog res维表时， 攒批处理的最大条数。 | Integ er | 否 | 128 | 无。 |
|---|---|---|---|---|---|
| jdbcR eadBa tchQu eueSiz e | 维表点查请求缓冲队列大小。 | Integ er | 否 | 256 | 无。 |
| jdbcR eadTi meout Ms | 维表点查的超时时间。 | Long | 否 | 默认值为0，表示不会超时 | 仅vvr 4.0.15-flink 1.13及以上版本、vvr 6.0.2- flink 1.15及以上版本支持该参数。 |
| jdbcR eadRe tryCou nt | 维表点查超时时的重试次数。 | Inter ger | 否 | VVR 8.0.5 以下版本：1 VVR 8.0.5 及以上版本：10 | 仅VVR 6.0.3以上版本支持该参数。 本参数与jdbcRetryCount不同，后者是指连接发生异常时的重试次数。 |
| jdbcSc anFetc hSize | 在一对多 join（ 即没有使用完整主键） 时使用 scan 接口，s can攒批处理数据的条数。 | Integ er | 否 | 256 | 无。 |

实时计算（流计算）

| jdbcSc anTim eoutS econd s | scan 操作的超时时间。 | Integ er | 否 | 60 | 单位为秒。 |
|---|---|---|---|---|---|
| cache | 缓存策略。 | Strin g | 否 | None | Hologres仅支持None和LRU两种缓存策略。 |
| cache Size | 缓存大小。 | Integ er | 否 | 10000 | 选择LRU缓存策略后，可以设置缓存大小。单位为条。 |
| cache TTLMs | 缓存更新时间间隔。 | Long | 否 | 见备注列。 | 单位为毫秒。cacheTTLMs默认值和cache的配置有关： 如果cache配置为LRU，则cacheTTLMs为缓存超时时间。默认不过期。 如果cache配置为None，则cacheTTLMs可以不配置，表示缓存不超时。 |
| cache Empty | 是否缓存 join结果为空的数据。 | Bool ean | 否 | true | true（默认值）：表示缓存join结果为空的数据。 false：表示不缓存join结果为空的数据。 |
| async | 是否异步返回数据。 | Bool ean | 否 | false | true：表示异步返回数据。 false（默认值）：表示不进行异步返回数据。 说明异步返回数据是无序的。 |

**使用示例**

**源表示例**

**非Binlog Source表**

实时计算（流计算）

```
CREATE TEMPORARY TABLE hologres_source (
  name varchar,
  age BIGINT,
  birthday BIGINT
) WITH (
  'connector'='hologres',
  'dbname'='<yourDbname>',
  'tablename'='<yourTablename>',
  'username' = '${secret_values.ak_id}',
  'password' = '${secret_values.ak_secret}',
  'endpoint'='<yourEndpoint>',
```

'field_delimiter'='|' --该参数可选。

```
  'sdkmode' = 'jdbc'
);
  name varchar,
  age BIGINT,
  birthday BIGINT
) WITH ( ); SELECT name, age, birthday from hologres_source;
```

**Binlog Source表**

Hologres连接器支持实时消费Hologres，即实时消费Hologres的Binlog数据。

**结果表示例**

实时计算（流计算）

```
  name varchar,
  age BIGINT,
  birthday BIGINT
) WITH ( ); CREATE TEMPORARY TABLE hologres_sink (
  name varchar,
  age BIGINT,
  birthday BIGINT
) WITH (
  'connector'='hologres',
  'dbname'='<yourDbname>',
  'tablename'='<yourTablename>',
  'username' = '${secret_values.ak_id}',
  'password' = '${secret_values.ak_secret}',
  'endpoint'='<yourEndpoint>'
); INSERT INTO hologres_sink SELECT * from datagen_source;
```

**维表示例**

```
  a INT,
  b BIGINT,
  c STRING,
  proctime AS PROCTIME()
) WITH ( ); CREATE TEMPORARY TABLE hologres_dim (
  a INT,
  b VARCHAR,
  c VARCHAR
) WITH (
  'connector' = 'hologres',
   ...
);
  a INT,
  b STRING
) WITH ( ); FROM datagen_source AS T JOIN hologres_dim FOR SYSTEM_TIME AS OF T.proctime AS H ON T.a = H.a;
```

实时计算（流计算）

**特色功能详解**

**流式语义**

流处理，也称为流数据或流事件处理，即对一系列无界数据或事件连续处理。执行流数据或流事件处理的系统通常允许您指定一种可靠性模式或处理语义，保证整个系统处理数据的准确性，因为网络或设备故障等可能会导致数据丢失。 根据Hologres Sink的配置和Hologres表的属性，流式语义分为以下两种： Exactly-once（仅一次）：即使在发生各种故障的情况下，系统只处理一次数据或事件。 At-least-once（至少一次）：如果在系统完全处理之前丢失了数据或事件，则从源头重新传输，因此可以多次处理数据或事件。如果第一次重试成功，则不必进行后续重试。 在Hologres结果表中使用流式语义，需要注意以下几点： 如果Hologres物理表未设置主键，则Hologres Sink使用At-least-once语义。 如果Hologres物理表已设置主键，则Hologres Sink通过主键确保Exactly-once语义。当同主键数据出现多次时，您需要设置**mutatetype**参数确定更新结果表的方式，**mutatetype**取值如下：
**insertorignore**（默认值）：保留首次出现的数据，忽略后续所有数据。
**insertorreplace**：后出现的数据整行替换已有数据。
**insertorupdate**：更新已有数据的部分列。例如一张表有a、b、c和d四个字段，a是PK（Primary
Key），写入Hologres时只写入a和b两个字段，在PK重复的情况下，系统只会更新b字段，c和d保持不变。

**说明**

当**mutatetype**设置为 `insertorreplace` 或 `insertorupdate` 时，系统根据主键更新数据。 Flink定义的结果表中的数据列数不一定要和Hologres物理表的列数一致，您需要保证缺失的列没有非空约束，即列值可以为Null，否则会报错。 默认情况下，Hologres Sink只能向一张表导入数据。如果导入数据至分区表的父表，即使导入成功，也会查询数据失败。您可以设置参数**partitionRouter**为true，开启自动将数据路由到对应分区表的功能。注意事项如下：
**tablename**参数需要填写为父表的表名。
如果没有提前创建分区表，需要在WITH参数中启用**createparttable=true**，从而支持自动创建分区表，否则会导入失败。

**宽表Merge和局部更新功能**

在把多个流的数据写到一张Hologres宽表的场景中，会涉及到宽表Merge和数据的局部更新。下面通过示例来介绍实现宽表merge的两种方式。

**说明**

本场景的两种实现方式均具有如下限制： 宽表必须有主键。 每个数据流的数据都必须包含完整的主键字段。 列存模式的宽表Merge场景在高RPS的情况下，CPU使用率会偏高，建议关闭表中字段的 Dictionary Encoding功能。

**方式一（推荐）**

实时计算（流计算）

**说明**

仅实时计算引擎VVR 6.0.7及以上版本支持使用此方式。 假设有两个Flink数据流，一个数据流中包含a、b和c字段，另一个数据流中包含a、d和e字段，Hologres宽表WIDE_TABLE包含a、b、c、d和e字段，其中a字段为主键。具体操作如下：
1. 使用Flink SQL创建一张Hologres结果表，并声明a、b、c、d、e五个字段，映射至宽表WIDE_TABLE。
2. 结果表的属性设置：
mutatetype设置为insertorupdate，可以根据主键更新数据。 ignoredelete设置为true，防止回撤消息产生Delete请求。
3. 将两个Flink数据流的数据分别INSERT至对应的结果表中。
`//` 已经定义的`source1`和`source2`

```
CREATE TEMPORARY TABLE hologres_sink ( -- 声明a,b,c,d,e五个字段
  a BIGINT,
  b STRING,
  c STRING,
  d STRING,
  e STRING,
  primary key(a) not enforced
) WITH (
  'connector'='hologres',
  'dbname'='<yourDbname>',
  'tablename'='<yourWideTablename>',  -- hologres宽表，包含a,b,c,d,e五个字段
  'username' = '${secret_values.ak_id}',
  'password' = '${secret_values.ak_secret}',
  'endpoint'='<yourEndpoint>',
```

`'mutatetype'='insertorupdate', --` 根据主键更新数据 `'ignoredelete'='true', --` 忽略回撤消息产生的`Delete`请求 `'partial-insert.enabled'='true' --` 开启部分列更新参数，支持仅更新`INSERT`语句中生命的字段

```
); BEGIN STATEMENT SET; INSERT INTO hologres_sink(a,b,c) select * from source1; -- 声明只插入a,b,c三个字段 INSERT INTO hologres_sink(a,d,e) select * from source2; -- 声明只插入a,d,e三个字段 END;
```

**方式二**

**说明**

仅实时计算引擎VVR 6.0.6及以下版本支持使用此方式。 假设有两个Flink数据流，一个数据流中包含a、b和c字段，另一个数据流中包含a、d和e字段，Hologres宽表WIDE_TABLE包含a、b、c、d和e字段，其中a字段为主键。具体操作如下：
1. 使用Flink SQL创建两张Hologres结果表，其中一张表只声明a、b和c字段，另一张表只声明a、d和e字
段。这两张表都映射至宽表WIDE_TABLE。
2. 两张结果表的属性设置：
mutatetype设置为insertorupdate，可以根据主键更新数据。 ignoredelete设置为true，防止回撤消息产生Delete请求。 实时计算（流计算）
3. 将两个Flink数据流的数据分别INSERT至对应的结果表中。
`//` 已经定义的`source1`和`source2`

```
CREATE TEMPORARY TABLE hologres_sink_1 ( -- 只声明a,b,c三个字段
  a BIGINT,
  b STRING,
  c STRING,
  primary key(a) not enforced
) WITH (
  'connector'='hologres',
  'dbname'='<yourDbname>',
  'tablename'='<yourWideTablename>',  -- hologres宽表，包含a,b,c,d,e五个字段
  'username' = '${secret_values.ak_id}',
  'password' = '${secret_values.ak_secret}',
  'endpoint'='<yourEndpoint>',
```

`'mutatetype' = 'insertorupdate', --` 根据主键更新数据 `'ignoredelete' = 'true' --` 忽略回撤消息产生的`Delete`请求

```
); CREATE TEMPORARY TABLE hologres_sink_2 ( -- 只声明a,d,e三个字段
  a BIGINT,
  d STRING,
  e STRING,
  primary key(a) not enforced
) WITH (
  'connector'='hologres',
  'dbname'='<yourDbname>',
  'tablename'='<yourWideTablename>',  -- hologres宽表，包含a,b,c,d,e五个字段
  'username' = '${secret_values.ak_id}',
  'password' = '${secret_values.ak_secret}',
  'endpoint'='<yourEndpoint>',
```

`'mutatetype'='insertorupdate', --` 根据主键更新数据 `'ignoredelete'='true' --` 忽略回撤消息产生的`Delete`请求

```
); BEGIN STATEMENT SET; INSERT INTO hologres_sink_1 select * from source1; INSERT INTO hologres_sink_2 select * from source2; END;
```

**作为CTAS和CDAS的目标端**

Hologres支持实时同步单表或整库级别的数据，在同步过程之中如果上游的表结构发生了变更也会实时同步到Hologres表中。新数据流到Hologres表时，Flink会先触发Hologres修改相应的表结构，然后再将数据写入到相应的表中。以上过程全部由Flink自动完成，您无需关心实现细节。

**DataStream API**

**重要**

通过DataStream的方式读写数据时，则需要使用对应的DataStream连接器连接Flink。Maven中央库中已经放置了Hologres DataStream连接器。VVR 6.0.7请使用其中的1.15-vvr-6.0.7-1版本的依赖。 实时计算（流计算）

**Hologres源表**

VVR提供了RichInputFormat的实现类HologresBulkreadInputFormat来读取Hologres表数据。以下为构建Hologres Source读取表数据的示例。

**VVR 6.0.7**

```
// set up the Java DataStream API final StreamExecutionEnvironment env = StreamExecutionEnvironment.getExecutionEnvironment();
```

`//` 初始化读取的表的`Schema`，需要和`Hologres`表`Schema`的字段匹配，可以只定义部分字段。

```
TableSchema schema = TableSchema.builder()
  .field("a", DataTypes.INT())
  .build();
```

`// Hologres`的相关参数。

```
Configuration config = new Configuration(); config.setString(HologresConfigs.ENDPOINT, "yourEndpoint"); config.setString(HologresConfigs.USERNAME, "yourUserName"); config.setString(HologresConfigs.PASSWORD, "yourPassword"); config.setString(HologresConfigs.DATABASE, "yourDatabaseName"); config.setString(HologresConfigs.TABLE, "yourTableName");
```

`//` 构建`JDBC Options`。

```
JDBCOptions jdbcOptions = JDBCUtils.getJDBCOptions(config); HologresBulkreadInputFormat inputFormat = new HologresBulkreadInputFormat(new HologresConnectionParam(config), jdbcOptions, schema, "", -1); TypeInformation<RowData> typeInfo = InternalTypeInfo.of(schema.toRowDataType().getLogicalType()); env.addSource(new InputFormatSourceFunction<>(inputFormat, typeInfo)).returns(typeInfo)
  .print();
env.execute();
```

**Hologres Binlog源表**

VVR提供了Source的实现类HologresBinlogSource来读取Hologres Binlog数据。以下为构建Hologres Binlog Source的示例。

**VVR 6.0.7**

实时计算（流计算）

```
final StreamExecutionEnvironment env = StreamExecutionEnvironment.getExecutionEnvironment();
```

`//` 初始化读取的表的`Schema`，需要和`Hologres`表`Schema`的字段匹配，可以只定义部分字段。

```
TableSchema schema = TableSchema.builder()
  .field("a", DataTypes.INT())
  .build();
```

`// Hologres`的相关参数。

```
Configuration config = new Configuration(); config.setString(HologresConfigs.ENDPOINT, "yourEndpoint"); config.setString(HologresConfigs.USERNAME, "yourUserName"); config.setString(HologresConfigs.PASSWORD, "yourPassword"); config.setString(HologresConfigs.DATABASE, "yourDatabaseName"); config.setString(HologresConfigs.TABLE, "yourTableName"); config.setString(HologresConfigs.SDK_MODE, "jdbc"); config.setBoolean(HologresBinlogConfigs.OPTIONAL_BINLOG, true); config.setBoolean(HologresBinlogConfigs.BINLOG_CDC_MODE, true);
```

`//` 构建`JDBC Options`。

```
JDBCOptions jdbcOptions = JDBCUtils.getJDBCOptions(config);
```

`//` 设置或创建默认`slotname`

```
config.setString(HologresBinlogConfigs.JDBC_BINLOG_SLOT_NAME, HoloBinlogUtil.getOrCreateDefaultSlotForJDBCBinlog(jdbcOptions)); boolean cdcMode = config.get(HologresBinlogConfigs.BINLOG_CDC_MODE)
  && config.get(HologresBinlogConfigs.OPTIONAL_BINLOG);
// 构建Binlog Record Converter。 JDBCBinlogRecordConverter recordConverter = new JDBCBinlogRecordConverter(
  jdbcOptions.getTable(),
  schema,
  new HologresConnectionParam(config),
  cdcMode,
  Collections.emptySet());
// 构建Hologres Binlog Source。 long startTimeMs = 0; HologresJDBCBinlogSource source = new HologresJDBCBinlogSource(
  new HologresConnectionParam(config),
  schema,
  config,
  jdbcOptions,
  startTimeMs,
  StartupMode.TIMESTAMP,
  recordConverter,
  "",
  -1);
env.fromSource(source, WatermarkStrategy.noWatermarks(), "Test source").print(); env.execute();
```

**说明**

方法buildRecordConverter不在VVR Connector依赖中，是示例代码中提供的方法。 实时计算（流计算）

**Hologres结果表**

VVR提供了OutputFormatSinkFunction的实现类HologresSinkFunction来写入数据。以下为构建 Hologres Sink的示例。

**VVR 6.0.7&VVR 8.0.1**

```
// set up the Java DataStream API final StreamExecutionEnvironment env = StreamExecutionEnvironment.getExecutionEnvironment();
```

`//` 初始化读取的表的`Schema`，需要和`Hologres`表`Schema`的字段匹配，可以只定义部分字段。

```
TableSchema schema = TableSchema.builder()
  .field("a", DataTypes.INT())
  .field("b", DataTypes.STRING())
  .build();
```

`// Hologres`的相关参数。

```
Configuration config = new Configuration(); config.setString(HologresConfigs.ENDPOINT, "yourEndpoint"); config.setString(HologresConfigs.USERNAME, "yourUserName"); config.setString(HologresConfigs.PASSWORD, "yourPassword"); config.setString(HologresConfigs.DATABASE, "yourDatabaseName"); config.setString(HologresConfigs.TABLE, "yourTableName"); config.setString(HologresConfigs.SDK_MODE, "jdbc"); HologresConnectionParam hologresConnectionParam = new HologresConnectionParam(config);
```

`//` 构建`Hologres Writer`，以`RowData`的方式写入数据。

```
AbstractHologresWriter<RowData> hologresWriter = HologresJDBCWriter.createRowDataWriter(
  hologresConnectionParam, schema, HologresTableSchema.get(hologresConnectionParam),
new Integer[0]);
```

`//` 构建`Hologres Sink`。

```
HologresSinkFunction sinkFunction = new HologresSinkFunction(hologresConnectionParam, h ologresWriter); TypeInformation<RowData> typeInfo = InternalTypeInfo.of(schema.toRowDataType().getLogicalType()); int offset = (int) (System.currentTimeMillis() % Integer.MAX_VALUE); env.fromElements((RowData)GenericRowData.of(2 + offset, StringData.fromString("2")), GenericRowData.of(3 + offset, StringData.fromString("3"))).returns(typeInfo)
  .addSink(sinkFunction);
env.execute();
```

**说明**

方法buildHologresWriter不在VVR Connector依赖中，是示例代码中提供的方法。

**Flink与Hologres时区说明**

**时间类型**

| 产品 | 类型 | 说明 |
|---|---|---|

实时计算（流计算）

| Flink | Flink TIMESTA MP | 表示没有时区信息的日期和时间，描述年、 月、日、小时、分钟、秒和小数秒对应的时间戳。可以通过一个字符串来指定，例如 1970-01-01 00:00:04.001 。 |
|---|---|---|
|  | Flink TIMESTA MP LTZ _ | 用于描述时间线上的绝对时间点，使用long保存从epoch至今的毫秒数，使用int保存毫秒中的纳秒数。epoch时间是从Java的标准epoch时间开始计算。在计算和可视化时， 每个TIMESTAMP LTZ类型的数据都使用Session （会话）中配置的时 _ 区。可以用于跨时区的计算，因为它是一个基于epoch的绝对时间点（比如上例中的毫秒）代表的就是不同时区的同一个绝对时间点。 相同的TIMESTAMP LTZ值，在不同的时区可能会反映出不同的本地 _ TIMESTAMP，例如：如果一个TIMESTAMP LTZ值为 2024-03- _ 19T04:00:00Z ，在上海时区（UTC+8）的本地时间戳会表示为 2024-03- 19T12:00:00 ，而在格林威治时区（UTC+0）则表示为 2024-03- 19T04:00:00 。 |
| Hologre s | TIMESTAMP | 类似于Flink的 TIMESTAMP 类型，表示没有时区信息的日期和时间。存储数据时不会改变，即使客户端的时区发生变化，存储的值也保持不变。例如： 2022- 01-01 01:01:01.123456 。 |
|  | TIMESTAMP WITH TIME ZONE (TIMESTAMPTZ ) | 类似于Flink的 TIMESTAMP LTZ 类型，它带有时区信息。Hologres存 _ 储 TIMESTAMPTZ 数据时，会将其转换为UTC时区的值。当查询数据时，Hologres会根据客户端的时区配置参数将UTC时区的值转换为客户端时区的值。 例如北京（UTC+8）时区的时间戳 2022-02-01 10:33:20.125+08 。在 Hologres中存储为TIMESTAMPTZ类型时，其值会是 2022-02-01 10:33:20.125+08 。 |

| 2024-03- |  |  |  |
|---|---|---|---|
|  |  | 2024-03- |  |
|  | 2024-03- |  |  |

|  | 19T04:00:00Z |
|---|---|
|  | 19T12:00:00 |
|  | 19T04:00:00 |

|  | 01-01 01:01:01.123456 |
|---|---|

|  | TIMESTAMP LTZ _ |
|---|---|
| TIMESTAMPTZ |  |

| 2022-02-01 |  |
|---|---|

|  | 10:33:20.125+08 |
|---|---|

**Flink读写Hologres时间**

实时计算引擎VVR 8.0.6及以上版本且 `type-mapping.timestamp-converting.legacy=false` 时，支

| Flink | Hologres | 详情 |
|---|---|---|
| TIMESTAMP | TIMESTAMP | 之间相互转换是直接的，不涉及时区转换。因此推荐采用该数据映射。 |
| TIMESTAMP L TZ | TIMESTAMP TZ |  |
| TIMESTAMP | TIMESTAMP TZ | 之间的转换涉及时区转换。为了在转换中保持准确性，需要通过配置项参数 table.local-time-zone 设置Flink时区。 例如当设置 'table.local-time-zone': 'Asia/Shanghai' 时， 表示Flink时区为上海（+8时区）时，Flink TIMESTAMP类型的数据为 2022-01-01 01:01:01.123456，写入Hologres TIMESTAMP TZ的数值为2022-01-01 01:01:01.123456+8。 |
| TIMESTAMP L TZ | TIMESTAMP |  |

实时计算引擎VVR 8.0.5及以下版本或VVR 8.0.6及以上版本设置 `type-mapping.timestamp-` `converting.legacy=false` 时，除TIMESTAMP间转化，其他类型相互转化可能会出现数据偏差问题。 实时计算（流计算）

| Flink | Hologres | 备注 |
|---|---|---|
| TIMESTAMP | TIMESTAMP | 之间相互转换是直接的，不涉及时区转换。因此推荐采用该数据映射。 |
| TIMESTAMP L TZ | TIMESTAMP TZ | 读写Hologres数据时都当作无时区时间进行处理，可能会存在数据偏差。 例如，Flink TIMESTAMP LTZ类型的数值为2024-03- _ 19T04:00:00Z，在上海（+8时区）对应的实际无时区时间为2024-03- 19T12:00:00，但是写入时将2024-03-19T04:00:00当作无时区时间，写入Hologres TIMESTAMP TZ的数值为2024-03- 19T04:00:00+08，数值偏差8小时。 |
| TIMESTAMP | TIMESTAMP TZ | 时区转换默认采用的是运行环境的JVM时区，而不是Flink时区，这与 Flink内部计算的时区转换格式不同。当Flink时区与机器的JVM时区不一致时，会导致数据存在偏差，建议采用Flink时区进行Hologres数据的读写。 |
| TIMESTAMP L TZ | TIMESTAMP |  |

### MySQL

**背景信息**

MySQL连接器支持所有兼容MySQL协议的数据库，包括RDS MySQL、PolarDB for MySQL或者自建

| 类别 | 详情 |
|---|---|
| 支持类型 | 源表、维表和结果表 |
| 运行模式 | 仅支持流模式 |
| 数据格式 | 暂不适用 |
| 特有监控指标 | 源表 currentFetchEventTimeLag：数据产生到拉取到Source Operator的间隔。 该指标仅在Binlog阶段有效，Snapshot阶段该值恒为0。 currentEmitEventTimeLag：数据产生到离开Source Operator的间隔。 该指标仅在Binlog阶段有效，Snapshot阶段该值恒为0。 sourceIdleTime：源表至今有多久不产生新数据。 维表和结果表：无。 |

实时计算（流计算）

| API种类 | Datastream和SQL |
|---|---|
| 是否支持更新或删除结果表数据 | 是 |

**特色功能**

MySQL的CDC源表，即MySQL的流式源表，会先读取数据库的历史全量数据，并平滑切换到Binlog读取上，保证不多读一条也不少读一条数据。即使发生故障，也能保证通过Exactly Once语义处理数据。 MySQL CDC源表支持并发地读取全量数据，通过增量快照算法实现了全程无锁和断点续传。 作为源表，支持以下功能特性。 流批一体，支持读取全量和增量数据，无需维护两套流程。 支持并发读取全量数据，性能水平扩展。 全量读取无缝切换增量读取，自动缩容，节省计算资源。 全量阶段读取支持断点续传，更稳定。 无锁读取全量数据，不影响在线业务。 并行解析Binlog文件，读取延迟更低。

**前提条件**

CDC源表在使用MySQL CDC源表前，必须先按照配置MySQL进行操作，这些操作主要为了满足使用MySQL CDC 源表的前提条件： 已开启了Binlog。 Binlog格式已设置为ROW。 binlog_row_image已设置为FULL。 已创建MySQL用户，并授予了SELECT、SHOW DATABASES、REPLICATION SLAVE和 REPLICATION CLIENT权限。 维表和结果表已设置IP白名单。

**使用限制**

CDC源表实时计算（流计算）

| VVR版本 | 支持的MySQL版本 |
|---|---|
| VVR 4.0.11及以上版本 | 5.6.x |
|  | 5.7.x |
|  | 8.0.x |

**重要**

scan.incremental.snapshot.enabled=true），且不支持关闭增量快照功能，而RDS MySQL 6.0.8和8.0.1版本的数据库已解除该限制，即支持关闭增量快照功能。建议您不要关闭增量快照功能，因为关闭增量快照功能会锁定MySQL数据库，可能会对线上业务处理性能产生影响。 MySQL的CDC源表需要一个有特定权限（包括SELECT、SHOW DATABASES、REPLICATION SLAVE和REPLICATION CLIENT）的MySQL用户，才能读取全量和增量数据。 当结合CTAS和CDAS整库同步语法使用时，MySQL CDC源表可以同步部分Schema变更。在其他使用对于RDS MySQL，不建议通过备库或只读从库读取数据。因为RDS MySQL的备库和只读从库Binlog 保留时间默认很短，可能由于Binlog过期清理，导致作业无法消费Binlog数据而报错。 MySQL CDC源表不支持读取PolarDB MySQL版1.0.19及以前版本的多主架构集群。PolarDB MySQL版1.0.19及以前版本的多主架构集群产生的Binlog可能出现重复Table id，导致CDC源表 Schema映射错误，从而解析Binlog数据报错。PolarDB MySQL版在高于1.0.19的版本进行适配，保证Binlog内Table id不会出现重复，从而避免解析报错。 维表和结果表语义上可以保证At-Least-Once，在结果表有主键的情况下，幂等可以保证数据的正确性。

**注意事项**

CDC源表实时计算（流计算） Server ID作用每个同步数据库数据的客户端，都会有一个唯一ID，即Server ID。MySQL SERVER会根据该ID来维护网络连接以及Binlog位点。因此如果有大量不同的Server ID的客户端一起连接MySQL 此外，如果多个MySQL CDC数据源共享相同的Server ID，且数据源之间无法复用时，会导致 Binlog位点错乱，多读或少读数据。还可能出现Server ID冲突的报错。因此建议每个MySQL CDC 数据源都配置不同的Server ID。 Server ID配置方式 Server ID可以在DDL中指定，也可以通过动态Hints配置。 建议通过动态Hints来配置Server ID，而不是在DDL参数中配置Server ID。 不同场景下Server ID的配置未开启增量快照框架或并行度为1 当未开启增量快照框架或并行度为1时，可以指定一个特定的Server ID。

```
SELECT * FROM source_table /*+ OPTIONS('server-id'='123456') */ ;
```

开启增量快照框架且并行度大于1 当开启增量快照框架且并行度大于1时，需要指定Server ID范围，要保证范围内可用的Server ID 数量不小于并行度。假设并行度为3，可以如下配置：

```
SELECT * FROM source_table /*+ OPTIONS('server-id'='123456-123458') */ ;
```

结合CTAS进行数据同步当结合CTAS进行数据同步时，如果CDC数据源配置相同，会自动对数据源进行复用，此时可以为多个CDC数据源配置相同的Server ID。 当作业中包含多个MySQL CDC源表，且不是使用CTAS语句同步时，数据源无法进行复用，需要为每一个CDC源表提供不同的Server ID。同理，如果开启增量快照框架且并行度大于1，需要指定Server ID范围。

```
select * from
  source_table1 /*+ OPTIONS('server-id'='123456-123457') */
left join
  source_table2 /*+ OPTIONS('server-id'='123458-123459') */
on source_table1.id=source_table2.id;
```

仅VVR 4.0.8及以上版本支持全量阶段的无锁读取、并发读取、断点续传等功能。 如果您使用的是VVR 4.0.8以下版本，需要对MySQL用户授予RELOAD权限用来获取全局读锁，保证数据读取的一致性。全局读锁会阻塞写入操作，持锁时间可能达到秒级，因此可能对线上业务造成影响。 此外，VVR 4.0.8以下版本在全量读取阶段无法执行Checkpoint，全量阶段的作业失败会导致作业重新读取全量数据，稳定性不佳。因此建议您将作业升级到VVR 4.0.8及以上版本。 结果表 RDS MySQL数据库支持自增主键，因此在结果表的DDL中不声明该自增字段。例如ID是自增字段，Flink DDL不声明该自增字段，则数据库在一行数据写入过程中会自动填补相关自增字段。 结果表的DDL声明的字段必须至少存在一个非主键的字段，否则会产生报错。 实时计算（流计算） 结果表的DDL中NOT ENFORCED表示Flink自身对主键不做强制校验，需要您自行保证主键的正确性和完整性。 Flink并不充分支持强制校验，Flink将假设列的可为空性与主键中的列是对齐的，从而认为主键是正确的。 维表如果做维表时希望使用索引查询，请按照MySQL最左前缀原则排列JOIN指定的数据列。但这并无法保证使用索引，由于SQL优化，某些条件可能会被优化导致连接器得到的过滤条件无法命中索引。要确定连接器是否真正使用了索引进行查询，可以在数据库侧查看具体执行的Select语句。

**语法结构**

```
   order_id INT,
   order_date TIMESTAMP(0),
   customer_name STRING,
   price DECIMAL(10, 5),
   product_id INT,
   order_status BOOLEAN,
   PRIMARY KEY(order_id) NOT ENFORCED
) WITH (
  'connector' = 'mysql',
  'hostname' = '<yourHostname>',
  'port' = '3306',
  'username' = '<yourUsername>',
  'password' = '<yourPassword>',
  'database-name' = '<yourDatabaseName>',
  'table-name' = '<yourTableName>'
);
```

| 说明连接器写入结果表原理：写入结果表时，会将接收到的每条数据拼接成一条SQL去执行。具体执行的SQL情况如下： 对于没有主键的结果表，会拼接执行 INSERT INTO table name (column1, column2, _ |  |
|---|---|
|  | INSERT INTO table name (column1, column2, _ |
| ...) VALUES (value1, value2, ...)； 语句。 |  |
| 对于包含主键的结果表，会拼接执行 INSERT INTO table name (column1, column2, _ |  |
| ...) VALUES (value1, value2, ...) ON DUPLICATE KEY UPDATE column1 = |  |
| VALUES(column1), column2 = VALUES(column2), ...; |  |

因为唯一索引冲突导致数据覆盖引发数据丢失。 如果在MySQL数据库定义了自增主键，在Flink DDL中不应该声明该自增字段。数据写入过程中，数据库会自动填补该自增字段。连接器仅支持写入和删除带自增字段的数据，不支持更新。

**WITH参数**

通用

| 参数 | 说明 | 是否必填 | 数据类型 | 默认值 | 备注 |
|---|---|---|---|---|---|

实时计算（流计算）

| connect or | 表类型。 | 是 | STRING | 无 | 作为源表时，可以填写为 mysql-cdc 或者 mysql ，二者等价。作为维表或结果表时，固定值为 mysql 。 |
|---|---|---|---|---|---|
| hostnam e | MySQL数据库的IP地址或者 Hostname。 | 是 | STRING | 无 | 请联系阿里云运维工程师获取。 |
| usernam e | MySQL数据库服务的用户名。 | 是 | STRING | 无 | 无。 |
| passwor d | MySQL数据库服务的密码。 | 是 | STRING | 无 | 无。 |
| databas e-name | MySQL数据库名称。 | 是 | STRING | 无 | 作为源表时，数据库名称支持正则表达式以读取多个数据库的数据。 使用正则表达式时，尽量不要使用^和$符号匹配开头和结尾。具体原因详见table- name备注的说明。 |
| table- name | MySQL表名。 | 是 | STRING | 无 | 作为源表时，表名支持正则表达式以读取多个表的数据。 在读取多个MySQL表时，将多个CTAS语句作为一个作业提交，可以避免启用多个 Binlog监听，提高性能和效率。 使用正则表达式时，尽量不要使用^和$符号匹配开头和结尾。具体原因详见以下说明。 说明 MySQL CDC源表在正则匹配表名时，会将您填写的 database-name，table- name 通过字符串 \\.（VVR 8.0.1前使用字符.）连接成为一个全路径的正则表达式，然后使用该正则表达式和MySQL数据库中表的全限定名进行正则匹配。 例如：当配置'database- name'='db .*'且'table- _ name'='tb .+'时，连接器将会使用正则 _ 表达式db .*\\.tb .+（8.0.1版本前 _ _ 为db .*.tb .+）去匹配表的全限定名来 _ _ 确定需要读取的表。 |
| port | MySQL数据库服务的端口号。 | 否 | INTEGE R | 3306 | 无。 |

源表独有实时计算（流计算）

| 参数 | 说明 | 是否必填 | 数据类型 | 默认值 | 备注 |
|---|---|---|---|---|---|
| server-id | 数据库客户端的一个数字 ID。 | 否 | STRING | 默认会随机生成一个 5400 ~64 00的值。 | 该ID必须是MySQL集群中全局唯一的。建议针对同一个数据库的每个作业都设置一个不同的 ID。 该参数也支持ID范围的格式，例如5400- 5408。在开启增量读取模式时支持多并发读取，此时推荐设定为ID范围，使得每个并发使用不同的ID。 |
| scan.incr emental. snapshot .enabled | 是否开启增量快照。 | 否 | BOOLEA N | true | 默认开启增量快照。增量快照是一种读取全量数据快照的新机制。与旧的快照读取相比，增量快照有很多优点，包括： 读取全量数据时，Source可以是并行读取。 读取全量数据时，Source支持chunk粒度的检查点。 读取全量数据时，Source不需要获取全局读锁（FLUSH TABLES WITH read lock）。 如果您希望Source支持并发读取，每个并发的 Reader需要有一个唯一的服务器ID，因此 server-id必须是5400-6400这样的范围，并且范围必须大于等于并发数。 |
| scan.incr emental. snapshot .chunk.si ze | 每个chunk的大小（包含的行数）。 | 否 | INTEGER | 8096 | 当开启增量快照读取时，表会被切分成多个 chunk读取。在读完chunk的数据之前，chunk的数据会先缓存在内存中。 每个chunk包含的行数越少，则表中的chunk 的总数量越大，尽管这会降低故障恢复的粒度，但可能导致内存OOM和整体的吞吐量降低。因此，您需要进行权衡，并设置合理的 chunk大小。 |
| scan.sna pshot.fet ch.size | 当读取表的全量数据时，每次最多拉取的记录数。 | 否 | INTEGER | 1024 | 无。 |

实时计算（流计算）

| scan.star tup.mod e | 消费数据时的启动模式。 | 否 | STRING | initia l | 参数取值如下： initial（默认）：在第一次启动时，会先扫描历史全量数据，然后读取最新的Binlog数据。 latest-offset：在第一次启动时，不会扫描历史全量数据，直接从Binlog的末尾（最新的Binlog处）开始读取，即只读取该连接器启动以后的最新变更。 earliest-offset：不扫描历史全量数据， 直接从可读取的最早Binlog开始读取。 specific-offset：不扫描历史全量数据， 从您指定的Binlog位点启动，位点可通过同时配置scan.startup.specific- offset.file和scan.startup.specific- offset.pos参数来指定从特定Binlog文件名和偏移量启动，也可以只配置scan.startup.specific-offset.gtid- set来指定从某个GTID集合启动。 timestamp：不扫描历史全量数据，从指定的时间戳开始读取Binlog。时间戳通过scan.startup.timestamp-millis指定，单位为毫秒。 重要 earliest-offset，specific- offset和timestamp启动模式在Flink计算引擎VVR 6.0.4及以上的版本支持使用。 对于earliest- offset，specific- offset和timestamp启动模式，如果启动时刻和指定的启动位点时刻的表结构不同，作业会因为表结构不同而报错。换一句话说，使用这三种启动模式，需要保证在指定的Binlog消费位置到作业启动的时间之间，对应表不能发生表结构变更。 |
|---|---|---|---|---|---|
| scan.star tup.speci fic- offset.fil e | 使用指定位点模式启动时， 启动位点的 Binlog文件名。 | 否 | STRING | 无 | 使用该配置时，scan.startup.mode必须配置为specific-offset。文件名格式例如 mysql-bin.000003 。 |
| scan.star tup.speci fic- offset.po s | 使用指定位点模式启动时， 启动位点在指定Binlog文件中的偏移量。 | 否 | INTEGER | 无 | 使用该配置时，scan.startup.mode必须配置为specific-offset。 |

实时计算（流计算）

| scan.star tup.speci fic- offset.gti d-set | 使用指定位点模式启动时， 启动位点的 GTID集合。 | 否 |  |  |  | 使用该配置时，scan.startup.mode必须配置为specific-offset。GTID集合格式例如 24DA167-0C0C-11E8-8442- 00059A3C7B00:1-19 。 |  |  |
|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  | 24DA167-0C0C-11E8-8442- |  |
|  |  |  |  | STRING | 无 | 00059A3C7B00:1-19 |  |  |
| scan.star tup.time stamp- millis | 使用指定时间模式启动时， 启动位点的毫秒时间戳。 | 否 |  | LONG | 无 | 使用该配置时，scan.startup.mode必须配置为timestamp。时间戳单位为毫秒。 重要在使用指定时间时，MySQL CDC会尝试读取每个Binlog文件的初始事件以确定其时间戳，最终定位至指定时间对应的 Binlog文件。请保证指定的时间戳对应的 Binlog文件在数据库上没有被清理且可以被读取到。 |  |  |
| server- time- zone | 数据库在使用的会话时区。 | VVR- 6.0.2 以下版本必填， 其他版本选填 |  | STRING | 如果您没有指定该参数， 则系统默认使用 Flink 作业运行时的环境时区作为数据库服务器时区， 即您选择的可用区所在的时区。 | 例如Asia/Shanghai，该参数控制了MySQL中的TIMESTAMP类型如何转成STRING类型。 |  |  |

实时计算（流计算）

| debeziu m.min.ro w.count.t o.stream .results | 当表的条数大于该值时，会使用分批读取模式。 | 否 | INTEGER | 1000 | Flink采用以下方式读取MySQL源表数据： 全量读取：直接将整个表的数据读取到内存里。优点是速度快，缺点是会消耗对应大小的内存，如果源表数据量非常大，可能会有 OOM风险。 分批读取：分多次读取，每次读取一定数量的行数，直到读取完所有数据。优点是读取数据量比较大的表没有OOM风险，缺点是读取速度相对较慢。 |
|---|---|---|---|---|---|
| connect. timeout | 连接MySQL 数据库服务器超时时，重试连接之前等待超时的最长时间。 | 否 | DURATI ON | 30s | 无。 |
| connect. max- retries | 连接MySQL 数据库服务时，连接失败后重试的最大次数。 | 否 | INTEGER | 3 | 无。 |
| connecti on.pool.s ize | 数据库连接池大小。 | 否 | INTEGER | 20 | 数据库连接池用于复用连接，可以降低数据库连接数量。 |
| jdbc.pro perties.* | JDBC URL中的自定义连接参数。 | 否 | STRING | 无 | 您可以传递自定义的连接参数，例如不使用SSL 协议，则可配置为'jdbc.properties.useSSL' = 'false'。 |
| debeziu m.* | Debezium读取Binlog的自定义参数。 | 否 | STRING | 无 | 您可以传递自定义的Debezium参数，例如使用'debezium.event.deserialization.failure. handling.mode'='ignore'来指定解析错误时的处理逻辑。 |
| heartbea t.interval | Source通过心跳事件推动 Binlog位点前进的时间间隔。 | 否 | DURATI ON | 30s | 心跳事件用于推动Source中的Binlog位点前进，这对MySQL中更新缓慢的表非常有用。对于更新缓慢的表，Binlog位点无法自动前进， 通过够心跳事件可以推到Binlog位点前进，可以避免Binlog位点不前进引起Binlog位点过期问题，Binlog位点过期会导致作业失败无法恢复，只能无状态重启。 |

实时计算（流计算）

| scan.incr emental. snapshot .chunk.k ey- column | 可以指定某一列作为快照阶段切分分片的切分列。 | 见备注列。 | STRING | 无 | 无主键表必填，选择的列必须是非空类型 （NOT NULL）。 有主键的表为选填，仅支持从主键中选择一列。 说明仅Flink计算引擎VVR 6.0.7及以上版本支持。 |
|---|---|---|---|---|---|
| rds.regio n-id | 阿里云 RDS MySQL 实例所在的地域ID。 | 使用读取 OSS 归档日志功能时必填。 | STRING | 无 | 仅Flink计算引擎VVR 6.0.7及以上版本支持。 |
| rds.acce ss-key-id | 阿里云 RDS MySQL 账号Access Key ID。 | 使用读取 OSS 归档日志功能时必填。 | STRING | 无 | 仅Flink计算引擎VVR 6.0.7及以上版本支持。 |
| rds.acce ss-key- secret | 阿里云 RDS MySQL 账号Access Key Secret。 | 使用读取 OSS 归档日志功能时必填。 | STRING | 无 | 仅Flink计算引擎VVR 6.0.7及以上版本支持。 |
| rds.db- instance- id | 阿里云 RDS MySQL 实例ID。 | 使用读取 OSS 归档日志功能时必填。 | STRING | 无 | 仅Flink计算引擎VVR 6.0.7及以上版本支持。 |
| rds.main -db-id | 阿里云 RDS MySQL 实例主库编号。 | 否 | STRING | 无 | 仅Flink计算引擎VVR 8.0.7及以上版本支持。 |

实时计算（流计算）

| rds.down load.tim eout | 从OSS下载单个归档日志的超时时间。 | 否 | DURATI ON | 60s | 仅Flink计算引擎VVR 6.0.7及以上版本支持。 |
|---|---|---|---|---|---|
| scan.incr emental. close- idle- reader.e nabled | 是否在快照结束后关闭空闲的 Reader。 | 否 | BOOLEA N | false | 仅Flink计算引擎VVR 8.0.1及以上版本支持。 该配置生效需要设置 execution.checkpointing.checkpoints- after-tasks-finish.enabled为true。 |
| scan.rea d- changelo g-as- append- only.ena bled | 是否将 changelog 数据流转换为 append- only数据流。 | 否 | BOOLEA N | false | 参数取值如下： true：所有类型的消息（包括INSERT、 DELETE、UPDATE BEFORE、 _ UPDATE AFTER）都会转换成INSERT类型 _ 的消息。仅在需要保存上游表删除消息等特殊场景下开启使用。 false（默认）：所有类型的消息都保持原样下发。 说明仅Flink计算引擎VVR 8.0.7及以上版本支持。 |
| scan.onl y.deseria lize.capt ured.tabl es.chang elog.ena bled | 在增量阶段, 是否仅对指定的表事件进行反序列化。 | 否 | BOOLEA N | false | 参数取值如下： true：仅对目标表的数据进行反序列化，减少反序列化操作，加快Binlog读取速度。 false（默认）：对所有表的数据进行反序列化。 说明仅Flink计算引擎VVR 8.0.7及以上版本支持。 |
| scan.par allel- deseriali ze- changelo g.enable d | 在增量阶段, 是否使用多线程对变更事件进行解析。 | 否 | BOOLEA N | false | 参数取值如下： true：在变更事件的反序列化阶段采用多线程处理，同时保证Binlog事件顺序不变，从而加快读取速度。 false（默认）：在事件的反序列化阶段使用单线程处理。 说明仅Flink计算引擎VVR 8.0.7及以上版本支持。 |

维表独有实时计算（流计算）

| 参数 | 说明 | 是否必填 | 数据类型 | 默认值 | 备注 |
|---|---|---|---|---|---|
| url | MySQL JDBC URL | 否 | STRING | 无 | 仅Flink计算引擎VVR 6.0.7及以上版本支持。 |
| lookup. max- retries | 读取数据失败后，重试读取的最大次数。 | 否 | INTEGE R | 3 | 仅Flink计算引擎VVR 6.0.7及以上版本支持。 |
| lookup.c ache.str ategy | 缓存策略。 | 否 | STRING | None | 支持None、LRU和ALL三种缓存策略。 说明使用LRU缓存策略时，还必须配置lookup.cache.max-rows参数。 |
| lookup.c ache.ma x-rows | 最大缓存条数。 | 否 | INTEGE R | 10000 0 | 当选择LRU缓存策略后，必须设置缓存大小。 当选择ALL缓存策略后，可以不设置缓存大小。 |
| lookup.c ache.ttl | 缓存超时时间。 | 否 | DURATI ON | 10 s | lookup.cache.ttl的配置和 lookup.cache.strategy有关，详情如下： 如果lookup.cache.strategy配置为 None，则lookup.cache.ttl可以不配置， 表示缓存不超时。 如果lookup.cache.strategy配置为LRU， 则lookup.cache.ttl为缓存超时时间。默认不过期。 如果lookup.cache.strategy配置为ALL， 则lookup.cache.ttl为缓存加载时间。默认不重新加载。 填写时请使用时间格式，例如1min或10s。 |
| lookup. max- join- rows | 主表中每一条数据查询维表时，匹配后最多返回的结果数。 | 否 | INTEGE R | 1024 | 在Flink计算引擎VVR 6.0.7及以上版本支持。 |

结果表独有

| 参数 | 说明 | 是否必填 | 数据类型 | 默认值 | 备注 |
|---|---|---|---|---|---|
| url | MySQL JDBC URL | 否 | STRING | 无 | 请联系阿里云运维工程师获取。 |

实时计算（流计算）

| sink.ma x-retries | 写入数据失败后，重试写入的最大次数。 | 否 | INTEGER | 3 | 无。 |
|---|---|---|---|---|---|
| sink.buff er- flush.ba tch-size | 一次批量写入的条数。 | 否 | INTEGER | 4096 | 在Flink计算引擎VVR 6.0.7及以上版本支持。 |
| sink.buff er- flush.ma x-rows | 内存中缓存的数据条数。 | 否 | INTEGER | 在Flink 计算引擎 VVR 6.0.7版本以下， 该参数默认值为 100。 在Flink 计算引擎 VVR 6.0.7版本及以上版本，该参数默认值为 10000。 | 需指定主键后，该参数才生效。 |
| sink.buff er- flush.int erval | 清空缓存的时间间隔。表示如果缓存中的数据在等待指定时间后，依然没有达到输出条件，系统会自动输出缓存中的所有数据。 | 否 | DURATI ON | 1s | 无。 |
| sink.ign ore- delete | 是否忽略数据 Delete操作。 | 否 | BOOLEA N | false | 在Flink计算引擎VVR 6.0.7及以上版本支持。 Flink SQL可能会生成数据Delete操作，在多个输出节点根据主键同时更新同一张结果表的不同字段的场景下，可能导致数据结果不正确。 例如一个任务在删除了一条数据后， 另一个任务又只更新了这条数据的部分字段，其余未被更新的字段由于被删除，其值会变成null或默认值。通过将ignoreDelete设置为true，可以避免数据删除操作。 |

实时计算（流计算）

| sink.ign ore-null- when- update | 更新数据时， 如果传入的数据字段值为 null，是更新对应字段为 null，还是跳过该字段的更新。 | 否 | BOOLEA N | false | 参数取值如下： true：不更新该字段。但是当Flink 表设置主键时，才支持配置该参数为 true。配置为true时： 如果是8.0.6及以下的版本，结果表写入数据不支持攒批执行。 如果是8.0.7及以上的版本，结果表写入数据支持攒批执行。 攒批写入虽然可以明显增强写入效率和整体吞吐量，但是会带来数据延迟问题和内存溢出风险。因此请您根据实际业务场景做好权衡。 false：更新该字段为null。 说明仅实时计算引擎VVR 8.0.5及以上版本支持该参数。 |
|---|---|---|---|---|---|

**类型映射**

CDC源表

| MySQL CDC字段类型 | Flink字段类型 |
|---|---|
| TINYINT | TINYINT |
| SMALLINT | SMALLINT |
| TINYINT UNSIGNED |  |
| TINYINT UNSIGNED ZEROFILL |  |
| INT | INT |
| MEDIUMINT |  |
| SMALLINT UNSIGNED |  |
| SMALLINT UNSIGNED ZEROFILL |  |
| BIGINT |  |
| INT UNSIGNED |  |

| k存算分离版开发指南·连接器 | 实时计算（流计算） |
|---|---|
|  | BIGINT |
| INT UNSIGNED ZEROFILL |  |
| MEDIUMINT UNSIGNED |  |
| MEDIUMINT UNSIGNED ZEROFILL |  |
| BIGINT UNSIGNED | DECIMAL(20, 0) |
| BIGINT UNSIGNED ZEROFILL |  |
| SERIAL |  |
| FLOAT [UNSIGNED] [ZEROFILL] | FLOAT |
| DOUBLE [UNSIGNED] [ZEROFILL] | DOUBLE |
| DOUBLE PRECISION [UNSIGNED] [ZEROFILL] |  |
| REAL [UNSIGNED] [ZEROFILL] |  |
| NUMERIC(p, s) [UNSIGNED] [ZEROFILL] | DECIMAL(p, s) |
| DECIMAL(p, s) [UNSIGNED] [ZEROFILL] |  |
| BOOLEAN | BOOLEAN |
| TINYINT(1) |  |
| DATE | DATE |
| TIME [(p)] | TIME [(p)] [WITHOUT TIME ZONE] |
| DATETIME [(p)] | TIMESTAMP [(p)] [WITHOUT TIME ZONE] |
| TIMESTAMP [(p)] | TIMESTAMP [(p)] |
|  | TIMESTAMP [(p)] WITH LOCAL TIME ZONE |

实时计算（流计算）

| CHAR(n) | STRING |
|---|---|
| VARCHAR(n) |  |
| TEXT |  |
| BINARY | BYTES |
| VARBINARY |  |
| BLOB |  |

**重要**

建议MySQL不要使用TINYINT(1)类型存储0和1以外的数值，MySQL使用TINYINT(1)存储 BOOLEAN类型数据，MySQL CDC源表会将TINYINT(1)映射到Flink的BOOLEAN上。如果存储0和 1以外的数值，会导致数据不准确。 维表和结果表

| MySQL字段类型 | Flink字段类型 |
|---|---|
| TINYINT | TINYINT |
| SMALLINT | SMALLINT |
| TINYINT UNSIGNED |  |
| INT | INT |
| MEDIUMINT |  |
| SMALLINT UNSIGNED |  |
| BIGINT | BIGINT |
| INT UNSIGNED |  |
| BIGINT UNSIGNED | DECIMAL(20, 0) |

实时计算（流计算）

| FLOAT | FLOAT |
|---|---|
| DOUBLE | DOUBLE |
| DOUBLE PRECISION |  |
| NUMERIC(p, s) | DECIMAL(p, s) 说明其中p <= 38。 |
| DECIMAL(p, s) |  |
| BOOLEAN | BOOLEAN |
| TINYINT(1) |  |
| DATE | DATE |
| TIME [(p)] | TIME [(p)] [WITHOUT TIME ZONE] |
| DATETIME [(p)] | TIMESTAMP [(p)] [WITHOUT TIME ZONE] |
| TIMESTAMP [(p)] |  |
| CHAR(n) | CHAR(n) |
| VARCHAR(n) | VARCHAR(n) |
| BIT(n) | BINARY(⌈n/8⌉) |
| BINARY(n) | BINARY(n) |
| VARBINARY(N) | VARBINARY(N) |
| TINYTEXT | STRING |
| TEXT |  |
| MEDIUMTEXT |  |
| 5 | > 文档版本：2026073 |

|  | Flink存算分离版开发指南·连接器 |
|---|---|
| LONGTEXT |  |
| TINYBLOB | BYTES 重要 Flink仅支持小于等于2,147,483,647(2^31 - 1)的 MySQL BLOB类型的记录。 |
| BLOB |  |
| MEDIUMBLOB |  |
| LONGBLOB |  |

**使用示例**

CDC源表

```
   order_id INT,
   order_date TIMESTAMP(0),
   customer_name STRING,
   price DECIMAL(10, 5),
   product_id INT,
   order_status BOOLEAN,
   PRIMARY KEY(order_id) NOT ENFORCED
) WITH (
  'connector' = 'mysql',
  'hostname' = '<yourHostname>',
  'port' = '3306',
  'username' = '<yourUsername>',
  'password' = '<yourPassword>',
  'database-name' = '<yourDatabaseName>',
  'table-name' = '<yourTableName>'
);
  order_id INT,
  customer_name STRING
) WITH ( ); SELECT order_id, customer_name FROM mysqlcdc_source;
```

维表实时计算（流计算）

```
  a INT,
  b BIGINT,
  c STRING,
  `proctime` AS PROCTIME()
) WITH ( );
  a INT,
  b VARCHAR,
  c VARCHAR
) WITH (
  'connector' = 'mysql',
  'hostname' = '<yourHostname>',
  'port' = '3306',
  'username' = '<yourUsername>',
  'password' = '<yourPassword>',
  'database-name' = '<yourDatabaseName>',
  'table-name' = '<yourTableName>'
);
  a INT,
  b STRING
) WITH ( ); SELECT T.a, H.b FROM datagen_source AS T JOIN mysql_dim FOR SYSTEM_TIME AS OF T.`proctime` AS H ON T. a = H.a;
```

结果表实时计算（流计算）

```
  `name` VARCHAR,
  `age` INT
) WITH ( );
  `name` VARCHAR,
  `age` INT
) WITH (
  'connector' = 'mysql',
  'hostname' = '<yourHostname>',
  'port' = '3306',
  'username' = '<yourUsername>',
  'password' = '<yourPassword>',
  'database-name' = '<yourDatabaseName>',
  'table-name' = '<yourTableName>'
); SELECT * FROM datagen_source;
```

实现原理 MySQL CDC源表在启动时扫描全表，将表按照主键分成多个分片（chunk），记录下此时的Binlog位点。并使用增量快照算法通过select语句，逐个读取每个分片的数据。作业会周期性执行Checkpoint， 记录下已经完成的分片。当发生Failover时，只需要继续读取未完成的分片。当分片全部读取完后，会从之前获取的Binlog位点读取增量的变更记录。Flink作业会继续周期性执行Checkpoint，记录下Binlog位点，当作业发生Failover，便会从之前记录的Binlog位点继续处理，从而实现Exactly Once语义。 元数据元数据在分库分表合并同步场景非常实用，因为分库分表合并后，一般业务还是希望区分每条数据的库名和表名来源，而元数据列可以访问源表的库名和表名信息。因此通过元数据列可以非常方便地将多张分表合并到一张目的表。 自vvr-4.0.11-flink-1.13版本开始，MySQL CDC Source支持元数据列语法，您可以通过元数据列访问以下元数据。

| 元数据key | 元数据类型 | 描述 |
|---|---|---|
| database nam _ e | STRING NOT NULL | 包含该行记录的库名。 |
| table name _ | STRING NOT NULL | 包含该行记录的表名。 |
| op ts _ | TIMESTAMP LTZ(3) _ NOT NULL | 该行记录在数据库中的变更时间，如果该记录来自表的存量历史数据而不是Binlog中获取，则该值总是0。 |

实时计算（流计算）

| op type _ | STRING NOT NULL | 该行记录的变更类型。 +I：表示INSERT消息 -D：表示DELETE消息 -U：表示UPDATE BEFORE消息 _ +U：表示UPDATE AFTER消息 _ 说明仅实时计算引擎VVR 8.0.7及以上版本支持。 |
|---|---|---|

将MySQL实例中多个分库下的多张orders表，合并同步到下游Hologres的holo_orders表中，代码示例如下所示。

```
  db_name STRING METADATA FROM 'database_name' VIRTUAL,  -- 读取库名。
  table_name STRING METADATA  FROM 'table_name' VIRTUAL, -- 读取表名。
  operation_ts TIMESTAMP_LTZ(3) METADATA FROM 'op_ts' VIRTUAL, -- 读取变更时间。
  op_type STRING METADATA FROM 'op_type' VIRTUAL, -- 读取变更类型。
  order_id INT,
  order_date TIMESTAMP(0),
  customer_name STRING,
  price DECIMAL(10, 5),
  product_id INT,
  order_status BOOLEAN,
  PRIMARY KEY(order_id) NOT ENFORCED
) WITH (
  'connector' = 'mysql-cdc',
  'hostname' = 'localhost',
  'port' = '3306',
  'username' = 'flinkuser',
  'password' = 'flinkpw',
```

`'database-name' = 'mydb_.*', --` 正则匹配多个分库。 `'table-name' = 'orders_.*' --` 正则匹配多张分表。

```
); INSERT INTO holo_orders SELECT * FROM mysql_orders;
```

在上面代码的基础上，WITH参数里配置scan.read-changelog-as-append-only.enabled参数为true 时，输出结果根据下游表主键设置情况有不同的表现： 下游表主键为order_id时，输出结果仅包含上游表每个主键的最后一次变更。即对于某个主键最后一次变更为删除操作的数据，在下游表可以看到一条相同主键的、op_type为-D的数据。 下游表主键为order_id、operation_ts、op_type时，输出结果包含上游表每个主键的完整变更。 支持正则表达式 MySQL CDC源表支持在表名或者库名中使用正则表达式匹配多个表或者多个库。通过正则表达式指定多张表的代码示例如下。 实时计算（流计算）

```
CREATE TABLE products (
  db_name STRING METADATA FROM 'database_name' VIRTUAL,
  table_name STRING METADATA  FROM 'table_name' VIRTUAL,
  operation_ts TIMESTAMP_LTZ(3) METADATA FROM 'op_ts' VIRTUAL,
  order_id INT,
  order_date TIMESTAMP(0),
  customer_name STRING,
  price DECIMAL(10, 5),
  product_id INT,
  order_status BOOLEAN,
  PRIMARY KEY(order_id) NOT ENFORCED
) WITH (
  'connector' = 'mysql-cdc',
  'hostname' = 'localhost',
  'port' = '3306',
  'username' = 'root',
  'password' = '123456',
```

'database-name' = '(^(test).*|^(tpc).*|txc|.*[p$]|t{2})', -- 正则表达式匹配多个库。 'table-name' = '(t[5-8]|tt)' -- 正则表达式匹配多张表。

```
);
```

上述例子中的正则表达式解释： ^(test).* 是前缀匹配示例，这个表达式可以匹配以test开头的库名，例如test1或test2。 .*[p$] 是后缀匹配示例，这个表达式可以匹配以p结尾的库名，例如cdcp或edcp。 txc是指定匹配，可以匹配指定名称的数据库名，例如txc。 MySQL CDC在匹配全路径表名时，会通过库名和表名来唯一确定一张表，即使用databasename.table-name作为匹配表的模式，例如匹配模式 (^(test).*|^(tpc).*|txc|.*[p$]|t{2}).(t[ 5- 8]|tt) 就可以匹配到数据库中的表txc.tt和test2.test5。

|  | 重要 table-name和database-name也支持使用逗号（,）分隔形式指定多张表或多个库，例如 'table-name' = 'mytable1,mytable2' 。但是其与正则表达式中的逗号（,）冲突，所以如果使用了含有逗号的正则表达式，则正则表达式需要改写成竖线（\|）的形式，例如 mytable \d{1, _ 2) 需要改写成等价的正则表达式 (mytable \d{1}\|mytable \d{2}) ，来避免使用逗号。 _ _ |
|---|---|
|  | 2) |

并发控制 MySQL连接器支持多并发读取全量数据，能够提高数据加载效率。同时配合Flink实时计算控制台的 Autopilot自动调优功能，在多并发读取完成后增量阶段，能够自动缩容，节约计算资源。 在Flink全托管控制台，您可以在资源配置页面的基础模式或专家模式中设置作业的并发数。设置并发的区别如下： 实时计算（流计算） 基础模式设置的并发数为整个作业的全局并发数。 专家模式支持按需为某个VERTEX设置并发数。

**重要**

无论是基础模式还是专家模式，在设置并发时，表中声明的server-id范围必须大于等于作业的并发数。例如server-id的范围为5404-5412，则共有8个唯一的server-id，因此作业最多可以设置8个并发，且不同的作业对于同一个MySQL实例的server-id范围不能有重叠，即每个作业需显式配置不同的server-id。 Autopilot自动缩容全量阶段积累了大量历史数据，为了提高读取效率，通常采用并发的方式读取历史数据。而在Binlog增量阶段，因为Binlog数据量少且为了保证全局有序，通常只需要单并发读取。全量阶段和增量阶段对资源的不同需求，可以通过自动调优功能自动帮您实现性能和资源的平衡。 自动调优会监控MySQL CDC Source的每个task的流量。当进入Binlog阶段，如果只有一个task在负责 Binlog读取，其他task均空闲时，自动调优便会自动缩小Source的CU数和并发。开启自动调优只需要在作业运维页面，将自动调优的模式设置为Active模式。 实时计算（流计算）

**说明**

默认调低并发度的最小触发时间间隔为24小时。 启动模式使用配置项scan.startup.mode可以指定MySQL CDC源表的启动模式。可选值包括： initial （默认）：在第一次启动时对数据库表进行全量读取，完成后切换至增量模式读取Binlog。 earliest-offset：跳过快照阶段，从可读取的最早Binlog位点开始读取。 latest-offset：跳过快照阶段，从Binlog的结尾处开始读取。该模式下源表只能读取在作业启动之后的数据变更。 specific-offset：跳过快照阶段，从指定的Binlog位点开始读取。位点可通过Binlog文件名和位置指定，或者使用GTID集合指定。 timestamp：跳过快照阶段，从指定的时间戳开始读取Binlog事件。 使用示例：

```
    'connector' = 'mysql-cdc',
```

`'scan.startup.mode' = 'earliest-offset', --` 从最早位点启动。 `'scan.startup.mode' = 'latest-offset', --` 从最晚位点启动。 `'scan.startup.mode' = 'specific-offset', --` 从特定位点启动。 `'scan.startup.mode' = 'timestamp', --` 从特定位点启动。 `'scan.startup.specific-offset.file' = 'mysql-bin.000003', --` 在特定位点启动模式下指定B `inlog`文件名。 `'scan.startup.specific-offset.pos' = '4', --` 在特定位点启动模式下指定`Binlog`位置。

```
    'scan.startup.specific-offset.gtid-set' = '24DA167-0C0C-11E8-8442-00059A3C7B00:1-
```

`19', --` 在特定位点启动模式下指定`GTID`集合。 `'scan.startup.timestamp-millis' = '1667232000000' --` 在时间戳启动模式下指定启动时间戳。

```
    ...
```

)

**重要**

MySQL source会在Checkpoint时将当前位点以INFO级别打印到日志中，日志前缀为 `Binlog offset on checkpoint {checkpoint-id}` ，该日志可以帮助您将作业从某个 Checkpoint位点开始启动作业。 如果读取的表曾经发生过表结构变化，从最早位点（earliest-offset）、特定位点（specificoffset）或时间戳（timestamp）启动可能会发生错误。因为Debezium读取器会在内部保存当前的最新表结构，结构不匹配的早期数据无法被正确解析。 关于无主键CDC源表在Flink计算引擎VVR 6.0.7及以上版本支持使用MySQL CDC无主键源表，使用无主键表要求必须设置scan.incremental.snapshot.chunk.key-column，且只能选择非空类型的字段。 无主键CDC源表的处理语义由scan.incremental.snapshot.chunk.key-column指定的列的行为决定： 如果指定的列不存在更新操作，此时可以保证Exactly once语义。 如果指定的列发生更新操作，此时只能保证At least once语义。但可以结合下游，通过指定下游主键，结合幂等性操作来保证数据的正确性。 实时计算（流计算） MySQL CDC源表支持读取阿里云RDS MySQL的备份日志。这在全量阶段执行时间较长，本地Binlog文件已经被自动清理，而自动或者手动上传的备份文件依然存在的场景下非常适用。 使用示例：

```
    'connector' = 'mysql-cdc',
    'rds.region-id' = 'cn-beijing',
    'rds.access-key-id' = 'xxxxxxxxx',
    'rds.access-key-secret' = 'xxxxxxxxx',
    'rds.db-instance-id' = 'rm-xxxxxxxxxxxxxxxxx',
    'rds.main-db-id' = '12345678',
    'rds.download.timeout' = '60s'
    ...
```

) 开启Binlog解析加速在增量阶段，MySQL CDC源表会解析Binlog文件生成各种变更消息，Binlog文件使用二进制记录着所有表的变更，通过配置下述参数可以加速Binlog文件解析的过程： 使用配置项scan.only.deserialize.captured.tables.changelog.enabled可以配置仅对指定的表事件进行解析。 使用配置项scan.only.deserialize.captured.tables.changelog.enabled可以配置采用多线程对 Binlog文件进行解析、并按顺序投放到消费队列。 使用示例：

```
    'connector' = 'mysql-cdc',
    'scan.only.deserialize.captured.tables.changelog.enabled' = 'true',  -- 仅对指定的表
```

事件进行解析。

```
    'scan.parallel-deserialize-changelog.enabled' = 'true'  -- 使用多线程对Binlog进行解析
```

。

```
    ...
```

)

**重要**

通过DataStream的方式读写数据时，则需要使用对应的DataStream连接器连接Flink。 实时计算（流计算）

```java
import org.apache.flink.api.common.eventtime.WatermarkStrategy; import org.apache.flink.streaming.api.environment.StreamExecutionEnvironment; import com.ververica.cdc.debezium.JsonDebeziumDeserializationSchema; import com.ververica.cdc.connectors.mysql.source.MySqlSource;
  public static void main(String[] args) throws Exception {
    MySqlSource<String> mySqlSource = MySqlSource.<String>builder()
        .hostname("yourHostname")
        .port(yourPort)
        .databaseList("yourDatabaseName") // set captured database
        .tableList("yourDatabaseName.yourTableName") // set captured table
        .username("yourUsername")
        .password("yourPassword")
        .deserializer(new JsonDebeziumDeserializationSchema()) // converts SourceRecord
to JSON String
        .build();
    StreamExecutionEnvironment env =
StreamExecutionEnvironment.getExecutionEnvironment();
    // enable checkpoint
    env.enableCheckpointing(3000);
    env
      .fromSource(mySqlSource, WatermarkStrategy.noWatermarks(), "MySQL Source")
      // set 4 parallel source tasks
      .setParallelism(4)
      .print().setParallelism(1); // use parallelism 1 for sink to keep message
ordering
    env.execute("Print MySQL Snapshot + Binlog");
  }
}
```

| 参数 | 说明 |
|---|---|
| hostname | MySQL数据库的IP地址或者Hostname。 |
| port | MySQL数据库服务的端口号。 |
| databaseList | MySQL数据库名称。 说明数据库名称支持正则表达式以读取多个数据库的数据，您可以使用 .* 匹配所有数据库。 |
| username | MySQL数据库服务的用户名。 |

实时计算（流计算）

| password | MySQL数据库服务的密码。 |
|---|---|
| deserializer | 反序列化器，将SourceRecord类型记录反序列化到指定类型。参数取值如下： RowDataDebeziumDeserializeSchema：将SourceRecord转成Flink Table或SQL内部数据结构RowData。 JsonDebeziumDeserializationSchema：将SourceRecord转成JSON格式的String。 |

实时计算（流计算） 模型集成

## AI大语言模型集成

### 模型设置

本文为您介绍注册、查询、修改、删除AI模型的DDL数据定义语句。

**使用须知**

支持OpenAI兼容接口的大模型服务。 部署的大模型服务网络可达，以支持实时计算 Flink 版服务调用。 仅实时计算引擎VVR 11.1及以上版本支持。

**说明**

请联系技术人员获取模型服务域名地址等相关信息。

**CREATE MODEL**

**注册模型**

1. 在实时计算开发控制台上**数据开发** **> ETL**页面新建作业草稿。详情请参见《**Flink****存算分离版****用户指**
**南》** > **数据开发** > **作业开发**。
2. 在**ETL**文本编辑区域，输入以下命令。

```xml
CREATE [TEMPORARY] MODEL [catalog_name.][db_name.]model_name INPUT ( { <physical_column_definition> [, ...n] ) OUTPUT ( { <physical_column_definition> [, ...n] ) WITH (key1=val1, key2=val2, ...) <physical_column_definition>:
  column_name column_type [COMMENT column_comment]
```

| 子句 | 描述 |  | 关键参数 |  |  |  | Schema限制 | 示例 |  |
|---|---|---|---|---|---|---|---|---|---|
| INPU T | 定义模型输入数据的字段、类型以及字段的顺序。 |  | column name _ （字段名） |  |  |  |  | INPUT (`input text` STRING _ COMMENT '用户评论') |  |
|  |  |  |  | column name _ |  |  |  |  | INPUT (`input text` STRING _ |
|  |  | 段、类型段的顺 |  |  |  |  |  | COMMENT '用户评论') |  |
|  |  |  |  |  | （字段名 |  |  |  |  |
|  |  |  | column type _ （类型） COMMENT （ 注释） |  |  |  | 有且仅有一个 STRING类型的字段。 |  |  |

实时计算（流计算） 模型集成

| OUT PUT |  | 定义模型输出数据的字段、类型以及字段顺序。 |  | column name _ （字段名） |  |  |  |  |  | 不同模型任务类型限 |  | OUTPUT (`sentiment label` _ STRING COMMENT '情感标签') |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  | column name _ |  |  |  |  |  |  |  | OUTPUT (`sentiment label` _ |  |
|  |  |  | 段、类型段顺序。 |  |  |  |  |  |  | 制如下： |  | STRING COMMENT '情感标签') |  |  |
|  |  |  |  |  |  | （字段名 |  |  |  |  |  |  |  |  |
|  |  |  |  | column type _ （类型） COMMENT （ 注释） |  |  |  |  |  | chat/completio ns：有且仅有一个STRING类型的字段。 embeddings： 有且仅有一个 ARRAY<FLOAT >类型的字段。 |  |  |  |  |
| WIT H |  | 请参见WITH参数。 |  | provider （ 服务名） endpoint （ |  |  |  |  |  |  |  | WITH |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  | WITH |  |
|  |  |  |  |  |  |  |  |  |  |  |  | ('provider'='bailian', |  |  |
|  |  |  |  |  |  |  | oint （ |  |  |  |  |  |  |  |
|  |  |  |  |  | endp |  | oint |  |  |  |  | 'endpoint'='${ENDPOINT}', |  |  |
|  |  |  |  | 接入地址） |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  | 'model'='qwen-turbo', |  |  |
|  |  |  |  | apiKey （密 |  |  |  |  |  | 无。 |  | 'apiKey'='${KEY}') |  |  |
|  |  |  |  | 钥） model （模型标识） |  |  |  |  |  |  |  |  |  |  |

**示例**

**百炼专属版模型服务**

```
CREATE MODEL model_bailian INPUT (`input` STRING) OUTPUT (`content` STRING) WITH (
  'provider'='bailian',
  'endpoint'='<Endpoint>',
  'api-key'='<bailian-key>',
  'model'='<Model>'
);
```

百炼专属版平台模型服务端口格式为： `<base-url>/compatible-mode/v1/<task>` 。

**base-url：**

**说明**

请联系技术人员获取百炼专属版模型的服务域名地址。
**task**：模型任务类型。支持以下取值。
chat/completions embeddings

**机器学习平台PAI**

实时计算（流计算） 模型集成

```
CREATE MODEL model_pai INPUT (`input` STRING) OUTPUT (`embedding` ARRAY<FLOAT>) WITH (
  'provider'='bailian',
```

`'endpoint'='<VPC`调用地址`>',`

```
  'api-key'='<Token>',
  'model'='<Model>'
);
```

请相关技术人员获取模型服务调用信息。

**重要**

VPC调用地址为http，需修改为https。地址后缀需要添加 `/v1/<task>` 。task：模型任务类型。支持以下取值： chat/completions embeddings Token为参数api-key的值。

**WITH参数**

**通用**

| 参数 | 说明 | 数据类型 | 是否必填 | 默认值 | 备注 |
|---|---|---|---|---|---|
| provid er | 模型服务类型。 | String | 是 | 无 | 固定值为 bailian 。 说明支持PAI平台或其他兼容OpenAI API模型服务，固定值不变。 |
| endpoi nt | 模型服务端口，或其他兼容OpenAI API 的Embeddings和 Chat/Completions 模型服务端口。 | String | 是 | 无 | 百炼专属版模型服务或PAI平台端口详见示例。 其他兼容OpenAI API的Embeddings 和Chat/Completions模型服务，可根据相应的API文档填写端口值。 |
| api-key | 用来访问百炼平台接口的密钥。 | String | 是 | 无 | 曾用键名：apiKey（vvr 11.1版本） |
| max- contex t-size | 单个请求的上下文的最大容量 | Integer | 否 | 无 | vvr 11.2及以上版本支持。 如果超过了最大容量，会触发 context-overflow-action中定义的行为。 |

实时计算（流计算） 模型集成

| contex t- overflo w- action | 单个请求的上下文超过最大容量时的处理行为 | String | 否 | truncat ed-tail | vvr 11.2及以上版本支持。 可选值如下： truncated-tail : 自动从尾部裁剪超出容量的token，保留最近 max-context-size 个token。 不记录日志。 truncated-tail-log : 自动从尾部裁剪超出容量的token，保留最近 max-context-size 个token。 记录截断日志。 truncated-head : 从头部裁剪最早的token，保留最新 max- context-size 个token。 truncated-head-log : 从头部裁剪最早的token，保留最新 max- context-size 个token。记录截断日志。 skipped : 直接丢弃该条数据。不记录日志。 skipped-log : 直接丢弃该条数据并记录日志。 |  |  |
|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  | max- |  |

|  |  | truncat | vvr 11 |
|---|---|---|---|
|  | ed-tail |  |  |

| max- |  |
|---|---|

|  | context-size |
|---|---|

|  | context-size |
|---|---|

**chat/completions**

Chat/Completions模型任务依赖如下参数：

| 参数 | 说明 | 数据类型 | 是否必填 | 默认值 | 备注 |
|---|---|---|---|---|---|
| model | 调用的服务端的具体模型。 | String | 是 | 无 | 支持文本生成类别的模型。 |
| system- prompt | 请求回答时的系统提示。 | String | 是 | "You are a helpful assistant." | 曾用键名：systemPrompt（vvr 11.1版本） |
| temperatur e | 控制生成文本时对每个候选词概率分布的平滑程度。 | float | 否 | 无 | 取值范围： [0, 2)。不建议取值为 0，无意义。 较高的temperature值会降低概率分布的峰值，使得更多的低概率词被选择，生成结果更加多样化；而较低的temperature值则会增强概率分布的峰值，使得高概率词更容易被选择，生成结果更加确定。 |
| top-p | 生成过程中核采样方法的概率阈值。 | float | 否 | 无 | 取值越大，生成的随机性越高；取值越小，生成的确定性越高。 曾用键名：topP（vvr 11.1版本） |

实时计算（流计算） 模型集成

| stop | 停用词。 | String | 否 | 无 | 在模型生成的内容即将包含指定的字符串时自动停止。 |
|---|---|---|---|---|---|
| max-tokens | 指定模型可生成的最大token个数。 | Integ er | 否 | 无 | 曾用键名：maxTokens（vvr 11.1版本） |

**embeddings**

Embeddings模型任务依赖如下参数：

| 参数 | 说明 | 数据类型 | 是否必填 | 默认值 | 备注 |
|---|---|---|---|---|---|
| model | 调用的服务端的具体模型。 | String | 是 | 无 | 支持文本向量模型。 |
| dimens ion | 控制输出的向量维度。 | Intege r | 否 | 102 4 | 可选值：1024, 768, 512。暂不支持其他值， 否则会提示错误。 |

**查看模型**

在**ETL**文本编辑区域，输入以下命令。 展示注册的模型名字。

```
SHOW MODELS [ ( FROM | IN ) [catalog_name.]database_name ];
```

展示创建模型的语句。

```
SHOW CREATE MODEL [catalog_name.][db_name.]model_name;
```

展示模型的输入输出结构。

```
DESCRIBE MODEL [catalog_name.][db_name.]model_name;
```

**示例**

实时计算（流计算） 模型集成

```
SHOW MODELS; --+------------+ --| model name | --+------------+ --| m | --+------------+ DESCRIBE MODEL m; -- +---------+--------+------+----------+ -- | name | type | null | is input | -- +---------+--------+------+----------+ -- | content | STRING | TRUE | TRUE | -- | label | BIGINT | TRUE | FALSE | -- +---------+--------+------+----------+
```

**修改模型**

在**ETL**文本编辑区域，输入以下命令。

```
ALTER MODEL [IF EXISTS] [catalog_name.][db_name.]model_name {
  RENAME TO new_table_name
  SET (key1=val1, ...)
  RESET (key1, ...)
}
```

**示例**

重命名已注册的模型。

```
ALTER MODEL m RENAME TO m1; -- 重命名为 m1;
```

修改模型参数。

```
ALTER MODEL m SET ('endpoint' = '<Your_Endpoint>'); -- 调整 endpoint 路径;
```

重置模型参数，还原为默认参数值。

```
ALTER MODEL m RESET ('endpoint'); -- 重置 endpoint 路径;
```

**删除模型**

在**ETL**文本编辑区域，输入以下命令。

```
DROP [TEMPORARY] MODEL [IF EXISTS] [catalog_name.][db_name.]model_name
```

**示例**

```
DROP MODEL m;
```

实时计算（流计算） 模型集成

### 通用调用

本文为您介绍如何使用ML_PREDICT进行AI大模型推断。

**使用限制**

仅实时计算引擎VVR 11.1及以上版本支持。 ML_PREDICT语句相关的Flink算子的吞吐量受到模型平台限流的限制。当触及模型平台允许的访问流量上限时，Flink作业会表现出以ML_PREDICT算子为瓶颈的反压现象。在限流情况严重时，可能会触发相关算子的超时报错及作业重启。

**语法**

```
ML_PREDICT(TABLE <TABLE NAME>, MODEL <MODEL NAME>, DESCRIPTOR(<INPUT COLUMN NAMES>))
```

**入参**

| 参数 | 数据类型 | 说明 |
|---|---|---|
| TABLE <TABLE NAME> | TABLE | 模型推断的输入数据流。可以是物理表名，也可以是视图名。 |
| MODEL <MODEL NAME> | MODEL | 注册的模型服务名字。详情请参见模型设置注册模型服务。 |
| DESCRIPTOR(<INPUT COLUMN NAMES>) | - | 输入数据中被用来作为模型推断列。 |

**示例**

**测试数据**

| id | movie nam _ e | user comment _ | actual label _ |
|---|---|---|---|
| 1 | 好东西 | 最爱小孩子猜声音那段，算得上看过的电影里相当浪漫的叙事了。很温和也很有爱。 | POSITIVE |
| 2 | 水饺皇后 | 乏善可陈 | NEGATIVE |

**测试语句**

创建大模型，使用ML_PREDICT函数对电影评论进行情感分类预测，SQL示例如下。 实时计算（流计算） 模型集成

```
CREATE TEMPORARY MODEL ai_analyze_sentiment INPUT (`input` STRING) OUTPUT (`content` STRING) WITH (
    'provider'='bailian',
    'endpoint'='<YOUR ENDPOINT>',
    'apiKey' = '<YOUR KEY>',
    'model'='<YOUR MODEL>',
    'systemPrompt' = 'Classify the text below into one of the following labels:
[positive, negative, neutral, mixed]. Output only the label.' ); CREATE TEMPORARY VIEW movie_comment(id, movie_name, user_comment, actual_label)
```

`AS VALUES (1, '`好东西`', '`最爱小孩子猜声音那段，算得上看过的电影里相当浪漫的叙事了。很温和也很有爱。 `', 'positive'), (2, '`水饺皇后`', '`乏善可陈', 'negative');

```
SELECT id, movie_name, content as predict_label, actual_label FROM ML_PREDICT(TABLE movie_comment, MODEL ai_analyze_sentiment, DESCRIPTOR(user_comment));
```

**输出结果**

预测结果 `predict_label` 与实际结果 `actual_label` 一致。

| id | movie nam _ e | predict label _ | actual label _ |
|---|---|---|---|
| 1 | 好东西 | POSITIVE | POSITIVE |
| 2 | 水饺皇后 | NEGATIVE | NEGATIVE |

### 文本分类

本文为您介绍如何使用AI_CLASSIFY通过AI大模型进行分类。

**使用限制**

仅实时计算引擎VVR 11.4及以上版本支持。 AI_CLASSIFY语句相关的Flink算子的吞吐量受到模型平台限流的限制。当触及平台允许的访问流量上限时，Flink作业会表现出以该算子为瓶颈的反压现象。在限流情况严重时，可能会触发相关算子的超时报错及作业重启。

**语法**

```
AI_CLASSIFY(
  MODEL => MODEL <MODEL NAME>,
  INPUT => <INPUT COLUMN NAME>,
  LABELS => <LABELS>
```

) 实时计算（流计算） 模型集成

**入参**

| 参数 | 数据类型 | 说明 |
|---|---|---|
| MODEL <MODEL NAME> | MODEL | 注册的模型服务名字。详情请参见模型设置注册模型服务。 说明目前需要该模型的输出类型为 VARIANT 类型。 |
| <INPUT COLUMN NAME> | STRING | 模型的待分类数据。 |
| <LABELS> | ARRAY<STRING > | 预期的分类类别。 说明目前该入参需要是一个常量。 |

**输出**

| 参数 | 数据类型 | 说明 |
|---|---|---|
| category | STRING | 模型判断的类别 |
| confidence | DOUBLE | 模型输出的置信度 |

**示例**

**测试数据**

| id | content | expected category _ |
|---|---|---|
| 1 | 【李宁官方旗舰店】革德之道10 男子篮球鞋实战球鞋减震回弹云五代科技黑红配色 | Clothing Shoes Accessories |
| 2 | Apple iPhone 15 Pro Max 256GB 深空黑 5G手机 A17Pro芯片钛金属边框官方正品国行 | Digital Product |

**测试语句**

创建大模型，使用AI_CLASSIFY函数对商品类别进行分类，SQL示例如下。 实时计算（流计算） 模型集成

```
CREATE TEMPORARY MODEL general_model INPUT (`input` STRING) OUTPUT (`content` VARIANT) WITH (
    'provider' = 'openai-compat',
    'endpoint'='<YOUR ENDPOINT>',
    'apiKey' = '<YOUR KEY>',
    'model' = '<YOUR MODEL>'
); CREATE TEMPORARY VIEW products(id, content)
```

`AS VALUES (1, '`【李宁官方旗舰店】革德之道`10` 男子篮球鞋实战球鞋减震回弹云五代科技黑红配色`'), (2` `, 'Apple iPhone 15 Pro Max 256GB` 深空黑 `5G`手机 `A17Pro`芯片钛金属边框官方正品国行');

```
-- Use positional argument to call AI_CLASSIFY SELECT id, category, confidence FROM products, LATERAL TABLE(
  AI_CLASSIFY(
    MODEL general_model, content, ARRAY['Digital Product', 'Clothing Shoes Accessories']
)); -- Use named argument to call AI_CLASSIFY SELECT id, category, confidence FROM products, LATERAL TABLE(
  AI_CLASSIFY(
    MODEL => MODEL general_model,
    INPUT => content,
    LABELS => ARRAY['Digital Product', 'Clothing Shoes Accessories']));
```

**输出结果**

| id | category | confidence |
|---|---|---|
| 1 | Clothing Shoes Accessories | 0.95 |
| 2 | Digital Product | 0.99 |

### 情感分析

本文为您介绍如何使用AI_SENTIMENT通过AI大模型进行情感分析。

**使用限制**

仅实时计算引擎VVR 11.4及以上版本支持。 AI_SENTIMENT语句相关的Flink算子的吞吐量受到模型平台限流的限制。当触及平台允许的访问流量上限时，Flink作业会表现出以该算子为瓶颈的反压现象。在限流情况严重时，可能会触发相关算子的超时报错及作业重启。

**语法**

实时计算（流计算） 模型集成

```
AI_SENTIMENT(
  MODEL => MODEL <MODEL NAME>,
  INPUT => <INPUT COLUMN NAME>
```

)

**入参**

| 参数 | 数据类型 | 说明 |
|---|---|---|
| MODEL <MODEL NAME> | MODEL | 注册的模型服务名字。详情请参见模型设置注册模型服务。 说明目前需要该模型的输出类型为 VARIANT 类型。 |
| <INPUT COLUMN NAME> | STRING | 模型的待分析数据。 |

**输出**

| 参数 | 数据类型 | 说明 |
|---|---|---|
| score | DOUBLE | 模型判断的情感分数（-1.0 到 1.0 之间）: -1.0： 极度负面 -0.5：较为负面 -0.0：中性 0.5：较为正面 1.0 极度正面 |
| label | STRING | 情感标签（positive/negative/neutral）。 |
| confidence | DOUBLE | 模型输出的置信度。 |

**示例**

**测试数据**

| id | movie nam _ e | comment | actual label _ |
|---|---|---|---|
| 1 | 好东西 | 最爱小孩子猜声音那段，算得上看过的电影里相当浪漫的叙事了。很温和也很有爱。 | POSITIVE |
| 2 | 水饺皇后 | 乏善可陈。 | NEGATIVE |

实时计算（流计算） 模型集成

**测试语句**

创建大模型，使用AI_SENTIMENT函数对电影评论进行情感分类预测，SQL示例如下。

```
CREATE TEMPORARY MODEL general_model INPUT (`input` STRING) OUTPUT (`content` VARIANT) WITH (
    'provider' = 'openai-compat',
    'endpoint'='<YOUR ENDPOINT>',
    'apiKey' = '<YOUR KEY>',
    'model' = '<YOUR MODEL>'
); CREATE TEMPORARY VIEW movie_comment(id, movie_name, user_comment, actual_label)
```

`AS VALUES (1, '`好东西`', '`最爱小孩子猜声音那段，算得上看过的电影里相当浪漫的叙事了。很温和也很有爱。 `', 'positive'), (2, '`水饺皇后`', '`乏善可陈。', 'negative');

```
-- Use positional argument to call AI_SENTIMENT SELECT id, movie_name, actual_label, score, label, confidence FROM movie_comment, LATERAL TABLE(
  AI_SENTIMENT(
    MODEL general_model, user_comment));
-- Use named argument to call AI_SENTIMENT SELECT id, movie_name, actual_label, score, label, confidence FROM movie_comment, LATERAL TABLE(
  AI_SENTIMENT(
    MODEL => MODEL general_model,
    INPUT => user_comment));
```

**输出结果**

预测结果 `label` 与实际结果 `actual_label` 一致。

| id | movie na _ me | actual label _ | score | label | confidence |
|---|---|---|---|---|---|
| 1 | 好东西 | positive | 0.8 | positive | 0.95 |
| 2 | 水饺皇后 | negative | -1.0 | negative | 0.95 |

### 信息提取

本文为您介绍如何使用AI_EXTRACT通过AI大模型进行结构化信息提取。

**使用限制**

仅实时计算引擎VVR 11.4及以上版本支持。 AI_EXTRACT语句相关的Flink算子的吞吐量受到模型平台限流的限制。当触及平台允许的访问流量上限时，Flink作业会表现出以该算子为瓶颈的反压现象。在限流情况严重时，可能会触发相关算子的超时报错及作业重启。 实时计算（流计算） 模型集成

**语法**

```
AI_EXTRACT(
  MODEL => MODEL <MODEL NAME>,
  INPUT => <INPUT COLUMN NAME>,
  EXTRACT_SCHEMA => <EXTRACT SCHEMA>
```

)

**入参**

| 参数 | 数据类型 | 说明 |
|---|---|---|
| MODEL <MODEL NAME> | MODEL | 注册的模型服务名字。详情请参见模型设置注册模型服务。 说明目前需要该模型的输出类型为 VARIANT 类型。 |
| <INPUT COLUMN NAME> | STRING | 模型待提取信息的原始文本。 |
| <EXTRACT SCHEMA> | STRING | 用JSON文本的形式描述提取的schema信息。 说明目前该入参需要是一个常量。 |

**输出**

| 参数 | 数据类型 | 说明 |
|---|---|---|
| extracted json _ | STRING | 提取出的结构化信息。 |

**示例**

**测试数据**

| id | description |
|---|---|
| 1 | 小明今年18岁住在杭州，他的号码是******。 |

**测试语句**

创建大模型，使用AI_EXTRACT提取用户信息，SQL示例如下。 实时计算（流计算） 模型集成

```
CREATE TEMPORARY MODEL general_model INPUT (`input` STRING) OUTPUT (`content` VARIANT) WITH (
    'provider' = 'openai-compat',
    'endpoint'='<YOUR ENDPOINT>',
    'apiKey' = '<YOUR KEY>',
    'model' = '<YOUR MODEL>'
); CREATE TEMPORARY VIEW infos(id, description)
```

`AS VALUES (1, '`小明今年`18`岁住在杭州，他的号码是`******`。');

```
-- Use positional argument to call AI_EXTRACT SELECT id, extracted_json FROM infos, LATERAL TABLE(
  AI_EXTRACT(
    MODEL general_model,
    description,
    '{"name":"string","phone":"string","address":"string","age":"int"}'));
-- Use named argument to call AI_EXTRACT SELECT id, extracted_json FROM infos, LATERAL TABLE(
  AI_EXTRACT(
    MODEL => MODEL general_model,
    INPUT => description,
    EXTRACT_SCHEMA =>
'{"name":"string","phone":"string","address":"string","age":"int"}'));
```

**输出结果**

| id | extracted json _ |
|---|---|
| 1 | {"address":"杭州","age":18,"name":"小明","phone":"******"} |

### 文本摘要

本文为您介绍如何使用AI_SUMMARIZE通过AI大模型生成文本摘要。

**使用限制**

仅实时计算引擎VVR 11.4及以上版本支持。 AI_SUMMARIZE语句相关的Flink算子的吞吐量受到模型平台限流的限制。当触及平台允许的访问流量上限时，Flink作业会表现出以该算子为瓶颈的反压现象。在限流情况严重时，可能会触发相关算子的超时报错及作业重启。

**语法**

实时计算（流计算） 模型集成

```
AI_SUMMARIZE(
  MODEL => MODEL <MODEL NAME>,
  INPUT => <INPUT COLUMN NAME>,
  MAX_LENGTH => <MAX LENGTH>
```

)

**入参**

| 参数 | 数据类型 | 说明 |
|---|---|---|
| MODEL <MODEL NAME> | MODEL | 注册的模型服务名字。详情请参见模型设置注册模型服务。 说明目前需要该模型的输出类型为 VARIANT 类型。 |
| <INPUT COLUMN NAME> | STRING | 模型的待分析数据。 |
| <MAX LENGTH> | INTEGER | 模型输出的最大长度。 说明目前该入参需要是一个常量。 |

**输出**

| 参数 | 数据类型 | 说明 |
|---|---|---|
| summary | STRING | 总结的内容 |

**示例**

**测试数据**

| id | description |
|---|---|
| 1 | 什么是 Flink Apache Flink 是一个开源的分布式流处理框架，用于对实时数据流和批量数据进行有状态计算。 简单理解： Flink 是一个处理实时数据的计算引擎可以处理持续不断产生的数据流（如网站点击、物联网传感器数据、股票交易等） 提供低延迟、高吞吐、精确一次的语义保证同时支持流处理和批处理 |

实时计算（流计算） 模型集成

**测试语句**

创建大模型，使用AI_SUMMARIZE总结输入数据

```
CREATE TEMPORARY MODEL general_model INPUT (`input` STRING) OUTPUT (`content` VARIANT) WITH (
    'provider' = 'openai-compat',
    'endpoint'='<YOUR ENDPOINT>',
    'apiKey' = '<YOUR KEY>',
    'model' = '<YOUR MODEL>'
); CREATE TEMPORARY VIEW infos(id, description) AS VALUES (1, '
```

什么是 `Flink` `Apache Flink` 是一个开源的分布式流处理框架，用于对实时数据流和批量数据进行有状态计算。 简单理解： `Flink` 是一个处理实时数据的计算引擎可以处理持续不断产生的数据流（如网站点击、物联网传感器数据、股票交易等） 提供低延迟、高吞吐、精确一次的语义保证同时支持流处理和批处理

```
'); -- Use positional argument to call AI_SUMMARIZE SELECT id, summary FROM infos, LATERAL TABLE(
  AI_SUMMARIZE(MODEL general_model, description, 10));
-- Use named argument to call AI_SUMMARIZE SELECT id, summary FROM infos, LATERAL TABLE(
  AI_SUMMARIZE(
    MODEL => MODEL general_model,
    INPUT => description,
    MAX_LENGTH => 10));
```

**输出结果**

| id | summary |
|---|---|
| 1 | 实时流处理引擎 |

### 文本翻译

本文为您介绍如何使用AI_TRANSLATE通过AI大模型进行翻译。

**使用限制**

仅实时计算引擎VVR 11.4及以上版本支持。 实时计算（流计算） 模型集成 AI_TRANSLATE语句相关的Flink算子的吞吐量受到模型平台限流的限制。当触及平台允许的访问流量上限时，Flink作业会表现出以该算子为瓶颈的反压现象。在限流情况严重时，可能会触发相关算子的超时报错及作业重启。

**语法**

```
AI_TRANSLATE(
  MODEL => MODEL <MODEL NAME>,
  INPUT => <INPUT COLUMN NAME>,
  SOURCE_LANG => <SOURCE LANGUAGE>,
  TARGET_LANG => <TARGET LANGUAGE>
```

)

**入参**

| 参数 | 数据类型 | 说明 |
|---|---|---|
| MODEL <MODEL NAME> | MODEL | 注册的模型服务名字。详情请参见模型设置注册模型服务。 说明目前需要该模型的输出类型为 VARIANT 类型。 |
| <INPUT COLUMN NAME> | STRING | 模型待分析的原始文本。 |
| <SOURCE LANGUAGE> | STRING | 源语言英文缩写。例如对于中文请输入 zh 。若输入为 auto ，则表示让模型自动检测。 目前支持的源语言如下： 中文（zh）英文 (en)、日文 (ja)、韩文 (ko)、法文 (fr)、德文 (de)、西班牙文 (es)、俄文 (ru)、阿拉伯文 (ar)、葡萄牙文 (pt) 说明实际支持的语言类型由模型决定。 目前该入参需要是一个常量。 |
| <TARGET LANGUAGE> | STRING | 目标语言的英文缩写。例如，翻译成中文请输入 zh 。 目前支持的目标语言如下： 中文（zh）英文 (en)、日文 (ja)、韩文 (ko)、法文 (fr)、德文 (de)、西班牙文 (es)、俄文 (ru)、阿拉伯文 (ar)、葡萄牙文 (pt) 说明实际支持的语言类型由模型决定。 目前该入参需要是一个常量。 |

实时计算（流计算） 模型集成

**输出**

| 参数 | 数据类型 | 说明 |
|---|---|---|
| translated text _ | STRING | 翻译后的文字。 |
| detected language _ | STRING | 识别到的语言。 |

**示例**

**测试数据**

| id | content |
|---|---|
| 1 | I like Flink very much. It's so fast! |

**测试语句**

创建大模型，使用AI_TRANSLATE翻译输入文本，SQL示例如下。 实时计算（流计算） 模型集成

```
CREATE TEMPORARY MODEL general_model INPUT (`input` STRING) OUTPUT (`content` VARIANT) WITH (
    'provider' = 'openai-compat',
    'endpoint'='<YOUR ENDPOINT>',
    'apiKey' = '<YOUR KEY>',
    'model' = '<YOUR MODEL>'
); CREATE TEMPORARY VIEW infos(id, content) AS VALUES (1, 'I like Flink very much. It''s so fast!'); -- Use positional argument to call AI_TRANSLATE SELECT id, translated_text, detected_language FROM infos, LATERAL TABLE(
  AI_TRANSLATE(
    MODEL general_model,
    content,
    'auto',
    'zh'
    ));
-- Use named argument to call AI_TRANSLATE SELECT id, translated_text, detected_language FROM infos, LATERAL TABLE(
  AI_TRANSLATE(
    MODEL => MODEL general_model,
    INPUT => content,
    SOURCE_LANG =>'auto',
    TARGET_LANG => 'zh'
    ));
```

**输出结果**

| id | translated text _ | detected language _ |
|---|---|---|
| 1 | 我非常喜欢 Flink，它非常快！ | en |

### 数据脱敏

本文为您介绍如何使用AI_MASK通过AI大模型进行数据脱敏。

**使用限制**

仅实时计算引擎VVR 11.4及以上版本支持。 实时计算（流计算） 模型集成 AI_MASK语句相关的Flink算子的吞吐量受到模型平台限流的限制。当触及平台允许的访问流量上限时，Flink作业会表现出以该算子为瓶颈的反压现象。在限流情况严重时，可能会触发相关算子的超时报错及作业重启。

**语法**

```
AI_MASK(
  MODEL => MODEL <MODEL NAME>,
  INPUT => <INPUT COLUMN NAME>,
  MASK_ENTITIES => <MASK ENTITIES>
```

)

**入参**

| 参数 | 数据类型 | 说明 |
|---|---|---|
| MODEL <MODEL NAME> | MODEL | 注册的模型服务名字。详情请参见模型设置注册模型服务。 说明目前需要该模型的输出类型为 VARIANT 类型。 |
| <INPUT COLUMN NAME> | STRING | 模型待分析的原始文本。 |
| <MASK ENTITIES> | ARRAY<STRING > | 需要脱敏的实体。 说明目前该入参需要是一个常量。 |

**输出**

| 参数 | 数据类型 | 说明 |
|---|---|---|
| masked text _ | STRING | 脱敏后的文字。 |
| detected entities _ | ARRAY<STRING > | 检测到的实体。 |

**示例**

**测试数据**

| id | content |
|---|---|
| 1 | Timmo真的太爱学习了吧，一有空闲就看到他在看学习资料。 |

实时计算（流计算） 模型集成

**测试语句**

创建大模型，使用AI_MASK进行数据脱敏，SQL示例如下。

```
CREATE TEMPORARY MODEL general_model INPUT (`input` STRING) OUTPUT (`content` VARIANT) WITH (
    'provider' = 'openai-compat',
    'endpoint'='<YOUR ENDPOINT>',
    'apiKey' = '<YOUR KEY>',
    'model' = '<YOUR MODEL>'
); CREATE TEMPORARY VIEW infos(id, content)
```

`AS VALUES (1, 'Timmo`真的太爱学习了吧，一有空闲就看到他在看学习资料。');

```
-- Use positional argument to call AI_MASK SELECT id, masked_text, detected_entities FROM infos, LATERAL TABLE(
  AI_MASK(
    MODEL general_model,
    content,
    ARRAY['name']
    ));
-- Use named argument to call AI_MASK SELECT id, masked_text, detected_entities FROM infos, LATERAL TABLE(
  AI_MASK(
    MODEL => MODEL general_model,
    INPUT => content,
    MASK_ENTITIES => ARRAY['name']
    ));
```

**输出结果**

| id | masked text _ | detected entities _ |
|---|---|---|
| 1 | [NAME]真的太爱学习了吧，一有空闲就看到他在看学习资料。 | [{"entity":"Timmo","type":"name"}] |

### 文本向量化

本文为您介绍如何使用AI_EMBED通过AI大模型进行向量生成。

**使用限制**

仅实时计算引擎VVR 11.4及以上版本支持。 实时计算（流计算） 模型集成 AI_EMBED语句相关的Flink算子的吞吐量受到模型平台限流的限制。当触及平台允许的访问流量上限时，Flink作业会表现出以该算子为瓶颈的反压现象。在限流情况严重时，可能会触发相关算子的超时报错及作业重启。

**语法**

```
AI_EMBED(
  MODEL => MODEL <MODEL NAME>,
  INPUT => <INPUT COLUMN NAME>
```

)

**入参**

| 参数 | 数据类型 | 说明 |
|---|---|---|
| MODEL <MODEL NAME> | MODEL | 注册的模型服务名字。详情请参见模型设置注册模型服务。 说明目前需要该模型的输出类型为 ARRAY<FLOAT> 类型。 |
| <INPUT COLUMN NAME> | STRING | 模型待分析的原始文本。 |

**输出**

| 参数 | 数据类型 | 说明 |
|---|---|---|
| embedding | ARRAY<FLOAT > | 生成的1024维向量。 |

**示例**

**测试数据**

| id | content |
|---|---|
| 1 | Flink |

**测试语句**

创建text-embedding-v3模型，使用AI_EMBED生成向量，SQL示例如下。 实时计算（流计算） 模型集成

```
CREATE TEMPORARY MODEL embedding_model INPUT (`input` STRING) OUTPUT (`embedding` ARRAY<FLOAT>) WITH (
    'provider' = 'bailian',
    'endpoint'='<YOUR ENDPOINT>',
    'apiKey' = '<YOUR KEY>',
    'model' = 'text-embedding-v3',
    'dimension' = '1024'
); CREATE TEMPORARY VIEW infos(id, content) AS VALUES (1, 'Flink'); -- Use positional argument to call AI_EMBED SELECT id, embedding FROM infos, LATERAL TABLE(
  AI_EMBED(
    MODEL embedding_model,
    content
    ));
-- Use named argument to call AI_MASK SELECT id, embedding FROM infos, LATERAL TABLE(
  AI_EMBED(
    MODEL => MODEL embedding_model,
    INPUT => content
    ));
```

**输出结果**

| id | embedding |
|---|---|
| 1 | [-0.13219477, 0.054332353, -0.033010617, -0.0039787884, ...] |

实时计算（流计算） 参考

## OpenAPI参考

### 准备工作

阿里云专有云与公共云一样，可通过POP网关的方式进行API调用。本文为您介绍调用前需要进行的准备工作。

#### 获取API信息及其Endpoint

通过POP网关调用API需要您了解产品开放API接口的相关信息，本文为您介绍获取云产品的Endpoint的两种方式。

**背景信息**

为了使专有云保持与公共云相同的使用方式，使您拥有更方便，更一致的体验，建议通过POP网关调用专有云API。

**说明**

Apsara Uni-manager运营控制台API目录中的API信息仅供调用参考，具体API的使用方式需要参见云产品的开发指南。如果发生不一致情况，以开发指南支持情况为准。

**操作步骤**

**通过开发者门户获取Endpoint**

1. 登录Apsara Uni-manager运营控制台。
2. 在顶部菜单栏选择**产品** > **应用服务** > **开发者门户**。
3. 在**开发者门户**页面，选择**API****集成** > **API****调试**。
4. 在左侧导航栏中选择目标云产品。
5. 在**版本**下拉列表中，选择目标API版本。
6. 在下方API列表中可浏览当前版本的所有API接口。
7. 选中对应接口，在参数名下获取云产品的POP Endpoint信息。
实时计算（流计算） 参考

**通过飞天基础运维平台获取Endpoint**

通过POP网关调用专有云API时需要使用云产品业务域的Endpoint。您可以在阿里云驻场运维工程师处获取。 您也可以自行获取Endpoint，本文以API网关为例为您介绍获取云产品业务域Endpoint的方法。
1. 登录Apsara Uni-manager运维控制台。
2. 顶部菜单栏选择**平台运维** > **飞天基础运维平台** > **运维工具**。
3. 在左侧导航栏，选择**运维工具** > **服务注册变量大盘**。
4. 在服务注册变量大盘页面，单击**高级筛选**。
5. 在Service Registration文本框中输入 `apigateway` ，单击**搜索**。
6. 在 `apigateway` 服务的**Service Registration**列中，单击
图标。
7. 单击 `apigateway` 服务**Service Registration**列的文本信息，在弹出的**注册变量**对话框中，查看
apigateway.openapi.endpoint值，即 `Endpoint` 。

#### 获取公共Header参数

调用API时需要提供多个Header参数，如RegionID、组织ID、资源集ID和实例ID。本文为您介绍如何获取这些参数，并解释调用后的一些返回值。

**获取Region ID**

1. 管理员登录Apsara Uni-manager运营控制台。
2. 在顶部菜单栏中，单击**企业**。
3. 在左侧导航栏中，选择**资源管理**>**地域管理**。
实时计算（流计算） 参考
4. 单击目标组织名称。
5. 在右侧**Region****列表**中查看**Region****名称**，即为Region ID。

**获取组织ID**

组织ID需要通过调用API方式获取，您可以在Apsara Uni-manager运营控制台中通过API在线调试功能快速获取组织ID信息。
1. 管理员登录Apsara Uni-manager运营控制台。
2. 单击顶部菜单栏**产品**，选择**开发工具** > **开发者门户**。
3. 在**开发者门户**页面，选择**API****集成**> **API****调试**。
4. 单击
按钮，选择**云平台** > **统一云管平台**，**版本**选择2024-09-12。
5. 在文本框内输入 `GetOrganizationList` 进行在线调试，在name参数填写目标组织名称后发起调用，调
用成功后查看**调用结果**中**id**的信息，即为组织ID。接口信息详见Apsara Uni-manager运营控制台开发指南中的章节GetOrganizationList。

**获取资源集ID**

资源集ID需要通过调用API方式获取，您可以在Apsara Uni-manager运营控制台中通过API在线调试功能快速获取资源集ID信息。
1. 管理员登录Apsara Uni-manager运营控制台。
2. 单击顶部菜单栏**产品**，选择**开发工具** > **开发者门户**。
3. 在**开发者门户**页面，选择**API****集成**> **API****调试**。
4. 单击
按钮，选择**云平台** > **统一云管平台**，**版本**选择2024-09-12。
5. 在文本框内输入 `ListResourceGroup` 进行在线调试，调用成功后查看**调用结果**中**id**的信息，即为资源
集ID。接口信息详见Apsara Uni-manager运营控制台开发指南中的章节ListResourceGroup。

**获取实例ID**

实例ID可以通过Apsara Uni-manager运营控制台中的云产品实例列表进行获取，本文中以API网关为例， 获取步骤如下：
1. 登录Apsara Uni-manager运营控制台。
2. 在顶部的菜单栏中，选择**产品**>**开发工具**>API网关。
3. 在左侧导航栏中，单击**实例**。
4. 在实例列表中查看**实例****ID**。

**返回参数**

对于列表类的云产品资源实例接口，调用后会默认增加如下返回值。

| 名称 | 描述 |
|---|---|
| ResourceGroupName | 资源集名称。 |
| ResourceGroup | 资源集ID。 |

实时计算（流计算） 参考

| DepartmentName | 组织名称。 |
|---|---|
| Department | 组织ID。 |

#### 获取AccessKey

AccessKey支持RAM和STS两种授权模式，在发起调用时选择使用其中一种AccessKey即可。本文将为您介绍如何获取通过RAM授权的AccessKey。

**背景信息**

AccessKey通过使用AccessKey ID和AccessKey Secret对称加密，实现验证某个请求发送者的身份的功能。其中AccessKey ID用于标示用户，AccessKey Secret是用户用于加密签名的字符串。 AccessKey的两种授权模式如下： 通过RAM授权给第三方请求者的AccessKey ID和AccessKey Secret。 通过STS授权给第三方请求者的AccessKey ID、AccessKey Secret和Security Token。获取方式请参 Apsara Uni-manager运营控制台提供了个人AccessKey和组织AccessKey（只有运营管理员和一级组织管理员可以获取组织AccessKey），推荐使用个人账号AccessKey调用Apsara Uni-manager运营控制台及云产品相关接口。如果使用个人账号AccessKey，需要在Header中添加以下限制性参数，否则可能提示权限不足： 个人账号AccessKey是由Apsara Uni-manager运营控制台权限体系管控的受限

**警告**

AccessKey，组织AccessKey相对权限较大，需要管理员确认操作的安全性。

| 参数名称 | 描述 |
|---|---|
| x-acs-regionid | 地域，如：cn-hangzhou-*。 |
| x-acs-organizationid | Apsara Uni-manager运营控制台中对应的组织ID。获取方法可参见《Apsara Uni-manager运营控制台开发指南》中的《GetOrganizationList》文档。 |
| x-acs-resourcegroupid | Apsara Uni-manager运营控制台中对应的资源集ID。 获取方法可参见《Apsara Uni-manager运营控制台开发指南》中的《ListResourceGroup》文档。 |
| x-acs-instanceid | 进行操作的实例ID，例如，ECS的实例ID可以从ECS列表中查询到。 |

**获取个人账号AccessKey**

获取个人账号AccessKey的方法如下：
1. 登录Apsara Uni-manager运营控制台。
2. 在系统界面右上角，单击当前登录用户头像，单击**个人信息**。
3. 在**阿里云****AccessKey**区域，您可以查看个人账户的AccessKey信息。
实时计算（流计算） 参考

**说明**

Accesskey ID和AccessKey Secret是您访问云资源时的密钥，具有该账号完整的权限，请您妥善保管。

**获取组织AccessKey**

获取组织AccessKey的方法如下：
1. 管理员登录Apsara Uni-manager运营控制台。
2. 在顶部菜单栏，单击**企业**。
3. 在左侧导航栏中，选择**资源管理** > **组织管理**。
4. 在组织结构中，单击目标一级组织名称。
5. 单击**管理****Accesskey**。
6. 在弹出的对话框中，查看组织AccessKey信息。

#### 获取STS AccessKey

本文为您介绍如何利用STS方式，调用专有云的产品API。

**背景信息**

阿里云临时安全令牌STS（Security Token Service）是阿里云提供的一种临时访问权限管理服务。您可以选择利用STS方式，调用专有云的产品API。

**操作步骤**

1. 获取用户角色的 `RAM Role` 。
i. 登录Apsara Uni-manager运营控制台。 ii. 单击页面右上角的用户头像，选择**个人信息**。 iii. 单击**查看当前角色策略**。

| 框中查看 RAM Role 。 |  |  |
|---|---|---|
| RAM Role | 获得 | stsAK |

实时计算（流计算） 参考

```
public static void main(String[] args) {
     ASClient asClient = new ASClient();
```

`//` 调用来源说明

```
        asClient.setSdkSource("test");
```

`//` 传入`Arn`

```
        String assumeRole = AssumeRole(asClient, "<RAM Role>");
        JSONObject assumeRoleJson = JSONObject.parseObject(assumeRole);
        JSONObject credentials = assumeRoleJson.getJSONObject("Credentials");
```

`//` 获取到`STS`三元组

```
        String stsAK = credentials.getString("AccessKeyId");
        String stsSK = credentials.getString("AccessKeySecret");
        String stsToken = credentials.getString("SecurityToken");
} public static String AssumeRole(ASClient asClient, String roleArn) {
        Map<String, String> headers = new HashMap<>();
        Map<String, Object> reqParams = new HashMap<>();
        reqParams.put("action", "AssumeRole");
        reqParams.put("Product", "Sts");
        reqParams.put("Version", "2015-04-01");
        reqParams.put("regionId", regionId);
```

`//` 当前登录用户的`ak`

```
        reqParams.put("AccessKeyId", <当前用户的AccessKey ID>);
```

`//` 当前登录用户的`sk`

```
        reqParams.put("AccessKeySecret", <当前用户的AccessKey Secret>);
        reqParams.put("roleSessionName", "StsUser");
        reqParams.put("roleArn", roleArn);
        return asClient.doRequest(endpoint, headers, reqParams);
}
```

3. 通过STS可以调用云产品的接口，下列代码以ECS为示例。
实时计算（流计算） 参考

```
public static void main(String[] args) {
     ASClient asClient = new ASClient();
        asClient.setSdkSource("test");
```

`//` 调用云产品的`API`

```
        String ecsRes = DescribeZones(asClient,<stsAK>,<stsSK>,<stsToken>);
} public static String DescribeZones(ASClient asClient, String stsAK, String stsSK, Str ing stsToken) {
        Map<String, String> headers = new HashMap<>();
        Map<String, Object> reqParams = new HashMap<>();
        reqParams.put("action", "DescribeZones");
        reqParams.put("Product", "Ecs");
        reqParams.put("Version", "2014-05-26");
        reqParams.put("regionId", "<your-RegionID>");
        //STS AK/SK/Token三元组
        reqParams.put("AccessKeyId", <stsAK>);
        reqParams.put("AccessKeySecret", <stsSK>);
        reqParams.put("SecurityToken", <stsToken>);
        return asClient.doRequest(endpoint, headers, reqParams, HttpMethod.GET);
    }
```

### 通过POP网关调用专有云API

#### Java版

通过POP Java SDK访问产品域名，需要了解该产品调用方式(RPC或ROA)。

**前提条件**

目前专有云推荐使用CommonRequest进行调用，可以在Apsara Uni-manager运营控制台**产品** > **应用服** 务 > **开发者门户**，选择**API****集成** > **SDK****示例**查看推荐SDK版本以及示例代码。

**重要**

不建议直接从SDK中心下载SDK到专有云场景下使用，公有云的SDK不一定支持专有云的API，可能存在兼容性问题，请谨慎使用！

**CommonRequest调用示例**

RPC调用，示例接口信息：产品（apigateway）、接口（DescribeApiGroups）、版本（2016-07- 14）。 调用示例如下： 实时计算（流计算） 参考

```java
import com.aliyuncs.CommonRequest; import com.aliyuncs.CommonResponse; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.exceptions.ServerException; import com.aliyuncs.http.MethodType; import com.aliyuncs.profile.DefaultProfile; public class DescribeApiGroups {
    public static void main(String[] args) {
```

`//` 创建`DefaultAcsClient`实例并初始化。

```
        DefaultProfile profile = DefaultProfile.getProfile("<your-regionid>", "<yourAcce
ssKeyId>", "<yourAccessSecret>");
```

`//` 忽略`SSL`

```
        // HttpClientConfig clientConfig = HttpClientConfig.getDefault();
        // clientConfig.setIgnoreSSLCerts(true);
```

`//` 设置连接超时

```
        // clientConfig.setConnectionTimeoutMillis(3000L);
```

`//` 设置读取超时

```
        // clientConfig.setReadTimeoutMillis(10000L);
        // profile.setHttpClientConfig(clientConfig);
        IAcsClient client = new DefaultAcsClient(profile);
```

`//` 创建`API`请求并设置参数。

```
        CommonRequest request = new CommonRequest();
```

`//` 设置请求方式

```
        request.setSysMethod(MethodType.POST);
```

`//` 设置云产品`Endpoint`

```
        request.setSysDomain("<apigatewayEndpoint>");
```

`//` 设置访问接口版本

```
        request.setSysVersion("2016-07-14");
        // 设置LocationProduct
        request.setSysLocationProduct("apigateway");
```

`//` 设置访问接口的名称

```
        request.setSysAction("DescribeApiGroups");
```

`//` 当使用`sts ak`调用`RPC`接口时需要在参数中加上`SecurityToken`字段

```
        // request.putBodyParameter("SecurityToken", "<your-SecurityToken>");
```

`//` 业务参数

```
        request.putQueryParameter("PageSize", "10");
        request.putQueryParameter("PageNumber", "1");
```

`//` 必填值，调用来源说明

```
        request.putHeadParameter("x-acs-caller-sdk-source", "ApiTestDemo");
```

`//` 非必填，企业版`V3.15.0`之前历史版本需要

```
        request.putHeadParameter("x-acs-regionid", "<your-regionid>");
```

`//` 非必填，资源集`ID`

```
        request.putHeadParameter("x-acs-resourcegroupid", "<your-resourcegroupid>");
```

`//` 必填, 组织`ID`

```
        request.putHeadParameter("x-acs-organizationid", "<your-organizationid>");
```

实时计算（流计算） 参考 `//` 非必填，修改&删除操作需要

```
        // request.putHeadParameter("x-acs-instanceid", "<your-instanceid>");
        try {
```

`//` 发起请求并处理应答或异常。

```java
            CommonResponse response = client.getCommonResponse(request);
            System.out.println(response.getData());
        } catch (ServerException e) {
            e.printStackTrace();
        } catch (ClientException e) {
            System.out.println("ErrCode:" + e.getErrCode());
            System.out.println("ErrMsg:" + e.getErrMsg());
            System.out.println("RequestId:" + e.getRequestId());
        }
    }
}
```

ROA调用，示例接口信息：产品（CR）接口（GetNamespaceList）版本（2016-06-07）。 调用示例如下：

```java
import com.aliyuncs.CommonRequest; import com.aliyuncs.CommonResponse; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.exceptions.ServerException; import com.aliyuncs.http.MethodType; import com.aliyuncs.profile.DefaultProfile; public class GetNamespaceList {
    public static void main(String[] args) {
```

`//` 创建`DefaultAcsClient`实例并初始化。

```
        DefaultProfile profile = DefaultProfile.getProfile("<your-regionid>", "<yourAcce
ssKeyId>", "<yourAccessSecret>");
```

`//` 忽略`SSL`

```
        // HttpClientConfig clientConfig = HttpClientConfig.getDefault();
        // clientConfig.setIgnoreSSLCerts(true);
```

`//` 设置连接超时

```
        // clientConfig.setConnectionTimeoutMillis(3000L);
```

`//` 设置读取超时

```
        // clientConfig.setReadTimeoutMillis(10000L);
        // profile.setHttpClientConfig(clientConfig);
        IAcsClient client = new DefaultAcsClient(profile);
```

`//` 创建`API`请求并设置参数。

```
        CommonRequest request = new CommonRequest();
```

`//` 设置`HTTPS`访问

```
        request.setSysProtocol(ProtocolType.HTTP);
```

`//` 设置请求方式

```
        request.setSysMethod(MethodType.GET);
```

实时计算（流计算） 参考 q y `yp` `//` 设置云产品`endpoint`

```
        request.setSysDomain("<crEndpoint>");
```

`//` 设置访问接口版本

```
        request.setSysVersion("2016-06-07");
```

`//` 设置`uriPattern` 只有`roa`调用需要传递此字段

```
        request.setSysUriPattern("/namespace");
        // 设置LocationProduct
        request.setSysLocationProduct("cr");
```

`//` 设置访问接口的名称

```
        request.setSysAction("GetNamespaceList");
```

`//` 必填值，调用来源说明

```
        request.putHeadParameter("x-acs-caller-sdk-source", "ApiTestDemo");
```

`//` 非必填，企业版`V3.15.0`之前历史版本需要

```
        request.putHeadParameter("x-acs-regionid", "<your-regionid>");
```

`//` 非必填,资源集`ID`

```
        request.putHeadParameter("x-acs-resourcegroupid", "<your-resourcegroupid>");
```

`//` 必填,组织`ID`

```
        request.putHeadParameter("x-acs-organizationid", "<your-organizationid>");
```

`//` 非必填，修改&删除操作需要

```
        // request.putHeadParameter("x-acs-instanceid", "<your-instanceid>");
```

`//` 当使用`STS AK`调用`ROA`接口时需要在`Header`加上`x-acs-security-token`字段

```
        // request.putHeadParameter("x-acs-security-token", "<your-securitytoken>");
        try {
```

`//` 发起请求并处理应答或异常。

```java
            CommonResponse response = client.getCommonResponse(request);
            System.out.println(response.getData());
        } catch (ServerException e) {
            e.printStackTrace();
        } catch (ClientException e) {
            System.out.println("ErrCode:" + e.getErrCode());
            System.out.println("ErrMsg:" + e.getErrMsg());
            System.out.println("RequestId:" + e.getRequestId());
        }
    }
}
```

**重要**

使用HTTPS协议访问OpenAPI时，SDK会默认开启校验SSL/TLS 证书有效性，若您代码环境没有证书环境，则会报错证书校验失败。 为保障生产环境通信安全，建议您保持开启，若在测试环境必须忽略证书校验，可以通过以下参数设置： Java 实时计算（流计算） 参考

```
HttpClientConfig clientConfig = HttpClientConfig.getDefault();
```

`//` 设置不校验服务端证书

```
clientConfig.setIgnoreSSLCerts(true)
```

#### Go版

本文为您介绍POP Go SDK调用的方式。

**前提条件**

目前专有云推荐使用CommonRequest进行调用，可以在Apsara Uni-manager运营控制台**产品** > **应用服** 务 > **开发者门户**，选择**API****集成** > **SDK****示例**查看推荐SDK版本以及示例代码。

**重要**

不建议直接从SDK中心下载SDK到专有云场景下使用，公有云的SDK不一定支持专有云的API，可能存在兼容性问题，请谨慎使用！

**背景信息**

当前支持RPC和ROA的方式调用API。

**CommonRequest调用示例**

RPC方式调用示例接口信息：产品（apigateway）、接口（DescribeApiGroups）、版本（2016-07- 14）。 示例代码如下： 实时计算（流计算） 参考

```java
package main import (
    "fmt"
    "github.com/aliyun/alibaba-cloud-sdk-go/sdk"
    "github.com/aliyun/alibaba-cloud-sdk-go/sdk/requests"
```

)

```
func main() {
    client, err := sdk.NewClientWithAccessKey("<your-RegionID>", "<AccessKey ID>", "<Acc
essKey Secret>")
    request := requests.NewCommonRequest()
    request.Method = "POST"
    request.Domain = "<ApigatewayEndpoint>"
    request.Version = "2016-07-14"
    request.ApiName = "DescribeApiGroups"
    request.Product = "apigateway"
```

`//` 当使用`sts ak`调用`rpc`接口时需要在参数中加上`SecurityToken`字段

```
    // request.QueryParams["SecurityToken"]="<your-SecurityToken>"
```

`//` 必填值，调用来源说明

```
    request.Headers["x-acs-caller-sdk-source"] = "ApiTestDemo"
```

`//` 非必填，企业版`V3.15.0`之前历史版本需要

```
    request.Headers["x-acs-regionid"] = "<your-RegionID>"
```

`//` 非必填，资源集`ID`

```
    request.Headers["x-acs-resourcegroupid"] = "<your-ResourceGroupID>"
```

`//` 必填，组织`ID`

```
    request.Headers["x-acs-organizationid"] = "<your-OrganizationID>"
```

`//` 非必填，修改&删除操作需要

```
    // request.Headers["x-acs-instanceid"] = "<your-InstanceID>"
    response, err := client.ProcessCommonRequest(request)
    if err != nil {
        panic(err)
    }
}
```

ROA调用示例接口信息：产品（CR）接口（GetNamespaceList）版本（2016-06-07）。 调用示例如下： 实时计算（流计算） 参考

```java
package main import (
 "fmt"
 "github.com/aliyun/alibaba-cloud-sdk-go/sdk"
 "github.com/aliyun/alibaba-cloud-sdk-go/sdk/requests"
 "os"
```

)

```
func main() {
    client, err := sdk.NewClientWithAccessKey("<your-regionid>", "<yourAccessKeyId>", "<
yourAccessSecret>")
 request := requests.NewCommonRequest()
 request.Method = "GET"
 request.Domain = "<crEndpoint>"
 request.Version = "2016-06-07"
 request.ApiName = "GetNamespaceList"
 request.Product = "cr"
 request.PathPattern = "/namespace"
```

`//` 当使用`sts ak`调用`ROA`接口时需要在`header`中加上`x-acs-security-token`字段

```
 // request.Headers["x-acs-security-token"] = "<your-SecurityToken>"
```

`//` 必填值，调用来源说明

```
 request.Headers["x-acs-caller-sdk-source"] = "ApiTestDemo"
```

`//` 非必填，企业版`V3.15.0`之前历史版本需要

```
    request.Headers["x-acs-regionid"] = "<your-RegionID>"
```

`//` 非必填，资源集`ID`

```
    request.Headers["x-acs-resourcegroupid"] = "<your-ResourceGroupID>"
```

`//` 必填，组织`ID`

```
    request.Headers["x-acs-organizationid"] = "<your-OrganizationID>"
```

`//` 非必填，修改&删除操作需要

```
 // request.Headers["x-acs-instanceid"] = "<your-InstanceID>"
 response, err := client.ProcessCommonRequest(request)
 if err != nil {
  panic(err)
 }
}
```

**设置代理**

当您在调用实例时，或许会需要设置代理，您可以通过以下两种方式设置代理。 通过环境变量设置。 环境变量HTTP_PROXY、HTTPS_PROXY或者NO_PROXY。 设置代码如下： 实时计算（流计算） 参考

```java
import (
    "os"
```

)

```
func main(){
 os.Setenv("HTTP_PROXY", "http://x.x.x.x:xxxx") // 设置 HTTP_PROXY 环境变量
 os.Setenv("HTTPS_PROXY", "https://x.x.x.x:xxxx") // 设置 HTTPS_PROXY 环境变量
}
```

通过客户端设置。 设置代码如下： `//` 客户端设置代理优先级比环境变量高

```
client.SetHttpProxy("http://x.x.x.x:xxxx") // 设置http代理 client.GetHttpProxy() // 获取http代理 client.SetHttpsProxy("https://x.x.x.x:xxxx") // 设置https代理 client.GetHttpsProxy() // 获取https代理 client.SetNoProxy("127.0.0.1,localhost") // 设置代理白名单 client.GetNoProxy() // 获取代理白名单
```

**SSL验证**

**摘要**

请求时验证SSL证书行为。 设置成 `true` ，禁用证书验证（这是不安全的，请设置证书！）。 设置成 `false` ，启用SSL证书验证，默认使用操作系统提供的CA证书。

**默认值**

默认值为 `false` 。

**设置**

**重要**

使用HTTPS协议访问OpenAPI时，SDK会默认开启校验SSL证书有效性，若您代码环境没有证书环境， 则会报错证书校验失败。为保障生产环境通信安全，建议您保持开启，若在测试环境必须忽略证书校验，可参考如下内容进行设置。 `//` 设置请求 `HTTPSInsecure`（只影响当前）

```
request.SetHTTPSInsecure(true) // 设置请求 HTTPSInsecure 为 true isInsecure := request.GetHTTPSInsecure() // 获取请求 HTTPSInsecure
```

当请求未设置时，客户端设置才能生效。 `//` 设置客户端 `HTTPSInsecure`（用于客户端发送的所有请求）。

```
client.SetHTTPSInsecure(true) // 设置客户端 HTTPSInsecure 为 true isInsecure := client.GetHTTPSInsecure() // 获取客户端 HTTPSInsecure
```

#### Python版

实时计算（流计算） 参考本文为您介绍POP Python SDK调用云产品API的方式。

**前提条件**

目前专有云推荐使用CommonRequest进行调用，可以在Apsara Uni-manager运营控制台**产品** > **应用服** 务 > **开发者门户**，选择**API****集成** > **SDK****示例**查看推荐SDK版本以及示例代码。

**重要**

不建议直接从SDK中心下载SDK到专有云场景下使用，公有云的SDK不一定支持专有云的API，可能存在兼容性问题，请谨慎使用！

**背景信息**

目前仅支持通过RPC方式调用API。

**CommonRequest调用示例**

调用示例接口信息：产品（ECS）、接口（DescribeInstances）、版本（2014-05-26）。 示例代码如下：

```java
from aliyunsdkcore.client import AcsClient import os from aliyunsdkcore.request import CommonRequest
```

# 创建`AcsClient`实例

```
client = AcsClient(
    "<AccessKey ID>",
    "<AccessKey Secret>",
    "<your-RegionID>",
```

`timeout=1000, #` 设置超时时间 `verify=False, #` 忽略证书或者`verify='<`证书位置`>'`

```
);
```

# 和`https`一起使用

```python
# client.set_verify(False)
# os.environ["HTTPS_PROXY"] = "http://127.0.0.1:8080"
# os.environ["HTTP_PROXY"] = "http://127.0.0.1:8080"
def describe_api_groups():
```

# 创建`request`，并设置参数

```
    request = CommonRequest()
```

# 当使用`sts ak`调用`rpc`接口时需要在参数中加上`SecurityToken`字段

```bash
    # params = {"PageSize":"10","PageNumber":"1","SecurityToken":"<your-SecurityToken>"}
;
    params = {"PageSize":"10","PageNumber":"1"};
    request.set_query_params(params)
    headers = {
```

# 必填值，调用来源说明

```
        "x-acs-caller-sdk-source":"ApiTestDemo",
```

# 非必填，企业版`V3.15.0`之前历史版本需要

```
        "x-acs-regionid":"<your-RegionID>",
```

# 非必填，资源集`ID`

```
        "x-acs-resourcegroupid":"<your-ResourceGroupID>",
```

# 必填，组织`ID`
实时计算（流计算） 参考

```
        "x-acs-organizationid":"<your-OrganizationID>"
```

# 非必填，修改&删除操作需要

```bash
        # "x-acs-instanceid":"<your-InstanceID>"
    }
    request.set_headers(headers)
    request.set_version("2016-07-14")
    request.set_action_name("DescribeApiGroups")
    request.set_endpoint("<ApigatewayEndpoint>")   //Endpoint请替换为真实地址
    request.set_product("apigateway")
    request.set_method("POST")
```

# 发起`API`请求并显示返回值

```
    response = client.do_action_with_exception(request)
if __name__ == '__main__':
    describe_api_groups()
```

**设置代理**

调用API时您或许需要通过环境变量设置HTTP_PROXY、HTTPS_PROXY。 示例代码如下：
# https的代理

```
os.environ["HTTPS_PROXY"] = "http://x.x.x.x:xxxx"
```

# http的代理

```
os.environ["HTTP_PROXY"] = "https://x.x.x.x:xxxx"
```

**HTTPS配置**

下面介绍使用HTTPS协议进行OpenAPI访问。

**使用HTTPS协议**

SDK默认使用HTTPS协议。

```
from aliyunsdkecs.request.v20140526.DescribeInstancesRequest import DescribeInstancesRequest from aliyunsdkcore.client import AcsClient client = AcsClient(
    region_id='<region_id>',  # 地域ID
```

)

```
request = DescribeInstancesRequest() request.set_protocol_type('https') # 使用https client.do_action_with_exception(request)
```

**忽略证书**

实时计算（流计算） 参考

|  | 重要使用HTTPS协议访问OpenAPI时，SDK会默认开启校验SSL/TLS证书有效性，若您代码环境没有证书环境，则会报错证书校验失败。 为保障生产环境通信安全，建议您保持开启，若在测试环境必须忽略证书校验，可以通过参数 verify 设置。 |  |
|---|---|---|

```
from aliyunsdkcore.client import AcsClient client = AcsClient(
    region_id='<region_id>',  # 地域ID
```

`verify=False #` 忽略对 `SSL` 证书的验证 )

**指定CA证书文件**

```
from aliyunsdkcore.client import AcsClient client = AcsClient(
    region_id='<region_id>',  # 地域ID
    verify='./cacert.pem'  # 证书路径
```

)

### AppManager API

#### 定义

##### 存算分离版 API 版本差异及使用说明

本文介绍 Flink 存算分离版当前提供的两套 API（v1 版与 v2 版）的版本差异、适用场景及使用建议，帮助开发者根据实际业务需要选择合适的 API 版本。

**版本说明**

Flink 存算分离版目前提供两套 API： 存算分离 v2 版 API：全新设计的 API 版本，功能更完善、扩展性更强，面向未来持续演进。 完整的 API 能力由 v1 版和 v2 版共同构成。部分功能在两个版本中重复实现，但接口定义、参数存在差异。

**使用建议**

**新开发业务用户（推荐使用 v2 版）**

全量可用 API 范围：v1 版 + v2 版。 当某个功能同时存在 v1 版和 v2 版实现时，请优先选用 v2 版。 v2 版是未来持续迭代和维护的版本，新特性将仅在 v2 版中提供。 建议从项目初期即采用 v2 版，以获得更好的长期支持与技术演进能力。

**历史业务用户（继续使用 v1）**

全量可用 API 范围：v1 版 + v2 版。 实时计算（流计算） 参考当某个功能同时存在 v1 版和 v2 版实现时，若当前业务已基于 v1 版开发并稳定运行，建议维持使用 v1 版，无需主动迁移。 v1 版将不再新增功能或进行非关键性维护，仅保留对现有业务的兼容性支持。

**后续演进计划**

v1 版将逐步停止维护，不再接收功能更新或优化。 v2 版将持续迭代，作为 Flink 存算分离版的主推 API 标准。

##### 存算分离v1版

###### ValidateSqlScript

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /pop/workspaces/[workspace]/sql/v1beta1/namespaces/[namespace]/sqlscripts:validate HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | String | Host | 是 | cn-wulan-env***-d01 | Region ID。 |
| namespac e | String | Path | 是 | flinkteam | 作业所在的项目空间名称。 |
| paramsJso n | String | Body | 否 | { "statement": "Drop TABLE `vvp`.`default`.`test`" } | 执行参数，sql脚本。 |
| workspace | String | Path | 是 | default | 作业所在的工作空间ID。您可以通过以下任意一种方式获取： 通过ListNamespaces获取。 在Flink全托管开发控制台工作空间详情中获取。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | String | CBC799F0-AS7S- 1D30-8A4F- 882ED4DD**** | 请求ID。 |

| link存算分离版开发参考 | 指南·OpenAPI |  | 实时计算（流计算） |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| data | String | { "validationResult": "VALIDATION RESU _ LT VALID DDL STA _ _ _ TEMENT" } | 详细信息。 |
| success | Boolean | true | 请求是否成功。 |

**示例**

请求示例

```json
POST /pop/workspaces/[workspace]/sql/v1beta1/namespaces/[namespace]/sqlscripts:validate HTTP/1.1 { "RegionId":"cn-wulan-env***-d01", "namespace":"flinkteam", "workspace":"default" }
```

正常返回示例 `JSON` 格式

```json
{
 "data":"{\"validationResult\":\"VALIDATION_RESULT_VALID_DDL_STATEMENT\"}",
 "requestId":"CBC799F0-AS7S-1D30-8A4F-882ED4DD****",
 "success":true
}
```

`XML` 格式

```xml
<data>{&quot;validationResult&quot;:&quot;VALIDATION_RESULT_VALID_DDL_STATEMENT&quot;} </data> <requestId>CBC799F0-AS7S-1D30-8A4F-882ED4DD****</requestId> <success>true</success>
```

###### UploadArtifactByOSSUrl

调用UpdateFolder，更新数据开发页面的文件夹。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /pop/workspaces/[workspace]/artifacts/v1/namespaces/[namespace]/artifacts:uploadByOSSUrl HTTP/1.1
```

实时计算（流计算） 参考

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | String | Host | 是 | cn-wulan-env***-d01 | Region名称。 |
| namespac e | String | Path | 是 | flinkteam | 作业所在的项目空间名称。 |
| workspace | String | Path | 是 | default | 作业所在的工作空间ID。您可以通过以下任意一种方式获取： 通过ListNamespaces获取。 在Flink全托管开发控制台工作空间详情中获取。 |
| paramsJso n | String | Body | 否 | {"filename":"", "ossUrl":""} | 执行参数，sql脚本。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | String | CBC799F0-AS7S- 1D30-8A4F- 882ED4DD**** | 请求ID。 |
| data | String | { "@type": "type.googleapis.c om/vvp.artifacts.v1 .CreateArtifactResp onse", "artifact": { "filename": "TopSpeedWindowi ng.jar", "content": "******", "namespace": "namespaces/flinkt eam", "uploader": "20678996188752 3346", "createTime": "2026-04- 30T03:06:24Z", "uri": "oss://flink- fullymanaged- apmd99ri0du673/a rtifacts/namespace s/flinkteam/TopSpe edWindowing.jar", "size": "11957" } } | 详细信息。 |
| success | Boolean | true | 请求是否成功。 |

**示例**

实时计算（流计算） 参考请求示例

```json
POST /pop/workspaces/[workspace]/artifacts/v1/namespaces/[namespace]/artifacts:uploadByOSSUrl HTTP/1.1 { "RegionId":"cn-wulan-env***-d01", "namespace":"flinkteam", "workspace":"default" }
```

正常返回示例 `JSON` 格式

```json
{
 "data":"
{\"@type\":\"type.googleapis.com/vvp.artifacts.v1.CreateArtifactResponse\",\"artifact\": {\"filename\":\"TopSpeedWindowing.jar\",\"content\":\"******\",\"namespace\":\"namespaces/ inkteam\",\"uploader\":\"206789961887523346\",\"createTime\":\"2026-04- 30T03:06:24Z\",\"uri\":\"oss://flink-fullymanagedapmd99ri0du673/artifacts/namespaces/flinkteam/TopSpeedWindowing.jar\",\"size\":\"11957\"}
 "requestId":"CBC799F0-AS7S-1D30-8A4F-882ED4DD****",
 "success":true
}
```

`XML` 格式

```xml
<data> {&quot;@type&quot;:&quot;type.googleapis.com/vvp.artifacts.v1.CreateArtifactResponse&quot; quot;artifact&quot;: {&quot;filename&quot;:&quot;TopSpeedWindowing.jar&quot;,&quot;content&quot;:&quot;******&q t;,&quot;namespace&quot;:&quot;namespaces/flinkteam&quot;,&quot;uploader&quot;:&quot;20678 61887523346&quot;,&quot;createTime&quot;:&quot;2026-04- 30T03:06:24Z&quot;,&quot;uri&quot;:&quot;oss://flink-fullymanagedapmd99ri0du673/artifacts/namespaces/flinkteam/TopSpeedWindowing.jar&quot;,&quot;size&quot; quot;11957&quot;}}</data> <requestId>CBC799F0-AS7S-1D30-8A4F-882ED4DD****</requestId> <success>true</success>
```

###### UpdateUdfArtifact

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

实时计算（流计算） 参考

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | String | Host | 是 | cn-wulan-env***-d01 | Region ID。 |
| paramsJso n | String | Body | 否 | { "jarUrl": "http://flink- resource.oss-cn-wulan- env**-d01- a.intra.env**.shuguang.c om/udx/metric- transform-2.2.7- shaded.jar" } | 变更参数。 |
| workspace | String | Path | 是 | default | 作业所在的工作空间ID。您可以通过以下任意一种方式获取： 通过ListNamespaces获取。 在Flink全托管开发控制台工作空间详情中获取。 |
| namespac e | String | Path | 是 | flinkteam | 作业所在的项目空间名称。 |
| udfArtifact Name | String | Path | 是 | metric-transform-227- shaded | Udf名称。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
|  |  | { "missingClasses": [], "@type": "type.googleapis.c om/vvp.sql.v1beta 1.UpdateUdfArtifac tResponse", "collidingClasses": [], "udfArtifact": { "dependencyJarUris ": [], "udfClasses": [ { "functionNames": [], "udfArtifactName": "namespaces/flinkt eam/udfartifacts/m etric-transform- 227-shaded", "className": "com.alibaba.blink. udtf.TimestampPro be", "classType": "UDF TYPE SCALA _ _ R" }, { "functionNames": [], "udfArtifactName": "namespaces/flinkt eam/udfartifacts/m etric-transform- |  |

实时计算（流计算） 参考

| 参数名称 | 类型 | 227-shaded", 示例 "className": | 说明 |
|---|---|---|---|
| data | String | "com.alibaba.blink. udtf.TransformUdtf ", "classType": "UDF TYPE TABLE" _ _ } ], "artifactType": "ARTIFACT TYPE JA _ _ VA", "createTime": "2024-03- 08T08:13:54Z", "uploader": "22347490986944 5380", | 详细信息。 |
|  |  | "jarUpdateTime": "2024-03- 08T09:04:22.53111 3Z", "name": "namespaces/flinkt eam/udfartifacts/m etric-transform- 227-shaded", "namespace": "namespaces/flinkt eam", "jarUrl": "hdfs:///vvp/data/sq l- artifacts/namespac es/flinkteam/udfs/ metric-transform- 227-shaded/2024- 03-08T08-13- 54.732313Z/metric -transform-2.2.7- shaded.jar", "updateTime": "2024-03- 08T09:04:22.53111 3Z" } } |  |
| requestId | String | CBC799F0-AS7S- 1D30-8A4F- 882ED4DD**** | 请求ID。 |
| success | Boolean | true | 请求是否成功。 |

**示例**

请求示例

```json
PUT /pop/workspaces/[workspace]/sql/v1beta1/namespaces/[namespace]/udfartifacts/[udfArtifactNa ] HTTP/1.1 { "RegionId":"cn-wulan-env***-d01", "workspace":"default", "namespace":"flinkteam", "udfArtifactName":"metric-transform-227-shaded" }
```

正常返回示例实时计算（流计算） 参考 `JSON` 格式

```json
{
 "data":"{\"missingClasses\":
[],\"@type\":\"type.googleapis.com/vvp.sql.v1beta1.UpdateUdfArtifactResponse\",\"colliding asses\":[],\"udfArtifact\":{\"dependencyJarUris\":[],\"udfClasses\": [{\"functionNames\":[],\"udfArtifactName\":\"namespaces/flinkteam/udfartifacts/metric-t ransform-227shaded\",\"className\":\"com.alibaba.blink.udtf.TimestampProbe\",\"classType\":\"UDF_TYPE_ ALAR\"},{\"functionNames\": [],\"udfArtifactName\":\"namespaces/flinkteam/udfartifacts/metric-transform-227shaded\",\"className\":\"com.alibaba.blink.udtf.TransformUdtf\",\"classType\":\"UDF_TYPE_T LE\"}],\"artifactType\":\"ARTIFACT_TYPE_JAVA\",\"createTime\":\"2024-03- 08T08:13:54Z\",\"uploader\":\"223474909869445380\",\"jarUpdateTime\":\"2024-03- 08T09:04:22.531113Z\",\"name\":\"namespaces/flinkteam/udfartifacts/metric-transform- 227-shaded\",\"namespace\":\"namespaces/flinkteam\",\"jarUrl\":\"hdfs:///vvp/data/sql-a rtifacts/namespaces/flinkteam/udfs/metric-transform-227-shaded/2024-03-08T08-13- 54.732313Z/metric-transform-2.2.7-shaded.jar\",\"updateTime\":\"2024-03- 08T09:04:22.531113Z\"}}",
 "requestId":"CBC799F0-AS7S-1D30-8A4F-882ED4DD****",
 "success":true
}
```

`XML` 格式

```xml
<data>{&quot;missingClasses&quot;: [],&quot;@type&quot;:&quot;type.googleapis.com/vvp.sql.v1beta1.UpdateUdfArtifactResponse&q t;,&quot;collidingClasses&quot;:[],&quot;udfArtifact&quot;: {&quot;dependencyJarUris&quot;:[],&quot;udfClasses&quot;:[{&quot;functionNames&quot;: [],&quot;udfArtifactName&quot;:&quot;namespaces/flinkteam/udfartifacts/metrictransform-227shaded&quot;,&quot;className&quot;:&quot;com.alibaba.blink.udtf.TimestampProbe&quot;,&quot lassType&quot;:&quot;UDF_TYPE_SCALAR&quot;},{&quot;functionNames&quot;: [],&quot;udfArtifactName&quot;:&quot;namespaces/flinkteam/udfartifacts/metrictransform-227shaded&quot;,&quot;className&quot;:&quot;com.alibaba.blink.udtf.TransformUdtf&quot;,&quot; assType&quot;:&quot;UDF_TYPE_TABLE&quot;}],&quot;artifactType&quot;:&quot;ARTIFACT_TYPE_JA &quot;,&quot;createTime&quot;:&quot;2024-03- 08T08:13:54Z&quot;,&quot;uploader&quot;:&quot;223474909869445380&quot;,&quot;jarUpdateTime uot;:&quot;2024-03- 08T09:04:22.531113Z&quot;,&quot;name&quot;:&quot;namespaces/flinkteam/udfartifacts/metrictransform-227shaded&quot;,&quot;namespace&quot;:&quot;namespaces/flinkteam&quot;,&quot;jarUrl&quot;:&qu ;hdfs:///vvp/data/sql-artifacts/namespaces/flinkteam/udfs/metric-transform-227shaded/2024-03-08T08-13-54.732313Z/metric-transform-2.2.7shaded.jar&quot;,&quot;updateTime&quot;:&quot;2024-03-08T09:04:22.531113Z&quot;}} </data> <requestId>CBC799F0-AS7S-1D30-8A4F-882ED4DD****</requestId> <success>true</success>
```

###### UpdateMember

实时计算（流计算） 参考

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
PUT /pop/workspaces/[workspace]/members/v1/namespaces/[namespace] HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| paramsJso n | String | Body | 否 | { "role": "viewer", "member": "242425410145292209" } | 用户业务权限变更参数。 |
| workspace | String | Path | 是 | default | 作业所在的工作空间ID。您可以通过以下任意一种方式获取： 通过ListNamespaces获取。 在Flink全托管开发控制台工作空间详情中获取。 |
| namespac e | String | Path | 是 | flinkteam | 作业所在的项目空间名称。 |
| RegionId | String | Host | 是 | cn-wulan-env***-d01 | Region名称。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| success | Boolean | true | 请求是否成功。 |
| requestId | String | 29F07013-6BE2- 4F99-90B6- 9E27BF2A26C4 | 请求ID。 |
| data | String | { "@type": "type.googleapis.c om/vvp.members.v 1.UpdateMemberR esponse", "member": { "role": "owner", "member": "user:2424254101 45292209" } } | 变更后用户的业务权限详细信息。 |

**示例**

请求示例实时计算（流计算） 参考

```json
PUT /pop/workspaces/[workspace]/members/v1/namespaces/[namespace] HTTP/1.1 { "workspace":"default", "namespace":"flinkteam", "RegionId":"cn-wulan-env***-d01" }
```

正常返回示例 `JSON` 格式

```json
{
 "data":"
{\"@type\":\"type.googleapis.com/vvp.members.v1.UpdateMemberResponse\",\"member\": {\"role\":\"owner\",\"member\":\"user:242425410145292209\"}}",
 "success":true,
 "requestId":"29F07013-6BE2-4F99-90B6-9E27BF2A26C4"
}
```

`XML` 格式

```xml
<data> {&quot;@type&quot;:&quot;type.googleapis.com/vvp.members.v1.UpdateMemberResponse&quot;,&qu ;member&quot;: {&quot;role&quot;:&quot;owner&quot;,&quot;member&quot;:&quot;user:242425410145292209&quot; </data> <success>true</success> <requestId>29F07013-6BE2-4F99-90B6-9E27BF2A26C4</requestId>
```

###### UpdateFormat

调用UpdateFormat，用于Format变更，包含是否可为source、sink、format参数、依赖的jar包等。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
PUT /pop/workspaces/[workspace]/sql/v1beta1/namespaces/[namespace]/formats/[name] HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | String | Host | 是 | cn-wulan-env***-d01 | Region ID。 |

实时计算（流计算） 参考

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| workspace | String | Path | 是 | default | 作业所在的工作空间ID。您可以通过以下任意一种方式获取： 通过ListNamespaces获取。 在Flink全托管开发控制台工作空间详情中获取。 |
| name | String | Path | 是 | customized-csv | 待变更的format名称。 |
| paramsJso n | String | Body | 否 | { "name": "namespaces/flinkteam/f ormats/customized-csv", "type": "customized- csv", "source": true, "sink": false, "properties": [ { "key": "format.column- delimiter", "required": false, "defaultValue": ",", "description": "" } ], "dependencies": [ "hdfs:///tmp/myformats/c ustomized-csv-demo- 1.0-SNAPSHOT.jar" ] } | format变更参数。 |
| namespac e | String | Path | 是 | flinkteam | 作业所在的项目空间名称。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| success | Boolean | true | 请求是否成功。 |

实时计算（流计算） 参考

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| data | String | { "affectedTables": [], "@type": "type.googleapis.c om/vvp.sql.v1beta 1.UpdateFormatRe sponse", "format": { "sink": false, "name": "namespaces/flinkt eam/formats/custo mized-csv", "source": true, "type": "customized-csv", "properties": [ { "defaultValue": ",", "description": "", "definesFormat": false, "key": "format.column- delimiter", "required": false } ], "packaged": false, "dependencies": [ "hdfs:///tmp/myfor mats/customized- csv-demo-1.0- SNAPSHOT.jar" ] } } | format变更后详细信息。 |
| requestId | String | CBC799F0-AS7S- 1D30-8A4F- 882ED4DD**** | 请求ID。 |

**示例**

请求示例

```json
PUT /pop/workspaces/[workspace]/sql/v1beta1/namespaces/[namespace]/formats/[name] HTTP/1.1 { "RegionId":"cn-wulan-env***-d01", "workspace":"default", "name":"customized-csv", "namespace":"flinkteam" }
```

正常返回示例 `JSON` 格式实时计算（流计算） 参考

```json
{
 "data":"{\"affectedTables\":
[],\"@type\":\"type.googleapis.com/vvp.sql.v1beta1.UpdateFormatResponse\",\"format\": {\"sink\":false,\"name\":\"namespaces/flinkteam/formats/customizedcsv\",\"source\":true,\"type\":\"customized-csv\",\"properties\": [{\"defaultValue\":\",\",\"description\":\"\",\"definesFormat\":false,\"key\":\"format.col n-delimiter\",\"required\":false}],\"packaged\":false,\"dependencies\": [\"hdfs:///tmp/myformats/customized-csv-demo-1.0-SNAPSHOT.jar\"]}}",
 "success":true,
 "requestId":"CBC799F0-AS7S-1D30-8A4F-882ED4DD****"
}
```

`XML` 格式

```xml
<data>{&quot;affectedTables&quot;: [],&quot;@type&quot;:&quot;type.googleapis.com/vvp.sql.v1beta1.UpdateFormatResponse&quot;, uot;format&quot;: {&quot;sink&quot;:false,&quot;name&quot;:&quot;namespaces/flinkteam/formats/customizedcsv&quot;,&quot;source&quot;:true,&quot;type&quot;:&quot;customizedcsv&quot;,&quot;properties&quot;: [{&quot;defaultValue&quot;:&quot;,&quot;,&quot;description&quot;:&quot;&quot;,&quot;define ormat&quot;:false,&quot;key&quot;:&quot;format.columndelimiter&quot;,&quot;required&quot;:false}],&quot;packaged&quot;:false,&quot;dependencies uot;:[&quot;hdfs:///tmp/myformats/customized-csv-demo-1.0-SNAPSHOT.jar&quot;]}}</data> <success>true</success> <requestId>CBC799F0-AS7S-1D30-8A4F-882ED4DD****</requestId>
```

###### UpdateDeploymentDesiredState

调用UpdateDeploymentDesiredState，更新实时计算中的部署目标状态。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
PUT /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/deployments/[deploymentId]/state HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | String | Host | 是 | cn-wulan-env***-d01 | Region ID。 |
| namespac e | String | Path | 是 | flinkteam | 作业所在的项目空间名称。 |
| deployme ntId | String | Path | 是 | d0b3abf0-4bfe-46b1- a324-5b7def580c00 | 作业ID。 |

| 实时计算（流计 | 算） |  |  | Flink | 存算分离版开发指南·OpenAP 参考 |
|---|---|---|---|---|---|
| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
| paramsJso n | String | Body | 否 | {"state": "CANCELLED"} | 执行参数，sql脚本。 |
| workspace | String | Path | 是 | default | 作业所在的工作空间ID。您可以通过以下任意一种方式获取： 通过ListNamespaces获取。 在Flink全托管开发控制台工作空间详情中获取。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | String | CBC799F0-AS7S- 1D30-8A4F- 882ED4DD**** | 请求ID。 |
|  |  | { "metadata": { "createdAt": "2026- 04-24T03:47:01Z", "workspace": "9cuwr9g7y1hl19", "modifiedAt": "2026-04- 24T03:58:25.52528 4Z", "resourceVersion": 172, "name": "sqlJob", "namespace": "flinkteam", "annotations": { "creator": "23540697665705 7054", "resource- plan.has.migrated" : "true", "storage.disaster.r po": "1800", "deployment.sourc e-type": "EDITOR", "deployment.has.d eployed": "false", "deployment.paren t.id": "", "modifier": "23540697665705 7054", "creatorName": "flinkadmin", "plan.uri": "deployment/a3d8 8b2a-e076-4491- 86f2- 5a81ea4c7300/res ourcePlan.json", "priority": "5", "priority.class.nam |  |

实时计算（流计算） 参考

| 参数名称 | 类型 | e": "flink-p5", 示例 "migration.display. | 说明 |
|---|---|---|---|
|  |  | enabled": "false", "deployment.exec- plan.uri.valid": "true", "com.dataartisans. appmanager.contr oller.deployment.s pec.version": "13", "default.resource- setting.has.migrate d": "true", "deployment.refere nced.deployment.d raft.history.version ": "1", "deployment.exec- plan.uri": "oss://flink- fullymanaged- 9cuwr9g7y1hl19/fli nk- jobs/namespaces/fl inkteam/jobs/c944e 978-5cb9-4879- |  |
| data | String | 8312- c0872ee50182/exe cPlan.json", "deployment.refere nced.deployment.d raft.id": "cee26b6e- d03b-4a03-a628- a6fe665c525e", "resources.from.job .has.migrated": "true", "taker": " \| vvp-0", "modifierName": "flinkadmin", "deployment.refere nced.deployment.d raft.history.id": "561a6a3d-7858- 4056-acfb- ad0cdec09e55" }, "id": "a3d88b2a- e076-4491-86f2- 5a81ea4c7300", "labels": {} }, "apiVersion": "v1", "kind": "Deployment", "spec": { "template": { "metadata": { "annotations": { "flink.resource.type ": "fine-grained", "job.resource.total. memory.byte": "3724541952", "job.resource.total. cpu": "0.7", "native.kubernetes. mode": "true", "flink.queryable- | 详细信息。 |

实时计算（流计算） 参考

| 参数名称 | 类型 | state.enabled": 示例 "false", | 说明 |
|---|---|---|---|
|  |  | "flink.security.ssl.e nabled": "false" } }, "spec": { "artifact": { "flinkImageTag": "1.17.0-vvr-8.0.7- manifest-251107", "kind": "SQLSCRIPT", "sqlScript": "CREATE TEMPORARY TABLE `datahub table` _ (strname VARCHAR) with ( 'connector' = 'datagen' ); CREATE TEMPORARY TABLE `kafka table` _ (strname VARCHAR, lens BIGINT) with ( 'connector' = 'print' ); INSERT INTO kafka table _ SELECT SUBSTRING (strname, 0, 10) AS strname, CAST (CHAR LENGTH _ (strname) AS BIGINT) AS lens FROM datahub table;", _ "imageUserDefined ": false, "flinkImageRegistry ": "cn-wulan- env35-d01- reg.docker.intra.en v35.shuguang.com :80/ververica- paas", "versionName": "vvr-8.0.7-flink- 1.17", "flinkImageReposit ory": "vvr", "flinkVersion": "1.17" }, "parallelism": 1, "batchMode": false, "resources": { "jobmanager": { "memory": "2Gi", "cpu": 0.5 }, "taskmanager": { "memory": "3Gi", "cpu": 1.0 } }, |  |

实时计算（流计算） 参考

| 参数名称 | 类型 | "logging": { 示例 "log4jLoggers": { | 说明 |
|---|---|---|---|
|  |  | "": "INFO" }, "logReservePolicy": { "expirationDays": 7, "openHistory": true }, "loggingProfile": "default" }, "flinkConfiguration" : {} } }, "restoreStrategy": { "kind": "FROM SAVEPOINT _ ", "allowNonRestored State": false, "savepointId": "5cea0d88-303d- 44e5-a96e- 47f7217723d7" }, "state": "CANCELLED", "upgradeStrategy": { "kind": "NONE" }, "maxSavepointCre ationAttempts": 4, "maxJobCreationAt tempts": 1, "deploymentTarget Id": "a89ff052- 38c6-4fd3-9b91- e9c53f8ee019" }, "status": { "startTime": 1777002980004, "state": "RUNNING", "endTime": 0 } } |  |
| success | Boolean | true | 请求是否成功。 |

**示例**

请求示例

```json
PUT /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/deployments/[deploymentId]/state HTTP/1.1 { "RegionId":"cn-wulan-env***-d01", "namespace":"flinkteam", "deploymentId":"d0b3abf0-4bfe-46b1-a324-5b7def580c00", "workspace":"default" }
```

正常返回示例 `JSON` 格式实时计算（流计算） 参考

```json
{
 "data":"{\"metadata\":{\"createdAt\":\"2026-04-
24T03:47:01Z\",\"workspace\":\"9cuwr9g7y1hl19\",\"modifiedAt\":\"2026-04- 24T03:58:25.525284Z\",\"resourceVersion\":172,\"name\":\"sqlJob\",\"namespace\":\"flinktea ",\"annotations\":{\"creator\":\"235406976657057054\",\"resourceplan.has.migrated\":\"true\",\"storage.disaster.rpo\":\"1800\",\"deployment.sourcetype\":\"EDITOR\",\"deployment.has.deployed\":\"false\",\"deployment.parent.id\":\"\",\"mo fier\":\"235406976657057054\",\"creatorName\":\"flinkadmin\",\"plan.uri\":\"deployment/a3d b2a-e076-4491-86f2- 5a81ea4c7300/resourcePlan.json\",\"priority\":\"5\",\"priority.class.name\":\"flinkp5\",\"migration.display.enabled\":\"false\",\"deployment.execplan.uri.valid\":\"true\",\"com.dataartisans.appmanager.controller.deployment.spec.version :\"13\",\"default.resourcesetting.has.migrated\":\"true\",\"deployment.referenced.deployment.draft.history.version\" "1\",\"deployment.exec-plan.uri\":\"oss://flink-fullymanaged-9cuwr9g7y1hl19/flinkjobs/namespaces/flinkteam/jobs/c944e978-5cb9-4879-8312c0872ee50182/execPlan.json\",\"deployment.referenced.deployment.draft.id\":\"cee26b6e-d 03b-4a03-a628-a6fe665c525e\",\"resources.from.job.has.migrated\":\"true\",\"taker\":\"
| vvp-
0\",\"modifierName\":\"flinkadmin\",\"deployment.referenced.deployment.draft.history.id\" 561a6a3d-7858-4056-acfb-ad0cdec09e55\"},\"id\":\"a3d88b2a-e076-4491-86f2- 5a81ea4c7300\",\"labels\":{}},\"apiVersion\":\"v1\",\"kind\":\"Deployment\",\"spec\": {\"template\":{\"metadata\":{\"annotations\":{\"flink.resource.type\":\"finegrained\",\"job.resource.total.memory.byte\":\"3724541952\",\"job.resource.total.cpu\":\"0 \",\"native.kubernetes.mode\":\"true\",\"flink.queryablestate.enabled\":\"false\",\"flink.security.ssl.enabled\":\"false\"}},\"spec\": {\"artifact\":{\"flinkImageTag\":\"1.17.0-vvr-8.0.7-manifest- 251107\",\"kind\":\"SQLSCRIPT\",\"sqlScript\":\"CREATE TEMPORARY TABLE `datahub_table` (strname VARCHAR)\with (\ 'connector' = 'datagen'\);\\CREATE TEMPORARY TABLE `kafka_t able` (strname VARCHAR, lens BIGINT)\with (\ 'connector' = 'print'\);\\INSERT INTO kafka_table\SELECT SUBSTRING (strname, 0, 10) AS strname, CAST (CHAR_LENGTH (strname) A S BIGINT) AS lens\FROM\ datahub_table;\",\"imageUserDefined\":false,\"flinkImageRegistry\":\"cn-wulan-env35d01-reg.docker.intra.env35.shuguang.com:80/ververica-paas\",\"versionName\":\"vvr- 8.0.7-flink- 1.17\",\"flinkImageRepository\":\"vvr\",\"flinkVersion\":\"1.17\"},\"parallelism\":1,\"bat Mode\":false,\"resources\":{\"jobmanager\": {\"memory\":\"2Gi\",\"cpu\":0.5},\"taskmanager\": {\"memory\":\"3Gi\",\"cpu\":1.0}},\"logging\":{\"log4jLoggers\": {\"\":\"INFO\"},\"logReservePolicy\": {\"expirationDays\":7,\"openHistory\":true},\"loggingProfile\":\"default\"},\"flinkConfigu tion\":{}}},\"restoreStrategy\": {\"kind\":\"FROM_SAVEPOINT\",\"allowNonRestoredState\":false,\"savepointId\":\"5cea0d88- 303d-44e5-a96e-47f7217723d7\"},\"state\":\"CANCELLED\",\"upgradeStrategy\": {\"kind\":\"NONE\"},\"maxSavepointCreationAttempts\":4,\"maxJobCreationAttempts\":1,\"depl mentTargetId\":\"a89ff052-38c6-4fd3-9b91-e9c53f8ee019\"},\"status\": {\"startTime\":1777002980004,\"state\":\"RUNNING\",\"endTime\":0}}",
 "requestId":"CBC799F0-AS7S-1D30-8A4F-882ED4DD****",
 "success":true
}
```

`XML` 格式

```xml
<data>{&quot;metadata&quot;:{&quot;createdAt&quot;:&quot;2026-04-
```

实时计算（流计算） 参考

|  | <data>{&quot;metadata&quot;:{&quot;createdAt&quot;:&quot;2026 04 24T03:47:01Z&quot;,&quot;workspace&quot;:&quot;9cuwr9g7y1hl19&quot;,&quot;modifiedAt&quot quot;2026-04- 24T03:58:25.525284Z&quot;,&quot;resourceVersion&quot;:172,&quot;name&quot;:&quot;sqlJob&q ;,&quot;namespace&quot;:&quot;flinkteam&quot;,&quot;annotations&quot;: {&quot;creator&quot;:&quot;235406976657057054&quot;,&quot;resource- plan.has.migrated&quot;:&quot;true&quot;,&quot;storage.disaster.rpo&quot;:&quot;1800&quot quot;deployment.source- type&quot;:&quot;EDITOR&quot;,&quot;deployment.has.deployed&quot;:&quot;false&quot;,&quot ployment.parent.id&quot;:&quot;&quot;,&quot;modifier&quot;:&quot;235406976657057054&quot; uot;creatorName&quot;:&quot;flinkadmin&quot;,&quot;plan.uri&quot;:&quot;deployment/a3d88b e076-4491-86f2- 5a81ea4c7300/resourcePlan.json&quot;,&quot;priority&quot;:&quot;5&quot;,&quot;priority.cl .name&quot;:&quot;flink- p5&quot;,&quot;migration.display.enabled&quot;:&quot;false&quot;,&quot;deployment.exec- plan.uri.valid&quot;:&quot;true&quot;,&quot;com.dataartisans.appmanager.controller.deploy t.spec.version&quot;:&quot;13&quot;,&quot;default.resource- setting.has.migrated&quot;:&quot;true&quot;,&quot;deployment.referenced.deployment.draft. tory.version&quot;:&quot;1&quot;,&quot;deployment.exec- plan.uri&quot;:&quot;oss://flink-fullymanaged-9cuwr9g7y1hl19/flink- jobs/namespaces/flinkteam/jobs/c944e978-5cb9-4879-8312- c0872ee50182/execPlan.json&quot;,&quot;deployment.referenced.deployment.draft.id&quot;:&q ;cee26b6e-d03b-4a03-a628- a6fe665c525e&quot;,&quot;resources.from.job.has.migrated&quot;:&quot;true&quot;,&quot;tak quot;:&quot; \| vvp- 0&quot;,&quot;modifierName&quot;:&quot;flinkadmin&quot;,&quot;deployment.referenced.deplo nt.draft.history.id&quot;:&quot;561a6a3d-7858-4056-acfb- ad0cdec09e55&quot;},&quot;id&quot;:&quot;a3d88b2a-e076-4491-86f2- 5a81ea4c7300&quot;,&quot;labels&quot;: {}},&quot;apiVersion&quot;:&quot;v1&quot;,&quot;kind&quot;:&quot;Deployment&quot;,&quot;s &quot;:{&quot;template&quot;:{&quot;metadata&quot;:{&quot;annotations&quot;: {&quot;flink.resource.type&quot;:&quot;fine- grained&quot;,&quot;job.resource.total.memory.byte&quot;:&quot;3724541952&quot;,&quot;job source.total.cpu&quot;:&quot;0.7&quot;,&quot;native.kubernetes.mode&quot;:&quot;true&quot quot;flink.queryable- state.enabled&quot;:&quot;false&quot;,&quot;flink.security.ssl.enabled&quot;:&quot;false& t;}},&quot;spec&quot;:{&quot;artifact&quot;:{&quot;flinkImageTag&quot;:&quot;1.17.0-vvr -8.0.7-manifest- 251107&quot;,&quot;kind&quot;:&quot;SQLSCRIPT&quot;,&quot;sqlScript&quot;:&quot;CREATE TEMPORARY TABLE `datahub table` (strname VARCHAR)with ( &#x27;connector&#x27; = _ &#x27;datagen&#x27;);CREATE TEMPORARY TABLE `kafka table` (strname VARCHAR, lens _ BIGINT)with ( &#x27;connector&#x27; = &#x27;print&#x27;);INSERT INTO kafka tableSELECT SUBSTRING (strname, 0, 10) AS strname, CAST (CHAR LENGTH (strname) AS _ _ BIGINT) AS lensFROM datahub table;&quot;,&quot;imageUserDefined&quot;:false,&quot;flinkImageRegistry&quot;:&q _ ;cn-wulan-env35-d01-reg.docker.intra.env35.shuguang.com:80/ververica- paas&quot;,&quot;versionName&quot;:&quot;vvr-8.0.7-flink- 1.17&quot;,&quot;flinkImageRepository&quot;:&quot;vvr&quot;,&quot;flinkVersion&quot;:&quo .17&quot;},&quot;parallelism&quot;:1,&quot;batchMode&quot;:false,&quot;resources&quot;: {&quot;jobmanager&quot;: {&quot;memory&quot;:&quot;2Gi&quot;,&quot;cpu&quot;:0.5},&quot;taskmanager&quot;: {&quot;memory&quot;:&quot;3Gi&quot;,&quot;cpu&quot;:1.0}},&quot;logging&quot;: {&quot;log4jLoggers&quot;:{&quot;&quot;:&quot;INFO&quot;},&quot;logReservePolicy&quot;: {&quot;expirationDays&quot;:7,&quot;openHistory&quot;:true},&quot;loggingProfile&quot;:&q ;default&quot;},&quot;flinkConfiguration&quot;:{}}},&quot;restoreStrategy&quot;: | ; u ; ; , 2 a m h u e y p ; q u t u |
|---|---|---|

实时计算（流计算） 参考

```xml
{&quot;kind&quot;:&quot;FROM_SAVEPOINT&quot;,&quot;allowNonRestoredState&quot;:false,&quot avepointId&quot;:&quot;5cea0d88-303d-44e5-a96e- 47f7217723d7&quot;},&quot;state&quot;:&quot;CANCELLED&quot;,&quot;upgradeStrategy&quot;: {&quot;kind&quot;:&quot;NONE&quot;},&quot;maxSavepointCreationAttempts&quot;:4,&quot;maxJo reationAttempts&quot;:1,&quot;deploymentTargetId&quot;:&quot;a89ff052-38c6-4fd3-9b91e9c53f8ee019&quot;},&quot;status&quot;: {&quot;startTime&quot;:1777002980004,&quot;state&quot;:&quot;RUNNING&quot;,&quot;endTime&q t;:0}}</data> <requestId>CBC799F0-AS7S-1D30-8A4F-882ED4DD****</requestId> <success>true</success>
```

###### UpdateDeployment

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
PUT /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/deployments/[deploymentId]/patch HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | String | Host | 是 | cn-wulan-env***-d01 | Region ID。 |
| namespac e | String | Path | 是 | flinkteam | 作业所在的项目空间名称。 |
| deployme ntId | String | Path | 是 | d0b3abf0-4bfe-46b1- a324-5b7def580c00 | 作业ID。 |
|  |  |  |  | { "metadata": { "id": "7325ac07-e466-4c1b- b598-311c6f2c103b", "name": "sqlJob", "namespace": "flinkteam", "workspace": "9cuwr9g7y1hl19", "createdAt": "2026-04- 28T01:59:31Z", "modifiedAt": "2026-04- 28T02:07:18Z", "labels": {}, "annotations": { "creator": "235406976657057054" , "resource- plan.has.migrated": "true", "storage.disaster.rpo": "1800", |  |

实时计算（流计算） 参考

| 参数名称 | 类型 | 位置 | 是否必选 | "deployment.has.deploy 示例 ed": "false", | 说明 |
|---|---|---|---|---|---|
|  |  |  |  | "deployment.source- type": "EDITOR", "deployment.parent.id": |  |
| paramsJso n | String | Body | 否 | "", "modifier": "235406976657057054" , "creatorName": "flinkadmin", "plan.uri": "deployment/7325ac07- e466-4c1b-b598- 311c6f2c103b/resourceP lan.json", "priority": "5", "priority.class.name": "flink-p5", "migration.display.enabl ed": "false", "com.dataartisans.appm anager.controller.deploy ment.spec.version": "5", "default.resource- setting.has.migrated": "true", "deployment.referenced. deployment.draft.history .version": "3", "deployment.referenced. deployment.draft.id": "cee26b6e-d03b-4a03- a628-a6fe665c525e", "modifierName": "flinkadmin", "taker": " \| vvp-0", "deployment.referenced. deployment.draft.history .id": "5bfca9e9-a50d- 483b-bad5- 1e1d5315acaf", "one- time.retry": "false", "stop-with- savepoint.enabled": false }, "resourceVersion": 9 }, "spec": { "state": "SUSPENDED", "upgradeStrategy": { "kind": "NONE" }, "restoreStrategy": { "kind": "LATEST STATE" _ }, "deploymentTargetId": "a89ff052-38c6-4fd3- 9b91-e9c53f8ee019", "maxSavepointCreationA ttempts": 4, "maxJobCreationAttempt s": 1, "template": { "metadata": { "annotations": { "flink.resource.type": "fine-grained", "job.resource.total.mem ory.byte": "0", "job.resource.total.cpu": "0.0", "native.kubernetes.mod e": "true", | 执行参数，sql脚本。 |

实时计算（流计算） 参考

| 参数名称 | 类型 | 位置 | 是否必选 | "flink.queryable- 示例 state.enabled": "false", | 说明 |
|---|---|---|---|---|---|
|  |  |  |  | "flink.security.ssl.enable d": "false" } }, "spec": { "artifact": { "kind": "SQLSCRIPT", "versionName": "vvr- 8.0.7-flink-1.17", "imageUserDefined": false, "sqlScript": "CREATE TEMPORARY TABLE `datahub table` _ (strname VARCHAR) with ( 'connector' = 'datagen' ); CREATE TEMPORARY TABLE `kafka table` _ (strname VARCHAR, lens BIGINT) with ( 'connector' = 'print' ); INSERT INTO kafka table _ SELECT SUBSTRING (strname, 0, 10) AS strname, CAST (CHAR LENGTH _ (strname) AS BIGINT) AS lens FROM datahub table;", _ "flinkVersion": "1.17", "flinkImageTag": "1.17.0-vvr-8.0.7- manifest-251107", "flinkImageRegistry": "cn-wulan-env**-d01- reg.docker.intra.env**.s huguang.com:80/ververi ca-paas", "flinkImageRepository": "vvr" }, "parallelism": 1, "resources": { "jobmanager": { "memory": "2Gi", "cpu": 0.5 }, "taskmanager": { "memory": "3Gi", "cpu": 1.0 } }, "flinkConfiguration": {}, "logging": { "log4jLoggers": { "": "INFO" }, "logReservePolicy": { "expirationDays": 7, "openHistory": true }, "loggingProfile": "default" }, "batchMode": false } } }, "status": { "state": "SUSPENDED", "startTime": 1777341571990, "endTime": 0 } } |  |

实时计算（流计算） 参考

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| workspace | String | Path | 是 | default | 作业所在的工作空间ID。您可以通过以下任意一种方式获取： 通过ListNamespaces获取。 在Flink全托管开发控制台工作空间详情中获取。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | String | CBC799F0-AS7S- 1D30-8A4F- 882ED4DD**** | 请求ID。 |
|  |  | { "metadata": { "createdAt": "2026- 04-24T03:47:01Z", "workspace": "9cuwr9g7y1hl19", "modifiedAt": "2026-04- 24T03:56:19.55614 7Z", "resourceVersion": 134, "name": "sqlJob", "namespace": "flinkteam", "annotations": { "storage.disaster.r po": "1800", "deployment.sourc e-type": "EDITOR", "modifier": "23540697665705 7054", "creatorName": "flinkadmin", "one- time.retry": "false", "priority.class.nam e": "flink-p5", "deployment.exec- plan.uri.valid": "true", "default.resource- setting.has.migrate d": "true", "deployment.exec- plan.uri": "oss://flink- fullymanaged- 9cuwr9g7y1hl19/fli nk- jobs/namespaces/fl inkteam/jobs/f736b bd6-c9cf-48ab- 973a- 9653bb0f8c0a/exe |  |

实时计算（流计算） 参考

| 参数名称 | 类型 | cPlan.json", 示例 "deployment.refere | 说明 |
|---|---|---|---|
|  |  | nced.deployment.d raft.id": "cee26b6e- d03b-4a03-a628- a6fe665c525e", "resources.from.job .has.migrated": "true", "taker": " \| vvp-0", "creator": "23540697665705 7054", "resource- plan.has.migrated" : "true", "restore- from.savepoint-id": "5cea0d88-303d- 44e5-a96e- 47f7217723d7", "stop-with- savepoint.enabled" : "false", "deployment.has.d eployed": "false", "deployment.paren t.id": "", "plan.uri": "deployment/a3d8 8b2a-e076-4491- 86f2- 5a81ea4c7300/res |  |
| data | Integer | ourcePlan.json", "priority": "5", "migration.display. enabled": "false", "com.dataartisans. appmanager.contr oller.deployment.s pec.version": "11", "deployment.refere nced.deployment.d raft.history.version ": "1", "modifierName": "flinkadmin", "deployment.refere nced.deployment.d raft.history.id": "561a6a3d-7858- 4056-acfb- ad0cdec09e55" }, "id": "a3d88b2a- e076-4491-86f2- 5a81ea4c7300", "labels": {} }, "apiVersion": "v1", "kind": "Deployment", "spec": { "template": { "metadata": { "annotations": { "flink.resource.type ": "fine-grained", "job.resource.total. memory.byte": "0", "job.resource.total. cpu": "0.0", "native.kubernetes. | 详细信息。 |

实时计算（流计算） 参考

| 参数名称 | 类型 | mode": "true", 示例 "flink.queryable- | 说明 |
|---|---|---|---|
|  |  | state.enabled": "false", "flink.security.ssl.e nabled": "false" } }, "spec": { "artifact": { "flinkImageTag": "1.17.0-vvr-8.0.7- manifest-251107", "kind": "SQLSCRIPT", "sqlScript": "CREATE TEMPORARY TABLE `datahub table` _ (strname VARCHAR) with ( 'connector' = 'datagen' ); CREATE TEMPORARY TABLE `kafka table` _ (strname VARCHAR, lens BIGINT) with ( 'connector' = 'print' ); INSERT INTO kafka table _ SELECT SUBSTRING (strname, 0, 10) AS strname, CAST (CHAR LENGTH _ (strname) AS BIGINT) AS lens FROM datahub table;", _ "imageUserDefined ": false, "flinkImageRegistry ": "cn-wulan- env35-d01- reg.docker.intra.en v35.shuguang.com :80/ververica- paas", "versionName": "vvr-8.0.7-flink- 1.17", "flinkImageReposit ory": "vvr", "flinkVersion": "1.17" }, "parallelism": 1, "batchMode": false, "resources": { "jobmanager": { "memory": "2Gi", "cpu": 0.5 }, "taskmanager": { |  |

实时计算（流计算） 参考

| 参数名称 | 类型 | "memory": "3Gi", 示例 "cpu": 1.0 } }, | 说明 |
|---|---|---|---|
|  |  | "logging": { "log4jLoggers": { "": "INFO" }, "logReservePolicy": { "expirationDays": 7, "openHistory": true }, "loggingProfile": "default" }, "flinkConfiguration" : {} } }, "restoreStrategy": { "kind": "FROM SAVEPOINT _ ", "allowNonRestored State": false, "savepointId": "5cea0d88-303d- 44e5-a96e- 47f7217723d7" }, "state": "SUSPENDED", "upgradeStrategy": { "kind": "NONE" }, "maxSavepointCre ationAttempts": 4, "maxJobCreationAt tempts": 1, "deploymentTarget Id": "a89ff052- 38c6-4fd3-9b91- e9c53f8ee019" }, "status": { "startTime": 1777002791356, "state": "SUSPENDED", "endTime": 0 } } |  |
| success | Boolean | true | 请求是否成功。 |

**示例**

请求示例

```json
PUT /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/deployments/[deploymentId]/patch HTTP/1.1 { "RegionId":"cn-wulan-env***-d01", "namespace":"flinkteam", "deploymentId":"d0b3abf0-4bfe-46b1-a324-5b7def580c00", "workspace":"default" }
```

正常返回示例 `JSON` 格式实时计算（流计算） 参考

```json
{
 "data":"{\"metadata\":{\"createdAt\":\"2026-04-
24T03:47:01Z\",\"workspace\":\"9cuwr9g7y1hl19\",\"modifiedAt\":\"2026-04- 24T03:56:19.556147Z\",\"resourceVersion\":134,\"name\":\"sqlJob\",\"namespace\":\"flinktea ",\"annotations\":{\"storage.disaster.rpo\":\"1800\",\"deployment.sourcetype\":\"EDITOR\",\"modifier\":\"235406976657057054\",\"creatorName\":\"flinkadmin\",\"one time.retry\":\"false\",\"priority.class.name\":\"flink-p5\",\"deployment.execplan.uri.valid\":\"true\",\"default.resourcesetting.has.migrated\":\"true\",\"deployment.exec-plan.uri\":\"oss://flinkfullymanaged-9cuwr9g7y1hl19/flink-jobs/namespaces/flinkteam/jobs/f736bbd6-c9cf-48ab- 973a- 9653bb0f8c0a/execPlan.json\",\"deployment.referenced.deployment.draft.id\":\"cee26b6e-d 03b-4a03-a628-a6fe665c525e\",\"resources.from.job.has.migrated\":\"true\",\"taker\":\"
| vvp-0\",\"creator\":\"235406976657057054\",\"resource-
plan.has.migrated\":\"true\",\"restore-from.savepoint-id\":\"5cea0d88-303d-44e5-a96e- 47f7217723d7\",\"stop-withsavepoint.enabled\":\"false\",\"deployment.has.deployed\":\"false\",\"deployment.parent.id :\"\",\"plan.uri\":\"deployment/a3d88b2a-e076-4491-86f2- 5a81ea4c7300/resourcePlan.json\",\"priority\":\"5\",\"migration.display.enabled\":\"false\ \"com.dataartisans.appmanager.controller.deployment.spec.version\":\"11\",\"deployment.ref enced.deployment.draft.history.version\":\"1\",\"modifierName\":\"flinkadmin\",\"deploymen referenced.deployment.draft.history.id\":\"561a6a3d-7858-4056-acfbad0cdec09e55\"},\"id\":\"a3d88b2a-e076-4491-86f2-5a81ea4c7300\",\"labels\": {}},\"apiVersion\":\"v1\",\"kind\":\"Deployment\",\"spec\":{\"template\":{\"metadata\":{ \"annotations\":{\"flink.resource.type\":\"finegrained\",\"job.resource.total.memory.byte\":\"0\",\"job.resource.total.cpu\":\"0.0\",\"na ve.kubernetes.mode\":\"true\",\"flink.queryablestate.enabled\":\"false\",\"flink.security.ssl.enabled\":\"false\"}},\"spec\": {\"artifact\":{\"flinkImageTag\":\"1.17.0-vvr-8.0.7-manifest- 251107\",\"kind\":\"SQLSCRIPT\",\"sqlScript\":\"CREATE TEMPORARY TABLE `datahub_table` (strname VARCHAR)\with (\ 'connector' = 'datagen'\);\\CREATE TEMPORARY TABLE `kafka_t able` (strname VARCHAR, lens BIGINT)\with (\ 'connector' = 'print'\);\\INSERT INTO kafka_table\SELECT SUBSTRING (strname, 0, 10) AS strname, CAST (CHAR_LENGTH (strname) A S BIGINT) AS lens\FROM\ datahub_table;\",\"imageUserDefined\":false,\"flinkImageRegistry\":\"cn-wulan-env35d01-reg.docker.intra.env35.shuguang.com:80/ververica-paas\",\"versionName\":\"vvr- 8.0.7-flink- 1.17\",\"flinkImageRepository\":\"vvr\",\"flinkVersion\":\"1.17\"},\"parallelism\":1,\"bat Mode\":false,\"resources\":{\"jobmanager\": {\"memory\":\"2Gi\",\"cpu\":0.5},\"taskmanager\": {\"memory\":\"3Gi\",\"cpu\":1.0}},\"logging\":{\"log4jLoggers\": {\"\":\"INFO\"},\"logReservePolicy\": {\"expirationDays\":7,\"openHistory\":true},\"loggingProfile\":\"default\"},\"flinkConfigu tion\":{}}},\"restoreStrategy\": {\"kind\":\"FROM_SAVEPOINT\",\"allowNonRestoredState\":false,\"savepointId\":\"5cea0d88- 303d-44e5-a96e-47f7217723d7\"},\"state\":\"SUSPENDED\",\"upgradeStrategy\": {\"kind\":\"NONE\"},\"maxSavepointCreationAttempts\":4,\"maxJobCreationAttempts\":1,\"depl mentTargetId\":\"a89ff052-38c6-4fd3-9b91-e9c53f8ee019\"},\"status\": {\"startTime\":1777002791356,\"state\":\"SUSPENDED\",\"endTime\":0}}",
 "requestId":"CBC799F0-AS7S-1D30-8A4F-882ED4DD****",
 "success":true
}
```

实时计算（流计算） 参考 `XML` 格式

```xml
<data>{&quot;metadata&quot;:{&quot;createdAt&quot;:&quot;2026-04- 24T03:47:01Z&quot;,&quot;workspace&quot;:&quot;9cuwr9g7y1hl19&quot;,&quot;modifiedAt&quot; quot;2026-04- 24T03:56:19.556147Z&quot;,&quot;resourceVersion&quot;:134,&quot;name&quot;:&quot;sqlJob&qu ;,&quot;namespace&quot;:&quot;flinkteam&quot;,&quot;annotations&quot;: {&quot;storage.disaster.rpo&quot;:&quot;1800&quot;,&quot;deployment.sourcetype&quot;:&quot;EDITOR&quot;,&quot;modifier&quot;:&quot;235406976657057054&quot;,&quot;cr torName&quot;:&quot;flinkadmin&quot;,&quot;onetime.retry&quot;:&quot;false&quot;,&quot;priority.class.name&quot;:&quot;flinkp5&quot;,&quot;deployment.execplan.uri.valid&quot;:&quot;true&quot;,&quot;default.resourcesetting.has.migrated&quot;:&quot;true&quot;,&quot;deployment.execplan.uri&quot;:&quot;oss://flink-fullymanaged-9cuwr9g7y1hl19/flinkjobs/namespaces/flinkteam/jobs/f736bbd6-c9cf-48ab-973a- 9653bb0f8c0a/execPlan.json&quot;,&quot;deployment.referenced.deployment.draft.id&quot;:&qu ;cee26b6e-d03b-4a03-a628a6fe665c525e&quot;,&quot;resources.from.job.has.migrated&quot;:&quot;true&quot;,&quot;take quot;:&quot; | vvp- 0&quot;,&quot;creator&quot;:&quot;235406976657057054&quot;,&quot;resourceplan.has.migrated&quot;:&quot;true&quot;,&quot;restore-from.savepointid&quot;:&quot;5cea0d88-303d-44e5-a96e-47f7217723d7&quot;,&quot;stop-withsavepoint.enabled&quot;:&quot;false&quot;,&quot;deployment.has.deployed&quot;:&quot;false& ot;,&quot;deployment.parent.id&quot;:&quot;&quot;,&quot;plan.uri&quot;:&quot;deployment/a3 8b2a-e076-4491-86f2- 5a81ea4c7300/resourcePlan.json&quot;,&quot;priority&quot;:&quot;5&quot;,&quot;migration.di lay.enabled&quot;:&quot;false&quot;,&quot;com.dataartisans.appmanager.controller.deploymen spec.version&quot;:&quot;11&quot;,&quot;deployment.referenced.deployment.draft.history.ver on&quot;:&quot;1&quot;,&quot;modifierName&quot;:&quot;flinkadmin&quot;,&quot;deployment.re renced.deployment.draft.history.id&quot;:&quot;561a6a3d-7858-4056-acfbad0cdec09e55&quot;},&quot;id&quot;:&quot;a3d88b2a-e076-4491-86f2- 5a81ea4c7300&quot;,&quot;labels&quot;: {}},&quot;apiVersion&quot;:&quot;v1&quot;,&quot;kind&quot;:&quot;Deployment&quot;,&quot;sp &quot;:{&quot;template&quot;:{&quot;metadata&quot;:{&quot;annotations&quot;: {&quot;flink.resource.type&quot;:&quot;finegrained&quot;,&quot;job.resource.total.memory.byte&quot;:&quot;0&quot;,&quot;job.resource tal.cpu&quot;:&quot;0.0&quot;,&quot;native.kubernetes.mode&quot;:&quot;true&quot;,&quot;fl k.queryablestate.enabled&quot;:&quot;false&quot;,&quot;flink.security.ssl.enabled&quot;:&quot;false&q t;}},&quot;spec&quot;:{&quot;artifact&quot;:{&quot;flinkImageTag&quot;:&quot;1.17.0-vvr -8.0.7-manifest- 251107&quot;,&quot;kind&quot;:&quot;SQLSCRIPT&quot;,&quot;sqlScript&quot;:&quot;CREATE TEMPORARY TABLE `datahub_table` (strname VARCHAR)with ( &#x27;connector&#x27; = &#x27;datagen&#x27;);CREATE TEMPORARY TABLE `kafka_table` (strname VARCHAR, lens BIGINT)with ( &#x27;connector&#x27; = &#x27;print&#x27;);INSERT INTO kafka_tableSELECT SUBSTRING (strname, 0, 10) AS strname, CAST (CHAR_LENGTH (strname) AS BIGINT) AS lensFROM datahub_table;&quot;,&quot;imageUserDefined&quot;:false,&quot;flinkImageRegistry&quot;:&qu ;cn-wulan-env35-d01-reg.docker.intra.env35.shuguang.com:80/ververicapaas&quot;,&quot;versionName&quot;:&quot;vvr-8.0.7-flink- 1.17&quot;,&quot;flinkImageRepository&quot;:&quot;vvr&quot;,&quot;flinkVersion&quot;:&quot .17&quot;},&quot;parallelism&quot;:1,&quot;batchMode&quot;:false,&quot;resources&quot;: {&quot;jobmanager&quot;: {&quot;memory&quot;:&quot;2Gi&quot;&quot;cpu&quot;:05}&quot;taskmanager&quot;:
```

实时计算（流计算） 参考

```xml
{&quot;memory&quot;:&quot;2Gi&quot;,&quot;cpu&quot;:0.5},&quot;taskmanager&quot;: {&quot;memory&quot;:&quot;3Gi&quot;,&quot;cpu&quot;:1.0}},&quot;logging&quot;: {&quot;log4jLoggers&quot;:{&quot;&quot;:&quot;INFO&quot;},&quot;logReservePolicy&quot;: {&quot;expirationDays&quot;:7,&quot;openHistory&quot;:true},&quot;loggingProfile&quot;:&qu ;default&quot;},&quot;flinkConfiguration&quot;:{}}},&quot;restoreStrategy&quot;: {&quot;kind&quot;:&quot;FROM_SAVEPOINT&quot;,&quot;allowNonRestoredState&quot;:false,&quot avepointId&quot;:&quot;5cea0d88-303d-44e5-a96e- 47f7217723d7&quot;},&quot;state&quot;:&quot;SUSPENDED&quot;,&quot;upgradeStrategy&quot;: {&quot;kind&quot;:&quot;NONE&quot;},&quot;maxSavepointCreationAttempts&quot;:4,&quot;maxJo reationAttempts&quot;:1,&quot;deploymentTargetId&quot;:&quot;a89ff052-38c6-4fd3-9b91e9c53f8ee019&quot;},&quot;status&quot;: {&quot;startTime&quot;:1777002791356,&quot;state&quot;:&quot;SUSPENDED&quot;,&quot;endTime uot;:0}}</data> <requestId>CBC799F0-AS7S-1D30-8A4F-882ED4DD****</requestId> <success>true</success>
```

###### UpdateConnector

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
PUT /pop/workspaces/[workspace]/sql/v1beta1/namespaces/[namespace]/connectors/[name] HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | String | Host | 是 | cn-wulan-env***-d01 | Region ID。 |
| workspace | String | Path | 是 | default | 作业所在的工作空间ID。您可以通过以下任意一种方式获取： 通过ListNamespaces获取。 在Flink全托管开发控制台工作空间详情中获取。 |
| name | String | Path | 是 | hologres-fix | 要变更的connector名称。 |

实时计算（流计算） 参考

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| paramsJso n | String | Body | 否 | { "type": "hologres-fix", "name": "namespaces/flinkteam/ connectors/hologres-fix", "packaged": false, "source": true, "sink": true, "lookup": false, "dependencies": [ "hdfs:///vvp/data/sql- artifacts/namespaces/fli nkteam/custom- connectors/2024-03- 11T05-51- 25.289740Z/ververica- connector-hologres-1.15- vvr-6.0-fix.jar" ], "supportedFormats": [ "json","csv" ], "properties": [ { "key": "connector", "required": true, "defaultValue": "hologres-fix", "description": "", "definesFormat": false }, { "key": "dbname", "required": true, "defaultValue": "", "description": "", "definesFormat": false }, { "key": "endpoint", "required": true, "defaultValue": "", "description": "", "definesFormat": false }, { "key": "tablename", "required": true, "defaultValue": "", "description": "", "definesFormat": false } ] } | 变更参数，用于声明 connector的属性，例如： 类型名称、必填的连接参数、可否作为source、 sink、依赖的jar包等。 |
| namespac e | String | Path | 是 | flinkteam | 作业所在的项目空间名称。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| success | Boolean | true | 请求是否成功。 |

实时计算（流计算） 参考

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| data | String | { "affectedTables": [], "connector": { "lookup": true, "supportedFormats ": [ "json", "csv" ], "environments": [], "sink": true, "name": "namespaces/flinkt eam/connectors/ho logres-fix", "source": true, "type": "hologres- fix", "properties": [ { "defaultValue": "hologres-fix", "description": "", "definesFormat": false, "key": "connector", "required": true }, { "defaultValue": "", "description": "", "definesFormat": false, "key": "dbname", "required": true }, { "defaultValue": "", "description": "", "definesFormat": false, "key": "endpoint", "required": true }, { "defaultValue": "", "description": "", "definesFormat": false, "key": "tablename", "required": true } ], "packaged": false, "dependencies": [ "hdfs:///vvp/data/sq l- artifacts/namespac es/flinkteam/custo m- connectors/2024- 03-11T05-51- 25.289740Z/verver ica-connector- hologres-1.15-vvr- 6.0-fix.jar" ] }, "@type": "type.googleapis.c om/vvp.sql.v1beta 1.UpdateConnector Response" } | 详细数据。 |

实时计算（流计算） 参考

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | String | 4FA46133-1C97- 4B48-96E3- 3B7DFFFEC707 | 请求ID。 |

**示例**

请求示例

```json
PUT /pop/workspaces/[workspace]/sql/v1beta1/namespaces/[namespace]/connectors/[name] HTTP/1.1 { "RegionId":"cn-wulan-env***-d01", "workspace":"default", "name":"hologres-fix", "namespace":"flinkteam" }
```

正常返回示例 `JSON` 格式

```json
{
 "data":"{\"affectedTables\":[],\"connector\":{\"lookup\":true,\"supportedFormats\":[\"
json\",\"csv\"],\"environments\": [],\"sink\":true,\"name\":\"namespaces/flinkteam/connectors/hologresfix\",\"source\":true,\"type\":\"hologres-fix\",\"properties\": [{\"defaultValue\":\"hologresfix\",\"description\":\"\",\"definesFormat\":false,\"key\":\"connector\",\"required\":true {\"defaultValue\":\"\",\"description\":\"\",\"definesFormat\":false,\"key\":\"dbname\",\"r uired\":true}, {\"defaultValue\":\"\",\"description\":\"\",\"definesFormat\":false,\"key\":\"endpoint\",\ equired\":true}, {\"defaultValue\":\"\",\"description\":\"\",\"definesFormat\":false,\"key\":\"tablename\", required\":true}],\"packaged\":false,\"dependencies\":[\"hdfs:///vvp/data/sqlartifacts/namespaces/flinkteam/custom-connectors/2024-03-11T05-51-25.289740Z/ververica-c onnector-hologres-1.15-vvr-6.0fix.jar\"]},\"@type\":\"type.googleapis.com/vvp.sql.v1beta1.UpdateConnectorResponse\"}",
 "success":true,
 "requestId":"4FA46133-1C97-4B48-96E3-3B7DFFFEC707"
}
```

`XML` 格式实时计算（流计算） 参考

```xml
<data>{&quot;affectedTables&quot;:[],&quot;connector&quot;: {&quot;lookup&quot;:true,&quot;supportedFormats&quot;: [&quot;json&quot;,&quot;csv&quot;],&quot;environments&quot;: [],&quot;sink&quot;:true,&quot;name&quot;:&quot;namespaces/flinkteam/connectors/hologresfix&quot;,&quot;source&quot;:true,&quot;type&quot;:&quot;hologresfix&quot;,&quot;properties&quot;:[{&quot;defaultValue&quot;:&quot;hologresfix&quot;,&quot;description&quot;:&quot;&quot;,&quot;definesFormat&quot;:false,&quot;key&q t;:&quot;connector&quot;,&quot;required&quot;:true}, {&quot;defaultValue&quot;:&quot;&quot;,&quot;description&quot;:&quot;&quot;,&quot;definesF mat&quot;:false,&quot;key&quot;:&quot;dbname&quot;,&quot;required&quot;:true}, {&quot;defaultValue&quot;:&quot;&quot;,&quot;description&quot;:&quot;&quot;,&quot;definesF mat&quot;:false,&quot;key&quot;:&quot;endpoint&quot;,&quot;required&quot;:true}, {&quot;defaultValue&quot;:&quot;&quot;,&quot;description&quot;:&quot;&quot;,&quot;definesF mat&quot;:false,&quot;key&quot;:&quot;tablename&quot;,&quot;required&quot;:true}],&quot;pa aged&quot;:false,&quot;dependencies&quot;:[&quot;hdfs:///vvp/data/sqlartifacts/namespaces/flinkteam/custom-connectors/2024-03-11T05-51-25.289740Z/ververica-c onnector-hologres-1.15-vvr-6.0fix.jar&quot;]},&quot;@type&quot;:&quot;type.googleapis.com/vvp.sql.v1beta1.UpdateConnecto esponse&quot;}</data> <success>true</success> <requestId>4FA46133-1C97-4B48-96E3-3B7DFFFEC707</requestId>
```

###### TableExists

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
GET /pop/workspaces/[workspace]/catalog/v1beta2/namespaces/[namespace]/catalogs/[cat]:tableExi s HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | String | Host | 是 | cn-wulan-env***-d01 | Region ID。 |
| namespac e | String | Path | 是 | ververica | 作业所在的项目空间名称。 |

实时计算（流计算） 参考

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| workspace | String | Path | 是 | default | 作业所在的工作空间ID。您可以通过以下任意一种方式获取： 通过ListNamespaces获取。 在Flink全托管开发控制台工作空间详情中获取。 |
| cat | String | Path | 是 | vvp | catalog名称。 |
| database | String | Query | 是 | default | database名称。 |
| table | String | Query | 是 | mydatahub | table名称。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| data | String | { "@type": "type.googleapis.c om/vvp.sql.catalog. v1beta2.TableExist sResponse", "exists": true } | 详细信息。 |
| requestId | String | 39253EC3-B674- 4B11-AD97- C221D6DB1003 | 请求ID。 |
| success | Boolean | true | 请求是否成功。 |

**示例**

请求示例

```
GET /pop/workspaces/[workspace]/catalog/v1beta2/namespaces/[namespace]/catalogs/[cat]:tableExi s HTTP/1.1 &RegionId=cn-wulan-env***-d01 &namespace=ververica &workspace=default &cat=vvp &database=default &table=mydatahub
```

&公共请求参数正常返回示例 `JSON` 格式实时计算（流计算） 参考

```json
{
 "data":"
{\"@type\":\"type.googleapis.com/vvp.sql.catalog.v1beta2.TableExistsResponse\",\"exists\" ue}",
 "requestId":"39253EC3-B674-4B11-AD97-C221D6DB1003",
 "success":true
}
```

`XML` 格式

```xml
<data> {&quot;@type&quot;:&quot;type.googleapis.com/vvp.sql.catalog.v1beta2.TableExistsResponse&q t;,&quot;exists&quot;:true}</data> <requestId>39253EC3-B674-4B11-AD97-C221D6DB1003</requestId> <success>true</success>
```

###### SetDeploymentResourceMode

调用SetDeploymentResourceMode，设置作业resourceMode。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
PUT /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/deployments/[deploymentId]/setresource HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | String | Host | 是 | cn-wulan-env***-d01 | Region ID。 |
| workspace | String | Path | 是 | default | 作业所在的工作空间ID。您可以通过以下任意一种方式获取： 通过ListNamespaces获取。 在Flink全托管开发控制台工作空间详情中获取。 |
| namespac e | String | Path | 是 | flinkteam | 作业所在的项目空间名称。 |
| deployme ntId | String | Path | 是 | d0b3abf0-4bfe-46b1- a324-5b7def580c00 | 作业ID。 |

实时计算（流计算） 参考

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| paramsJso n | String | Body | 否 | { "deploymentResourceMo deBase": { "kind": "auto" } } | 请求参数，kind可选项： auto、fine-grained、 coarse-grained。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| success | Boolean | true | 请求是否成功。 |
|  |  | { "metadata": { "createdAt": "2024- 03-12T06:12:17Z", "modifiedAt": "2024-03- 12T06:44:00.82332 3Z", "resourceVersion": 15, "name": "sqljob", "namespace": "flinkteam", "annotations": { "creator": "22985261012276 3813", "resource- plan.has.migrated" : "true", "deployment.has.d eployed": "false", "deployment.sourc e-type": "EDITOR", "deployment.paren t.id": "", "modifier": "22985261012276 3813", "creatorName": "flinkadmin", "priority": "5", "priority.class.nam e": "", "autopilot.mode": "monitor", "com.dataartisans. appmanager.contr oller.deployment.s pec.version": "3", "deployment.refere nced.deployment.d raft.history.version ": "1", "x- namespace-owner- master-uid": "10529101227299 09", "default.resource- setting.has.migrate d": "true", "deployment.exec- plan.uri": |  |

实时计算（流计算） 参考

| 参数名称 | 类型 | "hdfs:///vvp/data/pl 示例 an/namespaces/flin | 说明 |
|---|---|---|---|
|  |  | kteam/deployment/ d0b3abf0-4bfe- 46b1-a324- 5b7def580c00/exe cPlan.json", "deployment.refere nced.deployment.d raft.id": "c6f157ac- 60b9-4b38-8bad- d435387cfd59", "comment": "", "modifierName": "flinkadmin", "taker": "default- cluster \| 0", "deployment.refere nced.deployment.d raft.history.id": "1fbfefd4-9b1c- 4e94-b6ad- 268a5c6b64cd" }, "workspaceName": "default", "id": "d0b3abf0-4bfe- 46b1-a324- 5b7def580c00", "labels": {} }, "apiVersion": "v1", "kind": "Deployment", "spec": { "template": { "metadata": { |  |
| data | String | "annotations": { "flink.resource.type ": "auto", "job.resource.total. memory.byte": "8589934592", "job.resource.total. cpu": "4.0", "native.kubernetes. mode": "true", "flink.queryable- state.enabled": "false" } }, "spec": { "artifact": { "flinkImageTag": "1.15.0-vvr-6.0.7- 29", "kind": "SQLSCRIPT", "sqlScript": "-- ******************* ******************* ******************* ***********-- -- Author: Write your name here -- Created Time: 2024-03-12 14:11:38 -- Description: Write your description here -- | 详细数据。 |

实时计算（流计算） 参考

| 参数名称 | 类型 | ******************* 示例 ******************* | 说明 |
|---|---|---|---|
|  |  | ******************* ***********-- CREATE TEMPORARY TABLE `datahub table` _ (strname VARCHAR) with ( \u0027connector\u 0027 \u003d \u0027datagen\u00 27 ); CREATE TEMPORARY TABLE `kafka table` _ (strname VARCHAR, lens BIGINT) with ( \u0027connector\u 0027 \u003d \u0027print\u0027 ); INSERT INTO kafka table _ SELECT SUBSTRING (strname, 0, 10) AS strname, CAST (CHAR LENGTH _ (strname) AS BIGINT) AS lens FROM datahub table; _ ", "imageUserDefined ": false, "flinkImageRegistry ": "cn-qingdao- env17e-d01- reg.docker.intra.en v17e.shuguang.co m:80/ververica- paas", "versionName": "vvr-6.0.0-flink- 1.15", "flinkImageReposit ory": "vvr", "flinkVersion": "1.15" }, "parallelism": 1, "batchMode": false, "resources": { "jobmanager": { "memory": "4Gi", "cpu": 2.0 }, "taskmanager": { "memory": "4Gi", "cpu": 2.0 } }, "logging": { "log4jLoggers": { "": "INFO" }, "logReservePolicy": |  |

实时计算（流计算） 参考

| 参数名称 | 类型 | { "expirationDays": 示例 7, "openHistory": | 说明 |
|---|---|---|---|
|  |  | true }, "loggingProfile": "default" }, "flinkConfiguration" : { "execution.checkpo inting.interval": "180s", "execution.checkpo inting.min-pause": "180s" } } }, "restoreStrategy": { "kind": "LATEST STATE", _ "allowNonRestored State": false }, "state": "RUNNING", "upgradeStrategy": { "kind": "NONE" }, "maxSavepointCre ationAttempts": 4, "maxJobCreationAt tempts": 1, "deploymentTarget Id": "f2ed6708- a7e1-4e86-a99e- 327fac9265c2" }, "status": { "startTime": 0, "state": "RUNNING", "endTime": 0 } } |  |
| requestId | String | BCC13432-238D- 41D7-B0A6- 582241A6B572 | 请求ID。 |

**示例**

请求示例

```json
PUT /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/deployments/[deploymentId]/setresource HTTP/1.1 { "RegionId":"cn-wulan-env***-d01", "workspace":"default", "namespace":"flinkteam", "deploymentId":"d0b3abf0-4bfe-46b1-a324-5b7def580c00" }
```

正常返回示例 `JSON` 格式

```json
{
 "data":"{\"metadata\":{\"createdAt\":\"2024-03-12T06:12:17Z\",\"modifiedAt\":\"2024-
03- 12T06:44:00.823323Z\",\"resourceVersion\":15,\"name\":\"sqljob\",\"namespace\":\"flinkteam
```

实时计算（流计算） 参考

```json
,\"annotations\":{\"creator\":\"229852610122763813\",\"resourceplan.has.migrated\":\"true\",\"deployment.has.deployed\":\"false\",\"deployment.sourcetype\":\"EDITOR\",\"deployment.parent.id\":\"\",\"modifier\":\"229852610122763813\",\"crea rName\":\"flinkadmin\",\"priority\":\"5\",\"priority.class.name\":\"\",\"autopilot.mode\" monitor\",\"com.dataartisans.appmanager.controller.deployment.spec.version\":\"3\",\"deplo ent.referenced.deployment.draft.history.version\":\"1\",\"x-namespace-owner-masteruid\":\"1052910122729909\",\"default.resourcesetting.has.migrated\":\"true\",\"deployment.execplan.uri\":\"hdfs:///vvp/data/plan/namespaces/flinkteam/deployment/d0b3abf0-4bfe-46b1-a 324- 5b7def580c00/execPlan.json\",\"deployment.referenced.deployment.draft.id\":\"c6f157ac-6 0b9-4b38-8badd435387cfd59\",\"comment\":\"\",\"modifierName\":\"flinkadmin\",\"taker\":\"defaultcluster | 0\",\"deployment.referenced.deployment.draft.history.id\":\"1fbfefd4-9b1c- 4e94-b6ad-268a5c6b64cd\"},\"workspaceName\":\"default\",\"id\":\"d0b3abf0-4bfe-46b1a324-5b7def580c00\",\"labels\": {}},\"apiVersion\":\"v1\",\"kind\":\"Deployment\",\"spec\":{\"template\":{\"metadata\":{ \"annotations\": {\"flink.resource.type\":\"auto\",\"job.resource.total.memory.byte\":\"8589934592\",\"job source.total.cpu\":\"4.0\",\"native.kubernetes.mode\":\"true\",\"flink.queryablestate.enabled\":\"false\"}},\"spec\":{\"artifact\":{\"flinkImageTag\":\"1.15.0-vvr- 6.0.7-29\",\"kind\":\"SQLSCRIPT\",\"sqlScript\":\"--
********************************************************************--\-- Author:
Write your name here\-- Created Time: 2024-03-12 14:11:38\-- Description: Write you r description here\--
********************************************************************--\CREATE TEMPORARY
TABLE `datahub_table` (strname VARCHAR)\with (\ \\u0027connector\\u0027 \\u003d \\u00 27datagen\\u0027\ );\\CREATE TEMPORARY TABLE `kafka_table` (strname VARCHAR, lens BIGINT)\with (\ \\u0027connector\\u0027 \\u003d \\u0027print\\u0027\ );\\INSERT INTO kafka_table\SELECT SUBSTRING (strname, 0, 10) AS strname, CAST (CHAR_LENGTH (strname) A S BIGINT) AS lens\FROM\ datahub_table;\\",\"imageUserDefined\":false,\"flinkImageRegistry\":\"cn-qingdaoenv17e-d01-reg.docker.intra.env17e.shuguang.com:80/ververicapaas\",\"versionName\":\"vvr-6.0.0-flink- 1.15\",\"flinkImageRepository\":\"vvr\",\"flinkVersion\":\"1.15\"},\"parallelism\":1,\"bat Mode\":false,\"resources\":{\"jobmanager\": {\"memory\":\"4Gi\",\"cpu\":2.0},\"taskmanager\": {\"memory\":\"4Gi\",\"cpu\":2.0}},\"logging\":{\"log4jLoggers\": {\"\":\"INFO\"},\"logReservePolicy\": {\"expirationDays\":7,\"openHistory\":true},\"loggingProfile\":\"default\"},\"flinkConfigu tion\":{\"execution.checkpointing.interval\":\"180s\",\"execution.checkpointing.minpause\":\"180s\"}}},\"restoreStrategy\": {\"kind\":\"LATEST_STATE\",\"allowNonRestoredState\":false},\"state\":\"RUNNING\",\"upgrad trategy\": {\"kind\":\"NONE\"},\"maxSavepointCreationAttempts\":4,\"maxJobCreationAttempts\":1,\"depl mentTargetId\":\"f2ed6708-a7e1-4e86-a99e-327fac9265c2\"},\"status\": {\"startTime\":0,\"state\":\"RUNNING\",\"endTime\":0}}",
 "success":true,
 "requestId":"BCC13432-238D-41D7-B0A6-582241A6B572"
}
```

`XML` 格式

```xml
<data>{&quot;metadata&quot;:{&quot;createdAt&quot;:&quot;2024-03-
```

实时计算（流计算） 参考

```
12T06:12:17Z&quot;,&quot;modifiedAt&quot;:&quot;2024-03- 12T06:44:00.823323Z&quot;,&quot;resourceVersion&quot;:15,&quot;name&quot;:&quot;sqljob&quo ,&quot;namespace&quot;:&quot;flinkteam&quot;,&quot;annotations&quot;: {&quot;creator&quot;:&quot;229852610122763813&quot;,&quot;resourceplan.has.migrated&quot;:&quot;true&quot;,&quot;deployment.has.deployed&quot;:&quot;false&q t;,&quot;deployment.sourcetype&quot;:&quot;EDITOR&quot;,&quot;deployment.parent.id&quot;:&quot;&quot;,&quot;modifier uot;:&quot;229852610122763813&quot;,&quot;creatorName&quot;:&quot;flinkadmin&quot;,&quot;p ority&quot;:&quot;5&quot;,&quot;priority.class.name&quot;:&quot;&quot;,&quot;autopilot.mod quot;:&quot;monitor&quot;,&quot;com.dataartisans.appmanager.controller.deployment.spec.ver on&quot;:&quot;3&quot;,&quot;deployment.referenced.deployment.draft.history.version&quot; uot;1&quot;,&quot;x-namespace-owner-masteruid&quot;:&quot;1052910122729909&quot;,&quot;default.resourcesetting.has.migrated&quot;:&quot;true&quot;,&quot;deployment.execplan.uri&quot;:&quot;hdfs:///vvp/data/plan/namespaces/flinkteam/deployment/d0b3abf0- 4bfe-46b1-a324- 5b7def580c00/execPlan.json&quot;,&quot;deployment.referenced.deployment.draft.id&quot;:&qu ;c6f157ac-60b9-4b38-8badd435387cfd59&quot;,&quot;comment&quot;:&quot;&quot;,&quot;modifierName&quot;:&quot;flinkad n&quot;,&quot;taker&quot;:&quot;default-cluster | 0&quot;,&quot;deployment.referenced.deployment.draft.history.id&quot;:&quot;1fbfefd4- 9b1c-4e94-b6ad- 268a5c6b64cd&quot;},&quot;workspaceName&quot;:&quot;default&quot;,&quot;id&quot;:&quot;d0b bf0-4bfe-46b1-a324-5b7def580c00&quot;,&quot;labels&quot;: {}},&quot;apiVersion&quot;:&quot;v1&quot;,&quot;kind&quot;:&quot;Deployment&quot;,&quot;sp &quot;:{&quot;template&quot;:{&quot;metadata&quot;:{&quot;annotations&quot;: {&quot;flink.resource.type&quot;:&quot;auto&quot;,&quot;job.resource.total.memory.byte&quo :&quot;8589934592&quot;,&quot;job.resource.total.cpu&quot;:&quot;4.0&quot;,&quot;native.ku rnetes.mode&quot;:&quot;true&quot;,&quot;flink.queryablestate.enabled&quot;:&quot;false&quot;}},&quot;spec&quot;:{&quot;artifact&quot;: {&quot;flinkImageTag&quot;:&quot;1.15.0-vvr-6.0.7- 29&quot;,&quot;kind&quot;:&quot;SQLSCRIPT&quot;,&quot;sqlScript&quot;:&quot;--
********************************************************************---- Author:
Write your name here-- Created Time: 2024-03-12 14:11:38-- Description: Write your description here--********************************************************************-- CREATE TEMPORARY TABLE `datahub_table` (strname VARCHAR)with ( \u0027connector\u0027 \u003d \u0027datagen\u0027 );CREATE TEMPORARY TABLE `kafka_table` (strname VARCHAR, lens BIGINT)with ( \u0027connector\u0027 \u003d \u0027print\u0027 );INSERT INTO kafka_tableSELECT SUBSTRING (strname, 0, 10) AS strname, CAST (CHAR_LENGTH (strname) AS BIGINT) AS lensFROM datahub_table;&quot;,&quot;imageUserDefined&quot;:false,&quot;flinkImageRegistry&quot;:&qu ;cn-qingdao-env17e-d01-reg.docker.intra.env17e.shuguang.com:80/ververicapaas&quot;,&quot;versionName&quot;:&quot;vvr-6.0.0-flink- 1.15&quot;,&quot;flinkImageRepository&quot;:&quot;vvr&quot;,&quot;flinkVersion&quot;:&quot .15&quot;},&quot;parallelism&quot;:1,&quot;batchMode&quot;:false,&quot;resources&quot;: {&quot;jobmanager&quot;: {&quot;memory&quot;:&quot;4Gi&quot;,&quot;cpu&quot;:2.0},&quot;taskmanager&quot;: {&quot;memory&quot;:&quot;4Gi&quot;,&quot;cpu&quot;:2.0}},&quot;logging&quot;: {&quot;log4jLoggers&quot;:{&quot;&quot;:&quot;INFO&quot;},&quot;logReservePolicy&quot;: {&quot;expirationDays&quot;:7,&quot;openHistory&quot;:true},&quot;loggingProfile&quot;:&qu ;default&quot;},&quot;flinkConfiguration&quot;: {&quot;execution.checkpointing.interval&quot;:&quot;180s&quot;,&quot;execution.checkpointi .min-pause&quot;:&quot;180s&quot;}}},&quot;restoreStrategy&quot;: {&quot;kind&quot;:&quot;LATEST_STATE&quot;,&quot;allowNonRestoredState&quot;:false},&quot; ate&quot;:&quot;RUNNING&quot;&quot;upgradeStrategy&quot;:
```

实时计算（流计算） 参考

```xml
ate&quot;:&quot;RUNNING&quot;,&quot;upgradeStrategy&quot;: {&quot;kind&quot;:&quot;NONE&quot;},&quot;maxSavepointCreationAttempts&quot;:4,&quot;maxJo reationAttempts&quot;:1,&quot;deploymentTargetId&quot;:&quot;f2ed6708-a7e1-4e86-a99e- 327fac9265c2&quot;},&quot;status&quot;: {&quot;startTime&quot;:0,&quot;state&quot;:&quot;RUNNING&quot;,&quot;endTime&quot;:0}}< /data> <success>true</success> <requestId>BCC13432-238D-41D7-B0A6-582241A6B572</requestId>
```

###### ParseFormat

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /pop/workspaces/[workspace]/sql/v1beta1/namespaces/[namespace]/formats:analyzejars HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | String | Host | 是 | cn-wulan-env***-d01 | Region ID。 |
| workspace | String | Path | 是 | default | 作业所在的工作空间ID。您可以通过以下任意一种方式获取： 通过ListNamespaces获取。 在Flink全托管开发控制台工作空间详情中获取。 |
| paramsJso n | String | Body | 否 | { "jarUris": [ "http://flink- resource.oss-cn-wulan- env**-d01- a.intra.env**.shuguang.c om/format/customized- csv-demo-1.0- SNAPSHOT.jar" ] } | 待解析format jar包列表。 |
| namespac e | String | Path | 是 | flinkteam | 作业所在的项目空间名称。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| success | Boolean | true | 请求是否成功。 |

| F | link存算分离版开发参考 | 指南·OpenAPI |  | 实时计算（流计算） |  |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| data | String | { "duplicatedSinkFac toriesFormats": [], "formats": [], "@type": "type.googleapis.c om/vvp.sql.v1beta 1.AnalyzeFormatJar sResponse", "duplicatedFilesyst emFormatFactories Formats": [], "duplicatedSourceF actoriesFormats": [] } | Format解析结果详细信息。 |
| requestId | String | CBC799F0-AS7S- 1D30-8A4F- 882ED4DD**** | 请求ID。 |

**示例**

请求示例

```json
POST /pop/workspaces/[workspace]/sql/v1beta1/namespaces/[namespace]/formats:analyzejars HTTP/1.1 { "RegionId":"cn-wulan-env***-d01", "workspace":"default", "namespace":"flinkteam" }
```

正常返回示例 `JSON` 格式

```json
{
 "data":"{\"duplicatedSinkFactoriesFormats\":[],\"formats\":
[],\"@type\":\"type.googleapis.com/vvp.sql.v1beta1.AnalyzeFormatJarsResponse\",\"duplicate ilesystemFormatFactoriesFormats\":[],\"duplicatedSourceFactoriesFormats\":[]}",
 "success":true,
 "requestId":"CBC799F0-AS7S-1D30-8A4F-882ED4DD****"
}
```

`XML` 格式

```xml
<data>{&quot;duplicatedSinkFactoriesFormats&quot;:[],&quot;formats&quot;: [],&quot;@type&quot;:&quot;type.googleapis.com/vvp.sql.v1beta1.AnalyzeFormatJarsResponse&q t;,&quot;duplicatedFilesystemFormatFactoriesFormats&quot;: [],&quot;duplicatedSourceFactoriesFormats&quot;:[]}</data> <success>true</success> <requestId>CBC799F0-AS7S-1D30-8A4F-882ED4DD****</requestId>
```

实时计算（流计算） 参考

###### ParseConnector

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /pop/workspaces/[workspace]/sql/v1beta1/namespaces/[namespace]/connectors:analyzejars HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | String | Host | 是 | cn-wulan-env***-d01 | Region ID。 |
| workspace | String | Path | 是 | default | 作业所在的工作空间ID。您可以通过以下任意一种方式获取： 通过ListNamespaces获取。 在Flink全托管开发控制台工作空间详情中获取。 |
| paramsJso n | String | Body | 否 | {"jarUris": ["http://flink- resource.oss-cn-wulan- env**-d01- a.intra.env**.shuguang.c om/connectors/ververica -connector-hologres- 1.15-vvr-6.0-fix.jar"]} | 待解析的自定已connector jar包路径列表。 |
| namespac e | String | Path | 是 | flinkteam | 作业所在的项目空间名称。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| success | Boolean | true | 请求是否成功。 |
|  |  | {"connectors": [{"lookup":false,"s upportedFormats": [],"environments": [],"sink":true,"nam e":"namespaces/fli nkteam/connectors /hologres- fix","source":true,"t ype":"hologres- fix","properties": |  |

| link存算分离版开发参考 | 指南·OpenAPI |  | 实时计算（流计算） |
|---|---|---|---|
| 参数名称 | 类型 | [{"defaultValue":"1 示例 0","description":""," | 说明 |
|  |  | definesFormat":fals e,"key":"poolsize"," required":false}, {"defaultValue":"fa lse","description":"" ,"definesFormat":fa lse,"key":"async","r equired":false}, {"defaultValue":"", "description":"","de finesFormat":false, "key":"cacheReloa dTimeBlackList","re quired":false}, {"defaultValue":"", "description":"","de finesFormat":false, "key":"password","r equired":false}, {"defaultValue":"fa lse","description":"" ,"definesFormat":fa lse,"key":"bhclienti gnorebeforeupdate ","required":false}, {"defaultValue":"1 000","description": "","definesFormat": false,"key":"jdbcret rysleepinitms","req uired":false}, {"defaultValue":"fa lse","description":"" ,"definesFormat":fa lse,"key":"insertifn otexists","required" :false}, {"defaultValue":"2 56","description":"" ,"definesFormat":fa lse,"key":"jdbcscan fetchsize","require d":false}, {"defaultValue":"- 1","description":""," definesFormat":fals e,"key":"starttime ms","required":fals e}, {"defaultValue":"tr ue","description":"" ,"definesFormat":fa lse,"key":"jdbcenab ledefaultfornotnullc olumn","required":f alse}, {"defaultValue":"fa lse","description":"" ,"definesFormat":fa lse,"key":"binlog","r equired":false}, {"defaultValue":"1 00","description":"" ,"definesFormat":fa lse,"key":"binlogba |  |

实时计算（流计算） 参考

| 参数名称 | 类型 | tchreadsize","requi 示例 red":false}, | 说明 |
|---|---|---|---|
|  |  | {"defaultValue":"5 00","description":"" ,"definesFormat":fa lse,"key":"clientma xpause","required": false}, {"defaultValue":"2" ,"description":"","d efinesFormat":false ,"key":"errorcount", "required":false}, {"defaultValue":"2 56","description":"" ,"definesFormat":fa lse,"key":"jdbcwrite batchsize","require d":false}, {"defaultValue":"fa lse","description":"" ,"definesFormat":fa lse,"key":"jdbcusel egacyputhandler"," required":false}, {"defaultValue":"1 28","description":"" ,"definesFormat":fa lse,"key":"jdbcread batchsize","require d":false}, {"defaultValue":"4" ,"description":"","d efinesFormat":false ,"key":"bhclientthre adpool","required": false}, {"defaultValue":"1" ,"description":"","d efinesFormat":false ,"key":"jdbcreadret rycount","required" :false}, {"defaultValue":"1 00000","descriptio n":"","definesForm at":false,"key":"cac heSize","required": false}, {"defaultValue":"1 0000","description" :"","definesFormat" :false,"key":"maxin queue","required":f alse}, {"defaultValue":"1 00000","descriptio n":"","definesForm at":false,"key":"ma xRowCount","requi red":false}, {"defaultValue":"6 00000","descriptio n":"","definesForm |  |
|  |  | at":false,"key":"bhc lientasynctimeout", "required":false}, |  |

实时计算（流计算） 参考

| 参数名称 | 类型 | {"defaultValue":"fa 示例 lse","description":"" | 说明 |
|---|---|---|---|
|  |  | ,"definesFormat":fa lse,"key":"enable d _ irect connect","req _ uired":false}, {"defaultValue":"1 00","description":"" ,"definesFormat":fa lse,"key":"rpcreque steveryfailures","re quired":false}, {"defaultValue":"fa lse","description":"" ,"definesFormat":fa lse,"key":"usebhcli entmode","require d":false}, {"defaultValue":"tr ue","description":"" ,"definesFormat":fa lse,"key":"enableth rottle","required":f alse}, {"defaultValue":"3" ,"description":"","d efinesFormat":false ,"key":"connections ize","required":fals e}, {"defaultValue":"0" ,"description":"","d efinesFormat":false ,"key":"jdbcreadtim eoutms","required" :false}, {"defaultValue":"1 0","description":""," definesFormat":fals e,"key":"jdbcretryc ount","required":fal se}, {"defaultValue":"E xception","descripti on":"","definesFor mat":false,"key":"a ctiononinsert","req uired":false}, {"defaultValue":"h ologres- fix","description":"" ,"definesFormat":fa lse,"key":"connecto r","required":true}, {"defaultValue":"", "description":"","de finesFormat":false, "key":"username"," required":false}, {"defaultValue":"1 0","description":""," definesFormat":fals e,"key":"bhclientre aderqueue","requir ed":false}, {"defaultValue":"1" ,"description":"","d |  |

实时计算（流计算） 参考

| 参数名称 | 类型 | efinesFormat":false 示例 ,"key":"maxconcurr | 说明 |
|---|---|---|---|
|  |  | encypershard","req uired":false}, {"defaultValue":"2 048","description": "","definesFormat": false,"key":"bhclien tasyncqueue","req uired":false}, {"defaultValue":"\\ u0002","descriptio n":"","definesForm at":false,"key":"arr aydelimiter","requir ed":false}, {"defaultValue":"2" ,"description":"","d efinesFormat":false ,"key":"bhclientwrit erbatch","required" :false}, {"defaultValue":"1 000","description": "","definesFormat": false,"key":"sqlretr yinterval","required ":false}, {"defaultValue":"9 0000","description" :"","definesFormat" :false,"key":"bhclie nttimeout","require d":false}, {"defaultValue":"2 097152","descripti on":"","definesFor mat":false,"key":"jd bcwritebatchbytesi ze","required":false }, {"defaultValue":"1 000","description": "","definesFormat": false,"key":"binlogr etryintervalms","re quired":false}, {"defaultValue":"fa lse","description":"" ,"definesFormat":fa lse,"key":"fieldnam etolower","required ":false}, {"defaultValue":"tr ue","description":"" ,"definesFormat":fa lse,"key":"ignorede lete","required":fal se}, {"defaultValue":"6 0000","description" :"","definesFormat" :false,"key":"storer pctimeout","requir ed":false}, {"defaultValue":"d efault","description |  |

实时计算（流计算） 参考

| 参数名称 | 类型 | ":"","definesFormat 示例 ":false,"key":"resou | 说明 |
|---|---|---|---|
| data | String | rce group","require _ d":false}, {"defaultValue":"1 00","description":"" ,"definesFormat":fa lse,"key":"clientpau se","required":false }, {"defaultValue":"in sertOrIgnore","desc ription":"","defines Format":false,"key" :"mutatetype","req uired":false}, {"defaultValue":"fa lse","description":"" ,"definesFormat":fa lse,"key":"disablebi nlog","required":fal se}, {"defaultValue":"A LL","description":"", "definesFormat":fal se,"key":"cache","r equired":false}, {"defaultValue":"", "description":"","de finesFormat":false, "key":"sink.paralleli sm","required":fals e}, {"defaultValue":"", "description":"","de finesFormat":false, "key":"jdbcbinlogsl otname","required" :false}, {"defaultValue":"1 00","description":"" ,"definesFormat":fa lse,"key":"asyncca pacity","required":f alse}, {"defaultValue":"1 00","description":"" ,"definesFormat":fa lse,"key":"cacheSc anLimit","required" :false}, {"defaultValue":"2 0971520","descript ion":"","definesFor mat":false,"key":"jd bcwritebatchtotalb ytesize","required": false}, {"defaultValue":"5" ,"description":"","d efinesFormat":false ,"key":"rpcretries"," required":false}, {"defaultValue":"1 024","description": "","definesFormat": false,"key":"bhclien | 自定义connector解析详细信息。 |

实时计算（流计算） 参考

| 参数名称 | 类型 | treaderbatch","req 示例 uired":false}, | 说明 |
|---|---|---|---|
|  |  | {"defaultValue":"6 0000","description" :"","definesFormat" :false,"key":"jdbcm etacachettl","requir ed":false}, {"defaultValue":"tr ue","description":"" ,"definesFormat":fa lse,"key":"splitstrat egy","required":fals e}, {"defaultValue":"fa lse","description":"" ,"definesFormat":fa lse,"key":"partitionr outer","required":fa lse}, {"defaultValue":"", "description":"","de finesFormat":false, "key":"connectionp oolname","required ":false}, {"defaultValue":"6 0000","description" :"","definesFormat" :false,"key":"jdbcco nnectionmaxidlems ","required":false}, {"defaultValue":"", "description":"","de finesFormat":false, "key":"dbname","re quired":true}, {"defaultValue":"fa lse","description":"" ,"definesFormat":fa lse,"key":"enablety penormalization","r equired":false}, {"defaultValue":"2 62144","descriptio n":"","definesForm at":false,"key":"spli tdatasize","require d":false}, {"defaultValue":"6 0000","description" :"","definesFormat" :false,"key":"binlog requesttimeoutms" ,"required":false}, {"defaultValue":"3 2","description":""," definesFormat":fals e,"key":"splitlength ","required":false}, {"defaultValue":"1 80000","descriptio n":"","definesForm at":false,"key":"asy nctimeoutms","req uired":false}, {"defaultValue":"bi |  |

实时计算（流计算） 参考

| 参数名称 | 类型 | nary","description": 示例 "","definesFormat": | 说明 |
|---|---|---|---|
|  |  | false,"key":"jdbcco pyformat","require d":false}, {"defaultValue":"5 000","description": "","definesFormat": false,"key":"jdbcret rysleepstepms","re quired":false}, {"defaultValue":"", "description":"","de finesFormat":false, "key":"userpcmode ","required":false}, {"defaultValue":"fa lse","description":"" ,"definesFormat":fa lse,"key":"cdcmode ","required":false}, {"defaultValue":"tr ue","description":"" ,"definesFormat":fa lse,"key":"enableBi naryCache","requir ed":false}, {"defaultValue":"1 0000","description" :"","definesFormat" :false,"key":"jdbcwr iteflushinterval","re quired":false}, {"defaultValue":"1 00","description":"" ,"definesFormat":fa lse,"key":"shardrpc retries","required":f alse}, {"defaultValue":"fa lse","description":"" ,"definesFormat":fa lse,"key":"partial- insert.enabled","re quired":false}, {"defaultValue":"6 0","description":""," definesFormat":fals e,"key":"jdbcscanti meoutseconds","re quired":false}, {"defaultValue":"fa lse","description":"" ,"definesFormat":fa lse,"key":"insertoru pdate","required":f alse}, {"defaultValue":"1 000","description": "","definesFormat": false,"key":"scanba tchsize","required": false}, {"defaultValue":"1" ,"description":"","d efinesFormat":false ,"key":"asynccallba |  |

实时计算（流计算） 参考

| 参数名称 | 类型 | ckpool","required":f 示例 alse}, | 说明 |
|---|---|---|---|
|  |  | {"defaultValue":":", "description":"","de finesFormat":false, "key":"primarykeys ep","required":false }, {"defaultValue":"fa lse","description":"" ,"definesFormat":fa lse,"key":"createpa rttable","required": false}, {"defaultValue":"fa lse","description":"" ,"definesFormat":fa lse,"key":"reportme trics","required":fal se}, {"defaultValue":"", "description":"","de finesFormat":false, "key":"starttime","r equired":false}, {"defaultValue":"fa lse","description":"" ,"definesFormat":fa lse,"key":"useholoh ubmode","required ":false}, {"defaultValue":"u nordered","descript ion":"","definesFor mat":false,"key":"a syncresultorder","r equired":false}, {"defaultValue":"2 56","description":"" ,"definesFormat":fa lse,"key":"jdbcread batchqueuesize","r equired":false}, {"defaultValue":"- 1","description":""," definesFormat":fals e,"key":"jdbcmetaa utorefreshfactor","r equired":false}, {"defaultValue":"1 0","description":""," definesFormat":fals e,"key":"binlogmax retrytimes","requir ed":false}, {"defaultValue":"n one","description": "","definesFormat": false,"key":"sdkmo de","required":false }, {"defaultValue":"9 223372036854775 807","description": "","definesFormat": false,"key":"cacheT TLMs","required":fa |  |

实时计算（流计算） 参考

| 参数名称 | 类型 | lse}, 示例 {"defaultValue":"fa | 说明 |
|---|---|---|---|
|  |  | lse","description":"" ,"definesFormat":fa lse,"key":"upsertso urce","required":fal se}, {"defaultValue":"fa lse","description":"" ,"definesFormat":fa lse,"key":"bhclienti gnoredelete","requi red":false}, {"defaultValue":"fa lse","description":"" ,"definesFormat":fa lse,"key":"remove- u0000-in- text.enabled","requ ired":false}, {"defaultValue":"e arliestOffset","desc ription":"","defines Format":false,"key" :"binlogstartupmod e","required":false} , {"defaultValue":"1 00","description":"" ,"definesFormat":fa lse,"key":"sqlretries ","required":false}, {"defaultValue":"fa lse","description":"" ,"definesFormat":fa lse,"key":"supportc olumnstorageforma t","required":false} , {"defaultValue":"1 0","description":""," definesFormat":fals e,"key":"channelthr eadcount","require d":false}, {"defaultValue":"fa lse","description":"" ,"definesFormat":fa lse,"key":"ignorenu llwhenupdate","req uired":false}, {"defaultValue":"st ream","description" :"","definesFormat" :false,"key":" tabl __ ename ","require __ d":false}, {"defaultValue":"", "description":"","de finesFormat":false, "key":"nullvalues"," required":false}, {"defaultValue":"", "description":"","de finesFormat":false, "key":"endpoint","r equired":true}, |  |

实时计算（流计算） 参考

| 参数名称 | 类型 | {"defaultValue":"1 示例 0000","description" | 说明 |
|---|---|---|---|
|  |  | :"","definesFormat" :false,"key":"refres hinterval","require d":false}, {"defaultValue":"\\ u0002","descriptio n":"","definesForm at":false,"key":"fiel d delimiter","requir _ ed":false}, {"defaultValue":"fa lse","description":"" ,"definesFormat":fa lse,"key":"enable fi _ lter push down","r _ _ equired":false}, {"defaultValue":"", "description":"","de finesFormat":false, "key":"tablename", "required":true}, {"defaultValue":"tr ue","description":"" ,"definesFormat":fa lse,"key":"cacheEm pty","required":fals e}, {"defaultValue":"p ublic","description" :"","definesFormat" :false,"key":"schem aname","required": false}, {"defaultValue":"6 00","description":"" ,"definesFormat":fa lse,"key":"jdbcscan transactionsessiont imeoutseconds","re quired":false}],"pa ckaged":false,"dep endencies": ["hdfs:///vvp/data/s ql- artifacts/namespac es/flinkteam/custo m- connectors/2024- 03-12T01-50- 56.079896Z/verver ica-connector- hologres-1.15-vvr- 6.0- fix.jar"]}],"@type":" type.googleapis.co m/vvp.sql.v1beta1. AnalyzeConnectorJ arsResponse","dupl icatedSourceFactor iesConnectors": [],"duplicatedSinkF |  |
| requestId | String | actoriesConnectors 05AEEA60-8B59- ":[]} 4CCD-9F35- B27EE47F4D4E | 请求ID。 |

实时计算（流计算） 参考

**示例**

请求示例

```json
POST /pop/workspaces/[workspace]/sql/v1beta1/namespaces/[namespace]/connectors:analyzejars HTTP/1.1 { "RegionId":"cn-wulan-env***-d01", "workspace":"default", "namespace":"flinkteam" }
```

正常返回示例 `JSON` 格式

```json
{
 "data":"{\"connectors\":[{\"lookup\":false,\"supportedFormats\":[],\"environments\":[]
,\"sink\":true,\"name\":\"namespaces/flinkteam/connectors/hologresfix\",\"source\":true,\"type\":\"hologres-fix\",\"properties\": [{\"defaultValue\":\"10\",\"description\":\"\",\"definesFormat\":false,\"key\":\"poolsize\ \"required\":false}, {\"defaultValue\":\"false\",\"description\":\"\",\"definesFormat\":false,\"key\":\"async\" "required\":false}, {\"defaultValue\":\"\",\"description\":\"\",\"definesFormat\":false,\"key\":\"cacheReloadT eBlackList\",\"required\":false}, {\"defaultValue\":\"\",\"description\":\"\",\"definesFormat\":false,\"key\":\"password\",\ equired\":false}, {\"defaultValue\":\"false\",\"description\":\"\",\"definesFormat\":false,\"key\":\"bhclien gnorebeforeupdate\",\"required\":false}, {\"defaultValue\":\"1000\",\"description\":\"\",\"definesFormat\":false,\"key\":\"jdbcretr leepinitms\",\"required\":false}, {\"defaultValue\":\"false\",\"description\":\"\",\"definesFormat\":false,\"key\":\"inserti otexists\",\"required\":false}, {\"defaultValue\":\"256\",\"description\":\"\",\"definesFormat\":false,\"key\":\"jdbcscanf chsize\",\"required\":false},{\"defaultValue\":\"- 1\",\"description\":\"\",\"definesFormat\":false,\"key\":\"starttimems\",\"required\":fals
```

,

```
{\"defaultValue\":\"true\",\"description\":\"\",\"definesFormat\":false,\"key\":\"jdbcenab defaultfornotnullcolumn\",\"required\":false}, {\"defaultValue\":\"false\",\"description\":\"\",\"definesFormat\":false,\"key\":\"binlog\ \"required\":false}, {\"defaultValue\":\"100\",\"description\":\"\",\"definesFormat\":false,\"key\":\"binlogbat readsize\",\"required\":false}, {\"defaultValue\":\"500\",\"description\":\"\",\"definesFormat\":false,\"key\":\"clientmax use\",\"required\":false}, {\"defaultValue\":\"2\",\"description\":\"\",\"definesFormat\":false,\"key\":\"errorcount\ \"required\":false}, {\"defaultValue\":\"256\",\"description\":\"\",\"definesFormat\":false,\"key\":\"jdbcwrite tchsize\",\"required\":false}, {\"defaultValue\":\"false\",\"description\":\"\",\"definesFormat\":false,\"key\":\"jdbcuse gacyputhandler\",\"required\":false}, {\"defaultValue\":\"128\",\"description\":\"\",\"definesFormat\":false,\"key\":\"jdbcreadb chsize\",\"required\":false}, {\"defaultValue\":\"4\",\"description\":\"\",\"definesFormat\":false,\"key\":\"bhclientthr
```

实时计算（流计算） 参考

```
dpool\",\"required\":false}, {\"defaultValue\":\"1\",\"description\":\"\",\"definesFormat\":false,\"key\":\"jdbcreadret count\",\"required\":false}, {\"defaultValue\":\"100000\",\"description\":\"\",\"definesFormat\":false,\"key\":\"cacheS e\",\"required\":false}, {\"defaultValue\":\"10000\",\"description\":\"\",\"definesFormat\":false,\"key\":\"maxinqu e\",\"required\":false}, {\"defaultValue\":\"100000\",\"description\":\"\",\"definesFormat\":false,\"key\":\"maxRow unt\",\"required\":false}, {\"defaultValue\":\"600000\",\"description\":\"\",\"definesFormat\":false,\"key\":\"bhclie asynctimeout\",\"required\":false}, {\"defaultValue\":\"false\",\"description\":\"\",\"definesFormat\":false,\"key\":\"enable_ rect_connect\",\"required\":false}, {\"defaultValue\":\"100\",\"description\":\"\",\"definesFormat\":false,\"key\":\"rpcreques veryfailures\",\"required\":false}, {\"defaultValue\":\"false\",\"description\":\"\",\"definesFormat\":false,\"key\":\"usebhcl ntmode\",\"required\":false}, {\"defaultValue\":\"true\",\"description\":\"\",\"definesFormat\":false,\"key\":\"enableth ttle\",\"required\":false}, {\"defaultValue\":\"3\",\"description\":\"\",\"definesFormat\":false,\"key\":\"connections e\",\"required\":false}, {\"defaultValue\":\"0\",\"description\":\"\",\"definesFormat\":false,\"key\":\"jdbcreadtim utms\",\"required\":false}, {\"defaultValue\":\"10\",\"description\":\"\",\"definesFormat\":false,\"key\":\"jdbcretryc nt\",\"required\":false}, {\"defaultValue\":\"Exception\",\"description\":\"\",\"definesFormat\":false,\"key\":\"act noninsert\",\"required\":false},{\"defaultValue\":\"hologresfix\",\"description\":\"\",\"definesFormat\":false,\"key\":\"connector\",\"required\":true {\"defaultValue\":\"\",\"description\":\"\",\"definesFormat\":false,\"key\":\"username\",\ equired\":false}, {\"defaultValue\":\"10\",\"description\":\"\",\"definesFormat\":false,\"key\":\"bhclientre erqueue\",\"required\":false}, {\"defaultValue\":\"1\",\"description\":\"\",\"definesFormat\":false,\"key\":\"maxconcurre ypershard\",\"required\":false}, {\"defaultValue\":\"2048\",\"description\":\"\",\"definesFormat\":false,\"key\":\"bhclient yncqueue\",\"required\":false}, {\"defaultValue\":\"\\\\u0002\",\"description\":\"\",\"definesFormat\":false,\"key\":\"arr delimiter\",\"required\":false}, {\"defaultValue\":\"2\",\"description\":\"\",\"definesFormat\":false,\"key\":\"bhclientwri rbatch\",\"required\":false}, {\"defaultValue\":\"1000\",\"description\":\"\",\"definesFormat\":false,\"key\":\"sqlretry terval\",\"required\":false}, {\"defaultValue\":\"90000\",\"description\":\"\",\"definesFormat\":false,\"key\":\"bhclien imeout\",\"required\":false}, {\"defaultValue\":\"2097152\",\"description\":\"\",\"definesFormat\":false,\"key\":\"jdbcw tebatchbytesize\",\"required\":false}, {\"defaultValue\":\"1000\",\"description\":\"\",\"definesFormat\":false,\"key\":\"binlogre yintervalms\",\"required\":false}, {\"defaultValue\":\"false\",\"description\":\"\",\"definesFormat\":false,\"key\":\"fieldna tolower\",\"required\":false}, {\"defaultValue\":\"true\",\"description\":\"\",\"definesFormat\":false,\"key\":\"ignorede te\",\"required\":false}, {\"defaultValue\":\"60000\",\"description\":\"\",\"definesFormat\":false,\"key\":\"storerp imeout\",\"required\":false}, {\"defaultValue\":\"default\",\"description\":\"\",\"definesFormat\":false,\"key\":\"resou
```

实时计算（流计算） 参考

```
{\defaultValue\:\default\,\description\:\\,\definesFormat\:false,\key\:\resou e_group\",\"required\":false}, {\"defaultValue\":\"100\",\"description\":\"\",\"definesFormat\":false,\"key\":\"clientpau \",\"required\":false}, {\"defaultValue\":\"insertOrIgnore\",\"description\":\"\",\"definesFormat\":false,\"key\" mutatetype\",\"required\":false}, {\"defaultValue\":\"false\",\"description\":\"\",\"definesFormat\":false,\"key\":\"disable nlog\",\"required\":false}, {\"defaultValue\":\"ALL\",\"description\":\"\",\"definesFormat\":false,\"key\":\"cache\",\ equired\":false}, {\"defaultValue\":\"\",\"description\":\"\",\"definesFormat\":false,\"key\":\"sink.paralle sm\",\"required\":false}, {\"defaultValue\":\"\",\"description\":\"\",\"definesFormat\":false,\"key\":\"jdbcbinlogsl name\",\"required\":false}, {\"defaultValue\":\"100\",\"description\":\"\",\"definesFormat\":false,\"key\":\"asynccapa ty\",\"required\":false}, {\"defaultValue\":\"100\",\"description\":\"\",\"definesFormat\":false,\"key\":\"cacheScan mit\",\"required\":false}, {\"defaultValue\":\"20971520\",\"description\":\"\",\"definesFormat\":false,\"key\":\"jdbc itebatchtotalbytesize\",\"required\":false}, {\"defaultValue\":\"5\",\"description\":\"\",\"definesFormat\":false,\"key\":\"rpcretries\ \"required\":false}, {\"defaultValue\":\"1024\",\"description\":\"\",\"definesFormat\":false,\"key\":\"bhclient aderbatch\",\"required\":false}, {\"defaultValue\":\"60000\",\"description\":\"\",\"definesFormat\":false,\"key\":\"jdbcmet achettl\",\"required\":false}, {\"defaultValue\":\"true\",\"description\":\"\",\"definesFormat\":false,\"key\":\"splitstr egy\",\"required\":false}, {\"defaultValue\":\"false\",\"description\":\"\",\"definesFormat\":false,\"key\":\"partiti router\",\"required\":false}, {\"defaultValue\":\"\",\"description\":\"\",\"definesFormat\":false,\"key\":\"connectionpo name\",\"required\":false}, {\"defaultValue\":\"60000\",\"description\":\"\",\"definesFormat\":false,\"key\":\"jdbccon ctionmaxidlems\",\"required\":false}, {\"defaultValue\":\"\",\"description\":\"\",\"definesFormat\":false,\"key\":\"dbname\",\"r uired\":true}, {\"defaultValue\":\"false\",\"description\":\"\",\"definesFormat\":false,\"key\":\"enablet enormalization\",\"required\":false}, {\"defaultValue\":\"262144\",\"description\":\"\",\"definesFormat\":false,\"key\":\"splitd asize\",\"required\":false}, {\"defaultValue\":\"60000\",\"description\":\"\",\"definesFormat\":false,\"key\":\"binlogr uesttimeoutms\",\"required\":false}, {\"defaultValue\":\"32\",\"description\":\"\",\"definesFormat\":false,\"key\":\"splitlengt ",\"required\":false}, {\"defaultValue\":\"180000\",\"description\":\"\",\"definesFormat\":false,\"key\":\"asynct eoutms\",\"required\":false}, {\"defaultValue\":\"binary\",\"description\":\"\",\"definesFormat\":false,\"key\":\"jdbcco format\",\"required\":false}, {\"defaultValue\":\"5000\",\"description\":\"\",\"definesFormat\":false,\"key\":\"jdbcretr leepstepms\",\"required\":false}, {\"defaultValue\":\"\",\"description\":\"\",\"definesFormat\":false,\"key\":\"userpcmode\" "required\":false}, {\"defaultValue\":\"false\",\"description\":\"\",\"definesFormat\":false,\"key\":\"cdcmode ,\"required\":false}, {\"defaultValue\":\"true\",\"description\":\"\",\"definesFormat\":false,\"key\":\"enableBi
```

实时计算（流计算） 参考

```
ryCache\",\"required\":false}, {\"defaultValue\":\"10000\",\"description\":\"\",\"definesFormat\":false,\"key\":\"jdbcwri flushinterval\",\"required\":false}, {\"defaultValue\":\"100\",\"description\":\"\",\"definesFormat\":false,\"key\":\"shardrpcr ries\",\"required\":false}, {\"defaultValue\":\"false\",\"description\":\"\",\"definesFormat\":false,\"key\":\"partial insert.enabled\",\"required\":false}, {\"defaultValue\":\"60\",\"description\":\"\",\"definesFormat\":false,\"key\":\"jdbcscanti outseconds\",\"required\":false}, {\"defaultValue\":\"false\",\"description\":\"\",\"definesFormat\":false,\"key\":\"inserto pdate\",\"required\":false}, {\"defaultValue\":\"1000\",\"description\":\"\",\"definesFormat\":false,\"key\":\"scanbatc ize\",\"required\":false}, {\"defaultValue\":\"1\",\"description\":\"\",\"definesFormat\":false,\"key\":\"asynccallba pool\",\"required\":false}, {\"defaultValue\":\":\",\"description\":\"\",\"definesFormat\":false,\"key\":\"primarykeys \",\"required\":false}, {\"defaultValue\":\"false\",\"description\":\"\",\"definesFormat\":false,\"key\":\"createp ttable\",\"required\":false}, {\"defaultValue\":\"false\",\"description\":\"\",\"definesFormat\":false,\"key\":\"reportm rics\",\"required\":false}, {\"defaultValue\":\"\",\"description\":\"\",\"definesFormat\":false,\"key\":\"starttime\", required\":false}, {\"defaultValue\":\"false\",\"description\":\"\",\"definesFormat\":false,\"key\":\"useholo bmode\",\"required\":false}, {\"defaultValue\":\"unordered\",\"description\":\"\",\"definesFormat\":false,\"key\":\"asy resultorder\",\"required\":false}, {\"defaultValue\":\"256\",\"description\":\"\",\"definesFormat\":false,\"key\":\"jdbcreadb chqueuesize\",\"required\":false},{\"defaultValue\":\"- 1\",\"description\":\"\",\"definesFormat\":false,\"key\":\"jdbcmetaautorefreshfactor\",\"r uired\":false}, {\"defaultValue\":\"10\",\"description\":\"\",\"definesFormat\":false,\"key\":\"binlogmaxr rytimes\",\"required\":false}, {\"defaultValue\":\"none\",\"description\":\"\",\"definesFormat\":false,\"key\":\"sdkmode\ \"required\":false}, {\"defaultValue\":\"9223372036854775807\",\"description\":\"\",\"definesFormat\":false,\"k \":\"cacheTTLMs\",\"required\":false}, {\"defaultValue\":\"false\",\"description\":\"\",\"definesFormat\":false,\"key\":\"upserts rce\",\"required\":false}, {\"defaultValue\":\"false\",\"description\":\"\",\"definesFormat\":false,\"key\":\"bhclien gnoredelete\",\"required\":false}, {\"defaultValue\":\"false\",\"description\":\"\",\"definesFormat\":false,\"key\":\"removeu0000-in-text.enabled\",\"required\":false}, {\"defaultValue\":\"earliestOffset\",\"description\":\"\",\"definesFormat\":false,\"key\" binlogstartupmode\",\"required\":false}, {\"defaultValue\":\"100\",\"description\":\"\",\"definesFormat\":false,\"key\":\"sqlretrie ",\"required\":false}, {\"defaultValue\":\"false\",\"description\":\"\",\"definesFormat\":false,\"key\":\"support lumnstorageformat\",\"required\":false}, {\"defaultValue\":\"10\",\"description\":\"\",\"definesFormat\":false,\"key\":\"channelthr dcount\",\"required\":false}, {\"defaultValue\":\"false\",\"description\":\"\",\"definesFormat\":false,\"key\":\"ignoren lwhenupdate\",\"required\":false}, {\"defaultValue\":\"stream\",\"description\":\"\",\"definesFormat\":false,\"key\":\"__tabl ame \"\"required\":false}
```

实时计算（流计算） 参考

```json
ame__\",\"required\":false}, {\"defaultValue\":\"\",\"description\":\"\",\"definesFormat\":false,\"key\":\"nullvalues\" "required\":false}, {\"defaultValue\":\"\",\"description\":\"\",\"definesFormat\":false,\"key\":\"endpoint\",\ equired\":true}, {\"defaultValue\":\"10000\",\"description\":\"\",\"definesFormat\":false,\"key\":\"refresh terval\",\"required\":false}, {\"defaultValue\":\"\\\\u0002\",\"description\":\"\",\"definesFormat\":false,\"key\":\"fie _delimiter\",\"required\":false}, {\"defaultValue\":\"false\",\"description\":\"\",\"definesFormat\":false,\"key\":\"enable_ lter_push_down\",\"required\":false}, {\"defaultValue\":\"\",\"description\":\"\",\"definesFormat\":false,\"key\":\"tablename\", required\":true}, {\"defaultValue\":\"true\",\"description\":\"\",\"definesFormat\":false,\"key\":\"cacheEmp \",\"required\":false}, {\"defaultValue\":\"public\",\"description\":\"\",\"definesFormat\":false,\"key\":\"schema me\",\"required\":false}, {\"defaultValue\":\"600\",\"description\":\"\",\"definesFormat\":false,\"key\":\"jdbcscant nsactionsessiontimeoutseconds\",\"required\":false}],\"packaged\":false,\"dependencies\": [\"hdfs:///vvp/data/sql-artifacts/namespaces/flinkteam/custom-connectors/2024-03-12T01-5 0-56.079896Z/ververica-connector-hologres-1.15-vvr-6.0fix.jar\"]}],\"@type\":\"type.googleapis.com/vvp.sql.v1beta1.AnalyzeConnectorJarsResponse\ \"duplicatedSourceFactoriesConnectors\":[],\"duplicatedSinkFactoriesConnectors\":[]}",
 "success":true,
 "requestId":"05AEEA60-8B59-4CCD-9F35-B27EE47F4D4E"
}
```

`XML` 格式

```xml
<data>{&quot;connectors&quot;:[{&quot;lookup&quot;:false,&quot;supportedFormats&quot;: [],&quot;environments&quot;: [],&quot;sink&quot;:true,&quot;name&quot;:&quot;namespaces/flinkteam/connectors/hologresfix&quot;,&quot;source&quot;:true,&quot;type&quot;:&quot;hologresfix&quot;,&quot;properties&quot;: [{&quot;defaultValue&quot;:&quot;10&quot;,&quot;description&quot;:&quot;&quot;,&quot;defin Format&quot;:false,&quot;key&quot;:&quot;poolsize&quot;,&quot;required&quot;:false}, {&quot;defaultValue&quot;:&quot;false&quot;,&quot;description&quot;:&quot;&quot;,&quot;def esFormat&quot;:false,&quot;key&quot;:&quot;async&quot;,&quot;required&quot;:false}, {&quot;defaultValue&quot;:&quot;&quot;,&quot;description&quot;:&quot;&quot;,&quot;definesF mat&quot;:false,&quot;key&quot;:&quot;cacheReloadTimeBlackList&quot;,&quot;required&quot; lse}, {&quot;defaultValue&quot;:&quot;&quot;,&quot;description&quot;:&quot;&quot;,&quot;definesF mat&quot;:false,&quot;key&quot;:&quot;password&quot;,&quot;required&quot;:false}, {&quot;defaultValue&quot;:&quot;false&quot;,&quot;description&quot;:&quot;&quot;,&quot;def esFormat&quot;:false,&quot;key&quot;:&quot;bhclientignorebeforeupdate&quot;,&quot;required uot;:false}, {&quot;defaultValue&quot;:&quot;1000&quot;,&quot;description&quot;:&quot;&quot;,&quot;defi sFormat&quot;:false,&quot;key&quot;:&quot;jdbcretrysleepinitms&quot;,&quot;required&quot; lse}, {&quot;defaultValue&quot;:&quot;false&quot;,&quot;description&quot;:&quot;&quot;,&quot;def esFormat&quot;:false,&quot;key&quot;:&quot;insertifnotexists&quot;,&quot;required&quot;:fa e}, {&quot;defaultValue&quot;:&quot;256&quot;,&quot;description&quot;:&quot;&quot;,&quot;defin Format&quot;:false,&quot;key&quot;:&quot;jdbcscanfetchsize&quot;,&quot;required&quot;:fals {&qotdefaltVale&qot &qot
```

实时计算（流计算） 参考

```
,{&quot;defaultValue&quot;:&quot;- 1&quot;,&quot;description&quot;:&quot;&quot;,&quot;definesFormat&quot;:false,&quot;key&quo :&quot;starttimems&quot;,&quot;required&quot;:false}, {&quot;defaultValue&quot;:&quot;true&quot;,&quot;description&quot;:&quot;&quot;,&quot;defi sFormat&quot;:false,&quot;key&quot;:&quot;jdbcenabledefaultfornotnullcolumn&quot;,&quot;re ired&quot;:false}, {&quot;defaultValue&quot;:&quot;false&quot;,&quot;description&quot;:&quot;&quot;,&quot;def esFormat&quot;:false,&quot;key&quot;:&quot;binlog&quot;,&quot;required&quot;:false}, {&quot;defaultValue&quot;:&quot;100&quot;,&quot;description&quot;:&quot;&quot;,&quot;defin Format&quot;:false,&quot;key&quot;:&quot;binlogbatchreadsize&quot;,&quot;required&quot;:fa e}, {&quot;defaultValue&quot;:&quot;500&quot;,&quot;description&quot;:&quot;&quot;,&quot;defin Format&quot;:false,&quot;key&quot;:&quot;clientmaxpause&quot;,&quot;required&quot;:false}, {&quot;defaultValue&quot;:&quot;2&quot;,&quot;description&quot;:&quot;&quot;,&quot;defines rmat&quot;:false,&quot;key&quot;:&quot;errorcount&quot;,&quot;required&quot;:false}, {&quot;defaultValue&quot;:&quot;256&quot;,&quot;description&quot;:&quot;&quot;,&quot;defin Format&quot;:false,&quot;key&quot;:&quot;jdbcwritebatchsize&quot;,&quot;required&quot;:fal }, {&quot;defaultValue&quot;:&quot;false&quot;,&quot;description&quot;:&quot;&quot;,&quot;def esFormat&quot;:false,&quot;key&quot;:&quot;jdbcuselegacyputhandler&quot;,&quot;required&qu ;:false}, {&quot;defaultValue&quot;:&quot;128&quot;,&quot;description&quot;:&quot;&quot;,&quot;defin Format&quot;:false,&quot;key&quot;:&quot;jdbcreadbatchsize&quot;,&quot;required&quot;:fals
```

,

```
{&quot;defaultValue&quot;:&quot;4&quot;,&quot;description&quot;:&quot;&quot;,&quot;defines rmat&quot;:false,&quot;key&quot;:&quot;bhclientthreadpool&quot;,&quot;required&quot;:false {&quot;defaultValue&quot;:&quot;1&quot;,&quot;description&quot;:&quot;&quot;,&quot;defines rmat&quot;:false,&quot;key&quot;:&quot;jdbcreadretrycount&quot;,&quot;required&quot;:false {&quot;defaultValue&quot;:&quot;100000&quot;,&quot;description&quot;:&quot;&quot;,&quot;de nesFormat&quot;:false,&quot;key&quot;:&quot;cacheSize&quot;,&quot;required&quot;:false}, {&quot;defaultValue&quot;:&quot;10000&quot;,&quot;description&quot;:&quot;&quot;,&quot;def esFormat&quot;:false,&quot;key&quot;:&quot;maxinqueue&quot;,&quot;required&quot;:false}, {&quot;defaultValue&quot;:&quot;100000&quot;,&quot;description&quot;:&quot;&quot;,&quot;de nesFormat&quot;:false,&quot;key&quot;:&quot;maxRowCount&quot;,&quot;required&quot;:false}, {&quot;defaultValue&quot;:&quot;600000&quot;,&quot;description&quot;:&quot;&quot;,&quot;de nesFormat&quot;:false,&quot;key&quot;:&quot;bhclientasynctimeout&quot;,&quot;required&quot false}, {&quot;defaultValue&quot;:&quot;false&quot;,&quot;description&quot;:&quot;&quot;,&quot;def esFormat&quot;:false,&quot;key&quot;:&quot;enable_direct_connect&quot;,&quot;required&quot false}, {&quot;defaultValue&quot;:&quot;100&quot;,&quot;description&quot;:&quot;&quot;,&quot;defin Format&quot;:false,&quot;key&quot;:&quot;rpcrequesteveryfailures&quot;,&quot;required&quot false}, {&quot;defaultValue&quot;:&quot;false&quot;,&quot;description&quot;:&quot;&quot;,&quot;def esFormat&quot;:false,&quot;key&quot;:&quot;usebhclientmode&quot;,&quot;required&quot;:fals
```

,

```
{&quot;defaultValue&quot;:&quot;true&quot;,&quot;description&quot;:&quot;&quot;,&quot;defi sFormat&quot;:false,&quot;key&quot;:&quot;enablethrottle&quot;,&quot;required&quot;:false {&quot;defaultValue&quot;:&quot;3&quot;,&quot;description&quot;:&quot;&quot;,&quot;defines rmat&quot;:false,&quot;key&quot;:&quot;connectionsize&quot;,&quot;required&quot;:false}, {&quot;defaultValue&quot;:&quot;0&quot;,&quot;description&quot;:&quot;&quot;,&quot;defines rmat&quot;:false,&quot;key&quot;:&quot;jdbcreadtimeoutms&quot;,&quot;required&quot;:false {&quot;defaultValue&quot;:&quot;10&quot;,&quot;description&quot;:&quot;&quot;,&quot;define ormat&quot;:false,&quot;key&quot;:&quot;jdbcretrycount&quot;,&quot;required&quot;:false}, {&quot;defaultValue&quot;:&quot;Exception&quot;,&quot;description&quot;:&quot;&quot;,&quot
```

实时计算（流计算） 参考

```
efinesFormat&quot;:false,&quot;key&quot;:&quot;actiononinsert&quot;,&quot;required&quot;:f se},{&quot;defaultValue&quot;:&quot;hologresfix&quot;,&quot;description&quot;:&quot;&quot;,&quot;definesFormat&quot;:false,&quot;key&q t;:&quot;connector&quot;,&quot;required&quot;:true}, {&quot;defaultValue&quot;:&quot;&quot;,&quot;description&quot;:&quot;&quot;,&quot;definesF mat&quot;:false,&quot;key&quot;:&quot;username&quot;,&quot;required&quot;:false}, {&quot;defaultValue&quot;:&quot;10&quot;,&quot;description&quot;:&quot;&quot;,&quot;define ormat&quot;:false,&quot;key&quot;:&quot;bhclientreaderqueue&quot;,&quot;required&quot;:fal }, {&quot;defaultValue&quot;:&quot;1&quot;,&quot;description&quot;:&quot;&quot;,&quot;defines rmat&quot;:false,&quot;key&quot;:&quot;maxconcurrencypershard&quot;,&quot;required&quot;:f se}, {&quot;defaultValue&quot;:&quot;2048&quot;,&quot;description&quot;:&quot;&quot;,&quot;defi sFormat&quot;:false,&quot;key&quot;:&quot;bhclientasyncqueue&quot;,&quot;required&quot;:fa e}, {&quot;defaultValue&quot;:&quot;\\u0002&quot;,&quot;description&quot;:&quot;&quot;,&quot;d inesFormat&quot;:false,&quot;key&quot;:&quot;arraydelimiter&quot;,&quot;required&quot;:fal }, {&quot;defaultValue&quot;:&quot;2&quot;,&quot;description&quot;:&quot;&quot;,&quot;defines rmat&quot;:false,&quot;key&quot;:&quot;bhclientwriterbatch&quot;,&quot;required&quot;:fals
```

,

```
{&quot;defaultValue&quot;:&quot;1000&quot;,&quot;description&quot;:&quot;&quot;,&quot;defi sFormat&quot;:false,&quot;key&quot;:&quot;sqlretryinterval&quot;,&quot;required&quot;:fals
```

,

```
{&quot;defaultValue&quot;:&quot;90000&quot;,&quot;description&quot;:&quot;&quot;,&quot;def esFormat&quot;:false,&quot;key&quot;:&quot;bhclienttimeout&quot;,&quot;required&quot;:fals
```

,

```
{&quot;defaultValue&quot;:&quot;2097152&quot;,&quot;description&quot;:&quot;&quot;,&quot;d inesFormat&quot;:false,&quot;key&quot;:&quot;jdbcwritebatchbytesize&quot;,&quot;required&q t;:false}, {&quot;defaultValue&quot;:&quot;1000&quot;,&quot;description&quot;:&quot;&quot;,&quot;defi sFormat&quot;:false,&quot;key&quot;:&quot;binlogretryintervalms&quot;,&quot;required&quot; alse}, {&quot;defaultValue&quot;:&quot;false&quot;,&quot;description&quot;:&quot;&quot;,&quot;def esFormat&quot;:false,&quot;key&quot;:&quot;fieldnametolower&quot;,&quot;required&quot;:fal }, {&quot;defaultValue&quot;:&quot;true&quot;,&quot;description&quot;:&quot;&quot;,&quot;defi sFormat&quot;:false,&quot;key&quot;:&quot;ignoredelete&quot;,&quot;required&quot;:false}, {&quot;defaultValue&quot;:&quot;60000&quot;,&quot;description&quot;:&quot;&quot;,&quot;def esFormat&quot;:false,&quot;key&quot;:&quot;storerpctimeout&quot;,&quot;required&quot;:fals
```

,

```
{&quot;defaultValue&quot;:&quot;default&quot;,&quot;description&quot;:&quot;&quot;,&quot;d inesFormat&quot;:false,&quot;key&quot;:&quot;resource_group&quot;,&quot;required&quot;:fal }, {&quot;defaultValue&quot;:&quot;100&quot;,&quot;description&quot;:&quot;&quot;,&quot;defin Format&quot;:false,&quot;key&quot;:&quot;clientpause&quot;,&quot;required&quot;:false}, {&quot;defaultValue&quot;:&quot;insertOrIgnore&quot;,&quot;description&quot;:&quot;&quot;, uot;definesFormat&quot;:false,&quot;key&quot;:&quot;mutatetype&quot;,&quot;required&quot; lse}, {&quot;defaultValue&quot;:&quot;false&quot;,&quot;description&quot;:&quot;&quot;,&quot;def esFormat&quot;:false,&quot;key&quot;:&quot;disablebinlog&quot;,&quot;required&quot;:false {&quot;defaultValue&quot;:&quot;ALL&quot;,&quot;description&quot;:&quot;&quot;,&quot;defin Format&quot;:false,&quot;key&quot;:&quot;cache&quot;,&quot;required&quot;:false}, {&quot;defaultValue&quot;:&quot;&quot;,&quot;description&quot;:&quot;&quot;,&quot;definesF
```

实时计算（流计算） 参考

```
mat&quot;:false,&quot;key&quot;:&quot;sink.parallelism&quot;,&quot;required&quot;:false}, {&quot;defaultValue&quot;:&quot;&quot;,&quot;description&quot;:&quot;&quot;,&quot;definesF mat&quot;:false,&quot;key&quot;:&quot;jdbcbinlogslotname&quot;,&quot;required&quot;:false {&quot;defaultValue&quot;:&quot;100&quot;,&quot;description&quot;:&quot;&quot;,&quot;defin Format&quot;:false,&quot;key&quot;:&quot;asynccapacity&quot;,&quot;required&quot;:false}, {&quot;defaultValue&quot;:&quot;100&quot;,&quot;description&quot;:&quot;&quot;,&quot;defin Format&quot;:false,&quot;key&quot;:&quot;cacheScanLimit&quot;,&quot;required&quot;:false}, {&quot;defaultValue&quot;:&quot;20971520&quot;,&quot;description&quot;:&quot;&quot;,&quot; finesFormat&quot;:false,&quot;key&quot;:&quot;jdbcwritebatchtotalbytesize&quot;,&quot;requ ed&quot;:false}, {&quot;defaultValue&quot;:&quot;5&quot;,&quot;description&quot;:&quot;&quot;,&quot;defines rmat&quot;:false,&quot;key&quot;:&quot;rpcretries&quot;,&quot;required&quot;:false}, {&quot;defaultValue&quot;:&quot;1024&quot;,&quot;description&quot;:&quot;&quot;,&quot;defi sFormat&quot;:false,&quot;key&quot;:&quot;bhclientreaderbatch&quot;,&quot;required&quot;:f se}, {&quot;defaultValue&quot;:&quot;60000&quot;,&quot;description&quot;:&quot;&quot;,&quot;def esFormat&quot;:false,&quot;key&quot;:&quot;jdbcmetacachettl&quot;,&quot;required&quot;:fal }, {&quot;defaultValue&quot;:&quot;true&quot;,&quot;description&quot;:&quot;&quot;,&quot;defi sFormat&quot;:false,&quot;key&quot;:&quot;splitstrategy&quot;,&quot;required&quot;:false}, {&quot;defaultValue&quot;:&quot;false&quot;,&quot;description&quot;:&quot;&quot;,&quot;def esFormat&quot;:false,&quot;key&quot;:&quot;partitionrouter&quot;,&quot;required&quot;:fals
```

,

```
{&quot;defaultValue&quot;:&quot;&quot;,&quot;description&quot;:&quot;&quot;,&quot;definesF mat&quot;:false,&quot;key&quot;:&quot;connectionpoolname&quot;,&quot;required&quot;:false {&quot;defaultValue&quot;:&quot;60000&quot;,&quot;description&quot;:&quot;&quot;,&quot;def esFormat&quot;:false,&quot;key&quot;:&quot;jdbcconnectionmaxidlems&quot;,&quot;required&qu ;:false}, {&quot;defaultValue&quot;:&quot;&quot;,&quot;description&quot;:&quot;&quot;,&quot;definesF mat&quot;:false,&quot;key&quot;:&quot;dbname&quot;,&quot;required&quot;:true}, {&quot;defaultValue&quot;:&quot;false&quot;,&quot;description&quot;:&quot;&quot;,&quot;def esFormat&quot;:false,&quot;key&quot;:&quot;enabletypenormalization&quot;,&quot;required&qu ;:false}, {&quot;defaultValue&quot;:&quot;262144&quot;,&quot;description&quot;:&quot;&quot;,&quot;de nesFormat&quot;:false,&quot;key&quot;:&quot;splitdatasize&quot;,&quot;required&quot;:false {&quot;defaultValue&quot;:&quot;60000&quot;,&quot;description&quot;:&quot;&quot;,&quot;def esFormat&quot;:false,&quot;key&quot;:&quot;binlogrequesttimeoutms&quot;,&quot;required&quo :false}, {&quot;defaultValue&quot;:&quot;32&quot;,&quot;description&quot;:&quot;&quot;,&quot;define ormat&quot;:false,&quot;key&quot;:&quot;splitlength&quot;,&quot;required&quot;:false},{ &quot;defaultValue&quot;:&quot;180000&quot;,&quot;description&quot;:&quot;&quot;,&quot;def esFormat&quot;:false,&quot;key&quot;:&quot;asynctimeoutms&quot;,&quot;required&quot;:false {&quot;defaultValue&quot;:&quot;binary&quot;,&quot;description&quot;:&quot;&quot;,&quot;de nesFormat&quot;:false,&quot;key&quot;:&quot;jdbccopyformat&quot;,&quot;required&quot;:fals
```

,

```
{&quot;defaultValue&quot;:&quot;5000&quot;,&quot;description&quot;:&quot;&quot;,&quot;defi sFormat&quot;:false,&quot;key&quot;:&quot;jdbcretrysleepstepms&quot;,&quot;required&quot; lse}, {&quot;defaultValue&quot;:&quot;&quot;,&quot;description&quot;:&quot;&quot;,&quot;definesF mat&quot;:false,&quot;key&quot;:&quot;userpcmode&quot;,&quot;required&quot;:false}, {&quot;defaultValue&quot;:&quot;false&quot;,&quot;description&quot;:&quot;&quot;,&quot;def esFormat&quot;:false,&quot;key&quot;:&quot;cdcmode&quot;,&quot;required&quot;:false}, {&quot;defaultValue&quot;:&quot;true&quot;,&quot;description&quot;:&quot;&quot;,&quot;defi sFormat&quot;:false,&quot;key&quot;:&quot;enableBinaryCache&quot;,&quot;required&quot;:fal },
```

实时计算（流计算） 参考

```
}, {&quot;defaultValue&quot;:&quot;10000&quot;,&quot;description&quot;:&quot;&quot;,&quot;def esFormat&quot;:false,&quot;key&quot;:&quot;jdbcwriteflushinterval&quot;,&quot;required&quo :false}, {&quot;defaultValue&quot;:&quot;100&quot;,&quot;description&quot;:&quot;&quot;,&quot;defin Format&quot;:false,&quot;key&quot;:&quot;shardrpcretries&quot;,&quot;required&quot;:false {&quot;defaultValue&quot;:&quot;false&quot;,&quot;description&quot;:&quot;&quot;,&quot;def esFormat&quot;:false,&quot;key&quot;:&quot;partialinsert.enabled&quot;,&quot;required&quot;:false}, {&quot;defaultValue&quot;:&quot;60&quot;,&quot;description&quot;:&quot;&quot;,&quot;define ormat&quot;:false,&quot;key&quot;:&quot;jdbcscantimeoutseconds&quot;,&quot;required&quot; lse}, {&quot;defaultValue&quot;:&quot;false&quot;,&quot;description&quot;:&quot;&quot;,&quot;def esFormat&quot;:false,&quot;key&quot;:&quot;insertorupdate&quot;,&quot;required&quot;:false {&quot;defaultValue&quot;:&quot;1000&quot;,&quot;description&quot;:&quot;&quot;,&quot;defi sFormat&quot;:false,&quot;key&quot;:&quot;scanbatchsize&quot;,&quot;required&quot;:false}, {&quot;defaultValue&quot;:&quot;1&quot;,&quot;description&quot;:&quot;&quot;,&quot;defines rmat&quot;:false,&quot;key&quot;:&quot;asynccallbackpool&quot;,&quot;required&quot;:false {&quot;defaultValue&quot;:&quot;:&quot;,&quot;description&quot;:&quot;&quot;,&quot;defines rmat&quot;:false,&quot;key&quot;:&quot;primarykeysep&quot;,&quot;required&quot;:false}, {&quot;defaultValue&quot;:&quot;false&quot;,&quot;description&quot;:&quot;&quot;,&quot;def esFormat&quot;:false,&quot;key&quot;:&quot;createparttable&quot;,&quot;required&quot;:fals
```

,

```
{&quot;defaultValue&quot;:&quot;false&quot;,&quot;description&quot;:&quot;&quot;,&quot;def esFormat&quot;:false,&quot;key&quot;:&quot;reportmetrics&quot;,&quot;required&quot;:false {&quot;defaultValue&quot;:&quot;&quot;,&quot;description&quot;:&quot;&quot;,&quot;definesF mat&quot;:false,&quot;key&quot;:&quot;starttime&quot;,&quot;required&quot;:false}, {&quot;defaultValue&quot;:&quot;false&quot;,&quot;description&quot;:&quot;&quot;,&quot;def esFormat&quot;:false,&quot;key&quot;:&quot;useholohubmode&quot;,&quot;required&quot;:false {&quot;defaultValue&quot;:&quot;unordered&quot;,&quot;description&quot;:&quot;&quot;,&quot efinesFormat&quot;:false,&quot;key&quot;:&quot;asyncresultorder&quot;,&quot;required&quot; alse}, {&quot;defaultValue&quot;:&quot;256&quot;,&quot;description&quot;:&quot;&quot;,&quot;defin Format&quot;:false,&quot;key&quot;:&quot;jdbcreadbatchqueuesize&quot;,&quot;required&quot; alse},{&quot;defaultValue&quot;:&quot;- 1&quot;,&quot;description&quot;:&quot;&quot;,&quot;definesFormat&quot;:false,&quot;key&quo :&quot;jdbcmetaautorefreshfactor&quot;,&quot;required&quot;:false}, {&quot;defaultValue&quot;:&quot;10&quot;,&quot;description&quot;:&quot;&quot;,&quot;define ormat&quot;:false,&quot;key&quot;:&quot;binlogmaxretrytimes&quot;,&quot;required&quot;:fal }, {&quot;defaultValue&quot;:&quot;none&quot;,&quot;description&quot;:&quot;&quot;,&quot;defi sFormat&quot;:false,&quot;key&quot;:&quot;sdkmode&quot;,&quot;required&quot;:false}, {&quot;defaultValue&quot;:&quot;9223372036854775807&quot;,&quot;description&quot;:&quot;&q t;,&quot;definesFormat&quot;:false,&quot;key&quot;:&quot;cacheTTLMs&quot;,&quot;required&q t;:false}, {&quot;defaultValue&quot;:&quot;false&quot;,&quot;description&quot;:&quot;&quot;,&quot;def esFormat&quot;:false,&quot;key&quot;:&quot;upsertsource&quot;,&quot;required&quot;:false}, {&quot;defaultValue&quot;:&quot;false&quot;,&quot;description&quot;:&quot;&quot;,&quot;def esFormat&quot;:false,&quot;key&quot;:&quot;bhclientignoredelete&quot;,&quot;required&quot; alse}, {&quot;defaultValue&quot;:&quot;false&quot;,&quot;description&quot;:&quot;&quot;,&quot;def esFormat&quot;:false,&quot;key&quot;:&quot;remove-u0000-intext.enabled&quot;,&quot;required&quot;:false}, {&quot;defaultValue&quot;:&quot;earliestOffset&quot;,&quot;description&quot;:&quot;&quot;, uot;definesFormat&quot;:false,&quot;key&quot;:&quot;binlogstartupmode&quot;,&quot;required
```

实时计算（流计算） 参考

```
uot;:false}, {&quot;defaultValue&quot;:&quot;100&quot;,&quot;description&quot;:&quot;&quot;,&quot;defin Format&quot;:false,&quot;key&quot;:&quot;sqlretries&quot;,&quot;required&quot;:false},{ &quot;defaultValue&quot;:&quot;false&quot;,&quot;description&quot;:&quot;&quot;,&quot;defi sFormat&quot;:false,&quot;key&quot;:&quot;supportcolumnstorageformat&quot;,&quot;required& ot;:false}, {&quot;defaultValue&quot;:&quot;10&quot;,&quot;description&quot;:&quot;&quot;,&quot;define ormat&quot;:false,&quot;key&quot;:&quot;channelthreadcount&quot;,&quot;required&quot;:fals
```

,

```
{&quot;defaultValue&quot;:&quot;false&quot;,&quot;description&quot;:&quot;&quot;,&quot;def esFormat&quot;:false,&quot;key&quot;:&quot;ignorenullwhenupdate&quot;,&quot;required&quot; alse}, {&quot;defaultValue&quot;:&quot;stream&quot;,&quot;description&quot;:&quot;&quot;,&quot;de nesFormat&quot;:false,&quot;key&quot;:&quot;__tablename__&quot;,&quot;required&quot;:false {&quot;defaultValue&quot;:&quot;&quot;,&quot;description&quot;:&quot;&quot;,&quot;definesF mat&quot;:false,&quot;key&quot;:&quot;nullvalues&quot;,&quot;required&quot;:false}, {&quot;defaultValue&quot;:&quot;&quot;,&quot;description&quot;:&quot;&quot;,&quot;definesF mat&quot;:false,&quot;key&quot;:&quot;endpoint&quot;,&quot;required&quot;:true}, {&quot;defaultValue&quot;:&quot;10000&quot;,&quot;description&quot;:&quot;&quot;,&quot;def esFormat&quot;:false,&quot;key&quot;:&quot;refreshinterval&quot;,&quot;required&quot;:fals
```

,

```xml
{&quot;defaultValue&quot;:&quot;\\u0002&quot;,&quot;description&quot;:&quot;&quot;,&quot;d inesFormat&quot;:false,&quot;key&quot;:&quot;field_delimiter&quot;,&quot;required&quot;:fa e}, {&quot;defaultValue&quot;:&quot;false&quot;,&quot;description&quot;:&quot;&quot;,&quot;def esFormat&quot;:false,&quot;key&quot;:&quot;enable_filter_push_down&quot;,&quot;required&qu ;:false}, {&quot;defaultValue&quot;:&quot;&quot;,&quot;description&quot;:&quot;&quot;,&quot;definesF mat&quot;:false,&quot;key&quot;:&quot;tablename&quot;,&quot;required&quot;:true}, {&quot;defaultValue&quot;:&quot;true&quot;,&quot;description&quot;:&quot;&quot;,&quot;defi sFormat&quot;:false,&quot;key&quot;:&quot;cacheEmpty&quot;,&quot;required&quot;:false}, {&quot;defaultValue&quot;:&quot;public&quot;,&quot;description&quot;:&quot;&quot;,&quot;de nesFormat&quot;:false,&quot;key&quot;:&quot;schemaname&quot;,&quot;required&quot;:false}, {&quot;defaultValue&quot;:&quot;600&quot;,&quot;description&quot;:&quot;&quot;,&quot;defin Format&quot;:false,&quot;key&quot;:&quot;jdbcscantransactionsessiontimeoutseconds&quot;,&q t;required&quot;:false}],&quot;packaged&quot;:false,&quot;dependencies&quot;: [&quot;hdfs:///vvp/data/sql-artifacts/namespaces/flinkteam/custom-connectors/2024-03- 12T01-50-56.079896Z/ververica-connector-hologres-1.15-vvr-6.0fix.jar&quot;]}],&quot;@type&quot;:&quot;type.googleapis.com/vvp.sql.v1beta1.AnalyzeConnec rJarsResponse&quot;,&quot;duplicatedSourceFactoriesConnectors&quot;: [],&quot;duplicatedSinkFactoriesConnectors&quot;:[]}</data> <success>true</success> <requestId>05AEEA60-8B59-4CCD-9F35-B27EE47F4D4E</requestId>
```

###### ListTables

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

实时计算（流计算） 参考

```
GET /pop/workspaces/[workspace]/catalog/v1beta2/namespaces/[namespace]/catalogs/[cat]:listTabl HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| workspace | String | Path | 是 | default | 作业所在的工作空间ID。您可以通过以下任意一种方式获取： 通过ListNamespaces获取。 在Flink全托管开发控制台工作空间详情中获取。 |
| namespac e | String | Path | 是 | ververica | 作业所在的项目空间名称。 |
| cat | String | Path | 是 | vvp | catalog名称。 |
| database | String | Query | 是 | default | Catalog下数据库名称。 |
| RegionId | String | Host | 是 | cn-wulan-env***-d01 | Region名称。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | String | 202107221428- KKE3K857WS | 请求ID。 |

实时计算（流计算） 参考

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| data | String | {"tables": [{"name":"blackhol e","schema": {"column": [{"name":"id","type ":"VARCHAR(21474 83647)","expressio n":""}],"watermark Spec": []},"properties": {"connector":"blac khole"},"comment" :""}, {"name":"blackhol e sink","schema": _ {"column": [{"name":"name"," type":"VARCHAR(2 147483647)","expr ession":""}, {"name":"score","t ype":"BIGINT","exp ression":""}],"water markSpec": []},"properties": {"connector":"blac khole"},"comment" :"blackhole sink table"}]} | 详细信息。 |

**示例**

请求示例

```
GET /pop/workspaces/[workspace]/catalog/v1beta2/namespaces/[namespace]/catalogs/[cat]:listTabl HTTP/1.1 &workspace=default &namespace=ververica &cat=vvp &database=default &RegionId=cn-wulan-env***-d01
```

&公共请求参数正常返回示例 `JSON` 格式实时计算（流计算） 参考

```json
{
 "data":"{\"tables\":[{\"name\":\"blackhole\",\"schema\":{\"column\":
[{\"name\":\"id\",\"type\":\"VARCHAR(2147483647)\",\"expression\":\"\"}],\"watermarkSpec\" []},\"properties\":{\"connector\":\"blackhole\"},\"comment\":\"\"}, {\"name\":\"blackhole_sink\",\"schema\":{\"column\": [{\"name\":\"name\",\"type\":\"VARCHAR(2147483647)\",\"expression\":\"\"}, {\"name\":\"score\",\"type\":\"BIGINT\",\"expression\":\"\"}],\"watermarkSpec\": []},\"properties\":{\"connector\":\"blackhole\"},\"comment\":\"blackhole sink table\"}]}",
 "requestId":"202107221428-KKE3K857WS"
}
```

`XML` 格式

```xml
<data>{&quot;tables&quot;:[{&quot;name&quot;:&quot;blackhole&quot;,&quot;schema&quot;: {&quot;column&quot;: [{&quot;name&quot;:&quot;id&quot;,&quot;type&quot;:&quot;VARCHAR(2147483647)&quot;,&quot;e ression&quot;:&quot;&quot;}],&quot;watermarkSpec&quot;:[]},&quot;properties&quot;: {&quot;connector&quot;:&quot;blackhole&quot;},&quot;comment&quot;:&quot;&quot;}, {&quot;name&quot;:&quot;blackhole_sink&quot;,&quot;schema&quot;:{&quot;column&quot;: [{&quot;name&quot;:&quot;name&quot;,&quot;type&quot;:&quot;VARCHAR(2147483647)&quot;,&quot xpression&quot;:&quot;&quot;}, {&quot;name&quot;:&quot;score&quot;,&quot;type&quot;:&quot;BIGINT&quot;,&quot;expression&q t;:&quot;&quot;}],&quot;watermarkSpec&quot;:[]},&quot;properties&quot;: {&quot;connector&quot;:&quot;blackhole&quot;},&quot;comment&quot;:&quot;blackhole sink table&quot;}]}</data> <requestId>202107221428-KKE3K857WS</requestId>
```

###### ListSessionClusters

调用ListSessionClusters，列出指定工作区和命名空间下的所有会话集群。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
GET /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/sessionclusters HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | String | Host | 是 | cn-wulan-env***-d01 | Region ID。 |

实时计算（流计算） 参考

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| workspace | String | Path | 是 | default | 作业所在的工作空间ID。您可以通过以下任意一种方式获取： 通过ListNamespaces获取。 在Flink全托管开发控制台工作空间详情中获取。 |
| namespac e | String | Path | 是 | flinkteam | 作业所在的项目空间名称。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| data | String | { "metadata": {}, "apiVersion": "v1", "kind": "SessionClusterList ", "items": [] } | 详细信息。 |
| requestId | String | CBC799F0-AS7S- 1D30-8A4F- 882ED4DD**** | 请求ID。 |
| success | Boolean | true | 请求是否成功。 |

**示例**

请求示例

```
GET /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/sessionclusters HTTP/1.1 &RegionId=cn-wulan-env***-d01 &workspace=default &namespace=flinkteam
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "data":"{\"metadata\":
{},\"apiVersion\":\"v1\",\"kind\":\"SessionClusterList\",\"items\":[]}",
 "requestId":"CBC799F0-AS7S-1D30-8A4F-882ED4DD****",
 "success":true
}
```

`XML` 格式实时计算（流计算） 参考

```xml
<data>{&quot;metadata&quot;: {},&quot;apiVersion&quot;:&quot;v1&quot;,&quot;kind&quot;:&quot;SessionClusterList&quot;,& ot;items&quot;:[]}</data> <requestId>CBC799F0-AS7S-1D30-8A4F-882ED4DD****</requestId> <success>true</success>
```

###### ListSecretValues

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
GET /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/secret-values HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | String | Host | 是 | cn-wulan-env***-d01 | Region ID。 |
| namespac e | String | Path | 是 | flinkteam | 作业所在的项目空间名称。 |
| workspace | String | Path | 是 | default | 作业所在的工作空间ID。您可以通过以下任意一种方式获取： 通过ListNamespaces获取。 在Flink全托管开发控制台工作空间详情中获取。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| success | Boolean | true | 请求是否成功。 |
| requestId | String | 5CC1B23C-CCA3- 4283-B275- 0F969CDFD34F | 请求ID。 |

实时计算（流计算） 参考

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| data | String | { "metadata": { "totalSize": 1, "totalPage": 1 }, "apiVersion": "v1", "kind": "SecretValueList", "items": [ { "metadata": { "createdAt": "2024- 03-11T03:07:09Z", "modifiedAt": "2024-03- 11T03:07:09Z", "resourceVersion": 1, "name": "secretkey", "namespace": "flinkteam", "annotations": { "creator": "22985261012276 3813", "modifier": "22985261012276 3813", "creatorName": "flinkadmin", "modifierName": "flinkadmin" }, "id": "6dd63491- f0bf-4af3-a38e- 7001d479addc", "labels": {} }, "apiVersion": "v1", "kind": "SecretValue", "spec": { "kind": "Plain", "value": "******" } } ] } | 详细数据。 |

**示例**

请求示例

```
GET /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/secret-values HTTP/1.1 &RegionId=cn-wulan-env***-d01 &namespace=flinkteam &workspace=default
```

&公共请求参数正常返回示例 `JSON` 格式实时计算（流计算） 参考

```json
{
 "data":"{\"metadata\":
{\"totalSize\":1,\"totalPage\":1},\"apiVersion\":\"v1\",\"kind\":\"SecretValueList\",\"ite \":[{\"metadata\":{\"createdAt\":\"2024-03-11T03:07:09Z\",\"modifiedAt\":\"2024-03- 11T03:07:09Z\",\"resourceVersion\":1,\"name\":\"secretkey\",\"namespace\":\"flinkteam\",\" notations\": {\"creator\":\"229852610122763813\",\"modifier\":\"229852610122763813\",\"creatorName\":\" inkadmin\",\"modifierName\":\"flinkadmin\"},\"id\":\"6dd63491-f0bf-4af3-a38e- 7001d479addc\",\"labels\":{}},\"apiVersion\":\"v1\",\"kind\":\"SecretValue\",\"spec\": {\"kind\":\"Plain\",\"value\":\"******\"}}]}",
 "success":true,
 "requestId":"5CC1B23C-CCA3-4283-B275-0F969CDFD34F"
}
```

`XML` 格式

```xml
<data>{&quot;metadata&quot;: {&quot;totalSize&quot;:1,&quot;totalPage&quot;:1},&quot;apiVersion&quot;:&quot;v1&quot;,&q t;kind&quot;:&quot;SecretValueList&quot;,&quot;items&quot;:[{&quot;metadata&quot;: {&quot;createdAt&quot;:&quot;2024-03- 11T03:07:09Z&quot;,&quot;modifiedAt&quot;:&quot;2024-03- 11T03:07:09Z&quot;,&quot;resourceVersion&quot;:1,&quot;name&quot;:&quot;secretkey&quot;,&q t;namespace&quot;:&quot;flinkteam&quot;,&quot;annotations&quot;: {&quot;creator&quot;:&quot;229852610122763813&quot;,&quot;modifier&quot;:&quot;22985261012 63813&quot;,&quot;creatorName&quot;:&quot;flinkadmin&quot;,&quot;modifierName&quot;:&quot; inkadmin&quot;},&quot;id&quot;:&quot;6dd63491-f0bf-4af3-a38e- 7001d479addc&quot;,&quot;labels&quot;: {}},&quot;apiVersion&quot;:&quot;v1&quot;,&quot;kind&quot;:&quot;SecretValue&quot;,&quot;s c&quot;:{&quot;kind&quot;:&quot;Plain&quot;,&quot;value&quot;:&quot;******&quot;}}]} </data> <success>true</success> <requestId>5CC1B23C-CCA3-4283-B275-0F969CDFD34F</requestId>
```

###### ListSavepoints

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
GET /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/savepoints HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | String | Host | 是 | cn-wulan-env***-d01 | Region ID。 |

| 实时计算（流计 | 算） |  |  | Flink | 存算分离版开发指南·OpenAP |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| namespac e | String | Path | 是 | flinkteam | 作业所在的项目空间名称。 |
| deployme ntId | String | Query | 是 | d0b3abf0-4bfe-46b1- a324-5b7def580c00 | 作业ID。 |
| jobId | String | Query | 否 | 5af678c0-7db0-4650- 94c2-d2604f0a**** | 作业实例ID。 |
| workspace | String | Path | 是 | default | 作业所在的工作空间ID。您可以通过以下任意一种方式获取： 通过ListNamespaces获取。 在Flink全托管开发控制台工作空间详情中获取。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
|  |  | { "metadata": {}, "apiVersion": "v1", "kind": "SavepointList", "items": [{ "metadata": { "createdAt": "2026- 04-24T03:55:16Z", "jobId": "f736bbd6- c9cf-48ab-973a- 9653bb0f8c0a", "workspace": "9cuwr9g7y1hl19", "nativeFormat": false, "modifiedAt": "2026-04- 24T03:55:19Z", "deploymentId": "a3d88b2a-e076- 4491-86f2- 5a81ea4c7300", "origin": "USER REQUEST", _ "resourceVersion": 2, "namespace": "flinkteam", "annotations": { "com.dataartisans. appmanager.contr oller.deployment.s pec.version": "9", "taker": " \| vvp-0" }, "comment": "", "id": "5cea0d88- 303d-44e5-a96e- 47f7217723d7" }, "apiVersion": "v1", "kind": |  |

实时计算（流计算） 参考

| 参数名称 | 类型 | "Savepoint", 示例 "spec": { | 说明 |
|---|---|---|---|
| data | String | "flinkSavepointId": "fc2e33c1-8132- 516f-2923- 7371060fb449", "savepointLocation ": "oss://flink- fullymanaged- 9cuwr9g7y1hl19/fli nk- savepoints/namesp aces/flinkteam/depl oyments/a3d88b2a -e076-4491-86f2- 5a81ea4c7300/5ce a0d88-303d-44e5- a96e- 47f7217723d7/sav epoint-f736bb- f467305080c0" }, "status": { "state": "COMPLETED" } }, | 详细信息。 |
|  |  | { "metadata": { "createdAt": "2026- 04-24T03:52:08Z", "jobId": "e5c412be- c160-460a-9d7b- 0b7111c77e15", "workspace": "9cuwr9g7y1hl19", "nativeFormat": false, "modifiedAt": "2026-04- 24T03:52:13Z", "deploymentId": "a3d88b2a-e076- 4491-86f2- 5a81ea4c7300", "origin": "USER REQUEST", _ "resourceVersion": 2, "namespace": "flinkteam", "annotations": { "com.dataartisans. appmanager.contr oller.deployment.s pec.version": "6", "taker": " \| vvp-0" }, "comment": "", "id": "58778df9- 5082-4da3-9890- d531fcc1200d" }, "apiVersion": "v1", "kind": "Savepoint", "spec": { "flinkSavepointId": "3ac331a3-6ef9- d8f7-e3e8- e3d5b2649180", "savepointLocation ": "oss://flink- fullymanaged- 9cuwr9g7y1hl19/fli nk- i t / |  |

实时计算（流计算） 参考

| 参数名称 | 类型 | savepoints/namesp a示c例es/flinkteam/depl oyments/a3d88b2a | 说明 |
|---|---|---|---|
|  |  | -e076-4491-86f2- 5a81ea4c7300/587 78df9-5082-4da3- 9890- d531fcc1200d/save point-e5c412- 8a27e8210de8" }, "status": { "state": "COMPLETED" } }] } |  |
| requestId | String | CBC799F0-AS7S- 1D30-8A4F- 882ED4DD**** | 请求ID。 |
| success | Boolean | true | 请求是否成功。 |

**示例**

请求示例

```
GET /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/savepoints HTTP/1.1 &RegionId=cn-wulan-env***-d01 &namespace=flinkteam &deploymentId=d0b3abf0-4bfe-46b1-a324-5b7def580c00 &workspace=default
```

&公共请求参数正常返回示例 `JSON` 格式实时计算（流计算） 参考

```json
{
 "data":"{\"metadata\":{},\"apiVersion\":\"v1\",\"kind\":\"SavepointList\",\"items\":
[{\"metadata\":{\"createdAt\":\"2026-04-24T03:55:16Z\",\"jobId\":\"f736bbd6-c9cf-48ab-9 73a- 9653bb0f8c0a\",\"workspace\":\"9cuwr9g7y1hl19\",\"nativeFormat\":false,\"modifiedAt\":\"20 -04-24T03:55:19Z\",\"deploymentId\":\"a3d88b2a-e076-4491-86f2- 5a81ea4c7300\",\"origin\":\"USER_REQUEST\",\"resourceVersion\":2,\"namespace\":\"flinkteam ,\"annotations\": {\"com.dataartisans.appmanager.controller.deployment.spec.version\":\"9\",\"taker\":\"
| vvp-0\"},\"comment\":\"\",\"id\":\"5cea0d88-303d-44e5-a96e-
47f7217723d7\"},\"apiVersion\":\"v1\",\"kind\":\"Savepoint\",\"spec\": {\"flinkSavepointId\":\"fc2e33c1-8132-516f-2923- 7371060fb449\",\"savepointLocation\":\"oss://flink-fullymanaged-9cuwr9g7y1hl19/flinksavepoints/namespaces/flinkteam/deployments/a3d88b2a-e076-4491-86f2- 5a81ea4c7300/5cea0d88-303d-44e5-a96e-47f7217723d7/savepoint-f736bbf467305080c0\"},\"status\":{\"state\":\"COMPLETED\"}},{\"metadata\": {\"createdAt\":\"2026-04-24T03:52:08Z\",\"jobId\":\"e5c412be-c160-460a-9d7b- 0b7111c77e15\",\"workspace\":\"9cuwr9g7y1hl19\",\"nativeFormat\":false,\"modifiedAt\":\"20 -04-24T03:52:13Z\",\"deploymentId\":\"a3d88b2a-e076-4491-86f2- 5a81ea4c7300\",\"origin\":\"USER_REQUEST\",\"resourceVersion\":2,\"namespace\":\"flinkteam ,\"annotations\": {\"com.dataartisans.appmanager.controller.deployment.spec.version\":\"6\",\"taker\":\"
| vvp-0\"},\"comment\":\"\",\"id\":\"58778df9-5082-4da3-9890-
d531fcc1200d\"},\"apiVersion\":\"v1\",\"kind\":\"Savepoint\",\"spec\": {\"flinkSavepointId\":\"3ac331a3-6ef9-d8f7-e3e8e3d5b2649180\",\"savepointLocation\":\"oss://flink-fullymanaged-9cuwr9g7y1hl19/flinksavepoints/namespaces/flinkteam/deployments/a3d88b2a-e076-4491-86f2- 5a81ea4c7300/58778df9-5082-4da3-9890-d531fcc1200d/savepoint-e5c412- 8a27e8210de8\"},\"status\":{\"state\":\"COMPLETED\"}}]}",
 "requestId":"CBC799F0-AS7S-1D30-8A4F-882ED4DD****",
 "success":true
}
```

`XML` 格式实时计算（流计算） 参考

```xml
<data>{&quot;metadata&quot;: {},&quot;apiVersion&quot;:&quot;v1&quot;,&quot;kind&quot;:&quot;SavepointList&quot;,&quot; ems&quot;:[{&quot;metadata&quot;:{&quot;createdAt&quot;:&quot;2026-04- 24T03:55:16Z&quot;,&quot;jobId&quot;:&quot;f736bbd6-c9cf-48ab-973a- 9653bb0f8c0a&quot;,&quot;workspace&quot;:&quot;9cuwr9g7y1hl19&quot;,&quot;nativeFormat&quo :false,&quot;modifiedAt&quot;:&quot;2026-04- 24T03:55:19Z&quot;,&quot;deploymentId&quot;:&quot;a3d88b2a-e076-4491-86f2- 5a81ea4c7300&quot;,&quot;origin&quot;:&quot;USER_REQUEST&quot;,&quot;resourceVersion&quot; ,&quot;namespace&quot;:&quot;flinkteam&quot;,&quot;annotations&quot;: {&quot;com.dataartisans.appmanager.controller.deployment.spec.version&quot;:&quot;9&quot;, uot;taker&quot;:&quot; | vvp- 0&quot;},&quot;comment&quot;:&quot;&quot;,&quot;id&quot;:&quot;5cea0d88-303d-44e5-a96e- 47f7217723d7&quot;},&quot;apiVersion&quot;:&quot;v1&quot;,&quot;kind&quot;:&quot;Savepoint uot;,&quot;spec&quot;:{&quot;flinkSavepointId&quot;:&quot;fc2e33c1-8132-516f-2923- 7371060fb449&quot;,&quot;savepointLocation&quot;:&quot;oss://flink-fullymanaged- 9cuwr9g7y1hl19/flink-savepoints/namespaces/flinkteam/deployments/a3d88b2a-e076-4491- 86f2-5a81ea4c7300/5cea0d88-303d-44e5-a96e-47f7217723d7/savepoint-f736bbf467305080c0&quot;},&quot;status&quot;:{&quot;state&quot;:&quot;COMPLETED&quot;}}, {&quot;metadata&quot;:{&quot;createdAt&quot;:&quot;2026-04- 24T03:52:08Z&quot;,&quot;jobId&quot;:&quot;e5c412be-c160-460a-9d7b- 0b7111c77e15&quot;,&quot;workspace&quot;:&quot;9cuwr9g7y1hl19&quot;,&quot;nativeFormat&quo :false,&quot;modifiedAt&quot;:&quot;2026-04- 24T03:52:13Z&quot;,&quot;deploymentId&quot;:&quot;a3d88b2a-e076-4491-86f2- 5a81ea4c7300&quot;,&quot;origin&quot;:&quot;USER_REQUEST&quot;,&quot;resourceVersion&quot; ,&quot;namespace&quot;:&quot;flinkteam&quot;,&quot;annotations&quot;: {&quot;com.dataartisans.appmanager.controller.deployment.spec.version&quot;:&quot;6&quot;, uot;taker&quot;:&quot; | vvp- 0&quot;},&quot;comment&quot;:&quot;&quot;,&quot;id&quot;:&quot;58778df9-5082-4da3-9890d531fcc1200d&quot;},&quot;apiVersion&quot;:&quot;v1&quot;,&quot;kind&quot;:&quot;Savepoint uot;,&quot;spec&quot;:{&quot;flinkSavepointId&quot;:&quot;3ac331a3-6ef9-d8f7-e3e8e3d5b2649180&quot;,&quot;savepointLocation&quot;:&quot;oss://flink-fullymanaged- 9cuwr9g7y1hl19/flink-savepoints/namespaces/flinkteam/deployments/a3d88b2a-e076-4491- 86f2-5a81ea4c7300/58778df9-5082-4da3-9890-d531fcc1200d/savepoint-e5c412- 8a27e8210de8&quot;},&quot;status&quot;:{&quot;state&quot;:&quot;COMPLETED&quot;}}]} </data> <requestId>CBC799F0-AS7S-1D30-8A4F-882ED4DD****</requestId> <success>true</success>
```

###### ListNamespaces

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
GET /pop/namespaces/v1/namespaces HTTP/1.1
```

**请求参数**

实时计算（流计算） 参考

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | String | Host | 是 | cn-wulan-env***-d01 | Region ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | String | CBC799F0-AS7S- 1D30-8A4F- 882ED4DD**** | 请求ID。 |
| data | String | { "@type": "type.googleapis.c om/vvp.namespace s.v1.ListNamespac esResponse", "namespaces": [{ "roleBindings": [{ "role": "owner", "members": ["user:2354069766 5705****"] }, { "role": "owner", "members": ["user:1664076657 00****"] }], "cluster": "", "isHa": false, "workspace": "9cuwr9g7y1hl19", "cpuBrand": "Intel", "previewSessionClu sterName": "", "createTime": "2026-04- 24T03:33:43.68062 6Z", "lifecyclePhase": "LIFECYCLE PHASE _ ACTIVE", "name": _ "namespaces/flinkt eam", "labels": {} }] } | 详细信息。 |
| success | Boolean | true | 请求是否成功。 |

**示例**

请求示例

```
GET /pop/namespaces/v1/namespaces HTTP/1.1 &RegionId=cn-wulan-env***-d01
```

&公共请求参数正常返回示例 `JSON` 格式实时计算（流计算） 参考

```json
{
 "data":"
{\"@type\":\"type.googleapis.com/vvp.namespaces.v1.ListNamespacesResponse\",\"namespaces\" [{\"roleBindings\":[{\"role\":\"owner\",\"members\":[\"user:23540697665705****\"]}, {\"role\":\"owner\",\"members\": [\"user:166407665700****\"]}],\"cluster\":\"\",\"isHa\":false,\"workspace\":\"9cuwr9g7y1hl \",\"cpuBrand\":\"Intel\",\"previewSessionClusterName\":\"\",\"createTime\":\"2026-04- 24T03:33:43.680626Z\",\"lifecyclePhase\":\"LIFECYCLE_PHASE_ACTIVE\",\"name\":\"namespaces/ inkteam\",\"labels\":{}}]}",
 "requestId":"CBC799F0-AS7S-1D30-8A4F-882ED4DD****",
 "success":true
}
```

`XML` 格式

```xml
<data> {&quot;@type&quot;:&quot;type.googleapis.com/vvp.namespaces.v1.ListNamespacesResponse&quot &quot;namespaces&quot;:[{&quot;roleBindings&quot;: [{&quot;role&quot;:&quot;owner&quot;,&quot;members&quot;: [&quot;user:23540697665705****&quot;]}, {&quot;role&quot;:&quot;owner&quot;,&quot;members&quot;: [&quot;user:166407665700****&quot;]}],&quot;cluster&quot;:&quot;&quot;,&quot;isHa&quot;:fa e,&quot;workspace&quot;:&quot;9cuwr9g7y1hl19&quot;,&quot;cpuBrand&quot;:&quot;Intel&quot;, uot;previewSessionClusterName&quot;:&quot;&quot;,&quot;createTime&quot;:&quot;2026-04- 24T03:33:43.680626Z&quot;,&quot;lifecyclePhase&quot;:&quot;LIFECYCLE_PHASE_ACTIVE&quot;,&q t;name&quot;:&quot;namespaces/flinkteam&quot;,&quot;labels&quot;:{}}]}</data> <requestId>CBC799F0-AS7S-1D30-8A4F-882ED4DD****</requestId> <success>true</success>
```

###### ListFunctions

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
GET /pop/workspaces/[workspace]/catalog/v1beta2/namespaces/[namespace]/catalogs/[cat]:listFunc ons HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | String | Host | 是 | cn-wulan-env***-d01 | Region名称。 |
| namespac e | String | Path | 是 | ververica | 作业所在的项目空间名称。 |

| link存算分离版参考 | 开发指南 | ·OpenAPI |  |  | 实时计算（流计算） |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| workspace | String | Path | 是 | default | 作业所在的工作空间ID。您可以通过以下任意一种方式获取： 通过ListNamespaces获取。 在Flink全托管开发控制台工作空间详情中获取。 |
| cat | String | Path | 是 | vvp | catalog名称。 |
| database | String | Query | 是 | default | catalog数据库名称。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| data | String | {"@type":"type.go ogleapis.com/vvp.s ql.catalog.v1beta2. ListFunctionsRespo nse","functions": [{"name":"Timesta mpProbe","classNa me":"com.alibaba. blink.udtf.Timesta mpProbe","function Language":"FUNCTI ON LANGUAGE JAV _ _ A","functionType":" FUNCTION TYPE FL _ _ INK","description":" This is a user- defined function"}, {"name":"Transfor mUdtf","className ":"com.alibaba.blin k.udtf.TransformUd tf","functionLangua ge":"FUNCTION LA _ NGUAGE JAVA","fu _ nctionType":"FUNC TION TYPE FLINK"," _ _ description":"This is a user-defined function"}]} | 详细数据。 |
| requestId | String | 0ADBBDD0-E2E9- 4611-98C6- 6767A3AB87D2 | 请求ID。 |
| success | Boolean | true | 请求是否成功。 |

**示例**

请求示例实时计算（流计算） 参考

```
GET /pop/workspaces/[workspace]/catalog/v1beta2/namespaces/[namespace]/catalogs/[cat]:listFunc ons HTTP/1.1 &RegionId=cn-wulan-env***-d01 &namespace=ververica &workspace=default &cat=vvp &database=default
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "data":"
{\"@type\":\"type.googleapis.com/vvp.sql.catalog.v1beta2.ListFunctionsResponse\",\"functio \": [{\"name\":\"TimestampProbe\",\"className\":\"com.alibaba.blink.udtf.TimestampProbe\",\"fu tionLanguage\":\"FUNCTION_LANGUAGE_JAVA\",\"functionType\":\"FUNCTION_TYPE_FLINK\",\"descr tion\":\"This is a user-defined function\"}, {\"name\":\"TransformUdtf\",\"className\":\"com.alibaba.blink.udtf.TransformUdtf\",\"funct nLanguage\":\"FUNCTION_LANGUAGE_JAVA\",\"functionType\":\"FUNCTION_TYPE_FLINK\",\"descript n\":\"This is a user-defined function\"}]}",
 "requestId":"0ADBBDD0-E2E9-4611-98C6-6767A3AB87D2",
 "success":true
}
```

`XML` 格式

```xml
<data> {&quot;@type&quot;:&quot;type.googleapis.com/vvp.sql.catalog.v1beta2.ListFunctionsResponse uot;,&quot;functions&quot;: [{&quot;name&quot;:&quot;TimestampProbe&quot;,&quot;className&quot;:&quot;com.alibaba.blin udtf.TimestampProbe&quot;,&quot;functionLanguage&quot;:&quot;FUNCTION_LANGUAGE_JAVA&quot;, uot;functionType&quot;:&quot;FUNCTION_TYPE_FLINK&quot;,&quot;description&quot;:&quot;This is a user-defined function&quot;}, {&quot;name&quot;:&quot;TransformUdtf&quot;,&quot;className&quot;:&quot;com.alibaba.blink tf.TransformUdtf&quot;,&quot;functionLanguage&quot;:&quot;FUNCTION_LANGUAGE_JAVA&quot;,&qu ;functionType&quot;:&quot;FUNCTION_TYPE_FLINK&quot;,&quot;description&quot;:&quot;This is a user-defined function&quot;}]}</data> <requestId>0ADBBDD0-E2E9-4611-98C6-6767A3AB87D2</requestId> <success>true</success>
```

###### ListFormats

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

实时计算（流计算） 参考

```
GET /pop/workspaces/[workspace]/sql/v1beta1/namespaces/[namespace]/formats HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | String | Host | 是 | cn-wulan-env***-d01 | Region ID。 |
| workspace | String | Path | 是 | default | 作业所在的工作空间ID。您可以通过以下任意一种方式获取： 通过ListNamespaces获取。 在Flink全托管开发控制台工作空间详情中获取。 |
| namespac e | String | Path | 是 | flinkteam | 作业所在的项目空间名称。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| success | Boolean | true | 请求是否成功。 |

实时计算（流计算） 参考

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| data | String | { "formats": [ { "sink": true, "name": "namespaces/flinkt eam/formats/avro", "source": true, "type": "avro", "properties": [ { "defaultValue": "", "description": "Must be set to \u0027avro\u0027 to configure this format.", "definesFormat": false, "key": "format", "required": true } ], "packaged": true, "dependencies": [ "hdfs:///vvp/data/sq l- artifacts/namespac es/ververica/conne ctors/vvr-6.0.7- flink- 1.15/opt/formats/a vro/flink-sql-avro- 1.15-vvr-6.0.7- SNAPSHOT.jar" ] } ], "@type": "type.googleapis.c om/vvp.sql.v1beta 1.ListFormatsRespo nse" } | 详细信息。 |
| requestId | String | 6BFF2035-B5FB- 4E1A-8F32- 4CA636417A3D | 请求ID。 |

**示例**

请求示例

```
GET /pop/workspaces/[workspace]/sql/v1beta1/namespaces/[namespace]/formats HTTP/1.1 &RegionId=cn-wulan-env***-d01 &workspace=default &namespace=flinkteam
```

&公共请求参数正常返回示例 `JSON` 格式实时计算（流计算） 参考

```json
{
 "data":"{\"formats\":
[{\"sink\":true,\"name\":\"namespaces/flinkteam/formats/avro\",\"source\":true,\"type\":\" ro\",\"properties\":[{\"defaultValue\":\"\",\"description\":\"Must be set to \\u0027avro\\u0027 to configure this format.\",\"definesFormat\":false,\"key\":\"format\",\"required\":true}],\"packaged\":true "dependencies\":[\"hdfs:///vvp/data/sql-artifacts/namespaces/ververica/connectors/vvr- 6.0.7-flink-1.15/opt/formats/avro/flink-sql-avro-1.15-vvr-6.0.7- SNAPSHOT.jar\"]}],\"@type\":\"type.googleapis.com/vvp.sql.v1beta1.ListFormatsResponse\"}",
 "success":true,
 "requestId":"6BFF2035-B5FB-4E1A-8F32-4CA636417A3D"
}
```

`XML` 格式

```xml
<data>{&quot;formats&quot;: [{&quot;sink&quot;:true,&quot;name&quot;:&quot;namespaces/flinkteam/formats/avro&quot;,&qu ;source&quot;:true,&quot;type&quot;:&quot;avro&quot;,&quot;properties&quot;: [{&quot;defaultValue&quot;:&quot;&quot;,&quot;description&quot;:&quot;Must be set to \u0027avro\u0027 to configure this format.&quot;,&quot;definesFormat&quot;:false,&quot;key&quot;:&quot;format&quot;,&quot;req red&quot;:true}],&quot;packaged&quot;:true,&quot;dependencies&quot;: [&quot;hdfs:///vvp/data/sql-artifacts/namespaces/ververica/connectors/vvr-6.0.7-flink- 1.15/opt/formats/avro/flink-sql-avro-1.15-vvr-6.0.7- SNAPSHOT.jar&quot;]}],&quot;@type&quot;:&quot;type.googleapis.com/vvp.sql.v1beta1.ListForm sResponse&quot;}</data> <success>true</success> <requestId>6BFF2035-B5FB-4E1A-8F32-4CA636417A3D</requestId>
```

###### ListFlinkVersions

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
GET /pop/workspaces/[workspace]/api/v1/flink-version-meta.json HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | String | Host | 是 | cn-wulan-env***-d01 | Region ID。 |

实时计算（流计算） 参考

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| workspace | String | Path | 是 | default | 作业所在的工作空间ID。您可以通过以下任意一种方式获取： 通过ListNamespaces获取。 在Flink全托管开发控制台工作空间详情中获取。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
|  |  | { "defaultFlinkVersio nName": "vvr- 6.0.0-flink-1.15", "flinkVersionMetad atas": [ { "supportFindUsedC atalogs": false, "useForJarFineGrai ned": false, "versionName": "vvr-3.0.9-flink- 1.12", "flinkVersion": "1.12", "useForSqlDeploym ents": true, "labels": {}, "features": { "supportFindUsedC atalogs": false, "supportDynamicLo gLevel": false, "supportDagExpan sion": false, "useForJarFineGrai ned": false, "supportNativeSav epoint": false, "supportStateComp atibility": false, "supportNativeK8s" : false, "supportJvmDebug ": false, "supportLogArchive ": false, "useForSqlDeploym ents": true, "supportLogPaging ": false }, "tarUrl": "hdfs:///vvp/data/sq l- artifacts/namespac es/default/package d-vvr-dist/vvr- 3.0.9-flink- 1.12/vvr-3.0.9- fli k 1 12 |  |

实时计算（流计算） 参考

| 参数名称 | 类型 | flink-1.12- d示is例t.tar.gz", "supportStateComp | 说明 |
|---|---|---|---|
|  |  | atibility": false, "defaultFor": [], "imageTag": "1.12.0-vvr-3.0.9- 1109", "vvrVersion": "3.0.9", "status": "DEPRECATED" }, { "supportFindUsedC atalogs": true, "useForJarFineGrai ned": false, "versionName": "vvr-4.0.18-flink- 1.13", "flinkVersion": "1.13", "useForSqlDeploym ents": true, "labels": {}, "features": { "supportFindUsedC atalogs": true, "supportDynamicLo gLevel": true, "supportDagExpan sion": false, "useForJarFineGrai ned": false, "supportNativeSav |  |
| data | String | epoint": false, "supportStateComp atibility": true, "supportNativeK8s" : false, "supportJvmDebug ": true, "supportLogArchive ": true, "useForSqlDeploym ents": true, "supportLogPaging ": true }, "tarUrl": "hdfs:///vvp/data/sq l- artifacts/namespac es/default/package d-vvr-dist/vvr- 4.0.18-flink- 1.13/vvr-4.0.18- flink-1.13- dist.tar.gz", "supportStateComp atibility": true, "defaultFor": [], "imageTag": "1.13.0-vvr-4.0.18- 22", "vvrVersion": "4.0.18", "status": "DEPRECATED" }, { "supportFindUsedC atalogs": true, "useForJarFineGrai ned": false, "versionName": | 详细信息。 |

实时计算（流计算） 参考

| 参数名称 | 类型 | versionName : "示vv例r-6.0.0-flink- 1.15", | 说明 |
|---|---|---|---|
|  |  | "flinkVersion": "1.15", "useForSqlDeploym ents": true, "labels": {}, "features": { "supportFindUsedC atalogs": true, "supportDynamicLo gLevel": true, "supportDagExpan sion": false, "useForJarFineGrai ned": false, "supportNativeSav epoint": false, "supportStateComp atibility": true, "supportNativeK8s" : false, "supportJvmDebug ": true, "supportLogArchive ": true, "useForSqlDeploym ents": true, "supportLogPaging ": true }, "tarUrl": "hdfs:///vvp/data/sq l- artifacts/namespac es/default/package d-vvr-dist/vvr- 6.0.7-flink- 1.15/vvr-6.0.7- flink-1.15- dist.tar.gz", "supportStateComp atibility": true, "defaultFor": [], "imageTag": "1.15.0-vvr-6.0.7- 29", "vvrVersion": "6.0.7", "status": "STABLE" } ] } |  |
| requestId | String | 63269B06-8027- 4CD0-9AB5- D9791B185B82 | 请求ID。 |
| success | Boolean | true | 请求是否成功。 |

**示例**

请求示例

```
GET /pop/workspaces/[workspace]/api/v1/flink-version-meta.json HTTP/1.1 &RegionId=cn-wulan-env***-d01 &workspace=default
```

&公共请求参数实时计算（流计算） 参考正常返回示例 `JSON` 格式

```json
{
 "data":"{\"defaultFlinkVersionName\":\"vvr-6.0.0-flink-
1.15\",\"flinkVersionMetadatas\": [{\"supportFindUsedCatalogs\":false,\"useForJarFineGrained\":false,\"versionName\":\"vvr- 3.0.9-flink-1.12\",\"flinkVersion\":\"1.12\",\"useForSqlDeployments\":true,\"labels\": {},\"features\": {\"supportFindUsedCatalogs\":false,\"supportDynamicLogLevel\":false,\"supportDagExpansion\ false,\"useForJarFineGrained\":false,\"supportNativeSavepoint\":false,\"supportStateCompat ility\":false,\"supportNativeK8s\":false,\"supportJvmDebug\":false,\"supportLogArchive\":f se,\"useForSqlDeployments\":true,\"supportLogPaging\":false},\"tarUrl\":\"hdfs:///vvp/data ql-artifacts/namespaces/default/packaged-vvr-dist/vvr-3.0.9-flink-1.12/vvr-3.0.9-flink- 1.12-dist.tar.gz\",\"supportStateCompatibility\":false,\"defaultFor\": [],\"imageTag\":\"1.12.0-vvr-3.0.9- 1109\",\"vvrVersion\":\"3.0.9\",\"status\":\"DEPRECATED\"}, {\"supportFindUsedCatalogs\":true,\"useForJarFineGrained\":false,\"versionName\":\"vvr- 4.0.18-flink-1.13\",\"flinkVersion\":\"1.13\",\"useForSqlDeployments\":true,\"labels\": {},\"features\": {\"supportFindUsedCatalogs\":true,\"supportDynamicLogLevel\":true,\"supportDagExpansion\" lse,\"useForJarFineGrained\":false,\"supportNativeSavepoint\":false,\"supportStateCompatib ity\":true,\"supportNativeK8s\":false,\"supportJvmDebug\":true,\"supportLogArchive\":true, useForSqlDeployments\":true,\"supportLogPaging\":true},\"tarUrl\":\"hdfs:///vvp/data/sqlartifacts/namespaces/default/packaged-vvr-dist/vvr-4.0.18-flink-1.13/vvr-4.0.18-flink-1 .13-dist.tar.gz\",\"supportStateCompatibility\":true,\"defaultFor\": [],\"imageTag\":\"1.13.0-vvr-4.0.18- 22\",\"vvrVersion\":\"4.0.18\",\"status\":\"DEPRECATED\"}, {\"supportFindUsedCatalogs\":true,\"useForJarFineGrained\":false,\"versionName\":\"vvr- 6.0.0-flink-1.15\",\"flinkVersion\":\"1.15\",\"useForSqlDeployments\":true,\"labels\": {},\"features\": {\"supportFindUsedCatalogs\":true,\"supportDynamicLogLevel\":true,\"supportDagExpansion\" lse,\"useForJarFineGrained\":false,\"supportNativeSavepoint\":false,\"supportStateCompatib ity\":true,\"supportNativeK8s\":false,\"supportJvmDebug\":true,\"supportLogArchive\":true, useForSqlDeployments\":true,\"supportLogPaging\":true},\"tarUrl\":\"hdfs:///vvp/data/sqlartifacts/namespaces/default/packaged-vvr-dist/vvr-6.0.7-flink-1.15/vvr-6.0.7-flink- 1.15-dist.tar.gz\",\"supportStateCompatibility\":true,\"defaultFor\": [],\"imageTag\":\"1.15.0-vvr-6.0.7- 29\",\"vvrVersion\":\"6.0.7\",\"status\":\"STABLE\"}]}",
 "requestId":"63269B06-8027-4CD0-9AB5-D9791B185B82",
 "success":true
}
```

`XML` 格式实时计算（流计算） 参考

```xml
<data>{&quot;defaultFlinkVersionName&quot;:&quot;vvr-6.0.0-flink- 1.15&quot;,&quot;flinkVersionMetadatas&quot;: [{&quot;supportFindUsedCatalogs&quot;:false,&quot;useForJarFineGrained&quot;:false,&quot;v sionName&quot;:&quot;vvr-3.0.9-flink- 1.12&quot;,&quot;flinkVersion&quot;:&quot;1.12&quot;,&quot;useForSqlDeployments&quot;:true quot;labels&quot;:{},&quot;features&quot;: {&quot;supportFindUsedCatalogs&quot;:false,&quot;supportDynamicLogLevel&quot;:false,&quot; pportDagExpansion&quot;:false,&quot;useForJarFineGrained&quot;:false,&quot;supportNativeSa point&quot;:false,&quot;supportStateCompatibility&quot;:false,&quot;supportNativeK8s&quot; alse,&quot;supportJvmDebug&quot;:false,&quot;supportLogArchive&quot;:false,&quot;useForSql ployments&quot;:true,&quot;supportLogPaging&quot;:false},&quot;tarUrl&quot;:&quot;hdfs:/// p/data/sql-artifacts/namespaces/default/packaged-vvr-dist/vvr-3.0.9-flink-1.12/vvr- 3.0.9-flink-1.12dist.tar.gz&quot;,&quot;supportStateCompatibility&quot;:false,&quot;defaultFor&quot;: [],&quot;imageTag&quot;:&quot;1.12.0-vvr-3.0.9- 1109&quot;,&quot;vvrVersion&quot;:&quot;3.0.9&quot;,&quot;status&quot;:&quot;DEPRECATED&qu ;}, {&quot;supportFindUsedCatalogs&quot;:true,&quot;useForJarFineGrained&quot;:false,&quot;ver onName&quot;:&quot;vvr-4.0.18-flink- 1.13&quot;,&quot;flinkVersion&quot;:&quot;1.13&quot;,&quot;useForSqlDeployments&quot;:true quot;labels&quot;:{},&quot;features&quot;: {&quot;supportFindUsedCatalogs&quot;:true,&quot;supportDynamicLogLevel&quot;:true,&quot;su ortDagExpansion&quot;:false,&quot;useForJarFineGrained&quot;:false,&quot;supportNativeSave int&quot;:false,&quot;supportStateCompatibility&quot;:true,&quot;supportNativeK8s&quot;:fa e,&quot;supportJvmDebug&quot;:true,&quot;supportLogArchive&quot;:true,&quot;useForSqlDeplo ents&quot;:true,&quot;supportLogPaging&quot;:true},&quot;tarUrl&quot;:&quot;hdfs:///vvp/da /sql-artifacts/namespaces/default/packaged-vvr-dist/vvr-4.0.18-flink-1.13/vvr-4.0.18-fl ink-1.13dist.tar.gz&quot;,&quot;supportStateCompatibility&quot;:true,&quot;defaultFor&quot;: [],&quot;imageTag&quot;:&quot;1.13.0-vvr-4.0.18- 22&quot;,&quot;vvrVersion&quot;:&quot;4.0.18&quot;,&quot;status&quot;:&quot;DEPRECATED&quo }, {&quot;supportFindUsedCatalogs&quot;:true,&quot;useForJarFineGrained&quot;:false,&quot;ver onName&quot;:&quot;vvr-6.0.0-flink- 1.15&quot;,&quot;flinkVersion&quot;:&quot;1.15&quot;,&quot;useForSqlDeployments&quot;:true quot;labels&quot;:{},&quot;features&quot;: {&quot;supportFindUsedCatalogs&quot;:true,&quot;supportDynamicLogLevel&quot;:true,&quot;su ortDagExpansion&quot;:false,&quot;useForJarFineGrained&quot;:false,&quot;supportNativeSave int&quot;:false,&quot;supportStateCompatibility&quot;:true,&quot;supportNativeK8s&quot;:fa e,&quot;supportJvmDebug&quot;:true,&quot;supportLogArchive&quot;:true,&quot;useForSqlDeplo ents&quot;:true,&quot;supportLogPaging&quot;:true},&quot;tarUrl&quot;:&quot;hdfs:///vvp/da /sql-artifacts/namespaces/default/packaged-vvr-dist/vvr-6.0.7-flink-1.15/vvr-6.0.7flink-1.15dist.tar.gz&quot;,&quot;supportStateCompatibility&quot;:true,&quot;defaultFor&quot;: [],&quot;imageTag&quot;:&quot;1.15.0-vvr-6.0.7- 29&quot;,&quot;vvrVersion&quot;:&quot;6.0.7&quot;,&quot;status&quot;:&quot;STABLE&quot;}] </data> <requestId>63269B06-8027-4CD0-9AB5-D9791B185B82</requestId> <success>true</success>
```

###### ListDeploymentTargets

实时计算（流计算） 参考

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
GET /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/deployment-targets HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | String | Host | 是 | cn-wulan-env***-d01 | Region ID。 |
| namespac e | String | Path | 是 | flinkteam | 作业所在的项目空间名称。 |
| workspace | String | Path | 是 | default | 作业所在的工作空间ID。您可以通过以下任意一种方式获取： 通过ListNamespaces获取。 在Flink全托管开发控制台工作空间详情中获取。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | String | CBC799F0-AS7S- 1D30-8A4F- 882ED4DD**** | 请求ID。 |

实时计算（流计算） 参考

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| data | String | { "metadata": {}, "apiVersion": "v1", "kind": "DeploymentTarget List", "items": [{ "metadata": { "createdAt": "2026- 04-24T03:33:44Z", "workspace": "9cuwr9g7y1hl19", "modifiedAt": "2026-04- 24T03:33:44Z", "resourceVersion": 1, "name": "dt- flinkteam", "namespace": "flinkteam", "annotations": { "creator": "14949745101258 46", "modifier": "14949745101258 46", "creatorName": "null", "modifierName": "null" }, "id": "a89ff052-38c6- 4fd3-9b91- e9c53f8ee019", "labels": {} }, "apiVersion": "v1", "kind": "DeploymentTarget ", "ha": false, "spec": { "kubernetes": { "namespace": "flinkteam" }, "kind": "kubernetes", "state": "ONLINE" } }] } | 详细信息。 |
| success | Boolean | true | 请求是否成功。 |

**示例**

请求示例

```
GET /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/deployment-targets HTTP/1.1 &RegionId=cn-wulan-env***-d01 &namespace=flinkteam &workspace=default
```

&公共请求参数正常返回示例实时计算（流计算） 参考 `JSON` 格式

```json
{
 "data":"{\"metadata\":
{},\"apiVersion\":\"v1\",\"kind\":\"DeploymentTargetList\",\"items\":[{\"metadata\": {\"createdAt\":\"2026-04- 24T03:33:44Z\",\"workspace\":\"9cuwr9g7y1hl19\",\"modifiedAt\":\"2026-04- 24T03:33:44Z\",\"resourceVersion\":1,\"name\":\"dtflinkteam\",\"namespace\":\"flinkteam\",\"annotations\": {\"creator\":\"1494974510125846\",\"modifier\":\"1494974510125846\",\"creatorName\":\"null ,\"modifierName\":\"null\"},\"id\":\"a89ff052-38c6-4fd3-9b91-e9c53f8ee019\",\"labels\": {}},\"apiVersion\":\"v1\",\"kind\":\"DeploymentTarget\",\"ha\":false,\"spec\": {\"kubernetes\": {\"namespace\":\"flinkteam\"},\"kind\":\"kubernetes\",\"state\":\"ONLINE\"}}]}",
 "requestId":"CBC799F0-AS7S-1D30-8A4F-882ED4DD****",
 "success":true
}
```

`XML` 格式

```xml
<data>{&quot;metadata&quot;: {},&quot;apiVersion&quot;:&quot;v1&quot;,&quot;kind&quot;:&quot;DeploymentTargetList&quot; quot;items&quot;:[{&quot;metadata&quot;:{&quot;createdAt&quot;:&quot;2026-04- 24T03:33:44Z&quot;,&quot;workspace&quot;:&quot;9cuwr9g7y1hl19&quot;,&quot;modifiedAt&quot; quot;2026-04- 24T03:33:44Z&quot;,&quot;resourceVersion&quot;:1,&quot;name&quot;:&quot;dtflinkteam&quot;,&quot;namespace&quot;:&quot;flinkteam&quot;,&quot;annotations&quot;: {&quot;creator&quot;:&quot;1494974510125846&quot;,&quot;modifier&quot;:&quot;1494974510125 6&quot;,&quot;creatorName&quot;:&quot;null&quot;,&quot;modifierName&quot;:&quot;null&quot; &quot;id&quot;:&quot;a89ff052-38c6-4fd3-9b91-e9c53f8ee019&quot;,&quot;labels&quot;: {}},&quot;apiVersion&quot;:&quot;v1&quot;,&quot;kind&quot;:&quot;DeploymentTarget&quot;,&q t;ha&quot;:false,&quot;spec&quot;:{&quot;kubernetes&quot;: {&quot;namespace&quot;:&quot;flinkteam&quot;},&quot;kind&quot;:&quot;kubernetes&quot;,&quo state&quot;:&quot;ONLINE&quot;}}]}</data> <requestId>CBC799F0-AS7S-1D30-8A4F-882ED4DD****</requestId> <success>true</success>
```

###### ListDeployments

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
GET /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/deployments HTTP/1.1
```

**请求参数**

实时计算（流计算） 参考

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | String | Host | 是 | cn-wulan-env***-d01 | Region ID。 |
| namespac e | String | Path | 是 | flinkteam | 作业所在的项目空间名称。 |
| workspace | String | Path | 是 | default | 作业所在的工作空间ID。您可以通过以下任意一种方式获取： 通过ListNamespaces获取。 在Flink全托管开发控制台工作空间详情中获取。 |
| pageSize | String | Query | 否 | 10 | 分页参数，表示所请求页码元素数量，最大值为100， 最小值为1，默认值为10。 |
| pageIndex | String | Query | 否 | 1 | 分页参数，页码索引，表示所请求页码，最小值为1， 默认值为1。 |
| sortName | String | Query | 否 | ["age", "name"] | 表示按年龄和姓名进行排序的字段列表。 |
| sortOrder | String | Query | 否 | DESC | 排序顺序。 DESC：降序。 ASC：顺序。 默认值：DESC。 |
| creator | String | Query | 否 | 235406976657057054 | 规则创建者。 |
| modifier | String | Query | 否 | yunduntest | 更新人。 |
| priority | String | Query | 否 | 1 | 线路优先级。1优先级最高，数值越大优先级越低。 |
| deployme ntId | String | Query | 否 | d0b3abf0-4bfe-46b1- a324-5b7def580c00 | 作业ID。 |
| name | String | Query | 否 | blinkteam | namespace名称。 |
| status | String | Query | 否 | 1 | 状态。 |

| link存算分离版 | 开发指南 | ·OpenAPI |  |  |  |
|---|---|---|---|---|---|

参考

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| state | String | Query | 否 | false | 剧本的运行状态： true： 发布流程。 false： 禁用流程。 |
| batchMod e | String | Query | 否 | true | 表示禁用批量处理模式，适用于逐个处理任务或数据的情况。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| success | Boolean | true | 请求是否成功。 |
|  |  | { "metadata": { "totalSize": 1, "totalPage": 1 }, "apiVersion": "v1", "kind": "DeploymentList", "items": [{ "metadata": { "createdAt": "2026- 04-30T03:54:19Z", "workspace": "9cuwr9g7y1hl19", "modifiedAt": "2026-04- 30T05:38:17Z", "resourceVersion": 4, "name": "sqlJob", "namespace": "flinkteam", "annotations": { "creator": "23540697665705 7054", "resource- plan.has.migrated" : "true", "storage.disaster.r po": "1800", "deployment.has.d eployed": "false", "deployment.sourc e-type": "EDITOR", "deployment.paren t.id": "", "modifier": "23540697665705 7054", "creatorName": "flinkadmin", "plan.uri": "deployment/9151 0cd2-9d21-463a- abf4- 9c608d23e92e/res ourcePlan.json", |  |

实时计算（流计算） 参考

| 参数名称 | 类型 | "priority": "5", 示例 "priority.class.nam | 说明 |
|---|---|---|---|
|  |  | e": "flink-p5", "migration.display. enabled": "false", "com.dataartisans. appmanager.contr oller.deployment.s pec.version": "2", "default.resource- setting.has.migrate d": "true", "deployment.refere nced.deployment.d raft.history.version ": "7", "deployment.refere nced.deployment.d raft.id": "cee26b6e- d03b-4a03-a628- a6fe665c525e", "modifierName": "flinkadmin", "taker": " \| vvp-0", "deployment.refere nced.deployment.d raft.history.id": "c7819685-3abe- 4115-a26b- |  |
| data | String | d40e73c58856" }, "id": "91510cd2- 9d21-463a-abf4- 9c608d23e92e", "labels": {} }, "apiVersion": "v1", "kind": "Deployment", "spec": { "template": { "metadata": { "annotations": { "flink.resource.type ": "fine-grained", "native.kubernetes. mode": "true", "flink.queryable- state.enabled": "false", "flink.security.ssl.e nabled": "false" } }, "spec": { "artifact": { "flinkImageTag": "1.17.0-vvr-8.0.7- manifest-251107", "kind": "SQLSCRIPT", "sqlScript": "CREATE TEMPORARY TABLE `datahub table` _ (strname VARCHAR) with ( 'connector' = 'datagen' ); | 详细信息。 |

实时计算（流计算） 参考

| 参数名称 | 类型 | CREATE 示例 TEMPORARY TABLE | 说明 |
|---|---|---|---|
|  |  | `kafka table` _ (strname VARCHAR, lens BIGINT) with ( 'connector' = 'print' ); INSERT INTO kafka table _ SELECT SUBSTRING (strname, 0, 10) AS strname, CAST (CHAR LENGTH _ (strname) AS BIGINT) AS lens FROM datahub table;", _ "imageUserDefined ": false, "flinkImageRegistry ": "cn-wulan-env**- d01- reg.docker.intra.en v**.shuguang.com: 80/ververica-paas", "versionName": "vvr-8.0.7-flink- 1.17", "flinkImageReposit ory": "vvr", "flinkVersion": "1.17" }, "parallelism": 1, "batchMode": false, "resources": { "jobmanager": { "memory": "2Gi", "cpu": 0.5 }, "taskmanager": { "memory": "3Gi", "cpu": 1.0 } }, "logging": { "log4jLoggers": { "": "INFO" }, "logReservePolicy": { "expirationDays": 7, "openHistory": true }, "loggingProfile": "default" }, "flinkConfiguration" : {} } }, "restoreStrategy": { "kind": "LATEST STATE", _ "allowNonRestored State": false }, "state": "CANCELLED", "upgradeStrategy": { "kind": "NONE" }, "maxSavepointCre ationAttempts": 4, |  |

实时计算（流计算） 参考

| 参数名称 | 类型 | "maxJobCreationAt 示例 tempts": 1, | 说明 |
|---|---|---|---|
|  |  | "deploymentTarget Id": "a89ff052- 38c6-4fd3-9b91- e9c53f8ee019" }, "status": { "startTime": 0, "state": "CANCELLED", "endTime": 0 } }] } |  |
| requestId | String | CBC799F0-AS7S- 1D30-8A4F- 882ED4DD**** | 请求ID。 |

**示例**

请求示例

```
GET /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/deployments HTTP/1.1 &RegionId=cn-wulan-env***-d01 &namespace=flinkteam &workspace=default
```

&公共请求参数正常返回示例 `JSON` 格式实时计算（流计算） 参考

```json
{
 "data":"{\"metadata\":
{\"totalSize\":1,\"totalPage\":1},\"apiVersion\":\"v1\",\"kind\":\"DeploymentList\",\"item ":[{\"metadata\":{\"createdAt\":\"2026-04- 30T03:54:19Z\",\"workspace\":\"9cuwr9g7y1hl19\",\"modifiedAt\":\"2026-04- 30T05:38:17Z\",\"resourceVersion\":4,\"name\":\"sqlJob\",\"namespace\":\"flinkteam\",\"ann ations\":{\"creator\":\"235406976657057054\",\"resourceplan.has.migrated\":\"true\",\"storage.disaster.rpo\":\"1800\",\"deployment.has.deployed\" "false\",\"deployment.sourcetype\":\"EDITOR\",\"deployment.parent.id\":\"\",\"modifier\":\"235406976657057054\",\"crea rName\":\"flinkadmin\",\"plan.uri\":\"deployment/91510cd2-9d21-463a-abf4- 9c608d23e92e/resourcePlan.json\",\"priority\":\"5\",\"priority.class.name\":\"flinkp5\",\"migration.display.enabled\":\"false\",\"com.dataartisans.appmanager.controller.depl ment.spec.version\":\"2\",\"default.resourcesetting.has.migrated\":\"true\",\"deployment.referenced.deployment.draft.history.version\" "7\",\"deployment.referenced.deployment.draft.id\":\"cee26b6e-d03b-4a03-a628a6fe665c525e\",\"modifierName\":\"flinkadmin\",\"taker\":\" | vvp- 0\",\"deployment.referenced.deployment.draft.history.id\":\"c7819685-3abe-4115-a26bd40e73c58856\"},\"id\":\"91510cd2-9d21-463a-abf4-9c608d23e92e\",\"labels\": {}},\"apiVersion\":\"v1\",\"kind\":\"Deployment\",\"spec\":{\"template\":{\"metadata\":{ \"annotations\":{\"flink.resource.type\":\"finegrained\",\"native.kubernetes.mode\":\"true\",\"flink.queryablestate.enabled\":\"false\",\"flink.security.ssl.enabled\":\"false\"}},\"spec\": {\"artifact\":{\"flinkImageTag\":\"1.17.0-vvr-8.0.7-manifest- 251107\",\"kind\":\"SQLSCRIPT\",\"sqlScript\":\"CREATE TEMPORARY TABLE `datahub_table` (strname VARCHAR)\with (\ 'connector' = 'datagen'\);\\CREATE TEMPORARY TABLE `kafka_t able` (strname VARCHAR, lens BIGINT)\with (\ 'connector' = 'print'\);\\INSERT INTO kafka_table\SELECT SUBSTRING (strname, 0, 10) AS strname, CAST (CHAR_LENGTH (strname) A S BIGINT) AS lens\FROM\ datahub_table;\",\"imageUserDefined\":false,\"flinkImageRegistry\":\"cn-wulan-env**d01-reg.docker.intra.env**.shuguang.com:80/ververica-paas\",\"versionName\":\"vvr- 8.0.7-flink- 1.17\",\"flinkImageRepository\":\"vvr\",\"flinkVersion\":\"1.17\"},\"parallelism\":1,\"bat Mode\":false,\"resources\":{\"jobmanager\": {\"memory\":\"2Gi\",\"cpu\":0.5},\"taskmanager\": {\"memory\":\"3Gi\",\"cpu\":1.0}},\"logging\":{\"log4jLoggers\": {\"\":\"INFO\"},\"logReservePolicy\": {\"expirationDays\":7,\"openHistory\":true},\"loggingProfile\":\"default\"},\"flinkConfigu tion\":{}}},\"restoreStrategy\": {\"kind\":\"LATEST_STATE\",\"allowNonRestoredState\":false},\"state\":\"CANCELLED\",\"upgr eStrategy\": {\"kind\":\"NONE\"},\"maxSavepointCreationAttempts\":4,\"maxJobCreationAttempts\":1,\"depl mentTargetId\":\"a89ff052-38c6-4fd3-9b91-e9c53f8ee019\"},\"status\": {\"startTime\":0,\"state\":\"CANCELLED\",\"endTime\":0}}]}",
 "success":true,
 "requestId":"CBC799F0-AS7S-1D30-8A4F-882ED4DD****"
}
```

`XML` 格式

```xml
<data>{&quot;metadata&quot;: {&quot;totalSize&quot;:1,&quot;totalPage&quot;:1},&quot;apiVersion&quot;:&quot;v1&quot;,&q t;kind&quot;:&quot;DeploymentList&quot;,&quot;items&quot;:[{&quot;metadata&quot;: {&quot;createdAt&quot;:&quot;2026-04-
```

实时计算（流计算） 参考

```xml
{&quot;createdAt&quot;:&quot;202604 30T03:54:19Z&quot;,&quot;workspace&quot;:&quot;9cuwr9g7y1hl19&quot;,&quot;modifiedAt&quot; quot;2026-04- 30T05:38:17Z&quot;,&quot;resourceVersion&quot;:4,&quot;name&quot;:&quot;sqlJob&quot;,&quot amespace&quot;:&quot;flinkteam&quot;,&quot;annotations&quot;: {&quot;creator&quot;:&quot;235406976657057054&quot;,&quot;resourceplan.has.migrated&quot;:&quot;true&quot;,&quot;storage.disaster.rpo&quot;:&quot;1800&quot; quot;deployment.has.deployed&quot;:&quot;false&quot;,&quot;deployment.sourcetype&quot;:&quot;EDITOR&quot;,&quot;deployment.parent.id&quot;:&quot;&quot;,&quot;modifier uot;:&quot;235406976657057054&quot;,&quot;creatorName&quot;:&quot;flinkadmin&quot;,&quot;p n.uri&quot;:&quot;deployment/91510cd2-9d21-463a-abf4- 9c608d23e92e/resourcePlan.json&quot;,&quot;priority&quot;:&quot;5&quot;,&quot;priority.cla .name&quot;:&quot;flinkp5&quot;,&quot;migration.display.enabled&quot;:&quot;false&quot;,&quot;com.dataartisans.ap anager.controller.deployment.spec.version&quot;:&quot;2&quot;,&quot;default.resourcesetting.has.migrated&quot;:&quot;true&quot;,&quot;deployment.referenced.deployment.draft.h tory.version&quot;:&quot;7&quot;,&quot;deployment.referenced.deployment.draft.id&quot;:&qu ;cee26b6e-d03b-4a03-a628a6fe665c525e&quot;,&quot;modifierName&quot;:&quot;flinkadmin&quot;,&quot;taker&quot;:&quot
| vvp-
0&quot;,&quot;deployment.referenced.deployment.draft.history.id&quot;:&quot;c7819685- 3abe-4115-a26b-d40e73c58856&quot;},&quot;id&quot;:&quot;91510cd2-9d21-463a-abf4- 9c608d23e92e&quot;,&quot;labels&quot;: {}},&quot;apiVersion&quot;:&quot;v1&quot;,&quot;kind&quot;:&quot;Deployment&quot;,&quot;sp &quot;:{&quot;template&quot;:{&quot;metadata&quot;:{&quot;annotations&quot;: {&quot;flink.resource.type&quot;:&quot;finegrained&quot;,&quot;native.kubernetes.mode&quot;:&quot;true&quot;,&quot;flink.queryablestate.enabled&quot;:&quot;false&quot;,&quot;flink.security.ssl.enabled&quot;:&quot;false&q t;}},&quot;spec&quot;:{&quot;artifact&quot;:{&quot;flinkImageTag&quot;:&quot;1.17.0-vvr -8.0.7-manifest- 251107&quot;,&quot;kind&quot;:&quot;SQLSCRIPT&quot;,&quot;sqlScript&quot;:&quot;CREATE TEMPORARY TABLE `datahub_table` (strname VARCHAR)with ( &#x27;connector&#x27; = &#x27;datagen&#x27;);CREATE TEMPORARY TABLE `kafka_table` (strname VARCHAR, lens BIGINT)with ( &#x27;connector&#x27; = &#x27;print&#x27;);INSERT INTO kafka_tableSELECT SUBSTRING (strname, 0, 10) AS strname, CAST (CHAR_LENGTH (strname) AS BIGINT) AS lensFROM datahub_table;&quot;,&quot;imageUserDefined&quot;:false,&quot;flinkImageRegistry&quot;:&qu ;cn-wulan-env**-d01-reg.docker.intra.env**.shuguang.com:80/ververicapaas&quot;,&quot;versionName&quot;:&quot;vvr-8.0.7-flink- 1.17&quot;,&quot;flinkImageRepository&quot;:&quot;vvr&quot;,&quot;flinkVersion&quot;:&quot .17&quot;},&quot;parallelism&quot;:1,&quot;batchMode&quot;:false,&quot;resources&quot;: {&quot;jobmanager&quot;: {&quot;memory&quot;:&quot;2Gi&quot;,&quot;cpu&quot;:0.5},&quot;taskmanager&quot;: {&quot;memory&quot;:&quot;3Gi&quot;,&quot;cpu&quot;:1.0}},&quot;logging&quot;: {&quot;log4jLoggers&quot;:{&quot;&quot;:&quot;INFO&quot;},&quot;logReservePolicy&quot;: {&quot;expirationDays&quot;:7,&quot;openHistory&quot;:true},&quot;loggingProfile&quot;:&qu ;default&quot;},&quot;flinkConfiguration&quot;:{}}},&quot;restoreStrategy&quot;: {&quot;kind&quot;:&quot;LATEST_STATE&quot;,&quot;allowNonRestoredState&quot;:false},&quot; ate&quot;:&quot;CANCELLED&quot;,&quot;upgradeStrategy&quot;: {&quot;kind&quot;:&quot;NONE&quot;},&quot;maxSavepointCreationAttempts&quot;:4,&quot;maxJo reationAttempts&quot;:1,&quot;deploymentTargetId&quot;:&quot;a89ff052-38c6-4fd3-9b91e9c53f8ee019&quot;},&quot;status&quot;: {&quot;startTime&quot;:0,&quot;state&quot;:&quot;CANCELLED&quot;,&quot;endTime&quot;:0}}] </data> <success>true</success>
```

实时计算（流计算） 参考

```xml
<requestId>CBC799F0-AS7S-1D30-8A4F-882ED4DD****</requestId>
```

###### ListDatabases

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
GET /pop/workspaces/[workspace]/catalog/v1beta2/namespaces/[namespace]/catalogs/[cat]:listData ses HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | String | Host | 是 | cn-wulan-env***-d01 | Region ID。 |
| namespac e | String | Path | 是 | ververica | 作业所在的项目空间名称。 |
| workspace | String | Path | 是 | default | 作业所在的工作空间ID。您可以通过以下任意一种方式获取： 通过ListNamespaces获取。 在Flink全托管开发控制台工作空间详情中获取。 |
| cat | String | Path | 是 | vvp | catalog名称。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| data | String | { "@type": "type.googleapis.c om/vvp.sql.catalog. v1beta2.ListDataba sesResponse", "databases": [ { "name": "default", "properties": {}, "comment": "The default database" } ] } | 详细信息。 |

实时计算（流计算） 参考

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | String | 76F325D7-3EC4- 4E34-81A8- 18B92D7EE606 | 请求ID。 |
| success | Boolean | true | 请求是否成功。 |

**示例**

请求示例

```
GET /pop/workspaces/[workspace]/catalog/v1beta2/namespaces/[namespace]/catalogs/[cat]:listData ses HTTP/1.1 &RegionId=cn-wulan-env***-d01 &namespace=ververica &workspace=default &cat=vvp
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "data":"
{\"@type\":\"type.googleapis.com/vvp.sql.catalog.v1beta2.ListDatabasesResponse\",\"databas \":[{\"name\":\"default\",\"properties\":{},\"comment\":\"The default database\"}]}",
 "requestId":"76F325D7-3EC4-4E34-81A8-18B92D7EE606",
 "success":true
}
```

`XML` 格式

```xml
<data> {&quot;@type&quot;:&quot;type.googleapis.com/vvp.sql.catalog.v1beta2.ListDatabasesResponse uot;,&quot;databases&quot;: [{&quot;name&quot;:&quot;default&quot;,&quot;properties&quot;: {},&quot;comment&quot;:&quot;The default database&quot;}]}</data> <requestId>76F325D7-3EC4-4E34-81A8-18B92D7EE606</requestId> <success>true</success>
```

###### ListConnectors

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

实时计算（流计算） 参考

```
GET /pop/workspaces/[workspace]/sql/v1beta1/namespaces/[namespace]/connectors HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | String | Host | 是 | cn-wulan-env***-d01 | Region ID。 |
| workspace | String | Path | 是 | default | 作业所在的工作空间ID。您可以通过以下任意一种方式获取： 通过ListNamespaces获取。 在Flink全托管开发控制台工作空间详情中获取。 |
| namespac e | String | Path | 是 | flinkteam | 作业所在的项目空间名称。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| success | Boolean | true | 请求是否成功。 |

实时计算（流计算） 参考

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| data | String | { "connectors": [ { "lookup": false, "supportedFormats ": [], "environments": [ "PUBLIC CLOUD", _ "PRIVATE CLOUD", _ "ALIBABA GROUP", _ "VVC CLOUD" ], _ "sink": false, "name": "namespaces/flinkt eam/connectors/da tagen", "source": true, "type": "datagen", "properties": [ { "defaultValue": "", "description": "Must be set to \u0027datagen\u00 27 to configure this connector.", "definesFormat": false, "key": "connector", "required": true }, { "defaultValue": "", "description": "Rows per second to control the emit rate, default 10000L.", "definesFormat": false, "key": "rows- per-second", "required": false }, { "defaultValue": "", "description": "Total number of rows to emit. By default, the source is unbounded.", "definesFormat": false, "key": "number-of-rows", "required": false } ], "packaged": true, "dependencies": [] } ], "@type": "type.googleapis.c om/vvp.sql.v1beta 1.ListConnectorsRe sponse" } | 详细数据。 |
| requestId | String | A62F262E-3055- 490B-B17B- 0C6BF83C4BE6 | 请求ID。 |

**示例**

请求示例实时计算（流计算） 参考

```
GET /pop/workspaces/[workspace]/sql/v1beta1/namespaces/[namespace]/connectors HTTP/1.1 &RegionId=cn-wulan-env***-d01 &workspace=default &namespace=flinkteam
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "data":"{\"connectors\":[{\"lookup\":false,\"supportedFormats\":[],\"environments\":[\
"PUBLIC_CLOUD\",\"PRIVATE_CLOUD\",\"ALIBABA_GROUP\",\"VVC_CLOUD\"],\"sink\":false,\"name\" "namespaces/flinkteam/connectors/datagen\",\"source\":true,\"type\":\"datagen\",\"properti \":[{\"defaultValue\":\"\",\"description\":\"Must be set to \\u0027datagen\\u0027 to configure this connector.\",\"definesFormat\":false,\"key\":\"connector\",\"required\":true}, {\"defaultValue\":\"\",\"description\":\"Rows per second to control the emit rate, default 10000L.\",\"definesFormat\":false,\"key\":\"rows-persecond\",\"required\":false},{\"defaultValue\":\"\",\"description\":\"Total number of rows to emit. By default, the source is unbounded.\",\"definesFormat\":false,\"key\":\"number-ofrows\",\"required\":false}],\"packaged\":true,\"dependencies\": []}],\"@type\":\"type.googleapis.com/vvp.sql.v1beta1.ListConnectorsResponse\"}",
 "success":true,
 "requestId":"A62F262E-3055-490B-B17B-0C6BF83C4BE6"
}
```

`XML` 格式

```xml
<data>{&quot;connectors&quot;:[{&quot;lookup&quot;:false,&quot;supportedFormats&quot;: [],&quot;environments&quot;: [&quot;PUBLIC_CLOUD&quot;,&quot;PRIVATE_CLOUD&quot;,&quot;ALIBABA_GROUP&quot;,&quot;VVC_CL D&quot;],&quot;sink&quot;:false,&quot;name&quot;:&quot;namespaces/flinkteam/connectors/dat en&quot;,&quot;source&quot;:true,&quot;type&quot;:&quot;datagen&quot;,&quot;properties&quo :[{&quot;defaultValue&quot;:&quot;&quot;,&quot;description&quot;:&quot;Must be set to connector.&quot;,&quot;definesFormat&quot;:false,&quot;key&quot;:&quot;connector&quot;,&qu ;required&quot;:true}, {&quot;defaultValue&quot;:&quot;&quot;,&quot;description&quot;:&quot;Rows per second to control the emit rate, default 10000L.&quot;,&quot;definesFormat&quot;:false,&quot;key&quot;:&quot;rows-persecond&quot;,&quot;required&quot;:false}, {&quot;defaultValue&quot;:&quot;&quot;,&quot;description&quot;:&quot;Total number of rows to emit. By default, the source is unbounded.&quot;,&quot;definesFormat&quot;:false,&quot;key&quot;:&quot;number-ofrows&quot;,&quot;required&quot;:false}],&quot;packaged&quot;:true,&quot;dependencies&quot; []}],&quot;@type&quot;:&quot;type.googleapis.com/vvp.sql.v1beta1.ListConnectorsResponse&qu ;}</data> <success>true</success> <requestId>A62F262E-3055-490B-B17B-0C6BF83C4BE6</requestId>
```

实时计算（流计算） 参考

###### ListCatalogs

调用ListCatalogs，获取指定工作空间指定namespace下的catalog列表。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
GET /pop/workspaces/[workspace]/catalog/v1beta2/namespaces/[namespace]/catalogs HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | String | Host | 是 | cn-wulan-env***-d01 | Region ID。 |
| namespac e | String | Path | 是 | ververica | 作业所在的项目空间名称。 |
| workspace | String | Path | 是 | default | 作业所在的工作空间ID。您可以通过以下任意一种方式获取： 通过ListNamespaces获取。 在Flink全托管开发控制台工作空间详情中获取。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| data | String | {"@type":"type.go ogleapis.com/vvp.s ql.catalog.v1beta2. ListCatalogsRespon se","catalogs": [{"name":"namesp aces/flinkteam/cata logs/vvp","properti es": {"defaultDatabase" :"default","type":"v vp"}}]} | 详细数据。 |
| requestId | String | 31F99ADC-B72E- 4BA1-AD32- B938D5A57532 | 请求ID。 |
| success | Boolean | true | 请求是否成功。 |

**示例**

实时计算（流计算） 参考请求示例

```
GET /pop/workspaces/[workspace]/catalog/v1beta2/namespaces/[namespace]/catalogs HTTP/1.1 &RegionId=cn-wulan-env***-d01 &namespace=ververica &workspace=default
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "data":"
{\"@type\":\"type.googleapis.com/vvp.sql.catalog.v1beta2.ListCatalogsResponse\",\"catalogs :[{\"name\":\"namespaces/flinkteam/catalogs/vvp\",\"properties\": {\"defaultDatabase\":\"default\",\"type\":\"vvp\"}}]}",
 "requestId":"31F99ADC-B72E-4BA1-AD32-B938D5A57532",
 "success":true
}
```

`XML` 格式

```xml
<data> {&quot;@type&quot;:&quot;type.googleapis.com/vvp.sql.catalog.v1beta2.ListCatalogsResponse& ot;,&quot;catalogs&quot;: [{&quot;name&quot;:&quot;namespaces/flinkteam/catalogs/vvp&quot;,&quot;properties&quot;: {&quot;defaultDatabase&quot;:&quot;default&quot;,&quot;type&quot;:&quot;vvp&quot;}}]} </data> <requestId>31F99ADC-B72E-4BA1-AD32-B938D5A57532</requestId> <success>true</success>
```

###### ListArtifacts

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
GET /pop/workspaces/[workspace]/artifacts/v1/namespaces/[namespace]/artifacts:list HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | String | Host | 是 | cn-wulan-env***-d01 | Region ID。 |

| 实时计算（流计 | 算） |  |  | Flink | 存算分离版开发指南·OpenAP 参考 |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| namespac e | String | Path | 是 | flinkteam | 作业所在的项目空间名称。 |
| workspace | String | Path | 是 | default | 作业所在的工作空间ID。您可以通过以下任意一种方式获取： 通过ListNamespaces获取。 在Flink全托管开发控制台工作空间详情中获取。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | String | CBC799F0-AS7S- 1D30-8A4F- 882ED4DD**** | 请求ID。 |
| data | String | { "@type": "type.googleapis.c om/vvp.artifacts.v1 .ListArtifactsRespo nse", "artifacts": [{ "filename": "TopSpeedWindowi ng.jar", "size": "0", "createTime": "2026-04- 29T09:20:14Z", "uploader": "23540697665705 7054", "namespace": "namespaces/flinkt eam", "uri": "oss://flink- fullymanaged- 9cuwr9g7y1hl19/ar tifacts/namespaces /flinkteam/TopSpee dWindowing.jar", "content": "" }] } | 详细信息。 |
| success | Boolean | true | 请求是否成功。 |

**示例**

请求示例实时计算（流计算） 参考

```
GET /pop/workspaces/[workspace]/artifacts/v1/namespaces/[namespace]/artifacts:list HTTP/1.1 &RegionId=cn-wulan-env***-d01 &namespace=flinkteam &workspace=default
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "data":"
{\"@type\":\"type.googleapis.com/vvp.artifacts.v1.ListArtifactsResponse\",\"artifacts\": [{\"filename\":\"TopSpeedWindowing.jar\",\"size\":\"0\",\"createTime\":\"2026-04- 29T09:20:14Z\",\"uploader\":\"235406976657057054\",\"namespace\":\"namespaces/flinkteam\", uri\":\"oss://flink-fullymanaged- 9cuwr9g7y1hl19/artifacts/namespaces/flinkteam/TopSpeedWindowing.jar\",\"content\":\"\"}]}"
 "requestId":"CBC799F0-AS7S-1D30-8A4F-882ED4DD****",
 "success":true
}
```

`XML` 格式

```xml
<data> {&quot;@type&quot;:&quot;type.googleapis.com/vvp.artifacts.v1.ListArtifactsResponse&quot;, uot;artifacts&quot;: [{&quot;filename&quot;:&quot;TopSpeedWindowing.jar&quot;,&quot;size&quot;:&quot;0&quot;,&q t;createTime&quot;:&quot;2026-04- 29T09:20:14Z&quot;,&quot;uploader&quot;:&quot;235406976657057054&quot;,&quot;namespace&quo :&quot;namespaces/flinkteam&quot;,&quot;uri&quot;:&quot;oss://flink-fullymanaged- 9cuwr9g7y1hl19/artifacts/namespaces/flinkteam/TopSpeedWindowing.jar&quot;,&quot;content&qu ;:&quot;&quot;}]}</data> <requestId>CBC799F0-AS7S-1D30-8A4F-882ED4DD****</requestId> <success>true</success>
```

###### GetUdfArtifact

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
GET /pop/workspaces/[workspace]/sql/v1beta1/namespaces/[namespace]/udfartifacts/[udfArtifactNa ] HTTP/1.1
```

**请求参数**

实时计算（流计算） 参考

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | String | Host | 是 | cn-wulan-env***-d01 | Region ID。 |
| requireFu nctionNa mes | Boole an | Query | 是 | true | 是否返回funtion名称信息。 |
| workspace | String | Path | 是 | default | 作业所在的工作空间ID。您可以通过以下任意一种方式获取： 通过ListNamespaces获取。 在Flink全托管开发控制台工作空间详情中获取。 |
| namespac e | String | Path | 是 | flinkteam | 作业所在的项目空间名称。 |
| udfArtifact Name | String | Path | 是 | metric-transform-227- shaded | udf名称。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| data | String | { "@type": "type.googleapis.c om/vvp.sql.v1beta 1.GetUdfArtifactRe sponse", "udfArtifact": { "dependencyJarUris ": [], "udfClasses": [ { "functionNames": [ "TimestampProbe" ], "udfArtifactName": "namespaces/flinkt eam/udfartifacts/m etric-transform- 227-shaded", "className": "com.alibaba.blink. udtf.TimestampPro be", "classType": "UDF TYPE SCALA _ _ R" }, { "functionNames": [ "TransformUdtf" ], "udfArtifactName": "namespaces/flinkt eam/udfartifacts/m etric-transform- 227-shaded", "className": "com.alibaba.blink. udtf.TransformUdtf ", "classType": | 详细信息。 |

实时计算（流计算） 参考

| da a | S g | , c ass ype |  |
|---|---|---|---|
| 参数名称 | 类型 | "UDF TYPE TABLE" 示例_ _ } ], "artifactType": | 说明 |
|  |  | "ARTIFACT TYPE JA _ _ VA", "createTime": "2024-03- 08T08:13:54Z", "uploader": "22347490986944 5380", "jarUpdateTime": "2024-03- 08T08:13:57Z", "name": "namespaces/flinkt eam/udfartifacts/m etric-transform- 227-shaded", "namespace": |  |
|  |  | "namespaces/flinkt eam", "jarUrl": "hdfs:///vvp/data/sq l- artifacts/namespac es/flinkteam/udfs/ metric-transform- 227-shaded/2024- 03-08T08-13- 54.732313Z/metric -transform-2.2.7- shaded.jar", "updateTime": "2024-03- 08T08:13:57Z" } } |  |
| requestId | String | C44A1880-5138- 4204-9165- DC65C4B059C2 | 请求ID。 |
| success | Boolean | true | 请求是否成功。 |

**示例**

请求示例

```
GET /pop/workspaces/[workspace]/sql/v1beta1/namespaces/[namespace]/udfartifacts/[udfArtifactNa ] HTTP/1.1 &RegionId=cn-wulan-env***-d01 &requireFunctionNames=true &workspace=default &namespace=flinkteam &udfArtifactName=metric-transform-227-shaded
```

&公共请求参数正常返回示例 `JSON` 格式实时计算（流计算） 参考

```json
{
 "data":"
{\"@type\":\"type.googleapis.com/vvp.sql.v1beta1.GetUdfArtifactResponse\",\"udfArtifact\" {\"dependencyJarUris\":[],\"udfClasses\":[{\"functionNames\": [\"TimestampProbe\"],\"udfArtifactName\":\"namespaces/flinkteam/udfartifacts/metrictransform-227shaded\",\"className\":\"com.alibaba.blink.udtf.TimestampProbe\",\"classType\":\"UDF_TYPE_ ALAR\"},{\"functionNames\": [\"TransformUdtf\"],\"udfArtifactName\":\"namespaces/flinkteam/udfartifacts/metrictransform-227shaded\",\"className\":\"com.alibaba.blink.udtf.TransformUdtf\",\"classType\":\"UDF_TYPE_T LE\"}],\"artifactType\":\"ARTIFACT_TYPE_JAVA\",\"createTime\":\"2024-03- 08T08:13:54Z\",\"uploader\":\"223474909869445380\",\"jarUpdateTime\":\"2024-03- 08T08:13:57Z\",\"name\":\"namespaces/flinkteam/udfartifacts/metric-transform-227shaded\",\"namespace\":\"namespaces/flinkteam\",\"jarUrl\":\"hdfs:///vvp/data/sqlartifacts/namespaces/flinkteam/udfs/metric-transform-227-shaded/2024-03-08T08-13- 54.732313Z/metric-transform-2.2.7-shaded.jar\",\"updateTime\":\"2024-03- 08T08:13:57Z\"}}",
 "requestId":"C44A1880-5138-4204-9165-DC65C4B059C2",
 "success":true
}
```

`XML` 格式

```xml
<data> {&quot;@type&quot;:&quot;type.googleapis.com/vvp.sql.v1beta1.GetUdfArtifactResponse&quot;, uot;udfArtifact&quot;:{&quot;dependencyJarUris&quot;:[],&quot;udfClasses&quot;: [{&quot;functionNames&quot;: [&quot;TimestampProbe&quot;],&quot;udfArtifactName&quot;:&quot;namespaces/flinkteam/udfart acts/metric-transform-227shaded&quot;,&quot;className&quot;:&quot;com.alibaba.blink.udtf.TimestampProbe&quot;,&quot lassType&quot;:&quot;UDF_TYPE_SCALAR&quot;},{&quot;functionNames&quot;: [&quot;TransformUdtf&quot;],&quot;udfArtifactName&quot;:&quot;namespaces/flinkteam/udfarti cts/metric-transform-227shaded&quot;,&quot;className&quot;:&quot;com.alibaba.blink.udtf.TransformUdtf&quot;,&quot; assType&quot;:&quot;UDF_TYPE_TABLE&quot;}],&quot;artifactType&quot;:&quot;ARTIFACT_TYPE_JA &quot;,&quot;createTime&quot;:&quot;2024-03- 08T08:13:54Z&quot;,&quot;uploader&quot;:&quot;223474909869445380&quot;,&quot;jarUpdateTime uot;:&quot;2024-03- 08T08:13:57Z&quot;,&quot;name&quot;:&quot;namespaces/flinkteam/udfartifacts/metrictransform-227shaded&quot;,&quot;namespace&quot;:&quot;namespaces/flinkteam&quot;,&quot;jarUrl&quot;:&qu ;hdfs:///vvp/data/sql-artifacts/namespaces/flinkteam/udfs/metric-transform-227shaded/2024-03-08T08-13-54.732313Z/metric-transform-2.2.7shaded.jar&quot;,&quot;updateTime&quot;:&quot;2024-03-08T08:13:57Z&quot;}}</data> <requestId>C44A1880-5138-4204-9165-DC65C4B059C2</requestId> <success>true</success>
```

###### GetTable

实时计算（流计算） 参考

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
GET /pop/workspaces/[workspace]/catalog/v1beta2/namespaces/[namespace]/catalogs/[cat]:getTable HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | String | Host | 是 | cn-wulan-env***-d01 | Region ID。 |
| namespac e | String | Path | 是 | ververica | 作业所在的项目空间名称。 |
| workspace | String | Path | 是 | default | 作业所在的工作空间ID。您可以通过以下任意一种方式获取： 通过ListNamespaces获取。 在Flink全托管开发控制台工作空间详情中获取。 |
| cat | String | Path | 是 | vvp | catalog名称。 |
| database | String | Query | 是 | default | database名称。 |
| table | String | Query | 是 | mydatahub | table名称。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|

实时计算（流计算） 参考

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| data | String | { "@type": "type.googleapis.c om/vvp.sql.catalog. v1beta2.GetTableR esponse", "table": { "name": "mydatahub", "schema": { "column": [ { "name": "strname", "type": "VARCHAR(214748 3647)", "expression": "" } ], "watermarkSpec": [] }, "properties": { "accessId": "SVw******PtL", "endpoint": "https://datahub.cn -wulan-env188- d01.dh.inter.env18 8.shuguang.com", "connector": "datahub", "accessKey": "RfE******VMB", "project": "datahub", "topic": "mysource" }, "comment": "" }, "success": true, "message": "" } | 详细信息。 |
| requestId | String | FCB6D11E-8FAA- 48F7-8E25- 28218A6878F5 | 请求ID。 |
| success | Boolean | true | 请求是否成功。 |

**示例**

请求示例

```
GET /pop/workspaces/[workspace]/catalog/v1beta2/namespaces/[namespace]/catalogs/[cat]:getTable HTTP/1.1 &RegionId=cn-wulan-env***-d01 &namespace=ververica &workspace=default &cat=vvp &database=default &table=mydatahub
```

&公共请求参数正常返回示例 `JSON` 格式实时计算（流计算） 参考

```json
{
 "data":"
{\"@type\":\"type.googleapis.com/vvp.sql.catalog.v1beta2.GetTableResponse\",\"table\":{ \"name\":\"mydatahub\",\"schema\":{\"column\": [{\"name\":\"strname\",\"type\":\"VARCHAR(2147483647)\",\"expression\":\"\"}],\"watermarkS c\":[]},\"properties\": {\"accessId\":\"SVw******PtL\",\"endpoint\":\"https://datahub.cn-wulan-env188d01.dh.inter.env188.shuguang.com\",\"connector\":\"datahub\",\"accessKey\":\"RfE******VMB\ \"project\":\"datahub\",\"topic\":\"mysource\"},\"comment\":\"\"},\"success\":true,\"messa \":\"\"}",
 "requestId":"FCB6D11E-8FAA-48F7-8E25-28218A6878F5",
 "success":true
}
```

`XML` 格式

```xml
<data> {&quot;@type&quot;:&quot;type.googleapis.com/vvp.sql.catalog.v1beta2.GetTableResponse&quot &quot;table&quot;:{&quot;name&quot;:&quot;mydatahub&quot;,&quot;schema&quot;: {&quot;column&quot;: [{&quot;name&quot;:&quot;strname&quot;,&quot;type&quot;:&quot;VARCHAR(2147483647)&quot;,&q t;expression&quot;:&quot;&quot;}],&quot;watermarkSpec&quot;:[]},&quot;properties&quot;: {&quot;accessId&quot;:&quot;SVw******PtL&quot;,&quot;endpoint&quot;:&quot;https://datahub -wulan-env188d01.dh.inter.env188.shuguang.com&quot;,&quot;connector&quot;:&quot;datahub&quot;,&quot;acc sKey&quot;:&quot;RfE******VMB&quot;,&quot;project&quot;:&quot;datahub&quot;,&quot;topic&qu ;:&quot;mysource&quot;},&quot;comment&quot;:&quot;&quot;},&quot;success&quot;:true,&quot;m sage&quot;:&quot;&quot;}</data> <requestId>FCB6D11E-8FAA-48F7-8E25-28218A6878F5</requestId> <success>true</success>
```

###### GetResourcePlan

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
GET /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/deployments/[deploymentId]/resou e_plan HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | String | Host | 是 | cn-wulan-env***-d01 | Region ID。 |

| 实时计算（流计 | 算） |  |  | Flink | 存算分离版开发指南·OpenAP |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| workspace | String | Path | 是 | default | 作业所在的工作空间ID。您可以通过以下任意一种方式获取： 通过ListNamespaces获取。 在Flink全托管开发控制台工作空间详情中获取。 |
| namespac e | String | Path | 是 | flinkteam | 作业所在的项目空间名称。 |
| deployme ntId | String | Path | 是 | d0b3abf0-4bfe-46b1- a324-5b7def580c00 | 作业deploymentId。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| success | Boolean | true | 请求是否成功。 |
| data | String | { "success": true, "message": "", "plan": "" } | 作业资源配置计划详细信息。 |
| requestId | String | 87589423-CE39- 470D-81EA- 5AB477CF4CD4 | 请求ID。 |

**示例**

请求示例

```
GET /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/deployments/[deploymentId]/resou e_plan HTTP/1.1 &RegionId=cn-wulan-env***-d01 &workspace=default &namespace=flinkteam &deploymentId=d0b3abf0-4bfe-46b1-a324-5b7def580c00
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "data":"{\"success\":true,\"message\":\"\",\"plan\":\"\"}",
 "success":true,
 "requestId":"87589423-CE39-470D-81EA-5AB477CF4CD4"
}
```

实时计算（流计算） 参考 `XML` 格式

```xml
<data> {&quot;success&quot;:true,&quot;message&quot;:&quot;&quot;,&quot;plan&quot;:&quot;&quot;} </data> <success>true</success> <requestId>87589423-CE39-470D-81EA-5AB477CF4CD4</requestId>
```

###### GetGlobalDeploymentDefaults

调用GetGlobalDeploymentDefaults，获取实时计算服务中的全局部署默认配置。

**请求头**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| namespac e | String | Header | 是 | flinkteam | 作业所在的项目空间名称。 |

**请求语法**

```
GET /pop/workspaces/[workspace]/api/v1/global-deployment-defaults HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | String | Host | 是 | cn-wulan-env***-d01 | Region ID。 |
| workspace | String | Path | 是 | default | 作业所在的工作空间ID。您可以通过以下任意一种方式获取： 通过ListNamespaces获取。 在Flink全托管开发控制台工作空间详情中获取。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | String | CBC799F0-AS7S- 1D30-8A4F- 882ED4DD**** | 请求ID。 |

实时计算（流计算） 参考

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| data | String | { "apiVersion": "v1", "kind": "GlobalDeployment Defaults", "spec": { "template": { "metadata": { "annotations": { "native.kubernetes. mode": "true", "flink.queryable- state.enabled": "false", "flink.security.ssl.e nabled": "false" } }, "spec": { "artifact": { "kind": "JAR", "imageUserDefined ": false }, "parallelism": 1, "resources": { "jobmanager": { "memory": "4Gi", "cpu": 1.0 }, "taskmanager": { "memory": "4Gi", "cpu": 1.0 } }, "logging": { "log4jLoggers": { "": "INFO" }, "logReservePolicy": { "expirationDays": 7, "openHistory": true }, "loggingProfile": "default" }, "flinkConfiguration" : {} } }, "restoreStrategy": { "kind": "LATEST STATE", _ "allowNonRestored State": false }, "state": "CANCELLED", "upgradeStrategy": { "kind": "STATELESS" }, "maxSavepointCre ationAttempts": 4, "maxJobCreationAt tempts": 1 } } | 详细信息。 |
| success | Boolean | true | 请求是否成功。 |

**示例**

请求示例实时计算（流计算） 参考

```
GET /pop/workspaces/[workspace]/api/v1/global-deployment-defaults HTTP/1.1 &RegionId=cn-wulan-env***-d01 &workspace=default
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "data":"{\"apiVersion\":\"v1\",\"kind\":\"GlobalDeploymentDefaults\",\"spec\":
{\"template\":{\"metadata\":{\"annotations\": {\"native.kubernetes.mode\":\"true\",\"flink.queryablestate.enabled\":\"false\",\"flink.security.ssl.enabled\":\"false\"}},\"spec\": {\"artifact\": {\"kind\":\"JAR\",\"imageUserDefined\":false},\"parallelism\":1,\"resources\": {\"jobmanager\":{\"memory\":\"4Gi\",\"cpu\":1.0},\"taskmanager\": {\"memory\":\"4Gi\",\"cpu\":1.0}},\"logging\":{\"log4jLoggers\": {\"\":\"INFO\"},\"logReservePolicy\": {\"expirationDays\":7,\"openHistory\":true},\"loggingProfile\":\"default\"},\"flinkConfigu tion\":{}}},\"restoreStrategy\": {\"kind\":\"LATEST_STATE\",\"allowNonRestoredState\":false},\"state\":\"CANCELLED\",\"upgr eStrategy\": {\"kind\":\"STATELESS\"},\"maxSavepointCreationAttempts\":4,\"maxJobCreationAttempts\":1}
 "requestId":"CBC799F0-AS7S-1D30-8A4F-882ED4DD****",
 "success":true
}
```

`XML` 格式

```xml
<data> {&quot;apiVersion&quot;:&quot;v1&quot;,&quot;kind&quot;:&quot;GlobalDeploymentDefaults&quo ,&quot;spec&quot;:{&quot;template&quot;:{&quot;metadata&quot;:{&quot;annotations&quot;: {&quot;native.kubernetes.mode&quot;:&quot;true&quot;,&quot;flink.queryablestate.enabled&quot;:&quot;false&quot;,&quot;flink.security.ssl.enabled&quot;:&quot;false&q t;}},&quot;spec&quot;:{&quot;artifact&quot;: {&quot;kind&quot;:&quot;JAR&quot;,&quot;imageUserDefined&quot;:false},&quot;parallelism&qu ;:1,&quot;resources&quot;:{&quot;jobmanager&quot;: {&quot;memory&quot;:&quot;4Gi&quot;,&quot;cpu&quot;:1.0},&quot;taskmanager&quot;: {&quot;memory&quot;:&quot;4Gi&quot;,&quot;cpu&quot;:1.0}},&quot;logging&quot;: {&quot;log4jLoggers&quot;:{&quot;&quot;:&quot;INFO&quot;},&quot;logReservePolicy&quot;: {&quot;expirationDays&quot;:7,&quot;openHistory&quot;:true},&quot;loggingProfile&quot;:&qu ;default&quot;},&quot;flinkConfiguration&quot;:{}}},&quot;restoreStrategy&quot;: {&quot;kind&quot;:&quot;LATEST_STATE&quot;,&quot;allowNonRestoredState&quot;:false},&quot; ate&quot;:&quot;CANCELLED&quot;,&quot;upgradeStrategy&quot;: {&quot;kind&quot;:&quot;STATELESS&quot;},&quot;maxSavepointCreationAttempts&quot;:4,&quot; xJobCreationAttempts&quot;:1}}</data> <requestId>CBC799F0-AS7S-1D30-8A4F-882ED4DD****</requestId> <success>true</success>
```

实时计算（流计算） 参考

###### GetFunction

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
GET /pop/workspaces/[workspace]/catalog/v1beta2/namespaces/[namespace]/catalogs/[cat]:getFunct n HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | String | Host | 是 | cn-wulan-env***-d01 | Region ID。 |
| namespac e | String | Path | 是 | flinkteam | 作业所在的项目空间名称。 |
| workspace | String | Path | 是 | default | 作业所在的工作空间ID。您可以通过以下任意一种方式获取： 通过ListNamespaces获取。 在Flink全托管开发控制台工作空间详情中获取。 |
| cat | String | Path | 是 | vvp | catalog名称。 |
| database | String | Query | 是 | default | database名称。 |
| function | String | Query | 是 | TransformUdtf | function名称。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|

实时计算（流计算） 参考

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| data | String | { "@type": "type.googleapis.c om/vvp.sql.catalog. v1beta2.GetFunctio nResponse", "function": { "name": "TransformUdtf", "className": "com.alibaba.blink. udtf.TransformUdtf ", "functionLanguage ": "FUNCTION LANGU _ AGE JAVA", _ "functionType": "FUNCTION TYPE F _ _ LINK", "description": "This is a user-defined function" }, "success": true, "message": "" } | 详细信息。 |
| requestId | String | DD2A9970-CED3- 4AD6-B0F6- 8DFDD84AC6AC | 请求ID。 |
| success | Boolean | true | 请求是否成功。 |

**示例**

请求示例

```
GET /pop/workspaces/[workspace]/catalog/v1beta2/namespaces/[namespace]/catalogs/[cat]:getFunct n HTTP/1.1 &RegionId=cn-wulan-env***-d01 &namespace=flinkteam &workspace=default &cat=vvp &database=default &function=TransformUdtf
```

&公共请求参数正常返回示例 `JSON` 格式实时计算（流计算） 参考

```json
{
 "data":"
{\"@type\":\"type.googleapis.com/vvp.sql.catalog.v1beta2.GetFunctionResponse\",\"function\ {\"name\":\"TransformUdtf\",\"className\":\"com.alibaba.blink.udtf.TransformUdtf\",\"funct nLanguage\":\"FUNCTION_LANGUAGE_JAVA\",\"functionType\":\"FUNCTION_TYPE_FLINK\",\"descript n\":\"This is a user-defined function\"},\"success\":true,\"message\":\"\"}",
 "requestId":"DD2A9970-CED3-4AD6-B0F6-8DFDD84AC6AC",
 "success":true
}
```

`XML` 格式

```xml
<data> {&quot;@type&quot;:&quot;type.googleapis.com/vvp.sql.catalog.v1beta2.GetFunctionResponse&q t;,&quot;function&quot;: {&quot;name&quot;:&quot;TransformUdtf&quot;,&quot;className&quot;:&quot;com.alibaba.blink tf.TransformUdtf&quot;,&quot;functionLanguage&quot;:&quot;FUNCTION_LANGUAGE_JAVA&quot;,&qu ;functionType&quot;:&quot;FUNCTION_TYPE_FLINK&quot;,&quot;description&quot;:&quot;This is a user-defined function&quot;},&quot;success&quot;:true,&quot;message&quot;:&quot;&quot;}</data> <requestId>DD2A9970-CED3-4AD6-B0F6-8DFDD84AC6AC</requestId> <success>true</success>
```

###### GetDeploymentDefaults

调用GetDeploymentDefaults，查询实时计算中指定命名空间和工作区的部署默认配置。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
GET /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/deployment-defaults HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | String | Host | 是 | cn-wulan-env***-d01 | Region ID。 |
| namespac e | String | Path | 是 | flinkteam | 作业所在的项目空间名称。 |

实时计算（流计算） 参考

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| workspace | String | Path | 是 | default | 作业所在的工作空间ID。您可以通过以下任意一种方式获取： 通过ListNamespaces获取。 在Flink全托管开发控制台工作空间详情中获取。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | String | CBC799F0-AS7S- 1D30-8A4F- 882ED4DD**** | 请求ID。 |

实时计算（流计算） 参考

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| data | String | { "metadata": { "createdAt": "2026- 04-24T03:46:53Z", "workspace": "9cuwr9g7y1hl19", "modifiedAt": "2026-04- 24T03:46:53Z", "resourceVersion": 1, "name": "stream", "namespace": "flinkteam", "annotations": { "deployment.defaul ts.type": "stream", "creator": "system", "modifier": "system" }, "id": "690e3396-700a- 4b77-9fcf- d14a592f****", "labels": {} }, "apiVersion": "v1", "kind": "DeploymentDefaul ts", "spec": { "template": { "spec": { "resources": {}, "flinkConfiguration" : { "execution.checkpo inting.interval": "180s", "table.exec.state.ttl ": "36 h", "restart- strategy.fixed- delay.delay": "10 s", "restart- strategy.fixed- delay.attempts": "2147483647", "execution.checkpo inting.min-pause": "180s", "restart- strategy": "fixed- delay" } } } } } | 详细信息。 |
| success | Boolean | true | 请求是否成功。 |

**示例**

请求示例实时计算（流计算） 参考

```
GET /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/deployment-defaults HTTP/1.1 &RegionId=cn-wulan-env***-d01 &namespace=flinkteam &workspace=default
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "data":"{\"metadata\":{\"createdAt\":\"2026-04-
24T03:46:53Z\",\"workspace\":\"9cuwr9g7y1hl19\",\"modifiedAt\":\"2026-04- 24T03:46:53Z\",\"resourceVersion\":1,\"name\":\"stream\",\"namespace\":\"flinkteam\",\"ann ations\": {\"deployment.defaults.type\":\"stream\",\"creator\":\"system\",\"modifier\":\"system\"},\ d\":\"690e3396-700a-4b77-9fcf-d14a592f****\",\"labels\": {}},\"apiVersion\":\"v1\",\"kind\":\"DeploymentDefaults\",\"spec\":{\"template\": {\"spec\":{\"resources\":{},\"flinkConfiguration\": {\"execution.checkpointing.interval\":\"180s\",\"table.exec.state.ttl\":\"36 h\",\"restart-strategy.fixed-delay.delay\":\"10 s\",\"restart-strategy.fixeddelay.attempts\":\"2147483647\",\"execution.checkpointing.minpause\":\"180s\",\"restart-strategy\":\"fixed-delay\"}}}}}",
 "requestId":"CBC799F0-AS7S-1D30-8A4F-882ED4DD****",
 "success":true
}
```

`XML` 格式

```xml
<data>{&quot;metadata&quot;:{&quot;createdAt&quot;:&quot;2026-04- 24T03:46:53Z&quot;,&quot;workspace&quot;:&quot;9cuwr9g7y1hl19&quot;,&quot;modifiedAt&quot; quot;2026-04- 24T03:46:53Z&quot;,&quot;resourceVersion&quot;:1,&quot;name&quot;:&quot;stream&quot;,&quot amespace&quot;:&quot;flinkteam&quot;,&quot;annotations&quot;: {&quot;deployment.defaults.type&quot;:&quot;stream&quot;,&quot;creator&quot;:&quot;system& ot;,&quot;modifier&quot;:&quot;system&quot;},&quot;id&quot;:&quot;690e3396-700a-4b77- 9fcf-d14a592f****&quot;,&quot;labels&quot;: {}},&quot;apiVersion&quot;:&quot;v1&quot;,&quot;kind&quot;:&quot;DeploymentDefaults&quot;, uot;spec&quot;:{&quot;template&quot;:{&quot;spec&quot;:{&quot;resources&quot;: {},&quot;flinkConfiguration&quot;: {&quot;execution.checkpointing.interval&quot;:&quot;180s&quot;,&quot;table.exec.state.ttl& ot;:&quot;36 h&quot;,&quot;restart-strategy.fixed-delay.delay&quot;:&quot;10 s&quot;,&quot;restart-strategy.fixeddelay.attempts&quot;:&quot;2147483647&quot;,&quot;execution.checkpointing.minpause&quot;:&quot;180s&quot;,&quot;restart-strategy&quot;:&quot;fixed-delay&quot;}}}}}< /data> <requestId>CBC799F0-AS7S-1D30-8A4F-882ED4DD****</requestId> <success>true</success>
```

###### GetDeployment

实时计算（流计算） 参考

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
GET /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/deployments/[deploymentId] HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | String | Host | 是 | cn-wulan-env***-d01 | Region ID。 |
| namespac e | String | Path | 是 | flinkteam | 作业所在的项目空间名称。 |
| deployme ntId | String | Path | 是 | d0b3abf0-4bfe-46b1- a324-5b7def580c00 | 作业ID。 |
| workspace | String | Path | 是 | default | 作业所在的工作空间ID。您可以通过以下任意一种方式获取： 通过ListNamespaces获取。 在Flink全托管开发控制台工作空间详情中获取。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
|  |  | { "metadata": { "createdAt": "2026- 04-24T03:47:01Z", "workspace": "9cuwr9g7y1hl19", "modifiedAt": "2026-04- 24T03:58:26Z", "resourceVersion": 174, "name": "sqlJob", "namespace": "flinkteam", "annotations": { "creator": "23540697665705 7054", "resource- plan.has.migrated" : "true", "storage.disaster.r po": "1800", "deployment.sourc |  |

实时计算（流计算） 参考

| 参数名称 | 类型 | e-type": "EDITOR", 示例 "deployment.has.d | 说明 |
|---|---|---|---|
|  |  | eployed": "false", "deployment.paren t.id": "", "modifier": "23540697665705 7054", |  |
|  |  | "creatorName": "flinkadmin", "plan.uri": "deployment/a3d8 8b2a-e076-4491- 86f2- 5a81ea4c7300/res ourcePlan.json", "priority": "5", "priority.class.nam e": "flink-p5", "migration.display. enabled": "false", "deployment.exec- plan.uri.valid": "true", "com.dataartisans. appmanager.contr oller.deployment.s pec.version": "13", "default.resource- setting.has.migrate d": "true", "deployment.refere nced.deployment.d raft.history.version ": "1", "deployment.exec- plan.uri": "oss://flink- fullymanaged- 9cuwr9g7y1hl19/fli nk- jobs/namespaces/fl inkteam/jobs/c944e 978-5cb9-4879- 8312- c0872ee50182/exe cPlan.json", "deployment.refere nced.deployment.d raft.id": "cee26b6e- d03b-4a03-a628- a6fe665c525e", "resources.from.job .has.migrated": "true", "taker": " \| vvp-0", "modifierName": "flinkadmin", "deployment.refere nced.deployment.d raft.history.id": "561a6a3d-7858- 4056-acfb- ad0cdec09e55" }, "id": "a3d88b2a- e076-4491-86f2- 5a81ea4c7300", "labels": {} }, |  |

实时计算（流计算） 参考

| 参数名称 | 类型 | "apiVersion": "v1", 示例 "kind": | 说明 |
|---|---|---|---|
| data | String | "Deployment", "spec": { "template": { "metadata": { "annotations": { "flink.resource.type ": "fine-grained", "job.resource.total. memory.byte": "0", "job.resource.total. cpu": "0.0", "native.kubernetes. mode": "true", "flink.queryable- state.enabled": "false", "flink.security.ssl.e nabled": "false" } }, "spec": { "artifact": { "flinkImageTag": "1.17.0-vvr-8.0.7- manifest-251107", "kind": "SQLSCRIPT", "sqlScript": "CREATE TEMPORARY TABLE `datahub table` _ (strname VARCHAR) with ( 'connector' = 'datagen' ); CREATE TEMPORARY TABLE `kafka table` _ (strname VARCHAR, lens BIGINT) with ( 'connector' = 'print' ); INSERT INTO kafka table _ SELECT SUBSTRING (strname, 0, 10) AS strname, CAST (CHAR LENGTH _ (strname) AS BIGINT) AS lens FROM datahub table;", _ "imageUserDefined ": false, "flinkImageRegistry ": "cn-wulan- env35-d01- reg.docker.intra.en v35.shuguang.com :80/ververica- paas", | 详细信息。 |
| > 文档版本：20260 | 730 |  | 47 |

实时计算（流计算） 参考

| 参数名称 | 类型 | "versionName": 示例 "vvr-8.0.7-flink- | 说明 |
|---|---|---|---|
|  |  | 1.17", "flinkImageReposit ory": "vvr", "flinkVersion": "1.17" }, "parallelism": 1, "batchMode": false, "resources": { "jobmanager": { "memory": "2Gi", "cpu": 0.5 }, "taskmanager": { "memory": "3Gi", "cpu": 1.0 } }, "logging": { "log4jLoggers": { "": "INFO" }, "logReservePolicy": { "expirationDays": 7, "openHistory": true }, "loggingProfile": "default" }, "flinkConfiguration" : {} } }, "restoreStrategy": { "kind": "FROM SAVEPOINT _ ", "allowNonRestored State": false, "savepointId": "5cea0d88-303d- 44e5-a96e- 47f7217723d7" }, "state": "CANCELLED", "upgradeStrategy": { "kind": "NONE" }, "maxSavepointCre ationAttempts": 4, "maxJobCreationAt tempts": 1, "deploymentTarget Id": "a89ff052- 38c6-4fd3-9b91- e9c53f8ee019" }, "status": { "startTime": 1777002980004, "state": "CANCELLED", "endTime": 0 } } |  |
| requestId | String | CBC799F0-AS7S- 1D30-8A4F- 882ED4DD**** | 请求ID。 |
| success | Boolean | true | 请求是否成功。 |

**示例**

实时计算（流计算） 参考请求示例

```
GET /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/deployments/[deploymentId] HTTP/1.1 &RegionId=cn-wulan-env***-d01 &namespace=flinkteam &deploymentId=d0b3abf0-4bfe-46b1-a324-5b7def580c00 &workspace=default
```

&公共请求参数正常返回示例 `JSON` 格式实时计算（流计算） 参考

```json
{
 "data":"{\"metadata\":{\"createdAt\":\"2026-04-
24T03:47:01Z\",\"workspace\":\"9cuwr9g7y1hl19\",\"modifiedAt\":\"2026-04- 24T03:58:26Z\",\"resourceVersion\":174,\"name\":\"sqlJob\",\"namespace\":\"flinkteam\",\"a otations\":{\"creator\":\"235406976657057054\",\"resourceplan.has.migrated\":\"true\",\"storage.disaster.rpo\":\"1800\",\"deployment.sourcetype\":\"EDITOR\",\"deployment.has.deployed\":\"false\",\"deployment.parent.id\":\"\",\"mo fier\":\"235406976657057054\",\"creatorName\":\"flinkadmin\",\"plan.uri\":\"deployment/a3d b2a-e076-4491-86f2- 5a81ea4c7300/resourcePlan.json\",\"priority\":\"5\",\"priority.class.name\":\"flinkp5\",\"migration.display.enabled\":\"false\",\"deployment.execplan.uri.valid\":\"true\",\"com.dataartisans.appmanager.controller.deployment.spec.version :\"13\",\"default.resourcesetting.has.migrated\":\"true\",\"deployment.referenced.deployment.draft.history.version\" "1\",\"deployment.exec-plan.uri\":\"oss://flink-fullymanaged-9cuwr9g7y1hl19/flinkjobs/namespaces/flinkteam/jobs/c944e978-5cb9-4879-8312c0872ee50182/execPlan.json\",\"deployment.referenced.deployment.draft.id\":\"cee26b6e-d 03b-4a03-a628-a6fe665c525e\",\"resources.from.job.has.migrated\":\"true\",\"taker\":\"
| vvp-
0\",\"modifierName\":\"flinkadmin\",\"deployment.referenced.deployment.draft.history.id\" 561a6a3d-7858-4056-acfb-ad0cdec09e55\"},\"id\":\"a3d88b2a-e076-4491-86f2- 5a81ea4c7300\",\"labels\":{}},\"apiVersion\":\"v1\",\"kind\":\"Deployment\",\"spec\": {\"template\":{\"metadata\":{\"annotations\":{\"flink.resource.type\":\"finegrained\",\"job.resource.total.memory.byte\":\"0\",\"job.resource.total.cpu\":\"0.0\",\"na ve.kubernetes.mode\":\"true\",\"flink.queryablestate.enabled\":\"false\",\"flink.security.ssl.enabled\":\"false\"}},\"spec\": {\"artifact\":{\"flinkImageTag\":\"1.17.0-vvr-8.0.7-manifest- 251107\",\"kind\":\"SQLSCRIPT\",\"sqlScript\":\"CREATE TEMPORARY TABLE `datahub_table` (strname VARCHAR)\with (\ 'connector' = 'datagen'\);\\CREATE TEMPORARY TABLE `kafka_t able` (strname VARCHAR, lens BIGINT)\with (\ 'connector' = 'print'\);\\INSERT INTO kafka_table\SELECT SUBSTRING (strname, 0, 10) AS strname, CAST (CHAR_LENGTH (strname) A S BIGINT) AS lens\FROM\ datahub_table;\",\"imageUserDefined\":false,\"flinkImageRegistry\":\"cn-wulan-env35d01-reg.docker.intra.env35.shuguang.com:80/ververica-paas\",\"versionName\":\"vvr- 8.0.7-flink- 1.17\",\"flinkImageRepository\":\"vvr\",\"flinkVersion\":\"1.17\"},\"parallelism\":1,\"bat Mode\":false,\"resources\":{\"jobmanager\": {\"memory\":\"2Gi\",\"cpu\":0.5},\"taskmanager\": {\"memory\":\"3Gi\",\"cpu\":1.0}},\"logging\":{\"log4jLoggers\": {\"\":\"INFO\"},\"logReservePolicy\": {\"expirationDays\":7,\"openHistory\":true},\"loggingProfile\":\"default\"},\"flinkConfigu tion\":{}}},\"restoreStrategy\": {\"kind\":\"FROM_SAVEPOINT\",\"allowNonRestoredState\":false,\"savepointId\":\"5cea0d88- 303d-44e5-a96e-47f7217723d7\"},\"state\":\"CANCELLED\",\"upgradeStrategy\": {\"kind\":\"NONE\"},\"maxSavepointCreationAttempts\":4,\"maxJobCreationAttempts\":1,\"depl mentTargetId\":\"a89ff052-38c6-4fd3-9b91-e9c53f8ee019\"},\"status\": {\"startTime\":1777002980004,\"state\":\"CANCELLED\",\"endTime\":0}}",
 "requestId":"CBC799F0-AS7S-1D30-8A4F-882ED4DD****",
 "success":true
}
```

`XML` 格式

```xml
<data>{&quot;metadata&quot;:{&quot;createdAt&quot;:&quot;2026-04-
```

实时计算（流计算） 参考

|  | <data>{&quot;metadata&quot;:{&quot;createdAt&quot;:&quot;2026 04 24T03:47:01Z&quot;,&quot;workspace&quot;:&quot;9cuwr9g7y1hl19&quot;,&quot;modifiedAt&quot quot;2026-04- 24T03:58:26Z&quot;,&quot;resourceVersion&quot;:174,&quot;name&quot;:&quot;sqlJob&quot;,&q ;namespace&quot;:&quot;flinkteam&quot;,&quot;annotations&quot;: {&quot;creator&quot;:&quot;235406976657057054&quot;,&quot;resource- plan.has.migrated&quot;:&quot;true&quot;,&quot;storage.disaster.rpo&quot;:&quot;1800&quot quot;deployment.source- type&quot;:&quot;EDITOR&quot;,&quot;deployment.has.deployed&quot;:&quot;false&quot;,&quot ployment.parent.id&quot;:&quot;&quot;,&quot;modifier&quot;:&quot;235406976657057054&quot; uot;creatorName&quot;:&quot;flinkadmin&quot;,&quot;plan.uri&quot;:&quot;deployment/a3d88b e076-4491-86f2- 5a81ea4c7300/resourcePlan.json&quot;,&quot;priority&quot;:&quot;5&quot;,&quot;priority.cl .name&quot;:&quot;flink- p5&quot;,&quot;migration.display.enabled&quot;:&quot;false&quot;,&quot;deployment.exec- plan.uri.valid&quot;:&quot;true&quot;,&quot;com.dataartisans.appmanager.controller.deploy t.spec.version&quot;:&quot;13&quot;,&quot;default.resource- setting.has.migrated&quot;:&quot;true&quot;,&quot;deployment.referenced.deployment.draft. tory.version&quot;:&quot;1&quot;,&quot;deployment.exec- plan.uri&quot;:&quot;oss://flink-fullymanaged-9cuwr9g7y1hl19/flink- jobs/namespaces/flinkteam/jobs/c944e978-5cb9-4879-8312- c0872ee50182/execPlan.json&quot;,&quot;deployment.referenced.deployment.draft.id&quot;:&q ;cee26b6e-d03b-4a03-a628- a6fe665c525e&quot;,&quot;resources.from.job.has.migrated&quot;:&quot;true&quot;,&quot;tak quot;:&quot; \| vvp- 0&quot;,&quot;modifierName&quot;:&quot;flinkadmin&quot;,&quot;deployment.referenced.deplo nt.draft.history.id&quot;:&quot;561a6a3d-7858-4056-acfb- ad0cdec09e55&quot;},&quot;id&quot;:&quot;a3d88b2a-e076-4491-86f2- 5a81ea4c7300&quot;,&quot;labels&quot;: {}},&quot;apiVersion&quot;:&quot;v1&quot;,&quot;kind&quot;:&quot;Deployment&quot;,&quot;s &quot;:{&quot;template&quot;:{&quot;metadata&quot;:{&quot;annotations&quot;: {&quot;flink.resource.type&quot;:&quot;fine- grained&quot;,&quot;job.resource.total.memory.byte&quot;:&quot;0&quot;,&quot;job.resource tal.cpu&quot;:&quot;0.0&quot;,&quot;native.kubernetes.mode&quot;:&quot;true&quot;,&quot;f k.queryable- state.enabled&quot;:&quot;false&quot;,&quot;flink.security.ssl.enabled&quot;:&quot;false& t;}},&quot;spec&quot;:{&quot;artifact&quot;:{&quot;flinkImageTag&quot;:&quot;1.17.0-vvr -8.0.7-manifest- 251107&quot;,&quot;kind&quot;:&quot;SQLSCRIPT&quot;,&quot;sqlScript&quot;:&quot;CREATE TEMPORARY TABLE `datahub table` (strname VARCHAR)with ( &#x27;connector&#x27; = _ &#x27;datagen&#x27;);CREATE TEMPORARY TABLE `kafka table` (strname VARCHAR, lens _ BIGINT)with ( &#x27;connector&#x27; = &#x27;print&#x27;);INSERT INTO kafka tableSELECT SUBSTRING (strname, 0, 10) AS strname, CAST (CHAR LENGTH (strname) AS _ _ BIGINT) AS lensFROM datahub table;&quot;,&quot;imageUserDefined&quot;:false,&quot;flinkImageRegistry&quot;:&q _ ;cn-wulan-env35-d01-reg.docker.intra.env35.shuguang.com:80/ververica- paas&quot;,&quot;versionName&quot;:&quot;vvr-8.0.7-flink- 1.17&quot;,&quot;flinkImageRepository&quot;:&quot;vvr&quot;,&quot;flinkVersion&quot;:&quo .17&quot;},&quot;parallelism&quot;:1,&quot;batchMode&quot;:false,&quot;resources&quot;: {&quot;jobmanager&quot;: {&quot;memory&quot;:&quot;2Gi&quot;,&quot;cpu&quot;:0.5},&quot;taskmanager&quot;: {&quot;memory&quot;:&quot;3Gi&quot;,&quot;cpu&quot;:1.0}},&quot;logging&quot;: {&quot;log4jLoggers&quot;:{&quot;&quot;:&quot;INFO&quot;},&quot;logReservePolicy&quot;: {&quot;expirationDays&quot;:7,&quot;openHistory&quot;:true},&quot;loggingProfile&quot;:&q ;default&quot;},&quot;flinkConfiguration&quot;:{}}},&quot;restoreStrategy&quot;: | ; u ; ; , 2 a m h u e y p l q u t u |
|---|---|---|

实时计算（流计算） 参考

```xml
{&quot;kind&quot;:&quot;FROM_SAVEPOINT&quot;,&quot;allowNonRestoredState&quot;:false,&quot avepointId&quot;:&quot;5cea0d88-303d-44e5-a96e- 47f7217723d7&quot;},&quot;state&quot;:&quot;CANCELLED&quot;,&quot;upgradeStrategy&quot;: {&quot;kind&quot;:&quot;NONE&quot;},&quot;maxSavepointCreationAttempts&quot;:4,&quot;maxJo reationAttempts&quot;:1,&quot;deploymentTargetId&quot;:&quot;a89ff052-38c6-4fd3-9b91e9c53f8ee019&quot;},&quot;status&quot;: {&quot;startTime&quot;:1777002980004,&quot;state&quot;:&quot;CANCELLED&quot;,&quot;endTime uot;:0}}</data> <requestId>CBC799F0-AS7S-1D30-8A4F-882ED4DD****</requestId> <success>true</success>
```

###### GetDefaultDatabase

调用GetDefaultDatabase，获取catalog下默认的database。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
GET /pop/workspaces/[workspace]/catalog/v1beta2/namespaces/[namespace]/catalogs/[cat]:getDefau Database HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | String | Host | 是 | cn-wulan-env***-d01 | Region ID。 |
| namespac e | String | Path | 是 | ververica | 作业所在的项目空间名称。 |
| workspace | String | Path | 是 | default | 作业所在的工作空间ID。您可以通过以下任意一种方式获取： 通过ListNamespaces获取。 在Flink全托管开发控制台工作空间详情中获取。 |
| cat | String | Path | 是 | vvp | catalog名称。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|

实时计算（流计算） 参考

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| data | String | { "@type": "type.googleapis.c om/vvp.sql.catalog. v1beta2.GetDefault DatabaseResponse ", "database": "default" } | 详细信息。 |
| requestId | String | 59F6950E-FC05- 495E-A286- 08C111EC7A4B | 请求ID。 |
| success | Boolean | true | 请求是否成功。 |

**示例**

请求示例

```
GET /pop/workspaces/[workspace]/catalog/v1beta2/namespaces/[namespace]/catalogs/[cat]:getDefau Database HTTP/1.1 &RegionId=cn-wulan-env***-d01 &namespace=ververica &workspace=default &cat=vvp
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "data":"
{\"@type\":\"type.googleapis.com/vvp.sql.catalog.v1beta2.GetDefaultDatabaseResponse\",\"da base\":\"default\"}",
 "requestId":"59F6950E-FC05-495E-A286-08C111EC7A4B",
 "success":true
}
```

`XML` 格式

```xml
<data> {&quot;@type&quot;:&quot;type.googleapis.com/vvp.sql.catalog.v1beta2.GetDefaultDatabaseRes nse&quot;,&quot;database&quot;:&quot;default&quot;}</data> <requestId>59F6950E-FC05-495E-A286-08C111EC7A4B</requestId> <success>true</success>
```

###### GetDatabase

**请求头**

实时计算（流计算） 参考该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
GET /pop/workspaces/[workspace]/catalog/v1beta2/namespaces/[namespace]/catalogs/[cat]:getDatab e HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | String | Host | 是 | cn-wulan-env***-d01 | Region ID。 |
| namespac e | String | Path | 是 | ververica | 作业所在的项目空间名称。 |
| workspace | String | Path | 是 | default | 作业所在的工作空间ID。您可以通过以下任意一种方式获取： 通过ListNamespaces获取。 在Flink全托管开发控制台工作空间详情中获取。 |
| cat | String | Path | 是 | vvp | catalog名称。 |
| database | String | Query | 是 | default | database名称。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| data | String | {"@type":"type.go ogleapis.com/vvp.s ql.catalog.v1beta2. GetDatabaseRespo nse","database": {"name":"default", "properties": {},"comment":"Th e default database"},"succes s":true,"message":" "} | 详细信息。 |
| requestId | String | CBC799F0-AS7S- 1D30-8A4F- 882ED4DD**** | 请求ID。 |
| success | Boolean | true | 请求是否成功。 |

实时计算（流计算） 参考

**示例**

请求示例

```
GET /pop/workspaces/[workspace]/catalog/v1beta2/namespaces/[namespace]/catalogs/[cat]:getDatab e HTTP/1.1 &RegionId=cn-wulan-env***-d01 &namespace=ververica &workspace=default &cat=vvp &database=default
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "data":"
{\"@type\":\"type.googleapis.com/vvp.sql.catalog.v1beta2.GetDatabaseResponse\",\"database\ {\"name\":\"default\",\"properties\":{},\"comment\":\"The default database\"},\"success\":true,\"message\":\"\"}",
 "requestId":"CBC799F0-AS7S-1D30-8A4F-882ED4DD****",
 "success":true
}
```

`XML` 格式

```xml
<data> {&quot;@type&quot;:&quot;type.googleapis.com/vvp.sql.catalog.v1beta2.GetDatabaseResponse&q t;,&quot;database&quot;:{&quot;name&quot;:&quot;default&quot;,&quot;properties&quot;: {},&quot;comment&quot;:&quot;The default database&quot;},&quot;success&quot;:true,&quot;message&quot;:&quot;&quot;}</data> <requestId>CBC799F0-AS7S-1D30-8A4F-882ED4DD****</requestId> <success>true</success>
```

###### GetCatalog

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
GET /pop/workspaces/[workspace]/catalog/v1beta2/namespaces/[namespace]/catalogs/[cat]:getCatal HTTP/1.1
```

**请求参数**

实时计算（流计算） 参考

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | String | Host | 是 | cn-wulan-env***-d01 | Region ID。 |
| namespac e | String | Path | 是 | ververica | 作业所在的项目空间名称。 |
| workspace | String | Path | 是 | default | 作业所在的工作空间ID。您可以通过以下任意一种方式获取： 通过ListNamespaces获取。 在Flink全托管开发控制台工作空间详情中获取。 |
| cat | String | Path | 是 | vvp | catalog名称。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| data | String | { "@type": "type.googleapis.c om/vvp.sql.catalog. v1beta2.GetCatalo gResponse", "catalog": { "name": "namespaces/flinkt eam/catalogs/vvp", "properties": { "defaultDatabase": "default", "type": "vvp" } } } | 详细信息。 |
| requestId | String | 0AFF0B61-35A5- 46D9-930F- 3826DCA3D3F9 | 请求ID。 |
| success | Boolean | true | 请求是否成功。 |

**示例**

请求示例

```
GET /pop/workspaces/[workspace]/catalog/v1beta2/namespaces/[namespace]/catalogs/[cat]:getCatal HTTP/1.1 &RegionId=cn-wulan-env***-d01 &namespace=ververica &workspace=default &cat=vvp
```

&公共请求参数实时计算（流计算） 参考正常返回示例 `JSON` 格式

```json
{
 "data":"
{\"@type\":\"type.googleapis.com/vvp.sql.catalog.v1beta2.GetCatalogResponse\",\"catalog\" {\"name\":\"namespaces/flinkteam/catalogs/vvp\",\"properties\": {\"type\":\"vvp\",\"defaultDatabase\":\"default\"}}}",
 "requestId":"0AFF0B61-35A5-46D9-930F-3826DCA3D3F9",
 "success":true
}
```

`XML` 格式

```xml
<data> {&quot;@type&quot;:&quot;type.googleapis.com/vvp.sql.catalog.v1beta2.GetCatalogResponse&qu ;,&quot;catalog&quot;: {&quot;name&quot;:&quot;namespaces/flinkteam/catalogs/vvp&quot;,&quot;properties&quot;: {&quot;type&quot;:&quot;vvp&quot;,&quot;defaultDatabase&quot;:&quot;default&quot;}}} </data> <requestId>0AFF0B61-35A5-46D9-930F-3826DCA3D3F9</requestId> <success>true</success>
```

###### GetArtifactMetadata

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
GET /pop/workspaces/[workspace]/artifacts/v1/namespaces/[namespace]/artifacts:getMetadata HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | String | Host | 是 | cn-wulan-env***-d01 | Region ID。 |
| namespac e | String | Path | 是 | flinkteam | 作业所在的项目空间名称。 |
| filename | String | Query | 是 | test.csv | 文件名称。 |

实时计算（流计算） 参考

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| workspace | String | Path | 是 | default | 作业所在的工作空间ID。您可以通过以下任意一种方式获取： 通过ListNamespaces获取。 在Flink全托管开发控制台工作空间详情中获取。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | String | CBC799F0-AS7S- 1D30-8A4F- 882ED4DD**** | 请求ID。 |
| data | String | { "artifact": { "filename": "TopSpeedWindowi ng.jar", "size": "0", "createTime": "2026-04- 29T09:20:14Z", "uploader": "23540697665705 7054", "namespace": "namespaces/flinkt eam", "uri": "oss://flink- fullymanaged- 9cuwr9g7y1hl19/ar tifacts/namespaces /flinkteam/TopSpee dWindowing.jar", "content": "" }, "@type": "type.googleapis.c om/vvp.artifacts.v1 .GetArtifactMetadat aResponse" } | 详细信息。 |
| success | Boolean | true | 请求是否成功。 |

**示例**

请求示例实时计算（流计算） 参考

```
GET /pop/workspaces/[workspace]/artifacts/v1/namespaces/[namespace]/artifacts:getMetadata HTTP/1.1 &RegionId=cn-wulan-env***-d01 &namespace=flinkteam &filename=test.csv &workspace=default
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "data":"{\"artifact\":
{\"filename\":\"TopSpeedWindowing.jar\",\"size\":\"0\",\"createTime\":\"2026-04- 29T09:20:14Z\",\"uploader\":\"235406976657057054\",\"namespace\":\"namespaces/flinkteam\", uri\":\"oss://flink-fullymanaged- 9cuwr9g7y1hl19/artifacts/namespaces/flinkteam/TopSpeedWindowing.jar\",\"content\":\"\"},\" ype\":\"type.googleapis.com/vvp.artifacts.v1.GetArtifactMetadataResponse\"}",
 "requestId":"CBC799F0-AS7S-1D30-8A4F-882ED4DD****",
 "success":true
}
```

`XML` 格式

```xml
<data>{&quot;artifact&quot;: {&quot;filename&quot;:&quot;TopSpeedWindowing.jar&quot;,&quot;size&quot;:&quot;0&quot;,&qu ;createTime&quot;:&quot;2026-04- 29T09:20:14Z&quot;,&quot;uploader&quot;:&quot;235406976657057054&quot;,&quot;namespace&quo :&quot;namespaces/flinkteam&quot;,&quot;uri&quot;:&quot;oss://flink-fullymanaged- 9cuwr9g7y1hl19/artifacts/namespaces/flinkteam/TopSpeedWindowing.jar&quot;,&quot;content&qu ;:&quot;&quot;},&quot;@type&quot;:&quot;type.googleapis.com/vvp.artifacts.v1.GetArtifactMe dataResponse&quot;}</data> <requestId>CBC799F0-AS7S-1D30-8A4F-882ED4DD****</requestId> <success>true</success>
```

###### GenerateResourcePlan

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/deployments/[deploymentId]/resou e_plan:generate HTTP/1.1
```

**请求参数**

实时计算（流计算） 参考

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | String | Host | 是 | cn-wulan-env***-d01 | Region ID。 |
| workspace | String | Path | 是 | default | 作业所在的工作空间ID。您可以通过以下任意一种方式获取： 通过ListNamespaces获取。 在Flink全托管开发控制台工作空间详情中获取。 |
| namespac e | String | Path | 是 | flinkteam | 作业所在的项目空间名称。 |
| deployme ntId | String | Path | 是 | d0b3abf0-4bfe-46b1- a324-5b7def58**** | 作业deploymentId。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| success | Boolean | true | 请求是否成功。 |

实时计算（流计算） 参考

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| data | String | { "success": true, "plan": " {\"ssgProfiles\": [{\"name\":\"defaul t\",\"cpu\":0.2,\"hea p\":\"768 mb\",\"offHeap\":\" 32 mb\",\"managed\": {},\"extended\": {}}],\"nodes\": [{\"id\":1,\"type\":\" StreamExecTableS ourceScan\",\"desc\ ":\"Source: datahub table[4]\", _ \"profile\": {\"group\":\"default \",\"parallelism\":1,\ "maxParallelism\":3 2768,\"minParalleli sm\":1}}, {\"id\":2,\"type\":\" StreamExecCalc\",\ "desc\":\"Calc[5]\",\ "profile\": {\"group\":\"default \",\"parallelism\":1,\ "maxParallelism\":3 2768,\"minParalleli sm\":1}}, {\"id\":3,\"type\":\" StreamExecSink\",\ "desc\":\"Sink: kafka table[6]\",\"p _ rofile\": {\"group\":\"default \",\"parallelism\":1,\ "maxParallelism\":3 2768,\"minParalleli sm\":1}}],\"edges\" : [{\"source\":1,\"tar get\":2,\"mode\":\"P IPELINED\",\"strate gy\":\"FORWARD\"} , {\"source\":2,\"targ et\":3,\"mode\":\"PI PELINED\",\"strateg y\":\"FORWARD\"}], \"vertices\": {\"717c7b8afebbfb 7137f6f0f99beb2a 94\":[1,2,3]}}" } | 资源配置计划详细信息。 |
| requestId | String | CBC799F0-AS7S- 1D30-8A4F- 882ED4DD****" | 请求ID。 |

**示例**

请求示例实时计算（流计算） 参考

```json
POST /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/deployments/[deploymentId]/resou e_plan:generate HTTP/1.1 { "RegionId":"cn-wulan-env***-d01", "workspace":"default", "namespace":"flinkteam", "deploymentId":"d0b3abf0-4bfe-46b1-a324-5b7def58****" }
```

正常返回示例 `JSON` 格式

```json
{
 "data":"{\"success\":true,\"plan\":\"{\\\"ssgProfiles\\\":
[{\\\"name\\\":\\\"default\\\",\\\"cpu\\\":0.2,\\\"heap\\\":\\\"768 mb\\\",\\\"offHeap\\\":\\\"32 mb\\\",\\\"managed\\\":{},\\\"extended\\\": {}}],\\\"nodes\\\": [{\\\"id\\\":1,\\\"type\\\":\\\"StreamExecTableSourceScan\\\",\\\"desc\\\":\\\"Source: datahub_table[4]\\\",\\\"profile\\\": {\\\"group\\\":\\\"default\\\",\\\"parallelism\\\":1,\\\"maxParallelism\\\":32768,\\\"minP allelism\\\":1}}, {\\\"id\\\":2,\\\"type\\\":\\\"StreamExecCalc\\\",\\\"desc\\\":\\\"Calc[5]\\\",\\\"profile \": {\\\"group\\\":\\\"default\\\",\\\"parallelism\\\":1,\\\"maxParallelism\\\":32768,\\\"minP allelism\\\":1}}, {\\\"id\\\":3,\\\"type\\\":\\\"StreamExecSink\\\",\\\"desc\\\":\\\"Sink: kafka_table[6]\\\",\\\"profile\\\": {\\\"group\\\":\\\"default\\\",\\\"parallelism\\\":1,\\\"maxParallelism\\\":32768,\\\"minP allelism\\\":1}}],\\\"edges\\\": [{\\\"source\\\":1,\\\"target\\\":2,\\\"mode\\\":\\\"PIPELINED\\\",\\\"strategy\\\":\\\"FO ARD\\\"}, {\\\"source\\\":2,\\\"target\\\":3,\\\"mode\\\":\\\"PIPELINED\\\",\\\"strategy\\\":\\\"FOR RD\\\"}],\\\"vertices\\\":{\\\"717c7b8afebbfb7137f6f0f99beb2a94\\\":[1,2,3]}}\"}",
 "success":true,
 "requestId":"CBC799F0-AS7S-1D30-8A4F-882ED4DD****\""
}
```

`XML` 格式实时计算（流计算） 参考

```xml
<data>{&quot;success&quot;:true,&quot;plan&quot;:&quot;{\&quot;ssgProfiles\&quot;: [{\&quot;name\&quot;:\&quot;default\&quot;,\&quot;cpu\&quot;:0.2,\&quot;heap\&quot;:\&quot 68 mb\&quot;,\&quot;offHeap\&quot;:\&quot;32 mb\&quot;,\&quot;managed\&quot;: {},\&quot;extended\&quot;:{}}],\&quot;nodes\&quot;: [{\&quot;id\&quot;:1,\&quot;type\&quot;:\&quot;StreamExecTableSourceScan\&quot;,\&quot;des &quot;:\&quot;Source: datahub_table[4]\&quot;,\&quot;profile\&quot;: {\&quot;group\&quot;:\&quot;default\&quot;,\&quot;parallelism\&quot;:1,\&quot;maxParalleli \&quot;:32768,\&quot;minParallelism\&quot;:1}}, {\&quot;id\&quot;:2,\&quot;type\&quot;:\&quot;StreamExecCalc\&quot;,\&quot;desc\&quot;:\&q t;Calc[5]\&quot;,\&quot;profile\&quot;: {\&quot;group\&quot;:\&quot;default\&quot;,\&quot;parallelism\&quot;:1,\&quot;maxParalleli \&quot;:32768,\&quot;minParallelism\&quot;:1}}, {\&quot;id\&quot;:3,\&quot;type\&quot;:\&quot;StreamExecSink\&quot;,\&quot;desc\&quot;:\&q t;Sink: kafka_table[6]\&quot;,\&quot;profile\&quot;: {\&quot;group\&quot;:\&quot;default\&quot;,\&quot;parallelism\&quot;:1,\&quot;maxParalleli \&quot;:32768,\&quot;minParallelism\&quot;:1}}],\&quot;edges\&quot;: [{\&quot;source\&quot;:1,\&quot;target\&quot;:2,\&quot;mode\&quot;:\&quot;PIPELINED\&quot; &quot;strategy\&quot;:\&quot;FORWARD\&quot;}, {\&quot;source\&quot;:2,\&quot;target\&quot;:3,\&quot;mode\&quot;:\&quot;PIPELINED\&quot;, quot;strategy\&quot;:\&quot;FORWARD\&quot;}],\&quot;vertices\&quot;: {\&quot;717c7b8afebbfb7137f6f0f99beb2a94\&quot;:[1,2,3]}}&quot;}</data> <success>true</success> <requestId>CBC799F0-AS7S-1D30-8A4F-882ED4DD****&quot;</requestId>
```

###### FunctionExists

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
GET /pop/workspaces/[workspace]/catalog/v1beta2/namespaces/[namespace]/catalogs/[cat]:function ists HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | String | Host | 是 | cn-wulan-env***-d01 | Region名称。 |
| namespac e | String | Path | 是 | ververica | 作业所在的项目空间名称。 |

实时计算（流计算） 参考

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| workspace | String | Path | 是 | default | 作业所在的工作空间ID。您可以通过以下任意一种方式获取： 通过ListNamespaces获取。 在Flink全托管开发控制台工作空间详情中获取。 |
| cat | String | Path | 是 | vvp | Catalog名称。 |
| database | String | Query | 是 | default | Database名称。 |
| function | String | Query | 是 | TransformUdtf | Function名称。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| data | String | { "@type": "type.googleapis.c om/vvp.sql.catalog. v1beta2.FunctionE xistsResponse", "exists": true } | 详细信息。 |
| requestId | String | D96DD415-AD97- 4EBA-832E- 99FADB6A4F87 | 请求ID。 |
| success | Boolean | true | 请求是否成功。 |

**示例**

请求示例

```
GET /pop/workspaces/[workspace]/catalog/v1beta2/namespaces/[namespace]/catalogs/[cat]:function ists HTTP/1.1 &RegionId=cn-wulan-env***-d01 &namespace=ververica &workspace=default &cat=vvp &database=default &function=TransformUdtf
```

&公共请求参数正常返回示例 `JSON` 格式实时计算（流计算） 参考

```json
{
 "data":"
{\"@type\":\"type.googleapis.com/vvp.sql.catalog.v1beta2.FunctionExistsResponse\",\"exists :true}",
 "requestId":"D96DD415-AD97-4EBA-832E-99FADB6A4F87",
 "success":true
}
```

`XML` 格式

```xml
<data> {&quot;@type&quot;:&quot;type.googleapis.com/vvp.sql.catalog.v1beta2.FunctionExistsRespons quot;,&quot;exists&quot;:true}</data> <requestId>D96DD415-AD97-4EBA-832E-99FADB6A4F87</requestId> <success>true</success>
```

###### ForcefullyCreateLock

调用ForcefullyCreateLock，给指定资源加锁（通常是draft）。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/locks HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | String | Host | 是 | cn-wulan-env***-d01 | Region ID。 |
| namespac e | String | Path | 是 | default | 作业所在的项目空间名称。 |
| workspace | String | Path | 是 | flinkteam | 作业所在的工作空间ID。您可以通过以下任意一种方式获取： 通过ListNamespaces获取。 在Flink全托管开发控制台工作空间详情中获取。 |
| resourceT ype | String | Query | 否 | DeploymentDraft | 欲锁定的资源类型，锁定 draft时传： DeploymentDraft。 |
| resourceId | String | Query | 否 | c6f157ac-60b9-4b38- 8bad-d435387cfd59 | 欲锁定的资源ID。 |

实时计算（流计算） 参考

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| success | Boolean | true | 请求是否成功。 |
| requestId | String | 69DEC7C2-BCE5- 4E80-8CDA- FE7ADE09AAAD | 请求ID。 |
| data | String | { "metadata": { "createdAt": "2024- 03- 12T10:16:35.16403 4Z", "modifiedAt": "2024-03- 12T10:16:35.16403 4Z", "namespace": "flinkteam", "id": "ec62ce3c-fe33- 383e-8b31- 2fe9d89af2af" }, "apiVersion": "v1", "kind": "Lock", "spec": { "holderName": "flinkadmin", "holderId": "22985261012276 3813" } } | 资源锁定详情。 |

**示例**

请求示例

```json
POST /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/locks HTTP/1.1 { "RegionId":"cn-wulan-env***-d01", "namespace":"default", "workspace":"flinkteam" }
```

正常返回示例 `JSON` 格式

```json
{
 "data":"{\"metadata\":{\"createdAt\":\"2024-03-
12T10:16:35.164034Z\",\"modifiedAt\":\"2024-03- 12T10:16:35.164034Z\",\"namespace\":\"flinkteam\",\"id\":\"ec62ce3c-fe33-383e-8b31- 2fe9d89af2af\"},\"apiVersion\":\"v1\",\"kind\":\"Lock\",\"spec\": {\"holderName\":\"flinkadmin\",\"holderId\":\"229852610122763813\"}}",
 "success":true,
 "requestId":"69DEC7C2-BCE5-4E80-8CDA-FE7ADE09AAAD"
}
```

`XML` 格式实时计算（流计算） 参考

```xml
<data>{&quot;metadata&quot;:{&quot;createdAt&quot;:&quot;2024-03- 12T10:16:35.164034Z&quot;,&quot;modifiedAt&quot;:&quot;2024-03- 12T10:16:35.164034Z&quot;,&quot;namespace&quot;:&quot;flinkteam&quot;,&quot;id&quot;:&quot c62ce3c-fe33-383e-8b31- 2fe9d89af2af&quot;},&quot;apiVersion&quot;:&quot;v1&quot;,&quot;kind&quot;:&quot;Lock&quot &quot;spec&quot;: {&quot;holderName&quot;:&quot;flinkadmin&quot;,&quot;holderId&quot;:&quot;2298526101227638 &quot;}}</data> <success>true</success> <requestId>69DEC7C2-BCE5-4E80-8CDA-FE7ADE09AAAD</requestId>
```

###### ExecuteSqlscriptsStatements

调用ExecuteSqlscriptsStatements，进行Function管理。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /pop/workspaces/[workspace]/sql/v1beta1/namespaces/[namespace]/sqlscripts:executemulti HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | String | Host | 是 | cn-wulan-env***-d01 | Region ID。 |
| workspace | String | Path | 是 | default | 作业所在的工作空间ID。您可以通过以下任意一种方式获取： 通过ListNamespaces获取。 在Flink全托管开发控制台工作空间详情中获取。 |
| namespac e | String | Path | 是 | flinkteam | 作业所在的项目空间名称。 |
| paramsJso n | String | Body | 否 | {"executeFunctionStr": ["DROP FUNCTION `TimestampProbe`"]} | 执行参数，sql脚本。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|

实时计算（流计算） 参考

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| data | String | { "@type": "type.googleapis.c om/vvp.sql.v1beta 1.ListUdfArtifactsR esponse", "udfArtifacts": [ { "name": "namespaces/flinkt eam/udfartifacts/m etric-transform- 227", "jarUrl": "hdfs:///tmp/udf/me tric-transform- 2.2.7-shaded.jar", "udfClasses": [ { "className": "com.alibaba.blink. udtf.TimestampPro be", "classType": "UDF TYPE SCALA _ _ R", "udfArtifactName": "namespaces/flinkt eam/udfartifacts/m etric-transform- 227", "functionNames": [ "TimestampProbe" ] } ], "artifactType": "ARTIFACT TYPE JA _ _ VA", "dependencyJarUris ": [], "uploader": "22985261012276 3813", "namespace": "namespaces/flinkt eam", "createTime": "2024-03- 11T02:54:25Z", "updateTime": "2024-03- 11T02:54:25Z", "jarUpdateTime": "2024-03- 11T02:54:25Z" } ] } | Function详细信息。 |
| requestId | String | 151E1A19-091A- 4317-ADF9- FDD81C735414 | 请求ID。 |
| success | Boolean | true | 请求是否成功。 |

**示例**

请求示例实时计算（流计算） 参考

```json
POST /pop/workspaces/[workspace]/sql/v1beta1/namespaces/[namespace]/sqlscripts:executemulti HTTP/1.1 { "RegionId":"cn-wulan-env***-d01", "workspace":"default", "namespace":"flinkteam" }
```

正常返回示例 `JSON` 格式

```json
{
 "data":"
{\"@type\":\"type.googleapis.com/vvp.sql.v1beta1.ListUdfArtifactsResponse\",\"udfArtifacts :[{\"name\":\"namespaces/flinkteam/udfartifacts/metric-transform- 227\",\"jarUrl\":\"hdfs:///tmp/udf/metric-transform-2.2.7-shaded.jar\",\"udfClasses\": [{\"className\":\"com.alibaba.blink.udtf.TimestampProbe\",\"classType\":\"UDF_TYPE_SCALAR\ \"udfArtifactName\":\"namespaces/flinkteam/udfartifacts/metric-transform- 227\",\"functionNames\": [\"TimestampProbe\"]}],\"artifactType\":\"ARTIFACT_TYPE_JAVA\",\"dependencyJarUris\": [],\"uploader\":\"229852610122763813\",\"namespace\":\"namespaces/flinkteam\",\"createTime :\"2024-03-11T02:54:25Z\",\"updateTime\":\"2024-03- 11T02:54:25Z\",\"jarUpdateTime\":\"2024-03-11T02:54:25Z\"}]}",
 "requestId":"151E1A19-091A-4317-ADF9-FDD81C735414",
 "success":true
}
```

`XML` 格式

```xml
<data> {&quot;@type&quot;:&quot;type.googleapis.com/vvp.sql.v1beta1.ListUdfArtifactsResponse&quot &quot;udfArtifacts&quot;: [{&quot;name&quot;:&quot;namespaces/flinkteam/udfartifacts/metric-transform- 227&quot;,&quot;jarUrl&quot;:&quot;hdfs:///tmp/udf/metric-transform-2.2.7shaded.jar&quot;,&quot;udfClasses&quot;: [{&quot;className&quot;:&quot;com.alibaba.blink.udtf.TimestampProbe&quot;,&quot;classType& ot;:&quot;UDF_TYPE_SCALAR&quot;,&quot;udfArtifactName&quot;:&quot;namespaces/flinkteam/udf tifacts/metric-transform-227&quot;,&quot;functionNames&quot;: [&quot;TimestampProbe&quot;]}],&quot;artifactType&quot;:&quot;ARTIFACT_TYPE_JAVA&quot;,&qu ;dependencyJarUris&quot;: [],&quot;uploader&quot;:&quot;229852610122763813&quot;,&quot;namespace&quot;:&quot;namespa s/flinkteam&quot;,&quot;createTime&quot;:&quot;2024-03- 11T02:54:25Z&quot;,&quot;updateTime&quot;:&quot;2024-03- 11T02:54:25Z&quot;,&quot;jarUpdateTime&quot;:&quot;2024-03-11T02:54:25Z&quot;}]}</data> <requestId>151E1A19-091A-4317-ADF9-FDD81C735414</requestId> <success>true</success>
```

###### ExecuteSqlScript

实时计算（流计算） 参考

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /pop/workspaces/[workspace]/sql/v1beta1/namespaces/[namespace]/sqlscripts:execute HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | String | Host | 是 | cn-wulan-env***-d01 | Region ID。 |
| namespac e | String | Path | 是 | flinkteam | 作业所在的项目空间名称。 |
| paramsJso n | String | Body | 否 | {"statement":"Drop TABLE `vvp`.`default`.`test`"} | 执行参数，sql脚本。 |
| workspace | String | Path | 是 | default | 作业所在的工作空间ID。您可以通过以下任意一种方式获取： 通过ListNamespaces获取。 在Flink全托管开发控制台工作空间详情中获取。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | String | CBC799F0-AS7S- 1D30-8A4F- 882ED4DD**** | 请求ID。 |
| data | String | { "@type": "type.googleapis.c om/vvp.sql.v1beta 1.ExecuteStatemen tsResponse", "responses": [{ "result": "RESULT SUCCESS _ ", "errorMessages": [] }] } | 详细信息。 |
| success | Boolean | true | 请求是否成功。 |

**示例**

请求示例实时计算（流计算） 参考

```json
POST /pop/workspaces/[workspace]/sql/v1beta1/namespaces/[namespace]/sqlscripts:execute HTTP/1.1 { "RegionId":"cn-wulan-env***-d01", "namespace":"flinkteam", "workspace":"default" }
```

正常返回示例 `JSON` 格式

```json
{
 "data":"
{\"@type\":\"type.googleapis.com/vvp.sql.v1beta1.ExecuteStatementsResponse\",\"responses\" [{\"result\":\"RESULT_SUCCESS\",\"errorMessages\":[]}]}",
 "requestId":"CBC799F0-AS7S-1D30-8A4F-882ED4DD****",
 "success":true
}
```

`XML` 格式

```xml
<data> {&quot;@type&quot;:&quot;type.googleapis.com/vvp.sql.v1beta1.ExecuteStatementsResponse&quo ,&quot;responses&quot;: [{&quot;result&quot;:&quot;RESULT_SUCCESS&quot;,&quot;errorMessages&quot;:[]}]}</data> <requestId>CBC799F0-AS7S-1D30-8A4F-882ED4DD****</requestId> <success>true</success>
```

###### DeployDeploymentDraft

调用DeployDeploymentDraft，部署实时计算任务到指定的工作区和命名空间。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/deployment-drafts/deploy HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | String | Host | 是 | cn-wulan-env***-d01 | Region ID。 |

实时计算（流计算） 参考

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| workspace | String | Path | 是 | default | 作业所在的工作空间ID。您可以通过以下任意一种方式获取： 通过ListNamespaces获取。 在Flink全托管开发控制台工作空间详情中获取。 |
| namespac e | String | Path | 是 | flinkteam | 作业所在的项目空间名称。 |
|  |  |  |  | { "metadata": { "createdAt": "2026-04- 24T03:46:53Z", "workspace": "9cuwr9g7y1hl19", "resourceVersion": 32, "name": "sqlJob", "namespace": "flinkteam", "annotations": { "migration.display.enabl ed": "false", "creator": "235406976657057054" , "modifier": "235406976657057054" , "creatorName": "flinkadmin", "modifierName": "flinkadmin", "priority": "5", "deployment.draft.refere nced.deployment.id": "7325ac07-e466-4c1b- b598-311c6f2c103b" }, "labels": {}, "lock": { "metadata": { "createdAt": "2026-04- 24T03:46:53Z", "workspace": "9cuwr9g7y1hl19", "modifiedAt": "2026-04- 24T03:46:53Z", "namespace": "flinkteam", "annotations": { "creator": "235406976657057054" , "modifier": "235406976657057054" }, "id": "313fde08-4b44- 38b5-99c4- 7f3038449796" }, "apiVersion": "v1", "kind": "Lock", "spec": { "holderName": "flinkadmin", "holderId": "235406976657057054" } }, "id": "cee26b6e- d03b-4a03-a628- a6fe665c525e", |  |

实时计算（流计算） 参考

| 参数名称 | 类型 | 位置 | 是否必选 | "parentId": "cd1562be- 示例 02ed-32cf-945b- | 说明 |
|---|---|---|---|---|---|
| paramsJso n | String | Body | 否 | 9769afe4c55e", "description": "cd1562be-02ed-32cf- 945b-9769afe4c55e" }, "spec": { "state": "CANCELLED", "upgradeStrategy": { "kind": "STATELESS" }, "restoreStrategy": { "kind": "LATEST STATE" _ }, "deploymentTargetId": "a89ff052-38c6-4fd3- 9b91-e9c53f8ee019", "maxSavepointCreationA ttempts": 4, "maxJobCreationAttempt s": 1, "template": { "metadata": { "annotations": { "flink.resource.type": "fine-grained", "native.kubernetes.mod e": "true", "flink.queryable- state.enabled": "false", "flink.security.ssl.enable d": "false" } }, "spec": { "artifact": { "kind": "SQLSCRIPT", "versionName": "vvr- 8.0.7-flink-1.17", "imageUserDefined": | 执行参数，sql脚本。 |
|  |  |  |  | false, "sqlScript": "CREATE TEMPORARY TABLE `datahub table` _ (strname VARCHAR) with ( 'connector' = 'datagen' ); CREATE TEMPORARY TABLE `kafka table` _ (strname VARCHAR, lens BIGINT) with ( 'connector' = 'print' ); INSERT INTO kafka table _ SELECT SUBSTRING (strname, 0, 10) AS strname, CAST (CHAR LENGTH _ (strname) AS BIGINT) AS lens FROM datahub table;" }, _ "parallelism": 1, "resources": { "jobmanager": { "memory": "2Gi", "cpu": 0.5 }, "taskmanager": { "memory": "3Gi", "cpu": 1.0 } }, "flinkConfiguration": {}, "logging": { |  |

实时计算（流计算） 参考

| 参数名称 | 类型 | 位置 | 是否必选 | "log4jLoggers": { "": 示例 "INFO" }, | 说明 |
|---|---|---|---|---|---|
|  |  |  |  | "logReservePolicy": { "expirationDays": 7, "openHistory": true }, "loggingProfile": "default" }, "batchMode": false } } } } |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| success | Boolean | true | 请求是否成功。 |
|  |  | { "commitResult": { "success": true, "deployment": { "metadata": { "createdAt": "2026- 04-28T01:59:31Z", "workspace": "9cuwr9g7y1hl19", "modifiedAt": "2026-04- 28T02:07:17.20581 4Z", "resourceVersion": 4, "name": "sqlJob", "namespace": "flinkteam", "annotations": { "creator": "23540697665705 7054", "resource- plan.has.migrated" : "true", "storage.disaster.r po": "1800", "deployment.has.d eployed": "false", "deployment.sourc e-type": "EDITOR", "modifier": "23540697665705 7054", "creatorName": "flinkadmin", "plan.uri": "deployment/7325 ac07-e466-4c1b- b598- 311c6f2c103b/reso urcePlan.json", "priority": "5", "priority.class.nam e": "flink-p5", "migration.display. enabled": "false", "com.dataartisans. appmanager.contr oller.deployment.s |  |

实时计算（流计算） 参考

| 参数名称 | 类型 | pec.version": "4", 示例 "default.resource- | 说明 |
|---|---|---|---|
|  |  | setting.has.migrate d": "true", "deployment.refere nced.deployment.d raft.history.version ": "3", "deployment.refere nced.deployment.d raft.id": "cee26b6e- d03b-4a03-a628- a6fe665c525e", "modifierName": "flinkadmin", "taker": " \| vvp-0", "deployment.refere nced.deployment.d raft.history.id": "5bfca9e9-a50d- 483b-bad5- 1e1d5315acaf" }, "id": "7325ac07- e466-4c1b-b598- 311c6f2c103b", "labels": {} }, "apiVersion": "v1", "kind": "Deployment", "spec": { "template": { "metadata": { "annotations": { |  |
|  |  | "flink.resource.type ": "fine-grained", "native.kubernetes. mode": "true", "flink.queryable- state.enabled": "false", "flink.security.ssl.e nabled": "false" } }, "spec": { "artifact": { "flinkImageTag": "1.17.0-vvr-8.0.7- manifest-251107", "kind": "SQLSCRIPT", "sqlScript": "CREATE TEMPORARY TABLE `datahub table` _ (strname VARCHAR) with ( 'connector' = 'datagen' ); CREATE TEMPORARY TABLE `kafka table` _ (strname VARCHAR, lens BIGINT) with ( 'connector' = |  |

实时计算（流计算） 参考

| 参数名称 | 类型 | 'print' 示例 ); | 说明 |
|---|---|---|---|
|  |  | INSERT INTO kafka table _ SELECT SUBSTRING (strname, 0, 10) AS strname, CAST (CHAR LENGTH _ (strname) AS BIGINT) AS lens FROM datahub table;", _ "imageUserDefined ": false, "flinkImageRegistry ": "cn-wulan- env35-d01- reg.docker.intra.en v35.shuguang.com :80/ververica- paas", "versionName": "vvr-8.0.7-flink- 1.17", "flinkImageReposit ory": "vvr", "flinkVersion": "1.17" }, "parallelism": 1, "batchMode": false, "resources": { "jobmanager": { "memory": "2Gi", "cpu": 0.5 }, "taskmanager": { "memory": "3Gi", "cpu": 1.0 } }, "logging": { "log4jLoggers": { "": "INFO" }, "logReservePolicy": { "expirationDays": 7, "openHistory": true }, "loggingProfile": "default" }, "flinkConfiguration" : {} } }, "restoreStrategy": { "kind": "NONE" }, "state": "RUNNING", "upgradeStrategy": { "kind": "NONE" }, "maxSavepointCre ationAttempts": 4, "maxJobCreationAt tempts": 1, "deploymentTarget Id": "a89ff052- 38c6-4fd3-9b91- e9c53f8ee019" }, "status": { "startTime": 1777341571990, "state": |  |

实时计算（流计算） 参考

| 参数名称 | 类型 | "RUNNING", 示例 "endTime": 0 } } }, | 说明 |
|---|---|---|---|
|  |  | "draftHistoryResult ": { "deploymentDraftH istory": { "metadata": { "draftId": "cee26b6e-d03b- 4a03-a628- a6fe665c525e", "workspace": "9cuwr9g7y1hl19", "modifiedAt": "2026-04- 28T02:07:17.18692 5Z", "resourceVersion": 32, "annotations": { "migration.display. enabled": "false", "creator": "23540697665705 7054", "modifier": "23540697665705 7054", "creatorName": "flinkadmin", "modifierName": "flinkadmin", "priority": "5", "deployment.draft.r eferenced.deploym ent.id": "7325ac07- e466-4c1b-b598- 311c6f2c103b" }, "description": "cd1562be-02ed- 32cf-945b- 9769afe4c55e", "version": "3", "parentId": "cd1562be-02ed- 32cf-945b- 9769afe4c55e", "labels": {}, "createdAt": "2026- 04- 28T02:07:17.18692 5Z", "name": "sqlJob", "namespace": "flinkteam", "lock": { "metadata": { "createdAt": "2026- 04-24T03:46:53Z", "modifiedAt": "2026-04- 24T03:46:53Z", "namespace": "flinkteam", "annotations": { "creator": "23540697665705 7054", "modifier": "23540697665705 |  |

实时计算（流计算） 参考

| 参数名称 | 类型 | 7054" }, "id": 示例 "313fde08-4b44- | 说明 |
|---|---|---|---|
| data | String | 38b5-99c4- 7f3038449796" }, "apiVersion": "v1", "kind": "Lock", "spec": { "holderName": "flinkadmin", "holderId": "23540697665705 7054" } }, "id": "5bfca9e9-a50d- 483b-bad5- 1e1d5315acaf", "deleteLock": 0 }, "apiVersion": "v1", "kind": "DeploymentDraftH istory", "spec": { "template": { "metadata": { "annotations": { "flink.resource.type ": "fine-grained", "native.kubernetes. mode": "true", "flink.queryable- state.enabled": "false", "flink.security.ssl.e nabled": "false" } }, "spec": { "artifact": { "kind": "SQLSCRIPT", "sqlScript": "CREATE TEMPORARY TABLE `datahub table` _ (strname VARCHAR) with ( 'connector' = 'datagen' ); CREATE TEMPORARY TABLE `kafka table` _ (strname VARCHAR, lens BIGINT) with ( 'connector' = 'print' ); INSERT INTO kafka table _ SELECT SUBSTRING (strname, 0, 10) AS strname, CAST (CHAR LENGTH _ (strname) AS BIGINT) AS lens FROM datahub table;", _ "imageUserDefined | 详细信息。 |

实时计算（流计算） 参考

| 参数名称 | 类型 | ": false, 示例 "versionName": | 说明 |
|---|---|---|---|
|  |  | "vvr-8.0.7-flink- 1.17" }, "parallelism": 1, "batchMode": false, "resources": { "jobmanager": { "memory": "2Gi", "cpu": 0.5 }, "taskmanager": { "memory": "3Gi", "cpu": 1.0 } }, "logging": { "log4jLoggers": { "": "INFO" }, "loggingProfile": "default" }, "flinkConfiguration" : {} } }, "restoreStrategy": { "kind": "LATEST STATE", _ "allowNonRestored State": false }, "state": "CANCELLED", "upgradeStrategy": { "kind": "STATELESS" }, "maxSavepointCre ationAttempts": 4, "maxJobCreationAt tempts": 1, "deploymentTarget Id": "a89ff052- 38c6-4fd3-9b91- e9c53f8ee019" } }, "success": true }, "validationResult": { "success": true, "kind": "SQLSCRIPT", "artifactValidation": { "validationResult": "VALIDATION RESU _ LT VALID INSERT _ _ _ QUERY", "errorDetails": { "columnNumber": 0, "endLineNumber": 0, "endColumnNumbe r": 0, "lineNumber": 0, "message": "" } }, "planValidation": { "resourcePlan": " {\"ssgProfiles\": [{\"name\":\"defaul t\",\"cpu\":0.2,\"hea p\":\"768 mb\",\"offHeap\":\" 32 mb\",\"managed\": {},\"extended\": |  |

实时计算（流计算） 参考

| 参数名称 | 类型 | {}}],\"nodes\": 示例 [{\"id\":1,\"type\":\" | 说明 |
|---|---|---|---|
|  |  | StreamExecTableS ourceScan\",\"desc\ ":\"Source: datahub table[22]\ _ ",\"profile\": {\"group\":\"default \",\"parallelism\":1,\ "maxParallelism\":3 2768,\"minParalleli sm\":1}}, {\"id\":2,\"type\":\" StreamExecCalc\",\ "desc\":\"Calc[23]\" ,\"profile\": {\"group\":\"default \",\"parallelism\":1,\ "maxParallelism\":3 2768,\"minParalleli sm\":1}}, {\"id\":3,\"type\":\" StreamExecSink\",\ "desc\":\"Sink: kafka table[24]\",\" _ profile\": {\"group\":\"default \",\"parallelism\":1,\ "maxParallelism\":3 2768,\"minParalleli sm\":1}}],\"edges\" : [{\"source\":1,\"tar get\":2,\"mode\":\"P IPELINED\",\"strate gy\":\"FORWARD\"} , {\"source\":2,\"targ et\":3,\"mode\":\"PI PELINED\",\"strateg y\":\"FORWARD\"}], \"vertices\": {\"717c7b8afebbfb 7137f6f0f99beb2a 94\":[1,2,3]}}", "success": true, "message": "", "execPlan": "{ \"flinkVersion\" : \"1.17-vvr-8.0.7-10- SNAPSHOT\", \"nodes\" : [ { \"id\" : 25, \"type\" : \"stream- exec-table-source- scan 1\", _ \"scanTableSource\ " : { \"table\" : { \"identifier\" : \"`vvp`.`default`.`d atahub table`\" _ }, \"factoryIdentifier\" : \"datagen\" }, \"outputType\" : |  |

实时计算（流计算） 参考

| 参数名称 | 类型 | \"ROW<`strname` 示例 VARCHAR(2147483 | 说明 |
|---|---|---|---|
|  |  | 647)>\", \"description\" : \"TableSourceScan( table=[[vvp, default, datahub table]], _ fields= [strname])\", \"inputProperties\" : [ ], \"uid\" : \"1\" }, { \"id\" : 26, \"type\" : \"stream- exec-calc 1\", _ \"projection\" : [ { \"kind\" : \"CALL\", \"internalName\" : \"$SUBSTRING$1\", \"operands\" : [ { \"kind\" : \"INPUT REF\", _ \"inputIndex\" : 0, \"type\" : \"VARCHAR(214748 3647)\" }, { \"kind\" : \"LITERAL\", \"value\" : 0, \"type\" : \"INT NOT NULL\" }, { \"kind\" : \"LITERAL\", \"value\" : 10, \"type\" : \"INT NOT NULL\" } ], \"type\" : \"VARCHAR(214748 3647)\" }, { \"kind\" : \"CALL\", \"syntax\" : \"SPECIAL\", \"internalName\" : \"$CAST$1\", \"operands\" : [ { \"kind\" : \"CALL\", \"internalName\" : \"$CHAR LENGTH$ _ 1\", \"operands\" : [ { \"kind\" : \"INPUT REF\", _ \"inputIndex\" : 0, \"type\" : \"VARCHAR(214748 3647)\" } ], \"type\" : \"INT\" } ], \"type\" : \"BIGINT\" } ], |  |

实时计算（流计算） 参考

| 参数名称 | 类型 | \"condition\" : null, 示例 \"inputProperties\" : | 说明 |
|---|---|---|---|
|  |  | [ { \"requiredDistributi ons\" : [ { \"type\" : \"UNKNOWN\" } ], \"damBehavior\" : \"PIPELINED\", \"priority\" : 0 } ], \"outputType\" : \"ROW<`strname` VARCHAR(2147483 647), `lens` BIGINT>\", \"description\" : \"Calc(select= [SUBSTRING(strna me, 0, 10) AS strname, CAST(CHAR LENGT _ H(strname) AS BIGINT) AS lens])\", \"uid\" : \"2\" }, { \"id\" : 27, \"type\" : \"stream- exec-sink 1\", _ \"configuration\" : { \"table.exec.sink.ke yed-shuffle\" : \"AUTO\", \"table.exec.sink.n ot-null-enforcer\" : \"ERROR\", \"table.exec.sink.ty pe-length- enforcer\" : \"IGNORE\", \"table.exec.sink.u psert-materialize\" : \"AUTO\" }, \"dynamicTableSin k\" : { \"table\" : { \"identifier\" : \"`vvp`.`default`.`k afka table`\" _ }, \"factoryIdentifier\" : \"print\" }, \"inputChangelogM ode\" : [ \"INSERT\" ], \"inputProperties\" : [ { \"requiredDistributi ons\" : [ { \"type\" : \"UNKNOWN\" } ], \"damBehavior\" : \"PIPELINED\", |  |

实时计算（流计算） 参考

| 参数名称 | 类型 | \"priority\" : 0 示例 } ], | 说明 |
|---|---|---|---|
|  |  | \"outputType\" : \"ROW<`strname` VARCHAR(2147483 647), `lens` BIGINT>\", \"description\" : \"Sink(table= [vvp.default.kafka _ table], fields= [strname, lens])\", \"uid\" : \"3\" } ], \"edges\" : [ { \"source\" : 25, \"target\" : 26, \"shuffle\" : { \"type\" : \"FORWARD\" }, \"shuffleMode\" : \"PIPELINED\" }, { \"source\" : 26, \"target\" : 27, \"shuffle\" : { \"type\" : \"FORWARD\" }, \"shuffleMode\" : \"PIPELINED\" } ] }" } }, "success": true } |  |
| requestId | String | CBC799F0-AS7S- 1D30-8A4F- 882ED4DD**** | 请求ID。 |

**示例**

请求示例

```json
POST /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/deployment-drafts/deploy HTTP/1.1 { "RegionId":"cn-wulan-env***-d01", "workspace":"default", "namespace":"flinkteam" }
```

正常返回示例 `JSON` 格式

```json
{
 "data":"{\"commitResult\":{\"success\":true,\"deployment\":{\"metadata\":
{\"createdAt\":\"2026-04- 28T01:59:31Z\",\"workspace\":\"9cuwr9g7y1hl19\",\"modifiedAt\":\"2026-04- 28T02:07:17.205814Z\",\"resourceVersion\":4,\"name\":\"sqlJob\",\"namespace\":\"flinkteam\ \"annotations\":{\"creator\":\"235406976657057054\",\"resource-
```

实时计算（流计算） 参考

```
plan.has.migrated\":\"true\",\"storage.disaster.rpo\":\"1800\",\"deployment.has.deployed\" "false\",\"deployment.sourcetype\":\"EDITOR\",\"modifier\":\"235406976657057054\",\"creatorName\":\"flinkadmin\",\"pla uri\":\"deployment/7325ac07-e466-4c1b-b598- 311c6f2c103b/resourcePlan.json\",\"priority\":\"5\",\"priority.class.name\":\"flinkp5\",\"migration.display.enabled\":\"false\",\"com.dataartisans.appmanager.controller.depl ment.spec.version\":\"4\",\"default.resourcesetting.has.migrated\":\"true\",\"deployment.referenced.deployment.draft.history.version\" "3\",\"deployment.referenced.deployment.draft.id\":\"cee26b6e-d03b-4a03-a628a6fe665c525e\",\"modifierName\":\"flinkadmin\",\"taker\":\" | vvp- 0\",\"deployment.referenced.deployment.draft.history.id\":\"5bfca9e9-a50d-483b-bad5- 1e1d5315acaf\"},\"id\":\"7325ac07-e466-4c1b-b598-311c6f2c103b\",\"labels\": {}},\"apiVersion\":\"v1\",\"kind\":\"Deployment\",\"spec\":{\"template\":{\"metadata\":{ \"annotations\":{\"flink.resource.type\":\"finegrained\",\"native.kubernetes.mode\":\"true\",\"flink.queryablestate.enabled\":\"false\",\"flink.security.ssl.enabled\":\"false\"}},\"spec\": {\"artifact\":{\"flinkImageTag\":\"1.17.0-vvr-8.0.7-manifest- 251107\",\"kind\":\"SQLSCRIPT\",\"sqlScript\":\"CREATE TEMPORARY TABLE `datahub_table` (strname VARCHAR)\with (\ 'connector' = 'datagen'\);\\CREATE TEMPORARY TABLE `kafka_t able` (strname VARCHAR, lens BIGINT)\with (\ 'connector' = 'print'\);\\INSERT INTO kafka_table\SELECT SUBSTRING (strname, 0, 10) AS strname, CAST (CHAR_LENGTH (strname) A S BIGINT) AS lens\FROM\ datahub_table;\",\"imageUserDefined\":false,\"flinkImageRegistry\":\"cn-wulan-env35d01-reg.docker.intra.env35.shuguang.com:80/ververica-paas\",\"versionName\":\"vvr- 8.0.7-flink- 1.17\",\"flinkImageRepository\":\"vvr\",\"flinkVersion\":\"1.17\"},\"parallelism\":1,\"bat Mode\":false,\"resources\":{\"jobmanager\": {\"memory\":\"2Gi\",\"cpu\":0.5},\"taskmanager\": {\"memory\":\"3Gi\",\"cpu\":1.0}},\"logging\":{\"log4jLoggers\": {\"\":\"INFO\"},\"logReservePolicy\": {\"expirationDays\":7,\"openHistory\":true},\"loggingProfile\":\"default\"},\"flinkConfigu tion\":{}}},\"restoreStrategy\": {\"kind\":\"NONE\"},\"state\":\"RUNNING\",\"upgradeStrategy\": {\"kind\":\"NONE\"},\"maxSavepointCreationAttempts\":4,\"maxJobCreationAttempts\":1,\"depl mentTargetId\":\"a89ff052-38c6-4fd3-9b91-e9c53f8ee019\"},\"status\": {\"startTime\":1777341571990,\"state\":\"RUNNING\",\"endTime\":0}}},\"draftHistoryResult\" {\"deploymentDraftHistory\":{\"metadata\":{\"draftId\":\"cee26b6e-d03b-4a03-a628a6fe665c525e\",\"workspace\":\"9cuwr9g7y1hl19\",\"modifiedAt\":\"2026-04- 28T02:07:17.186925Z\",\"resourceVersion\":32,\"annotations\": {\"migration.display.enabled\":\"false\",\"creator\":\"235406976657057054\",\"modifier\":\ 35406976657057054\",\"creatorName\":\"flinkadmin\",\"modifierName\":\"flinkadmin\",\"prior y\":\"5\",\"deployment.draft.referenced.deployment.id\":\"7325ac07-e466-4c1b-b598- 311c6f2c103b\"},\"description\":\"cd1562be-02ed-32cf-945b- 9769afe4c55e\",\"version\":\"3\",\"parentId\":\"cd1562be-02ed-32cf-945b- 9769afe4c55e\",\"labels\":{},\"createdAt\":\"2026-04- 28T02:07:17.186925Z\",\"name\":\"sqlJob\",\"namespace\":\"flinkteam\",\"lock\": {\"metadata\":{\"createdAt\":\"2026-04-24T03:46:53Z\",\"modifiedAt\":\"2026-04- 24T03:46:53Z\",\"namespace\":\"flinkteam\",\"annotations\": {\"creator\":\"235406976657057054\",\"modifier\":\"235406976657057054\"},\"id\":\"313fde08 4b44-38b5-99c4-7f3038449796\"},\"apiVersion\":\"v1\",\"kind\":\"Lock\",\"spec\": {\"holderName\":\"flinkadmin\",\"holderId\":\"235406976657057054\"}},\"id\":\"5bfca9e9a50d-483b-bad5- 1e1d5315acaf\",\"deleteLock\":0},\"apiVersion\":\"v1\",\"kind\":\"DeploymentDraftHistory\" "spec\":{\"template\":{\"metadata\":{\"annotations\":{\"flink.resource.type\":\"finegrained\"\"nativekubernetesmode\":\"true\"\"flinkqueryable-
```

实时计算（流计算） 参考

```
grained\,\native.kubernetes.mode\:\true\,\flink.queryable state.enabled\":\"false\",\"flink.security.ssl.enabled\":\"false\"}},\"spec\": {\"artifact\":{\"kind\":\"SQLSCRIPT\",\"sqlScript\":\"CREATE TEMPORARY TABLE `datahub_table` (strname VARCHAR)\with (\ 'connector' = 'datagen'\);\\CREATE TEMPORARY TABLE `kafka_table` (strname VARCHAR, lens BIGINT)\with (\ 'connector' = 'print'\);\\INSERT INTO kafka_table\SELECT SUBSTRING (strname, 0, 10) AS strname, CAST (CHAR_LENGTH (strname) AS BIGINT) AS lens\FROM\ datahub_table;\",\"imageUserDefined\":false,\"versionName\":\"vvr-8.0.7-flink- 1.17\"},\"parallelism\":1,\"batchMode\":false,\"resources\":{\"jobmanager\": {\"memory\":\"2Gi\",\"cpu\":0.5},\"taskmanager\": {\"memory\":\"3Gi\",\"cpu\":1.0}},\"logging\":{\"log4jLoggers\": {\"\":\"INFO\"},\"loggingProfile\":\"default\"},\"flinkConfiguration\": {}}},\"restoreStrategy\": {\"kind\":\"LATEST_STATE\",\"allowNonRestoredState\":false},\"state\":\"CANCELLED\",\"upgr eStrategy\": {\"kind\":\"STATELESS\"},\"maxSavepointCreationAttempts\":4,\"maxJobCreationAttempts\":1,\ eploymentTargetId\":\"a89ff052-38c6-4fd3-9b91e9c53f8ee019\"}},\"success\":true},\"validationResult\": {\"success\":true,\"kind\":\"SQLSCRIPT\",\"artifactValidation\": {\"validationResult\":\"VALIDATION_RESULT_VALID_INSERT_QUERY\",\"errorDetails\": {\"columnNumber\":0,\"endLineNumber\":0,\"endColumnNumber\":0,\"lineNumber\":0,\"message\" "\"}},\"planValidation\":{\"resourcePlan\":\"{\\\"ssgProfiles\\\": [{\\\"name\\\":\\\"default\\\",\\\"cpu\\\":0.2,\\\"heap\\\":\\\"768 mb\\\",\\\"offHeap\\\":\\\"32 mb\\\",\\\"managed\\\":{},\\\"extended\\\": {}}],\\\"nodes\\\": [{\\\"id\\\":1,\\\"type\\\":\\\"StreamExecTableSourceScan\\\",\\\"desc\\\":\\\"Source: datahub_table[22]\\\",\\\"profile\\\": {\\\"group\\\":\\\"default\\\",\\\"parallelism\\\":1,\\\"maxParallelism\\\":32768,\\\"minP allelism\\\":1}}, {\\\"id\\\":2,\\\"type\\\":\\\"StreamExecCalc\\\",\\\"desc\\\":\\\"Calc[23]\\\",\\\"profil \\": {\\\"group\\\":\\\"default\\\",\\\"parallelism\\\":1,\\\"maxParallelism\\\":32768,\\\"minP allelism\\\":1}}, {\\\"id\\\":3,\\\"type\\\":\\\"StreamExecSink\\\",\\\"desc\\\":\\\"Sink: kafka_table[24]\\\",\\\"profile\\\": {\\\"group\\\":\\\"default\\\",\\\"parallelism\\\":1,\\\"maxParallelism\\\":32768,\\\"minP allelism\\\":1}}],\\\"edges\\\": [{\\\"source\\\":1,\\\"target\\\":2,\\\"mode\\\":\\\"PIPELINED\\\",\\\"strategy\\\":\\\"FO ARD\\\"}, {\\\"source\\\":2,\\\"target\\\":3,\\\"mode\\\":\\\"PIPELINED\\\",\\\"strategy\\\":\\\"FOR RD\\\"}],\\\"vertices\\\":{\\\"717c7b8afebbfb7137f6f0f99beb2a94\\\": [1,2,3]}}\",\"success\":true,\"message\":\"\",\"execPlan\":\"{\ \\\"flinkVersion\\\" : \\\"1.17-vvr-8.0.7-10-SNAPSHOT\\\",\ \\\"nodes\\\" : [ {\ \\\"id\\\" : 25,\ \\\"t ype\\\" : \\\"stream-exec-table-source-scan_1\\\",\ \\\"scanTableSource\\\" : {\ \\\"table\\\" : {\ \\\"identifier\\\" : \\\"`vvp`.`default`.`datahub_table`\\\"\ },\ \\\"factoryIdentifier\\\" : \\\"datagen\\\"\ },\ \\\"outputType\\\" : \\\ "ROW<`strname` VARCHAR(2147483647)>\\\",\ \\\"description\\\" : \\\"TableSourceScan(table=[[vvp, default, datahub_table]], fields=[strname])\\\",\ \\ \"inputProperties\\\" : [ ],\ \\\"uid\\\" : \\\"1\\\"\ }, {\ \\\"id\\\" : 26,\ \\\"type\\\" : \\\"stream-exec-calc_1\\\",\ \\\"projection\\\" : [ {\ \\\"kind\\ \" : \\\"CALL\\\",\ \\\"internalName\\\" : \\\"$SUBSTRING$1\\\",\ \\\"operands \\\" : [ {\ \\\"kind\\\" : \\\"INPUT_REF\\\",\ \\\"inputIndex\\\" : 0,\ \\\"type\\\" : \\\"VARCHAR(2147483647)\\\"\ }, {\ \\\"kind\\\" : \\\"LITERAL\\\",\ \\\"value\\\" : 0,\ \\\"type\\\" : \\\"INT NOT NULL\\\"\ }, {\ \\\"kind\\\" : \\\"LITERAL\\\",\ \\\"value\\\" : 10,\
```

实时计算（流计算） 参考

```json
\\\"type\\\" : \\\"INT NOT NULL\\\"\ } ],\ \\\"type\\\" : \\\"VARCHAR(2147483647)\\\"\ }, {\ \\\"kind\\\" : \\\"CALL\\\",\ \\\"syntax\\\" : \\\"SPECIAL\\\",\ \\\"internalName\\\" : \\\"$CAST$1\\\",\ \\ \"operands\\\" : [ {\ \\\"kind\\\" : \\\"CALL\\\",\ \\\"internalName\\\" : \\\"$CHAR_LENGTH$1\\\",\ \\\"operands\\\" : [ {\ \\\"kind\\\" : \\\"INPUT_REF\\\",\ \\\"inputIndex\\\" : 0,\ \\\"type\\\" : \\\"VARCHAR(2147483647)\\\"\ } ],\ \\\"type\\\" : \\\"INT\\\"\ } ],\ \\\"type\\\" : \\\"BIGINT\\\"\ } ],\ \\\"condition\\\" : null,\ \\\"inputProper ties\\\" : [ {\ \\\"requiredDistributions\\\" : [ {\ \\\"type\\\" : \\\"UNKN OWN\\\"\ } ],\ \\\"damBehavior\\\" : \\\"PIPELINED\\\",\ \\\"priority\\\" : 0\ } ],\ \\\"outputType\\\" : \\\"ROW<`strname` VARCHAR(2147483647), `lens` BIGI NT>\\\",\ \\\"description\\\" : \\\"Calc(select=[SUBSTRING(strname, 0, 10) AS strname, CAST(CHAR_LENGTH(strname) AS BIGINT) AS lens])\\\",\ \\\"uid\\\" : \\\"2\\\" \ }, {\ \\\"id\\\" : 27,\ \\\"type\\\" : \\\"stream-exec-sink_1\\\",\ \\\"conf iguration\\\" : {\ \\\"table.exec.sink.keyed-shuffle\\\" : \\\"AUTO\\\",\ \\\" table.exec.sink.not-null-enforcer\\\" : \\\"ERROR\\\",\ \\\"table.exec.sink.type-le ngth-enforcer\\\" : \\\"IGNORE\\\",\ \\\"table.exec.sink.upsert-materialize\\\" : \\\"AUTO\\\"\ },\ \\\"dynamicTableSink\\\" : {\ \\\"table\\\" : {\ \\\ "identifier\\\" : \\\"`vvp`.`default`.`kafka_table`\\\"\ },\ \\\"factoryIdentifier\\\" : \\\"print\\\"\ },\ \\\"inputChangelogMode\\\" : [ \\\"INSERT\\\" ],\ \\\"inputProperties\\\" : [ {\ \\\"requiredDistributions\\\" : [ {\ \\\"type\\\" : \\\"UNKNOWN\\\"\ } ],\ \\\"damBehavior\\\" : \\\" PIPELINED\\\",\ \\\"priority\\\" : 0\ } ],\ \\\"outputType\\\" : \\\"ROW<`str name` VARCHAR(2147483647), `lens` BIGINT>\\\",\ \\\"description\\\" : \\\"Sink(table= [vvp.default.kafka_table], fields=[strname, lens])\\\",\ \\\"uid\\\" : \\\"3\\\"\ } ],\ \\\"edges\\\" : [ {\ \\\"source\\\" : 25,\ \\\"target\\\" : 26,\ \\\"shuff le\\\" : {\ \\\"type\\\" : \\\"FORWARD\\\"\ },\ \\\"shuffleMode\\\" : \\\"PIP ELINED\\\"\ }, {\ \\\"source\\\" : 26,\ \\\"target\\\" : 27,\ \\\"shuffle\\\" : {\ \\\"type\\\" : \\\"FORWARD\\\"\ },\ \\\"shuffleMode\\\" : \\\"PIPELINED\\\"\ } ]\}\"}},\"success\":true}",
 "success":true,
 "requestId":"CBC799F0-AS7S-1D30-8A4F-882ED4DD****"
}
```

`XML` 格式

```xml
<data>{&quot;commitResult&quot;:{&quot;success&quot;:true,&quot;deployment&quot;: {&quot;metadata&quot;:{&quot;createdAt&quot;:&quot;2026-04- 28T01:59:31Z&quot;,&quot;workspace&quot;:&quot;9cuwr9g7y1hl19&quot;,&quot;modifiedAt&quot; quot;2026-04- 28T02:07:17.205814Z&quot;,&quot;resourceVersion&quot;:4,&quot;name&quot;:&quot;sqlJob&quot &quot;namespace&quot;:&quot;flinkteam&quot;,&quot;annotations&quot;: {&quot;creator&quot;:&quot;235406976657057054&quot;,&quot;resourceplan.has.migrated&quot;:&quot;true&quot;,&quot;storage.disaster.rpo&quot;:&quot;1800&quot; quot;deployment.has.deployed&quot;:&quot;false&quot;,&quot;deployment.sourcetype&quot;:&quot;EDITOR&quot;,&quot;modifier&quot;:&quot;235406976657057054&quot;,&quot;cr torName&quot;:&quot;flinkadmin&quot;,&quot;plan.uri&quot;:&quot;deployment/7325ac07e466-4c1b-b598- 311c6f2c103b/resourcePlan.json&quot;,&quot;priority&quot;:&quot;5&quot;,&quot;priority.cla .name&quot;:&quot;flinkp5&quot;,&quot;migration.display.enabled&quot;:&quot;false&quot;,&quot;com.dataartisans.ap anager.controller.deployment.spec.version&quot;:&quot;4&quot;,&quot;default.resourcesetting.has.migrated&quot;:&quot;true&quot;,&quot;deployment.referenced.deployment.draft.h tory.version&quot;:&quot;3&quot;,&quot;deployment.referenced.deployment.draft.id&quot;:&qu
```

实时计算（流计算） 参考

```
;cee26b6e-d03b-4a03-a628a6fe665c525e&quot;,&quot;modifierName&quot;:&quot;flinkadmin&quot;,&quot;taker&quot;:&quot
| vvp-
0&quot;,&quot;deployment.referenced.deployment.draft.history.id&quot;:&quot;5bfca9e9a50d-483b-bad5-1e1d5315acaf&quot;},&quot;id&quot;:&quot;7325ac07-e466-4c1b-b598- 311c6f2c103b&quot;,&quot;labels&quot;: {}},&quot;apiVersion&quot;:&quot;v1&quot;,&quot;kind&quot;:&quot;Deployment&quot;,&quot;sp &quot;:{&quot;template&quot;:{&quot;metadata&quot;:{&quot;annotations&quot;: {&quot;flink.resource.type&quot;:&quot;finegrained&quot;,&quot;native.kubernetes.mode&quot;:&quot;true&quot;,&quot;flink.queryablestate.enabled&quot;:&quot;false&quot;,&quot;flink.security.ssl.enabled&quot;:&quot;false&q t;}},&quot;spec&quot;:{&quot;artifact&quot;:{&quot;flinkImageTag&quot;:&quot;1.17.0-vvr -8.0.7-manifest- 251107&quot;,&quot;kind&quot;:&quot;SQLSCRIPT&quot;,&quot;sqlScript&quot;:&quot;CREATE TEMPORARY TABLE `datahub_table` (strname VARCHAR)with ( &#x27;connector&#x27; = &#x27;datagen&#x27;);CREATE TEMPORARY TABLE `kafka_table` (strname VARCHAR, lens BIGINT)with ( &#x27;connector&#x27; = &#x27;print&#x27;);INSERT INTO kafka_tableSELECT SUBSTRING (strname, 0, 10) AS strname, CAST (CHAR_LENGTH (strname) AS BIGINT) AS lensFROM datahub_table;&quot;,&quot;imageUserDefined&quot;:false,&quot;flinkImageRegistry&quot;:&qu ;cn-wulan-env35-d01-reg.docker.intra.env35.shuguang.com:80/ververicapaas&quot;,&quot;versionName&quot;:&quot;vvr-8.0.7-flink- 1.17&quot;,&quot;flinkImageRepository&quot;:&quot;vvr&quot;,&quot;flinkVersion&quot;:&quot .17&quot;},&quot;parallelism&quot;:1,&quot;batchMode&quot;:false,&quot;resources&quot;: {&quot;jobmanager&quot;: {&quot;memory&quot;:&quot;2Gi&quot;,&quot;cpu&quot;:0.5},&quot;taskmanager&quot;: {&quot;memory&quot;:&quot;3Gi&quot;,&quot;cpu&quot;:1.0}},&quot;logging&quot;: {&quot;log4jLoggers&quot;:{&quot;&quot;:&quot;INFO&quot;},&quot;logReservePolicy&quot;: {&quot;expirationDays&quot;:7,&quot;openHistory&quot;:true},&quot;loggingProfile&quot;:&qu ;default&quot;},&quot;flinkConfiguration&quot;:{}}},&quot;restoreStrategy&quot;: {&quot;kind&quot;:&quot;NONE&quot;},&quot;state&quot;:&quot;RUNNING&quot;,&quot;upgradeStr egy&quot;: {&quot;kind&quot;:&quot;NONE&quot;},&quot;maxSavepointCreationAttempts&quot;:4,&quot;maxJo reationAttempts&quot;:1,&quot;deploymentTargetId&quot;:&quot;a89ff052-38c6-4fd3-9b91e9c53f8ee019&quot;},&quot;status&quot;: {&quot;startTime&quot;:1777341571990,&quot;state&quot;:&quot;RUNNING&quot;,&quot;endTime&q t;:0}}},&quot;draftHistoryResult&quot;:{&quot;deploymentDraftHistory&quot;: {&quot;metadata&quot;:{&quot;draftId&quot;:&quot;cee26b6e-d03b-4a03-a628a6fe665c525e&quot;,&quot;workspace&quot;:&quot;9cuwr9g7y1hl19&quot;,&quot;modifiedAt&quot; quot;2026-04- 28T02:07:17.186925Z&quot;,&quot;resourceVersion&quot;:32,&quot;annotations&quot;: {&quot;migration.display.enabled&quot;:&quot;false&quot;,&quot;creator&quot;:&quot;2354069 657057054&quot;,&quot;modifier&quot;:&quot;235406976657057054&quot;,&quot;creatorName&quot &quot;flinkadmin&quot;,&quot;modifierName&quot;:&quot;flinkadmin&quot;,&quot;priority&quot &quot;5&quot;,&quot;deployment.draft.referenced.deployment.id&quot;:&quot;7325ac07e466-4c1b-b598-311c6f2c103b&quot;},&quot;description&quot;:&quot;cd1562be-02ed-32cf- 945b- 9769afe4c55e&quot;,&quot;version&quot;:&quot;3&quot;,&quot;parentId&quot;:&quot;cd1562be- 02ed-32cf-945b-9769afe4c55e&quot;,&quot;labels&quot;: {},&quot;createdAt&quot;:&quot;2026-04- 28T02:07:17.186925Z&quot;,&quot;name&quot;:&quot;sqlJob&quot;,&quot;namespace&quot;:&quot; inkteam&quot;,&quot;lock&quot;:{&quot;metadata&quot;:{&quot;createdAt&quot;:&quot;2026- 04-24T03:46:53Z&quot;,&quot;modifiedAt&quot;:&quot;2026-04- 24T03:46:53Z&quot;,&quot;namespace&quot;:&quot;flinkteam&quot;,&quot;annotations&quot;: {&
```

t t & t &

```
t235406976657057054&
```

t & t

```
difi
```

& t &

```
t23540697665
```

实时计算（流计算） 参考

```
{&quot;creator&quot;:&quot;235406976657057054&quot;,&quot;modifier&quot;:&quot;23540697665 57054&quot;},&quot;id&quot;:&quot;313fde08-4b44-38b5-99c4- 7f3038449796&quot;},&quot;apiVersion&quot;:&quot;v1&quot;,&quot;kind&quot;:&quot;Lock&quot &quot;spec&quot;: {&quot;holderName&quot;:&quot;flinkadmin&quot;,&quot;holderId&quot;:&quot;2354069766570570 &quot;}},&quot;id&quot;:&quot;5bfca9e9-a50d-483b-bad5- 1e1d5315acaf&quot;,&quot;deleteLock&quot;:0},&quot;apiVersion&quot;:&quot;v1&quot;,&quot;k d&quot;:&quot;DeploymentDraftHistory&quot;,&quot;spec&quot;:{&quot;template&quot;: {&quot;metadata&quot;:{&quot;annotations&quot;: {&quot;flink.resource.type&quot;:&quot;finegrained&quot;,&quot;native.kubernetes.mode&quot;:&quot;true&quot;,&quot;flink.queryablestate.enabled&quot;:&quot;false&quot;,&quot;flink.security.ssl.enabled&quot;:&quot;false&q t;}},&quot;spec&quot;:{&quot;artifact&quot;: {&quot;kind&quot;:&quot;SQLSCRIPT&quot;,&quot;sqlScript&quot;:&quot;CREATE TEMPORARY TABLE `datahub_table` (strname VARCHAR)with ( &#x27;connector&#x27; = &#x27;datagen&#x27;);CREATE TEMPORARY TABLE `kafka_table` (strname VARCHAR, lens BIGINT)with ( &#x27;connector&#x27; = &#x27;print&#x27;);INSERT INTO kafka_tableSELECT SUBSTRING (strname, 0, 10) AS strname, CAST (CHAR_LENGTH (strname) AS BIGINT) AS lensFROM datahub_table;&quot;,&quot;imageUserDefined&quot;:false,&quot;versionName&quot;:&quot;vvr- 8.0.7-flink- 1.17&quot;},&quot;parallelism&quot;:1,&quot;batchMode&quot;:false,&quot;resources&quot;: {&quot;jobmanager&quot;: {&quot;memory&quot;:&quot;2Gi&quot;,&quot;cpu&quot;:0.5},&quot;taskmanager&quot;: {&quot;memory&quot;:&quot;3Gi&quot;,&quot;cpu&quot;:1.0}},&quot;logging&quot;: {&quot;log4jLoggers&quot;: {&quot;&quot;:&quot;INFO&quot;},&quot;loggingProfile&quot;:&quot;default&quot;},&quot;flin onfiguration&quot;:{}}},&quot;restoreStrategy&quot;: {&quot;kind&quot;:&quot;LATEST_STATE&quot;,&quot;allowNonRestoredState&quot;:false},&quot; ate&quot;:&quot;CANCELLED&quot;,&quot;upgradeStrategy&quot;: {&quot;kind&quot;:&quot;STATELESS&quot;},&quot;maxSavepointCreationAttempts&quot;:4,&quot; xJobCreationAttempts&quot;:1,&quot;deploymentTargetId&quot;:&quot;a89ff052-38c6-4fd3- 9b91-e9c53f8ee019&quot;}},&quot;success&quot;:true},&quot;validationResult&quot;: {&quot;success&quot;:true,&quot;kind&quot;:&quot;SQLSCRIPT&quot;,&quot;artifactValidation& ot;: {&quot;validationResult&quot;:&quot;VALIDATION_RESULT_VALID_INSERT_QUERY&quot;,&quot;error tails&quot;: {&quot;columnNumber&quot;:0,&quot;endLineNumber&quot;:0,&quot;endColumnNumber&quot;:0,&quo lineNumber&quot;:0,&quot;message&quot;:&quot;&quot;}},&quot;planValidation&quot;: {&quot;resourcePlan&quot;:&quot;{\&quot;ssgProfiles\&quot;: [{\&quot;name\&quot;:\&quot;default\&quot;,\&quot;cpu\&quot;:0.2,\&quot;heap\&quot;:\&quot 68 mb\&quot;,\&quot;offHeap\&quot;:\&quot;32 mb\&quot;,\&quot;managed\&quot;: {},\&quot;extended\&quot;:{}}],\&quot;nodes\&quot;: [{\&quot;id\&quot;:1,\&quot;type\&quot;:\&quot;StreamExecTableSourceScan\&quot;,\&quot;des &quot;:\&quot;Source: datahub_table[22]\&quot;,\&quot;profile\&quot;: {\&quot;group\&quot;:\&quot;default\&quot;,\&quot;parallelism\&quot;:1,\&quot;maxParalleli \&quot;:32768,\&quot;minParallelism\&quot;:1}}, {\&quot;id\&quot;:2,\&quot;type\&quot;:\&quot;StreamExecCalc\&quot;,\&quot;desc\&quot;:\&q t;Calc[23]\&quot;,\&quot;profile\&quot;: {\&quot;group\&quot;:\&quot;default\&quot;,\&quot;parallelism\&quot;:1,\&quot;maxParalleli \&quot;:32768,\&quot;minParallelism\&quot;:1}}, {\&quot;id\&quot;:3,\&quot;type\&quot;:\&quot;StreamExecSink\&quot;,\&quot;desc\&quot;:\&q t;Sink: kafka_table[24]\&quot;,\&quot;profile\&quot;: {\&quot;group\&quot;:\&quot;default\&quot;,\&quot;parallelism\&quot;:1,\&quot;maxParalleli \&quot;:32768,\&quot;minParallelism\&quot;:1}}],\&quot;edges\&quot;:
```

实时计算（流计算） 参考 q , q q , q g q

```
[{\&quot;source\&quot;:1,\&quot;target\&quot;:2,\&quot;mode\&quot;:\&quot;PIPELINED\&quot; &quot;strategy\&quot;:\&quot;FORWARD\&quot;}, {\&quot;source\&quot;:2,\&quot;target\&quot;:3,\&quot;mode\&quot;:\&quot;PIPELINED\&quot;, quot;strategy\&quot;:\&quot;FORWARD\&quot;}],\&quot;vertices\&quot;: {\&quot;717c7b8afebbfb7137f6f0f99beb2a94\&quot;: [1,2,3]}}&quot;,&quot;success&quot;:true,&quot;message&quot;:&quot;&quot;,&quot;execPlan&q t;:&quot;{ \&quot;flinkVersion\&quot; : \&quot;1.17-vvr-8.0.7-10-SNAPSHOT\&quot;, \&quot;nodes\&quot; : [ { \&quot;id\&quot; : 25, \&quot;type\&quot; : \&quot;strea m-exec-table-source-scan_1\&quot;, \&quot;scanTableSource\&quot; : { \&quot;tabl e\&quot; : { \&quot;identifier\&quot; : \&quot;`vvp`.`default`.`datahub_table`\&quot; }, \&quot;factoryIdentifier\&quot; : \&quot;datagen\&quot; }, \&quot;outputType\&quot; : \&quot;ROW&lt;`strname` VARCHAR(2147483647)&gt;\&quot;, \& quot;description\&quot; : \&quot;TableSourceScan(table=[[vvp, default, datahub_table]], fields=[strname])\&quot;, \&quot;inputProperties\&quot; : [ ], \&quot;uid\&quot; : \&quot;1\&quot; }, { \&quot;id\&quot; : 26, \&quot;type\&quot; : \&quot;stream-ex ec-calc_1\&quot;, \&quot;projection\&quot; : [ { \&quot;kind\&quot; : \&quot;CAL L\&quot;, \&quot;internalName\&quot; : \&quot;$SUBSTRING$1\&quot;, \&quot;oper ands\&quot; : [ { \&quot;kind\&quot; : \&quot;INPUT_REF\&quot;, \&quot;inputIndex\&quot; : 0, \&quot;type\&quot; : \&quot;VARCHAR(2147483647)\&quot; }, { \&quot;kind\&quot; : \&quot;LITERAL\&quot;, \&quot;value\&quot; : 0, \&quot;type\&quot; : \&quo t;INT NOT NULL\&quot; }, { \&quot;kind\&quot; : \&quot;LITERAL\&quot;, \&quot;value\&quot; : 10, \&quot;type\&quot; : \&quot;INT NOT NULL\&quot; } ], \&quot;type\&quot; : \&quot;VARCHAR(2147483647)\&quot; }, { \&quot;kind\&quot; : \&quot;CALL\&quot;, \&quot;syntax\&quot; : \&quot;SPECIAL\&quot;, \&quot;internalName\&quot; : \&quot;$CAST$1\&quot;, \&q uot;operands\&quot; : [ { \&quot;kind\&quot; : \&quot;CALL\&quot;, \&quot; internalName\&quot; : \&quot;$CHAR_LENGTH$1\&quot;, \&quot;operands\&quot; : [ { \&quot;kind\&quot; : \&quot;INPUT_REF\&quot;, \&quot;inputIndex\&quot; : 0, \&quot;type\&quot; : \&quot;VARCHAR(2147483647)\&quot; } ], \&quot;type\&quot; : \&quot;INT\&quot; } ], \&quot;type\&quot; : \&quot;BIGINT\&quot; } ], \&quot;condition\&quot; : null, \&quot;inputProperties\&quot; : [ { \&quot;requiredDistributions\&quot; : [ { \&quot;type\&quot; : \&quot;UNKNOWN\&quot; } ], \&quot;damBehavior\&quot; : \& quot;PIPELINED\&quot;, \&quot;priority\&quot; : 0 } ], \&quot;outputType\&quot; : \&quot;ROW&lt;`strname` VARCHAR(2147483647), `lens` BIGINT&gt;\&quot;, \&quot;description\&quot; : \&quot;Calc(select=[SUBSTRING(strname, 0, 10) AS strname, CAST(CHAR_LENGTH(strname) AS BIGINT) AS lens])\&quot;, \&quot;uid\&quot; : \&quot;2\&quot; }, { \&quot;id\&quot; : 27, \&quot;type\&quot ; : \&quot;stream-exec-sink_1\&quot;, \&quot;configuration\&quot; : { \&quot;tab le.exec.sink.keyed-shuffle\&quot; : \&quot;AUTO\&quot;, \&quot;table.exec.sink.notnull-enforcer\&quot; : \&quot;ERROR\&quot;, \&quot;table.exec.sink.type-length-enfo rcer\&quot; : \&quot;IGNORE\&quot;, \&quot;table.exec.sink.upsert-materialize\&quot ; : \&quot;AUTO\&quot; }, \&quot;dynamicTableSink\&quot; : { \&quot;table\&quot; : { \&quot;identifier\&quot; : \&quot;`vvp`.`default`.`kafka_table`\&quot; }, \&quot;factoryIdentifier\&quot; : \&quot;print\&quot; }, \&quot;inputChangelogMode\&quot; : [ \&quot;INSERT\&quot; ], \&quot;inputProperties\&quot; : [ { \&quot;requiredDistributions\&quot; : [ { \&quot;type\&quot; : \&quot;UNKNOWN\&quot; } ], \&quot;damBehavior\&quot; : \& quot;PIPELINED\&quot;, \&quot;priority\&quot; : 0 } ], \&quot;outputType\&quot; : \&quot;ROW&lt;`strname` VARCHAR(2147483647), `lens` BIGINT&gt;\&quot;, \&quot;description\&quot; : \&quot;Sink(table= [vvp.default.kafka_table], fields=[strname, lens])\&quot;, \&quot;uid\&quot; :
```

实时计算（流计算） 参考

```xml
\&quot;3\&quot; } ], \&quot;edges\&quot; : [ { \&quot;source\&quot; : 25, \&quot ;target\&quot; : 26, \&quot;shuffle\&quot; : { \&quot;type\&quot; : \&quot;FORWA RD\&quot; }, \&quot;shuffleMode\&quot; : \&quot;PIPELINED\&quot; }, { \&quot;s ource\&quot; : 26, \&quot;target\&quot; : 27, \&quot;shuffle\&quot; : { \&quo t;type\&quot; : \&quot;FORWARD\&quot; }, \&quot;shuffleMode\&quot; : \&quot;PIPELI NED\&quot; } ]}&quot;}},&quot;success&quot;:true}</data> <success>true</success> <requestId>CBC799F0-AS7S-1D30-8A4F-882ED4DD****</requestId>
```

###### DeleteUdfArtifact

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
/pop/workspaces/[workspace]/sql/v1beta1/namespaces/[namespace]/udfartifacts/[udfArtifactNa ] HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | String | Host | 是 | cn-wulan-env***-d01 | Region ID。 |
| workspace | String | Path | 是 | default | 作业所在的工作空间ID。您可以通过以下任意一种方式获取： 通过ListNamespaces获取。 在Flink全托管开发控制台工作空间详情中获取。 |
| namespac e | String | Path | 是 | ververica | 作业所在的项目空间名称。 |
| udfArtifact Name | String | Path | 是 | metric-transform-227- shaded | udf名称。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|

实时计算（流计算） 参考

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| data | String | { "referencedClasses ": [], "@type": "type.googleapis.c om/vvp.sql.v1beta 1.DeleteUdfArtifact Response" } | 详细信息。 |
| requestId | String | 07E49735-A389- 4853-AFBA- 28F9EB0EFDC4 | 请求ID。 |
| success | Boolean | true | 请求是否成功。 |

**示例**

请求示例

```
/pop/workspaces/[workspace]/sql/v1beta1/namespaces/[namespace]/udfartifacts/[udfArtifactNa ] HTTP/1.1 &RegionId=cn-wulan-env***-d01 &workspace=default &namespace=ververica &udfArtifactName=metric-transform-227-shaded
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "data":"{\"referencedClasses\":
[],\"@type\":\"type.googleapis.com/vvp.sql.v1beta1.DeleteUdfArtifactResponse\"}",
 "requestId": "07E49735-A389-4853-AFBA-28F9EB0EFDC4",
 "success":true
}
```

`XML` 格式

```xml
<data>{&quot;referencedClasses&quot;: [],&quot;@type&quot;:&quot;type.googleapis.com/vvp.sql.v1beta1.DeleteUdfArtifactResponse&q t;}</data> <requestId>07E49735-A389-4853-AFBA-28F9EB0EFDC4</requestId> <success>true</success>
```

###### DeleteSecretValue

**请求头**

实时计算（流计算） 参考该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
DELETE /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/secret-values/[name] HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | String | Host | 是 | cn-qingdao-env***-d01 | Region ID。 |
| namespac e | String | Path | 是 | flinkteam | 作业所在的项目空间名称。 |
| workspace | String | Path | 是 | default | 作业所在的工作空间ID。您可以通过以下任意一种方式获取： 通过ListNamespaces获取。 在Flink全托管开发控制台工作空间详情中获取。 |
| name | String | Path | 否 | secretKey | 变量名称。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| success | Boolean | true | 请求是否成功。 |
| requestId | String | 1CCA8A71-98C6- 491B-9A2D- ADDFC0939294 | 请求ID。 |

**示例**

请求示例

```
DELETE /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/secret-values/[name] HTTP/1.1 &RegionId=cn-qingdao-env***-d01 &namespace=flinkteam &workspace=default
```

&公共请求参数正常返回示例 `JSON` 格式实时计算（流计算） 参考

```json
{
 "success":true,
 "requestId":"1CCA8A71-98C6-491B-9A2D-ADDFC0939294"
}
```

`XML` 格式

```xml
<success>true</success> <requestId>1CCA8A71-98C6-491B-9A2D-ADDFC0939294</requestId>
```

###### DeleteMember

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
DELETE /pop/workspaces/[workspace]/members/v1/namespaces/[namespace]/members/[member] HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| workspace | String | Path | 是 | default | 作业所在的工作空间ID。您可以通过以下任意一种方式获取： 通过ListNamespaces获取。 在Flink全托管开发控制台工作空间详情中获取。 |
| namespac e | String | Path | 是 | flinkteam | 作业所在的项目空间名称。 |
| member | String | Path | 是 | user:242425410145292 209 | 待解除授权的用户信息，格式：user:${uid}。 |
| RegionId | String | Host | 是 | cn-wulan-env***-d01 | Region名称。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| success | Boolean | true | 请求是否成功。 |

| link存算分离版开发 | 指南·OpenAPI |  | 实时计算（流计算） |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | String | 8AA170D4-F4D1- 4E90-A02D- 0CC211BE8171 | 请求ID。 |

**示例**

请求示例

```
DELETE /pop/workspaces/[workspace]/members/v1/namespaces/[namespace]/members/[member] HTTP/1.1 &workspace=default &namespace=flinkteam &member=user:242425410145292209 &RegionId=cn-wulan-env***-d01
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "success":true,
 "requestId":"8AA170D4-F4D1-4E90-A02D-0CC211BE8171"
}
```

`XML` 格式

```xml
<success>true</success> <requestId>8AA170D4-F4D1-4E90-A02D-0CC211BE8171</requestId>
```

###### DeleteFormat

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
DELETE /pop/workspaces/[workspace]/sql/v1beta1/namespaces/[namespace]/formats/[name] HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | String | Host | 是 | cn-wulan-env***-d01 | Region ID。 |

实时计算（流计算） 参考

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| workspace | String | Path | 是 | default | 作业所在的工作空间ID。您可以通过以下任意一种方式获取： 通过ListNamespaces获取。 在Flink全托管开发控制台工作空间详情中获取。 |
| name | String | Path | 是 | customized-csv | 待删除的format名称。 |
| namespac e | String | Path | 是 | flinkteam | 作业所在的项目空间名称。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | String | EC30D915-1E89- 4B66-B1AA- C5D161DAB50D | 请求ID。 |

**示例**

请求示例

```
DELETE /pop/workspaces/[workspace]/sql/v1beta1/namespaces/[namespace]/formats/[name] HTTP/1.1 &RegionId=cn-wulan-env***-d01 &workspace=default &name=customized-csv &namespace=flinkteam
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "requestId":"EC30D915-1E89-4B66-B1AA-C5D161DAB50D"
}
```

`XML` 格式

```xml
<requestId>EC30D915-1E89-4B66-B1AA-C5D161DAB50D</requestId>
```

###### DeleteFolder

实时计算（流计算） 参考

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
DELETE /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/folders/[folderId] HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | String | Host | 是 | cn-wulan-env***-d01 | Region名称。 |
| workspace | String | Path | 是 | default | 作业所在的工作空间ID。您可以通过以下任意一种方式获取： 通过ListNamespaces获取。 在Flink全托管开发控制台工作空间详情中获取。 |
| namespac e | String | Path | 是 | flinkteam | 作业所在的项目空间名称。 |
| folderId | String | Path | 是 | 123 | 文件夹ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | String | CBC799F0-AS7S- 1D30-8A4F- 882ED4DD**** | 请求ID。 |
| success | Boolean | true | 表示请求是否成功。 |

**示例**

请求示例

```
DELETE /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/folders/[folderId] HTTP/1.1 &RegionId=cn-wulan-env***-d01 &workspace=default &namespace=flinkteam &folderId=123
```

&公共请求参数正常返回示例实时计算（流计算） 参考 `JSON` 格式

```json
{
 "requestId":"CBC799F0-AS7S-1D30-8A4F-882ED4DD****",
 "success":true
}
```

`XML` 格式

```xml
<requestId>CBC799F0-AS7S-1D30-8A4F-882ED4DD****</requestId> <success>true</success>
```

###### DeleteDeployment

调用DeleteDeployment，删除指定的部署资源，释放相关工作负载及关联组件。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
/pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/deployments/[deploymentId] HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | String | Host | 是 | cn-wulan-env***-d01 | Region ID。 |
| namespac e | String | Path | 是 | flinkteam | 作业所在的项目空间名称。 |
| deployme ntId | String | Path | 是 | d0b3abf0-4bfe-46b1- a324-5b7def580c00 | 作业ID。 |
| workspace | String | Path | 是 | default | 作业所在的工作空间ID。您可以通过以下任意一种方式获取： 通过ListNamespaces获取。 在Flink全托管开发控制台工作空间详情中获取。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|

实时计算（流计算） 参考

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | String | CBC799F0-AS7S- 1D30-8A4F- 882ED4DD**** | 请求ID。 |
| success | Boolean | true | 请求是否成功。 |

**示例**

请求示例

```
/pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/deployments/[deploymentId] HTTP/1.1 &RegionId=cn-wulan-env***-d01 &namespace=flinkteam &deploymentId=d0b3abf0-4bfe-46b1-a324-5b7def580c00 &workspace=default
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "requestId":"CBC799F0-AS7S-1D30-8A4F-882ED4DD****",
 "success":true
}
```

`XML` 格式

```xml
<requestId>CBC799F0-AS7S-1D30-8A4F-882ED4DD****</requestId> <success>true</success>
```

###### DeleteConnector

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
DELETE /pop/workspaces/[workspace]/sql/v1beta1/namespaces/[namespace]/connectors/[name] HTTP/1.1
```

**请求参数**

实时计算（流计算） 参考

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | String | Host | 是 | cn-wulan-env***-d01 | Region ID。 |
| workspace | String | Path | 是 | default | 作业所在的工作空间ID。您可以通过以下任意一种方式获取： 通过ListNamespaces获取。 在Flink全托管开发控制台工作空间详情中获取。 |
| name | String | Path | 是 | hologres-fix | 要删除的connector名称。 |
| namespac e | String | Path | 是 | flinkteam | 作业所在的项目空间名称。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| success | Boolean | true | 请求是否成功。 |
| requestId | String | 7113AD53-5192- 46E5-B592- 81175BAF7F54 | 请求ID。 |

**示例**

请求示例

```
DELETE /pop/workspaces/[workspace]/sql/v1beta1/namespaces/[namespace]/connectors/[name] HTTP/1.1 &RegionId=cn-wulan-env***-d01 &workspace=default &name=hologres-fix &namespace=flinkteam
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "success":true,
 "requestId":"7113AD53-5192-46E5-B592-81175BAF7F54"
}
```

`XML` 格式实时计算（流计算） 参考

```xml
<success>true</success> <requestId>7113AD53-5192-46E5-B592-81175BAF7F54</requestId>
```

###### DeleteArtifact

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
DELETE /pop/workspaces/[workspace]/artifacts/v1/namespaces/[namespace]/artifacts:delete HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | String | Host | 是 | cn-wulan-env***-d01 | Region ID。 |
| namespac e | String | Path | 是 | flinkteam | 作业所在的项目空间名称。 |
| filename | String | Query | 是 | test.csv | 文件名称。 |
| workspace | String | Path | 是 | default | 作业所在的工作空间ID。您可以通过以下任意一种方式获取： 通过ListNamespaces获取。 在Flink全托管开发控制台工作空间详情中获取。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | String | CBC799F0-AS7S- 1D30-8A4F- 882ED4DD**** | 请求ID。 |
| success | Boolean | true | 请求是否成功。 |

**示例**

请求示例实时计算（流计算） 参考

```
DELETE /pop/workspaces/[workspace]/artifacts/v1/namespaces/[namespace]/artifacts:delete HTTP/1.1 &RegionId=cn-wulan-env***-d01 &namespace=flinkteam &filename=test.csv &workspace=default
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "requestId":"CBC799F0-AS7S-1D30-8A4F-882ED4DD****",
 "success":true
}
```

`XML` 格式

```xml
<requestId>CBC799F0-AS7S-1D30-8A4F-882ED4DD****</requestId> <success>true</success>
```

###### DatabaseExists

调用DatabaseExists，确认catalog下的指定database是否存在。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
GET /pop/workspaces/[workspace]/catalog/v1beta2/namespaces/[namespace]/catalogs/[cat]:database ists HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | String | Host | 是 | cn-wulan-env***-d01 | Region ID。 |
| namespac e | String | Path | 是 | ververica | 作业所在的项目空间名称。 |

实时计算（流计算） 参考

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| workspace | String | Path | 是 | default | 作业所在的工作空间ID。您可以通过以下任意一种方式获取： 通过ListNamespaces获取。 在Flink全托管开发控制台工作空间详情中获取。 |
| cat | String | Path | 是 | vvp | catalog名称。 |
| database | String | Query | 是 | default | catalog下数据库名称。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| data | String | { "@type": "type.googleapis.c om/vvp.sql.catalog. v1beta2.DatabaseE xistsResponse", "exists": true } | 详细信息。 |
| requestId | String | 41CAB2BF-B428- 4240-A746- 1F6CE6DE**** | 请求ID。 |
| success | Boolean | true | 请求是否成功。 |

**示例**

请求示例

```
GET /pop/workspaces/[workspace]/catalog/v1beta2/namespaces/[namespace]/catalogs/[cat]:database ists HTTP/1.1 &RegionId=cn-wulan-env***-d01 &namespace=ververica &workspace=default &cat=vvp &database=default
```

&公共请求参数正常返回示例 `JSON` 格式实时计算（流计算） 参考

```json
{
 "data":"
{\"@type\":\"type.googleapis.com/vvp.sql.catalog.v1beta2.DatabaseExistsResponse\",\"exists :true}",
 "requestId":"41CAB2BF-B428-4240-A746-1F6CE6DE****",
 "success":true
}
```

`XML` 格式

```xml
<data> {&quot;@type&quot;:&quot;type.googleapis.com/vvp.sql.catalog.v1beta2.DatabaseExistsRespons quot;,&quot;exists&quot;:true}</data> <requestId>41CAB2BF-B428-4240-A746-1F6CE6DE****</requestId> <success>true</success>
```

###### CreateUdfArtifact

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /pop/workspaces/[workspace]/sql/v1beta1/namespaces/[namespace]/udfartifacts HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | String | Host | 是 | cn-qingdao-env***-d01 | Region ID。 |
| paramsJso n | String | Body | 否 | {"name": "metric- transform-2.2.7- shaded", "jarUrl": "http://flink- resource.oss-cn-wulan- env**-d01- a.intra.env**.shuguang.c om/udx/metric- transform-2.2.7- shaded.jar"} | udf参数，指定待创建的udf 使用的jar包所在的存储路径及udf名称（注意：指定路径的udf jar必须真实存在）。 |

实时计算（流计算） 参考

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| workspace | String | Path | 是 | default | 作业所在的工作空间ID。您可以通过以下任意一种方式获取： 通过ListNamespaces获取。 在Flink全托管开发控制台工作空间详情中获取。 |
| namespac e | String | Path | 是 | flinkteam | 作业所在的项目空间名称。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|

实时计算（流计算） 参考

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| data | String | { "@type": "type.googleapis.c om/vvp.sql.v1beta 1.CreateUdfArtifact Response", "collidingClasses": [], "udfArtifact": { "dependencyJarUris ": [], "udfClasses": [ { "functionNames": [], "udfArtifactName": "namespaces/flinkt eam/udfartifacts/m etric-transform- 227", "className": "com.alibaba.blink. udtf.TimestampPro be", "classType": "UDF TYPE SCALA _ _ R" }, { "functionNames": [], "udfArtifactName": "namespaces/flinkt eam/udfartifacts/m etric-transform- 227", "className": "com.alibaba.blink. udtf.TransformUdtf ", "classType": "UDF TYPE TABLE" _ _ } ], "artifactType": "ARTIFACT TYPE JA _ _ VA", "createTime": "2024-03- 11T02:54:24.82276 6Z", "uploader": "22985261012276 3813", "jarUpdateTime": "2024-03- 11T02:54:24.82276 6Z", "name": "namespaces/flinkt eam/udfartifacts/m etric-transform- 227", "namespace": "flinkteam", "jarUrl": "hdfs:///tmp/udf/me tric-transform- 2.2.7-shaded.jar", "updateTime": "2024-03- 11T02:54:24.82276 6Z" } } | 详细信息。 |
| requestId | String | 8F0CFB56-7CE8- 45AA-A788- 41B7D2504E5F | 请求ID。 |

| F | link存算分离版开发参考 | 指南·OpenAPI |  | 实时计算（流计算） |  |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| success | Boolean | true | 请求是否成功。 |

**示例**

请求示例

```json
POST /pop/workspaces/[workspace]/sql/v1beta1/namespaces/[namespace]/udfartifacts HTTP/1.1 { "RegionId":"cn-qingdao-env***-d01", "workspace":"default", "namespace":"flinkteam" }
```

正常返回示例 `JSON` 格式

```json
{
 "data":"
{\"@type\":\"type.googleapis.com/vvp.sql.v1beta1.CreateUdfArtifactResponse\",\"collidingCl ses\":[],\"udfArtifact\":{\"dependencyJarUris\":[],\"udfClasses\":[{\"functionNames\": [],\"udfArtifactName\":\"namespaces/flinkteam/udfartifacts/metric-transform- 227\",\"className\":\"com.alibaba.blink.udtf.TimestampProbe\",\"classType\":\"UDF_TYPE_SCA R\"},{\"functionNames\": [],\"udfArtifactName\":\"namespaces/flinkteam/udfartifacts/metric-transform- 227\",\"className\":\"com.alibaba.blink.udtf.TransformUdtf\",\"classType\":\"UDF_TYPE_TABL "}],\"artifactType\":\"ARTIFACT_TYPE_JAVA\",\"createTime\":\"2024-03- 11T02:54:24.822766Z\",\"uploader\":\"229852610122763813\",\"jarUpdateTime\":\"2024-03- 11T02:54:24.822766Z\",\"name\":\"namespaces/flinkteam/udfartifacts/metric-transform- 227\",\"namespace\":\"flinkteam\",\"jarUrl\":\"hdfs:///tmp/udf/metric-transform-2.2.7shaded.jar\",\"updateTime\":\"2024-03-11T02:54:24.822766Z\"}}",
 "requestId":"8F0CFB56-7CE8-45AA-A788-41B7D2504E5F",
 "success":true
}
```

`XML` 格式实时计算（流计算） 参考

```xml
<data> {&quot;@type&quot;:&quot;type.googleapis.com/vvp.sql.v1beta1.CreateUdfArtifactResponse&quo ,&quot;collidingClasses&quot;:[],&quot;udfArtifact&quot;: {&quot;dependencyJarUris&quot;:[],&quot;udfClasses&quot;:[{&quot;functionNames&quot;: [],&quot;udfArtifactName&quot;:&quot;namespaces/flinkteam/udfartifacts/metrictransform- 227&quot;,&quot;className&quot;:&quot;com.alibaba.blink.udtf.TimestampProbe&quot;,&quot;cl sType&quot;:&quot;UDF_TYPE_SCALAR&quot;},{&quot;functionNames&quot;: [],&quot;udfArtifactName&quot;:&quot;namespaces/flinkteam/udfartifacts/metrictransform- 227&quot;,&quot;className&quot;:&quot;com.alibaba.blink.udtf.TransformUdtf&quot;,&quot;cla Type&quot;:&quot;UDF_TYPE_TABLE&quot;}],&quot;artifactType&quot;:&quot;ARTIFACT_TYPE_JAVA& ot;,&quot;createTime&quot;:&quot;2024-03- 11T02:54:24.822766Z&quot;,&quot;uploader&quot;:&quot;229852610122763813&quot;,&quot;jarUpd eTime&quot;:&quot;2024-03- 11T02:54:24.822766Z&quot;,&quot;name&quot;:&quot;namespaces/flinkteam/udfartifacts/metrictransform- 227&quot;,&quot;namespace&quot;:&quot;flinkteam&quot;,&quot;jarUrl&quot;:&quot;hdfs:///tmp df/metric-transform-2.2.7-shaded.jar&quot;,&quot;updateTime&quot;:&quot;2024-03- 11T02:54:24.822766Z&quot;}}</data> <requestId>8F0CFB56-7CE8-45AA-A788-41B7D2504E5F</requestId> <success>true</success>
```

###### CreateSecretValue

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/secret-values HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | String | Host | 是 | cn-wulan-env***-d01 | Region名称。 |
| workspace | String | Path | 是 | default | 作业所在的工作空间ID。您可以通过以下任意一种方式获取： 通过ListNamespaces获取。 在Flink全托管开发控制台工作空间详情中获取。 |
| namespac e | String | Path | 是 | flinkteam | 作业所在的项目空间名称。 |

| F | link存算分离版参考 | 开发指南 | ·OpenAPI |  |  | 实时计算（流计算） |  |
|---|---|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| paramsJso n | String | Body | 否 | { "metadata": { "name": "flink access id", _ _ "workspace": "9cuwr9g7y1hl19", "namespace": "flinkteam" }, "spec": { "kind": "Plain", "value": "flink access key" } } _ _ | 请求参数，指定变量名称和变量值。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| success | Boolean | true | 请求是否成功。 |

实时计算（流计算） 参考

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| data | String | { "eagleEyeTraceId": "0a2318ab177734 16617444310d**** ", "asapiSuccess": true, "asapiRequestId": "5EBEB7CA-1133- 4746-8132- A35DC078****", "data": { "metadata": { "createdAt": "2026- 04- 28T02:01:01.79117 2Z", "workspace": "9cuwr9g7y1hl19", "modifiedAt": "2026-04- 28T02:01:01.79117 2Z", "resourceVersion": 1, "name": "flink access id", _ _ "namespace": "flinkteam", "annotations": { "creator": "23540697665705* ***", "modifier": "23540697665705* ***", "creatorName": "flinkadmin", "modifierName": "flinkadmin" }, "id": "c73a06e7- c2d2-4d78-9dbe- 87413280****", "labels": {} }, "apiVersion": "v1", "kind": "SecretValue", "spec": { "kind": "Plain", "value": "flink access key" _ _ } } | 详细数据。 |
| requestId | String | 19E71203-97A1- 4355-8C25- D566CA82**** | 请求ID。 |

**示例**

请求示例实时计算（流计算） 参考

```json
POST /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/secret-values HTTP/1.1 { "RegionId":"cn-wulan-env***-d01", "workspace":"default", "namespace":"flinkteam" }
```

正常返回示例 `JSON` 格式

```json
{
 "data":"
{\"eagleEyeTraceId\":\"0a2318ab17773416617444310d****\",\"asapiSuccess\":true,\"asapiReque Id\":\"5EBEB7CA-1133-4746-8132-A35DC078****\",\"data\":{\"metadata\":{\"createdAt\":\"20 26-04-28T02:01:01.791172Z\",\"workspace\":\"9cuwr9g7y1hl19\",\"modifiedAt\":\"2026-04- 28T02:01:01.791172Z\",\"resourceVersion\":1,\"name\":\"flink_access_id\",\"namespace\":\"f nkteam\",\"annotations\": {\"creator\":\"23540697665705****\",\"modifier\":\"23540697665705****\",\"creatorName\":\" inkadmin\",\"modifierName\":\"flinkadmin\"},\"id\":\"c73a06e7-c2d2-4d78-9dbe- 87413280****\",\"labels\":{}},\"apiVersion\":\"v1\",\"kind\":\"SecretValue\",\"spec\": {\"kind\":\"Plain\",\"value\":\"flink_access_key\"}}",
 "success":true,
 "requestId":"19E71203-97A1-4355-8C25-D566CA82****"
}
```

`XML` 格式

```xml
<data> {&quot;eagleEyeTraceId&quot;:&quot;0a2318ab17773416617444310d****&quot;,&quot;asapiSuccess uot;:true,&quot;asapiRequestId&quot;:&quot;5EBEB7CA-1133-4746-8132- A35DC078****&quot;,&quot;data&quot;:{&quot;metadata&quot;: {&quot;createdAt&quot;:&quot;2026-04- 28T02:01:01.791172Z&quot;,&quot;workspace&quot;:&quot;9cuwr9g7y1hl19&quot;,&quot;modifiedA quot;:&quot;2026-04- 28T02:01:01.791172Z&quot;,&quot;resourceVersion&quot;:1,&quot;name&quot;:&quot;flink_acces id&quot;,&quot;namespace&quot;:&quot;flinkteam&quot;,&quot;annotations&quot;: {&quot;creator&quot;:&quot;23540697665705****&quot;,&quot;modifier&quot;:&quot;23540697665 5****&quot;,&quot;creatorName&quot;:&quot;flinkadmin&quot;,&quot;modifierName&quot;:&quot; inkadmin&quot;},&quot;id&quot;:&quot;c73a06e7-c2d2-4d78-9dbe- 87413280****&quot;,&quot;labels&quot;: {}},&quot;apiVersion&quot;:&quot;v1&quot;,&quot;kind&quot;:&quot;SecretValue&quot;,&quot;s c&quot;: {&quot;kind&quot;:&quot;Plain&quot;,&quot;value&quot;:&quot;flink_access_key&quot;}} </data> <success>true</success> <requestId>19E71203-97A1-4355-8C25-D566CA82****</requestId>
```

###### CreateSavepoint

调用CreateSavepoint，创建保存点，用于事务处理中标记一个可回滚的状态位置。 实时计算（流计算） 参考

**请求头**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | String | Header | 是 | cn-wulan-env***-d01 | region名称。 |

**请求语法**

```
POST /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/savepoints HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| namespac e | String | Path | 是 | flinkteam | 作业所在的项目空间名称。 |
| paramsJso n | String | Body | 否 | { "deploymentId": "7325ac07-e466-4c1b- b598-311c6f2c103b" } | 执行参数，sql脚本。 |
| workspace | String | Path | 是 | default | 作业所在的工作空间ID。您可以通过以下任意一种方式获取： 通过ListNamespaces获取。 在Flink全托管开发控制台工作空间详情中获取。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|

实时计算（流计算） 参考

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| data | String | { "metadata": { "createdAt": "2026- 04- 28T02:13:28.27727 8Z", "jobId": "bf735437-b3ea- 4d1a-847e- bbacd144****", "workspace": "9cuwr9g7y1hl19", "nativeFormat": false, "modifiedAt": "2026-04- 28T02:13:28.27727 8Z", "deploymentId": "7325ac07-e466- 4c1b-b598- 311c6f2c103b", "origin": "USER REQUEST", _ "resourceVersion": 1, "namespace": "flinkteam", "annotations": { "com.dataartisans. appmanager.contr oller.deployment.s pec.version": "10", "taker": " \| vvp-0" }, "id": "425dfb74- 2bbb-4879-8273- 0b087a97****" }, "apiVersion": "v1", "kind": "Savepoint", "spec": { "savepointLocation ": "oss://flink- fullymanaged- 9cuwr9g7y1hl19/fli nk- savepoints/namesp aces/flinkteam/depl oyments/7325ac07 -e466-4c1b-b598- 311c6f2c103b/425 dfb74-2bbb-4879- 8273- 0b087a97b502" }, "status": { "state": "STARTED" } } | 详细信息。 |
| requestId | String | CBC799F0-AS7S- 1D30-8A4F- 882ED4DD**** | 请求ID。 |
| success | Boolean | true | 请求是否成功。 |

**示例**

实时计算（流计算） 参考请求示例

```json
POST /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/savepoints HTTP/1.1 { "namespace":"flinkteam", "workspace":"default" }
```

正常返回示例 `JSON` 格式

```json
{
 "data":"{\"metadata\":{\"createdAt\":\"2026-04-
28T02:13:28.277278Z\",\"jobId\":\"bf735437-b3ea-4d1a-847ebbacd144****\",\"workspace\":\"9cuwr9g7y1hl19\",\"nativeFormat\":false,\"modifiedAt\":\"20 -04-28T02:13:28.277278Z\",\"deploymentId\":\"7325ac07-e466-4c1b-b598- 311c6f2c103b\",\"origin\":\"USER_REQUEST\",\"resourceVersion\":1,\"namespace\":\"flinkteam ,\"annotations\": {\"com.dataartisans.appmanager.controller.deployment.spec.version\":\"10\",\"taker\":\"
| vvp-0\"},\"id\":\"425dfb74-2bbb-4879-8273-
0b087a97****\"},\"apiVersion\":\"v1\",\"kind\":\"Savepoint\",\"spec\": {\"savepointLocation\":\"oss://flink-fullymanaged-9cuwr9g7y1hl19/flinksavepoints/namespaces/flinkteam/deployments/7325ac07-e466-4c1b-b598- 311c6f2c103b/425dfb74-2bbb-4879-8273-0b087a97b502\"},\"status\": {\"state\":\"STARTED\"}}",
 "requestId":"CBC799F0-AS7S-1D30-8A4F-882ED4DD****",
 "success":true
}
```

`XML` 格式

```xml
<data>{&quot;metadata&quot;:{&quot;createdAt&quot;:&quot;2026-04- 28T02:13:28.277278Z&quot;,&quot;jobId&quot;:&quot;bf735437-b3ea-4d1a-847ebbacd144****&quot;,&quot;workspace&quot;:&quot;9cuwr9g7y1hl19&quot;,&quot;nativeFormat&quo :false,&quot;modifiedAt&quot;:&quot;2026-04- 28T02:13:28.277278Z&quot;,&quot;deploymentId&quot;:&quot;7325ac07-e466-4c1b-b598- 311c6f2c103b&quot;,&quot;origin&quot;:&quot;USER_REQUEST&quot;,&quot;resourceVersion&quot; ,&quot;namespace&quot;:&quot;flinkteam&quot;,&quot;annotations&quot;: {&quot;com.dataartisans.appmanager.controller.deployment.spec.version&quot;:&quot;10&quot; quot;taker&quot;:&quot; | vvp-0&quot;},&quot;id&quot;:&quot;425dfb74-2bbb-4879-8273- 0b087a97****&quot;},&quot;apiVersion&quot;:&quot;v1&quot;,&quot;kind&quot;:&quot;Savepoint uot;,&quot;spec&quot;:{&quot;savepointLocation&quot;:&quot;oss://flink-fullymanaged- 9cuwr9g7y1hl19/flink-savepoints/namespaces/flinkteam/deployments/7325ac07-e466-4c1bb598-311c6f2c103b/425dfb74-2bbb-4879-8273-0b087a97b502&quot;},&quot;status&quot;: {&quot;state&quot;:&quot;STARTED&quot;}}</data> <requestId>CBC799F0-AS7S-1D30-8A4F-882ED4DD****</requestId> <success>true</success>
```

###### CreateMember

实时计算（流计算） 参考

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /pop/workspaces/[workspace]/members/v1/namespaces/[namespace] HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| paramsJso n | String | Body | 否 | { "role": "viewer", "member": "242425410145292209" } | 用户授权信息，为指定用户授予指定业务权限，权限枚举：viewer、owner、 eidtor。 |
| workspace | String | Path | 是 | default | 作业所在的工作空间ID。您可以通过以下任意一种方式获取： 通过ListNamespaces获取。 在Flink全托管开发控制台工作空间详情中获取。 |
| namespac e | String | Path | 是 | flinkteam | 作业所在的项目空间名称。 |
| RegionId | String | Host | 是 | cn-wulan-env***-d01 | Region名称。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| success | Boolean | true | 请求是否成功。 |
| requestId | String | E3D311D5-77CB- 452F-B9EA- C215C8201363 | 请求ID。 |
| data | String | { "@type": "type.googleapis.c om/vvp.members.v 1.CreateMemberRe sponse", "member": { "role": "viewer", "member": "user:2424254101 45292209" } } | 用户业务授权详细信息。 |

**示例**

请求示例实时计算（流计算） 参考

```json
POST /pop/workspaces/[workspace]/members/v1/namespaces/[namespace] HTTP/1.1 { "workspace":"default", "namespace":"flinkteam", "RegionId":"cn-wulan-env***-d01" }
```

正常返回示例 `JSON` 格式

```json
{
 "data":"
{\"@type\":\"type.googleapis.com/vvp.members.v1.CreateMemberResponse\",\"member\": {\"role\":\"viewer\",\"member\":\"user:242425410145292209\"}}",
 "success":true,
 "requestId":"E3D311D5-77CB-452F-B9EA-C215C8201363"
}
```

`XML` 格式

```xml
<data> {&quot;@type&quot;:&quot;type.googleapis.com/vvp.members.v1.CreateMemberResponse&quot;,&qu ;member&quot;: {&quot;role&quot;:&quot;viewer&quot;,&quot;member&quot;:&quot;user:242425410145292209&quot }</data> <success>true</success> <requestId>E3D311D5-77CB-452F-B9EA-C215C8201363</requestId>
```

###### CreateFormat

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /pop/workspaces/[workspace]/sql/v1beta1/namespaces/[namespace]/formats HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | String | Host | 是 | cn-wulan-env***-d01 | Region ID。 |

实时计算（流计算） 参考

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| workspace | String | Path | 是 | default | 作业所在的工作空间ID。您可以通过以下任意一种方式获取： 通过ListNamespaces获取。 在Flink全托管开发控制台工作空间详情中获取。 |
| namespac e | String | Path | 是 | flinkteam | 作业所在的项目空间名称。 |
| paramsJso n | String | Body | 否 | {"creator": "", "sink": false, "modifier": "", "name": "namespaces/flinkteam/f ormats/customized-csv", "creator name": "", _ "source": true, "modifier name": "", _ "type": "customized- csv", "version name": "", _ "properties": [{"defaultValue": ",", "description": "", "definesFormat": false, "key": "format.column- delimiter", "required": false}], "packaged": false, "dependencies": ["http://flink- resource.oss-cn-wulan- env**-d01- a.intra.env**.shuguang.c om/format/customized- csv-demo-1.0- SNAPSHOT.jar"]} | 自定format创建参数。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| success | Boolean | true | 请求是否成功。 |

实时计算（流计算） 参考

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| data | String | { "@type": "type.googleapis.c om/vvp.sql.v1beta 1.CreateFormatRes ponse", "format": { "sink": false, "name": "namespaces/flinkt eam/formats/custo mized-csv", "source": true, "type": "customized-csv", "properties": [ { "defaultValue": ",", "description": "", "definesFormat": false, "key": "format.column- delimiter", "required": false } ], "packaged": false, "dependencies": [ "hdfs:///tmp/myfor mats/customized- csv-demo-1.0- SNAPSHOT.jar" ] } } | 新增format详细信息。 |
| requestId | String | 0ED81455-6971- 4EBA-BBD4- 3F686175080D | 请求ID。 |

**示例**

请求示例

```json
POST /pop/workspaces/[workspace]/sql/v1beta1/namespaces/[namespace]/formats HTTP/1.1 { "RegionId":"cn-wulan-env***-d01", "workspace":"default", "namespace":"flinkteam" }
```

正常返回示例 `JSON` 格式实时计算（流计算） 参考

```json
{
 "data":"
{\"@type\":\"type.googleapis.com/vvp.sql.v1beta1.CreateFormatResponse\",\"format\": {\"sink\":false,\"name\":\"namespaces/flinkteam/formats/customizedcsv\",\"source\":true,\"type\":\"customized-csv\",\"properties\": [{\"defaultValue\":\",\",\"description\":\"\",\"definesFormat\":false,\"key\":\"format.col n-delimiter\",\"required\":false}],\"packaged\":false,\"dependencies\": [\"hdfs:///tmp/myformats/customized-csv-demo-1.0-SNAPSHOT.jar\"]}}",
 "success":true,
 "requestId":"0ED81455-6971-4EBA-BBD4-3F686175080D"
}
```

`XML` 格式

```xml
<data> {&quot;@type&quot;:&quot;type.googleapis.com/vvp.sql.v1beta1.CreateFormatResponse&quot;,&q t;format&quot;: {&quot;sink&quot;:false,&quot;name&quot;:&quot;namespaces/flinkteam/formats/customizedcsv&quot;,&quot;source&quot;:true,&quot;type&quot;:&quot;customizedcsv&quot;,&quot;properties&quot;: [{&quot;defaultValue&quot;:&quot;,&quot;,&quot;description&quot;:&quot;&quot;,&quot;define ormat&quot;:false,&quot;key&quot;:&quot;format.columndelimiter&quot;,&quot;required&quot;:false}],&quot;packaged&quot;:false,&quot;dependencies uot;:[&quot;hdfs:///tmp/myformats/customized-csv-demo-1.0-SNAPSHOT.jar&quot;]}}</data> <success>true</success> <requestId>0ED81455-6971-4EBA-BBD4-3F686175080D</requestId>
```

###### CreateDeployment

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/deployments HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | String | Host | 是 | cn-wulan-env***-d01 | Region名称。 |
| namespac e | String | Path | 是 | flinkteam | 作业所在的项目空间名称。 |

实时计算（流计算） 参考

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| paramsJso n | String | Body | 否 | { "name": "namespaces/flinkteam/f ormats/customized-csv", "type": "customized- csv", "source": true, "sink": false, "properties": [ { "key": "format.column- delimiter", "required": false, "defaultValue": ",", "description": "" } ], "dependencies": [ "hdfs:///tmp/myformats/c ustomized-csv-demo- 1.0-SNAPSHOT.jar" ] } | 执行参数，sql脚本。 |
| workspace | String | Path | 是 | default | 作业所在的工作空间ID。您可以通过以下任意一种方式获取： 通过ListNamespaces获取。 在Flink全托管开发控制台工作空间详情中获取。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| success | Boolean | true | 请求是否成功。 |
| requestId | String | CBC799F0-AS7S- 1D30-8A4F- 882ED4DD**** | 请求ID。 |
|  |  | { "metadata": { "createdAt": "2026- 04- 24T03:46:53.34248 4Z", "workspace": "9cuwr9g7y1hl19", "modifiedAt": "2026-04- 24T03:46:53.34248 4Z", "resourceVersion": 1, "name": "sqlJob", "namespace": "flinkteam", "annotations": { "migration.display. enabled": "false", "creator": "23540697665705 7054", "modifier": "23540697665705 7054", "creatorName": "flinkadmin", "modifierName": |  |

实时计算（流计算） 参考

| 参数名称 | 类型 | "modifierName": "示fli例nkadmin", "priority": "5" }, | 说明 |
|---|---|---|---|
|  |  | "description": "cd1562be-02ed- 32cf-945b- 9769afe4c55e", "lock": { "metadata": { "createdAt": "2026- |  |
| data | String | 04-24T03:46:53Z", "workspace": "9cuwr9g7y1hl19", "modifiedAt": "2026-04- 24T03:46:53Z", "namespace": "flinkteam", "annotations": { "creator": "23540697665705 7054", "modifier": "23540697665705 7054" }, "id": "313fde08-4b44- 38b5-99c4- 7f3038449796" }, "apiVersion": "v1", "kind": "Lock", "spec": { "holderName": "flinkadmin", "holderId": "23540697665705 7054" } }, "id": "cee26b6e-d03b- 4a03-a628- a6fe665c525e", "parentId": "cd1562be-02ed- 32cf-945b- 9769afe4c55e", "labels": {} }, "apiVersion": "v1", "kind": "DeploymentDraft", "spec": { "template": { "metadata": { "annotations": { "native.kubernetes. mode": "true", "flink.queryable- state.enabled": "false", "flink.security.ssl.e nabled": "false" } }, "spec": { "artifact": { "kind": "SQLSCRIPT", "sqlScript": "INSERT INTO mySink SELECT SUBSTRING(a,0,10) AS a, CAST(CHAR LENGT _ H(a) AS BIGINT) as cnt FROM | 详细信息。 |

实时计算（流计算） 参考

|  |  | cnt FROM |  |
|---|---|---|---|
| 参数名称 | 类型 | m示y例Source;", "imageUserDefined | 说明 |
|  |  | ": false, "versionName": "vvr-8.0.7-flink- 1.17" }, "parallelism": 1, "batchMode": false, "resources": { "jobmanager": { "memory": "4Gi", "cpu": 1.0 }, "taskmanager": { "memory": "4Gi", "cpu": 1.0 } }, "logging": { "log4jLoggers": { "": "INFO" }, "logReservePolicy": { "expirationDays": 7, "openHistory": true }, "loggingProfile": "default" }, "flinkConfiguration" : {} } }, "restoreStrategy": { "kind": "LATEST STATE", _ "allowNonRestored State": false }, "state": "CANCELLED", "upgradeStrategy": { "kind": "STATELESS" }, "maxSavepointCre ationAttempts": 4, "maxJobCreationAt tempts": 1, "deploymentTarget Id": "a89ff052- 38c6-4fd3-9b91- e9c53f8ee019" } } |  |

**示例**

请求示例

```json
POST /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/deployments HTTP/1.1 { "RegionId":"cn-wulan-env***-d01", "namespace":"flinkteam", "workspace":"default" }
```

正常返回示例 `JSON` 格式实时计算（流计算） 参考

```json
{
 "data":"{\"metadata\":{\"createdAt\":\"2026-04-
24T03:46:53.342484Z\",\"workspace\":\"9cuwr9g7y1hl19\",\"modifiedAt\":\"2026-04- 24T03:46:53.342484Z\",\"resourceVersion\":1,\"name\":\"sqlJob\",\"namespace\":\"flinkteam\ \"annotations\": {\"migration.display.enabled\":\"false\",\"creator\":\"235406976657057054\",\"modifier\":\ 35406976657057054\",\"creatorName\":\"flinkadmin\",\"modifierName\":\"flinkadmin\",\"prior y\":\"5\"},\"description\":\"cd1562be-02ed-32cf-945b-9769afe4c55e\",\"lock\": {\"metadata\":{\"createdAt\":\"2026-04- 24T03:46:53Z\",\"workspace\":\"9cuwr9g7y1hl19\",\"modifiedAt\":\"2026-04- 24T03:46:53Z\",\"namespace\":\"flinkteam\",\"annotations\": {\"creator\":\"235406976657057054\",\"modifier\":\"235406976657057054\"},\"id\":\"313fde08 4b44-38b5-99c4-7f3038449796\"},\"apiVersion\":\"v1\",\"kind\":\"Lock\",\"spec\": {\"holderName\":\"flinkadmin\",\"holderId\":\"235406976657057054\"}},\"id\":\"cee26b6ed03b-4a03-a628-a6fe665c525e\",\"parentId\":\"cd1562be-02ed-32cf-945b- 9769afe4c55e\",\"labels\": {}},\"apiVersion\":\"v1\",\"kind\":\"DeploymentDraft\",\"spec\":{\"template\": {\"metadata\":{\"annotations\":{\"native.kubernetes.mode\":\"true\",\"flink.queryablestate.enabled\":\"false\",\"flink.security.ssl.enabled\":\"false\"}},\"spec\": {\"artifact\":{\"kind\":\"SQLSCRIPT\",\"sqlScript\":\"INSERT INTO mySink SELECT SUBSTRING(a,0,10) AS a, CAST(CHAR_LENGTH(a) AS BIGINT) as cnt FROM mySource;\",\"imageUserDefined\":false,\"versionName\":\"vvr-8.0.7-flink- 1.17\"},\"parallelism\":1,\"batchMode\":false,\"resources\":{\"jobmanager\": {\"memory\":\"4Gi\",\"cpu\":1.0},\"taskmanager\": {\"memory\":\"4Gi\",\"cpu\":1.0}},\"logging\":{\"log4jLoggers\": {\"\":\"INFO\"},\"logReservePolicy\": {\"expirationDays\":7,\"openHistory\":true},\"loggingProfile\":\"default\"},\"flinkConfigu tion\":{}}},\"restoreStrategy\": {\"kind\":\"LATEST_STATE\",\"allowNonRestoredState\":false},\"state\":\"CANCELLED\",\"upgr eStrategy\": {\"kind\":\"STATELESS\"},\"maxSavepointCreationAttempts\":4,\"maxJobCreationAttempts\":1,\ eploymentTargetId\":\"a89ff052-38c6-4fd3-9b91-e9c53f8ee019\"}}",
 "success":true,
 "requestId":"CBC799F0-AS7S-1D30-8A4F-882ED4DD****"
}
```

`XML` 格式实时计算（流计算） 参考

```xml
<data>{&quot;metadata&quot;:{&quot;createdAt&quot;:&quot;2026-04- 24T03:46:53.342484Z&quot;,&quot;workspace&quot;:&quot;9cuwr9g7y1hl19&quot;,&quot;modifiedA quot;:&quot;2026-04- 24T03:46:53.342484Z&quot;,&quot;resourceVersion&quot;:1,&quot;name&quot;:&quot;sqlJob&quot &quot;namespace&quot;:&quot;flinkteam&quot;,&quot;annotations&quot;: {&quot;migration.display.enabled&quot;:&quot;false&quot;,&quot;creator&quot;:&quot;2354069 657057054&quot;,&quot;modifier&quot;:&quot;235406976657057054&quot;,&quot;creatorName&quot &quot;flinkadmin&quot;,&quot;modifierName&quot;:&quot;flinkadmin&quot;,&quot;priority&quot &quot;5&quot;},&quot;description&quot;:&quot;cd1562be-02ed-32cf-945b- 9769afe4c55e&quot;,&quot;lock&quot;:{&quot;metadata&quot;: {&quot;createdAt&quot;:&quot;2026-04- 24T03:46:53Z&quot;,&quot;workspace&quot;:&quot;9cuwr9g7y1hl19&quot;,&quot;modifiedAt&quot; quot;2026-04- 24T03:46:53Z&quot;,&quot;namespace&quot;:&quot;flinkteam&quot;,&quot;annotations&quot;: {&quot;creator&quot;:&quot;235406976657057054&quot;,&quot;modifier&quot;:&quot;23540697665 57054&quot;},&quot;id&quot;:&quot;313fde08-4b44-38b5-99c4- 7f3038449796&quot;},&quot;apiVersion&quot;:&quot;v1&quot;,&quot;kind&quot;:&quot;Lock&quot &quot;spec&quot;: {&quot;holderName&quot;:&quot;flinkadmin&quot;,&quot;holderId&quot;:&quot;2354069766570570 &quot;}},&quot;id&quot;:&quot;cee26b6e-d03b-4a03-a628a6fe665c525e&quot;,&quot;parentId&quot;:&quot;cd1562be-02ed-32cf-945b- 9769afe4c55e&quot;,&quot;labels&quot;: {}},&quot;apiVersion&quot;:&quot;v1&quot;,&quot;kind&quot;:&quot;DeploymentDraft&quot;,&qu ;spec&quot;:{&quot;template&quot;:{&quot;metadata&quot;:{&quot;annotations&quot;: {&quot;native.kubernetes.mode&quot;:&quot;true&quot;,&quot;flink.queryablestate.enabled&quot;:&quot;false&quot;,&quot;flink.security.ssl.enabled&quot;:&quot;false&q t;}},&quot;spec&quot;:{&quot;artifact&quot;: {&quot;kind&quot;:&quot;SQLSCRIPT&quot;,&quot;sqlScript&quot;:&quot;INSERT INTO mySink SELECT SUBSTRING(a,0,10) AS a, CAST(CHAR_LENGTH(a) AS BIGINT) as cnt FROM mySource;&quot;,&quot;imageUserDefined&quot;:false,&quot;versionName&quot;:&quot;vvr- 8.0.7-flink- 1.17&quot;},&quot;parallelism&quot;:1,&quot;batchMode&quot;:false,&quot;resources&quot;: {&quot;jobmanager&quot;: {&quot;memory&quot;:&quot;4Gi&quot;,&quot;cpu&quot;:1.0},&quot;taskmanager&quot;: {&quot;memory&quot;:&quot;4Gi&quot;,&quot;cpu&quot;:1.0}},&quot;logging&quot;: {&quot;log4jLoggers&quot;:{&quot;&quot;:&quot;INFO&quot;},&quot;logReservePolicy&quot;: {&quot;expirationDays&quot;:7,&quot;openHistory&quot;:true},&quot;loggingProfile&quot;:&qu ;default&quot;},&quot;flinkConfiguration&quot;:{}}},&quot;restoreStrategy&quot;: {&quot;kind&quot;:&quot;LATEST_STATE&quot;,&quot;allowNonRestoredState&quot;:false},&quot; ate&quot;:&quot;CANCELLED&quot;,&quot;upgradeStrategy&quot;: {&quot;kind&quot;:&quot;STATELESS&quot;},&quot;maxSavepointCreationAttempts&quot;:4,&quot; xJobCreationAttempts&quot;:1,&quot;deploymentTargetId&quot;:&quot;a89ff052-38c6-4fd3- 9b91-e9c53f8ee019&quot;}}</data> <success>true</success> <requestId>CBC799F0-AS7S-1D30-8A4F-882ED4DD****</requestId>
```

###### CreateConnector

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。 实时计算（流计算） 参考

**请求语法**

```
POST /pop/workspaces/[workspace]/sql/v1beta1/namespaces/[namespace]/connectors HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | String | Host | 是 | cn-wulan-env***-d01 | Region名称。 |
| workspace | String | Path | 是 | default | 作业所在的工作空间ID。您可以通过以下任意一种方式获取： 通过ListNamespaces获取。 在Flink全托管开发控制台工作空间详情中获取。 |
| namespac e | String | Path | 是 | flinkteam | 作业所在的项目空间名称。 |

实时计算（流计算） 参考

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| paramsJso n | String | Body | 否 | { "type": "hologres-fix", "name": "namespaces/flinkteam/ connectors/hologres-fix", "packaged": false, "source": true, "sink": true, "lookup": false, "dependencies": [ "hdfs:///vvp/data/sql- artifacts/namespaces/fli nkteam/custom- connectors/2024-03- 11T05-51- 25.289740Z/ververica- connector-hologres-1.15- vvr-6.0-fix.jar" ], "supportedFormats": [ "json","csv" ], "properties": [ { "key": "connector", "required": true, "defaultValue": "hologres-fix", "description": "", "definesFormat": false }, { "key": "dbname", "required": true, "defaultValue": "", "description": "", "definesFormat": false }, { "key": "endpoint", "required": true, "defaultValue": "", "description": "", "definesFormat": false }, { "key": "tablename", "required": true, "defaultValue": "", "description": "", "definesFormat": false } ] } | 新connector参数信息，包括connector类型、名称、 支持的连接参数、能否作为 sourc、sink、支持的 format、依赖的jar等。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| success | Boolean | true | 请求是否成功。 |

实时计算（流计算） 参考

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| data | String | { "connector": { "lookup": true, "supportedFormats ": [ "json", "csv" ], "environments": [], "sink": true, "name": "namespaces/flinkt eam/connectors/ho logres-fix", "source": true, "type": "hologres- fix", "properties": [ { "defaultValue": "hologres-fix", "description": "", "definesFormat": false, "key": "connector", "required": true }, { "defaultValue": "", "description": "", "definesFormat": false, "key": "dbname", "required": true }, { "defaultValue": "", "description": "", "definesFormat": false, "key": "endpoint", "required": true }, { "defaultValue": "", "description": "", "definesFormat": false, "key": "tablename", "required": true } ], "packaged": false, "dependencies": [ "hdfs:///tmp/mycon nectors/ververica- connector- hologres-1.15-vvr- 6.0-fix.jar" ] }, "@type": "type.googleapis.c om/vvp.sql.v1beta 1.CreateConnector Response" } | 新connector详细信息。 |
| requestId | String | CBC799F0-AS7S- 1D30-8A4F- 882ED4DD**** | 请求ID。 |

**示例**

请求示例实时计算（流计算） 参考

```json
POST /pop/workspaces/[workspace]/sql/v1beta1/namespaces/[namespace]/connectors HTTP/1.1 { "RegionId":"cn-wulan-env***-d01", "workspace":"default", "namespace":"flinkteam" }
```

正常返回示例 `JSON` 格式

```json
{
 "data":"{\"connector\":{\"lookup\":true,\"supportedFormats\":
[\"json\",\"csv\"],\"environments\": [],\"sink\":true,\"name\":\"namespaces/flinkteam/connectors/hologresfix\",\"source\":true,\"type\":\"hologres-fix\",\"properties\": [{\"defaultValue\":\"hologresfix\",\"description\":\"\",\"definesFormat\":false,\"key\":\"connector\",\"required\":true {\"defaultValue\":\"\",\"description\":\"\",\"definesFormat\":false,\"key\":\"dbname\",\"r uired\":true}, {\"defaultValue\":\"\",\"description\":\"\",\"definesFormat\":false,\"key\":\"endpoint\",\ equired\":true}, {\"defaultValue\":\"\",\"description\":\"\",\"definesFormat\":false,\"key\":\"tablename\", required\":true}],\"packaged\":false,\"dependencies\": [\"hdfs:///tmp/myconnectors/ververica-connector-hologres-1.15-vvr-6.0fix.jar\"]},\"@type\":\"type.googleapis.com/vvp.sql.v1beta1.CreateConnectorResponse\"}",
 "success":true,
 "requestId":"CBC799F0-AS7S-1D30-8A4F-882ED4DD****"
}
```

`XML` 格式

```xml
<data>{&quot;connector&quot;:{&quot;lookup&quot;:true,&quot;supportedFormats&quot;: [&quot;json&quot;,&quot;csv&quot;],&quot;environments&quot;: [],&quot;sink&quot;:true,&quot;name&quot;:&quot;namespaces/flinkteam/connectors/hologresfix&quot;,&quot;source&quot;:true,&quot;type&quot;:&quot;hologresfix&quot;,&quot;properties&quot;:[{&quot;defaultValue&quot;:&quot;hologresfix&quot;,&quot;description&quot;:&quot;&quot;,&quot;definesFormat&quot;:false,&quot;key&q t;:&quot;connector&quot;,&quot;required&quot;:true}, {&quot;defaultValue&quot;:&quot;&quot;,&quot;description&quot;:&quot;&quot;,&quot;definesF mat&quot;:false,&quot;key&quot;:&quot;dbname&quot;,&quot;required&quot;:true}, {&quot;defaultValue&quot;:&quot;&quot;,&quot;description&quot;:&quot;&quot;,&quot;definesF mat&quot;:false,&quot;key&quot;:&quot;endpoint&quot;,&quot;required&quot;:true}, {&quot;defaultValue&quot;:&quot;&quot;,&quot;description&quot;:&quot;&quot;,&quot;definesF mat&quot;:false,&quot;key&quot;:&quot;tablename&quot;,&quot;required&quot;:true}],&quot;pa aged&quot;:false,&quot;dependencies&quot;:[&quot;hdfs:///tmp/myconnectors/ververicaconnector-hologres-1.15-vvr-6.0fix.jar&quot;]},&quot;@type&quot;:&quot;type.googleapis.com/vvp.sql.v1beta1.CreateConnecto esponse&quot;}</data> <success>true</success> <requestId>CBC799F0-AS7S-1D30-8A4F-882ED4DD****</requestId>
```

实时计算（流计算） 参考

###### CreateFolder

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/folders HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | String | Host | 是 | cn-wulan-env***-d01 | Region名称。 |
| workspace | String | Path | 是 | default | 作业所在的工作空间 ID。您可以通过以下任意一种方式获取： 通过 ListNamespaces 获取。 在Flink 全托管开发控制台工作空间详情中获取。 |
| namespac e | String | Path | 是 | flinkteam | 作业所在的项目空间名称。 |
| paramsJso n | String | Body | 否 | { "metadata": { "parentId": "cd1562be- 02ed-32cf-945b- 9769afe4****", "name": "changsha", "namespace": "flinkteam" } } | 执行参数，sql脚本。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| success | Boolean | true | 表示业务请求是否成功。 |

实时计算（流计算） 参考

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| data | String | { "eagleEyeTraceId": "0a2318ab177734 16555583153d**** ", "asapiSuccess": true, "asapiRequestId": "A11B1055-5AB7- 4AB4-AEB0- 32947AEB****", "data": { "metadata": { "createdAt": "2026- 04- 28T02:00:55.598** **", "workspace": "9cuwr9g7y1hl19", "modifiedAt": "2026-04- 28T02:00:55.598** **", "namespace": "flinkteam", "name": "changsha", "annotations": { "creator": "23540697665705* ***", "modifier": "23540697665705* ***", "creatorName": "flinkadmin", "modifierName": "flinkadmin" }, "id": "6b252d46- 8653-4d69-9183- 1a16b5a8****", "type": "development", "parentId": "cd1562be-02ed- 32cf-945b- 9769afe4****" }, "apiVersion": "v1", "kind": "Folder", "spec": { "children": [] } } | 当success为false，返回空值。 当success为true，返回授权信息。 |
| requestId | String | CBC799F0-AS7S- 1D30-8A4F- 882ED4DD**** | 请求ID。 |

**示例**

请求示例实时计算（流计算） 参考

```json
POST /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/folders HTTP/1.1 { "RegionId":"cn-wulan-env***-d01", "workspace":"default", "namespace":"flinkteam" }
```

正常返回示例 `JSON` 格式

```json
{
 "data":"
{\"eagleEyeTraceId\":\"0a2318ab17773416555583153d****\",\"asapiSuccess\":true,\"asapiReque Id\":\"A11B1055-5AB7-4AB4-AEB0-32947AEB****\",\"data\":{\"metadata\":{\"createdAt\":\"20 26-04-28T02:00:55.598****\",\"workspace\":\"9cuwr9g7y1hl19\",\"modifiedAt\":\"2026-04- 28T02:00:55.598****\",\"namespace\":\"flinkteam\",\"name\":\"changsha\",\"annotations\": {\"creator\":\"23540697665705****\",\"modifier\":\"23540697665705****\",\"creatorName\":\" inkadmin\",\"modifierName\":\"flinkadmin\"},\"id\":\"6b252d46-8653-4d69-9183- 1a16b5a8****\",\"type\":\"development\",\"parentId\":\"cd1562be-02ed-32cf-945b- 9769afe4****\"},\"apiVersion\":\"v1\",\"kind\":\"Folder\",\"spec\":{\"children\":[]}}",
 "success":true,
 "requestId":"CBC799F0-AS7S-1D30-8A4F-882ED4DD****"
}
```

`XML` 格式

```xml
<data> {&quot;eagleEyeTraceId&quot;:&quot;0a2318ab17773416555583153d****&quot;,&quot;asapiSuccess uot;:true,&quot;asapiRequestId&quot;:&quot;A11B1055-5AB7-4AB4-AEB0- 32947AEB****&quot;,&quot;data&quot;:{&quot;metadata&quot;: {&quot;createdAt&quot;:&quot;2026-04- 28T02:00:55.598****&quot;,&quot;workspace&quot;:&quot;9cuwr9g7y1hl19&quot;,&quot;modifiedA quot;:&quot;2026-04- 28T02:00:55.598****&quot;,&quot;namespace&quot;:&quot;flinkteam&quot;,&quot;name&quot;:&qu ;changsha&quot;,&quot;annotations&quot;: {&quot;creator&quot;:&quot;23540697665705****&quot;,&quot;modifier&quot;:&quot;23540697665 5****&quot;,&quot;creatorName&quot;:&quot;flinkadmin&quot;,&quot;modifierName&quot;:&quot; inkadmin&quot;},&quot;id&quot;:&quot;6b252d46-8653-4d69-9183- 1a16b5a8****&quot;,&quot;type&quot;:&quot;development&quot;,&quot;parentId&quot;:&quot;cd1 2be-02ed-32cf-945b- 9769afe4****&quot;},&quot;apiVersion&quot;:&quot;v1&quot;,&quot;kind&quot;:&quot;Folder&qu ;,&quot;spec&quot;:{&quot;children&quot;:[]}}</data> <success>true</success> <requestId>CBC799F0-AS7S-1D30-8A4F-882ED4DD****</requestId>
```

###### ListJobs

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。 实时计算（流计算） 参考

**请求语法**

```
GET /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/jobs HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | String | Host | 是 | cn-wulan-env***-d01 | Region ID。 |
| deployme ntId | String | Query | 是 | d0b3abf0-4bfe-46b1- a324-5b7def580c00 | 作业ID。 |
| namespac e | String | Path | 是 | flinkteam | 作业所在的项目空间名称。 |
| workspace | String | Path | 是 | default | 作业所在的工作空间ID。您可以通过以下任意一种方式获取： 通过ListNamespaces获取。 在Flink全托管开发控制台工作空间详情中获取。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| data | String | {"success": true,"message": "","plan": ""} | 详细信息。 |
| requestId | String | CBC799F0-AS7S- 1D30-8A4F- 882ED4DD**** | 请求ID。 |
| success | Boolean | true | 请求是否成功。 |

**示例**

请求示例

```
GET /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/jobs HTTP/1.1 &RegionId=cn-wulan-env***-d01 &deploymentId=d0b3abf0-4bfe-46b1-a324-5b7def580c00 &namespace=flinkteam &workspace=default
```

&公共请求参数正常返回示例 `JSON` 格式实时计算（流计算） 参考

```json
{
 "data":"{\"success\": true,\"message\": \"\",\"plan\": \"\"}",
 "requestId":"CBC799F0-AS7S-1D30-8A4F-882ED4DD****",
 "success":true
}
```

`XML` 格式

```xml
<data>{&quot;success&quot;: true,&quot;message&quot;: &quot;&quot;,&quot;plan&quot;: &quot;&quot;}</data> <requestId>CBC799F0-AS7S-1D30-8A4F-882ED4DD****</requestId> <success>true</success>
```

###### ReplaceDeployment

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
PUT /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/deployments/[deploymentId] HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | String | Host | 是 | cn-wulan-env***-d01 | Region ID。 |
| namespac e | String | Path | 是 | flinkteam | 作业所在的项目空间名称。 |
| deployme ntId | String | Path | 是 | d0b3abf0-4bfe-46b1- a324-5b7def580c00 | 作业ID。 |

实时计算（流计算） 参考

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| paramsJso n | String | Body | 否 | {"name":"jarjob","engin eVersion":"vvr-11.5.0- flink- 1.20","executionMode":" STREAMING","imageUser Defined":false,"deploym entTarget": {"mode":"PER JOB","na _ me":"dt- flinkteam"},"artifact": {"kind":"JAR","jarArtifact ":{"jarUri":"oss://flink- fullymanaged- apmd99ri0du673/artifact s/namespaces/flinkteam/ TopSpeedWindowing.jar" }},"kerberosConfig": {"kerberosEnabled":fals e},"namespace":"flinkte am"} | 执行参数，sql脚本。 |
| workspace | String | Path | 是 | default | 作业所在的工作空间ID。您可以通过以下任意一种方式获取： 通过ListNamespaces获取。 在Flink全托管开发控制台工作空间详情中获取。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| success | Boolean | true | 请求是否成功。 |
| requestId | String | CBC799F0-AS7S- 1D30-8A4F- 882ED4DD**** | 请求ID。 |
|  |  | { "deploymentId" : "7f4143a2-2eee- 4c5c-8803- a50d388514ac", "name" : "jarjob", "executionMode" : "STREAMING", "streamingResourc eSetting" : { "resourceSettingMo de" : "BASIC", "basicResourceSett ing" : { "parallelism" : 1, "jobmanagerResou rceSettingSpec" : { "cpu" : 1.0, "memory" : "4Gi" }, "taskmanagerReso |  |

实时计算（流计算） 参考

| 参数名称 | 类型 | "taskmanagerReso u示rc例eSettingSpec" : { "cpu" : 1.0, | 说明 |
|---|---|---|---|
|  |  | "memory" : "4Gi" } } }, |  |
| data | Integer | "kerberosConfig" : { "kerberosEnabled" : false }, "labels" : { }, "engineVersion" : "vvr-11.5.0-flink- 1.20", "referencedDeploy mentDraftId" : "", "deploymentHasCh anged" : true, "taker" : " \| vvp-0", "priority" : 5, "resourceTuning" : { "mode" : "none", "resourceTuningId" : "", "resourceTuningNa me" : "", "scheduledPlanIsCa ncelling" : false }, "autopilot" : { "mode" : "", "recommendation" : "", "ignoreRecommen dation" : "" }, "deploymentTarget " : { "mode" : "PER JOB", "name" _ : "dt-flinkteam" }, "artifact" : { "kind" : "JAR", "jarArtifact" : { "jarUri" : "oss://flink- fullymanaged- apmd99ri0du673/a rtifacts/namespace s/flinkteam/TopSpe edWindowing.jar" } }, "flinkConf" : { "execution.checkpo inting.interval" : "180s", "restart- strategy.fixed- delay.attempts" : "2147483647", "table.exec.state.ttl " : "36 h", "restart- strategy" : "fixed- delay", "execution.checkpo inting.min-pause" : "180s", "restart- strategy.fixed- delay.delay" : "10 s" }, "logging" : { "loggingProfile" : "default", "log4jLoggers" : [ { "loggerName" : "", "loggerLevel" : | 详细信息。 |

实时计算（流计算） 参考

|  |  | loggerLevel : |  |
|---|---|---|---|
| 参数名称 | 类型 | "示IN例FO" } ], "logReservePolicy" | 说明 |
|  |  | : { "openHistory" : true, "expirationDays" : 7 } }, "jobSummary" : { "starting" : 0, "running" : 0, "cancelling" : 0, "cancelled" : 0, "finished" : 0, "failed" : 0 }, "workspace" : "apmd99ri0du673", "namespace" : "flinkteam", "creator" : "20678996188752 3346", "creatorName" : "flinkadmin", "modifier" : "20678996188752 3346", "modifierName" : "flinkadmin", "createdAt" : 1777526754, "modifiedAt" : 1777526754 } |  |

**示例**

请求示例

```json
PUT /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/deployments/[deploymentId] HTTP/1.1 { "RegionId":"cn-wulan-env***-d01", "namespace":"flinkteam", "deploymentId":"d0b3abf0-4bfe-46b1-a324-5b7def580c00", "workspace":"default" }
```

正常返回示例 `JSON` 格式实时计算（流计算） 参考

```json
{
 "data":"{\"deploymentId\":\"7f4143a2-2eee-4c5c-8803-
a50d388514ac\",\"name\":\"jarjob\",\"executionMode\":\"STREAMING\",\"streamingResourceSett g\":{\"resourceSettingMode\":\"BASIC\",\"basicResourceSetting\": {\"parallelism\":1,\"jobmanagerResourceSettingSpec\": {\"cpu\":1.0,\"memory\":\"4Gi\"},\"taskmanagerResourceSettingSpec\": {\"cpu\":1.0,\"memory\":\"4Gi\"}}},\"kerberosConfig\": {\"kerberosEnabled\":false},\"labels\":{},\"engineVersion\":\"vvr-11.5.0-flink- 1.20\",\"referencedDeploymentDraftId\":\"\",\"deploymentHasChanged\":true,\"taker\":\"
| vvp-0\",\"priority\":5,\"resourceTuning\":
{\"mode\":\"none\",\"resourceTuningId\":\"\",\"resourceTuningName\":\"\",\"scheduledPlanIs ncelling\":false},\"autopilot\": {\"mode\":\"\",\"recommendation\":\"\",\"ignoreRecommendation\":\"\"},\"deploymentTarget\" {\"mode\":\"PER_JOB\",\"name\":\"dt-flinkteam\"},\"artifact\": {\"kind\":\"JAR\",\"jarArtifact\":{\"jarUri\":\"oss://flink-fullymanagedapmd99ri0du673/artifacts/namespaces/flinkteam/TopSpeedWindowing.jar\"}},\"flinkConf\":{ \"execution.checkpointing.interval\":\"180s\",\"restart-strategy.fixeddelay.attempts\":\"2147483647\",\"table.exec.state.ttl\":\"36 h\",\"restartstrategy\":\"fixed-delay\",\"execution.checkpointing.min-pause\":\"180s\",\"restartstrategy.fixed-delay.delay\":\"10 s\"},\"logging\": {\"loggingProfile\":\"default\",\"log4jLoggers\": [{\"loggerName\":\"\",\"loggerLevel\":\"INFO\"}],\"logReservePolicy\": {\"openHistory\":true,\"expirationDays\":7}},\"jobSummary\": {\"starting\":0,\"running\":0,\"cancelling\":0,\"cancelled\":0,\"finished\":0,\"failed\":0 \"workspace\":\"apmd99ri0du673\",\"namespace\":\"flinkteam\",\"creator\":\"206789961887523 6\",\"creatorName\":\"flinkadmin\",\"modifier\":\"206789961887523346\",\"modifierName\":\" inkadmin\",\"createdAt\":1777526754,\"modifiedAt\":1777526754}",
 "success":true,
 "requestId":"CBC799F0-AS7S-1D30-8A4F-882ED4DD****"
}
```

`XML` 格式实时计算（流计算） 参考

```xml
<data>{&quot;deploymentId&quot;:&quot;7f4143a2-2eee-4c5c-8803a50d388514ac&quot;,&quot;name&quot;:&quot;jarjob&quot;,&quot;executionMode&quot;:&quot;STR MING&quot;,&quot;streamingResourceSetting&quot;: {&quot;resourceSettingMode&quot;:&quot;BASIC&quot;,&quot;basicResourceSetting&quot;: {&quot;parallelism&quot;:1,&quot;jobmanagerResourceSettingSpec&quot;: {&quot;cpu&quot;:1.0,&quot;memory&quot;:&quot;4Gi&quot;},&quot;taskmanagerResourceSettingS c&quot;: {&quot;cpu&quot;:1.0,&quot;memory&quot;:&quot;4Gi&quot;}}},&quot;kerberosConfig&quot;:{ &quot;kerberosEnabled&quot;:false},&quot;labels&quot;: {},&quot;engineVersion&quot;:&quot;vvr-11.5.0-flink- 1.20&quot;,&quot;referencedDeploymentDraftId&quot;:&quot;&quot;,&quot;deploymentHasChanged uot;:true,&quot;taker&quot;:&quot; | vvp- 0&quot;,&quot;priority&quot;:5,&quot;resourceTuning&quot;: {&quot;mode&quot;:&quot;none&quot;,&quot;resourceTuningId&quot;:&quot;&quot;,&quot;resourc uningName&quot;:&quot;&quot;,&quot;scheduledPlanIsCancelling&quot;:false},&quot;autopilot& ot;: {&quot;mode&quot;:&quot;&quot;,&quot;recommendation&quot;:&quot;&quot;,&quot;ignoreRecomme ation&quot;:&quot;&quot;},&quot;deploymentTarget&quot;: {&quot;mode&quot;:&quot;PER_JOB&quot;,&quot;name&quot;:&quot;dtflinkteam&quot;},&quot;artifact&quot;: {&quot;kind&quot;:&quot;JAR&quot;,&quot;jarArtifact&quot;: {&quot;jarUri&quot;:&quot;oss://flink-fullymanagedapmd99ri0du673/artifacts/namespaces/flinkteam/TopSpeedWindowing.jar&quot;}},&quot;flinkCon quot;:{&quot;execution.checkpointing.interval&quot;:&quot;180s&quot;,&quot;restartstrategy.fixeddelay.attempts&quot;:&quot;2147483647&quot;,&quot;table.exec.state.ttl&quot;:&quot;36 h&quot;,&quot;restart-strategy&quot;:&quot;fixeddelay&quot;,&quot;execution.checkpointing.minpause&quot;:&quot;180s&quot;,&quot;restart-strategy.fixed-delay.delay&quot;:&quot;10 s&quot;},&quot;logging&quot;: {&quot;loggingProfile&quot;:&quot;default&quot;,&quot;log4jLoggers&quot;: [{&quot;loggerName&quot;:&quot;&quot;,&quot;loggerLevel&quot;:&quot;INFO&quot;}],&quot;log servePolicy&quot;: {&quot;openHistory&quot;:true,&quot;expirationDays&quot;:7}},&quot;jobSummary&quot;: {&quot;starting&quot;:0,&quot;running&quot;:0,&quot;cancelling&quot;:0,&quot;cancelled&quo :0,&quot;finished&quot;:0,&quot;failed&quot;:0},&quot;workspace&quot;:&quot;apmd99ri0du673 uot;,&quot;namespace&quot;:&quot;flinkteam&quot;,&quot;creator&quot;:&quot;206789961887523 6&quot;,&quot;creatorName&quot;:&quot;flinkadmin&quot;,&quot;modifier&quot;:&quot;20678996 87523346&quot;,&quot;modifierName&quot;:&quot;flinkadmin&quot;,&quot;createdAt&quot;:17775 754,&quot;modifiedAt&quot;:1777526754}</data> <success>true</success> <requestId>CBC799F0-AS7S-1D30-8A4F-882ED4DD****</requestId>
```

##### 存算分离v2版

###### ValidateSqlStatement

验证实时计算引擎中的SQL语句是否正确。

**请求头**

实时计算（流计算） 参考

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| workspace | String | Header | 是 | a14bd5d90a**** | 工作空间ID。 |

**请求语法**

```
POST /api/v2/namespaces/[namespace]/sql-statement/validate HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| namespac e | String | Path | 是 | default-namespace | 项目空间名称。 |

| 参数名称 | 类型 | 位置 |  | 是否必选 |  | 示例 |  | 说明 |
|---|---|---|---|---|---|---|---|---|
| body | string | wholebody |  | 是 |  | {'statemen |  | 待验证的 sql 内容。 |
|  |  |  |  |  |  |  | {'statemen |  |
|  |  |  |  |  |  | t': 'SELECT |  | 待 |
|  |  |  |  |  |  |  |  | 容 |
|  |  |  |  |  |  | 1'} |  |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| reason | String | "" | 错误原因。 业务正常时该字段返回空值。 |
| eagleEyeTrace Id | String | 0a1129361783048 3500182**** | 鹰眼追踪ID。 |
| asapiSuccess | Boolean | true | 表示API调用成功，返回结果符合预期，无错误发生。 |
| asapiRequestI d | String | CF3A87DE-268D- 4E4B-865F- CCC91**** | asapi请求ID。 |
| success | Boolean | true | 请求是否成功。 |
| requestId | String | CBC799F0-AS7S- 1D30-8A4F- 882ED4DD**** | 请求ID。 |

实时计算（流计算） 参考

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| data | String | { "validationResult": "VALIDATION RESU _ LT VALID SELECT _ _ _ QUERY", "success": true, "message": "SQL validate success", "errorDetails": { "columnNumber": 0, "endLineNumber": 0, "invalidFlinkConf": [], "endColumnNumbe r": 0, "lineNumber": 0, "message": "" } } | 当success为false，返回空值。 当success为true，返回详细数据。 |
| errorCode | String | "" | 当success为false时，该值不为空，表示业务错误码。 当success为true时，该值为空。 |
| errorMessage | String | "" | 当success为false，返回业务错误信息。 当success为true，返回空值。 |
| httpCode | Integer | 200 | HTTP状态码。 |
| message | String | "" | 附加信息。 |

**示例**

请求示例

```json
POST /api/v2/namespaces/[namespace]/sql-statement/validate HTTP/1.1 { "namespace":"default-namespace", "body":"{'statement': 'SELECT 1'}" }
```

正常返回示例 `JSON` 格式实时计算（流计算） 参考

```json
{
 "reason":"",
 "eagleEyeTraceId":"0a11293617830483500182****",
 "asapiSuccess":true,
 "asapiRequestId":"CF3A87DE-268D-4E4B-865F-CCC91****",
 "data":"{    \"validationResult\": \"VALIDATION_RESULT_VALID_SELECT_QUERY\",    \"succe
ss\": true, \"message\": \"SQL validate success\", \"errorDetails\": { \"colu mnNumber\": 0, \"endLineNumber\": 0, \"invalidFlinkConf\": [], \"endColumnNumber\": 0, \"lineNumber\": 0, \"message\": \"\" } }",
 "success":true,
 "requestId":"CBC799F0-AS7S-1D30-8A4F-882ED4DD****",
 "errorMessage":"",
 "errorCode":"",
 "httpCode":200,
 "message":""
}
```

`XML` 格式

```xml
<reason /> <eagleEyeTraceId>0a11293617830483500182****</eagleEyeTraceId> <asapiSuccess>true</asapiSuccess> <asapiRequestId>CF3A87DE-268D-4E4B-865F-CCC91****</asapiRequestId> <data>{
    &quot;validationResult&quot;: &quot;VALIDATION_RESULT_VALID_SELECT_QUERY&quot;,
    &quot;success&quot;: true,
    &quot;message&quot;: &quot;SQL validate success&quot;,
    &quot;errorDetails&quot;: {
      &quot;columnNumber&quot;: 0,
      &quot;endLineNumber&quot;: 0,
      &quot;invalidFlinkConf&quot;: [],
      &quot;endColumnNumber&quot;: 0,
      &quot;lineNumber&quot;: 0,
      &quot;message&quot;: &quot;&quot;
    }
  }</data>
 <success>true</success>
 <requestId>CBC799F0-AS7S-1D30-8A4F-882ED4DD****</requestId>
 <errorMessage  />
 <errorCode  />
 <httpCode>200</httpCode>
 <message  />
```

###### UpdateMember

更新更新特定项目空间下的成员信息。

**请求头**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|

实时计算（流计算） 参考

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| workspace | String | Header | 是 | a14bd5d90a**** | 工作空间ID。 |

**请求语法**

```
PUT /gateway/v2/namespaces/[namespace]/members HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| namespac e | String | Path | 是 | default-namespace | 项目空间名称。 |

| 参数名称 | 类型 |  | 位置 |  | 是否必选 |  | 示例 |  | 说明 |  |
|---|---|---|---|---|---|---|---|---|---|---|
| body | string |  | wholebody |  |  |  | {'member': |  |  |  |
|  |  |  |  |  |  |  |  | {'member': |  |  |
|  |  |  |  |  |  |  | '23136675424 |  |  |  |
|  |  |  |  |  |  |  |  |  | 成员授权信息详 |  |
|  |  |  |  | ody | 否 |  |  |  | 成员授权信息详 |  |
|  |  |  |  |  |  |  | 6****', |  | 情。 |  |
|  |  |  |  |  |  |  |  |  | 情。 |  |
|  |  |  |  |  |  |  | 'role': |  |  |  |
|  |  |  |  |  |  |  | 'VIEWER'} |  |  |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| success | Boolean | true | 请求是否成功。 |
| requestId | String | CBC799F0-AS7S- 1D30-8A4F- 882ED4DD**** | 请求ID。 |
| data | String | { "member": "2313667542****", "role": "viewer" } | 当success为false，返回空值。 当success为true，返回详细数据。 |
| errorCode | String | "" | 当success为false时，该值不为空，表示业务错误码。 当success为true时，该值为空。 |
| errorMessage | String | "" | 当success为false，返回业务错误信息。 当success为true，返回空值。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例实时计算（流计算） 参考

```json
PUT /gateway/v2/namespaces/[namespace]/members HTTP/1.1 { "namespace":"default-namespace" }
```

正常返回示例 `JSON` 格式

```json
{
 "data":"{    \"member\": \"2313667542****\",    \"role\": \"viewer\"  }",
 "success":true,
 "requestId":"CBC799F0-AS7S-1D30-8A4F-882ED4DD****",
 "errorMessage":"",
 "errorCode":"",
 "httpCode":200
}
```

`XML` 格式

```xml
<data>{
    &quot;member&quot;: &quot;2313667542****&quot;,
    &quot;role&quot;: &quot;viewer&quot;
  }</data>
 <success>true</success>
 <requestId>CBC799F0-AS7S-1D30-8A4F-882ED4DD****</requestId>
 <errorMessage  />
 <errorCode  />
 <httpCode>200</httpCode>
```

###### UpdateDeployment

更新部署配置或应用程序版本，以实现服务的平滑升级和变更管理。

**请求头**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| workspace | String | Header | 是 | a14bd5d90a**** | 工作空间ID。 |

**请求语法**

```
PUT /api/v2/namespaces/[namespace]/deployments/[deploymentId] HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| namespac e | String | Path | 是 | default-namespace | 项目空间名称。 |

| 实时计算（流计 | 算） |  |  | Flink | 存算分离版开发指南·OpenAP 参考 |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| deployme ntId | String | Path | 是 | d0b3abf0-4bfe-46b1- a324-5b7d**** | 作业ID。 |

|  | 参数名称 |  |  |  | 类型 |  |  |  | 位置 |  |  |  |  |  | 是否必选 |  |  |  |  |  | 示例 |  |  | 说明 |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | {"artifact |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | {"artifact |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | ": |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | {"kind":"SQL |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | SCRIPT","sql |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | Artifact": |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | {"sqlScript" |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | :"CREATE |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | TEMPORARY |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | TABLE |  | datah (st |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | ub table |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | _ rname |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | VARCHAR) |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | with ( |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | ' = |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 'datagen' |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | ); |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | TEMPORARY |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | TABLE kafka table _ (strname |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | VARCHAR, |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | lens |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | BIGINT) |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | with ( |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | ' = |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 'print' |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | ); |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | kafka table _ |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | SUBSTRING |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | (strname, |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 0, 10) AS |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | strname, |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | CAST |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | (CHAR LENGTH _ |  |  |  |  |

实时计算（流计算） 参考

|  |  |  |  |  |  |  |  |  |  |  | (strname) |  |  |  | 说明 |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  | 参数名称 |  | 类型 |  | 位置 |  | 是否必选 |  | 示例 |  |  |  | 说明 |  |
|  |  |  |  |  |  |  |  |  |  |  | AS BIGINT) |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  | AS lens |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  | FROM |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  | ble; |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  | r":"20877848 |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  | 2972****","c |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  | reatorName": |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  | "flinkadmin" |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  | ,"deployment |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  | HasChanged": |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  | true,"deploy |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  | mentId":"1e3 |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  | 2fa1e-fd0e- |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  | 48e6-81d2- |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  | fa66443****" |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  | ,"deployment |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  | Target": |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  | {"mode":"PER |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  | JOB","name" _ |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  | :"dt- |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  | flinkteam"}, |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  | "engineVersi |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  | on":"vvr- |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  | 8.0.7-flink- |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  | 1.17","execu |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  | tionMode":"S |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  | TREAMING","f |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  | linkConf": |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  | {"execution. |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  | checkpointin |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  | g.interval": |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  | "180s","exec |  |  |  |  |  |
|  |  |  | body |  | string |  | wholebody |  | 是 |  | ution.checkp |  |  |  | 需要更新的作业 |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 内容。 |  |
|  |  |  |  |  |  |  |  |  |  |  | ointing.min- |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  | pause":"180s |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  | ","restart- |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  | strategy":"f |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  | ixed- |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  | delay","rest |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  | art- |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  | strategy.fix |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  | ed- |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  | delay.attemp |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  | ts":"214748* |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  | ***","restar |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  | t- |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  | strategy.fix |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  | ed- |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  | delay.delay" |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  | :"10 |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  | s","table.ex |  |  |  |  |  |

实时计算（流计算） 参考

|  |  |  |  | ec.state.ttl |  |  |
|---|---|---|---|---|---|---|
| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |  |
|  |  |  |  | ":"36 |  |  |
|  |  |  |  | h"},"jobSumm |  |  |
|  |  |  |  | ary": |  |  |
|  |  |  |  | {"cancelled" |  |  |
|  |  |  |  | :0,"cancelli |  |  |
|  |  |  |  | ng":0,"faile |  |  |
|  |  |  |  | d":0,"finish |  |  |
|  |  |  |  | ed":0,"runni |  |  |
|  |  |  |  | ng":0,"start |  |  |
|  |  |  |  | ing":0},"log |  |  |
|  |  |  |  | ging": |  |  |
|  |  |  |  | {"log4jLogge |  |  |
|  |  |  |  | rs": |  |  |
|  |  |  |  | [{"loggerLev |  |  |
|  |  |  |  | el":"INFO"," |  |  |
|  |  |  |  | loggerName": |  |  |
|  |  |  |  | ""}],"logRes |  |  |
|  |  |  |  | ervePolicy": |  |  |
|  |  |  |  | {"expiration |  |  |
|  |  |  |  | Days":7,"ope |  |  |
|  |  |  |  | nHistory":tr |  |  |
|  |  |  |  | ue},"logging |  |  |
|  |  |  |  | Profile":"de |  |  |
|  |  |  |  | fault"},"mod |  |  |
|  |  |  |  | ifier":"2087 |  |  |
|  |  |  |  | 7848297216** |  |  |
|  |  |  |  | **","modifie |  |  |
|  |  |  |  | rName":"flin |  |  |
|  |  |  |  | kadmin","nam |  |  |
|  |  |  |  | e":"sqlJob", |  |  |
|  |  |  |  | "namespace": |  |  |
|  |  |  |  | "flinkteam", |  |  |
|  |  |  |  | "streamingRe |  |  |
|  |  |  |  | sourceSettin |  |  |
|  |  |  |  | g": |  |  |
|  |  |  |  | {"basicResou |  |  |
|  |  |  |  | rceSetting": |  |  |
|  |  |  |  | {"jobmanager |  |  |
|  |  |  |  | ResourceSett |  |  |
|  |  |  |  | ingSpec": |  |  |
|  |  |  |  | {"cpu":1.0," |  |  |
|  |  |  |  | memory":"4Gi |  |  |
|  |  |  |  | "},"parallel |  |  |
|  |  |  |  | ism":1,"task |  |  |
|  |  |  |  | managerResou |  |  |
|  |  |  |  | rceSettingSp |  |  |
|  |  |  |  | ec": |  |  |
|  |  |  |  | {"cpu":1.0," |  |  |
|  |  |  |  | memory":"4Gi |  |  |
|  |  |  |  | "}},"resourc |  |  |
|  |  |  |  | eSettingMode |  |  |
|  |  |  |  | ":"BASIC"}} |  |  |

实时计算（流计算） 参考

| 参数名称 | 类型 | 位置 | 是否必选 |  |  | 例 | 说明 |
|---|---|---|---|---|---|---|---|
|  |  |  |  |  | 示 |  |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| success | Boolean | true | 请求是否成功。 |
| requestId | String | CBC799F0-AS7S- 1D30-8A4F- 882ED4DD**** | 请求ID。 |
|  |  | { "artifact": { "kind": "SQLSCRIPT", "sqlArtifact": { "sqlScript": "CREATE TEMPORARY TABLE `datahub table` _ (strname VARCHAR) with ( 'connector' = 'datagen' ); CREATE TEMPORARY TABLE `kafka table` _ (strname VARCHAR, lens BIGINT) with ( 'connector' = 'print' ); INSERT INTO kafka table _ SELECT SUBSTRING (strname, 0, 10) AS strname, CAST (CHAR LENGTH _ (strname) AS BIGINT) AS lens FROM datahub table; _ " } }, "creator": "208778482972*** *", "creatorName": "flinkadmin", "deploymentHasCh anged": true, |  |

实时计算（流计算） 参考

| 参数名称 | 类型 | "deploymentId": 示例 "f9d616ef-4422- | 说明 |
|---|---|---|---|
| data | String | 42b5-b95c- f691d44****", "deploymentTarget ": { "mode": "PER JOB", "name": _ "dt-flinkteam" }, "engineVersion": "vvr-8.0.7-flink- 1.17", "executionMode": "STREAMING", "flinkConf": { "execution.checkpo inting.interval": "180s", "table.exec.state.ttl ": "36 h", "restart- strategy.fixed- delay.delay": "10 s", "restart- strategy": "fixed- delay", "restart- strategy.fixed- delay.attempts": "21474****", | 当success为false，返回空值。 当success为true，返回详细数据。 |
|  |  | "execution.checkpo inting.min-pause": "180s" }, "jobSummary": { "cancelled": 0, "cancelling": 0, "failed": 0, "finished": 0, "running": 0, "starting": 0 }, "logging": { "log4jLoggers": [ { "loggerLevel": "INFO", "loggerName": "" } ], "logReservePolicy": { "expirationDays": 7, "openHistory": true }, "loggingProfile": "default" }, "modifier": "20877848297**** ", "modifierName": "flinkadmin", "name": "sqlJob", "namespace": "flinkteam", "streamingResourc eSetting": { "basicResourceSett ing": { "jobmanagerResou rceSettingSpec": { "cpu": 1.0, "memory": "4Gi" }, "parallelism": 1, "taskmanagerReso urceSettingSpec": |  |
| > 文档版本：20260 | 730 |  | 57 |

实时计算（流计算） 参考

| 参数名称 | 类型 | { "cpu": 1.0, 示例 "memory": "4Gi" } | 说明 |
|---|---|---|---|
|  |  | }, "resourceSettingMo de": "BASIC" } } |  |
| errorCode | String | "" | 当success为false时，该值不为空，表示业务错误码。 当success为true时，该值为空。 |
| errorMessage | String | "" | 当success为false，返回业务错误信息。 当success为true，返回空值。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```json
PUT /api/v2/namespaces/[namespace]/deployments/[deploymentId] HTTP/1.1 { "namespace":"default-namespace", "deploymentId":"d0b3abf0-4bfe-46b1-a324-5b7d****", "body":"{"artifact":{"kind":"SQLSCRIPT","sqlArtifact":{"sqlScript":"CREATE TEMPORARY TABLE `datahub_table` (strname VARCHAR)with ( 'connector' = 'datagen' );CREATE TEMPORARY TABLE `kafka_table` (strname VARCHAR, lens BIGINT)with ( 'connector' = 'print' );INSERT INTO kafka_tableSELECT SUBSTRING (strname, 0, 10) AS strname, CAST (CHAR_LENGTH (strname) AS BIGINT) AS lensFROM datahub_table;"}},"creator":"208778482972****","creatorName":"flinkadmin","deploymentHasCh ged":true,"deploymentId":"1e32fa1e-fd0e-48e6-81d2-fa66443****","deploymentTarget": {"mode":"PER_JOB","name":"dt-flinkteam"},"engineVersion":"vvr-8.0.7-flink-1.17","executi onMode":"STREAMING","flinkConf": {"execution.checkpointing.interval":"180s","execution.checkpointing.minpause":"180s","restart-strategy":"fixed-delay","restart-strategy.fixeddelay.attempts":"214748****","restart-strategy.fixed-delay.delay":"10 s","table.exec.state.ttl":"36 h"},"jobSummary": {"cancelled":0,"cancelling":0,"failed":0,"finished":0,"running":0,"starting":0},"logging" {"log4jLoggers":[{"loggerLevel":"INFO","loggerName":""}],"logReservePolicy": {"expirationDays":7,"openHistory":true},"loggingProfile":"default"},"modifier":"2087784829 16****","modifierName":"flinkadmin","name":"sqlJob","namespace":"flinkteam","streamingReso ceSetting":{"basicResourceSetting":{"jobmanagerResourceSettingSpec": {"cpu":1.0,"memory":"4Gi"},"parallelism":1,"taskmanagerResourceSettingSpec": {"cpu":1.0,"memory":"4Gi"}},"resourceSettingMode":"BASIC"}}" }
```

正常返回示例 `JSON` 格式实时计算（流计算） 参考

```json
{
 "data":"{    \"artifact\": {      \"kind\": \"SQLSCRIPT\",      \"sqlArtifact\": {
\"sqlScript\": \"CREATE TEMPORARY TABLE `datahub_table` (strname VARCHAR)\with (\ 'co nnector' = 'datagen'\ );\\CREATE TEMPORARY TABLE `kafka_table` (strname VARCHAR, lens BIGINT)\with (\ 'connector' = 'print'\ );\\INSERT INTO kafka_table\SELECT SUBSTRING (strname, 0, 10) AS strname, CAST (CHAR_LENGTH (strname) AS BIGINT) AS lens\FROM\ datahub_table;\\" } }, \"creator\": \"208778482972****\", \"creatorName\": \"flinkadmin\", \"deploymentHasChanged\": true, \"deploymentId\": \"f9d616ef-4422- 42b5-b95c-f691d44****\", \"deploymentTarget\": { \"mode\": \"PER_JOB\", \"n ame\": \"dt-flinkteam\" }, \"engineVersion\": \"vvr-8.0.7-flink-1.17\", \"execu tionMode\": \"STREAMING\", \"flinkConf\": { \"execution.checkpointing.interval\": \"180s\", \"table.exec.state.ttl\": \"36 h\", \"restart-strategy.fixed-delay.delay\": \"10 s\", \"restart-strategy\": \"fixed-del ay\", \"restart-strategy.fixed-delay.attempts\": \"21474****\", \"execution.checkpointing.min-pause\": \"180s\" }, \"jobSummary\": { \"cancel led\": 0, \"cancelling\": 0, \"failed\": 0, \"finished\": 0, \"running\": 0, \"starting\": 0 }, \"logging\": { \"log4jLoggers\": [ { \"loggerLevel\": \"INFO\", \"loggerName\": \"\" } ], \"logReservePolicy\": { \"expirationDays\": 7, \"openHistory\": true }, \"loggingProfile\": \"default\" }, \"modifier\": \"20877848297****\", \ "modifierName\": \"flinkadmin\", \"name\": \"sqlJob\", \"namespace\": \"flinkteam\ ", \"streamingResourceSetting\": { \"basicResourceSetting\": { \"jobmanagerResourceSettingSpec\": { \"cpu\": 1.0, \"memory\": \"4Gi\" }, \"parallelism\": 1, \"taskmanagerResourceSettingSpec\": { \"cpu\": 1.0, \"memory\": \"4Gi\" } }, \"resourceSettingMode\": \"BASIC\" } }",
 "success":true,
 "requestId":"CBC799F0-AS7S-1D30-8A4F-882ED4DD****",
 "errorMessage":"",
 "errorCode":"",
 "httpCode":200
}
```

`XML` 格式

```xml
<data>{
    &quot;artifact&quot;: {
      &quot;kind&quot;: &quot;SQLSCRIPT&quot;,
      &quot;sqlArtifact&quot;: {
        &quot;sqlScript&quot;: &quot;CREATE TEMPORARY TABLE `datahub_table` (strname VAR
CHAR)with ( &#x27;connector&#x27; = &#x27;datagen&#x27; );CREATE TEMPORARY TABLE `kafka_table` (strname VARCHAR, lens BIGINT)with ( &#x27;connector&#x27; = &#x27;print&#x27; );INSERT INTO kafka_tableSELECT SUBSTRING (strname, 0, 10) AS strname, CAST (CHAR_LENGTH (strname) AS BIGINT) AS lensFROM datahub_table;&quot;
      }
    },
    &quot;creator&quot;: &quot;208778482972****&quot;,
    &quot;creatorName&quot;: &quot;flinkadmin&quot;,
    &quot;deploymentHasChanged&quot;: true,
    &quot;deploymentId&quot;: &quot;f9d616ef-4422-42b5-b95c-f691d44****&quot;,
    &quot;deploymentTarget&quot;: {
      &quot;mode&quot;: &quot;PER_JOB&quot;,
      &quot;name&quot;: &quot;dt-flinkteam&quot;
},
```

实时计算（流计算） 参考

```
    },
    &quot;engineVersion&quot;: &quot;vvr-8.0.7-flink-1.17&quot;,
    &quot;executionMode&quot;: &quot;STREAMING&quot;,
    &quot;flinkConf&quot;: {
      &quot;execution.checkpointing.interval&quot;: &quot;180s&quot;,
      &quot;table.exec.state.ttl&quot;: &quot;36 h&quot;,
      &quot;restart-strategy.fixed-delay.delay&quot;: &quot;10 s&quot;,
      &quot;restart-strategy&quot;: &quot;fixed-delay&quot;,
      &quot;restart-strategy.fixed-delay.attempts&quot;: &quot;21474****&quot;,
      &quot;execution.checkpointing.min-pause&quot;: &quot;180s&quot;
    },
    &quot;jobSummary&quot;: {
      &quot;cancelled&quot;: 0,
      &quot;cancelling&quot;: 0,
      &quot;failed&quot;: 0,
      &quot;finished&quot;: 0,
      &quot;running&quot;: 0,
      &quot;starting&quot;: 0
    },
    &quot;logging&quot;: {
      &quot;log4jLoggers&quot;: [
        {
          &quot;loggerLevel&quot;: &quot;INFO&quot;,
          &quot;loggerName&quot;: &quot;&quot;
        }
```

`],`

```xml
      &quot;logReservePolicy&quot;: {
        &quot;expirationDays&quot;: 7,
        &quot;openHistory&quot;: true
      },
      &quot;loggingProfile&quot;: &quot;default&quot;
    },
    &quot;modifier&quot;: &quot;20877848297****&quot;,
    &quot;modifierName&quot;: &quot;flinkadmin&quot;,
    &quot;name&quot;: &quot;sqlJob&quot;,
    &quot;namespace&quot;: &quot;flinkteam&quot;,
    &quot;streamingResourceSetting&quot;: {
      &quot;basicResourceSetting&quot;: {
        &quot;jobmanagerResourceSettingSpec&quot;: {
          &quot;cpu&quot;: 1.0,
          &quot;memory&quot;: &quot;4Gi&quot;
        },
        &quot;parallelism&quot;: 1,
        &quot;taskmanagerResourceSettingSpec&quot;: {
          &quot;cpu&quot;: 1.0,
          &quot;memory&quot;: &quot;4Gi&quot;
        }
      },
      &quot;resourceSettingMode&quot;: &quot;BASIC&quot;
    }
  }</data>
 <success>true</success>
 <requestId>CBC799F0-AS7S-1D30-8A4F-882ED4DD****</requestId>
 <errorMessage  />
 <errorCode  />
```

实时计算（流计算） 参考

```xml
 <httpCode>200</httpCode>
```

###### StopJob

停止作业实例。

**请求头**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| workspace | String | Header | 是 | a14bd5d90a**** | 工作空间ID。 |

**请求语法**

```
POST /api/v2/namespaces/[namespace]/jobs/[jobId]:stop HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| namespac e | String | Path | 是 | default-namespace | 项目空间名称。 |
| jobId | String | Path | 是 | 5af678c0-7db0-4650- 94c2-d2604f0a**** | 作业实例ID。 |

| 参数名称 | 类型 | 位置 |  | 是否必选 |  | 示例 |  | 说明 |
|---|---|---|---|---|---|---|---|---|
| body | string | wholebody |  | 是 |  | {'stopStra |  | 停止作业实例参数。 |
|  |  |  |  |  |  |  | {'stopStra | 停止作业实例参 |
|  |  |  |  |  |  | tegy': |  |  |
|  |  |  |  |  |  | 'NONE'} |  |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| success | Boolean | true | 请求是否成功。 |
| requestId | String | CBC799F0-AS7S- 1D30-8A4F- 882ED4DD**** | 请求ID。 |
|  |  | { "artifact": { "kind": "SQLSCRIPT", "sqlArtifact": { "sqlScript": "CREATE TEMPORARY TABLE `datahub table` _ (strname VARCHAR) |  |

| link存算分离版开发参考 | 指南·OpenAPI |  | 实时计算（流计算） |
|---|---|---|---|
| 参数名称 | 类型 | with ( 示例 'connector' = | 说明 |
| data | String | 'datagen' ); CREATE TEMPORARY TABLE `kafka table` _ (strname VARCHAR, lens BIGINT) with ( 'connector' = 'print' ); INSERT INTO kafka table _ SELECT SUBSTRING (strname, 0, 10) AS strname, CAST (CHAR LENGTH _ (strname) AS BIGINT) AS lens FROM datahub table; _ " } }, "creator": "208778482972*** *", "creatorName": "flinkadmin", "deploymentId": "5ef6cbcf-9df1- 4d54-ab32- 0a2c81****", "deploymentName" : "sqlJob", "engineVersion": "vvr-8.0.7-flink- 1.17", "executionMode": "STREAMING", "flinkConf": { "table.exec.operato r-name.max- length": "10240", "env.java.opts.job manager": "- Xloggc:/opt/flink/lo g/jobmanager- gc.log - XX:+UseGCLogFile Rotation - XX:NumberOfGCLo gFiles=2 - XX:GCLogFileSize= 50M", "***":"***" }, "jobId": "65eb3696-db7d- 4a58-9851- cda26f252924", "logging": { "log4j2Configuratio nTemplate": " | 当success为false，返回空值。 当success为true，返回详细数据。 |

实时计算（流计算） 参考

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| errorCode | String | "" | 当success为false时，该值不为空，表示业务错误码。 当success为true时，该值为空。 |
| errorMessage | String | "" | 当success为false，返回业务错误信息。 当success为true，返回空值。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```json
POST /api/v2/namespaces/[namespace]/jobs/[jobId]:stop HTTP/1.1 { "namespace":"default-namespace", "jobId":"5af678c0-7db0-4650-94c2-d2604f0a****", "body":"{'stopStrategy': 'NONE'}" }
```

正常返回示例 `JSON` 格式实时计算（流计算） 参考

```json
{
 "data":"{    \"artifact\": {      \"kind\": \"SQLSCRIPT\",      \"sqlArtifact\": {
\"sqlScript\": \"CREATE TEMPORARY TABLE `datahub_table` (strname VARCHAR)\with (\ 'co nnector' = 'datagen'\ );\\CREATE TEMPORARY TABLE `kafka_table` (strname VARCHAR, lens BIGINT)\with (\ 'connector' = 'print'\ );\\INSERT INTO kafka_table\SELECT SUBSTRING (strname, 0, 10) AS strname, CAST (CHAR_LENGTH (strname) AS BIGINT) AS lens\FROM\ datahub_table;\\" } }, \"creator\": \"208778482972****\", \"creatorName\": \"flinkadmin\", \"deploymentId\": \"5ef6cbcf-9df1-4d54-ab32-0a2c81****\", \"deploy mentName\": \"sqlJob\", \"engineVersion\": \"vvr-8.0.7-flink-1.17\", \"executionMo de\": \"STREAMING\", \"flinkConf\": { \"table.exec.operator-name.max-length\": \ "10240\", \"env.java.opts.jobmanager\": \"-Xloggc:/opt/flink/log/jobmanager-gc.log -XX:+UseGCLogFileRotation -XX:NumberOfGCLogFiles=2 -XX:GCLogFileSize=50M\", \"***\" :\"***\" }, \"jobId\": \"65eb3696-db7d-4a58-9851-cda26f252924\", \"logging\": { \"log4j2ConfigurationTemplate\": \"<?xml version=\\\"1.0\\\" encoding=\\\"UTF-8\\ \" ****\\", \"log4jLoggers\": [ { \"loggerLevel\": \"INFO\", \"loggerName\": \"\" } ], \"logReservePolicy\": { \"expirationDays\": 7, \"openHistory\": true } }, \"metric\": { \"totalCpu\": 2.0, \"totalMemoryByte\": 85899**** }, \"modifier\": \"2087784829721****\", \"modifierName\": \"flinkadmin\", \"namespace\": \"flinktea m\", \"restoreStrategy\": { \"kind\": \"NONE\" }, \"startTime\": 178305*** *, \"status\": { \"currentJobStatus\": \"RUNNING\", \"running\": { \ "observedFlinkJobRestarts\": 0, \"observedFlinkJobStatus\": \"RUNNING\" } }, \"streamingResourceSetting\": { \"basicResourceSetting\": { \"jobmanagerResourceSettingSpec\": { \"cpu\": 1.0, \"memory\": \"4Gi\" }, \"parallelism\": 1, \"taskmanagerResourceSettingSpec\": { \"cpu\": 1.0, \"memory\": \"4Gi\" } }, \"resourceSettingMode\": \"BASIC\" }, \"userFlinkConf\": { \"execution.checkpointing.interval\": \"180 s\", \"table.exec.state.ttl\": \"36 h\", \"restart-strategy.fixed-delay.delay\ ": \"10 s\", \"restart-strategy\": \"fixed-delay\", \"restart-strategy.fixed-d elay.attempts\": \"214748****\", \"execution.checkpointing.min-pause\": \"180s\" } }",
 "success":true,
 "requestId":"CBC799F0-AS7S-1D30-8A4F-882ED4DD****",
 "errorMessage":"",
 "errorCode":"",
 "httpCode":200
}
```

`XML` 格式

```xml
<data>{
    &quot;artifact&quot;: {
      &quot;kind&quot;: &quot;SQLSCRIPT&quot;,
      &quot;sqlArtifact&quot;: {
        &quot;sqlScript&quot;: &quot;CREATE TEMPORARY TABLE `datahub_table` (strname VAR
CHAR)with ( &#x27;connector&#x27; = &#x27;datagen&#x27; );CREATE TEMPORARY TABLE `kafka_table` (strname VARCHAR, lens BIGINT)with ( &#x27;connector&#x27; = &#x27;print&#x27; );INSERT INTO kafka_tableSELECT SUBSTRING (strname, 0, 10) AS strname, CAST (CHAR_LENGTH (strname) AS BIGINT) AS lensFROM datahub_table;&quot;
      }
    },
    &quot;creator&quot;: &quot;208778482972****&quot;,
    &quot;creatorName&quot;: &quot;flinkadmin&quot;,
&quot;deploymentId&quot;:&quot;5ef6cbcf-9df1-4d54-ab32-0a2c81****&quot;,
```

实时计算（流计算） 参考

```
    &quot;deploymentId&quot;: &quot;5ef6cbcf9df14d54ab320a2c81
&quot;,
    &quot;deploymentName&quot;: &quot;sqlJob&quot;,
    &quot;engineVersion&quot;: &quot;vvr-8.0.7-flink-1.17&quot;,
    &quot;executionMode&quot;: &quot;STREAMING&quot;,
    &quot;flinkConf&quot;: {
      &quot;table.exec.operator-name.max-length&quot;: &quot;10240&quot;,
      &quot;env.java.opts.jobmanager&quot;: &quot;-Xloggc:/opt/flink/log/jobmanager-gc.l
og -XX:+UseGCLogFileRotation -XX:NumberOfGCLogFiles=2 -XX:GCLogFileSize=50M&quot;,
      &quot;***&quot;:&quot;***&quot;
      },
    &quot;jobId&quot;: &quot;65eb3696-db7d-4a58-9851-cda26f252924&quot;,
    &quot;logging&quot;: {
      &quot;log4j2ConfigurationTemplate&quot;: &quot;&lt;?xml version=\&quot;1.0\&quot;
encoding=\&quot;UTF-8\&quot; ****&quot;,
      &quot;log4jLoggers&quot;: [
        {
          &quot;loggerLevel&quot;: &quot;INFO&quot;,
          &quot;loggerName&quot;: &quot;&quot;
        }
```

`],`

```
      &quot;logReservePolicy&quot;: {
        &quot;expirationDays&quot;: 7,
        &quot;openHistory&quot;: true
      }
    },
    &quot;metric&quot;: {
      &quot;totalCpu&quot;: 2.0,
      &quot;totalMemoryByte&quot;: 85899****
    },
    &quot;modifier&quot;: &quot;2087784829721****&quot;,
    &quot;modifierName&quot;: &quot;flinkadmin&quot;,
    &quot;namespace&quot;: &quot;flinkteam&quot;,
    &quot;restoreStrategy&quot;: {
      &quot;kind&quot;: &quot;NONE&quot;
    },
    &quot;startTime&quot;: 178305****,
    &quot;status&quot;: {
      &quot;currentJobStatus&quot;: &quot;RUNNING&quot;,
      &quot;running&quot;: {
        &quot;observedFlinkJobRestarts&quot;: 0,
        &quot;observedFlinkJobStatus&quot;: &quot;RUNNING&quot;
      }
    },
    &quot;streamingResourceSetting&quot;: {
      &quot;basicResourceSetting&quot;: {
        &quot;jobmanagerResourceSettingSpec&quot;: {
          &quot;cpu&quot;: 1.0,
          &quot;memory&quot;: &quot;4Gi&quot;
        },
        &quot;parallelism&quot;: 1,
        &quot;taskmanagerResourceSettingSpec&quot;: {
          &quot;cpu&quot;: 1.0,
          &quot;memory&quot;: &quot;4Gi&quot;
        }
      },
```

实时计算（流计算） 参考

```xml
      &quot;resourceSettingMode&quot;: &quot;BASIC&quot;
    },
    &quot;userFlinkConf&quot;: {
      &quot;execution.checkpointing.interval&quot;: &quot;180s&quot;,
      &quot;table.exec.state.ttl&quot;: &quot;36 h&quot;,
      &quot;restart-strategy.fixed-delay.delay&quot;: &quot;10 s&quot;,
      &quot;restart-strategy&quot;: &quot;fixed-delay&quot;,
      &quot;restart-strategy.fixed-delay.attempts&quot;: &quot;214748****&quot;,
      &quot;execution.checkpointing.min-pause&quot;: &quot;180s&quot;
    }
  }</data>
 <success>true</success>
 <requestId>CBC799F0-AS7S-1D30-8A4F-882ED4DD****</requestId>
 <errorMessage  />
 <errorCode  />
 <httpCode>200</httpCode>
```

###### StartJobWithParams

启动作业实例。

**请求头**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| workspace | String | Header | 是 | a14bd5d90a**** | 工作空间ID。 |

**请求语法**

```
POST /api/v2/namespaces/[namespace]/jobs:start HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| namespac e | String | Path | 是 | default-namespace | 项目空间名称。 |

|  |  | 参数名称 |  | 类型 |  |  | 位置 |  |  | 是否必选 |  | 示例 |  | 说明 |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  | body |  | string |  |  |  |  |  |  |  | {'deployme |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  | {'deployme |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  | ntId': |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  | '0ba1ce1c- |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  | 6cf1-4763- |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  | 8d45- |  | 作业实例启动参 |  |
|  |  |  |  |  | ring |  | wholebody |  |  | 否 |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  | 244f9****', |  | 数。 |  |
|  |  |  |  |  |  |  |  |  |  |  |  | 'restoreStra |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  | tegy': |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  | {'kind': |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  | 'NONE'}} |  |  |  |

实时计算（流计算） 参考

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| success | Boolean | true | 请求是否成功。 |
| requestId | String | CBC799F0-AS7S- 1D30-8A4F- 882ED4DD**** | 请求ID。 |
| data | String | { "artifact": { "kind": "SQLSCRIPT", "sqlArtifact": { "sqlScript": "CREATE TEMPORARY TABLE `datahub table` _ (strname VARCHAR) with ( 'connector' = 'datagen' ); CREATE TEMPORARY TABLE `kafka table` _ (strname VARCHAR, lens BIGINT) with ( 'connector' = 'print' ); INSERT INTO kafka table _ SELECT SUBSTRING (strname, 0, 10) AS strname, CAST (CHAR LENGTH _ (strname) AS BIGINT) AS lens FROM datahub table; _ " } }, "creator": "20877848297**** ", "creatorName": "flinkadmin", "deploymentId": "b74e0fc1-914b- 4009-b11c- 52e6278****", "deploymentName" : "sqlJob", "engineVersion": "vvr-8.0.7-flink- 1.17", "executionMode": "STREAMING", "flinkConf": { "table.exec.operato r-name.max- length": "10240", | 当success为false，返回空值。 当success为true，返回详细数据。 |

实时计算（流计算） 参考

| 参数名称 | 类型 | "env.java.opts.job 示例 manager": "- | 说明 |
|---|---|---|---|
|  |  | Xloggc:/opt/flink/lo g/jobmanager- gc.log - XX:+UseGCLogFile Rotation - XX:NumberOfGCLo gFiles=2 - XX:GCLogFileSize= 50M", "***":"***" }, "jobId": "003fbc67- 1c8c-4147-9bf4- 19da2****7", "logging": { "log4j2Configuratio nTemplate": " |  |
| errorCode | String | "" | 当success为false时，该值不为空，表示业务错误码。 当success为true时，该值为空。 |
| errorMessage | String | "" | 当success为false，返回业务错误信息。 当success为true，返回空值。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```json
POST /api/v2/namespaces/[namespace]/jobs:start HTTP/1.1 { "namespace":"default-namespace" }
```

正常返回示例 `JSON` 格式实时计算（流计算） 参考

```json
{
 "data":"{    \"artifact\": {      \"kind\": \"SQLSCRIPT\",      \"sqlArtifact\": {
\"sqlScript\": \"CREATE TEMPORARY TABLE `datahub_table` (strname VARCHAR)\with (\ 'co nnector' = 'datagen'\ );\\CREATE TEMPORARY TABLE `kafka_table` (strname VARCHAR, lens BIGINT)\with (\ 'connector' = 'print'\ );\\INSERT INTO kafka_table\SELECT SUBSTRING (strname, 0, 10) AS strname, CAST (CHAR_LENGTH (strname) AS BIGINT) AS lens\FROM\ datahub_table;\\" } }, \"creator\": \"20877848297****\", \"creatorName\": \"flinkadmin\", \"deploymentId\": \"b74e0fc1-914b-4009-b11c-52e6278****\", \"deplo ymentName\": \"sqlJob\", \"engineVersion\": \"vvr-8.0.7-flink-1.17\", \"executionM ode\": \"STREAMING\", \"flinkConf\": { \"table.exec.operator-name.max-length\": \"10240\", \"env.java.opts.jobmanager\": \"-Xloggc:/opt/flink/log/jobmanager-gc.log -XX:+UseGCLogFileRotation -XX:NumberOfGCLogFiles=2 -XX:GCLogFileSize=50M\", \"***\" :\"***\" }, \"jobId\": \"003fbc67-1c8c-4147-9bf4-19da2****7\", \"logging\": { \"log4j2ConfigurationTemplate\": \"<?xml version=\\\"1.0\\\" encoding=\\\"UTF-8\\\"
****\\",      \"log4jLoggers\": [        {          \"loggerLevel\": \"INFO\",          \
"loggerName\": \"\" } ], \"logReservePolicy\": { \"expirationDays\": 7, \"openHistory\": true } }, \"modifier\": \"208778482972****\", \"modifierName\": \"flinkadmin\", \"namespace\": \"flinkteam \", \"restoreStrategy\": { \"kind\": \"NONE\" }, \"startTime\": 1783059223, \"status\": { \"currentJobStatus\": \"STARTING\" }, \"streamingResourceSetting\": { \"basicResourceSetting\": { \"jobmanagerResourceSettingSpec\": { \"cpu\": 1.0, \"memory\": \"4Gi\" }, \"parallelism\": 1, \"taskmanagerResourceSettingSpec\": { \"cpu\": 1.0, \"memory\": \"4Gi\" } }, \"resourceSettingMode\": \"BASIC\" }, \"userFlinkConf\": { \"execution.checkpointing.interval\": \"180 s\", \"table.exec.state.ttl\": \"36 h\", \"restart-strategy.fixed-delay.delay\ ": \"10 s\", \"restart-strategy\": \"fixed-delay\", \"restart-strategy.fixed-d elay.attempts\": \"214748****\", \"execution.checkpointing.min-pause\": \"180s\" } }",
 "success":true,
 "requestId":"CBC799F0-AS7S-1D30-8A4F-882ED4DD****",
 "errorMessage":"",
 "errorCode":"",
 "httpCode":200
}
```

`XML` 格式

```xml
<data>{
    &quot;artifact&quot;: {
      &quot;kind&quot;: &quot;SQLSCRIPT&quot;,
      &quot;sqlArtifact&quot;: {
        &quot;sqlScript&quot;: &quot;CREATE TEMPORARY TABLE `datahub_table` (strname VAR
CHAR)with ( &#x27;connector&#x27; = &#x27;datagen&#x27; );CREATE TEMPORARY TABLE `kafka_table` (strname VARCHAR, lens BIGINT)with ( &#x27;connector&#x27; = &#x27;print&#x27; );INSERT INTO kafka_tableSELECT SUBSTRING (strname, 0, 10) AS strname, CAST (CHAR_LENGTH (strname) AS BIGINT) AS lensFROM datahub_table;&quot;
      }
    },
    &quot;creator&quot;: &quot;20877848297****&quot;,
    &quot;creatorName&quot;: &quot;flinkadmin&quot;,
    &quot;deploymentId&quot;: &quot;b74e0fc1-914b-4009-b11c-52e6278****&quot;,
    &quot;deploymentName&quot;: &quot;sqlJob&quot;,
&quot;engineVersion&quot;:&quot;vvr-807-flink-117&quot;,
```

实时计算（流计算） 参考

```
    &quot;engineVersion&quot;: &quot;vvr8.0.7flink1.17&quot;,
    &quot;executionMode&quot;: &quot;STREAMING&quot;,
    &quot;flinkConf&quot;: {
      &quot;table.exec.operator-name.max-length&quot;: &quot;10240&quot;,
      &quot;env.java.opts.jobmanager&quot;: &quot;-Xloggc:/opt/flink/log/jobmanager-gc.l
og -XX:+UseGCLogFileRotation -XX:NumberOfGCLogFiles=2 -XX:GCLogFileSize=50M&quot;,
      &quot;***&quot;:&quot;***&quot;
      },
    &quot;jobId&quot;: &quot;003fbc67-1c8c-4147-9bf4-19da2****7&quot;,
    &quot;logging&quot;: {
      &quot;log4j2ConfigurationTemplate&quot;: &quot;&lt;?xml version=\&quot;1.0\&quot;
encoding=\&quot;UTF-8\&quot; ****&quot;,
      &quot;log4jLoggers&quot;: [
        {
          &quot;loggerLevel&quot;: &quot;INFO&quot;,
          &quot;loggerName&quot;: &quot;&quot;
        }
```

`],`

```
      &quot;logReservePolicy&quot;: {
        &quot;expirationDays&quot;: 7,
        &quot;openHistory&quot;: true
      }
    },
    &quot;modifier&quot;: &quot;208778482972****&quot;,
    &quot;modifierName&quot;: &quot;flinkadmin&quot;,
    &quot;namespace&quot;: &quot;flinkteam&quot;,
    &quot;restoreStrategy&quot;: {
      &quot;kind&quot;: &quot;NONE&quot;
    },
    &quot;startTime&quot;: 1783059223,
    &quot;status&quot;: {
      &quot;currentJobStatus&quot;: &quot;STARTING&quot;
    },
    &quot;streamingResourceSetting&quot;: {
      &quot;basicResourceSetting&quot;: {
        &quot;jobmanagerResourceSettingSpec&quot;: {
          &quot;cpu&quot;: 1.0,
          &quot;memory&quot;: &quot;4Gi&quot;
        },
        &quot;parallelism&quot;: 1,
        &quot;taskmanagerResourceSettingSpec&quot;: {
          &quot;cpu&quot;: 1.0,
          &quot;memory&quot;: &quot;4Gi&quot;
        }
      },
      &quot;resourceSettingMode&quot;: &quot;BASIC&quot;
    },
    &quot;userFlinkConf&quot;: {
      &quot;execution.checkpointing.interval&quot;: &quot;180s&quot;,
      &quot;table.exec.state.ttl&quot;: &quot;36 h&quot;,
      &quot;restart-strategy.fixed-delay.delay&quot;: &quot;10 s&quot;,
      &quot;restart-strategy&quot;: &quot;fixed-delay&quot;,
      &quot;restart-strategy.fixed-delay.attempts&quot;: &quot;214748****&quot;,
      &quot;execution.checkpointing.min-pause&quot;: &quot;180s&quot;
    }
```

实时计算（流计算） 参考

```xml
  }</data>
 <success>true</success>
 <requestId>CBC799F0-AS7S-1D30-8A4F-882ED4DD****</requestId>
 <errorMessage  />
 <errorCode  />
 <httpCode>200</httpCode>
```

###### StartJob

启动作业实例。

**请求头**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| workspace | String | Header | 是 | a14bd5d90a**** | 工作空间ID。 |

**请求语法**

```
POST /api/v2/namespaces/[namespace]/jobs HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| namespac e | String | Path | 是 | default-namespace | 项目空间名称。 |

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|

实时计算（流计算） 参考

|  |  | 参数名称 |  | 类型 |  |  | 位置 |  | 是否必选 |  | 示例 |  | 说明 |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  |  |  | {'deployme |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  | {'deployme |  |  |
|  |  |  |  |  |  |  |  |  |  |  | ntId':'7e3f3 |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  | e05-337a- |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  | 47a0-b944- |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  | b41e3****',' |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  | resourceSett |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  | ingSpec': |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  | {'streamingR |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  | esourceSetti |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  | ng': |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  | {'basicResou |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  | rceSetting': |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  | {'jobmanager |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  | ResourceSett |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  | ingSpec': |  |  |  |
|  |  | body |  | string |  |  | wholebody |  | 是 |  | {'cpu':'1.0' |  | 启动实例参数。 |  |
|  |  |  |  |  |  |  |  |  |  |  | ,'memory':'4 |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  | Gi'},'parall |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  | elism':1,'ta |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  | skmanagerRes |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  | ourceSetting |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  | Spec': |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  | {'cpu':'1.0' |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  | ,'memory':'4 |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  | Gi'}},'resou |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  | rceSettingMo |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  | de':'BASIC'} |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  | },'restoreSt |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  | rategy': |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  | {'kind':'NON |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  | E'}} |  |  |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| success | Boolean | true | 请求是否成功。 |
| requestId | String | CBC799F0-AS7S- 1D30-8A4F- 882ED4DD**** | 请求ID。 |
|  |  | { "artifact": { "kind": "SQLSCRIPT", "sqlArtifact": { "sqlScript": "CREATE TEMPORARY TABLE `datahub table` _ (strname VARCHAR) with ( |  |

| 实时计算（流计算） |  |  | Flink存算分离版开发指南·OpenAP 参考 |
|---|---|---|---|
| 参数名称 | 类型 | 'connector' = 示例 'datagen' | 说明 |
| data | String | ); CREATE TEMPORARY TABLE `kafka table` _ (strname VARCHAR, lens BIGINT) with ( 'connector' = 'print' ); INSERT INTO kafka table _ SELECT SUBSTRING (strname, 0, 10) AS strname, CAST (CHAR LENGTH _ (strname) AS BIGINT) AS lens FROM datahub table; _ " } }, "creator": "208778482972*** *", "creatorName": "flinkadmin", "deploymentId": "f9d616ef-4422- 42b5-b95c- f691d****5", "deploymentName" : "sqlJob", "engineVersion": "vvr-8.0.7-flink- 1.17", "executionMode": "STREAMING", "flinkConf": { "table.exec.operato r-name.max- length": "10240", "env.java.opts.job manager": "- Xloggc:/opt/flink/lo g/jobmanager- gc.log - XX:+UseGCLogFile Rotation - XX:NumberOfGCLo gFiles=2 - XX:GCLogFileSize= 50M", "***":"***" }, "jobId": "fa1b89ca- 908b-4cd5-b5b1- bb0ac****", "logging": { "log4j2Configuratio nTemplate": " | 当success为false，返回空值。 当success为true，返回详细数据。 |
| errorCode | String | "" | 当success为false时，该值不为空，表示业务错误码。 当success为true时，该值为空。 |

| F | link存算分离版开发参考 | 指南·OpenAPI |  | 实时计算（流计算） |  |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| errorMessage | String | "" | 当success为false，返回业务错误信息。 当success为true，返回空值。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```json
POST /api/v2/namespaces/[namespace]/jobs HTTP/1.1 { "namespace":"default-namespace", "body":"{'deploymentId':'7e3f3e05-337a-47a0-b944-b41e****','resourceSettingSpec': {'streamingResourceSetting':{'basicResourceSetting':{'jobmanagerResourceSettingSpec': {'cpu':'1.0','memory':'4Gi'},'parallelism':1,'taskmanagerResourceSettingSpec': {'cpu':'1.0','memory':'4Gi'}},'resourceSettingMode':'BASIC'}},'restoreStrategy': {'kind':'NONE'}}" }
```

正常返回示例 `JSON` 格式实时计算（流计算） 参考

```json
{
 "data":"{    \"artifact\": {      \"kind\": \"SQLSCRIPT\",      \"sqlArtifact\": {
\"sqlScript\": \"CREATE TEMPORARY TABLE `datahub_table` (strname VARCHAR)\with (\ 'co nnector' = 'datagen'\ );\\CREATE TEMPORARY TABLE `kafka_table` (strname VARCHAR, lens BIGINT)\with (\ 'connector' = 'print'\ );\\INSERT INTO kafka_table\SELECT SUBSTRING (strname, 0, 10) AS strname, CAST (CHAR_LENGTH (strname) AS BIGINT) AS lens\FROM\ datahub_table;\\" } }, \"creator\": \"208778482972****\", \"creatorName\": \"flinkadmin\", \"deploymentId\": \"f9d616ef-4422-42b5-b95c-f691d****5\", \"deploy mentName\": \"sqlJob\", \"engineVersion\": \"vvr-8.0.7-flink-1.17\", \"executionMo de\": \"STREAMING\", \"flinkConf\": { \"table.exec.operator-name.max-length\": \ "10240\", \"env.java.opts.jobmanager\": \"-Xloggc:/opt/flink/log/jobmanager-gc.log -XX:+UseGCLogFileRotation -XX:NumberOfGCLogFiles=2 -XX:GCLogFileSize=50M\", \"***\" :\"***\" }, \"jobId\": \"fa1b89ca-908b-4cd5-b5b1-bb0ac****\", \"logging\": { \"log4j2ConfigurationTemplate\": \"<?xml version=\\\"1.0\\\" encoding=\\\"UTF-8\\\"
****\\",      \"log4jLoggers\": [        {          \"loggerLevel\": \"INFO\",          \
"loggerName\": \"\" } ], \"logReservePolicy\": { \"expirationDays\": 7, \"openHistory\": true } }, \"modifier\": \"208778482972****\", \"modifierName\": \"flinkadmin\", \"namespace\": \"flinkteam \", \"restoreStrategy\": { \"kind\": \"NONE\" }, \"startTime\": 1783051000, \"status\": { \"currentJobStatus\": \"STARTING\" }, \"streamingResourceSetting\": { \"basicResourceSetting\": { \"jobmanagerResourceSettingSpec\": { \"cpu\": 1.0, \"memory\": \"4Gi\" }, \"parallelism\": 1, \"taskmanagerResourceSettingSpec\": { \"cpu\": 1.0, \"memory\": \"4Gi\" } }, \"resourceSettingMode\": \"BASIC\" }, \"userFlinkConf\": { \"execution.checkpointing.interval\": \"180 s\", \"table.exec.state.ttl\": \"36 h\", \"restart-strategy.fixed-delay.delay\ ": \"10 s\", \"restart-strategy\": \"fixed-delay\", \"restart-strategy.fixed-d elay.attempts\": \"214748****\", \"execution.checkpointing.min-pause\": \"180s\" } }",
 "success":true,
 "requestId":"CBC799F0-AS7S-1D30-8A4F-882ED4DD****",
 "errorMessage":"",
 "errorCode":"",
 "httpCode":200
}
```

`XML` 格式

```xml
<data>{
    &quot;artifact&quot;: {
      &quot;kind&quot;: &quot;SQLSCRIPT&quot;,
      &quot;sqlArtifact&quot;: {
        &quot;sqlScript&quot;: &quot;CREATE TEMPORARY TABLE `datahub_table` (strname VAR
CHAR)with ( &#x27;connector&#x27; = &#x27;datagen&#x27; );CREATE TEMPORARY TABLE `kafka_table` (strname VARCHAR, lens BIGINT)with ( &#x27;connector&#x27; = &#x27;print&#x27; );INSERT INTO kafka_tableSELECT SUBSTRING (strname, 0, 10) AS strname, CAST (CHAR_LENGTH (strname) AS BIGINT) AS lensFROM datahub_table;&quot;
      }
    },
    &quot;creator&quot;: &quot;208778482972****&quot;,
    &quot;creatorName&quot;: &quot;flinkadmin&quot;,
    &quot;deploymentId&quot;: &quot;f9d616ef-4422-42b5-b95c-f691d****5&quot;,
    &quot;deploymentName&quot;: &quot;sqlJob&quot;,
&quot;engineVersion&quot;:&quot;vvr-807-flink-117&quot;,
```

实时计算（流计算） 参考

```
    &quot;engineVersion&quot;: &quot;vvr8.0.7flink1.17&quot;,
    &quot;executionMode&quot;: &quot;STREAMING&quot;,
    &quot;flinkConf&quot;: {
      &quot;table.exec.operator-name.max-length&quot;: &quot;10240&quot;,
      &quot;env.java.opts.jobmanager&quot;: &quot;-Xloggc:/opt/flink/log/jobmanager-gc.l
og -XX:+UseGCLogFileRotation -XX:NumberOfGCLogFiles=2 -XX:GCLogFileSize=50M&quot;,
      &quot;***&quot;:&quot;***&quot;
      },
    &quot;jobId&quot;: &quot;fa1b89ca-908b-4cd5-b5b1-bb0ac****&quot;,
    &quot;logging&quot;: {
      &quot;log4j2ConfigurationTemplate&quot;: &quot;&lt;?xml version=\&quot;1.0\&quot;
encoding=\&quot;UTF-8\&quot; ****&quot;,
      &quot;log4jLoggers&quot;: [
        {
          &quot;loggerLevel&quot;: &quot;INFO&quot;,
          &quot;loggerName&quot;: &quot;&quot;
        }
```

`],`

```
      &quot;logReservePolicy&quot;: {
        &quot;expirationDays&quot;: 7,
        &quot;openHistory&quot;: true
      }
    },
    &quot;modifier&quot;: &quot;208778482972****&quot;,
    &quot;modifierName&quot;: &quot;flinkadmin&quot;,
    &quot;namespace&quot;: &quot;flinkteam&quot;,
    &quot;restoreStrategy&quot;: {
      &quot;kind&quot;: &quot;NONE&quot;
    },
    &quot;startTime&quot;: 1783051000,
    &quot;status&quot;: {
      &quot;currentJobStatus&quot;: &quot;STARTING&quot;
    },
    &quot;streamingResourceSetting&quot;: {
      &quot;basicResourceSetting&quot;: {
        &quot;jobmanagerResourceSettingSpec&quot;: {
          &quot;cpu&quot;: 1.0,
          &quot;memory&quot;: &quot;4Gi&quot;
        },
        &quot;parallelism&quot;: 1,
        &quot;taskmanagerResourceSettingSpec&quot;: {
          &quot;cpu&quot;: 1.0,
          &quot;memory&quot;: &quot;4Gi&quot;
        }
      },
      &quot;resourceSettingMode&quot;: &quot;BASIC&quot;
    },
    &quot;userFlinkConf&quot;: {
      &quot;execution.checkpointing.interval&quot;: &quot;180s&quot;,
      &quot;table.exec.state.ttl&quot;: &quot;36 h&quot;,
      &quot;restart-strategy.fixed-delay.delay&quot;: &quot;10 s&quot;,
      &quot;restart-strategy&quot;: &quot;fixed-delay&quot;,
      &quot;restart-strategy.fixed-delay.attempts&quot;: &quot;214748****&quot;,
      &quot;execution.checkpointing.min-pause&quot;: &quot;180s&quot;
    }
```

实时计算（流计算） 参考

```xml
  }</data>
 <success>true</success>
 <requestId>CBC799F0-AS7S-1D30-8A4F-882ED4DD****</requestId>
 <errorMessage  />
 <errorCode  />
 <httpCode>200</httpCode>
```

###### ListSavepoints

获取作业快照及最近系统检查点列表。

**请求头**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| workspace | String | Header | 是 | a14bd5d90a**** | 工作空间ID。 |

**请求语法**

```
GET /api/v2/namespaces/[namespace]/savepoints HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| namespac e | String | Path | 是 | default-namespace | 项目空间名称。 |
| deployme ntId | String | Query | 否 | d0b3abf0-4bfe-46b1- a324-5b7de**** | 作业ID。 |
| jobId | String | Query | 否 | 5af678c0-7db0-4650- 94c2-d2604f0a**** | 实例 ID。 |
| pageSize | Integ er | Query | 否 | 10 | 分页参数，表示所请求页码元素数量，最大值为 100， 最小值为 1，默认值为 10。 |
| pageIndex | Integ er | Query | 否 | 1 | 分页参数，页码索引，表示所请求页码，最小值为 1， 默认值为 1。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| success | Boolean | true | 请求是否成功。 |

实时计算（流计算） 参考

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | String | CBC799F0-AS7S- 1D30-8A4F- 882ED4DD**** | 请求ID。 |
| data | String | [ { "createdAt": 17830****, "deploymentId": "f9d616ef-4422- 42b5-b95c- f691d4****", "description": "", "jobId": "fa1b89ca- 908b-4cd5-b5b1- bb0ac74****", "modifiedAt": 178305****, "namespace": "flinkteam", "nativeFormat": false, "savepointId": "f1702682-c180- 4799-954a- e3217****", "savepointLocation ": "oss://flink- fullymanaged- ttor1krb1mjo85/flin k- savepoints/namesp aces/flinkteam/depl oyments/f9d616ef- ****", "savepointOrigin": "USER REQUEST", _ "status": { "state": "STARTED" }, "stopWithDrainEna bled": false } ] | 当success为false，返回空值。 当success为true，返回详细数据。 |
| errorCode | String | "" | 当success为false时，该值不为空，表示业务错误码。 当success为true时，该值为空。 |
| errorMessage | String | "" | 当success为false，返回业务错误信息。 当success为true，返回空值。 |
| httpCode | Integer | 200 | HTTP状态码。 |
| totalSize | Integer | 1 | 总条数。 |
| pageIndex | Integer | 1 | 分页参数，页码索引，表示所请求页码。 |
| pageSize | Integer | 10 | 分页参数，表示所请求页码元素数量。 |

实时计算（流计算） 参考

**示例**

请求示例

```
GET /api/v2/namespaces/[namespace]/savepoints HTTP/1.1 &namespace=default-namespace
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "totalSize":1,
 "data":"[    {      \"createdAt\": 17830****,      \"deploymentId\": \"f9d616ef-4422-42
b5-b95c-f691d4****\", \"description\": \"\", \"jobId\": \"fa1b89ca-908b-4cd5-b 5b1-bb0ac74****\", \"modifiedAt\": 178305****, \"namespace\": \"flinkteam\", \"nativeFormat\": false, \"savepointId\": \"f1702682-c180-4799-954a-e3217****\", \"savepointLocation\": \"oss://flink-fullymanaged-ttor1krb1mjo85/flinksavepoints/namespaces/flinkteam/deployments/f9d616ef-****\", \"savepointOrigin\": \ "USER_REQUEST\", \"status\": { \"state\": \"STARTED\" }, \"stopWithDrainEnabled\": false } ]",
 "pageIndex":1,
 "success":true,
 "requestId":"CBC799F0-AS7S-1D30-8A4F-882ED4DD****",
 "errorMessage":"",
 "errorCode":"",
 "pageSize":10,
 "httpCode":200
}
```

`XML` 格式实时计算（流计算） 参考

```xml
<totalSize>1</totalSize> <data>[
    {
      &quot;createdAt&quot;: 17830****,
      &quot;deploymentId&quot;: &quot;f9d616ef-4422-42b5-b95c-f691d4****&quot;,
      &quot;description&quot;: &quot;&quot;,
      &quot;jobId&quot;: &quot;fa1b89ca-908b-4cd5-b5b1-bb0ac74****&quot;,
      &quot;modifiedAt&quot;: 178305****,
      &quot;namespace&quot;: &quot;flinkteam&quot;,
      &quot;nativeFormat&quot;: false,
      &quot;savepointId&quot;: &quot;f1702682-c180-4799-954a-e3217****&quot;,
      &quot;savepointLocation&quot;: &quot;oss://flink-fullymanaged-
ttor1krb1mjo85/flink-savepoints/namespaces/flinkteam/deployments/f9d616ef-****&quot;,
      &quot;savepointOrigin&quot;: &quot;USER_REQUEST&quot;,
      &quot;status&quot;: {
        &quot;state&quot;: &quot;STARTED&quot;
      },
      &quot;stopWithDrainEnabled&quot;: false
    }
  ]</data>
 <pageIndex>1</pageIndex>
 <success>true</success>
 <requestId>CBC799F0-AS7S-1D30-8A4F-882ED4DD****</requestId>
 <errorMessage  />
 <errorCode  />
 <pageSize>10</pageSize>
 <httpCode>200</httpCode>
```

###### ListJobs

获取到某个已部署作业下所有作业实例的信息。

**请求头**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| workspace | String | Header | 是 | a14bd5d90a**** | 工作空间ID。 |

**请求语法**

```
GET /api/v2/namespaces/[namespace]/jobs HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| namespac e | String | Path | 是 | default-namespace | 项目空间名称。 |

实时计算（流计算） 参考

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| pageIndex | Integ er | Query | 否 | 1 | 分页参数，页码索引，表示所请求页码，最小值为 1， 默认值为 1。 |
| pageSize | Integ er | Query | 否 | 10 | 分页参数，表示所请求页码元素数量，最大值为 100， 最小值为 1，默认值为 10。 |
| deployme ntId | String | Query | 是 | d0b3abf0-4bfe-46b1- a324-5b7d**** | 作业ID。 |
| sortName | String | Query | 否 | gmt create _ | 排序规则。 枚举值: gmt create(创建时间) _ job id(Job ID) _ status(状态) |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| success | Boolean | true | 请求是否成功。 |
| requestId | String | CBC799F0-AS7S- 1D30-8A4F- 882ED4DD**** | 请求ID。 |

实时计算（流计算） 参考

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| data | String | [ { "artifact": { "kind": "SQLSCRIPT" }, "creator": "20877848297**** ", "creatorName": "flinkadmin", "deploymentId": "91cf243c-7a10- 4728-ba77- c22313****", "deploymentName" : "sqlJob", "engineVersion": "vvr-8.0.7-flink- 1.17", "executionMode": "STREAMING", "jobId": "4f86148c- fc32-40df-9047- b9f418****", "metric": { "totalCpu": 2.0, "totalMemoryByte": 858993**** }, "modifier": "208778482972*** *", "modifierName": "flinkadmin", "namespace": "flinkteam", "restoreStrategy": { "kind": "NONE" }, "startTime": 178330****, "status": { "currentJobStatus": "RUNNING", "running": { "observedFlinkJobR estarts": 0, "observedFlinkJobS tatus": "RUNNING" } }, "streamingResourc eSetting": { "basicResourceSett ing": { "jobmanagerResou rceSettingSpec": { "cpu": 1.0, "memory": "4Gi" }, "parallelism": 1, "taskmanagerReso urceSettingSpec": { "cpu": 1.0, "memory": "4Gi" } }, "resourceSettingMo de": "BASIC" } } ] | 当success为false，返回空值。 当success为true，返回详细数据。 |

实时计算（流计算） 参考

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| errorCode | String | "" | 当success为false时，该值不为空，表示业务错误码。 当success为true时，该值为空。 |
| errorMessage | String | "" | 当success为false，返回业务错误信息。 当success为true，返回空值。 |
| httpCode | Integer | 200 | HTTP状态码。 |
| totalSize | Integer | 1 | 总条数。 |
| pageIndex | Integer | 1 | 分页参数，页码索引，表示所请求页码。 |
| pageSize | Integer | 10 | 分页参数，表示所请求页码元素数量。 |

**示例**

请求示例

```
GET /api/v2/namespaces/[namespace]/jobs HTTP/1.1 &namespace=default-namespace &deploymentId=d0b3abf0-4bfe-46b1-a324-5b7d****
```

&公共请求参数正常返回示例 `JSON` 格式实时计算（流计算） 参考

```json
{
 "totalSize":1,
 "data":"[    {      \"artifact\": {        \"kind\": \"SQLSCRIPT\"      },      \"creato
r\": \"20877848297****\", \"creatorName\": \"flinkadmin\", \"deploymentId\": \ "91cf243c-7a10-4728-ba77-c22313****\", \"deploymentName\": \"sqlJob\", \"engin eVersion\": \"vvr-8.0.7-flink-1.17\", \"executionMode\": \"STREAMING\", \"jobI d\": \"4f86148c-fc32-40df-9047-b9f418****\", \"metric\": { \"totalCpu\": 2.0 , \"totalMemoryByte\": 858993**** }, \"modifier\": \"208778482972****\", \"modifierName\": \"flinkadmin\", \"namespace\": \"flink team\", \"restoreStrategy\": { \"kind\": \"NONE\" }, \"startTime\": 178330****, \"status\": { \"currentJobStatus\": \"RUNNING\", \"running\": { \"observedFlinkJobRestarts\": 0, \"observedFlinkJobStatus\": \"RUNNING\" } }, \"streamingResourceSetting\": { \"basicResourceSetting\": { \"jobmanagerResourceSettingSpec\": { \"cpu\": 1.0, \"memory\": \"4Gi\" }, \"parallelism\": 1, \"taskmanagerResourceSettingSpec\": { \"cpu\": 1.0, \"memory\": \" 4Gi\" } }, \"resourceSettingMode\": \"BASIC\" } } ]",
 "pageIndex":1,
 "success":true,
 "requestId":"CBC799F0-AS7S-1D30-8A4F-882ED4DD****",
 "errorMessage":"",
 "errorCode":"",
 "pageSize":10,
 "httpCode":200
}
```

`XML` 格式

```xml
<totalSize>1</totalSize> <data>[
    {
      &quot;artifact&quot;: {
        &quot;kind&quot;: &quot;SQLSCRIPT&quot;
      },
      &quot;creator&quot;: &quot;20877848297****&quot;,
      &quot;creatorName&quot;: &quot;flinkadmin&quot;,
      &quot;deploymentId&quot;: &quot;91cf243c-7a10-4728-ba77-c22313****&quot;,
      &quot;deploymentName&quot;: &quot;sqlJob&quot;,
      &quot;engineVersion&quot;: &quot;vvr-8.0.7-flink-1.17&quot;,
      &quot;executionMode&quot;: &quot;STREAMING&quot;,
      &quot;jobId&quot;: &quot;4f86148c-fc32-40df-9047-b9f418****&quot;,
      &quot;metric&quot;: {
        &quot;totalCpu&quot;: 2.0,
        &quot;totalMemoryByte&quot;: 858993****
      },
      &quot;modifier&quot;: &quot;208778482972****&quot;,
      &quot;modifierName&quot;: &quot;flinkadmin&quot;,
      &quot;namespace&quot;: &quot;flinkteam&quot;,
      &quot;restoreStrategy&quot;: {
        &quot;kind&quot;: &quot;NONE&quot;
      },
      &quot;startTime&quot;: 178330****,
&quot;status&quot;:{
```

实时计算（流计算） 参考

```xml
      &quot;status&quot;: {
        &quot;currentJobStatus&quot;: &quot;RUNNING&quot;,
        &quot;running&quot;: {
          &quot;observedFlinkJobRestarts&quot;: 0,
          &quot;observedFlinkJobStatus&quot;: &quot;RUNNING&quot;
        }
      },
      &quot;streamingResourceSetting&quot;: {
        &quot;basicResourceSetting&quot;: {
          &quot;jobmanagerResourceSettingSpec&quot;: {
            &quot;cpu&quot;: 1.0,
            &quot;memory&quot;: &quot;4Gi&quot;
          },
          &quot;parallelism&quot;: 1,
          &quot;taskmanagerResourceSettingSpec&quot;: {
            &quot;cpu&quot;: 1.0,
            &quot;memory&quot;: &quot;4Gi&quot;
          }
        },
        &quot;resourceSettingMode&quot;: &quot;BASIC&quot;
      }
    }
  ]</data>
 <pageIndex>1</pageIndex>
 <success>true</success>
 <requestId>CBC799F0-AS7S-1D30-8A4F-882ED4DD****</requestId>
 <errorMessage  />
 <errorCode  />
 <pageSize>10</pageSize>
 <httpCode>200</httpCode>
```

###### ListEngineVersionMetadata

获取系统支持的引擎版本列表。

**请求头**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| workspace | String | Header | 是 | a14bd5d90a**** | 工作空间ID。 |

**请求语法**

```
GET /api/v2/engine-version-meta.json HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | String | Host | 否 | cn-wulan-env188-d01 | Region ID。 |

实时计算（流计算） 参考

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| success | Boolean | true | 请求是否成功。 |
| requestId | String | CBC799F0-AS7S- 1D30-8A4F- 882ED4DD**** | 请求ID。 |
| data | String | { "defaultEngineVers ion": "vvr-11.5.0- flink-1.20", "engineVersionMet adata": [ { "engineVersion": "vvr-6.0.0-flink- 1.15", "features": { "supportNativeSav epoint": true, "useForSqlDeploym ents": true }, "status": "DEPRECATED" }, { "engineVersion": "vvr-11.5.0-flink- 1.20", "features": { "supportNativeSav epoint": true, "useForSqlDeploym ents": true }, "status": "STABLE" }, { "engineVersion": "vvr-4.0.18-flink- 1.13", "features": { "supportNativeSav epoint": true, "useForSqlDeploym ents": true }, "status": "DEPRECATED" }, { "engineVersion": "vvr-8.0.7-flink- 1.17", "features": { "supportNativeSav epoint": true, "useForSqlDeploym ents": true }, "status": "STABLE" } ] } | 当success为false，返回空值。 当success为true，返回详细数据。 |
| errorCode | String | "" | 当success为false时，该值不为空，表示业务错误码。 当success为true时，该值为空。 |
| errorMessage | String | "" | 当success为false，返回业务错误信息。 当success为true，返回空值。 |

| 实时计算（流计算） |  |  | Flink存算分离版开发指南·OpenAP |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```
GET /api/v2/engine-version-meta.json HTTP/1.1
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "data":"{    \"defaultEngineVersion\": \"vvr-11.5.0-flink-1.20\",
\"engineVersionMetadata\": [ { \"engineVersion\": \"vvr-6.0.0-flink-1.15\", \"features\": { \"supportNativeSavepoint\": true, \"useForSqlDeployments\": true }, \"status\": \"DEPRECATED\" }, { \"engineVersion\": \"vvr-11.5.0-flink-1.20\", \"features\": { \" supportNativeSavepoint\": true, \"useForSqlDeployments\": true }, \"status\": \"STABLE\" }, { \"engineVersion\": \"vvr-4.0.18-flink- 1.13\", \"features\": { \"supportNativeSavepoint\": true, \"useF orSqlDeployments\": true }, \"status\": \"DEPRECATED\" }, { \"engineVersion\": \"vvr-8.0.7-flink-1.17\", \"features\": { \"supportNativeSavepoint\": true, \"useForSqlDeployments\": true }, \"status\": \"STABLE\" } ] }",
 "success":true,
 "requestId":"CBC799F0-AS7S-1D30-8A4F-882ED4DD****",
 "errorMessage":"",
 "errorCode":"",
 "httpCode":200
}
```

`XML` 格式实时计算（流计算） 参考

```xml
<data>{
    &quot;defaultEngineVersion&quot;: &quot;vvr-11.5.0-flink-1.20&quot;,
    &quot;engineVersionMetadata&quot;: [
      {
        &quot;engineVersion&quot;: &quot;vvr-6.0.0-flink-1.15&quot;,
        &quot;features&quot;: {
          &quot;supportNativeSavepoint&quot;: true,
          &quot;useForSqlDeployments&quot;: true
        },
        &quot;status&quot;: &quot;DEPRECATED&quot;
      },
      {
        &quot;engineVersion&quot;: &quot;vvr-11.5.0-flink-1.20&quot;,
        &quot;features&quot;: {
          &quot;supportNativeSavepoint&quot;: true,
          &quot;useForSqlDeployments&quot;: true
        },
        &quot;status&quot;: &quot;STABLE&quot;
      },
      {
        &quot;engineVersion&quot;: &quot;vvr-4.0.18-flink-1.13&quot;,
        &quot;features&quot;: {
          &quot;supportNativeSavepoint&quot;: true,
          &quot;useForSqlDeployments&quot;: true
        },
        &quot;status&quot;: &quot;DEPRECATED&quot;
      },
      {
        &quot;engineVersion&quot;: &quot;vvr-8.0.7-flink-1.17&quot;,
        &quot;features&quot;: {
          &quot;supportNativeSavepoint&quot;: true,
          &quot;useForSqlDeployments&quot;: true
        },
        &quot;status&quot;: &quot;STABLE&quot;
      }
```

]

```xml
  }</data>
 <success>true</success>
 <requestId>CBC799F0-AS7S-1D30-8A4F-882ED4DD****</requestId>
 <errorMessage  />
 <errorCode  />
 <httpCode>200</httpCode>
```

###### ListDeploymentTargets

获取作业可部署目标的列表，部署目标是session集群或者perjob集群。

**请求头**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|

实时计算（流计算） 参考

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| workspace | String | Header | 是 | a14bd5d90a**** | 工作空间ID。 |

**请求语法**

```
GET /api/v2/namespaces/[namespace]/deployment-targets HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| namespac e | String | Path | 是 | default-namespace | 项目空间名称。 |
| pageSize | Integ er | Query | 否 | 10 | 分页参数，表示所请求页码元素数量，最大值为 100， 最小值为 1，默认值为 10。 |
| pageIndex | Integ er | Query | 否 | 1 | 分页参数，页码索引，表示所请求页码，最小值为 1， 默认值为 1。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| success | Boolean | true | 请求是否成功。 |
| requestId | String | CBC799F0-AS7S- 1D30-8A4F- 882ED4DD**** | 请求ID。 |
| data | String | [ { "name": "dt- flinkteam", "namespace": "flinkteam" } ] | 当success为false，返回空值。 当success为true，返回详细数据。 |
| errorCode | String | "" | 当success为false时，该值不为空，表示业务错误码。 当success为true时，该值为空。 |
| errorMessage | String | "" | 当success为false，返回业务错误信息。 当success为true，返回空值。 |
| httpCode | Integer | 200 | HTTP状态码。 |
| totalSize | Integer | 1 | 总条数。 |

实时计算（流计算） 参考

**示例**

请求示例

```
GET /api/v2/namespaces/[namespace]/deployment-targets HTTP/1.1 &namespace=default-namespace
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "totalSize":1,
 "data":"[    {      \"name\": \"dt-flinkteam\",      \"namespace\": \"flinkteam\"    }
]",
 "success":true,
 "requestId":"CBC799F0-AS7S-1D30-8A4F-882ED4DD****",
 "errorMessage":"",
 "errorCode":"",
 "httpCode":200
}
```

`XML` 格式

```xml
<totalSize>1</totalSize> <data>[
    {
      &quot;name&quot;: &quot;dt-flinkteam&quot;,
      &quot;namespace&quot;: &quot;flinkteam&quot;
    }
  ]</data>
 <success>true</success>
 <requestId>CBC799F0-AS7S-1D30-8A4F-882ED4DD****</requestId>
 <errorMessage  />
 <errorCode  />
 <httpCode>200</httpCode>
```

###### GetSavepoint

获取快照和系统检查点的详细信息。

**请求头**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| workspace | String | Header | 是 | a14bd5d90a**** | 工作空间ID。 |

**请求语法**

```
GET /api/v2/namespaces/[namespace]/savepoints/[savepointId] HTTP/1.1
```

实时计算（流计算） 参考

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| namespac e | String | Path | 是 | default-namespace | 项目空间名称。 |
| savepointI d | String | Path | 是 | 907a8f0e-4f6c-412b- 8a5e-7d4a065b**** | Savepoint ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| success | Boolean | true | 请求是否成功。 |
| requestId | String | CBC799F0-AS7S- 1D30-8A4F- 882ED4DD**** | 请求ID。 |
| data | String | { "createdAt": 178305****, "deploymentId": "f9d616ef-4422- 42b5-b95c- f691d44****5", "description": "", "jobId": "fa1b89ca- 908b-4cd5-b5b1- bb0****4", "modifiedAt": 178****, "namespace": "flinkteam", "nativeFormat": false, "savepointId": "f1702682-c180- 4799-954a- e3217e****", "savepointLocation ": "oss://flink- fullymanaged- ttor1krb1mjo85/flin k- savepoints/namesp aces/flinkteam/depl oyments/f9d616ef- 44****", "savepointOrigin": "USER REQUEST", _ "status": { "state": "STARTED" }, "stopWithDrainEna bled": false } | 当success为false，返回空值。 当success为true，返回详细数据。 |
| errorCode | String | "" | 当success为false时，该值不为空，表示业务错误码。 当success为true时，该值为空。 |

| F | link存算分离版开发参考 | 指南·OpenAPI |  | 实时计算（流计算） |  |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| errorMessage | String | "" | 当success为false，返回业务错误信息。 当success为true，返回空值。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```
GET /api/v2/namespaces/[namespace]/savepoints/[savepointId] HTTP/1.1 &namespace=default-namespace &savepointId=907a8f0e-4f6c-412b-8a5e-7d4a065b****
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "data":"{    \"createdAt\": 178305****,    \"deploymentId\": \"f9d616ef-4422-42b5-b95c-
f691d44****5\", \"description\": \"\", \"jobId\": \"fa1b89ca-908b-4cd5-b5b1-bb0*** *4\", \"modifiedAt\": 178****, \"namespace\": \"flinkteam\", \"nativeFormat\": false, \"savepointId\": \"f1702682-c180-4799-954a-e3217e****\", \"savepointLocation\": \"oss://flink-fullymanaged-ttor1krb1mjo85/flinksavepoints/namespaces/flinkteam/deployments/f9d616ef-44****\", \"savepointOrigin\": \"USER_REQUEST\", \"status\": { \"state\": \"STARTED\" }, \"stopWithDrainEnabled\": false }",
 "success":true,
 "requestId":"CBC799F0-AS7S-1D30-8A4F-882ED4DD****",
 "errorMessage":"",
 "errorCode":"",
 "httpCode":200
}
```

`XML` 格式实时计算（流计算） 参考

```xml
<data>{
    &quot;createdAt&quot;: 178305****,
    &quot;deploymentId&quot;: &quot;f9d616ef-4422-42b5-b95c-f691d44****5&quot;,
    &quot;description&quot;: &quot;&quot;,
    &quot;jobId&quot;: &quot;fa1b89ca-908b-4cd5-b5b1-bb0****4&quot;,
    &quot;modifiedAt&quot;: 178****,
    &quot;namespace&quot;: &quot;flinkteam&quot;,
    &quot;nativeFormat&quot;: false,
    &quot;savepointId&quot;: &quot;f1702682-c180-4799-954a-e3217e****&quot;,
    &quot;savepointLocation&quot;: &quot;oss://flink-fullymanaged-ttor1krb1mjo85/flink-s
avepoints/namespaces/flinkteam/deployments/f9d616ef-44****&quot;,
    &quot;savepointOrigin&quot;: &quot;USER_REQUEST&quot;,
    &quot;status&quot;: {
      &quot;state&quot;: &quot;STARTED&quot;
    },
    &quot;stopWithDrainEnabled&quot;: false
  }</data>
 <success>true</success>
 <requestId>CBC799F0-AS7S-1D30-8A4F-882ED4DD****</requestId>
 <errorMessage  />
 <errorCode  />
 <httpCode>200</httpCode>
```

###### GetMember

查看用户授权详情。

**请求头**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| workspace | String | Header | 是 | a14bd5d90a**** | 工作空间ID。 |

**请求语法**

```
GET /gateway/v2/namespaces/[namespace]/members/[member] HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| namespac e | String | Path | 是 | default-namespace | 项目空间名称。 |
| member | String | Path | 是 | user:2424254101**** | 成员名称。格式： user:${uid}。 |

**返回数据**

实时计算（流计算） 参考

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| success | Boolean | true | 请求是否成功。 |
| requestId | String | CBC799F0-AS7S- 1D30-8A4F- 882ED4DD**** | 请求ID。 |
| data | String | { "member": "231366754****", "role": "editor" } | 当success为false，返回空值。 当success为true，返回详细数据。 |
| errorCode | String | "" | 当success为false时，该值不为空，表示业务错误码。 当success为true时，该值为空。 |
| errorMessage | String | "" | 当success为false，返回业务错误信息。 当success为true，返回空值。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```
GET /gateway/v2/namespaces/[namespace]/members/[member] HTTP/1.1 &namespace=default-namespace &member=user:2424254101****
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "data":"{    \"member\": \"231366754****\",    \"role\": \"editor\"  }",
 "success":true,
 "requestId":"CBC799F0-AS7S-1D30-8A4F-882ED4DD****",
 "errorMessage":"",
 "errorCode":"",
 "httpCode":200
}
```

`XML` 格式实时计算（流计算） 参考

```xml
<data>{
    &quot;member&quot;: &quot;231366754****&quot;,
    &quot;role&quot;: &quot;editor&quot;
  }</data>
 <success>true</success>
 <requestId>CBC799F0-AS7S-1D30-8A4F-882ED4DD****</requestId>
 <errorMessage  />
 <errorCode  />
 <httpCode>200</httpCode>
```

###### GetLatestJobStartLog

获取作业实例最新的启动日志。

**请求头**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| workspace | String | Header | 是 | a14bd5d90a**** | 工作空间ID。 |

**请求语法**

```
GET /api/v2/namespaces/[namespace]/deployments/[deploymentId]/latest_jobmanager_start_log HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| namespac e | String | Path | 是 | default-namespace | 项目空间名称。 |
| deployme ntId | String | Path | 是 | d0b3abf0-4bfe-46b1- a324-5b7de**** | 已部署作业 ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| reason | String | "" | 错误原因。 业务正常时该字段返回空值。 |
| eagleEyeTrace Id | String | 0ad40c441762830 708230897**** | 鹰眼ID。 |
| asapiSuccess | Boolean | true | 表示API调用成功，返回结果符合预期，无错误发生。 |

| link存算分离版开发参考 | 指南·OpenAPI |  | 实时计算（流计算） |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| asapiRequestI d | String | CF3A87DE-268D- 4E4B-865F- CCC911E70B1F | asapi请求ID。 |
| success | Boolean | true | 请求是否成功。 |
| requestId | String | CBC799F0-AS7S- 1D30-8A4F- 882ED4DD**** | 请求ID。 |
| data | String | seconds: [1800] end new OSSLogClient endTimeInMs: [1783059502] **** | 当success为false，返回空值。 当success为true，返回详细数据。 |
| errorCode | String | "" | 当success为false时，该值不为空，表示业务错误码。 当success为true时，该值为空。 |
| errorMessage | String | "" | 当success为false，返回业务错误信息。 当success为true，返回空值。 |
| httpCode | Integer | 200 | HTTP状态码。 |
| message | String | "" | 附加信息。 |

**示例**

请求示例

```
GET /api/v2/namespaces/[namespace]/deployments/[deploymentId]/latest_jobmanager_start_log HTTP/1.1 &namespace=default-namespace &deploymentId=d0b3abf0-4bfe-46b1-a324-5b7de****
```

&公共请求参数正常返回示例 `JSON` 格式实时计算（流计算） 参考

```json
{
 "reason":"",
 "eagleEyeTraceId":"0ad40c441762830708230897****",
 "asapiSuccess":true,
 "asapiRequestId":"CF3A87DE-268D-4E4B-865F-CCC911E70B1F",
 "data":"seconds: [1800]\end new OSSLogClient endTimeInMs:[1783059502] ****\",
 "success":true,
 "requestId":"CBC799F0-AS7S-1D30-8A4F-882ED4DD****",
 "errorMessage":"",
 "errorCode":"",
 "httpCode":200,
 "message":""
}
```

`XML` 格式

```xml
<reason /> <eagleEyeTraceId>0ad40c441762830708230897****</eagleEyeTraceId> <asapiSuccess>true</asapiSuccess> <asapiRequestId>CF3A87DE-268D-4E4B-865F-CCC911E70B1F</asapiRequestId> <data>seconds: [1800]end new OSSLogClient endTimeInMs:[1783059502] ****</data> <success>true</success> <requestId>CBC799F0-AS7S-1D30-8A4F-882ED4DD****</requestId> <errorMessage /> <errorCode /> <httpCode>200</httpCode> <message />
```

###### GetJob

获取作业实例的详细信息。

**请求头**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| workspace | String | Header | 是 | a14bd5d90a**** | 工作空间ID。 |

**请求语法**

```
GET /api/v2/namespaces/[namespace]/jobs/[jobId] HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| namespac e | String | Path | 是 | default-namespace | 项目空间名称。 |

| link |  | ·OpenAPI |  |  |  |
|---|---|---|---|---|---|

参考

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| jobId | String | Path | 是 | 5af678c0-7db0-4650- 94c2-d2604f0a**** | 作业实例ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| success | Boolean | true | 请求是否成功。 |
| requestId | String | CBC799F0-AS7S- 1D30-8A4F- 882ED4DD**** | 请求ID。 |
| data | String | { "artifact": { "kind": "SQLSCRIPT", "sqlArtifact": { "sqlScript": "CREATE TEMPORARY TABLE `datahub table` _ (strname VARCHAR) with ( 'connector' = 'datagen' ); CREATE TEMPORARY TABLE `kafka table` _ (strname VARCHAR, lens BIGINT) with ( 'connector' = 'print' ); INSERT INTO kafka table _ SELECT SUBSTRING (strname, 0, 10) AS strname, CAST (CHAR LENGTH _ (strname) AS BIGINT) AS lens FROM datahub table; _ " } }, "creator": "208778482972*** ", "creatorName": "flinkadmin", "deploymentId": "f9d616ef-4422- 42b5-b95c- f691d****", "deploymentName" : "sqlJob", "engineVersion": "vvr-8.0.7-flink- | 当success为false，返回空值。 当success为true，返回详细数据。 |

实时计算（流计算） 参考

| 参数名称 | 类型 | 1.17", 示例 "executionMode": | 说明 |
|---|---|---|---|
|  |  | "STREAMING", "flinkConf": { "table.exec.operato r-name.max- length": "10240", "env.java.opts.job manager": "- Xloggc:/opt/flink/lo g/jobmanager- gc.log - XX:+UseGCLogFile Rotation - XX:NumberOfGCLo gFiles=2 - XX:GCLogFileSize= 50M", "***":"***" }, "jobId": "fa1b89ca- 908b-4cd5-b5b1- bb0ac****", "logging": { "log4j2Configuratio nTemplate": " |  |
| errorCode | String | "" | 当success为false时，该值不为空，表示业务错误码。 当success为true时，该值为空。 |
| errorMessage | String | "" | 当success为false，返回业务错误信息。 |
|  |  |  | 当success为true，返回空值。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```
GET /api/v2/namespaces/[namespace]/jobs/[jobId] HTTP/1.1 &namespace=default-namespace &jobId=5af678c0-7db0-4650-94c2-d2604f0a****
```

&公共请求参数正常返回示例 `JSON` 格式实时计算（流计算） 参考

```json
{
 "data":"{    \"artifact\": {      \"kind\": \"SQLSCRIPT\",      \"sqlArtifact\": {
\"sqlScript\": \"CREATE TEMPORARY TABLE `datahub_table` (strname VARCHAR)\with (\ 'co nnector' = 'datagen'\ );\\CREATE TEMPORARY TABLE `kafka_table` (strname VARCHAR, lens BIGINT)\with (\ 'connector' = 'print'\ );\\INSERT INTO kafka_table\SELECT SUBSTRING (strname, 0, 10) AS strname, CAST (CHAR_LENGTH (strname) AS BIGINT) AS lens\FROM\ datahub_table;\\" } }, \"creator\": \"208778482972***\", \"creatorName\": \"flinkadmin\", \"deploymentId\": \"f9d616ef-4422-42b5-b95c-f691d****\", \"deploym entName\": \"sqlJob\", \"engineVersion\": \"vvr-8.0.7-flink-1.17\", \"executionMod e\": \"STREAMING\", \"flinkConf\": { \"table.exec.operator-name.max-length\": \" 10240\", \"env.java.opts.jobmanager\": \"-Xloggc:/opt/flink/log/jobmanager-gc.log - XX:+UseGCLogFileRotation -XX:NumberOfGCLogFiles=2 -XX:GCLogFileSize=50M\", \"***\": \"***\" }, \"jobId\": \"fa1b89ca-908b-4cd5-b5b1-bb0ac****\", \"logging\": { \"log4j2ConfigurationTemplate\": \"<?xml version=\\\"1.0\\\" ***\", \"log4jLoggers\ ": [ { \"loggerLevel\": \"INFO\", \"loggerName\": \"\" } ], \"logReservePolicy\": { \"expirationDays\": 7, \"openHistory\": tr ue } }, \"modifier\": \"20877848297****5\", \"modifierName\": \"flinkadmin\", \"namespace\": \"flinkteam\", \"restoreStrategy\": { \"kind\" : \"NONE\" }, \"startTime\": 1783051000, \"status\": { \"currentJobStatus\": \"STARTING\" }, \"streamingResourceSetting\": { \"basic ResourceSetting\": { \"jobmanagerResourceSettingSpec\": { \"cpu\": 1.0, \"memory\": \"4Gi\" }, \"parallelism\": 1, \"taskmanagerResourceSettingSpec\": { \"cpu\": 1.0, \"memory\": \"4Gi\ " } }, \"resourceSettingMode\": \"BASIC\" }, \"userFlinkConf\": { \"execution.checkpointing.interval\": \"180s\", \"table.exec.state.ttl\": \"36 h\", \"restart-strategy.fixed-delay.delay\": \"10 s\", \"restart-strategy\": \"fixed-del ay\", \"restart-strategy.fixed-delay.attempts\": \"21474****\", \"execution.checkpointing.min-pause\": \"180s\" } }",
 "success":true,
 "requestId":"CBC799F0-AS7S-1D30-8A4F-882ED4DD****",
 "errorMessage":"",
 "errorCode":"",
 "httpCode":200
}
```

`XML` 格式

```xml
<data>{
    &quot;artifact&quot;: {
      &quot;kind&quot;: &quot;SQLSCRIPT&quot;,
      &quot;sqlArtifact&quot;: {
        &quot;sqlScript&quot;: &quot;CREATE TEMPORARY TABLE `datahub_table` (strname VAR
CHAR)with ( &#x27;connector&#x27; = &#x27;datagen&#x27; );CREATE TEMPORARY TABLE `kafka_table` (strname VARCHAR, lens BIGINT)with ( &#x27;connector&#x27; = &#x27;print&#x27; );INSERT INTO kafka_tableSELECT SUBSTRING (strname, 0, 10) AS strname, CAST (CHAR_LENGTH (strname) AS BIGINT) AS lensFROM datahub_table;&quot;
      }
    },
    &quot;creator&quot;: &quot;208778482972***&quot;,
    &quot;creatorName&quot;: &quot;flinkadmin&quot;,
    &quot;deploymentId&quot;: &quot;f9d616ef-4422-42b5-b95c-f691d****&quot;,
    &quot;deploymentName&quot;: &quot;sqlJob&quot;,
    &quot;engineVersion&quot;: &quot;vvr-8.0.7-flink-1.17&quot;,
&quot;executionMode&quot;:&quot;STREAMING&quot;,
```

实时计算（流计算） 参考

```
    &quot;executionMode&quot;: &quot;STREAMING&quot;,
    &quot;flinkConf&quot;: {
      &quot;table.exec.operator-name.max-length&quot;: &quot;10240&quot;,
      &quot;env.java.opts.jobmanager&quot;: &quot;-Xloggc:/opt/flink/log/jobmanager-gc.l
og -XX:+UseGCLogFileRotation -XX:NumberOfGCLogFiles=2 -XX:GCLogFileSize=50M&quot;,
      &quot;***&quot;:&quot;***&quot;
    },
    &quot;jobId&quot;: &quot;fa1b89ca-908b-4cd5-b5b1-bb0ac****&quot;,
    &quot;logging&quot;: {
      &quot;log4j2ConfigurationTemplate&quot;: &quot;&lt;?xml version=\&quot;1.0\&quot;
***&quot;,
      &quot;log4jLoggers&quot;: [
        {
          &quot;loggerLevel&quot;: &quot;INFO&quot;,
          &quot;loggerName&quot;: &quot;&quot;
        }
```

`],`

```
      &quot;logReservePolicy&quot;: {
        &quot;expirationDays&quot;: 7,
        &quot;openHistory&quot;: true
      }
    },
    &quot;modifier&quot;: &quot;20877848297****5&quot;,
    &quot;modifierName&quot;: &quot;flinkadmin&quot;,
    &quot;namespace&quot;: &quot;flinkteam&quot;,
    &quot;restoreStrategy&quot;: {
      &quot;kind&quot;: &quot;NONE&quot;
    },
    &quot;startTime&quot;: 1783051000,
    &quot;status&quot;: {
      &quot;currentJobStatus&quot;: &quot;STARTING&quot;
    },
    &quot;streamingResourceSetting&quot;: {
      &quot;basicResourceSetting&quot;: {
        &quot;jobmanagerResourceSettingSpec&quot;: {
          &quot;cpu&quot;: 1.0,
          &quot;memory&quot;: &quot;4Gi&quot;
        },
        &quot;parallelism&quot;: 1,
        &quot;taskmanagerResourceSettingSpec&quot;: {
          &quot;cpu&quot;: 1.0,
          &quot;memory&quot;: &quot;4Gi&quot;
        }
      },
      &quot;resourceSettingMode&quot;: &quot;BASIC&quot;
    },
    &quot;userFlinkConf&quot;: {
      &quot;execution.checkpointing.interval&quot;: &quot;180s&quot;,
      &quot;table.exec.state.ttl&quot;: &quot;36 h&quot;,
      &quot;restart-strategy.fixed-delay.delay&quot;: &quot;10 s&quot;,
      &quot;restart-strategy&quot;: &quot;fixed-delay&quot;,
      &quot;restart-strategy.fixed-delay.attempts&quot;: &quot;21474****&quot;,
      &quot;execution.checkpointing.min-pause&quot;: &quot;180s&quot;
    }
  }</data>
```

实时计算（流计算） 参考

```xml
 <success>true</success>
 <requestId>CBC799F0-AS7S-1D30-8A4F-882ED4DD****</requestId>
 <errorMessage  />
 <errorCode  />
 <httpCode>200</httpCode>
```

###### GetGenerateResourcePlanResult

根据异步工单ID获取异步生成细粒度资源结果。

**请求头**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| workspace | String | Header | 是 | a14bd5d90a**** | 工作空间ID。 |

**请求语法**

```
GET /api/v2/namespaces/[namespace]/deployments/tickets/[ticketId]/resourceplan:asyncGenerate HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| namespac e | String | Path | 是 | default-namespace | 项目空间名称。 |
| ticketId | String | Path | 是 | 88a8fc49-e090-430a- 85d8-3ee8c79c**** | 回执 ID，调用 GenerateResourcePlanW ithFlinkConfAsync API 获取。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| success | Boolean | true | 请求是否成功。 |
| requestId | String | CBC799F0-AS7S- 1D30-8A4F- 882ED4DD**** | 请求ID。 |

实时计算（流计算） 参考

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| data | String | { "plan": " {\"ssgProfiles\": [{\"name\":\"defaul t\",\"cpu\":0.2,\"hea p\":\"768 mb\",\"offHeap\":\" 32 mb\",\"managed\": {},\"extended\": {}}],\"nodes\": [{\"id\":1,\"type\":\" StreamExecTableS ourceScan\",\"desc\ ":\"Source: datahub table[5]\", _ \"profile\": {\"group\":\"default \",\"parallelism\":1,\ "maxParallelism\":3 2768,\"minParalleli sm\":1}}, {\"id\":2,\"type\":\" StreamExecCalc\",\ "desc\":\"Calc[6]\",\ "profile\": {\"group\":\"default \",\"parallelism\":1,\ "maxParallelism\":3 2768,\"minParalleli sm\":1}}, {\"id\":3,\"type\":\" StreamExecSink\",\ "desc\":\"Sink: kafka table[7]\",\"p _ rofile\": {\"group\":\"default \",\"parallelism\":1,\ "maxParallelism\":3 2768,\"minParalleli sm\":1}}],\"edges\" : [{\"source\":1,\"tar get\":2,\"mode\":\"P IPELINED\",\"strate gy\":\"FORWARD\"} , {\"source\":2,\"targ et\":3,\"mode\":\"PI PELINED\",\"strateg y\":\"FORWARD\"}], \"vertices\": {\"717c7b8afebbfb 7137f6****\": [1,2,3]}}", "ticketStatus": "FINISHED" } | 当success为false，返回空值。 当success为true，返回详细数据。 |
| errorCode | String | "" | 当success为false时，该值不为空，表示业务错误码。 当success为true时，该值为空。 |

| link存算分离版开发 | 指南·OpenAPI |  | 实时计算（流计算） |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| errorMessage | String | "" | 当success为false，返回业务错误信息。 当success为true，返回空值。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```
GET /api/v2/namespaces/[namespace]/deployments/tickets/[ticketId]/resourceplan:asyncGenerate HTTP/1.1 &namespace=default-namespace &ticketId=88a8fc49-e090-430a-85d8-3ee8c79c****
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "data":"{    \"plan\": \"{\\\"ssgProfiles\\\":
[{\\\"name\\\":\\\"default\\\",\\\"cpu\\\":0.2,\\\"heap\\\":\\\"768 mb\\\",\\\"offHeap\\\":\\\"32 mb\\\",\\\"managed\\\":{},\\\"extended\\\": {}}],\\\"nodes\\\": [{\\\"id\\\":1,\\\"type\\\":\\\"StreamExecTableSourceScan\\\",\\\"desc\\\":\\\"Source: datahub_table[5]\\\",\\\"profile\\\": {\\\"group\\\":\\\"default\\\",\\\"parallelism\\\":1,\\\"maxParallelism\\\":32768,\\\"minP allelism\\\":1}}, {\\\"id\\\":2,\\\"type\\\":\\\"StreamExecCalc\\\",\\\"desc\\\":\\\"Calc[6]\\\",\\\"profile \": {\\\"group\\\":\\\"default\\\",\\\"parallelism\\\":1,\\\"maxParallelism\\\":32768,\\\"minP allelism\\\":1}}, {\\\"id\\\":3,\\\"type\\\":\\\"StreamExecSink\\\",\\\"desc\\\":\\\"Sink: kafka_table[7]\\\",\\\"profile\\\": {\\\"group\\\":\\\"default\\\",\\\"parallelism\\\":1,\\\"maxParallelism\\\":32768,\\\"minP allelism\\\":1}}],\\\"edges\\\": [{\\\"source\\\":1,\\\"target\\\":2,\\\"mode\\\":\\\"PIPELINED\\\",\\\"strategy\\\":\\\"FO ARD\\\"}, {\\\"source\\\":2,\\\"target\\\":3,\\\"mode\\\":\\\"PIPELINED\\\",\\\"strategy\\\":\\\"FOR RD\\\"}],\\\"vertices\\\":{\\\"717c7b8afebbfb7137f6****\\\":[1,2,3]}}\", \"ticketStat us\": \"FINISHED\" }",
 "success":true,
 "requestId":"CBC799F0-AS7S-1D30-8A4F-882ED4DD****",
 "errorMessage":"",
 "errorCode":"",
 "httpCode":200
}
```

`XML` 格式实时计算（流计算） 参考

```xml
<data>{
    &quot;plan&quot;: &quot;{\&quot;ssgProfiles\&quot;:
[{\&quot;name\&quot;:\&quot;default\&quot;,\&quot;cpu\&quot;:0.2,\&quot;heap\&quot;:\&quot 68 mb\&quot;,\&quot;offHeap\&quot;:\&quot;32 mb\&quot;,\&quot;managed\&quot;: {},\&quot;extended\&quot;:{}}],\&quot;nodes\&quot;: [{\&quot;id\&quot;:1,\&quot;type\&quot;:\&quot;StreamExecTableSourceScan\&quot;,\&quot;des &quot;:\&quot;Source: datahub_table[5]\&quot;,\&quot;profile\&quot;: {\&quot;group\&quot;:\&quot;default\&quot;,\&quot;parallelism\&quot;:1,\&quot;maxParalleli \&quot;:32768,\&quot;minParallelism\&quot;:1}}, {\&quot;id\&quot;:2,\&quot;type\&quot;:\&quot;StreamExecCalc\&quot;,\&quot;desc\&quot;:\&q t;Calc[6]\&quot;,\&quot;profile\&quot;: {\&quot;group\&quot;:\&quot;default\&quot;,\&quot;parallelism\&quot;:1,\&quot;maxParalleli \&quot;:32768,\&quot;minParallelism\&quot;:1}}, {\&quot;id\&quot;:3,\&quot;type\&quot;:\&quot;StreamExecSink\&quot;,\&quot;desc\&quot;:\&q t;Sink: kafka_table[7]\&quot;,\&quot;profile\&quot;: {\&quot;group\&quot;:\&quot;default\&quot;,\&quot;parallelism\&quot;:1,\&quot;maxParalleli \&quot;:32768,\&quot;minParallelism\&quot;:1}}],\&quot;edges\&quot;: [{\&quot;source\&quot;:1,\&quot;target\&quot;:2,\&quot;mode\&quot;:\&quot;PIPELINED\&quot; &quot;strategy\&quot;:\&quot;FORWARD\&quot;}, {\&quot;source\&quot;:2,\&quot;target\&quot;:3,\&quot;mode\&quot;:\&quot;PIPELINED\&quot;, quot;strategy\&quot;:\&quot;FORWARD\&quot;}],\&quot;vertices\&quot;: {\&quot;717c7b8afebbfb7137f6****\&quot;:[1,2,3]}}&quot;,
    &quot;ticketStatus&quot;: &quot;FINISHED&quot;
  }</data>
 <success>true</success>
 <requestId>CBC799F0-AS7S-1D30-8A4F-882ED4DD****</requestId>
 <errorMessage  />
 <errorCode  />
 <httpCode>200</httpCode>
```

###### GetDeployment

获取已部署作业的详细信息。

**请求头**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| workspace | String | Header | 是 | a14bd5d90a**** | 工作空间ID。 |

**请求语法**

```
GET /api/v2/namespaces/[namespace]/deployments/[deploymentId] HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| namespac e | String | Path | 是 | default-namespace | 项目空间名称。 |

| F | link存算分离版参考 | 开发指南 | ·OpenAPI |  |  | 实时计算（流计算） |  |
|---|---|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| deployme ntId | String | Path | 是 | d0b3abf0-4bfe-46b1- a324-5b7d**** | 作业ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| success | Boolean | true | 请求是否成功。 |
| requestId | String | CBC799F0-AS7S- 1D30-8A4F- 882ED4DD**** | 请求ID。 |
|  |  | { "artifact": { "kind": "SQLSCRIPT", "sqlArtifact": { "sqlScript": "CREATE TEMPORARY TABLE `datahub table` _ (strname VARCHAR) with ( 'connector' = 'datagen' ); CREATE TEMPORARY TABLE `kafka table` _ (strname VARCHAR, lens BIGINT) with ( 'connector' = 'print' ); INSERT INTO kafka table _ SELECT strname, CAST (CHAR LENGTH _ (strname) AS BIGINT) AS lens FROM datahub table; _ " } }, "creator": "2087784829****", "creatorName": "flinkadmin", "deploymentHasCh anged": true, "deploymentId": "f9d616ef-4422- 42b5-b95c- f691****", "deploymentTarget ": { "mode": "PER JOB", "name": _ "dt-flinkteam" }, |  |

实时计算（流计算） 参考

| 参数名称 | 类型 | "engineVersion": 示例 "vvr-8.0.7-flink- | 说明 |
|---|---|---|---|
| data | String | 1.17", "executionMode": "STREAMING", "flinkConf": { "execution.checkpo inting.interval": "180s", "table.exec.state.ttl ": "36 h", "restart- strategy.fixed- delay.delay": "10 s", "restart- strategy": "fixed- delay", "restart- strategy.fixed- delay.attempts": "21474****", "execution.checkpo inting.min-pause": "180s" }, "jobSummary": { "cancelled": 0, "cancelling": 0, "failed": 0, "finished": 0, "running": 0, "starting": 0 }, "logging": { "log4jLoggers": [ { "loggerLevel": "INFO", | 当success为false，返回空值。 当success为true，返回详细数据。 |
|  |  | "loggerName": "" } ], "logReservePolicy": { "expirationDays": 7, "openHistory": true }, "loggingProfile": "default" }, "modifier": "208778482****", "modifierName": "flinkadmin", "name": "sqlJob", "namespace": "flinkteam", "streamingResourc eSetting": { "basicResourceSett ing": { "jobmanagerResou rceSettingSpec": { "cpu": 1.0, "memory": "4Gi" }, "parallelism": 1, "taskmanagerReso urceSettingSpec": { "cpu": 1.0, "memory": "4Gi" } }, "resourceSettingMo de": "BASIC" } } |  |

实时计算（流计算） 参考

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| errorCode | String | "" | 当success为false时，该值不为空，表示业务错误码。 当success为true时，该值为空。 |
| errorMessage | String | "" | 当success为false，返回业务错误信息。 当success为true，返回空值。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```
GET /api/v2/namespaces/[namespace]/deployments/[deploymentId] HTTP/1.1 &namespace=default-namespace &deploymentId=d0b3abf0-4bfe-46b1-a324-5b7d****
```

&公共请求参数正常返回示例 `JSON` 格式实时计算（流计算） 参考

```json
{
 "data":"{    \"artifact\": {      \"kind\": \"SQLSCRIPT\",      \"sqlArtifact\": {
\"sqlScript\": \"CREATE TEMPORARY TABLE `datahub_table` (strname VARCHAR)\with (\ 'co nnector' = 'datagen'\ );\\CREATE TEMPORARY TABLE `kafka_table` (strname VARCHAR, lens BIGINT)\with (\ 'connector' = 'print'\ );\\INSERT INTO kafka_table\SELECT strname, CAST (CHAR_LENGTH (strname) AS BIGINT) AS lens\FROM\ datahub_table;\\" } }, \"creator\": \"2087784829****\", \"creatorName\": \"flinkadmin\", \"deploymentHasC hanged\": true, \"deploymentId\": \"f9d616ef-4422-42b5-b95c-f691****\", \"deployme ntTarget\": { \"mode\": \"PER_JOB\", \"name\": \"dt-flinkteam\" }, \"engineVersion\": \"vvr-8.0.7-flink-1.17\", \"executionMode\": \"STREAMING\", \"f linkConf\": { \"execution.checkpointing.interval\": \"180s\", \"table.exec.state.ttl\": \"36 h\", \"restart-strategy.fixed-delay.delay\": \"10 s\ ", \"restart-strategy\": \"fixed-delay\", \"restart-strategy.fixed-delay.attem pts\": \"21474****\", \"execution.checkpointing.min-pause\": \"180s\" }, \"jo bSummary\": { \"cancelled\": 0, \"cancelling\": 0, \"failed\": 0, \"finished\": 0, \"running\": 0, \"starting\": 0 }, \"logging\": { \"log4jLoggers\": [ { \"loggerLevel\": \"INFO\", \"loggerName\": \"\" } ], \"logReservePolicy\": { \"expirationDays\": 7, \"openHistory\": true }, \"loggingProfile\": \"d efault\" }, \"modifier\": \"208778482****\", \"modifierName\": \"flinkadmin\", \"name\": \"sqlJob\", \"namespace\": \"flinkteam\", \"streamingResourceSetting\": { \"basicResourceSetting\": { \"jobmanagerResourceSettingSpec\": { \"cpu\": 1.0, \"memory\": \"4Gi\" }, \"parallelism\": 1, \" taskmanagerResourceSettingSpec\": { \"cpu\": 1.0, \"memory\": \"4Gi\" } }, \"resourceSettingMode\": \"BASIC\" } }",
 "success":true,
 "requestId":"CBC799F0-AS7S-1D30-8A4F-882ED4DD****",
 "errorMessage":"",
 "errorCode":"",
 "httpCode":200
}
```

`XML` 格式

```xml
<data>{
    &quot;artifact&quot;: {
      &quot;kind&quot;: &quot;SQLSCRIPT&quot;,
      &quot;sqlArtifact&quot;: {
        &quot;sqlScript&quot;: &quot;CREATE TEMPORARY TABLE `datahub_table` (strname VAR
CHAR)with ( &#x27;connector&#x27; = &#x27;datagen&#x27; );CREATE TEMPORARY TABLE `kafka_table` (strname VARCHAR, lens BIGINT)with ( &#x27;connector&#x27; = &#x27;print&#x27; );INSERT INTO kafka_tableSELECT strname, CAST (CHAR_LENGTH (strname) AS BIGINT) AS lensFROM datahub_table;&quot;
      }
    },
    &quot;creator&quot;: &quot;2087784829****&quot;,
    &quot;creatorName&quot;: &quot;flinkadmin&quot;,
    &quot;deploymentHasChanged&quot;: true,
    &quot;deploymentId&quot;: &quot;f9d616ef-4422-42b5-b95c-f691****&quot;,
    &quot;deploymentTarget&quot;: {
      &quot;mode&quot;: &quot;PER_JOB&quot;,
      &quot;name&quot;: &quot;dt-flinkteam&quot;
    },
&quot;engineVersion&quot;:&quot;vvr-807-flink-117&quot;,
```

实时计算（流计算） 参考

```
    &quot;engineVersion&quot;: &quot;vvr8.0.7flink1.17&quot;,
    &quot;executionMode&quot;: &quot;STREAMING&quot;,
    &quot;flinkConf&quot;: {
      &quot;execution.checkpointing.interval&quot;: &quot;180s&quot;,
      &quot;table.exec.state.ttl&quot;: &quot;36 h&quot;,
      &quot;restart-strategy.fixed-delay.delay&quot;: &quot;10 s&quot;,
      &quot;restart-strategy&quot;: &quot;fixed-delay&quot;,
      &quot;restart-strategy.fixed-delay.attempts&quot;: &quot;21474****&quot;,
      &quot;execution.checkpointing.min-pause&quot;: &quot;180s&quot;
    },
    &quot;jobSummary&quot;: {
      &quot;cancelled&quot;: 0,
      &quot;cancelling&quot;: 0,
      &quot;failed&quot;: 0,
      &quot;finished&quot;: 0,
      &quot;running&quot;: 0,
      &quot;starting&quot;: 0
    },
    &quot;logging&quot;: {
      &quot;log4jLoggers&quot;: [
        {
          &quot;loggerLevel&quot;: &quot;INFO&quot;,
          &quot;loggerName&quot;: &quot;&quot;
        }
```

`],`

```xml
      &quot;logReservePolicy&quot;: {
        &quot;expirationDays&quot;: 7,
        &quot;openHistory&quot;: true
      },
      &quot;loggingProfile&quot;: &quot;default&quot;
    },
    &quot;modifier&quot;: &quot;208778482****&quot;,
    &quot;modifierName&quot;: &quot;flinkadmin&quot;,
    &quot;name&quot;: &quot;sqlJob&quot;,
    &quot;namespace&quot;: &quot;flinkteam&quot;,
    &quot;streamingResourceSetting&quot;: {
      &quot;basicResourceSetting&quot;: {
        &quot;jobmanagerResourceSettingSpec&quot;: {
          &quot;cpu&quot;: 1.0,
          &quot;memory&quot;: &quot;4Gi&quot;
        },
        &quot;parallelism&quot;: 1,
        &quot;taskmanagerResourceSettingSpec&quot;: {
          &quot;cpu&quot;: 1.0,
          &quot;memory&quot;: &quot;4Gi&quot;
        }
      },
      &quot;resourceSettingMode&quot;: &quot;BASIC&quot;
    }
  }</data>
 <success>true</success>
 <requestId>CBC799F0-AS7S-1D30-8A4F-882ED4DD****</requestId>
 <errorMessage  />
 <errorCode  />
 <httpCode>200</httpCode>
```

实时计算（流计算） 参考

**3.3.1.3.17.**

###### GenerateResourcePlanWithFlinkConfAsync

提交异步生成resource plan工单，返回一个异步工单ID用于查询工单结果。

**请求头**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| workspace | String | Header | 是 | a14bd5d90a**** | 工作空间ID。 |

**请求语法**

```
POST /api/v2/namespaces/[namespace]/deployments/[deploymentId]/resourceplan:asyncGenerate HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| namespac e | String | Path | 是 | default-namespace | 项目空间名称。 |
| deployme ntId | String | Path | 是 | d0b3abf0-4bfe-46b1- a324-5**** | deploymentId，deploym ent 的唯一标识。 |

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|

实时计算（流计算） 参考

|  |  | 参数名称 |  | 类型 |  | 位置 |  | 是否必选 |  | 示例 |  | 说明 |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  |  | {'executio |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  | {'executio |  |  |
|  |  |  |  |  |  |  |  |  |  | n.checkpoint |  |  |  |
|  |  |  |  |  |  |  |  |  |  | ing.interval |  |  |  |
|  |  |  |  |  |  |  |  |  |  | ': '180s', |  |  |  |
|  |  |  |  |  |  |  |  |  |  | 'execution.c |  |  |  |
|  |  |  |  |  |  |  |  |  |  | heckpointing |  |  |  |
|  |  |  |  |  |  |  |  |  |  | .min- |  |  |  |
|  |  |  |  |  |  |  |  |  |  | pause': |  |  |  |
|  |  |  |  |  |  |  |  |  |  | '180s', |  |  |  |
|  |  |  |  |  |  |  |  |  |  | 'restart- |  |  |  |
|  |  |  |  |  |  |  |  |  |  | strategy': |  |  |  |
|  |  |  |  |  |  |  |  |  |  | 'fixed- |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  | 生成 resource |  |
|  |  |  |  |  |  |  |  |  |  | delay', |  | plan 需要的 |  |
|  |  | body |  | string |  | wholebody |  | 否 |  | 'restart- |  | Flink |  |
|  |  |  |  |  |  |  |  |  |  | strategy.fix |  | configuration |  |
|  |  |  |  |  |  |  |  |  |  | ed- |  | 。 |  |
|  |  |  |  |  |  |  |  |  |  | delay.attemp |  |  |  |
|  |  |  |  |  |  |  |  |  |  | ts': |  |  |  |
|  |  |  |  |  |  |  |  |  |  | '2147483647' |  |  |  |
|  |  |  |  |  |  |  |  |  |  | , 'restart- |  |  |  |
|  |  |  |  |  |  |  |  |  |  | strategy.fix |  |  |  |
|  |  |  |  |  |  |  |  |  |  | ed- |  |  |  |
|  |  |  |  |  |  |  |  |  |  | delay.delay' |  |  |  |
|  |  |  |  |  |  |  |  |  |  | : '10 s', |  |  |  |
|  |  |  |  |  |  |  |  |  |  | 'table.exec. |  |  |  |
|  |  |  |  |  |  |  |  |  |  | state.ttl': |  |  |  |
|  |  |  |  |  |  |  |  |  |  | '36 h'} |  |  |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| success | Boolean | true | 请求是否成功。 |
| requestId | String | CBC799F0-AS7S- 1D30-8A4F- 882ED4DD**** | 请求ID。 |
| data | String | { "ticketId": "fda9f510-a668- 4de1-9c0f-9fc****" } | 当success为false，返回空值。 当success为true，返回详细数据。 |
| errorCode | String | "" | 当success为false时，该值不为空，表示业务错误码。 当success为true时，该值为空。 |
| errorMessage | String | "" | 当success为false，返回业务错误信息。 当success为true，返回空值。 |

| 实时计算（流计算） |  |  | Flink存算分离版开发指南·OpenAP |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```json
POST /api/v2/namespaces/[namespace]/deployments/[deploymentId]/resourceplan:asyncGenerate HTTP/1.1 { "namespace":"default-namespace", "deploymentId":"d0b3abf0-4bfe-46b1-a324-5****" }
```

正常返回示例 `JSON` 格式

```json
{
 "data":"{    \"ticketId\": \"fda9f510-a668-4de1-9c0f-9fc****\"  }",
 "success":true,
 "requestId":"CBC799F0-AS7S-1D30-8A4F-882ED4DD****",
 "errorMessage":"",
 "errorCode":"",
 "httpCode":200
}
```

`XML` 格式

```xml
<data>{
    &quot;ticketId&quot;: &quot;fda9f510-a668-4de1-9c0f-9fc****&quot;
  }</data>
 <success>true</success>
 <requestId>CBC799F0-AS7S-1D30-8A4F-882ED4DD****</requestId>
 <errorMessage  />
 <errorCode  />
 <httpCode>200</httpCode>
```

###### DeleteVariable

删除变量。

**请求头**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| workspace | String | Header | 是 | a14bd5d90a**** | 工作空间ID。 |

**请求语法**

实时计算（流计算） 参考

```
DELETE /api/v2/namespaces/[namespace]/variables/[name] HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| namespac e | String | Path | 是 | default-namespace | 项目空间名称。 |
| name | String | Path | 是 | variableName | 需要删除的变量名称。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| success | Boolean | true | 请求是否成功。 |
| requestId | String | CBC799F0-AS7S- 1D30-8A4F- 882ED4DD**** | 请求ID。 |
| errorCode | String | "" | 当success为false时，该值不为空，表示业务错误码。 当success为true时，该值为空。 |
| errorMessage | String | "" | 当success为false，返回业务错误信息。 当success为true，返回空值。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```
DELETE /api/v2/namespaces/[namespace]/variables/[name] HTTP/1.1 &namespace=default-namespace &name=blinkteam
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "success":true,
 "requestId":"CBC799F0-AS7S-1D30-8A4F-882ED4DD****",
 "errorMessage":"",
 "errorCode":"",
 "httpCode":200
}
```

实时计算（流计算） 参考 `XML` 格式

```xml
<success>true</success> <requestId>CBC799F0-AS7S-1D30-8A4F-882ED4DD****</requestId> <errorMessage /> <errorCode /> <httpCode>200</httpCode>
```

###### DeleteSavepoint

删除快照。

**请求头**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| workspace | String | Header | 是 | a14bd5d90a**** | 工作空间ID。 |

**请求语法**

```
DELETE /api/v2/namespaces/[namespace]/savepoints/[savepointId] HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| namespac e | String | Path | 是 | default-namespace | 项目空间名称。 |
| savepointI d | String | Path | 是 | 907a8f0e-4f6c-412b- 8a5e-7d4a065b**** | 需要删除的Savepoint ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| success | Boolean | true | 请求是否成功。 |
| requestId | String | CBC799F0-AS7S- 1D30-8A4F- 882ED4DD**** | 请求ID。 |
| errorCode | String | "" | 当success为false时，该值不为空，表示业务错误码。 当success为true时，该值为空。 |
| errorMessage | String | "" | 当success为false，返回业务错误信息。 当success为true，返回空值。 |

| link存算分离版开发 | 指南·OpenAPI |  |  |
|---|---|---|---|

参考

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```
DELETE /api/v2/namespaces/[namespace]/savepoints/[savepointId] HTTP/1.1 &namespace=default-namespace &savepointId=907a8f0e-4f6c-412b-8a5e-7d4a065b****
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "success":true,
 "requestId":"CBC799F0-AS7S-1D30-8A4F-882ED4DD****",
 "errorMessage":"",
 "errorCode":"",
 "httpCode":200
}
```

`XML` 格式

```xml
<success>true</success> <requestId>CBC799F0-AS7S-1D30-8A4F-882ED4DD****</requestId> <errorMessage /> <errorCode /> <httpCode>200</httpCode>
```

###### DeleteMember

删除指定的用户权限信息。

**请求头**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| workspace | String | Header | 是 | a14bd5d90a**** | 工作空间ID。 |

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| namespac e | String | Path | 是 | default-namespace | 项目空间名称。 |

| 实时计算（流计 | 算） |  |  | Flink | 存算分离版开发指南·OpenAP |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| member | String | Path | 是 | user:223769*** | 成员UID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| success | Boolean | true | 请求是否成功。 |
| requestId | String | CBC799F0-AS7S- 1D30-8A4F- 882ED4DD**** | 请求ID。 |
| errorCode | String | "" | 当success为false时，该值不为空，表示业务错误码。 当success为true时，该值为空。 |
| errorMessage | String | "" | 当success为false，返回业务错误信息。 当success为true，返回空值。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```
DELETE /gateway/v2/namespaces/[namespace]/members/[member] HTTP/1.1 &namespace=default-namespace &member=user:223769***
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "success":true,
 "requestId":"CBC799F0-AS7S-1D30-8A4F-882ED4DD****",
 "errorMessage":"",
 "errorCode":"",
 "httpCode":200
}
```

`XML` 格式实时计算（流计算） 参考

```xml
<success>true</success> <requestId>CBC799F0-AS7S-1D30-8A4F-882ED4DD****</requestId> <errorMessage /> <errorCode /> <httpCode>200</httpCode>
```

###### DeleteJob

删除一个作业下非运行状态的作业实例信息。

**请求头**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| workspace | String | Header | 是 | a14bd5d90a**** | 工作空间ID。 |

**请求语法**

```
DELETE /api/v2/namespaces/[namespace]/jobs/[jobId] HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| namespac e | String | Path | 是 | default-namespace | 项目空间名称。 |
| jobId | String | Path | 是 | 5af678c0-7db0-4650- 94c2-d2604f0a**** | 作业实例ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| success | Boolean | true | 请求是否成功。 |
| requestId | String | CBC799F0-AS7S- 1D30-8A4F- 882ED4DD**** | 请求ID。 |
| errorCode | String | "" | 当success为false时，该值不为空，表示业务错误码； 当success为true时，该值为空。 |
| errorMessage | String | "" | 当success为false，返回业务错误信息； 当success为true，返回空值。 |

实时计算（流计算） 参考

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| httpCode | Integer | 200 | 固定值200。 |

**示例**

请求示例

```
DELETE /api/v2/namespaces/[namespace]/jobs/[jobId] HTTP/1.1 &namespace=default-namespace &jobId=5af678c0-7db0-4650-94c2-d2604f0a****
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "success":true,
 "requestId":"CBC799F0-AS7S-1D30-8A4F-882ED4DD****",
 "errorMessage":"",
 "errorCode":"",
 "httpCode":200
}
```

`XML` 格式

```xml
<success>true</success> <requestId>CBC799F0-AS7S-1D30-8A4F-882ED4DD****</requestId> <errorMessage /> <errorCode /> <httpCode>200</httpCode>
```

###### DeleteDeployment

根据已部署作业ID删除已部署作业。

**请求头**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| workspace | String | Header | 是 | a14bd5d90a**** | 工作空间ID。 |

**请求语法**

```
DELETE /api/v2/namespaces/[namespace]/deployments/[deploymentId] HTTP/1.1
```

**请求参数**

实时计算（流计算） 参考

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| namespac e | String | Path | 是 | default-namespace | 项目空间名称。 |
| deployme ntId | String | Path | 是 | 5737ef81-d2f1-49cf- 8752-30910809**** | 作业ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| success | Boolean | true | 请求是否成功。 |
| requestId | String | CBC799F0-AS7S- 1D30-8A4F- 882ED4DD**** | 请求ID。 |
| errorCode | String | "" | 当success为false时，该值不为空，表示业务错误码。 当success为true时，该值为空。 |
| errorMessage | String | "" | 当success为false，返回业务错误信息。 当success为true，返回空值。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```
DELETE /api/v2/namespaces/[namespace]/deployments/[deploymentId] HTTP/1.1 &namespace=default-namespace &deploymentId=5737ef81-d2f1-49cf-8752-30910809****
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "success":true,
 "requestId":"CBC799F0-AS7S-1D30-8A4F-882ED4DD****",
 "errorMessage":"",
 "errorCode":"",
 "httpCode":200
}
```

`XML` 格式实时计算（流计算） 参考

```xml
<success>true</success> <requestId>CBC799F0-AS7S-1D30-8A4F-882ED4DD****</requestId> <errorMessage /> <errorCode /> <httpCode>200</httpCode>
```

###### CreateVariable

创建变量。

**请求头**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| workspace | String | Header | 是 | a14bd5d90a**** | 工作空间ID。 |

**请求语法**

```
POST /api/v2/namespaces/[namespace]/variables HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| namespac e | String | Path | 是 | default-namespace | 项目空间名称。 |

|  | 参数名称 |  |  | 类型 |  | 位置 |  |  | 是否必选 |  | 示例 |  | 说明 |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  | body |  |  |  |  |  |  |  |  |  | {'descript |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  | {'descript |  |  |
|  |  |  |  |  |  |  |  |  |  |  | ion': |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  | 'Created by |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  | VVP2 SDK', |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  | 'kind': |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  | 'Encrypted', |  | 创建变量的数据 |  |
|  |  | body |  | string |  | wholebody |  |  | 是 |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  | 'name': |  | 内容。 |  |
|  |  |  |  |  |  |  |  |  |  |  | 'sls access _ _ |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  | id', |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  | 'value': |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  | 'dBRPSRR8Lbb |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  | ylhdZ'} |  |  |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| success | Boolean | true | 请求是否成功。 |

| link存算分离版开发 | 指南·OpenAPI |  |  |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | String | CBC799F0-AS7S- 1D30-8A4F- 882ED4DD**** | 请求ID。 |
| data | String | { "description": "Created by VVP2 SDK", "kind": "Encrypted", "name": "sls access id", _ _ "value": "dBRPSRR8Lb****" } | 当success为false，返回空值。 当success为true，返回详细数据。 |
| errorCode | String | "" | 当success为false时，该值不为空，表示业务错误码。 当success为true时，该值为空。 |
| errorMessage | String | "" | 当success为false，返回业务错误信息。 当success为true，返回空值。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```json
POST /api/v2/namespaces/[namespace]/variables HTTP/1.1 { "namespace":"default-namespace", "body":"{'description': 'Created by VVP2 SDK', 'kind': 'Encrypted', 'name': 'sls_access_id', 'value': 'dBRPSRR8LbbylhdZ'}" }
```

正常返回示例 `JSON` 格式

```json
{
 "data":"{    \"description\": \"Created by VVP2 SDK\",    \"kind\": \"Encrypted\",    \
"name\": \"sls_access_id\", \"value\": \"dBRPSRR8Lb****\" }",
 "success":true,
 "requestId":"CBC799F0-AS7S-1D30-8A4F-882ED4DD****",
 "errorMessage":"",
 "errorCode":"",
 "httpCode":200
}
```

`XML` 格式实时计算（流计算） 参考

```xml
<data>{
    &quot;description&quot;: &quot;Created by VVP2 SDK&quot;,
    &quot;kind&quot;: &quot;Encrypted&quot;,
    &quot;name&quot;: &quot;sls_access_id&quot;,
    &quot;value&quot;: &quot;dBRPSRR8Lb****&quot;
  }</data>
 <success>true</success>
 <requestId>CBC799F0-AS7S-1D30-8A4F-882ED4DD****</requestId>
 <errorMessage  />
 <errorCode  />
 <httpCode>200</httpCode>
```

###### CreateSavepoint

创建快照。

**请求头**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| workspace | String | Header | 是 | a14bd5d90a**** | 工作空间ID。 |

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| namespac e | String | Path | 是 | default-namespace | 项目空间名称。 |
| body | String | Body | 否 | { 'deploymentId': 'ee56beb9-2a99-4d87- 8633-63c****2', 'description': '', 'nativeFormat': False } | 触发 savepoint 参数。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| success | Boolean | true | 请求是否成功。 |
| requestId | String | CBC799F0-AS7S- 1D30-8A4F- 882ED4DD**** | 请求ID。 |

实时计算（流计算） 参考

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| data | String | { "createdAt": 178305****, "deploymentId": "f9d616ef-4422- 42b5-b95c- f69****", "description": "", "jobId": "fa1b89ca- 908b-4cd5-b5b1- bb0ac****", "modifiedAt": 1783051217, "namespace": "flinkteam", "nativeFormat": false, "savepointId": "f1702682-c180- 4799-954a- e321****", "savepointLocation ": "oss://flink- full****", "savepointOrigin": "USER REQUEST", _ "status": { "state": "STARTED" }, "stopWithDrainEna bled": false } | 当success为false，返回空值。 当success为true，返回详细数据。 |
| errorCode | String | "" | 当success为false时，该值不为空，表示业务错误码。 当success为true时，该值为空。 |
| errorMessage | String | "" | 当success为false，返回业务错误信息。 当success为true，返回空值。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```json
POST /api/v2/namespaces/[namespace]/savepoints HTTP/1.1 { "namespace":"default-namespace" }
```

正常返回示例 `JSON` 格式实时计算（流计算） 参考

```json
{
 "data":"{    \"createdAt\": 178305****,    \"deploymentId\": \"f9d616ef-4422-42b5-b95c-
f69****\", \"description\": \"\", \"jobId\": \"fa1b89ca-908b-4cd5-b5b1-bb0ac****\" , \"modifiedAt\": 1783051217, \"namespace\": \"flinkteam\", \"nativeFormat\": f alse, \"savepointId\": \"f1702682-c180-4799-954a-e321****\", \"savepointLocation\": \"oss://flink-full****\", \"savepointOrigin\": \"USER_REQUEST\ ", \"status\": { \"state\": \"STARTED\" }, \"stopWithDrainEnabled\": false }",
 "success":true,
 "requestId":"CBC799F0-AS7S-1D30-8A4F-882ED4DD****",
 "errorMessage":"",
 "errorCode":"",
 "httpCode":200
}
```

`XML` 格式

```xml
<data>{
    &quot;createdAt&quot;: 178305****,
    &quot;deploymentId&quot;: &quot;f9d616ef-4422-42b5-b95c-f69****&quot;,
    &quot;description&quot;: &quot;&quot;,
    &quot;jobId&quot;: &quot;fa1b89ca-908b-4cd5-b5b1-bb0ac****&quot;,
    &quot;modifiedAt&quot;: 1783051217,
    &quot;namespace&quot;: &quot;flinkteam&quot;,
    &quot;nativeFormat&quot;: false,
    &quot;savepointId&quot;: &quot;f1702682-c180-4799-954a-e321****&quot;,
    &quot;savepointLocation&quot;: &quot;oss://flink-full****&quot;,
    &quot;savepointOrigin&quot;: &quot;USER_REQUEST&quot;,
    &quot;status&quot;: {
      &quot;state&quot;: &quot;STARTED&quot;
    },
    &quot;stopWithDrainEnabled&quot;: false
  }</data>
 <success>true</success>
 <requestId>CBC799F0-AS7S-1D30-8A4F-882ED4DD****</requestId>
 <errorMessage  />
 <errorCode  />
 <httpCode>200</httpCode>
```

###### CreateMember

将一个用户添加到对应项目空间下并授予对应权限。

**请求头**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| workspace | String | Header | 是 | a14bd5d90a**** | 工作空间ID。 |

**请求语法**

实时计算（流计算） 参考

```
POST /gateway/v2/namespaces/[namespace]/members HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| namespac e | String | Path | 是 | default-namespace | 项目空间名称。 |

| 参数名称 | 类型 |  | 位置 |  |  | 是否必选 |  | 示例 |  | 说明 |  |
|---|---|---|---|---|---|---|---|---|---|---|---|
| body | string |  | wholebody |  |  |  |  | {'member': |  |  |  |
|  |  |  |  |  |  |  |  |  | {'member': |  |  |
|  |  |  |  |  |  |  |  | '2313667542* |  |  |  |
|  |  |  |  |  |  |  |  |  |  | 成员账号和权限 |  |
|  |  |  |  |  | ody | 否 |  |  |  | 成员账号和权 |  |
|  |  |  |  |  |  |  |  | ***5', |  | 对应关系。 |  |
|  |  |  |  |  |  |  |  |  |  | 对应 |  |
|  |  |  |  |  |  |  |  | 'role': |  |  |  |
|  |  |  |  |  |  |  |  | 'EDITOR'} |  |  |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| success | Boolean | true | 请求是否成功。 |
| requestId | String | CBC799F0-AS7S- 1D30-8A4F- 882ED4DD**** | 请求ID。 |
| data | String | { "member": "2313667542****", "role": "editor" } | 当success为false，返回空值。 当success为true，返回详细数据。 |
| errorCode | String | "" | 当success为false时，该值不为空，表示业务错误码。 当success为true时，该值为空。 |
| errorMessage | String | "" | 当success为false，返回业务错误信息。 当success为true，返回空值。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```json
POST /gateway/v2/namespaces/[namespace]/members HTTP/1.1 { "namespace":"default-namespace" }
```

正常返回示例实时计算（流计算） 参考 `JSON` 格式

```json
{
 "data":"{    \"member\": \"2313667542****\",    \"role\": \"editor\"  }",
 "success":true,
 "requestId":"CBC799F0-AS7S-1D30-8A4F-882ED4DD****",
 "errorMessage":"",
 "errorCode":"",
 "httpCode":200
}
```

`XML` 格式

```xml
<data>{
    &quot;member&quot;: &quot;2313667542****&quot;,
    &quot;role&quot;: &quot;editor&quot;
  }</data>
 <success>true</success>
 <requestId>CBC799F0-AS7S-1D30-8A4F-882ED4DD****</requestId>
 <errorMessage  />
 <errorCode  />
 <httpCode>200</httpCode>
```

###### CreateDeployment

创建一个已部署作业。

**请求头**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| workspace | String | Header | 是 | a14bd5d90a**** | 工作空间ID。 |

**请求语法**

```
POST /api/v2/namespaces/[namespace]/deployments HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| namespac e | String | Path | 是 | default-namespace | 项目空间名称。 |

|  | 参数名称 | 类型 | 位置 |  | 是否必选 |  |  | 示例 |  | 说明 |
|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  | {"artifact |  |  |
|  |  |  |  |  |  |  |  |  | {"artifact |  |
|  |  |  |  |  |  |  |  | ": |  |  |
|  |  |  |  |  |  |  |  | {"kind":"SQL |  |  |
|  |  |  |  |  |  |  |  | SCRIPT","sql |  |  |

|  |  | link存算分离版开参考 |  |  |  |  | 发指南·OpenAPI |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 实时计算（流计算） |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  | 参数名称 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | Artifact": |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  | 类型 |  |  |  |  | 位置 |  |  |  |  |  | 是否必选 |  |  |  |  |  | 示例 |  |  |  |  | 说明 |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | {"sqlScript" |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | :"CREATE |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | TEMPORARY |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | TABLE |  |  | datah e (st |  |  |  |  |
|  |  | body |  |  |  |  | string |  |  |  |  | wholebody |  |  |  |  |  |  |  |  |  |  |  | ub tabl |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | _ rname |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | VARCHAR) |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | with ( |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | ' = |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 'datagen' |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | ); |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | TEMPORARY |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | TABLE |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | VARCHAR, |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | lens |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | BIGINT) |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 是 |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | ' = |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 'print' |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | ); |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | Deployment |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | INTO |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 内 |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | kafka table _ |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | strname, |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | CAST |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | (CHAR LENGTH _ |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | (strname) |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | AS BIGINT) |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | AS lens |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | FROM |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | ble; |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | ymentTarget" |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | : |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | {"mode":"PER |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | JOB","name" _ |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | :"dt- |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | flinkteam"}, |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | "engineVersi |  |  |  |  |  |  |  |

实时计算（流计算） 参考

|  |  |  |  | on":"vvr- |  |  |
|---|---|---|---|---|---|---|
| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |  |
|  |  |  |  | 8.0.7-flink- |  |  |
|  |  |  |  | 1.17","execu |  |  |
|  |  |  |  | tionMode":"S |  |  |
|  |  |  |  | TREAMING","n |  |  |
|  |  |  |  | ame":"sqlJob |  |  |
|  |  |  |  | "} |  |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| success | Boolean | true | 请求是否成功。 |
| requestId | String | CBC799F0-AS7S- 1D30-8A4F- 882ED4DD**** | 请求ID。 |
|  |  | { "artifact": { "kind": "SQLSCRIPT", "sqlArtifact": { "sqlScript": "CREATE TEMPORARY TABLE `datahub table` _ (strname VARCHAR) with ( 'connector' = 'datagen' ); CREATE TEMPORARY TABLE `kafka table` _ (strname VARCHAR, lens BIGINT) with ( 'connector' = 'print' ); |  |
|  |  | INSERT INTO kafka table _ SELECT strname, CAST (CHAR LENGTH _ (strname) AS BIGINT) AS lens FROM datahub table; _ |  |

实时计算（流计算） 参考

| 参数名称 | 类型 | " } }, "creator": 示例 "20877848***", | 说明 |
|---|---|---|---|
|  |  | "creatorName": "flinkadmin", "deploymentHasCh anged": true, "deploymentId": "f9d616ef-4422- 42b5-b95c-f***", "deploymentTarget ": { "mode": "PER JOB", "name": _ "dt-flinkteam" }, "engineVersion": "vvr-8.0.7-flink- 1.17", "executionMode": "STREAMING", |  |
| data | String | "flinkConf": { "execution.checkpo inting.interval": "180s", "table.exec.state.ttl ": "36 h", "restart- strategy.fixed- delay.delay": "10 s", "restart- strategy": "fixed- delay", "restart- strategy.fixed- delay.attempts": "21474****", "execution.checkpo inting.min-pause": "180s" }, "jobSummary": { "cancelled": 0, "cancelling": 0, "failed": 0, "finished": 0, "running": 0, "starting": 0 }, "logging": { "log4jLoggers": [ { "loggerLevel": "INFO", "loggerName": "" } ], "logReservePolicy": { "expirationDays": 7, "openHistory": true }, "loggingProfile": "default" }, "modifier": "2087784829****", "modifierName": "flinkadmin", "name": "sqlJob", "namespace": "flinkteam", "streamingResourc eSetting": { "basicResourceSett ing": { "jobmanagerResou rceSettingSpec": { | 当success为false，返回空值。 当success为true，返回详细数据。 |

实时计算（流计算） 参考

| 参数名称 | 类型 | "cpu": 1.0, 示例 "memory": "4Gi" }, | 说明 |
|---|---|---|---|
|  |  | "parallelism": 1, "taskmanagerReso urceSettingSpec": { "cpu": 1.0, "memory": "4Gi" } }, "resourceSettingMo de": "BASIC" } } |  |
| errorCode | String | "" | 当success为false时，该值不为空，表示业务错误码。 当success为true时，该值为空。 |
| errorMessage | String | "" | 当success为false，返回业务错误信息。 当success为true，返回空值。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```json
POST /api/v2/namespaces/[namespace]/deployments HTTP/1.1 { "namespace":"default-namespace", "body":"{"artifact":{"kind":"SQLSCRIPT","sqlArtifact":{"sqlScript":"CREATE TEMPORARY TABLE `datahub_table` (strname VARCHAR) with ( 'connector' = 'datagen' ); CREATE TEMPORARY TABLE `kafka_table` (strname VARCHAR, lens BIGINT) with ( 'connector' = 'print' ); INSERT INTO kafka_table SELECT strname, CAST (CHAR_LENGTH (str name) AS BIGINT) AS lens FROM datahub_table; "}},"deploymentTarget":{"mode":"PER_JOB" ,"name":"dt-flinkteam"},"engineVersion":"vvr-8.0.7-flink- 1.17","executionMode":"STREAMING","name":"sqlJob"}" }
```

正常返回示例 `JSON` 格式实时计算（流计算） 参考

```json
{
 "data":"{    \"artifact\": {      \"kind\": \"SQLSCRIPT\",      \"sqlArtifact\": {
\"sqlScript\": \"CREATE TEMPORARY TABLE `datahub_table` (strname VARCHAR)\with (\ 'co nnector' = 'datagen'\ );\\CREATE TEMPORARY TABLE `kafka_table` (strname VARCHAR, lens BIGINT)\with (\ 'connector' = 'print'\ );\\INSERT INTO kafka_table\SELECT strname, CAST (CHAR_LENGTH (strname) AS BIGINT) AS lens\FROM\ datahub_table;\\" } }, \"creator\": \"20877848***\", \"creatorName\": \"flinkadmin\", \"deploymentHasChanged\": true, \"deploymentId\": \"f9d616ef-4422-42b5-b95c-f***\", \"deploymentTarget\": { \"mode\": \"PER_JOB\", \"name\": \"dt-flinkteam\" } , \"engineVersion\": \"vvr-8.0.7-flink-1.17\", \"executionMode\": \"STREAMING\", \"flinkConf\": { \"execution.checkpointing.interval\": \"180s\", \"table.exec.state.ttl\": \"36 h\", \"restart-strategy.fixed-delay.delay\": \"10 s\ ", \"restart-strategy\": \"fixed-delay\", \"restart-strategy.fixed-delay.attem pts\": \"21474****\", \"execution.checkpointing.min-pause\": \"180s\" }, \"jo bSummary\": { \"cancelled\": 0, \"cancelling\": 0, \"failed\": 0, \"finished\": 0, \"running\": 0, \"starting\": 0 }, \"logging\": { \"log4jLoggers\": [ { \"loggerLevel\": \"INFO\", \"loggerName\": \"\" } ], \"logReservePolicy\": { \"expirationDays\": 7, \"openHistory\": true }, \"loggingProfile\": \"d efault\" }, \"modifier\": \"2087784829****\", \"modifierName\": \"flinkadmin\", \"name\": \"sqlJob\", \"namespace\": \"flinkteam\", \"streamingResourceSetting\": { \"basicResourceSetting\": { \"jobmanagerResourceSettingSpec\": { \"cpu\": 1.0, \"memory\": \"4Gi\" }, \"parallelism\": 1, \" taskmanagerResourceSettingSpec\": { \"cpu\": 1.0, \"memory\": \"4Gi\" } }, \"resourceSettingMode\": \"BASIC\" } }",
 "success":true,
 "requestId":"CBC799F0-AS7S-1D30-8A4F-882ED4DD****",
 "errorMessage":"",
 "errorCode":"",
 "httpCode":200
}
```

`XML` 格式

```xml
<data>{
    &quot;artifact&quot;: {
      &quot;kind&quot;: &quot;SQLSCRIPT&quot;,
      &quot;sqlArtifact&quot;: {
        &quot;sqlScript&quot;: &quot;CREATE TEMPORARY TABLE `datahub_table` (strname VAR
CHAR)with ( &#x27;connector&#x27; = &#x27;datagen&#x27; );CREATE TEMPORARY TABLE `kafka_table` (strname VARCHAR, lens BIGINT)with ( &#x27;connector&#x27; = &#x27;print&#x27; );INSERT INTO kafka_tableSELECT strname, CAST (CHAR_LENGTH (strname) AS BIGINT) AS lensFROM datahub_table;&quot;
      }
    },
    &quot;creator&quot;: &quot;20877848***&quot;,
    &quot;creatorName&quot;: &quot;flinkadmin&quot;,
    &quot;deploymentHasChanged&quot;: true,
    &quot;deploymentId&quot;: &quot;f9d616ef-4422-42b5-b95c-f***&quot;,
    &quot;deploymentTarget&quot;: {
      &quot;mode&quot;: &quot;PER_JOB&quot;,
      &quot;name&quot;: &quot;dt-flinkteam&quot;
    },
&quot;engineVersion&quot;:&quot;vvr-807-flink-117&quot;,
```

实时计算（流计算） 参考

```
    &quot;engineVersion&quot;: &quot;vvr8.0.7flink1.17&quot;,
    &quot;executionMode&quot;: &quot;STREAMING&quot;,
    &quot;flinkConf&quot;: {
      &quot;execution.checkpointing.interval&quot;: &quot;180s&quot;,
      &quot;table.exec.state.ttl&quot;: &quot;36 h&quot;,
      &quot;restart-strategy.fixed-delay.delay&quot;: &quot;10 s&quot;,
      &quot;restart-strategy&quot;: &quot;fixed-delay&quot;,
      &quot;restart-strategy.fixed-delay.attempts&quot;: &quot;21474****&quot;,
      &quot;execution.checkpointing.min-pause&quot;: &quot;180s&quot;
    },
    &quot;jobSummary&quot;: {
      &quot;cancelled&quot;: 0,
      &quot;cancelling&quot;: 0,
      &quot;failed&quot;: 0,
      &quot;finished&quot;: 0,
      &quot;running&quot;: 0,
      &quot;starting&quot;: 0
    },
    &quot;logging&quot;: {
      &quot;log4jLoggers&quot;: [
        {
          &quot;loggerLevel&quot;: &quot;INFO&quot;,
          &quot;loggerName&quot;: &quot;&quot;
        }
```

`],`

```xml
      &quot;logReservePolicy&quot;: {
        &quot;expirationDays&quot;: 7,
        &quot;openHistory&quot;: true
      },
      &quot;loggingProfile&quot;: &quot;default&quot;
    },
    &quot;modifier&quot;: &quot;2087784829****&quot;,
    &quot;modifierName&quot;: &quot;flinkadmin&quot;,
    &quot;name&quot;: &quot;sqlJob&quot;,
    &quot;namespace&quot;: &quot;flinkteam&quot;,
    &quot;streamingResourceSetting&quot;: {
      &quot;basicResourceSetting&quot;: {
        &quot;jobmanagerResourceSettingSpec&quot;: {
          &quot;cpu&quot;: 1.0,
          &quot;memory&quot;: &quot;4Gi&quot;
        },
        &quot;parallelism&quot;: 1,
        &quot;taskmanagerResourceSettingSpec&quot;: {
          &quot;cpu&quot;: 1.0,
          &quot;memory&quot;: &quot;4Gi&quot;
        }
      },
      &quot;resourceSettingMode&quot;: &quot;BASIC&quot;
    }
  }</data>
 <success>true</success>
 <requestId>CBC799F0-AS7S-1D30-8A4F-882ED4DD****</requestId>
 <errorMessage  />
 <errorCode  />
 <httpCode>200</httpCode>
```

实时计算（流计算） 参考

###### FlinkApiProxy

您可以使用flink rest api的方式来调用本接口，获取session集群或者运行作业的相关信息。注意本接口仅支持您获取相关信息，无法对session集群和作业进行操作或管理。

**请求头**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| workspace | String | Header | 是 | a14bd5d90a**** | 工作空间ID。 |

**请求语法**

```
GET /flink-ui/v2/proxy HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| namespac e | String | Query | 是 | default-namespace | 项目空间名称。 |
| resourceT ype | String | Query | 是 | jobs | 资源类型，支持以下类型： jobs sessionclusters |
| resourceId | String | Query | 是 | c6f157ac-60b9-4b38- 8bad-d43**** | 资源类型是 jobs，则使用 jobid；资源类型是 sessionclusters，则使用 session 名称。 |
| flinkApiPat h | String | Query | 是 | /jobs/4df35f8e54554b23 bf7dcd38a151**** | flink rest api 路径。 如/jobs/jobid/config 可以获取 jobid 对应作业的配置信息，更多使用可查看flink 社区 rest api 文档。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| success | Boolean | true | 请求是否成功。 |
| requestId | String | CBC799F0-AS7S- 1D30-8A4F- 882ED4DD**** | 请求ID。 |
|  |  | {\"jid\":\"65eb3696 db7d4a589851cda |  |

| 实时计算（流计算） |  |  | Flink存算分离版开发指南·OpenAP 参考 |
|---|---|---|---|
| 参数名称 | 类型 | 2****4\",\"name\":\ 示例 "1dbd6e8c-d493- | 说明 |
| data | String | 41d0-aa0f- 45972****1\",\"isSt oppable\":false,\"st ate\":\"RUNNING\",\ "start- time\":178****394,\ "end-time\":- 1,\"duration\":2210 8,\"maxParallelism\ ":- 1,\"now\":178****5 02,\"timestamps\": {\"CANCELLING\":0 ,\"RECONCILING\":0 ,\"INITIALIZING\":17 830****394,\"CREA TED\":17830****3,\ "RESTARTING\":0,\" RUNNING\":1783*** *2,\"FAILING\":0,\"C ANCELED\":0,\"FINI SHED\":0,\"SUSPEN DED\":0,\"FAILED\": 0},\"vertices\": [{\"id\":\"717c7b8a febbfb713****\",\"n ame\":\"Source: datahub table[23] - _ > Calc[24] -> Sink: kafka table[25]\",\" _ maxParallelism\":3 2768,\"parallelism\ ":1,\"status\":\"CRE ATED\",\"start- time\":-1,\"end- time\":- 1,\"duration\":- 1,\"tasks\": {\"CREATED\":0,\"C ANCELING\":0,\"SC HEDULED\":1,\"CAN CELED\":0,\"FAILED \":0,\"RECONCILING \":0,\"INITIALIZING\ ":0,\"FINISHED\":0,\ "DEPLOYING\":0,\"R UNNING\":0},\"metr ics\":{\"read- bytes\":0,\"read- bytes- complete\":false,\" write- bytes\":0,\"write- bytes- complete\":false,\"r ead- records\":0,\"read- records- complete\":false,\" write- records\":0,\"write- records- complete\":false,\" accumulated- backpressured- | 当success为false，返回空值。 当success为true，返回详细数据。 |

实时计算（流计算） 参考

| 参数名称 | 类型 | time\":0,\"accumul 示例 ated-idle- | 说明 |
|---|---|---|---|
|  |  | time\":0,\"accumul ated-busy- time\":0.0}}],\"stat us-counts\": {\"CREATED\":1,\"C ANCELING\":0,\"SC HEDULED\":0,\"CAN CELED\":0,\"FAILED \":0,\"RECONCILING \":0,\"INITIALIZING\ ":0,\"FINISHED\":0,\ "DEPLOYING\":0,\"R UNNING\":0},\"plan \": {\"jid\":\"65eb3696 db7d4a589851cda 26f252924\",\"nam e\":\"1dbd6e8c- d493-41d0-aa0f- 4597224738b1\",\" type\":\"STREAMIN G\",\"nodes\": [{\"id\":\"717c7b8a febbfb713****eb2a 94\",\"parallelism\": 1,\"operator\":\"\",\" operator strategy\" _ :\"\",\"description\": \" [23]:TableSourceSc an(table=[[vvp, default, datahub table]], _ fields=[strname]) +- [24]:Calc(select= [SUBSTRING(strna me, 0, 10) AS strname, CAST(CHAR LENGT _ H(strname) AS BIGINT) AS lens]) +- [25]:Sink(table= [vvp.default.kafka _ table], fields= [strname, lens]) \",\"optimizer prop _ erties\":{}}]}} |  |
| errorCode | String | "" | 当success为false时，该值不为空，表示业务错误码。 当success为true时，该值为空。 |
| errorMessage | String | "" | 当success为false，返回业务错误信息。 当success为true，返回空值。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

实时计算（流计算） 参考请求示例

```
GET /flink-ui/v2/proxy HTTP/1.1 &namespace=default-namespace &resourceType=jobs &resourceId=c6f157ac-60b9-4b38-8bad-d43**** &flinkApiPath=/jobs/4df35f8e54554b23bf7dcd38a151****
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "data":"{\\\"jid\\\":\\\"65eb3696db7d4a589851cda2****4\\\",\\\"name\\\":\\\"1dbd6e8c-d
493-41d0-aa0f- 45972****1\\\",\\\"isStoppable\\\":false,\\\"state\\\":\\\"RUNNING\\\",\\\"starttime\\\":178****394,\\\"end-time\\\":-1,\\\"duration\\\":22108,\\\"maxParallelism\\\":- 1,\\\"now\\\":178****502,\\\"timestamps\\\": {\\\"CANCELLING\\\":0,\\\"RECONCILING\\\":0,\\\"INITIALIZING\\\":17830****394,\\\"CREATED\ ":17830****3,\\\"RESTARTING\\\":0,\\\"RUNNING\\\":1783****2,\\\"FAILING\\\":0,\\\"CANCELED \":0,\\\"FINISHED\\\":0,\\\"SUSPENDED\\\":0,\\\"FAILED\\\":0},\\\"vertices\\\": [{\\\"id\\\":\\\"717c7b8afebbfb713****\\\",\\\"name\\\":\\\"Source: datahub_table[23] -
> Calc[24] -> Sink:
kafka_table[25]\\\",\\\"maxParallelism\\\":32768,\\\"parallelism\\\":1,\\\"status\\\":\\\" EATED\\\",\\\"start-time\\\":-1,\\\"end-time\\\":-1,\\\"duration\\\":-1,\\\"tasks\\\":{ \\\"CREATED\\\":0,\\\"CANCELING\\\":0,\\\"SCHEDULED\\\":1,\\\"CANCELED\\\":0,\\\"FAILED\\\ 0,\\\"RECONCILING\\\":0,\\\"INITIALIZING\\\":0,\\\"FINISHED\\\":0,\\\"DEPLOYING\\\":0,\\\" NNING\\\":0},\\\"metrics\\\":{\\\"read-bytes\\\":0,\\\"read-bytescomplete\\\":false,\\\"write-bytes\\\":0,\\\"write-bytes-complete\\\":false,\\\"readrecords\\\":0,\\\"read-records-complete\\\":false,\\\"write-records\\\":0,\\\"writerecords-complete\\\":false,\\\"accumulated-backpressured-time\\\":0,\\\"accumulatedidle-time\\\":0,\\\"accumulated-busy-time\\\":0.0}}],\\\"status-counts\\\": {\\\"CREATED\\\":1,\\\"CANCELING\\\":0,\\\"SCHEDULED\\\":0,\\\"CANCELED\\\":0,\\\"FAILED\\ :0,\\\"RECONCILING\\\":0,\\\"INITIALIZING\\\":0,\\\"FINISHED\\\":0,\\\"DEPLOYING\\\":0,\\\ UNNING\\\":0},\\\"plan\\\": {\\\"jid\\\":\\\"65eb3696db7d4a589851cda26f252924\\\",\\\"name\\\":\\\"1dbd6e8c-d493- 41d0-aa0f-4597224738b1\\\",\\\"type\\\":\\\"STREAMING\\\",\\\"nodes\\\": [{\\\"id\\\":\\\"717c7b8afebbfb713****eb2a94\\\",\\\"parallelism\\\":1,\\\"operator\\\":\\ \\\",\\\"operator_strategy\\\":\\\"\\\",\\\"description\\\":\\\" [23]:TableSourceScan(table=[[vvp, default, datahub_table]], fields=[strname])<br/>+- [2 4]:Calc(select=[SUBSTRING(strname, 0, 10) AS strname, CAST(CHAR_LENGTH(strname) AS BIGINT) AS lens])<br/> +- [25]:Sink(table=[vvp.default.kafka_table], fields=[strname, lens])<br/>\\\",\\\"optimizer_properties\\\":{}}]}}",
 "success":true,
 "requestId":"CBC799F0-AS7S-1D30-8A4F-882ED4DD****",
 "errorMessage":"",
 "errorCode":"",
 "httpCode":200
}
```

`XML` 格式实时计算（流计算） 参考

```xml
<data> {\&quot;jid\&quot;:\&quot;65eb3696db7d4a589851cda2****4\&quot;,\&quot;name\&quot;:\&quot;1 d6e8c-d493-41d0-aa0f- 45972****1\&quot;,\&quot;isStoppable\&quot;:false,\&quot;state\&quot;:\&quot;RUNNING\&quot \&quot;start-time\&quot;:178****394,\&quot;end-time\&quot;:- 1,\&quot;duration\&quot;:22108,\&quot;maxParallelism\&quot;:- 1,\&quot;now\&quot;:178****502,\&quot;timestamps\&quot;: {\&quot;CANCELLING\&quot;:0,\&quot;RECONCILING\&quot;:0,\&quot;INITIALIZING\&quot;:17830** 394,\&quot;CREATED\&quot;:17830****3,\&quot;RESTARTING\&quot;:0,\&quot;RUNNING\&quot;:1783
**2,\&quot;FAILING\&quot;:0,\&quot;CANCELED\&quot;:0,\&quot;FINISHED\&quot;:0,\&quot;SUSPE
ED\&quot;:0,\&quot;FAILED\&quot;:0},\&quot;vertices\&quot;: [{\&quot;id\&quot;:\&quot;717c7b8afebbfb713****\&quot;,\&quot;name\&quot;:\&quot;Source: datahub_table[23] -&gt; Calc[24] -&gt; Sink: kafka_table[25]\&quot;,\&quot;maxParallelism\&quot;:32768,\&quot;parallelism\&quot;:1,\&qu ;status\&quot;:\&quot;CREATED\&quot;,\&quot;start-time\&quot;:-1,\&quot;endtime\&quot;:-1,\&quot;duration\&quot;:-1,\&quot;tasks\&quot;: {\&quot;CREATED\&quot;:0,\&quot;CANCELING\&quot;:0,\&quot;SCHEDULED\&quot;:1,\&quot;CANCEL \&quot;:0,\&quot;FAILED\&quot;:0,\&quot;RECONCILING\&quot;:0,\&quot;INITIALIZING\&quot;:0, quot;FINISHED\&quot;:0,\&quot;DEPLOYING\&quot;:0,\&quot;RUNNING\&quot;:0},\&quot;metrics\& ot;:{\&quot;read-bytes\&quot;:0,\&quot;read-bytes-complete\&quot;:false,\&quot;write-by tes\&quot;:0,\&quot;write-bytes-complete\&quot;:false,\&quot;readrecords\&quot;:0,\&quot;read-records-complete\&quot;:false,\&quot;writerecords\&quot;:0,\&quot;write-records-complete\&quot;:false,\&quot;accumulatedbackpressured-time\&quot;:0,\&quot;accumulated-idle-time\&quot;:0,\&quot;accumulatedbusy-time\&quot;:0.0}}],\&quot;status-counts\&quot;: {\&quot;CREATED\&quot;:1,\&quot;CANCELING\&quot;:0,\&quot;SCHEDULED\&quot;:0,\&quot;CANCEL \&quot;:0,\&quot;FAILED\&quot;:0,\&quot;RECONCILING\&quot;:0,\&quot;INITIALIZING\&quot;:0, quot;FINISHED\&quot;:0,\&quot;DEPLOYING\&quot;:0,\&quot;RUNNING\&quot;:0},\&quot;plan\&quo
```

:

```xml
{\&quot;jid\&quot;:\&quot;65eb3696db7d4a589851cda26f252924\&quot;,\&quot;name\&quot;:\&quo 1dbd6e8c-d493-41d0-aa0f- 4597224738b1\&quot;,\&quot;type\&quot;:\&quot;STREAMING\&quot;,\&quot;nodes\&quot;: [{\&quot;id\&quot;:\&quot;717c7b8afebbfb713****eb2a94\&quot;,\&quot;parallelism\&quot;:1,\ uot;operator\&quot;:\&quot;\&quot;,\&quot;operator_strategy\&quot;:\&quot;\&quot;,\&quot;d cription\&quot;:\&quot;[23]:TableSourceScan(table=[[vvp, default, datahub_table]], fields=[strname])&lt;br/&gt;+- [24]:Calc(select=[SUBSTRING(strname, 0, 10) AS strname, CAST(CHAR_LENGTH(strname) AS BIGINT) AS lens])&lt;br/&gt; +- [25]:Sink(table= [vvp.default.kafka_table], fields=[strname, lens])&lt;br/&gt;\&quot;,\&quot;optimizer_properties\&quot;:{}}]}}</data> <success>true</success> <requestId>CBC799F0-AS7S-1D30-8A4F-882ED4DD****</requestId> <errorMessage /> <errorCode /> <httpCode>200</httpCode>
```

###### ListDeployments

列出所有部署的资源信息。

**请求头**

实时计算（流计算） 参考

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| workspace | String | Header | 是 | a14bd5d90a**** | 工作空间ID。 |

**请求语法**

```
GET /api/v2/namespaces/[namespace]/deployments HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| namespac e | String | Path | 是 | default-namespace | 项目空间名称。 |
| pageSize | Integ er | Query | 否 | 10 | 分页参数，表示所请求页码元素数量，最大值为 100， 最小值为 1，默认值为 10。 |
| pageIndex | Integ er | Query | 否 | 1 | 分页参数，页码索引，表示所请求页码，最小值为 1， 默认值为 1。 |
| name | String | Query | 否 | test | deployment 名称。 |
| execution Mode | String | Query | 否 | STREAMING | deployment 执行模式。 枚举值: BATCH(批作业) STREAMING(流作业) |
| status | String | Query | 否 | FINISHED | deployment 最新作业状态。 枚举值: CANCELLED(CANCELL ED) FAILED(FAILED) RUNNING(RUNNING) TRANSITIONING(TRAN SITIONING) FINISHED(FINISHED) |
| creator | String | Query | 否 | 17915******4216 | 创建者 UID。 |
| modifier | String | Query | 否 | 170906468757**** | 修改者 UID。 |
| labelKey | String | Query | 否 | key1 | 标签名。 |

| link存算分离版 | 开发指南 | ·OpenAPI |  |  | 实时计算（流计算） |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| labelValue Array | String | Query | 否 | value1,value2 | 标签值，多个值使用分号隔开。 |

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| sortName | string | Query | 否 | gmt create _ | 排序方式，支持按创建时间和修改时间倒序返回数据。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| success | Boolean | true | 请求是否成功。 |
| requestId | String | CBC799F0-AS7S- 1D30-8A4F- 882ED4DD**** | 请求ID。 |

实时计算（流计算） 参考

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| data | String | [ { "artifact": { "kind": "SQLSCRIPT" }, "creator": "2087784829****", "creatorName": "flinkadmin", "deploymentHasCh anged": true, "deploymentId": "f9d616ef-4422- 42b5-b95c- f691d4****", "deploymentTarget ": { "mode": "PER JOB", "name": _ "dt-flinkteam" }, "engineVersion": "vvr-8.0.7-flink- 1.17", "executionMode": "STREAMING", "flinkConf": { "execution.checkpo inting.interval": "180s", "table.exec.state.ttl ": "36 h", "restart- strategy.fixed- delay.delay": "10 s", "restart- strategy": "fixed- delay", "restart- strategy.fixed- delay.attempts": "21474****7", "execution.checkpo inting.min-pause": "180s" }, "jobSummary": { "cancelled": 0, "cancelling": 0, "failed": 0, "finished": 0, "running": 0, "starting": 0 }, "modifier": "208778482****5", "modifierName": "flinkadmin", "name": "sqlJob", "namespace": "flinkteam" } ] | 当success为false，返回空值。 当success为true，返回详细数据。 |
| errorCode | String | "" | 当success为false时，该值不为空，表示业务错误码。 当success为true时，该值为空。 |
| errorMessage | String | "" | 当success为false，返回业务错误信息。 当success为true，返回空值。 |

| F | link存算分离版开发参考 | 指南·OpenAPI |  | 实时计算（流计算） |  |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| httpCode | Integer | 200 | HTTP状态码。 |
| totalSize | Integer | 1 | 总条数。 |

**示例**

请求示例

```
GET /api/v2/namespaces/[namespace]/deployments HTTP/1.1 &namespace=default-namespace
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "totalSize":1,
 "data":"[    {      \"artifact\": {        \"kind\": \"SQLSCRIPT\"      },      \"creato
r\": \"2087784829****\", \"creatorName\": \"flinkadmin\", \"deploymentHasChanged\": true, \"deploymentId\": \"f9d616ef-4422-42b5-b95c-f691d4*
***\",      \"deploymentTarget\": {        \"mode\": \"PER_JOB\",        \"name\": \"dt-
flinkteam\" }, \"engineVersion\": \"vvr-8.0.7-flink-1.17\", \"executionMode\": \"STREAMING\", \"flinkConf\": { \"execution.checkpointing.interval\": \"180s\", \"table.exec.state.ttl\": \"36 h\ ", \"restart-strategy.fixed-delay.delay\": \"10 s\", \"restart-strategy\": \"fixed-delay\", \"restart-strategy.fixed-delay.attempts\": \"21474****7\", \"execution.checkpointing.min-pause\": \"180s\" }, \"jobSummary\": { \" cancelled\": 0, \"cancelling\": 0, \"failed\": 0, \"finished\": 0, \"running\": 0, \"starting\": 0 }, \"modifier\": \"208778482****5\", \"modifierName\": \"flinkadmin\", \"name\": \"sqlJob\", \"namespace\": \"flink team\" } ]",
 "success":true,
 "requestId":"CBC799F0-AS7S-1D30-8A4F-882ED4DD****",
 "errorMessage":"",
 "errorCode":"",
 "httpCode":200
}
```

`XML` 格式实时计算（流计算） 参考

```xml
<totalSize>1</totalSize> <data>[
    {
      &quot;artifact&quot;: {
        &quot;kind&quot;: &quot;SQLSCRIPT&quot;
      },
      &quot;creator&quot;: &quot;2087784829****&quot;,
      &quot;creatorName&quot;: &quot;flinkadmin&quot;,
      &quot;deploymentHasChanged&quot;: true,
      &quot;deploymentId&quot;: &quot;f9d616ef-4422-42b5-b95c-f691d4****&quot;,
      &quot;deploymentTarget&quot;: {
        &quot;mode&quot;: &quot;PER_JOB&quot;,
        &quot;name&quot;: &quot;dt-flinkteam&quot;
      },
      &quot;engineVersion&quot;: &quot;vvr-8.0.7-flink-1.17&quot;,
      &quot;executionMode&quot;: &quot;STREAMING&quot;,
      &quot;flinkConf&quot;: {
        &quot;execution.checkpointing.interval&quot;: &quot;180s&quot;,
        &quot;table.exec.state.ttl&quot;: &quot;36 h&quot;,
        &quot;restart-strategy.fixed-delay.delay&quot;: &quot;10 s&quot;,
        &quot;restart-strategy&quot;: &quot;fixed-delay&quot;,
        &quot;restart-strategy.fixed-delay.attempts&quot;: &quot;21474****7&quot;,
        &quot;execution.checkpointing.min-pause&quot;: &quot;180s&quot;
      },
      &quot;jobSummary&quot;: {
        &quot;cancelled&quot;: 0,
        &quot;cancelling&quot;: 0,
        &quot;failed&quot;: 0,
        &quot;finished&quot;: 0,
        &quot;running&quot;: 0,
        &quot;starting&quot;: 0
      },
      &quot;modifier&quot;: &quot;208778482****5&quot;,
      &quot;modifierName&quot;: &quot;flinkadmin&quot;,
      &quot;name&quot;: &quot;sqlJob&quot;,
      &quot;namespace&quot;: &quot;flinkteam&quot;
    }
  ]</data>
 <success>true</success>
 <requestId>CBC799F0-AS7S-1D30-8A4F-882ED4DD****</requestId>
 <errorMessage  />
 <errorCode  />
 <httpCode>200</httpCode>
```

###### ListMembers

查看特定项目下用户UID和授权的对应关系。

**请求头**

实时计算（流计算） 参考

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| workspace | String | Header | 是 | a14bd5d90a**** | 工作空间ID。 |

**请求语法**

```
GET /gateway/v2/namespaces/[namespace]/members HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| namespac e | String | Path | 是 | default-namespace | 项目空间名称。 |
| pageIndex | Integ er | Query | 否 | 1 | 分页参数，页码索引，表示所请求页码，默认值为 1。 |
| pageSize | Integ er | Query | 否 | 10 | 分页参数，所请求页码的元素数量，默认值为 10，最大值 100。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| success | Boolean | true | 请求是否成功。 |
| requestId | String | CBC799F0-AS7S- 1D30-8A4F- 882ED4DD**** | 请求ID。 |
| data | String | [ { "member": "19326829721009 78", "role": "owner" }, { "member": "20877848297216 2995", "role": "owner" } ] | 当success为false，返回空值。 当success为true，返回详细数据。 |
| errorCode | String | "" | 当success为false时，该值不为空，表示业务错误码。 当success为true时，该值为空。 |
| errorMessage | String | "" | 当success为false，返回业务错误信息。 当success为true，返回空值。 |
| httpCode | Integer | 200 | HTTP状态码。 |

|  | 实时计算（流计算） |  |  | Flink存算分离版开发指南·OpenAP 参考 | I |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| totalSize | Integer | 1 | 总条数。 |

**示例**

请求示例

```
GET /gateway/v2/namespaces/[namespace]/members HTTP/1.1 &namespace=default-namespace
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "totalSize":1,
 "data":"[    {      \"member\": \"1932682972100978\",      \"role\": \"owner\"    },
{ \"member\": \"208778482972162995\", \"role\": \"owner\" } ]",
 "success":true,
 "requestId":"CBC799F0-AS7S-1D30-8A4F-882ED4DD****",
 "errorMessage":"",
 "errorCode":"",
 "httpCode":200
}
```

`XML` 格式

```xml
<totalSize>1</totalSize> <data>[
    {
      &quot;member&quot;: &quot;1932682972100978&quot;,
      &quot;role&quot;: &quot;owner&quot;
    },
    {
      &quot;member&quot;: &quot;208778482972162995&quot;,
      &quot;role&quot;: &quot;owner&quot;
    }
  ]</data>
 <success>true</success>
 <requestId>CBC799F0-AS7S-1D30-8A4F-882ED4DD****</requestId>
 <errorMessage  />
 <errorCode  />
 <httpCode>200</httpCode>
```

###### ListVariables

获取变量列表。

**请求头**

实时计算（流计算） 参考

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| workspace | String | Header | 是 | a14bd5d90a**** | 工作空间ID。 |

**请求语法**

```
GET /api/v2/namespaces/[namespace]/variables HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| namespac e | String | Path | 是 | default-namespace | 项目空间名称。 |
| pageSize | Integ er | Query | 否 | 10 | 分页参数，表示所请求页码元素数量，最大值为 100， 最小值为 1，默认值为 10。 |
| pageIndex | Integ er | Query | 否 | 1 | 分页参数，页码索引，表示所请求页码，最小值为 1， 默认值为 1。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| success | Boolean | true | 请求是否成功。 |
| requestId | String | CBC799F0-AS7S- 1D30-8A4F- 882ED4DD**** | 请求ID。 |
| data | String | [ { "description": "Created by VVP2 SDK", "kind": "Encrypted", "name": "sls access id", _ _ "value": "******" } ] | 当success为false，返回空值。 当success为true，返回详细数据。 |
| errorCode | String | "" | 当success为false时，该值不为空，表示业务错误码。 当success为true时，该值为空。 |
| errorMessage | String | "" | 当success为false，返回业务错误信息。 当success为true，返回空值。 |
| httpCode | Integer | 200 | HTTP状态码。 |

| 实时计算（流计算） |  |  | Flink存算分离版开发指南·OpenAP 参考 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| totalSize | Integer | 1 | 总条数。 |
| pageIndex | Integer | 1 | 分页参数，页码索引，表示所请求页码。 |
| pageSize | Integer | 10 | 分页参数，表示所请求页码元素数量。 |

**示例**

请求示例

```
GET /api/v2/namespaces/[namespace]/variables HTTP/1.1 &namespace=default-namespace
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "totalSize":1,
 "data":"[    {      \"description\": \"Created by VVP2 SDK\",      \"kind\": \"Encrypte
d\", \"name\": \"sls_access_id\", \"value\": \"******\" } ]",
 "pageIndex":1,
 "success":true,
 "requestId":"CBC799F0-AS7S-1D30-8A4F-882ED4DD****",
 "errorMessage":"",
 "errorCode":"",
 "pageSize":10,
 "httpCode":200
}
```

`XML` 格式

```xml
<totalSize>1</totalSize> <data>[
    {
      &quot;description&quot;: &quot;Created by VVP2 SDK&quot;,
      &quot;kind&quot;: &quot;Encrypted&quot;,
      &quot;name&quot;: &quot;sls_access_id&quot;,
      &quot;value&quot;: &quot;******&quot;
    }
  ]</data>
 <pageIndex>1</pageIndex>
 <success>true</success>
 <requestId>CBC799F0-AS7S-1D30-8A4F-882ED4DD****</requestId>
 <errorMessage  />
 <errorCode  />
 <pageSize>10</pageSize>
 <httpCode>200</httpCode>
```

实时计算（流计算） 参考

#### API示例

##### 示例

**注意事项**

凡是带有Resp的接口都要用固定的方式解析。所有put、post都要设置content-type以及使用自带的 JsonUtil序列化。

**示例代码**

```java
package sample; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.http.FormatType; import com.aliyuncs.profile.DefaultProfile; import com.aliyuncs.profile.IClientProfile; import com.aliyuncs.ververica.model.v20200501.*; import com.fasterxml.jackson.core.JsonProcessingException; import com.fasterxml.jackson.core.type.TypeReference; import com.ververica.common.model.ResultModel; import com.ververica.common.model.deployment.Artifact; import com.ververica.common.model.deployment.Deployment; import com.ververica.common.model.deployment.DeploymentState; import com.ververica.common.model.namespace.Namespace; import com.ververica.common.params.*; import com.ververica.common.resp.*; import com.ververica.common.util.JsonUtil; import com.ververica.common.util.SdkUtil; import java.util.List; public class SdkSample {
    /**
```

* 正常格式：

```
     * {
     * "requestId":"202008030937-4TFJR5MK2R",
```

`* "success": true, #`为`true`时，结果中仅展示`requestId`，`false`时会抛出`reason`和`message`

```
     * "message": "",
     * "reason": "",
```

`* "data":` 数据内容（`Object`）

```
     * }
```

`*/`

```
    public static void main(String[] args) throws JsonProcessingException, ClientExcepti
on {
        String regionId = "cn-hangzhou";
        DefaultProfile.addEndpoint(regionId, "ververica", "ververica-
share.aliyuncs.com");
        IClientProfile profile = DefaultProfile.getProfile(regionId, "**************", "
****************");
        DefaultAcsClient client = new DefaultAcsClient(profile);
        /**
```

实时计算（流计算） 参考目前支持以下4个`region`

```
         ververica-share.cn-hangzhou.aliyuncs.com
         ververica-share.cn-shanghai.aliyuncs.com
         ververica-share.cn-shenzhen.aliyuncs.com
         ververica-share.cn-beijing.aliyuncs.com
```

`*/`

```
        String deploymentId = "placeholder";
```

`//namespace/deploymentId`根据实际环境作业配置 `//` 获取`namespaces`列表

```java
        ListNamespacesRequest listNamespacesRequest = new ListNamespacesRequest();
        listNamespacesRequest.setSysVersion("2024-11-18");
        ResultModel<ListNamespacesResp> listNamespacesRespResultModel = JsonUtil.toBean(
SdkUtil.getHttpContentString(client, TypeReference<ResultModel<ListNamespacesResp>>() {
        });
        List<Namespace> namespaceList =
listNamespacesRespResultModel.getData().getNamespaces();
        System.out.println(JsonUtil.toJson(namespaceList));
        String workspaceName = namespaceList.get(0).getWorkspace();
        String namespace = namespaceList.get(0).getName();
        // 获取deployment
        GetDeploymentRequest getDeploymentRequest = new GetDeploymentRequest();
        getDeploymentRequest.setWorkspace(workspaceName);
        getDeploymentRequest.setNamespace(namespace);
        getDeploymentRequest.setDeploymentId(deploymentId);
        getDeploymentRequest.setSysVersion("2024-11-18");
        String data = client.doAction(getDeploymentRequest).getHttpContentString();
        System.out.println(data);
        ResultModel<GetDeploymentResp> getDeploymentRespResultModel =
JsonUtil.toBean(data, new TypeReference<ResultModel<GetDeploymentResp>>() {
        });
        Deployment deployment = getDeploymentRespResultModel.getData();
        deployment.getMetadata().getAnnotations().put("update-flag", "zdbox");
        deployment.getMetadata().getLabels().put("key2", "value2");
        deployment.getSpec().setState(DeploymentState.RUNNING);
```

`//` 更新`deployment`状态

```
        UpdateDeploymentDesiredStateParams updateDeploymentDesiredStateParams = new Upda
teDeploymentDesiredStateParams();
        updateDeploymentDesiredStateParams.setState(DeploymentState.CANCELLED);
UpdateDeploymentDesiredStateRequest();
        updateDeploymentDesiredStateRequest.setWorkspace(workspaceName);
        updateDeploymentDesiredStateRequest.setNamespace(namespace);
        updateDeploymentDesiredStateRequest.setDeploymentId(deploymentId);
updateDeploymentDesiredStateRequest.setParamsJson(JsonUtil.toJson(updateDeploymentDesiredS teParams));
        updateDeploymentDesiredStateRequest.setHttpContentType(FormatType.JSON);
        updateDeploymentDesiredStateRequest.setSysVersion("2024-11-18");
```

实时计算（流计算） 参考

```java
System.out.println(client.doAction(updateDeploymentDesiredStateRequest).getHttpContentStri ());
        ResultModel<UpdateDeploymentDesiredStateResp>
                updateDeploymentDesiredStateRespResultModel =
JsonUtil.toBean(client.doAction(updateDeploymentDesiredStateRequest).getHttpContentString
                        new TypeReference<ResultModel<UpdateDeploymentDesiredStateResp>>
() {
                        });
System.out.println(JsonUtil.toJson(updateDeploymentDesiredStateRespResultModel));
```

`// Create savepoint:`如果`data`为空，则说明触发失败，请查看`message`

```
        /**
```

* 成功包含`data`字段返回数据：`{"data":{"metadata":{"createdAt":"2020-08-`

```json
18T07:04:40.379926Z","jobId":"d0d6720f-00ac-47cc-8d54-7d88a4d7b446","modifiedAt":"2020- 08-18T07:04:40.379926Z","deploymentId":"0cb796fc-2641-488e-bde8- 52b2199c5747","origin":"USER_REQUEST","resourceVersion":1,"namespace":"test","annotations" {"com.dataartisans.appmanager.controller.deployment.spec.version":"4"},"id":"c4e40dc9-6 9c7-4ba0-8add-5f862ecb00ef"},"apiVersion":"v1","kind":"Savepoint","spec": {"savepointLocation":"oss://qiqi-zp/vvp/flinksavepoints/namespaces/test/deployments/0cb796fc-2641-488e-bde8-52b2199c5747/c4e40dc9-69 c7-4ba0-8add-5f862ecb00ef"},"status":{"state":"STARTED"}},"requestId":"188B1FFC-2729- 458E-A404-D3CD5D972DA0"}
```

* 失败无`data`字段，并且有`message`：`{"RequestId":"B545121D-ED4C-4E71-9D76-`

```
CBD510A04E5B","HostId":"ververica-share.cnshanghai.aliyuncs.com","Code":"BadRequest","Message":"No
         active job for a deployment."}
```

`*/`

```java
                createSavepointRequest = new CreateSavepointRequest();
        createSavepointRequest.setWorkspace(workspaceName);
        createSavepointRequest.setNamespace(namespace);
        CreateSavepointParams createSavepointParams
                = new CreateSavepointParams();
        createSavepointParams.setDeploymentId(deploymentId);
        createSavepointRequest.setParamsJson(JsonUtil.toJson(createSavepointParams));
        createSavepointRequest.setHttpContentType(FormatType.JSON);
        createSavepointRequest.setSysVersion("2024-11-18");
System.out.println(client.doAction(createSavepointRequest).getHttpContentString());
        ResultModel<CreateSavepointResp> savepoint =
JsonUtil.toBean(client.doAction(createSavepointRequest).getHttpContentString(),
                        new TypeReference<ResultModel<CreateSavepointResp>>() {
                        });
        System.out.println(JsonUtil.toJson(savepoint));
```

`//` 获取`savepoints`列表

```
        ListSavepointsRequest listSavepointsRequest
                = new
                ListSavepointsRequest();
        listSavepointsRequest.setWorkspace(workspaceName);
        listSavepointsRequest.setNamespace(namespace);
```

实时计算（流计算） 参考 p q p

```
(
```

p

```java
);
        listSavepointsRequest.setDeploymentId(deploymentId);
        listSavepointsRequest.setSysVersion("2024-11-18");
        ResultModel<ListSavepointsResp> savepoints =
JsonUtil.toBean(client.doAction(listSavepointsRequest).getHttpContentString(), new TypeReference<ResultModel<ListSavepointsResp>>() {
                });
        System.out.println(JsonUtil.toJson(savepoints.getData().getSavepoints()));
System.out.println(JsonUtil.toJson(savepoints.getData().getSavepoints().size()));
```

`//` 获取`jobs`列表

```java
        ListJobsRequest listJobsRequest = new ListJobsRequest();
        listJobsRequest.setWorkspace(workspaceName);
        listJobsRequest.setNamespace(namespace);
        listJobsRequest.setDeploymentId(deploymentId);
        listJobsRequest.setSysVersion("2024-11-18");
                JsonUtil.toBean(client.doAction(listJobsRequest).getHttpContentString(),
new TypeReference<ResultModel<ListJobsResp>>() {
                });
        System.out.println(JsonUtil.toJson(jobs.getData().getJobs()));
```

`//` 获取部署目标列表

```java
                listDeploymentTargetsRequest = new ListDeploymentTargetsRequest();
        listDeploymentTargetsRequest.setWorkspace(workspaceName);
        listDeploymentTargetsRequest.setNamespace(namespace);
        listDeploymentTargetsRequest.setSysVersion("2024-11-18");
        ResultModel<ListDeploymentTargetsResp> deploymentTargets =
JsonUtil.toBean(client.doAction(listDeploymentTargetsRequest).getHttpContentString(),
                        new TypeReference<ResultModel<ListDeploymentTargetsResp>>() {
                        });
System.out.println(JsonUtil.toJson(deploymentTargets.getData().getDeploymentTargets()));
```

`//sql`语法检查，成功则`validationResult`：`VALIDATION_RESULT_VALID_INSERT_QUERY`或者

```
VALIDATION_RESULT_VALID_DDL_STATEMENT，其他查看errorDetails
                validateSqlScriptRequest = new ValidateSqlScriptRequest();
        validateSqlScriptRequest.setWorkspace(workspaceName);
        validateSqlScriptRequest.setNamespace(namespace);
                validateSqlScriptParams = new ValidateSqlScriptParams();
        validateSqlScriptParams.setStatement("CREATE TABLE RANDOM_TABLE(`name` STRING) w
ith ('connector'='random','type'='random')"); validateSqlScriptRequest.setParamsJson(JsonUtil.toJson(validateSqlScriptParams));
        validateSqlScriptRequest.setHttpContentType(FormatType.JSON);
        validateSqlScriptRequest.setSysVersion("2024-11-18");
JsonUtil.toBean(SdkUtil.getHttpContentString(client,
```

实时计算（流计算） 参考

```java
TypeReference<ResultModel<ValidateSqlScriptResp>>() {
        });
        System.out.println(JsonUtil.toJson(validateSqlScriptRespResultModel));
```

`//` 执行`ddl`操作:如果成功data.result='RESULT_SUCCESS|RESULT_SUCCESS_WITH_ROWS',否则查

```java
看message
                executeSqlScriptRequest = new ExecuteSqlScriptRequest();
        executeSqlScriptRequest.setWorkspace(workspaceName);
        executeSqlScriptRequest.setNamespace(namespace);
        ExecuteSqlScriptParams executeSqlScriptParams
                = new
                ExecuteSqlScriptParams();
        executeSqlScriptParams.setStatement("create table abaaaa (a varchar) with ('conn
ector' = 'random', 'type' = 'random');");
        executeSqlScriptParams.setStatement("show tables;");
        executeSqlScriptRequest.setParamsJson(JsonUtil.toJson(executeSqlScriptParams));
        executeSqlScriptRequest.setHttpContentType(FormatType.JSON);
        executeSqlScriptRequest.setSysVersion("2024-11-18");
JsonUtil.toBean(client.doAction(executeSqlScriptRequest).getHttpContentString(),
                new TypeReference<ResultModel<ExecuteSqlScriptResp>>() {
                });
        System.out.println(JsonUtil.toJson(executeSqlScriptRespResultModel));
```

`//`创建`deployment(sql`作业)

```java
        GetGlobalDeploymentDefaultsRequest getGlobalDeploymentDefaultsRequest
                = new
                GetGlobalDeploymentDefaultsRequest();
        getGlobalDeploymentDefaultsRequest.setWorkspace(workspaceName);
        getGlobalDeploymentDefaultsRequest.setNamespace(namespace);
System.out.println(client.doAction(getGlobalDeploymentDefaultsRequest).getHttpContentStrin ));
        getGlobalDeploymentDefaultsRequest.setSysVersion("2024-11-18");
        ResultModel<GetGlobalDeploymentDefaultsResp> globalDefaults =
JsonUtil.toBean(client.doAction(getGlobalDeploymentDefaultsRequest).getHttpContentString()
                        new TypeReference<ResultModel<GetGlobalDeploymentDefaultsResp>>
() {
                        });
        System.out.println(JsonUtil.toJson(globalDefaults.getData()));
        Deployment.DeploymentSpec spec =
                globalDefaults.getData().getSpec();
        spec.setState(DeploymentState.RUNNING);
```

`// SQL`作业

```
        Artifact.SqlScriptArtifact
                sqlScriptArtifact = new
                Artifact.SqlScriptArtifact();
        sqlScriptArtifact.setSqlScript("INSERT INTO PRINT_TABLE SELECT /* comments */ UP
PER(name) FROM RANDOM_TABLE");
        spec.getTemplate().getSpec().setArtifact(sqlScriptArtifact);
```

实时计算（流计算） 参考 `//` 创建`DataStream`作业只需要传入不同的`Artifact`即可

```java
        Artifact.JarArtifact jarArtifact = new
                Artifact.JarArtifact();
        jarArtifact.setJarUri("oss://qiqi-zp/multioss/artifacts/namespaces/test/job-1.0-
SNAPSHOT2.jar");
        // spec.getTemplate().getSpec().setArtifact(jarArtifact);
                createDeploymentParams = new CreateDeploymentParams();
        Deployment.DeploymentMetadata metadata = new
                Deployment.DeploymentMetadata();
        metadata.setName("lxg-sdk-sql-test-5");
        spec.setDeploymentTargetId("3965ca94-2fa9-47ee-818b-ff89ddf4ba4f");
        createDeploymentParams.setMetadata(metadata);
        createDeploymentParams.setSpec(spec);
                createDeploymentRequest = new CreateDeploymentRequest();
        createDeploymentRequest.setWorkspace(workspaceName);
        createDeploymentRequest.setNamespace(namespace);
        String paramsStr = JsonUtil.toJson(createDeploymentParams);
        System.out.printf("##########params:\n%s\n", paramsStr);
        createDeploymentRequest.setParamsJson(paramsStr);
        createDeploymentRequest.setHttpContentType(FormatType.JSON);
        createDeploymentRequest.setSysVersion("2024-11-18");
System.out.println(client.doAction(createDeploymentRequest).getHttpContentString()); JsonUtil.toBean(client.doAction(createDeploymentRequest).getHttpContentString(),
                new TypeReference<ResultModel<CreateDeploymentResp>>() {
                });
        System.out.println(JsonUtil.toJson(createDeploymentRespResultModel));
```

`//` 获取`artifacts`列表

```java
        ListArtifactsRequest listArtifactsRequest = new
                ListArtifactsRequest();
        listArtifactsRequest.setWorkspace(workspaceName);
        listArtifactsRequest.setNamespace(namespace);
        listArtifactsRequest.setSysVersion("2024-11-18");
JsonUtil.toBean(client.doAction(listArtifactsRequest).getHttpContentString(), new TypeReference<ResultModel<ListArtifactsResp>>() {
                });
        System.out.println(JsonUtil.toJson(artifacts));
```

`//` 获取`artifact`

```java
                getArtifactMetadataRequest = new GetArtifactMetadataRequest();
        getArtifactMetadataRequest.setWorkspace(workspaceName);
        getArtifactMetadataRequest.setNamespace(namespace);
        getArtifactMetadataRequest.setFilename("flip-75-demo-1.0-SNAPSHOT-1.jar");
        getArtifactMetadataRequest.setSysVersion("2024-11-18");
System.out.println(client.doAction(getArtifactMetadataRequest).getHttpContentString());
        ResultModel<GetArtifactMetadataResp> artifact =
```

实时计算（流计算） 参考

```java
JsonUtil.toBean(client.doAction(getArtifactMetadataRequest).getHttpContentString(),
                        new TypeReference<ResultModel<GetArtifactMetadataResp>>() {
                        });
        System.out.println(JsonUtil.toJson(artifact));
```

`//` 删除`artifact`

```java
        DeleteArtifactRequest deleteArtifactRequest
                = new
                DeleteArtifactRequest();
        deleteArtifactRequest.setWorkspace(workspaceName);
        deleteArtifactRequest.setNamespace(namespace);
        deleteArtifactRequest.setFilename("flip-75-demo-1.0-SNAPSHOT-1.jar");
        deleteArtifactRequest.setSysVersion("2024-11-18");
                deleteArtifactResponse = client.getAcsResponse(deleteArtifactRequest);
        System.out.println(JsonUtil.toJson(deleteArtifactResponse));
```

`//` 获取`deployments`列表

```java
        ListDeploymentsRequest listDeploymentsRequest
                = new
                ListDeploymentsRequest();
        listDeploymentsRequest.setWorkspace(workspaceName);
        listDeploymentsRequest.setNamespace(namespace);
        listDeploymentsRequest.setSysVersion("2024-11-18");
        ResultModel<ListDeploymentsResp> deployments =
JsonUtil.toBean(client.doAction(listDeploymentsRequest).getHttpContentString(),
                        new TypeReference<ResultModel<ListDeploymentsResp>>() {
                        });
        System.out.println(JsonUtil.toJson(deployments));
```

`//` 删除`deployment` 指定已存在的且状态为`CANCELLED`的`DeploymentId`

```java
                deleteDeploymentRequest = new DeleteDeploymentRequest();
        deleteDeploymentRequest.setWorkspace(workspaceName);
        deleteDeploymentRequest.setNamespace(namespace);
        deleteDeploymentRequest.setDeploymentId(deploymentId);
        deleteDeploymentRequest.setSysVersion("2024-11-18");
client.getAcsResponse(deleteDeploymentRequest);
        System.out.println(JsonUtil.toJson(deleteDeploymentResponse));
    }
}
```

**说明**

详细的调用示例代码建议联系阿里云技术支持获取。

##### pom.xml

```xml
<?xml version="1.0" encoding="UTF-8"?> <project xmlns="http://maven.apache.org/POM/4.0.0"
```

实时计算（流计算） 参考

```xml
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://maven.apache.org/POM/4.0.0
http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <groupId>com.aliyun</groupId>
    <artifactId>vvp-sdk-sample-java</artifactId>
    <version>0.0.1</version>
    <properties>
        <junit.version>4.12</junit.version>
        <slf4j.version>1.7.25</slf4j.version>
    </properties>
    <dependencies>
        <dependency>
            <groupId>com.aliyun</groupId>
            <artifactId>aliyun-java-sdk-core</artifactId>
            <version>4.5.3</version>
        </dependency>
        <dependency>
            <groupId>org.slf4j</groupId>
            <artifactId>slf4j-api</artifactId>
            <version>1.7.25</version>
        </dependency>
        <dependency>
            <groupId>org.slf4j</groupId>
            <artifactId>slf4j-log4j12</artifactId>
            <version>1.7.25</version>
        </dependency>
        <dependency>
            <groupId>com.aliyun</groupId>
            <artifactId>aliyun-java-sdk-ververica</artifactId>
            <version>0.0.3-SNAPSHOT</version>
            <classifier>shaded</classifier>
        </dependency>
</dependencies>
    <build>
        <plugins>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-compiler-plugin</artifactId>
                <version>3.1</version>
                <configuration>
                    <source>8</source>
                    <target>8</target>
                </configuration>
            </plugin>
        </plugins>
    </build>
</project>
```

实时计算（流计算） 参考

## SQL开发参考

### 概述

Flink SQL是实时计算为简化实时计算模型，降低用户使用实时计算门槛而设计的一套符合标准SQL语义的实时计算SQL。Flink SQL有以下优势： 开发成本低。使用阿里云Flink SQL，可以不再编写长达数千行的Storm代码，通过一两句简单的SQL即可描述复杂且多变的业务逻辑。 维护成本低。使用阿里云Flink SQL，可以不用再维护数千行的Storm代码。 使用最原始的Storm编程模式，您必须考虑各类系统异常情况，包括系统异常、系统宕机、错误情况下数据准确性等各类细节问题。 阿里云团队将上述各类问题均在SQL语义中进行抽象和解决。实时计算具备以下特点。 数据的准确性。实时计算独特的Exactly-Once Processing语义保证，能够保证各种Failover场景的数据准确性。 性能的可优化性。实时计算集成SQL优化逻辑，将SQL翻译为最底层的执行代码的普通人员编写的Storm 代码，效率更高，提高编写SQL代码的效率。 编程的可扩展性。实时计算支持UFD的扩展功能，对于SQL无法表达的、或者业务定制化逻辑，阿里实时计算通过自定义UFD进行功能扩展。 系统的可扩展性。实时计算在保证任务和系统稳定性同时，在数据突增时（如，双11）可以做到弹性扩容。

### 关键字

本文为您介绍Flink关键字。 Flink V1.11关键字详情，请参见Reserved Keywords。

|  | 说明如果您需要在DDL中定义Flink关键字，请在关键字两端添加反引号（`），例如 ｀value ｀ 。 |
|---|---|
|  | ｀ |

### 创建数据视图

**背景信息**

通常，业务逻辑比较复杂，需要将多层嵌套写在DML语句中，但是这种方式定位问题比较困难。此时，您可以通过定义数据视图的方式，将多层嵌套写在数据视图中，简化开发过程。 数据视图仅用于辅助计算逻辑的描述，不会产生数据的物理存储。

**说明**

**语法**

```
CREATE TEMPORARY VIEW viewName AS [ (columnName[ , columnName]* ) ] queryStatement;
```

viewName：视图名称。 columnName：字段名称。 queryStatement：嵌套语句别名。

**示例**

实时计算（流计算） 参考

```
CREATE TEMPORARY VIEW tmp_view AS SELECT
```

*

```
FROM
    datagen_source;
    rds_output
SELECT
```

`r,` `t,` `c,` u

```
FROM
    tmp_view;
```

### 基本概念

#### Watermark

实时计算可以基于时间属性对数据进行窗口聚合。基于Event Time时间属性的窗口函数作业中，数据源表 WATERMARK 定义了表的事件时间属性，其形式为WATERMARK FOR rowtime_column_name ASwatermark_strategy_expression。rowtime_column_name把一个现有的列定义为一个为表标记事件时间的属性。该列的类型必须为 TIMESTAMP(3)，且是 schema 中的顶层列，它也可以是一个计算列。 watermark_strategy_expression定义了watermark的生成策略。它允许使用包括计算列在内的任意非查询表达式来计算watermark，表达式的返回类型必须是TIMESTAMP(3)，表示了从Epoch以来的经过的时间。返回的watermark只有当其不为空且其值大于之前发出的本地watermark时才会被发出（以保证 watermark 递增）。每条记录的watermark生成表达式计算都会由框架完成。框架会定期发出所生成的最大的watermark，如果当前watermark仍然与前一个watermark相同、为空、或返回的 watermark 的值小于最后一个发出的watermark，则新的 watermark不会被发出。Watermark根据pipeline.autowatermark-interval中所配置的间隔发出。若watermark的间隔是0ms，那么每条记录都会产生一个 watermark，且watermark会在不为空并大于上一个发出的watermark时发出。 使用事件时间语义时，表必须包含事件时间属性和 watermark 策略。Flink提供了几种常用的watermark 策略： 严格递增时间戳：WATERMARK FOR rowtime_column AS rowtime_column。 发出到目前为止已观察到的最大时间戳的watermark，时间戳大于最大时间戳的行被认为没有迟到。 递增时间戳：WATERMARK FOR rowtime_column AS rowtime_column -INTERVAL '0.001' SECOND。 发出到目前为止已观察到的最大时间戳减1的watermark，时间戳大于或等于最大时间戳的行被认为没有迟到。 有界乱序时间戳：WATERMARK FOR rowtime_column AS rowtime_column- INTERVAL 'string' timeUnit。 发出到目前为止已观察到的最大时间戳减去指定延迟的watermark，例如， WATERMARK FOR rowtime_column AS rowtime_column - INTERVAL '5'SECOND是一个5秒延迟的watermark策略。 实时计算（流计算） 参考

```
CREATE TABLE Orders (
 user BIGINT,
 product STRING,
 order_time TIMESTAMP(3),
 WATERMARK FOR order_time AS order_time -INTERVAL '5' SECOND
) WITH ( . . . );
```

Watermark含义是所有时间戳 `t'< t` 的事件都已经发生。假如watermark t 已经生效，那么后续 Event Time小于 t 的记录都会被丢弃掉（目前实时计算的处理方式是丢弃这些来的更晚的数据，后续支持用户配置让更晚的数据也能继续更新）。 针对乱序的流，watermark至关重要。即使一些事件延迟到达，也不至于过于影响窗口计算的正确性。 并行数据流中，当算子（Operator）有多个输入流时，算子的Event Time以最小流Event Time为准。

#### 计算列

计算列可以使用其它列的数据，计算出其所属列的数值。如果您的数据源表中没有TIMESTAMP类型的列， 可以使用计算列方法从其它类型的字段进行转换。

**计算列概念**

计算列是虚拟列，并非实际存储在表中。计算列可以通过表达式、内置函数、或是自定义函数等方式，使用其它列的数据，计算出其所属列的数值。计算列在Flink SQL中可以像普通字段一样被使用。

**计算列的用途**

目前Watermark的Event Time（也称为rowtime）列只支持TIMESTAMP类型（未来会支持LONG类型）。watermark只能定义在源表DDL中，如果您的源表中没有TIMESTAMP类型的列，可以使用计算列从其他类型的字段进行转换。

**计算列语法**

```
column_name AS computed_column_expression
```

**计算列示例**

watermark的rowtime必须是TIMESTAMP数据类型。当前实时计算支持毫秒级别的、在Unix时间戳里是 13位TIMESTAMP数据类型。如果DataHub的TIME字段是微秒级别的（16位Unix时间戳），可以用计算列方法转换为13位的时间戳，如下所示。 实时计算（流计算） 参考

```
CREATE TABLE test_stream(
  a INT,
  b BIGINT,
  `TIME` BIGINT,
```

`ts AS TO_TIMESTAMP(TIME/1000), --`利用计算列，将`16`位时间戳转换为`13`位时间戳。

```
) WITH (
  'connector' = 'datahub',
  ...
);
```

| TIME |  | 包 |
|---|---|---|
| 型的 | ts |  |

#### 时间属性

本文为您介绍Flink SQL支持的Event Time和Processing Time数据类型。 Flink SQL支持2种时间类型Event Time和Processing Time。 Event Time：您提供的事件时间（通常是数据的最原始的创建时间），Event time必须是您提供在 Schema里的数据。 Processing Time：系统对事件进行处理的本地系统时间。 下图是不同时间属性在实时计算流程中的位置。 从上图的定义可以看出，Ingestion Time和Processing Time是系统为流式记录增加的时间属性，您并不能控制。Event Time则是流记录本身携带的时间属性。由于数据本身存在乱序以及网络抖动等其它原因，Event Time为t1（对应partition1）时刻的纪录，有可能会晚于t2（对应prtition2）时刻的被Flink处理，即t2 > t1。

**Event Time**

EventTime也称为rowtime。EventTime时间属性必须在源表DDL中声明，可以将源表中的某一字段声明成 EventTime。目前只支持将TIMESTAMP类型（将来会支持 LONG 类型）声明成rowtime字段。如果不是TIMESTAMP类型，需要借助计算列，基于现有列构造出一个TIMESTAMP类型的列。 但由于数据本身会有乱序，加之网络抖动或其它原因，数据到达的顺序和被处理的顺序可能是不一致的（乱序）。因此定义一个rowtime字段，需要显示地定义一个Watermark计算方法。 窗口函数基于Event Time聚合的示例如下。 实时计算（流计算） 参考

```
CREATE TABLE tt_stream(
  a VARCHAR,
  b VARCHAR,
  c TIMESTAMP,
  WATERMARK wk1 FOR c as withOffset(c, 1000)  --watermark计算方法
) WITH (
  'connector' = 'sls',
  'topic' = 'yourTopicName',
  'accessId' = 'yourAccessId',
  'accessKey' = 'yourAccessSecret'
); CREATE TABLE rds_output(
  id VARCHAR,
  c TIMESTAMP,
  f TIMESTAMP,
  cnt BIGINT
) WITH (
  'connector' = 'rds',
  'url' = 'jdbc:mysql://****3306/test',
  'tableName' = 'yourTableName',
  'userName' = 'yourUserName',
  'password' = 'yourPassword'
); INSERT INTO rds_output SELECT a AS id,
     SESSION_START(c, INTERVAL '1' SECOND) AS c,
     CAST(SESSION_END(c, INTERVAL '1' SECOND) AS TIMESTAMP) AS f,
     COUNT(a) AS cnt
FROM tt_stream GROUP BY SESSION(c, INTERVAL '1' SECOND), a
```

**Processing Time**

Processing Time是系统产生的，不在您的原始数据中，您需要在数据源表的声明中显式的定义一个 Processing Time列。

```
filedName as PROCTIME()
```

窗口函数基于Processing Time聚合的示例如下。 实时计算（流计算） 参考

```
CREATE TABLE mq_stream (
  a VARCHAR,
  b VARCHAR,
  c BIGINT,
```

`d AS PROCTIME() ---`在数据源表的声明中显式的定义一个`Processing Time`列。

```
) WITH (
  'connector' = 'mq',
  'topic' = 'yourTopic',
  'accessId' = 'yourAccessId',
  'accessKey' = 'yourAccessSecret'
); CREATE TABLE rds_output (
  id VARCHAR,
  c TIMESTAMP,
  f TIMESTAMP,
  cnt BIGINT
) with (
  'connector' = 'rds',
  'url' = 'yourDatebaseURL',
  'tableName' = 'yourDatabasTableName',
  'userName' = 'yourUserName',
  'password' = 'yourPassword'
); INSERT INTO rds_output SELECT a AS id,
     SESSION_START(d, INTERVAL '1' SECOND) AS c,
     SESSION_END(d, INTERVAL '1' SECOND) AS f,
     COUNT(a) AS cnt
FROM mq_stream GROUP BY SESSION(d, INTERVAL '1' SECOND), a
```

**时间属性字段传递**

目前，时间属性字段经过如下两种操作后会失去时间属性： 非window的group by 双流join 如果经过以上两种操作后，继续使用该时间属性字段进行窗口函数运算会出现类

```
似 org.apache.flink.table.api.ValidationException: Window can only be defined over a time
```

`attribute column.` 的报错。

### DML语句

#### INSERT INTO语句

本文为您介绍如何在一个作业中写入一个Sink或多个Sink。

**写入一个Sink示例**

源表实时计算（流计算） 参考

```
  name VARCHAR,
  score BIGINT
) WITH ( );
```

结果表

```
  name VARCHAR,
  score BIGINT
) WITH ( );
```

DML

```
INSERT INTO blackhole_sink SELECT UPPER(name), score FROM datagen_source;
```

**写入多个Sink示例**

源表

```
  name VARCHAR,
  score BIGINT
) WITH ( );
```

结果表A

```
  name VARCHAR,
  score BIGINT
) WITH ( );
```

结果表B

```
  name VARCHAR,
  score BIGINT
) WITH ( );
```

DML 本文以写入两个Sink为例进行介绍。 实时计算（流计算） 参考 BEGIN STATEMENT SET; --写入多个`Sink`时，必填。

```
  SELECT UPPER(name), sum(score)
  GROUP BY UPPER(name);
  SELECT LOWER(name), max(score)
  GROUP BY LOWER(name);
```

END; --写入多个`Sink`时，必填。 写入多个Sink语句时，需要以**BEGIN STATEMENT SET;**开头，以**END;**结尾。

**说明**

### QUERY语句

### 窗口函数

#### 概述

本文为您介绍Flink SQL支持的窗口函数以及窗口函数支持的时间属性和窗口类型。

### 窗口函数

窗口函数Flink SQL支持基于无限大窗口的聚合（无需在SQL Query中，显式定义任何窗口）以及对一个特定的窗口的聚合。例如，需要统计在过去的1分钟内有多少用户点击了某个的网页，可以通过定义一个窗口来收集最近1分钟内的数据，并对这个窗口内的数据进行计算。 Flink SQL支持的窗口聚合主要是两种：Window聚合和Over聚合。本文档主要为您介绍Window聚合。 Window聚合支持Event Time和Processing Time两种时间属性定义窗口。每种时间属性类型支持三种窗口类型：滚动窗口（TUMBLE）、滑动窗口（HOP）和会话窗口（SESSION）。

#### 时间属性

Flink SQL支持以下两种时间属性。Flink可以基于这两种时间属性对数据进行窗口聚合。 Event Time：您提供的事件时间（通常是数据的最原始的创建时间），Event Time一定是您提供在 Schema里的数据。 Processing Time：对事件进行处理的本地系统时间。 Flink时间属性详情，请参见时间属性。

**说明**

**级联窗口**

| 数值 | TUMBLE ROWTIME _ |  |
|---|---|---|
|  | max(rowtime) | 作 。 |
| window end - 1 _ |  |  |

示例逻辑为：基于1分钟的滚动窗口聚合结果，进行1小时的滚动窗口聚合，可以满足您的多维度开窗需求。 实时计算（流计算） 参考

```
CREATE TEMPORARY TABLE user_clicks(
  username varchar,
  click_url varchar,
  eventtime varchar,
  ts AS TO_TIMESTAMP(eventtime),
  WATERMARK FOR ts AS ts - INTERVAL '2' SECOND  --为Rowtime定义Watermark。
) with (
  'connector'='sls',
  ...
); CREATE TEMPORARY TABLE tumble_output(
  window_start TIMESTAMP,
  window_end TIMESTAMP,
  username VARCHAR,
  clicks BIGINT
) with (
```

`'connector'='datahub' --`目前`SLS`只支持输出`VARCHAR`类型的`DDL`，所以使用`DataHub`存储。

```
  ...
); CREATE TEMPORARY VIEW one_minute_window_output AS SELECT
  TUMBLE_ROWTIME(ts, INTERVAL '1' MINUTE) as rowtime,  --使用TUMBLE_ROWTIME作为二级Window
```

的聚合时间。

```
  username,
  COUNT(click_url) as cnt
FROM user_clicks GROUP BY TUMBLE(ts, INTERVAL '1' MINUTE),username; BEGIN statement set; INSERT INTO tumble_output SELECT
  TUMBLE_START(rowtime, INTERVAL '1' HOUR),
  TUMBLE_END(rowtime, INTERVAL '1' HOUR),
  username,
  SUM(cnt)
FROM one_minute_window_output GROUP BY TUMBLE(rowtime, INTERVAL '1' HOUR), username; END;
```

#### 滚动窗口

本文为您介绍如何使用Flink滚动窗口函数。

**定义**

实时计算（流计算） 参考滚动窗口（TUMBLE）将每个元素分配到一个指定大小的窗口中。通常，滚动窗口有一个固定的大小，并且不会出现重叠。例如，如果指定了一个5分钟大小的滚动窗口，无限流的数据会根据时间划分为 `[0:00,` `0:05)` 、 `[0:05, 0:10)` 、 `[0:10, 0:15)` 等窗口。下图展示了一个30秒的滚动窗口。

**语法**

TUMBLE函数用在GROUP BY子句中，用来定义滚动窗口。

```xml
TUMBLE(<time-attr>, <size-interval>) <size-interval>: INTERVAL 'string' timeUnit
```

**说明**

`<time-attr>` 参数必须是时间流中的一个合法的时间属性字段，指定为Processing Time或Event Time，请参见概述，了解如何定义时间属性。

**标识函数**

使用标识函数选出窗口的起始时间或者结束时间，窗口的时间属性用于下级Window的聚合。

| 窗口标识函数 |  | 返回类型 | 描述 |
|---|---|---|---|
| TUMBLE START(time- _ |  | TIMESTAMP | 返回窗口的起始时间（包含边界）。例如 [00:10,00:15) 窗口，返回 00:10 。 |
|  | TUMBLE START(time- _ |  |  |
| attr, size- |  |  |  |
| interval) |  |  |  |

实时计算（流计算） 参考

| TUMBLE END(time- _ |  |  |  | 返回窗口的结束时间（包含边界）。例如 [00:00, 00:15] 窗口，返回 00:15 。 |  |  |
|---|---|---|---|---|---|---|
|  | TUMBLE END(time- _ |  |  |  |  |  |
| attr, size- |  |  |  |  |  |  |
|  |  | TIMESTAMP |  | 00:15] |  |  |
| interval) |  |  |  |  |  |  |
| TUMBLE ROWTIME(tim _ |  |  |  | 返回窗口的结束时间（不包含边界）。例如 [00:00, 00:15] 窗口，返回 00:14:59.999 。返回值是一个rowtime attribute，即可以基于该字段进行时间属性的操作，例如，级联窗口只能用在基于Event Time的 Window上，详情请参见级联窗口。 |  |  |
|  |  |  |  |  | [00:00, |  |
|  | TUMBLE ROWTIME(tim _ | TIMESTAMP(rowtime- |  |  |  |  |
|  |  |  | time- | 00:15] |  |  |
| e-attr, size- |  | T |  |  |  |  |
|  |  | a |  |  |  |  |
| interval) |  |  |  |  |  |  |
| TUMBLE PROCTIME(ti _ |  |  |  | 返回窗口的结束时间（不包含边界）。例如 [00:00, 00:15] 窗口，返回 00:14:59.999 。返回值是一个Proctime Attribute，即可以基于该字段进行时间属性的操作。例如，级联窗口只能用在基于Processing Time 的Window上，详情请参见级联窗口。 |  |  |
|  |  |  |  |  | [00:00, |  |
|  | TUMBLE PROCTIME(ti _ | TIMESTAMP(rowtime- |  |  |  |  |
|  |  |  | time- | 00:15] |  |  |
| me-attr, size- |  | TI |  |  |  |  |
|  |  | at |  |  |  |  |
| interval) |  |  |  |  |  |  |

**使用Event Time统计每个用户每分钟在指定网站的单击数示例**

测试数据

| username（VARCHAR） | click url（VARCHAR） _ | ts（TIMESTAMP） |
|---|---|---|
| Jark | http://taobao.com/xxx | 2017-10-10 10:00:00.0 |
| Jark | http://taobao.com/xxx | 2017-10-10 10:00:10.0 |
| Jark | http://taobao.com/xxx | 2017-10-10 10:00:49.0 |
| Jark | http://taobao.com/xxx | 2017-10-10 10:01:05.0 |
| Jark | http://taobao.com/xxx | 2017-10-10 10:01:58.0 |
| Timo | http://taobao.com/xxx | 2017-10-10 10:02:10.0 |

测试语句实时计算（流计算） 参考

```
CREATE TEMPORARY TABLE user_clicks(
  username varchar,
  click_url varchar,
  eventtime varchar,
  ts AS TO_TIMESTAMP(eventtime),
  WATERMARK FOR ts AS ts - INTERVAL '2' SECOND  --为Rowtime定义Watermark。
) with (
  'connector'='sls',
  ...
); CREATE TEMPORARY TABLE tumble_output(
  window_start TIMESTAMP,
  window_end TIMESTAMP,
  username VARCHAR,
  clicks BIGINT
) with (
```

`'connector'='datahub' --`目前`SLS`只支持输出`VARCHAR`类型的`DDL`，所以使用`DataHub`存储。

```
  ...
); INSERT INTO tumble_output SELECT TUMBLE_START(ts, INTERVAL '1' MINUTE) as window_start, TUMBLE_END(ts, INTERVAL '1' MINUTE) as window_end, username, COUNT(click_url) FROM user_clicks GROUP BY TUMBLE(ts, INTERVAL '1' MINUTE),username;
```

测试结果

|  | window start _ （TIMESTAMP） |  |  |  | window end _ （TIMESTAMP） |  |  | username（VARCHA R） | clicks（BIGINT） |
|---|---|---|---|---|---|---|---|---|---|
|  | 2017-10-10 |  |  |  |  |  |  | Jark | 3 |
|  |  | 2017-10-10 |  |  |  |  | 2017-10-10 | Jar |  |
|  | 10:00:00.0 |  |  |  |  |  |  |  |  |
|  |  |  |  |  | 10:01:00.0 |  |  |  |  |
|  | 2017-10-10 |  |  |  |  |  |  | Jark | 2 |
|  |  | 2017-10-10 |  |  |  |  | 2017-10-10 | Jar |  |
|  | 10:01:00.0 |  |  |  |  |  |  |  |  |
|  |  |  |  |  | 10:02:00.0 |  |  |  |  |
|  | 2017-10-10 |  |  |  |  |  |  | Timo | 1 |
|  |  | 2017-10-10 |  |  |  |  | 2017-10-10 | Ti |  |
|  | 10:02:00.0 |  |  |  |  |  |  |  |  |
|  |  |  |  |  | 10:03:00.0 |  |  |  |  |

**使用Processing Time统计每个用户每分钟在指定网站的单击数示例**

测试数据

| username （VARCHAR） | click url（VARCHAR） _ |
|---|---|

实时计算（流计算） 参考

| Jark | http://taobao.com/xxx |
|---|---|
| Jark | http://taobao.com/xxx |
| Jark | http://taobao.com/xxx |
| Jark | http://taobao.com/xxx |
| Jark | http://taobao.com/xxx |
| Timo | http://taobao.com/xxx |

测试语句

```
CREATE TEMPORARY TABLE window_test (
  username   VARCHAR,
  click_url  VARCHAR,
  ts as PROCTIME()
) WITH (
  'connector'='sls',
  ...
); CREATE TEMPORARY TABLE tumble_output(
  window_start TIMESTAMP,
  window_end TIMESTAMP,
  username VARCHAR,
  clicks BIGINT
) with (
```

`'connector'='datahub' --`目前`SLS`只支持输出`VARCHAR`类型的`DDL`，所以使用`DataHub`存储。

```
  ...
); INSERT INTO tumble_output SELECT TUMBLE_START(ts, INTERVAL '1' MINUTE), TUMBLE_END(ts, INTERVAL '1' MINUTE), username, COUNT(click_url) FROM window_test GROUP BY TUMBLE(ts, INTERVAL '1' MINUTE), username;
```

测试结果

| window start _ （TIMESTAMP） | window end _ （TIMESTAMP） | username （VARCHAR） | clicks（BIGINT） |
|---|---|---|---|

实时计算（流计算） 参考

|  | 2019-04-11 |  |  |  |  |  |  |  |  | Jark | 5 |
|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  | 2019-04-11 |  |  |  |  | 20 | 19-04-11 |  | Jark |  |
|  | 14:43:00.0 |  |  |  |  |  |  |  |  |  |  |
|  |  |  | 00 |  |  | 14:44:00.000 |  |  |  |  |  |
|  | 2019-04-11 |  |  |  |  |  |  |  |  | Timo | 1 |
|  |  | 2019-04-11 |  |  |  |  | 201 |  | 9-04-11 | Timo |  |
|  | 14:43:00.0 |  |  |  |  |  |  |  |  |  |  |
|  |  |  | 00 |  |  | 14:44:00.000 |  |  |  |  |  |

#### 滑动窗口

本文为您介绍如何使用Flink滑动窗口函数。

**定义**

滑动窗口（HOP），也被称作Sliding Window。不同于滚动窗口，滑动窗口的窗口可以重叠。 滑动窗口有两个参数：**slide**和**size**。**slide**为每次滑动的步长，**size**为窗口的大小。
**slide < size**，则窗口会重叠，每个元素会被分配到多个窗口。
**slide = size**，则等同于滚动窗口（TUMBLE）。
**slide > size**，则为跳跃窗口，窗口之间不重叠且有间隙。
通常，大部分元素符合多个窗口情景，窗口是重叠的。因此，滑动窗口在计算移动平均数（moving averages）时很实用。例如，计算过去5分钟数据的平均值，每10秒钟更新一次，可以设置**slide**为10秒，**size**为5分钟。下图为您展示间隔为30秒，窗口大小为1分钟的滑动窗口。

**函数语法**

HOP函数用在GROUP BY子句中，用来定义滑动窗口。 实时计算（流计算） 参考

```xml
HOP(<time-attr>, <slide-interval>,<size-interval>) <slide-interval>: INTERVAL 'string' timeUnit <size-interval>: INTERVAL 'string' timeUnit
```

**说明**

`<time-attr>` 参数必须是流中的一个合法的时间属性字段，指定为Processing Time或Event Time。请参见概述，了解如何定义时间属性。

**标识函数**

使用滑动窗口标识函数选出窗口的起始时间或者结束时间，窗口的时间属性用于下级Window的聚合。

| 窗口标识函数 |  | 返回类型 |  | 描述 |  |  |  |  |
|---|---|---|---|---|---|---|---|---|
| HOP START（<time- _ |  |  |  | 返回窗口的起始时间（包含边界）。例如 [00:10, 00:15) 窗口，返回 00:10 。 |  |  |  |  |
|  | HOP START（<time- _ |  |  |  |  |  |  |  |
| attr>, <slide- |  |  |  |  |  |  |  |  |
|  |  | TIMESTAMP |  |  |  |  |  |  |
|  |  | TIMESTA |  | 00:15) |  |  |  |  |
| interval>, <size- |  |  |  |  |  |  |  |  |
| interval>） |  |  |  |  |  |  |  |  |
| HOP END（<time- _ |  |  |  | 返回窗口的结束时间（包含边界）。例如 [00:00, 00:15) 窗口，返回 00:15 。 |  |  |  |  |
|  | HOP END（<time- _ |  |  |  |  |  |  |  |
| attr>, <slide- |  |  |  |  |  |  |  |  |
|  |  | TIMESTAMP |  |  |  |  |  |  |
|  |  | TIMESTA |  | 00:15) |  |  |  |  |
| interval>, <size- |  |  |  |  |  |  |  |  |
| interval>） |  |  |  |  |  |  |  |  |
| HOP ROWTIME（<time- _ |  |  |  | 返回窗口的结束时间（不包含边界）。例如 [00:00, |  |  |  |  |
|  | HOP ROWTIME（<time- _ |  |  | 返回窗口的结束时间（不 |  |  | [00:00, |  |
| attr>, <slide- |  | TIMESTAMP（ro | wtime- | 00:15) |  | 00:14:59.999 |  |  |
| interval>, <size- |  | attr） |  |  |  |  |  |  |
| interval>） |  |  |  |  |  |  |  |  |
| HOP PROCTIME（<time _ |  |  |  | 返回窗口的结束时间（不包含边界）。例如 [00:00, |  |  |  |  |
|  | HOP PROCTIME（<time _ |  |  | 返回窗口的结束时间（不包 |  |  | [00:00, |  |
| -attr>, <slide- |  | TIMESTAMP（ro | wtime- |  | 00:15) |  |  |  |
| interval>, <size- |  | attr） |  |  |  |  |  |  |
| interval>） |  |  |  |  |  |  |  |  |

| [00:10, |  |
|---|---|

| [00:00, |  |
|---|---|

**示例**

统计每个用户过去1分钟的单击次数，每30秒更新1次，即1分钟的窗口，30秒滑动1次。 测试数据

| username（VARCHAR） | click url（VARCHAR） _ | ts（TIMESTAMP） |
|---|---|---|
| Jark | http://taobao.com/xxx | 2017-10-10 10:00:00.0 |

实时计算（流计算） 参考

| Jark | http://taobao.com/xxx | 2017-10-10 10:00:10.0 |
|---|---|---|
| Jark | http://taobao.com/xxx | 2017-10-10 10:00:49.0 |
| Jark | http://taobao.com/xxx | 2017-10-10 10:01:05.0 |
| Jark | http://taobao.com/xxx | 2017-10-10 10:01:58.0 |
| Timo | http://taobao.com/xxx | 2017-10-10 10:02:10.0 |

测试语句

```
CREATE TEMPORARY TABLE user_clicks (
  username VARCHAR,
  click_url VARCHAR,
  eventtime VARCHAR,
  ts AS TO_TIMESTAMP(eventtime),
  WATERMARK FOR ts AS ts - INTERVAL '2' SECOND  --为Rowtime定义Watermark。
) with (
  'connector'='sls',
  ...
); CREATE TEMPORARY TABLE hop_output (
  window_start TIMESTAMP,
  window_end TIMESTAMP,
  username VARCHAR,
  clicks BIGINT
) with (
```

`'connector'='datahub' --`目前`SLS`只支持输出`VARCHAR`类型的`DDL`，所以使用`DataHub`存储。

```
  ...
);
    hop_output
SELECT
    HOP_START (ts, INTERVAL '30' SECOND, INTERVAL '1' MINUTE),
    HOP_END (ts, INTERVAL '30' SECOND, INTERVAL '1' MINUTE),
    username,
    COUNT (click_url)
FROM
    user_clicks
GROUP BY
    HOP (ts, INTERVAL '30' SECOND, INTERVAL '1' MINUTE),username;
```

测试结果实时计算（流计算） 参考

|  | window start _ （TIMESTAMP） |  |  |  | window end _ （TIMESTAMP） |  |  | username （VARCHAR） | clicks （BIGINT） |
|---|---|---|---|---|---|---|---|---|---|
|  | 2017-10-10 |  |  |  |  |  |  | Jark | 2 |
|  |  | 2017-10-10 |  |  |  |  | 2017-10-10 | Jar |  |
|  | 09:59:30.0 |  |  |  |  |  |  |  |  |
|  |  |  |  |  | 10:00:30.0 |  |  |  |  |
|  | 2017-10-10 |  |  |  |  |  |  | Jark | 3 |
|  |  | 2017-10-10 |  |  |  |  | 2017-10-10 | Jar |  |
|  | 10:00:00.0 |  |  |  |  |  |  |  |  |
|  |  |  |  |  | 10:01:00.0 |  |  |  |  |
|  | 2017-10-10 |  |  |  |  |  |  | Jark | 2 |
|  |  | 2017-10-10 |  |  |  |  | 2017-10-10 | Jar |  |
|  | 10:00:30.0 |  |  |  |  |  |  |  |  |
|  |  |  |  |  | 10:01:30.0 |  |  |  |  |
|  | 2017-10-10 |  |  |  |  |  |  | Jark | 2 |
|  |  | 2017-10-10 |  |  |  |  | 2017-10-10 | Jar |  |
|  | 10:01:00.0 |  |  |  |  |  |  |  |  |
|  |  |  |  |  | 10:02:00.0 |  |  |  |  |
|  | 2017-10-10 |  |  |  |  |  |  | Jark | 1 |
|  |  | 2017-10-10 |  |  |  |  | 2017-10-10 | Jar |  |
|  | 10:01:30.0 |  |  |  |  |  |  |  |  |
|  |  |  |  |  | 10:02:30.0 |  |  |  |  |
|  | 2017-10-10 |  |  |  |  |  |  | Timo | 1 |
|  |  | 2017-10-10 |  |  |  |  | 2017-10-10 | Ti |  |
|  | 10:02:00.0 |  |  |  |  |  |  |  |  |
|  |  |  |  |  | 10:03:00.0 |  |  |  |  |
|  | 2017-10-10 |  |  |  |  |  |  | Timo | 1 |
|  |  | 2017-10-10 |  |  |  |  | 2017-10-10 | Ti |  |
|  | 10:02:30.0 |  |  |  |  |  |  |  |  |
|  |  |  |  |  | 10:03:30.0 |  |  |  |  |

HOP窗口无法读取数据进入的时间，第一个窗口的开启时间会前移。**前移时长**=**窗口时长**-**滑动步长**，示例如下表。

| 窗口时长 （秒） | 滑动步长（秒） |  | Event Time |  |  |  | 第一个窗口 StartTime |  |  |  |  | 第一个窗口EndTime |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 120 | 30 |  | 2019-07-31 |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  | 2019-07-31 |  |  |  | 201 | 9-07-31 |  |  |  | 201 | 9-07-31 |  |
|  |  |  | 10:00:0 |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  | 0.0 |  | 09:58:3 |  |  | 0.0 |  | 10:00:30.0 |  |  |  |
| 60 | 10 |  | 2019-07-31 |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  | 2019-07-31 |  |  |  | 201 | 9-07-31 |  |  |  | 201 | 9-07-31 |  |
|  |  |  | 10:00:0 |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  | 0.0 |  | 09:59:1 |  |  | 0.0 |  | 10:00:10.0 |  |  |  |

#### 会话窗口

本文为您介绍如何使用Flink会话窗口函数。

**定义**

实时计算（流计算） 参考会话窗口（SESSION）通过SESSION活动来对元素进行分组。会话窗口与滚动窗口和滑动窗口相比，没有窗口重叠，没有固定窗口大小。相反，当它在一个固定的时间周期内不再收到元素，即会话断开时，该窗口就会关闭。 会话窗口通过一个间隔时间（Gap）来配置，这个间隔定义了非活跃周期的长度。例如，一个表示鼠标单击活动的数据流可能具有长时间的空闲时间，并在两段空闲之间散布着高浓度的单击。如果数据在指定的间隔 （Gap）之后到达，则会开始一个新的窗口。 会话窗口示例如下图，每个Key由于不同的数据分布，形成了不同的Window。

**函数语法**

SESSION函数用于在GROUP BY子句中定义会话窗口。

```xml
SESSION(<time-attr>, <gap-interval>) <gap-interval>: INTERVAL 'string' timeUnit
```

**说明**

`<time-attr>` 参数必须是数据流中的一个合法的时间属性字段，指定为Processing Time或Event Time，请参见概述，了解如何定义时间属性。

**标识函数**

使用标识函数选出窗口的起始时间或者结束时间，窗口的时间属性用于下级Window的聚合。

| 窗口标识函数 | 返回类型 | 描述 |
|---|---|---|

实时计算（流计算） 参考

| SESSION START（<tim _ |  |  |  | 返回窗口的起始时间（包含边界）。例如 [00:10,00:15) 的窗口，返回 00:10 ，即为此会话窗口内第一条记录的时间。 |  |  |  |  |
|---|---|---|---|---|---|---|---|---|
|  | SESSION START（<tim _ |  |  | 返 |  |  |  |  |
| e-attr>, <gap- |  |  |  |  |  |  |  |  |
|  |  | Tim |  |  |  |  |  |  |
| interval>） |  |  |  |  |  |  |  |  |
| SESSION END（<time- _ |  |  |  | 返回窗口的结束时间（包含边界）。例如 [00:00,00:15) 的窗口，返回 00:15 ，即为此会话窗口内最后一条记录的时间+ <gap- interval> 。 |  |  |  |  |
|  | SESSION END（<time- _ |  |  |  |  |  |  |  |
| attr>, <gap- |  |  |  |  |  |  |  |  |
|  |  | Ti |  |  |  |  |  |  |
| interval>） |  |  |  |  |  |  |  |  |
| SESSION ROWTIME（<t _ |  |  |  | 返回窗口的结束时间（不包含边界）。例如 [00:00,00:15) 的窗口，返回 00:14:59.999 。返回值是一个rowtime attribute，也就是可以基于该字段进行时间类型的操作，例如级联窗口。该参数只能用于基于Event Time的Window。 |  |  |  |  |
|  | SESSION ROWTIME（<t _ |  |  | 如 |  |  | [00:00,00:15) |  |
| ime-attr>, <gap- |  | Timest attr） | （rowtime- |  |  |  |  |  |
| interval>） |  |  |  |  |  |  |  |  |
| SESSION PROCTIME（< _ |  |  |  | 返回窗口的结束时间（不包含边界）。例如 [00:00,00:15) 的窗口，返回 00:14:59.999 。返回值是一个Proctime Attribute，也就是可以基于该字段进行时间类型的操作，例如级联窗口。该参数只能用于基于Processing Time的Window。 |  |  |  |  |
|  |  |  |  |  |  | [00:00,00:15) |  |  |
|  | SESSION PROCTIME（< _ | Timestamp rowtime- |  | 如 [ |  | [ |  |  |
| time-attr>, <gap- |  |  |  |  |  |  |  |  |
|  |  | （ attr） |  |  |  |  |  |  |
| interval>） |  |  |  |  |  |  |  |  |

|  | interval> |
|---|---|

**示例**

统计每个用户在每个活跃会话期间的单击次数，会话超时时长为30秒。 测试数据

| username （VARCHAR） | click url （VARCHAR） _ | ts （TIMESTAMP） |
|---|---|---|
| Jark | http://taobao.com/xxx | 2017-10-10 10:00:00.0 |
| Jark | http://taobao.com/xxx | 2017-10-10 10:00:10.0 |
| Jark | http://taobao.com/xxx | 2017-10-10 10:00:49.0 |
| Jark | http://taobao.com/xxx | 2017-10-10 10:01:05.0 |
| Jark | http://taobao.com/xxx | 2017-10-10 10:01:58.0 |
| Timo | http://taobao.com/xxx | 2017-10-10 10:02:10.0 |

测试语句实时计算（流计算） 参考

```
CREATE TEMPORARY TABLE user_clicks(
  username varchar,
  click_url varchar,
  eventtime varchar,
  ts AS TO_TIMESTAMP(eventtime),
  WATERMARK FOR ts AS ts - INTERVAL '2' SECOND  --为Rowtime定义Watermark。
) with (
  'connector'='sls',
  ...
); CREATE TEMPORARY TABLE session_output(
  window_start TIMESTAMP,
  window_end TIMESTAMP,
  username VARCHAR,
  clicks BIGINT
) with (
```

`'connector'='datahub' --`目前`SLS`只支持输出`VARCHAR`类型的`DDL`，所以使用`DataHub`存储。

```
  ...
); INSERT INTO session_output SELECT SESSION_START(ts, INTERVAL '30' SECOND), SESSION_END(ts, INTERVAL '30' SECOND), username, COUNT(click_url) FROM user_clicks GROUP BY SESSION(ts, INTERVAL '30' SECOND), username;
```

测试结果

|  | window start _ （TIMESTAMP） |  |  |  | window end _ （TIMESTAMP） |  |  | username （VARCHAR） | clicks （BIGINT） |
|---|---|---|---|---|---|---|---|---|---|
|  | 2017-10-10 |  |  |  |  |  |  | Jark | 2 |
|  |  | 2017-10-10 |  |  |  |  | 2017-10-10 | Jar |  |
|  | 10:00:00.0 |  |  |  |  |  |  |  |  |
|  |  |  |  |  | 10:00:40.0 |  |  |  |  |
|  | 2017-10-10 |  |  |  |  |  |  | Jark | 2 |
|  |  | 2017-10-10 |  |  |  |  | 2017-10-10 | Jar |  |
|  | 10:00:49.0 |  |  |  |  |  |  |  |  |
|  |  |  |  |  | 10:01:35.0 |  |  |  |  |
|  | 2017-10-10 |  |  |  |  |  |  | Jark | 1 |
|  |  | 2017-10-10 |  |  |  |  | 2017-10-10 | Jar |  |
|  | 10:01:58.0 |  |  |  |  |  |  |  |  |
|  |  |  |  |  | 10:02:28.0 |  |  |  |  |
|  | 2017-10-10 |  |  |  |  |  |  | Timo | 1 |
|  |  | 2017-10-10 |  |  |  |  | 2017-10-10 | Ti |  |
|  | 10:02:10.0 |  |  |  |  |  |  |  |  |
|  |  |  |  |  | 10:02:40.0 |  |  |  |  |

#### OVER窗口

实时计算（流计算） 参考 OVER窗口（OVER Window）是传统数据库的标准开窗，不同于Group By Window，OVER窗口中每1个元素都对应1个窗口。OVER窗口可以按照实际元素的行或实际的元素值（时间戳值）确定窗口，因此流数据元素可能分布在多个窗口中。 在应用OVER窗口的流式数据中，每1个元素都对应1个OVER窗口。每1个元素都触发1次数据计算，每个触发计算的元素所确定的行，都是该元素所在窗口的最后1行。在实时计算的底层实现中，OVER窗口的数据进行全局统一管理（数据只存储1份），逻辑上为每1个元素维护1个OVER窗口，为每1个元素进行窗口计算， 完成计算后会清除过期的数据。

**语法**

```
SELECT
    agg1(col1) OVER (definition1) AS colName,
    ...
    aggN(colN) OVER (definition1) AS colNameN
FROM Tab1;
```

agg1(col1)：按照GROUP BY指定col1列对输入数据进行聚合计算。 AS colName：别名。

**说明**

agg1到aggN所对应的OVER definition1必须相同。 外层SQL可以通过AS的别名查询数据。

**类型**

Flink SQL中对OVER窗口的定义遵循标准SQL的定义语法，传统OVER窗口没有对其进行更细粒度的窗口类型命名划分。按照计算行的定义方式，OVER Window可以分为以下两类： ROWS OVER Window：每1行元素都被视为新的计算行，即每1行都是一个新的窗口。 RANGE OVER Window：具有相同时间值的所有元素行视为同一计算行，即具有相同时间值的所有行都是同一个窗口。

**属性**

| 正交属性 | 说明 | proctime | eventtime |
|---|---|---|---|
| ROWS OVER Window | 按照实际元素的行确定窗口。 | 支持 | 支持 |
| RANGE OVER Window | 按照实际的元素值（时间戳值）确定窗口。 | 支持 | 支持 |

**Rows OVER Window语义**

窗口数据 ROWS OVER Window的每个元素都确定一个窗口。ROWS OVER Window分为Unbounded（无界流）和Bounded（有界流）两种情况。 Unbounded ROWS OVER Window数据示例如下图所示。 实时计算（流计算） 参考虽然上图所示窗口user1的w7、w8及user2的窗口w3、w4都是同一时刻到达，但它们

**说明**

仍然在不同的窗口，这一点与RANGE OVER Window不同。 Bounded ROWS OVER Window数据以3个元素（往前2个元素）的窗口为例，如下图所示。 虽然上图所示窗口user1的w5、w6及user2的窗口w1、w2都是同一时刻到达，但它们

**说明**

仍然在不同的窗口，这一点与RANGE OVER Window不同。 窗口语法实时计算（流计算） 参考

```
SELECT
    agg1(col1) OVER(
     [PARTITION BY (value_expression1,..., value_expressionN)]
     ORDER BY timeCol
     ROWS
     BETWEEN (UNBOUNDED | rowCount) PRECEDING AND CURRENT ROW) AS colName, ...
FROM Tab1;
```

value_expression：分区值表达式。 timeCol：元素排序的时间字段。 rowCount：定义根据当前行开始向前追溯几行元素。 案例以Bounded ROWS OVER Window场景为例。假设，一张商品上架表，包含有商品ID、商品类型、商品上架时间、商品价格数据。要求输出在当前商品上架之前同类的3个商品中的最高价格。 测试数据

| 商品ID | 商品类型 | 上架时间 | 销售价格 |
|---|---|---|---|
| ITEM001 | Electronic | 2017-11-11 10:01:00 | 20 |
| ITEM002 | Electronic | 2017-11-11 10:02:00 | 50 |
| ITEM003 | Electronic | 2017-11-11 10:03:00 | 30 |
| ITEM004 | Electronic | 2017-11-11 10:03:00 | 60 |
| ITEM005 | Electronic | 2017-11-11 10:05:00 | 40 |
| ITEM006 | Electronic | 2017-11-11 10:06:00 | 20 |
| ITEM007 | Electronic | 2017-11-11 10:07:00 | 70 |
| ITEM008 | Clothes | 2017-11-11 10:08:00 | 20 |

|  |  | 2017-11-11 |  |
|---|---|---|---|
|  | 10:01:00 |  |  |

|  |  | 2017-11-11 |  |
|---|---|---|---|
|  | 10:02:00 |  |  |

|  |  | 2017-11-11 |  |
|---|---|---|---|
|  | 10:03:00 |  |  |

|  |  | 2017-11-11 |  |
|---|---|---|---|
|  | 10:03:00 |  |  |

|  |  | 2017-11-11 |  |
|---|---|---|---|
|  | 10:05:00 |  |  |

|  |  | 2017-11-11 |  |
|---|---|---|---|
|  | 10:06:00 |  |  |

|  |  | 2017-11-11 |  |
|---|---|---|---|
|  | 10:07:00 |  |  |

|  |  | 2017-11-11 |  |
|---|---|---|---|
|  | 10:08:00 |  |  |

实时计算（流计算） 参考测试代码

```
CREATE TEMPORARY TABLE tmall_item(
  itemID VARCHAR,
  itemType VARCHAR,
  eventtime varchar,
  onSellTime AS TO_TIMESTAMP(eventtime),
  price DOUBLE,
  WATERMARK FOR onSellTime AS onSellTime - INTERVAL '0' SECOND  --为Rowtime定义
) WITH (
  'connector' = 'sls',
   ...
); SELECT
    itemID,
    itemType,
    onSellTime,
    price,
    MAX(price) OVER (
        PARTITION BY itemType
        ORDER BY onSellTime
        ROWS BETWEEN 2 preceding AND CURRENT ROW) AS maxPrice
FROM tmall_item;
```

测试结果

| itemID | itemType | onSellTime | price | maxPrice |
|---|---|---|---|---|
| ITEM001 | Electronic | 2017-11-11 10:01:00 | 20 | 20 |
| ITEM002 | Electronic | 2017-11-11 10:02:00 | 50 | 50 |
| ITEM003 | Electronic | 2017-11-11 10:03:00 | 30 | 50 |
| ITEM004 | Electronic | 2017-11-11 10:03:00 | 60 | 60 |
| ITEM005 | Electronic | 2017-11-11 10:05:00 | 40 | 60 |
| ITEM006 | Electronic | 2017-11-11 10:06:00 | 20 | 60 |
| ITEM007 | Electronic | 2017-11-11 10:07:00 | 70 | 70 |
| ITEM008 | Clothes | 2017-11-11 10:08:00 | 20 | 20 |

|  |  | 2017-11-11 |
|---|---|---|
| tronic | 10:01:00 |  |

|  |  | 2017-11-11 |
|---|---|---|
| tronic | 10:02:00 |  |

|  |  | 2017-11-11 |
|---|---|---|
| tronic | 10:03:00 |  |

|  |  | 2017-11-11 |
|---|---|---|
| tronic | 10:03:00 |  |

|  |  | 2017-11-11 |
|---|---|---|
| tronic | 10:05:00 |  |

|  |  | 2017-11-11 |
|---|---|---|
| tronic | 10:06:00 |  |

|  |  | 2017-11-11 |
|---|---|---|
| tronic | 10:07:00 |  |

|  |  | 2017-11-11 |
|---|---|---|
| hes | 10:08:00 |  |

实时计算（流计算） 参考

**RANGE OVER Window语义**

窗口数据 RANGE OVER Window所有具有共同元素值（元素时间戳）的元素行确定一个窗口，RANGE OVER Window分为Unbounded和Bounded的两种情况。 Unbounded RANGE OVER Window数据示例如下图所示。 上图所示窗口user1的w7、user2的窗口w3，两个元素同一时刻到达，属于相同的

**说明**

window，这一点与ROWS OVER Window不同。 Bounded RANGE OVER Window数据，以3秒中数据 `(INTERVAL '2' SECOND)` 的窗口为例，如下图所示。 实时计算（流计算） 参考上图所示窗口user1的w6、user2的窗口w3，元素都是同一时刻到达，属于相同的

**说明**

window，这一点与ROWS OVER Window不同。 窗口语法

```
SELECT
    agg1(col1) OVER(
     [PARTITION BY (value_expression1,..., value_expressionN)]
     ORDER BY timeCol
     RANGE
     BETWEEN (UNBOUNDED | timeInterval) PRECEDING AND CURRENT ROW) AS colName,
... FROM Tab1;
```

value_expression：进行分区的字表达式。 timeCol：元素排序的时间字段。 timeInterval：定义根据当前行开始向前追溯指定时间的元素行。 案例 Bounded RANGE OVER Window场景示例：假设一张商品上架表，包含有商品ID、商品类型、商品上架时间、商品价格数据。需要求比当前商品上架时间早2分钟的同类商品中的最高价格。 实时计算（流计算） 参考测试数据

| 商品ID | 商品类型 | 上架时间 | 销售价格 |
|---|---|---|---|
| ITEM001 | Electronic | 2017-11-11 10:01:00 | 20 |
| ITEM002 | Electronic | 2017-11-11 10:02:00 | 50 |
| ITEM003 | Electronic | 2017-11-11 10:03:00 | 30 |
| ITEM004 | Electronic | 2017-11-11 10:03:00 | 60 |
| ITEM005 | Electronic | 2017-11-11 10:05:00 | 40 |
| ITEM006 | Electronic | 2017-11-11 10:06:00 | 20 |
| ITEM007 | Electronic | 2017-11-11 10:07:00 | 70 |
| ITEM008 | Clothes | 2017-11-11 10:08:00 | 20 |

|  |  | 2017-11-11 |  |
|---|---|---|---|
|  | 10:01:00 |  |  |

|  |  | 2017-11-11 |  |
|---|---|---|---|
|  | 10:02:00 |  |  |

|  |  | 2017-11-11 |  |
|---|---|---|---|
|  | 10:03:00 |  |  |

|  |  | 2017-11-11 |  |
|---|---|---|---|
|  | 10:03:00 |  |  |

|  |  | 2017-11-11 |  |
|---|---|---|---|
|  | 10:05:00 |  |  |

|  |  | 2017-11-11 |  |
|---|---|---|---|
|  | 10:06:00 |  |  |

|  |  | 2017-11-11 |  |
|---|---|---|---|
|  | 10:07:00 |  |  |

|  |  | 2017-11-11 |  |
|---|---|---|---|
|  | 10:08:00 |  |  |

测试代码

```
CREATE TEMPORARY TABLE tmall_item(
  itemID VARCHAR,
  itemType VARCHAR,
  eventtime varchar,
  onSellTime AS TO_TIMESTAMP(eventtime),
  price DOUBLE,
  WATERMARK FOR onSellTime AS onSellTime - INTERVAL '0' SECOND  --为Rowtime定义
) WITH (
  'connector' = 'sls',
   ...
); SELECT
    itemID,
    itemType,
    onSellTime,
    price,
    MAX(price) OVER (
        PARTITION BY itemType
        ORDER BY onSellTime
        RANGE BETWEEN INTERVAL '2' MINUTE preceding AND CURRENT ROW) AS maxPrice
FROM tmall_item;
```

实时计算（流计算） 参考测试结果

| itemID | itemType | onSellTime | price | maxPrice |
|---|---|---|---|---|
| ITEM001 | Electronic | 2017-11-11 10:01:00 | 20 | 20 |
| ITEM002 | Electronic | 2017-11-11 10:02:00 | 50 | 50 |
| ITEM003 | Electronic | 2017-11-11 10:03:00 | 30 | 50 |
| ITEM004 | Electronic | 2017-11-11 10:03:00 | 60 | 60 |
| ITEM005 | Electronic | 2017-11-11 10:05:00 | 40 | 60 |
| ITEM006 | Electronic | 2017-11-11 10:06:00 | 20 | 40 |
| ITEM007 | Electronic | 2017-11-11 10:07:00 | 70 | 70 |
| ITEM008 | Clothes | 2017-11-11 10:08:00 | 20 | 20 |

|  |  | 2017-11-11 | 20 |
|---|---|---|---|
| onic | 10:01:00 |  |  |

|  |  | 2017-11-11 | 50 |
|---|---|---|---|
| onic | 10:02:00 |  |  |

|  |  | 2017-11-11 | 30 |
|---|---|---|---|
| onic | 10:03:00 |  |  |

|  |  | 2017-11-11 | 60 |
|---|---|---|---|
| onic | 10:03:00 |  |  |

|  |  | 2017-11-11 | 40 |
|---|---|---|---|
| onic | 10:05:00 |  |  |

|  |  | 2017-11-11 | 20 |
|---|---|---|---|
| onic | 10:06:00 |  |  |

|  |  | 2017-11-11 | 70 |
|---|---|---|---|
| onic | 10:07:00 |  |  |

|  |  | 2017-11-11 | 20 |
|---|---|---|---|
| es | 10:08:00 |  |  |

### 内置函数

#### 概述

本文为您介绍Flink提供的用于数据转换的内置函数。 Flink V1.11：请参见Flink V1.11内置函数。 Flink V1.12：请参见Flink V1.12内置函数。

**说明**

Flink全托管VVR 3.0.0版本在Flink V1.12的基础上增加了部分内置函数，详情请参见标量函数。 如果内置函数中不存在您所需的函数，您可以通过自定义函数实现，自定义函数详情请参见概述。

#### 标量函数

##### BITAND

本文仅适用于VVP 2.4.0且VVR 3.0.0及以上版本。

**重要**

实时计算（流计算） 参考

**语法**

输入和输出类型均为整型，且类型一致。

**说明**

**入参**

| 参数 | 数据类型 |
|---|---|
| number1 | INT |
| number2 | INT |

**示例**

测试数据

| a(INT) | b(INT) |
|---|---|
| 2 | 3 |

测试语句

```
FROM T1;
```

测试结果

**intt(INT)**

##### BITNOT

本文仅适用于VVP 2.4.0且VVR 3.0.0及以上版本。

**重要**

**语法**

输入和输出类型均为整型，且类型一致。

**说明**

**入参**

| 参数 | 数据类型 |
|---|---|
| number | INT |

实时计算（流计算） 参考

**示例**

测试数据

**a(INT)**

测试语句

```
FROM T1;
```

测试结果

**var1(INT)**

-8

##### BITOR

本文仅适用于VVP 2.4.0且VVR 3.0.0及以上版本。

**重要**

**语法**

**入参**

| 参数 | 数据类型 |
|---|---|
| number1 | INT |
| number2 | INT |

输入和输出类型均为整型，且类型一致。

**说明**

**示例**

测试数据

| a(INT) | b(INT) |
|---|---|
| 2 | 3 |

测试语句

```
FROM T1;
```

测试结果实时计算（流计算） 参考

**var1(INT)**

-3

##### BITXOR

本文仅适用于VVP 2.4.0且VVR 3.0.0及以上版本。

**重要**

**语法**

**入参**

| 参数 | 数据类型 |
|---|---|
| number1 | INT |
| number2 | INT |

输入和输出类型均为整型，且类型一致。

**说明**

**示例**

测试数据

| a(INT) | b(INT) |
|---|---|
| 2 | 3 |

测试语句

```
FROM T1;
```

测试结果

**var1(INT)**

##### CONV

本文为您介绍如何使用CONV函数，对数字或字符类型的数值进行进制转换。

**重要**

本文仅适用于VVP 2.4.0且VVR 3.0.0及以上版本。
**CONV()**精度为64位。
实时计算（流计算） 参考

**语法**

```
VARCHAR CONV(BIGINT number, INT FROM_BASE, INT TO_BASE)
```

`or`

```
VARCHAR CONV(VARCHAR number, INT FROM_BASE, INT TO_BASE)
```

**入参**

| 参数 | 数据类型 | 说明 |
|---|---|---|
| number | BIGINT、VARCHAR | 说明当number为 NULL或非法字符时，结果返回为NULL。 |
| FROM BASE _ | INT | 取值范围[2, 36]。 |
| TO BASE _ | INT | 可以为正数，取值范围[2, 36]；也可以为负数，取值范围[-36, -2]。 |

**示例**

测试数据

| id(INT) | x(BIGINT) | y (VARCHAR) |
|---|---|---|
| 1 | 12L | '12' |
| 2 | 10L | '10' |
| 3 | 0L | 'test' |
| 4 | NULL | NULL |

测试语句

```
SELECT id, conv(x, 10, 16) as var1, conv(y, 10, 2) as var2 FROM T1;
```

测试结果

| id(INT) | var1(VARCHAR) | var2(VARCHAR) |
|---|---|---|
| 1 | C | 1100 |
| 2 | A | 1010 |
| 3 | 0 | NULL |
| 4 | NULL | NULL |

##### DATEDIFF

实时计算（流计算） 参考本文仅适用于VVP 2.4.0且VVR 3.0.0及以上版本。

**重要**

**语法**

```
INT DATEDIFF(VARCHAR enddate, VARCHAR startdate) INT DATEDIFF(TIMESTAMP enddate, VARCHAR startdate) INT DATEDIFF(VARCHAR enddate, TIMESTAMP startdate) INT DATEDIFF(TIMESTAMP enddate, TIMESTAMP startdate)
```

**入参**

| 参数 | 数据类型 |
|---|---|
| startdate | TIMESTAMP、VARCHAR |
| enddate | TIMESTAMP、VARCHAR |

**说明**

VARCHAR日期格式：**yyyy-MM-dd**或**yyyy-MM-dd HH:mm:ss**。 如果入参中任何一个为NULL或解析错误，则返回为NULL。

**示例**

测试数据

| datetime1(VARCHAR) | datetime2(VARCHAR) | nullstr(VARCHAR) |
|---|---|---|
| 2017-10-15 00:00:00 | 2017-09-15 00:00:00 | NULL |

测试语句

```
SELECT DATEDIFF(datetime1, datetime2) as int1,
        DATEDIFF(TIMESTAMP '2017-10-15 23:00:00',datetime2) as int2,
        DATEDIFF(datetime2,TIMESTAMP '2017-10-15 23:00:00') as int3,
        DATEDIFF(datetime2,nullstr) as int4,
        DATEDIFF(nullstr,TIMESTAMP '2017-10-15 23:00:00') as int5,
        DATEDIFF(nullstr,datetime2) as int6,
        DATEDIFF(TIMESTAMP '2017-10-15 23:00:00',TIMESTAMP '2017-9-15 00:00:00')as int
FROM T1;
```

测试结果

| int1(INT) | int2(INT) | int3(INT) | int4(INT) | int5(INT) | int6(INT) | int7(INT) |
|---|---|---|---|---|---|---|
| 30 | 31 | -31 | NULL | NULL | NULL | 31 |

##### DATE_ADD

实时计算（流计算） 参考本文仅适用于VVP 2.4.0且VVR 3.0.0及以上版本。

**重要**

**语法**

**入参**

| 参数 | 数据类型 |
|---|---|
| startdate | TIMESTAMP、VARCHAR 说明 VARCHAR类型日期格式为yyyy-MM-dd或yyyy-MM- dd HH:mm:ss。 |
| time | TIMESTAMP |
| days | INT |

如果入参中任何一个为NULL或解析错误，则返回为NULL。

**说明**

**示例**

测试数据

| datetime1(VATCHAR) | nullstr(VATCHAR) |
|---|---|
| 2017-09-15 00:00:00 | null |

测试语句

```
SELECT DATE_ADD(datetime1, 30) as var1,
 DATE_ADD(TIMESTAMP '2017-09-15 23:00:00',30) as var2,
FROM T1;
```

测试结果

| var1(VARCHAR) | var2(VARCHAR) | var3(VARCHAR) |
|---|---|---|
| 2017-10-15 | 2017-10-15 | null |

##### DATE_FORMAT

本文为您介绍如何使用DATE_FORMAT函数，将字符串类型的日期从原格式转换至目标格式。 本文仅适用于VVP 2.4.0且VVR 3.0.0及以上版本。

**重要**

**语法**

实时计算（流计算） 参考

```
VARCHAR DATE_FORMAT(TIMESTAMP time, VARCHAR to_format) VARCHAR DATE_FORMAT(VARCHAR date, VARCHAR to_format) VARCHAR DATE_FORMAT(VARCHAR date, VARCHAR from_format, VARCHAR to_format)
```

**入参**

| 参数 | 数据类型 | 说明 |
|---|---|---|
| time | TIMESTAMP | 源字符串。 |
| date | VARCHAR | 源字符串，默认格式为：yyyy-MM-dd HH:mm:ss。 |
| from format _ | VARCHAR | 可选，原格式，默认格式为yyyy-MM-dd hh:mm:ss。 |
| to format _ | VARCHAR | 目标格式。 |

如果入参中任何一个为NULL或解析错误，则返回为NULL。

**说明**

**示例**

测试数据

| date1(VARCHAR) | datetime1(VARCHAR) | nullstr(VARCHAR) |
|---|---|---|
| 0915-2017 | 2017-09-15 00:00:00 | NULL |

测试语句

```
SELECT DATE_FORMAT(datetime1, 'yyMMdd') as var1,
 DATE_FORMAT(nullstr, 'yyMMdd') as var2,
 DATE_FORMAT(datetime1, nullstr) as var3,
 DATE_FORMAT(date1, 'MMdd-yyyy', nullstr) as var4,
 DATE_FORMAT(date1, 'MMdd-yyyy', 'yyyyMMdd') as var5,
 DATE_FORMAT(TIMESTAMP '2017-09-15 23:00:00', 'yyMMdd') as var6
FROM T1;
```

测试结果

| var1(VARCH AR) | var2(VARCH AR) | var3(VARCH AR) | var4(VARCH AR) | var5(VARCH AR) | var6(VARCH AR) |
|---|---|---|---|---|---|
| 170915 | null | null | null | 20170915 | 170915 |

##### DATE_FORMAT_TZ

本文为您介绍如何使用DATE_FORMAT_TZ函数，将时间戳类型的数据根据指定的时区，转成指定格式的字符串。 本文仅适用于VVP 2.4.0且VVR 3.0.0及以上版本。

**重要**

**语法**

实时计算（流计算） 参考

```
VARCHAR DATE_FORMAT_TZ(TIMESTAMP timestamp, VARCHAR format, VARCHAR timezone) VARCHAR DATE_FORMAT_TZ(TIMESTAMP timestamp, VARCHAR timezone)
```

**入参**

| 参数 | 数据类型 | 说明 |
|---|---|---|
| timestamp | TIMESTAMP | 时间类型。 |
| format | VARCHAR | 输出日期格式，例如yyyy-MM-dd HH:mm:ss。 |
| timezone | VARCHAR | 指定时区，例如Asia/Shanghai。 |

**示例**

测试数据

| timestamp1(TIMESTAMP) | format1(VARCHAR) | timezone1(VARCHAR) |
|---|---|---|
| 0 | yyyy-MM-dd HH:mm:ss | Asia/Shanghai |

测试语句

```
SELECT
   DATE_FORMAT_TZ(timestamp1, format1, timezone1) as var1,
FROM T1;
```

测试结果

| var1(VARCHAR) | var2(VARCHAR) |
|---|---|
| 1970-01-01 08:00:00 | 1970-01-01 08:00:00 |

##### DATE_SUB

本文仅适用于VVP 2.4.0且VVR 3.0.0及以上版本。

**重要**

**语法**

**入参**

| 参数 | 数据类型 |
|---|---|

实时计算（流计算） 参考

| startdate | VARCHAR 说明 VARCHAR类型日期格式为yyyy-MM-dd或yyyy-MM- dd HH:mm:ss。 |
|---|---|
| time | TIMESTAMP |
| days | INT |

如果入参中任何一个为NULL或解析错误，则返回为NULL。

**说明**

**示例**

测试数据

| date1(VARCHAR) | nullstr(VARCHAR) |
|---|---|
| 2017-10-15 | NULL |

测试语句

```
SELECT DATE_SUB(date1, 30) as var1,
 DATE_SUB(TIMESTAMP '2017-10-15 23:00:00',30) as var2,
FROM T1;
```

测试结果

| var1(VARCHAR) | var2(VARCHAR) | var3(VARCHAR) |
|---|---|---|
| 2017-09-15 | 2017-09-15 | NULL |

##### FROM_UNIXTIME

本文为您介绍如何使用FROM_UNIXTIME函数，返回VARCHAR类型的日期值。 本文仅适用于VVP 2.4.0且VVR 3.0.0及以上版本。

**重要**

**语法**

```
VARCHAR FROM_UNIXTIME(BIGINT unixtime, VARCHAR format)
```

**入参**

| 参数 | 数据类型 | 说明 |
|---|---|---|
| unixtime | BIGINT | 以秒为单位的时间戳。 |
| format | VARCHAR | 可选，日志格式，默认格式为yyyy-MM-dd HH:mm:ss。 |

实时计算（流计算） 参考如果入参中任何一个为NULL或解析错误，则返回为NULL。

**说明**

**示例**

测试数据

| unixtime1(BIGINT) | nullstr(VARCHAR) |
|---|---|
| 1505404800 | NULL |

测试语句

```
SELECT FROM_UNIXTIME(unixtime1) as var1,
 FROM_UNIXTIME(unixtime1,'MMdd-yyyy') as var2,
FROM T1;
```

测试结果

| var1(VARCHAR) | var2(VARCHAR) | var3(VARCHAR) |
|---|---|---|
| 2017-09-15 00:00:00 | 0915-2017 | NULL |

##### ISNAN

本文为您介绍如何使用ISNAN函数，判断指定的浮点数是否为NaN（Not a number），类似于Java中本文仅适用于VVP 2.4.0且VVR 3.0.0及以上版本。

**重要**

**语法**

**入参**

| 参数 | 数据类型 |
|---|---|
| d | DOUBLE |
| f | FLOAT |

**示例**

测试数据表 1. T1

| d | f |
|---|---|
| 0.1 | 0.1 |
| 0 | 0 |

实时计算（流计算） 参考测试语句

```
SELECT ISNAN(CAST(d AS DOUBLE)) as d1, FROM T1;
```

测试结果

| d1(BOOLEAN) | d2(BOOLEAN) |
|---|---|
| false | false |
| false | false |

##### JSON_VALUE

本文为您介绍如何使用JSON_VALUE函数，从JSON字符串中提取指定路径的表达式。 本文仅适用于VVP 2.4.0且VVR 3.0.0及以上版本。

**重要**

**语法**

```
VARCHAR JSON_VALUE(VARCHAR content, VARCHAR path)
```

**入参**

| 参数 | 数据类型 | 说明 |
|---|---|---|
| content | VARCHAR | 需要解析的JSON对象。 |
| path | VARCHAR | 指定路径表达式。自定义路径需要使用单引号（'），示例如下。 JSON VALUE(json,'$.passenger name') AS _ _ ABC 目前路径支持的符号及功能如下： $：根对象。 []：数组下标。 *：数组通配符。 .：取子元素。 |

如果入参中有不合法的JSON和NULL，则返回为NULL。

**说明**

**示例**

测试数据表 1. T1

| id(INT) | json(VARCHAR) | path1(VARCHAR) |
|---|---|---|
| 1 | [10, 20, [30, 40]] | $[2][*] |

实时计算（流计算） 参考

| 2 | {"aaa":"bbb","ccc": {"ddd":"eee","fff":"ggg","hhh": ["h0","h1","h2"]},"iii":"jjj"} | $.ccc.hhh[*] |
|---|---|---|
| 3 | {"aaa":"bbb","ccc": {"ddd":"eee","fff":"ggg",hhh": ["h0","h1","h2"]},"iii":"jjj"} | $.ccc.hhh[1] |
| 4 | [10, 20, [30, 40]] | NULL |
| 5 | NULL | $[2][*] |
| 6 | "{xx]" | "$[2][*]" |

测试语句

```
SELECT
```

`id`，

```
FROM
    T1;
```

测试结果

| id (INT) | value (VARCHAR) |
|---|---|
| 1 | [30,40] |
| 2 | ["h0","h1","h2"] |
| 3 | H1 |
| 4 | NULL |
| 5 | NULL |
| 6 | NULL |

##### KEYVALUE

本文为您介绍如何使用KEYVALUE函数，将目标字符串按照split1分隔符拆分成Key-Value（KV）对，然后本文仅适用于VVP 2.4.0且VVR 3.0.0及以上版本。

**重要**

**语法**

```
VARCHAR KEYVALUE(VARCHAR str, VARCHAR split1, VARCHAR split2, VARCHAR key_name)
```

**入参**

| 参数 | 数据类型 | 说明 |
|---|---|---|
| str | VARCHAR | 待拆分的目标字符串。 |

实时计算（流计算） 参考

| split1 | VARCHAR | 按照split1分隔符，将目标字符串拆分成Key- Value（KV）对。 |
|---|---|---|
| split2 | VARCHAR | 按照split2分隔符将Key-Value对分开。 |
| key name _ | VARCHAR | Key的名称。 |

**说明**

如果split1或split2为NULL时，则返回NULL。 如果str或者key_name为NULL时，则返回NULL。 如果没有匹配的Key时，则返回NULL。

**示例**

测试数据表 1. T1

| str(VARCHAR) | split1(VARCHAR) | split2(VARCHAR) | key1(VARCHAR) |
|---|---|---|---|
| k1=v1;k2=v2 | ; | = | k2 |
| NULL | ; | \| | : |
| k1:v1\|k2:v2 | NULL | = | : |
| k1:v1\|k2:v2 | \| | = | NULL |
| k1:v1\|k2:v2 | \| | = | : |

测试语句

```
SELECT KEYVALUE(str, split1, split2, key1) as `result` FROM T1;
```

测试结果

**result(VARCHAR)**

v2 NULL NULL NULL NULL

##### MURMUR_HASH

本文为您介绍如何使用MURMUR_HASH函数，按Murmur 32哈希算法计算指定参数的32位哈希值。 本文仅适用于VVP 2.4.0且VVR 3.0.0及以上版本。

**重要**

实时计算（流计算） 参考

**语法**

**入参**

| 参数 | 数据类型 |
|---|---|
| value | VARCHAR或数值类型。 |

**示例1**

测试数据表 1. T1 This is a test String. NULL test 测试语句

```
FROM T1;
```

测试结果

**intt(VARCHAR)**

740959099 NULL 271330425

**示例2**

测试数据表 2. T2

**str**

4.5 NULL 测试语句

```
FROM T2;
```

测试结果

**intt(VARCHAR)**

实时计算（流计算） 参考 -2130121231 NULL 1863595885

##### MURMUR_HASH_64

本文为您介绍如何使用MURMUR_HASH_64函数，按Murmur 128哈希算法计算指定参数的64位哈希值。 本文仅适用于VVP 2.4.0且VVR 3.0.0及以上版本。

**重要**

**语法**

**入参**

| 参数 | 数据类型 |
|---|---|
| value | VARCHAR或数值类型。 |

**示例1**

测试数据表 1. T1 This is a test String. NULL test 测试语句

```
FROM T1;
```

测试结果

**big(VARCHAR)**

2706826604463634835 NULL 5010266691562018262

**示例2**

测试数据表 2. T2 实时计算（流计算） 参考 4.5 NULL 测试语句

```
FROM T2;
```

测试结果

**big(VARCHAR)**

8033179276572534397 NULL -6697622088025985219

##### PARSE_URL

本文仅适用于VVP 2.4.0且VVR 3.0.0及以上版本。

**重要**

**语法**

```
VARCHAR PARSE_URL(VARCHAR urlStr, VARCHAR partToExtract [, VARCHAR key])
```

**入参**

| 参数 | 数据类型 | 说明 |
|---|---|---|
| urlStr | VARCHAR | 目标URL。 说明如果urlStr参数值为NULL时，则返回值为NULL。 |
| partToExtract | VARCHAR | 指定链接中解析的部分。取值如下： HOST PATH QUERY REF PROTOCOL FILE AUTHORITY USERINFO |
| key | VARCHAR | 可选，指定截取部分，具体的键。 |

实时计算（流计算） 参考

**示例**

测试数据

| url1(VARCHAR) | nullstr(VARCHAR) |
|---|---|
| http://facebook.com/path/p1.php?query=1 | NULL |

测试语句

```
SELECT PARSE_URL(url1, 'QUERY', 'query') as var1,
       PARSE_URL(url1, 'QUERY') as var2,
       PARSE_URL(url1, 'HOST') as var3,
       PARSE_URL(url1, 'PATH') as var4,
       PARSE_URL(url1, 'REF') as var5,
       PARSE_URL(url1, 'PROTOCOL') as var6,
       PARSE_URL(url1, 'FILE') as var7,
       PARSE_URL(url1, 'AUTHORITY') as var8,
       PARSE_URL(nullstr, 'QUERY') as var9,
       PARSE_URL(url1, 'USERINFO') as var10,
FROM T1;
```

测试结果

| var1( VAR CHA R) | var2( VAR CHA R) | var3( VAR CHA R) | var4( VAR CHA R) | var5( VAR CHA R) | var6( VAR CHA R) | var7 (VAR CHA R) | var8 (VAR CHA R) | var9 (VAR CHA R) | var1 0(VA RCH AR) | var1 1(VA RCH AR) |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | query =1 | faceb ook.c om | /path/ p1.ph p | NULL | http | /path /p1.p hp? query =1 | faceb ook.c om | NULL | NULL | NULL |

##### REGEXP

本文为您介绍如何使用REGEXP函数，对指定的字符串执行一个正则表达式搜索，并返回一个Boolean值表示是否找到指定的匹配模式。 本文仅适用于VVP 2.4.0且VVR 3.0.0及以上版本。

**重要**

**语法**

**入参**

| 参数 | 数据类型 | 说明 |
|---|---|---|
| str | VARCHAR | 指定的字符串。 |
| pattern | VARCHAR | 指定的匹配模式。 |

实时计算（流计算） 参考如果str或pattern为空或为NULL，则返回false。

**说明**

**示例**

测试数据表 1. T1

| str1(VARCHAR) | pattern1(VARCHAR) |
|---|---|
| k1=v1;k2=v2 | k2* |
| k1:v1\|k2:v2 | k3 |
| NULL | k3 |
| k1:v1\|k2:v2 | NULL |
| k1:v1\|k2:v2 | ( |

测试语句

```
FROM T1;
```

测试结果

**result(BOOLEAN)**

true false false false false

##### REGEXP_REPLACE

本文为您介绍如何使用REGEXP_REPLACE函数，用目标字符串替换指定字符串，并返回新的字符串。 本文仅适用于VVP 2.4.0且VVR 3.0.0及以上版本。

**重要**

**语法**

```
VARCHAR REGEXP_REPLACE(VARCHAR str, VARCHAR pattern, VARCHAR replacement)
```

**入参**

| 参数 | 数据类型 | 说明 |
|---|---|---|
| str | VARCHAR | 指定的字符串。 |
| pattern | VARCHAR | 被替换的字符串。 |

实时计算（流计算） 参考

| replacement | VARCHAR | 用于替换的目标字符串。 |
|---|---|---|

**重要**

如果入参为NULL或者正则不合法时，则返回NULL。 系统会将pattern和replacement的字符串解析成正则表达式，正则表达式使用Java Pattern进行处理，因此pattern和replacement的字符串需遵从Java Regex语法。

**示例**

测试数据表 1. T1

| str1(VARCHAR) | pattern1(VARCHAR) | replace1(VARCHAR) |
|---|---|---|
| 2014-03-13 | - | ‘’ |
| ‘‘ | - | ‘‘ |
| 2014-03-13 | '' | s |
| 2014-03-13 | ( | s |
| 100-200 | (\d+) | num |

测试语句

```
SELECT REGEXP_REPLACE(str1, pattern1, replace1) as result FROM T1;
```

测试结果

**result(VARCHAR)**

20140313 空 s2s0s1s4s-s0s3s-s1s3s null num-num

##### SPLIT_INDEX

本文为您介绍如何使用SPLIT_INDEX函数，将目标字符串按照指定分隔符分割成若干段，返回指定位置的字段信息。

**重要**

本文仅适用于VVP 2.4.0且VVR 3.0.0及以上版本。

**语法**

```
VARCHAR SPLIT_INDEX(VARCHAR str, VARCHAR sep, INT index)
```

实时计算（流计算） 参考

**入参**

| 参数 | 数据类型 | 说明 |
|---|---|---|
| str | VARCHAR | 目标字符串。 |
| sep | VARCHAR | 分隔符。 |
| index | INT | 字段位置，index从0开始。 说明如果获取不到字段，则返回NULL。 |

如果入参任何一个为NULL，则返回NULL。

**说明**

**示例**

测试数据表 1. T1

| str(VARCHAR) | sep(VARCHAR) | index(INT) |
|---|---|---|
| Jack,John,Mary | , | 2 |
| Jack,John,Mary | , | 3 |
| Jack,John,Mary | NULL | 0 |
| NULL | , | 0 |

测试语句

```
FROM T1;
```

测试结果

**var1(VARCHAR)**

Mary NULL NULL NULL

##### TO_DATE

本文为您介绍如何使用TO_DATE函数，将INT类型或者VARCHAR类型的日期转换成DATE类型。 本文仅适用于VVP 2.4.0且VVR 3.0.0及以上版本。

**重要**

**语法**

实时计算（流计算） 参考

**入参**

| 参数 | 数据类型 | 说明 |
|---|---|---|
| time | INT | 表示从1970-1-1到所表示时间之间天数。 |
| date | VARCHAR | 默认格式为yyyy-MM-dd。 |
| format | VARCHAR | 日期格式。 |

**示例**

测试数据表 1. T1

| date1(INT) | date2(VARCHAR) | date3(VARCHAR) |
|---|---|---|
| 100 | 2017-09-15 | 20170915 |

测试语句

```
SELECT TO_DATE(date1) as var1,
 TO_DATE(date2) as var2,
FROM T1;
```

测试结果

| var1(DATE) | var2(DATE) | var3(DATE) |
|---|---|---|
| 1970-04-11 | 2017-09-15 | 2017-09-15 |

##### TO_TIMESTAMP_TZ

本文为您介绍如何使用TO_TIMESTAMP_TZ函数，将VARCHAR类型的日期根据指定时区转换成 TIMESTAMP类型。 本文仅适用于VVP 2.4.0且VVR 3.0.0及以上版本。

**重要**

**语法**

```
TIMESTAMP TO_TIMESTAMP_TZ(VARCHAR date, VARCHAR timezone) TIMESTAMP TO_TIMESTAMP_TZ(VARCHAR date, VARCHAR format，VARCHAR timezone)
```

**入参**

| 参数 | 数据类型 | 说明 |
|---|---|---|
| timezone | VARCHAR | 字符串表示的时区，例如Asia/Shanghai。 |

实时计算（流计算） 参考

| date | VARCHAR | 默认格式为yyyy-MM-dd HH:mm:ss。 |
|---|---|---|
| format | VARCHAR | 日期格式。 |

**示例**

测试数据表 1. T1

| timestamp1(VARCHAR) | format1(VARCHAR) | timezone1(VARCHAR) |
|---|---|---|
| 1970-01-01 00:00:00 | yyyy-MM-dd HH:mm:ss | Asia/Shanghai |

测试语句

```
SELECT
     UNIX_TIMESTAMP(TO_TIMESTAMP_TZ(timestamp1, timezone1)) as var1,
     UNIX_TIMESTAMP(TO_TIMESTAMP_TZ(timestamp1, format1, timezone1)) as var2
FROM T1;
```

测试结果

| var1(BIGINT) | var2(BIGINT) |
|---|---|
| -28800 | -28800 |

##### UNIX_TIMESTAMP

本文仅适用于VVP 2.4.0且VVR 3.0.0及以上版本。

**重要**

**语法**

```
BIGINT UNIX_TIMESTAMP(VARCHAR date, VARCHAR format)
```

**入参**

| 参数 | 数据类型 | 说明 |
|---|---|---|
| timestamp | TIMESTAMP | 无。 |
| date | VARCHAR | 默认日期格式为 yyyy-MM-dd HH:mm:ss 。 |
| format | VARCHAR | 默认日期格式为 yyyy-MM-dd hh:mm:ss 。 |

**示例**

测试数据表 1. T1

| date1(VARCHAR) | date2(VARCHAR) |
|---|---|

实时计算（流计算） 参考

| 2021-03-25 00:00:00 | 1970-01-01 00:00:00 |
|---|---|

测试语句

```
SELECT UNIX_TIMESTAMP(to_timestamp_tz(date1)) as big1, FROM T1;
```

测试结果

| big1（BIGINT） | big2（BIGINT） |
|---|---|
| 1616601600 | -28800 |

#### 表值函数

##### GENERATE_SERIES

本文为您介绍如何使用GENERATE_SERIES函数，按from、from+1、from+2 … to-1的规则，生成一系列填充数据。

**重要**

本文仅适用于VVP 2.4.0且VVR 3.0.0及以上版本。

**语法**

**入参**

| 参数 | 数据类型 |
|---|---|
| from | INT类型，指定下界，包含下界值。 |
| to | INT类型，指定上界，不包含上界值。 |

**示例**

测试数据表 1. T1

| s(INT) | e(INT) |
|---|---|
| 1 | 3 |
| -2 | 1 |

测试语句

```
SELECT s, e, v as v;
```

测试结果实时计算（流计算） 参考

| s(INT) | e(INT) | v(INT) |
|---|---|---|
| 1 | 3 | 1 |
| 1 | 3 | 2 |
| -2 | 1 | -2 |
| -2 | 1 | -1 |
| -2 | 1 | 0 |

##### JSON_TUPLE

本文为您介绍如何使用JSON_TUPLE函数，从JSON字符串中取出各路径字符串所表示的值。 本文仅适用于VVP 2.4.0且VVR 3.0.0及以上版本。

**重要**

**语法**

**入参**

| 参数 | 数据类型 | 说明 |
|---|---|---|
| str | VARCHAR | JSON字符串。 |
| path1～pathN | VARCHAR | 表示路径的字符串，前面不需要 $ 。 |

**示例**

测试数据表 1. T1

| d(VARCHAR) | s(VARCHAR) |
|---|---|
| {"qwe":"asd","qwe2":"asd2","qwe3":"asd3"} | qwe3 |
| {"qwe":"asd4","qwe2":"asd5","qwe3":"asd3"} | qwe2 |

测试语句

```
SELECT d, v AS T(v);
```

测试结果

| d(VARCHAR) | v(VARCHAR) |
|---|---|
| {"qwe":"asd","qwe2":"asd2","qwe3":"asd3"} | asd |
| {"qwe":"asd","qwe2":"asd2","qwe3":"asd3"} | asd3 |

实时计算（流计算） 参考

| {"qwe":"asd4","qwe2":"asd5","qwe3":"asd3"} | asd4 |
|---|---|
| {"qwe":"asd4","qwe2":"asd5","qwe3":"asd3"} | asd5 |

##### MULTI_KEYVALUE

本文为您介绍如何使用MULTI_KEYVALUE函数，将目标字符串中拆分为Key-Value（KV）对，匹配split1 和split2的KV对，并返回key_name1和key_name2对应的Value值。 本文仅适用于VVP 2.4.0且VVR 3.0.0及以上版本。

**重要**

**语法**

```
MULTI_KEYVALUE(VARCHAR str, VARCHAR split1, VARCHAR split2, VARCHAR key_name1, VARCHAR key_name2, ...)
```

**入参**

| 参数 | 数据类型 | 说明 |
|---|---|---|
| str | VARCHAR | 目标字符串。 |
| split1 | VARCHAR | KV对的分隔符。 当split1为NULL时，表示按照空格作为KV对的分割符。 当split1的长度>1时，split1仅表示分隔符的集合，每个字符都表示一个有效的分隔符。 |
| split2 | VARCHAR | KV的分隔符。 当split2为NULL时，表示按照空格作为KV的分割符。当 split2的长度>1时，split2仅表示分隔符的集合，每个字符都表示一个有效的分隔符。 |
| key name1, _ key name2, ... _ | VARCHAR | 需要获取Value的Key值列表。 |

**示例**

测试数据表 1. T1

| str(VARCHAR) | split1(VARCHA R) | split2(VARCHA R) | key1(VARCHAR ) | key2(VARCHAR ) |
|---|---|---|---|---|
| k1=v1;k2=v2 | ; | = | k1 | k2 |
| NULL | ; | = | k1 | k2 |
| k1:v1;k2:v2 | ; | : | k1 | k3 |
| k1:v1;k2:v2 | ; | = | k1 | k2 |
| k1:v1;k2:v2 | , | : | k1 | k2 |
| k1:v1;k2=v2 | ; | : | k1 | k2 |

实时计算（流计算） 参考

| k1:v1abck2:v2 | abc | : | k1 | k2 |
|---|---|---|---|---|
| k1:v1;k2=v2 | ; | := | k1 | k2 |
| k1:v1 k2:v2 | NULL | : | k1 | k2 |
| k1 v1;k2 v2 | ; | NULL | k1 | k2 |

测试语句

```
SELECT c1, c2 FROM T1, lateral table(MULTI_KEYVALUE(str, split1, split2, key1, key2)) as T(c1, c2);
```

测试结果

| c1(VARCHAR) | c2(VARCHAR) |
|---|---|
| v1 | v2 |
| NULL | NULL |
| v1 | NULL |
| NULL | NULL |
| NULL | NULL |
| v1 | NULL |
| v1 | v2 |
| v1 | v2 |
| v1 | v2 |
| v1 | v2 |

##### STRING_SPLIT

本文为您介绍如何使用STRING_SPLIT函数，根据指定的分隔符将目标字符串拆分为子字符串，并返回子字符串列表。 本文仅适用于VVP 2.4.0且VVR 3.0.0及以上版本。

**重要**

**语法**

**入参**

| 参数 | 数据类型 | 说明 |
|---|---|---|
| string | VARCHAR | 目标字符串。 |

实时计算（流计算） 参考

| separator | VARCHAR | 指定的分隔符。 说明 separator暂不支持多字符串形式，只支持单字符串形式。 |
|---|---|---|

**说明**

如果string为NULL，则返回一个空行。 如果string包含两个或多个连续出现的分隔符时，则返回长度为零的空子字符串。 如果string未包含指定分隔符，则返回目标字符串。

**示例**

测试数据表 1. T1

| d(varchar) | s(varchar) |
|---|---|
| abc-bcd | - |
| hhh | - |

测试语句

```
SELECT d,v FROM T1, lateral table(string_split(d, s)) as T(v);
```

测试结果

| d(varchar) | v(varchar) |
|---|---|
| abc-bcd | abc |
| abc-bcd | bcd |
| hhh | hhh |

#### 聚合函数

##### APPROX_COUNT_DISTINCT

本文为您可以介绍如何使用APPROX_COUNT_DISTINCT函数，提升作业性能。 本文仅适用于VVP 2.4.0且VVR 3.0.0及以上版本。

**重要**

**背景信息**

Count Distinct优化时，Aggregate节点的State需要保存所有Distinct Key信息。当Distinct Key数目过大时，State的读写开销太大，因此Count Distinct优化存在性能瓶颈。但在很多场景，完全精确的统计并不那么必要。如果您希望牺牲部分精确度来换取性能上的提升，您可以使用新增的内置函数**APPROX_COUNT_DISTINCT**提升作业性能。**APPROX_COUNT_DISTINCT**支持MiniBatch或 Local-Global等Aggregate上的优化，但是需要注意以下几点： 实时计算（流计算） 参考输入不含有撤回消息。 Distinct Key数目需要足够大，例如UV。如果Distinct Key数目不

**语法**

**入参**

| 参数 | 数据类型 | 说明 |
|---|---|---|
| col | 任意类型 | 字段名称 |
| accuracy | FLOAT | 可选，准确率，取值范围为(0.0, 1.0)，默认值为 0.99，取值越高，准确率越高，state开销越大，性能越低。 |

**示例**

测试数据表 1. T1

| a (VARCHAR) | c (BIGINT) |
|---|---|
| Hi | 1 |
| Hi | 2 |
| Hi | 3 |
| Hi | 4 |
| Hi | 5 |
| Hi | 6 |

测试代码

```
SELECT
```

`a,`

```
  APPROX_COUNT_DISTINCT(b) as b,
FROM T1 GROUP BY a;
```

测试结果

| a (VARCHAR) | b (BIGINT) | c (BIGINT) |
|---|---|---|
| Hi | 6 | 6 |

##### FIRST_VALUE

本文为您介绍如何使用FIRST_VALUE函数，返回指定数据流的第1条非NULL数据。 实时计算（流计算） 参考本文仅适用于VVP 2.4.0且VVR 3.0.0及以上版本。

**重要**

**语法**

**入参**

| 参数 | 数据类型 | 说明 |
|---|---|---|
| value | 任意参数类型 | 指定数据流。 说明如果输入数据全为NULL，则返回 NULL。 |
| order | BIGINT | 根据order判定FIRST VALUE所在行，取order值最小的 _ 记录作为FIRST VALUE。 _ |

所有输入参数需要为相同的数据类型。

**重要**

**示例**

测试数据表 1. T1

| a(BIGINT) | b(INT) | c(VARCHAR) |
|---|---|---|
| 1 | 1 | Hello |
| 2 | 2 | Hello |
| 3 | 3 | Hello |
| 4 | 4 | Hello |
| 5 | 5 | Hello |
| 6 | 6 | Hello |
| 7 | 7 | NULL |
| 8 | 7 | Hello World |
| 9 | 8 | Hello World |
| 10 | 20 | Hello World |

测试语句

```
OVER (PARTITION BY c ORDER BY PROCTIME() RANGE UNBOUNDED PRECEDING) AS var1 FROM T1;
```

测试结果实时计算（流计算） 参考

| c(VARCHAR) | var1(INT) |
|---|---|
| Hello | 1 |
| Hello | 1 |
| Hello | 1 |
| Hello | 1 |
| Hello | 1 |
| Hello | 1 |
| NULL | 7 |
| Hello World | 7 |
| Hello World | 7 |
| Hello World | 7 |

##### LAST_VALUE

本文为您介绍如何使用LAST_VALUE函数，返回指定数据流的最后1条非NULL数据。 本文仅适用于VVP 2.4.0且VVR 3.0.0及以上版本。

**重要**

**语法**

**入参**

| 参数 | 数据类型 | 说明 |
|---|---|---|
| value | 任意参数类型 | 指定数据流。 |
| order | BIGINT | 根据order判定LAST VALUE所在的行，取order值最大 _ 的记录作为LAST VALUE。 _ |

所有输入参数需要为相同的数据类型。

**重要**

**示例**

测试数据表 1. T1

| a(BIGINT) | b(INT) | c(VARCHAR) |
|---|---|---|
| 1 | 1 | Hello |
| 2 | 2 | Hello |

实时计算（流计算） 参考

| 3 | 3 | Hello |
|---|---|---|
| 4 | 4 | Hello |
| 5 | 5 | Hello |
| 6 | 6 | Hello |
| 7 | 7 | NULL |
| 8 | 7 | Hello World |
| 9 | 8 | Hello World |
| 10 | 20 | Hello World |

测试语句

```
OVER (PARTITION BY c ORDER BY PROCTIME() RANGE UNBOUNDED PRECEDING) AS var1 FROM T1;
```

测试结果

| c(VARCHAR) | var1(INT) |
|---|---|
| Hello | 1 |
| Hello | 2 |
| Hello | 3 |
| Hello | 4 |
| Hello | 5 |
| Hello | 6 |
| NULL | 7 |
| Hello World | 7 |
| Hello World | 8 |
| Hello World | 20 |

### 自定义函数（Datastream）

#### 概述

本文为您介绍Flink自定义函数开发时的注意事项、自定义函数的分类、定义和参数传递方法。

**注意事项**

为了避免JAR包依赖冲突，在开发自定义函数时您需要注意以下几点： 作业开发页面选择的Flink版本，请和Pom依赖中的Flink版本保持一致。 实时计算（流计算） 参考 Flink相关依赖，scope请使用provided，即在依赖中添加 `<scope>provided</scope>` 。 其他第三方依赖请采用Shade方式打包，Shade打包详情请参见Apache Maven Shade Plugin。

**自定义函数分类**

Flink支持以下3类自定义函数。

| 分类 | 描述 |
|---|---|
| UDF（User Defined Scalar Function） | 用户自定义标量值函数，将0个、1个或多个标量值映射到一个新的标量值。其输入与输出是一对一的关系，即读入一行数据，写出一条输出值。详情请参见自定义标量函数（UDF）。 |
| UDAF（User Defined Aggregation Function） | 自定义聚合函数，将多条记录聚合成1条记录。其输入与输出是多对一的关系，即将多条输入记录聚合成一条输出值。详情请参见自定义聚合函数（UDAF）。 |
| UDTF（User Defined Table-valued Function） | 自定义表值函数，将0个、1个或多个标量值作为输入参数（可以是变长参数）。与自定义的标量函数类似，但与标量函数不同。表值函数可以返回任意数量的行作为输出，而不仅是1个值。返回的行可以由1 个或多个列组成。调用一次函数输出多行或多列数据。详情请参见自定义表值函数（UDTF）。 |

**自定义函数参数传递**

如果您的自定义函数中某些参数值后期需要修改，直接在UDF代码里修改会很麻烦。此时，您可以在Flink全托管控制台更多Flink配置项中配置该参数后，在UDF代码中使用该参数。后续您可以直接在Flink全托管控制台修改该参数值，从而达到快速修改UDF参数值的目的。 自定义函数中提供了可选的open(FunctionContext context)方法，FunctionContext具备参数传递功能，自定义配置项通过此对象来传递。自定义函数的参数传递操作步骤如下：
1. 在作业开发页面右侧**高级配置**面板**更多****Flink****配置**中添加参数及取值。代码示例如下。

```
maxJobCreationAttempts: value
```

2. 在UDF代码中通过ConfigOptions.key()方式获取自定义函数参数。代码示例如下。

```
String strValue = context.getJobParameter("key","default_value"); Integer intValue = Integer.parseInt(context.getJobParameter("key","default_value"));
```

如果函数参数是key-value格式的，只能使用FunctionContext#getJobParameter方法获取 pipeline.global-job-parameters配置项的值。在pipeline.global-job-parameters中定义key-value 时，key和value之间需要通过半角冒号（:）分隔，不同kv之间需要通过逗号（,）分隔。如果key或 value中含有半角冒号或逗号，需要使用半角双引号（"）包围起来。如果在此情况下key或value中还含有半角双引号，则需要通过连写两个半角双引号（""）进行转义。代码示例如下。

```
pipeline.global-job-parameters: 'json1:"{k1:""value1""}",json2:"k2"'
```

该配置就定义了以下的map。

| key | value |
|---|---|
| json1 | {k1:""value1""} |
| json2 | k2 |

此时就能通过FunctionContext#getJobParameter获取上述map的各项内容。

```
context.getJobParameter("json1", null); // 获得字符串{k1:""value1""}
```

实时计算（流计算） 参考

**自定义函数注册方法**

自定义函数分为全局自定义函数和作业级自定义函数，注册方法详情如下所示： 全局自定义函数 i. 登录实时计算开发平台。 ii. 在左侧导航栏上，单击**作业开发**。 iii. 在**UDFs**页签，单击图标。 iv. 上传自定义函数JAR文件。 您可以通过以下任何一种方式上传自定义函数JAR文件：
**上传文件**：单击**选择文件**项右侧的**选择文件**后，选择您的目标自定义函数JAR文件。如果有依赖文
件，单击**依赖文件**项右侧的**选择文件**，选择您的目标自定义函数JAR所依赖的文件。
**外部****URL**：输入外部URL地址。

**说明**

您的自定义函数JAR文件会被上传到您选择的OSS Bucket中的sql-artifacts目录下。此外，Flink开发控制台会解析自定义函数JAR文件中是否使用了Flink UDF、UDAF和UDTF接口的类，并自动提取类名，填充到Function Name字段中。 对于Java类型的UDF，其依赖可以打包到自定义函数JAR包中，也可以通过依赖文件项进行上传。 在自定义函数文件或者其依赖文件比较大时，推荐通过外部URL的方式进行上传。需要注意的是，如果外部URL是OSS Bucket地址，其依赖文件必须位于sqlartifacts/namespaces/{namespace}目录下。 v. 单击**确认**。 在SQL编辑器页面左侧**UDFs**列表，您可以看到所有注册成功的UDF。 作业级自定义函数因全局自定义函数（Catalog Function）在注册时，默认使用最新的Flink版本解析。如果您在作业中使用全局自定义函数，同时在高级配置选中了非最新的Flink版本，则有可能出现不兼容的问题。此时，您可以根据作业需要使用的引擎版本来实现UDF代码，并通过作业级自定义函数的方式解决此问题。作业级自定义函数的使用流程如下： i. 上传自定义函数JAR包。 在左侧导航栏**资源上传**中，上传自定义函数JAR包。 ii. 在作业中指定作业级自定义函数。 实时计算（流计算） 参考在作业**附加依赖文件**中，指定自定义函数JAR包。 iii. 注册自定义函数。 通过 `CREATE TEMPORARY FUNCTION` 语法注册作业级自定义函数。

```
CREATE TEMPORARY FUNCTION MyScalarFunc AS 'com.test.MyScalarFunc';
```

#### 自定义标量函数（UDF）

**定义**

自定义标量函数（UDF）将0个、1个或多个标量值映射到一个新的标量值。输入与输出是一对一的关系，即读入一行数据，写出一条输出值。

**UDF开发**

Flink为您提供了UDX示例，便于您快速开发业务。Flink UDX示例中包含UDF、UDAF和

**说明**

UDTF的实现，示例中已为您配置对应版本的开发环境，您无需进行环境搭建。
1. 下载并解压ASI_UDX_Demo示例到本地。
解压完成后，会生成**ASI_UDX-main**文件夹。其中：
**pom.xml**：项目级别的配置文件，主要描述了项目的Maven坐标、依赖关系，开发者需要遵循的规
则、缺陷管理系统，组织和Licenses，以及其他所有的项目相关因素。
**\ASI_UDX-main\src\main\java\ASI_UDF\ASI_UDF.java**：自定义标量函数（UDF）示例的
Java代码。
2. 在Intellij IDEA中，单击**file > open**，打开刚才解压缩完成的**ASI_UDX-main**。
3. 双击打开\ASI_UDX-main\src\main\java\ASI_UDF后，根据您的业务，配置**ASI_UDF.java**。
该示例中，**ASI_UDF.java**已配置了获取每条数据中从begin~end位的字符的代码。

```java
package ASI_UDF; import org.apache.flink.table.functions.ScalarFunction; public class ASI_UDF extends ScalarFunction {
    public String eval(String s, Integer begin, Integer end) {
        return s.substring(begin, end);
    }
}
```

4. 双击打开\ASI_UDX-main\后，配置**pom.xml**。
该示例中，**pom.xml**文件已配置了Flink 1.11版依赖的主要JAR包信息。如果您的业务： Flink 1.11版依赖的主要JAR包如下。 实时计算（流计算） 参考

```xml
<dependencies>
        <dependency>
            <groupId>org.apache.flink</groupId>
            <artifactId>flink-streaming-java_2.12</artifactId>
            <version>1.11.0</version>
            <!--<scope>provided</scope>-->
        </dependency>
        <dependency>
            <groupId>org.apache.flink</groupId>
            <artifactId>flink-table</artifactId>
            <version>1.11.0</version>
            <type>pom</type>
            <!--<scope>provided</scope>-->
        </dependency>
        <dependency>
            <groupId>org.apache.flink</groupId>
            <artifactId>flink-core</artifactId>
            <version>1.11.0</version>
        </dependency>
        <dependency>
            <groupId>org.apache.flink</groupId>
            <artifactId>flink-table-common</artifactId>
            <version>1.11.0</version>
        </dependency>
    </dependencies>
```

5. 在下载文件中**pom.xml**所在的目录执行如下命令打包文件。

```
mvn package -Dcheckstyle.skip
```

\ASI_UDX-main\target\目录下会出现**ASI_UDX-1.0-SNAPSHOT.jar**的JAR包，即代表完成了UDF开发工作。

**UDF注册**

UDF注册过程，请参见管理自定义函数（UDF）。

**UDF使用**

在注册UDF完成后，您就可以使用UDF，详细的操作步骤如下。
1. Flink SQL作业开发。详情请参见作业开发。
获取ASI_UDF_Source表中a字段中每行字符串中第2~4位的字符，代码示例如下。 实时计算（流计算） 参考

```
CREATE TEMPORARY TABLE ASI_UDF_Source (
  a VARCHAR,
  b INT,
  c INT
) WITH ( ); CREATE TEMPORARY TABLE ASI_UDF_Sink (
  a VARCHAR
) WITH ( ); INSERT INTO ASI_UDF_Sink SELECT ASI_UDF('a',2,4) FROM ASI_UDF_Source;
```

2. 在**作业列表**中，单击目标作业名称**操作**列的**启动**。
启动成功后，ASI_UDF_Sink表每行会被插入ASI_UDF_Source表中a字段每行字符串的第2~4位字符。

#### 自定义聚合函数（UDAF）

**定义**

自定义聚合函数（UDAF），将多条记录聚合成1条记录。其输入与输出是多对一的关系，即将多条输入记录聚合成一条输出值。

**UDAF开发**

**说明**

Flink为您提供了UDF示例，便于您快速开发业务。Flink UDF示例中包含UDSF、UDAF和UDTF的实现，示例中已为您配置对应版本的开发环境，您无需进行环境搭建。
1. 下载并解压ASI_UDX_Demo示例到本地。
解压完成后，会生成**ASI_UDX-main**文件夹。其中：
**pom.xml**：项目级别的配置文件，主要描述了项目的Maven坐标、依赖关系，开发者需要遵循的规
则、缺陷管理系统，组织和Licenses，以及其他所有的项目相关因素。
**\ASI_UDX-main\src\main\java\ASI_UDAF\ASI_UDAF.java**：自定义聚合函数（UDAF）示例
的Java代码。
2. 在Intellij IDEA中，单击**file > open**，打开刚才解压缩完成的**ASI_UDX-main**。
3. 双击打开\ASI_UDX-main\src\main\java\ASI_UDAF后，根据您的业务，配置**ASI_UDAF.java**。
该示例中，**ASI_UDAF.java**已配置了当前数据和历史数求和的代码。例如，第1个数据是1，第2个数据是2，第3个数据是3，则第一个结果是1，第2个结果是3，第3个结果是6。 实时计算（流计算） 参考

```java
package ASI_UDAF; import org.apache.flink.table.functions.AggregateFunction; public class ASI_UDAF{
    public static class AcSum {
        public long sum;
    }
    public static class WeightedSum extends AggregateFunction<Long, AcSum> {
        @Override
        public Long getValue(AcSum acSum) {
            return acSum.sum;
        }
        @Override
        public AcSum createAccumulator() {
            AcSum acCount = new AcSum();
            acCount.sum = 0;
            return acCount;
        }
        public void accumulate(AcSum acc, long acSum) {
            acc.sum += acSum;
        }
    }
}
```

4. 双击打开\ASI_UDX-main\后，配置**pom.xml**。
该示例中，**pom.xml**文件已配置了Flink 1.11版依赖的主要JAR包信息。如果您的业务： Flink 1.11版依赖的主要JAR包如下。 实时计算（流计算） 参考

```xml
<dependencies>
        <dependency>
            <groupId>org.apache.flink</groupId>
            <artifactId>flink-streaming-java_2.12</artifactId>
            <version>1.11.0</version>
            <!--<scope>provided</scope>-->
        </dependency>
        <dependency>
            <groupId>org.apache.flink</groupId>
            <artifactId>flink-table</artifactId>
            <version>1.11.0</version>
            <type>pom</type>
            <!--<scope>provided</scope>-->
        </dependency>
        <dependency>
            <groupId>org.apache.flink</groupId>
            <artifactId>flink-core</artifactId>
            <version>1.11.0</version>
        </dependency>
        <dependency>
            <groupId>org.apache.flink</groupId>
            <artifactId>flink-table-common</artifactId>
            <version>1.11.0</version>
        </dependency>
    </dependencies>
```

5. 在下载文件中**pom.xml**所在的目录执行如下命令打包文件。

```
mvn package -Dcheckstyle.skip
```

\ASI_UDX-main\target\目录下会出现**ASI_UDX-1.0-SNAPSHOT.jar**的JAR包，即代表完成了UDAF 开发工作。

**UDAF注册**

UDAF注册过程，请参见管理自定义函数（UDF）。

**UDAF使用**

在注册UDAF完成后，您就可以使用UDAF，详细的操作步骤如下。
1. Flink SQL作业开发。详情请参见作业开发。
获取ASI_UDAF_Source表中a字段当前数据和历史数据之和，代码示例如下。 实时计算（流计算） 参考

```
CREATE TEMPORARY TABLE ASI_UDAF_Source (
  a   BIGINT
) WITH ( ); CREATE TEMPORARY TABLE ASI_UDAF_Sink (
  sum  BIGINT
) WITH ( ); INSERT INTO ASI_UDAF_Sink SELECT `ASI_UDAF$WeightedSum`(a) FROM ASI_UDAF_Source;
```

2. 在**作业列表**中，单击目标作业名称**操作**列的**启动**。
启动成功后，ASI_UDAF_Sink表每行会被插入ASI_UDAF_Source表中a字段当前数据和历史数据之和。

#### 自定义表值函数（UDTF）

**定义**

自定义表值函数（UDTF），自定义表值函数，将0个、1个或多个标量值作为输入参数（可以是变长参数）。与自定义的标量函数类似，但与标量函数不同。表值函数可以返回任意数量的行作为输出，而不仅是 1个值。返回的行可以由1个或多个列组成。调用一次函数输出多行或多列数据。

**UDTF开发**

**说明**

Flink为您提供了UDF示例，便于您快速开发业务。Flink UDF示例中包含UDSF、UDAF和UDTF的实现，示例中已为您配置对应版本的开发环境，您无需进行环境搭建。
1. 下载并解压ASI_UDX_Demo示例到本地。
解压完成后，会生成**ASI_UDX-main**文件夹。其中：
**pom.xml**：项目级别的配置文件，主要描述了项目的Maven坐标、依赖关系，开发者需要遵循的规
则、缺陷管理系统，组织和Licenses，以及其他所有的项目相关因素。
**\ASI_UDX-main\src\main\java\ASI_UDF\ASI_UDTF.java**：自定义表值函数（UDTF）示例的
Java代码。
2. 在Intellij IDEA中，单击**file > open**，打开刚才解压缩完成的**ASI_UDX-main**。
3. 双击打开\ASI_UDX-main\src\main\java\ASI_UDTF后，根据您的业务，修改**ASI_UDTF.java**文件内
容。 该示例中，**ASI_UDTF.java**已配置了将一行字符串按照竖线（|）分割成多列字符串的代码。 实时计算（流计算） 参考

```java
package ASI_UDTF; import org.apache.flink.api.java.tuple.Tuple2; import org.apache.flink.table.functions.TableFunction; public class ASI_UDTF extends TableFunction<Tuple2<String,String>> {
    public void eval(String str){
        String[] split = str.split("\\|");
        String name = split[0];
        String place = split[1];
        Tuple2<String,String> tuple2 = Tuple2.of(name,place);
        collect(tuple2);
    }
}
```

4. 双击打开\ASI_UDX-main\后，配置**pom.xml**。
该示例中，**pom.xml**文件已配置了Flink 1.11版依赖的主要JAR包信息。如果您的业务： Flink 1.11版依赖的主要JAR包如下。

```xml
<dependencies>
        <dependency>
            <groupId>org.apache.flink</groupId>
            <artifactId>flink-streaming-java_2.12</artifactId>
            <version>1.11.0</version>
            <!--<scope>provided</scope>-->
        </dependency>
        <dependency>
            <groupId>org.apache.flink</groupId>
            <artifactId>flink-table</artifactId>
            <version>1.11.0</version>
            <type>pom</type>
            <!--<scope>provided</scope>-->
        </dependency>
        <dependency>
            <groupId>org.apache.flink</groupId>
            <artifactId>flink-core</artifactId>
            <version>1.11.0</version>
        </dependency>
        <dependency>
            <groupId>org.apache.flink</groupId>
            <artifactId>flink-table-common</artifactId>
            <version>1.11.0</version>
        </dependency>
    </dependencies>
```

5. 在下载文件中**pom.xml**所在的目录执行如下命令打包文件。

```
mvn package -Dcheckstyle.skip
```

\ASI_UDX-main\target\目录下会出现**ASI_UDX-1.0-SNAPSHOT.jar**的JAR包，即代表完成了UDTF 开发工作。 实时计算（流计算） 参考

**UDTF注册**

UDTF注册过程，请参见管理自定义函数（UDF）。

**UDTF使用**

在注册UDTF完成后，您就可以使用UDTF，详细的操作步骤如下。
1. Flink SQL作业开发。详情请参见作业开发。
ASI_UDTF_Source表中message字段每行字符串按照竖线（|）分割成多列，代码示例如下。

```
CREATE TEMPORARY TABLE ASI_UDTF_Source (
  `message`  VARCHAR
) WITH ( ); CREATE TEMPORARY TABLE ASI_UDTF_Sink (
  name  VARCHAR,
  place  VARCHAR
) WITH ( ); INSERT INTO ASI_UDTF_Sink SELECT name,place FROM ASI_UDTF_Source,lateral table(ASI_UDTF(`message`)) as T(name,place);
```

2. 在**作业列表**中，单击目标作业名称**操作**列的**启动**。
启动成功后，ASI_UDTF_Sink表会被插入ASI_UDTF_Source表中message字段按照竖线（|）分割成多列的字符。

### 自定义函数（Python）

#### 概述

Flink支持在SQL作业中使用Python自定义函数，本文为您介绍Flink自定义函数UDX的分类、定义和依赖， 以及如何进行调试和调优。

**UDX分类**

Flink支持以下3类自定义函数。

| UDX分类 | 描述 |
|---|---|
| UDF（User Defined Scalar Function） | 用户自定义标量函数，将0个、1个或多个标量值映射到一个新的标量值。 其输入与输出是一对一的关系，即读入一行数据，写出一条输出值。详情请参见自定义标量函数（UDF）。 |
| UDAF（User Defined Aggregation Function） | 自定义聚合函数，将多条记录聚合成1条记录。其输入与输出是多对一的关系，即将多条输入记录聚合成一条输出值。详情请参见自定义聚合函数 （UDAF）。 |
| UDTF（User Defined Table-valued Function） | 自定义表值函数，将0个、1个或多个标量值作为输入参数（可以是变长参数）。与自定义的标量函数类似，但与标量函数不同。表值函数可以返回任意数量的行作为输出，而不仅是1个值。返回的行可以由1个或多个列组成。调用一次函数输出多行或多列数据。详情请参见自定义表值函数 （UDTF）。 |

实时计算（流计算） 参考

**依赖**

Flink集群已预装了Pandas、NumPy和PyArrow等常用的Python包，您可以在作业开发页面，了解Flink集群中已安装的第三方Python包列表。 此外，您也可以在Python自定义函数中使用其它类型的第三方Python包。需要注意的是，如果使用了非预装的第三方Python包，在注册Python UDF时，需要将其作为依赖文件上传，详情请参见管理自定义函数和使用Python依赖。

**调试**

您可以在Python自定义函数的代码实现中，通过Logging的方式，输出日志信息，方便问题定位，示例如下。

```python
@udf(result_type=DataTypes.BIGINT()) def add(i, j):
  logging.info("hello world")
  return i + j
```

日志输出后，您可以在TaskManager的日志文件中查看日志。

**调优**

使用Pandas库除了普通Python自定义函数之外，Flink也支持您使用Pandas自定义函数。对于Pandas自定义函数，输入数据的类型是Pandas中定义的数据结构，例如pandas.Series和pandas.DataFrame等，您可以在 Pandas自定义函数中使用Pandas和Numpy等高性能的Python库，开发出高性能的Python自定义函数，详情请参见Vectorized User-defined Functions。 配置以下参数 Python自定义函数的性能在很大程度取决于Python自定义函数自身的实现，如果遇到性能问题，您需要尽可能优化Python自定义函数的实现。除此之外，Python自定义函数的性能也受以下参数取值的影响。

| 参数 | 说明 |
|---|---|
| python.fn- execution.bundle.size | Python UDF的计算是异步的，在执行过程中，Java算子将数据异步发送给 Python进程进行处理。Java算子在将数据发送给Python进程之前，会先将数据缓存起来，到达一定阈值之后，再发送给Python进程。python.fn- execution.bundle.size参数可用来控制可缓存的数据最大条数。 默认值为100000，单位是条数。 |
| python.fn- execution.bundle.time | 用来控制数据的最大缓存时间。当缓存的数据条数到达python.fn- execution.bundle.size定义的阈值或缓存时间到达python.fn- execution.bundle.time定义的阈值时，会触发缓存数据的计算。 默认值为1000，单位是毫秒。 |
| python.fn- execution.arrow.batch.size | 使用Pandas UDF时，一个arrow batch可容纳的数据最大条数，默认值为 10000。 说明 python.fn-execution.arrow.batch.size参数值不能大于python.fn-execution.bundle.size参数值。 |

**说明**

以上3个参数并不是配置的越大越好，当这些参数取值配置过大时，可能会导致 Checkpoint时，需要处理过多的数据，从而导致Checkpoint时间过长，甚至会导致Checkpoint失败。以上参数的更多详情，请参见Configuration。 实时计算（流计算） 参考

#### 自定义标量函数（UDF）

本文为您介绍Python自定义标量函数（UDF）的使用限制、开发、注册和使用流程。

**定义**

自定义标量函数（UDF）将0个、1个或多个标量值映射到一个新的标量值。输入与输出是一对一的关系，即读入一行数据，写出一条输出值。

**使用限制**

由于Flink产品受部署环境和网络环境等因素的影响，所以开发Python自定义函数时，需要注意以下限制： 仅支持开源Flink V1.12及以上版本。 Flink集群上已预装了Python 3.7.9，因此需要您在Python 3.7.9版本开发代码。 Flink运行环境使用的是JDK 1.8，如果Python作业中依赖第三方JAR包，请确保JAR包兼容JDK 1.8。 仅支持开源Scala V2.11版本，如果Python作业中依赖第三方JAR包，请确保使用Scala V2.11对应的 JAR包依赖。

**UDF开发**

Flink为您提供了Python UDX示例，便于您快速开发UDX。Flink Python UDX示例中包

**说明**

含了Python UDF、Python UDAF和Python UDTF的实现。本文以Windows操作系统为例，为您介绍如何进行UDF开发。
1. 下载并解压python_demo-master示例到本地。
2. 在PyCharm中，单击**file > open**，打开刚才解压缩完成的**python_demo-master**。
3. 双击打开\python_demo-master\udx\udfs.py后，根据您的业务，修改**udfs.py**。
该示例中，**sub_string**定义了获取每条数据中从begin~end位的字符的代码。

```python
from pyflink.table import DataTypes from pyflink.table.udf import udf @udf(result_type=DataTypes.STRING()) def sub_string(s: str, begin: int, end: int):
    return s[begin:end]
```

4. 在下载文件中udx所在的目录（即\python_demo-master目录）下执行如下命令打包文件。

```
zip -r python_demo.zip udx
```

\python_demo-master\目录下会出现**python_demo.zip**ZIP包，即代表完成了Python UDF的开发工作。

**UDF注册**

UDF注册过程，请参见注册自定义函数。

**UDF使用**

在完成注册UDF后，您就可以使用UDF，详细的操作步骤如下。
1. Flink SQL作业开发。详情请参见作业开发。
获取ASI_UDF_Source表中a字段中每行字符串中第2~4位的字符，代码示例如下。 实时计算（流计算） 参考

```
CREATE TEMPORARY TABLE ASI_UDF_Source (
  a VARCHAR,
  b INT,
  c INT
) WITH ( ); CREATE TEMPORARY TABLE ASI_UDF_Sink (
  a VARCHAR
) WITH ( ); INSERT INTO ASI_UDF_Sink SELECT ASI_UDF(a,2,4) FROM ASI_UDF_Source;
```

2. 在**作业列表**中，单击目标作业名称**操作**列的**启动**。
启动成功后，ASI_UDF_Sink表每行会被插入ASI_UDF_Source表中a字段每行字符串的第2~4位字符。

#### 自定义聚合函数（UDAF）

本文为您介绍Python自定义聚合函数（UDAF）的使用限制、开发、注册和使用流程。

**定义**

自定义聚合函数（UDAF），将多条记录聚合成1条记录。其输入与输出是多对一的关系，即将多条输入记录聚合成一条输出值。

**使用限制**

由于Flink产品受部署环境和网络环境等因素的影响，所以开发Python自定义函数时，需要注意以下限制： 仅支持开源Flink V1.12及以上版本。 Flink集群上已预装了Python 3.7.9，因此需要您在Python 3.7.9版本开发代码。 Flink运行环境使用的是JDK 1.8，如果Python作业中依赖第三方JAR包，请确保JAR包兼容JDK 1.8。 仅支持开源Scala V2.11版本，如果Python作业中依赖第三方JAR包，请确保使用Scala V2.11对应的 JAR包依赖。

**UDAF开发**

Flink为您提供了Python UDX示例，便于您快速开发UDX。Flink Python UDX示例中包

**说明**

含了Python UDF、Python UDAF和Python UDTF的实现。本文以Windows操作系统为例，为您介绍如何进行UDAF开发。
1. 下载并解压python_demo-master示例到本地。
2. 在PyCharm中，单击**file > open**，打开刚才解压缩完成的**python_demo-master**。
3. 双击打开\python_demo-master\udx\udafs.py后，根据您的业务，配置**udafs.py**。
该示例中，**weighted_avg**定义了当前数据和历史数据求含权重的均值的代码。 实时计算（流计算） 参考

```python
from pyflink.common import Row from pyflink.table import AggregateFunction, DataTypes from pyflink.table.udf import udaf class WeightedAvg(AggregateFunction):
    def create_accumulator(self):
        # Row(sum, count)
        return Row(0, 0)
    def get_value(self, accumulator: Row) -> float:
        if accumulator[1] == 0:
            return 0
        else:
            return accumulator[0] / accumulator[1]
    def accumulate(self, accumulator: Row, value, weight):
        accumulator[0] += value * weight
        accumulator[1] += weight
    def retract(self, accumulator: Row, value, weight):
        accumulator[0] -= value * weight
        accumulator[1] -= weight
weighted_avg = udaf(f=WeightedAvg(),
                    result_type=DataTypes.DOUBLE(),
                    accumulator_type=DataTypes.ROW([
                        DataTypes.FIELD("f0", DataTypes.BIGINT()),
                        DataTypes.FIELD("f1", DataTypes.BIGINT())]))
```

4. 在下载文件中udx所在的目录（即\python_demo-master目录）下执行如下命令打包文件。

```
zip -r python_demo.zip udx
```

\python_demo-master\目录下会出现**python_demo.zip**的ZIP包，即代表完成了UDAF开发工作。

**UDAF注册**

UDAF注册过程，请参见注册自定义函数。

**UDAF使用**

在完成注册UDAF后，您就可以使用UDAF，详细的操作步骤如下。
1. Flink SQL作业开发。详情请参见作业开发。
获取ASI_UDAF_Source表中a字段以b字段为权重的a字段当前数据和历史数据的均值，代码示例如下。 实时计算（流计算） 参考

```
CREATE TEMPORARY TABLE ASI_UDAF_Source (
  a   BIGINT,
  b   BIGINT
) WITH ( ); CREATE TEMPORARY TABLE ASI_UDAF_Sink (
  avg_value  DOUBLE
) WITH ( ); INSERT INTO ASI_UDAF_Sink SELECT weighted_avg(a, b) FROM ASI_UDAF_Source;
```

2. 在**作业列表**中，单击目标作业名称**操作**列的**启动**。
启动成功后，ASI_UDAF_Sink表每行会被插入ASI_UDAF_Source表中以b字段为权重的a字段当前数据和历史数据的均值。

#### 自定义表值函数（UDTF）

本文为您介绍Python自定义表值函数（UDTF）的使用限制、开发、注册和使用流程。

**定义**

自定义表值函数（UDTF），将0个、1个或多个标量值作为输入参数（可以是变长参数）。表值函数可以返回任意数量的行作为输出，而不仅是1个值。返回的行可以由1个或多个列组成。调用一次函数输出多行或多列数据。与自定义的标量函数类似，但与标量函数不同。

**使用限制**

由于Flink产品受部署环境和网络环境等因素的影响，所以开发Python自定义函数时，需要注意以下限制： 仅支持开源Flink V1.12及以上版本。 Flink集群上已预装了Python 3.7.9，因此需要您在Python 3.7.9版本开发代码。 Flink运行环境使用的是JDK 1.8，如果Python作业中依赖第三方JAR包，请确保JAR包兼容JDK 1.8。 仅支持开源Scala V2.11版本，如果Python作业中依赖第三方JAR包，请确保使用Scala V2.11对应的 JAR包依赖。

**UDTF开发**

Flink为您提供了Python UDX示例，便于您快速开发UDX。Flink Python UDX示例中包

**说明**

含了Python UDF、Python UDAF和Python UDTF的实现。本文以Windows操作系统为例，为您介绍如何进行UDTF开发。
1. 下载并解压python_demo-master示例到本地。
2. 在PyCharm中，单击**file > open**，打开刚才解压缩完成的**python_demo-master**。
3. 双击打开\python_demo-master\udx\udtfs.py后，根据您的业务，修改**udtfs.py**文件内容。
该示例中，**split**定义了将一行字符串按照竖线（|）分割成多列字符串的代码。 实时计算（流计算） 参考

```python
from pyflink.table import DataTypes from pyflink.table.udf import udtf @udtf(result_types=[DataTypes.STRING(), DataTypes.STRING()]) def split(s: str):
    splits = s.split("|")
    yield splits[0], splits[1]
```

4. 在下载文件中udx所在的目录（即\python_demo目录）下执行如下命令打包文件。

```
zip -r python_demo.zip udx
```

\python_demo\目录下会出现**python_demo.zip**的ZIP包，即代表完成了UDTF开发工作。

**UDTF注册**

UDTF注册过程，请参见注册自定义函数。

**UDTF使用**

在完成UDTF注册后，您就可以使用UDTF，详细的操作步骤如下。
1. Flink SQL作业开发。详情请参见作业开发。
ASI_UDTF_Source表中每行字符串的message字段与字符串aa按照竖线（|）连接之后，按照竖线（|） 分割成多列，代码示例如下。

```
CREATE TEMPORARY TABLE ASI_UDTF_Source (
  `message`  VARCHAR
) WITH ( ); CREATE TEMPORARY TABLE ASI_UDTF_Sink (
  name  VARCHAR,
  place  VARCHAR
) WITH ( ); INSERT INTO ASI_UDTF_Sink SELECT name,place FROM ASI_UDTF_Source,lateral table(split(concat_ws('|', `message`, 'aa'))) as T(name,place);
```

2. 在**作业列表**中，单击目标作业名称**操作**列的**启动**。
启动成功后，ASI_UDTF_Sink表会被插入两列数据，这两列数据是ASI_UDTF_Source表中message和 aa字段按照竖线（|）连接后，再按照竖线（|）分割成多列的字符。

### 机器学习函数

#### CLUSTER_SERVING

本文以输入格式为input_shape=(?,128)的Tensorflow SavedMode模型为例，为您介绍如何使用机器学

**使用限制**

实时计算（流计算） 参考本文仅适用于VVP 2.4.2及以上版本。

**背景信息**

Analytics Zoo是英特尔®开源的统一大数据分析和AI平台，支持分布式TensorFlow及PyTorch的训练和推理，通过英特尔® OpenVINO工具套件和DL Boost指令集等，提升深度学习工作负载的性能。Analytics Zoo Cluster Serving是Analytics Zoo的分布式推理解决方案，可以部署在Apache Flink集群上进行分布式运算。通过使用Cluster Serving，您无需编写任何机器学习相关代码，即可实现端到端的分布式机器学习推理流程。Analytics Zoo详情请参见Analytics Zoo。 Cluster Serving将其部分功能集成在Flink的内置函数中，支持TensorFlow、PyTorch和OpenVINO的推理模型。您可以直接在Flink开发控制台中调用CLUSTER_SERVING函数，进行分布式机器学习推理。使用 CLUSTER_SERVING函数时，您只需要提供模型文件和数据文件，即可完成机器学习端到端的应用。

**语法**

**入参**

| 参数 | 数据类型 | 说明 |
|---|---|---|
| uri | String | 数据ID。 |
| data | String | 数据。 |

**示例**

测试数据表 1. input.csv

| uri(String) | data(String) |
|---|---|
| my-data | 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 |

测试步骤 i. 登录OSS控制台，上传测试数据input.csv文件至oss://***/input.csv目录。 ii. 在Flink开发控制台，创建源表和结果表、加载模型并将CLUSTER_SERVING函数在线推理的数据插入结果表。 实时计算（流计算） 参考

```
   uri STRING,
  `data` STRING
) WITH (
   'connector' = 'filesystem',
   'path' = 'oss://alink-vvp/artifacts/namespaces/test-module-default/input.csv',
   'format' = 'csv'
);
   uri1 STRING,
   data1 STRING
 ) WITH (
); LOAD MODULE `cluster-serving`; INSERT INTO ClusterServingOutput SELECT cluster_serving(uri, `data`) FROM ClusterServingInput;
```

iii. 在作业**高级配置**的**更多****Flink****配置**和Preview Session集群**其他配置**均增加以下配置，并单击**保存**。

```
pipeline.global-job-parameters: '"modelPath:""[模型目录地址]"""'
```

其中，模型目录地址为您模型文件的OSS存放目录，例如oss://***/tf_auto/。 iv. 在作业运维界面，单击目标作业**操作**列下的**启动**。 测试结果

| uri1 | data1 |
|---|---|
| 0.03932024,0.017788976,-2.2538425E- 4,0.021853039,0.030905273,0.052324444,0.053021688,0.08776 946,0.0625467,0.12149326,0.048770625,0.04533424,0.0927158 6,0.023119276,0.0037812046,0.052707616,0.029312208,0.0235 19568,0.07501668,0.037939064,0.06363185,0.04994791,0.0850 4477,0.06940596,0.052632406,0.028651983,0.02205597,0.0586 1686,0.040175162,0.04682718,0.05283319,0.01967535,0.11177 8766,0.03182444,0.04509241,0.09942829,0.009491239,0.03890 3005,0.11488753,0.019503327,0.0346709,0.060727723,0.03718 308,0.1295206,0.04292037,0.13272661,0.009957914,0.0503708 87,0.03016096,0.067269124,0.09981682,0.08606887,0.0851935 45,0.041775055,0.02956512,0.027142545,0.09836763,0.029330 501,0.040107135,0.0753366,0.068517864,0.020111244,0.08627 1614,0.04449262,0.107297346,0.07932708,0.036529146,0.0148 92701,0.08245985,0.04272034,0.076421194,0.035283472,0.028 554386,0.019374546,0.048012834,0.011391987,0.028220229,0. 054405782,0.037807927,0.085761145,0.07974813,0.04150249,- 0.017132144,0.08219319,0.019887058,0.034193676,0.06221051 ,0.07516215,0.0598385,0.09159884,0.038117558,0.05329266,0. 021038251,0.072046585,0.05561088,0.017538168,0.025691401, 0.08580602,0.02225845,0.117060736,0.060743354,0.11840888, 0.065381594,0.08059649,0.045638822,0.06399781,0.011646094 ,0.043574452,0.123603456,0.045708194,0.05672055,0.0840283 7,0.118181005,0.09657015,0.08259893,0.0010145458,0.031954 847,0.07388758,0.035380267,0.070080444,0.06764534,0.05873 1187,0.022044828,0.094359346,0.05559277,0.032255664,0.073 60537,0.11992536 | 128 |

实时计算（流计算）

## 废弃
