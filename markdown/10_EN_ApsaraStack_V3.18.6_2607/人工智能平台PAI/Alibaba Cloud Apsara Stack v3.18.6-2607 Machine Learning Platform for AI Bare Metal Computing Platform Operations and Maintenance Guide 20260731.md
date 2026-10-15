---
title: "Alibaba Cloud Apsara Stack v3.18.6-2607 Machine Learning Platform for AI Bare Metal Computing Platform Operations and Maintenance Guide 20260731"
product_version: "V3.18.6_2607"
doc_version: "20260731"
pdf_pages: 73
source_pdf: "Alibaba Cloud Apsara Stack v3.18.6-2607 Machine Learning Platform for AI Bare Metal Computing Platform Operations and Maintenance Guide 20260731.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/3816%202607/pdf%203/%E4%BA%BA%E5%B7%A5%E6%99%BA%E8%83%BD%E5%B9%B3%E5%8F%B0PAI/Alibaba%20Cloud%20Apsara%20Stack%20v3.18.6-2607%20Machine%20Learning%20Platform%20for%20AI%20Bare%20Metal%20Computing%20Platform%20Operations%20and%20Maintenance%20Guide%2020260731.pdf"
converter: pdf2md (PyMuPDF line classifier)
---

# Alibaba Cloud Apsara Stack v3.18.6-2607 Machine Learning Platform for AI Bare Metal Computing Platform Operations and Maintenance Guide 20260731

## O&M overview

This topic describes the objectives, requirements, and precautions of Bare Metal Computing Platform (BMCP) O&M and how to obtain technical support.

**Objectives**

This guide helps O&M engineers perform preventive maintenance to ensure the long-term stability of BMCP. O&M engineers can follow the instructions in this guide to handle system issues that are identified during maintenance. For system issues that are not covered in this guide, O&M engineers can contact Apsara Stack engineers for technical support.

**Requirements**

O&M engineers must possess IT skills, including the knowledge of computer networks, computer operations, and troubleshooting. O&M engineers must pass the pre-job training and learn the knowledge for the Apsara Stack system. The required knowledge for the system includes system principles, networking, features, and the usage of maintenance tools.

**Important**

During the maintenance, O&M engineers must follow operation procedures to ensure personal safety and system security. No part of user data may be copied or disseminated in any form or by any means without prior written consent from users.

**Precautions**

To ensure a stable system and prevent unexpected events, O&M engineers must comply with the following guidelines: Hierarchical permission management Permissions on networks, devices, systems, and data are granted based on the services and roles of O&M engineers. This prevents system faults that are caused by unauthorized operations. System security Before O&M engineers perform operations on the system, they must be aware of the impacts of the operations. This ensures that the system is not affected by high-risk operations. O&M engineers must record the details about the issues that are encountered during the operations. This helps O&M engineers troubleshoot the issues. Personal safety and data security O&M engineers must take measures to ensure safety based on device manuals when they use electrical equipment. O&M engineers must use secure devices to access the business network. Unauthorized data replication and dissemination are prohibited.

**Technical support**

O&M engineers can contact Apsara Stack technical support for help during the maintenance.

## Getting started

### BMCP Operations Console

The Bare Metal Computing Platform (BMCP) Operations Console is a cutting-edge O&M technical solution that focuses on intelligent computing, high-performance computing, and scenarios where intelligent computing and high-performance computing are integrated. The BMCP Operations Console provides a high-performance computing system based on an Intel architecture and an intelligent computing system based on a NVIDIA architecture. It is compatible with domestic software and hardware ecosystems. The BMCP Operations Console provides O&M engineers with computing resource topology visualization and resource O&M capabilities. O&M engineers can centrally manage and maintain computing, network, and storage resources from the job and trace perspective. It greatly improves the O&M efficiency.

**Characteristics and benefits**

Full-stack device management Provides a multi-tenant-oriented computing resource normalization and O&M platform that covers computing, storage, and network resource topology management and maintenance. Computing resource supply for various architectures Supports mainstream training and inference platforms that use intel CPUs and NVIDIA GPUs. Supports domestic software and hardware ecosystem platforms based on Hygon CPUs and Hygon GPUs or based on Kunpeng CPUs and Huawei Ascend NPUs to ensure the supply of computing resources. Visualized real-time monitoring Provides visualized topology monitoring for nodes, links, and network elements, and uses time slice labeling to display the real-time status of computing, storage, and network resources. Job path analysis The job path analysis feature provides a topology view to display O&M planes from the perspective of jobs in order to conduct fine-grained O&M, including monitoring, alerting, diagnostics, and logging. Intelligent device inspection and diagnostics Analyzes the status of hardware devices and logs and conducts multi-level inspection to eliminate potential job risks in clusters. Performs cluster and computing job diagnostics to quickly locate issues, isolate resources, or fix issues. ROI optimization Supports the reuse of vendor or data center-level GPUs to improve the stock of computing resources in order to optimize the Return on Investment (ROI).

**Note**

The BMCP Operations Console is an enterprise-class O&M solution which is suitable for scientific institutions that need to process massive computing jobs, intelligent computing jobs, large-sized Internet enterprises, and the financial industry. It is a powerful and flexible resource O&M platform.

**Features**

**Job path analysis**

This module analyzes the topology of jobs in data planes and manages the lifecycle of nodes, GPUs, RDMA networks, RDMA network elements, and links in a visualized manner.

**Resource management**

This module allows you to manage all physical resources that are used by your businesses, including computing, storage, and network resources.

**Alert management**

This module monitors the stability metrics of computing resources, including nodes, GPUs, and RDMA resources, and generates alerts in real time when events are detected.

**Cluster management**

This module manages all computing logic resources used by your businesses, allowing you to centrally manage computing, storage, and network resources.

**Inspection and diagnostics**

This module inspects and diagnoses resources in different scenarios to quickly locate the cause.

**Log management**

This module allows you to export cluster or node logs to help improve the overall O&M efficiency and system reliability.

### Work with the BMCP

**Operations Console**

This topic describes how to work with the Bare Metal Computing Platform (BMCP) Operations Console. You can view the topology of training and inference jobs within the last 7 days on the BMCP Operations Console, and view the GPU, network interface controller (NIC), and vSwitch usage of these jobs and their metrics.

### Log in to the BMCP O&M

**platform**

This topic describes how users such as O&M engineers log in to the Apsara Uni-manager Operations Console.

**Prerequisites**

The endpoint of the Apsara Uni-manager Operations Console and the username and password that are used to log in to the console are obtained from a deployment engineer or an administrator. The endpoint of the Apsara Uni-manager Operations Console is in the following format: regi on-id.ops.console.intranet-domain-id. A supported browser is used. We recommend that you use Google Chrome.
1. Open a web browser.
2. In the address bar, enter the endpoint of the Apsara Uni-manager Operations Console.
Press the ENTER key.

**Note**

You can click the current language in the upper-right corner to switch to another language. Simplified Chinese, English, and traditional Chinese are supported.
3. Enter the correct username and password.

**Note**

Obtain the username and password that are used to log in to the Apsara Unimanager Operations Console from a deployment engineer or an administrator. If you enter an invalid password three consecutive times, the system enables the image verification login feature. If you enter an invalid password five consecutive times, the system locks your account. In this case, you can contact the administrator to unlock your account. The first time that you log in to the Apsara Uni-manager Operations Console, change the password for your account as prompted. To enhance security, make sure that your password meets the following requirements: The password contains uppercase and lowercase letters. The password contains digits. The password contains at least one of the following special characters: ! @
# $ %
The password is 10 to 20 characters in length.
4. Click **Agree to Private Policy and Log On** .
5. In the menu bar at the top of the page, select **Product Operation > Computing > BMCP**
**Operation platform**.

## Overview

This topic describes the content displayed on the Overview page of the Bare Metal Computing Platform (BMCP) Operations Platform, where you can view Alert Dashboard, Resource Statistics, Computing Power Dashboard, and Control Services.

**Alert dashboard**

The alert dashboard displays alerts related to computing, networks, and storage.

**Resource statistics**

This section displays resource data related to intelligent computing clusters, supercomputing clusters, and storage clusters. Total number of intelligent computing clusters, number of servers, and number of instances Intelligent computing clusters include bare metal-intelligent computing clusters and ACKintelligent computing clusters. Intelligent computing instances include high-bandwidth network intelligent computing instances, managed intelligent computing instances, and basic intelligent computing instances. Intelligent computing instances include only bare metal instances. Total number of converged clusters, number of servers, and number of instances Converged instances include basic converged instances and high-bandwidth network converged instances. Total number of supercomputing clusters, number of servers, and number of instances Supercomputing clusters include bare metal-supercomputing clusters. Supercomputing instances include high-performance high-bandwidth network instances. Total number of storage clusters, number of servers, and number of file systems

**Resource dashboard**

This section displays the usage of intelligent computing resources, supercomputing resources, and storage resources.

**Note**

Supercomputing resources do not include the CPU cores and memory of intelligent computing clusters. Intelligent computing resources do not include the GPUs and GPU memory of supercomputing clusters. Intelligent computing resources (number of GPUs and GPU memory) Select a GPU type from the drop-down list, such as **NVIDIA** or **Hygon**, to view the GPU quantity of the selected type and total GPU memory.

**Note**

The available GPU types are subject to those displayed on the page. View the data for Allocated, Not Allocated, Total, and Allocation Rate. The amount of allocated resources indicates the resources that are allocated to tenants. The amount of unallocated resources indicates the resources in the resource pool. The total amount of resources equals the sum of resources allocated to tenants and resources in the resource pool. Allocation rate = Resources in the resource pool/(Resources allocated to tenants + Resources in the resource pool) × 100%. Converged resources (number of GPUs and GPU memory) Select a GPU type from the drop-down list, such as **NVIDIA** or **Hygon**, to view the GPU quantity of the selected type and total GPU memory.

**Note**

The available GPU types are subject to those displayed on the page. View the data for Allocated, Not Aallocated resources, Total, and Allocation Rate. The amount of allocated resources indicates the resources that are allocated to tenants. The amount of unallocated resources indicates the resources in the resource pool. The total amount of resources equals the sum of resources allocated to tenants and resources in the resource pool. Allocation Rate = Resources in the resource pool/(Resources allocated to tenants + Resources in the resource pool) × 100%. Supercomputing resources (number of CPU cores and memory) Select a CPU type from the drop-down list, such as **Intel** or **Hygon**, to view the CPU core quantity of the selected type and total memory.

