---
title: "Alibaba Cloud Apsara Stack v3.18.6-2607 Data Transmission Service Product Introduction 20260831"
product_version: "V3.18.6_2607"
doc_version: "20260831"
pdf_pages: 20
source_pdf: "a8e3391c51657c7f_Alibaba Cloud Apsara Stack v3.18.6-2607 Data Transmission Service Product Introduction 20260831.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/3816%202607/pdf%203/%E6%95%B0%E6%8D%AE%E4%BC%A0%E8%BE%93%E6%9C%8D%E5%8A%A1%20DTS/Alibaba%20Cloud%20Apsara%20Stack%20v3.18.6-2607%20Data%20Transmission%20Service%20Product%20Introduction%2020260831.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes)
---

# Alibaba Cloud Apsara Stack v3.18.6-2607 Data Transmission Service Product Introduction 20260831

## Table of Contents

- 1 What is DTS?
  - 1.1 Overview
  - 1.2 Benefits
  - 1.3 Scenarios
  - 1.4 Features

## 1 What is DTS?

Data Transmission Service (DTS) is a data service that is provided by Alibaba Cloud. DTS supports data transmission between various types of data sources, such as relational databases and big data systems. Compared with traditional data migration or synchronization tools, DTS provides diverse features and high performance, security, reliability, and ease of use. DTS helps you simplify data transmission and focus on your application development.

### 1.1 Overview

This topic provides an overview of the features of Data Transmission Service (DTS), such as data synchronization, data migration, and change tracking.

**Data synchronization**

You can use DTS to synchronize data between data sources in real time. The following table describes the capabilities supported by the data synchronization feature.

| Capability | Description |
|---|---|
| Add or remove the objects to be synchronized | You can add or remove the objects to be synchronized at any time when a data synchronization task is running. |
| View and analyze the synchronization performance | DTS provides trend charts that allow you to view and analyze the performance of your data synchronization tasks. The synchronization performance is measured based on bandwidth, records per second (RPS), and synchronization latency. |
| Monitor data synchronization tasks | DTS allows you to monitor the status of data synchronization tasks. If the threshold for synchronization latency is reached, the system sends an alert notification to you. You can set the alert threshold based on the sensitivity of your business to synchronization latency. |

You can use DTS to migrate data between homogeneous or heterogeneous data sources. DTS provides the following extract, transform, and load (ETL) capabilities: object name mapping for columns, tables, and databases, and data filtering. These capabilities allow you to migrate data between various types of data sources with ease. DTS uses online migration. You need to only configure the source instance, the destination instance, and the objects to be migrated. DTS automatically completes the entire data migration process. You can select all of the supported migration types to minimize the impact of online data migration on your services. However, you must ensure that DTS servers can connect to both the source and destination instances. The following table describes the ETL capabilities supported by the data migration feature.

| Capability | Description |
|---|---|
| Enable object name mapping for columns, tables, and databases | You can migrate data between two columns, tables, or databases that have different names. |
| Filter the data to be migrated | You can set SQL conditions to filter the data to be migrated in a specific table. For example, you can specify a time range to migrate only the latest data. |

**Change tracking**

DTS allows you to track incremental data in databases in real time. You can consume the tracked data based on your business requirements. The following table describes the capabilities supported by the change tracking feature.

| Capability | Description |
|---|---|
| Add or remove the objects for change tracking | You can add or remove the objects for change tracking at any time when a change tracking task is running. |
| View the tracked data | You can view the incremental data that is tracked by a change tracking task in the DTS console. |
| Modify the consumption checkpoint | You can modify the consumption checkpoint at any time. |
| Monitor change tracking tasks | DTS allows you to monitor the status of change tracking tasks. If the threshold for consumption latency is reached, the system sends an alert notification to you. You can set the alert threshold based on the sensitivity of your business to consumption latency. |

**ETL**

DTS provides the ETL feature. When you configure a data migration or synchronization task, you can rename databases, tables, and columns in the destination instance and set conditions to filter specific data. The following table describes the capabilities supported by the ETL feature.

| Capability | Description |
|---|---|
| High computing effectiveness | Integrated with the powerful capabilities of DTS in collecting streaming data from databases, the ETL feature ensures data accuracy and provides high computing effectiveness in the industry. |
| Flexible task monitoring and management | You can monitor and manage ETL tasks in the DTS console. For example, you can start a task, stop a task, and view task details. |

