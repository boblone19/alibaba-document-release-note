---
title: "Alibaba Cloud Apsara Stack v3.18.6-2607 Data Management Product Introduction 20260831"
product_version: "V3.18.6_2607"
doc_version: "20260831"
pdf_pages: 20
source_pdf: "aea31fa2896d2e12_Alibaba Cloud Apsara Stack v3.18.6-2607 Data Management Product Introduction 20260831.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/3816%202607/pdf%203/%E6%95%B0%E6%8D%AE%E7%AE%A1%E7%90%86%20DMS/Alibaba%20Cloud%20Apsara%20Stack%20v3.18.6-2607%20Data%20Management%20Product%20Introduction%2020260831.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings)
---

# Alibaba Cloud Apsara Stack v3.18.6-2607 Data Management Product Introduction 20260831

## Table of Contents

- 1 What is DMS?
- 2 Features
- 3 Benefits
- 4 Scenarios
- 5 Features

S?

## 1 What is DMS?

Data Management (DMS) is a fully managed service that is provided by Apsara Stack. You can use this service to manage data, table schemas, R&D processes, R&D specifications, users, permissions, and access security.

**Supported databases**

Relational databases: MySQL: ApsaraDB RDS for MySQL, PolarDB-X, MySQL databases from other cloud service providers, and self-managed MySQL databases SQL Server: ApsaraDB RDS for SQL Server, SQL Server databases from other cloud service providers, and self-managed SQL Server databases PostgreSQL: ApsaraDB RDS for PostgreSQL, PostgreSQL databases from other cloud service providers, and self-managed PostgreSQL databases Self-managed Dameng (DM) databases Self-managed Oracle databases ApsaraDB for OceanBase and self-managed OceanBase databases NoSQL databases: Redis: ApsaraDB for Redis, Redis databases from other cloud service providers, and selfmanaged Redis databases MongoDB: ApsaraDB for MongoDB, MongoDB databases from other cloud service providers, and self-managed MongoDB databases Graph Database (GDB) Online analytical processing (OLAP) databases: AnalyticDB for MySQL AnalyticDB for PostgreSQL

**Note**

Self-managed databases are databases that are installed on Apsara Stack Elastic Compute Service (ECS) instances, instances from other cloud service providers, or servers in data centers.

**Features**

DMS provides support for the entire database development process. You can design table schemas in an on-premises environment based on the design specifications. Before you publish SQL statements to an online environment, DMS can review the add, remove, modify, and query operations in the statements. Then, you can publish schemas to the specified environment as needed. DMS provides fine-grained access control at the database, table, or field level. You can perform all operations on databases in the DMS console. The operations can be traced and audited. DMS allows you to configure operation specifications and approval processes for multiple modules based on your business requirements. These modules include the schema design, data change, data export, and permission application. DMS integrates database development with database interaction. You can manage databases without the need to switch between database endpoints at a high frequency by using database accounts and passwords. DMS provides the task orchestration feature that allows you to orchestrate and schedule SQL tasks for databases. You can use this feature to perform a variety of operations with ease. For example, you can use this feature to dump historical data or generate periodical S? reports.

## 2 Features

Data Management (DMS) provides seven features to cater to various scenarios. These features are: data asset management, SQL console, database development, data transmission service (DTS), security and compliance, solutions, and operations and maintenance (O&M) management.

**Data asset management**

Instance management: You can add, edit, and view the information of database instances that are added to DMS. You can also perform management operations on these instances, including permission management, enable or disable instances, and delete instances. Data classification: You can classify and manage instances, databases, and tables in a database instance. This helps administrators, developers, and O&M engineers manage data in tables. Sensitive data management: You can manage all medium and high sensitivity data centrally from DMS. This improves control over sensitive data within enterprises.

**SQL console**

Visual operation section: You can view all tables, fields, and indexes of the current database. You can also edit the schema of a table and import and export data from it. SQL execution section: You can write, format, and execute SQL statements. You can also modify or update result sets. Execution result section: You can view the execution results and execution history. Quick actions: You can perform quick actions such as obtaining a list of tables, metadata synchronization, export, table schema version management, operation auditing, risk auditing, and super SQL mode.

