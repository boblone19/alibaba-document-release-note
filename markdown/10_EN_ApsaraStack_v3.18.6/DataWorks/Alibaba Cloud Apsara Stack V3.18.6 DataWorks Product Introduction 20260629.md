---
title: "DataWorks Product Introduction 20260629"
product_version: "V3.18.6"
pdf_pages: 36
source_pdf: "cb2e2843090ff29a_Alibaba Cloud Apsara Stack V3.18.6 DataWorks Product Introduction 20260629.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/v3.18.6%E7%89%88%E6%9C%AC%E6%96%87%E6%A1%A3/DataWorks/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.6%20DataWorks%20Product%20Introduction%2020260629.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes)
---

# DataWorks Product Introduction 20260629

## Table of Contents

- 1 DataWorks
  - 1.1 What is DataWorks?
  - 1.2 Benefits
  - 1.3 Scenarios
  - 1.4 Features
    - 1.4.1 Data integration
    - 1.4.2 DataStudio
    - 1.4.3 Operation Center
    - 1.4.4 Data Map
    - 1.4.5 Data quality
    - 1.4.6 Security center
    - 1.4.7 Data Protection Umbrella
    - 1.4.8 Data Governance Center
    - 1.4.9 Data assets
    - 1.4.10 Data analysis
    - 1.4.11 DataService Studio
    - 1.4.12 Approval Center
    - 1.4.13 Migration Assistant
    - 1.4.14 Open Platform
    - 1.4.15 Workspace Management
    - 1.4.16 Tenant Management
    - 1.4.17 DataWorks Copilot
    - 1.4.18 Internationalization

## 1 DataWorks

DataWorks is an end-to-end big data development and governance platform that provides data warehousing, data lake, and data lakehouse solutions based on big data compute engines, such as MaxCompute, Hologres, and AnalyticDB. Since 2009, DataWorks has been summarizing and improving the big data development methodology of Alibaba Group to support data mid-end building. DataWorks collaborates with public service sectors, stateowned enterprises, customers in various industries, such as finance, retail, Internet, energy, and manufacturing, and the industrial sector to improve data application efficiency and facilitate the digital transformation of industries.

### 1.1 What is DataWorks?

DataWorks has developed and accumulated hundreds of core capabilities for more than ten years. DataWorks provides data integration, data development, data governance, data security, and data analysis services. These services provide end-to-end data governance capabilities to help enterprises reduce data processing costs, increase data value, and unleash data productivity.

**Data Integration**

DataWorks Data Integration is a stable, efficient, and scalable data synchronization service. It can be used to migrate and synchronize data among a wide range of heterogeneous data sources that reside in complex network environments in a fast and stable manner. Data Integration supports batch synchronization, real-time synchronization, and full or incremental synchronization that combines batch and real-time synchronization. Data Integration supports the following features: You can configure a scheduling cycle for a batch synchronization node. You can synchronize data among nearly 50 types of heterogeneous data sources, such as relational databases, data warehouses, NoSQL databases, file storage systems, and message queues. Data Integration provides synchronization plug-ins that can be used to connect to the servers of data sources and collect data. Data Integration supports data transmission in complex network environments. For example, it can transmit data across local private networks or virtual private clouds (VPCs).

> **Note:** Data Integration uses specific protocols to accelerate the transmission of large amounts of data over a long distance. This way, the stability and efficiency of the data transmission are ensured.

Data Integration implements accurate throttling on channels, record streams, and byte streams. Data Integration also supports fault tolerance and allows you to rerun specific or all threads, processes, and jobs. Data Integration uses the network interface controller (NIC) on each server and adopts a distributed architecture to transmit gigabytes or terabytes of data within a short period of time. Data Integration supports conversion between different data types and accurately identifies, filters, collects, and displays dirty data to facilitate inbound data control. In addition, Data Integration provides statistics such as data volume, data throughput, and job duration and detects dirty data in each job.

**Data Modeling**

Data Modeling is an intelligent data modeling service that is developed by the Alibaba Cloud DataWorks team. Data Modeling has accumulated the best practices of the methodology for data warehouse modeling of Alibaba Group over the past ten years. Data Modeling strengths the modeling capabilities of enterprises, including reverse modeling capabilities in the process of data mid-end and data mart building, and helps enterprises quickly build data assets. Data Modeling consists of the following modules: **Data Warehouse Planning**, **Data**
**Standard**, **Dimensional Modeling**, and **Data Metric**.
**Data Warehouse Planning**: allows you to plan data layers, data domains, and workflows,
and configure model design workspaces. Different units can share the same data standards and the same data model.
**Data Standard**: allows you to impose constraints on field standards, lookup tables,
measurement units, and naming dictionaries to ensure the consistency of data processing in data modeling and application. This way, data can be produced in a standardized manner, and data application and processing costs are reduced.
**Dimensional Modeling**: supports reverse modeling, which helps resolve the issue of the
cold start of modeling based on existing data warehouses. This module also supports visualized dimensional modeling based on data warehouses and allows you to quickly build data models by using FML statements, a type of domain-specific language (DSL) similar to SQL statements. You can efficiently publish your model to the desired R&D engine.
**Data Metric**: allows you to create atomic metrics and derived metrics. You can create a
single derived metric or multiple derived metrics at the same time based on the same atomic metric and different periods and modifiers. This module is seamlessly integrated with Dimensional Modeling. Data Modeling helps enterprises build modeling capabilities and mine the value of data assets. You can use Data Modeling in the following scenarios:
**Standardize management of massive data** : Larger enterprises have more complex
data structures. With the rapid development of enterprise business, the amount of business data exponentially grows. How to manage and store data in a structured and orderly manner is a challenge that every large enterprise faces.
**Break information barriers by interconnecting business data** : If the data of each
business or department in an enterprise is isolated from one another, the decision-makers cannot clearly or fully understand the data. How to break data silos between departments or business domains is a requirement for business data management.
**Integrate data standards to achieve unified and flexible data interconnection** :
Inconsistent descriptions of the same data result in duplicate data, incorrect calculation results, and difficulties in business data management. How to formulate a unified data standard without changing the original system architecture and realize flexible interconnection between upstream and downstream business is one of the core focuses of standardized management.
**Maximize data value to maximize profit** : Make the most of various types of enterprise
data to maximize the data value to deliver a more efficient data service for enterprises.

**Datablau**

DataWorks provides the Datablau feature based on the Datablau Data Modeler (DDM) client. You can use Datablau to design and manage data models and add and implement data standards for data development in DataWorks. This allows you to obtain more value from data and efficiently manage the lifecycle of data. Datablau supports the following features: Visualized model design: Datablau provides professional local clients and lightweight online clients that you can use to build visualized models in different scenarios. Collaborative design: Datablau allows multiple users to collaborate on the same model. Customization of data standards: Datablau allows you to define data standards, code specifications, and naming conventions. Intelligent reference of data standards: Datablau allows you to set data standards before you build a data model. This way, you can reference the pre-set standards when you build data models. Forward and reverse modeling based on DDL statements: Datablau allows you to execute DDL statements to publish a model to a compute engine instance. Data Modeling also allows you to export a model from a compute engine instance, edit the model, and then republish the model to the compute engine instance. This way, you do not need to perform complex operations in traditional modeling, such as manual import and export of data models. Model library: Datablau allows you to import data models to or export data models from a model library for centralized management. Model monitoring: Datablau helps you monitor the data models that are published to a compute engine instance. This way, you can easily identify the inconsistency between the schema of a table and the schema of a physical model. Integration with DataStudio: Datablau allows you to publish a model to a compute engine instance that is associated with a DataWorks workspace for subsequent data development and analysis. This way, you can design and publish models in a standard manner.