**Data consistency**

DTS uses the data reading module, data loading module, data verification feature, and resumable transmission feature to ensure data consistency between the source and destination databases.

### 1.2 Benefits

Compared with third-party data migration or synchronization tools, Data Transmission Service (DTS) supports diverse data transmission scenarios and ensures high performance, security, and reliability. DTS allows you to create and manage tasks with high efficiency.

**Multiple transmission modes**

DTS supports multiple data transmission modes, including data migration, data synchronization, and change tracking.

> **Note:** In the change tracking and data synchronization modes, data is transmitted in real time.

In the data migration mode, data is migrated between databases without interrupting application operations. The application downtime during data migration is reduced to a few minutes.

**High performance**

DTS uses servers with high specifications to ensure the performance of each data synchronization or migration instance. Compared with traditional data synchronization tools, DTS provides better synchronization performance. You can use DTS to concurrently synchronize transactions and the incremental data of a single table. DTS supports concurrent data capture and data write. The data capture and data write modules are decoupled to improve the overall throughput. To implement concurrent migration between tables and within tables, DTS applies a variety of intelligent sharding policies on the tables to be migrated. This ensures parallel data synchronization and improves the processing efficiency of a large number of databases and a large amount of data in a single table. DTS uses efficient network protocols and data compression technology to reduce the amount of data on long-distance connections and minimize data transmission latency. Multiple TCP connections are deployed to improve the synchronization performance and stability in abnormal network environments. DTS provides horizontal scaling capabilities. You can improve capacity by increasing the number of tasks. At the underlying layer of DTS, multiple measures are taken to improve performance.

**High security and reliability**

DTS provides a 24 × 7 mechanism for validating data accuracy in some instances to discover and rectify inaccurate data. This helps ensure reliable data transmission. DTS is deployed based on clusters. If a node in a cluster is down or faulty, the control center moves all tasks from this node to another healthy node in the cluster within seconds. Secure transmission protocols and tokens are used for authentication across DTS modules to ensure reliable data transmission. DTS supports the deployment of multiple data centers in the same city or across cities. If one of the data centers fails, you can quickly switch your workloads to another data center.

**Ease of use**

The DTS console is a GUI that provides a wizard-like process to assist you in creating tasks for various scenarios. To facilitate task management, the DTS console displays task information such as status, progress, and performance. DTS supports resumable transmission and monitors task status on a regular basis. If DTS detects a network failure or system error, DTS automatically fixes the failure or error and restarts the task. If the failure or error persists, you can manually troubleshoot and restart the task in the DTS console.

### 1.3 Scenarios

Data Transmission Service (DTS) is applicable to scenarios such as interruption-free data migration, accelerated access to global services, geo-disaster recovery, and active georedundancy.

**Interruption-free data migration**

Traditional migration tools have many disadvantages. For example, these tools cannot ensure data consistency, require that services be suspended for a long time, and even have a great impact on the business during data migration. DTS provides an interruption-free data migration solution that minimizes the service downtime to minutes. The interruption-free data migration process involves schema migration, full data migration, and incremental data migration. In the incremental data migration phase, data is synchronized between the source and destination instances in real time. You can validate the services in the destination instance, and switch your services to the destination instance after the validation is complete. The entire system is then eventually migrated.

> **Note:** Throughout the migration process, you may experience service interruptions only when the services are switched from the source instance to the destination instance.

**Accelerated access to global services**

In traditional architectures, if services with widely distributed users, such as global services, are deployed in only one region, users in other regions have to access the services remotely, resulting in high access latency and poor user experience. DTS synchronizes data from the center to various cells in real time. Read requests of users in different regions can be routed to the nearby cells to avoid remote access. This way, the access latency is reduced, and the access to global services is accelerated.

**Quick building of a custom BI system**

Self-managed business intelligence (BI) systems are difficult to manipulate and cannot meet increasing requirements for real-time capabilities. Alibaba Cloud provides comprehensive BI systems. DTS allows you to synchronize data in real time from self-managed databases to Alibaba Cloud BI storage systems, such as MaxCompute, AnalyticDB, and Realtime Compute for Apache Flink. DTS helps you build a custom BI system that meets your business requirements on Alibaba Cloud.

**Real-time data analysis**

