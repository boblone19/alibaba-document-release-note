---
title: "Message Queue for Apache Kafka User Guide 20260629"
product_version: "V3.18.6"
pdf_pages: 160
source_pdf: "dd9919bd166fc0f6_Alibaba Cloud Apsara Stack V3.18.6 Message Queue for Apache Kafka User Guide 20260629.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/v3.18.6%E7%89%88%E6%9C%AC%E6%96%87%E6%A1%A3/%E6%B6%88%E6%81%AF%E9%98%9F%E5%88%97Kafka%E7%89%88%20/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.6%20Message%20Queue%20for%20Apache%20Kafka%20User%20Guide%2020260629.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes)
---

# Message Queue for Apache Kafka User Guide 20260629

## Table of Contents

- 1 What is ?
- 2 Console operations
  - 2.1 Log on to the console
  - 2.2 Getting started
    - 2.2.1 Create a topic
    - 2.2.2 Send messages
    - 2.2.3 Query messages
  - 2.3 Instances
    - 2.3.1 Manage instances
    - 2.3.2 Configure instance relationships
    - 2.3.3 Obtain the endpoint of an instance
    - 2.3.4 Configure instance parameters
    - 2.3.5 View the instance monitoring information
    - 2.3.6 View the operation logs of an instance
  - 2.4 Topics
    - 2.4.1 Create topics
    - 2.4.2 View the list of topics
    - 2.4.3 View partition status in a topic
    - 2.4.4 View the subscriptions of a topic
    - 2.4.5 Modify topic configurations
    - 2.4.6 Increase the number of partitions in a topic
    - 2.4.7 Migrate topic partitions
  - 2.5 Consumer groups
    - 2.5.1 Create a consumer group
    - 2.5.2 View the list of consumer groups
    - 2.5.3 View the consumer status of a consumer group
    - 2.5.4 Reset the consumer offset of a consumer group
  - 2.6 Messages
    - 2.6.1 Send messages
    - 2.6.2 Query messages
  - 2.7 ACL
    - 2.7.1 Create SASL users
    - 2.7.2 Grant permissions to SASL users
    - 2.7.3 Configure an ACL
    - 2.7.4 Change the passwords of SASL users
    - 2.7.5 Delete SASL users
    - 2.7.6 Delete the permissions of SASL users
    - 2.7.7 Download an ACL certificate
  - 2.8 VIPs
    - 2.8.1 Create a VIP
    - 2.8.2 Delete a VIP
    - 2.8.3 Request a domain name
  - 2.9 Data integration
    - 2.9.1 Message routing
      - 2.9.1.1 Manage replicators
      - 2.9.1.2 Cloud information
      - 2.9.1.3 Tasks
        - 2.9.1.3.1 Remote tasks
        - 2.9.1.3.2 Local tasks
    - 2.9.2 Connect
      - 2.9.2.1 analyticdb-for-mysql-sink-connector
      - 2.9.2.2 analyticdb-for-postgresql-sink-connector
      - 2.9.2.3 elasticsearch-sink-connector
      - 2.9.2.4 flink-job-sink-connector
      - 2.9.2.5 hologres-sink-connector
      - 2.9.2.6 hologres-source-connector
      - 2.9.2.7 localfs-sink-connector
      - 2.9.2.8 localfs-source-connector
      - 2.9.2.9 mongodb-sink-connector
      - 2.9.2.10 mongodb-source-connector
      - 2.9.2.11 mysql-sink-connector.json
      - 2.9.2.12 mysql-source-connector.json
      - 2.9.2.13 oceanbase-mysql-sink-connector
      - 2.9.2.14 oceanbase-mysql-source-connector
      - 2.9.2.15 oss-sink-connector
      - 2.9.2.16 oss-source-connector
      - 2.9.2.17 otlp-sls-sink-connector
      - 2.9.2.18 otlp-source-connector
      - 2.9.2.19 polardb-for-mysql-sink-connector
      - 2.9.2.20 polardb-for-mysql-source-connector
      - 2.9.2.21 polardb-for-postgresql-sink-connector
      - 2.9.2.22 polardb-for-postgresql-source-connector
      - 2.9.2.23 polardb-x-2.0-sink-connector
      - 2.9.2.24 polardb-x-2.0-source-connector
      - 2.9.2.25 postgresql-sink-connector.json
      - 2.9.2.26 postgresql-source-connector.json
      - 2.9.2.27 prometheus-sink-connector
      - 2.9.2.28 prometheus-source-connector
      - 2.9.2.29 redis-sink-connector
      - 2.9.2.30 redis-source-connector
      - 2.9.2.31 sls-sink-connector
      - 2.9.2.32 sls-source-connector
      - 2.9.2.33 spark-sink-connector
      - 2.9.2.34 tablestore-sink-connector
      - 2.9.2.35 tablestore-source-connector
      - 2.9.2.36 Transform configuration
    - 2.9.3 Ingest data to data lakes
  - 2.10 Zone-disaster recovery
    - 2.10.1 Solution overview
    - 2.10.2 Create replica clusters
  - 2.11 Data migration
    - 2.11.1 Cloud migration
      - 2.11.1.1 Migrate data of topics and groups to the cloud
    - 2.11.2 Cloud‑to‑Cloud Migration
      - 2.11.2.1 Use the ApsaraMQ for Kafka console to migrate services from one ApsaraMQ for Kafka instance to another
      - 2.11.2.2 Cloud‑to‑Cloud Migration using the Kafka data migration tool
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

## 1 What is ?

ApsaraMQ for Kafka is a distributed, high-throughput, and scalable message queue service provided by Alibaba Cloud. Used in big data fields such as log collection, monitoring data aggregation, streaming data processing, and online and offline analytics, ApsaraMQ for Kafka is an indispensable part of the big data ecosystem.

**Benefits**

ApsaraMQ for Kafka provides fully managed services for open source Apache Kafka and helps resolve specific pain points of open source Apache Kafka. ApsaraMQ for Kafka does not require deployment or O&M. You can focus on business development. With ApsaraMQ for Kafka, you can improve your service scalability and reliability with lower service costs.

**Application ecosystem**

ApsaraMQ for Kafka provides a rich application ecosystem that covers the following fields: Big data: ApsaraMQ for Kafka is used in fields such as website behavior analysis, log aggregation, application monitoring, streaming data processing, and online and offline data analytics. Data integration: ApsaraMQ for Kafka allows you to import messages to offline data warehouses such as MaxCompute, Object Storage Service (OSS), ApsaraDB RDS, Hadoop, and HBase. Stream computing integration: ApsaraMQ for Kafka integrates stream computing engines such as Realtime Compute, E-MapReduce, Spark, and Storm.

## 2 Console operations

### 2.1 Log on to the console

This topic describes how to log on to the ApsaraMQ for Kafka console. The URL of the Apsara Uni-manager Management Console is obtained from the deployment personnel before you log on to the Apsara Uni-manager Management Console. A browser is available. We recommend that you use the Google Chrome browser.

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
4. If your account has multi-factor authentication (MFA) enabled, perform corresponding
operations in the following scenarios: You log on to the Apsara Uni-manager Management Console for the first time after MFA is enabled by the administrator: a. On the Bind Virtual MFA Device page, bind an MFA device. b. Enter the username and password again as in Step 2 and click **Log On**. c. Enter a six-digit MFA verification code and click **Authenticate**. You have enabled MFA and bound an MFA device: Enter a six-digit MFA verification code and click **Authenticate**.

> **Note:** For more information, see the **Bind a virtual MFA device to enable** **MFA** topic in **Apsara Uni-manager Management Console User Guide** .

5. In the top navigation bar, choose **Products > Middleware > ApsaraMQ for Kafka**.
6. On the **ApsaraMQ for Kafka** page, select the organization and region and click **Kafka**.

### 2.2 Getting started

#### 2.2.1 Create a topic

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

**Usage notes**

To create an instance in the ApsaraMQ for Kafka console, you must upgrade ApsaraMQ for Kafka to V3.18.0. ApsaraMQ for Kafka V3.18.0 or later allows you to scale out an instance in the console if the instance is created in the console. The scaling method remains unchanged for instances delivered by using ApsaraMQ for Kafka of versions earlier than V3.18.0.

**Create an instance**

1. Log in to the ApsaraMQ for Kafka console.
2. In the left-side navigation pane, click **Instance List**.
3. On the **Instance List** page, click **Create an instance**.
4. On the **Create a Kafka instance** page, configure the following parameters and click
**Submit**.

> **Note:** If Service Catalog is enabled for your environment, configure the following parameters on the **Create a Kafka instance** page and click **Confirm Order**.

| Section | Parameter | Description |
|---|---|---|
| Basic information | Organization | The organization to which the instance that you want to create belongs. |
|   | Resource Set | The resource set to which the instance that you want to create belongs. |
|   | Geography | The region where the instance that you want to create resides. |
|   | Instance Type | The instance type. Single Zone is selected by default. |
|   | Primary Availability Zone | The primary zone. |
|   | Instance name | The instance name. |
|   | Kernel version | The kernel version of the instance. Valid values: v2.8.2 and v3.3.3. |
|   | Chip Type | The type of the chip that is used by the ApsaraMQ for Kafka resource pool. |

| ssage Queue for A | pache Kafka User Guide·Console operation |   |
|---|---|---|
| Kafka node information |   |   |
|   | Specifications | The specification of the instance that you want to create. Valid values: Broker4C16G Broker16C64G Broker32C128G Broker8C32G |
|   | Number of brokers | The number of brokers. Minimum value: 3. |
|   | Storage Type | The storage type. The default value is fast- disks-ssd, which specifies exclusive SSDs. You cannot specify a custom value for this parameter. |
|   | Number of disks per Broker | The number of disks for a single broker. Default value: 1. |
|   | Network Type | The network type. Valid values: AnyTunnel SingleTunnel Note If you select AnyTunnel, the instance may be accessed by customer networks after networks are integrated. Make sure that the instance is protected. |
|   | VPC | The ID of the VPC. Note This parameter is required only if you set Network Type to SingleTunnel. |

| Network Information |   |   |
|---|---|---|
|   | VSwitch | The ID of the vSwitch to which the instance that you want to create belongs. Note This parameter is required only if you set Network Type to SingleTunnel. We recommend that you select the vSwitch associated with the primary zone. You can view the zone where the vSwitch resides in the parentheses next to the vSwitch. |
|   | Access Point Type | The type of the endpoint. Valid values: PLAINTEXT and SASL. The default value is SASL. Note You can access an ApsaraMQ for Kafka instance by using a plaintext endpoint without authentication. Make sure that the endpoint is protected. |
|   | Domain name prefix | The prefix of the domain name. The prefix can contain only letters, digits, and hyphens (-). It must be 3 to 20 characters in length. |
|   | SASL plaintext access point | The port number of the SASL plaintext endpoint. The default port number is 8088. Note This parameter is displayed only if you set Access Point Type to SASL. |
|   | SASL SSL encrypted access _ point | The port number of the encrypted SASL SSL endpoint. The default port _ number is 8081. Note This parameter is displayed only if you set Access Point Type to SASL. |

|   | Plaintext access point | The port number of the plaintext endpoint. The default port number is 8080. Note This parameter is displayed only if you set Access Point Type to PLAINTEXT. |
|---|---|---|

**View an instance**

1. On the **Instance List** page, you can view **Tag**, **Instance status**, and **Expansion status** of
each instance. You can click the icon in the **Monitoring** column of an instance to open the
**Monitoring** window to view the monitoring information about the instance.
2. On the Instance List page, find the instance whose details you want to view and click the
name of the instance, or click **Details** in the **Operation** column to open the **Instance**
**Details** page.
3. On the **Instance Details** page, view the details of the instance on the **Basic information**,
**Running status**, **Access point information**, and **Task execution record** tabs.
i. **Basic information**: You can view the instance ID, instance name, zone, region, instance type, cluster type, major version, minor version, chip type, and specifications. ii. **Running status**: You can view the running status, payment type, creation time, and auto-renewal status of the instance. You can also view topology information about ZooKeeper and broker nodes. iii. **Access point information**: You can view information such as the network type, status, VPC ID, vSwitch ID, SASL_SSL, SASL_PLAINTEXT, and PLAINTEXT. iv. **Task execution record**: You can view the task type, status, start time, and end time.

**Restart an instance**

1. On the **Instance List** page, find the instance you want to restart and click **Restart** in the
**Operation** column.
2. In the message that appears, click **OK**.

**Scale out an instance**

If your ApsaraMQ for Kafka instance cannot meet your business requirements, you can scale out the instance in the ApsaraMQ for Kafka console.

> **Important:** After the scale-out, the number of brokers cannot be greater than the total number of exclusive nodes. ApsaraMQ for Kafka does not allow you to scale in an instance.

1. On the **Instance List** page, find the instance that you want to scale out and click
**Expansion** in the **Operation** column.
2. On the **Kafka instance expansion** page, specify a value in the **Number of final state**
**Broker nodes** field and click **Submit**.

> **Note:** If Service Catalog is enabled for your environment, configure the following parameters on the **Create a Kafka instance** page and click **Confirm Order**.

**Perform load balancing**

After you scale out an instance, existing topics are not automatically distributed to new brokers. In this case, you need to perform load balancing.
1. On the **Instance List** page, find the instance that is scaled out and click the
icon in the
**Operation** column. Then, click **Load balancing**.
2. In the message that appears, read the note and click **OK**.

> **Note:** After the scale-out, you can perform load balancing to evenly reallocate all partitions in the instance to all brokers.
> Load balancing operations may affect concurrent traffic. We recommend that you perform these operations during off-peak hours.
> Load balancing operations may affect the topics on which you have performed load balancing in the instance. Fully evaluate the impacts before you perform load balancing operations.

**Release an instance**

> **Warning:** After you release an instance, all data in the instance is deleted and cannot be restored. Proceed with caution.
> Before you release an instance, make sure that the disaster recovery cluster relationship has been removed.

1. On the **Instance List** page, find the instance that you want to manage and click **Release**
in the **Operation** column. `confirm`, and then click **OK**.
2. In the dialog box that appears, read the note, enter

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

Each instance can belong only to one resource group. After you specify a resource group for an instance, you cannot change the resource group. The permissions to query the instance relationship list and configure instance relationships are granted to the logon user.

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

This topic describes how to obtain the endpoint of an ApsaraMQ for Kafka instance. The instance ownership is configured. For more information, see Configure instance relationships. A VIP is created. For more information, see Create a VIP.

**Background information**

ApsaraMQ for Kafka allows you to use endpoints to connect to the following ports: 8080: You can use this port when you connect to an instance in a virtual private cloud (VPC). Simple Authentication and Security Layer (SASL) authentication is not supported. 8081: You can use this port when you connect to an instance in a VPC. SASL authentication is supported. The PLAINTEXT mechanism is used to authenticate client identities, and the SSL encryption method is used during message transmission. 8088: You can use this port when you connect to an instance in a VPC. SASL authentication is supported. The PLAINTEXT mechanism is used to authenticate client identities.

**Procedure**

1. Log on to the ApsaraMQ for Kafka console.
2. In the left-side navigation pane, click **Instance List**.
3. On the **Instance List** page, find the instance that you want to manage, and click the
instance name, or click **Details** in the **Operation** column.
4. On the **Instance details** page, click the **Access point information** tab to obtain the
endpoint of the instance, such as SASL_SSL, PLAINTEXT, and SASL_PLAINTEXT.

#### 2.3.4 Configure instance parameters

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
|---|---|---|
| num.partitions | The number of partitions of a topic. If you do not specify the number of partitions for a topic when you create the topic, the value of this parameter is used as the default value. | 3 |
| auto.create.topics.enable | Specifies whether to enable the automatic topic creation feature. After you enable the feature, a topic is automatically created if the topic does not exist but is specified for a produce or fetch request. If you do not enable this feature, you need to create a topic by using the CLI. | No |
| num.io.threads | The number of I/O threads used by a server to process requests. The value of this parameter must be greater than or equal to the number of disks. | 16 |
| queued.max.requests | The maximum number of requests that can be queued for processing by an I/O thread before a network thread stops receiving requests. | 80 |
| replica.fetch.wait.max.ms | The maximum period of time that the system can wait for the partition leader to respond to a request from a follower. If the request fails, the system automatically performs retries. Unit: milliseconds. | 500 |

| replica.lag.time.max.ms | The maximum period of time within which a follower must send a request to fetch data from the partition leader. If a follower does not send requests within this period of time, the follower is removed from the ISR list and is considered unavailable. Unit: milliseconds. | 30000 |
|---|---|---|
| num.network.threads | The number of network threads used by a server to process network requests. | 3 |
| log.retention.bytes | The maximum size of data that can be stored in each partition of a topic. Unit: bytes. The maximum data size of each topic is calculated by multiplying the value of this parameter by the total number of partitions of a topic. If you specify both the log.retention.hours parameter and this parameter, a log file is deleted when one of the thresholds specified by the parameters is exceeded. The setting of this parameter is overwritten if you configure the corresponding setting for a topic. | 4 |
| replica.fetch.max.bytes | The maximum size of data that can be obtained in each fetch request when the follower backs up data from the leader. Unit: bytes. | 10000000 |
| num.replica.fetchers | The number of threads used to back up data from the partition leader. | 4 |
| default.replication.factor | The default number of replicas for automatically created topics. | 3 |
| offsets.retention.minutes | The retention period of a committed offset. After the retention period of an offset elapses, the offset is marked by the system and is pending to be deleted. Unit: minutes. | 10080 |

| background.threads | The number of threads used for data processing in the background, such as deleting files. | 10 |
|---|---|---|

4. After you modify a parameter, click **Modify** in the **Operation** column of the parameter.
5. In the **Modify configuration** message, click **OK**.

#### 2.3.5 View the instance monitoring information

**information**

You can view monitoring charts in the CloudMonitor console to obtain the information about ApsaraMQ for Kafka instances. This topic describes how to view the monitoring data of an ApsaraMQ for Kafka instance in the ApsaraMQ for Kafka console and the CloudMonitor console.

**Background information**

ApsaraMQ for Kafka allows you to monitor the status of your resources in real time by using CloudMonitor. For example, you can monitor the status of your brokers, topics, and groups. You can also configure alert rules for metrics. If a metric value exceeds the specified alert threshold, CloudMonitor notifies you by making a phone call or sending a text message, an email, or a DingTalk chatbot notification. This way, you can handle exceptions at the earliest opportunity. For more information, see the **Overview** topic of the **CloudMonitor User**
**Guide** in Apsara Stack Documentation Center.

**Procedure**

1. Log on to the ApsaraMQ for Kafka console.
2. In the left-side navigation pane, click **Instance List**.
3. On the **Instance List** page, find the instance that you want to manage, and click the
instance name, or click **Details** in the **Operation** column.

> **Note:** You can also click the
> icon in the **Monitoring** column to open the monitoring panel.

4. On the **Instance details** page, click the **Monitoring** tab to view the monitoring
information.

> **Note:** You can also click **View more** in the upper-right corner of the Monitoring tab to go to the CloudMonitor console and view the detailed monitoring data of the instance.

| Item | Description |
|---|---|
| Granularity | The granularity by which the instance is monitored. Valid values: Broker, Topic, and Group. You can click the corresponding tab to view details. |

| Monitoring cycle | The period during which monitoring data is collected. Valid values: Hourly monitoring cycles: Last Hour, Last 3 hours, Last 6 hours, and Last 12 hours. Daily monitoring cycles: Last 1 day, Last 3 days, and Last 7 days. Custom: allows you to specify the start time and end time to define a monitoring cycle based on your business requirements. |
|---|---|
| Monitoring metric | The monitoring metrics. In this example, the granularity is set to broker. You can view the following metrics: Broker Message production traffic (BYTE), Broker message consumption traffic (BYTE), Broker Message production request frequency (count), Number of Broker messages produced (count), and Broker message consumption request frequency (count). For more information about monitoring metrics, see the supported metrics of ApsaraMQ for Kafka in the CloudMonitor User Guide in Apsara Stack Documentation Center. You can also click the icon in the upper-right corner of each monitoring chart to quickly create an alert rule. |

#### 2.3.6 View the operation logs of an instance

This topic describes how to view the operation logs of an ApsaraMQ for Kafka instance. This helps you quickly identify the cause of exceptions that occur when you manage or use ApsaraMQ for Kafka and improve troubleshooting efficiency.

**Note**

1. Operation logs are retained for seven days. To adjust the retention period, modify the
logging configurations as an administrator.
2. If you extend the retention period by modifying the logging configurations, the log data
generated before the new retention period is not backfilled.

**Procedure**

1. Log on to the ApsaraMQ for Kafka console.
2. In the left-side navigation pane, click **Instance List**.
3. On the **Instance List** page, find the instance that you want to manage, and click the
instance name, or click **Details** in the **Operation** column.
4. On the **Instance details** page, click the **Operation Log** tab to view the operation log of
the instance.
5. By default, the system displays all operations performed on the ApsaraMQ for Kafka
instance and its related resources in the last seven days. You can select a filter condition from the drop-down list next to **Operator**. You can also click **Advanced Filter** to filter the operations by **Operator**, **Operation**
**Name**, **Execution Status**, **Operation Source IP**, and **Operation Time**.

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

1. Log in to the ApsaraMQ for Kafka console.
2. In the left-side navigation pane, click **Instance List**.
3. On the **Instance List** page, find the instance that you want to manage, and click the
instance name, or click **Details** in the **Operation** column.
4. Click the **Topic management** tab.
5. On the **Topic management** tab, view the list of topics.

#### 2.4.3 View partition status in a topic

After you create a topic, you can view the status of each partition in the topic.

**Procedure**

1. Log on to the ApsaraMQ for Kafka console.
2. On the **Instance List** page, find the instance that you want to manage, and click the
instance name, or click **Details** in the **Operation** column.
3. On the **Instance details** page, click the **Topic management** tab.
4. On the **Topic management** tab, find the topic that you want to manage and click
**Partition status** in the **Operation** column.
In the **Partition status** panel, the status of all partitions in the topic is displayed.

