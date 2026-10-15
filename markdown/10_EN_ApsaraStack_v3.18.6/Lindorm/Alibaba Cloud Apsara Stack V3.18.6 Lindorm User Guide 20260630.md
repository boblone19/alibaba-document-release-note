---
title: "Lindorm User Guide 20260630"
product_version: "V3.18.6"
pdf_pages: 49
source_pdf: "Alibaba Cloud Apsara Stack V3.18.6 Lindorm User Guide 20260630.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/v3.18.6%E7%89%88%E6%9C%AC%E6%96%87%E6%A1%A3/Lindorm/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.6%20Lindorm%20User%20Guide%2020260630.pdf"
converter: line-classifier (PyMuPDF)
---

# Lindorm User Guide 20260630

## What is Lindorm?

Lindorm is a cloud native multi-model database service that allows you to store data of all sizes. Lindorm provides low-cost storage for large volumes of data. Lindorm supports wide table models and is compatible with the standard APIs of multiple open source services, such as Apache HBase, OpenTSDB, and SQL. Lindorm provides databases that are suitable for scenarios such as the Internet, Internet of Things (IoT), Internet of Vehicles (IoV), advertising, social networking, monitoring, gaming, and risk control scenarios. Lindorm provides technical support for the core business of Alibaba Group. Lindorm uses a cloud native multi-model architecture in which computing is decoupled from storage. Lindorm provides benefits such as elasticity, cost-effectiveness, ease of use, high compatibility, and high stability. It allows you to store and analyze data such as metadata, logs, bills, tags, messages, reports, dimension tables, result tables, feeds, user personas, device data, monitoring data, sensor data, small files, and small pictures. Lindorm provides the following core capabilities: Data interoperability: Lindorm supports wide table models. It provides a unified API and also supports the APIs of multiple open source database management systems. Data can be transferred and synchronized between models. This makes application development more agile, flexible, and efficient. Cost-effectiveness: Lindorm can handle tens of millions of concurrent requests and respond with a latency of a few milliseconds. Lindorm greatly reduces the storage cost by using high-density and cost-effective media, automatic cold and hot data separation, and adaptive compression. Cloud-native support and high scalability: Lindorm allows you to scale computing and storage resources separately. Lindorm also provides serverless services that you can scale based on actual usage. Open data ecosystem: Lindorm provides multiple simplified management capabilities such as data exchanges, processing, and subscription. It can be seamlessly integrated with systems such as MySQL, Spark, Flink, and Kafka.

**Multi-modal capabilities**

Lindorm supports wide table models and Lindorm Tunnel Service (LTS). It provides a unified API and supports the APIs of multiple open source database management systems. Data can be transferred and synchronized between models. This makes application development more agile, flexible, and efficient. The core multi-model capabilities are provided by LindormTable. LindormTable is used to store large amounts of key-value data and table data. It provides global secondary indexes, multi-dimensional queries, dynamic columns, and Time to Live (TTL). It is applicable to scenarios such as metadata storage, orders, bills, user personas, social networking information, feeds, and logs. LindormTable is compatible with the open standards of multiple types of open source software, such as Apache HBase. LindormTable supports tens of millions of concurrent requests, separation of cold and hot data, and hundreds of petabytes of data storage. Compared with the performance delivered by open source Apache HBase, the throughput is increased by 2 to 6 times, the percentile 99% (P99) latency is reduced by 90%, the mean time to repair (MTTR) is reduced by 90%, the data compression ratio is increased by 100%, and the comprehensive storage cost is reduced by 50%.

## LTS

LTS provides easy-to-use capabilities, including data exchange, processing, and change tracking. You can use these capabilities to migrate data, track real-time data changes, dump data to data lakes, and synchronize data from data warehouses to Lindorm databases. You can also use these capabilities to back up and restore data, and implement multi-active redundancy based on units. This way, LTS provides an all-in-one data ecosystem service for Lindorm. A combination of HBase and Elasticsearch or a combination of HBase, OpenTSDB, and Elasticsearch is used in some scenarios, such as monitoring, social networking, and advertising. In such cases, you may face multiple pain points, such as complex architectures, complex queries, weak consistency, high cost, and misalignment of features. The cloud native multi-model capabilities of Lindorm can help you resolve these pain points to ensure efficient innovations.

## Getting started with

**Lindorm**

### Log on to the ApsaraDB for

**Lindorm console**

This topic describes how to log on to the ApsaraDB for Lindorm console.

**Prerequisites**

The URL of the Apsara Uni-manager Management Console is obtained from the deployment personnel before you log on to the Apsara Uni-manager Management Console. A browser is available. We recommend that you use the Google Chrome browser.

**Procedure**

1. In the address bar, enter the URL of the Apsara Uni-manager Management Console. Press
the Enter key.
2. Enter your username and password.
Obtain the username and password that you can use to log on to the console from the operations administrator.

**Note**

When you log on to the Apsara Uni-manager Management Console for the first time, you must change the password of your username. Your password must meet complexity requirements. The password must be 8 to 20 characters in length and must contain at least two of the following character types: Uppercase or lowercase letters Digits Special characters, which include ! @ # $ %
3. Click **Login**.
4. If multi-factor authentication (MFA) is enabled for your account, perform the following
operations based on your login scenario: You log on to the Apsara Uni-manager Management Console for the first time after MFA is enabled by the administrator. a. On the Bind Virtual MFA Device page, follow the on-screen instructions to bind an MFA device. b. Enter the username and password again as in Step 2 and click **Log On**. c. Enter the six-digit MFA code and click **Authentication**. You have enabled and bound MFA: Enter the six-digit MFA code and click **Authentication**.

**Note**

For more information about how to bind and enable MFA, see **Security Center** >
**MFA** > **Manage MFA** in Apsara Uni-manager Operations Console User Guide.

| Section | Paramete r | Description |
|---|---|---|
| Basic configurat ion | Organizat ion | The organization to which the instance belongs. |
|  | Resource Set | The resource set to which the instance belongs. |
| Area | Geograph y | The region in which you want to create the instance. Services in different regions cannot communicate over an internal network. After the instance is created, the region cannot be changed. |
|  | Zone | The zone in which the instance is deployed. |

5. In the top navigation bar, click **Products**, then click **ApsaraDB for Lindorm** in the
**Database Services** section.

### Create a Lindorm instance

This topic describes how to create a Lindorm instance in the Lindorm console.

**Prerequisites**

An Apsara Stack tenant account is created.

**Procedure**

1. Log in to the Lindorm console.
2. On the **Instances** page, click **CreateLindorm**.
3. Configure the parameters described in the following table.

| Network Configura tion | IP Type | IPv4: assigns an IPv4 address to the instance. This option is suitable for IPv4 networks. IPv4/v6 Dual-Stack: assigns IPv4 and IPv6 addresses to the instance. This option is suitable for hybrid networks in which both IPv4 and IPv6 clients need to access the instance. If you select this option, you must configure an IPv6 address whitelist to specify the IPv6 addresses that can access the instance. Note To configure this parameter, you must turn on the IPv6 display switch first. For more information, see the Turn on the IPv6 display switch topic in the O&M Guide. If the system prompts that you are not authorized, see Authorize a tenant organization to access SLB. |
|---|---|---|
|  | VPC | The ID of the virtual private cloud (VPC) where you want to deploy the instance. |
|  | VSwitch | The ID of the vSwitch where you want to deploy the instance. |
| Basic Specificati on Configura tion | Instance name | The name of the Lindorm instance. The name must be 2 to 128 characters in length. It must start with a letter. The name can contain digits, letters, underscores ( ), and hyphens _ (-). |
|  | Chip Architect ure | The chip architecture of the Lindorm instance is determined by the deployment environment. |
|  | Storage Type | The storage type of the Lindorm instance. Valid value:L ocal HDD disk. Local HDD disk: A local HDD is attached to a single physical server. Local HDDs provide multiple benefits, such as low latency, high IOPS, high throughput, and high cost-effectiveness. Local HDDs are the preferred storage media for industries such as the Internet and finance, which have high requirements for big data computing, storage, and analysis. Local HDDs are suitable for the storage and offline computing of large amounts of data. |

