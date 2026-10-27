---
title: "Alibaba Cloud Apsara Stack V3.18.3 Message Queue for Apache Kafka User Guide 20241107"
product_version: "V3.18.3"
doc_version: "20241107"
pdf_pages: 45
source_pdf: "Alibaba Cloud Apsara Stack V3.18.3 Message Queue for Apache Kafka User Guide 20241107.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/V3.18.3/%E6%B6%88%E6%81%AF%E9%98%9F%E5%88%97kafka/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.3%20Message%20Queue%20for%20Apache%20Kafka%20User%20Guide%2020241107.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes+edge-junk)
---

# Alibaba Cloud Apsara Stack V3.18.3 Message Queue for Apache Kafka User Guide 20241107

## Table of Contents

- 1 What is ApsaraMQ for Kafka?
- 2 Console operations
  - 2.1 Log on to the ApsaraMQ for Kafka console
  - 2.2 Getting started
    - 2.2.1 Create topics
    - 2.2.2 Send messages
    - 2.2.3 Query messages
  - 2.3 Instances
    - 2.3.1 Manage instances
    - 2.3.2 Configure instance relationships
    - 2.3.3 Obtain the endpoint of an instance
  - 2.4 Topics
    - 2.4.1 Create topics
    - 2.4.2 View the list of topics
    - 2.4.3 View partition status in a topic
    - 2.4.4 View the subscriptions of a topic
    - 2.4.5 Modify topic configurations
    - 2.4.6 Increase the number of partitions in a topic
    - 2.4.7 Configure topic parameters
  - 2.5 Consumer groups
    - 2.5.1 View the list of consumer groups
    - 2.5.2 View the consumer status of a consumer group
    - 2.5.3 Reset the consumer offset of a consumer group
  - 2.6 Configure instance parameters
  - 2.7 Messages
    - 2.7.1 Send messages
    - 2.7.2 Query messages
  - 2.8 ACL
    - 2.8.1 Enable ACL
    - 2.8.2 Create SASL users
    - 2.8.3 Grant permissions to SASL users
    - 2.8.4 Change the passwords of SASL users
    - 2.8.5 Delete SASL users
    - 2.8.6 Delete the permissions of SASL users
  - 2.9 VIPs
    - 2.9.1 Create VIPs
    - 2.9.2 Delete VIPs
  - 2.10 Zone-disaster recovery
    - 2.10.1 Solution introduction
    - 2.10.2 Create replica clusters
- 3 Pod command operations
  - 3.1 Command verification
    - 3.1.1 Create topics
    - 3.1.2 Send messages
    - 3.1.3 Consume messages
  - 3.2 Topics
    - 3.2.1 Create topics
    - 3.2.2 View the status of a topic
    - 3.2.3 View the current offset of a partition
    - 3.2.4 View the list of topics
    - 3.2.5 Increase the number of partitions in a topic
    - 3.2.6 Modify topic configurations
  - 3.3 Consumer groups
    - 3.3.1 View the consumer status of a consumer group
    - 3.3.2 View the list of consumer groups
  - 3.4 Messages
    - 3.4.1 Send messages
    - 3.4.2 Consume messages

Kafka?

## 1 What is ApsaraMQ for Kafka?

**Kafka?**

ApsaraMQ for Kafka is a distributed, high-throughput, and scalable message queue service provided by Alibaba Cloud. Used in big data fields such as log collection, monitoring data aggregation, streaming data processing, and online and offline analytics, ApsaraMQ for Kafka is an indispensable part of the big data ecosystem.

**Benefits**

ApsaraMQ for Kafka provides fully managed services for open source Apache Kafka and helps resolve specific pain points of open source Apache Kafka. ApsaraMQ for Kafka does not require deployment or O&M. You can focus on business development. With ApsaraMQ for Kafka, you can improve your service scalability and reliability with lower service costs.

**Application ecosystem**

ApsaraMQ for Kafka provides a rich application ecosystem that covers the following fields: Big data: ApsaraMQ for Kafka is used in fields such as website behavior analysis, log aggregation, application monitoring, streaming data processing, and online and offline data analytics. Data integration: ApsaraMQ for Kafka allows you to import messages to offline data warehouses such as MaxCompute, Object Storage Service (OSS), ApsaraDB RDS, Hadoop, and HBase. Stream computing integration: ApsaraMQ for Kafka integrates stream computing engines such as Realtime Compute, E-MapReduce, Spark, and Storm.

## 2 Console operations

### 2.1 Log on to the ApsaraMQ for Kafka console

**Kafka console**

This topic describes how to log on to the ApsaraMQ for Kafka console.

**Prerequisites**

The URL of the Apsara Uni-manager Management Console is obtained from the deployment personnel before you log on to the Apsara Uni-manager Management Console. A browser is available. We recommend that you use the Google Chrome browser.

**Procedure**

1. In the address bar, enter the URL of the Apsara Uni-manager Management Console. Press
the Enter key.
2. Enter your username and password.
Obtain the username and password that you can use to log on to the console from the operations administrator.

> **Note:** When you log on to the Apsara Uni-manager Management Console for the first time, you must change the password of your username. Your password must meet complexity requirements. The password must be 8 to 20 characters in length and must contain at least two of the following character types:
> Uppercase or lowercase letters
> Digits
> Special characters, which include ! @ # $ %

3. Click **Login**.
4. If MFA is enabled for your account, perform the required operations based on the scenario:

**This is your first time logging on to the Apsara Uni-manager Management**

**Console after MFA is enabled by the administrator.**

a. On the Bind Virtual MFA Device page, follow the on-screen instructions to bind an MFA device. b. Enter the username and password again as in Step 2 and click **Log On**. c. Enter a six-digit MFA verification code and click **Authenticate**.

**You have enabled MFA and bound an MFA device.**

Enter a six-digit MFA verification code and click **Authenticate**.
5. In the top navigation bar, choose **Products > Middleware > ApsaraMQ for Kafka**.
6. On the **ApsaraMQ for Kafka** page, select the organization and region and click **Kafka**.

### 2.2 Getting started

#### 2.2.1 Create topics

In ApsaraMQ for Kafka, topics are used to store messages published by producers. Before you send and receive messages, you must create a topic.
1. Log on to the ApsaraMQ for Kafka console.
2. On the **Instance List** page, find the instance that you want to manage and click **Details** in
the **Operation** column.
3. On the **Instance details page**, click the **Topic management** tab.
4. On the **Topic management** tab, click **Create a Topic**.
5. In the **Create a Topic** dialog box, follow the on-screen instructions to configure the
parameters and click **OK**. The following table describes the parameters.

| Parameter | Description |
|---|---|
| Topic | The topic name. The topic name can contain only letters, digits, hyphens (-), and underscores ( ). _ The topic name must be 3 to 64 characters in length. If the name contains more than 64 characters, the name is automatically truncated. The topic name cannot be changed after the topic is created. |
| Instance | The ID of the instance on which the topic is created. |
| Number of partitions | The number of partitions in the topic. We recommend that the number of partitions be a multiple of 6 to reduce data skew risks. Valid values: 1 to 48. |

#### 2.2.2 Send messages

After you create a topic, you can send messages to the topic in the ApsaraMQ for Kafka console.

**Procedure**

1. Log on to the ApsaraMQ for Kafka console.
2. On the **Instance List** page, find the instance that you want to manage and click **Details** in
the **Operation** column.
3. On the **Instance details page**, click the **Topic management** tab.
4. On the **Topic management** tab, find the topic that you want to manage and click **Send**
**message** in the **Operation** column.
5. In the **Send message** panel, enter the ID of the partition from which you want to send a
message in the **Partition** field and the message key and message value in the **Message**
**Key** and **Message Value** fields. Then, click **OK**.

#### 2.2.3 Query messages

After you send a message, you can query the message.

**Background information**

ApsaraMQ for Kafka allows you to query messages by using one of the following methods: By offset: If you know the partition from which the message is sent and the consumer offset of the message, you can use this method to query the message. By time: If you do not know the partition from which the message is sent and the consumer offset of the message but know the time when the message is sent, you can use this method to query the message.

**Usage notes**

Up to 30 messages whose total size does not exceed 10 MB can be returned in a query result. A maximum of 1 KB of content can be displayed for each message. Content that exceeds 1 KB is automatically truncated. If you want to view the complete content of a message, download the message. Only messages that are not cleared by the broker can be queried. The following message cleanup policies are used on ApsaraMQ for Kafka brokers: If the disk usage is lower than 85%, expired messages are deleted at 04:00 every day. If the disk usage reaches 85%, expired messages are immediately deleted. If the disk usage reaches 90%, stored messages are deleted in the order that the messages were stored in the clients.

**Query a message by offset**

