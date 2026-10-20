---
title: "MaxCompute Product Introduction 20260629"
product_version: "V3.18.6"
pdf_pages: 24
source_pdf: "eb1a8ef365a6cdf7_Alibaba Cloud Apsara Stack V3.18.6 MaxCompute Product Introduction 20260629.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/v3.18.6%E7%89%88%E6%9C%AC%E6%96%87%E6%A1%A3/%E5%A4%A7%E6%95%B0%E6%8D%AE%E8%AE%A1%E7%AE%97%E6%9C%8D%E5%8A%A1/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.6%20MaxCompute%20Product%20Introduction%2020260629.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes)
---

# MaxCompute Product Introduction 20260629

## Table of Contents

- 1 MaxCompute
  - 1.1 Features
  - 1.2 Product value
  - 1.3 Scenarios
  - 1.4 Features

## 1 MaxCompute

MaxCompute is a highly efficient, highly available, and low-cost **EB-level** computing service for big data. It is independently developed by Alibaba Cloud. This service is used within Alibaba Group to process exabytes of data each day. MaxCompute is a distributed system designed for big data processing. As one of the core services in the Alibaba Cloud computing solution, MaxCompute is used to store and compute structured data. MaxCompute is designed to support multiple tenants and provide features such as data security and horizontal scaling. It provides a centralized graphical user interface (GUI) and centralized APIs for various data processing tasks of different users based on an abstract job processing framework. MaxCompute is primarily used to store and compute batch structured data. It provides solutions for large-scale data warehouses, along with big data analytics and modeling services. The goal of MaxCompute is to simplify the process of analyzing large volumes of data. This lets you perform big data analysis without needing to understand the underlying details of distributed computing.

### 1.1 Features

MaxCompute is a data processing platform developed by Alibaba Group to process large amounts of data. MaxCompute provides channels for data uploads and downloads, a range of computing and analysis features including MaxCompute SQL and MaxCompute MapReduce, and comprehensive security solutions.

**Data tunnel**

Tunnel: provides highly-concurrent offline data upload and download services. MaxCompute Tunnel enables you to upload or download large amounts of data to or from MaxCompute. MaxCompute Tunnel provides a Java API. DataHub: provides real-time data uploads and downloads. Data uploaded by using DataHub is available immediately, whereas data uploaded by using MaxCompute Tunnel is not.

**Computing and analysis tasks**

SQL: MaxCompute stores data in tables and allows data queries by using SQL statements. MaxCompute can be used as traditional database software, and can process terabytes to petabytes of data. MaxCompute SQL does not support transactions, indexing, or operations such as UPDATE and DELETE. The SQL syntax that is used in MaxCompute is different from the SQL syntax that is used in Oracle and MySQL. SQL statements from other database engines cannot be seamlessly migrated to MaxCompute. MaxCompute SQL returns query results in minutes or seconds, not in milliseconds. MaxCompute SQL is easy to learn. You can get started with MaxCompute SQL based on your prior experience of database operations, without a deep knowledge of distributed computing. MapReduce: First proposed by Google, MapReduce is a distributed data processing model that has gained extensive attention and has been used in a wide range of business scenarios. You must have a basic knowledge of distributed computing and related programming experience before you use MapReduce. MapReduce provides a Java API. Graph: an iterative graph computing framework provided by MaxCompute. Graph computing jobs use graphs to build models. A graph is a collection of vertices and edges that have values. MaxCompute Graph performs iterations to edit graphs, enable graphs to evolve, and obtain analysis results. Unstructured data access and processing in integrated computing scenarios: MaxCompute SQL cannot directly process external data, such as unstructured data from Object Storage Service (OSS). Data must be imported to MaxCompute tables by using relevant tools before computation. The MaxCompute team introduces the unstructured data processing framework to the MaxCompute system architecture to handle this issue. MaxCompute allows you to create external tables to process data from the following data sources: Internal data sources: OSS, Tablestore, AnalyticDB for MySQL, ApsaraDB RDS, Apsara File Storage for HDFS, and Taobao Distributed Data Layer (TDDL) External data sources: open source Hadoop Distributed File System (HDFS), ApsaraDB for MongoDB, and ApsaraDB for HBase Unstructured data access and processing in MaxCompute: MaxCompute reads and writes volumes to store and process unstructured data, which otherwise must be stored in an external storage system.

**Spark on MaxCompute**

Spark on MaxCompute is a big data analysis engine that is developed by Alibaba Cloud and provides users with big data processing capabilities.

**SDK**

SDK is a toolkit that MaxCompute provides for developers.

**Security solution**

MaxCompute provides powerful security services to ensure user data security.

### 1.2 Product value

MaxCompute is designed for storing and computing batch structured data. It provides solutions for large-scale data warehouses and big data analysis and modeling services.

**Excellent big data cloud service and real data sharing platform**

**in China**

MaxCompute can be used for data warehousing, data mining, data analytics, and data sharing. Alibaba Group uses this centralized data processing platform in several of its own services, such as Aliloan, Data Cube, DMP (Alimama), and Yu'e Bao.

**Support for many clusters, users, and concurrent jobs**

