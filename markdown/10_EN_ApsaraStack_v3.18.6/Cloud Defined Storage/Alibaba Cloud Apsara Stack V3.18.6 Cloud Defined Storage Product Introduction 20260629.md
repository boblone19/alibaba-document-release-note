---
title: "Cloud Defined Storage Product Introduction 20260629"
product_version: "V3.18.6"
pdf_pages: 37
source_pdf: "b6399df375395deb_Alibaba Cloud Apsara Stack V3.18.6 Cloud Defined Storage Product Introduction 20260629.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/v3.18.6%E7%89%88%E6%9C%AC%E6%96%87%E6%A1%A3/%E4%BA%91%E6%9C%8D%E5%8A%A1%E5%AE%9A%E4%B9%89%E5%AD%98%E5%82%A8/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.6%20Cloud%20Defined%20Storage%20Product%20Introduction%2020260629.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes)
---

# Cloud Defined Storage Product Introduction 20260629

## Table of Contents

- 1 Cloud Defined Storage
  - 1.1 Features
  - 1.2 Benefits
  - 1.3 Scenarios
  - 1.4 Features
    - 1.4.1 Object Storage Service
    - 1.4.2 Elastic Block Storage
    - 1.4.3 Simple Log Service
    - 1.4.4 Hybrid Disaster Recovery

## 1 Cloud Defined Storage

Cloud Defined Storage (CDS) is a distributed file storage system provided by Alibaba Cloud. CDS features high security, high reliability, low cost, centralized management, and elastic resource scaling, which allows efficient data storage and retrieval. Based on Object Storage Service (OSS), Log Service, Apsara File Storage NAS, and Elastic Block Storage (EBS), CDS provides storage for unstructured data such as files, images, and videos, and supports log storage, query, and analysis features. This allows users in different industries to access unstructured data and process massive amounts of logs. CDS is ideal to provide unstructured data storage and log services in big data scenarios such as mobile application and large websites. CDS offers a one-stop storage solution for users in different industries that is cost-effective, secure, and reliable.

### 1.1 Features

**Overview**

Cloud Defined Storage (CDS) is a distributed file system provided by Alibaba Cloud for cloud service-defined storage. CDS provides structured and unstructured data storage, query, and analysis capabilities by deploying services such as Elastic Block Storage (EBS), Object Storage Service (OSS), Simple Log Service, and Tablestore. It provides cost-effective, secure, and reliable integrated storage solutions for enterprises in different fields. The following figure shows the product architecture. You can deploy services such as OSS and Simple Log Service in storage clusters of CDS. The features supported by a storage cluster vary based on the service that you deployed in the cluster. The following table describes the differences among different storage services.

| Service | Description | Scenario |
|---|---|---|

| EBS | A high-performance and low-latency block-level storage service provided by Alibaba Cloud for Elastic Compute Service (ECS) instances. EBS supports random read and write operations. You can format an EBS device and create file systems on the device in the same way as you do with a physical disk. | EBS can meet the data storage requirements of most business scenarios. |
|---|---|---|
| OSS | A storage service designed to store large amounts of unstructured data such as images, audio, and videos on the Internet. You can call API operations to access data in OSS. | OSS is suitable for scenarios such as website construction and separation of dynamic and static resources. |
| Simple Log Service | Simple Log Service allows you to collect, transform, store, query, analyze, visualize, consume, and ship log data. Simple Log Service also allows you to configure alerts. | It is applicable to the following scenarios: data collection, real-time computing, data warehousing and offline analysis, product operations and analysis, O&M, and management. |

**OSS**

OSS is a secure, cost-effective, and highly reliable cloud storage service provided by Alibaba Cloud. It adopts technologies such as triplicate storage, Erasure Coding (EC), and version control and supports comprehensive capabilities including permission management, disaster recovery and backup, data encryption, and data processing. It features high reliability, robust security, and cost-effectiveness. OSS is suitable for scenarios that require the storage of massive unstructured data such as documents, audio files, videos, and images, offline data storage, and cross-region disaster recovery of data.

**EBS**

EBS is a persistent random block storage service designed for ECS. EBS provides low latency and high reliability. EBS provides devices based on a distributed storage architecture. EBS provides ECS instances with block-level storage that features low latency, high durability, and high reliability. EBS devices use the EC mechanism to ensure data reliability for ECS instances. You can create, release, and resize EBS devices based on your business requirements. EBS supports cloud disks. Cloud disks are block-level storage devices designed for ECS instances. Cloud disks are classified by performance into the following types: premium performance disks, standard performance disks, ultra disks, and standard SSDs.

**Simple Log Service**

Simple Log Service is an end-to-end data logging service that is developed by Alibaba Cloud. It is tested and verified by Alibaba Group in various big data scenarios. It provides a platform on which you can use various features to process large amounts of data at low cost and in real time. The types of data that you can process include logs, metrics, and traces. You can use Simple Log Service to collect, process, consume, query, and analyze log data without the need to invest in in-house data collection or processing systems. Simple Log Service helps improve O&M efficiency and allows you to process large amounts of data.

**Hybrid Disaster Recovery**

The following section introduces the Hybrid Disaster Recovery service: Positioning Disaster recovery at the application level for business continuity: In the case of data center failure or long-time system maintenance, Hybrid Disaster Recovery allows you to quickly run applications on the cloud. This shortens the service interruption period and reduces losses. You can use the server replication feature of Hybrid Disaster Recovery to implement cross-zone disaster recovery protection for ECS instances so that you do not need to create servers again on the cloud. Hybrid Disaster Recovery provides a high-standard disaster recovery solution for key enterprise applications. It features disaster recovery with a recovery point objective (RPO) of a few minutes and a recovery time objective (RTO) of a few minutes.

### 1.2 Benefits

Cloud Defined Storage (CDS) provides flexible deployment, high performance, and high reliability. When different cloud services are deployed in CDS, CDS inherits the benefits of the cloud services.

**Overall advantages**

**Flexible deployment**

CDS provides storage based on cloud services and allows you to deploy cloud services together or independently. In addition, CDS supports dynamic and flexible resource scaling.

**High performance**

CDS can integrate resources such as CPU resources and hard disk resources on all storage nodes, and distribute data storage and process tasks in real time in a dynamic and balanced manner. This helps implement concurrent data processing, prevents issues caused by single points of failure (SPOFs), and improves the processing capabilities of clusters. The performance of CDS storage clusters can be easily improved to meet the growing storage requirements for applications.

**High reliability**

CDS storage clusters use the erasure coding (EC) mechanism to store data as data blocks on different servers in different racks. If a data block error occurs, you can easily restore the data block.

**High availability**

CDS storage clusters use fully redundant architectures to prevent issues caused by SPOFs. In addition, CDS provides automatic failure detection and data migration features to shield applications from server-related and network-related hardware faults. This ensures the high availability of applications. The EC mechanism used by storage clusters ensures proper data redundancy and improves space utilization.

**High scalability**

CDS improves the service capability of a storage cluster by using various methods, such as expanding the cluster, adding and upgrading server hardware in the cluster, and adding storage nodes to the cluster. CDS storage clusters support smooth online upgrades and hot upgrades, and allow you to dynamically add or remove storage nodes. In addition, the storage clusters support automatic data migration and do not require shutdown maintenance.

**Access security**

CDS provides multiple permission management mechanisms, and authenticates each request from applications to prevent unauthorized access. This ensures data security.

**Easy management**

