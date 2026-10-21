---
title: "Alibaba Cloud Apsara Stack v3.18.6-2607 Time Series and Spatial-Temporal Database Product Introduction 20260827"
product_version: "V3.18.6_2607"
doc_version: "20260827"
pdf_pages: 11
source_pdf: "a25a423acc855922_Alibaba Cloud Apsara Stack v3.18.6-2607 Time  Series and Spatial-Temporal  Database Product Introduc"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/3816%202607/pdf%203/%E4%BA%91%E5%8E%9F%E7%94%9F%E5%A4%9A%E6%A8%A1%E6%95%B0%E6%8D%AE%E5%BA%93%20Lindorm/Alibaba%20Cloud%20Apsara%20Stack%20v3.18.6-2607%20Time%20%20Series%20and%20Spatial-Temporal%20%20Database%20Product%20Introduction%2020260827.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes)
---

# Alibaba Cloud Apsara Stack v3.18.6-2607 Time Series and Spatial-Temporal Database Product Introduction 20260827

## Table of Contents

- 1 Lindorm
  - 1.1 Product details
  - 1.2 Product value
  - 1.3 Scenarios
  - 1.4 Features

## 1 Lindorm

Lindorm is a cloud-native, multi-model, and hyper-converged database built for scenarios such as the Internet of Things (IoT), the Internet, and the Internet of Vehicles (IoV). It provides unified access to and converged processing of various data types, such as wide table, time series, text, object, stream, and spatial data. Lindorm is compatible with multiple openstandard interfaces and integrates with third-party ecosystem tools.

### 1.1 Product details

Lindorm is a cloud-native database service that supports multiple data models. You can use the Alibaba Cloud console to create Lindorm instances, upgrade engine versions, scale nodes, or release instances as needed.

**Instance**

An instance is the smallest unit of service that Lindorm provides. Different instance types offer different computing and storage capabilities. A single Lindorm instance can store and compute data for multiple models, such as wide table, time series, text, object, stream, and spatial data.

**Storage engines**

Lindorm supports storage engines such as the wide table engine, time series engine, search engine, and file engine. It is compatible with multiple open standard interfaces, such as HBase, Cassandra, S3, OpenTSDB, Solr, Hadoop Distributed File System (HDFS), and Kafka. Lindorm also provides capabilities such as SQL queries, time series processing, and text search and analysis.

**Network**

Virtual private cloud A virtual private cloud (VPC) is a private network on the cloud. Different VPCs are logically isolated at Layer 2 to provide high security and performance. If Lindorm-cli is deployed on an ECS instance, you can connect to your Lindorm instance over a VPC for higher security and lower network latency. The Internet If an on-premises device needs to connect to a Lindorm instance, you can request a public endpoint to connect over the Internet. Connecting over the Internet may pose security risks. For higher security, connect over a VPC.

**Auto Scaling**

Lindorm supports Auto Scaling. This service automatically adjusts your computing and storage resources based on defined policies to help reduce infrastructure and operations and maintenance (O&M) costs. Lindorm storage resources support online scaling within seconds. Computing resources for the wide table, time series, and search engines support online scaling within minutes. Lindorm supports node upgrades and downgrades for each engine. This allows for rapid elastic scaling to efficiently handle peak workloads.

**Unified multi-model processing**

Lindorm allows data to be shared between different models. For example, the search engine can act as an index for the wide table and time series engines, which speeds up multi-dimensional searches and analysis. Lindorm provides integrated processing capabilities, including data ingestion, storage, retrieval, computation, and analysis. Lindorm supports unified SQL access for cross-engine queries on multiple data models.

**Cold storage**

Lindorm supports a cold storage feature to reduce storage costs by storing cold data from your database. You can set a boundary between hot and cold data to automatically archive data from your tables into the appropriate storage tier.

**Secondary indexes**

The Lindorm wide table engine supports a high-performance native secondary index feature. This feature lets you create multiple index tables for a single primary table. Each index table can have a different storage policy, such as a specific compression algorithm or a hot and cold data separation policy. Lindorm ensures data consistency between the primary and index tables. Data in the index tables is updated automatically, which improves write efficiency.

