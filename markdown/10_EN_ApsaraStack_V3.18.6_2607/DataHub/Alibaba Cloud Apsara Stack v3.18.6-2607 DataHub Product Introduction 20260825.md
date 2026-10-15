---
title: "Alibaba Cloud Apsara Stack v3.18.6-2607 DataHub Product Introduction 20260825"
product_version: "V3.18.6_2607"
doc_version: "20260825"
pdf_pages: 9
source_pdf: "65b2bb428bb1f72d_Alibaba Cloud Apsara Stack v3.18.6-2607 DataHub Product Introduction 20260825.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/3816%202607/pdf%203/DataHub/Alibaba%20Cloud%20Apsara%20Stack%20v3.18.6-2607%20DataHub%20Product%20Introduction%2020260825.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings)
---

# Alibaba Cloud Apsara Stack v3.18.6-2607 DataHub Product Introduction 20260825

## Table of Contents

- 1 DataHub
  - 1.1 Features
  - 1.2 Benefits
  - 1.3 Scenarios
  - 1.4 Functions and features

## 1 DataHub

### 1.1 Features

DataHub collects, stores, and processes streaming data from mobile devices, applications, website services, and sensors. You can use your own applications or Apsara Stack Realtime Compute to process streaming data in DataHub, such as real-time website access logs, application logs, and events. The processed data is updated in real time and delivered to you in the form of alerts and statistics (visualized as graphs or tables).

**Data queue**

DataHub preserves the order of data within each shard. The performance of a single topic is horizontally scalable by adjusting the number of shards.

**Checkpoint-based data restoration**

DataHub provides the application checkpointing feature. If applications fail, you can restore data from any one of the saved checkpoints.

**Data synchronization**

Data in DataHub is automatically synchronized to other Alibaba Cloud services. You can create a DataConnector to synchronize data in DataHub to other Alibaba Cloud services in real time or near real time. These Alibaba Cloud services include MaxCompute, Object Storage Service (OSS), Elasticsearch, ApsaraDB RDS for MySQL, AnalyticDB, and Tablestore. After you configure DataConnector, data you write to DataHub becomes available to other Alibaba Cloud services. This allows you use the data in other Alibaba Cloud Services. The synchronization process applies at-least-once semantics to ensure data is not lost when errors occur during synchronization. However, this may result in duplicate records.

**Scalability**

DataHub can scale flexibly to increase or decrease the number of shards in a cluster. This allows you to handle traffic surges or save resource costs based on actual business conditions. For example, if the topic has insufficient throughput to cope with the surge in service load during the Double 11 Shopping Festival, you can use the SplitShard operation to increase the number of shards to a maximum of 256 shards in response to the traffic spike. This expands the throughput capacity up to 256 MB/s. When traffic returns to normal after the Double 11 Shopping Festival and you no longer require high throughput capacity, you can use the MergeShard operation to merge every two shards into one.

### 1.2 Benefits

Built on the Apsara system of Alibaba Cloud, DataHub features elastic scalability, high availability, high throughput, and low latency.

**High throughput**

You can write terabytes (TB) of data into a topic and up to 80 million records into a shard every day.

**Low latency**

DataHub makes it easy to collect and process various streaming data in real time so you can react quickly to new information.

**High usability**

DataHub provides a variety of SDKs in different programming language, including C++, Java, Python, Ruby, and Go. In addition to SDKs, DataHub provides RESTful APIs so that you can manage DataHub by using existing protocols. You can use collection tools such as Fluentd, Logstash, and Oracle GoldenGate to write streaming data to DataHub. DataHub supports structured and unstructured data. You can write unstructured data to DataHub, or create a schema for the data before it is written to the system.

**High availability**

No service interruption occurs during auto-scaling. DataHub automatically backs up multiple copies of data to implement data redundancy.

**Dynamic scaling**

The throughput of each topic can be increased or decreased dynamically, with the maximum throughput of a topic reaching 256,000 records per second.

**High security**

DataHub provides enterprise-level security mechanisms and tenant-level isolation. It supports multiple authentication and authorization methods. For example, you can configure an allowlist or grant permissions by using Resource Access Management (RAM).

### 1.3 Scenarios

