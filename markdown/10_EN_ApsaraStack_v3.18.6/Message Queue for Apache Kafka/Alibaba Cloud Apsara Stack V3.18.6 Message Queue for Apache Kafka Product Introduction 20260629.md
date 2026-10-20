---
title: "Message Queue for Apache Kafka Product Introduction 20260629"
product_version: "V3.18.6"
pdf_pages: 17
source_pdf: "efa742ad46a1a5ae_Alibaba Cloud Apsara Stack V3.18.6 Message Queue for Apache Kafka Product Introduction 20260629.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/v3.18.6%E7%89%88%E6%9C%AC%E6%96%87%E6%A1%A3/%E6%B6%88%E6%81%AF%E9%98%9F%E5%88%97Kafka%E7%89%88%20/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.6%20Message%20Queue%20for%20Apache%20Kafka%20Product%20Introduction%2020260629.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes)
---

# Message Queue for Apache Kafka Product Introduction 20260629

## Table of Contents

- 1 ApsaraMQ for Kafka
  - 1.1 Product details
  - 1.2 Benefits
  - 1.3 Features
  - 1.4 Use scenarios
  - 1.5 Instance specifications
  - 1.6 Key concepts
  - 1.7 Limitations

## 1 ApsaraMQ for Kafka

ApsaraMQ for Kafka is a distributed message queue service provided by Alibaba Cloud. This service features high throughput and scalability. Widely used in big data fields such as log collection, monitoring data aggregation, streaming data processing, and online and offline analytics, ApsaraMQ for Kafka consists of an indispensable part of the big data ecosystem. ApsaraMQ for Kafka provides a fully managed service with ultrahigh elasticity, and eliminates the need for deployment and O&M while ensuring professional, reliable, and secure operations.

### 1.1 Product details

ApsaraMQ for Kafka is a fully managed, distributed message queue system designed to reduce the operations and maintenance (O&M) costs and complexity associated with open source Apache Kafka. It provides high-throughput message processing, persistent storage, multi-replica partitions, stream processing, auto-scaling, and security controls. ApsaraMQ for Kafka also features cross-region high availability, elastic scalability, full management, global deployment capabilities, and deep integration with other services. The service is ideal for use cases such as real-time data collection, data pipelines, monitoring and alerting, microservice decoupling, and event-driven architectures. Using ApsaraMQ for Kafka, you can reduce O&M costs, enhance business agility and data processing capabilities, ensure data consistency, and accelerate your time-to-market.

**Open source compatibility**

ApsaraMQ for Kafka is 100% compatible with open source Apache Kafka and supports versions 2.8.x and 3.3.x. You can seamlessly migrate your existing services to the cloud without modifying your code and take advantage of a fully managed, distributed message queue service.
**Open source compatibility:** ApsaraMQ for Kafka is fully compatible with Apache Kafka.
You can use native Apache Kafka clients to communicate with ApsaraMQ for Kafka. ApsaraMQ for Kafka currently supports Apache Kafka versions 2.8.x and 3.3.x.
**Seamless migration:** ApsaraMQ for Kafka leverages the existing open source Apache
Kafka ecosystem, which lets you migrate your services to the cloud without modifying your code.

**O&M and monitoring features**

HouseKeeping (health inspection component): The HouseKeeping component performs runtime inspections of the core links in ApsaraMQ for Kafka. It runs a full diagnostic scan on the cluster every minute and sends an alert if an unhealthy status is detected. The component also generates a daily inspection report that allows Alibaba Cloud O&M engineers to monitor the health of the ApsaraMQ for Kafka system.

> **Note:** If an unhealthy cluster is detected during an inspection, the risks are displayed on the **Instance Risks** tab of the **Instance Details** page.
> Business monitoring and alerting: You can set monitoring and alerts for message accumulation in each Consumer Group to help you promptly identify issues.
> OpenAPI: ApsaraMQ for Kafka provides a comprehensive set of management OpenAPI operations that allow you to implement various resource management and O&M features.