| Parameter | Description |
|---|---|
| Total Number Of Messages On The Current Server | The total number of messages in all partitions. |
| Partition ID | The partition ID. |
| Earliest Offset | The minimum offset in the partition. |
| Latest Offset | The maximum offset in the partition. |
| ISR | The in-sync replicas. |
| Leader | The leader replica. Messages are sent to and received from the leader. |

#### 2.4.4 View the subscriptions of a topic

After you create a topic, you can view the online consumer groups that subscribe to the topic.

**Procedure**

1. Log on to the ApsaraMQ for Kafka console.
2. On the **Instance List** page, find the instance that you want to manage, and click the
instance name, or click **Details** in the **Operation** column.
3. On the **Instance details** page, click the **Topic management** tab.
4. On the **Topic management** tab, find the topic that you want to manage and click
**Subscription relationship** in the **Operation** column.
In the panel that appears, you can view all consumer groups that subscribe to the topic.

|   | > Document Version: 2026062 |
|---|---|

| Parameter | Description |
|---|---|
| Topic | The topic name. |
| Subscription Consumer Group | The number of consumer groups that subscribe to the topic. |
| No. | The serial number. |
| Consumer Group ID | The ID of the online consumer group that subscribes to the topic. If the group ID is offline, you cannot view the topic. |

#### 2.4.5 Modify topic configurations

After you create a topic, you can modify the configurations of the topic.

**Procedure**

1. Log on to the ApsaraMQ for Kafka console.
2. On the **Instance List** page, find the instance that you want to manage, and click the
instance name, or click **Details** in the **Operation** column.
3. On the **Instance details** page, click the **Topic management** tab.
4. On the **Topic management** tab, find the topic that you want to manage, click the
icon in the **Operation** column, and then click **topic configuration**.
5. In the **Topic configuration** dialog box, find the configuration item that you want to modify,
click **Modify**, select or enter a target value, and click **OK**.

| Parameter | Description |
|---|---|
| min.insync.replicas(Minimum number of synchronized replicas) | The minimum number of synchronized replicas. The minimum value is 1. The maximum value is the current number of replicas. We recommend that you set this value to 1. The minimum number of synchronized replicas must be smaller than or equal to the number of replicas. The minimum number of synchronized replicas defines the minimum number of replicas from which the system receives acknowledgments to determine the successful writing of a message. This value is valid only if the producer sets message acknowledgment to All or -1 . |

| retention.ms(Message retention time(ms)) | The period of time for which messages are retained in a topic. Valid values: 3600000 ms to 864000000 ms. |
|---|---|
| max.message.bytes(Maximum message size(bytes)) | The maximum size of a message that the topic can receive from a producer. Valid values: 1048576 bytes to 10485760 bytes. |
| retention.bytes(The total amount of data saved for each partition under each topic(bytes)) | The total amount of data stored in each partition in each topic. Valid values: -1 , or 268435456 bytes to 1073741824bytes. Note The value -1 indicates that the log size of the partition has no limit. |

#### 2.4.6 Increase the number of partitions in a topic

**topic**

After you create a topic, you can increase the number of partitions in the topic. You cannot decrease the number of partitions in a topic in ApsaraMQ for Kafka. If you want to decrease the number of partitions in a topic, delete the topic and create another topic that has the required number of partitions.

**Procedure**

1. Log on to the ApsaraMQ for Kafka console.
2. On the **Instance List** page, find the instance that you want to manage, and click the
instance name, or click **Details** in the **Operation** column.
3. On the **Instance details** page, click the **Topic management** tab.
4. On the **Topic management** page, find the topic that you want to manage, click the
icon in the **Operation** column, and then click **Increase the number of partitions**.
5. In the **Increase the number of partitions** dialog box, configure the **Number of new**
**partitions** parameter and click **OK**.

> **Note:** The number of partitions ranges from 1 to 48. To reduce the risk of data skew, we recommend that you select a multiple of 6. For special requirements, submit a ticket for consultation.

#### 2.4.7 Migrate topic partitions

This topic describes how to migrate topic partitions on a scaled-out ApsaraMQ for Kafka instance. An ApsaraMQ for Kafka instance is deployed and its value of **Expansion status** is
**Expanded**. For more information about how to scale out an instance, see the "Scale out an
instance" section of the Manage instances topic.

**Procedure**

**Rebalance messages for a single topic**

1. Log in to the ApsaraMQ for Kafka console.
2. In the left-side navigation pane, click **Instance List**.
3. On the **Instance List** page, find the instance that you want to manage, and click the
instance name, or click **Details** in the **Operation** column.
4. Click the **Topic management** tab.
5. In the topic list, find the topic that you want to manage, click the
icon in the **Operation** column, and then click **Message rebalancing**.
6. In the **Message rebalancing** dialog box, view the brokers in the **Current distribution**
**brokers** section. In the **Rebalanced brokers** section, select all brokers or the brokers to
which you want to redistribute messages.
7. Confirm the selected brokers in the **Purpose brokers** section and click **OK**.

**Batch rebalance messages**

> **Note:** You cannot select destination brokers for batch message rebalancing. By default, messages are load-balanced across all brokers.

1. Log in to the ApsaraMQ for Kafka console.
2. In the left-side navigation pane, click **Instance List**.
3. On the **Instance List** page, find the instance that you want to manage, and click the
instance name, or click **Details** in the **Operation** column.
4. Click the **Topic management** tab.
5. In the topic list, select the topics for which you want to rebalance messages and click **Bulk**
**Message Rebalancing** below the topic list.
6. In the **Confirm** dialog box, confirm the topics for which you want to rebalance messages
and click **OK**.

### 2.5 Consumer groups

#### 2.5.1 Create a consumer group

This topic describes how to create a consumer group.

**Background information**

Consumer groups are the core of the message parallel consumption, load balancing, and fault tolerance mechanisms. If multiple consumer instances are added to the same consumer group and subscribe to one or more the same topics, ApsaraMQ for Kafka automatically assigns partitions to members in the consumer group. This ensures that each message is consumed only once by a consumer in the group.

**Procedure**

1. Log in to the ApsaraMQ for Kafka console.
2. In the left-side navigation pane, click **Instance List**.
3. On the **Instance List** page, find the instance that you want to manage and click its name.
You can also click **Details** in the **Operation** column.
4. On the **Instance Details** page, click the **Group Management** tab.
5. On the **Group Management** tab, click **Create Consumer Group**.
6. In the **Create Consumer Group** dialog box, enter a name into the **Consumer Group**
parameter and click **OK**.

> **Note:** The value of the **Consumer Group** parameter must be 1 to 255 characters in length, and can contain letters, digits, underscores (_), hyphens (-), and periods (.).
> The value of the **Consumer Group** parameter cannot be modified after the consumer group is created. Proceed with caution.

**What to do next**

View sample code: Click **Code sample** in the **Operation** column. Then, the system automatically generates connection and consumption templates for the selected mainstream programming language, including the **message sending**, **message**
**receiving**, and **configuration file** templates. You can click **Copy** to copy the code.
To delete a consumer group, click **Delete** in the **Operation** column of the consumer group. In the message that appears, click **OK**.

#### 2.5.2 View the list of consumer groups

This topic describes how to view the list of consumer groups.

**Procedure**

1. Log on to the ApsaraMQ for Kafka console.
2. In the left-side navigation pane, click **Instance List**.
3. On the **Instance List** page, find the instance that you want to manage, and click the
instance name, or click **Details** in the **Operation** column.
4. On the **Instance details** page, click the **Group management** tab.
5. On the **Group management** tab, view the list of consumer groups.

#### 2.5.3 View the consumer status of a consumer group

**consumer group**

This topic describes how to view the consumer status of a consumer group.

**Procedure**

1. Log on to the ApsaraMQ for Kafka console.
2. In the left-side navigation pane, click **Instance List**.
3. On the **Instance List** page, find the instance that you want to manage, and click the
instance name, or click **Details** in the **Operation** column.
4. On the **Instance details** page, click the **Group management** tab.
5. On the **Group management** tab, find the consumer group that you want to manage and
click **Consumption status** in the **Operation** column. In the **Consumption status** panel, the status of all consumers in the consumer group is displayed.

| Parameter | Description |
|---|---|
| Total message accumulation | The total number of unconsumed messages in all topics to which the consumer group subscribes. |
| Topic | The name of the topic to which the consumer group subscribes. |
| Accumulation | The number of unconsumed messages in the topic to which the consumer group subscribes. |

6. **Optional.** If you want to view the consumption details of a specific topic, find the topic in
the topic list of the **Consumption status** panel and click **Details** in the **Operation** column of the topic. The consumption details of the topic are displayed in the message that appears.

| Parameter | Description |
|---|---|
| Partition ID | The partition ID. |

| owner | The ID of the online consumer that subscribes to the topic. Note The value is in the <Client ID> /<IP address> _ format. You cannot view the owner information about offline consumers. |
|---|---|
| Maximum site | The maximum offset from which messages can be consumed in the partition. |
| Consumption point | The offset from which messages are consumed in the partition. |
| Accumulation | The total number of accumulated messages in the current partition. The value is calculated by using the following formula: Total number of accumulated messages = Maximum offset - Consumer offset. Note This parameter is a key metric. If a large number of messages are accumulated, consumers may be blocked, or the consumption rate cannot keep up with the production rate. In this case, you need to analyze the consumer running status and improve the consumption speed. |

#### 2.5.4 Reset the consumer offset of a consumer group

**consumer group**

If you reset a consumer offset, the offset from which a consumer starts to consume messages is changed. You can reset consumer offsets to skip the accumulated or undesired messages instead of consuming them. You can also consume messages sent after a point in time regardless of whether the messages sent before this point in time are consumed. All consumers in the consumer group for which you want to reset the consumer offset are stopped.

> **Important:** ApsaraMQ for Kafka no longer supports the resetting of offsets during client connection.
> ApsaraMQ for Kafka considers a consumer stopped only after the period of time specified by the `ConsumerConfig.SESSION_TIMEOUT_MS_CONFIG` parameter elapses. The default value of the parameter is 10000, in milliseconds.

**Background information**

ApsaraMQ for Kafka allows you to reset consumer offsets by using one of the following methods:
**Clear all accumulated messages and start consumption from the latest offset:** If
you no longer want to consume accumulated messages on the broker, clear the messages for the consumer. This way, the consumer offset is set to the latest offset.

> **Important:** This method changes only the consumer offset. The accumulated messages are not deleted.

**Start consumption at the specified time point**: You can reset the offset of a consumer
group to a previous or future time point. For example, assume "t" is the time point when a message is stored. After the reset, the consumer group subscribes to messages stored after the "t" time point.

**Procedure**

1. Log on to the ApsaraMQ for Kafka console.
2. In the left-side navigation pane, click **Instance List**.
3. On the **Instance List** page, find the instance that you want to manage, and click the
instance name, or click **Details** in the **Operation** column.
4. On the **Instance details** page, click the **Group management** tab.
5. On the **Group management** tab, find the consumer group that you want to manage and
click **Reset consumption point** in the **Operation** column.
6. In the **Reset consumer point** dialog box, select the topic from the **Topic** drop-down list,
select a method used to reset the consumption offset, and then click **OK**.

### 2.6 Messages

#### 2.6.1 Send messages

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

#### 2.6.2 Query messages

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

### 2.7 ACL

#### 2.7.1 Create SASL users

This topic describes how to create a Simple Authentication and Security Layer (SASL) user. The ACL feature is enabled for the ApsaraMQ for Kafka instance. For more information, see Enable ACL.

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
| Password | The password of the SASL user. |
| Type | The type of the SASL user. ApsaraMQ for Kafka supports the following SASL mechanism: SCRAM: a username and password verification mechanism that provides higher security than PLAIN. ApsaraMQ for Kafka uses SCRAM-SHA- 256. |

#### 2.7.2 Grant permissions to SASL users

This topic describes how to grant permissions to a Simple Authentication and Security Layer (SASL) user. An SASL user is created. For more information, see Create SASL users.

**Procedure**

1. Log on to the ApsaraMQ for Kafka console.
2. In the left-side navigation pane, click **Instance List**.
3. On the **Instance List** page, find the instance that you want to manage, and click the
instance name, or click **Details** in the **Operation** column.
4. On the **Instance Details** page, click **SASL Permissions**.
5. Click **Create an ACL**.
6. In the **Create an ACL** dialog box, configure the parameters and click **OK**. The following
table describes the parameters.

| Parameter | Description |
|---|---|
| Username | The name of the SASL user. Note ApsaraMQ for Kafka supports the use of asterisks (*) as wildcard characters. You can use an asterisk (*) to specify all usernames. |

| Resource type | The resource type. Valid values: Topic: a topic. Group: a consumer group. Cluster: a cluster. |
|---|---|
| Matching pattern | The mode in which resources are matched. Valid values: Full match: matches resources by literal value. In this mode, only resources with the same name are matched. Prefix matching: matches resources by prefix. In this mode, resource names that start with the specified prefix are matched. |
| Operation type | The type of the operation that the SASL user can perform on resources. You can select multiple operation types to authorize various permissions at a time. Topic resources support the following operation types: Write: writes data. Read: reads data. Describe: describes resources. Describe Configs: describes configurations. _ Alter: alters resources. Delete: deletes resources. Create: creates resources. Alter Configs: alters configurations. _ All: selects all. Group resources support only the operation type Read. Cluster resources support the following operation types: Cluster Action: cluster operations. _ Describe: describes resources. Alter: alters resources. Create: creates resources. Alter Configs: alters configurations. _ All: selects all. |
| Whether to customize the resource name | If you select this option, you can enter a custom group name (resource name) instead of selecting an existing group to create an ACL. To make the created ACL take effect, you must manually create a group with the same name. Note This option is available only when you set Resource type to Group and set Matching pattern to Full match. |

| Resource Name | The resource name. The value can be the name of a topic or a consumer group. Note ApsaraMQ for Kafka supports the use of asterisks (*) as wildcard characters. You can use an asterisk (*) to specify all resource names. |
|---|---|
| Whitelist address | The IP address that you want to add to the ACL. Only the IP addresses and ports in the ACL can access the ApsaraMQ for Kafka instance. |

#### 2.7.3 Configure an ACL

This topic describes how to configure an access control list (ACL) for an ApsaraMQ for Kafka instance. After an ACL is configured for an ApsaraMQ for Kafka instance, only the IP addresses and ports in the ACL can be used to access the instance. An ApsaraMQ for Kafka instance is deployed and is in the **In service** state.

**Create an ACL**

1. Log on to the ApsaraMQ for Kafka console.
2. In the left-side navigation pane, click **Instance List**.
3. On the **Instance List** page, find the instance that you want to manage, and click the
instance name, or click **Details** in the **Operation** column.
4. On the **Instance Details** page, click **SASL Permissions**.
5. On the SASL permissions tab, click **Create an ACL**. In the **Create an ACL** dialog box,
configure the parameters that are described in the following table and click **OK**.

| Parameter | Description |
|---|---|
| Username | The name of the SASL user. Note ApsaraMQ for Kafka supports the use of asterisks (*) as wildcard characters. You can use an asterisk (*) to specify all usernames. |
| Resource type | The resource type. Valid values: Topic: a topic. Group: a consumer group. Cluster: a cluster. |

| Matching pattern | The mode in which resources are matched. Valid values: Full match: matches resources by literal value. In this mode, only resources with the same name are matched. Prefix matching: matches resources by prefix. In this mode, resource names that start with the specified prefix are matched. |
|---|---|
| Operation type | The type of the operation that the SASL user can perform on resources. You can select multiple operation types to authorize various permissions at a time. Topic resources support the following operation types: Write: writes data. Read: reads data. Describe: describes resources. Describe Configs: describes configurations. _ Alter: alters resources. Delete: deletes resources. Create: creates resources. Alter Configs: alters configurations. _ All: selects all. Group resources support only the operation type Read. Cluster resources support the following operation types: Cluster Action: cluster operations. _ Describe: describes resources. Alter: alters resources. Create: creates resources. Alter Configs: alters configurations. _ All: selects all. |
| Whether to customize the resource name | If you select this option, you can enter a custom group name (resource name) instead of selecting an existing group to create an ACL. To make the created ACL take effect, you must manually create a group with the same name. Note This option is available only when you set Resource type to Group and set Matching pattern to Full match. |
| Resource Name | The resource name. The value can be the name of a topic or a consumer group. Note ApsaraMQ for Kafka supports the use of asterisks (*) as wildcard characters. You can use an asterisk (*) to specify all resource names. |

| Whitelist address | The IP address that you want to add to the ACL. Only the IP addresses and ports in the ACL can access the ApsaraMQ for Kafka instance. |
|---|---|

**Delete an ACL**

1. Log on to the ApsaraMQ for Kafka console.
2. In the left-side navigation pane, click **Instance List**.
3. On the **Instance List** page, find the instance that you want to manage, and click the
instance name, or click **Details** in the **Operation** column.
4. On the **Instance Details** page, click **SASL Permissions**.
5. On the SASL permissions tab, find the ACL that you want to delete and click **Delete** in the
**Operation** column.
6. In the **Delete ACL** dialog box, click **OK**.

#### 2.7.4 Change the passwords of SASL users

This topic describes how to change the password of a Simple Authentication and Security Layer (SASL) user. A SASL user is created. For more information, see Create SASL users.

**Procedure**

1. Log on to the ApsaraMQ for Kafka console.
2. In the left-side navigation pane, click **Instances**.
3. On the **Instance List** page, find the instance that you want to manage and click **Details** in
the **Operation** column.
4. Click the **SASL user** tab.
5. On the **SASL user** tab, find the SASL user whose password you want to change and click
**Modify** in the **Operation** column.
6. In the **Modify SASL users** dialog box, enter a new password and click **OK**.

#### 2.7.5 Delete SASL users

This topic describes how to delete a Simple Authentication and Security Layer (SASL) user. A SASL user is created. For more information, see Create SASL users.

**Procedure**

1. Log on to the ApsaraMQ for Kafka console.
2. In the left-side navigation pane, click **Instances**.
3. On the **Instance List** page, find the instance that you want to manage and click **Details** in
the **Operation** column.
4. Click the **SASL user** tab.
5. On the **SASL user** tab, find the SASL user that you want to delete and click **Delete** in the
**Operation** column.
6. In the **Delete SASL user** message, click **OK**.

#### 2.7.6 Delete the permissions of SASL users

This topic describes how to delete the permissions that are granted to a Simple Authentication and Security Layer (SASL) user. Permissions are granted to the SASL user. For more information, see Grant permissions to SASL users.

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

#### 2.7.7 Download an ACL certificate

This topic describes how to download an Access Control List (ACL) certificate. The endpoint type for the target instance is SASL. The endpoint information contains values for SASL_SSL and SASL_PLAINTEXT.

**Procedure**

1. Log on to the ApsaraMQ for Kafka console.
2. In the left-side navigation pane, click **Instance List**.
3. On the **Instance List** page, find the instance that you want to manage, and click the
instance name, or click **Details** in the **Operation** column.
4. On the **Instance Details** page, click **SASL Permissions**.
5. On the **SASL Permissions** tab, click **Download ACL Certificate** to download the
certificate to your local computer.

### 2.8 VIPs

#### 2.8.1 Create a VIP

This topic describes how to create a virtual IP address (VIP).

**Background information**

**g**

ApsaraMQ for Kafka provides the following types of VIPs:
**SingleTunnel:** Allows access to ApsaraMQ for Kafka only from a specific VPC.
**AnyTunnel:** Allows access to ApsaraMQ for Kafka from any VPC.

**Procedure**

1. Log on to the ApsaraMQ for Kafka console.
2. In the left-side navigation pane, click **Instance List**.
3. On the **Instance List** page, find the instance that you want to manage, and click the
instance name, or click **Details** in the **Operation** column.
4. On the **Instance Details** page, click the **Endpoints** tab, and then click **Create**.
5. On the **Create VIP** page, configure the following network parameters and click **Submit**.

| Parameter | Description |
|---|---|
| Network Type | The network type. Valid values: AnyTunnel SingleTunnel Note If you select AnyTunnel, the instance may be accessed by customer networks after networks are integrated. Make sure that the instance is protected. |
| Endpoint Type | The type of the endpoint. Valid values: PLAINTEXT and SASL. The default value is SASL. Note You can access an ApsaraMQ for Kafka instance by using a plaintext endpoint without authentication. Make sure that the endpoint is protected. |
| VPC ID | The ID of the VPC. Note This parameter is required only if you set Network Type to SingleTunnel. |

| VSwitch ID | The ID of the vSwitch to which the instance that you want to create belongs. Note This parameter is required only if you set Network Type to SingleTunnel. We recommend that you select the vSwitch associated with the primary zone. You can view the zone where the vSwitch resides in the parentheses next to the vSwitch. |
|---|---|
| UID | The UID of the owner of the specified vSwitch ID. Note This parameter is required only when Network Type is set to SingleTunnel. |
| Domain Name Prefix | The prefix of the domain name. The prefix can contain only letters, digits, and hyphens (-). It must be 3 to 20 characters in length. |
| SASL Plaintext Endpoint | The port number of the SASL plaintext endpoint. The default port number is 8088. Note This parameter is displayed only if you set Access Point Type to SASL. |
| SASL SSL Encrypted Endpoint _ | The port number of the encrypted SASL SSL endpoint. The _ default port number is 8081. Note This parameter is displayed only if you set Access Point Type to SASL. |
| Plaintext Endpoint | The port number of the plaintext endpoint. The default port number is 8080. Note This parameter is displayed only if you set Access Point Type to PLAINTEXT. |

To create a VIP, you must update the ApsaraMQ for Kafka network and restart the ApsaraMQ for Kafka service. This process takes approximately 10 minutes for each ApsaraMQ for Kafka node.

#### 2.8.2 Delete a VIP

This topic describes how to delete a VIP.

**Procedure**

