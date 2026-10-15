---
title: "Alibaba Cloud Apsara Stack v3.18.6-2607 ApsaraDB for POLARDB Product Introduction 20260901"
product_version: "V3.18.6_2607"
doc_version: "20260901"
pdf_pages: 29
source_pdf: "b7fab4f039128fa1_Alibaba Cloud Apsara Stack v3.18.6-2607 ApsaraDB for POLARDB Product Introduction 20260901.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/3816%202607/pdf%203/%E4%BA%91%E5%8E%9F%E7%94%9F%E6%95%B0%E6%8D%AE%E5%BA%93%20PolarDB/Alibaba%20Cloud%20Apsara%20Stack%20v3.18.6-2607%20ApsaraDB%20for%20POLARDB%20Product%20Introduction%2020260901.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings)
---

# Alibaba Cloud Apsara Stack v3.18.6-2607 ApsaraDB for POLARDB Product Introduction 20260901

## Table of Contents

- 1 Product details
- 2 Benefits
- 3 Scenarios
- 4 Features
  - 4.1 Features of PolarDB for MySQL
    - 4.1.1 Primary/Secondary edition
  - 4.2 Features of PolarDB for PostgreSQL
    - 4.2.1 Primary/Secondary edition
  - 4.3 Features of PolarDB-X
    - 4.3.1 Functions and features

ails

## 1 Product details

PolarDB is a powerful cloud-native database. It delivers high availability, high performance, and easy scalability, making it suitable for enterprise applications of any scale.

**Product engine introduction**

PolarDB offers three database engines: PolarDB for MySQL, PolarDB for PostgreSQL, and PolarDB HTAP Edition (short for PolarDB-X). You can quickly create a database instance that suits your application scenario. PolarDB for MySQL Edition PolarDB for MySQL Edition is Alibaba Cloud's self-developed cloud-native relational database. It provides you with database services featuring ultra-high elasticity and performance, high availability and reliability, and cost-effectiveness. PolarDB for MySQL Primary/Standby Edition This edition uses a high-availability architecture consisting of one primary instance and one standby instance. These instances are deployed on different physical machines, either in the same data center or across different data centers. Data is synchronized between them via streaming replication (log transmission). Requests are routed directly to the primary instance via Server Load Balancer (SLB). The primary/standby highavailability architecture remains available even if one node fails. If the standby instance fails, the management and control component initiates a standby database rebuild process on a third machine (other than the primary and standby nodes). This restores the standard one-primary-one-standby configuration. Since all traffic accessing the connection string is directed to the primary database, neither the standby database failure nor its rebuild process affects business availability. PolarDB for PostgreSQL Edition

**Primary/Standby Edition**

This edition uses a high-availability architecture consisting of one primary instance and one standby instance. These instances are deployed on different physical machines, either in the same data center or across different data centers. Data is synchronized between them via streaming replication (log transmission). Requests are routed directly to the primary instance via Server Load Balancer (SLB). The primary/standby highavailability architecture remains available even if one node fails. If the standby instance fails, the management and control component initiates a standby database rebuild process on a third machine (other than the primary and standby nodes). This restores the standard one-primary-one-standby configuration. Since all traffic accessing the connection string is directed to the primary database, neither the standby database failure nor its rebuild process affects business availability. PolarDB HTAP Edition (short for PolarDB-X) PolarDB-X is a high-performance, cloud-native distributed database designed and developed by Alibaba Group. It delivers high throughput, large storage capacity, low latency, easy scalability, and ultra-high availability for the cloud era. PolarDB-X has consistently supported all business related to Alibaba Group's Double 11 Shopping Festival. After more than a decade of refinement, it delivers strong data consistency, high system stability, and rapid cluster elasticity. It is widely used in public sectors including finance, judicial and taxation services, transportation and logistics, and power and energy. PolarDB-X firmly follows an open, self-controlled development path. It builds distributed capabilities around the open-source MySQL ecosystem, minimizing learning and usage costs for users.

**Product details**

ails

**PolarDB for MySQLEdition**

**Compute-storage separation**

ApsaraDB PolarDB uses a compute-storage separation architecture. Database proxies and compute nodes run on separate Elastic Compute Service (ECS) instances. The shared storage layer uses Enterprise SSD (ESSD) disks, which significantly reduces your PolarDB costs.

**Super MySQL**

PolarDB is 100% compatible with native MySQL and ApsaraDB RDS for MySQL. You can migrate your MySQL database to PolarDB for MySQL without changing any application code or configuration. PolarDB delivers high-value features such as one-write-multiple-read, shared storage, stable operation with up to 6 billion rows of data, DDL within seconds, primary/secondary switchover without transient disconnection, flashback query, and enhanced partitioned tables.

**Data security**

PolarDB for MySQL supports transparent data encryption (TDE). TDE encrypts and decrypts data files in real-time during I/O. The system encrypts data before writing it to disk and decrypts it when reading from disk into memory. TDE does not increase the size of data files, and developers can use TDE without changing any application code.

**Global secondary index**

A global secondary index (GSI) indexes data across the entire table. Index entries may have identical key values but come from different partitions, or they may combine multiple distinct key values.

**SQL audit**

You can enable the SQL audit feature to record all Data Manipulation Language (DML) and Data Definition Language (DDL) operations. Built-in security engines audit database activities in real time. Real-time detection: Detect various attacks and threats in real time and identify security risks promptly. High-risk operation identification: Use intelligent algorithms and large-scale models to identify high-risk operations . Abnormal access source identification: Automatically detect new or abnormal access sources.

**PolarDB PostgreSQLEdition**

**Backup and restoration**

Data backup
    - Automatic backup: The system generates a default automatic backup policy when you