**DataStudio**

DataStudio is an all-in-one integrated development environment (IDE) that enables you to develop the extract, transform, and load (ETL) process and data mining algorithms. DataStudio also allows you to build data warehouses in DataWorks. After underlying data is aggregated, the data is disordered and cannot be directly used by upper-layer algorithms or data intelligence applications. In this case, you must process the aggregated data. You can build data centers in the data resource platform to process data. DataStudio supports the following features: DataStudio supports various compute engines, such as MaxCompute, E-MapReduce (EMR), Hologres, AnalyticDB, and ClickHouse. You can create, test, deploy, and perform O&M operations on nodes of the preceding compute engines in DataStudio. DataStudio provides an intelligent code editor and the scheduling capability and allows you to configure scheduling dependencies in a visualized manner. The scheduling capability is verified by tens of millions of scheduling nodes and complex business dependencies in Alibaba Group. DataStudio isolates the development environment from the production environment and provides features such as code version management, code review, smoke testing, and release control. In addition, DataStudio works together with ActionTrail. This way, enterprises can develop data in a standard manner.

**O&M Center**

O&M Center is an end-to-end service that provides O&M capabilities for data developers and O&M personnel. O&M Center allows you to specify the priorities of nodes and control and monitor the execution of nodes. To handle the volume, diversity, and complexity of data that is used in DataWorks and meet the requirements of various data processing tasks, a scheduling system that supports high concurrency, multiple cycles, and various data processing procedures is required. O&M Center allows you to monitor the status of nodes, view alerts of failed nodes or instances, and view the daily O&M statistics. Such statistics help you maintain the timeliness of your data and troubleshoot node issues at the earliest opportunity.

**Data Map**

Data Map allows you to centrally manage data and track data lineages. Based on data search, Data Map provides tools, such as table instructions, data categories, data lineages, and field lineages. Data Map helps customers and owners of data tables efficiently manage data and collaborate on development.

**Data Quality**

Data quality supports quality checks on common big data storage systems, such as MaxCompute, Hologres, AnalyticDB for PostgreSQL, and AnalyticDB for MySQL. You can configure quality monitoring rules across multiple dimensions, including completeness, accuracy, validity, consistency, uniqueness, and timeliness. You can also associate quality monitoring rules with scheduling nodes. When an associated task is complete, the rules are triggered to validate the data, which helps you immediately detect data issues. You can set the severity of rules to control whether a task fails, which prevents the spread of dirty data and reduces the time and cost of data recovery.

**Security Center**

Security Center allows you to build a security system that can secure data and personal privacy in an efficient manner. Security Center can meet various security requirements in high-risk scenarios, such as auditing. You can use Security Center without the need to perform additional configurations. Security Center provides security capabilities for big data systems in the cloud throughout the entire data security lifecycle. It also provides best practices for various security diagnostic scenarios based on security specifications. Security Center supports the following features: Data permission management: Security Center supports fine-grained permission requesting, request processing, and permission auditing. This allows you to manage permissions based on the principle of least privilege. In addition, Security Center allows you to view the request processing progress and follow up request processing in real time. Best practices for security diagnosis scenarios: Security Center provides features such as platform security diagnosis and data usage diagnosis. It also provides best practices for various security diagnosis scenarios based on security specifications. These features ensure that your business is run more effectively in a secure environment.

**Data Security Guard**

Data Security Guard is a data security management platform that you can use to identify data assets, detect sensitive data, classify data based on categories and sensitivity levels, mask data, monitor data access behavior, report alerts, and audit risks. Data Security Guard provides security management services for MaxCompute. Data Security Guard supports the following features:

**Intelligent detection of sensitive data**

Data Security Guard automatically detects an enterprise's sensitive data based on selftraining models and algorithms, and displays statistics on data types, volume, and visitors. It also recognizes custom data types.

**Precise data classification**

Data Security Guard allows you to classify data and create sensitivity levels to improve the efficiency of data management.

**Flexible data masking**

Data Security Guard provides diverse and configurable methods for dynamic data masking.

**Monitoring and auditing of risk-prone user behaviors**

Data Security Guard uses various multidimensional correlation analysis and algorithms to detect risk-prone user behaviors. It also provides alerts and supports visualized auditing for detected risks.

**Data Governance Center**

Data Governance Center detects issues that need to be handled in the data storage, node computing, code development, data quality, and data security stages based on preconfigured governance plans. Data Governance Center also provides health scores to evaluate the effectiveness of data governance and visualizes the governance results by providing governance reports and the rankings of governance issues from the global, workspace, and personal perspectives. This helps you efficiently achieve governance goals. In addition, Data Governance Center provides features such as business asset management, asset analysis, resource consumption details of tasks, and cost estimation to help you better understand the usage details of various resources.

**Data Asset Management**

Data Asset Management is a tenant-level feature. To use this feature, you must obtain the required permissions. This feature allows you to manage data assets in your business system and DataWorks, such as tables and APIs. Before you use this feature, you must use Data Integration to synchronize data and then use DataStudio to process the data. This way, you can manage data in a centralized manner. You can also have a command of the core data assets and formulate standards for the management of the data assets.

**Data Analysis**

Data Analysis provides easy-to-use tools for non-professional data developers such as product managers, operations staff, and data analysts to obtain and use data. These tools help improve the efficiency of data analysis. Data Analysis allows you to upload data, query tables, add tables to favorites, execute SQL statements to obtain data, share SQL files, download SQL query results, and view workbooks. Data Analysis helps data analysts, product managers, and operations staff to efficiently analyze and share massive data in a secure manner.
**Massive data analysis**: Data Analysis uses compute engines to analyze large amounts of
data in an efficient manner.
**Data sharing**: Data Analysis can analyze data obtained from the databases of different
business systems. Data Analysis allows you to export data to MaxCompute tables. Data Analysis also allows you to share result data with specific members and grant the members the permissions to access the data. This way, data can be shared among different systems and different users.
**High security**: Data Analysis supports security auditing on operations such as SQL queries
and downloads of SQL query results.

**DataService Studio**

DataWorks provides DataService Studio for building a data service bus that enterprises can use to manage private and public APIs in a centralized manner. DataService Studio supports the following features:

**Quick generation and registration of APIs**

DataService Studio allows you to create APIs based on data tables. You can also register existing APIs in DataService Studio to publish and manage the APIs in a centralized manner.

**Secure data sharing**

DataService Studio and API Gateway are interconnected. This allows you to publish APIs to API Gateway with ease. DataService Studio works together with API Gateway to provide a secure, stable, low-cost, and easy-to-use data sharing service.

