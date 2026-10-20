---
title: "Elasticsearch User Guide 20260629"
product_version: "V3.18.6"
pdf_pages: 186
source_pdf: "e3eb3750a3f2a431_Alibaba Cloud Apsara Stack V3.18.6 Elasticsearch User Guide 20260629.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/v3.18.6%E7%89%88%E6%9C%AC%E6%96%87%E6%A1%A3/%E6%A3%80%E7%B4%A2%E5%88%86%E6%9E%90%E6%9C%8D%E5%8A%A1%20Elasticsearch%E7%89%88/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.6%20Elasticsearch%20User%20Guide%2020260629.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes)
---

# Elasticsearch User Guide 20260629

## Table of Contents

- 1 What is Alibaba Cloud Elasticsearch?
- 2 Kernel version release notes
- 3 Limits and configuration suggestions
- 4 Terms
- 5 Preparations
  - 5.1 Sign in to the Alibaba Cloud Elasticsearch console
  - 5.2 View information on the Overview page
  - 5.3 Create a cluster
  - 5.4 Access a cluster
  - 5.5 View cluster information
- 6 Quick start
  - 6.1 Create an index
  - 6.2 Manage documents
    - 6.2.1 Create a document
    - 6.2.2 Update a document
    - 6.2.3 Retrieve a document
    - 6.2.4 Search for documents
    - 6.2.5 Perform a complex search
    - 6.2.6 Analyze document statistics
    - 6.2.7 Delete a document
    - 6.2.8 Delete an index
- 7 Manage clusters
  - 7.1 Manage clusters
    - 7.1.1 Customize the columns displayed in the cluster list
    - 7.1.2 Export a list of Elasticsearch clusters
    - 7.1.3 Refresh instance
    - 7.1.4 Modify the name of a cluster
    - 7.1.5 Manage cluster tags
    - 7.1.6 Restart an instance or node
    - 7.1.7 Releasing an instance
  - 7.2 View cluster information
    - 7.2.1 View instance information
    - 7.2.2 View tasks
    - 7.2.3 View the logs of a node
  - 7.3 Scale in or out a cluster
  - 7.4 Configuration and management
    - 7.4.1 Configure clusters
    - 7.4.2 Plugin configuration
      - 7.4.2.1 Supported plugins
        - 7.4.2.1.1 Elasticsearch plugins
        - 7.4.2.1.2 Kibana plugins
        - 7.4.2.1.3 OpenSearch plugins
        - 7.4.2.1.4 Dashboard plugins
      - 7.4.2.2 Install or uninstall plug-ins
    - 7.4.3 Security settings
    - 7.4.4 Data backup
      - 7.4.4.1 Manual backup and restoration
      - 7.4.4.2 Automatic backup
  - 7.5 Kibana console
    - 7.5.1 Log in to the Kibana console
    - 7.5.2 Modify the Kibana configuration
  - 7.6 Dashboards console
    - 7.6.1 Log on to the Dashboards console
    - 7.6.2 Modify Dashboards configuration
- 8 Using plugins
  - 8.1 Work with Elasticsearch plug-ins
    - 8.1.1 Use a-pack-xdcr for cross-cluster index replication
    - 8.1.2 Synchronize index data across clusters with the xdcr plugin
    - 8.1.3 Use the opendistro_sql plug-in to query cluster data by executing SQL statements
    - 8.1.4 Use the vector search plugin (aliyun-knn)
    - 8.1.5 Manage index lifecycles with the ISM plugin
    - 8.1.6 Use the opendistro_security plug-in to control permissions
    - 8.1.7 Compress index files with the aliyun-codec plugin
    - 8.1.8 Bulk aggregation with the faster-bulk plugin
    - 8.1.9 Throttle cluster traffic with the aliyun-qos plug-in
  - 8.2 Use OpenSearch plugins
    - 8.2.1 Implement vector search using the opensearch-knn plugin
    - 8.2.2 Replicate indexes across clusters
  - 8.3 Work with Kibana plug-ins
    - 8.3.1 Use the opendistro-alerting plug-in to implement cluster alerting
- 9 Elasticsearch MCP Server

d Elasticsearch?

## 1 What is Alibaba Cloud Elasticsearch?

**Elasticsearch?**

Elasticsearch is a real-time, distributed search and analysis engine based on Lucene. It is a leading open source enterprise search engine available under the Apache license. It provides a distributed service that enables users to store, search, and analyze massive datasets quickly and in near real-time. Elasticsearch is often the core engine for applications that require complex query features and must handle high query volumes. An Elasticsearch cluster is a distributed system composed of multiple nodes. These nodes work together to store data and provide indexing and search capabilities across the entire cluster. To improve horizontal scaling, the system splits large indexes into multiple shards, which are then distributed among the nodes. Elasticsearch also creates replica shards on different nodes to back up data. This process increases high availability, distributes the search workload, and improves concurrent performance. Alibaba Cloud Elasticsearch provides a service that is 100% compatible with open source Elasticsearch. The service supports multiple versions of the open source ES kernel and includes targeted performance optimizations. Alibaba Cloud Elasticsearch also offers many proprietary technologies, such as plugins and features for Chinese tokenization, AISearch, query Quality of Service (QoS), cross-cluster replication, data compression, and aggregated writes. The service provides enterprise-grade capabilities, including zone-disaster recovery for high availability, snapshot backup and recovery, security authentication, visual cluster creation, plugin management, multi-tenancy, and Auto Scaling. In addition to Elasticsearch, Alibaba Cloud also fully supports OpenSearch. The default OpenSearch version provided is 3.1.0. OpenSearch, forked from Elasticsearch 7.10, is a continuously evolving project that aims to provide an open, extensible, and vendor-neutral platform for search and analysis. The Alibaba Cloud OpenSearch service is fully compatible with the open source OpenSearch ecosystem and supports core features such as Dashboards, SQL queries, Piped Processing Language (PPL), Index State Management, and asynchronous search. The service also integrates Alibaba Cloud's security systems, monitoring and alerts, automatic backups, and Auto Scaling capabilities. You can deploy either the Elasticsearch or OpenSearch engine to meet your business needs. This provides a unified, cloud-native management experience with an enterprise-grade Service-Level Agreement (SLA). e notes

## 2 Kernel version release notes

**notes**

This topic describes the kernel version release notes of Apsara Stack Elasticsearch.

| Kernel version | Product | Apsara Stack version | Overview of kernel capabilities | Apsara Stack release date |
|---|---|---|---|---|
| v7.10.0 | Elasticsearch | v3.20.0 | The following capabilities are added: Elasticsearch supports separated storage of cold and hot data. Elasticsearch supports large query isolation. Elasticsearch supports geo-disaster recovery. | 2026-03-20 |
| v3.1.0 | OpenSearch | v3.18.6 | OpenSearch V3.1.0 integrates several key capabilities, including: Performance optimization for vector search and improvements to the Hierarchical Navigable Small World (HNSW) algorithm. Enhanced visualization features in OpenSearch Dashboards. Support for multi-source data association analysis. Enhanced security and fine-grained management capabilities for role- based access control (RBAC). Improved monitoring and alerting features that allow more flexible trigger conditions for custom metrics. Enhanced plug-in ecosystem compatibility to ensure stability and scalability of third-party plug-ins in new kernel versions. This version also improves cluster stability and recovery speed, and optimizes the write throughput in large-scale indexing scenarios. | 2025-12-30 |

> **Important:** You need to purchase OpenSearch kernel features before you can use them.
> By default, OpenSearch Dashboards and OpenSearch use the same kernel version.

on suggestions

## 3 Limits and configuration suggestions

**suggestions**

This topic describes the suggestions on using Elasticsearch and the limits of Elasticsearch. For content not described in this topic, we recommend that you refer to the open source Elasticsearch best practices.

**Suggested cluster versions and specifications**

To ensure the stability of Elasticsearch clusters, we recommend that you select Elasticsearch V7.10.0. In a production environment, we recommend that you create independent master nodes and client nodes. The maximum number of nodes in an Elasticsearch cluster must be five times the number of CPU cores per node. We recommend that you configure at least three data nodes. The node specifications must be at least 8 cores and 32 GiB of memory. Use the same specifications for nodes of the same type. Make sure that the specification difference between different types of nodes is not big. We recommend that you select the Elasticsearch version and specifications by following the best practices in the user-side console, and preferably create Elasticsearch clusters in the user-side console. The O&Mside console is not suggested. During cluster creation, each data node corresponds to a disk at the physical resource layer. You cannot change the disk capacity during the use of the cluster. To improve resource utilization, we recommend that you set the disk type and capacity based on the resources available on the physical machine when you create an Elasticsearch cluster. We recommend that you use SSDs to store data in scenarios other than logging scenarios. The suggested disk type is for reference only. The actual resources available in the console prevail. yoda-LVM storage is not suggested for data nodes because this poses security risks. You can use yoda-LVM storage for master nodes to optimize disk utilization. If you use yoda-LVM storage to store data, we recommend that you set the disk capacity to 100 GiB or less. To improve cluster security, we recommend that you do not select the AnyTunnel network type when you create an Elasticsearch cluster.

**Suggested cluster storage capacity**

The disk space of an Elasticsearch cluster is determined by the following factors: Number of replicas: For production reliability, you must set at least one replica. Indexing overhead: Typically 10% larger than the source data (excluding parameters such as `_all` ). Storage space reserved by the operating system: By default, the operating system reserves 5% of storage space for critical processes, system recovery, and disk fragments. Elasticsearch overheads: Elasticsearch reserves 20% of disk space for internal operations, such as segment merging and logging. Security threshold overheads: Elasticsearch reserves at least 15% of disk space as the security threshold. Therefore, in most cases, the disk space required by an Elasticsearch cluster is about 3.4 times the volume of source data. It can be calculated using the following formula: Minimum required disk space = Volume of source data × (1 + Number of replicas) × (1 + Indexing overheads)/(1 - Security threshold overheads) × Compression ratio/(1 - Space reserved by the operating system)/(1 - Elasticsearch overheads) = Volume of source data × (1 + Number of replica shards) × 1.7 on suggestions The value equals the source data multiplied by 3.4.

> **Note:** We recommend that you disable the **_all** parameter unless you must use this parameter for your business.
> Indexes that have the **_all** parameter enabled incur larger overheads on disk usage. Therefore, we recommend that you assess the disk space by 1.5 times the original value. This indicates that the minimum required disk space is calculated using the following formula: Minimum required disk space = Volume of source data × (1 + Number of replica shards) × 1.7 × (1 + 0.5) = Volume of source data × 5.1.

The specifications of a single Elasticsearch node limit the capacity of a cluster. Based on test results and O&M experience, the following recommendations for the maximum data volume per single node in various scenarios are provided to ensure optimal cluster performance: For general retrieval scenarios, the recommended maximum data volume for a single node is 30 times the memory. In high-performance retrieval scenarios, do not exceed 10 times the node memory. In log retrieval scenarios, do not exceed 50 times the node memory. In extreme scenarios where the cluster performance is relatively low, the volume of data on each node must not exceed 600 times the amount of memory. For example, a node with 16 GiB of memory can load up to 9,600 GiB of data.

> **Important:** If you use clusters of Elasticsearch V5.X or V6.X to store long numbers, such as ID numbers and bank account numbers as strings, the maximum volume of data cannot exceed 25 times the amount of memory. For example, 16 GiB of memory can load up to 400 GiB of data.

In the following table, cluster specifications are used as an example to calculate the maximum disk space per node.

| Specificat ion | Maximu m number of nodes | Maximum disk capacity per node (general) | Maximum disk capacity per node (high-performance) | Maximum disk space per node in logging scenarios |
|---|---|---|---|---|
| 8 CPU cores and 32 GiB of memory | 50 | 960 GiB | 320 GiB | 1.5 TB |
| 16 CPU cores and 64 GiB of memory | 50 | 1.9 TB | 640 GiB | 3 TB |

**Suggestions on cluster shards**

on suggestions The number of shards and the size of each shard determine the stability and performance of an Elasticsearch cluster. This prevents cluster performance degradation caused by numerous shards when it is difficult to define the business scenarios. The following guidelines can help you plan shards. These guidelines are for reference only.

> **Note:** In versions earlier than Elasticsearch V7.X, one index has five primary shards, and each primary shard has one replica shard by default. In Elasticsearch V7.X and later, one index has one primary shard, and the primary shard has one replica shard by default.

For clusters used in a production environment, all indexes must have at least one replica. Before you assign shards, assess the volume of data that you want to store. If the total data volume is large, write a small amount of data to reduce the workloads of your Elasticsearch cluster. In this case, configure multiple primary shards for each index and one replica shard for each primary shard. If both the total data volume and the volume of data that you want to write are small, configure one primary shard for each index and one or more replica shards for each primary shard. We recommend that the size of each shard does not exceed 30 GiB. However, the shard size must be at least several GiB. In log analytics scenarios or scenarios that require extremely large indexes, make sure that the size of each shard does not exceed 100 GiB. The number of shards, including replicas, must be equal to the number of data nodes or a multiple of the number of data nodes. We recommend that you specify a maximum of five shards, including replica shards, for an index on a node. A single node should not have more than 1000 shards. We recommend a maximum of 10 shards per GiB of storage. For example, an 8-core, 32 GiB node can support up to 320 shards.

**Resource limits**

Limits on the number of nodes: 3 to 50

> **Note:** If the cluster contains large numbers of nodes, risks in resource scheduling and cluster stability increase. We recommend that you create multiple production clusters or upgrade nodes.

Limits on the disk space capacity: No more than 20 TB per node Limits on specifications: 8 CPU cores and 32 GiB of memory 16 CPU cores and 64 GiB of memory (suggested specification) 32 CPU cores and 128 GiB of memory

**Limits on features**

Cross-cluster data synchronization—the underlying capability for Multi-zone Disaster Recovery—is supported in Elasticsearch 6.8 and later. When using this feature, ensure that primary and standby clusters have identical specifications and maintain data write rates at or below 3,000 documents per second per shard. Before implementing cross-cluster synchronization for disaster recovery, thoroughly evaluate risks and feasibility based on your business scenario and product disaster recovery constraints. on suggestions In the x86 architecture, Elasticsearch V5.X, V6.X, and V7.X are supported. In the ARM architecture, only Elasticsearch V6.X and V7.X are supported, and Elasticsearch V5.X is not supported. In the ARM architecture, the vector retrieval plug-in and DAMO Academy NLP word segmentation plug-in are not supported. The TransportClient is not supported. Use the RestClient to connect a client to your cluster. To ensure cluster stability, we recommend that you do not return an excessively large document (larger than 10 MB) or an excessive amount of data (more than 10 MB) at a time.

**Availability notes**

Elasticsearch uses a distributed architecture while ensuring the availability of clusters with best efforts. However, in some scenarios, the high-availability architecture still cannot guarantee the availability of clusters. Plans must be provided to guarantee business stability on the business side and platform O&M side. These scenarios include but are not limited to: The cluster needs to frequently perform read, write, or update operations when it is in an unhealthy state or the resource usage of the cluster is consistently high. For example, the CPU usage is 50% or higher, the memory usage is 75% or higher, or the disk usage is 75% or higher. The cluster is improperly used. For example, the cluster contains less than three nodes, resources are deployed in a single zone, no replicas are configured for indexes, custom plug-ins are abnormal, the cluster consistently receives numerous slow queries or slow write requests, or index merging is frequently triggered. Single points of failure (SPOFs) that cannot be automatically identified exist. For example, unresponsive nodes, packet loss, or disk I/O errors exist. Currently, Elasticsearch can identify only node disconnection. Multiple hardware devices are faulty. For example, multiple physical machines or multiple network devices are faulty at the same time. To improve the availability of Elasticsearch clusters, take note of these suggestions: Select proper cluster specifications and set a proper number of nodes to ensure businesses are stable and the resource usage of the cluster is not high. Configure indexes properly, including the number of shards, number of replicas, and index configuration, to ensure the performance and reliability of Elasticsearch. Periodically check the status and health of the cluster, troubleshoot issues at the earliest opportunity, and take necessary approaches. Back up the cluster at a scheduled time and perform disaster recovery drills to prevent data loss and system faults. Configure the monitoring and alerting system properly to identify and respond to exceptions promptly. In dual-zone disaster recovery scenarios, we recommend that you disable automatic index creation and dynamic field recognition. We recommend that you pay close attention to the status of the cluster, and follow the preceding suggestions and the suggestions in the official Elasticsearch documentation to ensure the high availability of Elasticsearch clusters. In addition, we recommend that you pay close attention to the official Elasticsearch documentation and community to obtain the up-todate technical support and best practices.

**A single machine plays multiple roles**

Apsara Stack Elasticsearch relies on the Platform as a Service (PaaS) base, which provides only physical machine capabilities. To improve resource utilization and meet customer demands, Elasticsearch does not strictly limit the anti-affinity of data nodes in Elasticsearch clusters. This means that multiple data nodes may be deployed on the same physical machine. Suggestions: on suggestions To avoid scheduling the primary and replica shards of an index to the same physical machine when multiple data nodes are deployed on the same physical machine, clusters in this scenario are set to the yellow state by default to remind you of the potential risk of data loss caused by physical machine failures. If your cluster enters the yellow state after it is created, check whether multiple data nodes are scheduled to the same physical machine. In this scenario, we recommend that you delete the unhealthy cluster in the production environment and contact the O&M engineer to expand and recreate the cluster. If you must use a cluster that has multiple data nodes deployed on the same physical machine, contact the O&M engineer to manually set the cluster to the green state. In the case that a single machine plays multiple roles, the processing capacity of the cluster is degraded. We recommend that you use the cluster for testing and verification only. Do not use the cluster in production environments. You can choose to spread data nodes when creating a cluster to avoid deploying multiple data nodes on the same physical machine. This improves the availability of your cluster. However, if the number of physical machines is less than the number of data nodes, the cluster fails to be created. Configure data node spreading based on the actual scenario and the platform resources.

**Data reliability**

Apsara Stack Elasticsearch relies on the PaaS storage capability and ensures data reliability based on the primary-replica replication mechanism of Elasticsearch. However, in some scenarios, data reliability cannot be guaranteed. The business side and O&M side need to prepare plans, back up data in a timely manner, and pay close attention to the validity and reliability of backup data. These scenarios include but are not limited to: The storage service is down. For example, multiple hard disks are damaged at the same time, and data stored in the external storage is lost. The storage service is used improperly. For example, the index has no replicas, the asynchronous write feature is enabled for indexes, data loss occurs due to custom plug-ins, and no attribute limit is imposed when multiple data nodes are deployed on a single physical machine. A single physical machine fails when the cluster is unhealthy.

**Security notes**

As a distributed enterprise-class search engine, Apsara Stack Elasticsearch provides certain security measures. However, you still need to take necessary security measures to ensure data security. These measures include but are not limited to: Do not use the AnyTunnel network type. Do not enable Kibana nodes unless it is necessary. Limit access to your Elasticsearch cluster. Do not use the elastic superuser. Create different API accounts for different applications and strictly control the permissions of these accounts. Keep passwords confidential. Do not upload or install any custom plug-ins that may pose security risks. Periodically update the Elasticsearch engine version to install the latest security patches.

**Performance stability**

The performance stability of Elasticsearch depends on multiple factors, including physical resources, the actual business data, and how Elasticsearch is used. For example, the data volume, QPS, query method, and queried content directly affect cluster performance. To improve the performance stability of Elasticsearch clusters, we recommend that you take note of the following suggestions: on suggestions Ensure the cluster capacity. Assess the required cluster capacity and perform stress tests to meet the requirements of business scenarios. Make sure that the resource usage of the cluster is not high. Optimize the index structure. The design of the Elasticsearch index structure has a great impact on performance stability. To optimize the index structure, it is necessary to properly select the field type, mapping method, and tokenizer to avoid problems such as duplicate fields, unnecessary mappings, and wrong tokenizer selection. Optimize the query method. The complexity and use of query statements also affect the stability of the cluster. You need to continuously optimize the query method as needed. Manage the data volume. The volume of data stored on an Elasticsearch cluster is an important factor that affects the performance stability of the cluster. When the data volume is excessively large, the query and write speeds may be adversely affected, and the complexity of cluster maintenance also increases. Therefore, it is necessary to properly manage the data volume, including configuration of data shards and replicas, and clear unneeded data promptly. Periodic maintenance: Periodic cluster maintenance is an important approach to ensure cluster performance stability. Maintenance tasks include useless index and snapshot cleanup, index structure optimization, and node restarts. A variety of factors may affect the performance stability of Elasticsearch clusters. You need to play close attention to the status and resource usage of your cluster when using the cluster, scale out the cluster in a timely manner, and exercise caution when updating the cluster configuration. In addition, make sure that you have traffic throttling, circuit breaking, and service degradation plans to handle cluster stability issues.

## 4 Terms

This article introduces the basic concepts and brief descriptions of common terms encountered in the use of Alibaba Cloud Elasticsearch services.

**Cluster**

A Elasticsearch cluster (also known as an instance) consists of one or more Elasticsearch nodes. All nodes store data together. Each cluster must have a unique cluster name. If a cluster with the same name exists in the same environment, an error may occur.

**Node**

A node is a server in a cluster that stores data and participates in indexing and searching of the cluster. A cluster can have multiple nodes, each of which can play a different role: Data node: a node that stores index data. It is used to add, delete, modify, query, and aggregate documents. Dedicated master node: performs operations on the cluster, such as creating or deleting indexes, tracks which nodes are part of the cluster, and determines which shards are allocated to related nodes. Stable master nodes are very important for the health of the cluster. If there are no dedicated master nodes, all data nodes can act as master nodes. However, if the service load is too high and the load on the data node is high, the primary node becomes unstable. Coordinating node: serves as a traffic ingress and is responsible for forwarding requests to the corresponding data nodes. By using an independent coordinating node, you can reduce the load of data nodes and improve processing performance and service stability. To prevent risks caused by multiple data nodes or dedicated master nodes on a single machine, Alibaba Cloud Elasticsearch set cluster anti-affinity to avoid nodes that are assigned the same role on the same machine. The dedicated master node has strong anti-affinity, and the data node has weak anti-affinity. If there are not enough machines, if multiple data nodes are allocated on the same machine, the cluster status changes to yellow and indexes cannot be allocated. At the same time, when multiple data nodes on a single server occur, there are related configurations that prohibit the primary and secondary shards from being scheduled on a single server to avoid data loss.

**index**

An index is a collection of documents with similar characteristics, which is equivalent to a database in the ApsaraDB RDS. For example, you can have an index of customer data, an index of product catalogs, and an index of order data. An index is usually identified by a name (all letters must be lowercase) that is used to refer to the index when indexing, searching, updating, and deleting documents in the index.

**Type (type)**

A type is usually a logical classification or partition of an index, allowing different types of documents to be stored under an index, equivalent to a table in the ApsaraDB RDS. such as user type and blog type.

> **Note:** Elasticsearch versions later than 6.x no longer support creating multiple types in an index.

Elasticsearch 5.x allows different types of documents to be stored under one index, Elasticsearch 6.x allows only one type under one index, Elasticsearch 7.x index type naming allows only_doc.

**Document (document)**

A document is the basic unit of information that can be indexed, equivalent to a row of data in a ApsaraDB RDS. For example, you can create a document for a customer, or a document for a product. Documents can be represented in JSON format. In an index, you can store as many documents as you want, and documents must be indexed.

**Field**

The smallest unit that makes up a document. It is equivalent to a column of data in a ApsaraDB RDS.

**Mapping**

It is used to define a document and how its fields are stored and indexed. It is equivalent to a schema in a ApsaraDB RDS. For example, you can define the name and type of a field and the word splitter used in the mapping. The following table describes the mappings between Elasticsearch and ApsaraDB RDS.

| Elasticsearch | ApsaraDB RDS |
|---|---|
| index | Database |
| type | table |
| document | row |
| field | column |
| mapping | schema |

**Shards**

Shards represent index shards. Elasticsearch, a complete index can be divided into multiple shards. This has the advantage that a large index can be split into multiple shards and distributed to different nodes to form a distributed search. The number of shards can only be specified before the index is created, and cannot be changed after the index is created.

**Replicas**

A backup of an index, Elasticsearch multiple copies can be set. Write operations are completed on the primary shard and then distributed to the replica shards. Both the primary shard and replica shard of an index can provide external query services. Therefore, replicas can improve the high availability of the system and the concurrency performance during searches. However, if there are too many copies, the burden of data synchronization during write operations will also increase. Elasticsearch versions earlier than 7.0 create five primary shards for an index and one replica shard for each primary shard. Versions 7.0 and later create one primary shard and one replica shard for an index. The differences between the two are as follows:

| Shard type | Supported Requests | Quantity modifiable | Additional information |
|---|---|---|---|
| Primary shard | Query and indexing requests | The number of primary shards for an index cannot be changed. This number is specified when the index is created. | Each document in an index belongs to one primary shard. The number of primary shards determines the maximum volume of data that an index can store. Important The more primary shards, the more performance overheads of an Elasticsearch cluster. |

| Replica shard | Query requests | The number of replica shards can be changed at any time. | Replica shards are important to search performance and provide the following benefits: Improved fault tolerance: If a primary shard on a node is damaged or lost, you can restore the primary shard from its replica shards. Improved search efficiency: Elasticsearch automatically balances the load of queries among replica shards. |
|---|---|---|---|

## 5 Preparations

### 5.1 Sign in to the Alibaba Cloud Elasticsearch console

**Elasticsearch console**

This topic describes how to sign in to the Alibaba Cloud Elasticsearch console.

**Prerequisites**

Obtain the service domain name for the Apsara Uni-manager Operation Console from the deployment personnel. We recommend using Google Chrome.

**Procedure**

1. In your browser's address bar, enter the service domain name for the Apsara Uni-manager
Operation Console and press Enter.

> **Note:** Click the current language in the upper-right corner to switch languages.
> The **federated sign-in** option is displayed only when global Identity Provider (IdP) settings are configured. The name for this option can be customized.

If you are repeatedly prompted to continue, or if you cannot find the entry for the Apsara Uni-manager Operation Console, you may need to install a certificate to access the console. This can occur if your browser certificate has expired or if the environment has HTTPS authentication enabled. Click **Browser Certificate**
**Installation** in the upper-right corner to open the installation guide.
2. Enter your username and password.
Obtain the username and password from your operations administrator.

