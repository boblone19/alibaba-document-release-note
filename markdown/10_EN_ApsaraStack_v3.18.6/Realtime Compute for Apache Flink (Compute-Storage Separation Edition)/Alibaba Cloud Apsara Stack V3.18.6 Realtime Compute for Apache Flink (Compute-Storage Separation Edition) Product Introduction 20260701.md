---
title: "Realtime Compute for Apache Flink (Compute-Storage Separation Edition) Product Introduction 20260701"
product_version: "V3.18.6"
pdf_pages: 13
source_pdf: "Alibaba Cloud Apsara Stack V3.18.6 Realtime Compute for Apache Flink (Compute-Storage Separation Edition) Product Introduction 20260701.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/v3.18.6%E7%89%88%E6%9C%AC%E6%96%87%E6%A1%A3/%E5%AE%9E%E6%97%B6%E8%AE%A1%E7%AE%97FLink/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.6%20Realtime%20Compute%20for%20Apache%20Flink%20%28Compute-Storage%20Separation%20Edition%29%20Product%20Introduction%2020260701.pdf"
converter: line-classifier (PyMuPDF)
---

# Realtime Compute for Apache Flink (Compute-Storage Separation Edition) Product Introduction 20260701

Realtime Compute for Apache Fli nk (Compute-Storage Separation

## Product details

Alibaba Cloud Realtime Compute for Apache Flink supports features including data ingestion and storage, data development, data O&M, and automatic tuning.

**Data ingestion and storage**

A prerequisite for any big data analysis system is that data must be ingested into the big data system. To maximize compatibility with customers' existing streaming storage systems, Alibaba Cloud Realtime Compute for Apache Flink integrates with multiple upstream streaming storage services, such as DataHub, Log Service, Tablestore, and Message Queue. Customers can leverage their existing streaming data storage without needing to perform separate data ingestion or data integration tasks.

**Data development**

Flink SQL syntax checking After modifying text in the IDE, click **Validate** to trigger SQL syntax checking. If errors are found, the IDE displays the line number, column number, and reason for each error. Flink SQL code hinting When writing Flink SQL, the IDE provides hints for keywords, built-in functions, and SQL auto-completion. Flink SQL syntax highlighting The IDE applies distinct colors to Flink SQL keywords to visually differentiate structural elements of the SQL statement. DDL generation assistance Generating DDL statements for Realtime Compute typically involves mechanical translation — manually converting the DDL of a target data store into Realtime Compute-compatible DDL. Realtime Compute provides tools to assist with DDL generation, reducing the complexity of manually writing streaming jobs, lowering the error rate in SQL authoring, and ultimately improving productivity for real-time computing tasks. Users can select a template on the development page to auto-generate DDL statements. Running the template then generates and displays the corresponding table schema in the Schema view. Support for standard SQL Use standard SQL to perform real-time data cleansing, statistical aggregation, and data analysis. The system supports common aggregate functions and enables join queries between streaming and static data.

**Data O&M**

Alibaba Cloud Realtime Compute provides O&M and monitoring capabilities including job status, data throughput curves, failover events, checkpoints, JobManager metrics, TaskExecutor metrics, lineage tracking, and property parameter inspection.

**Automatic tuning**

This feature helps users optimize job parallelism and resource allocation more effectively, provided that all operators and upstream/downstream components of the streaming job meet performance and stability requirements. It globally optimizes job performance to resolve tuning issues such as insufficient throughput, end-to-end backpressure, and resource waste.

**High availability and high security**

Realtime Compute for Apache Fli nk (Compute-Storage Separation Built on a compute-storage separation architecture, the system support same-city high availability disaster recovery and highly secure multi-tenant isolation. Realtime Compute for Apache Fli nk (Compute-Storage Separation

## Benefits

Compared with other realtime compute products, Alibaba Cloud Realtime Compute for Apache Flink offers strong competitiveness. You can leverage the following advantages to solve your business challenges in realtime big data analysis.

**Powerful realtime processing capabilities**

Alibaba Cloud Realtime Compute integrates multiple end-to-end features to simplify end-toend realtime computing development for users: Powerful realtime compute engine: Alibaba Cloud Realtime Compute provides standard Flink SQL and supports automatic recovery in various failure scenarios to ensure data processing accuracy during failures. Supports multiple built-in functions for strings, time, statistics, and other types. Enables precise control of computing resources to fully guarantee job isolation. Provides compute engines for Flink 1.17, Flink 1.15, and Flink 1.13. Python jobs (ARM) support only Flink 1.17. Key performance metrics exceed those of open-source Flink by 3 to 4 times. Data compute latency is optimized to the second or even millisecond level. A single job can achieve throughput at the million level, and a single cluster can scale to thousands of nodes. Deeply integrates with various cloud data storage systems, including DataHub, Simple Log Service, ApsaraDB RDS, Tablestore, AnalyticDB for MySQL. No additional data integration work is required. Alibaba Cloud Realtime Compute for Apache Flink can directly read from and write to these products.

**Excellent streaming development experience**

Supports standard Flink SQL. Realtime Compute uses built-in functions for strings, time, statistics, and other calculations to replace inefficient and complex Flink Java APIs with simple Flink SQL, enabling more BI and operations personnel to perform realtime big data analysis and processing using basic Flink SQL, thus democratizing realtime big data processing. The current external interface of Realtime Compute is defined as Flink SQL/UDF. It provides an all-in-one development tool for streaming data analysis, statistics, and processing. The target users are primarily data warehouse developers and data analysts who prefer not to engage deeply in low-level code development and instead wish to write simple realtime SQL to fulfill their streaming data analysis tasks. Provides an end-to-end streaming data processing solution Includes auxiliary suites for different stages such as data development, data O&M, and monitoring and alerting. Supports automatic fault tolerance for server hard disk failures within the cluster Supports hot-swappable hard disks. Business recovery time for failed disks is less than two minutes. The platform adopts a multi-node cluster architecture Management nodes within the platform support high availability. Routine O&M management node failures do not affect normal business operations.

**Low labor and cluster costs**

Realtime Compute for Apache Fli nk (Compute-Storage Separation The highly optimized SQL execution engine generates compute tasks that are more efficient and cost-effective than manually written native Storm tasks. Whether in development cost or runtime cost, Alibaba Cloud Realtime Compute is significantly lower than open-source streaming frameworks. By using it, you can focus entirely on your business and rapidly achieve market goals without needing to write complex Java code for Storm tasks. Alibaba Cloud assumes all costs related to debugging, testing, tuning, deployment, and subsequent O&M of open-source software such as Storm and Zookeeper. Without affecting runtime performance, the system supports inconsistent CPU, hard disk, memory, and NIC specifications within a single component cluster, maximizing compatibility with existing equipment. Realtime Compute for Apache Fli nk (Compute-Storage Separation

## Scenarios

Alibaba Cloud Realtime Compute for Flink is suitable for scenarios such as real-time extract, transform, and load (ETL) and index building, real-time statistics and analytics, real-time machine learning platforms, and real-time event processing.

**Real-time ETL & index building**

Realtime Compute uses its various data tunnels and flexible SQL processing capabilities to clean, merge, and structure streaming data in real time. Realtime Compute effectively supplements and optimizes offline data warehouses by providing a channel for real-time data transmission.

**Real-time statistics & analytics**

Realtime Compute collects and processes streaming data sources, and monitors and displays various metrics in real time. This enables real-time, data-driven operations. For example: Real-time statistics for page views (PVs) and unique visitors (UVs). Statistics on the average traffic flow through a checkpoint every 5 minutes. Statistics and display of dam pressure data.

**Real-time machine learning platform**

This platform helps data analysts and application developers complete the end-to-end process, from data processing and feature engineering to model training and prediction.

**Real-time event processing**

You can detect and analyze system, user, and business behavior in real time to identify malicious activities. For example: Display user behavior dashboards, such as transaction and user dashboards. A site-wide transaction curve graph helps operations and technical staff understand the current transaction status. If transactions fluctuate abnormally, such as with a sudden drop, an alert is triggered immediately. This allows staff to investigate the issue and reduce the business impact. Monitor major sales promotions, such as Double 11 and 618, in real time. Operations staff can use real-time metrics to quickly decide whether to change the promotion strategy. Set up rule-based alerts to detect specific patterns of financial theft in online payments.

| Feature category | Feature | Sub- feature | Description |
|---|---|---|---|
| Console | Job manageme nt | DataStream job | Supports DataStream jobs. |
|  |  | SQL job | Supports SQL jobs. |
|  |  | SQL editor | Provides an SQL editor. |
|  |  | UDF | Supports user-defined functions (UDFs). |
|  |  | Peak job throughput | A single job in a single cluster can reach a peak throughput of up to 8 million records per second. |
|  |  | Job resource and parallelism tuning | Supports manual and intelligent tuning for job resources and parallelism: Manual tuning: Provides operator-level settings to adjust resources such as CPU, memory, and parallelism. Intelligent tuning: You can adjust global job resources, and a backend AI system automatically optimizes resource allocation based on the job's real-time operational status. |
|  |  | StreamSQL developmen t kit | Provides a comprehensive StreamSQL development kit with auto-complete, syntax highlighting, and syntax checking. |
|  |  | Concurrent job capacity | A single cluster supports at least 2,400 concurrent jobs. |
|  |  | Complex event processing (CEP) with dynamic rules | Complex Event Processing (CEP) with dynamic rules decouples developers from policy analysts by separating the application framework from business rules. Flink automatically loads updated rules to ensure business continuity. |

Realtime Compute for Apache Fli nk (Compute-Storage Separation

## Features

This topic describes the features of Real-time Compute for Apache Flink.

|  |  | Fast recovery from single- point failures | Jobs recover quickly from a single checkpoint after a failure. |
|---|---|---|---|
|  |  | Job runtime parameters | Runtime parameters for stream jobs let you configure the Time to Live (TTL) for state data. |
|  | Metadata manageme nt | Built-in catalog for Paimon | Supports Apache Paimon table creation through the built-in catalog. |
|  | Built-in connectors | Built-in connectors | Provides more than 30 built-in connectors for a wide range of data sources. |
|  | Custom connectors | User- defined connectors | Users can upload custom connectors for specific data sources. |
|  | Change data capture (CDC) | Log-based automatic metadata discovery and managemen t | Supports automatic metadata discovery and management through a catalog. Combined with the Create Table As Select (CTAS) syntax, you can synchronize data and automatically propagate schema changes with a single line of SQL. |
|  |  | Incremental synchroniza tion | Supports incremental data synchronization. |
| Connectors | Flink CDC |  |  |
|  |  | Breakpoint resume | Supports resuming data synchronization from breakpoints. |
|  |  | Full synchroniza tion | Supports full data synchronization. |
|  |  | Full and incremental integrated reads | Enables unified data synchronization for both full and incremental reads. |
|  |  | CTAS for database and table sharding synchroniza tion | Use CTAS syntax with regular expressions to merge and synchronize data from sharded databases and tables into a downstream data warehouse. |

Realtime Compute for Apache Fli nk (Compute-Storage Separation

|  |  | Dynamic table addition | Dynamically add new source tables to a synchronization job without affecting existing table states or requiring a full resynchronization. |
|---|---|---|---|
|  |  | CDAS for full database synchroniza tion | Enables full database synchronization using CDAS syntax and a catalog. |
| Scalability | Compute | Cluster scaling capability | Leverages a distributed computing framework to provide stream processing services that can be scaled on demand. A compute cluster can scale up to 2,400 nodes. |
|  | cluster scale |  |  |
|  | Cross-chip architecture | Mixed x86 deployment | Supports mixed deployments of Intel and Hygon CPUs within the same cluster. |
|  |  | Heterogene ous cross- chip deployment | Supports mixed deployments of heterogeneous x86 and ARM architectures within the same cluster. |
|  | Scaling | Hot scaling support | Supports on-demand hot scaling (scaling up or down) of resources within a single cluster without affecting online services. |
| O&M and monitoring | Fault detection | Resource- level fault detection and automatic job migration | Provides fault detection and automatic job migration for high CPU, I/O, memory, and disk utilization. |
|  | Online job debugging | Non- disruptive online job debugging | Provides online debugging for stream computing jobs without disrupting the production environment. |
|  | Job O&M dashboard | Job O&M dashboard | The job O&M dashboard displays underlying metrics, such as traffic and resource usage, for you to monitor job health. |
|  | Capacity monitoring | Capacity level monitoring and managemen t | Supports capacity usage monitoring and management. |

Realtime Compute for Apache Fli nk (Compute-Storage Separation

| Security | Secret manageme nt | Secret managemen t for SQL jobs | Supports secret management for SQL jobs. |
|---|---|---|---|
|  | Access control | IP address range for allowlist | Lets you configure access control allowlist using IP address ranges. |
|  | Log auditing | Search operation logs | Search operation logs through the visual interface in the log center. |
| High availability | Disaster recovery | Intra-city disaster recovery | Supports namespace-level intra-city disaster recovery. You can also create non-disaster recovery instances in the secondary data center. |
| Network | Service IP address | Dual-stack support for service virtual IP (VIP) addresses | Supports IPv6 and IPv4 in dual-stack mode for service virtual IP (VIP) addresses. |

Realtime Compute for Apache Fli nk (Compute-Storage Separation
