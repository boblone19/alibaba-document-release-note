---
title: "Alibaba Cloud Apsara Stack v3.18.6-2607 Cloud Defined Storage Product Introduction 20260831"
product_version: "V3.18.6_2607"
doc_version: "20260831"
pdf_pages: 46
source_pdf: "Alibaba Cloud Apsara Stack v3.18.6-2607 Cloud Defined Storage Product Introduction 20260831.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/3816%202607/pdf%203/CDS/Alibaba%20Cloud%20Apsara%20Stack%20v3.18.6-2607%20Cloud%20Defined%20Storage%20Product%20Introduction%2020260831.pdf"
converter: pdf2md (PyMuPDF line classifier)
---

# Alibaba Cloud Apsara Stack v3.18.6-2607 Cloud Defined Storage Product Introduction 20260831

## Cloud Defined Storage

Cloud Defined Storage (CDS) is a distributed file storage system provided by Alibaba Cloud. CDS features high security, high reliability, low cost, centralized management, and elastic resource scaling, which allows efficient data storage and retrieval. Based on Object Storage Service (OSS), Log Service, Apsara File Storage NAS, and Elastic Block Storage (EBS), CDS provides storage for unstructured data such as files, images, and videos, and supports log storage, query, and analysis features. This allows users in different industries to access unstructured data and process massive amounts of logs. CDS is ideal to provide unstructured data storage and log services in big data scenarios such as mobile application and large websites. CDS offers a one-stop storage solution for users in different industries that is cost-effective, secure, and reliable.

### Features

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

The following section introduces the Hybrid Disaster Recovery service: Positioning Disaster recovery at the application level for business continuity: In the case of data center failure or long-time system maintenance, Hybrid Disaster Recovery allows you to quickly run applications on the cloud. This shortens the service interruption period and reduces losses. You can use the server replication feature of Hybrid Disaster Recovery to implement cross-zone disaster recovery protection for ECS instances so that you do not need to create servers again on the cloud. Scenarios Hybrid Disaster Recovery provides a high-standard disaster recovery solution for key enterprise applications. It features disaster recovery with a recovery point objective (RPO) of a few minutes and a recovery time objective (RTO) of a few minutes.

### Benefits

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

**Note**

The throughput performance varies based on the hardware of a server.

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

### Scenarios

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

### Features

#### Object Storage Service

This topic describes the functions and features of Object Storage Service (OSS).

**Bucket management**

| Feature | Description |
|---|---|
| Create buckets | A bucket is a container for storing objects. Each object must belong to a bucket. A bucket has various configuration properties, including the region, access control list (ACL), and storage class. You can create buckets as needed to store data. |
| Delete buckets | You can delete an empty bucket that contains no objects. Warning You cannot recover a deleted bucket. Proceed with caution. |
| ACL | You can set the ACL when creating a bucket, or modify the ACL after creation based on your business requirements. Only the bucket owner can perform this operation. The following ACLs are available: public-read-write: Public read/write. Any user, including anonymous users, can read and write objects in the bucket. Warning Any user on the Internet can access the objects in the bucket and write data to the bucket. This may cause data leakage. If malicious users write illegal information to the bucket, your legitimate rights and interests may be violated. We recommend that you do not configure the public-read-write ACL unless necessary. public-read: Public read. Only a bucket owner can write objects in the bucket. Any user, including anonymous users, can read objects in the bucket. Warning Any user on the Internet can access the objects in the bucket. This may cause data leakage. Configure this ACL with caution. private: Private. Only a bucket owner can read and write objects in the bucket. Other users cannot access the objects in the bucket. |

| Static website hosting | You can use the static website hosting feature to host your static website on an OSS bucket and access the website by using the endpoint of the bucket. The default homepage is the page that OSS returns when a user accesses the static website domain name through a browser. This page is equivalent to the index.html file of a website. The file that you specify as the default homepage must be an object in the root directory of the bucket that allows anonymous access. The file must be in HTML format. The default 404 page is the error page that OSS returns when a 404 error occurs during access to an object in the bucket through a browser. The file that you specify as the default 404 page must be an object in the root directory of the bucket that allows anonymous access. The file can be in HTML, JPG, PNG, BMP, or WebP format. |
|---|---|
| Capacity management | You can set a capacity limit for a bucket when creating the bucket. You can modify the capacity limit for a bucket in the console. |
| Log transfer | Accessing OSS generates a large number of access logs. You can use the log transfer feature to write these logs to a specified bucket as log files on an hourly basis according to a fixed naming convention. You can analyze the stored logs by using Simple Log Service (SLS) or by building a Spark cluster. |
| Lifecycle management | Lifecycle rules can periodically delete infrequently accessed data or data no longer needed, which helps you manage stored data more efficiently and saves labor and storage costs. For example, if a bucket contains a large number of objects that you want to delete, manual deletion supports only up to 1,000 objects at a time, which is tedious. In this case, you can configure a lifecycle rule that matches the entire bucket and deletes all objects after one day. OSS deletes all data in the bucket on the next day. |
| Bucket tagging | You can use the bucket tagging feature to classify and manage buckets. For example, you can list buckets with specific tags or set ACLs for buckets with specific tags. |
| Hotlink protection | OSS supports hotlink protection by configuring an allowlist, a blocklist, and an empty Referer policy based on the Referer field in HTTP and HTTPS headers. When a browser sends a request to OSS, the request header includes the Referer field, which indicates the source page of the request. If you configure hotlink protection, OSS checks the Referer in the request against the configured Referer rules to determine whether to allow the request: If the Referer in the browser request matches the allowlist, OSS allows the request. If the Referer in the browser request matches the blocklist or does not match the allowlist, OSS denies the request. If you do not allow empty Referers, only requests that include the Referer field in the HTTP or HTTPS header can access OSS resources. |