|  | Disk Size | The size of the local disk. The specifications are obtained from the configuration parameters of the business plan. The specifications may differ from the actual disk model and may occupy the disk exclusively. If the actual disk size is larger than this value, the actual available size is the size of the disk. |
|---|---|---|
|  | Number of disks per node | The number of disks per node. Important The instance uses a three-replica architecture. The available storage can be calculated by using the following formula: Available storage = Number of disks per node × Disk size × (Node data volume/3). The following storage calculation formula is used: Total instance storage = Disk size × Security threshold 0.85/Number of replicas 3 × Number of disks per node (n) × Total number of nodes for all engines (m). For example, if the disk size is 6 TB, the number of disks per node is 10, and 3 wide table engines are used, then the total storage capacity of the instance = 6 TB × 0.85/3 × 10 × 3 = 51 TB. |
| Multi- Mode Engine Configura tion | Wide Table Engine | Select the specifications of LindormTable. The following specifications are supported: lindorm.g1.8c32g lindorm.g1.16c64g lindorm.g1.32c64g lindorm.g1.32c128g |
|  | Number of Wide Table Engine Nodes | The number of LindormTable nodes in the instance. The number of nodes ranges from 2 to 20. |

4. Click **Confirm Order**.

### Configure a whitelist

This topic describes how to configure a whitelist for a Lindorm instance. Before you use a Lindorm instance, you must add the IP addresses or CIDR blocks to an instance whitelist to allow access from those addresses. This improves database security and stability. A properly configured whitelist can enhance the security of your instance. We recommend that you perform regular maintenance on your whitelists.

**Background information**

The system creates a default whitelist for each instance. This whitelist can be modified or cleared, but cannot be deleted. After a Lindorm instance is created, the system automatically adds the IP address 127.0.0.1 to the **default** whitelist of the instance. The IP address 127.0.0.1 indicates that no IP addresses are allowed to access the instance.

**Procedure**

| Parameter | Description |
|---|---|
| Group name | The group name must be 2 to 32 characters in length. It can contain lowercase letters, digits, and underscores ( ) and must start with a _ lowercase letter and end with a lowercase letter or a digit. |
| Type | You can select IPv4 or IPv6. |
| Whitelist within a group | Take note of the following requirements when you add IP addresses to the whitelist: Separate multiple IP addresses with commas (,). A maximum of 1,000 unique IP addresses can be added. You can specify IP addresses in the following formats: IPv4: 10.23.12.24 (specific IPv4 address) or 10.23.12.24/24 (CIDR block with a prefix length ranging from 1 to 32). IPv6: 2001:db8::1 (specific IPv6 address) or 2001:db8::/32 (CIDR block with a prefix length ranging from 1 to 128). Note If you enter a CIDR block whose prefix length is 0, such as 0.0.0.0/0 or ::/0, all IP addresses are allowed to access the instance. This poses a high security risk. Proceed with caution. Examples Allow a single IPv6 address: 2001:db8:85a3::8a2e:370:7334 Allow an IPv6 CIDR block: 240e:390:a100::/44 Allow all IP addresses (high risk): ::/0 or 0.0.0.0/0 |
| Import file (.txt) | You can import IP addresses in batches. |

1. Log in to the Lindorm console.
2. On the **Instances** page, find the instance that you want to manage. Then, click the
instance ID or click **Manage** in the **Actions** column.
3. In the left-side navigation pane of the **Instance Details** page, click **Whitelist**.
4. Click **Add a whitelist Group** in the upper-left corner.
5. In the **New name adding list groups (up to 50 groups supported)** panel, configure
the following parameters.

| Load the private IP addresses of ECS instances | i. Select Import ECS Internal IP Address. ii. Select IP addresses based on your business requirements. Note To find the Elastic Compute Service (ECS) instance to which a specific IP address is assigned, you can move the pointer over the IP address. Then, the system displays the ID and name of the ECS instance to which the IP address is assigned. |
|---|---|

| Section | Parameter | Description |
|---|---|---|
| Basic configurat ion | Organizati on | The organization to which the instance belongs. |
|  | Resource Set | The resource set to which the instance belongs. |
|  | Instance name | The name of the LTS instance. The name must be 2 to 128 characters in length. It must start with a letter. The name can contain letters, digits, and the following special characters: - _ |
| Area | Geograph y | The region where the instance resides. Services in different regions cannot communicate over an internal network. After the instance is created, the region cannot be changed. |
|  | > Document Version: 2026063 |  |

6. Click **OK**.

### Create an LTS instance

Lindorm Tunnel Service (LTS) is a data ecosystem service that is customized based on the characteristics of Lindorm business scenarios. This topic describes how to create an LTS instance in the Lindorm console.

**Prerequisites**

An Apsara Stack tenant account is created.

**Procedure**

1. Log on to the Lindorm console.
2. On the **Instances** page, click **CreateLTS**.
3. Configure the parameters described in the following table.

| dorm | User Guide·Getting started with indorm |  |
|---|---|---|
|  | Availabilit y Zone | The zone in which the instance is deployed. |
| Specificati on Configura tion | Chip Architectu re | Select the chip architecture of the LTS engine. |
|  | Data Channel Service Specificati ons | Select the specifications of the LTS engine. |
|  | Number of specificati on nodes | The number of LTS engine nodes that are created. Note You must specify this parameter. Valid values: 1 to 20. |

4. Click **Submit**.
t

## Instance management

### View the endpoint of a

**Lindorm instance**

This topic describes how to view the endpoint of a Lindorm instance.

**Procedure**

1. Log in to the Lindorm console.
2. On the **Instances** page, find the instance that you want to manage. Then, click the
instance ID or click **Manage** in the **Actions** column.
3. In the left-side navigation pane of the **Instance Details** page, click **Database**
**Connection**.
4. On the **Database Connection** page, select the engine that you want to manage to view
the endpoint and port.

**Note**

You can also turn on the IPv6 switch on the right side of an endpoint to connect to a database by using an IPv6 address.

### Activate a classic network

**endpoint**

This topic describes how to activate the classic network endpoint of a Lindorm instance.

**Procedure**

1. Log on to the Lindorm console.
2. On the **Instances** page, find the instance that you want to manage. Then, click the
instance ID or click **View Instance Details** in the **Actions** column.
3. In the left-side navigation pane, click **Database Connections**.
4. Click the **Wide Table Engine** tab based on your business requirements.
5. Click **Activate the classic network address**.

**Note**

The **Activate the classic network address** button appears only when the instance is in the **Running** state.
6. In the **Activate the classic network address** message, click **OK**.

### Release an instance

If you no longer need a Lindorm instance, you can release the instance. This topic describes how to release a Lindorm instance. t

**Procedure**

1. Log on to the Lindorm console.
2. On the **Instances** page, find the instance that you want to manage and click **Release** in
the **Actions** column.
3. In the message that appears, click **OK**.

**Warning**

After an instance is released, all data in the instance is deleted. Exercise caution when you release an instance.

### Version update

This topic describes how to upgrade a Lindorm instance and how to upgrade a Lindorm Tunnel Service (LTS) instance.

**Upgrade a Lindorm instance**

1. Log on to the Lindorm console.
2. On the **Instances** page, click the ID of the instance that you want to manage or click
**Manage** in the **Actions** column corresponding to the instance.
3. In the **Configurations** section of the **Instance Details** page, find the engine that you
want to manage.
4. Choose **Manage > Upgrade Minor Version**.

**Note**

The **Upgrade Minor Version** button appears only when a new version is available. The button does not appear when the current version is the latest.
5. In the **Upgrade Minor Version** dialog box, click **OK**.

**Note**

The system performs a rolling upgrade on a cluster to ensure that the Lindorm service is not interrupted during the upgrade. Before a region server restarts, the system moves all regions to other region servers to minimize the impact on your workloads. The upgrade may cause network jitter. However, the entire Lindorm cluster remains available. You can perform minor version upgrades based on your business requirements. The amount of time that is required to upgrade the minor version of a Lindorm cluster varies based on the size of the cluster and the number of regions in the cluster. A larger cluster requires more time to upgrade the minor version.

**Upgrade an LTS instance**

1. Log on to the Lindorm console.
2.
3. In the **LTS Node Information** section of the **Instance Details** page, choose **Manage >**
**Upgrade Minor Version**.
t

**Note**

The **Upgrade Minor Version** button appears only when a new version is available. The button does not appear when the current version is the latest.

### Restart an engine

This topic describes how to restart an engine of a Lindorm instance.

**Procedure**

1. Log on to the Lindorm console.
2. On the **Instances** page, click the ID of the instance that you want to manage or click
**Manage** in the **Actions** column corresponding to the instance.
3. In the **Configurations** section of the **Instance Details** page, find the engine that you
want to manage.
4. Find the engine that you want to manage, and choose **Manage > Restart Engine** on the
right side.
5. In the **Restart Engine** message, click **OK**.

### Scale nodes

This topic describes how to change the number of nodes for an engine of a Lindorm instance.

**Procedure**

1. Log on to the Lindorm console.
2. On the **Instances** page, click the ID of the instance that you want to manage or
click **Manage** in the **Actions** column corresponding to the instance.
3. In the **Configurations** section of the **Instance Details** page, find the engine that you
want to manage.
4. Find the engine that you want to manage and choose **Manage > Change node**
**configuration** on the right side.
5. On the **Lindorm node change** page, specify **Number of engine nodes**.