create an instance. The system performs full physical backups periodically based on the policy and uploads them to Object Storage Service (OSS). You can modify settings such as the backup cycle, retention period, and backup task scheduling time for the automatic backup policy on the O&M console.
    - Manual backup: You can manually create physical backups on the O&M console.
Log backup ails The system periodically uploads logs generated by instances to OSS and rotates them promptly after successful upload to save disk space on physical machines. You can modify settings such as the number of retained logs and the log retention period on the O&M console. Restore from a backup set PolarDB allows you to create a new instance from an existing backup set. Clone instance PolarDB allows you to clone an existing instance to create a new one. The new instance is independent and inherits only data from the original instance at the time of cloning. Point-in-time recovery PolarDB supports point-in-time recovery. To use this feature, you must ensure that a full backup set is available before your target point in time and that all WAL logs between the full backup set and the target point in time are stored in OSS. Point-in-time recovery creates a new instance that is independent of the original one.

**TDE**

TDE encrypts and decrypts data files in real time during I/O. Data is encrypted before writing to disk and decrypted when reading from disk into memory. TDE does not increase the data file size, and developers do not need to change any application code to use it.

**Data masking**

PolarDB provides the built-in DBMS_REDACT package to mask or redact data returned by queries, which helps obfuscate sensitive data. DBMS_REDACT includes stored procedures to create, modify, enable, disable, and delete masking policies. You can use these procedures to customize data obfuscation.

**SQL firewall**

Preventing SQL injection attacks is typically the responsibility of database application developers, and database administrators have limited defense capabilities. The SQL/Protect plug-in detects SQL injections by analyzing incoming queries. When it detects a potentially dangerous query, it alerts the database administrator and immediately blocks the execution of the query.

**SQL audit**

PolarDB supports SQL audit, allowing you to view detailed SQL information and perform periodic SQL audits. Enabling the SQL audit feature does not affect instance performance.

**PolarDB HTAP Edition(short forPolarDB-X)**

**Centralized and distributed architecture**

A single system offers both centralized and distributed architectures, allowing you to flexibly select the best fit for your business needs. This approach reduces customer investment and operational costs for database systems. Distributed instances resolve performance and capacity scaling bottlenecks of centralized systems through horizontal data partitioning, table sharding, and clustered deployment of individual services. These capabilities deliver the elastic scalability and massive capacity that are essential for distributed databases.

**Cloud-native database**

The system integrates seamlessly with the cloud platform, enabling unified network management, monitoring and alerting, O&M, authentication, tenant planning, and quota management. ails

**Two database-level modes: DRDS (database and table**

**sharding) and AUTO (partitioned tables)**

Both modes can coexist within a single instance. If you previously used DRDS 1.0, the transition to PolarDB-X is seamless and requires minimal application modifications. Additionally, comprehensive data migration services are provided.

**High reliability and high availability**

Powered by the proprietary X-Paxos protocol library and the X-DB storage engine, the system effectively eliminates issues such as read, write, and space amplification, as well as tombstones and frequent compaction. This significantly enhances system and data stability and consistency while reducing resource consumption. Built on multi-node Paxos strong consistency, the system guarantees zero data loss (RPO is 0) during single-node failures. It supports multiple disaster recovery architectures, including 3-node/4-replica active-active deployments across two data centers in the same region, 3-data-center disaster recovery within the same region, and cross-region disaster recovery. Furthermore, all platform management components are designed for high availability, ensuring that O&M node failures do not impact normal business operations.

**High compatibility**

PolarDB-X is highly compatible with MySQL. The centralized mode supports MySQL 5.7 and 8.0, enabling seamless migration with zero application modifications. The distributed mode offers high compatibility with MySQL 5.7 and 8.0, covering SQL syntax and functions. It features a Global Timestamp Service (GTS) to ensure globally consistent distributed transactions. Powered by TSO and 2PC, it delivers full ACID capabilities for databases, meeting Read-Committed and Repeatable-Read isolation levels in distributed environments. Additionally, it provides Global Secondary Indexes (GSI) built on top of distributed transactions. Transactional multi-write ensures strong consistency between indexes and primary tables, while a Cost-Based Optimizer (CBO) enables intelligent index selection. Furthermore, at the metadata and ecosystem integration levels, PolarDB-X leverages Online DDL to ensure metadata consistency across distributed nodes. At the hardware level, it is certified to be compatible with mainstream Chinese chip architectures, such as Kunpeng and Hygon.

**High scalability**

Built on a Share-Nothing architecture, PolarDB-X supports horizontal scaling. Vertical scaling is achieved by upgrading or downgrading node specifications, while horizontal scaling is accomplished by adding or removing nodes. Overall system performance scales linearly with the number of nodes. Online scaling is supported to meet elasticity requirements of your business. In Online Transaction Processing (OLTP) scenarios, it handles tens of millions of concurrent connections and supports PB-scale data storage. In Online Analytical Processing (OLAP) scenarios, its Massively Parallel Processing (MPP) technology enables linear improvement in query performance after machines are scaled out, satisfying complex report query demands such as TPC-H.

**One cloud, multiple resource pools**

You can flexibly allocate physical machines to create multiple resource pools within a single cloud. This enables physical machine-level resource isolation and fault isolation for applications of different tiers, various branches, and production and testing systems.

**Resource efficiency**

Storage nodes adopt a one-primary, one-secondary, plus log architecture. This design guarantees zero data loss across three nodes while consuming the resources of only approximately 2.3 replicas, thereby reducing software and hardware procurement costs by 23%. ails

**Native MySQL global Binlog**