| Retention policy (WORM) | The OSS retention policy supports the Write Once Read Many (WORM) feature, which allows you to store and use data in a way that prevents deletion and tampering. To prevent any user, including the resource owner, from modifying or deleting objects in a bucket within a specified period, you can configure a retention policy for the bucket. Before the retention period of the objects expires, you can only upload and read objects in the bucket. You can modify or delete objects only after the retention period expires. |
|---|---|
| CORS | OSS provides Cross-Origin Resource Sharing (CORS) settings in the HTML5 protocol, enabling cross-origin access. When OSS receives a cross-origin request or an OPTIONS request, it reads the CORS rules of the bucket and performs the corresponding permission check. OSS checks each rule in sequence and uses the first matching rule to allow the request and return the corresponding headers. If no rule matches, OSS does not attach any CORS-related headers. |
| Inventory | You can use the API to obtain information about specified objects in a bucket, such as the quantity, size, and storage class. |
| Back-to-origin rules | Back-to-origin supports two types: mirroring and redirection to meet your requirements for hot data migration and request redirection. Mirroring back-to-origin After configuring mirroring back-to-origin, if you perform a GET operation on a nonexistent object in OSS, OSS requests the object from the origin address specified in the back-to-origin rule, returns the target object to you after retrieval, and writes the object to OSS. Mirroring back-to-origin is primarily used for seamless data migration to OSS. For example, if your service runs on a self-built origin server or another cloud product and you need to migrate the service to OSS without stopping the service, you can use the mirroring write-back feature. Redirection After configuring redirection, if you perform a GET operation on a nonexistent object in OSS, OSS redirects your request to the origin address specified in the back-to-origin rule to retrieve the target object. You can use this redirection feature to redirect requests for objects and implement various business scenarios based on redirection. |
| Access by using a custom domain name | After you upload an object to a bucket, OSS automatically generates an object URL. You can access the object directly through the object URL. To access these objects by using a custom domain name, you must bind the custom domain name to the bucket where the objects reside. |

**Object management**

| Feature | Description |
|---|---|

| Upload objects | An object is the basic unit of data storage in OSS and is also referred to as an OSS file. You can select an appropriate upload method based on the file size and network environment. OSS provides the following upload methods: Simple upload: Includes streaming upload and file upload. The maximum file size is 5 GiB. Form upload: The maximum file size is 5 GiB. Append upload: The maximum file size is 5 GiB. Resumable upload: Supports concurrent upload, resumable transfer, and custom part size. We recommend resumable upload for large files. The maximum file size is 48.8 TiB. Multipart upload: You can use multipart upload for large files. The maximum file size is 48.8 TiB. During the upload process, you can set object metadata and monitor the upload progress through the progress bar. After the upload, you can also configure an upload callback. |
|---|---|
| Delete objects | You can delete objects by using the following methods: Delete objects through the console. Automatically delete objects through lifecycle management policies. Delete objects through SDKs and APIs. Delete objects through tools such as ossutil. Warning You cannot recover deleted objects. Proceed with caution. |
| ACL | OSS provides object-level ACLs to control access permissions for objects. You can set the ACL when uploading an object, or modify the ACL after uploading. If you do not set an ACL, the default value is Inherit Bucket. Inherit Bucket: The object inherits the ACL of the bucket to which it belongs. Private: Only the object owner can read and write the object. Other users cannot access the object. Public Read: Only the object owner can write the object. Any user, including anonymous users, can read the object. Public Read/Write: Any user, including anonymous users, can read and write the object. Use this permission with caution. |

| Download objects | OSS provides various object download methods. You can select an appropriate method to download files stored in a bucket. The following download methods are available: Download to local: Download objects from a bucket to your local device. Streaming download: When a file is too large or a one-time download takes too long, you can use streaming download to process partial content at a time until the download completes. Range download: If only a portion of the data in a file is needed, you can use range download to download data within a specified range. Resumable download: When you download a large file, network instability or unexpected program termination may cause the download to fail, even after multiple retries. To address this, OSS provides the resumable download feature, which splits the file into multiple slices and downloads each slice separately. After downloading all slices, OSS merges them into a complete file. Conditional download: When downloading a file, you can specify one or more conditions. OSS downloads the file if the conditions are met, and returns an error without downloading the file if the conditions are not met. |
|---|---|
| Manage objects | OSS allows you to quickly search for and locate target objects by specifying an object name prefix. You can create directories to store objects in specified directories. |
| Object tagging | Object tagging uses a set of key-value pairs to tag objects. You can add tags when upload objects or add tags to existing objects to implement the following features: Configure lifecycle rules for objects with the same tags. Manage permissions for objects with specified tags through RAM policies. |

**Data security**

| Feature | Description |
|---|---|
| Three-replica storage | The system replicates each chunk into three identical replicas and stores them on different nodes in the cluster based on a specific strategy. This approach ensures data recovery from other nodes if a node fails. |

