---
title: "Alibaba Cloud Apsara Stack V3.18.3 Elastic Compute Service Operations and Maintenance Guide 20250318"
product_version: "V3.18.3"
doc_version: "20250318"
pdf_pages: 124
source_pdf: "Alibaba Cloud Apsara Stack V3.18.3 Elastic Compute Service Operations and Maintenance Guide 20250318.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/V3.18.3/%E4%BA%91%E6%9C%8D%E5%8A%A1%E5%99%A8ECS/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.3%20Elastic%20Compute%20Service%20Operations%20and%20Maintenance%20Guide%2020250318.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes)
---

# Alibaba Cloud Apsara Stack V3.18.3 Elastic Compute Service Operations and Maintenance Guide 20250318

## Table of Contents

- 1 Log on to the Apsara Uni-manager Operations Console
- 2 ECS operations and maintenance
  - 2.1 Computing overview
  - 2.2 Cluster O&M
    - 2.2.1 View computing clusters
    - 2.2.2 Log on to the AG of a cluster
    - 2.2.3 Manage computing clusters
      - 2.2.3.1 Get an overview of a computing cluster
      - 2.2.3.2 Manage cluster configurations
        - 2.2.3.2.1 View cluster configurations
        - 2.2.3.2.2 View change records
      - 2.2.3.3 Manage computing servers
        - 2.2.3.3.1 View computing servers
        - 2.2.3.3.2 Manage server status
  - 2.3 Computing servers
    - 2.3.1 Manage computing servers
      - 2.3.1.1 View computing servers
      - 2.3.1.2 View O&M details about a computing server
      - 2.3.1.3 Lock a server
      - 2.3.1.4 Unlock a server
      - 2.3.1.5 Activate a computing server
      - 2.3.1.6 Migrate all instances from a computing server
      - 2.3.1.7 Deactivate a physical machine for maintenance
      - 2.3.1.8 View audit logs
    - 2.3.2 View computing server-level migration tasks
  - 2.4 ECS
      - 2.4.1.1 View ECS instances
      - 2.4.1.2 View the details of an instance
      - 2.4.1.3 Manage instance status
        - 2.4.1.3.1 Start instances
        - 2.4.1.3.2 Stop an instance
        - 2.4.1.3.3 Restart an instance
      - 2.4.1.4 Migrate an instance
      - 2.4.1.5 View the migration history of an instance
      - 2.4.1.6 Manage ISOs
      - 2.4.1.7 Use the rescue mode
    - 2.4.2 Disks
      - 2.4.2.1 View disks
      - 2.4.2.2 View disk details
      - 2.4.2.3 Detach a disk
      - 2.4.2.4 Create a snapshot
      - 2.4.2.5 View snapshots
    - 2.4.3 Images
      - 2.4.3.1 Overview
      - 2.4.3.2 View images
      - 2.4.3.3 View ISO details
    - 2.4.4 Snapshots
      - 2.4.4.1 Overview
      - 2.4.4.2 View snapshots
      - 2.4.4.3 Delete snapshots
      - 2.4.4.4 Create an image
      - 2.4.4.5 View audit logs
      - 2.4.4.6 View automatic snapshot policies
    - 2.4.5 ENIs
      - 2.4.5.1 View the details of an ENI
      - 2.4.5.2 Unbind an ENI
      - 2.4.5.3 Release an ENI
      - 2.4.5.4 View audit logs
    - 2.4.6 Security groups
      - 2.4.6.1 Overview
      - 2.4.6.2 View the details of a security group
      - 2.4.6.3 View audit logs
    - 2.4.7 Custom instance types
      - 2.4.7.1 Add a custom instance type
      - 2.4.7.2 View a custom instance type
      - 2.4.7.3 Disable custom instance types
      - 2.4.7.4 View audit logs
    - 2.4.8 View O&M audit Logs
  - 2.5 Control and monitoring
  - 2.6 Analyze the computing capacity
  - 2.7 Migration task management
    - 2.7.1 Manage migration tasks
      - 2.7.1.1 Migrate an ECS instance
      - 2.7.1.2 Create a computing server-level migration task
      - 2.7.1.3 Create a batch migration task
      - 2.7.1.4 View migration tasks
      - 2.7.1.5 Stop a migration task
    - 2.7.2 Configure migration constraints
    - 2.7.3 View CPU compatibility configurations
  - 2.8 Computing O&M configurations
    - 2.8.1 View monitoring settings
    - 2.8.2 Configure O&M actions
      - 2.8.2.1 Configure throttling for a proactive O&M action
      - 2.8.2.2 Configure the approval process for a proactive O&M action
      - 2.8.2.3 Submit a proactive O&M event for a server
  - 2.9 View the computing O&M data
  - 2.10 AI/HPC O&M
    - 2.10.1 Manage cluster data replication tasks on a client
    - 2.10.2 Manage ACL whitelists for an RDMA network
- 3 VM hot migration
  - 3.1 Overview
  - 3.2 Limits
  - 3.3 Complete hot migration on AG
  - 3.4 Modify the position of the NC where the VM is located
  - 3.5 FAQ
- 4 Hot migration of disks
  - 4.1 Overview
  - 4.2 Limits
  - 4.3 O&M after hot migration
- 5 Upgrade solution
  - 5.1 Overview
  - 5.2 Limits on GPU clusters
  - 5.3 Limits on FPGA clusters
- 6 Handle routine alarms
  - 6.1 Overview
  - 6.2 API proxy
  - 6.3 API Server
  - 6.4 RegionMaster
  - 6.5 PYNC
  - 6.6 AGs
  - 6.7 Server groups
- 7 Inspection
  - 7.1 Overview
  - 7.2 Cluster basic health inspection
    - 7.2.1 Overview
    - 7.2.2 Monitoring inspection
    - 7.2.3 Inspection of basic software package versions
    - 7.2.4 Inspections of basic public resources
  - 7.3 Cluster resource inspection
    - 7.3.1 Overview
    - 7.3.2 Cluster inventory inspection
    - 7.3.3 VM inspection
  - 7.4 What do I do if a split-brain issue occurs in the data centers in which ECS is deployed in disaster recovery mode?

ager Operations Console

## 1 Log on to the Apsara Uni-manager Operations Console

**manager Operations Console**

This topic describes how to log on to the Apsara Uni-manager Operations Console.

**Prerequisites**

The endpoint of the Apsara Uni-manager Operations Console and the username and password used to log on to the console are obtained from the deployment engineer or an administrator. The endpoint of the Apsara Uni-manager Operations Console is in the following format: regi on-id.ops.console.intranet-domain-id. A web browser. We recommend that you use Google Chrome.
1. Open your browser.
2. In the address bar, enter the endpoint of the Apsara Uni-manager Operations Console.
Press the Enter key. ager Operations Console

> **Note:** You can click the current language in the upper-right corner to switch to another language. Simplified Chinese, English, and Traditional Chinese are supported.

3. Enter your username and password.

> **Note:** Obtain the username and password that are used to log on to the Apsara Uni-manager Operations Console from the deployment engineer or an administrator.

If you log on to the Apsara Uni-manager Operations Console for the first time, you must change the password of your username. To enhance security, your password must meet the following requirements: The password contains uppercase and lowercase letters. The password contains digits. ager Operations Console The password contains at least one of the following special characters: ! @ # $ % The password is 10 to 20 characters in length.
4. Click **Log On**.

## 2 ECS operations and maintenance

**maintenance**

### 2.1 Computing overview

This topic describes the Computing Overview page of the Compute Operations Console. On the Computing Overview page, you can obtain a high-level overview of services in IaaS O&M, stay updated with service status, and view service information, such as diagnostic results, alerts, inventory usage, key metrics, and health status.

## 1 Log on to the Apsara Uni-manager Operations Console.

2. In the top navigation bar, choose **Product Operation > Computing > Compute**
3. In the **Service Check** section, view the diagnostic score that is displayed on the dashboard
and the numbers of check items that are in the Normal, Risk, Abnormal, and Suggestions states.

> **Note:** If the diagnostic score is 100, the dashboard is displayed in green. If the diagnostic score is lower than 100, the dashboard is displayed in red.

In the upper-right corner of the section, click **Check Now**. In the **Service Check** dialog box, view the updated diagnostic score on the dashboard, status of each check item, and exception details.
4. In the **Unhandled Alerts Today** section, view the statistics of alerts at all risk levels.
In the upper-right corner of the section, click **View Details**. You are redirected to the Alerts page. You can also choose **Monitor&Alarms > Alarm Mmanagement > Alarm List** in the top navigation bar of the Apsara Uni-manager Operations Console to go to the Alerts page.
5. In the **One-click Search** section, enter the ID or IP address of a resource in the search box,
such as instance ID, disk ID, image ID, elastic network interface (ENI) ID, security group ID, private or public IP address of an Elastic Compute Service (ECS) instance, or IP address of a physical server. In the search result, click the resource to go to the details page. On the page that appears, view the information about the resource.
6. In the **Allocated Capacity Ratio** section, view the usage of vCPUs, memory, and elastic IP
addresses (EIPs) for clusters. You can also view the number of used resources, number of available resources, and total number of resources.

> **Note:** By default, the metric statistics of all clusters are displayed. To view the statistics only of a cluster, select the cluster from the drop-down list in the upper-right corner of this section.

The following table describes the metrics.

| Metric | Description |
|---|---|

| stic Compute Service | Operations and Maintenance Gu de·ECS operations and mainten nc |
|---|---|

| vCPU (Cores) | The number of vCPUs. vCPUs are the components of VMs. |
|---|---|
| Memory (GB) | The memory size. |
| EIPs | The number of EIPs. |

7. In the **Core Metrics** section, view the total number of clusters and the numbers of
computing clusters, storage clusters, and hybrid clusters. You can also view the total number of computing servers, the numbers of computing servers in the Normal, Mlock, and NC Downtime states, the total number of ECS instances, and the numbers of ECS instances in the Running, Stopped, and Pending states. Perform the following operations to view details: Click the value of **Total Number of Clusters** to view cluster details on the **Computing**
**Cluster O&M** page.
Click the value of **Total Number of Computing Servers** to view server details on the
**Computing Server O&M** page.
Click the value of **Total Number of ECS Instances** to view instance details on the **ECS**
**Instances** page.
8. In the **Health Status of Services** section, view the health status of each service.
Click the name of a service that you want to view. In the **Deploy Servers** dialog box, view information about the service, including the service status, server role, IP address of the physical server on which the service is deployed, hostname, cluster, description, and the Apsara Stack service to which the service belongs.

### 2.2 Cluster O&M

#### 2.2.1 View computing clusters

This topic describes how to query and view information about all computing clusters, including the total number of clusters, the number of clusters that are not in the final state, the number of clusters that are in the final state, the cluster names, cluster types, and cluster instance types.
2. In the top navigation bar, choose **Product Operation > Computing > Compute**
3. In the left-side navigation pane, click **Computing Cluster O&M**.
By default, the details of all clusters are displayed.
4. In the upper-right corner of the page, view the total number of clusters, the number of
clusters that are not in the final state, and the number of clusters that are in the final state. The number of clusters that are not in the final state is displayed in red.
5. (Optional) Select the items that you want to display in the cluster list and specify a custom
column order. i. In the upper-right corner of the page that appears, click the icon. ii. Select or deselect the items that you want to display in the cluster list. The data of the items displayed in the cluster list is updated in real time.
6. In the upper-left corner of the **Computing Cluster O&M** page, enter the name of a cluster
and click the icon to search for the cluster.
7. View the parameters in te Region, CPU Processor, Cluster Type, Compute Type, Desired
State, Zone, Servers, Instance Family, and Cluster Specifications columns of the cluster.

> **Note:** Take note of the following computing types:
> `CPU` : provides CPU and memory resources for Elastic Compute Service (ECS) instances in the Kernel-based Virtual Machine (KVM) architecture.
> `Local Disk` : provides local storage, CPU, and memory resources for ECS instances in the KVM architecture.
> `GPU` : provides GPU, CPU, and memory resources for ECS instances in the KVM architecture.
> `Converged Computing and Storage` : provides cloud storage, CPU, and memory resources for ECS instances in the KVM architecture.
> `SHENLONG` : provides CPU and memory resources for ECS instances in the Shenlong architecture.
> `VMOC` : provides CPU and memory resources for ECS instances in the VMOC architecture. The VMOC architecture can be deployed on non- Shenlong physical machines to provide computing power for ECS instances.
> Take note of the following cluster specifications:
> `share,ncTypeHybrid` specifies the shared cluster.
> `pin,exclusive,ncTypeHybrid` specifies the exclusive cluster.
> `bare_metal` specifies the bare metal cluster.

View the details of the cluster. Find the cluster that you want to view and click the cluster name in the **Cluster**
**Name/Alias** column. The **Overview** tab of the Computing Cluster Details page is
displayed. You can view the basic information, instance resources, and inventory information of the cluster. For more information, see Get an overview of a computing cluster. View the configurations and configuration change records of a cluster. Find the cluster that you want to view and click the cluster name in the **Cluster**
**Name/Alias** column. On the details page of the cluster, click the **Configurations** tab.
You can view the configurations of a cluster and the change records of the cluster configurations. For more information, see Manage cluster configurations. Manage computing servers. On the Clusters page, find the cluster that you want to view and click the cluster name in the **Cluster Name/Alias** column. On the details page of the cluster, click the
**Computing Servers** tab. You can view the basic information and O&M details of a
computing server in a cluster, or manage the business status of a computing server, such as manually locking a network computer (NC). For more information, see Manage computing servers. Log on to the Admin Gateway (AG) of the cluster that you want to manage to perform simple O&M on VMs. For more information, see Log on to the AG of a cluster.

#### 2.2.2 Log on to the AG of a cluster

You can log on to the Admin Gateway (AG) of a cluster to go to the Terminal Service page. Then, you can perform O&M operations on virtual machines (VMs) in the cluster by using the CLI. This topic describes how to log on to the AG of a cluster from the Computing Clusters page.
2. In the top navigation bar, choose **Product Operation > Computing > Compute**
3. In the left-side navigation pane, click **Computing Cluster O&M**.
By default, the details of all clusters are displayed.
4. On the page that appears, find the cluster that you want to manage and click **Connect to**
**Cluster AG** in the **Operation** column.
The Terminal Service page appears.
5. In the left-side navigation pane, click vmXXX. Then, specify the O&M operation that you
want to perform in the CLI on the right side.

> **Note:** vmXXX indicates the VM ID.

#### 2.2.3 Manage computing clusters

##### 2.2.3.1 Get an overview of a computing cluster

In the Compute Operations Console, you can view the details of a computing cluster on the Overview tab of the Computing Cluster Details page. The details include the basic information of the cluster, statistics about computing server resources, numbers of Elastic Compute Service (ECS) instances, distribution of physical servers by state, distribution of ECS instances by state, inventory utilization, and inventory of instances by instance type.
2. In the top navigation bar, choose **Product Operation > Computing > Compute**
3. In the left-side navigation pane, click **Computing Cluster O&M**.
4. Find the cluster that you want to view and click the cluster name in the **Cluster Name**
column. By default, the **Overview** tab of the **Computing Cluster Details** page is displayed.
5. View the basic information of the computing cluster and the information about computing
servers and ECS instances in the cluster. In the **Cluster Information** section, view the basic information of the cluster, including the region, type, zone, and network type of the cluster, and whether the cluster is an All in ECS 1.0 cluster. In the upper-right corner of this section, click **Connect to Cluster AG** to log on to the Admin Gateway (AG) and perform O&M on the cluster. For more information, see Log on to the AG of a cluster. In the **Server Resources** section, view the number of computing servers, the number of CPU cores, and the available memory. In the **ECS Instances** section, view the total number of ECS instances, the number of running ECS instances, and the number of abnormal ECS instances. In the **NC State Distribution** section, view the distribution of physical servers in different states.

> **Note:** Move the pointer over the chart. The number of physical servers in each state is displayed.

The following table describes the states of physical servers.

| State | Description |
|---|---|
| Failover | The physical server is down. |

| Normal | The physical server runs as expected. You can schedule instances to the physical server. |
|---|---|
| No heartbeat | The physical server has no heartbeats. |
| Mlock | The physical server is locked for maintenance purposes. |
| Rlock | The physical server is forcefully reserved and can be used to recover or modify VMs. When the resources of the physical server are insufficient, the physical server performs defragmentation. Otherwise, an alert is generated. The physical server must have heartbeats and remain available. |
| Initializing | The physical server is being initialized. |

In the **ECS Instance State Distribution** section, view the distribution of ECS instances in different states. The following table describes the states of ECS instances.

| State | Description |
|---|---|
| Running | The instance runs as expected. |
| Stopped | After an instance is stopped or after an instance is created but not started, the instance is in the Stopped state. Instances in the Stopped state cannot provide external services. |
| Pending | After an instance is created, the instance is in the Pending state before it enters the Running state. If the instance remains in the Pending state for an extended period of time, an exception occurs. |
| Creating | After you start or restart an instance in the ECS console or by calling an API operation, the instance enters the Creating state before it enters the Running state. If the instance remains in the Creating state for an extended period of time, an exception occurs. |
| Stopping | After you stop an instance in the ECS console or by calling an API operation, the instance enters the Stopping state before it enters the Stopped state. If the instance remains in the Stopping state for an extended period of time, an exception occurs. |
| Releasing | After you release an instance, the instance enters the Releasing state before it enters the Released state. |

In the **Inventory Utilization** section, view the total amount of resources, the amount of used resources, and the percentage of used resources in all resources. In the **Inventory** section, view the inventory details of instances by instance type in the cluster.

##### 2.2.3.2 Manage cluster configurations

###### 2.2.3.2.1 View cluster configurations

This topic describes how to view the configurations of a cluster, including the values of configuration items and the time when configuration items were last modified.
2. In the top navigation bar, choose **Product Operation > Computing > Compute**
3. In the left-side navigation pane, click **Computing Cluster O&M**.
4. Find the cluster that you want to view and click the cluster name in the **Cluster Name**
column. The **Overview** tab of the **Computing Cluster Details** page is displayed.
5. In the upper-left corner of the tab, click the **Configurations** tab.
The **Configurations** tab is displayed.
6. View the values of configuration items and the time when configuration items were last
modified.

###### 2.2.3.2.2 View change records

This topic describes how to view the configuration change records of a cluster.
2. In the top navigation bar, choose **Product Operation > Computing > Compute**
3. In the left-side navigation pane, click **Computing Cluster O&M**.
4. Find the cluster that you want to view and click the cluster name in the **Cluster Name**
column. The **Overview** tab of the **Computing Cluster Details** page is displayed.
5. Click the **Configurations** tab.
The **Cluster Configurations** tab is displayed.
6. Click the **Change Records** tab. All the configuration change records of the cluster are
displayed.
7. In the upper-left corner of the tab, enter a ticket ID in the search box and click the
icon. View the values of configuration items and the time when the configuration items were changed.

##### 2.2.3.3 Manage computing servers

###### 2.2.3.3.1 View computing servers

You can view a list of computing servers in a computing cluster and the details of each computing server. The details include server basic information, O&M details, and information about Elastic Compute Service (ECS) instances that are deployed on the computing server.
2. In the top navigation bar, choose **Product Operation > Computing > Compute**
3. In the left-side navigation pane, click **Computing Cluster O&M**.
4. Find the cluster that you want to view and click the cluster name in the **Cluster Name**
column. The **Overview** tab of the **Computing Cluster Details** page is displayed.
5. Click the **Computing Servers** tab.
6. View the list of computing servers.
i. **Optional:**Change the columns that are displayed in the list. a. In the upper-right corner of the tab, click the icon. b. In the **Custom list item display** dialog box, select the columns that you want to display in the computing server list. c. Click **OK**. ii. View the following details of a computing server in the cluster: hostname, IP address, NC ID, NC type, number of vCPUs, memory size, status, number of instances, data center, rack, and serial number (SN). For information about the status of computing servers, see Get an overview of a computing cluster.
7. View O&M details about a computing server and the details of ECS instances that are
deployed on the computing server. View O&M details about a computing server. a. Find the computing server that you want to view and click the server name in the
**Hostname** column.
b. View O&M details about the computing server on the **Computing Server Details** page. For more information, see View O&M details about a computing server. View the details of the ECS instances that are deployed on the computing server. a. Click the number in the **Instances** column. b. In the **Instance List** panel, view the values in the Instance ID, Status, Instance Name, CPU, and Memory columns for instances. c. To view the details of an ECS instance, click the instance ID in the **Instance ID** column. The **Instance Details** page appears, which displays the basic information and configurations of the instance. For more information, see View the details of an instance.

###### 2.2.3.3.2 Manage server status

This topic describes how to manage the status of computing servers (NCs) in a cluster. You can manually lock, unlock, and activate computing servers.
2. In the top navigation bar, choose **Product Operation > Computing > Compute**
3. In the left-side navigation pane, click **Computing Cluster O&M**.
4. Find the cluster that you want to manage and click the cluster name in the **Cluster Name**
column. The **Overview** tab of the **Computing Cluster Details** page appears.
5. In the upper-left corner of the page, click the **Computing Servers** tab.
6. Manage the business status of servers. The following table describes the operations that
you can perform on computing servers.

| Option | Description | Procedure |
|---|---|---|
| Lock NC | You can lock abnormal servers to prevent instances from being scheduled to these servers. If the servers are locked, the status of the servers cannot be automatically changed. You can also lock servers for which you want to reserve resources. | i. On the Computing Servers tab, find the server that you want to lock and click Lock NC in the Operation column. ii. In the Lock NC dialog box, select a lock state and configure the Changed By, Change Ticket Title, and Reason parameters. iii. Click OK. |
| Unlock NC | You can unlock servers in the no heartbeat, mlock, and rlock states. After you unlock a server, the server is automatically activated and you can schedule instances to the server. | i. On the Compute Servers tab, find the server that you want to unlock and click Unlock NC in the Operation column. ii. In the Unlock NC dialog box, enter a reason for unlocking the server. iii. Click OK. |
| Business Launch | You can activate servers in the no heartbeat, mlock, rlock, failover, and initializing states. | i. On the Computing Servers tab, find the server that you want to activate and click Business Launch in the Operation column. ii. In the dialog box that appears, configure the Reason parameter. iii. Click OK. |

### 2.3 Computing servers

#### 2.3.1 Manage computing servers

##### 2.3.1.1 View computing servers