**Note**

The available CPU types are subject to those displayed on the page. View data for Allocated, Not Aallocated, Total, and Allocation Rate. The amount of allocated resources indicates the resources that are allocated to tenants. The amount of unallocated resources indicates the resources in the resource pool. The total amount of resources equals the sum of resources allocated to tenants and resources in the resource pool. Allocation Rate = Resources in the resource pool/(Resources allocated to tenants + Resources in the resource pool) × 100%. Storage resources Select a storage resource type from the drop-down list, such as **APFS** or **CPFS**, to view the utilization of storage resources of the selected type. View the data for **Used**, **Allocated**, **Total**, and **Utilization** of storage resources.

**Computing power dashboard**

This dashboard displays data for GPU Computing Power and CPU Computing Power. GPU Computing Power (Unit: TFLOPS) Select a GPU type from the drop-down list to view the data of GPU computing power of the selected type. The time range is not configurable. The dashboard displays the total computing power, allocated computing power, and distribution rate within the last week and of the current day. CPU Computing Power (Unit: TFLOPS) Select a CPU type from the drop-down list to view the data of CPU computing power of the selected type. The time range is not configurable. The dashboard displays the total computing power, allocated computing power, and distribution rate within the last week and of the current day.

**Note**

CPU computing power refers to the computing power of supercomputing CPUs, excluding the computing power of CPUs in intelligent computing clusters. GPU computing power refers to the computing power of intelligent computing GPUs, excluding the computing power of GPUs in supercomputing clusters.

**Control services**

The Control Services module displays the status: **Abnormal** or **At Desired**, of computing, networks, and storage control services. **Abnormal** indicates that the service deployment has not been completed. **At Desired State** indicates that the service has been deployed.

## Visualized monitoring

### Job Path Analysis

This section describes how to use job path analysis.

**Limits**

Only Hygon DCUK100-AI, ZW810E, Kunlun P800, METAX C550, Moore Threads S5000, and NVIDIA T4, A2, A10, and A16 support job path analysis.

**Prerequisites**

The cluster running the task must have the ai-task-inspector component installed. If it is not installed, install **Container O&M Service** via **BMCP > Cluster Management > Software**
**Instances**.

**Note**

You can initiate tasks through many products, such as PAI or AI Studio. As long as the task consumes GPU resources on BMCP nodes, you can use the job path analysis feature.
1. Log on to the BMCP Operations Platform.
2. In the left-side navigation pane, click **Visualized Monitoring > Job Path Analysis**.
3. On the **Job Path Analysis** page, use filters to locate a **Job ID**. After selection, click
**Search**.

**Note**

First, select**Start And End Time**. You can query tasks up to seven days before the current time.
**Node ID** is optional. If you select a **Node ID**, the system automatically populates
the **Cluster ID** field with the cluster where that node resides.
**Cluster ID** and **Namespace** are required. Finally, select a **Job ID**.
**Job Information** is collapsed by default. Click the
icon on the left to expand it. Job information includes job status, occupied resources, and job start/end times.
4. Click **Job Details**. The right panel expands to show **Basic Information** and node runtime
information. On the **Basic Information** page, view the **Job status**, **Number of nodes**, **Number of**
**GPU cards**, **CPU resources**, **Memory resources**, and the job lifecycle.
Node runtime information includes **Node ID/Name**, **Online Status**, **Node Type**, **SN**, and **Cluster**.
5. In the **Job view** area, select a **time slice**. The canvas below displays the job’s topology and
resource utilization for that time slice. Topology includes components such as GPU cards, RDMA cards, switches, and their interconnections. Resource metrics include GPU utilization and RDMA NIC bandwidth usage.

**Note**

When you hover your mouse over a GPU card, RDMA card, or other component, the system displays its specific name and resource utilization.

## Alerts

### Resource event alert

The resource event alert monitors stability metrics for computing resources, including nodes, GPUs, RDMA software stack, and others. It issues real-time alerts for exceptions. This document describes how to view and handle resource event alerts (including compute and storage resources).

**Prerequisites**

Deploy CloudMonitor (CMS) and ensure it reaches the desired state.

**Note**

Resource event alert depends heavily on CMS. Confirm that CMS is deployed and has reached the desired state before use.
1. Log on to the BMCP Operations Platform.
2. In the left-side navigation pane, click **Alerts**.
3. On the **Resource Event Alert** page, view the alert list within the site.
By default, you enter the **Calculation** tab.
4. View and handle **Calculation** alerts.
i. You can filter alerts by **Alert Level**, **Alert Status**, **Alert Source**, and **Alert ID**. Click
**Advanced filter** to combine filters using **Alert ID**, **Alert Name**, and **Alert Start Time**.

**Note**

Alert levels include: **P1 emergency, P2 is serious, P3 Warning, P4 hint.** Alert statuses include **: Processed, Unprocessed.** Alert sources include: **Calculation (in-band), Calculation (out-of-band),**

**Network.**

ii. For alerts with status **Unprocessed**, click **Add event ticket** to handle them. When you click **Add event ticket**, select **Processing Method**, enter **Handler** and
**Reason for closing**, then click **OK**.

**Note**

Processing methods include Ignore (the alert requires no action) and Fixed (the fault corresponding to the alert has been resolved).
5. Click the **Storage** tab to view and handle **Storage** alerts.
i. You can filter alerts by **Alert Level**, **Alert Status**, **Alert Name**, **Alarm Content**, and
**Alert Start Time**. You can also click **Advanced filtering** to combine filters using **Alert**
**Name**, **Alarm Content**, and **Alert Start Time**.

**Note**

Alert levels include: **P1 emergency, P2 is serious, P3 Warning, P4 hint.** Alert statuses include **: Processed, Unprocessed.** Alert sources include: **Calculation (in-band), Calculation (out-of-band),**

**Network.**

ii. Click an alert ID to go to the **Alert details** page to view detailed alert information and handle the alert according to business needs. For more alert information, see the section **Alert list** in **Apsara Uni-manager**
**Operations Console User Guide**.

### Job event alert

A job event alert refers to failover events that occur on all compute nodes occupied by a task during its runtime. This document describes how to view job alerts.

**Limits**

Job event alert supports only **ACK - Intelligent Computing Cluster** .
1. Log on to the BMCP Operations Platform.
2. In the left-side navigation pane, click **Alerts**.
By default, the system navigates to the **Resource Event Alert** tab.
3. Click the **Job Event Alert** tab, select **Cluster ID**, **Namespace**, and **Job ID**, and then click
**Search**. The **Job Event Alert** displays all associated alerts generated during the lifecycle
of the job.

## Clusters

### Computing

#### Clusters

##### Query the details of a computing cluster

This topic describes how to query the details of a Bare Metal Computing Platform (BMCP) cluster, including the basic information, nodes, and operation logs of the cluster. You can query the details of a bare metal-intelligent computing cluster, ACK-intelligent computing cluster, bare metal-supercomputing cluster, or converged computing cluster.

**Prerequisites**

A BMCP cluster is created in the Apsara Uni-manager Operations Console.
1. Log on to the BMCP Operations Platform.
2. In the left-side navigation pane, choose **Clusters**.
3. Choose **Computing > Cluster**.
This tab displays computing clusters owned by all tenants in the site.
4. Query computing clusters:
Basic query: a. Search for clusters by cluster ID or cluster name or select Automatic Recognition. b. Click the icon to search for clusters in fuzzy match mode. Advanced filtering: a. Click **Advanced Filter**. b. Search for clusters by keyword-based automatic recognition, or specify the **Cluster ID** and **Cluster Name**. c. Click **Search** to search for clusters that match the specified conditions in fuzzy match mode.
5. Click **Details** in the **Actions** column of the desired cluster to view **Basic Information**,
**Cluster Node**s, **Monitoring**, and **Operation Logs** of the cluster.
i. **Basic Information** The following table lists the information on the Basic Information page.

| Section | Description |
|---|---|
| Basic Information | This section displays cluster information such as Cluster ID, Cluster Name, Cluster Status, Nodes, and Created At. |
| Configuration Information | This section displays the Cluster Instance Type, CPU Cores, Memory (GB), GPU Memory (GB), and Computing Power (TFLOPS). |
| Storage Information | This section displays the high-performance storage status. |

ii. **Cluster Nodes** Click the **Cluster Node**s tab to view bare metal nodes allocated to this cluster. You cannot view Elastic Compute Service (ECS) nodes in the cluster. You can view node information, such as **Node Name/ID**, **Online Status**, **SN**, **Node IP Address**, and
**Model**. You can click **Details** in the **Actions** column of a node to view its details. For
more information, see View the details of a computing node. iii. **Monitoring** Click the **Monitoring** tab to view the monitoring information of the cluster, such as Memory Usage, Cluster Load, and Connections. iv. **Operation Logs** Click the Operation Logs tab to view the operation logs of the cluster. You can view the historical operation logs of the cluster by operation type and operation time. a. Select an option from the **Operation Type** drop-down list, such as Create Cluster, Delete Cluster, Scale out Cluster, or Scale in Cluster, to search for operation logs of the specified operation type. If you do not select an operation type, operation logs of all operation types will be displayed. b. Specify **Start Date** and **End Date** (accurate to seconds). Then, operation logs from the start date to the end date will be displayed. c. Click **Operation Details** in the Actions column to view atomic steps in the operation and the detailed information.

#### Nodes

##### Query the details of a computing node