> **Note:** **First-time sign-in**
> On your first sign-in to the Apsara Uni-manager Operation Console, you must change your password. Follow the on-screen prompts to complete the password change. For security purposes, the new password must be 10 to 32 characters long and include uppercase letters, lowercase letters, digits, and special characters (such as !, @, #, $, and %).
> **Forgot Password**
> If you forget your password, click **Forgot Password**. Enter your **username**, **Email** (the email address provided when your user account was created), and the verification code. A password reset link is sent to your email address. Click the link to set a new password.

3. Click **Log on**.
4. If multi-factor authentication (MFA) is enabled for your account, follow the relevant steps:
First-time sign-in after an administrator has enforced MFA: a. On the Bind Virtual MFA Device page, follow the on-screen instructions. b. Enter your username and password again, and then click **Log on**. c. Enter the 6-digit MFA code and click **Authenticate**. If you have already enabled and bound a virtual MFA device: Enter the 6-digit MFA code and click **Authenticate**.

> **Note:** For more information about binding and enabling a virtual MFA device, see **Apsara U** **ni-manager Operation Console User Guide** > **Security Center** > **Multi-factor** **authentication** > **Manage multi-factor authentication**.

5. In the top navigation bar, choose **Products > Big Data Computing > Alibaba Cloud**
**Elasticsearch** to open the Alibaba Cloud Elasticsearch console.

**UI icons**

Icons in the upper-right corner of the top navigation bar : Opens the **Apsara Assistant** dialog box. For more information, see Elasticsearch MCP Server. : Switches the display language. Options include English and Traditional Chinese. / : Switches between **light mode** and **dark mode**. : Displays notifications. Click **View More** to open the **Message Center** and view all messages. Icons in the floating menu in the lower-right corner : Opens the **Apsara Assistant** dialog box. : Opens the Pricing page, which includes a pricing calculator, configuration list, and service pricing details. : Opens the **Configuration Pricer**. The number on the icon indicates the quantity of services added. This icon's visibility depends on your user permissions.

### 5.2 View information on the Overview page

**Overview page**

This topic describes the information displayed on the Overview page of the Elasticsearch console.

**Introduction to the Overview page**

Log on to the Alibaba Cloud OpenSearch console. The **Overview** page appears by default. The following table describes the information on this page.

| Region | Description |
|---|---|
| Overview | In the Instance overview section, view the Total Instances and Normal Instances in your organization. Click Total Instances to go to the Instance List page to view instance details and create instances. For more information, see Create a cluster. Click Normal Instances to go to the Instance List page to view the details of instances in the Normal state. |

| Quota Statistics | In the Quota Statistics section, you can view the resource usage (%) and resource allocation. The resource allocation is displayed from the CPU, memory, and disk dimensions, including the current quota, allocated quota, and quota usage. Click the icon to go to the Quota Management page. |
|---|---|
| Top 10 in Quota Use | In the Top 10 in Quota Use section, you can view the resource usage and resource usage trends. You can click Cpu usage, Mem usage, or Quota usage by Disk to view the top 10 quotas with the highest resource usage in the current organization and the subordinate organizations. You can view the trends of resource usage within the previous 7, 15, or 30 days. |
| Monitoring Sorting | In the Monitoring Sorting section, you can view resources sorted based on different dimensions, such as active shards or query rate. You can specify Ascending order or Descending order, Maximum, Average, and Value, or 10, 20, or 30 to sort the statistics. |
| Alert statistics | In the Alarm Statistics section, you can view the total number of alerts and the information about alerts at the P1 (critical), P2 (warning), and P3 (information) levels. |
| Alert Trend | In the Alert Trend section, you can view the trends of alerts within the previous 7, 15, and 30 days. |

### 5.3 Create a cluster

Elasticsearch allows you to create Elasticsearch and OpenSearch clusters. This topic describes how to create a cluster in the console, including how to configure cluster information and how to configure a whitelist.

**Create an Elasticsearch cluster**

1. Log in to the Alibaba Cloud Elasticsearch console.
2. Go to the Create Instance page.
You can use the following methods to go to the Create Instance page: In the **Overview** section of the **Overview** page, click **Clusters (Total)** to go to the
**Instance List** page and click **Create**.
In the left-side navigation pane, click **Clusters List**. On the page that appears, click
**Create**.
3. On the **Create Instance** page, specify the parameters in the Basic Information, Data Node
Information, Kibana Node Information, Dedicated Master Node Information, Coordinator Node Information, and Network Information sections.

> **Note:** If you use an environment that supports the Apsara Copilot feature (corresponding to the
> icon in the console) and the text-selection search feature is enabled, you can
> select the parameters whose details you want to view and click **Consult Apsara** **Copilot** in the dialog box to learn more about the parameters in the Apsara Copilot dialog box on the right. You can enable text-selection search by clicking the
> button
> in the upper-right corner of the Apsara Copilot dialog box.

| Section | Parameter | Description |
|---|---|---|
| Billing Configuratio n | Billing Method | The billing method refers to how cloud services charge based on actual usage. Currently, Pay-as-you-go is supported. Note This parameter is displayed only if you have created the service management item. For more information about how to create a service management item, see Operations > Service operations > Service catalog > Service management in Apsara Uni-manager Management Console User Guide. |
|   | Organization/ Resource Set | Select the organization and resource set to which the cluster belongs. |
|   | Region | The region of the cluster. |
|   | Instance Type | You can select opensearch or elasticsearch. In this example, select elasticsearch. |
|   | AZ Type | Single-Zone Deployment: Select the primary zone. Dual-Zone Deployment: This mode is available only in the disaster recovery scenarios. Select the primary and secondary zones. Note In dual-zone disaster recovery scenarios, we recommend that you disable automatic indexing and dynamic field identification. For more information, see the Configure the YML file section of the Configure clusters topic. Multi-Zone Deployment: This mode is available only in the disaster recovery scenarios. Select the primary zone, secondary zone, and tertiary zone. |

| Basic Information |   |   |
|---|---|---|
|   | Availability Zone | The zone of the cluster. |
|   | Chip Architecture | The architecture of the physical machine on which the cluster is created. |
|   | Kernel Version | Elasticsearch V5.X, V6.X, and V7.X are supported. The actual Elasticsearch versions displayed in the console prevail. |
|   | Instance Name | The name of the cluster. The name must be 0 to 30 characters in length, and can contain underscores ( ), hyphens (-), and _ letters. It must start with a letter or digit. If no name is specified, the system generates a name. You can change the name after the cluster is created. |
|   | Application Scenario | The following use scenarios are supported: High-Performance Search General Search Log Retrieval and Analysis Note In High-Performance Search and General Search scenarios, you must select SSDs. In Log Retrieval and Analysis scenarios, you can select HDDs in most cases. If you require high performance, you can select SSDs. |
|   | Data Node | Specify whether to enable data nodes. Data nodes are enabled by default and cannot be changed. |

|   | Data Node Specification | The following specifications are supported: 8 CPU core and 32 GiB memory, 16 CPU cores and 64 GiB memory, and 32 CPU cores and 128 GiB memory. The actual specifications displayed in the console prevail. Note A local disk is automatically allocated to each data node. The storage capacity of a node is limited to the capacity of a single disk. After a node is created, it cannot be shared or expanded. You can click AI Specification Recommendation to ask Apsara Copilot to recommend specifications based on your business requirements. For more information about how to enable Apsara Copilot, see Apsara Uni-manager Management Console > Apsara Copilot User Guide. The Elasticsearch cluster allows you to use the showMiniSpec switch to control the availability of the specification of 4 CPU cores and 16 GiB memory. By default, the switch is turned off. This switch only affects the switches of Data Node and Dedicated Master Node. They are turned on or off simultaneously. To turn on this switch, follow these steps. Log in to the Apsara Uni-manager Operations Console. In the top navigation bar, choose Platform Operation > Management and Control Service O&M > UniConsole. On the Products page, enter elasticsearch in the search box and click Switch List next to elasticsearchnext. Find the showMiniSpec switch and click Change Switch Status in the Actions column. Turn on the Current Value switch and click OK. It takes one to two minutes before the modification takes effect. If you need to create other specifications, contact Alibaba Cloud technical support. |
|---|---|---|
| Data Node Information |   |   |

|   | Data Node Storage Type | The disk type of data nodes. You can select Local SSD or Local HDD. The actual disk types displayed in the console prevail. Important Exercise caution when you specify Data Node Storage Type. You cannot change the disk type after the cluster is created. In High-Performance Search and General Search scenarios, you must select SSDs. In Log Retrieval and Analysis scenarios, you can select HDDs in most cases. If you require high performance, you can select SSDs. To create a disk of the yoda-lvm type, contact Alibaba Cloud technical support. |
|---|---|---|
|   | Storage Space per Data Node (GiB) | The storage space of each data node in the cluster. The system automatically allocates a qualified local disk to each data node based on the storage type and node specification that you specified. The specifications of the created data node are determined by the size of a single disk. The data node does not support sharing or capacity expansion. We recommend that you set this parameter to a value between 500 and 20480. This range helps achieve the optimal balance among resource utilization, O&M efficiency, and cost control. |
|   | Data Node Count | The number of data nodes in the cluster. Specify the number of data nodes as follows: If the cluster resides in a single zone and dedicated master nodes are disabled, three data nodes are created by default. You can also create five data nodes. Note You cannot select other specifications because an excessive number of data nodes causes cluster stability issues when no dedicated master node exists. If the cluster resides in a single zone and dedicated master nodes are enabled, three data nodes are created by default. You can create 2 to 50 data nodes. If the cluster is deployed across two or more zones, six data nodes are created by default. You can create 4 to 50 data nodes. The number must be a multiple of 2. |

|   | Enable Full Sharding | This parameter is unavailable when dedicated master nodes are disabled. By default, data nodes are spread. This parameter is available after dedicated master nodes are enabled. Configure this parameter based on your business requirements and the resources available in the console. Valid values: Not Required: Multiple data nodes are deployed on the same physical machine. Required: Data nodes are spread in case multiple Elasticsearch data nodes are deployed on the same physical machine. This improves cluster availability. Note If this feature is enabled and the number of physical machines is smaller than that of data nodes, the cluster fails to be created. |
|---|---|---|
| Kibana Node Information | Kibana Node | Specify whether to enable Kibana nodes. By default, Kibana nodes are disabled. You can manually enable Kibana nodes. After you turn on the switch, you can select the specification of Kibana nodes. |
|   | Kibana Node Specification | You can select 1C 2Gi or 2C 4Gi. The actual specifications displayed in the console prevail. If you need to create other specifications, contact Alibaba Cloud technical support. |
|   | Kibanaserver Password | The password used during Kibana initialization. This password is used only in Kibana. The password must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. The following special characters are supported: ! @ # $ % ^ & * ( ) + - = _ The password must be 12 to 32 characters in length. Note Before you use Kibana, you must configure the Kibana whitelist on the Security page of the cluster. |
|   | Dedicated Master Node | Specify whether to enable dedicated master nodes. By default, dedicated master nodes are enabled. You cannot disable dedicated master nodes after the cluster is created. You can manually disable dedicated master nodes when you create a cluster that resides in a single zone. |

| Dedicated Master Node Information |   |   |
|---|---|---|
|   | Dedicated Master Node Specification | The following specifications are supported: 8 CPU cores and 32 GiB memory, 16 CPU cores and 32 GiB memory, and 16 CPU cores and 64 GiB memory. The actual specifications displayed in the console prevail. Note The Elasticsearch cluster allows you to use the showMiniSpec switch to control the availability of the specification 4 CPU cores and 16 GiB memory. By default, the switch is turned off. This switch only affects the switches of Data Node and Dedicated Master Node. They are turned on or off simultaneously. To turn on this switch, follow these steps. Log in to the Apsara Uni-manager Operations Console. In the top navigation bar, choose Platform Operation > Management and Control Service O&M > UniConsole. On the Products page, enter elasticsearch in the search box and click Switch List next to elasticsearchnext. Find the showMiniSpec switch and click Change Switch Status in the Actions column. Turn on the Current Value switch and click OK. It takes one to two minutes before the modification takes effect. If you need to create other specifications, contact Alibaba Cloud technical support. |
|   | Dedicated Master Node Storage Class | The disk type of dedicated master nodes. The following three disk types are supported. The actual disk types displayed in the console prevail. LVM: the default disk type. yoda-LVM storage is shared. We recommend that you use this disk type. Local HDD: not recommended. To avoid resource waste, select this disk type only when the yoda-LVM storage is insufficient. Local SSD: not recommended. To avoid resource waste, select this disk type only when the yoda-LVM storage is insufficient. |
|   | Dedicated Master Node Storage Space | The storage space of each dedicated master node in the cluster. The default value is 100 GiB and cannot be changed. |

|   | Dedicated Master Node Count | The number of dedicated master nodes in the cluster. Specify the number of dedicated master nodes as follows: If the cluster resides in a single zone, three dedicated master nodes are created by default. You cannot change the number in this case. If the cluster is deployed across two or more zones, five data nodes are created by default. You can also create three dedicated master nodes. |
|---|---|---|
| Coordinator Node Information | Coordinator Node | Specify whether to enable client nodes. By default, client nodes are disabled. You can manually enable client nodes. After client nodes are enabled, you can specify the specifications and number of client nodes. |
|   | Coordinator Node Specification | The following specifications are supported: 4 CPU cores and 16 GiB memory, 8 CPU cores and 32 GiB memory, 16 CPU cores and 32 GiB memory, and 16 CPU cores and 64 GiB memory. The actual specifications displayed in the console prevail. If you need to create other specifications, contact Alibaba Cloud technical support. |
|   | Coordinator Node Count | The number of client nodes in the cluster. Default value: 2. Valid values: 2 to 25. |
| Network Information | Network Type | Valid values: Virtual Private Cloud (Single Tunnel) and Virtual Private Cloud (any tunnel). |
|   | VPC | The ID of the virtual private cloud (VPC). |
|   | VSwitch | The ID of the vSwitch. |
|   | Login Name | The default login name is elastic and cannot be changed. It is used to log in to your Elasticsearch cluster and the Kibana console of the cluster. |
|   | Login Password | The password that corresponds to the elastic username. The password must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. The following special characters are supported: ! @ # $ % ^ & * ( ) + - = _ The password must be 12 to 32 characters in length. |

|   | Login Name | The default login name is monitoring collector and cannot be _ changed. The account used by the control service. Some control features rely on this account. Note Before you use the control features, you must configure a whitelist on the Security page of the cluster. |
|---|---|---|
|   | Login Password | The password corresponds to the account used by the control service. The password must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. The following special characters are supported: ! @ # $ % ^ & * ( ) + - = _ The password must be 12 to 32 characters in length. |

4. (Optional) View the configuration overview.
In the right-side **Configuration overview** panel, you can perform the following operations. View parameter configurations In the **Configuration overview** panel, the required parameters are verified in real time. If a required parameter is left empty, a corresponding red warning is displayed. Manage quotas You can click **Quota Management** to go to the Quotas page and configure the quota limits for the cluster. For more information about how to configure quota limits, see the
**Quota management > Operations** section in **Apsara Uni-manager Management**
**Console User Guide**.
Locate parameters quickly Click the entry on the right of the target parameter to quickly jump to the configuration settings.
5. Confirm and submit the configurations.
If you have created the **Alibaba Cloud Search and Analytics Service** in cloud resources, please verify that the parameter configurations are correct, and then click
**Confirm Order**. For more information, see the Service management topic.
If you have not created the **Alibaba Cloud Search and Analytics Service** in cloud resources, please verify that the parameter configurations are correct, and then click
**Submit**. For more information, see the Service management topic.
For more information about service management, see the **Service management** topic in
**Apsara Uni-manager Operations Console User Guide** .
6. In the message that appears, click **OK**.
A period of time is required before an Elasticsearch cluster can provide services after it is created. If **Normal** is displayed in the **Status** column of the cluster, the cluster has been successfully created.

> **Note:** Before you use the cluster, you must configure a whitelist. Otherwise, you may encounter issues such as monitoring data collection failure or Kibana console login failure. For more information, see the Security Settings section of the Cluster configuration topic.
> To view information in the **Security Level** column of the cluster on the **Instance** **List** page, you must first enable security level-based authorization. For more information, see **Apsara Uni-manager Management Console User Guide >** **Security policies > Security level-based authorization**.

**Create an OpenSearch cluster**

1. Log in to the Alibaba Cloud Elasticsearch console.
2. Go to the Create Instance page.
You can use the following methods to go to the Create Instance page: In the **Overview** section of the **Overview** page, click **Clusters (Total)** to go to the
**Instance List** page and click **Create**.
In the left-side navigation pane, click **Clusters List**. On the page that appears, click
**Create**.
3. On the **Create Instance** page, specify the parameters in the Basic Information, Data Node
Information, Dashboard Node Information, Dedicated Master Node Information, Coordinator Node Information, and Network Information sections.

> **Note:** If you use an environment that supports the Apsara Copilot feature (corresponding to the
> icon in the console) and the text-selection search feature is enabled, you can
> select the parameters whose details you want to view and click **Consult Apsara** **Copilot** in the dialog box to learn more about the parameters in the Apsara Copilot dialog box on the right. You can enable text-selection search by clicking the
> button
> in the upper-right corner of the Apsara Copilot dialog box.

| Section | Parameter | Description |
|---|---|---|

| Billing Configuratio n | Billing Method | The billing method refers to how cloud services charge based on actual usage. Currently, Pay-as-you-go is supported. Note This parameter is displayed only if you have created the service management item. For more information about how to create a service management item, see Operations > Service operations > Service catalog > Service management in Apsara Uni-manager Management Console User Guide. |
|---|---|---|
| Basic Information | Organization/ Resource Set | Select the organization and resource set to which the cluster belongs. |
|   | Region | The region of the cluster. |
|   | Instance Type | You can select opensearch or elasticsearch. In this example, select opensearch. |
|   | AZ Type | Only single-zone deployment is supported. |
|   | Availability Zone | The zone of the cluster. |
|   | Chip Architecture | The architecture of the physical machine on which the cluster is created. |
|   | Kernel Version | OpenSearch V3.1.0 is available. The actual versions displayed in the console prevail. |
|   | Instance Name | The name of the cluster. The name must be 0 to 30 characters in length, and can contain underscores ( ), hyphens (-), and _ letters. It must start with a letter or digit. If no name is specified, the system generates a name. You can change the name after the cluster is created. |
|   | Application Scenario | The following use scenarios are supported: High-Performance Search General Search Log Retrieval and Analysis Note In High-Performance Search and General Search scenarios, you must select SSDs. In Log Retrieval and Analysis scenarios, you can select HDDs in most cases. If you require high performance, you can select SSDs. |

|   | Data Node | Specify whether to enable data nodes. Data nodes are enabled by default and cannot be changed. |
|---|---|---|
|   | Data Node Specification | The following specifications are supported: 8 CPU cores and 32 GiB memory, 16 CPU cores and 64 GiB memory, and 32 CPU cores and 128 GiB memory. The actual specifications displayed in the console prevail. Note A local disk is automatically allocated to each data node. The storage capacity of a node is limited to the capacity of a single disk. After a node is created, it cannot be shared or expanded. You can click AI Specification Recommendation to ask Apsara Copilot to recommend specifications based on your business requirements. For more information about how to enable Apsara Copilot, see Apsara Uni-manager Management Console > Apsara Copilot User Guide. The Elasticsearch cluster allows you to use the showMiniSpec switch to control the availability of the specification of 4 CPU cores and 16 GiB memory. By default, the switch is turned off. This switch only affects the switches of Data Node and Dedicated Master Node. They are turned on or off simultaneously. To turn on this switch, follow these steps. Log in to the Apsara Uni-manager Operations Console. In the top navigation bar, choose Platform Operation > Management and Control Service O&M > UniConsole. On the Products page, enter elasticsearch in the search box and click Switch List next to elasticsearchnext. Find the showMiniSpec switch and click Change Switch Status in the Actions column. Turn on the Current Value switch and click OK. It takes one to two minutes before the modification takes effect. If you need to create other specifications, contact Alibaba Cloud technical support. |
|   | n: 20260629 | 3 |

| Data Node Information |   |   |
|---|---|---|
|   | Data Node Storage Type | The disk type of data nodes. You can select Local SSD or Local HDD. The actual disk types displayed in the console prevail. Important Exercise caution when you specify Data Node Storage Type. You cannot change the disk type after the cluster is created. In High-Performance Search and General Search scenarios, you must select SSDs. In Log Retrieval and Analysis scenarios, you can select HDDs in most cases. If you require high performance, you can select SSDs. To create a disk of the yoda-lvm type, contact Alibaba Cloud technical support. |
|   | Storage Space per Data Node (GiB) | The storage space of each data node in the cluster. The system automatically allocates a qualified local disk to each data node based on the storage type and node specification that you specified. The specifications of the created data node are determined by the size of a single disk. The data node does not support sharing or capacity expansion. We recommend that you set this parameter to a value between 500 and 20480. This range helps achieve the optimal balance among resource utilization, O&M efficiency, and cost control. |
|   |   | The number of data nodes in the cluster. Specify the number of data nodes as follows: If the cluster resides in a single zone and dedicated master nodes are disabled, three data nodes are created by default. You can also create five data nodes. Note |
|   | Data Node Count | You cannot select other specifications because an excessive number of data nodes causes cluster stability issues when no dedicated master node exists. If the cluster resides in a single zone and dedicated master nodes are enabled, three data nodes are created by default. You can create 2 to 50 data nodes. |

|   | Enable Full Sharding | This parameter is unavailable when dedicated master nodes are disabled. By default, data nodes are spread. This parameter is available after dedicated master nodes are enabled. Configure this parameter based on your business requirements and the resources available in the console. Valid values: Not Required: Multiple data nodes are deployed on the same physical machine. Required: Data nodes are spread in case multiple Elasticsearch data nodes are deployed on the same physical machine. This improves cluster availability. Note If this feature is enabled and the number of physical machines is smaller than that of data nodes, the cluster fails to be created. |
|---|---|---|
| Dashboard Node Information | Dashboard Node | Specify whether to enable Dashboard nodes. By default, Dashboard nodes are disabled. You can manually enable Dashboard nodes. After you turn on the switch, you can select the specification of Dashboard nodes. |
|   | Dashboard Node Specification | You can select 1C 2Gi or 2C 4Gi. The actual specifications displayed in the console prevail. If you need to create other specifications, contact Alibaba Cloud technical support. |
|   | Graphical Component Password | The password used during Dashboard initialization. This password is used only in Dashboard. The password must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. The following special characters are supported: ! @ # $ % ^ & * ( ) + - = _ The password must be 12 to 32 characters in length. |
|   | Dedicated Master Node | Specify whether to enable dedicated master nodes. By default, dedicated master nodes are enabled. You cannot disable dedicated master nodes after the cluster is created. You can manually disable dedicated master nodes when you create a cluster that resides in a single zone. |

|   | Dedicated Master Node Specification | The following specifications are supported: 8 CPU cores and 32 GiB memory, 16 CPU cores and 32 GiB memory, and 16 CPU cores and 64 GiB memory. The actual specifications displayed in the console prevail. If you need to create other specifications, contact Alibaba Cloud technical support. Note The Elasticsearch cluster allows you to use the showMiniSpec switch to control the availability of the specification 4 CPU cores and 16 GiB memory. By default, the switch is turned off. This switch only affects the switches of Data Node and Dedicated Master Node. They are turned on or off simultaneously. To turn on this switch, follow these steps. Log in to the Apsara Uni-manager Operations Console. In the top navigation bar, choose Platform Operation > Management and Control Service O&M > UniConsole. On the Products page, enter elasticsearch in the search box and click Switch List next to elasticsearchnext. Find the showMiniSpec switch and click Change Switch Status in the Actions column. Turn on the Current Value switch and click OK. It takes one to two minutes before the modification takes effect. If you need to create other specifications, contact Alibaba Cloud technical support. |
|---|---|---|
| Dedicated Master Node Information |   |   |

|   | Dedicated Master Node Storage Class | The disk type of dedicated master nodes. The following three disk types are supported. The actual disk types displayed in the console prevail. LVM: the default disk type. yoda-LVM storage is shared. We recommend that you use this disk type. Local HDD: not recommended. To avoid resource waste, select this disk type only when the yoda-LVM storage is insufficient. Local SSD: not recommended. To avoid resource waste, select this disk type only when the yoda-LVM storage is insufficient. |
|---|---|---|
|   | Dedicated Master Node Storage Space | The storage space of each dedicated master node in the cluster. The default value is 100 GiB and cannot be changed. |
|   | Dedicated Master Node Count | The number of dedicated master nodes in the cluster. Specify the number of dedicated master nodes as follows: If the cluster resides in a single zone, three dedicated master nodes are created by default. You cannot change the number in this case. If the cluster is deployed across two or more zones, five data nodes are created by default. You can also create three dedicated master nodes. |
| Coordinator Node Information | Coordinator Node | Specify whether to enable client nodes. By default, client nodes are disabled. You can manually enable client nodes. After client nodes are enabled, you can specify the specifications and number of client nodes. |
|   | Coordinator Node Specification | The following specifications are supported: 4 CPU cores and 16 GiB memory, 8 CPU cores and 32 GiB memory, 16 CPU cores and 32 GiB memory, and 16 CPU cores and 64 GiB memory. The actual specifications displayed in the console prevail. If you need to create other specifications, contact Alibaba Cloud technical support. |
|   | Coordinator Node Count | The number of client nodes in the cluster. Default value: 2. Valid values: 2 to 25. |
|   | Network Type | Valid values: Virtual Private Cloud (Single Tunnel) and Virtual Private Cloud (any tunnel). |
|   | VPC | The ID of the VPC. |
|   | VSwitch | The ID of the vSwitch. |
| Document Versio |   |   |

| Network Information |   |   |
|---|---|---|
|   | Login Name | The default login name is admin and cannot be changed. It is used to log in to your OpenSearch cluster and the Dashboard console of the cluster. |
|   | Login Password | The password that corresponds to the elastic username. The password must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. The following special characters are supported: ! @ # $ % ^ & * ( ) + - = _ The password must be 12 to 32 characters in length. |
|   | Login Name | The default login name is monitoring collector and cannot be _ changed. The account used by the control service. Some control features rely on this account. |
|   | Login Password | The password corresponds to the account used by the control service. The password must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. The following special characters are supported: ! @ # $ % ^ & * ( ) + - = _ The password must be 12 to 32 characters in length. |

4. (Optional) View the configuration overview.
In the right-side **Configuration overview** panel, you can perform the following operations. View parameter configurations In the **Configuration overview** panel, the required parameters are verified in real time. If a required parameter is left empty, a corresponding red warning is displayed. Manage quotas You can click **Quota Management** to go to the Quotas page and configure the quota limits for the cluster. For more information about how to configure quota limits, see the
**Quota management > Operations** section in **Apsara Uni-manager Management**
**Console User Guide**.
Locate parameters quickly Click the entry on the right of the target parameter to quickly jump to the configuration settings.
5. Confirm and submit the configurations.
If you have created the **Alibaba Cloud Search and Analytics Service** in cloud resources, please verify that the parameter configurations are correct, and then click
**Confirm Order**. For more information, see the Service management topic.
If you have not created the **Alibaba Cloud Search and Analytics Service** in cloud resources, please verify that the parameter configurations are correct, and then click
**Submit**. For more information, see the Service management topic.
For more information about service management, see the **Service management** topic in
**Apsara Uni-manager Operations Console User Guide** .
6. In the message that appears, click **OK**.
A period of time is required before an Elasticsearch cluster can provide services after it is created. If **Normal** is displayed in the **Status** column of the cluster, the cluster has been successfully created.

> **Note:** To view information in the **Security Level** column of the cluster on the **Instance List** page, you must first enable security level-based authorization. For more information, see **Apsara Uni-manager Management Console User Guide > Security policies** **> Security level-based authorization**.

### 5.4 Access a cluster

You can access an Elasticsearch cluster from an Elastic Compute Service (ECS) instance or the Kibana/Dashboard console.

**Prerequisites**

An Elasticsearch cluster is created and added to the whitelist. For more information, see Create a cluster. Create an ECS instance: If the network type of the Elasticsearch cluster is SingleTunnel, the ECS instance and Elasticsearch cluster must reside in the same virtual private cloud (VPC). If the network type of the Elasticsearch cluster is AnyTunnel, any ECS instances can access the Elasticsearch cluster.

**Access a cluster from an ECS instance**

1. Log in to the ECS instance over SSH and install the cURL tool.

> **Note:** For more information about how to log in to an ECS instance, see **Quick start >** **Connect to an instance > Instance connecting overview** in ESC User Guide.

2. Run a cURL command to access the cluster using its private endpoint.

```bash
curl http://<HOST>:<PORT> -u elastic:<password>
```

**<HOST>**: The private endpoint of the Elasticsearch cluster. You can obtain the endpoint
from the Basic Information page of the cluster.

> **Note:** Log on to the Alibaba Cloud Elasticsearch console. In the navigation pane on the left, click **Elasticsearch Instances**, and then click the ID of the target instance. On the **Basic Information** page, you can find the private endpoint.

**<PORT>**: the internal port of the Elasticsearch cluster. You can obtain the information
from the Basic Information page. The default port is 9200.
**<password>**: the password of the elastic account of the Elasticsearch cluster.

**Access a cluster from the Kibana/Dashboard console**

> **Note:** For Elasticsearch instances, use the Kibana console. For OpenSearch instances, use the Dashboard console. The procedures are similar. This topic uses the Kibana console as an example.

1. Log on to the Alibaba Cloud Elasticsearch console. In the left navigation pane, click **Instance**
**List**.
2. In the **Instance List**, click the target instance ID.
3. On the **Basic Information** page, locate the **Kibana Information** section and click the
access URL for the corresponding console.
4. Enter the username and password, and click **Login**.

> **Important:** The default username is elastic for an Elasticsearch instance and admin for an OpenSearch instance. The password is the one that you specified when you created the cluster.

5. Click the
icon in the upper-left corner, choose **Management > Dev Tools**, and then run the `GET /` command in the **Console** to access the cluster.

> **Note:** A cluster of Elasticsearch V6.8.2 is used in this example. The procedure may vary depending on the Elasticsearch version. The actual console page prevails.

### 5.5 View cluster information

This topic describes how to view Elasticsearch cluster information in the Kibana console to help identify and handle potential risks.

**Procedure**

> **Note:** For Elasticsearch instances, use the Kibana console. For OpenSearch instances, use the Dashboard console. The procedures are similar. This topic uses the Kibana console as an example.

1. Log in to the Kibana console.
2. Run the following commands to view the basic information of the cluster.
View the Elasticsearch cluster version

```
GET /
```

View the health status of the cluster

```
GET /_cat/health?v
```

Elasticsearch indicates data integrity by displaying the cluster health status. Cluster health states are represented by using the green, yellow, and red colors.

| Cluster health | Description |
|---|---|

| green | The cluster is in the Normal state, and all shards are allocated as expected. |
|---|---|
| yellow | The cluster is available, but some index replica shards are not allocated. |
| red | Some primary shards cannot be allocated. Indexes in the red state exist. Data fails to be written into these indexes. Consequently, the cluster cannot provide services as normal. |

If the cluster is in the yellow or red state, the cluster is abnormal. This indicates that some primary or replica shards in the cluster are not allocated. We recommend that you find the reason why the shards are not allocated and mitigate the potential risks at the earliest opportunity. View information about nodes in the cluster

```
GET /_cat/nodes?v
```

View Java virtual machine (JVM) heap memory

```
GET /_nodes/stats/jvm?pretty
```

View disks

```
GET /_cat/allocation?v
```

View indexes

```
GET /_cat/indices?v
```

## 6 Quick start

### 6.1 Create an index

This topic describes how to create an index for an Elasticsearch cluster by using the Kibana console, including configuring the number of shards, number of replicas, and field mappings. You can create indexes in Elasticsearch V7.0.0 and later.

**Procedure**

> **Note:** For Elasticsearch instances, use the Kibana console. For OpenSearch instances, use the Dashboard console. The procedures are similar. This topic uses the Kibana console as an example.

1. Log in to the Kibana console.
2. Run the following command to create an index:

```json
PUT my_index
  "settings": {
    "index": {
      "number_of_shards": "5",
      "number_of_replicas": "1"
```

`},`

```json
  "mappings": {
    "properties": {
      "post_date": {
        "type": "date"
```

`},`

```json
      "tags": {
        "type": "keyword"
```

`},`

```json
      "title": {
        "type": "text",
        "analyzer": "cjk"
```

> **Important:** The preceding sample code applies only to Elasticsearch V7.0.0 and later. You can modify the code based on your business requirements. For more information, see Doc index.

In Elasticsearch V7.0.0 and later, mapping types are removed. However, these mapping types are still supported in earlier versions. For more information, see Removal of types. In the preceding example, an index named `my_index` is created, and the type of the index

| is | doc _ |   |
|---|---|---|
| cjk |   |   |
|   |   | tok |

is `_doc` . The index is split into five shards, has one replica for each shard, and uses the After the index is created and the mappings are configured, the following result is returned:

```json
  "acknowledged" : true,
  "shards_acknowledged" : true,
  "index" : "my_index"
```

### 6.2 Manage documents

#### 6.2.1 Create a document

Elasticsearch allows you to create documents by sending PUT requests, specifying indexes, types, and IDs of documents, and defining fields in the request body. This topic describes how to create a document in an Elasticsearch cluster by running a PUT command.

**Procedure**

1. Log in to the Kibana console.
2. Run the following command to create a document by using the PUT method:

```
PUT /<index_name>/<type>/<ID>
  "<field_name>": "<value>"
```

| Parameter | Description |
|---|---|
| <index name> _ | The name of the index. |
| <type> | The type of the index. If you use a cluster of an Elasticsearch version earlier than V7.0.0, you can specify an index type based on your business requirements. For clusters of Elasticsearch V7.0.0 or later, the index type is fixed to doc. _ |
| <ID> | The ID of the document. |
| <field name> _ | The name of the field. |
| <value> | The value of the field. |

Sample code: Create a document whose ID is 1

```json
PUT /my_index/_doc/1
  "title": "One",
  "tags": ["ruby"],
  "post_date":"2009-11-15T13:00:00"
```

After the document is created, the following result is returned:

```json
  "_index" : "my_index",
  "_type" : "_doc",
  "_id" : "1",
  "_version" : 1,
  "result" : "created",
  "_shards" : {
    "total" : 2,
    "successful" : 2,
    "failed" : 0
```

`},`

```json
  "_seq_no" : 0,
  "_primary_term" : 1
```

Create a document whose ID is 2

```json
PUT /my_index/_doc/2
  "title": "Two",
  "tags": ["ruby"],
  "post_date":"2009-11-15T14:00:00"
```

After the document is created, the following result is returned:

```json
  "_index" : "my_index",
  "_type" : "_doc",
  "_id" : "2",
  "_version" : 1,
  "result" : "created",
  "_shards" : {
    "total" : 2,
    "successful" : 2,
    "failed" : 0
```

`},`

```json
  "_seq_no" : 1,
  "_primary_term" : 1
```

For more information, see Docs Index.

#### 6.2.2 Update a document

Elasticsearch allows you to update documents by using the PUT or POST method, which is suitable for real-time data processing. This topic describes how to update an entire document or part of a document in Elasticsearch.

**Procedure**

1. Log in to the Kibana console.
2. Run one of the following commands to update a document by using the PUT or POST
method. Update an entire document

```
PUT /<index_name>/<type>/<ID>
  "<field_name>": "<value>"
```

Update part of a document

```json
POST /<index_name>/<type>/_update/<ID>
  "script" : {
        "source": "ctx._source.<field_name> = '<value>'"
```

| Parameter | Description |
|---|---|
| <index name> _ | The name of the index. |
| <type> | The type of the index. If you use a cluster of an Elasticsearch version earlier than V7.0.0, you can specify an index type based on your business requirements. For clusters of Elasticsearch V7.0.0 or later, the index type is fixed to doc. _ |
| <ID> | The ID of the document. |
| <field name> _ | The name of the field. |
| <value> | The value of the field. |

Examples: Update an entire document

```json
PUT /my_index/_doc/1
  "title": "One World One Dream",
  "tags": ["ruby"],
  "post_date":"2009-11-15T13:00:00"
```

If the document is updated, the following result is returned:

```json
  "_index" : "my_index",
  "_type" : "_doc",
  "_id" : "1",
  "_version" : 2,
  "result" : "updated",
  "_shards" : {
    "total" : 2,
    "successful" : 2,
    "failed" : 0
```

`},`

```json
  "_seq_no" : 1,
  "_primary_term" : 1
```

Update part of a document

```json
POST /my_index/_update/1
    "script" : {
        "source": "ctx._source.title='One World'"
```

If the document is updated, the following result is returned:

```json
  "_index" : "my_index",
  "_type" : "_doc",
  "_id" : "1",
  "_version" : 5,
  "result" : "updated",
  "_shards" : {
    "total" : 2,
    "successful" : 2,
    "failed" : 0
```

`},`

```json
  "_seq_no" : 4,
  "_primary_term" : 1
```

You can also call the corresponding API operation to batch update documents. For more information, see Docs Update.

#### 6.2.3 Retrieve a document

This topic describes how to retrieve a specific document in the Kibana console of an Elasticsearch cluster by sending GET requests.

**Procedure**

1. Log in to the Kibana console.
2. Run the following command to retrieve a document by using the GET method:

```
GET /<index_name>/<type>/<ID>
```

| Parameter | Description |
|---|---|
| <index name> _ | The name of the index. |
| <type> | The type of the index. If you use a cluster of an Elasticsearch version earlier than V7.0.0, you can specify an index type based on your business requirements. For clusters of Elasticsearch V7.0.0 or later, the index type is fixed to doc. _ |
| <ID> | The ID of the document. |

Sample code:

```
GET /my_index/_doc/1
```

If the command succeeds, the following result is returned:

```json
  "_index" : "my_index",
  "_type" : "_doc",
  "_id" : "1",
  "_version" : 5,
  "_seq_no" : 4,
  "_primary_term" : 1,
  "found" : true,
  "_source" : {
    "title" : "One World",
    "tags" : [
      "ruby",
      "blue"
```

`],`

```json
    "post_date" : "2009-11-15T13:00:00"
```

For more information, see Docs GET.

#### 6.2.4 Search for documents

This topic describes how to search for Elasticsearch documents by URI parameters in the Kibana console by sending GET requests.

**Procedure**

1. Log in to the Kibana console.
2. Run the following command to search for documents by using the GET method. URI
parameters in the command are used to specify the object you want to search.

```
GET /_search GET /<index_name>/_search
```

**<index_name>**: the name of the index.
To search for documents in which the title field contains the T keyword, run the following command:

```
GET /my_index/_search?q=title:T*
```

If the command succeeds, the following result is returned:

```json
  "took" : 689,
  "timed_out" : false,
  "_shards" : {
    "total" : 5,
    "successful" : 5,
    "skipped" : 0,
    "failed" : 0
```

`},`

```json
  "hits" : {
    "total" : {
      "value" : 1,
      "relation" : "eq"
```

`},`

```json
    "max_score" : 1.0,
    "hits" : [
        "_index" : "my_index",
        "_type" : "_doc",
        "_id" : "2",
        "_score" : 1.0,
        "_source" : {
          "title" : "Two",
          "tags" : [
            "ruby"
```

`],`

```json
          "post_date" : "2009-11-15T14:00:00"
```

`]` For more information, see Docs GET.

#### 6.2.5 Perform a complex search

This topic describes how to perform a complex search in the Kibana console by sending GET requests, including queries by time range and keyword. By performing these operations, you can efficiently retrieve document data in a specific index.

**Procedure**

1. Log in to the Kibana console.
2. Run the following command to perform a complex search by using the GET method:

```json
GET /<index_name>/_search
    "query" : {
```

`""`

| Parameter | Description |
|---|---|
| <index name> _ | The name of the index. |
| query | The request body. |

Sample code: Query by time range

```json
GET /my_index/_search
    "query" : {
        "range" : {
            "post_date" : { "from" : "2009-11-15T13:00:00", "to" : "2009-11-
15T14:00:00" }
```

If the command succeeds, the following result is returned:

```json
  "took" : 1,
  "timed_out" : false,
  "_shards" : {
    "total" : 5,
    "successful" : 5,
    "skipped" : 0,
    "failed" : 0
```

`},`

```json
  "hits" : {
    "total" : {
      "value" : 2,
      "relation" : "eq"
```

`},`

```json
    "max_score" : 1.0,
    "hits" : [
        "_index" : "my_index",
        "_type" : "_doc",
        "_id" : "2",
        "_score" : 1.0,
        "_source" : {
          "title" : "Two",
          "tags" : [
            "ruby"
```

`],`

```json
          "post_date" : "2009-11-15T14:00:00"
```

`},`

```json
        "_index" : "my_index",
        "_type" : "_doc",
        "_id" : "1",
        "_score" : 1.0,
        "_source" : {
          "title" : "One World",
          "tags" : [
            "ruby"
```

`],`

```json
          "post_date" : "2009-11-15T13:00:00"
```

`]` Query by keyword

```json
GET /my_index/_search
    "query" : {
    "simple_query_string" : {
        "query": "One +(python | ruby) -Two",
        "fields": ["title^5", "tags"],
        "default_operator": "or"
```

If the command succeeds, the following result is returned:

```json
  "took" : 1,
  "timed_out" : false,
  "_shards" : {
    "total" : 5,
    "successful" : 5,
    "skipped" : 0,
    "failed" : 0
```

`},`

```json
  "hits" : {
    "total" : {
      "value" : 1,
      "relation" : "eq"
```

`},`

```json
    "max_score" : 2.2378674,
    "hits" : [
        "_index" : "my_index",
        "_type" : "_doc",
        "_id" : "1",
        "_score" : 2.2378674,
        "_source" : {
          "title" : "One World",
          "tags" : [
            "ruby"
```

`],`

```json
          "post_date" : "2009-11-15T13:00:00"
```

`]` For more information, see Docs GET.

#### 6.2.6 Analyze document statistics

Elasticsearch allows you to perform aggregate queries on the data of a specific index in the Kibana console by sending POST requests. This topic describes how to use Elasticsearch to perform statistical analysis on document data.

**Procedure**

1. Log in to the Kibana console.
2. Run the following command to analyze document statistics by using the POST method:

```json
POST /<index_name>/_search
  "size": 0,
  "aggs": {
    "group_by_tags": {
      "terms": {
        "field": "tags"
```

**<index_name>**: the name of the index.
Sample code:

```json
POST /my_index/_search
  "size": 0,
  "aggs": {
    "group_by_tags": {
      "terms": {
        "field": "tags"
```

If the command succeeds, the following result is returned:

```json
  "took" : 1,
  "timed_out" : false,
  "_shards" : {
    "total" : 5,
    "successful" : 5,
    "skipped" : 0,
    "failed" : 0
```

`},`

```json
  "hits" : {
    "total" : {
      "value" : 2,
      "relation" : "eq"
```

`},`

```json
    "max_score" : null,
    "hits" : [ ]
```

`},`

```json
  "aggregations" : {
    "group_by_tags" : {
      "doc_count_error_upper_bound" : 0,
      "sum_other_doc_count" : 0,
      "buckets" : [
          "key" : "ruby",
          "doc_count" : 2
```

`]`

#### 6.2.7 Delete a document

Elasticsearch allows you to delete specific documents in the Kibana console. This topic describes how to run the DELETE command to delete a document with a specific index, type, and ID.

**Procedure**

1. Log in to the Kibana console.
2. Run the following command to delete a document by using the DELETE method:

```
DELETE /<index_name>/<type>/<ID>
```

| Parameter | Description |
|---|---|
| <index name> _ | The name of the index. |

| <type> | The type of the index. If you use a cluster of an Elasticsearch version earlier than V7.0.0, you can specify an index type based on your business requirements. For clusters of Elasticsearch V7.0.0 or later, the index type is fixed to doc. _ |
|---|---|
| <ID> | The ID of the document. |

Sample code:

```
DELETE /my_index/_doc/2
```

If the document is deleted, the following result is returned:

```json
  "_index" : "my_index",
  "_type" : "_doc",
  "_id" : "2",
  "_version" : 2,
  "result" : "deleted",
  "_shards" : {
    "total" : 2,
    "successful" : 2,
    "failed" : 0
```

`},`

```json
  "_seq_no" : 4,
  "_primary_term" : 1
```

For more information, see Docs Delete.

#### 6.2.8 Delete an index

You can delete Elasticsearch indexes by running a DELETE command in the Kibana console. This topic describes how to delete an index by specifying the index name and obtain the deletion confirmation result.

**Procedure**

1. Log in to the Kibana console.
2. Run the following command to delete an index by using the DELETE method:

```
DELETE /<index_name>
```

**<index_name>**: the name of the index.
Sample code:

```
DELETE /my_index
```

If the index is deleted, the following result is returned:

```json
  "acknowledged" : true
```

For more information, see Docs Delete.

## 7 Manage clusters

### 7.1 Manage clusters

#### 7.1.1 Customize the columns displayed in the cluster list

**cluster list**

Elasticsearch allows you to customize the columns displayed in the cluster list. You can select the columns to be displayed in the console. This topic describes how to customize the columns displayed in the cluster list.

**Procedure**

1. Log in to the Alibaba Cloud Search and Analytics Service console. In the left-side navigation pane,
click **Clusters List**.
2. In the upper-right corner of the page that appears, click the
icon.
3. In the **Custom Columns** list, select the columns that you want to view. Then, the cluster
list displays the specified columns.

#### 7.1.2 Export a list of Elasticsearch clusters

This topic describes how to export a list of Elasticsearch clusters, including the export range and the selection of data columns to be exported.

**Procedure**

1. Log in to the Alibaba Cloud Search and Analytics Service console. In the left-side navigation pane,
click **Clusters List**.
2. In the upper-right corner of the page that appears, click the
icon.
3. In the **Export** dialog box, configure the Export Data by Scope and Columns to Export
parameters.
**Export Data by Scope**: By default, all resources are selected. You can also select
Selected Data.
**Columns to Export**: Select columns that you want to export.
4. Click **OK**.

#### 7.1.3 Refresh instance

If the information of an Elasticsearch cluster, such as its status, is not updated promptly in the console, you can manually refresh the page to view the up-to-date information. This topic describes how to update the information of a cluster.

**Procedure**

1. Log on to the Alibaba Cloud Retrieval Analysis Service console. In the left navigation pane, click
**Instance List**.
2. There are two ways to refresh the instance.
On the **Elasticsearch Instances** page, click the icon. Click the ID of the target instance. On the **Basic Information** page, click **Refresh** in the upper-right corner.

#### 7.1.4 Modify the name of a cluster

This topic describes how to modify the name of an Elasticsearch cluster.

**Procedure**

1. Sign in to the Alibaba Cloud Elasticsearch console.
2. In the left-side navigation pane, click **Clusters List**.
3. Rename a cluster.
You can use either of the following methods to rename the cluster:

> **Note:** The cluster name must be 0 to 30 characters in length and start with a letter, digit, or Chinese character. It can contain underscores (_) or hyphens (-).

Method 1: a. On the **Instance List** page, move the pointer over **Instance ID/name** and click . b. In the **Modify Name** dialog box that appears, enter a new name. c. Click **OK**. Method 2: a. On the **Instance List** page, click **Instance ID/name**. b. In the **Basic Information** section, click **Edit** next to **Name**. c. Enter a new name as prompted and click **OK**.

#### 7.1.5 Manage cluster tags

If you have multiple Elasticsearch clusters, you can add tags to the clusters to facilitate cluster management. A tag consists of a key and a value. You can use keys and values to further classify clusters. This topic describes how to add a tag to a cluster, filter clusters by tag, and remove a tag from a cluster.

**Add tags**

1. Log in to the Alibaba Cloud Search and Analytics Service console.
2. In the left-side navigation pane, click **Clusters List**.
3. On the **Instance List** page, add tags to one or more clusters.
Add a tag to a single cluster a. Move the pointer in the **Tag** column of the cluster to which you want to add a tag, and click the icon. b. In the **Edit Tags** dialog box, click **Add**, configure the **Tag Key** and **Tag Value** parameters, and click **OK**. c. In the Edited message, confirm that the tag is added to the cluster, and then click Close. Add tags to multiple clusters at a time a. Select multiple clusters to which you want to add tags and click **Batch Add Tags** below the cluster list. b. In the **Batch Add Tags** dialog box, click **Add**, configure the **Tag Key** and **Tag Value** parameters, and click **OK**. c. In the Edited message, confirm that the tags are added to the clusters, and then click Close.

> **Note:** The tag key must be unique.
> You can create up to 20 tags at a time.
> For more information about how to manage tags in a centralized manner, see **Apsara Uni-manager Management Console User Guide > Operation** **Center > Resource Operations > Manage tags**.

**Filter clusters by tag**

After tags are added to clusters, you can perform the following operations to filter clusters by tag:
1. On the **Instance List** page, click **Filter by Tag**.
2. Select values for the **Tag Key** and **Tag Value** parameters from the drop-down list to filter
clusters. After clusters are filtered, you can click the icon next to the tag in the **Filter by Tag** search box to delete the filter condition.

**Remove tags**

**Remove a tag from a single cluster**

i. Click the icon in the **Tag** column of the cluster from which you want to remove a tag. ii. In the **Edit Tags** dialog box, find the tag key and tag value that you want to delete, click the icon on the right, and then click **OK**. iii. In the Edited message, confirm that the tag is removed from the cluster, and then click
**Close**.

**Remove tags from multiple clusters**

i. Select multiple clusters from which you want to remove tags and click **Batch Remove**
**Tags** below the cluster list.
ii. In the **Batch Remove Tags** dialog box, select the tags that you want to remove and click **OK**. iii. In the Edited message, confirm that the tags are removed from the clusters, and then click **Close**.

#### 7.1.6 Restart an instance or node

You may need to restart an Elasticsearch instance or node when you modify its configuration or when a cluster or node is in an abnormal state. This topic describes how to restart an instance or node in the console.

**Prerequisites**

Make sure the instance status is Normal.

**Usage notes**

In most cases, if the loads of a cluster are not high and the indexes in the cluster have replica shards, the cluster can still provide services during a restart. However, access timeouts may occur during a restart in some cases. For example, if a number of nodes in the cluster are forced to restart at the same time, the cluster is heavily loaded and is not accessible, the indexes in the cluster do not have replica shards, or large amounts of data are written or queried during a restart or forced restart, access timeouts may occur. In these cases, we recommend that you design a retry mechanism on your client first and restart the cluster during off-peak hours.

**Procedure**

1. Log on to the Alibaba Cloud Elasticsearch console.
2. In the navigation pane on the left, click **Instance List**.
3. On the **Instance List** page, click the ID of the target instance.
4. On the **Basic Information** page, click **Restart** in the upper-right corner.
5. In the **Restart** dialog box, configure the following parameters.

| Parameter | Description |
|---|---|
| Operation Type | Supports Instance Restart and Node Restart: Instance Restart: Restarts all nodes in the instance. Node Restart: Restarts the selected nodes. |
| Select Node | Select the node or nodes to restart. You can select multiple nodes to restart them in a batch. This parameter is displayed only when Operation Type is set to Node Restart. |

| Restart Mode | Supports Restart and Forced Restart: Restart: Perform this operation only when the instance is in the Normal state. Otherwise, you must perform a forced restart. Note During a node restart, the CPU and memory usage of the node may temporarily spike. This can cause service jitter. The service typically recovers after a short period. Forced Restart: If the instance is in an abnormal state (yellow or red), you cannot perform a regular restart. You must perform a forced restart. Important If an instance is in an abnormal state, do not scale it out, restart it, change its password, or perform other configuration changes. Ensure that the instance status returns to Normal (green) before you perform these operations. |
|---|---|

6. Click **OK**.

> **Note:** If you perform a forced restart, you must select the **Confirm Forced Restart** checkbox.

While the instance is restarting, its status is Restarting (yellow). After the restart is complete, the status changes to Normal (green).

#### 7.1.7 Releasing an instance

This topic describes how to release an instance that you no longer need.

**Usage notes**

After a cluster is released, data stored in the cluster cannot be restored. We recommend that you back up data before you release a cluster. For more information, see Manual backup and restoration and Automatic backup. If a cluster fails to be created due to insufficient resources, you can release the instances and cancel the creation task.

**Procedure**

1. Log on to the Alibaba Cloud Elasticsearch console. In the navigation pane on the left, click
**Instance List**.
2. On the **Instance List** page, find the instance that you want to release and click **Release**
**Instance** in the **Actions** column.
3. In the **Confirm Deletion** dialog box, click **OK**.
After the instance is released, a **Deleted Successfully** message is displayed, and the instance is removed from the list.

### 7.2 View cluster information

#### 7.2.1 View instance information

On an instance's basic information page, you can view its ID, status, endpoint, and port, along with information about its Kibana/Dashboard and node visualization. This topic describes how to view information about a cluster.

**View information about an Elasticsearch instance**

1. Log on to the Alibaba Cloud OpenSearch console. In the left navigation pane, click **Instance List**.
2. In the **Instance List**, click the ID of the target instance.
3. On the **Basic Information** page, you can view the basic information, Kibana information,
and visualized node information of the cluster.

| Category | Parameter | Description |
|---|---|---|
| Basic Information | Instance ID | The instance ID is a unique identifier. |
|   | Name | The name of the instance. You can specify a custom name for an instance during creation and use the name to search for instances. |
|   | Instance Type | elasticsearch. |
|   | Status | The status of the cluster. A cluster can be in one of the following states: Normal (green), In effect (yellow), and Failure (red). |
|   | Created At | The time at which the instance was created. |
|   | Chip Architecture | The architecture of the physical server that hosts the instance. |
|   | Version | Elasticsearch 5.x, 6.x, and 7.x are supported. The versions available in the console prevail. |
|   | Region | The region that hosts the instance. |

|   | Network Type | Valid values: VPC (Single Tunnel) and VPC (Any Tunnel). |
|---|---|---|
|   | Internal Endpoint | You can use this endpoint to access the instance service within a VPC. |
|   | Actual IP Address Corresponding to Elasticsearch Domain Name | The actual IP address of the cluster. |
|   | Actual IP Address Corresponding to Kibana Domain Name | The IP address of the Kibana service. |
| Kibana Information | Kibana Console Connection URL | The endpoint of the Kibana console. Click the endpoint to log in to the Kibana console. For more information, see Log in to the Kibana console. |
| Node Visualization | None | Click the icon to enter the node visualization mode. In this mode, you can view the status of the cluster and its nodes. Hover over a node icon to view information such as the node name, node status, CPU specifications, memory size, and storage space. You can also Restart the node or View Node Logs. Click the icon to enter the configuration list mode. In this mode, you can view the configuration of the cluster, such as the specifications and number of data nodes. |

**View information about an OpenSearch instance**

1. Log on to the Alibaba Cloud OpenSearch console. In the left navigation pane, click **Instance List**.
2. In the **Instance List**, click the ID of the target instance.
3. On the **Basic Information** page, view the cluster’s basic information, Dashboard
information, and node visualization information.

| Category | Parameter | Description |
|---|---|---|
|   | Instance ID | The unique ID of the instance. |

| er Guide·Manage cluster | s Elasticsearc |   |
|---|---|---|
| Basic Information |   |   |
|   | Name | The name of the instance. You can specify a custom name when you create the instance and search for instances by name. |
|   | Instance Type | opensearch. |
|   | Status | The status of the instance. Valid states include Normal (green), Activating (yellow), and Failed (red). |
|   | Creation Time | The time when the instance was created. |
|   | Chip Architecture | The architecture of the physical server where the instance is deployed. |
|   | Version | Version 3.1.0 is supported. The actual version is displayed in the console. |
|   | Region | The region where the instance resides. |
|   | Network Type | Supported types: VPC (single tunnel) and VPC (any tunnel). |
|   | Private Endpoint | You can use this endpoint to access the instance service within a VPC. |
|   | Actual IP address of the OpenSearch domain name | The actual IP address of the cluster. |
|   | Actual IP address of the Dashboard domain name | The actual IP address of the Dashboard service. |
| Dashboard Information | Dashboard console URL | Click the Kibana console URL to open the Kibana console. For more information, see Log on to the Dashboards console. |

| Node Visualization | None | Click the icon to enter the node visualization mode. In this mode, you can view the status of the cluster and its nodes. Hover over a node icon to view information such as the node name, node status, CPU specifications, memory size, and storage space. You can also Restart the node or View Node Logs. Click the icon to enter the configuration list mode. In this mode, you can view the configuration of the cluster, such as the specifications and number of data nodes. |
|---|---|---|

#### 7.2.2 View tasks

You can view the progress of different tasks created for an Elasticsearch cluster, including tasks for cluster specification upgrade or downgrade, cluster configuration file update, cluster creation, plug-in installation, and cluster restart. This topic describes how to view the tasks of an Elasticsearch cluster.

**Prerequisites**

The instance status is Normal. A change task is running in the instance.

**Procedure**

1. Log on to the Alibaba Cloud Elasticsearch console. In the left navigation pane, click **Instances**.
2. On the **Instances** page, click the target instance ID.
3. On the Basic Information page, click the
icon in the upper-right corner.
4. In the task list, you can view **Change Start Time**, **Change Type**, and **Change Status**.
5. Click the
icon to the left of the task to view the list that displays the status and uptime of each node in the cluster. Click **Node Information** or **Node Logs** to view the information or logs of the corresponding node.

> **Note:** After the task completes, the icon in the upper-right corner of the Basic Information page changes to
> , and the
> icon in the task list disappears.

#### 7.2.3 View the logs of a node

This topic describes how to view the logs of a node.

**Procedure**

1. Log on to the Alibaba Cloud OpenSearch console. In the navigation pane on the left, click
**Instance List**.
2. On the **Instance List** page, click the ID of the target instance.
3. In the **Node Visualization** section of the **Basic Information** page, move the pointer over
the icon of a node and click **View Node Logs** in the menu that appears.
4. In the Node Logs message, view the logs of the node.

> **Note:** By default, the system displays only the latest 100 log entries of the node. If auto refresh is enabled, log data is updated every 30 seconds. For more information about how to query log details, refer to Operations and Maintenance Guide and go to the corresponding log page.

### 7.3 Scale in or out a cluster

If the configuration of your Elasticsearch cluster does not meet the business requirements, you can scale in or out the Elasticsearch cluster to avoid resource waste or handle unexpected business spikes. This topic describes how to scale in or out an Elasticsearch cluster.

**Prerequisites**

Ensure that the cluster is in a normal state.

**Usage notes**

Cluster scale-in operations are high-risk operations. Improper cluster scale-in operations may lead to insufficient storage space. Assess the risks before you scale in a cluster. Typically, we recommend that you do not scale in Elasticsearch clusters.

**Procedure**

> **Note:** The procedure for scaling OpenSearch instances is similar to that for Elasticsearch instances. This topic uses an Elasticsearch instance as an example.

1. Log on to the Alibaba Cloud OpenSearch service console. In the navigation pane on the left, click
**Instance List**.
2. On the **Instance List** page, click the ID of the target instance.
3. On the right side of the **Node Visualization** section on the **Basic Information** page,
choose **Configuration Update > Upgrade** or **Configuration Update > Downgrade** as needed.
4. On the **Upgrade Instance** or **Downgrade Instance** page, modify the cluster
configuration as needed. For more information about the parameters, see Create a cluster.
5. Click **Submit**.
6. In the **The operation is successful** message, click **OK**.
On the **Instance List** page, wait for the instance status to change to **Normal**, which indicates that the configuration change is complete.

### 7.4 Configuration and management

**management**

#### 7.4.1 Configure clusters

You can use the cluster configuration feature to modify configurations and configure synonyms, security settings, and the YML file of an Elasticsearch cluster. This topic describes how to configure an Elasticsearch cluster.

**Go to the Cluster Configuration page**

1. Log in to the Alibaba Cloud Search and Analytics Service console.
2. In the left-side navigation pane, click **Clusters List**.
3. On the **Instance List** page, click the ID of the cluster that you want to configure.
4. In the left-side navigation pane, choose **Configuration and Management > Cluster**
**Configuration**.

**Configure synonyms**

1. Go to the Cluster Configuration page.
2. In the **Basic Configuration** section, click **Upload** on the right side of **Synonym**
**Dictionary Configuration**.
3. In the **Synonym Dictionary Configuration** panel, click **Configure**.
4. In the **Synonym Dictionary Configuration** text box, enter the name of the bucket that
stores the synonym dictionary file and the name of the file. The synonym dictionary file is used by the synonym dictionary of Elasticsearch. New indexes use the updated synonym dictionary. The synonym dictionary file must be a TXT file encoded in UTF-8. The file must not exceed 1 MB in size. Each line can contain only one synonym expression. Synonym expressions support Solr rules and WordNet rules. The following code provides an example:

```
tomato, tomato Charge => Charge
```

> **Important:** Elasticsearch allows you to upload synonym dictionary files from Object Storage Service (OSS). Make sure that the bucket and Elasticsearch cluster reside in the same region and the file is in the TXT format.
> Before you upload a synonym dictionary file, make sure that the cluster is in the Normal state.
> Elasticsearch supports hot and cold updates for custom dictionaries. Hot updates do not require cluster restarts.

| Parameter | Description |
|---|---|
| Add OSS File | Upload a dictionary file from OSS. The parameter is fixed to Add OSS File and cannot be changed. |
| Bucket Name | Enter the name of the OSS bucket. Important Make sure that the bucket exists and resides in the same region as the Elasticsearch cluster. |
| File Name | Enter the name of the dictionary file to be uploaded. Important The dictionary file must be a TXT file encoded in UTF-8. The file must already be uploaded to the bucket and publicly readable. |

5. Click **Add**.
If the file appears in the **Synonym Dictionary Configuration** text box and **success** is displayed to the right of the file name, the file is added.
6. Click **Save**.
7. After the status of the Elasticsearch cluster becomes Normal, log in to the Kibana console of
the cluster. Then, create indexes, verify synonyms, and upload test data to perform a search test.

> **Important:** When you create an index, you must configure the `settings` and specify

`"synonyms_path":"synonym"` for the `settings` parameter. For more information, see Using Synonyms.

**Security settings**

You can specify whether the specified user can log in to the Kibana console and configure a whitelist to improve cluster and system security. After you create a cluster, you must configure a whitelist. Otherwise, you may encounter issues such as failure to collect monitoring data and failure to log in to the Kibana console.

**Procedure**

1. Go to the Cluster Configuration page.
2. In the **Security Settings** section, click **Modify**.
3. In the **Security Settings** panel, manage the account information and view the certificate
information.

**Manage account information**

View the login name elastic (or admin): The login name of an Elasticsearch cluster is elastic, while the login name of an OpenSearch cluster is admin. The login name, elastic or admin, is equivalent to the administrator account and has all permissions of a superuser.

> **Important:** If you reset the password of the elastic or admin account for an Elasticsearch cluster, only access to the cluster by using the elastic or admin account is affected. Access to the Elasticsearch cluster by using other accounts is not affected. We recommend that you use a custom account to access your Elasticsearch cluster. The custom account must be assigned a role with the required permissions.

kibanaserver: the account used by the Kibana service. The account has the kibana_system permission and is granted only the least permissions required for initializing Kibana. The account cannot be used to access user data. The whitelist of this account must contain the IP address of the Kibana service. If the whitelist is improperly configured, Kibana cannot be accessed. monitoring_collector: the account used by the control service. The account has the aliyun-ops permission. Some control features, such as monitoring data collection and automatic backup, rely on this account. The account is granted the least control permissions. It cannot be used to access user data. The whitelist of this account must contain all possible IP addresses of the control components. If the whitelist is improperly configured, some control features will become unavailable. For example, you may be unable to view monitoring data, enable automatic backup, or perform disaster recovery failovers through Apsara Stack Resilience. Change the password Click **Change Password** to change the password of an account. This operation does not require cluster restarts. Modify the whitelist

> **Important:** You can modify the whitelist only for Elasticsearch clusters, but not for OpenSearch clusters.

Click **Modify Whitelist** to modify the whitelist. Separate multiple IP addresses with commas (,). Example: `127.0.0.1,127.0.0.2` . Specify an IP address range by entering a CIDR block. For example, `1.2.3.4/24` indicates that all IP addresses in the 1.2.3.X CIDR block are allowed to access the Elasticsearch cluster. By default, the whitelist is set to `127.0.0.1` , which means that the corresponding account is not allowed to remotely access the Elasticsearch cluster.

**View certificate information**

The certificate is used by Elasticsearch nodes to communicate with each other. Only nodes with the same certificate can access each other.

> **Important:** The certificate is randomly generated by the system. If you want to use the Cross Data Center Replication (XDCR), Cross-Cluster Search (CCS), or Cross- Cluster Reindex feature in Elasticsearch, make sure that the primary and secondary clusters use the same certificate.
> You can use custom certificates. If you want to change the certificate, contact the O&M engineer.

**Troubleshoot errors and exceptions**

> **Note:** To obtain the IP address of the Kibana service, contact the O&M engineer or refer to the cluster management operations in the O&M guide.

Failure to log in to the Kibana console Error message: Elasticsearch V6.X/7.X: Kibana server is not ready yet Elasticsearch V5.X: Authorization Exception Cause: The whitelist of the kibanaserver account is improperly configured. Solution: Modify the whitelist of the kibanaserver account and add the IP address of the Kibana service to the whitelist of the kibanaserver account. You can still log in to the Kibana console after the Kibana whitelist is disabled Exception: You can still log in to the Kibana console after the Kibana whitelist is disabled. Cause: The Kibana page is not reinitialized. Solution: Contact the O&M engineer to restart the pod that runs the Kibana service. No monitoring data is displayed Exception: "no data" is displayed on the Grafana monitoring page. Cause: The whitelist of the monitoring_collector account is improperly configured. Solution: Modify the whitelist of the monitoring_collector account and add the IP address of the exporter service to the whitelist of the monitoring_collector account. An error is thrown when you access the Elasticsearch plug-in page Error message: 403 Forbidden:[Ip 23.5.**.** is not allow in ip white/black list] Cause: The whitelist of the monitoring_collector account is improperly configured. Solution: Modify the whitelist of the monitoring_collector account and add the IP address of the essen service to the whitelist of the monitoring_collector account. An error is thrown when you access the automatic backup page Error message: proxy request fail Cause: The whitelist of the monitoring_collector account is improperly configured. Solution: Modify the whitelist of the monitoring_collector account and add the IP address of the essen service to the whitelist of the monitoring_collector account. Automatic backup does not take effect Exception: The snapshot is not taken normally after the specified time point. Cause: The whitelist of the monitoring_collector account is improperly configured. Solution: Modify the whitelist of the monitoring_collector account and add the IP address of the snapshot service to the whitelist of the monitoring_collector account. Cross-cluster access error Error message: [][22.0.x.x:9300] general node connection failure Cause: The clusters that need to intercommunicate use different certificates. Solution: Contact the O&M engineer or refer to the cluster management operations in the O&M guide.

**Modify configurations**

> **Important:** The modification operation will cause the Elasticsearch cluster to restart. Proceed with caution.

1. Go to the Cluster Configuration page.
2. In the **Modify Configurations** section, click **Edit** and configure the fields based on your
business requirements. The following tables describe the configuration fields. The fields displayed on the user interface (UI) take precedence.

**Version 7.10.0**

| Field Name | Value description | Description |
|---|---|---|

| apack.accesslog.enabled | Boolean value. Valid values: true false Default value: true. | Access log auditing feature. |
|---|---|---|
| apack.accesslog.search.enable d | Boolean value. Valid values: true false Default value: true. | Feature for printing search request fields. |
| thread pool.write.queue size _ _ | A positive integer. The value is adjusted based on the cluster size and write operation requirements. Default value: 10000. | Specifies the size of the document write queue. |
| thread pool.search.queue size _ _ | A positive integer. The value is adjusted based on the cluster size and load. Default value: 1000. | Specifies the size of the document search queue. |
| cluster.routing.allocation.disk. watermark.low | String. Default value: 85%. You can also set a fixed value for the available disk space, such as 500 MB or 100 GB. | If the disk usage of a node reaches this threshold, the cluster stops allocating new shards to the node. |
| cluster.routing.allocation.disk. watermark.high | String. Default value: 90%. You can also set a fixed value for the available disk space, such as 500 MB or 100 GB. | If the disk usage of a node reaches this threshold, the cluster attempts to reallocate shards to other nodes with lower disk usage. |
| cluster.routing.allocation.disk. watermark.flood stage _ | String. Default value: 95%. You can also set a fixed value for the available disk space, such as 500 MB or 100 GB. | If the disk usage of a node reaches this threshold, the cluster marks the node as unallocatable, attempts to move all shards from the node to other nodes, and sets the shards on the node to read-only. |
| action.auto create index _ _ | Boolean value. Valid values: true false Default value: true. | Specifies whether to automatically create an index if it does not exist when a new document is received. |

| action.destructive requires na _ _ me | Boolean value. Valid values: true false Default value: false. | Specifies whether an index name must be explicitly provided when you delete an index. |
|---|---|---|

**Version 6.8.13**

| Field Name | Value description | Description |
|---|---|---|
| action.auto create index _ _ | Boolean value. Valid values: true false Default value: true. | Specifies whether to automatically create an index if it does not exist when a new document is received. |
| action.destructive requires n _ _ ame | Boolean value. Valid values: true false Default value: false. | Specifies whether an index name must be explicitly provided when you delete an index. |
| thread pool.write.queue size _ _ | A positive integer. The value is adjusted based on the cluster size and write operation requirements. Default value: 200. | Specifies the size of the document write queue. |
| thread pool.search.queue siz _ _ e | A positive integer. The value is adjusted based on the cluster size and load. Default value: 1000. | Specifies the size of the document search queue. |
| cluster.routing.allocation.disk. watermark.low | String. Default value: 85%. You can also set a fixed value for the available disk space, such as 500 MB or 100 GB. | If the disk usage of a node reaches this threshold, the cluster stops allocating new shards to the node. |
| cluster.routing.allocation.disk. watermark.high | String. Default value: 90%. You can also set a fixed value for the available disk space, such as 500 MB or 100 GB. | If the disk usage of a node reaches this threshold, the cluster attempts to reallocate shards to other nodes with lower disk usage. |

| cluster.routing.allocation.disk. watermark.flood stage _ | String. Default value: 95%. You can also set a fixed value for the available disk space, such as 500 MB or 100 GB. | If the disk usage of a node reaches this threshold, the cluster marks the node as unallocatable, attempts to move all shards from the node to other nodes, and sets the shards on the node to read- only. |
|---|---|---|

**Version 5.5.3**

| Field Name | Value description | Description |
|---|---|---|
| thread pool.bulk.queue size _ _ | A positive integer. The value is adjusted based on the cluster size and write operation requirements. Default value: 200. | Specifies the size of the queue for batch document write operations. |
| thread pool.search.queue size _ _ | A positive integer. The value is adjusted based on the cluster size and load. Default value: 1000. | Specifies the size of the document search queue. |
| cluster.routing.allocation.disk. watermark.low | String. Default value: 85%. You can also set a fixed value for the available disk space, such as 500 MB or 100 GB. | If the disk usage of a node reaches this threshold, the cluster stops allocating new shards to the node. |
| cluster.routing.allocation.disk. watermark.high | String. Default value: 90%. You can also set a fixed value for the available disk space, such as 500 MB or 100 GB. | If the disk usage of a node reaches this threshold, the cluster attempts to reallocate shards to other nodes with lower disk usage. |
| action.auto create index _ _ | Boolean value. Valid values: true false Default value: true. | Specifies whether to automatically create an index if it does not exist when a new document is received. |
| action.destructive requires na _ _ me | Boolean value. Valid values: true false Default value: false. | Specifies whether an index name must be explicitly provided when you delete an index. |

3. After you confirm the configuration, click **Submit**.

**Configure the YML file**

1. Go to the Cluster Configuration page.
2. In the **YML File Configuration** section, click **Modify Configuration** on the right side.
3. In the **YML File Configuration** panel, configure the following parameters.

> **Warning:** Improper YML file configurations may cause cluster unavailability or data loss. Do not modify the configuration unless it is necessary, especially the preset settings.

| Parameter | Description |
|---|---|
| Auto Indexing | Specifies whether to automatically create an index if a new document is uploaded to the Elasticsearch cluster but no index exists. If you select Custom, partial indexes are automatically created. You must use a regular expression to specify the name of the index that you want to create. For example, if you set the value to +.*,-* , only system indexes that start with . are automatically created. This parameter corresponds to the action.auto create index _ _ configuration item in the YML file. The default value of this configuration item is true. Important The indexes that are automatically created may not meet your business requirements. Therefore, we recommend that you perform an assessment before you enable the system to automatically create indexes. |
| Index Deletion | Specifies whether to specify the index name when you delete an index. If you set this parameter to Allow Wildcards, you can use wildcard characters to delete multiple indexes at a time. Deleted indexes cannot be restored. Proceed with caution. This parameter corresponds to the action.destructive requires name configuration item in the _ _ YML file. The default value of this configuration item is false. |
| Other Configurations | Enter custom configurations. Warning Incorrect YML file configurations may cause cluster unavailability or data loss. If you are not an O&M engineer, we recommend that you do not customize the configuration. |

4. Select **This operation will restart the cluster. Continue?** and click **OK**.
Then, the system restarts the Elasticsearch cluster. After the cluster is restarted, the configurations in the YML file are updated.

#### 7.4.2 Plugin configuration

##### 7.4.2.1 Supported plugins

###### 7.4.2.1.1 Elasticsearch plugins

This topic lists the supported Elasticsearch plugins and their versions.

**Version 7.10.0**

| Plugin name | Built-in | Plugin version | Description |
|---|---|---|---|
| a-pack-core | Built-in | 7.10.0 | The A-Pack core plugin. It provides basic feature support and integration capabilities for Alibaba Cloud Elasticsearch. |
| aliyun-codec | Non-built-in | 7.10.0 | The Alibaba Cloud codec plugin. It optimizes index storage and query performance and supports custom data encoding policies. |
| aliyun-knn | Built-in | 7.10.0 | The Alibaba Cloud KNN plugin. It supports k-nearest neighbor (k-NN) vector search for similarity retrieval in AI and machine learning (ML) scenarios. |
| aliyun- optimization | Built-in | 7.10.0 | The Alibaba Cloud performance optimization plugin. It improves the efficiency of Elasticsearch clusters using storage and query optimization policies. |
| aliyun-qos | Non-built-in | 7.10.0 | The Alibaba Cloud Quality of Service (QoS) plugin. It manages resource allocation and request priorities to ensure the performance of critical tasks. |
| analysis-aliws | Custom | 7.10.0 | The Alibaba Cloud analysis (AliWS) plugin. It provides custom text processing features, such as industry- specific word segmentation. |
| analysis-icu | Built-in | 7.10.0 | The ICU analysis plugin. It integrates the ICU module from Lucene to support multilingual text processing, such as for Japanese, Korean, and Arabic. |
| analysis-ik | Built-in | 7.10.0 | The IK Chinese analysis plugin. It provides efficient Chinese word segmentation for scenarios such as E- commerce and news. |

| analysis- kuromoji | Built-in | 7.10.0 | The Japanese (Kuromoji) analysis plugin. It supports tokenization and grammatical parsing for Japanese text. |
|---|---|---|---|
| analysis- phonetic | Built-in | 7.10.0 | The phonetic analysis plugin. It uses a phonetic feature filter to enable fuzzy matching based on pronunciation, such as for name searches. |
| analysis-pinyin | Built-in | 7.10.0 | The Pinyin analysis plugin. It converts Chinese characters to Pinyin for tokenization and supports Chinese Pinyin search. |
| analysis-smartcn | Built-in | 7.10.0 | The Smart Chinese analysis plugin. It integrates the Smart Chinese module from Lucene to provide basic Chinese word segmentation. |
| analysis-stempel | Built-in | 7.10.0 | The Polish (Stempel) analysis plugin. It supports tokenization and morphological stemming for Polish text. |
| analysis- ukrainian | built-in | 7.10.0 | The Ukrainian analysis plugin. It supports tokenization and grammatical processing for Ukrainian text. |
| elasticsearch- repository-oss | Built-in | 7.10.0 | The OSS repository plugin. It lets you store Elasticsearch snapshots in Alibaba Cloud Object Storage Service (OSS) for long-term backup and recovery. |
| faster-bulk | No | 7.10.0 | The batch operation optimization plugin. It improves data write performance and reduces latency for batch indexing operations. |
| hybrid-cloud | Built-in | 7.10.0 | The hybrid cloud plugin. It supports hybrid deployments of Alibaba Cloud Elasticsearch with on-premises data centers and enables cross-environment data synchronization. |
| ingest- attachment | Built-in | 7.10.0 | The ingest attachment processor plugin. It uses Apache Tika to parse and extract text from attachments such as PDF and Office files. |

| mapper- murmur3 | Built-in | 7.10.0 | The Murmur3 hash mapping plugin. It computes and stores the hash of a field's value at index time. This is used to deduplicate data or accelerate searches. |
|---|---|---|---|
| mapper-size | Built-in | 7.10.0 | The document size mapping plugin. It records the original, uncompressed size of a document at index time to help monitor storage overhead. |
| opendistro- index- management | Non-built-in | 7.10.0 | The Open Distro index state management plugin. It automates the index lifecycle, such as scrolling, applying retention policies, and migrating between hot, warm, and cold states. |
| opendistro-job- scheduler | Custom | 7.10.0 | The Open Distro job scheduler plugin. It provides a distributed service for scheduling periodic tasks, such as monitoring and maintenance tasks. |
| opendistro secu _ rity | Built-in | 7.10.0 | The Open Distro security plugin. It provides access control, identity verification, and encryption features to secure Elasticsearch clusters. |
| repository-hdfs | Built-in | 7.10.0 | The HDFS repository plugin. It lets you store snapshots in Hadoop Distributed File System (HDFS). This is useful for big data ecosystem integration. |
| repository-s3 | Built-in | 7.10.0 | The S3 repository plugin. It lets you store snapshots in AWS S3 Object Storage Service. This is useful for cross- cloud backup scenarios. |
| sql | Built-in | 7.10.0 | The SQL query plugin. It lets you query Elasticsearch data using SQL syntax, which reduces the learning curve for users. |
| xdcr | Non-built-in | 7.10.0 | The cross-data center replication (XDCR) plugin. It enables multi-region data synchronization and high availability, and supports disaster recovery and data localization. |

**Version 6.8.13**

| Plugin name | Built-in | Plugin version | Description |
|---|---|---|---|
| a-pack- repository-oss | Built-in | 6.8.13 | The A-Pack OSS repository plugin. It lets you store Elasticsearch snapshots in Alibaba Cloud OSS for long-term backup and recovery. |
| a-pack-xdcr | Built-in | 6.8.13 | The A-Pack XDCR plugin. It enables multi- region data synchronization and high availability, and supports disaster recovery and data localization. |
| aliyun-knn | Built-in | 6.8.13 | The Alibaba Cloud KNN plugin. It supports k-NN vector search for similarity retrieval in AI and ML scenarios. |
| analysis-aliws | Built-in | 6.8.13 | The Alibaba Cloud analysis (AliWS) plugin. It provides custom text processing features, such as industry-specific word segmentation. |
| analysis-icu | Built-in | 6.8.13 | The ICU analysis plugin. It integrates the ICU module from Lucene to support multilingual text processing, such as for Japanese, Korean, and Arabic. |
| analysis-ik | Built-in | 6.8.13 | The IK Chinese analysis plugin. It provides efficient Chinese word segmentation for scenarios such as E-commerce and news. |
| analysis- kuromoji | Built-in | 6.8.13 | The Japanese (Kuromoji) analysis plugin. It supports tokenization and grammatical parsing for Japanese text. |
| analysis- phonetic | Built-in | 6.8.13 | The phonetic analysis plugin. It uses a phonetic feature filter to enable fuzzy matching based on pronunciation, such as for name searches. |
| analysis-pinyin | Built-in | 6.8.13 | The Pinyin analysis plugin. It converts Chinese characters to Pinyin for tokenization and supports Chinese Pinyin search. |

| analysis-smartcn | Built-in | 6.8.13 | The Smart Chinese analysis plugin. It integrates the Smart Chinese module from Lucene to provide basic Chinese word segmentation. |
|---|---|---|---|
| analysis-stempel | Built-in | 6.8.13 | The Polish (Stempel) analysis plugin. It supports tokenization and morphological stemming for Polish text. |
| analysis- ukrainian | Built-in | 6.8.13 | The Ukrainian analysis plugin. It supports tokenization and grammatical processing for Ukrainian text. |
| ingest- attachment | Built-in | 6.8.13 | The ingest attachment processor plugin. It uses Apache Tika to parse and extract text from attachments such as PDF and Office files. |
| mapper- murmur3 | Built-in | 6.8.13 | The Murmur3 hash mapping plugin. It computes and stores the hash of a field's value at index time. This is used to deduplicate data or accelerate searches. |
| mapper-size | Built-in | 6.8.13 | The document size mapping plugin. It records the original, uncompressed size of a document at index time to help monitor storage overhead. |
| opendistro-job- scheduler | Built-in | 6.8.13 | The Open Distro job scheduler plugin. It provides a distributed service for scheduling periodic tasks, such as monitoring and maintenance tasks. |
| opendistro alerti _ ng | Non-built-in | 6.8.13 | The Open Distro alerting plugin. It supports real-time alerting and notifications, such as email and Slack messages, based on search results. |
| opendistro index _ management _ | Built-in | 6.8.13 | The Open Distro index management plugin. It automates the index lifecycle, such as scrolling, applying retention policies, and migrating between hot, warm, and cold states. |
| opendistro secur _ ity | Built-in | 6.8.13 | The Open Distro security plugin. It provides access control, identity verification, and encryption features to secure Elasticsearch clusters. |

| opendistro sql _ | Non-built-in | 6.8.13 | The Open Distro SQL plugin. It lets you query Elasticsearch data using SQL syntax, which reduces the learning curve for users. |
|---|---|---|---|
| repository-hdfs | Built-in | 6.8.13 | The HDFS repository plugin. It lets you store snapshots in HDFS. This is useful for big data ecosystem integration. |
| repository-s3 | built-in | 6.8.13 | The S3 repository plugin. It lets you store snapshots in AWS S3 Object Storage Service. This is useful for cross-cloud backup scenarios. |
| sqlplugin | Built-in | 6.8.13 | The SQL query plugin. It lets you query Elasticsearch data using SQL syntax and provides SQL interface support that is not from Open Distro. |

**Version 5.5.3**

| Plugin name | Built-in | Plugin version | Description |
|---|---|---|---|
| analysis-icu | Built-in | 5.5.3 | The ICU analysis plugin. It integrates the ICU module from Lucene to support Unicode and multilingual text processing, such as for Japanese, Korean, and Arabic. |
| analysis-ik | Built-in | 5.5.3 | The IK Chinese analysis plugin. It uses IK Analyzer to provide efficient Chinese word segmentation and search optimization. |
| analysis- kuromoji | Built-in | 5.5.3 | The Japanese (Kuromoji) analysis plugin. It integrates the Kuromoji module from Lucene to support Japanese text analysis. |
| analysis- phonetic | Built-in | 5.5.3 | The phonetic analysis plugin. It uses a phonetic feature filter to enable fuzzy matching based on pronunciation, such as for name searches. |
| analysis-pinyin | Built-in | 5.5.3 | The Pinyin analysis plugin. It converts Chinese characters to Pinyin for tokenization and supports Chinese Pinyin search. |

| analysis-smartcn | Built-in | 5.5.3 | The Smart Chinese analysis plugin. It integrates the Smart Chinese module from Lucene to provide basic Chinese word segmentation. |
|---|---|---|---|
| analysis-stempel | Built-in | 5.5.3 | The Polish (Stempel) analysis plugin. It integrates the Stempel module from Lucene to support Polish text processing. |
| analysis- ukrainian | Built-in | 5.5.3 | The Ukrainian analysis plugin. It integrates the UkrainianMorfologikAnalyzer from Lucene to support Ukrainian text analysis. |
| elasticsearch- repository-oss | Built-in | 5.5.3 | The Alibaba Cloud OSS snapshot repository plugin. It lets you store Elasticsearch snapshots in Alibaba Cloud OSS. |
| gab-paas-plugin | Custom | 5.5.3 | The GAB Platform as a Service (PaaS) plugin. It provides feature support for integration with the Alibaba Cloud PaaS platform. Specific features depend on the business scenario. |
| ingest- attachment | Built-in | 5.5.3 | The ingest attachment processor plugin. It uses Apache Tika to parse and extract text from attachments such as PDF and Office files. |
| ingest-geoip | Built-in | 5.5.3 | The GeoIP analysis processor plugin. It uses the Maxmind database to look up geographic location data from an IP address. |
| ingest-user- agent | Built-in | 5.5.3 | The user agent information extraction processor plugin. It extracts information about devices, browsers, and more from a user agent string. |
| mapper- attachments | Built-in | 5.5.3 | The attachment mapping plugin. It lets you store the content of rich text files, such as PDF and Office documents, as a field and perform full-text searches on it. |
| mapper- murmur3 | Built-in | 5.5.3 | The Murmur3 hash mapping plugin. It computes and stores the hash of a field's value at index time. |
| mapper-size | Built-in | 5.5.3 | The document size mapping plugin. It records the original, uncompressed size of a document at index time. |

| pangu | Built-in | 5.5.3 | The Pangu repository plugin. It lets you store snapshots in the Alibaba Cloud Pangu distributed storage system. |
|---|---|---|---|
| repository-hdfs | Built-in | 5.5.3 | The HDFS repository plugin. It lets you store snapshots in HDFS. |
| repository-s3 | Built-in | 5.5.3 | The S3 repository plugin. It lets you store snapshots in AWS S3 Object Storage Service. |
| search-guard-5 | Built-in | 5.5.3 | The Search Guard 5 security plugin. It provides access control, authentication, and authorization features for Elasticsearch 5. |
| sql | Built-in | 5.5.3 | The SQL query plugin. It lets you query Elasticsearch data using SQL syntax. |

###### 7.4.2.1.2 Kibana plugins

This topic lists the plugins supported by Kibana and their corresponding versions.

**Version 7.10.0**

| Plugin name | Built-in | Plugin version | Description |
|---|---|---|---|
| opendistro- alerting | Non-built-in | 7.10.0 | Open Distro Kibana alerting plugin. Create, manage, and trigger alert rules based on Elasticsearch data in Kibana. |

**Version 6.8.13**

| Plugin name | Built-in | Plugin version | Description |
|---|---|---|---|
| bsearch querybuild _ er | Non-built-in | 6.8.13 | BSearch query builder plugin. Provides a visualization tool to build and test BSearch query statements. |
| kibana- prometheus- exporter | Non-built-in | 6.8.13 | Kibana Prometheus metrics exporter plugin. Exports Kibana monitoring data (such as performance metrics) to the Prometheus monitoring system. |

| opendistro-alerting | Non-built-in | 6.8.13 | Open Distro Kibana alerting plugin. Create, manage, and trigger alert rules based on Elasticsearch data in Kibana. |
|---|---|---|---|

**Version 5.5.3**

| Plugin name | Built-in | Plugin version | Description |
|---|---|---|---|
| searchguard | Built-in | 5.5.3 | Search Guard Kibana plugin. Integrates Elasticsearch security features (such as access control and identity verification) into Kibana for unified permission management. |

###### 7.4.2.1.3 OpenSearch plugins

This topic lists the plugins supported by OpenSearch and their corresponding versions.

**Version 3.1.0**

| Plugin name | Built-in | Plugin version | Description |
|---|---|---|---|
| analysis-ik | Built-in | 3.1.0 | The IK analyzer for OpenSearch. |
| opensearch- repository-oss- plugin | Built-in | 3.1.0 | Enables integration with Alibaba Cloud OSS as a snapshot repository for backup and recovery operations. |
| prometheus- exporter | Built-in | 3.1.0 | Exposes OpenSearch metrics in Prometheus format. This supports monitoring and alerting through Prometheus and Grafana. |
| opensearch- alerting | Built-in | 3.1.0 | Provides real-time alerting based on search results. It lets you define triggers and actions. |
| opensearch- asynchronous- search | Built-in | 3.1.0 | Supports long-running searches by executing queries asynchronously and retrieving the results later. |
| opensearch-cross- cluster-replication | Built-in | 3.1.0 | Enables cross-cluster replication for high availability, disaster recovery, and data localization. |

| opensearch- custom-codecs | Built-in | 3.1.0 | Adds support for custom index codecs to optimize storage and performance for specific use cases. |
|---|---|---|---|
| opensearch-flow- framework | Built-in | 3.1.0 | Provides a framework to build and manage guided workflows and multi-step processes. |
| opensearch- geospatial | Built-in | 3.1.0 | Extends the geospatial search and analysis capabilities of OpenSearch, including GeoJSON and shape queries. |
| opensearch-index- management | Built-in | 3.1.0 | Automates index lifecycle management, including rollovers, retention policies, and state transitions (hot/warm/cold). |
| opensearch-job- scheduler | Built-in | 3.1.0 | Provides a distributed task scheduling service for periodic tasks, such as monitoring and maintenance. |
| opensearch-knn | Built-in | 3.1.0 | Supports k-nearest neighbor (k-NN) vector search for similarity search and AI/ML applications. |
| opensearch-ltr | Built-in | 3.1.0 | Supports learning to rank (LTR) based on machine learning models to improve search relevance. |
| opensearch- notifications | Built-in | 3.1.0 | A centralized notification service that sends alerts through channels such as email, Slack, and Chime. |
| opensearch- notifications-core | Built-in | 3.1.0 | The core module of the notification system. It provides APIs and a messaging infrastructure. |
| opensearch- observability | Built-in | 3.1.0 | A unified observability solution for logs, metrics, traces, and user experience. |
| opensearch- reports-scheduler | Built-in | 3.1.0 | Schedules and distributes reports generated from dashboards and visualizations on a regular basis. |
| opensearch- security | Built-in | 3.1.0 | A comprehensive security plugin that provides authentication, authorization, encryption, and audit logs. |

| opensearch-sql | Built-in | 3.1.0 | Provides a SQL interface to query OpenSearch indexes using familiar SQL syntax. |
|---|---|---|---|
| opensearch- system-templates | Built-in | 3.1.0 | Manages system-generated index templates used for internal OpenSearch features and plugins. |
| query-insights | Built-in | 3.1.0 | Analyzes search query performance, latency, and resource usage to optimize relevance and efficiency. |

###### 7.4.2.1.4 Dashboard plugins

This topic lists the supported Dashboard plugins and their versions.

**Version 3.1.0**

| Plugin name | Built-in | Plugin version | Description |
|---|---|---|---|
| indexManagement Dashboards | Built-in | 3.1.0 | Provides an interface to monitor and manage index lifecycles. Supported operations include rollover, deletion, and state transition. |

##### 7.4.2.2 Install or uninstall plug-ins

The plug-in configuration feature lets you manually install or uninstall plug-ins that have been uploaded to the Operations and Maintenance (O&M) platform.

**Prerequisites**

The instance status is Normal, and an O&M engineer has uploaded the required plug-in to the O&M platform.

**Procedure**

1. Log on to the Alibaba Cloud Elasticsearch console. In the navigation pane on the left, click
**Instance List**.
2. On the **Instance List** page, click the ID of the target instance.
3. In the navigation pane on the left, choose **Configuration and Management > Plug-in**
**Configuration**.
4. On the **Plug-ins** page, you can perform the following operations:
Click the **Default Plug-ins** tab to view the plug-ins that are installed by default. Click the **Custom Plug-ins** tab to **install** or **uninstall** a plug-in. In the dialog box that appears, read the risk information and click **Confirm**.

> **Warning:** After you install or uninstall a plug-in, the cluster is restarted. Proceed with caution.

After the cluster is restarted and the status of the plug-in displays Installed or Uninstalled, the plug-in is successfully installed or uninstalled.

#### 7.4.3 Security settings

This topic describes how to configure security settings in Elasticsearch, including configuring an IP address whitelist for accessing an Elasticsearch cluster over Virtual Private Cloud (VPC) and enabling HTTPS to manage access permissions and ensure data transmission security.

**Go to the Security page**

1. Log in to the Alibaba Cloud Search and Analytics Service console.
2. In the left-side navigation pane, click **Clusters List**.
3. On the **Instance List** page, find the cluster that you want to manage and click its ID.
4. In the left-side navigation pane of the page that appears, choose **Configuration and**
**Management > Security**. By default, the **Network Settings** page appears.

**Configure a VPC whitelist**

Before you access an Elasticsearch cluster over a VPC, you need to add the IP address of your device to a whitelist of the cluster. If access to an Elasticsearch cluster fails, you can follow the instructions in this topic to check whether you add the right IP address to the whitelist of the cluster.
1. Go to the Security page.
2. On the right side of **Private IP Address Whitelist**, click **Add IP Address Whitelist**.
3. In the **Add IP Address Whitelist** dialog box, configure **VPC** and **IP Addresses in**
**Whitelist**.
4. Click **OK**.
To modify or remove the configured IP address whitelist, click **Modify** or **Delete** in the
**Actions** column.

**Enable HTTPS**

Hyper Text Transfer Protocol over Secure Socket Layer (HTTPS) is a security-enhanced version of HTTP. HTTPS works with Secure Socket Layer (SSL) to ensure the security of data transmission. HTTPS uses HTTP for communication. SSL is used to encrypt data. To ensure data security, we recommend that you enable HTTPS.

> **Important:** By default, the HTTPS feature is disabled for Elasticsearch clusters. we recommend that you manually enable this feature. By default, the HTTPS feature is enabled for OpenSearch clusters and cannot be disabled.

1. Go to the Security page.
2. Turn on the switch next to **Enable HTTPS** to enable HTTPS.

#### 7.4.4 Data backup

##### 7.4.4.1 Manual backup and restoration

You can call the snapshot API operation to back up or restore data for your Elasticsearch cluster. The snapshot API operation retrieves the status and data of your Elasticsearch cluster and stores them to a shared repository.

**Background information**

The first snapshot is a full copy of the data in a cluster. Subsequent snapshots store only incremental data. When the system creates subsequent snapshots, it only adds data to or removes data from the previous snapshot. Therefore, less time is required to create a subsequent snapshot than the first snapshot. For more information about Elasticsearch cluster backup and restoration, see Snapshot and restore API.

**Usage notes**

This topic uses the following markers to provide descriptions for code: <1>, <2>, and <3>. Remove these markers before you run the code. You can run the code provided in this topic in the Kibana console of your Elasticsearch cluster. For more information, see Log in to the Kibana console.

**Create a repository**

```json
PUT _snapshot/my_backup
   "type": "oss",
    "settings": {
        "endpoint": "http://oss-cn-hangzhou-internal.aliyuncs.com", <1>
        "access_key_id": "xxxx",
        "secret_access_key": "xxxxxx",
        "bucket": "xxxxxx", <2>
        "compress": true,
        "base_path": "snapshot/" <3>
```

<1>: The `endpoint` parameter specifies the internal endpoint of an Object Storage Service (OSS) bucket. <2>: The bucket parameter specifies the name of the OSS bucket. <3>: The base_path parameter specifies the path of the repository. The default value is the root directory.

**Set the size of each part**

You can upload large volumes of data to an OSS bucket in multiple parts. When you upload the data, you can use the `chunk_size` parameter to set the size of each part. Example:

```json
POST _snapshot/my_backup/ <1>
    "type": "oss",
    "settings": {
        "endpoint": "http://oss-cn-hangzhou-internal.aliyuncs.com",
        "access_key_id": "xxxx",
        "secret_access_key": "xxxxxx",
        "bucket": "xxxxxx",
        "chunk_size": "500mb",
        "base_path": "snapshot/" <2>
```

<1>: the request method.

> **Important:** When you update the settings of a repository, use the POST method instead of the PUT method. If you use the PUT method for the update, other settings of the repository are also updated.

<2>: the path of the repository. The default value is the root directory.

**Query repository information**

```
GET _snapshot
```

You can also use the `GET _snapshot/my_backup` command to query the information of a specified repository.

**Commands for creating snapshots**

The following command is a basic command that is used to create a snapshot:

```
PUT _snapshot/my_backup/snapshot_1
```

This command creates the `snapshot_1` snapshot for all enabled indexes. The snapshot is stored in the `my_backup` repository. After you run the command, the system immediately returns a response and creates the snapshot in the backend. If you want the system to return a response after the snapshot is created, specify the `wait_for_completion` parameter in the command. Example:

```
PUT _snapshot/my_backup/snapshot_1?wait_for_completion=true
```

After you run the command, the system does not return a response until the snapshot is created. If a large snapshot is used, it takes a long time to return the snapshot. The time varies based on the size of the snapshot. For more information, see the Monitor snapshot restoration progress section in this topic.

**Create a snapshot for specified indexes**

By default, a snapshot contains all enabled indexes. If Kibana is used when you create a snapshot, you may want to ignore all diagnostic indexes (the `.kibana` indexes) because of limited disk space. To create a snapshot for specified indexes, run the following command.

> **Important:** A repository stores multiple snapshots. Each snapshot is a copy of all indexes, specified indexes, or a single index in a cluster. When you create a snapshot, specify the desired indexes and make sure that the snapshot name is unique.

```json
PUT _snapshot/my_backup/snapshot_2
    "indices": "index_1,index_2"
```

The preceding command creates a snapshot only for the indexes named `index1` and

```
 index2 .
```

**Query snapshot information**

In some cases, you may need to query snapshot information. For example, a snapshot name that contains a date is hard to remember, such as `backup_2014_10_28` . To query the information of a snapshot, send a `GET` request that contains both the repository name and snapshot name. Example:

```
GET _snapshot/my_backup/snapshot_2
```

The response contains detailed information of the snapshot:

```json
"snapshots": [
      "snapshot": "snapshot_2",
      "indices": [
         ".marvel_2014_28_10",
         "index1",
         "index2"
```

`],`

```json
      "state": "SUCCESS",
      "start_time": "2014-09-02T13:01:43.115Z",
      "start_time_in_millis": 1409662903115,
      "end_time": "2014-09-02T13:01:43.439Z",
      "end_time_in_millis": 1409662903439,
      "duration_in_millis": 324,
      "failures": [],
      "shards": {
         "total": 10,
         "failed": 0,
         "successful": 10
```

`]` You can replace the snapshot name in the preceding command with `_all` to query all snapshots in the repository. Example:

```
GET _snapshot/my_backup/_all
```

**Delete a snapshot**

You can specify a repository name and a snapshot name in a `DELETE` request to delete the specified snapshot. Example:

```
DELETE _snapshot/my_backup/snapshot_2
```

> **Important:** You can delete snapshots only by calling the DELETE API operation. A snapshot may be associated with the data in other snapshots. The DELETE API operation does not delete files that are still being used by other snapshots. It deletes only the files that are associated with the deleted snapshot and are no longer used by other snapshots.
> If you choose to manually delete a snapshot, you may delete files that are used by other snapshots. This can cause data loss.

**Monitor snapshot restoration progress**

You can specify the `wait_for_completion` parameter to wait for the snapshot restoration process to complete. However, it takes a long period of time to restore a medium-sized cluster from a snapshot. In this case, you can use one of the following methods to view the detailed snapshot restoration progress. Send a `GET` request with the snapshot ID specified. Example:

```
GET _snapshot/my_backup/snapshot_3
```

If the system is creating the snapshot when you run the preceding command, the information of the creation task is returned, such as the start time and duration of the task.

> **Important:** The preceding command shares a thread pool with the command used to create a snapshot. Therefore, if you create a snapshot for large shards, the preceding command has to wait until the resources that are used by the snapshot creation command in the thread pool are released.

Call the _status API operation to query the snapshot status. Example:

```json
"snapshots": [
      "snapshot": "snapshot_3",
      "repository": "my_backup",
      "state": "IN_PROGRESS", <1>
      "shards_stats": {
         "initializing": 0,
         "started": 1, <2>
         "finalizing": 0,
         "done": 4,
         "failed": 0,
         "total": 5
```

`},`

```json
      "stats": {
         "number_of_files": 5,
         "processed_files": 5,
         "total_size_in_bytes": 1792,
         "processed_size_in_bytes": 1792,
         "start_time_in_millis": 1409663054859,
         "time_in_millis": 64
```

`},`

```json
      "indices": {
         "index_3": {
            "shards_stats": {
               "initializing": 0,
               "started": 0,
               "finalizing": 0,
               "done": 5,
               "failed": 0,
               "total": 5
```

`},`

```json
            "stats": {
               "number_of_files": 5,
               "processed_files": 5,
               "total_size_in_bytes": 1792,
               "processed_size_in_bytes": 1792,
               "start_time_in_millis": 1409663054859,
               "time_in_millis": 64
```

`},`

```json
            "shards": {
               "0": {
                  "stage": "DONE", <3>
                  "stats": {
                     "number_of_files": 1,
                     "processed_files": 1,
                     "total_size_in_bytes": 514,
                     "processed_size_in_bytes": 514,
                     "start_time_in_millis": 1409663054862,
                     "time_in_millis": 22
```

`},`

```
               ...
```

<1>: the status of the snapshot. If a snapshot is being created, the value of the field is

```
 IN_PROGRESS .
```

<2>: the number of shards that are being transmitted. If a value of 1 is returned, one shard is being transmitted to the snapshot, and the other shards have been transmitted. The value of the `shards_stats` parameter indicates the status of the snapshot and the statistics about each index and shard. This parameter allows you to obtain the details of the snapshot creation progress. <3>: The snapshot can be in one of the following states: `INITIALIZING` : The shard is verifying the status of the cluster to check whether the shard can be stored in a snapshot. In most cases, this process is fast. `STARTED` : Data is being transmitted to the repository. `FINALIZING` : Data is transmitted, and the shard is sending snapshot metadata. `DONE` : The snapshot is created. `FAILED` : An error occurred during the snapshot creation. The shard, index, or snapshot cannot be created. In this case, analyze the logs for detailed information.

**Cancel a snapshot**

To cancel a snapshot, run the following command when the snapshot is being created. If the snapshot is being created, the system stops the creation and deletes the snapshot from the repository.

```
DELETE _snapshot/my_backup/snapshot_3
```

**Restore indexes from a snapshot**

To restore indexes from a snapshot, run the repository creation command on the Elasticsearch cluster to which the indexes are restored. You can use one of the following methods to restore indexes from a snapshot: To restore indexes from a specified snapshot, append `_restore` to the snapshot ID in the command. Example:

```
POST _snapshot/my_backup/snapshot_1/_restore
```

After you run this command, the system restores all indexes in the snapshot by default. For example, if the `snapshot_1` snapshot contains five indexes, all these indexes are restored to the Elasticsearch cluster. You can also specify the indexes that you want to restore. For more information, see the Create a snapshot for specified indexes section of this topic. Restore specified indexes and rename the indexes. If you want to only verify or process the data in indexes and do not want to overwrite the data, use this method to restore the indexes. Example:

```json
POST /_snapshot/my_backup/snapshot_1/_restore
 "indices": "index_1", <1>
 "rename_pattern": "index_(.+)", <2>
 "rename_replacement": "restored_index_$1" <3>
```

| In this example, the | index 1 _ . |
|---|---|
| restored index 1 _ _ |   |

In this example, the `index_1` index is restored to your Elasticsearch cluster and renamed <1>: The system restores only the `index_1` index from the snapshot. <2>: The system searches for the index that is being restored and matches the index name with the provided index template. <3>: The system renames the matched index. If you want the system to return a response after it restores the index, specify the `wait_for_completion` parameter in the command.

```
POST _snapshot/my_backup/snapshot_1/_restore?wait_for_completion=true
```

After you call the _restore API operation, the system immediately returns a response and restores the index in the backend. If you want the system to return a response after the index is restored, specify the `wait_for_completion` parameter in the command. Example:

**Monitor index restoration progress**

> **Note:** Restoring data from a repository applies the existing restoration mechanism in Elasticsearch. Restoring shards from a repository is the same as restoring data from a node.

You can call the recovery API operation to monitor the progress of an index restoration task. Monitor the restoration of a specified index. Example:

```
GET restored_index_3/_recovery
```

The recovery API operation is a general-purpose operation. It can be used to query the status of the shards that are being transmitted to your Elasticsearch cluster. Monitor the restoration of all indexes on the cluster. This may include shards that are irrelevant to the restoration process.

```
GET /_recovery/
```

Sample response:

```json
"restored_index_3" : {
 "shards" : [ {
   "id" : 0,
   "type" : "snapshot", <1>
   "stage" : "index",
   "primary" : true,
   "start_time" : "2014-02-24T12:15:59.716",
   "stop_time" : 0,
   "total_time_in_millis" : 175576,
   "source" : { <2>
     "repository" : "my_backup",
     "snapshot" : "snapshot_3",
     "index" : "restored_index_3"
```

`},`

```json
   "target" : {
     "id" : "ryqJ5lO5S4-lSFbGntkEkg",
     "hostname" : "my.fqdn",
     "ip" : "10.0.**.**",
     "name" : "my_es_node"
```

`},`

```json
   "index" : {
     "files" : {
       "total" : 73,
       "reused" : 0,
       "recovered" : 69,
       "percent" : "94.5%" <3>
```

`},`

```json
     "bytes" : {
       "total" : 79063092,
       "reused" : 0,
       "recovered" : 68891939,
       "percent" : "87.1%"
```

`},`

```json
     "total_time_in_millis" : 0
```

`},`

```json
   "translog" : {
     "recovered" : 0,
     "total_time_in_millis" : 0
```

`},`

```json
   "start" : {
     "check_index_time" : 0,
     "total_time_in_millis" : 0
 } ]
```

<1>: The `type` parameter indicates the type of restoration. The value `snapshot` indicates that the shard is being restored from a snapshot. <2>: The `source` parameter indicates the source snapshot and repository. <3>: The `percent` parameter indicates the progress of the restoration task. The value 94.5% indicates that 94.5% of shard files are restored. The response lists all indexes that are being restored and all shards in these indexes. Each shard contains statistics about the start or end time, duration, restoration progress, and transmitted bytes.

**Cancel index restoration**

To cancel index restoration, you only need to delete the indexes that are being restored. A restoration process is a shard restoration process. You can call the DELETE API operation to modify the status of a cluster and cancel index restoration. Example:

```
DELETE /restored_index_3
```

If you run the preceding command when the `restored_index_3` index is being restored, the system stops the restoration and deletes the data that has been restored to your cluster. For more information, see Snapshot And Restore.

**Use a snapshot to migrate data**

To use a snapshot to migrate data to an Elasticsearch cluster, perform the following steps:
1. Back up the snapshot to OSS.
2. Create a repository on the destination Elasticsearch cluster. The repository must use the
OSS bucket that stores the snapshot.
3. Set the `base_path` parameter to the path of the snapshot.
4. Run the snapshot restoration command on the destination Elasticsearch cluster.
These steps provide a simple solution to snapshot-based data migration. For more information, see Use a snapshot stored in OSS to migrate Elasticsearch data.

##### 7.4.4.2 Automatic backup

The snapshot feature lets you set the backup cycle and time for automatic backup. You can also manually create snapshots. This topic describes how to configure automatic backup.

**Prerequisites**

An Operations and Maintenance (O&M) engineer has created a backup repository on the O&M platform. For more information about how to create a backup repository, see the **Repository**
**Management > Add Repository** section in the *O&M Guide*.

**Procedure**

1. Log on to the Alibaba Cloud Elasticsearch console. In the navigation pane on the left, click
**Instance List**.
2. On the **Instance List** page, click the ID of the target instance.
3. In the navigation pane on the left, choose **Configuration and Management > Data**
**Backup**.
4. In the **Associated Repository** section of the **Data Backup** page, click **Change**
**Associated Repository** to the right of **Repository Name**, select a repository, and click
**OK**.
5. In the **Data Backup** area, you can turn on the **Enable Automatic Backup** switch.
6. Click **Set** on the right side of **Auto Snapshot Period**.
7. In the **Auto Snapshot Configuration** panel, specify **Frequency**.

> **Important:** The start time is based on the time zone of the current region. Avoid creating cluster snapshots during automatic data backups.

| Backup Cycle | Description |
|---|---|
| Every Minute | Backs up data every few minutes. You can customize the interval in minutes. |
| Every Hour | Backs up data every few hours. You can customize the interval in hours. |
| Daily | Backs up data every day. You can customize the specific backup time. |
| Weekly | Backs up data every few weeks. You can customize the interval in weeks. |
| Monthly | You can schedule monthly automatic backups and specify a custom interval in months. |
| Custom | Select a custom backup cycle and time. |

|   | Important Scheduled backups consume CPU, memory resources, and disk space. This can affect the performance of your Elasticsearch cluster. The query and write performance of the cluster may decrease during a scheduled backup. Set a reasonable frequency and time period, and do not specify a short backup interval. |   |
|---|---|---|

8. Click **OK**.
After you click OK, the system automatically backs up data based on the backup cycle that you set. You can view detailed backup information in the **Snapshot List**.

> **Note:** To back up data immediately, click **Back Up Immediately** in the **Snapshot List**.

The snapshot list automatically clears automatic backup records every hour. Only the latest 10 records are retained. The snapshot list does not clear manual backup records that are generated after you click **Create Snapshot**.

### 7.5 Kibana console

#### 7.5.1 Log in to the Kibana console

Apsara Stack Elasticsearch provides the Kibana console for you to scale your businesses. The Kibana console is seamlessly integrated into Elasticsearch. It lets you view the status of your Elasticsearch cluster in real time and manage the cluster. This topic describes how to log in to the Kibana console.

**Prerequisites**

The Elasticsearch cluster is in the Normal state, and Kibana nodes are enabled. You have an account that is allowed to log on to Kibana and a whitelist is configured. For more information, see Security Settings.

**Procedure**

1. Log in to the Alibaba Cloud Elasticsearch console. In the navigation pane on the left, click
**Instance List**.
2. On the **Instance List** page, click the ID of the target instance.
3. On the **Basic Information** page, in the **Kibana Information** section, click the link to the
right of **Kibana Console URL**.
4. Enter the username and password and click Log In.

> **Note:** The default username is elastic. The password is the one that you specified when you created the instance.

5. Click the
icon in the upper-left corner and choose **Management > Dev Tools** to go to the **Console** page.

#### 7.5.2 Modify the Kibana configuration

You can modify the Kibana configuration to view, install, and uninstall Kibana plug-ins uploaded to the Elasticsearch O&M console. This topic describes how to modify the Kibana configuration.

**Prerequisites**

The Elasticsearch cluster is in the Normal state. The O&M engineer has uploaded Kibana plugins to the Elasticsearch O&M console.

**Procedure**

1. Log on to the Alibaba Cloud Elasticsearch console. In the navigation pane on the left, click
**Instance List**.
2. On the **Instance List** page, click the ID of the target instance.
3. In the **Kibana Information** section of the **Basic Information** page, click **Modify**
**Configuration**.
4. On the **Plug-in Configuration** page, you can view the Kibana plug-in list.
5. Click **Install** or **Remove** in the Actions column of a plug-in.

> **Warning:** Installing or uninstalling a plug-in restarts the cluster. Confirm the operation before you proceed.

6. In the dialog box that appears, read the risk warning and click **Confirm**.
Wait for the cluster to restart. The status of the plug-in changes to Installed or Uninstalled, which indicates that the operation is successful.

### 7.6 Dashboards console

#### 7.6.1 Log on to the Dashboards console

This topic describes how to log on to the OpenSearch Dashboards console.

**Prerequisites**

The instance status is Normal, and the Dashboards node is enabled.

**Procedure**

1. Log on to the Alibaba Cloud OpenSearch console. In the navigation pane on the left, click
**Instance List**.
2. On the **Instance List** page, click the ID of the target instance.
3. On the **Basic Information** page, in the **Dashboards Information** section, click the link
next to **Dashboards Console URL**.
4. Enter your username and password and click **Log In**.

> **Note:** The default username is admin. The password is the one that you set when you created the instance.

5. Click the
icon in the upper-left corner and choose **Management > Dev Tools** to open the **Console** page.

#### 7.6.2 Modify Dashboards configuration

Modify the Dashboard configuration to view, install, or uninstall Dashboard plugins that you have uploaded to the O&M platform. This topic describes how to perform this task.

**Procedure**

1. Log on to the Alibaba Cloud Retrieval and Analysis Service console. In the navigation pane on the
left, click **Instance List**.
2. In the **Instance List**, click the target instance ID.
3. On the **Basic Information** page, in the **Dashboard Information** section, click **Modify**
**Configuration** on the right.
4. On the **Plugin Configuration** page, view the list of Dashboard plugins.
5. Click **Install** or **Uninstall** next to the target plugin.

> **Warning:** Installing or uninstalling a plugin triggers a cluster restart. Proceed with caution.

6. In the dialog box that appears, read the risk notice and click **Confirm**.
After the cluster successfully restarts, the status of an installed plugin changes to Installed and the status of an uninstalled plugin changes to Not Installed. This confirms that the plugin was successfully installed or uninstalled.

## 8 Using plugins

### 8.1 Work with Elasticsearch plug-ins

**ins**

#### 8.1.1 Use a-pack-xdcr for cross-cluster index replication

**replication**

This topic describes how to use the a-pack-xdcr plugin for Elasticsearch to replicate data from one cluster to another.

**Prerequisites**

Create a source cluster (leader) and a destination cluster (follower) of the same type. Ensure that the two clusters can communicate with each other. Enable an IP address whitelist. For more information, see Security Settings.

**Limitations**

This feature is supported only for Elasticsearch version 6.8. The a-pack-xdcr plugin is a built-in system plugin. It is installed by default when you create a cluster and cannot be uninstalled. Cross-cluster replication works only for new indexes. The index that you want to replicate must have the `"settings.index.soft_deletes.enabled": true` setting.

**Preparation**

1. Log on to the Kibana console of the source cluster (leader).
For more information, see Log on to the Kibana console.
2. In the left-side navigation pane, click **Dev Tools**.
3. In the **Console**, run the following command to create an index named `my_test_index` and
set `"settings.index.soft_deletes.enabled": true` for it.

```json
PUT /my_test_index
  "settings": {
    "index.soft_deletes.enabled": true,
    "number_of_shards": 1,
    "number_of_replicas": 1
```

`},`

```json
  "mappings": {
    "_doc": {
      "properties": {
        "message": {
          "type": "text"
```

4. Run the `GET _nodes` command to get the `<IP:Port>` information. You will need this
information in a later step. From the query result, get the value of the `transport_address` parameter. For example:

```
 10.XX.XX.106:9300 .
```

**Procedure**

1. Log on to the Kibana console of the destination cluster (follower).
For more information, see Log on to the Kibana console.
2. In the left-side navigation pane, click **Dev Tools**.
3. In the **Console**, run the following command on the destination cluster (follower) to add the
source cluster (leader) as a remote cluster.

```json
PUT _cluster/settings
  "persistent": {
    "cluster": {
      "remote": {
        "leader": {
          "seeds": [
            "<your cluster IP>:<your cluster Port>"
```

`]`

> **Note:** Replace `<your cluster IP>` and `<your cluster Port>` with the `<IP:Port>` information from Step 4 of the Preparation section.

4. Run the following command to start replicating the index.

```
PUT _xdcr/leader/my_test_index
```

> **Note:** `my_test_index` is an example index name. Replace it with the name of the index that you want to replicate from the source cluster (leader).

5. Run the following command to view the status of the synchronization task.

```
GET _cat/xdcr?v
```

If the command is successful, it returns a result similar to the following.

> **Note:** In the output, `index` is the index name, `repository` is the remote cluster, `shard` is the index shard, `localSeqNo` is the maximum sequence number on the local cluster, and `remoteSeqNo` is the maximum sequence number on the remote cluster.

6. Run the following command to view the data in the replicated index.

```
GET /my_test_index/_search
```

> **Note:** `my_test_index` is an example index name. Replace it with the name of the replicated index.

You can also run the following command to stop the index replication.

```
DELETE /_xdcr/leader/my_test_index
```

#### 8.1.2 Synchronize index data across clusters with the xdcr plugin

**with the xdcr plugin**

This topic describes how to use the xdcr plugin for Elasticsearch to synchronize index data across clusters.

**Limitations**

This topic applies to Elasticsearch version 7.10.0. The xdcr plugin is a built-in system plugin and cannot be uninstalled.

**Prerequisites**

You have a primary cluster and a standby cluster of the same type. Ensure that the two clusters can communicate with each other. The allowlist is enabled. For more information, see Security Settings.

**Procedure**

Step 1: Log on to the Kibana console Step 2: Create a repository on the standby cluster Step 3: Enable cluster synchronization on the standby cluster Step 4: Verify data synchronization in different use cases Use case 1: Verify data synchronization for a new index Use case 2: Verify incremental and full synchronization for specific indexes Use case 3: Verify the use of the excludes parameter during cluster-wide synchronization

> **Note:** Replace the variables in the commands with your actual values. The data used in this topic is for reference only.

**Step 1: Log on to the Kibana console**

1. Log on to the Kibana console for both the primary and standby clusters. For detailed
instructions, see Log on to the Kibana console.
2. In the upper-left corner, click the
icon. In the left navigation pane, choose
**Management > Dev Tools** to open the **Console**.

**Step 2: Create a repository on the standby cluster**

1. On the standby cluster, run the following command to create a remote repository that
connects to the primary cluster. This example names the repository `rep0801` . i. Create the repository.

```json
PUT /_xdcr/repository/<new_repository_name>
  "address": "<primary_cluster_ip_address>",
  "port":<primary_cluster_port_number>,
  "userName": "<primary_cluster_username>",
  "password": "<primary_cluster_password>"
```

> **Note:** To get the IP address and port number of the primary cluster, log on to its Kibana console and run the `GET _nodes` command to find the `<IP:Port>` information.
> Cluster username and password for the primary cluster: The default username is elastic. The password is the one you set when creating the cluster.

The following example shows how to create a repository named `rep0801` :
2. Run the following command to verify that the repository exists.

```
GET /_xdcr/repository/
```

The following output confirms that the repository was created.
3. (Optional) To delete an existing repository, run the following command.

```
DELETE /_xdcr/repository/<repository_name>
```

**Step 3: Enable cluster synchronization on the standby cluster**

1. On the standby cluster, run the following command to enable cluster synchronization.

```
POST /_xdcr/cluster_sync/<repository_name>
```

Or:

```
PUT /_xdcr/cluster_sync/<repository_name>
```

The following output confirms that the feature was enabled:
2. Run the following command to verify that cluster synchronization is enabled.

```
GET /_xdcr/cluster_sync
```

The following output confirms that the feature was enabled.

**Step 4: Verify data synchronization in different use cases**

**Use case 1: Verify new index synchronization**

1. . Create an index and insert data**
1. On the primary cluster, run the following command to create an index. For example, you
can create an index named `kk-index02` ( `PUT /kk-index02` ).

```
PUT /<index_name>
```

2. Insert data into the index:

```json
POST /kk-index02/_doc
  "aaa":"primary cluster data 1",
  "bbb":"primary cluster data 12"
```

3. View the created index and its data.

```
GET /_cat/indices GET /<index_name>/_search
```

The following output confirms that the index and its data were created.
2. . View the synchronized index and data**
On the standby cluster, run the following commands in sequence to view the synchronized index and its data.

```
GET /_cat/indices GET /<index_name>/_search
```

The following output confirms that the data was synchronized.
3. . (Optional) Disable cluster or index synchronization**
To disable data synchronization for a cluster or a specific index, run the corresponding command. Disable data synchronization for the cluster

```
DELETE /_xdcr/cluster_sync/<repository_name>
```

Disable data synchronization for a specific index

```
DELETE /_xdcr/cluster_sync/<repository_name>/<index_name>
```

**Use case 2: Verify incremental and full synchronization**

1. . Create indexes and insert data**
1. On the primary cluster, create two indexes (for example, kk-indexa001 and kk-indexb002)
and insert data into each index.

```json
# Create an index on the primary cluster.
PUT /kk-indexa001
# Insert data into the index.
POST /kk-indexa001/_doc
  "aaa":"primary cluster index a data 1",
  "bbb":"primary cluster index a data 12"
```

```json
# Create an index on the primary cluster.
PUT /kk-indexb002
# Insert data into the index.
POST /kk-indexb002/_doc
  "aaa":"primary cluster index b data 1",
  "bbb":"primary cluster index b data 2"
```

2. On the primary cluster, run the following commands to verify that the indexes and their
data were created.

```
GET /_cat/indices?v GET /<index_name>/_search
```

The following output indicates a successful creation.
2. . Enable synchronization and verify status**
1. On the standby cluster, enable synchronization for each specific index.

> **Important:** If cluster synchronization is enabled, you must disable it first. This feature synchronizes all indexes and will conflict with the index-specific commands that follow, causing an error.

Enable an incremental synchronization task for index A.

```
PUT /_xdcr/index_sync/<repository_name>/<index_name>
```

Enable a full synchronization task for index B.

```
PUT /_xdcr/_recovery/<repository_name>/<index_name>
```

2. On the standby cluster, run the following commands to check the status of the
synchronization tasks.

```
GET _cat/xdcr GET /_xdcr/stats GET /_cat/xdcr/concurrent_sync
```

3. . Insert more data into the indexes**
1. On the host group, execute the following command to again insert data into the indexes
named kk-indexa001 and kk-indexb002.

```json
POST /kk-indexa001/_doc
  "aaaz":"primary cluster index a data 3",
  "bbbx":"primary cluster index a data 4"
POST /kk-indexb002/_doc
  "aaaa":"primary cluster index b data 3",
  "bbbx":"primary cluster index b data 4"
```

2. On the primary cluster, run the following commands to verify that the data was inserted.

```
GET /_cat/indices?v GET /<index_name>/_search
```

4. . Verify the synchronized data**
On the standby cluster, run the following commands to check the details of the synchronized data.

```
GET /_cat/indices?v GET /<index_name>/_search
```

The result is as expected if the index configured for incremental synchronization contains one more document than the index configured for full synchronization.

|   | Note A full synchronization task is a one-time operation. In contrast, an incremental synchronization task is continuous and synchronizes new changes from the primary cluster. |   |   |   |
|---|---|---|---|---|
|   |   | full synchronization | incremental |   |
|   | synchronization |   |   |   |

**Use case 3: Verify using the excludes parameter**

1. On the primary cluster, use the following commands to create three indexes (for example,
`index-a1` , `index-b1` , and `index-c1` ) and then check the indexes.

```json
PUT /index-a1 POST /index-a1/_doc
  "aaaz":"primary cluster index a data 3",
  "bbbx":"primary cluster index a data 4"
GET /_cat/indices
```

2. On the standby cluster, run the following command to enable cluster synchronization while
excluding a specific index. This example excludes `index-b1` .

```
PUT /_xdcr/cluster_sync/<repository_name>?excludes=<index_name>
```

For example:

```
PUT /_xdcr/cluster_sync/rep0801?excludes=index-b1
```

3. Run the following command to check the cluster synchronization status.

```
GET /_xdcr/cluster_sync
```

4. Run the following commands to check the status of the synchronization tasks. Tasks are
started for all indexes except `index-b1` . View the status of synchronization tasks.

```
GET _cat/xdcr
```

View the status of synchronization tasks in JSON format.

```
GET /_xdcr/stats
```

View ongoing synchronization tasks.

```
GET /_cat/xdcr/concurrent_sync
```

#### 8.1.3 Use the opendistro_sql plug-in to query cluster data by executing SQL statements

**cluster data by executing SQL statements**

This topic describes how to use the opendistro_sql plug-in of Elasticsearch to query data in an Elasticsearch cluster by executing SQL statements.

**Prerequisites**

The opendistro_sql plug-in is installed. For more information, see Install or uninstall plugins. Whitelist-based authentication is enabled. For more information, see the Security settings section of the Configure clusters topic.

**Procedure**

> **Note:** A cluster of Elasticsearch V6.8 is used in this example. The procedure may vary depending on the Elasticsearch version. The actual console page prevails.

**Step 1: Log in to the Kibana console and go to the Console tab**

Log in to the Kibana console of the Elasticsearch cluster and go to the Console tab. For more information, see Log in to the Kibana console.

**Step 2: Create a test index and insert test data into the index**

1. Run the following command to create a test index:

```json
PUT test_user_data
  "mappings": {
    "_doc": {
      "properties": {
        "name": { "type": "text" },
        "age": { "type": "integer" },
        "city": { "type": "keyword" },
        "salary": { "type": "float" },
        "join_date": {
          "type": "date",
          "format": "yyyy-MM-dd||epoch_millis"
```

2. Run the following commands to insert three test data entries into the index:

```json
POST test_user_data/_doc/1
  "name": "Alice",
  "age": 30,
  "city": "Beijing",
  "salary": 15000.5,
  "join_date": "2022-03-15"
POST test_user_data/_doc/2
  "name": "Bob",
  "age": 28,
  "city": "Shanghai",
  "salary": 18000.0,
  "join_date": "2021-07-20"
POST test_user_data/_doc/3
  "name": "Charlie",
  "age": 35,
  "city": "Beijing",
  "salary": 22000.8,
  "join_date": "2020-11-05"
```

**Step 3: Use the opendistro_sql plug-in to query the test data**

**by executing SQL statements**

Elasticsearch supports the following SQL query syntax:

> **Note:** Replace `<your_index>` in the following code with the name of the index that you want to query.

Syntax for an SQL query in a GET request

```
GET _opendistro/_sql?sql=select * from <your_index> limit 50
```

Sample command:

```
GET _opendistro/_sql?sql=SELECT name, age, city FROM test_user_data LIMIT 2
```

Expected return result:

```json
  "took" : 16,
  "timed_out" : false,
  "_shards" : {
    "total" : 5,
    "successful" : 5,
    "skipped" : 0,
    "failed" : 0
```

`},`

```json
  "hits" : {
    "total" : 3,
    "max_score" : 1.0,
    "hits" : [
        "_index" : "test_user_data",
        "_type" : "_doc",
        "_id" : "2",
        "_score" : 1.0,
        "_source" : {
          "city" : "Shanghai",
          "name" : "Bob",
          "age" : 28
```

`},`

```json
        "_index" : "test_user_data",
        "_type" : "_doc",
        "_id" : "1",
        "_score" : 1.0,
        "_source" : {
          "city" : "Beijing",
          "name" : "Alice",
          "age" : 30
```

`]` Syntax for an SQL query in a POST request

```json
POST _opendistro/_sql
 "query": "SELECT * FROM <your_index> LIMIT 50"
```

Sample command:

```json
POST _opendistro/_sql
  "query": "SELECT name, salary FROM test_user_data WHERE age > 29 ORDER BY salary DE
SC"
```

Expected return result:

```json
  "took" : 14,
  "timed_out" : false,
  "_shards" : {
    "total" : 5,
    "successful" : 5,
    "skipped" : 0,
    "failed" : 0
```

`},`

```json
  "hits" : {
    "total" : 2,
    "max_score" : null,
    "hits" : [
        "_index" : "test_user_data",
        "_type" : "_doc",
        "_id" : "3",
        "_score" : null,
        "_source" : {
          "name" : "Charlie",
          "salary" : 22000.8
```

`},`

```json
        "sort" : [
          22000.8
```

`]` `},`

```json
        "_index" : "test_user_data",
        "_type" : "_doc",
        "_id" : "1",
        "_score" : null,
        "_source" : {
          "name" : "Alice",
          "salary" : 15000.5
```

`},`

```json
        "sort" : [
          15000.5
```

`]` `]` Syntax for an SQL query with the CSV format specified for the data to return

```json
POST _opendistro/_sql?format=csv
 "query": "SELECT * FROM <your_index> LIMIT 50"
```

Sample command:

```json
POST _opendistro/_sql?format=csv
  "query": "SELECT name, age, city FROM test_user_data"
```

Expected return result:

```
city,name,age Shanghai,Bob,28 Beijing,Alice,30 Beijing,Charlie,35
```

> **Note:** For more information about SQL syntax, see SQL.

If you want to execute Java code by using SQL statements, download the Java Database Connectivity (JDBC) driver from https://github.com/opendistro-forelasticsearch/sql-jdbc.

#### 8.1.4 Use the vector search plugin (aliyun-knn)

**knn)**