As a fully managed real-time data streaming service platform of Alibaba Cloud, DataHub is deeply integrated with core products such as MaxCompute, Realtime Compute for Apache Flink, and E-MapReduce (EMR). It provides an end-to-end solution for enterprises, covering real-time data collection, cleaning, and transformation, as well as multi-dimensional analysis. It helps build an efficient and flexible one-stop data processing system.

**Data uploading**

As the core hub for enterprise-level data migration to the cloud, DataHub provides standardized data access layer services. Through a unified API/SDK design, you only need to write data once to enable distribution and consumption across multiple services within the Alibaba Cloud ecosystem. This architecture effectively eliminates the complexity of connecting multiple cloud service APIs in traditional data migration. It is compatible with mainstream computing frameworks such as Kafka, Flink, and Spark Streaming, and supports seamless integration with storage and analysis components such as Object Storage Service (OSS), MaxCompute, and EMR. This implements the data transfer efficiency of "write once, use everywhere".

**Data collection**

DataHub provides several types of data collection tools for you to write your data into DataHub. DataHub supports log collection from Logstash and Fluentd, and binary log collection from Data Transmission Service (DTS) and Oracle GoldenGate (OGG). DataHub also supports the collection of surveillance videos based on the GB/T 28181 standard.

**Data streaming**

You can write applications to subscribe to data in DataHub, process the data in real time, and then output the processed data. You can also use another application to process the streaming data output from the previous application to form a directed acyclic graph (DAG)-based data processing procedure.

**Data archiving**

You only need to create a DataHub connector and configure relevant parameters to archive streaming data to MaxCompute on a regular basis.

### 1.4 Functions and features

This topic describes the features of DataHub.

| Category | Feature | Description |
|---|---|---|
| System-related | Horizontal scaling | Supports online, horizontal, and dynamic scale-in and scale- out. |
|   | Quota management of a single Elastic Compute Service (ECS) instance | Supports single-ECS instance quota management. The number of shards per ECS instance can be configured. The QPS, RPS, and throughput limits for each shard can be configured. |
|   | Throttling policy | Supports various types of throttling policies. |
|   | Distributed resource scheduling | Supports distributed resource scheduling and the fully service-oriented platform. |
|   | Multiple data replicas | Supports multiple data replicas and tolerates single-node failures. |
|   | Multi-cluster disaster recovery | Supports the multi-cluster disaster recovery feature. |
|   | Online hot upgrade | Supports the online hot upgrade. |
|   | Data lifecycle configuration | Supports configuration of data lifecycles. |
|   | Millisecond- level read and write latencies | Supports millisecond-level read and write latencies. |

| Function-related | Data import by using various open source plug-ins | Supports data import by using various open source plug-ins, such as Fluentd, Logstash, and Oracle GoldenGate (OGG). |
|---|---|---|
|   | SDKs for multiple languages | Supports SDKs for multiple languages, such as C++, Java, Python, and Go. |
|   | Structured and unstructured data storage | Supports structured TUPLE and unstructured BLOB storage modes. |
|   | Multi-tenancy | Supports multi-tenancy. |
|   | Multi- subscription | Supports multi-subscription offsets and storage of subscription offsets. |
|   | Synchronization of various types of data sources | Supports synchronization of various types of data sources. MaxCompute is natively supported. |
|   | Publishing and subscription | Supports the publishing and subscription features for common streaming data. |
|   | Various data write modes | Supports various data write modes, such as Hash and PartitionKey. |
|   | Function computing at the backend | Supports function computing at the backend. |
|   | Permission management | Supports the Alibaba Cloud account system and the RAM user system and multi-tenant isolation at the topic granularity. |
| Visualized management- related | Visualized management | Supports visualized permission management. |
|   | Web console management | Supports management in the web console, such as log management, subscription, and creation and deletion of synchronization offsets. |
|   | Visualized log management | Supports visualized log management for different log types, such as logs for creating and deleting synchronization offsets. |

|   | Visualized O&M | Supports visualized O&M, such as log storage capacity scale-ins and scale-outs. |
|---|---|---|
|   | Visualized dashboard monitoring | Supports visualized dashboard monitoring, such as the display of real-time traffic and other parameters. |
