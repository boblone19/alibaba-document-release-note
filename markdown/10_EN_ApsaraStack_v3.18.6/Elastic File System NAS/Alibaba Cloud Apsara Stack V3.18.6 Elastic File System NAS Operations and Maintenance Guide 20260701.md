---
title: "Elastic File System NAS Operations and Maintenance Guide"
product_version: "V3.18.6"
doc_version: "20260701"
pdf_pages: 35
source_pdf: "76ed93e132a54a57_Alibaba Cloud Apsara Stack V3.18.6 Elastic File System NAS Operations and Maintenance Guide 20260701"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/v3.18.6%E7%89%88%E6%9C%AC%E6%96%87%E6%A1%A3/%E9%98%BF%E9%87%8C%E4%BA%91%E5%BC%B9%E6%80%A7%E6%96%87%E4%BB%B6%E5%AD%98%E5%82%A8%20EFS-NAS/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.6%20Elastic%20File%20System%20NAS%20Operations%20and%20Maintenance%20Guide%2020260701.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings)
---

# Elastic File System NAS Operations and Maintenance Guide

## Table of Contents

- 1 Log in to the Apsara Uni-manager Operations Console
- 2 O&M overview
- 3 Configure permissions
- 4 Cluster O&M
  - 4.1 Cluster O&M overview
  - 4.2 View cluster details
    - 4.2.1 View capacity information about a cluster
    - 4.2.2 View monitoring data of a cluster
  - 4.3 Configure QoS policies
  - 4.4 Configure the data compression feature
- 5 Node O&M
  - 5.1 Node O&M overview
  - 5.2 View monitoring data of a node
  - 5.3 Repair nodes
- 6 Manage file systems
  - 6.1 Manage QoS
  - 6.2 Manage QoS policies
- 7 Events and alerts
  - 7.1 Manage system alerts
  - 7.2 Manage system events
- 8 Cloud platform monitoring
- 9 Log center
- 10 Manage storage capacity

to the Apsara Uni-manager Oper ations Console

## 1 Log in to the Apsara Uni-manager Operations Console

**manager Operations Console**

This topic describes how to log in to the Apsara Uni-manager Operations Console as a user such as an O&M engineer. overview

## 2 O&M overview

Apsara Stack Elastic File Storage-File Storage NAS (EFS-NAS) is a file storage service for compute nodes, such as Elastic Compute Service (ECS) instances, Elastic High Performance Computing (E-HPC) clusters, and Container Service for Kubernetes (ACK) clusters. EFS-NAS is a distributed file system that provides the following benefits: shared access, scalability, high reliability, and high performance. You can efficiently manage EFS-NAS resources such as clusters, nodes, and file systems by using standardized processes and visualized O&M tools to ensure business continuity and high availability.

**O&M architecture**

The following figure shows the O&M architecture of EFS-NAS. On-site TAM and SRE Team Unified Monitoring and Alerting Module of EFS- NAS

**EFS-NAS Node**

**EFS-NAS Node**

**EFS-NAS Node**

Local Local Local Monitoring Module Monitoring Module Monitoring Module

**Features**

| Feature | Description |
|---|---|
| Cluster O&M | The cluster O&M feature allows you to manage EFS-NAS clusters in a graphical user interface (GUI). You can view basic information about clusters in real time, search for clusters, view the capacity information and monitoring data of clusters, configure quality of service (QoS) policies for clusters, and configure the data compression feature for clusters. |
| Node O&M | The node O&M feature allows you to view information about nodes in an EFS-NAS cluster, search for nodes, and view monitoring data of nodes. You can also repair nodes by using the shutdown and repair feature of Apsara Infrastructure Management. |
| File system management | The file system management feature allows you to view and manage EFS- NAS file systems in a centralized manner. For example, you can view the details of a file system, search for file systems, view the shared addresses of a file system, and manage QoS policies. |

overview

| Events and alerts | Alerts related to EFS-NAS are reported to the monitoring and alerting center of the Apsara Uni-manager Operations Console. After alerts are triggered in the system, you can view the alerts and the details of each alert. We recommend that you handle alerts at the earliest opportunity. You can disable the event alerts feature based on your business requirements. To enhance risk monitoring and accelerate emergency response, EFS-NAS allows you to manage events in the Event Center of the Apsara Uni- manager Operations Console. You can search for and handle EFS-NAS- related events at different levels in a centralized manner. |
|---|---|
| Log center | The run logs of EFS-NAS are reported to the log center of the Apsara Uni- manager Operations Console. If a system error occurs, you can quickly identify the issue in the run log. |
| Storage capacity | The storage capacity information of all EFS-NAS clusters is integrated into the Storage Capacity module of the Apsara Uni-manager Operations Console. You can view the capacity usage of all EFS-NAS clusters in a unified data view. This way, you can identify resource bottlenecks in a timely manner and make proper scaling plans to improve resource utilization and O&M efficiency. In addition, you can configure alert rules for EFS-NAS clusters based on their capacity usage. When the capacity usage of a cluster exceeds the specified threshold, the system automatically triggers an alert to help you quickly locate the cluster with abnormal capacity usage. |

**Usage notes**

Take note of the following items when you perform O&M operations on EFS-NAS:
**Ensure data compliance**: To collect and transmit data of users, EFS-NAS must be
explicitly authorized by users. EFS-NAS follows the principle of data minimization while collecting data. It collects only necessary O&M data, such as logs, performance metrics, and error information. Sensitive data must be masked or encrypted for transmission.
**Manage O&M account permissions**: You must follow the principle of least privilege and
grant accounts only necessary permissions on the required O&M modules. Regularly audit the allocation of permissions and revoke or update account permissions.
**Perform high-risk operations with caution**: You must contact Apsara Stack technical
support to assess the impact of high-risk operations such as changing configurations, starting or stopping services, scaling, and repairing machines. You must perform these operations in the agreed maintenance window and inform customers of the possible impact scope in advance.
**Comply with security specifications of customers** : You must follow customer
information security policies, audit requirements, and data confidentiality agreements to ensure that O&M operations are compliant and controllable.

**How to obtain help**

To obtain help during system maintenance, you can contact Apsara Stack technical support. gure permissions

## 3 Configure permissions

By default, the system administrator has full permissions on Elastic File Storage-File Storage NAS (EFS-NAS). To meet the requirements for fine-grained permission control in multi-user scenarios, EFS-NAS provides two predefined O&M roles. The predefined roles allow you to control permissions of regular users in a fine-grained manner. You can assign the predefined roles to regular users to authorize the regular users to access only specific features or perform specific operations. This improves system security and O&M compliance.