This topic describes how to query Bare Metal Computing Platform (BMCP) computing nodes and their details, including basic information and operation logs. You can query nodes in bare metal-intelligent computing clusters, ACK-intelligent computing clusters, bare metalsupercomputing clusters, converged computing clusters, as well as unassigned nodes in the resource pool.
1. Log on to the BMCP Operations Platform.
2. In the left-side navigation pane, choose **Clusters**.
3. Choose **Computing** > **Nodes**.
This tab displays computing notes owned by all tenants and computing nodes in the resource pool.
4. Query computing nodes:
Basic query: a. Search for nodes by node ID, node name, SN, cluster ID, subnet IP address, Virtual Private Cloud (VPC) IP address, or out-of-band IP address. b. Click the icon to search for nodes in fuzzy match mode. Advanced filtering: a. Click **Advanced Filter**. b. Specify the Node ID, Node Name, SN, Cluster ID, Subnet IP Address, VPC IP Address, and Out-of-band IP Address filter conditions at the same time. c. Click **Search** to search for nodes that meet the specified conditions in fuzzy match mode.
5. Click **Details** in the **Actions** column of the desired node to view **Basic Information**,
**Monitoring**, and **Operation Logs** of the node.
i. Basic Information The following table lists the information displayed on the Basic Information tab.

| Section | Description |
|---|---|
| Basic Information | This section displays Node ID, Node Name, SN, Region, Zone, and other items. |
| Configuration Information | This section displays node hardware information, including CPU, GPU, Operating System, Network, NIC, and Disk. |

ii. Monitoring The **Monitoring** tab displays the node monitoring data, including CPU Utilization, Memory Usage, Load, and Connections. iii. Operation Logs You can filter the historical operation logs for the node by operation type. a. Select one of the following options from the **Operation Type** drop-down list: Apply for Instance, Regitser Again, O&M Instance, Attach Instance, Mount Storage, Unmount Storage, Request Error, and more. If you do not select a filter condition, operation logs of all types for the node will be displayed. b. Specify **Start Date** and **End Date** (accurate to days). Then, operation logs from 00:00:00 of the start date to 23:59:59 of the end date will be displayed. c. Click **Operation Details** in the **Actions** column to view all atomic steps included in the operation and the detailed information.

### Storage

**View storage cluster details**

1. Log on to the BMCP Operations Platform.
2. In the left-side navigation pane, click **Resource Management**.
3. On the **Resource Management** page, click the **Storage** tab.
By default, you enter the **Storage** tab.
4. View information such as the **Health status**, **Disk type**, **File system type**, and **Number**
**of nodes** for the cluster.
5. Find the target cluster.
You can enter the **Cluster ID** in the search box in the upper-right corner of the cluster list to perform an exact query.
6. Click the cluster ID of the target cluster or click **Details** in the **Operation** column to view
detailed information about the cluster. On the **Cluster Details** tab, view information such as the **Number of file systems**,
**Number of nodes**, **File system type**, **Health status**, and **Disk type**.
On the **Cluster Node** tab, view information such as the **Management IP**, **SN**, **Model**,
**CPU architecture**, and **Memory** of nodes.
You can perform an exact query by using the **Node Name**. On the **Service** tab, view service roles and their statuses. You can perform a fuzzy query by using the **Service Name**. You can click **Tianji O & M** in the **Operation** column of the target service role to go to the **Apsara Infrastructure Management** platform and manage the service role. On the **Monitoring** tab, view monitoring metrics including read bandwidth, write bandwidth, and read IOPS.

**View client cluster details**

1. On the **Storage** tab, click **Client cluster**.
View information such as the **Cluster Status**, **Cluster Type**, **Number of nodes**, **Quorum**
**nodes**, and **Mount a file system**.
2. Find the target cluster.
You can enter the **Cluster Name** in the search box in the upper-right corner of the cluster list to perform an exact query.
3. Click the **Cluster Name** of the target cluster or click **Details** in the **Operation** column to
view detailed information about the cluster. On the **Cluster Details** tab, view the number of nodes, number of quorum nodes, and basic information of the cluster. On the **Cluster Node** tab, view basic information such as the **Node Type** and **Node**
**status**.
You can also click **Details** in the **Operation** column of the target node to view View cluster node details.

### Network

#### Query subnets

This topic describes how to query and update the information about all switches connected to the cloud.
1. Log on to the Bare Metal Computing Platform (BMCP) Operations Console.
2. In the left-side navigation pane, click **Clusters**.
3. Click the **Network** tab.
This tab displays all switches connected to the cloud, including **HSW** and **CHSW**. You can view the following information about each switch: **Subnet name**, **IP range**, **Gateway**,
**Description**, and **Update Time**.
4. In the upper part of the page, specify **Subnet name** to perform a **fuzzy search**.
5. Click **Get subnet** to query the switches that are connected to the cloud in real time and
synchronize the information to the current page.

## Resource management

### Computing

#### Servers

##### View server details

This topic describes how to query all physical servers and view their detailed information.
1. Log on to the Bare Metal Computing Platform (BMCP) Operations Console.
2. In the left-side navigation pane, click **Resource management**.
By default, the **Calculation > Server** tab is displayed. You can view all physical servers on this tab.
3. Query servers:
Basic filtering: a. You can query servers by hostname, SN, or model or select a tag from the drop-down list. b. Click the icon to search servers in fuzzy match mode. Advanced filter: a. Click **Advanced Filter**. b. Specify the hostname, SN, and model at the same time. c. Click **Search** to search servers in fuzzy match mode.
5. Click **Details** in the Operation column of the desired server to view **Basic Information**,
**Monitoring**, and **Operation Log** of the server.
i. Basic information The following table lists the information displayed on the Basic Information page.

| Section | Description |
|---|---|
| Basic Information | This section displays information such as Resource ID, Resource Name, SN, Region, and Zone. |
| Configuration Information | This section displays the hardware information of the server, such as Model, CPU, GPU, Operating System, Network, Nic information, and Disk information. |

ii. Monitoring On the **Monitoring** tab, you can view the CPU utilization, memory utilization, loads, disk reads, disk writes, and number of connections within the specified time period. iii. Operation Log On the **Operation Log** tab, you can filter operation logs by operation type and operation time. a. You can select a tag from the **Operation Type** drop-down list to filter **operation logs**. You can select the following tags: Apply for an instance, Re-apply, O & M instance, Mount instance, Mount storage, and Unmount storage. If you do not select a filter condition, **operation logs** of types of operations that have been performed on the server are displayed. b. Click **Operation Time**, and specify **Start Date** and **End Date** (accurate to days). Then, **operation logs** from 00:00:00 of the start date to 23:59:59 of the end date are displayed. c. You can click **Operation details** in the Operation column to view all atomic steps included in the operation and the detailed information.

##### Register server resources

This topic describes how to register server resources.
1. Log on to the BMCP Operations Platform.
2. In the left-side navigation pane, choose **Resource management**.
By default, the **Computing > Servers** tab is displayed, where you can view all physical servers in the site.
3. Click **Register Resource** above the list.
4. In the **Select an access mode** dialog box, configure parameters listed in the following
table..

| Parameter | Description |
|---|---|
| Access Mode | The access mode. Valid values: Access over CHSW Access over HSW |
| Resources To be Managed | The resource to be managed. |

5. Click **OK**.
6. In the displayed **Register Resource** panel, perform the following operations:
i. In the **Basic Information** section, configure the following parameters:
**Region** and **Zone**
ii. In the **Resources** section, configure the parameters described in the following table.

| Parameter | Description |
|---|---|

| Resource Type | The type of the resource. Valid values if you select Access over CHSW: High-Performance Computing Management: A standard image provided by the platform is used to initialize and start bare metal instances. Intelligent Computing Management: A standard image provided by the platform is used to initialize and start GPU-accelerated bare metal servers in AI scenarios. Valid values if you select Access over HSW: Intelligent Computing Management: A standard image provided by the platform is used to initialize and startGPU-accelerated bare metal instances in AI scenarios. In-band Management: Start CPU-accelerated bare metal instances without modifying their original operating systems. High-Performance Computing Management: A standard image provided by the platform is used to initialize and start GPU- accelerated bare metal instances in high-performance computing scenarios. |
|---|---|
| Architecture | The CPU architecture of the resource. Valid values: x86 64 _ aarch64 sw 64 _ |
| Model | The model of the resource. If no model is available, add a model first. |
| SN | The serial number of the resource. The value must be 2 to 128 characters in length and can contain periods (.), underscores ( ), _ hyphens (-), and colons (:). The name cannot start with a special character. This parameter is not required if you select Access over CHSW. |
| Device Model | The device model. The value must be less than 128 characters in length and can contain letters and digits. This parameter is not required if you select Access over CHSW. |
| Data Center | The data center in which the resource is deployed. The value must be less than 128 characters in length and can contain letters and digits. This parameter is not required if you select Access over CHSW. |
| Room | The room in which the resource is deployed. The value must be 2 to 128 characters in length and can contain letters, digits, hyphens (-), and underscores ( ). Example: 1-1-1. _ This parameter is not required if you select Access over CHSW. |

| Rack | The rack in which the resource is deployed. The value must be 3 characters in length. It must start with an uppercase letter and end with an integer in the range of 01 to 24. Example: F02. This parameter is not required if you select Access over CHSW. |
|---|---|
| Rack Number | The rack number. The value must be a positive integer in the range of 1 to 48. This parameter is not required if you select Access over CHSW. |
| Warranty Period | The time period during which maintenance is performed. |

iii. In the **Image** section, configure the parameters described in the following table.

| Parameter | Description |
|---|---|
| Image Type | The type of the image. Valid values: Public Image and Custom Image. |
| Public/Custom Image | The image that you want to use. |

iv. In the **Network** section, configure the parameters described in the following table.

| Parameter | Description |
|---|---|
| Physical Machine Gateway | The physical machine gateway. This parameter is not required if you select Access over CHSW. |
| Physical Machine Gateway Port | The port of the physical machine gateway. This parameter is not required if you select Access over CHSW. |
| Subnet | The subnet that you want to use. This parameter is not required if you select Access over CHSW. |
| Subnet IP Address | The IP address that belongs to the subnet. This parameter is not required if you select Access over CHSW. |
| Out-of-band Information | By default, you do not need to specify the out-of-band information. To specify the out-of-band information, select Show. |
| Out-of-band IP Address | The out-of-band IP address. This parameter is required only if you select Expand for Out-of-band Information. |
| Out-of-band Username | The out-of-band username. This parameter is required only if you select Expand for Out-of-band Information. The value must be 2 to 128 characters in length. It must start with a letter and can contain digits and special characters, including ~ ! @ # $ % ^ & * () - = + \| [ { } ] ; : . _ |
| Out-of-band Password | The out-of-band password. This parameter is required only if you select Expand for Out-of-band Informationr. The value must be 1 to 128 characters in length. |