1. Log on to the ApsaraMQ for Kafka console.
2. On the **Instance List** page, find the instance that you want to manage and click **Details** in
the **Operation** column.
3. On the **Instance details page**, click the **Message query** tab.
4. On the **Message query** tab, click **Query by site**, enter or select the topic, partition, and
consumer offset, and then click **Query**. The queried message is displayed on the **Message query** tab.

| Parameter | Description |
|---|---|
| Partition | The partition in the topic from which the message is sent. |
| Site | The consumer offset of the message. |
| Time | The time when the message is stored on the broker. |

| Key(size: 1B) | The message key. The key is transformed into a string. |
|---|---|
| Value(size: 1B) | The message value. The value is transformed into a string. |

5. **(Optional)** If you want to download the key or value of a message, select the message and
click **Download message** next to **Key** or **Value**.

**Query a message by time**

1. Log on to the ApsaraMQ for Kafka console.
2. On the **Instance List** page, find the instance that you want to manage and click **Details** in
the **Operation** column.
3. On the **Instance details page**, click the **Message query** tab.
4. On the **Message query** tab, click **Query by time**, enter or select the topic, partition, and
time, and then click **Query**. The queried message is displayed on the **Message query** tab.

| Parameter | Description |
|---|---|
| Partition | The partition in the topic from which the message is sent. |
| Site | The consumer offset of the message. |
| Time | The time when the message is stored on the broker. |
| Key(size: 1B) | The message key. The key is transformed into a string. |
| Value(size: 1B) | The message value. The value is transformed into a string. |

5. **(Optional)** If you want to download the key or value of a message, select the message and
click **Download message** next to **Key** or **Value**.

### 2.3 Instances

#### 2.3.1 Manage instances

In ApsaraMQ for Kafka, an instance is used to store information about topics and group IDs. This topic describes how to create, scale out, and release an instance in the ApsaraMQ for Kafka console. This topic also describes how to view the details of an instance in the console. Sufficient physical resources are reserved to ensure the successful creation of an instance.

**Usage limits**

To create an instance in the ApsaraMQ for Kafka console, you must upgrade ApsaraMQ for Kafka to V3.18.0. ApsaraMQ for Kafka V3.18.0 or later allows you to scale out an instance in the console if the instance is created in the console. The scaling method remains unchanged for instances delivered by using ApsaraMQ for Kafka versions earlier than 3.18.0.

**Create an instance**

1. Log on to the ApsaraMQ for Kafka console.
2. In the left-side navigation pane, click **Instances**.
3. On the **Instances** page, click **Create an instance**.
4. On the **Create a Kafka instance** page, configure the parameters and click **Submit**. The
following table describes the parameters.

| Section | Parameter | Description |
|---|---|---|
| Basic information | Organization | The organization to which the instance that you want to create belongs. |
|   | Resource Set | The resource set to which the instance that you want to create belongs. |
|   | Geography | The region where the instance that you want to create resides. |
|   | Primary Availability Zone | The zone in which you want to create the instance. |
|   | Instance name | The instance name. |
| Kafka node information | Chip Type | The type of the chip that is used by the ApsaraMQ for Kafka resource pool. |
|   | Specifications | The specification of the instance that you want to create. Valid values: Broker4C16G Broker16C64G Broker32C128G Broker64C256G |
|   | Number of brokers | The number of brokers. Minimum value: 3. |

|   | Storage Type | The storage type. The default value is fast- disks-ssd, which specifies exclusive SSDs. You cannot specify a custom value for this parameter. |
|---|---|---|
|   | Number of disks per Broker | The number of disks. Default value: 1. You cannot specify a custom value for this parameter. |
| Network Information | Network Type | The network type. Valid values: AnyTunnel SingleTunnel |
|   | VPC | The ID of the virtual private cloud (VPC) in which the instance that you want to create is deployed. This parameter is required only if you set the Network Type parameter to SingleTunnel. |
|   | VSwitch | The ID of the vSwitch to which the instance that you want to create belongs. This parameter is required only if you set the Network Type parameter to SingleTunnel. |

**View the details of an instance**

1. On the **Instances** page, find the instance whose details you want to view and click **Details**
in the **Operation** column.
2. On the **Instance details** page, view the details of the instance on the **Instance details**,
**Running status**, **Access point information**, and **Task execution record** tabs.

**Scale out an instance**

If your ApsaraMQ for Kafka instance cannot meet your business requirements, you can scale out the instance in the ApsaraMQ for Kafka console.

> **Important:** After the scale-out, the number of brokers cannot be greater than the total number of exclusive nodes. ApsaraMQ for Kafka does not allow you to scale in an instance.

1. On the **Instances** page, find the instance that you want to scale out and click **Expansion**
in the **Operation** column.
2. On the **Kafka instance expansion** page, specify a value in the **Number of final state**
**Broker nodes** field and click **Submit**.

**Load balancing**

After you scale out an instance, existing topics are not automatically distributed to new brokers. In this case, you need to perform load balancing.
1. On the **Instances** page, find the instance that you want to manage and click **Load**
**balancing** in the **Operation** column.
2. In the message that appears, click **OK**.

**Release an instance**

> **Warning:** After you release an instance, all data in the instance is deleted and cannot be restored. Proceed with caution.

1. On the **Instances** page, find the instance that you want to manage and click **Release** in
the **Operation** column.
2. In the message that appears, click **OK**.

#### 2.3.2 Configure instance relationships

Users in a resource group can view an ApsaraMQ for Kafka instance and perform operations on the instance only after you configure the relationships of the instance.

**Limits**

**Historical versions**

ApsaraMQ for Kafka strongly depends on the Apsara Uni-manager Management Console and OneConsole. To use the instance relationship feature, you must upgrade the three products at the same time. The following items describe the version numbers of the products after the upgrade: ApsaraMQ for Kafka Hotfix name: v3.14.0r-paas-kafka-SP003 Version: ASEN_Prd-kafka_v1.14.3_archX Apsara Uni-manager Management Console: v3.14.0r-ascm-SP012 OneConsole: v3.14.0r-ascm-SP012

**Current versions**

ApsaraMQ for Kafka strongly depends on the Apsara Uni-manager Management Console and OneConsole. To use the instance relationship feature, you must upgrade the three products at the same time. The following items describe the version numbers of the products after the upgrade: ApsaraMQ for Kafka Hotfix name: v3.16.2r-paas-kafka-SP001 Version: ASEN_Prd-kafka_v1.14.3_archX Apsara Uni-manager Management Console: v3.16.2r-ascm-SP003 OneConsole: v3.16.2r-oneConsole-SP003 After you upgrade the product versions, the resource auditor automatically has the permissions to query the instance relationship list. The organization administrator automatically has the permissions to query the instance relationship list and configure instance relationships. Other users have the permissions to query the instance relationship list and configure instance relationships only after the administrator grants the permissions to the users.

**Roles**

The organization administrator and resource auditor automatically have the permissions to query the instance relationship list or configure instance relationships.

**Configurations**

Each instance can belong only to one resource group. After you specify a resource group for an instance, you cannot change the resource group.

**Prerequisites**

The permissions to query the instance relationship list and configure instance relationships are granted to the logon user.

**Procedure**

1. Use the admin account to log on to the ApsaraMQ for Kafka console. For more information,
see Log on to the ApsaraMQ for Kafka console.
2. In the left-side navigation pane, click **Instance Relationship Configuration**.
3. On the **Instance relationship configuration** page, find the instance that you want to
manage and click **Home configuration** in the **Operation** column.
4. In the **Home configuration** panel, select the organization and resource set to which the
instance belongs and click **OK**. On the **Instance relationship configuration** page, you can see the value in the
**Operation** column of the corresponding instance changes to **Configured**.

#### 2.3.3 Obtain the endpoint of an instance

This topic describes how to obtain the endpoint of an ApsaraMQ for Kafka instance.

**Prerequisites**

The instance relationships are configured. For more information, see Configure instance relationships. A virtual IP address (VIP) is created. For more information, see Create a VIP.

**Background information**

ApsaraMQ for Kafka allows you to use endpoints to connect to the following ports: 8080: You can use this port when you connect to an instance in a virtual private cloud (VPC). Simple Authentication and Security Layer (SASL) authentication is not supported. 8081: You can use this port when you connect to an instance in a VPC. SASL authentication is supported. The PLAINTEXT mechanism is used to authenticate client identities, and the Secure Sockets Layer (SSL) encryption method is used during message transmission. 8088: You can use this port when you connect to an instance in a VPC. SASL authentication is supported. The PLAINTEXT mechanism is used to authenticate client identities.

**Procedure**

