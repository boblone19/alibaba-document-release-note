---
title: "Alibaba Cloud Apsara Stack v3.18.6-2607 Alibaba Cloud Message Queue Product Introduction 20260828"
product_version: "V3.18.6_2607"
doc_version: "20260828"
pdf_pages: 27
source_pdf: "Alibaba Cloud Apsara Stack v3.18.6-2607 Alibaba Cloud Message Queue Product Introduction 20260828.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/3816%202607/pdf%203/%E4%BA%91%E6%B6%88%E6%81%AF%E9%98%9F%E5%88%97%20RocketMQ%20%E7%89%88/Alibaba%20Cloud%20Apsara%20Stack%20v3.18.6-2607%20Alibaba%20Cloud%20Message%20Queue%20Product%20Introduction%2020260828.pdf"
converter: pdf2md (PyMuPDF line classifier)
---

# Alibaba Cloud Apsara Stack v3.18.6-2607 Alibaba Cloud Message Queue Product Introduction 20260828

sage Queue for Apache RocketM Q?

## What is Message Queue for

**Apache RocketMQ?**

Message Queue for Apache RocketMQ is a distributed messaging middleware that is developed by Alibaba Cloud based on Apache RocketMQ. This Alibaba Cloud service features low latency, high concurrency, high availability, and high reliability. Message Queue for Apache RocketMQ is a core service in the enterprise-level Internet architecture. Using the highly available distributed cluster technology, this service offers a series of messaging services in the cloud, including message subscription and delivery, message tracing and query, scheduled or delayed messages, and resource statistics. Message Queue for Apache RocketMQ provides asynchronous decoupling and load shifting for distributed application systems. It also supports various features for Internet applications, including massive message accumulation, high throughput, and reliable message consumption retry. It is one of the core Alibaba Cloud services that are used to support the Double 11 Shopping Festival. Message Queue for Apache RocketMQ supports access by using TCP. It also supports the Java, C++,and .NET programming languages. This facilitates quick access to Message Queue for Apache RocketMQ for applications that are developed in different programming languages. ails

## Product details

This topic describes how ApsaraMQ for RocketMQ works and the key features of ApsaraMQ for RocketMQ. ApsaraMQ for RocketMQ supports connections over TCP and HTTP from clients that are developed in multiple programming languages, offers high performance and reliability based on multiple replicas, and provides multi-dimensional O&M and management tools. It also supports enterprise-class features, such as message traces and dead-letter queues.

**How it works**

ApsaraMQ for RocketMQ uses classic message queue models. It provides an asynchronous communication layer between distributed systems. Asynchronous communication is implemented mainly based on producers, consumers, messages, and queues.
**Producers:** Producers are applications or services that send messages to queues.
**Consumers:** Consumers are applications or services that extract and process messages
from queues.
**Messages:** Messages are the basic unit of communication, which can contain textual data,
binary data, or structured data.
**Queues:** A queue is a temporary storage area used to store messages. In a point-to-point
model, each message can be received only by one consumer. In a pub/sub model, a message is distributed to one or more consumers. In most cases, ApsaraMQ for RocketMQ processes data in the following steps:
1. The producer creates the message and sends it to a message queue.
2. The message queue persists the message to prevent data loss caused by system failures.
3. The consumer connects to the message queue and pulls or receives the message from the
message queue by using long polling or push mechanisms.
4. After the consumer processes the message, the consumer typically sends an
acknowledgement (ACK) to indicate that the message has been processed. Then, the message is removed from the queue to ensure that the message is not processed multiple times. ApsaraMQ for RocketMQ improves reliability by implementing redundant storage and data replicas, which prevent message loss even in cases of partial system failures. ApsaraMQ for RocketMQ services can be scaled in and scaled out based on workloads. You do not need to manually scale services.

**Key functions and features**

**Producers: message types and scenarios**

**Message types**

