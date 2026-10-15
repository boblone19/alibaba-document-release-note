---
title: "Alibaba Cloud Apsara Stack v3.18.6-2607 Alibaba Cloud Message Queue RocketMQ v5.0 Product Introduction 20260828"
product_version: "V3.18.6_2607"
doc_version: "20260828"
pdf_pages: 25
source_pdf: "Alibaba Cloud Apsara Stack v3.18.6-2607 Alibaba Cloud Message Queue RocketMQ v5.0 Product Introduction 20260828.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/3816%202607/pdf%203/%E4%BA%91%E6%B6%88%E6%81%AF%E9%98%9F%E5%88%97%20RocketMQ%20%E7%89%88/Alibaba%20Cloud%20Apsara%20Stack%20v3.18.6-2607%20Alibaba%20Cloud%20Message%20Queue%20RocketMQ%20v5.0%20Product%20Introduction%2020260828.pdf"
converter: pdf2md (PyMuPDF line classifier)
---

# Alibaba Cloud Apsara Stack v3.18.6-2607 Alibaba Cloud Message Queue RocketMQ v5.0 Product Introduction 20260828

## ApsaraMQ for RocketMQ

## x

ApsaraMQ for RocketMQ 5.x is a distributed messaging middleware that is developed by Alibaba Cloud based on Apache RocketMQ 5.x. It features low latency, high concurrency, high availability, and high reliability. ApsaraMQ for RocketMQ 5.x is a core service in the enterprise-level Internet architecture. Using the highly available distributed cluster technology, it offers a series of messaging services in the cloud, including message subscription and publishing, message trace query, scheduled and delayed messages, and resource statistics. ApsaraMQ for RocketMQ 5.x provides asynchronous decoupling and peak-load shifting capabilities for distributed application systems. It also supports various features for Internet applications, including accumulation of large numbers of messages, high throughput, and reliable message consumption retries. ApsaraMQ for RocketMQ 5.x is one of the core cloud services that are used to support Double 11. ApsaraMQ for RocketMQ 5.x supports connections over TCP and supports multiple programming languages such as Java, C++, and .NET. This allows you to connect applications that are developed in different programming languages to ApsaraMQ for RocketMQ 5.x. ApsaraMQ for RocketMQ 5.x uses a compute-storage separation architecture to support independent scaling of computing and storage resources. This enables a lighter-weight deployment mode and a more flexible and miniaturized cluster configuration, reducing resource overheads and O&M complexity.

## Product details

This topic describes the basic principles of Cloud Message Queue and the core features and technical specifications of . supports the TCP protocol and provides software development kits (SDKs) for multiple programming languages. It delivers high performance and ensures high availability through a multi-replica mechanism. It also supports enterprise-grade features, such as message traces and dead-letter queues, and provides multi-dimensional O&M and management tools.

**How Cloud Message Queue works**

Cloud Message Queue is based on the classic message queue model. It provides an intermediary layer for asynchronous communication between distributed systems. The main components are producers, consumers, messages, and queues.
**Producers:** Also known as publishers, they are applications or services that send
messages to a queue.
**Consumers:** Also known as subscribers, they are applications or services that pull and
process messages from a queue.
**Messages:** The basic unit of communication. A message can contain text, binary data, or
structured data.
**Queues:** A temporary storage area for messages. In a point-to-point model, each message
can be received by only one consumer. In a publish/subscribe pattern, a message is distributed to one or more subscribers. The general workflow of Cloud Message Queue is as follows:
1. A producer creates a message and sends it to a message queue.
2. The message queue service ensures message persistence to prevent data loss from system
failures.
3. A consumer connects to the message queue. It then pulls or receives messages from the
queue on demand, or through methods such as long polling and push mechanisms.
4. After a consumer processes a message, it usually sends an acknowledgement (ACK). The
ACK indicates that the message was processed successfully. The message is then deleted from the queue to prevent it from being processed again. Cloud Message Queue improves reliability through redundant storage and data replicas. This ensures that messages are not lost even if some system components fail. The service can automatically scale to adapt to changes in payload, without manual intervention.

**Core features and technical specifications**

**Producers: Message types and scenarios**

**Message types**

