---
title: "Alibaba Cloud Apsara Stack v3.18.6-2607 Elasticsearch Product Introduction 20260825"
product_version: "V3.18.6_2607"
doc_version: "20260825"
pdf_pages: 15
source_pdf: "Alibaba Cloud Apsara Stack v3.18.6-2607 Elasticsearch Product Introduction 20260825.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/3816%202607/pdf%203/%E6%A3%80%E7%B4%A2%E5%88%86%E6%9E%90%E6%9C%8D%E5%8A%A1Elasticsearch%E7%89%88/Alibaba%20Cloud%20Apsara%20Stack%20v3.18.6-2607%20Elasticsearch%20Product%20Introduction%2020260825.pdf"
converter: pdf2md (PyMuPDF line classifier)
---

# Alibaba Cloud Apsara Stack v3.18.6-2607 Elasticsearch Product Introduction 20260825

## Alibaba Cloud Elasticsearch

Elasticsearch is a real-time, distributed search and analysis engine based on Lucene. It is a leading open source enterprise search engine available under the Apache license. It provides a distributed service that enables users to store, search, and analyze massive datasets quickly and in near real-time. Elasticsearch is often the core engine for applications that require complex query features and must handle high query volumes. An Elasticsearch cluster is a distributed system composed of multiple nodes. These nodes work together to store data and provide indexing and search capabilities across the entire cluster. To improve horizontal scaling, the system splits large indexes into multiple shards, which are then distributed among the nodes. Elasticsearch also creates replica shards on different nodes to back up data. This process increases high availability, distributes the search workload, and improves concurrent performance. Alibaba Cloud Elasticsearch provides a service that is 100% compatible with open source Elasticsearch. The service supports multiple versions of the open source ES kernel and includes targeted performance optimizations. Alibaba Cloud Elasticsearch also offers many proprietary technologies, such as plugins and features for Chinese tokenization, AISearch, query Quality of Service (QoS), cross-cluster replication, data compression, and aggregated writes. The service provides enterprise-grade capabilities, including zone-disaster recovery for high availability, snapshot backup and recovery, security authentication, visual cluster creation, plugin management, multi-tenancy, and Auto Scaling. In addition to Elasticsearch, Alibaba Cloud also fully supports OpenSearch. The default OpenSearch version provided is 3.1.0. OpenSearch, forked from Elasticsearch 7.10, is a continuously evolving project that aims to provide an open, extensible, and vendor-neutral platform for search and analysis. The Alibaba Cloud OpenSearch service is fully compatible with the open source OpenSearch ecosystem and supports core features such as Dashboards, SQL queries, Piped Processing Language (PPL), Index State Management, and asynchronous search. The service also integrates Alibaba Cloud's security systems, monitoring and alerts, automatic backups, and Auto Scaling capabilities. You can deploy either the Elasticsearch or OpenSearch engine to meet your business needs. This provides a unified, cloud-native management experience with an enterprise-grade Service-Level Agreement (SLA).

### Product details

Alibaba Cloud Elasticsearch is fully compatible with open-source Elasticsearch and OpenSearch. It supports multiple versions of open-source Elasticsearch and OpenSearch version 3.1.0, featuring targeted kernel performance optimizations. Additionally, it offers multi-tenancy, permission and security management, auto scaling, third-party or custom plug-ins uploads, data backup, and cross-cluster index synchronization.

**Multi-tenancy**

Alibaba Cloud Elasticsearch supports multi-tenancy, enabling multiple business units to share the Elasticsearch service on the cloud platform while ensuring data isolation between them. Each tenant can create and use one or more Elasticsearch clusters, as well as configure the number of cluster nodes, node specifications, and related parameters as needed. Alibaba Cloud Elasticsearch ensures a high level of data isolation and robust security for user data.

**Permission and security management**

Alibaba Cloud Elasticsearch controls account permissions and supports role-based access control. The operations console distinguishes between read-only roles and read/write roles to isolate permissions during resource creation and O&M processes. All write operations performed by users on the console are logged, ensuring full traceability of any changes. You can set a unique password for each instance to ensure data security.

**PB-level search**

Powered by distributed storage and indexing technologies, the system supports near realtime analysis and retrieval of massive datasets at the petabyte scale.

**Auto scaling**