Normal messages: suitable for asynchronous communication, such as log collection and event notification. ails Transactional messages: Ensure the atomicity of business operations and message sending, such as payment and inventory updates. Ordered messages: Ensure that messages are strictly ordered by business dimension, such as order ID. This type of message is suitable for processing financial transactions. Scheduled and delayed messages: Support delayed message delivery that is accurate to the millisecond, such as payment timeouts.

**Key capabilities**

Topics: ApsaraMQ for RocketMQ categorizes the business logic by topic and sends messages based on topics. Tags: ApsaraMQ for RocketMQ allows you to classify and filter messages by tag. You can use tags to implement finer-grained message management. Batch message sending: ApsaraMQ for RocketMQ allows you to send multiple messages at the same time, achieving higher efficiency and lower network overheads.

**Consumers: efficient consumption and high reliability**

**Consumption modes**

Clustering consumption: In this mode, a message is consumed by only one instance in the consumer group. This mode is suitable for high-throughput scenarios, such as order processing. Broadcasting consumption: In this mode, a message is repeatedly consumed by all instances in the consumer group. This mode is suitable for global notification scenarios, such as applying configurations.

**Consumer groups**

Load balancing: Messages are automatically distributed to the corresponding consumer group for consumption. Failover: If the ApsaraMQ for RocketMQ broker fails, tasks are automatically migrated to ensure consumption continuity. Horizontal scaling: improves the consumption capacity by adding brokers.

**Offsets**

Consumer offset resetting: You can reset the consumption progress by time to analyze message traces or discard accumulated messages.

**Push and pull modes**

Push mode: The ApsaraMQ for RocketMQ broker actively pushes messages. This mode is suitable for scenarios with high real-time requirements. Pull mode: The consumer actively pulls messages. This mode is suitable for batch processing scenarios or scenarios that require low latency.

**Consumption guarantee**

Failed messages can be retried up to 16 times and automatically quarantined to a deadletter queue. You can also use tags and SQL statements to filter messages for higher processing efficiency.

**High availability and high performance**

**Throughput**: A single ApsaraMQ for RocketMQ cluster supports millions of transactions per
second (TPS) and millisecond-level latency to support high concurrency for businesses. ails
**Multi-replica mechanism**: ApsaraMQ for RocketMQ implements data synchronization and
backeup, and supports cross-region disaster recovery to ensure availability.

**Enterprise-class features**

**Protocols**: ApsaraMQ for RocketMQ supports connections over TCP and HTTP and provides
SDKs for multiple programming languages, such as Java, C, C++, and .NET.
**Message traces**: You can use message traces to track message flows and facilitate
troubleshooting.
**Dead-letter queues**: Messages that cannot be consumed as expected are stored in a
special queue called dead-letter queue for subsequent processing. Dead-letter queues quarantine failed messages to prevent workflow congestion.
**Permission control**: ApsaraMQ for RocketMQ supports multi-layer security protection
based on virtual private clouds (VPCs), Resource Access Management (RAM) roles, and IP address whitelists to meet compliance requirements in various industries, such as finance and healthcare.
**Active geo-redundancy**: You can purchase active geo-redundancy instances in the
ApsaraMQ for RocketMQ console. If you deploy Multi-Site High Availability (MSHA) for your project, your business workloads are distributed to different production centers based on regions. Each production center provides external services at the same time, and data is synchronized and backed up between the production centers. If one of the production centers fails, you can use MSHA to switch the workloads to other healthy disaster recovery sites. This enables smooth business migration and fast disaster recovery.
**Resource statistics**: You can use this feature to collect statistics about message
production and message consumption. This feature allows you to view the total number of messages that a topic receives or the TPS for message production within a specified period of time. This feature also allows you to view the total number of messages that are delivered from a topic to a consumer group or the TPS for message consumption within a specified period of time.

**Management tools**