In the mainstream distributed database market, vendors have historically overlooked distributed change logs, such as redo logs and binlogs. However, given the evolution of relational databases, ecosystem and standards are crucial for market scalability. PolarDB-X supports global binlog capabilities, ensuring compatibility with and embracing the MySQL database ecosystem. You can interact with PolarDB-X just like a MySQL database and obtain binlog logs using the standard binlog dump protocol. Powered by the Change Data Capture (CDC) component, PolarDB-X delivers a globally consistent, native MySQL Binlog service. This allows upstream and downstream ecosystems to consume data exactly as they would from a standalone MySQL instance, significantly enhancing capabilities for data synchronization, backup, and restoration.

**SQL diagnosis and optimization**

This feature provides comprehensive O&M capabilities, including SQL audit and analysis, instance sessions, slow query logs, space analysis, lock analysis, performance trends, and real-time performance. These capabilities empower DBAs to efficiently manage databases and quickly troubleshoot issues.

**Distributed transactions**

Globally consistent distributed transactions are provided, ensuring strong global read-write consistency for distributed transactions.

**Global secondary indexes**

Global secondary indexes and global unique indexes are provided to enhance the convenience of multi-dimensional business queries.

**SQL flashback queries**

Convenient row-level data flashback capabilities are provided to address accidental SQL operations.

**High performance**

PolarDB-X partitions data based on business needs, clustering it closely with primary business operations to optimize response times for online transactional workloads. It supports scalable read-only nodes with automatic read-write splitting to enhance read performance. By isolating production traffic from analytical workloads, it ensures the stability of your core production systems.

**Backup**

Both local backups and remote (cross-region) backups are supported, fulfilling the mutual backup requirements across multiple data centers. Features include point-in-time recovery (PITR), customizable backup policies, and a visual management console for backup sets.

**Security and control**

PolarDB-X features a comprehensive account and permission system compatible with standalone databases. It also provides robust security capabilities, such as multi-tenant isolation, IP whitelists, SQL audit, TLS (SSL) transport encryption (TLSv1.2 and TLSv1.3), and TDE for storage.

**Permissions**

On the console, you can achieve unified multi-level tenant management, including dynamic resource configuration, usage statistics, and strict resource isolation. Premission management and fine-grained user operation auditing are provided. ails A robust permission authentication and isolation mechanism is provided to ensure the privacy of your data. Resource isolation is supported via the multi-tenant mode.

## 2 Benefits

You can use the cloud-native database PolarDB just as you would a traditional database. PolarDB has the following benefits:

**PolarDB for MySQL**

**Cost-effective**

Multiple compute nodes share the same storage. When you add read-only nodes, you only pay for the compute nodes. This significantly reduces scale-out costs.

**Highly elastic**

You can add or remove nodes in minutes. You can scale out storage capacity online without interrupting your business.

**High performance**

The database kernel is highly optimized. It uses physical replication, high-speed networks, and distributed shared storage to significantly improve performance. Performance is up to 6 times better than that of open source MySQL.

**High availability and reliability for data security**

The Primary/Secondary Edition uses a primary-secondary high availability (HA) architecture. It can maintain availability if one node fails. If the secondary node fails, the management component rebuilds the secondary database on a different healthy machine. This restores the normal primary-secondary state. The failure and reconstruction of the secondary database do not affect business availability because all traffic from the connection string is directed to the primary database.

**Data security**

Comprehensive security measures, such as whitelists, VPC networks, and multi-replica data storage, secure data access, storage, and management.

**Lock-free backup**

Using the snapshot technology of the underlying distributed storage, the entire backup process does not require locks. This results in higher efficiency and reduced impact.

**PolarDB for PostgreSQL**

**Simple and easy to use**

Fully compatible with PostgreSQL and highly compatible with Oracle syntax. Your code and applications require few or no modifications.

**Lock-free backup**

Using the snapshot technology of the underlying distributed storage, the entire backup process does not require locks. This results in higher efficiency and reduced impact.

**Fast elasticity for uncertain business growth**

You can upgrade or downgrade specifications in minutes. You can add or remove nodes in minutes.

**Extreme performance**

A cluster can contain one primary node and up to 15 read-only nodes. This meets the performance requirements of high-concurrency scenarios, especially for read-intensive workloads.

**High availability and reliability for data security**

The Primary/Secondary Edition uses a primary-secondary high availability architecture. It can maintain availability if one node fails. If the secondary node fails, the management component rebuilds the secondary database on a different healthy machine. This restores the normal primary-secondary state. The failure and reconstruction of the secondary database do not affect business availability because all traffic from the connection string is directed to the primary database.

**PolarDB-X**

**Cloud-native and MySQL ecosystem**

Using cloud resources and containerization, PolarDB-X can create or reconfigure a cluster in minutes without manual intervention. Various ecosystem tools from Alibaba Cloud and the open source community provide continuous support for PolarDB-X. These products include Data Transmission Service (DTS), Database Backup (DBS), Data Management (DMS), Database Autonomy Service (DAS), Data Integration, Cloud Monitor, and Performance Testing (PTS). PolarDB-X actively embraces and contributes to the MySQL ecosystem. It is now fully compatible with the MySQL ecosystem in terms of protocols, syntax, transaction behavior, account systems, security, and the command line interface.

**Storage-compute disaggregation architecture**

To maximize cloud database scalability, PolarDB-X uses a Shared-Nothing system architecture based on storage-compute disaggregation. This architecture allows for layered capacity planning as needed. The data nodes (DNs) of PolarDB-X are built on X-DB, a three-node, strong consistency database developed by Alibaba. It provides full compatibility with MySQL syntax and the ability to process complex queries. X-DB, combined with the cost-based optimizer (CBO) for hybrid transactional and analytical processing (HTAP) in PolarDB-X, precisely controls computation pushdown for improved overall performance.

**Transparent distributed experience**