**Note**

The number of nodes ranges from 2 to 20.
6. Click **Submit**.

## LindormTable

### Overview

LindormTable is a wide table engine service provided by Lindorm to allow you to store large amounts of semi-structured and structured data in distributed storage. LindormTable can store various types of data, such as metadata, orders, bills, profiles, social networking information, feeds, and logs. LindormTable is compatible with standard APIs of open source software and services such as Apache HBase. LindormTable supports hundreds of trillions of rows in a single table, tens of millions of concurrent queries per second (QPS), responses to queries within milliseconds, and disaster recovery that ensures strong consistency across data centers. LindormTable can meet the business requirements for the storage and query of large amounts of data.

**Cost-effectiveness**

Lindorm implements technologies such as high-density low-cost media, intelligent cold and hot data separation, high compression ratio algorithm, and adaptive coding. The storage and processing costs for massive data are 80% lower than self-managed engines.

**Enterprise-grade stability**

LindormTable is built on top of a high-availability architecture and provides enterprisegrade stability. This architecture has demonstrated high stability in the production environment of Alibaba Group for more than a decade.

**High compatibility**

LindormTable is compatible with various open source standard APIs such as Apache HBase. LindormTable can connect to compute engines such as Spark and Flink. This way, LindormTable can be seamlessly integrated into mainstream data ecosystems. For more information about LindormTable, see the benefits section of Lindorm product introduction.

**Typical scenarios**

**Big data**

Lindorm allows you to store a large amount of data at a low cost, import datasets in batches, and access data in real time. Lindorm provides efficient data channels to import incremental data and full data. Lindorm can be integrated with big data platforms such as Spark to enable offline analysis on large amounts of data.

| App Journal Sensor RDS Data So | User User Real-time Details Query Analysis Re Highly Concurrent Data Writing Online Interactive Data Analysis Lindorm DLA Lindorm Cold Data Incremental Data Synchronization Batch Backflow of Ana OSS Spark-based Big Data Analytics urce |
|---|---|

| Highly C | oncurrent Data Writ | ing |
|---|---|---|
|  | Lindorm |  |

Benefits Cost-effectiveness: Lindorm supports high compression ratios, cold and hot data separation, and data storage in HDD disks and Object Storage Service (OSS). Tunneled data transmission: Lindorm allows you to use Lindorm Tunnel Service (LTS, former BDS) to synchronize data between Lindorm and third-party systems in a simple and efficient manner. Bulk import: Lindorm allows you to import a large amount of data to Lindorm by using BulkLoad. This makes data transmission faster than that of traditional methods. High concurrency: Lindorm provides horizontal scaling to reach tens of millions of QPS. Scalability: Lindorm uses a decoupled storage and computing architecture. This enables independent auto scaling.

**Finance and retail**

You can use Lindorm to store a large number of transaction records in the financial and retail industries. Lindorm can also be used to store important financial risk control information, such as user activities, user personas, rule-based models, and device fingerprints. Lindorm supports high concurrency and provides cost-effective, flexible, and reliable services. It allows you to create competitive services for transaction management and financial risk control.

| Data U | ploadin |
|---|---|

| Rule-ba | sed Mode |
|---|---|

Real-time Data Sending Transaction Query Financial Users Real-time Data Sending Advertiser Historical Transactions Behavior Logs (Logon and Payment) Risk Control & D Event Data Behavior Analysis Crawler-based Data Fetching Other Information Application Servers Model Patterns

**Benefits**

Cost-effectiveness: Lindorm supports high compression ratios, cold and hot data separation, and data storage in HDD disks and OSS. High concurrency: Lindorm provides horizontal scaling to reach tens of millions of QPS. Flexibility: Lindorm supports dynamic columns and the Time to Live (TTL) mechanism. Features or tags can be automatically added to or removed from dynamic columns. Data automatically expires based on the TTL setting. Low latency: Lindorm supports instant responses within milliseconds and allows you to deploy clusters in primary/secondary mode. Each request is sent to multiple replicas for concurrent processing. This accelerates data queries. Tunneled data transmission: Lindorm allows you to use LTS (former BDS) to synchronize data between Lindorm and third-party systems in a simple and efficient manner. High availability: Lindorm supports active-standby or active-active disaster recovery and automatic failovers to ensure a service uptime of 99.95%.

**Internet of Vehicles (IoV)**

You can use Lindorm to store important data such as driving trajectories, vehicle status, and precise positioning data in IoV scenarios. Lindorm provides scalable, reliable, and costeffective services. It allows you to create services for online ride-hailing, logistics, and new energy vehicle detection.

| Cars Coaches Trucks |  | Application Servers ploading | Position-based Vehicle GeofReindceing & Tra Hailing Vehicle StatusLindorm Vehicle Status QueryR &ea Rl-etaiml-tieme Al Trajectories Vehicle Accurate Positioning Monitoring Spark-based Big BI Reports Lindorm Enterprise RSetpaotritsstical Data Analytics Driving AnaAlynsaislytics |
|---|---|---|---|
|  | Data U |  |  |

| cle GeofReindceing & Tr | a |
|---|---|

|  | le StatusLindorm ectories |  |
|---|---|---|
| Vehicle StatusLin Trajectories Accurate Positioning | le StatusLin ectories |  |
|  |  | g |

|  | ise RSetpaotritsstical g AnaAlynsaislytics |
|---|---|
| Enterpr Drivin | ise RSetpaotritsst g AnaAlynsaisly |

**Benefits**

Cost-effectiveness: Lindorm supports high compression ratios, cold and hot data separation, and data storage in HDD disks and OSS. Scalability: Lindorm uses a decoupled storage and computing architecture. This enables independent auto scaling. Flexibility: Lindorm supports dynamic columns and the TTL mechanism. Features or tags can be automatically added to or removed from dynamic columns. Data automatically expires based on the TTL setting. Low latency: Lindorm supports instant responses within milliseconds and allows you to deploy clusters in primary/secondary mode. Each request is sent to multiple replicas for concurrent processing. This accelerates data queries. Tunneled data transmission: Lindorm allows you to use LTS (former BDS) to synchronize data between Lindorm and third-party systems in a simple and efficient manner. High availability: Lindorm supports active-standby or active-active disaster recovery and automatic failovers to ensure a service uptime of 99.95%.

**Online social networking**

You can use Lindorm to store important data such as messages, comments, posts, and likes in social networking scenarios. Lindorm features high availability, low latency, and ease of use. It allows you to develop a high-performance and reliable system for managing social networking feeds.

| Phone PC WEB |  |  |  |  | Feeds DLaintadorm |  |
|---|---|---|---|---|---|---|
|  |  |  |  |  | es, Posts, and App Feeds |  |
|  | Feeds Conten | t & Social Relations Application |  |  |  |  |
|  |  |  | Images, Docu | Images, Docu | mentation, and Sho | rt Videos |
|  |  |  |  |  | OSS |  |

Obtain feeds User Obtain ima CDN

**Benefits**

High availability: Lindorm supports active-standby or active-active disaster recovery and automatic failovers to ensure a service uptime of 99.95%. Low latency: Lindorm supports instant responses within milliseconds and allows you to deploy clusters in primary/secondary mode. Each request is sent to multiple replicas for concurrent processing. This accelerates data queries. Cost-effectiveness: Lindorm supports high compression ratios, cold and hot data separation, and data storage in HDD disks and OSS. Scalability: Lindorm uses a decoupled storage and computing architecture. This enables independent auto scaling.

**Connection methods**

Use Lindorm SQL to connect to LindormTable. Lindorm SQL provides an excellent developer experience. We recommend that you use this method. Use the Apache HBase API to connect to LindormTable. This method is suitable for applications that are developed based on Apache HBase. LindormTable allows you to use multiple connection methods to access a wide table at the same time. You can use one of the preceding methods to access the same data table.

### Connect to LindormTable

If you want to use LindormTable SQL client to connect to a Lindorm instance, you must obtain an endpoint that can be used to connect to the instance, the corresponding username, and the corresponding password. This topic describes how to obtain the endpoint.

**Obtain the endpoint**

1. Log on to the Lindorm console.
2. Click the ID of the instance that you want to manage to go to the **Instance Details** page.
3. In the left-side navigation pane, click **Database Connections**. The **Wide Table Engine**
tab appears by default. On this tab, view Lindorm wide table SQL address.

**Note**

Lindorm instances support access over Virtual Private Cloud (VPC) and over the classic network. The private endpoint of a Lindorm instance is used to connect to the instance over a VPC and can be obtained from the Lindorm console. The classic network endpoint of a Lindorm instance is used to connect to the instance over the classic network and can be obtained only after you apply for it.

