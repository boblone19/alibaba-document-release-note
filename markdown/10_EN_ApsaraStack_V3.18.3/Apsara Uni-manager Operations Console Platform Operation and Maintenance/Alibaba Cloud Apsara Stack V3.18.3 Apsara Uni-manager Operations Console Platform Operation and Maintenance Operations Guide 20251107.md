---
title: "Alibaba Cloud Apsara Stack V3.18.3 Apsara Uni-manager Operations Console Platform Operation and Maintenance Operations Guide 20251107"
product_version: "V3.18.3"
doc_version: "20251107"
pdf_pages: 348
source_pdf: "Alibaba Cloud Apsara Stack V3.18.3 Apsara Uni-manager Operations Console Platform Operation and Maintenance Operations Guide 20251107.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/V3.18.3/%E4%B8%93%E6%9C%89%E4%BA%91%E8%BF%90%E7%BB%B4%E5%B9%B3%E5%8F%B0/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.3%20Apsara%20Uni-manager%20Operations%20Console%20Platform%20Operation%20and%20Maintenance%20Operations%20Guide%2020251107.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes)
---

# Alibaba Cloud Apsara Stack V3.18.3 Apsara Uni-manager Operations Console Platform Operation and Maintenance Operations Guide 20251107

## Table of Contents

- 1 Computing O&M
  - 1.1 Compute Operations Console
    - 1.1.1 Computing overview
    - 1.1.2 Computing cluster O&M
      - 1.1.2.1 Configure cluster-level CPU oversold ratios
    - 1.1.3 Computing server O&M
    - 1.1.4 ECS O&M
      - 1.1.4.1 ECS instances
      - 1.1.4.2 Disks
      - 1.1.4.3 Images
      - 1.1.4.4 Snapshots
      - 1.1.4.5 ENIs
      - 1.1.4.6 Security groups
      - 1.1.4.7 Instance type management
      - 1.1.4.8 O&M audit logs
    - 1.1.5 Compute capacity analytics
    - 1.1.6 Manage migration tasks
    - 1.1.7 ECS Intelligent O&M
      - 1.1.7.1 ECS instance events
      - 1.1.7.2 ECS physical machine events
      - 1.1.7.3 ECS O&M events
      - 1.1.7.4 ECS physical machine O&M
    - 1.1.8 Computing O&M settings
    - 1.1.9 ECS workflows
    - 1.1.10 Computing O&M data
    - 1.1.11 Tiangong O&M
      - 1.1.11.1 Tiangong products
      - 1.1.11.2 Tiangong workflows
- 2 Network operations
  - 2.1 Network Operations Console
    - 2.1.1 Dashboard
      - 2.1.1.1 Overview
      - 2.1.1.2 Network topology
      - 2.1.1.3 Custom views
    - 2.1.2 Basic network
      - 2.1.2.1 Network element management
      - 2.1.2.2 Syslog
      - 2.1.2.3 HPN management
        - 2.1.2.3.1 HPN network elements
        - 2.1.2.3.2 RDMA network interface O&M
        - 2.1.2.3.3 HPN performance analysis
        - 2.1.2.3.4 HPN instant diagnostics
      - 2.1.2.4 CPN
        - 2.1.2.4.1 CPN diagnosis
        - 2.1.2.4.2 CPN performance analysis
        - 2.1.2.4.3 CPN access gateways
          - 2.1.2.4.3.1 Manage RDMA devices
          - 2.1.2.4.3.2 Manage RDMA device policies
          - 2.1.2.4.3.3 Manage policies for the RDMA device interface
        - 2.1.2.4.4 RDMA NIC O&M
        - 2.1.2.4.5 CPN management
          - 2.1.2.4.5.1 CPN topology
          - 2.1.2.4.5.2 CPN network element
        - 2.1.2.4.6 CPN network monitoring
          - 2.1.2.4.6.1 CPN host monitoring dashboard
          - 2.1.2.4.6.2 CPN switch dashboard
          - 2.1.2.4.6.3 NAK packet analysis tool
      - 2.1.2.5 CGW
      - 2.1.2.6 Leased line management
        - 2.1.2.6.1 Leased lines
        - 2.1.2.6.2 Leased line group
        - 2.1.2.6.3 Access point management
        - 2.1.2.6.4 Access device management
        - 2.1.2.6.5 Express Connect circuit management
        - 2.1.2.6.6 VBR management
        - 2.1.2.6.7 Router interface management
        - 2.1.2.6.8 Route table management
      - 2.1.2.7 opsDNS management
        - 2.1.2.7.1 opsDNS monitoring
        - 2.1.2.7.2 opsDNS domain service
      - 2.1.2.8 Connection of intelligent computing servers to VPCs
        - 2.1.2.8.1 Manage access gateways
        - 2.1.2.8.2 Manage operation logs
        - 2.1.2.8.3 Manage networks for bare metal instances
        - 2.1.2.8.4 O&M configurations
          - 2.1.2.8.4.1 Apply for a bare metal instance in a VPC
          - 2.1.2.8.4.2 Release a bare metal instance in a VPC
          - 2.1.2.8.4.3 Delete a route table entry
          - 2.1.2.8.4.4 Delete a router interface
          - 2.1.2.8.4.5 Delete a VBR
          - 2.1.2.8.4.6 Delete an Express Connect circuit
          - 2.1.2.8.4.7 Delete all resources
          - 2.1.2.8.4.8 View the bandwidth of the Express Connect circuit
          - 2.1.2.8.4.9 View trunk usage
          - 2.1.2.8.4.10 View BM VPN usage
          - 2.1.2.8.4.11 View BD usage
          - 2.1.2.8.4.12 Check the initialization configuration
          - 2.1.2.8.4.13 Check the route configuration
          - 2.1.2.8.4.14 Display information about bare metal network gateways
    - 2.1.3 Networking services
      - 2.1.3.1 SLB O&M
        - 2.1.3.1.1 SLB cluster management
        - 2.1.3.1.2 SLB management
      - 2.1.3.2 Proxy O&M
        - 2.1.3.2.1 Proxy management
      - 2.1.3.3 XGW O&M
        - 2.1.3.3.1 XGW cluster management
        - 2.1.3.3.2 XGW management
        - 2.1.3.3.3 NAT gateway monitoring
        - 2.1.3.3.4 Router interface instances
      - 2.1.3.4 CGW O&M
        - 2.1.3.4.1 CGW management
      - 2.1.3.5 CEN O&M
        - 2.1.3.5.1 CEN-TR cluster management
        - 2.1.3.5.2 CEN workflows
      - 2.1.3.6 AVS O&M
        - 2.1.3.6.1 AVS management
      - 2.1.3.7 VPC-On-ECS
    - 2.1.4 Network monitoring and alerting
      - 2.1.4.1 Network alert dashboard
      - 2.1.4.2 Network alert settings
        - 2.1.4.2.1 Monitoring rule management
        - 2.1.4.2.2 Alert template management
        - 2.1.4.2.3 Trap template settings
    - 2.1.5 Intelligent diagnostics
      - 2.1.5.1 Network inspection
      - 2.1.5.2 Intelligent path analysis
      - 2.1.5.3 Network instance diagnostics
      - 2.1.5.4 Container network diagnostics
      - 2.1.5.5 Network health assessment
      - 2.1.5.6 Optical transceiver module diagnostics
    - 2.1.6 Network resources
      - 2.1.6.1 Network asset management
      - 2.1.6.2 IP address pool management
        - 2.1.6.2.1 IP address pools
        - 2.1.6.2.2 Collection settings
      - 2.1.6.3 Reverse access
    - 2.1.7 Traffic visualization
      - 2.1.7.1 Visual settings
      - 2.1.7.2 Overview
      - 2.1.7.3 Traffic search and scheduling
    - 2.1.8 Cloud service interconnection
      - 2.1.8.1 Dynamic VIPs
      - 2.1.8.2 Dynamic DNS
    - 2.1.9 Network changes
      - 2.1.9.1 Change plans
      - 2.1.9.2 Execution history

O&M

## 1 Computing O&M

### 1.1 Compute Operations Console

#### 1.1.1 Computing overview

This topic describes the Computing Overview page of the Compute Operations Console. On the Computing Overview page, you can obtain a high-level overview of services in IaaS O&M, stay updated with service status, and view service information, such as diagnostic results, alerts, inventory usage, key metrics, and health status.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Computing** > **Compute**
3. View information on the **Computing Overview** page.
4. In the **Service Check** section, view the diagnostic score that is displayed on the dashboard
and the numbers of check items that are in the Normal, Risk, Abnormal, and Suggestion states.

> **Note:** If the diagnostic score is 100, the dashboard is displayed in green. If the diagnostic score is lower than 100, the dashboard is displayed in red.

O&M In the upper-right corner of the section, click **Check Now**. In the **Service Check** dialog box, view the updated diagnostic score on the dashboard, status of each check item, and exception details.
5. In the **Unhandled Alerts Today** section, view the number of alerts at each severity level
in the chart. In the upper-right corner of the section, click **View Details**. The Alerts page appears. You can also choose **Monitor&Alarms** > **Alerts** > **Alerts** in the top navigation bar of the Apsara Uni-manager Operations Console to go to the Alerts page.
6. In the **One-click Search** section, enter an Elastic Compute Service (ECS) instance ID, a
disk ID, an image ID, an elastic network interface (ENI) ID, a security group ID, the private or public IP address of an ECS instance, or the IP address or hostname of a physical machine to search for the required resource. In the search result, click the resource to go to the details page. On the page that appears, view the information about the resource.
7. In the **Allocated Capacity Ratio** section, view the metric statistics of clusters in the
**Usage**, **Used**, **Available**, and **Total** columns. The metrics include vCPUs (Cores), Memory
(GB), and EIPs.

> **Note:** By default, the metric statistics of all clusters are displayed in the Allocated Capacity Ratio section. You can select a cluster from the drop-down list in the upper-right corner of this section to display only the metric statistics of the selected cluster.

8. In the **Core Metrics** section, view the total number of clusters and the numbers of
computing clusters, storage clusters, and hybrid clusters. You can also view the total number of computing servers, the numbers of computing servers in the **Normal**, **Mlock**, and **NC_Downtime** states, the total number of ECS instances, and the numbers of ECS instances in the **Running**, **Stopped**, and **Pending** states. Perform the following operations to view the details of clusters, servers, or ECS instances: Click the value of **Total Number of Clusters** to view cluster details on the **Computing**
**Cluster O&M** page.
Click the value of **Total Number of Computing Servers** to view server details on the
**Computing Server O&M** page.
Click the value of **Total Number of ECS Instances** to view instance details on the **ECS**
**Instances** page.
9. In the **Health Status of Services** section, view the health status of each service.
Find the service that you want to view and click the service name. In the **Deploy Servers** dialog box, view information in the columns, including **Status**, **Server Role**, **IP**,
**Hostname**, **Cluster**, **Description**, and **Service**.

#### 1.1.2 Computing cluster O&M

You can perform O&M operations on computing clusters and view cluster information and status.

**View computing clusters and their O&M details**

1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Computing** > **Compute**
3. In the left-side navigation pane, click **Computing Cluster O&M**. By default, the
information of all clusters is displayed on the Computing Cluster O&M page. O&M
4. In the upper-right corner of the Computing Cluster O&M page, view the total number of
clusters, the number of clusters that have not reached the desired state, and the number of clusters that have reached the desired state.

> **Note:** The number of clusters that have not reached the desired state is displayed in red.

5. In the upper-left corner of the page, enter a cluster name in the search box for exact
search. View the cluster information in the following columns: **Cluster Name/Alias**, **Region**, **CPU**
**Processor**, **Cluster Type**, **Compute Type**, **Desired State**, **Zone**, **Servers**, **Instance**
**Family**, and **Cluster Specifications**.

> **Note:** Valid values of the **Compute Type** parameter:
> CPU: provides CPU and memory resources for Elastic Compute Service (ECS) instances in the Kernel-based Virtual Machine (KVM) architecture.
> Local Disk: provides local storage, CPU, and memory resources for ECS instances in the KVM architecture.
> GPU: provides GPU, CPU, and memory resources for ECS instances in the KVM architecture.
> Hybrid: provides cloud storage, CPU, and memory resources for ECS instances in the KVM architecture.
> SHENLONG: provides CPU and memory resources for ECS instances in the SHENLONG architecture.
> VMOC: provides CPU and memory resources for ECS instances in the Virtual Mission Operational Center (VMOC) architecture. The VMOC architecture can be deployed on non-SHENLONG physical machines to provide computing power for ECS instances.
> Valid values of the **Cluster Specifications** parameter:
> share,ncTypeHybrid: shared clusters.
> pin,exclusive,ncTypeHybrid: exclusive clusters.
> ncTypeHybrid,bareMetal: bare metal clusters.

6. View the O&M details of a computing cluster.
i. On the Computing Cluster O&M page, click the name of the cluster that you want to view to go to the **Computing Cluster Details** page. O&M ii. On the **Overview** tab, view the information about computing servers and ECS instances in the cluster. In the **Cluster Information** section, view the basic information of the cluster, including the region in which the cluster is deployed, cluster type, whether the cluster uses only ECS resources, zone, cluster ID, instance family, cluster status, network type, physical network, disk type, and cluster specifications.

> **Note:** In the upper-right corner of this section, click **Connect to Cluster AG** to log on to the Admin Gateway (AG). For more information, see the Log on to the AG of a cluster section of this topic.

In the **Server Resources** section, view the number of computing servers, the number of CPUs, and the amount of available memory. O&M In the **ECS Instances** section, view the total number of ECS instances, the number of ECS instances that are running, and the number of abnormal ECS instances. In the **NC State Distribution** section, view the distribution of physical machines in different states.

> **Note:** Move the pointer over the chart. The number of physical machines in each state is displayed.

The following table describes the states of physical machines.

| State | Description |
|---|---|
| Failover | The physical machine is down. |
| Normal | The physical machine runs as expected. You can schedule instances to the physical machine. |
| No heartbeat | The physical machine has no heartbeats. |
| Mlock | The physical machine is manually locked. |
| Rlock | The physical machine is forcefully reserved and can be used to recover or modify VMs. If the resources of the physical machine are insufficient, the physical machine performs defragmentation. Otherwise, an alert is triggered. The physical machine must have heartbeats and remain available. |
| Initializing | The physical machine is being initialized. All the virtual private cloud (VPC) configurations of the physical machine are being reissued by the RegionMaster. |

O&M In the **ECS Instance State Distribution** section, view the distribution of ECS instances in different states. The following table describes the states of ECS instances.

| State | Description |
|---|---|
| Running | The instance runs as expected. |
| Stopped | After an instance is stopped or after an instance is created but not started, the instance is in the Stopped state. Instances in the Stopped state cannot provide external services. |
| Pending | After an instance is created, the instance is in the Pending state before it enters the Running state. If the instance remains in the Pending state for an extended period of time, an exception occurs. |
| Creating | After you start or restart an instance in the ECS console or by calling an API operation, the instance enters the Creating state before it enters the Running state. If the instance remains in the Creating state for an extended period of time, an exception occurs. |
| Stopping | After you stop an instance in the ECS console or by calling an API operation, the instance enters the Stopping state before it enters the Stopped state. If the instance remains in the Stopping state for an extended period of time, an exception occurs. |
| Releasing | After you release an instance, the instance enters the Releasing state before it enters the Released state. |

In the **Inventory Utilization** section, view the total amount of resources, the amount of used resources, and the percentage of used resources in all resources. In the **Inventory** section, view the inventory details of the instance types in the cluster. iii. Click the **Configurations** tab. On this tab, you can configure the CPU oversold ratio and view its configuration records. For more information, see Configure CPU oversold ratios. iv. Click the **Computing Servers** tab. O&M View information about the computing servers in the cluster in the following columns:
**Hostname**, **IP Address**, **NC ID**, **NC Type**, **vCPU (Cores)**, **Memory**, **Service State**,
**Instances**, **Data Center**, **Rack**, and **SN**.

> **Note:** For more information about valid values of the Service State parameter, see the table describing the states of physical machines of this topic.

View the O&M details of a computing server. a. Find the computing server that you want to view and click the server name in the
**Hostname** column.
b. On the **Computing Server Details** page, view the O&M details of the computing server. For more information, see the 6. View the O&M details of a computing server. section of the "Computing server O&M" topic. View the details of ECS instances that are deployed on a computing server. a. Find the computing server that you want to view and click the number in the
**Instances** column.
b. In the **Instance List** panel, view the instance information in the following columns:
**Instance ID**, **Status**, **Instance Name**, **CPU**, and **Memory**.
c. Click an instance ID in the **Instance ID** column. The **Instance Details** page of the ECS instance appears. For more information, see ECS instances. O&M Manage the service states of the computing servers in the cluster. The following table describes the operations that you can perform on computing servers.

| Operation | Scenario | Procedure |
|---|---|---|
| Lock NC | You can lock abnormal servers to prevent instances from being scheduled to these servers. If the servers are locked, the status of the servers cannot be automatically changed. You can also lock servers for which you want to reserve resources. | a. On the Computing Servers tab, find the server that you want to lock and click Lock NC in the Operation column. b. In the Lock NC dialog box, confirm the server information, select a lock state, and then configure the Changed By, Change Ticket Title, and Reason parameters. c. Click OK. |
| Unlock NC | You can unlock servers in the no heartbeat, mlock, and rlock states. After you unlock a server, the server is automatically activated and you can schedule instances to the server. | a. On the Computing Servers tab, find the server that you want to unlock and click Unlock NC in the Operation column. b. In the Unlock NC dialog box, confirm the server information and enter the reason for unlocking the server. c. Click OK. |
| Activate | You can activate servers in the no heartbeat, mlock, rlock, failover, and initializing states. | a. On the Computing Servers tab, find the server that you want to activate and click Activate in the Operation column. b. In the dialog box that appears, enter a reason for activating the server, the user who performed the operation, and a ticket title in the Reason field. c. Click OK. |

**Log on to the AG of a cluster**

You can log on to the AG of a cluster to go to the Terminal Service page. Then, you can perform O&M operations on VMs in the cluster by using the CLI.
1. On the Computing Cluster O&M page, find the cluster that you want to manage and click
**Connect to Cluster AG** in the **Operation** column. The Terminal Service page appears.
2. Perform O&M operations by using the CLI on the Terminal Service page based on your
business requirements. O&M

##### 1.1.2.1 Configure cluster-level CPU oversold ratios

The CPU oversold ratio configuration feature allows you to dynamically change the number of saleable vCPUs in a cluster based on your business requirements. This topic describes how to change the CPU oversold ratio of a cluster.

**Limits**

You can change the CPU oversold ratio only at the cluster level. The CPU oversold ratio configuration feature is available only for clusters that use specific shared Elastic Compute Service (ECS) instances of the following instance families: Intel processor-powered instance families: ecs.s5-k, ecs.s6-k, ecs.s7-k, and ecs.s8-k Hygon processor-powered instance families: ecs.s5-hg-k, ecs.s6-hg-k, and ecs.s7-hg-k Yitian processor-powered instance family: ecs.s8-yt-k Kunpeng processor-powered instance family: ecs.s5-kp-k Phytium processor-powered instance families: ecs.s5-ft-k and ecs.s6-ft-k Sunway processor-powered instance family: ecs.s6-sw-k Custom instance family: ecs.anyshare (If only instances of the ecs.anyshare instance family are available for a cluster, the CPU oversold ratio of the cluster cannot be changed.) The CPU resources of offline servers in a cluster are unavailable for changing the CPU oversold ratio of the cluster. You cannot change the CPU oversold ratio of a cluster that is being scaled. You can change the CPU oversold ratio of a cluster only if at least one server in the cluster is in the free state.

**Precautions**

Before you change the CPU oversold ratio of a cluster, the system checks whether the CPU oversold ratios of all servers in the cluster are the same. If the CPU oversold ratios of the servers are different, the system does not allow you to change the CPU oversold ratio of the cluster. O&M When you change the CPU oversold ratio of a cluster, a precheck task is initiated. If the precheck task fails, you cannot change the CPU oversold ratio of the cluster. In this case, you must handle the error based on the failure message reported by the precheck task, and then change the CPU oversold ratio of the cluster again. You can change the CPU oversold ratio of a cluster only once within 3 hours. This limit does not apply to the precheck task. When you change the CPU oversold ratio of a cluster, the CPU oversold ratios of dedicated hosts associated with the cluster are not affected. The following specific rules apply: After you change the CPU oversold ratio of a cluster, the number of saleable vCPUs of a dedicated host remains unchanged. After a dedicated host is released, the number of saleable vCPUs of the dedicated host is recalculated based on the CPU oversold ratio that you last configured for the cluster. When you reduce the CPU oversold ratio of a cluster, the system checks whether the number of used vCPUs is greater than 80% of the number of saleable vCPUs in the cluster after the reduction. If yes, you cannot reduce the CPU oversold ratio of the cluster. A high CPU oversold ratio may cause performance degradation issues, such as extended response time, intensified resource contention, and host instability. Proceed with caution. After you change the CPU oversold ratio of a cluster, you can view the details of the change on the **CPU Oversold Ratio Configuration Records** tab. An extended period of time is required to complete the change. You cannot terminate, cancel, or roll back the change. The CPU oversold ratio change may fail on specific servers. In this case, you can contact O&M engineers to change the CPU oversold ratios of these servers in the Emergency Operation Command Center (EOCC).
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Computing** > **Compute**
3. In the left-side navigation pane, click **Computing Cluster O&M**.
4. On the Computing Cluster O&M page, find the cluster that you want to manage and click
the cluster name to go to the **Computing Cluster Details** page.
5. On the Computing Cluster Details page, click the **Configurations** tab.
6. On the **Configure CPU Oversold Ratio** tab, change the CPU oversold ratio of the cluster.
Enter your reason for this change in the **Reason** field, select **I have read the preceding**
**notes and want to perform the operation.**, and then click **Submit**.
7. On the **CPU Oversold Ratio Configuration Records** tab, view the configuration records
of CPU oversold ratios. You can specify the **Task Type** parameter to search for required records, and then view the information about the records in the following columns: **Task ID**, **Cluster Name**, **Task**
**Status**, **Task Type**, **Pre-change vCPUs per Server**, **Post-change vCPUs per Server**,
**Task Start Time**, **Task End Time**, and **Result**.

**FAQ**

**What do I do if the CPU oversold ratios of servers are different**

**in a cluster?**

You are not allowed to change the CPU oversold ratio of a cluster if the CPU oversold ratios of servers are different in the cluster. This may occur due to the following causes:
1. You changed the CPU oversold ratios of specific servers in the cluster by using a command
line interface (CLI). O&M
2. You changed the CPU oversold ratios of servers in the cluster in a visualized manner.
However, the CPU oversold ratios of specific servers failed to be changed due to exceptions. If you failed to change the CPU oversold ratio of a cluster due to inconsistent CPU oversold ratios of servers in the cluster, contact O&M engineers to change the CPU oversold ratios of all servers to the same value in the EOCC.

**What do I do if the number of unused vCPUs on specific servers**

**is negative?**

When you reduce the CPU oversold ratio of a cluster, the system only checks whether the number of used vCPUs of the entire cluster instead of individual servers exceeds the threshold. As a result, the number of unused vCPUs on specific servers may be negative. In this case, you can perform hot or cold migration to move some ECS instances to other servers.

#### 1.1.3 Computing server O&M

You can perform O&M operations on computing servers to view server information and status.

**View computing servers and their O&M details**

1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Computing** > **Compute**
3. In the left-side navigation pane, click **Computing Server O&M**.
In the upper-right corner of the Computing Server O&M page, view the total number of computing servers and the numbers of computing servers in the **free**, **mlock**, and
**nc_down** states.
4. On the **Machines** tab of the Computing Server O&M page, you can view the details of all
computing servers. In the upper part of the Machines tab, enter an IP address, a hostname, or a serial number in the search box to search for a computing server. Alternatively, click **Advanced Search** and search for a computing server by **Model**, **Data Center**, **Rack**, or their combinations.
5. In the list below, view the information about each computing server in the following
columns: **Host Name/Alias**, **NC IP/ID**, **Model**, **CPU Cores**, **Memory**, **CPU Processor**,
**Compute Type**, **Status**, **Cluster**, **Data Center**, **Rack**, **SN**, and **Region**.
O&M

> **Note:** For information about valid values of the **Status** parameter, see the table that describes the states of physical servers in the Computing cluster O&M topic.
> Valid values of the **Compute Type** parameter:
> CPU: provides CPU and memory resources for Elastic Compute Service (ECS) instances in the Kernel-based Virtual Machine (KVM) architecture.
> Local Disk: provides local storage, CPU, and memory resources for ECS instances in the KVM architecture.
> GPU: provides GPU, CPU, and memory resources for ECS instances in the KVM architecture.
> Hybrid: provides cloud storage, CPU, and memory resources for ECS instances in the KVM architecture.
> SHENLONG: provides CPU and memory resources for ECS instances in the SHENLONG architecture.
> VMOC: provides CPU and memory resources for ECS instances in the Virtual Missions Operational Center (VMOC) architecture. The VMOC architecture can be deployed on non-SHENLONG physical servers to provide computing power for ECS instances.

6. View the O&M details of a computing server.
i. Find the computing server that you want to view and click the name in the **Hostname** column. ii. On the Computing Server Details page, you can perform operations on the computing server by clicking buttons in the upper-right corner. For more information, see the Perform diagnostics on a computing server section of this topic. iii. On the **Computing Server Details** page, view the following information.

| Section/Tab | Description |
|---|---|
| Business Information | Displays the business information about the computing server, including Business ID, IP, Hostname, Status, Management Heartbeat, Selling Mode, Cluster, Available Instance Families, Operating System, and Compute Type. Note Click the cluster name to go to the Computing Cluster Details page. On this page, view the O&M details of the computing cluster. For more information, see the 6. View the O&M details of a computing cluster section of the "Computing cluster O&M" topic. |

O&M

| Hardware Information | Displays the hardware information about the computing server, including SN, Model, Rack, CPU Model, GPU, vCPU (Cores), and Memory. |
|---|---|
| Resource Information | Displays the vCPU utilization, the total number of vCPU cores, the number of used vCPU cores, the number of available vCPU cores, the memory usage, the total memory, the used memory, and the available memory. |
| ECS Instances | On this tab, you can perform the following operations: In the upper part of the tab, enter an instance ID in the search box to search for an ECS instance. Alternatively, click Advanced Search and search for an ECS instance by Business Foundation System Status, AliUid, or their combinations. In the ECS instance list, view the information about each ECS instance in the following columns: Instance ID/Name, vCPU/Memory, Status, Private/Public IP Address, Bandwidth, User Information, Images, Creation Time, and All in ECS Resources or Not. View the details of an ECS instance. Find the ECS instance that you want to view and click its ID to go to the instance details page. For more information, see the 7. View the details of an instance. section of the "ECS instances" topic. Manage an ECS instance. You can perform diagnostics on the instance, migrate the instance, view migration history, view audit logs, change the instance status, and manage ISOs. For more information, see the What to do next section of the "ECS instances" topic. |

O&M

| Performance Monitoring | On this tab, specify a time range and view the trend charts of the following performance metrics within the specified period of time: CPU(%), Memory (%), System Load, Network Retransmission (%), and Network Traffic (MB). |
|---|---|
| Alert Information | On this tab, view the information about each alert, including the alert name, alert cause, alert details, first time when the alert was reported, last time when the alert was reported, and number of times that the alert was reported. |
| Control Service | On this tab, view server roles and their states. You can also search for a server role on this tab. View the server role information in the Apsara Infrastructure Management console: Find the server role that you want to view and click Apsara Infrastructure Management Framework in the Operation column to go to the Product & Cluster O&M page. For more information, see Apsara Infrastructure Management O&M Guide. |

O&M

| Machine Migration Task | View the information about each migration task, including the task ID, number of migrated instances, destination physical server, task status, migration progress, start time, update time, and task creator. View the details of a migration task: Find the migration task that you want to view and click its ID. In the Migrated Instance Details panel, view the detailed information about the task, including the instance ID, migration status, destination physical server, migration type, number of retries (used retries/maximum retries), start time, update time, and migration result. Note Cold migration tasks: migrates instances that are in the Pending state. Hot migration tasks: migrates instances that are in the Running state. Restart a migration task. If a migration task fails, you can clickR estart in the Operation column of the task. In the dialog box that appears, enter the reason and then click OK. Cancel a migration task: Find the migration task that you want to cancel and click Cancel in the Operation column. In the dialog box that appears, enter the reason and then click OK. |
|---|---|
| Operation Audit | During the O&M of a computing server, the operations that may cause risks are audited. On this tab, you can click the following sub-tabs to view the corresponding information. For more information, see O&M audit logs. Operations in the Apsara Uni-manager Operations Console POP API Calls Server Controller API Call History |

**Perform diagnostics on a computing server**

1. On the Computing Server Details page of a computing server, click **Diagnose** in the upper-
right corner.
2. On the **End-to-end Demarcation** page, view the diagnostic results. For more information,
see ECS Diagnosis.

**View operation records of a computing server**

**Background information**

During the O&M of a computing server, the operations that may cause risks are audited. You can view the detailed audit information about the computing server.
1. Find the computing server that you want to view and click **Audit Operations** in the
**Operation** column.
2. View the information displayed in the **Audit Operations** panel. For more information, see
O&M audit logs.

**Lock a physical server**

O&M

**Background information**

You can lock physical servers based on your business requirements. If a physical server is locked, you cannot create instances on it. mlock: If a physical server is locked and enters the mlock state, ECS instances on it are restarted and scheduled to other physical servers, excluding the instances for which failover is disabled. rlock: If normal physical servers do not meet the failover requirements, the physical servers in the rlock state are used to restore instances that fail.
1. Find the computing server that you want to lock, and click **Lock** in the **Operation** column.
2. In the **Lock NC** dialog box, confirm the server and configure the **Lock Status**, **Changed**
**By**, **Change Ticket Title**, and **Locking Reason** parameters.
3. Then, click **OK**.

**Unlock a physical server**

**Background information**

You can unlock physical servers that are in the no heartbeat, mlock, and rlock states. After you unlock a physical server, the server is automatically activated and you can schedule instances to the server. O&M
1. Find the computing server that you want to unlock and click **Unlock** in the **Operation**
column.
2. In the **Unlock NC** dialog box, confirm the server and enter the reason.
3. Then, click **OK**.

**Activate a physical server**

**Background information**

You can activate computing servers that are in the mlock, rlock, no heartbeat, nc_down, and initializing states.

**Prerequisites**

The computing server that you want to activate is in the **mlock** state.
1. Find the computing server that you want to activate, move the pointer over the
icon in the **Operation** column, and then select **Activate**.
2. In the dialog box that appears, confirm the computing server information and enter the
reason.
3. Then, click **OK**.

**Migrate all instances from a server**

**Background information**

When you scale down or maintain a computing server, you must migrate all ECS instances on the server before you can perform operations on the server. In this case, you can migrate all ECS instances on the server to other computing servers.

**Prerequisites**

The computing server is in the free or mlock state.

**Usage notes**

After you submit a migration task, the server enters the mlock state. After the migration task is complete, fails, or is canceled, you must submit an application to unlock the server. The ECS instances on the server are migrated to other computing servers based on the ECS scheduling rules. The migration task may not be successful in a single attempt due to various reasons. If an ECS instance in the **Stopped** or **Pending** state is migrated, the system attempts to start the ECS instance and bring the ECS instance to the **Running** state. You cannot specify the computing server to which the ECS instances are migrated. After the migration task is complete, you must check for any remaining ECS instances on the original server to ensure that all ECS instances are migrated.
1. Find the computing server that you want to manage, move the pointer over the
icon in the **Operation** column, and then select **Migrate All Instances**.
2. On the Create Machine Migration Task page, configure the following parameters.
O&M

| Section | Parameter | Description |
|---|---|---|
| Source NC | Select Machine | The server from which you want to migrate all ECS instances. Enter a hostname or an IP address in the search box to search for a server, and then select it. Important You can select only one server. |
| Migration Destination Configurations | Enhanced Hot Migration Compatibility | Specifies whether to enable the enhanced hot migration compatibility. If you set this parameter to Yes, you can migrate the ECS instances to an available physical server with a different CPU model. For information about CPU compatibility, see the CPU compatibility configurations section of the "Manage migration tasks" topic. |
|   | Destination Selection Policy | Random Selection (default): migrates the ECS instances to a random physical server that has sufficient resources. Specify NC: migrates the ECS instances to a specific physical server. If you select this policy, the migration may fail. To specify the destination server, search for physical servers by cluster, hostname, server IP address, or server ID, and then select the physical server from the server list. Note The system provides suggestions on each physical server only for reference. You can select a physical server that is not recommended based on your business requirements. Specify Cluster: migrates the ECS instances to a specific cluster. If you select this policy, the migration may fail. To specify the destination cluster, search for the cluster by name, and then select it in the cluster list below. Note The system provides suggestions on each cluster only for reference. You can select a cluster that is not recommended based on your business requirements. |

O&M

| Advanced Migration Parameters Note You can configure advanced paramete rs based on your business requirem ents to increase the success rate of instance migration . You can click Configur ation Descript ion to view the descriptio n of the paramete rs in this section. | Allowed Service Interruption Duration | The service interruption duration in the last phase of hot migration. Unit: milliseconds. Valid values: 200 to 2000. Default value: 300. |
|---|---|---|
|   | Check SLB | Valid values: Yes: checks whether the ECS instances to be migrated are associated with Server Load Balancer (SLB) instances. If the ECS instances to be migrated are associated with SLB instances, the migration task may fail. No: does not check whether the ECS instances to be migrated are associated with SLB instances. Default value: Yes. |
|   | Check AVS Version | Valid values: Yes: checks whether the AVS versions of the source and destination hosts are the same. If the AVS versions are different, the migration task fails. No: does not check the AVS versions of the source and destination hosts. Default value: Yes. |
|   | Check Virtual NC Version | Valid values: Yes: checks whether the virtualization version of the destination host supports hot migration. If hot migration is not supported, the migration task fails. No: does not check the virtualization version of the destination host. Default value: Yes. |
|   | Allow Reserved NC | Valid values: Yes: allows the ECS instances to be migrated to a reserved host. No: does not allow the ECS instance to be migrated to a reserved host. Default value: No. |

O&M

|   | Check CPU Tag | Valid values: Yes: checks whether the CPU tag set of the source host is a subset of the CPU tag set of the destination host. If the CPU tag set of the source host is not a subset of the CPU tag set of the destination host, the migration task fails. No: does not check the CPU tag set of the source host. Default value: Yes. |
|---|---|---|
| Operation Information | Reason | The reason for migrating all ECS instances on the physical server. |

3. Select **I have read the preceding notes and confirm this operation.** and click
**Submit**.

**What to do next**

After you run a task to migrate all ECS instances from a computing server, you can check the progress and result of the migration task.
1. On the **Machine Migration Tasks** tab, view the following information about each
migration task. You can search for a migration task by **Task ID**, **Source Physical**
**Machine ID**, or their combination.

| Parameter | Description |
|---|---|
| Task ID | The ID of the migration task. |
| Source NC ID and IP Address | The ID and IP address of the source physical server from which ECS instances are migrated. |
| Instances | The number of ECS instances that are migrated. |
| Task Status | The status of the migration task. Valid values: init running success failed create failed create ecs migrate task canceled |

O&M

| Task Success Rate | The success rate of the migration task, which is calculated based on the following formula: Success rate of a migration task = (Number of successful subtasks/Total number of subtasks) × 100%. |
|---|---|
| Destination Selection Policy | The policy for selecting a destination physical server. The policy that you specified when you created the migration task is displayed. |
| Destination Information | The destination physical server or cluster to which the ECS instances are migrated. |
| Task Result | The result of the migration task. A value of all ecs migrate tasks belong to this task success! indicates that the migration task is successful. |
| Created At | The time when the migration task was created. |
| Updated At | The time when the migration task was updated. |
| Migration Reason | The reason for creating the migration task. |
| Operator | The account that is used to create the migration task. |

| ask Result | belong to this task success! |
|---|---|

2. Click **Details** in the **Operation** column of a migration task. In the panel that appears, view
the following information:
**Basic Information**: This section displays the basic information about the migration task,
such as the task ID, number of ECS instances, and task status.
**Instances**: This section displays view the ECS instances involved in the migration task.
3. Cancel a migration task based on your business requirements.

> **Note:** After you cancel a migration task:
> The migration task enters the **canceled** state.
> Subtasks that are in the **init** state are terminated. Subtasks that are in the **pending** and **migrating** states are not affected.

i. Find the migration task that you want to cancel, and click **Terminate Task** in the
**Operation** column.
ii. In the message that appears, click **OK**.

**Deactivate a physical machine for maintenance**

**Back information**

O&M If a physical machine cannot be repaired at the software level in the current environment and must be deactivated for maintenance, you must notify your customers at the earliest opportunity and obtain their authorization before you can deactivate the physical machine for maintenance on site. After the physical machine is repaired, reactivate the physical machine and put it back into service in its original computing cluster. We recommend that you deactivate physical machines for maintenance on the **ECS**
**Intelligent O&M** > **ECS Physical Machine O&M** page. For more information, see ECS
physical machine O&M.

> **Warning:** Service interruptions may occur during the instance migration process. We recommend that you deactivate the physical machine during off-peak hours.

1. Find the computing server that you want to manage, move the pointer over the
icon in the **Operation** column, and then select **Deactivate for Maintenance**.
2. In the **Deactivate for Maintenance** dialog box, confirm the hostname, IP address, cluster,
serial number of the server, and configure the **Reason** and **Operator** parameters.
3. Then, click **OK**.

**What to do next**

View the maintenance details of a physical machine.
1. In the left-side navigation pane, choose **ECS Intelligent O&M** > **ECS Physical Machine**
**O&M**.
O&M
2. On the Physical Machine Maintenance page, find the physical machine that you want to
view and click **Details** in the **Operation** column to go to the Physical Machine Maintenance Details page. For more information, see ECS physical machine O&M.

#### 1.1.4 ECS O&M

##### 1.1.4.1 ECS instances

An Elastic Compute Service (ECS) instance is a virtual computing environment that consists of the most basic computing components, such as the CPU and memory. Users perform operations on ECS instances. This topic describes how to perform O&M operations on ECS instances.

**View ECS instances and their instance details**

1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Computing** > **Compute**
3. In the left-side navigation pane, choose **ECS O&M** > **ECS Instances**.
4. In the upper-right corner of the ECS Instances page, view the total number of ECS instances
and the numbers of ECS instances that are in the **Running**, **Stopped**, **Creating**, and
**Releasing** states.

> **Note:** The numbers displayed in the upper-right corner of the page may be different from those displayed in the ECS instance list due to workflow errors. The numbers displayed in the upper-right corner of the page prevail.

5. In the upper-left corner of the page, search for an ECS instance by instance ID, private IP
address, or public IP address. You can also click **Advanced Search** and filter ECS instances by **State in Business Foundation System**, **VPC**, **Apsara Stack Tenant Account ID**, or their combinations. Alternatively, you can select **All in ECS 1.0** or **All in ECS 2.0** in the upper-right corner of the page to filter ECS instances. O&M

> **Note:** **All in ECS 1.0**: indicates Heavenly Palace Adapter 1.0, which is the basic architecture for deploying On ECS services. You can deploy On ECS services on Heavenly Palace Adapter 1.0 only in the Apsara Infrastructure Management console. Heavenly Palace Adapter 1.0 serves as the agent for cloud services to apply for ECS resources. During the resource application, ECS clusters are exclusively occupied. The ECS instances in the clusters belong to Heavenly Palace Adapter 1.0 accounts and are deployed in virtual private clouds (VPCs).
> **All in ECS 2.0**: indicates Heavenly Palace Adapter 2.0, which is the advanced architecture for deploying On ECS services. You can deploy On ECS services on Heavenly Palace Adapter 2.0 in the Apsara Infrastructure Management console or by using Kubernetes cloud-native. Heavenly Palace Adapter 2.0 simplifies resource lifecycle management by using Infrastructure as Code (IaC) baseline declarations. When resources are called, tenant-side ECS clusters are shared. The ECS instances in the clusters belong to Heavenly Palace Adapter 2.0 accounts and are deployed in VPCs.

6. In the ECS instance list, view the instance information in the following columns: **Instance**
**ID/Name**, **Host**, **Host Name/Alias**, **Cluster**, **CPU/Memory**, **Status**, **Private /Public IP**
**Address**, **RDMA IP**, **Bandwidth**, **User Information**, **Image**, **Creation Time**, and **All in**
**ECS Project**.

> **Note:** Values in the **Status** column:

Business Foundation System: the status of an ECS instance in the Business Foundation System database. The Business Foundation System control service is the database that is applied for by the ECS Business Foundation System service and is used to control ECS business logic such as sales, constraints, and inventory. Server Controller: The Server Controller control service is the scheduling system of ECS. Server Controller issues all operations related to ECS instances to physical machines, such as the creation, modification, and deletion of ECS instances.
7. View the details of an instance.
i. In the instance list, find the ECS instance that you want to view and click its ID in the
**Instance ID/Name** column.
ii. On the instance details page, you can click buttons in the upper-right corner to perform various operations on the ECS instance. For more information, see the What to do next section of this topic.

> **Note:** For information about how to log on to the cluster Admin Gateway (AG), see the Log on to the AG of a cluster section of the "Computing cluster O&M" topic.

iii. View the following information on the instance details page.

| Section or tab | Description |
|---|---|

O&M

| Basic Information | This section displays the basic information about the ECS instance, including Instance ID, Instance Name, Specifications, Region, Zone, Creation Time, Apsara Stack Tenant Account ID, State in Business Foundation System, State in Server Controller, Cluster, Host ID, Host, and Rack. |
|---|---|
| Configurations | This section displays the configuration information about the ECS instance, including I/O Optimized, System Image, Operating System, System Disk, Network Type, Internal Bandwidth, Private IP Address, RDMA IP, VPC ID, vSwitch, and NAT IP Address. |
| Disks | View the list of disks and the disk information, includingD isk ID, Disk Type, Status, Cluster, and Feature. View the details of a disk. Perform various operations on a disk by clicking buttons in the Operation column, including Detatch, Audit Operations, Create Snapshot, and View Snapshots. For more information, see the What to do next section of the "Disks" topic. |
| ENIs | View the information about the elastic network interfaces (ENIs) that are bound to the ECS instance. The information includes ENI ID/MAC Address, Status, ENI Type, vSwitch, and IP. View the details of an ENI. Perform various operations on an ENI by clicking buttons in the Operation column, including Unbind and Operation Audit. For more information, see the View operation records section of the "ENIs" topic. |

O&M

| Security Groups | View the information about the security group to which the ECS instance belongs. The information includes Security Group ID/Name, Network Type, VPC ID, and Creation Time. View the details of a security group. View operation records of a security group by clicking Audit Operations in the Operation column. For more information, see Security groups. |
|---|---|
| Snapshots | View the list of snapshots and the snapshot information, including Snapshot ID/Name, Snapshot ID in Server Controller, Snapshot Type, Disk ID/Type, Progress, and Creation Time. View the details of a snapshot. Perform various operations on a snapshot by clicking buttons in the Operation column, including Delete, Audit Operations, and Create Image. For more information, see Snapshots. |
| Performance Monitoring | You can specify a time range and view the charts that describe the instance performance within the specified period of time. The performance metrics include CPU utilization, disk read/write (byte/s), disk IOPS, public bandwidth (bit/s), and internal bandwidth (bit/s). |
| ASO Migration Tasks | After a migration task is triggered in the Apsara Uni-manager Operations Console, you can view the status and result of the migration task on this tab. You can view the task information including Task ID, Source NC ID and IP Address, Destination NC ID and IP Address, Task Type, Retries, Task Status, Start Time, Migration Reason, Operator, and Migration Task Result. Valid values of the Task Type parameter are Cold Migration and Hot Migration. The value of the Retries parameter is a ratio of the number of executed retries to the maximum number of retries. |

O&M

| Migration History | View the historical migration tasks that are created within the lifecycle of the ECS instance. Both cold migration and hot migration tasks are displayed. You can view the information about each migration task, includingS ource NC, Destination NC, Status, Migration Time, End Time, and Migration Reason. |
|---|---|
| Audit Operations | View the operation records of the ECS instance on theO perations in the Apsara Uni-manager Operations Console, POP API Calls, and Server Controller API Calls subtabs. For more information, see O&M audit logs. |
| Associate Resources | View the topology that shows the relationships among the ECS instance and its associated resources. The resources include account, VPC, VM, computing server, cluster, image, data disk, system disk, network interface card (NIC), and security group. You can move the pointer over a resource to view the details of the resource. |

8. View the O&M details of a computing server.
i. In the ECS instance list, find an instance that you want to view and click the IP address in the **Host** column. ii. On the **Computing Server Details** page, view the O&M details of the computing server. For more information, see the 6. View the O&M details of a computing server section of the "Computing server O&M" topic.
9. View the O&M details of a computing cluster.
i. In the ECS instance list, find an instance that you want to view and click the cluster name in the **Cluster** column. ii. On the **Computing Cluster Details** page, view the O&M details of the computing cluster. For more information, see the 6. View the O&M details of a computing cluster section of the "Computing cluster O&M" topic. O&M

**What to do next**

**Perform diagnostics on an instance**

1. On the ECS Instances page, find the instance that you want to manage and click **Diagnose**
in the **Operation** column.
2. On the **End-to-end Demarcation** page, view the diagnostic results. For more information,
see the "ECS Diagnostics" documentation.

**Migrate an instance**

**Background information**

When an ECS instance or the physical server on which the instance resides fails, you must migrate the instance to a healthy physical server. You can perform a cold migration task or hot migration task based on the status of an instance to migrate the instance. Cold migration tasks: migrates instances that are in the Pending, Shutted, or ShutFailure state. Hot migration tasks: migrates instances that are in the running state.
1. On the ECS Instances page, find the instance that you want to manage, move the pointer
over **Migrate** in the **Operation** column, and then select **Migrate Instance**.
2. On the Create ECS Migration Task page, configure the parameters that are described in the
following table.

> **Note:** The **Cold Migration** or **Hot Migration** migration type is automatically selected based on the status of the instance.

**Cold Migration**: migrates instances that are in the **Pending** or **Shutted** state.

| Section | Parameter | Description |
|---|---|---|
| Instance Informatio n | Select Instance | The ID of the instance to be migrated is automatically displayed in the Instance ID drop-down list. You need to select this instance in the instance list below. You can also specify the ID of another instance based on your business requirements. Important You can select only one ECS instance. |

O&M

| Destination Selection | Destination Selection Policy | Random Selection (default): migrates the instance to a random physical machine that has sufficient resources. System Recommendation: migrates the instance to a recommended physical machine that ensures a high success rate of migration. Important If no data is displayed in the host list, no physical servers are recommended. We recommend that you select another policy. Specify NC: migrates the instance to a specific physical machine. To specify the destination physical machine, search for physical machines by cluster, hostname, server IP address, or server ID, and then select the physical machine to which you want to migrate the instance. Note The system provides suggestions on each physical machine only for reference. You can select a physical machine that is not recommended based on your business requirements. Specify Cluster: migrates the instance to a specific cluster. To specify the destination cluster, search for the cluster by name, and then select it in the cluster list below. Note The system provides suggestions on each cluster only for reference. You can select a cluster that is not recommended based on your business requirements. |
|---|---|---|
|   | Recovery Mode | The state that you want the instance to enter after migration. Valid values: Start after Migration Stop After Migration |
| Operation Informatio n | Reason | The reason for cold migration. |

**Hot Migration**: migrates instances that are in the **Running** state.

| Section | Parameter | Description |
|---|---|---|

O&M

| Instance Information | Select Instance | The ID of the instance to be migrated is automatically displayed in the Instance ID drop-down list. You need to select this instance in the instance list below. You can also specify the ID of another instance based on your business requirements. Important You can select only one ECS instance. |
|---|---|---|
| Basic Migration Parameters | Migration Rate | The migration rate. Unit: Mbit/s. We recommend that you enter a value that is greater than 500. |
|   | Enhanced Hot Migration Compatibility | Specifies whether to enable the enhanced hot migration compatibility. If you set this parameter to Yes, you can migrate the ECS instances to an available physical machine with a different CPU model. Important After you set this parameter to Yes and set the Destination Selection Policy parameter to System Recommendation, the available physical servers with different CPU models are additionally displayed. |

O&M

| Destination Selection |   |   |
|---|---|---|
|   | Destination Selection Policy | Random Selection (default): migrates the instance to a random physical machine that has sufficient resources. System Recommendation: migrates the instance to a recommended physical machine that ensures a high success rate of migration. Important If no data is displayed in the host list, no physical servers are recommended. We recommend that you select another policy. Specify NC: migrates the instance to a specific physical machine. To specify the destination physical machine, search for physical machines by cluster, hostname, server IP address, or server ID, and then select the physical machine to which you want to migrate the instance. Note The system provides suggestions on each physical machine only for reference. You can select a physical machine that is not recommended based on your business requirements. Specify Cluster: migrates the instance to a specific cluster. To specify the destination cluster, search for the cluster by name, and then select it in the cluster list below. Note The system provides suggestions on each cluster only for reference. You can select a cluster that is not recommended based on your business requirements. |

O&M

| Advanced Migration Parameters Note You can configure advanced parameters based on your business requirements to increase the success rate of migration. You can also click Configuratio n Description to view the description of the parameters in this section. | Allowed Service Interruption Duration | The service interruption duration in the last phase of hot migration. Unit: milliseconds. Valid values: 200 to 2000. Default value: 300. |
|---|---|---|
|   | Check SLB | Valid values: Yes: checks whether Server Load Balancer (SLB) instances are associated with the ECS instance. If the ECS instance is associated with SLB instances, the migration task may fail. No: does not check whether the ECS instance is associated with SLB instances. Default value: Yes. |
|   | Check AVS Version | Valid values: Yes: checks whether the AVS versions of the source and destination hosts are the same. If the AVS versions are different, the migration task fails. No: does not check the AVS versions of the source and destination hosts. Default value: Yes. |
|   | Check Virtual NC Version | Valid values: Yes: checks whether the virtualization version of the destination host supports hot migration. If the virtual version of the destination server does not support hot migration, the migration task fails. No: does not check the virtualization version of the destination host. Default value: Yes. |
|   | Allow Reserved NC | Valid values: Yes: allows the ECS instance to be migrated to a reserved host. No: does not allow the ECS instance to be migrated to a reserved host. Default value: No. |

O&M

|   | Check CPU Tag | Valid values: Yes: checks whether the CPU tag set of the source host is a subset of the CPU tag set of the destination host. If the CPU tag set of the source host is not a subset of the CPU tag set of the destination host, the migration task fails. No: does not check the CPU tag set of the source host. Default value: Yes. |
|---|---|---|
| Operation Information | Reason | The reason for hot migration. |

3. Select **I have read the preceding notes and confirm this operation.** and click
**Submit**。

**View the migration history of an instance**

You can view the historical migration tasks that are created during the lifecycle of an ECS instance.
1. On the ECS Instances page, find the instance that you want to manage, move the pointer
over **Migrate** in the **Operation** column, and then select **Migration Logs in Server**
**Controller**.
2. In the **Migration History** panel, view the historical migration tasks displayed on the Cold
Migration and Hot Migration tabs. On the **Cold Migration** tab, view the information about each cold migration task, including **Source NC**, **Destination NC**, **Status**, **Migration Time**, **End Time**, and
**Migration Reason**.
On the **Hot Migration** tab, view the information about each hot migration task, including
**Source NC**, **Destination NC**, **Status**, **Migration Time**, **Update Time**, **Migration**
**Rate**, and **Migration Reason**.

**View operation records of an instance**

**Background information**

During the O&M process of an ECS instance, the system audits risky operations that are performed on the instance and allows you to view the audit details. O&M
1. On the ECS Instances page, find the instance that you want to manage and click **Audit**
**Operations** in the **Operation** column.
2. In the **Audit Operations** panel, view the operation records of the ECS instance. For more
information, see O&M audit logs.

**Start one or more instances**

**Background information**

If an ECS instance is in a state in which the instance cannot provide services, such as the Shutted state, you must start the instance before you can use it.

**Prerequisites**

The instance to be started is in the **Pending**, **Shutted**, or **ShutFailure** state.
1. On the ECS Instances page, find the instance that you want to start, move the pointer over
the icon in the **Operation** column, and then select **Start**. You can also select multiple instances and click **Start** in the lower part of the page. This way, multiple instances are started at a time.
2. In the dialog box that appears, confirm the instance ID, enter a reason, and then click **OK**.

**Stop one or more instances**

O&M

**Background information**

You can stop an instance that is not in use.

**Prerequisites**

The instance to be stopped is in the **Running** state.

> **Important:** After you stop an instance, the applications running on the instance are interrupted. Make sure that you stop an instance during off-peak hours to minimize the impact on services.

1. On the ECS Instances page, find the instance that you want to stop, move the pointer over
the icon in the **Operation** column, and then select **Stop**. You can also select multiple instances and click **Stop** in the lower part of the page. This way, multiple instances are stopped at a time.
2. In the dialog box that appears, confirm the instance ID, enter a reason, and then click **OK**.

**Restart one or more instances**

**Background information**

After you change the logon password of an instance or install system updates, you must restart the instance.

**Prerequisites**

The instance to be restarted is in the **Running** state.

> **Warning:** After you restart an instance, the instance is stopped for a short period of time and the services that are running on the instance are interrupted. Proceed with caution.

1. On the ECS Instances page, find the instance that you want to restart, move the pointer
over the icon in the **Operation** column, and then select **Restart**. O&M You can also select multiple instances and click **Restart** in the lower part of the page. This way, multiple instances are restarted at a time.
2. In the dialog box that appears, confirm the instance ID, configure the **Restart Mode** and
**Reason** parameters, and then click **OK**.

**Manage ISOs**

**Background information**

You can mount an ISO to or unmount an ISO from an instance. After you mount an ISO to an instance, the system enters the rescue mode and performs operations on the instance.

**Prerequisites**

ISOs can be mounted to or unmounted from instances that are in the **Shutted** state.
1. On the ECS Instances page, find the instance that you want to manage, move the pointer
over the icon in the **Operation** column, and then click **Manage ISO**.
2. In the **Manage ISO** dialog box, mount or unmount an ISO based on your business
requirements. O&M Mount an ISO: a. In the **Available ISOs** section, find the ISO that you want to mount and click **Mount** in the **Operation** column. b. In the dialog box that appears, enter the operator name, ticket title, and reason for the operation. c. Click **OK**. The mounted ISO is displayed in the **Mounted ISOs** section. Unmount an ISO a. In the **Mounted ISOs** section, find the ISO that you want to unmount and click
**Uninstall** in the **Operation** column.
b. In the dialog box that appears, enter the operator name, ticket title, and reason for the operation. c. Click **OK**. The unmounted ISO is displayed in the **Available ISOs** section.

##### 1.1.4.2 Disks

You can attach disks to Elastic Compute Service (ECS) instances to increase the storage space of the ECS instances. This topic describes how to query and view disk details and perform O&M operations on disks. O&M

**View disk and O&M details**

1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Computing** > **Compute**
3. In the left-side navigation pane, choose **ECS O&M** > **Disk**.
4. In the upper part of the Disks page, configure the **Disk ID**, **Disk Type**, **Status**, and **ECS**
**Instance** parameters to filter disks. You can also select **All in ECS Project** in the upper-
right corner of the page to filter disks.
5. View disk information in the columns, including **Disk ID/Name**, **Disk Type**, **Capacity**, **ECS**
**Instance**, **Mount Point**, **Cluster**, **Status**, **Disk Category**, **Disk ID in Server Controller**,
**Apsara Stack Tenant Account ID**, and **Creation Time**.

> **Note:** Disk types include system disk and data disk.
> Disk categories include local disk, local SSD, basic disk, standard SSD, preconfigured SSD, ultra disk, Enterprise SSD (ESSD), premium performance disk, and standard performance disk.

When a disk is created, a unique ID is generated for the disk. This ID is only used in the Server Controller database for ECS.
6. View the details of a disk.
i. Find the disk that you want to view and click the disk ID in the **Disk ID/Name** column. ii. In the upper-right corner of the Disk Details page, click the buttons to perform operations on the disk. For more information, see the What to do next section of this topic. O&M iii. View the details of the disk on the **Disk Details** page.

| Section | Description |
|---|---|
| Basic Information | This section includes the following parameters: Disk ID, Disk ID in Server Controller, Disk Name, Disk Type, Disk Category, Disk Capacity, Mount Point, Creation Time, Attachment Time, Detachment Time, Modification Time, Region, Zone, Cluster, and Apsara Stack Tenant Account ID. |
| Snapshot Information | This section includes the Automatic Snapshot Policy ID parameter. |

7. View the details of an ECS instance to which the disk is attached.
i. On the Disks page, find the disk that is attached to an ECS instance and click the ID of the ECS instance in the **ECS Instance** column. O&M ii. View the instance details on the **Instance Details** page. For more information, see the "View the details of an instance" section of the View the details of an instance. In the instance list, find the ECS instance that you want to view and click its ID in the Instance ID/Name column. On the instance details page, you can click buttons in the upper-right corner to perform various operations on the ECS instance. For more information, see the section of this topic. For information about how to log on to the cluster Admin Gateway (AG), see the Log on to the AG of a cluster section of the "Computing cluster O&M" topic. View the following information on the instance details page. Section or tab Description Basic Information This section displays the basic information about the ECS instance, including Instance ID, Instance Name, Specifications, Region, Zone, Creation Time, Apsara Stack Tenant Account ID, State in Business Foundation System, State in Server Controller, Cluster, Host ID, Host, and Rack. Configurations This section displays the configuration information about the ECS instance, including I/O Optimized, System Image, Operating System, System Disk, Network Type, Internal Bandwidth, Private IP Address, RDMA IP, VPC ID, vSwitch, and NAT IP Address. Disks View the list of disks and the disk information, including Disk ID, Disk Type, Status, Cluster, and Feature. View the details of a disk. Perform various operations on a disk by clicking buttons in the Operation column, including Detatch, Audit Operations, Create Snapshot, and View Snapshots. For more information, see the section of the "Disks" topic. ENIs View the information about the elastic network interfaces (ENIs) that are bound to the ECS instance. The information includes ENI ID/MAC Address, Status, ENI Type, vSwitch, and IP. View the details of an ENI. Perform various operations on an ENI by clicking buttons in the Operation column, including Unbind and Operation Audit. For more information, see the View operation records section of the "ENIs" topic. Security Groups View the information about the security group to which the ECS instance belongs. The information includes Security Group ID/Name, Network Type, VPC ID, and Creation Time. View the details of a security group. View operation records of a security group by clicking Audit Operations in the Operation column. For more information, see Security groups. Snapshots View the list of snapshots and the snapshot information, including Snapshot ID/Name, Snapshot ID in Server Controller, Snapshot Type, Disk ID/Type, Progress, and Creation Time. View the details of a snapshot. Perform various operations on a snapshot by clicking buttons in the Operation column, including Delete, Audit Operations, and Create Image. For more information, see . Performance Monitoring You can specify a time range and view the charts that describe the instance performance within the specified period of time. The performance metrics include CPU utilization, disk read/write (byte/s), disk IOPS, public bandwidth (bit/s), and internal bandwidth (bit/s). ASO Migration Tasks After a migration task is triggered in the Apsara Uni-manager Operations Console, you can view the status and result of the migration task on this tab. You can view the task information including Task ID, Source NC ID and IP Address, Destination NC ID and IP Address, Task Type, Retries, Task Status, Start Time, Migration Reason, Operator, and Migration Task Result. Valid values of the Task Type parameter are Cold Migration and Hot Migration. The value of the Retries parameter is a ratio of the number of executed retries to the maximum number of retries. Migration History View the historical migration tasks that are created within the lifecycle of the ECS instance. Both cold migration and hot migration tasks are displayed. You can view the information about each migration task, including Source NC, Destination NC, Status, Migration Time, End Time, and Migration Reason. Audit Operations View the operation records of the ECS instance on the Operations in the Apsara Uni-manager Operations Console, POP API Calls, and Server Controller API Calls subtabs. For more information, see . Associate Resources View the topology that shows the relationships among the ECS instance and its associated resources. The resources include account, VPC, VM, computing server, cluster, image, data disk, system disk, network interface card (NIC), and security group. You can move the pointer over a resource to view the details of the resource. topic.
8. View the details of the cluster to which the disk belongs.
i. On the Disks page, find the disk and click the cluster name in the **Cluster** column. ii. View the cluster details on the **Computing Cluster Details** page. For more information, see the "View the O&M details of a compute cluster" section of the View the O&M details of a computing cluster. On the Computing Cluster O&M page, click the name of the O&M cluster that you want to view to go to the Computing Cluster Details page. On the Overview tab, view the information about computing servers and ECS instances in the cluster. In the Cluster Information section, view the basic information of the cluster, including the region in which the cluster is deployed, cluster type, whether the cluster uses only ECS resources, zone, cluster ID, instance family, cluster status, network type, physical network, disk type, and cluster specifications. In the upper-right corner of this section, click Connect to Cluster AG to log on to the Admin Gateway (AG). For more information, see the Log on to the AG of a cluster section of this topic. In the Server Resources section, view the number of computing servers, the number of CPUs, and the amount of available memory. In the ECS Instances section, view the total number of ECS instances, the number of ECS instances that are running, and the number of abnormal ECS instances. In the NC State Distribution section, view the distribution of physical machines in different states. Move the pointer over the chart. The number of physical machines in each state is displayed. The following table describes the states of physical machines. State Description Failover The physical machine is down. Normal The physical machine runs as expected. You can schedule instances to the physical machine. No heartbeat The physical machine has no heartbeats. Mlock The physical machine is manually locked. Rlock The physical machine is forcefully reserved and can be used to recover or modify VMs. If the resources of the physical machine are insufficient, the physical machine performs defragmentation. Otherwise, an alert is triggered. The physical machine must have heartbeats and remain available. Initializing The physical machine is being initialized. All the virtual private cloud (VPC) configurations of the physical machine are being reissued by the RegionMaster. In the ECS Instance State Distribution section, view the distribution of ECS instances in different states. The following table describes the states of ECS instances. State Description Running The instance runs as expected. Stopped After an instance is stopped or after an instance is created but not started, the instance is in the Stopped state. Instances in the Stopped state cannot provide external services. Pending After an instance is created, the instance is in the Pending state before it enters the Running state. If the instance remains in the Pending state for an extended period of time, an exception occurs. Creating After you start or restart an instance in the ECS console or by calling an API operation, the instance enters the Creating state before it enters the Running state. If the instance remains in the Creating state for an extended period of time, an exception occurs. Stopping After you stop an instance in the ECS console or by calling an API operation, the instance enters the Stopping state before it enters the Stopped state. If the instance remains in the Stopping state for an extended period of time, an exception occurs. Releasing After you release an instance, the instance enters the Releasing state before it enters the Released state. In the Inventory Utilization section, view the total amount of resources, the amount of used resources, and the percentage of used resources in all resources. In the Inventory section, view the inventory details of the instance types in the cluster. Click the Configurations tab. On this tab, you can configure the CPU oversold ratio and view its configuration records. For more information, see Configure CPU oversold ratios. Click the Computing Servers tab. View information about the computing servers in the cluster in the following columns: Hostname, IP Address, NC ID, NC Type, vCPU (Cores), Memory, Service State, Instances, Data Center, Rack, and SN. For more information about valid values of the Service State parameter, see the table describing the states of physical machines of this topic. View the O&M details of a computing server. Find the computing server that you want to view and click the server name in the Hostname column. On the Computing Server Details page, view the O&M details of the computing server. For more information, see the 6. View the O&M details of a computing server. section of the "Computing server O&M" topic. View the details of ECS instances that are deployed on a computing server. Find the computing server that you want to view and click the number in the Instances column. In the Instance List panel, view the instance information in the following columns: Instance ID, Status, Instance Name, CPU, and Memory. Click an instance ID in the Instance ID column. The Instance Details page of the ECS instance appears. For more information, see . Manage the service states of the computing servers in the cluster. The following table describes the operations that you can perform on computing servers. Operation Scenario Procedure Lock NC You can lock abnormal servers to prevent instances from being scheduled to these servers. If the servers are locked, the O&M status of the servers cannot be automatically changed. You can also lock servers for which you want to reserve resources. On the Computing Servers tab, find the server that you want to lock and click Lock NC in the Operation column. In the Lock NC dialog box, confirm the server information, select a lock state, and then configure the Changed By, Change Ticket Title, and Reason parameters. Click OK. Unlock NC You can unlock servers in the no heartbeat, mlock, and rlock states. After you unlock a server, the server is automatically activated and you can schedule instances to the server. On the Computing Servers tab, find the server that you want to unlock and click Unlock NC in the Operation column. In the Unlock NC dialog box, confirm the server information and enter the reason for unlocking the server. Click OK. Activate You can activate servers in the no heartbeat, mlock, rlock, failover, and initializing states. On the Computing Servers tab, find the server that you want to activate and click Activate in the Operation column. In the dialog box that appears, enter a reason for activating the server, the user who performed the operation, and a ticket title in the Reason field. Click OK. topic

**What to do next**

**Use the operation audit feature**

**Background information**

You can use the operation audit feature to view the operation records of a disk.
1. On the Disks page, find the disk whose operation records you want to view and click **Audit**
**Operations** in the **Operation** column.
2. In the **Audit Operations** panel, view the information about the operations performed on
the disk. For more information, see View O&M audit logs.

**Create a snapshot for a disk**

**Background information**

You can use snapshots to back up data, restore ECS instances that were accidentally released, and create custom images. Before you roll back disks, modify critical system files, or change the operating system of an instance, you can create snapshots for disks to improve fault tolerance.

**Precautions**

You can create snapshots only for disks that are attached to instances in the Stopped or Running state. You cannot create snapshots for disks attached to instances that have not been started. O&M If you create a snapshot for a new system disk or a new data disk created from another snapshot, an error is returned because the process of loading data to the disk is not complete. In most cases, you can create snapshots for a system disk one hour after the system disk is created. After a data disk is attached, you must wait for a period of time before you can create snapshots for the data disk. The amount of time that you need to wait varies based on the amount of the disk data. You cannot create snapshots for a new disk if the instance to which the disk is attached has not been started. If the creation progress has not reached 100%, the snapshot is being created. In this case, you cannot create another snapshot for the disk. The snapshot quota depends on the total number of disks that are available within your account. The maximum number of snapshots you can create = The number of disks × 6 + 6. You can create snapshots for a disk only after the instance to which the disk is attached has been started. An error is returned if you create a snapshot for an independent basic disk that has never been attached to an instance.
1. On the Disks page, find the disk for which you want to create a snapshot and click **Create**
**Snapshot** in the **Operation** column.
2. In the **Create Snapshot** dialog box, check the disk ID, configure the parameters that are
described in the following table, and then click **OK**.

| Parameter | Description |
|---|---|

O&M

| Snapshot Name | The name of the snapshot. Note The name must be 2 to 128 characters in length and can contain letters. The name must start with a letter and cannot start with http:// or https://. The name can contain digits, colons (:), underscores ( ), and _ hyphens (-). The name cannot start with auto because snapshots whose names start with auto are recognized as automatic snapshots. |
|---|---|
| Snapshot Description | The description of the snapshot. Note The description can be up to 256 characters in length. If you do not configure this parameter, it is left empty by default. The description cannot start with http:// or https://. |
| Description | The reason for creating the snapshot. You can create the snapshot to generate audit logs for troubleshooting and tracing. |

**View disk snapshots**

**Background information**

You can view the snapshots of disks, manage snapshots, and view automatic snapshot policies.
1. On the Disks page, find the disk whose snapshots you want to view and click **View**
**Snapshots** in the **Operation** column.
2. View the snapshots and automatic snapshot policies on the **Snapshots** page. For more
information, see Snapshots.

##### 1.1.4.3 Images

An image is a template for running environments within Elastic Compute Service (ECS) instances. An image includes an operating system and pre-installed applications. An image works as a copy that stores data from one or more disks. An ECS image may store data from a system disk or from both system and data disks. You can use an image to create an ECS instance or replace the system disk of an ECS instance. O&M
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Computing** > **Compute**
3. In the left-side navigation pane, choose **ECS O&M** > **Image**.
4. On the **Images** tab, view the image details.
In the upper part of the tab, you can filter images by **image ID** and **image type**

> **Important:** If you set the **Image Type** parameter to **Custom Image**, you must select an account from the **Apsara Stack Tenant Account ID** drop-down list.

The image information is displayed in the following columns: **Image ID**, **Capacity**,
**Status**, **Region**, **Image Type**, and **Apsara Stack Tenant Account ID**.
5. On the **ISOs** tab, view the ISO details.
In the upper part of the tab, you can enter an ISO name to search for the ISO. The ISO information is displayed in the following columns: **Parameter**, **System Type**, and **Status**.

##### 1.1.4.4 Snapshots

Snapshots provide data protection for disks. When a disk fails due to reasons such as virus infection, misconfiguration, and accidental deletion of data, you can restore disk data from a snapshot of the disk.

**Scenarios**

You can use snapshots to back up data, restore Elastic Compute Service (ECS) instances that were accidentally released, and create custom images. Before you roll back disks, modify critical system files, or change the operating system of an instance, you can create snapshots for disks to improve fault tolerance.

**View snapshots**

1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Computing** > **Compute**
3. In the left-side navigation pane, choose **ECS O&M** > **Snapshots**.
O&M
4. On the **Snapshots** tab, select an account from the **Apsara Stack Tenant Account ID**
drop-down list to view all the snapshots that are created within the account. In the upper part of the Snapshots tab, filter snapshots by **Apsara Stack Tenant**
**Account ID**, **Snapshot ID**, **Disk ID**, and **Instance ID**.

> **Note:** You must select an account from the **Apsara Stack Tenant Account ID** drop-down list.

View the information about snapshots in the following columns: **Snapshot ID/Name**,
**Snapshot ID in Server Controller**, **Snapshot Type**, **Disk ID/Type**, **Progress**,
**Region**, **Creation Time**, and **Modification Time**.
**Snapshot ID in Server Controller**: the unique ID that is generated for a
snapshot when the snapshot is created. This ID is only used in the Server Controller database for ECS.

> **Snapshot Type**: the type of a snapshot, which can be system snapshot, user snapshot, scheduled snapshot, or snapshot copy.

Find the snapshot whose disk you want to view and click the disk ID in the **Disk ID/Type** column. Then, view the information displayed on the **Disk Details** page. For more information, see the 5. View the details of a disk. section of the “Disks” topic.
5. On the **Automatic Snapshot Policies** tab, view the information about each automatic
snapshot policy, including the policy ID, policy name, and number of associated disks. O&M

> **Note:** You can apply automatic snapshot policies to system disks and data disks to automatically create snapshots of the disks on a regular basis. This prevents the risks that may arise if you manually create snapshots. Examples:
> When applications, such as personal websites or databases, that are deployed on an ECS instance encounter attacks or system vulnerabilities, you may be unable to manually create snapshots for disks on the instance. In this case, you can use the most recent automatic snapshots created by automatic snapshot policies to roll back the affected disks. This helps restore your data and reduce loss.
> You can configure an automatic snapshot policy to create snapshots before regular system maintenance tasks are performed. This eliminates the need to manually create snapshots and helps ensure that snapshots are always created before maintenance.

**Delete a snapshot**

**Prerequisites**

If a snapshot has been used to create custom images, you must delete those custom images before the snapshot can be deleted.
1. On the **Snapshots** tab, find the snapshot that you want to delete and click **Delete** in the
**Operation** column.
2. In the dialog box that appears, enter a reason and click **Delete**.

**View operation records of a snapshot**

**Background information**

This section describes how to view the audit logs of snapshots.
1. On the **Snapshots** tab, find the snapshot that you want to manage and click **Audit**
**Operations** in the **Operation** column.
2. In the **Audit Operations** panel, view the operation records of the snapshot. For more
information, see O&M audit logs. O&M

**Create an image**

**Background information**

You can create a custom image and use it to create identical instances or replace the system disks of existing instances. This way, you can manage multiple instances that have the same operating system and data environment.

**Prerequisites**

The progress of the snapshot is 100%. The disk of the snapshot is a system disk.
1. On the **Snapshots** tab, find the snapshot that you want to manage and click **Create**
**Image** in the **Operation** column.
2. In the **Create Image** dialog box, configure the parameters and click **OK**. The following
table describes the parameters. O&M

| Parameter | Description |
|---|---|
| Image Name | The name of the image. Note The name must be 2 to 128 characters in length and can contain letters. The name must start with a letter and cannot start with http:// or https://. |
| Image Description | The description of the image. Note The description can be up to 256 characters in length. If you do not set this parameter, it is left empty by default. The description cannot start with http:// or https://. |
| Reason | The reason for creating the image. This parameter facilitates troubleshooting and tracing based on the generated audit logs. |

##### 1.1.4.5 ENIs

An elastic network interface (ENI) is a virtual network interface controller (NIC) that can be bound to an Elastic Compute Service (ECS) instance in a virtual private cloud (VPC). You can use ENIs to deploy high availability clusters, implement fine-grained network management, and perform failovers at low costs.

**View ENIs and their details**

1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Computing** > **Compute**
3. In the left-side navigation pane, choose **ECS O&M** > **ENIs**.
4. On the ENIs page, search for ENIs by **Apsara Stack Tenant Account ID**, **ENI ID**, **VPC**,
**Instance ID**, **Private IP Address**, or their combinations.
O&M

> **Note:** You must select a value from the **Apsara Stack Tenant Account ID** drop-down list.

5. View the information about each ENI in the following columns: **ENI ID**, **Status**, **Zone**,
**Instance ID**, **ENI Type**, **MAC Address**, and **Creation Time**.
6. View the details of an ENI.
i. In the ENI list, find the ENI that you want to view and click its ID in the **ENI ID** column. ii. On the ENI Details page, you can perform operations on the ENI. For more information, see the View operation records section of this topic. iii. On the **ENI Details** page, view the details of the ENI.

| Section | Description |
|---|---|
| Basic Information | Displays the basic information about the ENI, including ENI ID, ENI Type, Status, ENI Name, VPC, vSwitch, Private IP Address, Public IP Address, IPV6, MAC Address, and Instances. |
| Business Information | Displays the business information about the ENI, including Region, Zone, and Apsara Stack Tenant Account ID. |
| VPort Information | Displays the VPort Name, VPC, vSwitch, and Status information. |

O&M

| Security Groups | View the security groups to which the ENI belongs. The security group information includes Security Group ID/Name, Network Type, VPC ID, Associated Instances, and Creation Time. View the details of a security group. Click the security group ID in the Security Group ID/Name column to go to the security group details page. For more information, see the View security groups and their details section of the "Security groups" topic. View the ECS instances with which the security group is associated. Click the value in the Associated Instances column to go to the ECS Instances page. For more information, see ECS instances. View the operation records of a security group. ClickA udit Operations in the Operation column. In the Audit Operations panel, view the detailed information. For more information, see O&M audit logs. |
|---|---|

7. View the details of the ECS instance to which an ENI is bound.
i. In the ENI list, click the ID in the **Instance ID** column of an ENI. ii. On the **Instance Details** page, view the details of the ECS instance. For more information, see the View ECS instances and instance details section of the "ECS instances" topic.

**View operation records**

1. In the ENI list, click **Audit Operations** in the **Operation** column of an ENI.
2. In the **Audit Operations** panel, view the operation records of the ENI. For more
information, see O&M audit logs.

##### 1.1.4.6 Security groups

A security group acts as a virtual firewall to control the inbound and outbound traffic of Elastic Compute Service (ECS) instances to improve security. Security groups provide state inspection and packet filtering capabilities. You can use security groups and security group rules to define security domains in the cloud.

**View security groups and their details**

1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Computing** > **Compute**
3. In the left-side navigation pane, choose **ECS O&M** > **Security Groups**.
O&M
4. In the upper part of the Security Groups page, filter security groups by **Security Group ID**,
**ECS Instance ID**, and **Apsara Stack Tenant Account ID**.

> **Note:** You must select an account from the **Apsara Stack Tenant Account ID** drop-down list.

5. View the information about security groups in the following columns: **Security Group**
**ID/Name**, **Region**, **Network Type**, **VPC ID**, and **Creation Time**.
6. View the details of a security group.
i. On the Security Groups page, find the security group that you want to view and click its ID in the **Security Group ID/Name** column. ii. On the Security Group Details page, view the details of the security group. In the **Basic Information** section, view the basic information about the security group, including the security group ID, virtual private cloud (VPC), description, creation time, and modification time. On the **Rules** tab, click the **Inbound** and **Outbound** tabs to view the inbound and outbound rules of the security group. The following table describes the parameters on the Rules tab.

| Parameter | Description |
|---|---|
| Rule direction | Outbound: access from ECS instances in the security group to other ECS instances on the internal network or to resources on the Internet. Inbound: access from other ECS instances on the internal network or from resources on the Internet to ECS instances in the security group. |

O&M

| Action | Accept: allows access requests on a specific port. Drop: denies access requests on a specific port and drops data packets without returning a response. If an Accept rule and a Drop rule differ only in the action, theD rop rule takes precedence over the Accept rule. |
|---|---|
| NIC Type | The network interface card (NIC) type of the security group rule. Only a value of intranet is supported, which indicates internal NICs. No public NICs are available in ECS instances that are deployed in VPCs. You can add only internal security group rules. However, the added rules take effect on traffic that is sent over the Internet and the internal network. |
| Protocol Type | The protocol type of the security group rule. Valid values: All: This value can be used in full-trust scenarios. TCP: This value can be used to allow or deny traffic on one or more successive ports. UDP: This value can be used to allow or deny traffic on one or more successive ports. ICMP: This value can be used when the ping command is used to test network connectivity between instances. ICMPv6: This value can be used when the ping6 command is used to test network connectivity between instances. GRE: This value can be used for VPN. |
| Authorized Object | Authorization objects vary based on the authorization type. |
| Port Range | The port range varies based on the protocol type. If the value of the Protocol Type parameter isA ll, the value -1/-1 is displayed, which indicates all ports. If the value of the Protocol Type parameter isT CP, you can specify a port range in the <Start port>/<End port> format. Valid values of port numbers: 1 to 65535. For example, 80/80 indicates port 80 and 1/22 indicates ports 1 to 22. If the value of the Protocol Type parameter isU DP, you can specify a port range in the <Start port>/<End port> format. Valid values of port numbers: 1 to 65535. For example, 80/80 indicates port 80 and 1/22 indicates ports 1 to 22. If the value of the Protocol Type parameter isI CMP, the value -1/-1 is displayed, which indicates all ports. If the value of the Protocol Type parameter isI CMPv6, the value -1/-1 is displayed, which indicates all ports. If the value of the Protocol Type parameter isG RE, the value -1/-1 is displayed, which indicates all ports. |
| Priority | The priority of the security group rule. Valid values: 1 to 100. Default value: 1. A value of 1 indicates the highest priority. |

O&M

| Description | The description of the security group rule. To facilitate rule management, we recommend that you provide a description. The description must be 1 to 512 characters in length. |
|---|---|

On the **Instances** tab, view the ECS instances that are associated with the security group. For more information, see ECS instances.

**View operation records of a security group**

1. Find the security group that you want to manage and click **Audit Operations** in the
**Operation** column.
2. In the **Audit Operations** panel, view the operation records of the security group. For more
information, see O&M audit logs.

##### 1.1.4.7 Instance type management

On the Specifications page, you can query and manage Elastic Compute Service (ECS) instance types. You can also create custom instance types if existing instance types cannot meet your business requirements.

**Create a custom instance type**

**Background information**

|   | Instance family.c(Number of CPU cores)m(Memory |
|---|---|
| XXX |   |

You can specify the instance type name, number of vCPUs, and memory size. Parameter settings such as the bandwidth, packet forwarding rate, and network interface controller (NIC) multi-queue are automatically specified by the system.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Computing** > **Compute**
3. In the left-side navigation pane, choose **ECS O&M** > **Specifications**.
O&M
4. On the Specifications page, click the **Custom Instance Type** tab. On the Custom Instance
Type tab, click **Create Instance Type**. On the Create Custom Instance Type page, configure the parameters that are described in the following table and click **Create**.

> **Note:** After a custom instance type is created, the instance type does not immediately take effect. You need to wait until the system synchronizes the operation.

| Parameter | Description |
|---|---|
| Instance Family | The instance family of the custom instance type. Instance types that you can select vary based on the region that you select and the resource inventory in the region. |
| Instance Type Name | The name of the custom instance type. The name must be in lowercase and can contain up to 10 lowercase letters. |
| CPU Cores (vCPUs) | The number of vCPUs, which is a variable in the parameter settings. Set the value to 1 or an even number that is greater than 1. Note The number of vCPUs cannot be greater than the maximum number of CPU cores of the physical server. Otherwise, the instance type cannot be created. |

O&M

| Memory (GB) | The virtual memory size, which is a variable in the parameter settings. Set the value to 1 or an even number that is greater than 1. Note The virtual memory size cannot be greater than the maximum memory size of the physical server. Otherwise, the instance type cannot be created. |
|---|---|
| GPUs | The number of GPUs. This parameter takes effect only when you select a GPU-accelerated instance family. Valid values: 0, 1, 2, 3, 4, and 8. |
| GPU Specification | The GPU specification. This parameter takes effect only when you select a GPU-accelerated instance family. You can view the parameter but cannot modify the parameter. |
| Local Disks | The number of local disks. This parameter takes effect only when you select an instance family with local SSDs. Set the value to 0, 1, or an integer greater than 1. |
| Available Capacity per Local Disk (GB) | The available capacity per local SSD. This parameter takes effect only when you select an instance family with local SSDs. You can view the parameter but cannot modify the parameter. |
| Local Disk Category | The type of the local SSDs. This parameter takes effect only when you select an instance family with local SSDs. You can view the parameter but cannot modify the parameter. |
| Max Disks | The maximum number of disks that can be attached to an instance of the instance type. You can view the parameter but cannot modify the parameter. |
| Max ENIs | The maximum number of elastic network interfaces (ENIs) that can be attached to an instance of the instance type. You can view the parameter but cannot modify the parameter. |
| Max Network Bandwidth (Gbit/s) | The maximum bandwidth of the instance type. The value is automatically generated after you configure the CPU Cores (vCPUs) parameter. You can modify the parameter. |
| Packet Forwarding Rate (10,000 PPS) | The packet forwarding rate. The value is automatically generated after you configure the CPU Cores (vCPUs) parameter. You can modify the parameter. |
| Reason | The reason for this operation. |

O&M
5. Return to the Custom Instance Type tab. On the Custom Instance Type tab, find the custom
instance type that you created in the previous step and click **Creating** in the **Status** column. In the Progress panel, view the creation progress of the custom instance type.

**View an instance type**

**Usage notes**

On the All Specifications tab, you can manage all standard instance types and custom instance types in the region, but you cannot manage dedicated host types. Instance types that are available for Tiangong products and instance types that are out of stock are unavailable in the Apsara Uni-manager Management Console regardless of whether the instance types are in the **Enabled** state. After you enable or disable an instance type, do not perform operations on the instance type until the state of the instance type changes to **Enabled** or **Disabled**.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Computing** > **Compute**
3. In the left-side navigation pane, choose **ECS O&M** > **Specifications**.
4. On the **All Specifications** tab of the Specifications page, select an instance family from
the **Instance Family** drop-down list and enter an instance type name in the **Instance**
**Type Name** field to search for the instance type.
5. View the information about the instance type in the following columns: **Instance Type**
**Name**, **Instance Family**, **Status**, **CPU Cores (vCPU)**, **Memory (GB)**, **Max Disks**, **Max**
**ENIs**, **Max Network Bandwidth (Gbit/s)**, and **Packet Forwarding Rate (10,000 PPS)**.
6. Click **Details** in the **Operation** column of the instance type. In the Instance Type Details
panel, view the basic information and extended attributes of the instance type.

**Enable an instance type**

1. On the All Specifications tab of the Specifications page, find the instance type that you want
to enable and click **Enable** in the **Operation** column.
2. In the dialog box that appears, enter a reason for the operation in the **Reason** field and
click **OK**.

> **Note:** You can enable only an instance type in the **Disabled** state.
> After you enable an instance type, 30 to 60 minutes are required for the change to take effect.

3. Click **Enabling** in the **Status** column of the instance type. In the Progress panel, view the
enabling progress.

**Disable an instance type**

O&M
1. On the All Specifications tab of the Specifications page, find the instance type that you want
to disable and click **Disable** in the **Operation** column.
2. In the dialog box that appears, enter a reason for the operation in the **Reason** field and
click **OK**.

> **Note:** You can disable only an instance type in the **Enabled** state.
> After you disable an instance type, 30 to 60 minutes are required for the change to take effect.

3. Click **Disabling** in the **Status** column of the instance type. In the Progress panel, view the
disabling progress.

**View operation records of an instance type**

1. On the All Specifications tab of the Specifications page, find the instance type whose
operation records you want to view and click **Operation Records** in the **Operation** column.
2. In the Operation Records panel, view the information on the **Operations in the Apsara**
**Uni-manager Operations Console** and **POP API Calls** tabs.
On the **Operations in the Apsara Uni-manager Operations Console** tab, view the operation information, including the resource on which the operation was performed, operation, operation time, operation result, error information, request ID, request parameters, and operator. On the **POP API Calls** tab, view the operation information, including operation, operation time, request ID, HTTP status code, error information, service, request parameters, and operator.

##### 1.1.4.8 O&M audit logs

You can view the historical operations that are performed on Elastic Compute Service (ECS) resources in the Apsara Uni-manager Operations Console, historical pctowap open platform (POP) API calls, and historical API calls in Server Controller. This way, you can trace operations in the console and identify high-risk operations. O&M
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Computing** > **Compute**
3. In the left-side navigation pane, choose **ECS O&M** > **O&M Audit Logs**.
4. View information on each tab. The following table describes the tabs of the O&M Audit Logs
page.

| Tab | Description |
|---|---|
| Operations in the Apsara Uni- manager Operations Console | i. In the upper part of the tab, you can search for operation records by Resource and Time Range. ii. In this list below, you can view the information about each resource in the following columns: Operation, Operation Time, Operation Result, Error Information, RequestId, Request Parameter, Operator, and Description. |
| POP API Calls | i. In the upper part of the tab, you can search for POP API calls byK eyword and Time Range. You can specify an operation, a request ID, or a caller as the keyword. ii. In the list below, you can view the information about each call in the following columns: Operation, Operation Time, RequestId, HTTP Status Code, Error Information, Service, Request Parameter, and Caller. |
| Server Controller API Calls | i. In the upper part of the tab, you can search for Server Controller API calls by Keyword and Time Range. You can specify an operation, a request ID, or a request IP address as the keyword. ii. In the list below, you can view the information about each call in the following columns: Operation, RequestId, Request Time, Response Code, Request IP Address, Request Duration (ms), and Request Parameter. |

O&M

#### 1.1.5 Compute capacity analytics

You can query the capacity and inventory usage of Elastic Compute Service (ECS) instance types to check their capacity and inventory usage trends.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Computing** > **Compute**
3. In the left-side navigation pane, click **Compute Capacity Analytics**.
4. On the Compute Capacity Analytics page, view the following information.
In the **Allocated Capacity Ratio** section, view the total number of resources, number of used resources, and resource usage by resource type. The resources include vCPU cores, memory, GPUs, and local disks. In the **vCPU/Memory Usage Trend** section, specify a time range in the upper right corner to view the usage trends of vCPUs and memory within the specified period of time.

> **Note:** Move the pointer over a data point on a line chart to view the resource usage details on the corresponding day.

In the **Inventory** section, select a zone from the drop-down list and enter an instance type in the search box to view the corresponding inventory.

#### 1.1.6 Manage migration tasks

This topic describes how to start, view, and configure a migration task.

**Tasks**

**Background information**

O&M ECS migration tasks If an instance or a physical server fails, you can migrate the instance from the failed physical server to a normal physical server to ensure system stability. On the **ECS Migration Tasks** tab, you can view the information about Elastic Compute Service (ECS) migration tasks, machine migration tasks, and batch migration tasks. A machine migration task or batch migration task consists of multiple subtasks. Each subtask is an ECS migration task. Therefore, the information about subtasks is also displayed on the ECS Migration Tasks tab, and ECS migration tasks contain migration tasks that are created for migrating single ECS instances and subtasks of machine migration tasks and batch migration tasks. You can also find an ECS instance on the **ECS Instances** page and create a migration task for the instance. For more information, see the "Migrate an instance" section of the Migrate an instance topic. Machine migration tasks When you scale down or maintain a computing server, you must migrate all ECS instances on the server before you can perform operations on the server. In this case, you can migrate all ECS instances on the server to other computing servers. The computing server must be in the `free` or `mlock` state. After you submit a migration task, the server enters the mlock state. If the migration task is complete, fails, or is canceled, you must submit an application to manually unlock the server. The ECS instances on the server are migrated to other computing servers based on ECS scheduling rules. The migration task may not be successful in a single attempt due to various reasons. If an ECS instance in the **Shutted** or **Pending** state is migrated, the ECS instance remains in the same state after the migration. After the migration task is complete, you must check whether all ECS instances are migrated. You can also find the server to be migrated on the **Computing Server O&M** page and create a machine migration task for the server. For more information, see the "Migrate all instances on a server" section of the Computing server O&M topic. Batch migration tasks A batch migration task migrates multiple ECS instances in a batch to the destination server based on the migration destination configurations. The migration result is affected by multiple factors, and the batch migration task may fail. You can use a batch migration task to migrate only ECS instances of the same instance family. Only ECS instances that are in the **Running**, **Shutted**, or **Pending** state can be migrated at a time. If ECS instances in the **Shutted** or **Pending** state are migrated, the ECS instances remain in the same state after the migration.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Computing** > **Compute**
3. In the left-side navigation pane, click **Migration Tasks**.
O&M
4. On the **ECS Migration Tasks** subtab of the **Tasks** tab, create an ECS migration task and
view the task. i. Click **Create ECS Migration Task**. ii. On the Create ECS Migration Task page, configure the parameters that are described in the following table.
**Cold Migration**: Cold migration tasks migrate only instances that are in the **Pending**
or **Shutted** state.

| Section | Parameter | Description |
|---|---|---|
| Instance Information | Select Instance | The instance to be migrated. Enter the ID of the instance to be migrated in the search box and select the instance in the instance list. Important You can select only one ECS instance. |

O&M

| Destination Selection | Destination Selection Policy | Random Selection: migrates the instance to a random physical server in which resources are sufficient. This is the default policy. System Recommendation: migrates the instance to a recommended physical server that ensures a high success rate of migration. Important If no data is displayed in the host list, no physical server is available. We recommend that you select another policy. Specify NC: migrates the instance to the specified physical server. You can search for physical servers by cluster, hostname, physical server IP address, or physical server ID and select a physical server in the list. Note The system provides suggestions on whether each physical server is suitable. The suggestions are for reference and do not affect the selection of physical servers. You can also select a physical server that is not recommended based on your actual requirements. Specify Cluster: migrates the instance to the specified cluster. You can search for clusters by cluster name and select a cluster in the cluster list. Note The system provides suggestions on whether each cluster is suitable. The suggestions are for reference and do not affect the selection of clusters. You can also select a cluster that is not recommended based on your actual requirements. |
|---|---|---|
|   | Recovery Mode | The state that you want the instance to enter after migration. Valid values: Start after Migration Stop After Migration |
| Operation Information | Reason | The reason for cold migration. |

O&M
**Hot Migration**: Hot migration tasks migrate only instances that are in the **Running**
state.

| Section | Parameter | Description |
|---|---|---|
| Instance Information | Select Instance | The instance to be migrated. Enter the ID of the instance to be migrated in the search box and select the instance in the instance list. Important You can select only one ECS instance. |
| Basic Migration Parameters | Migration Rate | The migration rate. Unit: Mbit/s. We recommend that you set the parameter to a value greater than 500. |
|   | Enhanced Hot Migration Compatibility | Specifies whether to migrate the ECS instance to an available physical server with a different CPU model. For more information about the compatibility of CPU models, see the CPU compatibility configurations section of this topic. Important If you enable this feature and set the Destination Selection Policy parameter to System Recommendation, available physical servers with different CPU models are displayed. |

O&M

| Destination Selection |   |   |
|---|---|---|
|   | Destination Selection Policy | Random Selection: migrates the instance to a random physical server in which resources are sufficient. This is the default policy. System Recommendation: migrates the instance to a recommended physical server that ensures a high success rate of migration. Note If no data is displayed in the host list, no physical server is available. We recommend that you select another policy. Specify NC: migrates the instance to the specified physical server. If you select this policy, the migration task may fail. You can search for physical servers by cluster, hostname, physical server IP address, or physical server ID and select a physical server in the list. Note The system provides suggestions on whether each physical server is suitable. The suggestions are for reference and do not affect the selection of physical servers. You can also select a physical server that is not recommended based on your actual requirements. Specify Cluster: migrates the instance to the specified cluster. You can search for clusters by cluster name and select a cluster in the cluster list. Note The system provides suggestions on whether each cluster is suitable. The suggestions are for reference and do not affect the selection of clusters. You can also select a cluster that is not recommended based on your actual requirements. |
|   | Allowed Service Interruption Duration | The service interruption duration in the last phase of hot migration. Unit: millisecond. Valid values: 200 to 2000. Default value: 300. |

O&M

| Advanced Migration |   |   |
|---|---|---|
|   | Check SLB | Valid values: Yes: checks whether Server Load Balancer (SLB) instances are associated with the ECS instance. If SLB instances are associated with the ECS instance, the migration task may fail. No: does not check SLB instances. Default value: Yes. |
| Parameters Note You can click Config uratio n Descri ption to view the descrip tion of parame ters in this section . You can configu re advanc ed parame ters to increas e the succes s rate of hot migrati on. Howev er, you must configu re these parame ters based on your busines s require ments. |   |   |
|   | Check AVS Version | Valid values: Yes: checks whether the Azure VMware Solution (AVS) versions of the source and destination servers are consistent. If the AVS versions are inconsistent, the migration task fails. No: does not check the AVS versions. Default value: Yes. |
|   | Check Virtual NC Version | Valid values: Yes: checks whether the virtual version of the destination server can support hot migration. If the virtual version of the destination server does not support hot migration, the migration task fails. No: does not check the virtual version of the destination server. Default value: Yes. |
|   | Allow Reserved NC | Valid values: Yes: allows the instance to be migrated to a reserved server. No: does not allow the instance to be migrated to a reserved server. Default value: No. |

O&M

|   | Check CPU Tag | Valid values: Yes: checks whether the CPU tags of the source server are included in the tags of the destination server. If the CPU tags of the source server are not included in the tags of the destination server, the migration task fails. No: does not check the CPU tags of the servers. Default value: Yes. |
|---|---|---|
| Operation Information | Reason | The reason for hot migration. |

iii. Select **I have read the preceding notes and confirm this operation.** and click
**Submit**.
iv. View all ECS instance migration tasks in the task list. You can search for tasks by **task**
**ID**, **instance ID**, **task type**, or **task status**. The following table describes the
parameters in the task list.

| Parameter | Description |
|---|---|

O&M

| Task ID | The ID of the migration task. |
|---|---|
| Instance ID | The ID of the ECS instance to be migrated. |
| Source NC ID and IP Address | The ID and IP address of the source physical server that hosts the ECS instance to be migrated. |
| Destination NC ID and IP Address | The ID and IP address of the destination physical server to which the ECS instance is migrated. |
| Task Status | The status of the migration task. Valid values: Precheck Failed Canceled Initializing Waiting Migrating Successful Failed |
| Task Type | The type of the migration task. Valid values: Hot Migration Cold Migration |
| Retries | The number of retries and the maximum number of retries that can be performed if a migration task fails. At most five retries are allowed. If five tries fail, the ECS migration task enters the Failed state. |
| Migration Request Result | The response to the migration request, but not the final result of the migration task. |
| Created At | The time when the migration task was created. |
| Started At | The time when the migration task was started. |
| Updated At | The time when the migration task was updated. |
| Migration Reason | The reason for the migration. |
| Operator | The account that is used to create the migration task. |

O&M

| Migration Task Result | The result of the migration task. migration succeeded! indicates that the ECS migration task is successful. |
|---|---|

5. On the **Tasks** tab, click **Machine Migration Tasks**. Then, create a machine migration task
and view the task. i. Click **Create Machine Migration Task**. ii. On the Create Machine Migration Task page, configure the parameters that are described in the following table.

| Section | Parameter | Description |
|---|---|---|
| Source NC | Select Machine | The server on which all ECS instances are to be migrated. Enter a physical server name or IP address in the search box to search for a server, and then select it as the source physical server. Important You can select only one server. |
|   | Enhanced Hot Migration Compatibility | Specifies whether to migrate ECS instances to an available physical server with a different CPU model. For more information about the compatibility of CPU models, see the CPU compatibility configurations section of this topic. |

O&M

| Migration Destination Configurations |   |   |
|---|---|---|
|   | Destination Selection Policy | Random Selection: migrates ECS instances to a random physical server in which resources are sufficient. This is the default policy. Specify NC: migrates ECS instances to the specified physical server. If you select this policy, the migration task may fail. You can search for physical servers by cluster, hostname, physical server IP address, or physical server ID and select a physical server in the list. Note The system provides suggestions on whether each physical server is suitable. The suggestions are for reference and do not affect the selection of physical servers. You can also select a physical server that is not recommended based on your actual requirements. Specify Cluster: migrates ECS instances to the specified cluster. If you select this policy, the migration task may fail. You can search for clusters by cluster name and select a cluster in the cluster list. Note The system provides suggestions on whether each cluster is suitable. The suggestions are for reference and do not affect the selection of clusters. You can also select a cluster that is not recommended based on your actual requirements. |
| Advanced Migration Parameters | Allowed Service Interruption Duration | The service interruption duration in the last phase of hot migration. Unit: millisecond. Valid values: 200 to 2000. Default value: 300. |
|   | Check SLB | Valid values: Yes: checks whether SLB instances are associated with ECS instances. If SLB instances are associated with ECS instances, the migration task may fail. No: does not check SLB instances. Default value: Yes. |

O&M

| Note You can config ure advan ced param eters to |   |   |
|---|---|---|
|   | Check AVS Version | Valid values: Yes: checks whether the AVS versions of the source and destination servers are consistent. If the AVS versions are inconsistent, the migration task fails. No: does not check the AVS versions. Default value: Yes. |
|   | Check Virtual NC Version | Valid values: Yes: checks whether the virtual version of the destination server can support hot migration. If the virtual version of the destination server does not support hot migration, the migration task fails. No: does not check the virtual version of the destination server. Default value: Yes. |
| increa se the succe ss rate of hot migra tion. Howe ver, you must config ure these param eters based on your busin ess requir ement s. You can also click Confi gurat ion Descr iptio n to view the descri ption of param eters in this sectio n. |   |   |
|   | Allow Reserved NC | Valid values: Yes: allows the instances to be migrated to a reserved server. No: does not allow the instances to be migrated to a reserved server. Default value: No. |

O&M

|   | Check CPU Tag | Valid values: Yes: checks whether the CPU tags of the source server are included in the tags of the destination server. If the CPU tags of the source server are not included in the tags of the destination server, the migration task fails. No: does not check the CPU tags of the servers. Default value: Yes. |
|---|---|---|
| Operation Information | Reason | The reason for machine migration. |

iii. Select **I have read the preceding notes and confirm this operation.** and click
**Submit**.
iv. View the migration task in the task list. You can search for migration tasks by **task ID** or
**source physical server ID**. The following table describes the parameters in the task
list.

| Parameter | Description |
|---|---|

O&M

|   | Task ID | The ID of the migration task. |
|---|---|---|
|   | Source NC ID and IP Address | The ID and IP address of the source physical server. |
|   | Instances | The number of ECS instances that are migrated. |
|   | Task Status | The status of the migration task. Valid values: Initializing Running Successful Failed Creation Failed Creating Canceled |
|   | Task Success Rate | The success rate of the migration task. The success rate is calculated based on the following formula: Success rate of a migration task = Number of successful subtasks/Number of all subtasks × 100% |
|   | Destination Selection Policy | The policy for selecting a destination server. The policy that you specified when you created the migration task is displayed. |
|   | Destination Information | The destination server or cluster to which ECS instances are migrated. The server or cluster that you specified when you created the migration task is displayed. |
|   |   | The result of the migration task. all ecs migrate tasks belong to this task success! indicates that the machine migration task is successful. |
|   | Task Result | to this task success! |
|   | Created At | The time when the migration task was created. |
|   | Updated At | The time when the migration task was updated. |
|   | Migration Reason | The reason for the migration. |
|   | Operator | The account that is used to create the migration task. |

O&M v. Click **Details** in the **Operation** column of a migration task. In the panel that appears, view the following information about the task:
**Basic Information**: In this section, view the task ID, number of instances, and status
of the task.
**Migrate Instance**: In this section, view the information about the ECS instances that
you want to migrate.

> **Note:** Each ECS instance entry displayed in the instance list is a subtask of the machine migration task. To view details of a subtask, search for the ECS instance ID of the subtask on the **ECS Migration Tasks** tab.

vi. You can cancel a machine migration task based on your business requirements.

> **Note:** After a machine migration task is terminated:
> The status of the migration task changes to **Canceled**.
> Subtasks that are in the **Initializing** state are terminated. Subtasks that are in the **Pending** and **Migrating** states are not affected.

a. To terminate a migration task, find the migration task in the task list, and click
**Terminate Task** in the **Operation** column.
b. In the message that appears, click **OK**.
6. On the **Tasks** tab, click **Batch Migration Tasks**. Then, create a batch migration task and
view the task. i. Click **Create Batch Migration Task**. ii. On the Create Batch Migration Task page, configure the parameters that are described in the following table.

|   | Section |   | Parameter | Description |   |   |
|---|---|---|---|---|---|---|
|   | Instance Information |   | Select Instance | The ECS instances to be migrated. You can search for ECS instances by instance ID. Sperate multiple instances IDs with commas (,). Example: i-ez*****deuz,i-ez*****g4b4,i- ez*****02zd . |   |   |
|   |   |   |   |   | i-ez*****deuz,i-ez*****g4b4,i- |   |
|   |   |   |   | ez*****02zd |   |   |
|   |   |   | Enhanced Hot Migration Compatibility | Specifies whether to migrate ECS instances to an available physical server with a different CPU model. For more information about the compatibility of CPU models, see the CPU compatibility configurations section of this topic. |   |   |

O&M

| Migration Destination Configurations |   |   |
|---|---|---|
|   | Destination Selection Policy | Random Selection: migrates ECS instances to a random physical server in which resources are sufficient. This is the default policy. Specify NC: migrates ECS instances to the specified physical server. If you select this policy, the migration task may fail. You can search for physical servers by cluster, hostname, physical server IP address, or physical server ID and select a physical server in the list. Note The system provides suggestions on whether each physical server is suitable. The suggestions are for reference and do not affect the selection of physical servers. You can also select a physical server that is not recommended based on your actual requirements. Specify Cluster: migrates ECS instances to the specified cluster. If you select this policy, the migration task may fail. You can search for clusters by cluster name and select a cluster in the cluster list. Note The system provides suggestions on whether each cluster is suitable. The suggestions are for reference and do not affect the selection of clusters. You can also select a cluster that is not recommended based on your actual requirements. |
| Advanced Migration Parameters | Allowed Service Interruption Duration | The service interruption duration in the last phase of hot migration. Unit: millisecond. Valid values: 200 to 2000. Default value: 300. |
|   | Check SLB | Valid values: Yes: checks whether SLB instances are associated with ECS instances. If SLB instances are associated with ECS instances, the migration task may fail. No: does not check SLB instances. Default value: Yes. |

O&M

| Note You can configur e advance d parame ters to increase the |   |   |
|---|---|---|
|   | Check AVS Version | Valid values: Yes: checks whether the AVS versions of the source and destination servers are consistent. If the AVS versions are inconsistent, the migration task fails. No: does not check the AVS versions. Default value: Yes. |
|   | Check Virtual NC Version | Valid values: Yes: checks whether the virtual version of the destination server can support hot migration. If the virtual version of the destination server does not support hot migration, the migration task fails. No: does not check the virtual version of the destination server. Default value: Yes. |
| success rate of hot migratio n. Howeve r, you must configur e these parame ters based on your busines s require ments. You can also click Config uration Descrip tion to view the descript ion of parame ters in this section. |   |   |
|   | Allow Reserved NC | Valid values: Yes: allows the instances to be migrated to a reserved server. No: does not allow the instances to be migrated to a reserved server. Default value: No. |
|   | Check CPU Tag | Valid values: Yes: checks whether the CPU tags of the source server are included in the tags of the destination server. If the CPU tags of the source server are not included in the tags of the destination server, the migration task fails. No: does not check the CPU tags of the servers. Default value: Yes. |

O&M

| Operation Information | Reason | The reason for batch migration. |
|---|---|---|

iii. Select **I have read the preceding notes and confirm this operation.** and click
**Submit**.
iv. View the migration task in the task list. You can search for a task by **task ID**. The following table describes the parameters in the task list.

|   | Parameter | Description |
|---|---|---|
|   | Task ID | The ID of the migration task. |
|   | ECS Instances | The IDs of ECS instances that are migrated. Instance IDs are separated by commas (,). Example: i-ez*****deuz,i- ez*****g4b4,i-ez*****02zd . |
|   | Instances | The number of ECS instances that are migrated. |
|   | Task Status | The status of the migration task. Valid values: Initializing Running Successful Failed Creation Failed Creating Canceled |
|   | Task Success Rate | The success rate of the migration task. The success rate is calculated based on the following formula: Success rate of a migration task = Number of successful subtasks/Number of all subtasks × 100% |
|   | Destination Selection Policy | The policy for selecting a destination server. The policy that you specified when you created the migration task is displayed. |
|   | Destination Information | The destination server or cluster to which ECS instances are migrated. The server or cluster that you specified when you created the migration task is displayed. |
|   |   | The result of the migration task. all ecs migrate tasks belong to this task success! indicates that the batch migration task is successful. |
|   | Task Result | to this task success! |

| i-ez*****deuz,i- |   |
|---|---|

O&M

| Migration Reason | The reason for the migration. |
|---|---|
| Created At | The time when the migration task was created. |
| Updated At | The time when the migration task was updated. |
| Operator | The account that is used to create the migration task. |

v. Click **Details** in the **Operation** column of a migration task. In the panel that appears, view the following information about the task:
**Basic Information**: In this section, view the task ID, number of instances, and status
of the task.
**Migrate Instance**: In this section, view the information about the ECS instances that
you want to migrate.

> **Note:** Each ECS instance entry displayed in the instance list is a subtask of the batch migration task. To view details of a subtask, search for the ECS instance ID of the subtask on the **ECS Migration Tasks** tab.

vi. You can cancel a batch migration task based on your business requirements.

> **Note:** After a batch migration task is terminated:
> The **Status** of the migration task changes to **Canceled**.
> Subtasks that are in the **Initializing** state are terminated. Subtasks that are in the **Pending** and **Migrating** states are not affected.

a. To terminate a migration task, find the task in the task list and click **Terminate Task** in the **Operation** column. b. In the message that appears, click **OK**.

**Migration constraint configurations**

**Background information**

You can configure custom constraints for migration tasks if the default constraints do not meet your business requirements. The constraints for migration tasks contain the default migration rate and default timeout periods of migration tasks.

> **Note:** New migration constraints are applied to migration tasks that are created after the migration constraints are modified.

1. Log on to the Apsara Uni-manager Operations Console.
O&M
2. In the top navigation bar, choose **Product Operation** > **Computing** > **Compute**
3. In the left-side navigation pane, click **Migration Tasks**.
4. On the Migration Task Management page, click the **Migration Constraint Configurations**
tab.
5. Configure the following parameters and click **Submit**.
**Default Migration Rate Configurations:** Configure the default migration rates for
migration tasks. If you do not configure a migration rate for a migration task, the default migration rate is used.

> **Important:** If you configure a migration rate when you create an ECS migration task, the migration task is run at the specified rate. If you do not configure a migration rate, migration tasks are run at a rate based on the value of the **KVM** **Instance Migration Rate** or **ECS Bare Metal Instance Migration Rate** parameter.
> You cannot configure a migration rate when you create a machine migration task or a batch migration task. Subtasks are run at a rate based on the value of the **Machine Migration Rate** or **Batch Migration Rate** parameter.

| Parameter | Description | Default value |
|---|---|---|
| KVM Instance Migration Rate | The default migration rate for ECS instances that use the Kernel-based Virtual Machine (KVM) architecture. Unit: Mbit/s. Valid values: 20 to 2000. Note We recommend that you set this parameter to a value greater than or equal to 500. | 500 |
| ECS Bare Metal Instance Migration Rate | The default migration rate for ECS instances that use the X-Dragon architecture. Unit: Mbit/s. Valid values: 20 to 2000. Note We recommend that you set this parameter to a value greater than or equal to 1024. | 1024 |

O&M

| Machine Migration Rate | The default migration rate for machine migration tasks. Unit: Mbit/s. Valid values: 20 to 2000. Note We recommend that you set this parameter to a value greater than or equal to 800. | 800 |
|---|---|---|
| ECS Instance Batch Migration Rate | The default migration rate for batch migration tasks. Unit: Mbit/s. Valid values: 20 to 2000. Note We recommend that you set this parameter to a value greater than or equal to 800. | 800 |

**Default Timeout Configurations**: Configure the default timeout periods for migration
tasks. You cannot configure a timeout period when you create a migration task. You can use only the default timeout period.

> **Important:** Before you configure the default timeout periods for migration tasks, take note of the following items:
> The value of the **ECS Migration Timeout Period** parameter must be smaller than the values of the **Server-level Migration Timeout Period** and **ECS** **Instance Batch Migration Timeout Period** parameters.
> If a migration task times out, the migration task fails. Therefore, we recommend that you set each default migration timeout period to a value that is equal to or greater than 5 minutes.

| Parameter | Description | Default value |
|---|---|---|
| ECS Migration Timeout Period | The timeout period for an ECS migration task. Unit: minutes. Valid values: 2 to 60. | 20 |
| Server-level Migration Timeout Period | The timeout period for a machine migration task. Unit: minutes. Valid values: 2 to 120. | 60 |
| ECS Instance Batch Migration Timeout Period | The timeout period for a batch migration task. Unit: minutes. Valid values: 2 to 120. | 60 |

O&M

**CPU compatibility configurations**

**Background information**

If you enable the **Enhanced Hot Migration Compatibility** feature for a hot migration task to migrate ECS instances on a physical server to another physical server with a different CPU model, the migration succeeds only if the CPU model of the source server is compatible with that of the destination server. Otherwise, the migration task fails. Before you enable the
**Enhanced Hot Migration Compatibility** feature, we recommend that you follow the
instructions in this section to view the CPU models that are supported for migrations across CPU models of physical servers and the CPU compatibility.

> **Important:** Notes on CPU compatibility for hot migration:
> If the CPU models of the source and destination servers that you configured for a hot migration task are not displayed on the **CPU Compatibility Configurations** tab, the task is not allowed to hot migrate ECS instances in the Apsara Uni- manager Operations Console, and the task fails.
> You cannot add the CPU compatibility information for hot migration in the Apsara Uni-manager Operations Console.
> You can contact Alibaba Cloud technical support to add the CPU compatibility information for hot migration. After the CPU compatibility information is added, you can create hot migration tasks. However, the migration tasks may fail.

1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Computing** > **Compute**
3. In the left-side navigation pane, click **Migration Tasks**.
4. On the Migration Task Management page, click the **CPU Compatibility Configurations**
tab. On this tab, you can view the compatible CPU models of the source and destination servers. You can also search for a source CPU model to view its compatible destination CPU model.

| Parameter | Description |
|---|---|
| Source CPU Model | The CPU model of the physical server that hosts the ECS instances to be migrated. |
| Destination CPU Model | The CPU model of the physical server to which the ECS instances are migrated. |

O&M

#### 1.1.7 ECS Intelligent O&M

##### 1.1.7.1 ECS instance events

You can query events by instance. This allows you to know the exceptions of Elastic Compute Service (ECS) instances.

**Prerequisites**

ECS has reached the desired state. The Apsara Uni-manager Operations Console is in the desired state.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Computing** > **Compute**
3. In the left-side navigation pane, choose **ECS Intelligent O&M** > **ECS Instance Events**.
4. On the ECS Instance Events page, you can query all ECS instance events. You can also filter
ECS instance events by **Time Range**, **OpsCode**, **Event ID**, **Instance ID**, and **Physical**
**Machine IP**.

> **Note:** You must specify a time range and at least one parameter of the others.
> Valid values of the OpsCode parameter:
> InstanceFailure.Reboot: The instance is restarted.
> SystemFailure.Alert: A system alert is triggered.
> InstanceFailure.Alert: An instance alert is triggered.
> SystemMaintenance.Reboot: The instance is restarted during active O&M.
> SystemFailure.PerformanceAffect: The system performance is affected.
> SystemFailure.PerformanceImpact: The system performance is significantly affected.
> SystemFailure.Reboot: The system is restarted.

O&M
5. Find the instance event whose details you want to view and click **Details** in the **Operation**
column to view the event details.
6. Find the instance event that you want to manage and click the instance ID in the **Instance**
**ID** column to view the instance details. For more information, see the 7. View the details of
an instance. section of the “ECS instances” topic.
7. Find the instance event that you want to manage and click the IP address in the **Physical**
**Machine IP** column to view the computing server O&M details. For more information, see
the 6. View the O&M details of a computing server section of the "Computing server O&M" topic.
8. Find the instance event that you want to manage and click the cluster name in the **Cluster**
**name** column to view the computing cluster O&M details. For more information, see the 6.
View the O&M details of a computing cluster section of the "Computing cluster O&M" topic.

##### 1.1.7.2 ECS physical machine events

O&M In the Compute Operations Console, you can use the Elastic Compute Service (ECS) physical machine events feature to analyze the impact of physical machine events. If the breakdown of an ECS physical machine triggers the ECS instance migration process, you can view the migrated ECS instances.

**Prerequisites**

ECS has reached the desired state.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Computing** > **Compute**
3. In the left-side navigation pane, choose **ECS Intelligent O&M** > **ECS Physical Machine**
**Events**.
4. On the ECS Physical Machine Events page, view all ECS physical machine events. You can
configure the **Date Range**, **Physical Machine IP Address**, and **Event Status** parameters to filter ECS physical machine events.
5. View the information about the ECS physical machine events in the columns, including
**Physical Machine IP Address**, **Cluster**, **Affected Instances**, **Affected vCPUs**,
**Occurrences**, **Occurrence Time**, **Update Time**, **Event Status**, **Event Type**, **Event**
**Name**, **Event Description**, **Event Level**, and **Event Cause**.
6. Find the ECS physical machine event that you want to view and click **Details** in the
**Operation** column. The details panel of the ECS physical machine event appears.
O&M

| Section | Description |
|---|---|
|   | This section includes the following parameters: Physical Machine IP Address, Hostname, SN, Model, CPU (Cores), Memory (MB), Operating System Template, Cluster, Rack, and CPU Model. After you click the cluster name, the Computing Cluster Details page appears. For more information, see the "View the O&M details of a compute cluster" section of the View the O&M details of a computing cluster. On the Computing Cluster O&M page, click the name of the cluster that you want to view to go to the Computing Cluster Details page. On the Overview tab, view the information about computing servers and ECS instances in the cluster. In the Cluster Information section, view the basic information of the cluster, including the region in which the cluster is deployed, cluster type, whether the cluster uses only ECS resources, zone, cluster ID, instance family, cluster status, network type, physical network, disk type, and cluster specifications. In the upper-right corner of this section, click Connect to Cluster AG to log on to the Admin Gateway (AG). For more information, see the Log on to the AG of a cluster section of this topic. In the Server Resources section, view the number of computing servers, the number of CPUs, and the amount of available memory. In the ECS Instances section, view the total number of ECS instances, the number of ECS instances that are running, and the number of abnormal ECS instances. In the NC State Distribution section, view the distribution of physical |

O&M

|   | machines in different states. Move the pointer over the chart. The number of physical machines in each state is displayed. The following table describes the states of physical machines. State Description Failover The physical machine is down. Normal The physical machine runs as expected. You can schedule instances to the physical machine. No heartbeat The physical machine has no heartbeats. Mlock The physical machine is manually locked. Rlock The physical machine is forcefully reserved and can be used to recover or modify VMs. If the resources of the physical machine are insufficient, the |
|---|---|
| Physical Machine Basic Information | physical machine performs defragmentation. Otherwise, an alert is triggered. The physical machine must have heartbeats and remain available. Initializing The physical machine is being initialized. All the virtual private cloud (VPC) configurations of the physical machine are being reissued by the RegionMaster. In the ECS Instance State Distribution section, view the distribution of ECS instances in different states. The following table describes the states of ECS instances. State Description Running The instance runs as expected. Stopped After an instance is stopped or after an instance is created but not started, the instance is in the Stopped state. Instances in the Stopped state cannot provide external services. Pending After an instance is created, the instance is in the Pending state before it enters the Running state. If the instance remains in the Pending state for an extended period of time, an exception occurs. Creating After you start or restart an instance in the ECS console or by calling an API operation, the instance enters the Creating state before it enters the Running state. If the instance remains in the Creating state for an extended period of time, an exception occurs. Stopping After you stop an instance in the ECS console or by calling an API operation, the instance enters the Stopping state before it enters the Stopped state. If the instance remains in the Stopping state for an extended period of time, an exception occurs. Releasing After you release an instance, the instance enters the Releasing state before it enters the Released state. In the Inventory Utilization section, view the total amount of resources, the amount of used resources, and the percentage of used resources in all resources. In the Inventory section, view the inventory details of the instance types in the cluster. Click the Configurations tab. On this tab, you can configure the CPU oversold ratio and view its configuration records. For more information, see Configure CPU oversold ratios. Click the Computing Servers tab. View information about the computing servers in the cluster in the following columns: Hostname, IP Address, NC ID, NC Type, vCPU (Cores), Memory, Service State, Instances, Data Center, Rack, and SN. For more information about valid values of the Service State parameter, see the table describing the states of physical machines of this topic. View the O&M details of a computing server. Find the computing server that you want to view and click the server name in the Hostname column. On the Computing Server Details page, view the O&M details of the computing server. For more information, see the 6. View the O&M details of a computing server. section of the "Computing server O&M" topic. View the details of ECS instances that are deployed on a computing server. Find the computing server that you want to view and click the number in the Instances column. In the Instance List panel, view the instance information in the following columns: Instance ID, Status, Instance Name, CPU, and Memory. Click an instance ID in the Instance ID column. The Instance Details page of the ECS instance appears. For more information, see . Manage the service states of the computing servers in the cluster. The following table describes the operations that you can perform on computing servers. Operation Scenario Procedure Lock NC You can lock abnormal servers to prevent instances from being scheduled to these servers. If the servers are locked, the status of the servers cannot be automatically changed. You can also lock servers for which you want to reserve resources. On the Computing Servers tab, find the server that you want to lock and click Lock NC in the Operation column. In the Lock NC dialog box, confirm the server information, select a lock state, and then configure the Changed By, Change Ticket Title, and Reason |

O&M

|   | parameters. Click OK. Unlock NC You can unlock servers in the no heartbeat, mlock, and rlock states. After you unlock a server, the server is automatically activated and you can schedule instances to the server. On the Computing Servers tab, find the server that you want to unlock and click Unlock NC in the Operation column. In the Unlock NC dialog box, confirm the server information and enter the reason for unlocking the server. Click OK. Activate You can activate servers in the no heartbeat, mlock, rlock, failover, and initializing states. On the Computing Servers tab, find the server that you want to activate and click Activate in the Operation column. In the dialog box that appears, enter a reason for activating the server, the user who performed the operation, and a ticket title in the Reason field. Click OK. topic. |
|---|---|
| Event Details | This section includes the following parameters: Event ID, Event Type, Affected ECS Instances, Affected vCPUs, Affected Memory, Published At, and Status. |
|   | You can view the information about the affected instances in the following columns: Event ID, Instance ID, CPU (Cores), Memory (GB), Published At, End Time, Source Physical Machine, Destination Physical Machine IP Address, and Migration Status. Find the event that you want to view and click the event ID to view the event details. Find the instance that you want to view and click the instance ID in the Instance ID column to view the instance details. For more information, see the "View the details of an instance" section of the View the details of an instance. In the instance list, find the ECS instance that you want to view and click its ID in the Instance ID/Name column. On the instance details page, you can click buttons in the upper-right corner to perform various operations on the ECS instance. For more information, see the section of this topic. For information about how to log on to the cluster Admin Gateway (AG), see the Log on to the AG of a cluster section of the "Computing cluster O&M" topic. View the following information on the instance details page. Section or tab Description Basic Information This section displays the basic information about the ECS instance, including Instance ID, Instance Name, Specifications, Region, Zone, Creation Time, Apsara |

O&M

| Affected Instance Information | Stack Tenant Account ID, State in Business Foundation System, State in Server Controller, Cluster, Host ID, Host, and Rack. Configurations This section displays the configuration information about the ECS instance, including I/O Optimized, System Image, Operating System, System Disk, Network Type, Internal Bandwidth, Private IP Address, RDMA IP, VPC ID, vSwitch, and NAT IP Address. Disks View the list of disks and the disk information, including Disk ID, Disk Type, Status, Cluster, and Feature. View the details of a disk. Perform various operations on a disk by clicking buttons in the Operation column, including Detatch, Audit Operations, Create Snapshot, and View Snapshots. For more information, see the section of the "Disks" topic. ENIs View the information about the elastic network interfaces (ENIs) that are bound to the ECS instance. The information includes ENI ID/MAC Address, Status, ENI Type, vSwitch, and IP. View the details of an ENI. Perform various operations on an ENI by clicking buttons in the Operation column, including Unbind and Operation Audit. For more information, see the View operation records section of the "ENIs" topic. Security Groups View the information about the security group to which the ECS instance belongs. The information includes Security Group ID/Name, Network Type, VPC ID, and Creation Time. View the details of a security group. View operation records of a security group by clicking Audit Operations in the Operation column. For more information, see Security groups. Snapshots View the list of snapshots and the snapshot information, including Snapshot ID/Name, Snapshot ID in Server Controller, Snapshot Type, Disk ID/Type, Progress, and Creation Time. View the details of a snapshot. Perform various operations on a snapshot by clicking buttons in the Operation column, including Delete, Audit Operations, and Create Image. For more information, see . Performance Monitoring You can specify a time range and view the charts that describe the instance performance within the specified period of time. The performance metrics include CPU utilization, disk read/write (byte/s), disk IOPS, |
|---|---|
|   | public bandwidth (bit/s), and internal bandwidth (bit/s). ASO Migration Tasks After a migration task is triggered in the Apsara Uni-manager Operations Console, you can view the status and result of the migration task on this tab. You can view the task information including Task ID, Source NC ID and IP Address, Destination NC ID and IP Address, Task Type, Retries, Task Status, Start Time, Migration Reason, Operator, and Migration Task Result. Valid values of the Task Type parameter are Cold Migration and Hot Migration. The value of the Retries parameter is a ratio of the number of executed retries to the maximum number of retries. Migration History View the historical migration tasks that are created within the lifecycle of the ECS instance. Both cold migration and hot migration tasks are displayed. You can view the information about each migration task, including Source NC, Destination NC, Status, Migration Time, End Time, and Migration Reason. Audit Operations View the operation records of the ECS instance on the Operations in the Apsara Uni-manager Operations Console, POP API Calls, and Server Controller API Calls subtabs. For more information, see . Associate Resources View the topology that shows the relationships among the ECS instance and its associated resources. The resources include account, VPC, VM, computing server, cluster, image, data disk, system disk, network interface card (NIC), and security group. You can move the pointer over a resource to view the details of the resource. topic. |

O&M
7. Click the IP address of the physical machine in the **Physical Machine IP Address** column.
The **Computing Server Details** page appears. For more information, see the "View the O&M details of a compute server" section of the View the O&M details of a computing server. Find the computing server that you want to view and click the name in the Hostname column. On the Computing Server Details page, you can perform operations on the computing server by clicking buttons in the upper-right corner. For more information, see the section of this topic. On the Computing Server Details page, view the following information. Section/Tab Description Business Information Displays the business information about the computing server, including Business ID, IP, Hostname, Status, Management Heartbeat, Selling Mode, Cluster, Available Instance Families, Operating System, and Compute Type. Click the cluster name to go to the Computing Cluster Details page. On this page, view the O&M details of the computing cluster. For more information, see the 6. View the O&M details of a computing cluster section of the "Computing cluster O&M" topic. Hardware Information Displays the hardware information about the computing server, including SN, Model, Rack, CPU Model, GPU, vCPU (Cores), and Memory. Resource Information Displays the vCPU utilization, the total number of vCPU cores, the number of used vCPU cores, the number of available vCPU cores, the memory usage, the total memory, the used memory, and the available memory. ECS Instances On this tab, you can perform the following operations: In the upper part of the tab, enter an instance ID in the search box to search for an ECS instance. Alternatively, click Advanced Search and search for an ECS instance by Business Foundation System Status, AliUid, or their combinations. In the ECS instance list, view the information about each ECS instance in the following columns: Instance ID/Name, vCPU/Memory, Status, Private/Public IP Address, Bandwidth, User Information, Images, Creation Time, and All in ECS Resources or Not. View the details of an ECS instance. Find the ECS instance that you want to view and click its ID to go to the instance details page. For more information, see the 7. View the details of an instance. section of the "ECS instances" topic. Manage an ECS instance. You can perform diagnostics on the instance, migrate the instance, view migration history, view audit logs, change the instance status, and manage ISOs. For more information, see the What to do next section of the "ECS instances" topic. Performance Monitoring On this tab, specify a time range and view the trend charts of the following performance metrics within the specified period of time: CPU(%), Memory (%), System Load, Network Retransmission (%), and Network Traffic (MB). Alert Information On this tab, view the information about each alert, including the alert name, alert cause, alert details, first time when the alert was reported, last time when the alert was reported, and number of times that the alert was reported. Control Service On this tab, view server roles and their states. You can also search for a server role on this tab. View the server role information in the Apsara Infrastructure Management console: Find the server role that you want to view and click Apsara Infrastructure Management Framework in the Operation column to go to the Product & Cluster O&M page. For more information, see Apsara Infrastructure Management O&M Guide. Machine Migration Task View the information about each migration task, including the task ID, number of migrated instances, destination physical server, task status, migration progress, start time, update time, and task creator. View the details of a migration task: Find the migration task that you want to view and click its ID. In the Migrated Instance Details panel, view the detailed information about the task, including the instance ID, migration status, destination physical server, migration type, number of retries (used retries/maximum retries), start time, update time, and migration result. Cold migration tasks: migrates instances that are in the Pending state. Hot migration tasks: migrates instances that are in the Running state. Restart a migration task. If a migration task fails, you can click Restart in the Operation column of the task. In the dialog box that appears, enter the reason and then click OK. Cancel a migration task: Find the migration task that you want to cancel and click Cancel in the Operation column. In the dialog box that appears, enter the reason and then click OK. Operation Audit During the O&M of a computing server, the operations that may cause risks are audited. On this tab, you can click the following sub-tabs to view the corresponding information. For more information, see . Operations in the Apsara Uni-manager Operations Console POP API Calls Server Controller API Call History topic. O&M
8. Click the cluster name in the **Cluster** column. The **Computing Cluster Details** page
appears. For more information, see the "View the O&M details of a compute cluster" section of the View the O&M details of a computing cluster. On the Computing Cluster O&M page, click the name of the cluster that you want to view to go to the Computing Cluster Details page. On the Overview tab, view the information about computing servers and ECS instances in the cluster. In the Cluster Information section, view the basic information of the cluster, including the region in which the cluster is deployed, cluster type, whether the cluster uses only ECS resources, zone, cluster ID, instance family, cluster status, network type, physical network, disk type, and cluster specifications. In the upper-right corner of this section, click Connect to Cluster AG to log on to the Admin Gateway (AG). For more information, see the Log on to the AG of a cluster section of this topic. In the Server Resources section, view the number of computing servers, the number of CPUs, and the amount of available memory. In the ECS Instances section, view the total number of ECS instances, the number of ECS instances that are running, and the number of abnormal ECS instances. In the NC State Distribution section, view the distribution of physical machines in different states. Move the pointer over the chart. The number of physical machines in each state is displayed. The following table describes the states of physical machines. State Description Failover The physical machine is down. Normal The physical machine runs as expected. You can schedule instances to the physical machine. No heartbeat The physical machine has no heartbeats. Mlock The physical machine is manually locked. Rlock The physical machine is forcefully reserved and can be used to recover or modify VMs. If the resources of the physical machine are insufficient, the physical machine performs defragmentation. Otherwise, an alert is triggered. The physical machine must have heartbeats and remain available. Initializing The physical machine is being initialized. All the virtual private cloud (VPC) configurations of the physical machine are being reissued by the RegionMaster. In the ECS Instance State Distribution section, view the distribution of ECS instances in different states. The following table describes the states of ECS instances. State Description Running The instance runs as expected. Stopped After an instance is stopped or after an instance is created but not started, the instance is in the Stopped state. Instances in the Stopped state cannot provide external services. Pending After an instance is created, the instance is in the Pending state before it enters the Running state. If the instance remains in the Pending state for an extended period of time, an exception occurs. Creating After you start or restart an instance in the ECS console or by calling an API operation, the instance enters the Creating state before it enters the Running state. If the instance remains in the Creating state for an extended period of time, an exception occurs. Stopping After you stop an instance in the ECS console or by calling an API operation, the instance enters the Stopping state before it enters the Stopped state. If the instance remains in the Stopping state for an extended period of time, an exception occurs. Releasing After you release an instance, the instance enters the Releasing state before it enters the Released state. In the Inventory Utilization section, view the total amount of resources, the amount of used resources, and the percentage of used resources in all resources. In the Inventory section, view the inventory details of the instance types in the cluster. Click the Configurations tab. On this tab, you can configure the CPU oversold ratio and view its configuration records. For more information, see Configure CPU oversold ratios. Click the Computing Servers tab. View information about the computing servers in the cluster in the following columns: Hostname, IP Address, NC ID, NC Type, vCPU (Cores), Memory, Service State, Instances, Data Center, Rack, and SN. For more information about valid values of the Service State parameter, see the table describing the states of physical machines of this topic. View the O&M details of a computing server. Find the computing server that you want to view and click the server name in the Hostname column. On the Computing Server Details page, view the O&M details of the computing server. For more information, see the 6. View the O&M details of a computing server. section of the "Computing server O&M" topic. View the details of ECS instances that are deployed on a computing server. Find the computing server that you want to view and click the number in the Instances column. In the Instance List panel, view the instance information in the following columns: Instance ID, Status, Instance Name, CPU, and Memory. Click an instance ID in the Instance ID column. The Instance Details page of the ECS instance appears. For more information, see . Manage the service states of the computing servers in the cluster. The following table describes the operations that you can perform on computing servers. O&M Operation Scenario Procedure Lock NC You can lock abnormal servers to prevent instances from being scheduled to these servers. If the servers are locked, the status of the servers cannot be automatically changed. You can also lock servers for which you want to reserve resources. On the Computing Servers tab, find the server that you want to lock and click Lock NC in the Operation column. In the Lock NC dialog box, confirm the server information, select a lock state, and then configure the Changed By, Change Ticket Title, and Reason parameters. Click OK. Unlock NC You can unlock servers in the no heartbeat, mlock, and rlock states. After you unlock a server, the server is automatically activated and you can schedule instances to the server. On the Computing Servers tab, find the server that you want to unlock and click Unlock NC in the Operation column. In the Unlock NC dialog box, confirm the server information and enter the reason for unlocking the server. Click OK. Activate You can activate servers in the no heartbeat, mlock, rlock, failover, and initializing states. On the Computing Servers tab, find the server that you want to activate and click Activate in the Operation column. In the dialog box that appears, enter a reason for activating the server, the user who performed the operation, and a ticket title in the Reason field. Click OK. topic.

##### 1.1.7.3 ECS O&M events

You can view proactive O&M workflows in the ECS O&M Event module. You can also submit proactive O&M events and repair tickets for local disks.

**View proactive O&M workflows and their details**

1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Computing** > **Compute**
3. In the left-side navigation pane, choose **ECS Intelligent O&M** > **ECS O&M Event**.
4. On the Proactive O&M page, click **Advanced Filter** and filter proactive O&M workflows by
**Date Range**, **Proactive O&M Type**, **NC IP**, **Event Status**, **O&M Object**, and **Instance**
**Id**, or their combinations.
5. In the list of proactive O&M workflows, view the workflow information in the following
columns: **Proactive O&M Type**, **NC IP/Instance Id**, **Cluster**, **Status**, **Cause Category**,
**Content**, **Additional instructions**, **Update Time**, **Creation Time**, **Author**, and
**Handler**.
6. Click an IP address in the **NC IP** column of a proactive O&M event to go to the **Computing**
**Server Details** page. For more information, see the 6. View the O&M details about a
computing server. section of the "Computing server O&M" topic.
7. To view the details of a proactive O&M event, click **Details** in the **Operation** column of the
O&M event. On the Workflow Details page, view the following information. O&M

| Section | Description |
|---|---|
| Basic Information | This section displays the basic information about the workflow, including Workflow ID, Workflow Name, Manage Resource, Created At, Start Time, and Last Updated At. |
| Current Node | This section displays the information about the current node, including Node Location, Node Task, Start Information, End Information, Status, Result, Updated At, and Description. View the number next to the Start Information or End Information parameter to view the detailed start or end information of the workflow. Click Hyperlink to go to the ECS Diagnosis page and view the details of work items. For more information, see ECS Diagnosis. You can retry a failed work item. You must enter the reason for the retry. If the work item still fails, click Next Step to skip it and execute the next work item. Warning The retry and skip features are used only when an error that cannot be resolved occurs and must be used under the guidance of R&D personnel. |
| Workflow | This section displays the execution details of the workflow. View the number next to the Start Information or End Information parameter to view the detailed start or end information of the workflow. To view the details of a failed node, click Hyperlink in the upper-right corner of the node section to go to the ECS Diagnosis page. |

8. If a workflow whose value in the **Proactive O&M Type** column is **Local Disk Nc Repair**,
you can perform the following operations on the workflow details page. O&M

| Operation | Description |
|---|---|
| Confirm Repair Completed | After the repair is complete, click Confirm Repair Completed in the upper-right corner. In the dialog box that appears, enter the reason and click Complete Workflow to modify the workflow status. |
| Authorize to Isolate Disks | If a local disk exception occurs and needs to be isolated for repair, click Authorize to Isolate Disks in the upper-right corner. In the dialog box that appears, enter the reason and click Authorize to Isolate Disks to complete the authorization. |
| Authorize to Restore Isolated Disks | After you click Confirm Repair Completed, click Authorize to Restore Isolated Disks in the upper-right corner. In the dialog box that appears, enter the reason and click Authorize to Restore Isolated Disks to restore the isolated disks. |

**Submit proactive O&M events**

> **Warning:** During proactive O&M, services may be interrupted due to operations such as server restarts. Therefore, you must obtain the authorization from users and proceed with caution.

1. Click **Submit Proactive O&M Event**.
2. In the dialog box that appears, configure the following parameters and click **OK**.

| Parameter | Description |
|---|---|
| IP | The IP address of the server on which you want to perform the proactive O&M action. |

O&M

| M |   |   |   |
|---|---|---|---|
| Proactive O&M Type | The type of the proactive O&M action, which is the OpsCode of the proactive O&M event. Valid values: 0x410A01-Lock NC: locks the physical server. When the physical server is locked, Elastic Compute Service (ECS) instances cannot be created on or migrated to the physical server. 0x40003000001001-OOB Reboot NC without live migration: migrates ECS instances on the physical server in the O&M window and then restarts the physical server. 0x4000300001066-Change NC configuration: changes the configuration of a physical server. 0x400003-OOB Reboot NC with live migration: hot migrates ECS instances on the physical server and then restarts the physical server. 0x400012-Force NC OOB Reboot: forcibly restarts the physical server. 0x400011-recover NC status online: restores the physical server to a normal state. 0x3000000000802-Clean Wild Vm: clears residual ECS instances in the environment. 0x400016-Start Local Disk Nc: performs an out-of-band (OOB) restart on the physical server that failed due to a local disk failure and then starts the ECS instances on the physical server. 0x400018-Mark NC Down And Vm Migrate: forcibly migrates ECS instances on the physical server when the physical server is down. 0x30000000001005-Start Crashed Vm: restarts ECS instance on the physical server after a crash occurs. 0x40001000008001-Stop MOC While CN Down: marks the MOC as down and cleans the MOC after the controller node (CN) of an ECS bare metal instance is down. 0x4000A000000008-memory defragmentation: clears memory fragments from the physical server. 0x4000A000000007-Unlock Nc: automatically unlocks the physical server after it is locked. 0x30003000001001-Start Vm: starts the ECS instances. 0x99001000000001-Local Disk Nc Repair: isolates local disks on the physical server and replaces the disks for maintenance. 0x30000000000408-Qemu live upgrade: hot upgrades the QEMU process. 0x8000000000001-Nc Offline And Repair: deactivates the physical server for maintenance. 0x40007000000203-reload pync: reloads PYNC because PYNC is running for a long period of time and excessive file handles are generated. Important The configuration parameters vary based on the type of the proactive O&M action. Configure the parameters as prompted. |   |   |
|   |   | Important The configuration parameters vary based on the type of the proactive O&M action. Configure the parameters as prompted. |   |
| 2 |   | > Document Version: 202511 | 0 |

O&M

|   |   | When you submit a proactive O&M event, only the O&M actions that can be manually submitted are supported. You can enable or disable proactive O&M actions based on your |   |
|---|---|---|---|
| Reason Type | business requirements to prevent high-risk operations The reasotnr iwggheyr yeodu b wy ainnct otror epcetr fOo&rmM tahcet iopnrosa. cFtoivr em Oo&reM i nafcotrimona toionn the physical saebrvoeurt. hTohwe ftool lcoowninfigg urreea sOo&nMs aarcet iaovnas,il asebele :the Configure the approval settings section of the "Computing O&M settings" Hardware failures, such as failures in the fan, storage card, and topic. motherboard. Kernel errors, such as cgroup-level out of memory (OOM) errors. Network failures, such as network cable failures. System failures, such as memory fragmentation failures. Abnormal shutdown. Security protection, such as the protection against DDoS attacks. Internal restarts. | business requirements to prevent high-risk operations The reasotnr iwggheyr yeodu b wy ainnct otror epcetr fOo&rmM tahcet iopnrosa. cFtoivr em Oo&reM i nafcotrimona toionn the physical saebrvoeurt. hTohwe ftool lcoowninfigg urreea sOo&nMs aarcet iaovnas,il asebele :the Configure the approval settings section of the "Computing O&M settings" Hardware failures, such as failures in the fan, storage card, and topic. motherboard. |   |
| Reason | The reason for the proactive O&M action. |   |   |

**Proactive O&M types**

| Type | Submission method | Process |
|---|---|---|
| Lock NC | Manual submission | 1. Lock the server. 2. Complete O&M. |
| recover NC status online | Manual submission | 1. Restore the physical server to the online state. 2. Complete O&M. |
| Unlock Nc | Manual submission | 1. Lock the server. 2. Wait for the scheduled time for unlocking. 3. Unlock the server. 4. Complete O&M. |
| Start Vm | Manual submission | 1. Start ECS instances. 2. Complete O&M. |

O&M

| OOB Reboot NC without live migration | Automatic submission Manual submission | 1. Completes authorization as the administrator of the Apsara Uni-manager Operations Console: Log on to the Apsara Uni-manager Operations Console. In the top navigation bar, choose Platform Operation > O&M Change > Process Approval. In the left-side navigation pane, choose Process Approval > Pending Approval. On the Pending Approval page, complete authorization. Before you approve the proactive O&M workflow, make sure that the services on the physical server are running as expected. 2. Lock the server. 3. Initialize the instance status. 4. Notify your customers. 5. Migrates ECS instances in the O&M time window: If an instance exists, manually migrate the instance and then retry. Alternatively, skip the migration and perform downtime migration later. Downtime migration takes an extended period of time. 6. Check the physical server before you restart it. 7. Shut down the physical server: Log on to the Apsara Uni-manager Operations Console. In the top navigation bar, choose Platform Operation > Apsara Infrastructure Management > Resource Management. On the corresponding page, approve the shutdown requests for server roles. 8. Publish the proactive O&M event. 9. Perform the OOB restart on the physical server. 10. Check whether the physical server is started. 11. Complete O&M. |
|---|---|---|

O&M

| OOB Reboot NC with live migration | Automatic submission Manual submission | 1. Completes authorization as the administrator of the Apsara Uni-manager Operations Console: Log on to the Apsara Uni-manager Operations Console. In the top navigation bar, choose Platform Operation > O&M Change > Process Approval. In the left-side navigation pane, choose Process Approval > Pending Approval. On the Pending Approval page, complete authorization. Before you approve the proactive O&M workflow, make sure that the services on the physical server are running as expected. 2. Lock the server. 3. Initialize the instance status. 4. Perform online migration: If the migration fails, manually migrate instances on the Migration Tasks page. By default, if 50% or higher ECS instances are migrated, the migration is complete. 5. Reserve resource identifiers (RIs) for the ECS instances. 6. Notify your customers. 7. Migrates ECS instances in the O&M time window: If the instance migration is not complete. Manually complete the migration and try again. Alternatively, skip the migration and perform downtime migration later. Downtime migration takes an extended period of time. 8. Check the physical server before you restart it. 9. Publish the proactive O&M event. 10. Shut down the physical server: Log on to the Apsara Uni-manager Operations Console. In the top navigation bar, choose Platform Operation > Apsara Infrastructure Management > Resource Management. On the corresponding page, approve the shutdown requests for server roles. 11. Start only machines with ECS instances or storage nodes. 12. Publish the proactive O&M event. 13. Release the RI resource pool. 14. Complete O&M. |
|---|---|---|

O&M

| Force NC OOB Reboot | Automatic submission Manual submission | 1. Completes authorization as the administrator of the Apsara Uni-manager Operations Console: Log on to the Apsara Uni-manager Operations Console. In the top navigation bar, choose Platform Operation > O&M Change > Process Approval. In the left-side navigation pane, choose Process Approval > Pending Approval. On the Pending Approval page, complete authorization. Before you approve the proactive O&M workflow, make sure that the services on the physical server are running as expected. 2. Shut down the physical server: Log on to the Apsara Uni-manager Operations Console. In the top navigation bar, choose Platform Operation > Apsara Infrastructure Management > Resource Management. On the corresponding page, approve the shutdown requests for server roles. 3. Wait until the ECS instances are migrated. 4. Wait until the physical server fails. 5. Perform the OOB restart on the physical server. 6. Complete O&M. |
|---|---|---|
| Clean Wild Vm | Manual submission | 1. Clear residual ECS instances. 2. Complete O&M. |
| Start Crashed Vm | Automatic submission Manual submission | 1. Restore ECS instances after a crash occurs. 2. Start ECS instances. 3. Complete O&M. |

O&M

| Stop MOC While CN Down | Automatic submission Manual submission | 1. Completes authorization as the administrator of the Apsara Uni-manager Operations Console: Log on to the Apsara Uni-manager Operations Console. In the top navigation bar, choose Platform Operation > O&M Change > Process Approval. In the left-side navigation pane, choose Process Approval > Pending Approval. On the Pending Approval page, complete authorization. Before you approve the proactive O&M workflow, make sure that the services on the physical server are running as expected. 2. Lock the server. 3. Clean the MOC after the CN of an ECS instance is down. 4. The physical server is down. 5. Shut down the physical server: Log on to the Apsara Uni-manager Operations Console. In the top navigation bar, choose Platform Operation > Apsara Infrastructure Management > Resource Management. On the corresponding page, approve the shutdown requests for server roles. 6. Wait until the ECS instances are migrated. 7. Wait until the physical server fails. 8. Perform the OOB restart on the physical server. 9. Complete O&M. |
|---|---|---|
| Clear memory fragments on the physical server. | Automatic submission Manual submission | 1. Lock the server. 2. Drop fragments. 3. Trim the memory. 4. Unlock the server. 5. Complete O&M. |
| Mark NC Down And Vm Migrate | Automatic submission Manual submission | 1. The physical server is down. 2. Complete O&M. |
| reload pync | Automatic submission Manual submission | 1. Complete authorization in the Apsara Uni- manager Operations Console. 2. Lock the server. 3. Reload PYNC. 4. Unlock the server. 5. Complete O&M. |

**Submit a repair ticket for local disks**

O&M

> **Note:** If the machine already has a pending workflow, complete the workflow before you submit a repair ticket. Otherwise, the submission does not take effect.

1. Click **Submit Repair Ticket for Local Disks**.
2. In the dialog box that appears, configure the following parameters and click **Report**.

| Parameter | Description |
|---|---|
| Machine | The hostname of the machine for which you want to submit a repair ticket. You must obtain the hostname from the physical machine on site. |
| Slot Number | The slot number. You must obtain it from the physical machine on site. |
| Cause | The reason for submitting the repair ticket for local disks. |

**Modify the status of a workflow**

**Prerequisites**

The proactive O&M workflow is in the Running state. Complete a workflow i. Find the workflow that you want to manage, move the pointer over **Change Workflow**
**Status** in the **Operation** column, and then select **Complete Workflow**.
O&M ii. In the message that appears, click **OK**. Cancel a workflow i. Find the workflow that you want to manage, move the pointer over **Change Workflow**
**Status** in the **Operation** column, and then select **Cancel Workflow**.
ii. In the message that appears, click **OK**.

##### 1.1.7.4 ECS physical machine O&M

You can use the Elastic Compute Service (ECS) physical machine O&M feature to create and view physical machine maintenance tasks.

**Background information**

If a physical machine cannot be repaired at the software level and must be deactivated for maintenance, you must notify your customer at the earliest opportunity and obtain approval before you can deactivate and repair the physical machine on site. After the physical machine is repaired, reactivate it and put it back into service in the computing cluster to which the physical machine belonged before it was deactivated.

**Limits**

You can deactivate physical machines only in computing clusters (CPU clusters and MOC clusters) for maintenance.

> **Note:** On the **Machines** tab of the **Computing Server O&M** page, you can view the names of clusters in the **Cluster** column. CPU clusters are named in the `ECS-CPU-X-XXXX` format, and MOC clusters are named in the `ECS-MOC-X-XXXX` format.

**Usage notes**

When you deactivate a physical machine, the ECS instances deployed on the physical machine are automatically migrated to other physical machines in the same cluster as the deactivated physical machine. After the physical machine is repaired and put back into service, it is automatically added to the computing cluster to which it belonged before it was deactivated. The migrated ECS instances are not migrated back to the physical machine.

> **Warning:** Service interruptions may occur during the instance migration process. We recommend that you deactivate the physical machine during off-peak hours.

If the destination physical machines to which the ECS instances are migrated have insufficient resources or encounter other issues, the migration fails. In this case, go to the Physical Machine Maintenance page, find the physical machine that you want to deactivate, and then click Details in the Operation column. On the maintenance details page of the physical machine, click **Retry** below **Step3: ncMaintenanceMigrateEcsInstance**. If the retry fails, you must manually migrate the ECS instances from the physical machine. After you manually migrate the ECS instances, go back to the maintenance details page of the physical machine and click **Retry** below **Step3: ncMaintenanceMigrateEcsInstance** to continue deactivating the physical machine. For more information about how to manually migrate ECS instances, see Computing server O&M or ECS instances. O&M
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Computing** > **Compute**
3. In the left-side navigation pane, choose **ECS Intelligent O&M** > **ECS Physical Machine**
**O&M**.
4. On the Physical Machine Maintenance page, click **Create Physical Machine**
**Maintenance Event**.

> **Note:** To create a physical machine maintenance task, you can also click **Deactivate for** **Maintenance** for a physical machine on the **Computing Server O&M** page. For more information, see Computing server O&M.

5. In the dialog box that appears, configure the following parameters and click **OK**.

| Parameter | Description |
|---|---|
| Cluster | The cluster to which the physical machine that you want to deactivate for maintenance belongs. You can select only a CPU or MOC cluster. |
| Machine | The physical machine that you want to deactivate for maintenance. |

O&M

| Operator | The name of the operator who deactivates the physical machine for maintenance. |
|---|---|
| Maintenance Reason | The reason for deactivating the physical machine for maintenance. |

6. View information about the physical machines that are deactivated for maintenance in the
following columns: **Hostname**, **Maintenance Event ID**, **IP**, **Original Cluster**,
**Maintenance Reason**, **Maintenance Status**, **Initiated At**, **Rack**, and **Operator**.
7. To view the maintenance details of a physical machine, click **Details** in the **Operation**
column. In the **Basic Information** section of the page that appears, view the IP address, maintenance event ID, current step, maintenance status, start time, end time, and original cluster of the physical machine. In the **Execution Information** section, view the procedure of deactivating the physical machine for maintenance. If **Step5: offlineEcsNc** is complete, the physical machine is deactivated in its cluster and you can repair the physical machine. O&M

> **Note:** Take note of the following steps in the deactivation procedure:
> **Step1: ncOfflinePreCheck**: If the physical machine does not meet the requirements for deactivation, this step fails.
> **Step3: ncMaintenanceMigrateEcsInstance**: If the ECS instances fail to be migrated from the physical machine, this step fails. In this case, we recommend that you click **Retry** below **Step3:** **ncMaintenanceMigrateEcsInstance** to migrate the instances again. You can also manually migrate the ECS instances and then click **Retry** below **Step3:** **ncMaintenanceMigrateEcsInstance**. For more information about how to manually migrate ECS instances, see Computing server O&M or ECS instances.
> **Step4: offlineTianjiNc**: This step takes the physical machine out of service in Apsara Infrastructure Management and requires an extended period of time to complete. View the status of the physical machine in the Apsara Infrastructure Management console.

8. After you confirm that the physical machine is repaired, you must click **Maintenance**
**Completed below** below **Step6: AsoAuthorizationWork**. In the message that appears,
click **OK**. The procedure of deactivating the physical machine for maintenance is automatically executed. When **Step9: Finish** is complete, the procedure is complete and the physical machine is automatically added back to its original computing cluster.

> **Note:** If **Step8: expandTianjiClusterMachineExternal** remains in the **rolling** state, check the status and the **rolling** progress of the computing cluster to which the physical machine belongs in the Apsara Infrastructure Management console.

#### 1.1.8 Computing O&M settings

This topic describes how to configure Elastic Compute Service (ECS) metrics and O&M actions.

**Monitoring settings**

**Background information**

This section describes how to enable the feature of pushing alerts to the Apsara Uni-manager Operations Console for ECS metrics and configure alert levels.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Computing** > **Compute**
3. In the left-side navigation pane, click **ECS O&M Settings**.
4. On the **Monitoring** tab, view different types of metrics. The metric information is displayed
in the following columns: **Metric**, **Description**, **Monitoring Type**, **Resource Type**, **Push**
**to Apsara Uni-manager Operations Console**, and **Apsara Uni-manager Operations**
**Console Alert Level**. The following table describes the types of monitoring metrics.
O&M

| Type | Description |
|---|---|
| Control-side Monitoring | The metrics on the ECS software control side. For example, the monitor data loss too long metric indicates that monitoring data is _ _ _ _ unexpectedly missing for an extended period of time. |
| Virtualization Monitoring | The metrics for the virtualization services on ECS physical machines. For example, the vm monitor qemu exception indicates that an exception _ _ _ occurs during the collection of virtualization-related monitoring data of VMs. |
| System Monitoring | The metrics for the operating systems of ECS physical machines. For example, the cgroup mem limitation metric indicates that the memory _ _ usage of a cgroup exceeds the limit. |
| Hardware Monitoring | The metrics for ECS physical machine hardware. For example, the hardware exception alarm metric indicates that alerts are triggered due _ _ to hardware exceptions. |
| Hang Monitoring | The metrics for the breakdowns of ECS physical machines. For example, the nc hang exception metric indicates that ECS physical machines freeze. _ _ |
| Failover Monitoring | The metrics for physical machine-triggered failovers of ECS instances. For example, the nc down alert metric indicates that ECS instances fail when _ _ the physical machine on which the instances reside is down. |

5. Configure the alert settings for metrics.
i. Find the metric that you want to manage and click **Edit** in the **Operation** column. ii. In the dialog box that appears, modify the parameters and click **OK**. O&M

| Parameter | Description |
|---|---|
| Push Alert to Apsara Uni- manager Operations Console | Specifies whether to push the triggered alerts to the alert list in the Apsara Uni-manager Operations Console. By default, the alerts are pushed. If you enable the feature of pushing alerts to the Apsara Uni-manager Operations Console, the information about the triggered alerts is displayed in the alert list. You can troubleshoot issues based on the alert information. Important If you disable the feature of pushing alerts, the triggered alerts are not pushed to the alert list. In this case, you cannot find the alerts in the alert list and may fail to obtain important alert information. |

O&M

| Apsara Uni- manager Operations Console Alert Level | The alert level. You can modify this parameter based on your business requirements. Note The value of the Apsara Uni-manager Operations Console Alert Level parameter is consistent with that in the Alert Level column in the alert list in the Apsara Uni-manager Operations console. Description of alert levels: P1: critical P2: major P3: minor P4: information For the metrics of the Control-side Monitoring, Virtualization Monitoring, System Monitoring, Hardware Monitoring, and Failover Monitoring types: Default value: P3. Valid values: P2, P3, and P4. For the metrics of the Hang Monitoring type: Default value: P1. Valid values: P2, P3, and P4. Important If you changed the alert level for a failover monitoring metric from P1 to P2, P3, or P4, you cannot roll back the alert level to P1. |
|---|---|

**O&M action settings**

**Background information**

This section describes how to configure throttling and approval settings for active O&M actions.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Computing** > **Compute**
3. In the left-side navigation pane, click **ECS O&M Settings**.
4. On the **O&M Actions** tab, view the information about active O&M actions in the following
columns: **OpsCode** (O&M Type), **Throttling Status**, **Throttling Effective Time**, **Support**
**for Manual Reporting**, **Approval for Manually Reported O&M Workflow**, **Regional**
**Throttling Window** (Minutes), **Regional Throttling Threshold**, **Cluster-wide**
**Throttling Window** (Minutes), **Cluster-wide Throttling Threshold**, and **Throttling**
**Policy**.
O&M
5. Configure the throttling settings.

> **Note:** You can configure throttling for active O&M actions to meet on-site O&M requirements. For example, an active O&M action is configured to be performed when a physical machine is down.
> After the O&M workflow is started, if the environmental issue is not resolved, the physical machine is deactivated and restarted until the breakdown issue is resolved. In this case, if you configure throttling for the active O&M action to perform the action only once within 60 hours, the Apsara Uni-manager Operations Console automatically stops the O&M workflow after the action is performed once. Then, you can perform other O&M operations to resolve the issue at the earliest opportunity.

i. Find the active O&M action that you want to manage and click **Configure Throttling** in the **Operation** column.

> **Important:** If the number of times that an active O&M action is performed in a region or cluster reaches the specified threshold, the Apsara Uni-manager Operations Console no longer performs the active O&M action.

O&M ii. In the dialog box that appears, configure the parameters and click **OK**.

| Parameter | Description | Default value |
|---|---|---|
| Throttling | Specifies whether to enable throttling. Valid values: Disable Enable | Enable |
| Throttling Window (Minutes) | This parameter is displayed only if you enable throttling. This parameter specifies the period of time during which the active O&M action is performed in a region. | 10080 |
| Throttling Threshold | This parameter is displayed only if you enable throttling. This parameter specifies the maximum number of times that the active O&M action can be performed in a region. | 1 |
| Cluster-wide Throttling Window (Minutes) | This parameter is displayed only if you enable throttling. This parameter specifies the period of time during which the active O&M action is performed in a cluster. | 10080 |
| Cluster-wide Throttling Threshold | This parameter is displayed only if you enable throttling. This parameter specifies the maximum number of times that the active O&M action can be performed in a cluster. | 1 |
| Throttling Policy | This parameter is displayed only if you enable throttling. You can set this parameter only to Cancel. If the number of times that the active O&M action is performed reaches the specified threshold, the O&M workflow is automatically stopped. | Cancel |

6. Configure the approval settings.
O&M

> **Note:** You can submit active O&M workflows and adjust the approval step for active O&M workflows based on your business requirements to meet on-site O&M requirements. For example, the active O&M workflow can be executed without approval. For example, you can set the **Support for Manual Reporting** parameter to No for the **0x400012 Force NC OOB Reboot** O&M action. In this case, the active O&M action is unavailable in the **Submit Proactive O&M** **Event** dialog box when you submit active O&M events. This effectively reduces accidental operations.

> **Important:** Skipping the approval may affect the subsequent auditing. We recommend that you retain the approval step and set the approver to the administrator of the Apsara Uni-manager Operations Console.
> By default, you must contact the administrator of the Apsara Uni-manager Operations Console. To complete the approval as an approver, perform the following operations: Log on to the Apsara Uni-manager Operations Console. In the top navigation bar, choose **Platform Operation** > **O&M Change** > **Process Approval**. In the left-side navigation pane, click **Pending Approval**. After an active O&M workflow is approved, the workflow can be executed.
> The active O&M actions that support or do not support manual submission and manual approval are displayed in the Apsara Uni-manager Operations Console. The approval settings of specific active O&M actions cannot be modified. For example, the **0x4000A000000007 Unlock Nc** O&M action supports manual submission but does not support manual approval by default. In this case, the workflow of the active O&M action can be directly executed without approval after the workflow is submitted.

i. Find the active O&M action that you want to manage and click **Configure Approval** in the **Operation** column. O&M ii. In the dialog box that appears, configure the parameters and click **OK**.

| Parameter | Description |
|---|---|
| Support for Manual Reporting | Specifies whether to support manual submission. Default value: Yes. Valid values: Yes: supports manual submission. This active O&M action is available when you submit active O&M events. No: does not support manual submission. This active O&M action is unavailable when you submit active O&M events. For more information about how to submit active O&M events, see the "Submit proactive O&M events" section of the ECS O&M events topic. |
| Approval for Manually Reported O&M Workflow | This parameter is displayed only if you set the Support for Manual Reporting parameter to Yes. This parameter specifies whether approval is required for submitted active O&M events. Default value: Yes. Valid values: Yes: Approval is required for submitted active O&M events. No: Approval is not required for submitted active O&M events. |

#### 1.1.9 ECS workflows

This topic describes how to view the workflow information of an ECS instance, including how to view the workflow details and perform related operations. To use the ECS Workflow page, we recommend that you seek the help of an Alibaba Cloud L2 maintenance engineer.

**View workflow information and activity details**

1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Computing** > **Compute**
3. In the left-side navigation pane, click **ECS Workflow**.
4. On the Workflow page, click **Advanced Filter**. Then, specify parameters such as
**Workflow ID**, **Workflow Name**, **Workflow Status**, **Business ID**, **Apsara Stack Tenant**
**Account ID**, **InstanceId**, and **Time Range** to filter workflows.
O&M

> **Note:** Valid values of the **Workflow Status** parameter include:
> SCHEDULABLE: The workflow can be scheduled.
> HUMAN_PROCESSING: The workflow needs to be manually processed.
> RUNNING: The workflow is running.
> COMPLETED: The workflow is complete.
> FAILED: The workflow failed.
> TERMINATED: The workflow is terminated.

5. View the information about workflows in the columns, including **Workflow Name**,
**Workflow ID**, **Business ID**, **Apsara Stack Tenant Account ID**, **InstanceId**, **Start Time**,
**End Time**, **Execution Node**, and **Execution Status**.
6. Find the workflow that you want to view and click **Activity Details** in the **Operation**
column. On the Activity Details page, view the workflow details in the columns, including
**Activity ID**, **Activity Name**, **Method**, **Status**, **Input**, **Output**, **Exception**, **Start Time**,
and **End Time**.

**Restart a workflow**

**Prerequisites**

The workflow that you want to restart is in the **COMPLETED**, **FAILED**, or
**HUMAN_PROCESSING** state.
1. On the Workflow page, find the workflow that you want to restart and click **Restart** in the
**Operation** column.
2. In the message that appears, click **OK**.

**Roll back a workflow**

**Prerequisites**

The workflow that you want to roll back is in the HUMAN_PROCESSING state. O&M
1. On the Workflow page, find the workflow that you want to roll back and click **Roll Back** in
the **Operation** column.
2. In the message that appears, click **OK**.

**Terminate a workflow**

**Prerequisites**

The workflow that you want to terminate is in the HUMAN_PROCESSING state.
1. On the Workflow page, find the workflow that you want to terminate and click **Terminate** in
the **Operation** column.
2. In the message that appears, click **OK**.

#### 1.1.10 Computing O&M data

The Computing O&M Data module intuitively displays data in the current environment, including migrated data, data of custom instance types, O&M data, and monitoring data. The data helps you understand the abnormal monitoring data, changes in the resources on which proactive O&M operations are performed, migrated data changes, and status changes in the current environment. This topic describes how to view computing O&M data.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Computing** > **Compute**
3. In the left-side navigation pane, click **Computing O&M Data**.
4. View computing O&M data.
By default, the computing O&M data of the last seven days is displayed on the Computing O&M Data page. You can select 7 Days, 1 Month, 3 Months, or 6 Months from the Time Range drop-down list in the upper-right corner of the page to view data in the time range. To analyze detailed O&M data, click **Export O&M Data** in the upper-right corner to export the O&M data to your computer for analysis.

| Section | Description |
|---|---|
| ECS O&M Resource Overview | This section displays the numbers of Elastic Compute Service (ECS) instances, physical machines, and clusters that are available in the current environment. |
| Migrated Data Overview | This section displays the numbers of instances on which hot migration is performed, instances on which cold migration is performed, and migrated physical machines in the current environment. |
| Custom Instance Overview | This section displays the total number of custom instance types in the current environment. You can click View Details in the upper-right corner of the Custom Instance Overview section to go to the Specifications page. For more information about custom instance types, see Custom instance types. |

O&M

| Physical Machine O&M | This section displays the number of O&M operations performed on physical machines, number of physical machines on which O&M operations were performed, and number of physical machines on which O&M operations are being performed in the current environment. You can click View Details in the upper-right corner of the Physical Machine O&M section to go to the Proactive O&M page. |
|---|---|
| Instance O&M | This section displays the number of O&M operations performed on ECS instances, number of ECS instances on which O&M operations were performed, and number of ECS instances on which O&M operations are being performed in the current environment. You can click View Details in the upper-right corner of the Instance O&M section to go to the Proactive O&M page. |
| ECS Monitoring & Alerting Statistics | This section displays the top 10 ECS O&M alerts of the P1 to P3 levels that have been handled in the last week in the current environment. The time range cannot be modified. To view all alerts, you can click View Details in the upper-right corner of the ECS Monitoring & Alerting Statistics section to go to the Alerts page. For more information, see Alerts in Apsara Uni-manager Operations Console User Guide |

#### 1.1.11 Tiangong O&M

##### 1.1.11.1 Tiangong products

This topic describes how to view the basic information about cloud products that are deployed on ECS in the Tiangong 1.0 and Tiangong 2.0 architectures.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Computing** > **Compute**
3. In the left-side navigation pane, choose **Tiangong O&M** > **Tiangong Product**.
4. View data on the Tiangong cloud products page. By default, the system displays the details
of cloud products deployed on ECS, including the cloud product name, Tiangong architecture, and number of Tiangong machine groups. In the upper-left corner of the Tiangong cloud products page, you can enter a cloud product name in the search box to search for the cloud product.
5. View the details of a cloud product.
O&M i. Find the cloud product that you want to view and click **Details** in the **Operation** column. The details page of the cloud product appears. ii. On the **Overview** tab, view information in the **Basic Information** and **Tiangong**
**Resource Inventory** sections.
**Basic Information**: includes the **Tiangong architecture** and **Number of Tiangong**
**machine groups** parameters.
**Tiangong Resource Inventory**: allows you to view information in the **Machine**
**Group ID**, **Resource Template**, **Number of produced instances**, and **Number of**
**production instances** columns.
Enter a machine group ID in the search box to search for the machine group. iii. Click the **Tiangong Machine Group** tab. On the Tiangong Machine Group tab, view information about machine groups in the **Type**, **Resource Template**, **VM Image**,
**Supported specifications (families)**, **Deployment policy**, and **Instances**
**(Created/Total)** columns.
Enter a machine group ID in the search box to search for the machine group. Find the machine group that you want to view and click the value in the **Resource**
**Template** column. In the Resource Template Details panel, view the details of the
resource template of the machine group. Find the machine group that you want to view and click the value in the **Instances**
**(Created/Total)** column. In the Instance Details panel, view the status of the
instances.

##### 1.1.11.2 Tiangong workflows

This topic describes how to view the information about Tiangong workflows that are triggered by the tasks sent by Apsara Infrastructure Management Framework. The workflow information includes status information such as resource processing and instance cloning. This topic also describes common O&M operations to facilitate the Tiangong management.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Computing** > **Compute**
O&M
3. In the left-side navigation pane, choose **Tiangong O&M** > **Tiangong Workflow**.
4. By default, the information about workflows that are triggered by tasks sent by Apsara
Infrastructure Management Framework is displayed on the Tiangong workflow page. The information includes **Workflow ID**, **Workflow Initiator**, **Workflow Type**, **Instance**
**ID/hostname**, **Workflow status**, and **Exception Information**.

> **Note:** **Workflow Initiator**: The value of this parameter is globally unique and consists of information about a project, a cluster, and a server role group in Apsara Infrastructure Management.
> **Workflow Type**: The valid values of this parameter include Single Instance Creation, Single Instance Update, Instance Deletion, Instance Cloning, and Instance Recloning.
> **Instance ID/hostname**: You can click the value in the **Instance ID/hostname** column to view the instance details. For more information, see the 7. View the details of an instance section of the "ECS instances" topic.
> **Workflow status**: The valid values of this parameter include Complete and Failed.
> **Exception Information**: You can view the details of a workflow failure.

5. Click **Advanced Filter** and filter workflows by **Workflow ID**, **Workflow Type**, and
**Hostname**.
6. View workflow logs.
i. Find the workflow that you want to manage and click **View workflow logs** in the
**Operation** column.
O&M ii. In the Workflow logs panel, specify a time range and view the workflow logs within the specified time range. You can view the information about each log, including the time, log level, and log content.

> **Note:** You can view logs only within the last seven days.

## 2 Network operations

### 2.1 Network Operations Console

#### 2.1.1 Dashboard

##### 2.1.1.1 Overview

The Overview page displays the key metrics of network services to help users keep track of the status of services and devices at the earliest opportunity.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
3. In the left-side navigation pane, choose **Dashboard** > **Overview**.
4. View the network dashboard information.

| Section | Description |
|---|---|

| Port Usage | Displays the port usage of network devices. You can click View Details to view the details of network devices in the following columns: Device Role, Device Name, IP Address, Usage, Device Status, Total Number of Ports, and Used. |
|---|---|
| Port Error Packet Statistics | You can select a time range to view the number of error packets generated by all device ports within the specified time range. Only the top five device ports with the most error packets are displayed. |
| Device Overview | Displays the models of network devices and the number of each model. |
| Network Monitoring | Alerts: displays the total number of alerts that are triggered by network devices. The right-side table displays the alert information including Alert Time, Alert Device, and Alert Item. You can click View Details to go to the Network Alert Dashboard page in the Network Monitoring & Alerting module. On this page, you can view the alert details. For more information, see Network alert dashboard. Alert Device: displays the number of network devices that trigger alerts. Alert item: displays the number of alert items for which alerts are triggered. |

| Automatic Backups | Displays the status of automatic backups and the number of backup files in each status. You can click View Details to view the details of automatic backups, including File name and Creation time. In the Backup details dialog box, you can select a backup file and click Export to download the backup file to your local device. |
|---|---|
| Traffic Dashboard | You can select a time range to view the input and output trend charts of the Server Load Balancer (SLB) and XGW clusters within the specified time range. |
| Configuration Synchronization | Displays the synchronization status of configuration files and the number of files in each status. |

##### 2.1.1.2 Network topology

On the Network Topology page, you can view the physical network topology.

**Prerequisites**

The NetworkBaseServiceCluster cluster for BaseServiceAll has been deployed and has reached the desired state.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
3. In the left-side navigation pane, choose **Dashboard** > **Network Topology**.
4. Select a data center from the **Data Center** drop-down list and view the physical network
topology of the selected data center. Click **Baseline topology** or **Dynamic Topology** to view the network topology of the corresponding type. If the **dynamic topology** or the **base topology** has data discrepancies, you can click
**Update topology** to update the topology.
Network devices displayed in different colors are in different states. Blue: A device is in a normal state. Orange: A device is in an abnormal state. If you choose to display the **baseline topology**, the **Real-time alert refresh** feature is available. If you do not enable this feature, the states of devices and links in the topology are not updated when an alert is generated. If you choose to display the **dynamic topology**, the **Real-time alert refresh** feature is not available.
5. View the network device information and interconnection link statuses.
Click a network device icon. In the Network Device Information panel, view the device information in the **Basic device information** and **Alert List** sections. Click a connection between two network devices. In the Interconnection link status panel, view the link status details in the **Link information List** and **Alert List** sections.

##### 2.1.1.3 Custom views

The Apsara Uni-manager Operations Console allows you to create a custom view. After the view is created, you can configure the content and rules of the view to summarize and demonstrate the monitoring data and graph information based on your business requirements.

**Prerequisites**

The NetworkBaseServiceCluster cluster for BaseServiceAll has been deployed and has reached the desired state.

**Create a view**

1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
3. In the left-side navigation pane, choose **Dashboard** > **Custom Views**.
4. On the Custom Views page, click **Create View**.
5. In the Create View dialog box, configure the **View Name** and **View Description**
parameters, and then click **OK**. After the view is created, the page of the view automatically appears.

> **Note:** The view name must be unique. If the **Data Already Existing** message appears, you must change the view name, and then click **OK** when no name conflict occurs.

6. Create a subview.
i. Click the icon in the view section. ii. In the Create Subview panel, configure the following parameters and click **OK**. After the subview is created, the page of the view automatically appears, on which the subview is displayed.

| Parameter | Description |
|---|---|
| Device | The device to be monitored. |
| Monitoring Type | The type of the monitoring metric. Valid values: interface: the switch interface, including the water level, packet error, and packet loss of the interface. hardware: the switch hardware, including the memory usage and CPU usage. capacity: others. This option is not supported. |
| Metric | The monitoring metric. |
| Submetric | The monitoring submetric. |

iii. You can create more subviews by repeating Step 6.

**Query a view**

1. In the upper part of the Custom Views page, select a view name from the drop-down list,
specify a time range, and then click **Search**.
2. The Custom Views page displays the monitoring charts of all the corresponding subviews.

**Delete a view**

**Delete a subview**

1. Search for the view that you want to manage.
2. Find the subview that you want to delete and click the
icon in the upper-right corner of the subview section.
3. In the message that appears, click **OK**.

**Delete a view**

> **Important:** If you delete a view, all subviews of the view are also deleted. Proceed with caution.

1. Search for the view that you want to delete.
2. In the upper-right corner of the view section, click **Delete View**.
3. In the message that appears, click **OK**.

#### 2.1.2 Basic network

##### 2.1.2.1 Network element management

Network elements are network devices such as vSwitches and routers. The Network Element Management module displays the basic information and status of physical network devices. The module also supports configuration management operations on physical network devices, including device management, password management, and configuration consistency comparison. For more information about the features of the Network Operations Console that are applicable to device manufacturers, see vSwitch Monitoring Capabilities Supported by Network Operations Console.

**Manage devices**

On the Device Management tab, you can view the monitoring information about physical network devices and configure collection settings for them.

**Manage network monitoring data**

**Background information**

On the **Network Monitoring** tab, you can view the basic information, status, and traffic monitoring information of physical network devices in Apsara Stack to stay updated with their health status.

**Prerequisites**

The NetworkBaseServiceCluster cluster for BaseServiceAll is deployed and has reached the desired state.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
3. In the left-side navigation pane, choose **Basic Network** > **Network Element**
**Management**.
4. On the **Network Monitoring** tab of the **Device Management** tab, specify the **IDC**
parameter to view the physical network devices in Apsara Stack. You can view information about the physical network devices in the columns, including
**Device Name**, **Management IP address**, **SN**, **Business Domain**, **Vendor**, **Model**, **Role**,
**Online Time**, **Ping status**, **Snmp status**, and **Last Updated**.

> **Note:** You can click **Export** in the upper-right corner of the Network Monitoring tab to export the information about the physical network devices to your computer.
> If the ping or Simple Network Management Protocol (SNMP) is abnormal, Unreachable in red is displayed in the **Ping status** or **Snmp status** column.
> In the upper-right corner of the Network Monitoring tab, you can enter a device name or an IP address in the search box to search for the physical network device, and then view its information.
> The **Management IP address**, **Ping status**, and **Snmp status** columns can be used to sort the physical network devices. The **Role** column can be used to filter the physical network devices.

5. Find the physical network device that you want to view and click its name or click **Details**
in the **Details** column to view the details of the physical network device. The following table describes the details of the physical network device.

| Section or tab | Description |
|---|---|

| Basic information | View the information about the device from the parameters, including Device Name, IP, SN, Vendor, Model, Role, Online time, Ping status, Snmp status, Last Updated, Release, and Software version. |
|---|---|
| Port | View the information about the ports of the device in the columns, including Port Name, Port rate, Port description, Management status, Operation Status, Peer Device, Peer interface, Peer description, and Last Updated. Note The Management status and Operation Status columns can be used to sort the ports of a device. If exceptions occur, Down in red is displayed in the Management status or Operation Status column. View the details of a port. a. Find the port that you want to view and click its name or clickS ee in the Details column to view the details of the port. b. View the basic information and usage data of the port. In the Water level data section, you can select a time range in the Quick query section or specify a custom time range in the upper-right corner to query traffic data within the specified time range. |

| CPU usage | View the CPU utilization of the device. |
|---|---|
| Memory usage | View the memory usage of the device. |

| Aggregation Port Management | View the information about all aggregation ports of the device. On the Aggregation Port Management tab, find the aggregation port that you want to view and click See in the Operation column to view the usage data of the aggregation port. |
|---|---|
| Alert information | View the alert information about the device. Note During routine O&M, you need to view the alert information about a device at the earliest opportunity. If no data is displayed on the Alert information tab, the device is running as expected. If alert events occur, the system displays the alert events that are not handled on the Alert information tab. You need to handle the alert events at the earliest opportunity. |

6. Optional. Delete the monitoring information of the network device.
i. Click **Delete** in the **Details** column of the device. ii. In the message that appears, click **Delete**.

**Configure collection settings**

**Feature description**

On the Collection settings tab, you can set the collection interval of physical network devices and manage out-of-band (OOB) CIDR blocks. Before you collect network device information, you must configure a collection interval. In the OOB CIDR block management section, you can configure the management scope of a physical network device. In most cases, operations engineers must add the loopback CIDR block in which the network device to be managed resides.

**Prerequisites**

The NetworkBaseServiceCluster cluster for BaseServiceAll is deployed and has reached the desired state.

**Background information**

If you use the network element management feature of the Network Operations Console for the first time, you must add the loopback CIDR block planned by the current network device in Apsara Stack. In most cases, the loopback CIDR block is the CIDR block specified by the netdev.loopback field in the planned IP address list. To expand the network and the loopback CIDR block, you must add the CIDR block involved in the expansion to the management scope. The procedure to add an expanded CIDR block is the same as that used to add the loopback CIDR block for the first time. Then, you can search for the CIDR block of the managed device on the Collection settings tab.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
3. In the left-side navigation pane, choose **Basic Network** > **Network Element**
**Management**.
4. On the **Device Management** tab, click the **Collection settings** tab.

| Section | Description |
|---|---|
| Collection cycle settings | i. In the Collection cycle settings section, configure the Automatic scan cycle (minutes), Device scan cycle (minutes), Port scan cycle (minutes), and Link scan cycle (minutes) parameters. Note If you have no special requirements, we recommend that you use the default values. ii. Click Submitted. Then, the system collects the device information based on your configurations. |
|   | Add a CIDR block. a. Click Add CIDR block. |

|   | peration |
|---|---|
| OOB CIDR block management | b. In the Add CIDR block dialog box, configure the following parameters. Then, click OK. Manage CIDR blocks: Enter an IP address and its subnet mask in CIDR notation. Example: 10.0.0.0/8. Computer room: Select a data center from the drop-down list. Business Domain: Select In-band or Out-of-band from the drop- down list. View CIDR blocks. a. In the search box above the CIDR clock list, enter an ID, a management CIDR block, or the name of a data center and click the icon to search for the CIDR block, and then view information about the CIDR block. b. View information about the CIDR blocks in the columns, includingI D, Management CIDR blocks, Computer room, Business Domain, Created, and Last modification. Modify a CIDR block. a. Find the CIDR block that you want to modify and clickE diting in the Operation column. b. In the Modify CIDR block dialog box, modify the parameter settings, and click OK. Delete a CIDR block. a. Find the CIDR block that you want to delete and clickD elete in the Operation column. b. In the message that appears, click OK. |

**Manage passwords**

You can modify the password of a physical network device.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
3. In the left-side navigation pane, choose **Basic Network** > **Network Element**
**Management**.
4. On the Network Element Management page, click the Password management tab. On the
**Password management** tab, query current network devices.

> **Note:** You can enter a device name in the search box to perform an exact search.

5. Select one or more devices whose passwords you want to modify and click **Add to**
**implementation**. Then, the devices whose passwords you want to modify are displayed in
the **Implementation equipment** section on the right.

> **Note:** To remove a device from the **Implementation equipment** section, you can click **Management** in the **Operation** column of the device, and then select **Delete**. You can also click **Empty** in the upper-right corner to remove all devices from the Implementation equipment section.

6. In the lower-right corner of the Password management tab, enter values in the **User name**
and **Old password** fields, and click **Verification**. The system verifies the old password before you can modify the passwords.

> **Note:** If multiple devices are added to the Implementation equipment section and the old passwords of the devices are different, you need to separately verify the old passwords.
> After the verification is passed, **Verified** is displayed in the Verification status column.

7. After the verification is passed, modify the passwords for one or more devices.
Modify the password of a device. a. In the Implementation equipment section, find the device whose password you want to modify, click **Management** in the **Operation** column, and then select **Set account**
**password**.
b. In the Set account password dialog box, configure the **User name** and **Password** parameters, and click **OK**. Modify the passwords of all added devices. a. In the lower part of the **Implementation equipment** section, click **Modify**. b. In the dialog box that appears, configure the **User name** and **Password** parameters, and click **OK**.

**Compare configuration consistency for devices**

You can compare the current configurations of a device with its configurations on startup and check whether the configurations are consistent.

**Prerequisites**

The NetworkBaseServiceCluster cluster for BaseServiceAll is deployed and has reached the desired state.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
3. In the left-side navigation pane, choose **Basic Network** > **Network Element**
**Management**.
4. On the Network Element Management page, click the **Configuration consistency**
**comparison** tab. On the Configuration consistency comparison tab, view the information
about the network devices in the columns, including **Device Name**, **Device**
**Manufacturer**, **Device logon IP address**, and **Result**.

> **Note:** You can enter a device name in the search box to perform an exact search.

5. Select one or more devices whose configurations you want to compare and click
**Consistency comparison**.
Click **Refresh status** to update the comparison status. Click **Export result** to export the comparison results to your computer for viewing.

##### 2.1.2.2 Syslog

The Syslog module records and stores the logs generated by network hardware devices in the system based on dimensions such as time, log level, and module to facilitate subsequent analysis and management. This helps you identify and solve issues to improve the availability and stability of devices.

**View logs**

1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
3. In the left-side navigation pane, choose **Basic Network** >**Syslog**.
4. On the Syslog page, click **Advanced Filter**. Then, configure the **Data Center**, **Source**
**Device**, **Recorded At**, **Log Content**, **Parsing Status**, **Log Level**, **Manufacturer**, and
**Alert Module** parameters to filter logs.
5. View the information about the logs that meet the filter conditions in the columns that are
described in the following table.

| Column | Description |
|---|---|
| Recorded At | The time when the log entry was recorded. You can sort log entries based on the column. |
| Log Content | The parsed log data, which is the content of the raw log. |
| Source Device | The source device from which the log data was collected. |
| Parsing Status | The parsing status of log data. Valid values: Parsed and Parsing Failed. Note Logs may fail to be parsed due to the following reasons: The log format does not meet the RFC 3164 specification. The network device from which the log data was collected is not produced by an asset-heavy manufacturer that is supported by Apsara Stack. |
| Log Level | The level of the log data. Valid values: Emergency, Alert, Serious, Error, Warning, Notification, Information, and Debugging. |
| Module | The module to which the log data belongs. |
| Raw Logs | The raw log data that is not parsed. |
| Manufacturer | The manufacturer of the network device. |

6. Find the log entry that you want to view and click **Details** in the Operation column. In the
Syslog Details panel, view more detailed information about the log, such as the alert matching results, module details, and location.

**What to do next**

**Export logs**

On the Syslog page, click **Export Logs** in the upper-left corner to export the logs to your computer for viewing.

> **Note:** By default, all logs are exported.

**Test the log parsing feature**

1. On the Syslog page, click **Test Analysis** in the upper-left corner.
2. In the Test Analysis dialog box, enter content in the **Original Text** field and click **Submit**.

> **Note:** If you click **Reset**, the content in the Original Text field is cleared.

3. In the Parsing Results section, view the parsed information, such as the description,
hostname, and log level.

##### 2.1.2.3 HPN management

> **Note:** By default, the HPN Management module is not displayed. To use this module, perform the following operations: Log on to the Apsara Uni-manager Operations Console. In the top navigation bar, choose More > **User Authorities**. In the left-side navigation pane, click **Menu Management**. On the Menu management page, modify the menu settings to display the HPN Management module.

###### 2.1.2.3.1 HPN network elements

> This topic describes how to view High Performance Network (HPN) network device assets and monitoring and O&M information in the Apsara Uni-manager Operations Console.

**ocedue**

1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
3. In the left-side navigation pane, choose **Basic Network** > **HPN Management** > **HPN**
**Network Elements**.
4. On the HPN Network Element page, configure the **Select IDC** parameter and specify the
name of a network element to search for the network element.
5. Click the name of the network element or click **Details** in the **Operation** column of the
network element to view the details of the network element. On the details page of the network element, view the basic information about the network element. On the **Port** tab, view port information. Click the name of the port that you want to view or click **View** in the **Details** column of the port to view the port details. On the **CPU Utilization** tab, view CPU utilization. On the **Memory Utilization** tab, view memory usage. On the **Aggregation Port Management** tab, view the information about aggregation ports. Find the aggregation port that you want to view and click **View** in the **Actions** column to view the usage data charts of the aggregation port. On the **Alert** tab, view the alert information about the network element. Find the alert that you want to view and click **View** in the **Alert Details** column to view the alert details.

**Delete a network element**

1. On the HPN Network Element page, find the network element that you want to delete and
click **Delete** in the **Operation** column.
2. In the message that appears, click **OK**.

> **Note:** Deleted network elements cannot be restored. Proceed with caution.

###### 2.1.2.3.2 RDMA network interface O&M

The remote direct memory access (RDMA) network interface O&M feature can regularly check the performance metrics of an RDMA network interface by using performance monitoring. This helps you identify issues at the earliest opportunity, quickly troubleshoot and resolve issues, and ensure network stability and reliability.

**Terms**

**RDMA** is a high-speed network technology used to resolve delays in server-side data
processing during network transmission. RDMA directly sends data to the storage area of a computer over the network. During the process, data is quickly transmitted from one system to the memory of a remote system. RDMA implements direct memory access between hosts without affecting the operating system, accelerates data transmission, and reduces CPU load.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
3. In the left-side navigation pane, choose **Basic Network** > **HPN Management** > **RDMA**
**Card O&M**.
4. In the upper-right corner of the RDMA Card O&M page, select a data source from the **Data**
**Source** drop-down list. The following data sources are available:

**Bare Metal Server (BMS)**

**Platform of Artificial Intelligence (PAI)**

**Cloud Parallel File System (CPFS)**

**Super Computing Cluster (SCC)**

> **Note:** If you select **PAI**, you must configure the **Cluster** and **ViewType** parameters.
> If you select **CPFS** or **SCC**, you must configure the **Cluster** parameter.

5. On the **Cluster** tab, view the monitoring data of a cluster.

| Section | Description |
|---|---|

| Average QP | The average number of queue pairs (QPs) in the RDMA network. If you select PAI as the data source, this metric is not displayed. If the QPs are insufficient, the communication queue in the RDMA network may be congested, which compromises the efficiency and stability of data transmission. Excessive QPs may increase the overhead, complexity, and failure rate of the system. Note QP is a key term of the RDMA network. It refers to the communication queue between a pair of endpoints. |
|---|---|
| Abnormal Networks | The number of times that network device or traffic exceptions occur in the RDMA network. |
| Average Throughput Sent by RDMA (Mbit/s) | The average amount of data that is sent by all nodes in the RDMA network per second. |
| Average Throughput Received by RDMA (Mbit/s) | The average amount of data that is received by all nodes in the RDMA network per second. |
|   | i. On the right side of the monitoring chart, specify a time range to view the corresponding monitoring data. ii. In the Throughput Dashboard section, view the data of the RDMA TX BYTES and RDMA RX BYTES metrics within the specified time _ _ _ _ range. The RDMA TX BYTES metric specifies the number of bytes that are _ _ sent over the RDMA network per second. The RDMA RX BYTES metric specifies the number of bytes that are _ _ received over the RDMA network per second. |

| Monitoring Chart | iii. In the Display the Basic Data of RDMA Network section, view the data of the following metrics within the specified time range. The RDMA IGNORE CNP AVG metric specifies the average number _ _ _ of congestion notification packets (CNPs) that are ignored in the RDMA network per second. Note A CNP is used for network congestion control. When network congestion occurs, CNPs are sent to notify the sender to decrease the sending rate to prevent network congestion and packet loss. The RDMA OOB AVG metric specifies the average number of Out-of- _ _ Band (OOB) packets that are processed in the RDMA network per second. |
|---|---|
|   | Note OOB data is a special type of data transmitted over the RDMA network. The RDMA OOS AVG metric specifies the average number of Out-of- _ _ Order (OOS) packets that are processed in the RDMA network per second. Note OOS data is a special type of data transmitted over the RDMA network. OOS data is generated when packet loss or delay occurs during data transmission. The RDMA SENT CNP AVG metric specifies the average number of _ _ _ CNPs that are sent over the RDMA network per second. The RDMA HANDLE CNP AVG metric specifies the average number _ _ _ of CNPs that are processed in the RDMA network per second. The RDMA TX BYTES AVG metric specifies the average number of _ _ _ bytes that are sent over the RDMA network per second. The RDMA RX BYTES AVG metric specifies the average number of _ _ _ bytes that are received over the RDMA network per second. |
| RDMA Network Overview | You can view the node information in the following columns:N ode, Outbound Throughput, Inbound Throughput, Network QP, CNP Processed by Network, Out-of-order Data Packets, and Network Buffer Overflow. |

6. On the **Node** tab, view the monitoring data of nodes.

| Parameter | Description |
|---|---|
| QP in RDMA Network | The monitoring data of a node in the RDMA network. For more information about these metrics, see the description of them in the previous step. |
| Abnormal Networks |   |
| Throughput Sent by RDMA Network (Mbit/s) |   |
| Throughput Received by RDMA Network (Mbit/s) |   |
| Monitoring Chart |   |

###### 2.1.2.3.3 HPN performance analysis

The Apsara Uni-manager Operations Console provides the High Performance Network (HPN) performance analysis feature. This feature analyzes the maximum load and pressure resistance of the software and hardware by testing the performance of a machine under stress conditions. This helps you identify the pressure resistance limit of the machine and provides data support for O&M personnal to improve network performance.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
3. In the left-side navigation pane, choose **Basic Network** > **HPN Management** > **HPN**
**Performance Analysis**.
4. On the HPN performance analysis page, click **Create a test** to create an analysis task.
The following table describes the parameter combinations for an analysis task.

| Test cluster | Protocol type | Test type | Required parameters | Traffic model | Node |
|---|---|---|---|---|---|
| All | RDMA | Traffic test | Number of QPS tested Node Port Test duration (s) GDR | MtoN | Server Client |
|   |   |   |   | FullMesh | Server |
|   |   | Latency test | Node Port | N/A | Server |
|   | TCP | Traffic test | Node Port Test duration (s) Concurrent connections | MtoN | Server Client |
|   |   |   |   | FullMesh | Server |

The following table describes the parameters.

| Parameter | Description |
|---|---|
| Number of QPS tested | The number of test processes. This parameter determines the test bandwidth. |
| Node Port | The port number used for the test. |
| Test duration (s) | The duration of the test. Unit: seconds. |

| GDR | Specifies whether to enable direct communication between GPUs If you turn on this switch, the system associates the Remote Direct Memory Access (RDMA) network interface controller (NIC) with the corresponding GPU for traffic testing. Make sure that the machine supports this feature before you turn on the switch. |
|---|---|
| Concurrent connections | The number of connections that can be processed at the same time. |
| MtoN | The many-to-many relationship model. This model is used to test the one-way connectivity between Client nodes and Server nodes, including the one-way connectivity between a single Client node and a single Server node and between multiple Client nodes and multiple Server nodes. |
| FullMesh | All nodes in the network topology are connected to each other. This option allows you to test the two-way connectivity between all destination nodes. |
| Client | The sender of the test traffic. |
| Server | The receiver of the test traffic. |

5. Click **Submit**. Then, the analysis task is created.
Click **Cancel** to go back to the page for creating an analysis task. You can modify the parameters based on your business requirements. Click **View task details** to go to the **Analysis Task details** page.

**What to do next**

**View task details**

1. On the **HPN performance analysis** page, click Advanced Filter and filter tasks by **Start**
**and end time**, **Task ID**, **Test type**, **Protocol Type**, **Traffic model**, **Task Status**, or their
combinations.
2. Click **Details** in the Actions column of a task.
3. On the **Analysis Task details** page, view the task information and analysis results.

**Refresh a task**

Click **Refresh** in the Actions column of a task to refresh the task.

###### 2.1.2.3.4 HPN instant diagnostics

High Performance Network (HPN) instant diagnostics refer to a diagnosis on HPN nodes. During the diagnosis, the system software, network, and GPU of nodes are checked. After the diagnosis, the diagnostic results and details are provided to help administrators troubleshoot network performance issues.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
3. In the left-side navigation pane, choose **Basic Network** > **HPN Management** > **HPN**
**Instant Diagnostics**.
4. On the HPN instant diagnosis page, select a test cluster and one or more nodes from the
drop-down lists and then click **Diagnosis**.

> **Note:** You can select multiple nodes at a time.

5. View the diagnostic results.

| Diagnostic result | Description |
|---|---|
| Diagnostic Item | Displays the diagnostic items, including OS Release Version, OS Kernel Version, Server CPU Model, Server Disk Space, RDMA NIC Drive Installation, RDMA NIC Drive Load, bonding Module Installation, GDR Module Installation, GDR Module Load, Number of RDMA Devices, RDMA Device Firmware Version, RDMA Device Aggregation Mode, RDMA Device Aggregation Status, RDMA Device Hash Policy, RDMA Device Port Rate, RDMA Device MTU Settings, PCIe MRR Configuration, PCIe Link Details, PCIe Link Rate, PCIe Link Width, and GPU Online Check. |
| Diagnostic Result | Displays the diagnostic result of each diagnostic item. The result can beP assed or Failed. |
| Diagnostic Details | Displays the diagnostic details of each diagnostic item. For example, the RDMA device port rates are consistent. |
| Current Value | Displays the diagnostic value corresponding to each diagnostic item. |

##### 2.1.2.4 CPN

###### 2.1.2.4.1 CPN diagnosis

The Computing Platform Network (CPN) diagnosis feature checks the nodes in CPN and displays the diagnostic items, diagnostic details, and diagnostic results to help administrators better understand and manage network performance and troubleshoot issues.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
3. In the left-side navigation pane, choose **Basic Network > CPN Management > CPN**
**Diagnosis**.
4. Click **Create a diagnosis**, select a **cluster** and a **test node**, and then click **OK**.

> **Note:** You can select multiple nodes.

5. In the dialog box that appears, confirm that the selected parameters are correct and click
**OK**. The diagnostic task starts running immediately.
6. View diagnostic results.
i. Click **Details** in the **Actions** column of the diagnostic task.

| Diagnostic Analysis results | Description |
|---|---|
| Overview view | Displays the clusters, nodes, the total number of users, the number of normal users, and the number of abnormal users. |
| Details view | You can query diagnostic details by node or diagnostic item. |

ii. On the **Diagnostic Analysis results** page, click **Details view**. iii. Select **Node** or **Diagnostic Item** from the drop-down list, enter the node IP address or diagnostic item name in the search box, and then click .

> **Note:** Click **Advanced Filter** to query nodes and diagnostic items.

iv. On the Details view tab, you can view diagnostic results, diagnostic details, and error messages.

**What to do next**

On the **CPN one-click diagnosis** page, you can perform the following operations:

| Operation | Procedure |
|---|---|
| Filter diagnostic tasks | Basic filter i. Select Start and end time or Status from the drop-down list. ii. Select a time range or status to filter diagnostic tasks that meet the condition. Advanced filter i. Click Advanced Filter. ii. Set Start and end time and Status and click Search. |
| Retry | 1. Click Retry in the Actions column of the diagnostic task. 2. In the message that appears, click OK. |
| Delete | 1. Click Delete in the Actions column of the diagnostic task. 2. In the message that appears, click OK. |

###### 2.1.2.4.2 CPN performance analysis

You can perform a CPN performance analysis task to test the performance of machines under stress conditions. The task analyzes the maximum load and pressure resistance of the existing software and hardware. This helps identify the pressure limits of the machines and provides sufficient data for the O&M team to improve network performance.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
3. In the left-side navigation pane, choose **Basic Network > CPN Management > CPN**
**Performance Analysis**.
4. Click **Create a test** to create an analysis task.
The following table describes the parameter combinations for an analysis task in which Protocol Type is set to RDMA.

| Test cluster | Protoc ol type | Test type | Required parameter | Value of Traffic model | Node |
|---|---|---|---|---|---|
| Arbitrary | RDMA | Traffic test | Number of QPS tested Node Port Test duration (s) GDR | MtoN | Server Client |
|   |   |   |   | FullMesh | Server |
|   |   |   |   | Ring | Server |
|   |   | Latency Test | Node Port Test duration (s) | N/A | Server |

The following table describes the parameters you must configure to create an analysis task in which Protocol Type is set to RDMA.

| Parameter | Description |
|---|---|

| Number of QPS tested | The number of test processes. This parameter determines the test bandwidth. If the number of queue pairs (QPs) is insufficient, the related queues are blocked, which affects the efficiency and stability of data transmission. If the number of QPs is excessively large, the system overheads, complexity, and failure rate are increased. Note QP is a key concept in RDMA networks and is used to describe a queue between a pair of endpoints. |
|---|---|
| Node Port | The port number used for the test. |
| Test duration (s) | The duration of the test. Unit: seconds. |
| GDR | Specifies whether to enable GDR. If you turn on the switch, the system associates the eRDMA interface (ERI) with a GPU for traffic testing. Before you turn on the switch, check whether your machine supports the feature. If your machine does not support the feature, do not turn on the switch. |
| MtoN | Many to Many (MtoN) specifies a many-to-many relational model. This option allows you to test the one-way connectivity from Client nodes to Server nodes, including the one-way connectivity from a single Client node and a single Server node and from multiple Client nodes to multiple Server nodes. |
| FullMesh | All nodes in the network topology are connected to each other. This option allows you to test the two-way connectivity between all destination nodes. |
| Ring | Multiple nodes in the network topology form a closed loop. Data packets are sent from one node to the next node in sequence and finally returned to the original node. This option allows you to test the actual available network bandwidth. |
| Client | The sender of the test traffic. |
| Server | The receiver of the test traffic. |

The following table describes the parameters you must configure to create an analysis task in which Protocol Type is set to Communication Library.

| Test clust er | Protocol type | Test type | Communicati on library | Required parameter |
|---|---|---|---|---|

| Arbitr ary | Commun ication Library | Communi cation library test | NCCL CPN-CCL RCCL PCCL |   |   | Algorithm: the algorithm of the task. The algorithm bandwidth, bus bandwidth, and execution time of a task vary based on the algorithm. Communication primitive: the data transmission and processing methods vary based on the communication primitive. Select a value from the drop- down list. Timeout period (s): If the execution time of performance analysis test is greater than the specified timeout period plus 1 minute, the test task fails. Data type: the data type of the performance analysis test. Select a value from the drop-down list. Number of iterations: the number of times the current task is executed. Start bytes: the minimum amount of data to start the task. Number of cut-off bytes: the maximum amount of data to stop the task. Step factor: Specify an integer greater than 1. If you set the parameter to 2, the data specification increases by two times. The first row corresponds to the value of the Start bytes parameter and the last row corresponds to the value of the Number of cut-off bytes parameter. Host List: Click Add entry to add hosts. mpirun custom parameters: Specify custom parameters in the --mca ... - -mca ... format. Example: --mca |   |   |   |
|---|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   | --mca ... - |   |   |
|   |   |   |   |   |   | -mca ... |   |   |   |
|   |   |   |   |   |   |   |   | --mca |   |
|   |   |   |   |   |   | tcp,self --mca btl tcp if include _ _ _ |   |   |   |
|   |   |   |   |   |   | bond0 --mca oob tcp if include _ _ _ |   |   |   |
|   |   |   |   |   |   | bond0 --bind-to none |   |   |   |

5. Click **Submit**.

**Related operations**

The following table describes the operations that you can perform on the **CPN performance**
**analysis** page.

| Operation | Procedure |
|---|---|

| Query a test task | Basic filter After you specify the start time and end time, the system automatically filters test tasks. Advanced filter i. Click Advanced Filter. ii. Configure the Start and end time, Test type, Protocol Type, and Status parameters. iii. Click Search. |
|---|---|
| View performance analysis details | 1. Find the required test task and click Details in the Actions column. 2. View the basic information, analysis results, and device information of the task. |
| Retry a test task | 1. Find the required test task and click Retry in the Actions column. 2. In the dialog box that appears, click OK. The value in the Task Status column changes to In progress. |
| Delete a test task | 1. Find the required test task and click Delete in the Actions column. 2. In the message that appears, click OK. |
| Terminate a test task | 1. Find the required test task and click Terminate in the Actions column. 2. In the dialog box that appears, click OK. The value in the Task Status column changes to Terminating. If the value in the Task Status column changes to Terminated, the task is terminated. |

###### 2.1.2.4.3 CPN access gateways

###### 2.1.2.4.3.1 Manage RDMA devices

This topic describes how to manage Remote Direct Memory Access (RDMA) devices, including how to scan for and delete RDMA devices.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
3. In the left-side navigation pane, choose **Basic Network > CPN Management > CPN**
**Access Gateway**.
4. Select the **RDMA Device Management** tab.
5. Manage RDMA devices.
Scan for new devices Click **Scan New Devices** to add new RDMA devices to the system. Query new devices Basic filter a. Select **Device Name**, **Equipment manufacturer**, **Equipment model**, **Device**
**role**, **Device Management IP**, **Serial Number**, or **Device status** from the drop-
down list. b. In the search box, enter the device name or manufacturer, or select the status of the device, and click . Advanced filter a. Click **Advanced Filter**. b. Enter the device name, device manufacturer, device model, device role, device management IP address, and serial number, and select the device status. c. Click **Search**. Delete a new device a. Click **Delete** in the **Actions** column. b. In the message that appears, click **OK**.

###### 2.1.2.4.3.2 Manage RDMA device policies

This topic describes how to configure policies for Remote Direct Memory Access (RDMA) devices to manage RDMA devices in a centralized manner.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
3. In the left-side navigation pane, choose **Basic Network > CPN Management > CPN**
**Access Gateway**.
4. Click the **RDMA device policy management** tab.
5. Click **Create an RDMA device policy** and set the parameters. The following table
describes the parameters.

| Parameter | Description |
|---|---|
| Policy name | Enter a custom name for the policy. |
| Description | Enter the description of the policy. This parameter is optional. |
| Equipment manufacturer | Select a device vendor from the drop-down list. The system automatically displays the device vendors on the RDMA Device Management tab. |

| Device role | Select the role of the device to which the policy applies from the drop-down list. Valid values: RASW: the access vSwitch of the data exchange module in RDMA networking scenarios. RDSW: the core vSwitch of the data exchange module in RDMA networking scenarios. The core vSwitch is used to connect different access vSwitches. EHSW: the vSwitch that is used to connect to the custodian network in RDMA networking scenarios. |
|---|---|
| Equipment model | Select the model of the device to which the policy applies from the drop-down list. The system automatically displays the device models on the RDMA Device Management tab. |
| Device List | Select the device to which the policy applies from the drop-down list. The system automatically displays the devices of a specific device model on the RDMA Device Management tab. |
| Headroom | The size of the RDMA over Converged Ethernet (RoCE) queue buffer, and the maximum number of available cell resources in the headroom. Enter the size of the global buffer. |

6. Click **OK**.

**What to do next**

On the **RDMA device policy management** tab, you can perform the following operations:

| Operation | Procedure |
|---|---|
| Query the policy for an RDMA device | 1. Select Device Name, Equipment manufacturer, Equipment model, Device role, Device Management IP, Serial Number, or Device status from the drop-down list. 2. Enter the device name, device vendor, device model, device role, device management IP address, serial number, or device status in the search box and click . |
| View the details of the policy of an RDMA device | 1. Click Details in the Actions column. 2. Click OK or Cancel. |
| Retry the policy of an RDMA device | 1. Click Retry in the Actions column. 2. In the message that appears, click OK. |

###### 2.1.2.4.3.3 Manage policies for the RDMA device interface

**interface**

This topic describes how to manage interface policies, such as policy configuration, query, and retry.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
3. In the left-side navigation pane, choose **Basic Network > CPN Management > CPN**
**Access Gateway**.
4. Click the **RDMA device interface policy management** tab.
5. Click **Create an RDMA device interface policy** and configure the following parameters.

| Parameter | Description |
|---|---|
| Policy Name | Enter a custom name for the policy. |
| Description | Enter the description of the policy. This parameter is optional. |
| Device Vendor | Select a device vendor from the drop-down list. The system automatically displays the device vendors on the RDMA Device Management tab. |
| Device Role | Select the role of the device to which the policy applies from the drop-down list. Valid values: RASW: the access vSwitch of the data exchange module in Remote Direct Memory Access (RDMA) networking scenarios. RDSW: the core vSwitch of the data exchange module in RDMA networking scenarios. The core vSwitch is used to connect different access vSwitches. EHSW: the vSwitch that is used to connect to the custodian network in RDMA networking scenarios. |
| Device Model | Select the model of the device to which the policy applies from the drop-down list. The system automatically displays the device models on the RDMA Device Management tab. |
| Device List | Select the device to which the policy applies from the drop-down list. The system automatically displays the devices of a specific device model on the RDMA Device Management tab. |

| RoCE queue PFCs configuration (RDMA over Converged Ethernet) | Headroom cache threshold: the size of the RDMA over Converged Ethernet (RoCE) queue buffer, and the maximum number of available cell resources in the headroom. Back pressure frame trigger threshold: the analysis model of network traffic. The model ensures that the sum of the back pressure frame triggering thresholds for all ingresses is less than or equal to the tail-drops threshold for the egress. Offset between back pressure frame stop threshold and trigger threshold: When the number of cell resources used by packets with a 802.1p priority decreases by the value of this parameter after PFC is triggered, PFC stops sending PFC pause frames. PFCs reserved threshold: the number of cell resources reserved for packets with a 802.1p priority in the guaranteed storage capacity. PFCs: If you use PFC and congestion occurs in a specific type of traffic, the routing of other types of traffic is not affected. This ensures that different types of packets on the same link do not affect each other. Deadlock monitoring function: If a link or device failure occurs, temporary loops may occur during the route reconvergence period. In this case, PFC frames are repeatedly sent and received between devices, packets cannot be forwarded, cell resources in the interface buffer are occupied and cannot be released, and the device enters the PFC deadlock state. |
|---|---|
| RoCE queue WRED configuration | ECN function: Explicit Congestion Notification (ECN) uses the DiffServ field in the IP header to mark the congestion status along the packet transmission path. An ECN-capable terminal can determine whether congestion occurs on the transmission path based on the packet content. If congestion occurs, the terminal adjusts the method to send packets to prevent congestion from being aggravated. Lower limit of average queue length: the lower limit of the length of the queue that the packets of the forwarding device enter in the egress. The lower limit is also called ECN threshold. Upper limit of average queue length: When the device assigns packets to a queue in the outbound direction, the queue size reaches the upper threshold (ECN threshold). Discarding probability: the marking probability if ECN is used. A larger value indicates that more packets are marked between the upper and lower limits. |

| Note If the length of the queue that the packets of the forwarding device enter in the egress is smaller than the lower limit, the forwarding device directly forwards the packets from the egress without processing the packets. When the device assigns packets to a queue in the outbound direction, if the average queue size is between the lower threshold and the upper threshold, take note of the following items: If the value of the ECN field in the received packets is 00, the packets are sent out of an ECN-incapable terminal. In this case, the forwarding device determines whether to drop the packets based on the drop probability. If the value of the ECN field in the received packets is 01 or 10, the packets are sent out of an ECN-capable terminal. In this case, the forwarding devices change the value of the ECN field for some of these packets based on the drop probability and forward these packets. All incoming packets are not dropped. If the ECN field is 11 in a packet, the packet on the original device has experienced congestion along the transmission path. In this case, the device does not process the packet and directly forwards the packet out of the outgoing interface. When the device assigns packets to a queue in the outbound direction, if the average queue size exceeds the upper threshold, take note of the following items: If the ECN field is 00, the packets are sent out of an ECN- incapable terminal, the device drops the packets. . Click OK. If the value of the ECN field in the packet received by the device is 01 or 10, it indicates that the packet sender What to do next supports the ECN function. After the ECN field of the inbound packet is changed to 11, the packet continues to On the RDMA device interface policbye fmorawnaradgede,m anedn atl l tianbbo, uynodu p caacnke ptse arfroer nmot t dhiesc faordlleodw.ing operations: If the ECN field is 11 in a packet, the packet on the original |   | Note If the length of the queue that the packets of the forwarding device enter in the egress is smaller than the lower limit, the forwarding device directly forwards the packets from the egress without processing the packets. When the device assigns packets to a queue in the outbound direction, if the average queue size is between the lower threshold and the upper threshold, take note of the following items: If the value of the ECN field in the received packets is 00, the packets are sent out of an ECN-incapable terminal. In this case, the forwarding device determines whether to drop the packets based on the drop probability. If the value of the ECN field in the received packets is 01 or 10, the packets are sent out of an ECN-capable terminal. In this case, the forwarding devices change the value of the ECN field for some of these packets based on the drop probability and forward these packets. All incoming packets are not dropped. If the ECN field is 11 in a packet, the packet on the original |   |   |
|---|---|---|---|---|
|   |   |   | Note If the length of the queue that the packets of the forwarding device enter in the egress is smaller than the lower limit, the forwarding device directly forwards the packets from the egress without processing the packets. When the device assigns packets to a queue in the outbound direction, if the average queue size is between the lower threshold and the upper threshold, take note of the following items: If the value of the ECN field in the received packets is 00, the packets are sent out of an ECN-incapable terminal. In this case, the forwarding device determines whether to drop the packets based on the drop probability. If the value of the ECN field in the received packets is 01 or 10, the packets are sent out of an ECN-capable terminal. In this case, the forwarding devices change the value of the ECN field for some of these packets based on the drop probability and forward these packets. All incoming packets are not dropped. If the ECN field is 11 in a packet, the packet on the original |   |
|   |   |   | device has experienced congestion along the transmission path. In this case, the device does not process the packet and directly forwards the packet out of the outgoing interface. When the device assigns packets to a queue in the outbound direction, if the average queue size exceeds the upper threshold, take note of the following items: If the ECN field is 00, the packets are sent out of an ECN- incapable terminal, the device drops the packets. |   |
|   |   |   | If the value of the ECN field in the packet received by the device is 01 or 10, it indicates that the packet sender t supports the ECN function. After the ECN field of the inbound packet is changed to 11, the packet continues to interface policbye fmorawnaradgede,m anedn atl l tianbbo, uynodu p caacnke ptse arfroer nmot t dhiesc faordlleodw.ing If the ECN field is 11 in a packet, the packet on the original |   |
| Operation |   |   | device has experienced congestion along the transmission path. In this case, the device does not process the packet Procedure and directly forwards the packet out of the outgoing interface. |   |
| Query the policy for an RDMA device interface |   | 1. Configure the Policy Name, Device Vendor, Device Model, Device Role, or Device Management IP parameter. 2. Enter the policy name, device vendor, device model, device role, or device management IP address in the search box and click the icon. | 1. Configure the Policy Name, Device Vendor, Device Model, Device Role, |   |
| View the details of a policy of an RDMA device interface |   | 1. Click Details in the Actions column. 2. Click OK or Cancel. |   |   |
| Retry the policy for an RDMA device interface |   | 1. Click Retry in the Actions column. 2. In the message that appears, click OK. |   |   |

###### 2.1.2.4.4 RDMA NIC O&M

To perform O&M on Remote Direct Memory Access (RDMA) network interface cards (NICs), you must check the performance metrics of RDMA NICs. RDMA NIC O&M allows you to identify and troubleshoot issues and ensure network stability and reliability.

**Terms**

**RDMA**: RDMA is a high-speed network technology developed to reduce the delay of server-
side data processing in network transmission. RDMA transfers data directly into the memory of a computer over the RDMA network and enables direct memory access between hosts without affecting the operating system. This increases the data transfer speed and reduces the CPU load.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
3. In the left-side navigation pane, choose **Basic Network > CPN Management > RDMA**
**Card O&M**.
4. In the upper-right corner of the page, select **Data Source** and **Cluster**. You can set Data
Source only to CPN.
5. On the **Cluster** tab, view the monitoring information about the cluster.

| Section | Description |
|---|---|
| Average QP | The average number of queue pairs (QPs) in the RDMA network. If you select PAI for Data Source, this parameter is unavailable. If the number of QPs is insufficient, the queue is blocked, which affects the efficiency and stability of data transmission. If the number of QPs is excessively large, the system overheads, complexity, and failure rate increase. Note A QP is a key concept in RDMA networks and is used to describe the queue between a pair of endpoints. |
| Abnormal Networks | The number of times that network device exceptions or traffic exceptions occur in the RDMA network. |
| Average Throughput Sent by RDMA (Mbit/s) | The average amount of data sent by all nodes in the RDMA network per second. |
| Average Throughput Received by RDMA (Mbit/s) | The average amount of data received by all nodes in the RDMA network per second. |
|   | i. Select the start time and the end time on the right side of the monitoring chart to view the monitoring data within the time range. ii. In the Throughput Dashboard section, view the RDMA TX BYTES and _ _ RDMA RX BYTES metrics. _ _ RDMA TX BYTES is the number of bytes sent in the RDMA network. _ _ RDMA RX BYTES is the number of bytes received in the RDMA _ _ network. |

|   | iii. In the Basic Data of RDMA Network section, view the following data in the specified time range: RDMA IGNORE CNP AVG: the average number of ignored _ _ _ Congestion Notification Packets (CNPs) in the RDMA network. Note CNPs are packets used for network congestion control. When network congestion occurs, CNPs are sent to notify the sender to reduce the sending rate to avoid network congestion and packet loss. RDMA TX PFC PAUSE AVG: the average number of Priority-based _ _ _ _ Flow Control (PFC) packets when data is sent in the RDMA network. |
|---|---|
| Monitoring Chart | RDMA RX PFC PAUSE AVG: the average number of PFC packets _ _ _ _ when data is received in the RDMA network. RDMA OOB AVG: the average amount of out-of-band (OOB) data _ _ processed in the RDMA network. Note OOB data is a special type of data transmitted in an RDMA network. RDMA OOS AVG: the average amount of out-of-order (OOS) data _ _ processed in the RDMA network. Note OOS data is a special type of data transmitted in an RDMA network. OOS data is generated when packet loss or latency occurs during transmission. RDMA SENT CNP AVG: the average number of CNPs sent in the _ _ _ RDMA network. RDMA MARKED ECN AVG: the average number of marked Explicit _ _ _ Congestion Notification (ECN) packets in the RDMA network. RDMA HANDLE CNP AVG: the average number of CNPs processed _ _ _ in the RDMA network. RDMA TX PFC TRANS AVG: the average number of PFC packets _ _ _ _ that are enabled in the RDMA network. RDMA QP CNT AVG: the average number of QPs in the RDMA _ _ _ network. RDMA TX BYTES AVG: the average number of bytes of data sent in _ _ _ the RDMA network. RDMA RX BYTES AVG: the average number of bytes of data _ _ _ received in the RDMA network. |

| RDMA Network Overview | View the metrics of the nodes in the RDMA network, includingN odes, Outbound Throughput, Inbound Throughput, Network QP, CNP Processed by Network, Out-of-order Data Packets, and Network Buffer Overflow. |
|---|---|

6. On the **Node** tab, view the monitoring information of each node.

| Parameter | Description |
|---|---|
| QP in RDMA Network | Displays the monitoring data of a node. For more information, see the descriptions of the cluster metrics. |
| Abnormal Networks |   |
| Throughput Sent by RDMA Network (Mbit/s) |   |
| Throughput Received by RDMA Network (Mbit/s) |   |
| Monitoring Chart |   |

###### 2.1.2.4.5 CPN management

###### 2.1.2.4.5.1 CPN topology

This topic describes how to query the topology information about clusters and nodes.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
3. In the left-side navigation pane, choose **Basic Network > CPN Management > CPN**
**Network Management > CPN Topology**.
4. In the upper-left corner of the page, select **Cluster** and **Nodes**.
5. Click **Query** to query the topology information.

**What to do next**

After the topology is displayed, you can perform the following operations:

| Operation | Procedure |
|---|---|
| Zoom in or zoom out the topology | Click or in the upper-right corner of the topology to zoom in or zoom out the topology. |
| Reset the topology canvas | Click in the upper-right corner of the topology to reset the canvas. |

| Display the topology in full screen | 1. Click in the upper right corner of the topology to display the topology in full screen. 2. Click in the upper-right corner to exit the full screen. |
|---|---|

###### 2.1.2.4.5.2 CPN network element

> This topic describes how to view network devices and monitoring and O&M information in the cloud platform.

1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
3. In the left-side navigation pane, choose **Basic Network > CPN Management > CPN**
**Network Management > CPN Network Element**.
4. Select a data center from the drop-down list and enter a network element name in the
**Network element name** search box.
5. Click the name of a network element or click **Details** in the **Actions** column to go to the
details page of the network element.

| Tab | Description |
|---|---|
| Port | Displays the port information of the network element device. Click the port name or click View in the Actions column to view the usage data of the port. |
| CPU Utilization | Displays the CPU usage of the network element device. |
| Memory Utilization | Displays the memory utilization of the network element device. |

| Aggregation Port Management | Displays the aggregated port information of the network element device. Click View in the Actions column to view the traffic of the port. |
|---|---|
| Alert | Displays the alert information of the network element device. |

**What to do next**

On the **CPN network element** page, you can also perform the following operations:

| Operation | Procedure |
|---|---|
| Delete a CPN network element | 1. Click Delete in the Actions column. 2. In the message that appears, click OK. |

###### 2.1.2.4.6 CPN network monitoring

###### 2.1.2.4.6.1 CPN host monitoring dashboard

You can use this feature to monitor the key metrics of remote direct memory access (RDMA) networks on the server side of the intelligent computing network. The metrics include bandwidth, packet loss rate, and traffic control.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
3. In the left-side navigation pane, choose **Basic Network > CPN Management > CPN**
**Network Monitoring > CPN Host Monitoring**.
4. In the upper-right corner of the CPN host monitoring dashboard page, click **Variable**
**Filtering**. In the Variable Filtering dialog box, configure the **Custer** and **Host** parameters,
and click **OK**.
5. On the **CPN host monitoring dashboard** page, view information about the following
metrics: **Network Overview**, **End-side congestion packet loss**, **Network card RDMA**
**packet loss**, **Network card RDMA communication QP quantity & network card**
**status**, **Network congestion metrics**, **Network physical throughput**, and **Nic queue**
**throughput**.You can also click the
icon to the left of each metric to view details.

###### 2.1.2.4.6.2 CPN switch dashboard

You can use this feature to monitor the running status metrics of vSwitches. The metrics include bandwidth, packet loss, and traffic control.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
3. In the left-side navigation pane, choose **Basic Network > CPN Management > CPN**
**Network Monitoring > CPN Switcher**.
4. In the upper-right corner of the CPN switch dashboard page, click **Variable Filtering**. In
the Variable Filtering dialog box, configure the **idc** and **host** parameters, and click **OK**.
5. On the CPN switch dashboard page, view information about the following metrics: **Network**
**Overview**, **Ruijie exception indicator top 50**, **Top 50 abnormal indicators**, **Queue**
**metrics**, **Port metrics**, **Alarm status**, and **Logs**. You can also click the
icon to the left of each metric to view details.

###### 2.1.2.4.6.3 NAK packet analysis tool

You can use this tool to collect NAK packets in real time. After the packets are aggregated and analyzed, a matrix diagram is generated to help you quickly identify abnormal nodes.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
3. In the left-side navigation pane, choose **Basic Network > CPN Management > CPN**
**Network Monitoring > NAK Message Analysis Tool**.
4. In the upper-right corner of the NAK message Analysis Tool page, click **Variable Filtering**.
In the Variable Filtering dialog box, configure the **Network cluster**, **SOURCE device**
**Group**, and **Destination device Group** parameters, and click **OK**.
5. On the **NAK message Analysis Tool** page, view information about the following metrics:
**Network cluster-level NAK dashboard** and **Device Group-level NAK dashboard.** You
can also click the icon to the left of each metric to view details.

##### 2.1.2.5 CGW

You can connect bare metal instances to a virtual private cloud (VPC) by using Central Gateway (CGW) to manage the bare metal instances in a centralized manner. CGW instances are dedicated hybrid switches (HSWs). The system supports operations such as instance management, operation log viewing, network management of bare metal instances, and O&M configurations to help you complete the daily O&M operations of CGW.

> **Note:** By default, the CGW feature is not displayed. To use the feature, click **User Authorities** in the top navigation bar of the Apsara Uni-manager Operations Console. In the left-side navigation pane of the page that appears, click **Menu Management**. On the Menu management page, find Cloud Gateways and click Modify in the Actions column. In the Edit menu items panel, turn on **Show or not**.

**Instance management**

On the Instance Management page, you can manage the added CGW instances in a centralized manner and view the summary information about the CGW instances in the system.

**Display devices**

1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
3. In the left-side navigation pane, choose **Basic Network** > **Cloud Gateways**.
4. On the Cloud Gateway page, click the **Instance Management** tab. On the **Display**
**Devices** tab, view the instance details.

| Parameter | Description |
|---|---|
| Cloud Gateway Name | The name of the CGW instance. |

| IBGP Role | The role of the CGW instance in the environment. Client: specifies that the CGW instance acts as a client of an Internal Border Gateway Protocol (iBGP) neighbor and provides server access. Deploy Client and RR on a Device: specifies that the CGW instance acts as a route reflector (RR) of an iBGP neighbor and provides server access. Deploy RR on a Device: specifies that the CGW instance acts as an RR of an iBGP neighbor and does not provide server access. |
|---|---|
| Manage IP Address | The IP address of the CGW instance. |
| Management status | The initialization state of the CGW instance. Valid values: Uninitialized Initializing Initialized |
| Authorization Status | The authorization state of the CGW instance. Valid values: Unauthorized Authorized Note To use CGW instances, you must plan the number of CGW licenses in Deployment Planner. If the number of CGW licenses in Deployment Planner is less than that of used CGW instances, the CGW instances without license authorization are in the Unauthorized state. In this case, you need to increase the number of CGW licenses. |
| Created At | The time when the CGW instance was created. |

**Scan new devices**

1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
3. In the left-side navigation pane, choose **Basic Network** > **Cloud Gateways**.
4. On the Cloud Gateway page, click the **Instance Management** tab. Then, click the **Scan**
**for New Devices** tab.
5. On the Scan for New Devices tab, find the device that you want to manage and click
**Manage** in the **Actions** column.
Alternatively, select multiple devices that you want to manage and click **Batch Manage**.
6. In the Manage dialog box, find the device and configure the **IBGP Role** parameter.
The IBGP Role parameter specifies the role of a CGW instance in the environment. Valid values of the IBGP Role parameter:
**Client**: specifies that the CGW instance acts as a client of an iBGP neighbor and provides
server access.
**Deploy Client and RR on a Device** : specifies that the CGW instance acts as an RR of an
iBGP neighbor and provides server access.
**Deploy RR on a Device**: specifies that the CGW instance acts as an RR of an iBGP
neighbor and does not provide server access.

> **Important:** The iBGP role configurations must meet the following networking requirements:
> Single-data center deployment: At least one group of CGW instances whose iBGP role is an RR and other devices whose iBGP role is a client are deployed in a single data center.
> Multi-data center deployment: One group of CGW instances whose iBGP role is an RR and other devices whose iBGP role is a client are deployed in at least two data centers.
> RR role recommendations:
> We recommend that you set the role to Deploy Client and RR on a Device.
> If you have higher network stability requirements, we recommend that you set the role to Deploy RR on a Device.

7. Click **OK**.

**Operation logs**

You can view records and results of CGW API operations that are called by the bare metal controller or Apsara Uni-manager Operations Console based on your O&M requirements.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
3. In the left-side navigation pane, choose **Basic Network** > **Cloud Gateways**.
4. On the Cloud Gateway page, click the **Operation Logs** tab.
5. Optional. Select **Start/End Time** and configure the start time and end time.
6. View the operation logs.

| Parameter | Description |
|---|---|
| ID | The ID of the API operation log. |
| Bare Metal Name | The name of the bare metal instance that was applied for or released in the VPC. |
| Created At | The time when the API operation was performed. |

| API Operation | The category of the API operation. Valid values: add: specifies that a bare metal instance is applied for in the VPC. del: specifies that a bare metal instance is released in the VPC. del pc: specifies that an Express Connect circuit is deleted. _ del vbr: specifies that a virtual border router (VBR) is deleted. _ del router intf: specifies that a router interface is deleted. _ _ del route entry: specifies that a route entry is deleted. _ _ |
|---|---|
| Vswitch ID | The ID of the dedicated vSwitch when the bare metal instance is applied for or released in the VPC. |
| Cloud Gateway Name | The name of the CGW instance involved with the API operation. |
| Port | The port to which the bare metal instance is connected. |
| Status | The status of the API operation. success: The API operation was successful. If the API operation is in progress, the value indicates the real-time status of the API operation. If the API operation is complete but the value is nots uccess, you can view the failure information in this column. Example: create vpc connection fail. |

7. Find the operation log that you want to view and click **Details** in the **Actions** column to
view the details, including the region ID, initiator, and HTTP status code.

**Network management of bare metal instances**

**Create a bare metal instance and connect it to a VPC**

Create a bare metal instance and connect it to a VPC based on your O&M requirements. After the bare metal instance is connected to the VPC, the bare metal instance can communicate with other resources in the VPC over a private network.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
3. In the left-side navigation pane, choose **Basic Network** > **Cloud Gateways**.
4. On the Cloud Gateway page, click the **Bare Metal Network Management** tab.
5. On the Bare Metal Network Management tab, click **Create Bare Metal Instance**. In the
Create Bare Metal Instance dialog box, configure the **Bare Metal Name**, **SN**, and
**Description** parameters and click **OK**.
6. Find the bare metal instance that you created and click **Connect to VPC** in the **Actions**
column. In the Connect to VPC dialog box, configure the parameters that are described in the following table and click **OK**.

| Parameter | Description |
|---|---|
| Bare Metal Name | The name of the bare metal instance. You do not need to configure this parameter. |

| Bare Metal SN | The serial number of the bare metal instance. You do not need to configure this parameter. |
|---|---|
| AK | The AccessKey ID and AccessKey secret of the organization, which can be obtained from the Organizations page of the Apsara Uni-manager Management Console based on the organization to which the VPC belongs. For more information, see Manage the AccessKey pairs of an organization in Apsara Uni-manager Management Console User Guide. |
| SK |   |
| Vswitch ID | The ID of the dedicated vSwitch to which the bare metal instance is connected. |
| Region ID | The ID of the region in which the environment resides. |
| Cloud Gateway Name | The name of the CGW instance to which the bare metal instance is connected. |
| Port | The port of the CGW instance to which the bare metal instance is connected. |
| Bare Metal Description | The description of the bare metal instance. |

**View the network information about a bare metal instance in a**

**VPC**

1. On the **Bare Metal Network Management** tab, click **Advanced Filter** and filter bare
metal instances by specifying the following conditions: **Start and End Time**, **Bare Metal**
**Name**, **VPC ID**, **Vswitch ID**, **VBR ID**, **BD ID**, and **Cloud Gateway Name**.
2. View the network information about the bare metal instance that meets the filter
conditions.

| Parameter | Description |
|---|---|
| Bare Metal Name | The name of the bare metal instance. |
| SN | The serial number of the bare metal instance. |
| VPC ID | The ID of the VPC to which the bare metal instance belongs. |
| Vswitch ID | The ID of the dedicated vSwitch to which the bare metal instance is connected. |
| Cloud Gateway Name | The name of the CGW instance to which the bare metal instance is connected. |

| Port | The port of the CGW instance to which the bare metal instance is connected. |
|---|---|
| VBR ID | The VBR ID of the Express Connect circuit created on the HSW by the VPC to which the bare metal instance belongs. |
| BD ID | The value of the hardware bridge-domain (BD) to which the bare metal instance is added. |
| Created At | The time when the bare metal network was created. |
| Bare Metal IP Address | The IP address of the bare metal instance. Click Manage in the Bare Metal IP Address column to assign an IP address to the bare metal instance. This helps you configure the network of bare metal instances. For more information, see the Manage the IP address of a bare metal instance section of this topic. |

3. Find the bare metal instance and click **Details** in the **Actions** column to view the details of
the bare metal instance, such as the ID of the Express Connect circuit, VPC router interface, and VBR interface.

**Disconnect a bare metal instance from a VPC**

After a bare metal instance is disconnected from a VPC, access isolation of resources can be implemented. Find the bare metal instance and click **Close the Connection to VPC** or **Delete Instance** in the Actions column. Click **Close the Connection to VPC** in the **Actions** column to disconnect the bare metal instance from the VPC.

> **Note:** The Close the Connection to VPC option appears only after the bare metal instance is connected to a VPC.

Click **Delete Instance** in the Actions column to disconnect the bare metal instance from the VPC and delete the bare metal instance.

> **Note:** The Delete Instance option appears only for bare metal instances created on the Bare Metal Network Management page.

**Manage the IP address of a bare metal instance**

> In the Bare Metal IP Address Management panel, you can assign an IP address to a bare metal instance. This helps you configure the network of bare metal instances.

**Background information**

CGW works with Bare-metal Management Service (BMS). BMS is used to install bare metal instances, assign IP addresses, and complete network configurations. CGW is used to connect bare metal instances to VPCs. In some scenarios, you may not install bare metal instances or complete network configurations by using BMS, but you must use CGW to connect bare metal instances to VPCs. In such scenarios, the system cannot assign IP addresses to bare metal instances, and you must manually maintain IP address assignment results. This may cause IP address conflicts and poor usability. Therefore, network management of bare metal instances is supported on the Cloud Gateway page. You can manage IP addresses of bare metal instances in the Bare Metal IP Address Management panel.

**Prerequisites**

A bare metal instance is connected to a VPC.
1. Find the bare metal instance and click **Manage** in the **Bare Metal IP Address** column.
2. In the **Bare Metal IP Address Management** panel, click **Apply for Bare Metal IP**
**Address**.
3. In the **Apply for Bare Metal IP Address** dialog box, configure the **Bare Metal NIC**, **IP**,
and **IP Address Description** parameters and click **OK**.

> **Note:** If you do not specify the IP parameter, an IP address is automatically generated.

4. After you apply for an IP address for a bare metal instance, view the IP address in the **Bare**
**Metal IP Address Management** panel.
Find the IP address of the bare metal instance and click **Edit** to change the IP address. Find the IP address of the bare metal instance and click **Release** to release the IP address.

**O&M configurations**

**Apply for a bare metal instance in a VPC**

In O&M emergency scenarios, you can use this feature to add the physical port of the CGW instance associated with a bare metal instance to the VPC.

> **Warning:** This operation is only for emergency scenarios and must be performed under the guidance of R&D engineers. Otherwise, normal business operations may be affected.
> This feature can only be used to connect the bare metal instance to the CGW instance port but cannot be used to perform operations on the bare metal instance. To configure the network port, IP address, and routing information of the bare metal instance, contact the corresponding product team for guidance.
> Typically, you cannot use this feature to apply for a bare metal instance in the VPC. You can use the bare metal controller to call an API operation to enable the bare metal network.

1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
3. In the left-side navigation pane, choose **Basic Network** > **Cloud Gateways**.
4. On the Cloud Gateway page, click the **O&M Settings** tab.
5. Select **Apply for Bare Metal in VPC** from the drop-down list in the upper-left corner of the
tab.
6. Configure the parameters that are described in the following table.

| Parameter | Description |
|---|---|
| Region ID | The ID of the region in which the environment resides. |
| Cloud Gateway Name | The name of the CGW instance to which the bare metal instance is connected. |
| Vswitch ID | The ID of the vSwitch to which the bare metal instance is to be added. You can obtain the vSwitch ID from the VPC console of the Apsara Uni-manager Management Console. |
| Port | The port of the CGW instance to which the bare metal instance is connected. |
| AK | The AccessKey ID and AccessKey secret of the organization, which can be obtained from the Organizations page of the Apsara Uni-manager Management Console based on the organization to which the VPC belongs. For more information, see Manage the AccessKey pairs of an organization in Apsara Uni-manager Management Console User Guide. |
| SK |   |
| Bare Metal Name | The name of the bare metal instance that you want to apply for. The name must be unique. |

> **Note:** If the specified values are invalid, click **Re-enter** in the lower part of the tab and configure the parameters again.

7. Click **Next**.
8. Check the information. If the information is correct, click **Confirm**.
After the configurations are delivered, the **Result: Successful** message appears, and you can search for the bare metal instance by bare metal instance name on the **Bare Metal**
**Network Management** tab. If the bare metal instance is displayed, it is connected to the
VPC.

**Release a bare metal instance in a VPC**

In O&M emergency scenarios, you can use this feature to disconnect the physical port of the CGW instance associated with a bare metal instance from the VPC.

> **Warning:** This operation is only for emergency scenarios and must be performed under the guidance of R&D engineers. Otherwise, normal business operations may be affected.
> This feature can only be used to connect the bare metal instance to the CGW instance port but cannot be used to perform operations on the bare metal instance. To configure the network port, IP address, and routing information of the bare metal instance, contact the corresponding product team for guidance.
> Typically, you cannot use this feature to release a bare metal instance in the VPC. You can use the bare metal controller to call an API operation to delete the bare metal network.

1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
3. In the left-side navigation pane, choose **Basic Network** > **Cloud Gateways**.
4. On the Cloud Gateway page, click the **O&M Settings** tab.
5. Select **Release Bare Metal in VPC** from the drop-down list in the upper-left corner of the
tab.
6. Configure the parameters that are described in the following table.

| Parameter | Description |
|---|---|
| Region ID | The ID of the region in which the environment resides. |

| Bare Metal Name | The name of the bare metal instance that you want to release. You can obtain the name of the bare metal instance on theB are Metal Network Management tab. |
|---|---|

> **Note:** If the specified values are invalid, click **Re-enter** in the lower part of the tab and configure the parameters again.

7. Click **Next**.
8. Check the information. If the information is correct, click **Confirm**.
After the configurations are delivered, the **Result: Successful** message appears, and you can search for the bare metal instance by bare metal instance name on the **Bare Metal**
**Network Management** tab. If the bare metal instance is not displayed, it is released in
the VPC.

**Delete a route entry**

In O&M emergency scenarios, you can use this feature to delete route entries that point to the bare metal subnet in the VPC and the default route entries of a VBR.

> **Warning:** This operation is only for emergency scenarios and must be performed under the guidance of R&D engineers. Otherwise, normal business operations may be affected.
> Typically, you cannot use this feature to delete a VPC route entry. This operation is only for emergency scenarios.
> You can perform this operation to delete only one route entry at a time. To delete multiple route entries, you must perform this operation multiple times.

1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
3. In the left-side navigation pane, choose **Basic Network** > **Cloud Gateways**.
4. On the Cloud Gateway page, click the **O&M Settings** tab.
5. Select **Delete Route Table Entry** from the drop-down list in the upper-left corner of the
tab.
6. Configure the parameters that are described in the following table.

| Parameter | Description about deleting a VPC route entry | Description about deleting a VBR route entry |
|---|---|---|
| Region ID | The ID of the region in which the environment resides. | The ID of the region in which the environment resides. |
| Route Table ID | The ID of the VPC route table, which can be obtained from the VPC console. For more information about how to obtain the ID of a VPC route table, see VPC User Guide. | The ID of the VBR route table. If the bare metal instance involved with the VBR is connected to a VPC, you can search for the bare metal instance by bare metal instance name on the Bare Metal Network Management tab, and then click Details in the Actions column. The value of the VBR Route Table ID parameter in the details is the value of this parameter. If the bare metal instance involved with the VBR fails to be connected to a VPC, specify the name and creation time of the bare metal instance to search for the operation logs and find an operation log whose API Operation is add on the Operation Logs tab. Click Details in the Actions column. The value of the VBR Route Table ID parameter in the details is the value of this parameter. |

| Router Interface ID | The ID of the VPC router interface, which can be obtained from the VPC console. For more information about how to obtain the ID of a VPC router interface, see VPC User Guide. | The ID of the VBR interface. If the bare metal instance involved with the VBR is connected to a VPC, you can search for the bare metal instance by bare metal instance name on the Bare Metal Network Management tab, and then click Details in the Actions column. The value of the VBR Router Interface parameter in the details is the value of this parameter. If the bare metal instance involved with the VBR fails to be connected to a VPC, specify the name and creation time of the bare metal instance to search for the operation logs and find an operation log whose API Operation is add on the Operation Logs tab. Click Details in the Actions column. The value of the VBR Router Interface parameter in the details is the value of this parameter. |
|---|---|---|
| Routing Destinatio n CIDR | The destination CIDR block to which the VPC points, which can be obtained from the VPC console. For more information about how to obtain a destination CIDR block, see VPC User Guide. | Set the value to 0.0.0.0/0. |
| AK | The AccessKey ID and AccessKey secret of the organization, which can be obtained from the Organizations page of the Apsara Uni-manager Management Console based on the organization to which the VPC belongs. For more information, see Manage the AccessKey pairs of an organization in Apsara Uni-manager Management Console User Guide. | The AccessKey ID and AccessKey secret of the organization, which can be obtained from the Organizations page of the Apsara Uni-manager Management Console based on the organization to which the VBR belongs. For more information, see Manage the AccessKey pairs of an organization in Apsara Uni-manager Management Console User Guide. |
| SK |   |   |

> **Note:** If the specified values are invalid, click **Re-enter** in the lower part of the tab and configure the parameters again.

7. Click **Next**.
8. Check the information. If the information is correct, click **Confirm**.
The system begins to deliver the configurations. After the configurations are delivered, the
**Result: Successful** message appears.
9. Optional. In actual fault scenarios, if multiple route entries exist in the route table, repeat
Step 5 to Step 8 to delete other route entries.

**Delete a router interface**

In O&M emergency scenarios, you can use this feature to delete a VPC router interface and a VBR interface.

> **Warning:** This operation is only for emergency scenarios and must be performed under the guidance of R&D engineers. Otherwise, normal business operations may be affected.

1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
3. In the left-side navigation pane, choose **Basic Network** > **Cloud Gateways**.
4. On the Cloud Gateway page, click the **O&M Settings** tab.
5. Select **Delete Router Interface** from the drop-down list in the upper-left corner of the tab.
6. Configure the parameters that are described in the following table.

| Parameter | Description about deleting a VPC router interface | Description about deleting a VBR interface |
|---|---|---|
| Region ID | The ID of the region in which the environment resides. | The ID of the region in which the environment resides. |

| Router Interface ID | The ID of the VPC router interface. On the Operation Logs tab, specify the name and creation time of the bare metal instance to search for the operation logs and find an operation log whose API Operation is add. Click Details in the Actions column. The value of the VPC Router Interface parameter in the details is the value of this parameter. | The ID of the VBR interface. If the bare metal instance involved with the VBR is connected to a VPC, you can search for the bare metal instance by bare metal instance name on the Bare Metal Network Management tab, and then click Details in the Actions column. The value of the VBR Router Interface parameter in the details is the value of this parameter. If the bare metal instance involved with the VBR fails to be connected to a VPC, specify the name and creation time of the bare metal instance to search for the operation logs and find an operation log whose API Operation is add on the Operation Logs tab. Click Details in the Actions column. The value of the VBR Router Interface parameter in the details is the value of this parameter. |
|---|---|---|
| AK | The AccessKey ID and AccessKey secret of the organization, which can be obtained from the Organizations page of the Apsara Uni-manager Management Console based on the organization to which the VPC belongs. For more information, see Manage the AccessKey pairs of an organization in Apsara Uni- manager Management Console User Guide. | The AccessKey ID and AccessKey secret of the organization, which can be obtained from the Organizations page of the Apsara Uni-manager Management Console based on the organization to which the VBR belongs. For more information, see Manage the AccessKey pairs of an organization in Apsara Uni-manager Management Console User Guide. |
| SK |   |   |

> **Note:** If the specified values are invalid, click **Re-enter** in the lower part of the tab and configure the parameters again.

7. Click **Next**.
8. Check the information. If the information is correct, click **Confirm**.
The system begins to deliver the configurations. After the configurations are delivered, the
**Result: Successful** message appears.
After the configurations are delivered, you can choose **Product Operation** > **Networking**
> **Network Intelligence** in the navigation bar of the Apsara Uni-manager Operations

Console. On the homepage of Apsara Network Intelligence, enter the ID of the router interface to search for the router interface. If no search result appears, the router interface is deleted.

**Delete a VBR**

In O&M emergency scenarios, you can use this feature to delete a VBR.

> **Warning:** This operation is only for emergency scenarios and must be performed under the guidance of R&D engineers. Otherwise, normal business operations may be affected.

1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
3. In the left-side navigation pane, choose **Basic Network** > **Cloud Gateways**.
4. On the Cloud Gateway page, click the **O&M Settings** tab.
5. Select **Delete VBR** from the drop-down list in the upper-left corner of the tab.
6. Configure the parameters that are described in the following table.

| Parameter | Description |
|---|---|
| Region ID | The ID of the region in which the environment resides. |
| VBR ID | The ID of the VBR that you want to delete. On theO peration Logs tab, specify the name and creation time of the bare metal instance to search for the operation logs and find an operation log whose API Operation is add. Click Details in the Actions column. The value of the VBR ID parameter in the details is the value of this parameter. |
| AK | The AccessKey ID and AccessKey secret of the organization, which can be obtained from the Organizations page of the Apsara Uni-manager Management Console based on the organization to which the VBR belongs. For more information, see Manage the AccessKey pairs of an organization in Apsara Uni-manager Management Console User Guide. |
| SK |   |

> **Note:** If the specified values are invalid, click **Re-enter** in the lower part of the tab and configure the parameters again.

7. Click **Next**.
8. Check the information. If the information is correct, click **Confirm**.
The system begins to deliver the configurations. After the configurations are delivered, the
**Result: Successful** message appears.
After the configurations are delivered, you can choose **Product Operation** > **Networking**
> **Network Intelligence** in the navigation bar of the Apsara Uni-manager Operations

Console. On the homepage of Apsara Network Intelligence, enter the ID of the VBR to search for the VBR. If no search result appears, the VBR is deleted.

**Delete an Express Connect circuit**

In O&M emergency scenarios, you can use this feature to delete an Express Connect circuit.

> **Warning:** This operation is only for emergency scenarios and must be performed under the guidance of R&D engineers. Otherwise, normal business operations may be affected.

1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
3. In the left-side navigation pane, choose **Basic Network** > **Cloud Gateways**.
4. On the Cloud Gateway page, click the **O&M Settings** tab.
5. Select **Delete Express Connect Circuit** from the drop-down list in the upper-left corner of
the tab.
6. Configure the parameters that are described in the following table.

| Parameter | Description |
|---|---|
| Region ID | The ID of the region in which the environment resides. |
| Express Connect Circuit ID | The ID of the Express Connect circuit that you want to delete. On the Operation Logs tab, specify the name and creation time of the bare metal instance to search for the operation logs and find an operation log whose API Operation is add. Click Details in the Actions column. The value of the Express Connect Circuit ID parameter in the details is the value of this parameter. |

| AK | The AccessKey ID and AccessKey secret of the organization, which can be obtained from the Organizations page of the Apsara Uni-manager Management Console based on the organization to which the VBR belongs. For more information, see Manage the AccessKey pairs of an organization in Apsara Uni-manager Management Console User Guide. |
|---|---|
| SK |   |

> **Note:** If the specified values are invalid, click **Re-enter** in the lower part of the tab and configure the parameters again.

7. Click **Next**.
8. Check the information. If the information is correct, click **Confirm**.
The system begins to deliver the configurations. After the configurations are delivered, the
**Result: Successful** message appears.
After the configurations are delivered, you can choose **Product Operation** > **Networking**
> **Network Intelligence** in the navigation bar of the Apsara Uni-manager Operations

Console. On the homepage of Apsara Network Intelligence, enter the ID of the Express Connect circuit to search for the Express Connect circuit. If no search result appears, the Express Connect circuit is deleted.

**Delete all resources**

In O&M emergency scenarios, you can use this feature to delete all resources, including VPC route entries, VBR route entries, VPC router interfaces, VBR interfaces, VBRs, and Express Connect circuits.

> **Warning:** This operation is only for emergency scenarios and must be performed under the guidance of R&D engineers. Otherwise, normal business operations may be affected.

1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
3. In the left-side navigation pane, choose **Basic Network** > **Cloud Gateways**.
4. On the Cloud Gateway page, click the **O&M Settings** tab.
5. Select **Delete ALL Resources** from the drop-down list in the upper-left corner of the tab.
6. Configure the parameters that are described in the following table.

| Parameter | Description |
|---|---|
| Region ID | The ID of the region in which the environment resides. |
| Cloud Gateway Name | The name of the CGW instance to which the bare metal instance is connected. |
| AK | The AccessKey ID and AccessKey secret of the organization, which can be obtained from the Organizations page of the Apsara Uni-manager Management Console based on the organization to which the VBR belongs. For more information, see Manage the AccessKey pairs of an organization in Apsara Uni-manager Management Console User Guide. |
| SK |   |
| VPC Router Interface ID | The ID of the VPC router interface, which can be obtained from the VPC console. For more information about how to obtain the ID of a VPC router interface, see VPC User Guide. |
| VPC Route Table ID | The ID of the VPC route table, which can be obtained from the VPC console. For more information about how to obtain the ID of a VPC route table, see VPC User Guide. |
| VBR Route Table ID | The ID of the VBR route table. If the bare metal instance involved with the VBR is connected to a VPC, you can search for the bare metal instance by bare metal instance name on the Bare Metal Network Management tab, and then click Details in the Actions column. The value of the VBR Route Table ID parameter in the details is the value of this parameter. If the bare metal instance involved with the VBR fails to be connected to a VPC, specify the name and creation time of the bare metal instance to search for the operation logs and find an operation log whose API Operation is add on the Operation Logs tab. Click Details in the Actions column. The value of the VBR Route Table ID parameter in the details is the value of this parameter. |

| VPC CIDR1 | The destination CIDR block 1 to which the VPC points, which can be obtained from the VPC console. For more information about how to obtain a destination CIDR block, see VPC User Guide. |
|---|---|
| VPC CIDR2 | The destination CIDR block 2 to which the VPC points, which can be obtained from the VPC console. For more information about how to obtain a destination CIDR block, see VPC User Guide. |
| VBR Router Interface ID | The ID of the VBR interface. If the bare metal instance involved with the VBR is connected to a VPC, you can search for the bare metal instance by bare metal instance name on the Bare Metal Network Management tab, and then click Details in the Actions column. The value of the VBR Router Interface parameter in the details is the value of this parameter. If the bare metal instance involved with the VBR fails to be connected to a VPC, specify the name and creation time of the bare metal instance to search for the operation logs and find an operation log whose API Operation is add on the Operation Logs tab. Click Details in the Actions column. The value of the VBR Router Interface in the details is the value of this parameter. |
| VBR ID | The ID of the VBR that you want to delete. On theO peration Logs tab, specify the name and creation time of the bare metal instance to search for the operation logs and find an operation log whose API Operation is add. Click Details in the Actions column. The value of the VBR ID parameter in the details is the value of this parameter. |
| Express Connect Circuit ID | The ID of the Express Connect circuit that you want to delete. On the Operation Logs tab, specify the name and creation time of the bare metal instance to search for the operation logs and find an operation log whose API Operation is add. Click Details in the Actions column. The value of the Express Connect Circuit ID parameter in the details is the value of this parameter. |
| Trunk ID | You do not need to specify this parameter. |

> **Note:** If the specified values are invalid, click **Re-enter** in the lower part of the tab and configure the parameters again.

7. Click **Next**.
8. Check the information. If the information is correct, click **Confirm**.
The system begins to deliver the configurations. After the configurations are delivered, the
**Result: Successful** message appears.

**View the bandwidth of an Express Connect circuit**

You can view the bandwidth of the Express Connect circuit to which a router interface corresponds based on your O&M requirements when a CGW instance is connected to a VPC in the system.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
3. In the left-side navigation pane, choose **Basic Network** > **Cloud Gateways**.
4. On the Cloud Gateway page, click the **O&M Settings** tab.
5. Select **View Express Connect Circuit Bandwidth** from the drop-down list in the upper-
left corner of the tab.
6. Configure the parameters that are described in the following table and click **Query**. The
system displays the bandwidth of the Express Connect circuit that meets the filter conditions.

| Parameter | Description |
|---|---|
| Region ID | The ID of the region in which the environment resides. |
| Router Interface ID | The ID of the VBR interface. On the Bare Metal Network Management tab, specify a VPC ID and CGW instance name. Click Details in the Actions column. The value of the VBR Router Interface parameter in the details is the value of this parameter. |
| AK | The AccessKey ID and AccessKey secret of the organization, which can be obtained from the Organizations page of the Apsara Uni-manager Management Console based on the organization to which the VBR belongs. For more information, see Manage the AccessKey pairs of an organization in Apsara Uni-manager Management Console User Guide. |
| SK |   |

7. View the table on the left and obtain the bandwidth in units of bit/s based on the
specifications. The bandwidth information describes the specifications of the Express Connect circuit bandwidth on the HSW of the current VPC.

| Specifications | Bandwidth (unit: bit/s) |
|---|---|
| Large.1 | 1G |
| Large.2 | 2G |

| Large.4 | 4G |
|---|---|
| Large.5 | 5G |
| Xlarge.1 | 10G |
| Xlarge.2 | 20G |
| Xlarge.4 | 40G |
| Xlarge.5 | 50G |
| Xlarge.8 | 80G |
| Xlarge.10 | 100G |
| Xlarge.16 | 160G |
| Xlarge.20 | 200G |
| Xlarge.50 | 500G |
| Xlarge.320 | 3200G |

**Change the bandwidth of an Express Connect circuit**

In O&M emergency scenarios, you can use this feature to change the bandwidth of an Express Connect circuit.

**Warning**

This operation may affect your business. Unauthorized operations are prohibited. Configuration changes must be performed under the guidance of technical support.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
3. In the left-side navigation pane, choose **Basic Network** > **Cloud Gateways**.
4. On the Cloud Gateway page, click the **O&M Settings** tab.
5. Select **Change Express Connect Circuit Bandwidth** from the drop-down list in the
upper-left corner of the tab.
6. Configure the parameters that are described in the following table and click **Next**.

| Parameter | Description |
|---|---|
| Region ID | The ID of the region in which the environment resides. |
| Router Interface ID | The ID of the VBR interface. On the Bare Metal Network Management tab, specify a VPC ID and CGW instance name. Click Details in the Actions column. The value of the VBR Router Interface parameter in the details is the value of this parameter. |
| Router Interface Specifications | The specifications of the Express Connect circuit bandwidth. |
| AK | The AccessKey ID and AccessKey secret of the organization, which can be obtained from the Organizations page of the Apsara Uni-manager Management Console based on the organization to which the VBR belongs. For more information, see Manage the AccessKey pairs of an organization in Apsara Uni-manager Management Console User Guide. |
| SK |   |

7. Check whether the parameter configurations are valid.
If yes, click **Confirm**. After the configurations are delivered, check whether the bandwidth of the Express Connect circuit is changed by referring to the View the bandwidth of an Express Connect circuit section of this topic. If not, click **Back to Modify** to configure the parameters again.

**View trunk usage**

You can view trunk usage to obtain up-to-date information about the usage of hardware ports in a timely manner.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
3. In the left-side navigation pane, choose **Basic Network** > **Cloud Gateways**.
4. On the Cloud Gateway page, click the **O&M Settings** tab.
5. Select **View Trunk Usage** from the drop-down list in the upper-left corner of the tab.
6. Specify a trunk ID and CGW instance name, select a trunk state, and then click **Search** to
view trunk usage. Valid values of the **Status** parameter are **Idle**, **Used**, **Creating**, and
**Deleting**.

> **Note:** Specify the last integer of the value of the **Port** parameter that is obtained from the **Bare Metal Network Management** tab as a trunk ID. For example, if the value of the Port parameter is 10GE1/0/40, specify 40 as a trunk ID.

**View VPN usage of a bare metal instance**

You can view the VPN usage of a bare metal instance, and the VPN is assigned to a CGW instance.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
3. In the left-side navigation pane, choose **Basic Network** > **Cloud Gateways**.
4. On the Cloud Gateway page, click the **O&M Settings** tab.
5. Select **View BM VPN Usage** from the drop-down list in the upper-left corner of the tab.
6. Specify the name of a CGW instance, a Virtual Extensible Local Area Network (VXLAN) ID,
and the VPN name of a bare metal instance, select a state, and then click **Search** to view the bare metal instance VPNs assigned to all the HSWs. Valid values of the **Status** parameter are **Succeeded** and **Creating**.

**View BD usage**

You can view BD usage to learn about the BD configuration distribution in a timely manner.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
3. In the left-side navigation pane, choose **Basic Network** > **Cloud Gateways**.
4. On the Cloud Gateway page, click the **O&M Settings** tab.
5. Select **View BD Usage** from the drop-down list in the upper-left corner of the tab.
6. Specify a CGW instance name, BD ID, and vSwitch ID, select a state, and then click **Search**
to view BD usage. Valid values of the **Status** parameter are **Succeeded**, **Creating**, and
**Deleting**.

**Check initialization configurations**

In O&M emergency scenarios, you can use this feature to check whether the initialization configurations of the HSW are successful.

> **Note:** This feature only checks the initialization status of the platform access gateway vSwitch and whether the initialization configurations are successful. No operation is performed on the bare metal instance.

1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
3. In the left-side navigation pane, choose **Basic Network** > **Cloud Gateways**.
4. On the Cloud Gateway page, click the **O&M Settings** tab.
5. Select **Check the Initialization Configuration** from the drop-down list in the upper-left
corner of the tab.
6. Configure the parameters that are described in the following table.

| Parameter | Description |
|---|---|
| Region ID | The ID of the region in which the environment resides. |
| HSW Name | The name of the vSwitch to be checked in instance management. |

> **Note:** If the specified values are invalid, click **Re-enter** in the lower part of the tab and configure the parameters again.

7. After you specify the parameters, click **Next** and click **Check** to check the initialization
configurations of the vSwitch.

**Check route configurations**

In O&M emergency scenarios, you can use this feature to locate abnormal operations and check whether the route configurations of a bare metal instance are valid.

**Background information**

You can use this operation to locate the exception and scan the HSW after a bare metal instance fails to be added. This feature only checks whether the route configurations of the bare metal instance are valid. No operation is performed on the bare metal instance.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
3. In the left-side navigation pane, choose **Basic Network** > **Cloud Gateways**.
4. On the Cloud Gateway page, click the **O&M Settings** tab.
5. Select **Check the Route Configuration** from the drop-down list in the upper-left corner of
the tab.
6. Configure the parameters that are described in the following table.

| Parameter | Description |
|---|---|
| Region ID | The ID of the region in which the environment resides. |
| Bare Metal Name | The name of the bare metal instance that was applied for or released in a VPC. It uniquely identifies the bare metal instance within a region. |
| AK | The AccessKey ID and AccessKey secret of the organization, which can be obtained from the Organizations page of the Apsara Uni-manager Management Console based on the organization to which the VBR belongs. For more information, see Manage the AccessKey pairs of an organization in Apsara Uni-manager Management Console User Guide. |
| SK |   |

> **Note:** If the specified values are invalid, click **Re-enter** in the lower part of the tab and configure the parameters again.

7. After you specify the parameters, click **Next** and click **Check** to check the route
configurations.

**Display the information about a bare metal network gateway**

In O&M emergency scenarios, you can use this feature to check the gateway of a vSwitch.

**Background information**

This operation is only for emergency scenarios in which the bare metal network is inaccessible. This operation is used to check the vSwitch gateway information and has no impact on the bare metal instance.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
3. In the left-side navigation pane, choose **Basic Network** > **Cloud Gateways**.
4. On the Cloud Gateway page, click the **O&M Settings** tab.
5. Select **Display the Information of Bare Metal Network Gateways** from the drop-down
list in the upper-left corner of the tab.
6. Configure the parameters that are described in the following table.

| Parameter | Description |
|---|---|
| Region ID | The ID of the region in which the environment resides. |
| Vswitch ID | The ID of the vSwitch. You can obtain the vSwitch ID from the VPC console. |
| AK | The AccessKey ID and AccessKey secret of the organization, which can be obtained from the Organizations page of the Apsara Uni-manager Management Console based on the organization to which the VPC belongs. For more information, see Manage the AccessKey pairs of an organization in Apsara Uni-manager Management Console User Guide. |
| SK |   |

> **Note:** If the specified values are invalid, click **Re-enter** in the lower part of the tab and configure the parameters again.

7. After you configure the parameters, click **Next** and click **Check** to check the information
about the bare metal network gateway.

##### 2.1.2.6 Leased line management

###### 2.1.2.6.1 Leased lines

The Apsara Uni-manager Operations Console allows you to manage virtual private cloud (VPC), Data Center Interconnect (DCI), and interconnection leased lines. You can also view the monitoring data of the leased lines.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
3. In the left-side navigation pane, choose **Basic Network** > **Leased Line Management** >
**Leased Line Dashboard**.
4. In the upper part of the Leased Line Instances page, view the number of alerting instances,
number of normal instances, and percentage of normal instances by **VPC Private Link**,
**DCI Express Connect Circuit**, and **Leased Line**.
5. Click **VPC Private Link** to view the corresponding information.
On the **Hosted Connection** tab, view the access point overview and the list of VPC leased lines. In the **Express Connect Circuits** section, filter VPC leased lines by **Access Device**
**Name**, **Access Point ID**, **Data Center of Access Device**, **Service State**, **RegionID**,
or their combinations. You can also click **Details** in the **Actions** column of a leased line to view its details. On the **Monitoring & Alerting** tab, view the monitoring and alerting information of the leased lines. Click **Details** in the **Alert Details** column of an alert to view its details.
6. Click **DCI Express Connect Circuit** to view the corresponding information.
On the **Hosted Connection** tab, view the DCI interconnection topology and the list of DCI leased lines. You can also perform the following operations: Create a DCI leased line: Click **Create DCI Express Connect Circuit**. In the dialog box that appears, configure the following parameters and click **OK**.

| Section | Parameter | Description |
|---|---|---|
| Local Basic Settings | Express Connect Circuit Name | The name of the leased line. |
|   | Express Connect Circuit Type | The type of the leased line. Valid values: InterDomain IntraDomain |
|   | Region | The region ID of the source access point of the leased line. |
|   | Idc | The data center to which the source access point of the leased line belongs. |
|   | Carrier | The Internet service provider (ISP) that provides the leased line service. |
|   | Access Device | The source access point of the leased line. |
|   | Port | The port of the source access point. |
|   | Port Type | The port type of the source access point. |
|   | Express Connect Circuit Bandwidth | The bandwidth of the leased line. Unit: MB. |
|   | Direct Connection Status | The direct connection status of the leased line. Valid values: Firewall Direct-Connect |

| Direct |   |   |
|---|---|---|
|   | Firewall Type | The type of the firewall. This parameter takes effect only if you set the Direct Connection Status parameter to Firewall. Valid values: Cloud Firewall User Firewall Other |
| Connection Attributes and Firewall Information |   |   |
|   | Firewall Name | The name of the firewall device. This parameter takes effect only if you set the Direct Connection Status parameter to Firewall. |
|   | Firewall Remarks | The description of the firewall device. This parameter takes effect only if you set the Direct Connection Status parameter to Firewall. |
| Peer Basic Settings | Peer Region | The region ID of the destination access point of the leased line. |
|   | PeerIdc | The data center to which the destination access point of the leased line belongs. |
|   | Peer Device | The destination access point of the leased line. |
|   | Peer Port | The port of the destination access point. |
|   | Peer Port Type | The port type of the destination access point. |
| Other Settings | Local IP Address | The CIDR block of the source access point. Set the value in the IP address/mask format. |
|   | Peer IP Address | The CIDR block of the destination access point. Set the value in the IP address/mask format. |
|   | Status | Specifies whether to enable the leased line immediately after it is created. |
|   | Associate Express Connect Circuit Group | The group to which the leased line belongs. If no group is available, you can click Create Express Connect Circuit Group to create one. For more information, see Leased line groups. |
|   | Remarks | The description of the leased line. |

View the leased line information: Click **Advanced Filter** and filter DCI leased lines by
**Instance Name**, **Express Connect Circuit Type**, **Access Region**, **Peer Region**,
**Interconnection Type on both Sides of the Express Connect Circuit** , **Express**
**Connect Circuit Status**, or their combinations. You can also click **Details** in the
**Actions** column of a leased line to view its details.
Modify a DCI leased line: Find the leased line that you want to modify and click **Modify** in the **Actions** column. In the dialog box that appears, modify parameters based on your business requirements and click **OK**. Delete a DCI leased line: Find the leased line that you want to delete, move the pointer over the icon in the **Actions** column, and then select **Delete**. In the message that appears, click **Delete**.

> **Note:** After you delete a leased line, it cannot be recovered. Proceed with caution.

Perform quick diagnostics: Find the leased line that you want to manage, move the pointer over the icon in the **Actions** column, and then select **Quick Diagnostics**. The **Network instance diagnosis results** page appears. For more information, see Network instance diagnosis. On the **Monitoring & Alerting** tab, view the monitoring and alerting information of the leased lines. Click **Details** in the **Alert Details** column of a leased line to view its details.
7. Click **Leased Line** to view the corresponding information.
On the **Hosted Connection** tab, view the interconnection leased line topology and the list of interconnection leased lines. You can also perform the following operations: Create an interconnection leased line: Click **Create Leased Line**. In the dialog box that appears, configure parameters and click **OK**. For more information about parameters, refer to the step for creating a DCI leased line described in this topic. View the leased line information: Click **Advanced Filter** and filter interconnection leased lines by **Instance Name**, **Express Connect Circuit Type**, **Access Region**,
**Peer Region**, **Interconnection Type on both Sides of the Express Connect**
**Circuit**, **Express Connect Circuit Status**, or their combinations. You can also click
**Details** in the **Actions** column of a leased line to view its details.
Modify an interconnection leased line: Find the leased line that you want to modify and click **Modify** in the **Actions** column. In the dialog box that appears, modify parameters based on your business requirements and click **OK**. Delete an interconnection leased line: Find the leased line that you want to delete, move the pointer over the icon in the **Actions** column, and then select **Delete**. In the message that appears, click **Delete**.

> **Note:** After you delete a leased line, it cannot be recovered. Proceed with caution.

Perform quick diagnostics: Find the leased line that you want to manage, move the pointer over the icon in the **Actions** column, and then select **Quick Diagnostics**. The **Network instance diagnosis results** page appears. For more information, see Network instance diagnosis. On the **Monitoring & Alerting** tab, view the monitoring and alerting information of the leased lines. Click **Details** in the **Alert Details** column of an alert to view its details.

###### 2.1.2.6.2 Leased line group

Leased line management allows you to manage groups of data center interconnection (DCI) leased lines and interconnection leased lines.

**Create a leased line group**

1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
3. In the left-side navigation pane, choose **Basic Network** > **Leased Line Management** >
**Leased Line Groups**.
4. On the Leased Line Group Management page, click **Create Express Connect Circuit**
**Group**. In the Create Express Connect Circuit Group dialog box, configure the parameters
that are described in the following table and click **OK**.

| Parameter | Description |
|---|---|
| Special Group Name | The name of the leased line group. |
| Express Connect Circuit Group Type | The type of the leased line group. Valid values: DCInterConnection: DCI leased line ExternalConnection: interconnection leased line |
| Region | The ID of the source region of the leased line group. |
| Idc | The name of the source data center of the leased line group. |
| PeerRegion | The ID of the destination region of the leased line group. |
| PeerIdc | The name of the destination data center of the leased line group. |
| Remarks | The remarks of the leased line group. |

**View the details of a leased line group**

1. On the Leased Line Group Management page, click **Advanced Filter** and search for a
leased line group by **Group Name**, **Group Type**, **Source Region ID**, **Source IDC**, **Peer**
**Region ID**, **Peer IDC**, and **Remarks**.
2. Find the leased line group that you want to view and click **Details** in the **Operation**
column to view the information in the **Group Details** and **Associate Hosted Connection** sections.
3. In the **Associate Hosted Connection** section, perform the following operations:
Associate the leased line group with a leased line: Click **Associate Instance**. In the Associate Instance dialog box, configure the following parameters click **OK**. View the details of the associated leased line: Find the associated leased line and click
**Details** in the **Operation** column.
Disassociate the leased line group from the leased line: Find the leased line that you want to disassociate and click **Disassociate** in the **Operation** column. In the message that appears, click **OK**.

**Edit a leased line group**

1. On the Leased Line Group Management page, find the leased line group that you want to
manage and click **Edit** in the **Operation** column.
2. In the Modify Express Connect Circuit Group dialog box, modify parameters and click **OK**.

**Delete a leased line group**

1. On the Leased Line Group Management page, find the leased line group that you want to
delete and click **Delete** in the **Operation** column.
2. In the message that appears, click **OK**.

> **Note:** This operation deletes the leased line group and disassociates the leased line group from leased lines. Proceed with caution.

###### 2.1.2.6.3 Access point management

Access points are Apsara Stack data centers located in different regions. One or more access points are deployed in each region. This topic describes how to manage access points.

**Query an access point**

1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
3. In the left-side navigation pane, choose **Basic Network** > **Leased Line Management** >
**Access Point Management**.
4. The list of access points is displayed. View the access point information in the following
columns: **Access point ID**, **Manage regions**, **Physical Region**, **Type**, **Status**, **Access**
**Point Name**, **Description**, **Physical location**, **Data center operator**, **Creation time**,
and **Modification time**. You can search for an access point by access point ID.
5. Click **Details** in the **Operation** column of an access point to view its details.

**Modify an access point**

1. Find the access point that you want to manage and click **Edit** in the **Operation** column.
2. In the **Edit access point** dialog box, modify the following parameters based on your
business requirements and click **OK**.

| Parameter | Description |
|---|---|
| Access point ID | The ID of the access point. This parameter cannot be modified. |
| Access Point Name | The name of the access point. You can enter a new name. The name must be 2 to 256 characters in length and cannot start with http:// or https:// . |
| Description | The description of the access point. You can modify the description content. The description must be 2 to 256 characters in length and cannot start with http:// or https:// . |

| Access point status | The access point status. Valid values: In good condition More customers are connected The access customer is full. Unavailable |
|---|---|
| Physical location | The location of the access point. |
| Data center operator | The Internet service provider (ISP) of the data center to which the access point belongs. |
| Physical Region | The region ID of the access point. |

###### 2.1.2.6.4 Access device management

This topic describes how to manage access devices.

**View the details of an access device**

1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
3. In the left-side navigation pane, choose **Basic Network** > **Leased Line Management** >
**Access Device Management**.
4. On the Access Device Management page, view the following information about access
devices: **Device ID**, **Region**, **Access point ID**, **Device status**, **Physical location**,
**Access Mode**, **Device Name**, **Description**, **Creation time**, and **Modification time**. You
can enter the ID of an access device in the **Device ID** field to obtain the information about the access device.
5. Find the access device that you want to view and click **Details** in the **Operation** column to
view the details of the access device.

**Modify the information about an access device**

1. On the Access Device Management page, find the access device that you want to manage
and click **Edit** in the **Operation** column.
2. In the **Edit access device** dialog box, modify the parameters that are described in the
following table and click **OK**.

| Parameter | Description |
|---|---|
| Device ID | The ID of the access device. This parameter cannot be modified. |
| Device status | The state of the access device. Valid values: In good condition The access customer is full. Unavailable |
| Device physical location | The location of the access device. |
| Whether to use XNET to manage CSW | Specifies whether to use XNET to manage Customer Switches (CSWs). Valid values: Yes No |
| XNET Endpoint URL | The URL of the XNET endpoint. |
| XNET Device ID | The ID of the XNET device. |
| Outer source IP address encapsulated by VXLAN | The outer source IP address encapsulated by Virtual Extensible Local Area Network (VXLAN). |

| VXLAN encapsulated internal source Mac | The inner source MAC address encapsulated by VXLAN. |
|---|---|
| Device Management IP | The management IP address of the access device. |
| Device Manufacturer name | The manufacturer of the access device. |
| Device model | The model of the access device. |
| Device Name | The name of the access device. |
| Description | The description of the access device. |

###### 2.1.2.6.5 Express Connect circuit management

You can use an Express Connect circuit to connect your on-premises data center to an Apsara Stack access point. This topic describes how to manage Express Connect circuits.

**Create an Express Connect circuit**

1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
3. In the left-side navigation pane, choose **Basic Network** > **Leased Line Management** >
**Express Connect Circuit Management**.
4. On the Physical Connection Management page, click **Create a physical connection**. In
the dialog box that appears, configure the following parameters and click **OK**.

| Parameter | Description |
|---|---|
| Physical Connection name | The name of the Express Connect circuit. The name can be 2 to 128 characters in length and cannot start with http:// or https:// . |
| Description | The description of the Express Connect circuit. The description can be 2 to 128 characters in length and cannot start with http:// or https:// . |
| BID | The bound ID. |
| Primary account ID | The ID of the virtual private cloud (VPC) to which you want to connect the Express Connect circuit. |
| Access point type | The method that is used to connect the Express Connect circuit. Set the value to VPC access point. |
| Access point ID | The region ID of the data center. |
| Access Port type | The type of the port. |
| Device Name | The name of the Customer Switch (CSW). The name can be 2 to 256 characters in length and cannot start with http:// or https:// . |
| Device Port | The port of the CSW. |
| Access bandwidth | The bandwidth of the access point to which the Express Connect circuit is connected. Unit: Mbit/s. Valid values: 2 to 10000. |
| Redundant physical connection | Select an existing Express Connect circuit as the redundant Express Connect circuit. When you establish the second Express Connect circuit, you can specify it as a redundant one and upload its ID. If you do so, Apsara Stack allocates a separate access device for higher availability. The Express Connect circuit that you specify must exist and be in the Allocated, Confirmed, or Enabled state. |

5. On the **Physical Connection Management** page, find the Express Connect circuit that
you created in the previous step, and click **Enable** in the **Operation** column. You can also click **Cancel**, **Termination**, **Delete**, **Approval**, **Reject**, or **Confirm** in the
**Operation** column of an Express Connect circuit to manage it.

###### 2.1.2.6.6 VBR management

A virtual border router (VBR) functions as a router between a customer-premises equipment (CPE) device and a virtual private cloud (VPC). VBRs route traffic between VPCs and data centers. This topic describes how to manage VBRs.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
3. In the left-side navigation pane, choose **Basic Network** > **Leased Line Management** >
**VBR Management**.
4. On the VBR management page, click **Create a virtual border router** . In the dialog box
that appears, configure the following parameters and click **OK**.

| Parameter | Description |
|---|---|
| BID | The bound ID. |
| Primary account ID | The ID of the virtual private cloud (VPC) to which you want to connect the VBR. |
| Region | The ID of the region in which the VBR is deployed. |
| Physical Connection ID | The ID of the Express Connect circuit that you want to connect to the VBR. |
| VLAN ID | The virtual local area network (VLAN) ID of the VBR. Valid values: 1 to 2999. Only the owner of the Express Connect circuit can specify or modify this parameter. |
| Local IP address | The local IP address of the Express Connect circuit. This parameter is required when the Express Connect circuit is not in the waiting state. Only the owner of the VBR can specify or modify this parameter. |
| Peer IP address | The peer IP address of the Express Connect circuit. This parameter is required when the Express Connect circuit is not in the waiting state. Only the owner of the VBR can specify or modify this parameter. |
| Subnet mask | The subnet mask that connects the local and peer IP addresses. This parameter is required when the Express Connect circuit is not in the waiting state. Only the owner of the VBR can specify or modify this parameter. |
| VBR Name | The name of the VBR. The name can be 2 to 128 characters in length and cannot start with http:// or https:// . |
| Description | The description of the VBR. The description can be 2 to 128 characters in length and cannot start with http:// or https:// . |

| Owner Bid | The bound ID of the VBR owner. |
|---|---|
| Owner AliUid | The Apsara Stack account ID of the VBR owner. |

5. After the VBR is created, it is in the **Active** state.
To manage the VBR, click **Release**, **Modify**, **Terminate**, or **Show Details** in the
**Operation** column of the VBR.

###### 2.1.2.6.7 Router interface management

After you create a virtual border router (VBR), you must create a pair of router interfaces to connect the VBR and a virtual private cloud (VPC). The connection initiator must be a VBR.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
3. In the left-side navigation pane, choose **Basic Network** > **Leased Line Management** >
**Router Interface Management**.
4. On the Router interface management page, click **Create a route interface**.
5. In the **Create a router interface** wizard, configure the following parameters in the **Local**
**information** step and click **Next Step**.
In this step, the information about the created VBR is entered.

| Parameter | Description |
|---|---|
| Create router type | The type of the router interface that you want to create. Valid values: Single A pair |
| Name | The name of the router interface. |
| Description | The description of the router interface. |
| BID | The bound ID. |
| UID | The ID of the VPC that you want to connect to the router interface. |
| Region | The ID of the router interface. |

| Router type | The router type. Valid values: VRouter VBR |
|---|---|
| Zone | The zone of the router interface. |
| Router ID | The ID of the VBR. |
| Access point ID | This parameter is available only when you set the Router type parameter to VBR. The ID of the access point. |
| Role | This parameter is available only when you set the Router type parameter to VRouter. The role of the router interface. Valid values: InitiatingSide AcceptingSide |
| Specifications | The specifications of the router interface. |
| Health check source IP | The source IP address that is used for health checks. |
| Health check destination IP | The destination IP address that is used for health checks. |
| Skip inventory check | Specifies whether to skip inventory check. Valid values: Yes No |

6. Configure the following parameters in the **Peer Information** step and click **Next Step**.
In this step, the information about the VPC that you want to connect to the router interface is entered.

| Parameter | Description |
|---|---|
| Name | The name of the router interface. |
| Description | The description of the router interface. |
| BID | The bound ID. |

| UID | The ID of the VPC that you want to connect to the router interface. |
|---|---|
| Region | The ID of the router interface. |
| Router type | The router type. Valid values: VRouter VBR |
| Zone | The zone of the router interface. |
| Router ID | The ID of the peer VPC. |
| Access point ID | The ID of the access point. |
| Role | The role of the router interface. Valid values: InitiatingSide AcceptingSide |
| Specifications | The specifications of the router interface. |
| Health check source IP | The source IP address that is used for health checks. |
| Health check destination IP | The destination IP address that is used for health checks. |
| Skip inventory check | Specifies whether to skip inventory check. Valid values: Yes No |

7. In the **Confirm configuration** step, confirm the local information and peer information
and then click **Create**.
8. On the Router interface management page, find the router interfaces that you created in
previous steps. If the router interfaces are in the **active** state, they are created.

###### 2.1.2.6.8 Route table management

A route table contains a set of rules that are called route entries. This topic describes how to manage route tables.
1. Configure routes that point to a virtual private cloud (VPC) and a data center for a virtual
border router (VBR). i. Log on to the Apsara Uni-manager Operations Console. ii. In the top navigation bar, choose **Product Operation** > **Networking** > **Network** iii. In the left-side navigation pane, choose **Basic Network** > **Leased Line Management** >
**Router Table Management**.
iv. On the Route table management page, specify the BID, UID, Route table ID, and Router ID parameters and click **Search** to search for route tables. v. Find the route table to which you want to add a route entry and click **Add Route Entry** in the **Operation** column. vi. In the Add Route Entry dialog box, configure the parameters to add a route whose destination CIDR block is the VPC CIDR block and click **Create**. The following table describes the parameters.

| Parameter | Description |
|---|---|
| Route Table ID | The ID of the route table to which you want to add the route entry. |
| Destination CIDR Block | The destination CIDR block. |
| ECMP | Specify whether to enable equal-cost multi-path (ECMP) routing. Valid values: Yes No |
| Next Hop Type | The type of the next hop. Note If you enable ECMP routing, set this parameter to RouterInterface. |
| Next Hop ID | The next hop interface ID. |

vii. Repeat the preceding steps to configure a route that points to a data center.

> **Note:** To view the next hop interface information, go to the VBR management page and view the value in the **VLAN Interface ID** column.

2. Configure a route that points to the router interface of a VBR for the VPC.
3. Configure a route that points to the VPC for the gateway device in the data center.

##### 2.1.2.7 opsDNS management

###### 2.1.2.7.1 opsDNS monitoring

1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
3. In the left-side navigation pane, choose **Basic Network** > **opsDNS Management** >
**opsDNS Monitoring**.
4. On the opsDNS Monitoring page, configure the **Cluster** and **Start/End Time** parameters.
Then, you can view the trend charts of QPS and domain name resolution success rate of instances in the selected cluster within the specified time range. Move the pointer over a specific point of time to view the corresponding data.

###### 2.1.2.7.2 opsDNS domain service

This topic describes how to configure an opsDNS domain name service.

**Usage notes**

1. Make sure that you know the scope of impact after you submit a Domain Name System
(DNS) record of a domain name. Pay attention to the potential impact of resolution type switching.
2. Operations on DNS records are idempotent. If you add DNS records of the same resolution
type to the same domain name, the new record overwrites the original one.
3. The time-to-live (TTL) of all DNS records under the same domain name and of the same
resolution type must be consistent. By default, the TTL configured for the DNS record that is added in the last operation prevails. The value of TTL is a positive integer of uint32.
4. CNAME records cannot coexist with records of other resolution types. Before you add a
CNAME record to a domain name, remove other records from the domain name. A domain name can have only one CNAME record.
5. You cannot add CNAME records to defined zones in the cloud, such as tbsite.net.
6. You can add domain names only to defined zones in the cloud. You cannot register a
domain name for a zone outside the cloud.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
3. In the left-side navigation pane, choose **Basic Network** > **opsDNS Management** >
**opsDNS Domain Service**.
4. On the opsDNS Domain Service page, view the domain name resolution information,
including **Domain Name**, **Resource Type**, **DNS Record**, and **TTL**. Click **Advanced Filter** to filter domain name resolution entries by **Domain Name**, **Record**
**Type**, **Record Value**, or their combinations.
5. Click **Create a domain name resolution record .** In the Create DNS Record dialog box,
configure the following parameters and click**OK.** It takes 0 to 5 minutes for a new domain name resolution entry to take effect.

| Parameter | Description |
|---|---|
| Domain Name | The record name of the domain name. Note The record name consists of a domain name prefix and a domain name suffix. The domain name prefix must meet the following format requirements: i. The domain name cannot contain underscores ( ). It can contain _ only letters, digits, and hyphens (-). ii. The domain name can be started only with letters or digits. iii. The domain name can be ended only with letters, digits, or periods (.). iv. A wildcard domain name is not allowed, which means that *. cannot be placed at the beginning of the domain name. |

| Resource Type | The resource type of the domain name resolution. Valid values: A AAAA CHAME Note i. A CNAME record cannot coexist with records of other types. If an A or AAAA record already exists and you want to add a CNAME record, you must delete the existing record before you can add a new one. ii. A domain name can have only one CNAME record. iii. You cannot configure CNAME records for the DNS zone. In this case, the fixed suffix of opsDNS, such as tbsite.net, amtest00 and inter.env00.shuguang.com, can only have NS, SOA, and A records, and CNAME records are not allowed. |
|---|---|
| DNS Record | The IP address to which the domain name is mapped. Note i. An A record must be a valid IPv4 address. ii. An AAAA record must be a valid IPv6 address. iii. A CNAME record must be a valid domain name. The requirements for the character set and length of the domain name must be the same as the format requirements for the Domain Name parameter, but the CNAME value cannot be a generic domain name. |
| TTL | The TTL of a DNS record. |

6. Go back to the opsDNS Domain Service page and click **Details** in the **Operation** column of
a domain name resolution entry. On the opsDNS Resolution Settings page, view the detailed DNS records and search for a DNS record by **Record Value**.
7. On the opsDNS Resolution Settings page, perform the following operations:
Create a DNS record: Click **Create DNS Record**. In the Create DNS Record dialog box, configure parameters and click **OK**. It takes 0 to 5 minutes for a new DNS record to take effect. Delete a DNS record: Find the DNS record that you want to delete and click **Delete** in the
**Operation** column. In the dialog box that appears, confirm the information, enter
**DELETE** in the field, and then click **OK**. After 0 to 5 minutes, the DNS record is deleted.

##### 2.1.2.8 Connection of intelligent computing servers to VPCs

**servers to VPCs**

You can use access gateways such as dedicated computing host switches (CHSWs) on the computing power platform to connect intelligent computing servers to virtual private clouds (VPCs). This helps implement the centralized management of intelligent computing servers. The system supports operations such as instance management, operation log management, bare metal network management, and O&M configurations to complete the daily O&M operations of access gateways on the computing power platform.

###### 2.1.2.8.1 Manage access gateways

On the Instance Management tab, you can view information about access gateways on the computing power platform, such as the access gateway name, internal Border Gateway Protocol (IBGP) role, and creation time.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
3. In the left-side navigation pane, choose **Basic Network > Cloud Gateways**.
4. Click the **Instance Management** tab. Then, click the **Scan for New Devices** tab.
i. Find the device that you want to manage and click **Manage** in the **Actions** column. Select the devices that you want to manage and click **Batch Manage** below the device list. ii. Configure the **IBGP Role** parameter for the device. The IBGP role specifies the role of the access gateway on the computing power platform in the environment. Valid values: Client, Deploy Client and RR on A Device, and Deploy RR on a Device.
**Client**: The access gateway on the computing power platform serves as the client of
the IBGP peer and is used only for server access.
**Deploy Client and RR on A Device**: The access gateway on the computing power
platform serves as the RR reflective route of the IBGP peer and is used for server access.
**Deploy RR on a Device**: The access gateway on the computing power platform only
serves as the RR reflective route of the IBGP peer and cannot be used for server access.

> **Important:** The following list describes the networking requirements for the IBGP role:
> Single-data center deployment: At least one set of access gateways on the computing power platform is deployed, and the IBGP roles of the access gateways are RR roles. The IBGP roles of other devices are Client.
> Multi-data center deployment: A set of access gateways on the computing power platform are deployed in at least two data centers, and the IBGP roles of the access gateways are RR roles. The IBGP roles of other devices are Client.
> You can select an RR role based on the following description:
> By default, the recommended value is Deploy Client and RR on A Device.
> If you have high requirements on network stability, we recommend that you select Deploy RR on a Device.

iii. Click **OK**.

**View access gateways on the computing power platform**

On the **Instance Management** tab, click the **Display Devices** tab to view the instance details.

| Parameter | Description |
|---|---|
| Cloud Gateway Name | The name of the access gateway on the computing power platform. |
| IBGP role | The role of the access gateway on the computing power platform in the environment. Client: indicates that the access gateway on the computing power platform serves as the client of the IBGP peer and only serves as a server. Deploy Client and RR on A Device : indicates that the access gateway on the computing power platform serves as the RR reflective route of the IBGP peer and serves as a server. Deploy RR on a Device: indicates that the access gateway on the computing power platform only serves as the RR reflective route of the IBGP peer. |
| Manage IP Address | The IP address of the access gateway on the computing power platform. |
| Management status | The initialization status of the access gateway on the computing power platform. Uninitialized Initializing Initialized |
| Created At | The creation time of the access gateway on the computing power platform. |

###### 2.1.2.8.2 Manage operation logs

To meet O&M requirements, you can view the records and results of API operations that are managed by bare metal instances and called by the Apsara Uni-manager Operations Console. The API records and results are provided by the access gateway of the computing power platform.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
3. In the left-side navigation pane, choose **Basic Network** > **Cloud Gateways**.
4. Click the **Operation Logs** tab.
5. Optional. In the Start/End Time section, configure the **Start Date** and **End Date**
parameters.
6. View the operation logs.

| Parameter | Description |
|---|---|
| ID | The index of the operation log. |
| Created At | The time when the operation was performed. |
| Bare Metal Name | The name of the bare metal instance that was applied for or released in the VPC. |
| API Operation | The category of the API operation. For example, you can apply for or release a bare metal instance in a VPC. add: A bare metal instance is applied for in the VPC. del: A bare metal instance is released in the VPC. del pc: A physical connection is deleted. _ del vbr: A Virtual Border Router (VBR) is deleted. _ del router intf: A router interface is deleted. _ _ del route entry: A route table entry is deleted. _ _ |
| Vswitch ID | The ID of the vSwitch when the bare metal instance is applied for or released in the VPC. |
| Cloud Gateway Name | The name of the access gateway of the computing power platform that is involved in the current API operation. |
| Port | The port to which the bare metal instance belongs. |
| Status | The status of the API operation. success indicates that the operation was successful. If the API operation is in progress, the value indicates the real-time status of the API operation. If the API operation is complete but the value is nots uccess, you can view the failure information in this column. Example: create vpc connection fail. |
| Actions | Click Details in the Actions column to view more details. For example, you can view the region ID, initiator, and status code. |

###### 2.1.2.8.3 Manage networks for bare metal instances

**instances**

On the Bare Metal Network Management tab, view information about the bare metal instance that is connected to a virtual private cloud (VPC) by using the access gateway on the computing power platform.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
3. In the left-side navigation pane, choose **Basic Network** > **Cloud Gateways**.
4. Click the **Bare Metal Network Management** tab.
5. Create a bare metal instance and add it to a VPC.
i. Click **Create Bare Metal Instance**, configure the **Bare Metal Name**, **SN**, and
**Description** parameters, and then click **OK**.
ii. Find the bare metal instance that you create, and click **Connect to VPC**.

| Parameter | Description |
|---|---|
| Bare Metal Name | The name of the bare metal instance. You do not need to configure this parameter. |
| Bare Metal SN | The serial number of the bare metal instance. You do not need to configure this parameter. |
| AK and SK | The AccessKey ID and AccessKey secret of the organization, which can be obtained from the Organizations page of the Apsara Uni- manager Management Console based on the organization to which the VPC belongs. For more information, see Manage organizations in Apsara Uni-manager Operations Console User Guide. |
| Region ID | The name of the region in the current environment. |
| Vswitch ID | The private vSwitch to which the bare metal instance belongs. |
| Cloud Gateway Name | The physical gateway to which the bare metal instance belongs. |
| Port | The port of the physical gateway to which the bare metal instance belongs. |
| Bare Metal Description | The description of the bare metal instance. |

iii. Click **OK**.

**What to do next**

After you create the bare metal instance, you can perform the following operations:

| Operation | Procedure |
|---|---|
| Query the bare metal instance. | 1. Select the start and end time, bare metal instance name, VPC ID, vSwitch ID, Virtual Border Router (VBR) ID, BD ID, or name of the access gateway of the computing power platform. 2. Specify search conditions. The system automatically displays the instances that meet the search conditions. |
| View the details of the bare metal instance. | 1. Click Details in the Actions column to view the ID of the Express Connect circuit, VBR ID, and logical name. 2. Click OK. |
| Close the connection to the VPC. | 1. Click Close the Connection to VPC in the Actions column of the bare metal instance. 2. In the message that appears, click Exit. |
| Delete the bare metal instance. | 1. Click Delete Instance in the Actions column. 2. In the message that appears, click Exit. |

###### 2.1.2.8.4 O&M configurations

###### 2.1.2.8.4.1 Apply for a bare metal instance in a VPC

**VPC**

In O&M emergency scenarios, you can use the feature to add the physical port of the access gateway associated with a bare metal instance to a virtual private cloud (VPC). The access gateway must be deployed on a computing power platform.

**Prerequisites**

> **Warning:** This operation is only for emergency scenarios and must be performed under the guidance of technical support personnel. Otherwise, normal business operations will be affected.
> The feature can only be used to connect the bare metal instance to the access gateway port. You cannot use the feature to perform operations on the bare metal instance. To configure the network port, IP address, and routing information of the bare metal instance, contact the product team.
> In most cases, you cannot use the feature to apply for a bare metal instance in a VPC. You can use the bare metal controller to call an API operation to enable the network of the bare metal instance.

i. Log on to the Apsara Uni-manager Operations Console. ii. In the top navigation bar, choose **Product Operation** > **Networking** > **Network** iii. In the left-side navigation pane, choose **Basic Network** > **Computing Access**
**Gateway**.
iv. Click the **O & M configuration** tab. v. Select **Apply for Bare Metal in VPC** from the drop-down list in the upper-left corner of the tab. vi. Configure the parameters described in the following table.

| Parameter | Description |
|---|---|
| Region ID | The name of the region in the current environment. |
| Computing power platform access gateway name | The name of the access gateway to which the bare metal instance is connected. |
| Vswitch ID | The ID of the vSwitch to which you want to add the bare metal instance. You can obtain the vSwitch ID from the VPC page in the Apsara Uni-manager Management Console. |
| Port | The port of the access gateway to which the bare metal instance is connected. |
| AK and SK | The AccessKey ID and AccessKey secret of the organization, which can be obtained from the Organizations page of the Apsara Uni-manager Management Console based on the organization to which the VPC belongs. For more information, see Manage organizations in Apsara Uni-manager Operations Console User Guide. |
| Bare Metal Name | The name of the bare metal instance that you want to apply for. The names of bare metal instances must be unique. |

vii. Click **Next**. viii. Check the information. If the information is correct, click **Confirm**. After the configurations are delivered, the **Success** message appears. You can search for the bare metal instance by instance name on the **Bare Metal network management** tab. If the bare metal instance is displayed, the bare metal instance is added to the VPC.

###### 2.1.2.8.4.2 Release a bare metal instance in a VPC

In O&M emergency scenarios, you can use the feature to disconnect the physical port of the access gateway associated with a bare metal instance from a virtual private cloud (VPC). The access gateway must be deployed on a computing power platform.

**Context**

> **Warning:** This operation is only for emergency scenarios and must be performed under the guidance of technical support personnel. Otherwise, normal business operations will be affected.
> The feature can only be used to disconnect the bare metal instance from the access gateway port. You cannot use the feature to perform operations on the bare metal instance. To configure the network port, IP address, and routing information of the bare metal instance, contact the product team.
> In most cases, you cannot use the feature to release a bare metal instance in a VPC. You can use the bare metal controller to call an API operation to delete the network of the bare metal instance.

1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
3. In the left-side navigation pane, choose **Basic Network** > **Computing Access Gateway**.
4. Click the **O & M configuration** tab.
5. Select **Release Bare Metal in VPC** from the drop-down list in the upper-left corner of the
tab.
6. Configure the parameters described in the following table.

| Parameter | Description |
|---|---|

| Region ID | The name of the region in the current environment. |
|---|---|
| Bare Metal Name | The name of the bare metal instance that you want to release. You can search for the bare metal instance on theB are Metal network management tab by instance name. |

> **Note:** If the specified values are incorrect, click **Re-enter** in the lower part of the tab and configure the parameters again.

7. Click **Next**.
8. Check the information. If the information is correct, click **Confirm**.
After the configurations are delivered, the **Success** message appears. In this case, you can search for the bare metal instance by instance name on the **Bare Metal network**
**management** tab. If the bare metal instance is not displayed, the instance is released.

###### 2.1.2.8.4.3 Delete a route table entry

In O&M emergency scenarios, you can use the feature to delete route table entries that point to the subnet of a bare metal instance in a virtual private cloud (VPC) and the default route table entries of a virtual border router (VBR).

> **Warning:** This operation is only for emergency scenarios and must be performed under the guidance of technical support personnel. Otherwise, normal business operations will be affected.

In most scenarios, you cannot use this feature to delete a VPC route table entry. This operation is only used for emergency scenarios. You can perform this operation to delete only one route table entry at a time. To delete multiple route table entries, you must perform this operation multiple times.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
3. In the left-side navigation pane, choose **Basic Network** > **Computing Access Gateway**.
4. Click the **O & M configuration** tab.
5. Select **Delete Route Table Entry** from the drop-down list in the upper-left corner of the
tab.

| Parameter | Description |
|---|---|
| Region ID | The name of the region in the current environment. |
| Route Table ID | To obtain the ID of the VPC route table or VBR route table, click theB are Metal network management tab, search for the bare metal instance, and view the details of the bare metal instance. |
| Router Interface ID | To obtain the router interface of the VPC or VBR, click theB are Metal network management tab, search for the bare metal instance, and view the details of the bare metal instance. |
| Routing Destination CIDR | The destination CIDR block of the subnet of the bare metal instance. To obtain the destination CIDR block, click the Bare Metal network management tab, search for the bare metal instance, and view the details of the bare metal instance. |
| AK and SK | The AccessKey ID and AccessKey secret of the organization to which the bare metal instance belongs. You can obtain the AccessKey pair of the organization on the Organizations page of the Apsara Uni-manager Management Console. For more information, see Manage organizations in Apsara Uni-manager Operations Console User Guide. |

6. Click Next.
7. Check the parameters. If the settings are correct, click**Confirm**. After the configurations
are delivered, the **Success** message appears.

###### 2.1.2.8.4.4 Delete a router interface

In emergency O&M scenarios, you can use this feature to delete the router interface of a virtual private cloud (VPC) or virtual border router (VBR).

> **Warning:** This operation is only for emergency scenarios and must be performed under the guidance of technical support personnel. Otherwise, normal business operations will be affected.

1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
3. In the left-side navigation pane, choose **Basic Network** > **Computing Access Gateway**.
4. Click the **O & M configuration** tab.
5. Select **Delete Router Interface** from the drop-down list in the upper-left corner of the tab.
6. Configure the parameters described in the following table.

| Parameter | Description |
|---|---|
| Region ID | The name of the region in the current environment. |
| Router Interface ID | To obtain the router interface of the VPC or VBR, click the Bare Metal network management tab, search for the bare metal instance, and view the details of the bare metal instance. |
| AK and SK | The AccessKey ID and AccessKey secret of the organization to which the bare metal instance belongs. You can obtain the AccessKey pair of the organization on the Organizations page of the Apsara Uni-manager Management Console. For more information, see Manage organizations in Apsara Uni-manager Operations Console User Guide. |

7. Click Next.
8. Check the parameters. If the settings are correct, click**Confirm**. After the configurations
are delivered, the **Success** message appears.

###### 2.1.2.8.4.5 Delete a VBR

In O&M emergency scenarios, you can use this feature to delete a virtual border router (VBR).

> **Warning:** This operation is only for emergency scenarios and must be performed under the guidance of technical support. Otherwise, normal business operations will be affected.

1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
3. In the left-side navigation pane, choose **Basic Network** > **Computing Access Gateway**.
4. Click the **O & M configuration** tab.
5. Select **Delete VBR** from the drop-down list in the upper-left corner of the tab.
6. Configure the parameters described in the following table.

| Parameter | Description |
|---|---|
| Region ID | The name of the region in the current environment. |
| VBR ID | The ID of the VBR to be deleted. To obtain the VBR ID, click the Bare Metal network management tab, search for the bare metal instance, and view the details of the bare metal instance. |
| AK and SK | The AccessKey ID and AccessKey secret of the organization to which the VBR belongs. You can obtain the AccessKey pair of the organization on the Organizations page of the Apsara Uni-manager Management Console. For more information, see Manage organizations in Apsara Uni-manager Operations Console User Guide. |

7. Click **Next**.
8. Check the information. If the information is correct, click **Confirm**.

###### 2.1.2.8.4.6 Delete an Express Connect circuit

In O&M emergency scenarios, you can use this feature to delete an Express Connect circuit.

> **Warning:** This operation is only for emergency scenarios and must be performed under the guidance of technical support. Otherwise, normal business operations will be affected.

1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
3. In the left-side navigation pane, choose **Basic Network** > **Computing Access Gateway**.
4. Click the **O & M configuration** tab.
5. Select **Delete Express Connect Circuit** from the drop-down list in the upper-left corner of
the tab.
6. Configure the parameters described in the following table.

| Parameter | Description |
|---|---|
| Region ID | The name of the region in the current environment. |

| Express Connect Circuit ID | The ID of the Express Connect circuit to be deleted. To obtain the Express Connect circuit ID, click the Bare Metal network management tab, search for the bare metal instance, and view the details of the bare metal instance. |
|---|---|
| AK and SK | The AccessKey ID and AccessKey secret of the organization to which the VPC belongs. You can obtain the AccessKey pair of the organization on the Organizations page of the Apsara Uni-manager Management Console. For more information, see Manage organizations in Apsara Uni-manager Operations Console User Guide. |

7. Click **Next**.
8. Check the information. If the information is correct, click **Confirm**.

###### 2.1.2.8.4.7 Delete all resources

In O&M emergency scenarios, you can use this feature to delete all resources. The resources include virtual private cloud (VPC) route table entries, virtual border router (VBR) route table entries, VPC router interfaces, VBR router interfaces, VBRs, and Express Connect circuits.

> **Warning:** This operation is only for emergency scenarios and must be performed under the guidance of technical support. Otherwise, normal business operations will be affected.

1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
3. In the left-side navigation pane, choose **Basic Network** > **Computing Access Gateway**.
4. Click the **O & M configuration** tab.
5. Select **Delete ALL Resources** from the drop-down list in the upper-left corner of the tab.
6. Configure the parameters described in the following table.

| Parameter | Description |
|---|---|
| Region ID | The name of the region in the current environment. |
| Computing power platform access gateway name | The name of the access gateway to which the bare metal instance is connected. |

| AK and SK | The AccessKey ID and AccessKey secret of the organization to which the VPC belongs, which can be obtained from the Organizations page of the Apsara Uni-manager Management Console. For more information, see Manage organizations in Apsara Uni-manager Operations Console User Guide. |
|---|---|
| VPC Router Interface ID | The ID of the VPC router interface. To obtain the VPC router interface ID, click the Bare Metal network management tab, search for the bare metal instance, and view the details of the bare metal instance. |
| VPC Route Table ID | The ID of the VPC route table. To obtain the VPC route table ID, click the Bare Metal network management tab, search for the bare metal instance, and view the details of the bare metal instance. |
| VBR Route Table ID | The VBR route table ID. To obtain the VBR route table ID, click the Bare Metal network management tab, search for the bare metal instance, and view the details of the bare metal instance. |
| VPC CIDR1 | A destination CIDR block that points to the subnet of the bare metal instance in the VPC. To obtain the destination CIDR block, click the Bare Metal network management tab, search for the bare metal instance, and view the details of the bare metal instance. |
| VPC CIDR2 | Another destination CIDR block that points to the subnet of the bare metal instance in the VPC. To obtain the destination CIDR block, click the Bare Metal network management tab, search for the bare metal instance, and view the details of the bare metal instance. |
| VBR Router Interface ID | The VBR router interface ID. To obtain the VBR router interface ID, click the Bare Metal network management tab, search for the bare metal instance, and view the details of the bare metal instance. |
| VBR ID | The ID of the VBR to be deleted. To obtain the VBR ID, click the Bare Metal network management tab, search for the bare metal instance, and view the details of the bare metal instance. |
| Express Connect Circuit ID | The ID of the Express Connect circuit to be deleted. To obtain the Express Connect circuit ID, click the Bare Metal network management tab, search for the bare metal instance, and view the details of the bare metal instance. |

| Trunk ID | Obtain the value of the Port parameter from the Bare Metal network management tab and specify the last integer of the value as a trunk ID. For example, if the port number is 10GE1/0/40, set Trunk ID to 40. You can also leave the parameter empty. |
|---|---|

7. Click **Next**.
8. Check the information. If the information is correct, click **Confirm**.

###### 2.1.2.8.4.8 View the bandwidth of the Express Connect circuit

**Connect circuit**

You can view the bandwidth of the Express Connect circuit when the access gateway is connected to a virtual private cloud (VPC) based on your O&M requirements.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
3. In the left-side navigation pane, choose **Basic Network** > **Computing Access Gateway**.
4. Click the **O & M configuration** tab.
5. In the left-side drop-down list, select **View Express Connect Circuit Bandwidth**.
6. Configure the filter conditions and click **Query**. The information about the bandwidth of the
Express Connect circuit that meets the search conditions is displayed. The bandwidth information includes the specifications of the Express Connect circuit on the PHSW of the current VPC. Then, you can check the table on the left and obtain the bandwidth (bit/s) based on the specification.

**Search conditions**

| Parameter | Description |
|---|---|
| Region ID | The name of the region in the current environment. |
| Router Interface ID | The ID of the virtual border router (VBR) interface. On the Bare Metal network management tab, specify the ID of the VPC and the name of the access gateway. Then, click Details in the Actions column. |
| AK and SK | The AccessKey ID and AccessKey secret. You can obtain the values on the Organizations page of the Apsara Uni-manager Management Console based on the organization to which the VBR belongs. For more information, see Manage organizations in Apsara Uni-manager Operations Console User Guide. |

**Bandwidth comparison table**

| Specification string | Bandwidth (bit/s) |
|---|---|
| Large.1 | 1G |
| Large.2 | 2G |
| Large.5 | 5G |
| Xlarge.1 | 10G |
| Xlarge.2 | 20G |
| Xlarge.4 | 40G |
| Xlarge.5 | 50G |
| Xlarge.8 | 80G |
| Xlarge.10 | 100G |
| Xlarge.16 | 160G |
| Xlarge.20 | 200G |

###### 2.1.2.8.4.9 View trunk usage

You can view trunk usage to obtain the latest information about the usage of hardware ports at the earliest opportunity.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
3. In the left-side navigation pane, choose **Basic Network** > **Computing Access Gateway**.
4. Click the **O & M configuration** tab.
5. In the left-side drop-down list, select **View Trunk Usage**.
6. Specify a trunk ID and a computing access gateway name, select a trunk state, and then
click **Search**. The trunk state can be Idle, Used, Creating, or Deleting.

> **Note:** You can obtain the value of the **Port** parameter from the **Bare Metal network** **management** tab and specify the last integer of the value as a trunk ID. For example, if the port number is 10GE1/0/40, specify 40 as the trunk ID.

7. View results that meet the filter conditions in a list.

###### 2.1.2.8.4.10 View BM VPN usage

You can view information about the BM VPN that is assigned to a computing access gateway.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** **>** **Networking** **>** **Network**
3. In the left-side navigation pane, choose **Basic Network** > **Computing Access Gateway**.
4. Click the **O & M configuration** tab.
5. In the left-side drop-down list, select **View BM VPN Usage**.
6. Specify a **computing access gateway name**, a **VXLAN ID**, and a **BM VPN name**, select
a trunk state, and then click **Search**. The trunk state can be Succeeded or Creating.
7. The results that meet the filter conditions are displayed in the list.

###### 2.1.2.8.4.11 View BD usage

You can view the BD usage to learn about the BD configuration distribution at the earliest opportunity.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
3. In the left-side navigation pane, choose **Basic Network** > **Computing Access Gateway**.
4. Click the **O & M configuration** tab.
5. In the left-side drop-down list, select **View BD Usage**.
6. Specify a computing access gateway name, a BD ID, and a vSwitch ID, select a trunk state,
and then click **Search**. The Status options contain Succeeded, Creating, and Deleting.
7. The results that meet the filter conditions are displayed in the list.

###### 2.1.2.8.4.12 Check the initialization configuration

You can use this feature to check whether the initialization configuration of vSwitches for computing access gateways is complete.

> **Note:** The feature only checks the initialization status and whether the initialization configuration is successful. The feature does not perform operations on bare metal instances.

1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
3. In the left-side navigation pane, choose **Basic Network** > **Computing Access Gateway**.
4. Click the **O & M configuration** tab.
5. In the left-side drop-down list, select **Check the Initialization Configuration**.
6. Configure the parameters. The following table describes the parameters.

| Parameter | Description |
|---|---|
| Region ID | The ID of the region in the current environment. |
| HSW Name | The name of the vSwitch that you want to check. |

7. Click **Next**.
8. Confirm the parameter settings and click **Check** to check the initialization configuration of
the specified vSwitch.

###### 2.1.2.8.4.13 Check the route configuration

You can use this feature to identify abnormal operations and scan the vSwitches of computing access gateways to check whether the route configuration of bare metal instances is valid.

> **Note:** The feature only checks whether the route configuration of a bare metal instance is valid. The feature does not perform operations on the instance.

1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
3. In the left-side navigation pane, choose **Basic Network** > **Computing Access Gateway**.
4. Click the **O & M configuration** tab.
5. In the left-side drop-down list, select **Check the Route Configuration**.
6. Configure the parameters. The following table describes the parameters.

| Parameter | Description |
|---|---|
| Region ID | The ID of the region in the current environment. |
| Bare Metal Name | The name of the bare metal instance whose routing configuration you want to check. You can obtain the name of the bare metal instance on theB are Metal network management tab. |
| AK and SK | The AccessKey ID and AccessKey secret of the organization to which the bare metal instance belongs. You can obtain the AccessKey pair of the organization on the Organizations page of the Apsara Uni-manager Management Console. For more information, see Manage organizations in Apsara Uni-manager Operations Console User Guide. |

7. Click **Next**.
8. Confirm the parameter settings and click **Check** to check the route configuration.

###### 2.1.2.8.4.14 Display information about bare metal network gateways

**network gateways**

You can use this feature to check the gateways of vSwitches in scenarios where bare metal networks are unavailable and O&M emergency is performed. The feature only checks the gateway information of vSwitches. The feature does not perform operations on bare metal instances.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
3. In the left-side navigation pane, choose **Basic Network** > **Computing Access Gateway**.
4. Click the **O & M configuration** tab.
5. In the left-side drop-down list, select **Display the Information of Bare Metal Network**
**Gateways**.
6. Configure the parameters. The following table describe the parameters.

| Parameter | Description |
|---|---|
| Region ID | The ID of the region in the current environment. |

| Vswitch ID | The vSwitch ID of the bare metal instance that you want to manage. You can obtain the vSwitch ID from the Virtual Private Cloud (VPC) console. |
|---|---|
| AK and SK | The AccessKey ID and AccessKey secret of the organization, which can be obtained from the Organizations page of the Apsara Uni-manager Management Console based on the organization to which your VPC belongs. For more information, see Manage organizations in Apsara Uni-manager Operations Console User Guide. |

7. Click **Next**.
8. Confirm the parameter settings and click **Check** to check the information about bare metal
network gateways.

#### 2.1.3 Networking services

##### 2.1.3.1 SLB O&M

###### 2.1.3.1.1 SLB cluster management

After you add tags to Server Load Balancer (SLB) clusters, you can easily select clusters in the tenant console. This improves the usability of SLB clusters.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
3. In the left-side navigation pane, choose **Network Products** > **SLB O&M** > **SLB Cluster**
**Management**.
4. On the SLB Cluster Management page, select a region ID and click **Search** to view the
cluster information.
5. Find the cluster that you want to manage and click **Edit Tag** in the **Actions** column. In the
dialog box that appears, modify the tag name and click **OK**.

> **Note:** The default cluster tag named **default** cannot be modified.

###### 2.1.3.1.2 SLB management

The SLB Management module contains the Cluster Monitoring and Instance Monitoring tabs and shows the basic information, running status, and usage of SLB network products.

##### 2.1.3.2 Proxy O&M

###### 2.1.3.2.1 Proxy management

The SLB Proxy Management module displays information about Layer 7 Server Load Balancer (SLB) resources and monitoring O&M.

**View information about proxy clusters**

On the Proxy Cluster tab, you can view the node status, usage data, and aggregation monitoring metrics of an SLB proxy cluster.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
3. In the left-side navigation pane, choose **Network Products** > **Proxy O&M** > **SLB Proxy**.
4. On the **Proxy Cluster** tab of the SLB Proxy Management page, select the cluster that you
want to view from the **Cluster** drop-down list. Then, view the cluster information in the
**Node Information** and **Cluster Aggregation Monitoring** sections.
5. View the cluster information in the **Node Information** section.
View node information in the Node, Cluster, and Item columns. Find the node whose details you want to view and click **Details** in the **Operation** column. On the SLB Proxy Node Details page, view the metrics of the node.

> **Note:** The range between the start time and end time cannot exceed 12 hours.
> You can click **Last5Minutes**, **Last30Minutes**, **Last1Hour**, or **Last6Hours** in the time range section to query the usage data within the time range.
> You can move the pointer over a point in time in a chart to view the values of all metrics at the point in time.

The following table describes the metrics.

| Category | Metric | Description |
|---|---|---|
| slb proxy cpu _ _ | hirq | The percentage of the time that the system takes to handle hardware interrupts to the total operating time of the system. |
|   | sirq | The percentage of the time that the system takes to handle software interrupts to the total operating time of the system. |
|   | sys | The system CPU utilization. |
|   | user | The percentage of the time that the CPU takes to execute user processes to the total time. |

|   | util | The percentage of the CPU usage time to the total time. |
|---|---|---|
|   | wait | The percentage of the time that the CPU waits for I/O operations to the total time. |
| slb proxy diskio _ _ | await | The average duration of I/O requests sent to the device that requests for the service. Unit: milliseconds. |
|   | qusize | The average queue length of requests sent to the device. |
|   | rqsize | The average size of requests sent to the device by sector. |
|   | rrqms | The number of merged read requests sent to the device per second. |
|   | rs | The number of read requests sent to the device per second. |
|   | rsecs | The number of sectors read from the device per second. |
|   | svctm | The average service time to make I/O requests to the device. Unit: milliseconds. |
|   | util | The percentage of the time that CPU takes to make I/O requests to the device to the total CPU time, which indicates the bandwidth utilization of the device. |
|   | wrqms | The number of merged write requests sent to the device per second. |
|   | ws | The number of write requests sent to the device per second. |
|   | wsecs | The number of sectors written to the device per second. |
|   | load1 | The average system load within 1 minute. Unit: %. |

| rm Operation and Main perations Guide·Netwo ions | tena Apsara Uni-manager Operations rk o Consol |   |
|---|---|---|
| slb proxy load _ _ |   |   |
|   | load5 | The average system load within 5 minutes. Unit: %. |
|   | load15 | The average system load within 15 minutes. Unit: %. |
|   | plit | The number of active tasks in the system during the sampling time, excluding the completed tasks. |
|   | runq | The number of tasks in the queue during the sampling time. |
| slb proxy mem _ _ | Dirty | The volume of data waiting to be written back to the disk. Unit: KB. |
|   | SReclaimable | The size of recoverable slab memory. Unit: KB. |
|   | Shmem | The size of shared memory that has been allocated. Unit: KB. |
|   | Slab | The cache size of kernel data structure. Unit: KB. |
|   | Writeback | The volume of data being written back. Unit: KB. |
|   | buff | The size of memory used as a buffer. Unit: KB. |
|   | cach | The size of memory allocated by the operating system to the file buffer. Unit: KB. |
|   | free | The idle physical memory size. Unit: KB. |
|   | total | The total system memory size Unit: KB. |
|   | used | The size of used memory. Unit: KB. |
|   | util | The memory usage. |
|   | accept | The total number of received TCP connections. |
|   | active | The number of active TCP connections, including the read, write, and waiting requests. |

| ra Uni-manager Operat ole |   |   |
|---|---|---|
| slb proxy qps _ _ |   |   |
|   | cps | The average number of TCP connections received per second. |
|   | h2qps | The number of HTTP/2 requests processed per second. |
|   | handle | The total number of processed TCP connections. |
|   | handleps | The average number of connections processed per second. |
|   | httpqps | The number of HTTP requests processed per second. |
|   | qps | The number of requests processed per second. |
|   | read | The number of TCP connections that read request data. |
|   | reqs | The total number of generated requests. |
|   | rt | The average response time. Unit: milliseconds. |
|   | spdyps | The number of SPDY requests processed per second. |
|   | sslf | The number of failed SSL connections. |
|   | sslhst | The average time for an SSL handshake. Unit: milliseconds. |
|   | sslqps | The number of SSL requests processed per second. |
|   | sslv3f | The number of failed SSLv3 connections. |
|   | wait | The number of waiting persistent TCP connections. |
|   | write | The number of TCP connections that write response data to users. |
|   | AtmpFa | The number of failed TCP connections per second. |

| rm Operation and Main perations Guide·Netwo ions | tena Apsara Uni-manager Operations rk o Consol |   |
|---|---|---|
| slb proxy tcp _ _ |   |   |
|   | CurrEs | The number of current TCP connections. |
|   | EstRes | The number of times that TCP connections are reset per second. |
|   | active | The number of TCP connections that are actively initiated per second. |
|   | iseg | The number of inbound TCP segments per second. |
|   | lisove | The number of TCP requests dropped because the listenaccept queue is full. |
|   | outseg | The number of outbound TCP segments per second. |
|   | pasive | The number of passively generated TCP connections per second. |
|   | retran | The retransmission rate of segments. The value is calculated based on the retransmitted segments and the total segments. |

6. In the **Cluster Aggregation Monitoring** section, specify the start time and end time to
view the aggregation metrics of the cluster on the **Core Metrics** and **All Metrics** tabs. The following table describes the metrics.

> **Note:** The range between the start time and end time cannot exceed 12 hours.
> You can move the pointer over a point in time in a chart to view the values of all metrics at the point in time.

| Tab | Metric | Description |
|---|---|---|
| Core Metrics | qps | The number of requests processed per second. |
|   | accept | The total number of received TCP connections. |
|   | active | The number of active TCP connections, including the read, write, and waiting requests. |
|   | cps | The average number of TCP connections received per second. |

| All Metrics |   |   |
|---|---|---|
|   | h2qps | The number of HTTP/2 requests processed per second. |
|   | handle | The total number of processed TCP connections. |
|   | handleps | The average number of connections processed per second. |
|   | httpqps | The number of HTTP requests processed per second. |
|   | qps | The number of requests processed per second. |
|   | read | The number of TCP connections that read request data. |
|   | reqs | The total number of generated requests. |
|   | rt | The average response time. Unit: milliseconds. |
|   | spdyps | The number of SPDY requests processed per second. |
|   | sslf | The number of failed SSL connections. |
|   | sslhst | The average time for an SSL handshake. Unit: milliseconds. |
|   | sslqps | The number of SSL requests processed per second. |
|   | sslv3f | The number of failed SSLv3 connections. |
|   | wait | The number of waiting persistent TCP connections. |
|   | write | The number of TCP connections that write response data to users. |

**View information about proxy instances**

You can view the monitoring metrics and usage data charts of SLB proxy instances.

**Prerequisites**

The NetworkBaseServiceCluster cluster for BaseServiceAll is deployed and has reached the desired state.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
3. In the left-side navigation pane, choose **Network Products** > **Proxy O&M** > **SLB Proxy**.
4. On the **Proxy Instance** tab, select a cluster from the **Cluster** drop-down list, enter an
instance ID or a virtual IP address in the **Enter Instance ID or VIP** field, select a listener, and then click **Search**.
5. Click the **Request**, **Connect**, **Traffic**, **Latency**, and **Status Code** tabs to view the usage
data charts of the corresponding metrics. The following table describes the metrics.

| Metric | Description |
|---|---|
| qps | The average number of requests received per second. |
| req concurrent _ | The number of concurrent requests. |
| conn concurrent _ | The number of concurrent connections. |
| cps | The average number of connections received per second. |
| outBitsPS | The outbound traffic rate. Unit: bits/s. |
| inBitsPS | The inbound traffic rate. Unit: bits/s. |
| upstream rt _ | The average processing latency of backend Elastic Compute Service (ECS) instances. Unit: milliseconds. |
| status code 2xx _ _ | The number of requests for which a 2xx response code is returned. |
| status code 3xx _ _ | The number of requests for which a 3xx response code is returned. |
| status code 4xx _ _ | The number of requests for which a 4xx response code is returned. |
| status code 5xx _ _ | The number of requests for which a 5xx response code is returned. |

| status code other _ _ | The number of requests for which a response code other than 2xx, 3xx, 4xx, and 5xx is returned. |
|---|---|
| upstream code 4xx _ _ | The number of requests with a 4xx response code returned by backend ECS instances. |

##### 2.1.3.3 XGW O&M

###### 2.1.3.3.1 XGW cluster management

1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
3. In the left-side navigation pane, choose **Network Products** > **XGW O&M** > **XGW Cluster**
**Management**.
4. On the XGW Cluster Management page, select a region ID from the **Region** drop-down list
and click **Synchronize data** to obtain the latest data of the XGW cluster list.
5. Find the cluster that you want to manage, click **Quick Settings** in the **Operation** column,
and then select **Set backup zone**.

> **Note:** The cluster that you select as the secondary zone must have the same architecture and reside in the same region as the current cluster.
> Click **Set backup zone**. Then, the system checks the data. After the data is checked, you can configure a secondary zone.

6. Select a secondary zone from the Select backup zone drop-down list and click **OK**.

###### 2.1.3.3.2 XGW management

The XGW Management module allows you to manage virtual private cloud (VPC) gateways and view the usage data of device nodes and service instances.

**View XGW clusters**

The XGW Management module allows you to view the basic information, status, aggregated traffic, and usage of each device node of XGW clusters.

**Prerequisites**

The NetworkBaseServiceCluster cluster for BaseServiceAll has been deployed and has reached the desired state.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
3. In the left-side navigation pane, choose **Network Products** > **XGW O&M** > **XGW**
**Management**.
4. On the **XGW Cluster** tab of the XGW Management page, select the cluster that you want to
view from the **Cluster** drop-down list. Then, view the cluster information in the **Node**
**Information** and **Aggregated Traffic** sections.
5. View the cluster information in the **Node Information** section.
View node information in the following columns: **Hostname**, **IDC**, **IP**, and **State**. Find the node whose details you want to view and click **Details** in the **Operation** column. In the panel that appears, view the usage of the node by metric. For more information about the metrics, see the table in the following step.
6. In the **Aggregated Traffic** section, view the usage of the device nodes by metric. The
following table describes the metrics.

> **Note:** The range between the start time and end time cannot exceed 24 hours.
> You can select **Last1Hour**, **Last3Hours**, **Last6Hours**, or **Last1Day** to query the usage data within the selected time range.
> You can move the pointer over a point in time in a chart to view the values of the corresponding metrics.

| Section | Metric | Description |
|---|---|---|
| ByteRate | InByteRate | The inbound bandwidth. Unit: bit/s. |
|   | OutByteRate | The outbound bandwidth. Unit: bit/s. |
| PacketLossRate | PacketLossRateIn | The number of inbound packets dropped per second. Unit: packets per second (PPS). |
|   | PacketLossRateOut | The number of outbound packets dropped per second. Unit: PPS. |
| PacketRate | PacketRateIn | The number of inbound packets per second. Unit: PPS. |
|   | PacketRateOut | The number of outbound packets per second. Unit: PPS. |

**View instance monitoring information**

On the Instance Monitoring tab, you can view the usage of an instance in an XGW cluster.

**Prerequisites**

The NetworkBaseServiceCluster cluster for BaseServiceAll has been deployed and has reached the desired state.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
3. In the left-side navigation pane, choose **Network Products** > **XGW O&M** > **XGW**
**Management**.
4. Click the **Instance Monitoring** tab. On this tab, select the cluster that you want to manage
from the **Cluster** drop-down list, enter the IP address of the instance that you want to query, and then click **Search**. The following table describes the metrics.

> **Note:** The range between the start time and end time cannot exceed 12 hours.
> You can click **Last1Hour**, **Last3Hours**, **Last6Hours**, or **Last1Day** to query the usage data within the selected time range.
> You can move the pointer over a point in time in a chart to view the values of the corresponding metrics.

| Metric | Description |
|---|---|
| InBps | The inbound bandwidth. Unit: bit/s. |
| InDropSpeed | The number of inbound packets dropped per second. Unit: PPS. |
| InFinSpeed | The number of inbound FIN packets per second. Unit: PPS. |
| InPps | The number of inbound packets per second. Unit: PPS. |
| InRateLimitDropSpeed | The number of inbound packets dropped per second due to throttling. Unit: PPS. |
| InRstSpeed | The number of inbound RST packets per second. Unit: PPS. |
| InSynAckSpeed | The number of inbound SYN/ACK packets per second. Unit: PPS. |
| OutBps | The outbound bandwidth. Unit: bit/s. |

| OutDropSpeed | The number of outbound packets dropped per second. Unit: PPS. |
|---|---|
| OutFinSpeed | The number of outbound FIN packets per second. Unit: PPS. |
| OutPps | The number of outbound packets per second. Unit: PPS. |
| OutRateLimitDropSpeed | The number of outbound packets dropped per second due to throttling. Unit: PPS. |
| OutRstSpeed | The number of outbound RST packets per second. Unit: PPS. |
| OutSynAckSpeed | The number of outbound SYN/ACK packets per second. Unit: PPS. |

###### 2.1.3.3.3 NAT gateway monitoring

In scenarios such as multi-cloud geo-disaster recovery and hybrid cloud, you can query the monitoring data of a NAT gateway by tunnel ID.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
3. In the left-side navigation pane, choose **Network Products** > **XGW O&M** > **NAT**
**Gateway Monitoring**.
4. On the NAT Gateway Monitoring page, select a cluster, specify a time range, enter the
tunnel ID, and then click **Query** to view the trend chart of the NAT gateway.

> **Note:** You can move the pointer over a point in time in the chart to view the corresponding monitoring data.

The following table describes the metrics displayed in the chart.

| Metric | Description |
|---|---|

| e Operations Guide·Network o ations | Apsara Uni-manager Operations Consol |
|---|---|

| CurrNum | The number of connected instances. |
|---|---|
| EstablishRate | The number of connections that are established per second. |
| RatelimitDrop | The number of packets dropped due to throttling. |
| CapacityDropInc | The number of packets dropped due to the Inc capacity limit. |
| CapacityDrop | The number of packets dropped due to the capacity limit. |
| IninNum | The number of initialized instances. |
| RatelimitDropInc | The number of packets dropped due to the Inc throttling. |

###### 2.1.3.3.4 Router interface instances

This topic describes how to view the instances of a router interface and the O&M information about the instances.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
3. In the left-side navigation pane, choose **Network Products** > **XGW O&M** > **RI Instances**.
4. On the RI Instances page, click Advanced Filter. In the **Search Condition** section, select
**VPC ID** or **UID** from the drop-down list and enter the corresponding value in the field.
5. Optional. Specify the **Connection Type**, **RI ID**, **Router Type**, **Router ID**, **Instance State**,
**Instance Name**, **Peer RI ID**, **Peer Router ID**, **Peer Router Type**, and **Peer Region ID**
parameters to filter router interface instances.
6. Click **Search**. The router interface instances that match the UID are displayed on the RI
Instances page.

> **Note:** If you select **VPC ID** from the drop-down list in the **Search Condition** section, all router interface instances that belong to the virtual private cloud (VPC) are automatically queried.

7. Find the router interface instance that you want to manage and click **Details** in the
**Operation** column. On the details page, view the detailed O&M information about the
router interface instance. If usage data exists, the usage data is also displayed on the page.

##### 2.1.3.4 CGW O&M

###### 2.1.3.4.1 CGW management

The CGW Management module allows you to view the basic information, status, aggregated traffic, and usage of each device node of CGW clusters.

**Prerequisites**

The NetworkBaseServiceCluster cluster for BaseServiceAll has been deployed and has reached the desired state.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
3. In the left-side navigation pane, choose **Network Products** > **CGW O&M** > **CGW**
**Management**.
4. On the **CGW Cluster** tab of the CGW Management page, select the cluster that you want to
view from the **Cluster** drop-down list. Then, view the cluster information in the **Node**
**Information** and **Aggregated Traffic** sections.
5. View the cluster information in the **Node Information** section.
View node information in the following columns: **Hostname**, **IDC**, **IP**, and **State**. Find the node whose details you want to view and click **Details** in the **Operation** column. In the panel that appears, view the usage of the node by metric. For more information about the metrics, see the table in the following step.
6. In the **Aggregated Traffic** section, view the usage of the device nodes by metric. The
following table describes the metrics.

> **Note:** The range between the start time and end time cannot exceed 24 hours.
> You can select **Last1Hour**, **Last3Hours**, **Last6Hours**, or **Last1Day** to query the usage data within the selected time range.
> You can move the pointer over a point in time in a chart to view the values of the corresponding metrics.

| Section | Metric | Description |
|---|---|---|
| ByteRate | InByteRate | The inbound bandwidth. Unit: bit/s. |
|   | OutByteRate | The outbound bandwidth. Unit: bit/s. |
| PacketLossRate | PacketLossRateIn | The number of inbound packets dropped per second. Unit: packets per second (PPS). |
|   | PacketLossRateOut | The number of outbound packets dropped per second. Unit: PPS. |
| PacketRate | PacketRateIn | The number of inbound packets per second. Unit: PPS. |
|   | PacketRateOut | The number of outbound packets per second. Unit: PPS. |

##### 2.1.3.5 CEN O&M

> **Note:** By default, the CEN O&M module is not displayed. To use this module, perform the following operations: Log on to the Apsara Uni-manager Operations Console. In the top navigation bar, click **User Authorities**. In the left-side navigation pane, click **Menu** **Management**. On the Menu management page, modify the menu settings to display the CEN O&M module.

###### 2.1.3.5.1 CEN-TR cluster management

VM instances that run on physical machines have their own IP addresses, and can access the Internet and host applications.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
3. In the left-side navigation pane, choose **Network Products** > **CEN O&M** > **CEN-TR**
**Clusters**.
4. On the page that appears, select a cluster from the drop-down list. Then, the corresponding
node information is displayed below, including the node IP, hostname, and status.
5. Click **Details** in the **Operation** column of a node. On the node details page, view the
monitoring data of the node within a specific period of time, including the traffic, CPU utilization, and memory usage. The following table describes the key monitoring metrics.

| Section |   | Metric | Description |
|---|---|---|---|
| Traffic | Flow | multicast rx bps _ _ | The rate of inbound multicast data that is transmitted to the transit router node. Unit: bit/s. |
|   |   | multicast target tx bps _ _ _ | The expected rate of outbound multicast data that is transmitted from the transit router node. Unit: bit/s. |
|   |   | multicast tx bps _ _ | The rate of outbound multicast data that is transmitted from the transit router node. Unit: bit/s. |
|   |   | rx bps _ | The rate of inbound data that is transmitted to the transit router node. Unit: bit/s. |
|   |   | tx bps _ | The rate of outbound data that is transmitted from the transit router node. Unit: bit/s. |
|   |   | multicast rx pps _ _ | The number of inbound multicast packets that are sent to the transit router node per second. |
|   |   | multicast tx pps _ _ | The number of outbound multicast packets that are sent from the transit router node per second. |

|   | BandWidth |   |   |
|---|---|---|---|
|   |   | multicast target tx pps _ _ _ | The expected number of outbound multicast packets that are sent from the transit router node per second. |
|   |   | rx drop pps _ _ | The number of dropped inbound packets that are sent to the transit router node per second. |
|   |   | tx drop pps _ _ | The number of dropped outbound packets that are sent from the transit router node per second. |
|   |   | tx pps _ | The number of outbound packets that are sent from the transit router node per second. |
|   |   | rx pps _ | The number of inbound packets that are sent to the transit router node per second. |
| CPU utilization |   | cpu util _ | The CPU utilization, in percentage. |
| Memory usage |   | mem util _ | The memory usage, in percentage. |

###### 2.1.3.5.2 CEN workflows

On the CEN Workflows page, you can view the workflow event details and relevant information of a Cloud Enterprise Network (CEN) instance.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
3. In the left-side navigation pane, choose **Network Products** > **CEN O&M** > **CEN**
**Workflows**.
4. On the page that appears, select a value from the **Business Foundation System Type**
drop-down list, enter an event ID in the **Event ID** field, and then click **Search**.
5. View the event details in the **Basic Information** and **Procedure Details** sections.
6. In the **Procedure Details** section, find the step that you want to view and click **Details** in
the **StepMessage** column.

**What to do next**

| Operation | Procedure |
|---|---|
| Terminate a workflow | 1. In the Basic Information section, click Terminate. 2. In the message that appears, click OK. |
| Re-push a workflow | 1. In the Basic Information section, click Re-push. 2. In the message that appears, click OK. |
| Roll back a workflow. | 1. In the Basic Information section, click Roll Back. 2. In the message that appears, click OK. |
| Jump a workflow | 1. In the Basic Information section, click Jump. 2. In the dialog box that appears, configure the Select Jump Method and Steps to Jump parameters. Select Jump Method: The jump method. Valid values:P revious Step, Next, and Specify Steps. Steps to Jump: The number of steps to jump. This parameter takes effect only if you set the Select Jump Method parameter to Specify Steps. 3. Click OK. |

##### 2.1.3.6 AVS O&M

###### 2.1.3.6.1 AVS management

The Apsara virtual switch (AVS) management feature allows you to view the basic information and usage dashboard of AVSes.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
3. In the left-side navigation pane, choose **Network Products** > **AVS O&M** > **AVS**
**Management**.
4. On the AVS management page, you can view the ASV information in the following columns:
**Hostname**, **NC IP**, **Kernel version**, **pync version**, **rpm version**, **Version mvssSDK**, and
**vtools version**.
5. Find the AVS that you want to manage and click **Details** in the **Operation** column. On the
page that appears, view the monitoring data in the **netdev traffic**, **CPU usage**, **Total**
**vport traffic**, **vxlanVport total traffic**, and **Physical Nic traffic** sections.
The following table describes the metrics.

| Category |   | Metric | Description |
|---|---|---|---|
| netdev traffic | Flow | if ipackets sum _ _ | The number of packets that the network interface controller (NIC) receives per second. |
|   |   | if opackets sum _ _ | The number of packets that the NIC sends per second. |
|   |   | if idrop sum _ _ | The number of NIC inbound packets that are dropped per second. |
|   |   | if odrop sum _ _ | The number of NIC outbound packets that are dropped per second. |
|   | BandWidth | if ibytes sum _ _ | The number of bytes that the NIC receives per second. |
| 6 |   | > Document Version: 2025110 |   |

|   | r Operations |   |   |
|---|---|---|---|
|   |   | if obytes sum _ _ | The number of bytes that the NIC sends per second. |
| CPU usage |   | usage avg _ | The average CPU utilization. |
|   |   | usage min _ | The minimum CPU utilization. |
|   |   | usage max _ | The maximum CPU utilization. |
|   | Flow | rx packets sum _ _ | The number of inbound packets per second. |
|   |   | rx dropped sum _ _ | The number of inbound packets that are dropped per second. |
|   |   | tx packets sum _ _ | The number of outbound packets per second. |
|   |   | tx dropped sum _ _ | The number of outbound packets that are dropped per second. |
|   |   | slb tx packets sum _ _ _ | The number of packets that Server Load Balancer (SLB) sends per second. |
|   |   | slb tx dropped sum _ _ _ | The number of SLB outbound packets that are dropped per second. |
|   |   | slb rx packets sum _ _ _ | The number of packets that SLB receives per second. |
|   |   | slb rx dropped sum _ _ _ | The number of SLB inbound packets that are dropped per second. |
|   |   | rx pps limit error sum _ _ _ _ | The number of inbound packets that are dropped due to throttling per second. |

|   |   | tx pps limit error sum _ _ _ _ | The number of outbound packets that are dropped due to throttling per second. |
|---|---|---|---|
|   |   | rx acl error sum _ _ _ | The number of inbound packets that are dropped from the security group per second. |
|   |   | tx acl error sum _ _ _ | The number of outbound packets that are dropped from the security group per second. |
|   |   | ipv6 tx packets sum _ _ _ | The number of packets that IPv6 clients send per second. |
|   |   | ipv6 tx acl error sum _ _ _ _ | The number of IPv6 outbound packets that are dropped from the security group per second. |
|   |   | ipv6 rx packets sum _ _ _ | The number of packets that IPv6 clients receive per second. |
|   |   | ipv6 rx acl error sum _ _ _ _ | The number of IPv6 inbound packets that are dropped from the security group per second. |
|   | BandWidth | rx bytes sum _ _ | The number of bytes that are received per second. |
|   |   | rx dropped bytes sum _ _ _ | The number of bytes of inbound packets that are dropped per second. |
|   |   | tx bytes sum _ _ | The number of bytes that are sent per second. |
|   |   | tx dropped bytes sum _ _ _ | The number of bytes of outbound packets that are dropped per second. |
|   |   | slb tx bytes sum _ _ _ | The number of bytes that SLB sends per second. |

| Total vport traffic |   |   |   |
|---|---|---|---|
|   |   | slb tx dropped bytes sum _ _ _ _ | The number of bytes of SLB outbound packets that are dropped per second. |
|   |   | slb rx bytes sum _ _ _ | The number of bytes that SLB receives per second. |
|   |   | slb rx dropped bytes sum _ _ _ _ | The number of bytes of SLB inbound packets that are dropped per second. |
|   |   | ipv6 tx bytes sum _ _ _ | The number of bytes that IPv6 clients send per second. |
|   |   | ipv6 rx bytes sum _ _ _ | The number of bytes that IPv6 clients receive per second. |
|   | NorthSouthFlow | tx igw packets avg _ _ _ | The number of packets that are sent per second in the north-south traffic. |
|   |   | rx igw packets avg _ _ _ | The number of packets that are received per second in the north-south traffic. |
|   |   | ipv6 tx igw packets avg _ _ _ _ | The number of packets that IPv6 clients send per second in the north-south traffic. |
|   |   | ipv6 rx igw packets avg _ _ _ _ | The number of packets that IPv6 clients receive per second in the north-south traffic. |
|   | NorthSouthBandWi dth | tx igw bytes avg _ _ _ | The number of bytes that are sent per second in the north- south traffic. |
|   |   | rx igw bytes avg _ _ _ | The number of bytes that are received per second in the north-south traffic. |
|   |   | ipv6 tx igw bytes avg _ _ _ _ | The number of bytes that IPv6 clients send per second in the north-south traffic. |
|   | n: 20251107 |   |   |

|   |   | ipv6 rx igw bytes avg _ _ _ _ | The number of bytes that IPv6 clients receive per second in the north-south traffic. |
|---|---|---|---|
|   | Connect | session count sum _ _ | The total number of fast forwarding connections. |
|   |   | slb session count sum _ _ _ | The number of SLB connections. |
|   |   | noconn flows num sum _ _ _ | The number of User Datagram Protocol (UDP) and Internet Control Message Protocol (ICMP) connections. |
|   |   | tcp connecting flows num _ _ _ sum _ | The number of new connections. |
|   |   | tcp established flows num _ _ _ sum _ | The number of concurrent connections. |
|   |   | tcp closing flows num su _ _ _ _ m | The number of connections that are being closed. |
|   |   | tcp closed flows num sum _ _ _ _ | The number of closed connections. |
|   |   | rx session new fail sum _ _ _ _ | The number of inbound connections that fail to be created. |
|   |   | rx session update fail sum _ _ _ _ | The number of inbound connections that fail to be updated. |
|   |   | tx session new fail sum _ _ _ _ | The number of outbound connections that fail to be created. |
|   |   | tx session update fail sum _ _ _ _ | The number of outbound connections that fail to be updated. |

|   | RetransmissionRat e | tx retrans avg _ _ | The ratio of the number of re-sent outbound packets to the total number of outbound packets. |
|---|---|---|---|
|   |   | rx retrans avg _ _ | The ratio of the number of re-sent inbound packets to the total number of inbound packets. |
|   |   | tx igw retrans avg _ _ _ | The ratio of the number of re-sent outbound packets to the total number of outbound packets in the north-south traffic. |
|   |   | rx igw retrans avg _ _ _ | The ratio of the number of re-sent inbound packets to the total number of inbound packets in the north-south traffic. |
|   |   | ipv6 rx retrans avg _ _ _ | The ratio of the number of re-sent IPv6 outbound packets to the total number of IPv6 outbound packets. |
|   |   | ipv6 tx retrans avg _ _ _ | The ratio of the number of re-sent IPv6 inbound packets to the total number of IPv6 inbound packets. |
|   |   | ipv6 tx igw retrans avg _ _ _ _ | The ratio of the number of re-sent IPv6 outbound packets to the total number of IPv6 outbound packets in the north-south traffic. |
|   |   | ipv6 rx igw retrans avg _ _ _ _ | The ratio of the number of re-sent IPv6 inbound packets to the total number of IPv6 inbound packets in the north- south traffic. |
|   |   | rx packets avg _ _ | The number of inbound packets per second. |

| tform Operation e Operations Gui ations | and Maintena de·Network o | Apsara Uni-manager Operations Consol |   |
|---|---|---|---|
| vxlanVport total traffic | Flow |   |   |
|   |   | tx packets avg _ _ | The number of outbound packets per second. |
|   |   | rx dropped avg _ _ | The number of inbound packets that are dropped per second. |
|   |   | tx dropped avg _ _ | The number of outbound packets that are dropped per second. |
|   |   | rx pps limit error avg _ _ _ _ | The number of inbound packets that are dropped due to packets per second (PPS) throttling per second. |
|   |   | rx fastpath error avg _ _ _ | The number of inbound packets that are dropped due to fast forwarding per second. |
|   |   | tx pps limit error avg _ _ _ _ | The number of outbound packets that are dropped due to PPS throttling per second. |
|   |   | tx fastpath error avg _ _ _ | The number of outbound packets that are dropped due to fast forwarding per second. |
|   |   | rx cpu limit error avg _ _ _ _ | The number of inbound packets that are dropped due to CPU throttling per second. |
|   |   | tx cpu limit error avg _ _ _ _ | The number of outbound packets that are dropped due to CPU throttling per second. |
|   |   | relay packet err avg _ _ _ | The number of packets that encounter relay errors. |
|   |   | relay packet avg _ _ | The number of packets that are relayed. |

|   |   | rx loc route error avg _ _ _ _ | The number of inbound location table match errors per second. |
|---|---|---|---|
|   |   | ipv6 rx loc error avg _ _ _ _ | The number of inbound IPv6 location table match errors per second. |
|   | BandWidth | rx bps limit error avg _ _ _ _ | The number of inbound packets that are dropped due to bytes per second (BPS) throttling per second. |
|   |   | tx bps limit error avg _ _ _ _ | The number of outbound packets that are dropped due to BPS throttling per second. |
|   |   | rx bytes avg _ _ | The number of bytes that are received per second. |
|   |   | rx dropped bytes avg _ _ _ | The number of bytes of inbound packets that are dropped per second. |
|   |   | tx bytes avg _ _ | The number of bytes that are sent per second. |
|   |   | tx dropped bytes avg _ _ _ | The number of bytes of outbound packets that are dropped per second. |
|   |   | rx drop packets avg _ _ _ | The number of inbound packets that are dropped per second. |
|   |   | rx error packets avg _ _ _ | The number of error inbound packets per second. |
|   |   | rx missed errors avg _ _ _ | The number of inbound packets that are dropped in the buffer per second. |
| Physical Nic traffic | Flow | rx packets avg _ _ | The number of inbound packets per second. |

|   |   | tx error packets avg _ _ _ | The number of error outbound packets per second. |
|---|---|---|---|
|   |   | tx packets avg _ _ | The number of outbound packets per second. |
|   | BandWidth | rx bytes avg _ _ | The number of bytes that are received per second. |
|   |   | tx bytes avg _ _ | The number of bytes that are sent per second. |

##### 2.1.3.7 VPC-On-ECS

1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
3. In the left-side navigation pane, choose **Network Products** > **VPC-On-ECS**.
4. On the VPC-On-ECS page, click **Advanced Filter** and then specify the **VPC ID**, **Status**, and
**Created At** parameters to filter virtual private clouds (VPCs).
5. Find a VPC that you want to manage and click its name or **Details** in the **Operation**
column. On the details page of the VPC, you can view the VPC details in the **VPC Instance**
**Information**, **VRouter Information**, and **vSwitches** sections.
6. In the **vSwitches** section, perform the following operations:
Create a vSwitch: Click **Create vSwitch**. In the dialog box that appears, configure the following parameters and click **OK**.

| Parameter | Description |
|---|---|
| AZone | The ID of the zone to which the vSwitch belongs. |
| CIDR | The IPv4 CIDR block of the vSwitch. |
| Usage | The purpose of the vSwitch. Valid values: Alibaba Cloud Service Container Network |
| Description | The description of the vSwitch. |

Search for vSwitches: Click **Advanced Filter** and then specify the **Instance ID**, **Owner**,
**AZone**, and **Created At** parameters to filter vSwitches.
Delete a vSwitch: Find a vSwitch that you want to delete and click **Delete** in the
**Operation** column. In the dialog box that appears, click **OK**.

> **Important:** After you delete a vSwitch, the vSwitch cannot be restored. Proceed with caution.

#### 2.1.4 Network monitoring and alerting

##### 2.1.4.1 Network alert dashboard

The Network Alert Dashboard module displays the alert information of all network components on the platform.

**Prerequisites**

The NetworkBaseServiceCluster cluster for BaseServiceAll has been deployed and has reached the desired state.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
3. In the left-side navigation pane, choose **Network Monitoring & Alerting** > **Network**
**Alert Dashboard**.
4. On the **Current Alerts** tab, view the alerts of all network components on the platform. You
can search for alerts by **device name**, **device IP address**, or **alert rule name**.
5. Click **Details** in the **Alert Details** column of an alert to view detailed information about the
alert.
6. Find the reason why an alert is triggered and then handle the alert.
If you have confirmed that the alert does not affect the operation of the system, click
**Ignore** in the **Operation** column. In the message that appears, click **OK** to ignore the
alert. If you have confirmed that the alert is meaningless, click **Delete** in the **Operation** column. In the message that appears, click **OK** to delete the alert. After the alert is handled, you can query it on the **Alert History** tab. Click **View** in the
**Alert Details** column of the alert to view detailed information about the alert.

**What to do next**

| Operation | Procedure |
|---|---|
| Export alert information | 1. Click Export Table. 2. In the message that appears, click OK to export the alert information to your local device. |

| Delete all alerts | 1. Click Delete All. 2. In the message that appears, click OK to delete all alerts. |
|---|---|

##### 2.1.4.2 Network alert settings

###### 2.1.4.2.1 Monitoring rule management

You can associate the monitoring metrics of a monitored instance with an alert template. When the value of a metric meets the conditions specified in the alert template, an alert event is triggered.

**Prerequisites**

The NetworkBaseServiceCluster cluster for BaseServiceAll has been deployed and has reached the desired state. An alert template is created.

**Limits**

Monitoring rules can be configured only for the interface monitoring metrics of physical network devices.

**Create an monitoring rule**

1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
3. In the left-side navigation pane, choose **Network Monitoring & Alerting** > **Network**
**Alert Settings** > **Monitoring Rules**.
4. Click **Create a monitoring rule**. On the page that appears, complete all configurations in
the following steps as prompted: i. Basic rule configuration In this step, configure the following parameters and click **Next**.

| Section | Parameter | Description |
|---|---|---|
| Basic configuration | Name | The name of the monitoring rule. |
|   | Metric category | The category of the metric that you want to monitor. Valid values: ApsaraNetwork NetworkDevice |
|   | Metric type | The type of the metric that you want to monitor. |
|   | Metric Group | The metric group. |
|   | Metric | The name of the metric that you want to monitor. |
| Monitoring node configuration | Product cluster | The cluster to which the monitoring node belongs. |
|   | IDC | The data center to which the monitoring node belongs. |
|   | Manufacturer | The manufacturer of the monitoring node. |
|   | Monitoring node | The monitoring node. |
|   | Monitoring instance | The monitored instance. |
|   | Enabled | Specifies whether to enable the monitoring node. |

ii. Associate an alert template In this step, select the alert template that you want to associate with the metric and click
**Next**.
iii. Confirm information In this step, confirm the parameters that you configured. If you want to modify parameters, click **Previous step**. If you confirm that the parameters are configured as expected, click **Create** to create the monitoring rule.

> **Note:** By default, the newly created monitoring rule is enabled.

**What to do next**

**View monitoring rules**

1. On the **Monitoring Rules** page, you can view the details of monitoring rules in the
following columns: **Monitoring Rule name**, **Monitoring node**, **Monitoring category**,
**Monitoring type**, **Metric**, **Monitoring instance**, **Associate an alert template**,
**Enabled**, and **Created**.
2. Find the monitoring rule that you want to view and click its name in the **Monitoring Rule**
**name** column. On the **Monitoring Rule details** page, view the configuration information
and associated alert template of the monitoring rule.
3. Find the monitoring rule that you want to view and click the value in the **Associate an**
**alert template** column. In the panel that appears, view the information about the
associated alert template.

**Enable a monitoring rule**

1. Find the monitoring rule that you want to enable and click **Enable** in the **Operation**
column.

> **Note:** Only the monitoring rules whose value in the **Enabled** column is **Disabled** can be enabled.

2. In the message that appears, click **OK**.

**Disable a monitoring rule**

1. Find the monitoring rule that you want to disable and click **Disabled** in the **Operation**
column.

> **Note:** Only the monitoring rules whose value in the **Enabled** column is **Enable** can be disabled.

2. In the message that appears, click **OK**.

**Delete a monitoring rule**

1. Find the monitoring rule that you want to delete and click **Delete** in the **Operation** column.
2. In the message that appears, click **Delete**.

###### 2.1.4.2.2 Alert template management

The alert conditions for monitoring metrics are configured in alert templates. When the monitoring metrics meet the specified alert conditions, alert notifications or message suppression actions are performed based on the configured alert rule or the suppression rule.

**Prerequisites**

The NetworkBaseServiceCluster cluster for BaseServiceAll has been deployed and has reached the desired state.

**Limits**

Alert templates can be created only for the monitoring metrics of physical network device interfaces.

**Create an alert template**

1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
3. In the left-side navigation pane, choose **Network Monitoring & Alerting** > **Network**
**Alert Settings** > **Alert Templates**.
4. On the Alert Templates page, click **Create an alert template**. In the dialog box that
appears, configure the parameters and click **OK**. The following table describes the parameters.

| Section | Parameter | Description |
|---|---|---|
| Basic configuration | Alert rule name | The name of the alert template. The name is globally unique. |
|   | Metric category | The level-1 category of the metric. |
|   | Metric type | The metric type. |
|   | Metric Group | The metric group. |
|   | Metric | The metric name. |
| Decision Rules | Aggregate Functions | The function that is used to calculate the metric value. |
|   | Expression | The operator used to compare the metric value with the threshold value. |
|   | Alert value | The threshold value. |
|   | Duration (Times) | The number of times that the metric value reaches thespecified threshold value before an alert notification is sent. Default value: 1. |
|   | Minimum alert interval (Times) | The minimum interval between two consecutive alert notifications. |

| tform Operation and M e Operations Guide·Ne ations |   |   |
|---|---|---|
| Alert settings |   |   |
|   | Maximum number of notifications | The maximum number of notifications that can be sent for an alert. Default value: 1000. |
|   | Alert level | The level of the alert. Valid values: P1 P2 P3 P4 |
|   | Rule description | The description of the alert template. |
|   | Enabled | Specifies whether to enable the alert template. |

> **Note:** After an alert template is created, it is enabled by default.

**What to do next**

**View alert templates**

1. On the **Alert Templates** page, you can view the alert template information in the following
columns: **Alert Template name**, **Monitoring category**, **Monitoring type**, **Metric**,
**Enabled**, and **Created**.
2. Find the alert template that you want to view and click its name. In the **Alert template**
**details** panel, you can view the details of the alert template.

**Enable an alert template**

1. Find the alert template that you want to enable and click **Enable** in the **Operation** column.

> **Note:** Only disabled alert templates can be enabled.

2. In the message that appears, click **OK**.

**Disable an alert template**

1. Find the alert template that you want to disable and click **Disabled** in the **Operation**
column.

> **Note:** Only enabled alert templates can be disabled.

2. In the message that appears, click **OK**.

**Delete an alert template**

1. Find the alert template that you want to delete and click **Delete** in the **Operation** column.
2. In the message that appears, click **Delete**.

###### 2.1.4.2.3 Trap template settings

This topic describes how to configure and manage trap alert rules of network devices. If the initially configured trap subscriptions do not meet the monitoring requirements, you can add a trap to enhance monitoring coverage.

**Prerequisites**

The NetworkBaseServiceCluster cluster for BaseServiceAll is deployed and at desired state.

**Background information**

Simple Network Management Protocol (SNMP) traps are used in this topic. SNMP trap is a part of SNMP and is a mechanism that enables the managed network devices, such as vSwitches and vRouters, to send SNMP messages to the Network Operation Center (NOC) monitoring server. If an exception occurs on the device being monitored or the vSwitch metrics have an exception, the SNMP agent that is running in the vSwitch sends an alert event to the NOC monitoring server.

**Add a trap**

1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
3. In the left-side navigation pane, choose **Network Monitoring & Alerting** > **Network**
**Alert Settings** > **Trap Template Setting**.
4. On the Trap Template Setting page, click **Create Trap**. In the Create Trap dialog box,
configure the parameters that are described in the following table.

| Parameter | Description | Example |
|---|---|---|
| Trap Name | The name of the alert event. | linkdown or BGPneighbor down. You can customize the value. |
| Trap OID | The object identifier (OID) of the alert event. | .1.3.6.1.4.1.25506.8.35.12.1.12 The value must be configured based on the device document and cannot be customized. |
| Trap Type | The type of the alert event. Valid values: Operation Hardware Protocol Others | N/A |

| Trap Index | The index ID of the alert item. The key-value pair in trap messages, which is used to identify alert objects. Typically, the value of this parameter can be an API name, a protocol ID, or an index ID. You can specify multiple values for this parameter. | The value must be configured based on the device document and cannot be customized. |
|---|---|---|
| Trap Msg | The message of the alert item. The key-value pair in trap messages, which is used to identify the alert data. Typically, the value of this parameter can be the additional information about the alert item, such as a message about the location of the state machine, a message about the current status, or a system message. You can specify multiple values for this parameter. | The value must be configured based on the device document and cannot be customized. |
| Alert Type | The type of the alert. Valid values: Fault Restore | N/A |
| Alert Association | Specifies whether the alert has a corresponding recovery alert. Note If you select Recovered, you must configure the settings of the associated alert trap. | N/A |

5. Click **OK**. After the configurations are submitted, the system checks whether the values of
the Trap OID and Trap Name parameters are unique. If yes, the trap is added. After the trap is added, the alert events of the configured Trap OID are monitored and are displayed on the **Current Alerts** and **Alert History** tabs of **Network Alert Dashboard**.

**What to do next**

**View the alert details of a trap**

1. On the Trap Template Setting page, view the following information about traps: **Trap**
**Name**, **Trap OID**, **Trap Type**, **Recovery Alert**, **Alert Type**, and **Alert Details**.
2. Select **By Name**, **By OID**, or **Type** from the Query Type drop-down list to query a trap.
3. Find the trap that you want to view and move the pointer over **Details** in the **Alert Details**
column to view the alert details of the trap.

**Export trap information**

On the Trap Template Setting page, click **Export Table** to export all trap information to your on-premises machine. In the message that appears, click OK.

**Delete a trap**

1. Find the trap that you want to delete and click **Delete** in the **Operation** column.
2. In the message that appears, click **OK**.

#### 2.1.5 Intelligent diagnostics

##### 2.1.5.1 Network inspection

The network inspection feature allows you to schedule network inspection tasks on a regular basis and convert inspection results into inspection events or alerts.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
3. In the left-side navigation pane, choose **Intelligent Diagnostics** > **Network Inspection**.
4. On the Network Inspection page, view the information about inspection configurations in
the following columns: **Name**, **Description**, **Execution Cycle**, **Status**, **Number of**
**Executions**, **Product**, **Service**, and **Role**.
You can click **Advanced Filter** and filter inspection configurations by **Name**, **Product**,
**Service**, **Role**, Status, or their combinations.

> **Note:** Click the up and down arrow icon next to **Number of Executions** to sort data in ascending or descending order.

5. Find the inspection configuration that you want to view and click **View Details** in the
**Operation** column. In the panel that appears, view the details of the inspection
configuration on the **Execution Information** and **Related Events** tabs. On the **Execution Information** tab, view the information in the **Basic Information** and
**Execution Information** sections. In the **Execution Information** section, you can
perform the following operations: Filter tasks by **Task ID**, **Status**, **Operation Time**, or their combinations. Find the task that you want to view, and move the pointer over the value in the **The**
**execution status** column or **Execution Parameters** and **Additional Information** in
the **Operation** column to view the execution result, execution parameters, and additional information of the task.

> **Note:** Description of execution states:
> waiting: The inspection task is waiting to be triggered.
> running: The inspection task is running.
> success: The inspection task is successfully executed.
> failed: The inspection task failed to be executed.
> timeout: The inspection task timed out.
> cleaned: The inspection task is deleted when the cloud platform is initialized.

On the **Related Events** tab, view the related events. View the event information in the following columns: **Event Name**, **Event**
**Description**, **Associated Object**, **Event Source Type**, **Event Source**, **Event**
**Timeout Period**, **Event Severity**, **Associated Alert ID**, and **Triggered At**.
Click **Advanced Filter** and filter events by **Time**, **Event Name**, **Associated Object**,
**Alert Severity**, **Event Source Type**, **Event Exception Type**, or their combinations.
Find the event that you want to view, and click **Details** in the **Actions** column to view the event details.

**What to do next**

| Operation | Procedure |
|---|---|
| Import an inspection configuration | 1. Click Import Inspection Settings. 2. Select the inspection configuration file that you want to import and click Open. |

| Enable an inspection configuration | Note You can enable only inspection configurations that are in theD isable state. 1. Find the inspection configuration that you want to enable and click Enable in the Operation column. 2. In the message that appears, click OK. |
|---|---|
| Disable an inspection configuration | Note You can disable only inspection configurations that are in the Enable state. 1. Find the inspection configuration that you want to disable and click Disable in the Operation column. 2. In the message that appears, click OK. |

##### 2.1.5.2 Intelligent path analysis

The intelligent path analysis and forwarding feature provides path diagnostics capabilities. You can use this feature to implement end-to-end path analysis by quickly establishing IP paths. This facilitates fault analysis and shortens the fault analysis time.

**Prerequisites**

The NetworkBaseServiceCluster cluster for BaseServiceAll has been deployed and has reached the desired state.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
3. In the left-side navigation pane, choose **Intelligent Diagnostics** > **Intelligent Path**
**Analysis**.
4. On the Intelligent Path Analysis page, click **Create Path Analysis**. On the page that
appears, configure the following parameters and click **Analysis**.

| Parameter | Description | Example |
|---|---|---|

| Scenario | The scenario of path analysis. Valid values: Mutual access between ECS instances: access between Elastic Compute Service (ECS) instances in a virtual private cloud (VPC). ECS access server load balancer: access from an ECS instance in a VPC to a Server Load Balancer (SLB) instance. ECS access AnyTunnel: access from an ECS instance in a VPC to an AnyTunnel virtual IP address (VIP). ECS access SingleTunnel: access from an ECS instance in a VPC to a SingleTunnel VIP. ECS access IDC: access between an ECS instance in a VPC and a data center. ECS access to the Internet: access from an ECS instance in a VPC to the Internet. Exchange of space-based containers: access between Docker containers in a cloud platform. Apsara infrastructure management framework container access load balancing: access from a Docker container to an SLB instance in a cloud platform. Apsara infrastructure management framework container access NC: access from a Docker container to a physical machine in a cloud platform. NC Mutual visits: access between physical machines in a cloud platform. NC access Apsara infrastructure management framework container: access from a physical machine to a Docker container in a cloud platform. NC access load balancing: access from a physical machine to an SLB instance in a cloud platform. | Mutual access between ECS instances |
|---|---|---|
| Physical link analysis | Specify whether to enable or disable the physical link analysis feature. If you enable this feature, you must deliver the configuration to vSwitches. In this case, the analysis time is extended. If you disable this feature, the analysis time is shortened. However, the packet capture data of the physical devices is not contained. | N/A |
| Source IP address | The IP address of the source node. IPv4 and IPv6 addresses are supported. | 192.168.1.1 and FE80::/10 |
| Destination IP address | The IP address of the destination node. IPv4 and IPv6 addresses are supported. | 192.168.1.1 and FE80::/10 |

| Detection Protocol | The protocol type of probe packets for the path analysis. Valid values: TCP UDP ICMP | TCP |
|---|---|---|
| SOURCE Port | The port of the source node. If you leave this parameter empty, all ports are used. | 80 |
| Destination Port | The port of the destination node. If you leave this parameter empty, all ports are used. | 8080 |
| Number of probe packets | The total number of probe packets for path analysis. | 10 |
| SOURCE VpcId | The ID of the VPC in which the source node resides. | vpc- **fczvaczv |
| Destination VpcId | The ID of the VPC in which the destination node resides. | vpc- **fczvaczv |
| Timeout period | The timeout period of the packet capture in the analysis task. If this period is exceeded, the packet capture stops. Unit: minutes. | 5 |

5. In the **Path analysis** section, the status timeline of the analysis task is displayed, and the
estimated time required for each phase is displayed. The topology of the path is displayed at the bottom of the timeline. After the analysis is complete, the analysis result is displayed.

> **Note:** For path nodes of the ECS type or physical machine type, you can click the hyperlink in the topology to go to the details page.
> After you select the topology, you can drag the topology and change the location of the topology.

6. In the **Diagnosis details** section, the details of the task are displayed.
7. In the **Analyze one by one** section, the analysis details of the packets captured by the
task are displayed if the analysis task is successful. You can view the analysis details of packets one by one.

**What to do next**

| Operation | Procedure |
|---|---|
| View the details of an analysis task | 1. On the Intelligent Path Analysis page, select a time range to view the information about the intelligent path analysis tasks within the specified time range. 2. Find the analysis task that you want to view and clickD etails in the Operation column. You can view the analysis results, including the path analysis, diagnostic details, and analysis details of each packet. |
| Terminate an analysis task | On the Intelligent Path Analysis page, find the analysis task that you want to terminate and click Terminate in the Operation column. Note You cannot terminate an analysis task that is in theC ompleted state. |

##### 2.1.5.3 Network instance diagnostics

The network instance diagnostics feature allows you to analyze the status of network instances with a few clicks.

**Scenarios**

The network instance diagnostics feature helps you quickly analyze a network instance to identify whether it has an unexpected state. This feature provides visualized and automated diagnostics capabilities and can improve the O&M efficiency of network O&M engineers, reduce O&M risks, and improve the quality of virtual private cloud (VPC) O&M.

**Limits**

The NetworkBaseServiceCluster cluster for BaseServiceAll has been deployed and has reached the desired state. After a diagnostic task is started, it does not stop until the diagnosis is complete. You cannot pause or terminate the task.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
3. In the left-side navigation pane, choose **Intelligent Diagnostics** > **Network Instance**
**Diagnosis**.
4. In the **One-click analysis of the running status of network instances** section, select
the service whose instance you want to diagnose, enter the ID of the instance, and then click **Diagnose now**. You can select one of the following values: SLB DNS Elastic IP Address Virtual Board Router Physical Connection NAT Gateway DCI Connection External Connection
5. The Network instance diagnosis results page appears. On this page, view the information in
the **Instance details**, **Instance topology**, and **Diagnosis details** sections.

> **Note:** The **Instance details** section is displayed only when you select SLB in the previous step.
> In the field at the top of the Network instance diagnosis results page, the ID of the diagnosed instance is displayed by default. You can also enter the ID of another instance and click **Diagnose now** to perform diagnostics.

In this example, an Server Load Balancer (SLB) instance is diagnosed and its diagnostic results are described. Instance details: Instance topology: In the topology example shown in the preceding figure, the leftmost column displays the SLB instance, the middle column displays the listeners of the SLB instance, and the rightmost column displays the backend servers that correspond to the listeners. If a backend server is of the ECS type or the machine type of Apsara Infrastructure Management, click realServer in the topology. A panel appears to show the server details. After you select the topology, you can drag the topology to change the location of the topology. Diagnosis details: This section displays the information about diagnostic items in the following columns: **Diagnostic item name**, **Description**, **Diagnostic results**, and
**Diagnosis details**.
6. You can also perform the following operations in the **Task list** section on the Network
Instance Diagnosis page to view historical diagnostic results of an instance: Specify a time range, find the diagnostic task that you want to view, and then click **Details** in the **Operation** column to go to the Network instance diagnosis results page. On this page, view the diagnostic results in the **Instance details**, **Instance topology**, and
**Diagnosis details** sections.

##### 2.1.5.4 Container network diagnostics

This topic describes the automated intelligent diagnostics capabilities for container networks based on mutual accessibility.

**Scenarios**

The container network diagnostics feature helps you quickly analyze container networks to determine whether the container networks have unexpected states. Visualized and automated diagnostics capabilities are provided. This feature can improve the O&M efficiency of network O&M engineers, reduce O&M risks, and improve the O&M quality of virtual private clouds (VPCs).
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
3. In the left-side navigation pane, choose **Intelligent Diagnostics** > **Diagnose Container**
**Network**.
4. On the Container Network Diagnostics page, click **Create Diagnosis Task**. On the page
that appears, configure the parameters that are described in the following table and click
**Submit**.

| Parameter | Description |
|---|---|
| Source IP Address | The source IP address. |
| Destination Node Information | The information about the destination node. Select Destination IP Address or Destination Domain and enter the corresponding information. |
| Destination Port | The number of the destination port. |
| Protocol | The type of the protocol. Valid values: tcp udp |
| Enable Global Check | Specifies whether to enable the global check. After you turn on Enable Global Check, no topology information is displayed. |

5. After the diagnostic task is complete, view the path analysis topology and diagnostic report
in the lower part of the page.

**What to do next**

| Operation | Procedure |
|---|---|
| View the details of a diagnostic task | 1. On the Container Network Diagnostics page, find the diagnostic task that you want to view and click Details in the Operation column. 2. On the Diagnose Container Network page, view the details of the diagnostic task, including the path analysis topology and diagnostic report. |
| Terminate a diagnostic task | You can terminate a diagnostic task only when it is in the Running state. 1. On the Container Network Diagnostics page, find the diagnostic task that you want to terminate and click Terminate in the Operation column. 2. In the message that appears, click OK. |

##### 2.1.5.5 Network health assessment

The Network Health Assessment module evaluates and diagnoses the health status of each layer of the network based on the dimensions such as performance, capacity, function, and status. This module provides an overview of the network health status and detects issues and risks at all layers of the network in real time to ensure that the network runs as expected.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
3. In the left-side navigation pane, choose **Intelligent Diagnostics** > **Network Health**
**Assessment**.
4. On the Network Health Assessment page, view the health assessment status of different
network layers in the Health overview list.

| Evaluation layer | Description | Dimension |
|---|---|---|
| Network service instance | The Network Health Assessment module detects the access and configuration issues of a network service instance at the earliest opportunity by checking the features and configurations of the network service instance. | Function health assessment score, numbers of normal diagnostics items and total diagnostics items, and overall score of this layer in percentage |
| Overlay network layer | The Network Health Assessment module comprehensively evaluates the health status of services such as eXtreme Global Workspace (XGW), Apsara Virtual Switch (AVS), Content Switched Network (CSW), Converged Gateway (CGW), Smart Network Appliance (SNA), and Hybrid Switch (HSW) by checking the monitoring results of the physical servers, network element nodes, and packet loss of the services. | Status health assessment score, numbers of normal diagnostics items and total diagnostics items, and overall score of this layer in percentage |
| Network service controller | The Network Health Assessment module checks the alerts on the control planes of services such as Virtual Private Cloud (VPC), Server Load Balancer (SLB), DNS, and NSP and identifies issues at the earliest opportunity by checking the monitoring data of the services. | Status health assessment score, numbers of normal diagnostics items and total diagnostics items, and overall score of this layer in percentage |
| Physical device layer | The Network Health Assessment module evaluates the health status of devices by monitoring the core metrics of the devices. | Performance health assessment score, capacity health assessment score, status health assessment score, numbers of normal diagnostics items and total diagnostics items, and overall score of this layer in percentage. |
| Protocol layer | The Network Health Assessment module checks the status of routing protocols, such as Open Shortest Path First (OSPF) and Border Gateway Protocol (BGP). | Capacity health assessment score, numbers of normal diagnostics items and total diagnostics items, and overall score of this layer in percentage |

| Network layer | The Network Health Assessment module comprehensively evaluates the health status of the network layer by checking the monitoring data of interconnection status of devices, physical interface of the network, intelligent prediction of the optical module, and network interface controllers (NICs). | Performance health assessment score, status health assessment score, numbers of normal diagnostics items and total diagnostics items, and overall score of this layer in percentage |
|---|---|---|

5. In the Health overview list, find an evaluation layer whose details you want to view and
click **Details** in the Operation column to go to the **Health Details** page. i. In the **KPI details** section, click Advanced Filter. Then, configure the KPI name, Status, and Network evaluation hierarchy type parameters to filter key performance indicators (KPIs). The following table describes the information about KPIs in the list.

| Parameter | Description |
|---|---|
| KPI name | The name of the KPI at the evaluation layer. KPIs are different at different evaluation layers. |
| Hierarchy type | The dimensions based on which the layer is evaluated. The dimensions vary with different evaluation layers. Network service instance: Only the function dimension is supported. Overlay network layer: Only the status dimension is supported. Network service controller: Only the status dimension is supported. Physical device layer: Only the performance, capacity, and status dimensions are supported. Protocol layer: Only the capacity dimension is supported. Network layer: Only the performance and status dimensions are supported. |
| Status | The KPI status. Valid values: critical, abnormal, sub-health, and healthy. |
| Total number of diagnostic items | The total number of KPI items that are diagnosed. |

| Number of diagnostics items passed | The number of the KPI items that passed the diagnostics. |
|---|---|
| Number of diagnostic exceptions | The number of abnormal KPI items. You can click the number in the Number of diagnostic exceptions column to filter the abnormal events by the current KPI in the Abnormal Event section. |
| Health Assessment Score (percentile system) | The health evaluation score of the KPI. The score is calculated based on the following formula: Health evaluation score of a KPI = Number of items that passed the diagnostics/Total number of diagnostics items. |
| Update Time | The time when the KPI was last diagnosed. |

ii. In the **Abnormal Event** section, click Advanced Filter and configure the KPI name, Start time, Clear Time, Show cleared issues, Grade, Associated instance, and Event type parameters to filter abnormal events. The following table describes the information about abnormal events in the list.

| Parameter | Description |
|---|---|
| Name | The name of the abnormal event. |
| KPI name | The name of the alert event to which the abnormal event belongs. |
| Problem Description | The description of the abnormal event. |
| Associated instance | The information about the instance associated with the abnormal event. |
| Critical grade | The severity level of the abnormal event. The severity levels are listed in descending order: P1, P2, P3, P4, P5, P6, and P7. |
| Type | The type of the abnormal event. Valid values: status, function, capacity, and performance. |
| Clear Tags | Indicates whether the abnormal event is cleared. By default, No is displayed in the Clear Tags column of an abnormal event. After you click Clear in the Operation column, Yes is displayed in the Clear Tags column of the abnormal event. |
| Confirmation mark | Indicates whether the abnormal event is confirmed. By default, No is displayed in the Confirmation mark column of an abnormal event. After you click Confirm in the Operation column, Yes is displayed in the Confirmation mark column of the abnormal event. |

| Start time | The time when the abnormal event was detected. |
|---|---|
| Clear Time | The time when the abnormal event was cleared. |

a. Find the abnormal event that you want to view and click **Details** in the Operation column. In the Exception event details panel, view the details of the abnormal event. b. Click **Confirm** in the Operation column to mark the event as an abnormal event. c. Handle the abnormal event based on its name, issue description, severity level, and associated instance, and then click **Clear** in the Operation column.

> **Note:** **Clear** is displayed in the Operation column of an abnormal event only after you click **Confirm** in the Operation column of the abnormal event.

##### 2.1.5.6 Optical transceiver module diagnostics

The Optical Module Diagnostics module analyzes and predicts the status of optical transceiver modules based on AI algorithms and assists O&M personnel in troubleshooting issues.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
3. In the left-side navigation pane, choose **Intelligent Diagnostics** > **Optical Module**
**Diagnostics**.
4. In the upper part of the Optical Module Diagnostics page, view the status distribution of
optical transceiver modules on the current day and the status distribution of optical transceiver modules within a specific period of time.

> **Note:** The status of an optical transceiver module can be health, sub-health, exception, or unknown. The line chart shows the trend in the proportion of optical transceiver modules in the health state.

5. In the lower part of the Optical Module Diagnostics page, view the basic information and
analysis results of optical transceiver modules. You can click **Advanced Filter** and then filter optical transceiver modules by **optical transceiver module model**, **optical**
**transceiver module manufacturer**, **optical transceiver module status**, **hostname**,
**interface name**, and **device type**.

| Parameter | Description |
|---|---|
| Hostname | The name of the device to which the optical transceiver module belongs. |
| Interface name | The interface name of the device to which the optical transceiver module belongs. |
| Ownership Type | The type of the device to which the optical transceiver module belongs. Valid values: NETWORK SWITCH and NC. _ |
| Manufacturer | The manufacturer of the optical transceiver module. |
| Model | The model of the optical transceiver module. |
| Status | The status of the optical transceiver module. |
| Failure probability | The failure probability of the optical transceiver module. The failure probability is predicted based on the transmit power, received power, and bias current variation. |
| Expected residual life | The expected residual life of the optical transceiver module. Note The residual life is calculated based on the monitoring data and threshold of the bias current. If the bias current threshold or the real- time bias current value cannot be detected, unknown is displayed in the Expected residual life column. |
| Intelligent analysis results | The intelligent analysis result of the optical transceiver module. The analysis is performed based on the predicted failure probability and expected residual life. The following exception analysis results may be returned: The failure probability of the optical transceiver module is high. The residual life of the optical transceiver module is insufficient. The connection of the optical transceiver module is poor. |

6. Find the optical transceiver module that you want to view and click **Details** in the
Operation column. The **Optical Module Prediction Details** page appears. i. In the upper part of the page, view the basic information and prediction of the optical transceiver module. ii. In the lower part of the page, select a time range and view the metrics of the optical transceiver module, including **temperature**, **bias current**, **voltage**, **transmit power**, and **received power**.

| Metric | Description |
|---|---|
| Temperature | The temperature of an optical transceiver module affects the performance and life of the optical transceiver module. If the temperature is excessively high or low, the performance of the optical transceiver module may be damaged and the life of the optical transceiver module may be shortened. Excessively high temperature may affect the transmission distance and rate of the optical transceiver module. In addition, the performance of the light emitter and the detector may be compromised, which results in a failure of the optical transceiver module. Excessively low temperature affects the performance and life of the optical transceiver module. |
| Bias current | The bias current of an optical transceiver module is used to stimulate the laser to emit optical signals and affects the output power of the laser and the transmission distance of the optical transceiver module. Excessively large bias current may cause aging and damage of the laser and shorten the life of the optical transceiver module. Excessively small bias current may lower the output power of the laser and shorten the transmission distance. |
| Voltage | The voltage of an optical transceiver module refers to the voltage that is used to stimulate the laser to emit optical signals and the receiver to receive optical signals. If the voltage is unstable or deviates from the specified range, the optical transceiver module may fail or its performance may degrade. If the voltage is lower than expected, the transmit power of the optical transceiver module may be decreased. If the voltage is higher than expected, the optical transceiver module may fail. |
| Transmit power | The transmit power of an optical transceiver module refers to the power of the laser to emit optical signals. The transmit power of the optical transceiver module affects the transmission distance and rate of the optical transceiver module. Excessively high transmit power may damage the optical transceiver module. Excessively low transmit power may shorten the transmission distance. |
| Received power | The received power of an optical transceiver module refers to the power of the receiver to receive optical signals. The received power of the optical transceiver module affects the receiver sensitivity and transmission performance of the optical transceiver module. If the received power exceeds the specified range, issues such as signal transmission interruption, error increase, and transmission distance decrease may occur. In this case, you can monitor the received power to identify and resolve issues at the earliest opportunity. If the received power is higher than expected, you can decrease the transmit power or check the length of the jointed fiber. If the received power is lower than expected, you can increase the transmit power or check the quality of the jointed fiber. |

#### 2.1.6 Network resources

##### 2.1.6.1 Network asset management

The Network Asset Management page displays network assets in virtual private clouds (VPCs). You can query a network asset by using a property such as Asset Type, IP Address, or Instance ID.

**Prerequisites**

The NetworkBaseServiceCluster cluster for BaseServiceAll is deployed and at desired state.

**Background information**

Only some instances in VPCs are displayed on the Network Asset Management page. You can query specific instances by instance IP address or ID. Filter properties include Asset Type, IP Address, IP Address Version, Network Type, Instance ID, Zone, Product, ClusterName, Service, ServerRole, IP Address Pool ID, Base Resource, Inband Resource, and vpcId. When you query a network asset, you must specify the Product and ClusterName parameters before you specify the Service parameter. When you query a network asset, you must specify the Product, ClusterName, and Service parameters before you specify the ServiceRole parameter.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
3. In the left-side navigation pane, choose **Network Resources** > **Network Asset**
**Management**.
4. On the Network Asset Management page, click **Advanced Filter** and search for a network
asset in a VPC by **Asset Type**, **IP Address**, **IP Address Version**, **Network Type**,
**Instance ID**, **Zone**, **Product**, **ClusterName**, **Service**, **ServerRole**, **IP Address Pool ID**,
**Base Resource**, **In-band Resource**, and **vpcId**.
5. Click **Overloaded IP Data** to refresh the IP address data.
6. Find the network asset that you want to view and click **View Details** in the **Operation**
column to view the details of the network asset.

##### 2.1.6.2 IP address pool management

###### 2.1.6.2.1 IP address pools

You can view the CIDR blocks of each cloud service on the IP segment management page. You can also add CIDR blocks, query the details of CIDR blocks, or delete CIDR blocks based on your O&M requirements. The conflict check feature provides the address conflict check capability for CIDR block scaling scenarios. You can use the feature to check and analyze whether a CIDR block contains another CIDR block or is contained in another CIDR block.

**Background information**

The IP address pool feature is applicable to scenarios such as multi-cloud geo-disaster recovery and hybrid clouds. This feature allows you to perform the following operations: Multiple cloud services are deployed in a cloud instance. In O&M scenarios such as network changes and security reviews, you can obtain CIDR blocks of cloud services based on your business requirements to analyze the scope of changes and security policies. The IP address pool feature allows you to view the CIDR block of each cloud service in a cloud instance. You can also use this feature to add custom CIDR blocks.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
3. In the left-side navigation pane, choose **Network Resources** > **IP Address Pool**
**Management** > **IP Address Pools**.
On the IP segment management page, you can view the distribution of the CIDR block category, protocol, IPv4 prefixes, IPv6 prefixes, and the CIDR block list.
4. In the CIDR block list, you can search for CIDR blocks. Exact match is supported. You can
also perform the following operations. View the details of a CIDR block. Find the CIDR block that you want to view and click
**Details** in the **Operation** column. In the panel that appears, you can view the details of
the CIDR block. Add a CIDR block. Click **Manual entry**. In the panel that appears, configure the parameters and click **OK**. The following table describes the parameters.

| Parameter | Description |
|---|---|
| Network segment name | The name of the CIDR block. |
| Network Segment Information | The CIDR block. |
| Protocol Type | The protocol of the CIDR block. Valid values: IPv4 IPv6 |
| Network segment ownership | The ownership of the CIDR block. Valid values: Network equipment Cloud products Other |
| Network type Layer | The network type of the CIDR block. Valid values: Platform network Tenant Network |
| Region | The region in which the CIDR block resides. |
| Zone | The zone in which the CIDR block resides. |
| Network segment category | The type of the CIDR block. Valid values: Private network segment Public network segment Internet private use Other |
| Product Name | The name of the product to which the CIDR block belongs. |

| Cluster name | The name of the cluster to which the CIDR block belongs. |
|---|---|
| Service name | The name of the service to which the CIDR block belongs. |
| Service role | The service role to which the CIDR block belongs. |
| IDC | The data center to which the CIDR block belongs. |
| Associated network devices | The network device associated with the CIDR block. |
| Associated network interface | The port associated with the CIDR block. |
| Remarks | The description of the CIDR block. |
| Enable | Specifies whether to enable the CIDR block. |
| Expiration Time | The expiration time of the CIDR block. |

Delete a CIDR block. Find the CIDR block that you want to delete and click **Delete** in the
**Operation** column. In the message that appears, click OK.
5. Click **Conflict verification**. In the dialog box that appears, enter the CIDR block that you
want to check and click **Detection**. Then, the verification result of the CIDR block is returned.

###### 2.1.6.2.2 Collection settings

On the Collection Settings page, you can view the collection settings of the IP address pools of cloud services across the platform. You can also trigger a data update for a single IP address pool on this page.

**Background information**

The collection settings feature is applicable to scenarios such as multi-cloud geo-disaster recovery and hybrid clouds. This feature allows you to perform the following operations: View the collection rules of IP address pools of all cloud services across the cloud platform. Trigger a data update for a single IP address pool.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
3. In the left-side navigation pane, choose **Network Resources** > **IP Address Pool**
**Management** > **Collection Settings**.
4. On the Collection Settings page, find the IP address pool that you want to manage by the IP
address pool name and view the CIDR block collection settings of the IP address pool.
5. Click **Details** in the **Operation** column. In the Details panel, view the details of the IP
address pool.
6. Click **Single trigger** in the **Operation** column. In the message that appears, click **OK**.
Then, the system displays the trigger result.

##### 2.1.6.3 Reverse access

The reverse access feature implements active access from base cloud services to virtual private clouds (VPCs) by establishing NAT mappings.

**Create a reverse access instance**

1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
3. In the left-side navigation pane, choose **Network Resources** > **Reverse Access**.
4. On the Cloud Service Reverse Access page, click **Create Reverse Access Instance**. In the
dialog box that appears, configure the following parameters and click **Create Application**. After the instance is created, an application ID that is automatically assigned by the system for the instance is displayed on the Cloud Service Reverse Access page.

| Parameter | Description |
|---|---|
| Application Name | The name of the application. |
| Application Description | The description of the application. |
| uid | The user ID that is used for resource management. This parameter is required. |

5. In the **Server Address Pool Settings** section, configure the following parameters and
click **Create**.

| Parameter | Description |
|---|---|
| Address Pool ID | The ID of the address pool of the application server. If you leave this parameter empty, a new address pool ID is created. |
| Address Pool Name | The name of the address pool. |
| Address Pool Description | The description of the address pool. |

| Creation Mode | The creation type of the application server. Valid values: Within VPC Outside VPC Note If you select application servers in a VPC, you can add multiple application servers in the same VPC at a time. Separate the server IDs or IP addresses with commas (,). |
|---|---|
| vpcId | This parameter takes effect only if you set the Creation Mode parameter to Within VPC. The ID of the VPC in which the application server resides. |
| serverIds | This parameter takes effect only if you set the Creation Mode parameter to Within VPC. The IDs of the application servers to be added. You can add multiple application servers at a time. Separate the server IDs with commas (,). |
| vswitchId | This parameter takes effect only if you set the Creation Mode parameter to Within VPC. The ID of the vSwitch to which the application server belongs. |
| mappingIp | This parameter takes effect only if you set the Creation Mode parameter to Within VPC. The mapping IP address that is created for the specified vSwitch. The IP address is used to map the IP address of the application server. Note If the existing mapping IP addresses in the vSwitch are not used up, the mapping IP address created in this step may not be used. If no mapping IP addresses exist in the vSwitch and you do not create a mapping IP address in this step, an error may be reported later. |
| serverIps | This parameter takes effect only if you set the Creation Mode parameter to Outside VPC. The classic network IP addresses of the application servers to be added. |

6. Configure the following parameters and click **Create ECS Authorization**.

| Parameter | Description |
|---|---|
| VPC ID | The ID of the VPC in which the Elastic Compute Service (ECS) instance that you want to authorize the reverse access instance to access resides. |
| Creation Mode | The creation type of the ECS authorization. Valid values: Instance ID Instance IP Address |
| instanceId | This parameter takes effect only if you set the Creation Mode parameter to Instance ID. The ID of the ECS instance to be accessed. |
| instanceIp | This parameter takes effect only if you set the Creation Mode parameter to Instance IP Address. The private IP address of the ECS instance to be accessed. |
| instancePort | The port of the ECS instance to be accessed. |

7. View the details of a reverse access instance.
i. Find the reverse access instance that you want to view and click **Details** in the
**Operation** column.
ii. On the **Reverse Access Instance Details** page, view the instance details in the **Basic**
**Information** section and on the **Server Address Pool** and **ECS Reverse**
**Authorization** tabs.
iii. On the **Server Address Pool** tab, perform the following operations.

| Operation | Procedure |
|---|---|
| Create an address pool | a. Click Create Address Pool. b. In the dialog box that appears, configure the parameters as described in Step 5 and click Create. |

| View the server details of an address pool | a. Find the address pool that you want to view and clickS erver Details in the Operation column. In the Server Details panel, view the server details of the address pool. b. The server details are displayed in the following columns: VPC ID, Server ID, Server IP, Server Mapping IP, Server Type, and Status. Note To add an application server, click Add Application Server To delete an application server, find the application server that you want to delete and click Delete in the Operation column. |
|---|---|
| Modify an address pool | a. Find the address pool that you want to modify and clickM odify in the Operation column. b. In the dialog box that appears, modify the parameters and clickM odify. Note You can modify only the Name and Description parameters. |
| Delete an address pool | a. Find the address pool that you want to delete and clickD elete in the Operation column. b. In the message that appears, click Delete. Note Before you delete an address pool, you must delete all application servers that are associated with the address pool. Otherwise, the address pool cannot be deleted. The address pool is deleted immediately after you click Delete. Proceed with caution. |

iv. On the **ECS Reverse Authorization** tab, perform the following operations.

| Operation | Procedure |
|---|---|
| Create an authorization | a. Click Authorize. b. In the dialog box that appears, configure the parameters as described in Step 6 and click Create ECS Authorization. |
| Delete an authorization | a. Find the authorization that you want to delete and clickD elete in the Operation column. b. In the message that appears, click Delete. Note The authorization is deleted immediately after you click Delete. Proceed with caution. |

**What to do next**

**Modify a reverse access instance**

1. Find the reverse access instance that you want to modify and click **Modify** in the
**Operation** column.
2. In the dialog box that appears, modify the parameters and click **Modify**.

> **Note:** You can modify only the **Instance ID/Name** and **Description** parameters.

**Delete a reverse access instance**

1. Find the reverse access instance that you want to delete and click **Details** in the
**Operation** column.
2. On the **Reverse Access Instance Details** page, click **Delete Instance** in the upper-right
corner.
3. In the message that appears, click **Delete**.

> **Note:** Before you delete a reverse access instance, you must delete all application servers and address pools that are associated with the instance. Otherwise, the instance cannot be deleted.

#### 2.1.7 Traffic visualization

The Traffic Visualization module can monitor physical and virtual networks in the cloud platform, and analyze real-time and historical traffic in the networks. This module also analyzes traffic by virtual network, public network, and border physical network and generates visualized charts. You can also troubleshoot issues based on the traffic data or monitored traffic metrics.

> **Note:** By default, the Traffic Visualization module is not displayed. To use this module, perform the following operations: Log on to the Apsara Uni-manager Operations Console. In the top navigation bar, choose More > **User Authorities**. In the left-side navigation pane, click **Menu Management**. On the Menu management page, modify the menu settings to display the Traffic Visualization module.

##### 2.1.7.1 Visual settings

Before you use traffic visualization, you must configure items such as analyzers, collection rules, and scenarios to collect, process, and analyze traffic based on your business requirements.

**Workflow**

The following flowchart shows how to initialize traffic visualization.
1. For more information about how to add an analyzer and an analysis port, see the Manage
analysis devices section of this topic.
2. For more information about how to add a collection rule, see the Manage collection rules
section of this topic.
3. For more information about how to add an analysis scenario, see the Manage scenarios
section of this topic.

**Manage analysis devices**

Analysis devices include analyzers and analysis ports. The collection and analysis of traffic depends on the analysis devices. Before you collect and analyze traffic, you must create the required analysis devices. An **analyzer**, also known as a network performance monitor (NPM), refers to a device that performs traffic analysis. The following types of analyzers are supported: NPM physical machines and NPM central control machines. An **analysis port**refers to the traffic collection port of an NPM device. Traffic is received on the port for collection and analysis.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
3. In the left-side navigation pane, choose **Traffic Visualization** > **Visual Settings**.
4. On the **Analyze Device Management** tab, you can perform the following operations.

| Section | Operation | Procedure |
|---|---|---|
|   |   | i. In the Analyzer management section, click Add analyzer. |

| sara Uni-manage nsole | r Operations | Platform Operation and Mainten nce Operations Guide·Network peration |
|---|---|---|
| Analyzer management | Create an analyzer | ii. In the Add Analyzer panel, configure the following parameters: Zone: the zone in which you want to create an analyzer. Analyzer name: the name of the analyzer. Analyzer role: the role that the NPM device plays. Valid values: NPM physical machine: collects and processes traffic. NPM central controller: displays traffic analysis results. Galaxy Security Gateway: preferentially forwards traffic to the traffic gateway when you configure virtual private cloud (VPC) traffic mirroring rules. Manage IP addresses: the IP address of the NPM device. Username: the username that is used to log on to the NPM device. Password: the password that is used to log on to the NPM device. Serial Number: the serial number of the NPM device. Portal: the web page URL of the NPM central controller, which is used for daily O&M and management of the NPM device. The portal is automatically generated by the |
|   | View the details of an analyzer | system. After the analyzer is created, you can view the value in the analyzer list. i. In the Analyzer management section, find the analyzer thaAtn yaoluy zwearn dt etos cvrieipwt iaonnd: cthlicek d Desectraipiltsio inn othf eth Oep aenraaltyizoenr. column. iii. Click OK. ii. In the Details panel, view the details of the analyzer. |

|   | Modify an analyzer | i. In the Analyzer management section, find the analyzer that you want to manage and click Edit in the Operation column. ii. In the Edit analyzer panel, modify the parameters based on your business requirements and click OK. Note The Analyzer role parameter cannot be modified. |
|---|---|---|
|   | Delete an analyzer | Important If an analyzer is associated with a collection rule, you cannot delete the analyzer. i. In the Analyzer management section, find the analyzer that you want to delete and click Delete in the Operation column. ii. In the message that appears, click OK. |

| Analysis Port Management | Create an analysis port | Note Before you create an analysis port, make sure that an analyzer is created. i. In the Analysis Port Management section, click Add an analysis Port. ii. In the Add an analysis Port panel, configure the following parameters. Analysis port name: the name of the analysis port. Analyzer name: the analyzer that you want to use. Analyzer physical interface name: the physical interface of the analyzer. Analysis Port Type: the type of the analysis port. Valid values: VPC Physical ACK ALL Analysis port IP: the IP address of the analysis port. Description: the description of the analysis port. iii. Click OK. |
|---|---|---|

|   | View the details of an analysis port. | i. In the Analysis Port Management section, find the analysis port that you want to view and click Details in the Operation column. ii. In the Details panel, view the details of the analysis port. |
|---|---|---|
|   | Modify an analysis port | i. In the Analysis Port Management section, find the analysis port that you want to modify and click Edit in the Operation column. ii. In the Edit analysis Port panel, modify the parameters based on your business requirements and click OK. Note The Analyzer name and Analyzer physical interface name parameters cannot be modified. |
|   | Delete an analysis port | Important If an analysis port is associated with a collection rule, you cannot delete the analysis port. i. In the Analysis Port Management section, find the analysis port that you want to delete and click Delete in the Operation column. ii. In the message that appears, click OK. |

**Manage collection rules**

A collection rule defines the data source and analysis mode of traffic. The analysis devices specified in a collection rule collect and analyze traffic based on the collection rule.

**Prerequisites**

You have created an analyzer and an analysis port. For more information, see the Manage analysis devices section of this topic.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
3. In the left-side navigation pane, choose **Traffic Visualization** > **Visual Settings**.
4. Click the **Collection rule management** tab. On this tab, you can perform the following
operations.

| Operation | Procedure |
|---|---|

| Create a collection rule | i. Click Add collection rules. ii. In the Add collection rules panel, configure the parameters. For more information about the parameters, see the Appendix section of this topic. iii. Click OK. |
|---|---|

| Modify a collection rule | i. Find the collection rule that you want to modify and clickE dit in the Operation column. ii. In the Edit collection rules panel, modify the parameters based on your business requirements. Note If the Data source type parameter is set to Elastic network card, you can modify the Zone, Rule name, Display VPC Image Filtering Rules, SLB Instance, and Description parameters. If the Data source type parameter is set to Physical switch, you can modify the Zone, Rule name, and Description parameters. If the Data source type parameter is set to ACK container, you can modify the Rule name and ACK Cluster ID parameters. iii. Click OK. |
|---|---|
| Delete a collection rule | Important If a collection rule is associated with an analysis scenario, you cannot delete the collection rule. i. Find the rule that you want to delete and clickD elete in the Operation column. ii. In the message that appears, click OK. |

**Appendix**

Parameters required for creating a collection rule

| Parameter | Description |
|---|---|
| Zone | The zone in which you want to create a collection rule. |
| Rule name | The name of the collection rule. |
| Data source type | The type of the data source. Valid values: Elastic network card: collects traffic from elastic network interfaces (ENIs). Physical switch: collects traffic from physical switches. ACK container: collects traffic from Container Service for Kubernetes (ACK) containers. |
| Traffic analysis mode | Set the value to Traffic Image. This value specifies that traffic is completely replicated to the analysis port. |

| AliUid | This parameter is available only if you set the Data source type parameter to Elastic network card. The Apsara Stack account ID for authorization. The level-1 organization corresponding to the Apsara Stack account ID must have authorized the Cloud Gateway (CGW) service account in the Apsara Uni-manager Management Console. Note After authorization is complete, the service creates a VPC image, creates a Server Load Balancer (SLB) instance, and then attaches the NPM server or traffic gateway to the backend servers of the SLB instance for tenants in the level-1 organization. |
|---|---|
| Select VPC | This parameter is available only if you set the Data source type parameter to Elastic network card. Select the VPC to which the ENI belongs. |
| Select ENI | This parameter is available only if you set the Data source type parameter to Elastic network card. Select the ENI that you want to use. |
| Display VPC Image Filtering Rules | This parameter is available only if you set the Data source type parameter to Elastic network card. This parameter specifies whether to display VPC image filtering rules. Valid values: Show Hide |
| Collection Policy for Inbound Rules | This parameter is available only if you set the Data source type parameter to Elastic network card and the Display VPC Image Filtering Rules parameter to Show. Select the collection action of the inbound rule. Valid values: Collect Network Traffic Network Traffic Is Not Collected |
| Source CIDR Block of Inbound Traffic | This parameter is available only if you set the Data source type parameter to Elastic network card and the Display VPC Image Filtering Rules parameter to Show. Enter the source CIDR block of the inbound network traffic. |

| Source Port Range of Inbound Traffic | This parameter is available only if you set the Data source type parameter to Elastic network card and the Display VPC Image Filtering Rules parameter to Show. Enter the source port range of the inbound network traffic. Note The port range is 1 to 65535. Separate the first port and the last port with a forward slash (/). Examples: 1/200 and 80/80. If you set the protocol type to ALL or ICMP, you do not need to set this parameter. In this case, all ports are available. |
|---|---|
| Protocol Type Used by Inbound Traffic to Be Mirrored | This parameter is available only if you set the Data source type parameter to Elastic network card and the Display VPC Image Filtering Rules parameter to Show. Select the protocol that is used by the inbound traffic to be mirrored. Valid values: ALL ICMP TCP UDP |
| Destination CIDR Block of Inbound Traffic | This parameter is available only if you set the Data source type parameter to Elastic network card and the Display VPC Image Filtering Rules parameter to Show. Enter the destination CIDR block of the inbound network traffic |
| Destination Port Range of Inbound Traffic | This parameter is available only if you set the Data source type parameter to Elastic network card and the Display VPC Image Filtering Rules parameter to Show. Enter the destination port range of the inbound network traffic. Note The port range is 1 to 65535. Separate the first port and the last port with a forward slash (/). Examples: 1/200 and 80/80. If you set the protocol type to ALL or ICMP, you do not need to set this parameter. In this case, all ports are available. |
| Collection Policy for Outbound Rules | This parameter is available only if you set the Data source type parameter to Elastic network card and the Display VPC Image Filtering Rules parameter to Show. Select the collection action of the outbound rule. Valid values: Collect Network Traffic Network Traffic Is Not Collected |

| Source CIDR Block of Outbound Traffic | This parameter is available only if you set the Data source type parameter to Elastic network card and the Display VPC Image Filtering Rules parameter to Show. Enter the source CIDR block of the outbound network traffic. |
|---|---|
| Source Port Range of Outbound Traffic | This parameter is available only if you set the Data source type parameter to Elastic network card and the Display VPC Image Filtering Rules parameter to Show. Enter the source port range of the outbound network traffic. Note The port range is 1 to 65535. Separate the first port and the last port with a forward slash (/). Examples: 1/200 and 80/80. If you set the protocol type to ALL or ICMP, you do not need to set this parameter. In this case, all ports are available. |
| Protocol Type Used by Outbound Traffic to Be Mirrored | This parameter is available only if you set the Data source type parameter to Elastic network card and the Display VPC Image Filtering Rules parameter to Show. Select the protocol that is used by the outbound traffic to be mirrored. Valid values: ALL ICMP TCP UDP |
| Destination CIDR Block of Outbound Traffic | This parameter is available only if you set the Data source type parameter to Elastic network card and the Display VPC Image Filtering Rules parameter to Show. Enter the destination CIDR block of the outbound network traffic. |
| Destination Port Range of Outbound Traffic | This parameter is available only if you set the Data source type parameter to Elastic network card and the Display VPC Image Filtering Rules parameter to Show. Enter the destination port range of the outbound network traffic. Note The port range is 1 to 65535. Separate the first port and the last port with a forward slash (/). Examples: 1/200 and 80/80. If you set the protocol type to ALL or ICMP, you do not need to set this parameter. In this case, all ports are available. |
| SLB Type | This parameter is available only if you set the Data source type parameter to Elastic network card. You can select Use Existing SLB Instance or Create SLB Instance. |

| SLB Instance | This parameter is available only if you set the Data source type parameter to Elastic network card and the SLB Type parameter to Use Existing SLB Instance. Select the SLB instance that you want to use. |
|---|---|
| SLB Backend Device Name | This parameter is available only if you set the Data source type parameter to Elastic network card and the SLB Type parameter to Create SLB Instance. Select the name of the SLB backend device. |
| Analysis Port Name of SLB Backend Device | This parameter is available only if you set the Data source type parameter to Elastic network card and the SLB Type parameter to Create SLB Instance. Select the name of the analysis port of the SLB backend device. |
| Data source host device | This parameter is available only if you set the Data source type parameter to Physical switch. Select the host device of the physical switch. |
| Port name of the data source host device | This parameter is available only if you set the Data source type parameter to Physical switch. Select the ports of the physical switch host device. You can select multiple ports at a time. |
| Data Source Port ID | This parameter is available only if you set the Data source type parameter to Physical switch. The value is automatically matched based on the data source host device and the port name of the data source host device that you select. |
| Analyzer Name | This parameter is available only if you set the Data source type parameter to Physical switch. Select the analyzer that you want to use to collect traffic. |
| Analysis Port Name | This parameter is available only if you set the Data source type parameter to Physical switch. Select the analysis port that you want to use to collect traffic. |
| Analysis Port VLAN ID | This parameter is available only if you set the Data source type parameter to Physical switch. Enter the VLAN ID of the analysis port. |

| Create Resource Type | This parameter is available only if you set the Data source type parameter to ACK container. Select the type of resources to be created. OnlyS LB Instance is supported. |
|---|---|
| SLB Type | This parameter is available only if you set the Data source type parameter to ACK container. Select the purpose of the SLB instance to be created. Valid values: Data Channel: creates an SLB instance to connect the ACK cluster to the ACK traffic analysis port of the NPM device. This serves as a data channel to carry the ACK traffic. Signaling Channel: creates an SLB instance to connect the ACK cluster to the management port of the NPM device. This serves as a signal channel. |
| Level-1 Organization AliUid | This parameter is available only if you set the Data source type parameter to ACK container. The Apsara Stack account ID for authorization. The level-1 organization corresponding to the Apsara Stack account ID must have authorized the CGW service account in the Apsara Uni-manager Management Console. Note After authorization is complete, the service creates a VPC image, creates an SLB instance, and then attaches the NPM server or traffic gateway to the backend servers of the SLB instance for tenants in the level-1 organization. |
| ACK Cluster ID | This parameter is available only if you set the Data source type parameter to ACK container. Select the ID of an ACK cluster. |
| Select VPC | This parameter is available only if you set the Data source type parameter to ACK container. Select the VPC to which the ACK cluster belongs. |
| Select a VSwitch | This parameter is available only if you set the Data source type parameter to ACK container. Select the vSwitch to which the ACK cluster belongs. |
| SLB Backend Device Name | This parameter is available only if you set the Data source type parameter to ACK container. Select the name of the SLB backend device. |
| Analysis Port Name of SLB Backend Device | This parameter is available only if you set the Data source type parameter to ACK container. The name of the analysis port of the SLB backend device. |

| Description | This parameter is available only if you set the Data source type parameter to Elastic network card or Physical switch. Enter the description of the collection rule. |
|---|---|

**Manage scenarios**

You can associate different collection rules with different analysis scenarios based on your business requirements.

**Prerequisites**

You have created a collection rule. For more information, see the Manage collection rules section of this topic.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
3. In the left-side navigation pane, choose **Traffic Visualization** > **Visual Settings**.
4. Click the **Scenario Management** tab. On this tab, you can perform the following
operations.

| Operation | Procedure |
|---|---|
|   | i. Click Create an analysis scenario. ii. In the Add scenario panel, configure the following parameters. |

| Create an analysis scenario |   |
|---|---|
|   | Zone: the zone in which you want to create an analysis scenario. Scene name: the name of the analysis scenario. Network Type: the network type of the analysis scenario. Valid values: VPC: the virtual network. BORDER: the border physical network. |
| Modify an analysis scenario | Collection rules: the one or more collection rules that you want to i. Find the analysis scenario that you want to modify and clickE dit in the associate with the analysis scenario. You can select multiple collection Operation column. rules. ii. In the Edit scene panel, modify the parameters based on your business Description: the description of the analysis scenario. requirements. iii. Click OK. Note The Network Type parameter cannot be modified. iii. Click OK. |
| Delete an analysis scenario | i. Find the analysis scenario that you want to delete and clickD elete in the Operation column. ii. In the message that appears, click OK. |

**View network resources**

You can view all the SLB instances that are created in the traffic visualization module.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
3. In the left-side navigation pane, choose **Traffic Visualization** > **Visual Settings**.
4. Click the **Network Resource List** tab. On this tab, view the network resource information
in the following columns: **Zone**, **Resource ID**, **Resource Value**, **Resource Type**, **VpcId**,
**Resource Usage**, **Resource Owner**, and **Created At**.

##### 2.1.7.2 Overview

The Overview page in the Traffic Visualization module displays the traffic details of virtual and physical networks in the trend charts and pie charts. This allows you to view historical and real-time traffic and perform statistical analysis based on your business requirements.

**Prerequisites**

The initial configurations for traffic visualization are complete. For more information, see Visual settings.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
3. In the left-side navigation pane, choose **Traffic Visualization** > **Overview**.
4. In the upper-right corner of the Overview page, specify a time range to view the traffic
details within the specified time range.

| Section | Description | Operation |
|---|---|---|
| Network Streams | Displays the total number of traffic flows in all virtual network and physical network scenarios within the specified time range. | Click a number to go to the Stream Search and Scheduling page. |
| Resource Statistics | Displays the number of virtual private clouds (VPCs), elastic IP addresses (EIPs), and Elastic Compute Service (ECS) instances within the specified time range. | N/A. |

| Virtual Network | Displays the traffic trend, ratio, and ranking overview of different metrics in virtual network scenarios within the specified time range. | Click View Details in different sections. In the dialog box that appears, select a network type, a scenario, a time range, and one or more metrics to view the corresponding traffic trend, ratio, or ranking overview of the selected metrics. Click Select Metrics and select one or more metrics that you want to view. |
|---|---|---|
| Physical Network | Displays the traffic trend, ratio, and ranking overview of different metrics in physical network scenarios within the specified time range. |   |

##### 2.1.7.3 Traffic search and scheduling

You can use the traffic search and scheduling feature to view the detailed traffic data and perform traffic scheduling. This allows you to balance the workload and efficiently utilize system resources.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
3. In the left-side navigation pane, choose **Traffic Visualization** > **Traffic Query and**
**Scheduling**.
4. On the Streams Search and Scheduling page, click **2-tuples** or **5-tuples**, click **Advanced**
**Filter**, set filter conditions, and then click **Search**.

| Category | Advanced filter condition |
|---|---|
| 2-tuples | In this mode, a source IP address and a destination IP address are used to identify network traffic. Start and End Time: Select the start time and end time. Network Type: Select VPC or BORDER. Scenario: Select the scenario that you want to query. Source VPC ID: This parameter is available only when the Network Type parameter is set to VPC. Destination VPC ID: This parameter is available only when the Network Type parameter is set to VPC. Source vSwitch ID: This parameter is available only when the Network Type parameter is set to VPC. Destination vSwitch ID: This parameter is available only when the Network Type parameter is set to VPC. Source Cloud Service: This parameter is available only when the Network Type parameter is set to BORDER. Destination Cloud Service: This parameter is available only when the Network Type parameter is set to BORDER. Source IP Address: Enter a source IP address. You can also enter a CIDR block. Destination IP Address: Enter a destination IP address. You can also enter a CIDR block. Core Metrics: You can select multiple metrics at a time. Sort by Indicator: Select the metric by which traffic flows are sorted. Sorting Rule: Select Ascend or Descend. |

| 5-tuples | In this mode, Source IP Address, Source Port, Destination IP Address, Destination Port, and Protocol Type are used to identify network traffic. Start and End Time: Select the start time and end time. Network Type: Select VPC or BORDER. Scenario: Select the scenario that you want to query. Source VPC ID: This parameter is available only when the Network Type parameter is set to VPC. Destination VPC ID: This parameter is available only when the Network Type parameter is set to VPC. Source vSwitch ID: This parameter is available only when the Network Type parameter is set to VPC. Destination vSwitch ID: This parameter is available only when the Network Type parameter is set to VPC. Source Cloud Service: This parameter is available only when the Network Type parameter is set to BORDER. Destination Cloud Service: This parameter is available only when the Network Type parameter is set to BORDER. Protocol Type: Select Only TCP traffic is displayed., Only UDP traffic is displayed., or Other Traffic Types. Source IP Address: Enter a source IP address. You can also enter a CIDR block. Destination IP Address: Enter a destination IP address. You can also enter a CIDR block. Source Port: Enter the source port number. Destination Port: Enter the destination port number. Core Metrics: You can select multiple metrics at a time. Sort by Indicator: Select the metric by which traffic flows are sorted. Sorting Rule: Select Ascend or Descend. |
|---|---|

5. View the traffic flows that meet the specified filter conditions.

**View the details of traffic flows identified by 2-tuples**

a. On the 2-tuples tab, find the traffic flow that you want to view and click **Details** in the
**Operation** column.
b. In the **Traffic Details** panel, view the information in the **Cloud Network Association**
**Information** and **Traffic Trend** sections.
c. Optional. On the 2-tuples tab, find the traffic flow that you want to view and click **5-**
**tuples Expansion** in the **Operation** column. The 5-tuples tab is displayed.

**View the details of traffic flows identified by 5-tuples**

On the 5-tuples tab, more details of traffic flows are displayed. a. Find the traffic flow that you want to view and click **Details** in the **Operation** column. b. In the **Traffic Details** panel, view the information in the **Cloud Network Association**
**Information** and **Traffic Trend** sections.

#### 2.1.8 Cloud service interconnection

The Cloud Service Interconnection module provides network access to cloud services, configuration of VIPs and DNS, and mutual access between cloud services in multiple clouds, data centers, and Apsara Stack.

> **Note:** By default, the Cloud Service Interconnection module is not displayed. To use this module, perform the following operations: Log on to the Apsara Uni-manager Operations Console. In the top navigation bar, choose More > **User Authorities**. In the left-side navigation pane, click **Menu Management**. On the Menu management page, modify the menu settings to display the Cloud Service Interconnection module.

##### 2.1.8.1 Dynamic VIPs

The dynamic virtual IP address (VIP) feature expands the network capabilities of cloud service interconnection. The feature allows you to create dynamic VIPs by using VIP resources applied for by the cloud services in Apsara Infrastructure Management as templates. You can modify the **type**, **tunnel_type**, and **ipprotocol** properties when you create a dynamic VIP. Other properties are the same as those in the template VIP resources defined by the cloud services. During the scaling, upgrades, and downgrades of cloud services, dynamic VIP resources and template VIP resources can be simultaneously updated by integrating with Apsara Infrastructure Management.

**Background information**

In scenarios that require large storage capacities, the dynamic VIP feature can scale out multiple Object Storage Service (OSS) Intranet VIP resources to bypass the single-VIP network speed of 5 Gbit/s. In hybrid cloud scenarios, you must access the Apsara Uni-manager Management Console over the Internet and use the dynamic VIP feature to create Internet VIP resources for the Apsara Uni-manager Management Console. The dynamic VIP tunnel type can be set only to classic_to_any_tunnel.

**Create a dynamic VIP**

1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
3. In the left-side navigation pane, choose **Cloud Service Interconnection** > **Dynamic**
**VIPs**.
4. On the Dynamic VIP page, click **Create Dynamic VIP**. In the dialog box that appears,
configure the following parameters and click **OK**.

| Parameter | Description |
|---|---|
| Cloud Name | The name of the cloud instance. |
| Region | The ID of the region. |
| Project | The name of the project. |
| Cluster | The name of the cluster. |
| Service | The name of the service. |

| ServiceRole | The name of the server role. |
|---|---|
| Application | The application name. |
| Template VIP Name | The name of the template VIP. |
| DynVipType | The type of the Server Load Balancer (SLB) instance. |
| DynVipTunnelType | The type of the tunnel. |
| Ipprotocol | The type of the VIP. |
| SuName | The service unit. |

**What to do next**

**View the details of a dynamic VIP**

1. On the Dynamic VIP page, click **Advanced Filter** and then specify the **VIP Address** and
**Template VIP Name** parameters to filter dynamic VIPs.
2. Find the dynamic VIP that you want to view and click **Details** in the Operation column to
view the details of the dynamic VIP.

**Update a dynamic VIP**

If the basic properties of a dynamic VIP are inconsistent with those of a template VIP, or if an operation on the dynamic VIP fails, **Abnormal** is displayed in the **Status** column that corresponds to the dynamic VIP. When the system detects that an exception occurs on the dynamic VIP, the system automatically checks and deletes DNS records that are associated with the abnormal dynamic VIP to reduce the impact on your business. The O&M personnel must check whether the dynamic VIP exception is caused by resource changes during service upgrades or scaling and perform the corresponding operations: If the exception is caused by resource changes during service upgrades or scaling, click
**Update** in the Actions column. The system queries the template VIP parameters by calling
Apsara Infrastructure Management API operations and combines these parameters with the variable properties of the dynamic VIP to update the dynamic VIP. If the exception is not caused by resource changes during service upgrades or scaling, contact Alibaba Cloud technical support.

**Delete a dynamic VIP**

1. Find the dynamic VIP that you want to delete and click **Delete** in the Operation column.
2. In the message that appears, click **OK**.

|   | Important Risks may arise if you delete dynamic VIPs. Proceed with caution. Before you delete a dynamic VIP, make sure that the VIP does not have sessions and that DNS records can no longer be resolved to the dynamic VIP. |   |
|---|---|---|

##### 2.1.8.2 Dynamic DNS

The dynamic DNS feature works with the dynamic virtual IP address (VIP) feature to implement horizontal network expansion by resolving DNS resources in cloud services to multiple VIPs, including one static VIP and multiple dynamic VIPs.

**Background information**

The dynamic DNS feature is applicable to scenarios such as multi-cloud geo-disaster recovery and hybrid clouds. This feature allows you to perform the following operations: Add domain names for zones corresponding to ops-dns intranet-domain and internetdomain. By default, ops-dns returns the resolution records in rotation mode. Add the forwarding records of a tenant DNS to forward domain name resolution requests in a specific zone to external DNS servers such as DNS servers in Apsara Stack, heterogeneous clouds, and Alibaba Cloud.

> **Warning:** Before you resolve DNS domain names in the Apsara Infrastructure Management console, make sure that the parameters of the dynamic VIPs and the static VIP are exactly the same, and VIP listening on access is normal. Otherwise, network exceptions may occur.

**Create a dynamic DNS record**

1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
3. In the left-side navigation pane, choose **Cloud Service Interconnection** > **Dynamic**
**DNS**.
4. On the Dynamic VIP page, click **Add DNS Record**. In the dialog box that appears,
configure the following parameters and click **OK**.

| Parameter | Description |
|---|---|
| Cloud Name | The name of the cloud instance. |
| Region | The region ID. |
| DNS Type | The type of DNS. Valid values: dns product and ops dns. |
| DNS Record Type | The type of the DNS record. If you set theD NS Type parameter to dns product, set this parameter to Forward-Zone. If you set the DNS Type parameter to ops DNS, set this parameter to A. |
| Remote Cloud ID | This parameter takes effect only when the DNS Type parameter is set to dns product. The ID of the cloud instance in the current cloud. |
| DnsZone | This parameter takes effect only when the DNS Type parameter is set to dns product. The DNS zone. Separate multiple zones with commas (,). |

| Forwarders | This parameter takes effect only when the DNS Type parameter is set to dns product. The forwarding IP addresses. Separate multiple IP addresses with commas (,). |
|---|---|
| DnsDomain | This parameter takes effect only when the DNS Type parameter is set to ops dns. The IP address of the DNS domain. |
| DnsRecord | This parameter takes effect only when the DNS Type parameter is set to ops dns. The IP address recorded by the DNS. |

**What to do next**

**View the details of a dynamic DNS record**

On the Dynamic DNS page, click **Advanced Filter** and then specify the **Remote Cloud ID**,
**Record Type**, **Zone**, **DnsDomain**, and **Forwarders/records** parameters to filter dynamic
DNS records.

**Update a dynamic DNS record**

1. On the Dynamic DNS page, find a dynamic DNS record that you want to update and click
**Update** in the Operation column.
2. In the dialog box that appears, modify the **Remote Cloud ID** and **DnsRecord** parameters.
Then, click **OK**.

**Delete a dynamic DNS record**

1. Find the dynamic DNS record that you want to delete and click **Delete** in the Operation
column.
2. In the message that appears, click **OK**.

> **Warning:** Risks may arise if you delete DNS records. Proceed with caution. Before you delete a DNS record, make sure that an alternate DNS record is available for the domain name or that no other clients have access to this domain name.

#### 2.1.9 Network changes

The network change feature simplifies the process of configuring switches in mainstream scenarios, such as expanding the RAMA CIDR blocks, expanding the CIDR blocks of kernelbased virtual machines (KVMs), expanding the virtual IP address (VIP) range of Server Load Balancer (SLB) instances, and expanding the access switch (ASW) CIDR blocks.

##### 2.1.9.1 Change plans

You can view the available change plans on the Change scheme List page in the Network Change module.

**Prerequisites**

The incremental planning is complete in Apsara Stack Deployment Planner, and the desired state file is obtained. Switches are installed, deployed, and connected based on the incremental planning. Switches are powered up and patches are updated for versions. The association configuration for the distribution switch (DSW) is added.

**Change plans**

The following table describes the available change plans that are preset in the Apsara Unimanager Operations Console.

| Change plan | Risk level | Description |
|---|---|---|
| Switch password change | High risk | This change plan applies to scenarios where you want to change the password of a switch based on your business requirements or password policies. You must save the new password. |
| Access control list (ACL) rule configuration | High risk | This change plan applies to scenarios where you want to create ACL rules for switches. You can use the change plan to create multiple ACL rules at a time. Ports whose configurations are changed at a time use the same set of ACL rules. You cannot add rules to an existing ACL. Otherwise, when you roll back this change plan, the ACL is deleted. |
| Three-zone disaster recovery of CGW clusters | High risk | This change plan applies only to scenarios where you deploy a single CGW cluster in three zones. |
| Connection between the classic network and a data center | High risk | This change plan applies to scenarios where you want to connect a data center to the classic network by using inter- connection switches (ISWs) or customer switches (CSWs). This change plan allows you to configure the network quality analysis (NQA) instance and static routes for switches by using physical interfaces or subinterfaces. The change plan supports the switches that are deployed in the single-zone, active/standby, or active-active mode. Separate input parameters with commas (,). |
| Simple network management protocol (SNMP) configuration | High risk | This change plan applies to scenarios where you want to set the SNMP configuration for a network device when you configure network monitoring for it. |

| Using public CIDR blocks as virtual private cloud (VPC) CIDR blocks | High risk | The private CIDR blocks of a VPC are specified by the private cidr table in the key value config info configuration of _ _ _ _ the VPC in Apsara Stack. After you associate an elastic IP address (EIP) with an Elastic Compute Service (ECS) instance deployed in the VPC, the ECS instance routes data based on the private network configuration specified by the private cidr _ table. If you want to use public IP addresses or pseudo-public IP addresses as private IP addresses, you can assign these public IP addresses to an Apsara virtual switch (AVS) as private CIDR blocks. To do so, modify the vpc default private cidr _ _ _ parameter in the key value config info configuration. You can _ _ _ also modify the User cidr table of the VPC to use the custom _ private network configuration. |
|---|---|---|
| Incremental deployment of access switches (ASWs) in Apsara Stack | Low risk | This change plan applies to scenarios where you want to implement the incremental deployment of ASWs in Apsara Stack. |
| kvm docker CIDR _ block add | Low risk | This change plan allows you to add kvm docker CIDR blocks. _ |
| kvm docker CIDR _ block expansion | Low risk | This change plan allows you to expand kvm docker CIDR _ blocks. |
| RAMA CIDR block add | Low risk | This change plan allows you to add RAMA CIDR blocks. |
| RAMA CIDR block expansion | Low risk | This change plan allows you to expand RAMA CIDR blocks. |
| Expansion of the virtual IP address (VIP) range of a Server Load Balancer (SLB) instance | Low risk | If the IP addresses in the VIP resource pool are insufficient or the reserved CIDR blocks are insufficient, you can use this change plan to expand the VIP range. |
| Expansion of the mapping server CIDR _ blocks of a VPC | Low risk | Apsara Stack provides the reverse access feature that allows one-way access from the classic network to VPCs. A certain number of IP addresses are reserved for reverse access during the delivery. The reserved IP addresses may be used up. In this case, you must expand the IP addresses for reverse access. |

1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
3. In the left-side navigation pane, choose **Network Change** > **Change Plans**.
4. On the Change scheme List page, view the information about the change plans in the
columns, such as **Scheme name**, **Risk level**, **Impact Products**, **Number of executions**, and **Description**. To filter change plans, click **Advanced Filter** and then specify the **Scheme name**, **Risk**
**level**, and **Impact Products** parameters.

> **Note:** To view the execution history of a change plan, click the number in the **Number of** **executions** column of the change plan to go to the **Program execution history** page. For more information, see Execution history.

5. Find a change plan whose details you want to view and click **Details** in the **Operation**
column. On the **Change Plan Details page**, you can view information in the **Basic**
**information** and **Scheme flow chart** sections.

> **Note:** In the **Scheme flow chart** section, click the step icon. In the **Procedure details** panel, you can view information in the **Step information** and **Execution Information** sections.

6. On the **Change Plan Details page**, click **Initiate Execution** in the upper-right corner. In
the Initiate execution dialog box, configure the parameters and then click **OK**.

> **Note:** You can also click **Initiate execution** in the **Operation** column of a change plan on the **Change scheme List** page.
> The parameters that you need to configure for execution vary based on the change plan. The parameters displayed in the Initiate execution dialog box prevail.

7. On the **Plan execution details** page, you can perform the following operations:
In the **Basic information** section, you can view the basic information about the execution. In the **Execution progress** section, you can **continue**, **suspend**, or **terminate** the change plan. You can perform the following operations based on the execution status: Click **View details**. In the panel that appears, view the procedure details on the **Basic**
**information**, **Execution Information**, and **Parameter information** tabs.
If the execution is in the ParamVerifying state, the workflow is paused and the parameter verification result waits for the confirmation from the change plan executor. Click **Confirm parameters**. In the Confirm parameters dialog box, view the verification result and identify whether the result is normal based on the actual situation. Then, you can click **Terminate workflow** to terminate the workflow or
**Approved** to continue the workflow. When the workflow enters the End state, the
workflow ends. If the execution is in an abnormal state, such as Failed or `W_MaxRetries` , suspend the change plan, troubleshoot issues based on the execution logs, and then continue or reexecute the change plan. If the execution is in the W_MaxRetries state, click **Retry** to retry the execution. In the **Execution Information** section, you can view the **event records**, **parameter**
**information**, and **execution logs**.

**What to do next**

**Import a change plan**

1. On the **Change scheme List** page, click **Import solution**.
2. Select the change plan that you want to import and click **Open**.

##### 2.1.9.2 Execution history

You can view the execution history of change plans on the Program execution history page in the Network Change module.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
3. In the left-side navigation pane, choose **Network Change** > **Execution History**.
4. On the Program execution history page, you can view the execution details of change plans
in the columns, such as **Workflow ID**, **Scheme name**, **Description**, **Execution time**,
**Execution result**, and **Executor**.
To filter executions, click **Advanced Filter** and then specify the **Schema name**,
**Execution result**, **Execution time**, **Author**, and **Workflow ID** parameters.

> **Note:** For more information about **execution results**, see the Appendix section of this topic.

5. Find the execution that you want to view and click **View details** in the **Operation** column.
On the **Plan execution details** page, you can perform the following operations: In the **Basic information** section, you can view the basic information about the execution. In the **Execution progress** section, you can **continue**, **suspend**, or **terminate** the change plan. You can perform the following operations based on the execution status: Click **View details**. In the panel that appears, view the procedure details on the **Basic**
**information**, **Execution Information**, and **Parameter information** tabs.
If the execution is in the ParamVerifying state, the workflow is paused and the parameter verification result waits for the confirmation from the change plan executor. Click **Confirm parameters**. In the Confirm parameters dialog box, view the verification result and identify whether the result is normal based on the actual situation. Then, you can click **Terminate workflow** to terminate the workflow or
**Approved** to continue the workflow. When the workflow enters the End state, the
workflow ends. If the execution is in an abnormal state, such as Failed or `W_MaxRetries` , suspend the change plan, troubleshoot issues based on the execution logs, and then continue or reexecute the change plan. If the execution is in the W_MaxRetries state, click **Retry** to retry the execution. In the **Execution Information** section, you can view the **event records**, **parameter**
**information**, and **execution logs**.

**Appendix**

The following table describes the **execution results** of a change plan and the corresponding states.

| Execution result | Description | Status |
|---|---|---|

| Pending | The change plan is waiting for execution. | Launching |
|---|---|---|
| Preparing | The environment is being prepared. | Launching |
| ParamParsing | The parameters are being preprocessed. | Launching |
| TransformBuilding | The workflow is being configured and orchestrated. | Launching |
| ContextBuilding | The workflow context is generated. | Launching |
| WardenLaunching | The workflow engine is started. | Launching |
| TaskRunning | The workflow is running. | Running |
| ParamVerifying | The parameters are waiting for verification. | Interrupted |
| End | The workflow is complete. | Closed |
| Cleaned | The workflow is deleted as residual data. | Closed |
| Failed | An exception occurred during the workflow execution. | Closed |
| W Init _ | The workflow is initialized. | Running |
| W New _ | The workflow is created. | Running |
| W Adopting _ | The workflow is distributed. | Running |
| W Start _ | The workflow is started. | Running |
| W Running _ | The workflow is running. | Running |
| W Done _ | The workflow is being closed. | Interrupted |

| W Closed _ | The workflow is closed. | Closed |
|---|---|---|
| W Cancelled _ | The workflow is canceled. | Closed |
| W StepError _ | The steps of the workflow are abnormal. | Closed |
| W MaxRetries _ | The maximum number of retries for the workflow is reached. | Closed |
| W Paused _ | The workflow is paused. | Interrupted |
| W Rollback _ | The workflow is rolled back. | Running |
| W Misfired _ | The workflow is stopped due to a timeout. | Closed |
| W Escaping _ | The workflow is escaping. | Running |
| W EscapeFail _ | The workflow failed to escape. | Closed |
| W EscapeSuccess _ | The workflow successfully escaped. | Closed |
| W QuotaReached _ | The upper limit for the workflow is reached. | Closed |