The vector search plugin, developed by the Alibaba Cloud Elasticsearch team, is built on the Proxima vector search library from Alibaba DAMO Academy. It enables you to quickly implement vector search for use cases like image search, video fingerprint sampling, facial recognition, speech recognition, and product recommendation. This topic describes how to use the vector search plugin.

**Background information**

Use cases The Alibaba Cloud Elasticsearch vector search engine is battle-tested in large-scale production applications, including Pailitao (search by image), Alibaba Cloud Image Search, Qutoutiao video fingerprint sampling, personalized recommendations, personalized search, and CrossMedia search. How it works The vector search feature in Alibaba Cloud Elasticsearch is implemented as a plugin to ensure full compatibility with native Elasticsearch versions. You can use the vector search engine with no additional learning curve. In addition to supporting real-time incremental writes and near real-time (NRT) search queries, the vector index inherits all of Elasticsearch's native distributed capabilities, such as multi-replica support and fault recovery.

> **Note:** The Alibaba Cloud Elasticsearch vector search plugin does not support data migration using methods like an OSS snapshot or DataWorks. We recommend that you use Logstash.

Algorithm description The vector search engine currently supports the hnsw algorithm and the linear algorithm. These algorithms are suitable for scenarios with small, fully in-memory, single-node datasets. The following table compares the performance of the two algorithms. Table 1. Performance comparison between the hnsw and linear algorithms The data in this table was measured in an Alibaba Cloud Elasticsearch V6.8.13 environment. The test environment was configured as follows: Machine specifications: Two data nodes, each with 16 vCPUs, 64 GB of memory, and a 100 GB SSD cloud disk. Dataset: SIFT 128-dimensional float vectors. Total data volume: 20 million entries. The index used default parameters.