Normal messages: Suitable for asynchronous communication, such as log collection and event notifications. Transactional messages: Ensure the atomicity of business operations and message sending. Examples include order payments and inventory deductions. Ordered messages: Ensure messages are strictly ordered based on a business dimension, such as an order ID. An example is a financial transaction stream. Scheduled and delayed messages: Support message delivery with millisecond-level delays. An example is closing an order after a timeout.

**Core capabilities**

Topic classification: Use topics to divide business logic and distribute messages. Tags: Refine message classification and allow consumers to filter messages by tag. Batch sending: Improve sending efficiency and reduce network overhead.

**Consumers: efficient consumption and reliability**

**Consumption modes**

Clustering consumption: A message is consumed by only one instance in a consumer group. This is suitable for high-throughput scenarios, such as order processing. Broadcasting consumption: A message is consumed by all instances in a consumer group. This is suitable for global notification scenarios, such as configuration delivery.

**Consumer group**

Load balancing: Automatically distribute message queues to consumer group instances to enable parallel consumption. Failover: Automatically migrate tasks after a broker goes down to ensure consumption continuity. Horizontal scaling: Increase the number of brokers to improve consumption capacity.

**Offset**

Reset offsets: Reset the consumption progress based on a specific time. This allows you to trace back messages or discard stacked messages.

**Push and pull modes**

Push model: The broker actively pushes messages. This is suitable for scenarios that require high real-time performance. Pull model: The consumer actively pulls messages. This is suitable for batch processing or low-latency scenarios.

**Consumption assurance**

Supports failed message retries (up to 16 times) and automatic isolation to a dead-letter queue (DLQ). Supports message filtering (by tag or SQL) to reduce unnecessary processing.

**High-performance and high-availability architecture**

**Throughput:** A single cluster supports millions of transactions per second (TPS) with
millisecond-level latency. This meets the needs of high-concurrency businesses.
**Multi-replica mechanism:** Data is backed up and synchronized across replicas. This
supports cross-region disaster recovery and ensures availability.
**Decoupled storage and compute architecture:** Message computation (reception,
forwarding, and protocol parsing) is fully decoupled from persistent storage.

**Enterprise-grade features**

**Protocol support:** Supports the TCP protocol. Provides SDKs for multiple languages, such
as Java, C/C++, and .NET.
**Message trace:** Tracks the entire flow of a message to help you quickly locate issues.
**Dead-letter queue:** Stores messages that cannot be consumed normally in a special
queue for later processing. This isolates failed messages and prevents them from blocking the normal flow.
**Access control:** Supports multi-layer security protection based on VPCs, RAM roles, and IP
whitelists. This meets the compliance requirements of industries such as finance and healthcare.
**Resource reports:** Provides statistics on message production and consumption. For a
given period, you can query the total number of messages or the TPS for messages sent to a topic, or for messages delivered to a group ID.

**Management tools**

**Web console:** Supports topic management, group management, message queries,
message traces, and resource reports.
**OpenAPI:** Provides APIs that allow customers to integrate management tools into their
own consoles.
**mqadmin command set:** Apsara Stack provides a rich set of management commands to
manage the service.

**Apsara Stack deployment**

**Flexible deployment:** Supports standalone deployment on Apsara Stack and supports
hybrid cloud architectures.
**O&M control:** Apsara Stack supports the mqadmin command set and OpenAPI O&M tools.
This simplifies integration with management platforms and enables unified O&M.

## Benefits

is a professional message middleware that provides benefits such as high reliability, high availability, and high performance. It supports TCP connections and on-premises deployment.

**Benefits**

**Professional**

ApsaraMQ for RocketMQ is a professional message middleware with a mature technical system that ensures zero message loss. Its open source version, Apache RocketMQ, has won multiple domestic and international awards. Over 1,000 core applications within Apsara Stack use it to process hundreds of billions of messages daily. It is proven stable and reliable in real-world scenarios, including the core systems for Double 11 transactions and products.

**Highly reliable**

Each message is stored on disk in multiple copies. Strict power outage tests ensure zero message loss. The system supports massive message accumulation and remains reliable under high traffic pressure, even when a single topic accumulates over 10 billion messages. By default, messages are stored for 3 days. You can reset the consumer offset to consume messages from any point in time within this period.

**High-performance**

It supports horizontal scaling. It supports messages up to 4 MB, including message attributes.