v. In the **Configure Password** section, configure the parameters described in the following table.

| Parameter | Description |
|---|---|
| Login Username | The username used to log in to the resource. The default value is root, which cannot be changed. |
| Login Password | The password used to log in to the resource. It must be 8 to 30 characters in length, and must contain at least three types of the following characters: uppercase letters, lowercase letters, digits, and special characters. Supported special characters include ( ) ` ~ ! @ # $ % ^ & * - + = \| { } [ ] : ; ' < > , . ? /. _ |
| Confirm Password | You need to enter the login password again. The value of this parameter must be consistent with that of the Login Password parameter. Important Remember the password you set. If you forget it, you can log on to the BMCP Operations Console to reset it.. |

vi. In the **Resource Name** section, configure the parameters described in the following table.

| Parameter | Description |
|---|---|
| Resource Name | The name of the resource. It must be 2 to 128 characters in length, and can contain letters, digits, hyphens (-), and periods (.). The name must start with a letter or digit. This parameter is not required if you select Access over CHSW. |
| Hostname | The hostname. This parameter is not required if you select Access over CHSW. |
| Resource Description | The description of the resource. It must be 0 to 1,000 characters in length. |

7. After you complete the configurations, click **OK**.

**Note**

If change authorization is enabled, you must contact the authorization administrator of the Apsara Uni-manager Operations Console to complete the approval in **Platform**
**Operation > Task Center > Task List** before the resource can be successfully
registered.

##### Manage servers

This topic describes how to start, restart, stop, delete, and initialize servers.

**Prerequisites**

The server **Resource owner** is **Resource Pool**.
1. Log on to the BMCP Operations Platform.
2. Choose **Resource managemen**t.
By default, you enter the **Computing** > **Servers** tab. This page displays all physical servers in the site.
3. Filter for your target server.
4. In the **Actions** column of the target server, click **Resource Status**.
You can start, restart, stop, delete, or release a single resource.

| Operation status | Power status | Available operations |
|---|---|---|
| Not Initialized, The system is reset. | Irrelevant | Initialize Resource |
| Complete | Shut Down | Start Resource, Delete Resource |
| Complete | Start Up | Restart Resource, Stop Resource, Delete Resource |

5. Select one or more servers, then click **Delete Resource** or **Initialize Resource** at the
bottom of the server list.

**Note**

If change authorization is enabled, you must contact the authorization administrator of the Apsara Uni-manager Operations Console to complete the approval in **Platform**
**Operation > Task Center > Task List** before the resource can be successfully deleted.

##### Remotely log on to a server

This topic describes how to remotely log on to a server.

**Prerequisites**

The server to which you want to log on is running.
1. Log on to the Bare Metal Computing Platform (BMCP) Operations Console.
2. In the left-side navigation pane, click **Resource management**.
By default, the **Calculation > Server** tab is displayed. You can view all physical servers on this tab.
3. Filter servers.
4. Find the desired server and click **Remote logon** in the **Operation** column.
5. In the dialog box that appears, enter the password and click **OK**.

##### Re-register a server

This topic describes how to re-register servers.
1. Log on to the Bare Metal Computing Platform (BMCP) Operations Console.
2. In the left-side navigation pane, click **Resource Management**.
3. On the **Resource Management** page, click the **Calculation** tab.
You can view all physical servers on this tab.
4. Find the desired server, click the
icon, and click **Re-register**.
5. In the **Re-register** panel, specify the basic information, resources, image, network,
password, and resource name settings. i. In the **Basic Information** section, specify **Region** and **Zone**. ii. In the **Resources** section, specify **Resource Type**, **Architecture**, **Model**, **SN**,
**Equipment model**, **Data Center**, **Room**, **Cabinet**, **SN**, **Rack unit number**, and
**Maintenance time**.
iii. In the **Image** section, specify the image type and image. iv. In the **Network** section, specify **Physical machine Gateway**, **Physical machine**
**gateway port**, **Subnet**, **Subnet IP**, and **Out-of-band information**.
v. In the **Configure password** section, specify **Login Password** and **Confirm password**. The password must be 8 to 30 characters in length, and must contain at least three types of the following characters: uppercase letters, lowercase letters, digits, and special characters. Special characters include ( ) ` ~ ! @ # $ % ^ & * _ - + = | { } [ ] : ; ' < > , . ? /.

**Important**

Keep your password confidential. If you lost the password, you can log on to the BMCP Operations Console and reset the password. vi. In the **Resource Name** section, specify **Resource Name**, **Hostname**, and **Resource**
**Description**.

**Note**

The resource name must be 2 to 128 characters in length, and can contain letters, digits, periods (.), and hyphens (-). The name must start with a letter or digit.
6. After you complete the configuration, click **OK**.

##### Enable or disable servers

This topic describes how to enable and disable servers.

**Prerequisites**

The **Resource Owner** of the server is **Resource Pool**.

**Enable servers**

1. Log on to the BMCP Operations Platform.
2. In the left-side navigation pane, click **Resource management**.
By default, the **Computing** > **Servers** tab appears. This tab displays all existing physical servers within the site.
3. Find the server for which **Resource Availability** is **Disable**.
4. Select a method to enable servers.
**Enable a single server**: Click the
icon in the **Actions** column of the server, choose
**Resource Availability** > **Enable**.
**Batch enable servers**: Select the checkboxes of multiple servers, then click **Enable**
**Resource** at the bottom of the server list.
5. In the dialog box that appears, click **OK**.

**Disable servers**

**Important**

After a server is disabled, it cannot be added to clusters.
1. Log on to the BMCP Operations Platform.
2. In the left-side navigation pane, click **Resource management**.
By default, the **Computing** > **Server**s tab appears. This tab displays all existing physical servers within the site.
3. Find the server where **Resource Availability** is **Enable**.
4. Select a method to disable servers.
**Disable a single server**: Click the
icon in the **Actions** column of the server, choose
**Resource Availability** > **Disable**.
**Batch disable servers**: Select the checkboxes of multiple servers, then click **Disable**
**Resource** at the bottom of the server list.
5. In the dialog box that appears, click **OK**.

#### GPUs

##### View GPU details

This section describes how to query the list of GPU cards installed on bare metal machines at a site and view detailed information for each GPU card.

**Prerequisites**

You can query GPU cards only after the bare metal machine completes provisioning.
1. Log on to the BMCP Operations Platform.
2. In the left-side navigation pane, click **Resource Management**.
3. On the **Resource Management** page, click the **Calculation > GPU card** tab to enter the
page. This page displays all GPU card resources on provisioned servers at the site.
4. Query GPUs:
Basic query: a. Supports **GPU ID**, **Node**, **GPU model**, or tag selection from dropdown. b. Click to perform a fuzzy search for matching GPU cards. Advanced filter: a. Click **Advanced filter**. b. Supports simultaneous input of GPU ID, Node ID, and GPU model. c. Click **Search** to perform a compound fuzzy search based on selected criteria.
5. View node, server, and GPU card details.
v. Click the node name to view details of the compute node to which the GPU card belongs. vi. Click the server name to view details of the server to which the GPU card belongs. vii. Click **Details** in the **Operation** column for the corresponding GPU card to view its **Basic**
**Information**.
The basic information page includes the following information.

| Information category | Description |
|---|---|
| GPU card information | Includes GPU ID, Node, Server to which the server belongs, Manufacturer, GPU model, Flash storage capacity, Computing power, and other information. |
| Configuration information | Includes VBIOS version, Driver name, Driver version, BusInfo, and other information. |

### Storage

#### View file system details

This topic describes how to view details of a file system resource.
1. Log on to the BMCP Operations Platform.
2. In the left-side navigation pane, click **Resource Management**.
3. On the **Resource Management** page, click the **Storage** tab.
The system displays the **File system** tab by default.
4. You can enter a **File System Name** in the search box above the file system list to filter
results. You can also click **Advanced Filter** and use the **File System Name** field to filter.
5. Click the name in the **Storage Cluster** column for your target file system to view the
storage cluster details. The details include the number of cluster file systems, number of nodes, capacity, health status, file system type, cluster node information, server roles, and monitoring metrics.
6. Click the name in the **Client cluster** column for your target file system to view the client
cluster details. The details include the number of nodes, number of quorum nodes, cluster type, mounted file system path, maximum number of cached files, worker threads, and cluster nodes.
7. Click **Details** in the Operation column for your target file system.
View the file system details, including the file system name, storage cluster, client cluster, specifications, and monitoring metrics.

#### View server resource details

This topic describes how to view server resource details.
1. Log on to the Bare Metal Computing Platform (BMCP) Operations Console.
2. In the left-side navigation pane, click **Resource management**.
3. On the **Resource Management** page, click the **Storage** tab.
By default, the **File system** tab is displayed.
4. Click the **Server** tab.
You can enter a **hostname**, **IP**, or **SN** into the search box above the list to search servers. You can also click **Advanced Filter** and specify the **Hostname**, **IP**, and **SN** filter conditions.
5. Click the ID of the desired server in the **Storage cluster ID** column.
You can then view the storage cluster information of the server, including the number of file systems, number of nodes, capacity, health status, file system type, cluster node information, service roles, and monitoring data.

#### View cache resources of a computing

**node**

This topic describes how to view the cache resources of a computing node.
1. Log on to the Bare Metal Computing Platform (BMCP) Operations Console.
2. In the left-side navigation pane, click **Resource management**.
3. On the **Resource Management** page, click the **Storage** tab.
By default, the **File system** tab is displayed.
4. Click the **Compute Node Cache** tab.
You can enter a **cluster ID** into the search box above the cache instance list to filter cache instances.
5. Click **Details** in the **Operation** column of the desired cache instance.
You can view the detailed information about the cache instance, including **Basic**
**Information**, **worker-related configuration parameters**, and **fuse-related**
**configuration parameters**.
The **Basic Information** section displays information such as **Instance tag**,
**Namespace**, **Read-write type**, **Number of cache nodes**, and **fuse state**.
The **worker-related configuration parameters** section displays information such as
**Service Port**, **Back-end file system**, **Cache Page Size**, and **Back-to-source data**
**block size**.
The **fuse-related configuration parameters** section displays information such as
**Kernel Cache**, **Cache Fragment Size**, **Aggregate fuse request size**, and
**Asynchronous IO type**.