| Erasure coding | The system divides the original data into multiple data chunks and generates a specific number of parity chunks through computation. These data chunks and parity chunks form an erasure coding (EC) group and reside on different storage nodes. When some data chunks or parity chunks are lost, the system can recover the lost data from the remaining chunks. EC involves two concepts: data chunks (N) and parity chunks (M). Data chunks (N): The system divides data into n data slices. Parity chunks (M): The system computes m parity chunks from the n data chunks. The data chunks (N) and parity chunks (M) form an EC group and reside on different servers. When any number of chunks up to M are lost, the system can recover the lost chunks through the EC algorithm. N+M is configurable. We recommend a configuration of 8+3 for Apsara Stack, depending on the number of cluster nodes deployed. The system supports online modification of EC policies. |   |
|---|---|---|
| Resource isolation | OSS uses Access Key symmetric key authentication for user authentication and verifies the signature of every HTTP request from users. After user verification succeeds, the system reassembles the discretely stored data of the user, thereby achieving data storage isolation across multiple tenants. |   |
| Disaster recovery and backup | Zone- disaster recovery | Zone-disaster recovery stores your data redundantly across multiple availability zones (AZs) within the same region. This approach minimizes data loss during a single availability zone failure to help you recover your business quickly. OSS provides two zone-disaster recovery solutions: Two-AZ zone-disaster recovery: After you enable zone- disaster recovery for a bucket, OSS synchronizes data from the bucket in the primary data center to a backup bucket in the OSS cluster of the standby data center. When the primary data center experiences a complete failure, such as a power outage or fire, data remains accessible. To address the growing demands for high traffic and concurrency while ensuring high availability and disaster recovery capabilities, OSS allows you to deploy multiple independent two-zone disaster recovery clusters within the same region. These clusters work together to handle business traffic, enabling elastic resource scaling and risk isolation. Three-AZ zone-disaster recovery: After you create a bucket with zone-redundant storage, the system stores user data redundantly across three independent availability zones within the same region. This ensures that if any availability zone becomes unavailable due to network outages, power failures, or disasters, the other two availability zones continue to provide services, maintaining business continuity and data security. When an availability zone fails, OSS continues to provide strongly consistent services. The failover process is transparent to users and ensures zero data loss, meeting the stringent requirements of critical business systems for RPO (Recovery Point Objective) equal to 0 and RTO (Recovery Time Objective) approaching 0. |

|   | Cross- region replication | Cross-region replication automatically and asynchronously replicates objects across buckets in different OSS data centers (regions) in near real time. This feature replicates object creation, update, and deletion operations from a source bucket to a target bucket in a different region. |
|---|---|---|
|   | Cross-cloud replication | Cross-cloud replication allows you to replicate data from one cloud system to another, enabling data backup across different cloud systems. When a cloud system fails, you can switch your business directly to another cloud system to ensure business continuity. |
|   | RAM policy | Resource Access Management (RAM) is a resource access control service provided by Alibaba Cloud. A RAM policy is a user-based authorization policy. By configuring RAM policies, you can centrally manage users, such as employees, systems, or applications, and control which resources under your cloud account these users can access. For example, you can restrict other users to read- only access to a specific bucket. |
| Security management and account authorization |   |   |
|   | Bucket policy | Bucket policy: A bucket policy is a resource-based authorization policy. Compared with RAM policies, bucket policies are simpler to operate. You can configure bucket policies directly in the console through a graphical interface, and the bucket owner can grant access permissions directly without requiring RAM operation permissions. Bucket policies support granting access permissions to RAM users of other accounts and granting access permissions with specific IP-based restrictions to anonymous users. Bucket ACL: You can set the ACL when creating a bucket, or modify the ACL at any time after bucket creation based on your business requirements. Only the bucket owner can perform this operation. Bucket ACLs include public-read-write (public read/write), public-read (public read), and private (Private). Hotlink protection: OSS supports hotlink protection for buckets. This feature uses an allowlist mechanism for access origins to prevent unauthorized use of OSS resources. |
|   | Object ACL | In addition to bucket-level ACLs, OSS also provides object- level ACLs. You can set the ACL when uploading an object, or modify the ACL at any time after the upload based on your business requirements. Object ACLs include Inherit Bucket, public-read-write (public read/write), public-read (public read), and private (Private). |
|   | Server-side encryption | OSS provides static data protection through server-side encryption, suitable for application scenarios with high security or compliance requirements for file storage, such as storing deep learning sample files and online collaborative document data. |

| Cloud Defined Storage |   |   |
|---|---|---|
| Encryption |   |   |
|   | Client-side encryption | When you use client-side encryption, the system generates a random data encryption key for each object and uses the plaintext of this key to symmetrically encrypt the object data. A master key generates the random data encryption key, and the system stores the encrypted content as object metadata on the server. During decryption, the system first uses the master key to decrypt the encrypted random key, and then uses the decrypted plaintext of the random data encryption key to decrypt the object data. The master key participates only in local computation on the client and is never transmitted over the network or stored on the server, ensuring the data security of the master key. Warning When using client-side encryption, you are responsible for the integrity and correctness of the master key. You bear all losses and consequences caused by the inability to decrypt encrypted data due to incorrect use or loss of the master key resulting from improper maintenance. When copying or migrating encrypted data, you are responsible for the integrity and correctness of the encryption metadata. You bear all losses and consequences caused by the inability to decrypt encrypted data due to errors or loss of the encryption metadata resulting from improper maintenance. |
|   | Transport layer encryption (TLS) | Communication between client applications and OSS uses Transport Layer Security (TLS) for encryption. TLS is a standard encryption protocol that ensures privacy and data integrity between clients and servers communicating over the Internet. You can configure the TLS version on the OSS server. After configuration, the client supports only the specified TLS version for sending and receiving data with OSS, meeting the security requirements of the communication link. |

| Versioning | Versioning is a bucket-level data protection feature. After you enable versioning, the system saves data overwrite and deletion operations as historical versions. After accidentally overwriting or deleting an object, you can recover the object stored in the bucket to any historical version. |
|---|---|

**Data processing**