CDS frees you from complex O&M tasks, such as data partition management, software and hardware upgrades, configuration updates, and cluster scale-outs. CDS allows you to store audit logs to Simple Log Service and download logs from Simple Log Service. This facilitates the long-term storage and management of audit logs. The centralized O&M platform CDS Ops supports daily O&M operations on storage clusters and cloud services that are deployed in the storage clusters, such as Object Storage Service (OSS), Simple Log Service, and Elastic Block Storage (EBS).

**Advantages of OSS**

**Advantages of OSS over self-managed storage**

| Item | OSS | Self-managed server storage |
|---|---|---|
| Reliability | Provides automatic backup for redundancy. Tolerates faults at the hard disk, node, rack, and cluster levels. Read and write operations are not interrupted in the event of failures of up to two nodes. This ensures business continuity. | Is prone to errors due to low hardware reliability. If a disk has a bad sector, data may be irreversibly lost. Requires manual data restoration, which can be complex, time- consuming, and labor-intensive. |
| Security | Provides multi-level security protection for enterprises. Provides resource isolation mechanisms for multiple tenants. Provides various authentication and authorization mechanisms. It also provides features such as whitelists, hotlink protection, Resource Access Management (RAM), and Security Token Service (STS) for temporary access. | Requires a separate security mechanism. |
| Data processing | Provides Image Processing (IMG). | Requires independent purchase and deployment of data processing capabilities. |

**Other advantages of OSS**

Ease of use OSS provides standard RESTful API operations, some of which are compatible with Amazon S3 API operations, a wide range of SDKs, client tools, and the OSS console. You can use any one of these options to upload, download, query, and manage large amounts of data used in your apps and websites in the same way you would with regular file systems. OSS supports streaming writes and reads. It is suitable for business scenarios that require simultaneous write and read of large files such as videos. OSS supports lifecycle management. You can configure lifecycle rules to delete expired objects in batches. OSS provides plenty of storage space that is also scalable. You can add nodes to increase your storage space. A single bucket can contain trillions of objects. Powerful and flexible security mechanisms OSS provides STS and URL-based authentication and authorization mechanisms, allowlists, hotlink protection, and RAM. Rich image processing features OSS supports the conversion between formats such as JPG, PNG, BMP, GIF, WebP, and TIFF. OSS also supports various of operations on image objects, such as thumbnails, cropping, watermarking, and resizing.

**Advantages of EBS**

EBS provides devices based on a distributed storage architecture. EBS provides ECS instances with block-level storage that features low latency, high durability, and high reliability. EBS devices use the EC mechanism to ensure data reliability for ECS instances. You can create, release, and resize EBS devices based on your business requirements.

**High performance**

The self-developed user-mode TCP stack that supports a single write latency of 100 microseconds is used. The self-developed user-mode file system is used to further improve SSD performance.

**High reliability**

If a single disk node fails, the service remains uninterrupted. If multiple disk nodes fail, no data is lost. This ensures service stability. Disaster recovery is implemented based on in-cloud data replication and cross-cloud data replication.

**High availability**

You can resize EBS devices, including system and data disks, without interrupting your business. When you resize an EBS device, you do not need to stop the Elastic Compute Service (ECS) instance to which the EBS device is attached or detach the EBS device from the ECS instance. Cloud disks are hot migrated across clusters without affecting services.

**Security**

Disk encryption is supported, and the integrity of snapshots and images is ensured based on encryption algorithms. The full-link cyclic redundancy check (CRC) feature is used to prevent underlying hardware failures.

**Advantages of Tablestore**

**Scalability**

Tablestore does not impose any limits on the amount of data that can be stored in tables. As data increases, Tablestore adjusts data partitions to provide more storage space for tables and improve the capability of handling sudden spikes of access requests. Tablestore supports CPUs, disks, memory, and network interface controllers (NICs) of different specifications in a single-component cluster provided that the cluster performance is not affected. This ensures maximum compatibility with existing devices.

**High performance**

High-performance Tablestore instances provide single-digit millisecond latency when you access single rows of data. The read/write performance is not affected by the size of data in a table.

**Data reliability**

Tablestore provides high data reliability. It stores multiple copies of data and restores data if any of the copies are damaged. Tablestore supports automatic fault tolerance for server disk failures in a cluster and supports hot swapping of disks. In the event of a disk failure, services can be restored within a minute. Tablestore supports full and incremental backup and data restoration from storage. Tablestore supports the backup between data clusters in different data centers. You can view and manage the backup process. Tablestore supports the backup and restoration of the metadata, files, and tables of key components.

**High availability**

Tablestore uses automatic failure detection and data migration to shield applications from host- and network-related hardware faults. This provides high availability for your applications.

**Access security**

Tablestore provides multiple permission management mechanisms. It verifies and authenticates the identity of each application request to prevent unauthorized data access, which improves data security. Tablestore supports the management of data access permissions, including logon permissions, table creation permissions, read and write permissions, and whitelist-related permissions. Tablestore allows you to use the Apsara Uni-manager Management Console to manage administrative permissions, including administrator classification. You can use the console to manage user permissions in a centralized manner. You can manage the access control features of all components in the system. You can also block regular users from querying access control details and simplify access control for administrators. This improves the usability of access control.

**Strong consistency**

Tablestore ensures high data consistency for data writes. After a write operation succeeds, three replicas are written to a disk. Applications can read the latest data immediately.

**Flexible data models**

Tablestore tables do not require a rigid schema. Each row can contain a different number of columns. Tablestore supports multiple data types, including Integer, Boolean, Double, String, and Binary.

**Powerful data indexing capabilities**

Tablestore provides powerful data query features, such as primary key-based queries, secondary index-based queries, and search index-based queries. Secondary index: defines a custom data structure that can be used to improve query efficiency based on your business requirements. Search index: supports query methods such as boolean queries, fuzzy queries, geo queries, and full-text searches based on inverted indexes and column-oriented storage.

**Monitoring service integration**

You can log on to the Tablestore console to obtain monitoring information in real time, including the number of requests per second and the average response latency.

**Multi-tenant management**

Isolation: allows tasks of multiple tenants to be submitted to different queues and run separately. Resources are isolated among tenants. Permission: allows you to manage tenants in a centralized manner, dynamically configure and manage tenant resources, isolate resources, view statistics for resource usage, and manage tenants at multiple levels in the console. Scheduling: supports multi-tenant scheduling of multiple clusters and multiple resource pools.

**Advantages of Simple Log Service**

**Fully managed service**

Log Service is easy to access and easy to use. LogHub provides all features of Kafka, provides monitoring and alerting data, and supports auto scaling (by petabytes per day). LogSearch/Analytics provides the saved search feature, and allows you to view log data on dashboards and configure alerts. Log Service provides more than 30 access methods to connect to open source software, such as Storm and Spark Streaming.

**Comprehensive ecosystem**

LogHub supports more than 30 types of data sources, including embedded devices, web pages, servers, and programs. LogHub can connect to different consumption systems, such as Storm and Spark Streaming. LogSearch/Analytics supports complete query and analysis syntax and is compatible with SQL-92 syntax. Log Service can be connected to Grafana by using Java Database Connectivity (JDBC).

**Real-time response**

LogHub: Data can be immediately consumed after the data is written to Log Service. Logtail is used as an agent to collect and send data to Log Service in real time. LogSearch/Analytics: Data can be queried 3 seconds after the data is written to Log Service. If you specify multiple conditions to query data from hundred billions of data records, the result can be returned in seconds.