**Reliability**

ApsaraMQ for Kafka uses a distributed architecture that supports multi-cluster deployment and disaster recovery across two availability zones (AZs). This ensures your services can continue to run without requiring reconfiguration or restarts. It supports multi-replica replication to ensure message reliability. It supports horizontal scaling to increase message concurrency and handle message accumulation. A health inspection component performs runtime inspections of core links and sends alerts if unhealthy states are detected.

**Availability**

ApsaraMQ for Kafka optimizes message storage to prevent service unavailability caused by disk overload. It also provides monitoring and alerting capabilities for open source metrics to meet daily O&M requirements.

**Security**

ApsaraMQ for Kafka provides authentication, authorization, and user permission delegation mechanisms to deliver enterprise-grade security protection.
**Permission management:** ApsaraMQ for Kafka fully supports features such as Alibaba
Cloud accounts, Resource Access Management (RAM) users, and blacklists and whitelists. This enables authorization for Alibaba Cloud accounts, RAM users, and cross-account access between enterprises.
**Data transmission:** ApsaraMQ for Kafka supports access control lists (ACLs), Simple
Authentication and Security Layer (SASL) user management, and permission management for users on topics and Groups to ensure secure data transmission.
**Alibaba Cloud VPC:** In addition to public network access, ApsaraMQ for Kafka also
supports virtual private clouds (VPCs). You have full control over your VPCs. For example, you can select IP address ranges and configure route tables and gateways. You can also use other Alibaba Cloud resources, such as Elastic Compute Service (ECS) instances, ApsaraDB RDS instances, and Server Load Balancer (SLB) instances, in your custom VPCs.

### 1.2 Benefits

ApsaraMQ for Kafka offers advantages over self-managed open-source Apache Kafka, including out-of-the-box usability, a fully managed service, high availability, and elastic computing.

**Out-of-the-box usability**

ApsaraMQ for Kafka is 100% compatible with open-source Apache Kafka and supports seamless migration to the cloud. Open-source compatibility: ApsaraMQ for Kafka is 100% compatible with open-source Apache Kafka. You can use open-source Apache Kafka clients to communicate with ApsaraMQ for Kafka. ApsaraMQ for Kafka supports kernel versions 2.8.x and 3.3.x. Seamless migration: ApsaraMQ for Kafka is built on the open-source Apache Kafka ecosystem. This lets you migrate to the cloud without changing your code.

**Fully managed service**

Monitoring and alerts: ApsaraMQ for Kafka provides comprehensive monitoring charts and alerts to help you identify issues promptly.

**High availability**

The Alibaba Cloud development and performance optimization teams have improved the open-source product to provide a superior service. Data persistence: Messages are persisted to disk in the message queue for high data reliability and service availability. High throughput: The ApsaraMQ for Kafka cluster maintains high throughput, even with many accumulated messages.

**Elastic computing**

You can scale resources as needed as needed. The scaling process does not affect your applications. Cluster scale-out: You can scale out nodes horizontally. Partition scale-out: You can scale out partitions quickly.

### 1.3 Features

ApsaraMQ for Kafka is a distributed message queue service provided by Alibaba Cloud. This service features high throughput and scalability. It lets you manage instances, topics, and groups, to perform monitoring and O&M, and guarantees high reliability at the same time.

**Instance management**

| Feature | Description |
|---|---|
| Create an instance | You can create ApsaraMQ for Kafka instances based on their specifications. |
| View the instance list | You can view the list of deployed instances. |
| Scale out an instance | You can increase the number of nodes. |
| View the details of an instance | You can view the details of an instance. |
| Release an instance | You can release an instance and clear the messages in the instance. |
| Perform load balancing | After the instance scale-out, you can perform load balancing to redistribute the partitions of the topic. |

**Topic management**

| Feature | Description |
|---|---|
| Create a topic | You can create topics. |