| Module | Page | Description |
|---|---|---|
| Dashboard | N/A | You can view the basic information and space usage of the cluster. |
| Data management | Namespace management | You can view all namespaces in the cluster and centrally manage the namespaces. |
|  | Table management | You can view all tables in the cluster and the attributes of the tables. You can click the name of a table to view the details. |
|  | User management | You can view the users of the cluster and the permissions that the users have. You can add users, change the passwords of users, and delete users. |
|  | ACL management | You can manage the permissions of the users of the cluster. You can grant permissions to users or revoke permissions from users. |
| Data query | N/A | You can query the information about a table by using an SQL statement. |

### Cluster management

#### Cluster management system

You can use the cluster management system to view the resource usage of a Lindorm cluster and centrally manage data stored in the cluster. This topic describes the pages in the cluster management system.

**Prerequisites**

A Lindorm instance is created. For more information, see Create a Lindorm instance.
1. Log on to the Lindorm console.
2. On the **Instances** page, find the instance that you want to manage. Then, click the
instance ID or click **View Instance Details** in the **Actions** column.
3. In the left-side navigation tree, choose **Wide Table Engine > Cluster Management**.
4. In the **UI Access** section, click **ClusterManager** to go to the cluster management system.
The cluster management system consists of the dashboard, data management, and data query modules. The following table describes the pages in each module.

#### Grouping management

Lindorm provides a grouping feature, which allows you to create groups to isolate tenants. You can add region servers to different groups, and each group hosts different tables. This way, resources are isolated. This topic describes how to use the cluster management system to manage groups.

**Background information**

**Bacgoud**

**o**

**a**

**o**

When multiple users or applications share a Lindorm cluster, the users or applications may compete for resources. The read and write operations performed by business-critical online applications may be adversely affected by the bulk read and write operations performed by offline applications. To resolve this issue, you can create groups. The following figure shows an example on how to create groups to isolate resources. In this example, RegionServer1 and RegionServer2 are added to Group1 and RegionServer3 and RegionServer4 are added to Group2. Table1 and Table2 are moved to Group1. All regions of Table1 and Table2 are distributed to RegionServer1 and RegionServer2 in Group1. All regions of Table3 and Table4 are distributed to RegionServer3 and RegionServer4 in Group2. As a result, requests sent to Table1 and Table2 are processed only by RegionServer1 and RegionServer2, and requests sent to Table3 and Table4 are processed only by RegionServer3 and RegionServer4. This way, resources are isolated.

**View group information**

In the left-side navigation pane of the cluster management system, click **Dashboard**. In the
**Cluster group** section, you can view the information about all groups of the current cluster.
If you have not created a group, the system automatically creates a group named default. All RegionServers and tables belong to the default group. For more information about how to log on to the cluster management system, see Cluster management system.

**Create a group**

1. Log on to the cluster management system of Lindorm. For more information, see Cluster
management system.
2. In the left-side navigation pane of the cluster management system, click **Dashboard**.
3. In the **Cluster group** section, choose **More > Create group**.
4. In the **Create Group** dialog box, specify **GroupName**.
5. Click **OK**.

**Note**

By default, no region servers or tables are added to a group when a group is created. You must manually add region servers and tables to the group.

**Delete a group**

A group can be deleted only after all region servers and tables are removed from the group.
1. In the left-side navigation pane of the cluster management system, click **Dashboard**.
2. In the **Cluster group** section, find the group that you want to delete and click **Delete** in
the **Action** column.
3. In the message that appears, click **OK**.

**Move a region server to a group**

By default, all region servers in a Lindorm cluster belong to the default group. Before you use region servers, you must manually add the region servers to the corresponding group.
1. In the left-side navigation pane of the cluster management system, click **Dashboard**.
2. In the **Cluster group** section, select the region servers that you want to use.
3. Click **Move group**.
4. In the **Move group of ldserver** dialog box, select **target group**.
5. Click **OK**.

**Note**

If you add a table to a group that does not contain region servers, the region of the table becomes inaccessible because no region server is available for the region. We recommend that you add at least two region servers to each group. When a region server is down, the regions of the tables in the group can be distributed to the other region server. If your group contains only one region server and the region server is down, all tables in the group become inaccessible. When you remove a region server from a group, the regions that are being accessed on the region server are distributed to other region servers in the group.

**Specify a group for a namespace**

If no group is specified for a namespace, all tables in the namespace belong to the default group.
1. In the left-side navigation pane of the cluster management system, choose **Data Manager**
**> Namespace Manager**.
2. On the **Namespace Manager** page, find the namespace that you want to manage and
click **Bind group** in the **Operation** column.
3. In the **Bind group** dialog box, specify **Target group**.
4. Click **OK**.

**Note**

If you change the group that is specified for a namespace, the change does not apply to the existing tables in the namespace. After you specify a group for a namespace, all newly created tables in the namespace are added to the group. You can also move the tables in the namespace to another group.

**Move a table to a group**

Do not move a table to a group that does not contain region servers. Otherwise, the table becomes inaccessible.
1. In the left-side navigation pane of the cluster management system, choose **Data Manager**
**> Table Manager**.
2. On the **Table** page, select the table that you want to move and click **Move Group**.
3. In the **Move Group** dialog box, specify **target group**.
4. Click **OK**.

#### Namespace management

Namespaces are logical groups for tables in Lindorm. You can use the same name for tables that belong to different namespaces. Lindorm provides a default namespace. If you do not specify a namespace, the system uses the default namespace. This topic describes how to use the cluster management system to manage namespaces.

**Create a namespace**

1. Log on to the cluster management system of Lindorm.
2. In the left-side navigation pane, choose **Data Manager > Namespace Manager**.
3. On the **Namespace Manager** page, click **Add**.
4. In the **AddNameSpace** dialog box, specify **namespace**.
5. Click **OK**.

**Delete a namespace**

1. In the left-side navigation pane of the cluster management system, choose **Data Manager**
**> Namespace Manager**.
2. On the **Namespace Manager** page, find the namespace that you want to delete and click
**Delete** in the **Operation** column.
3. In the message that appears, click **OK**.

**Note**

Before you delete a namespace, you must delete all tables in the namespace. Otherwise, you fail to delete the namespace.

**Specify a group for a namespace**

For information about how to specify a group for a namespace, see the Specify a group for a namespace section of the Grouping management topic.

#### User management

Lindorm supports user authentication. You need only to provide a username and password for user authentication. Your password is stored as ciphertext on the server and is transmitted as ciphertext during the authentication process. This way, passwords cannot be used or forged even if they are intercepted by unauthorized users. This topic describes how to use the cluster management system to manage users.

**Create a user**

1. In the left-side navigation pane of the cluster management system, choose **Data Manager**
**> User Manager**.
2. On the **User Manager** page, click **Add user**.
3. In the **Add user** dialog box, specify **Username** and **Password**.
4. Click **OK**.

| Type | Description | Statement |
|---|---|---|
| WRITE | Operations related to writing data to tables in Lindorm. | PUT, BATCH, DELETE, INCREMENT, APPEND, and CHECKANDMUTATE |
| READ | Operations related to reading data from tables in Lindorm. | GET, SCAN, and EXIST |
|  | Operations related to reading the descriptors and namespaces of tables in Lindorm. | GETTABLEDESCRIPTOR, LISTTABLES, and LISTNAMESPACEDESCRIPTORS |
| ADMIN | Data Definition Language (DDL) operations other than those related to deleting tables or table data. | CREATETABLE, ENABLETABLE, and DISABLETABLE |
|  | DDL operations related to namespaces. | CREATENAMESPACE |

**Note**

After you create a user, the password of the user cannot be viewed in the system. If you forget the password, you must change the password. A newly created user does not have permissions to access resources. You need to go to the Access Control page and grant permissions to the user so that the user can access resources.

**Change the password of a user**

1. In the left-side navigation pane of the cluster management system, choose **Data Manager**
**> User Manager**.
2. On the **User Manager** page, find the user that you want to manage and click **Change**
**password** in the **Operation** column.
3. In the **Change password** dialog box, specify **Username** and **New password**.
4. Click **OK**.

**Delete a user**

1. In the left-side navigation pane of the cluster management system, choose **Data Manager**
**> User Manager**.
2. On the **User Manager** page, find the user that you want to manage and click **Delete** in the
**Operation** column.
3. In the message that appears, click **OK**.

#### ACL-based permission management

This topic describes how to use the cluster management system to manage access control list (ACL)-based permissions.

**Permission types**

The following table describes the types of permissions that are supported by Lindorm and the statements that you can execute with the corresponding permissions.