**O&M roles provided by EFS-NAS**

A role is a collection of access permissions. You can assign different roles to different users when you create users. This way, you can control access to the system. The following table describes the permissions of O&M roles provided by EFS-NAS.

| Role | Permission |
|---|---|
| EFS-NAS O&M supervisor | Read-only permissions on the EFS-NAS operations console. In most cases, this role is assigned to O&M engineers to monitor the status of EFS-NAS. |
| EFS-NAS O&M administrator | Read and write permissions on the EFS-NAS operations console. |

**Add a user and grant permissions to the user**

1. Log in to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, click **User Authorities**.
3. In the left-side navigation pane, click **User Management**.
4. On the **Users** tab of the **Users** page, click **Add**.
5. In the **Add User** dialog box, configure the parameters and click **OK**. The following table
describes the parameters.

| Parameter | Description |
|---|---|
| Username | The name of the user. The name can be up to 48 characters in length and can contain digits, letters, underscores ( ), hyphens (-), and periods (.). The email _ format is supported. Consecutive underscores are not supported. |
| Password | The password of the user. The password must be 10 to 20 characters in length and must contain lowercase letters, uppercase letters, digits, and special characters. |
| Confirm Password | The same password that you enter to confirm the password. |
| Display Name | The display name of the user. |

gure permissions

| Logon Policy | The policy used when you log in with the user. |
|---|---|
| Role | The role that the user assumes. Example: EFS-NAS O&M supervisor. |
| Department | The department to which the user belongs. |
| Mobile Phone | The mobile number of the user. |
| Email Address | The email address of the user. |
| Allowed to Create AccessKey ID | Specifies whether to allow the user to create AccessKey pairs. By default, the user is not allowed to create AccessKey pairs. |

**What to do next**

Log in to the Apsara Uni-manager Operations Console with the user and perform O&M operations in the EFS-NAS operations console. r O&M

## 4 Cluster O&M

### 4.1 Cluster O&M overview

You can use the cluster O&M feature to manage Elastic File Storage-File Storage NAS (EFS- NAS) clusters in a visualized manner. You can view the basic information, capacity usage, and monitoring data of the clusters in real time. You can also configure quality of service (QoS) policies for disks at the cache layer and data layer to ensure sufficient bandwidth for core services. In addition, you can enable the data compression feature for clusters to optimize storage efficiency and improve cluster observability and O&M efficiency.
1. Log in to the EFS-NAS operations console.
ii. In the top navigation bar, choose **Product Operation > Storage > EFS-NAS**
2. In the left-side navigation pane, choose EFS-NAS Operations Console > **Cluster**
**Operations**.
3. On the **Cluster Operations** page, manage EFS-NAS clusters.

| Operation | Description |
|---|---|
| View the basic information about a cluster | View the information about a cluster, including the cluster name, storage medium, cluster status, and capacity usage. |
| Search for a cluster | Search for a cluster by cluster name or storage medium. You can click Advanced Filter to specify multiple conditions to exactly search for a cluster. |
| View the details of a cluster | Find the cluster that you want to manage and click its name. On the Cluster Details page, view the basic information, capacity usage, and monitoring data of the cluster. View the basic information about the cluster, including the cluster name, storage medium, region, zone, and number of physical nodes. View the capacity information of the cluster, including the physical capacity, physical capacity usage trends, logical capacity, and logical capacity usage trends. View the monitoring data of the cluster, including IOPS, bandwidth, and latency. |
| Configure QoS policies | Configure QoS policies for disks at the cache layer and data layer in a cluster to control the restoration bandwidth when disk or node failures occur. |

r O&M

| Configure the data compression feature | By default, the data compression feature is enabled for clusters. You can modify the data compression configurations based on your business requirements. After the data compression feature is enabled for a cluster, the system uses the LZ4 algorithm to compress the data written to the cluster. This effectively reduces the used physical storage space and storage costs. |
|---|---|

### 4.2 View cluster details

#### 4.2.1 View capacity information about a cluster

**cluster**

You can view the physical capacity, physical capacity usage trends, logical capacity, and logical capacity usage trends of an Elastic File Storage-File Storage NAS (EFS-NAS) cluster. This way, you can scale the cluster based on the capacity usage.
1. Log in to the EFS-NAS operations console.
ii. In the top navigation bar, choose **Product Operation > Storage > EFS-NAS**
2. In the left-side navigation pane, choose EFS-NAS Operations Console > **Cluster**
**Operations**.
3. On the **Cluster Operations** page, find the cluster that you want to manage and click its
name to go to the Cluster Details page.
4. On the **Capacity** tab, view the capacity information about the cluster.

| Section | Description |
|---|---|
| Logical Capacity | You can view the used logical capacity, total logical capacity, and percentage of used logical capacity of the cluster. Total Capacity: the maximum amount of data that you can write to the cluster. Used: the amount of data that has been written to the cluster. |
| Physical Capacity | You can view the used physical capacity, total physical capacity, and percentage of used physical capacity of the cluster. Total Capacity: the total disk storage capacity that are available to the Object Storage Daemon (OSD) instances in the cluster. Used: the physical disk storage capacity occupied by data such as replicas, metadata, and logs. |
| Physical Capacity Trend | You can specify a time range to view the total physical capacity and physical capacity usage trend. |

r O&M

| Logical Capacity Trend | You can specify a time range to view the total logical capacity and logical capacity usage trend. |
|---|---|

#### 4.2.2 View monitoring data of a cluster

You can view the IOPS, bandwidth, and latency metrics of an Elastic File Storage-File Storage

| NAS (EFS-NAS) cluster. | This helps you understand the cluster status, identify performance |   |
|---|---|---|
| issues, and optimize cluster performance. |   |   |

1. Log in to the EFS-NAS operations console.
ii. In the top navigation bar, choose **Product Operation > Storage > EFS-NAS**
2. In the left-side navigation pane, choose EFS-NAS Operations Console > **Cluster**
**Operations**.
3. On the **Cluster Operations** page, find the cluster that you want to manage and click its
name.
4. On the Cluster Details page, click the **Monitoring** tab. On the Monitoring tab, specify a
time range to view the monitoring data of the cluster.

| You can view the monitoring data within the last 15 minutes, 30 minutes, 1 hour, 3 hours, |   |   |
|---|---|---|
| and 1 day. You can select different time ranges to help you analyze performance trends of |   |   |
| the cluster in different periods. |   |   |