1. Log on to the ApsaraMQ for Kafka console.
2. In the left-side navigation pane, click **Instances**.
3. On the **Instance List** page, find the instance that you want to manage and click **Details** in
the **Operation** column.
4. On the **Access point information** tab of the **Instance details** page, view the endpoint of
the instance.

### 2.4 Topics

#### 2.4.1 Create topics

In ApsaraMQ for Kafka, topics are used to store messages published by producers. Before you send and receive messages, you must create a topic.

**Procedure**

1. Log on to the ApsaraMQ for Kafka console.
2. On the **Instance List** page, find the instance that you want to manage and click **Details** in
the **Operation** column.
3. On the **Instance details page**, click the **Topic management** tab.
4. On the **Topic management** tab, click **Create a Topic**.
5. In the **Create a Topic** dialog box, follow the on-screen instructions to configure the
parameters and click **OK**. The following table describes the parameters.

| Parameter | Description |
|---|---|
| Topic | The topic name. The topic name can contain only letters, digits, hyphens (-), and underscores ( ). _ The topic name must be 3 to 64 characters in length. If the name contains more than 64 characters, the name is automatically truncated. The topic name cannot be changed after the topic is created. |
| Instance | The ID of the instance on which the topic is created. |
| Number of partitions | The number of partitions in the topic. We recommend that the number of partitions be a multiple of 6 to reduce data skew risks. Valid values: 1 to 48. |

#### 2.4.2 View the list of topics

This topic describes how to view the list of topics.

**Procedure**

1. Log on to the ApsaraMQ for Kafka console.
2. On the **Instance List** page, find the instance that you want to manage and click **Details** in
3. On the **Instance details page**, click the **Topic management** tab.
4. On the **Topic management** tab, view the list of topics.

#### 2.4.3 View partition status in a topic

After you create a topic, you can view the status of each partition in the topic.

**Procedure**

1. Log on to the ApsaraMQ for Kafka console.
2. On the **Instance List** page, find the instance that you want to manage and click **Details** in
the **Operation** column.
3. On the **Instance details page**, click the **Topic management** tab.
4. On the **Topic management** tab, find the topic that you want to manage and click
**Partition status** in the **Operation** column.
In the **Partition status** panel, the status of all partitions in the topic is displayed.

| Parameter | Description |
|---|---|
| The total number of messages on the current server | The total number of messages in all partitions. |
| Partition ID | The ID of the partition in the topic. |
| Minimum site | The minimum consumer offset of the topic in the current partition. |
| Maximum offset | The maximum consumer offset of the topic in the current partition. |

#### 2.4.4 View the subscriptions of a topic

After you create a topic, you can view the online consumer groups that subscribe to the topic.

**Procedure**

1. Log on to the ApsaraMQ for Kafka console.
2. On the **Instance List** page, find the instance that you want to manage and click **Details** in
the **Operation** column.
3. On the **Instance details page**, click the **Topic management** tab.
4. On the **Topic management** tab, find the topic that you want to manage and click
**Subscription relationship** in the **Operation** column.
In the panel that appears, you can view all consumer groups that subscribe to the topic.

| Parameter | Description |
|---|---|
| Topic | The topic name. |

| Subscription Consumer Group | The number of consumer groups that subscribe to the topic. |
|---|---|

#### 2.4.5 Modify topic configurations

After you create a topic, you can modify the configurations of the topic.

**Procedure**

1. Log on to the ApsaraMQ for Kafka console.
2. On the **Instance List** page, find the instance that you want to manage and click **Details** in
the **Operation** column.
3. On the **Instance details page**, click the **Topic management** tab.
4. On the **Topic management** tab, find the topic that you want to manage and choose **... >**
**topic configuration** in the **Operation** column.
5. In the **Topic configuration** dialog box, find the configuration item that you want to modify
and click **Modify** next to the configuration item. Then, specify a new value, click **OK**, and close the dialog box.

| Parameter | Description |
|---|---|
| min.insync.replicas(Minimum number of synchronized replicas) | The minimum number of synchronized replicas. Valid values: 1 to 3. Recommended value: 1. The minimum number of synchronized replicas must be smaller than or equal to the number of replicas. The minimum number of synchronized replicas defines the minimum number of replicas from which the system receives acknowledgments to determine the successful writing of a message. The minimum number of replicas is valid only if the producer sets message acknowledgment to All or -1. |
| retention.ms(Message retention time(hour)) | The period of time for which messages are retained in a topic. Valid values: 1 to 168. Unit: hours. |
| max.message.bytes(Maximum message size(M)) | The maximum size of a message that the topic can receive from a producer. Valid values: 1 to 10. Unit: MB. |

#### 2.4.6 Increase the number of partitions in a topic

**topic**

After you create a topic, you can increase the number of partitions in the topic. ApsaraMQ for Kafka does not allow you to decrease the number of partitions in a topic. If you want to decrease the number of partitions in a topic, you can delete the topic and create another topic that has the required number of partitions.

**Procedure**

1. Log on to the ApsaraMQ for Kafka console.
2. On the **Instance List** page, find the instance that you want to manage and click **Details** in
the **Operation** column.
3. On the **Instance details page**, click the **Topic management** tab.
4. On the **Topic management** tab, find the topic that you want to manage and choose

**>**

**Increase the number of partitions** in the **Operation** column.
5. In the **Increase the number of partitions** dialog box, configure the **Number of new**
**partitions** parameter and click **OK**.

#### 2.4.7 Configure topic parameters

This topic describes how to configure the parameters of a topic.

**Procedure**

1. Log on to the ApsaraMQ for Kafka console.
2.
3. On the **Instance List** page, find the instance that you want to manage and click **Details** in
the **Operation** column. 4.
5. On the **Instance details page**, click the **Topic management** tab.
6. On the **Topic management** tab, find the topic that you want to manage and choose **... >**
**topic configuration** in the **Operation** column.
7. In the **Topic configuration** dialog box, click **Modify** next to the parameter that you want
to modify. Then, specify a value in the field that appears and click **OK**. The following table describes the parameters.

| Parameter | Description | Example |
|---|---|---|
| min.insync.replicas | The minimum number of replicas. Valid values: 1 to 3. | 1 |
| retention.ms | The message retention period. Valid values: 1 to 168. Unit: hours. | 168 |
| max.message.bytes | The maximum size of a message. Valid values: 1 to 10. Unit: MB. | 10 |

| retention.bytes | The total size of data that can be stored in each partition of a topic. The default value is -1, which specifies that the total size is not limited. Unit: MB. | 10 |
|---|---|---|

### 2.5 Consumer groups

#### 2.5.1 View the list of consumer groups

This topic describes how to view the list of consumer groups.

**Procedure**

1. Log on to the ApsaraMQ for Kafka console.
2. In the left-side navigation pane, click **Instances**.
3. On the **Instance List** page, find the instance that you want to manage and click **Details** in
the **Operation** column.
4. On the **Instance details page**, click the **Group management** tab.
5. On the **Group management** tab, view the list of consumer groups.

#### 2.5.2 View the consumer status of a consumer group

**consumer group**

This topic describes how to view the consumer status of a consumer group.

**Procedure**

1. Log on to the ApsaraMQ for Kafka console.
2. In the left-side navigation pane, click **Instances**.
3. On the **Instance List** page, find the instance that you want to manage and click **Details** in
the **Operation** column.
4. On the **Instance details page**, click the **Group management** tab.
5. On the **Group management** tab, find the consumer group that you want to manage and
click **Consumption status** in the **Operation** column. In the **Consumption status** panel, the status of all consumers in the consumer group is displayed.

| Parameter | Description |
|---|---|
| Consumer Group | The name of the consumer group. |
| Total message accumulation | The total number of unconsumed messages in all topics to which the consumer group subscribes. |

| Topic | The name of the topic to which the consumer group subscribes. |
|---|---|
| Accumulation | The number of unconsumed messages in the topic to which the consumer group subscribes. |

6. **(Optional)** If you want to view the consumption details of a specific topic, find the topic in
the topic list of the **Consumption status** panel and click **Details** in the **Operation** column of the topic. The consumption details of the topic is displayed in the message that appears.

| Parameter | Description |
|---|---|
| Partition ID | The ID of the partition in the topic. |
| owner | The ID and IP address of the online consumer that subscribes to the topic. Note The value is in the <Client ID> /<IP _ address> format. You cannot view the owner information about offline consumers. |
| Maximum site | The maximum consumer offset of the topic in the current partition. |
| Consumption point | The consumer offset of the topic in the current partition. |
| Accumulation | The total number of accumulated messages in the current partition. The value is calculated by using the following formula: Total number of accumulated messages = Maximum offset - Consumer offset. Note This parameter is a key metric. If a large number of messages are accumulated, consumers may be blocked or the consumption rate cannot keep up with the production rate. In this case, you need to analyze the consumer running status and improve the consumption speed. |

