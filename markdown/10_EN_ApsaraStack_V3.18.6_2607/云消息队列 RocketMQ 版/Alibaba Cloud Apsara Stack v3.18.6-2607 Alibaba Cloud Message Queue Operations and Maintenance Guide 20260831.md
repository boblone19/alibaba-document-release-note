---
title: "Alibaba Cloud Apsara Stack v3.18.6-2607 Alibaba Cloud Message Queue Operations and Maintenance Guide 20260831"
product_version: "V3.18.6_2607"
doc_version: "20260831"
pdf_pages: 63
source_pdf: "Alibaba Cloud Apsara Stack v3.18.6-2607 Alibaba Cloud Message Queue Operations and Maintenance Guide 20260831.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/3816%202607/pdf%203/%E4%BA%91%E6%B6%88%E6%81%AF%E9%98%9F%E5%88%97%20RocketMQ%20%E7%89%88/Alibaba%20Cloud%20Apsara%20Stack%20v3.18.6-2607%20Alibaba%20Cloud%20Message%20Queue%20Operations%20and%20Maintenance%20Guide%2020260831.pdf"
converter: pdf2md (PyMuPDF line classifier)
---

# Alibaba Cloud Apsara Stack v3.18.6-2607 Alibaba Cloud Message Queue Operations and Maintenance Guide 20260831

## O&M overview

This topic describes the product architecture and O&M architecture of ApsaraMQ for RocketMQ.

### System architecture

This topic is intended to help you understand the system architecture and components of ApsaraMQ for RocketMQ during O&M. ApsaraMQ for RocketMQ provides components that are responsible for service discovery, data storage, authentication, configuration, log collection, and high availability. Figure 1. System architecture ApsaraMQ for RocketMQ consists of the following components:

**Service discovery components**

ApsaraMQ for RocketMQ provides Name Servers and Address Servers for service discovery. An Address Server, also called Cai, is used to register and discover domain names for Name Servers and Diamond. A caller obtains domain names from the Address Server and locally caches the domains names. A Name Server is a core component for flexible deployment and linear scaling of ApsaraMQ for RocketMQ. This component is used to register and search for message queues. A broker registers message queues with a Name Server and synchronizes the status of the broker to the Name Server. Producers and consumers can find specific brokers through Name Servers. After producers and consumers are connected to Name Servers, the producers and consumers can cache the information about the required brokers and message queues, and periodically update the cached information from the Name Servers.

**Broker**

A broker is a core component that is used to process message queues. Multiple brokers can be deployed in cluster, multi-replica, or primary/secondary mode to achieve high availability. Brokers provide message service capabilities that feature high availability, high stability, high efficiency, and linear scaling. A broker registers topic and subscription information to Name Servers to provide services. Brokers are responsible for sending, receiving, and storing messages.

**Console**

The ApsaraMQ for RocketMQ console is a user interface (UI) that allows user access. All operations on message queues can be performed in the console. We recommend that you preferentially perform these operations in the console.

**API**

The ApsaraMQ for RocketMQ API provides a set of API operations that you can call over HTTP and HTTPS. This helps you use ApsaraMQ for RocketMQ and manage resources with ease. For example, you can call API operations to create topics, query group IDs, query messages, and query the status of consumers.

**DAuth**

DAuth provides unified logon services and access control for message queues. For example, it provides resource permission control, cross-account and RAM user access control, and resource authorization.

**Diamond**

Diamond is a configuration center that stores the configuration information of message queues, including VIP conversion rules and resource permission information.

**Tlog**

Tlog collects resource statistics and other key logs of ApsaraMQ for RocketMQ.

**Controller**

Controller is used to perform primary/secondary switchover for brokers to achieve high availability. It interacts with ZooKeeper to check the status of the brokers in a cluster. This way, it can ensure the consistency between the primary and secondary brokers.

**Housekeeping**

Housekeeping regularly checks the health status of the core link of ApsaraMQ for RocketMQ, covering core business, kernel parameters, application configurations, application metrics, and the console. If exceptions are detected, an alert is triggered at the earliest opportunity to ensure the high availability of the ApsaraMQ for RocketMQ cluster.

### O&M architecture

This topic is intended to help you understand the O&M architecture of Message Queue for Apache RocketMQ. The O&M operations of Message Queue for Apache RocketMQ rely on command lines.

| O&M category | Description | O&M tool |
|---|---|---|

| Routine maintenance | Perform inspection and monitoring. | Command line: You can run commands to manually inspect the containers and components of Message Queue for Apache RocketMQ. |
|---|---|---|
| Shutdown maintenance | Check and verify the statuses of containers and components. Stop and start containers and components. | Command line,Apsara Uni- manager Operations Console. |

### Updates

This topic describes the updates of ApsaraMQ for RocketMQ from V3.8.0 to V3.18.3 to help you get started with the updated version.

**Optimization of resource isolation by instance**

ApsaraMQ for RocketMQ provides instances for multi-tenancy isolation. Each user can purchase multiple instances and logically isolate them from each other. To ensure the compatibility with the existing resources of existing users, ApsaraMQ for RocketMQ provides the following types of instances and namespaces: Default instances, which are compatible with the existing resources of existing users This type of instance has no separate namespace. Resource names must be globally unique within and across all instances. By default, an instance without a namespace is automatically generated for the existing resources of each existing user. If no existing resources are available, you can create at most one instance without a namespace. You can configure the endpoint, which can be obtained from the **Instances** page in the ApsaraMQ for RocketMQ console.

```
// Recommended configuration: properties.put(PropertyKeyConst.NAMESRV_ADDR, "xxxx"); // Compatible configuration, which is not recommended. We recommend that you update this configuration to the recommended configuration: properties.put(PropertyKeyConst.ONSAddr, "xxxx");
```

New instances A new instance has a separate namespace. Resource names must be unique within an instance but can be the same across different instances. You can configure the endpoint, which can be obtained from the **Instances** page in the ApsaraMQ for RocketMQ console.

```
// Recommended configuration: properties.put(PropertyKeyConst.NAMESRV_ADDR, "xxx");
```

A RocketMQ client must be updated to the following latest versions for different programming languages: Java: V1.8.7.1.Final C and C++: V2.0.0 .NET: V1.1.3

**Optimization of resource application**

Previously, ApsaraMQ for RocketMQ resources consisted of topics, producer IDs, and consumer IDs. Each two of the resources have a many-to-many relationship, which was difficult to comprehend. Each time you created a topic, you must associate the topic with a producer ID and a consumer ID. This process was too complex for medium- and large-sized enterprise customers. To optimize user experience and help new users get started, the resource application process has been simplified. The resource application process has been optimized in the following aspects: Topic management, which is unchanged You need to apply for a topic. A topic is used to classify messages. It is the primary classifier. Group management You do not need to apply for a producer ID. Producer IDs and consumer IDs are integrated into group IDs. In the ApsaraMQ for RocketMQ console, the Producers module has been removed. The Producers and Consumers modules have been integrated into the Groups module. You do not need to associate a producer ID or consumer ID with a topic. Instead, you need only to apply for a group ID and associate it with a topic in the code. Compatibility: The list of producer IDs is no longer displayed. This does not affect the current services. The consumer IDs that start with CID- or CID_ and that you have applied for can still be used and can be set in the **PropertyKeyConst.ConsumerId** or
**PropertyKeyConst.GROUP_ID** parameter of the code.
Sample code We recommend that you update a RocketMQ client to the following latest versions for different programming languages: Java: V1.8.7.1.Final C and C++: V2.0.0 .NET: V1.1.3 Existing producer IDs or consumer IDs can still be used and do not affect the current services. However, we recommend that you update your instance configuration to the recommended configuration. Recommended configuration: Integrate producer IDs and consumer IDs into group IDs.

```
// Set the PropertyKeyConst.GROUP_ID parameter. The original PropertyKeyConst.ProducerId and PropertyKeyConst.ConsumerId parameters are deprecat ed. properties.put(PropertyKeyConst.GROUP_ID, "The original CID-XXX or the GID-XXX");
```

Compatible configuration: Use a producer ID to identify a producer and a consumer ID to identify a consumer.

```
// When you create a producer, you must set the PropertyKeyConst.ProducerId paramet er. properties.put(PropertyKeyConst.ProducerId, "The original PID-XXX or the GID-XXX"); // When you create a consumer, you must set the PropertyKeyConst.ConsumerId paramet er. properties.put(PropertyKeyConst.ConsumerId, "The original CID-XXX or the GID-XXX");
```

## Operations console guide

**for ApsaraMQ for RocketMQ**

### Log in to the RocketMQ

**Operations Console**

This topic describes how to log in to the RocketMQ Operations Console.

**Prerequisites**

The endpoint of the Apsara Uni-manager Operations Console and the username and password that are used to log on to the console are obtained from a deployment engineer or an administrator. The endpoint of the Apsara Uni-manager Operations Console is in the following format: regi on-id.ops.console.intranet-domain-id. A web browser is available. We recommend that you use Google Chrome.

**Procedure**

1. Open your browser.
2. In the address bar, enter the endpoint of the Apsara Uni-manager Operations Console.
Press the ENTER key. You can click the current language in the upper-right corner to switch to another language. Simplified Chinese, English, and traditional Chinese are supported.
3. Enter the username and password.
Obtain the username and password that are used to log on to the Apsara Unimanager Operations Console from a deployment engineer or an administrator. If you enter an invalid password for three consecutive times, the system enables the image verification logon feature. If you enter an invalid password for five consecutive times, the account is locked. Contact the administrator to activate the account. If this is the first time you log on to the Apsara Uni-manager Operations Console, you must change the password as prompted. To enhance security, your password must meet the following requirements: The password contains uppercase and lowercase letters. The password contains digits. The password contains at least one of the following special characters: ! @ # $ % The password is 10 to 20 characters in length.
4. Click **Log In**.
5. In the top navigation bar, choose **Product Operation > Middleware > RocketMQ**
**Operations Console**.