| Performance metric | hnsw | linear |
|---|---|---|
| Top-10 recall rate | 98.6% | 100% |
| Top-50 recall rate | 97.9% | 100% |
| Top-100 recall rate | 97.4% | 100% |
| Latency (p99) | 0.093s | 0.934s |
| Latency (p90) | 0.018s | 0.305s |

> **Note:** In the table, `p` stands for percentile. For example, Latency (p99) indicates that 99% of queries are completed within the specified time.

**Limitations**

This feature is available only for Alibaba Cloud Elasticsearch V6.8.13 and later. ARM-based instances are not supported.

**Prerequisites**

The vector search plugin (aliyun-knn) is installed on your instance. Before you install the vector search plugin, ensure that your Elasticsearch instance uses data nodes with at least 2 vCPUs and 8 GiB of memory. The 2 vCPUs and 8 GiB specification is for functional testing only. For production environments, data nodes must have at least 4 vCPUs and 16 GiB of memory. If your nodes do not meet this requirement, upgrade your data node specifications first. You have planned your index and cluster. You have configured an IP whitelist. For more information, see Security settings.

**Create a vector index**

1. Log on to the Kibana console of your Alibaba Cloud Elasticsearch instance.
For more information, see Log on to the Kibana console.
2. In the left-side navigation pane, click **Dev Tools**.
3. In the **Console**, run the following command to create a vector index.