**TCP support**

It provides TCP connections and supports multiple programming languages, such as Java, C++, and .NET.

**On-premises deployment**

It supports deployment on Apsara Stack and physical servers. You can build a complete cloud messaging service with just a few servers. Apsara Stack provides the mqadmin command set and management OpenAPI. This allows operations and maintenance (O&M) engineers to monitor the system status in real time. It supports a hybrid cloud architecture. You can connect to public cloud services over a leased line.

**Comparison with open source**

Apsara Stack has several advantages over the open source version of in the following five dimensions:

| Category | Apsara Stack | Open source version |
|---|---|---|

| Security | Continuous security vulnerability fixes with automatic updates and patch support. An integrated Apsara Stack account permission system shared across all Apsara Stack services. Multi-tenant data isolation capabilities. Flexible resource access management methods, such as RAM users and role assumption through Security Token Service (STS). Fine-grained access control for API permissions. | Security vulnerability fixes depend on the community, requiring users to perform updates manually. Basic Access Control List (ACL) permissions without multi-tenant data isolation. Requires you to configure your own permission management solution. Weak API permission management that relies on custom user configurations. |
|---|---|---|
| Stability | Fast product issue resolution with support from the Apsara Stack team. Compatibility with multi-architecture chip processors, such as ARM and x86. Clear performance and capacity metrics that make the performance of each chip quantifiable. Mature O&M and change management solutions with a visual interface and automated O&M toolchain. | Issue resolution depends on the open source community, which can have longer response times. Limited chip compatibility, mainly supporting mainstream architectures. Performance metrics require users to test and optimize on their own. O&M experience depends on the user's expertise, with no ready- made solutions available. |
| Observability | A rich, built-in system of monitoring metrics that covers the underlying physical resource layer, platform layer, and tenant service layer. Metrics include message latency, throughput, and cluster status. Supports custom monitoring and alerting, with deep integration with CloudMonitor. Visualization dashboards and alerting capabilities. Continuous optimization of monitoring dimensions and metric granularity. | Relies on the basic monitoring included with the open source version, which has limited metrics. Requires integration with third- party tools, such as Prometheus and Grafana, for advanced monitoring. Custom observability solutions must be developed by the user. Updates to monitoring metrics depend on community iterations. |
| Elasticity | Provides intra-cluster and multi-cluster scaling capabilities. | Elastic scaling depends on manual operations or third-party tools. Elasticity is limited by the hardware environments supported by the open source community. |

| Multi-chip support | Supports mixed deployment of different chips across multiple clusters, such as using ARM and x86 clusters together. A single cluster requires the same chip type, but different clusters can be heterogeneous. Chip performance optimization and adaptation, with official performance optimization guidance from Apsara Stack. | A single cluster requires the same chip type. Mixed deployment of heterogeneous chips is not supported. Chip compatibility requires users to test and optimize on their own. |
|---|---|---|

**Key takeaways**

**Security**: Apsara Stack provides more fine-grained security control through a mature
account and permission system. The open source version requires you to build your own security framework.
**Stability**: Apsara Stack provides official support and hardware compatibility optimizations.
The open source version relies on community maintenance, and its hardware compatibility may be limited.
**Observability**: Apsara Stack integrates multiple cloud monitoring capabilities to provide
more comprehensive observability. The open source version requires third-party tools.
**Elasticity**: Apsara Stack provides intra-cluster and multi-cluster scaling capabilities. The
open source version requires manual operations and is limited by the hardware environments supported by the community.
**Multi-chip support**: Apsara Stack supports heterogeneous chip deployment across
multiple clusters. The open source version only supports the same chip type within a single cluster.

## Features

is a distributed messaging middleware service developed based on Apache RocketMQ. It provides access methods for multiple programming languages and multi-dimensional management tools, along with a range of distinctive features such as dead-letter queues and message queries for different application scenarios. The following sections describe these features in detail.

**Instance management**