PolarDB-X aims to provide an experience of operating a distributed database that is as simple as using a standalone MySQL database. To achieve this, PolarDB-X offers the following easy-to-use, transparent distributed capabilities: By default, PolarDB-X uses automatic sharding based on the primary key. This removes the need to design a **partition key** when you migrate data and services, and enables automatic sharding. High-performance, strong consistency distributed transactions. PolarDB-X uses the selfdeveloped X-Paxos protocol to ensure a recovery point objective (RPO) of 0 during failover. It also uses a Timestamp Oracle (TSO) policy and distributed Multi-Version Concurrency Control (MVCC) to guarantee the isolation and consistency of distributed transactions. Distributed linear scaling. PolarDB-X uses a partitioning policy based on consistent hashing for effective load balancing and hot spot suppression. During scale-out, it maintains computation pushdown and data consistency with zero impact on your business. Parallel processing and throttling capabilities provide strong support for business continuity during scaling. Global binary logging and globally consistent backups. These features solve the challenges of streaming data from each node of a distributed database to downstream systems, along with recovery consistency issues caused by different backup times across nodes.

## 3 Scenarios

PolarDB, a cloud-native database, is designed for a wide range of business scenarios. It delivers high performance, high availability, and high scalability to meet diverse business needs.

**PolarDB for MySQL edition**

**Migration with zero code changes and revitalized MySQL**

**performance**

As your business grows, traditional MySQL systems may face performance bottlenecks and scaling challenges. Recommended solution: Migrate your existing MySQL database to PolarDB. PolarDB is 100% compatible with MySQL 8.0, allowing most applications to migrate seamlessly without code modifications. After migration, you will experience a significant performance boost over opensource MySQL, powered by Remote Direct Memory Access (RDMA) high-speed networking and distributed shared storage. You can also leverage the lock-free backup feature to back up terabyte-scale data within minutes without impacting online operations.

**Real-time analytics and dynamic report generation**

Enterprises need real-time business data analysis to drive operational decisions. However, the traditional transactional + analytical architecture suffers from data synchronization latency and high maintenance costs. Recommended solution: Leverage the native HTAP capability of PolarDB. Within a single logical instance, you can achieve read/write splitting by routing transactional requests to the primary node and analytical requests to read-only nodes. Data is instantly available for analysis immediately after being written, eliminating the need for ETL. This ensures real-time analytics while completely isolating analytical workloads from transactional operations.

**PolarDB for PostgreSQL edition**

**Fully controllable database**

**Scenario**: For customers requiring data autonomy and control, PolarDB holds relevant
qualifications.
**Product capabilities:**PolarDB for PostgreSQL is 100% compatible with PostgreSQL syntax
and highly compatible with Oracle syntax. Its open-source ecosystem satisfies all autonomy and control requirements.

**Oracle database migration to the cloud**

**Scenario**: An end-to-end Oracle migration solution validated by 200+ customers is provided,
ensuring an efficient and low-risk transition.
**Product capabilities**:

**High compatibility with Oracle syntax**

SQL compatibility: Industry-leading compatibility for data types, SQL syntax, stored procedures, and packages is provided. Critical feature compatibility: Partitioned tables, CONNECT BY, DBLINK, PL/SQL, stored procedures, flashback, and global indexes are supported. Client compatibility: PolarDB is fully compatible with Oracle OCI, Pro*C, Java, Windows, and .NET drivers, and provides client compatibility tools.
**Efficient, low-risk Oracle migration** (lower cost, shorter cycle, fewer modifications, and
reduced risk): PolarDB provides assessment and analysis tools to evaluate compatibility and estimate modification effort. Automatic conversion capabilities reduce adaptation costs and ensure predictable project timelines. Data Transmission Service (DTS) tools is supported to guarantee migration integrity. Full and incremental synchronization ensures uninterrupted service during migration. Twoway synchronization allows rollback in case of anomalies, keeping migration risks under control. PolarDB provides end-to-end expert support covering assessment, migration implementation, and performance optimization.

**Multi-model AI scenarios and Agent long-term memory**

In RAG and Memory scenarios, using a single multi-model database can significantly reduce database costs and enable multiple technical approaches via plugins. The following describes a typical long-term memory scenario for a database: Memory engine: We recommend the Mem0 framework, an advanced memory framework designed for AI Agents. It integrates long-term and short-term memory, and categorizes information into working, factual, and situational types. Furthermore, it natively supports PolarDB's vector and graph data engines. Base data engine: The PolarDB for PostgreSQL edition natively integrates the PGVector vector engine and a graph engine compatible with Apache AGE. This all-in-one architecture avoids the complexity of stitching together multiple systems and leverages cloud-native capabilities to ensure exceptional performance and scalability.

**PolarDB Converged Edition (Centralized & Distributed)**

**(PolarDB-X)**

**High-load, low-latency transactions**

**Scenario**: Transaction systems are among the most critical components of information
systems. Business continuity, transactional consistency, and system security form the foundation for their reliable operation. Sustained high-load, low-latency performance represents the future direction for transaction systems.
**Product capabilities**: PolarDB Converged Edition (Centralized & Distributed) employs the
self-developed majority-consensus protocol X-Paxos on storage nodes to deliver strong triplereplica consistency. This ensures an Recovery Point Objective (RPO) of zero during highavailability failover and disaster recovery scenarios. Additionally, powered by a global Timestamp Oracle (TSO) clock and distributed Multi-Version Concurrency Control (MVCC), distributed transactions guarantee transactional consistency across multi-node data access.

**High peak-to-valley traffic**