```json
PUT test
  "settings": {
    "index.codec": "proxima",
    "index.vector.algorithm": "hnsw"
```

`},`

```json
  "mappings": {
    "properties": {
      "feature": {
        "type": "proxima_vector",
        "dim": 2,
        "vector_type": "float",
        "distance_method": "SquaredEuclidean"
```

| Type | Parameter | Default | Description |
|---|---|---|---|
| setting | index.codec | proxima | Specifies whether to build an underlying proxima k-NN index. Valid values: proxima (Recommended): Builds an underlying proxima k-NN index that supports vector search. null: Does not build an underlying proxima k-NN index when the index is created. An inverted index is built instead. In this case, proxima vector fields support _ only script-based search, not hnsw or linear search. |
|   | index.vecto r.algorithm | hnsw | The vector search algorithm. Valid values: hnsw: The hnsw algorithm. linear: The linear algorithm. |
|   | index.vecto r.general.bu ilder.offline mode _ | false | Specifies whether to use the offline optimization mode to build the k-NN index. Valid values: false: Does not use the offline optimization mode. true: Uses the offline optimization mode. This significantly reduces segment fragmentation during index building and improves overall write throughput. |

| mapping | type | proxima vect _ or | The type of the vector field. For example, setting the feature field type to proxima vector makes feature a _ vector field. |   |   |
|---|---|---|---|---|---|
|   | dim | 2 | The vector dimension. This parameter is required. The value must be an integer from 1 to 2048. |   |   |
|   | vector type _ | float | The data type of the vector. Valid values: float short binary For array types other than binary , the array length must be the same as dim. For the binary type, vector data must be converted to an array of unsigned 32-bit integers (uint32), and dim must be an integer multiple of 32. For example, if the business data is the 64-bit binary value 10001001001001011110000010011111010000 11010010011010011010000100, then it is written to the vector as [-1994006369, 1128900228] . |   |   |
|   |   |   |   | [-1994006369, |   |
|   | distance me _ thod | SquaredEucli dean (without square root) | The distance metric. Valid values: SquaredEuclidean: Euclidean distance (without square root). InnerProduct: Inner product distance. Hamming: Hamming distance (for the BINARY type only). For more information about distance metrics, see Distance metrics. |   |   |

|   |   | vector |
|---|---|---|
|   | 1128900228] |   |