| Feature | Description |
|---|---|
| Instance creation | Create an instance. This instance functions as an isolated server or service environment that receives, stores, and forwards messages. You can create instances of different specifications. You can select the organization, resource set, and chip architecture of the instance during creation. You can set TPS limits for message sending and subscription. |
| Instance list query | Query the list of instances that you created in a specified region. The list includes the instance ID/name, instance type, cluster ID, department, and status. |
| Instance details | View the basic information, network information (endpoints), topic information, group information, message query results, and peak TPS of an instance. |
| Instance specification modification | Edit a selected instance to modify the instance name, description, maximum number of topics, message sending TPS, and message subscription TPS. |
| Network management | The system provides a default internal endpoint for TCP protocol clients. |
| Instance deletion | Delete an instance. |
| Instance-level throttling | The system supports instance-level throttling based on the TPS concurrency configured during instance creation. If throttling is enabled, the system rejects message production when the message concurrency reaches the limit configured for the instance. |
| Instance scale-out | Scale out the brokers of an instance. The system supports partition load balancing and automatically redistributes partitions after the scale-out is complete. |
| Operation logs | View operation logs to quickly identify the cause of issues and improve troubleshooting efficiency. |

**Topic management**

| Feature | Description |
|---|---|
| Topic creation | Create a message topic. Supported message types include normal messages, partitionally ordered messages, scheduled and delayed messages, and transactional messages. |
| Topic list query | View the list of created topics, including the topic name, type, permissions, description, and actions. You can perform fuzzy searches by topic name. |
| Topic description modification | Modify the description of a topic. |
| Topic deletion | Delete a selected topic. |
| Message sending | Send and receive messages on a selected topic to quickly verify message accumulation and failed message redelivery capabilities. |
| Resource reports | Use resource reports to collect and query data on message production and consumption. |
| Subscription relationship query | View the subscription relationships of a topic. |

**Group management**

| Feature | Description |
|---|---|
| Group creation | Select the protocol type of a group to create a group for the selected instance and configure its description. |
| Group list query | View the list of created groups under the selected instance, including the group ID, creation time, permissions, description, and actions. |
| Subscription relationship query | View the subscription relationships of a group. |
| Consumer status | View the aggregate information of the selected group and the information of individual consumers in the group, including the online status, subscription relationships, consumption TPS, message accumulation, and thread stack information. |

| Resource reports | Use resource reports to collect and query data on message production and consumption. |
|---|---|
| Consumption offset reset | Reset the consumption offset for the selected group. You can clear all accumulated messages and start consumption from the latest offset, or reset the consumption offset to a specific point in time. |
| Group deletion | Delete the selected group. |

**Message tracing**

| Feature | Description |
|---|---|
| Message trace query by message ID | Query message traces by message ID. You must enter the unique message ID, topic, and approximate sending time of the message. This method delivers fast queries and precise matching. |
| Message trace query by message key | Query message traces by message key. You must enter the message key, topic, and approximate sending time of the message. This method performs a fuzzy query and can retrieve up to 1,000 traces. |
| Message trace query by topic | Query message traces by topic. This method performs a range query. You only need to enter the topic and time range, but the query returns a large number of messages within the specified time range and lacks differentiating attributes. |
| Message trace query | View the producer information, topic information, and consumer information of a message, and export the queried message traces as a trace image. |

**Message query**

| Feature | Description |
|---|---|
| Message query by message ID | Query messages in a specified topic by message ID. This method performs an exact query, and you only need to enter the topic and message ID to accurately find any message. |
| Message query by message key | Query messages in a specified topic by message key. creates an index for messages based on the message key that you configure. When you enter the topic and message key to perform a query, matches and returns the relevant messages based on this index. |
| Message query by topic | Query messages by topic. This method retrieves all messages in a topic within a specified time range in batches so that you can find the target data. |

| Consumption verification | Resend the queried messages. |
|---|---|
| Message download | Download the queried messages. |

**Dead-letter queues**

Dead-letter queues are supported to handle messages that fail to be consumed after the maximum number of retries. These messages are known as dead-letter messages. Managing dead-letter messages prevents message loss. Features include querying, batch exporting, and redelivering dead-letter messages.

| Feature | Description |
|---|---|
| Dead-letter message query by group ID | Query all dead-letter messages generated by a specific group ID within a specified time range based on the group ID and the time range when the dead-letter messages were generated. |
| Dead-letter message query by message ID | Perform an exact query to find any specific message based on the group ID and message ID. |
| Dead-letter message export | Export dead-letter messages individually or in batches. The exported files use the CSV format. |
| Dead-letter message resending | Resend dead-letter messages. |