**Scenario**: High peak-to-valley differences refer to system access scenarios where peak load
is over 20 times the valley load within a specific period. This is commonly seen in flash sales, group buying, and time-limited promotions. System administrators often face the dilemma of balancing capacity safety and cost control, making cost optimization and seamless scaling core requirements.
**Product capabilities**: PolarDB Converged Edition (Centralized & Distributed) leverages a
distributed linear scaling mechanism that maintains compute pushdown and data consistency during scaling, achieving zero business disruption. Combined with traffic control capabilities, it further enhances business stability throughout the scaling process.

**Centralized data storage**

**Scenario**: Also known as data centralization or data aggregation, this scenario typically
resides in the Operational Data Store (ODS) layer of an enterprise data architecture and serves to consolidate data from various vertical business sources. The primary requirements for this scenario include high-concurrency writes, large-capacity storage, multi-dimensional queries, and low-cost data egress.

**Product capabilities**

PolarDB Converged Edition (Centralized & Distributed) seamlessly scales up/down or out/in based on traffic and storage needs to meet demands for high-concurrency writes and massive storage. Data Manipulation Language (DML) parallel computing and large transactions are supported to effectively satisfy batch processing requirements and execution efficiency. High-performance Global Secondary Index (GSI) allows users to query PolarDB Converged Edition (Centralized & Distributed) data along any dimension without being restricted by sharding rules. Global Binlog is a unified change log service for distributed databases that guarantees transaction ordering. It is compatible with MySQL Binlog file format and Dump protocol, making downstream data consumption highly convenient.

**Rapid distributed transformation**

**Scenario**: When business volume approaches the limits of a single-node database, or when
oversized tables cause performance and maintenance issues, distributed transformation becomes a cost-effective solution. However, migrating the database is often the most complex part of this process. Users consistently demand the ability to use a distributed database just as easily as a single-node MySQL.
**Product capabilities**: PolarDB Converged Edition (Centralized & Distributed) introduces a
suite of transparent distributed capabilities that preserve the single-node MySQL experience to the greatest extent possible—across connections, development, and management. This dramatically shortens the distributed transformation cycles and allows development and operations teams to retain their existing technical stacks as much as poosible. Currently, PolarDB Converged Edition (Centralized & Distributed) supports a smooth evolution from single-node to distributed architectures. You can dynamically convert a large table into distributed partitioned tables via Data Definition Language (DDL). Combined with distributed transactions and MySQL-binlog-compatible data backflow, this enables a rapid transition from single-node to distributed systems.

**Autonomous and controllable database replacement**

**Scenario**: Achieving autonomy and control over information systems is a crucial step for
large enterprises undergoing digital transformation. As a core foundational software component, databases are prioritized for replacement. Autonomous and controllable database transformations are now widely underway in telecommunications, financial services, energy, and public institutions.
**Product capabilities**: PolarDB Converged Edition (Centralized & Distributed) is Alibaba
Cloud's self-developed cloud-native distributed database, designed for autonomy and control. It offers multiple deployment models—including public cloud, Apsara Stack, DBStack, and software editions—and features comprehensive delivery and service teams. It has already helped over a hundred enterprises complete commercial database replacements, core database distributed transformations, distributed database technical training, and architectural consulting.

## 4 Features

### 4.1 Features of PolarDB for MySQL

**MySQL**

This topic describes the features of PolarDB for MySQL.

#### 4.1.1 Primary/Secondary edition

This topic describes the features of Alibaba Cloud PolarDB for MySQLPrimary/Standby Edition, helping you quickly understand the product capabilities.

| Feature category |   | Description |
|---|---|---|
| Instance management | Create an instance | Create a PolarDB for MySQL Primary/Secondary Edition instance. |
|   | Restart an instance | Restart an instance to quickly restore its state. |
|   | Change configuration | Change an instance's configuration, such as specifications or storage space, if the current configuration does not meet application requirements or is too high or too low. |
|   | Set a maintenance window | The default maintenance window is 02:00 to 06:00. We recommend that you set the maintenance window to off- peak hours to avoid potential impact on services. |
|   | Release an instance | Release an instance after deleting all databases in it. |
|   | Upgrade a minor engine version | Upgrade the minor engine version automatically or manually. Minor engine version upgrades involve performance improvements, new features, or bug fixes. |
|   | Set instance parameters | View and modify values of some parameters. Query parameter modification records. |
|   | Read-only instances | Add a read-only instance. Read-only instances offload database pressure from the primary instance when the database has many read requests and few write requests. |
|   | Tag management | Create multiple tags. Attach different tags to instances for categorization. Then, filter instances using these tags. |

| Database management | Account management | Manage database account permissions. Two types of database accounts are supported: privileged accounts and standard accounts. |
|---|---|---|
|   | Create a database | After you create a PolarDB for MySQL instance and configure a whitelist, create databases and accounts within the instance. |
|   | Delete a database | Delete deprecated databases. |
|   | Database connections | View and modify database connection addresses. Log in to the database of a PolarDB for MySQL instance by using Alibaba Cloud Data Management Service (DMS). Use the hybrid access feature to smoothly migrate a classic network to a virtual private cloud (VPC) without service interruption. Switch the network type of an instance between classic network and virtual private cloud. Switch the VPC and vSwitch of an instance. |
|   | Database proxy | Use the dedicated proxy service,which provides advanced features such as read/write splitting, connection pooling, and transaction splitting. |
| Monitoring and alerts | View system resources and engine monitoring | View comprehensive performance monitoring items. Select a query time to view corresponding monitoring data. |
|   | Set an alert rule | Create alert rules to promptly detect abnormal instance monitoring data and handle it quickly. |
| Cloud Monitor | View a monitoring dashboard | View Cloud Monitor metrics to quickly locate O&M issues. |
|   | Set an alert rule | Create alert rules to trigger alerts when cloud service monitoring metrics reach specified thresholds and notify relevant users promptly. |
|   | View alert history | After an alert is triggered, view alert history filtered by cloud product, cloud service instance, alert level, and more. Export and download alert history for local data analysis. |
|   | Set a whitelist | Set a whitelist to enhance database security and stability. |

