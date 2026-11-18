---
title: "Simple Log Service — Product Introduction (English translation)"
product_version: "v3.18.6-SP2607"
doc_version: "20260729"
source_pages: 12
source_pdf: "03_产品简介_enterprise-ascm-product-introduction.pdf"
source_url: "https://apsara-doc.oss-cn-hangzhou.aliyuncs.com/apsara-pdf/enterprise/v_3_18_6_20260730/sls/zh/enterprise-ascm-product-introduction.pdf"
translation: "unofficial, translated by QwenWork from the Chinese V3.18.6 manual; not an Alibaba Cloud official English publication"
---

# Simple Log Service — Product Introduction

> **Note on this file.** Alibaba Cloud's international documentation portal has **no English
> Product Introduction for SLS in V3.18.6** (English volumes existed for V3.18.3). This document is
> an unofficial English translation of the Chinese V3.18.6 (product version `v3.18.6-SP2607`,
> document date 2026-07-29) manual, for internal reading only. Terminology follows the Chinese text;
> repeated running-header lines emitted by the PDF extractor ("日志服务") have been removed.

Simple Log Service (SLS) is a cloud-native observability and analytics platform that provides
large-scale, low-cost, real-time, platform-level services for Log, Metric and Trace data. SLS
offers one-stop data collection, processing (data transformation), query and analysis,
visualization, alerting, consumption and shipping, comprehensively improving your digital
capabilities in R&D, operations, business operations and security scenarios. SLS provides the
following capabilities:

- **Data collection**: supports Log, Metric and Trace data types and more than 50 kinds of data
  sources, including Alibaba Cloud services, servers and applications, IoT devices, mobile clients,
  open-source software and standard protocols.
- **Query and analysis**: supports real-time query and analysis of PB-scale data, providing more than
  10 query operators, more than 10 machine-learning functions and more than 100 SQL functions, and
  supporting Scheduled SQL and dedicated SQL.
- **Data processing**: provides more than 200 built-in functions, more than 400 regular expressions
  and flexible custom functions to perform filtering, splitting, transformation, enrichment and
  replication, covering data dispatching, normalising and merging scenarios.
- **Visualization**: supports visualisation of query and analysis results with more than 10 chart
  types including tables, line charts, bar charts and maps, and supports customised dashboards built
  on these charts (with embedding and drill-down analysis).
- **Alerting**: an alerting service based on query and analysis; when results meet the alert
  conditions, real-time notifications are sent according to the pre-configured alert tasks.
- **Consumption and shipping**: supports real-time data consumption, applicable to Storm, Flume and
  Flink consumption scenarios; supports real-time data shipping, applicable to shipping data to OSS.

## Product details

**Data collection**

SLS provides more than 50 data ingestion solutions:

- Collects logs, time-series data and Trace data related to servers and applications.
- Collects logs from IoT devices.
- Collects logs of Alibaba Cloud services.
- Collects mobile-end data.
- Collects data from open-source software such as Logstash, Flume, Beats, Fluentd and Telegraph.
- Ingests data through standard protocols such as HTTP, HTTPS, Syslog, Kafka and Prometheus.

**Query and analysis**

SLS supports real-time query and analysis of data:

- Supports exact query, fuzzy query, full-text query and field query.
- Supports contextual query, log clustering, LiveTail, index rebuilding and other features.
- Supports standard SQL:92 syntax.
- Provides dedicated SQL instances.

**Data processing**

SLS provides data processing for normalising, enriching, routing, masking and filtering data:

- *Normalising*: extracts fields and converts formats from messy logs to obtain structured data for
  subsequent stream processing and data-warehouse computing.
- *Enrichment*: joins logs (for example order logs) with dimension tables (for example user profile
  tables) to add more dimensions for analysis.
- *Routing*: transfers logs from overseas regions to the central region through cross-region
  acceleration for global log centralisation.
- *Masking*: masks sensitive information such as passwords, mobile numbers and addresses.
- *Filtering*: filters out logs of critical services for focused analysis.

**Consumption and shipping**