**Data ecosystem service**

Lindorm uses Lindorm Tunnel Service (LTS) to import and migrate data. LTS is a data ecosystem service customized for Lindorm scenarios. It supports use cases such as data migration, real-time subscriptions, data lake offloading, data loading into data warehouses, active-active deployments, and backup and recovery.

**Cluster management system**

The Lindorm wide table engine provides a cluster management system for intelligent operations and maintenance (O&M) of instances. This includes the following capabilities: View information about an instance, such as capacity in each zone, server lists, table properties, and table sizes. Manage database tables and namespaces. Manage database accounts and permissions. Run simple SQL statements to query data in the database. View real-time monitoring metrics at multiple levels, including instances, groups, nodes, namespaces, and tables. Perform health checks on instances and view inspection reports to quickly analyze and locate issues. The Lindorm search engine provides a cluster management system to manage index tables. This includes operations such as creating, deleting, and updating configurations.

### 1.2 Product value

Lindorm is built on a cloud-native architecture. It provides elastic scaling, low cost, high performance, ease of use, high availability, high reliability, and an open ecosystem.

**Elastic scaling**

The fully distributed architecture decouples storage and compute. This allows for the independent elastic scaling of computing and storage resources. You can scale storage resources online within seconds. Computing resources, such as LindormTable, LindormTSDB, and the search engine, can be scaled online within minutes.

**Low cost**

Offers multiple storage specifications, such as compute-optimized, standard, and storageoptimized, to provide cost-effective solutions for various scenarios. Multiple engines share a unified storage pool, which reduces storage fragmentation and lowers usage costs. The built-in, deeply optimized compression algorithms provide a data compression ratio of over 10:1, which is an improvement of more than 50% compared to Snappy. Built-in adaptive encoding is tailored for different data types, allowing for fast data queries without decoding. Supports intelligent hot and cold data separation, allowing you to use a mix of storage specifications to significantly reduce overall data storage costs.

**High performance**

LindormTable: Supports a throughput of tens of millions of concurrent operations and storage of hundreds of petabytes. Its performance is 3 to 7 times higher than open-source HBase, and its P99 latency is one-tenth that of open-source HBase. LindormTSDB offers write and query performance that is 1.3 times that of InfluxDB and 5 to 10 times that of OpenTSDB. The search engine is deeply optimized based on the Lucene engine, and its overall performance is 30% better than open-source Solr or ES.

**Ease of use**

Compatible with multiple open standard interfaces, such as HBase, Cassandra, Phoenix, OpenTSDB, and Solr, allowing for seamless service migration. Provides a fully managed cloud service that requires no Operations and Maintenance (O&M). You can use the graphical user interface (GUI) for simple system administration and data access.

**High availability**

The distributed, multi-replica architecture enables clusters to automatically recover from disasters. Supports cross-zone disaster recovery with strong consistency and meets financial-grade availability standards. Supports Global Distributed Cache deployments.

**High reliability**

Multi-replica storage at the underlying layer ensures high data reliability. Provides enterprise-grade backup capabilities.

**Open ecosystem**

Supports smooth online data migration from systems such as MySQL, HBase, and Cassandra. Seamlessly integrates with compute engines such as Spark, Flink, Data Lake Analytics (DLA), and MaxCompute. Seamlessly subscribes to data from log channels, such as Kafka and Simple Log Service (SLS), and provides fast data processing. You can use Lindorm Stream to subscribe to incremental data changes in Lindorm in real time for custom consumption.

### 1.3 Scenarios

Lindorm is a cloud-native multi-model database developed by Alibaba Cloud. It is designed for low-cost storage and analysis of massive multi-model data and serves as a data foundation for the Internet of Everything. Lindorm provides single-millisecond response times and supports horizontal scaling to petabytes of storage and tens of millions of queries per second (QPS). It is a key component of Alibaba's core services and is used in scenarios such as big data, finance, the Internet of Vehicles, and Internet services.

**Best practices within Alibaba Group**

