---
title: "Alibaba Cloud Apsara Stack V3.18.2 DataHub User Guide 20240613"
product_version: "V3.18.2"
doc_version: "20240613"
pdf_pages: 9
source_pdf: "Alibaba Cloud Apsara Stack V3.18.2 DataHub User Guide 20240613.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/v3.18.2%E7%89%88%E6%9C%AC%E6%96%87%E6%A1%A3/Datahub/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.2%20DataHub%20User%20Guide%2020240613.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes)
---

# Alibaba Cloud Apsara Stack V3.18.2 DataHub User Guide 20240613

## Table of Contents

- 1 What is DataHub?
- 2 Limits
- 3 Data Archive
  - 3.1 Overview
  - 3.2 Archive to MaxCompute
    - 3.2.1 Create a DataConnector
    - 3.2.2 View archive details
- 4 Performance monitoring

## 1 What is DataHub?

DataHub is a real-time data distribution platform designed to process streaming data. You can publish and subscribe to applications for streaming data in DataHub and distribute the data to other platforms. DataHub allows you to analyze streaming data and build applications based on the streaming data. DataHub collects, stores, and processes streaming data from mobile devices, applications, website services, and sensors. You can use your own applications or Alibaba Cloud Realtime Compute to process streaming data in DataHub, such as real-time website access logs, application logs, and events. The processing results such as alerts and statistics presented in graphs and tables are updated in real time. Based on the Apsara system of Alibaba Cloud, DataHub features high availability, low latency, high scalability, and high throughput. DataHub is seamlessly integrated with Realtime Compute, allowing you to use SQL to analyze streaming data. DataHub also supports synchronizing streaming data to various Alibaba Cloud services such as MaxCompute and OSS. The features of DataHub are described as follows:
**Data queue**: DataHub automatically generates a cursor for each record in a shard. The
cursor is a unique sequence of numbers. You can improve the performance of a topic by increasing the number shards in the topic.
**Checkpoint-based data restoration**: DataHub supports saving checkpoints in the
system. You can restore data from any checkpoint you saved when your application fails.
**Data synchronization**: Data in DataHub can be automatically synchronized to other
Alibaba Cloud platforms, including MaxCompute, Object Storage Service (OSS), AnalyticDB, ApsaraDB RDS for MySQL, Table Store, and Elasticsearch.
**Scalable topics**: DataHub allows you to scale in or out the topic by splitting a shard into
two or merging two shards.

## 2 Limits

Before using DataHub, learn the limits on certain features. The following table describes the limits. Table 1. Limits

| Item | Range | Description |
|---|---|---|
| Active shards | (0,10] | Each topic can contain up to 10 active shards. |
| Shards | (0,512] | You can create up to 512 shards in each topic. |
| HTTP body size | ≤ 4 MB | The HTTP request body size cannot exceed 4 MB. |
| String size | ≤ 1 MB | The size of a string cannot exceed 1 MB. |
| Merge and split operations on new shards | ≥ 5s | You cannot merge a shard with another shard or split the shard in less than 5 seconds after it is created. |
| Queries per second (QPS) | ≤ 1,000 | The write QPS limit for each shard is 1,000. Multiple queries in one batch are considered one query. |
| Throughput | ≤ 1 MB/s | Each shard provides a throughput of up to 1 MB/s. |
| Projects | ≤ 5 | You can create up to 5 projects with each account. |
| Topics | ≤ 20 | You can create up to 20 topics in each project. Contact the administrator if you need to create more topics. |
| Time-to-live of records | [1,7] | The time-to-live of each record in the topic is from 1 to 7 days. |

## 3 Data Archive

### 3.1 Overview

In the DataHub console, you can archive data in DataHub to other data warehouses by using DataConnector so that you can easily analyze and process historical data. This section describes how to archive data in DataHub to MaxCompute.

### 3.2 Archive to MaxCompute

#### 3.2.1 Create a DataConnector

This topic describes how to archive data from DataHub to MaxCompute.
1. Log on to the DataHub console.
2. On the **Projects** page, click **View** in the Actions column of a project. On the project details
page that appears, click View in the Actions column of a topic.
3. On the topic details page, click **+DataConnector** in the upper-right corner and select
**MaxCompute**. Then the **Create DataConnector** dialog box appears.
4. In the **Create DataConnector** dialog box, configure all the required information and click
**Create**.

> **Note:** The parameters required to be configured are described as follows.
> Table 1. Parameter description

| Name | Description |
|---|---|
| Project | The name of the MaxCompute project to which data in the topic is archived. |
| Table | The name of the MaxCompute table to which data in the topic is archived. |
| AccessKey ID and AccessKey Secret | The AccessKey for accessing MaxCompute. The AccessKey must belong to a RAM user that has CreateInstance, Desc, and Alter permissions on the MaxCompute table. |
| Partition Mode | The following modes are available: system time, event time, and _ _ user define. If you select system time, partitions are created based _ _ on the recording time. If you select event time, partitions are created _ based on the specified event time value. When you create the topic, _ you must define a topic field as event time and set its data type to _ TIMESTAMP. The field values must be accurate to microseconds. If you select user define, partitions are created based on the user-defined _ partition field. |
| Partitioning Interval | If you set Partition Mode to system time or event time, you must set _ _ a partitioning interval. The minimum value is 15 minutes. |
| Partition Key | Only the default format is supported. Customized format will be supported at a later date. If the partitioning interval is set to 15 minutes, the partition key format is ds=20170704,hh=01,mm=15. Note that a corresponding partition field must be contained in the MaxCompute table. |

#### 3.2.2 View archive details

This section describes how to view archive details after a DataConnector has been created. The Details page of DataConnector displays the basic information including the name of the topic involved, the destination MaxCompute project and table names, and the archive progress. The archive progress is indicated by Latest Record Time, Last Synced Record Time, and Latency.

> **Note:** Latest Record Time indicates the timestamp at which the latest record was ingested to DataHub. Last Synced Record Time indicates the timestamp at which the latest record that has been synchronized to the destination platform was ingested to DataHub. Latency, in seconds, indicates the gap between the latest record time and the last synced record time.

You can also check the archive progress of each shard. If a shard is in **ERROR** status, place your mouse pointer over the question mark next to ERROR to show the cause of the issue. After the issue is fixed, you can click Resume in the Actions column of the shard to resume the DataConnector. For example, if the task is terminated because the corresponding MaxCompute partition is deleted, you can re-create the MaxCompute partition by using SDK or in the MaxCompute console. Then click **Resume** in the Actions column of the shard to resume archiving. If multiple shards are not in **RUNNING** status, you can click **Resume**
**Archiving** to resume archiving for all these shards.
ng

## 4 Performance monitoring

This topic describes how to monitor the performance of DataHub. In the DataHub console, you can view near real-time performance statistics of topics, such as queries per second (QPS) and throughput. The available metrics are listed as follows: Read and write QPS Read and write records per second (RPS) Read and write throughput, measured in KB per second Read and write latency, measured in microseconds per request On the **Projects** page, click **View** in the Actions column of a project. On the project details page that appears, click View in the Actions column of a topic. Then, on the topic details page, click **Metric** to view the performance statistics of the topic. You can obtain the performance statistics for a specified time range.