### Network

#### Query network element details

This section describes how to query all network element resources (including DSW, RDSW, HSW, CHSW, EHSW, RASW, etc.) within a site.
1. Log on to the BMCP Operations Platform.
2. In the left-side navigation pane, click **Resource Management**.
The system opens the **Calculation** page by default.
3. Click the **Network > Network Element** tab to view all network element resources within
the site.
4. Enter the relevant information in the **Network element name** or **Management IP**
**addresses** search box to locate the target network element.
5. Click **Details** in the **Operation** column for the corresponding network element to open its
details page.
**Basic Information**: Displays basic information about the network element device,
including its **Network element name**, **SN**, **Manufacturer**, **Role**, and **Network**
**domain**.
**Port**: Displays port information for the network element device, including **Port Name**,
**Port rate**, **Port description**, **Management status**, and **Operation Status**.
**Monitoring**: Displays the **CPU usage** and **Memory usage** of the network element
device.
6. Click **Jump to the network console** in the **Operation** column for the corresponding
network element to view more detailed information about the CPN network element. For more information, see the **CPN Network Element** chapter in **Apsara Uni-manager**
**Operations Console User Guide**.

#### View trace details

This section describes how to query all traces within a site, including switch traces and node traces, to quickly identify abnormal nodes.
1. Log on to the BMCP Operations Platform.
2. In the left-side navigation pane, click **Resource Management**.
The system opens the **Calculation** page by default.
3. Click the **Network > Link** tab to enter the page. This page displays all traces within the
site.
4. Enter the relevant information in the **Link name** search box to query the target trace.
5. Click **Link name** or **Operation** column **Details** to enter the trace details page.
**Link information**: Displays basic trace information such as **Link name**, **Link type**,
**Rate**, and **Management status**.
**Switch port**: Displays port information for this switch, including **Port Name**,
**Equipment**, **Port rate**, **Port description**, **Management status**, and **Operation**
**Status**.
**RDMA Nic Port**: Displays port information for this RDMA NIC, including **NIC name**,
**Node**, **MAC address**, and **Management status**.

## Inspection and diagnostics

### Inspection

#### Diagnose a cluster or node

This topic describes how to diagnose a cluster or node.

**Limits**

Cluster/node diagnostics is supported only for bare metal-intelligent computing clusters (intelligent computing high-bandwidth network instances), ACK-intelligent computing clusters (intelligent computing high-bandwidth network instances and intelligent computing training and inference optimization instances), and converged computing clusters (high-bandwidth network converged instances and basic converged instances) that contain bare metal nodes.

**Important**

If this operation includes time-consuming diagnostic items or stress tests, GPU resources are occupied. Make sure that this operation does not affect your business.
1. Log on to the BMCP Operations Platform.
2. Choose **Inspection and Diagnostics > Inspection**.
The **Clutser/Node Diagnostics** tab is displayed by fault.
3. Click **Create Task**. In the **One-click Diagnostics** dialog box, specify **Task Name**, **Task**
**Type**, and , **Diagnostics Scope**, and select diagnostic items. Click **OK**.
Click a number in the **Subitem** column to view the supported diagnostics items. For more information about diagnostics items, see Description of diagnostic items.

**Manage clutser/node diagnostics tasks**

On the **Cluster/Node Diagnostics** page, you can query and manage clutser/node diagnostics tasks.
1. Query clutser/node diagnostics tasks.
In the list, select a filter and enter the relevant information in the search box. The task list will automatically display tasks that match the search conditions.

**Note**

You can search for diagnostic tasks by **Task ID**, **Task Name**, and **Start and End**
**Time**.
You can also click **Advanced Filter** to specify multiple filter criteria for progressive filtering, which allows you to quickly locate the target diagnostic tasks.
2. Cancel a diagnostics task.
Locate a diagnostics task in the **Running** state and click **Cancel** in the **Actions** column.
3. View diagnostics details.
Locate a diagnostics task in the **Complete** state and click **Details** in the **Actions** column.

#### Job diagnosis

This section describes how to diagnose clusters involved in job tasks.

**Limits**

Job diagnosis supports only **Bare Metal** node-based **Container-intelligent Computing**
**Power Cluster**.

**Create a job diagnostic task**

**Important**

If this detection includes time-consuming diagnostic items or stress tests, it occupies GPU resources. Make sure that this operation does not affect your business.
1. Log in to the BMCP O&M platform.
2. In the left-side navigation pane, select Inspection and Diagnostics**Inspection and**
**Diagnostics > Inspection**.
By default, the **Cluster/node diagnosis** tab appears.
3. Click the **Job diagnosis** tab.
4. Click **Create a task**. In the **One-click diagnosis** dialog box, set the **Task name**, select
the **Cluster ID**, **Namespace**, **Job ID**, and **Diagnostic items**, then click **OK**. Click the number in the **Sub-item** column to view the currently supported diagnostic items.

**Manage job diagnostic tasks**

You can query and manage **Job diagnosis** tasks on the **Job diagnosis** page.
1. Query the **Job diagnosis** task list.
Click **Advanced filter**, then select the **Cluster ID**, **Namespace**, and **Job ID** to find diagnostic tasks.
2. Cancel a diagnostic task.
For any task with the status **Running**, click **Cancel** in the **Operation** column.
3. View diagnostic details.
After the diagnostic task status changes to **Completed**, click **Details** in the **Operation** column to view the diagnostic results.

#### Diagnostic item description

The diagnosis feature provides cluster, node, and job diagnostics. This document describes the supported diagnostic items in detail.

**System health diagnosis**

| Diagnostic item | Description |
|---|---|
| Resource QoS diagnosis | The container engine containerd has an exception. The ctr command times out or hangs. |
| DNS setting check | Check the DNS configuration in /etc/resolv.conf on the physical machine. |
| NIC uplink port wiring mapping check | Confirm whether the correspondence between each server NIC port and switch port is correct. |

**Network performance diagnosis**

| Diagnostic item | Description |
|---|---|
| NIC rate compliance check | Check and ensure that the NIC rate complies with system requirements. |
| BOND port check | Check the status and configuration of network bonded ports. |
| NIC-to-GPU connection relationship check | Verify that the connection topology between NIC and GPU is correct. |
| Bonding module check | Check whether the bonding network module is correctly installed. |
| OS distribution | Check the operating system distribution. |
| OS kernel version | Check and ensure that the kernel version complies with system requirements. |
| RDMA device aggregation hash policy | Check the aggregation hash policy configuration for RDMA devices. |
| RDMA QOS _ configuration check | Check and optimize the RDMA Quality of Service configuration. |
| RDMA device count | Check whether the number of RDMA devices meets expectations. |
| RDMA device name and status | Check the name and operational status of RDMA devices. |
| RDMA device aggregation mode | Check the aggregation mode configuration for RDMA devices. |
| RDMA device MTU setting | Check and optimize the MTU setting for RDMA devices. |
| RDMA device port rate | Check whether the RDMA device port rate meets performance requirements. |
| RDMA device aggregation status | Check the aggregation status of RDMA devices. |

| MLX LAG mode check | Check and confirm the MLX LAG mode configuration. |
|---|---|
| PCIe link rate and width consistency check | Check the consistency of PCIe link rate and width. |
| RDMA device firmware version consistency check | Check the consistency of RDMA device firmware versions. |
| RDMA NIC driver loading | Check whether the RDMA NIC driver loads correctly. |
| PCIe MRR configuration | Check the PCIe MRR configuration. |
| GDR module loading | Check whether the GDR module loads correctly. |
| LLDP service running status | Check the running status of the LLDP service. |
| NVIDIA FABRIC MA _ _ NAGER service running status | Check the running status of the NVIDIA Fabric Manager service. |
| PCIe link rate and width downgrade check | Check and fix any PCIe link rate or width downgrade issues. |
| Uplink switch and port name check | Check the configuration of uplink switch and port names. |
| alixpu peermem _ status check | Check the loading status of the alixpu peermem module and reload it if _ necessary. |
| XDR module installation check | Verify the integrity of the XDR module installation and reinstall it if necessary. |
| APG ICN status check | Check for APG ICN abnormal status and restart related services if necessary. |
| GPU card drop | Check whether any GPU cards are dropped. |

| Check IB NIC order | Check whether the IB NIC order meets expectations. |
|---|---|
| PCI ACS status check | Enable the PCI ACS feature and reconfigure virtualization settings. |

**Gpu diagnostic**

**Note**

Diagnostic items relate to the graphics card. Refer to the interface display for the specific supported diagnostic items.

| Diagnostic item | Description |
|---|---|
| System environment check | Check and fix GPU device drivers, firmware, core services, kernel data interfaces, environment variables, and runtime libraries. |
| Network device check | Check and update network device drivers and firmware to ensure they meet high network requirements. |
| Historical fault screening | Analyze and handle historical faults recorded by the system. |
| GPU device presence status check | Check and ensure that GPU devices are properly present. |
| GPU uplink speed check | Check and handle any speed or lane reduction issues in GPU uplink and interconnect. |
| Device operating condition check | Check and handle abnormal states of GPU devices, such as overheating, frequency reduction, and severe memory faults. |
| DCGM fault diagnosis | Run DCGM Level 2 to Level 4 diagnostic programs to check and handle device abnormal states. |
| Device capability attribute check | Check and confirm whether GPU devices support advanced features such as GRDMA. |
| GPU memory bandwidth test | Test and analyze H2D, D2H, and D2D bandwidth performance of the GPU. |
| GPU peer-to-peer communication test | Test and evaluate the efficiency of peer-to-peer communication between GPU devices. |

| Black Scholes algorithm simulation | Use the Black Scholes algorithm to evaluate GPU computing performance. |
|---|---|
| Gravity body simulation | Test the GPU computing power limit through million-body gravity simulations. |
| CUDA matrix multiplication test | Check and optimize data accuracy and performance of CUDA matrix multiplication. |
| CuBLAS matrix multiplication test | Check and optimize data accuracy and performance of CuBLAS matrix multiplication. |
| GPU stress test | Perform long-duration stress tests on the GPU to check device stability. |
| HBM memory stress test | Check the performance and stability of HBM memory. |
| GPU data copy accuracy test | Verify the accuracy of GPU data copying. |
| GPU data copy performance test | Test and optimize GPU data copy performance. |
| Kernel function execution performance test | Analyze and improve kernel function launch and execution latency. |
| General matrix multiplication floating-point performance test | Test matrix multiplication performance for different data types. |
| cuDNN common function performance test | Test and optimize performance of common cuDNN functions. |
| cuBLAS common function performance test | Test and optimize performance of common cuBLAS functions. |
| Single-GPU matrix multiplication performance test | Test and optimize large matrix multiplication performance on a single GPU. |