**Metrics**

| Metric | Description |
|---|---|
| IOPS | The total number of read and write operations performed on the cluster per second. This metric is used to evaluate the storage system capability of processing concurrent requests. Read IOPS: the total number of read operations performed on the cluster per second. Write IOPS: the total number of write operations performed on the cluster per second. If the IOPS suddenly drops, a storage performance issue or a network exception may occur. Troubleshoot the issue at the earliest opportunity. |
| Bandwidth | The total bandwidth used when data is read from and written to the cluster. Unit: KiB/s. Read Bandwidth: the total bandwidth used when data is read from the cluster. Write Bandwidth: the total bandwidth used when data is written to the cluster. If the bandwidth usage is close to the upper limit, the data transmission speed may be affected. In this case, we recommend that you increase the bandwidth. |

r O&M

| Delay | The average read/write latency of the cluster. This metric is used to evaluate the response speed of the cluster. Unit: microseconds. Read Latency: the average response time of read operations. Write Latency: the average response time of write operations. If the latency suddenly increases, a storage or network exception may occur. Pay special attention to such a case. |
|---|---|

### 4.3 Configure QoS policies

You can configure quality of service (QoS) policies for disks at the cache layer and data layer in a cluster to control the restoration bandwidth when disk or node failures occur. This prevents an impact on the service performance during the restoration process.

**Background information**

Elastic File Storage-File Storage NAS (EFS-NAS) uses a tiered storage architecture:
**Cache layer**: Based on high-performance SSDs, the cache layer caches hot data to
significantly accelerate access and ensures data security based on the multi-replica mechanism.
**Data layer**: The data layer provides highly reliable persistent storage and ensures data
security by using the erasure coding (EC) 4+2 mechanism. If a storage node or disk fails, the system automatically triggers data restoration and dynamically controls the restoration bandwidth based on the QoS policies. This ensures data reliability and balances the restoration speed and service performance.
1. Log in to the EFS-NAS operations console.
ii. In the top navigation bar, choose **Product Operation > Storage > EFS-NAS**
2. In the left-side navigation pane, choose EFS-NAS Operations Console > **Cluster**
**Operations**.
3. On the **Cluster Operations** page, find the cluster that you want to manage and click
**Configure QoS** in the **Operation** column.
4. In the **Configure QoS** panel, configure the parameters. The following table describes the
parameters.

| Parameter | Description |
|---|---|
| Storage Layer | The storage layer for which you want to configure the QoS policy. You can configure a QoS policy for the cache layer and data layer. Valid values: Cache Layer: controls the restoration bandwidth at the cache layer. Data Layer: controls the restoration bandwidth at the data layer. |

r O&M

| Type | The type of the QoS policy. The type of the last configured policy is used. Valid values: Static QoS: specifies a fixed maximum restoration bandwidth. This type of QoS policy is suitable for scenarios in which the system load is stable. Dynamic QoS: dynamically adjusts the restoration bandwidth based on the system load. This type of QoS policy accelerates data restoration while ensuring service performance. |
|---|---|
| Recovery Speed | The speed at which data is restored. This parameter is available only if you set the Type parameter to Static QoS. Set the maximum restoration bandwidth for each disk based on your business load and required restoration efficiency .Valid values: Slow Recovery (Single Disk Recovery Bandwidth: 10MiB/s): preferentially ensures the performance of online services. However, the data restoration process may take a long period of time to complete. During this period, if hardware failures occur, the data security level may be affected. Medium-Speed Recovery (Single Disk Recovery Bandwidth: 15MiB/s): balances the service performance and restoration bandwidth. The restoration duration is medium. When the system I/O is close to saturation, the service I/O latency may be increased. High-Speed Recovery (Single Disk Recovery Bandwidth: 30MiB/s): preferentially ensures the restoration speed. However, a large amount of storage bandwidth is occupied, which may affect the performance of high-load services. You can select this option only when you need to scale out the cluster for rebalancing. |
| Minimum Recovery Bandwidth For a Single Disk | These parameters are available only if you set the Type parameter toD ynamic QoS. Set a range within which the system can adjust the restoration bandwidth. Minimum Recovery Bandwidth For a Single Disk: the minimum required restoration speed. Maximum Recovery Bandwidth For a Single Disk: the maximum restoration speed, which prevents the data restoration process from occupying excessive resources. The maximum restoration speed must be greater than the minimum restoration bandwidth for a single disk. Client Bandwidth Threshold: the threshold for the client bandwidth. If the client bandwidth is smaller than the specified value, the system automatically increases the restoration bandwidth. |
| Maximum Recovery Bandwidth For a Single Disk |   |
| Client Bandwidth Threshold |   |

| Minimum Recovery Bandwidth For a Single Disk: | the minimum required |
|---|---|
| restoration speed. |   |

| Maximum Recovery Bandwidth For a Single Disk | : the maximum |
|---|---|
| restoration speed, which prevents the data restoration process from occupying |   |
| excessive resources. The maximum restoration speed |   |

| Client Bandwidth Threshold | : the threshold for the client bandwidth. If the |
|---|---|
| client bandwidth is smaller than the specified value, the system automatically |   |
| increases the restoration bandwidth. |   |

5. Click **OK**.

| After the QoS policy is configured, it immediately takes effect and applies to all disks in the |   |
|---|---|
| cluster storage pool. |   |

**Configuration suggestions**

r O&M

| During peak hours | , we recommend that you configure a static QoS policy with a slow |
|---|---|
| restoration speed. Alternatively, you can configure a dynamic QoS policy and set the |   |
| maximum restoration bandwidth to a smaller value. |   |

| During off-peak hours | , you can configure a static QoS policy with a high restoration |
|---|---|
| speed to accelerate data restoration. This minimizes the restoration duration and prevents |   |
| risks. |   |

| In hybrid load scenarios | , we recommend that you configure a dynamic QoS policy. The |
|---|---|
| system automatically adjusts the restoration speed based on the real-time load. |   |

### 4.4 Configure the data compression feature

**compression feature**

Elastic File Storage-File Storage NAS (EFS-NAS) clusters support the data compression feature. By default, this feature is enabled for all clusters. After the data compression feature is enabled for a cluster, the system uses the LZ4 algorithm to compress the data written to the cluster. This effectively reduces the used physical storage space and storage costs.

**Usage notes**