Lindorm is widely used in core business operations within Alibaba Group. It stores and analyzes real-time data for applications such as Taobao messages, Alipay bills, and Cainiao logistics information. Lindorm offers Alibaba Group low cost, high concurrency, and elastic scaling.

**Big data scenarios**

Lindorm supports low-cost storage, fast batch imports, and real-time access to massive amounts of data. It provides efficient channels for both incremental and full data. Lindorm easily integrates with big data platforms, such as Spark and MaxCompute, to perform largescale offline analysis. These capabilities provide businesses with advantages such as low cost, fast imports, and elastic scaling.

**Finance and retail**

Lindorm stores massive order records from financial transactions and important data for financial risk control, such as user events, profiles, rule models, and device fingerprints. It provides a low-cost, high-concurrency, flexible, and reliable solution that meets the real-time data storage requirements of financial transaction and risk control scenarios.

**Internet of Vehicles**

Lindorm stores important data for the Internet of Vehicles, such as driving trajectories, vehicle status, and precise location information. It provides a low-cost, elastic, flexible, and reliable solution for data storage and processing in scenarios such as ride-hailing, logistics transportation, and new energy vehicle monitoring.

**Internet and social media**

Lindorm stores important data for social media applications, such as chats, comments, posts, and likes. By offering ease of development, high availability, and low latency, Lindorm significantly reduces user access wait times and provides a stable and reliable social feed system.

### 1.4 Features

| Feature category | Feature | Description |
|---|---|---|
|   | Create an instance | A base platform can have only one instance. The instance is created with the platform. |
|   | Scale-out | Lets you scale out instances using scale-out packages. |
|   | Upgrade the minor engine version | Upgrade packages are provided by the product and released as hotfixes. |

| Instance managem ent |   |   |
|---|---|---|
|   | Upgrade or downgrad e an instance | Lets you change instance types, including upgrades and downgrades, and modify storage capacity. |
|   | Release an instance | Lets you release existing instances. |
|   | View basic instance informatio n | View detailed information for an instance in the console. This includes basic information, running status, and detailed configuration. |
|   | Instance list | Displays basic instance information in a list. The list includes the instance name, status, and network operation entries. |
| Account managem ent | Create an account | Lets you create privileged and standard accounts. |
|   | Modify account permissio ns | Lets you modify the permissions of existing accounts. |
|   | Service authorizat ion account | Authorize a service account to let helpdesk staff provide technical support. |
|   | Reset a password | Lets you reset account passwords. |
|   | Reset a privileged account | Lets you reset privileged accounts. |
|   | Delete an account | Lets you delete specified accounts. |
| Data backup | Full backup | Perform full backups of your data. This requires manual deployment and can be managed from the console. |
|   | Increment al backup | Perform incremental backups of your data. This requires manual deployment and can be managed from the console. |

| Database managem ent | Create a namespac e | Lets you create namespaces. |
|---|---|---|
|   | Delete a namespac e | Lets you delete existing namespaces. |
| Monitorin g and alerting | View metrics | View monitoring metrics in the console. Metrics include the number of timelines, data points written per second, and disk usage (Master disk usage). You can also set alert rules for these metrics. |
| Data migration | HBase data migration | Migrate data from a self-managed HBase cluster to Alibaba Cloud HBase. Both full and incremental migration are supported. |
| Import and export | Write data using Blink | Lets you write data using Blink. |
|   | Export data to MaxComp ute | Lets you export data to MaxCompute. |
| Disaster recovery | Cross- data center disaster recovery | Provides high availability (HA) disaster recovery across data centers. |
| Data security | Configure a whitelist | Configure a whitelist for an instance to allow access from external devices. |
| Kernel features | Dynamic columns | The LindormTable engine supports dynamic columns. This means you can write data to and query columns that were not explicitly defined when the table was created. |
|   | Secondary index | Provides native support for secondary indexes. |
| Hardware support | Support for domestic hardware | Supports Hygon 2, 3, and 4 chips. Supports Kunpeng chips. Supports Phytium chips. Supports Yitian chips. Supports mixed deployment with the x86 instruction set. Supports mixed deployment with the Arm instruction set. |