**Web console**: ApsaraMQ for RocketMQ provides a web console in which you can manage
topics and groups, query messages and message traces, and view resource statistics.
**API**: ApsaraMQ for RocketMQ provides API operations that allow you to integrate the
management tools with your console.
**mqadmin command set**: Apsara Stack provides a rich set of management commands.
You can run commands to manage your resources in ApsaraMQ for RocketMQ.

**Deployment on Apsara Stack**

**Flexible deployment**: ApsaraMQ for RocketMQ can be deployed on Apsara Stack as an
independent service or on a hybrid cloud architecture.
**O&M management**: Apsara Stack supports O&M management tools such as the mqadmin
command set and API operations. You can integrate various management tools with the ApsaraMQ for RocketMQ console and perform unified O&M operations.

## Benefits

As a professional messaging middleware, ApsaraMQ for RocketMQ provides various benefits such as high reliability, high availability, and high performance. It also supports multiple protocols and independent deployment.

**Benefits of ApsaraMQ for RocketMQ**

**Professionalism**

ApsaraMQ for RocketMQ is a professional messaging middleware in the industry. It ensures data integrity and is built on top of a sophisticated technical system. ApsaraMQ for RocketMQ is developed based on open source Apache RocketMQ and has won several awards both in and outside China. More than 1,000 core applications of Alibaba Cloud use ApsaraMQ for RocketMQ, which can forward hundreds of billions of messages per day. It delivers stable and reliable performance in real-life business scenarios such as the Double 11 Shopping Festival.

**High reliability.**

Each message is stored in multiple replicas on disks. No message is found lost after rigorous power-off tests. ApsaraMQ for RocketMQ supports the accumulation of large numbers of messages. A single topic supports more than 10 billion messages even if the workload of the system is high. By default, messages are stored for three days. ApsaraMQ for RocketMQ allows you to reset consumer offsets for messages that are produced at any point in time within three days.

**High availability**

ApsaraMQ for RocketMQ provides the active geo-redundancy feature, which allows you to implement fast failover without downtime. Business recovery and fault recovery are decoupled to ensure business continuity.

**High performance**

ApsaraMQ for RocketMQ supports horizontal scaling. The maximum size of a single message that is supported by ApsaraMQ for RocketMQ is 4 MB, including the message attributes.

**Support for multiple protocols**

ApsaraMQ for RocketMQ supports connections over TCP and HTTP and supports multiple programming languages such as Java, C++, and .NET.

**Independent deployment**

ApsaraMQ for RocketMQ can be deployed on Apsara Stack as an independent service or on physical machines. To build a complete messaging system on ApsaraMQ for RocketMQ, you only need to use a few machines. Apsara Stack provides the mqadmin command set and management API operations. O&M engineers can conveniently monitor the health status of your system in real time. ApsaraMQ for RocketMQ can be deployed on a hybrid cloud architecture and allows you to use Express Connect circuits to connect to services on the Alibaba Cloud public cloud.

**Comparison between ApsaraMQ for RocketMQ and open source**

**Apache RocketMQ**

ApsaraMQ for RocketMQ outperforms open source Apache RocketMQ in terms of the following aspects:

| Category | ApsaraMQ for RocketMQ | Open source Apache RocketMQ |
|---|---|---|
| Security | Continuous fixing for vulnerabilities, including automatic updates and patch support. An integrated Apsara Stack account permission system for all cloud services. Multi-tenant resource isolation. Flexible resource access control methods, such as Resource Access Management (RAM) users and roles, and Security Token Service (STS). Fine-grained control of API permissions. | Vulnerability fixing rely on community solutions and requires active updates from users. Basic access control based on access control lists (ACLs), which do not support multi-tenant isolation. Permission management requires custom methods and configurations. Coarse-grained control of API permissions, which rely on custom configurations. |
| Stability | Efficient troubleshooting from Apsara Stack technical support. Adaptation to multi- architecture chip processors, such as ARM and x86. Clear performance metrics, with quantified performance for each type of chip. Mature O&M change solutions, such as visualized operations and automated O&M tool chains. | Insufficient troubleshooting that replies on community solutions. Reply on mainstream architectures with limited adaptation to chips. Performance metrics require customer-side testing and optimization. O&M replies on customer- side experience because no mature O&M solutions are provided. |
| Disaster recovery | Zone-disaster recovery, including symmetric and asymmetric disaster recovery between zones. Disaster recovery supported by data centers. Active geo-redundancy for cross-region disaster recovery. Automatic failover and disaster recovery by high- availability clusters. | Basic master-replica replication, which requires customer-side configurations. Disaster recovery across data centers, which requires external tools. Active geo-redundancy requires customer-side design and configurations. Highly complex disaster recovery solutions that rely on community best practices. |