**High throughput**

Log Service provides high throughput after Log Service software is optimized. If Log Service is deployed on a single server, the throughput performance can reach the following levels: Data write: Raw logs can be written to Simple Log Service at a speed that exceeds 400 MB/s, and indexed logs can be written to Simple Log Service at a speed that exceeds 150 MB/s. Real-time consumption: Data can be consumed in real time at a speed that exceeds 400 MB/s. QPS: The queries per second (QPS) can exceed 10,000. Original query: If you set five or more query conditions for hundreds of billions of data records, 100 data entries that meet the query conditions are returned within 10 seconds. Real-time analysis: Billions of data records are returned within seconds. If you set five or more query conditions for tens of billions of data records, the data is returned within 5 seconds.

> **Note:** The throughput performance varies based on the hardware of a server.

**Scalability**

Simple Log Service provides flexible scaling capabilities to process petabytes of data.

**HDR**

**Ease of use**

Disaster recovery sites can be deployed and managed in the console with ease. Failover and disaster recovery drills can be performed at any time and can be quickly cleared.

**Tiered RPO and RTO goals**

Enterprises can develop tiered recovery point objective (RPO) and recovery time objective (RTO) goals for applications with different importance weights. Actual disaster recovery metrics depend on the infrastructure of enterprises, especially network conditions. HDR provides RPOs and RTOs in minutes based on the disk-level data replication technology.

**Cross-zone disaster recovery**

HDR supports efficient data replication and disaster recovery for application servers that run Windows and Linux. Cross-zone disaster recovery for applications can be implemented. You can run scheduled backup jobs and restore jobs only for data of critical applications such as SQL Server databases and Oracle databases to implement cross-zone disaster recovery.

**Cross-cloud disaster recovery**

Cross-cloud disaster recovery indicates the scenario where the production and disaster recovery clouds are two cloud instances deployed in different regions. If a fault occurs on the production cloud, your business system is switched to the disaster recovery cloud. This effectively prevents system failures caused by exceptions on the cloud instances, ensures business availability, and meets the RPO and RTO goals of your business.

### 1.3 Scenarios

Cloud Defined Storage (CDS) can provide one-stop storage solutions for enterprises in different industries in a cost-efficient, secure, and reliable manner. Enterprises can deploy different services in CDS to meet requirements in different scenarios.

**OSS**

**High storage capacity for image, audio, and video applications**

**Offline data storage**

OSS is a cost-effective storage service that provides high data availability. You can use OSS to store on-premises data that you want to archive for long-term use.

**Cross-region disaster recovery of data**

You can use cross-region replication or cross-cloud replication to asynchronously replicate your data between two regions or clouds. This way, you can build a storage architecture with three data centers across two zones and store your data in different regions for backup and disaster recovery. This ensures the continuity of your business even in case of severe disaster events.

**EBS**

Elastic Block Storage (EBS) is a persistent random block storage service that provides low latency and high reliability and is designed for Elastic Compute Service (ECS). EBS provides devices based on a distributed storage architecture. EBS devices are classified into the following types based on whether they can be attached to multiple ECS instances: disks and shared disks.

**Disks**

Disks are classified by performance into the following types: premium performance disks, standard performance disks, ultra disks, and standard SSDs. Standard performance disks and premium performance disks are ideal for online transaction processing (OLTP) databases (such as MySQL, PostgreSQL, Oracle, and SQL Server), NoSQL databases (such as MongoDB, HBase, and Cassandra), and Elasticsearch, Logstash, and Kibana (ELK) distributed logs. Premium performance disks deliver up to 25,000 random IOPS for ECS instances. Ultra disks are ideal for medium I/O load scenarios and deliver up to 3,000 random IOPS for ECS instances. Ultra disks can be used as system disks of ECS instances. Standard SSDs are ideal for I/O-intensive applications and deliver stable and high random IOPS performance. Standard SSDs can be used in small and medium-sized development and test environments that require high data reliability.

**Simple Log Service**

Simple Log Service is applicable to the following scenarios: data collection, real-time computing, data warehousing and offline analysis, product operation and analysis, O&M, and management.

**Data collection and consumption**

You can use the LogHub module of Simple Log Service to collect large amounts of log data in real time. The log data can be metrics, events, binary logs, text logs, and clickstream data. Easy to use: More than 30 real-time data collection methods are provided for you to quickly set up your platform and reduce O&M workload. Automatically scalable: Log Service scales based on traffic and business requirements, helping you handle traffic spikes and respond to growing business demands.

**ETL and stream processing**

You can connect LogHub to multiple real-time computing engines and services. LogHub can monitor the processing progress and generate alerts based on the monitoring results. You can also use SDKs or call API operations to consume logs. Easy operations: LogHub provides SDKs in multiple programming languages and programming frameworks. It can interconnect with various stream computing engines. Comprehensive features: LogHub supports alert mechanisms and provides large amounts of monitoring data. Elastic scaling: PB-grade elasticity and zero latency.

**Real-time query and analysis**

The LogAnalytics module allows you to index LogHub data in real time and query data by using keywords, fuzzy match, context, or SQL aggregate functions. You can also query data within the specified range. Strong real-timeliness: Data can be queried immediately after it is written. High efficiency at low cost: LogSearch/Analytics is able to index PBs of data each day. Costs are 85% lower compared with self-built systems. Strong analysis capability: LogSearch/Analytics supports multiple query methods and SQL for aggregation analysis. It also provides visualization and alerting capabilities.

**HDR**

**Cross-zone disaster recovery**

Hybrid Disaster Recovery (HDR) supports cross-zone disaster recovery to meet various business requirements. If a fault occurs at the production site, the business system is switched to the disaster recovery site. This effectively prevents system failures caused by regional disasters, ensures business availability, and meets the recovery point objective (RPO) and recovery time objective (RTO) goals of your business.

**Cross-cloud disaster recovery**

HDR supports cross-cloud disaster recovery. Cross-cloud disaster recovery indicates the scenario in which the primary and secondary clouds are two cloud instances deployed in different regions. If a fault occurs on the primary cloud, the business system is switched to the secondary cloud. This effectively prevents system failures caused by errors in cloud instances, ensures business availability, and meets the RPO and RTO goals of your business.

### 1.4 Features

#### 1.4.1 Object Storage Service

This topic describes features of Object Storage Service (OSS).

**Bucket management**

| Feature | Description |
|---|---|
| Create a bucket | A bucket is a container for storing objects. All objects must be stored in a specific bucket. You can configure various bucket attributes, such as the region, access control list (ACL), and storage class. You can create buckets to store data based on your business requirements. |
| Delete a bucket | You can delete an empty bucket that contains no objects. Warning Deleted buckets cannot be recovered. Proceed with caution. |