| roduct Introduction· | Features ApsaraDB for POLARD |   |
|---|---|---|
| Data security |   |   |
|   | IP type and whitelist | Assign either IPv4 single-stack or IPv4/IPv6 dual-stack addresses to accommodate diverse network environment requirements. In dual-stack mode, independent IPv6 whitelists can be configured to enforce precise access control. |
|   | Set SSL encryption | Enable Secure Sockets Layer (SSL) encryption and install the SSL CA certificate on required application services to improve link security. |
|   | Set TDE | Transparent Data Encryption (TDE) performs real-time I/O encryption and decryption on data files. Data is encrypted before being written to disk and decrypted when read from disk into memory. |
|   | SQL audit | View SQL details. Audit SQL regularly. |
| Service availability | Automatic or manual primary/secondary switchover | Set primary and secondary instances for automatic or manual switchover. After a switchover, the original primary instance becomes the secondary instance. |
|   | Modify data replication method | Set the data replication method between PolarDB for MySQL primary and secondary instances to improve cloud database availability. |
| Backup and restore | Backup methods | Manual backup and automatic backup methods are supported. |
|   | Download data backups and log backups | Download unencrypted data backups and log backups for archiving data or restoring data to local databases. |
|   | One-click binlog upload | Upload binlog with one click to save log backups to Object Storage Service (OSS). |
|   | Database recovery | Create a new instance that replicates the content of the primary instance exactly, including instance data and settings. Clone instances are mainly used to restore primary instance data or create multiple identical instances in batches. |

| Autonomous service | One-click diagnostics | Use the one-click diagnostics feature to diagnose instances and view visualized diagnostic results. |
|---|---|---|
|   | Session management | Use the instance session feature to view and manage sessions of target instances. |
|   | Real-time performance | View real-time performance of MySQL. |
|   | Storage analysis | Use the storage analysis feature to promptly detect abnormal database space and prevent impacts on database stability. |
|   | Lock analysis | View and analyze the most recent deadlock in the database. |
|   | Performance trend | View performance trends in multiple ways. You can view the performance trend range, compare performance trends, and view the customized performance trends. |
|   | Slow SQL statements | View slow log trends, execution details, and suggestions. |
|   | Diagnostic report | Create and view diagnostic reports. |
| Log management | Log query | Query error logs, slow log details, and primary/secondary switchover logs of instances to help locate and analyze faults. |
| Parameter management | Set instance parameters | View and modify values of some parameters. Trace parameter change history. |
|   | Use parameter templates | Use parameter templates to centrally manage identical or partially identical parameter configurations across multiple instances. Quickly apply templates to target instances to improve parameter management and instance configuration efficiency. |
| Recycle bin | Recover an instance | Use the instance-level recycle bin. After an instance is deleted, recover it from the recycle bin. Modify the recycle bin's retention period. |
|   | Destroy an instance | Destroying an instance also destroys all backups except cross-region backups, including regular data backups, log backups, and permanent backups. |

| Intelligent data migration | Migrate from RDS MySQL to PolarDB for MySQL | Migrating from RDS MySQL to PolarDB for MySQL is supported by PolarDB. |
|---|---|---|
|   | Migrate from PolarDB for MySQL 5.7 to PolarDB for MySQL 8.0 | Migrating PolarDB for MySQL 5.7 to PolarDB for MySQL 8.0 is supported by PolarDB. |

### 4.2 Features of PolarDB for PostgreSQL

**PostgreSQL**

#### 4.2.1 Primary/Secondary edition

This topic describes the features of Alibaba Cloud PolarDB for PostgreSQL Primary/Standby Edition (formerly known as PolarDB for PostgreSQL with local disks). This helps you quickly understand the product's capabilities.

| Feature category |   | Description |
|---|---|---|
| Instance management | Create an instance | Create a PolarDB for PostgreSQLActive-Standby Edition instance. |
|   | Restart an instance | Restart an instance to quickly restore its status. |
|   | Modify the configuration | If an instance's configuration is excessive or insufficient for your application's requirements, you can change its specifications or storage space. |
|   | Set a maintenance window | The default maintenance window is 02:00 to 06:00. We recommend that you set the maintenance window to off- peak hours as needed. This helps prevent potential impact on your business during maintenance. |
|   | Perform a primary/secondary switchover | To ensure high availability of databases, PolarDB provides the primary/secondary switchover feature. The system automatically switches to the secondary instance when the primary instance is unavailable. You can also manually switch your business to the secondary instance. |
|   | Release an instance | After all databases in an instance are deleted, you can release the instance. |

|   | Recycle bin | Restore instances: The recycle bin allows you to restore deleted instances. You can also modify the retention period for instances in the recycle bin. Destroy instances: When you destroy an instance, the system destroys all backups except cross-region backups. These backups include regular data backups, log backups, and permanent backups. |
|---|---|---|
|   | Read-only instances | Add a read-only instance. Read-only instances offload database pressure from the primary instance when the database has many read requests and few write requests. |
|   | Configure instance parameters | View and modify the values of some parameters. Query parameter modification records. |
|   | Tag | Create multiple tags. Add different tags to your instances to classify them. Then, you can filter instances by tag. |
| Quick migration | Migrate data from ApsaraDB RDS for PostgreSQL to PolarDB for PostgreSQL via GUI | Migrate data from ApsaraDB RDS for PostgreSQL to PolarDB for PostgreSQL through visualized operations. |
| Database connections | Connect to PolarDB databases by using clients | Connect to PolarDB databases by using the pgAdmin4 client. |
|   | Log in to a PolarDB database by using DMS | Log in to a database in a PolarDB instance by using Data Management (DMS) of Alibaba Cloud. |
|   | Hybrid access | PolarDB for PostgreSQL instances support hybrid access. This feature allows you to smoothly migrate from the classic network to a virtual private cloud (VPC) without interrupting access. |
|   | Manage internal endpoints and ports | View and change the internal endpoint and port number of a PolarDB for PostgreSQL cluster on the PolarDB console. |
|   | Change the network type | Switch the network type of instances between the classic network and virtual private cloud. |
|   | Create an account | Create two types of database accounts: privileged accounts and standard accounts. |
| > Document Version: | 20260901 2 |   |

