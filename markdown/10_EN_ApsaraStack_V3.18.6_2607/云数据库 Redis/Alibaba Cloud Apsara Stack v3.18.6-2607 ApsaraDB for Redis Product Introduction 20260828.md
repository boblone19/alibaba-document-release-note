---
title: "Alibaba Cloud Apsara Stack v3.18.6-2607 ApsaraDB for Redis Product Introduction 20260828"
product_version: "V3.18.6_2607"
doc_version: "20260828"
pdf_pages: 17
source_pdf: "7110e9f650a57c19_Alibaba Cloud Apsara Stack v3.18.6-2607 ApsaraDB for Redis Product Introduction 20260828.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/3816%202607/pdf%203/%E4%BA%91%E6%95%B0%E6%8D%AE%E5%BA%93%20Redis/Alibaba%20Cloud%20Apsara%20Stack%20v3.18.6-2607%20ApsaraDB%20for%20Redis%20Product%20Introduction%2020260828.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes)
---

# Alibaba Cloud Apsara Stack v3.18.6-2607 ApsaraDB for Redis Product Introduction 20260828

## Table of Contents

- 1 Product Details
- 2 Benefits
- 3 Common scenarios
- 4 Functions and features

ails

## 1 Product Details

Tair (Redis OSS-compatible) supports various architectures and provides persistent data storage, high availability, scalability, and intelligent O&M.

**Flexible Architecture**

**Standard Architecture**

Primary and secondary nodes synchronize data in real time. The primary node provides service access, and the secondary node provides high availability (HA). If the primary node fails, the system switches to the secondary node to take over the services and ensure service stability. The standard architecture is suitable for the following scenarios: Businesses that require high Redis protocol compatibility. Businesses that use Redis for persistent data storage. Scenarios where the performance pressure on a single Redis instance is manageable. Scenarios that use simple Redis commands and involve fewer complex operations, such as sorting and calculations.

**Cluster Architecture**

The cluster architecture consists of proxy nodes, data shards, and configuration server components. You can scale out horizontally by adding data shards. Each data shard uses a dual-replica, high-availability architecture deployed on different machines. If the primary node fails, the system automatically performs a failover to the secondary node to ensure high service availability. The cluster architecture is suitable for the following scenarios: Scenarios with large data volumes. Scenarios with high queries per second (QPS) for read and write requests. Throughput-intensive, high-performance application scenarios.

**Standalone Instance**

A standalone instance uses a single-node deployment and does not have a secondary node for real-time data synchronization. Because this architecture has only one database node, it does not have a hot replica for high availability (HA). If the database node fails, the data on the node is lost. The system then relaunches a new Redis process without any data. After the node fails and the service is automatically switched over, the application must prefetch the data.

**Warning**

Standalone instances do not guarantee data availability or service continuity. Before you choose this architecture, you must be aware of the risks. Do not use standalone instances in production environments. Standalone instances do not support features such as automatic or manual backup, or offline full key analysis. If you require data reliability, use a high-availability architecture. Standalone instances are suitable for the following scenarios: Standalone instances offer a significant price advantage and are highly cost-effective. They are suitable for pure caching scenarios where data reliability requirements are not high. ails

**Read/Write Splitting Architecture**

The read/write splitting architecture consists of proxy nodes, primary and secondary nodes, and read-only nodes. Read-only nodes use a chained replication architecture. You can increase the number of read-only nodes to linearly scale the overall performance of the instance. The read/write splitting architecture is suitable for the following scenarios: Scenarios with high QPS for read requests, such as scenarios that involve centralized hot spot data. Scenarios that require high Redis protocol compatibility to avoid the limitations of the cluster architecture.

**Data Security**

**Data Backup and Recovery**

Backup: Data persistence is achieved based on RDB snapshot storage. The system automatically backs up data from the secondary node based on the default policy, which is one backup per day. You can modify the backup policy as needed or manually initiate a temporary backup. Recovery: You can restore data to the current instance or a new instance from a specified backup set. When you restore data to a new instance, the data in the new instance is consistent with the data in the backup set. This feature can be used for data recovery, rapid business deployment, or data validation. Download backup files: Backup files are retained for 7 days. To archive backups for a longer period, for example, for regulatory or information security purposes, you can download the backup files to local storage.

**Multilayer Network Security Protection**

Virtual private cloud (VPC): Tair supports VPCs. Different VPCs are isolated at Layer 2 to provide high security and performance. Anti-DDoS: Tair supports Anti-DDoS to monitor and purge volumetric attacks in real time. IP address whitelist: You can configure whitelists that contain more than 1,000 IP addresses to block unauthorized access. You must configure a whitelist before you connect to an instance. Password authentication: Tair supports password authentication for secure and reliable access. You can create up to 20 accounts for a single instance and set permissions for each account. This allows for flexible instance management and helps minimize the risk of misoperations. SSL encryption: Tair supports Secure Sockets Layer (SSL) encryption. After you enable this feature, you must install an SSL CA certificate on your application. This encrypts network connections at the transport layer to enhance data communication security and ensure data integrity.