k-NN vector search also provides advanced query parameters. For more information, see Advanced parameters.
4. Run the following command to add a document.

```json
POST test/_doc
  "feature": [1.0, 2.0]
```

**Vector query**

Standard search Run the following command to perform a standard search on your documents.

```json
GET test/_search
  "query": {
    "hnsw": {
      "feature": {
        "vector": [1.5, 2.5],
        "size": 10
```

Common parameters:

| Parameter | Description |
|---|---|
| hnsw | The vector query algorithm. This must be consistent with the algorithm specified when the index was created. |
| vector | The array length of the vector data to be queried must be consistent with the dim specified in the mapping when the index is created. |

| size | Specifies the number of documents to return. Note The size parameter in vector search is different from the native Elasticsearch size parameter. The former controls the number of documents retrieved by the knn vector search plugin, while the latter controls the number of documents retrieved for the entire query. When you run a query, the system first uses the vector search size parameter to retrieve the top-N documents. Then, the native Elasticsearch size parameter is used to retrieve the documents for the entire query and return the final result. We recommend that you keep the value of thes ize parameter for vector search the same as the value of the Elasticsearch size parameter (default: 10). |
|---|---|

k-NN vector search also provides advanced query parameters. For more information, see Advanced parameters. Warm up an index (to reduce latency) Because a k-NN index requires full in-memory search, query latency can be high during a cold start. The k-NN plugin provides an index warmup feature to preload the k-NN index into local memory before it serves search requests. This significantly reduces query latency during cold starts. Warm up all vector indexes.

```
POST _vector/warmup
```

Warm up a specific vector index.

```
POST _vector/{indexName}/warmup
```

> **Important:** If your cluster has many large vector indexes but you only need vector search on specific ones, warm up only those indexes to improve in-memory search performance.

**Vector scoring**

Vector search uses a unified scoring formula that depends on the distance metric. The choice of distance metric directly affects search ranking. Scoring formula: Score = 1 / (distance + 1)

> **Note:** By default, the vector scoring mechanism uses squared Euclidean distance.
> In practice, you can calculate the distance from the score to optimize your vectors and improve scoring accuracy.

**Distance metrics**

Different distance metrics correspond to different scoring mechanisms. The following table describes the metrics supported by the aliyun-knn plugin.

| Distance metric | Definition | Scoring formula | Use cases | Example |
|---|---|---|---|---|
| SquaredEuclidea n (Euclidean distance without square root) | Euclidean distance is a common metric that measures the straight-line distance between two points in a multi- dimensional space. | For two n- dimensional vectors A = [A1, A2,…, An] and B = [B1, B2,…, Bn]: Squared Euclidean distance = (A1-B1)² + (A2-B2)² + ... + (An-Bn)² Score = 1 / (distance + 1) Note Vector scoring uses squared Euclidean distance by default. | Euclidean distance reflects the absolute difference in the numerical values of individual features. It is often used in analyses where the magnitude of dimensional values is important, such as analyzing the similarity or difference in user value based on user behavior metrics. | For two 2D vectors [0,0] and [1,2], the squared Euclidean distance is (1-0)² + (2-0)² = 5. |

| InnerProduct (inner product distance) | The inner product, also known as the dot product, is an operation that takes two vectors and returns a single scalar value. | For two n- dimensional vectors A = [A1, A2,…, An] and B = [B1, B2,…, Bn]: Inner product distance = A1*B1 + A2*B2 + ... + An*Bn Score = 1 / (distance + 1) where distance is the inner product distance. | The inner product distance considers both the angle between two vectors and their absolute lengths. When vectors are normalized, the inner product is equivalent to cosine similarity. | For two 2D vectors [1,1] and [1,5], the inner product distance is 1*1 + 1*5 = 6. |
|---|---|---|---|---|
| Hamming (Hamming distance, for binary type only) | In information theory, the Hamming distance between two strings of equal length is the number of positions at which the corresponding symbols differ. | For two n-bit binary codes x and y: d(x,y) = Σ(x[i] ⊕ y[i]) for i=0 to n-1, where ⊕ is the XOR operation. Score = 1 / (distance + 1) | A typical use case is error correction and detection in data transmission, where it counts the differing bits to estimate the error rate. | The Hamming distance between 1011101 and 1001001 is 2. Important When using the aliyun- knn plugin, binary vector data must be converted into an array of unsigned 32-bit integers (uint32), and the dim must be a multiple of 32. |

> **Note:** You can specify the distance metric using the `distance_method` parameter in the index's **mapping**.

**Circuit breaker parameters**

| Parameter | Description | Default |
|---|---|---|

| indices.breaker.vect or.native.indexing.li mit | If off-heap memory usage exceeds this value, write operations are rejected. Writes can resume after background build tasks complete and release memory. A circuit breaker error indicates high system memory consumption. We recommend that you reduce the write traffic. | 70% |
|---|---|---|
| indices.breaker.vect or.native.total.limit | The maximum percentage of off-heap memory that can be used for background vector index builds. If actual off-heap memory usage exceeds this percentage, shards may restart. | 80% |

> **Important:** Vector circuit breaker parameters are cluster-level settings. You can view them by running the **GET _cluster/settings** command. We recommend that you do not adjust these values.

**Advanced parameters**

Table 2. Build parameters (hnsw)

| Parameter | Description | Default |
|---|---|---|
| index.vector.hnsw.b uilder.max scan nu _ _ m | Controls the neighbor search range during graph construction to guarantee worst-case performance. | 100000 |
| index.vector.hnsw.b uilder.neighbor cnt _ | The number of neighbors for each node in the level 0 graph of HNSW. We recommend that you set this value to 100. A larger value increases offline index storage consumption but improves the quality of the graph construction. | 100 |
| index.vector.hnsw.b uilder.upper neighb _ or cnt _ | The maximum number of neighbors for each node in the upper layers of the HNSW graph (excluding layer 0). This value is typically set to half of neighbor cnt and cannot exceed 255. _ | 50 |
| index.vector.hnsw.b uilder.efconstructio n | Controls the size of the neighbor scan area during graph construction. A larger value improves the quality of the offline graph construction but slows down index building. We recommend an initial value of 400. | 400 |

| index.vector.hnsw.b uilder.max level _ | The total number of HNSW layers, including the base layer (layer 0) and the upper layers. For example, with a total of 10 million documents and a scaling factor of 30, the number of layers is _ calculated by taking the logarithm of 10 million with a base of 30 and rounding the result up to the nearest integer, which is 5. This parameter has little impact on performance. We recommend an initial value of 6. | 6 |
|---|---|---|
| index.vector.hnsw.b uilder.scaling factor _ | This parameter specifies the factor for the exponential decrease in data size from one layer to the next. It is typically set to a value between 10 and 100. The larger the scaling factor, the _ fewer layers are generated. The recommended initial value is 50. | 50 |

> **Note:** The preceding parameters must be configured in the index **setting** and are applicable only to the **hnsw** algorithm.

Table 3. Query parameters (hnsw)

| Parameter | Description | Default |
|---|---|---|
| ef | Controls the size of the subgraph search range during online retrieval. A larger value improves the recall rate but degrades performance. We recommend a value between 100 and 1,000. | 100 |

The following is a query example.

```json
GET test/_search
  "query": {
    "hnsw": {
      "feature": {
        "vector": [1.5, 2.5],
        "size": 10,
        "ef": 100
```

**FAQ**

Q: How do I evaluate the query recall rate? A: You can create two indexes with identical configurations, one using the hnsw algorithm and the other using the linear algorithm. Write the same vector data to both indexes. After the data is refreshed, use the same query vector to compare the document IDs returned by the linear index and the hnsw index. The recall rate is the number of common document IDs in both result sets divided by the number of results requested.

> **Note:** The number of common document IDs is the count of IDs present in both result sets.

Q: What do I do if a `circuitBreakingException` error occurs during cluster writes? A: This error indicates that the off-heap memory usage has exceeded the limit specified by
**indices.breaker.vector.native.indexing.limit** (default is 70%), which triggers the write
circuit breaker. Write operations typically resume automatically after the background index build tasks are complete and memory is released. We recommend that you implement a retry mechanism in your client-side write logic. Q: Why is the CPU still active after write tasks have stopped? A: Vector index building occurs during a refresh or flush operation. Even if the write traffic has stopped, background tasks for building the vector index may still be running. The computing resources are freed after the final refresh cycle completes. Q: What do I do if vector search with the aliyun-knn plugin is slow or a memory circuit breaker is triggered? A: The aliyun-knn plugin performs searches on in-memory vectors, making it memoryintensive. Large indexes can cause slow performance or trigger the memory circuit breaker. As a best practice, ensure the index size does not exceed 50% of the data node's memory. If you cannot reduce the data volume and memory is insufficient, upgrade your cluster specifications.

#### 8.1.5 Manage index lifecycles with the ISM plugin

**plugin**

This topic describes how to use the ISM plugin in Elasticsearch to manage index lifecycles. This feature is supported only in Alibaba Cloud Elasticsearch instances that run Elasticsearch 6.8.13_ali1.3.0 or 7.10.0_ali1.6.0.

**Prerequisites**

The opendistro-job-scheduler and opendistro-index-management plugins are manually installed. For more information, see Plugin configuration. Before you use the Kibana console, you must configure a Kibana whitelist in the security settings on the instance details page. For more information, see Security settings.

**Limitations**

Your Alibaba Cloud Elasticsearch cluster must run Elasticsearch 6.8.13_ali1.3.0 or 7.10.0_ali1.6.0.

**Procedure**

1. Log on to the Kibana console of your Alibaba Cloud Elasticsearch instance.
For more information about how to log on to the Kibana console, see Log on to the Kibana console.

> **Note:** The steps and examples in this topic use an Alibaba Cloud Elasticsearch 7.10.0_ali1.6.0 instance. The UI may differ for other versions.

2. In the left-side navigation pane, click the
icon, then choose **Management > Dev**
**tools**.
3. On the **Console** tab, run the following command to create an ISM policy.