| View the list of topics | You can view the list of created topics. |
|---|---|
| View partition status in a topic | After you create a topic, you can view the status of each partition in the topic. |
| View the subscriptions of a topic | After you create a topic, you can view the online consumer groups that subscribe to the topic. |
| Modify topic configurations | You can modify the configurations of a topic, including the minimum synchronized replicas, message retention period, and maximum message size. |
| Increase the number of partitions in a topic | After you create a topic, you can increase the number of partitions in the topic. Note ApsaraMQ for Kafka does not allow you to decrease the number of partitions in a topic. If you want to decrease the number of partitions in a topic, delete the topic and create another topic that has the required number of partitions. |

**Group management**

| Feature | Description |
|---|---|
| View the list of consumer groups | You can view the list of consumer groups. |
| View the consumer status of a consumer group | You can view the consumer status of a consumer group. |
| Reset the consumer offset of a consumer group | If you reset a consumer offset, the offset from which a consumer starts to consume messages is changed. You can reset consumer offsets to skip the accumulated or undesired messages instead of consuming them. You can also consume messages sent after a point in time. |

**Message management**

| Feature | Description |
|---|---|
| Send messages | After you create a topic, you can send messages to the topic you created in the ApsaraMQ for Kafka console. |

| Query messages | You can query messages by time, offset, topic, or partition. You can also view and download messages. |
|---|---|

**Basic features**

| Feature | Description |
|---|---|
| Use the publish-subscribe model | ApsaraMQ for Kafka supports the one-to-many publish-subscribe model. After a publisher sends messages to a topic, messages can be consumed by one or more consumers at the same time. |
| Send messages in batches | You can send multiple messages at a time. |
| Feature version compatibility | Compatible with Apache Kafka 2.8.x and 3.3.x kernel versions. |

**ACL management**

| Feature | Description |
|---|---|
| Manage Simple Authentication and Security Layer (SASL) permissions | Create access control lists (ACLs): You can create permissions on resources. Delete ACLs: You can delete permissions on resources. Query user permissions: You can query the specified user permissions based on the user or resource information. |
| Manage SASL users | Create SASL users: You can create SASL users. Delete SASL users: You can delete SASL users. Modify SASL users: You can modify the passwords of SASL users. |

**Endpoint management**

| Feature | Description |
|---|---|
| Create virtual IP addresses (VIPs) | ApsaraMQ for Kafka provides the following types of endpoints: AnyTunnel: allows access to ApsaraMQ for Kafka from any virtual private cloud (VPC). SingleTunnel: allows access to ApsaraMQ for Kafka only from a specific VPC. |

| Delete VIPs | You can delete the VIP of an instance. Note After you delete a VIP, the ApsaraMQ for Kafka instance becomes unavailable. Proceed with caution. |
|---|---|

**Access ApsaraMQ for Kafka using SDKs**

| Feature | Description |
|---|---|
| SDK support for multiple languages | You can access ApsaraMQ for Kafka using SDKs for multiple programming languages such as Java, Python, C++, Go, PHP, Ruby, and Node.js. |

**Instance relationship configuration**

| Feature | Description |
|---|---|
| Bind instance ownership | You can associate instances with resource groups. After you associate the instance with the resource group, you can perform operations on the resources of the instance only using the Apsara Stack account of the resource group. |

**Monitoring and alerting**

| Feature | Description |
|---|---|
| Use Managed Service for Prometheus and Grafana for monitoring and alerting | You can use Grafana dashboards to display various monitoring metrics for ApsaraMQ for Kafka. You can also use Managed Service for Prometheus to view the monitoring metrics for ApsaraMQ for Kafka by querying statements at a specific point in time or within a specific period of time. The monitoring metrics include the number of brokers, percentage of network thread time, length of the request queue, length of the response queue, synchronized replicas that are less than the set ISR, and number of failed replicas. You can use the Managed Service for Prometheus console to view the alert information and alert rules of ApsaraMQ for Kafka. The monitoring metrics include KafkaDeadLock, KafkaBrokerCount, KafkaRequestQueueSize, KafkaOldGcRate, KafkaUnderMinIsr, and KafkaUnderReplicated. The following alert rules can be viewed: Rule, State, Error, Last Evaluation, and Evaluation Time. |