**Database development**

Change schemas Schema design: You can design table schemas for databases or tables. These table schemas conform to the predefined development specifications. You can customize development processes for different lines of business based on your business requirements to ensure the consistency of schemas among multiple environments, such as the development environment, test environment, and production environment. Schema synchronization: You can compare the schemas of different databases and generate scripts to ensure consistency across databases. This can be used to compare and synchronize table schemas across multiple database environments. Shadow table synchronization: This feature can automatically create a shadow table based on the schema of a source table. You can use this feature for end-to-end stress testing. Empty database initialization: You can use this feature to synchronize the schemas of a database to an empty database. This allows you to quickly initialize databases across regions and branches. Table consistency management: You can use this feature to compare a batch of tables with a base table, and generate and execute scripts to repair consistency issues between the tables. You can use this to ensure schema consistency between the two environments, or to compare table schemas between logical databases. Change data General data operations: You can use SQL statements such as INSERT, UPDATE, DELETE, and TRUNCATE for data initialization, historical data clearing, error fixing, and feature test. Historical data clearing: You can clear historical data periodically to prevent data accumulation from impacting the stability of the environment. Data import: You can quickly import a large amount of data to databases. This helps you save labor and resources. Lockless changes Lockless data change: You can use this feature to ensure execution performance and reduce the impact of the SQL statement on database performance or database storage. This feature is especially useful when you need to change a large amount of data. Lockless schema change: You can use this feature to change schemas without the need to lock tables. This prevents table locking and synchronization latency between primary and secondary databases. Data export SQL result set export: You can export the result set of an SQL query statement. Database export: You can export a database or individual table. You can also export only the schemas or table data of a database or individual table for data analysis. SQL review: This feature can review the submitted SQL statements and provide optimization suggestions. This feature checks whether your queries use indexes and conform to database development standards, helping you write efficient and secure queries and reducing the risk of SQL injection attacks. Database clone: You can use this feature to replicate and synchronize database data and initialize databases in multiple environments. Test data generation: You can use this feature to generate a large amount of test data, such as random values, region names, and virtual IP addresses. This helps you prepare test data with ease. DevOps: You can use this feature to customize development processes and manage the quality of these processes. This can help you effectively implement development processes, reduce accidental operations, protect data, and thus improve development efficiency.

**Data Transmission Service (DTS)**

Data transmission and migration Data migration: You can use this feature to migrate data between homogeneous and heterogeneous data sources. This is suitable for data migration to Alibaba Cloud, data migration between instances in Alibaba Cloud, and database partitioning and scaling. Change tracking: You can use this feature to track data changes from databases in real time. Then, you can consume the tracked data. You can use this feature in cache updates, business decoupling, synchronization of heterogeneous data, and synchronization of extract, transform, and load (ETL) operations. Data synchronization: You can use this feature to synchronize data between data sources in real time. This feature can be used for active geo-redundancy, geo-disaster recovery, zone-disaster recovery, cross-border data synchronization, query load balancing, cloud BI systems, and real-time data warehousing. Advanced Database & Application Migration (ADAM): A solution for smooth database migration. You can use ADAM to evaluate the feasibility and costs of database migration and obtain recommendations on databases. ADAM helps reduce the risks, technical difficulties, and turnaround time of migrating databases and applications. Data integration, development, and application Batch processing: This feature provides low-code data development tools to process complex big data in batches. This feature can be used for fine-grained enterprise operations, data-driven marketing, intelligent recommendation, and other big data scenarios. Stream processing: This feature provides real-time data processing tools that extract, transform, process, and load streaming data. This feature provides more options for realtime data processing and computing, which helps enterprises accelerate digital transformation. Task orchestration: This feature supports complex task orchestration and scheduling to improve the efficiency of data development. Data service: You can use this feature to expose data managed on DMS to other entities. This feature helps manage data security by controlling the scope of the exposed data to the required minimum. Data visualization: This feature can visualize data in the database in a variety of ways to help generate insights for decision-making.