### Overview

This topic describes the core features and key metrics of ApsaraMQ for RocketMQ so that you can better understand the running status and health status of ApsaraMQ for RocketMQ instances.

**Procedure**

1. Log in to the RocketMQ 4.x Operations Console.
2. By default, the **Overview** page is displayed. This page displays Metrics overview, Disk
usage TOP Broker, Inflow TPS TOP Broker, Outflow TPS TOP Broker, Alarm Statistics, and Last 5 alarm records.

| Section | Description |
|---|---|

| Metrics overview | Total number of clusters: the number of ApsaraMQ for RocketMQ clusters in the current environment. Total number of brokers: the total number of online brokers in all clusters. You can click Total number of brokers or the number below Total number of brokers to go to the Broker Management page and view the details of brokers. Total topics: the number of topics that are created in the system. Total Group: the number of consumer groups. Total number of instances: the number of deployed ApsaraMQ for RocketMQ instances. |
|---|---|
| Disk usage TOP Broker | This section displays the brokers with the highest disk usage, including the name of each broker, the corresponding IP address and port number, and the specific disk usage in percentage. |
| Inflow TPS TOP Broker | This section displays the top four brokers with the highest inbound message rate. Unit: messages per second. |
| Outflow TPS TOP Broker | This section displays the top four brokers with the highest outbound message rate. Unit: messages per second. |
| Alarm Statistics | This section displays the total number of alerts with different severity levels, such as P1 Critical, P2 Major, P3 Minor, and P4 Warning. |
| Last 5 alarm records | This section displays the most recent five alert records, including the alert item, severity, and alert time. Click View more to go to the Alert List page. On this page, you can view the alert information, including real-time alerts that are not handled and historical alerts that are handled. |

### Manage brokers

This topic describes how to view and manage brokers.

**Background information**

In RocketMQ, broker management is a key part of ensuring the efficient and stable operation of the messaging system. As a core component of RocketMQ, a broker is responsible for operations such as message storage, forwarding, and queries.

**View broker information**

1. Log in to the RocketMQ 4.x Operations Console.
2. In the navigation pane on the left, click **Broker Management**.
3. On the **Broker Management** page, select a **Cluster Name**.
4. (Optional) Search for a broker by its name.
5. In the broker list, view the basic information about each broker.

| Parameter | Description |
|---|---|
| Broker Name | The unique name that identifies the broker group. |
| Primary/Secondary | Indicates the role of the broker instance in its cluster, either primary or secondary. |
| Host IP | The network address of a single broker, which consists of an IP address and a port number. |
| Status | The current status of the broker. readonly: The broker is in read-only mode. online: The broker is online and working properly. offline: The broker is offline and cannot provide services, possibly due to a failure or other reasons. |
| HA Status | The working state of the current broker instance. SYNC STATE: The broker is in a synchronous _ state. ONLY MASTER: The broker is the only _ primary node and has no corresponding secondary node. ASYNC STATE: The broker is in an _ asynchronous state, which means data is being synchronized from the primary node to the secondary node. HAIF STATE: The broker is in a semi- _ synchronous state. |

| Inbound Transactions Per Second (TPS) | The number of messages received per second. Click the traffic value to open the Top 10 Business Production Traffic Analysis dialog box. This dialog box shows the top 10 topics with the most messages sent by producers, including their Topic, TPS, and Timestamp information. |
|---|---|
| Outbound TPS | The number of messages sent per second. Click the traffic value to open the Top 10 Business Consumption Traffic Analysis dialog box. This dialog box shows the top 10 topics with the highest consumption and their corresponding consumer groups, including their Topic, Group, TPS, and Timestamp information. |

6. On the **Broker Management** page, click a broker name or click **View** in the **Actions**
column to view detailed information about the broker. On the **Basic Information** tab, view the **Basic Information** and **Key Metrics** for the broker.
**Basic Information**: View information about the primary and secondary nodes of the
broker.
**Key Metrics**: View metrics such as the broker's **send TPS**, **pull TPS**, **disk usage**,
**disk space**, and **retention period**. You can also analyze trend graphs of **in/out TPS**,
**PageCache**, **CPU**, **memory**, **disk I/O**, and **network I/O** over a specified period. You
can switch the time range to **15 minutes**, **1 hour**, **6 hours**, or a custom time range. On the **Configuration Information** tab, view the **Key**, **Value**, and **Description** for each configuration item. Click **Modify** in the **Actions** column to change the **Configuration**
**Value**.
On the **VPC Management** tab, view the VPC network information for the broker cluster, including **VPC ID/Name**, **vSwitch ID**, **Region**, **Cluster**, **broker VIP**, and **nameserver**
**VIP**.
On the **Status Repair** tab, you can repair brokers that have an abnormal status. For more information, see Repair a broker.

**Disable writes to a broker**

In RocketMQ, you can disable writes to a broker to prevent new messages from being written during maintenance, troubleshooting, or emergencies. This helps prevent data inconsistency and other potential issues. You can disable writes only for broker nodes that have a **Status** of **online**.
1. Log in to the RocketMQ 4.x Operations Console.
2. In the navigation pane on the left, click **Broker Management**.
3. On the **Broker Management** page, click **Disable Write** in the **Actions** column.
4. In the dialog box that appears, click **OK**.

**Recover a broker**

You can resume writes to a broker to allow new messages to be written to it. Write protection is available only for Broker nodes in the **readonly** state.
1. Log in to the RocketMQ 4.x Operations Console.
2. In the navigation pane on the left, click **Broker Management**.
3. On the **Broker Management** page, click **Remove Write Protection** in the **Actions**
column.
4. In the dialog box that appears, click **OK**.

**Take a broker offline or bring it online**

1. Log in to the RocketMQ 4.x Operations Console.
2. In the navigation pane on the left, click **Broker Management**.
3. On the **Broker Management** page, click **Take Offline** or **Bring Online** in the **Actions**
column.
4. In the dialog box that appears, click **OK**.

**Restart a broker**

1. Log in to the RocketMQ 4.x Operations Console.
2. In the navigation pane on the left, click **Broker Management**.
3. On the **Broker Management** page, click **Restart** in the **Actions** column.
4. In the dialog box that appears, click **OK**.

**Repair a broker**

If a broker's state machine becomes abnormal, you can use the status repair feature to repair the broker. The following are types of abnormal states: Split-brain between primary and secondary nodes Primary and secondary nodes remain in the async_state state for a long time Primary and secondary nodes remain in the half_sync state for a long time
1. In the **Current Repair Status** section, you can view the current state of the broker's state
machine and the repair process.
2. In the **Broker List** section, click an available operation in the **Actions** column or above the
list, and then complete the operation as prompted.
3. Repeat step 2 until the repair process is complete.
In the **Status Repair Topology** section, you can view the broker's lifecycle state machine in real time.

### NameServer management

This topic describes how to view the information about a NameServer node.

**Background information**

The NameServer management module in the RocketMQ Operations Console is used to manage and monitor NameServer nodes in an ApsaraMQ for RocketMQ cluster. NameServer plays an important role in ApsaraMQ for RocketMQ. It is mainly responsible for service discovery and routing information management, and is the hub for communication among message producers, consumers, and brokers.

**Procedure**

1. Log in to the RocketMQ 4.x Operations Console.
2. In the left-side navigation pane, click **NameServer Management**.
3. On the **NameServer management** page, view **IP address**, **Port**, **Status**, and **Number**
**of connections** of NameServer nodes.

| Parameter | Description |
|---|---|

| IP address | The identifier of a NameServer node in the network, which is used by clients (producers and consumers) to communicate with the NameServer node. Each NameServer node has a unique IP address. |
|---|---|
| Port | The port number used by a client to communicate with the NameServer node. |
| Status | The running condition of the NameServer node. |
| Number of connections | The number of clients that are connected to the NameServer node, including producers, consumers, and brokers. |

4. Click **Details** in the **Operation** column of the NameServer node. In the **Details** dialog box,
view the keys and values of the NameServer node.

### Metadata management

On the Metadata Management page, you can view and manage the virtual private cloud (VPC) configurations associated with an ApsaraMQ for RocketMQ cluster, view and modify ApsaraMQ for RocketMQ metadata, configure IP address whitelists, and manage instances and cloud product accounts.

**Procedure**

1. Log in to the RocketMQ 4.x Operations Console.
2. In the left-side navigation pane, click **Metadata management**.
3. On the **Metadata Management** page, you can perform the following operations:
On the **VPC management** tab, you can view the information about the VPC bound to the ApsaraMQ for RocketMQ instance, including **VPC ID** and **VPC name**. Click **View broker** in the Operation column to view information about the brokers in the VPC, including
**Broker address**, **Broker VIP**, **Nameserver VIP**, **Instance ID**, **Cluster**, and **Switch ID**.
Click the **Configuration Management** tab. You can view the configuration items and their descriptions and modify the configuration items. To modify a configuration value, click **Modify** in the **Operation** column, specify **Cluster** and **Configuration value**, and then click **OK**.

| Parameter | Description |
|---|---|
| Cluster | Select the cluster that you want to modify from the drop-down list. |
| Configuration value | true: enables write authentication. false: disables write authentication. |

**Important**

The modification will update the configuration values of the relevant configuration items of all brokers in the cluster. Exercise caution when you perform this operation. Click the **TaoKeeper node management** tab. In the left-side navigation pane, click a node. The detailed data of the node is displayed in the right-side pane. During a switchover of the primary/secondary brokers, you can click **Delete a node** to remove metadata.

**Important**