| roduct Introduction· | Features ApsaraDB for POLARD |   |
|---|---|---|
| Account management |   |   |
|   | Reset an account | Reset the password of an account on the PolarDB console. |
|   | Delete an account | Delete a database account on the PolarDB console. |
| Database management | Create a database | After you create a PolarDB for PostgreSQL instance and configure a whitelist, create a database and an account in the instance. |
|   | Delete a database | Delete deprecated databases. |
| Monitoring and alerts | View monitoring data | View resource monitoring data of instances on the PolarDB console. |
|   | Configure alert rules | Create alert rules on the PolarDB console. |
| Cloud Monitor | View a monitoring dashboard | View Cloud Monitor metrics to quickly locate O&M issues. |
|   | Configure alert rules | Create alert rules to trigger alerts when cloud service monitoring metrics reach specified thresholds and notify relevant users promptly. |
|   | View alert history | After an alert is triggered, view alert history filtered by cloud product, cloud service instance, alert level, and more. Export and download alert history for local data analysis. |
| Data security | Configure an IP whitelist | Configure a whitelist to enhance database security and stability. |
|   | IP type and whitelist | Assign either IPv4 single-stack or IPv4/IPv6 dual-stack addresses to accommodate diverse network environment requirements. In dual-stack mode, independent IPv6 whitelists can be configured to enforce precise access control. |
|   | Configure SSL encryption | Enable Secure Sockets Layer (SSL) encryption and install the SSL CA certificate on required application services to improve link security. |
|   | Set TDE | Transparent Data Encryption (TDE) performs real-time I/O encryption and decryption on data files. Data is encrypted before being written to disk and decrypted when read from disk into memory. |
| 2 | > Document Version: 2026090 |   |

|   | SQL audit | View SQL details. Audit SQL periodically. |
|---|---|---|
|   | Back up data | Adjust the backup policy to set automatic backup cycles for PolarDB data backups and log backups. You can also manually back up PolarDB data. |
|   | Download data backup files and log backup files | Download unencrypted data backup files and log backup files. Archive the backup files that you downloaded and use the backup files to restore data to on-premises databases. |
| Backup and restoration |   |   |
|   | Restore data | Create a new instance that replicates the content of the primary instance exactly, including instance data and settings. Clone instances are mainly used to restore primary instance data or create multiple identical instances in batches. |
| Plugin management | Plugin management | Install and uninstall extension plugins. Flexibly enable advanced features such as spatial geographic information (PostGIS), full-text query, and vector computation to meet diverse business requirements. |
| Log management | Log query | Query error logs, slow log details, and primary/secondary switchover logs of instances to help locate and analyze faults. |
| Parameter configuration | Modifiable parameters | Modify the values of modifiable parameters. |
|   | View the parameter modification history | View the parameter modification history. |
| CloudDBA | Quick diagnosis | Use the quick diagnosis feature to diagnose instances and obtain visualized diagnostic results. |
|   | Slow SQL queries | View the trends and statistics of slow queries. |

### 4.3 Features of PolarDB-X

#### 4.3.1 Functions and features

This topic describes the functions and features of Alibaba Cloud PolarDB-X to help you quickly understand the product.

| Feature category | Feature | Description |
|---|---|---|

| Instance management | Read-only instance | Create read-only instances and provide read-only cluster resources with trace traffic isolation to ensure the stability of online services and the primary cluster while supporting Hybrid Transactional/Analytical Processing (HTAP) load workloads. |
|---|---|---|
|   | Add or remove nodes | Change the number of nodes for both the primary instance and read-only instances simultaneously. |
|   | Instance details | Query the list of existing instances and view the details of each instance. |
|   | Log in to the database | Log in to an instance and manage database instances through a graphical interface. |
|   | Account management | Provide a database account permission system. Support a standalone MySQL-compatible account and permission system to ensure secure account operations for different roles. Modify account permissions, lock accounts, and delete accounts. |
|   | Release an instance | Release an instance and restore the resource inventory after you delete all databases under the instance. |
|   | Release protection | Enable release protection for an instance to prevent accidental deletion of production instances caused by misoperations or automated scripts, providing a final security safeguard for critical business data. |
|   | Instance version | Support MySQL 5.7 and 8.0. |
|   | Restart an instance | Restart an instance to quickly restore the instance status. |
|   | Upgrade the version | Smoothly upgrade the instance version and evaluate compatibility and performance between the old and new versions. |
|   | Upgrade or downgrade | Scale up or downgrade an existing instance. |