**Low O&M costs**

DataService Studio adopts a serverless architecture. This allows you to focus on the query logic of an API without the need to worry about the infrastructure, such as computing resources. DataService Studio supports automatic scaling for computing resources, which significantly reduces your O&M costs.

**Flexible data exchange services**

DataService Studio is the key component for data exchange. It can be used by public service sectors as a secure, flexible, and reliable platform for data sharing across departments and networks. DataService Studio provides a secure, flexible, and reliable data service bus that enables the public service sectors to exchange data across departments over different networks and share data with the public.

**Migration Assistant**

Migration Assistant allows you to migrate jobs from open source scheduling engines to DataWorks and migrate development results from DataWorks. Migration Assistant is applicable to the following scenarios:

**Backup**

You can use Migration Assistant to periodically back up your node code to prevent data from being deleted by mistake.

**Quick replication**

You can use Migration Assistant to export a common workflow that can be replicated in other workspaces.

**Test environment creation**

You can use Migration Assistant to copy all node code and replace production data with test data to build a test environment.

**Data development in a hybrid cloud environment**

You can use Migration Assistant to migrate node code from the Alibaba Cloud public cloud to Apsara Stack to develop data in a hybrid cloud environment.

**Isolation between the development and production environments**

If the production environment of your workspace is completely isolated from the development environment of the workspace, you can use Migration Assistant to export nodes from the development environment and import them to the production environment for deployment.

**Open Platform**

DataWorks uses Open Platform to open its data and capabilities to external applications. Open Platform consists of the OpenAPI, OpenEvent, and Extensions modules. You can use the modules to quickly integrate your applications with DataWorks. This helps you manage data processing, data governance, and data O&M, and allows you to identify important changes in DataWorks and respond to the changes at the earliest opportunity.

**Tenant Management**

Tenant Management provides the following features: workspace management, member management, resource scheduling, compute engine management, authorization management, and resource group management. This helps organization administrators to manage important resources in their organizations.

### 1.2 Benefits

DataWorks provides various benefits, such as computing and processing of ultra-large-scale data, rapid integration of massive heterogeneous data sources, end-to-end data quality monitoring, and secure data sharing.

**Powerful computing capabilities**

DataWorks integrates with compute engines that can process large amounts of data. DataWorks supports join operations for trillions of data records, millions of concurrent nodes, and I/O throughput of petabytes per day. The offline scheduling system can run millions of concurrent nodes. You can also configure rules and alerts to monitor the execution of nodes in real time. DataWorks provides efficient and easy-to-use SQL and MapReduce engines, which support most standard SQL syntax. DataWorks protects user data from loss, breach, or theft by using multi-layer data storage and access security mechanisms, including triplicate backups, read/write request authentication, application sandboxes, and system sandboxes.

**All-in-one platform**

DataWorks provides a graphical user interface (GUI) that allows multiple users to collaborate on a workspace. DataWorks integrates all processes from data integration, processing, management, and monitoring to output. DataWorks allows you to create and edit workflows on the GUI. DataWorks provides a collaborative development environment. Users can be added to a workspace and assigned different roles to perform operations, such as node development, online scheduling, O&M, and data permission management.

**Integration from heterogeneous data sources**

DataWorks supports batch synchronization of data among heterogeneous data stores at custom intervals in minutes, days, hours, weeks, or months. More than 400 pairs of heterogeneous data stores are supported.

**Web-based software**

DataWorks is an out-of-the-box service. You can use it on the Internet or an internal network without the need for installation and deployment.

**Multitenancy**

Data is isolated among different tenants. Each tenant controls permissions, processes data, allocates resources, and manages members in a unified and independent manner.

**Intelligent monitoring and alerting**

By setting monitoring thresholds, you can control the entire process of all nodes as well as monitor the running status of each node.

**Easy-to-use SQL editor**

The SQL editor supports automatic code and metadata completion, code formatting and folding, and pre-compilation. The SQL editor also offers two editor themes. These features ensure good user experience.

**Holistic data quality monitoring**

DataWorks supports quality check, notification, and management for heterogeneous data sources, batch data, and real-time data.

**Convenient API development and management**

DataWorks interacts with API Gateway to make it easy for you to develop and publish APIs for data sharing.

**Secure data sharing**

DataWorks provides an encryption component that can be integrated into the data transfer process. When data is transferred from the owner to a user, the data transferred to the user is encrypted. DataWorks is equipped with the envelope encryption technology, which ensures that the provided ciphertext can be used only by authorized users. This ensures that data cannot be used after being transferred to a third party and enhances data security during data sharing.

### 1.3 Scenarios

DataWorks is widely used in various data scenarios, such as cloud data warehouses, business intelligence (BI) applications, and data-driven operations.

**Cloud data warehouses**

Large-scale enterprises can use Apsara Stack DataWorks to build ultra-large data warehouses. DataWorks can process massive data with robust capabilities: Massive data storage: allows you to build a data warehouse that stores petabytes or exabytes of data and supports linear expansion of storage capacity. Data integration: supports data synchronization and integration across heterogeneous data sources to eliminate data silos. Data analytics: supports MaxCompute-based big data analytics, programming frameworks such as SQL and MapReduce, and a visualized workflow designer. Data management: provides a data resource management view and a procedure for processing data permission requests based on a unified metadata service. Batch scheduling: supports periodic scheduling of nodes at different intervals, scheduling of millions of concurrent threads per day, and real-time node monitoring and alerting.

**BI applications**

This section describes how to create reports by using DataWorks. You can analyze the following items based on the network logs of your website: Page views, unique visitors, and device types such as Android devices, iPads, iPhones, and PCs. You can also create a daily report based on these statistics. Locations of visitors. The following log entry is used as an example:

```
xx.xxx.xx.xxx - - [12/Feb/2014:03:15:52 +0800] "GET /articles/4914.html HTTP/1.1" 200 3 "http://xxx.cn/articles/6043.html" "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/xx.x.xxxx.xxx Safari/537.36" -
```

1. Create a destination table named ods_log_tracker in MaxCompute, and then import data to
the table.
2. Configure dependencies among the tables to be analyzed.
3. Create a shell node, a data synchronization node, and an ODPS SQL node.
4. Develop the nodes.

**Data-driven operations**

Innovative business: supports data mining, data modeling, and real-time decision-making to help you use big data analytics results in your business system. Small and medium-sized enterprises: supports efficient processing and analysis of data to help enterprises make informed business decisions.

### 1.4 Features

#### 1.4.1 Data integration

Data Integration is a stable, efficient, and scalable data synchronization service. It is designed to migrate and synchronize data between various disparate data sources in complex network environments.