1. Log on to the ApsaraMQ for Kafka console.
2. In the left-side navigation pane, click **Instance List**.
3. On the **Instance List** page, find the instance that you want to manage, and click the
instance name, or click **Details** in the **Operation** column.
4. On the **Instance details** page, click the **Access point information** tab and click **Delete**.
5. In the **Confirm deletion** dialog box, enter
`confirm` and click **OK**.

> **Important:** After you delete a VIP, the ApsaraMQ for Kafka instance becomes unavailable. Proceed with caution.

#### 2.8.3 Request a domain name

This topic describes how to request a domain name for a virtual IP address (VIP) endpoint that does not have a domain name prefix. The VIP endpoint does not have a domain name prefix.

**Procedure**

1. Log on to the ApsaraMQ for Kafka console.
2. In the left-side navigation pane, click **Instance List**.
3. On the **Instance List** page, find the instance that you want to manage, and click the
instance name, or click **Details** in the **Operation** column.
4. On the **Instance Details** page, click the **Endpoint Information** tab, and click **Request**
**Domain Name**.
5. In the **Request Domain Name** window, enter a domain name prefix, and click **OK**.

### 2.9 Data integration

#### 2.9.1 Message routing

You can use the message routing feature to create and manage message synchronization clouds, remote tasks, and local tasks.

##### 2.9.1.1 Manage replicators

This topic describes how to create and view replicators in the ApsaraMQ for Kafka console.

**Background information**

ApsaraMQ for Kafka allows you to dynamically create and manage replicators in the ApsaraMQ for Kafka console. This eliminates the cumbersome process of planning and deploying incremental replicators in disaster recovery scenarios.

**Usage notes**

Replicators require significant resources. A replicator typically requires at least 16 vCPUs and 32 GB of memory. The current version supports only multi-zone scenarios.

**Create a replicator**

1. Log on to the ApsaraMQ for Kafka console.
2. In the left-side navigation pane, choose **Data Integration > Message Routing**.
3. On the **Replicator** tab, click **Create a Replicator**.
4. In the **Create a Replicator** dialog box, configure the following parameters and click **OK**.

| Parameter | Description |
|---|---|
| Availability Zone | Select the zone in which you want to create the replicator. |
| Use | Select the purpose of the replicator. |

**View replicators**

1. Log on to the ApsaraMQ for Kafka console.
2. In the left-side navigation pane, choose **Data Integration > Message Routing**.
3. On the **Replicator** tab, you can view existing replicators and their information, including
**Replicator ID**, **Geography**, **Availability Zone**, **Whether to create dynamically** ,
**Status**, and **Use**.
4. Optional. You can enter the desired replicator ID in the search box above the list for a quick
search.
5. Optional. You can click **Details** in the **Operation** column of the desired replicator to view
its details.
**Instance Details**: displays the key values of replicators, including **cluster1**,
**bootstrapServers1**, **targetCluster**, **bootstrapServers2**, **autoOffsetReset**, **cluster2**,
and **timestamp**.
**MirrorSourceConnector Details**/**MirrorCheckpointConnector**
**Details**/**MirrorHeartbeatConnector Details**: displays **Connector Information**, **Task**
**Status**, and **Task Configuration**.
Click **Restart** in the upper-right corner of the **Connector Information** module to restart the MirrorSourceConnector, MirrorCheckpointConnector, MirrorHeartbeatConnector, and all tasks.

> **Note:** MirrorSourceConnector: reads data from the source cluster and writes the data to the destination cluster.
> MirrorCheckpointConnector: records the offset of the consumer group in the source cluster and synchronizes the offset to the destination cluster.
> MirrorHeartbeatConnector: sends heartbeats between the source and destination clusters to monitor the connection status.

**Restart a replicator**

> **Important:** During the restart of a replicator, message replication between the source and destination clusters is suspended.

1. Log on to the ApsaraMQ for Kafka console.
2. In the left-side navigation pane, choose **Data Integration > Message Routing**.
3. On the **Replicator** tab, click **Restart** in the Operation column of the desired replicator.
4. In the message that appears, click **OK**.

##### 2.9.1.2 Cloud information

This topic describes how to create and manage a message synchronization cloud.

**Background information**

You can use message synchronization clouds and remote tasks to migrate data between different clouds. Remote tasks also provide atomic APIs for geo-disaster recovery and enable data migration between different clouds to achieve disaster recovery. The ApsaraMQ for Kafka instance on one cloud is connected to the ApsaraMQ for Kafka instance on the other cloud. In addition, the domain name of the Apsara Uni-manager Management Console on one cloud is connected to the domain name of the Apsara Unimanager Management Console on the other cloud. The IP addresses of the endpoints in the two clouds are mutually reachable.

**Create a message synchronization cloud**

You can perform the following steps to create a message synchronization cloud.
1. Log on to the ApsaraMQ for Kafka console.
2. In the left-side navigation pane, choose **Data Integration > Message Routing**.
3. On the **Message Routing** page, click the **Cloud Information** tab.
4. Click **Create Message synchronization cloud** .
5. In the **Create Message synchronization cloud** dialog box, configure the following
parameters and click **OK**.

| Parameter | Description |
|---|---|
| Cloud Name | Enter a name for the message synchronization cloud. |
| AK | Enter your AccessKey ID. |
| Geography | Enter the region in which the cloud to be synchronized resides. |
| SK | Enter your AccessKey secret. |
| kafka instance endpoint | Enter the domain name of the ApsaraMQ for Kafka instance. |
| ascm Domain Names | Enter the domain name of the Apsara Uni-manager Management Console. |
| Organization ID | Select the ID of the organization to which the destination cloud cluster belongs. |
| Resource set ID | Select the ID of the resource set to which the destination cloud cluster belongs. |
| Remarks | Optional. Enter a description. |

**View a message synchronization cloud**

You can perform the following steps to view the created message synchronization clouds and their basic information.
1. Log on to the ApsaraMQ for Kafka console.
2. In the left-side navigation pane, choose **Data Integration > Message Routing**.
3. On the **Message Routing** page, click the **Cloud Information** tab.
4. On the **Cloud Information** tab, you can view the created message synchronization clouds
and their basic information, including **Cloud Name**, **uuid**, **Geography**, **AccessKey**, **Kafka**
**Domain Names**, **Organization**, **Resource Set**, **Creation time**, and **Remarks**.
5. Optional. You can enter a cloud name in the search box above the list for a quick search.

**Delete a message synchronization cloud**

You can perform the following steps to delete a message synchronization cloud.
1. Log on to the ApsaraMQ for Kafka console.
2. In the left-side navigation pane, choose **Data Integration > Message Routing**.
3. On the **Message Routing** page, click the **Cloud Information** tab.
4. On the **Cloud Information** tab, find the message synchronization cloud that you want to
delete and click **Delete** in the **Operation** column.
5. In the **Confirm** message, click **OK**.

##### 2.9.1.3 Tasks

This topic describes how to create and manage remote tasks and local tasks.

###### 2.9.1.3.1 Remote tasks

This topic describes how to create and manage remote tasks.

**Background information**

You can use remote tasks to migrate data between different clouds. Remote tasks also provide atomic APIs for geo-disaster recovery and enable data migration between different clouds to achieve disaster recovery. The ApsaraMQ for Kafka instance on one cloud is connected to the ApsaraMQ for Kafka instance on the other cloud. In addition, the domain name of the Apsara Uni-manager Management Console on one cloud is connected to the domain name of the Apsara Unimanager Management Console on the other cloud. The IP addresses of the endpoints in the two clouds are mutually reachable.

**Create a remote task**

You can perform the following steps to create a remote task.
1. Log on to the ApsaraMQ for Kafka console.
2. In the left-side navigation pane, choose **Data Integration > Message Routing**.
3. On the **Message Routing** page, click the **Tasks** tab.
4. Click **Create Offsite Tasks**, configure the following parameters, and then click **OK**.

| Parameter | Description |
|---|---|

| Message Source | SOURCE instance | Select the source ApsaraMQ for Kafka instance. Note The source instance is an instance within the current region. |
|---|---|---|
|   | Type | Select the type of the migration task. Valid values: Instance Migration topic migration |
|   | Synchronous Topic | Select the topic to be synchronized. You can select multiple topics. If you do not specify this parameter, all topics in the instance are synchronized. Regular expressions are supported. For example, hello.* indicates that all topics that start with hello are synchronized. Note This parameter is displayed only if you set Type to topic migration. |
|   | sasl User | Select the Simple Authentication and Security Layer (SASL) user. |
|   | Source Replicator | Select the source replicator. |
| Message Destination | Message synchronization cloud | Select the destination message synchronization cloud. |
|   | Target Region | The system automatically configures the destination region based on the message synchronization cloud that you select. |
|   | Target Instance | Select the destination ApsaraMQ for Kafka instance. |

| Synchronization Start Point | Select an offset to start the data synchronization. Valid values: Earliest point Nearest Point Specified time |
|---|---|
| Time point | Select a date. If the offset cannot be found in the specified partition of the specified topic after you select the time, data synchronization starts from the earliest offset. An offset cannot be found if the specified time is earlier than the earliest offset or later than the latest offset. Note This parameter is displayed only if you set Synchronization Start Point to Specified time. |
| Description | Enter a description. |

5. After the remote task is created, you can view its basic information and status in the task
list on the **Tasks** tab.

**View remote tasks**

You can perform the following steps to view a remote task.
1. Log on to the ApsaraMQ for Kafka console.
2. In the left-side navigation pane, choose **Data Integration > Message Routing**.
3. On the **Message Routing** page, click the **Tasks** tab.
4. On the **Tasks** tab, you can view the created tasks and their basic information, including
**uuid**, **Source cluster**, **Target Cluster**, **Migration Type**, **Synchronized topic**, **Status**,
**Synchronization Policy**, **Current limiting**, and **Creation time**.
5. You can also click **Details** in the **Operation** column of a task to view the details of the
task, including **Source Information**, **Target Information**, and **Other information**.

**Start a remote task**

You can perform the following steps to start a remote task.
1. Log on to the ApsaraMQ for Kafka console.
2. In the left-side navigation pane, choose **Data Integration > Message Routing**.
3. On the **Message Routing** page, click the **Tasks** tab.
4. On the **Tasks** tab, find the remote task that you want to start and click **Start** in the
**Operation** column.
5. In the **Confirm** message, click **OK**.
6. Optional. After you click **Start** to start a remote task, you can click **Stop** to stop the task.

**Delete a remote task**

You can perform the following steps to delete a remote task.
1. Log on to the ApsaraMQ for Kafka console.
2. In the left-side navigation pane, choose **Data Integration > Message Routing**.
3. On the **Message Routing** page, click the **Tasks** tab.
4. On the **Tasks** tab, find the remote task that you want to delete and click **Delete** in the
**Operation** column.
5. In the **Confirm** message, click **OK**.

###### 2.9.1.3.2 Local tasks

This topic describes how to create and manage local tasks.

**Background information**

You can use local tasks to migrate services from one ApsaraMQ for Kafka instance to another ApsaraMQ for Kafka instance. For more information, see Use the ApsaraMQ for Kafka console to migrate services from one ApsaraMQ for Kafka instance to another.

**Create a local task**

You can perform the following steps to create a local task.
1. Log on to the ApsaraMQ for Kafka console.
2. In the left-side navigation pane, choose **Data Integration > Message Routing**.
3. On the **Message Routing** page, click the **Tasks** tab.
4. Click **Create a local task**, configure the following parameters, and then click **OK**.

| Parameter |   | Description |
|---|---|---|
| Message Source | SOURCE instance | Select the source ApsaraMQ for Kafka instance. |
|   | Type | Select the type of the migration task. Valid values: Instance Migration topic migration |
|   | Synchronous Topic | Select the topic to be synchronized. You can select multiple topics. If you do not specify this parameter, all topics in the instance are synchronized. Regular expressions are supported. For example, hello.* indicates that all topics that start with hello are synchronized. Note This parameter is displayed only if you set Type to topic migration. |

| Message Destination | Target Instance | Select the destination ApsaraMQ for Kafka instance. |
|---|---|---|
|   | Target Replicator | Select the destination replicator. |
| Synchronization Start Point |   | Select an offset to start the data synchronization. Valid values: Earliest point Nearest Point Specified time |
| Time point |   | Select a date. If the offset cannot be found in the specified partition of the specified topic after you select the time, data synchronization starts from the earliest offset. An offset cannot be found if the specified time is earlier than the earliest offset or later than the latest offset. Note This parameter is displayed only if you set Synchronization Start Point to Specified time. |
| Current limiting |   | Configure the throttling rule for the data synchronization process of the disaster recovery instances. Unit: MB/s. Note If throttling is not required during the data synchronization of disaster recovery instances, set this parameter to 0. |
| Description |   | Enter a description. |

5. After the local task is created, you can view its basic information and status in the task list
on the **Tasks** tab.

**View a local task**

You can perform the following steps to view a local task.
1. Log on to the ApsaraMQ for Kafka console.
2. In the left-side navigation pane, choose **Data Integration > Message Routing**.
3. On the **Message Routing** page, click the **Tasks** tab.
4. On the **Tasks** tab, you can view the created tasks and their basic information, including
**uuid**, **Source cluster**, **Target Cluster**, **Migration Type**, **Synchronized topic**, **Status**,
**Synchronization Policy**, **Current limiting**, and **Creation time**.
5. You can also click **Details** in the **Operation** column of a task to view the details of the
task, including **Source Information**, **Target Information**, and **Other information**.

**Start a local task**

You can perform the following steps to start a local task.
1. Log on to the ApsaraMQ for Kafka console.
2. In the left-side navigation pane, choose **Data Integration > Message Routing**.
3. On the **Message Routing** page, click the **Tasks** tab.
4. On the **Tasks** tab, find the local task that you want to start and click **Start** in the
**Operation** column.
5. In the **Confirm** message, click **OK**.
6. Optional. After you click **Start** to start a local task, you can click **Stop** to stop the task.

**Migrate a domain name**

You can perform the following steps to migrate the domain name of a source cluster to the destination cluster.

> **Note:** Prerequisites:
> The source instance has a domain name.
> The message lag between the source and destination instances is 0. A domain name can be migrated only if the message lag between the source and destination instances is 0. You can view the message **lag** in the **Other information** section on the **Task Details** page.

1. Log on to the ApsaraMQ for Kafka console.
2. In the left-side navigation pane, choose **Data Integration > Message Routing**.
3. On the **Message Routing** page, click the **Tasks** tab.
4. On the **Tasks** tab, find the desired local task and click **Domain Migration** in the
**Operation** column.
5. In the **Confirm** message, click **OK**.

**Disable write operations for a local task**

You can perform the following steps to block the traffic of the source cluster so that a local task can be performed.

> **Note:** Note that write operations cannot be re-enabled within three minutes after they are disabled.

1. Log on to the ApsaraMQ for Kafka console.
2. In the left-side navigation pane, choose **Data Integration > Message Routing**.
3. On the **Message Routing** page, click the **Tasks** tab.
4. On the **Tasks** tab, find the local task for which you want to disable write operations, click
the icon in the **Operation** column, and then click **Forbidden to write**.
5. In the **Confirm** message, click **OK**.

**Delete a local task**

You can perform the following steps to delete a local task.
1. Log on to the ApsaraMQ for Kafka console.
2. In the left-side navigation pane, choose **Data Integration > Message Routing**.
3. On the **Message Routing** page, click the **Tasks** tab.
4. On the **Tasks** tab, find the local task that you want to delete, click the
icon in the
**Operation** column, and then select **Delete**.
5. In the **Confirm** message, click **OK**.

#### 2.9.2 Connect

This topic describes how to manage connects and connectors.

**Background information**

Kafka Connect enables reliable and scalable data streaming between ApsaraMQ for Kafka and external systems, such as databases, message queues, and file systems. An ApsaraMQ for Kafka instance is created. For more information, see the Create an instance section in the Manage instances topic. Automatic topic creation is enabled for the ApsaraMQ for Kafka instance. This indicates that
**auto.create.topics.enable** is turned on in the **Parameter configuration** panel of the
ApsaraMQ for Kafka instance. For more information, see auto.create.topics.enable in the Configure instance parameters topic.

**Create a connect**

1. Log on to the ApsaraMQ for Kafka console.
2. In the left-side navigation pane, choose **Data Integration > Connect**.
3. On the **Connect** page, click **Create Connect**.
4. In the **Create Connect** dialog box, configure the following parameters and click **OK**.

| Parameter | Description |
|---|---|
| Zone ID | The ID of the zone to which the connect belongs. |
| Kafka instance | The ApsaraMQ for Kafka instance to which the connect is connected. |

**Manage connects**

**View connects**

1. Log on to the ApsaraMQ for Kafka console.
2. In the left-side navigation pane, choose **Data Integration > Connect**.
3. On the **Connect** page, you can view the created connects and their basic information,
including **Connect ID**, **Kafka instance ID**, **Zone**, and **Status**.
4. Optional. You can enter a connect ID in the search box above the list for an exact search.

**View the details of a connect**

1. Log on to the ApsaraMQ for Kafka console.
2. In the left-side navigation pane, choose **Data Integration > Connect**.
3. On the **Connect** page, click the ID of the connect that you want to view in the **Connect ID**
column, or click **Details** in the **Operation** column. On the **Connector list** page, you can view the task list and basic information, including **Task ID**, **Type**, **Maximum number of**
**tasks**, and **Status**.

**Delete a connect**

1. Log on to the ApsaraMQ for Kafka console.
2. In the left-side navigation pane, choose **Data Integration > Connect**.
3. On the **Connect** page, find the connect that you want to delete and click **Delete** in the
**Operation** column. In the message that appears, click OK.

**Create a connector**

1. Log on to the ApsaraMQ for Kafka console.
2. In the left-side navigation pane, choose **Data Integration > Connect**.
3. On the **Connect** page, click the ID of the connect that you want to view in the **Connect ID**
column, or click **Details** in the **Operation** column to open the **Connector list** page.
4. On the **Connector list** page, click **Create Connector**.
5. On the **Create Connector** page, configure the following parameters and click **Submit**.

| Parameter | Description |
|---|---|
| Task ID | Enter the task ID. |
| Type | Select a connector type. For more information about the supported connector types, see the Connector types section in this topic. |
| Connector configuration | Configure the parameters of the selected connector type and click Next Step. For more information about the parameters for each connector, see the Connector configuration reference column in the Connector types section of this topic. |

| Transform configuration | Different connector types support different predicates and converters. The actual predicates and converters displayed on the page prevail. For more information, see Transform configuration. |
|---|---|

**Connector types**

| Type | Description | Connector configuration reference |
|---|---|---|
| analyticdb-for-mysql- sink-connector | Synchronizes data from ApsaraMQ for Kafka to AnalyticDB for MySQL in real time. | analyticdb-for-mysql-sink-connector |
| analyticdb-for- postgresql-sink- connector | Synchronizes data from ApsaraMQ for Kafka to AnalyticDB for PostgreSQL in real time. | analyticdb-for-postgresql-sink- connector |
| elasticsearch-sink- connector | Synchronizes data from ApsaraMQ for Kafka to Elasticsearch in real time. | elasticsearch-sink-connector |
| localfs-sink-connector | Synchronizes data from ApsaraMQ for Kafka to files in real time. | localfs-sink-connector |
| flink-job-sink- connector | Synchronizes data from ApsaraMQ for Kafka to Flink in real time. | flink-job-sink-connector |
| hologres-sink- connector | Synchronizes data from ApsaraMQ for Kafka to Hologres in real time. | hologres-sink-connector |
| hologres-source- connector | Synchronizes data from Hologres to ApsaraMQ for Kafka in real time. | hologres-source-connector |
| localfs-source- connector | Synchronizes data from files to ApsaraMQ for Kafka in real time. | localfs-source-connector |
| mongodb-sink- connector | Synchronizes data from ApsaraMQ for Kafka to ApsaraDB for MongoDB in real time. | mongodb-sink-connector |
| mongodb-source- connector | Synchronizes data from ApsaraDB for MongoDB to ApsaraMQ for Kafka in real time. | mongodb-source-connector |

| mysql-sink-connector | Synchronizes data from ApsaraMQ for Kafka to MySQL in real time. | mysql-sink-connector.json |
|---|---|---|
| mysql-source- connector | Synchronizes data from ApsaraDB RDS for MySQL to ApsaraMQ for Kafka in real time. | mysql-source-connector.json |
| oceanbase-mysql- sink-connector | Synchronizes data from ApsaraMQ for Kafka to OceanBase in real time. | oceanbase-mysql-sink-connector |
| oceanbase-mysql- source-connector | Synchronizes data from OceanBase to ApsaraMQ for Kafka in real time. | oceanbase-mysql-source-connector |
| oss-sink-connector | Synchronizes data from ApsaraMQ for Kafka to Object Storage Service (OSS) in real time. | oss-sink-connector |
| oss-source-connector | Synchronize data from OSS to ApsaraMQ for Kafka in real time. | oss-source-connector |
| otlp-sls-sink- connector | Synchronizes telemetry data (traces, metrics, and logs) in the OpenTelemetry Protocol (OTLP) format to Simple Log Service (SLS). | otlp-sls-sink-connector |
| otlp-source-connector | Receives telemetry data (traces, metrics, and logs) in the OTLP format and synchronizes the data to ApsaraMQ for Kafka. | otlp-source-connector |
| polardb-for-mysql- sink-connector | Synchronizes data from ApsaraMQ for Kafka to PolarDB for MySQL in real time. | polardb-for-mysql-sink-connector |
| polardb-for-mysql- source-connector | Synchronizes data from PolarDB for MySQL to ApsaraMQ for Kafka in real time. | polardb-for-mysql-source-connector |
| polardb-for- postgresql-sink- connector | Synchronizes data from ApsaraMQ for Kafka to PolarDB for PostgreSQL in real time. | polardb-for-postgresql-sink- connector |
| polardb-for- postgresql-source- connector | Synchronizes data from PolarDB for PostgreSQL to ApsaraMQ for Kafka in real time. | polardb-for-postgresql-source- connector |