**Monitoring**

CloudMonitor provides real-time resource monitoring, monitoring data collection and visualization, and real-time alerting and notifications. You can use CloudMonitor to create monitoring and alert rules, automatically monitor service status, and send alert notifications to promptly detect service anomalies and improve O&M efficiency.

| Feature | Description |
|---|---|
| Service monitoring | Monitor instances in real time at the following granularities: Instance Group Topic Topic & Group |
| Monitoring metric query | View monitoring metric charts for selected resources. |
| Alert rule creation | Use CloudMonitor to create alert rules. |

**High scalability**

| Feature | Description |
|---|---|
| Smooth scaling | The system supports smooth scaling. Adding or removing nodes is transparent to users and does not affect normal cluster services. |
| Multi-dimensional scaling | The system supports multi-dimensional horizontal scaling across multiple clusters, multiple nodes within a cluster, multiple topics, and multiple queues. |

**High availability**

| Feature | Description |
|---|---|
| No single point of failure | The system eliminates single points of failure by using a large-scale distributed cluster architecture. Nodes in the cluster run independently. If one node goes down, it does not affect other nodes in the cluster. |
| Overload protection | The system provides overload protection. When traffic exceeds the system capacity, services within the capacity limit remain unaffected. |

## Scenarios

supports distributed transactions, real-time computing, Internet of Things (IoT) applications, and large-scale cache synchronization.

**Asynchronous decoupling and peak-load shifting**

was first used in the core systems for Alibaba's Double 11 sales event. It is now widely used in microservice systems for logistics, shopping carts, and reward points. The service provides asynchronous decoupling between systems and shifts traffic during peak loads.

**Shorten service invocation paths with asynchronous**

**decoupling**

decouples upstream services from downstream systems. This shortens the service invocation path. Asynchronous systems have faster response times, support loose coupling between upstream and downstream components, and increase developer efficiency.

**Improve stability with peak-load shifting**

Traditional middleware only provides asynchronous processing. was designed for online transaction scenarios. It provides both asynchronous capabilities and peak-load shifting as a core feature. Peak-load shifting improves system stability and greatly reduces business costs. To provide peak-load shifting, middleware needs to support massive message accumulation and manage traffic with mixed hot and cold messages. can accumulate hundreds of millions of messages. It handles traffic spikes during events such as major sales promotions. This ensures downstream services operate smoothly and stably within safe limits.

**Distributed transactions**

In traditional transaction processing, interactions between multiple systems are coupled into a single transaction. This results in long response times and affects system availability. Distributed transaction messages integrate the transaction system and the message queue into one transaction process. This ensures eventual data consistency between distributed systems. Downstream systems, such as those for shopping carts and reward points, are isolated and can process tasks in parallel. Figure 1. Distributed transaction scenario

**Real-time computing**

streams continuously generated source data to a compute engine for real-time computing. Supported compute engines include Spark, Storm, EMR, ARMS, and BeamRunner. Figure 2. Real-time computing scenario

**IoT applications**

IoT devices connect to the cloud through a micro message queue for bidirectional communication and data transmission. Device data is sent through to compute engines. The data can then be analyzed or efficiently written in real time to services such as TSDB, HiStore, and MaxCompute. Figure 3. IoT application scenario

**Large-scale cache synchronization**

During major sales promotions, such as the Double 11 event, many products are displayed and their prices change in real time. High concurrent access to the product database leads to long page response times. A centralized cache creates a bandwidth bottleneck and cannot handle the high demand for product price information. reduces page response times through large-scale cache synchronization. This approach involves a multi-cache design for different sales venues to meet the high demand for accessing product prices. Figure 4. Large-scale cache synchronization scenario

## Limits

enforces constraints on specific metrics. When you use , ensure that you do not exceed the corresponding limits to prevent system exceptions. The following table describes the specific limits and their values. Table 1. Limits