To implement real-time data analysis without affecting online services, you need to synchronize service data to an analysis system in real time. For this reason, acquiring service data in real time becomes essential. The change tracking feature of DTS helps you acquire real-time incremental data without affecting online services and synchronize the data to the analysis system by using the SDK for real-time data analysis.

**Lightweight cache update policies**

DTS provides the change tracking feature that can be used to track the incremental data in databases in an asynchronous manner and update the cached data. This way, data integrity is ensured, and lightweight cache update policies are implemented. Cache update policies offer the following benefits: Quick update with low latency Cache invalidation is an asynchronous process, and updated data is directly returned after the database update is complete. For this reason, you do not need to consider the cache invalidation process. The entire update process is quick with low latency. Simple and reliable applications The complex doublewrite logic is not required for your applications. You need to only start asynchronous threads to track incremental data and update cached data. Application updates without performance degradation DTS tracks incremental data by parsing incremental logs in databases. This does not affect the performance of your business and databases.

**Business decoupling with asynchronous communication**

**between different types of business logic**

You can use the change tracking feature of DTS to decouple different types of business logic. This is achieved by means of real-time notifications and asynchronous communication between different types of business logic. This makes the core business logic simple and reliable.

**Horizontal scaling of the read capability**

A single database instance may not have sufficient resources to deal with a large number of read requests. To scale out the read capability and relieve the pressure on the database instance, you can use the real-time data synchronization feature of DTS to create read-only instances and distribute read requests across these read-only instances.

### 1.4 Features

This topic describes the features of Alibaba Cloud Data Transmission Service (DTS) to help you quickly understand the product capabilities.

| Feature category |   | Description |
|---|---|---|
|   | Db2 for i migration to MySQL | Supports schema migration, full data migration, and incremental data migration. |
|   | Migrate data from Db2 for i to PolarDB for MySQL | Supports schema migration, full data migration, and incremental data migration. |
|   | Db2 for LUW migration to AnalyticDB PostgreSQL | Supports schema migration, full data migration, and incremental data migration. |
|   | Migrate data from Db2 for LUW to PolarDB for PostgreSQL | Supports schema migration, full data migration, and incremental data migration. |
|   | Migrate data from Db2 for LUW to PolarDB for MySQL | Supports schema migration, full data migration, and incremental data migration. |

|   | Migrate data from PolarDB for MySQL to MySQL | Supports schema migration, full data migration, and incremental data migration. Supports self-managed MySQL versions 5.1, 5.5, 5.6, and 5.7. |
|---|---|---|
|   | Migrate data from PolarDB for MySQL to Kafka | Supports full data migration and incremental data migration. Supports self-managed Kafka versions 0.1 to 2.7. |
|   | MaxCompute migration to MySQL | Supports schema migration and full data migration. |
|   | Data migration between MongoDB instances | Only self-managed MongoDB database instances are supported as source and destination. Supported MongoDB database versions are 3.0, 3.2, 3.4, 3.6, 4.0, or 4.2. |
|   | MySQL migration to PolarDB-X 1.0 | MySQL versions 5.1 to 5.7. RDS MySQL versions 5.1 to 5.7 attached to PolarDB-X 1.0. Supports full data migration and incremental data migration, but does not support schema migration. |
|   | Migrate data from MySQL to PolarDB-X 2.0 | Supports schema migration, full data migration, and incremental data migration. |
|   | MySQL migration to AnalyticDB PostgreSQL | Self-managed MySQL versions 5.1 to 5.7, RDS MySQL versions 5.5, 5.6, 5.7. Supports schema migration, full data migration, and incremental data migration. |
|   | MySQL migration to Kafka | Self-managed MySQL versions 5.1 to 5.7, RDS MySQL versions 5.5, 5.6, 5.7. Supports schema migration, full data migration, and incremental data migration. Kafka requires public network or private network access, and must be able to communicate with DTS. Select the public network access method and enter the public or private IP address. Self-managed Kafka versions 0.10 to 2.0 over public network. |