> **Note:** The examples in this topic are based on version 7.10.0_ali1.6.0.

```json
PUT _opendistro/_ism/policies/policy_1
  "policy": {
    "description": "test",
    "default_state": "ingest",
    "states": [
        "name": "ingest",
        "actions": [
            "rollover": {
              "min_doc_count": 5
```

`],`

```json
        "transitions": [
            "state_name": "search"
```

`]` `},`

```json
        "name": "search",
        "actions": [],
        "transitions": [
            "state_name": "delete",
            "conditions": {
              "min_index_age": "5m"
```

`]` `},`

```json
        "name": "delete",
        "actions": [
            "delete": {}
```

`],`

```json
        "transitions": []
```

`],`

```json
    "ism_template": {
      "index_patterns": [
        "test-*"
```

`],`

```json
      "priority": 0
```

| Parameter | Description |
|---|---|
| default state _ | The initial state of an index. |
| states | A list of states for the policy. |
| actions | The actions to perform in a state. For a list of all available actions, see Actions. |
| transitions.conditions | The conditions that must be met to transition to the next state and run the next action. For a list of all available conditions, see Conditions. |
| ism template _ | ISM automatically applies the policy to any new index that matches the specified index patterns. |

4. View the created policy.

```
GET _opendistro/_ism/policies/policy_1
```

The following example shows a successful response.

```json
  "_id" : "policy_1",
  "_version" : 1,
  "_seq_no" : 0,
  "_primary_term" : 1,
  "policy" : {
    "policy_id" : "policy_1",
    "description" : "test",
    "last_updated_time" : 1676530893161,
    "schema_version" : 1,
    "error_notification" : null,
    "default_state" : "ingest",
    "states" : [
        "name" : "ingest",
        "actions" : [
            "rollover" : {
              "min_doc_count" : 5
```

`],`

```json
        "transitions" : [
            "state_name" : "search"
```

`]` `},`

```json
        "name" : "search",
        "actions" : [ ],
        "transitions" : [
            "state_name" : "delete",
            "conditions" : {
              "min_index_age" : "5m"
```

`]` `},`

```json
        "name" : "delete",
        "actions" : [
            "delete" : { }
```

`],`

```json
        "transitions" : [ ]
```

`],`

```json
    "ism_template" : [
        "index_patterns" : [
          "test-*"
```

`],`

```json
        "priority" : 0,
        "last_updated_time" : 1676530893161
```

`]`
5. Set the rollover_alias.

```json
PUT _index_template/ism_rollover
  "index_patterns": [
    "test-*"
```

`],`

```json
  "template": {
    "settings": {
      "opendistro.index_state_management.rollover_alias": "test"
```

The following example shows a successful response.

```json
   "acknowledged" : true
```

6. Create an index and an index alias.

```json
PUT test-000001
  "aliases": {
    "test": {
      "is_write_index": true
```

The following example shows a successful response.

```json
   "acknowledged" : true,
   "shards_acknowledged" : true,
   "index" : "test-000001"
```

7. Verify that ISM has automatically attached the policy.

```
GET _opendistro/_ism/explain/test-000001
```

The following example shows a successful response.

```json
  "test-000001" : {
    "index.opendistro.index_state_management.policy_id" : "policy_1",
    "index" : "test-000001",
    "index_uuid" : "CE4KQZASTmGKyPP5cM****",
    "policy_id" : "policy_1"
```

8. Verify the result.
To verify that the policy takes effect, write five documents to the index to trigger a state transition.

```json
POST test/_doc
  "message": "dummy"
```

> **Note:** After you attach a policy to an index, the ISM plugin creates a job that runs every 5 minutes by default. This job executes policy actions, checks conditions, and transitions the index between states.
> You can also run the `GET _opendistro/_ism/explain/test-000001` command to check the current state of the ISM policy.

#### 8.1.6 Use the opendistro_security plug-in to control permissions

**control permissions**

This topic describes how to use the opendistro_security plug-in of Elasticsearch to verify identities with Active Directory or Lightweight Directory Access Protocol (LDAP) in order to enforce fine-grained role-based access control (RBAC) on indexes, documents, and fields.

**Prerequisites**

The opendistro_security plug-in is installed. For more information, see Plug-in configuration. Whitelist-based authentication is enabled before you use Kibana. For more information, see the Security settings section of the Configure clusters topic. Sample index data is prepared. Indexes are created, and data is written to the indexes. In this topic, indexes test_security1 and test_security2 are created. Create index test_security1

```json
PUT test_security1/_doc/_bulk?refresh {"index":{"_id":"1"}} {"city":"hz","name":"sss","readable_by":"read_test_security1"} {"index":{"_id":"2"}} {"city":"hz","name":"zzz","readable_by":"read_test_security1"} {"index":{"_id":"3"}} {"city":"jd","name":"aaa"} {"index":{"_id":"4"}} {"city":"jd","name":"ccc"} {"index":{"_id":"5"}} {"city":"wz","name":"bbb"}
```

Create index test_security2

```json
PUT test_security2/_doc/_bulk?refresh {"index":{"_id":"1"}} {"city":"hz","name":"sss","readable_by":"read_test_security1"} {"index":{"_id":"2"}} {"city":"hz","name":"zzz","readable_by":"read_test_security1"} {"index":{"_id":"3"}} {"city":"jd","name":"aaa"} {"index":{"_id":"4"}} {"city":"jd","name":"ccc"} {"index":{"_id":"5"}} {"city":"wz","name":"bbb"}
```

**Limits**

Only Elasticsearch V6.8.13 and V7.10.0 support this feature.

**Configure RBAC**

1. Log in to the Kibana console of the Elasticsearch cluster and go to the homepage of the
Kibana console as prompted. For information about how to log in to the Kibana console, see Log in to the Kibana console.

> **Note:** In this example, a cluster of Elasticsearch V7.10 is used. The procedure may vary depending on the Elasticsearch version. The actual console page prevails.

2. Create a user.
i. In the left-side navigation pane, click the icon, and choose **Open Distro for**
**Elasticsearch > Security**.
ii. In the left-side navigation pane of the **Security** page, click **Internal users**. iii. On the **Internal users** page, click **Create internal user**. iv. On the **Create internal user** page, specify the user information. v. Click **Create**. You can also create a user by calling an API operation. For more information, see Create user. Sample code:

```json
PUT _opendistro/_security/api/internalusers/read_test_security1
   "password":"yourPassword"
```

3. Create a role.
i. In the left-side navigation pane, click the icon, and choose **Open Distro for**
**Elasticsearch > Security**.
ii. In the left-side navigation pane of the **Security** page, click **Roles**. iii. On the **Roles** page, click **Create role**. iv. On the **Create Role** page, specify the role information. The following example shows how to configure read-only permissions on the index named index_security1. v. Click **Create**. You can also create a role by calling an API operation. For more information, see Create role. Sample code:

```json
PUT _opendistro/_security/api/roles/read_test_security1
  "index_permissions":[{
    "index_patterns":[
        "test_security1"
```

`],`

```json
    "allowed_actions":[
        "read"
```

`]` `}]`
4. Associate the role with the user.
i. After the role is created, go to the role modification page and click the **Mapped users** tab. ii. Click **Map users**.

> **Note:** If no user is available, click **Create internal user** to create a user.

iii. On the **Map user** page, choose **Users** (the user to associate). iv. Click **Map**. You can also associate a role with a user by calling an API operation. For more information, see Create role mapping. Sample code:

```json
PUT _opendistro/_security/api/rolesmapping/read_test_security1
   "users":["read_test_security1"]
```

5. Verify the permissions of the user.
Use the created username and password to log in to the Kibana console and run the following command to verify the permissions of the user: The user does not have write permissions on index test_security1. For example, when you write data to index test_security1, "no permissions error" is returned.

```json
PUT test_security1/_doc/3
  "city":"jd",
  "name":"zz"
```

Expected result: The user does not have permissions on index test_security2. For example, when you query data in index test_security2, "no permissions error" is returned.

```json
GET test_security2/_search
  "query":{
      "match_all":{}
```

Expected result: The user has read permissions on index test_security1. The user has permissions to query data in the index. For example, when you query data in index test_security1, the corresponding data is returned.

```json
GET test_security1/_search
  "query":{
      "match_all":{}
```

Expected result:

**Configure attribute-based access control (ABAC)**

1. Log in to the Kibana console of the Elasticsearch cluster and go to the homepage of the
Kibana console as prompted. For information about how to log in to the Kibana console, see Log in to the Kibana console.

> **Note:** In this example, a cluster of Elasticsearch V7.10 is used. The procedure may vary depending on the Elasticsearch version. The actual console page prevails.

2. Create a user. For more information, see Create a user.
When you create a user, you need to add user attributes by configuring **Attributes**. You can also create a user by calling an API operation and configure **Attributes**. For more information, see Create user. Sample code:

```json
PUT _opendistro/_security/api/internalusers/read_test_security1
  "password":"yourPassword",
  "attributes":{
      "alias":"read_test_security1"
```

3. Create a role. For more information, see Create a role.
When you create a role, you need to configure **Document level security** to specify the user attributes that can be accessed. Sample configuration:

```json
  "term": {
       "readable_by":"${attr.internal.alias}"
```

You can also call an API operation to create a role and configure document-level security. For more information, see Document-level security. Sample code:

```json
PUT _opendistro/_security/api/roles/read_test_security_doc
  "index_permissions":[{
    "index_patterns":[
        "test_security*"
```

`],`

```json
    "dls":"{\"bool\":{\"must\":{\"match\":{\"readable_by\":
    \"${attr.internal.alias}\"}}}}",
    "allowed_actions":[
        "read"
```

`]` `}]`
4. Associate the role with the user. For more information, see Associate the role with the user.
5. Verify the permissions of the user.
Use the created username and password to log in to the Kibana console and run the following command to view all data stored in the index.

```json
GET test_security1/_search
  "query":{
      "match_all":{}
```

Expected result (only attributes that the role is allowed to access are queried):

**Configure document-level access control**

For more information about document-level access control, see Attribute-based security.
1. Log in to the Kibana console of the Elasticsearch cluster and go to the homepage of the
Kibana console as prompted. For information about how to log in to the Kibana console, see Log in to the Kibana console.

> **Note:** In this example, a cluster of Elasticsearch V7.10 is used. The procedure may vary depending on the Elasticsearch version. The actual console page prevails.

2. Create a user. For more information, see Create a user.
3. Create a role. For more information, see Create a role.
When you create a role, you need to configure **Document level security** to specify the documents that can be accessed. Sample configuration: The user can access only documents whose **city** is **hz** in index test_security*.

```json
  "bool": {
    "must": {
      "match": {
        "city": "hz"
```

You can also call an API operation to create a role and configure Document level security. For more information, see Document-level security. Sample code:

```json
PUT _opendistro/_security/api/roles/read_test_security_doc
  "index_permissions":[{
    "index_patterns":[
        "test_security*"
```

`],`

```json
    "dls":"{\"bool\":{\"must\":{\"match\":{\"city\":\"hz\"}}}}",
    "allowed_actions":[
        "read"
```

`]` `}]`
4. Associate the role with the user. For more information, see Associate the role with the user.
5. Verify the permissions of the user.
Use the created username and password to log in to the Kibana console and run the following command to view all data stored in the index.

```json
GET test_security1/_search
  "query":{
      "match_all":{}
```

Expected result (only documents that the role is allowed to access are queried):

#### 8.1.7 Compress index files with the aliyun-codec plugin

**codec plugin**

The `aliyun-codec` plugin is a proprietary index compression plugin from Alibaba Cloud. It compresses underlying index files in Elasticsearch (ES) and supports the `source_reuse_doc_values` feature. This topic describes how to use the `aliyun-codec` plugin.

**Prerequisites**

You have created an Alibaba Cloud Elasticsearch instance of version 7.10.0. Upgrade the instance's kernel version as needed: If you only need to compress index files, upgrade the kernel version to `1.5.0` or later. If you need to compress index files and use the `source_reuse_doc_values` feature, upgrade the kernel version to `1.6.0` or later. You have installed the `aliyun-codec` plugin. You have configured a whitelist. For more information, see Security Settings.

**Limitations**

Only Alibaba Cloud Elasticsearch instances that run version `7.10.0` with a kernel version of `1.5.0` or later support the index compression feature of the `aliyun-codec` plugin. Only Alibaba Cloud Elasticsearch instances that run version `7.10.0` with a kernel version of `1.6.0` or later support the `source_reuse_doc_values` feature.

**Use index compression**

1. Log on to the Kibana console.
2. In the upper-left corner, click the
icon and choose **Management > Dev Tools**.
3. On the **Console** tab, create an index and enable index compression.
The following example creates an index named `index1` and uses the `zstd` algorithm to compress the source, doc_values, and postings files.

> **Note:** To disable compression for a specific file type, set the corresponding parameter to
> `""` . For example, `"index.postings.compression": ""` disables compression for postings files.

```json
PUT /index1
  "settings": {
    "number_of_shards": 2,
    "number_of_replicas": 1,
    "index.codec" : "ali",
    "index.source.compression":"zstd",
    "index.doc_value.compression.default":"zstd",
    "index.postings.compression":"zstd"
```

`},`

```json
  "mappings": {
    "_source": {
      "enabled": true
```

`},`

```json
    "properties": {
      "name": {
        "type": "keyword",
        "doc_values": true,
        "index": true
```

`},`

```json
      "age": {
        "type": "integer",
        "doc_values": true,
        "index": true
```

`},`

```json
      "address": {
        "type": "text",
        "doc_values": false,
        "index": true
```

The following table describes the parameters related to index compression.

| Parameter | Description |
|---|---|
| index.codec | Specifies the compression codec for data storage. Set to ali to use Alibaba Cloud's custom codec for optimized compression. |

| index.source.compr ession | Specifies the compression algorithm for source files. Valid values: zstd: Uses the zstd compression algorithm with a compression block size of 128 KB . zstd 1024: Uses the zstd compression algorithm with a _ compression block size of 1024 KB . zstd dict: Uses the zstd compression algorithm with the dict _ feature. This provides a higher compression ratio than zstd , which slightly reduces read and write performance. best compression: Uses the native ES source compression _ algorithm. default: Uses the native ES source compression algorithm. |
|---|---|
| index.doc value.co _ mpression.default | Specifies the compression algorithm for doc values files. Valid values: _ zstd: Uses the zstd compression algorithm, which offers a high compression ratio. lz4: Uses the lz4 compression algorithm, which provides faster compression. Note Currently, this plugin only compresses doc values for fields of _ type number , date , keyword , and ip . |
| index.postings.com pression | Specifies the compression algorithm for postings files. |

|   | dict |
|---|---|
| zstd |   |

```
Use source_reuse_doc_values
```

**Enable  source_reuse_doc_values**

The following example creates an index named `index2` and enables the `source_reuse_doc_values` feature.

> **Important:** The `source_reuse_doc_values` feature can be enabled only when you create an index. Once enabled, it cannot be disabled.

```json
PUT index2
  "settings": {
    "index": {
      "ali_codec_service": {
        "source_reuse_doc_values": {
          "enabled": true
```

**Adjust  source_reuse_doc_values  configuration**

> **Note:** Native ES stores multiple copies of data in its underlying structures, such as `_source` ,

|   | source reuse doc values _ _ _ |
|---|---|
| source _ |   |

After you enable the `source_reuse_doc_values` feature, you can adjust the following settings: Adjust the maximum number of fields with the `source_reuse_doc_values` feature enabled. If the number of fields with the `source_reuse_doc_values` feature enabled exceeds the value that you set, ES throws an exception or automatically disables the `source_reuse_doc_values` feature. The maximum number of fields is `50` by default. The following example sets the maximum number of fields to `100` .

```json
PUT _cluster/settings
  "persistent": {
       "apack.ali_codec_service.source_reuse_doc_values.max_fields": 100
```

Specify whether to enforce the maximum field limit for the `source_reuse_doc_values` feature.

```json
PUT _cluster/settings
  "persistent": {
       "apack.ali_codec_service.source_reuse_doc_values.strict_max_fields": true
```

`true` : ES throws an exception when the limit is exceeded. `false` : ES automatically disables the `source_reuse_doc_values` feature when the limit is exceeded. Adjust the concurrency for reading values from fields that have the `source_reuse_doc_values` feature enabled during queries.

| source reuse doc values _ _ _ |   | feature c |
|---|---|---|
| ds where |   |   |

To reduce latency, you can adjust the concurrency for retrieving the values of these fields. The default concurrency is `5` . The following code shows an example of how to adjust the concurrency to `2` .

```json
PUT index2/_settings
  "index": {
    "ali_codec_service": {
      "source_reuse_doc_values": {
        "fetch_slice": 2
```

Adjust the thread pool and queue size for reading values from fields that have the `source_reuse_doc_values` feature enabled. The default thread pool size is the number of CPU cores on the node, and the default queue size is `1000` . This setting can only be adjusted by modifying the YML file. To adjust these settings, add the following configuration to the YML file:

```
apack.doc_values_fetch:
    size: 8
    queue_size: 1000
```

#### 8.1.8 Bulk aggregation with the faster-bulk plugin

**plugin**

The Alibaba Cloud Elasticsearch (ES) team developed the proprietary faster-bulk plugin to improve write throughput and reduce write rejections. The plugin aggregates bulk write requests based on a specified request size and time interval. This approach prevents small bulk write requests from blocking the write queue and significantly increases write throughput.

**Prerequisites**

You have created an Alibaba Cloud Elasticsearch version 7.10.0 instance. You have installed the faster-bulk plugin. After installation, the bulk aggregation feature is disabled by default, and you must enable it before use. You have configured an allowlist. For more information, see Security settings.

**Enable bulk aggregation**

1. Log on to the Kibana console.
2. In the upper-left corner, click the
icon and choose **Management > Dev Tools**.
3. In the **Console**, run the following command to enable bulk aggregation.

```json
PUT _cluster/settings
   "transient" : {
      "apack.fasterbulk.combine.enabled":"true"
```

**Bulk aggregation size and time interval**

Run the following command to specify the aggregation size and time interval for bulk write requests. The plugin writes data when, on a single data node, the cumulative size of bulk write requests or the aggregation time interval reaches the specified threshold.

```json
PUT _cluster/settings
   "transient" : {
      "apack.fasterbulk.combine.flush_threshold_size":"1mb",
      "apack.fasterbulk.combine.interval":"50"
```

**apack.fasterbulk.combine.flush_threshold_size**: The maximum size of aggregated
bulk requests. The default value is **1mb**.
**apack.fasterbulk.combine.interval**: The maximum time interval for aggregating bulk
requests, in `ms` . The default value is **50**.

> **Note:** For high-concurrency workloads, consider increasing the aggregation size or time interval based on your cluster's capacity to reduce write queue congestion.

**Enable direct routing**

When `routing` and the primary key ( `_id` ) are not specified for bulk document writes, you can enable direct routing for the cluster or a specified index to improve write speed.

> **Note:** If a cluster or index has direct routing enabled, and you also specify `routing` and a primary key ( `_id` ) in the write operation, direct routing will not take effect and will not affect normal business write operations.

Enable direct routing for the cluster.

```json
PUT _cluster/settings
  "persistent" : {
    "index.direct_routing.global.enable" : "true"
```

Create an index and enable direct routing.

> **Note:** Replace `<index>` with your index name.

```json
PUT /<index>
  "settings": {
  "index.direct_routing.enable" : "true"
```

**Disable bulk aggregation**

Run the following command to disable bulk aggregation.

```json
PUT _cluster/settings
   "transient" : {
      "apack.fasterbulk.combine.enabled":"false"
```

#### 8.1.9 Throttle cluster traffic with the aliyun-qos plug-in

**qos plug-in**

The aliyun-qos plug-in is a proprietary plug-in for Alibaba Cloud Elasticsearch (ES). This plugin provides cluster-level throttling for read and write requests to improve cluster stability. During critical periods, the plug-in lets you degrade specific index operations and keep traffic within a manageable range. For example, if an upstream service cannot control its traffic, especially for read requests, you can configure rules in the aliyun-qos plug-in to manage requests based on business priority and protect the stability of your ES cluster.

**Prerequisites**

You have created a version 7.10.0 Alibaba Cloud Elasticsearch instance. You have installed the aliyun-qos plug-in and upgraded it to the latest version. You have enabled a whitelist. For more information, see Security settings. You can log in to the Kibana console of the target ES instance and run the `GET` /_cat/plugins?v command to check the plug-in version.

> **Note:** The latest version of the plug-in for ES version `7.10.0` is **7.10.0_ali1.12.0.1.2**.

**Usage notes**

The throttling feature of the aliyun-qos plug-in is disabled by default. This plug-in is designed to protect the cluster and improve its stability, not for precise metering of read and write traffic. When you upgrade the aliyun-qos plug-in to the latest version, note the following: Due to differences in the implementation between versions, throttling may be temporarily unavailable during the upgrade. Throttling automatically resumes after the plug-in on the master node is upgraded. During data conversion from an old version to the new version, some rate limiters may fail to convert. If a conversion fails, run the following command to try again. If the command returns an error, retry it multiple times until `hasError` is `false` .

```
POST /_qos/limiter/ops/upgrade
```

> **Note:** If the command runs for a long time without returning a response, it indicates that no legacy rate limiters exist on the instance. You can ignore this step.

**Estimate thresholds**

To avoid affecting the performance of read and write requests, the aliyun-qos plug-in applies throttling at the cluster level. However, it does not perform precise metering of traffic on every node in the cluster, which can cause minor deviations from the configured threshold. Before you use the aliyun-qos plug-in, estimate your throttling thresholds based on the following guidelines: Query requests

```
 Throttling threshold for query requests = End-to-end QPS (queries per second) of
client requests that arrive at the ES cluster
```

> **Note:** The end-to-end QPS refers only to the number of query requests that reach a coordinating node per second.

Write requests The calculation for the write request throttling threshold is similar to that for query requests but must also be adjusted for the number of replicas. For example, consider a cluster with two data nodes and an index with one shard and one replica. When `10 MB` of data is written, each data node receives a `10 MB` write operation due to the replica. Additionally, internal tasks from X-Pack, such as Monitor, Audit, and Watcher, also consume write throughput. You must account for this overhead when you set the threshold.

**Enable throttling**

The throttling feature of the aliyun-qos plug-in is disabled by default. You must enable it before using it. All commands in this topic can be run on the Kibana console. For more information, see Log on to the Kibana console.

```json
PUT _cluster/settings
  "persistent": {
    "apack.qos.limiter.enabled": true
```

**Configure a rate limiter**

The following code and parameter descriptions explain how to configure a rate limiter.

> **Note:** A rate limiter consists of two main parts: the `limiters` definition and the `tags` definition. Use the `tags` object to define the resource scope and the `limiters` object to specify the throttling type and threshold.
> Rate limiters are classified as regular or default. To use a default rate limiter, set a **tag** to **. Examples include setting a default traffic limit per `shard` or a default QPS for each application.
> When a request exceeds a throttling limit, ES rejects subsequent requests.

For specific examples of how to configure a rate limiter, see Rate limiter configuration examples.

```json
PUT /_qos/limiter/${limiterName}
  "limiters": {
     "${action}.${limiter_type}":${threshold}
```

`},`

```json
  "tags": {
    "${tagName}":${tagValue}
```

`},`

```json
  "priority":0,
  "params":{
      "watchMode":true
```

| Parameter | Description | Value |
|---|---|---|
| action | The action to throttle. This setting limits specific types of requests. | write: Document write requests, which include index and create operations. update: Document update requests. delete: Document delete requests. search: Search requests. search shards: Requests to query the total number of shards _ for an index. |

| limiter ty _ pe | The throttling type. Rate Concurrency Per-request limits | rate: The rate of requests. This value must be an integer. qps: The query rate. This value must be an integer. tps: The write rate. This value must be an integer. throughput: The data throughput. This is supported only for the write, update, and delete actions. Valid units include GB, MB, and KB. The maximum value is 2 GB. thread count: The request concurrency. Each request is _ counted as one concurrent operation. concurrent count: The request concurrency, calculated _ based on the specific operations within a request. For example, search shards.concurrent count:20 allows _ _ a maximum of 20 concurrent shard queries. max per request: The maximum number of a specific _ _ operation type within a single request. For example, update.max per request:10 specifies that a single _ _ write request can contain at most 10 update operations. max size per request: The maximum size of a single _ _ _ request. This is supported only for the write, update, and delete actions. |
|---|---|---|
| threshold | The throttling threshold. | An integer within the int range that is greater than or equal to -1. Note Some types support strings with units. For more information, see the description of the limiter type _ parameter. |
| tagName | The name of the tag. | node: The name of the current node. is master: A boolean that indicates whether the current _ node is the master node. The tag value is true or false . index: The index name. If multiple index names are specified, the value is an array. If an alias is provided in the request, this tag resolves to the actual index name. This tag is available only for requests that are subclasses of IndicesRequest . shard: The shard name, in the format index[id] , such as test[0] . This tag is available only for requests that are subclasses of ReplicationRequest . index in url: The index string from the URL. If an alias is _ _ provided in the request, this tag contains the alias. This tag is available only for requests that are subclasses of IndicesRequest . |

| tagValue | The value of the tag. | A string or an array of strings. If an array is provided, the rule matches if the tag value is in the array. Exact matching, wildcard matching, and any-value matching are supported. Examples: Exact match: "abc" Wildcard match: "ab*" Any-value match: "**" Note Using "**" creates a default rate limiter. This means a separate, precise rate limiter is created for every value of this tag. For example, if you set index:"**",search.tps:1 , the search rate for each index is limited to 1, rather than limiting the total search rate to 1. |
|---|---|---|
| priority | The priority of the rate limiter. | An integer. Default value: 0. Note A higher value indicates a higher priority. If multiple default rate limiters match a request, only the highest- priority limiter applies. |
| params | Advanced parameters. | watchMode: Specifies whether to enable watch mode. Valid values: true and false (default). If this parameter is set to true , Elasticsearch only records rejections in its metrics but does not actually throttle requests. You can use this mode to validate throttling effects in advance and avoid incorrect configurations. For more information about the API, see FAQ. |

|   | true |
|---|---|
| true |   |

**Rate limiter configuration examples**

> **Note:** In the following examples, replace ${limiterName} with the name of your rate limiter.
> You can define multiple rules. A request is throttled if it matches any rule.

**Set search QPS throttling**

You can limit the number of query requests that a coordinating node receives per second by setting the number of allowed query requests per second for an index. If the number of requests received per second exceeds this limit, ES rejects the requests. The values for `index` and `index_patterns` support full index names and index wildcards.

| Actions | Code example |
|---|---|

| Set the search QPS limit for a single index. | PUT / qos/limiter/${limiterName} _ { "limiters": { "search.qps": "1000" }, "tags": { "index": "twitter" } } |
|---|---|
| Set the search QPS limit for indices with a specific name prefix. | PUT / qos/limiter/${limiterName} _ { "limiters": { "search.qps": "1000" }, "tags": { "index": "nginx-log-*" } } |
| Set a default search QPS limit for each individual index. | PUT / qos/limiter/${limiterName} _ { "limiters": { "search.qps": "1000" }, "tags": { "index": "**" } } Note The index:** expression applies the limit to each index individually. For example, if a cluster has three indices named A, B, and C, the search QPS for each index is limited to 1000 . |

| Set a total search QPS limit for all indices combined. | PUT / qos/limiter/${limiterName} _ { "limiters": { "search.qps": "1000" }, "tags": { "index": "*" } } Note The index:* expression applies the limit to all indices as a group. For example, if a cluster has three indices named A, B, and C, their combined search QPS is limited to 1000 . This is equivalent to not setting the index tag. |
|---|---|

When you run a query from a client or on the Kibana console, you receive the following error if the search QPS exceeds the configured limit. If you receive this error, adjust the search QPS limit accordingly.

```json
  "error": {
    "root_cause": [
        "type": "status_exception",
        "reason": "search blocked, limited by [<limiterName>][search.qps](<limiterId>)
threshold:[x]"
```

`],`

```json
    "type": "status_exception",
    "reason": "search blocked, limited by [<limiterName>][search.qps](<limiterId>) thre
shold:[x]"
```

`},`

```json
  "status": 429
```

**Set write TPS throttling**

By setting the number of write requests per second for an index, you can limit the number of write requests that a coordinating node receives. When the number of write requests received per second exceeds the throttling limit, ES rejects the requests. The values for `index` and `index_patterns` support full index names and index wildcards.