#### 2.5.3 Reset the consumer offset of a consumer group

**consumer group**

If you reset a consumer offset, the offset from which a consumer starts to consume messages is changed. You can reset the consumer offset to skip accumulated or undesired messages or consume messages stored after a point in time, regardless of whether the messages stored before this point in time are consumed.

**Prerequisites**

All consumers in the consumer group for which you want to reset the consumer offset are stopped.

> **Important:** ApsaraMQ for Kafka does not allow you to reset consumer offsets for online consumers.
> After you stop a consumer, the broker determines the consumer is stopped only after the time specified by the `ConsumerConfig.SESSION_TIMEOUT_MS_CONFIG` parameter elapses. Default value of the parameter: 10000 milliseconds.

**Background information**

ApsaraMQ for Kafka allows you to reset consumer offsets by using one of the following methods: Clear all accumulated messages: If you no longer want to consume accumulated messages on the broker, you can clear the messages for the consumer. This way, the consumer offset is set to the latest offset.

> **Important:** This method changes only the consumer offset. The accumulated messages are not deleted.

Start consumption at a specific point in time: You can reset the offset of a consumer group to a point in time "t" that is in the past or future. The point in time "t" is a point in time when a message is stored. After the reset, the consumer group subscribes to messages stored after the "t" time point.

**Procedure**

1. Log on to the ApsaraMQ for Kafka console.
2. In the left-side navigation pane, click **Instances**.
3. On the **Instance List** page, find the instance that you want to manage and click **Details** in
the **Operation** column.
4. On the **Instance details page**, click the **Group management** tab.
5. On the **Group management** tab, find the consumer group that you want to manage and
click **Reset consumption point** in the **Operation** column.
6. In the **Reset consumption point** dialog box, select the topic from the **Topic** drop-down
list, specify a method used to reset the consumer offset, and then click **OK**.

### 2.6 Configure instance parameters

**parameters**

This topic describes how to configure the parameters of an ApsaraMQ for Kafka instance. After you modify the parameters of an ApsaraMQ for Kafka instance, the running of the instance is affected. Confirm before you modify instance parameters.

**Procedure**

1. Log on to the ApsaraMQ for Kafka console.
2. On the **Instances** page, find the instance whose parameters you want to modify and click
**Parameter configuration** in the **Operation** column.
3. In the **Parameter configuration** panel, modify the parameters that are described in the
following table.

> **Warning:** The default configurations are optimal configurations. We recommend that you do not modify the default configurations unless necessary. The modification of the following parameters, except for the **log.retention.bytes** parameter, causes the restart of ApsaraMQ for Kafka. We recommend that you modify the parameters when your business is idle.

| Parameter | Description | Example |
|---|---|---|
| message.max.bytes | The maximum size of a message that the server can receive. You must configure the same setting for this parameter on the consumer and producer clients. Otherwise, a message published by the producer may be beyond the processing capability of the consumer. Specify a proper value for this parameter based on your business requirements. | 10000000 |
| num.partitions | The number of partitions of a topic. If you do not specify the number of partitions for a topic when you create the topic, the value of this parameter is used as the default value. | 3 |

| auto.create.topics.enable | Specifies whether to enable the automatic topic creation feature. After you enable the feature, a topic is automatically created if the topic does not exist but is specified for a produce or fetch request. If you do not enable this feature, you need to create a topic by using the CLI. | No |
|---|---|---|
| num.io.threads | The number of I/O threads used by a server to process requests. The value of this parameter must be greater than or equal to the number of disks. | 16 |
| queued.max.requests | The maximum number of requests that can be queued for processing by an I/O thread before a network thread stops receiving requests. | 80 |
| replica.fetch.wait.max.ms | The maximum period of time that the system can wait for the partition leader to respond to a request from a follower. If the request fails, the system automatically performs retries. Unit: milliseconds. | 500 |
| replica.lag.time.max.ms | The maximum period of time within which a follower must send a request to fetch data from the partition leader. If a follower does not send requests within this period of time, the follower is removed from the ISR list and is considered unavailable. Unit: milliseconds. | 30000 |
| num.network.threads | The number of network threads used by a server to process network requests. | 3 |

| log.retention.bytes | The maximum size of data that can be stored in each partition of a topic. Unit: bytes. The maximum data size of each topic is calculated by multiplying the value of this parameter by the total number of partitions of a topic. If you specify both the log.retention.hours parameter and this parameter, a log file is deleted when one of the thresholds specified by the parameters is exceeded. The setting of this parameter is overwritten if you configure the corresponding setting for a topic. | 4 |
|---|---|---|
| replica.fetch.max.bytes | The maximum size of data that can be obtained in each fetch request when the follower backs up data from the leader. Unit: bytes. | 10000000 |
| num.replica.fetchers | The number of threads used to back up data from the partition leader. | 4 |
| default.replication.factor | The default number of replicas for automatically created topics. | 3 |
| offsets.retention.minutes | The retention period of a committed offset. After the retention period of an offset elapses, the offset is marked by the system and is pending to be deleted. Unit: minutes. | 10080 |
| background.threads | The number of threads used for data processing in the background, such as deleting files. | 10 |

4. After you modify a parameter, click **Modify** in the **Operation** column of the parameter.
5. In the **Modify configuration** message, click **OK**.

### 2.7 Messages

#### 2.7.1 Send messages

After you create a topic, you can send messages to the topic in the ApsaraMQ for Kafka console.
1. Log on to the ApsaraMQ for Kafka console.
2. On the **Instance List** page, find the instance that you want to manage and click **Details** in
the **Operation** column.
3. On the **Instance details page**, click the **Topic management** tab.
4. On the **Topic management** tab, find the topic that you want to manage and click **Send**
**message** in the **Operation** column.
5. In the **Send message** panel, enter the ID of the partition from which you want to send a
message in the **Partition** field and the message key and message value in the **Message**
**Key** and **Message Value** fields. Then, click **OK**.

#### 2.7.2 Query messages

After you send a message, you can query the message.

**Background information**

ApsaraMQ for Kafka allows you to query messages by using one of the following methods: By offset: If you know the partition from which the message is sent and the consumer offset of the message, you can use this method to query the message. By time: If you do not know the partition from which the message is sent and the consumer offset of the message but know the time when the message is sent, you can use this method to query the message.

**Usage notes**

Up to 30 messages whose total size does not exceed 10 MB can be returned in a query result. A maximum of 1 KB of content can be displayed for each message. Content that exceeds 1 KB is automatically truncated. If you want to view the complete content of a message, download the message. Only messages that are not cleared by the broker can be queried. The following message cleanup policies are used on ApsaraMQ for Kafka brokers: If the disk usage is lower than 85%, expired messages are deleted at 04:00 every day. If the disk usage reaches 85%, expired messages are immediately deleted. If the disk usage reaches 90%, stored messages are deleted in the order that the messages were stored in the clients.

**Query a message by offset**

1. Log on to the ApsaraMQ for Kafka console.
2. On the **Instance List** page, find the instance that you want to manage and click **Details** in
the **Operation** column.
3. On the **Instance details page**, click the **Message query** tab.
4. On the **Message query** tab, click **Query by site**, enter or select the topic, partition, and
consumer offset, and then click **Query**. The queried message is displayed on the **Message query** tab.

| Parameter | Description |
|---|---|
| Partition | The partition in the topic from which the message is sent. |
| Site | The consumer offset of the message. |
| Time | The time when the message is stored on the broker. |
| Key(size: 1B) | The message key. The key is transformed into a string. |
| Value(size: 1B) | The message value. The value is transformed into a string. |

5. **(Optional)** If you want to download the key or value of a message, select the message and
click **Download message** next to **Key** or **Value**.

**Query a message by time**

1. Log on to the ApsaraMQ for Kafka console.
2. On the **Instance List** page, find the instance that you want to manage and click **Details** in
the **Operation** column.
3. On the **Instance details page**, click the **Message query** tab.
4. On the **Message query** tab, click **Query by time**, enter or select the topic, partition, and
time, and then click **Query**. The queried message is displayed on the **Message query** tab.

| Parameter | Description |
|---|---|
| Partition | The partition in the topic from which the message is sent. |
| Site | The consumer offset of the message. |
| Time | The time when the message is stored on the broker. |
| Key(size: 1B) | The message key. The key is transformed into a string. |
| Value(size: 1B) | The message value. The value is transformed into a string. |

5. **(Optional)** If you want to download the key or value of a message, select the message and
click **Download message** next to **Key** or **Value**.

### 2.8 ACL

#### 2.8.1 Enable ACL