| Multi-GPU matrix multiplication performance test | Test and optimize large matrix multiplication performance across multiple GPUs. |
|---|---|
| Compute- communication overlap performance test | Test the GPU’s ability to overlap computation and communication. |
| NCCL communication performance test | Test and optimize NCCL collective communication performance. |
| HIP GPU memory bandwidth test | Test and analyze H2D and D2H bandwidth performance of HIP-based GPUs. |
| HIP device feature attribute check | Check and confirm the feature attributes of GPU devices. |
| HIP device basic attribute check | Check the basic attributes of GPU devices. |
| HIP bus bandwidth test | Use the zero-fraction algorithm to test GPU bandwidth anomalies. |
| HIP device peer-to- peer communication check | Check whether peer-to-peer communication between GPU devices is enabled. |
| HIP HelloWorld kernel function test | Verify that the device can correctly execute the HelloWorld kernel function. |
| HIP matrix multiplication test | Test data accuracy of HIP matrix multiplication. |
| Compute core stress test | Stress test DCU compute cores and record temperature and power consumption curves. |
| Memory stress test | Stress test DCU memory and record temperature and power consumption curves. |
| Component stress test | Simultaneously stress test DCU memory and compute cores, and record temperature and power consumption curves. |
| PCIe bandwidth test | Test DCU PCIe bandwidth. |

| XHMI bandwidth test | Test DCU XHMI bandwidth. |
|---|---|
| HBM bandwidth test | Test DCU HBM bandwidth. |
| Balanced computing power test | Test FP64, FP32, FP16, INT8, and INT4 balanced computing power values of the DCU. |
| RCCL communication performance test | Test RCCL collective communication efficiency and bandwidth performance. |
| HBM bidirectional DMA test | Test correctness and speed of bidirectional DMA between host and device HBM. |
| L3 cache bidirectional DMA test | Test the correctness and speed of bidirectional DMA between host and device L3 cache. |
| Job execution test | Verify the device’s ability and efficiency to execute computing tasks. |
| Single-host GPU-to- GPU memory copy test (AUTO mode) | Test single-host GPU-to-GPU memory copy efficiency, balancing performance and accuracy. |
| Single-host GPU-to- GPU memory copy test (UNIT mode) | Test the accuracy of single-host GPU-to-GPU memory copying. |
| Single-host GPU-to- GPU memory copy test (PERF mode) | Test the performance of single-host GPU-to-GPU memory copying. |
| Peak power consumption test | Test peak power consumption of XPU devices and monitor temperature and power changes. |
| Dynamic power consumption test | Test dynamic power consumption changes of the XPU. |
| Global memory availability test | Test the availability of XPU global memory. |
| XPU Link functionality test | Verify the functional availability of XPU Link. |

| Operator unit test | Execute operator unit tests and count failed unit tests. |
|---|---|
| Global memory read/write test | Test the read/write capability of XPU global memory. |
| XPU Link C2C test | Test the C2C functionality of XPU Link. |
| Dynamic power consumption test | Test dynamic power consumption of PG1. |
| PCIe link performance test | Test memory access performance of PG1, including bandwidth and latency under various scenarios. |
| Floating-point computing power validation | Validate whether the floating-point computing power performance of PG1 meets requirements. |
| GPU memory stress test | Measure performance of the PG1 memory subsystem, including memory bandwidth and latency. |
| Sahara peak power stress test | Extreme power stress test. |
| Sahara stable power stress test | Stable power stress test. |
| Sahara cache stress test | PG1 cache stress test. |
| Sahara SDC stress test | SDC stress test. |
| ICN port status check | Check the ICN port link status of PG1. |
| ICN communication stress test (unidirectional) | Test unidirectional communication performance of ICN. |
| ICN communication stress test (bidirectional) | Test bidirectional communication performance of ICN. |

| PCCL communication performance test | Test PCCL collective communication performance, including bandwidth and communication latency. |
|---|---|
| MXVS floating-point computing power test | Test floating-point computing power performance at different precisions. |
| MXVS unidirectional PCIe link test | Measure unidirectional memory access bandwidth and latency under different scenarios. |
| MXVS bidirectional PCIe link test | Measure bidirectional memory access bandwidth and latency under different scenarios. |
| MXVS unidirectional point-to-point link test | Measure unidirectional point-to-point memory access bandwidth and latency under different scenarios. |
| MXVS bidirectional point-to-point link test | Measure bidirectional point-to-point memory access bandwidth and latency under different scenarios. |
| MXVS MetaX link test | Evaluate inter-GPU bandwidth via MetaXLink. |
| MXVS GPU memory stress test | Test HBM memory bandwidth. |
| MXVS stress test (MetaXLink) | Drive computing power and power consumption above 95% to evaluate GPU stability. |
| MXVS stress test (XCore) | Drive computing power and power consumption above 95% to evaluate GPU stability. |
| MCCL communication performance test | Test MCCL collective communication performance, including bandwidth and communication latency. |
| MUDNN matrix multiplication performance test | Measure GPU floating-point performance using MUDNN matrix multiplication. |
| MUDNN matrix multiplication stability test | Verify GPU functional integrity by checking the correctness of MUDNN matrix multiplication results. |

| MUDNN unary performance test | Memory bandwidth performance test. |
|---|---|
| MUDNN unary stability test | Memory functionality test. |
| MUDNN 2D convolution kernel function test (NCHW) | Test functional completeness of MUDNN 2D convolution kernels (tensor format: NCHW). |
| MUDNN 2D convolution kernel function test (NHWC) | Test functional completeness of MUDNN 2D convolution kernels (tensor format: NHWC). |
| MUDNN 3D convolution kernel function test (NCDHW) | Test functional completeness of MUDNN 3D convolution kernels (tensor format: NCDHW). |
| MUDNN 3D convolution kernel function test (NDHWC) | Test functional completeness of MUDNN 3D convolution kernels (tensor format: NDHWC). |
| MUDNN Flash Attention operator function test | Test functional completeness of the MUDNN Flash Attention operator. |
| GPU memory read/write test | GPU memory read/write test. |
| MCCL communication performance test | Test MCCL collective communication performance, including bandwidth and communication latency. |

**Container health diagnosis**

| Diagnostic item | Description |
|---|---|
| Detect anomalies in the container engine containerd. | The container engine containerd is abnormal. The ctr command times out or hangs. |
| Detect hanging runc processes. | A hanging runc process prevents operations on the corresponding container. |

| Detect memory leaks in shim processes. | A memory leak in a shim process prevents operations on the container. |
|---|---|
| Detect leaked shim processes. | The container is deleted, but the corresponding shim process still exists. |
| Detect leaked runc folders. | The container is deleted, but the corresponding runc folder still exists. |
| Monitor systemd health. | If the machine systemd/dbus hangs, or if the number of mount points exceeds 5000, systemd becomes unresponsive. |
| Detect disk error messages. | Disk error messages in dmesg cause some operations of the container engine to fail. |

## Basic configurations

### Models

#### Add a device model

This topic describes how to add a device model.

**Background information**

You can add **managed intelligent computing**, **In-Band**, and **HPC** device models by clicking **Add model**. The system automatically imports device models of all other types during the Zhuque planning phase.
1. Log on to the BMCP Operations Platform.
2. Click **Basic Configurations > Models**.
3. Click **Add model** in the upper-left corner of the device model list.
4. Configure parameters.

| Configurati on item | Required | Description |
|---|---|---|
| Machine Type | Yes | Select a device model type. Valid values: Intelligent Computing Manged/Manage In-band Manged by High-Performance Computing Note The supported device model types depend on what is displayed in the console of your actual deployment environment. |
| Model Name | Yes | Enter a model name. |
| CPU architecture | Yes | Select a CPU architecture. |
| CPU vendor | Yes | Select a CPU manufacturer. |
| CPU model | Yes | Enter a CPU model. |
| CPU Cores | Yes | Enter the number of vCPUs. |

| Memory | Yes | Enter a memory size. Unit: GB. |
|---|---|---|
| Disk size | Yes | Enter a disk size. Unit: GB. |
| Disk type | Yes | Uppercase letters only. Examples: HDD, SSD, SATA. |
| GPU manufactur er | No | Select a GPU manufacturer. |
| GPU model | No | Select a GPU model. |
| Number of GPUs | No | Enter the number of GPUs. |
| Number of NICs | Yes | Enter the number of NICs. |
| Nic type | Yes | Select the NIC type. |
| Number of U of the machine | Yes | Enter the rack unit (U) size of the machine. |
| Manufactur er name | Yes | The name must be 2 to 128 characters in length, and start with a letter. It can contain numbers and special characters such as underscores ( ), hyphens (-), periods (.), colons (:), and commas _ (,). The name . |
| Server rated power | Yes | Enter the server rated power. |
| Minimum CPU security frequency | No | Enter the minimum CPU security frequency. |
| Description | No | Enter the description. |

5. Click **OK**.

#### Query machine types

This topic describes how to query machine types.
1. Log on to the BMCP Operations Platform.
2. Click **Basic Configuration > Models**.
3. On the machine type list page, you can view existing machine type information.
The machine type information includes **Specifications**, **Model Name**, **Machine Type**,
**Architecture**, **CPU cores**, **CPU vendor**, **CPU model**, **GPU manufacturer**, and **GPU**
**model**.
4. In the filter list, select filter options and enter corresponding information in the search bar.
The machine type list automatically displays machine types that match your search criteria.

**Note**

You can find target machine types by using information such as **Model Name**, **CPU**
**vendor**, **CPU model**, **GPU manufacturer**, and **GPU model**.
You can also click **Advanced Filter** to select multiple filter items progressively for faster machine type lookup.

#### Modify model