If you delete a node, the normal operation of ApsaraMQ for RocketMQ is affected. Proceed with caution. On the **IP whitelist** tab, you can configure an IP address whitelist for the ApsaraMQ for RocketMQ instance. Only clients in the whitelist are allowed to update and obtain broker configurations, and update name server configurations. You cannot modify or delete the IP address whitelist that is generated by the system by default. If no whitelist is manually configured, the system disables access control by default. Search for an IP address in the IP address whitelist: On the **IP whitelist** tab, enter an IP address and click **Confirm**. The system displays a list of search results. Add an IP address to the IP address whitelist: On the **IP whitelist** tab, click **Add**. In the dialog box that appears, enter an IP address or CIDR block, and then click **OK**. Modify an IP address in the IP address whitelist: In the IP address whitelist, find the IP address that you want to modify and click **Edit** in the Operation column. In the dialog box that appears, modify the IP address and click **OK**. Delete an IP address from the IP address whitelist: Find the IP address that you want to delete and click **Delete** in the Operation column. In the message that appears, click
**OK**.
On the **Instance Management** tab, you can view the information about the instances that are created by calling the SDK based on the AccessKey ID and AccessKey secret that you applied for from the baseline. The information includes **Instance ID/Name**, **Cluster**
**ID**, **Product Name**, and **Status**.
a. Optional. Select a cluster name from the **Cluster name** drop-down list and enter a product name to filter instances. b. Click **View** in the **Operation** column to go to the **Instance Management Details** page. The instance details include **Basic Information**, **Topic Management**, and
**Group Management**.
**Basic Information**: displays information such as **Instance ID/Name**, **Instance**
**Name**, **Cluster ID**, **Product Name**, and **Status**.
**Topic Management**: displays information such as **Topic**, **Type**, and **Description**.
**Group Management**: displays information such as **Group ID**, **Type**, and
**Description**.
On the **Cloud Product Account Management** tab, you can view and modify the account information that is used to access cloud products. View the account information about a cloud product: Enter a product name in the
**Product** field to filter account information. The account information includes **Account**
**Name/ID**, **Cloud Product**, and **Status**.
Modify the account information about a cloud service: Find the account that you want to modify and click **Edit** in the **Operation** column. In the **Edit Account** dialog box, modify the values of **Cloud Product** and **Status** and click **OK**. You cannot modify the value of the **Account Name/ID** parameter.

### Copilot

#### Hot upgrade

This topic describes how to create a hot upgrade task.

**Background information**

A hot upgrade of ApsaraMQ for RocketMQ refers to a version update or configuration adjustment without service interruption to reduce system downtime and maintain service continuity.

**Prerequisites**

An upgrade approval task exists in the current system.

**Procedure**

1. Log in to the RocketMQ 4.x Operations Console.
2. In the left-side navigation pane, choose **Copilot > Upgrade**.
3. On the **Hot upgrade** page, click **create a hot upgrade task** .
4. In the message that appears, click **OK**. You can select a cluster from the **Cluster name**
drop-down list to filter brokers.

| Parameter | Description |
|---|---|
| Broker name | The unique name of a broker group. |
| Broker address | The address of a single broker in the network, which consists of an IP address and a port number. |
| Master/Slave | Indicates the role of the broker instance in the cluster to which it belongs. It can be the primary node or a secondary node. |

| HA status | The operational status of the current broker instance. SYNC STATE: indicates that the broker is in _ the synchronous state. ONLY MASTER: indicates that the broker is _ the only primary node and does not have a corresponding secondary node. ASYNC STATE: indicates that the broker is _ in the asynchronous state, that is, data is being synchronized from the primary node to the secondary node. HAIF STATE: indicates that the broker is in _ the semi-synchronous state. |
|---|---|
| Update time | The time when the HA status was last updated or checked. |
| Upgrade Status | The upgrade status of the broker. |
| Whether to disable writing | Indicates whether to prohibit writing messages to the broker. Yes: indicates that messages cannot be written to the broker. No: indicates that messages can be written to the broker. |
| Inflow TPS | The number of inbound messages per second. Click a value in the Inflow TPS column. In the Top 10 Business Production Traffic Analysis dialog box, view information about the top 10 topics with the most messages sent by current producers, including Topic, TPS, and Timestamp. |
| Outflow TPS | The number of outbound messages per second. Click a value in the Outflow TPS column. In the Top 10 Business Consumption Traffic Analysis dialog box, view information about the top 10 topics with the most consumed messages and the corresponding consumer groups, including Topic, Group, TPS, and Timestamp. |

5. Make sure that **HA status** of the broker in the broker cluster to be upgraded is
**SYNC_STATE**.
In this example, a group of primary and secondary nodes is upgraded. You can repeat Step 6 through Step 9 to upgrade other groups of primary and secondary nodes.
6. Disable writing for a group of primary/secondary nodes.
On the **Hot upgrade** page, click **Write forbidden** in the **Operation** column for a group of primary and secondary nodes. In the message that appears, click **OK**.
7. Upgrade the primary and secondary nodes.
i. After **Upgrade Status** of the primary and secondary nodes changes to **Upgradeable**, click **Upgrade** in the **Operation** column of the primary node. In the message that appears, click **OK**. ii. After **Upgrade Status** of the primary node changes to **Upgrade completed**, click
**Upgrade** in the **Operation** column of the secondary node. In the message that appears,
click **OK**.
8. Enable writing for a group of primary/secondary nodes.
When **Upgrade Status** of the primary and secondary nodes is **Upgrade completed** and
**HA status** is **SYNC_STATE**, click **Release write prohibition** in the **Operation** column for
the primary and secondary nodes. In the message that appears, click **OK**.

#### Disaster recovery deployment

This topic describes how to deploy disaster recovery for a single cluster and scale out a disaster recovery cluster.

**Background information**

After the delivery phase ends, the efficiency of deploying ApsaraMQ for RocketMQ disaster recovery must be improved to reduce the impact on online business. Disaster recovery relationships need to be established in the O&M phase, and O&M personnel schedule and implement related changes.

**Prerequisites**

The cluster is normal. The upgrade and scale-out operations in the primary and secondary data centers follow the standard processes. The primary data center is started normally, whereas the secondary data center is blocked. Through the broker_location, you can view the information about the primary and secondary nodes, and a broker_name table has been successfully allocated in the primary data center.

**Usage notes**

A cluster that contains topics of globally ordered messages does not support disaster recovery deployment. Check the models for the physical nodes where all brokers of ApsaraMQ for RocketMQ are located in the primary and secondary data centers. Make sure that a group of primary and secondary physical nodes uses the same model and disk capacity. When you select a node in the secondary data center for the disaster recovery deployment, make sure that the model of the selected node in the secondary data center is the same as the model of the selected node in the primary data center. If you cannot select physical nodes with the same model from the primary and secondary data centers, proceed with caution or submit a ticket to contact the planner to assess the model risk.

**Deploy disaster recovery for a single cluster**

You can terminate a task in the completed or uncompleted state. If you click **End**
**disaster recovery task**, the task information table is cleared.
1. Log in to the RocketMQ 4.x Operations Console.
2. In the left-side navigation pane, choose **Copilot > Disaster Recovery**.
3. On the **Disaster recovery setup** page, click **Create a disaster recovery task** .
4. In the dialog box that appears, configure the **Cluster** and **Main engine room** parameters
and click **OK**. This operation triggers task creation. The system checks whether an unfinished deployment task exists. If no unfinished deployment task exists, the existing cluster information is synchronized to the new task. The new brokers in the primary data center are displayed at the end of the list and will be published. In addition, the metadata file of a primary broker in the cluster is cached.

| Parameter | Description |
|---|---|
| Broker name | The unique name of a broker group. |
| Broker address | The address of a single broker in the network, which consists of an IP address and a port number. |
| Master/Slave | Indicates the role of the broker instance in the cluster to which it belongs. It can be the primary node or a secondary node. |
| Status | The operational status of the current broker instance. SYNC STATE: indicates that the broker is in _ the synchronous state. ONLY MASTER: indicates that the broker is _ the only primary node and does not have a corresponding secondary node. ASYNC STATE: indicates that the broker is _ in the asynchronous state, that is, data is being synchronized from the primary node to the secondary node. HAIF STATE: indicates that the broker is in _ the semi-synchronous state. |
| Inflow TPS | The number of inbound messages per second. Click a value in the Inflow TPS column. In the Top 10 Business production traffic analysis message, view information about the top 10 topics with the most messages sent by current producers, including Topic, TPS, and Timestamp. |

| Outflow TPS | The number of outbound messages per second. Click a value in the Outflow TPS column. In the Top 10 Business consumption traffic analysis message, view information about the top 10 topics with the most consumed messages and the corresponding consumer groups, including Topic, Group, TPS, and Timestamp. |
|---|---|
| Forbidden to write | Indicates whether to prohibit writing messages to the broker. Yes: indicates that messages cannot be written to the broker. No: indicates that messages can be written to the broker. |
| idc room | The name of the data center to which the broker belongs. |

In this example, a group of primary and secondary nodes is upgraded. You can repeat Step 5 through Step 10 to upgrade other groups of primary and secondary nodes.
5. Disable writing for a group of primary/secondary nodes.
On the **Disaster recovery setup** page, click **Forbidden to write** in the **Operation** column for a group of primary and secondary nodes. In the message that appears, click **OK**. This operation disables the write feature of the corresponding node and observes that the traffic drops to 0.
6. Unpublish the secondary node.
i. When the traffic drops to 0, click **Downline** in the Operation column of the secondary node. In the message that appears, click **OK**. The node is unpublished, the corresponding BrokerName is deleted, and all files except `broker.conf` , `/config/topics.json` , and `/config/subscriptionGroup.json` in the store directory are deleted. After the secondary node is unpublished, the status of the primary node changes to
**ONLY_MASTER**.
7. Add a secondary node to the primary node.
After the secondary node is unpublished, **Add a secondary node** appears in the
**Operation** column of the primary node in the primary data center.
Click **Add a secondary node**, select a secondary node, and click **OK** to add a secondary node in the secondary data center, synchronize the cached metadata file to the broker, and set the broker to read and write prohibiting. Meanwhile, the information about the secondary node is inserted into the broker_name table.
8. Promote the original secondary node to the primary node (published).
After the secondary node is unpublished, **Go online** appears in the **Operation** column of the secondary node in the primary data center. After the secondary node in the secondary data center is added, click **Go online** and then click **OK**. The broker is configured as the new primary node, the cached metadata file is synchronized to the broker, and the broker is set to read and write prohibiting. BrokerName is applied for and inserted into the database. Then, the container is restarted.
9. Add a secondary node to the new primary node.
After the original secondary node is promoted to the primary node, **Add a secondary**
**node** appears in the **Operation** column.
Click **Add a secondary node**, select a secondary node, and click **OK** to add the second secondary node in the secondary data center, synchronize the cached metadata file to the broker, and set the broker to read and write prohibiting. Meanwhile, the information about the second secondary node is inserted into the broker_name table.
0. Remove write prohibition.
Click **Unban writing** in the **Operation** column for the primary and secondary nodes, and then click **OK** in the message that appears. Then, observe the increase in traffic.