| Feature | Description |
|---|---|
| Source image protection | After you enable source image protection, the system blocks direct access to OSS source objects and access that uses image parameters to modify image styles. |
| Image processing rules | You can configure multiple style processing rules. |
| Image effect processing | You can adjust image brightness, contrast, sharpness, blur, and rotation through a graphical interface. |
| Image styles | A style contains multiple image processing parameters to help you quickly perform complex image processing operations. |
| Image resizing | You can choose to disable resizing, scale down proportionally, scale up proportionally, or resize to specified width and height. |
| Progressive display | This feature enables a display mode that renders images from blurry to clear. Ite applies only to JPG images. |
| Auto orientation | The system rotates the image based on the EXIF orientation data before resizing the image. |
| Format conversion | You can convert image formats and choose the source format, JPG, JPEG, PNG, BMP, GIF, WebP, or TIFF as needed. |
| Image quality | You can choose relative quality, absolute quality, or no compression. |
| Image watermark | You can choose to disable watermarks, use image watermarks, or use text watermarks. |
| Video snapshot | You can extract video frames and convert them to the required image format by using an SDK or adding snapshot parameters to the URL. |

**Scalability**

| Feature | Description |
|---|---|
| Cloud Storage Gateway | The file gateway maps the object structure of an OSS bucket to the directories and files of a NAS file system, allowing users to read and write objects in a specified OSS bucket through standard NFS and SMB protocols. The gateway also uses local storage space as a hot data cache to ensure high-performance data access while providing the massive storage capacity of the OSS bucket. |
| Cluster scaling | The cluster supports horizontal scaling of its size, including management and data nodes. A single cluster can scale up to hundreds of petabytes while maintaining linear performance scaling. |

**Reliability description**

For EC N+M, N data chunks and M parity chunks from devices form an EC group. The following describes the reliability for different cluster sizes: When the cluster size is greater than or equal to N+M+M nodes, the system tolerates the simultaneous failure of two devices without data loss, and the failure of a single device without data loss or business interruptions. When the cluster size is less than N+M+M nodes, a folded EC scenario may occur within the cluster. Therefore, the system tolerates the failure of only one device without data loss or business interruptions, but it cannot guarantee zero data loss if two devices fail simultaneously.

**Tools and compatibility**

| Feature | Description | Supported versions |
|---|---|---|
| Tools | ossbrowser graphical management tool | ossbrowser 2.0 |
|   | ossfs object-to-file-system tool for NFS and CIFS | ossfs 2.0 |
|   | ossftp object-to-FTP tool | ossftp 1.2.0 |
|   | ossutil command-line tool | ossutil 2.0 |
| SDK support | Java | 3.17.4 and earlier |
|   | Python | 2.18.3 and earlier |
|   | PHP | 2.0.0 and earlier |
| > Document Version: 2026 | 0831 2 |   |

| d Storage |   |   |
|---|---|---|
|   | C | 3.11.2 and earlier |
|   | Go | 3.0.2 and earlier |

**Deployment requirements**

In non-disaster recovery scenarios, an OSS cluster requires at least six nodes for deployment. In zone-disaster recovery scenarios, the number of nodes required for OSS cluster deployment depends on the disaster recovery solution in use. Two-AZ zone-disaster recovery: Deploy the OSS cluster across two availability zones. Deploying a cluster in a single availability zone requires at least six nodes, and both availability zones must have the same number of cluster nodes. Three-AZ zone-disaster recovery: An OSS 3AZ cluster cannot be the initial cluster. You can build an additional 3AZ disaster recovery cluster only when a zone-disaster recovery cluster already exists in the cloud environment. Deploying an OSS 3AZ cluster requires at least 21 nodes. Each single availability zone requires at least seven nodes, and all three availability zones must have the same number of cluster nodes.

#### Elastic Block Storage

This topic describes the features of Elastic Block Storage (EBS).

**Cloud disk management**

| Feature | Description |
|---|---|
| Create a cloud disk | You can create a cloud disk separately to increase the storage space of an Elastic Compute Service (ECS) instance. Cloud disks include premium performance disks, standard performance disks, ultra disks, and standard SSDs based on their performance. |
| Attach a cloud disk | You can attach a separately created cloud disk to an ECS instance in the same region and zone as a data disk. |
| Detach a cloud disk | You can detach a data disk from an ECS instance when the instance no longer needs the data disk. You can also detach a data disk from an ECS instance and then attach the data disk to another ECS instance in the same zone. |
| Release a cloud disk | If you no longer need a data disk, you can manually release it. All data stored on the cloud disk is released. You can also temporarily store the released cloud disk in the recycle bin. Within the retention period configured for the recycle bin, you can restore the cloud disk from the recycle bin. |

| Batch attach or detach cloud disks | You can attach multiple cloud disks to the same ECS instance at a time. You can also detach multiple cloud disks from the same ECS instance at a time. |
|---|---|
| Reinitialize a cloud disk | You can reinitialize a cloud disk to restore it to its initial state when it was created. Important After a cloud disk is reinitialized, the data stored on the cloud disk is lost and cannot be recovered. Exercise caution when you perform this operation. If you still need the data on the cloud disk, transfer the data or create a snapshot in advance. |
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
| Three replicas | The system replicates each data chunk into three identical replicas and stores them on different nodes in the cluster based on a specific strategy. This ensures that even if one node fails, the system can recover the data from other nodes. |
| Erasure coding (EC) | The system splits raw data into multiple data chunks and generates a specific number of parity chunks through computation. These data chunks and parity chunks form an EC group and are distributed across different storage nodes. If some data chunks or parity chunks are lost, the system can recover the lost data from the remaining chunks. EC involves two concepts: data chunks (n) and parity chunks (m): Data chunks (n): The system splits data into n data slices. Parity chunks (m): The system calculates m parity chunks from the n data chunks. The data chunks (n) and parity chunks (m) form an EC group and reside on different servers. The system can recover any lost chunks by using the EC algorithm as long as the number of lost chunks is less than or equal to m. You can configure n+m. Apsara Stack recommends an 8+3 configuration, depending on the number of deployed cluster nodes. |
| Modify EC policies online | You can modify EC policies online through the O&M platform. Important After you enable the EC mode, you cannot switch back to the three replicas mode. Proceed with caution. |

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