You can view a list of computing servers and the details of each computing server. The details include the hostname, IP address, model, number of vCPUs, memory size, architecture, status, and computing cluster to which the computing server belongs.
2. In the top navigation bar, choose **Product Operation > Computing > Compute**
3. In the left-side navigation pane, click **ECS O&M**.
The **Machines** tab of the Computing Servers page is displayed. View the details of all computing servers on the tab.
4. In the upper-right corner of the Computing Servers page, view the total number of
computing servers and the numbers of computing servers in the free, mlock, and nc_down states.
5. **Optional:**Change the columns that are displayed in the list of computing servers.
i. In the upper-right corner of the tab, click the icon. ii. In the **Custom list item display** dialog box, select the columns that you want to display in the computing server list. iii. Click **OK**.
6. In the upper-left corner of the Machines tab, enter an IP address, a hostname, or a serial
number in the search box and click the icon to search for computing servers. You can also click **Advanced Search** to refine your search. Specify filter conditions, such as a model, data center, and rack, and then click **Search**.
7. In the computing server list, view the following information about each computing server:
hostname, IP address, model, number of vCPUs, memory size, architecture, status, cluster, data center, rack, serial number (SN), and region. For information about the parameters that are related to the status of computing servers, see Get an overview of a computing cluster.
8. View O&M details about a computing server.
i. Find the computing server you want to view and click the hostname in the **Hostname** column. ii. On the **Computing Server Details** page, view information about the computing server. For more information, see View O&M details about a computing server.

##### 2.3.1.2 View O&M details about a computing server

**server**

This topic describes how to view O&M details about a computing server. The O&M details include business information, hardware information, resource information, Elastic Compute Service (ECS) instances that are deployed on the computing server, performance monitoring information, alert information, control service status, server-level migration tasks, and audited operations. You can perform operations on different tabs.
2. In the top navigation bar, choose **Product Operation > Computing > Compute**
3. In the left-side navigation pane, click **ECS O&M**.
The **Machines** tab of the Computing Servers page is displayed. View the details of all computing servers on the tab.
4. Find the computing server that you want to view and click the name in the **Hostname**
column.
5. View O&M details about the computing server on the Computing Server Details page.
The following table describes the parameters on the page.

| Section or tab | Description |
|---|---|
| Business Information | Displays the following information about the computing server: business ID, IP address, hostname, status, management heartbeat status, selling mode, cluster name, instance type, and operating system. To view the details of the computing cluster to which the computing server belongs, click the cluster name to go to the Computing Cluster Details page. For more information, see the Manage computing clusters chapter. |
| Hardware Information | Displays the following information about the computing server: serial number, model, rack, CPU model, GPU, number of vCPUs, and memory size. |
| Resource Information | Displays the usage of vCPUs and memory of the computing server. |
| ECS Instances | Displays the following information about each ECS instance that is deployed on the computing server: the number of vCPUs, memory size, status, private or public IP address, bandwidth, user information, image, creation time, and whether the instance uses only resources in the All in ECS project. Allows you to perform the following operations on each instance: diagnose the instance, migrate the instance, view migration history, view audit logs, change the instance status, connect to the instance by using Virtual Network Computing (VNC), and manage ISOs. For more information, see the ECS instances chapter. |
| Performance Monitoring | Displays the trend charts of the following performance metrics within a specific period of time: CPU (%), memory (%), system load, network retransmission (%), and network traffic (MB). You can set a start time and an end time in the Date Range field to specify a period of time. |
| Alert Information | Displays the following information about each alert: alert name, alert cause, alert details, first and last times when the alert was reported, and number of times that the alert was reported. |
| Control Service | Displays server roles and their status. You can search for a server role on this tab. Allows you to perform the following operations to view server role information in the Apsara Infrastructure Management console: Find the server role that you want to view and click Apsara Infrastructure Management in the Operation column. The Project & Cluster O&M page is displayed. For more information, see the Clusters chapter in Apsara Infrastructure Management. |

| Machine Migration Task | Displays the following information about each server-level migration task: task ID, number of migrated instances, destination physical machine, task status, migration progress, start time, update time, and task creator. Allows you to perform the following operations to view information about a migration task: Find the migration task that you want to view, click the task ID in the Task ID column, and then view the migration status, destination physical machine, migration type, and number of retries that are displayed in the Migrated Instance Details panel. Note Cold Migration: migrates instances that are in the Pending state. Hot Migration: migrates instances that are in the Running state. Allows you to perform the following operations to rerun a migration task: If a migration task failed, click Restart in the Operation column. In the message that appears, click OK. If you want to cancel the task, click Cancel in the Operation column. In the dialog box that appears, enter a reason and click OK. |
|---|---|
| Operation Audit | Displays information about the audited operations. In the O&M of the computing server, the operations that may cause risks are audited. You can view the historical operations in the Apsara Uni- manager Operations Console, historical POP API calls, and historical server controller API calls. For more information, see View O&M audit Logs. |

##### 2.3.1.3 Lock a server

You can lock servers based on your business requirements. You cannot create instances on locked servers.

**Background information**

Common scenarios in which servers are locked: O&M lock: If an Elastic Compute Service (ECS) instance on a server that enters the mlock state is restarted, the instance is scheduled to another server, except that failover is disabled for the ECS instance. Resource reservation lock: If normal servers cannot be used for failover, the servers in the rlock state are used to restore instances that go down.
2. In the top navigation bar, choose **Product Operation > Computing > Compute**
3. In the left-side navigation pane, click **ECS O&M**.
The **Machines** tab of the Computing Servers page is displayed. View the details of all computing servers on the tab.
4. Find the server that you want to lock and click **Lock** in the **Operation** column.
5. In the **Lock NC** dialog box, configure the Lock Status, Changed By, Change Ticket Title, and
Locking Reason parameters.
6. Click **OK**.

##### 2.3.1.4 Unlock a server

You can unlock a server to allow the server to be scheduled. After you unlock a server, the server is automatically activated and you can schedule instances to the server.

**Background information**

Only servers in the No Heartbeat, mlock, or rlock state can be unlocked.
2. In the top navigation bar, choose **Product Operation > Computing > Compute**
3. In the left-side navigation pane, click **ECS O&M**.
The **Machines** tab of the Computing Servers page is displayed. View the details of all computing servers on the tab.
4. Find the server that you want to unlock, move the pointer over the
icon in the
**Operation** column, and then select **Unlock**.
5. In the **Unlock NC** dialog box, view the IP address of the server and enter the operation
reason in the **Reason** field.
6. Click **OK**.

##### 2.3.1.5 Activate a computing server

This topic describes how to activate a computing server.

**Prerequisites**

The computing server that you want to activate is in the **mlock** state.

**Background information**

You can activate computing servers that are in the mlock, rlock, no heartbeat, nc_down, and initializing states.
2. In the top navigation bar, choose **Product Operation > Computing > Compute**
3. In the left-side navigation pane, click **ECS O&M**.
The **Machines** tab of the Computing Servers page is displayed. View the details of all computing servers on the tab.
4. Find the computing server that you want to activate, move the pointer over the
icon in the **Operation** column, and then select **Activate**.
5. In the dialog box that appears, confirm the information about the computing server and
enter your reason for the activation operation in the **Reason** field.
6. Click **OK**.

##### 2.3.1.6 Migrate all instances from a computing server

**server**

This topic describes how to migrate all Elastic Compute Service (ECS) instances on a computing server to other computing servers.

**Prerequisites**

The computing server is in the free (normal) or mlock (O&M lock) state.

**Background information**

When you scale down or maintain a computing server, you must migrate all ECS instances on the server before you can perform operations on the server. In this case, you can migrate all ECS instances on the server to other computing servers. When you migrate all instances from a computing server, take note of the following items: After you submit a migration task, the server enters the mlock state. If the migration task is completed, fails, or is canceled, you must submit an application to unlock the server. The ECS instances on the server are migrated to other computing servers based on the ECS scheduling rules. The migration task may not be successful in a single attempt due to various reasons. If an ECS instance in the **Stopped** or **Pending** state is migrated, the system attempts to start the ECS instance and bring the ECS instance to the **Running** state. You cannot specify the computing server to which you want to migrate the ECS instances. After the migration task is completed, you must check for any remaining ECS instances on the original server to ensure that all ECS instances are migrated.
2. In the top navigation bar, choose **Product Operation > Computing > Compute**
3. In the left-side navigation pane, click **ECS O&M**.
The **Machines** tab of the Computing Servers page is displayed. View the details of all computing servers on the tab.
4. Find the computing server that you want to manage, move the pointer over the
icon in the **Operation** column, and then select **Migrate All Instances**. You can also select the server and click **Machine Migration** below the server list.
5. In the **Machine Migration** dialog box, configure the Operated By, Change Ticket Title, and
Reason parameters, select **I have read the preceding notes and confirm this**
**operation**, and then click **OK**.

**What to do next**

After you perform a migration task, you can view the status of the migration task on the Machine Migration Task tab. For more information, see View computing server-level migration tasks.

##### 2.3.1.7 Deactivate a physical machine for maintenance

**maintenance**

This topic describes how to take a physical machine, also known as a computing server, out of service for maintenance by deactivating the physical machine.

**Prerequisites**

At least two physical machines exist in the computing cluster to which the physical machine that you want to deactivate belongs. For information about how to view physical machines in a cluster, see View computing servers.

**Scenarios**

If you cannot repair the fault in a physical machine at the software level and must deactivate the physical machine for maintenance, notify your customer at the earliest opportunity, deactivate and repair the physical machine on site with the approval of the customer, and then reactivate the physical machine to put the physical machine back into service in the computing cluster to which the physical machine belonged before it was deactivated. You can deactivate physical machines only in computing clusters (CPU clusters and SHENLONG clusters) for maintenance, not physical machines in Hybrid, GPU, SCC, or SCC+RDMA clusters.

|   | Note On the Machines tab of the Computing Server O&M page in the Compute Operations Console, you can view the names of clusters in the Cluster column. CPU clusters are named in the ECS-CPU-X-XXXX format, and SHENLONG clusters are named in the ECS- MOC-X-XXXX format. |   |   |
|---|---|---|---|
|   |   | ECS- |   |
|   | MOC-X-XXXX |   |   |

**Considerations**

Before you deactivate a physical machine for maintenance, take note of the following items: When you deactivate a physical machine for maintenance, the Elastic Compute Service (ECS) instances that reside on the deactivated physical machine are automatically migrated to other physical machines in the same cluster as the deactivated physical machine. After the physical machine is repaired and put back into service, the physical machine is automatically added to the cluster to which it belonged before it was deactivated.

> **Warning:** Service interruptions may occur during the instance migration process. Deactivate the physical machine during off-peak hours.

If the destination physical machines to which the ECS instances are migrated have insufficient resources or encounter other issues, the migration fails. In this case, navigate to the Physical Machine Maintenance page in the Compute Operations console, find the physical machine that you want to deactivate, and then click Details in the Operation column. On the maintenance details page of the physical machine, click **Retry** below
**Step3: ncMaintenanceMigrateEcsInstance**. If the retry fails, you must manually
migrate the ECS instances away from the physical machine. After you manually migrate the ECS instances, go back to the maintenance details page of the physical machine and click
**Retry** below **Step3: ncMaintenanceMigrateEcsInstance** to continue deactivating the
physical machine. For information about how to migrate ECS instances, see Migrate all instances from a computing server or Migrate an instance.
2. In the top navigation bar, choose **Product Operation > Computing > Compute**
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Create a Deactivate for Maintenance task.
(Recommend) Deactivate a physical machine for maintenance on the **Physical Machine**
**Maintenance** page.
a. In the left-side navigation pane, choose **ECS Intelligent O&M > ECS Physical**
**Machine Maintenance**.
b. On the **Physical Machine Maintenance** page, click **Create Physical Machine**
**Maintenance Event**.
c. Configure the parameters described in the following table.

| Parameter | Description |
|---|---|
| Cluster | Select the cluster to which the physical machine that you want to deactivate for maintenance belongs. You can select only CPU and SHENLONG clusters. |
| Machine | Select the physical machine that you want to deactivate for maintenance. |
| Operator | Enter the name of the operator who deactivates the physical machine for maintenance. |
| Maintenance Reason | Enter a reason. |

d. Click **OK**. Deactivate a physical machine for maintenance on the **Computing Server O&M** page. a. In the left-side navigation pane, click **ECS O&M**. The **Machines** tab of the Computing Servers page is displayed. View the details of all computing servers on the tab. b. On the Machines tab, find the physical machine that you want to deactivate for maintenance. In the **Operation** column, choose
**> Deactivate for Maintenance**.
c. In the **Deactivate for Maintenance** dialog box, confirm the information of the physical machine, including the **Hostname** and **Cluster** parameters, and configure the
**Reason** and **Operator** parameters.
d. Click **OK**.
5. On the **Physical Machine Maintenance** page, find the physical machine and click
**Details** in the **Operation** column.
In the **Basic Information** section of the page that appears, you can view the IP address, maintenance event ID, and maintenance status of the physical machine.
6. In the **Execution Information** section, view the procedure of deactivating the physical
machine for maintenance. If **Step5: offlineEcsNc** is complete, the physical machine is deactivated in its cluster and you can repair the physical machine.

> **Note:** Take note of the following steps in the deactivation procedure:
> **Step1: ncOfflinePreCheck**: If the physical machine does not meet the requirements for deactivation, the physical machine fails the check.
> **Step3: ncMaintenanceMigrateEcsInstance**: If the ECS instances fail to be migrated away from the physical machine, we recommend that you click **Retry** below **Step3: ncMaintenanceMigrateEcsInstance** to migrate the instances again. You can also manually migrate the ECS instances and then click **Retry** below **Step3: ncMaintenanceMigrateEcsInstance**. For information about how to migrate ECS instances, see Migrate all instances from a computing server or Migrate an instance.
> **Step4: offlineTianjiNc**: This step takes the physical machine out of service in Apsara Infrastructure Management and requires an extended period of time to complete. View the status of the physical machine in the Apsara Infrastructure Management console.

7. After you confirm that the physical machine is repaired, you must go to **Step6:**
**AsoAuthorizationWork** on the maintenance details page and click **Maintenance**
**Completed**. In the message that appears, click **OK**.
The procedure of deactivating the physical machine for maintenance is automatically executed. When **Step9: Finish** is complete, the procedure is complete and the physical machine is automatically added back to its original computing cluster.

> **Note:** If **Step8: expandTianjiClusterMachineExternal** remains in the **Waiting** (**rolling**) state, check the status and the **rolling** progress of the computing cluster to which the physical machine belongs.

##### 2.3.1.8 View audit logs

Server O&M operations that may introduce risks are audited. You can view the historical operations in the Apsara Uni-manager Operations Console, historical POP API calls, and historical server controller API calls for a computing server.
2. In the top navigation bar, choose **Product Operation > Computing > Compute**
3. In the left-side navigation pane, click **ECS O&M**.
The **Machines** tab of the Computing Servers page is displayed. View the details of all computing servers on the tab.
4. Find the computing server for which you want to view audit logs and click **Audit**
**Operations** in the **Operation** column.
5. In the **Audit Operations** panel, view audit logs.
For more information, see View O&M audit Logs.

#### 2.3.2 View computing server-level migration tasks

**tasks**

After you run a task to migrate all instance from a computing server, also known as a physical machine, you can check the progress and results of the migration task. You can also view the details of all instances and O&M details about the computing servers that are associated with the migration task.
2. In the top navigation bar, choose **Product Operation > Computing > Compute**
3. In the left-side navigation pane, click **ECS O&M**.
The **Machines** tab of the Computing Servers page is displayed. View the details of all computing servers on the tab.
4. Click the **Machine Migration Task** tab to view the details of a computing server-level
migration task.
5. The details include the task ID, source physical machine, number of instances, destination
physical machine, task status, migration progress, task start time, and the user who initiates the task.

> **Note:** If the migration task failed, we recommend that you click **Migrate All** **Instances** to re-run the migration task.

### 2.4 ECS

#### 2.4.1 VM

##### 2.4.1.1 View ECS instances

This topic describes how to search for Elastic Compute Service (ECS) instances and view information about the instances, such as the physical machines (computing servers) on which the instances reside, the clusters to which the instances belong, and the hostnames, aliases, status, networks, and bandwidth of the instances.
2. In the top navigation bar, choose **Product Operation > Computing > Compute**
3. In the left-side navigation pane, choose **ECS O&M > ECS Instances**.
In the upper-right corner of the ECS Instances page, view the total number of ECS instances and the numbers of ECS instances that are in the Running, Stopped, Creating, and Releasing states.

> **Note:** The total number of ECS instances that is displayed in the upper-right corner may be different from the number of ECS instances that are displayed in the instance list. The total number of ECS instances that is displayed in the upper-right corner is accurate and prevails.

4. In the upper-left corner of the ECS Instances page, enter an instance ID, private IP
addresses, or public IP addresses in the search box to search for ECS instances. If you enter multiple IP addresses in the search box, separate the IP addresses with commas (,). You can also click **Advanced Search** and configure parameters, such as **State in**
**Business Foundation System**, **VPC**, and **Apsara Stack Tenant Account ID** to perform
a refined search. You can also select **All in ECS 1.0** or **All in ECS 2.0** in the upper-right corner of the ECS Instances page to narrow down the scope of search results.

> **Note:** **All in ECS 1.0**: indicates Heavenly Palace Adapter 1.0, which is the basic architecture for deploying On ECS services. You can deploy On ECS services on Heavenly Palace Adapter 1.0 only in the Apsara Infrastructure Management console. Heavenly Palace Adapter 1.0 acts as an agent for cloud services to request resources from ECS and exclusively occupies ECS clusters during the resource requests. ECS instances in the clusters are owned by Heavenly Palace Adapter 1.0 accounts and deployed in virtual private clouds (VPCs).
> **All in ECS 2.0**: indicates Heavenly Palace Adapter 2.0, which is the advanced architecture for deploying On ECS services. You can deploy On ECS services on Heavenly Palace Adapter 2.0 in the Apsara Infrastructure Management console or by using Kubernetes cloud-native. Heavenly Palace Adapter 2.0 simplifies resource lifecycle management by using Infrastructure as Code (IaC) baseline declarations and shares tenant-side ECS clusters when using resources. ECS instances in the clusters are owned by Heavenly Palace Adapter 2.0 accounts and deployed in VPCs.

5. (Optional) Change the columns that are displayed in the ECS instance list.
i. In the upper-right corner of the ECS Instances page, click the icon. ii. In the **Custom list item display** dialog box, select the columns that you want to display in the ECS instance list. iii. Click **OK**.
6. View the values in the Host, Host Name/Alias, Cluster, CPU/Memory, Status, Private IP/Public
IP Address, RDMA IP, and Bandwidth columns corresponding to an ECS instance. View the details of an ECS instance. On the **ECS Instances** page, click the ID of an ECS instance in the **Instance ID/Name** column to view the details of the instance on the Instance Details page. For more information about instances, see View the details of an instance. View the O&M details of the computing server that hosts an ECS instance. On the **ECS Instances** page, click the **NC IP** address in the **Host** column corresponding to an ECS instance to view the O&M details of the computing server that hosts the instance on the Computing Server Details page. For more information, see View O&M details about a computing server. View the O&M details of the computing cluster to which an ECS instance belongs. On the **ECS Instances** page, click the cluster name in the **Cluster** column corresponding to an ECS instance to view the O&M details of the computing cluster to which the instance belongs on the Computing Cluster Details page. For more information, see Overview of computing clusters.

##### 2.4.1.2 View the details of an instance

This topic describes how to view the details of an Elastic Compute Service (ECS) instance and perform operations on the instance.
2. In the top navigation bar, choose **Product Operation > Computing > Compute**
3. In the left-side navigation pane, choose **ECS O&M > ECS Instances**.
4. On the ECS Instances page, click the ID of the instance whose details you want to view in
the **Instance ID/Name** column.
5. **(Optional)** In the upper-right corner of the Instance Details page, perform operations on
the instance. The following table describes the operations that you can perform on the instance.

| Operation | Procedure |
|---|---|
| Migrate | Click Migrate. For more information, see Migrate an instance. |
| Connect to AG | Click Connect to AG. For more information, see Log on to the AG of a cluster. |
| Change Instance Status | Click More actions and then select Start, Stop, or Restart. For more information, see Start an instance, Stop an instance, or Restart an instance. You can also select multiple instances on the ECS Instances page and select an option to change the status of the instances at the same time in the lower part of the page. |
| Manage ISO | Choose More actions > Manage ISO. For more information, see Manage ISOs. |
| Diagnose | Click Diagnose. For more information, see Diagnose exceptions on a host or an ECS instance. |

6. View the details of the ECS instance and perform operations based on your business
requirements. The following table describes the sections and tabs on the Instance Details page.

| Section or tab | Description |
|---|---|
| Basic Information | In this section, you can view the basic information of the instance, such as the instance ID, name, specifications, region, zone, and creation time. |
| Configurations | In this section, you can view the configurations of the instance, such as the I/O optimization attribute, image, operating system, system disk, network type, internal bandwidth, private IP address, and Remote Direct Memory Access (RDMA) IP address of the instance. |
| Disks | On this tab, you can view cloud disk information and perform operations on the disks. The information of each cloud disk includes the cloud disk ID, disk type, status, cluster, and features. The operations that you can perform on the cloud disks include detaching the cloud disks, auditing operations that involve the cloud disks, creating snapshots for the cloud disks, and viewing snapshots of the cloud disks. For more information, see the topics under ECS operations and maintenance > ECS > Disks. |
| ENIs | On this tab, you can view elastic network interface (ENI) information and perform operations on the ENIs. The information of each ENI includes the ENI ID, MAC address, ENI status, ENI type, vSwitch, and IP addresses. The operations that you can perform on the ENIs include unbinding the ENIs and auditing operations that involve the ENIs. For more information, see the topics under ECS operations and maintenance > ECS > ENIs. |
| Security Groups | On this tab, you can view security group information and perform operations on the security groups. The information of each security group includes the security group ID, security group name, network type, virtual private cloud (VPC) ID, and creation time. The operations that you can perform on the security groups include auditing operations that involve the security groups. For more information, see the topics under ECS operations and maintenance > ECS > Security groups. |

| Snapshots | On this tab, you can view snapshot information and perform operations on the snapshots. The information about each snapshot includes the snapshot ID, snapshot name, snapshot ID in the server controller, and snapshot type. The operations that you can perform on the snapshots include viewing the snapshots, deleting the snapshots, creating images from the snapshots, viewing the snapshot policies, and viewing auditing operations that involve the snapshots. For more information, see the topics under ECS operations and maintenance > ECS > Snapshots. |
|---|---|
| Performance Monitoring | On this tab, you can view the charts that show the instance performance during a specific period of time from the following aspects: CPU utilization, disk read/write (byte/s), disk IOPS, public bandwidth (bit/s), and internal bandwidth (bit/s). |
| ASO Migration Tasks | On this tab, you can view the status and result of a migration task related to the instance after the migration task is triggered in the Apsara Uni-manager Operations Console. The information of each migration task includes the source NC ID and IP address, destination NC ID and IP address, and migration type, which can be hot migration or cold migration. |
| ASO Migration Tasks | On this tab, you can view the historical migration tasks that were created for the instance during the instance lifecycle, including cold and hot migration tasks. The information of each historical migration task includes the source NC information, destination NC information, task status, migration time, end time, and migration reason. |
| Audit Operations | On this tab, you can view the historical operations that were performed on the instance in the Apsara Uni-manager Operations Console and the historical POP API calls and historical Server Controller API calls that were made for the instance. For more information, see Audit logs. |
| Associated Resources | On this tab, the topology of instance-specific resources is displayed, such as the account, VPC, ECS instance, computing servers, cluster, and ENIs. |