|   | Data migration between MySQL instances | Self-managed MySQL versions 5.1 to 5.7, RDS MySQL versions 5.5, 5.6, 5.7. Supports schema migration, full data migration, and incremental data migration. |
|---|---|---|
|   | MySQL migration to Oracle | Oracle versions 9i, 10g, 11g. MySQL versions 5.1 to 5.7. Supports schema migration, full data migration, and incremental data migration. |
|   | MySQL migration to PostgreSQL | Supports MySQL versions 5.5, 5.6, 5.7, 8.0. Supports PostgreSQL versions 10.x, 11.x, 12.x, 13.x. PostgreSQL must be accessed as a self-managed database over public network. |
|   | Oracle migration to AnalyticDB MySQL 2.0 | Oracle versions 9i, 10g, 11g. Supports full data migration and incremental data migration. |
|   | Oracle migration to AnalyticDB MySQL 3.0 | Oracle versions 9i, 10g, 11g. Supports schema migration, full data migration, and incremental data migration. |
|   | Oracle migration to AnalyticDB PostgreSQL | Oracle versions 9i, 10g, 11g. Supports schema migration, full data migration, and incremental data migration. |
|   | Oracle migration to PolarDB-X 1.0 | Oracle versions 9i, 10g, 11g. RDS MySQL versions 5.1 to 5.73 attached to PolarDB-X 1.0. Supports full data migration and incremental data migration, but does not support schema migration. |
|   | Oracle migration to MySQL | Oracle versions 9i, 10g, 11g. MySQL versions 5.1 to 5.7. Supports schema migration, full data migration, and incremental data migration. |
|   | Data migration between Oracle instances | Oracle versions 9i, 10g, 11g. Supports schema migration, full data migration, and incremental data migration. |

| Data migration |   |   |
|---|---|---|
|   | Oracle migration to PolarDB for PostgreSQL (Compatible with Oracle) | Oracle versions 9i, 10g, 11g. Supports schema migration, full data migration, and incremental data migration. PolarDB for PostgreSQL (Compatible with Oracle) requires public network or private network access, and must be able to communicate with DTS. Select the public network access method and enter the public or private IP address. |
|   | Oracle migration to PostgreSQL | Oracle versions 9i, 10g, 11g. Supports schema migration, full data migration, and incremental data migration. |
|   | Oracle migration to PPAS | Oracle versions 9i, 10g, 11g. Supports schema migration, full data migration, and incremental data migration. |
|   | Oracle migration to Kafka | Self-managed Kafka versions 0.10 to 2.0 over public network. Supports schema migration, full data migration, and incremental data migration. Oracle versions 9i, 10g, 11g, 12g, 18c, 19c. RAC access only supports public network method, and leased line access only supports configuring one of the VIPs. |
|   | Oracle migration to PostgreSQL | Oracle versions 9i, 10g, 11g. Supports schema migration, full data migration, and incremental data migration. PolarDB for PostgreSQL (Compatible with Oracle) requires public network or private network access, and must be able to communicate with DTS. Select the public network access method and enter the public or private IP address. PostgreSQL versions 10.x, 11.x, 12.x require public network or private network access, and must be able to communicate with DTS. Select the public network access method and enter the public or private IP address. |
|   | Oracle to CCB streaming collection SDK | Oracle versions 9i, 10g, 11g, 12c, 18c, 19c. Supports full data migration and incremental data migration. |
|   | Migrate data from PolarDB for MySQL to MySQL | Supports schema migration, full data migration, and incremental data migration. |

|   | PolarDB for PostgreSQL (Compatible with Oracle) migration to Kafka | Self-managed Kafka versions 0.10 to 2.0 over public network. Only supports incremental data migration. PolarDB for PostgreSQL (Compatible with Oracle) needs to be accessed as a self-managed database over public network, by entering the IP and Port of PolarDB for PostgreSQL (Compatible with Oracle) for connection. |
|---|---|---|
|   | PolarDB for PostgreSQL (Compatible with Oracle) migration to Oracle | PolarDB for PostgreSQL (Compatible with Oracle) needs to be accessed as a self-managed database over public network, by entering the IP and Port of PolarDB for PostgreSQL (Compatible with Oracle) for connection. Self-managed Oracle versions 9i to 19c over public network. Supports full and incremental data migration, but does not support schema migration. |
|   | Data migration between PolarDB for PostgreSQL (Compatible with Oracle) instances | PolarDB for PostgreSQL (Compatible with Oracle) needs to be accessed as a self-managed database over public network, by entering the IP and Port of PolarDB for PostgreSQL (Compatible with Oracle) for connection. Supports schema migration, full data migration, and incremental data migration. |
|   | PolarDB-X 2.0 migration to AnalyticDB PostgreSQL | Supports schema migration, full data migration, and incremental data migration. |
|   | PolarDB-X 2.0 migration to Kafka | Supports schema migration, full data migration, and incremental data migration. |
|   | PolarDB-X 2.0 migration to MySQL | Supports schema migration, full data migration, and incremental data migration. |
|   | Data migration between PolarDB-X 2.0 instances | Supports schema migration, full data migration, and incremental data migration. |
|   | PostgreSQL migration to PolarDB for PostgreSQL | Supports schema migration, full data migration, and incremental data migration. |