#### Simple Log Service

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
| Three replicas | Each chunk is replicated into three replicas, and these replicas are stored on different nodes in a cluster based on a specified policy. This ensures that even if a node fails, data can still be recovered from other nodes. |

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

#### Tablestore

This topic describes the features of Tablestore.

**Basic features**

**Instance**

| Feature | Description |
|---|---|
| Create instance | Creates an instance, which the system assigns to a specific cluster with a unique endpoint. After creating the instance, your application can create tables and perform operations within it. |

| Delete instance | Deletes an instance. Before deleting an instance, you must delete all of its tables; otherwise, the operation fails. |
|---|---|
| Instance management | You can manage instances by creating, deleting, or listing them in the console. Each instance has a unique endpoint that you can find in the console. All requests to the instance must use this endpoint. |

**Table**

A table is a collection of rows, and each row consists of a primary key and attributes. Both primary key columns and attribute columns consist of a name and a value. All rows in a table must have the same number and names of primary key columns. However, the number, names, and data types of attribute columns can vary from row to row.

| Feature | Description |
|---|---|
| Create table | Creates a table within an instance. When you create a table, you must specify its name and primary key schema. You can also configure advanced options such as time to live (TTL), max versions, and pre-partitioning. For High-Performance instances, you can set the reserved read/write throughput for a table. The system allocates resources based on these settings. You can set the reserved read/write throughput to 0, in which case the system does not reserve dedicated resources for the table. |
| Delete table | This operation releases the storage and I/O resources allocated to the table and deletes all its data. |
| Update table | Updates a table's settings, such as its time to live (TTL), max versions, and reserved read/write throughput. For High-Performance instances, you can scale the reserved read/write throughput up or down. |
| List tables | Lists the names of all tables within an instance. |
| Delete row | Deletes all versions of a row specified by its primary key. |
| Update row | Updates a row specified by its primary key. Supports writing to a column, deleting a column, or deleting a specific version of a column. Supports conditional updates (ConditionalUpdate). Supports specifying the version number for the attribute column you are updating. |

| Read row | Reads a row specified by its primary key. Supports specifying which attribute columns to read. Supports reads with a filter. Supports reading multiple versions of an attribute column by specifying the number of versions. Supports reading multiple versions of an attribute column that fall within a specified version number range. You can read up to 128 attribute columns in a single operation. |
|---|---|
| Read a range of data | Tablestore sorts rows by their primary keys. A primary key consists of one or more primary key columns in a defined order. The GetRange operation reads a continuous range of data. You can read up to 5,000 rows or 4 MiB of data in a single operation. Supports both forward and reverse reads. Supports specifying the number of rows to read. If the result set exceeds 5,000 rows or 4 MiB of data, you must make multiple read requests using the returned next primary key as the starting point. Supports reads with a filter. Supports reading multiple versions of an attribute column by specifying the number of versions. Supports reading multiple versions of an attribute column that fall within a specified version number range. |
| Batch insert, update, or delete rows in one or more tables | Inserts, updates, or deletes multiple rows in one or more tables in a single operation. Use the BatchWriteRow API for multi-row operations. Use the BatchGetRow and GetRange APIs for batch reads. Supports conditional updates (ConditionalUpdate) with arithmetic operators (=, !=, >, >=, <, <=) and logical operators (NOT, AND, OR), allowing up to 10 combined conditions. Conditional updates enable optimistic locking. For example, to update a row, you can first retrieve the value of a column (e.g., column A = 1), then set a condition that column A = 1 before updating the row to set column A = 2. If the update fails, it means another client has already updated the row. Supports specifying the version number for the attribute column to be updated. You can write up to 200 rows or 4 MiB of data in a single operation. |
| Batch read rows from one or more tables | Reads multiple rows from one or more tables in a single operation. Supports specifying which attribute columns to read. Supports reads with a filter. Supports reading multiple versions of an attribute column by specifying the number of versions. Supports reading multiple versions of an attribute column that fall within a specified version number range. You can read up to 100 rows in a single operation. |

| Time to live (TTL) | The time to live (TTL) is a table attribute that defines the lifespan of data in seconds. Tablestore automatically deletes data that has exceeded its TTL, which reduces data storage and lowers costs. |
|---|---|
| Max versions | Specifies the maximum number of versions that can be retained for each attribute column in a table. When the number of versions for an attribute column exceeds this limit, Tablestore asynchronously deletes the oldest version. |
| Pre-partitioning | By default, a new table has only one partition. You can pre-partition a table upon creation, either automatically or by defining custom partitions, to improve performance for concurrent writes. |
| Filter | Applies server-side filtering to read results, returning only the rows that match the filter conditions. By returning only matching rows, filters can significantly reduce network traffic and response times in most scenarios. |

**Row**

A row in a table consists of a primary key and attributes. Both the primary key and attributes can contain multiple columns, each with a name. Each row must contain primary key columns, but attribute columns are optional.

| Feature | Description |
|---|---|
| Primary key | The primary key uniquely identifies each row in a table. It consists of one to four primary key columns. When you create a table, you must explicitly define the composition of the primary key, including the name, data type, and order of each primary key column. |
| Auto-increment primary key | You can configure a non-partition key column as an auto-incrementing primary key. When you write a row, you do not need to provide a value for this column. Tablestore automatically generates a unique and strictly increasing value for it within the partition. |
| Attribute column | Attribute columns store the data of a row. A row can include any number of attribute columns. |
| Multiple data versions | Each attribute column can store multiple versions of data, with each version identified by a version number. |

**Search index**