The data compression feature may slightly affect the write performance, but it can significantly save storage space. If you change data compression configurations, data stored in the cluster before the change will not be affected. The changed data compression configurations apply only to data written to the cluster after the change. After the data compression feature is disabled for a cluster, data written to the cluster is no longer compressed.
1. Log in to the EFS-NAS operations console.
ii. In the top navigation bar, choose **Product Operation > Storage > EFS-NAS**
2. In the left-side navigation pane, choose EFS-NAS Operations Console > **Cluster**
**Operations**.
3. On the **Cluster Operations** page, find the cluster that you want to manage and click **Set**
**Data Compression** in the **Operation** column.
4. In the **Set Data Compression** panel, turn on or off **Data Compression** based on your
business requirements. Set the Compression Algorithm parameter to lz4. The data written to the cluster will be compressed and decompressed based on the LZ4 algorithm.
5. Click **OK**.
O&M

## 5 Node O&M

### 5.1 Node O&M overview

The node O&M feature allows you to view information about nodes in an Elastic File Storage- File Storage NAS (EFS-NAS) cluster, search for nodes, and view node details.
1. Log in to the EFS-NAS operations console.
ii. In the top navigation bar, choose **Product Operation > Storage > EFS-NAS**
2. In the left-side navigation pane, choose EFS-NAS Operations Console > **Node Operations**.
3. On the **Node Operations** page, manage nodes in an EFS-NAS cluster.

| Operation | Description |
|---|---|
| View information about a node | View the node name, node status, cluster to which the node belongs, and IP address. |
| Search for a node | Search for the required node by node name, IP address, or cluster to which the node belongs. You can click Advanced Filter to specify multiple conditions to exactly search for nodes. |
| View the details of a node | Find the node that you want to view and click its name or clickD etails in the Operation column. On the node details page, view the basic information and monitoring data of the node. View the basic information about the node, including the node name, node status, node type, cluster to which the node belongs, and creation time. View monitoring data of the node, such as the CPU utilization, memory usage, and network bandwidth. |

**What to do next**

Repair nodes by using the shutdown and repair feature of Apsara Infrastructure Management.

### 5.2 View monitoring data of a node

**node**

You can view the CPU utilization, memory usage, network bandwidth, packet, packet loss rate, error packet rate, and Object Storage Daemon (OSD) information of nodes. This helps you understand the node status, identify performance issues, and optimize node performance. O&M
1. Log in to the Elastic File Storage-File Storage NAS (EFS-NAS) operations console.
ii. In the top navigation bar, choose **Product Operation > Storage > EFS-NAS**
2. In the left-side navigation pane, choose EFS-NAS Operations Console > **Node Operations**.
3. On the **Node Operations** page, find the node that you want to manage and click its name
or click **Details** in the **Operation** column.
4. On the node details page, view the monitoring data of the node.

| You can view the monitoring data of the node within the last 15 minutes, 30 minutes, 1 |   |
|---|---|
| hour, 3 hours, and 1 day. You can select an appropriate time range to help you analyze |   |
| performance trends of the node in different periods. |   |

**Monitoring metrics**

| Metric | Description |
|---|---|
| CPU Usage | The CPU utilization of a node, in percent. In normal cases, the CPU utilization is lower than 80%. If the CPU utilization is greater than 90% for a long period of time, the system performance may be affected. |
| Memory Usage | The memory usage of a node, in percent. In normal cases, the memory usage is lower than 85%. If the memory usage is greater than 95% for a long period of time, the system may become unstable. |
| Network Bandwidth | The network bandwidth that is used when a node sends and receives data. The Network Bandwidth metric includes the Network Transmission Bandwidth and Network Receiving Bandwidth sub-metrics. This metric is used to evaluate the node capability of sending and receiving data within a period of time and the actual bandwidth usage. |
| Packet | The number of packets sent and received by a node per second. This metric is used to evaluate the activity level of the network. The Packet metric includes the Number of Packets Sent per Second and Accepted Packets per Second sub- metrics. |
| Packet Loss Rate | The percentage of packets that are lost when a node sends and receives packets. This metric reflects the reliability of network transmission and includes the Packet Loss Rate at the Sender and Packet Loss Rate at the Receiver sub- metrics. In normal cases, both the packet loss rate at the sender and the packet loss rate at the receiver are less than 0.1%. If the sub-metrics are abnormal for a long period of time, exceptions, such as network congestion, link failure, or insufficient network interface controller (NIC) resources, may occur. |
| Wrong Packet Rate | The percentage of error packets sent and received by a node.T his metric reflects the network communication quality of the node. This metric includes the Sending Packet Error Rate and Packet Error Rate at the Receiving End sub- metrics and is used to diagnose the network link, NIC, or driver exceptions. |

O&M

| OSD Information | The status, configurations, and resource usage of the OSD instances on a storage node. Each OSD instance corresponds to a physical disk in most cases. The following key metrics are included: Name: the unique identifier of an OSD instance. Status: the status of an OSD instance. The OSD instance is in the Health state when it is running as expected. Type: the storage media. Valid values: SSD and HDD. Capacity: the total storage capacity and used capacity. Proportion of Healthy Data: the proportion of accessible data with complete data replicas, in percent. Percentage of Degraded Data: the proportion of accessible data with insufficient data replicas, in percent. Proportion of Data Recovered: the proportion of data that is being repaired or restored, in percent. Proportion of Unavailable Data: the proportion of data that is temporarily inaccessible, in percent. If a large number of OSD instances on a node become unhealthy, disk failures, network interruptions, or host downtime may occur. Handle the exceptions at the earliest opportunity to prevent data loss. |
|---|---|

### 5.3 Repair nodes

The shutdown and repair feature allows you to shut down a running node and perform repair operations on the node, excluding hard disk repair.

**Scenarios**

This feature is applicable to scenarios in which you need to shut down and repair a running and accessible node but do not require hard disk repair.

**Important**

If a node is inaccessible or requires hard disk repair, contact Apsara Stack technical support.

**Usage notes**

**Warning**

When you repair a machine, strictly follow the hardware maintenance specifications and procedures. Do not disassemble the machine or perform operations on the machine while it is energized, which may cause more faults or personal injury. In each cluster, only one machine can be repaired at a time. Do not shut down the machine for repair until the **IDC Operation** step. After you shut down a machine for repair, if the machine is disconnected for more than 180 minutes, the Elastic File Storage-File Storage NAS (EFS-NAS) cluster restores the data of the node to another node. We recommend that you minimize the shutdown time of your machine. O&M

**Prerequisites**

The node name and IP address of the machine to be repaired are obtained on the Node Operations page of the EFS-NAS console. Other nodes are healthy.

**Important**