**Security and compliance**

Permissions: You can manage the query, change, export, and logon permissions of instances, databases, tables, data columns, and rows. Security rules: DMS manages database rule sets in a fine-grained manner to create database operation specifications and development processes. Approval process: You can select and configure approval processes based on different user behaviors. Access IP whitelist: This feature allows you to effectively control the use of DMS so that only authorized employees in a trusted environment can access DMS. Operation audit: You can query the information about operations that are performed in DMS, including SQL statements that are used in the SQL console, tickets, logon information, and operation logs. This feature helps you troubleshoot database issues and provides data for operation audit. Sensitive data management: This feature helps you detect and identify sensitive data assets, and helps you protect these data assets from abuse.

**Solutions**

T+1 full data snapshot: This feature creates snapshots for individual tables every hour or day on a T+1 basis. This facilitates statistical analysis on a daily or monthly basis. For example, this feature can collect statistics and calculate the total amount of orders on the previous day to provide you up-to-date information about business operations.

**O&M management**

User management: You can add and delete DMS users, manage user permissions, and grant permissions on instances, databases, tables, rows, and sensitive columns. Task management: You can create SQL tasks and manage existing tasks. Configuration management: You can change the system configurations of DMS to suit the requirements of your business at any time. For example, you can enable automatic synchronization of instance resources. Database grouping: You can add multiple databases with the same environment or engine type to one group. You can use this feature to apply a data change or schema design to all of the databases in a database group with ease.

## 3 Benefits

DMS provides multiple benefits. These benefits include various data sources, secure and controllable procedures, and fine-grained access control. These benefits improve data security and simplify data management.

**Various data sources**

**Unified operations and comprehensive audits**

After you adds a database instance to DMS as an administrator, you can perform the required operations in the DMS console. These operations include querying databases, changing schemas, and changing data. You can query and audit all historical operations based on multiple dimensions. These dimensions include the operator, database, table, and time.

**Fine-grained access control**

Common users do not need to use database accounts and passwords. These users only need to request the query, export, or change permission on the destination database, table, or field in the DMS console based on their business requirements. After a permission expires, DMS revokes the permission.

**Custom approval processes**

You can create custom approval processes for the modules of each database instance. These approval processes are specific to your business requirements. This allows you to meet requirements from several aspects, such as efficiency and security. Example: Impose loose controls on a test environment. You can reduce stages or set no approval process. Impose strict controls on a production environment. You can specify an approval process that includes the required operations for the production environment. The production environment takes effect until all these operations are approved by the specified engineers in sequence.

**Custom design specifications for schemas**

You can create custom design specifications for MySQL table schemas. These design specifications include the field type, index type, number of indexes, field length, table size, and release process.

**Simple procedure to schedule and orchestrate periodical tasks**

DMS provides a quick method to create the required orchestration and recurring schedules for the SQL task nodes of various databases in a quick manner. You can use this feature to perform serval operations on databases to explore the value of data. These operations include transferring historical data and generating periodical reports.

## 4 Scenarios

Data Management (DMS) is ideal for implementing data security and improving development efficiency. It is typically used in scenarios such as cloud migration, disaster recovery, T +1 data warehouses, real-time data warehouses, and cross-instance queries.

**Data security and development efficiency**

You can use DMS to apply custom security rules, sensitive data identification rules, and masking rules. This helps improve the data security and reliability of your applications. You can also make use of scheduled tasks and data management windows to reduce the risk of issues that may arise due to human error. Pain points: High reliance on intra-person communication to perform O&M tasks and implement changes, leading to low efficiency within enterprises. Manual labor is unable to keep up with the O&M responsibilities of hundreds of instances, which include the detection and prevention of errors. This leads to challenges in maintaining business reliability. Benefits: You can use DMS to centrally manage a large number of instances, improving development efficiency. You can use DMS to build a data security protection system from scratch to ensure data security.

**T +1 data warehouse**