SLS provides consumption and shipping: data can be consumed in real time through SDKs and API
operations, and shipped to OSS in real time through the console. Specifically:

- Consumption by third-party software such as Splunk, QRadar, Logstash and Flume.
- Consumption in Java, Python and Go.
- Consumption through Alibaba Cloud services such as Function Compute and Realtime Compute.
- Consumption through stream computing platforms such as Flink, Spark and Storm.
- Shipping of data to OSS.

**Visualization**

- *Built-in dashboard charts*: tables, line charts, bar charts and more, savable into dashboards.
- *Third-party visualisation*: integrates directly with Grafana, DataV and other tools.

**Alerting**

Alerts can be configured on query and analysis results. After configuration, SLS periodically checks
the results and sends an alert notification when the preset conditions are met, providing real-time
service-status monitoring.

## Product advantages

| Advantage | Description |
|---|---|
| Unified ingestion | Ingests multiple data types from many sources. |
| Intelligent | Provides complete AIOps capabilities, including anomaly detection and root cause analysis. |
| Efficient | Real-time collection and query/analysis of hundreds of billions of data records. |
| One-stop | Collection, processing, query and analysis, visualization, alerting and more in one platform. |
| Elastic | Elastic scaling for PB-scale data. |
| Low O&M cost | Installation, deployment and scaling are automated through the console; a high-availability architecture and service self-checks greatly reduce O&M cost. |

## Scenarios

**Data collection and consumption**

Through LogHub, SLS can ingest various real-time log data at large scale and low cost (Metric,
Event, Binlog, TextLog, Click, and more). Advantages: convenience — more than 50 real-time
collection methods let you build a platform quickly, and strong configuration management reduces O&M
burden; elastic scaling — handles both traffic peaks and business growth.

**Real-time log query and analysis**

LogAnalytics indexes data in LogHub in real time and provides rich query methods (keywords, fuzzy,
context, range, SQL aggregation), and supports Scheduled SQL and dedicated SQL. Strong real-time
capability (queryable as soon as written); massive and low cost (PB/day indexing capability, cost
about 15% of a self-built solution); strong analytical capability (multiple query methods, SQL
aggregation, visualization and alerting).

**Data processing**

Same capabilities as described in *Data processing* above (normalising, enrichment, routing,
masking, filtering).

**Data cleansing and real-time computing (ETL / stream processing)**

LogHub connects with various real-time computing and service systems and provides complete
progress monitoring and alerting; custom consumption can be implemented through SDK/API.
Convenient operation: SDKs and programming frameworks in multiple languages integrate seamlessly with
stream computing engines. Complete features: an alerting mechanism with rich monitoring data. Elastic
scaling: PB-level elasticity with zero latency.

**Data shipping (LogShipper)**

LogShipper ships logs to the storage service OSS, with compression, custom partitions and
row/column storage formats. No limit on data volume; row, column and TextFile formats; flexible
configuration such as user-defined partitions.

## Features

**Basic features**