A single cluster can scale to over 10,000 servers while maintaining 80% linear scalability. A single MaxCompute system supports more than 1 million servers across multiple clusters. However, linear scalability is slightly affected. The system also supports multi-data-center deployment within a zone. A single MaxCompute system can support over 10,000 users, 1,000 projects, and 100 departments across multiple tenants. A single MaxCompute system can support an average of over 1 million jobs submitted daily and more than 20,000 concurrent jobs.

**Big data computing at your fingertips**

You do not need to worry about storage limitations or long computing times as your data volume grows. MaxCompute automatically scales cluster storage and computing capabilities based on your data volume. This lets you focus on data analysis and mining to maximize the value of your data.

**Out-of-the-box service**

You do not need to worry about cluster creation, configuration, or operations and maintenance (O&M). You can upload data, analyze it, and obtain results in MaxCompute with just a few simple steps.

**Secure and reliable data storage**

MaxCompute uses multi-level data storage and access control mechanisms to protect user data against loss, leakage, or interception. These mechanisms include data replication, read and write request authentication, and application and system sandboxes.

**Reliable management nodes**

MaxCompute uses the multi-node cluster architecture. The management nodes of each component feature high availability. The faults that occur on O&M management nodes do not interrupt your services.

**Powerful fault tolerance**

Supports hard disk hot-swapping and automatic fault tolerance for server hard disk failures within the cluster.

**Comprehensive storage space management**

MaxCompute lets you query information about the storage capacity and usage of the distributed file system and supports data lifecycle management. You can store data in different locations based on their value or tags. For example, you can write temporary files to SSDs to accelerate I/O operations and improve cluster resource efficiency. MaxCompute also provides a self-optimizing Zstandard (zstd) compression algorithm that delivers an optimal compression ratio.

**Comprehensive data backup**

MaxCompute lets you perform full or incremental data backups and restore data from storage media. MaxCompute lets you back up data for clusters in different data centers. This supports cross-data-center backup requirements. You can use Apsara Bigdata Manager to visually manage the backup process. MaxCompute lets you back up and restore the metadata, files, and tables of key components.

**Secure and reliable access control**

MaxCompute lets you manage data access permissions. These permissions include logon, table creation, read and write, and whitelist-related permissions. You can manage administrative permissions, such as administrator classification, in the Apsara Uni-manager Management Console. You can centrally manage user permissions in the Apsara Uni-manager Management Console. You can view and manage the permission features of all system components. You can also hide permission management details from regular users and simplify permission management for administrators. This improves the usability of permission management.

**Multi-tenancy for multi-user collaboration**

MaxCompute lets you configure data access policies. This enables multiple data analysts in an organization to collaborate and makes data accessible only to users with the required permissions. This approach ensures data security and maximizes productivity.
**Isolation**: You can submit the tasks of multiple tenants (projects) to different queues for
parallel execution. Resources are isolated among tenants.
**Permission**: You can centrally manage different tenants and dynamically configure,
manage, and isolate their resources. You can also collect statistics on tenant resource usage and manage multi-level tenants.
**Scheduling**: MaxCompute supports multi-tenant scheduling across multiple clusters and
resource pools.

**Multi-region deployment**

Cross-domain computing pattern Allows you to specify compute clusters to use computing resources more efficiently. Data exchanges between clusters occur within MaxCompute, and data replication and synchronization between clusters are managed based on configured policies. This eliminates the need for cross-domain operations and significantly reduces data processing latency. Cell-based pattern MaxCompute frontend, control plane, and compute clusters can be independently deployed in a cell region and operate without dependency on a centralized control plane. These clusters support the independent execution and management of computing tasks within the cell region and provide region-level high availability. They are not affected by network disconnections from the central region.

**Multi-device support**

MaxCompute supports using CPUs, hard disks, memory, and network interface controllers (NICs) with different specifications in a single-component cluster to maximize compatibility with existing devices, provided that cluster performance is not affected.

### 1.3 Scenarios

MaxCompute is suitable for storage and computing in scenarios in which more than 100 GB of data is involved. MaxCompute can process up to exabytes of data and is widely used in Alibaba Group. MaxCompute is suitable for various big data processing scenarios, such as data warehousing and business intelligence (BI) analysis for large Internet enterprises, website log analysis, e-commerce transaction analysis, and exploration of user characteristics and interests.

**Cost-effectiveness and quick data migration to the cloud**

**Scenario**: A cloud platform for Internet big data application services is built to meet the
business requirements of an information service provider that focuses on the new energy industry.
**Results**: The entire business system is migrated to the cloud within three months. The cloud
platform reduces the data processing time to less than one third of the self-managed big data platform. Multiple security mechanisms help ensure the security of the cloud data.
**Customer benefits**:
**More focus on core business**: The entire business system is migrated to the cloud within
three months. This allows the enterprise to use various cloud resources to improve the business.
**Low investment and O&M costs**: Compared with a self-managed big data platform, the
cloud platform significantly helps reduce the costs of infrastructure construction, O&M personnel, and R&D.
**High security and stability** : The comprehensive service capabilities and stable
performance of Alibaba Cloud ensure data security on the cloud.

**Fine-grained business operation for millions of users based on**

**large amounts of data**