The cluster scales horizontally. Server scale-out and scale-in operations do not affect business queries and require zero service downtime.

**Near real-time search**

Data becomes available for analysis and retrieval almost immediately after import. You can query newly ingested data within milliseconds, achieving millisecond-level response times.

**Full-text search for massive data**

Designed for massive full-text databases, the system stores structured and text-based keyword information to enable multi-dimensional matching, filtering, inverted indexing, and full-text retrieval.

**Visualization**

The system provides a user-friendly visualization platform for massive index repositories and full-text search clusters. It allows you to view the status of index repositories and clusters in real time, with basic metrics displayed through a web interface.

**API**

The system provides native Elasticsearch APIs for data import, index creation, and data retrieval in big data search services.

**NLP tokenizer**

The system integrates Alibaba DAMO Academy's proprietary Natural Language Processing (NLP) tokenization plug-in, which supports natural semantic understanding and word segmentation for Chinese. It also supports lexicon expansion and provides multi-language analyzer capabilities via custom plug-ins. Supported languages include Chinese, Uyghur, Tibetan, Arabic, Russian, Japanese, Korean, and more.

**Vector retrieval**

The system supports vector similarity matching for unstructured data, such as images and voiceprints. This enables scenario-based applications including image-to-image search, video matching, and voice recognition.

**Geographic information query matching**

Powered by custom plug-ins, the system supports geographic information query matching. You can define, query, and aggregate geographic data using non-geographic coordinate formats.

**Custom plug-in and lexicon expansion**

The system allows you to upload third-party or custom plug-ins. It also provides extensive configurations such as tokenization, synonyms, correction terms, and blocked words to improve search effectiveness and meet personalized full-text retrieval requirements.

**Aggregation write**

The system supports pushing down aggregation operators to improve search and aggregation analysis performance.

**Sorting**

The system supports sorting by relevance and by fields such as time.

**Comprehensive search**

Keyword and comprehensive searches deliver millisecond-level response times, while fuzzy and batch searches achieve second-level responses.

**Data backup**

Powered by the data snapshot technology on a distributed file system, the system performs data backups and rapid recovery to ensure data reliability. It also supports snapshot backup and restoration through Alibaba Cloud Object Storage Service (OSS).

**Cross-cluster data replication (XDCR)**

The XDCR feature supports cross-cluster data replication to facilitate business disaster recovery.

**Cluster-wide throttling (QoS)**

The aliyun-qos plug-in, developed by the Alibaba Cloud Elasticsearch team, enhances cluster stability through cluster-level read/write throttling. During peak traffic periods, it can gracefully downgrade specified indices to keep traffic within appropriate limits. For example, if upstream services cannot manage traffic spikes, especially for read-heavy workloads, you can configure aliyun-qos plug-in rules to appropriately downgrade traffic based on business priority, thereby protecting the stability of the Elasticsearch service.

**Index compression (aliyun-codec)**

The aliyun-codec plug-in, developed by the Alibaba Cloud Elasticsearch team, compresses multiple types of underlying Elasticsearch (ES) index files and supports the source_reuse_doc_values feature. This plug-in is suitable for high-write-volume scenarios with strict index storage budegets, such as log processing and time-series analysis, as it significantly reduces index storage costs.

**Ecosystem compatibility**

The system is compatible with both the Elasticsearch and OpenSearch ecosystems. Rich ecosystem components include Kibana, Dashboard, and Grafana.

### Common scenarios

Alibaba Cloud Elasticsearch can be used in many scenarios, including log analysis and fullstack observability, information retrieval, and data intelligence.

**Intelligent Q&A systems using RAG**

Alibaba Cloud Elasticsearch uses retrieval-augmented generation (RAG) technology to combine the generation capabilities of large language models (LLMs) with the real-time search of Elasticsearch. This combination is used to build dynamic, accurate, and verifiable intelligent Q&A systems for enterprises. This scenario is ideal for businesses that need to integrate internal knowledge bases, such as documents, databases, and logs, to generate high-quality answers in real time. Common use cases include customer service systems, compliance reviews, and medical-assisted diagnostics.

**Log analysis and observability**