| Category | Feature | Description |
|---|---|---|
|   | Offline single-table batch data synchronization | Alibaba Cloud proprietary This feature allows you to read data from and write data to the following Alibaba Cloud proprietary databases: AnalyticDB for MySQL (2.0), AnalyticDB for MySQL (3.0), AnalyticDB for PostgreSQL, ApsaraDB for OceanBase, Distributed Relational Database Service (DRDS), DataHub, Hologres, HybridDB for MySQL, Lindorm, MaxCompute, Object Storage Service (OSS), OSS- HDFS, PolarDB, PolarDB-O, PolarDB-X 2.0, and Tablestore. Relational databases This feature allows you to read data from and write data to the following types of relational databases: AnalyticDB for MySQL (2.0), AnalyticDB for MySQL (3.0), AnalyticDB for PostgreSQL, ApsaraDB for OceanBase, DB2, Dameng (DM), DRDS, HybridDB for MySQL, MySQL, Oracle, PolarDB, PolarDB-O, PolarDB-X 2.0, PostgreSQL, SQL Server, SAP HANA, MariaDB, and TIDB (read- only). Big data storage This feature allows you to read data from and write data to the following types of big data warehouses: ClickHouse, Data Lake Formation 2.0 (write-only), DataHub, GBase8a, HBase, Hive, Hologres, Kafka, KingbaseES, Lindorm, LogHub, StarRocks, and Vertica. Semi-structured storage |

|   |   | This feature allows you to read data from and write data to the following semi-structured storage services: Azure Blob Storage (read-only), File Transfer Protocol (FTP), Hadoop Distributed File System (HDFS), HttpFile (read-only), OSS, OSS- HDFS, and RESTful API. NoSQL databases This feature allows you to read data from and write data to the following NoSQL databases: Elasticsearch, MongoDB, Redis (write-only), and Tablestore. File/object storage This feature allows you to read data from and write data to file/object storage: FTP, HDFS, HttpFile (read-only), and OSS. Message queues This feature allows you to read data from and write data to the following message queue services: Datahub, Kafka, and Loghub. Open protocol storage |
|---|---|---|
| Data Integration- Standard Edition |   | This feature allows you to read data from and write data to open protocol storage: ClickHouse, Elasticsearch, FTP, HBase, HDFS, Hive, Kafka, MongoDB, PostgreSQL, and RESTful API. Other databases This feature allows you to read data from and write data to Yashan Database, Shentong Database, and GaussDB. This feature allows you to read data from Informix. |
|   | Data source management | Network connectivity control This feature allows you to synchronize and integrate data between disparate data sources in complex network environments. Environment isolation This feature allows you to isolate data sources in the production environment from those in the development environment. This prevents operations that are performed on data sources in the development environment from affecting data in the production environment. Permission control This feature allows you to manage permissions on data sources, such as granting permissions on data sources to users. This ensures the security of data sources. Authentication file management This feature allows you to manage the authentication files of specific data sources, including Kerberos authentication files and SSL- based authentication files. |

|   | Offline batch data synchronization from a database | This feature allows you to synchronize full data and incremental data from a database to a compute engine at the same time. Supported databases include AnalyticDB for MySQL (V2.0), AnalyticDB for MySQL (V3.0), AnalyticDB for PostgreSQL, DRDS, Hologres, HybridDB for MySQL, PolarDB, DB2, DM, MySQL, Oracle, PostgreSQL, SQL Server, and Hive. |
|---|---|---|
|   | Rate control for offline batch data synchronization | Transmission rate control This feature allows you to configure the maximum data transmission rate for a synchronization node. If this rate is excessively high, the I/O usage of the connected database may reach 100%, which can negatively impact its performance. Connection concurrency control This feature allows you to configure the maximum number of parallel threads that a synchronization node uses to read data from the source and write data to the destination. This prevents the synchronization node from getting stuck. |
|   | Data filtering for readers | This feature allows you to configure filter conditions for the reader in your data synchronization node, ensuring that only data meeting these conditions is read. |
|   | Dirty data monitoring | This feature allows you to configure a dirty data monitoring rule for your data synchronization node. Based on this rule, DataWorks determines whether to terminate the synchronization task. |

| Data Integration- Real-time Synchronization Enhancement Packages Note In addition to the features of Data Integration- Standard Edition, the features supported in this module are implemented by using enhancement packages. | Real-time data synchronization for a single table | Real-time data reading This feature allows you to read data from the following tables in real time: MySQL, DataHub, LogHub, Kafka, and PolarDB. Real-time data writing This feature allows you to write data to the following tables in real time: MaxCompute, Hologres, AnalyticDB for MySQL (3.0), Elasticsearch, DataHub, and Kafka. Data Definition Language (DDL) messages DDL messages are supported. When writing data to Hologres, you can dynamically add columns. |
|---|---|---|
|   | Real-time full- database synchronization | Supported real-time full-database synchronization solutions: Synchronizes entire DRDS databases to Hologres in real time. Synchronizes entire PolarDB databases to Elasticsearch, Hologres, Kafka, or PolarDB in real time. Synchronizes entire MySQL databases to Elasticsearch, Hologres, Kafka, or PolarDB in real time. Synchronizes entire Oracle databases to DataHub, Hologres, Kafka, or PolarDB in real time. |
|   | Full and incremental (near real-time) database synchronization | This feature allows you to perform full and incremental (near real-time) synchronization of entire ApsaraDB for OceanBase, PolarDB, MySQL, and Oracle databases to MaxCompute. |
|   | Sharded databases and partitioned tables during real- time synchronization | This feature allows you to perform real-time synchronization of sharded PolarDB and MySQL databases and their partitioned tables to MaxCompute. |
|   | Data processing during real-time synchronization | This feature allows you to configure data filtering and string replacement during real-time synchronization. |
|   | Task monitoring during real-time synchronization | This feature allows you to configure monitoring for a real-time synchronization node. You can receive alerts by DingTalk, SMS, or email. |

#### 1.4.2 DataStudio

DataStudio is the data development platform in DataWorks. You can use DataStudio to build standardized and efficient data processing workflows. Key features include:

| Feature | Description |
|---|---|
| File management | Solutions and business flows Use solutions and business flows to manage tasks, tables, resources, and functions. Directory tree Displays the hierarchical structure of your files in a directory tree. Batch operations Perform batch operations on files, such as committing, changing owners, and deleting. Global code search Search for code within the current workspace. Recycle Bin Temporarily stores deleted files in the Recycle Bin. |
| Task development | You can use a wide range of node types, including MaxCompute, Hologres, algorithm, database, general-purpose, and custom nodes. The specific node types available are shown in the console. Node group Bundle multiple nodes into a node group for easy reuse. Code editor The code editor provides syntax highlighting, error checking, code formatting, and auto-completion for table and field names. Multi-user editing Enables non-real-time collaborative editing through file locking and unlocking. |
| Table management | MaxCompute tables Create tables with a visual editor or DDL statements, view table metadata, and import data from local files. |
| Resource and function management | MaxCompute resources and functions Upload resources (Python, JAR, Archive, File) and register functions. |
| Task scheduling configuration | Configure periodic and manual scheduling, DAG orchestration, scheduling parameters, dependencies, rerun counts and intervals, timeout periods, and scheduling resource groups. |
| Task debugging | Test-run workflows, run tasks with or without parameters, and run smoke tests. Run ad-hoc queries, view run history, and download run results. |

| Version management | Version management features include comparison, rollback, commits, reviews, and publishing. |
|---|---|

#### 1.4.3 Operation Center