| polardb-x-2.0-sink- connector | Synchronizes data from ApsaraMQ for Kafka to PolarDB-X V2.0 in real time. | polardb-x-2.0-sink-connector |
|---|---|---|
| polardb-x-2.0-source- connector | Synchronizes data from PolarDB-X V2.0 to ApsaraMQ for Kafka in real time. | polardb-x-2.0-source-connector |
| postgresql-sink- connector | Synchronizes data from ApsaraMQ for Kafka to ApsaraDB RDS for PostgreSQL in real time. | postgresql-sink-connector.json |
| postgresql-source- connector | Synchronizes data from ApsaraDB RDS for PostgreSQL to ApsaraMQ for Kafka in real time. | postgresql-source-connector.json |
| prometheus-sink- connector | Synchronizes data from ApsaraMQ for Kafka to Managed Service for Prometheus in real time. | prometheus-sink-connector |
| prometheus-source- connector | Synchronizes data from Managed Service for Prometheus to ApsaraMQ for Kafka in real time. | prometheus-source-connector |
| redis-sink-connector | Synchronizes data from ApsaraMQ for Kafka to ApsaraDB for Redis in real time. | redis-sink-connector |
| redis-source- connector | Synchronizes data from ApsaraDB for Redis to ApsaraMQ for Kafka in real time. | redis-source-connector |
| sls-sink-connector | Synchronizes data from ApsaraMQ for Kafka to SLS in real time. | sls-sink-connector |
| sls-source-connector | Synchronizes data from SLS to ApsaraMQ for Kafka in real time. | sls-source-connector |
| spark-sink-connector | Submits Spark tasks in real time based on the data in ApsaraMQ for Kafka. | spark-sink-connector |
| tablestore-sink- connector | Synchronizes data from ApsaraMQ for Kafka to Tablestore in real time. | tablestore-sink-connector |
| tablestore-source- connector | Synchronizes data from Tablestore to ApsaraMQ for Kafka in real time. | tablestore-source-connector |

**Manage connectors**

**View connectors**

1. Log on to the ApsaraMQ for Kafka console.
2. In the left-side navigation pane, choose **Data Integration > Connect**.
3. On the **Connect** page, click the ID of the connect that you want to view in the **Connect ID**
column, or click **Details** in the **Operation** column to open the **Connector list** page.
4. On the **Connector list** page, you can view the created connectors and their basic
information, including **Task ID**, **Type**, **Maximum number of tasks**, and **Status**.
5. Optional. You can enter a connector ID in the search box above the list for an exact search.

**View the details of a connector**

1. Log on to the ApsaraMQ for Kafka console.
2. In the left-side navigation pane, choose **Data Integration > Connect**.
3. On the **Connect** page, click the ID of the connect that you want to view in the **Connect ID**
column, or click **Details** in the **Operation** column to open the **Connector list** page.
4. On the **Connector list** page, find the connector that you want to view and click **Details** in
the **Operation** column to view the configuration details of the connector.

**Delete a connector**

1. Log on to the ApsaraMQ for Kafka console.
2. In the left-side navigation pane, choose **Data Integration > Connect**.
3. On the **Connect** page, click the ID of the connect that you want to view in the **Connect ID**
column, or click **Details** in the **Operation** column to open the **Connector list** page.
4. On the **Connector list** page, find the connector that you want to delete and click **Delete** in
the **Operation** column. In the message that appears, click OK.

**Enable or disable a connector**

1. Log on to the ApsaraMQ for Kafka console.
2. In the left-side navigation pane, choose **Data Integration > Connect**.
3. On the **Connect** page, click the ID of the connect that you want to view in the **Connect ID**
column, or click **Details** in the **Operation** column to open the **Connector list** page.
4. On the **Connector list** page, click **Disable** or **Enable** in the **Operation** column of the
desired connector. In the message that appears, click OK.

**Restart a connector and its tasks**

1. Log on to the ApsaraMQ for Kafka console.
2. In the left-side navigation pane, choose **Data Integration > Connect**.
3. On the **Connect** page, click the ID of the connect that you want to view in the **Connect ID**
column, or click **Details** in the **Operation** column to open the **Connector list** page.
4. On the **Connector list** page, click **Details** in the **Operation** column of the desired
connector.
5. On the **Connector Details** page, click **Restart All** in the upper-right corner. In the
message that appears, click OK to restart the connector and all tasks.

**Restart failed tasks**

1. Log on to the ApsaraMQ for Kafka console.
2. In the left-side navigation pane, choose **Data Integration > Connect**.
3. On the **Connect** page, click the ID of the connect that you want to view in the **Connect ID**
column, or click **Details** in the **Operation** column to open the **Connector list** page.
4. On the **Connector list** page, click **Details** in the **Operation** column of the desired
connector. Restart a failed task: On the **Connector Details** page, click **Restart** in the **Operation** column of the failed task. In the message that appears, click OK. Restart all failed tasks: On the **Connector Details** page, click **Restart Failed Tasks** in the upper-right corner. In the message that appears, click OK.

##### 2.9.2.1 analyticdb-for-mysql-sink-connector

This topic describes how to configure the parameters for analyticdb-for-mysql-sink-connector. You are creating a connector, and the connector type is set to analyticdb-for-mysql-sinkconnector. For more information about how to create a connector, see the Create a connector section in the Connect topic.

**Parameters**

**Basic Configuration**

| Parameter | Description |
|---|---|
| Max Tasks | The maximum number of tasks that can be created for the connector. Default value: 12. Valid values: 1 to 12. |

**Connection Configuration**

| Parameter | Description |
|---|---|
| Database Connection URL | The Java Database Connectivity (JDBC) URL that you can use to connect to the AnalyticDB for MySQL database, in the format of jdbc:mysql://host:port/database? parameters . |
| Username | The username used to connect to the AnalyticDB for MySQL database. |
| Password | The password used to connect to the AnalyticDB for MySQL database. |

|   |   | jdbc:mysql://host:port/database? |
|---|---|---|
|   | parameters |   |

| Database Time Zone | The time zone of the AnalyticDB for MySQL database. |
|---|---|

**Data Configuration**

| Parameter | Description |
|---|---|
| Kafka Topics | The Kafka topics from which messages are consumed. Separate multiple topics with commas (,). |
| Target Table Name | The name of the table to which data is written. It must be a fully-qualified identifier. Example: <database>.<table> . |
| Insert Mode | The mode in which data is inserted. Valid values: insert: Data is only inserted. upsert: Data is inserted or updated. update: Data is only updated. |
| Enable Delete | Specify whether to synchronize DELETE events to the destination table. After this feature is enabled, the sink connector physically deletes the data. This feature must be used together with insert.mode=upsert and primary.key.mode=record key . _ |
| Primary Key Mode | The primary key retrieval mode. Valid values: From Record Key: retrieves primary keys from record key . This mode is required for handling _ DELETE events. From Record Value: retrieves primary keys from record value . _ From Kafka Coordinates: retrieves primary keys from kafka . |
| Primary Key Fields | The names of the primary key fields. Separate multiple fields with commas (,). |

|   | insert.mode=upsert |
|---|---|
| primary.key.mode=record key _ |   |

**Advanced Configuration**

| Parameter | Description |
|---|---|
| Quote Identifiers | Specify whether to use quotation marks ("") to enclose table names and column names. The default value is true and cannot be modified. |

| Field Include List | The list of fields to be included. Separate multiple fields with commas (,). If you leave this parameter empty, all fields are included. |
|---|---|

##### 2.9.2.2 analyticdb-for-postgresql-sink-connector

This topic describes how to configure the parameters for analyticdb-for-postgresql-sinkconnector. You are creating a connector, and the connector type is set to analyticdb-for-postgresql-sinkconnector. For more information about how to create a connector, see the Create a connector section in the Connect topic.

**Parameters**

**Basic Configuration**

| Parameter | Description |
|---|---|
| Max Tasks | The maximum number of tasks that can be created for the connector. Default value: 12. Valid values: 1 to 12. |

**Connection Configuration**

| Parameter | Description |
|---|---|
| Database Connection URL | The Java Database Connectivity (JDBC) connection URL of the AnalyticDB for PostgreSQL database. Example: jdbc:postgresql://<host>:<port>/<database> . |
| Username | The username used to connect to the AnalyticDB for PostgreSQL database. |
| Password | The password used to connect to the AnalyticDB for PostgreSQL database. |
| Database Time Zone | The time zone of the AnalyticDB for PostgreSQL database. |

**Data Configuration**

| Parameter | Description |
|---|---|

| Kafka Topics | The Kafka topics from which messages are consumed. Separate multiple topics with commas (,). |
|---|---|
| Target Table Name | The name of the AnalyticDB for PostgreSQL table to which data is written. It must be a fully-qualified identifier. Example: <schema>.<table> . |
| Insert Mode | The mode in which data is inserted. Valid values: insert: Data is only inserted. upsert: Data is inserted or updated. update: Data is only updated. |
| Enable Delete | Specify whether to synchronize DELETE events to the destination table. After this feature is enabled, the sink connector physically deletes the data. This feature must be used together with insert.mode=upsert and primary.key.mode=record key . Valid values: _ Disable Enable |
| Primary Key Mode | The primary key retrieval mode. Valid values: From Record Key: retrieves primary keys from record key . This mode is required for handling _ DELETE events. From Record Value: retrieves primary keys from record value . _ From Kafka Coordinates: retrieves primary keys from kafka . |
| Primary Key Fields | The names of the primary key fields. Separate multiple fields with commas (,). |

|   | insert.mode=upsert |
|---|---|
| primary.key.mode=record key _ |   |

**Advanced Configuration**

| Parameter | Description |
|---|---|
| Quote Identifiers | Specify whether to use quotation marks ("") to enclose table names and column names. The default value is true and cannot be modified. |
| Field Include List | The list of fields to be included. Separate multiple fields with commas (,). If you leave this parameter empty, all fields are included. |

##### 2.9.2.3 elasticsearch-sink-connector

This topic describes how to configure the parameters for Elasticsearch-sink-connector. You are creating a connector, and the connector type is set to Elasticsearch-sink-connector. For more information about how to create a connector, see Create a connector.

**Configuration description**

**Basic Configuration**

| Parameter | Description |
|---|---|
| Max Tasks | The maximum number of tasks for parallel processing. The number of tasks must be between 1 and 12. |

**Connection Configuration**

| Parameter | Description |
|---|---|
| Elasticsearch Connection URL | The endpoint of the Elasticsearch cluster. |
| Elasticsearch Username | The username that is used to log in to the Elasticsearch cluster. |
| Elasticsearch Password | The password that is used to log in to the Elasticsearch cluster. |
| Elasticsearch Index | The name of the index that is created in the Elasticsearch cluster. |

**Data Configuration**

| Parameter | Description |
|---|---|
| Kafka Topics | The Kafka topics from which messages will be consumed. |

##### 2.9.2.4 flink-job-sink-connector

This topic describes how to configure the parameters for flink-job-sink-connector. You are creating a connector, and the connector type is set to flink-job-sink-connector. For more information about how to create a connector, see the Create a connector section in the Connect topic.

**Parameters**

**Basic Configuration**

| Parameter | Description |
|---|---|
| Max Tasks | The job manager uses only one task to avoid duplicate commands. The value cannot be modified. |
| Command Topic | The name of the Kafka topic that receives Flink job management commands in JSON format. The commands contain the action, jobId, and sql fields. |

**Flink VVP Connection**

| Parameter | Description |
|---|---|
| VVP Endpoint | The endpoint of the Ververica Platform (VVP) API. Example: ververica.cn-*****.cloud.***-env.com . |
| Region | The region where the VVP resides. Example: cn- hangzhou . |
| AccessKey ID | The AccessKey ID of your Apsara Stack tenant account. We recommend that you use a Resource Access Management (RAM) user. |
| AccessKey Secret | The AccessKey secret of your Apsara Stack tenant account. |
| Namespace | The name of the VVP namespace. |
| Workspace | The name of the VVP workspace. Default value: default. |
| Job Folder | The name of the directory where VVP jobs are stored. You need to create the directory in the VVP console first. |

**Job Default Configuration**

| Parameter | Description |
|---|---|

| Default Parallelism | The default concurrency level of Flink jobs. Default value: 1. Valid values: 1 to 128. |
|---|---|
| JobManager CPU | The default number of CPU cores assigned to the job manager. Default value: 0.5. |
| JobManager Memory | The default amount of memory assigned to the job manager. Examples: 1Gi and 2Gi. Default value: 1Gi. |
| TaskManager CPU | The default number of CPU cores assigned to the task manager. Default value: 0.5. |
| TaskManager Memory | The default amount of memory assigned to the task manager. Examples: 1Gi and 2Gi. Default value: 1Gi. |

**Retry Configuration**

| Parameter | Description |
|---|---|
| Max Retries | The maximum number of attempts to retry a failed VVP API call. Default value: 3. Valid values: 0 to 10. |
| Retry Backoff (ms) | The retry backoff in milliseconds. Actual interval = Backoff x Number of retry attempts. Default value: 3000. |

**Data Configuration**

| Parameter | Description |
|---|---|
| Value Converter | The value converter class. The default value is org.apache.kafka.connect.json.JsonConverter and cannot be modified. |

##### 2.9.2.5 hologres-sink-connector

This topic describes how to configure the parameters for hologres-sink-connector. You are creating a connector, and the connector type is set to hologres-sink-connector. For more information about how to create a connector, see the Create a connector section in the Connect topic.

**Parameters**

**Basic Configuration**

| Parameter | Description |
|---|---|
| Max Tasks | The maximum number of parallel tasks. Default value: 12. Valid values: 1 to 12. |

**Connection Configuration**

| Parameter | Description |
|---|---|
| Database Connection URL | The Java Database Connectivity (JDBC) connection URL of the Hologres database. Example: jdbc:postgresql://<host>: <port>/<database> . |
| Username | The username used to connect to the Hologres database. |
| Password | The password used to connect to the Hologres database. |
| Database Time Zone | The time zone of the Hologres database. |

|   | <port>/<database> |
|---|---|

**Data Configuration**

| Parameter | Description |   |   |
|---|---|---|---|
| Kafka Topics | The Kafka topics from which messages are consumed. Separate multiple topics with commas (,). |   |   |
| Target Table Name | The name of the Hologres table to which data is written. It must be a fully-qualified identifier. Example: <schema>. <table> . |   |   |
|   |   | <schema>. |   |

|   | <table> |
|---|---|

| Insert Mode | The mode in which data is inserted. Valid values: insert: Data is only inserted. upsert: Data is inserted or updated. update: Data is only updated. |
|---|---|
| Enable Delete | Specify whether to synchronize DELETE events to the destination table. After this feature is enabled, the sink connector physically deletes the data. This feature must be used together with insert.mode=upsert and primary.key.mode=record key . Valid values: _ Disable Enable |
| Primary Key Mode | The primary key retrieval mode. Valid values: From Record Key: retrieves primary keys from record key . This mode is required for handling _ DELETE events. From Record Value: retrieves primary keys from record value . _ From Kafka Coordinates: retrieves primary keys from kafka . |
| Primary Key Fields | The names of the primary key fields. Separate multiple fields with commas (,). |

|   | insert.mode=upsert |
|---|---|
| primary.key.mode=record key _ |   |

**Advanced Configuration**

| Parameter | Description |
|---|---|
| Quote Identifiers | Specify whether to use quotation marks ("") to enclose table names and column names. The default value is true and cannot be modified. |
| Field Include List | The list of fields to be included. Separate multiple fields with commas (,). If you leave this parameter empty, all fields are included. |

##### 2.9.2.6 hologres-source-connector

This topic describes how to configure the parameters for hologres-source-connector. You are creating a connector, and the connector type is set to hologres-source-connector. For more information about how to create a connector, see the Create a connector section in the Connect topic.

**Parameters**

**Basic Configuration**

| Parameter | Description |
|---|---|
| Max Tasks | The maximum number of tasks that can be created for the connector. Default value: 1. Valid values: 1 to 12. |

**Connection Configuration**

| Parameter | Description |
|---|---|
| Database Hostname | The hostname of the Hologres instance endpoint. |
| Database Port | The port of the Hologres instance. |
| Username | The username used to connect to the Hologres database. |
| Password | The password used to connect to the Hologres database. |
| Database Name | The name of the Hologres database to which you want to connect. |

**Subscription Configuration**

| Parameter | Description |
|---|---|
| Table Include List | The tables to be monitored in the schema.table format. Separate multiple tables with commas (,). |
| Binlog Slot Mapping | Slot mappings in the schema.table:slot name format for multi-table subscription. Separate multiple slot mappings with commas (,). |
| Snapshot Mode | The snapshot policy used when the connector is started. Valid values: Snapshot Only Snapshot and CDC, downstream consumers MUST use upsert semantics to handle duplicate records correctly CDC Only |

**Data Configuration**

| Parameter | Description |
|---|---|
| Topic Prefix | The name prefix of the generated Kafka topics. |
| Key Schema Enable | Specify whether to include schema information in message keys. Valid values: Enable Disable |
| Value Schema Enable | Specify whether to include schema information in message values. Valid values: Enable Disable |

##### 2.9.2.7 localfs-sink-connector

This topic describes how to configure the parameters for localfs-sink-connector. You are creating a connector, and the connector type is set to localfs-sink-connector. For more information about how to create a connector, see the Create a connector section in the Connect topic.

**Parameters**

**Basic Configuration**

| Parameter | Description |
|---|---|
| Max Tasks | The maximum number of parallel tasks. The default value is 1 and cannot be modified. |

**Output Configuration**

| Parameter | Description |
|---|---|
| Output Directory Template | The output directory path template, which supports the following variables: ${topic} , ${partition} , ${year} , ${month} , ${day} , and ${hour} . |

|   | ${topic} |   |
|---|---|---|
| ${month} |   |   |

| ${partition} |   |
|---|---|

| Output Format | The file output format. Valid values: json csv text |
|---|---|
| Compression Type | The file compression algorithms. Valid values: none gzip |

**File Rotation Configuration**

| Parameter | Description |
|---|---|
| Rotation Policy | The file rotation policy. Valid values: size: rotate by size. time: rotate by time. count: rotate by number of records. |
| Rotation Size Threshold (bytes) | The file size threshold for file rotation by size. Default value: 64 MB. |
| Rotation Time Interval (ms) | The interval at which files are rotated by time. Default value: 1 hour. |
| Rotation Record Count Threshold | The record threshold for file rotation by number of records. |
| File Name Prefix | The name prefix of the output files. |

**Data Configuration**

| Parameter | Description |
|---|---|
| Kafka Topics | The Kafka topics from which messages will be consumed. Separate multiple topics with commas (,). |

##### 2.9.2.8 localfs-source-connector

This topic describes how to configure the parameters for localfs-source-connector. You are creating a connector, and the connector type is set to localfs-source-connector. For more information about how to create a connector, see the Create a connector section in the Connect topic.

**Parameters**

**Basic Configuration**

| Parameter | Description |
|---|---|
| Max Tasks | The maximum number of parallel tasks. The default value is 1 and cannot be modified. |

**Filesystem Configuration**

| Parameter | Description |
|---|---|
| Scan Directory Path | The local directory path (a path in a container) to be scanned. Example: /mnt/nas/input/ . |
| Recursive Scan | Specify whether to scan subdirectories recursively. |

**Data Configuration**

| Parameter | Description |
|---|---|
| Target Kafka Topic | The Kafka topic to which data is written. |
| Scan Interval (ms) | The file scan interval in milliseconds. Default value: 10000. |
| Skip Headers | The number of rows to skip in the file header, such as the CSV header. Default value: 0. |

**File Cleanup Configuration**

| Parameter | Description |   |
|---|---|---|
| Cleanup Policy | The file cleanup policy. The default value is io.streamthoughts.kafka.connect.filepulse.fs.clean.L ogCleanupPolicy , which indicates that files are only logged. They are not moved or deleted. |   |
|   |   | io.streamthoughts.kafka.connect.filepulse.fs.clean.L |
|   | ogCleanupPolicy |   |

**Status Storage Configuration**

| Parameter | Description |
|---|---|
| Kafka Broker Address | The address of the Kafka broker used to store status. |
| Status Topic | The name of the topic for tracing the file processing status. |

##### 2.9.2.9 mongodb-sink-connector

This topic describes how to configure the parameters for mongodb-sink-connector. You are creating a connector, and the connector type is set to mongodb-sink-connector. For more information about how to create a connector, see the Create a connector section in the Connect topic.

**Parameters**

**Basic Configuration**

| Parameter | Description |
|---|---|
| Max Tasks | The maximum number of tasks that can be created for the connector. Default value: 1. Valid values: 1 to 12. |
| Topic List | The Kafka topics from which messages are consumed. Separate multiple topics with commas (,). |

**Connection Configuration**

|   | Parameter | Description |   |   |
|---|---|---|---|---|
|   |   | The connection URI of the ApsaraDB for MongoDB database, in the format of mongodb://[username:password@]host1[:port1] |   |   |
|   |   |   | mongodb://[username:password@]host1[:port1] |   |
|   |   | [,host2[:port2],...[,hostN[:portN]]][/[database][? |   |   |
|   | Connection URI | options]] |   |   |

| Database Name | The name of the ApsaraDB for MongoDB database. |
|---|---|
| Collection Name | The name of the collection in the ApsaraDB for MongoDB database. If you leave this parameter empty, the topic names are used. |

**Advanced Configuration**

| Parameter | Description |
|---|---|
| CDC Handler | Valid values: No CDC Processing MongoDB Change Stream |
| ID Strategy | The document id field generation policy. Valid values: _ Extract id from Value _ Auto Generate ObjectId |
| Write Strategy | The mode in which data is written to ApsaraDB for MongoDB. Valid values: Upsert Mode Insert Only |

##### 2.9.2.10 mongodb-source-connector

This topic describes how to configure the parameters for mongodb-source-connector. You are creating a connector, and the connector type is set to mongodb-source-connector. For more information about how to create a connector, see the Create a connector section in the Connect topic.

**Parameters**

**Basic Configuration**

| Parameter | Description |
|---|---|
| Max Tasks | The maximum number of parallel tasks. The default value is 1. |