Search Index uses an inverted index and columnar storage to enable multi-dimensional queries and statistical analysis on large datasets. A single Search Index can support various query types without the need to create multiple indexes for different conditions. Compared to a global secondary index, Search Index supports more complex operations, including boolean queries, fuzzy queries, full-text search, and geo-queries. We recommend using Search Index for hot data and using a secondary index or no index for cold data.

| Categ ory | Feature | Description |
|---|---|---|
| Index mana geme nt | Search Index manage ment | Create one or more Search Indexes on a data table to accelerate queries. When you create a Search Index, you must add the fields you want to query to the index. You can also configure advanced options such as routing keys, time to live (TTL), and pre-sorting. After creating a Search Index, you can view its description, list all Search Indexes, and delete them. |
|   | Lifecycle manage ment | The time to live (TTL) is an attribute of a Search Index that specifies how long data is retained. Search Index automatically deletes data that exceeds its TTL, which reduces data storage and lowers costs. You can use Search Index TTL if your table does not have UpdateRow write operations. |
|   | Dynamic schema modifica tion | Tablestore data tables are schema-free, but Search Index has a strong schema. When creating a Search Index, you must specify which columns to add to make them queryable. You can dynamically modify the Search Index schema to add, update, or delete indexed columns, or to change the routing key. |
| Data types | Data type mapping | A Search Index field gets its value from the data table column of the same name, and their data types must be compatible. Search Index supports Long, Double, Boolean, Keyword, FuzzyKeyword, Text, Date, Geo-point, Vector, and Nested data types. Search Index fields also support additional properties such as arrays, virtual columns, and highlighting. The available properties vary by data type. |
|   | String types | Search Index supports three string-related types: Keyword, FuzzyKeyword, and Text. Keyword: The Keyword type is similar to string types in databases and programming languages like C++ and Java. It is the most commonly used string type. Use the Keyword type if your use case does not require fuzzy queries or full- text search. The Keyword type is required for sorting and aggregation. FuzzyKeyword: The FuzzyKeyword type is a string type that supports high- performance wildcard, prefix, and suffix queries. It maintains excellent query performance even as data volume grows. Use the FuzzyKeyword type if you need high-performance (millisecond-level) wildcard, prefix, or suffix queries. Text: The Text type is similar to text fields in search engines. It supports various analyzers that split a string into a sequence of terms for indexing. It is primarily used for full-text search scenarios. Use the Text type if you need full-text search capabilities. |
|   | Date data type | Search Index has extensive support for date data types. You can map Integer or String data from your table to the Date type in the index. Using the Date type for range queries is faster than using the String type. |

|   | Array and nested types | In addition to basic types like Long, Double, Boolean, Keyword, Text, and GeoPoint, Search Index also supports two special types: Array and Nested. Array type: An array is a property that can be applied to basic types like Long, Double, Boolean, Keyword, Text, and GeoPoint. For example, a Long array field can contain multiple long integers. A query will return a row if any value in the array matches the query condition. Nested type: Represents a nested document. A row (document) can contain multiple sub-rows (sub-documents) stored in a single nested field. For a nested field, you must define the structure of its sub-rows, including their fields and properties. |
|---|---|---|
|   | Virtual column | With virtual columns, you can map a column from your table to a virtual column in the Search Index. The new virtual column can have a different data type than the original column. This lets you create a new column for query acceleration or to use a different analyzer without modifying your table schema or data. Use different analyzers for a single Text field: You can map a single string column to multiple Text columns in a Search Index, each using a different analyzer to meet various business requirements. Accelerate queries: Improve query performance in certain scenarios without cleaning or rebuilding table data. You just need to map the corresponding column to another type. For example, converting a number type to a Keyword type can improve the performance of a TermQuery, and converting a String type to a number type can improve the performance of a RangeQuery. |
|   | Match- all query | A MatchAllQuery matches all rows. It is often used to count the total number of rows in a table or to return a few random rows of data. |
|   | Term query | A TermQuery performs an exact match, similar to a string comparison. For Text type fields, a row is matched if any of its analyzed terms match the query term exactly. |
|   | Terms query | Similar to a TermQuery, but a TermsQuery allows you to specify multiple keywords. A row is returned if it matches any of the specified keywords, which is equivalent to the SQL IN operator. |
|   | Range query | A RangeQuery finds data based on a range condition. For Text type fields, a row is matched if any of its analyzed terms fall within the specified range. |
|   | Exists query | An ExistsQuery, also known as a NOT NULL query, checks if a specific column exists in a row, which is useful for sparse data. For example, you can use it to find all rows where the address column is not empty. |

| Basic querie s |   |   |
|---|---|---|
|   | Fuzzy query | Search Index provides wildcard, prefix, and suffix queries to meet various fuzzy query needs. Wildcard query: Similar to the LIKE syntax in relational databases, it supports the asterisk (*) and question mark (?) wildcards. The asterisk (*) represents any sequence of characters, and the question mark (?) represents any single character. Queries can start with an asterisk (*) or a question mark (?). For query patterns like *word* , you can achieve better performance by using a token-based wildcard query, which is a combination of fuzzy tokenization and a phrase matching query. Prefix query: Matches content based on a prefix. For example, a query with the prefix apple will match content such as apple6s and applexr . In addition to Chinese and English, prefix queries also support other languages. Suffix query: Matches content by its suffix. For example, you can query for all mobile numbers that end with 1234 . |
|   | Geo- query | Tablestore provides the following geo-query capabilities: Geo-distance query: A GeoDistanceQuery finds data within a specified distance from a central point. A location matches if its distance to the specified center point is less than or equal to the specified value. Geo-bounding box query: A GeoBoundingBoxQuery finds data within a rectangular geographical area. A location matches if it falls within the specified rectangular bounds. Geo-polygon query: A GeoPolygonQuery finds data within a polygonal geographical area. A location matches if it falls within the specified polygon. |
|   | Nested query | A NestedQuery is used to query data within the sub-rows of a nested field. You cannot query a nested field directly. Instead, you must use a NestedQuery, which specifies the path to the nested field and a sub-query. The sub-query can be of any query type. |
|   | Sort and paginati on | When querying data with Search Index, you can retrieve results in a specific order by pre-defining a sort order or specifying one at query time. When the result set is large, you can use token-based or offset-based pagination to quickly navigate to the desired data. |
|   | Collapse (dedupli cation) | If query results contain many items of a certain type, you can use the Collapse feature to group the result set by a specific column. This ensures that each type appears only once in the results, which promotes diversity in the displayed results. |
| Combi ned querie s | Boolean query | A BoolQuery contains one or more sub-queries and determines whether a row matches based on these sub-queries. Each sub-query can be of any query type, including another BoolQuery. |