The Operation Center includes Operation Dashboard, Real-time Task O&M, Scheduled Task O&M, Trigger-based Task O&M, Intelligent Monitoring, Engine O&M, Scheduling Settings, and Operation History.

| Feature | Description |
|---|---|
| Operation Dashboard | The Operation Dashboard displays key O&M metrics, overall task run status, and scheduling resource usage trends. It also shows the run status distribution and data synchronization progress for batch and real-time synchronization tasks. This information helps improve your task O&M efficiency. |
| Real-time Task O&M | This section provides O&M for real-time compute tasks and real- time synchronization tasks, including viewing logs, starting or stopping tasks, decommissioning, and monitoring. |
| Scheduled Task O&M | For scheduled tasks, scheduled instances, backfill instances, and test instances, this module provides O&M operations such as viewing logs, testing, backfilling data, rerunning, suspending or resuming, and marking them as successful. |
| Trigger-based Task O&M | Also known as manual task O&M, this module provides O&M for trigger-based tasks and trigger-based instances, including operations such as viewing logs, testing, backfilling data, rerunning, suspending or resuming, and marking them as successful. |
| Intelligent Monitoring | Intelligent Monitoring analyzes DataWorks task runs. It supports configuring smart baselines, Rule Management, alerts, and on- call schedules. Based on your rules and the task status, the system automatically determines whether, when, how, and to whom to send an alert. |
| Engine O&M | This feature provides O&M for the MaxCompute engine. You can view information about its j*********, q**********, and project lists. |

| Scheduling Settings | DataWorks enhances its standard scheduling configurations with a custom scheduling calendar feature. This allows you to define more flexible scheduling dates and methods for your tasks. Scheduling calendar management This feature allows you to define more flexible scheduling dates and methods for your tasks. Workspace parameters DataWorks adds workspace -level scheduling parameters to its existing task-level scheduling parameters. You can use workspace parameters when multiple parameters in the same workspace need to have the same value. These parameters can be masked to protect sensitive data. In a standard-mode workspace , you can set different values for workspace parameters in the production environment and development environment . |   |   |   |
|---|---|---|---|---|
|   |   |   | workspace |   |
|   |   | workspace |   |   |
| Operation History | The Operation History page records your actions across the Operation Center, allowing you to trace historical operations and view their details. |   |   |   |

|   | parameters |
|---|---|

|   |   |   | workspace |
|---|---|---|---|
|   | workspace parameters |   |   |
| production environment |   |   |   |

#### 1.4.4 Data Map

Data Map is an enterprise data asset management module built on metadata. It provides features including global data search, detailed metadata viewing, data preview, data lineage, and data category management. Data Map helps you find, understand, and use your data. Key features include:

| Feature | Description |
|---|---|
| Homepage | The homepage has three main areas: Data usage You can use Recently Viewed (tables, APIs), Albums I Manage, and Albums I Follow to filter for target information and view its details. Data management You can configure Data Album and Category Navigation to view related summary information. Metadata collection You can view summary information by selecting different data sources, such as MaxCompute, MySQL, Hologres, and AnalyticDB for PostgreSQL. |
| Search | Supports searching by table, API, and workspace. Search by keyword. Filter search results by specific criteria. |

| Data Album | The data album feature helps you classify, organize, and manage data tables from a business perspective. You can add specified tables to a data album for quick access and management. |
|---|---|
| My Data | You can view and manage related data on the My Data page, including: Data I Own, Data I Manage, Production Account Data, My Favorites, Permission Management, and Refresh Table Metadata. |
| Metadata Collection | This feature lets you centrally manage metadata from various systems and view it in Data Map. Key features include: Collects metadata from various data sources, including databases such as E-MapReduce, Hologres, Table Store (OTS), MySQL, Oracle, and SQL Server. Detects real-time metadata changes, such as table creation, modification, or deletion. |
| Configuration Management | Supports Category Navigation Configuration, Project Management Configuration, and Other Configurations (such as security control). |

#### 1.4.5 Data quality

The data quality feature helps you detect changes in source data and identify dirty data generated during Extract, Transform, and Load (ETL) processes as early as possible. It automatically intercepts problematic tasks, preventing dirty data from propagating to downstream systems. This prevents the creation of unexpected data that could impact operations and business decisions. It also reduces the time and cost of troubleshooting and avoids resource waste from re-running jobs. Data quality supports quality checks on common big data storage systems, such as MaxCompute, Hologres, AnalyticDB for PostgreSQL, and AnalyticDB for MySQL. You can configure quality monitoring rules across multiple dimensions, including completeness, accuracy, validity, consistency, uniqueness, and timeliness. You can also associate quality monitoring rules with scheduling nodes. When an associated task is complete, the rules are triggered to validate the data, which helps you immediately detect data issues. You can set the severity of rules to control whether a task fails, which prevents the spread of dirty data and reduces the time and cost of data recovery. Its core features are as follows:

**New version**

| Feature | Description |
|---|---|
| Quality overview | The quality overview dashboard provides a comprehensive view of data quality within your workspace. It displays key metrics that require attention, trends and distributions of quality rule check statuses after job runs, tables with the most quality issues and their responsible owners, and rule coverage status. This helps quality managers quickly understand the overall data quality, address issues promptly, and improve data quality. |

| Quality assets | Rule list View a list of all quality monitoring rules created in your workspace. You can filter rules by data source type, table name, or rule template to find and manage specific rules. Rule template library Create your own rule template library to centrally manage reusable custom monitoring rules. Applying these templates streamlines the rule configuration process and improves efficiency. |
|---|---|
| Rule configuration | Configuration by table Configure quality monitoring rules for individual tables to monitor whether the data meets your requirements. This feature automatically blocks problematic tasks and prevents dirty data from propagating downstream, ensuring the output data meets expectations. Configuration by template This feature provides a variety of pre-built table-level and field-level monitoring templates. |
| Quality Operations | Quality monitoring View a list of all quality monitoring tasks in your workspace. You can filter tasks by table name, keyword, or trigger type to locate and manage them. Run logs View the run logs to check the validation results of your quality monitoring tasks. After a monitoring task runs, you can review the detailed results on the run logs page. |
| Quality analysis | Create report templates and customize them by adding various metrics from rule configurations and runs. The system can then automatically generate and send reports based on a defined schedule, time, and subscriber list. |

**Legacy version**

| Feature | Description |
|---|---|
| Overview | The data quality overview page displays alert and blocking statistics. |
| My subscriptions | Displays the latest quality status for data entities (including MaxCompute, DataHub, and Kafka) that you subscribe to. |
| Rule management | View the rule list. Supports configuration by table, configuration by template, and a custom rule template library. |

| Task query | On the task query page, you can search for past validation results by table or node. |
|---|---|
| Configuration | Report template management The report template management page allows you to create report templates. You can add metrics from rule configurations and runs. The system automatically generates and sends reports based on a defined schedule, time, and subscriber list. Denoising management The denoising management feature allows you to suppress an alert and prevent task blocking for a specified period, even if a data quality rule check fails in the workspace. |

#### 1.4.6 Security center

As the security portal for your cloud-based big data system, DataWorks Security Center provides features that span the entire data security lifecycle. It also offers best practices for security diagnostics to help you meet security standards. Key features include:

| Feature | Description |
|---|---|

| data platform security | Platform Security Diagnostics Security Diagnostics for Data Compute and Storage Assesses the security of data permission controls, storage encryption, and backups. This helps you quickly identify potential security risks and improve data security during storage and access. Security Diagnostics for Data Transmission Assesses the security of data source access controls and the isolation between production and development data sources. This helps you identify and resolve security risks during data transmission to ensure a secure transfer environment. Security Diagnostics for Data Production Standardization Assesses the security of your data production process by evaluating factors in your workspace, including role assignments, the number of administrators, and deployment permissions. This helps you quickly identify and mitigate security risks, improving the stability and security of your data production pipeline. Data Access Control Manages permission requests and approvals. Lets you view records of permission requests, approvals, and audits. Sensitive Behavior Control Permission Request Lets you request permissions for Data Integration tasks to access their data sources. Lets you request permissions to publish APIs through Data Service. Permission Audit Lets you audit permission ownership by Alibaba Cloud account and sensitive behavior. |
|---|---|
| data usage security | Secures data content and privacy in your DataWorks workspace by offering solutions to identified security issues. This helps you quickly establish a baseline security framework to protect data during and after its use. |
| security policy | Enables entity transfers at the workspace level. Lets you view transfer logs. Lets you configure transfer rules. |

#### 1.4.7 Data Protection Umbrella

Data Protection Umbrella is a data security management product that includes data discovery, data masking, d****************, access control, risk identification, and data lineage. It helps you quickly identify sensitive data and apply security controls. Key features include:

| Feature | Description |
|---|---|
| Home | This page summarizes the following: Data discovery: The total number of fields matched by data identification rules over the past week, along with a breakdown by project. Data access: The daily access volume for fields that match data identification rules within the selected time period. Data risk: The number of new risks detected in the past week and the number of risks that have remained unresolved for over a month. Data audit: The number of data risks discovered and resolved. |
| Data discovery | Lets you identify sensitive data in your organization by configuring rules. This feature provides a visual overview of your data assets, broken down by dimensions such as project. |
| Data access | Displays access metrics for sensitive data identified by rules, including access volume, trends, user counts, access details, export volume, and export details. This helps you monitor access to your sensitive data. This feature currently supports data from the MaxCompute engine. |
| Data risk | Identifies potential risks using methods such as manual tagging, risk rules, and AI algorithms. It also allows you to add notes from manual audits. This feature currently supports risk identification for data operations in the MaxCompute engine. |
| Data audit | Provides a multi-dimensional view of your risk resolution status and risk distribution. This feature currently supports auditing for the MaxCompute engine. |

| Rule configuration | Data classification Data classification categorizes data based on value, content sensitivity, impact, and distribution scope. Different sensitivity levels have different governance principles and development requirements. After classifying data, you can apply appropriate controls based on its sensitivity level. Data identification rule In Data Protection Umbrella, you configure data identification rules based on sensitive field types. Once configured, these rules identify the corresponding types of sensitive data in your tenant. DataWorks provides a variety of built-in sensitive field types and identification rules. If the built-in rules do not meet your needs, you can create custom sensitive field types and identification rules. Data masking management In DataWorks, you can configure masking rules to protect sensitive data during queries and storage. This feature supports various masking scenarios that you can customize to meet your requirements. Risk identification management This feature uses multi-dimensional correlation analysis and intelligent algorithms to proactively identify and alert you to risky operations based on risk identification rules. It provides a unified, visual interface for auditing. DataWorks includes built-in risk identification rules for many scenarios, which you can use directly or customize for your business. User group management In DataWorks, the user group management feature lets you group accounts with the same data access permissions. When configuring data masking, you can add these user groups to an allowlist, allowing members to access the original, unmasked data. |
|---|---|
| System settings | You can configure settings such as data discovery account, discovery scope, discovery content, permission control mode, and enable tagging. |

#### 1.4.8 Data Governance Center

The Data Governance Center automatically discovers issues related to data storage, compute, code development, data quality, and security based on pre-configured governance plans. It uses a health score to quantify assessments and presents governance results through governance reports and leaderboards from global, workspace, and personal perspectives, helping you achieve your governance goals efficiently. The center also provides features such as business asset management, asset analysis, detailed task resource consumption, and cost estimation for a clear understanding of your resource usage. Its core functions are as follows:

| Feature | Description |
|---|---|

| Governance assessment | Evaluation report Provides the following information from global, workspace, and personal perspectives: Overall governance health score Overall governance assessment Health scores for the five governance dimensions: storage, compute, quality, development, and security Governance effectiveness Trends for the health score and the number of governance issues Le*******rd The governance leaderboard ranks objects, such as governance items and check item events, by individual, workspace, and governance unit to help drive governance initiatives. |
|---|---|
| Governance Workbench | Governance plan A governance plan lets you set goals for different scenarios. You can use templates to quickly select governance rules, identify optimization targets, and help responsible parties track governance effectiveness. This ensures that teams meet their goals on time. Governance item issues The system automatically detects issues requiring optimization based on your configured governance items. You can view the total number of optimizable issues, rankings of optimizable items, issue categories, and details of optimizable tasks or tables. This helps you quickly find and resolve pending governance issues. Check item event From global, workspace, and personal perspectives, the system automatically triggers checks and intercepts issues during processes like task publishing and submission based on the check items you have enabled. You can view a statistical overview and detailed information for these events here. Allowlist This section lists allowlist requests for governance item issues that you have marked as not requiring action. You can also manage these requests, for example, by revoking them. Graceful decommissioning This feature provides a streamlined workflow for decommissioning tasks. It includes batch risk assessment of multiple tasks, sending decommissioning notifications, and decommissioning process management. Applicable scenarios include: You need to decommission nodes that have regularly scheduled downstream tasks. An obsolete node is difficult to decommission due to unpredictable risks. Task 360, Table 360 These features provide a consolidated view of all information related to a task or table, including basic information, associated governance items, affected baselines, execution instances, metrics, and event records. |

| Usage analysis | Resource usage overview Provides overview statistics, usage rankings, and anomaly analysis for DataWorks and MaxCompute resources. Resource usage details Provides detailed lists of resource consumption for DataWorks and MaxCompute. |
|---|---|
| Knowledge Base | Provides detailed descriptions, resolution methods, and important notes for each governance item and check item. |
| Configuration management | Solution template The system provides built-in templates that include check items and governance items. You can use them after enabling a template. Check items are applied during processes like task publishing and submission to intercept problems and prevent the introduction of new governance issues. Governance items are used for post-hoc analysis to discover existing issues that require optimization. You can enable specific items as needed. Check item configuration The system generates an initial list of check items from the selected template. On this page, you can configure these items—for example, by enabling them globally or individually—to intercept problems during processes like task publishing and submission and prevent the introduction of new governance issues. Governance item configuration Governance items are initially generated based on the selected template. Here, you can enable or disable specific governance items. Cost configuration This feature lets you set custom resource unit prices, which automatically includes cost estimation statistics in governance effectiveness reports. This is used to estimate costs for compute and storage resources. Governance unit A governance unit consists of one or more workspaces. The most common practice is to group workspaces by business line. Governance units centrally aggregate statistics for all their included workspaces, such as the overall health score and governance item and check item events. In this section, you can create, edit, and delete governance units. |