|   | PostgreSQL migration to PolarDB for PostgreSQL (Compatible with Oracle) | Supports schema migration, full data migration, and incremental data migration. PolarDB for PostgreSQL (Compatible with Oracle) must be accessed as a self-managed database over public network. PostgreSQL must be accessed as a self-managed database over public network. PostgreSQL versions 10.x, 11.x, 12.x. |
|---|---|---|
|   | Data migration between PostgreSQL instances | PostgreSQL versions 9.x to 10.x. Supports schema migration, full data migration, and incremental data migration. For self-managed databases, incremental migration requires the installation of the ali decoding plugin. _ |
|   | PPAS migration to PolarDB for PostgreSQL (Compatible with Oracle) | Supports schema migration, full data migration, and incremental data migration. PPAS requires public network or private network access, and must be able to communicate with DTS. Select the public network access method and enter the public or private IP address. PolarDB for PostgreSQL (Compatible with Oracle) requires public network or private network access, and must be able to communicate with DTS. Select the public network access method and enter the public or private IP address. |
|   | Migrate data from ApsaraDB for MongoDB to Kafka | Supports only full and incremental data migration. Schema migration is not supported. Supports self-managed Kafka versions 0.1 to 2.7. |
|   | Data migration between Redis instances | Only self-managed Redis over public network. Cluster architecture is not supported. Supported self-managed Redis versions: 2.8, 3.0, 3.2, 4.0. Supports full data migration and incremental data migration. |
|   | Data migration between SQL Server instances | Supported SQL Server versions: 2005 to 2017. Supports schema migration, full data migration, and incremental data migration. |
|   | Data migration between PolarDB for MySQL instances | Supports schema migration, full data migration, and incremental data migration. |
|   | Migrate data from PolarDB for MySQL to PolarDB-X 2.0 | Supports schema migration, full data migration, and incremental data migration. |

|   | Migrate data from PolarDB-X 2.0 to PolarDB for MySQL | Supports schema migration, full data migration, and incremental data migration. |
|---|---|---|
|   | Migrate data from RDS for PostgreSQL to PolarDB for PostgreSQL | Supports schema migration, full data migration, and incremental data migration. |
|   | Data migration between PolarDB for PostgreSQL instances | Supports schema migration, full data migration, and incremental data migration. |
|   | Self-managed MySQL (Public Network) migration to PolarDB- X 2.0 | Supports schema migration, full data migration, and incremental data migration. |
|   | RDS MySQL (Instance) migration to PolarDB-X 2.0 | Supports schema migration, full data migration, and incremental data migration. |
|   | RDS PostgreSQL migration to PolarDB for PostgreSQL | Supports schema migration, full data migration, and incremental data migration. |
|   | PolarDB-X 1.0 migration to Kafka | Supports schema migration, full data migration, and incremental data migration. Kafka version 2.7. |
|   | Migrate data from OceanBase Database for MySQL to PolarDB for MySQL | Supports schema migration, full data migration, and incremental data migration. |
| Change tracking | Incremental data subscription with PolarDB-X 1.0 as source | RDS MySQL versions 5.1 to 5.7 attached to PolarDB-X 1.0. |
|   | Incremental change tracking from a PolarDB-X 2.0 source | Supports multi-stream change data capture (CDC). |