**Connection Configuration**

|   | Parameter | Description |   |   |
|---|---|---|---|---|
|   | Connection URI | The connection URI of the ApsaraDB for MongoDB database, in the format of mongodb://[username:password@]host1[:port1] |   |   |
|   |   |   | mongodb://[username:password@]host1[:port1] |   |
|   |   | [,host2[:port2],...[,hostN[:portN]]][/[database][? |   |   |
|   |   | options]] |   |   |
|   | Database Name | The name of the ApsaraDB for MongoDB database that you want to monitor. |   |   |
|   | Collection Name | The name of the collection that you want to monitor. If you leave the parameter empty, the entire database is monitored. |   |   |

**Topic Configuration**

| Parameter | Description |
|---|---|
| Topic Prefix | The name prefix of the generated Kafka topics. |

**Advanced Configuration**

| Parameter | Description |
|---|---|
| Full Document Mode | Specify whether an update operation returns the entire document. Valid values: Full Document Changed Fields Only |
| Startup Mode | The startup mode of the connector. Valid values: Start from Latest Copy Existing then CDC |

##### 2.9.2.11 mysql-sink-connector.json

This topic describes how to configure the parameters for mysql-sink-connector. You are creating a connector, and the connector type is set to mysql-sink-connector. For more information about how to create a connector, see Create a connector.

**Configuration description**

**Basic Configuration**

| Parameter | Description |
|---|---|
| Max Tasks | The maximum number of tasks for parallel processing. The number of tasks must be between 1 and 12. |

**Connection Configuration**

| Parameter | Description |
|---|---|
| Database Connection URL | The JDBC URL that you can use to connect to the MySQL database, in the format of jdbc:mysql://host:port/database?Parameters . |
| Username | The username that is used to connect to the MySQL database. |
| Password | The password that is used to connect to the MySQL database. |
| Database Time Zone | The time zone used by the database. Example: Asia/Shanghai. |

**Data Configuration**

| Parameter | Description |
|---|---|
| Kafka Topics | The Kafka topics from which messages will be consumed. Separate multiple topics with commas (,). |
| Target Table Name | The name of the MySQL table to which you want to write data. |
| Insert Mode | Insert mode of input data: insert: inserts data only. upsert: inserts or updates data. update: updates data only. |
| Primary Key Mode | The retrieval mode of the primary key: record value: obtains the primary key from record values. _ |

| Primary Key Fields | The name of the primary key field. Separate multiple fields with commas (,). |
|---|---|

**Advanced Configuration**

| Parameter | Description |
|---|---|
| Quote Identifiers | Specifies whether to use quotation marks for table and column names. Default value: true . |
| Field Include List | The field that you want to include. Separate multiple fields with commas (,). If you leave this parameter empty, all fields are included. |

##### 2.9.2.12 mysql-source-connector.json

This topic describes how to configure the parameters for mysql-source-connector. You are creating a connector, and the connector type is set to mysql-source-connector. For more information about how to create a connector, see Create a connector.

**Configuration description**

**Basic Configuration**

| Parameter | Description |
|---|---|
| Max Tasks | The maximum number of tasks for parallel processing. The number of tasks must be 1. |

**Connection Configuration**

| Parameter | Description |
|---|---|
| Database Hostname | The IP address of the MySQL database server. |
| Database Port | The port number of the MySQL database server. |
| Username | The username that is used to connect to the MySQL database server. |

| Password | The password that is used to connect to the MySQL database server. |
|---|---|
| Database Server ID | The numeric ID of the database client. Note This ID must be unique across all currently running database processes in the MySQL cluster. |

**Data Configuration**

| Parameter | Description |
|---|---|
| Database Include List | The names of the databases that you want to monitor. Separate multiple databases with commas (,). |
| Table Include List | The fully qualified table identifiers used to match the tables to be monitored. Separate multiple tables with commas (,). |
| Topic Prefix | The topic prefix. |
| Schema History Kafka Servers | The host and port pairs used by the connector to establish the initial connection to the Kafka cluster for retrieving the previously stored database schema history. The Kafka cluster should be the one used by the Kafka connect process. |
| Schema History Kafka Topic | The name of the Kafka topic where the connector stores the database schema history. |

##### 2.9.2.13 oceanbase-mysql-sink-connector

This topic describes how to configure the parameters for oceanbase-mysql-sink-connector. You are creating a connector, and the connector type is set to oceanbase-mysql-sinkconnector. For more information about how to create a connector, see the Create a connector section in the Connect topic.

**Parameters**

**Basic Configuration**

| Parameter | Description |
|---|---|

| Max Tasks | The maximum number of parallel tasks. Default value: 12. Valid values: 1 to 12. |
|---|---|

**Connection Configuration**

| Parameter | Description |
|---|---|
| Database Connection URL | The Java Database Connectivity (JDBC) URL that you can use to connect to the OceanBase database, in the format of jdbc:mysql://host:port/database?parameters . |
| Username | The username used to connect to the OceanBase database. |
| Password | The password used to connect to the OceanBase database. |
| Database Time Zone | The time zone of the OceanBase database. |

**Data Configuration**

| Parameter | Description |
|---|---|
| Kafka Topics | The Kafka topics from which messages are consumed. Separate multiple topics with commas (,). |
| Target Table Name | The name of the MySQL table to which data is written. |
| Insert Mode | The mode in which data is inserted. Valid values: insert: Data is only inserted. upsert: Data is inserted or updated. update: Data is only updated. |
| Enable Delete | Specify whether to synchronize DELETE events to the destination table. After this feature is enabled, the sink connector physically deletes the data. This feature must be used together with insert.mode=upsert and primary.key.mode=record key . Valid values: _ Disable Enable |

|   | insert.mode=upsert |
|---|---|
| primary.key.mode=record key _ |   |

| Primary Key Mode | The primary key retrieval mode. Valid values: From Record Key: retrieves primary keys from record key . This mode is required for handling _ DELETE events. From Record Value: retrieves primary keys from record value . _ From Kafka Coordinates: retrieves primary keys from kafka . |
|---|---|
| Primary Key Fields | The names of the primary key fields. Separate multiple fields with commas (,). |

**Advanced Configuration**

| Parameter | Description |
|---|---|
| Quote Identifiers | Specify whether to use quotation marks ("") to enclose table names and column names. The default value is true and cannot be modified. |
| Field Include List | The list of fields to be included. Separate multiple fields with commas (,). If you leave this parameter empty, all fields are included. |

##### 2.9.2.14 oceanbase-mysql-source-connector

This topic describes how to configure the parameters for oceanbase-mysql-source-connector. You are creating a connector, and the connector type is set to oceanbase-mysql-sourceconnector. For more information about how to create a connector, see the Create a connector section in the Connect topic.

**Parameters**

**Basic Configuration**

| Parameter | Description |
|---|---|
| Max Tasks | The maximum number of parallel tasks. The value is fixed to 1. |

**Connection Configuration**

| Parameter | Description |
|---|---|

| Database Hostname | The IP address of the OceanBase database server. Only OceanBase databases that have the binlog service deployed are supported. |
|---|---|
| Database Port | The port of the OceanBase database server. |
| Username | The username used to connect to the OceanBase database. |
| Password | The password used to connect to the OceanBase database. |
| Database Server ID | The numeric ID of the database client. The ID must be unique among all running database processes in the OceanBase cluster. |

**Data Configuration**

| Parameter | Description |
|---|---|
| Database Include List | An optional list of regular expressions separated by commas (,). It is used to match the names of databases that you want to monitor. |
| Table Include List | An optional list of regular expressions separated by commas (,). It is used to match the fully-qualified identifiers of tables that you want to monitor. Example: <database>. <table> . |
| Topic Prefix | The prefix of the generated topics. |
| Schema History Kafka Servers | The host and port pairs used by the connector to establish the initial connection to the Kafka cluster for retrieving the database schema history. The Kafka cluster must be the same as the one used by the Kafka connect process. |
| Schema History Kafka Topic | The name of the Kafka topic where the connector stores the database schema history. |
| Snapshot Mode | The snapshot policy used when the connector is started. Valid values: Initial Full Snapshot (downstream recommended to use upsert mode for duplicate keys) Schema Only Snapshot Never Snapshot |

|   | <table> |
|---|---|

| Key Schema Enable | Specify whether to include schema information in message keys. Valid values: Enable Disable |
|---|---|
| Value Schema Enable | Specify whether to include schema information in message values. Valid values: Enable Disable |

##### 2.9.2.15 oss-sink-connector

This topic describes how to configure the parameters for oss-sink-connector. You are creating a connector, and the connector type is set to oss-sink-connector. For more information about how to create a connector, see the Create a connector section in the Connect topic.

**Parameters**

**Basic Configuration**

| Parameter | Description |
|---|---|
| Max Tasks | The maximum number of parallel tasks. The default value is 1 and cannot be modified. |

**Connection Configuration**

| Parameter | Description |
|---|---|
| Access Key ID | The AccessKey ID of the Apsara Stack tenant account. |
| Access Key Secret | The AccessKey secret of the Apsara Stack tenant account. |
| Bucket Name | The name of the Object Storage Service (OSS) bucket. |
| OSS Endpoint | The Simple Storage Service (S3)-compatible OSS endpoint. |

**Data Configuration**

| 2 | > Document Version: 2026062 |
|---|---|

| Parameter | Description |
|---|---|
| Kafka Topics | The Kafka topics from which messages are consumed. |
| Output Format | The file output format. Valid values: json csv avro parquet |
| File Name Template | The OSS file name template. Example: filename/{{topic}}-{{partition}}- {{start offset}} . _ |
| Compression Type | The file compression algorithm. Valid values: none gzip snapp zstd |

|   |   | filename/{{topic}}-{{partition}}- |
|---|---|---|
|   | {{start offset}} _ |   |

##### 2.9.2.16 oss-source-connector

This topic describes how to configure the parameters for oss-source-connector. You are creating a connector, and the connector type is set to oss-source-connector. For more information about how to create a connector, see the Create a connector section in the Connect topic.

**Parameters**

**Basic Configuration**

| Parameter | Description |
|---|---|
| Max Tasks | The maximum number of parallel tasks. The default value is 1 and cannot be modified. |

**OSS Connection Configuration**

| Parameter | Description |
|---|---|

| OSS Endpoint | The endpoint of Object Storage Service (OSS). Example: http://oss-cn-xxx.cloud.xxx.com . |
|---|---|
| Bucket Name | The name of the OSS bucket. |
| Object Prefix | Only files with the specified prefix are scanned. Example: data/csv/ . |
| AccessKey ID | The AccessKey ID used for OSS authentication. |
| AccessKey Secret | The AccessKey secret used for OSS authentication. |

**Data Configuration**

| Parameter | Description |
|---|---|
| Target Kafka Topic | The Kafka topic to which data is written. |
| Scan Interval (ms) | The file scan interval in milliseconds. Default value: 10000. |
| Skip Headers | The number of rows to skip in the file header. Default value: 0. |

**File Cleanup Configuration**

| Parameter | Description |   |
|---|---|---|
| Cleanup Policy | The file cleanup policy. The default value is io.streamthoughts.kafka.connect.filepulse.fs.clean.L ogCleanupPolicy , which indicates that files are only logged. They are not moved or deleted. |   |
|   |   | io.streamthoughts.kafka.connect.filepulse.fs.clean.L |
|   | ogCleanupPolicy |   |
| Success File Target Prefix | The OSS path prefix of files that are successfully processed. |   |
| Failure File Target Prefix | The OSS path prefix of files that failed to be processed. |   |

**Status Storage Configuration**

| Parameter | Description |
|---|---|
| Kafka Broker Address | The address of the Kafka broker used to store status. |
| Status Topic | The name of the topic for tracing the file processing status. |

##### 2.9.2.17 otlp-sls-sink-connector

This topic describes how to configure the parameters for otlp-sls-sink-connector. You are creating a connector, and the connector type is set to otlp-sls-sink-connector. For more information about how to create a connector, see the Create a connector section in the Connect topic.

**Parameters**

**Basic Configuration**

| Parameter | Description |
|---|---|
| Max Tasks | The maximum number of parallel tasks. Default value: 1. Valid values: 1 to 12. |
| Kafka Topics | The Kafka topics from which messages are consumed. In most cases, an OpenTelemetry Protocol (OTLP) source connector outputs three topics. Separate multiple topics with commas (,). |

**SLS Connection Configuration**

| Parameter | Description |
|---|---|
| SLS Endpoint | The endpoint of Simple Log Service (SLS). The endpoint does not contain the project prefix. The project prefix is automatically added by the SDK. Example: data.cn- hangzhou.log.aliyuncs.com . |
| SLS Project | The name of the SLS project. |
| AccessKey ID | The AccessKey ID of the Apsara Stack tenant account, which must have permissions ( log:PostLogStoreLogs ) to write data to SLS. |

|   | hangzhou.log.aliyuncs.com |
|---|---|

| AccessKey Secret | The AccessKey secret of the Apsara Stack tenant account. |
|---|---|

**Logstore Configuration**

| Parameter | Description |
|---|---|
| Traces Logstore | The name of the SLS Logstore to which trace data is written. |
| Metrics Logstore | The name of the SLS Logstore to which metric data is written. |
| Logs Logstore | The name of the SLS Logstore to which log data is written. |

**Write Configuration**

| Parameter | Description |
|---|---|
| Batch Size | The maximum number of log entries that can be written to SLS per batch. Default value: 2000. Valid values: 1 to 10000. |

**Data Configuration**

| Parameter | Description |
|---|---|
| Value Converter | The value converter class. The StringConverter is used to process OTLP data and cannot be changed. |

##### 2.9.2.18 otlp-source-connector

This topic describes how to configure the parameters for otlp-source-connector. You are creating a connector, and the connector type is set to otlp-source-connector. For more information about how to create a connector, see the Create a connector section in the Connect topic.

**Parameters**

**Basic Configuration**

| Parameter | Description |
|---|---|

| Max Tasks | Only one task is allowed because the OpenTelemetry Protocol (OTLP) receiver is a single-threaded server. |
|---|---|

**Receiver Configuration**

| Parameter | Description |
|---|---|
| Enable gRPC Receiver | Specify whether to enable the OTLP gRPC receiver. |
| gRPC Port | The port on which the gRPC receiver listens. Default value: 4317. |
| Enable HTTP Receiver | Specify whether to enable the OTLP HTTP receiver. |
| HTTP Port | The port on which the HTTP receiver listens. Default value: 4318. |
| Bind Address | The IP address bound to the OTLP receiver. The default value is 0.0.0.0 , which indicates that the receiver listens on all network interface controllers (NICs). |

**TLS Configuration**

| Parameter | Description |
|---|---|
| Enable TLS | Specify whether to enable TLS encryption. The default value is false and cannot be modified. |

**Kafka Topic Configuration**

| Parameter | Description |
|---|---|
| Traces Topic | The name of the Kafka topic to which trace data is written. |
| Metrics Topic | The name of the Kafka topic to which metric data is written. |
| Logs Topic | The name of the Kafka topic to which log data is written. |

**Message Format Configuration**

| Parameter | Description |
|---|---|

| Message Queue Size | The size of the internal message queue for each signal type. New messages are discarded when the queue is full. Default value: 10000. Valid values: 100 to 1000000. |
|---|---|

##### 2.9.2.19 polardb-for-mysql-sink-connector

This topic describes how to configure the parameters for polardb-for-mysql-sink-connector. You are creating a connector, and the connector type is set to polardb-for-mysql-sinkconnector. For more information about how to create a connector, see the Create a connector section in the Connect topic.

**Parameters**

**Basic Configuration**

| Parameter | Description |
|---|---|
| Max Tasks | The maximum number of parallel tasks. Default value: 12. Valid values: 1 to 12. |

**Connection Configuration**

| Parameter | Description |
|---|---|
| Database Connection URL | The Java Database Connectivity (JDBC) URL that you can use to connect to the PolarDB for MySQL database, in the format of jdbc:mysql://host:port/database?parameters . |
| Username | The username used to connect to the PolarDB for MySQL database. |
| Password | The password used to connect to the PolarDB for MySQL database. |
| Database Time Zone | The time zone of the PolarDB for MySQL database. |

**Data Configuration**

| Parameter | Description |
|---|---|

| Kafka Topics | The Kafka topics from which messages will be consumed. Separate multiple topics with commas (,). |
|---|---|
| Target Table Name | The name of the MySQL table to which data is written. |
| Insert Mode | The mode in which data is inserted. Valid values: insert: Data is only inserted. upsert: Data is inserted or updated. update: Data is only updated. |
| Enable Delete | Specify whether to synchronize DELETE events to the destination table. After this feature is enabled, the sink connector physically deletes the data. This feature must be used together with insert.mode=upsert and primary.key.mode=record key . Valid values: _ Enable Disable |
| Primary Key Mode | The primary key retrieval mode. Valid values: From Record Key: retrieves primary keys from record key . This mode is required for handling _ DELETE events. From Record Value: retrieves primary keys from record value . _ From Kafka Coordinates: retrieves primary keys from kafka . |
| Primary Key Fields | The names of the primary key fields. Separate multiple fields with commas (,). |

|   |   | insert.mode=upsert and |
|---|---|---|
| te | primary.key.mode=record key _ |   |

**Advanced Configuration**

| Parameter | Description |
|---|---|
| Quote Identifiers | Specify whether to use quotation marks ("") to enclose table names and column names. The default value is true and cannot be modified. |
| Field Include List | The list of fields to be included. Separate multiple fields with commas (,). If you leave this parameter empty, all fields are included. |

##### 2.9.2.20 polardb-for-mysql-source-connector

This topic describes how to configure the parameters for polardb-for-mysql-source-connector. You are creating a connector, and the connector type is set to polardb-for-mysql-sourceconnector. For more information about how to create a connector, see the Create a connector section in the Connect topic.

**Parameters**

**Basic Configuration**

| Parameter | Description |
|---|---|
| Max Tasks | The maximum number of parallel tasks. The default value is 1 and cannot be modified. |

**Connection Configuration**

| Parameter | Description |
|---|---|
| Database Hostname | The IP address of the PolarDB for MySQL database server. |
| Database Port | The port of the PolarDB for MySQL database server. |
| Username | The username used to connect to the PolarDB for MySQL database. |
| Password | The password used to connect to the PolarDB for MySQL database. |
| Database Server ID | The numeric ID of the database client. The ID must be unique among all running database processes in the PolarDB for MySQL cluster. |

**Data Configuration**

| Parameter | Description |
|---|---|
| Database Include List | An optional list of regular expressions separated with commas (,). It is used to match the names of databases that you want to monitor. |

| Table Include List | An optional list of regular expressions separated with commas (,). It is used to match the fully-qualified identifiers of tables that you want to monitor. Example: <database>. <table> . |   |   |
|---|---|---|---|
|   |   | <database>. |   |
| Topic Prefix | The prefix of the generated topics |   |   |
| Schema History Kafka Servers | The host and port pairs used by the connector to establish the initial connection to the Kafka cluster for retrieving the database schema history. The Kafka cluster must be the same as the one used by the Kafka connect process. |   |   |
| Schema History Kafka Topic | The name of the Kafka topic where the connector stores the database schema history. |   |   |
| Snapshot Mode | The snapshot policy used when the connector is started. Valid values: Initial Full Snapshot Schema Only Snapshot Never Snapshot When Needed Snapshot |   |   |
| Key Schema Enable | Specify whether to include schema information in message keys. Valid values: Enable Disable |   |   |
| Value Schema Enable | Specify whether to include schema information in message values. Valid values: Enable Disable |   |   |

|   | <table> |
|---|---|

##### 2.9.2.21 polardb-for-postgresql-sink-connector

This topic describes how to configure the parameters for polardb-for-postgresql-sinkconnector. You are creating a connector, and the connector type is set to polardb-for-postgresql-sinkconnector. For more information about how to create a connector, see the Create a connector section in the Connect topic.

**Parameters**

**Basic Configuration**

| Parameter | Description |
|---|---|
| Max Tasks | The maximum number of parallel tasks. Default value: 12. Valid values: 1 to 12. |

**Connection Configuration**

| Parameter | Description |
|---|---|
| Database Connection URL | The Java Database Connectivity (JDBC) connection URL of the PolarDB for PostgreSQL database. Example: jdbc:postgresql://<host>:<port>/<database> . |
| Username | The username used to connect to the PolarDB for PostgreSQL database. |
| Password | The password used to connect to the PolarDB for PostgreSQL database. |
| Database Time Zone | The time zone of the PolarDB for PostgreSQL database. |

**Data Configuration**

| Parameter | Description |
|---|---|
| Kafka Topics | The Kafka topics from which messages will be consumed. Separate multiple topics with commas (,). |
| Target Table Name | The name of the PolarDB for PostgreSQL table to which data is written. It must be a fully-qualified identifier. Example: <schema>.<table> . |
| Insert Mode | The mode in which data is inserted. Valid values: insert: Data is only inserted. upsert: Data is inserted or updated. update: Data is only updated. |

| Enable Delete | Specify whether to synchronize DELETE events to the destination table. After this feature is enabled, the sink connector physically deletes the data. This feature must be used together with insert.mode=upsert and primary.key.mode=record key . Valid values: _ Enable Disable |
|---|---|
| Primary Key Mode | The primary key retrieval mode. Valid values: From Record Key: retrieves primary keys from record key . This mode is required for handling _ DELETE events. From Record Value: retrieves primary keys from record value . _ From Kafka Coordinates: retrieves primary keys from kafka . |
| Primary Key Fields | The names of the primary key fields. Separate multiple fields with commas (,). |

|   |   | insert.mode=upsert and |
|---|---|---|
| te | primary.key.mode=record key _ |   |

**Advanced Configuration**

| Parameter | Description |
|---|---|
| Quote Identifiers | Specify whether to use quotation marks ("") to enclose table names and column names. The default value is true and cannot be modified. |
| Field Include List | The list of fields to be included. Separate multiple fields with commas (,). If you leave this parameter empty, all fields are included. |

##### 2.9.2.22 polardb-for-postgresql-source-connector