In complex business scenarios, a vast number of devices, such as servers, physical servers, Docker containers, mobile devices, and IoT sensors, generate large volumes of diverse and unstructured metrics, logs, and application performance management (APM) data. This volume of data presents significant challenges for full-link anomaly detection, business analysis, and Operations and Maintenance (O&M). Users often struggle to extract value from complex logs while facing high storage costs. Alibaba Cloud Elasticsearch uses open source components, such as Beats and Logstash, to quickly connect to common data sources. Kibana dashboards can be used to efficiently build visual O&M dashboards. These dashboards can be flexibly configured with information such as hostnames, IP addresses, deployment status, and display colors. This process helps users quickly locate and identify issues within massive datasets, improving problem-solving efficiency and unlocking the value of log data.

**Information retrieval**

People use the mobile internet daily to query various types of information. For example, they search for credit card bills, electronic invoices, nearby restaurants and hotels, media inquiries, shopping orders, and logistics information. To help users efficiently retrieve information, businesses need to implement information retrieval services for massive datasets. Compared to traditional relational databases, Elasticsearch has powerful full-text search capabilities and provides easy-to-use RESTful APIs and clients for various languages. It can find matching information in petabytes of structured and unstructured data in just a few milliseconds. Alibaba Cloud Elasticsearch provides high availability, ease of use, and various self-developed plugins that support complex combinations, conditional queries, and fuzzy queries. It easily handles high-performance reads and writes for various data types, including text, numbers, dates, IP geolocation data, and even images, audio, and video. This enables the rapid development of retrieval services, such as e-commerce product or order search, app search, and enterprise Customer Relationship Management (CRM) systems, and their integration into existing business frameworks.

**Data intelligence**

With the rapid development of industries such as gaming, education, and retail, massive amounts of business data are generated in addition to the log and metric data from underlying systems. This data includes user behavior, driving routes, and transaction records. In a data-driven operational context, in-depth statistical analysis and mining of this business data are required to identify problems and opportunities for upper-layer services and to support business decisions. This process is how data is used to generate business value. Alibaba Cloud Elasticsearch provides structured query capabilities and supports complex filtering and aggregation functions. It can quickly and efficiently analyze data such as user behavior, properties, and tags to enable precise audience targeting. Additionally, Kibana can be used to perform statistical classification of business data and build comprehensive dashboards. As a result, massive datasets in scenarios such as e-commerce, mobile applications, and advertising media can be efficiently analyzed to uncover deep business value.

### Product value

Alibaba Cloud Elasticsearch is a service that is 100% compatible with open source Elasticsearch. It supports multiple versions of open source Elasticsearch and includes a kernel optimized for high performance. The service extends the open source product with proprietary plugins for Chinese tokenization and vector search. It also provides enterprisegrade security authentication, visual tools for managing clusters and plugins, and pluginbased support for SQL queries and snapshot backups.

**Near real-time search and analysis**

The service uses distributed storage and index retrieval technology to handle massive data volumes. It provides real-time analysis and retrieval for petabyte-scale data with millisecondlevel responses.

**High-performance vector search**

You can perform millisecond-level similarity searches on high-dimensional vector data, such as text embeddings, image feature vectors, and audio fingerprints. This high-performance vector search capability improves the response speed and accuracy of AI applications. It also resolves the efficiency and precision issues found in traditional systems that process vector data.

**Elastic scaling**

You can scale out your cluster horizontally. The scaling process is smooth and does not affect queries if replicas are present. No service downtime is required.

**Visual search and analysis**

The service includes web-based, user-friendly tools for managing large-scale index libraries and full-text search clusters.

**Data queries**

SQL queries: After data is ingested, you can use a plugin to run SQL-compatible queries. Geographic information queries: You can use a plugin to run geographic information queries.

**Access control**

You can configure permissions to separate write permissions from read-only permissions. You can create and manage multiple identities under a single account and assign different permissions to each identity to control user access to resources. You can manage multiple clusters from a central location. This includes features such as dynamic configuration, resource management, and resource isolation.

**Data security**

You can use password protection to prevent unauthorized access and avoid data breaches. You can create multiple clusters and manage their passwords and configurations independently. This lets you segment and manage permissions at the business level. You can use operation logs to record all changes. You can flexibly control read and write permissions for data at the index and field levels within an Elasticsearch cluster. The service follows Alibaba Cloud's three-network isolation standard. You can view the IP addresses of all domain names in the console to prevent unintended network exposure.

**Data backups**