##### 2.4.1.3 Manage instance status

###### 2.4.1.3.1 Start instances

If an Elastic Compute Service (ECS) instance is in a state in which the instance cannot provide services, such as the Stopped state, you must start the instance before you can use the instance.

**Prerequisites**

The instance is in the **pending**, **stopped**, or **failed to start** state.
2. In the top navigation bar, choose **Product Operation > Computing > Compute**
3. In the left-side navigation pane, choose **ECS O&M > ECS Instances**.
4. Find the instance that you want to manage, move the pointer over the
icon in the
**Operation** column, and then select **Start**.
You can also select multiple instances and click **Start** in the lower part of the page to batch start the instances.
5. In the dialog box that appears, enter a reason for the operation in the **Reason** field.
6. Click **OK**.

###### 2.4.1.3.2 Stop an instance

You can stop the instances that are not used.

**Prerequisites**

The instance that you want to stop is in the **Running** state.

> **Important:** The stop operation may interrupt the applications that are running on instances. Perform this operation during off-peak hours to minimize the impact on services.

2. In the top navigation bar, choose **Product Operation > Computing > Compute**
3. In the left-side navigation pane, choose **ECS O&M > ECS Instances**.
4. Find the instance that you want to stop, move the pointer over the
icon in the
**Operation** column, and then select **Stop**.
You can also select multiple instances and click **Stop** in the lower part of the page to batch stop the instances.
5. In the dialog box that appears, enter a reason for the stop operation in the **Reason** field.
6. Click **OK**.

###### 2.4.1.3.3 Restart an instance

After you change the logon passwords or install system updates for instances, you must restart the instances.

**Prerequisites**

The instance that you want to restart is in the **Running** state.

> **Warning:** The restart operation stops the instance for a short period of time and interrupts services that are running on the instance. Proceed with caution.

2. In the top navigation bar, choose **Product Operation > Computing > Compute**
3. In the left-side navigation pane, choose **ECS O&M > ECS Instances**.
4. Find the instance that you want to restart, move the pointer over the
icon in the
**Operation** column, and then select **Restart**.
You can also select multiple instances and click **Restart** in the lower part of the page to batch restart the instances.
5. In the dialog box that appears, select a restart mode and enter a reason for the restart
operation.
6. Click **OK**.

##### 2.4.1.4 Migrate an instance

If an Elastic Compute Service (ECS) instance or a physical server that hosts an ECS instance fails, you can migrate the instance from one server to another server to ensure system stability. You can hot migrate or cold migrate an instance based on the status of the instance. This topic describes how to migrate a single ECS instance. For more information about how to migrate multiple ECS instances at a time or migrate all instances on a physical server, see Create a batch migration task or Create a computing server-level migration task.
2. In the top navigation bar, choose **Product Operation > Computing > Compute**
3. In the left-side navigation pane, choose **ECS O&M > ECS Instances**.
4. On the ECS Instances page, find the instance that you want to migrate and choose **Migrate**
**> Migrate Instance** in the **Operation** column.
5. On the **Create ECS Migration Task** page, configure the parameters.
The **Cold Migration** or **Hot Migration** tab is automatically displayed based on the status of the instance. The following tables describe the corresponding parameters.
**Cold Migration**: Only instances in the **Pending** or **Stopped** (Shutted) state can be
migrated.

| Section | Parameter | Description |
|---|---|---|

| Instance Information | Select Instance | The ID of the ECS instance to be migrated. The system automatically fills the instance ID in the search box. This way, you can directly select the instance in the instance list. You can also specify the ID of another instance based on your business requirements. Important You can select only one ECS instance. |
|---|---|---|

| Destination Selection | Destination Selection Policy | Random Selection: The system selects a random physical machine in which resources are sufficient. This is the default value. System Recommendation: Select one of the physical servers that have a high migration success rate and are recommended by the system. Important If no data is displayed in the physical machine list, no physical machines are available. We recommend that you select another policy. Specify NC: Specify the physical machine to which you want to migrate the instance. Search for the destination machine based on the cluster, hostname, NC IP address, or NC ID above the NC list, and then select an NC as the destination physical machine. Note The system provides suggestions for each physical machine, but does not select a destination physical machine. You can select a physical machine that is not recommended if necessary for business reasons. Specify Cluster: Specify the cluster to which the instance is migrated. Search for and select the cluster based on the cluster name above the cluster list. Note The system provides suggestions on each cluster but does not select a cluster. You may also select a cluster that is not recommended based on your business requirements. |
|---|---|---|
|   | Recovery Mode | The state that you want the instance to restore after migration. Start after Migration Stop After Migration |
| Operation Information | Reason | The reason for cold migration. |

**Hot Migration**: migrates instances that are in the **Running** state.

| Section | Parameter | Description |
|---|---|---|
| Instance Information | Select Instance | The ID of the ECS instance to be migrated. The system automatically fills the instance ID in the search box. This way, you can directly select the instance in the instance list. You can also specify the ID of another instance based on your business requirements. Important You can select only one ECS instance. |
| Basic Migration Parameters | Migration Rate | The migration rate. Unit: Mbit/s. We recommend that you set this parameter to a value greater than 500 Mbit/s. |
|   | Enhanced Hot Migration Compatibility | This mode allows you to migrate ECS instances to an available physical server with a different CPU model. For information about CPU compatibility, see View CPU compatibility configurations. Important If you set Destination Selection Policy to System Recommendation after you enable this feature, the system displays available physical servers of different CPU generations, in addition to the physical servers of the same CPU generation. |

| Destination Selection |   |   |
|---|---|---|
|   | Destination Selection Policy | Random Selection: The system selects a random physical machine in which resources are sufficient. This is the default value. System Recommendation: Select one of the physical servers that have a high migration success rate and are recommended by the system. Important If no data is displayed in the physical machine list, no physical machines are available. We recommend that you select another policy. Specify NC: Specify the physical machine to which you want to migrate the instance. Search for the destination machine based on the cluster, hostname, NC IP address, or NC ID above the NC list, and then select an NC as the destination physical machine. Note The system provides suggestions for each physical machine, but does not select a destination physical machine. You can select a physical machine that is not recommended if necessary for business reasons. Specify Cluster: Specify the cluster to which the instance is migrated. Search for and select the cluster based on the cluster name above the cluster list. Note The system provides suggestions on each cluster but does not select a cluster. You may also select a cluster that is not recommended based on your business requirements. |

| Advanced Migration Parameters Note You can click Configuratio n Description to view the parameter descriptions in this section. You can configure advanced migration parameters based on your business requirements to increase the success rate of instance migration. | Allowed Service Interruption Duration | The service interruption duration in the last phase of hot migration. Unit: milliseconds. Valid values: 200 to 2000. Default value: 300. |
|---|---|---|
|   | Check SLB | Specifies whether to check SLB instance attachment status. Valid values: Yes: checks whether the instance is attached to an SLB instance. If the instance is attached to an SLB instance, the migration task may fail. No: does not check whether the instance is attached to an SLB instance and proceeds with migration. Default value: Yes. |
|   | Check AVS Version | Specifies whether to check the consistency of the application virtual switch (AVS) versions. Valid values: Yes: The system checks whether the AVS versions of the source and destination hosts are the same. If the AVS versions are different, the migration task fails. No: The system does not check the AVS version and proceeds with migration. Default value: Yes. |
|   | Check Virtual NC Version | Specifies whether to check the support status of hot migration in the virtualization version on the destination host. Valid values: Yes: The system checks whether the virtualization version of the destination host supports hot migration. If hot migration is not supported, the migration task fails. No: The system does not check the virtualization version and proceeds with the migration. Default value: Yes. |
|   | Allow Reserved NC | Specifies whether the instance can be migrated to a reserved host. Valid values: Yes: The instance can be migrated to a reserved host. No: The instance cannot be migrated to a reserved host. Default value: No. |

|   | Check CPU Tag | Specifies whether to check that the CPU tag set of the source host is the subset of the CPU tag set of the destination host. Valid values: Yes: The system checks whether the CPU tag set of the source host is a subset of the CPU tag set of the destination host. If the CPU tag set of the source host is not a subset of the CPU tag set of the destination host, the migration task fails. No: The system does not check the CPU tag set and proceeds with the migration. Default value: Yes. |
|---|---|---|
| Operation Information | Reason | The reason for hot migration. |

6. Select **I have read the preceding notes and confirm this operation.** and click
**Submit**.
You can view the status and progress of the migration task in the task list. For more information, see View migration tasks.

##### 2.4.1.5 View the migration history of an instance

In the Compute Operations Console, you can view the migration tasks, including hot migration and cold migration tasks, that are performed on an Elastic Compute Service (ECS) instance.
2. In the top navigation bar, choose **Product Operation > Computing > Compute**
3. In the left-side navigation pane, choose **ECS O&M > ECS Instances**.
4. Find the instance that you want to view and choose **Migrate > View Migration History**
in the **Operation** column.
5. In the **Migration History** panel, view the historical migration tasks that are displayed on
the Cold Migration and Hot Migration tabs. View the following information about a cold migration task: source NC, destination NC, status, start time, end time, and migration reason. View the following information about a hot migration task: source NC, destination NC, status, start time, update time, migration rate, and migration reason.

##### 2.4.1.6 Manage ISOs

You can mount an ISO to or unmount an ISO from an instance. After you mount an ISO to an instance, the instance enters the Rescue mode and you can perform operations on the instance.

**Prerequisites**

The instance on which you want to mount or unmount an ISO is in the **Stopped** state.
2. In the top navigation bar, choose **Product Operation > Computing > Compute**
3. In the left-side navigation pane, choose **ECS O&M > ECS Instances**.
4. On the page that appears, find the instance that you want to manage and move the pointer
over the icon in the **Operation** column and select **Manage ISO**.
5. In the **Manage ISO** dialog box, mount or unmount an ISO based on your business
requirements. To mount an ISO, find the ISO in the **Available ISOs** section and click **Mount** in the
**Operation** column. After the ISO is mounted, it is displayed in the **Mounted ISOs**
section. To unmount an ISO, find the ISO in the **Mounted ISOs** section and click **Unmount** in the
**Operation** column. After the ISO is unmounted, it is displayed in the **Available ISOs**
section.
6. In the dialog box that appears, enter an operator name, a ticket title, and a reason and
click **OK**.

##### 2.4.1.7 Use the rescue mode

This topic describes how to enter the rescue mode to repair an Elastic Compute Service (ECS) instance that cannot be started.

**Prerequisites**

The ID of the source instance (instance that cannot be started) and the ID of a rescue instance are obtained. The rescue instance is the instance that is used to repair the source instance. For more information, see View the details of an instance.

**Background information**

ECS supports the rescue mode. When an instance cannot be started because of incorrect operating system configurations, you can recover the instance by using another instance that runs as expected. To do this, move the system disk of the impaired instance to the rescue instance, modify the operating system configurations on the rescue instance, and then move the system disk back to the impaired instance. Then, the impaired instance can run as expected.
1. Detach the system disk from the source instance.
i. Log on to the AG and run the `go2which` command to query the disk IDs ( `disk_id` ) of the source instance.

```
go2which <instance_id>
```

> **Note:** Replace <instance_id> with the ID of the source instance.

ii. Detach the system disk from the source instance.

```
go2hyapi detach_disk region_id=<region_id> instance_id=<instance_id> disk_id=<disk_ id>
```

> **Note:** Replace <region_id> with the region ID of the source instance, <instance_id> with the ID of the source instance, and <disk_id> with the system disk ID of the source instance.

2. Attach the system disk to the rescue instance.

```
go2hyapi attach_disk region_id=<region_id> instance_id=<instance_id> disk_id=<disk_id
```

`>`

> **Note:** Replace <region_id> with the region ID of the rescue instance, <instance_id> with the ID of the rescue instance, and <disk_id> with the system disk ID of the source instance.

3. Log on to the rescue instance and check whether the system disk of the source instance is
attached. i. Check whether the partitions of the disk are mounted to the rescue instance.

```
fdisk -l
```

The following sample command output indicates that the system disk of the source instance is attached to the rescue instance. ii. Create a folder and mount the partitions of the disk to check whether the rescue instance runs as expected.

```
mkdir /mnt/a mount /dev/vdb1 /mnt/a ls /mnt/a touch /mnt/a/test.log ls /mnt/a
```

The following sample command output indicates that the rescue instance runs as expected.
4. Log on to the AG and run the `go2which detach` command to detach the system disk of the
source instance from the rescue instance.

```
go2hyapi detach_disk region_id=<region_id> instance_id=<instance_id> disk_id=<disk_id
```

`>`

> **Note:** Replace <region_id> with the region ID of the rescue instance, <instance_id> with the ID of the rescue instance, and <disk_id> with the system disk ID of the source instance.

5. Log on to the AG and attach the disk back to the source instance as the system disk.

```
go2hyapi attach_disk region_id=<region_id> instance_id=<instance_id> disk_id=<disk_id
> device=/dev/xvda
```

> **Note:** Replace <region_id> with the region ID of the source instance, <instance_id> with the ID of the source instance, and <disk_id> with the system disk ID of the source instance.

6. Start the source instance.
For more information, see the **Start instances** topic in **ECS User Guide**.

#### 2.4.2 Disks

##### 2.4.2.1 View disks

You can view a list of disks and the details of each disk. The details include the basic information of the disk, and Elastic Compute Service (ECS) instances and computing clusters that are associated with the disk.
2. In the top navigation bar, choose **Product Operation > Computing > Compute**
3. In the left-side navigation pane, choose **ECS O&M > Disk**.
4. In the upper part of the page, specify one or more filter conditions and click **Search** to
search for disks. In the upper-right corner of the page, select a **All in ECS Project** option to narrow down the search results
5. View information about the disks, including disk ID, disk types, disk capacity, associated
ECS instances, and mount points. To view the details of a disk, find the disk and click the disk ID in the **Disk ID/Name** column to go to the **Disk Details** page. For more information, see View disk details. To view the details of the ECS instance to which a disk is attached, find the disk and click the instance ID in the **ECS Instance** column to go to the **Instance Details** page. For more information, see View the details of an instance. To view the details of the computing cluster to which a disk belongs, find the disk and click the cluster name in the **Cluster** column to go to the **Computing Cluster Details** page. For more information, see the **Manage computing clusters** chapter.

> **Note:** The following disk types are supported: system disk and data disk.
> The following disk categories are supported: standard SSD, ultra disk, shared standard SSD, shared ultra disk, standard performance disk, and premium performance disk.

##### 2.4.2.2 View disk details

You can view the details of disks, such as the basic information and the snapshot information.
2. In the top navigation bar, choose **Product Operation > Computing > Compute**
3. In the left-side navigation pane, choose **ECS O&M > Disk**.
4. Find the disk that you want to view and click the ID of the disk in the **Disk ID/Name**
column.
5. View the basic information and snapshot information of the disk.
Basic Information: the disk ID, disk ID in the server controller, disk name, disk type, disk category, disk capacity, and mount point. Snapshot Information: the ID of the automatic snapshot policy.

##### 2.4.2.3 Detach a disk

You can detach disks that are no longer needed. You can detach a disk from one Elastic Compute Service (ECS) instance and then attach the disk to another ECS instance in the same zone. This topic describes how to detach a disk.

**Prerequisites**

Before you detach a disk, make sure that the following conditions are met: The disk is attached to an instance and is in the **In_use** state. To prevent data loss and ensure data integrity, we recommend that you stop read and write operations on the disk before you detach it.
2. In the top navigation bar, choose **Product Operation > Computing > Compute**
3. In the left-side navigation pane, choose **ECS O&M > Disk**.
4. Find the disk that you want to detach and click **Detach** in the **Operation** column.

> **Note:** You can perform **detach** operations only on data disks.

5. In the dialog box that appears, enter a reason and click **OK**.

##### 2.4.2.4 Create a snapshot

You can create snapshots for disks to back up data.

**Prerequisites**

Before you create snapshots for a disk, take note of the following items: The Elastic Compute Service (ECS) instance to which the disk is attached must be in the
**Stopped** or **Running** state. Snapshots cannot be created for disks on the new instances
that are not started at least once. If you create a snapshot for a new system disk or data disk that is created from another snapshot, an error message is returned because the process of loading data to the disk is not complete. The amount of time required to create a snapshot for a newly added data disk varies based on the size of the disk. If the instance to which a disk is attached is not started at least once, snapshots cannot be created for the disk. If the snapshot creation progress does not reach 100%, the snapshot is being created. You cannot create another snapshot when a snapshot is being created for the disk. The snapshot quota is determined by the total number of disks in your account. The maximum number of snapshots that can be created in your account is calculated by using the following formula: Number of disks × 6 + 6. Snapshots can be created for a disk only after the instance to which the disk is attached is started. If you create a snapshot for a disk that is not attached to instances at least once, an error message is returned.

**Background information**

You can use snapshots to back up data, restore ECS instances that are released, and create custom images. Before you roll back disks, modify critical system files, or change the operating system of an instance, you can create snapshots for disks to improve fault tolerance.
2. In the top navigation bar, choose **Product Operation > Computing > Compute**
3. In the left-side navigation pane, choose **ECS O&M > Disk**.
4. Find the disk for which you want to create snapshots and click **Create Snapshot** in the
**Operation** column.
5. In the **Create Snapshot** dialog box, enter a snapshot name, a snapshot description, and
the reason for creating the snapshot. The snapshot name must be 2 to 128 characters in length. The name must start with a letter and cannot start with http:// or https://. The name can contain digits, letters, colons (:), underscores (_), and hyphens (-).

> **Note:** The name cannot start with auto because snapshots whose names start with auto are recognized as automatic snapshots.

6. Click **OK**.

##### 2.4.2.5 View snapshots

You can view the snapshots of disks, manage snapshots, and view automatic snapshot policies.
2. In the top navigation bar, choose **Product Operation > Computing > Compute**
3. In the left-side navigation pane, choose **ECS O&M > Disk**.
4. Find the disk that you want to view and click **View Snapshots** in the **Operation** column.
For more information, see View snapshots.

#### 2.4.3 Images

##### 2.4.3.1 Overview

An ECS image is a template that contains software configurations such as the ECS instance operating system and the programs and servers for applications. You must specify an ECS image to create an instance. The operating system and software provided by the image will be installed on the instance that you create.

##### 2.4.3.2 View images

In the Compute Operations Console, you can view a list of images and the information about each image.
2. In the top navigation bar, choose **Product Operation > Computing > Compute**
3. In the left-side navigation pane, choose **ECS O&M > Image**.
By default, the **Images** tab appears. On the Images tab, you can view the information about each image, including the ID, name, operating system, capacity, status, region, and type of the image.
4. **(Optional)** To view the information about a specific image, enter the ID of the image in the
search box and specify the image type. Then, the image is displayed in the image list.

> **Important:** If you set the **Image Type** parameter to **Custom Image**, you must configure the **Apsara Stack Tenant Account ID** parameter.

##### 2.4.3.3 View ISO details

This topic describes how to check the operating system type of an ISO file and whether the file can be mounted.
2. In the top navigation bar, choose **Product Operation > Computing > Compute**
3. In the left-side navigation pane, choose **ECS O&M > Image**.
By default, the **Images** tab appears. On the Images tab, you can view the information about each image, including the ID, name, operating system, capacity, status, region, and type of the image.
4. Click the **ISO Management** tab.
5. In the upper-left corner of the tab, enter an ISO file name to search for the file.
6. Check the operating system type of the ISO file and whether the file can be mounted.

#### 2.4.4 Snapshots

##### 2.4.4.1 Overview

Snapshots are point-in-time copies of disks. You can use snapshots to back up data or create custom images. When you use disks, you may encounter the following scenarios: You want to use the data of a disk to write or save data to a different disk. Disks provide secure storage for your data. However, data that is stored on a disk may be incorrect due to specific reasons, such as application errors or application vulnerabilities that are exploited. If this occurs, a mechanism is required to help restore your instance to a desired state. Apsara Stack allows you to create snapshots to back up disk data at specific points in time. You can create disk snapshots on a schedule to ensure business continuity.

##### 2.4.4.2 View snapshots

In the Compute Operations Console, you can view the list of snapshots and the details of each snapshot.
2. In the top navigation bar, choose **Product Operation > Computing > Compute**
3. In the left-side navigation pane, choose **ECS O&M > Snapshots**.
By default, the **Snapshots** tab is displayed.
4. In the upper part of the snapshot list, configure the **Apsara Stack Tenant Account ID**,
**Snapshot ID**, **Disk ID**, and **Instance ID** parameters and click **Search**.

> **Note:** The **Apsara Stack Tenant Account ID** parameter is required.

5. In the snapshot list, view the details of the specified snapshot, including the ID and name of
the snapshot, snapshot ID in Server Controller, snapshot type, ID and type of the disk, and creation progress of the snapshot. The snapshot ID in Server Controller is the unique ID generated for the snapshot in Server Controller when the snapshot is created for the first time, which is used only in Server Controller.

##### 2.4.4.3 Delete snapshots

You can delete snapshots that you no longer require in the Compute Operations Console.

**Prerequisites**

Before you delete snapshots that were used to create custom images, you must delete the custom images.
2. In the top navigation bar, choose **Product Operation > Computing > Compute**
3. In the left-side navigation pane, choose **ECS O&M > Snapshots**.
By default, the **Snapshots** tab is displayed.
4. In the upper part of the snapshot list, configure the **Apsara Stack Tenant Account ID**,
**Snapshot ID**, **Disk ID**, and **Instance ID** parameters and click **Search**.

> **Note:** The **Apsara Stack Tenant Account ID** parameter is required.

5. Find the snapshot that you want to delete and click **Delete** in the **Operation** column.
6. In the dialog box that appears, enter a reason for deleting the snapshot and click **OK**.

##### 2.4.4.4 Create an image

In the Compute Operations Console, you can create a custom image from a snapshot. The image contains the operating system and the environment variables of the snapshot.

**Prerequisites**

The progress of the snapshot is 100%. The disk of the snapshot is a system disk.
2. In the top navigation bar, choose **Product Operation > Computing > Compute**
3. In the left-side navigation pane, choose **ECS O&M > Snapshots**.
By default, the **Snapshots** tab is displayed.
4. In the upper part of the snapshot list, configure the **Apsara Stack Tenant Account ID**,
**Snapshot ID**, **Disk ID**, and **Instance ID** parameters and click **Search**.

