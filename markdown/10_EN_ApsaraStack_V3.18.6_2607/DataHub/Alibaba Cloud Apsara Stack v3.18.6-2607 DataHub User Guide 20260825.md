---
title: "Alibaba Cloud Apsara Stack v3.18.6-2607 DataHub User Guide 20260825"
product_version: "V3.18.6_2607"
doc_version: "20260825"
pdf_pages: 167
source_pdf: "Alibaba Cloud Apsara Stack v3.18.6-2607 DataHub User Guide 20260825.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/3816%202607/pdf%203/DataHub/Alibaba%20Cloud%20Apsara%20Stack%20v3.18.6-2607%20DataHub%20User%20Guide%2020260825.pdf"
converter: pdf2md (PyMuPDF line classifier)
---

# Alibaba Cloud Apsara Stack v3.18.6-2607 DataHub User Guide 20260825

## What is DataHub?

DataHub provides real-time streaming data collection, reliable storage, and efficient processing capabilities. It enables you to analyze data at a low latency and consume data in real time. DataHub is a distributed streaming data processing platform. It provides efficient data publishing, subscription, and distribution capabilities to help you analyze and consume data in real time. End-to-end streaming data processing: It can consistently collect volumetric data from mobile platforms, applications and services, website logs, and IoT sensors, persist data, and process data in real time. You can use custom programs or streaming compute engines to process real-time logs or transaction events and then quickly generate real-time statistics, visualized charts, and intelligent alerts. Enterprise-class architecture and base: DataHub is designed on top of Apsara Infrastructure Management. It features high availability, low latency, high scalability, and high throughput, which is suitable for handling large numbers of concurrent writes and real-time reads. Seamless ecosystem integration: DataHub is deeply integrated with Realtime Compute of Apsara Stack to simplify streaming data analysis by supporting standard SQL statements. In addition, its flexible data distribution capabilities can help you deliver processed streaming data to other cloud services in real time, such as MaxCompute and Object Storage Service (OSS). This way, you can process real-time and offline data in a unified architecture. DataHub provides the following features: Data queue (ordered and elastic): The architecture of DataHub is designed based on topics and shards. A data queue strictly maintains the order in which data is written and consumed within a shard. A data queue can be horizontally scaled for a specific shard to linearly improve the throughput of a single topic. Offset/checkpoint storage (offset/checkpoint hosting): DataHub can persist consumption offsets or checkpoints to its server for applications. When an application encounters a failover or restart, it can automatically resume consumption from the saved offset or checkpoint. This ensures the continuity and consistency of data consumption. Data synchronization (cross-service distribution): DataHub can automatically deliver streaming data to Apsara Stack services in real time, including MaxCompute, Hologres, AnalyticDB for MySQL, ApsaraDB RDS, Tablestore, and OSS. Elastic scaling (online adjustment): DataHub supports topic-specific dynamic scale-out and scale-in. It adopts the SplitShard and MergeShard mechanisms to flexibly adjust the throughput without business interruptions.

## Terms

This topic describes the terms that are used in DataHub.

| Term | Description |
|---|---|
| Project | Projects are the organizational unit used in DataHub. A project contains one or more topics. Projects in DataHub are independent of MaxCompute projects. |
| Topic | Topics are the smallest unit for data subscription and publication in DataHub. You can use topics to distinguish different types of streaming data. |
| Topic Lifecycle | The retention period of a record in a topic. Unit: days. Valid values: 1 to 7. |
| Shard | Shards ensure the concurrent data transmission of a topic. Each shard has a unique ID. Active shards occupy server resources. We recommend that you create shards based on your business requirements. |
| Shard Hash Key Range | A shard property, which indicates the hash key range. The hash key range is left-closed and right-open. Data points with the same key are written to the same shard. |
| Shard Merge | The operation that merges two adjacent shards. Two shards are considered adjacent if the hash key ranges of the shards form a contiguous set without gaps. |
| Shard Split | The operation that splits one shard into two adjacent shards. |
| Record | The unit of data that is written into DataHub. |
| RecordType | The data type of records in topics. The data type can be TUPLE or BLOB. Tuple topics contain records that are similar to data records in databases. Each record contains multiple columns. You can write a block of binary data as a record to blob topics. |

## Limits

This topic describes the limits of DataHub. The following table describes the limits of DataHub.

| Item | Limit | Description |
|---|---|---|
| Active shards | (0,256] | Each topic can contain up to 256 active shards. |
| Total number of shards | (0,512] | You can create up to 512 shards in each topic. |
| Http BodySize | Up to 4 MB | The size of an HTTP request body cannot exceed 4 MB. |
| String size | Up to 1 MB | The size of a string cannot exceed 1 MB. |
| Waiting time for ShardMerge or ShardSplit | 5s | You cannot perform the ShardMerge or ShardSplit operation on a shard within 5 seconds after the shard is created. |
| QPS | Up to 5,000 | The write QPS limit of a shard is 5,000. Multiple write queries in one batch are considered one query. |
| Throughput | Up to 5 MB/s | The write throughput limit of a shard is 5 MB/s. |
| Projects per account | Up to 50 | You can create up to 50 projects within an Apsara Stack tenant account. |
| Topics per project | Up to 500 | You can create up to 500 topics in a project. To create more topics, contact Apsara Stack technical support. |
| Time-to-live (TTL) of records | [1,7] | The TTL of a record in a topic ranges from one to seven days. |

## Quick Start

### Overview

This topic describes how to work with DataHub to complete basic operations.

**Flowchart**

**Procedure**

1. Create a project.
Projects are the basic organizational unit in DataHub. Each project contains one or more topics. To use DataHub, you must create a project first.
2. Create a topic.
Topics are the smallest unit for data subscription and publishing in DataHub. You can use topics to distinguish different types of streaming data.
3. Collect data samples.
DataHub provides the data sampling feature. You can use this feature to collect data samples from a specific shard to assess data quality.
4. Synchronize data.
DataHub provides the data synchronization feature. You can synchronize real-time data from DataHub to other data warehouses by using DataConnectors. This helps you analyze and process historical data with ease.
5. Subscribe to topics.
DataHub provides the subscription feature, which can persist consumption offsets to the DataHub server and reset offsets. This mechanism efficiently ensures the continuity of data transmission after an application recovers from a fault. It strictly guarantees that all messages are delivered at least once.

### Before you begin

#### Log in to the DataHub console

This topic describes how to log in to the DataHub console. In this example, Google Chrome is used.

**Prerequisites**

Before you log in to the DataHub console, make sure that the following requirements are met: You have obtained the URL of the Apsara Uni-manager Management Console. A web browser is available. We recommend that you use Google Chrome.

**Procedure**

1. In the address bar of the browser, enter the URL of the Apsara Uni-manager Management
Console and press the Enter key.
2. On the login page, enter your username and password.
You need to obtain the username and password from an operations administrator.

**Note**

The first time you log in to the Apsara Uni-manager Management Console, you must change the password of your account as prompted. To ensure the security of your account, you must specify a password that is 8 to 20 characters in length and contains at least two of the following character types: Letters Digits Special characters, such as exclamation marks (!), at signs (@), number signs (#), dollar signs ($), and percent signs (%)
3. Click **Log In** to go to the Apsara Uni-manager Management Console.
4. In the top navigation bar, choose **Products > Big Data Computing > DataHub** to go to
the DataHub console.

**Note**

You can click icons in the upper-right corner of the page to use the following features: : switches between English, simplified Chinese, and traditional Chinese. or : switches between light mode and dark mode. : displays message notifications. You can click **More** to go to **Message**
**Center** to view all messages.

#### View information on the Overview page

The Overview page of the DataHub console displays resource overview, storage overview, common information, and synchronization tasks. It supports real-time monitoring, storage management, quick operations, and multi-database synchronization. This topic describes the Overview page.

**Overview page**

After you log in to the DataHub console, the **Overview** page appears by default. The following table describes the sections displayed on the Overview page.

| Section | Description |
|---|---|
| Resource Overview | This section displays the following information: Read Traffic (Today), Write Traffic (Today), Storage Usage (Total), Number of Projects, and Data update time. The unit varies with the data size, for example, Byte, KB, MB, and GB. |
| Storage Overview | This section displays the storage usage of each project in the current organization in a pie chart. The projects are sorted in descending order based on storage usage in the legend. You can perform the following operations to view information: Move the pointer over sectors in different colors on the pie chart to view the storage usage of each project. Click Details in the upper-right corner of the Storage Overview section. On the Projects page, view the details of each project. |
| Common Information | In this section, you can perform the following operations: You can create a project by using Quick Access. You can click Beginner's Guide to view the documentation. You can view Primary Account ID, Classic Network (Private), and VPC (Private). |
| Synchronization Task | DataHub allows you to synchronize data to the following services: MaxCompute: DataHub allows you to synchronize data to MaxCompute and create custom partitions. Hologres: DataHub allows you to use HoloHub to synchronize data to Hologres. Elasticsearch: You can synchronize data from DataHub to Elasticsearch. RDS & MySQL: You can synchronize data from DataHub to ApsaraDB RDS in IGNORE or OVERWRITE mode. Tablestore: DataHub allows you to synchronize data to Tablestore in PUT or UPDATE mode. Object Storage Service (OSS): DataHub allows you to archive data to OSS based on the time when data is written to DataHub. Click the icon next to the name of a cloud service to log in to the console of the cloud service. |

#### Create a project

Projects are the basic organizational unit in DataHub. Each project contains one or more topics. To use DataHub, you must create a project first. This topic describes how to create a project and bind a virtual private cloud (VPC) to the project in the DataHub console.

**Prerequisites**

An Apsara Stack tenant account authorized to create projects is created.

**Usage notes**

DataHub projects are independent of MaxCompute projects. You cannot use MaxCompute projects as DataHub projects. Therefore, you must create projects in DataHub when you use DataHub. You can create up to 50 projects with an Apsara Stack tenant account.

**Procedure**

1. Log in to the DataHub console.
2. In the left-side navigation pane, click **Projects**. On the Projects page, click **Create Project**
in the upper-right corner.
3. On the **Create Project** page, configure the following parameters.

| Section | Parameter | Description |
|---|---|---|
| Billing configuration | Billing method | The billing method determines how fees are charged for the cloud services that you use. Currently, only Pay-as-you-go is supported. Note This parameter is displayed only after the service management feature is configured. For more information about service management, see Operations > Service operations > Service catalogs > Service management in Apsara Uni-manager Management Console User Guide. |
| Area | Organization/Res ource Set | Select an organization and a resource set. |
|   | Region | Select a region. |
| Basic Settings | Name | Enter a name that meets the following requirements: The name must be 3 to 32 characters in length, and can contain letters, digits, and underscores ( ). It _ must start with a letter. |
|   | Description | Enter a description for the project. |

4. Optional. View the configuration.
In the right-side **Configuration overview** section, you can perform the following operations: View parameters The **Configuration overview** section verifies the required parameters in real time. If a required parameter is skipped, a red status bar is displayed. Quick navigation You can click the bar next to a parameter to navigate to the parameter.
5. Confirm and submit the configuration.
Confirm the parameters and click **Confirm Order** if the following requirements are met: On the Service Management page, a service is created and **DataHub** is displayed in the Cloud resources column of the service. If no service whose Cloud resources value is **DataHub** exists on the Service Management page, confirm the parameters and click **Submit**. For more information about service management, see the topics below **Service**
**management** in **Apsara Uni-manager Management Console User Guide** .
6. Optional. Click **View** in the Actions column of the project to view the details of the project.
To delete the project, click **Delete** in the Actions column.

**Bind a VPC to a DataHub project**

DataHub adopts the VPC binding mechanism to isolate and limit access at the network layer. This ensures that only cloud resources in the specified VPC can communicate with DataHub. Perform the following steps to bind and unbind a VPC:
1. On the **Bound VPC List** tab of the project details page, click **Bind VPC**.
2. In the dialog box that appears, enter the name of the desired VPC and click **Bind VPC**.
3. Optional. To unbind the VPC, click **Delete** in the Actions column of the VPC.

#### Create a topic

Topics are the smallest unit for data subscription and publishing in DataHub. You can use topics to distinguish different types of streaming data. This topic describes how to create a topic in the DataHub console.

**Prerequisites**

A project is created.

**Usage notes**

You can create up to 500 topics in each project. If you want to create more topics in a project, contact the administrator.

**Procedure**

1. Log in to the DataHub console.
2. In the left-side navigation pane, click **Projects**. On the **Projects** page, find the project in
which you want to create a topic and click **View** in the **Actions** column. The project details page appears.
3. On the project details page, click **Create Topic** in the upper-right corner.
You can select **Create Directly** or **Import MaxCompute Tables** to create the topic.
**Method 1**: **Create Directly**

| Parameter | Description |
|---|---|
| Creation Type | Select Create Directly. |
| Name | The name of the topic. The name must meet the following requirements: The name can contain only lowercase letters, digits, and underscores ( ). _ The name must start with a lowercase letter. The name must be 3 to 64 characters in length. |
| Type | The type of data in the topic. Valid values: TUPLE: structured data. BLOB: unstructured data. |

| Schema Details | The schema. If the Type parameter is set to TUPLE, the system generates a schema whose version number is 0 by default. If you want to modify or add versions, you can go to the topic details page to modify the settings after you create the topic. If the Type parameter is set to BLOB, this parameter is unavailable. |
|---|---|
| Number of Shards | Valid values: 1 to 256. |
| Lifecycle | Valid values: 1 to 7. |
| Shard Extension Mode | Specifies whether to enable shard scale-out. If you turn on this switch, shards can be horizontally scaled and cannot be merged or split. In this case, the number of shards cannot be decreased but can be increased. After you turn on this switch, you can use Kafka to consume data in the topic. |
| Enable Multi-version | This parameter is available only when the Type parameter is set to TUPLE. Specifies whether to enable multi-version schemas. If you turn on this switch, the topic can have multiple versions of schemas at the same time. You can write data by using one of the schemas. The consumers adaptively parse the data based on the schema version. If the schema version is deleted, the data fails to be parsed. Take note of the following items: You can no longer call the appendFields operation. You can create, delete, modify, and query schemas. When you create a DataConnector, the schema of the latest version is used. |
| Description | The description of the topic. The description can be 3 to 1,024 characters in length. |

**Method 2**: **Import MaxCompute Tables**

**Note**

Before you perform the following steps, make sure that you have created a MaxCompute project and a destination table, and you have obtained the corresponding AccessKey ID and AccessKey secret.

| Parameter | Description |
|---|---|
| Creation Type | Select Import MaxCompute Tables. |
| Project Name | The name of the MaxCompute project. |
| Table Name | The name of the MaxCompute table. |
| AccessKey ID | The AccessKey ID used to access MaxCompute. |
| AccessKey Secret | The AccessKey secret used to access MaxCompute. |

Click **Next**. In the **Create Topic** dialog box, configure the following parameters.

| Parameter | Description |
|---|---|
| Name | By default, the MaxCompute table name specified in the previous step is displayed. |
| Type | Valid values: TUPLE: structured data. BLOB: unstructured data. The system automatically obtains the data type, which cannot be modified. |
| Schema Details | The schema. If the Type parameter is set to TUPLE, the system generates a schema whose version number is 0 by default. If you want to modify or add versions, you can go to the topic details page to modify the settings after you create the topic. If the Type parameter is set to BLOB, this parameter is unavailable. The system automatically obtains the schema details, which cannot be modified. |

| Number of Shards | Valid values: 1 to 256. |
|---|---|
| Lifecycle | Valid values: 1 to 7. |
| Shard Extension Mode | Specifies whether to enable shard scale-out. If you turn on this switch, shards can be horizontally scaled and cannot be merged or split. In this case, the number of shards cannot be decreased but can be increased. After you turn on this switch, you can use Kafka to consume data in the topic. |
| Enable Multi-version | This parameter is available only when the Type parameter is set to TUPLE. Specifies whether to enable multi-version schemas. If you turn on this switch, the topic can have multiple versions of schemas at the same time. You can write data by using one of the schemas. The consumers adaptively parse the data based on the schema version. If the schema version is deleted, the data fails to be parsed. In addition, take note of the following items: You can no longer call the appendFields operation. You can create, delete, modify, and query schemas. When you create a DataConnector, the schema of the latest version is used. |
| Description | The description of the topic. The description can be 3 to 1,024 characters in length. |

4. Click **Create**.
Refresh the **Topic List** tab to view the created topic. You can also perform the following operations on existing topics:
**View**: Click **View** in the Actions column of a topic to view its details.
**Delete**: Click **Delete** in the Actions column of a topic to delete the topic.

**Important**

Before you delete a topic, you must check whether the topic is added to a group. If the topic is added to a group, you must remove it from the group before you can delete the topic.

#### Create a group

A group is a collection of topics. If you subscribe to a group, you subscribe to all topics in the group. Groups are compatible with the Kafka protocol. This topic describes how to create a group in the DataHub console.

**Background information**

To ensure compatibility with Kafka, DataHub provides the group feature, which allows you to subscribe to multiple topics at a time. You can create a group in a project and add the topics to which you want to subscribe to the group. This way, you can use the group to subscribe to multiple topics in the project. If a topic is added to a group, you can view the subscription that is automatically created by the group on the Subscription List tab of the topic details page. If you delete the subscription, you cannot use the group to subscribe to the topic and existing consumption offsets disappear.

**Usage notes**

A group can contain up to 50 topics.

**Procedure**

1. Log on to the DataHub console.
2. In the left-side navigation pane, click **Projects**. On the **Projects** page, find the project in
which you want to create a topic and click **View** in the **Actions** column. The project details page appears.
3. On the project details page, click **Create Group** in the upper-right corner.
4. In the **Create Group** panel, configure the parameters and click **Create**. The following table
describes the parameters.

| Parameter | Description |
|---|---|

| Name | The name of the group. The name must meet the following requirements: The name can contain only lowercase letters, digits, and underscores ( ). _ The name must start with a lowercase letter. The name must be 3 to 32 characters in length. |
|---|---|
| Description | The description of the group. The description must be 3 to 1,024 characters in length. |
| Topic | The topics to be added to the group. |

5. View the information about the group on the **Groups** tab of the project details page.
You can perform the following operations on the group: Click **Edit** in the Actions column. In the panel that appears, you can add topics to or remove topics from the group. Click **Delete** in the Actions column. In the message that appears, confirm the information and click **Delete** to delete the group.

### Use the data sampling feature

DataHub provides the data sampling feature. You can use this feature to collect data samples from a specific shard to assess data quality. This topic describes how to work with the data sampling feature in the DataHub console.

**Background information**

When you collect data samples, you must specify the start time of data sampling and the maximum number of records that you want to collect.

**Prerequisites**

A project and a topic are created and data is written to the topic.

**Procedure**

1. Log in to the DataHub console.
2. In the left-side navigation pane, click **Projects**. On the **Projects** page, find the project that
you want to manage and click **View** in the **Actions** column.
3. On the **Topic List** tab, find the topic that you want to manage and click **View** in the
**Actions** column.
4. On the **Shard List** tab, find the shard from which you want to collect samples and click
**Sample** in the **Actions** column.
5. In the **Sampling Shard ID** panel, specify **Sampling Quantity** and **Start Time** and then
click **Sample**. DataHub collects records that are written to the shard after the specified start time and displays the sampled records in the table. The number of sampled records does not exceed the specified sample quantity. control

## DataHub permission

**control**

### Overview

DataHub integrates Resource Access Management (RAM) to allow you to manage the permissions of Apsara Stack tenant accounts and RAM users in a fine-grained manner. Based on the least privilege principle, the security of data transmission can be greatly improved. DataHub uses RAM to manage resource access permissions. Only RAM users that are granted the required permissions can access resources in DataHub. An Apsara Stack tenant account has full permissions on the resources within the account. By default, a RAM user has no permissions on resources. You must grant permissions to the RAM user. The following topics describe how DataHub manages resource access permissions based on RAM.

**Note**

An Apsara Stack tenant account corresponds to a level-1 organization and requires no authorization. A RAM user corresponds to a specific user and must be granted permissions by an Apsara Stack tenant account.

### DataHub resources

Resource Access Management (RAM) allows you to control access to the projects, topics, and subscriptions in DataHub. A subscription is an action that allows an application to read and process the records in topics of a specific project. Access control is supported at the project, topic, and subscription level. Shard-level authentication is not supported. In RAM, each type of DataHub resource uses an Alibaba Cloud Resource Name (ARN) format to describe all resources or a specific resource of the type. For example, the ARN format of a project in a specific region is

| acs:dhs:$region:$accountid:projects/$projectName |   |   |   |
|---|---|---|---|
| $projectName | , and | $subId | parameters specify th |

subscription ID. Table 1. ARN formats for different resource types

| Resource type | ARN format |
|---|---|
| SingleProject | acs:dhs:$region:$accountid:projects/$projectName |
| AllProject | acs:dhs:$region:$accountid:projects/* |
| SingleTopic | acs:dhs:$region:$accountid:projects/$projectName/topics/$topicName |
| AllTopic | acs:dhs:$region:$accountid:projects/$projectName/topics/* |

control

| SingleSubscription | acs:dhs:$region:$accountid:projects/$projectName/topics/$topicName/subscr iptions/$subId |
|---|---|
| AllSubscription | acs:dhs:$region:$accountid:projects/$projectName/topics/$topicName/subscr iptions/* |

### DataHub API

DataHub provides different API operations to allow you to manage projects, topics, shards, subscriptions, and records. A Resource Access Management (RAM) user must be granted the required permissions before the RAM user can call a DataHub API operation. Each DataHub API operation corresponds to a specific RAM action and a specific resource type. The following tables describe the RAM action and resource type for each API operation.

**Project API**

Table 1. API operations for projects

| Operation | RAM action | Resource type |
|---|---|---|
| CreateProject | dhs:CreateProject | AllProject |
| ListProject | dhs:ListProject | AllProject |
| DeleteProject | dhs:DeleteProject | SingleProject |
| GetProject | dhs:GetProject | SingleProject |
| UpdateProject | dhs: UpdateProject | SingleProject |

**Topic API**

Table 2. API operations for topics

| Operation | RAM action | Resource type |
|---|---|---|
| CreateTopic | dhs:CreateTopic | AllTopic |
| ListTopic | dhs:ListTopic | AllTopic |
| DeleteTopic | dhs:DeleteTopic | SingleTopic |
| GetTopic | dhs:GetTopic | SingleTopic |

control

| UpdateTopic | dhs: UpdateTopic | SingleTopic |
|---|---|---|

**Subscription API**

Table 3. API operations for subscriptions

| Operation | RAM action | Resource type |
|---|---|---|
| CreateSubscription | dhs:CreateSubscription | AllSubscription |
| ListSubscription | dhs:ListSubscription | AllSubscription |
| DeleteSubscription | dhs:DeleteSubscription | SingleSubscription |
| GetSubscription | dhs:GetSubscription | SingleSubscription |
| UpdateSubscription | dhs: UpdateSubscription | SingleSubscription |
| CommitOffset | dhs:CommitOffset | SingleSubscription |
| GetOffset | dhs:GetOffset | SingleSubscription |

**Shard API**

Table 4. API operations for shards

| Operation | RAM action | Resource type |
|---|---|---|
| ListShard | dhs:ListShard | SingleTopic |
| MergeShard | dhs:MergeShard | SingleTopic |
| SplitShard | dhs:SplitShard | SingleTopic |

**Record API**

Table 5. API operations for records

| Operation | RAM action | Resource type |
|---|---|---|
| PutRecords | dhs:PutRecords | SingleTopic |

control

| GetRecords | dhs:GetRecords | SingleTopic |
|---|---|---|
| GetCursor | dhs:GetRecords | SingleTopic |

### Conditions supported by

**DataHub**

This topic describes the conditions that can be applied to the Resource Access Management (RAM) policies for DataHub. The following table describes the conditions that can be applied to the RAM policies for DataHub. Table 1. Conditions that can be applied to the RAM policies for DataHub

| Condition | Description | Valid value |
|---|---|---|
| acs:SourceIp | The IP addresses that can access the specified object. | Any valid IP address. The wildcard character (*) is supported. |
| acs:SecureTransport | Specifies whether HTTPS is used to access the specified object. | true and false |
| acs:MFAPresent | Specifies whether multi- factor authentication (MFA) is enabled for logon. | true/false |
| acs:CurrentTime | The time when the specified object can be accessed. | The time is specified in the ISO 8601 standard. |

### Sample RAM policies for

**DataHub**

#### AliyunDataHubFullAccess

This topic provides an example of the AliyunDataHubFullAccess policy. The following is an example: `{`

```json
  "Version": "1",
  "Statement": [
```

`{`

```json
      "Action": "dhs:*",
      "Resource": "*",
      "Effect": "Allow"
```

`}` `]` `}` control

#### AliyunDataHubReadOnlyAccess

This section describes how to set the AliyunDataHubReadOnlyAccess policy content. The authorization policy content can be set as follows: `{`

```json
  "Version": "1",
  "Statement": [
```

`{`

```json
      "Action": ["dhs:List*", "dhs:Get*"],
      "Resource": "*",
      "Effect": "Allow"
```

`}` `]` `}`

## Data collection

### Overview

In addition to SDK, DataHub supports various data collection tools to help you quickly collect data to DataHub. The topics in this directory describe how to collect data by using Fluentd, Logstash, and Oracle GoldenGate (OGG).

### Fluentd

The DataHub plug-in for Fluentd is an output plug-in developed based on Fluentd to write collected data to DataHub. The plug-in complies with the development conventions of Fluentd output plug-ins and is easy to install. You can use the plug-in to write the collected data to DataHub with ease. This topic describes how to install and use the DataHub plug-in for Fluentd.

**Install the DataHub plug-in for Fluentd**

Install the plug-in by using RubyGems

```
gem install fluent-plugin-DataHub
```

**Important**

We recommend that you change the gem source to https://gems.ruby-china.com. Install the plug-in by using an installation package The plug-in must be installed in Linux. Before you install the plug-in, install Ruby. For users who have not installed Fluentd, a full installation package for installing both Fluentd and the DataHub plug-in for Fluentd is provided. For users who have installed Fluentd, an installation package for the DataHub plug-in for Fluentd is provided. Complete installation: If you have not installed Fluentd, download the full installation package fluentd-with-datahub-0.12.25.tar.gz for installing both Fluentd and the DataHub plug-in for Fluentd. Run the following command to install the plug-in.

**Important**

Fluentd 0.12.25 is provided in the full installation package.

```bash
$ tar -xzvf fluentd-with-datahub-0.12.25.tar.gz $ cd fluentd-with-datahub $ sudo sh install.sh
```

Separate installation: If you have installed Fluentd, download the installation package for the DataHub plug-in for Fluentd fluent-plugin-datahub-0.12.25.gem and run the gem command to install the plug-in.

```bash
$ sudo gem install --local fluent-plugin-datahub-0.12.25.gem
```

**Use cases**

Case 1: Upload a CSV file This section describes how to write the incremental content of a CSV file to DataHub in near real time by using the DataHub plug-in for Fluentd. The following example shows the format of the CSV file:

```
0,qe614c760fuk8judu01tn5x055rpt1,true,100.1,14321111111 1,znv1py74o8ynn87k66o32ao4x875wi,true,100.1,14321111111 2,7nm0mtpgo1q0ubuljjjx9b000ybltl,true,100.1,14321111111 3,10t0n6pvonnan16279w848ukko5f6l,true,100.1,14321111111 4,0ub584kw88s6dczd0mta7itmta10jo,true,100.1,14321111111 5,1ltfpf0jt7fhvf0oy4lo8m3z62c940,true,100.1,14321111111 6,zpqsfxqy9379lmcehd7q8kftntrozb,true,100.1,14321111111 7,ce1ga9aln346xcj761c3iytshyzuxg,true,100.1,14321111111 8,k5j2id9a0ko90cykl40s6ojq6gruyi,true,100.1,14321111111 9,ns2zcx9bdip5y0aqd1tdicf7bkdmsm,true,100.1,14321111111 10,54rs9cm1xau2fk66pzyz62tf9tsse4,true,100.1,14321111111
```

Each line is a record to be written to DataHub. Fields are separated by commas ( `,` ). The CSV file is saved as `/temp/test.csv` on the on-premises machine. The following table describes the schema of the DataHub topic to which the CSV file is written. Table 1. Schema of the DataHub topic

| Field | Data type |
|---|---|
| id | BIGINT |
| name | STRING |
| gender | BOOLEAN |
| salary | DOUBLE |
| my time _ | TIMESTAMP |

After you modify the Fluentd configuration file based on the CSV file and topic schema, run the following command to start Fluentd to upload the CSV file to DataHub:

```
${FLUENTD_HOME}/fluentd-with-DataHub/bin/fluentd -c fluentd_test.conf
```

In this example, the following Fluentd configuration file is used:

```xml
<source>
  @type tail
  path /xxx/yyy (the path of the CSV file)
  tag test1
  format csv
  keys id,name,gender,salary,my_time
</source> <match test1>
  @type DataHub
  access_id your_app_id
  access_key your_app_key
  endpoint http://ip:port
  project_name test_project
  topic_name fluentd_performance_test_1
  column_names ["id", "name", "gender", "salary", "my_time"]
  flush_interval 1s
  buffer_chunk_limit 3m
  buffer_queue_limit 128
  dirty_data_continue true
  dirty_data_file /xxx/yyy (the path of the stale data file)
  retry_times 3
  put_data_batch_size 1000
</match>
```

Case 2: Collect Log4j logs The following sample code shows a Log4j log:

```
11:48:43.439 [qtp1847995714-17] INFO AuditInterceptor - [c2un5sh7cu52ek6am1ui1m5h] end /web/v1/project/tefe4mfurtix9kwwyrvfqd0m/node/0m0169kapshvgc3ujskwkk8g/health GET, 4061
```

`ms` In this example, the following Fluentd configuration file is used:

```xml
<source>
  @type tail
  path bayes.log
  tag test
  format /(?<request_time>\d\d:\d\d:\d\d.\d+)\s+\[(?<thread_id>[\w\-]+)\]\s+(?<log_leve
l>\w+)\s+(?<class>\w+)\s+-\s+\[(?<request_id>\w+)\]\s+(?<detail>.+)/ </source> <match test>
  @type DataHub
  access_id your_access_id
  access_key your_access_key
  endpoint http://ip:port
  project_name test_project
  topic_name DataHub_fluentd_out_1
  column_names ["thread_id", "log_level", "class"]
</match>
```

**Plug-in configurations**

Table 2. Read configuration

| Parameter | Description |
|---|---|
| tag test1 | The tag, which is mapped to the destination information by using the specified regular expression. |
| format csv | The format of the file from which data is collected. |
| keys id,name,gender,salary,my time _ | The columns to be collected from the CSV file. The column names must be the same as those in the schema of the destination DataHub topic. |

Table 3. Write configuration

| Parameter | Description |
|---|---|
| shard id 0 _ | The ID of the shard to which all records are written. By default, all records are written to the shard in a round-robin manner. The default ID is 0. |
| shard keys ["id"] _ | The column used as the shard key. Hashed shard keys are used as indexes for writing data. |
| flush interval 1 _ | The interval between consecutive data flushes. Fluentd writes data at least once every second. The default value is 60. Unit: seconds. |
| buffer chunk limit 3m _ _ | The maximum size of a chunk. Unit: k or m, which indicates KB or MB. We recommend you set the maximum size to 3 MB. |
| buffer queue limit 128 _ _ | The maximum length of the chunk queue. Both the buffer chunk limit and buffer queue limit parameters _ _ _ _ determine the size of the buffer. The default value is 128 MB. |
| put data batch size 1000 _ _ _ | The number of records to be written to DataHub each time. In this example, 1,000 records are written to DataHub each time. |
| retry times 3 _ | The number of retries allowed. Default value: 3. |
| retry interval 3 _ | The retry interval. Unit: seconds. Default value: 3. |

| dirty data continue true _ _ | Specifies whether to ignore stale data. A value of true indicates that the plug-in retries the operation for a specific number of times before it writes stale data records to the stale data file. |
|---|---|
| dirty data file /xxx/yyy _ _ | The directory in which the stale data file is stored. |
| column names ["id"] _ | The name of the columns to be written to DataHub. |

### Logstash plugin

This guide explains how to use the Logstash plugin to collect and upload log data to DataHub. With the DataHub Output and Input plugins for Logstash, you can process various data sources, structure the data, and transmit it. It covers installation, configuration, and usage, including data synchronization, error handling, and parameter configuration.

**Logstash collection tool**

To expand data collection in DataHub, Alibaba Cloud Real-time Compute provides DataHub Output and Input plugins for Logstash. These plugins allow you to connect to over 30 data sources supported by the open-source community, including files, syslog, Redis, Log4j, and Apache or Nginx logs. Logstash also supports features like the filter plugin for custom data processing. This guide uses log collection as an example to show you how to quickly collect and send log data to DataHub.

**Note**

The DataHub Output and Input plugins for Logstash are open source under the Apache License 2.0.

**Installation**

**Requirements**

Logstash requires Java Runtime Environment (JRE) 7 or later. Some features may not work with earlier versions.

**Installation methods**

Alibaba Cloud provides two ways to install the Logstash plugin:

**One-click installation**

Use a one-click installation package to install Logstash and the DataHub plugin together. Compatible with Logstash 6 and 7

```
tar -xzvf logstash-with-datahub-6.4.0-1.0.10.tar.gz cd logstash-with-datahub-6.4.0
```

Compatible with Logstash 8

```
tar -xzvf logstash-with-datahub-8.10.3-1.0.12.tar.gz cd logstash-with-datahub-8.10.3
```

**Manual installation**

Install Logstash by following the official Logstash installation guide. Note that the latest version of Logstash requires Java 7 or later. Install the DataHub plugin by downloading the required plugin files. To upload data to DataHub, use the DataHub Logstash Output plugin: logstash-output-datahub-1.0.10.gem (compatible with Logstash 6 and 7) logstash-output-datahub-1.0.12.gem (compatible with Logstash 8) To download data from DataHub, use the DataHub Logstash Input plugin: logstash-input-datahub-1.0.10.gem (compatible with Logstash 6 and 7) logstash-input-datahub-1.0.12.gem (compatible with Logstash 8) Run the following commands to install the plugins:

```bash
$ {LOG_STASH_HOME}/bin/logstash-plugin install --local logstash-output-datahub-1.0.10 .gem $ {LOG_STASH_HOME}/bin/logstash-plugin install --local logstash-input-datahub-1.0.10. gem
```

If you encounter an error similar to the following during installation:

```
WARNING: can not set Session#timeout=(0) no session context
```

First, verify that your machine can access the internet. If the network connection is working, try switching to a Chinese mirror source.

**Offline installation**

If your production machine cannot access the internet, you cannot install the plugin by using the method described previously. You must create an offline installation package because the package is tied to a specific Logstash version. First, install the plugin on a test machine by using the method described previously. Then, refer to the official documentation to create an offline installation package, upload it to your production machine, and perform the offline installation.

**Upload data with the Logstash Output plugin**

**Configure Log4j logs for DataHub**

The following example shows how to use Logstash to collect and structure Log4j log data. Here is a sample Log4j log entry:

```
20:04:30.359 [qtp1453606810-20] INFO AuditInterceptor - [13pn9kdr5tl84stzkmaa8vmg] end /web/v1/project/fhp4clxfbu0w3ym2n7ee6ynh/statistics?executionName=bayes_poc_test GET, 1 87 ms
```

To structure this Log4j data and collect it in DataHub, create a DataHub topic with the following schema:

| Field name | Type |
|---|---|
| request time _ | STRING |
| thread id _ | STRING |

| log level _ | STRING |
|---|---|
| class name _ | STRING |
| request id _ | STRING |
| detail | STRING |

The Logstash task is configured as follows:

```bash
input {
    file {
        # Use forward slashes ("/") on Windows, not backslashes ("\").
        path => "${APP_HOME}/log/bayes.log"
        start_position => "beginning"
```

`}` `}`

```
filter{
    grok {
        match => {
           "message" => "(?<request_time>\d\d:\d\d:\d\d\.\d+)\s+\[(?<thread_id>[\w\-
]+)\]\s+(?<log_level>\w+)\s+(?<class_name>\w+)\s+\-\s+\[(?<request_id>\w+)\]\s+(?<detai l>.+)"
```

`}` `}` `}`

```
output {
    datahub {
        access_id => "Your accessId"
        access_key => "Your accessKey"
        endpoint => "Endpoint"
        project_name => "project"
        topic_name => "topic"
        #shard_id => "0"
        #shard_keys => ["thread_id"]
        dirty_data_continue => true
        dirty_data_file => "/Users/ph0ly/trash/dirty.data"
        dirty_data_file_max_size => 1000
```

`}` `}`

**Configure CSV files for DataHub**

The following example shows how to use Logstash to collect data from a standard CSV file. Here is a sample CSV file:

```
1111,1.23456789012E9,true,14321111111000000,string_dataxxx0, 2222,2.23456789012E9,false,14321111111000000,string_dataxxx1
```

The corresponding DataHub topic schema is:

| Field name | Type |
|---|---|
| col1 | BIGINT |
| col2 | DOUBLE |
| col3 | BOOLEAN |
| col4 | TIMESTAMP |
| col5 | STRING |

The Logstash task is configured as follows:

```
input {
    file {
        path => "${APP_HOME}/data.csv"
        start_position => "beginning"
```

`}` `}`

```
filter{
    csv {
        columns => ['col1', 'col2', 'col3', 'col4', 'col5']
```

`}` `}`

```
output {
    datahub {
        access_id => "Your accessId"
        access_key => "Your accessKey"
        endpoint => "Endpoint"
        project_name => "project"
        topic_name => "topic"
        #shard_id => "0"
        #shard_keys => ["thread_id"]
        dirty_data_continue => true
        dirty_data_file => "/Users/ph0ly/trash/dirty.data"
        dirty_data_file_max_size => 1000
```

`}` `}`

**Configure JSON files for DataHub**

**One-to-one sync (one JSON file to one topic)**

Sample JSON file (located at /home/software/data/22/test_topic_22.json):

```
[{"col1":"aaaaa","col2":222},{"col1":"aaaaa","col2":222},{"col1":"aaaaa","col2":222},{" col1":"aaaaa","col2":222},{"col1":"aaaaa","col2":222},{"col1":"aaaaa","col2":222},{"col 1":"aaaaa","col2":222},{"col1":"aaaaa","col2":222},{"col1":"aaaaa","col2":222},{"col1": "aaaaa","col2":222}] [{"col1":"aaaaa","col2":222},{"col1":"aaaaa","col2":222},{"col1":"aaaaa","col2":222},{" col1":"aaaaa","col2":222},{"col1":"aaaaa","col2":222},{"col1":"aaaaa","col2":222},{"col 1":"aaaaa","col2":222},{"col1":"aaaaa","col2":222},{"col1":"aaaaa","col2":222},{"col1": "aaaaa","col2":222}]
```

Configuration file:

```bash
input {
    file {
        path => "/home/software/data/22/test_topic_22.json"
        start_position => "beginning"
        # Checkpoint file location
                sincedb_path => "/home/software/sincedb/filedatahub"
        codec => json {
            charset => "UTF-8"
```

`}` `}` `}`

```
filter{
    mutate {
      rename => {
        "col1"    =>    "col1"
        "col2"    =>    "col2"
```

`}` `}` `}`

```
output {
   datahub {
      access_id => "xxxx"
      access_key => "xxxx"
      endpoint => "http://dh-cn-shanghai-int-vpc.aliyuncs.com"
      project_name => "test_dh1"
      topic_name => "topic_test_2"
      #shard_id => "0"
      #shard_keys => ["thread_id"]
      dirty_data_continue => true
      dirty_data_file => "/home/software/dirty_vehIdInfo.data"
      dirty_data_file_max_size => 1000
```

`}` `}` Command and result:

```
bash bin/logstash -f config/logstash.conf
```

**Many-to-many sync (multiple JSON files to multiple topics)**

Sample JSON file (located at /home/software/data/22/test_topic_22.json):

```
[{"col1":"aaaaa","col2":222},{"col1":"aaaaa","col2":222},{"col1":"aaaaa","col2":222},{" col1":"aaaaa","col2":222},{"col1":"aaaaa","col2":222},{"col1":"aaaaa","col2":222},{"col 1":"aaaaa","col2":222},{"col1":"aaaaa","col2":222},{"col1":"aaaaa","col2":222},{"col1": "aaaaa","col2":222}] [{"col1":"aaaaa","col2":222},{"col1":"aaaaa","col2":222},{"col1":"aaaaa","col2":222},{" col1":"aaaaa","col2":222},{"col1":"aaaaa","col2":222},{"col1":"aaaaa","col2":222},{"col 1":"aaaaa","col2":222},{"col1":"aaaaa","col2":222},{"col1":"aaaaa","col2":222},{"col1": "aaaaa","col2":222}]
```

Sample JSON file (located at /home/software/data/11/test_topic.json):

```json
[{"col1":"aaaaa","col2":"bbbbbb"},{"col1":"aaaaa","col2":"bbbbbb"}, {"col1":"aaaaa","col2":"bbbbbb"},{"col1":"aaaaa","col2":"bbbbbb"}, {"col1":"aaaaa","col2":"bbbbbb"}] [{"col1":"aaaaa","col2":"bbbbbb"},{"col1":"aaaaa","col2":"bbbbbb"}, {"col1":"aaaaa","col2":"bbbbbb"},{"col1":"aaaaa","col2":"bbbbbb"}, {"col1":"aaaaa","col2":"bbbbbb"}] [{"col1":"aaaaa","col2":"bbbbbb"},{"col1":"aaaaa","col2":"bbbbbb"}, {"col1":"aaaaa","col2":"bbbbbb"},{"col1":"aaaaa","col2":"bbbbbb"}, {"col1":"aaaaa","col2":"bbbbbb"}]
```

Configuration file:

```bash
input {
    file {
        path => "/home/software/data/**/*.json"
        start_position => "beginning"
        # Checkpoint file location
                sincedb_path => "/home/software/sincedb/filedatahub"
        codec => json {
            charset => "UTF-8"
```

`}` `}` `}`

```bash
filter{
  # Differentiate based on the path
    if "22"  in [path] {
        mutate {
          rename => {
```

```
            "col1"        =>    "col1"
            "col2"        =>    "col2"
```

`}` `}` `}`

```
    if "11" in [path] {
        mutate {
          rename => {
            "col1"    =>    "col1"
            "col2"    =>    "col2"
```

`}` `}` `}` `}`

```
output {
    if "22"  in [path] {
      datahub {
        access_id => "xxxxx"
        access_key => "xxxxx"
        endpoint => "http://dh-cn-shanghai-int-vpc.aliyuncs.com"
        project_name => "test_dh1"
        topic_name => "topic_test_2"
        #shard_id => "0"
        #shard_keys => ["thread_id"]
        dirty_data_continue => true
        dirty_data_file => "/home/software/dirty_vehIdInfo.data"
        dirty_data_file_max_size => 1000
```

`}` `}`

```
    if "11"  in [path] {
      datahub {
        access_id => "xxxxx"
        access_key => "xxxxx"
        endpoint => "http://dh-cn-shanghai-int-vpc.aliyuncs.com"
        project_name => "test_dh1"
        topic_name => "topic_test"
        #shard_id => "0"
        #shard_keys => ["thread_id"]
        dirty_data_continue => true
        dirty_data_file => "/home/software/dirty.data"
        dirty_data_file_max_size => 1000
```

`}` `}` `}` Command and result:

```
bash bin/logstash -f config/logstash.conf
```

**One-to-many sync (route data from one JSON file to different**

**topics based on a key)**

```json
[{"col1":"aaaaa","col2":222},{"col1":"aaaaa","col2":222},{"col1":"aaaaa","col2":222},{" col1":"aaaaa","col2":222},{"col1":"aaaaa","col2":222},{"col1":"aaaaa","col2":222},{"col 1":"aaaaa","col2":222},{"col1":"aaaaa","col2":222},{"col1":"aaaaa","col2":222},{"col1": "aaaaa","col2":222}] [{"col1":"aaaaa","col2":222},{"col1":"aaaaa","col2":222},{"col1":"aaaaa","col2":222},{" col1":"aaaaa","col2":222},{"col1":"aaaaa","col2":222},{"col1":"aaaaa","col2":222},{"col 1":"aaaaa","col2":222},{"col1":"aaaaa","col2":222},{"col1":"aaaaa","col2":222},{"col1": "aaaaa","col2":222}] [{"col1":"bbbbb","col2":"ccccc"},{"col1":"bbbbb","col2":"ccccc"}, {"col1":"bbbbb","col2":"ccccc"},{"col1":"bbbbb","col2":"ccccc"}, {"col1":"bbbbb","col2":"ccccc"},{"col1":"bbbbb","col2":"ccccc"}, {"col1":"bbbbb","col2":"ccccc"},{"col1":"bbbbb","col2":"ccccc"}, {"col1":"bbbbb","col2":"ccccc"},{"col1":"bbbbb","col2":"ccccc"}] [{"col1":"bbbbb","col2":"ccccc"},{"col1":"bbbbb","col2":"ccccc"}, {"col1":"bbbbb","col2":"ccccc"},{"col1":"bbbbb","col2":"ccccc"}, {"col1":"bbbbb","col2":"ccccc"},{"col1":"bbbbb","col2":"ccccc"}, {"col1":"bbbbb","col2":"ccccc"},{"col1":"bbbbb","col2":"ccccc"}, {"col1":"bbbbb","col2":"ccccc"},{"col1":"bbbbb","col2":"ccccc"}]
```

Configuration file:

```
input {
    file {
        path => "/home/software/data/22/test_topic_22.json"
        start_position => "beginning"
    sincedb_path => "/home/software/sincedb/filedatahub"
        codec => json {
            charset => "UTF-8"
```

`}` `}` `}`

```
filter{
    mutate {
      rename => {
        "col1"    =>    "col1"
        "col2"    =>    "col2"
```

`}` `}` `}`

```bash
output {
     # Route to different topics based on the value of col1
   if[col1] == "aaaaa" {
     datahub {
        access_id => "xxxxx"
        access_key => "xxxxx"
        endpoint => "http://dh-cn-shanghai-int-vpc.aliyuncs.com"
        project_name => "test_dh1"
        topic_name => "topic_test_2"
        #shard_id => "0"
        #shard_keys => ["thread_id"]
        dirty_data_continue => true
        dirty_data_file => "/home/software/dirty_vehIdInfo.data"
        dirty_data_file_max_size => 1000
```

`}` `}`

```
   else {
     datahub {
          access_id => "xxxxx"
          access_key => "xxxxx"
          endpoint => "http://dh-cn-shanghai-int-vpc.aliyuncs.com"
          project_name => "test_dh1"
          topic_name => "topic_test"
          #shard_id => "0"
          #shard_keys => ["thread_id"]
          dirty_data_continue => true
          dirty_data_file => "/home/software/dirty_vehIdInfo.data"
          dirty_data_file_max_size => 1000
```

`}` `}` `}` Command and result:

```
bash bin/logstash -f config/logstash.conf
```

**Sync MySQL data to DataHub**

Configuration file:

```
input {
  jdbc {
    jdbc_driver_library => "mysql-connector-java-5.1.47.jar"
    jdbc_driver_class => "com.mysql.jdbc.Driver"
    jdbc_connection_string => "jdbc:mysql://xxxx:3306/databaese"
    jdbc_user => "username"
    jdbc_password => "password"
    use_column_value => true
    tracking_column => "modifytime"
    schedule => "* * * * *"
    statement => "select * from suyang_test"
```

`}` `}`

```
output {
      datahub {
        access_id => "Your accessId"
        access_key => "Your accessKey"
        endpoint => "Endpoint"
        project_name => "project"
        topic_name => "topic"
        #shard_id => "0"
        #shard_keys => ["thread_id"]
        dirty_data_continue => true
        dirty_data_file => "/Users/ph0ly/trash/dirty.data"
        dirty_data_file_max_size => 1000
```

`}` `}`

**Run Logstash**

Use the following command to start Logstash:

```
logstash -f <path_to_config_file>
```

The `batch_size` parameter specifies the number of records to send to DataHub in each batch. The default value is 125. To start Logstash with a specific batch size, use the following command:

```
logstash -f <path_to_config_file> -b 256
```

Parameters:

```
    access_id(Required): Your Alibaba Cloud AccessKey ID.
    access_key(Required): Your Alibaba Cloud AccessKey secret.
    endpoint(Required): The DataHub service endpoint.
    project_name(Required): The DataHub project name.
    topic_name(Required): The DataHub topic name.
    retry_times(Optional): The number of retries.
      - -1: Infinite retries (default).
      - 0: No retries.
      - >0: A specific number of retries.
    retry_interval(Optional): The interval between retries in seconds. Default: 5.
    skip_after_retry(Optional): Specifies whether to skip the current data batch if ret