The access control list (ACL) feature of ApsaraMQ for Kafka allows you to grant permissions to Simple Authentication and Security Layer (SASL) users to send and receive messages in ApsaraMQ for Kafka. This topic describes how to enable the ACL feature for an ApsaraMQ for Kafka instance.

**Usage notes**

After you enable the ACL feature for an ApsaraMQ for Kafka instance, ApsaraMQ for Kafka is restarted. Before you enable the ACL feature, make sure that this operation does not affect your business.

**Prerequisites**

A virtual IP address (VIP) is created. For more information, see Create VIPs.

**Procedure**

1. Log on to the ApsaraMQ for Kafka console.
2. In the left-side navigation pane, click **Instances**.
3. On the **Instances** page, find the instance that you want to manage and click **Details** in the
**Operation** column.
4. In the upper-right corner of the **Basic information** section of the **Instance details** tab,
click **Enable ACL**.
5. In the **Alert** message, click **OK**.

#### 2.8.2 Create SASL users

This topic describes how to create a Simple Authentication and Security Layer (SASL) user.

**Prerequisites**

The ACL feature is enabled for the ApsaraMQ for Kafka instance. For more information, see Enable ACL.

**Procedure**

1. Log on to the ApsaraMQ for Kafka console.
2. In the left-side navigation pane, click **Instances**.
3. On the **Instance List** page, find the instance that you want to manage and click **Details** in
the **Operation** column.
4. Click the **SASL user** tab.
5. On the **SASL User** tab, click **Create a SASL user** .
6. In the **Create a SASL user** dialog box, configure the parameters and click **OK**. The
following table describes the parameters.

| Parameter | Description |
|---|---|

| Username | The name of the SASL user. |
|---|---|
| Password | The password of the SASL user. |
| Type | The type of the SASL user. ApsaraMQ for Kafka supports the following SASL mechanism: SCRAM: a username and password verification mechanism that provides higher security than PLAIN. ApsaraMQ for Kafka uses SCRAM-SHA- 256. |

#### 2.8.3 Grant permissions to SASL users

This topic describes how to grant permissions to a Simple Authentication and Security Layer (SASL) user.

**Prerequisites**

A SASL user is created. For more information, see Create SASL users.

**Procedure**

1. Log on to the ApsaraMQ for Kafka console.
2. In the left-side navigation pane, click **Instances**.
3. On the **Instance List** page, find the instance that you want to manage and click **Details** in
the **Operation** column.
4. Click the **SASL permissions** tab.
5. On the **SASL permissions** tab, click **Create an ACL**.
6. In the **Create an ACL** dialog box, configure the parameters and click **OK**. The following
table describes the parameters.

| Parameter | Description |
|---|---|
| Username | The name of the SASL user. Note ApsaraMQ for Kafka supports the use of asterisks (*) as wildcard characters. You can use an asterisk (*) to specify all usernames. |

| Resource type | The resource type. Valid values: Topic: a topic. Group: a consumer group. |
|---|---|
| Matching pattern | The mode in which resources are matched. Valid values: Full match: matches resources by literal value. In this mode, only resources with the same name are matched. Prefix matching: matches resources by prefix. In this mode, resource names that start with the specified prefix are matched. |
| Operation type | The type of the operation that the SASL user can perform on the resources. Write: writes data. Read: reads data. Important If you set the Resource type parameter to Group, you must set the Operation type parameter to Read. |
| Resource Name | The resource name. The value can be the name of a topic or a consumer group. Note ApsaraMQ for Kafka supports the use of asterisks (*) as wildcard characters. You can use an asterisk (*) to specify all resource names. |

#### 2.8.4 Change the passwords of SASL users

This topic describes how to change the password of a Simple Authentication and Security Layer (SASL) user.

**Prerequisites**

A SASL user is created. For more information, see Create SASL users.

**Procedure**

1. Log on to the ApsaraMQ for Kafka console.
2. In the left-side navigation pane, click **Instances**.
3. On the **Instance List** page, find the instance that you want to manage and click **Details** in
the **Operation** column.
4. Click the **SASL user** tab.
5. On the **SASL user** tab, find the SASL user whose password you want to change and click
**Modify** in the **Operation** column.
6. In the **Modify SASL users** dialog box, enter a new password and click **OK**.

#### 2.8.5 Delete SASL users

This topic describes how to delete a Simple Authentication and Security Layer (SASL) user.

**Prerequisites**

A SASL user is created. For more information, see Create SASL users.

**Procedure**

1. Log on to the ApsaraMQ for Kafka console.
2. In the left-side navigation pane, click **Instances**.
3. On the **Instance List** page, find the instance that you want to manage and click **Details** in
the **Operation** column.
4. Click the **SASL user** tab.
5. On the **SASL user** tab, find the SASL user that you want to delete and click **Delete** in the
**Operation** column.
6. In the **Delete SASL user** message, click **OK**.

#### 2.8.6 Delete the permissions of SASL users

This topic describes how to delete the permissions that are granted to a Simple Authentication and Security Layer (SASL) user.

**Prerequisites**

Permissions are granted to the SASL user. For more information, see Grant permissions to SASL users.

**Procedure**

1. Log on to the ApsaraMQ for Kafka console.
2. In the left-side navigation pane, click **Instances**.
3. On the **Instance List** page, find the instance that you want to manage and click **Details** in
the **Operation** column.
4. Click the **SASL permissions** tab.
5. On the **SASL permissions** tab, specify the query conditions to query the permissions that
you want to delete and click **Query**.
6. In the query result, find the permissions that you want to delete and click **Delete** in the
**Operation** column.
7. In the **Delete ACL** message, click **OK**.

### 2.9 VIPs

#### 2.9.1 Create VIPs

This topic describes how to create a virtual IP address (VIP).
1. Log on to the ApsaraMQ for Kafka console.
2. In the left-side navigation pane, click **Instances**.
3. On the **Instance List** page, find the instance that you want to manage and click **Details** in
4. On the **Access point information** tab of the **Instance details** page, click **Create**.
5. On the **Create VIP Information** page, perform the following operations:
If you want to create a VIP of the AnyTunnel type, set the **Network Type** parameter to AnyTunnel and click **Submit**. If you want to create a VIP of the SingleTunnel type, set the **Network Type** parameter to SingleTunnel, specify the ID of the virtual private cloud (VPC) in the **VPC** field and the ID of the vSwtich in the **VSwitch** field, and then click **Submit**. To create a VIP, you must update the network of ApsaraMQ for Kafka and restart ApsaraMQ for Kafka. The estimated time to create a VIP is calculated by using the following formula: Estimated time in minutes = Number of ApsaraMQ for Kafka nodes × 10.

#### 2.9.2 Delete VIPs

This topic describes how to delete a virtual IP address (VIP).

**Procedure**

1. Log on to the ApsaraMQ for Kafka console.
2. In the left-side navigation pane, click **Instances**.
3. On the **Instance List** page, find the instance that you want to manage and click **Details** in
the **Operation** column.
4. On the **Access point information** tab of the **Instance details** page, click **Delete**.
5. In the **Confirm deletion** dialog box, enter
`confirm` and click **OK**.

> **Important:** After you delete a VIP, the ApsaraMQ for Kafka instance becomes unavailable. Exercise caution when you delete a VIP.

### 2.10 Zone-disaster recovery

#### 2.10.1 Solution introduction

ApsaraMQ for Kafka provides zone-disaster recovery capabilities for financial business that has high data stability and regulatory requirements.

**Description**

In the zone-disaster recovery solution provided by ApsaraMQ for Kafka, a primary cluster and a secondary cluster are deployed in two data centers that reside in the same zone. The primary cluster provides external services, and the KafkaReplicator component synchronizes data from the primary cluster to the secondary cluster. If both clusters run as expected, all data in the primary cluster, including messages and consumer offsets, are backed up to the secondary cluster. When faults, such as business cannot be restored in a short period of time due to damaged software or hardware and the data center is rebuilt due to a fire or natural disaster, occur in the primary cluster, you can use the ApsaraMQ for Kafka console or the Application Service Registration (ASR) mechanism to switch business from the primary cluster to the secondary cluster to provide external services.

**Architecture**

The following figure describes the zone-disaster recovery solution in which two ApsaraMQ for Kafka clusters are deployed. Architecture description: An ApsaraMQ for Kafka cluster and a KafkaReplicator database cluster are deployed in Data Center A and Data Center B, respectively. The KafkaReplicator component synchronizes data from Data Center A to Data Center B to ensure data consistency. When a fault occurs in Data Center A, the business of Data Center A is switched to Data Center B. In this case, the domain name used to access the business remains unchanged.

**Usage limits**

After you create a zone-disaster recovery cluster, you must change the virtual IP address (VIP) of the application client to the domain name of the zone-disaster recovery cluster. Otherwise, you cannot connect to the zone-disaster recovery cluster during disaster recovery switchover.