**Scenario**: A big data platform is built to meet the business requirements of a community-
oriented vertical e-commerce app that focuses on the manicure industry. The big data platform provides business monitoring, business analysis, fine-grained operation, and recommendation for the app.
**Results**: MaxCompute helps achieve fine-grained operation for millions of users. The cloud
platform helps the e-commerce app be more agile, intelligent, and insightful and quickly respond to the data and analytics requirements of new business.
**Customer benefits**:
**Improved business insights**: MaxCompute helps achieve fine-grained operation for
millions of users.
**Data-driven business**: The platform improves the business data analysis capability and
monitors business data in an effective manner to improve business efficiency.
**Quick response to business requirements**: The MaxCompute ecosystem can quickly
respond to the business requirements for data analysis.

**Precision marketing based on big data**

**Scenario**: A core big data precision marketing platform is built for an Internet enterprise that
focuses on precision marketing and advertising technologies and services.
**Results**: A core big data precision marketing platform is built. All log data is stored in
MaxCompute. Batch scheduling and analysis are performed by using DataWorks.
**Customer benefits**:
**Cost-effective analysis of large amounts of data**: Statistical analysis of large amounts
of data can reduce costs by half while equivalent business requirements are met. This helps reduce costs in an effective manner and helps startup enterprises grow rapidly.
**Real-time data query and analysis**: MaxCompute provides technical advantages for
enterprises, eliminates the technical bottleneck in processing and analysis of large amounts of data, and queries and analyzes data in real time. MaxCompute collects, analyzes, and stores more than 2 billion data records of visitor activities per day. MaxCompute can respond to data queries from a table that contains hundreds of millions of log entries within milliseconds based on business requirements.
**Easy use of Machine learning platform** : The performance of algorithm models directly
affects the revenue of the customer. The machine learning platform of MaxCompute is easy to use and is a good choice to meet the business requirements of the customer.

### 1.4 Features

This topic outlines the features of Alibaba Cloud MaxCompute.

| Category | Feature | Description |
|---|---|---|

|   | CopyTask | When you submit a COPY command on the MaxCompute client, the MaxCompute cluster directly connected to the client is called the local cluster. The other MaxCompute cluster is called the remote cluster. The local and remote clusters are logical concepts and can be the same cluster. CopyTask copies data between the local and remote clusters. The mechanism is as follows: CopyTask starts a distributed job in the local cluster, reads data from the local cluster, and then writes the data to the remote cluster through the remote cluster's Tunnel service. Data is read directly from the disk, not through the local Tunnel. Note Because the COPY command uses HTTP to transfer data, the Tunnel service must be configured on the remote cluster to receive or send data. |
|---|---|---|
|   | Isolation 2.0 | The isolation system (Isolation) of the internal environment has open Java permissions. It supports reading from and writing to the file system, accessing compliant networks, and using the Java Native Interface (JNI). The isolation system audits IP addresses. This system is used to start isolated runtime environments for MapReduce and Java user-defined functions (UDFs). |
|   | Logview | Logview is a tool to view and debug jobs after they are submitted to MaxCompute. Use Logview to see the following details for a job: the running status, the results, the details of the job, and the progress of each step. |
|   | MaxCompute Graph | MaxComputeGraph is a processing framework for iterative graph computing. Graph computing jobs are modeled using graphs. A graph consists of vertices and edges, and both vertices and edges have values. MaxComputeGraph supports the following graph editing operations: modify the value of a vertex or an edge, add or delete a vertex, and add or delete an edge. |
|   | MaxCompute Studio | MaxComputeStudio is a big data integrated development environment (IDE) tool provided by the Alibaba Cloud MaxCompute platform. It is a development plugin based on the popular IntelliJ IDEA IDE. Install it on a developer client to perform data development quickly and easily. |
|   | MaxCompute client (odpscmd) | Access MaxCompute projects and run commands using the MaxCompute client (odpscmd). |
|   | MMA 2.0 migration tool | MaxCompute Migration Assist (MMA) is a data migration tool from MaxCompute. It helps you quickly migrate historical data from Hive to MaxCompute. |

|   | PyODPS | PyODPS is the Python software development kit (SDK) for MaxCompute. It provides simple and convenient Python programming interfaces. PyODPS supports fast, flexible, and expressive data structures similar to Pandas. You can use the data processing features of Pandas through the DataFrame API provided by PyODPS. |
|---|---|---|
|   | Service mode | A service mode for providing computing resources where resources are pre-provisioned. Capabilities include the following: In-memory data transfer. Shuffled intermediate results are not written to disk, which avoids disk I/O overhead. Resident processes. This eliminates the time overhead of more than 10 seconds required for resource application. Additionally, the service primarily supports small and medium- sized queries in business scenarios. These include the following: The maximum runtime for a SQL job in the standard fuxijob pattern is 20 minutes. Queries that use a small amount of resources, such as fewer than 2,000 instances. |
|   | StreamingTu nnel | StreamingTunnel is a channel for writing data in streaming mode. It supports Flink, DataHub, Data Transmission Service (DTS), real- time data synchronization, and Kafka. |
|   | Tunnel | Tunnel is a batch data channel. Supported tools include the MaxCompute client, DataWorks, DTS, Sqoop, Kettle plugins, and the MMA migration tool. |
|   | Tasks and management | A task is the basic computing unit in MaxCompute. SQL and MapReduce features are completed through tasks. For most tasks you submit, especially computing tasks such as SQL DML statements and MapReduce, MaxCompute parses them to get an execution plan. An execution plan consists of multiple dependent execution stages. In MaxCompute, SQL, Spark, and MapReduce tasks are instantiated as MaxCompute instances when they run. An instance goes through two stages: Running and Terminated. |
|   | Hierarchical throttling | MaxCompute has global throttling measures at the platform level. The hierarchical throttling feature allows business or team administrators (ProjectOwners) to manage the resource usage of their teams. It currently supports limiting the number of instances and allows team administrators to configure throttling rules. It provides user-based job throttling. Team administrators can set concurrent job submission limits at the user level based on the resource allocation needs of the business or team. |