If another node has exceptions or alerts, fix them before you perform the repair. The preparations for machine repair are completed to minimize the machine shutdown time.
1. Log in to the Apsara Uni-manager Operations Console.
ii. In the top navigation bar, choose **Platform Operation > Resource Management**.
2. Start a shutdown and repair task.
i. In the left-side navigation pane, choose **Resource Management > Machines**. ii. On the Machines page, find the machine that you want to manage and click **Details** in the **Actions** column. iii. In the upper-right corner of the machine details page, click **Machine Management** and select **Power Off and Repair** from the drop-down list. iv. In the **Confirmation** dialog box, confirm that the machine information is correct, enter the reason for this operation, and then click **OK**.
3. On the Machine maintenance page, perform repair operations.
After you start a repair task, the system follows the workflow and runs the task. The following table describes the repair steps. Step 4 requires manual operations. Other steps are automatically completed by the system.

**Important**

If a step fails, handle the exception and retry the step.

| No. | Step | Execution method | Description |
|---|---|---|---|
| 1 | Precheck | Automatically completed by the system | Check whether the machine is on the blacklist. |
| 2 | Pre- processin g | Automatically completed by the system | Back up machine metadata and configuration data to Object Storage Service (OSS). |

O&M

| 3 | Tianji Approval | Automatically completed by the system (manual review required in some scenarios) | Approve the node to be disconnected. Pay attention to the approval progress to ensure that all machine components are approved. If the approval of a component remains in the pending state, click Approval in the Operation column to approve the component. |
|---|---|---|---|
| 4 | IDC Operation | After you complete manual operations, click Complete the operation. | Perform repair operations on the machine in the data center and reconnect the node. |
| 5 | Service Online | Automatically completed by the system | Check the status of the node, including whether the machine is started and whether the machine is running as expected. |

**Verify results**

After the node is repaired, check the status of the node on the **Node Operations** page in the EFS-NAS console. When the node status changes from Offline to Health, the node is running as expected. ge file systems

## 6 Manage file systems

The file system management feature allows you to view and manage Elastic File Storage-File Storage NAS (EFS-NAS) file systems in a centralized manner. For example, you can view the details of a file system, search for file systems, view the shared addresses of a file system, and manage quality of service (QoS).

**Prerequisites**

An EFS-NAS cluster is created in the Apsara Uni-manager Management Console.
1. Log in to the EFS-NAS operations console.
ii. In the top navigation bar, choose **Product Operation > Storage > EFS-NAS**
2. In the left-side navigation pane, choose EFS-NAS Operations Console > **File System**
**Management**.
3. On the **File System Management** page, perform operations based on your business
requirements.

| Operation | Description |
|---|---|
| View information about a file system | You can view information about a file system, such as Instance ID/Instance Name, Cluster, Shared Protocol, Share Status, Account ID, Directory Path, and Health Status. |
| Search for a file system | You can search for a file system by Cluster, Instance ID, Instance Name, Health Status, Account ID, Creation Time, or their combinations. You can click Advanced Filter to specify multiple conditions to exactly search for a file system. |
| View the shared addresses of a file system | Find the shared file system that you want to manage and clickV iew Shared Addresses in the Operation column. |
| Manage QoS | To prevent file systems from consuming excessive system resources, you can configure QoS policies to limit the maximum read/write bandwidth and maximum operations per second (OPS) of file systems. |

### 6.1 Manage QoS

To prevent file systems from consuming excessive system resources, you can configure quality of service (QoS) policies to limit the maximum read/write bandwidth and maximum operations per second (OPS) of file systems. After QoS is configured for a file system, you can modify or delete the QoS configuration based on your business requirements.

**Prerequisites**

A QoS policy is created for a cluster. For more information, see Create a QoS policy. ge file systems

**Configure QoS**

1. Log in to the Elastic File Storage-File Storage NAS (EFS-NAS) operations console.
ii. In the top navigation bar, choose **Product Operation > Storage > EFS-NAS**
2. In the left-side navigation pane, click **File System Management**.
3. On the **File System Management** page, find the file system that you want to manage and
click **Configure QoS** in the **Operation** column.
4. In the **Configure QoS** panel, select a QoS policy.
5. Click **OK**.

**Modify QoS**

1. On the **File System Management** page, find the file system that you want to manage and
click **Modify QoS** in the **Operation** column.
2. In the **Configure QoS** panel, select a QoS policy.
3. Click **OK**.

**Delete QoS configuration**

**Important**

Deleted QoS configuration cannot be recovered. Proceed with caution. If you delete a QoS configuration, only the association between the QoS policy and the file system is removed, and the QoS policy itself is not deleted.
1. On the **File System Management** page, find the file system that you want to manage and
click **Delete QoS configuration** in the **Operation** column.
2. In the message that appears, click **OK**.

### 6.2 Manage QoS policies

In Elastic File Storage-File Storage NAS (EFS-NAS), the system comprehensively evaluates the maximum available bandwidth and maximum operations per second (OPS) of clusters in different scenarios based on the business workload, storage medium, I/O mode, and network bandwidth. You can limit the maximum available bandwidth and maximum OPS of clusters by configuring quality of service (QoS) policies for file systems. After a QoS policy is created, you can use the QoS policy as the QoS configuration of a file system, and modify or delete the QoS policy based on your business requirements.

**Background information**

You can configure the **Maximum Bandwidth** and **Maximum OPS** parameters for a QoS policy to limit the access of all clients to a specified file system. This way, resources are isolated and QoS is ensured. Bandwidth: the amount of data that a file system can transfer per unit of time. You can specify the maximum bandwidth to limit the total read and write throughput of the file system. This prevents high-throughput applications, such as AI training, big data analysis, and video rendering, from consuming too much network and storage bandwidth and affecting the performance of other businesses. This is suitable for high-throughput scenarios such as sequential read and write operations on large files and batch data processing. ge file systems OPS: the number of I/O operations that can be processed by the storage system per second. I/O operations include reading or writing files, creating or deleting files, and reading or modifying file metadata. You can specify the maximum OPS to limit the total I/O operations that clients can perform on the file system per unit of time. This is suitable for random-access-intensive services, such as databases, VM storage, small file services, and log systems. When the total access to a file system reaches the specified maximum bandwidth or maximum OPS threshold, the system throttles the excess traffic. Subsequent requests are delayed or queued to ensure that the overall load remains within limits and that critical services continue to run stably.

**Usage notes**

You can create a maximum of 128 QoS policies for a single cluster.

**Create a QoS policy**