| Access Control List (ACL) | You can set the ACL of a bucket when you create a bucket or modify the ACL after bucket creation based on your business requirements. Only the bucket owner can perform this operation. Available access permissions include: public-read-write: Anyone, including anonymous users, can read from and write to objects in the bucket. Warning Any user on the Internet can access objects in this bucket and write data to it. This may lead to data leakage. If malicious users write illegal content, it may infringe upon your legitimate rights and interests. We strongly recommend against setting this permission unless required for specific scenarios. public-read: Only the bucket owner can write to objects in this bucket. Anyone, including anonymous users, can read objects in this bucket. Warning Any user on the Internet can access objects in this bucket. This may lead to data leakage. Set this permission with caution. private: Only the bucket owner can read from and write to objects in this bucket. |
|---|---|
| Static website hosting | You can use the static website hosting feature to host your static website on an OSS bucket and access the website using the bucket's endpoint. The default homepage is the website's landing page (equivalent to index.html) returned by OSS when users access the static website domain via a browser. The object specified as the default homepage must reside in the bucket's root directory, allow anonymous access, and be in HTML format. The default 404 page is the error page returned by OSS when a 404 error occurs while accessing an object in the bucketvia a browser. The object specified as the default 404 page must reside in the bucket's root directory, allow anonymous access, and be in HTML, JPG, PNG, BMP, or WebP format. |
| Capacity management | When you create a bucket, you can set a maximum capacity limit for it. You can modify the bucket's capacity limit through the console. |
| Log transfer | Accessing OSS generates a large volume of access logs. You can use the log transfer feature to generate log files hourly based on a fixed naming convention and write them to a bucket you specify. You can analyze stored logs using Alibaba Cloud Simple Log Service or by setting up a Spark cluster. |

| Lifecycle management | Lifecycle rules allow you to automatically delete infrequently accessed or obsolete data, helping you manage stored data more efficiently and save significant labor and storage costs. For example, if you need to delete a large number of objects in a bucket, manually deleting them (up to 1,000 objects per operation) can be cumbersome. In this case, you can configure a lifecycle rule that applies to the entire bucket and sets all objects to delete after one day. All data in the bucket will then be deleted the next day. |
|---|---|
| Bucket tagging | You can use bucket tags to classify and manage buckets, such as listing buckets with specific tags or setting access permissions for buckets with specific tags. |
| Hotlink protection | OSS supports hotlink protection based on the Referer field in HTTP and HTTPS headers. You can configure allowlists, blocklists, and whether empty Referers are allowed. When a browser sends a request to OSS, the request header includes a Referer field that tells OSS the source page of the request. If hotlink protection is configured, OSS checks the request's Referer against the configured Referer rules to determine whether to allow the request: If the Referer in the request matches an entry in the allowlist, OSS allows the request. If the Referer in the request matches an entry in the blocklist, or does not match any entry in the allowlist, OSS denies the request. If empty Referers are not allowed, only requests containing a Referer field in their HTTP or HTTPS headers can access OSS resources. |
| Retention policy (WORM) | OSS retention policies feature Write Once Read Many (WORM) compliance, enabling you to store and use data in an immutable and undeletable manner. If you want to prevent any user, including the resource owner, from modifying or deleting objects in a specific bucket for a defined period, you can configure a retention policy for that bucket. Before the retention period expires, users can only upload and read objects in the bucket. After the retention period expires, users can modify or delete objects. |
| Cross-Origin Resource Sharing (CORS) | OSS provides CORS settings based on the HTML5 protocol to help you enable cross-origin access. When OSS receives a cross-origin request (or an OPTIONS request), it reads the CORS rules associated with the bucket and performs the corresponding permission checks. OSS evaluates each rule in sequence and uses the first matching rule to allow the request and return the corresponding headers. If no rules match, OSS does not attach any CORS-related headers. |
| Inventory | You can use an API to retrieve information such as the count, size, and storage class of specified objects in a bucket. |

| Back-to-origin rules | Back-to-origin rules support two types: mirroring and redirection, which can meet your needs for data hot migration and redirecting specific requests. Mirroring back-to-origin After you configure mirroring back-to-origin, when a user performs a GET operation on a non-existent object in OSS, OSS requests the object from the address specified in the back-to-origin rule. After obtaining the target object, OSS returns it to the user and writes the object to OSS. Mirroring back-to-origin is primarily used for seamless data migration to OSS. For example, when your service is already running on your own origin server or another cloud product and you need to migrate to OSS without service interruption, you can use this feature. Redirection After you configure redirection, when a user performs a GET operation on a non-existent object in OSS, OSS redirects the user's request to the address specified in the back-to-origin rule to retrieve the target object. You can use this redirection feature to redirect object and implement various related business scenarios. |
|---|---|
| Access using a custom domain name | After you upload an object to a bucket, OSS automatically generates a URL for the object. You can directly access the object using this URL. If you want to access these objects using a custom domain name (your own domain), you must bind the custom domain name to the bucket where the objects reside. |

**Object management**

| Feature | Description |
|---|---|
| Upload objects | An object is the basic unit for storing data in OSS, and is also known as a file in OSS. You can select an appropriate upload method based on the file size and network conditions. OSS provides the following upload methods: Simple upload: includes streaming upload and file upload. The maximum file size is 5 GiB. Form upload: The maximum file size is 5 GiB. Append upload: The maximum file size is 5 GiB. Resumable upload: supports concurrent uploads, resumable uploads, and custom part sizes. We recommend that you use resumable uploads for large files. The maximum file size is 48.8 TiB. Multipart upload: used for uploading large files. The maximum file size is 48.8 TiB. During upload, you can configure object metadata and view the upload progress by using a progress bar. After the upload is completed, you can configure an upload callback. |

| Delete objects | You can delete objects by using the following methods: Delete objects on the console. Automatically delete objects based on lifecycle management policies. Delete objects by using SDKs or APIs. Delete objects by using tools such as ossutil. Warning Deleted objects cannot be recovered. Proceed with caution. |
|---|---|
| ACL | OSS provides object-level ACLs to control access permissions on objects. You can configure ACLs when you upload objects or modify ACLs after the upload. If you do not configure an ACL, the default value is inherited from the bucket. Available access permissions include: Inherit from bucket: The read/write permissions on objects follow the read/write permissions of the bucket. Private: Only the object owner can read from and write to the object. Other users cannot access the object. Public read: Only the object owner can write to the object. Anyone, including anonymous users, can read the object. Public read/write: Anyone, including anonymous users, can read from and write to the object. Use this permission with caution. |
| Download objects | OSS provides various object download methods. You can select an appropriate method to download files stored in buckets. The following download methods are supported: Download to local files: Download objects in buckets to your local device. Streaming download: Download a large object or an object that takes a long time to download, by processing it in parts until the entire object is downloaded. Range download: Download only a specific range of data from an object when you need only a portion of the data. Resumable download: Download a large object by splitting it into multiple parts and downloading each part separately. If the network is unstable or the program exits unexpectedly during the download, the process can be resumed. After all parts are downloaded, they are merged into a complete object. Conditional download: Download objects only if one or more specified conditions are met. If the conditions are not met, OSS returns an error and does not download the objects. |
| Manage objects | OSS allows you to quickly search for and locate target objects by specifying filename prefixes. You can create directories to organize and store objects. |

| Object tagging | Object tagging uses key-value pairs to tag objects. You can add tags when you upload objects or add tags to existing objects to achieve the following: Configure lifecycle rules for objects with the same tags. Manage permissions on objects with specified tags by using Resource Access Management (RAM) policies. |
|---|---|

**Data security**