DMS allows you to create snapshots for individual tables every hour or day on a T+1 basis. This way, you can view the statistics on data by hour, day, or month. Pain points: Traditional T+1 data warehouses use complex operations to aggregate incremental data, which consumes a large amount of computing resources. This negatively affects the timeliness of the data. Incremental data is fetched in real time or at a scheduled time. This has a significant impact on business systems. Data slicing problems at a given time point. Benefits: History tables record the life cycle of incremental information in real time. DMS generates hourly and daily snapshots five times more efficient than traditional solutions. DTS does not make use of plug-ins or log parsing to fetch data. This reduces the resource overhead to a minimum, with little to no impact on the performance of business systems. Data can be sliced at any point-in-time.

**Cross-instance query**

DMS allows you to perform real-time join queries across online or heterogeneous data sources that are deployed in different environments. You can perform queries on MySQL databases, SQL Server databases, PostgreSQL databases, and Redis databases. Even when such database instances are deployed in different regions and environments, you can write a dynamic SQL statement to perform join queries on these databases. Benefits: Cross-database queries after vertical and horizontal partitioning: You can perform real-time join queries for common commodity databases and order databases across multiple regions and units. Join queries on heterogeneous databases: For example, after data is migrated from a SQL Server database to a MySQL database, you can perform join queries to verify the consistency between both databases. Join queries in hybrid clouds: You can perform join queries on databases across on-premise IDC and cloud environments.

## 5 Features

This article introduces the features of Alibaba Cloud Data Management (DMS), helping you quickly understand the product functionality.

| Feature category | Feature | Description |
|---|---|---|
| Data assets | Category management | Supports defining categories with up to four levels of depth as needed, for effectively managing database instances, databases, tables, and other assets by business dimension. |
|   | Data assets | Supports unified search of global assets, classification dashboard statistics, and other related functions. |
| Database backup | Cloud product backup capabilities | Supports PolarDB-X 1.0 (formerly DRDS) backup. For other capabilities, refer to ASR (Backup Management Platform). |
|   |   | Supports RDS backup files. For other capabilities, refer to ASR (Backup Management Platform). |
|   |   | Supports self-managed databases on ECS and on-premises databases backup. Supports self-managed MySQL database backup, full backup, incremental log backup, instance recovery, database and table recovery, and backup set download. |
|   |   | Supports Polar-X 1.0 (formerly DRDS) backup, full backup, instance recovery, database and table recovery, and backup set download. |
|   |   | Supports MongoDB backup, ReplicaSet topology, full backup, incremental log backup, instance recovery, database and table recovery, and backup set download. |
|   |   | Supports Redis backup, Standard Edition topology, full backup, incremental log backup, instance recovery, database and table recovery, and backup set download. |
|   | Backup dump capability | Supports dumping backup sets to external storage, including NAS storage, S3 storage, etc. |

| SQL Console | SQL window | Supports writing SQL commands with formatting and execution (provides intelligent SQL auto-completion). Supports editing and updating result sets (only for relational database data returned with primary keys or unique keys). Execution results displayed in table or JSON format (MongoDB), supporting single or multiple row copying, downloading, and generation of insert scripts. Supports viewing SQL history executed by the current Alibaba Cloud account in a specific database. |
|---|---|---|
|   | Code generator | Provides support for quickly generating code formats such as iBatis based on table structure. |
|   | Sharing | Supports sharing SQL Console with or without SQL scripts. Recipients can quickly access the corresponding SQL Console through the shared link to perform database queries and other related operations. |
|   | Command tab | Supports MySQL, Redis, and MongoDB. |
|   | Object information | You can view table structure definitions and table creation statements. |
|   | Export | Supports exporting table data, table structure, and table creation statements. |
|   | Schemas | Supports instances in flexible management control mode. |
|   | Open table | Supports quickly returning table data, with refresh capability to trigger a new query. |
|   | Batch operations | Supports MySQL-related database engines. |
|   | ActionTrail | Supports targeted auditing of SQL queries, tickets, logins, and other information for a single database, facilitating problem identification and resolution. |
|   | Data plans | Provides shortcuts for data plan-related function operations. |
|   | Table structure version management | Supports instances in flexible management control mode. |