| Database management | Create a database | Create a distributed database to support tens of millions of concurrent connections and store petabytes of data. |
|---|---|---|
|   | Parameter settings | Configure parameters at the instance and database levels. |
|   | Security management | Configure the database access allowlist, three-role separation mode, and SSL encryption configuration. |
|   | Database management | Query the list of existing databases, character sets, and bound account information, and delete databases. |
|   | Data table management | View the table schema, sharding keys, table properties, and status. |
|   | Log in to the database | Log in to the database through Data Management Service (DMS) for O&M operations. |
|   | Account management | Provide a database account permission system that supports a standalone MySQL-compatible account and permission system to ensure secure account operations for different roles. |
| Data restoration | Backup policy settings | Configure the backup retention period in days, the backup interval with daily granularity, the backup time window with hourly granularity, and the backup mode (physical backup). |
|   | Backup progress query | Query the backup progress. |
|   | Backup set query | Query completed backup sets. |
|   | Data backup | Perform quick backup and consistent backup at the instance level, and support physical backup. |
|   | Data restoration | Restore a new instance from a backup set or a point in time. |
|   | Table recycle bin | Enable or disable the feature. The recycle bin retains dropped tables for 2 hours. You can restore tables from the recycle bin or permanently delete them. |

| Performance monitoring | View performance monitoring metrics | View performance monitoring metrics to track the running status of an instance and use fine-grained monitoring data to quickly locate O&M issues. |
|---|---|---|
| Cloud Monitor | View the monitoring dashboard | View Cloud Monitor metric information to quickly locate O&M issues. |
|   | Configure alert rules | Create alert rules to trigger alerts based on configured cloud service monitoring metric thresholds and send timely notifications to relevant users. |
|   | View alert history | After an alert occurs, view the alert history by cloud service, instance, and alert level. You can also export and download the alert history for local data analysis. |
| Integrated centralized and distributed architecture | Support centralized databases | Support 3-node centralized databases. |
|   | Switch from centralized to distributed architecture | Migrate data to a distributed architecture through Data Transmission Service (DTS). |
| Hardware support | Support Hygon | Support Hygon processors of generations 2, 3, and 4. |
|   | Support Kunpeng | Support Kunpeng chips. |
|   | Support Phytium chips | Support Phytium chips. |
|   | Support YiTian | Support YiTian chips. |
|   | Support mixed deployment of x86 instruction sets | Support mixed deployment within a cluster. |
|   | Support mixed deployment of ARM instruction sets | Support mixed deployment within a cluster. |
|   | Migration evaluation | The console allows you to create a migration task through a graphical interface to migrate data from PolarDB-X 1.0 to PolarDB-X 2.0. |

| psaraDB for POLARDB | Product Introduction·Feature |   |
|---|---|---|
| Instance migration |   |   |
|   | One-click migration | The console allows you to create a migration task through a graphical interface for the following scenarios: Migrate data from RDS MySQL to PolarDB-X 2.0. Migrate data from PolarDB-X 2.0 to PolarDB-X 2.0. |
| Security management | Enable SSL encryption | Enable SSL encryption for the instance. |
|   | Download the CA certificate | Download the CA certificate. |
|   | Update the validity period | Update the validity period of the SSL encryption. |
|   | Configure the IP allowlist | Configure an allowlist to enhance the security and stability of the database. |
|   | IP types and allowlist | Allocate IPv4 single-stack or IPv4/IPv6 dual-stack addresses to meet the requirements of different network environments. In dual-stack mode, configure an independent IPv6 allowlist to precisely control access permissions. |
|   | Parallel computing | Support distributed parallel computing to improve the efficiency of large-scale data processing. |
|   | Batch processing | Process data in batches to reduce network overhead and increase throughput. |
|   | Query cache | Cache query results to reduce the compute cost of repeated queries. |
|   | Data compression | Use advanced data compression algorithms to reduce storage capacity usage. |
|   | Stored procedure optimization | Optimize the execution path of stored procedures to reduce the running time. |
|   | Function call optimization | Improve the efficiency of built-in function calls and reduce function call overhead. |

|   | Index selection optimization | Automatically select the optimal Index strategy to improve query performance. |
|---|---|---|
|   | Statistics maintenance | Update statistics regularly to ensure that the query optimizer makes optimal decisions. |
|   | Data locality optimization | Use the data locality principle to reduce data access latency. |
|   | Data prefetch mechanism | Prefetch data to load potentially required chunks in advance and reduce wait time. |
| High-performance distributed kernel |   |   |
|   | Data partition policies | Support multiple data partition policies, such as range partition, list partition, and hash partition. |
|   | Data skew handling | Automatically detect and resolve data skew issues to ensure stable system operation. |
|   | Dynamic execution plan adjustment | Dynamically adjust the execution plan based on real-time load to adapt to different workloads. |
|   | Resource scheduling optimization | Optimize the resource scheduling slgorithm to improve resource utilization. |
|   | Concurrency control | Implement an efficient concurrency control mechanism to reduce lock conflicts. |
|   | Deadlock detection and recovery | Automatically detect and resolve deadlock issues to ensure normal system operation. |
|   | Transaction management | Provide comprehensive transaction management features to ensure data consistency. |
|   | Log management | Optimize the log management process to reduce log write overhead. |
|   | Cache consistency | Ensure cache consistency across multiple nodes to prevent dirty reads. |
|   | Data synchronization | Provide an efficient data synchronization mechanism to ensure data consistency. |

|   | Data replication | Support multiple data replication modes, such as synchronous replication and asynchronous replication. |
|---|---|---|
|   | Data sharding | Implement automated data sharding policies to improve data distribution uniformity. |
|   | Data migration | Provide convenient data migration tools to simplify the migration process. |
| PolarDB-X 2.0 intelligent assistant | Intelligent O&M assisted tool | Built on large language models and a distributed database expert knowledge base, the assistant integrates instance detail query, intelligent Q&A, and intelligent diagnostic capabilities. The PolarDB- X 2.0 intelligent assistant supports natural language interaction and deeply understands the distributed architecture of PolarDB-X. It performs root cause diagnosis for multi-node performance issues and provides optimization recommendations. |