| Observability | Various built-in monitoring metrics at the underlying physical resource layer, platform layer, and tenant business layer, such as message latency, throughput, and cluster status. Custom monitoring and alerting that are deeply integrated with Apsara Stack monitoring services. Visualized dashboards and alerting capabilities. Continuous optimization for monitoring dimensions and metrics. | Basic monitoring provided by the open source version with limited monitoring metrics. Advanced monitoring requires integration with third-party tools, such as Prometheus and Grafana. Customized observation solutions must be developed by customers themselves. Updates of monitoring metrics rely on community iteration. |
|---|---|---|
| Scalability | Scaling within and across clusters. | Elastic scaling rely on manual operations or third- party tools. The scalability is limited by the hardware environment supported by the community. |
| Multi-chip support | Support different chips in multiple clusters, such as ARM clusters and x86 clusters. Each cluster must use the same type of chip, but you can deploy clusters that use heterogeneous chips. Support chip performance optimization and adaptation, with performance tuning guides provided by Apsara Stack. | Each cluster must use the same type of chip, and you cannot deploy clusters that use heterogeneous chips. Chip adaptation requires customer-side testing and optimization. |

**Highlights**

1. **Security**: ApsaraMQ for RocketMQ uses a mature account and permission system to
support fine-grained security control. If you use open source Apache RocketMQ, you must build your own security framework.
2. **Stability**: ApsaraMQ for RocketMQ provides official technical support and hardware
adaptation and optimization. However, open source Apache RocketMQ relies on community maintenance, which supports limited hardware compatibility.
3. **Disaster recovery**: ApsaraMQ for RocketMQ provides advanced built-in disaster recovery
solutions, such as active geo-redundancy. If you use open source Apache RocketMQ, you must integrate with third-party tools to implement advanced disaster recovery capabilities.
4. **Observability**: ApsaraMQ for RocketMQ is integrated with a variety of CloudMonitor
features to support holistic observability, while open source Apache RocketMQ relies on third-party tools.
5. **Scalability**: ApsaraMQ for RocketMQ supports scaling within or across clusters. However,
open source Apache RocketMQ requires manual operations and are limited by the hardware environment provided by the community.
6. **Multi-chip support**: ApsaraMQ for RocketMQ allows you to deploy heterogeneous chips in
multiple clusters. However, open source Apache RocketMQ clusters must use the same type of chip.

## Features

Message Queue for Apache RocketMQ is a distributed messaging middleware service built on Apache RocketMQ. It provides SDKs for multiple programming languages and a wide range of management tools. The service also offers purpose-built features for different use cases, such as dead-letter queues and message queries. The following sections describe these features in detail.

**Instance management**