|   | Super mode | Supports instances in security collaboration control mode. |
|---|---|---|
|   | Risk audit | Supports comprehensive risk identification for metadata, sensitive data, and SQL review, effectively improving database security and stability. |
| Instances | Non-locking schema changes | Manages the non-locking schema change switch for the current instance, which can be toggled. Only instances in security collaboration control mode are supported. Only MySQL and PolarDB-MySQL instance types are supported. |
|   | Delete an instance | Deletes an instance so it no longer appears in the list. This will clear related usage data in the product (including user authorization information). |
|   | Synchronize dictionary | After triggering, metadata information such as databases, tables, fields, and indexes will be collected from the database instance. Only instances in security collaboration control mode are supported. |
|   | Security rules | View security rules used by the current instance and switch between different security rules. |
|   | Instance DBA | View DBA information configured for the current instance and make changes if needed. |
|   | Instance logon | After logging in to an instance, you can view, edit, and use data and structures. |
|   | View details | View basic information configured when the instance was registered. |
|   | Test connectivity | Test the connection to the database using the configured connection information. The connection must be available to use subsequent functions in the product. |
|   | Control mode | View the control mode information used by the current instance and switch between different modes. |
|   | Modify an instance | Edit various registration information for the instance. |
|   | Cross-instance query | View cross-instance query information used by the current instance and disable it if needed. Only instances in security collaboration control mode are supported. |

| Schema design | Table synchronization | Provides various ticket types such as structure synchronization, empty database initialization, and table consistency repair. After submission, the ticket follows the verification rules, SQL execution, and approval process configured in "Security Rules" to achieve structure consistency synchronization between source and destination databases. Added "shadow table synchronization" to support periodic synchronization of source table structures to target tables, supporting typical scenarios such as end-to-end load testing. Supports MySQL, PolarDB-MySQL, and OceanBase. |
|---|---|---|
|   | Schema design | Provides table structure development management based on structure design specifications and development processes in "Security Rules." Changes are controlled according to "Security Rules" and can be scheduled for execution after approval. Supports MySQL, PolarDB-MySQL, and OceanBase. |
| Databases | Single database query | You can execute custom SQL statements in the SQL window and view execution results, limited to operations with current database table permissions. |
|   | Synchronize dictionary | After triggering, metadata information such as databases, tables, fields, and indexes will be collected from the database instance. Only instances in security collaboration control mode are supported. |
|   | Export | Supports exporting table structures, table creation statements, and data, limited to operations with current database table permissions. |
|   | Database cloning | Supports synchronizing source database (table) structure and data to target database (table). Currently only supports MySQL. |
|   | Test data generation | Provides the ability to automatically generate data according to various rules based on field types. Supports relational databases. |
|   | Manage owner | You can manage owner configuration information for the current database. Limited to administrators and DBAs. |
|   | Management permissions | You can manage user permission status for the current database, granting and revoking permissions. Limited to administrators, DBAs, and data owners. |
|   | Table details | You can view table structure definitions, including fields, indexes, and other related information. Limited to operations with current database table permissions. |
| 6 | > Document Version: 2026083 |   |

|   | Configure logical database | Supports configuring multiple sharded databases as a single logical database to simplify the management of database sharding. |
|---|---|---|
|   | DevOps | This feature allows you to define projects and iterations based on the R&D process of your enterprise. You can specify tickets that can be created in each iterative stage, and the types and statuses of the tickets that require to be checked in each iterative stage. This way, the enterprise can track the entire R&D process of its databases to ensure that all changes are made. |
|   | Next-day full data snapshot | Supports periodic data snapshots. |
|   | Workflow | Workflow supports file detection and assignment node functions. |
|   | Workflow | Supports DAG flowchart orchestration of SQL task nodes and DSQL task nodes for multiple database types. These can be configured as recurring scheduled tasks to implement data warehouse development, periodic report processing, historical data archiving, and other functions. Provides data integration, SQL task node deployment, dependency checking, and periodic scheduling management of task flow instances. Added data backfill and SQL code hinting functions. |
| Data plans |   |   |
|   | Data change | Provides various ticket types such as regular data changes, non- locking data changes, historical data cleanup, programmable object changes, and batch data import. After submission, the ticket follows the verification process for affected rows and syntax configured in "Security Rules" and can be executed after approval. |
|   | Data visualization | Supports defining commonly used analysis query results as charts, dashboards, and large screens for visualization. |
|   | Data export | Provides capabilities for exporting SQL result sets and quickly exporting database and table data. After submission, the ticket follows the verification process for affected rows and syntax configured in "Security Rules" and can be executed after approval. |