This topic describes how to configure the parameters for polardb-for-postgresql-sourceconnector. You are creating a connector, and the connector type is set to polardb-for-postgresql-sourceconnector. For more information about how to create a connector, see the Create a connector section in the Connect topic.

**Parameters**

**Basic Configuration**

| Parameter | Description |
|---|---|
| Max Tasks | The maximum number of parallel tasks. The default value is 1 and cannot be modified. |

**Connection Configuration**

| Parameter | Description |
|---|---|
| Database Hostname | The resolvable hostname or IP address of the PolarDB for PostgreSQL database server. |
| Database Port | The port of the PolarDB for PostgreSQL database server. |
| Username | The username used to connect to the PolarDB for PostgreSQL database. |
| Password | The password used to connect to the PolarDB for PostgreSQL database. |
| Database Name | The name of the PolarDB for PostgreSQL database that you want to monitor. |

**Data Configuration**

| Parameter | Description |
|---|---|
| Table Include List | The tables to be monitored in the schema.table format. Separate multiple tables with commas (,). |
| Topic Prefix | The name prefix of the generated Kafka topics. It must not be duplicated with the prefixes of topics specified for other connectors. The prefix must not contain periods (.). |
| Snapshot Mode | The snapshot policy used when the connector is started. Valid values: Initial Full Snapshot Always Snapshot Never Snapshot Exported Snapshot |

| Key Schema Enable | Specify whether to include schema information in message keys. Valid values: Enable Disable |
|---|---|
| Value Schema Enable | Specify whether to include schema information in message values. Valid values: Enable Disable |

**Advanced Configuration**

| Parameter | Description |
|---|---|
| Topic Connector Replacement Rule | The topic name replacement rule, which cannot be changed. |

##### 2.9.2.23 polardb-x-2.0-sink-connector

This topic describes how to configure the parameters for polardb-x-2.0-sink-connector. You are creating a connector, and the connector type is set to polardb-x-2.0-sink-connector. For more information about how to create a connector, see the Create a connector section in the Connect topic.

**Parameters**

**Basic Configuration**

| Parameter | Description |
|---|---|
| Max Tasks | The maximum number of parallel tasks. Default value: 12. Valid values: 1 to 12. |

**Connection Configuration**

| Parameter | Description |
|---|---|
| Database Connection URL | The Java Database Connectivity (JDBC) URL that you can use to connect to the PolarDB-X database, in the format of jdbc:mysql://host:port/database?parameters . |
| Username | The username used to connect to the PolarDB-X database. |

| Password | The password used to connect to the PolarDB-X database. |
|---|---|
| Database Time Zone | The time zone of the PolarDB-X database. |

**Data Configuration**

| Parameter | Description |
|---|---|
| Kafka Topics | The Kafka topics from which messages will be consumed. Separate multiple topics with commas (,). |
| Target Table Name | The name of the MySQL table to which data is written. |
| Insert Mode | The mode in which data is inserted. Valid values: insert: Data is only inserted. upsert: Data is inserted or updated. update: Data is only updated. |
| Enable Delete | Specify whether to synchronize DELETE events to the destination table. After this feature is enabled, the sink connector physically deletes the data. This feature must be used together with insert.mode=upsert and primary.key.mode=record key . Valid values: _ Enable Disable |
| Primary Key Mode | The primary key retrieval mode. Valid values: From Record Key: retrieves primary keys from record key . This mode is required for handling _ DELETE events. From Record Value: retrieves primary keys from record value . _ From Kafka Coordinates: retrieves primary keys from kafka . |
| Primary Key Fields | The names of the primary key fields. Separate multiple fields with commas (,). |

|   |   | insert.mode=upsert and |
|---|---|---|
| te | primary.key.mode=record key _ |   |

**Advanced Configuration**

| Parameter | Description |
|---|---|

| Quote Identifiers | Specify whether to use quotation marks ("") to enclose table names and column names. The default value is true and cannot be modified. |
|---|---|
| Field Include List | The list of fields to be included. Separate multiple fields with commas (,). If you leave this parameter empty, all fields are included. |

##### 2.9.2.24 polardb-x-2.0-source-connector

This topic describes how to configure the parameters for polardb-x-2.0-source-connector. You are creating a connector, and the connector type is set to polardb-x-2.0-sourceconnector. For more information about how to create a connector, see the Create a connector section in the Connect topic.

**Parameters**

**Basic Configuration**

| Parameter | Description |
|---|---|
| Max Tasks | The maximum number of parallel tasks. The default value is 1 and cannot be modified. |

**Connection Configuration**

| Parameter | Description |
|---|---|
| Database Hostname | The IP address of the PolarDB-X database server. |
| Database Port | The port of the PolarDB-X database server. |
| Username | The username used to connect to the PolarDB-X database. |
| Password | The password used to connect to the PolarDB-X database. |
| Database Server ID | The numeric ID of the database client. The ID must be unique among all running database processes in the PolarDB-X cluster. |

**Data Configuration**

| Parameter | Description |
|---|---|
| Database Include List | An optional list of regular expressions separated by commas (,). It is used to match the names of databases that you want to monitor. |
| Table Include List | An optional list of regular expressions separated by commas (,). It is used to match the fully-qualified identifiers of tables that you want to monitor. Example: <database>. <table> . |
| Topic Prefix | The prefix of the generated topics. |
| Schema History Kafka Servers | The host and port pairs used by the connector to establish the initial connection to the Kafka cluster for retrieving the database schema history. The Kafka cluster must be the same as the one used by the Kafka connect process. |
| Schema History Kafka Topic | The name of the Kafka topic where the connector stores the database schema history. |
| Snapshot Mode | The snapshot policy used when the connector is started. Valid values: Initial Full Snapshot Schema Only Snapshot Never Snapshot When Needed Snapshot |
| Key Schema Enable | Specify whether to include schema information in message keys. Valid values: Enable Disable |
| Value Schema Enable | Specify whether to include schema information in message values. Valid values: Enable Disable |

|   | <table> |
|---|---|

##### 2.9.2.25 postgresql-sink-connector.json

This topic describes how to configure the parameters for postgresql-sink-connector. You are creating a connector, and the connector type is set to postgresql-sink-connector. For more information about how to create a connector, see Create a connector.

**Configuration description**

**Basic Configuration**

| Parameter | Description |
|---|---|
| Max Tasks | The maximum number of tasks for parallel processing. The number of tasks must be between 1 and 12. |

**Connection Configuration**

| Parameter | Description |
|---|---|
| Database Connection URL | The JDBC URL that you can use to connect to the PostgreSQL database. |
| Username | The username that is used to connect to the PostgreSQL database. |
| Password | The password that is used to connect to the PostgreSQL database. |
| Database Time Zone | The time zone used by the database. Example: Asia/Shanghai. |

**Data Configuration**

| Parameter | Description |
|---|---|
| Kafka Topics | The Kafka topics from which messages will be consumed. Separate multiple topics with commas (,). |
| Target Table Name | The name of the PostgreSQL table to which you want to write data. |
| Insert Mode | Insert mode of input data: insert: inserts data only. upsert: inserts or updates data. update: updates data only. |

| Primary Key Mode | The retrieval mode of the primary key: record value: obtains the primary key from record values. _ |
|---|---|
| Primary Key Fields | The name of the primary key field. Separate multiple fields with commas (,). |

**Advanced Configuration**

| Parameter | Description |
|---|---|
| Quote Identifiers | Specifies whether to use quotation marks for table and column names. Default value: true . |
| Field Include List | The fields that you want to include. Separate multiple fields with commas (,). If you leave this parameter empty, all fields are included. |

##### 2.9.2.26 postgresql-source-connector.json

This topic describes how to configure the parameters for postgresql-source-connector. You are creating a connector, and the connector type is set to postgresql-source-connector. For more information about how to create a connector, see Create a connector.

**Configuration description**

**Basic Configuration**

| Parameter | Description |
|---|---|
| Max Tasks | The maximum number of tasks for parallel processing. The number of tasks must be 1. |

**Connection Configuration**

| Parameter | Description |
|---|---|
| Database Hostname | The resolvable hostname or IP address of the PostgreSQL database server. |
| Database Port | The port number of the PostgreSQL database server. |

| Username | The username that is used to connect to the PostgreSQL database server. |
|---|---|
| Password | The password that is used to connect to the PostgreSQL database server. |
| Database Name | The name of the PostgreSQL database that you want to monitor. |

**Data Configuration**

| Parameter | Description |
|---|---|
| Table Include List | The tables to be monitored in the schema.table format. Separate multiple tables with commas (,). |
| Topic Prefix | The prefix of the Kafka topic name. Note Note that the topic prefix of a connector must not duplicate or contain the topic prefix of any other connector. |

**Advanced Configuration**

| Parameter | Description |
|---|---|
| Topic Connector Replacement Rule | The replacement rule for topic names, which defaults to $1 $2 $3 . Underscores ( ) are used to replace the _ _ _ default dot ( . ) separators. |

##### 2.9.2.27 prometheus-sink-connector

This topic describes how to configure the parameters for prometheus-sink-connector. You are creating a connector, and the connector type is set to prometheus-sink-connector. For more information about how to create a connector, see the Create a connector section in the Connect topic.

**Parameters**

**Basic Configuration**

| Parameter | Description |
|---|---|
| Max Tasks | The maximum number of parallel tasks. Valid values: 1 to 12. |
| Kafka Topics | The Kafka topics from which messages are consumed. Separate multiple topics with commas (,). |

**Connection Configuration**

| Parameter | Description |
|---|---|
| Prometheus URL | The endpoint of the HTTP API of Managed Service for Prometheus. Example: https://prometheus:9090 . |
| Remote Write URL | The remote write endpoint of Managed Service for Prometheus. Example: https://prometheus:9090/api/v1/write . |
| Username | The username used to authenticate to Managed Service for Prometheus. |
| Password | The password used to authenticate to Managed Service for Prometheus. |
| Skip SSL Verification | Specify whether to skip SSL certificate verification. This setting is suitable for environments using self-signed certificates. |
| Connection Timeout (ms) | The timeout period of HTTP connections in milliseconds. |

**Write Configuration**

| Parameter | Description |
|---|---|
| Batch Size | The maximum number of records that can be written per batch. When the upper limit is reached, remote write is triggered. |
| Batch Flush Interval (ms) | The batch flush interval in milliseconds. Remote write is triggered when the interval ends even if the batch.size upper limit is not reached. |

| Remote Write Timeout (ms) | The timeout period of HTTP requests for remote write. Unit: milliseconds. |
|---|---|
| Extra Labels | Additional labels added to all metrics. Format: key1=value1,key2=value2 . |

**Dead Letter Queue Configuration**

| Parameter | Description |
|---|---|
| Enable DLQ | Specify whether to enable the dead letter queue feature. Valid values: true and false. After this feature is enabled, messages that cannot be processed are sent to the specified topic. |
| DLQ Topic | The name of the Kafka topic used by the dead letter queue. Note This parameter is required when Enable DLQ is set to true. |
| DLQ Bootstrap Servers | The Kafka bootstrap servers used by the dead letter queue. Note This parameter is required when Enable DLQ is set to true. |

**Retry Configuration**

| Parameter | Description |
|---|---|
| Max Retries | The maximum number of attempts to retry a failed request. |
| Retry Backoff (ms) | The initial backoff in milliseconds. It increases exponentially after each retry attempt. |

##### 2.9.2.28 prometheus-source-connector

This topic describes how to configure the parameters for prometheus-source-connector. You are creating a connector, and the connector type is set to prometheus-source-connector. For more information about how to create a connector, see the Create a connector section in the Connect topic.

**Parameters**

**Basic Configuration**

| Parameter | Description |
|---|---|
| Max Tasks | The maximum number of parallel tasks. Valid values: 1 to 12. We recommend that you keep the number of tasks same as the number of PromQL queries. |

**Connection Configuration**

| Parameter | Description |
|---|---|
| Prometheus URL | The endpoint of the HTTP API of Managed Service for Prometheus. Example: https://prometheus:9090 . |
| Username | The username used to authenticate to Managed Service for Prometheus. |
| Password | The password used to authenticate to Managed Service for Prometheus. |
| Skip SSL Verification | Specify whether to skip SSL certificate verification. This setting is suitable for environments using self-signed certificates. |
| Connection Timeout (ms) | The timeout period of HTTP connections in milliseconds. |

**Query Configuration**

| Parameter | Description |
|---|---|
| PromQL Queries | PromQL queries separated by commas (,). Example: up,http requests total . _ _ |
| Kafka Topic | The name of the Kafka topic to which metric data is written. |
| Poll Interval (ms) | The interval between two PromQL queries, in milliseconds. Minimum value: 1000. |
| Query Timeout (s) | The timeout period of a PromQL query, in seconds. |

**Retry Configuration**

| Parameter | Description |
|---|---|
| Max Retries | The maximum number of attempts to retry a failed request. |
| Retry Backoff (ms) | The initial backoff in milliseconds. It increases exponentially after each retry attempt. |

##### 2.9.2.29 redis-sink-connector

This topic describes how to configure the parameters for redis-sink-connector. You are creating a connector, and the connector type is set to redis-sink-connector. For more information about how to create a connector, see the Create a connector section in the Connect topic.

**Parameters**

**Basic Configuration**

| Parameter | Description |
|---|---|
| Max Tasks | The maximum number of tasks that can be created for the connector. Default value: 1. Valid values: 1 to 10. |
| Topics | The Kafka topics from which messages are consumed. Separate multiple topics with commas (,). |

**Connection Configuration**

| Parameter | Description |
|---|---|
| Redis Hosts | The addresses of ApsaraDB for Redis servers, in the host:port format. Separate multiple addresses with commas (,). |
| Password | The password used to connect to the ApsaraDB for Redis database. |

| Database Index | The index to be used in the ApsaraDB for Redis database. Default value: 0. Valid values: 0 to 15. |
|---|---|

**Data Configuration**

| Parameter | Description |
|---|---|
| Redis Command | The command used to write data to the ApsaraDB for Redis database. Valid values: SET HSET LPUSH RPUSH SADD ZADD |
| Key Strategy | The key generation policy. Valid values: TOPIC TOPIC PARTITION _ KAFKA KEY _ CUSTOM |
| Key Prefix | The key prefix. |
| Key Separator | The delimiter used to separate keys and values. |
| Batch Size | The maximum number of records that can be written to ApsaraDB for Redis per batch. Default value: 100. Valid values: 1 to 10000. |
| TTL (Seconds) | The TTL of keys in seconds. A value of 0 indicates that keys never expire. Default value: 0. |

**Advanced Configuration**

| Parameter | Description |
|---|---|

| Max Retries | The maximum number of attempts to retry a write failure. Default value: 3. Valid values: 0 to 10. |
|---|---|
| Null Value Behavior | The policy used to handle null values. Valid values: IGNORE DELETE FAIL |

##### 2.9.2.30 redis-source-connector

This topic describes how to configure the parameters for redis-source-connector. You are creating a connector, and the connector type is set to redis-source-connector. For more information about how to create a connector, see the Create a connector section in the Connect topic.

**Parameters**

**Basic Configuration**

| Parameter | Description |
|---|---|
| Max Tasks | The maximum number of parallel tasks. The value is fixed to 1. |
| Target Topic | The name of the Kafka topic to which you want to send data. |

**Connection Configuration**

| Parameter | Description |
|---|---|
| Redis Hosts | The addresses of ApsaraDB for Redis servers, in the host:port format. Separate multiple addresses with commas (,). |
| Password | The password used to connect to the ApsaraDB for Redis database. |

| Database Index | The index to be used in the ApsaraDB for Redis database. Default value: 0. Valid values: 0 to 15. |
|---|---|

**Data Configuration**

| Parameter | Description |
|---|---|
| Source Mode | The data source capture mode. Valid values: PUBSUB KEYSPACE STREAM POLL |
| Subscribe Channels | The channels to which you want to subscribe in PUBSUB mode. Separate multiple channels with commas (,). |
| Subscribe Patterns | The modes of the channels to which you want to subscribe in PUBSUB mode. Wildcard characters are supported. Separate multiple modes with commas (,). |
| Keyspace Events | The types of events for which you want to listen in KEYSPACE mode. Valid values; set del expired evicted all |
| Keyspace Pattern | The key modes for which you want to listen in KEYSPACE mode. Wildcard characters are supported. |
| Stream Keys | The Stream keys to read in STREAM mode. Separate multiple keys with commas (,). |
| Poll Pattern | The key modes to be scanned in POLL mode. |
| Poll Interval (ms) | The scan interval in POLL mode. Unit: milliseconds. Default value: 5000. |

**Advanced Configuration**

| Parameter | Description |
|---|---|
| Batch Size | The maximum number of messages that can be sent to ApsaraMQ for Kafka per batch. Default value: 100. Valid values: 1 to 10000. |
| Batch Timeout (ms) | The timeout period for sending messages in batches. Unit: milliseconds. Default value: 1000. |
| Max Retries | The maximum number of attempts to retry a write failure. Default value: 3. Valid values: 0 to 10. |

##### 2.9.2.31 sls-sink-connector

This topic describes how to configure the parameters for sls-sink-connector. You are creating a connector, and the connector type is set to sls-sink-connector. For more information about how to create a connector, see the Create a connector section in the Connect topic.

**Parameters**

**Basic Configuration**

| Parameter | Description |
|---|---|
| Max Tasks | The maximum number of parallel tasks. Valid values: 1 to 12. |
| Kafka Topics | The Kafka topics from which messages are consumed. Separate multiple topics with commas (,). |

**SLS Connection Configuration**

| Parameter | Description |
|---|---|
| SLS Endpoint | The endpoint of Simple Log Service (SLS). |

| AccessKey ID | The AccessKey ID of the Apsara Stack tenant account that has permissions to write data to the Logstore. |
|---|---|
| AccessKey Secret | The AccessKey secret of the Apsara Stack tenant account that has permissions to write data to the Logstore. |
| SLS Project | The name of the SLS project. |
| Logstore Name | The name of the Logstore to which data is written. |

**Write Configuration**

| Parameter | Description |
|---|---|
| Data Format | The format in which data is written to SLS. Valid values: JSON Format (json) Raw String (raw) |
| Batch Size | The maximum number of log entries that can be written to SLS per batch. Default value: 2000. Value values: 1 to 10000. |

**Data Configuration**

| Parameter | Description |
|---|---|
| Value Converter | The serialization format of message values, which is automatically selected based on Data Format. JSON Format (json): The JSON converter is used. Raw String (raw): The string converter is used. Note The value cannot be modified. |

##### 2.9.2.32 sls-source-connector

This topic describes how to configure the parameters for sls-source-connector. You are creating a connector, and the connector type is set to sls-source-connector. For more information about how to create a connector, see the Create a connector section in the Connect topic.

**Parameters**

**Basic Configuration**

| Parameter | Description |
|---|---|
| Kafka Topic | The name of the Kafka topic to which log data is written. |

**SLS Connection Configuration**

| Parameter | Description |
|---|---|
| SLS Endpoint | The endpoint of Simple Log Service (SLS). |
| AccessKey ID | The AccessKey ID of the Apsara Stack tenant account that has permissions to write data to the Logstore. |
| AccessKey Secret | The AccessKey secret of the Apsara Stack tenant account that has permissions to write data to the Logstore. |
| SLS Project | The name of the SLS project. |
| Logstore Name | The name of the Logstore to which data is written. |

**Consume Configuration**

| Parameter | Description |
|---|---|
| Consume Start Position | The initial position where logs are consumed. Valid values: From Beginning (begin) From Latest (end) Specific Time (specific time) _ |
| Consume Start Timestamp | Enter a timestamp accurate to seconds in the Unix format. Example: 1700000000. Note This parameter is available when Consume Start Position is set to Specific Time (specific time). _ |

| Consumer Group Name | The name of the SLS consumer group, which is used for resumable upload. We recommend that you use a unique name in case of name conflicts. |
|---|---|
| Consumer Group Password | The password of the SLS consumer group. This parameter is optional. |

**Batch Configuration**

| Parameter | Description |
|---|---|
| Batch Size | The maximum number of log entries that can be pulled from SLS each time. Default value: 100. Value values: 1 to 10000. |
| Poll Interval (ms) | The polling interval when no new data is available. Unit: milliseconds. Default value: 1000. Valid values: 100 to 60000. |

**Data Configuration**

| Parameter | Description |
|---|---|
| Value Converter | The serialization format of message values. The JSON converter is used and cannot be changed. |

##### 2.9.2.33 spark-sink-connector

This topic describes how to configure the parameters for spark-sink-connector. You are creating a connector, and the connector type is set to spark-sink-connector. For more information about how to create a connector, see the Create a connector section in the Connect topic.

**Parameters**

**Basic Configuration**

| Parameter | Description |
|---|---|
| Max Tasks | The maximum number of parallel tasks. Valid values: 1 to 12. |

| Command Topic | The name of the Kafka topic that receives commands submitted by Spark jobs. The commands use the JSON format. |
|---|---|

**Livy Connection**

| Parameter | Description |   |   |
|---|---|---|---|
| Livy URL | The endpoint of the Livy REST API. Example: http://emr- header-1:8998 . |   |   |
|   |   | http://emr- |   |
| Auth Type | The type of Livy authentication. |   |   |
| Username | The username used for Livy authentication. |   |   |
| Password | The password used for Livy authentication. |   |   |

|   | header-1:8998 |
|---|---|

**Job Configuration**

| Parameter | Description |
|---|---|
| Max Concurrent Jobs | The maximum number of concurrent Spark jobs supported by a task. |
| Job Timeout (min) | The timeout period of Spark jobs in minutes. A Spark job is terminated when the timeout period ends. |
| Poll Interval (ms) | The interval for querying the status of Livy jobs, in milliseconds. |
| Status Topic | The name of the Kafka topic to which job status is written. |

**Retry Configuration**

| Parameter | Description |
|---|---|
| Max Retries | The maximum number of attempts to retry a failed Livy API call. |
| Retry Backoff (ms) | The initial retry backoff in milliseconds. The actual interval increases exponentially. |

