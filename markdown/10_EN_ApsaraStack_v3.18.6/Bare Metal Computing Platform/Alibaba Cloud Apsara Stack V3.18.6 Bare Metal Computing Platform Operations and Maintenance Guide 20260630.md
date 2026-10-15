---
title: "Bare Metal Computing Platform Operations and Maintenance Guide"
product_version: "V3.18.6"
doc_version: "20260630"
pdf_pages: 60
source_pdf: "Alibaba Cloud Apsara Stack V3.18.6 Bare Metal Computing Platform Operations and Maintenance Guide 20260630.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/v3.18.6%E7%89%88%E6%9C%AC%E6%96%87%E6%A1%A3/%E8%A3%B8%E9%87%91%E5%B1%9E%E7%AE%97%E5%8A%9B%E5%B9%B3%E5%8F%B0BMCP/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.6%20Bare%20Metal%20Computing%20Platform%20Operations%20and%20Maintenance%20Guide%2020260630.pdf"
converter: pdf2md (PyMuPDF line classifier)
---

# Bare Metal Computing Platform Operations and Maintenance Guide

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

### Log on to the BMCP

**Operations Console**

This topic describes how to log on to the Apsara Uni-manager Operations Console and then access the Bare Metal Computing Platform (BMCP) Operations Console.

**Prerequisites**

To log on to the BMCP Operations Console, you must first log on to the Apsara Uni-manager Operations Console. Make sure that the endpoint of the Apsara Uni-manager Operations Console is obtained. We recommend that you use the Google Chrome browser.
1. Enter the endpoint of the Apsara Uni-manager Operations Console into the address bar of
the browser.
2. Enter your username and password.
You can obtain the username and password from the operations administrator.

**Note**