> **Note:** The **Apsara Stack Tenant Account ID** parameter is required.

5. Find the snapshot from which you want to create an image and click **Create Image**.
6. In the **Create Image** dialog box, configure the parameters.
The following table describes the parameters.

| Parameter | Description |
|---|---|
| Image Name | The name of the image. The name must meet the following requirements: The name must be 2 to 128 characters in length. It must start with a letter and cannot start with http:// or https://. |
| Public Image | If you select Yes, the image you create can be used by other users. Default value: No. |
| Image Description | The description of the image. The description must meet the following requirements: The description can be up to 256 characters in length. By default, this field is empty. You can leave this field empty. It cannot start with http:/ or https://. |
| Reason | The reason for creating the image. You can use this reason when audit logs are generated to facilitate troubleshooting. |

7. After you configure the parameters, click **OK**.

##### 2.4.4.5 View audit logs

This topic describes how to view the audit logs of a snapshot.
2. In the top navigation bar, choose **Product Operation > Computing > Compute**
3. In the left-side navigation pane, choose **ECS O&M > Snapshots**.
By default, the **Snapshots** tab is displayed.
4. In the upper part of the snapshot list, configure the **Apsara Stack Tenant Account ID**,
**Snapshot ID**, **Disk ID**, and **Instance ID** parameters and click **Search**.

> **Note:** The **Apsara Stack Tenant Account ID** parameter is required.

5. Find the snapshot that you want to view and click **Audit Operations** in the **Operation**
column.
6. In the **Audit Operations** panel, view the operations that were performed in the Apsara
Uni-manager Operations Console, POP API calls, and API calls in Server Controller.

##### 2.4.4.6 View automatic snapshot policies

You can apply automatic snapshot policies to system disks and data disks to automatically create snapshots of the disks on a periodical basis. You can view the details of each automatic snapshot policy, including the policy ID, policy name, and number of associated disks.

**Background information**

You can use automatic snapshot policies to mitigate the risks that are associated with the manual creation of snapshots. Examples: When applications, such as personal websites or databases, that are deployed on an Elastic Compute Service (ECS) instance encounter attacks or system vulnerabilities, you may be unable to manually create snapshots. In this case, you can use the most recent automatic snapshots to roll back the affected disks to restore your data and reduce the impacts of data loss. Before regular system maintenance tasks are performed, you can specify an automatic snapshot policy to create snapshots. This eliminates the need to manually create snapshots and ensures that snapshots are always created before maintenance.
2. In the top navigation bar, choose **Product Operation > Computing > Compute**
3. In the left-side navigation pane, choose **ECS O&M > Snapshots**.
By default, the **Snapshots** tab is displayed.
4. In the upper-left corner of the page, click the **Automatic Snapshot Policies** tab.
5. On the **Automatic Snapshot Policies** tab, view the details of each automatic snapshot
policy, including the policy ID, policy name, and number of associated disks.

#### 2.4.5 ENIs

##### 2.4.5.1 View the details of an ENI

In the Compute Operations Console, you can view the list of elastic network interfaces (ENIs) and the details of each ENI.
2. In the top navigation bar, choose **Product Operation > Computing > Compute**
3. In the left-side navigation pane, choose **ECS O&M > ENIs**.
4. In the upper part of the ENI list, configure the **Apsara Stack Tenant Account ID**, **ENI ID**,
**VPC**, **Instance ID**, and **Private IP Address** parameters and click **Search**.

> **Note:** The **Apsara Stack Tenant Account ID** parameter is required.

5. In the ENI list, view the details of the specified ENI and the associated Elastic Compute
Service (ECS) instance. View the details of the specified ENI. In the ENI list, click the ID of the ENI in the **ENI ID** column to go to the ENI Details page. On the **ENI Details** page, view the basic information, business information, VPort information, and security group information of the ENI. View the details of the associated ECS instance. In the ENI list, click the ID of the ECS instance associated with the specified ENI in the
**Instance ID** column to go to the Instance Details page. On the **Instance Details** page,
view the details of the ECS instance. For more information about ECS instances, see View the details of an instance.

##### 2.4.5.2 Unbind an ENI

You can unbind secondary elastic network interfaces (ENIs) from Elastic Compute Service (ECS) instances. You cannot unbind primary ENIs from ECS instances. After a secondary ENI is unbound from an instance, the instance no longer processes traffic on the ENI.

**Prerequisites**

Before you unbind a secondary ENI, make sure that the following requirements are met: The secondary ENI is in the **InUse** state. The instance to which the secondary ENI is bound is in the **Running** or **Stopped** state.
2. In the top navigation bar, choose **Product Operation > Computing > Compute**
3. In the left-side navigation pane, choose **ECS O&M > ENIs**.
4. In the upper part of the ENI list, configure the **Apsara Stack Tenant Account ID**, **ENI ID**,
**VPC**, **Instance ID**, and **Private IP Address** parameters and click **Search**.

> **Note:** The **Apsara Stack Tenant Account ID** parameter is required.

5. Click **Detach** in the **Operation** column corresponding to the ENI that you want to unbind.
6. In the dialog box that appears, enter a reason and click **OK**.

##### 2.4.5.3 Release an ENI

You can release elastic network interfaces (ENIs) that are no longer needed. Secondary ENIs can be released, whereas primary ENIs cannot be released.

**Prerequisites**

The secondary ENI that you want to release is in the **Available** state.
2. In the top navigation bar, choose **Product Operation > Computing > Compute**
3. In the left-side navigation pane, choose **ECS O&M > ENIs**.
4. In the upper part of the ENI list, configure the **Apsara Stack Tenant Account ID**, **ENI ID**,
**VPC**, **Instance ID**, and **Private IP Address** parameters and click **Search**.

> **Note:** The **Apsara Stack Tenant Account ID** parameter is required.

5. Click **Release** in the **Operation** column corresponding to the ENI that you want to release.
6. In the dialog box that appears, enter a reason and click **OK**.

##### 2.4.5.4 View audit logs

You can view the historical operations that were performed in the Apsara Uni-manager Operations Console, historical POP API calls, and historical API calls in Server Controller for elastic network interfaces (ENIs).
2. In the top navigation bar, choose **Product Operation > Computing > Compute**
3. In the left-side navigation pane, choose **ECS O&M > ENIs**.
4. In the upper part of the ENI list, configure the **Apsara Stack Tenant Account ID**, **ENI ID**,
**VPC**, **Instance ID**, and **Private IP Address** parameters and click **Search**.

> **Note:** The **Apsara Stack Tenant Account ID** parameter is required.

5. Find the ENI that you want to view and click **Audit Operations** in the **Operation** column.
6. In the **Audit Operations** panel, view the operations that were performed in the Apsara
Uni-manager Operations Console, POP API calls, and API calls in Server Controller. For more information, see View O&M audit Logs.

#### 2.4.6 Security groups

##### 2.4.6.1 Overview

A security group is a virtual firewall that provides Stateful Packet Inspection (SPI). Security groups provide virtual firewall-like functionality and are used for network access control for one or more ECS instances. They are important means of network security isolation and are used to divide security domains on the cloud. Security group rules can permit the inbound and outbound traffic of the ECS instances associated with the security group. You can authorize or cancel security group rules at any time. Changes to security group rules are automatically applied to ECS instances that are members of the security group. When you configure security group rules, ensure that the rules are concise and easy to manage. If you associate an instance with multiple security groups, hundreds of rules may apply to the instance, which may cause connection errors when you access the instance.

##### 2.4.6.2 View the details of a security group

In the Compute Operations Console, you can view the information about each security group in the security group list, including the region, network type, virtual private cloud (VPC) ID, associated Elastic Compute Service (ECS) instances, and creation time. You can also view the details of a security group on the details page. The details include the basic information, inbound and outbound rules of the security group, and the details of ECS instances that are associated with the security group.
2. In the top navigation bar, choose **Product Operation > Computing > Compute**
3. In the left-side navigation pane, choose **ECS O&M > Security Groups**.
You can view the basic information of each security group in the security group list, including the security group ID and name, region, network type, VPC ID, and creation time. You can also configure the **Security Group ID**, **ECS Instance ID**, or **Apsara Stack**
**Tenant Account ID** parameter and click **Search** to search for specific security groups.
4. In the security group list, find the security group that you want to view and click the ID of
the security group in the **Security Group ID/Name** column to go to the Security Group Details page.
5. On the Security Group Details page, view the details of the security group, including the
basic information, inbound and outbound rules of the security group, and the details of ECS instances that are associated with the security group. View the basic information In the **Basic Information** section, view the basic information of the security group, including the security group ID, VPC, description, creation time, modification time, and the number of associated ECS instances. View security group rules On the **Rules** tab, click the **Inbound** and **Outbound** tabs to view the inbound and outbound rules of the security group. The following table describes the parameters on the two tabs.

| Parameter | Description |
|---|---|
| Direction | Outbound: access from the ECS instances in the current security group to other ECS instances on the internal network or to resources on the Internet. Inbound: access from other ECS instances on the internal network or from resources on the Internet to ECS instances in the security group. |
| Action | Accept: allows access requests on a specific port. Drop: drops access requests on a specific port and drops data packets without returning a response. If an Accept rule and a Drop rule differ only in the action, theD rop rule takes precedence over the Accept rule. |
| NIC Type | The type of the network interface (NIC). Only intranet is supported. Public NICs are not available to ECS instances that are deployed in VPCs. You can add only internal security group rules. However, the added rules control traffic on the Internet and the internal network. |
| Protocol Type | The protocol type of the security group rule. Valid values: All: applies to the full-trust scenarios. TCP: allows or denies traffic on one or more consecutive ports. UDP: allows or denies traffic on one or more consecutive ports. ICMP: uses the ping command to test the network connectivity between instances. ICMPv6: uses the ping6 command to test the network connectivity between instances. GRE: applies to the VPN services. |
| Authorization Object | The authorization objects of the rule, which vary based on the authorization action. |

| Port Range | The port range of the rule, which varies based on the protocol type. If the Protocol Type parameter is set to All, the value -1/-1 is displayed, which indicates all ports. If the Protocol Type parameter is set to TCP, a custom port range in the <Start port>/<End port> format is supported. Valid values of port numbers: 1 to 65535. For example, 80/80 indicates port 80 and 1/22 indicates ports 1 to 22. If the Protocol Type parameter is set to UDP, a custom port range in the <Start port>/<End port> format is supported. Valid values of port numbers: 1 to 65535. For example, 80/80 indicates port 80 and 1/22 indicates ports 1 to 22. If the Protocol Type parameter is set to ICMP, the value -1/-1 is displayed, which indicates all ports. If the Protocol Type parameter is set to ICMPv6, the value -1/-1 is displayed, which indicates all ports. If the Protocol Type parameter is set to GRE, the value -1/-1 is displayed, which indicates all ports. |
|---|---|
| Priority | The priority of the rule. Valid values: 1 to 100. The default value is 1, which indicates the highest priority. |
| Description | The description of the rule. To facilitate rule management, we recommend that you provide an informative description. The description must be 1 to 512 characters in length. |

View the associated ECS instances Click the **Instances** tab to view the ECS instances that are associated with the security group.

##### 2.4.6.3 View audit logs

You can view the historical operations that were performed in the Apsara Uni-manager Operations Console, historical POP API calls, and historical Server Controller API calls for security groups.
2. In the top navigation bar, choose **Product Operation > Computing > Compute**
3. In the left-side navigation pane, choose **ECS O&M > Security Groups**.
You can view the basic information of each security group in the security group list, including the security group ID and name, region, network type, VPC ID, and creation time. You can also configure the **Security Group ID**, **ECS Instance ID**, or **Apsara Stack**
**Tenant Account ID** parameter and click **Search** to search for specific security groups.
4. Find the security group that you want to view and click **Audit Operations** in the
**Operation** column.
5. In the **Audit Operations** panel, view the operation records on the Operations in the Apsara
Uni-manager Operations Console, POP API Calls, and Server Controller API Calls tabs. For more information, see Audit logs.

#### 2.4.7 Custom instance types

##### 2.4.7.1 Add a custom instance type

When existing instance types cannot meet your business requirements, you can add custom instance types in the Compute Operations Console and create instances of the custom instance types.

**Background information**

Each custom instance type is named in the following format: `<Instance family>.c<Number of` `CPU cores)m<Memory size>.customize.XXX` . `XXX` specifies the user-defined name of the custom instance type. The final name of a custom instance type is automatically generated based on the parameters that you configure when you add the custom instance type. The parameters include Instance Type Name, CPU Cores (vCPUs), Memory (GB), Max Network Bandwidth (Gbit/s), Packet Forwarding Rate (10,000 PPS), and eniQueueNum.

> **Note:** If you select an instance family equipped with local SSDs from the Instance Family drop- down list when you add a custom instance type, the Local Disks parameter is displayed.

**Instructions**

The instance families to which you can add custom instance types are displayed in the Apsara Uni-manager Operations Console based on your actual environment. Select instance families from the Instance Family drop-down list based on your business requirements to add custom instance types. For information about instance families, see Introduction to Instance Families and Instance Types in the Apsara Stack ECS documentation.

> **Important:** You can continue to use the custom instance types that are already added to the ecs.anyshare instance family.

2. In the top navigation bar, choose **Product Operation > Computing > Compute**
3. In the left-side navigation pane, choose **ECS O&M > Specifications**.
4. Click the **Custom Instance Type** tab and then click **Create Instance Type**.
5. Configure parameters and click **Create**.

> **Note:** After a custom instance type is added, wait for the instance type to take effect.

The following table describes the parameters.

| Parameter | Description |
|---|---|

|   | Instance Family |   |   | Required. Select an instance family from the Instance Family drop-down list. Note The instance families to which you can add custom instance types are displayed in the drop-down list. |   |   |   |   |   |
|---|---|---|---|---|---|---|---|---|---|
|   |   |   |   | Specify a name for the custom instance type. The final name of the custom instance type is in the following format: <Instance |   |   |   |   |   |
|   |   |   |   |   |   |   | <Instance |   |   |
|   |   |   |   | family>.c<Number of CPU cores)m<Memory |   |   |   |   |   |
|   |   |   |   | size>.customize.XXX |   |   |   |   |   |
|   |   |   |   |   | Important The name of a custom instance type equipped with local SSDs is in the following format: <Instance |   |   |   |   |
|   |   |   |   |   |   | <Instance |   |   |   |
|   |   |   |   |   | family>.c<Number of CPU cores)m<Memory |   |   |   |   |
|   |   |   |   |   | size>d<Number of local SSDs>.customize.XXX |   |   |   |   |
|   |   |   |   |   | family>.c<Number of CPU cores)m<Memory |   |   |   |   |
|   | Instance Type Name |   |   |   |   |   |   |   |   |
|   |   |   |   |   | size>d<Number of local HDDs>.customize.XXX |   |   |   |   |
|   | CPU Cores (vCPUs) |   |   | Required. Specify the number of vCPUs. Enter 1 or an even number greater than 1. Important Do not enter a value that exceeds the maximum number of CPU cores per physical machine. Otherwise, the custom instance type cannot be added. |   |   |   |   |   |

| Memory (GB) | Required. Specify a memory size. Enter 1 or an even number greater than 1. Important Do not enter a value that exceeds the maximum amount of memory per physical machine. Otherwise, the custom instance type cannot be added. |
|---|---|
| Max Disks | The value is automatically calculated. |
| Max ENIs | The value is automatically calculated. |
| Max Network Bandwidth (Gbit/s) | The value is automatically calculated. You can change the value based on your business requirements. |
| Packet Forwarding Rate (10,000 PPS) | The value is automatically calculated. You can change the value based on your business requirements. |
| Reason | Required. Enter a reason. |

**Result**

The new custom instance type is displayed on the Custom Instance Type tab. After you add custom instance types, you can create instances of the instance types. For more information, see **Instances > Create an instance** in the ECS User Guide in the Apsara Stack Documentation Center.

##### 2.4.7.2 View a custom instance type

In the Compute Operations Console, you can view the details of a custom instance type that you added.
2. In the top navigation bar, choose **Product Operation > Computing > Compute**
3. In the left-side navigation pane, choose **ECS O&M > Specifications**.
4. On the **All Specifications** or **Custom Instance Type** tab, enter the name of a custom
instance type in the search box to search for the instance type.
5. View the details of the custom instance type. The details include the instance family,
instance type name, number of vCPUs, memory size in GB, network baseline bandwidth, packet forwarding rate, and maximum number of elastic network interfaces (ENIs) per instance.

##### 2.4.7.3 Disable custom instance types

In the Compute Operations Console, you can disable the custom instance types that you no longer require. After you disable a custom instance type, you can no longer select the custom instance type when you create instances.
2. In the top navigation bar, choose **Product Operation > Computing > Compute**
3. In the left-side navigation pane, choose **ECS O&M > Specifications**.
4. On the **All Specifications** or **Custom Instance Type** tab, find the custom instance type
that you want to disable and click **Disable** in the **Operation** column.
5. In the dialog box that appears, specify a reason and click **OK**.

> **Note:** If a custom instance type was used to create instances, you cannot disable the instance type.
> To re-enable a custom instance type that you disabled, find the instance type and click **Enable** in the **Operation** column.
> After you disable or enable a custom instance type, you must wait for the disable or enable operation to take effect.
> After you disable or enable a custom instance type, you must wait for the disable or enable operation to take effect. Do not perform operations on the instance type until the status of the instance type changes to **Disabled** or **Enabled**.

##### 2.4.7.4 View audit logs

You can view the historical operations that are performed in the Apsara Uni-manager Operations Console and the historical POP API calls that are made for a custom instance type.
2. In the top navigation bar, choose **Product Operation > Computing > Compute**
3. In the left-side navigation pane, choose **ECS O&M > Specifications**.
4. On the **All Specifications** or **Custom Instance Type** tab, find the custom instance type
that you want to manage and click **Operation Records** in the **Operation** column.
5. In the **Operation Records** panel, view the historical operations that are performed in the
Apsara Uni-manager Operations Console and the historical POP API calls that are made for the custom instance type.

#### 2.4.8 View O&M audit Logs

The Compute Operations Console provides traceability of resource operations. In the Compute Operations Console, you can view the historical operations performed on resources, historical POP API calls, and historical Server Controller API calls and identify high-risk operations.
2. In the top navigation bar, choose **Product Operation > Computing > Compute**
3. In the left-side navigation pane, click **O&M Audit Logs**.
By default, the **Operations in the Apsara Uni-manager Operations Console** tab is displayed on the O&M Audit Logs page.
4. View the information displayed on each tab. The following table describes the information
that you can view on each tab.

| Tab | Description |
|---|---|
| Operations in the Apsara Uni-manager Operations Console | In the upper part of the tab, specify a resource, an operation, a request ID, or an operator for the Resource parameter, specify a time range for the Time Range parameter, and then click Search. In the operation list, view the following information about the operation records: operation, operation time, operation result, error information, request ID, request parameters, operator, and description. |
| POP API Calls | In the upper part of the tab, specify an operation, a request ID, or a caller for the Keyword parameter, specify a time range for the Time Range parameter, and then click Search. In the API call list, view the following information about the calls: operation, operation time, request ID, HTTP status code, error information, service, request parameters, and caller. |
| Server Controller API Calls | In the upper part of the tab, specify an operation, a request ID, or a request IP address for the Keyword parameter, specify a time range for the Time Range parameter, and then click Search. In the API call list, view the following information about the calls: operation, request ID, request time, response code, request IP address, request duration, and request parameters. |

### 2.5 Control and monitoring

You can view control and monitoring information of servers in the Compute Operations Console, including the details of RDS instances, execution status of scheduled tasks, abnormal workflows, and workflows.
2. In the top navigation bar, choose **Product Operation > Computing > Compute**
3. In the left-side navigation pane, click **Control and Monitoring**.
4. View control and monitoring information.
In the **RDS Instances** section, view the list of RDS instances. The list includes the following columns: Database Instance, CPU Utilization, Connections, and Disk Usage. The Connections column indicates the percentage of existing connections in the maximum number of connections for each RDS instance. Click an instance name in the **Database**
**Instance** column. You are redirected to **ApsaraDB Operations and Maintenance**
**System**. For more information, see the View instances topic in ApsaraDB RDS Operations
and Maintenance Guide. In the **Scheduled Tasks** section, view the execution status of scheduled tasks. View the details of a scheduled task, including the task status, time when the task was last triggered, and task description. On the **Abnormal Workflows** tab, view the list of abnormal workflows and the details of an abnormal workflow. View the list of abnormal workflows. The list includes the following columns: Workflow ID, Workflow Name, RequestId, Apsara Stack Tenant Account ID, InstanceId, Start Time, End Time, and Execution Node. View the details of an abnormal workflow. a. Click a workflow ID in the **Workflow ID** column, or click **View Details** in the
**Operation** column.
b. In the **Activity Details** panel, view the ID, name, status, start time, and end time of each activity. c. In the **Operation** column corresponding to an activity, click **Add Input**. In the
**Workflow Input** dialog box, view the input information.
d. In the **Operation** column corresponding to an activity, click **Add Output**. In the
**Workflow Output** dialog box, view the output information.
e. In the **Operation** column corresponding to an activity, click **Add Error**. In the
**Workflow Error** dialog box, view the error message.
On the **Workflows** tab, view the details of each workflow, including the workflow name, request ID, Apsara Stack tenant account ID, workflow status, time when the workflow was created, time when the workflow was updated, and node on which the workflow is executed.

### 2.6 Analyze the computing capacity

**capacity**

This topic describes how to check the inventory usage of Elastic Compute Service (ECS) instance types in the Compute Operations Console. This helps you learn about the usage trends of ECS instance types.
2. In the top navigation bar, choose **Product Operation > Computing > Compute**
3. In the left-side navigation pane, click **Compute Capacity Analytics**.
4. View the analysis of computing capacity.
In the **Allocated Capacity Ratio** section, view the total number of resources, number of used resources, and inventory usage by resource type. The resources include vCPU cores, memory, GPUs, and local disks. In the **vCPU/Memory Usage Trend** section, specify a time range to view the usage trends of vCPU cores and memory.

> **Note:** Move the pointer over a data point on a line chart to view the detailed resource usage on the corresponding day.

In the **Inventory** section, select a zone from the drop-down list and enter an instance type to view the inventory information.

### 2.7 Migration task management

#### 2.7.1 Manage migration tasks

##### 2.7.1.1 Migrate an ECS instance

If an Elastic Compute Service (ECS) instance or node controller (NC) that hosts an ECS instance fails, you can migrate the instance from one NC to another NC to ensure system stability. This topic describes how to create a migration task for a single ECS instance.