| Feature | Description |
|---|---|
| Triplicate | The system replicates each data chunk into three identical replicas and stores these replicas on different nodes in the cluster based on a specific strategy. This ensures that even if a node fails, the data can still be recovered from other nodes. |
| Erasure coding (EC) | The system splits raw data into multiple data chunks and generates a specific number of parity chunks through calculation. These data chunks and parity chunks form an EC group and are distributed across different storage nodes. If some data chunks or parity chunks are lost, the system can recover the lost data from the remaining chunks. EC involves two concepts: data chunks (N) and parity chunks (M): Data chunks (N): The data is split into N data slices. Parity chunks (M): The system calculates M parity chunks from N data chunks. Data chunks (N) and parity chunks (M) form an EC group and are stored on different servers. The system can recover any lost chunks by using the EC algorithm as long as the number of lost chunks is less than or equal to M. You can configure N+M. For Apsara Stack, we recommend an 8+3 configuration (depending on the number of deployed cluster nodes). You can modify EC policies online. |
| Resource isolation | OSS authenticates users using AccessKey pairs based on symmetric key authentication. The system verifies the signature of each HTTP request. After successful authentication, the system reassembles the user's discretely stored data to achieve data isolation among multiple tenants. |

| Disaster recovery and backup | Zone- disaster recovery | Zone-disaster recovery redundantly stores your data across multiple Availability Zones (AZs) within the same region. This minimizes data loss during single-AZ failures and helps you quickly restore services. OSS provides two zone-disaster recovery solutions. Details are as follows: Two-AZ disaster recovery: After you enable zone- disaster recovery for a bucket, OSS synchronizes the data from buckets in the primary data center to backup buckets in the OSS cluster in the standby data center. If the primary data center experiences a complete failure (such as power outage or fire), data access remains available. To address the growing demands for high traffic and concurrency while ensuring high availability and disaster recovery capabilities, OSS allows you to deploy multiple independent two-zone disaster recovery clusters within the same region. These clusters work together to handle business traffic, enabling elastic resource scaling and risk isolation. Three-AZ disaster recovery: After you create a bucket with zone-redundant storage, your data is redundantly stored across three independent AZs within the same region. This ensures that if one AZ becomes unavailable due to network disconnection, power outage, or disaster, the other two AZs continue to provide services, guaranteeing business continuity and data security. When an AZ fails, OSS still provides strong consistency services. The failover process is transparent to users, ensuring no data loss and meeting the stringent requirements of critical business systems for a Recovery Point Objective (RPO) of 0 and a Recovery Time Objective (RTO) approaching 0. |
|---|---|---|
|   | Cross- region replication | Cross-region replication automatically and asynchronously (near real-time) replicates objects across buckets in different OSS data centers (regions). It replicates operations such as object creation, update, and deletion from a source bucket to a destination bucket in a different region. |
|   | Cross-cloud replication | Cross-cloud replication allows you to replicate data from one cloud system to another, helping you back up data across different cloud systems. If a cloud system fails, you can directly switch your business to another cloud system to ensure business continuity. |

| Security control and account authorization | RAM policy | RAM is a resource access control service provided by Alibaba Cloud. RAM policies are user-based authorization policies. By configuring RAM policies, you can centrally manage users (such as employees, systems, or applications) and control which resources under your cloud account they can access. For example, you can restrict other users to read-only access to a specific bucket. |
|---|---|---|
|   | Bucket policy | Bucket policy: Bucket policies are resource-based authorization policies. Compared with RAM policies, bucket policies are easier to configure. They support graphical configuration on the console and allow bucket owners to directly grant access permissions without requiring RAM operation permissions. Bucket policies can be used to grant access permissions to RAM users of other accounts and to anonymous users with specific IP condition restrictions. Bucket ACL: You can set ACL for a bucket when creating it, or modify the ACL at any time after creation based on your business needs. Only the bucket owner can perform this operation. Bucket ACLs include public-read- write, public-read, and private. Hotlink protection: OSS allows you to configure hotlink protection for buckets by setting up a whitelist mechanism for access sources. This prevents others from stealing your OSS resources. |
|   | Object ACL | In addition to bucket-level ACLs, OSS also provides object- level ACLs. You can set the ACL when uploading an object, or modify it at any time after the upload based on your business needs. Object ACLs include inherit from bucket, public-read-write, public-read, and private. |
|   | Server-side encryption | OSS provides static data protection through server-side encryption. This is suitable for scenarios with high security or compliance requirements for file storage, such as storing deep learning sample files or online collaborative documents. |

|   | Client-side encryption | When you use client-side encryption, the system generates a random data encryption key for each object and uses the plaintext of this key to symmetrically encrypt the object's data. The master key is used to generate the random data encryption key, and the encrypted content is saved as the object's metadata on the server. During decryption, the system first uses the master key to decrypt the encrypted random key, then uses the decrypted plaintext of the random data encryption key to decrypt the object's data. The master key participates only in local client computations and is neither transmitted over the network nor stored on the server, ensuring the security of the master key. Warning When using client-side encryption, you are responsible for the integrity and correctness of the master key. Any losses or consequences caused by improper maintenance leading to incorrect or lost master keys, resulting in the inability to decrypt encrypted data, are borne by you. When copying or migrating encrypted data, you are responsible for the integrity and correctness of the encryption metadata. Any losses or consequences caused by improper maintenance leading to errors or loss of encryption metadata, resulting in the inability to decrypt encrypted data, are borne by you. |
|---|---|---|
| Encryption |   |   |
|   | Transport Layer Security (TLS) | Client applications communicate with OSS over Transport Layer Security (TLS) encryption. TLS is a standard encryption protocol that ensures privacy and data integrity for communication between clients and servers over the Internet. You can configure the TLS version on the OSS server. After the configuration, clients can only use the specified TLS version to send and receive data with OSS, meeting the security requirements of the communication link. |

| Versioning | Versioning is a bucket-level data protection feature. After you enable versioning, overwrite and delete operations on data are saved as historical versions. If you accidentally overwrite or delete an object, you can restore the object stored in the bucket to any historical version. |
|---|---|

**Data processing**

| Feature | Description |
|---|---|
| Source image protection | After you enable source image protection, direct access to the original OSS objects or access that modifies image styles by passing image parameters is disabled. |
| Image processing rules | You can configure multiple style processing rules. |
| Image effect processing | Use the graphical interface to adjust image brightness, contrast, sharpness, blur, and rotation. |
| Image style | A single style contains multiple image processing parameters, enabling you to quickly perform complex image processing operations. |
| Image scaling | Select from no scaling, proportional scaling down, proportional scaling up, or scaling to a specified width and height as needed. |
| Gradual display | You can enable this mode that starts blurry and becomes clear. This feature applies only to images in the JPG format. |
| Auto-rotate | This feature rotates images based on EXIF orientation information before performing thumbnail generation. |
| Format conversion | This feature converts images to different formats. You can select from the original format, JPG, JPEG, PNG, BMP, GIF, WebP, or TIFF as needed. |
| Image quality | Select relative quality, absolute quality, or no compression as needed. |
| Image watermark | Select no watermark, image watermark, or text watermark as needed. |
| Video frame capture | Use SDKs or add frame capture parameters to URLs toe xtract video frames and convert them into the required image formats. |

**Scalability**

| Feature | Description |
|---|---|

| Cloud Storage Gateway (CSG) | The file gateway maps the object structure of an OSS bucket to the directory and file structure of a NAS file system. Users can read and write objects in a specified OSS bucket by using standard Network File System (NFS) and Server Message Block (SMB) protocols. The gateway uses local storage as a hot data cache, which ensures high-performance data access while allowing users to benefit from the massive capacity of OSS buckets. |
|---|---|
| Cluster scaling | The cluster scale (including control and data nodes) supports horizontal scaling. A single cluster can scale to hundreds of petabytes while maintaining linear performance scaling. |

**Reliability description**