| TRASH | Operations that can prevent users from accidentally deleting tables or table data. | TRUNCATETABLE and DELETETABLE |
|---|---|---|
| SYSTEM | O&M operations. The permissions are required if you use Big Datahub Service (BDS) to migrate and synchronize data that is stored in Lindorm. | COMPACT and FLUSH |

**Permission classification**

The following permission levels from high to low are defined to control access to Lindorm instances and the relevant resources: Global, Namespace, and Table. A higher level provides all permissions that are provided by a lower level. For example, if User 1 is granted the global read and write permissions, User 1 has the read and write permissions on all tables in all namespaces. If User 2 is granted the read and write permissions on Namespace 1, User 2 has the read and write permissions on all tables in Namespace 1, including newly created tables in Namespace 1.

**Grant permissions to a user**

You can use the ACL Management module of the cluster management system to grant permissions to a user. In this example, the read permissions on a table is granted to a user.
1. In the left-side navigation pane of the cluster management system, choose **Data Manager**
**> ACL Management**.
2. In the **Table permission** section, choose **More > grant privileges**.
3. In the **grant table privilege** dialog box, select an option from the **user name** drop-down
list, select a namespace from the **grant namespace** drop-down list, and then select a table from the **grant table** drop-down list.
4. Select READ in the **grant privileges** field.
5. Click **OK**.

**Revoke permissions from a user**

You can use the ACL Management module of the cluster management system to revoke permissions from a user. Each user can have multiple levels of permissions. In this example, the permissions on the Global level are revoked from a user.
1. In the left-side navigation pane of the cluster management system, choose **Data**
**Management > ACL Control**.
2. In the **Global permission** section, click **revoke** in the **Action** column of the user whose
permissions you want to revoke.
3. In the **revoke privilege** dialog box, select the permissions that you want to revoke.

**Note**

The **revoke privileges** dialog box displays all permissions that the user has on the Global, Namespace, and Table levels.
4. Click **OK**.

| The | ROW | fi |
|---|---|---|
| qualifier |  |  |

**Enable or disable the ACL feature**

**Note**

If you no longer need to use the ACL feature, you can disable the feature. After you disable the ACL feature, no username or password is needed for requests, including API requests, SQL requests, and non-Java requests. You can enable or disable the ACL feature without the need to restart the cluster. However, after you enable the ACL feature, if you reconnect your client to the cluster without providing your username and password, a user authentication error is returned. To pass user authentication in this scenario, reconnect your client to the cluster with your username and password.
1. In the left-side navigation pane of the cluster management system, choose **Data Manager**
**> ACL Management**.
2. Turn on or turn off **ACL**.
3. In the message that appears, click **yes**.

#### Data query

Lindorm allows you to query data stored in tables by executing SQL statements in the cluster management system. This topic describes how to use the cluster management system to query data in tables.

**Limits**

The cluster management system supports only the `SELECT` statement. To ensure data security, the cluster management system returns up to 100 entries for each query. To query varbinary data with conditions, you must use hexadecimal strings as values. The `ROW` and `COL` fields are reserved fields in SQL. When you use these fields in queries, you must enclose the fields in grave accents (`). When you specify a family for the `qualifier` field, you must also enclose the field in grave accents (`).

**Query data in a table**

1. In the left-side navigation pane of the cluster management system, choose **Data Query** >
SQL Executor.
2. On the **SQL Executor** page, select a namespace from the **namespace** drop-down list.
3. Select the name of the table that you want to query in the **Tables of current namespace**
list.
4. Enter an SQL statement in the SQL editor.
5. Click **Execute**.

**Note**

You can use the following shortcut keys to execute the SQL statement: Windows: CTRL + ENTER macOS: COMMAND + RETURN

**Obtain hexadecimal strings**

To query varbinary data with conditions, you must use hexadecimal strings as values. For example, to query data whose rowkey is r1, set the `WHERE` condition to `WHERE` `rowkey='7321'` in the SQL statement. The hexadecimal string of r1 is 7321. The Data Query page of the cluster management system provides a conversion tool for you to convert values to hexadecimal strings.
1. In the left-side navigation pane of the cluster management system, choose **Data Query** >
SQL Executor.
2. On the **SQL Executor** page, select a namespace from the **namespace** drop-down list.
3. Enter a binary string in the **Binary to hex string conversion** field.
4. View the hexadecimal string on the top of the SQL editor.
5. Use the hexadecimal string in a SQL statement.
6. Optional. Turn on **HexString** to view the query result when the hexadecimal string is used.
7. Click **Execute**.

## LindormTSDB

**Important**

Starting September 1, 2024, you can **no longer purchase LindormTSDB**. If you purchased LindormTSDB and migrated data to LindormTSDB by using TSDB before September 1, 2024, you can still use LindormTSDB as expected.

### Overview

#### Overview

Lindorm provides a **high-performance, cost-efficient, stable, and reliable** online time series engine named LindormTSDB. LindormTSDB provides multiple capabilities such as efficient data reading and writing, storage based on a high compression ratio, and time series data aggregation.

**Important**

You can **no longer purchase LindormTSDB** from September 1, 2024. Users who have purchased LindormTSDB or who want to migrate TSDB data to LindormTSDB can still use LindormTSDB.
**High performance**: LindormTSDB provides high write throughput. LindormTSDB is
developed by Alibaba Cloud and allows you to write time series data at a high concurrency.
**Data compression**: LindormTSDB provides built-in data compression capabilities.
LindormTSDB integrates the time series data compression algorithm developed by Alibaba Cloud and common data block compression algorithms to provide a compression ratio of up to 10:1.
**Time series indexing**: LindormTSDB provides built-in time series indexing capabilities.
These capabilities allow you to run multi-dimensional high-performance data queries based on tens of billions of time series in an efficient manner.
**Time series computing**: LindormTSDB provides an aggregation engine to deliver
powerful time series aggregation capabilities. The aggregation engine supports more than 10 core aggregation operators, more than 20 filling policies, and more than 10 interpolation algorithms.
**Elastic scaling**: LindormTSDB adopts a distributed architecture and supports online elastic
scaling to accommodate data storage and processing requirements of any scale.

**Scenarios**

LindormTSDB is widely used in industry scenarios such as **IoT, industrial IoT (IIoT), and**
**application performance management (APM)**. LindormTSDB allows you to write tens of
millions of time series data points in seconds and store data at a high compression ratio with low costs. LindormTSDB also provides various features, such as pre-downsampling, interpolation, multi-dimensional aggregate computing, and visualized query results. This way, LindormTSDB can meet your requirements for storing and processing large amounts of time series data. You can use SQL to connect to and use LindormTSDB. The following methods are supported: If you use Java to access LindormTSDB, see the **Use the JDBC driver for Lindorm to**
**connect to and use LindormTSDB** topic of **Connection guide** in **Lindorm Developer**
**Guide**.
If you use other programming languages to access LindormTSDB, see the **HTTP-based**
**SQL API** topic of **Connection guide** in **Lindorm Developer Guide**.
If you are a database administrator or a data analyst, see the **Use Lindorm-cli to connect**
**to and use LindormTSDB** topic of **Connection guide** in **Lindorm Developer Guide**.

#### Features

This topic describes the features of LindormTSDB.

**Efficient reading and writing for time series data**

LindormTSDB provides efficient and concurrent reading and writing capabilities. You can read millions of data points per second and write tens of millions of data points per second.

**Data writing**

You can use one of the following methods to write data to LindormTSDB: Use the INSERT statement of SQL. We recommend that you use Java Database Connectivity (JDBC) to connect to LindormTSDB if you choose this method. Use a compatible device to write data over the Message Queuing Telemetry Transport (MQTT) protocol. Use the InfluxDB line protocol to write data. Use the OpenTSDB API to write data. Use Prometheus to write monitoring data to the remote storage. You can execute SQL statements to query data or use the OpenTSDB API to query data. You can also use the data query feature in the Lindorm console to visualize the queried data based on data groups, downsampling, and spatial aggregation.

**Data management**

Time series data stored in different databases is isolated. You can execute SQL statements to specify the interval between time-based partitions and the time-to-live (TTL) values of data for these databases. For more information, see Manage databases. You can verify the identities of the users that want to access your time series data and check the permissions that the users have on the storage that stores the time series data. You can execute SQL statements or use the Lindorm console to manage the users in LindormTSDB and the permissions of these users. For more information, see User and permission management.

**Efficient time series data storage technologies**

Time series data compression LindormTSDB uses an efficient compression technology to reduce the average storage space occupied by each data point to 1 to 2 bytes. This reduces the overall storage usage by 90% and increases the speed of data writing.

**Computing capabilities for time series data**