| Aggre gation and statisti cs | Aggrega tion and statistics | Use aggregation and statistics functions to find the minimum, maximum, sum, and average of values, counting rows, counting distinct rows, calculating percentiles, grouping by field value, grouping by range, grouping by geo- location, grouping by filter condition, creating histograms, retrieving rows within aggregation groups, and performing nested queries. You can combine multiple aggregation functions to meet complex query requirements. |
|---|---|---|
| Full- text search | Match query | A MatchQuery performs an approximate match to find data containing a specified phrase. Tablestore first tokenizes the values in Text type columns and the query keywords using the configured analyzer, and then queries based on the resulting terms. |
|   | Match phrase query | A MatchPhraseQuery performs an approximate match to find data where the terms of a specified phrase appear in the correct order. A row matches only if the analyzed terms exist in the same order and position within the row's data. |
|   | Analyzer | After you set an analyzer for a Text type field, the system tokenizes the content into multiple terms based on the specified analyzer type. Currently, five analyzer types are supported: single-character, delimiter, minimum semantic, maximum semantic, and fuzzy. |
|   | Snippet and highlight ing | Highlights text in search results that matches or is relevant to the query terms. This helps users quickly identify relevant information and improves search efficiency. |
| Vector search | Vector search | A vector search (KnnVectorQuery) uses numerical vectors to perform approximate nearest neighbor (ANN) searches, allowing you to find the most similar items in large datasets. This feature is suitable for use cases such as Retrieval-Augmented Generation (RAG), recommendation systems, similarity detection, and natural language processing with semantic search. |
| Data export | Parallel scan | Search Index provides the Search API, which supports a full set of features, including all query functions, sorting, and aggregation. Results are returned in a specified order. However, some scenarios, such as integration with computing systems like Spark and Presto or data filtering tasks, only require full query capabilities and need to retrieve all matching data as quickly as possible, without regard for the order of the entire result set. To support these needs, Search Index offers the ParallelScan API. Compared to the Search API, the ParallelScan API retains all query functions but omits analytical features like sorting and aggregation. This trade-off delivers a performance improvement of more than 5x, enabling the export of hundreds of millions of rows per minute with horizontally scalable capacity. |

**Secondary index**

A secondary index improves query efficiency by creating one or more index tables and using their primary key columns for lookups. This effectively extends the primary key query capability of a data table to different columns.

| Feature | Description |
|---|---|

| Single-column and composite indexes | Supports creating an index on a single column or on multiple columns of a data table. |
|---|---|
| Index synchronization | The data synchronization method differs between a global secondary index and a local secondary index. With a global secondary index, Tablestore asynchronously replicates indexed columns and primary key columns from the data table to the index table. Under normal conditions, the synchronization latency is at the millisecond level. With a local secondary index, Tablestore synchronously replicates indexed columns and primary key columns from the data table to the index table. After data is written to the data table, it is immediately available for querying in the index table. |
| Covering index | Supports including attribute columns in an index table. After pre-defining columns in a data table, you can create an index on any of these pre-defined columns and the data table's primary key columns. You can specify some of the pre-defined columns to be included as attribute columns in the index table. An index table can also be created with no attribute columns. When pre-defined columns are included as attribute columns in an index table, you can read their values directly from the index table without needing to look them up in the data table. |
| Index backfill | Supports backfilling existing data from a data table into a newly created index table. |
| Sparse index | If a pre-defined column from a data table is included as an attribute column in an index table, an index entry is still created for a row even if that pre-defined column is missing, as long as all indexed columns are present. However, if any of the indexed columns are missing, no index entry is created for that row. |
| Index data query | You can query data based on the index, performing range or point lookups on the index's primary key. Data is synchronized asynchronously between the data table and the index table. Under normal conditions, the synchronization latency is at the millisecond level. Supports single-column and composite indexes, and allows index tables to include attribute columns. Supports sparse indexes. Querying an index table does not automatically look up data in the data table. You must perform this lookup yourself. Supports creating and deleting indexes on existing data tables. |

**Reliability and availability**

| Level | Description |
|---|---|

| Three replicas | Replicates each data chunk into three identical copies and stores them on different nodes across the cluster. This ensures that if a node fails, data is recoverable from the other copies. |
|---|---|
| Erasure coding (EC) | Divides original data into multiple data blocks and generates a set of parity blocks. These data and parity blocks form an EC group distributed across different storage nodes. If some blocks are lost, the data can be recovered from the remaining blocks. EC involves data blocks (n) and parity blocks (m): Data blocks (n): The data is split into n data slices. Parity blocks (m): m parity blocks are computed from the n data blocks. The data blocks (n) and parity blocks (m) form an EC group, and each block is stored on a different server. If up to m blocks are lost, the EC algorithm can recover the missing blocks. The n+m configuration is adjustable and depends on the number of nodes in the cluster. For private cloud deployments, the recommended configuration is 8+3 (requiring 14 or more nodes). |
| Online EC policy modification | Supports modifying the EC policy online through the operations platform. Important After EC mode is enabled, you cannot switch back to three-way replication mode. Proceed with caution. |
| Node decommissioning | Supports decommissioning a host node without affecting data or applications. |
| Node scaling | You can dynamically add storage and front-end nodes to scale the overall service capacity. |
| Load balancing | When data size or workload becomes significantly imbalanced between partitions, the system automatically triggers partition splits and merges. The system then schedules the new partitions. During this automatic process, partitions may be briefly unavailable for a few seconds before recovering automatically. |