> **Note:** Find the ECS instance that you want to migrate on the **ECS Instances** page and create a migration task for the instance. For more information, see Migrate an instance.

2. In the top navigation bar, choose **Product Operation > Computing > Compute**
3. In the left-side navigation pane, click **Migration Tasks**.
The **ECS Migration Tasks** tab under the **Tasks** tab appears.
4. Click **Create ECS Migration Task**.
5. In the **Create ECS Migration Task** dialog box, configure the parameters.
**Cold Migration**: Only instances in the **Pending** or **Stopped** (Shutted) state can be
migrated.

| Parameter or section | Parameter | Description |
|---|---|---|
| Instance Information | Select Instance | Select the instance that you want to migrate. Enter the ID of the instance to be migrated in the search box above the instance list, and then select the instance. Important You can select only one ECS instance. |

| Destination Selection | Destination Selection Policy | Random Selection: The system selects a random physical machine in which resources are sufficient. This is the default value. System Recommendation: Select one of the physical servers that have a high migration success rate and are recommended by the system. Important If no data is displayed in the physical machine list, no physical machines are available. We recommend that you select another policy. Specify NC: Specify the physical machine to which you want to migrate the instance. Search for the destination machine based on the cluster, hostname, NC IP address, or NC ID above the NC list, and then select an NC as the destination physical machine. Note The system provides suggestions for each physical machine, but does not select a destination physical machine. You can select a physical machine that is not recommended if necessary for business reasons. Specify Cluster: Specify the cluster to which the instance is migrated. Search for and select the cluster based on the cluster name above the cluster list. Note The system provides suggestions on each cluster but does not select a cluster. You may also select a cluster that is not recommended based on your business requirements. |
|---|---|---|
|   | Recovery Mode | The state that you want the instance to restore after migration. Start after Migration Stop After Migration |
| Operation Information | Reason | The reason for cold migration. |

**Hot Migration**: migrates instances that are in the **Running** state.

| Parameter or section | Parameter | Description |
|---|---|---|
| Instance Information | Select Instance | Select the instance that you want to migrate. Enter the ID of the instance to be migrated in the search box above the instance list, and then select the instance in the instance list. Important You can select only one ECS instance. |
| Basic Migration Parameters | Migration Rate | The migration rate. Unit: Mbit/s. We recommend that you set this parameter to a value greater than 500 Mbit/s. |
|   | Enhanced Hot Migration Compatibility | This mode allows you to migrate ECS instances to an available physical server with a different CPU model. For information about CPU compatibility, see View CPU compatibility configurations. Important If you set Destination Selection Policy to System Recommendation after you enable this feature, the system displays available physical servers of different CPU generations, in addition to the physical servers of the same CPU generation. |

| Destination Selection |   |   |
|---|---|---|
|   | Destination Selection Policy | Random Selection: The instance is migrated to a random physical machine in which resources are sufficient. System Recommendation: The system filters and selects the physical servers that have a high migration success rate. Note If no data is displayed in the host list, no physical servers are available. We recommend that you select another policy. Specify NC: If you specify the machine to which the instance is migrated, the migration may fail. Search for the destination machine based on the cluster, hostname, NC IP address, or NC ID above the NC list, and then select an NC as the destination physical machine. Note The system provides suggestions on whether each physical machine is suitable for reference, but these suggestions are for reference only and do not limit your selection of the destination physical machine. You can select an NC that is not recommended if necessary for business reasons. Specify Cluster: Specify the cluster to which the instance is migrated. Search for and select the cluster based on the cluster name above the cluster list. Note The system provides suggestions for each cluster but does not select a cluster. You can select a cluster that is not recommended if necessary for business reasons. |

| Advanced Migration Parameters Note You can click Configura tion Descripti on to view the parameter description s in this section. You can configure advanced migration parameter s based on your business requireme nts to increase the success rate of instance migration. | Allowed Service Interruption Duration | The service interruption duration in the last phase of hot migration. Unit: milliseconds. Valid values: 200 to 2000. Default value: 300. |
|---|---|---|
|   | Check SLB | Specifies whether to check SLB instance attachment status. Valid values: Yes: checks whether the instance is attached to an SLB instance. If the instance is attached to an SLB instance, the migration task may fail. No: does not check whether the instance is attached to an SLB instance and proceeds with migration. Default value: Yes. |
|   | Check AVS Version | Specifies whether to check the consistency of the application virtual switch (AVS) versions. Valid values: Yes: The system checks whether the AVS versions of the source and destination hosts are the same. If the AVS versions are different, the migration task fails. No: The system does not check the AVS version and proceeds with migration. Default value: Yes. |
|   | Check Virtual NC Version | Specifies whether to check the support status of hot migration in the virtualization version on the destination host. Valid values: Yes: The system checks whether the virtualization version of the destination host supports hot migration. If hot migration is not supported, the migration task fails. No: The system does not check the virtualization version and proceeds with the migration. Default value: Yes. |
|   | Allow Reserved NC | Specifies whether the instance can be migrated to a reserved host. Valid values: Yes: The instance can be migrated to a reserved host. No: The instance cannot be migrated to a reserved host. Default value: No. |

|   | Check CPU Tag | Specifies whether to check that the CPU tag set of the source host is the subset of the CPU tag set of the destination host. Valid values: Yes: The system checks whether the CPU tag set of the source host is a subset of the CPU tag set of the destination host. If the CPU tag set of the source host is not a subset of the CPU tag set of the destination host, the migration task fails. No: The system does not check the CPU tag set and proceeds with the migration. Default value: Yes. |
|---|---|---|
| Operation Information | Reason | The reason for hot migration. |

6. Select **I have read the preceding notes and confirm this operation.** and click
**Submit**.
You can view the status and progress of the migration task in the task list. For more information, see View migration tasks.

##### 2.7.1.2 Create a computing server-level migration task

**task**

This topic describes how to migrate all Elastic Compute Service (ECS) instances on a computing server to other computing servers.

**Prerequisites**

The computing server is in the `free` or `mlock` state.

**Scenarios**

When you scale down or maintain a computing server, you must migrate all ECS instances on the server before you can perform operations on the server. In this case, you can create a computing server-level migration task to migrate all ECS instances on the server to other computing servers.

**Usage notes**

When you migrate all instances from a computing server, take note of the following items: After you submit a migration task, the server enters the mlock state. If the migration task is complete, fails, or is canceled, you must submit an application to unlock the server. ECS instances on the server are migrated to other computing servers based on the ECS scheduling rules. The migration task may not be successful in a single attempt due to various reasons. If an ECS instance in the **Stopped** or **Pending** state is migrated, the status of the ECS instance remains unchanged. After the migration task is complete, you must check for any remaining ECS instances on the original server to ensure that all ECS instances are migrated.

> **Note:** You can also find the server whose instances you want to migrate on the **Computing** **Server O&M** page and create a computing server-level migration task for the server. For more information, see Migrate all instances from a computing server.

2. In the top navigation bar, choose **Product Operation > Computing > Compute**
3. In the left-side navigation pane, click **Migration Tasks**.
By default, the **ECS Migration Tasks** tab under the **Tasks** tab appears.
4. On the **Machine Migration Tasks** tab, click **Create Machine Migration Task**.
5. On the **Create Machine Migration Task** page, configure the parameters described in the
following table.

| Section | Parameter | Description |
|---|---|---|
| Source NC | Select Machine | The server from which you want to migrate all ECS instances. To specify the source server, search for the server based on the hostname or IP address in the search box and then select the server from the server list. Important You can select only one server. |
|   | Enhanced Hot Migration Compatibility | Specifies whether to enable the enhanced hot migration compatibility mode. This mode allows you to migrate ECS instances to an available physical server with a different CPU model. For information about CPU compatibility, see View CPU compatibility configurations. |

|   | Destination Selection Policy | Random Selection (default): migrates ECS instances to a random physical server whose resources are sufficient. Specify NC: migrates ECS instances to the specified server. In this case, the migration may fail. To specify the destination server, search for the server based on the cluster, hostname, IP address, or server ID in the search box and then select the server from the server list. Note The system provides suggestions on each physical server only for reference. You can select a physical server that is not recommended if it is necessary for your business. Specify Cluster: migrates ECS instances to the specified cluster. In this case, the migration may fail. To specify the destination cluster, search for the cluster by name in the search box and select it from the cluster list. Note The system provides suggestions on each cluster only for reference. You can select a cluster that is not recommended if it is necessary for your business. |
|---|---|---|
| Migration Destination Configurations |   |   |

| Advanced Migration Parameters Note You can configure advanced migration parameters based on your business requiremen ts to increase the success rate of instance migration. You can click Configurat ion Descriptio n to view the parameter descriptions in this section. | Allowed Service Interruption Duration | The service interruption duration in the last phase of hot migration. Unit: milliseconds. Valid values: 200 to 2000. Default value: 300. |
|---|---|---|
|   | Check SLB | Valid values: Yes: checks whether the instances to be migrated are attached to Server Load Balancer (SLB) instances. If an instance is attached to an SLB instance, the migration task may fail. No: does not check whether the instances are attached to SLB instances and proceeds with migration. Default value: Yes. |
|   | Check AVS Version | Valid values: Yes: checks whether the AVS versions of the source and destination hosts are the same. If the AVS versions are different, the migration task fails. No: does not check the AVS versions and proceeds with migration. Default value: Yes. |
|   | Check Virtual NC Version | Valid values: Yes: checks whether the virtualization version of the destination host supports hot migration. If hot migration is not supported, the migration task fails. No: does not check the virtualization version and proceeds with the migration. Default value: Yes. |
|   | Allow Reserved NC | Valid values: Yes: allows the instances to be migrated to a reserved host. No: does not allow the instances to be migrated to a reserved host. Default value: No. |

|   | Check CPU Tag | Valid values: Yes: checks whether the CPU tag set of the source host is a subset of the CPU tag set of the destination host. If the CPU tag set of the source host is not a subset of the CPU tag set of the destination host, the migration task fails. No: does not check the CPU tag sets and proceeds with the migration. Default value: Yes. |
|---|---|---|
| Operation Information | Reason | The reason for computing server-level migration. |

6. Select **I have read the preceding notes and confirm this operation** and click **Submit**.
You can view the status and progress of the migration task in the task list. For more information, see View migration tasks. You can stop the migration task if it is no longer needed. For more information, see Stop a migration task.

##### 2.7.1.3 Create a batch migration task

If an Elastic Compute Service (ECS) instance or a physical server that hosts an ECS instance fails, you can migrate the instance from one server to another server to ensure system stability. You can also migrate multiple ECS instances from a server at the same time. This topic describes how to migrate multiple ECS instances at a time.

**Usage notes**

A batch migration task migrates multiple ECS instances to the destination server based on the configurations of the migration destination. However, the migration is affected by multiple factors and may fail. Only ECS instances of the same instance family can be migrated at a time. Only ECS instances in the **Running**, **Stopped**, or **Pending** state can be migrated at a time. If an ECS instance in the **Stopped** or **Pending** state is migrated, the status of the ECS instance remains unchanged.
2. In the top navigation bar, choose **Product Operation > Computing > Compute**
3. In the left-side navigation pane, click **Migration Tasks**.
By default, the **ECS Migration Tasks** tab under the **Tasks** tab appears.
4. On the **Batch Migration Tasks** tab, click **Create Batch Migration Task**.
5. On the **Create Batch Migration Task** page, configure the parameters described in the
following table.

| Section |   | Parameter | Description |   |   |
|---|---|---|---|---|---|
| Instance Information |   | Select Instance | The ECS instances to be migrated. You can enter the IDs of instances to be migrated in the search box to search for the instances. Separate multiple instance IDs with commas (,). Example: i-ez*****deuz,i-ez*****g4b4,i- ez*****02zd . |   |   |
|   |   |   |   | i-ez*****deuz,i-ez*****g4b4,i- |   |
|   |   |   | ez*****02zd |   |   |
| Migration Destination Configurations |   | Enhanced Hot Migration Compatibility | Specifies whether to enable the enhanced hot migration compatibility mode. This mode allows you to migrate ECS instances to an available physical server with a different CPU model. For information about CPU compatibility, see View CPU compatibility configurations. |   |   |
|   |   | Destination Selection Policy | Random Selection (default): migrates ECS instances to a random physical server whose resources are sufficient. Specify NC: migrates ECS instances to the specified server. In this case, the migration may fail. To specify the destination server, search for the server based on the cluster, hostname, IP address, or server ID in the search box and then select the server from the server list. Note The system provides suggestions on each physical server only for reference. You can select a physical server that is not recommended if it is necessary for your business. Specify Cluster: migrates ECS instances to the specified cluster. In this case, the migration may fail. To specify the destination cluster, search for the cluster by name in the search box and select it from the cluster list. Note The system provides suggestions on each cluster only for reference. You can select a cluster that is not recommended if it is necessary for your business. |   |   |

| Advanced Migration Parameters Note You can configure advanced migration parameters based on your business requiremen ts to increase the success rate of instance migration. You can click Configurat ion Descriptio n to view the parameter description s in this section. | Allowed Service Interruption Duration | The service interruption duration in the last phase of hot migration. Unit: milliseconds. Valid values: 200 to 2000. Default value: 300. |
|---|---|---|
|   | Check SLB | Valid values: Yes: checks whether the instances to be migrated are attached to Server Load Balancer (SLB) instances. If an instance is attached to an SLB instance, the migration task may fail. No: does not check whether the instances are attached to SLB instances and proceeds with migration. Default value: Yes. |
|   | Check AVS Version | Valid values: Yes: checks whether the AVS versions of the source and destination hosts are the same. If the AVS versions are different, the migration task fails. No: does not check the AVS versions and proceeds with migration. Default value: Yes. |
|   | Check Virtual NC Version | Valid values: Yes: checks whether the virtualization version of the destination host supports hot migration. If hot migration is not supported, the migration task fails. No: does not check the virtualization version and proceeds with the migration. Default value: Yes. |
|   | Allow Reserved NC | Valid values: Yes: allows the instances to be migrated to a reserved host. No: does not allow the instances to be migrated to a reserved host. Default value: No. |

|   | Check CPU Tag | Valid values: Yes: checks whether the CPU tag set of the source host is a subset of the CPU tag set of the destination host. If the CPU tag set of the source host is not a subset of the CPU tag set of the destination host, the migration task fails. No: does not check the CPU tag sets and proceeds with the migration. Default value: Yes. |
|---|---|---|
| Operation Information | Reason | The reason for migrating multiple ECS instances at a time. |

6. Select **I have read the preceding notes and confirm this operation** and click **Submit**.
You can view the status and progress of the migration task in the task list. For more information, see View migration tasks. You can stop the migration task if it is no longer needed. For more information, see Stop a migration task.

##### 2.7.1.4 View migration tasks

After you create a migration task, you can view information about the migration task in the migration task list, such as the task ID, instance information, machine information, task status, task success rate, task execution result, migration reason, and operator.

**Background information**

You can view information about Elastic Compute Service (ECS) migration tasks, machine migration tasks (also known as computing server-level migration tasks), and batch migration tasks. A machine or batch migration task consists of multiple subtasks. Each subtask is an ECS migration task that migrates an ECS instance. The subtasks are displayed together with the ECS migration tasks that you separately created in the ECS migration task list. You can create migration tasks of different types based on your business requirements. To migrate an ECS instance, create an ECS migration task. For more information, see Create an ECS migration task. To migrate all ECS instances that reside on one physical machine, create a machine migration task. For more information, see Create a machine migration task. To migrate multiple ECS instances at a time, create a batch migration task. For more information, see Create a batch migration task.
2. In the top navigation bar, choose **Product Operation > Computing > Compute**
3. In the left-side navigation pane, click **Migration Tasks**.
The **ECS Migration Tasks** tab under the **Tasks** tab appears.
4. View ECS migration tasks.
On the **ECS Migration Tasks** tab, you can view all ECS migration tasks, including the subtasks of machine and batch migration tasks. You can search for ECS migration tasks by task ID, instance ID, task type (**Hot Migration** or **Cold Migration**), or task status (such as
**Successful** or **Migrating**).

| Parameter | Description |
|---|---|
| Task ID | The ID of the migration task. |
| Instance ID | The ID of the migrated ECS instance. |
| Source NC ID and IP Address | The ID and IP address of the source physical machine from which the ECS instance is migrated. |
| Destination NC ID and IP Address | The ID and IP address of the destination physical machine to which the ECS instance is migrated. |
| Task Status | The status of the migration task. Valid values: pre check failed _ _ canceled init waiting migrating success failed |
| Task Type | The type of the migration task. Valid values: Hot Migration Cold Migration |
| Retries | The actual number and maximum number of times that the migration task is retried after a failure. A migration task can be retried up to five times. After five retries fail, the value in the Task Status column of the migration task changes to failed. |
| Migration Request Result | The result returned by Server Controller after a migration request is initiated. The result does not represent the final result of the migration task. |
| Created At | The time when the migration task is created. |

| Started At | The time when the migration task starts. |   |   |
|---|---|---|---|
| Updated At | The time when the migration task is updated. |   |   |
| Migration Reason | The reason why the migration task is created. |   |   |
| Operator | The account used to create the migration task. |   |   |
| Migration Task Result | The execution result of the migration task. A value of migration succeeded! indicates that the migration task is successfully executed. |   |   |
|   |   | migration |   |

| k Result | succeeded! |
|---|---|

5. View machine migration tasks.
Click the **Machine Migration Tasks** tab under the Tasks tab. You can view information about machine migration tasks in the migration task list. You can search for machine migration tasks by task ID or source physical machine ID.

> **Note:** You can also click **Computing Server O&M** in the left-side navigation pane and then click the **Server-level Migration Tasks** tab on the Computing Server O&M page to view information about existing machine migration tasks. For more information, see View computing server-level migration tasks.

| Parameter | Description |
|---|---|
| Task ID | The ID of the migration task. |
| Source NC ID and IP Address | The ID and IP address of the source physical machine from which ECS instances are migrated. |
| Instances | The number of migrated ECS instances. |
| Task Status | The status of the migration task. Valid values: init running success failed create failed create ecs migrate task canceled |

| Task Success Rate | The success rate of the migration task, which is calculated by using the following formula: Success rate of a migration task = (Number of successful subtasks/Total number of subtasks) × 100%. |
|---|---|
| Destination Selection Policy | The policy for selecting a destination. The policy that you specified when you created the migration task is displayed. For information about how to select a destination selection policy for a machine migration task, see Create a machine migration task. |
| Destination Information | The destination physical machine or cluster to which the ECS instances are migrated. |
| Task Result | The execution result of the migration task. A value of all ecs migrate tasks belong to this task success! indicates that the machine migration task is successfully executed. |
| Created At | The time when the migration task is created. |
| Updated At | The time when the migration task is updated. |
| Migration Reason | The reason why the migration task is created. |
| Operator | The account used to create the migration task. |
| Operation | Click Details to view information about the machine migration task in the task details panel. The task details panel consists of the following sections: Basic Information: This section displays the basic information about the machine migration task, such as the task ID, number of ECS instances, and task status. Migrate Instance: This section displays a list of ECS instances involved in the machine migration task. For information about the parameters in the instance list, see the View ECS migration tasks step of this topic. Note Each row in the instance list displays information about a subtask of the machine migration task that migrates an ECS instance. The information about the subtasks is also displayed on the ECS Migration Tasks tab. You can search for the subtasks by ECS instance ID. Click Terminate Task to cancel the machine migration task. For information about the considerations and limits that apply when you terminate a migration task, see Terminate a migration task. |

|   | migrate tasks belong to this task success! |
|---|---|

6. View batch migration tasks.
Click the **Batch Migration Tasks** tab under the Tasks tab. You can view information about batch migration tasks in the migration task list. You can search for batch migration tasks by task ID.

|   | Parameter | Description |
|---|---|---|
|   | Task ID | The ID of the migration task. |
|   | ECS Instances | The IDs of the migrated ECS instances. The IDs are separated by commas (,). Example: i-ez*****deuz,i-ez*****g4b4,i- ez*****02zd . |
|   |   | ez*****02zd |
|   | Instances | The number of migrated ECS instances. |
|   | Task Status | The status of the migration task. Valid values: init running success failed create failed create ecs migrate task canceled |
|   | Task Success Rate | The success rate of the migration task, which is calculated by using the following formula: Success rate of a migration task = (Number of successful subtasks/Total number of subtasks) × 100%. |
|   | Destination Selection Policy | The policy for selecting a destination. The policy that you specified when you created the migration task is displayed. For information about how to select a destination selection policy for a batch migration task, see Create a batch migration task. |
|   | Destination Information | The destination physical machine or cluster to which the ECS instances are migrated. |
|   | Task Result | The execution result of the migration task. A value of all ecs migrate tasks belong to this task success! indicates that the batch migration task is successfully executed. |
|   | Migration Reason | The reason why the migration task is created. |
|   | Created At | The time when the migration task is created. |

| i-ez*****deuz,i-ez*****g4b4,i- |   |
|---|---|

|   | migrate tasks belong to this task success! |
|---|---|

| Updated At | The time when the migration task is updated. |
|---|---|
| Operator | The account used to create the migration task. |
| Operation | Click Details to view information about the batch migration task in the task details panel. The task details panel consists of the following sections: Basic Information: This section displays the basic information about the batch migration task, including the task ID, number of ECS instances, and task status. Migrate Instance: This section displays a list of ECS instances involved in the batch migration task. For information about the parameters in the instance list, see the View ECS migration tasks step of this topic. Note Each row in the instance list displays information about a subtask of the batch migration task that migrates an ECS instance. The information about the subtasks is also displayed on the ECS Migration Tasks tab. You can search for the subtasks by ECS instance ID. Click Terminate Task to cancel the batch migration task. For information about the considerations and limits that apply when you terminate a migration task, see Terminate a migration task. |

##### 2.7.1.5 Stop a migration task

A computing server-level migration task or batch migration task contains multiple subtasks. In each subtask, a single Elastic Compute Service (ECS) instance is migrated. You can stop a migration task based on your business requirements.

**Usage notes**

Before you stop a migration task, take note of the following items: You can stop only computing server-level migration tasks and batch migration tasks. For a stopped migration task: The **status** of the migration task changes to **canceled**. Subtasks in the **init** state are stopped.

> **Important:** Subtasks in the **pending** or **migrating** state are not affected.

2. In the top navigation bar, choose **Product Operation > Computing > Compute**
3. Stop the migration task based on its type.
**Computing server-level migration task**:
Method 1: Stop the migration task on the **Computing Server O&M** page a. In the left-side navigation pane, click **Computing Server O&M**. By default, the **Machines** tab of the Computing Server O&M page appears. On this tab, you can view the details of all computing servers. b. On the **Server-level Migration Tasks** tab, find the migration task that you want to stop and click **Terminate Task** in the **Operation** column.