For an EC configuration with N data chunks and M parity chunks, the chunks form an EC group. The reliability varies depending on the cluster size, as described below: When the cluster contains N+M+M or more nodes, it can tolerate the simultaneous failure of two devices without data loss. It can also tolerate the failure of one device without data loss or service interruption. When the cluster contains fewer than N+M+M nodes, EC folding may occur within the cluster. In this case, the cluster can tolerate the failure of only one device without data loss or service interruption. It cannot guarantee that data will be preserved if two devices fail simultaneously.

**Tools and compatibility**

| Feature | Description | Supported version |
|---|---|---|
| Tool | ossbrowser graphical management tool | ossbrowser 2.0 |
|   | ossfs object-to-file system tool for NFS and CIFS | ossfs 1.91.4 |
|   | ossftp object-to-FTP tool | ossftp 1.2.0 |
|   | ossutil command-line tool | ossutil 2.0 |
| SDK support | Java | Version 3.17.4 and earlier |
|   | Python | Version 2.18.3 and earlier |
|   | PHP | Version 2.0.0 and earlier |
|   | C | Version 3.11.2 and earlier |
| 4 | > Document Version: 2026062 |   |

|   | Go | Version 3.0.2 and earlier |
|---|---|---|

**Deployment requirements**

In non-disaster recovery scenarios, an OSS cluster requires at least six nodes for deployment. In zone-disaster recovery scenarios, the number of nodes required for OSS cluster deployment depends on the disaster recovery solution used. Two-AZ disaster recovery: Deploy the OSS cluster across two AZs. Each AZ must contain at least six nodes, and the number of nodes in both AZs must be identical. Three-AZdisaster recovery: The OSS three-AZ cluster cannot be the primary cluster. You can deploy an additional three-AZ disaster recovery cluster only if a zone-disaster recovery cluster already exists in the same cloud. The OSS three-AZ cluster requires at least 21 nodes for deployment. Each AZ must contain at least seven nodes, and the number of nodes in all three AZs must be identical.

#### 1.4.2 Elastic Block Storage

This topic describes the features of Elastic Block Storage (EBS).

**Cloud disk management**

| Feature | Description |
|---|---|
| Create a cloud disk | You can create a cloud disk separately to increase the storage space of an Elastic Compute Service (ECS) instance. Cloud disks include premium performance disks, standard performance disks, ultra disks, and standard SSDs based on their performance. |
| Attach a cloud disk | You can attach a separately created cloud disk to an ECS instance in the same region and zone as a data disk. |
| Detach a cloud disk | You can detach a data disk from an ECS instance when the instance no longer needs the data disk. You can also detach a data disk from an ECS instance and then attach the data disk to another ECS instance in the same zone. |
| Release a cloud disk | If you no longer need a data disk, you can manually release it. All data stored on the cloud disk is released. You can also temporarily store the released cloud disk in the recycle bin. Within the retention period configured for the recycle bin, you can restore the cloud disk from the recycle bin. |
| Batch attach or detach cloud disks | You can attach multiple cloud disks to the same ECS instance at a time. You can also detach multiple cloud disks from the same ECS instance at a time. |

| Reinitialize a cloud disk | You can reinitialize a cloud disk to restore it to its initial state when it was created. Important After a cloud disk is reinitialized, the data stored on the cloud disk is lost and cannot be recovered. Exercise caution when you perform this operation. If you still need the data on the cloud disk, transfer the data or create a snapshot in advance. |
|---|---|
| Clone a cloud disk | You can use cloud disk cloning to quickly create a replica of an existing cloud disk. |
| Expand cloud disk | As your business grows and application data increases, you can resize your cloud disks to store more data. You can resize both system disks and data disks online. For online resizing, changes take effect immediately without requiring a restart of the ECS instance. For offline resizing, after resizing a cloud disk offline, you must restart the associated ECS instance on the ECS console or by calling the RebootInstance operation for the new capacity to take effect. |
| Hot reconfigure a cloud disk | When an ECS instance is running, you can change its cloud disk type online, without stopping the instance or detaching the cloud disk. This feature is suitable for scenarios where you need to flexibly scale the storage capability. The following cloud disk reconfiguration operations are supported. Downgrading and other reconfiguration operations are not supported. Ultra disks: can be reconfigured to standard SSDs, standard performance disks, and premium performance disks. Standard SSDs: can be reconfigured to standard SSDs into ultra disks, standard performance disks, and premium performance disks. Premium performance disks: can be reconfigured standard performance disks only. Standard performance disks: can be reconfigured to premium performance disks only. |
| Storage set | You can create a storage set to classify EBS clusters based on dimensions such as the business type, and associate EBS clusters with different partitions in the storage set. This allows you to isolate EBS clusters of different business types. Storage sets can be shared across level-1 organizations. |
| Configure quality of service (QoS) for a cloud disk | You can configure the maximum input/output operations per second (IOPS) and throughput for cloud disks on GUI-based Cloud Defined Storage (CDS)- OPS. |

| Migrate a cloud disk | EBS supports cluster migration and hot migration of cloud disks to meet your diverse requirements for cloud disk-level or cluster-level migration. Cluster migration: allows you to migrate cloud disks in batches from EBS 1.0 or CDS-EBS clusters to CDS-EBS clusters. This feature is suitable for cluster upgrades and resource integration, improving efficiency and reducing operational complexity. Hot migration of cloud disks: allows you to migrate one or more cloud disks online without interrupting your business. You can migrate cloud disks between EBS 1.0 clusters, between EBS 1.0 and CDS-EBS clusters, or between CDS-EBS clusters. This feature meets O&M requirements such as elastic scheduling, fault avoidance, and load balancing. |
|---|---|

**Data security and reliability**

| Feature | Description |
|---|---|
| Triplicate | The system replicates each data chunk into three identical replicas and stores them on different nodes in the cluster based on a specific strategy. This ensures that even if one node fails, the system can recover the data from other nodes. |
| Erasure coding (EC) | The system splits raw data into multiple data chunks and generates a specific number of parity chunks through computation. These data chunks and parity chunks form an EC group and are distributed across different storage nodes. If some data chunks or parity chunks are lost, the system can recover the lost data from the remaining chunks. EC involves two concepts: data chunks (n) and parity chunks (m): Data chunks (n): The system splits data into n data slices. Parity chunks (m): The system calculates m parity chunks from the n data chunks. The data chunks (n) and parity chunks (m) form an EC group and reside on different servers. The system can recover any lost chunks by using the EC algorithm as long as the number of lost chunks is less than or equal to m. You can configure n+m. Apsara Stack recommends an 8+3 configuration, depending on the number of deployed cluster nodes. |
| Modify EC policies online | You can modify EC policies online through the O&M platform. Important After you enable the EC mode, you cannot switch back to the triplicate mode. Proceed with caution. |