**Data Configuration**

| Parameter | Description |
|---|---|
| Value Converter | The value converter class. The default value is org.apache.kafka.connect.json.JsonConverter and cannot be modified. |

##### 2.9.2.34 tablestore-sink-connector

This topic describes how to configure the parameters for tablestore-sink-connector. You are creating a connector, and the connector type is set to tablestore-sink-connector. For more information about how to create a connector, see the Create a connector section in the Connect topic.

**Parameters**

**Basic Configuration**

| Parameter | Description |
|---|---|
| Max Tasks | The maximum number of parallel tasks. Default value: 1. We recommend that you keep the number of tasks same as the number of topic partitions. |

**Connection Configuration**

| Parameter | Description |
|---|---|
| TableStore Endpoint | The endpoint of the Tablestore instance. Example: http://xxxx . |
| Instance Name | The name of the Tablestore instance. |
| Access Key ID | The AccessKey ID of the Apsara Stack tenant account. |
| Access Key Secret | The AccessKey secret of the Apsara Stack tenant account. |

**Table Mapping Configuration**

| Parameter | Description |
|---|---|

| Kafka Topics | The Kafka topics from which messages are consumed. Separate multiple topics with commas (,). |
|---|---|
| Topic to Table Mapping | The explicit topic-to-table mappings in Tablestore. Format: topic1:table1,topic2:table2 . |

**Primary Key Configuration**

| Parameter | Description |
|---|---|
| Primary Key Mode | The source of primary keys is fixed to kafka (Kafka metadata: topic + partition + offset). |

**Write Configuration**

| Parameter | Description |
|---|---|
| Insert Mode | Valid values: Overwrite (put) Incremental Update (update) |
| Delete Mode | Valid values: No Deletion Row Deletion Column Deletion (update mode only) Note Column deletion is available only when the insert mode is set to Incremental Update (update). |
| Auto Create Table | Specify whether to automatically create the destination table. After this feature is enabled, if the destination does not exist, the system automatically creates one. If the table already exists but the primary keys do not match, an error is thrown. Valid values: Yes No |
| Buffer Size | The size of the buffer queue in memory. Unit: messages. Default value: 1024. |
| Max Concurrency | The maximum number of concurrent requests. Default value: 10. |

**Data Configuration**

| Parameter | Description |
|---|---|
| Value Converter | The value converter class. The default value is org.apache.kafka.connect.json.JsonConverter and cannot be modified. |

##### 2.9.2.35 tablestore-source-connector

This topic describes how to configure the parameters for tablestore-source-connector. You are creating a connector, and the connector type is set to tablestore-source-connector. For more information about how to create a connector, see the Create a connector section in the Connect topic.

**Parameters**

**Basic Configuration**

| Parameter | Description |
|---|---|
| Max Tasks | The maximum number of parallel tasks. The default value is 1 and cannot be modified. |

**Connection Configuration**

| Parameter | Description |
|---|---|
| TableStore Endpoint | The endpoint of the Tablestore instance. Example: http://xxxx . |
| Instance Name | The name of the Tablestore instance. |
| Access Key ID | The AccessKey ID of the Apsara Stack tenant account. |
| Access Key Secret | The AccessKey secret of the Apsara Stack tenant account. |

**Source Configuration**

| Parameter | Description |
|---|---|

| Source Table Name | The name of the Tablestore table to read. The table must have the Stream feature enabled. |
|---|---|
| Target Kafka Topic | The name of the Kafka topic to which change data is written. |
| Start Mode | The initial position where data is read during the first-time startup. Valid values: Latest (LATEST) Earliest (TRIM HORIZON) _ |

**Performance Configuration**

| Parameter | Description |
|---|---|
| Poll Interval (ms) | The polling interval when no new data is available. Unit: milliseconds. Minimum value: 100. Default value: 1000. |
| Batch Size | The maximum number of records that can be read from the Stream each time. Default value: 100. Suggested values: 10 to 500. |

**Data Configuration**

| Parameter | Description |
|---|---|
| Value Converter | The value converter class. The default value is org.apache.kafka.connect.json.JsonConverter . |

##### 2.9.2.36 Transform configuration

This article describes how to configure conditional predicates and converters.

**Configure conditional predicates**

> **Note:** You can click **Add Predicate** to add at most 10 conditional predicates.
> A conditional predicate can be referenced by multiple converters.

| Parameter | Description |
|---|---|
| Predicate Type | HasHeaderKey: checks whether the specified key exists in the headers of records. RecordIsTombstone: checks whether records are tombstone records. The value of a tombstone record is null. TopicNameMatches: checks whether topic names match the specified regular expression. |
| Predicate Name | The name of the predicate. Predicate names must be unique. |
| Regex Pattern | Note This parameter is available only when TopicNameMatches is selected as the predicate type. The regular expression used to match topic names. |
| Header Key Name | Note This parameter is available only when HasHeaderKey is selected as the predicate type. The header key to be checked. |

**Configure converters**

> **Note:** You can click **Add converter** to add at most 10 converters.

| Parameter | Description |
|---|---|

| Converter type | Valid values: Cast: converts a field, key, or value to a specific type. For example, forcefully convert an integer field to a field with smaller width. DropHeaders: removes one or more headers from each record. ExtractField: extracts a specific field from a Struct or Map as a new record value. Filter: discards records so that the records will not be converted. It is commonly used with predicates to filter out records that match specific conditions. Flatten: a flat nested data structure that generates field names by connecting field names of each level with a configurable delimiter. HeaderFrom: moves or replicates fields in the key or value of a record to the header of the record. HoistField: wraps data in a Struct or Map by using the specified field name. InsertField: inserts a field by using a property of the record metadata or a static value. InsertHeader: inserts a header to each record. MaskField: uses a valid null value, such as 0, false, or empty string, to mask the specified field. RegexRouter: uses a regular expression and a replacement string to update the recorded topics. ReplaceField: filters out or renames fields. TimestampConverter: converts timestamps between different formats, such as Unix epoch, string, connect date, and timestamp. ValueToKey: replaces the record key with a subset of fields in the record value. ExtractNewRecordState: folds the Change Data Capture (CDC) events of Debezium into a simple structure and extracts the after part as the message value. This method is suitable for scenarios where the downstream node does not support Debezium. Note Click Description to view the usage notes for the converter. |
|---|---|
| Converter name | The name of the converter. Converter names must be unique. |

| Configuration related to the selected converter type | Complete the converter configuration based on the selected converter type. The following tables describe the configuration for each converter type. |
|---|---|
| Predicate (Optional) | If predicates are used, the converter is triggered only when the specified conditions are met. Select Negate to trigger the converter when the specified conditions are not met. |

**Cast**

| Parameter | Description |
|---|---|
| Apply To | Specify whether to convert the record key or record value. Record Value Record Key |
| Cast Specification (spec) | A list of fields and field types in the format of field1:type,field2:type . The following field types are supported: int8, int16, int32, int64, float32, float64, boolean, and string. |

**DropHeaders**

| Parameter | Description |
|---|---|
| Headers to Remove (headers) | The list of headers to remove in the format of header1,header2 . Multiple headers are separated with commas (,). |

**ExtractField**

| Parameter | Description |
|---|---|
| Apply To | Specify whether to convert the record key or record value. Record Value Record Key |

| Field Name to Extract (field) | The name of the field to be extracted from the record. |
|---|---|

**Filter**

None

**Flatten**

| Parameter | Description |
|---|---|
| Apply To | Specify whether to convert the record key or record value. Record Value Record Key |
| Field Name Delimiter (delimiter) | The delimiter used to connect the input record field names during the generation of output record field names. |

**HeaderFrom**

| Parameter | Description |
|---|---|
| Apply To | Specify whether to convert the record key or record value. Record Value Record Key |
| Source Field Names (fields) | The names of the fields to be replicated or moved to the record header. Separate multiple field names with commas (,). Format: field1,field2 . |
| Target Header Names (headers) | Header names corresponding to the specified field names. Separate multiple header names with commas (,). Format: header1,header2 . |
| Operation Type (operation) | Valid values: move: moves the fields to the headers. The fields are removed from the key or value. Copy: copies the fields to the headers. The fields are retained in the key or value. |

**HoistField**

| Parameter | Description |
|---|---|
| Apply To | Specify whether to convert the record key or record value. Record Value Record Key |
| Wrapper Field Name (field) | The name of the field created in the result Struct or Map. |

**InsertField**

| Parameter | Description |
|---|---|
| Apply To | Specify whether to convert the record key or record value. Record Value Record Key |
| Topic Field Name (topic.field) | The field name of the Kafka topic. This parameter applies only to sink connectors. Note If the suffix of the field name is ! , the field is a required field. In this case, the value of the field must not be null. If the suffix of the field name is ? , the field is optional. The value of the field can be null. By default, the ? or ! parameter is not specified. If the suffix is ? , the suffix is optional. |

| Partition Field Name (partition.field) | The field name of the Kafka partition. This parameter applies only to sink connectors. Note If the suffix of the field name is ! , the field is a required field. In this case, the value of the field must not be null. If the suffix of the field name is ? , the field is optional. The value of the field can be null. By default, the ? or ! parameter is not specified. If the suffix is ? , the suffix is optional. |
|---|---|
| Offset Field Name (offset.field) | The field name of the Kafka offset. This parameter applies only to sink connectors. Note If the suffix of the field name is ! , the field is a required field. In this case, the value of the field must not be null. If the suffix of the field name is ? , the field is optional. The value of the field can be null. By default, the ? or ! parameter is not specified. If the suffix is ? , the suffix is optional. |

| Timestamp Field Name (timestamp.field) | The field name of the record timestamp. This parameter applies only to sink connectors. Note If the suffix of the field name is ! , the field is a required field. In this case, the value of the field must not be null. If the suffix of the field name is ? , the field is optional. The value of the field can be null. By default, the ? or ! parameter is not specified. If the suffix is ? , the suffix is optional. |
|---|---|
| Static Field Name (static.field) | The name of the static field. Note If the suffix of the field name is ! , the field is a required field. In this case, the value of the field must not be null. If the suffix of the field name is ? , the field is optional. The value of the field can be null. By default, the ? or ! parameter is not specified. If the suffix is ? , the suffix is optional. |
| Static Field Value (static.value) | The value of the static field. The value is required if the name of the static field is specified. |

**InsertHeader**

| Parameter | Description |
|---|---|
| Header Name (header) | The name of the header to be added. |
| Header Value (value.literal) | The value of the header to be added to all records. |

**MaskField**

| Parameter | Description |
|---|---|

| Apply To | Specify whether to convert the record key or record value. Record Value Record Key |
|---|---|
| Fields to Mask (fields) | The names of the fields to be masked. Separate multiple field names with commas (,). Format: field1,field2 . |
| Custom Replacement Value (replacement) | The custom value to replace the values of all fields. Note The value can be a number or a non-empty string. If you leave this parameter empty, a null value is used. |

**RegexRouter**

| Parameter | Description |
|---|---|
| Regular Expression (regex) | The regular expression to be used. |
| Replacement String (replacement) | The string for replacement. Use java.util.regex.Matcher#replaceFirst() . |

**ReplaceField**

| Parameter | Description |
|---|---|
| Apply To | Specify whether to convert the record key or record value. Record Value Record Key |
| Fields to Include (include) | The list of fields to include. If you specify this parameter, only the specified fields are used. Separate multiple fields with commas (,). Format: field1,field2 . |

| Fields to Exclude (exclude) | The list of fields to exclude. The parameter has a higher priority than Fields to Include (include). Separate multiple fields with commas (,). Format: field1,field2 . |
|---|---|
| Field Rename Mappings (renames) | The list of field renaming mappings. Separate multiple mappings with commas (,). Separate the old name and new name in each mapping with a colon (:). Format: oldName1:newName1,oldName2:newName2 . |

**TimestampConverter**

| Parameter | Description |
|---|---|
| Apply To | Specify whether to convert the record key or record value. Record Value Record Key |
| Timestamp Field (field) | The name of the field that contains the timestamp. If you leave this parameter empty, the value is a timestamp. |
| Target Type (target.type) | The expected format of the timestamp. Valid values: String Unix Date Time Timestamp |
| Time Format (format) | The timestamp format compatible with SimpleDateFormat . It is used to generate output when type=string or used to parse the input content when the input content is a string. |

**ValueToKey**

| Parameter | Description |
|---|---|
| Fields to Extract as Key (fields) | The names of the fields to be extracted from the record value as the record key. Separate multiple field names with commas (,). Format: field1,field2 . |

| Message Queue for Apache Kafka | User Guide·Console operation |
|---|---|

**ExtractNewRecordState**

| Parameter | Description |
|---|---|
| Delete Handling Mode (delete.handling.mode) | Specify how DELETE events are handled. Valid values: Drop delete events (drop): discards DELETE events. Keep as null record (none): sets the values of DELETE events to null. Rewrite with delete marker (rewrite): extracts the value of the before field and adds the deleted field. __ |
| Drop Tombstones (drop.tombstones) | Specify whether to discard tombstone records. Tombstone records are messages whose values are null. Tombstone records are used to record keys that are deleted during Kafka log compression. Valid values: Drop tombstone messages Keep tombstone messages |
| Metadata Fields to Add to Value (add.fields) | A list of metadata fields separated by commas (,). These fields are added to message values. The following fields are available: op : operation type table : table name db : database name schema : schema name ts ms : event timestamp _ ts us : timestamp in microseconds _ ts ns : timestamp in nanoseconds _ source.ts ms : timestamp of the source _ database lsn : log sequence number name : connector name |

| Value Metadata Field Prefix (add.fields.prefix) | The prefix of the metadata fields added to message values. The default prefix is two underscores ( ). For example, after the default __ prefix is added to the op field, the field changes to op . __ |
|---|---|
| Metadata Fields to Add to Headers (add.headers) | A list of metadata fields separated by commas (,). These fields are added to Kafka message headers. The following fields are available: op : operation type tables : table name db : database name schema : schema name ts ms : event timestamp _ ts us : timestamp in microseconds _ ts ns : timestamp in nanoseconds _ source.ts ms : the timestamp of the _ source database lsn : log sequence number name : connector name |
| Header Metadata Field Prefix (add.headers.prefix) | The prefix of the metadata fields added to message headers. The default prefix is two underscores ( ). For example, after the default __ prefix is added to the op field, the field changes to op . __ |
| Route By Field (route.by.field) | A message field whose value is used as the name of the specified topic. You can specify this parameter to route messages to different topics based on field values. |

#### 2.9.3 Ingest data to data lakes

Ingesting data to data lakes is a process of persisting real-time or offline data from a Kafka message queue to a data lake after data cleansing and conversion.

**Background information**

Ingesting data to data lakes is a process of persisting raw data from different business systems to a data lake after automated collection, cleansing, and conversion. You can persist real-time logs from message queues, transaction records from databases, and sensor data from IoT devices. In Apsara Stack and modern big data architectures, a data lake is usually built on top of object storage, such as Object Storage Service (OSS). It supports a wide array of data formats, such as Parquet, ORC, and JSON, and is compatible with various computing engines, such as MaxCompute, Flink, Spark, and Hive. A connect is created. For more information, see the Create a connect section in the Connect topic. AI Data Lake (ADL) is deployed.

**Create a data ingestion task**

1. Log in to the ApsaraMQ for Kafka console.
2. In the left-side navigation pane, choose **Data Integration > Data Lake Ingestion**.
3. On the **Data Lake Ingest** page, click **Create Ingest Task**.
4. In the **Create Ingest Task** dialog box, perform the following steps and click **OK**.
i. Select a connect. Select a connect from the **Please select a Connect cluster** drop-down list and click
**Next**.
ii. Select a data source. Select a connector from the **Connector** drop-down list, configure the relevant parameters, and click **Next**.

> **Note:** For more information about the supported connector types and the configuration for each connector type, see Connector types.

iii. Specify the destination table. In the **Configure Target Table** step, configure the following parameters, confirm other information, and click **Next**.

| Parameter | Description |
|---|---|
| Task Name | Enter a task name. |
| User AK | Enter the AccessKey ID used to access the data lake. |
| User SK | Enter the AccessKey secret used to access the data lake. |
| Target Catalog | Select the catalog created on the ADL platform. |

iv. Preview the configuration. In the **Configuration Preview** step, confirm **Connect Cluster**, **Data Source**, and
**Target Table** and click **Create**.

**View the details of a data ingestion task**

1. Optional. On the **Data Lake Ingest** page, you can filter tasks by task name, status, and
data format.
2. In the task list, you can view the following information about data ingestion tasks: **Task**
**Name**, **Status**, **Source > Target**, **Data Format**, and **Created At**.
3. Find the desired task and click **Details** in the **Operation** column.
4. In the message that appears, you can view **Basic Information**, **Sync Configuration**,
**Associated Connector**, and **Operation History** of the data ingestion task.
**Basic Information**: displays **Task Name**, **Task ID**, **Status**, **Created At**, **Source Kafka**
**Cluster**, **Source Topic**, **Connect Cluster**, and **Connect Zone**.
**Sync Configuration**: displays **Target Catalog**, **Data Format**, **Warehouse Path**,
**Storage Endpoint**, **Access Key**, and **Secret Key**.
**Associated Connector**: displays the two key components of the task. Both connectors
must be in the RUNNING state before the task can synchronize data as normal.

> **Note:** Click **Pause** to stop pulling data from the database.
> Click **Resume** to resume consumption from the offset.
> Click **Restart** to reinitialize the connection. Perform this operation after the configuration is updated.

**Operation History**: displays the logs of key events in descending chronological order.

**Pause or resume a data ingestion task**

When you pause a data ingestion task, the Kafka connect stops the task thread of the connector. When you resume a data ingestion task, the connector attempts to resume from the previous offset.
1. On the **Data Lake Ingest** page, find the desired data ingestion task and click **Pause** or
**Resume** in the **Operation** column.
2. Click **OK**.

**Delete a data ingestion task**

> **Important:** You cannot restore a data ingestion task after you delete it. Make sure that important configurations are backed up or metadata is exported before you start.

1. On the **Data Lake Ingest** page, find the desired data ingestion task and click **Delete** in
the **Operation** column.
2. Click **OK**.

### 2.10 Zone-disaster recovery

#### 2.10.1 Solution overview

ApsaraMQ for Kafka provides zone-disaster recovery capabilities for financial business that requires high data stability and regulatory compliance. In the zone-disaster recovery solution provided by ApsaraMQ for Kafka, a primary cluster and a secondary cluster are deployed in two data centers that reside in the same zone. The primary cluster provides external services, and the KafkaReplicator component synchronizes data from the primary cluster to the secondary cluster. If both clusters run as expected, all data in the primary cluster, including messages and consumer offsets, is backed up to the secondary cluster. If the primary cluster fails, you can use the ApsaraMQ for Kafka console or the Application Service Registration (ASR) mechanism to switch business from the primary cluster to the secondary cluster. Failure scenarios include a disruption of the hardware or software environment that prevents timely service recovery, or a catastrophic event such as a fire or natural disaster that results in a full data center rebuild. The secondary cluster then handles service requests. Once the primary cluster is restored, you can switch business back to the primary cluster.

**Architecture**

The following figure shows the zone-disaster recovery architecture in which two ApsaraMQ for Kafka clusters are deployed. Architecture description: An ApsaraMQ for Kafka cluster and a KafkaReplicator database cluster are deployed in both Data Center A and Data Center B. The KafkaReplicator component synchronizes data from Data Center A to Data Center B to ensure data consistency. When a fault occurs in Data Center A, the business of Data Center A is switched to Data Center B. In this case, the domain name used to access the business remains unchanged.

**Limits**

After you implement a zone-disaster recovery solution, you must change the connection endpoint of the application client from the virtual IP address (VIP) of the primary ApsaraMQ for Kafka cluster to the domain name of the secondary ApsaraMQ for Kafka cluster. Otherwise, you cannot connect to the secondary ApsaraMQ for Kafka cluster during a disaster recovery switchover.

#### 2.10.2 Create replica clusters

This topic describes how to create a replica cluster and establish a replication relationship to provide disaster recovery capabilities by using ApsaraMQ for Kafka instances. Two ApsaraMQ for Kafka instances are deployed. One of the instances is used in production environments and the other is used in zone-disaster recovery environments. Make sure that KafkaReplicator is deployed in the clusters to which the instances belong. If KafkaReplicator is not deployed, contact ApsaraMQ for Kafka technical support to deploy it.
1. Log on to the ApsaraMQ for Kafka console.
2. In the left-side navigation pane, click **Replica Clusters**.
3. On the **Disaster Recovery** page, click **Create a disaster recovery cluster**.
4. Perform the following operations to complete the wizard.
i. In the **Configure Basic information** step, configure the following parameters and click
**Next**.

| Parameter | Description |
|---|---|
| Disaster recovery cluster name | The name of the replica cluster. Note The name of the replica cluster must meet the following rules: It can only contain letters, digits, and hyphens (-). It must be 3 to 20 characters in length. If the name is longer than 20 characters, it is automatically truncated. You cannot change the name of the replica cluster after the replica cluster is created. |

ii. In the **Configure Source Service** step, specify the following parameters of the source instances and click **Next**.

| Parameter | Description |
|---|---|
| SOURCE Kafka instance | The source Kafka instance. |
| Source KafkaReplicator instance | The source Kafka replicator. |
| Synchronization Start Point | The offset to start the data synchronization. You can select Earliest point, Nearest Point, or Specified time. |
| Time point | The date and time. Note This option is available only when you set Synchronization Start Point to Specified time. |
| Synchronous current limiting | If you do not need to perform current limiting during the data synchronization of disaster recovery instances, enter 0 in the field. Unit: MB/s. |

iii. In the **Configure Target Services** step, specify the information about the target instances and click Next. In the Confirmation step, confirm the information and click
**Create**.
After a replica cluster is created, you can view the replica cluster on the **Disaster**
**Recovery** page.

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
4. In the **Delete a cluster** dialog box, click **OK**.

### 2.11 Data migration

#### 2.11.1 Cloud migration