**Scale out a disaster recovery cluster**

You can terminate a task in the completed or uncompleted state. If you click **End**
**disaster recovery task**, the task information table is cleared.
1. Log in to the RocketMQ 4.x Operations Console.
2. In the left-side navigation pane, choose **Copilot > Disaster Recovery**.
3. On the **Disaster recovery setup** page, click **Create a disaster recovery task** .
4. In the dialog box that appears, configure the **Cluster** and **Main engine room** parameters
and click **OK**. This operation triggers task creation. The system checks whether an unfinished deployment task exists. If no unfinished deployment task exists, the existing cluster information is synchronized to the new task. The new brokers in the primary data center are displayed at the end of the list and will be published. In addition, the metadata file of a primary broker in the cluster is cached.
5. Publish the new brokers in the primary data center.
If a new broker is added, **Go online** appears in the Operation column for the unpublished secondary broker or new broker in the primary data center. Click **Go online** and then click
**OK**. The broker is configured as the new primary node, the cached metadata file is
synchronized to the broker, and the broker is set to read and write prohibiting. BrokerName is applied for and inserted into the database. Then, the container is restarted.
6. Add a secondary node to the new primary node.
After the original secondary node is promoted to the primary node, **Add a secondary**
**node** appears in the **Operation** column.
Click **Add a secondary node**, select a secondary node, and click **OK** to add the second secondary node in the secondary data center, synchronize the cached metadata file to the broker, and set the broker to read and write prohibiting. Meanwhile, the information about the second secondary node is inserted into the broker_name table.

#### Disaster recovery removal

This topic describes how to remove a disaster recovery relationship.

**Background information**

Disaster recovery relationships between brokers can be removed to scale in a disaster recovery cluster into a single-data center cluster, perform a cluster migration, or implement phased migration to the IT Application Innovation (ITAI) ecosystem.

**Prerequisites**

The cluster is normal. The upgrade and scale-out operations in the primary and secondary data centers follow the standard processes. The primary node is deployed in the primary data center.

**Applicable scope**

A disaster recovery data center needs to be converted into a single data center. A cluster needs to be migrated across data centers. Phased migration to the ITAI ecosystem is required.

**Procedure**

The following procedure uses a group of brokers as an example. The procedure is the same for other groups of brokers.
1. Log in to the RocketMQ 4.x Operations Console.
2. In the left-side navigation pane, choose **Copilot > Disaster Recovery Remove**.
3. On the **Release of disaster recovery relationship** page, select a cluster from the
**Cluster name** drop-down list.
4. The list displays the basic information about brokers.

| Parameter | Description |
|---|---|
| Broker name | The unique name of a broker group. |

| Master/Slave | Indicates the role of the broker instance in the cluster to which it belongs. It can be the primary node or a secondary node. |
|---|---|
| Host IP | The address of a single broker in the network, which consists of an IP address and a port number. |
| Status | The status of the broker. readonly: indicates that the broker is in read-only mode. online: indicates that the broker is online and working properly. offline: indicates that the broker is offline and may be unable to provide services due to faults or other reasons. |
| HA status | The operational status of the current broker instance. SYNC STATE: indicates that the broker is in _ the synchronous state. ONLY MASTER: indicates that the broker is _ the only primary node and does not have a corresponding secondary node. ASYNC STATE: indicates that the broker is _ in the asynchronous state, that is, data is being synchronized from the primary node to the secondary node. HAIF STATE: indicates that the broker is in _ the semi-synchronous state. |
| Inflow TPS | The number of inbound messages per second. Click a value in the Inflow TPS column. In the Top 10 Business production traffic analysis dialog box, view information about the top 10 topics with the most messages sent by current producers, including Topic, TPS, and Timestamp. |
| Outflow TPS | The number of outbound messages per second. Click a value in the Outflow TPS column. In the Top 10 Business consumption traffic analysis dialog box, view information about the top 10 topics with the most consumed messages and the corresponding consumer groups, including Topic, Group, TPS, and Timestamp. |

5. Disable writing for a group of primary/secondary nodes.
On the **Release of disaster recovery relationship** page, click **Write forbidden** in the
**Operation** column for a group of primary and secondary nodes. In the message that
appears, click **OK**. This operation disables the write feature of the corresponding node and observes that the traffic drops to 0.
6. Click **Remove the disaster recovery relationship** in the **Operation** column of the
secondary node, and then click **OK**. This operation stops the broker and removes the information about the node from the broker_name table.
7. After the disaster recovery relationship is removed, you can clear the metadata. Click
**Clean up data** in the **Operation** column of the secondary node to delete files other than

```
 /home/admin/store/broker.conf ,  /home/admin/store/config/topics.json , and
 /home/admin/store/config/subscriptionGroup.json .
```

#### Capacity analysis

You can view the performance metrics of a cluster within a specified time range, including the cluster-level resource usage overview and historical resource usage trends.

**Background information**

Capacity analysis is designed to provide an intuitive and comprehensive visualization platform for you to evaluate and monitor the current load status and capacity usage trends of an ApsaraMQ for RocketMQ cluster. This supports scientific decision-making and proactive O&M.

**Procedure**

1. Log in to the RocketMQ 4.x Operations Console.
2. In the left-side navigation pane, choose **Copilot > Capacity Analyze**.
3. On the **Capacity Analysis** page, specify **Cluster name** and **Time range**, and select a
Broker specification.
4. The page displays the Transactions Per Second (TPS) trend and save time trend.
Move the pointer over a chart to view the detailed values at the current time point.
**tps trend**: displays the trend charts of the inbound message rate, outbound message
rate, and total throughput of the cluster. The dotted orange line in the chart represents the theoretical maximum TPS of the broker specification.
**Save time trend**: displays the trend chart of the retention period of messages on the
broker. The default message retention period is 72 hours.

#### Cluster inspection

You can use the **cluster inspection** feature to inspect clusters and generate cluster inspection reports.

**Create an inspection task**

1. Log in to the RocketMQ 4.x Operations Console.
2. In the left-side navigation pane, choose **Copilot > Cluster Inspection**.
3. On the **Cluster Inspection** page, click **Create an inspection task**.
4. In the **Create an inspection task** dialog box, configure the following parameters and click
**OK**.

| Parameter | Description |
|---|---|

| Inspection task type | One inspection: The inspection task is immediately executed. Scheduled inspection: The inspection task is automatically executed on a regular basis. |
|---|---|
| Scheduled inspection time | This parameter is available only when the Inspection task type parameter is set to Scheduled inspection. You can enter a cron expression or click Use Generator to specify the execution time. |
| Cluster | Select the cluster that you want to inspect. Note If no cluster is selected, the system automatically inspects all clusters and aggregates the results. |
| Inspection settings | Select inspection items. The following table describes the inspection items. |

The following table describes the inspection items.

| Inspection item | Inspection rule |
|---|---|
| Broker Basic Information | Inspects the basic information of the brokers of the cluster, such as the traffic volume, disk space usage, and ZooKeeper status. Note This item is selected by default and cannot be canceled. |
| Broker Permission Check | Inspects whether each broker is readable and writable. |
| Broker Authentication Status Check | Inspects whether each broker has authentication enabled. |
| Message Retention Time Check | Inspects whether the message retention period of the cluster is equal to or greater than 72 hours. |
| Nameserver registration status check | Inspects the registration status of each broker. |

| NameServer Connection Count Check | Inspects the number of nameserver connections and status. |
|---|---|
| NameServer CPU Steal Time Check | Inspects the CPU steal time of the nameserver node. |

**Enable an inspection task**

By default, after an inspection task is created, the task enters the **To be run** state. You can click **Start inspection** to perform an inspection.
1. In the task list, click **Start inspection** in the **Operation** column of the desired inspection
task.
2. In the message that appears, click **OK**.

**Disable an inspection task**

You can disable an inspection task that is in the Running state. After the inspection task is disabled, the system stops running the task.
1. In the task list, click **Close inspection** in the **Operation** column of the desired inspection
task.
2. In the message that appears, click **OK**.

**View inspection results**

1. In the task list, you can view the information of each inspection task, including **Task ID**,
**Cluster**, **Inspection type**, **Inspection items**, **Task Status**, **Latest inspection time**,
**Creation time**, and **Scheduled inspection time**.
Click the information in the **Inspection item** column. In the **Inspection item** dialog box, you can view the inspection items and inspection rules of the current task.
2. Click **View inspection results** in the **Operation** column of the desired inspection tasks.
3. In the **Inspection Task Result** dialog box, you can view **ID**, **Inspection Status**,
**Inspection Duration**, **Creation time**, and **Expiration Time** of the inspection task.
4. Click **View the inspection report** in the **Operation** column of the desired inspection task.
5. In the **Inspection results** panel, you can view the detailed inspection report of the cluster.
You can click **Download Report** to generate and export a complete inspection report of the cluster. The following three report formats are supported: Markdown HTML PDF

**Modify an inspection task**

1. In the task list, click **Editor** in the **Operation** column of the desired inspection task.
2. In the **Edit inspection task** dialog box, specify **Cluster** and **Inspection Settings**, and
click **OK**.