ries are exhausted due to a DataHub exception. Default: false.
    approximate_request_bytes(Optional): Limits the size of each request in bytes to pr
event rejections due to an excessively large request body. This is an approximate value . Default: 2048576 (2 MB).
    shard_keys(Optional): An array of field names used to calculate a hash for routing
each record to a specific shard.
    shard_id(Optional): Specifies a fixed shard ID to which all data is sent. This para
meter takes precedence over `shard_keys`. If both are unspecified, data is sent to shar ds in a round-robin fashion.
    dirty_data_continue(Optional): If set to true, continues processing by ignoring dir
ty data. This option requires `dirty_data_file` to be set. Default: false.
    dirty_data_file(Optional): The file to store dirty data. This must be specified if
`dirty_data_continue` is true. Note: The dirty data file is split into two parts, .part 1 and .part2, to manage older and newer data.
    dirty_data_file_max_size(Optional): The maximum size in bytes for the dirty data fi
le. This is an approximate limit.
    enable_pb(Optional): Specifies whether to use Protocol Buffers (PB) for data transm
ission. Default: true. Set to false if you are using a private cloud that does not supp ort PB.
```

**Read data with the Logstash Input plugin**

**Read DataHub data and write to a file**

The Logstash configuration is as follows:

```bash
input {
    datahub {
        access_id => "Your accessId"
        access_key => "Your accessKey"
        endpoint => "Endpoint"
        project_name => "test_project"
        topic_name => "test_topic"
        interval=> 5
        # Example of setting a starting cursor for specific shards
        #cursor => {
        #    "0"=>"20000000000000000000000003110091"
        #    "2"=>"20000000000000000000000003110091"
        #    "1"=>"20000000000000000000000003110091"
        #    "4"=>"20000000000000000000000003110091"
        #    "3"=>"20000000000000000000000003110000"
```

`#}`

```
        shard_ids => []
        pos_file => "/home/admin/logstash/pos_file"
```

`}` `}`

```
output {
    file {
        path => "/home/admin/logstash/output"
```

`}` `}`

**Parameters**

```
    access_id(Required): Your Alibaba Cloud AccessKey ID.
    access_key(Required): Your Alibaba Cloud AccessKey secret.
    endpoint(Required): The DataHub service endpoint.
    project_name(Required): The DataHub project name.
    topic_name(Required): The DataHub topic name.
    retry_times(Optional): The number of retries.
      - -1: Infinite retries.
      - 0: No retries.
      - >0: A specific number of retries.
    retry_interval(Optional): The interval between retries in seconds.
    shard_ids(Optional): An array of shard IDs to read from. If empty, all shards are r
ead by default.
    cursor(Optional): The starting cursor for consumption. If not specified, consumptio
n starts from the beginning.
    pos_file(Required): The checkpoint file for recording consumption progress. The con
sumer preferentially uses the checkpoint to resume from the last offset.
    enable_pb(Optional): Specifies whether to use Protocol Buffers (PB) for data transm
ission. Default: true. Set to false if you are using a private cloud that does not supp ort PB.
    compress_method(Optional): The compression algorithm for network transmission. By d
efault, no compression is used. Options: "lz4", "deflate".
    print_debug_info(Optional): Prints debug information from DataHub. Default: false.
Enabling this will print a large amount of information and should only be used for debu gging.
```

**FAQ**

**Q: How do I write Logstash built-in fields to DataHub?**

A: Logstash adds built-in fields, such as `@timestamp` , to every record. Because DataHub does not support column names with special characters, you must rename these fields in your configuration. For example, to rename `@timestamp` to `column_name` , add the following configuration:

```
filter{
    mutate {
      rename => {
        "@timestamp" => "column_name"
```

`}` `}`

**References**

For more configuration parameters, refer to the official Logstash website and the ELK stack Chinese guide.

### DataHub plug-ins for OGG

#### Overview

As the big data market grows, traditional relational database management systems (RDBMSs) cannot meet the needs of online analytical processing (OLAP) scenarios. This topic describes how to synchronize data from an Oracle database to DataHub, which is a big data processing platform of Apsara Stack, in real time. Then, you can use big data tools to analyze your data.

**Background information**

Oracle GoldenGate (OGG) is a tool for log-based structured data replication across heterogeneous environments. It is used for data backup between primary and secondary Oracle databases. It is also used to synchronize data from Oracle databases to other databases such as IBM Db2 and MySQL databases. The following figure shows the logical architecture of OGG. OGG is deployed on the source and destination databases and involves Data Pump, Manager, Extract, Collector, and Replicat processes. Manager process: the control process of OGG. Both the source and destination databases have one and only one Manager process. The Manager process is used to start, stop, and monitor other processes. Extract process: a process that extracts data from the source database tables or transaction logs. You can configure the Extract process for initial data loads and incremental data synchronization. For initial data loads, the Extract process directly synchronizes data from the source tables to the destination database. To keep source data synchronized to the destination database, the Extract process captures incremental data manipulation language (DML) and data definition language (DDL) operations after the initial data load. This topic describes incremental data synchronization. Data Pump process: The Extract process writes all the captured operations to a trail file on the source database. The Data Pump process reads the trail file on the source database and sends the data operations over the network to the remote trail file on the destination database. Collector process: a process on the destination database. It receives data from the source database and generates trail files. Replicat process: a process that reads the trail file on the destination database, reconstructs the DML or DDL operations, and then applies them to the destination database. The plug-in described in this topic serves as a Replicat process. OGG offers the Replicat feature that applies the updated data to DataHub by analyzing trail files. The data in DataHub can be processed in real time by using Realtime Compute and can be stored in MaxCompute for offline data processing. The current version of the DataHub plug-in for OGG is 2.0.5. You can download the package of the latest version from the link provided at the end of this topic, or download the source code from GitHub.

**Supported database versions**

| Database | Supported version | Plug-in version |
|---|---|---|
| Oracle | 11g to 19c | 2.0.2 to 2.0.8 |
| MySQL | Enterprise Edition and Community Edition | 2.0.3 to 2.0.8 |

**Scenarios**

The following example describes how to use the DataHub plug-in for OGG. A source Oracle table stores information about sales orders. The table contains three fields. The field names are oid, pid, and num, which indicate the order ID, commodity ID, and commodity quantity. The data types of these fields are all INT. Before you perform incremental data synchronization, synchronize existing data from the source table to MaxCompute by using DataX. To synchronize incremental data, perform the following steps:
1. Create a topic in DataHub and set the schema of the topic to (string record_id, string
optype, string readtime, bigint oid_before, bigint oid_after, bigint pid_before, bigint pid_after, bigint num_before, bigint num_after).
2. Install and configure the DataHub plug-in for OGG and specify the following parameters to
configure the field mappings:

```xml
<ctypeColumn>optype</ctypeColumn> <ctimeColumn>readtime</ctimeColumn> <cidColumn>record_id</cidColumn> <columnMapping>
     <column src="oid" dest="oid_after" destOld="oid_before" isShardColumn="true"/>
     <column src="pid" dest="pid_after" destOld="pid_before"/>
     <column src="num" dest="num_after" destOld="num_before"/>
</columnMapping>
```

The optype parameter indicates the type of the data update. Valid values of the optype parameter are I, D, and U, which represent the insert, delete, and update operations. The readtime parameter indicates the time of the data update.
3. When the plug-in can properly run, data updates are synchronized from the source table to
DataHub. For example, after you insert a record (1,2,1) into the source table, DataHub receives the following record:

```
+--------+------------+------------+------------+------------+------------+------------ ------------+------------+
| record_id | optype     | readtime   | oid_before | oid_after  | pid_before | pid_af
ter | num_before | num_after | +-------+------------+------------+------------+------------+------------+------------+ -----------+------------+
| 14810373343020000 |     I          | 2016-12-06 15:15:28.000141 | NULL       | 1
| NULL       | 2          | NULL       | 1   |
```

If you change a value in the record, DataHub receives the updated record. For example, if you change the value of the num field to 20, DataHub receives the following updated record that shows both the original values and the updated values:

```
+-------+------------+------------+------------+------------+------------+------------+ -----------+------------+
| record_id | optype     | readtime   | oid_before | oid_after  | pid_before | pid_af
ter | num_before | num_after | +--------+------------+------------+------------+------------+------------+------------ ------------+------------+
| 14810373343080000 |     U          | 2016-12-06 15:15:58.000253 | 1          | 1
| 2          | 2          | 1          | 20         |
```

4. Start Oracle GoldenGate Software Command Interface (GGSCI) on the source database. In
GGSCI, run the `stats dhext` command to query the operation statistics of each table. You can also run the command on the destination database to check whether the operation statistics are the same on the source database and the destination database.

**Real-time analysis**

You can use Realtime Compute to summarize in real time the data of the previous day generated by offline analysis. For example, you can obtain information about the total number of sales orders and the sales volume of each commodity in real time. For each piece of incoming data change, you can identify the changed values and update the statistics in real time.

**Offline analysis**

To facilitate offline analysis, you can store DataHub data in MaxCompute. Run the following command to create a table with the specified schema in MaxCompute:

```
create table orders_log(record_id string, optype string, readtime string, oid_before bi gint, oid_after bigint, pid_before bigint, pid_after bigint, num_before bigint, num_aft er bigint);
```

Create a DataConnector to synchronize data to MaxCompute. The data that flows into DataHub is automatically synchronized to MaxCompute. We recommend that you store the data synchronized to MaxCompute in different partitions based on the time when the data is synchronized. For example, the incremental data of each day is stored in an independent partition. This way, after the data synchronization on a day is complete, data stored in the corresponding partition can be processed on the same day. You can merge the incremental data of that day with the latest full data. Then, the final full data is obtained. For ease of illustration, partitions are not considered in the following example. The incremental data generated on December 6, 2016 is used in this example. The full data of the previous day is stored in the orders_base table, and the incremental data synchronized from DataHub is stored in the orders_log table. If you merge the two tables, the final full data is written into the orders_result table. Execute the following SQL statement in MaxCompute to perform the preceding operations:

```
INSERT OVERWRITE TABLE orders_result SELECT t.oid, t.pid, t.num FROM
```

`(`

```
     SELECT oid, pid, num, '0' x_record_id, 1 AS x_optype
     FROM
     orders_base
     UNION ALL
     SELECT decode(optype,'D',oid_before,oid_after) AS oid
              , decode(optype,'D', pid_before,pid_after) AS pid
              , num_after AS num
              , record_id x_record_id
              , decode(optype, 'D', 0, 1) AS x_optype
     FROM
     orders_log
 ) t
JOIN
```

`(`

```
     SELECT
     oid
     , pid
     , max(record_id) x_max_modified
     FROM
```

`(`

```
     SELECT
     oid
     , pid
     , '0' record_id
     FROM
     orders_base UNION ALL SELECT
                      decode(optype,'D',oid_before,oid_after) AS oid
                      , decode(optype,'D', pid_before,pid_after) AS pid
                      , record_id
                      FROM
                      orders_log ) g
     GROUP BY oid , pid
 ) s
```

`ON`

```
t.oid = s.oid AND t.pid = s.pid AND t.x_record_id = s.x_max_modified AND t.x_optype <>
```

0;

**Parameters**

**configure**

| Parameter | Default value | Required | Description |
|---|---|---|---|
| batchSize | 1000 | No | The maximum number of records that can be written to DataHub at a time. |

| batchTimeoutMs | 5000 | No | The maximum time to wait after which a new flush is triggered. Minimum value: 1000. Unit: milliseconds. |
|---|---|---|---|
| dirtyDataContinue | false | No | Specifies whether to ignore dirty records. |
| dirtyDataFile | datahub ogg plugin.di _ _ rty | No | The name of the file that stores dirty records. |
| dirtyDataFileMaxSize | 500 | No | The maximum size of the file that stores dirty records. Unit: MB. |
| retryTimes | -1 | No | The maximum number of retries. Valid values: -1: unlimited retries. 0: no retries. n: the number of retries. |
| retryInterval | 3000 | No | The interval between two consecutive retries. Unit: milliseconds. |
| disableCheckPointFile | false | No | Specifies whether to prevent the creation of checkpoint files. |
| checkPointFileName | datahub ogg plugin.c _ _ hk | No | The checkpoint file name of the Adapter process. |

| storageCtimeColumnA sTimestamp(Deprecat ed) | false | No | This parameter is deprecated. Time values are converted to the corresponding field type in DataHub. If the original time value is of the TIMESTAMP type, the value is converted to a timestamp in microseconds. If the original time value is of the STRING type, the value is converted to a string in the format of yyyy-MM-dd HH:mm:ss.SSSSSS. |
|---|---|---|---|
| charset | UTF-8 | No | The database character set in Oracle. In most cases, you do not need to set this parameter unless garbled characters occur. |
| commitFlush | true | No | Specifies whether to write uncommitted transactions to storage. If you set this parameter to true, data loss can be prevented, but the overall execution performance is affected. Set this parameter to true unless you encounter performance bottlenecks. Note This parameter is deprecated. |
| reportMetric | false | No | Specifies whether to report metrics. |
| reportMetricIntervalMs | 5 * 60 * 1000 | No | The intervals at which metrics are reported. The time is recounted after each reporting. Unit: milliseconds. |

| buildCorePollSize | Number of configured tables | No | The minimum number of threads in the thread pool for parsing data. |
|---|---|---|---|
| buildMaximumPoolSize | Twice the value of the buildCorePollSize parameter | No | The maximum number of threads in the thread pool for parsing data. |
| writeCorePollSize | Number of configured tables | No | The minimum number of threads in the thread pool for writing data to DataHub. |
| writeMaximumPoolSize | Number of configured tables | No | The maximum number of threads in the thread pool for writing data to DataHub. |

**defaultOracleConfigure**

| Parameter | Default value | Required | Description |
|---|---|---|---|
| sid | - | Yes | The system identifier (SID) of the Oracle database. |
| schema | - | Yes | The schema of the Oracle database. |
| dateFormat(Deprecate d) | yyyy-MM-dd HH:mm:ss | No | The format into which timestamps are converted. |

**defaultDatahubConfigure**

| Parameter | Default value | Required | Description |
|---|---|---|---|
| endPoint | - | Yes | The endpoint of DataHub. |
| project | - | Yes | The name of the DataHub project. |

| accessId | - | Yes | The AccessKey ID used to access DataHub. |
|---|---|---|---|
| accessKey | - | Yes | The AccessKey secret used to access DataHub. |
| compressType | - | No | The data compression format. Valid values: DEFLATE and LZ4. By default, the data is not compressed. |
| enablePb | false | No | Specifies whether to enable Protocol Buffers (Protobuf) for data transfer. |
| ctypeColumn | - | No | The field in DataHub that indicates the data update type. The configuration can be overwritten by the ctypeColumn parameter in the mappings. The value must be of the STRING type. |
| ctimeColumn | - | No | The field in DataHub that indicates the time when the data insert, update, or delete operation is performed. The configuration can be overwritten by the ctimeColumn parameter in the mappings. The value must be of the STRING or TIMESTAMP type. |

| cidColumn | - | No | The field in DataHub that indicates the sequence number of the updated record. The configuration can be overwritten by the cidColumn parameter in the mappings. The sequence number increases as more records are updated. Multiple sequence numbers may not be consecutive. The value must be of the STRING type. |
|---|---|---|---|
| constColumnMap | - | No | The added field that contains a single constant value specified for each record. The values specified for different records in this field are separated with commas (,) in the format similar to c1=xxx,c2=xxx. The configuration can be overwritten by the constColumnMap parameter in the mappings. The field indicates the data update time on the source database. The following table describes the parameters that can be used in this field. |

**constColumnMap**

| Parameter | Description |
|---|---|
| %t | The UNIX timestamp that indicates the number of milliseconds that have elapsed since 00:00:00 Thursday, January 1, 1970. |
| %a | The abbreviation for the weekday name. Example: Mon. |
| %A | The full weekday name. Example: Monday. |

| %b | The abbreviation of the month name. Example: Jan. |
|---|---|
| %B | The full month name. Example: January. |
| %c | The date and time. Example: Thu Mar 3 23:05:25 2005. |
| %d | The day of the month. Example: 01. |
| %D | The date. Example: 05/09/20. |
| %H | The hour in the 24-hour clock. Valid values: 00 to 23. |
| %I | The hour in the 12-hour clock. Valid values: 01 to 12. |
| %j | The day of the year. Valid values: 001 to 366. |
| %k | The hour in the 24-hour clock. Valid values: 00 to 23. |
| %m | The month. Valid values: 01 to 12. |
| %M | The minute. Valid values: 00 to 59. |
| %p | The period of the current day. Valid values: am and pm. |
| %s | The UNIX timestamp that indicates the number of milliseconds that have elapsed since 00:00:00 Thursday, January 1, 1970. |
| %S | The second. Valid values: 00 to 59. |
| %y | The last two digits of the year: Valid values: 00 to 99. |
| %Y | The year. Example: 2010. |

| %z | The time zone. Example: +0800 for UTC+8. |
|---|---|

To use the date when the data is synchronized to MaxCompute as the value of the partition

| <constColumnMap>ds=%Y%m%d</constColumnMap> |   |   |
|---|---|---|
| ameter value, such as | 20200509 | , is written to |

**mapping**

| Parameter | Default value | Required | Description |
|---|---|---|---|
| oracleSchema | - | No | If you do not set this parameter, the schema specified by the defaultOracleConfigur e parameter is used. |
| oracleTable | - | Yes | The name of the Oracle table. |
| datahubProject | - | No | If you do not set this parameter, the project specified by the defaultDatahubConfig ure parameter is used. |
| datahubAccessId(Depr ecated) | - | No | This parameter is deprecated. By default, the AccessKey ID specified by the defaultDatahubConfig ure parameter is used. |
| datahubAccessKey(De precated) | - | No | This parameter is deprecated. By default, the AccessKey secret specified by the defaultDatahubConfig ure parameter is used. |
| datahubTopic | - | Yes | The name of the DataHub topic. |
| shardId(Deprecated) | - | No | The IDs of the shards. If you set this parameter, the shard IDs are not automatically updated. Example: 0,1,2. |

| rowIdColumn | - | No | The field in DataHub that indicates the IDs of the records. The value must be of the STRING type. This parameter is used if the source Oracle table does not have a primary key. |
|---|---|---|---|
| ctypeColumn | - | No | This parameter is the same as the ctypeColumn parameter in defaultDatahubConfig ure. |
| ctimeColumn | - | No | This parameter is the same as the ctimeColumn parameter in defaultDatahubConfig ure. |
| cidColumn | - | No | This parameter is the same as the cidColumn parameter in defaultDatahubConfig ure. |
| constColumnMap | - | No | This parameter is the same as the constColumnMap parameter in defaultDatahubConfig ure. |

**Parameters in columnMapping**

| Parameter | Default value | Required | Description |
|---|---|---|---|
| src | - | Yes | The field name in the Oracle table. |
| dest | - | Yes | The field name in the DataHub topic. |

| destOld | - | No | The name of the field that records the data before the data is transmitted to the DataHub topic. |
|---|---|---|---|
| isShardColumn | false | No | Specifies whether to generate shard IDs based on the hash key values. |
| isKeyColumn | false | No | Specifies whether to write the value of this parameter before the change to the DataHub field that corresponds to the dest parameter if the value is NULL after the change, but is not NULL before the change. |
| isDateFormat | true | No | Specifies whether to convert time values to the format specified by the dateFormat parameter. This parameter takes effect only when the corresponding DataHub field is of the TIMESTAMP type. If the data type of the field is DATE or TIMESTAMP in Oracle, you do not need to set this parameter. If you set this parameter to false, the source data must be of the LONG type. |
| dateFormat | yyyy-MM- dd HH:mm:ss[.fffffffff] | No | The date format into which time values are converted. In most cases, you do not need to set this parameter unless the values do not conform to the default format. |

| isDefaultCharset | true | No | Specifies whether to use the default character set in Oracle. In most cases, you do not need to set this parameter unless garbled characters occur. You must first configure the character set, and then set this parameter to false for the field that contains garbled characters. |
|---|---|---|---|

**FAQ**

**Files for troubleshooting:**

**datahub-ogg-plugin.log:** the logs of the DataHub plug-in. Most of the issues can be
resolved by checking the errors reported in such logs. Logs of this type are stored in the log subdirectory of the plug-in directory.
**ggserr.log:** the monitoring logs. In most cases, you can view user operations and the
startup status in the monitoring logs in the ogg/adapter directory. Reported errors such as the invalid configuration of the Extract process or the missing of specific dynamic-link libraries (DDLs) are recorded in the monitoring logs.
**dirrpt:** the process report files. Run the VIEW REPORT command to view the error
information in a process report file. If data is transmitted to the destination database without error reported in both the ggserr.log and the plug-in log files, you may find the error information recorded in this file.
**dirchk:** the log file that stores the checkpoint information of a process in OGG.
**datahub_ogg_plugin.chk:** the log file that stores the offset information of the plug-in.

**Q: What do I do if I cannot write data to DataHub?**

A: Check the whole process. Check whether the dirdat file stores the data read from the source database. If not, the cause lies in the Extract process on the source database. Check whether the dirdat file stores replicated data on the destination database. If not, the cause lies in the Data Pump process on the source database. View the log files of the plug-in to check whether the data is skipped by the checkpoints, or an error occurs with the plug-in. **These are the most common causes.** If the data is transmitted to the destination database and no errors are recorded in the log files of the plug-in, check the log files in the dirrpt subdirectory. The data may be skipped by the checkpoints created on the destination database. Check whether the Oracle schema is correctly configured. Data may be skipped because the Oracle schema does not match the schema of the source database.

**Q: What do I do if I cannot query the record ID but other fields are returned?**

A: In most cases, this issue may be caused by configuration errors. You must thoroughly check the configurations. Check the version of the plug-in. Only version 2.0.3 or later allows you to query the record ID. Check whether the token of the Extract process on the source database is correctly

| TABLE OGG TEST.*,tokens (TKN- _ |   |
|---|---|
|   | . For example, if you mistakenly enter TKN-ROWID as |

configured in the following syntax: `TABLE OGG_TEST.*,tokens (TKN-` TKN_ROWID, the query request fails. Check whether `<rowIdColumn></rowIdColumn>` is configured in the configure.xml file on the destination database. Run the Logdump command to check whether the record ID can be obtained, as shown in the following figure.

**Q: What do I do if an error occurs in the token clause for TKN-ROWID?**

**Error messages:**

```
2020-01-17 16:17:17 INFO OGG-06509 Oracle GoldenGate Capture for Oracle, dhext.prm: Using the following key columns for source table OGG_TEST.ORDERS: OID. 2020-01-17 16:17:17 INFO OGG-01298 Oracle GoldenGate Capture for Oracle, dhext.prm: Column function diagnostic message: could not find column "RECORD". 2020-01-17 16:17:17 ERROR OGG-00369 Oracle GoldenGate Capture for Oracle, dhext.prm: Error in token clause for TKN-ROWID. 2020-01-17 16:17:17 ERROR OGG-01668 Oracle GoldenGate Capture for Oracle, dhext.prm: PROCESS ABENDING.
```

A: If the row ID still cannot be retrieved after you use the token syntax `TABLE` OGG_TEST.*,tokens (TKN-ROWID=@GETENV('RECORD','rowid')); , use the following methods to troubleshoot the issue: Check the version of the plug-in. Only version 2.0.3 or later allows you to query row IDs. Check your token syntax with the official sample provided by OGG. If the syntax is consistent, change the single quotation marks (') to double quotation marks (") in the `@GETENV('RECORD','rowid'))` part. Restart the Manager process.

**Q: What do I do if the error "dsOperation.getPosition():xxxxxxx old sendPosition is**

**xxxxx, Skip this Operation, it maybe duplicated." is returned?**

A: In most cases, this issue occurs because processes restart on the source database. This error indicates that checkpoints of the DataHub plug-in are duplicate. The system often mistakenly identifies duplication. In addition, checkpoints of OGG are enough for normal running of the application. You can set disableCheckPointFile to true to prevent the creation of checkpoint files in the DataHub plug-in. In later versions, we will no longer use checkpoints of the DataHub plug-in.

**Q: Why do I receive the log error "Unable to create operation:**

**com.goldengate.atg.datasource.ConcurrentTransactionException: Multiple "Begin-**

**Transaction" operations received for the same source transaction. Current**

**transaction begin position: xxx(xxx); current trail position: xxx"?**

A: Transactions on the source database conflict. Check whether an issue exists on the source Oracle database.

**Q: What do I do if an 8-hour delay occurs after the data is transmitted to DataHub?**

A: Set the goldengate.userexit.timestamp parameter to UTC+8 in the javaue.properties file and then restart DataHub Writer.

**Q: What do I do if specific fields are left empty after the DataHub plug-in parses**

**the data?**

A: Run the SET DEBUG command to enable the debugging mode in OGG. Check whether the reported full data matches the data on the source database. If the reported data matches the source data, the issue may be caused by incorrect configurations of the columnMapping parameter. If the reported data does not match the source data, check the result data from the Extract process. For more information, see Using the Logdump Utility. You can query a specific redo block address (RBA) in the log file.

**Q: What do I do if a parsing error occurs with the trail files on the source database**

**when OGG 12.3 is used?**

A: We recommend that you install OGG 12.2, or change `RMTTRAIL ./dirdat/st` to `RMTTRAIL` `./dirdat/st format RELEASE 12.2` in the configurations of the Extract process on the destination database.

**Q: What do I do if the error "java.lang.NumberFormatException: for input string :**

**xxxx" is returned?**

A: Check the mappings between Oracle and DataHub. For more information, see **Mappings**
**between data types in Oracle and DataHub**. For example, the mapping is invalid if you
convert the values of the destOld parameter of the STRING type in Oracle to values of the BIGINT type in DataHub.

**Q: What do I do if the error "String index out of range: 10" is returned?**

**Error messages:**

```
2020-01-14 10:03:24 [main] ERROR OperationHandler - dirty data : INSERT on WF_YN_07.CJ_ GLQX202001 [B] [columns: 27] [pos: 00000007260404799638 (seqno=726, rba=404799638)] [ti me: 2020-01-14 08:49:43.883741] java.lang.StringIndexOutOfBoundsException: String index out of range: 10
    at java.lang.AbstractStringBuilder.setCharAt(AbstractStringBuilder.java:407)
    at java.lang.StringBuilder.setCharAt(StringBuilder.java:76)
```

`at`

```
com.aliyun.odps.ogg.handler.datahub.RecordBuilder.convertStrToMicroseconds(RecordBuilder. va:272)
```

`at`

```
com.aliyun.odps.ogg.handler.datahub.RecordBuilder.setTupleData(RecordBuilder.java:242)
```

`at`

```
com.aliyun.odps.ogg.handler.datahub.RecordBuilder.buildTupleRecord(RecordBuilder.java:172
```

`at`

```
com.aliyun.odps.ogg.handler.datahub.RecordBuilder.buildRecord(RecordBuilder.java:82)
```

`at`

```
com.aliyun.odps.ogg.handler.datahub.operations.OperationHandler.processOperation(Operatio andler.java:50)
```

`at`

```
com.aliyun.odps.ogg.handler.datahub.operations.InsertOperationHandler.process(InsertOpera onHandler.java:31)
```

`at`

```
com.aliyun.odps.ogg.handler.datahub.DatahubHandler.operationAdded(DatahubHandler.java:108
    at oracle.goldengate.datasource.DsEventManager$3.send(DsEventManager.java:439)
```

`at`

```
oracle.goldengate.datasource.DsEventManager$EventDispatcher.distributeEvent(DsEventManage java:231)
```

`at`

```
oracle.goldengate.datasource.DsEventManager.fireOperationAdded(DsEventManager.java:447)
```

`at`

```
oracle.goldengate.datasource.AbstractDataSource.fireOperationAdded(AbstractDataSource.jav 464)
```

`at`

```
oracle.goldengate.datasource.UserExitDataSource.addOperationToTransactionAndFireEvent(Use xitDataSource.java:1337)
```

`at`

```
oracle.goldengate.datasource.UserExitDataSource.createOperation(UserExitDataSource.java:1
```

`5)` `at`

```
oracle.goldengate.datasource.UserExitDataSource.createOperation(UserExitDataSource.java:1
```

`6)` A: By default, the time values mapped from Oracle are of the DATE or TIMESTAMP type. A value is converted as a date and time string, such as 2020-01-10:10:00:00 in DataHub. Therefore, if you pass a time value not in the default format, the error occurs. **To resolve**

**this issue, you can set the  isDateFormat  parameter to false in columnMapping.**

**Q: What do I do if I cannot retrieve the values before the update?**

A: Check whether the `GETUPDATEBEFORES` parameter is set on the source database.

**Q: Why is the updated value left empty when the source table has a primary key?**

A: The following scenarios describe the different operations to retrieve the update operations when the source table has or does not have a primary key: For tables that do not have a primary key, if the value of a field is updated from A to B, the update operation is `"B" [before="A"]` . If a field is not updated, and the value is C, the update operation is `"C" [before="C"]` . For tables that have a primary key, if the value of a field is updated from A to B, the

| s | "B" [before="A"] |   |
|---|---|---|
| "" [before="C"] |   |   |
|   |   | . |

updated operation is `"B" [before="A"]` . If a field is not updated, and the value is C, the update operation is `"" [before="C"]` . Solution 1: For example, a table has three fields A, B, and C. Field A is set as the primary key. If Field B is not updated, the updated value of Field B is left empty. If you want to set Field B to the same value as the original value, specify TABLE OGG_TEST.*,keycols(a,b); in the Extract process on the source database. Solution 2: Specify the isKeyColumn parameter in columnMap. Example: `<column src="b"`

```
dest="b" destOld="b_old" isKeyColumn="true"/> .
```

**Q: What do I do if the error "Unsupported major.minor version 52.0" is returned?**

**Error messages:**

```
2019-12-23 18:03:58 [main] ERROR UserExitMain - java.lang.UnsupportedClassVersionError: com/aliyun/datahub/client/model/RecordSchema : Unsupported major.minor version 52.0 java.lang.UnsupportedClassVersionError: com/aliyun/datahub/client/model/RecordSchema : Unsupported major.minor version 52.0
    at oracle.goldengate.datasource.DataSourceLauncher.<init>
(DataSourceLauncher.java:161)
    at oracle.goldengate.datasource.UserExitMain.main(UserExitMain.java:108)
Caused by: org.springframework.beans.factory.BeanDefinitionStoreException: Factory meth od [public final oracle.goldengate.datasource.GGDataSource oracle.goldengate.datasource.factory.DataSourceFactory.getDataSource()] threw exception ; nested exception is java.lang.UnsupportedClassVersionError: com/aliyun/datahub/client/model/RecordSchema : Unsupported major.minor version 52.0
```

`at`

```
org.springframework.beans.factory.support.SimpleInstantiationStrategy.instantiate(SimpleI tantiationStrategy.java:169)
```

`at`

```
org.springframework.beans.factory.support.ConstructorResolver.instantiateUsingFactoryMeth (ConstructorResolver.java:570)
    ... 11 more
Caused by: java.lang.UnsupportedClassVersionError: com/aliyun/datahub/client/model/RecordSchema : Unsupported major.minor version 52.0
```

A: The error occurs because the Java Development Kit (JDK) version that you installed does not meet the environment requirement. We recommend that you download and install the JDK version 1.8, or you can download the source code from GitHub and compile a JAR package.

**Q: What do I do if the "Error opening module ./libggjava_ue.so - libjsig.so:cannot**

**open shared object file:no such file or directory" error is returned?**

A: Check the OGG version, the file to query, and the environment variables. Try to restart the Manager process or your machine. The issue may be resolved by restarting the machine, but this solution is not recommended.

**Q: What do I do if the error "OGG-00425 No DB login established to retrieve a**

**definition for table xxx.xxx" is returned?**

A: Regenerate the source-definitions file and replicate the file to the destination database.

**Q: Why is the error "defaultDatahubConfigure is null" returned?**

**Error messages:**

```
2020-01-17 17:28:32 [main] ERROR DatahubHandler - Init error java.lang.RuntimeException: defaultDatahubConfigure is null
```

`at`

```
com.aliyun.odps.ogg.handler.datahub.ConfigureReader.reader(ConfigureReader.java:117)
```

A: A spelling mistake was corrected in the plug-in V2.0.3. If you stick to the plug-in V2.0.2, change the parameter name from `defalutDatahubConfigure to defaultDatahubConfigure` in the configuration file.

**Q: What do I do if the error "OGG-06551 Oracle GoldenGate Collector: Could not**

**translate host name localhost into an Internet address." is returned on the**

**destination database?**

A: Reset the IP address that is mapped for the host name localhost in the /etc/hosts file on the destination database.

**Q: What do I do if the JVM cannot load a shared library (.so)?**

A: Restart the Manager process after you add the path of the shared library to the

| LD LIBRARY PATH environment variable. Example: _ _ |   |
|---|---|
| LD LIBRARY PATH=${LD LIBRARY PATH}:$JAVA HOME/lib/amd64:$JAVA HOME/lib/amd64/server _ _ _ _ _ _ |   |

**Q: What do I do in the following scenario: The error "2015-06-11 14:01:10 ERROR**

**OGG-01161 Bad column index (5) specified for table OGG_TEST.T_PERSON, max**

**columns = 5" is returned. The Adapter for writing flat files and the JMS Adapter fail**

**to work when I add a field in the table. No issues are found in OGG on the source**

**database.**

A: The schema of the table is not consistent on the source and the destination databases. You must create a DEFGEN configuration file and copy the file to the dirdef directory on the destination database. Then, restart the Replicat process.

**Q: Why is the "Error (4) retrieving column value" error reported in the OGG report**

**file?**

A: In most cases, this is because OGG fails to parse trail files. You can view the debugging logs to identify the RBA that reported the error, and adjust the checkpoint to skip the RBA to resolve the issue.

**Release notes**

**2.0.2**

Download link

**2.0.3**

Download link Record IDs can be retrieved from the source Oracle tables. Data types such as DECIMAL and TIMESTAMP in DataHub are supported. A spelling mistake is corrected in the plug-in V2.0.3. If you stick to the plug-in V2.0.2, change the parameter name from defalutDatahubConfigure to defaultDatahubConfigure in the configuration file. Data compression and data transfer by using Protobuf are supported.

**2.0.4**

Download link Database character sets can be configured. This feature can prevent garbled characters for databases whose data is not encoded in UTF-8.

**2.0.5**

Download link The performance is optimized with transactions per second (TPS) increased by 70% at most. Metrics can be reported for logs. The following issue is fixed: The time when the constColumnMap parameter is retrieved is different from the actual time.

**2.0.6**

Download link The following issue is fixed: Excessive thread data exists. The following issue is fixed: The updated value is empty and cannot be hashed. Data types including TINYINT, SMALLINT, INTEGER, and FLOAT in DataHub are supported.

**2.0.7**

Download link The plug-in is adapted to OGG for Big Data 12.3.2.1, and no longer supports OGG Application Adapters.

**2.0.8**

Download link The plug-in is adapted to OGG for Big Data 19.1.0.0, and no longer supports OGG Application Adapters.

#### OGG for Oracle

##### OGG for Oracle

The DataHub plug-in for Oracle GoldenGate (OGG) captures Oracle data through two modes— OGG Application Adapters and OGG for Big Data—which differ in the process type on the destination database.

**Overview**

DataHub supports two OGG modes for Oracle data collection: OGG Application Adapters and OGG for Big Data. With OGG Application Adapters, the Extract process runs on the destination database. With OGG for Big Data, the Replicat process runs on the destination database.

**Key differences:**

1. Oracle version support: Application Adapters supports only Oracle 11g. OGG for Big Data
supports Oracle 19c and earlier. 2. Maintenance: Application Adapters stopped at version 12.2 with unresolved issues and is no longer maintained. OGG for Big Data is actively updated alongside Oracle.

**Recommended: OGG for Big Data.**

**Data type mappings**

DataHub stores TIMESTAMP values in microseconds. Oracle DATE and TIMESTAMP values are converted to microsecond timestamps during mapping.

| Oracle | DataHub | Description |
|---|---|---|
| char | STRING |   |
| varchar / varchar2 | STRING |   |
| number | BIGINT / DOUBLE / DECIMAL | Integers map to BIGINT. Floating-point numbers map to DOUBLE or DECIMAL depending on precision requirements. |

| INTEGER | BIGINT |   |
|---|---|---|
| BINARY FLOAT / BINARY DOUB _ _ LE | DOUBLE / DECIMAL |   |
| FLOAT | DOUBLE / DECIMAL |   |
| date / timestamp | TIMESTAMP / STRING | Automatically converted to microsecond timestamps in DataHub. |
| raw | STRING | Automatically Base64-encoded before writing to DataHub. |

This table covers common mappings. All Oracle-supported data types are listed in Details of Support for Oracle Data Types.

**Versions and downloads**

The table lists selected plug-in versions. Download other versions from Oracle GoldenGate Downloads or Oracle Software Delivery Cloud.

| datahub-ogg- plugin | Source database | Destination database | Supported Oracle database version | Description |
|---|---|---|---|---|
| 2.0.2 | OGG 12.1.x.x (recommended version: 12.1.2.1) | OGG Application Adapters 12.1.2.1 | Oracle Database 11g |   |

| 2.0.3 | OGG 12.2.x.x (recommended version: 12.2.0.2) | OGG Application Adapters 12.2.0.1 | Oracle Database 11g | Row IDs can be retrieved from the source Oracle tables. Supports DataHub DECIMAL and TIMESTAMP data types. Fixes a typo: "defalutDatahu bConfigure" = > "defaultData hubConfigure". If you still use V2.0.2, rename this parameter in the configuration file. Supports data compression and Protobuf- based data transfer. |
|---|---|---|---|---|
| 2.0.4 | OGG 12.2.x.x (recommended version: 12.2.0.2) | OGG Application Adapters 12.2.0.1 | Oracle Database 11g | Supports configurable database character sets. This prevents garbled characters for non-UTF-8 source databases. |
| 2.0.5 | OGG 12.2.x.x (recommended version: 12.2.0.2) | OGG Application Adapters 12.2.0.1 | Oracle Database 11g | Performance improved: up to 70% higher transactions per second (TPS). Supports log metrics reporting. Fixes incorrect constColumnM ap parameter retrieval timestamps. |

| 2.0.6 | OGG 12.2.x.x (recommended version: 12.2.0.2) | OGG Application Adapters 12.2.0.1 | Oracle Database 11g | The following issue in the plug-in V2.0.5 is fixed: Excessive thread data exists. Fixes an issue where empty updated values cannot be hashed. Supports DataHub TINYINT, SMALLINT, INTEGER, and FLOAT data types. |
|---|---|---|---|---|
| 2.0.7 | OGG 12.3.x.x (recommended version: 12.3.2.1) | OGG for Big Data 12.3.2.1 | Oracle Database 11g and 12c | Adapted to OGG for Big Data 12.3.2.1. No longer supports OGG Application Adapters. |
| 2.0.8 | OGG 19.1.x.x (recommended version: 19.1.0.0) | OGG for Big Data 19.1.0.0 | Oracle Database 19c and earlier | Adapted to OGG for Big Data 19.1.0.0. No longer supports OGG Application Adapters. |
| 2.1.0 | OGG 19.1.x.x (recommended version: 19.1.0.0) | OGG for Big Data 19.1.0.0 | Oracle Database 19c and earlier | Fixes known bugs. |

##### OGG Adapters

This document describes how to install and configure Oracle GoldenGate (OGG) and OGG Adapters to synchronize data from an Oracle database to DataHub.

**Prerequisites**

Oracle 11g is installed on the source. The current plugin version supports only Oracle 11g databases. OGG is installed on the source. Oracle GoldenGate V12.2.0.2 is recommended, but any version in the V12.2.x series is supported. OGG Adapters are installed on the target. Oracle GoldenGate Application Adapters V12.2.0.1 is recommended, but any version in the V12.2.x series is supported. JDK 1.8.

**Procedure**

This section describes how to install and configure OGG and its related components. The installation of the Oracle database is not covered. Important: A professional with operations and maintenance experience should configure the Oracle and OGG parameters. The following example provides a runnable sample configuration. This process requires the following installation packages: OGG OGG Adapters DataHub OGG plugin

**OGG source configuration**

1. . Configure the source database**

|   | Important If you skip any of the following configuration steps, the pre-update values for UPDATE operations might be null . Log in to SQL*Plus as a user with DBA privileges: sqlplus / as sysdba . |   |
|---|---|---|
|   | as sysdba |   |

```bash
# Create a separate tablespace
create tablespace ATMV datafile '/home/oracle/u01/app/oracle/oradata/uprr/ATMV.dbf' siz e 100m autoextend on next 50m maxsize unlimited;
 # Create a user named ogg_test with the password ogg_test
create user ogg_test identified by ogg_test default tablespace ATMV;
 # Grant sufficient privileges to ogg_test
grant connect,resource,dba to ogg_test;
 # Check the supplemental log status
Select SUPPLEMENTAL_LOG_DATA_MIN, SUPPLEMENTAL_LOG_DATA_PK, SUPPLEMENTAL_LOG_DATA_UI, S UPPLEMENTAL_LOG_DATA_FK, SUPPLEMENTAL_LOG_DATA_ALL from v$database;
 # Add supplemental log data for the database
alter database add supplemental log data; alter database add supplemental log data (primary key, unique,foreign key) columns;
 # Rollback commands
alter database drop supplemental log data (primary key, unique,foreign key) columns; alter database drop supplemental log data;
 # For all-column logging mode, note that DELETE operations in this mode only capture p
rimary key values. To capture other columns, configure NOCOMPRESSDELETES in the source Extract process. ALTER DATABASE ADD SUPPLEMENTAL LOG DATA (ALL) COLUMNS;
 # Enable forced logging mode for the database
alter database force logging;
 # Install sequence support
@sequence.sql
```

`#`

```
alter table sys.seq$ add supplemental log data (primary key) columns;
```

2. . Install the OGG source**
After downloading and extracting the OGG installation package, you will see the following directory structure:

```
drwxr-xr-x install drwxrwxr-x response -rwxr-xr-x runInstaller drwxr-xr-x stage
```

Oracle installations typically use a response file. Configure the installation dependencies in `response/oggcore.rsp` as follows:

```bash
oracle.install.responseFileVersion=/oracle/install/rspfmt_ogginstall_response_schema_v12_
# Must match the Oracle version
INSTALL_OPTION=ORA11g
# GoldenGate home directory
SOFTWARE_LOCATION=/home/oracle/u01/ggate
# Do not start the Manager process initially
START_MANAGER=false
# Manager port
MANAGER_PORT=7839
# Corresponding Oracle home directory
DATABASE_LOCATION=/home/oracle/u01/app/oracle/product/11.2.0/dbhome_1
# Optional, can be left unconfigured for now
INVENTORY_LOCATION=
# Group name (In this example, both Oracle and OGG use the ogg_test account. In a produ
ction environment, you can create a separate account for OGG.) UNIX_GROUP_NAME=oinstall
```

Run the following command:

```
runInstaller -silent -responseFile {YOUR_OGG_INSTALL_FILE_PATH}/response/oggcore.rsp
```

| In this example, the OGG installation directory is /home/oracle/u01/ggate installation log is located in /home/oracle/u01/ggate/cfgtoollogs/oui . The message in the silentInstall{timestamp}.log file indicates a successful installation of Oracle GoldenGate Core was successful. . |   |   | /home/oracle/u01/ggate |
|---|---|---|---|
|   |   | /home/oracle/u01/ggate/cfgtoollogs/oui |   |
|   | silentInstall{timestamp}.log |   |   |
| installation of Oracle GoldenGate Core was successful. |   |   |   |

| Run the | /home/oracle/u01/ggate/ggsci |   |
|---|---|---|
| CREATE SUBDIRS |   |   |
|   |   | to generate the requir |

Run the `/home/oracle/u01/ggate/ggsci` command. At the prompt, enter the command `CREATE SUBDIRS` to generate the required directories for OGG. This completes the source OGG installation.
3. . Configure the source Manager**
Use the GGSCI utility to configure the source Manager process. Run the `edit params mgr` command and add the following content:

```
PORT 7839 DYNAMICPORTLIST 7840-7849 USERID ogg_test, PASSWORD ogg_test PURGEOLDEXTRACTS ./dirdat/*, USECHECKPOINTS, MINKEEPDAYS 7 LAGREPORTHOURS 1 LAGINFOMINUTES 30 LAGCRITICALMINUTES 45 PURGEDDLHISTORY MINKEEPDAYS 3, MAXKEEPDAYS 7 PURGEMARKERHISTORY MINKEEPDAYS 3, MAXKEEPDAYS 7
```

After saving the configuration, run `view params mgr` to verify it. Then, run the following commands in sequence:
1. Start the Manager process: `start mgr` .
2. Check the Manager status: `info mgr` .
4. . Configure the source Extract**
Use GGSCI to configure the Extract process. You can use any name for the process. This example uses `dhext` . Run `edit params dhext` and add the following content:

```
EXTRACT dhext SETENV (NLS_LANG="AMERICAN_AMERICA.AL32UTF8") DBOPTIONS ALLOWUNUSEDCOLUMN USERID ogg_test, PASSWORD ogg_test REPORTCOUNT EVERY 1 MINUTES, RATE NUMFILES 5000 DISCARDFILE ./dirrpt/ext_test.dsc, APPEND, MEGABYTES 100 DISCARDROLLOVER AT 2:00 WARNLONGTRANS 2h, CHECKINTERVAL 3m EXTTRAIL ./dirdat/st, MEGABYTES 200 DDL & INCLUDE MAPPED OBJTYPE 'table' & INCLUDE MAPPED OBJTYPE 'index' & INCLUDE MAPPED OBJTYPE 'SEQUENCE' & EXCLUDE OPTYPE COMMENT DDLOPTIONS NOCROSSRENAME REPORT TABLE OGG_TEST.*,tokens (TKN-ROWID=@GETENV('RECORD','rowid')); SEQUENCE OGG_TEST.*; GETUPDATEBEFORES
```

**Note**

The line TABLE OGG_TEST.*, tokens (TKN-ROWID=@GETENV('RECORD','rowid')); is used to capture the `rowid` from the source table. If you do not need to capture the `rowid` , you can change this line to `TABLE OGG_TEST.*` . Add and start the Extract process:

```bash
# Add the Extract process
add extract dhext,tranlog, begin now
# Set the size of each trail file to 200 MB
add exttrail ./dirdat/st,extract dhext, megabytes 200
# Start the process
start dhext
```

After the Extract process starts, it captures database changes, which you can view in the files in the `ggate/dirdat` directory.
5. . Generate definition file**

**Note**

This step is not required for OGG versions 12.2.x and later. In GGSCI on the source, create a parameter file for the definition generator by running `edit` `params defgen` . Add the following content:

```
DEFSFILE ./dirdef/ogg_test.def USERID ogg_test, PASSWORD ogg_test table OGG_TEST.*;
```

Run the following command in the shell to generate `ogg_test.def` . After generating the file, copy it to the `dirdef` directory on the target. `./defgen paramfile ./dirprm/defgen.prm`
6. . Configure the source Pump**
Start GGSCI and configure the Pump process by running the `edit params pump` command:

```
EXTRACT pump RMTHOST xx.xx.xx.xx, MGRPORT 7839, COMPRESS PASSTHRU NUMFILES 5000 RMTTRAIL ./dirdat/st DYNAMICRESOLUTION TABLE OGG_TEST.*; SEQUENCE OGG_TEST.*;
```

Add and start the Pump process:

```bash
# Add the Pump process
add extract pump,exttrailsource ./dirdat/st
# Add the remote trail file on the target and set its size to 200 MB
add rmttrail ./dirdat/st,extract pump,megabytes 200
# Before starting the Pump, ensure the Manager process on the target is running
start pump
```

After the Pump process starts, you can find the transmitted trail files in the `dirdat` directory on the target.

**OGG target configuration**

1. . Install the OGG target**
OGG Adapters, the OGG component on the target, does not require a formal installation. Simply extract the package. After extraction, you must create the necessary directories. Start

| create subdirs |   |   |
|---|---|---|
| with | dir | in th |

GGSCI and run the `create subdirs` command. This command creates several new Copy the definition file generated on the source to the `dirdef` directory. This step is not required for OGG versions 12.2.x and later.
2. . Install and configure the DataHub plugin**
Prerequisites: JDK ≥ 1.7. After you configure JAVA_HOME and LD_LIBRARY_PATH, you can add the environment variables to the ~/.bash_profile file. For example:

```
export JAVA_HOME=/xxx/xxx export JRE_HOME=/xxx/xxx/jrexx export LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:$JRE_HOME/lib/amd64:$JRE_HOME/lib/amd64/server
```

After setting the environment variables, download and extract datahub-ogg-plugin.tar.gz. Modify the `javaue.properties` file in the `conf` directory, replacing `{YOUR_HOME}` with the path where you extracted the plugin.

```
gg.handlerlist=ggdatahub gg.handler.ggdatahub.type=com.aliyun.odps.ogg.handler.datahub.DatahubHandler gg.handler.ggdatahub.configureFileName={YOUR_HOME}/aliyun-datahub-oggplugin/conf/configure.xml goldengate.userexit.nochkpt=false goldengate.userexit.timestamp=utc+8 gg.classpath={YOUR_HOME}/aliyun-datahub-ogg-plugin/lib/* gg.log.level=debug jvm.bootoptions=-Xmx512m -Dlog4j.configuration=file:{YOUR_HOME}/datahub-ogg-plugin/conf /log4j.properties -Djava.class.path=ggjava/ggjava.jar
```

Modify the `log4j.properties` file in the `conf` directory, replacing `{YOUR_HOME}` with the extraction path. Then, modify the `configure.xml` file in the `conf` directory as described in the file's comments.

```xml
<?xml version="1.0" encoding="UTF-8"?> <configue>
    <defaultOracleConfigure>
        <!-- Oracle SID. Required. -->
        <sid>100</sid>
        <!-- Oracle schema. Can be overridden by oracleSchema in a mapping. One of them
must be specified. -->
        <schema>ogg_test</schema>
    </defaultOracleConfigure>
    <defalutDatahubConfigure>
        <!-- DataHub endpoint. Required. -->
        <endPoint>YOUR_DATAHUB_ENDPOINT</endPoint>
        <!-- DataHub project. Can be overridden by datahubProject in a mapping. One of
them must be specified. -->
        <project>YOUR_DATAHUB_PROJECT</project>
        <!-- DataHub AccessKey ID. Can be overridden by datahubAccessId in a mapping. O
ne of them must be specified. -->
        <accessId>YOUR_DATAHUB_ACCESS_ID</accessId>
        <!-- DataHub AccessKey secret. Can be overridden by datahubAccessKey in a
mapping. One of them must be specified. -->
        <accessKey>YOUR_DATAHUB_ACCESS_KEY</accessKey>
        <!-- The target field in DataHub for the data change type. Can be overridden by
ctypeColumn in a columnMapping. -->
        <ctypeColumn>optype</ctypeColumn>
        <!-- The target field in DataHub for the data change timestamp. Can be
overridden by ctimeColumn in a columnMapping. -->
        <ctimeColumn>readtime</ctimeColumn>
```

`ct`

```xml
eCou eadt e/ct eCou
        <!-- The target field in DataHub for the data change sequence ID. It increments
with each change but is not guaranteed to be consecutive. Can be overridden by cidColum n in a columnMapping. -->
        <cidColumn>record_id</cidColumn>
    </defalutDatahubConfigure>
    <!-- Default behavior is the strictest: infinite retries, no dirty data file, and e
xit on failure. -->
    <!-- The maximum number of records to upload per batch. Optional. Default: 1000. --
```

`>`

```xml
    <batchSize>1000</batchSize>
    <!-- The default format for converting time fields. Optional. Default: yyyy-MM-dd H
H:mm:ss. -->
    <defaultDateFormat>yyyy-MM-dd HH:mm:ss</defaultDateFormat>
    <!-- Whether to continue processing if dirty data is encountered. Optional.
Default: false. -->
    <dirtyDataContinue>true</dirtyDataContinue>
    <!-- The file for storing dirty data. Optional. Default: datahub_ogg_plugin.dirty.
-->
    <dirtyDataFile>datahub_ogg_plugin.dirty</dirtyDataFile>
    <!-- The maximum size of the dirty data file in MB. Optional. Default: 500. -->
    <dirtyDataFileMaxSize>200</dirtyDataFileMaxSize>
    <!-- The retry count. Use -1 for infinite retries, 0 for no retries, or a positive
integer for a specific number of retries. Optional. Default: -1. -->
    <retryCount>0</retryCount>
    <!-- A comma-separated list of shard IDs to use. This setting takes precedence. Opt
ional. Example: 0,1. -->
    <shardId>0,1</shardId>
    <!-- The interval between retries in milliseconds. Optional. Default: 3000. -->
    <retryInterval>4000</retryInterval>
    <!-- The checkpoint file. Optional. Default: datahub_ogg_plugin.chk. -->
    <checkPointFileName>datahub_ogg_plugin.chk</checkPointFileName>
    <mappings>
        <mapping>
            <!-- Oracle schema. See the description above. -->
            <oracleSchema></oracleSchema>
            <!-- Oracle table. Required. -->
            <oracleTable>t_person</oracleTable>
            <!-- DataHub project. See the description above. -->
            <datahubProject></datahubProject>
            <!-- DataHub topic. Required. -->
            <datahubTopic>t_person</datahubTopic>
            <!-- The target field in DataHub for the Oracle table rowid. Optional. -->
            <rowIdColumn></rowIdColumn>
            <ctypeColumn></ctypeColumn>
            <ctimeColumn></ctimeColumn>
            <cidColumn></cidColumn>
            <columnMapping>
                <!--
                src: The name of the Oracle column. Required.
                dest: The name of the DataHub field. Required.
                destOld: The DataHub field for storing the pre-update data. Optional.
                isShardColumn: Whether to use this column as the hash key for sharding.
Optional. Default: false. Can be overridden by shardId.
                isDateFormat: Whether to format the timestamp field using dateFormat. De
```

```
fault: true. If false, the source data must be of the long type.
                dateFormat: The format for the timestamp field. If not specified, the d
efault format is used.
                -->
                <column src="id" dest="id" isShardColumn="true"  isDateFormat="false" da
teFormat="yyyy-MM-dd HH:mm:ss"/>
                <column src="name" dest="name" isShardColumn="true"/>
                <column src="age" dest="age"/>
                <column src="address" dest="address"/>
                <column src="comments" dest="comments"/>
                <column src="sex" dest="sex"/>
                <column src="temp" dest="temp" destOld="temp1"/>
            </columnMapping>
        </mapping>
    </mappings>
</configue>
```

3. . Configure the target Manager**
Run the `edit params mgr` command to configure the Manager.

```
PORT 7839 DYNAMICPORTLIST 7840-7849 PURGEOLDEXTRACTS ./dirdat/*, USECHECKPOINTS, MINKEEPDAYS 7 LAGREPORTHOURS 1 LAGINFOMINUTES 30 LAGCRITICALMINUTES 45 PURGEDDLHISTORY MINKEEPDAYS 3, MAXKEEPDAYS 7 PURGEMARKERHISTORY MINKEEPDAYS 3, MAXKEEPDAYS 7
```

Then, start the Manager process by running the `start mgr` command.
4. . Configure the target writer**
Use the `edit params dhwriter` command in GGSCI to create the configuration file.

```
extract dhwriter getEnv (JAVA_HOME) getEnv (LD_LIBRARY_PATH) getEnv (PATH) CUSEREXIT ./libggjava_ue.so CUSEREXIT PASSTHRU INCLUDEUPDATEBEFORES, PARAMS "{YOUR_HOME }/datahub-ogg-plugin/conf/javaue.properties" sourcedefs ./dirdef/ogg_test.def table OGG_TEST.*;
```

Add and start the writer process.

```bash
# Add the process
add extract dhwriter, exttrailsource ./dirdat/st
# Start the writer process
start dhwriter
```

**Examples**

**Log examples**

The source does not involve plugin logic, so this section only covers the two main types of logs on the target:

| log | directory of the plu |
|---|---|
| datahub-ogg-plugin.log |   |

troubleshoot plugin-related issues.

| ed in the | dirrpt | dir |
|---|---|---|
| {process name}.rpt _ |   |   |

2. OGG log: Located in the `dirrpt` directory. By default, each Replicat process has its own
log file named `{process_name}.rpt` , such as `DHWRITER.rpt` in this guide. You can refer to this log to troubleshoot OGG-related issues.

**Data example**

A successful write to DataHub generates the following log entry in the plugin log:

```
2020-12-01 11:29:30.000461 [record_writer-1-thread-1] INFO ShardWriter - Write DataHub success, table: orders, topic: orders_new, shard: 0, recordNum: 1, rt: 3
```

You can view a sample of the written data on the DataHub page:

```
Shard ID System Time oid (STRING) num (STRING) pid (STRING) b ak (STRING) ctype (STRING) ctime (STRING) cid (STRING) rowid (ST RING) 0 11:29:30 AM, Dec 1, 2020 1 3 2 z h I 2020-12-01 03:29:24.000074 16067933700000 AAAWwyAA GAAABufAAC
```

##### OGG for Big Data

1. . Environment requirements**
Oracle database: Oracle Database 19c or earlier. The version of the Oracle database cannot be later than that of the source database. Source database: Oracle GoldenGate (OGG) 19.1.0.0. Destination database: OGG for Big Data 19.1.0.0. Official download link of OGG

**Note: In this example, OGG 19.1.0.0 is used. For other supported versions, see the**

**version description at the end of this topic.**

2. . Installation**

**The following part describes how to configure Oracle, and install and configure**

**OGG. The parameter configurations used in this topic are only for your reference.**

**Use the configurations provided by the O&M engineers for actual business**

**operations.**

**Configure OGG in the source database**

In this example, Oracle Database 11g is used. For more information about Oracle Database 12c or later that supports multitenancy, see Installing Oracle GoldenGate Microservices.
1. . Configure Oracle in the source database**

**Note: If one of the following configurations is missed, the parameters may be left**

**unspecified before the update operation.** Run the following command to start SQL*Plus
as the database administrator: sqlplus / as sysdba. Then, complete the following configurations:

```bash
# Create a tablespace.
create tablespace ATMV datafile '/home/oracle/u01/app/oracle/oradata/uprr/ATMV.dbf' siz e 100m autoextend on next 50m maxsize unlimited;
 # Create a user named ogg_test. The password is also set to ogg_test.
create user ogg_test identified by ogg_test default tablespace ATMV;
 # Grant required permissions to the user ogg_test.
grant connect,resource,dba to ogg_test;
 # Check whether supplemental logging is enabled for the database.
Select SUPPLEMENTAL_LOG_DATA_MIN, SUPPLEMENTAL_LOG_DATA_PK, SUPPLEMENTAL_LOG_DATA_UI, S UPPLEMENTAL_LOG_DATA_FK, SUPPLEMENTAL_LOG_DATA_ALL from v$database;
 # If the result is NO, enable supplemental logging.
alter database add supplemental log data; alter database add supplemental log data (primary key, unique,foreign key) columns;
 # rollback
alter database drop supplemental log data (primary key, unique,foreign key) columns; alter database drop supplemental log data;
 # Enable logging for all fields at the database level. After this logging mode is enab
led, only primary key fields are logged for a delete operation. If you require informat ion about other fields, set the NOCOMPRESSDELETES parameter in the Extract process in t he source database. ALTER DATABASE ADD SUPPLEMENTAL LOG DATA (ALL) COLUMNS;
 # Enable force logging.
alter database force logging;
 # Enable the support for sequences.
@sequence.sql
```

`#`

```
alter table sys.seq$ add supplemental log data (primary key) columns;
```

2. . Install OGG in the source database**
Download and decompress the OGG installation package. The following directories are generated:

```
drwxr-xr-x install drwxrwxr-x response -rwxr-xr-x runInstaller drwxr-xr-x stage
```

Install dependencies in response/oggcore.rsp. The following template describes the OGG response file:

```bash
oracle.install.responseFileVersion=/oracle/install/rspfmt_ogginstall_response_schema_v12_
# The installation option, which indicates the installed Oracle version.
INSTALL_OPTION=ORA11g
# The directory in which OGG is to be installed.
SOFTWARE_LOCATION=/home/oracle/u01/ggate
# Specifies whether to start the Manager process after installation.
START_MANAGER=false
# The port number of the Manager process.
MANAGER_PORT=7839
# The directory of the Oracle database.
DATABASE_LOCATION=/home/oracle/u01/app/oracle/product/11.2.0/dbhome_1
# Optional. The directory that stores the inventory files.
INVENTORY_LOCATION=
# The UNIX group of the inventory directory. In this example, OGG is installed by using
the ogg_test Oracle account. You can also create a dedicated account for OGG as needed. UNIX_GROUP_NAME=oinstall
```

Run the following command to install OGG:

```
runInstaller -silent -responseFile {YOUR_OGG_INSTALL_FILE_PATH}/response/oggcore.rsp
```

In this example, OGG is installed in the /home/oracle/u01/ggate directory, and the installation logs are stored in the /home/oracle/u01/ggate/cfgtoollogs/oui directory. The OGG installation is complete when the following message appears in the silentInstall{time}.log file:

**Note**

The installation of Oracle GoldenGate Core was successful. Run the /home/oracle/u01/ggate/ggsci command and enter `CREATE SUBDIRS` as prompted to create OGG directories whose names start with dir. OGG is installed in the source database.
3. . Configure the Manager process in the source database**
The following part describes how to configure the Manager process in the source database by using Oracle GoldenGate Software Command Interface (GGSCI). You can run the `edit params` `mgr` command to configure the Manager process. The following code shows the configurations:

```
PORT 7839 DYNAMICPORTLIST 7840-7849 USERID ogg_test, PASSWORD ogg_test PURGEOLDEXTRACTS ./dirdat/*, USECHECKPOINTS, MINKEEPDAYS 7 LAGREPORTHOURS 1 LAGINFOMINUTES 30 LAGCRITICALMINUTES 45 PURGEDDLHISTORY MINKEEPDAYS 3, MAXKEEPDAYS 7 PURGEMARKERHISTORY MINKEEPDAYS 3, MAXKEEPDAYS 7
```

After the Manager process is configured, you can run the `view params mgr` command to verify the configurations. Run the `start mgr` command to start the Manager process. Run the `info mgr` command to view the status of the Manager process.
4. . Configure the Extract process in the source database.**
To configure the Extract process, create a configuration file. You can specify a custom file name. The file is named dhext in this example. In GGSCI, run the `edit params dhext` command to edit the Extract configuration file.

```
EXTRACT dhext SETENV (NLS_LANG="AMERICAN_AMERICA.AL32UTF8") DBOPTIONS ALLOWUNUSEDCOLUMN USERID ogg_test, PASSWORD ogg_test REPORTCOUNT EVERY 1 MINUTES, RATE NUMFILES 5000 DISCARDFILE ./dirrpt/ext_test.dsc, APPEND, MEGABYTES 100 DISCARDROLLOVER AT 2:00 WARNLONGTRANS 2h, CHECKINTERVAL 3m EXTTRAIL ./dirdat/st, MEGABYTES 200 DDL & INCLUDE MAPPED OBJTYPE 'table' & INCLUDE MAPPED OBJTYPE 'index' & INCLUDE MAPPED OBJTYPE 'SEQUENCE' & EXCLUDE OPTYPE COMMENT DDLOPTIONS NOCROSSRENAME REPORT TABLE OGG_TEST.*,tokens (TKN-ROWID=@GETENV('RECORD','rowid')); SEQUENCE OGG_TEST.*; GETUPDATEBEFORES
```

**Note:** The TABLE OGG_TEST.*,tokens (TKN-ROWID=@GETENV('RECORD','rowid')); command can
be used to obtain the row IDs in the source table. If you do not need to obtain the row IDs, use TABLE OGG_TEST.*; to replace rowid in the command. Add and start the Extract process.

```bash
# Add the Extract process.
add extract dhext,tranlog, begin now
# The maximum file size in each trail is 200 MB.
add exttrail ./dirdat/st,extract dhext, megabytes 200
# Start the Extract process.
start dhext
```

After the Extract process is started, you can view the changes to the database in the files stored in the ggate/dirdat directory.
5. . Configure a data pump in the source database**
Start GGSCI in the source database. In GGSCI, run the following command to configure a data pump: `edit params pump` .

```
EXTRACT pump RMTHOST xx.xx.xx.xx, MGRPORT 7839, COMPRESS PASSTHRU NUMFILES 5000 RMTTRAIL ./dirdat/st DYNAMICRESOLUTION TABLE OGG_TEST.*; SEQUENCE OGG_TEST.*;
```

Add and start a data pump.

```bash
# Add a data pump.
add extract pump,exttrailsource ./dirdat/st
# Add a trail in the destination database. The maximum file size in each trail is 200 M
```

`B.`

```bash
add rmttrail ./dirdat/st,extract pump,megabytes 200
# Before you start the data pump, make sure that the Manager process in the destination
database is started. start pump
```

After the data pump is started, you can view the delivered trail in the dirdat directory in the destination database.

**Configure OGG for Big Data in the destination database**

1. . Install OGG for Big Data in the destination database**
OGG in the destination database is OGG for Big Data and does not need to be manually installed. You need only to decompress the installation package. After the decompression, you must start GGSCI and enter the `create subdirs` command to create the required directories. After the create subdirs command is run, multiple directories whose names start with dir are created in the OGG directory.
2. . Install and configure the DataHub plug-in for OGG**
Environment requirement: Java Development Kit (JDK) 1.8 or later. Configure the JAVA_HOME and LD_LIBRARY_PATH environmental variables and specify the configurations in the ~/.bash_profile file. Example:

```
export JAVA_HOME=/xxx/xxx export JRE_HOME=/xxx/xxx/jrexx export LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:$JRE_HOME/lib/amd64:$JRE_HOME/lib/amd64/server
```

After the environment variables are configured, download and decompress the datahub-oggplugin.tar.gz package. Modify the javaue.properties file in the conf subdirectory of the installation directory and replace ${GG_HOME} with the path after decompression.

```
gg.handlerlist=ggdatahub gg.handler.ggdatahub.type=com.aliyun.odps.ogg.handler.datahub.DatahubHandler gg.handler.ggdatahub.configureFileName=${GG_HOME}/aliyun-datahub-oggplugin/conf/configure.xml goldengate.userexit.timestamp=utc+8 goldengate.userexit.writers=javawriter javawriter.stats.display=TRUE javawriter.stats.full=TRUE gg.includeggtokens=true gg.classpath=${GG_HOME}/aliyun-datahub-ogg-plugin/lib/* gg.log=log4j gg.log.level=info gg.log.file.count=64 gg.log.file.size=128MB javawriter.bootoptions=-Xms512m -Xmx512m -Xmn256m -Djava.class.path=ggjava/ggjava.jar - Dlog4j.configurationFile=${GG_HOME}/aliyun-datahub-ogg-plugin/conf/log4j.properties
```

Modify the configure.xml file in the conf subdirectory of the installation directory, as shown in the following code:

```xml
<?xml version="1.0" encoding="UTF-8"?> <configue>
    <defaultOracleConfigure>
        <!--Required. The Oracle database system identifier (SID).-->
        <sid>100</sid>
        <!--The schema of the Oracle table. The configuration can be overwritten by ora
cleSchema in the mappings. At least one of these two parameters must be specified.-->
        <schema>ogg_test</schema>
    </defaultOracleConfigure>
    <defalutDatahubConfigure>
        <!--Required. The endpoint of DataHub.-->
        <endPoint>YOUR_DATAHUB_ENDPOINT</endPoint>
        <!--The name of the DataHub project. The configuration can be overwritten by da
tahubProject in the mappings. At least one of these two parameters must be specified.--
```

`>`

```xml
        <project>YOUR_DATAHUB_PROJECT</project>
        <!--The AccessKey ID for accessing DataHub. The configuration can be
overwritten by datahubAccessId in the mappings. At least one of these two parameters mu st be specified.-->
        <accessId>YOUR_DATAHUB_ACCESS_ID</accessId>
        <!--The AccessKey Secret for accessing DataHub. The configuration can be overwr
itten by datahubAccessKey in the mappings. At least one of these two parameters must be specified.-->
        <accessKey>YOUR_DATAHUB_ACCESS_KEY</accessKey>
        <!--The field in DataHub that indicates the data update type. The configuration
can be overwritten by ctypeColumn in the mappings.-->
        <ctypeColumn>optype</ctypeColumn>
        <!--The field in DataHub that indicates the data update time. The configuration
canbeoverwrittenbyctimeColumninthemappings-->
```

```
can be overwritten by ctimeColumn in the mappings.
```

`>`

```xml
        <ctimeColumn>readtime</ctimeColumn>
        <!--The field in DataHub that indicates the sequence number of the updated reco
rd. The configuration can be overwritten by cidColumn in the mappings. The sequence num ber increases as more records are updated. Multiple sequence numbers may not be consecu tive.-->
        <cidColumn>record_id</cidColumn>
    </defalutDatahubConfigure>
    <!--The approach to handling errors. By default, if an error occurs, the system ign
ores the error and continues the operation or repeatedly retries the operation.-->
    <!--Optional. The maximum number of records that can be managed at a time. Default
value: 1000.-->
    <batchSize>1000</batchSize>
    <!--Optional. The format into which the timestamp is converted. Default value: yyyy
-MM-dd HH:mm:ss.-->
    <defaultDateFormat>yyyy-MM-dd HH:mm:ss</defaultDateFormat>
    <!--Optional. Specifies whether the system ignores dirty records. Default value: fa
lse.-->
    <dirtyDataContinue>true</dirtyDataContinue>
    <!--Optional. The name of the file that stores dirty records. Default value: datahu
b_ogg_plugin.dirty.-->
    <dirtyDataFile>datahub_ogg_plugin.dirty</dirtyDataFile>
    <!--Optional The maximum size of the file that stores dirty records. Unit: MB. Defa
ult value: 500.-->
    <dirtyDataFileMaxSize>200</dirtyDataFileMaxSize>
    <!--Optional. The maximum number of retries allowed. A value of -1 indicates unlimi
ted retries. A value of 0 indicates no retries. A value greater than 0 indicates the sp ecified number of retries.-->
    <retryTimes>0</retryTimes>
    <!--Optional. The IDs of the shards with higher priority into which data is to be w
ritten. Example: 0,1.-->
    <shardId>0,1</shardId>
    <!--Optional. The interval between two consecutive retries. Unit: milliseconds. Def
ault value: 3000.-->
    <retryInterval>4000</retryInterval>
    <!--Optional. The name of the checkpoint file. Default value:
datahub_ogg_plugin.chk.-->
    <checkPointFileName>datahub_ogg_plugin.chk</checkPointFileName>
    <mappings>
        <mapping>
            <!--The schema of the Oracle table. This parameter is described in the
preceding part.-->
            <oracleSchema></oracleSchema>
            <!--Required. The name of the Oracle table.-->
            <oracleTable>t_person</oracleTable>
            <!--The name of the DataHub project. This parameter is described in the
preceding part.-->
            <datahubProject></datahubProject>
            <!--Required. The name of the DataHub topic.-->
            <datahubTopic>t_person</datahubTopic>
            <!--Optional. The field in DataHub that indicates the rows in the source ta
ble.-->
            <rowIdColumn></rowIdColumn>
            <ctypeColumn></ctypeColumn>
            <ctimeColumn></ctimeColumn>
```

```xml
            <cidColumn></cidColumn>
            <columnMapping>
                <!--
                src: required. The field names in the Oracle table.
                dest: required. The field names in the DataHub topic.
                destOld: optional. The DataHub topic field that stores the data before
update.
                isShardColumn: optional. Specifies whether to generate the shard ID base
d on the hash key value. The configuration can be overwritten by the shardId parameter. Default value: false.
                isDateFormat: specifies whether to convert the timestamp into a string b
ased on the dateFormat parameter. Default value: true. If you set this parameter to fal se, the data type in the source database must be LONG.
                dateFormat: The format into which the timestamp is converted. If this pa
rameter is left empty, the default format is used.
                -->
                <column src="id" dest="id" isShardColumn="true"  isDateFormat="false" da
teFormat="yyyy-MM-dd HH:mm:ss"/>
                <column src="name" dest="name" isShardColumn="true"/>
                <column src="age" dest="age"/>
                <column src="address" dest="address"/>
                <column src="comments" dest="comments"/>
                <column src="sex" dest="sex"/>
                <column src="temp" dest="temp" destOld="temp1"/>
            </columnMapping>
        </mapping>
    </mappings>
</configue>
```

3. . Configure the Manager process in the destination database**

```
port 7919 dynamicportlist 7910-7919 lagreportminutes 10 laginfoseconds 1 purgeoldextracts ./dirdat/*, usecheckpoints, minkeepdays 7
```

Run the `start mgr` command to start the Manager process.
4. . Configure the Replicat process in the destination database**
In GGSCI, run the `edit params dhwt` command to modify the configurations.

```
REPLICAT dhwt getEnv (JAVA_HOME) getEnv (LD_LIBRARY_PATH) getEnv (PATH) TARGETDB LIBFILE libggjava.so SET property=${GG_HOME}/aliyun-datahub-oggplugin/conf/javaue.properties --You must manually modify the path. MAP ogg_test.*, TARGET ogg_test.*;
```

**In the preceding code, you must manually modify the path of the javaue.properties**

**file and specify specific table names for the MAP parameter. In this example, all**

**tables within the ogg_test account are collected.**

Add and start the dhwt process

```bash
# Add the dhwt process.
add replicat dhwt, exttrailsource dirdat/st
# Start the dhwt process.
start dhwt
```

3. . Examples**

**Sample logs**

Plug-ins are not involved in the source database. Logs in the destination database can be categorized into the following two types:
1. DataHub plug-in logs: By default, each Replicat process has a log in the dirrpt directory.
The log name is in the format of Process name-datahub.log. For example, the log name for the dhwt process is DHWT-datahub.log. You can resolve issues related to plug-ins based on this type of logs.
2. OGG-related logs: By default, each Replicat process has a log in the dirrpt directory. The log
name is in the format of Process name.log. For example, the log name for the dhwt process is DHWT.log. You can resolve issues related to OGG based on this type of logs.

**Sample record**

After the sample data is written to DataHub, the following record is generated in the DataHub plug-in log:

```
2020-12-01 11:29:30.000461 [record_writer-1-thread-1] INFO ShardWriter - Write DataHub success, table: orders, topic: orders_new, shard: 0, recordNum: 1, rt: 3
```

You can view the following sample record in the DataHub console:

```
Shard ID System Time oid (STRING) num (STRING) pid (STRING) bak (STRING) ctype (STRING) ctime (STRING) cid (STRING) rowid (STRING) 0 December 1, 2020 11:29:30 1 3 2 zh I 2020-12-01 03:29:24.000074 16067933700000 AAAWwyAAGAAABufAAC
```

#### OGG for MySQL

1. . Environment requirements**
MySQL Enterprise Edition or Community Edition is installed. Oracle GoldenGate (OGG) for MySQL 12.2.0.2 is installed. OGG Application Adapters 12.2.0.1 is installed. Java 7 is installed. We recommend that you install Java Development Kit (JDK) 1.8.
2. . Installation**

**The following part describes how to configure MySQL, and install and configure**

**Oracle GoldenGate (OGG). The parameter configurations used in this topic are only**

**for your reference. Use the configurations provided by the O&M engineers for**

**actual business operations.**

**Prepare the installation packages**

You can download the required installation packages by referring to the last section of this topic. OGG for MySQL OGG Application Adapters DataHub agent for OGG

**Configure OGG in the source database**

1. . Configure MySQL in the source database**

**Enable binary logging**

Modify the `/etc/my.cnf` file to add the following configurations.

```bash
## for ogg
# Extract expects that all of the table columns are in the binary log.
# As a result, only binlog_row_image set as full is supported and this is the default
binlog_row_image=full
# It must be set to the value of ROW, which directs the database to log DML statements
in binary format. binlog_format=row
# prevents DDL logging history table entries in the binlog
binlog-ignore-db=oggddl
# binlog path
log-bin=/usr/local/mysql/logs/log
# binlog index path
log-bin-index=/usr/local/mysql/logs/binlog.index
# enable binlog must set server-id, you can modify if there are multiple services
server-id=1
```

After the /etc/my.cnf file is modified, restart MySQL.

**Create a database and a user**

After you connect to MySQL, run the following commands to create a database and a user:

```bash
# Create a database named ggtt for OGG test.
create database ggtt;
## Create a user named ogg_test for OGG test.
grant all privileges on ggtt.* to 'ogg_test'@'localhost' identified by 'ogg_test'; flush privileges;
```

2. . Install OGG in the source database**
Decompress the OGG for MySQL installation package.
1. . Create the required directories**
Run the `./ggsci` command to start Oracle GoldenGate Software Command Interface (GGSCI) and enter the following command. **Unless otherwise specified, the commands in**
**the following parts need to be run in GGSCI**.

```
create subdirs
```

After the preceding command is run, multiple directories whose names start with `dir` are created in the OGG home directory.
3. . Configure the Manager process in the source database**
Run the `edit params mgr` command to configure the Manager process. The following code shows the configurations:

```
port 7839 dynamicportlist 7840-7849 purgeoldextracts /home/goldengate/dirdat/*,usecheckpoints, minkeepdays 2
```

After the Manager process is configured, you can run the `view params mgr` command to verify the configurations. Run the `start mgr` command to start the Manager process. Run the `info mgr` command to view the status of the Manager process.
4. . Configure the Extract process in the source database.**
Run the `edit params dhext` command to configure the Extract process. dhext is the process name. The process name can be customized, provided that it is the same as that in the configurations. This requirement is not described again in the following parts.

```
extract dhext sourcedb ggtt@localhost:3306 userid ogg_test password ogg_test exttrail dirdat/ms TranLogOptions AltLogDest /usr/local/mysql/logs/binlog.index table ggtt.*;
```

After the configurations are edited, save the configurations. Then, add and start the Extract process.

```bash
# Add the Extract process.
add extract dhext,tranlog,begin now
# The maximum file size in each trail is 200 MB.
add exttrail ./dirdat/ms,extract dhext, megabytes 200 start dhext
```

5. . Configure a data pump in the source database**
Run the `edit params pump` command to configure a data pump.

```
extract pump passthru -- enable compress rmthost localhost,mgrport 7839,compress rmttrail dirdat/ms table ggtt.*;
```

After the configurations are edited, save the configurations. Then, add the data pump.

```bash
# Add the data pump.
add extract pump,exttrailsource dirdat/ms
# Add a trail in the destination database. The maximum file size in each trail is 200 M
```

`B.`

```bash
add rmttrail dirdat/ms,extract pump,megabytes 200
# When you start the data pump, the destination database is connected. Therefore, you m
ust start the Manager process in the destination database before you start the data pum p. Otherwise, an error is reported. start pump
```

**Configure the destination database**

1. . Install OGG in the destination database**
OGG in the destination database is OGG Application Adapters and does not need to be manually installed. You need only to decompress the installation package. After the decompression, you must start GGSCI and enter the `create subdirs` command to create the required directories. After the create subdirs command is run, multiple directories whose names start with dir are created in the OGG directory.
2. . Install and configure the DataHub plug-in for OGG**
Environment requirement: JDK 1.7 or later. Configure the JAVA_HOME and LD_LIBRARY_PATH environmental variables and specify the configurations in the ~/.bash_profile file. Example:

```
export JAVA_HOME=/xxx/xxx export JRE_HOME=/xxx/xxx/jrexx export LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:$JRE_HOME/lib/amd64:$JRE_HOME/lib/amd64/server
```

After the environment variables are configured, decompress the datahub-ogg-plugin.tar.gz package. Modify the javaue.properties file in the conf subdirectory of the installation directory and replace {YOUR_HOME} with the path after decompression. Decompress the `datahub-ogg-plugin.tar.gz` package. Modify the javaue.properties file in the conf subdirectory of the installation directory and replace {YOUR_HOME} with the absolute path after decompression.

```
gg.handlerlist=ggdatahub gg.handler.ggdatahub.type=com.aliyun.odps.ogg.handler.datahub.DatahubHandler gg.handler.ggdatahub.configureFileName={YOUR_HOME}/aliyun-datahub-oggplugin/conf/configure.xml goldengate.userexit.nochkpt=false goldengate.userexit.timestamp=utc+8 gg.classpath={YOUR_HOME}/aliyun-datahub-ogg-plugin/lib/* gg.log.level=debug jvm.bootoptions=-Xmx512m -Dlog4j.configuration=file:{YOUR_HOME}/datahub-ogg-plugin/conf /log4j.properties -Djava.class.path=ggjava/ggjava.jar
```

Modify the log4j.properties file in the conf subdirectory of the installation directory and replace {YOUR_HOME} with the path after decompression.

```bash
log4j.rootLogger=INFO,fileout log4j.logger.com.goldengate=DEBUG log4j.logger.com.aliyun=DEBUG
# Console output...
log4j.appender.CONSOLE=org.apache.log4j.ConsoleAppender log4j.appender.CONSOLE.layout=org.apache.log4j.PatternLayout log4j.appender.CONSOLE.layout.ConversionPattern=%-4r [%t] %-5p %c %x - %m%n
# Rolling log file output...
log4j.appender.fileout=org.apache.log4j.RollingFileAppender log4j.appender.fileout.File={YOUR_HOME}/aliyun-datahub-ogg-plugin/log/datahub-ogg-plugi n.log log4j.appender.fileout.MaxFileSize=10000KB log4j.appender.fileout.MaxBackupIndex=30 log4j.appender.fileout.layout=org.apache.log4j.PatternLayout log4j.appender.fileout.layout.conversionPattern=%d{yyyy-MM-dd HH:mm:ss} [%t] %-5p %c{1}
- %m%n
```

Modify the configure.xml file in the conf subdirectory of the installation directory, as shown in the following code:

**Parameters to take note of**

`sid` : This parameter has no practical significance. You can set this parameter to an arbitrary value. `schema` and `oracleSchema` : the name of the MySQL database. In this example, set this parameter to ggtt. `oracleTable` : the name of the MySQL table. `rowIdColumn` : You cannot set this parameter because MySQL cannot obtain row IDs.

```xml
<?xml version="1.0" encoding="UTF-8"?> <configue>
    <defaultOracleConfigure>
        <!--Required. You can set this parameter to an arbitrary value.-->
        <sid>100</sid>
        <!--The name of the MySQL database. The configuration can be overwritten by ora
cleSchema in the mappings. At least one of these two parameters must be specified.-->
        <schema>ogg_test</schema>
    </defaultOracleConfigure>
    <defalutDatahubConfigure>
        <!--Required. The endpoint of DataHub.-->
        <endPoint>YOUR_DATAHUB_ENDPOINT</endPoint>
        <!--The name of the DataHub project. The configuration can be overwritten by da
tahubProject in the mappings. At least one of these two parameters must be specified.--
```

`>`

```xml
        <project>YOUR_DATAHUB_PROJECT</project>
        <!--The AccessKey ID for accessing DataHub. The configuration can be
overwritten by datahubAccessId in the mappings. At least one of these two parameters mu st be specified.-->
        <accessId>YOUR_DATAHUB_ACCESS_ID</accessId>
        <!--The AccessKey secret for accessing DataHub. The configuration can be overwr
itten by datahubAccessKey in the mappings. At least one of these two parameters must be
```

```xml
specified.-->
        <accessKey>YOUR_DATAHUB_ACCESS_KEY</accessKey>
        <!--The field in DataHub that indicates the data update type. The configuration
can be overwritten by ctypeColumn in the mappings.-->
        <ctypeColumn>optype</ctypeColumn>
        <!--The field in DataHub that indicates the data update time. The configuration
can be overwritten by ctimeColumn in the mappings.-->
        <ctimeColumn>readtime</ctimeColumn>
        <!--The field in DataHub that indicates the sequence number of the updated reco
rd. The configuration can be overwritten by cidColumn in the mappings. The sequence num ber increases as more records are updated. Multiple sequence numbers may not be consecu tive.-->
        <cidColumn>record_id</cidColumn>
    </defalutDatahubConfigure>
    <!--The approach to handling errors. By default, if an error occurs, the system ign
ores the error and continues the operation or repeatedly retries the operation.-->
    <!--Optional. The maximum number of records that can be managed at a time. Default
value: 1000.-->
    <batchSize>1000</batchSize>
    <!--Optional. The format into which the timestamp is converted. Default value: yyyy
-MM-dd HH:mm:ss.-->
    <defaultDateFormat>yyyy-MM-dd HH:mm:ss</defaultDateFormat>
    <!--Optional. Specifies whether the system ignores dirty records. Default value: fa
lse.-->
    <dirtyDataContinue>true</dirtyDataContinue>
    <!--Optional. The name of the file that stores dirty records. Default value: datahu
b_ogg_plugin.dirty.-->
    <dirtyDataFile>datahub_ogg_plugin.dirty</dirtyDataFile>
    <!--Optional The maximum size of the file that stores dirty records. Unit: MB. Defa
ult value: 500.-->
    <dirtyDataFileMaxSize>200</dirtyDataFileMaxSize>
    <!--Optional. The maximum number of retries allowed. A value of -1 indicates unlimi
ted retries. A value of 0 indicates no retries. A value greater than 0 indicates the sp ecified number of retries.-->
    <retryTimes>0</retryTimes>
    <!--Optional. The IDs of the shards with higher priority into which data is to be w
ritten. Example: 0,1.-->
    <shardId>0,1</shardId>
    <!--Optional. The interval between two consecutive retries. Unit: milliseconds. Def
ault value: 3000.-->
    <retryInterval>4000</retryInterval>
    <!--Optional. The name of the checkpoint file. Default value:
datahub_ogg_plugin.chk.-->
    <checkPointFileName>datahub_ogg_plugin.chk</checkPointFileName>
    <mappings>
        <mapping>
            <! --The name of the MySQL database. This parameter is described in the
preceding part.-->
            <oracleSchema></oracleSchema>
            <!--Required. The name of the MySQL table.-->
            <oracleTable>t_person</oracleTable>
            <!--The name of the DataHub project. This parameter is described in the
preceding part.-->
            <datahubProject></datahubProject>
```

<!

```
Reqired ThenameoftheDataHbtopic
```

`>`

```xml
            <!--Required. The name of the DataHub topic.-->
            <datahubTopic>t_person</datahubTopic>
            <ctypeColumn></ctypeColumn>
            <ctimeColumn></ctimeColumn>
            <cidColumn></cidColumn>
            <columnMapping>
                <!--
                src: required. The field names in the Oracle table.
                dest: required. The field names in the DataHub topic.
                destOld: optional. The DataHub topic field that stores the data before
update.
                isShardColumn: optional. Specifies whether to generate the shard ID base
d on the hash key value. The configuration can be overwritten by the shardId parameter. Default value: false.
                isDateFormat: specifies whether to convert the timestamp into a string b
ased on the dateFormat parameter. Default value: true. If you set this parameter to fal se, the data type in the source database must be LONG.
                dateFormat: The format into which the timestamp is converted. If this pa
rameter is left empty, the default format is used.
                -->
                <column src="id" dest="id" isShardColumn="true"  isDateFormat="false" da
teFormat="yyyy-MM-dd HH:mm:ss"/>
                <column src="name" dest="name" isShardColumn="true"/>
                <column src="age" dest="age"/>
                <column src="address" dest="address"/>
                <column src="comments" dest="comments"/>
                <column src="sex" dest="sex"/>
                <column src="temp" dest="temp" destOld="temp1"/>
            </columnMapping>
        </mapping>
    </mappings>
</configue>
```

3. . Configure the Manager process in the destination database**
Run the `edit params mgr` command to configure the Manager process.

```
port 7839 dynamicportlist 7840-7849 purgeoldextracts dirdat/*,usecheckpoints, minkeepdays 7
```

Run the `start mgr` command to start the Manager process.
4. . Configure the Extract process in the destination writer**
Run the `edit params dhwriter` command to configure the Extract process.

```
extract dhwriter getEnv (JAVA_HOME) getEnv (LD_LIBRARY_PATH) getEnv (PATH) CUSEREXIT libggjava_ue.so CUSEREXIT PASSTHRU INCLUDEUPDATEBEFORES, PARAMS "{YOUR_HOME}/ datahub-ogg-plugin/conf/javaue.properties" GetUpdateBefores table ggtt.*;
```

After the configurations are edited, save the configurations. Then, add and start the Extract process.

```bash
# Add the Extract process.
add extract dhwriter, exttrailsource dirdat/ms
# Start the Extract process.
start dhwriter
```

3. . Mappings between data types of fields in MySQL and**
The unit of field values of the TIMESTAMP type in DataHub is microseconds. When you map field values of the DATETIME or TIMESTAMP type in MySQL, the values are converted into timestamps in microseconds.

| MySQL | DataHub | Description |
|---|---|---|
| CHAR and VARCHAR | STRING |   |
| INT, TINYINT, and BIG INT | BIGINT |   |
| DECIMAL, FLOAT, and DOUBLE | DOUBLE or DECIMAL | The data type is selected based on the required accuracy. |
| DATETIME and TIMESTAMP | TIMESTAMP |   |
| TEXT and TINYTEXT | STRING |   |

The preceding table describes the mappings between common data types in MySQL and DataHub. For more information about the data types supported by MySQL, see 1.3.5 Supported MySQL Data Types.
4. . Installation packages**
Only the download links of the DataHub plug-in for OGG are provided in this topic. To download OGG for MySQL and OGG Application Adapters, see Oracle GoldenGate Downloads and Oracle Software Delivery Cloud.

| datahub-ogg-plugin | OGG for MySQL | OGG Adapter | Supported MySQL version |
|---|---|---|---|
| 2.0.3 | 12.2.0.2 | 12.2.0.1 | Enterprise Edition and Community Edition |
| 2.0.4 | 12.2.0.2 | 12.2.0.1 | Enterprise Edition and Community Edition |
| 2.0.5 | 12.2.0.2 | 12.2.0.1 | Enterprise Edition and Community Edition |

#### OGG for Big Data (Kafka)

Oracle GoldenGate (OGG) for Big Data streams Oracle database changes to big data systems in real time, and supports Oracle Database 19c and earlier. Because DataHub is compatible with the Kafka Producer protocol, you can write Oracle data directly to DataHub over the DataHub Kafka interface using OGG for Big Data — without a dedicated DataHub plugin.

**Environment requirements**

Oracle database: any version supported by the latest OGG release. OGG in the source database: version must be equal to or later than the Oracle database version. Use the latest OGG release when possible. OGG for Big Data in the destination database: version must be equal to or later than the OGG version in the source database. Use the latest OGG for Big Data release when possible. Official download link for OGG.

**Installation**

The following sections describe how to configure Oracle and install and configure OGG. The parameter configurations shown here are for reference only. For production deployments, use the configurations provided by your operations and maintenance (O&M) engineers.

**Configure OGG in the source database**

For installation instructions, see Installing Oracle GoldenGate. If your source database is Oracle Database 11g, you can also refer to the OGG for Oracle documentation.

**Configure OGG for Big Data in the destination database**

1. . Install OGG for Big Data**
OGG for Big Data does not require a traditional installation — decompress the installation package to get started. After decompression, start Oracle GoldenGate Software Command Interface (GGSCI) and run the `create subdirs` command to initialize the required directory structure. This creates multiple directories prefixed with `dir` under the OGG root directory.
2. . Set Kafka-related parameters**
Three configuration files control how OGG for Big Data connects to DataHub and formats the outgoing data.

**a. Configure the custom_kafka_producer.properties file.**

This file sets Kafka Producer parameters. Edit `custom_kafka_producer.properties` in the `dirprm` directory (create the file if it does not exist). For a full parameter reference, see Documentation.

```bash
# The endpoint of Kafka. In the following example, the endpoint in the China (Hangzhou)
region is used. You can modify the value as required. bootstrap.servers=dh-cn-hangzhou.aliyuncs.com:9092 value.serializer=org.apache.kafka.common.serialization.ByteArraySerializer key.serializer=org.apache.kafka.common.serialization.ByteArraySerializer
# Tune the parameter settings. You can modify the parameters as required or use the def
ault values.
# compression.type=lz4
# batch.size=1024000
# max.request.size=41943040
# message.max.bytes=41943040
# linger.ms=5000
# reconnect.backoff.ms=1000
# By default, the Kafka interface of DataHub uses the SASL_SSL protocol for data transf
er. The following code shows required configurations: security.protocol=SASL_SSL sasl.mechanism=PLAIN
```

**b. Configure the kafka_client_producer_jaas.conf file.**

This file holds the AccessKey pair used to authenticate with DataHub. Create `kafka_client_producer_jaas.conf` in the `dirprm` directory and add the following content:

```
KafkaClient {
    org.apache.kafka.common.security.plain.PlainLoginModule required
    username="accessId"
    password="accessKey";
```

};

**c. Configure the kafka.props file.**

This file specifies the target Kafka topic, data format, and logging behavior. Edit `kafka.props` in the `dirprm` directory (create the file if it does not exist). For parameter details, see Using Oracle GoldenGate for Big Data.

```bash
gg.handlerlist = kafkahandler gg.handler.kafkahandler.type = kafka gg.handler.kafkahandler.KafkaProducerConfigFile=custom_kafka_producer.properties
# The Kafka topic to which data is to be written.
gg.handler.kafkahandler.TopicName =kafka_topic_name gg.handler.kafkahandler.format =json gg.handler.kafkahandler.mode=op gg.handler.kafkahandler.format.includeCurrentTimestamp=false gg.handler.kafkahandler.BlockingSend =true
# The token contains the information about row IDs and the token information that you s
pecify. gg.handler.kafkahandler.includeTokens=true
# Use the UPDATE statement to update a primary key.
gg.handler.kafkahandler.format.pkUpdateHandling =update
#gg.handler.kafkahandler.format.pkUpdateHandling =delete-insert
goldengate.userexit.timestamp=utc goldengate.userexit.writers=javawriter javawriter.stats.display=TRUE javawriter.stats.full=TRUE goldengate.userexit.nochkpt=FALSE gg.log=log4j gg.log.level=INFO gg.report.time=120sec
###Kafka Classpath settings ###
gg.classpath=/xxx/lib/kafka/libs/* javawriter.bootoptions=-Xmx512m -Xms32m -Djava.class.path=ggjava/ggjava.jar -Djava.secu rity.auth.login.config=dirprm/kafka_client_producer_jaas.conf
```

Note: Do not set the `gg.handler.kafkahandler.SchemaTopicName` parameter. This parameter requires the Kafka Consumer protocol, which DataHub does not support. The `java.security.auth.login.config` parameter is required. OGG for Big Data fails to start if this parameter is missing.
3. . Configure the Manager process**
Run the `edit params mgr` command to open the Manager process configuration.

```
PORT 7809 DYNAMICPORTLIST 7810-7909 AUTORESTART EXTRACT *,RETRIES 5,WAITMINUTES 3 PURGEOLDEXTRACTS ./dirdat/*,USECHECKPOINTS, MINKEEPDAYS 3
```

Then run `start mgr` to start the Manager process.
4. . Configure the Replicat process**

| run the | edit params mqkafka |   |
|---|---|---|
| mqkafka |   |   |
|   |   | is the process name |

In GGSCI, run the `edit params mqkafka` command to configure the Replicat process. In this

```
REPLICAT mqkafka TARGETDB LIBFILE libggjava.so SET property=dirprm/kafka.props REPORTCOUNT EVERY 1 MINUTES, RATE GROUPTRANSOPS 10000 --MAP QASOURCE.*, TARGET QASOURCE.*; MAP ogg_test.*, TARGET ogg_test.*;
```

Before adding and starting the Replicat process, create a DataHub topic. The Kafka interface cannot create topics — they must exist beforehand. Use a BLOB-type topic when possible. For details on creating topics, see Kafka compatibility.

```bash
# Add the mqkafka process.
add replicat mqkafka, exttrail ./dirdat/st
# Start the mqkafka process.
start mqkafka
```

**Examples**

Data written to DataHub through the Kafka interface has no schema. After synchronization to MaxCompute, write user-defined functions (UDFs) to parse the data. The following example shows the `JSON` -format data written to DataHub.
1. . Schema of an Oracle table**

```
  SQL> desc orders
   Name                                      Null?    Type
   ----------------------------------------- -------- ----------------------------
   OID                                                NUMBER(38)
   PID                                                VARCHAR2(511)
   NUM                                                VARCHAR2(511)
```

2. . Schema of a DataHub topic**
This example uses a TUPLE-type topic with two STRING fields to demonstrate the data format. For production use, a BLOB-type topic is recommended — TUPLE topics may cause errors when the data contains binary content. `{`

```json
    "fields":[
```

`{`

```json
            "name":"key",
            "type":"STRING"
```

`},` `{`

```json
            "name":"val",
            "type":"STRING"
```

`}` `]` `}`
3. . Write data**

**a. Run an SQL script.**

```
declare i number; op_num number; begin
          op_num := 1;
          for i in 1..op_num loop
        insert into orders(oid,pid,num) values(i,i+1,i+2);
      end loop;
      for i in 1..op_num loop
        update orders set pid=i*2+1 where oid=i;
      end loop;
      for i in 1..op_num loop
        delete from orders where oid=i;
      end loop;
          commit;
end;
```

**b. Check the logs.**

After the table is configured and the Replicat process is running, the following entry appears in `dirrpt/MQKAFKA_info_log4j.log` , confirming that the JSON schema for `OGG_TEST.ORDERS` was generated:

```
INFO 2020-05-29 20:23:55,069 [main] Creating JSON schema for table OGG_TEST.ORDERS in f ile ./dirdef/OGG_TEST.ORDERS.schema.json
```

The generated `dirdef/OGG_TEST.ORDERS.schema.json` file:

```
$cat dirdef/OGG_TEST.ORDERS.schema.json
```

`{`

```json
    "$schema":"http://json-schema.org/draft-04/schema#",
    "title":"OGG_TEST.ORDERS",
    "description":"JSON schema for table OGG_TEST.ORDERS",
    "definitions":{
        "row":{
            "type":"object",
            "properties":{
                "OID":{
                    "type":[
                        "string",
                        "null"
```

`]` `},`

```json
                "PID":{
                    "type":[
                        "string",
                        "null"
```

`]` `},`

```json
                "NUM":{
                    "type":[
```

```
type:[
                        "string",
                        "null"
```

`]` `}` `},`

```json
            "additionalProperties":false
```

`},`

```json
        "tokens":{
            "type":"object",
            "description":"Token keys and values are free form key value pairs.",
            "properties":{
```

`},`

```json
            "additionalProperties":true
```

`}` `},`

```json
    "type":"object",
    "properties":{
        "table":{
            "description":"The fully qualified table name",
            "type":"string"
```

`},`

```json
        "op_type":{
            "description":"The operation type",
            "type":"string"
```

`},`

```json
        "op_ts":{
            "description":"The operation timestamp",
            "type":"string"
```

`},`

```json
        "current_ts":{
            "description":"The current processing timestamp",
            "type":"string"
```

`},`

```json
        "pos":{
            "description":"The position of the operation in the data source",
            "type":"string"
```

`},`

```json
        "tokens":{
            "$ref":"#/definitions/tokens"
```

`},`

```json
        "before":{
            "$ref":"#/definitions/row"
```

`},`

```json
        "after":{
            "$ref":"#/definitions/row"
```

`}` `},`

```json
    "required":[
        "table",
        "op_type",
        "op_ts",
        "current_ts",
        "pos"
```

`],`

```json
    "additionalProperties":false
```

`}`

**c. Sample the data.**

After the SQL script runs, the three operations (INSERT, UPDATE, DELETE) are written to DataHub. Sample and view the data in the DataHub console. Each record carries an `op_type` field ( `I` , `U` , or `D` ) that identifies the operation, along with `before` and `after` row snapshots where applicable:

```json
Shard ID System Time key (STRING) val (STRING) 0 May 29, 2020 18:01:38 OGG_TEST.ORDERS {"table":"OGG_TEST.ORDERS","op_type":"I","op_ts":"2020-05-29 10:01:27.000067","current_ts":"2020-05- 29T18:01:33.062000","pos":"00000002790849451348","after": {"OID":"1","PID":"2","NUM":"3"}} 0 May 29, 2020 18:01:38 OGG_TEST.ORDERS {"table":"OGG_TEST.ORDERS","op_type":"U","op_ts":"2020-05-29 10:01:27.000067","current_ts":"2020-05- 29T18:01:33.064000","pos":"00000002790849451514","before": {"OID":"1","PID":"2","NUM":"3"},"after":{"OID":"1","PID":"3","NUM":"3"}} 0 May 29, 2020 18:01:38 OGG_TEST.ORDERS {"table":"OGG_TEST.ORDERS","op_type":"D","op_ts":"2020-05-29 10:01:27.000067","current_ts":"2020-05- 29T18:01:33.064001","pos":"00000002790849451685","before": {"OID":"1","PID":"3","NUM":"3"}}
```

## Data synchronization

### Overview

DataHub allows you to synchronize data to Apsara Stack services in real time or near real time, including MaxCompute, ApsaraDB RDS, and Object Storage Service (OSS). During data synchronization, you need to pay attention to the network configuration and the duplicate record issue. This topic describes the usage notes for the data synchronization feature of DataHub.

**Data synchronization**

The data synchronization feature of DataHub allows you to add data sources or data sinks to synchronize data. You can synchronize data from a topic to other Apsara Stack services in `real time or near real time` . This feature supports the following Apsara Stack services: MaxCompute, AnalyticDB for MySQL, ApsaraDB RDS, Tablestore, OSS, and Elasticsearch. You need to write data to DataHub only once. Then, you can create DataConnectors to synchronize the data to these services.

**Supported Apsara Stack services**

**Important**

When you create a DataConnector to synchronize data from DataHub to MaxCompute, a batch is synchronized every 5 minutes or when the data volume reaches 64 MB. When you create a DataConnector to synchronize data from DataHub to Tablestore, OSS, Elasticsearch, or Hologres, a batch is synchronized every 20 seconds or when the data volume reaches 4 MB. When you create a DataConnector to synchronize data from DataHub to ApsaraDB for MySQL, ApsaraDB RDS, or AnalyticDB for MySQL V3.0, a batch is synchronized every 20 seconds or when the data volume reaches 512 KB.

| Destination service | Supported data type of topics | Timeliness | Support for VPC |
|---|---|---|---|
| MaxCompute | TUPLE / BLOB | Near real time with a latency of 5 minutes | No |
| Hologres | TUPLE | Real time | No |
| ADS 3.0 | TUPLE | Real time | No |
| AnalyticDB for MySQL | TUPLE | Real time | No |
| ApsaraDB RDS | TUPLE | Real time | Yes |
| Tablestore | TUPLE | Real time | No |

| User Guide·Data synchron | ization |   | DataHu |
|---|---|---|---|

| OSS | TUPLE / BLOB | Real time | No |
|---|---|---|---|
| ElasticSearch | TUPLE | Real time | Yes |

**Usage notes**

We recommend that you synchronize data between Apsara Stack services in the same region. This eliminates the need to configure cross-region network connectivity and reduces the network latency. Due to the network isolation of Apsara Stack, you must specify the internal endpoint of an Apsara Stack service when you configure data synchronization for the Apsara Stack service. Public endpoints are not supported. DataHub supports only the at-least-once mechanism for data synchronization. This mechanism may cause a small number of duplicate records in the destination service in certain scenarios, such as a scenario in which a network error occurs. In this case, you must delete the duplicate records. When you create a DataConnector, DataHub automatically associates a subscription ID with the DataConnector to record the offset from which DataHub starts to read data. The recorded offset differs from the offset from which synchronization starts. Do not change the subscription ID. Only the owner and creator of a topic can create DataConnectors for the topic.

### Synchronize data to

**MaxCompute**

This topic describes how to synchronize data from DataHub to a MaxCompute table. It covers steps such as table creation, account configuration, partition settings, and synchronization task configuration.

**Preparations**

**Create a MaxCompute table**

DataHub allows you to synchronize data to MaxCompute tables. Both partitioned and nonpartitioned tables are supported. To facilitate data processing in MaxCompute, we recommend that you synchronize data to partitioned tables. DataHub allows you to synchronize data from the topics of the TUPLE or BLOB type to MaxCompute tables. If you want to synchronize data from topics of the TUPLE type, data types in MaxCompute tables must match data types in the DataHub topics. The following table describes the data type mappings.

| MaxCompute | DataHub |
|---|---|
| BIGINT | BIGINT |

| STRING | STRING |
|---|---|
| BOOLEAN | BOOLEAN |
| DOUBLE | DOUBLE |
| DATETIME | TIMESTAMP |
| DECIMAL | DECIMAL |
| TINYINT | TINIINT |
| SMALLINT | SMALLINT |
| INT | INTEGER |
| FLOAT | FLOAT |
| MAP | Not supported |
| ARRAY | Not supported |

DataHub does not support all data types in MaxCompute. We recommend that you create a MaxCompute schema based on the data types supported by DataHub. If you want to synchronize data of the BLOB type from topics, the MaxCompute schema needs to contain only one field of the STRING type. By default, DataHub synchronizes data to this field.

| DataHub | MaxCompute |
|---|---|
| BLOB | STRING |

To facilitate data tracking and troubleshooting, we recommend that you add the `__rowkey__` field of the STRING type when you create a MaxCompute schema. DataHub automatically synchronizes the trace information of the synchronized data in DataHub to this field to facilitate subsequent data troubleshooting.

**Prepare an account granted the required permissions for data**

**synchronization**

When you create a DataConnector to synchronize data from DataHub to MaxCompute, you must manually enter the information about the account that is used to access the MaxCompute table. Make sure that the entered account information is valid. In most cases, you can use a Resource Access Management (RAM) user for MaxCompute. You must grant the account the required permissions on the MaxCompute table. The permissions include the `CreateInstance` , `Describe` , `Alter` , and `Update` permissions. You can manage the permissions on MaxCompute tables in the DataWorks console. For more information, see Configure MaxCompute engine permissions. You can also use the command-line tool of MaxCompute for authorization. For more information, see MaxCompute permissions.Configure MaxCompute engine permissions

**Determine the value of the Timestamp Unit parameter**

The Timestamp Unit parameter specifies the unit in which the data of the TIMESTAMP type is converted and written to the fields of the DATETIME type in MaxCompute. If you want the fields of the TIMESTAMP type to be written to MaxCompute in the unit of seconds, select SECOND from the Timestamp Unit drop-down list when you create a DataConnector. If you want the fields of the TIMESTAMP type to be written to MaxCompute in the unit of milliseconds, select MILLISECOND from the Timestamp Unit drop-down list. If you want the fields of the TIMESTAMP type to be written to MaxCompute in the unit of microseconds, select MICROSECOND from the Timestamp Unit drop-down list.

**Check whether DataHub needs to be added to the service**

**whitelist of MaxCompute**

MaxCompute supports IP address whitelist for projects. If you configure an IP address whitelist for MaxCompute projects but the IP address of DataHub is not added to the whitelist, DataHub cannot synchronize data to MaxCompute. To resolve this issue, you can add DataHub to the service whitelist of MaxCompute. Then, DataHub can synchronize data to MaxCompute. The service name that DataHub registers with MaxCompute is **DataHub**. You can use a MaxCompute SDK or odpscmd to add DataHub to the service whitelist. Use a MaxCompute SDK

```java
public static void setServiceName() throws OdpsException {
    String endpoint = "";
    String project = "";
    String accessId = "";
    String accessKey = "";
    Account account = new AliyunAccount(accessId, accessKey);
    Odps odps = new Odps(account);
    odps.setEndpoint(endpoint);
    odps.setDefaultProject(project);
    Map<String, String> prop = new HashMap<>();
    // Add the name of the DataHub service to the service whitelist of MaxCompute. Se
parate multiple names with commas (,). The latest setting overwrites the previous set ting.
    prop.put("odps.security.ip.whitelist.services", "DataHub");
    Group group = new Groups(odps).get("groupName");
    group.updateProject(project, null, null, prop);
    // Check whether the service whitelist of MaxCompute meets your expectations.
    prop = odps.projects().get(project).getAllProperties();
    System.out.println("current service list: " +
prop.get("odps.security.ip.whitelist.services"));
```

`}` Use odpscmd Start odpscmd and run the setproject odps.security.ip.whitelist.services=DataHub; command to add DataHub to the service whitelist of MaxCompute. Then, you can run the setproject; command to check whether DataHub is added to the whitelist. If `odps.security.ip.whitelist.services=DataHub` is returned, DataHub is added.

**Usage notes**

More partitions cause slower data synchronization from DataHub due to the current writing standards of MaxCompute. When you create a DataConnector to synchronize data to MaxCompute, we recommend that you limit the number of partitions, especially in `USER_DEFINE` mode. Make sure that the timestamps of the records in a shard and the shards are as continuous as possible. Make sure that the partition configurations do not result in excessive partitions.

**Create a DataConnector**

1. Log in to the DataHub console.
2. In the left-side navigation pane, click **Projects**.
3. On the **Projects** page, find the project that you want to manage and click its name to go to
the project details page.
4. On the **Topic List** tab, find the topic that you want to manage and click its name to go to
the topic details page.
5. On the topic details page, click **+ Connector** in the upper-right corner.
6. In the **Create Connector** panel, click **MaxCompute**. Then, configure the parameters and
click **Create**. Key parameters: Import Fields: DataHub synchronizes the values of the specified fields from the DataHub topic to the MaxCompute table. Partition Mode: This parameter specifies the MaxCompute partition to which data is written. The following table describes the partition modes supported by DataHub.

| Partition mode | Partition basis | Supported data type of a topic | Description |
|---|---|---|---|

| USER DEFINE _ | Value of the partition field that has the same name as the partition field in MaxCompute in the record | TUPLE | The schema of the topic must contain the partition field in MaxCompute. The value of this field must be a UTF-8 string . The value of this field can be empty, which indicates that the data is not partitioned. |
|---|---|---|---|
| SYSTEM TIME _ | Time when the record is written to DataHub | TUPLE / BLOB | You must set the Partition Config parameter to specify the format to which timestamps are converted for time- based partitioning in MaxCompute. You must set the Timezone parameter to specify a time zone. |
| EVENT TIME _ | Value of the event time(TIMEST _ AMP) field in the record | TUPLE | You must set the Partition Config parameter to specify the format to which timestamps are converted for time- based partitioning in MaxCompute. You must set the Timezone parameter to specify a time zone. |
| META TIME _ | Value of the dh meta time __ _ _ __ field in the record | TUPLE / BLOB | You must set the Partition Config parameter to specify the format to which timestamps are converted for time- based partitioning in MaxCompute. You must set the Timezone parameter to specify a time zone. |

|   |   | event time(TIMEST _ | TU |
|---|---|---|---|
| NT TIME _ | AMP) |   |   |

|   |   | dh meta time __ _ _ __ |
|---|---|---|
| _ |   |   |

In `SYSTEM_TIME` , `EVENT_TIME` , or `META_TIME` mode, data is synchronized to different partitions in the destination MaxCompute table based on the timestamps and the specified time zone. By default, the timestamps are in microseconds. The Partition Config parameter specifies the configurations that are used to convert timestamps to implement time-based partitioning in the destination MaxCompute table. The following table describes the default MaxCompute time formats that are supported in the DataHub console.

| Partition | Time format | Description |
|---|---|---|
| ds | %Y%m%d | day |
| hh | %H | hour |
| mm | %M | minute |

The Time Range parameter specifies the time range of the partitions generated in the destination MaxCompute table. Valid values: `15 to 1440` . Unit: minutes. The step size is `15` minutes. The Timezone parameter specifies the time zone used to implement time-based partitioning. If you synchronize data of the BLOB type to MaxCompute, you can use hexadecimal delimiters to split the data before synchronization. For example, you can set the Split Key parameter to `0A` , which indicates line feeds (\n) . By default, topics whose data type is BLOB store binary data. However, such data is mapped to columns of the STRING type in MaxCompute. Therefore, Base64 encoding is automatically enabled when you create a DataConnector in the DataHub console. If you want to customize your DataConnectors, use an SDK.

**View a DataConnector**

You can view the details of a DataConnector, such as the status and synchronization offset, and restart or stop the DataConnector on the details page of the DataConnector, as shown in the following figure.

**Examples**

**USER_DEFINE mode**

1. Create a DataHub topic.
The schema of the topic must contain the partition fields in MaxCompute, and the fields are of the STRING type, as shown in the following figure.
2. Write data to the DataHub topic. You can use a DataHub SDK to write the data.
During the test, a DataHub SDK is used to write several records, where [ds,hh,mm] are [20210304,01,15] and [20210304,02,15]. The following figure shows the records.
3. Create a DataConnector.
In USER_DEFINE mode, you can configure the partition fields when you create a DataConnector. If no available MaxCompute table exists, a MaxCompute table is automatically created. In this example, the f1 and f2 fields are to be imported. The f3 field is not synchronized.
4. Verify the synchronized data.
You can view the synchronization information of the DataConnector in the DataHub console. Query data in the MaxCompute table. The following figure shows the query result. In USER_DEFINE mode, DataHub synchronizes data to the corresponding partition based on the value of the partition field in MaxCompute.

**SYSTEM_TIME mode**

1. Create a DataHub topic.
The partition to which data is written is determined based on the time when data is written to DataHub. Therefore, the topic schema needs to contain only data fields and does not need to contain partition fields, as shown in the following figure.
2. Write data to the DataHub topic. You can use a DataHub SDK to write the data.
During the test, a DataHub SDK is used to write multiple records. The time when the data is written to DataHub is `2021-03-04 14:02:45` . The following figure shows the records.
3. Create a DataConnector.

**Important**

The partition configurations must be the same as those of the MaxCompute table.
4. Verify the synchronized data.
You can view the synchronization information of the DataConnector in the DataHub console, such as DoneTime. Query data in the MaxCompute table. The following figure shows the query result. In SYSTEM_TIME mode, DataHub synchronizes data to the corresponding partition based on the time when data was written to DataHub.

**FAQ**

Question: What do I do if the timestamp for data synchronization to MaxCompute changes to 1970-01-19? Cause: The default unit of the timestamp for data synchronization from DataHub to MaxCompute is microseconds, and the unit of the timestamp when data was written to DataHub is milliseconds. Solution: Specify microseconds as the unit of the timestamp when data is written to DataHub.

### Synchronize data to Hologres

This topic describes how to synchronize data from DataHub to a Hologres instance to implement real-time data synchronization and management. It covers the preparations, data type mapping, and parameter configuration.

**Preparations**

**Create a Hologres instance and a table in the instance in the**

**Hologres console.**

DataHub synchronizes data based on the mappings between the data types of fields in DataHub and those in Hologres. The following table describes the data type mappings between DataHub and Hologres.

| DataHub | Hologres |
|---|---|
| TINYINT | SMALLINT |
| SMALLINT | SMALLINT |
| INTERGER | INTERGER |
| BIGINT | BIGINT |
| FLOAT | REAL |
| DOUBLE | DOUBLE PRECISION |
| DECIMAL | DECIMAL |
| STRING | TEXT |
| BOOLEAN | BOOLEAN |
| TIMESTAMP | TIMESTAMPTZ |

**Note**

The `TINYINT` , `SMALLINT` , `INTEGER` , and `FLOAT` data types in DataHub are supported by Hologres V2.0 and later.

**Create a DataConnector**

1. Log in to the DataHub console.
2. In the left-side navigation pane, click **Projects**.
3. On the **Projects** page, find the project that you want to manage and click its name to go to
the project details page.
4. On the **Topic List** tab, find the topic that you want to manage and click its name to go to
the topic details page.
5. On the topic details page, click
in the upper-right corner.
6. In the **Create Connector** panel, click **Hologres**. Then, configure the parameters and click
**Create**.

**Note**

You can synchronize data to partitioned tables in Hologres. If you specify a partitioned table when you create a DataConnector, data is automatically synchronized to the partitions based on the partition key.

| Parameter | Description |
|---|---|
| Instance | The ID of the Hologres instance. To view the ID of the Hologres instance, you can log in to the Hologres console and click Instances in the left-side navigation pane. |
| Database | The name of the Hologres database. |
| Table | The name of the Hologres table to which you want to write data. |

| Primary Key Conflict Policy | The primary key conflict policy that is used when data is written from DataHub to a Hologres table with a primary key. Valid values: replace: If a primary key conflict occurs when you write data, the original data is overwritten by the new data. ignore: If a primary key conflict occurs when you write data, new data is ignored. The data is not updated, and original data is retained. |
|---|---|
| Synchronization Scenarios | The mode in which data is synchronized from DataHub to Hologres. Valid values: default: Records are written from DataHub to Hologres one by one. dts old: New naming rules are disabled for additional _ columns. dts: New naming rules are enabled for additional columns. |
| Import Fields | The fields that you want to synchronize to Hologres. You can synchronize all or partial fields of the DataHub topic based on your business requirements. |
| Authentication Mode | The mode in which access to the Hologres instance is authenticated. Default value: AccessKey. |
| AccessKey ID | The AccessKey ID used to access the Hologres instance. To obtain the AccessKey ID, choose Enterprise > Resources > Organizations in the Apsara Uni-manager Management Console. On the Organizations page, select a level-1 organization and click Manage AccessKey Pairs in the Basic Information section to view the AccessKey ID. |
| AccessKey Secret | The AccessKey secret used to access the Hologres instance. To obtain the AccessKey secret, choose Enterprise > Resources > Organizations in the Apsara Uni-manager Management Console. On the Organizations page, select a level-1 organization and click Manage AccessKey Pairs in the Basic Information section to view the AccessKey secret. |
| Start Time | The time when DataHub starts to synchronize data to Hologres. |
| Timestamp Unit | The unit of time that is used to synchronize data from Hologres. The Timestamp Unit parameter specifies the unit in which the data of the TIMESTAMP type is converted and written to the fields of the DATETIME type in Hologres. |

**Note**

The `dts` and `dts_old` synchronization modes are applicable to scenarios in which data is synchronized to DataHub by using Data Transmission Service (DTS) and then synchronized from DataHub to Hologres. For more information about the new and original additional columns, see Synchronize data from DataHub.
7. Click the **Synchronization Task** tab to view the status of data synchronization from
DataHub to Hologres.
8. View the data that is synchronized to Hologres in real time.
Connect the Hologres instance to a development tool and use the tool to query the data synchronized to the Hologres instance in real time. For more information about development tools, see Development tools. Sample statement:

```
SELECT COUNT(*) FROM lineitem;
```

**FAQ**

**What do I do if the following error is reported when I create a DataConnector?**

```
 ErrorCode=NoPermission; ErrorMessage=Rejected by IP whitelist
```

**Solution**: Hologres allows you to configure IP address whitelists to manage access in the
HoloWeb console. If the preceding error is reported, check whether an IP address whitelist is configured in the HoloWeb console.

### Synchronize data to

**AnalyticDB for MySQL**

This topic describes how to synchronize data from topics of the TUPLE type to AnalyticDB for MySQL. You can select the IGNORE or OVERWRITE write mode for a synchronization task to achieve efficient data transmission.

**Preparations**

Create an AnalyticDB for MySQL cluster and a table in the cluster in the AnalyticDB for MySQL console. DataHub synchronizes data based on the mappings between the data types of fields in DataHub and those in AnalyticDB for MySQL. The following table describes the data type mappings between DataHub and AnalyticDB for MySQL.

| DataHub | AnalyticDB for MySQL |
|---|---|
| TINYINT | TINYINT |

| SMALLINT | SMALLINT |
|---|---|
| INTEGER | INT |
| BIGINT | BIGINT |
| STRING | VARCHAR |
| BOOLEAN | BOOLEAN / TINYINT |
| FLOAT | FLOAT |
| DOUBLE | DOUBLE |
| TIMESTAMP | TIMESTAMP / BIGINT |
| DECIMAL | DECIMAL |

The TINYINT, SMALLINT, INTEGER, and FLOAT data types in DataHub are supported by DataHub SDK for Java V2.16.1-public and later.

**Usage notes**

DataHub allows you to synchronize data from only topics of the TUPLE type to AnalyticDB for MySQL. OVERWRITE and IGNORE modes: In OVERWRITE mode, the REPLACE INTO statement is executed to insert data into the database. In IGNORE mode, the INSERT IGNORE INTO statement is executed to insert data into the database. The REPLACE INTO statement overwrites the data when a primary key conflict occurs, and the INSERT IGNORE INTO statement ignores conflicts and writes data to the database. A normal latency of data synchronization is in seconds. In other words, data is synchronized to AnalyticDB for MySQL within several seconds after the data is written to DataHub. Network exceptions may cause duplicate data updates. However, this ensures that data is synchronized at least once. The write performance of AnalyticDB for MySQL affects the synchronization performance. If the performance of an AnalyticDB for MySQL cluster does not meet the expectations, the synchronization rate may be slow, and data may be accumulated. In extreme cases, data may be lost because the synchronization latency exceeds the lifecycle.

**Create a DataConnector.**

1. Log in to the DataHub console.
2. In the left-side navigation pane, click **Projects**.
3. On the **Projects** page, find the project that you want to manage and click its name to go to
the project details page.
4. On the **Topic List** tab, find the topic that you want to manage and click its name to go to
the topic details page.
5. On the topic details page, click **Connector** in the upper-right corner.
6. In the **Create Connector** panel, click **ADS**, configure the parameters, and then click
**Create**.
The following section describes the key parameters that are used to create a DataConnector in the DataHub console. To create a DataConnector in a more flexible manner, use an SDK. Host: the endpoint of AnalyticDB for MySQL. To ensure that your cluster can be connected, you must enter an `internal endpoint` . Import Fields: the fields to be synchronized to AnalyticDB for MySQL. You can synchronize all or partial fields of the DataHub topic to AnalyticDB for MySQL based on your business requirements. Write Mode: the mode in which data is written. Valid values: IGNORE: ignores duplicate data. The `INSERT IGNORE INTO` statement is executed to write data. OVERWRITE: updates duplicate data. The `REPLACE INTO` statement is executed to write data.

**Example**

1. Create an AnalyticDB for MySQL cluster and a table in the AnalyticDB for MySQL console.
2. Create a DataHub topic.
In this example, a topic of the TUPLE type is created. The following figure shows the schema details of the created topic.
3. Create a DataConnector. In the Create Connector panel, select IGNORE from the Write
Mode drop-down list and all fields from the Import Fields drop-down list.
4. Write data of the TUPLE type to the created topic. The following figure shows the written
data. In this example, four records are written.
5. Connect to AnalyticDB for MySQL on the client and check whether the data is synchronized
to AnalyticDB for MySQL. The following figure shows the synchronized data.

### Synchronize data to

**Elasticsearch**

This topic describes how to create a DataConnector in DataHub to synchronize data to an Elasticsearch cluster. This topic covers the preparations, procedure, parameters, and examples.

**Preparations**

1. Create an index in Elasticsearch.
DataHub allows you to synchronize data to indexes in Elasticsearch 5.X, 6.X, and 7.X. DataHub allows you to synchronize data from only topics of the TUPLE type to Elasticsearch. Before you start a DataConnector, make sure that an index is created in Elasticsearch, or indexes can be automatically created. Otherwise, the DataConnector may fail.
2. Prepare an account that is granted required permissions for data synchronization.
When you create a DataConnector to synchronize data from DataHub to Elasticsearch, you must manually enter information used to access Elasticsearch, such as the endpoint, index name, account, and password. Make sure that the entered account information is authentic and valid. Otherwise, the DataConnector fails to be created.

**Create a DataConnector**

1. Log in to the DataHub console.
2. In the left-side navigation pane, click **Projects**.
3. On the **Projects** page, find the project that you want to manage and click its name to go to
the project details page.
4. On the **Topic List** tab, find the topic that you want to manage and click its name to go to
the topic details page.
5. On the topic details page, click **Connector** in the upper-right corner.
6. In the **Create Connector** panel, click **Elasticsearch**, configure the parameters, and then
click **Create**. Parameters:
**Endpoint:** the endpoint of Elasticsearch. You must enter an internal endpoint and an
internal port in the format of `Internal endpoint:Internal port` . For example, if the internal endpoint is `es-cn-xxx.elasticsearch.aliyuncs.com` and the internal port is `9200` , you must enter `es-cn-xxx.elasticsearch.aliyuncs.com:9200` .
**Index:** You can specify a static index or dynamic index.
Static index: If you create an index in advance or allow Elasticsearch to automatically create an index, all data is written to the index. Dynamic index: You must allow Elasticsearch to automatically create indexes. Otherwise, data fails to be written. You can allow Elasticsearch to generate indexes based on a time period or a field. Indexes can be generated based on only one field. Supported time formats

| Year | Month | Day | Week |
|---|---|---|---|
| %Y | %m | %d | %U |

Example 1: Create an index every morning

| test ${%Y-%m-%d} _ | . If the c |
|---|---|
| ritten is |   |

Example 2: Create indexes based on a field To create indexes based on the `col1` field, set the Index parameter to test_${col1} . If a record whose value in the col1 field is `AAA` and a record whose

| BBB | exist |
|---|---|

value in the col1 field is `BBB` exist, the two records are written to different indexes. The former is written to `test_AAA` and the latter is written to `test_BBB` .

**Important**

When the number of indexes in an Elasticsearch cluster increases, the data write slows down. Excessive indexes may cause timeout errors when DataHub writes data to Elasticsearch. Therefore, when you use dynamic indexes, you must prevent excessive indexes.
**User and Password:** the username and password that are used to access Elasticsearch.
**Type Fields:** The types that are generated during data synchronization from DataHub to
Elasticsearch vary with the version of Elasticsearch clusters. In a cluster of Elasticsearch V5.X, you can create multiple types in one index. However, in a cluster of Elasticsearch V6.X, you can create only one type in one index. Therefore, the way in which DataHub synchronizes data to Elasticsearch varies. The Type Fields parameter is required. When you create a DataConnector to synchronize data from DataHub to a cluster of Elasticsearch V5.X, the value of the field that you select is used as the type of a record. If multiple fields are selected, the values of the fields are concatenated by using vertical bars (|) and then used as the type of a record. The fields that you select from the Type Fields drop-down list cannot be null. When you create a DataConnector to synchronize data from DataHub to a cluster of Elasticsearch V6.X, the name of the field that you select is used as the type of a record. If multiple fields are selected, the names of the fields are concatenated by using vertical bars (|) and then used as the type of a record. The cluster of Elasticsearch V6.X supports custom values as the type of a record. Example:

```
DataHub Schema : f1 string, f2 string, f3 string, f4 string Data: ["test1","test2","test3",null]
```

| Type field | Type in Elasticsearch V5.X | Type in Elasticsearch V6.X |
|---|---|---|

| f1 | test1 | f1 |
|---|---|---|
| f1,f3 | test1 | test3 |
| ff | The type failed to be created. | ff |
| f1,ff | The type failed to be created. | f1\|ff |
| f4 | The type is created but the data failed to be synchronized. Dirty data occurs. | The type is created and the data is synchronized. |

**Important**

The type name cannot be customized when you create a DataConnector to synchronize data to a cluster of Elasticsearch V6.X in the DataHub console. If you want to customize the type name, you can use DataHub SDKs to create a DataConnector. Default types are used in a cluster of Elasticsearch V7.X. Therefore, you do not need to set the Type Fields parameter when you create a DataConnector to synchronize data to a cluster of Elasticsearch V7.X.
**ID Fields:** You can generate IDs for the data written to Elasticsearch based on the data
written to DataHub. You can also select no ID fields. In this case, Elasticsearch generates a unique ID for each record. When you create a DataConnector to synchronize data from DataHub to Elasticsearch, the value of the field that you select is used as the ID of a record. If multiple fields are selected, the values of the fields are concatenated by using vertical bars (|) and then used as the ID of a record. The fields that you select from the ID Fields drop-down list cannot be null. Example:

```
DataHub Schema : f1 string, f2 string, f3 string, f4 string Data: ["test1","test2","test3",null]
```

| ID field | Data ID |
|---|---|
|   | Elasticsearch automatically generates a unique ID for each record. |
| f1 | test1 |
| f1,f3 | test1\|test3 |
| ff | The ID failed to be created. |

| f4 | The ID is generated but the record failed to be synchronized. Dirty data occurs. |
|---|---|

**Router Fields:** You can generate routers for the data written to Elasticsearch based on
the data written to DataHub. You can also select no router fields. In this case, the router feature of Elasticsearch is not used. When you create a DataConnector to synchronize data from DataHub to Elasticsearch, the value of the field that you select is used as the router of a record. If multiple fields are selected, the values of the fields are concatenated by using vertical bars (|) and then used as the router of a record. The fields that you select from the Router Fields drop-down list cannot be null. For more information about examples, see the description of the `ID Fields` parameter.
**Import Fields:** the fields to be imported from DataHub to Elasticsearch. Fields that are
not selected are not synchronized from DataHub to Elasticsearch. Fields that are used as IDs and types in a cluster of Elasticsearch V5.X cannot be selected as the fields to be imported. No examples are provided because the fields to be imported do not completely determine the finally generated data. The following section provides a complete data synchronization example.
**Proxy Mode**: the proxy mode. Set this parameter based on your business requirements.
**Network Type:** the network type. Set this parameter based on the type of the
Elasticsearch cluster.

|   | Important You must append -worker to the ID of an Elasticsearch cluster when you set the Instance ID parameter. For example, if the ID of an Elasticsearch cluster is es-cn- xxx , you must enter es-cn-xxx-worker in the Instance ID field. |
|---|---|
|   | xxx |

**VPC ID**: You can view the VPC ID in the Elasticsearch console.
**Instance ID**: You can view the ID of the Elasticsearch cluster in the Elasticsearch
console.
**Start Time:** Select a time range based on your business requirement.

**Data write example**

In this example, the DataConnector is successfully created. If the DataConnector fails to be created, modify the configurations based on the preceding parameter description.

**The following table describes a topic schema in DataHub.**

| Field | Data type |
|---|---|
| f1 | BIGINT |
| f2 | STRING |
| f3 | BOOLEAN |
| f4 | DOUBLE |

| f5 | TIMESTAMP |
|---|---|
| f6 | DECIMAL |

**Example 1:**

Type Fields = f1 (This parameter is unavailable when you create a DataConnector to synchronize data from DataHub to a cluster of Elasticsearch V7.X.) ID Fields = f2 Import Fields = f1,f2,f3,f4,f5,f6

**Data = v1,v2,v3,v4,v5,v6**

| Elasticsearch version | Type | ID |   | Data |   |   |
|---|---|---|---|---|---|---|
| Elasticsearch V5.X | v1 | v2 |   | {f3:v3,f4:v4,f5:v5 ,f6:v6} |   |   |
| Elasticsearch V6.X | f1 | v2 |   | {f1:v1,f3:v3,f4:v4 ,f5:v5,f6:v6} |   |   |
|   |   |   |   |   | {f1:v1,f3:v3,f4:v4 |   |
|   |   |   |   | ,f5:v5,f6:v6} |   |   |
| Elasticsearch V7.X | - | v2 |   | {f1:v1,f3:v3,f4:v4 ,f5:v5,f6:v6} |   |   |
|   |   |   |   |   | {f1:v1,f3:v3,f4:v4 |   |
|   |   |   |   | ,f5:v5,f6:v6} |   |   |

|   |   | {f3:v3,f4:v4,f5:v5 |   |
|---|---|---|---|
|   | ,f6:v6} |   |   |

**Data = null,v2,v3,v4,v5,v6**

| Elasticsearch version | Type | ID |   | Data |   |   |
|---|---|---|---|---|---|---|
| Elasticsearch V5.X | - | - |   | Dirty data occurs because the type field is null. |   |   |
| Elasticsearch V6.X | f1 | v2 |   | {f1:v1,f3:v3,f4:v4 ,f5:v5,f6:v6} |   |   |
|   |   |   |   |   | {f1:v1,f3:v3,f4:v4 |   |
|   |   |   |   | ,f5:v5,f6:v6} |   |   |
| Elasticsearch V7.X | - | v2 |   | {f1:v1,f3:v3,f4:v4 ,f5:v5,f6:v6} |   |   |
|   |   |   |   |   | {f1:v1,f3:v3,f4:v4 |   |
|   |   |   |   | ,f5:v5,f6:v6} |   |   |

**Data = v1,null,v3,v4,v5,v6**

| Elasticsearch version | Type | ID | Data |
|---|---|---|---|

| Elasticsearch V5.X | - | - | Dirty data occurs because the ID field is null. |
|---|---|---|---|
| Elasticsearch V6.X | - | - | Dirty data occurs because the ID field is null. |
| Elasticsearch V7.X | - | - | Dirty data occurs because the ID field is null. |

**Example 2:**

Type Fields = f1,f2 (This parameter is unavailable when you create a DataConnector to synchronize data from DataHub to a cluster of Elasticsearch V7.X.) ID Fields = f3,f4 Import Fields = f1,f2,f3,f4,f5,f6

**Data = v1,v2,v3,v4,v5,v6**

| Elasticsearch version | Type | ID | Data |
|---|---|---|---|
| Elasticsearch V7.X | v1\|v2 | v3\|v4 | {f5:v5,f6,v6} |
| Elasticsearch V6.X | f1\|f2 | v3\|v4 | {f1:v1,f2:v2,f5:v5,f6:v 6} |
| Elasticsearch V7.X | - | v3\|v4 | {f1:v1,f2:v2,f5:v5,f6:v 6} |

**Data = v1,null,v3,v4,v5,v6**

| Elasticsearch version | Type | ID | Data |
|---|---|---|---|
| Elasticsearch V5.X | - | - | Dirty data occurs because the type field is null. |
| Elasticsearch V6.X | f1\|f2 | v3\|v4 | {f1:v1,f2:v2,f5:v5,f6:v 6} |
| Elasticsearch V7.X | - | v3\|v4 | {f1:v1,f2:v2,f5:v5,f6:v 6} |

**Data = v1,v2,null,v4,v5,v6**

| Elasticsearch version | Type | ID | Data |
|---|---|---|---|
| Elasticsearch V5.X | - | - | Dirty data occurs because the ID field is null. |
| Elasticsearch V6.X | - | - | Dirty data occurs because the ID field is null. |
| Elasticsearch V7.X | - | - | Dirty data occurs because the ID field is null. |

**Example 3:**

Type Fields = f1 (This parameter is unavailable when you create a DataConnector to synchronize data from DataHub to a cluster of Elasticsearch V7.X.) ID Fields = f2 Router Fields = f3 Import Fields = f1,f2,f3,f4,f5,f6

**Data = v1,v2,v3,v4,v5,v6**

| Elasticsearch version | Type | ID | Router |   | Data |   |   |
|---|---|---|---|---|---|---|---|
| Elasticsearch V5.X | v1 | v2 | v3 |   | {f4:v4,f5:v5, f6:v6} |   |   |
| Elasticsearch V6.X | f1 | v2 | v3 |   | {f1:v1,f4:v4, f5:v5,f6:v6} |   |   |
|   |   |   |   |   |   | {f1:v1,f4:v4, |   |
|   |   |   |   |   | f5:v5,f6:v6} |   |   |
| Elasticsearch V7.X | - | v2 | v3 |   | {f1:v1,f4:v4, f5:v5,f6:v6} |   |   |
|   |   |   |   |   |   | {f1:v1,f4:v4, |   |
|   |   |   |   |   | f5:v5,f6:v6} |   |   |

|   |   | {f4:v4,f5:v5, |   |
|---|---|---|---|
|   | f6:v6} |   |   |

**Data = null,v2,v3,v4,v5,v6**

| Elasticsearch version | Type | ID | Data |
|---|---|---|---|
| Elasticsearch V5.X | - | - | Dirty data occurs because the type field is null. |

| Elasticsearch V6.X | f1 | v2 |   | {f1:v1,f4:v4,f5:v5 ,f6:v6} |   |   |
|---|---|---|---|---|---|---|
|   |   |   |   |   | {f1:v1,f4:v4,f5:v5 |   |
|   |   |   |   | ,f6:v6} |   |   |
| Elasticsearch V7.X | - | v2 |   | {f1:v1,f4:v4,f5:v5 ,f6:v6} |   |   |
|   |   |   |   |   | {f1:v1,f4:v4,f5:v5 |   |
|   |   |   |   | ,f6:v6} |   |   |

**Data = v1,null,v3,v4,v5,v6**

| Elasticsearch version | Type | ID | Data |
|---|---|---|---|
| Elasticsearch V5.X | - | - | Dirty data occurs because the ID field is null. |
| Elasticsearch V6.X | - | - | Dirty data occurs because the ID field is null. |
| Elasticsearch V7.X | - | - | Dirty data occurs because the ID field is null. |

**Data = v1,v2,null,v4,v5,v6**

| Elasticsearch version | Type | ID | Data |
|---|---|---|---|
| Elasticsearch V5.X | - | - | Dirty data occurs because the router field is null. |
| Elasticsearch V6.X | - | - | Dirty data occurs because the router field is null. |
| Elasticsearch V7.X | - | - | Dirty data occurs because the router field is null. |

**View a DataConnector**

On the details page of a DataConnector, view the information about the DataConnector, such as the status and synchronization offset. You can also restart and stop the DataConnector. To reset the DataConnector, stop the DataConnector first.

**Example**

This example shows the procedure for synchronizing data from DataHub to Elasticsearch V7.10. All operations related to Elasticsearch are performed by using **the development**
**tools provided in the Kibana console**. For more information about other operations, see
Elasticsearch documentation.
1. Create an index in Elasticsearch.
By default, Elasticsearch can automatically create an index. Therefore, you can skip this step. If you do not allow Elasticsearch to automatically create an index, you must manually create an index. For more information about how to create an index, see Elasticsearch documentation.
2. Create a DataHub topic.

**Important**

DataHub allows you to synchronize data from only topics of the TUPLE type to Elasticsearch. For more information, see Create a topic. After the topic is created, view the topic.
3. Create a DataConnector to synchronize data to Elasticsearch.
In this example, f1 and f2 are used as the type fields, f3 and f4 as the ID fields, and all fields as the fields to be imported.
4. Write data to the DataHub topic.
You can use a DataHub SDK or a DataHub plug-in to write data to the DataHub topic. After a record is written, sample the data and view the written data.
5. Verify the synchronized data.
First, check the synchronization offset of the DataConnector that is used to synchronize data to Elasticsearch. The synchronization offset and synchronization time of the DataConnector have changed. The synchronization time is the time when the data is written to DataHub, and the synchronization offset has changed to 1. The synchronization offset starts from 0, and an offset of 0 indicates that the first record is written. Then, check whether data is synchronized to Elasticsearch. You can view the synchronized data in the Kibana console.

### Synchronize data to OSS

This topic describes how to create a DataConnector in DataHub to synchronize data from topics of the TUPLE or BLOB type to OSS. It covers the preparations, usage notes, procedure, and synchronization example. You can use this feature to achieve efficient data storage and management.

**Preparations**

Create an OSS bucket. DataHub allows you to synchronize data to OSS. Before you create a DataConnector to synchronize data from DataHub to OSS, you must create a bucket in the OSS console to receive data. Create a service-linked role for DataHub. When you create a DataConnector, you can authenticate the access to an OSS bucket by

|   | AccessKey pair |
|---|---|
| Token Service (STS) |   |

using the `AccessKey pair` of an account or a temporary access credential from `Security` `Token Service (STS)` . If you use a temporary access credential from STS, the service-linked role for DataHub is automatically created. Then, DataHub uses the service-linked role to synchronize data to OSS.

**Usage notes**

You can synchronize data from topics of the TUPLE and BLOB types in DataHub to OSS. Data in topics of the TUPLE type is in the CSV format. Columns in each record are separated by commas (,). Records are separated by line feeds (\n) . Data in topics of the BLOB type is appended to existing data. If you want to split OSS data, you must use delimiters to separate the DataHub data to be synchronized. The name of the file that is synchronized to OSS is composed of meaningful information such as `ConnectorId` . You cannot modify the name of the file. A secondary directory is generated based on the time when data is written to DataHub.

**Create a DataConnector**

1. Log in to the DataHub console.
2. In the left-side navigation pane, click **Projects**.
3. On the **Projects** page, find the project that you want to manage and click its name to go to
the project details page.
4. On the **Topic List** tab, find the topic that you want to manage and click its name to go to
the topic details page.
5. On the topic details page, click
in the upper-right corner.
6. In the **Create Connector** panel, click **Object Storage Service**. Then, configure the
parameters and click **Create**. The following table describes the parameters.

| Parameter | Description |
|---|---|
| Endpoint | The endpoint of OSS. We recommend that you enter the classic network endpoint and include the port number if needed. You can access OSS only over HTTP instead of HTTPS if you use an internal network. |
| Bucket | The name of the OSS bucket. |

| Directory Prefix | The name prefix of the directory in the OSS bucket. |
|---|---|
| Time Range | The time range of level-2 directories. Valid values: 15 to 1440. Uni: minutes. Default value: 15. |
| Time Format | The time format. Default value: %Y%m%d%H%M . |
| Import Fields | The fields to be synchronized to the OSS bucket. You can synchronize all or partial fields of the DataHub topic based on your settings. The fields that you can select are based on the latest version of the topic schema. |
| Authentication Mode | The mode in which the access to the OSS bucket is authenticated. Valid values: AccessKey STS If you set the Authentication Mode parameter to AccessKey, you must enter an AccessKey ID and an AccessKey secret. |
| Start Time | The time when DataHub starts to synchronize data from DataHub to OSS. |

**Example**

1. Create a bucket in the OSS console to receive data.
For more information, see **Create a bucket** in the **OSS User Guide**. The following figure shows the details page of an OSS bucket.
2. Create a DataHub topic.
In this example, a topic of the TUPLE type is created. The following figure shows the schema details of a topic.
3. Create a DataConnector.
4. Write data to the topic of the TUPLE type. The following figure shows the written data.
5. Verify the synchronized data
The following figure shows the path of a synchronized file in OSS. The path contains the names of the OSS bucket, top-level directory, secondary directory, and file. Download the file and view the file content. The data that is synchronized from the TUPLE topic is in the CSV format. The following figure shows the file content.

### Synchronize data to

**Tablestore**

This topic describes how to synchronize data from DataHub to Tablestore. It covers the preparations, usage notes, and procedure to help you correctly configure parameters to implement data synchronization.

**Preparations**

The related information about Tablestore is obtained, including the endpoint of Tablestore, a Tablestore instance that is created, and a table that is created in the Tablestore instance. The owner or creator account of a DataHub topic is obtained. Only the owner or creator account of the DataHub topic has the permissions to manage DataConnectors, including creating and deleting DataConnectors.

**Usage notes**

The primary key columns of the Tablestore table must have a one-to-one mapping with the fields in the DataHub topic. The order of the fields can be different. Field names in DataHub are case-insensitive. If the name of a primary key in the Tablestore table contains uppercase letters, these uppercase letters are converted to lowercase letters in the name of the mapped field in the DataHub topic. You can synchronize only data in topics of the TUPLE type to a Tablestore table. You can write up to 200 rows of data to Tablestore at a time. The following table lists the data type mappings.

| OTS | DataHub |
|---|---|
| INTEGER | TINYINT |
| INTEGER | SMALLINT |
| INTEGER | INTEGER |
| INTEGER | BIGINT |
| INTEGER | TIMESTAMP |
| DOUBLE | FLOAT |
| DOUBLE | DOUBLE |
| BOOLEAN | BOOLEEAN |
| STRING | STRING |
| STRING | DECIMAL |
| BINARY | Not supported |

If you use a temporary access credential from Security Token Service (STS), the servicelinked role for DataHub is automatically created. Then, DataHub uses the service-linked role to synchronize data to Tablestore.

**Create a DataConnector to synchronize data to Tablestore**

1. Log in to the DataHub console.
2. In the left-side navigation pane, click **Projects**.
3. On the **Projects** page, find the project that you want to manage and click its name to go to
the project details page.
4. On the **Topic List** tab, find the topic that you want to manage and click its name to go to
the topic details page.
5. On the details page of a topic, click **Connector** in the upper-right corner.
6. In the **Create Connector** panel, click **Tablestore**. Then, configure the parameters and
click **Create**. The following table describes the parameters.

| Parameter | Description |
|---|---|
| Endpoint | The internal endpoint of Tablestore. |
| Instance | The name of the Tablestore instance. |
| Table | The Tablestore table to which data is synchronized. |

| Write Mode | The following modes are supported: PUT: inserts data into the specified row. If the row exists, the existing data is overwritten. Otherwise, a new row is added. UPDATE: updates the data of a specific row. If the row does not exist, a new row is added. If the row exists, the values of the specified columns are added, modified, or deleted based on the request content. |
|---|---|
| Import Fields | The fields to be synchronized to Tablestore. You can synchronize all or partial fields of the DataHub topic based on your settings. The fields that you can select are based on the latest version of the topic schema. |
| Authentication Mode | The following two modes are supported. Default value: STS. AccessKey STS If you set the Authentication Mode parameter to AccessKey, you must enter an AccessKey ID and an AccessKey secret. |
| Start Time | The time when DataHub starts to synchronize data to Tablestore. |

7. After the synchronization task is created, click **View** on the **Synchronization Task** tab of
the topic details page to view the details of the synchronization task.

### Synchronize data to ApsaraDB

**RDS and ApsaraDB RDS for MySQL**

This topic describes how to synchronize data from DataHub to ApsaraDB RDS and ApsaraDB RDS for MySQL. It covers the preparations, usage notes, procedure, and synchronization examples. This topic guides users on how to configure key parameters to ensure effective data synchronization.

**Synchronize data to ApsaraDB RDS**

**Preparations**

Create an ApsaraDB RDS instance and a table in the instance. Create an ApsaraDB RDS instance and then a table in the instance in the ApsaraDB RDS console. You can create the ApsaraDB RDS instance in the classic network or a virtual private cloud (VPC). When you create a DataConnector, you must select the same network type as that of the ApsaraDB RDS instance. DataHub synchronizes data based on the mappings between the data types of fields in DataHub and those in ApsaraDB RDS. The following table describes the data type mappings between DataHub and ApsaraDB RDS.

| DataHub | ApsaraDB RDS |
|---|---|
| TINYINT | TINYINT |
| SMALLINT | SMALLINT |
| INTEGER | INT |
| BIGINT | BIGINT |
| STRING | VARCHAR |
| BOOLEAN | BOOLEAN / TINYINT |
| FLOAT | FLOAT |
| DOUBLE | DOUBLE |
| TIMESTAMP | TIMESTAMP / BIGINT |
| DECIMAL | DECIMAL |

The TINYINT, SMALLINT, INTEGER, and FLOAT data types in DataHub are supported by DataHub SDK for Java V2.16.1-public and later.

**Usage notes**

DataHub allows you to synchronize data from only topics of the TUPLE type to ApsaraDB RDS. By default, the timestamp in DataHub is converted to the timestamp in ApsaraDB RDS based on the microsecond precision. Take note of the data precision. To prevent lock contention caused by concurrent reads and writes on the data of the same primary key, you must write data of the same primary key to the same shard.

**Create a DataConnector**

1. Log in to the DataHub console.
2. In the left-side navigation pane, click **Projects**.
3. On the **Projects** page, find the project that you want to manage and click its name to go to
the project details page.
4. On the **Topic List** tab, find the topic that you want to manage and click its name to go to
the topic details page.
5. On the details page of the topic, click **Connector** in the upper-right corner.
6. In the **Create Connector** panel, click **RDS & MySQL**, configure the parameters, and then
click **Create**. The following section describes key parameters that are used to create a DataConnector in the DataHub console. To create a DataConnector in a more flexible manner, use an SDK.

| Parameter | Description |
|---|---|
| Host | The endpoint of ApsaraDB RDS. To ensure that your instance can be connected, you must enter an internal endpoint . |
| Write Mode | The mode in which data is written. Valid values: IGNORE: ignores duplicate data. The INSERT IGNORE INTO statement is executed to write data. OVERWRITE: updates duplicate data. The REPLACE INTO statement is executed to write data. |

| DataHub | User Guide·Data synchronizatio |
|---|---|

| Import Fields | The fields to be synchronized to ApsaraDB RDS. You can synchronize all or partial fields of the DataHub topic based on your business requirements. |
|---|---|
| VPC ID | The ID of the VPC in which the ApsaraDB RDS instance resides. You can view the VPC ID in the ApsaraDB RDS console. |
| Instance ID | The ID of the ApsaraDB RDS instance. If your ApsaraDB RDS instance resides in a VPC, you must set the Instance ID parameter. You can view the instance ID in the ApsaraDB RDS console. |

**Example**

1. Create an ApsaraDB RDS instance and a table in the instance in the ApsaraDB RDS console.
2. Create a DataHub topic. In this example, a topic of the TUPLE type is created. The following
figure shows the schema details of the topic.
3. Create a DataConnector. In this example, IGNORE is selected as Write Mode and all fields
are selected for the Import Fields parameter.
4. Write data of the TUPLE type to the created topic. The following figure shows the written
data. In this example, four records are written to the topic.
5. Verify the synchronized data. In this example, a MySQL client is used to connect to
ApsaraDB RDS to view the synchronized data. The following figure shows the synchronized data.

**Synchronize data to ApsaraDB RDS for MySQL**

**Preparations**

Create an ApsaraDB RDS for MySQL instance and a table in the instance in the ApsaraDB RDS console. DataHub synchronizes data based on the mappings between the data types of fields in DataHub and those in ApsaraDB RDS for MySQL. The following table describes the data type mappings between DataHub and ApsaraDB RDS for MySQL.

| DataHub | AnalyticDB for MySQL |
|---|---|
| TINYINT | TINYINT |
| SMALLINT | SMALLINT |

| INTEGER | INT |
|---|---|
| BIGINT | BIGINT |
| STRING | VARCHAR |
| BOOLEAN | BOOLEAN / TINYINT |
| FLOAT | FLOAT |
| DOUBLE | DOUBLE |
| TIMESTAMP | TIMESTAMP / BIGINT |
| DECIMAL | DECIMAL |

The TINYINT, SMALLINT, INTEGER, and FLOAT data types in DataHub are supported by DataHub SDK for Java V2.16.1-public and later.

**Usage notes**

DataHub allows you to synchronize data from only topics of the TUPLE type to ApsaraDB RDS for MySQL. By default, the timestamp in DataHub is converted to the timestamp in ApsaraDB RDS for MySQL based on the microsecond precision. Take note of the data precision. To prevent lock contention caused by concurrent reads and writes on the data of the same primary key, you must write data of the same primary key to the same shard.

**Create a DataConnector**

1. Log in to the DataHub console.
2. In the left-side navigation pane, click **Projects**.
3. On the **Projects** page, find the project that you want to manage and click its name to go to
the project details page.
4. On the **Topic List** tab, find the topic that you want to manage and click its name to go to
the topic details page.
5. On the topic details page, click **Connector** in the upper-right corner.
6. In the **Create Connector** panel, click **RDS & MySQL**, configure the parameters, and then
click **Create**. The following section describes the key parameters that are used to create a DataConnector in the DataHub console. To create a DataConnector in a more flexible manner, use an SDK.

| Parameter | Description |
|---|---|
| Host | The endpoint of ApsaraDB RDS for MySQL. To ensure that your instance can be connected, you must enter an internal endpoint . |
| Write Mode | The mode in which data is written. Valid values: IGNORE: ignores duplicate data. The INSERT IGNORE INTO statement is executed to write data. OVERWRITE: updates duplicate data. The REPLACE INTO statement is executed to write data. |

| User Guide·Data synchroniza | tion DataHu |
|---|---|

| Import Fields | The fields to be synchronized to ApsaraDB RDS for MySQL. You can synchronize all or partial fields of the DataHub topic to ApsaraDB RDS for MySQL based on your business requirements. |
|---|---|
| VPC ID | The ID of the VPC in which the ApsaraDB RDS for MySQL instance resides. You can view the VPC ID in the ApsaraDB RDS console. |
| Instance ID | The ID of the ApsaraDB RDS for MySQL instance. If your ApsaraDB RDS for MySQL instance resides in a VPC, you must set the Instance ID parameter. You can view the instance ID in the ApsaraDB RDS console. |

**Example**

1. Create an ApsaraDB RDS for MySQL instance and a table in the ApsaraDB RDS console.
2. Create a topic in the DataHub console. In this example, a topic of the TUPLE type is
created. The following figure shows the schema details of the created topic.
3. Create a DataConnector. In this example, IGNORE is selected as Write Mode and all fields
are selected for the Import Fields parameter.
4. Write data of the TUPLE type to the created topic. The following figure shows the written
data. In this example, four data records are written.
5. Verify the synchronized data. In this example, a MySQL client is used to connect to
ApsaraDB RDS to view the synchronized data. The following figure shows the synchronized data.

## View metrics

DataHub allows you to view topic-level metrics in the console, such as the queries per second (QPS) and traffic volume. This topic describes how to customize queries and view these metrics in the DataHub console.

**Background information**

DataHub allows you to view topic metrics in the console. You can view near-real-time information about topics, such as the queries per second (QPS) and traffic volume, on the Metric Statistics tab.

**Procedure**

1. Log in to the DataHub console.
2. In the left-side navigation pane, click **Projects**. On the Projects page, click **View** in the
**Actions** column of the project that you want to view to go to the project details page.
3. On the **Topic List** tab, click **View** in the **Actions** column of the topic that you want to view
to go to the topic details page.
4. On the topic details page, click the **Metric Statistics** tab, select a specific time point from
the drop-down list or specify a time range to view the metrics. You can view the following metrics: QPS: number of read and write requests per second. RPS: number of read and write records per second. Throughput: read/write throughput per second. Unit: KB. Latency: read/write latency per request. Unit: microseconds.

## Subscriptions

### Overview

**Resumable consumption** is required if you consume data in DataHub topics and want to
resume data consumption from the time point when your application fails. If you need to resume data consumption, you must save the current consumption offset and make sure that the service that stores the consumption offsets is highly availability. This increases the complexity of application development. The subscription feature of DataHub can persist consumption offsets to the server of DataHub to resolve the preceding problem. You need only to complete a few configurations and add a few lines of code to your application to obtain a highly available consumption offset maintenance service. In addition, the subscription feature allows you to reset consumption offsets. This ensures that data can be consumed at least once. For example, if an error occurs when your application consumes data at a specific time point and you want to consume the data again, you can reset the consumption offset without the need to restart the application. Your application will automatically consume data from the specified consumption offset.

### Create a subscription

This topic describes how to create a subscription in the DataHub console. Make sure that your account has the permissions to subscribe to topics in a specific project. The subscription feature allows you to save consumption offsets. You can use the read capability of DataHub with the capability of saving consumption offsets.

**Usage notes**

You can create a subscription in the DataHub console. Make sure that your account has the permissions to subscribe to topics in a specific project.

**Procedure**

1. Log in to the DataHub console.
2. In the left-side navigation pane, click **Projects**. On the Projects page, find the project that
you want to manage and click View in the Actions column. On the project details page, click the Topic List tab, find the topic that you want to manage, and then click **View** in the Actions column.
3. On the topic details page, click **Subscription**. In the Create Subscription panel, configure
the parameters and click **Create**.

| Parameter | Description |
|---|---|
| Application | The name of the application for which you want to create the subscription. The name must meet the following requirements: The name can contain only lowercase letters, digits, and underscores ( ). _ The name must start with a lowercase letter. The name must be 1 to 32 characters in length. |
| Description | The description of the subscription. The description must be 3 to 1,024 characters in length. |

4. Click the **Subscription List** tab on the topic details page to view the subscriptions of the
topic.

**Example**

The subscription feature allows you to save consumption offsets. You can use the read and write capabilities of DataHub with the capability of saving consumption offsets in scenarios in which you must save consumption offsets after data is read. The following sample code is used for reference only.

```
// The following sample code provides an example on how to consume data from a saved co nsumption offset and submit consumption offsets during consumption.
```

```
public void offset_consumption(int maxRetry) {
    String endpoint = "<YourEndPoint>";
    String accessId = "<YourAccessId>";
    String accessKey = "<YourAccessKey>";
    String projectName = "<YourProjectName>";
    String topicName = "<YourTopicName>";
    String subId = "<YourSubId>";
    String shardId = "0";
    List<String> shardIds = Arrays.asList(shardId);
    // Create a DataHub client.
    DatahubClient datahubClient = DatahubClientBuilder.newBuilder()
            .setDatahubConfig(
                    new DatahubConfig(endpoint,
                            // Specify whether to enable binary data transmission. In Da
taHub SDK for Java V2.12 and later, the server supports binary data transmission.
                            new AliyunAccount(accessId, accessKey), true))
            .build();
    RecordSchema schema = datahubClient.getTopic(projectName,
topicName).getRecordSchema();
    OpenSubscriptionSessionResult openSubscriptionSessionResult =
datahubClient.openSubscriptionSession(projectName, topicName, subId, shardIds);
    SubscriptionOffset subscriptionOffset =
openSubscriptionSessionResult.getOffsets().get(shardId);
    // 1. Obtain the cursor of the record at the current consumption offset. If the rec
ord expires or is not consumed, obtain the cursor of the first record within the time-t o-live (TTL) period of the topic.
    String cursor = "";
    // If the sequence number is smaller than 0, the record is not consumed.
    if (subscriptionOffset.getSequence() < 0) {
        // Obtain the cursor of the first record within the TTL period of the topic.
        cursor = datahubClient.getCursor(projectName, topicName, shardId,
CursorType.OLDEST).getCursor();
    } else {
        // Obtain the cursor of the next record.
        long nextSequence = subscriptionOffset.getSequence() + 1;
        try {
            // If the SeekOutOfRange error is returned after you obtain the cursor
based on the sequence number, the record of the current cursor expired.
            cursor = datahubClient.getCursor(projectName, topicName, shardId,
CursorType.SEQUENCE, nextSequence).getCursor();
        } catch (SeekOutOfRangeException e) {
            // Obtain the cursor of the first record within the TTL period of the topic
```

`.`

```
            cursor = datahubClient.getCursor(projectName, topicName, shardId,
CursorType.OLDEST).getCursor();
```

`}` `}`

```
    // 2. Read records and save consumption offsets. In this example, records of the TU
PLE type are read and a consumption offset is saved each time 1,000 records are read.
    long recordCount = 0L;
    // Read 1,000 records each time.
    int fetchNum = 1000;
    int retryNum = 0;
    int commitNum = 1000;
while(retryNum<maxRetry){
```

```java
    while (retryNum < maxRetry) {
        try {
            GetRecordsResult getRecordsResult = datahubClient.getRecords(projectName, t
opicName, shardId, schema, cursor, fetchNum);
            if (getRecordsResult.getRecordCount() <= 0) {
                // If no record can be read, pause the thread for 1,000 ms and continue
to read records.
                System.out.println("no data, sleep 1 second");
                Thread.sleep(1000);
                continue;
```

`}`

```java
            for (RecordEntry recordEntry : getRecordsResult.getRecords()) {
                // Consume data.
                TupleRecordData data = (TupleRecordData) recordEntry.getRecordData();
                System.out.println("field1:" + data.getField("field1") + "\t"
                        + "field2:" + data.getField("field2"));
                // Save the consumption offset after the data is consumed.
                recordCount++;
                subscriptionOffset.setSequence(recordEntry.getSequence());
                subscriptionOffset.setTimestamp(recordEntry.getSystemTime());
                // commit offset every 1000 records
                if (recordCount % commitNum == 0) {
                    // Submit the consumption offset.
                    Map<String, SubscriptionOffset> offsetMap = new HashMap<>();
                    offsetMap.put(shardId, subscriptionOffset);
                    datahubClient.commitSubscriptionOffset(projectName, topicName, subId
, offsetMap);
                    System.out.println("commit offset successful");
```

`}` `}`

```
            cursor = getRecordsResult.getNextCursor();
        } catch (SubscriptionOfflineException | SubscriptionSessionInvalidException e)
```

`{`

```
            // The subscription session is exited. Offline indicates that the
subscription is offline. SessionChange indicates that the subscription is consumed by o ther clients.
            e.printStackTrace();
            throw e;
        } catch (SubscriptionOffsetResetException e) {
            // The consumption offset is reset. You must obtain the version information
of the consumption offset again.
            SubscriptionOffset offset =
datahubClient.getSubscriptionOffset(projectName, topicName, subId, shardIds).getOffsets().get(shardId);
            subscriptionOffset.setVersionId(offset.getVersionId());
            // After the consumption offset is reset, you must obtain the cursor of the
record at the consumption offset again. The method used to obtain the cursor depends on the method used to reset the consumption offset.
            // If both the sequence number and timestamp are specified to reset the con
sumption offset, you can obtain the cursor based on the sequence number or the timestam
```

`p.`

```
            // If only the sequence number is specified to reset the consumption
offset, you can obtain the cursor based only on the sequence number.
            // If only the timestamp is specified to reset the consumption offset, you
canobtainthecursorbasedonlyonthetimestamp.
```

```java
can obtain the cursor based only on the timestamp.
            // In most cases, preferentially obtain the cursor based on the sequence nu
mber. If the cursor failed to be obtained based on the sequence number or the timestamp , obtain the cursor of the earliest record.
            cursor = null;
            if (cursor == null) {
                try {
                    long nextSequence = offset.getSequence() + 1;
                    cursor = datahubClient.getCursor(projectName, topicName, shardId, Cu
rsorType.SEQUENCE, nextSequence).getCursor();
                    System.out.println("get cursor successful");
                } catch (DatahubClientException exception) {
                    System.out.println("get cursor by SEQUENCE failed, try to get cursor
by SYSTEM_TIME");
```

`}` `}`

```java
            if (cursor == null) {
                try {
                    cursor = datahubClient.getCursor(projectName, topicName, shardId, Cu
rsorType.SYSTEM_TIME, offset.getTimestamp()).getCursor();
                    System.out.println("get cursor successful");
                } catch (DatahubClientException exception) {
                    System.out.println("get cursor by SYSTEM_TIME failed, try to get cur
sor by OLDEST");
```

`}` `}`

```java
            if (cursor == null) {
                try {
                    cursor = datahubClient.getCursor(projectName, topicName, shardId, Cu
rsorType.OLDEST).getCursor();
                    System.out.println("get cursor successful");
                } catch (DatahubClientException exception) {
                    System.out.println("get cursor by OLDEST failed");
                    System.out.println("get cursor failed!!");
                    throw e;
```

`}` `}`

```
        } catch (LimitExceededException e) {
            // limit exceed, retry
            e.printStackTrace();
            retryNum++;
        } catch (DatahubClientException e) {
            // other error, retry
            e.printStackTrace();
            retryNum++;
        } catch (Exception e) {
            e.printStackTrace();
            System.exit(-1);
```

`}` `}` `}`

**Note**

If you start an application for the first time, the application consumes data from the earliest record. When the application is running, you can refresh the Subscription List tab in the DataHub console. If you reset the consumption offset by clicking Reset in the DataHub console during the consumption, your application automatically detects the change of the consumption offset and consumes data from the specified consumption offset. When the application catches **OffsetResetedException**, the application calls the
**getSubscriptionOffset** operation to query the latest consumption offset from the
server. Then, the application can consume data from the latest consumption offset. A shard in a subscription cannot be consumed by multiple threads or processes at the same time. Otherwise, the consumption offset submitted by a thread is overwritten by that submitted by another thread and the server cannot determine the thread to which the saved consumption offset belongs. In this case, the server reports **OffsetSessionChangedException**. We recommend that you exit the subscription session to check whether data is repeatedly consumed if this exception is detected.

### Reset a consumption offset

You can reset a consumption offset to another one from which you want to consume data for each subscription in DataHub.

**Procedure**

1. Log in to the DataHub console.
2. In the left-side navigation pane, click **Projects**. On the Projects page, find the project that
you want to manage and click View in the Actions column. On the project details page, click the Topic List tab, find the topic that you want to manage, and then click **View** in the Actions column.
3. On the topic details page, click the **Subscription List** tab, find the subscription that you
want to manage, and then click **Reset** in the **Actions** column.
4. In the **Reset Offset** panel, specify a new consumption offset based on your business
requirements.
5. Click **Reset**.

### Delete a subscription

DataHub allows you to permanently delete subscriptions. After a subscription is deleted, it cannot be restored. This topic describes how to delete a subscription in the DataHub console.

**Usage notes**

You can delete subscriptions in DataHub. After you delete a subscription, the subscription is permanently deleted, including the consumption offsets saved for the subscription. Proceed with caution.

**Procedure**

1. Log in to the DataHub console.
2. In the left-side navigation pane, click **Projects**. On the Projects page, find the project that
you want to manage and click View in the Actions column. On the project details page, click the Topic List tab, find the topic that you want to manage, and then click **View** in the Actions column.
3. On the topic details page, click the **Subscription List** tab, find the subscription that you
want to delete, and then click **Delete** in the **Actions** column.
4. In the message that appears, confirm the information and click **Delete**.

### View consumption details

DataHub allows you to view the consumption details of each subscription. This topic describes how to view consumption details in the DataHub console.

**Procedure**

1. Log in to the DataHub console.
2. In the left-side navigation pane, click **Projects**. On the Projects page, find the project that
you want to manage and click View in the Actions column. On the project details page, click the Topic List tab, find the topic that you want to manage, and then click **View** in the Actions column.
3. On the topic details page, click the **Subscription List** tab, find the subscription whose
consumption details you want to view, and then click **Consumption Details** in the
**Actions** column.
4. In the **Collaborative Consumption Details** panel, view the subscription ID, name of the
application that consumes data, and shards from which data is consumed. ption

## Collaborative

**consumption**

### Note

DataHub-client-library encapsulates the Java SDK and integrates the consumer for collaborative consumption and the producer for distributing data evenly among shards.

### Overview

This topic describes the implementation principles and usage of offset-based data consumption and collaborative consumption. Offset-based data consumption allows you to continue consumption from the last submitted offset when a task is restarted, while collaborative consumption simplifies the process of consuming a topic by multiple consumers at the same time.

**Offset-based data consumption**

The offset-based data consumption feature allows you to save consumption offsets on the server. A consumption offset consists of the sequence number of a record and the timestamp when the record is written to DataHub. After you create a subscription for a topic and your application consumes specific data, the consumption offset is submitted to the server. When your application starts the next time, the application can obtain the consumption offset from the server and consume data from the next record. The consumption offsets must be saved on the server so that your application can consume data from a submitted consumption offset after shards are reallocated. This is a prerequisite for collaborative consumption. You do not need to manually submit consumption offsets in the consumer. You only need to specify the interval of submitting consumption offsets in the configurations of the consumer. The system considers that the previous records are consumed when it reads records. If the interval of submitting consumption offsets is exceeded, the system submits a consumption offset again. If the consumption offset fails to be submitted and your application is interrupted, the consumption offset may fail to be submitted in time. In this case, your application may repeatedly consume specific data.

**Collaborative consumption**

The collaborative consumption feature automatically allocates shards when multiple consumers consume a topic at the same time. This feature simplifies the data processing of clients.

**Note**

Manual shard allocation is difficult because multiple consumers may reside on different machines. If multiple consumers that subscribe to the same topic are in the same consumer group, a shard can be allocated to only one consumer in the consumer group. Example: Assume that A, B, and C are three consumer instances and the topic has 10 shards.
1. When the consumer instance A is started at first, 10 shards are allocated to it.
2. When the other two consumer instances are started, the shards are reallocated in the
following way: four to A, three to B, and three to C. ption
3. When one of the shards consumed by the consumer instance A is split into two and the two
shards are released after consumption, the shards are reallocated in the following way: four to A, four to B, and three to C.
4. When the consumer instance C is stopped, the shards are reallocated in the following way:
six to A and five to B.

**Heartbeat**

You must use the heartbeat feature to notify the server of the status of consumer instances. If the server has not received heartbeats from a consumer instance after the specified interval, the server considers that the consumer instance is stopped. When the status of a consumer instance changes, the server reallocates shards. The server returns the new allocation plan in heartbeat requests. Therefore, the client takes time to detect the reallocation of shards.

### Usage notes

A consumer or producer cannot access DataHub by using multiple threads. If you need to use multiple threads, specify a different consumer or producer for each thread.

### Maven dependencies and JDK

This topic describes how to configure Maven dependencies and specify the JDK version for the DataHub client library.

**Maven dependencies**

```xml
<dependency>
      <groupId>com.aliyun.datahub</groupId>
      <artifactId>datahub-client-library</artifactId>
      <version>1.0.6-public</version>
</dependency>
```

**JDK**

```
jdk: >= 1.7
```

### Usage examples

This topic provides complete examples of writing data to and reading from DataHub. These examples demonstrate how to initialize a producer and a consumer, send and receive data, and transfer data efficiently.

**Initialize a producer**

```
String endpoint = "http://dh-cn-hangzhou.aliyuncs.com"; String accessId = "<YourAccessKeyId>"; String accessKey = "<YourAccessKeySecret>"; String projectName = "<YourProjectName>"; String topicName = "<YourTopicName>"; ProducerConfig config = new ProducerConfig(endpoint, accessId, accessKey); Producer producer = new Producer(projectName, topicName, config);
```

ption

**Write data**

```
RecordSchema schema = new RecordSchema(); schema.addField(new Field("field1", FieldType.STRING)); schema.addField(new Field("field2", FieldType.BIGINT)); List<RecordEntry> recordEntries = new ArrayList<>(); for (int cnt = 0; cnt < 10; ++cnt) {
    RecordEntry entry = new RecordEntry();
    entry.addAttribute("key1", "value1");
    entry.addAttribute("key2", "value2");
    TupleRecordData data = new TupleRecordData(schema);
    data.setField("field1", "testValue");
    data.setField("field2", 1);
    entry.setRecordData(data);
    recordEntries.add(entry);
```

`}`

```
int maxRetry = 3; while (true) {
    try {
        producer.send(records, maxRetry);
        break;
    } catch (MalformedRecordException e) {
        // Malformed RecordEntry.
    } catch (InvalidParameterException e) {
        // Invalid parameter.
    } catch (ResourceNotFoundException e) {
        // The project, topic, or shard is not found. This can be caused by a shard spl
it or merge.
    } catch (DatahubClientException e) {
        // A network error or other exception exceeded the retry limit.
```

`}` `}`

```
// Close the producer before the application exits. producer.close();
```

**Initialize a consumer**

ption

```
String endpoint = "http://dh-cn-hangzhou.aliyuncs.com"; String accessId = "<YourAccessKeyId>"; String accessKey = "<YourAccessKeySecret>"; String projectName = "<YourProjectName>"; String topicName = "<YourTopicName>"; String SubId = "<YourSubscriptionId>"; // 1. Use coordinated consumption. Provide a subscription ID. ConsumerConfig config = new ConsumerConfig(endpoint, accessId, accessKey); Consumer consumer = new Consumer(projectName, topicName, SubId, config); // 2. Use uncoordinated consumption with the offset service. Provide a subscription ID and the list of shards for the consumer to read. List<String> assignment = Arrays.asList("0", "1", "2"); ConsumerConfig config = new ConsumerConfig(endpoint, accessId, accessKey); Consumer consumer = new Consumer(projectName, topicName, SubId, assignment, config); // 3. Use uncoordinated consumption without the offset service. Provide a subscription ID, the shards for the consumer to read, and their initial offsets. Map<String, Offset> offsetMap = new HashMap<>(); // Provide a sequence number and a timestamp. If the sequence number is out of range, t he timestamp is used to obtain the cursor. offsetMap.put("0", new Offset(100, 1548573440756L)); // Provide only a sequence number to get the cursor. offsetMap.put("1", new Offset().setSequence(1)); // Provide only a timestamp to get the cursor. offsetMap.put("2", new Offset().setTimestamp(1548573440756L)); ConsumerConfig config = new ConsumerConfig(endpoint, accessId, accessKey); Consumer consumer = new Consumer(projectName, topicName, SubId, offsetMap, config);
```

**Read data**

ption

```java
int maxRetry = 3; boolean stop = false; while (!stop) {
    try {
        while (true) {
            RecordEntry record = consumer.read(maxRetry);
            if (record != null) {
                TupleRecordData data = (TupleRecordData) record.getRecordData();
                System.out.println("field1:" + data.getField(0) + ", field2:" +
data.getField("field2"));
```

`}` `}`

```
    } catch (SubscriptionSessionInvalidException | SubscriptionOffsetResetException e)
```

`{`

```
        // Subscription exception. The current consumer session cannot recover.
        // You can log the error or create a new consumer.
        consumer.close();
        consumer = new Consumer(TEST_PROJECT, TEST_TOPIC, TEST_SUB_ID, config);
    } catch (ResourceNotFoundException | InvalidParameterException e) {
        // - The project, topic, shard, or subscription is not found.
        // - The seek operation is out of range.
        // - A shard split or merge can also cause a ResourceNotFoundException.
        // Verify that the resource exists, log the error, or exit the application.
    } catch (DatahubClientException e) {
        // - A network error or another exception exceeded the retry limit.
        // You can sleep for a while and then retry.
```

`}` `}`

```
// Close the consumer before the application exits. consumer.close();
```