> **Note:** You can also click the hostname of the corresponding server on the **Machines** tab to go to the server details page. On the **Compute Server Details** page, find the migration task on the **Machine Migration Task** tab and click **Terminate** **Task** in the **Operation** column.

Method 2: Stop the migration task on the **Migration Task Management** page a. In the left-side navigation pane, click **Migration Tasks**. By default, the **ECS Migration Tasks** tab under the **Tasks** tab appears. b. Click the **Machine Migration Tasks** tab. c. On the Machine Migration Tasks tab, find the migration task that you want to stop and click **Terminate Task** in the **Operation** column.
**Batch migration task**:
a. In the left-side navigation pane, click **Migration Tasks**. By default, the **ECS Migration Tasks** tab under the **Tasks** tab appears. b. Click the **Batch Migration Tasks** tab. c. On the Batch Migration Tasks tab, find the migration task that you want to stop and click **Terminate Task** in the **Operation** column.
4. In the message that appears, click **OK**.
You can click **Details** in the **Operation** column to view the status of subtasks in the migration task. The stopped subtasks are in the **canceled** state. After the computing server-level migration task or batch migration task is stopped, its status also changes to
**canceled**.
To view the details of a subtask, search for the subtask by using the ID of the corresponding ECS instance on the **ECS Migration Tasks** tab. For more information, see View migration tasks.

#### 2.7.2 Configure migration constraints

If the default migration task constraints, including the default migration rate and the default timeout period, do not meet your business requirements, you can configure custom constraints for migration tasks.

> **Note:** The new default migration rate and timeout period take effect on the migration tasks that are created after you modify the default migration rate and timeout period.

2. In the top navigation bar, choose **Product Operation > Computing > Compute**
3. In the left-side navigation pane, click **Migration Tasks**.
The **ECS Migration Tasks** tab under the **Tasks** tab appears.
4. Click the **Migration Constraint Configurations** tab.
5. Configure the parameters and click **Submit**.
**Default Migration Rate Configurations:** Configure the default rates for migration
tasks. If you do not specify migration rates for migration tasks, the default migration rates are used.

> **Important:** If you specify a migration rate when you create a migration task for a single Elastic Compute Service (ECS) instance, the migration task is executed at the specified rate. If you do not specify a migration rate when you create a migration task, the migration is performed based on **KVM Instance** **Migration Rate** or **ECS Bare Metal Instance Migration Rate** described in the following table.
> You cannot configure the migration rate when you create a machine migration task or a batch migration task. The following table describes the migration rates of different migration tasks. Subtasks are performed preferentially based on **Machine Migration Rate** or **Batch Migration Rate** described in the following table.

| Parameter | Description | Default value |
|---|---|---|
| KVM Instance Migration Rate | The default migration rate for ECS instances that use the Kernel-based Virtual Machine (KVM) architecture. Unit: Mbit/s. Valid values: 20 to 2000. Note We recommend that you use a default rate of no less than 500 Mbit/s. | 500 |
| ECS Bare Metal Instance Migration Rate | The default migration rate for ECS bare metal instances that use the Shenlong architecture. Unit: Mbit/s. Valid values: 20 to 2000. Note We recommend that you use a default rate of no less than 1,024 Mbit/s. | 1024 |

| Machine Migration Rate | The default migration rate for machine migration. Unit: Mbit/s. Valid values: 20 to 2000. Note We recommend that you use a default rate of no less than 800 Mbit/s. | 800 |
|---|---|---|
| Batch Migration Rate | The default migration rate for batch migration. Unit: Mbit/s. Valid values: 20 to 2000. Note We recommend that you use a default rate of no less than 800 Mbit/s. | 800 |

**Default Timeout Configurations**: Configure the default timeout period for each type of
migration task. You cannot configure the timeout period when you create a migration task. You can only use the default timeout period.

> **Important:** Before you configure the default timeout period for a type of migration task, take note of the following items:
> The value of the **ECS Migration Timeout Period** parameter must be less than the value of the **Server-level Migration Timeout Period** and **Batch** **Migration Timeout Period** parameters.
> If a migration task times out, the migration task fails. We recommend that you do not set the default migration timeout period to a value less than 5 minutes.

| Parameter | Description | Default value |
|---|---|---|
| ECS Migration Timeout Period | The timeout period of a migration task for a single ECS instance. Unit: minutes. Valid values: 2 to 60. | 20 |
| Server-level Migration Timeout Period | The timeout period of a machine (server- level) migration task. Unit: minutes. Valid values: 2 to 120. | 60 |
| Batch Migration Timeout Period | The timeout period of a batch migration task. Unit: minutes. Valid values: 2 to 120. | 60 |

#### 2.7.3 View CPU compatibility configurations

If **Enhanced Hot Migration Compatibility** is enabled when you create a hot migration task for an Elastic Compute Service (ECS) instance, the migration is successful only if the CPUs of the source and destination physical machines are compatible. An CPU incompatibility issue causes the hot migration task to fail. Before you enable the **Enhanced Hot Migration**
**Compatibility** feature, we recommend that you follow the procedure in this topic to view the
CPU models that support migration across physical servers and the CPU compatibility information.

> **Important:** Take note of the following items:
> If you cannot find the CPU compatibility information on the **CPU Compatibility** **Configurations** tab, you cannot migrate ECS instances that are in the Running state in the Apsara Uni-manager Operations Console. As a result, the hot migration task fails.
> You cannot add hot migration CPU compatibility information in the Apsara Uni- manager Operations Console.

2. In the top navigation bar, choose **Product Operation > Computing > Compute**
3. In the left-side navigation pane, click **Migration Tasks**.
The **ECS Migration Tasks** tab under the **Tasks** tab appears.
4. On the page that appears, click the **CPU Compatibility Configurations** tab.
You can view CPU compatibility information in the CPU list. You can search for CPU compatibility information by source CPU model.

| Parameter | Description |
|---|---|
| Source CPU Model | The CPU model of the physical server on which the ECS instance to be migrated resides. |
| Destination CPU Model | The CPU model of the physical server to which you want to migrate the ECS instance. |

### 2.8 Computing O&M configurations

**configurations**

#### 2.8.1 View monitoring settings

This topic describes how to enable the feature of pushing alerts to the alert list in the Apsara Uni-manager Operations Console for an Elastic Compute Service (ECS) monitoring metric and configure alert levels.

**Scenarios**

After you enable the feature of pushing alerts to the alert list in the Apsara Uni-manager Operations Console for an ECS monitoring metric and configure alert levels for the monitoring levels of the metric, log on to the Apsara Uni-manager Operations Console. In the top navigation bar, choose **Monitor&Alarms > Alerts > Alerts** to go to the Alerts page in the Alerts console. Then, you can find information about the alerts generated for the ECS monitoring metric in the alert list, including the alert levels, and troubleshoot issues based on the alert details.

> **Note:** For information about how to view alerts, see the **General O&M > Alerts** chapter in the Apsara Uni-manager Operations Console User Guide.

**Instructions**

Alerts generated for an ECS monitoring metric are displayed in the alert list in the Alerts console only after you enable the feature of pushing alerts to the alert list in the Apsara Unimanager Operations Console for the metric and configure alert levels for the monitoring levels of the metric. To display and view alerts generated for an ECS monitoring metric in the alert list in the Alerts console, perform the following steps:
1. Open the Edit dialog box of an ECS monitoring metric and select the Push Alert to Apsara
Uni-manager Operations Console option. In the **Apsara Uni-manager Operations**
**Console Alert Level** section, configure alert levels. For more information, see the
Procedure section of this topic. Section 1 in the preceding figure: displays the Push Alert to Apsara Uni-manager Operations Console option. Select this option to enable the feature of pushing alerts to the alert list in the Apsara Uni-manager Operations Console. Section 2 in the preceding figure: displays the monitoring levels of the ECS monitoring metric.

> **Note:** Each ECS monitoring metric has one or more built-in monitoring levels. The following monitoring levels are arranged from the highest to lowest severity level:

```
 fatal
 critical
 warning
 low_warning
```

> Different ECS monitoring metrics have different monitoring levels.
> For example, the pync_prepare_vm_exception metric has the `critical` and
> `warning` monitoring levels. The nc_session_too_large metric has the `fatal` monitoring level. The actual monitoring levels of each ECS monitoring metric are displayed on the **Monitoring** tab of the **Computing O&M** **Configurations** page in the **Compute Operations Console**.

Section 3 in the preceding figure: displays the alert levels for monitoring levels.

> **Note:** The following alert levels are arranged from the highest to lowest severity level:
> P1: critical
> P2: major
> P3: minor
> P4: information

2. View alerts.
After an alert is generated for an ECS monitoring metric, log on to the Apsara Uni-manager Operations Console. In the top navigation bar, choose **Monitor&Alarms > Alerts >**
**Alerts**. Then, enter the ECS monitoring metric name in the search box. In the search
results, you can view the alerts of the **alert level** that you configured in Step 1, as shown in the following figure.

> **Important:** If you configure multiple alert levels for an ECS monitoring metric, such as `critical` and `warning` , and alerts of an alert level are generated for the metric, the alerts are pushed to the alert list in the Alerts console. In this case, multiple alerts of different alert levels for the ECS monitoring metric may be displayed in the alert list.

2. In the top navigation bar, choose **Product Operation > Computing > Compute**
3. In the left-side navigation pane, click **ECS O&M Settings**.
4. Click a tab corresponding to a monitoring metric category under the **Monitoring** tab.
The monitoring metric category-specific tab displays a list of ECS monitoring metrics that includes the following columns: Metric, Description, Monitoring Type, Resource Type, Push to Apsara Uni-manager Operations Console, and Apsara Uni-manager Operations Console Alert Level.

| Monitoring metric category | Description |
|---|---|
| Control-side Monitoring | Includes the monitoring metrics for the ECS software control side. Example: monitor data loss too long, which indicates _ _ _ _ that monitoring data is unexpectedly missing for an extended period of time. |
| Virtualization Monitoring | Includes the monitoring metrics for the virtualization services on ECS physical machines. Example: vm monitor qemu exception, which indicates that an _ _ _ exception occurred while collecting virtualization-related monitoring data of virtual machines (VMs). |
| System Monitoring | Includes the monitoring metrics for the operating systems of ECS physical machines. Example: cgroup mem limitation, _ _ which indicates that the memory usage of a cgroup exceeds the limit. |
| Hardware Monitoring | Includes the monitoring metrics for ECS physical machine hardware. Example: hardware exception alarm, which _ _ indicates that alerts are generated for hardware exceptions. |
| Hang Monitoring | Includes the monitoring metrics for the hangs of ECS physical machines. Example: nc hang exception, which indicates that _ _ ECS physical machines freeze. |
| Failover Monitoring | Includes the monitoring metrics for physical machine-triggered failovers of ECS instances. Example: nc down alert, which _ _ indicates that ECS instances are failed over when the physical machine on which the instances reside is down. |

5. On the **Operation** column of the monitoring metric category-specific tab, click **Edit** to
modify the parameters of monitoring metrics. The following table describes the parameters.

| Parameter | Description |
|---|---|

| Push Alert to Apsara Uni-manager Operations Console | Specifies whether the generated alerts are pushed to the alert list in the Apsara Uni-manager Operations Console. Valid values: Yes and No. Important No: The generated alerts are not pushed to the alert list. In this case, you cannot find the alerts in the alert list and may fail to obtain important alert information. Yes: The generated alerts are pushed to the alert list. In this case, the alerts are displayed in the alert list only if you configure the Apsara Uni-manager Operations Console Alert Level parameter. |
|---|---|
| Apsara Uni-manager Operations Console Alert Level | The alert levels displayed in the alert list. The following monitoring levels of the monitoring metric may be displayed: fatal critical warning low warning _ The valid values of alert levels for monitoring levels may vary based on the monitoring metric category. For the Control-side Monitoring, Virtualization Monitoring, System Monitoring, Hardware Monitoring, and Hang Monitoring categories, the valid values of alert levels for monitoring levels are P2, P3, and P4. For the Failover Monitoring category, the valid values of alert levels for monitoring levels are P2, P3, and P4. Important If you changed the alert level for the monitoring level of a failover monitoring metric from P1 to P2, P3, or P4, you cannot roll back the alert level to P1. |

6. Click **OK**.
You can find a metric in the monitoring metric list and view the alert levels in the JSONformatted array displayed in the **Apsara Uni-manager Operations Console Alert Level** column.

#### 2.8.2 Configure O&M actions

##### 2.8.2.1 Configure throttling for a proactive O&M action

**action**

You can configure throttling limits for proactive O&M actions, such as the maximum number of times that the workflow of a proactive O&M action can be executed within the specified execution window. This prevents proactive O&M actions from being repeatedly and unnecessarily executed. This topic describes how to configure throttling for a proactive O&M action.

**Background information**

You can adjust throttling limits for proactive O&M actions based on actual conditions and onsite O&M requirements. For example, a proactive O&M action is configured to be executed when a physical machine freezes. If the proactive O&M action is executed but does not resolve the issue and the physical machine remains frozen, the action is executed repeatedly to deactivate and reactivate the physical machine until the physical machine is recovered. In this case, you can configure throttling limits for the proactive O&M action. For example, you can configure throttling limits to allow the proactive O&M action to be executed only one time within a 168-hour execution window. This way, after the proactive action is executed, the Apsara Uni-manager Operations Console does not execute the action again within the next 168 hours, and you can perform other O&M operations to resolve the physical machine freeze issue at the earliest opportunity.
2. In the top navigation bar, choose **Product Operation > Computing > Compute**
3. In the left-side navigation pane, click **ECS O&M Settings**.

> **Note:** By default, the **Monitoring** tab appears.

4. Click the **O&M Actions** tab.
A list of proactive O&M actions is displayed, which includes the **OpsCode** (O&M type),
**Throttling Status**, and **Throttling Effective Time** columns.
The **Support for Manual Reporting** and **Approval for Manually Reported O&M**
**Workflow** parameters of a proactive O&M action vary based on the approval
configuration of the action. For more information, see Configure the approval process for a proactive O&M action.
5. Find the proactive O&M action that you want to manage and click **Configure Throttling** in
the **Operation** column. In the Configure Throttling dialog box, configure parameters and click **OK**. The following table describes the parameters.

|   | Important If a proactive O&M action exceeds a regional or cluster-wide throttling limit, the Apsara Uni-manager Operations Console no longer executes the action. |   |
|---|---|---|

| Parameter | Description |
|---|---|
| opscode | The O&M type of the proactive O&M action. This parameter cannot be modified. |
| Throttling Status | Specifies whether to enable throttling for the proactive O&M action. |
| Throttling Window (Minutes) | The execution window of the proactive O&M action within the region. Unit: minutes. We recommend that you set this parameter to 10080. 10,080 minutes equals 168 hours. |
| Throttling Threshold | The maximum number of times that the workflow of the proactive O&M action can be executed in the region. We recommend that you set this parameter to 1. |
| Cluster-wide Throttling Window (Minutes) | The execution window for the proactive O&M action within the cluster. Unit: minutes. We recommend that you set this parameter to 10080. 10,080 minutes equals 168 hours. |
| Cluster-wide Throttling Window (Minutes) | The maximum number of times that the workflow of the proactive O&M action can be executed in the cluster. We recommend that you set this parameter to 1. |
| Throttling Policy | Set this parameter to Cancel, which specifies that the workflow is canceled when the proactive O&M action exceeds a throttling limit. |

##### 2.8.2.2 Configure the approval process for a proactive O&M action

**proactive O&M action**

You can enable the Support for Manual Reporting feature for proactive O&M actions to submit relevant proactive O&M events and initiate O&M. You can also configure the approval process for proactive O&M actions based on your business requirements.

**Background information**

On-site O&M personnel can create proactive O&M actions and configure the approval process for the actions, such as skipping the approval steps to perform the actions, based on actual scenarios and on-site O&M requirements. After you create a proactive O&M action and configure the approval process for the action, you must ask an Apsara Uni-manager Operations Console administrator to perform the following operations before you can perform the proactive O&M action: Log on to the Apsara Uni-manager Operations Console, choose Platform Operation > O&M Change > Process Approval in the top navigation bar, choose **Process Approval > Pending Approval** in the left-side navigation pane of the
**O&M Change** console, and then approve the submitted proactive O&M events.

> **Important:** Skipping the approval process may affect subsequent audits. We recommend that you retain the approval process for an Apsara Uni-manager Operations Console administrator to follow.

On-site O&M personnel can configure the **Support for Manual Reporting** feature for proactive O&M actions based on actual operating conditions to prevent accidental operations. For example, you can set the **Support for Manual Reporting** parameter to No in the **Configure Approval** dialog box to disable the Support for Manual Reporting feature for the **0x400012-Force NC OOB Reboot** proactive O&M action (O&M type). This way, you cannot select the proactive O&M action when you submit a proactive O&M event in the **Submit Proactive O&M Event** dialog box. This helps reduce related accidental operations.

**Considerations**

By default, the **Support for Manual Reporting** feature is enabled for proactive O&M actions. You can submit proactive O&M events related to proactive O&M actions.

> **Important:** You can submit proactive O&M events related to only the proactive O&M actions for which the Support for Manual Reporting feature is enabled. For information about how to submit a proactive O&M event, see Submit a proactive O&M event for a server.

The O&M types for which you can configure the Support for Manual Reporting feature and the Approval for Manually Reported O&M Workflow feature are displayed in the Apsara Unimanager Operations Console. You can use only the default setting of the Approval for Manually Reported O&M Workflow feature for specific O&M types, but cannot change the default setting. For example, the Support for Manual Reporting feature is automatically enabled and the Approval for Manually Reported O&M Workflow feature is automatically disabled for the **0x4000A000000007-Unlock Nc** O&M type. In this case, the proactive O&M action can be performed without the need for approval of an Apsara Uni-manager Operations Console administrator after you submit a proactive O&M event related to the O&M type.
2. In the top navigation bar, choose **Product Operation > Computing > Compute**
3. In the left-side navigation pane, click **ECS O&M Settings**.

> **Note:** The **Monitoring** tab appears.

4. Click the **O&M Actions** tab.
On the O&M Actions tab, you can view information about each proactive O&M action in the action list, such as the O&M type (**OpsCode**), whether relevant proactive O&M events can be manually submitted (**Support for Manual Reporting**), and whether the manually submitted proactive O&M events require approval (**Approval for Manually Reported**
**O&M Workflow**).
5. Find the proactive O&M action that you want to manage and click **Configure Approval** in
the **Operation** column. In the dialog box that appears, configure the parameters and click
**OK**. The following table describes the parameters.

| Parameter | Description |
|---|---|
| opscode | The O&M type. You cannot change the value of this parameter. |
| Support for Manual Reporting | Specifies whether you can submit proactive O&M events related to the proactive O&M action on the Proactive O&M page. Default value: Yes. Important If you set this parameter to No, you cannot submit proactive O&M events related to the proactive O&M action on the Proactive O&M page. Proceed with caution when you set this parameter to No. |
| Approval for Manually Reported O&M Workflow | Specifies whether manually submitted proactive O&M events require approval. Default value: Yes. Important If you set this parameter to No, the proactive O&M action can be performed without the need for approval. |

##### 2.8.2.3 Submit a proactive O&M event for a server

This topic describes how to submit a proactive O&M event for the hardware, system, or kernel of a server.

**Prerequisites**

The **Support for Manual Reporting** feature is enabled for the proactive O&M action that you want to perform. For more information, see Configure the approval process for a proactive O&M action.

**Background information**

If an exception occurs in a server component and the exception supports proactive O&M, you can obtain information about the component or exception from the alert list in the Apsara Uni-manager Operations Console. If you want to perform proactive O&M to resolve the exception, follow the instructions described in this topic to submit a proactive O&M event.

> **Warning:** During proactive O&M, services may be interrupted due to operations such as server restarts. Therefore, you must obtain the authorization from users and proceed with caution.

When you submit a proactive O&M event, you can select only a proactive O&M action for which the Support for Manual Reporting feature is enabled. This feature allows you to block proactive O&M actions based on your business requirements and prevents high-risk operations from being triggered by incorrect proactive O&M actions.

> **Important:** Before you submit a proactive O&M event, make sure that the selected proactive O&M action can resolve the exception in the actual environment. Otherwise, the proactive O&M action fails to be performed.

2. In the top navigation bar, choose **Product Operation > Computing > Compute**
3. In the left-side navigation pane, choose **ECS Intelligent O&M > ECS O&M Event**.
4. On the **Proactive O&M** page, click **Submit Proactive O&M Event**.
5. In the **Submit Proactive O&M Event** dialog box, configure parameters and click **OK**. The
following table describes the parameters.

| Parameter | Description |
|---|---|
| IP | The IP address of the server on which you want to perform the proactive O&M action. |

| Proactive O&M Type | The type of the proactive O&M action, which is theO psCode of the proactive O&M event. Valid values: Important The configuration parameters vary based on the type of the proactive O&M action. Configure the parameters as prompted. 0x410A01-Lock NC: locks the physical server. When the physical server is locked, Elastic Compute Service (ECS) instances cannot be created on or migrated to the physical server. 0x40003000001001-OOB Reboot NC without live migration: migrates ECS instances on the physical server in the O&M window and then restarts the physical server. 0x40003000001066-Change NC configuration: changes the configurations of the physical server. 0x400003-OOB Reboot NC with live migration: hot migrates ECS instances on the physical server and then restarts the physical server. 0x400012-Force NC OOB Reboot: forcibly restarts the physical server. 0x400011-recover NC status online: restores the physical server to a normal state. 0x3000000000802-Clean Wild Vm: clears residual ECS instances in the environment. 0x400016-Start Local Disk Nc: performs an out-of-band (OOB) restart on the physical server and then starts ECS instances after the physical server is down due to a local disk failure. 0x400018-Mark NC Down And Vm Migrate: forcibly migrates ECS instances on the physical server when the physical server is down. 0x30000000001005-Start Crashed Vm: restarts ECS instances on the physical server after a crash occurs. 0x40001000008001-Stop MOC While CN Down: marks the Microserver On Card (MoC) as down and cleans the MoC after the controller node (CN) of an ECS bare metal instance is down. 0x4000A000000008-memory defragmentation: cleans memory fragments on the physical server. 0x4000A000000007-Unlock Nc: unlocks the physical server after it is locked. 0x30003000001001-Start Vm: starts ECS instances on the physical server. 0x99001000000001-Local Disk Nc Repair: isolates local disks on the physical server and replaces the disks for maintenance. 0x30000000000408-Qemu live upgrade: hot upgrades the QEMU process. 0x8000000000001-Nc Offline And Repair: shuts down the physical machine for maintenance. |
|---|---|