| Cloud disk disaster recovery |   | Async replication Asynchronous replication applies to disaster recovery requirements for a group of cloud disks. Async replication uses the EBS data replication capabilities to protect data across zones, regions, or clouds. This feature asynchronously replicates data from one or a group of cloud disks to another cloud disk in a different zone, region, or cloud. If the primary disk fails, you can perform failover and reverse replication from the secondary disk to achieve disaster recovery. Consistent replication group Consistent replication groups apply to disaster recovery requirements for multiple groups of cloud disks. This feature provides unified management and operations for asynchronous replication across multiple cloud disks within a business system. It ensures that all cloud disks in the same replication group can be restored to the exact same point in time, providing reliable multi-disk disaster recovery protection. With a consistent replication group, primary disk data from the production site is asynchronously replicated to secondary disks at the disaster recovery site, either across zones on a cloud or across clouds. If the production site fails, you can perform failover and reverse replication from the disaster recovery site to achieve disaster recovery. |
|---|---|---|
| Cloud disk encryption |   | Cloud disk encryption is designed for scenarios that require data security or regulatory compliance, helping you protect data stored on ECS instances. Both system disks and data disks can be encrypted. Encryption must be enabled during cloud disk creation, and the encryption status cannot be changed after a cloud disk is created. |
| Hot migration for cloud disks |   | By creating a hot migration task for cloud disks, you can quickly migrate cloud disks between EBS clusters without interrupting disk usage. This improves maintenance efficiency and optimizes resource allocation. Currently, only high-performance disks and standard performance disks support hot migration. The cloud disk type and ID remain unchanged after migration. |
|   | Create snapshots | Snapshots allow you to retain a copy of cloud disk data at a specific point in time. By scheduling regular snapshots for your cloud disks, you can ensure continuous business operations. Snapshots are ideal for scenarios such as environment replication and disaster recovery backup. |
|   | Automatic snapshots | Automatic snapshot policies apply to system disks and data disks, enabling the system to create snapshots periodically. Leveraging automatic snapshot policies effectively enhances data security and improves operational fault tolerance. |

|   | Roll back cloud disks by using snapshots | If you have created snapshots for a cloud disk, you can use the rollback feature to restore the cloud disk data to a previous point in time. Important Rolling back a cloud disk is an irreversible operation. Once a rollback is completed, any data written to the disk after the snapshot was taken will be permanently lost. Proceed with caution. |
|---|---|---|
| Cloud disk snapshots |   |   |
|   | Snapshot chains | A snapshot chain is a relationship chain consisting of all snapshots of a cloud disk. Each cloud disk corresponds to one snapshot chain. You can view the capacity occupied by all snapshots of a cloud disk through its snapshot chain. |
|   | Snapshot- consistent groups | By creating a snapshot-consistent group, you can create snapshots for multiple cloud disks attached to one or more ECS instances simultaneously. Snapshot-consistent groups ensure write sequence consistency and crash consistency for data written to multiple cloud disks in business systems spanning multiple cloud disks. If you have strict data consistency requirements, you can enable the application-consistent snapshot feature when creating a consistent snapshot group. Application-consistent snapshots ensure internal data consistency within applications. This feature is supported only on the following operating systems: Windows Server 2016, Windows Server 2019, Windows Server 2022, Windows Server 2025, Ubuntu 20.04, Ubuntu 22.04, and Ubuntu 24.04. |
|   | Instant snapshot availability | For high-performance disks, if you enable the instant snapshot availability feature when creating a snapshot, you can immediately roll back the disk or create a new cloud disk based on the snapshot after the snapshot creation. You can manually disable this feature when it is no longer needed. |
|   | Shared snapshots | You can share snapshots created under your organization with other level-1 organizations. Users in recipient organizations can create cloud disks from these shared snapshots. |
| Local disks |   | A local disk is a local hard drive attached to the physical machine where the ECS instance resides, providing the ECS instance with local cache access capabilities. Because local disks connect directly to the physical machine, they offer advantages such as low latency, high random IOPS, and high throughput, making them suitable for high-performance caching scenarios. |

**Performance and scalability**

| Performance | Description |
|---|---|

| Minimum capacity per disk | 20 GiB |
|---|---|
| Maximum capacity per disk | Ultra disk: 32,768 GiB High-performance cloud disk: 131,072 GiB Cloud SSD: 32,768 GiB Standard performance disk: 32,768 GiB |
| Maximum IOPS | Ultra Disk: 5,000 High-performance disk: 25,000 Cloud SSD: 25,000 Standard performance disk: 5,000 |
| Maximum throughput | Ultra Disk: 140 MB/s High-performance disk: 300 MB/s Cloud SSD: 300 MB/s Standard performance disk: 140 MB/s |
| Multi-instance attachment | A high-performance disk with the multi-attach feature enabled can attach to multiple NVMe-compatible ECS instances in the same zone. This allows multiple ECS instances to concurrently read from and write to the same high- performance disk. |

**Deployment requirements**

An EBS standard cluster requires at least six nodes and supports up to 96 nodes. An EBS Lite cluster deployed on all-flash storage media requires at least four nodes.

**Important**

When you deploy a cluster with four or five nodes, only one fault domain exists. In this configuration, the failure of an additional node may result in data loss.

#### 1.4.3 Simple Log Service

This topic describes the features of Simple Log Service.

**Features**

| Feature | Description |
|---|---|

| Project | A project is a resource management unit in Simple Log Service for resource isolation and control. You can use projects to manage all logs of an application and the related log sources. A project manages all Logstores of a user, the configurations of machines from which logs are collected, and other information. A project also serves as an endpoint that you can use to access Simple Log Service resources. |   |
|---|---|---|
| Logstore | A Logstore in Simple Log Service is used to collect, store, and query logs. Each Logstore belongs to a project. You can create multiple Logstores for a project. |   |
| Metricstore | A Metricstore in Simple Log Service is used to collect, store, and query metrics. Simple Log Service stores all data in Metricstores as time series. Simple Log Service uses the model of time series data that is defined by Prometheus. Each time series consists of samples with the same metric identifier. |   |
| Machine group management | Simple Log Service uses machine groups to manage all servers from which logs are collected by using Logtail. A machine group is a virtual group that contains multiple servers. If you have multiple servers and want to use the same Logtail configuration to collect logs from these servers, you can add the servers to a machine group and apply the Logtail configuration to the machine group. |   |
| Log collection | Simple Log Service supports multiple data collection methods, such as Logtail, web tracking, and SDKs. Simple Log Service supports multiple data types, such as logs, metrics, and traces. Simple Log Service also supports multiple data sources, such as Alibaba Cloud services, servers and applications, Internet of Things (IoT) devices, mobile devices, open source software, and logs in standard formats. |   |
|   | Analysis algorithms | General aggregate functions. Security monitoring functions. Mapping functions. Mathematical statistics functions: standard deviation, covariance, correlation, regression slope, and other algorithms. Estimation functions, mathematical calculation functions, string processing functions, date and time functions, URL functions, regular expressions, JSON processing functions, IP address functions, window functions, and other functions. |
|   | Sequence decomposition | The STL algorithm is used to decompose time series data. |

|   | Data query | Simple Log Service supports queries on data of various types, such as JSON, text, and numeric data. Simple Log Service automatically builds indexes for text in JSON data. Simple Log Service supports full-text search. Simple Log Service supports combined queries with multiple conditions (AND, OR, and NOT). Simple Log Service supports contextual queries (N lines before and after) in raw logs. |
|---|---|---|
| Log query and analysis |   |   |
|   | LogReduce | Simple Log Service supports clustering logs in any format. Simple Log Service supports clustering query results. Simple Log Service supports adjusting clustering precision. Simple Log Service supports querying raw data based on clustering results. |
|   | Time series clustering | Simple Log Service uses density-based clustering to cluster multiple time series. Simple Log Service uses hierarchical clustering to cluster multiple time series. |
|   | Time series smoothing | Simple Log Service supports smoothing time series data by using the Holt-Winters, FIR, and IIR algorithms. |
|   | Time series forecast | Simple Log Service uses auto-regressive models to model time series data, predict time series, and detect anomalies. Simple Log Service uses moving auto-regressive models to model time series data, predict time series, and detect anomalies. Simple Log Service uses moving auto-regressive models with differencing to model time series data, predict time series, and detect anomalies. Simple Log Service accurately predicts single time series that contain periodicity and trends. |
|   | Maximum value detection | The maximum value detection function is used to find local maximum values of a sequence in a specified window. |