| Other basic features of MaxCompute |   |   |
|---|---|---|
|   | Basic security management capabilities | The security management system includes user management, role management, ACL authorization, Package authorization, Label authorization, setting up a data outflow protection mechanism (ProjectProtection), enabling LabelSecurity (column-level security control), setting labels for fields, setting IP whitelists for project access, prohibiting the download of SELECT results from DataWorks to a local machine, and improving the security management level through other Alibaba Cloud services. |
|   | Control cluster machine concurrency adjustment | Supports setting task priorities within a project and default task priorities for a project. Supports restarting failed tasks. Supports speculative execution for tasks. Supports fair scheduling and first-in, first-out (FIFO) task scheduling methods. Supports resource preemption within a Quota group. Supports file number and storage capacity quotas based on projects. Supports CPU and memory quota configuration for resource groups. You can configure a resource group to specify the minimum amount of vCPU or memory that can be used when resources are scarce. You can also specify the maximum amount of vCPU or memory that will be occupied based on actual conditions. |
|   | New Logview 2.0 | Logview 2.0 is built on Logview with a completely new page design, optimized loading speed, and the following new features: Supports displaying the job processing logic architecture with an interactive directed acyclic graph (DAG). You can also view the corresponding Operation level. Supports replaying the job running process. Supports viewing memory and CPU usage through FuxiSensor. |
|   | Hardware decoupling output | The cloud base is not tied to specific network or server hardware. It can be deployed together with the base software and Platform as a Service (PaaS) platform software, such as MaxCompute and other computing platform products, to the user's network environment and self-provided servers that meet the hardware evaluation deviation range. |
|   | Roles | After a MaxCompute project is created, in addition to the project owner (ProjectOwner), two built-in management roles have all permissions on the project: Super Administrator and _ AdminProjectOwner. Super Administrator role: A built-in management role that has _ permissions to operate all types of resources within the project and management permissions. Admin role: A built-in management role that has permissions to operate all types of resources within the project and some basic management permissions. Users can also customize roles and grant permissions. |

|   | Account system | Supports two account systems: Alibaba Cloud accounts and Resource Access Management (RAM) users. For RAM users, only the account system is recognized, not the RAM permission system. This means you can add any RAM user owned by the root account to a MaxCompute project. However, when MaxCompute authenticates the RAM user, it does not consider the permission definitions in RAM. |
|---|---|---|
|   | Resource system | MaxCompute provides storage and computing resources to offer big data computing services. It provides customers with resource- isolated resource groups for project use, measured in CUs and storage space. |
|   | Project system | A project is the basic organizational unit of MaxCompute. It is similar to the concept of a Database or Schema in a traditional database and is the main boundary for multi-user isolation and access control. A project contains multiple objects, such as tables, resources, functions, and instances. |
|   | Job settings | Supports job priority settings with nine priority levels for fine- grained control over job task resource allocation priority. |
|   | Ultra-large scale | Uses a distributed computing framework to provide large-scale data storage and computing, which can be scaled out as needed. The big data computing platform can support over 30,000 nodes in a single cluster and has been assessed by authoritative institutions. |
|   |   | A service instance can support at least 50,000 user projects. |
|   |   | A single cluster can support at least 380 PB of data in a single project, and a single project can support at least 40,000 tables. |
|   |   | A single table can support at least 1 PB of data and over 60,000 partitions. It can support multi-table association analysis on a single table with up to one trillion records. |
|   |   | Supports ultra-large-scale MapReduce computing, with a maximum of 100,000 Mappers, 4,000 Reducers, and 10,000 Joins. |
|   | High stability | The big data platform has passed stability tests by third-party assessment organizations, supporting destructive tests in different dimensions. The distributed batch processing capability has passed stability tests, ensuring functional continuity and platform stability under fault disturbances such as high CPU load, high memory load, high read/write load, and network jitter. |