1. Log in to the Elastic File Storage-File Storage NAS (EFS-NAS) operations console.
ii. In the top navigation bar, choose **Product Operation > Storage > EFS-NAS**
2. In the left-side navigation pane, click **Strategy Management**.
3. On the **Strategy Management** page, click **Create a policy**.
4. In the **Configure QoS** panel, configure the parameters. The following table describes the
parameters.

| Parameter | Description |
|---|---|
| Name | The name of the QoS policy, which is used to identify the QoS policy. |
| Description | The description of the QoS policy. |
| Cluster | The cluster associated with the QoS policy. Only file systems within the cluster can use the QoS policy you create. |
| Maximum Bandwidth | Limits the total read and write throughput of the file system. Valid values: Read: the maximum bandwidth for read operations. Write: the maximum bandwidth for write operations. Total: the maximum bandwidth for read and write operations. Important The total bandwidth must be greater than or equal to the read bandwidth or write bandwidth. Unit: MiB/s or GiB/s. |

ge file systems

| Maximum OPS | Limits the total I/O operations that clients can perform on the file system per unit of time. Valid values: Read: the maximum number of read operations. Write: the maximum number of write operations. Total: the maximum number of read and write operations. Important The total OPS must be greater than or equal to the read OPS or write OPS. Unit: Thousand/s or Ten Thousands/s. |
|---|---|

5. Click **OK**.

**Modify a QoS policy**

1. On the **Strategy Management** page, find the QoS policy that you want to modify and click
**Modify** in the **Operation** column.
2. In the **Configure QoS** panel, modify the Name, Maximum Bandwidth, and Maximum OPS
parameters based on your business requirements.

**Note**

After the name of a QoS policy is modified, the system automatically updates references to this name in all associated file system configurations to ensure name consistency.
3. Click **OK**.

**Delete a QoS policy**

**Important**

If you delete a QoS policy, the QoS configurations of all associated file systems become invalid. Evaluate the potential impact on your business before you delete the QoS policy. A deleted QoS policy cannot be recovered. Proceed with caution.
1. On the **Strategy Management** page, find the QoS policy that you want to delete and click
**Delete** in the **Operation** column.
2. In the message that appears, click **OK**.

**What to do next**

Configure QoS policies for file systems. For more information, see Configure QoS policies. s and alerts

## 7 Events and alerts

### 7.1 Manage system alerts

Alerts related to Elastic File Storage-File Storage NAS (EFS-NAS) are reported to the monitoring and alerting center of the Apsara Uni-manager Operations Console. After alerts are triggered in the system, you can view the alerts and the details of each alert. We recommend that you handle alerts at the earliest opportunity. You can close alerts based on your business requirements.
1. Log in to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Monitor&Alert** > **Alert Management** > **Alert List**.

**Note**

On the Alert List page, you can click **Handle Now** above the alert list to go to the
**Events** page. The Event Center aggregates and displays all alert data and provides
response levels for organizations to deliver emergency response and improve O&M efficiency.
3. On the **Alert List** page, select efs-nas from the **Resource Owner** drop-down list.
The system automatically displays the alerts related to EFS-NAS. You can view the information about alerts in the columns, including **Alert Level**, **Alert Item ID**, **Resource**
**Owner**, **Alert Information**, **Alert Status**, **Alert Start Time**, **Last Alert Time/Duration**,
and **Alerts**.

**Note**

By default, the list of alerts that are not closed is displayed. You can click the
**Disabled** tab to view the list of alerts that are closed.
On the **Not Disabled** tab, the system does not display closed alerts by default. However, you can click **Advanced Filter** and configure the Alert Status parameter to filter and view the closed alerts. Similarly, on the **Disabled** tab, the system does not display the alerts that are not closed by default. You can click
**Advanced Filter** and configure the Alert Status parameter to filter and view the
alerts that are not closed. You can click the up or down arrow next to **Alert Level** or **Last Alert**
**Time/Duration** to sort alerts.
You can select a value from the **Resource Owner** drop-down list or enter a keyword in the search box on the Alert List page to search for alerts. You can also click **Advanced Filter** and configure the **Alert Item ID**, , **Alert Start**
**Time**, **Alert Level**, **Alert Status**, **Alert Source**, **Object Type**, **Alert Object**
**Name**, and **Alert Attributes** parameters to search for alerts. You can set the
**Alert Level**, **Alert Status**, and **Alert Source** parameters to multiple values.
Find the alert that you want to manage and click the value in the **Alert Item ID** column to view the details of the alert.
4. **Close an alert based on your business requirements** : After an alert is handled and no
issue is identified or the alert does not need to be handled, you can click **Close** in the
**Actions** column of the alert. The system changes the state of the alert to **Disabled**, which
indicates that the alert has been handled. s and alerts After the state of the alert changes to Disabled, the alert is displayed on the **Disabled** tab. To close multiple alerts at a time, select the alerts on which you want to close and click
**Batch Close** in the lower-left corner of the page.
5. **Export report based on your business requirements** : In the upper-left corner of the
Alert List page, click **Export Report** to export alert data as an XLSX file to your computer.

### 7.2 Manage system events

To enhance risk monitoring and accelerate emergency response, Elastic File Storage-File Storage NAS (EFS-NAS) allows you to manage events in the Event Center of the Apsara Unimanager Operations Console. You can search for and handle EFS-NAS-related events at different levels in a centralized manner.

**Event levels**

L1: major events. When a major event occurs, the overall features of a cloud service are unavailable, and a wide range of related hardware and software resources, cloud service instances that are provided, and dependent service instances are abnormal. L2: significant events. When a significant event occurs, the overall features of a cloud service are abnormal, and the overall features of a worker server role cluster are abnormal, or some dependent service instances are abnormal. L3: routine events. When a routine event occurs, exceptions occur in a single cloud service instance, work software instance, work resource node, or management software instance. Handle the routine event at the earliest opportunity. L4: exceptions. When an exception occurs, no fault is caused but the exception needs to be handled. L5: information, which indicates other events that require attention.
1. Log in to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Monitor&Alert** > **Event Center** > **Events**.
On the Events page, events at the L1, L2, L3, L4, or L5 level and in the **Pending Response** or **Processing** state are displayed by default.
3. Click **Advanced Filter**, select efs-nas from the **Project** drop-down list, and then click
**Search**.
The system displays EFS-NAS-related events.

**Note**