|   | Change point detection | Simple Log Service finds intervals with different statistical characteristics in a time series. The endpoints of the intervals are change points. Simple Log Service finds points in a time series where a statistical measure sharply increases or decreases. |
|---|---|---|
| Trace | Simple Log Service provides distributed tracing based on the native OpenTelemetry protocol. Simple Log Service supports the ingestion, storage, analysis, and visualization of various types of trace data. Simple Log Service also supports artificial intelligence for IT operations (AIOps). OpenTelemetry is a globally recognized standard for distributed tracing. OpenTelemetry is compatible with various clients of OpenTracing and OpenCensus. OpenTelemetry provides a collection of APIs, SDKs, and tools. You can use OpenTelemetry to instrument, generate, collect, and export various observable data, including traces, logs, and metrics. |   |
| Scheduled SQL | Simple Log Service provides the Scheduled SQL feature. You can use the feature to automatically analyze data at regular intervals and aggregate data for storage. You can also use the feature to project and filter data. |   |
| Dashboard | Simple Log Service allows you to visualize query statements as charts. Simple Log Service supports various chart types, such as tables, line charts, and column charts. Simple Log Service allows you to add multiple charts to a dashboard for unified viewing. Simple Log Service supports drill-down analysis to obtain more in-depth analysis results. |   |
| Alert | Simple Log Service allows you to configure alert rules for query and analysis results. After you create an alert rule, Simple Log Service periodically checks the related query and analysis results. If the query and analysis results meet the trigger condition that you specified in the alert rule, Simple Log Service sends an alert notification. This way, you can monitor the service status in real time. |   |

**Data security and reliability**

| Feature | Description |
|---|---|
| Triplicate storage | Each chunk is replicated into three replicas, and these replicas are stored on different nodes in a cluster based on a specified policy. This ensures that even if a node fails, data can still be recovered from other nodes. |

| Erasure coding (EC) | Raw data is divided into multiple data fragments, and a certain number of parity fragments are generated by calculation. These data fragments and parity fragments together form an EC group and are distributed on different storage nodes. When some of the data fragments or parity fragments are lost, the lost data can be restored by using other fragments. EC involves the following concepts: Data fragments (n): Data is divided into n data fragments. Parity fragments (m): m parity fragments are computed from the n data fragments. The n data fragments and m parity fragments form ECS groups and reside on different servers. If the number of lost fragments is less than or equal to m, the lost fragments can be restored based on the EC algorithm. n and m can be configured, depending on the number of nodes deployed in the cluster. We recommend that you set n to 8 and m to 3 if the number of nodes is greater than or equal to 14. |
|---|---|
| Online modification of replica policies | EC policies can be modified online on CDS-OPS. |
| Data encryption | Simple Log Service supports data encryption by using Key Management Service (KMS) to protect static data. Simple Log Service supports encryption by using Simple Log Service- managed keys. Simple Log Service supports encryption by using Bring Your Own Key (BYOK). |
| Multiple regions | The SCMG control module is deployed in the central region to verify the uniqueness of projects and synchronize account information to Simple Log Service clusters in all regions. Independent Simple Log Service clusters are deployed in each region for log storage, query, and analysis. |

**Data management**

| Feature | Description |
|---|---|
| Data transformation | Simple Log Service provides more than 200 built-in functions, more than 400 regular expressions, and flexible custom functions to filter, split, convert, enrich, and replicate data. This feature meets your business requirements for multiple scenarios, such as data distribution, standardization, and integration. |

| Data consumption | Simple Log Service provides real-time consumption interfaces for log data that is collected to the server. Simple Log Service supports the following types of real-time consumption: SDK consumption: Simple Log Service provides SDKs in multiple programming languages, such as Java, Python, and Go. Consumer group consumption: A consumer group is an advanced mode that Simple Log Service provides for consumers. Consumer groups provide a lightweight computing framework that allows multiple consumers to consume data from a Logstore in parallel. Consumer groups provide features such as automatic shard allocation, sequential consumption, and consumption from checkpoints. Simple Log Service provides consumer group SDKs in multiple programming languages, such as Java, Python, and Go. Real-time computing system consumption Spark Streaming consumption Use Storm to consume log data Open source Flink consumption Open source product consumption: Flume consumption. |
|---|---|
| Data shipping | Simple Log Service supports shipping logs to Object Storage Service (OSS) in real time for long-term storage and data backup. |

**Deployment requirements**

At least four nodes must be deployed in a Simple Log Service cluster, and six nodes are recommended.

**Important**

If four nodes are deployed, only one node can fail. If one more node fails, data may be lost.

#### 1.4.4 Hybrid Disaster Recovery

This topic describes the features of Hybrid Disaster Recovery.

**Basic Features**

| Feature | Description |
|---|---|
| Cross-zone disaster recovery | When a production site's application cannot recover quickly due to force majeure (such as data center fires or power outages) or device failures (software or hardware damage), the disaster recovery service supports cross- zone disaster recovery for business applications. It performs disaster recovery and backup for the entire application to handle single-region failures, meeting the core RTO/RPO metrics for the business. |

| Cross-region disaster recovery | Cross-region disaster recovery involves deploying a production site and a disaster recovery site in two different regions. If the production site fails, the business system quickly switches to the disaster recovery site, ensuring business continuity and high availability. |
|---|---|
| Cross-cloud disaster recovery | Cross-cloud disaster recovery means the production cloud and disaster recovery cloud are two cloud instances deployed off-site. If the production cloud fails, the business system switches to the disaster recovery cloud. This effectively prevents system failures caused by instance failures, ensures business availability, and meets the core RTO/RPO metrics for the business. |
| Failover | Failover after data synchronization This failover first stops the protected instances in the protection group. It then waits for all protected instances to stop before performing the final round of data synchronization. After data synchronization completes, it initiates the failover. This ensures complete data consistency between the disaster recovery site and the production site, with no data loss. This failover mode applies to scenarios such as planned disaster recovery drills and business migration. Switch now This failover attempts to stop the protected instances in the protection group. It does not wait for all protected instances to stop, nor does it perform the final round of data synchronization. Some data loss may occur within the RPO. This failover mode applies to scenarios where the production site experiences a short-term unrecoverable failure and requires immediate failover to the disaster recovery site. |
| Fault recovery | Switchover after data synchronization This failback stops the protected instances in the protection group and waits for all protected instances to stop. It then performs the final round of data synchronization. After data synchronization completes, it initiates the failback. The service unavailability time will be longer than that of immediate failover. This is mainly used in scenarios where the production site is operating normally. Switch immediately. This failback attempts to stop the protected instances in the protection group. However, it does not wait for all protected instances to stop, nor does it perform the final round of data synchronization. Initiating failback immediately may result in some data loss. This is mainly used in scenarios where the disaster recovery site experiences a short-term unrecoverable failure, requiring immediate business recovery to the production site. |

| Alerting feature | It supports status monitoring for production sites, disaster recovery sites, protection groups, and security group policies, and reports alert information. This ensures the stable operation of disaster recovery services. |
|---|---|