|   | Incremental data subscription with MySQL as source | MySQL versions 5.1 to 5.7, RDS MySQL versions 5.5, 5.6, 5.7. |
|---|---|---|
|   | Incremental data subscription with Oracle as source | Oracle versions 9i, 10g, 11g. Oracle RAC is not supported. |
|   | Db2 for i synchronization to MySQL | Supports schema synchronization, full data synchronization, and incremental data synchronization. |
|   | Synchronize data from Db2 for i to PolarDB for MySQL | Supports schema synchronization, full data synchronization, and incremental data synchronization. |
|   | Db2 for LUW synchronization to AnalyticDB PostgreSQL | Supports schema synchronization, full data synchronization, and incremental data synchronization. Db2 for LUW versions 10.1, 10.5, 11.5. |
|   | Synchronize data from Db2 for LUW to PolarDB for PostgreSQL | Supports schema synchronization, full data synchronization, and incremental data synchronization. |
|   | Synchronize data from Db2 for LUW to PolarDB for MySQL | Supports schema synchronization, full data synchronization, and incremental data synchronization. |
|   | Synchronize data from PolarDB for MySQL to MySQL | Supports schema synchronization, full data synchronization, and incremental data synchronization. Supports self-managed MySQL versions 5.1, 5.5, 5.6, and 5.7. |
|   | Synchronize data from PolarDB for MySQL to Kafka | Supports full data synchronization and incremental data synchronization. Supports self-managed Kafka versions 0.1 to 2.7. |
|   | PolarDB-X 1.0 synchronization to DataHub | RDS MySQL versions 5.1 to 5.7 attached to PolarDB-X 1.0. Supports schema synchronization, full data synchronization, and incremental data synchronization. |
|   | Data synchronization between PolarDB-X 1.0 instances | RDS MySQL versions 5.1 to 5.7 attached to PolarDB-X 1.0. Supports schema synchronization, full data synchronization, and incremental data synchronization. |

|   | MySQL synchronization to AnalyticDB PostgreSQL | MySQL versions 5.1 to 5.7, RDS MySQL versions 5.5, 5.6, 5.7. Supports schema synchronization, full data synchronization, and incremental data synchronization. |
|---|---|---|
|   | MySQL synchronization to AnalyticDB MySQL 2.0 | MySQL versions 5.1 to 5.7, RDS MySQL versions 5.5, 5.6, 5.7. Supports schema synchronization, full data synchronization, and incremental data synchronization. |
|   | MySQL synchronization to AnalyticDB MySQL 3.0 | MySQL versions 5.1 to 5.7, RDS MySQL versions 5.5, 5.6, 5.7. Supports schema synchronization, full data synchronization, and incremental data synchronization. |
|   | MySQL synchronization to DataHub | MySQL versions 5.1 to 5.7, RDS MySQL versions 5.5, 5.6, 5.7. Supports schema synchronization and incremental data synchronization, but does not support full data synchronization. |
|   | MySQL synchronization to MaxCompute | MySQL versions 5.1 to 5.7, RDS MySQL versions 5.5, 5.6, 5.7. Supports schema synchronization, full data synchronization, and incremental data synchronization. Supported DDL statements: ALTER TABLE, ADD COLUMN. |
|   | One-way synchronization between MySQL instances | MySQL versions 5.1 to 5.7, RDS MySQL versions 5.5, 5.6, 5.7. Supports schema synchronization, full data synchronization, and incremental data synchronization. |
| Data synchronizat ion |   |   |
|   | Two-way synchronization between MySQL instances | MySQL versions 5.1 to 5.7, RDS MySQL versions 5.5, 5.6, 5.7. Supports schema synchronization, full data synchronization, and incremental data synchronization. |
|   | Oracle synchronization to AnalyticDB PostgreSQL | Oracle versions 9i, 10g, 11g, 12c, 18c, 19c. Supports schema synchronization, full data synchronization, and incremental data synchronization. |
|   | Oracle synchronization to DataHub | Oracle versions 9i, 10g, 11g, 12c, 18c, 19c. Supports schema synchronization and incremental data synchronization. |