```json
PUT /_qos/limiter/${limiterName}
  "limiters": {
    "write.tps": "100000"
```

`},`

```json
  "tags": {
    "index": "nginx-log-*"
```

**Set Bulk write throughput throttling**

You can limit the number of write bytes that a coordinating node receives per second by setting the total bytes written per second for Bulk requests. When the number of write bytes received per second exceeds the limit, ES rejects the requests. The values of `index` and `index_patterns` support full index names and index wildcards.

```json
PUT /_qos/limiter/${limiterName}
  "limiters": {
    "write.throughput": "100MB"
```

`},`

```json
  "tags": {
    "index": "nginx-log-*"
```

**Set single Bulk request size throttling**

By setting the maximum size of a single Bulk request, you can limit the number of bytes that a coordinating node receives in a single write request. If a request exceeds the throttling limit, ES rejects the request. The values for `index` and `index_patterns` support full index names and index wildcards.

```json
PUT /_qos/limiter/${limiterName}
  "limiters": {
    "write.max_size_per_request": "1000"
```

`},`

```json
  "tags": {
    "index": "nginx-log-*"
```

When you submit a write operation from a client or on the Kibana console, you receive the following error if the request size exceeds the configured limit. If you receive this error, reduce the size of your individual write requests.

```json
  "error" : {
    "root_cause" : [
        "type" : "status_exception",
        "reason" : "write_size blocked, limited by [<limiterName>]
[write.max_size_per_request](<limiterId>) threshold:[x] try acquire [x]"
```

`],`

```json
    "type" : "status_exception",
    "reason" : "write_size blocked, limited by [<limiterName>]
[write.max_size_per_request](<limiterId>) threshold:[x] try acquire [x]"
```

`},`

```json
  "status" : 400
```

**Set concurrent shard query throttling**

You can reduce the load on the cluster by setting the number of concurrent query `shard` s. The values of `index` and `index_patterns` support full index names and index wildcards.

```json
PUT /_qos/limiter/${limiterName}
  "limiters": {
    "search_shards.concurrent_count": "10"
```

`},`

```json
  "tags": {
    "index": "nginx-log-*"
```

**Set multiple throttling rules**

You can simultaneously set multiple configurations for the rate limiter. The values for `index` and `index_patterns` support full index names and index wildcards.

```json
PUT /_qos/limiter/${limiterName}
  "limiters": {
    "search.qps": "1000",
    "write.tps": "100000",
    "write.throughput": "1000000",
    "write.max_size_per_request": "1000",
    "search_shards.concurrent_count": "10"
```

`},`

```json
  "tags": {
    "index": "nginx-log-*"
```

**Get rate limiter configurations**

Use the following commands to retrieve rate limiter configurations.

> **Note:** In the following examples, replace ${limiterName} with the name of your rate limiter.

| Actions | Code example |
|---|---|
| Get all rate limiter configurations | GET qos/limiter _ |
| Get the configuration of a specific rate limiter | GET qos/limiter/${limiterName} _ |
| Get the configurations of specific rate limiters Note Separate multiple rate limiter names with a comma (,). Wildcards are not supported. | GET qos/limiter/${limiterName1,limiterName2} _ |

**Delete a rate limiter configuration**

Use the following commands to delete rate limiter configurations.

> **Note:** In the following examples, replace ${limiterName} with the name of your rate limiter.

| Actions | Code example |
|---|---|
| Delete the configuration of a specific rate limiter | DELETE qos/limiter/${limiterName} _ |
| Delete the configurations of specific rate limiters Note Separate multiple rate limiter names with a comma (,). Wildcards are not supported. | DELETE qos/limiter/${limiterName1,limiterName2} _ |

**Disable throttling**

You can disable the throttling feature by setting the throttling parameter to `false` or `null` .

| Method | Code example |
|---|---|
| Set the parameter to false | PUT cluster/settings _ { "persistent": { "apack.qos.limiter.enabled": false } } |
| Set the parameter to null | PUT cluster/settings _ { "persistent": { "apack.qos.limiter.enabled": null } } |

**FAQ**

Q: How do I get monitoring metrics for throttling? A: You can use the following APIs: Get current metric data Get current metric data for all nodes

```
GET /_qos/limiter/nodes/stats
```

Get current metric data for a specific node

```
GET /_qos/limiter/nodes/${nodeId}/stats
```

Get current metric data for a specific node and rate limiter

```
GET /_qos/limiter/nodes/${nodeId}/stats/${limiterIds}
```

Get historical metric data Get all historical metric data

```
GET /_qos/limiter/metric
```

Get historical metric data for a specific rate limiter

```
GET /_qos/limiter/metric/${limiterId}
```

### 8.2 Use OpenSearch plugins

#### 8.2.1 Implement vector search using the opensearch-knn plugin

**opensearch-knn plugin**

OpenSearch supports vector search through the opensearch-knn plugin to enable locationbased search. This topic shows how to create a vector index, add location data, and perform a search to find the hotels closest to a target point.

**Background**

OpenSearch provides a vector search feature that uses the built-in `knn_vector` field type and efficient approximate nearest neighbor (ANN) algorithms, such as HNSW, to quickly find the most semantically similar documents in a large-scale, high-dimensional vector space. The vector search feature in OpenSearch helps you efficiently implement intelligent use cases, such as semantic search, personalized recommendations, image-based search, and anomaly detection. This capability enhances the user experience and system intelligence, making it a cornerstone for building next-generation intelligent search and recommendation infrastructure. This topic demonstrates how to create a vector index, add location data, and search for the hotels that are closest to a specific point.

**Prerequisites**

An OpenSearch instance is running. You have configured an IP address whitelist. For more information, see security settings.

**Procedure**

**Step 1: Create a vector index**

1. Log on to the Dashboards console.
2. In the left-side navigation pane, click **Dev Tools**.
3. Run the following command to create an index named `hotels-location` to store sample
hotel data.

```json
PUT /hotels-location
  "settings": {
    "index.knn": true
```

`},`

```json
  "mappings": {
    "properties": {
      "location": {
        "type": "knn_vector",
        "dimension": 2
```

| Parameter | Description |
|---|---|

|   | "index.knn": true |   | To use the vector search feature, you must set index.knn to true . Otherwise, you cannot use fields of the knn vector type. _ |
|---|---|---|---|
|   | "type": "knn vector" _ |   | Declares this field as a vector field. OpenSearch builds an ANN index for this field. By default, OpenSearch uses HNSW. |
|   |   | "type": |   |
|   | "knn vector" _ |   |   |
|   | "dimension": 2 |   | The vector dimension is 2, representing longitude and latitude coordinates, such as [longitude, latitude] or [x, y] . |

Vector search queries typically return more than zero results. By default, the system assumes these queries return a large amount of frequently changing data and does not cache the results. In OpenSearch 3.1.0 and later, you can enable caching for these queries by increasing the value of the `indices.requests.cache.maximum_cacheable_size` parameter. For example, you can set it to 256.

**Step 2: Add data to the index**

Add three sample documents to the index. Each document represents a hotel. The `location` field in each document contains a two-dimensional vector that specifies the hotel's location.

```json
POST /hotels-location/_doc/1
  "name": "Shanshui Hotel",
  "location": [
    116.4,
    39.9
```

`]`

```json
POST /hotels-location/_doc/2
  "name": "Starry Inn",
  "location": [
    116.5,
    39.8
```

`]`

```json
POST /hotels-location/_doc/3
  "name": "Cloud Hotel",
  "location": [
    116.35,
    39.92
```

`]`

**Step 3: Search the data**

To find the two hotels closest to the point `[116.41, 39.89]` , run the following vector search query. The `k` parameter specifies the number of top similar documents to return.

```json
 GET /hotels-location/_search
  "size": 2,
  "query": {
    "knn": {
      "location": {
        "vector": [
          116.41,
          39.89
```

`],`

```json
        "k": 2
```

The search results are as follows:

```json
  "took": 868,
  "timed_out": false,
  "_shards": {
    "total": 1,
    "successful": 1,
    "skipped": 0,
    "failed": 0
```

`},`

```json
  "hits": {
    "total": {
      "value": 3,
      "relation": "eq"
```

`},`

```json
    "max_score": 0.9998,
    "hits": [
        "_index": "hotels-location",
        "_id": "1",
        "_score": 0.9998,
        "_source": {
          "name": "Shanshui Hotel",
          "location": [
            116.4,
            39.9
```

`]` `},`

```json
        "_index": "hotels-location",
        "_id": "3",
        "_score": 0.99551964,
        "_source": {
          "name": "Cloud Hotel",
          "location": [
            116.35,
            39.92
```

`]` `]`

**Additional information**

In OpenSearch, you can either import your own vectors or let OpenSearch automatically generate vector embeddings from your data. Automating vector embedding generation reduces the data preprocessing workload required for data ingestion and search. For more information about OpenSearch, see the official OpenSearch documentation.

#### 8.2.2 Replicate indexes across clusters

OpenSearch supports cross-cluster index replication using the opensearch-cross-clusterreplication plugin. This topic describes how to create and configure clusters, set up connections and replication, and manage replication tasks to improve query performance and disaster recovery.

**Background**

OpenSearch provides a native cross-cluster replication (CCR) feature that allows you to asynchronously and incrementally replicate writable indexes from a leader cluster to one or more remote follower clusters, creating read-only replicas on the destination. By enabling CCR, you can distribute query loads across multiple follower clusters while maintaining the write performance of the leader cluster. This configuration improves overall throughput. In the event of a regional failure, you can quickly switch to a follower cluster, which enhances system disaster recovery and business continuity. The OpenSearch CCR feature is a key technique for building a highly available and scalable search infrastructure.

**Prerequisites**

You have created leader and follower OpenSearch clusters, and their instances are running properly. Ensure that the leader and follower clusters can connect to each other. If you need assistance, contact Alibaba Cloud technical support. You have enabled the whitelist. For more information, see Security Settings.

**Procedure**

1. . Log on to the OpenSearch Dashboards console**
Log on to the OpenSearch Dashboards console for the leader and follower clusters. For more information, see Log on to the Dashboards console.
2. . Create an index and insert data**
1. On the OpenSearch Dashboards console of the leader cluster, run the following command
to create a sample index named `hotels-index` .

```json
PUT /hotels-index
  "settings": {
    "index.knn": true
```

`},`

```json
  "mappings": {
    "properties": {
      "location": {
        "type": "knn_vector",
        "dimension": 2,
        "space_type": "l2"
```

2. Run the following command to insert sample data.

```json
POST /_bulk {"index":{"_index":"hotels-index","_id":"3"}} {"location":[5.2,4.4]}
```

3. . Set up a connection and enable replication**

> **Important:** Ensure that the leader and follower clusters can connect. If you need assistance, contact Alibaba Cloud technical support.
> You must replace the variables in the commands with your actual values. The data provided is for reference only.

1. On the OpenSearch Dashboards console of a new follower cluster, use one of the following
two methods to establish a remote repository connection to the leader cluster. This example creates a remote repository named `test01` , where `lrr-test` is the name of the leader cluster. Method 1

```json
PUT _cluster/settings?pretty
  "persistent": {
    "cluster": {
      "remote": {
        "test01": {
          "seeds": ["lrr-test-discovery.es-essen.svc.cluster.local:9300"]
```

| seeds | must follow the |
|---|---|

`<namespace>.svc.cluster.local:9300` . For example: `lrr-test-discovery.es-`

```
essen.svc.cluster.local:9300 .
```

Obtain `<clusterName>` and `<namespace>` directly from the Instance Management page of the **ES O&M console**.

|   | kubectl get opensearch -A |
|---|---|
| <clusterName> |   |

command to find the mapping between `<clusterName>` and `<namespace>` . Method 2

```json
PUT _cluster/settings
  "persistent": {
    "cluster.remote.test01.seeds": ["10.XX.XX.83:9300"]
```

The value of `seeds` must follow the format `<leader_cluster_node_IP:9300>` . For example: `10.XX.XX.83:9300` . Log on to the OPS1 machine and run the following command to get the node IP of the leader cluster:

```bash
kubectl get pod -nes-essen -owide | grep $<leader_cluster_name>
```

2. Run the following command on the follower cluster to start the replication task for a specific
index. In this example, the index is `hotels-index-bak` .

```json
PUT _plugins/_replication/hotels-index-bak/_start
  "leader_alias": "test01",
   "leader_index": "hotels-index",
   "use_roles":{
      "leader_cluster_role": "all_access",
      "follower_cluster_role": "all_access"
```

| Parameter | Description | Example value |
|---|---|---|
| leader alias _ | The name of the remote repository. | test01 |
| leader index _ | The index on the leader cluster to replicate. | hotels-index |
| use roles _ | Roles required by the security plugin for cross-cluster replication. | all access _ |

4. . View replication status**
On the OpenSearch Dashboards console of the follower cluster, run the following command to view the replication status of a specific index. In this example, the index is `hotels-index-` `bak` .

```
GET _plugins/_replication/hotels-index-bak/_status?pretty
```

The following output indicates that the replication status is normal.

```json
  "status": "SYNCING",
  "reason": "User initiated",
  "leader_alias": "test01",
  "leader_index": "hotels-index",
  "follower_index": "hotels-index-bak",
  "syncing_details": {
    "leader_checkpoint": 0,
    "follower_checkpoint": 0,
    "seq_no": 1
```

**More operations**

Pause a replication task on the follower cluster

```
POST /_plugins/_replication/$<follower-index>/_pause
```

`{}` Resume a replication task on the follower cluster

```
POST /_plugins/_replication/$<follower-index>/_resume
```

`{}` Stop (delete) a replication task on the follower cluster (cannot be resumed)

```
POST /_plugins/_replication/$<follower-index>/_stop
```

`{}` View the status of leader indexes for CCR.

```
GET /_plugins/_replication/leader_stats
```

View the status of follower indexes for CCR.

```
GET /_plugins/_replication/follower_stats
```

**FAQ**

By default, after creation, each node in a leader or follower cluster includes the remote_cluster_client role. If a node does not have the remote_cluster_client role, add it. In the **Elasticsearch O&M**
**console > Cluster O&M > Modify Configuration**. In the **elasticsearch.yml** section, add

```
 node.roles: '["data", "cluster_manager", "remote_cluster_client"]' .
```

### 8.3 Work with Kibana plug-ins

#### 8.3.1 Use the opendistro-alerting plug-in to implement cluster alerting

**implement cluster alerting**

If you want to implement monitoring and alerting in Elasticsearch and Kibana, you can install and configure the opendistro-alerting plug-in. This topic describes how to configure the alerting feature for the opendistro-alerting plug-in in Elasticsearch V6.8.

**Background information**

For more information about how to use the opendistro-alerting plug-in, see Official API documentation.

**Prerequisites**

You must install the opendistro-alerting plug-in both Elasticsearch and Kibana. For more information, see Install or uninstall plug-ins. Whitelist-based authentication is enabled. For more information, see the Security settings section of the Configure clusters topic.

**Limits**

Only Elasticsearch V6.8 supports this feature.

**Procedure**

**Step 1: Log in to the Kibana console of the Elasticsearch**

**cluster**

1. Log in to the Alibaba Cloud Search and Analytics Service console.
2. In the left-side navigation pane, click **Clusters List**.
3. On the **Instance List** page, click the name of the desired cluster to go to the **Basic**
**Information** page.
4. In the **Kibana Information** section, click the endpoint next to **Kibana Console**
**Connection URL**.
5. Enter the username and password, and click **Log In** to log in to the Kibana console.

> **Note:** The username is elastic by default. The password is the one you specified for the elastic username when you created your Elasticsearch cluster.

**Step 2: Prepare test data**

1. In the upper-left corner, click the More icon. In the left-side navigation pane, choose
**Management > Dev Tools**. On the **Console** tab, enter the following test data.
i. Create a test index.

```json
PUT /error-demo
  "mappings": {
    "_doc": {
      "properties": {
        "message": {
          "type": "text"
```

ii. Write data to the index.

```json
POST /error-demo/_doc "message": "demo test error message" POST /error-demo/_doc "message": "demo test message"
```

iii. Run the following command to check whether the data is written:

```
GET /error-demo/_search
```

If a result similar to the following is returned, the data is written.

```json
  "took" : 51,
  "timed_out" : false,
  "_shards" : {
    "total" : 5,
    "successful" : 5,
    "skipped" : 0,
    "failed" : 0
```

`},`

```json
  "hits" : {
    "total" : 2,
    "max_score" : 1.0,
    "hits" : [
        "_index" : "error-demo",
        "_type" : "_doc",
        "_id" : "D-B0HZwBHT2vvpZBDXP-",
        "_score" : 1.0,
        "_source" : {
          "message" : "demo test error message"
```

`},`

```json
        "_index" : "error-demo",
        "_type" : "_doc",
        "_id" : "3WN0HZwBK1jX6iBUOWN2",
        "_score" : 1.0,
        "_source" : {
          "message" : "demo test message"
```

`]`

**Step 3: Create a destination**

1. In the upper-left corner, click the More icon. In the left-side navigation pane, choose **Open**
**Distro for Elasticsearch > Alerting**. On the page that appears, click the **Destinations**
tab.
2. On the **Destinations** tab, click **Add destination**.
3. On the **Add destination** page, enter the destination configuration information and click
**Create**.

| Parameter | Description |
|---|---|
| Name | The name of the destination. In this example, error Destination01 _ is used. |
| Type | Click the drop-down list and select one of the following three types: Amazon Chime Alerts or messages are sent to Amazon Chime chat channels. If you select this type, you need to create an incoming webhook in Chime. Slack Messages are sent to specified channels or users in your Slack workspace. If you select this type, you must use the incoming webhook URL provided by Slack. Custom webhook You can use a custom HTTP webhook URL to integrate with external systems that support HTTP POST requests, such as Teams, Mattermost, and user-created notification systems. In this example, Custom webhook is selected. |

|   |   | Both Define endpoint by URL and Define endpoint by custom attributes URL are supported. Define endpoint by URL: The endpoint is defined by specifying a URL. You can enter or specify a complete request URL. The system uses this URL as the endpoint of the service or API operation. Example: https://oapi.dingtalk.com/robot/send? access token=xxxxxxxxxxx . In this example, Define _ endpoint by URL is selected. Define endpoint by custom attributes URL: The endpoint is defined by specifying a custom attribute URL. No fixed URL is used. Instead, the final URL is concatenated or generated by using a set of custom attributes, such as protocol, hostname, port number, and path. |   |   |
|---|---|---|---|---|
|   |   |   | https://oapi.dingtalk.com/robot/send? |   |
|   | Settings | access token=xxxxxxxxxxx _ |   |   |
|   | Trigger condition | A custom HTTP request header that is used to transmit metadata or perform authentication. |   |   |

**Step 4: Create and define a monitor**

1. In the upper-left corner, click the More icon. In the left-side navigation pane, choose **Open**
**Distro for Elasticsearch > Alerting**. On the page that appears, click the **Monitors** tab.
2. On the **Monitors** tab, click **Create monitor**.
3. On the **Create monitor** page, specify the required parameters.

| Parameter | Description |
|---|---|
| Monitor name | The name of the monitor. In this example, error monitor01 is _ used. |
| Schedule | The scheduling settings, including: Frequency: specifies a time interval at which the system automatically executes a monitoring task. Every: specifies a specific time interval. In this example, every one minute is specified. |
| Monitor state | Controls whether the monitor runs. Off (Disable monitor): The monitor is enabled and will run automatically at the specified interval. On: If the switch is turned on, the monitor is disabled and does not execute monitoring tasks. |

4. Define the monitor.

| Parameter | Description |
|---|---|
| Define monitor | You can define monitors by selecting Define using visual graph (using visual images) or Define using extraction query (using specific query statements). If you select Define using visual graph, you need to select values for Index and Time field. If you select Define using extraction query, you need to select a value for Index, enter the query condition, and click Run to view the query results. In this example, Define using extraction query is selected. |
| Index | Click the drop-down list and select the index that you want to use. |
| Define extraction query | The following example shows the query condition. This query is to obtain data that includes the error keyword from messages. { "size": 1, "query": { "match": { "message":"error" } } } |

| Extraction query response | After you enter the query condition in the left section and click Run, the corresponding query results are returned in the right section. |
|---|---|

5. Click **Create**.

**Step 5: Create a trigger**

1. On the **Create Trigger** page, define and configure an alert trigger.

| Parameter | Description |
|---|---|
| Trigger name | The name of the trigger. In this example, error trigger01 is used. _ |
| Severity level | The severity of the trigger. |
| Extraction query response | The response to queries. The response is specified in the alert definition and cannot be modified. |

| Trigger condition | The condition to trigger the alert. You can modify the condition based on your business requirements. Example: ctx.results[0].hits.total > 0 . This indicates that an alert is triggered when the number of returned entries exceeds 0. |
|---|---|

2. After you configure the preceding settings, click **Run** to check the configuration condition. If
**true** is returned, the configuration condition is correct.

**Step 6: Configure an alert notification**

In the **Configure Actions** section, you can configure an alert notification. Enter the name, destination address, and notification message based on your requirements, and click **Create**.

| Parameter | Description |
|---|---|
| Action name | The name of the notification. In this example, error notification01 _ is used. |
| Destination name | The destination address of the notification. In most cases, the address is a URL. Click the drop-down list and select a destination address. In this example, error Destination01 is used, and it _ is a custom webhook. |
| Message | The content of the notification. The content can be modified based on your requirements. |
| Message preview | The notification preview, which cannot be modified. |

**Step 7: View the created alert**

In the upper-left corner, click the More icon. In the left-side navigation pane, choose **Open**
**Distro for Elasticsearch > Alerting**. On the **Dashboard** tab, view the created alert.
rver

## 9 Elasticsearch MCP Server

Powered by Model Context Protocol (MCP), Elasticsearch uses the hosting mode of Apsara Copilot to call the API to obtain Elasticsearch cluster information. You can also deploy MCP Server to query Elasticsearch cluster information. This helps you develop a natural languagedriven data query agent to query data and visualize intelligent data processing.

**Supported MCP modes**

Hosting mode of Apsara Copilot You can directly access the hosting mode of Apsara Copilot through a large language model without configuration. Manual MCP Server deployment Users can deploy applications, agents, or AI themselves.

**Hosting mode of Apsara Copilot**

> **Note:** Before you use the hosting mode of Apsara Copilot, refer to **Apsara Uni-manager** **Management Console > Apsara Copilot User Guide** and enable Apsara Copilot.

1. Log on to the Alibaba Cloud Elasticsearch console.
2. View the predefined MCP list.
In the navigation pane on the left, go to **AI Column > MCP** to view the list of preset MCPs. The preset system tools are listed below:

| Tool Name | API operation | Description |
|---|---|---|
| Global feature query | ListGlobalFeature s | Lists the global features of the Elasticsearch service. This helps you better apply the global features of Elasticsearch to your businesses. |
| Network list query | ListNetworkTypes | Lists the network types supported by the Elasticsearch service. This helps you select a proper access mode to access virtual private clouds (VPCs) and build a network architecture that best suits your businesses. |
| StorageClass list query | ListStorageClass | Lists the features for querying StorageClasses. You can filter StorageClasses based on your requirements and view the returned StorageClass information. This helps you optimize storage costs and choose a storage solution that balances performance and cost. |

rver

| CPU brand query | ListCpubrands | Queries the CPU brands supported by the current Elasticsearch service and the relevant information. You can view the CPU types supported by the cluster. This helps you select an appropriate chip type for business planning. |
|---|---|---|
| Deployment architecture query | ListDeploymentAr chs | Queries the detailed information about the architecture of the Elasticsearch service. You can view the zones in which the Elasticsearch service is deployed and the information about each node, and use the information for management and maintenance. |
| Version list query | ListEsVersions | Lists information about the supported Elasticsearch versions. You can view all supported engine versions. This helps you select an engine version that best suits your businesses. |
| Zone query | ListZones | Lists the information of zones in the specified region. You can view the supported zones, which helps you select proper zones in disaster recovery or non-disaster recovery scenarios. |
| Query instance snapshot repository information | GetSnapshotRep oInfo | Queries the detailed information about an Elasticsearch snapshot repository. You can view detailed information about a snapshot repository, such as the path, bucket, and AccessKey pair of the snapshot repository. |
| Snapshot repository list query | ListSnapshotRep oInfos | Queries a detailed list of Elasticsearch snapshot repositories. You can view the list of snapshot repositories, which helps you manage snapshot repositories and storage policies. |
| Pod information query | GetElasticsearch PodInfo | Queries the pod information of the specified Elasticsearch cluster. You can view the status information of Kubernetes pods for a specified instance to quickly assess pod health. |
| Pod log query | GetElasticsearch PodLogs | Queries the logs of pods in the specified Elasticsearch cluster. You can view the logs of a K8s Pod on a specified instance to diagnose issues with an abnormal Pod and quickly resolve them. |

rver

| Kibana plug-in query | ListKibanaPlugins | Lists the Kibana plug-ins installed in the specified Elasticsearch cluster. You can view the features provided by Kibana plug-ins installed in the specified Elasticsearch cluster and use them to meet your data visualization and analysis requirements. |
|---|---|---|
| Querying for instances | ListInstance | Elasticsearch – List Elasticsearch instances. You can view and manage instances. |
| Node list query | ListAllNode | Queries nodes in the specified Elasticsearch cluster and the status of the nodes. This lets you view data nodes, dedicated master nodes, client nodes, and Kibana nodes in the specified Elasticsearch cluster and their health status, which helps you quickly locate unhealthy nodes. |
| Available specification query | ListAvailiableSpe cs | Queries the node specifications supported by the Elasticsearch service. This lets you view the specifications supported by the specified node type. |
| Dictionary information query | ListDictInformatio n | Queries the dictionary information of an Elasticsearch cluster. This helps you view the dictionary information of the specified cluster. |
| Dictionary list query | ListDicts | Lists the available dictionaries in an Elasticsearch cluster. This helps you quickly view the list of dictionaries that are configured for the specified cluster, which facilitates dictionary management. |
| Plug-in list query | ListPlugins | Lists plug-ins in the specified Elasticsearch cluster. This lets you manage and view plug-ins in the specified cluster. |
| Snapshot list query | ListSnapshots | Lists the snapshots of the specified Elasticsearch cluster. You can view the list of snapshots and their statuses for a specific instance to help optimize snapshot management. |
| Security setting details list query | ListUserSecurityI nfo | Queries the security setting details of the specified Elasticsearch cluster. You can view the security settings of the specified cluster. |

rver

| Querying instance health status | DescribeElasticse archHealth | Queries the health status of the specified Elasticsearch cluster. You can view the health of a cluster to promptly identify instance failures. |
|---|---|---|
| Query instance details | DescribeInstance | Queries the detailed information of the specified Elasticsearch cluster. You can view the configuration, status, chip type, network type, and node information of the specified cluster, which helps you monitor and maintain the cluster. |
| Query the instance snapshot configuration | DescribeSnapsho tSetting | Queries the snapshot configuration of an Elasticsearch cluster. You can view the snapshot configuration and backup policies of the specified cluster. This helps you optimize data backup management. |
| Querying Configuration Files for Instance Plug- ins | GetConfigFiles | Queries the plug-in configuration files of the specified Elasticsearch cluster. You can view the configuration of the specified plug-in. This facilitates plug-in usage and management. |
| Cluster configuration details query | GetElasticsearch Settings | Queries the configuration details of an Elasticsearch cluster. You can view the configuration of the specified cluster and modify the configuration to improve the performance of the cluster. |

3. Use Apsara Copilot to call the tools.
i. In the upper part of the page, click the icon in the toolbar to open the **Apsara Copilot** panel. ii. In the lower part of the panel that appears, click the icon, turn on **MCP**, and click the icon to open the **Select MCP** panel. iii. Select the existing Elasticsearch MCP (**Elasticsearch**). iv. Click **OK**. After you return to the previous panel, describe the content of the query using the natural language, such as "instance list query". v. Click the icon on the right to send and execute the instruction. vi. Wait until the task is complete. Then, you can view the returned result.

**Manually deploy MCP Server**

1. Download the MCP service package.
2. Deploy MCP Server in an Elastic Compute Service (ECS) instance, container, or external
server. rver
3. You can integrate MCP as a backend service into an AI application, AI agent, or Robotic
Process Automation (RPA) process.
4. Call the RESTful API to use the MCP features.