|   | High availability | Multi-zone disaster recovery Supports X86+X86 architecture and mixed-deployment disaster recovery for Intel-Hygon architecture within a cluster. Multi-zone disaster recovery within a single region Supports Intel-Intel multi-zone disaster recovery within a single region. Cross-cloud geo-disaster recovery Supports Intel-Intel, Hygon-Hygon, Kunpeng-Kunpeng, and Phytium-Phytium cross-cloud geo-disaster recovery. Cross-region geo-disaster recovery Supports Intel-Intel, Hygon-Hygon, Kunpeng-Kunpeng, and Phytium-Phytium cross-region disaster recovery. |
|---|---|---|
|   | Chip compatibility | Supports multi-chip mixed deployment between compute clusters, including Intel, Hygon, Kunpeng, and Phytium. |
|   | Multi-version management and recovery | Supports multi-version recovery management for table-level data. |
|   | Operations management | Supports GUI-based parameter configuration management. |
|   | CLONETABLE | When you need to copy data from one table to another, use the CLONE TABLE feature of MaxCompute to improve data migration efficiency. |
|   | COMMON TABLE EXPRESSION (CTE) | A common table expression (CTE) is a temporary named result set used to simplify SQL. MaxCompute supports standard SQL CTEs to improve the readability and execution efficiency of SQL statements. |
|   | EXPLAIN | The EXPLAIN statement displays the structure of the execution plan for a MaxCompute SQL DML statement. This helps you understand the processing of the SQL statement and provides guidance for optimization. |
|   | GROUPING SETS | GROUPING SETS is an extension of the GROUP BY clause in a SELECT statement. It lets you group results in multiple ways without using multiple SELECT statements combined with UNION ALL. This allows the MaxCompute engine to produce a more efficient execution plan, which improves performance. |
|   | HAVING clause | The WHERE keyword in MaxCompute SQL cannot be used with aggregate functions. In this case, use the HAVING clause. |

|   | Java UDF | After the upgrade to MaxCompute 2.0, the data types supported by Java UDFs were expanded from BIGINT, STRING, DOUBLE, and BOOLEAN to include more new data types. Support was also added for complex types such as ARRAY, MAP, STRUCT, and Writable. MaxCompute Java UDFs include UDFs, user-defined aggregate functions (UDAFs), and user-defined table-valued functions (UDTFs). |
|---|---|---|
|   | Join | MaxCompute supports the following Join operations: Left outer join ( LEFT OUTER JOIN ): Can be shortened to LEFT JOIN . Returns all records from the left table, even if there are no matching records in the right table. Right outer join ( RIGHT OUTER JOIN ): Can be shortened to RIGHT JOIN . Returns all records from the right table, even if there are no matching records in the left table. Full outer join ( FULL OUTER JOIN ): Can be shortened to FULL JOIN . Returns all records from both the left and right tables. Inner join ( INNER JOIN ): The INNER keyword can be omitted. INNER JOIN returns rows when there is at least one match in both tables. Natural join ( NATURAL JOIN ): The join fields for the two tables in the JOIN are automatically determined based on the field names. OUTER NATURAL JOIN is supported. You can use the USING clause to perform a JOIN . Common fields appear only once in the output. Implicit join: A join performed without specifying the JOIN keyword. Multi-way join: A multi-way JOIN . You can use parentheses to specify the priority of a JOIN . A JOIN in parentheses has a higher priority. |
|   | Lateral View (pivot) | Using a UDTF directly in a SELECT statement has limitations. To solve this, you can use MaxCompute's Lateral View with a UDTF to split one row of data into multiple rows (pivot) and then aggregate the split data. |
|   | LOAD | To import data from an external storage into a MaxCompute table or partition, use the LOAD command. |
|   | MAPJOINHINT | When you perform a join operation on a large table and one or more small tables, you can explicitly specify a mapjoin hint in the select statement to improve query performance. |

|   | INNER JOIN |
|---|---|
| INNER JOIN |   |

| NATURAL JOIN |   |
|---|---|
| JOIN |   |

|   | JOIN |
|---|---|
| JOIN |   |

|   | MaxCompute SQLML | The MaxCompute SQLML feature depends on MaxCompute and the Alibaba Cloud product Platform for AI (PAI). You can use a client to develop MaxCompute SQLML jobs, train on data in MaxCompute using PAI, and use machine learning models to make predictions. This can provide guidance for business planning. |
|---|---|---|
|   | MaxCompute UDJ | MaxCompute introduces a new extension mechanism in the UDF framework called user defined join (UDJ). UDJ allows flexible custom operations across multiple tables and reduces the need to handle low-level details of the distributed system through methods such as MapReduce. |
|   | MaxCompute UDT | MaxCompute introduces a new feature based on its next- generation SQL engine called User-Defined Type (UDT). The UDT feature in MaxCompute lets you directly call classes from third- party languages in SQL to use their methods, or directly use third- party objects to get their data content. |
|   | MERGE INTO | MaxCompute supports delete and update features. However, when you need to perform batch operations on a target table using multiple insert , update , and delete statements, you must write multiple SQL statements and perform multiple full table scans. The merge into feature provided by MaxCompute requires only one full table scan to complete all operations. Its execution efficiency is higher than that of separate insert , update , and delete operations. The merge into operation is atomic. A job is considered successful only when all insert , update , and delete operations within the job succeed. If any internal logic fails, the entire job fails. In addition, merge into helps you avoid the problem where some operations succeed and some fail when executing insert , update , and delete operations separately. In such cases, the successful operations cannot be rolled back. |
|   | Python UDFs | MaxCompute Python 2 or Python 3 UDFs include UDFs, UDAFs, and UDTFs. MaxCompute Python UDFs support third-party libraries. |
|   | SELECT TRANSFORM | The SELECT TRANSFORM syntax lets you start a specified child process, pass input data to the child process through standard input in a specific format, and get output data by parsing the standard output of the child process. SELECT TRANSFORM allows MaxCompute SQL to support other scripting languages without you having to write UDFs. |