This topic describes how to modify a model.
1. Log on to the BMCP Operations Platform.
2. Click **Basic Configuration > Models**.
3. Click **Modify** in the **Operation** column of the target model.
4. In the **Modify model** dialog box, modify the model parameters and click **OK**.

#### Delete a model

This topic describes how to delete a model.

**Warning**

Before you delete a model, make sure that no instances are using this model. The deletion is irreversible.
1. Log on to the BMCP Operations Platform.
2. Click **Basic Configuration > Models**.
3. Click **Delete** in the **Operation** column of the target model.
4. In the confirmation dialog box, click **OK**.

### Images

You can manage custom images and public images on the Bare Metal Computing Platform (BMCP) Operations Console.

#### Custom images

**Upload a custom image**

1. Log on to the Bare Metal Computing Platform (BMCP) Operations Console.
2. In the left-side navigation pane, choose **Basic Configurations > Images**.
By default, the **Custom image** tab is displayed.
3. Click **Custom image upload** in the upper-left corner of the image list.
4. Configure the parameters as described in the following table.

| Parameter | Required | Description |
|---|---|---|
| Region | Yes | The region of the image. |
| Zone | Yes | The zone of the image. |
| Image name | Yes | The image name is automatically generated after you select an image file. |
| System architecture | Yes | The architecture used by the image. |
| Platform | Yes | The OS used by the image. |
| Kernel version | No | The kernel version of the image. |
| Image description | No | The description of the image. |

| Image Upload | Yes | Select the local image file that you want to upload. |
|---|---|---|

5. Click **OK**.

**Manage custom images**

You can **delete**, **enable**, **disable**, and **export** custom images.
1. Log on to the BMCP Operations Console.
2. In the left-side navigation pane, choose **Basic Configurations > Images**.
By default, the **Custom image** tab is displayed.
3. Search for your image by its name or ID in fuzzy match node above the image list.
4. Manage the image:
i. Delete the image a. Click **Delete image** in the **Operation** column of the image. b. In the message that appears, confirm the information and click **OK**.

**Important**

Before you delete an image, make sure that no instances use this image. The delete operation is irreversible. ii. Enable the image Choose **Enable status > Enable images** in the **Operation** column of the image. iii. Disable the image Choose **Enable status > Disable images** in the **Operation** column of the image. iv. Export the image Click **Image export** in the **Operation** column of the image to export the image to your on-premises machine.

#### Public images

You can enable, disable, and export public images and export signature files.

**Manage public images**

You can enable, disable, and export public images.
1. Log on to the Bare Metal Computing Platform (BMCP) Operations Console.
2. In the left-side navigation pane, choose **Basic Configurations > Images**.
By default, the **Custom image** tab is displayed.
3. Click the **Public image** tab.
4. Search for your image by its name or ID in fuzzy match node above the image list.
5. Manage the image:
i. **Enable the image** Choose **Enable status > Enable images** in the **Operation** column of the image. ii. **Disable the image** Choose **Enable status > Disable images** in the **Operation** column of the image. iii. **Export the image** Click **Image export** in the **Operation** column of the image to export the image to your on-premises machine. iv. **Export signature files** Click **Signature File Export** in the **Operation** column of the image to export the signature file to your on-premises machine.

**Verify image integrity**

BMCP allows users to verify the integrity of public images to ensure that they are not tampered with.
1. Log on to the BMCP Operations Console.
2. In the left-side navigation pane, choose **Basic Configurations > Images**.
By default, the **Custom image** tab is displayed.
3. Click the **Public image** tab.
4. Click **Download public key** above the list.
5. Click **Signature File Export** in the **Operation** column of the desired image.
6. You can run the following command to check whether the image has been tampered with:

```
 openssl dgst -sha256 -verify public.key -signature signature.bin imagefile
```

**Note**

Before you run the command, make sure that the public key, signature file, and image are downloaded. Set the following parameters to the actual values: `public.key` indicates the public key. `signature.bin` indicates the signature file. `imagefile` indicates the image file.

### GPU settings

#### Add a GPU

This topic describes how to add a GPU.
1. Log on to the Bare Metal Computing Platform (BMCP) Operations Console.
2. In the left-side navigation pane, choose **Basic Configurations > GPU Settings**.
3. Click **Add GPU** above the list.
4. Configure the parameters as described in the following table.

| Parameter | Require d | Description |
|---|---|---|
| GPU manufacturer | Yes | The GPU vendor name in English. |
| GPU manufacturer (Chinese) | No | The GPU vendor name in Chinese. |
| GPU model | Yes | The GPU model in English. |

| GPU model (Chinese) | No | The GPU model in Chinese. |
|---|---|---|
| GPU memory size | Yes | The size of GPU memory. Unit: GB. |
| TFLOPS | Yes | The TFLOPS. |

5. After you complete the configuration, click **OK**.

#### Query GPU

This topic describes how to query GPU.
1. Log on to the BMCP Operations Platform.
2. Click **Basic Configuration > GPU Settings**.
3. On the **GPU Configuration** page, enter a **GPU model** in the search bar. The system
automatically displays matching GPU configurations in the list. You can also click Advanced Filter, enter a GPU model, and then click Search to find matching GPU configurations.

#### Modify a GPU

This topic describes how to modify the information of a GPU.
1. Log on to the Bare Metal Computing Platform (BMCP) Operations Console.
2. In the left-side navigation pane, choose **Basic Configurations > GPU Settings**.
3. Click **Edit** in the **Operation** column of the desired GPU.
4. Modify the parameters. You can modify the GPU manufacturer (Chinese), GPU model
(Chinese), GPU memory size, and TFLOPS parameters.

**Note**

You cannot modify the GPU manufacturer or GPU model parameter.
5. Click **OK**.

#### Remove a GPU

This topic describes how to remove a GPU.
1. Log on to the Bare Metal Computing Platform (BMCP) Operations Console.
2. In the left-side navigation pane, choose **Basic Configurations > GPU Settings**.
3. Click **Delete** in the Operation column of the desired GPU.
4. Confirm the GPU information and click **OK**.

## Logs

### Cluster and node logs

This topic describes how to collect logs from a cluster, node, or network.
1. Log on to the BMCP Operations Platform.
2. Choose **Logs**.
The **Clutser/Node Logs** tab is displayed by default.
3. Click **Create Task**. Specify **Task Name**, **Log Type**, **Resource Scope**, and **Time Range**.
Click **OK**.

**Note**

When **Log Type** is **Cluster**, the cluster must be a bare metal-intelligent computing cluster, bare metal-supercomputing cluster, converged computing cluster, or ACKintelligent computing cluster that contains bare metal nodes.
4. Locate the task and click **Details** in the **Actions** column to view task details.
5. When the **Log Collection Status** of the task is **Complete**, select the task and click
**Export Logs** to download the compressed log package.

### Job logs

This topic describes how to collect job logs.

**Limits**

Job logs support only **ACK - intelligent computing clusters** that contain **bare metal**
**nodes**.
1. Log on to the BMCP Operations Platform.
2. In the left-side navigation pane, click **Logs**.
The system directs you to the **Cluster/node logs** tab by default.
3. Click the **Job log** tab.
4. Click **Create a task**, set **Task name**, select **Cluster ID**, **Namespace**, and **Job ID**, then
click **OK**.
5. Click **Details** in the **Actions** column of a log collection task to view its details.
6. When the **log collection status** is **Completed**, select the log collection task and click
**Export logs** to download the corresponding compressed log file package.

## Event center

You can manage event tickets in the event center. For example, you can view the basic information about an event ticket, such as the number and status of the event ticket, and review an event ticket.
1. Log in to the Bare Metal Computing Platform (BMCP) Operations Console.
2. In the left-side navigation pane, click **Event Center**.
3. On the upper part of the Event Center page, query event tickets by configuring the
**Incident Ticket Number** parameter.
4. Find the event ticket that you want to manage and click **Approval** in the Operation column.
5. In the **Event Ticket Details** panel, view data in the **Process Information**, **Basic**
**Information**, and **Problem Description** sections.
6. Click **Handle**.
7. In the **Approval** dialog box, select the review result.
i. If you select **Through**, the Please confirm approval. dialog box appears. In the input box, enter **I confirm that I am aware of the operational risks but still wish to**
**proceed.** and click **OK**.
ii. If you select **Refuse**, click **OK**.

**What to do next**

**Repair an event ticket**: After you approve an event ticket, click Details in the Operation
column. In the **Event Ticket Details** panel, click **Repair statement**. In the message that appears, click **OK**. View the details of an event ticket: After you approve an event ticket, click **Details** in the Operation column to view the details of the event ticket.

## Instance operations

The Instance O&M module provides component package management, software stack compatibility table, and upgrade task management features. These features help O&M personnel manage software component version compatibility and perform batch upgrades for bare metal instances.

### Upgrade task management

#### Create an upgrade task

An upgrade task in the BMCP Operations Console is a task unit used to issue new versions of component packages to target bare metal instances for batch upgrading. This topic describes how to create an upgrade task.
1. Log on to the BMCP Operations Platform.
2. Choose **Instance O&M > Upgrade Task Management**.
3. Click **Create Upgrade Task** in the upper-left corner of the task list.
4. In the **Select Machines** step, configure the following parameters:

| Parameter | Required | Description |
|---|---|---|
| Select a Component Package | Yes | Select the component package to be upgraded. The drop-down list displays available component packages in the system. |
| Target machines | Yes | Select the target machines on which the upgrade is to be performed. You can add target machines in the following three ways: Manually Enter: Enter machine SNs in the text box. Separate multiple SNs with commas (,), for example, SN-001,SN-002. After you enter the SNs, click Parse SN to parse and add the machines. Filter Cluster: Select one or more clusters in the cluster list to view the nodes in each cluster (including the SN, node name, status, image, and operating system information). Then, select the target nodes. You can also select all nodes in the current cluster. Import CSV File : Click Download Template to obtain the CSV template file. Fill in the machine information based on the template format, and then drag the CSV file to the upload area or click the upload area to upload the file. |

5. Click **Next**. In the **Canary Release Policy** step, configure the following parameters:

| Parameter | Description |
|---|---|