**Deep Kernel Optimization**

The Alibaba Cloud expert team performs deep kernel optimization on the Redis source code to prevent memory overflow and fix security vulnerabilities.

**High Availability**

**Dual Replicas**

ails A data shard consists of dual replicas, which are primary and secondary nodes. The primary and secondary nodes synchronize data in real time using RDB and AOF. The primary node provides external service access, and the secondary node provides high availability (HA). If the primary node fails, the system performs a failover to the secondary node to ensure service stability.

**Redundancy and Automatic Detection**

System components use a redundant design to prevent single points of failure and ensure that services can continue to run even if a node fails. The system automatically detects hardware failures. If a failure occurs, the system performs a failover and restores the service within seconds.

**Scalability**

After you create an instance, if your business volume changes and the instance performance becomes insufficient or excessive, you can change the instance configuration. You can adjust the instance architecture or memory specifications to meet the performance and capacity requirements of different scenarios.

**Intelligent O&M**

**Performance Monitoring Platform**

Tair provides a wide range of performance monitoring metrics, such as CPU utilization and the number of connections. You can query monitoring data for a specified period within the last month. This helps you understand the operational status of your instance and trace issues.

**Visualization Management Platform**

Tair provides a web-based visualization management console. The console provides a variety of O&M and management features, such as data backup and parameter settings. This helps you manage instances in a convenient and visualized manner.

**Database Kernel Version Management**

Tair (Redis OSS-compatible) is continuously optimized at the kernel level to fix security vulnerabilities and improve service stability. You can use the minor version upgrade feature in the console to upgrade the kernel to the latest version with a single click.

## 2 Benefits

Tair (Redis OSS-compatible) provides features such as ultra-high performance, elastic scaling, resource isolation, high data security, high availability, and ease of use.

**Ultra-high performance**

Supports cluster instances with a memory capacity of 128 GB or larger. The instances can meet large capacity and high performance requirements. Supports master-replica instances with a maximum memory capacity of 32 GB. The instances can meet general capacity and performance requirements. Supports CPUs, disks, memory, and network interface controllers (NICs) of different specifications in a cluster without affecting the operational performance of the cluster. This ensures compatibility with your existing devices.

**Elastic scaling**

Easy scaling: You can scale the instance storage capacity with only a few clicks in the Tair (Redis OSS-compatible) console. Online scaling: You can scale the instance storage capacity without service interruption.

**Resource isolation**

Supports instance isolation. This ensures the stability of individual services. Supports multi-tenant isolation. Each instance can use exclusive resources, such as CPU, memory, and I/O resources, and disk capacity. Supports multi-tenant parallel execution on a cluster by using multiple instances. Tasks from tenants are submitted to queues in different instances for execution. Tair (Redis OSScompatible) isolates resources among tenants based on different instances.

**Data security**

Data persistence: Tair (Redis OSS-compatible) provides high-speed data read/write capabilities and supports data persistence by using a hybrid storage of memory and disks. Tair (Redis OSS-compatible) allows you to load data from a persistent database into a cache database. Master/replica backup: Tair (Redis OSS-compatible) maintains two backup copies of all data on a master node and a replica node to prevent data loss. Access control: Tair (Redis OSS-compatible) supports password authentication to ensure secure and reliable access to databases. Data transmission encryption: Tair (Redis OSS-compatible) supports encryption based on SSL and Secure Transport Layer (TLS) to secure data transmission.

**High availability**

Master-replica architecture: Each instance runs in a master-replica architecture to eliminate the risk of single points of failure (SPOFs) and ensure high availability. Automatic failure detection and recovery: The system automatically detects hardware failures and performs a failover within seconds. This minimizes the impacts of sudden hardware failures. Automatic fault tolerance: Tair (Redis OSS-compatible) supports automatic fault tolerance for server disk failures in a cluster and hot swapping of disks. If a disk fails, services can be recovered within 2 minutes.

**Ease of use**

Supports Redis commands. You can use a Redis client to connect to a Tair (Redis OSScompatible) instance and manage data. Supports multiple commands in each query.

**Permission management**

Supports data access permission management. Permissions include logon permissions, table creation permissions, read and write permissions, and whitelist control permissions. Allows you to log on to the Tair (Redis OSS-compatible) console to manage permissions, including setting administrative permissions. Provides a unified permission management feature. This feature allows you to manage various permissions for each component of the system in the Tair (Redis OSS-compatible) console. This isolates common users from internal permission management details, simplifies the permission management for administrators, and improves user experience. Allows you to manage multiple tenants in a centralized manner in the Tair (Redis OSScompatible) console. For example, you can dynamically configure and manage tenant resources, isolate resources, view statistics on resource usage, and manage tenants of multiple levels.