| Feature | Description |
|---|---|
| Create instance | Create a Message Queue for Apache RocketMQ instance. An instance acts as an isolated server or service environment that receives, stores, and forwards messages. Create instances in a specified cluster and region. Specify the organization, resource group, and chip architecture during instance creation. Set TPS limits for message sending and subscription. |
| Query instance list | Query the list of instances you have created in a specified region. The list includes details such as instance ID/name, instance type, cluster ID, department, and status. |
| View instance details | View the basic information, network information (endpoints), topic information, group information, message query capabilities, and peak TPS of an instance. |
| Modify instance specifications | Modify the configurations of a selected instance, including its name, description, maximum topic count, message sending TPS, and message subscription TPS. |
| Network management | A TCP endpoint for private network access is available by default. Note To use an HTTP endpoint for private network access, you must add the HTTP component. You can modify an instance's VPC ID, vSwitch, and VPC name. You can also bind and unbind VPCs. |
| Delete instance | Delete an instance. |
| Instance-level throttling | Enable instance-level throttling based on the TPS you specified during instance creation. If throttling is enabled, the service rejects message production when the TPS limit is reached. |

| Scale out instance | Scale out the brokers of an instance. This feature supports partition load balancing and automatically redistributes partitions after the scale-out is complete. |
|---|---|
| Operation logs | Review operation logs to quickly diagnose issues and improve troubleshooting efficiency. |
| Data integration | Use fully managed, O&M-free connectors to synchronize data between Message Queue for Apache RocketMQ and other Alibaba Cloud services. |

**Topic management**

| Feature | Description |
|---|---|
| Create topic | Create topics for different message types, including normal, partitionally ordered, scheduled/delayed, and transactional messages. |
| Query topic list | View a list of created topics, including their names, types, permissions, descriptions, and available operations. You can perform a fuzzy search by topic name. |
| Edit topic description | Modify the description of a topic. |
| Delete topic | Delete a selected topic. |
| Send message | Quickly verify message sending and receiving, message backlog, and redelivery of failed messages for a selected topic. |
| Resource reports | Use resource reports to gather statistics and query data about message production and consumption. |
| View subscriptions | View the subscriptions of a topic. |

**Group management**

| Feature | Description |
|---|---|
| Create group | After you select the protocol type for a group, you can create a group for the selected instance and set its description. |
| Query group list | View the list of groups for a selected instance, including their group ID, creation time, permissions, description, and available operations. |

| View subscriptions | View the subscriptions of a group. |
|---|---|
| View consumer status | View comprehensive information for a selected group and details for each consumer client in the group, including online status, subscriptions, consumption TPS, message backlog, and thread stack information. |
| Resource reports | Use resource reports to gather statistics and query data about message production and consumption. |
| Reset consumption offset | Reset the consumption offset for a selected group. You can clear the entire message backlog and start consuming from the latest offset, or reset the consumption offset to a specific point in time. |
| Delete group | Delete a selected group. |

**Message trace**

| Feature | Description |
|---|---|
| Query message trace by Message ID | Query a message trace by Message ID. You must provide the message's unique Message ID, the topic, and the approximate send time. This method provides fast and precise results. |
| Query message trace by message key | Query a message trace by message key. You must provide the message key, the topic, and the approximate send time. This method performs a fuzzy search and can return up to 1,000 traces. |
| Query message traces by topic | Query message traces by topic. This method performs a range query. Although you only need to provide the topic and time range, the query may return a large number of messages and lacks granularity. |
| View trace | View information about the message producer, topic, and consumers. You can also export the queried message trace as an image. |

**Message routing**

| Feature | Description |
|---|---|
| Cross-cluster message synchronization | Use routing rules to dynamically plan message synchronization paths to synchronize messages from a source node to a destination node based on filtering conditions. This feature enables real-time, long-distance, cross-cluster message synchronization with millisecond-level latency, ensuring data consistency and integrity between clusters. |

**Message query**

| Feature | Description |
|---|---|
| Query message by Message ID | Query for a message in a specific topic by using its Message ID. This is a precise query that requires only the topic and Message ID to find a specific message. |
| Query message by message key | Query for messages in a specific topic by message key. The service creates an index based on the message key you set. When you query by topic and message key, the service uses this index to find and return matching messages. |
| Query messages by topic | Query for messages by topic. This method retrieves all messages within a specified time range for a given topic. |
| Consumption verification | Resend a queried message. |
| Download message | Download a queried message. |