You can use a custom plugin to perform snapshot backups and restore data with Alibaba Cloud OSS. This feature uses data snapshot technology based on a distributed file system to back up data and enable fast recovery, ensuring data reliability. You can perform full or incremental data backups. You can back up data clusters between data centers to meet mutual backup requirements. You can manage backups within a cluster through a visual interface.

**Data synchronization**

You can synchronize data between clusters using a proprietary cross-cluster index synchronization plugin.

**Simple deployment and maintenance**

You can use a proprietary management platform to create Elasticsearch clusters and Kibana visualization tools with a single click. This provides a flexible and convenient operation.

**Business monitoring**

Instance-level monitoring data is integrated with Cloud Monitor. The service provides a rich set of metrics by default. This lets you analyze metrics and configure alerts for your business clusters.

**Chinese tokenization**

The service integrates mainstream Chinese tokenization plugins by default, including the third-party IK Analyzer and the proprietary Alibaba DAMO Academy Chinese tokenization plugin.

**Vector search**

The service integrates Alibaba Cloud's proprietary vector search plugin by default. It supports vector search scenarios such as image search, video fingerprinting, facial recognition, and speech recognition.

**Kernel enhancements**

Some versions provide Alibaba Cloud kernel engine features that significantly enhance product performance compared to open source Elasticsearch. For example, Alibaba Cloud's Elasticsearch 7.10 version offers major improvements in cluster scheduling speed with a massive number of shards, write performance for documents with primary keys, and time series query performance.

**Disaster recovery deployment**

The service provides business disaster recovery capabilities and supports a disaster recovery architecture that uses cross-zone deployment.

**Service stability**

A targeted management and scheduling design optimizes the deployment structure. This design minimizes the chance of allocating primary and replica shards to nodes on the same server, which improves the high availability of the Elasticsearch cluster.

**Opendistro ecosystem support**

The service supports the open source Opendistro ecosystem. This provides capabilities for scenarios that are covered by the commercial X-Pack in open source Elasticsearch. These capabilities include but are not limited to the following: You can manage the lifecycle of indexes by integrating the Index State Management (ISM) plugin. You can use the Security plugin to enable Lightweight Directory Access Protocol (LDAP) capabilities.

### Functions and features

This topic provides an overview of the functions and features of Alibaba Cloud Elasticsearch to help you quickly understand its capabilities.

| Level 1 feature | Level 2 feature | Level 3 feature | Feature description |
|---|---|---|---|
| Security | Security isolation | Network security | Establishes network boundaries based on hybrid cloud standards, allowing the registration of existing network egresses and providing fully isolated access to SRS for dedicated worker nodes. |
|   | Security audit | Operation log audit | Logs all write operations performed on the Elasticsearch console. |
|   | Data security | Data replica redundancy | Distributes primary and replica shards across different physical machines. |
|   | Access control | Encrypted access | Secures data in transit by using Transport Layer Security (TLS) encryption for access links. |
|   |   | IP allowlist | Controls access to your cluster by using an IP allowlist. |
|   |   | Internet access | Supports internet access. |
| Storage | Data node storage | Solid State Drive (SSD) disk | Data nodes support storage on SSD disks. |
|   |   | Hard Disk Drive (HDD) disk | Data nodes support storage on HDD disks. |
|   | Dedicated master node storage | Logical Volume Manager (LVM) partition | Dedicated master nodes support LVM-partitioned disks. |

| Disaster recovery and backup | Disaster recovery Note Currently, only Elasticsearch instances support disaster recovery capabilities. | Same-region dual-AZ disaster recovery | Supports dual-AZ disaster recovery deployments in the same region. |
|---|---|---|---|
|   |   | Same-region triple-AZ disaster recovery | Supports triple-AZ disaster recovery deployments in the same region. |
|   |   | Geo-disaster recovery | Supports geo-disaster recovery across different regions. |
|   | Backup | Data backup and restoration | Provides full and incremental backup and restoration features based on Object Storage Service (OSS). |
|   | Data replication | Cross-cluster index synchronization | Supports cross-cluster data replication to help achieve business disaster recovery. |
| Management and control | Visualization tools | Kibana/Dashboards | Provides out-of-the-box visualization components. |
|   |   | Visual management of index templates | Supports visual management of index templates in Kibana or Dashboards. |
|   | Product console | Change operations | Allows you to perform change operations such as creating resources on the console. |
|   | Brand management | White-labeling | Supports white-labeling, allowing you to hide logos and other brand-specific information. |
|   | Node management | Anti-affinity | Supports anti-affinity policies during node creation to improve resilience. |
|   | Dictionary management | Cold and hot updates for custom dictionaries | Supports both cold and hot updates for custom dictionaries. Hot updates do not require an instance restart. |
| 2 | > Document Version: 2026082 |   |   |