| Feature | Description |
|---|---|
| Project | A project is the resource management unit of SLS, used for resource isolation and control. A project manages all log stores of an application, the machine configurations for log collection, and serves as the entry point for accessing SLS resources. |
| Logstore | A logstore is the unit for collecting, storing and querying log data. Each logstore belongs to one project, and each project can contain multiple logstores. |
| Metricstore | A Metricstore is the unit for collecting, storing and querying time-series data. SLS time-series data follows the Prometheus specification, and all data in a Metricstore is stored as time-series data. A time series consists of a time-series identifier and data points; data with the same identifier forms a timeline. |
| Machine group management | SLS manages all servers that collect logs through the Logtail client by means of machine groups. A machine group is a virtual group of servers; if multiple servers must use the same Logtail configuration, add them to one machine group and apply the configuration to that group. |
| Log collection | Through Logtail, WebTracking and SDKs, supports Log, Metric and Trace data types from many sources such as Alibaba Cloud services, servers and applications, IoT devices, mobile clients, open-source software and standard protocols. |
| Log query and analysis — analytic algorithms | General aggregation functions; security monitoring functions; MAP mapping functions; mathematical statistics functions (standard deviation, covariance, correlation, regression slope, and more); estimation functions, mathematics, string processing, date and time, URL functions, regular expressions, JSON processing, IP address, window functions, and more. |
| Series decomposition | Uses the STL algorithm to decompose time-series data. |
| Data query | Supports querying JSON, text and numeric data; automatically builds indexes for text in JSON format; supports full-text query; supports combined conditions (AND, OR, NOT); supports contextual query in raw logs (N lines before and after). |
| Log clustering | Supports clustering of any format and of query result data; adjustable clustering precision; supports reverse lookup of raw data from clustering results. |
| Time-series clustering | Clusters multiple time series using density-based clustering and hierarchical clustering. |
| Time-series smoothing | Smooths time-series data using Holt-Winters, FIR and IIR algorithms. |
| Time-series forecasting | Models time series with AR, moving-average AR, and differenced moving-average AR models for simple forecasting and outlier detection; accurately forecasts single series with periodicity and trend. |
| Maximum value detection | Finds local maxima of a series within a specified window. |
| Change point detection | Finds intervals with different statistical properties in a series (interval endpoints are change points); finds points where a statistic rises or drops sharply. |
| Trace service | Provides distributed tracing based on the native OpenTelemetry protocol, covering ingestion, storage, analysis, visualization and AIOps of Trace data. OpenTelemetry is the recognised distributed tracing standard, compatible with OpenTracing and OpenCensus clients, and consists of APIs, SDKs and tools to observe, generate, collect and export telemetry data (traces, logs, metrics). |
| Scheduled SQL | Analysing data on a schedule, storing aggregated data, and projecting and filtering data. |
| Dashboard | Displays frequently used queries as charts (tables, line charts, bar charts, and more); saves multiple charts in one dashboard; supports drill-down to deeper dimensions. |
| Alerting | Alerts on log query/analysis results, checked periodically and notified when preset conditions are met. |

**Data security and reliability**

| Feature | Description |
|---|---|
| Three replicas | Each data chunk is replicated into three identical copies kept on different nodes of the cluster according to a policy, so that data can still be recovered from other nodes if one node fails. |
| Erasure coding (EC) | Raw data is split into multiple data blocks and a number of parity blocks are computed; data and parity blocks form an EC group distributed across storage nodes. If some blocks are lost, the lost data can be recovered from the remaining blocks. EC uses data blocks (n) and parity blocks (m): data is split into n slices, and m parity blocks are computed from the n data blocks; the n+m blocks of an EC group reside on different servers, and any loss of up to m blocks can be recovered by the EC algorithm. `n+m` is configurable depending on the number of nodes in the deployed cluster; **the recommended Apsara Stack configuration is 8+3 (cluster with at least 14 nodes)**. |
| Online replica policy change | The EC policy can be changed online through the operations platform. |
| Data encryption | Supports encrypted storage through Key Management Service (KMS) for data-at-rest protection; supports encryption with SLS-managed keys and with customer-provided keys (BYOK). |
| Multi-region | The central region deploys the management module SCMG for Project uniqueness validation and for synchronising account information to the SLS clusters of each region; each region deploys an independent SLS cluster for log storage, query and analysis. |

**Data management**

| Feature | Description |
|---|---|
| Data processing | More than 200 built-in functions, more than 400 regular expressions and flexible custom functions for filtering, splitting, transformation, enrichment and replication. |
| Data consumption | Provides real-time consumption interfaces for logs collected to the server side: SDK consumption (Java, Python, Go and more); consumer group consumption — a lightweight computing framework that lets multiple consumers consume a Logstore in parallel, with automatic shard assignment, order preservation and resumable consumption, with consumer group SDKs in Java, Python, Go and more; real-time computing systems — Spark Streaming, Storm, open-source Flink; open-source products — Flume. |
| Data shipping | Ships logs to OSS in real time for long-term storage and backup. |

## Deployment requirements

An SLS cluster requires **at least 4 nodes**, and a 6-node configuration is recommended.

> **Important**
> With a 4-node deployment the failure domain is only one machine; if one more machine fails, data
> loss is possible.