| Basic features of MaxCompute SQL |   |   |
|---|---|---|
|   | SELECT syntax | Supports column expressions (select expr), target table _ information (table reference), WHERE clause (where condition), _ _ GROUP BY clause (col list), HAVING clause (having condition), _ _ ORDER BY for global sorting (order condition), DISTRIBUTE BY for _ hash sharding (distribute condition), SORT BY for local sorting _ (sort condition), and LIMIT to restrict the number of output rows _ (number). |
|   | SEMI JOIN (half join) | MaxCompute supports semi-join operations. It filters data from the left table using the right table, so that data from the right table does not appear in the result set. This can improve query performance. |
|   | SKEWJOIN HINT | When a join between two tables has a hot spot that causes a long- tail problem, you can improve join efficiency by extracting the hot spot key, processing the data as two parts (hot spot data and non- hot spot data), and then merging the results. SkewJoinHint can automatically or manually get the hot spot keys of the two tables, calculate the join results for hot spot and non-hot spot data separately, and merge them to speed up the join execution. |
|   | SQL Function | SQL-defined functions, as a type of user-defined function, compensate for MaxCompute's limitation of creating UDFs only with Java or Python. They also extend function-type parameters and anonymous function features, increasing the flexibility of expressing business logic. You can use these functions to implement simple features and improve code reuse. You can use and call SQL-defined UDFs in SQL scripts. Function-type parameters are supported, allowing you to pass built-in functions, UDFs, or SQL-defined functions during calls. Function-type parameters can be anonymous functions, allowing you to pass an anonymous function during a call. |
|   | UNLOAD | MaxCompute lets you export data from MaxCompute projects to OSS. This makes it convenient to store structured data in OSS and for other compute engines to use the data exported to OSS. |
|   | VALUES expression | To insert a small amount of data into a table, you can use the insert…values or values table operation to insert data into a small table. This means using a values expression as a table with data. |
|   | Intersection, union, and complement | Supports intersection (intersect, intersect all, intersect distinct), union (union, union all, union distinct), and complement (except, except all, except distinct, minus, minus all, minus distinct) operations. |

|   | Code- embedded UDFs | Code-embedded UDFs support embedding Java or Python code into SQL scripts. The Janino-compiler identifies and extracts the embedded code, compiles the code (Java), and dynamically generates resources and creates temporary functions. Code- embedded UDFs let you put SQL scripts and third-party code in the same source file, reducing the steps for using UDTs or UDFs and simplifying daily development. |
|---|---|---|
|   | Optimizer information collection | The MaxCompute optimizer is a cost-based optimizer. It needs to accurately estimate costs based on data characteristics (metadata), such as the number of rows and average string length. If accurate metadata is not available, the optimizer may misjudge the cost and generate a poor execution plan. Therefore, metadata is crucial for the optimizer. A table's metadata is primarily obtained by collecting statistics (ColumnStats) on its data. This metadata is the basis for inferring other metadata. MaxCompute provides the following two collection methods: Asynchronous collection framework (Analyze): You can asynchronously collect statistics using the analyze command. This requires you to initiate the collection. Synchronous collection framework (Freeride): ColumnStats are automatically collected as data is generated. This is more automated but affects query latency. |
|   | Other functions | MaxCompute SQL provides other common functions for development. You can select the appropriate functions as needed. |
|   | Partitions and columns | Supports adding partitions, deleting partitions, adding columns or comments, modifying column names, modifying column comments, modifying column names and comments simultaneously, modifying the update time of a partition, modifying the non-null property of a table column, modifying partition values, and merging partitions. |
|   | Dynamic filters | Supports dynamic range filters or bloom filters (DynamicRange\|BloomFilter) and dynamic partition pruning. |
|   | Parameterize d views | Traditional views do not accept any parameters from the caller, such as filtering data from the underlying tables or passing other parameters. This results in low code reusability. The current MaxCompute SQL engine supports parameterized views, which allow you to pass any table or other variables to customize the view's behavior. |
|   | Geospatial UDFs | MaxCompute natively supports the direct use of Hive UDFs, so it also supports using Hive geospatial functions in MaxCompute. |
|   | Complex type functions | You can use complex type functions in MaxCompute SQL to process complex data types, such as ARRAY, MAP, STRUCT, and JSON. |