|   | Database clone | Supports synchronizing source database (table) structure and data to target database (table). |
|---|---|---|
|   | Data service | Supports defining database query operations as interfaces for data output. |
|   | Data integration | Supports stream and batch processing. |
|   | Test data generation | Provides the ability to automatically generate data according to various rules based on field types. |
| Permissions | Instance access privileges | Provides an entry point for instance login permission request management. After submitting the process, permissions are automatically granted after approval according to the process configured in "Security Rules." |
|   | My permissions | Provides an entry point for managing permissions of the current logged-in Alibaba Cloud account. You can reasonably release unnecessary permissions and apply in advance for permissions that are about to expire. |
|   | Permission requesting | Provides requests for instance login, database, table, sensitive column, data row, programmable object permissions, and instance, database, and table owner permissions. |
|   | Job management | Provides a unified view of all tasks that need asynchronous scheduling within the product. Supports creating, pausing, deleting, and retrying tasks. |
|   | Security rules | Unified management of all security rules within the enterprise: You can add and edit security rules (including adjustments to approval processes, specific control rules, and table structure design rules). |
|   | Instance management | Unified management of database instances: You can view, register, edit, authorize, revoke permissions, disable, enable, delete, and perform other management operations on instance information. Added Resource Access Management to ensure database instances and databases can only be used by authorized users. |
|   | Approval process | Unified management of all approval processes within the enterprise: You can adjust the order of approval nodes, add and remove approval nodes, and adjust the approvers corresponding to approval nodes. |

| System manageme nt |   |   |
|---|---|---|
|   | Sensitive data protection | Supports automatic discovery of sensitive data based on legal and regulatory templates and custom rules. Supports data masking using built-in masking algorithms with custom masking rules, and fine-grained permission control. |
|   | Sensitive data management | Provides unified management of all classified sensitive and confidential fields within the enterprise. Supports setting encryption algorithms for sensitive and confidential fields to enhance data masking capabilities. |
|   | User management | Provides functions for adding, modifying, disabling, enabling, authorizing, and revoking authorizations for Alibaba Cloud account users. |
|   | User management | Provides functions for adding, modifying, disabling, enabling, authorizing, and revoking authorizations for Alibaba Cloud account users. Added Resource Access Management to ensure personnel can only use authorized database table information. |
|   | Row-level access control | Provides row-level access control capabilities for data. |
|   | Configuration management | Provides unified management of global configurations such as full table scan threshold limits, and the number of rows and queries per user per day. |
| Tables | Object information | You can view table structure definitions and table creation statements. |
|   | Export table creation statements | Export table creation statements for table structures. |
|   | Export a schema | Export table structure information in Excel format. |
|   | Database cloning | Supports synchronizing source database (table) structure and data to target database (table). |
|   | Test data generation | Provides the ability to automatically generate data according to various rules based on field types. |
| Menu | Top menu | Supports customizing favorites for commonly used functions for convenient quick access. |

| Search | Top search | Supports global search for databases and tables to access related operations. You can quickly filter and locate using multiple advanced conditions such as database type, permissions, and objects. Supports saving frequently used search conditions for quick retrieval. |
|---|---|---|
| Tickets | Ticket details | All ticket types support sharing in two modes: specifying personnel or not specifying personnel. Shared recipients can quickly access ticket details to view complete ticket content and progress information. |
| Feature optimizatio n | SQL review | Supports automated compliance review of SQL, iBatis, and MyBatis files to prevent non-compliant SQL such as SQL injection and SQL without indexes from being published. |