| Canary Release Mode | Select the canary release mode. The following three modes are supported: Full Delivery: The system dispatches the upgrade task to all target machines at once. By Wave: The system divides the target machines into batches of a fixed size and executes the upgrade batch by batch. By Percentage: The system executes the upgrade in batches based on a percentage of the total target machines. |
|---|---|
| Wave Size | After you select By Wave, configure the number of target machines in each wave. |
| Initial Percentage | After you select By Percentage, specify the percentage of target machines to be upgraded in the first dispatch. The system then gradually increases the percentage until all machines are upgraded. |
| Maximum Concurrency | The maximum number of machines that can be upgraded simultaneously. The system allows multiple waves or batches to run in parallel, but the total number of machines being upgraded at the same time does not exceed this value. |
| Pause upon Single-wave Failure | After this option is enabled, if a wave or batch fails, the system automatically pauses subsequent upgrade tasks. You must manually resume the task to continue. |

6. Click **Confirm Delivery**. In the confirmation dialog box, click **OK**.

#### View the details of an upgrade task

This topic describes how to view the details of an upgrade task.
1. Log on to the BMCP Operations Platform.
2. Choose **Instance O&M > Upgrade Task Management**.
3. Above the upgrade task list, search tasks by **Task ID** or **Bundle Name**.
4. In the upgrade task list, click **Details** in the **Actions** column of the target task.
5. On the upgrade task details page, view the existing upgrade task information.
The upgrade task details include **Task Information**, **Progress Overview**, and **Events**.

#### Pause or resume an upgrade task

This topic describes how to pause or resume an upgrade task.

**Limits**

Pause: The **Status** of the upgrade task is **In Progress**. Resume: The **Status** of the upgrade task is **Paused**.
1. Log on to the BMCP Operations Platform.
2. Choose **Instance O&M > Upgrade Task Management**.
3. In the **Actions** column of the target upgrade task, perform the operation as needed:
i. Click **Pause**. ii. Click **Resume**.

#### Proceed to the next wave of upgrade

**tasks**

This topic describes how to proceed to the next wave of upgrade tasks. After you perform this operation, the system executes the upgrade task on the next batch of target machines.

**Limits**

The **Canary Release Mode** of the upgrade task is **By Wave**. The **Status** of the upgrade task is **In Progress**.
1. Log on to the BMCP Operations Platform.
2. Choose **Instance O&M > Upgrade Task Management**.
3. In the **Actions** column of the target upgrade task, click the
icon, and then click **Poceed**
**with Next Wave**.
4. In the confirmation dialog box, click **OK**.

#### Cancel an upgrade task

This topic describes how to cancel an upgrade task. The cancel operation only stops the tasks that have not been issued.

**Limits**

The **Canary Release Mode** of the upgrade task is **By Wave** or **By Percentage**. The **Status** of the upgrade task is **In Progress**.
1. Log on to the BMCP Operations Platform.
2. Choose **Instance O&M > Upgrade Task Management**.
3. In the **Actions** column of the target upgrade task, click the
icon, and then click **Cancel**.
4. In the confirmation dialog box, click **OK**.

### Component package

**management**

#### Upload a component package

This topic describes how to upload a component package.

**Background Information**

A component package is the fundamental unit for managing and upgrading software components of bare metal instances in the BMCP Operations Console. By uploading custom component packages, you provide the required component versions for subsequent software stack bundles and upgrade tasks.

**Usage Limits**

When you select a component package from a bundle, its version is inherited directly, so you do not need to enter it again. When you upload a component package with the same name, the system displays a prompt, allowing to choose to overwrite the existing file or cancel the upload. During large-file uploads, the pop-up window is blocked and background operation is not supported. Please wait for the upload to complete before closing the pop-up window.
1. Log on to the BMCP Operations Platform.
2. Choose **Instance O&M > Component Package Management**.
3. Click **Upload Component Package** in the upper-left corner of the component package
list.
4. Configure parameters.

| Parameter | Required | Description |
|---|---|---|
| Component Type | Yes | Select the component type: GPU Driver, GPU SDK, or CPN Tool, or enter a custom type. |
| Package Type | Yes | Select the package type: rpm, deb, binary, or tgz. |
| Version | Yes | Enter the component package version. |
| File | Yes | Click Select File to upload the component package file. Alternatively, click Download TGZ Template to obtain the standard template, package your file according to the template format, and then upload it. |
| Description | No | Enter the component package description (up to 256 characters). |

5. Click **OK**.

#### Query component packages

This topic describes how to query component packages.
1. Log on to the BMCP Operations Console.
2. Choose **Instance O&M > Component Package Management**.
3. On the component package list page, view information about existing component
packages. The component package information includes **ID**, **Component Type**, **Type**, **Version**, **File**
**Name**, **Size**, **References**, **Source**, **Founder**, **Created By**, and **Update At**.
4. In the filter list, select a filter and enter the corresponding information in the search bar.
The component package list automatically displays component packages that match the filter conditions.
5. To view the details of a component package, click **Details** in the **Actions** column.
The details panel displays the complete information of the component package, including
**Basic Information** and **Associated Bundle.**

#### Delete a component package

This topic describes how to delete a component package.

**Limits**

Component packages referenced by software stack bundles cannot be deleted. System-preset component packages cannot be deleted.
1. Log on to the BMCP Operations Platform.
2. Choose **Instance O&M > Component Package Management**.
3. Locate the target component package and click **Delete** in the **Actions** column .
4. In the confirmation dialog box, click **OK**.

### Software stack profile

#### Create a bundle

This topic describes how to create a software stack bundle.

**Background Information**

A software stack bundle manages version match relationships among components and defines compatible version combinations across a set of component packages. With the software stack bundle, you can enable consistency detection of component versions on bare metal instances and issue batch upgrade tasks.
1. Log on to the BMCP Operations Platform.
2. Choose **Instance O&M > Software Stack Profile**.
3. Click **Create Bundle** in the upper-left corner of the bundle list.
4. Configure parameters.

| Parameter | Required | Description |
|---|---|---|

| Bundle Name | Yes | Enter a name that is unique across the system for the bundle. |
|---|---|---|
| Image Type | No | Select the image type. Default value: General-purpose Image |
| Description | No | Enter the description of the bundle. |

5. Click **OK**.

#### View the details of a software stack

**bundle**

This topic describes how to view the details of a software stack bundle.
1. Log on to the BMCP Operations Platform.
2. Choose **Instance O&M > Software Stack Profile**.
3. Above the bundle list, enter a bundle name to perform a fuzzy search.
4. In the bundle list, locate the target bundle and click **Details** in the **Actions** column.
5. On the bundle details page, view basic information and the component list.

#### Add components

This topic describes how to add components to a bundle.
1. Log on to the BMCP Operations Platform.
2. Choose **Instance O&M > Software Stack Profile**.
3. In the bundle list, click **Details** in the **Actions** column of the target bundle.
4. Click **Add Component**.
5. Configure the following parameters.

| Parameter | Required | Description |
|---|---|---|
| Component Type | Yes | Select the component type: GPU Driver, GPU SDK, or CPN Tool, or enter a custom type. |
| Associated Component Package | No | Specify whether to associate an uploaded component package. |

| Component Package | Yes | This parameter is displayed when Associate Component Package is set to Yes. Select the component package to associate. |
|---|---|---|
| Component Version | Yes | Enter the version of the component package. The default value is the version specified when the component package was uploaded. Note Version matching rule: An actual version is considered a match if it starts with the expected version as a prefix. For example, the expected version 535.129 matches the actual version 535.129.03. |

6. Click **OK**.

#### Enable or disbale a bundle

This topic describes how to enable or disable a software stack bundle.

**Limits**

To enable a bundle: The Rediness value of the bundle is **Ready**, and the Status of the bundle is **Draft** or **Disabled**. To disable a bundle: The Status of the bundle is **Draft** or **Enabled**.
1. Log on to the BMCP Operations Platform.
2. Choose **Instance O&M > Software Stack Profile**.
3. In the **Actions** column of the target bundle, click the
icon. Select the operation as needed: i. Click **Enable**. ii. Click **Disable**.
4. In the confirmation dialog box, click **OK**.

#### Use the Detect and upgrade feature

Using the Detect and Upgrade feature, you can check whether component versions on bare metal instances match those defined in the bundle and batch issue upgrade tasks for components whose versions do not match. This topic describes how to detect component versions on bare metal instances and perform upgrades using the software stack bundle.

**Prerequisites**

A software stack bundle has been created, and the required components have been added to the bundle. Components in the bundle are associated with their corresponding component packages, and the component package status is **Ready**. The bundle status is **Enabled**.
1. Log on to the BMCP Operations Platform.
2. In the left-side navigation pane, choose **Instance O&M > Software Stack Profile**.
3. In the **Operation** column of the target bundle, click **Detect and Upgrade**.
The detection and upgrade workflow consists of the following two steps: i. **Select Machines**: Select bare metal instances whose component versions you want to check. The system provides the following three methods to select machines:

| Method | Description |
|---|---|
| Manual Enter | Enter the machine SNs in the text box, separated by commas (,), for example, SN-001,SN-002. After that, click Parse SN to parse and add the machines. |
| Filter Cluster | Select one or more clusters from the cluster list to view the node list under each cluster (including SN, node name, status, image, and OS information), and select the machine nodes to be checked. You can also select all nodes in the current cluster. |
| Import CSV File | Click Download Template to obtain the CSV template file. Fill in the machine information according to the template format, then drag the CSV file into the upload area or click the upload area to select and upload the file. |

ii. **Detection Results**: After confirming the selected machines, click **Start Detection**. The system automatically checks whether the component versions on the selected machines match those defined in the bundle. Upon completion, the system automatically creates an upgrade task to upgrade components with mismatched versions.
4. (Optional) View the execution progress of the upgrade task. In the left-side navigation
pane, click **Instance O&M > Upgrade Task Management** to view the execution status and progress of the upgrade task.

#### Delete a bundle

This topic describes how to delete a software stack bundle.

**Limits**

System-preset bundles cannot be deleted. Custom bundles for which **Status** is **Draft** or **Disabled** can be deleted.
1. Log on to the BMCP Operations Platform.
2. Choose **Instance O&M > Software Stack Profile**.
3. Locate the target bundle, click the
icon in the **Actions** column, and then click **Delete**.
4. In the confirmation dialog box, click **OK**.