**Data processing and analysis**

Tunnel Service is an integrated service built on Tablestore that provides continuous data capture for both historical and incremental data. It offers distributed, real-time data consumption channels for incremental, full, and combined incremental-plus-full data streams. By creating a data channel for a table, you can easily process both historical and newly added data.

| Feature | Description |
|---|---|
|   | Unified full and incremental data channels: Tunnel Service provides not only incremental data consumption but also parallel processing for full data backfills and combined full-plus-incremental streams. |

| roduct Introduction·C d Storage | loud Defin Cloud Defined Storag |
|---|---|
| Tunnel Service |   |
|   | Ordered incremental data changes: Tunnel Service divides data into one or more logical partitions that can be consumed in parallel. Incremental data within each logical partition is ordered by write time, while data from different partitions can be consumed in parallel. |
|   | Consumption latency monitoring: Tunnel Service provides the recovery point objective (RPO) for client-side data consumption through the DescribeTunnel API and offers channel data consumption monitoring in the console. |
|   | Horizontally scalable data consumption: Tunnel Service provides automatic load balancing for logical partitions, which improves horizontal scaling and data consumption speed. |

**Data security and protection**

| Level | Description |
|---|---|
| Node-level | A single node failure does not affect the overall system. The service recovers automatically in less than one minute. |
| Data center-level | Tablestore supports active-standby disaster recovery with two clusters in the same city. The system asynchronously replicates data from the primary instance to a backup instance in a standby Tablestore cluster in the same city. If the primary data center fails (due to power outage, fire, etc.), data remains accessible. After a failover, the application can continue to access Tablestore without changing its endpoint. This same-city disaster recovery solution supports failover for multiple Tablestore clusters. Because data replication is asynchronous, some data may be lost if the primary cluster experiences a sudden failure before the data can be synchronized to the standby cluster. |
| Region-level | Tablestore provides two region-level disaster recovery solutions: three data centers in two regions and active-standby disaster recovery with two clusters in different regions. Active-standby disaster recovery with two clusters in different regions: The system asynchronously replicates data from the primary instance to a backup instance in a standby Tablestore cluster in a different region. If the primary data center fails, data access is maintained. After a failover, the application must change its Tablestore endpoint. Because data replication is asynchronous, some data may be lost if the primary cluster experiences a sudden failure before the data can be synchronized to the standby cluster. Three data centers in two regions: If your business has higher data backup requirements, you can build on the same-city dual-cluster disaster recovery solution by adding a standby cluster in a different region and using asynchronous data replication to implement a disaster recovery architecture with three data centers in two regions. |
| Software system- level | If a process in the system terminates unexpectedly due to a software defect, the service recovers automatically in less than one minute. |

**Deployment requirements**

A Tablestore cluster deployment requires a minimum of six nodes.

#### Hybrid Disaster Recovery

This topic describes the features of Hybrid Disaster Recovery.

**Basic Features**

| Feature | Description |
|---|---|
| Cross-zone disaster recovery | When a production site's application cannot recover quickly due to force majeure (such as data center fires or power outages) or device failures (software or hardware damage), the disaster recovery service supports cross- zone disaster recovery for business applications. It performs disaster recovery and backup for the entire application to handle single-region failures, meeting the core RTO/RPO metrics for the business. |
| Cross-region disaster recovery | Cross-region disaster recovery involves deploying a production site and a disaster recovery site in two different regions. If the production site fails, the business system quickly switches to the disaster recovery site, ensuring business continuity and high availability. |
| Cross-cloud disaster recovery | Cross-cloud disaster recovery means the production cloud and disaster recovery cloud are two cloud instances deployed off-site. If the production cloud fails, the business system switches to the disaster recovery cloud. This effectively prevents system failures caused by instance failures, ensures business availability, and meets the core RTO/RPO metrics for the business. |
| Failover | Failover after data synchronization This failover first stops the protected instances in the protection group. It then waits for all protected instances to stop before performing the final round of data synchronization. After data synchronization completes, it initiates the failover. This ensures complete data consistency between the disaster recovery site and the production site, with no data loss. This failover mode applies to scenarios such as planned disaster recovery drills and business migration. Switch now This failover attempts to stop the protected instances in the protection group. It does not wait for all protected instances to stop, nor does it perform the final round of data synchronization. Some data loss may occur within the RPO. This failover mode applies to scenarios where the production site experiences a short-term unrecoverable failure and requires immediate failover to the disaster recovery site. |

| Fault recovery | Switchover after data synchronization This failback stops the protected instances in the protection group and waits for all protected instances to stop. It then performs the final round of data synchronization. After data synchronization completes, it initiates the failback. The service unavailability time will be longer than that of immediate failover. This is mainly used in scenarios where the production site is operating normally. Switch immediately. This failback attempts to stop the protected instances in the protection group. However, it does not wait for all protected instances to stop, nor does it perform the final round of data synchronization. Initiating failback immediately may result in some data loss. This is mainly used in scenarios where the disaster recovery site experiences a short-term unrecoverable failure, requiring immediate business recovery to the production site. |
|---|---|
| Alerting feature | It supports status monitoring for production sites, disaster recovery sites, protection groups, and security group policies, and reports alert information. This ensures the stable operation of disaster recovery services. |