**Performance metrics**

| Feature | Description |
|---|---|
| High scalability | You can increase the number of partitions. You can purchase scale-out packages to horizontally scale out the peak traffic within a cluster or across multiple clusters. |

**Stability metrics**

| Feature | Description |
|---|---|
| Water Level Management | When the disk capacity is full, earlier data is automatically deleted to avoid unavailability. |
| High availability | The system prevents single points of failure (SPOFs) using a scalable distributed cluster architecture with three nodes by default. Each node of a cluster runs independently. If one node in a cluster fails, other nodes in the cluster are not affected. |

**High reliability**

| Feature | Description |
|---|---|
| Zone-disaster recovery | The system supports the configuration of a zone-disaster recovery architecture and switchover between zones. Note This feature needs to be used with KafkaReplicator. |

### 1.4 Use scenarios

This topic describes the typical use scenarios of ApsaraMQ for Kafka, including website activity tracking, log aggregation, stream computing, and data transfer hub.

**Asynchronous inference in AI computing scenarios**

In many AI applications, such as recommendation systems, risk governance, or intelligent customer service, model inference is required for processing massive real-time data. Because the inference process can be resource-intensive and time-consuming, if all requests are synchronously processed, this may lead to system bottlenecks. Kafka decouples data producers from AI inference services, which provides a high-performance, highly available asynchronous communication layer. This enables inference tasks to be executed independently with scalability. As a data pipeline, Kafka can receive real-time data streams from various sources. These data streams first enter Kafka topics and form a reliable buffer layer. AI inference services can asynchronously pull batches of data from these topics for prediction. This mechanism allows inference services to scale automatically based on their processing capacity, which avoids direct pressure on upstream data sources. Kafka delivers the following benefits for asynchronous inference in AI computing scenarios: Decoupling data sources and inference services: Kafka acts as a bridge between data producers and AI inference services, decouples their dependencies, and enables independent development and deployment. Auto scaling: When data volume or inference load increases, Kafka partitions and inference service instances can be added to scale horizontally to meet high-performance inference demands. Support for large-scale multimodal data transmission: AI inference scenarios often involve high-resolution images, video streams, and other large files, as well as multimodal data such as text, images, and audio. Kafka can transmit data references or directly handle serialized multimodal data. This provides core support for processing large-scale, complex multimodal data in inference systems. High throughput and low latency: Kafka supports high-throughput data streams and enables rapid data transfer to ensure timely AI inference and real-time data-driven decision-making. Data persistence and reliability: With proper configuration, Kafka's message persistence ensures no data loss. This enhances the robustness of asynchronous inference workflows.

**Website activity tracking**

Successful website operations require analysis of user actions on websites. You can use the publish-subscribe model of ApsaraMQ for Kafka to collect user action data on a website in real time, publish messages to different topics based on business data types, and then use message streams generated based on the real-time delivery of subscribed messages for realtime processing or real-time monitoring, or load the message streams to offline data warehouse systems such as Hadoop and MaxCompute for offline processing. User actions on a website include sign-in, logon, top-up, payment, and purchase. ApsaraMQ for Kafka provides the following benefits when it is used for website activity tracking: High throughput: High throughput is required to support the large amount of user action data on a website. Auto scaling: Promotions on a website can cause a sharp increase in user action data. During promotions, the number of brokers can be scaled out on demand. Big data analysis: ApsaraMQ for Kafka can connect to real-time stream computing engines such as Storm and Spark. ApsaraMQ for Kafka can also connect to offline data warehouse systems such as Hadoop.

**Log aggregation**