|   | Multi-way output (MULTI INSERT) | When processing data with MaxCompute SQL, the multi-insert operation can insert data into different target tables or partitions, achieving multi-way output. |
|---|---|---|
|   | Subqueries | Supports IN/NOT IN SUBQUERY, EXISTS/NOT EXISTS SUBQUERY, and SCALAR SUBQUERY. Subqueries support multiple columns. |
|   | String functions | You can use string functions in MaxCompute SQL to flexibly process specified strings. |
|   | Insert or overwrite dynamic partition data (DYNAMIC PARTITION) | When processing data with MaxCompute SQL, the insert into or insert overwrite statement does not directly specify partition values, but only the partition column names (partition fields). The values for the partition columns are provided in the SELECT clause, and the system automatically inserts the data into the corresponding partitions based on these values. |
|   | Insert or overwrite data (INSERT INTO\|INSERT OVERWRITE) | When processing data with MaxCompute SQL, the insert into or insert overwrite operation can save the results of a SELECT query to a target table. |
|   | Mathematical functions | MaxCompute SQL provides common mathematical functions for use during development. You can select the appropriate mathematical functions for data calculation and data transformation operations as needed. |
|   | Date functions | MaxCompute SQL provides common date functions. You can select the appropriate date functions to perform date calculations and conversions as needed. |
|   | Update or delete data (UPDATE\|DEL ETE) | The delete and update features in MaxCompute provide the ability to delete or update specified rows in a table, similar to their usage in traditional databases. The update statement supports a `from` syntax that is fully compatible with Snowflake at the syntax level. This makes it convenient for users to write SQL to ensure that the update data source is unique and that only the joined data is updated. |
|   | Materialized views | Supports creating materialized views, querying materialized view information, querying materialized view status, updating materialized views, deleting materialized views, and performing query rewrite operations based on materialized views. |
|   | Window functions | You can use window functions in MaxCompute SQL to flexibly analyze and process data in specified window columns. |

|   | Aggregate functions | Aggregate functions have a many-to-one relationship between input and output. They aggregate multiple input records into a single output value and can be used with the `groupby` statement in MaxCompute SQL. |
|---|---|---|
|   | Run SQL in script mode | When compiling a script in script mode, a multi-statement SQL script file is compiled as a whole, without needing to compile individual statements. When submitted for execution, the entire SQL script file is submitted, and a single execution plan is generated. This ensures that it is queued only once and executed only once, allowing you to make full use of MaxCompute resources. |
|   | Tables | Supports creating tables, changing table owners, modifying table comments, modifying table modification times, modifying table clustering properties, renaming tables, clearing data from non- partitioned tables, deleting tables, viewing table or view information, viewing table creation statements, listing tables and views in a project, and listing all partitions. |
|   | Table and partition lifecycle | Supports creating a table lifecycle, modifying a table lifecycle, and disabling or restoring a lifecycle. Lifecycle rules can only be set at the table level, not at the partition level. When a lifecycle is set for a partitioned table, it also takes effect at the partition level. For a partitioned table, you can disable the lifecycle feature for a specific partition. You cannot cancel the lifecycle for a non- partitioned table, you can only modify it. |
|   | Views | Supports creating or updating views, renaming views, viewing views, and deleting views. |
|   | JSON data type | MaxCompute has added a JSON data type. When you insert JSON data, MaxCompute automatically optimizes it. It uses column store to increase the compression ratio of JSON data and improve query analysis performance. |
| Large-scale cross-domain software enhancement package | Cross-domain multi-region deployment architecture | Provides multi-region deployment and cross-domain computing capabilities. Supports large-scale (over 500 servers) cross-cluster queries, cross-domain data replication, incremental replication, cross-cluster scheduling, and cross-domain management in multi- region scenarios. |
|   | Storage encryption | MaxCompute supports data encryption at rest using Key Management Service (KMS). This provides static data protection to meet enterprise regulatory and security compliance requirements. MaxCompute encrypts or decrypts data stored in MaxCompute on a per-project basis using KMS. Storage encryption is transparent to the business. MaxCompute supports the AES256, AESCTR, RC4, and SM4 Chinese cryptographic algorithms. MaxCompute supports encrypting or decrypting data using the default key (DataworksDefaultKey) and Bring-Your-Own-Key (BYOK). |

| Security enhancement package | Permission model 2.0 | Based on the fine-grained access control of permission model 2.0, MaxCompute has enhanced its user and role authentication and permission management features. This includes finer-grained capabilities such as tenant security isolation, ACL, policy authorization, IP whitelists, project protection, download permission control, cross-project resource sharing with package authorization, and column-level label-based access control. |
|---|---|---|
|   | Sandbox protection | When MaxCompute MapReduce and UDF programs run in a distributed environment, they are restricted by the Java sandbox. The main program of a MapReduce job is not subject to this restriction. The specific restrictions are as follows: Direct access to local files is not allowed. Files can only be accessed indirectly through the interfaces provided by MaxCompute MapReduce and Graph. This includes: Resources specified by the Resources option, including files, JAR packages, and resource tables. Log information output through System.out and System.err. You can view log information using the Log command on the MaxCompute client. Direct access to the distributed file system is not allowed. You can only access table records through MaxCompute MapReduce and Graph. JNI calls are not allowed. Creating Java threads and starting child processes to execute Linux commands are not allowed. Network access, including getting the local IP address, is not allowed. Java reflection restriction: The suppressAccessChecks permission is prohibited. You cannot use setAccessible on a private property or method to read private properties or call private methods. |
|   | 1.0 data types | BIGINT: A 64-bit signed integer. Value range: -263+1 to 263-1. Constant examples: 100000000000L, -1L. DOUBLE: A 64-bit binary floating-point number. Constant example: 3.14159261E+7. DECIMAL: A 10-base precise numeric type. The integer part ranges from -1036+1 to 1036-1. The fractional part is accurate to 10-18. Constant examples: 3.5BD, 99999999999.9999999BD. STRING: A string type. The length is limited to 8 MB. Constant examples: "abc", 'bcd', "alibaba", 'inc'. DATETIME: A date and time type. Value range: January 1, 0000 to December 31, 9999. Constant example: DATETIME'2017-11- 11 00:00:00'. BOOLEAN: A BOOLEAN type. Value range: True or False. Constant examples: True, False. |