**Scheduling**

Supports multi-tenant scheduling across multiple clusters and resource pools. enarios

## 3 Common scenarios

Tair (Redis OSS-compatible) is ideal for use in industries such as gaming, live streaming, and e-commerce.

**Gaming industry applications**

Tair (Redis OSS-compatible) can serve as an important architecture component in the gaming industry.

**Scenario 1: Use Redis as a storage database**

Gaming applications can be deployed in a simple architecture in which the main program runs on an Elastic Compute Service (ECS) instance and business data is persistently stored in Redis. Tair (Redis OSS-compatible) can be used for persistent storage. It uses the masterreplica architecture to implement redundancy.

**Scenario 2: Use Redis as a cache to accelerate access to applications**

You can use Redis as a cache to accelerate connections for applications and use an ApsaraDB RDS instance as a backend database for data storage. The high availability of Redis is essential. If your Redis service becomes unavailable, backend databases may be overwhelmed by the requests sent from applications. Tair (Redis OSScompatible) uses the master-replica architecture to ensure high availability. In this architecture, the master node provides services for your business. If this node fails, the system automatically switches workloads to the replica node. The complete failover process is transparent.

**Live streaming applications**

In most cases, live streaming service heavily relies on Tair (Redis OSS-compatible) to store user data and relationship information.

**High availability**

Tair (Redis OSS-compatible) can be deployed in a master-replica architecture to significantly improve service availability.

**High performance**

Tair (Redis OSS-compatible) provides cluster instances to overcome the performance bottleneck of the Redis single-thread mechanism. Cluster instances can effectively handle traffic spikes and support high performance.

**High scalability**

Tair (Redis OSS-compatible) allows you to deal with traffic spikes during peak hours by scaling out an instance with a few clicks. The scale-out is completely transparent to users.

**E-commerce applications**

In the e-commerce industry, Tair (Redis OSS-compatible) is widely used in modules such as commodity presentation and recommendation.

**Scenario 1: online shopping systems**

An online shopping system is likely to be overwhelmed by user traffic during large promotional activities such as flash sales. Most databases cannot handle the heavy load. To resolve this issue, you can use Tair (Redis OSS-compatible) for persistent storage.

**Scenario 2: inventory management systems that support stocktaking**

enarios A Tair (Redis OSS-compatible) instance can be used to count the inventory, and an ApsaraDB RDS instance can be used to store item quantity statistics. This way, the Tair (Redis OSScompatible) instance reads quantity statistics, and the ApsaraDB RDS instance stores quantity statistics. The Tair (Redis OSS-compatible) instance is deployed on a physical server, and the system provides high data storage capacity based on high-performance SSDs.

## 4 Functions and features

This topic describes the functions and features of Alibaba CloudTair (Redis OSS-compatible) to help you quickly understand its capabilities.

| Feature category | Feature | Description |
|---|---|---|
|   | Create an instance. | You can create instances on the console. |
|   | Change the configuration of an instance. | You can change the instance configuration. You can select the architecture type and instance type. |
|   | Change passwords. | You can change the password of an instance. |
|   | Configure a maintenance window. | You can modify the default maintenance window to perform maintenance on Tair (Redis OSS- compatible) instances during off- peak hours. |
|   | Upgrade the minor version of an instance. | The kernel can be continuously optimized to fix security vulnerabilities, and improve service stability. You can upgrade the kernel to the latest version (minor version) of a Tair (Redis OSS- compatible) instance with a few clicks in the Tair (Redis OSS- compatible) console. |
|   | Clear data. | The system allows you to clear data of Tair (Redis OSS-compatible) instances. You can choose to clear all data or only expired data of a Tair (Redis OSS-compatible) instance. |
|   | Release an instance. | You can release a Tair (Redis OSS- compatible) instance at any time. |

| Instance management |   |   |
|---|---|---|
|   | Manage accounts. | Tair (Redis OSS-compatible) allows you to create up to 20 accounts per instance. You can grant appropriate permissions to these accounts based on usage, enabling more flexible instance management and minimizing the risk of misoperations. |
|   | Restart an instance. | You can restart a Tair (Redis OSS- compatible) instance from the instance list on the console. |
|   | Export an instance list. | You can export the instance list from the console to manage the instances offline. |
|   | Manage tags. | When you have a large number of instances, you can create tags and add them to instances for classification. You can later filter instances by tag. |
|   | Configure parameters. | You can customize certain instance parameters. |
|   | Standalone instance | Maximize cost reduction. The cloud- native version provides a standalone mode with no high- availability replica overhead. It is ideal for non-core scenarios such as development, testing, and cache warmup. |
|   | Dedicated instance | The cloud-native version supports dedicated instances with fully exclusive CPU, memory, and network resources. This ensures stable latency and linear throughput growth in high- concurrency hotspot scenarios. |
|   | Convert instances from the classic edition to cloud- native. | You can convert classic edition instances to cloud-native edition. The cloud-native deployment model supports higher versions of Tair (Redis OSS-compatible) and offers more flexible architecture configurations. |