**Delete an inspection task**

You can delete inspection tasks that you no longer need.
1. In the task list, click **Delete** in the **Operation** column of the desired inspection task.
2. In the message that appears, click **OK**.

**Modify inspection rule parameters**

1. On the **Cluster Inspection** page, click **Inspection Config**.
2. On the **Rule Parameters** tab, you can view the current rule parameters, including **ID**,
**Inspection Item**, **Param Name**, **Param Value**, **Operator**, **Unit**, **Alert Level**, and
**Status**.
3. In the rule parameter list, find the rule parameter that you want to modify and click **Edit** in
the **Operation** column.
4. In the **Edit Rule Parameter** dialog box, modify the following parameters and then click
**OK**.

| Parameter | Description |
|---|---|
| Param Value | The numeric threshold for triggering an alert. |
| Operator | The comparison logic to determine whether the actual collected value meets the condition. Valid values: > >= < <= == != |
| Unit | The unit of measurement for the parameter value. |
| Alert Enabled | Specifies whether to enable the rule. On: The system monitors and triggers alerts based on this rule in real time. Off: No alert is generated even if the condition is met. This option is generally used for temporary blocking or debugging. |

| Alert Level | Note This parameter is available only when Alert Enabled is turned on. The severity of the alert. Valid values: P1 P2 P3 P4 |
|---|---|
| Description | The description for the rule. |

For example, to configure an alert rule for a reasonable disk usage, you can configure the following values: Param Value: 83 Operator: > Unit: % Alert Enabled: On Alert Level: P2 Description: An alert is triggered when disk usage exceeds 83%. Please free up space or expand capacity promptly. After the configuration, the system will continuously send P2-level alerts when disk usage reaches 84%, 85%, and so on, until it drops below 83%.

**Modify the weight of an inspection item**

In the cluster inspection system, each inspection item is assigned a weight, which is mainly used to calculate the overall health score.
1. On the **Cluster Inspection** page, click **Inspection Config**.
2. On the **Inspection Weights** tab, you can view **Inspection Item Name**, **Inspection Item**
**Code**, and **Weight Score** of each inspection item.
3. In the inspection item list, click **Edit** in the **Operation** column of the desired inspection
item.
4. In the **Edit Weight** dialog box, modify the value of the **Weight Score** parameter and click
**OK**.
A higher score indicates a greater weight, and the sum of the scores for all inspection items does not need to be equal to 100.

#### Topic migration

The topic migration feature allows you to migrate the data of a specified topic from the source cluster to the destination cluster in a smooth and secure manner. This feature is widely used in scenarios such as cluster scaling, cross-region migration, architecture upgrades, and disaster recovery failovers. It ensures zero-downtime, transparent data migration with no impact on business operations.

**Create a migration task**

Only topics of the normal message type can be migrated.
1. Log in to the RocketMQ 4.x Operations Console.
2. In the left-side navigation pane, choose **Copilot > Topic Migration**.
3. On the **Topic Migration** page, click **Create Migration Task**.
4. In the **Create Migration Task** dialog box, configure the following parameters and click
**OK**.

| Parameter | Description |
|---|---|
| Source Cluster | Select the original cluster that stores the topic to be migrated. |
| Instance | Select the ApsaraMQ for RocketMQ instance to which the topic to be migrated belongs. |
| Topic | The name of the topic to be migrated. |
| Target Cluster | Select the destination cluster to receive the migrated data. |
| Wait Days | The number of days that the system retains source data for rollback or verification after the migration is complete. |

5. After the migration task is created, the **Migration Task Detail** page appears. On the
**Migration Task Detail** page, perform the following steps:
You can cancel a migration task during the migration. In the **Step Logs** section, click **View Detail** to the right of a step to view the details of the step. If a migration step fails, you can click **Retry** to restart the task. i. Perform a pre-check a. Click **Start Check** to perform a pre-check. b. After the pre-check is complete, click **Next: Create Topic**. ii. Create a topic a. Click **Create Topic in Target Cluster** . b. After the topic is created, click **Next: Disable Write on Source Topic** . iii. Disable the write operation on the topic in the source cluster a. Click **Disable Write on Source Topic**. b. After the write operation on the topic in the source cluster is disabled, click **Next:**
**Monitor Consumer**.
iv. Monitor message consumption The automatic refresh interval is 30 seconds. After the number of accumulated messages in all consumer groups becomes 0 (Lag = 0), go to the next step to disable the read on the topic of the source cluster. a. After the wait period is complete, the system automatically monitors message consumption. You can click **Skip Consumer Check and Wait Period** to immediately start monitoring consumers. b. After message consumption monitoring is complete, click **Next: Disable Read on**
**Source Topic**.
v. Disable the read operation on the topic in the source cluster a. Click **Disable Read on Source Topic**. b. After the read operation on the topic in the source cluster is disabled, click **Next:**
**Cleanup Topic**.
vi. Clean up the topic a. Click **Delete Source Cluster Topic**. In the message that appears, click **OK**. b. After the topic in the source cluster is deleted, the operation is complete.

**View the details of a migration task**

1. Optional. On the **Topic Migration** page, you can filter migration tasks by **Topic**, **Status**,
**Cluster**, and **Instance ID**.
2. In the migration task list, you can view the following information about migration tasks:
**Task ID**, **Instance ID**, **Topic**, **Source Cluster**, **Target Cluster**, **Current Step**, **Status**,
and **Create Time**.
3. Click **View Detail** in the **Operation** column of a migration task. On the **Migration Task**
**Detail** page, you can view **Task Info**, **Task Result**, and **Step Logs** of the migration task.
In the **Step Logs** section, click **View Detail** to the right of a step to view the details of the step.

**Delete a migration task**

Migration tasks cannot be deleted while in progress.
1. In the migration task list, find the migration task that you want to delete and click **Delete** in
the **Operation** column.
2. In the message that appears, read the tips and then click **OK**.

**Important**

If you delete a task, the task records and step logs are permanently removed. Proceed with caution.

**Cancel a migration task**

You cannot cancel **Failed** or **Completed** migration tasks.
1. In the migration task list, find the migration task that you want to cancel and click **Cancel**
in the **Operation** column.
2. In the dialog box that appears, enter the reason for cancellation and click **OK**.

**Important**

When you cancel a migration task, the executed steps are rolled back (the permissions on the source cluster are restored and the topic in the destination cluster is deleted), which may result in the loss of unconsumed messages already sent to the destination cluster. Proceed with caution.

**Retry a migration task**

You can retry only **Failed** migration tasks.
1. In the migration task list, find the migration task that you want to retry and click **Retry** in
the **Operation** column.
2. In the message that appears, read the tips and then click **OK**.
When you retry a migration task, the task will resume execution from the failed step.

### Operational audit

This topic describes how to view the logs of operations performed on an ApsaraMQ for RocketMQ 4.x cluster.

**Procedure**

1. Log in to the RocketMQ 4.x Operations Console.
2. In the left-side navigation pane, click **Operational Log**.
3. Optional. You can specify **Operation type**, **Operator**, and **Operation Time** to filter
operation logs.
4. In the operation log list, you can view the following information: **ID**, **Operator ID/name**,
**Department ID**, **Operation type**, **Operation Time**, **Action Item**, and **Operation**
**parameters**.

## High-risk operations

### Levels of O&M operations

O&M operations are classified into the following three levels based on the business scenarios and risk degree: G1, G2, and G3. When you perform O&M operations as Level-1 and Level-2 support engineers, take note of the following rules: G1: You can follow the instructions in related documents, without the need to apply for changes. Such operations will not affect the business. G2: Before you can follow the instructions in related documents, you must apply for changes and obtain approval from the product line. Such operations will not affect the business. G3: Before you can follow the instructions in related documents, you must submit a ticket to apply for changes and obtain approval from the product line and customer. Such operations may affect the business.

### High-risk operations and files

This topic describes the high-risk operations that you must pay special attention to and the high-risk files that cannot be randomly deleted during O&M.

**High-risk operations**

High-risk operations are the **G3**-level O&M operations defined in the "Levels of O&M operations" topic. Follow the corresponding instructions when you perform such operations.

**High-risk files**

High-risk files are the files that cannot be randomly deleted. When you process these files, take note of the following rules: In principle, the files that have not dynamically grown since they are generated cannot be deleted. If you need to delete these files such as the legacy packages that are no longer used after upgrade, you must confirm this operation with the product line and customer. Do not delete configuration files. All content in the conf directory are protected. The files in the application package directory cannot be deleted. The log files that are in use cannot be deleted. For example, the mw.log file is in use and the mw-2018-07-22.log file is used to archive historical data. In this case, do not delete the mw.log file. A broker manage its high-risk files. You cannot manually delete these files. Table 1. High-risk files

| File | Purpose | Description |
|---|---|---|