| Feature | LindormTSDB | TSDB |
|---|---|---|
| APIs | LindormTSDB provides native SQL capabilities. LindormTSDB is compatible with most HTTP API operations that are provided by TSDB. LindormTSDB is compatible with the write line protocol of TSDB for InfluxDB®. | TSDB provides HTTP API operations that comply with the OpenTSDB style. TSDB can be used as remote storage for Prometheus. TSDB can work with external components to provide limited support for the SQL syntax. |
| SDKs | JDBC. For more information, see the Use the JDBC driver for Lindorm to connect to and use LindormTSDB topic of Connection guide in Lindorm Developer Guide. Java Native SDK. For more information, see the Tutorial: Use the Java Native SDK to connect to and use LindormTSDB topic of Connection guide in Lindorm Developer Guide. Compatible with TSDB SDK for Java. | Java SDK |

LindormTSDB provides various computing functions to allow you to process time series data. LindormTSDB supports multiple data processing operations, such as downsampling, data interpolation, and spatial aggregation, which allow you to perform complex queries.

**Monitoring & O&M**

LindormTSDB provides an O&M system that you can use to maintain your Lindorm instances. You can view the status, performance metrics, and storage usage of your instances in real time. You can also configure alert rules and alert notification methods. This way, you can identify resource bottlenecks at the earliest opportunity.

**Data security and cluster security**

LindormTSDB provides the following solutions to ensure the security of your data and Lindorm instances: LindormTSDB allows you to access your instances over virtual private clouds (VPCs) to ensure the security of the instances. LindormTSDB allows you to manage user permissions at the database level. This enables data access in a more fine-grained manner. By default, LindormTSDB creates multiple replicas of data to ensure data availability.

#### Comparison with TSDB

This topic compares the features provided by LindormTSDB and Time Series Database (TSDB). LindormTSDB is a next-generation time series engine that is developed based on TSDB. LindormTSDB is a new service that is developed by Alibaba Cloud and is compatible with most API operations that are provided by TSDB. The following table describes the similarities and differences between LindormTSDB and TSDB.

| Data models | Semi-structured time series table model | Time series data model that complies with the OpenTSDB style |
|---|---|---|
| Storage engine | A distributed time series storage engine that is developed by Alibaba Cloud | A key-value (KV) storage engine based on HBase |
| Precomput ing capabilitie s | LindormTSDB provides native support for continuous queries. LindormTSDB provides pre-downsampling capabilities for the storage engine. | Not supported. |
| Time-to- live (TTL) capabilitie s | LindormTSDB allows you to specify TTL values based on databases. | TSDB supports only global TTL configuration. You can clear only data and cannot clear the corresponding indexes. |
| Performan ce | LindormTSDB can be scaled up to write tens of millions of data points per second. | TSDB can be scaled up to write millions of data points per second. |
| Applicatio n scenarios | LindormTSDB can be widely used in IoT scenarios, Industrial Internet of Things (IIoT) scenarios, and the performance monitoring of enterprise applications. | TSDB is used for the performance monitoring of enterprise applications. |

### Getting started

#### Overview

This topic describes how to connect to LindormTSDB of Lindorm and provides references to help you use LindormTSDB.

**Important**

Starting September 1, 2024, you can **no longer purchase LindormTSDB**. If you purchased LindormTSDB and migrated data to LindormTSDB by using TSDB before September 1, 2024, you can still use LindormTSDB as expected.

**Process**

To create a Lindorm instance and use LindormTSDB, perform the following operations:
1. Create a Lindorm instance. For more information, see Create a Lindorm instance.
2. Optional. If you want to use a classic network endpoint to connect to LindormTSDB, apply
for the classic network endpoint first.
3. Connect to LindormTSDB. You can use three methods to connect to LindormTSDB. The
following table describes the methods, scenarios, and relevant references.

| Method | Scenario | References |
|---|---|---|
| Use LindormTSDB SDK for Java (recommended) | You connect to LindormTSDB from a high layer of a business model. This eliminates the need to develop applications for low- layer operations such as connection management and data format conversion. | For more information, see the Tutorial: Use LindormTSDB SDK for Java to connect to and use LindormTSDB topic of Connection guide in Lindorm Developer Guide. |
| Use a JDBC driver | The Java Database Connectivity (JDBC) API is used in the code of your application to connect to various heterogeneous databases. An object- relational mapping (ORM) framework for data access, such as MyBatis, is included in the code of your application. | For more information, see the Use the JDBC driver for Lindorm to connect to and use LindormTSDB topic of Connection guide in Lindorm Developer Guide. |
| Use Lindorm-cli | N/A | For more information, see the Use Lindorm-cli to connect to and use LindormTSDB topic of Connection guide in Lindorm Developer Guide. |

### O&M guide

#### Database management

##### Manage databases

This topic describes the concepts related to databases in LindormTSDB and the features that are provided by LindormTSDB for time series data. Each running LindormTSDB instance manages one or more databases. Data is isolated between databases. Each database stores one or more time series tables. The following figure shows LindormTSDB data layers. If you write the data of irrelevant projects to the same LindormTSDB instance, the data of each project is logically isolated to a large extent. In this case, we recommend that you store the data of each project in a separate database and grant required permissions on the databases to different users for access control. LindormTSDB allows users that have required permissions to access data across databases.

**Time series data management based on databases**

In LindormTSDB, a database is a collection of time series tables. You can store time series tables related to the same business in a separate database for data isolation. In addition, you can use the following features provided by LindormTSDB to manage data based on databases: Configure a time to live (**TTL**) for each database. When the time interval between the point in time indicated by the timestamp of time series data and the current time is longer than the configured TTL, the time series data is considered expired and is cleared by LindormTSDB.

**Important**

1. Timestamps of time series data can indicate event time or ingestion time:
Event time: indicates the point in time when an event that corresponds to time series data occurs. For more information about the timestamps that indicate event time, see the description of timestamp in **Data models** of **Lindorm**
**Developer Guide**.
Ingestion time: indicates the point in time when time series data is written to a database. The preceding TTL is configured based on **event time**.
2. If you configure a TTL for a database and the time interval between the point in time
indicated by the timestamp of the data that you want to write and the current time is longer than the TTL, the data can be written to the database. However, the data cannot be retrieved during subsequent queries.

**Database management by executing SQL statements**

LindormTSDB allows you to perform the following operations on a database by executing SQL statements: Create a database You can create a database in LindormTSDB. For more information about the SQL syntax used to create a database, see the **CREATE DATABASE** topic of **SQL syntax reference** in
**Lindorm Developer Guide**.

**Note**

By default, a user does not have permissions to access a database that is newly created. To perform operations on a new database, you must be granted corresponding permissions on the database. Delete a database You can delete a database in LindormTSDB. For more information about the SQL syntax used to delete a database, see the **DROP DATABASE** topic of **SQL syntax reference** in
**Lindorm Developer Guide**.
Modify the attributes of a database You can modify the attributes of a database in LindormTSDB. For example, you can change the TTL of a database in LindormTSDB. For more information about the SQL syntax used to modify the attributes of a database, see the **ALTER DATABASE** topic of **SQL syntax**
**reference** in **Lindorm Developer Guide**.
Query the attributes of a database You can query the attributes of a database in LindormTSDB. For more information about the SQL syntax used to query the attributes of a database, see the **DESCRIBE DATABASE** topic of **SQL syntax reference** in **Lindorm Developer Guide**.

#### User and permission management

This topic describes how access control is performed in LindormTSDB and how to manage users and permissions in LindormTSDB. Lindorm provides a multilayer access control system to ensure the security of enterprise-level applications. Access control is performed at the following layer: Engines at the logical layer: Access control is implemented for engines based on user authentication and permission verification.

**Enable the user authentication and permission verification**

By default, the user authentication and permission verification feature is **disabled** for LindormTSDB of a Lindorm instance. In this case, users can access LindormTSDB without user credentials regardless of the method that is used to access LindormTSDB. For an instance in the production environment, we recommend that you enable the user authentication and permission verification feature for LindormTSDB to improve security. You can use the following method to enable the feature by executing the ALTER SYSTEM statement: After you connect to LindormTSDB, execute the ALTER SYSTEM SET USER_AUTH=TRUE; statement to enable the user authentication and permission verification feature.

**Important**

After the user authentication and permission verification feature is enabled for LindormTSDB, user credentials are required for all subsequent requests. If you do not specify user credentials in a request, the request may fail the authentication. You must also specify user credentials when you execute the `ALTER SYSTEM` statement to enable the user authentication and permission verification feature. After the feature is enabled, some existing services may fail to be accessed. Therefore, we recommend that you carefully plan and fully evaluate the impacts before you enable the feature. After the user authentication and permission verification feature is enabled, you can execute the following ALTER SYSTEM statement to disable the feature: `ALTER`