#### 2.10.2 Create replica clusters

This topic describes how to create a replica cluster and establish a replication relationship to provide disaster recovery capabilities by using ApsaraMQ for Kafka instances.

**Prerequisites**

Two ApsaraMQ for Kafka instances are deployed. One of the instances is used in production environments and the other is used in zone-disaster recovery environments. Make sure that KafkaReplicator is deployed in the clusters to which the instances belong. If KafkaReplicator is not deployed, contact ApsaraMQ for Kafka technical support to deploy it.
1. Log on to the ApsaraMQ for Kafka console.
2. In the left-side navigation pane, click **Replica Clusters**.
3. On the **Disaster Recovery** page, click **Create a disaster recovery cluster**.

> **Note:** If no cluster is created, you can also click **Create** in the cluster list area to create a replica cluster.

4. On the wizard that appears, perform the following operations:
i. In the Configure Basic information step, enter the name of the replica cluster in the
**Disaster recovery cluster name** field. Then, click **Next**.

> **Note:** The name of the replica cluster must meet the following rules:
> The name can contain only letters, digits, hyphens (-), and underscores (_).
> The name must be 3 to 20 characters in length. If the name exceeds 20 characters in length, the name is automatically truncated.
> You cannot change the name of the replica cluster after the replica cluster is created.

ii. In the **Configure Source Service** step, specify the information about the source instances and click **Next**. iii. In the **Configure Target Service** step, specify the information about the destination instances and click **Next**. In the Confirmation step, confirm the information and click
**Create**.
After a replica cluster is created, you can view the replica cluster in the **Disaster Recovery** page.

> **Note:** You cannot use instances that are used to create a replica cluster as the source or destination instances to create another replica cluster.

**Switch to the secondary cluster**

When faults occur in the primary cluster, you can switch business in the primary cluster to the secondary cluster to prevent business interruption.

> **Important:** During the switchover, the network is switched. As a result, temporary disconnection can occur on the client. Confirm before you perform the switchover.

1. Log on to the ApsaraMQ for Kafka console.
2. In the left-side navigation pane, click **Replica Clusters**.
3. On the **Disaster Recovery** page, find the replica cluster that you want to manage and click
**Disaster recovery switchover** in the **Operation** column.
4. In the **Disaster recovery switchover** dialog box, select the primary cluster that you want
to switch and click **OK**.

**Delete a replica cluster**

If you no longer require disaster recovery capabilities, you can delete the replica cluster.

> **Important:** After you delete a replica cluster, synchronization tasks that are running are stopped and deleted. The primary and secondary clusters no longer provide disaster recovery capabilities. Deleted clusters cannot be recovered. Proceed with caution.

1. Log on to the ApsaraMQ for Kafka console.
2. In the left-side navigation pane, click **Replica Clusters**.
3. On the **Disaster Recovery** page, find the replica cluster that you want to manage and click
**Delete** in the **Operation** column.
4. In the message that appears, click **OK**.
ions

## 3 Pod command operations

### 3.1 Command verification

#### 3.1.1 Create topics

This topic describes how to create a topic.

**Prerequisites**

The information about the master node in ApsaraMQ for Kafka is obtained.

**Procedure**

1. Connect to the master node in ApsaraMQ for Kafka.
2. Run the `kubectl exec -it <pod> bash` to connect to the pod in ApsaraMQ for Kafka.

| mple, if the name of the pod is | alibaba-kafka-cluster-private-paas-default-0 |   |
|---|---|---|
| kubectl exec -it alibaba-kafka-cluster-private-paas-default-0 bash |   |   |
|   |   | comma |

3. Run the `sudo su admin` command to switch to the administrator account.

```
4. Run the  sh /home/admin/KafkaProxy/bin/kafka-topics.sh --create --bootstrap-server
`hostname -i`:9092 --topic test --replication-factor 3 --partitions 12 command to
```

create a topic.

**Execution result**

| sh /home/admin/KafkaProxy/bin/kafka-topics.sh --list --bootstrap-server |   |
|---|---|
|   | command to view the list of topics. |

Sample output:

```
__consumer_offsets test
```

> **Note:** The ___consumer_offsets topic is automatically created by the system. The topic is used to store offsets committed by each topic.

#### 3.1.2 Send messages

This topic describes how to send messages to a topic.

**Prerequisites**

The information about the master node in ApsaraMQ for Kafka is obtained.

**Background information**

ApsaraMQ for Kafka allows you to send messages by using the PLAINTEXT protocol.

**PLAINTEXT**

1. Connect to the master node in ApsaraMQ for Kafka.
ions
2. Run the `kubectl exec -it <pod> bash` to connect to the pod in ApsaraMQ for Kafka.

| mple, if the name of the pod is | alibaba-kafka-cluster-private-paas-default-0 |   |
|---|---|---|
| kubectl exec -it alibaba-kafka-cluster-private-paas-default-0 bash |   |   |
|   |   | comma |

3. Run the `sudo su admin` command to switch to the administrator account.
4. Send messages on port 9092 by using PLAINTEXT.

```
Run the java -jar /home/admin/kafka-pkgs/KafkaChecker.jar send -s `hostname -i`:9092
```

`-t test` command to directly send messages.

```
Run the java -Dlog4j.configuration=file:/home/admin/kafka-pkgs/log4j.properties -jar /home/admin/kafka-pkgs/KafkaChecker.jar send -s `hostname -i`:9092 -t test command
```

to send messages by enabling logging for debugging.

#### 3.1.3 Consume messages

This topic describes how to consume messages from a topic.

**Prerequisites**

The information about the master node in ApsaraMQ for Kafka is obtained.

**Background information**

ApsaraMQ for Kafka allows you to consume messages by using PLAINTEXT protocol.

**PLAINTEXT**

1. Connect to the master node in ApsaraMQ for Kafka.
2. Run the `kubectl exec -it <pod> bash` to connect to the pod in ApsaraMQ for Kafka.

| mple, if the name of the pod is | alibaba-kafka-cluster-private-paas-default-0 |   |
|---|---|---|
| kubectl exec -it alibaba-kafka-cluster-private-paas-default-0 bash |   |   |
|   |   | comma |

3. Run the `sudo su admin` command to switch to the administrator account.
4. Consume messages on port 9092 by using PLAINTEXT.

```
Run the sh /home/admin/KafkaProxy/bin/kafka-console-consumer.sh --from-beginning -topic test --group CID_test --bootstrap-server `hostname -i`:9092 command to
```

consume messages by using scripts.

```
Run the java -jar /home/admin/kafka-pkgs/KafkaChecker.jar consume -s `hostname -
```

i`:9092 --offsetReset earliest --printAll true command to consume messages by using the JAR tool.

```
Run the java -Dlog4j.configuration=file:/home/admin/kafka-pkgs/log4j.properties -jar /home/admin/kafka-pkgs/KafkaChecker.jar consume -s `hostname -i`:9092 --offsetReset
```

`earliest --printAll true` command to consume messages by enabling logging for debugging.

### 3.2 Topics

#### 3.2.1 Create topics

This topic describes how to create a topic. ions The information about the master node in ApsaraMQ for Kafka is obtained.
1. Connect to the master node in ApsaraMQ for Kafka.
2. Run the `kubectl exec -it <pod> bash` to connect to the pod in ApsaraMQ for Kafka.

| mple, if the name of the pod is | alibaba-kafka-cluster-private-paas-default-0 |   |
|---|---|---|
| kubectl exec -it alibaba-kafka-cluster-private-paas-default-0 bash |   |   |
|   |   | comma |

3. Run the `sudo su admin` command to switch to the administrator account.

```
4. Run the  sh /home/admin/KafkaProxy/bin/kafka-topics.sh --create --bootstrap-server
`hostname -i`:9092 --topic test --replication-factor 3 --partitions 12 command to
```

create a topic.

**Execution result**

| sh /home/admin/KafkaProxy/bin/kafka-topics.sh --list --bootstrap-server |   |
|---|---|
|   | command to view the list of topics. |

Sample output:

```
__consumer_offsets test
```

> **Note:** The ___consumer_offsets topic is automatically created by the system. The topic is used to store offsets committed by each topic.

#### 3.2.2 View the status of a topic

This topic describes how to view the status of a topic.

**Prerequisites**

The information about the master node in ApsaraMQ for Kafka is obtained.

**Procedure**

1. Connect to the master node in ApsaraMQ for Kafka.
2. Run the `kubectl exec -it <pod> bash` to connect to the pod in ApsaraMQ for Kafka.

| mple, if the name of the pod is | alibaba-kafka-cluster-private-paas-default-0 |   |
|---|---|---|
| kubectl exec -it alibaba-kafka-cluster-private-paas-default-0 bash |   |   |
|   |   | comma |