You can also click Advanced Filter and filter the events by specifying the following conditions: **Event ID**, **Event Name**, **Event Description**, **Start Time**, **Recovery Time**,
**Object Type**, **Project**, **Alert item ID**, **Event Object**, **Event Type**, and **Cluster**.
4. Find the event that you want to manage and click its name to view the event details and
perform operations, such as marking the event and responding to the event, based on your business requirements. In the upper-right corner of the event details page, click the icon to copy the URL of the event details page. s and alerts In the upper-right corner of the event details page, click **Mark** to mark the event. In the Classification mark dialog box, configure the parameters such as Valid and Cause of the Event, and click **Confirm**. In the upper-right corner of the event details page, click **Response** to respond to or close the event. To respond to the event, click Response and select **Response Event**. Then, the state of the event changes to **Processing**.

**Note**

After you respond to an event, you can click **Transfer** or **Close** on the event details page to transfer or close the event. To close the event, click Response and select **Direct statement**. In the Event statement dialog box, configure the parameters such as Valid and Cause of the Event and click **Confirm**. Then, the state of the event changes to **Closed**. After the event is closed, all event-related alerts will be closed. platform monitoring

## 8 Cloud platform monitoring

The cloud platform monitoring feature enables you to understand the running status of Elastic File Storage-File Storage NAS (EFS-NAS) clusters, services, and components. This way, you can identify and troubleshoot issues at the earliest opportunity.
1. Log in to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Monitor&Alert > Monitor Management > Tianjimon**.
3. In the left-side navigation pane, choose Cloud Product Business Monitoring > Cloud Product
Monitoring. On the **Product Monitoring** page, find the **efs-nas** product and click the product name.
4. On the **Cloud Product: efs-nas** page, click the cluster that you want to view, and view its
monitoring data on the right side.

**Note**

To view the monitoring data of abnormal clusters, select the **Show Abnormal**
**Only** check box.
Move the pointer over a trend chart to display and view the value at a specific point in time. You can turn on **Auto Refresh** in the upper-right corner to automatically update the monitoring data.
**View the monitoring data of a cluster**: Find the cluster whose monitoring data you
want to view, click the cluster name, and view the status, basic monitoring data, and machines of the cluster on the right side. The following table describes the related operations that you can perform.

| Operation | Description |
|---|---|
| View the basic information of a cluster | You can view the name, status, and zone of the selected cluster. |
| View the basic monitoring data of a cluster | On the Basic Monitoring tab, specify a time range and select metrics based on your business requirements to view the monitoring data of the cluster within the specified time range. The monitoring data includes Load, CPU, Mem, Traffic, TCP, TCP Retransmission, and Disk IOPS. |

platform monitoring

| View machines | On the Machines tab, you can view the basic information and monitoring data of all machines within the cluster. View machine information: View the information about all machines, including hostname and IP address, in the machine list. View the monitoring data of a machine: Find the machine whose monitoring data you want to view and click the icon in the Actions column. On the Machine Monitoring page, specify a time range and select metrics based on your business requirements to view the monitoring data of the machine within the specified time range. The monitoring data includes Load, CPU, Mem, Traffic, TCP, TCP Retransmission, and Disk IOPS. |
|---|---|

**View monitoring data of a service**: Find the service whose monitoring data you want
to view, click the service name, such as tianji, and view the status and business monitoring data of the service on the right side. The following table describes the related operations that you can perform.

| Operation | Description |
|---|---|
| View the basic information of a service | You can view the name, status, and home cluster of the selected service. |
| View business monitoring data | On the Business Monitoring tab, specify a time range and select metrics based on your business requirements to view the monitoring data of a service within the specified time range. Important Some services do not have monitoring data. |

**View monitoring data of a component**: Find the component whose monitoring data
you want to view, click the component name, such as TianjiClient#, and view the status, basic monitoring data, business monitoring data, and machines of the component on the right side. The following table describes the related operations that you can perform.

| Operation | Description |
|---|---|
| View the basic information of a component | You can view the name, associated instance, status, home cluster, and attributable service of the selected component. Click Associated Instance to switch to the component monitoring data of a specific instance. |
| View basic monitoring data | On the Basic Monitoring tab, you can view the basic monitoring data of a component, including the monitoring data of containers, processes, and Java virtual machines (JVMs). |

platform monitoring

| View business monitoring data | On the Business Monitoring tab, you can view the log and Prometheus monitoring data of a component. Important Some components do not have business monitoring data. |
|---|---|
| View machines | On the Machines tab, you can view the basic information and monitoring data of the machine to which the component belongs. View machine information: View the information about all machines, including hostname and IP address, in the machine list. View the monitoring data of a machine: Find the machine whose monitoring data you want to view and click the icon in the Actions column. On the Machine Monitoring page, specify a time range and select metrics based on your business requirements to view the monitoring data of the machine within the specified time range. The monitoring data includes Load, CPU, Mem, Traffic, TCP, TCP Retransmission, and Disk IOPS. |

enter

## 9 Log center

The operational logs of Elastic File Storage-File Storage NAS (EFS-NAS) are reported to the Log Center of the Apsara Uni-manager Operations Console. When the system runs abnormally, you can quickly identify the issue by viewing the operational logs.

**View log maps**

1. Log in to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Platform Operation** > **Log Center** > **Log Query**.
3. In the **Advanced Filter** section of the **Log Map** page, select **efs-nas** from the **Products**
drop-down list, specify conditions such as **Service**, **Log Type**, **Log Name**, and **Status** based on your business requirements, and then click **Search**. The system displays the log configurations of EFS-NAS.
4. You can manage the log configurations based on your business requirements. The following
table describes the operations that you can perform.

| Operation | Description |
|---|---|
| View log details of a product | Find the log whose details you want to view and clickD etails in the Actions column. On the Product log details page, view details in the Log Information, Log Ownership, and Machine Status sections. View log information: In the Log Information section, you can view information about the log, including Log Name, Log Type, Created At, Project, LogStore, Label, and Log Status. Click Document Collection in the upper-right corner to view the file collection configuration for accessing managed collection logs. Click Storage Configuration in the upper-right corner to view the storage configuration for accessing logs, such as the index configuration of Logstore. Note The configuration information is for reference only. To adjust the access configuration, modify the product baseline, or log in to the Apsara Infrastructure Management console to modify the desired- state configuration of a specific cluster. View log ownership: In the Log Ownership section, you can view the ownership information about the log, including Attributable Product, Service Name, Service Role, and Primary Account. View machine status: In the Machine Status section, you can view a list of machines associated with the current log. The displayed information about each machine includes Machine Name, IP Address, and Account Information. You can click Retry in the Operation column of a machine to resend the primary account information, as noted in the Log Ownership section, to the machine. This step is pivotal in verifying and securing the necessary permissions for uninterrupted log collection. |