| Connection management | View endpoints. | You can view the internal and public endpoints of Tair (Redis OSS- compatible) instances on the console. |
|---|---|---|
|   | Apply for a public endpoint for an instance. | The system supports internet access. |
|   | Change endpoints. | You can change the internal and public endpoints of instances. |
| Security settings | Configure an allowlist. | You can configure an allowlist. Proper use of the allowlist provides a high level of access security for Tair (Redis OSS-compatible) instances. We recommend that you maintain the allowlist regularly. |
|   | Configure SSL encryption. | The SSL encryption feature encrypts network connections at the transport layer to improve data and ensure data integrity during communication. |
|   | Use Transparent Data Encryption (TDE). | You can use the TDE feature to encrypt and decrypt Redis Database (RDB) data files. |
|   | IP type and allowlist | The system can assign IPv4-only or dual-stack (IPv4/IPv6) addresses to meet different network environment requirements. In dual-stack mode, you can configure independent IPv6 allowlists for precise access control. |
| Performance monitoring | View monitoring data. | You can query the monitoring data of Tair (Redis OSS-compatible) for a specified time range within the past month. |
|   | Customize metrics. | You can select the metrics to display on the performance monitoring page of the Tair (Redis OSS-compatible) console. |
|   | Change the monitoring frequency. | You can adjust the frequency at which monitoring data is collected. |

| Cloud monitoring | View a monitoring dashboard. | You can view metrics from Cloud Monitor to quickly identify operational issues. |
|---|---|---|
|   | Create an alarm rule. | You can create alarm rules. Then the system will trigger alarms based on predefined thresholds for cloud product monitoring metrics and notify relevant users promptly. |
|   | View alarm history. | After an alarm occurs, you can view alarm history by cloud product, cloud service instance, alarm level, and more. You can also export the alarm history for local data analysis. |
| Backup and recovery | Automatic backup | Tair (Redis OSS-compatible) uses RDB snapshots to back up data on replica nodes. The backup process does not negatively impact your instance performance. You can configure a custom backup policy on the console. |
|   | Manual backup | You can initiate a manual backup task at any time on the console. |
|   | Download backup. | You can copy URLs on the console to download database backup files locally for long-term storage. |
|   | Data restoration | You can restore data from a specified backup set to the current instance. |
|   | Clone instances. | You can create a new instance from a specified backup set. The new instance contains identical data. This feature is ideal for data restoration, rapid workload deployment, or data validation. |
|   | Performance trends | You can monitor the basic performance and trends of Tair (Redis OSS-compatible) instances over a specific time period. This includes CPU usage, memory used, Query Per Second (QPS), total connections, response time, network traffic, and keys hit. |

| CloudDBA |   |   |
|---|---|---|
|   | Top key statistics | You can view real-time and historical big keys and hot keys in the instance, including keys with large element counts and frequently accessed keys. This helps you effectively resolve instance performance issues. |
|   | Real-time performance | You can view the real-time performance of Tair (Redis OSS- compatible) instances. This includes CPU usage, memory usage, QPS, network traffic, server information, key information, client information, and connection information. |
|   | Instance sessions | You can view real-time session information between Tair (Redis OSS-Compatible) instances and clients, including client information, executed commands, and connection duration. You can also terminate abnormal sessions as needed. |
|   | Slow queries | You can view slow log details to monitor and analyze slow query issues. |
|   | Offline key analysis | You can use the Offline Key Analysis feature to analyze backup files of Tair (Redis OSS-compatible). This quickly identifies big keys in the instance and helps you understand the key usage and distribution in the memory, key expiration time, and more. This provides data support for your optimization operations and helps you avoid issues such as insufficient memory and performance degradation caused by key skew. |
|   | Diagnostic reports | You can initiate a diagnosis of the instance's operational status for a specified time period to evaluate the instance's health from multiple aspects, such as performance levels, access skew, and slow logs. This allows you to quickly identify anomalies. |

| Disaster recovery architecture | Migrate availability zones (AZs). | You can perform visual migration for single- or dual-zone deployments, enhancing capabilities for same-city and cross- region disaster recovery. |
|---|---|---|
| Audit log | Audit log | You can view SQL details and perform periodic SQL audits. |