**Dead-letter queue**

The service provides a dead-letter queue for messages that fail to be consumed after the maximum number of retries. By managing these dead-letter messages, you can prevent message loss. You can query, export in bulk, and resend dead-letter messages.

| Feature | Description |
|---|---|
| Query dead-letter messages by group ID | Query all dead-letter messages generated by a specific group ID within a specified time range. |
| Query dead-letter message by Message ID | Query for a specific dead-letter message by its group ID and Message ID. |
| Export dead-letter messages | Export dead-letter messages individually or in bulk. The exported file is in CSV format. |
| Resend dead-letter messages | Resend dead-letter messages. |

**Monitoring**

CloudMonitor provides real-time resource monitoring, data collection and visualization, and real-time alerts and notifications. You can create monitoring and alert rules in CloudMonitor to automatically monitor the operational status of your services and send alert notifications. This helps you proactively detect service anomalies and improve operational efficiency.

| Feature | Description |
|---|---|
| Service monitoring | Monitor instances at the following levels of granularity in real time: instance group topic topic and group |
| View monitoring metrics | View metric charts for selected resources. |
| Create alert rule | Create alert rules by using CloudMonitor. |

**High scalability**

| Feature | Description |
|---|---|
| Seamless scale-out and scale-in | Seamlessly scale out and scale in your resources. Adding or removing a node does not affect users or normal cluster operation. |
| Multi-dimensional scaling | Scale your resources horizontally across multiple dimensions, including clusters, nodes within a cluster, topics, and queues. |

**High availability**

| Feature | Description |
|---|---|
| No single point of failure | The service has no single point of failure. It uses a large-scale distributed cluster architecture where each node runs independently. If one node fails, other nodes in the cluster remain unaffected. |
| Overload protection | If traffic exceeds system capacity, overload protection ensures that services operating within the capacity limits remain unaffected. |
| Geo-redundancy | The service uses bidirectional data synchronization between instances and traffic switching capabilities to decouple service recovery from fault recovery to ensure business continuity in fault scenarios. |

## Scenarios

ApsaraMQ for RocketMQ is applicable for distributed transactions, real-time computing, Internet of Things (IoT) applications, and large-scale cache synchronization.

**Asynchronous decoupling and peak-load shifting**

ApsaraMQ for RocketMQ was first developed as a core system for the Double 11 Shopping Festival. ApsaraMQ for RocketMQ is widely used for asynchronous decoupling and peak-load shifting in microservices systems such as logistics, shopping cart, and credit point systems. ApsaraMQ for RocketMQ provides the following benefits:

**Optimized data processing**

ApsaraMQ for RocketMQ decouples upstream businesses from downstream systems and accelerates the processing of serverless calls. After decoupling is performed, the system can respond faster and the development efficiency is higher.

**High system stability**

ApsaraMQ for RocketMQ was first developed for online businesses and e-commerce transactions. Compared with traditional message-oriented middleware, ApsaraMQ for RocketMQ provides not only the asynchronization capability, but also the peak-load shifting capability. Peak-load shifting improves system stability and reduces business costs. The peak-load shifting feature requires message-oriented middleware to support a large number of accumulated messages and a traffic model in which hot messages and cold messages are mixed. ApsaraMQ for RocketMQ supports the accumulation of hundreds of millions of messages. It can accommodate traffic spikes in scenarios such as big sales promotions and ensure the stable and secure running of downstream services.

**Distributed transactions**

In traditional transaction processing mode, interactions among different systems are coupled into one transaction. This extends the response time and affects system availability. The introduction of distributed transactional messages creates a transaction processing workflow between transaction systems and ApsaraMQ for RocketMQ to ensure data consistency between distributed systems. Downstream business systems such as shopping carts and credits are isolated from each other and concurrently process transactions. Figure 1. Distributed transactions