| Reason Type | The reason why you want to perform the proactive O&M action on the physical server. The following reasons are available: Note The reasons that are displayed in the Apsara Uni-manager Operations Console prevail. Hardware failures, such as failures in the fan, storage card, and motherboard. Kernel errors, such as cgroup-level out of memory (OOM) errors. Network failures, such as network cable failures. System failures, such as memory fragmentation failures. Abnormal shutdown. Security protection, such as the protection against DDoS attacks. Internal restarts. |
|---|---|
| Reason | The detailed reason for the proactive O&M action. |

### 2.9 View the computing O&M data

In the Compute Operations Console, you can view the computing O&M data in the current environment, including the data of migration, custom instance types, O&M, and monitoring. This allows you to monitor abnormal fluctuations, changes in the number of proactive O&M actions, number of migrations, and status changes in the current environment. This topic describes how to view the computing O&M data.
2. In the top navigation bar, choose **Product Operation > Computing > Compute**
3. In the left-side navigation pane, click **Computing O&M Data**.
4. On the Computing O&M Data page, view the computing O&M data.
By default, the computing O&M data of the previous seven days is displayed. You can also select a time range from the Time Range drop-down list in the upper-right corner of the page. The supported time ranges include the previous seven days, one month, three months, and half a year. If you want to analyze the detailed O&M data, click **Export O&M Data** in the upper-right corner to export the data to your computer.

| Section | Description |
|---|---|
| ECS O&M Resource Overview | This section displays the numbers of Elastic Compute Service (ECS) instances, physical servers, and clusters in the current environment. |

| Migrated Data Overview | This section displays the numbers of hot migration instances, cold migration instances, and server-level migration instances in the current environment. |
|---|---|
| Custom Instance Overview | This section displays the total number of custom instance types in the current environment. You can click View Details in the upper-right corner of the Custom Instance Overview section to go to the Specifications page. For more information about custom instance types, see View a custom instance type. |
| Physical Machine O&M | This section displays the numbers of physical server O&M operations, maintained physical servers, and physical servers in O&M in the current environment. You can click View Details in the upper-right corner of the Physical Machine O&M section to view details on the Proactive O&M page. |
| Instance O&M | This section displays the numbers of ECS instance O&M operations, maintained ECS instances, and ECS instances in O&M in the current environment. You can click View Details in the upper-right corner of the Instance O&M section to view details on the Proactive O&M page. |
| ECS Monitoring & Alerting Statistics | This section displays the top 10 alerts of each alert level that have been handled by ECS O&M within the previous week on the P1 Critical, P2 Major, and P3 Minor tabs. The time period cannot be modified. To view the information about all alerts, clickV iew Details in the upper-right corner of the ECS Monitoring & Alerting Statistics section to go to the Alerts page. For more information, see 3.2.2. Alerts in the Apsara Uni-man ager Operations Console User Guide. |

### 2.10 AI/HPC O&M

#### 2.10.1 Manage cluster data replication tasks on a client

**on a client**

When Elastic Compute Service (ECS) instances of the Super Computing Cluster (SCC) type are used as nodes in an Elastic High Performance Computing (E-HPC) cluster and a Cloud Parallel File Storage (CPFS) file system is mounted to the instances, you can create a data replication task to upload data from the SCC ECS instances to Object Storage Service (OSS) buckets or download data from OSS buckets to the SCC ECS instances. This facilitates data transfer between CPFS and OSS.

**Prerequisites**

OSS is activated and an OSS bucket is created. For more information, see the **Quick start >**
**Create buckets** chapter of User Guide - Object Storage Service in the Apsara Stack
Documentation Center.

**Scenarios**

When you create a cluster in the E-HPC console and use SCC ECS instances as nodes in the cluster, an SCC is automatically generated on the **Super Computing Cluster** page of the ECS console after the cluster is created, and CPFS file systems are automatically mounted to the nodes (SCC ECS instances) in the SCC. For more information, see the **Manage clusters > Create a cluster** chapter of "E-HPC User Guide" in the Apsara Stack Documentation Center. For information about SCC instance types, see the **Intel-based instance families > SCC**
**instance families** chapter of ECS Instance Families & Instance Types in the Apsara Stack
Documentation Center. This topic describes how to upload data from an SCC ECS instance to which a CPFS file system is mounted to an OSS bucket, or download data from the OSS bucket to the ECS instance to transmit data between the CPFS file system and OSS bucket.

**Create a data replication task**

If your SCC ECS instance has a large amount of data or contains cold data, you can create a data replication task to upload the data to an OSS bucket for storage. You can also download data from the OSS bucket to the ECS instance to transmit data between the CPFS file system and OSS bucket. After you create a data replication task, the task is automatically executed. Perform the following steps:
2. In the top navigation bar, choose **Product Operation > Computing > Compute**
3. In the left-side navigation pane, choose **AI/HPC O&M > Client Cluster Management >**
**Client Cluster Data Replication** .
4. On the **CPFS/OSS Data Replication Tasks** page, click **Create Task**.
5. In the **Create Data Replication Task** panel, configure the parameters. The following
table describes the parameters.

| Parameter | Description |
|---|---|
| Apsara Stack Tenant Account ID | The ID of the Apsara Stack tenant account. |
| Data Flow Direction | The transfer direction of the data in the replication task. Valid values: Upload: uploads data from an SCC ECS instance to an OSS bucket. Download: downloads data from an OSS bucket to an SCC ECS instance. |
| Instance ID | Enter the ID of the ECS instance from which you want to upload data to an OSS bucket or to which you want to download data from an OSS bucket. |
| File Path | Enter the absolute path of a file or directory on the specified instance. Important The path must end with a forward slash (/). Example: /root/ . |

| Endpoint Domain Name | The OSS endpoint of the region in which the OSS bucket resides. |
|---|---|
| Bucket Name | The name of the OSS bucket. |
| Object Path | The absolute path of the OSS object. The path cannot contain the OSS bucket name. Important The path must end with a forward slash (/). Example: /root/ . |
| Speed Limit | The maximum transfer speed of the data replication task. Unit: KB/s. Default value: 0. A value of 0 specifies that the upload speed is unlimited. |

6. After you configure the parameters, click **OK**.
You can view the created task in the task list on the **CPFS/OSS Data Replication Tasks** page. If the migration task enters the **Completed** state, the task is complete.

**Verify the execution result**

You can view files and file paths for data uploaded from an SCC ECS instance to an OSS bucket or downloaded from an OSS bucket to an SCC ECS instance.
2. In the top navigation bar, choose **Product Operation > Computing > Compute**
3. In the left-side navigation pane, choose **AI/HPC O&M > Client Cluster Management >**
**Client Cluster Data Replication** .
4. In the task list, find the task whose execution result you want to view and click **View**
**Result** in the **Operation** column.
You can view the execution result of the data replication task in the **Data Replication**
**Task Result** dialog box.
5. Click **OK**.

**Delete a data replication task**

If you no longer require a task, you can delete the task from the task list.

> **Important:** If the task that you want to delete is in progress, the deletion is complete and the task information is removed from the task list. However, the execution of the task is not interrupted.

2. In the top navigation bar, choose **Product Operation > Computing > Compute**
3. In the left-side navigation pane, choose **AI/HPC O&M > Client Cluster Management >**
**Client Cluster Data Replication** .
4. In the data replication task list, find the task that you want to delete and click **Delete** in the
**Operation** column.
5. In the message that appears, check the task information and click **Delete**.

#### 2.10.2 Manage ACL whitelists for an RDMA network

**network**

For security reasons, clusters in a Remote Direct Memory Access (RDMA) network, such as Platform of Artificial Intelligence (PAI) clusters and Elastic High Performance Computing (E- HPC) clusters, cannot communicate with each other by default. If you want a PAI cluster and a Super Computing Cluster (SCC) E-HPC cluster to share one Cloud Parallel File Storage (CPFS) file system, you must create an access control list (ACL) whitelist to allow the clusters to communicate. Then, mount the CPFS file system to the PAI cluster.

> **Important:** If you want to use the ACL whitelist feature, contact Apsara Stack technical support to deploy this feature. In the left-side navigation pane of the Apsara Uni-manager Operations Console, choose **AI/HPC O&M > RDMA Network Configurations > RDMA** **Whitelist Configurations**.

**Scenarios**

In the RDMA network, the networks between clusters have the following characteristics: Networks within the same cluster are accessible to each other. For security reasons, different clusters, such as PAI clusters and E-HPC clusters, cannot communicate with each other across networks by default. By default, PAI clusters and SCC E-HPC clusters use RDMA networks. Therefore, PAI clusters and SCC E-HPC clusters cannot communicate with each other across networks by default.

> **Note:** For information about PAI clusters, see the **Resource Management > Overview** chapter of Platform of AI in the Apsara Stack Documentation Center.
> For information about E-HPC clusters, see the **Manage clusters > Create a** **cluster** chapter of E-HPC User Guide in the Apsara Stack Documentation Center.

The following figure shows how a PAI cluster shares a CPFS file system with an SCC E-HPC cluster.

| One-to- E-HPC Cluster one SCC (ehpc-test) Mapping (hpc-test) RDMA Network Cluster | 2. After you create an | PAI Cluster (pai-eflops-A-test) RDMA Network Cluster |
|---|---|---|

| 1. When you create the E-HPC cluster, the CPFS file system is mounted to | th3e | . cYluosut ecra.n B my oduenfat utlht,e n CePtFwSo rfkiles asyres tienmte rtcoo tnhnee PctAeId c launsdte ar no nAlCyL a wfthei |
|---|---|---|

CPFS
1. Create an SCC E-HPC cluster to which a CPFS file system is mounted and a PAI cluster.
When you create the SCC E-HPC cluster, an SCC is created in the ECS console of the Apsara Uni-manager Management Console. The cluster ID is in the `hpc-xxxx` format. Then, an ECS instance of the SCC instance type is added to the created SCC as a cluster node. This way, an SCC E-HPC cluster is created. The cluster ID is in the `ehpc-xxxx` format. The SCC and E-HPC clusters correspond to the same RDMA network cluster.

> **Note:** For information about SCC instance types, see the **Super computer clusters** chapter of User Guide - Elastic Compute Service in the Apsara Stack Documentation Center.

2. Create an ACL whitelist for the PAI cluster and the E-HPC cluster.
3. Mount the CPFS file system to the PAI cluster.

**Preparations**

**Create clusters**

Create an SCC E-HPC cluster and mount a CPFS file system to the cluster. For more information, see the **Manage clusters > Create a cluster** chapter of E-HPC Use r Guide in the Apsara Stack Documentation Center.

> **Note:** When you create an SCC E-HPC cluster, you must set the control nodes and compute nodes of the cluster to **ECS instances of the SCC type** and mount a CPFS file system to the instances. For more information, see the **Intel-based instance families > SCC** **instance families** chapter of Introduction to Instance Families and Instance Types in the Apsara Stack ECS Documentation Center.

After you create the SCC E-HPC cluster, take note of the following items: By default, SCC E-HPC clusters can access CPFS file systems. On the **RDMA ACL Whitelists** page in the Apsara Uni-manager Operations Console, an ACL whitelist is automatically created to enable network communication. Create a PAI cluster. The PAI cluster used in this example is the PAI-Eflops cluster used to train the PAI model. The cluster name is in the `pai-eflops-*-****` format. For more information, see the

**Resource Management > Create and manage intelligent computing resources**

chapter of Platform of AI in the Apsara Stack Documentation Center.

**Obtain cluster parameters**

You can perform the following operations to obtain the parameters required to create an ACL whitelist for network communication between a PAI cluster and an SCC E-HPC cluster.

> **Important:** You can use only the parameters related to the SCC cluster to search for the RDMA network cluster that corresponds to the E-HPC cluster to allow the clusters to communicate with each other. You must obtain the user ID, cluster ID, and region ID of the SCC cluster.

**Source cluster name**

To obtain the **source cluster name** of a PAI cluster, perform the following steps:
2. In the top navigation bar, choose **Product Operation > Platform Operation > Apsara**
**Infrastructure Management**.
3. In the left-side navigation pane, click **Product & Cluster O&M**.
4. In the **Products** section, select a zone in the **Zone** drop-down list and enter `pai-eflops`
in the **Product | Cluster** search box. In the search results, the cluster name in the `pai-eflops-*-****` format is the name of the destination PAI cluster.

> **Note:** In most cases, only one cluster whose name is in the `pai-eflops-*-****` format appears. You can copy and paste the cluster name.

**User ID**

The user ID is the Apsara Stack tenant account ID. You can perform the following operations to obtain the ID of the Apsara Stack tenant account to which the SCC belongs.
1. Obtain the **Management Node ID** of the SCC cluster on the **Cluster** page in the E-HPC
console of the Apsara Uni-manager Management Console. For more information, see the **Manage clusters > View cluster details** chapter of E-HPC User Guide in the Apsara Stack Documentation Center.
2. In the Apsara Uni-manager Operations Console, search for the obtained node ID, which is
the SCC ECS instance ID in the ECS instance list. For information about how to obtain the ID of an ECS instance, see View ECS instances.
3. Click the ID of the ECS instance that you searched for by the management node ID. Then,
the instance details page appears. The **Apsara Stack Tenant Account ID** in the **Basic Information** section is the user ID.

**SCC ID**

1. Obtain the **Management Node ID** of the SCC cluster on the **Cluster** page in the E-HPC
console of the Apsara Uni-manager Management Console. For more information, see the **Manage clusters > View cluster details** chapter of E-HPC User Guide in the Apsara Stack Documentation Center.
2. In the ECS instance list in the Apsara Uni-manager Management Console, search for the
obtained node ID, which is the SCC ECS instance ID. For more information, see the **Instances > Manage instance attributes > View**
**instance details** chapter of User Guide - Elastic Compute Service in the Apsara Stack
Documentation Center. The **cluster ID** of the instance that you searched for by the management node ID is the SCC ID.

**ID of the region in which the SCC resides**

1. Obtain the **Management Node ID** of the SCC cluster on the **Cluster** page in the E-HPC
console of the Apsara Uni-manager Management Console. For more information, see the **Manage clusters > View cluster details** chapter of E-HPC User Guide in the Apsara Stack Documentation Center.
2. In the ECS instance list in the Apsara Uni-manager Management Console, search for the
obtained node ID, which is the SCC ECS instance ID. For more information, see the **Instances > Manage instance attributes > View**
**instance details** chapter of User Guide - Elastic Compute Service in the Apsara Stack
Documentation Center.
3. Click the ID of the ECS instance that you searched for by the management node ID. The
**Instance Details** tab appears.
The **Region** parameter in the **Basic Information** section displays the ID of the region in which the SCC resides.

**Create an ACL whitelist**

You can perform the following operations to add an ACL whitelist for the PAI cluster and the SCC E-HPC cluster. This way, the PAI cluster and the SCC E-HPC cluster can communicate with each other.

> **Important:** Before you create an ACL whitelist, take note of the following items:
> You can configure an ACL whitelist only for a PAI cluster and an SCC E-HPC cluster that belong to the same Apsara Stack tenant account.
> You need to only add one ACL whitelist to allow communication between the PAI cluster and the SCC E-HPC cluster.

2. In the top navigation bar, choose **Product Operation > Computing > Compute**
3. In the left-side navigation pane, choose **AI/HPC O&M > RDMA Network Configurations**
**> RDMA Whitelist Configurations**.
4. On the **RDMA ACL Whitelists** page, click **Create ACL Whitelist**.
5. In the **Create ACL Whitelist** panel, configure the parameters.

> **Important:** You can use only the parameters of the SCC cluster to search for the RDMA network cluster corresponding to the E-HPC cluster. This way, the RDMA network cluster can communicate with the SCC E-HPC cluster. You must obtain the ID of the SCC ECS instance, cluster ID, and region ID. For more information, see the Obtain cluster

parameters section of this topic.