|   | Parameter configuration | GUI-based parameter management | Supports GUI-based management of instance parameters on the console. |
|---|---|---|---|
|   | Language analysis | aliws for Chinese word segmentation | Supports the Alibaba Cloud proprietary analysis-aliws plugin for Chinese word segmentation. |
|   |   | analysis-ik plugin for Chinese word segmentation | This plugin provides a dictionary-based segmentation algorithm. This enhanced version of the open- source plugin supports dynamic loading of dictionary files from OSS and enables both cold and hot updates for IK dictionaries. |
|   |   | analysis-kuromoji for Japanese word segmentation | Supports the analysis- kuromoji plugin for Japanese word segmentation. |
|   |   | analysis-phonetic plugin for phonetic analysis | This plugin converts differently spelled words into identical phonetic representations, enabling matching of similarly pronounced words. |
|   |   | analysis-smartcn for mixed Chinese-English analysis | This smart Chinese analysis plugin is primarily used for analyzing Chinese or mixed Chinese-English text, especially for segmenting simplified Chinese text. |
|   |   | analysis-pinyin plugin for pinyin analysis | This plugin performs conversion between Chinese characters and pinyin, enabling keyword searches using either format. |
|   | Multi-format document attachment processing | ingest-attachment plugin for processing attachments in multiple formats | This plugin indexes content from documents in various formats such as Word, Excel, PDF, and PPT. |

| Engine & plugins |   |   |   |
|---|---|---|---|
|   | Index management | opendistro index man _ _ agement plugin for index management | This plugin automates index lifecycle management, performance optimization, and status monitoring. |
|   | SQL support | SQL plugin | This plugin lets you query data in Elasticsearch by using standard SQL statements, just like querying a traditional database. |
|   | Full-text search | Text search | Provides powerful full-text search, including exact matching, fuzzy queries, prefix/suffix matching, and custom tokenization logic. It handles the retrieval of both long and short texts and allows you to customize result ranking based on recall data. |
|   | Vector search | Vector search | Combines powerful search features of Elasticsearch with vector similarity calculations, making it ideal for scenarios like recommendation systems, image retrieval, and natural language processing. |
|   | Index compression | Proprietary aliyun- codec plugin for index compression | This plugin integrates multiple compression algorithms to significantly reduce index storage costs. |
|   | Cross-cluster replication | Proprietary XDCR plugin for cross- cluster replication | This plugin synchronizes index data from one cluster to another. |
|   | Cluster-wide throttling | Proprietary aliyun-qos plugin for cluster-wide throttling | This plugin enables throttling on key metrics such as read/write rate, concurrency, and individual requests. During peak loads, it can downgrade specific indexes to keep traffic within an appropriate range. |
|   | Aggregated write | Proprietary faster-bulk plugin for aggregated write | This plugin improves write throughput by batching write requests based on size and time intervals. |

| Networking | Service IP address | Dual-stack IP | The service virtual IP (VIP) supports IPv6/IPv4 dual-stack mode. |
|---|---|---|---|
| Monitoring and operations | Monitoring | Grafana | Allows you to create custom monitoring dashboards in Grafana. |
|   |   | Kibana | Supports full observability and monitoring features through Kibana. |
|   |   | Cluster resource monitoring | Displays the total and allocated resources for cluster nodes. |
|   | Log management | GUI-based slow log search | Allows you to search slow logs through a GUI on the Log Center. |
|   |   | GUI-based business log search | Allows you to search business logs through a GUI on the Log Center. |
|   |   | GUI-based running log search | Allows you to search running logs through a GUI on the Log Center. |
| Multi- architecture support | Hybrid deployment across chips | Support for hybrid deployment of x86 and Arm architectures | Supports hybrid deployment of instances on multiple chip architectures, such as Intel, Hygon, and Kunpeng. |