#### 1.4.9 Data assets

DataWorks data asset management helps enterprises inventory their data assets and demonstrate the business value of the Data Middle Platform. It also allows business users to quickly find and use the data assets they need in a secure environment. Key features include:

| Feature | Description |
|---|---|
| Asset Panorama | Displays a 3D view of asset catalogs and data assets, showing their layout, relationships, and details across different levels and types. You can also search for assets within this panoramic view. Displays key statistics across various asset dimensions, such as core asset metrics, asset change trends, asset catalog distribution, popular asset rankings, newly published assets, and recently updated assets. |
| Asset Marketplace | Lets you browse asset catalogs by hierarchy or search for assets by keyword. You can then view asset details, request permissions, and analyze data. |
| Asset Value | Evaluates the value of published assets to help managers with asset inventories. This feature provides an asset value overview, asset value rankings, and asset value details. |
| Asset Consumption | Lets you visually query assets, such as models published from MaxCompute physical tables, and download the results. |
| Management Center | Catalog Management: Lets administrators configure the global asset catalog. Asset Management: Lets administrators publish or unpublish ingested assets and add them to a catalog. Asset Space: Lets asset administrators specify other workspaces whose assets can be centrally managed in the current workspace. Asset Collection: Lets asset administrators configure asset ingestion policies. |

#### 1.4.10 Data analysis

Data analysis provides three core functions: SQL query, spreadsheet, and system management. Designed to empower every user to become a data analyst, it provides streamlined tools for data analysts, product managers, and operations teams to quickly retrieve and use data for daily analysis. Key features include:

| Feature | Description |
|---|---|
| Home | This page provides quick access to SQL query and spreadsheet, and shows your recently edited files. |

| SQL query | Supports multiple big data engines and data source types, such as MaxCompute, MySQL, and PostgreSQL. The console displays the available options. Perform basic operations in the SQL editor. View SQL query results and logs. |
|---|---|
| Spreadsheet | View lists of files you created and files shared with you. You can rename, transfer, clone, delete, and search your created files. Import data using options such as Import Local Data, Import Spreadsheet Data, and Manual Edit. Use standard spreadsheet operations, including font settings, alignment, number formats, row and column formatting, conditional formatting, cell styles, functions, filters, sorting, clearing, and searching. Convert field types to numeric or string. |
| System management | Set the maximum number of records that a SQL query can return. Configure download and sharing features for spreadsheets. |

#### 1.4.11 DataService Studio

DataService Studio is a flexible, secure, stable, and cost-effective platform that allows you to create and publish APIs. DataService Studio serves as a bridge between databases and data applications, and provides comprehensive data processing and sharing capabilities for individuals, teams, and enterprises to help them manage APIs that belong to and do not belong to Alibaba Cloud in a centralized manner. For example, you can use DataService Studio to quickly generate APIs based on data tables. You can also register existing APIs with DataService Studio to publish and manage the APIs in a centralized manner. The following section describes the core features of DataService Studio.

| Feature | Description |
|---|---|
|   | Data source types Common relational databases: ApsaraDB RDS, MySQL, SQL Server, PostgreSQL, and Oracle. NoSQL databases: Tablestore and MongoDB. Big data storage systems: MaxCompute, Hologres, AnalyticDB for MySQL 2.0, AnalyticDB for MySQL 3.0, AnalyticDB for PostgreSQL, and PolarDB-X (formerly known as DRDS). Business processes Allows you to organize different types of resources (including APIs, functions, and workflows) in a business process. This helps you analyze data by business. APIs |

|   | When you create and configure an API in the codeless UI, the system pulls the schema of the table that you select, and you can specify the fields in the table as request parameters or response parameters based on your business requirements. You can also specify an operator for the API and configure paging and sorting for return results. A large number of operators are supported. You |
|---|---|
| Service Development | can specify the POST request method, and include request parameters in the request body. When you create and configure an API in the code editor, you can write SQL statements with complex logic. The code editor allows you to use table join clauses and aggregate functions in SQL statements and use MyBatis to generate dynamic SQL statements. You can specify the POST request method, and include request parameters in the request body. When you use a backend address to register an existing API with DataService Studio, common request methods and data formats are supported. After the API is registered with DataService Studio, you can centrally manage, publish, and integrate the API. You can configure data sources in the development or production environments. You can configure the timeout period, memory, and maximum number of entries to return on each page. Functions and filters Allows you to create a function and use the function as the prefilter or post-filter for an API. This way, the function can process the request parameters or responses of the API. This enhances the business logic of the API and enables the API to adapt to various scenarios. Provides the function ID as a new function property, and displays the list of associated APIs on the function editing page. Service orchestration Allows you to configure workflows by dragging nodes to directed acyclic graph (DAGs). You can arrange APIs and functions in a serial, parallel, or branch structure based on the business logic. Tables Allows you to search for a table by data source type and table name and preview the schema of the table. Tag management Allows you to add tags to created APIs, registered APIs, and workflows. This way, APIs can be classified and searched for in an efficient manner. Version management Allows you to manage the versions of resources and roll back a resource to a specific version. Generates a version record each time an API, function, or workflow is published. You can select two |

versions of a resource and compare the parameters or SQL scripts of the two versions. You can also roll back the resource to a specific version.

| Service Management | API management Allows you to view the APIs that are published, APIs that you are authorized to access, and APIs that you authorize others to access. This feature also allows you to unpublish, test, authorize access to, change the protocol of, or view the details page of a published API. Allows you to use the advanced search feature to filter APIs by data source name. API approval Allows tenant administrators to configure approval policies for publishing APIs, workflows, and functions in workspaces. This way, the APIs, workflows, and functions can be published only after they are approved. API statistics Collects statistics on the calls to APIs that are published to API Gateway. The following information is provided: total number of calls to all APIs over the last seven days, total duration of calls to all APIs over the last seven days, and statistics on each API. API testing Allows you to test APIs that are published. API calling and authentication Supports two authentication methods for API calls: simple authentication based on an AppCode and encrypted signature authentication based on an AppKey and an AppSecret. The two methods ensure the security of data sharing. API references Automatically generates a detailed reference page for each published API. An API caller can refer to the details page of an API before the API caller calls the API. The details page contains the basic information about the API, configuration notes of request and response parameters, sample success or error responses, and error codes. |
|---|---|
| Massively parallel processing (MPP) data source enhancement package | Supported databases: ClickHouse and AnalyticDB for MySQL 3.0. |

#### 1.4.12 Approval Center

Approval Center allows you to manage permissions on data and manage high-risk operations. You can also use Approval Center to specify the scope of requests and customize request processing procedures to meet your business requirements in different compliance scenarios. The following table describes the core features of Approval Center.

| Feature | Description |
|---|---|