| Parameter |   | Description |   | Example |
|---|---|---|---|---|
| Source Product Name |   | The product name of the PAI cluster. The value is fixed to pai . |   | pai |
| Source Cluster Name |   | The name of the PAI cluster. |   | pai-eflops-A-**** |
| User ID |   | The ID of the Apsara Stack tenant account to which the SCC belongs. |   | 12345678910***** |
| HPC Cluster ID |   | The ID of the SCC cluster. |   | hpc- ep503s85wgqkey8***** |
| Region ID of HPC Cluster |   | The ID of the region in which the SCC cluster resides. |   | cn-test-env**-d01 |
| Port Rule |   | The list of ports that allow mutual access between the PAI cluster and the SCC E- HPC cluster. The value is fixed to portOnly (1191, |   | portOnly (1191, 2181, |
|   |   |   | portOnly (1191, | 8191, 9092 to 9093, 60000 to 61000). |
|   |   | 2181, 8191, 9092 to 9093, 60000 to |   |   |
|   |   | 61000) |   |   |

6. After you configure the parameters, click **Confirm**.
On the **RDMA ACL Whitelists** page, you can view the ACL whitelist information, including
**ACL ID**, **Source Product Name**, **Source Cluster Name**, and **Port List**.

> **Note:** After the ACL whitelist is created, the PAI cluster and the SCC E-HPC cluster can immediately communicate with each other.

**What to do next**

After the PAI cluster and the SCC E-HPC cluster can communicate with each other, you must mount the CPFS file system to the PAI cluster in the PAI console of the Apsara Uni-manager Management Console. After the CPFS file system is mounted, the PAI cluster and the E-HPC cluster can share the CPFS file system. For more information, see the **AI Asset Management > Dataset Management > Create**
**and manage datasets** chapter of Platform of AI in the Apsara Stack Documentation Center.

## 3 VM hot migration

### 3.1 Overview

Hot migration is the process of migrating a running VM from one host to another. During migration, the VM runs normally and its services are not aware that any migration task is occurring. However, these services can detect a very short interruption between 100 and 1,000 ms.

**Scenarios**

During system operations and maintenance, hot migration is typically used for the following scenarios:
**Active O&M**: The host is faulty and must be repaired, but the fault does not affect the
operation of the system. You can use hot migration to migrate the VM to another host and repair the faulty host in offline mode.
**Server load balancing**: When a host is experiencing a high load, you can migrate some of
its VMs to other idle hosts to reduce resource consumption on the source host. Other scenarios where a VM must be migrated without affecting its business operations.

### 3.2 Limits

Before you perform hot migration, make sure that you are familiar with the limits on hot migration. The following limits apply to the hot migration feature of Apsara Stack: Migration can be performed only between physical machines of the same type that share the same versions of software.

> **Note:** Physical machines of the same type refer to the physical machines that have the same or compatible CPU models.

During hot migration, make sure that the network status of the physical machines is good. If the network connection of the physical machines is interrupted, the hot migration fails. The actual hot migration rate varies based on the remaining bandwidth of the physical machines and the speed limit configured when the migration is initiated. If the rate at which dirty pages are generated in the memory of the Elastic Compute Service (ECS) instance to be migrated exceeds the actual migration rate, the hot migration may last for an extended period of time or time out. ECS standard images support hot migration. When you migrate virtual machines (VMs) that use images excluded from the list, Apsara Stack is not responsible for errors that may occur. ECS instances that use local storage do not support hot migration. This is because after an ECS instance that uses local storage is migrated to a different physical machine, the instance loses access to the local storage. ECS instances that use GPUs, FPGAs, or other passthrough or single root input/output virtualization (SR-IOV) devices do not support hot migration. ECS instances to which elastic network interfaces (ENIs) of the Trunk or Member type are bound do not support hot migration.

> **Note:** VMs that were created in Apsara Stack V3.3 or earlier do not support hot migration. After you migrate the preceding VMs, you must restart the VMs for the migration to take effect.

### 3.3 Complete hot migration on AG

In the Apsara Uni-manager Operations Console, you can run commands to trigger and cancel hot migration operations.

**Trigger a hot migration operation**

> **Warning:** During a hot migration process, the underlying information, such as CPU FLAGS, of Elastic Compute Service (ECS) instances may change and your application authorization codes may become invalid.

After a hot migration operation is triggered for a virtual machine (VM), you can run the `go2which` command or use the ECS Operations and Maintenance System to check that the VM enters the **migrating** state. When the hot migration operation is complete, the VM returns to the **running** state. To trigger a hot migration operation, run the following `go2which` command:

```xml
go2hyapi live_migrate_vm == Functions usage: == |- live_migrate_vm <vm_name> [nc_id] [rate] [no_check_image] [no_check_load] [downtime]== Usage: == houyi_api.sh <function_name> [--help|-h] [name=value]
```

Table 1. Parameters

| Parameter | Description | Impact | Value |
|---|---|---|---|
| vm name _ | The name of the VM that you want to migrate. | N/A | N/A |
| nc id _ | The destination NC to which to migrate the VM. | If the NC does not support the specifications of the VM, the VM may fail to be migrated. | N/A |
| rate | The amount of bandwidth to allocate for the migration task. | The bandwidth resources of the physical machine are used for the migration. | 10 Gb network: 80 MB 1 Gb network: 40 MB |
| downtime | The maximum allowable downtime caused by migration. The default value is 300 ms. | The service downtime caused by migration is affected. | 200 ms to 2,000 ms |

| no check image _ _ | Forcefully migrates images that are not supported. | The Service Level Agreements (SLA) may be violated if this parameter is set to false. | false |
|---|---|---|---|
| no check load _ _ | Forcefully migrates images even when the load threshold requirements are not met. | Downtime cannot be controlled if this parameter is set to false. | false |

**Cancel a hot migration operation**

To cancel a hot migration operation, run the following command:

```
go2hyapi cancel_live_migrate_vm == Usage: == houyi_api.sh <function_name> [--help|-h] [name=value] == Functions usage: == |- cancel_live_migrate_vm <region_id> <vm_name>
```

Table 2. Parameters

| Parameter | Description | Impact | Value |
|---|---|---|---|
| vm name _ | The name of the VM that you want to migrate. | N/A | N/A |
| region id _ | The region ID of the VM. | N/A | N/A |

### 3.4 Modify the position of the NC where the VM is located

**where the VM is located**

When an exception occurs during hot migration and the migration cannot be rolled back through ECS Operations and Maintenance Platform, you can modify the VM state to trigger rollback.

**Trigger rollback**

If an exception occurs during hot migration, run the following command to trigger rollback:

```
go2hyapi call_api manually_change_migration_status == Functions usage: == |- call_api manually_change_migration_status <vm_name> <region_id> <where>
```

Table 1. Parameter description

| Parameter | Function | Impact | Value |
|---|---|---|---|
| vm name _ | The name of the VM to be migrated. | N/A | N/A |
| region id _ | The ID of the region where the target VM is located. | N/A | N/A |

| where | The ID of the NC where the VM is located. | N/A | N/A |
|---|---|---|---|

### 3.5 FAQ

This topic provides answers to some frequently asked questions about hot migrations.

**What are the required parameters to perform a hot migration by calling the**

**Server Controller API?**

vm_name: the name of a virtual machine (VM). nc_id

**How do I prepare for a hot migration?**

Confirm that the VM is in the running state. Confirm the server to which you want to migrate the VM.

**Can I cancel a hot migration? How do I cancel a hot migration?**

Yes, you can cancel a hot migration. If the API request is successful and the migration is not complete, you can run the `go2hyapi cancel_live_migrate_vm vm_name=<vm_name> region_id=` `<region_id>` command to cancel the hot migration. If the VM is migrated to the destination server, you cannot cancel the hot migration. You can obtain the value of the region_id parameter by running the `go2which <vm_name>` command and checking the returned region_info parameter.

**The VM is still in the migrating state after the hot migration is complete, and the**

**cancel_live_migrate_vm command is not working. What do I do?**

You can run the `virsh query-migrate <domid>` command on the source server of the VM to check whether the VM is being migrated. If the VM is being migrated, a piece of JSON information is returned. If the VM is migrated, run the following command on the AG to change the status of the VM:

```
go2hyapi manually_change_migration_status vm_name=<vm_name> where=<nc_id for the VM> region_id=<region_id>
```

domid is the name of the VM instance. You can run the virsh list|grep vm_name command to view the name.

**How do I check whether a VM is migrated?**

On the destination server of the VM, run the sudo virsh list|grep <vm_name> command. If the VM instance exists and is not in the Running state, the migration is successful.

**What logs do I refer to when an exception occurs during a hot migration?**

View the Libvirt underlying migration log on the server. Run the `/var/log/libvirt/libvirt.log` command to view information about the migration process, including log entries that contain keywords such as vport offline, detach, delete, and relay route. Run the following command to view the API management log of Server Controller on the AG:

```
/var/log/houyi/pync/houyipync.log
```

Run the following command to view the Qemu log:

```
/var/log/libvirt/qemu
```

Run the following command to view the regionmaster log on the VM:

```
regionmaster/logs/regionmaster/error.log
```

**A VM fails to start after a hot migration. Is the VM still in the pending state?**

If the **error vport update nc conf by vpc master failed dest_nc_id:xxx** error message is returned, the virtual private cloud (VPC) has an issue and the underlying task is interrupted.

**During a hot migration, the API returns the following error message: distributed**

**lock fail. What are the possible causes of this issue?**

The API is frequently called within a short period of time. Wait several minutes and then try again.

**What are the common scenarios in which migration fails? How do I resolve these**

**issues?** Table 1. Hot migration issues

| Scenario | Cause | Solution |
|---|---|---|
| The load is high and the VM migration fails the pressure inspection. | The service is interrupted for a long period of time. | You can set the no check load _ _ parameter to true to skip the inspection. |
| The VM fails the image inspection. | The image is not an Alibaba Cloud-specific image. | You can set the no check image parameter to _ _ true to skip the inspection. Proceed with caution. |

## 4 Hot migration of disks

### 4.1 Overview

Hot migration seeks to facilitate operations and maintenance of online clusters and improve service operation. Hot migration provides online migration capabilities for virtual disks. This function can also quickly copy data to new locations, enhancing the flexibility of services.

### 4.2 Limits

Before you perform hot migration on a disk, you must understand the limits that apply.

**Limits**

Only disks of the river type support hot migration. The source and destination clusters for a hot migration task must belong to the same Object Storage Service (OSS) domain. Hot migration is not supported by shared disks. Hot migration is not supported by disks that are larger than 2 TB in size. Format and capacity changes are not supported. Hot migration can be performed to migrate a disk only within the same zone. Hot migration is implemented internally. The names of the source and destination clusters must be less than 15 bytes in length. Migration cannot be rolled back.

> **Important:** Snapshots must be created to back up disk data before hot migration is performed on disks.
> When hot migration is complete, data exists on both the source and destination disks. You can use the pu tool to delete data from the source disk only after you confirm that data is complete and accessible on the destination disk. Job recycling is unavailable.

**API operations**

For more information about the API operations related to disk hot migration, see **Disk hot**
**migration** in **ECS Developer Guide**.

> **Note:** When a disk is being migrated, an I/O latency of less than 1 second is considered to be normal.
> Migration consumes network bandwidth. You must take measures to limit the number of concurrent migration tasks.

### 4.3 O&M after hot migration

The original source disk data remains on the source disk after hot migration and data backup operations are completed. To release disk space, delete the data from the source disk. After the data is deleted from the source disk, the space will be released at a later time.
1. On the compute cluster AG, run the `go2houyiregiondbrnd -e 'select task_id from`
`device_migrate_log where status="complete"'` command to obtain task: allTaskIds.
2. On the compute cluster AG, run the `go2riverdbrnd -e 'select`

```
task_id,src_pangu_path,dst_pangu_path from migration_log where task_id in ($allTaskIds) and status=2 and src_recycled=0 and DATE(gmt_finish) < DATE_ADD(CURDATE(), INTERVAL -1
```

`DAY)'` command.
3. Perform the following operations for each set of
<task_id,src_pangu_path,dst_pangu_path>:

```
i. Run the /apsara/deploy/bsutil rlm --dir=$dst_pangu_path|grep 'not-loaded'|wc -l
```

command on the host that runs the bstools role in the storage cluster. If the command output is not 0, proceed to the next step. ii. Run the /apsara/deploy/bsutil delete-image --dir=$src_pangu_path command on the host that runs the bstools role in the storage cluster. iii. Run the /apsara/river/river_admin migrate recycle $task_id command on the host that runs the river role in the storage cluster.

## 5 Upgrade solution

### 5.1 Overview

For both hot and cold migration of GPU and FPGA clusters, you must understand the limitations that apply to cluster upgrades.

### 5.2 Limits on GPU clusters

Before you upgrade a GPU cluster, familiarize yourself with the limits. The upgrade of GPU clusters in Apsara Stack is subject to the following limits: GPU clusters are supported only in Apsara Stack 3.3 and later. Elastic Compute Service (ECS) instances (VMs) that use GPUs, FPGAs, or other passthrough or SR-IOV devices do not support hot migration. The GN5I, GN5E, and GN4 type GPU clusters do not involve local disks and support only offline cold migration. If you perform a forced cold migration on GN5 and GA1 type GPU clusters that involve local disks, the local disks are reformatted and the data that is stored on the disks is lost. Before you migrate the clusters, you must back up your data.

### 5.3 Limits on FPGA clusters

Before upgrading an FPGA cluster, you must understand the limits. The upgrade of FPGA clusters in Apsara Stack are subject to the following limits: FPGA clusters are only supported in Apsara Stack 3.5 or later versions. VMs in an FPGA cluster must be shut down before the cluster can be upgraded. The FPGA service relies on Redis to a great extent. If the Redis service is interrupted during the hot upgrade of Apsara Stack, the FPGA service will be interrupted. The FPGA service will recover after the Redis service is restored. However, if a Redis instance fails to be created, you must restart the FPGA service after the Redis service is restored.

## 6 Handle routine alarms

### 6.1 Overview

This topic describes metrics and how to handle alerts. The metrics that are monitored in Elastic Compute Service (ECS) can be categorized into the following types: Basic metrics: These metrics are used to monitor the CPUs, memory, and service processes of physical machines. Connectivity metrics: These metrics are used to monitor the connectivity between different components and the connectivity between different networks. Service metrics: These metrics are used to monitor services, such as the status of various API requests. Table 1. Metrics

| Metric type | Function | How to handle alerts |
|---|---|---|
| Basic metrics | Monitor the basic performance such as CPU utilization and memory usage of physical machines and the availability of services, such as processes, that run on physical machines. | If an alert is generated indicating high CPU utilization, identify which process causes high CPU utilization. If the process considered critical, determine whether to restart the process. |
|   |   | If an alert is generated indicating high memory usage for a critical service, dump the memory data, contact Alibaba Cloud backend engineers to analyze the data, and then restart the application. |
| Connec tivity metrics | Check the connectivity between modules. | First, check the health status of modules. For example, check whether the host, services, ports, and domain names work as expected. If two modules that are connected are healthy, check the network connectivity between the modules. |
| Service metrics | Monitor critical calls. For example, check the latency of API requests, total number of API requests, and number of failed API requests, and identify database SQL exceptions. | If an API request failed, check the corresponding logs to identify the cause of the failure. If a database SQL exception occurs, check whether the exception was caused by a database exception, such as a system breakdown or a large number of connections, or an application issue. If the database SQL exception is caused by an application issue, submit the error information to Alibaba Cloud backend engineers for troubleshooting. |

### 6.2 API proxy

This topic describes the metrics of API proxy. Table 1. Metric description

| Metric | Alert item | Description |
|---|---|---|
| check apiproxy dns _ _ | Database HA switchover occurs or not | Checks whether Server Controller database switchover occurs. If so, nginx will be reloaded automatically. |
| check apiproxy con _ _ n new _ | check apiproxy conn ne _ _ _ w | Checks the connectivity to the Server Controller database. |
|   |   | Checks the connectivity to the API Server: Checks whether the API Server is down. Checks the network connectivity. |
| check apiproxy pro _ _ c new _ | check apiproxy proc ne _ _ _ w | Checks the memory usage and CPU utilization for nginx and memcache processes. |

### 6.3 API Server

The topic describes the monitoring metrics of the API Server. Table 1. Monitoring metrics

| Metric | Alert | Solution |
|---|---|---|
| check API _ Server proc new _ _ | The process does not exist or is abnormal. | Check whether the Java process exists and the CPU utilization and memory usage of the process. |
| check API _ Server conn new _ _ | Check the connectivity between the API Server and the Server Controller database. | Check whether the required components are down. If a component is down, perform the required O&M operations to resolve the issue. If the database is down, contact the database administrator (DBA). Check whether the VIP of the component is reachable. If not, contact Alibaba Cloud network engineers. |
|   | Check the connectivity between the API Server and TAIR. |   |
|   | Check the connectivity between the API Server and RegionMaster. |   |
|   | Check the connectivity between the API Server and RMS. |   |
| check API _ Server perf _ | Check the metrics of API requests, such as the latency, total number of API requests, and number of failed API requests. | This metric is used to identify faults. |
| check API _ Server errorlog _ | Check for database exceptions and instance creation failures. | If an exception occurs on a database, contact the DBA to check whether the database works as expected. If an instance fails to be created, identify the cause of the failure. |

### 6.4 RegionMaster

This topic describes the metrics of RegionMaster. Table 1. Metric description

| Metric | Alert item | Description |
|---|---|---|
| check regionmaster proc _ _ | The process does not exist or is abnormal. | Checks the state of the Java process: whether the process exists, and the CPU utilization and memory usage. |
| check regionmaster work _ _ | rms connectivity _ | Checks the connectivity to RMS. |
|   | regiondb connectivity _ | Checks the connectivity to the houyiregiondb database. |
|   | houyi connectivity _ | Checks the connectivity to the Server Controller database. |
|   | tair connectivity _ | Checks the connectivity to TAIR. |
| check zookeeper work _ _ | status | Checks the operating state of the Zookeeper process on the Server Controller. |
| check regionmaster errorlo _ _ g | errorlog for db _ _ | Checks whether the SQL statements are properly executed. |
|   | check regionmaster errorlog _ _ |   |
| check workflow master _ _ | Checks the operating state of the master in the workflow process. | - |
| check workflow worker _ _ | Checks the operating state of the worker in the workflow process. | - |

### 6.5 PYNC

This topic describes the metrics that are monitored for PYNC. Table 1. Metric description

| Metric | Alert item | Description |
|---|---|---|
| check vm start f _ _ _ ailed | Checks the causes of a VM startup fault. | You do not need to handle it immediately. It is typically caused by custom images. |
| check pync | Checks the CPU utilization and memory usage of PYNC. | - |
|   | PYNC has too many open file handles. | - |
|   | PYNC process count. | PYNC must have four processes. |

| Operations and Main e·Handle routine al |   |   |
|---|---|---|
| check pync _ |   |   |
|   | It has been long since pyncVmMonitor.LOG was last updated at ${pync monitor log last updated}. _ _ _ _ | Checks for reasons why a log has not updated for a long period of time, such as: Whether a PYNC process has encountered a problem. Whether the NC is running a key process called Uninterruptible Sleep. |

### 6.6 AGs

This topic describes the metrics of Admin Gateways (AGs). Table 1. Metrics

| Metric | Alert item | Description |
|---|---|---|
| disk usage _ | apsara 90 _ | /apsara disk usage. |
|   | homeadmin 90 _ | Usage of /home/admin. |
| check system ag _ _ | mem 85 _ | Memory usage. |
|   | cpu 98 _ | CPU utilization. |
|   | df 98 _ | Disk usage of the root directory. |
| check ag disk usage _ _ _ | check ag disk usage _ _ _ | Disk usage. |
| check nc down new _ _ _ | check recover failed _ _ | Checks the causes of an Elastic Compute Service (ECS) instance (VM) migration fault. Possible causes include: No resources are available in the cluster. A VM does not belong to any cluster. |
|   | check repeat recovered _ _ | Continuous VM migration. |
|   | check continuous nc down _ _ _ | Checks continuous NC downtime. |
|   | check nc down with vm _ _ _ _ | The state of the computing server (NC) in the database is nc down, but _ specific VMs operate as expected on the NC. Checks the NC for hardware faults: If a hardware fault occurs, you must perform O&M to resolve the fault. If no hardware fault is detected, restore the NC and change its state to locked. |

| check ag fhtd new _ _ _ | Checks whether the FHT tool works as expected. You can use the tool to migrate instances during failures and handle instance hangs. | If the tool does not exist, download the tool. In most cases, you can use the tool to migrate local disks. |
|---|---|---|

### 6.7 Server groups

This topic describes the metrics that are monitored for server groups. Table 1. Metric description

| Metric | Alert item | Description |
|---|---|---|
| check pync _ | pync mem _ | Monitors the memory usage of PYNC. |
|   | pync cpu _ | Monitors the CPU utilization of PYNC. |
|   | pync nofile _ | Monitors the number of PYNC handles. |
|   | pync nproc _ | Monitors the number of PYNC processes. |
|   | pync monitor log not updated _ _ _ _ | Monitors the status of PYNC scheduled tasks. |

## 7 Inspection

### 7.1 Overview

ECS inspection includes cluster basic health inspection and cluster resources inspection.

### 7.2 Cluster basic health inspection

## inspection

#### 7.2.1 Overview

Cluster basic health inspection includes monitoring inspection, inspection of basic software package versions, and basic public resources inspection.

#### 7.2.2 Monitoring inspection

This topic describes basic monitoring inspections and connectivity monitoring inspections.

#### 7.2.3 Inspection of basic software package versions

**versions**

This topic describes the version inspections of Server Controller components, Apsara system, virtualization packages, and basic service packages.

#### 7.2.4 Inspections of basic public resources

This topic describes ISO inspections and base image inspections.

**ISO inspection**

Elastic Compute Service (ECS) provides the following basic ISO files per region: linux-virt-release-xxxx.iso windows-virt-release-xxxx.iso You can run the following command to search the database for relevant information:

```
houyiregiondb select name,os_type,version,path,oss_info from iso_resource where os_type!=''\G
```

In the preceding command, take note of the following parameters: name: the name of the ISO file, such as xxxx.iso. os_type: the image type of the ISO file. path: the path on the Apsara Distributed File System cloud disk in which the ISO file is stored. You can run the /apsara/deploy/pu meta $path command to check whether the ISO file is stored in Apsara Distributed File System. oss_info: the path on the OSS local disk in which the ISO file is stored. To search for the path, provide relevant information to OSS support engineers.

**Base image inspection**

Run the following command to check the status of a base image in the database:

```
houyiregiondb select image_no,status,visibility,platform, region_no from image;
```

Check whether the base image works as expected. You can call the create_instance operation to create virtual machines (VMs) from the base image, and check whether the VMs run as expected.

### 7.3 Cluster resource inspection

#### 7.3.1 Overview

Cluster resource inspection includes cluster inventory inspection and VM inspection.

#### 7.3.2 Cluster inventory inspection

This topic describes the inspections of available cluster resources. The available resources of a cluster are measured by the number of virtual machines (VMs) that can be created from the resources. You can query the database that is installed in a cluster for the resources available in the cluster. For example, to query the available resources of a cluster that can be used to create VMs that each have 16 vCPUs and 64 GB of memory, run the following command:

```
houyiregiondb select sum( least ( floor(available_cpu/16),floor(available_memory/64/1024))) from nc_r esource,nc where nc.cluster_id=$id and nc.biz_status='free' and nc.id=nc_resource.id;
```

If the cluster contains large VMs, make sure that a sufficient number of unoccupied physical machines that have sufficient resources are available in the cluster. This allows you to migrate the VMs to the physical machines when the physical machines that host the VMs become unavailable. If limited or no physical machines that have sufficient resources are available in the cluster, large VMs cannot be migrated to other physical machines when the physical machines that host the VMs become unavailable. If this issue occurs, you must perform hot migrations to free up resources or release redundant VMs in the cluster.

**NC status inspection**

NC status inspection checks whether the status of a physical machine, also known as an NC, is normal in the database and the Apsara Infrastructure Management console. A physical machine can be in one of the following states in the Apsara Infrastructure Management console: Good: The physical machine works as expected. Error: The physical machine has an active alert. Probation: The physical machine is under observation and may fail. OS _error: The physical machine failed and is being cloned. Hw_error: The hardware of the physical machine failed and is being repaired. OS _probation: The physical machine is recovering from a fault or hardware failure and is under observation. If the physical machine passes the observation, the physical machine enters the Probation state. If an error is reported during the observation period, the physical machine fails the observation and enters the OS_error state.

> **Note:** Good is considered a stable state, whereas all other states are considered unstable states.

Physical machines can belong to the following types of cluster in the Apsara Infrastructure Management console: Default cluster: the cluster in which NCs are placed when they go offline. Non-default cluster: the cluster for online NCs. An NC that works as expected is placed in a non-default cluster, and is in the Good state. Table 1 describes the mappings between the status of physical machines in the Elastic Compute Service (ECS) database and in the Apsara Infrastructure Management console. Table 1. Table 1

| Status of a physical machine in the ECS database | Cluster | Status of a physical machine | Scenario |
|---|---|---|---|
| mlock | Non-default cluster | Unstable | The physical machine that goes online is proactively locked. |
| locked | Non-default cluster | Unstable | The physical machine is unlocked. |
| free | Non-default cluster | Stable | The physical machine works as expected. |
| nc down _ | Non-default cluster | Unstable | The physical machine works as expected or is down. |
| offline | Default cluster | Unstable | The physical machine goes offline. |

#### 7.3.3 VM inspection

This topic describes pending VM inspections, VM state inspections, and VM resource inspections.

**Pending VM inspection**

This type of inspection focuses on VMs that have been in the pending state for a long period of time. When a VM has been in the pending state for a long period of time, it is considered a redundant resource. Contact the user to handle it.

**VM state inspection**

This type of inspection focuses on the VM state consistency. For example, a VM is displayed as stopped in the database, but is displayed as running in NC. During the inspection, the VM states recorded in the database and on the host are checked. If the VM states are inconsistent, corresponding operations are performed. Run the following command to obtain the VM state in a database:

```
houyiregiondb –Ne “select status from vm where name=’$name’”
```

Run the following command to obtain the VM state on a host:

```python
sudo virsh list | grep $name
```

**VM resource inspection**

After the configuration of a VM is changed, the system checks whether the configuration of the VM recorded in the database is consistent with that used on the host. Run the following command to obtain the VM configuration in a database:

```
houyiregiondb –Ne “select vcpu, memory from vm where name=’$name’”
```

Run the following command to obtain the VM configuration on a host:

```python
sudo virsh list | grep $name
```

Obtain information about CPU and memory by viewing the corresponding fields.

### 7.4 What do I do if a split-brain issue occurs in the data centers in which ECS is deployed in disaster recovery mode?

**issue occurs in the data centers in**

**which ECS is deployed in disaster**

**recovery mode?**

For data centers, split-brain is a state in which a severe failure occurs on the physical network. A split-brain issue may cause exceptions in Elastic Compute Service (ECS). This topic describes the impacts of a split-brain issue in data centers on ECS and how to resolve the issue.

**Background information**

The ECS in two data centers works in primary-secondary disaster recovery mode. The data centers reside in different zones. Management nodes, compute nodes, and storage nodes are deployed in each data center. When the physical network between the two data centers is disconnected because of network device exceptions or other reasons, a split-brain issue occurs in the data centers.

**Impacts**

The data center in which the primary management database of ECS resides is the primary data center. The data center in which the secondary management database of ECS resides is the secondary data center. The split-brain issue may have the following impacts: Impacts on the operation of VMs The operation of VMs in the primary and secondary data centers is not affected. However, whether the VMs can provide services externally depends on the scope of the network failure. Impacts on the management of VMs Due to the split-brain issue, the primary data center cannot be connected to the secondary data center. If the network does not recover within 1 minute after the failure occurs, the instances in the secondary data center may be stopped. During the period of time when the split-brain issue occurs, unexpected errors occur when write operations (start, migrate, stop, and release operations) are performed on all instances in the secondary data center. Wait until the network recovers before you perform write operations on the instances. Theoretically, the status and operation of instances in the primary data center are not affected. Impacts on failover events During the period of time when the split-brain issue occurs, the primary and secondary data centers cannot be connected to each other, and the instances and NCs in the secondary data center cannot report heartbeats to those in the primary data center. As a result, specific instances generate false-posive events, which trigger failover tasks. A split-brain issue in data centers triggers throttling on failover tasks. If the number of failover tasks in a cluster within 1 hour exceeds the throttling threshold, the failover tasks are throttled to reduce false positives. The following scenarios occur for the failover tasks that are not throttled:
1. During the period of time when the split-brain issue occurs, unthrottled failover tasks
cannot be completed. In this case, the failover tasks are repeatedly run until the vpc vport is migrated.
2. After the split-brain issue is resolved, network migration tasks are immediately completed
and failover tasks continue to run to start VMs on other NCs.
3. In this case, whether the failover tasks can be completed varies based on whether the
original VMs in the secondary data center are still running. If the original VMs in the secondary data center are still running, the failover tasks fail and the operation of the VMs is not affected. If the original VMs in the secondary data center encounter other faults, such as physical machine downtime, in-data center network downtime, and VM shutdown, the failover tasks can be completed. The instances are restarted and recover.

**Solution**

After the data centers recover from the split-brain issue and are connected to each other, the status of the VMs and NCs in the data centers is restored as follows: VMs: The status of the VMs on the ECS management side is restored in a full heartbeat cycle, which is expected to be 15 to 30 minutes. NCs: During the period of time when the split-brain issue occurs, specific NCs are in the
**ncDown** state. You must call Server Controller APIs to restore the NCs.