##### 2.11.1.1 Migrate data of topics and groups to the cloud

**cloud**

This topic describes how to use the data migration tool provided by Apsara Stack to migrate data of topics and groups from a self-managed open source Apache Kafka cluster to an ApsaraMQ for Kafka instance.

**Migrate data to the cloud by using a metadata file**

You can use the `kafka-migration.jar` tool and the metadata file exported from a selfmanaged Apache Kafka cluster to enable ApsaraMQ for Kafka to automatically create topics and groups in an ApsaraMQ for Kafka instance. The following tool is downloaded to the self-managed Apache Kafka cluster from which you want to migrate data: kafka-migration.jar The metadata file of the self-managed Apache Kafka cluster is exported.

**Start the migration**

**Migrate topic data**

1. Run the env |grep kafka command in the kafka console pod of the destination ApsaraMQ
for Kafka instance to obtain the point of presence (POP) domain name of the instance. The `kafka_pop_domain` parameter indicates the POP domain name of the instance.
2. Run the following code in your self-managed Apache Kafka cluster to start the migration.
Before you run the code, modify the relevant parameters described in the following table based on your business requirements.

```
java -jar kafka-migration.jar TopicMigrationFromMetadata \ --fileName metadata.json \ --endpoint ggggg \ --destAk hhhh \ --destSk kkkk \ --destRegionId llll \ --destInstanceId iiii \ --commit
```

| Parameter | Description |   |   | Example |   |   |
|---|---|---|---|---|---|---|
| --fileName | The name of the metadata file. If you do not specify the parameter, the parameter is set to kafka-metadata- export.json by default. |   |   | metadata.json |   |   |
| --endpoint | The POP domain name of the destination ApsaraMQ for Kafka instance. |   |   | api- |   |   |
|   |   |   |   |   | api- |   |
|   |   |   |   | kafka.inter.env1.shuguang. |   |   |
|   |   | ce. |   |   |   |   |
|   |   |   |   | com |   |   |
| --destAk | The AccessKey ID of the Apsara Stack account to which the destination ApsaraMQ for Kafka instance belongs. |   |   | zNYXZmCqIchtIKr |   |   |
| --destSk | The AccessKey secret of the Apsara Stack account to which the destination ApsaraMQ for Kafka instance belongs. |   |   | HwMYEcd1j3EqSiLkSGV6Bu8dM cK |   |   |
| --destRegionId | The ID of the region in which the destination ApsaraMQ for Kafka instance resides. |   |   | cn-hangzhou |   |   |
| --destInstanceId | The ID of the destination ApsaraMQ for Kafka instance. |   |   | cluster-snje0r |   |   |

|   |   | metadata.json |
|---|---|---|
| kafka-metadata- | metadata | metadata |

|   | export.json |
|---|---|

|   |   | HwMYEcd1j3EqSiLkSGV6Bu8dM |   |
|---|---|---|---|
| nt to which the destination or Kafka instance belongs. | cK |   |   |

| --commit | Commits and runs the code. | commit |
|---|---|---|

**Migrate group data**

1. Connect to any server within the cluster of the destination ApsaraMQ for Kafka instance and
run the `hostname -i` command to obtain the endpoint of the topic from which you want to consume data in the destination ApsaraMQ for Kafka instance. The value of the

| bootstrapServers |   |
|---|---|
|   | form |

`bootstrapServers` parameter is in the `IP address obtained from the hostname -i`
2. Run the following code in your self-managed Apache Kafka cluster to start the migration.
Before you run the code, modify the relevant parameters described in the following table based on your business requirements.

```
java -jar kafka-migration.jar ConsumerGroupMigrationFromMetadata \ --fileName metadata.json \ --bootstrapServers ggggg \ --commit
```

|   | Parameter | Description | Example |
|---|---|---|---|
|   | --fileName | The name of the metadata file. If you do not specify the parameter, the parameter is set to kafka- metadata-export.json by default. | metadata.json |
|   | -- bootstrapServers | The endpoint of the topic from which you want to consume data in the destination ApsaraMQ for Kafka instance. | 10.17.150.217:9092 |
|   | bootstrapServers |   |   |
|   | --commit | Commits and runs the code. | commit |

|   |   |   |   | metadata.json |
|---|---|---|---|---|
|   |   | kafka- | metadata. | metadata. |
|   | metadata-export.json |   |   |   |

**View the migration progress**

**View the migration progress of topic data**

After you run the code to start the migration, you can view the migration progress of each topic in the section shown in the following figure.

**View the migration progress of group data**

After you run the code to start the migration, you can view the migration progress of each group in the section shown in the following figure.

**Verify migration results**

1. Log in to the ApsaraMQ for Kafka console.
2. In the left-side navigation pane, click **Instance List**.
3. On the **Instance List** page, find the instance that you want to manage, and click the
instance name, or click **Details** in the **Operation** column.
4. On the details page of the instance, click the **Topic management** or **Group management**
tab. On the **Topic management** or **Group management** tab, view the created topics or groups.

**FAQ**

**Q1: What happens if a topic already exists in the destination**

**ApsaraMQ for Kafka instance when I migrate the topic?**

The topic fails to be migrated, and an error shown in the following figure is reported, which indicates that the topic already exists in the destination ApsaraMQ for Kafka instance.

**Q2: What happens if the value of the endpoint parameter is**

**invalid when I migrate a topic?**

The topic fails to be migrated, and an error shown in the following figure is reported.

**Q3: What happens if the values of the destAk and DestSk**

**parameters are invalid when I migrate a topic?**

The topic fails to be migrated, and an error shown in the following figure is reported.

**Q4: What happens if the value of the destRegionId or**

**destInstanceId parameter is invalid when I migrate a topic?**

The topic fails to be migrated, and an error shown in the following figure is reported, which indicates that the destination ApsaraMQ for Kafka instance is not found or not running.

**Q5: What happens if the metadata.json file does not exist**

**when I migrate a topic?**

The topic fails to be migrated, and an error shown in the following figure is reported, which indicates that the file fails to be read.

**Q6: What happens if the value of the bootstrapServers**

**parameter is invalid when I migrate a group?**

The group fails to be migrated, and an error shown in the following figure is reported, which indicates that the value of the bootstrapServers parameter is invalid.

#### 2.11.2 Cloud‑to‑Cloud Migration

##### 2.11.2.1 Use the ApsaraMQ for Kafka console to migrate services from one ApsaraMQ for Kafka instance to another

**migrate services from one ApsaraMQ for Kafka**

**instance to another**

This topic describes how to use the ApsaraMQ for Kafka console to migrate services from one ApsaraMQ for Kafka instance to another ApsaraMQ for Kafka instance.

**Procedure**

1. Log on to the ApsaraMQ for Kafka console.
2. In the left-side navigation pane, choose **Data Integration > Message Routing**.
3. On the **Message Routing** page, click the **Tasks** tab.
4. Click **Create a local task**, configure the following parameters, and then click **OK**.

| Parameter |   | Description |
|---|---|---|
| Message Source | SOURCE instance | Select the source ApsaraMQ for Kafka instance. |
|   | Type | Select the type of the migration task. Valid values: Instance Migration topic migration |
|   | Synchronous Topic | Select the topic to be synchronized. You can select multiple topics. If you do not specify this parameter, all topics in the instance are synchronized. Regular expressions are supported. For example, hello.* indicates that all topics that start with hello are synchronized. Note This parameter is displayed only if you set Type to topic migration. |
| Message Destination | Target Instance | Select the destination ApsaraMQ for Kafka instance. |
|   | Target Replicator | Select the destination replicator. |
| Synchronization Start Point |   | Select an offset to start the data synchronization. Valid values: Earliest point Nearest Point Specified time |

| Time point | Select a date. If the offset cannot be found in the specified partition of the specified topic after you select the time, data synchronization starts from the earliest offset. An offset cannot be found if the specified time is earlier than the earliest offset or later than the latest offset. Note This parameter is displayed only if you set Synchronization Start Point to Specified time. |
|---|---|
| Current limiting | Configure the throttling rule for the data synchronization process of the disaster recovery instances. Unit: MB/s. Note If throttling is not required during the data synchronization of disaster recovery instances, set this parameter to 0. |
| Description | Enter a description. |

5. After the local task is created, you can view its basic information and status in the task list
on the **Tasks** tab.

##### 2.11.2.2 Cloud‑to‑Cloud Migration using the Kafka data migration tool

**data migration tool**

This topic describes how to use the Kafka data migration tool from Alibaba Cloud to migrate your services from one ApsaraMQ for Kafka instance to another.

**Migrate Kafka metadata and data in the cloud**

You can use the provided `kafka-migration-assessment.jar` tool and the `kafka-mirror-` `maker.sh` tool, which is included with the ApsaraMQ for Kafka instance, to migrate metadata and data. Download the `kafka-migration-assessment.jar` tool to the target ApsaraMQ for Kafka cluster. kafka-migration-assessment.jar

**Start the migration**

**Metadata migration (topics and groups)**

1. Upload the downloaded migration tool to the **target** ApsaraMQ for Kafka **cluster**.

```bash
# Upload the migration tool to the main container of the ApsaraMQ for Kafka instance.
kubectl cp /apsarapangu/disk4/tmp/xtermupload/kafka-migration-assessment.jar alibaba-ka fka-cluster-s****-0:/home/admin -c main
# Access the main container of the target ApsaraMQ for Kafka instance.
kubectl exec -it alibaba-kafka-cluster-s****-0 -c main -- bash
```

2. In the directory that contains the migration tool, run the following command to grant
executable permissions to the JAR file.

```
chmod 777 kafka-migration-assessment.jar
```

3. Parameter descriptions:

|   |   | Parameter |   | Description |   |   | Example |
|---|---|---|---|---|---|---|---|
|   |   | -- sourceAk |   | The AccessKey ID of the Alibaba Cloud account that owns the source ApsaraMQ for Kafka instance. |   |   | 0J********* |
|   |   | -- sourceSk |   | The AccessKey secret of the Alibaba Cloud account that owns the source ApsaraMQ for Kafka instance. |   |   | h7***************** |
|   |   | -- |   | The region ID of the source ApsaraMQ for Kafka instance. |   |   | cn-hangzhou |
|   |   |   | -- | The re |   |   |   |
|   |   | sourceRegio |   |   |   |   |   |
|   |   |   |   | K |   |   |   |
|   |   | nId |   |   |   |   |   |
|   |   | -- |   | The ID of the source ApsaraMQ for Kafka instance. |   |   | cluster-s***qu |
|   |   |   | -- | The ID o |   |   |   |
|   |   | sourceInsta |   |   |   |   |   |
|   |   |   |   | insta |   |   |   |
|   |   | nceId |   |   |   |   |   |
|   |   | -- |   | The kafka pop domain environment _ _ variable of the `kafka-console` container. |   |   | api- kafka.inter.env**.sh****.com |
|   |   |   | -- | The |   | kafka pop domain _ _ |   |
|   |   | sourceEndpo |   |   |   |   |   |
|   |   |   |   | va |   |   |   |
|   |   | int |   |   |   |   |   |
|   |   | -- destAk |   | The AccessKey ID of the Alibaba Cloud account that owns the target ApsaraMQ for Kafka instance. |   |   | ER********* |
|   |   | -- destSk |   | The AccessKey secret of the Alibaba Cloud account that owns the target ApsaraMQ for Kafka instance. |   |   | Ut***************** |

|   |   | -- |   |
|---|---|---|---|
|   | sourceAk |   |   |

|   |   | -- |   |
|---|---|---|---|
|   | sourceSk |   |   |

|   |   | api- |
|---|---|---|
| r. | kafka.inter.env**.sh****.com |   |

|   |   | -- |
|---|---|---|
|   | destAk |   |

|   |   | -- |
|---|---|---|
|   | destSk |   |

|   |   | -- |   | The region ID of the target ApsaraMQ for Kafka instance. | cn-hangzhou |
|---|---|---|---|---|---|
|   |   |   | -- | The |   |
|   |   | destRegionI |   |   |   |
|   |   | d |   |   |   |
|   |   | -- |   | The ID of the target ApsaraMQ for Kafka instance. | cluster-s***ty |
|   |   |   | -- | The ID |   |
|   |   | destInstanc |   |   |   |
|   |   |   |   | in |   |
|   |   | eId |   |   |   |
|   |   | -- |   | The kafka pop domain environment _ _ variable of the `kafka-console` container. | api- kafka.inter.env**.sh****.com |
|   |   |   | -- | The |   |
|   |   | destEndpoin |   |   |   |
|   |   | t |   |   |   |
|   |   | -- search |   | Specifies the topics or groups to migrate. | topic1,topic2,topic3 |
|   |   | -- commit |   | Commits the execution. | commit |
|   |   | -- |   | The endpoint of the corresponding topic in the target ApsaraMQ for Kafka instance. | localhost:9092 |
|   |   |   | -- | The endpoint |   |
|   |   | destBootstr |   |   |   |
|   |   |   |   | the targe |   |
|   |   | apServers |   |   |   |

|   |   | api- |
|---|---|---|
| r. | kafka.inter.env**.sh****.com |   |

|   |   | -- |
|---|---|---|
|   | search |   |

|   |   | -- |
|---|---|---|
|   | commit |   |

**Migrate topics in the cloud**

**Step 1: Run a topic migration evaluation**

```
java -jar kafka-migration-assessment.jar TopicMigrationFromAliyun \ --sourceAk 0J********* \ --sourceSk h7***************** \ --sourceRegionId cn-w****-env**-d01 \ --sourceInstanceId cluster-s**** \ --sourceEndpoint api-kafka.inter.env**.sh****.com \ --destAk ER********* \ --destSk Ut***************** \ --destRegionId cn-w****-env**-d01 \ --destInstanceId cluster-s**** \ --destEndpoint api-kafka.inter.env**.sh****.com
```

You can use the `--search` parameter to specify the topics for the migration evaluation. If you do not include this parameter, the tool evaluates all topics by default.

```
java -jar kafka-migration-assessment.jar TopicMigrationFromAliyun \ --sourceAk 0J********* \ --sourceSk h7***************** \ --sourceRegionId cn-w****-env**-d01 \ --sourceInstanceId cluster-s**** \ --sourceEndpoint api-kafka.inter.env**.sh****.com \ --destAk ER********* \ --destSk Ut***************** \ --destRegionId cn-w****-env**-d01 \ --destInstanceId cluster-s**** \ --destEndpoint api-kafka.inter.env**.sh****.com \ --search topic1,topic2,topic3,topic4
```

The following output shows the evaluation result: After you confirm the evaluation results, run the topic migration command.

**Step 2: Run the topic migration**

You can use the `--search` parameter to specify the topics to migrate.

```
java -jar kafka-migration-assessment.jar TopicMigrationFromAliyun \ --sourceAk 0J********* \ --sourceSk h7***************** \ --sourceRegionId cn-w****-env**-d01 \ --sourceInstanceId cluster-s**** \ --sourceEndpoint api-kafka.inter.env**.sh****.com \ --destAk ER********* \ --destSk Ut***************** \ --destRegionId cn-w****-env**-d01 \ --destInstanceId cluster-s**** \ --destEndpoint api-kafka.inter.env**.sh****.com \ --search topic1,topic2,topic3,topic4 \ --commit
```

The following output shows the migration result:

**Step 3: Verify the migration result**

After the migration is complete, go to the Topic Management tab of the target instance to view the created topics in the topic list.
1. Log in to the ApsaraMQ for Kafka console.
2. In the left-side navigation pane, click **Instance List**.
3. On the **Instance List** page, find the instance that you want to manage, and click the
instance name, or click **Details** in the **Operation** column.
4. Click the **Topic management** tab.
5. On the **Topic management** tab, view the list of topics.

**FAQ**

**Q1: If a topic from the source instance already exists in the target instance, is it**

**skipped during migration?**

Yes, it is.

**Migrate consumer groups in the cloud**

**Step 1: Run a group migration evaluation**

```
java -jar kafka-migration-assessment.jar ConsumerGroupMigrationFromAliyun \ --sourceAk 0J********* \ --sourceSk h7***************** \ --sourceRegionId cn-w****-env**-d01 \ --sourceInstanceId cluster-s**** \ --sourceEndpoint api-kafka.inter.env**.sh****.com \ --destAk ER********* \ --destSk Ut***************** \ --destRegionId cn-w****-env**-d01 \ --destInstanceId cluster-s**** \ --destEndpoint api-kafka.inter.env**.sh****.com \ --destBootstrapServers localhost:9092 \ --search group1,group2,group3
```

The following output shows the evaluation result: After you confirm the evaluation results, run the group migration command.

**Step 2: Run the group migration**

```
java -jar kafka-migration-assessment.jar ConsumerGroupMigrationFromAliyun \ --sourceAk 0J********* \ --sourceSk h7***************** \ --sourceRegionId cn-w****-env**-d01 \ --sourceInstanceId cluster-s**** \ --sourceEndpoint api-kafka.inter.env**.sh****.com \ --destAk ER********* \ --destSk Ut***************** \ --destRegionId cn-wulan-env82-d01 \ --destInstanceId cluster-s**** \ --destEndpoint api-kafka.inter.env**.sh****.com \ --destBootstrapServers localhost:9092 \ --search group1,group2,group3 \ --commit
```

The following output shows the migration result:

**Step 3: Verify the migration result**

After the migration is complete, go to the Group Management tab of the target instance to view the created groups in the group list.
1. Log on to the ApsaraMQ for Kafka console.
2. In the left-side navigation pane, click **Instance List**.
3. On the **Instance List** page, find the instance that you want to manage, and click the
instance name, or click **Details** in the **Operation** column.
4. On the **Instance details** page, click the **Group management** tab.
5. On the **Group management** tab, view the list of consumer groups.

**Migrate data in the cloud**

The `kafka-mirror-maker` tool uses a consumer to pull data from the source ApsaraMQ for Kafka instance and a producer to efficiently and reliably transfer the data to the target ApsaraMQ for Kafka instance.

**Prepare the data migration configuration files**

On the target ApsaraMQ for Kafka cluster, prepare the `migrationProducer.properties` and `migrationConsumer.properties` configuration files. Contents of the `migrationProducer.properties` file:

```
## The PLAINTEXT endpoint of the target Kafka cluster.
bootstrap.servers=ip:port
## Data compression type.
compression.type=none
```

Contents of the `migrationConsumer.properties` file:

```bash
## The PLAINTEXT endpoint of the source Kafka cluster.
bootstrap.servers=ip:port
## The partition assignment strategy for the consumer.
partition.assignment.strategy=org.apache.kafka.clients.consumer.RoundRobinAssignor
## The name of the group. Use a new group for the data migration.
group.id=test-consumer-group
# If no offset is committed, synchronization starts from the earliest data.
auto.offset.reset=earliest
```

**Use the data migration tool**

The tool is located in the `/home/admin/KafkaProxy/bin` directory inside the ApsaraMQ for Kafka container.
**After you migrate the topics** , run the following command to start the data migration.

```
./kafka-mirror-maker.sh --consumer.config ../config/migrationConsumer.properties --prod ucer.config ../config/migrationProducer.properties --whitelist 'topic1|topic2|topic3'
```

| Parameter | Description | Example |
|---|---|---|
| -- consumer.config | Specifies the consumer configuration file, which contains the connection information for the source cluster. | ../config/migrationConsumer.properties |
| -- producer.config | Specifies the producer configuration file, which contains the connection information for the target cluster. | ../config/migrationProducer.properties |
| --whitelist | A whitelist. Use a regular expression to specify the topics to replicate. | "topic1\|topic2\|topic3" |

|   |   | -- | S |
|---|---|---|---|
|   | consumer.config |   |   |

|   |   | -- | S |
|---|---|---|---|
|   | producer.config |   |   |

**Verify the data migration result**

1. On the Group Management tab of the target ApsaraMQ for Kafka instance, check if the
configured `group.id` exists.
2. Check the consumption status of the group and the consumption details of the topic. For
more information, see View the consumption status of a consumer group.
3. In the ApsaraMQ for Kafka console, check the partition status of the topic and confirm that
the number of messages is correct. For more information, see View the partition status of a topic.

**FAQ**

**Q1: How do I stop a running migration script?**

If you are in the command-line interface where the script is running, press Ctrl+C to stop the script. If you are not in the command-line interface where the script is running, find and kill the process as follows:

```
ps -ef | grep "kafka.tools.MirrorMaker"
```

Kill the process:

```
kill -9 xxx
```

ions

## 3 Pod command operations

### 3.1 Command verification

#### 3.1.1 Create topics

This topic describes how to create a topic. The information about the master node in ApsaraMQ for Kafka is obtained.

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

This topic describes how to send messages to a topic. The information about the master node in ApsaraMQ for Kafka is obtained.

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

This topic describes how to consume messages from a topic. The information about the master node in ApsaraMQ for Kafka is obtained.

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

#### 3.2.2 View the status of a topic

This topic describes how to view the status of a topic. The information about the master node in ApsaraMQ for Kafka is obtained.

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

The current offset of a partition is the latest message that is sent to the consumer by the ApsaraMQ for Kafka broker. This topic describes how to view the current offset of a partition. The information about the master node in ApsaraMQ for Kafka is obtained.

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

This topic describes how to view the list of topics. The information about the master node in ApsaraMQ for Kafka is obtained.

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

After you create a topic, you can increase the number of partitions in the topic. ApsaraMQ for Kafka does not allow you to decrease the number of partitions in a topic. If you want to decrease the number of partitions in a topic, you can delete the topic and create another topic that has the required number of partitions. The information about the master node in ApsaraMQ for Kafka is obtained.

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

This topic describes how to view the consumer status of a consumer group. The information about the master node in ApsaraMQ for Kafka is obtained.

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

This topic describes how to view the list of consumer groups. The information about the master node in ApsaraMQ for Kafka is obtained.

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

This topic describes how to send messages to a topic. The information about the master node in ApsaraMQ for Kafka is obtained.

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

This topic describes how to consume messages from a topic. The information about the master node in ApsaraMQ for Kafka is obtained.

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