3. Run the `sudo su admin` command to switch to the administrator account.

```
4. Run the  sh /home/admin/KafkaProxy/bin/kafka-topics.sh --describe --bootstrap-server
```

`hostname -i`:9092 --topic test command to view the status of the topic. Sample output: ions

```
Topic:test PartitionCount:12 ReplicationFactor:3 Configs:min.insync.replicas=1,flush.ms=1000,segment.bytes=268435456,retention.ms=864000 ,flush.messages=10000,max.message.bytes=10000000,unclean.leader.election.enable=false
        Topic: test     Partition: 0    Leader: 1003    Replicas: 1003,1002,1001
Isr: 1001,1003,1002
        Topic: test     Partition: 1    Leader: 1002    Replicas: 1002,1001,1003
Isr: 1003,1002,1001
        Topic: test     Partition: 2    Leader: 1001    Replicas: 1001,1003,1002
Isr: 1003,1002,1001
        Topic: test     Partition: 3    Leader: 1003    Replicas: 1003,1001,1002
Isr: 1001,1003,1002
        Topic: test     Partition: 4    Leader: 1002    Replicas: 1002,1003,1001
Isr: 1003,1002,1001
        Topic: test     Partition: 5    Leader: 1001    Replicas: 1001,1002,1003
Isr: 1003,1002,1001
        Topic: test     Partition: 6    Leader: 1003    Replicas: 1003,1002,1001
Isr: 1001,1003,1002
        Topic: test     Partition: 7    Leader: 1002    Replicas: 1002,1001,1003
Isr: 1003,1002,1001
        Topic: test     Partition: 8    Leader: 1001    Replicas: 1001,1003,1002
Isr: 1003,1002,1001
        Topic: test     Partition: 9    Leader: 1003    Replicas: 1003,1001,1002
Isr: 1001,1003,1002
        Topic: test     Partition: 10   Leader: 1002    Replicas: 1002,1003,1001
Isr: 1003,1002,1001
        Topic: test     Partition: 11   Leader: 1001    Replicas: 1001,1002,1003
Isr: 1003,1002,1001
```

#### 3.2.3 View the current offset of a partition

The current offset of a partition is the latest message that is sent to the consumer by the ApsaraMQ for Kafka broker. This topic describes how to view the current offset of a partition.

**Prerequisites**

The information about the master node in ApsaraMQ for Kafka is obtained.

**Procedure**

1. Connect to the master node in ApsaraMQ for Kafka.
2. Run the `kubectl exec -it <pod> bash` to connect to the pod in ApsaraMQ for Kafka.

| mple, if the name of the pod is | alibaba-kafka-cluster-private-paas-default-0 |   |
|---|---|---|
| kubectl exec -it alibaba-kafka-cluster-private-paas-default-0 bash |   |   |
|   |   | comma |

3. Run the `sudo su admin` command to switch to the administrator account.

```
4. Run the  java -jar /home/admin/kafka-pkgs/KafkaMetricChecker.jar object -o
kafka.log:name=LogEndOffset,partition=<partition id>,topic=<topic>,type=Log command
```

to view the current offset of the partition.

| test | , the ID of the partition is | 9 | , run the |
|---|---|---|---|

```
-jar /home/admin/kafka-pkgs/KafkaMetricChecker.jar object -o kafka.log:name=LogEndOffset,partition=9,topic=test,type=Lo command.
```

Sample output: ions

```
Value 16761
```

#### 3.2.4 View the list of topics

This topic describes how to view the list of topics.

**Prerequisites**

The information about the master node in ApsaraMQ for Kafka is obtained.

**Procedure**

1. Connect to the master node in ApsaraMQ for Kafka.
2. Run the `kubectl exec -it <pod> bash` to connect to the pod in ApsaraMQ for Kafka.

| mple, if the name of the pod is | alibaba-kafka-cluster-private-paas-default-0 |   |
|---|---|---|
| kubectl exec -it alibaba-kafka-cluster-private-paas-default-0 bash |   |   |
|   |   | comma |

3. Run the `sudo su admin` command to switch to the administrator account.

```
4. Run the  sh /home/admin/KafkaProxy/bin/kafka-topics.sh --list --bootstrap-server
```

`hostname -i`:9092 command to view the list of topics. Sample output:

```
CMDTest __consumer_offsets demo test test1 test2
```

#### 3.2.5 Increase the number of partitions in a topic

**topic**

After you create a topic, you can increase the number of partitions in the topic. ApsaraMQ for Kafka does not allow you to decrease the number of partitions in a topic. If you want to decrease the number of partitions in a topic, you can delete the topic and create another topic that has the required number of partitions.

**Prerequisites**

The information about the master node in ApsaraMQ for Kafka is obtained.

**Procedure**

1. Connect to the master node in ApsaraMQ for Kafka.
2. Run the `kubectl exec -it <pod> bash` to connect to the pod in ApsaraMQ for Kafka.

| mple, if the name of the pod is | alibaba-kafka-cluster-private-paas-default-0 |   |
|---|---|---|
| kubectl exec -it alibaba-kafka-cluster-private-paas-default-0 bash |   |   |
|   |   | comma |

3. Run the `sudo su admin` command to switch to the administrator account.
ions

```
4. Run the  sh /home/admin/KafkaProxy/bin/kafka-topics.sh -alter --bootstrap-server
`hostname -i`:9092 --topic <topic> --partitions <total partition number> command to
```

increase the number of partitions in a topic. For example, if you want to increase the number of partitions by 6 for the test topic that has 12 partitions, run the `sh /home/admin/KafkaProxy/bin/kafka-topics.sh -alter --`

```
bootstrap-server `hostname -i`:9092 --topic test --partitions 18 command.
```

Sample output:

```
Topic:test PartitionCount:18 ReplicationFactor:3 Configs:min.insync.replicas=1,flush.ms=1000,segment.bytes=268435456,retention.ms=864000 ,flush.messages=10000,max.message.bytes=10000000,unclean.leader.election.enable=false
        Topic: test     Partition: 0    Leader: 1003    Replicas: 1003,1002,1001
Isr: 1001,1003,1002
        Topic: test     Partition: 1    Leader: 1002    Replicas: 1002,1001,1003
Isr: 1003,1002,1001
        Topic: test     Partition: 2    Leader: 1001    Replicas: 1001,1003,1002
Isr: 1003,1002,1001
        Topic: test     Partition: 3    Leader: 1003    Replicas: 1003,1001,1002
Isr: 1001,1003,1002
        Topic: test     Partition: 4    Leader: 1002    Replicas: 1002,1003,1001
Isr: 1003,1002,1001
        Topic: test     Partition: 5    Leader: 1001    Replicas: 1001,1002,1003
Isr: 1003,1002,1001
        Topic: test     Partition: 6    Leader: 1003    Replicas: 1003,1002,1001
Isr: 1001,1003,1002
        Topic: test     Partition: 7    Leader: 1002    Replicas: 1002,1001,1003
Isr: 1003,1002,1001
        Topic: test     Partition: 8    Leader: 1001    Replicas: 1001,1003,1002
Isr: 1003,1002,1001
        Topic: test     Partition: 9    Leader: 1003    Replicas: 1003,1001,1002
Isr: 1001,1003,1002
        Topic: test     Partition: 10   Leader: 1002    Replicas: 1002,1003,1001
Isr: 1003,1002,1001
        Topic: test     Partition: 11   Leader: 1001    Replicas: 1001,1002,1003
Isr: 1003,1002,1001
        Topic: test     Partition: 12   Leader: 1003    Replicas: 1003,1002,1001
Isr: 1003,1002,1001
        Topic: test     Partition: 13   Leader: 1001    Replicas: 1001,1003,1002
Isr: 1001,1003,1002
        Topic: test     Partition: 14   Leader: 1002    Replicas: 1002,1001,1003
Isr: 1002,1001,1003
        Topic: test     Partition: 15   Leader: 1003    Replicas: 1003,1001,1002
Isr: 1003,1001,1002
        Topic: test     Partition: 16   Leader: 1001    Replicas: 1001,1002,1003
Isr: 1001,1002,1003
        Topic: test     Partition: 17   Leader: 1002    Replicas: 1002,1003,1001
Isr: 1002,1003,1001
```

#### 3.2.6 Modify topic configurations

If the configurations of a topic do not meet your business requirements, you can modify the configurations of the topic. ions The information about the master node in ApsaraMQ for Kafka is obtained.

**Procedure**

1. Connect to the master node in ApsaraMQ for Kafka.
2. Run the `kubectl exec -it <pod> bash` to connect to the pod in ApsaraMQ for Kafka.