|   | PolarDB-X 1.0 synchronization to AnalyticDB MySQL 3.0 | RDS MySQL versions 5.1 to 5.7 attached to PolarDB-X 1.0. Supports schema synchronization, full data synchronization, and incremental data synchronization. |
|---|---|---|
|   | PolarDB-X 1.0 synchronization to PolarDB-X 2.0 | RDS MySQL versions 5.1 to 5.7 attached to PolarDB-X 1.0. Supports full data synchronization and incremental data synchronization, but does not support schema synchronization. |
|   | Synchronize data from PolarDB-X 2.0 to PolarDB-X 1.0 | Supports full data synchronization and incremental data synchronization. Schema synchronization is not supported. |
|   | Synchronize data from PolarDB-X 2.0 to AnalyticDB for MySQL 3.0 | Supports schema synchronization, full data synchronization, and incremental data synchronization. |
|   | PolarDB-X 2.0 synchronization to AnalyticDB PostgreSQL | Supports schema synchronization, full data synchronization, and incremental data synchronization. |
|   | PolarDB-X 2.0 synchronization to MySQL | Supports schema synchronization, full data synchronization, and incremental data synchronization. |
|   | Data synchronization between PolarDB-X 2.0 instances | Supports schema synchronization, full data synchronization, and incremental data synchronization. |
|   | PostgreSQL synchronization to AnalyticDB PostgreSQL | Only supports full and incremental data synchronization, does not support schema synchronization. DDL synchronization is not supported. One task only supports synchronization of one database. |
|   | Synchronize data from ApsaraDB for MongoDB to Kafka | Supports only full and incremental data synchronization. Schema synchronization is not supported. Supports self-managed Kafka versions 0.1 to 2.7. |
|   | Data synchronization between Redis or Tair Enterprise Edition instances | Supported architectures: standard and cluster. Supported version: 5.0. Supports one-way and two-way synchronization. |

|   | Data synchronization between Redis Community Edition instances | Supported architectures: standard and cluster. Supported versions: 4.0, 5.0. |
|---|---|---|
|   | Data synchronization between SQL Server instances | Supported SQL Server versions: 2005 to 2017. Supports schema synchronization, full data synchronization, and incremental data synchronization. |
| Disaster recovery | Zone-disaster recovery | Supports zone-disaster recovery. |
|   | Geo-disaster recovery | Supports geo-disaster recovery. |
| Security | HTTPS certificate encryption | DTS Portal supports national cryptographic HTTPS access. |
|   | Resource isolation between different accounts | Integrates with ASCM to achieve resource isolation between different department accounts. |
|   | Security audit | Supports security audit. |
| Multi-region deployment | Multi-region deployment | Supports multi-region deployment. |
| Monitoring and alerting | Support for task alerting configuration | Supports configuration of task latency and task failure alerts. |
|   | Online SQL conversion | Real-time conversion of Oracle, Db2, Teradata SQL to multiple target databases such as PolarDB, AnalyticDB PostgreSQL, and other mainstream open-source databases. |
|   | Application profile | Java application profile information display. |
|   | Application evaluation | Java application evaluation details, modification points, and modification suggestions. |
|   | Application data collection | Source database Oracle, Db2, Teradata, Java application data collection (business SQL). |
|   | Incremental data comparison | Oracle, Db2, Teradata source database incremental comparison. |

| Data and application migration assessment (ADAM) |   |   |
|---|---|---|
|   | Support for hot upgrade functionality | Supports hot upgrades for subsequent assessment migration function iterations. |
|   | Support for high availability | Supports multi-data center disaster recovery. |
|   | Source database verification | Oracle, Db2, Teradata source database structure comparison. |
|   | Migration plan generation | Supports migration from mainstream open-source databases to PolarDB, AnalyticDB PostgreSQL. |
|   | Schema migration/revision | Supports schema revision and modification suggestions for migration from mainstream open-source databases to PolarDB, AnalyticDB PostgreSQL. |
|   | Source database profile | Display of collected source database profile. |
|   | Target database compatibility assessment | Display of source database assessment details, compatibility details, incompatibility points and reasons. |
|   | Target database selection recommendations | Compatibility selection recommendations for multiple target databases. |
| DTS data consistency verification and correction | Data consistency verification and correction | Supports creating data verification and correction tasks for database tables. |
| DTS periodic data integration | Periodic data integration | Relies on DMS task orchestration and scheduling functions to achieve periodic full data migration through orchestrated periodic data integration tasks. |
| DTS data ETL, stream and batch processing basic package | DTS data ETL stream and batch processing | Supports creating ETL tasks, stream and batch computing tasks for data processing with DTS Pro. |
| Cross-cloud synchronizat ion functionality | One-way and two- way synchronization across two clouds | Supports only MySQL versions 5.1 to 5.7 and RDS MySQL versions 5.5, 5.6, and 5.7. |