When you log on to the Apsara Uni-manager Operations Console for the first time, you must change the password as prompted. To ensure the security of your account, you must specify a password that is 8 to 20 characters in length and contains at least two of the following character types: Letters Digits Special characters, including exclamation points (!), at signs (@), number signs (#), dollar signs ($), and percent signs (%) The opsadmin account has full permissions. Proceed with caution when you use this acc ount.
3. Click **Agree to Private Policy and Log On** to log on to the Apsara Uni-manager
Operations Console.
4. In the top navigation bar, choose **Product Operation > Computing > BMCP**
**Operations Platform**.

## Overview

This topic describes the content displayed on the Overview page of the Bare Metal Computing Platform (BMCP) Operations Console. The Overview page displays alerts, resource data, computing power statistics, and control services.

**Alarm Board**

The alert dashboard displays alerts related to computing, networks, and storage.

**Resource Statistics**

This section displays resource data related to intelligent computing clusters, supercomputing clusters, and storage clusters. Total number of intelligent computing clusters, number of servers, and number of instances. Intelligent computing clusters are classified into **bare metal-intelligent computing**
**clusters** and **ACK-intelligent computing clusters**.
Intelligent computing instances are classified into **high-bandwidth network**
**intelligent computing** instances, **managed intelligent computing** instances, and
**basic intelligent computing** instances.
Intelligent computing instances include only bare metal instances. Elastic Compute Service (ECS) instances are not included. Total number of supercomputing clusters, number of servers, and number of instances. Supercomputing clusters include **bare metal-supercomputing clusters**. Supercomputing instances include **high-performance high-bandwidth network** instances. Total number of storage clusters, number of servers, and number of file systems.

**Resource Board**

This section displays the usage of intelligent computing resources, supercomputing resources, and storage resources.

**Note**

Supercomputing resources do not include the CPU cores and memory of intelligent computing clusters. Intelligent computing resources do not include the GPUs and GPU memory of supercomputing clusters. Intelligent computing resources (number of GPUs and GPU memory) Select a GPU type from the drop-down list, such as **Nvidia** or **Hygon**, to view the GPU quantity of the selected type and total GPU memory.

**Note**

The actual GPU types that you can select on the page shall prevail. Displays allocated resources, unallocated resources, total resources, and distribution ratio. The amount of allocated resources indicates the resources that are allocated to tenants. The amount of unallocated resources indicates the resources in the resource pool. The total amount of resources equals the sum of resources allocated to tenants and resources in the resource pool. Distribution ratio = Resources in the resource pool/(Resources allocated to tenants + Resources in the resource pool) × 100%. Supercomputing resources (number of CPU cores and memory) Select a CPU type from the drop-down list, such as **Intel** or **Hygon**, to view the CPU core quantity of the selected type and total memory.

**Note**

The actual CPU types that you can select on the page shall prevail. Displays allocated resources, unallocated resources, total resources, and distribution ratio. The amount of allocated resources indicates the resources that are allocated to tenants. The amount of unallocated resources indicates the resources in the resource pool. The total amount of resources equals the sum of resources allocated to tenants and resources in the resource pool. Distribution ratio = Resources in the resource pool/(Resources allocated to tenants + Resources in the resource pool) × 100%. Storage resources Select a storage resource type from the drop-down list, such as **APFS** or **CPFS**, to view usage of storage resources of the selected type. Displays **used** storage resources, **allocated** storage resources, **total** storage resources, and the **usage** of storage resources.

**Computational Power Board**

This dashboard displays the usage of GPU computing power and CPU computing power. GPU computing power (unit: TFLOPS) Select a GPU type from the drop-down list to view the usage of GPU computing power of the selected type. The time range is not configurable. The dashboard displays the total computing power, allocated computing power, and distribution ratio within the last week and of the current day. CPU computing power (unit: TFLOPS) Select a CPU type from the drop-down list to view the usage of CPU computing power of the selected type. The time range is not configurable. The dashboard displays the total computing power, allocated computing power, and distribution ratio within the last week and of the current day.

**Note**

CPU computing power refers to the computing power of supercomputing CPUs, excluding the computing power of CPUs in intelligent computing clusters. GPU computing power refers to the computing power of intelligent computing GPUs, excluding the computing power of GPUs in supercomputing clusters.

**Control Service**

The Control Service module displays the service status of the control services related to computing, networks, and storage. The status of a service can be **Not reaching the final**
**state** or **Has reached the final state**. **Not reaching the final state** indicates that the
service deployment has not been completed. **Has reached the final state** indicates that the service deployment is complete.

## Visualized monitoring

### Job path analysis

This topic describes how to work with job path analysis.

**Limits**

Only Hygon DCUK100-AI, APG PG1 A910E, and Kunlun P800 support job path analysis.

**Prerequisites**

The cluster in which the job is deployed has the ai-task-inspector component installed. If the component is not installed, go to **Bare Metal Computing Platform (BMCP) > Cluster**
**Management > Software Instance** to install it.

**Note**

You can use different services to submit jobs, such as Platform for AI (PAI) or AI Studio. You can use the job path analysis feature if only the job uses the GPU resources of BMCP nodes.
1. Log on to the BMCP Operations Console.
2. In the left-side navigation pane, click **Job Path Analysis** below Visualized Monitoring.
3. On the **Job Path Analysis** page, specify **Job ID** and click **Search**.

**Note**

Specify **Start And End Time** to select a time range. You can query historical jobs within at most the last 7 days. The **Node ID** parameter is optional. If you specified **Node ID**, **Cluster ID** is automatically set to the ID of the cluster that contains the node. The **Cluster ID** and **Namespace** parameters are required. Then, specify **Job ID**. By default, **Job Information** is hidden. You can click the icon on the left to view the status of the job, resources occupied by the job, and the start time and end time of the job.
4. After you click **Job Details**, the **Basic Information** and **Monitoring** tabs are displayed in
the right-side panel. The **Basic Information** tab displays the nodes occupied by the job, and the **Monitoring** tab displays the metrics of the occupied nodes, such as the average CPU utilization.
5. In the **Job view** section, click a **time slice**. Then, the canvas displays the topology and
resource usage of the job within the selected time slice. The topology displays the **GPUs,**
**RDMA cards, and vSwitches**, and the connections among them. Resource usage metrics
such as GPU utilization and RDMA network bandwidth usage are also displayed.

**Note**

Move the pointer over a GPU or RDMA card to view the name and resource usage of the resource.

## Alerts

### Resource event alerts

This topic introduces the resource event alert module and how to create an event ticket to handle alerts.

**Prerequisites**

CloudMonitor is deployed and reaches the final state.

**Note**

The resource event alert module strongly relies on CloudMonitor. Make sure that CloudMonitor is deployed and reaches the final state before you start.
1. Log on to the Bare Metal Computing Platform (BMCP) Operations Console.
2. In the left-side navigation pane, click **Alerts**.
3. On the **Resource Event Alert** tab, view existing alerts.
By default, the **Calculation** tab is displayed.
4. View **Calculation** alerts.
i. You can filter alerts by **alert level, alert status, alert source, or alert ID**. You can also click **Advanced Filter** to select multiple filter conditions, including alert ID, alert name, and alert start time.

**Note**

The following alert severity levels are available: **emergency, serious, warning,**
**and hint**.
Alerts can be in the following states: **Processed and Unprocessed**. Alerts related to the following resources are generated: **Calculation (in-band),**
**Calculation (out-of-band), and Network**.
ii. For alerts in the Unprocessed state, click **Add Event List** to handle the alerts. After the alerts are handled, their states change to Processed.

**Note**

You can handle an alert by selecting Ignore (the alert is ignored) or Fixed (the issue that triggers the alert is fixed).
5. Click the **Storage** tab to view **storage** alerts.
You can filter alerts by **alert level, alert status, alert name, alert content** , or **alert**
**start time**. You can also click **Advanced Filter** to select multiple filter conditions,
including alert name, alert content, and alert start time.

**Note**

The following alert severity levels are available: **emergency, serious, warning, and**
**hint**.
Alerts can be in the following states: **Processed and Unprocessed**. Alerts related to the following resources are generated: **Calculation (in-band),**
**Calculation (out-of-band), and Network**.

### Job event alerts

Thistopicdescribeshowtoviewjobalerts This topic describes how to view job alerts.
1. Log on to the BMCP Operations Console.
2. In the left-side navigation pane, click **Alerts**.
3. On the **Job Event Alert** tab, you can search for a job based on **Cluster ID**, **Namespace**,
or **Job ID** and click Search to view all relevant alerts generated during the lifecycle of the job.

## Clusters

### Computing

#### Clusters

##### Query the details of a computing cluster

This topic describes how to query the details of a Bare Metal Computing Platform (BMCP) cluster, including the basic information, nodes, and operation logs of the cluster. You can query the details of a bare metal-intelligent computing cluster, ACK-intelligent computing cluster, or bare metal-supercomputing cluster.

**Prerequisites**

A BMCP cluster is created in the Apsara Uni-manager Operations console.
1. Log on to the BMCP Operations Console.
2. In the left-side navigation pane, click **Clusters**.
3. Click the **Calculation > Cluster** tab.
This tab displays the computing clusters of all tenants.
4. Query computing clusters:
Basic filtering: a. You can search clusters by cluster ID or cluster name. b. Click the icon to search clusters in fuzzy match mode. Advanced filtering: a. Click **Advanced Filter**. b. Specify the Cluster ID and Cluster Name conditions. c. Click **Search** to search for clusters that match the specified conditions in fuzzy match mode.
5. Click **Details** in the Operation column of the desired cluster to view **Basic Information**,
**Cluster Node**, and **Operation Log**.
i. **Basic Information** The following table lists the information on the Basic Information page.

| Section | Description |
|---|---|
| Basic Information | This section displays cluster information such as the cluster ID, cluster name, cluster status, number of nodes, and creation time. |
| Configuration Information | This section displays the cluster instance specifications, number of CPU cores, memory size, GPU memory size, and computing power. |
| Storage Information | This section displays the high-performance storage status. |

ii. **Cluster Node** Click the **Cluster Node** tab to view **bare metal nodes** allocated to this cluster. You cannot view **Elastic Compute Service (ECS) nodes** in the cluster. You can view node information, such as **Node Name/ID**, **Status**, **SN**, **Node IP**, and **Model**. You can click
**Details** in the **Operation** column of a node to view the details of the node. For more
information, see View the details of a computing node. iii. **Monitoring** Click the **Monitoring** tab to view the monitoring information of the cluster, such as the memory usage, cluster loads, and number of connections. iv. **Operation Log** Click the Operation Log tab to view the operation logs of the cluster. You can view the historical operation logs of the cluster by operation type and operation event. a. Select an operation type from the **Operation Type** drop-down list, such as Create Cluster, Delete a cluster, Expansion Cluster, or Shrinking Cluster, to search for
**operation logs** of the specified operation type. If you do not select an operation type,
**operation logs** of all operation types are displayed.
b. Click **Operation Time** and specify **Start Date** and **End Date** (accurate to seconds). Then, **operation logs** from the start date to the end date are displayed. c. You can click **Operation details** in the Operation column to view atomic steps in the operation and the detailed information.

#### Nodes

##### View the details of a computing node

This topic describes how to query Bare Metal Computing Platform (BMCP) computing nodes and node details, including basic information and operation logs. You can query nodes in bare metal-intelligent computing clusters, ACK-intelligent computing clusters, bare metalsupercomputing clusters, and idle nodes in the resource pool.
1. Log on to the BMCP Operations Console.
2. In the left-side navigation pane, click **Cluster Management**.
3. On the **Cluster Management** page, click the **Calculation > Node** tab. This tab displays
computing notes owned by all tenants and computing nodes in the resource pool.
4. Query computing nodes:
Basic filtering: a. You can search nodes by node ID, node name, SN, cluster ID, subnet IP, VPC IP, or outof-band IP. b. Click the icon to search nodes in fuzzy match mode. Advanced filtering: a. Click **Advanced Filter**. b. Specify the Node ID, Node Name, SN, Cluster ID, Subnet IP, VPC IP, and Out-of-band IP filter conditions at the same time. c. Click **Search** to search for nodes that meet the specified conditions in fuzzy match mode.
5. Click **Details** in the Operation column of the desired node to view **Basic Information**,
**Monitoring**, and **Operation Log**.
i. Basic Information The following table lists the information displayed on the Basic Information page.

| Section | Description |
|---|---|
| Basic Information | The Basic Information section displays Node ID, Node Name, SN, Region, and Zone. |
| Configuration Information | The Configuration Information section displays node hardware information, including CPU, GPU, Operating System, Network, Nic, and Disk. |

ii. Monitoring The **Monitoring** tab displays the node monitoring data, including the CPU utilization, memory utilization, loads, and number of connections. iii. Operation Logs You can filter the historical operation logs of the node by operation type. a. You can select a tag from the **Operation Type** drop-down list to filter **operation logs**. You can select the following tags: Apply for an instance, Re-apply, O & M instance, Mount instance, Mount storage, Unmount storage, and Patrol inspection diagnosis. If you do not select a filter condition, **operation logs** of types of operations that have been performed on the server are displayed. b. Click **Operation Time**, and specify **Start Date** and **End Date** (accurate to days). Then, **operation logs** from 00:00:00 of the start date to 23:59:59 of the end date are displayed. c. You can click **Operation details** in the Operation column to view all atomic steps included in the operation and the detailed information.
6. Click **Node Status** in the Operation column of a node to manage the node. For more
information, see Manage computing nodes.
7. Click **Resource Enable** in the Operation column of a node to manage the node. For more
information, see Manage computing nodes.

### Storage

**View the details of a storage cluster**

1. Log on to the Bare Metal Computing Platform (BMCP) Operations Console.
2. In the left-side navigation pane, click **Clusters**.
3. On the **Cluster Management** page, click the **Storage** tab.
4. You can view the health status, disk type, file system type, and number of nodes of the
cluster.
5. Find the desired cluster.
In the upper-right corner of the cluster list, you can enter a **cluster ID** into the search box to search clusters in exact match mode.
6. Click **Details** in the **Operation** column of the cluster to view the cluster details.
On the **Basic Information** tab, you can view **Number of file systems**, **Number of**
**nodes**, **File system type**, **Health status**, and **Disk type**.
On the **Node** tab, you can view node information, such as **Management IP**, **SN**, **Model**,
**CPU architecture**, and **Memory**.
You can search nodes by node name in exact match mode. On the **Service** tab, you can view service roles and service status. You can search services by service name in fuzzy match mode. Click **Tianji O & M** in the **Operation** column of the desired service role. The **Monitoring** tab displays monitoring data.

**View the details of a client cluster**

1. Log on to the BMCP Operations Console.
2. In the left-side navigation pane, click **Clusters**.
3. On the **Cluster Management** page, click the **Storage** tab.
4. Click the **Client Cluster** tab.
You can view the cluster information, including the cluster status, cluster type, number of nodes, number of Quorum nodes, and **the file system mounted to the cluster** .
5. Find the desired cluster.
In the upper-right corner of the cluster list, you can enter a **cluster name** into the search box to search for the cluster in exact match mode.
6. Click **Details** in the **Operation** column of the desired cluster to view the cluster details.
The **Cluster Details** tab displays detailed cluster information, including the number of nodes, number of Quorum nodes, basic information, and configuration information. The **Cluster Node** tab displays the basic node information, including the node type and node status. You can also click **Details** in the **Operation** column of the desired node to view the node details, including the basic information, configuration information, monitoring data, and operation logs.

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
1. Log in to the Bare Metal Computing Platform (BMCP) Operations Console.
2. In the left-side navigation pane, click **Resource management**.
By default, the **Calculation > Server** tab is displayed. You can view all physical servers on this tab.
3. Click **Register Resources** above the list.
4. In the **Select an Access Method** dialog box, specify the access method. The following
table describes the parameters.

| Parameter | Description |
|---|---|
| Access Mode | The access method. Valid values: CHSW Access HSW Access |
| Resources To be Managed | The resource to be managed. |

5. Click **OK**.
6. In the Register Resources panel, perform the following operations:
i. In the **Basic Information** section, configure the following parameters:
**Region** and **Zone**
ii. In the **Resources** section, configure the parameters described in the following table.

| Parameter | Description |
|---|---|

| Resource Type | The type of the resource. Valid values if you select CHSW Access: Managed by High-Performance Computing: A standard image provided by the platform is used to initialize and start Elastic Compute Service (ECS) bare metal instances. Valid values if you select HSW Access: Intelligent Computing Managed: A standard image provided by the platform is used to initialize and start ECS bare metal instances. Manage In-band: When ECS bare metal instances are started, the original operating system of the device is not modified. Managed by High-Performance Computing: A standard image provided by the platform is used to initialize and start ECS bare metal instances. |
|---|---|
| Architecture | The CPU architecture of the resource. Valid values: x86 64 _ aarch64 sw 64 _ |
| Model | The model of the resource. If no model is available, add a model first. |
| SN | The serial number of the resource. The value must be 2 to 128 characters in length and can contain periods (.), underscores ( ), _ hyphens (-), and colons (:). The name cannot start with a special character. This parameter is not required if you select CHSW Access. |
| Equipment model | The device model. The value can be up to 128 characters in length and can contain letters and digits. This parameter is not required if you select CHSW Access. |
| Data Center | The data center in which the resource is deployed. The value can be up to 128 characters in length and can contain letters and digits. This parameter is not required if you select CHSW Access. |
| Room | The room in which the resource is deployed. The value must be 2 to 128 characters in length and can contain letters, digits, underscores ( ), and hyphens (-). Example: 1-1-1. _ This parameter is not required if you select CHSW Access. |
| Cabinet | The rack in which the resource is deployed. The value must be 3 characters in length. It must start with an uppercase letter and end with an integer in the range of 01 to 24. Example: F02. This parameter is not required if you select CHSW Access. |

| Rack unit number | The rack number. The value must be a positive integer in the range of 1 to 48. This parameter is not required if you select CHSW Access. |
|---|---|
| Maintenance time | The time period during which maintenance is performed. |

iii. In the **Image** section, configure the parameters described in the following table.

| Parameter | Description |
|---|---|
| Image type | The type of the image. Valid values: Public image and Custom image. |
| Public/custom images | The image that you want to use. |

iv. In the **Network** section, configure the parameters described in the following table.

| Parameter | Description |
|---|---|
| Physical machine Gateway | The physical machine gateway. This parameter is not required if you select CHSW Access. |
| Physical machine gateway port | The port of the physical machine gateway. This parameter is not required if you select CHSW Access. |
| Subnet | The subnet that you want to use. This parameter is not required if you select CHSW Access. |
| Subnet IP | The IP address that belongs to the subnet. This parameter is not required if you select CHSW Access. |
| Out-of-band information | By default, you do not need to specify the out-of-band information. To specify the out-of-band information, select Expand. |
| Out-of-band IP | The out-of-band IP address. This parameter is required only if you select Expand for the Out-of-band information parameter. |
| Out-of-band username | The out-of-band username. This parameter is required only if you select Expand for the Out-of-band information parameter. The value must be 2 to 128 characters in length. It must start with a letter and can contain digits and special characters. The supported special characters include ~ ! @ # $ % ^ & * () - = + \| [ { } ] ; : . _ |
| Out-of-band password | The out-of-band password. This parameter is required only if you select Expand for the Out-of-band information parameter. The value must be 1 to 128 characters in length. |

v. In the **Configure password** section, configure the parameters described in the following table.

| Parameter | Description |
|---|---|
| Login name | The username used to log in to the resource. The default value is root, which cannot be changed. |
| Login Password | The password used to log in to the resource. It must be 8 to 30 characters in length, and must contain at least three types of the following characters: uppercase letters, lowercase letters, digits, and special characters. Supported special characters include ( ) ` ~ ! @ # $ % ^ & * - + = \| { } [ ] : ; ' < > , . ? /. _ |
| Confirm password | You need to enter the login password again. The value of this parameter must be consistent with that of the Login Password parameter. Important Keep your password confidential. If you lost the password, you can log in to the BMCP Operations Console and reset the password. |

vi. In the **Resource Name** section, configure the parameters described in the following table.

| Parameter | Description |
|---|---|
| Resource Name | The name of the resource. It must be 2 to 128 characters in length, and can contain letters, digits, periods (.), and hyphens (-). The name must start with a letter or digit. This parameter is not required if you select CHSW Access. |
| Hostname | The hostname. This parameter is not required if you select CHSW Access. |
| Resource Description | The description of the resource. It must be 0 to 1,000 characters in length. |

7. After you complete the configurations, click **OK**.

##### Manage server resource status

This topic describes how to start, restart, stop, delete, and initialize server resources.

**Prerequisites**

The server **Resource owner** is **Resource Pool**.
1. Log on to the BMCP Operations Console.
2. In the left-side navigation pane, click **Resource management** to enter the **Calculation >**
**Server** tab by default. This page displays all physical servers in the site.
3. Filter for your target server.
4. In the **Actions** column for the target server, click **Resource Status**.
You can start, restart, stop, delete, or release a single resource.

| Operation status | Power status | Available operations |
|---|---|---|
| Uninitialized, System Reset | Irrelevant | Initialize a resource |
| Completed | Shut Down | Start a resource, Delete a resource |
| Completed | Start | Restart a resource, Stop a resource, Delete a resource |

5. You can also select one or more server resources, then click **Delete Resource** and
**Initialize Resources** at the bottom of the server list.

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

This topic describes how to enable and disable a server.

**Prerequisites**

The **resource owner** of the server is **Resource Pool**.

**Enable a server**

1. Log on to the Bare Metal Computing Platform (BMCP) Operations Console.
2. In the left-side navigation pane, click **Resource management**.
By default, the **Calculation > Server** tab appears. This tab displays all existing physical servers.
3. Search for the desired server.
4. Click the
icon in the **Operation** column of the server.
5. Choose **Resource Enable > Enable**.
6. In the message that appears, click OK.

**Disable a server**

**Important**

After a server is disabled, it cannot be added to clusters.
1. Log on to the BMCP Operations Console.
2. In the left-side navigation pane, click **Resource management**.
By default, the **Calculation > Server** tab appears. This tab displays all existing physical servers.
3. Search for the desired server.
4. Click the
icon in the **Operation** column of the server.
5. Choose **Resource Enable > Disable**.
6. In the message that appears, click OK.

#### GPUs

##### View GPU details

This topic describes how to query GPUs on an installed bare metal instance and view the detailed information about each GPU.

**Prerequisites**

You can query the GPUs of a bare metal instance only after the bare metal instance is installed.
1. Log on to the Bare Metal Computing Platform (BMCP) Operations Console.
2. In the left-side navigation pane, click **Resource Management**.
3. On the **Resource Management** page, click the **Calculation > GPU card** tab. This page
displays the GPUs on all installed bare metal instances.
4. Query GPUs:
Basic filtering: a. You can query GPUs by GPU ID, node ID, or GPU model or select a tag from the dropdown list. b. Click the icon to search GPUs in fuzzy mode. Advanced filtering: a. Click **Advanced Filter**. b. You can specify the GPU ID, node ID, and GPU model filter conditions at the same time. c. Click **Search** to search GPUs in fuzzy match mode.
5. Click **Details** in the Operation column of the desired GPU to view **Basic Information**.
The following table lists the information displayed on the Basic Information page.

| Section | Description |
|---|---|
| GPU card information | Displays GPU ID, Node, Server to which the server belongs, Manufacturer, GPU model, Flash storage capacity, and Computing Power. |
| Configuration Information | Displays VBIOS version, Driver name, Driver version, and BusInfo. |

### Storage

#### View the file system details

This topic describes how to view the file system details.
1. Log on to the Bare Metal Computing Platform (BMCP) Operations Console.
2. In the left-side navigation pane, click **Resource management**.
3. On the **Resource Management** page, click the **Storage** tab.
By default, the **File system** tab is displayed.
4. You can enter a **file system name** into the search box above the list to search file
systems. You can also click **Advanced Filter** to search file systems by **file system name**.
5. Click the name of the **storage cluster** of the file system.
You can then view the storage cluster information of the file system, including the number of file systems, number of nodes, capacity, health status, file system type, cluster node information, service roles, and monitoring data.
6. Click the name in the **Client cluster** column of the desired file system.
You can then view the client cluster information of the file system, including the number of nodes, number of Quorum nodes, cluster type, mount path in the file system, maximum number of cached files, worker threads, and cluster node information.
7. Click Details in the **Operation** column of the file system.
You can then view the details of the file system, including the file system name, storage cluster, client cluster, specification, and monitoring data.

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

This topic describes how to query all network elements, including DSW, RDSW, HSW, CHSW, EHSW, and RASW.

**Prerequisites**

None.
1. Log on to the Bare Metal Computing Platform (BMCP) Operations Console.
2. In the left-side navigation pane, click **Resource management**.
3. On the **Resource Management** page, choose **Network > Network Element**. This tab
displays all network elements.
4. Query network elements:
Basic filtering: a. You can search network elements by name or management IP address or select a tag from the drop-down list. b. Click the icon to search network elements in fuzzy match mode. Advanced filtering: a. Click **Advanced Filter**. b. Specify the Network element name and Manage IP addresses filter conditions at the same time. c. Click **Search** to search for network elements that match the specified conditions in fuzzy match mode.
5. Click **Details** in the Operation column of the desired network element to view **Basic**
**Information**.
6. The **Network element details > Basic Information** section displays the **basic**
**information** of the GPU and **ports**.
7. Query ports:
Basic filtering: a. You can search ports by name or select a tag from the drop-down list. b. Click the icon to search ports in fuzzy match mode. Advanced filtering: a. Click **Advanced Filter**. b. Enter a port name. c. Click **Search** to search ports in fuzzy match mode.

#### Network elements

## Inspection and diagnostics

### Inspection

#### Diagnose a cluster or node

This topic describes how to diagnose a cluster or node.

**Important**

If this operation includes time-consuming diagnostic items or stress tests, GPU resources are occupied. Make sure that this operation does not affect your business.
1. Log in to the Bare Metal Computing Platform (BMCP) Operations Console.
2. In the left-side navigation pane, choose **Inspection and Diagnostics > Inspection.**
3. On the **Cluster/node diagnosis** tab of the **Diagnosis** page, create a diagnostic task for a
cluster or node and view the diagnostic result.
4. Click **Create a task**. In the One-click diagnosis dialog box, specify the task name, choose
cluster diagnostics or node diagnostics, confirm the diagnostic scope, and select diagnostic items. Click a number in the **Sub-item** column to view the supported diagnostic items. For more information about diagnostic items, see Description of diagnostic items.
5. Click **OK** to create the task.
6. You can query historical diagnostic tasks by task ID in exact match mode or by task name
in fuzzy match mode. You can also specify a time range or click Advanced Filter and specify multiple filter conditions.
7. Cancel the diagnostic task.
Find the diagnostic task and click **Cancel** in the **Operation** column.
8. View the diagnostic result.
After the diagnostic task enters the Completed state, click **Details** in the Operation column to view the diagnostic result.

#### Diagnose a cluster in which a job runs

This topic describes how to diagnose a cluster in which a job runs.

**Note**

1. Log in to the Bare Metal Computing Platform (BMCP) Operations Console.
2. In the left-side navigation pane, choose **Inspection and Diagnostics > Inspection.**
3. On the Diagnosis page, click the **Job diagnosis** tab.
4. Create a diagnostic task for a cluster in which a job runs and view the diagnostic result.
5. Click Create a task. In the One-click diagnosis dialog box, configure the **Task name**,
**Cluster ID**, **Namespace**, **Job ID**, and **Diagnostic items** parameters.
Click a number in the **Sub-item** column to view the supported diagnostic items. For more information about diagnostic items, see Description of diagnostic items.
6. Click **OK** to create the task.
7. Query historical diagnostic tasks by cluster ID, namespace, and job ID.
8. Cancel the diagnostic task.
Find the diagnostic task and click **Cancel** in the **Operation** column.
9. View the diagnostic result.
After the diagnostic task enters the Completed state, click **Details** in the Operation column to view the diagnostic result.

#### Description of diagnostic items

The diagnostics feature provides cluster, node, and job diagnostics. This topic describes the supported diagnostic items.

**System diagnostics**

| Diagnostic item | Description |
|---|---|
| Resource QoS diagnostics | The containerd engine is abnormal, and the ctr command times out or hangs. |
| DNS configuration check | Check the DNS configuration of the physical machine /etc/resolv.conf. |
| NIC uplink mapping check | Check whether the mappings between the network interface controller (NIC) ports of each server and the switch ports are correct. |

**Network diagnostics**

| Diagnostic item | Description |
|---|---|
| NIC speed compliance check | Check and ensure that the NIC speed meets the system requirements. |
| BOND port check | Check the status and configuration of network bonding ports. |
| NIC-to-GPU connection check | Check whether the connection topology between NICs and GPUs is correct. |
| Bonding module check | Check whether the bonding network module is correctly installed. |

| OS release version | Check the OS release version. |
|---|---|
| OS kernel version | Check and ensure that the kernel version meets the system requirements. |
| Hash policy for aggregating RDMA network devices | Check the aggregation hash policy configuration of Remote Direct Memory Access (RDMA) network devices. |
| RDMA QoS configuration check | Check and optimize RDMA Quality of Service (QoS) configuration. |
| RDMA device quantity | Check whether the number of RDMA devices meets expectations. |
| RDMA device name and status | Check the names and running status of RDMA devices. |
| RDMA device aggregation mode | Check the aggregation mode configuration of RDMA devices. |
| RDMA device MTU settings | Check and optimize the MTU settings of RDMA devices. |
| RDMA device port rate | Check whether the RDMA device port rate meets the performance requirements. |
| RDMA device aggregation status | Check the aggregation status of RDMA devices. |
| MLX LAG mode check | Check and confirm the MLX LAG mode configuration. |
| PCIe link rate and width consistency check | Check the consistency of the PCIe link rate and width. |
| Consistency check of RDMA device firmware versions | Check the consistency of RDMA device firmware versions. |
| RDMA NIC driver loading | Check whether the RDMA NIC driver is loaded correctly. |

| PCIe MRR configuration | Check the PCIe MRR configuration. |
|---|---|
| GDR module load check | Check whether the GDR module is loaded correctly. |
| LLDP service running status | Check the running status of the LLDP service. |
| Running status of NVIDIA Fabric Manager | Check the running status of NVIDIA Fabric Manager. |
| PCIe link rate and width downgrade check | Check and fix the PCIe link rate and width downgrade issues. |
| Upstream switch and port name check | Check the upstream switch and port name configuration. |
| alixpu peermem _ status check | Check the loading status of the alixpu peermem module and reload it. _ |
| XDR module installation check | Check the integrity of the XDR module installation and reinstall it if necessary. |
| APG ICN status check | Check the APG ICN for abnormal status and restart the related services. |
| GPU drop | Check whether the GPU has fallen off the bus. |
| IB NIC sequence check | Check whether the IB NIC sequence is as expected. |

**GPU diagnostics**

**Note**

GPU diagnostic items are related to graphics cards. For the supported diagnostic items, see those displayed in the console.

| Diagnostic item | Description |
|---|---|

| OS environment check | Check and fix GPU device drivers, firmware, core services, kernel data interfaces, environment variables, and runtime libraries. |
|---|---|
| Network device check | Check and update network device drivers and firmware to meet high-speed network requirements. |
| Historical fault screening | Analyze and handle historical faults recorded in the system. |
| GPU device presence check | Check and ensure that the GPU device is in place properly. |
| GPU uplink speed check | Check and handle whether the uplink and interconnection of GPU devices have speed reduction and lane reduction issues. |
| Device operating condition check | Check for and handle abnormal conditions such as over-temperature, down- frequency, and severe memory faults of GPU devices. |
| DCGM fault diagnostics | Run the DCGM Level 2 to Level 4 diagnostic programs to check for and handle abnormal device status. |
| Device capability check | Check whether GPU devices support advanced features such as GRDMA. |
| GPU memory bandwidth test | Test and analyze GPU H2D, D2H, and D2D bandwidth performance. |
| GPU point-to-point communication test | Test and evaluate the efficiency of point-to-point communication between GPU devices. |
| Black-Scholes algorithm simulation | Evaluate GPU computing performance by using the Black-Scholes algorithm. |
| Gravity body simulation | Test GPU computing limits by using a million-body gravitational simulation. |
| CUDA matrix multiplication | Check and optimize the data accuracy and performance of CUDA matrix multiplication. |
| CuBLAS matrix multiplication | Check and optimize the data accuracy and performance of CuBLAS matrix multiplication. |
| GPU burn-in test | Perform long-term stress test on GPU to check device stability. |

| HBM memory stress test | Check the performance and stability of HBM memory. |
|---|---|
| Test of GPU data copy accuracy | Check the accuracy of GPU data copy. |
| Test of GPU data copy performance | Test and optimize GPU data copy performance. |
| Kernel launch performance test | Analyze and improve kernel launch and execution latency. |
| General matrix multiplication FLOPS | Test matrix multiplication performance for different data types. |
| cuDNN function performance | Test and optimize cuDNN common function performance. |
| cuBLAS function performance | Test and optimize cuBLAS common function performance. |
| Single-GPU matrix multiplication performance | Test and optimize single-GPU large matrix multiplication performance. |
| Multi-GPU matrix multiplication performance | Test and optimize multi-GPU large matrix multiplication performance. |
| Computation communication overlap test | Test GPU computation and communication overlap capabilities. |
| NCCL communication performance test | Test and optimize NCCL collective communication performance. |
| HIP memory bandwidth test | Test and analyze GPU H2D and D2H bandwidth performance based on HIP. |
| HIP device capability check | Check and confirm GPU device functional attributes. |
| Basic attribute check for HIP devices | Check basic attributes of GPU devices. |

| HIP bus bandwidth test | Test GPU bandwidth exceptions by using the Zero-Fraction algorithm. |
|---|---|
| HIP P2P communication check | Check whether P2P communication between GPU devices is enabled. |
| HIP HelloWorld kernel test | Check that the device can correctly execute the HelloWorld kernel function. |
| HIP matrix multiplication test | Test the data accuracy of HIP matrix multiplication. |
| Stress test on compute cores | Stress test DCU compute cores and record the temperature and power consumption over time. |
| Stress test on DCU memory | Stress test DCU memory and record the temperature and power consumption over time. |
| Component stress test | Stress test DCU compute cores and memory, and record the temperature and power consumption over time. |
| PCIe bandwidth test | Test DCU PCIe bandwidth. |
| XHMI bandwidth test | Test DCU XHMI bandwidth. |
| HBM bandwidth test | Test DCU HBM bandwidth. |
| Balanced computing power test | Test the balanced computing power of DCU across multiple numerical precisions: FP64, FP32, FP16, INT8, and INT4. |
| RCCL communication performance test | Test the collective communication efficiency and bandwidth performance of RCCL. |
| Bidirectional DMA test for HBM | Test the bidirectional DMA correctness and speed between hosts and devices for HBM. |
| Bidirectional DMA test for L3 cache | Test the bidirectional DMA correctness and speed between hosts and devices for L3 cache. |
| Task execution test | Test the execution capabilities and efficiency of device computing tasks. |

| Inter-device memory copy test (AUTO mode) | Test inter-device memory copy efficiency on a single machine to balance performance and accuracy. |
|---|---|
| Inter-device memory copy test (UNIT mode) | Test inter-device memory copy accuracy on a single machine. |
| Inter-device memory copy test (PERF mode) | Test inter-device memory copy performance on a single machine. |
| Peak power consumption test | Test the peak power consumption of XPU devices and monitor changes in temperature and power consumption. |
| Dynamic power consumption test | Test changes in XPU dynamic power consumption. |
| Global memory availability test | Test the availability of XPU global memory. |
| Functional test of XPU links | Verify the feature availability of XPU links. |
| Operator unit test | Perform operator unit tests and count the number of failed unit tests. |
| Global memory read/write test | Test the read/write capabilities of XPU global memory. |
| XPU link C2C test | Test the C2C functionality of XPU links. |
| Dynamic power consumption test | Test dynamic power consumption of PG1. |
| PCIe link performance test | Test the memory access performance of PG1, including the memory access bandwidth and latency in various scenarios. |
| Floating-point computing performance verification | Check whether the floating-point computing performance of PG1 meets requirements. |

| Memory subsystem performance test | Measure the performance of the PG1 memory subsystem, including memory bandwidth and latency. |
|---|---|
| Stress test on Sahara peak power | Stress test the extreme power consumption. |
| Stress test on Sahara stable power | Stress test the stable power consumption. |
| Stress test on Sahara cache | Stress test the PG1 cache. |
| Stress test on Sahara SDC | Perform a SDC stress test. |
| ICN port status check | Check the link status of the PG1 ICN port. |
| ICN communication performance test (unidirectional) | Test the unidirectional communication performance of ICN. |
| ICN communication performance test (bidirectional) | Test the bidirectional communication performance of ICN. |
| PCCL communication performance test | Test PCCL collective communication performance, including bandwidth and communication latency. |
| MXVS floating-point computing power test | Test floating-point performance at different precisions. |
| MXVS unidirectional PCIe link test | Measure unidirectional memory access bandwidth and latency in different scenarios. |
| MXVS bidirectional PCIe link test | Measure bidirectional memory access bandwidth and latency in different scenarios. |
| MXVS unidirectional P2P link test | Measure unidirectional P2P memory access bandwidth and latency in different scenarios. |
| MXVS bidirectional P2P link test | Measure bidirectional P2P memory access bandwidth and latency in different scenarios. |

| MXVS MetaX link test | Evaluate inter-card interconnect bandwidth of MetaXLink. |
|---|---|
| MXVS memory stress test | Test HBM memory bandwidth. |
| MXVS stress test (MetaXLink) | Evaluate GPU stability by pushing computing power and power consumption to over 95%. |
| MXVS stress test (XCore) | Evaluate GPU stability by pushing computing power and power consumption to over 95%. |
| MCCL communication performance test | Test MCCL collective communication performance, including bandwidth and communication latency. |
| MUDNN matrix multiplication performance | Measure GPU floating-point performance through MUDNN matrix multiplication. |
| Stability test of MUDNN matrix multiplication | Assess GPU functional integrity by verifying the correctness of MUDNN matrix multiplication results. |
| MUDNN Unary performance test | Test GPU memory bandwidth performance. |
| MUDNN Unary stable test | Test GPU memory features. |
| MUDNN Conv2d functional test (NCHW) | Test the functional completeness of MUDNN 2D convolution operations with NCHW-formatted tensors. |
| MUDNN Conv2d functional test (NHWC) | Test the functional completeness of MUDNN 2D convolution operations with NHWC-formatted tensors. |
| MUDNN Conv3d functional test (NCDHW) | Test the functional completeness of MUDNN 3D convolution operations with NCDHW-formatted tensors. |
| MUDNN Conv3d functional test (NDHWC) | Test the functional completeness of MUDNN 3D convolution operations with NDHWC-formatted tensors. |

| MUDNN Flash Attention test | Test the functional completeness of the MUDNN Flash Attention operator. |
|---|---|
| GPU memory read/write test | Test the memory read/write performance. |
| MCCL communication performance test | Test MCCL collective communication performance, including bandwidth and communication latency. |

**Container diagnostics**

| Diagnostic item | Description |
|---|---|
| containerd exception detection | The containerd container engine is abnormal, and the ctr command times out or hangs. |
| Detection of runc process hang | If a runc process hangs, the corresponding container becomes unresponsive. |
| Detection of memory leaks in shim processes | A memory leak in a shim process can render the corresponding container unresponsive. |
| Detection of shim process leaks | The container has been deleted, but its corresponding shim process is still running. |
| Detection of runc state directory leaks | The container has been deleted, but its corresponding runc state directory persists. |
| systemd health monitoring | A hang in the systemd or dbus daemon or an excessive number of mount points (> 5,000) can cause systemd to become unresponsive. |
| Check for disk error information | Disk error messages in dmesg can cause certain operations of the container runtime to fail. |

## Basic configurations

### Models

#### Add a device model

This topic describes how to add a device model.

**Background information**

You can add **managed intelligent computing**, **In-Band**, and **HPC** device models by clicking **Add model**. The system automatically imports device models of all other types during the Zhuque planning phase.
1. Log on to the BMCP Operations Console.
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

#### Query models

This topic describes how to query models.
1. Log on to the Bare Metal Computing Platform (BMCP) Operations Console.
2. In the left-side navigation pane, choose **Basic Configurations > Models**.
3. On the **Model Management** page, enter the model into the search box.
4. Click the
icon to search in fuzzy match mode.

#### Modify a model

This topic describes how to modify a model.
1. Log on to the Bare Metal Computing Platform (BMCP) Operations Console.
2. In the left-side navigation pane, choose **Basic Configurations > Models**.
3. Click **Modify** in the **Operation** column of a model.
4. In the **Modify model** dialog box, modify the model parameters.

#### Remove a model

This topic describes how to remove a model.
1. Log on to the Bare Metal Computing Platform (BMCP) Operations Console.
2. In the left-side navigation pane, choose **Basic Configurations > Models**.
3. Click **Delete** in the **Operation** column of the desired model.
4. In the message that appears, click **OK**.

**Warning**

Before you remove a model, make sure that the model is not used by instances. This operation is irreversible.

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
| GPU memory size | Yes | The size of GPU memory. Unit: GB. |
| TFLOPS | Yes | The TFLOPS. |

5. After you complete the configuration, click **OK**.

#### Query GPUs

This topic describes how to query GPUs.
1. Log on to the Bare Metal Computing Platform (BMCP) Operations Console.
2. In the left-side navigation pane, choose **Basic Configurations > GPU Settings**.
3. On the **GPU Configuration** page, enter a **GPU model** into the search box.
4. Click the
icon to search GPUs in fuzzy match mode.

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

### Clusters and nodes

This section describes how to pull logs from a cluster or node.
1. Log on to the Bare Metal Computing Platform (BMCP) Operations Console.
2. In the left-side navigation pane, click **Logs**.
3. On the **Log Management** page, click the **Cluster/node logs** tab.
4. On this tab, you can create a log pulling task for a cluster or node, and then download the
log package.
5. Click **Create a task**, specify **Task name** and **Log type**, confirm the scope, and configure
**Time range**.
6. Click **OK** to create the task.
7. You can click **Details** in the Operation column of the task to view the log pulling details.
8. Select the task and click **Export logs** to download the log package.

### Job logs

This topic describes how to collect job logs.

**Limits**

Job logs support only **ACK - intelligent computing clusters** that contain **bare metal**
**nodes**.
1. Log on to the BMCP Operations Console.
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