Many platforms, such as Taobao and Tmall, generate a large number of logs every day. In most cases, the logs are streaming data, such as page views and queries. Compared with logcentered systems, such as Scribe and Flume, ApsaraMQ for Kafka features higher performance, stronger data persistence, and shorter end-to-end response time. This makes ApsaraMQ for Kafka an ideal log collection center. In ApsaraMQ for Kafka, file details are ignored. Logs of multiple hosts or applications can be abstracted as log or event message streams and then asynchronously sent to ApsaraMQ for Kafka clusters. This greatly reduces the response time. ApsaraMQ for Kafka clients can submit and compress messages in batches. This prevents increased performance overhead for producers. Consumers can use offline warehouse systems such as Hadoop and MaxCompute and real-time online analysis systems such as Storm and Spark to perform statistical analysis on logs. ApsaraMQ for Kafka provides the following benefits when it is used for data aggregation: System decoupling: ApsaraMQ for Kafka serves as a bridge between application systems and analysis systems and decouples the two types of systems. High scalability: ApsaraMQ for Kafka is scalable. If the data volume increases, you can add nodes to rapidly scale out ApsaraMQ for Kafka. Online and offline analysis systems: ApsaraMQ for Kafka supports real-time online analysis systems and offline analysis systems such as Hadoop.

**Stream computing**

In fields such as stock market trend analysis, meteorological data monitoring and management, and website user action analysis, data collection and storage in databases before data processing are difficult due to the huge amount of data generated in real time. Therefore, traditional data processing architectures cannot meet the requirements of users. Different from traditional architectures, ApsaraMQ for Kafka and stream computing engines such as Storm, Samza, and Spark can efficiently resolve the preceding pain point. The stream computing model captures and processes data in real time during data flow, computes and analyzes data based on business requirements, and then saves or distributes the results to relevant components. ApsaraMQ for Kafka provides the following benefits when it is used for stream computing: System decoupling: ApsaraMQ for Kafka serves as a bridge between an application system and an analysis system and decouples the two systems. High scalability: ApsaraMQ for Kafka is highly scalable to deal with the huge amount of data generated in real time. Connection to stream computing engines: ApsaraMQ for Kafka can connect to open source stream computing engines such as Storm, Samza, and Spark, and Alibaba Cloud services such as E-MapReduce (EMR), Blink, and Realtime Compute.

**Data transfer hub**

Over the past 10 years, dedicated systems have emerged to provide specific services such as key-value storage (HBase), search (Elasticsearch), stream processing (Storm, Spark, and Samza), and time series database (OpenTSDB). Each dedicated system is designed for a single goal. The simplicity of dedicated systems makes it easier and more cost-efficient to build distributed systems on commercial hardware. In most cases, the same dataset needs to be injected into multiple dedicated systems. For example, if application logs are used for offline analysis, searching for a single log is also required. However, it is impractical to construct an independent workflow to collect data of each type before importing the data to the corresponding dedicated systems. In this case, you can use ApsaraMQ for Kafka as a data transfer hub to import the same data record to different dedicated systems. ApsaraMQ for Kafka provides the following benefits when it serves as a data transfer hub: High-capacity storage: ApsaraMQ for Kafka can store a large amount of data on commercial hardware and help build horizontally scalable distributed systems. One-to-many consumption model: The publish-subscribe model allows the same dataset to be consumed multiple times. Real-time and batch processing: ApsaraMQ for Kafka supports local data persistence and page cache, and transmits messages to consumers for real-time processing and batch processing at the same time without performance loss.

### 1.5 Instance specifications

This topic describes the specification types available for the Enterprise Edition of Message Queue for Apache Kafka to help you select an instance specification that meets your business requirements.

**Specification types**

The Enterprise Edition of Message Queue for Apache Kafka offers the following instance specification types:

| Featu re | Comp onent type | CPU (cores) | Memory (GB) | Storage (GB) | Nodes | Through put | Partitions |
|---|---|---|---|---|---|---|---|
| large- indep enden t-zk | Broker v2.8.2 | 48 | 192 | 1500 (expanda ble with multiple disks) Local NVMe SSD only | 3 Scaling step: 3 | Cluster- shared 360 MB/s read/write bandwidt h | Recommend ed maximum of 1,800 partition leaders per cluster. |
| stand ard- indep enden t-zk | Broker v2.8.2 | 16 | 64 | 1500 (expanda ble with multiple disks) Local NVMe SSD only | 3 Scaling step: 3 | Cluster- shared 120 MB/s read/write bandwidt h | Recommend ed maximum of 600 partition leaders per cluster. |
| profes sional- indep enden t-zk | Broker v2.8.2 | 32 | 128 | 1500 (expanda ble with multiple disks) Local NVMe SSD only | 3 Scaling step: 3 | Cluster- shared 240 MB/s read/write bandwidt h | Recommend ed maximum of 1,200 partition leaders per cluster. |
| stand ard | Broker v2.8.2 | 16 | 64 | 1500 (expanda ble with multiple disks) Local NVMe SSD only | 3 Scaling step: 3 | Cluster- shared 120 MB/s read/write bandwidt h | Recommend ed maximum of 600 partition leaders per cluster. |
|   |   | 4 | 16 |   |   | Cluster- shared 30 MB/s read/write bandwidt h | Recommend ed maximum of 150 partition leaders per cluster. |

|   |   | 8 | 32 |   |   | Cluster- shared 60 MB/s read/write bandwidt h | Recommend ed maximum of 300 partition leaders per cluster. |
|---|---|---|---|---|---|---|---|
| exclus ive | Broker v2.8.2 /Broke r v3.3.3 |   |   | 1500 (expanda ble with multiple disks) Local NVMe SSD only | 3 Scaling step: 1 |   |   |
|   |   | 16 | 64 |   |   | Cluster- shared 120 MB/s read/write bandwidt h | Recommend ed maximum of 600 partition leaders per cluster. |
|   |   | 32 | 128 |   |   | Cluster- shared 240 MB/s read/write bandwidt h | Recommend ed maximum of 1,200 partition leaders per cluster. |

### 1.6 Key concepts

This topic defines and explains the terms and concepts used in Message Queue for Apache Kafka to help you better understand and use the product.

**B**

**Broker**

An independent server in a Message Queue for Apache Kafka cluster.

**Consumer**

A message subscriber, also known as a message consumer, that reads and consumes messages from Message Queue for Apache Kafka servers.

**Consumer group**

A logical grouping of consumers that process the same category of messages. The relationship between consumer groups and topics is many-to-many (N:N).

**P**

**Partitional ordered messages**

By default, messages with the same key are distributed to the same partition, and messages within a partition are stored in the order they are sent. If a server in the cluster fails, message ordering is preserved, but attempts to send messages to some partitions may fail until the server is back online.

**Local storage**

A message storage method that uses the native Apache Kafka In-Sync Replica (ISR) algorithm with three replicas and `min.insync.replicas` =2.

**P**

**Partition**

A physical unit within a topic. Each topic consists of one or more partitions.

**Producer**

A message publisher, also known as a message producer, that produces and sends messages to Message Queue for Apache Kafka servers.

**Normal messages**

By default, messages with the same key are distributed to the same partition and are stored in the order they are sent. If a server in the cluster fails, messages may be delivered out of or*er.

**T**

**Topic**

In Message Queue for Apache Kafka, a topic is a logical category for classifying messages, consisting of one or more partitions distributed across one or more brokers.

### 1.7 Limitations

Before you use the Message Queue for Apache Kafka service, you need to understand the usage limits of Message Queue for Apache Kafka.

| Item | Description |
|---|---|
| Automatic topic creation | Supported |
| Automatic consumer group creation | Supported |
| Expose ZK | Not supported |
| Topic-level authorization | Supported |
| Changing instance network properties | Not supported |
| Maximum message size | 10 MB |

| Number of topics (number of partitions) | Unlimited Note Keep the total number of partitions per node at 500 or fewer. |
|---|---|
| Number of consumer groups | Unlimited |
| Log in to a Message Queue for Apache Kafka cluster | Supported Note Recommended for operators. |
| Server version | 2.8/3.3 |