```
SYSTEM SET USER_AUTH=FALSE;
```

To check whether the user authentication and permission verification feature is enabled for your instance, execute the following SHOW PARAMETER statement:

```
 SHOW PARAMETER USER_AUTH;
```

**Implement access control for LindormTSDB based on user**

**authentication and permission verification**

After the user authentication and permission verification feature is enabled, the username and password are required when you access LindormTSDB. In addition, you must have permissions on the object that you want to access when you write data to or query data from the object. Otherwise, data fails to be written or queried. This way, LindormTSDB can implement strict security control and isolate permissions for business access.

**Methods of including user credentials when you execute SQL**

**statements**

The methods of specifying the username and password when you connect to LindormTSDB vary based on business scenarios: Scenarios in which you use Lindorm-cli to connect to LindormTSDB For more information, see the **Use Lindorm-cli to connect to and use LindormTSDB** topic of **Connection guide** in **Lindorm Developer Guide**. Scenarios in which you use a Java Database Connectivity (JDBC) driver to build applications

| Permission name | Description |
|---|---|
| READ | Read permissions. To query data in tables, you must have read permissions on the tables. |

For more information, see the **Use the JDBC driver for Lindorm to connect to and use**
**LindormTSDB** topic of **Connection guide** in **Lindorm Developer Guide**.
Scenarios in which you call common API operations to execute SQL statements to build applications For more information, see the **Use the HTTP-based SQL API of LindormTSDB** topic of
**Connection guide** in **Lindorm Developer Guide**.
LindormTSDB allows you to execute SQL statements to perform the following operations for user management: Add a user For more information, see the **CREATE USER** topic of **SQL syntax reference** in **Lindorm**
**Developer Guide**.
Delete a user For more information, see the **DROP USER** topic of **SQL syntax reference** in **Lindorm**
**Developer Guide**.
Change the password of a user For more information, see the **ALTER USER** topic of **SQL syntax reference** in **Lindorm**
**Developer Guide**.
View existing users For more information, see the **SHOW** topic of **SQL syntax reference** in **Lindorm**
**Developer Guide**.

**Note**

After an instance is created, an initial user is created by default. The username and the password of the initial user are both root. You can log on to LindormTSDB as the initial user to create users that are required by other services and grant permissions to the users. To add other users after the user authentication and permission verification feature is enabled, you must log on as the root user.

**Warning**

We recommend that you change the password of the initial user immediately after the instance is created. Otherwise, security risks may occur. In LindormTSDB, permissions are classified into four types. The following table describes the four types of permissions.

| WRITE | Write permissions. To write data to tables, you must have write permissions on the tables. |
|---|---|
| ADMIN | Management permissions. To manage data objects in LindormTSDB, you must have administrative permissions on the data objects that you want to manage. |
| SYSTEM | System permissions. You must have system permissions to perform operations that may affect the entire instance. |

In addition, LindormTSDB allows you to grant permissions on specific resources to users or revoke the permissions from a user based on different business requirements. LindormTSDB allows you to grant and revoke permissions on the following resource scopes:

**GLOBAL**

You can grant and revoke permissions on all resources globally. If a user is granted one of the four types of permissions on all resources globally, the user can perform the corresponding operations on all data objects in LindormTSDB. For example, if a user is granted the READ permission on all resources globally, the user can query data in all time series tables in all databases. You can grant and revoke permissions on a specified database. If a user is granted a specific type of permissions on a database, the user can perform the corresponding operations on all data objects in the database. For example, if a user is granted the READ permission on a database named DB1, the user can query data in all time series tables in the database. LindormTSDB allows you to execute the GRANT statement to grant permissions to a user and execute the REVOKE statement to revoke permissions from a user.

**Important**

To grant permissions to a user or revoke permissions from a user, you must have the ADMIN permission on all resources globally. The permissions on the GLOBAL scope take precedence over the permissions on the DATABASE scope. If you are granted the READ permission on the GLOBAL scope, you can query time series tables in all databases. If you are granted the READ permission on the Database scope, you can query time series tables only in the database. The SYSTEM permission can be granted or revoked only on the GLOBAL scope.

**Permissions required to execute common SQL statements**

The following table describes the permissions required to execute common SQL statements.

**Note**

In the following table, ○ indicates that the permission is required, and × indicates that the permission is not required.

| SQL statement | GLOBAL |  |  |  | DATABASE |  |  | Remarks |
|---|---|---|---|---|---|---|---|---|
|  | READ | WRIT E | A D M IN | SYS TE M | R E A D | W R I T E | ADM IN |  |
| SELECT...FRO M... | ○ | × | × | × | ○ | × | × | - |
| INSERT INTO...VALUE S... | × | ○ | × | × | × | ○ | × | - |
| INSERT INTO...SELEC T... | ○ | ○ | × | × | ○ | ○ | × | The WRITE permission on the table to which data is inserted is required. The READ permission on the table from which data is queried is required. |
| DESCRIBE DATABASE ... | × | × | ○ | × | × | × | ○ | - |
| CREATE DATABASE... | × | × | ○ | × | × | × | × | - |
| ALTER DATABASE... | × | × | ○ | × | × | × | ○ | A user who is granted the ADMIN permission on the database can also modify the properties of the database. |
| DROP DATABASE... | × | × | ○ | × | × | × | ○ | A user who is granted the ADMIN permission on the database can also delete the database. |
| SHOW DATABASES | × | × | ○ | × | × | × | × | - |
| DESCRIBE TABLE ... | ○ | × | × | × | ○ | × | × | - |
| CREATE TABLE... | × | × | ○ | × | × | × | ○ | - |
| DROP TABLE... | × | × | ○ | × | × | × | ○ | - |

| CREATE USER | × | × | ○ | ○ | × | × | × | - |
|---|---|---|---|---|---|---|---|---|
| ALTER USER... | × | × | ○ | ○ | × | × | × | - |
| DROP USER... | × | × | ○ | ○ | × | × | × | - |
| SHOW USERS | × | × | ○ | ○ | × | × | × | - |
| GRANT... | × | × | ○ | ○ | × | × | × | - |
| REVOKE... | × | × | ○ | ○ | × | × | × | - |
| SHOW PRIVILEGES... | × | × | ○ | ○ | × | × | × | - |
| ALTER SYSTEM... | × | × | × | ○ | × | × | × | - |
| SHOW PARAMETER.. . | × | × | × | ○ | × | × | × | - |

**Authentication when calling OpenTSDB-compatible HTTP API**

For some applications that call OpenTSDB-compatible HTTP API operations to access LindormTSDB, when the user authentication and permission verification feature is enabled, you must include user credentials in the requests that are sent by calling the API operations. Method of specifying user credentials when calling OpenTSDB-compatible API operations to Include Base64-encoded user credentials in HTTP request headers. The method is similar to calling common API operations to send SQL requests. For more information, see the
**Specify user credentials for authentication** section of the **Use the HTTP-based SQL**
**API of LindormTSDB** topic in **Lindorm Developer Guide**.

**Note**

For applications that use TSDB SDKs, you can specify the username and password by calling the `basicAuth` method when you create a `TSDBConfig` object. Permissions required to call OpenTSDB-compatible API operations to access LindormTSDB To call OpenTSDB-compatible API operations, you must have permissions on the GLOBAL scope. The following table describes the permissions that are required to call each API operation.

| API operation | GLOBAL WRITE | GLOBAL READ | GLOBAL ADMIN |
|---|---|---|---|
| /api/put | ○ | × | × |
| /api/query | × | ○ | × |
| /api/query/last | × | ○ | × |
| /api/mput | ○ | × | × |
| /api/mquery | × | ○ | × |
| /api/query/mlast | × | ○ | × |
| /api/suggest | × | ○ | × |
| /api/dump meta _ | × | ○ | × |
| /api/search/lookup | × | ○ | × |
| /api/ttl | × | × | ○ |
| /api/truncate | × | × | ○ |

**Note**

In the following table, ○ indicates that the permission is required, and × indicates that the permission is not required.

**Integration with the access control in LindormTable**

The user information and permission data that are used in LindormTSDB can also be used in LindormTable. If LindormTable and LindormTSDB are both activated for your Lindorm instance, users that are created in LindormTSDB can also be used to access LindormTable. You can also view and manage users that are created in LindormTSDB in the cluster management system of LindormTable. The following figure shows the User Manager page of the cluster management system. Users that are created in LindormTable can also access LindormTSDB after the users are granted permissions on the specified LindormTSDB databases.

**Important**

Users that are created in LindormTable can be granted the TRASH permission. The TRASH permission does not take effect in LindormTSDB. If a namespace in LindormTable has the same name as a database in LindormTSDB and a user is granted permissions on the namespace, the user has permissions to access the database with the same name in LindormTSDB by default. Similarly, if a namespace in LindormTSDB has the same name as a database in LindormTable and a user is granted permissions on the namespace, the user has permissions to access the database with the same name in LindormTable by default.