|   | 2.0 data types | TINYINT: An 8-bit signed integer. Value range: -128 to 127. Constant examples: 1Y, -127Y. SMALLINT: A 16-bit signed integer. Value range: -32768 to 32767. Constant examples: 32767S, -100S. INT: A 32-bit signed integer. Value range: -231 to 231-1. Constant examples: 1000, -15645787. BIGINT: A 64-bit signed integer. Value range: -263+1 to 263-1. Constant examples: 100000000000L, -1L. BINARY: A binary data type. The current length is limited to 8 MB. Constant examples: unhex('FA34E10293CB42848573A4E39937F479'), X'616263'. FLOAT: A 32-bit binary floating-point number. Constant examples: 3.14F, cast(3.14159261E+7 as float). DOUBLE: A 64-bit binary floating-point number. Constant examples: 3.14D, 3.14159261E+7. DECIMAL(precision, scale): A 10-base precise numeric type. Constant examples: 3.5BD, 99999999999.9999999BD. precision: The maximum number of digits that can be represented. Value range: 1 <= precision <= 38. scale: The number of digits in the fractional part. Value range: 0 <= scale <= 18. If you do not specify these two parameters, the default is decimal(38, 18). VARCHAR(n): A variable-length character type, where n is the length. Value range: 1 to 65535. CHAR(n): A fixed-length character type, where n is the length. The maximum value is 255. If the length is less than n, it is padded with spaces, but the spaces are not used in comparisons. STRING: A string type. The current length is limited to 8 MB. Constant examples: "abc", 'bcd', "alibaba", 'inc'. DATE: A date type in the yyyy-mm-dd format. Value range: 0001-01-01 to 9999-12-31. Constant example: DATE'2017-11- 11'. DATETIME: A date and time type. Value range: 0001-01-01 00:00:00.000 to 9999-12-31 23:59:59.999, accurate to the millisecond. Constant example: DATETIME'2017-11-11 00:00:00'. TIMESTAMP: A time zone-independent timestamp type. Value range: 0001-01-01 00:00:00.000000000 to 9999-12-31 23:59:59.999999999, accurate to the nanosecond. Constant example: TIMESTAMP'2017-11-11 00:00:00.123456789'. BOOLEAN: A BOOLEAN type. Value range: True, False. Constant examples: True, False. Other complex types include ARRAY, MAP, and STRUCT. |
|---|---|---|
| Data types |   |   |
|   | Hive- compatible data types | The data types are the same as the 2.0 data types, but there are differences in INSERT statement conversion rules and function behavior compared to other data type versions. They are closer to Hive's behavior and are suitable for Hive-compatible scenarios. |

| Intelligent metadata software enhancement package | InformationS chema | MaxCompute's InformationSchema provides project metadata and usage history data. It adds fields and views specific to the MaxCompute service to the ANSI SQL-92 InformationSchema. MaxCompute provides a public project named InformationSchema. By accessing the read-only views provided by this public project, you can query the metadata and usage history information of your project. |
|---|---|---|
|   | Metadata management | The intelligent metadata warehouse provides metadata for MaxCompute tables, partitions, projects, tasks, data, and permissions. It provides an access interface for metadata applications and an audit function for the metadata warehouse. This is a required enhancement package. Cross-tenant authorization uses the Package+view method. |
| Federated computing enhancement package | Spark on MaxCompute | Spark on MaxCompute is a computing service provided by MaxCompute that is compatible with open source Spark. It is built on a unified computing resource and dataset permission system. Based on the Spark computing framework, it supports submitting and running Spark jobs using familiar development methods to meet richer data processing and analysis needs. Spark on MaxCompute supports open source Spark 2.3.0 and 2.4.5. |
|   | Volume | MaxCompute's distributed file system is suitable for storing small- scale user data, including configuration files and simple databases. Resources or data used in UDFs can be stored in a volume, but you must be aware of the small file problem and that volumes do not support compression. For large-scale data, store it in OSS. |
|   | Foreign tables | MaxCompute supports OSS foreign tables, including the following: Accessing OSS with a built-in Extractor, accessing OSS with a custom Extractor, supporting open source format data, supporting compressed format data, data partitioning for OSS foreign tables, and outputting data to OSS. It also supports OTS foreign tables, Hologres foreign tables, RDS foreign tables, and HBase foreign tables. Supports various open source data formats through STORED AS semantics, including PARQUET, ORC, SEQUENCEFILE, TEXTFILE, and AVRO. |
|   | Product openness | For provisioning and job development scheduling, MaxCompute is not only adapted for Alibaba Cloud products like DataWorks, but also for open source management tools like DBeaver and Airflow. |

|   | n·MaxComput |   |
|---|---|---|
|   |   | In commercial applications, MaxCompute officially integrates with business intelligence (BI) analysis platforms such as Tableau, FineBI, Quick BI, Superset, NetEase BI, and Guanyuan BI. |