| mple, if the name of the pod is | alibaba-kafka-cluster-private-paas-default-0 |   |
|---|---|---|
| kubectl exec -it alibaba-kafka-cluster-private-paas-default-0 bash |   |   |
|   |   | comma |

3. Run the `sudo su admin` command to switch to the administrator account.

```
4. Run the  cat /home/admin/kafka-config/server.properties | grep zookeeper.connect
```

command to view the connection information about ZooKeeper. Sample output:

```
zookeeper.connect=10.XX.XX.145:2188,10.XX.XX.143:2188,10.XX.XX.181:2188/kafka-private -clusters/cluster-private-paas-default zookeeper.connection.timeout.ms=36000
5. Run the  sh /home/admin/KafkaProxy/bin/kafka-configs.sh --zookeeper <zk connect> --
```

`describe --entity-name <topic> --entity-type topics` command to view the configurations of the topic. For example, if the URL of a ZooKeeper connection is

```
 10.XX.XX.183:2188,10.XX.XX.182:2188,10.XX.XX.181:2188/kafka-private-clusters/cluster-
```

|   |   | and the name of the topic is | test | , run the |
|---|---|---|---|---|

```
/home/admin/KafkaProxy/bin/kafka-configs.sh --zookeeper 10.XX.XX.183:2188,10.XX.XX.182:2188,10.XX.XX.181:2188/kafka-private-clusters/clusterprivate-paas-default --describe --entity-name test --entity-type topics command.
```

Sample output:

```
Configs for topic 'test' are retention.ms=86400000,min.insync.replicas=1,max.message.bytes=1000000
6. Run the  sh /home/admin/KafkaProxy/bin/kafka-configs.sh -zookeeper <zk connect> --alter
--add-config <config kv> --entity-name <topic> --entity-type topics command to
```

modify the configurations of the topic. For example, if the URL of a ZooKeeper connection is

```
 10.XX.XX.183:2188,10.XX.XX.182:2188,10.XX.XX.181:2188/kafka-private-clusters/cluster-
```

|   |   |   | , the name of the topic is | test |
|---|---|---|---|---|
| 1000000 | , run the |   |   |   |

```
10.XX.XX.183:2188,10.XX.XX.182:2188,10.XX.XX.181:2188/kafka-private-clusters/clusterprivate-paas-default --alter --add-config max.message.bytes=10000000 --entity-name test
```

| command to change the maximum message size to | 10000000 |
|---|---|

Sample output:

```
Completed Updating config for entity: topic 'test'.
```

| Parameter | Description |
|---|---|

ions

| min.insync.replicas | The minimum number of synchronized replicas. Valid values: 1 to 3. Recommended value: 1. The minimum number of synchronized replicas must be smaller than or equal to the number of replicas. The minimum number of synchronized replicas defines the minimum number of replicas from which the system receives acknowledgments to determine the successful writing of a message. The minimum number of replicas is valid only if the producer sets message acknowledgment to All or -1. |
|---|---|
| retention.ms | The period of time for which messages are retained in a topic. Valid values: 1 to 168. Unit: hours. |
| max.message.bytes | The maximum size of a message that the topic can receive from a producer. Valid values: 1 to 10. Unit: MB. |

### 3.3 Consumer groups

#### 3.3.1 View the consumer status of a consumer group

**consumer group**

This topic describes how to view the consumer status of a consumer group.

**Prerequisites**

The information about the master node in ApsaraMQ for Kafka is obtained.

**Procedure**

1. Connect to the master node in ApsaraMQ for Kafka.
2. Run the `kubectl exec -it <pod> bash` to connect to the pod in ApsaraMQ for Kafka.

| mple, if the name of the pod is | alibaba-kafka-cluster-private-paas-default-0 |   |
|---|---|---|
| kubectl exec -it alibaba-kafka-cluster-private-paas-default-0 bash |   |   |
|   |   | comma |

3. Run the `sudo su admin` command to switch to the administrator account.

```
4. Run the  sh /home/admin/KafkaProxy/bin/kafka-consumer-groups.sh --bootstrap-server
```

`hostname -i`:9092 --group <group> --describe command to view the consumer status of the consumer group. For example, if you want to view the consumer status of a consumer group named

| CID test _ | , run the |   |
|---|---|---|

```
bootstrap-server `hostname -i`:9092 --group CID_test --describe command.
```

Sample output: ions

```
Consumer group 'CID_test' has no active members. TOPIC PARTITION CURRENT-OFFSET LOG-END-OFFSET LAG CONSUMER-ID HOST CLIENT-ID test 6 16653 16653 0 -
-               -
test 11 16740 16740 0 -
-               -
test 10 16608 16608 0 -
-               -
test 0 16735 16735 0 -
-               -
test 7 16603 16603 0 -
-               -
test 5 16772 16772 0 -
-               -
test 8 16816 16816 0 -
-               -
test 1 16712 16712 0 -
-               -
test 4 16797 16797 0 -
-               -
test 9 16761 16761 0 -
-               -
test 3 16670 16670 0 -
-               -
test 2 16516 16516 0 -
-               -
```

#### 3.3.2 View the list of consumer groups

This topic describes how to view the list of consumer groups.

**Prerequisites**

The information about the master node in ApsaraMQ for Kafka is obtained.

**Procedure**

1. Connect to the master node in ApsaraMQ for Kafka.
2. Run the `kubectl exec -it <pod> bash` to connect to the pod in ApsaraMQ for Kafka.

| mple, if the name of the pod is | alibaba-kafka-cluster-private-paas-default-0 |   |
|---|---|---|
| kubectl exec -it alibaba-kafka-cluster-private-paas-default-0 bash |   |   |
|   |   | comma |

3. Run the `sudo su admin` command to switch to the administrator account.

```
4. Run the  sh /home/admin/KafkaProxy/bin/kafka-consumer-groups.sh --list --bootstrap-
```

server `hostname -i`:9092 command to view the list of consumer groups. Sample output:

```
CID_test
```

ions

### 3.4 Messages

#### 3.4.1 Send messages

This topic describes how to send messages to a topic.

**Prerequisites**

The information about the master node in ApsaraMQ for Kafka is obtained.

**Background information**

ApsaraMQ for Kafka allows you to send messages by using the PLAINTEXT protocol.

**PLAINTEXT**

1. Connect to the master node in ApsaraMQ for Kafka.
2. Run the `kubectl exec -it <pod> bash` to connect to the pod in ApsaraMQ for Kafka.

| mple, if the name of the pod is | alibaba-kafka-cluster-private-paas-default-0 |   |
|---|---|---|
| kubectl exec -it alibaba-kafka-cluster-private-paas-default-0 bash |   |   |
|   |   | comma |

3. Run the `sudo su admin` command to switch to the administrator account.
4. Send messages on port 9092 by using PLAINTEXT.

| java -jar /home/admin/kafka-pkgs/KafkaChecker.jar send -s `hostname -i`:9092 |   |
|---|---|
|   | command to directly send messages. |

```
Run the java -Dlog4j.configuration=file:/home/admin/kafka-pkgs/log4j.properties -jar /home/admin/kafka-pkgs/KafkaChecker.jar send -s `hostname -i`:9092 -t test command
```

to send messages by enabling logging for debugging.

#### 3.4.2 Consume messages

This topic describes how to consume messages from a topic.

**Prerequisites**

The information about the master node in ApsaraMQ for Kafka is obtained.

**Background information**

ApsaraMQ for Kafka allows you to consume messages by using PLAINTEXT protocol.

**PLAINTEXT**

1. Connect to the master node in ApsaraMQ for Kafka.
2. Run the `kubectl exec -it <pod> bash` to connect to the pod in ApsaraMQ for Kafka.

| mple, if the name of the pod is | alibaba-kafka-cluster-private-paas-default-0 |   |
|---|---|---|
| kubectl exec -it alibaba-kafka-cluster-private-paas-default-0 bash |   |   |
|   |   | comma |

3. Run the `sudo su admin` command to switch to the administrator account.
4. Consume messages on port 9092 by using PLAINTEXT.

```
Run the sh /home/admin/KafkaProxy/bin/kafka-console-consumer.sh --from-beginning -topic test --group CID_test --bootstrap-server `hostname -i`:9092 command to
```

consume messages by using scripts. ions

```
Run the java -jar /home/admin/kafka-pkgs/KafkaChecker.jar consume -s `hostname -
```

i`:9092 --offsetReset earliest --printAll true command to consume messages by using the JAR tool.

```
Run the java -Dlog4j.configuration=file:/home/admin/kafka-pkgs/log4j.properties -jar /home/admin/kafka-pkgs/KafkaChecker.jar consume -s `hostname -i`:9092 --offsetReset
```

`earliest --printAll true` command to consume messages by enabling logging for debugging.