| Limit | Value | Description |
|---|---|---|
| Topic name length | 64 characters | The topic name length cannot exceed this limit. Otherwise, the system cannot send or subscribe to messages. |
| Message size | Normal or ordered messages: up to 4 MB Transactional, scheduled or delayed messages: 64 KB Note Message attributes are part of a message. The size of message attributes cannot exceed 1 KB. | The message size cannot exceed the limit for the corresponding message type. Otherwise, the system fails to send messages. |
| Message retention period | 3 days | Messages can be retained for up to three days. After the retention period elapses, the system automatically deletes the messages. |
| Consumer offset reset | 3 days | Consumer offsets can be reset for messages that are sent at a point in time within three days after message consumption. |

| TPS for message sending and receiving per instance | Based on a specification of 32 cores, 186 GB memory with two primary and two secondary nodes, and using a 1-KB message body as a benchmark, the following data is verified in the test environment: Message sending and receiving: 30,000 messages per second Note The system supports sending up to 10,000 messages per second. | None |
|---|---|---|
| Delay duration for scheduled and delayed messages | 3 days | You can set the msg.setStartDeliverTime parameter to any point in time within 3 days (unit: milliseconds). If the value exceeds 3 days, the system fails to send the message. |
| Scheduled message concurrency | Default: 200 for clusters | If the default limit does not meet your requirements, contact Apsara Stack technical support to submit a request. |
| Transactional message concurrency | Default: 200 for clusters | If the default limit does not meet your requirements, contact Apsara Stack technical support to submit a request. |

## Terms

This topic introduces the terms related to to help you understand the concepts and use .

**Topic**

A topic is used to classify messages. It is the primary classifier.

**Message**

A message is a carrier that is used to transfer information.

**Message ID**

A message ID is a globally unique identifier for a message. Each message ID is automatically generated by .

**Message Key**

A message key is a unique identifier for the service logic of a message. Each message key is set by a producer.

**Tag**

A tag is used to further classify messages within a topic. It is the secondary classifier.

**Producer**

A Producer, also known as a message publisher, produces and sends messages.

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

In clustering consumption mode, the system evenly distributes messages in a topic to consumers in a consumer group. For example, if a topic has 9 messages and a consumer ID has 3 consumer instances, each instance consumes 3 messages on average.

**Broadcasting consumption**

In broadcasting consumption mode, every Consumer identified by a Consumer ID consumes each message once. For example, a topic contains nine messages, and a consumer group contains three consumers. In broadcasting consumption mode, each consumer consumes nine messages.

**Scheduled message**

A scheduled message is not immediately sent to consumers after the broker receives the message from the producer. The broker is configured to send the message to consumers at a specific point in time later than the current time.

**Delayed message**

A delayed message is not immediately sent to consumers after the broker receives the message. The broker is configured to send the message to consumers after a specific period of time elapses.

**Transactional message**

Message Queue for Apache RocketMQ provides a distributed transaction processing feature that is similar to X/Open XA to ensure transaction consistency by using transactional messages.

**Ordered message**

An ordered message is a message that is published and consumed in order. Ordered messages in are classified into globally ordered messages and partitionally ordered messages.

**Ordered delivery of messages**

For a specified Topic, a producer sends messages in specific order.

**Ordered consumption of messages**

For a specified Topic, a consumer receives messages in the order they were sent. Earlier messages are always received before later ones.

**Globally ordered message**

For a specified topic, all messages are published and consumed in strict first-in-first-out (FIFO) order.

**Partitionally ordered message**

For a specified topic, all messages are divided into partitions based on a sharding key. Messages within the same partition are published and consumed in strict FIFO order. A sharding key is a critical field that distinguishes different partitions in ordered messages and is entirely different from the key of a regular message.

**Message accumulation**

Message accumulation occurs when a producer has sent messages to a broker, but the consumer cannot consume all messages promptly due to limited processing capability. The broker retains the unconsumed messages in this state.

**Message filtering**

Subscribers can filter messages by message tag to ensure that they receive only the filtered messages. Messages are filtered on a broker.

**Message tracing**

The complete trace data of a message is aggregated by the time and location data of each node during the process from message delivery by a producer to message consumption by a subscriber. Message tracing records the complete trace of a message from its delivery by a producer to a broker and then to a consumer. This facilitates troubleshooting.

**Consumer offset reset**

The timeline is used as coordinates. A subscriber can reset the consumption progress of a topic that is subscribed to over the time span of persistent message storage. By default, messages are stored for three days. After the consumer offset is reset, the subscriber can receive messages that are sent by a producer to a broker after the specified point in time.