**Real-time computing**

Data that is continuously generated by a source flow to a computing engine in real time by using ApsaraMQ for RocketMQ. This achieves real-time computing. You can use the following computing engines: Spark, Storm, E-MapReduce, Application Real-Time Monitoring Service (ARMS), and Beam Runner. Figure 2. Real-time computing

**IoT applications**

IoT devices connect to the cloud by using ApsaraMQ for MQTT for bidirectional communication and data transmission. Device data is connected to a computing engine by using ApsaraMQ for RocketMQ. Analysis data or source data is efficiently written to a data store such as a time series database (TSDB), HiStore, or MaxCompute in real time. Figure 3. IoT applications

**Large-scale cache synchronization**

In business promotion activities such as the Double 11 Shopping Festival, each branch has a wide range of products, and the price of each product changes in real time. A huge number of concurrent access requests for the product database results in long response time on the web page of each branch. In centralized caching mode, the bandwidth becomes a bottleneck which blocks access requests to product prices. ApsaraMQ for RocketMQ can reduce the page response time by means of large-scale cache synchronization for different branches. This allows customers to access product prices. Figure 4. Large-scale cache synchronization es

## Instance types

This topic describes the instance types that Message Queue for Apache RocketMQ supports. You can use this information to select an instance type that meets your requirements.

**Instance types**

Message Queue for Apache RocketMQ provides the following instance types:

| Specific ations | Container CPU (cores) | Container memory (GB) | Container storage (GB) | TPS | Number of topics & GIDs |
|---|---|---|---|---|---|
| 30xlarge | 32 | 186 | 900 | 30000 | 2000 |
| 40xlarge | 56 | 240 | 1800 | 40000 | 2500 |
| 60xlarge | 88 | 368 | 1800 | 60000 | 3000 |
| 80xlarge | 120 | 496 | 1800 | 80000 | 3500 |

## Limits

This topic describes the limits on specific metrics in Message Queue for Apache RocketMQ. To avoid system exception errors, do not exceed the limits when you use Message Queue for Apache RocketMQ. The following table describes the limits. Table 1. Limits of Message Queue for Apache RocketMQ

| Restrictions | Limit | Description |
|---|---|---|
| The length of a topic name | 64 characters | The topic name cannot exceed this length limit. Otherwise, you will be unable to send or subscribe. |
| The size of a message | A normal message or an ordered message: 4 MB A transactional message, a scheduled message, or a delayed message: 64 KB Note Message attributes are part of a message. The size of message attributes cannot exceed 1 KB. | The size of a message cannot exceed the maximum size that is allowed for the message type. If the size of a message exceeds the corresponding limit, the message fails to be sent. |
| Message retention period | Three days | Messages can be retained for up to three days. After the three-day retention period ends, the system automatically deletes the messages. |
| Consumer offset resetting | Three days | Consumer offsets can be reset for messages that are retained within the previous three days. |
| The rate of transactions per second (TPS) for sending and receiving messages on a single Message Queue for Apache RocketMQ instance | For a cluster that consists of two primary brokers and two secondary brokers, a message of 1 KB size is used as a baseline. The following data is verified in the test environment: Messages that are sent and received per second: 30,000 Note A maximum of 10,000 messages can be sent per second. | N/A |

| Delay time of scheduled or delayed messages | 40 days | msg.setStartDeliverTime parameter can be set to a point in time within the following 40 days. The unit of the parameter value is milliseconds. If the specified point in time is not within the 40 days, the message fails to be sent. |
|---|---|---|
| Concurrent scheduled messages | 200 for a default cluster | If the default limit does not meet your requirements, contact Alibaba Cloud technical support to submit a request. |
| Concurrent transactional messages | 200 for a default cluster | If the default limit does not meet your requirements, contact Alibaba Cloud technical support to submit a request. |

## Terms

This topic introduces the terms related to Message Queue for Apache RocketMQ to help you better understand and use this service.