| Policies | Supported policies: Compute engines: The system supports approval policies based on MaxCompute projects or data security levels. DataService Studio: Administrators can create approval policies for publishing DataService Studio APIs in workspaces. Data Integration: Administrators can create approval policies for saving Data Integration nodes in workspaces. |
|---|---|
| Application Records | Allows you to query your permission request records. |
| Requests To Be Processed | Allows you to query permission requests that are pending your approval. |
| Processing Records | Allows you to query the records of permission requests that are processed by you. |

#### 1.4.13 Migration Assistant

Migration Assistant allows you to migrate tasks from open source scheduling engines to DataWorks and migrate development results from DataWorks. The following table describes the core features of Migration Assistant.

| Feature | Description |
|---|---|
| Home Page | This page provides quick access to the big data migration platform, including the entries for cloud tasks and DataWorks migration, and quick access to scenarios for you to complete related operations. |
| Cloud tasks | You can migrate tasks from open source scheduling engines to DataWorks. You can also export tasks from DataWorks. |
| DataWorks Migration | You can copy DataWorks development results in an efficient manner. The following types of objects are supported: auto triggered tasks, manually triggered tasks, resources, functions, and ad hoc queries. |
| Advanced Features | Migration Assistant provides the object detection feature, which allows you to view the development results and cross-workspace dependencies in a workspace. Development results include tables, auto triggered tasks, resources, manually triggered tasks, data sources, objects in DataService Studio, functions, ad hoc queries, and components. |

#### 1.4.14 Open Platform

DataWorks uses Open Platform to open its data and capabilities to external applications. Open Platform consists of the OpenAPI, OpenEvent, and Extensions modules. You can use the modules to quickly integrate your applications with DataWorks. This helps you manage data processing, data governance, and data O&M, and allows you to identify important changes in DataWorks and respond to the changes at the earliest opportunity. The following table describes the core features of Open Platform.

| Feature | Description |
|---|---|
| OpenAPI | DataWorks provides a variety of APIs. You can use the OpenAPI module to integrate your own platform with DataWorks. This page displays the number of successful API calls in the current month and the API call details. For more information, see related information in Developer Guide of the corresponding version. |
| OpenEvent | DataWorks uses OpenEvent to open up event messages that are generated during the running of DataWorks. You can use Kafka to subscribe to events to monitor and respond to user operations and system processing operations on the DataWorks platform based on your business requirements. |
| Extensions | DataWorks Extensions is a plug-in that you can use with OpenAPI and OpenEvent. You can register an extension to customize the processing logic for user operations in DataWorks and to implement behavior control such as blocking. |

#### 1.4.15 Workspace Management

A workspace is the basic unit for task development and member permission management in DataWorks. DataWorks supports workspaces in basic mode and standard mode. You can implement different levels of security control on production data by using workspaces in different modes. The following table describes the core features of Workspace Management.

| Category | Feature | Description |
|---|---|---|
|   | General Configurations | Allows you to manage the basic attributes and security settings of a workspace, such as limiting the number of queries and adding the workspace to sandbox whitelists, and associate a workspace with compute engines. |
|   | Data Sources | Allows you to add, edit, and view data sources. Data sources are the objects of readers and writers in Data Integration. |
|   | Cluster Management | Allows you to configure account mappings and endpoints for Cloudera Distribution Hadoop (CDH) clusters associated with a workspace. |

| Workspace Settings |   |   |
|---|---|---|
|   | Workspace Members and Roles | Allows you to add, delete, and modify members and roles of a workspace. Workspace Members: allows you to view, add, and edit members of the current workspace. Workspace Roles: allows you to view and add custom roles. Permissions: allows you to view the permissions granted to each workspace role. |
|   | MaxCompute Advanced Settings | Allows you to manage security authorization and add custom user roles for associated MaxCompute projects. |
| Tenant Configurations | Extension | Displays the check items that are enabled in Data Governance Center and the extensions that are registered and published on the Extensions page of Open Platform. You can enable or disable a check item or configure an extension on this page to manage the check on and procedure of the related development and O&M operations. |

#### 1.4.16 Tenant Management

Tenant Management provides the following features: workspace management, member management, compute engine management, authorization management, and resource group management. This helps organization administrators manage important resources in their organizations. The following table describes the core features of Tenant Management.

| Feature | Description |
|---|---|
| Project Management | Allows you to manage workspaces in a centralized manner. You can create a workspace and manage an existing workspace. For example, you can configure, disable, or delete an existing workspace. |
| Member Management | Allows you to use role-based access control (RBAC) to manage permissions of all members within a tenant on DataWorks functionalities in a centralized manner. This feature also allows you to assign the current user a tenant-related role. |
| Calculation Engine | Allows you to manage the compute engine instances that are associated with your workspace in a centralized manner. For example, you can configure the access identity for a compute engine instance. |
| Authorization management | Allows you to configure permissions of each role in the current workspace on DataWorks functionalities. |

| Resource group management | A DataWorks resource group is a collection of computing resources that can be used by DataWorks services. DataWorks resource groups are a prerequisite to use DataWorks. The status of a resource group affects the status of related features. The quota of a resource group affects the efficiency of tasks or services. On the Exclusive Resource Group tab, you can create a resource group for scheduling or a resource group for Data Integration. On the Shared Resource Group tab, you can view the usage of the shared resource group for scheduling and the shared resource group for Data Integration. |
|---|---|

#### 1.4.17 DataWorks Copilot

DataWorks Copilot is a new generation of AI assistant integrated in DataWorks. You can use natural language to communicate with DataWorks Copilot or obtain immediate assistance on your operation pages. This greatly improves the efficiency of data development and analysis. The core capabilities of DataWorks Copilot are provided in two interactive modes to meet your needs in different scenarios: Copilot Chat (conversational AI): an all-round conversation window that is your "command center" for complex issue discussion, task planning, and automated process execution. Copilot AI in place (Immersive AI): a "personal assistant" that is seamlessly embedded in your daily operation pages, providing contextual, intelligent assistance in place when you need it most.

| Feature | Description |
|---|---|

| Copilot | The following features are supported: Code generation Automatically converts natural languages that you enter into SQL statements. Code rewrite Rewrites the specified code through natural language interaction. Code correction Searches for and fixes errors in the specified code snippet. You can also start Copilot Chat with a few clicks to fix syntax errors in the editor. Comment generation Generates comments for specified SQL statements to improve the readability of the SQL statements. Code explanation Interprets specified SQL statements to improve the readability of the SQL statements. Code-related Q&A Provides explanations and usage examples for SQL syntax or MaxCompute functions you inquire about, helping you deepen your understanding of SQL and its functions. Code optimization Optimizes the selected SQL code. DataWorks Copilot helps you simplify the code logic, improve the code running efficiency, and reduce the load on your database. Code testing Generates a test solution and test code based on the selected SQL code. This helps you verify whether each part of the task code runs as expected. Quick table search Searches for required tables based on entered keywords. |
|---|---|
| SQL editor | Provides enhanced features for the SQL editor, including SQL generation, SQL error correction, comment generation, and SQL rewrite. |

#### 1.4.18 Internationalization

This topic describes the internationalization progress of DataWorks. The DataWorks console supports the following languages: simplified Chinese, traditional Chinese, and English. You can switch among the languages as needed.