#### Create a two-way synchronization task

**to implement disaster recovery**

This topic describes how to create a two-way synchronization task to implement disaster recovery.

**Usage notes**

When you create a business database in a disaster recovery instance, you must create a twoway synchronization task on the Lindorm Tunnel Service (LTS) web UI to implement disaster recovery due to the limitations of Lindorm time series databases.

**Procedure**

**Log on to the LTS web UI**

**Important**

After you purchase an LTS instance, the status of the instance is **Creating** in the console. You can log on to the LTS web UI only after the instance status becomes **Running**.
1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-left corner of the page that appears, select the organization to which the
instance belongs.
3. On the **Instances** page, find the instance that you want to manage and click the ID of the
instance or **View Instance Details** in the **Actions** column.
4. In the **LTS WebUI Access** section, click **ClusterManager** to go to the LTS web UI.

**Create a synchronization task**

1. Check whether the default data source is created.
The default data sources include **target_default** and **source_default**.
2. Make sure that the source and destination databases are created. The database created in
this example is test_db. Use the same DDL to create a database with the same name for the secondary instance.

**Note**

You can obtain the connection information about the secondary instance from the address in the target_default data source.

```
SQL endpoint example: jdbc:lindorm:tsdb:url=http://ld-fvxqdumy3e6suhh91-zone2-tsd b-external.lindorm.cn-wulan-env82-d01.inter.env82.shuguang.com:8242"
```

3. Modify the test_db information to add the target_{test_db} and source_{test_db} data
sources based on the default configurations of the default data sources.

```json
{
 "schemaPolicy":"weak",
 "database":"{test_db}",
 "address":"http://ld-fvxqdumy3e6suhh91-zone2-tsdb-external.lindorm.cn-wulan-env82-d0
1.inter.env82.shuguang.com:8242",
 "clusterKey":"hdfs://10.83.43.163:8020,10.83.36.240:8020",
 "client":"sdk",
 "clusterId":"ld-fvxqdumy3e6suhh91-zone2",
 "hdfsUri":"hdfs://10.83.43.163:8020,10.83.36.240:8020"
}
```

4. In the left-side navigation pane, choose Data Source Manage > **Data Source List**. On the
**Data Source Manage** page, click **Add data source**. Configure the related parameters.
5. After the data source is configured, you can view the details on the Data Source Manage
page.
6. In the left-side navigation pane, choose **Lindorm TSDB > Incremental Sync**. On the
Lindorm TSDB Incremental Sync page, click create new job and specify the source and destination clusters.
7. Click **Create** to create a real-time synchronization task.

| Feature | Scenario |
|---|---|
| Data migration between HBase and LindormTable | Seamless data migration between existing clusters and new clusters, cluster upgrades, online and offline workload decoupling, primary/secondary disaster recovery, and active geo-redundancy |
| Synchronization of full data and incremental data from ApsaraDB RDS to Lindorm | Online and offline workload decoupling and historical data archiving |
| Data synchronization from MaxCompute/Hive to Lindorm | Offline query acceleration, and the transmission of details and metrics from data warehouses to Lindorm for online queries |

## LTS

### Overview of LTS

Lindorm Tunnel Service (LTS) is a data ecosystem service that is customized for Lindorm business scenarios. LTS provides easy-to-use capabilities, including data exchange, processing, and change tracking. You can use these capabilities to migrate data, track realtime data changes, dump data to data lakes, and synchronize data from Lindorm to data warehouses. You can also use these capabilities to back up and restore data, and implement multi-active redundancy based on units. This way, LTS provides an all-in-one data ecosystem service for Lindorm.
**Cloud-native distributed system**: LTS is a distributed system that is deployed based on
Elastic Compute Service (ECS). LTS features excellent horizontal scalability and allows you to configure resources based on your business requirements.
**Ease of use**: LTS allows you to configure data migration, import, change tracking, and
archiving tasks with a few clicks. For example, to create a data migration task, you need only to specify the source, destination, and columns that you want to synchronize. LTS automatically replicates schemas, full data, or incremental data based on your settings.
**High security and reliability**: LTS minimizes the impact on the source and destination
systems and minimizes the risks of potential failures due to incompatibility. Before a task is started, LTS prechecks the network connectivity and security. While the task is running, LTS monitors the synchronization latency and the storage usage of the destination cluster in real time. LTS also implements throttling and reports alerts based on the monitoring data. After the task is complete, LTS verifies data.
**Cost-efficiency**: LTS is an optimized service based on open source systems, such as
Apache HBase. LTS allows you to process data at the physical file level. This is 10 times more efficient than traditional data replication. LTS also provides optimized CPU, cache, memory, and network I/O capabilities. This enables LTS to provide cost-effective tunnels and helps reduce your costs of data transfer and processing.

| Data export from Lindorm to MaxCompute (previously known as ODPS) | Export of historical data |
|---|---|
| Subscription to real-time data in LogHub | Allows you to subscribe to real-time data from LogHub and consume the data in Lindorm. |
| Change tracking | Subscription to real-time incremental data in Lindorm |

**Typical scenarios**

Cluster migration Scenarios Data migration from HBase to Lindorm. The switchover of cluster networks. For example, the network type is changed from the classic network to a virtual private cloud (VPC). Data migration between data centers across regions. Workload decoupling. Benefits Both the historical data and real-time incremental data can be migrated during one migration task. When data is being migrated, LTS does not interact with the source HBase or Lindorm cluster. LTS reads data only from the Hadoop Distributed File System (HDFS) of the source cluster. This minimizes the impact on the online business that runs on the source cluster. In most cases, compared with data migration at the API layer, data replication at the file layer can help you reduce more than 50% of the migration traffic. LTS is efficient. Each node can migrate data at a rate of up to 100 MB/s. You can add nodes for horizontal scaling to migrate terabytes or even petabytes of data. LTS provides stable services by retrying failed tasks. It monitors the synchronization rates and progress of tasks in real time and reports alerts when tasks fail. LTS ensures data accuracy by verifying the synchronized data. Automatic schema synchronization is supported to ensure consistent partitions. Decoupling online business from offline business LTS allows you to synchronize online business data in real time to HDFS or Object Storage Service (OSS) storage. LTS can work with components of big data services, such as Spark and MapReduce, to analyze data. This ensures that online business queries are not affected. Primary/secondary disaster recovery LTS supports two-way data synchronization between a primary cluster and a secondary cluster. When the primary cluster fails, you can switch to the secondary cluster to reduce the impact on your workloads. After the primary cluster recovers, you can use LTS to synchronize the incremental data from the secondary cluster to the primary cluster. Historical data storage in ApsaraDB RDS databases In scenarios where historical data, such as transaction orders, is stored, performance bottlenecks may occur in ApsaraDB RDS databases due to the ever-increasing data size. Periodic data archiving or sharding is complicated and causes high costs. LTS allows you to synchronize data from ApsaraDB RDS to LindormTable in real time to separate hot data from cold data. LindormTable provides features such as automatic horizontal scaling, highconcurrency queries, multi-dimensional indexing, and lightweight analysis. Lindorm Streams allows you to track data changes in sequence. LTS also allows you to synchronize data from LindormTable to other analytics systems for complex data analysis.

### Log on to the cluster

**management system**

This topic describes how to log on to the cluster management system of a Lindorm Tunnel Service (LTS) instance.

**Prerequisites**

An LTS instance is created. For more information, see Create an LTS instance.

**Procedure**

1. Log on to the Lindorm console.
2. On the **Instances** page, find the instance that you want to manage. Then, click the
instance ID or click **View Instance Details** in the **Actions** column.
3. In the **LTS WebUI Access** section, click **ClusterManager** to log on to the cluster
management system.

## Appendix

### Authorize a tenant

**organization to access SLB**

This topic describes how to grant a tenant organization the permissions to access Server Load Balancer (SLB) and helps you efficiently resolve related issues.

**Important**

If you need to create and use IPv6 addresses for your business, you must ensure that the current tenant organization has explicitly granted database services the permissions to access SLB. If such permissions are not granted, IPv6 addresses cannot be created.

**Procedure**

1. Log in to the Apsara Uni-manager Management Console.
2. In the top navigation bar, click **Configurations**.
3. In the left-side navigation pane, click **Service-linked Roles**.
4. On the Service-linked Roles page, click **Create Service-linked Role** in the upper-left
corner. Select **Server Load Balancer** for the **Service Name** parameter, and select the organization to which you want to grant permissions for the **Authorized Organization**
**Name** parameter.
5. Click **OK**.