**Topic**

A topic is used to classify messages. It is the primary classifier.

**Message**

In Message Queue for Apache RocketMQ, a message is a carrier that is used to transfer information.

**Message ID**

A message ID is a globally unique identifier for a message. Each message ID is automatically generated by the system.

**Message key**

A message key is a unique identifier for the service logic of a message. Each message key is set by a producer.

**Tag**

A tag is used to further classify messages within a topic. It is the secondary classifier.

**Producer**

A producer, also known as a message publisher, produces and sends messages.

**Producer instance**

An object instance of a producer. Different producer instances can run in different processes or on different machines. Producer instances can be shared among producer instance threads in the same process because these threads are secure.

**Consumer**

A consumer, also known as a message subscriber, receives and consumes messages.

**Consumer instance**

An object instance of a consumer. Different consumer instances can run in different processes or on different machines. A thread pool is configured for a consumer instance to consume messages.

**Group**

A group consists of producers or consumers that produce or consume messages of the same type and publish or subscribe to messages based on the same logic.

**Group ID**

A group ID identifies a group.

**Queue**

Each topic has one or more queues to store messages.

**Exactly-once delivery semantics**

Messages that are sent to the system can be consumed by consumers only once even when a message consumption retry occurs.

**Clustering consumption**

All consumers that are identified by the same consumer ID consume messages in an even manner. For example, if a topic contains nine messages and three consumer instances are identified by the same consumer ID, each of the three consumer instances consumes three messages in clustering consumption mode.

**Broadcasting consumption**

Each of the consumers that are identified by the same consumer ID consume each message once. For example, if a topic contains nine messages and three consumer instances are identified by the same consumer ID, each of the three consumer instances consumes the nine messages in broadcasting consumption mode.

**Scheduled message**

A producer sends a message to a RocketMQ broker and expects the message to be delivered to a consumer at a specified time in the future. The message is a scheduled message.

**Delayed message**

A producer sends a message to a RocketMQ broker and expects the message to be delivered to a consumer after a specified period of time. The message is a delayed message.

**Transactional message**

Message Queue for Apache RocketMQ provides a distributed transaction processing feature that is similar to X/Open XA to ensure transaction consistency by using transactional messages.

**Ordered message**

An ordered message is a message that is published and consumed in order. Ordered messages in Message Queue for Apache RocketMQ are classified into globally ordered messages and partitionally ordered messages.

**Ordered delivery of messages**

For a specified topic, a producer sends messages in specific order.

**Ordered consumption of messages**

For a specified topic, a consumer receives messages in first in, first out (FIFO) order.

**Globally ordered message**

All messages of a specified topic are published and consumed in strict FIFO order.

**Partitionally ordered message**

All messages of a specified topic are segmented by the sharding key. Messages in the same shard are published and consumed in strict FIFO order. A sharding key is a key field that is used in ordered messages to distinguish different shards. It is completely different from the key that is used in regular messages.

**Message accumulation**

A producer has sent messages to a RocketMQ broker but a consumer cannot consume all the messages in a short period of time due to limited consumption capability. Therefore, unconsumed messages are stored on the RocketMQ broker. This process is called message accumulation.

**Message filtering**

A subscriber can filter messages by tag so that the subscriber receives only the filtered messages. Messages are filtered on a RocketMQ broker.

**Message tracing**

The complete trace data of a message is aggregated by the time and location data of each node during the process from message delivery by a producer to message consumption by a subscriber. Message tracing records the complete trace of a message from its delivery by a producer to a RocketMQ broker and then to a consumer. This facilitates troubleshooting.

**Consumer offset reset**

The timeline is used as coordinates. A subscriber can reset the consumption progress of a topic that is subscribed to over the time span of persistent message storage. By default, messages are stored for three days. After the consumer offset is reset, the subscriber can receive messages that are sent by a producer to a RocketMQ broker after the specified point in time.