| /home/admin/store/commitlog/* | Stores the messages that are submitted by producers. These files are data files. | The mapedFileSizeCommitLog parameter in the /home/admin/rmq/conf/broke r.conf file specifies the size of each file. By default, each file is 1 GB in size. The deleteWhen parameter in the /home/admin/rmq/conf/broke r.conf file specifies the time to delete outdated data. By default, outdated data is deleted at 04:00 every morning. The diskMaxUsedSpaceRatio parameter in the home/admin/rmq/conf/broker .conf file specifies the space usage threshold for deleting outdated data. By default, outdated data is deleted when the storage usage reaches 75%. The leanFileForciblyEnable parameter in the home/admin/rmq/conf/broker .conf file specifies whether to forcibly delete outdated files when the disk is full. |
|---|---|---|
| /home/admin/store/config/cons umerOffset.json | Stores the consumer offsets. | This file is managed by brokers and cannot be manually deleted. |
| /home/admin/store/config/delay Offset.json | Stores the consumer offsets of retry queues. | This file is managed by brokers and cannot be manually deleted. |
| /home/admin/store/config/subsc riptionGroup.json | Stores the consumer group configurations. | This file is managed by brokers and cannot be manually deleted. |
| /home/admin/store/config/topic s.json | Stores the topic configurations. | This file is managed by brokers and cannot be manually deleted. |

## O&M preparation

This topic describes the logon portal, account, permissions, and tools required for O&M. Table 1. O&M preparation

| Item | Purpose | Description |
|---|---|---|
| Secure Shell (SSH) clients such as MobaXterm and PuTTY | Used to log on to the servers where related components reside. | The account used to log on to the servers must be granted permissions to perform related operations. However, we recommend that you do not use the root or admin account. |
| Account | Used to log on to the Message Queue for Apache RocketMQ console or the servers where related components reside. | You can obtain the username and password for logging on to the console from the technical support engineers of Message Queue for Apache RocketMQ. The account used to log on to the servers must be granted permissions to perform related operations. However, we recommend that you do not use the root or admin account. |

## Routine maintenance

ApsaraMQ for RocketMQ inspection and monitoring cover two aspects: components and services.

**Component inspection and monitoring**

Monitor the statuses of the following ApsaraMQ for RocketMQ components: Address Servers, Name Servers, brokers, Controller, Housekeeping, and the console.

**Service inspection and monitoring**

Inspect and monitor the core link of ApsaraMQ for RocketMQ during operation, covering core business, kernel parameters, application configurations, application metrics, and the console.

### Component inspection and

**monitoring**

Component inspection and monitoring for ApsaraMQ for RocketMQ cover the following aspects: Inspection: Periodically perform a dial test on URLs or ports to determine whether ApsaraMQ for RocketMQ components are normal. Inspections in HTTP, TCP, ping, and JDBC modes are supported. Monitoring: Collect logs from clients by using Tlog. Aggregate container monitoring data and custom metrics to measure the status of system operation.

#### Manual inspection

Linux commands are used for manual inspection. You can set specific parameters based on the actual environment.

##### Name server inspection

1. Log on to the container of a name server.
2. Run the ps aux|grep -i NamesrvStartup command to check whether the state of the Java
process of the name server is normal.
3. Run the `ss -s` command to check the number of connections. If the number of
connections is more than half of the maximum number of connections that are allowed for the name server, submit a ticket to contact O&M engineers.

##### Console inspection

The Message Queue for Apache RocketMQ console is a web system deployed in Tomcat. Perform the following steps to perform routine inspection:
1. Log on to the container of the Message Queue for Apache RocketMQ console.
2. Run the netstat -an |grep 7001 command to check whether the Tomcat process exists
and whether Port 7001 is enabled.
3. Check whether the NGINX process exists and whether Port 80 properly forwards packets to
Port 7001.
4. Check the /home/admin/logs/ons-api/*.log file to determine whether a major exception
exists.
5. Check whether an unwanted log file needs to be cleared from the /home/admin/ons-api/logs
directory.
6. Check whether the disk size is sufficient in /home/admin.

##### Controller inspection

1. Log on to the container of a controller.
2. Run the ps aux|grep -i FailoverStartUp command to check whether the state of the
Java process of the controller is normal.
3. Run the `grep 'take the leadership of role'`
`/home/admin/logs/rocketmqlogs/failover_controller.log` command to determine which of the two controllers is managing the failover.
4. Check the files in the `/home/admin/logs/rocketmqlogs/*.log` path to determine whether an
obvious exception error exists.

##### Broker inspection

1. Log on to the container of a broker.
2. Run the ps aux|grep brokerStartup command to view the process information.
3. Run the `ss -s` command to check the number of connections. If more than half of the
connections are in use, contact after-sales engineers.
4. View the logs of the broker in the /home/admin/logs/rocketmqlogs/ directory.
5. Run the `df -h` command. Make sure that the disk usage is less than 80%.
6. Check whether the following configurations exist in the /home/admin/store directory:
/home/admin/store/config/consumerOffset.json: consumer offsets. /home/admin/store/config/delayOffset.json: consumer offsets of scheduled messages. /home/admin/store/config/subscriptionGroup.json: consumer group configurations. /home/admin/store/config/topics.json: topic configurations. /home/admin/store/consumequeue: consumption index file. It is stored by topic. /home/admin/store/index: index file for key-based message query.
7. Check the commit log after a message is sent.
i. Check whether a file is generated in the /home/admin/store/commitlog directory. ii. Run the du -sh /home/admin/store/commitlog/* command to check whether new data is written to the file. iii. Run the `sh /home/admin/rmq/bin/mqadmin clusterlist` command to view the message sending and receiving status of all brokers in the cluster. Check the message sending and receiving status of the current broker.

##### Address Server inspection

1. Log on to the container of an Address Server.
An Address Server is an NGINX process module. By default, HTTP port 8080 is enabled.
2. Run the `curl -v 'http://localhost:8080/rocketmq/nsaddr4broker-internal'` command to
check the configurations of Name Servers on the Address Server. If the configurations of Name Servers are normal, the status code 200 and the content in /home/admin/cai/htdocs/rocketmq/nsaddr4broker-internal are returned.

##### Diamond Server inspection

1. Log on to the container of a Diamond Server.
2. Run the `df -lh` command to check the disk space. This prevents exceptions caused by
full disk storage.

| top | command to verify that |
|---|---|
| ping jmenv.tbsite.net -c 3 |   |

3. Run the `top` command to verify that the memory usage and CPU utilization are normal.
4. Run the `ping jmenv.tbsite.net -c 3` command to verify that Address Servers can be
reached with a low latency. For example, Address Servers can be reached within 10 ms over internal networks.
5. Run a script to cyclically ping all Diamond Servers. Make sure that the Diamond Servers
can connect to each other with a low latency.
6. Run the `tsar --nginx --load --cpu -l -i3` command to verify that the load on Diamond
Servers is in a controllable range. The single-server queries per second (QPS) limit is approximately 4,000. We recommend that the single-server QPS be less than 500, the number of processes that are being executed be less than the number of CPU cores, and the CPU utilization be less than 20%.

##### DAuth inspection

DAuth is a web system deployed in Tomcat. Perform the following steps to perform routine inspection:
1. Log on to the container of DAuth.
2. Check whether the Tomcat process exists and whether Port 8080 is enabled.
3. Check whether the NGINX process exists and whether Port 80 properly forwards packets to
Port 8080.
4. Check the /home/admin/dauth/logs/*.log file to determine whether a major exception exists.
5. Check whether an unwanted log file needs to be cleared from the /home/admin/dauth/logs
directory.
6. Run the curl 'localhost:8080'|grep Unsupported command. If the command output contains
the Unsupported keyword, DAuth is normal.
7. Check whether the disk size is sufficient in /home/admin.
8. DAuth also serves as a client connected to Diamond Servers. Pay attention to the following
aspects during inspection: Check the /home/admin/logs/diamond-client/diamond-client.log file to determine whether a major exception exists.

```
Run the curl 'http://jmenv.tbsite.net:8080/diamond-server/diamond-unit-spas'
```

command to obtain the server list of the Diamond Spas unit. Ping each server. Make sure that the latency is less than 10 ms.

##### Tlog console inspection

Log on to the container of the Tlog console. Run the ps aux|grep tomcat command to check the Tomcat process. Run the `df -h` command to check the disk space. Run the `curl -v 'http://localhost'` command to check whether the access is normal.

### Service inspection and

**monitoring**

The Housekeeping component of Message Queue for Apache RocketMQ is responsible for service inspection. Housekeeping periodically inspects various metrics of Message Queue for Apache RocketMQ, and records alert information in the /home/admin/logs/aliware-mq-hkagent/warning.log file in the container of Housekeeping. The metrics of Message Queue for Apache RocketMQ are fixed and cannot be changed.

### Logs

Logs are one of the most important O&M methods for ApsaraMQ for RocketMQ. They are used for monitoring and troubleshooting. Therefore, routine log maintenance is required. ApsaraMQ for RocketMQ logs include basic monitoring logs, service monitoring logs, container monitoring logs, and Java virtual machine (JVM) monitoring logs. For more information, see Log reference.

## O&M commands

Backend O&M commands are provided for experienced O&M engineers. We recommend that you perform related operations in the ApsaraMQ for RocketMQ console.

### Overview

Message Queue for Apache RocketMQ provides a backend O&M tool to facilitate routine O&M. The O&M tool is named sh mqadmin in the /home/admin/rmq/bin/ directory. To run O&M commands, you must log on to the container of a Name Server or broker.
1. Run the docker exec -it <Name Server or broker container ID> /bin/bash command to log
on to the container of the Name Server or broker.
2. Run O&M commands in the /home/admin/rmq/bin directory.

**Command examples**

Run the cd command in the mq-broker container to go to the rmq/bin directory, and then use the O&M tool to run relevant commands. Display all supported commands: `./mqadmin` Display the help information (usage and parameters) of the clusterList command:

```
 ./mqadmin help clusterList
```

Run the clusterList command to show the cluster list and details: `./mqadmin clusterList -` `m` The clusterList command uses the following syntax: `mqadmin clusterList [-h] [-i <arg>] [-` `m] [-n <arg>]` . When you use the clusterList command, take note of the following rules: `-h` , `-i` , `-m` , and `-n` are short IDs of parameters. If a short ID is provided, the corresponding option and parameter are specified. The short IDs enclosed in brackets indicate optional parameters. arg enclosed in angle brackets indicates that the parameter must be set to a specific value, for example, `./mqadmin clusterList -i 3 -m` .

**Resource naming**

The naming rules for the resources contained in instances with or without namespaces have been changed in Message Queue for Apache RocketMQ V3.8.1 and later. Take note of the following rules: Topic naming Instances with namespaces: instanceid%topic Instances without namespaces: topic Group ID naming Instances with namespaces: instanceid%gid Instances without namespaces: gid For information about instance namespaces, see Updates.

### View all O&M commands

Table 1. mqadmin

| Command | Description |
|---|---|
| updateTopic | Create a topic. |
| deleteTopic | Delete a topic. |
| topicList | View the topic list information. |
| topicCLusterList | View the cluster of a topic. |
| topicRoute | View the topic route information. |
| updateTopicPerm | Update the read and write permissions for a topic. |
| topicStatus | View topic statistics. |
| brokerStatus | View the status of a broker. |
| wipeWritePerm | Revoke the specified permissions from a broker. |
| updateBrokerConfig | Update the configurations of a broker. |
| producerConnection | View the connection status of a producer. |
| consumerConnection | View the connection status of a consumer. |
| brokerConsumerStats | View the consumption status of all group IDs of a broker. |
| updateSubGroup | Create or modify a consumer group. |
| deleteSubGroup | Delete a consumer group. |
| consumerProgress | View the consumption status of a consumer group. |
| consumerStatus | Obtain the consumption progress of a consumer. |
| queryMsgById | Query messages by message ID. |
| queryMsgByKey | Query messages by message key. |
| queryMsgByOffset | Query messages by message offset. |
| printMsg | View the messages in the specified period under a topic. |
| clusterList | View the cluster information. |
| resetOffsetByTime | Reset the offset. |

### updateTopic

Table 1. updateTopic

| Parameter | Required | Description |
|---|---|---|

| -b | Yes if -c is empty | The address of the broker on which the topic resides. |
|---|---|---|
| -c | Yes if -b is empty | The name of the cluster on which the topic resides. You can run the clusterList command obtain the cluster list. |
| -n | Yes | The addresses of Name Servers. The value is in the format of ip:port;ip:port. |
| -p | No | The permission of the topic to be created. Valid values: W, R, and WR. |
| -r | No | The number of readable queues. Default value: 8. |
| -w | No | The number of writable queues. Default value: 8. |
| -t | Yes | The name of the topic. |

### deleteTopic

This command is high-risk. Proceed with caution. Table 1. deleteTopic

| Parameter | Required | Description |
|---|---|---|
| -c | Yes | The name of the cluster on which the topic resides. You can run the clusterList command to obtain the cluster list. |
| -n | Yes | The addresses of Name Servers. The value is in the format of ip:port;ip:port. |
| -p | Yes | The name of the topic. |

### topicList

Table 1. topicList

| Parameter | Required | Description |
|---|---|---|
| -n | Yes | The addresses of Name Servers. The value is in the format of ip:port;ip:port. |

### topicClusterList

Table 1. topicClusterList

| Parameter | Required | Description |
|---|---|---|
| -n | Yes | The address of the Name Server. Example: 192.168.0.1:9876. |
| -t | Yes | The name of the topic. |

### topicRoute

Table 1. topicRoute

| Parameter | Required | Description |
|---|---|---|
| -t | Yes | The name of the topic. |
| -n | Yes | The addresses of Name Servers. The value is in the format of ip:port;ip:port. |

### updateTopicPerm

This command is high-risk. Proceed with caution. Table 1. updateTopicPerm

| Parameter | Required | Description |
|---|---|---|
| -b | Yes if -c is empty | The address of the broker. |
| -c | Yes if -b is empty | The name of the cluster. |
| -p | Yes | The type of permissions. A value of 2 indicates write- only permissions. A value of 4 indicates read-only permissions. A value of 6 indicates read and write permissions. |
| -t | Yes | The name of the topic. |
| -n | Yes | The addresses of Name Servers. The value is in the format of ip:port;ip:port. |

### topicStatus

Table 1. topicStatus

| Parameter | Required | Description |
|---|---|---|
| -t | Yes | The name of the topic. |

### brokerStatus

Table 1. brokerStatus

| Parameter | Required | Description |
|---|---|---|
| -b | Yes if -c is empty | The address of the broker. Example: 11.164.190.48:10911. |
| -c | Yes if -b is empty | The name of the cluster. |
| -n | Yes | The address of the Name Server. Example: 192.168.0.1:9876. |

### wipeWritePerm

This command is high-risk. Proceed with caution. Table 1. wipeWritePerm

| Required | Description |
|---|---|
| Yes | The name of the broker. |

### updateBrokerConfig

This command is high-risk. Proceed with caution. Table 1. updateBrokerConfig

| Parameter | Required | Description |
|---|---|---|
| -b | Yes if -c is empty | The address of the broker on which the topic resides. |
| -c | Yes if -b is empty | The name of the cluster on which the topic resides. You can run the clusterList command to obtain the cluster list. |
| -k | Yes | The name of the broker configuration item. |
| -v | Yes | The value of the broker configuration item. |
| -n | Yes | The addresses of Name Servers. The value is in the format of ip:port;ip:port. |

### producerConnection

Table 1. producerConnection

| Parameter | Required | Description |
|---|---|---|
| -g | Yes | The group ID of the producer. The format of the value varies depending on whether the instance has a namespace. If the instance has a namespace, the value is in the format of instanceid%gid. If the instance does not have a namespace, the value is in the format of gid. |
| -t | Yes | The name of the topic. |

### consumerConnection

Table 1. consumerConnection

| Parameter | Required | Description |
|---|---|---|
| -g | Yes | The group ID of the consumer group. |
| -n | Yes | The addresses of Name Servers. The value is in the format of ip:port;ip:port. |

### brokerConsumeStats

Table 1. brokerConsumeStats

| Parameter | Required | Description |
|---|---|---|

| -b | Yes | The address of the broker. Example: 11.164.190.48:10911. |
|---|---|---|
| -t | No | The timeout period, in milliseconds. Default value: 50000. |

### updateSubGroup

Table 1. updateSubGroup

| Parameter | Required | Description |
|---|---|---|
| -b | Yes if -c is empty | The address of the broker on which the topic resides. |
| -c | Yes if -b is empty | The name of the cluster on which the topic resides. You can run the clusterList command to obtain the cluster list. |
| -g | Yes | The name of the consumer group. |
| -n | Yes | The addresses of Name Servers. The value is in the format of ip:port;ip:port. |
| -d | No | Specifies whether to allow consumption in broadcasting mode. |
| -m | No | Specifies whether to allow consumption starting from the minimum position of the queue. Default value: false. |
| -q | No | The number of retry queues for each consumer group. Messages to be consumed are placed in a retry queue. |
| -r | No | The maximum number of consumption retries. If the maximum number of consumption retries is exceeded for a message, the message is delivered to the dead-letter queue and no more delivery attempts are made. |
| -s | No | Specifies whether to enable consumption. |

### deleteSubGroup

This command is high-risk. Proceed with caution. Table 1. deleteSubGroup

| Parameter | Required | Description |
|---|---|---|
| -b | Yes if -c is empty | The address of the broker on which the topic resides. |
| -c | Yes if -b is empty | The name of the cluster on which the topic resides. You can run the clusterList command to obtain the cluster list. |
| -g | Yes | The name of the consumer group. |
| -n | Yes | The addresses of Name Servers. The value is in the format of ip:port;ip:port. |

### consumerProgress

Table 1. consumerProgress

| Parameter | Required | Description |
|---|---|---|
| -g | Yes | The group ID of the consumer group. The format of the value varies depending on whether the instance has a namespace. If the instance has a namespace, the value is in the format of instanceid%gid. If the instance does not have a namespace, the value is in the format of gid. |
| -n | Yes | The addresses of Name Servers. The value is in the format of ip:port;ip:port. |

### consumerStatus

Table 1. consumerStatus

| Parameter | Required | Description |
|---|---|---|
| -g | Yes | The name of the consumer group. |
| -i | No | The IP address of the consumer. |
| -n | Yes | The addresses of Name Servers. The value is in the format of ip:port;ip:port. |
| -s | No | Specifies whether to display the stack information. |

### queryMsgById

Table 1. queryMsgById

| Parameter | Required | Description |
|---|---|---|
| -i | Yes | The ID of the message. |
| -n | Yes | The addresses of Name Servers. The value is in the format of ip:port;ip:port. |

### queryMsgByKey

Table 1. queryMsgByKey

| Parameter | Required | Description |
|---|---|---|
| -k | Yes | The key content set in the message. |
| -t | Yes | The name of the topic. |
| -n | Yes | The addresses of Name Servers. The value is in the format of ip:port;ip:port. |

### queryMsgByOffset

Table 1. queryMsgByOffset

| Parameter | Required | Description |
|---|---|---|
| -o | Yes | The offset of the message. |
| -i | Yes | The ID of the queue. |
| -b | Yes | The address of the broker on which the topic resides. |
| -t | Yes | The name of the topic. |

### printMsg

Table 1. printMsg

| Parameter | Required | Description |
|---|---|---|
| -b | Yes | The beginning of the time range to query. Specify the time in the format of yyyy-MM- dd#HH:mm:ss:SSS. |
| -e | Yes | The end of the time range to query. Specify the time in the format of yyyy-MM- dd#HH:mm:ss:SSS. |
| -d | No | Specifies whether to display the message body. |
| -s | No | The tag of the message. The value is in the format of TagA \|\| TagB. Default value: *. |
| -c | No | The encoding format, such as UTF-8 or GBK. |
| -t | Yes | The name of the topic. |

### clusterList

Table 1. clusterList

| Parameter | Required | Description |
|---|---|---|
| -m | Yes | Specifies whether to display cluster statistics. |
| -i | No | The interval between executions, in seconds. |
| -n | Yes | The addresses of Name Servers. The value is in the format of ip:port;ip:port. |

### resetOffsetByTime

This command may cause messages to be repeatedly consumed or skipped without consumption. Table 1. resetOffsetByTime

| Parameter | Required | Description |
|---|---|---|
| -g | Yes | The group ID of the consumer. The format of the value varies depending on whether the instance has a namespace. If the instance has a namespace, the value is in the format of instanceid%gid. If the instance does not have a namespace, the value is in the format of gid. |
| -s | Yes | The time. Specify the time in the format of yyyy- MM-dd#HH:mm:ss:SS. |
| -t | Yes | The name of the topic. |

## O&M activities

### Instance throttling

By default, throttling is disabled for ApsaraMQ for RocketMQ instances. The system does not limit the outbound message Transactions per Second (TPS). To limit the outbound message TPS, you can enable the instance throttling feature.

**Background information**

After the instance throttling feature is enabled, ApsaraMQ for RocketMQ stops receiving messages when the outbound message TPS threshold is exceeded.

**Prerequisites**

The throttling component **MQFlowLimit** is deployed to the cluster in which the ApsaraMQ for RocketMQ instance resides. Clock synchronization is complete between the tokenserver container in MQFlowLimit and the broker container. If not, the throttling accuracy will be affected.

**Usage notes**

Instance throttling is a high-risk operation that may adversely affect your business. Before you enable the instance throttling feature, consult Apsara Stack engineers and your customer. If you deploy the throttling component to a cluster in which an existing ApsaraMQ for RocketMQ instance runs, you need to roll back the cluster. When you roll back the cluster, the Console component is restarted but the broker is not restarted. Throttling takes effect only on instances that are created after the deployment and existing instances that have broker configurations updated. You can view instances for which the instance throttling feature is enabled in the flow_limit table in the onsflowlimit database.

**Step 1: Enable instance throttling**

1. Log in to the RocketMQ 4.x Operations Console.
2. In the left-side navigation pane, click **Broker Management**.
3. On the **Broker Management** page, click the name of a broker or click **View** in the
**Operation** column.
4. On the **Broker details** page, click the **Configuration information** tab.
5. In the **Configuration name** search box, enter **enableSendFlowlimit.**
6. Click **Modification** to the right of **enableSendFlowlimit**.
7. In the **Modify Configuration** dialog box, turn on **Configuration Value** and click **OK**.

**Important**

Repeat the steps to turn on the instance throttling switch for all brokers of the cluster.

**Step 2: Enable instance throttling reports**

1. Log in to the UiConsole console.
i. Log in to the Apsara Uni-manager Operations Console. ii. In the top navigation bar, choose **Platform Operation > Management and Control**
**Service O&M > UniConsole**.
2. On the **Products** page, enter **mq** into the search box and click **Search**.
3. Find **rocketmq** in the search results and click **Switch List** in the **Actions** column.
4. On the **rocketmq Switches** page, enter
`privateCloud.trafficLimit` into the search box and click **Search**.
5. Find **privateCloud.trafficLimit** in the search results and turn on the switch in the **Current**
**Value** column.

## Capacity assessment

### Name Server connections

**Metrics**

**Current resource usage**:
Log on to the mq-namesrv container and run the ss -s command.
**Benchmark and resource usage threshold** :
If more than half of the connections are in use, contact O&M engineers.

### Broker connections

**Metrics**

**Current resource usage**:
Log on to the mq-broker container and run the ss -s command.
**Benchmark and resource usage threshold** :
If more than half of the connections are in use, contact O&M engineers.

## Log reference

You can check logs to view the status of each Message Queue for Apache RocketMQ component or locate faults during O&M. This topic lists the paths of all the log files of Message Queue for Apache RocketMQ components and provides relevant descriptions. Table 1. Component logs

| Component | File | Description |
|---|---|---|
|   | /home/admin/logs/rocketmqlog s/broker.log | Keyword: Register broker to name server Check whether a broker is registered: The information "Register broker to name server {ip} OK" indicates that the broker has been registered on a Name Server. That is, the broker can be found in the cluster list. |
|   | /home/admin/logs/rocketmqlog s/remoting.log | Find the IP address of the client to determine when the network is disconnected. Many Message Queue for Apache RocketMQ projects involve remote calls. This log file is rarely used. |
|   | /home/admin/logs/rocketmqlog s/failover controller.log _ | Provide the information about primary/secondary switchovers, especially the switchover time of the state machine. |
|   | /home/admin/logs/rocketmqlog s/filter.log | Provide the filtered control results. A tag-like expression is used in Message Queue for Apache RocketMQ to configure filter conditions. |
|   | /home/admin/logs/rocketmqlog s/lock.log | Keyword: tryLockBatch Provide the binding relationship between consumers and queues. One queue can be allocated only to one consumer instance. The unlockBatch log is generated when a consumer instance is discontinued. |

|   | /home/admin/logs/rocketmqlog s/time.log | Provide the information about scheduled messages. Scheduled messages are first stored in the database on the server. Then, the database polls the messages to detect the messages whose sending time is approaching, and sends the messages by using the broker. Keywords: Scan add infly If a scheduled message is not delivered or not punctual, you can search for "Scan add infly: msgID" and view the point in time at which the message is pulled from the database and put into the broker for delivery. You can view the point in time at which the message is pulled in the time.log file based on the message ID. Then, you can refer to the trace to check when and where the process is blocked and slowed down. |
|---|---|---|
|   | /home/admin/logs/rocketmqlog s/transaction.log | Provide the information about transactional messages and in- doubt transactional messages. These messages are first stored in the database on the server. Some messages are transactions in the doubted state. In-doubt transactions that are not committed will be scanned by the database and the producer will be regularly asked for confirmation on these transactions. |

| Broker |   |   |
|---|---|---|
|   | /home/admin/logs/rocketmqlog s/stats.log | Record the transactions per second (TPS) of the current broker to facilitate query for historical TPS. In addition, the resource report is generated by aggregating these logs. Keywords: BROKER PUT NUMS: the TPS of _ _ writing messages per minute. BROKER GET NUMS: the TPS of _ _ reading messages per minute. This log file can be used for troubleshooting of a message reading or writing failure at a specific point in time. It can be used with Tlog to generate reports. |
|   | /home/admin/logs/rocketmqlog s/store.log | Provide macro statistics on TPS. Keywords: PAGECACHERT totalput: the TPS of writing messages. putmessagedistributetime: the number of messages that can be stored on the disk within the required duration. The messages are classified by time consumption. Messages are considered normal if they can be stored on the disk within 10 ms. This log file can be used to troubleshoot low TPS. It is usually used to analyze latency during stress testing. Serial writing of commitLog can be detected with ease. |

|   | /home/admin/logs/rocketmqlog s/dup.log | Provide the information about primary/secondary switchovers. The broker plays the role of SYNC MASTER. _ The state machine has the following states: 1. orignal-state: NULL STATE _ 2. singal-master-state: ONLY MASTER _ 3. async-sync-state: ASYNC STATE _ 4. semi-sync-state: HALF SYNC _ 5. sync-state: SYNC STATE _ The following content describes the state transition of the state machine after the service is started: The state machine is in the original state (NULL STATE) _ when the service is started. After the primary broker is started, the state machine transits to the ONLY MASTER _ state. Start the secondary broker and asynchronously synchronize messages to the secondary broker. The primary broker continues to write requests. When the message synchronization offset is less than 100 messages, hold the write requests to the primary broker, and enable the secondary broker in the HALF SYNC state to continue _ asynchronous replication. The state machine transits to the synchronous replication state (SYNC STATE) when all _ messages are written to the secondary broker. Controller determines which broker is primary or secondary. In Apsara Stack, approximately 99.99% of brokers are deployed in primary/secondary synchronous mode. Keyword: DuplicationStatus voteDupoffset identifies an offset. If it continues to grow, the consumer offset is normal. |
|---|---|---|

|   | /home/admin/logs/rocketmqlog s/dup-stats.log | Provide performance monitoring data such as the number of tasks, the writing latency of the secondary broker, and the writing latency of the on-premises broker. |
|---|---|---|
|   | /home/admin/logs/rocketmqlog s/dup-study.log | Provide the asynchronous replication status of the primary and secondary brokers. |
|   | /home/admin/logs/rocketmqlog s/broker default.log _ | Provide watermark data. This log file is of little significance for troubleshooting. |
|   | /home/admin/logs/rocketmqlog s/rocketmq.log | This log file is of little significance for troubleshooting. |
|   | /home/admin/logs/spas/spas sd _ k.log | Provide authentication, permission, validation, and authorization information. Obtain the UID of the Apsara Stack tenant account based on the AccessKey pair to determine the matched topic in the database. Check whether authorization is obtained. Permission rules: The AccessKey ID and AccessKey secret of the account used to create the topic in the console are used by the client port. |
| Name Server | /home/admin/logs/spas/spas sd _ k.log | Provide authentication, permission, validation, and authorization information. Obtain the UID of the Apsara Stack tenant account based on the AccessKey pair to determine the matched topic in the database. Check whether authorization is obtained. Permission rules: The AccessKey ID and AccessKey secret of the account used to create the topic in the console are used by the client port. |
|   | /home/admin/logs/rocketmqlog s/namesrv.log | N/A |

| Console | /home/admin/logs/spas/spas sd _ k.log | Provide authentication, permission, validation, and authorization information. Obtain the UID of the Apsara Stack tenant account based on the AccessKey pair to determine the matched topic in the database. Check whether authorization is obtained. Permission rules: The AccessKey ID and AccessKey secret of the account used to create the topic in the console are used by the client port. |
|---|---|---|
|   | /home/admin/rmq/ons- api/register.log | Allow users to query the information about the following operations: Add, delete, modify, and query topics. Add, delete, modify, and query group IDs. |
|   | /home/admin/rmq/ons- api/rest.log | Record exceptions of console operations. |
| Address Server | /home/admin/cai/logs/error.log | Provide execution error logs of Address Servers. |
|   | /home/admin/cai/logs/access.lo g | Provide access logs of Address Servers. |
| Controller | /home/admin/logs/rocketmqlog s/failover controller.log _ | Provide the primary/secondary switchover logs of brokers. After the logs are generated, you need to check and analyze whether the operations are normal. |
| Housekeeping | /home/admin/logs/aliware-mq- hkagent/warning.log | Record the inspection results of the inspection tool provided by Message Queue for Apache RocketMQ. After the logs are generated, you need to check and analyze whether the operations are normal. |