enter

| View operation records | Find the product log that you want to view and clickO peration Record in the Actions column. In the Operation Record panel, you can view the operation information such as Operation Name, Operation content, Status, Operator, and Operation time. |
|---|---|
| Enable log collection | You can use one of the following methods to enable log collection. After you enable log collection, logs are collected to Simple Log Service (SLS). Enable log collection for a single product log: Find the product log for which you want to enable log collection and click Open acquisition in the Actions column. In the message that appears, click OK. Enable log collection for multiple product logs at a time: Select the product logs for which you want to enable log collection and click Batch open collection below the product log list. In the message that appears, click OK. |
| Disable log collection | You can use one of the methods to disable log collection. Disable log collection for a single product log: Find the product log for which you want to disable log collection and click Close Acquisition in the Actions column. In the message that appears, click OK. Disable log collection for multiple product logs at a time: Select the product logs for which you want to disable log collection and click Batch close collection below the product log list. In the message that appears, click OK. |

**Query run logs**

1. Log in to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Platform Operation** > **Log Center** > **Log Query**.
3. In the left-side navigation pane, click Log Query. On the **Log Query** page, click the
**Platform Logs** tab. On this tab, configure the query conditions. The following table
describes the parameters of query conditions.

|   | Parameter | Description |   |   |
|---|---|---|---|---|
|   | Products | Select efs-nas from the drop-down list. |   |   |
|   | Log Type | Select Run Logs from the drop-down list. |   |   |
|   | Log Name | Select efs-nas-ops-log from the drop-down list. |   |   |
|   | Time Range | Specify the time range in which you want to query run logs. |   |   |
|   | Query Conditions | Enter a keyword to query logs. You can specify a query condition that contains and, or, or not operators. Example: (44 or http) and error not fatal . |   |   |
|   |   |   | (44 or http) and error |   |
|   |   | not fatal |   |   |

4. Click **Search**.
enter You can view the log details that meet the query conditions in the log search result list, and perform operations on the logs. The following table describes the operations that you can perform.

| Operation | Description |
|---|---|
| View log overview | View the information about a log, including Product Name, Service Name, Service Role, Log Name, Logs, and Error Logs. |
| Search for logs | Enter a keyword to query logs. |
| Show exception logs only | Select the Show exception logs only check box to quickly locate exception logs. |
| Export a log list | Click Export List to export logs to your computer in the JSON format. |
| Switch the log display mode | Click List or Aggregation to view logs in a list or aggregation form. |
| View information about a log record | In the log list, view information about a log record, including times, level, pid, and logger. |
| View details of a log record | In the List display mode, find the log record whose details you want to view and click Details in the Operation column to view log details, including times, level, pid, logger, and error. |

ge storage capacity

## 10 Manage storage capacity

The storage capacity information of all EFS-NAS clusters is integrated into the Storage Capacity module of the Apsara Uni-manager Operations Console. You can view the capacity usage of all EFS-NAS clusters in a unified data view. This way, you can identify resource bottlenecks in a timely manner and make proper scaling plans to improve resource utilization and O&M efficiency. In addition, you can configure alert rules for EFS-NAS clusters based on their capacity usage. When the capacity usage of a cluster exceeds the specified threshold, the system automatically triggers an alert to help you quickly locate the cluster with abnormal capacity usage.
1. Log in to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Platform Operation > Capacity > Storage Capacity**.
3. In the left-side navigation pane, choose Storage Capacity > EFS-NAS. On the **EFS-NAS**
page, you can view the cluster overview, capacity allocation rate trend, and capacity details, and configure alert rules based on your business requirements. The following table describes these operations.

| Operation | Description |
|---|---|
| View the capacity overview | In the Capacity Overview section, select a zone to view the used capacity, total capacity, and capacity usage rate of all clusters in the zone. The capacity data of all-flash clusters and hybrid-flash clusters are displayed separately. |
| View the capacity allocation rate trend | In the Capacity Allocation Rate Trend section, select a time range and a cluster to view the capacity allocation rate trend of the cluster. Move the pointer over a trend chart to view the data at a specific point in time, including the date, usage rate, used capacity, and total capacity. |
| View capacity details | On the Capacity Details tab, perform operations based on your business requirements. View capacity information about a cluster: In the cluster list, find the cluster that you want to view and view information about the cluster in the following columns: Cluster, Zone, Storage Type, Physical Capacity Usage, Physical Capacity Usage (TiB), Logical Capacity Usage, Logical Capacity Usage (TiB), Inventory Capacity Usage, and Inventory Capacity Usage (TiB). Search for a cluster: Select a cluster from the Cluster drop-down list and click Search. You can also click Advanced Filter to filter clusters by Cluster, Zone, Storage Type, or their combinations. Export capacity information of a cluster: Click Export in the upper- right corner to export the capacity information of the cluster to your computer in the CSV format. Filter or sort displayed columns: Click the icon in the upper-right corner. In the dialog box that appears, select or deselect the columns and adjust the display order of selected columns. |

ge storage capacity

| Configure a capacity alert rule for a cluster | You can configure an alert rule for an EFS-NAS cluster based on its capacity usage. When the capacity usage of the cluster meets the specified trigger condition, the system generates an alert. i. On the Alert Settings tab, click Create. ii. In the Create Alert Rule dialog box, configure the Rule Name, Rule Description, Alert Severity, and Trigger Condition parameters. You can set the Trigger Condition parameter based on the physical capacity usage, logical capacity usage, or inventory capacity usage. You can set the comparator to Greater Than or Equal to, or Less Than or Equal To. The specific value must be an integer greater than or equal to 0. Configure the specific trigger condition based on your business requirements. For example, you can set the Trigger Condition parameter to Logic Disk(GiB) ssd Allocation Rate Greater Than or Equal to 80% for an all-flash cluster. iii. Click OK. After an alert rule is created, you can modify or delete the alert rule based on your business requirements. Modify an alert rule: Find the alert rule that you want to modify and click Edit in the Actions column. In the Edit Alert Rule dialog box, modify the Rule Name, Rule Description, Alert Severity, and Trigger Condition parameters, and then click OK. Delete an alert rule: Find the alert rule that you want to delete and click Delete in the Actions column. In the Note message, click OK. Filter or sort displayed columns: Click the icon in the upper-right corner. In the dialog box that appears, select or deselect the columns and adjust the display order of selected columns. |
|---|---|
