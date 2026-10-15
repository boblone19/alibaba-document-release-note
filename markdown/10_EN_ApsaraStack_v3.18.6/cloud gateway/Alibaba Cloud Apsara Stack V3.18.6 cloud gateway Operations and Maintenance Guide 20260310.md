---
title: "cloud gateway Operations and Maintenance Guide"
product_version: "V3.18.6"
doc_version: "20260310"
pdf_pages: 132
source_pdf: "6d0f62f9ad12628c_Alibaba Cloud Apsara Stack V3.18.6 cloud gateway Operations and Maintenance Guide 20260310.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/v3.18.6%E7%89%88%E6%9C%AC%E6%96%87%E6%A1%A3/%E4%BA%91%E6%8E%A5%E5%85%A5%E7%BD%91%E5%85%B3%20/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.6%20cloud%20gateway%20Operations%20and%20Maintenance%20Guide%2020260310.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings)
---

# cloud gateway Operations and Maintenance Guide

## Table of Contents

- 1 Log on to the Apsara Uni-manager Operations Console
- 2 Basic network
  - 2.1 HPN management
    - 2.1.1 HPN network elements
    - 2.1.2 RDMA network interface O&M
    - 2.1.3 HPN performance analysis
    - 2.1.4 HPN instant diagnostics
  - 2.2 CPN
    - 2.2.1 CPN diagnosis
    - 2.2.2 CPN performance analysis
    - 2.2.3 CPN alert center
    - 2.2.4 CPN access gateways
      - 2.2.4.1 Manage RDMA devices
      - 2.2.4.2 Manage RDMA device policies
      - 2.2.4.3 Manage policies for the RDMA device interface
    - 2.2.5 RDMA NIC O&M
    - 2.2.6 CPN management
      - 2.2.6.1 CPN topology
      - 2.2.6.2 CPN network element
    - 2.2.7 CPN network monitoring
      - 2.2.7.1 CPN host monitoring dashboard
      - 2.2.7.2 CPN switch dashboard
      - 2.2.7.3 NAK packet analysis tool
      - 2.2.7.4 High-precision monitoring dashboard
      - 2.2.7.5 High-precision vSwitch monitoring dashboard
      - 2.2.7.6 Job monitoring
      - 2.2.7.7 CPN stream monitoring
  - 2.3 CGW
  - 2.4 Computing access gateways
- 3 Networking products
  - 3.1 CGW O&M
    - 3.1.1 CGW cluster management
    - 3.1.2 CGW management
- 4 Traffic visualization
  - 4.1 Visual settings

ager Operations Console

## 1 Log on to the Apsara Uni-manager Operations Console

**manager Operations Console**

This topic describes how users such as O&M engineers log on to the Apsara Uni-manager

**Prerequisites**

The endpoint of the Apsara Uni-manager Operations Console and the username and password that are used to log on to the console are obtained from a deployment engineer or an administrator. The endpoint of the Apsara Uni-manager Operations Console is in the following format: regi on-id.ops.console.intranet-domain-id. A web browser is available. We recommend that you use Google Chrome.

**Procedure**

1. Open your browser.
2. In the address bar, enter the endpoint of the Apsara Uni-manager Operations Console.
Press the ENTER key. You can click the current language in the upper-right corner to switch to another language. Simplified Chinese, English, and traditional Chinese are supported.
3. Enter the username and password.
ager Operations Console Obtain the username and password that are used to log on to the Apsara Unimanager Operations Console from a deployment engineer or an administrator. If you enter an invalid password for three consecutive times, the system enables the image verification logon feature. If you enter an invalid password for five consecutive times, the account is locked. Contact the administrator to activate the account. If this is the first time you log on to the Apsara Uni-manager Operations Console, you must change the password as prompted. To enhance security, your password must meet the following requirements: The password contains uppercase and lowercase letters. The password contains digits. The password contains at least one of the following special characters: ! @ # $ % The password is 10 to 20 characters in length.
4. Click **Log In**.

## 2 Basic network

### 2.1 HPN management

By default, the HPN Management module is not displayed. To use this module, perform the following operations: Log on to the Apsara Uni-manager Operations Console. In the top navigation bar, choose More > **User Authorities**. In the left-side navigation pane, click **Menu Management**. On the Menu management page, modify the menu settings to display the HPN Management module.

#### 2.1.1 HPN network elements

This topic describes how to view High Performance Network (HPN) network device assets and monitoring and O&M information in the Apsara Uni-manager Operations Console.

**Procedure**

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
Deleted network elements cannot be restored. Proceed with caution.

#### 2.1.2 RDMA network interface O&M

The remote direct memory access (RDMA) network interface O&M feature can regularly check the performance metrics of an RDMA network interface by using performance monitoring. This helps you identify issues at the earliest opportunity, quickly troubleshoot and resolve issues, and ensure network stability and reliability.

**Terms**

**RDMA** is a high-speed network technology used to resolve delays in server-side data
processing during network transmission. RDMA directly sends data to the storage area of a computer over the network. During the process, data is quickly transmitted from one system to the memory of a remote system. RDMA implements direct memory access between hosts without affecting the operating system, accelerates data transmission, and reduces CPU load.

**Procedure**

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

If you select **PAI**, you must configure the **Cluster** and **ViewType** parameters. If you select **CPFS** or **SCC**, you must configure the **Cluster** parameter.
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

#### 2.1.3 HPN performance analysis

The Apsara Uni-manager Operations Console provides the High Performance Network (HPN) performance analysis feature. This feature analyzes the maximum load and pressure resistance of the software and hardware by testing the performance of a machine under stress conditions. This helps you identify the pressure resistance limit of the machine and provides data support for O&M personnal to improve network performance.

**Procedure**

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

#### 2.1.4 HPN instant diagnostics

High Performance Network (HPN) instant diagnostics refer to a diagnosis on HPN nodes. During the diagnosis, the system software, network, and GPU of nodes are checked. After the diagnosis, the diagnostic results and details are provided to help administrators troubleshoot network performance issues.

**Procedure**

1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
3. In the left-side navigation pane, choose **Basic Network** > **HPN Management** > **HPN**
**Instant Diagnostics**.
4. On the HPN instant diagnosis page, select a test cluster and one or more nodes from the
drop-down lists and then click **Diagnosis**. You can select multiple nodes at a time.
5. View the diagnostic results.

| Diagnostic result | Description |
|---|---|
| Diagnostic Item | Displays the diagnostic items, including OS Release Version, OS Kernel Version, Server CPU Model, Server Disk Space, RDMA NIC Drive Installation, RDMA NIC Drive Load, bonding Module Installation, GDR Module Installation, GDR Module Load, Number of RDMA Devices, RDMA Device Firmware Version, RDMA Device Aggregation Mode, RDMA Device Aggregation Status, RDMA Device Hash Policy, RDMA Device Port Rate, RDMA Device MTU Settings, PCIe MRR Configuration, PCIe Link Details, PCIe Link Rate, PCIe Link Width, and GPU Online Check. |
| Diagnostic Result | Displays the diagnostic result of each diagnostic item. The result can beP assed or Failed. |
| Diagnostic Details | Displays the diagnostic details of each diagnostic item. For example, the RDMA device port rates are consistent. |
| Current Value | Displays the diagnostic value corresponding to each diagnostic item. |

### 2.2 CPN

#### 2.2.1 CPN diagnosis

The Computing Platform Network (CPN) diagnosis feature checks the nodes in CPN and displays information such as the diagnostic items, diagnostic details, and diagnostic results to help administrators better understand and manage network performance and troubleshoot issues.

**Procedure**

1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
3. In the left-side navigation pane, choose **Basic Network > CPN Management > CPN**
**Diagnostics**.
4. On the CPN Quick Diagnostics page, click **Create Diagnostics Task**.
In the Create Diagnostics Task dialog box, configure the parameters that are described in the following table.

| Parameter | Description |
|---|---|
| Task Name | The name of the diagnostic task. |
| Resource Pool | Default value: No. This indicates the Elastic Compute Service (ECS) Bare Metal Instances that are not added to compute clusters. |
| Cluster | The cluster on which the diagnostic task is performed. |
| Group | The hosts within the cluster that are grouped based on the CIDR block of the connected vSwitch. Each group can contain up to 100 hosts. |
| Diagnostics node | The node on which the diagnostic task is performed. |

You can select multiple nodes.
5. Click **OK**. The diagnostic task starts running immediately.

**View diagnostic results**

1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
3. In the left-side navigation pane, choose **Basic Network > CPN Management > CPN**
**Diagnostics**.
4. On the CPN Quick Diagnostics page, find the diagnostic task that you want to manage and
click **Details** in the **Operation** column.

| Tab | Description |
|---|---|
| Diagnostics Result | Displays the diagnostic results of the nodes on which the diagnostic task is performed. |
| Overview view | Displays the cluster, the total number of instances, the number of normal items, and the number of abnormal items. |
| Detailed View | Displays the diagnostic details by node or diagnostic item. |

5. Click the **Diagnostics Result** tab. On the Diagnostics Result tab, click **Details** in the
Actions column of an abnormal diagnostic result. In the **Abnormal Diagnostic Details** panel, view the detailed information. Click **Details** in the Actions column of a diagnostic item. In the **Abnormal Diagnostic Result Details** dialog box, view the detailed information.
6. Click the **Overview View** tab to view the cluster, IP addresses, the total number of
instances, the number of normal items, and the number of abnormal items.
7. Click the **Detailed View** tab to query diagnostic details by **node** or **diagnostic item**. You
can view information such as the diagnostic results, diagnostic details, and error messages.

**What to do next**

The following table describes the operations that you can perform on the **CPN Quick**
**Diagnostics** page.

| Operation | Procedure |
|---|---|
| Filter diagnostic tasks | Basic filter i. Select Start and End Time or Status from the drop-down list. ii. Select a time range or state. The tasks that meet the filter condition are displayed. Advanced filter i. Click Advanced Filter. ii. Configure the Start and End Time and Status parameters and click Search. |
| Retry a diagnostic task | 1. Find the diagnostic task that you want to manage and clickR etry in the Operation column. 2. In the message that appears, click OK. |
| Delete a diagnostic task | 1. Find the diagnostic task that you want to manage and clickD elete in the Operation column. 2. In the message that appears, click OK. |

#### 2.2.2 CPN performance analysis

You can perform a Computing Platform Network (CPN) performance analysis task to test the performance of machines under stress conditions. The task analyzes the maximum load and pressure resistance of the existing software and hardware. This helps identify the pressure limits of the machines and provides sufficient data for the O&M team to improve network performance.

**Procedure**

1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
3. In the left-side navigation pane, choose **Basic Network > CPN Management > CPN**
**Performance Analysis**.
4. On the CPN Performance Analysis page, click **Create Test**. On the Create Analysis Task
page, create an analysis task. The following table describes the parameter combinations of an analysis task for which the Protocol Type parameter is set to RDMA.

| Test cluster | Protoc ol Type | Test type | Required parameter | Traffic model value | Node |
|---|---|---|---|---|---|
| Arbitrary | RDMA | Traffic test | Number of QPS tested Node Port Test duration (s) GDR | MtoN | Server Client |
|   |   |   |   | FullMesh | Server |
|   |   |   |   | Ring | Server |
|   |   | Latency Test | Node Port Test duration (s) | N/A | Server |

The following table describes the parameters you must configure to create an analysis task for which the Protocol Type parameter is set to RDMA.

| Parameter | Description |
|---|---|

| Number of QPS tested | The number of test processes. This parameter determines the test bandwidth. If the queue pairs (QPs) are insufficient, the communication queue in the RDMA network may be congested, which compromises the efficiency and stability of data transmission. If the number of QPs is excessively large, the system overheads, complexity, and failure rate are increased. Note QP is a key term of the RDMA network. It refers to the communication queue between a pair of endpoints. |
|---|---|
| Node Port | The port number used for the test. |
| Test duration (s) | The duration of the test. Unit: seconds. |
| GDR | Specifies whether to enable direct communication between GPUs If you turn on this switch, the system associates the RDMA network interface controller (NIC) with the corresponding GPU for traffic testing. Make sure that the machine supports this feature before you turn on the switch. |
| MtoN | The many-to-many relationship model. This model is used to test the one-way connectivity between Client nodes and Server nodes, including the one-way connectivity between a single Client node and a single Server node and between multiple Client nodes and multiple Server nodes. |
| FullMesh | All nodes in the network topology are connected to each other. This option allows you to test the two-way connectivity between all destination nodes. |
| Ring | Multiple nodes in the network topology form a closed loop. Data packets are sent from one node to the next node in sequence and finally returned to the original node. This option allows you to test the actual available network bandwidth. |
| Client | The sender of the test traffic. |
| Server | The receiver of the test traffic. |

The following table describes the parameters you must configure to create an analysis task for which the Protocol Type parameter is set to Communication Library.

| Test clust er | Protocol Type | Test type | Communicati on Library | Required parameter |
|---|---|---|---|---|

| Arbitr ary | Commun ication Library | Communi cation library test | NCCL CPN-CCL RCCL PCCL |   |   | Algorithm: the algorithm of the task. The algorithm bandwidth, bus bandwidth, and execution time of a task vary based on the algorithm. Communication Primitive: The data transmission and processing methods vary based on the communication primitive. Select a value from the drop- down list. Timeout Period (Seconds): If the execution time of performance analysis test is greater than the specified timeout period plus 1 minute, the test task fails. Data Type: the data type of the performance analysis test. Select a value from the drop-down list. Iterations: the number of times the current task is executed. Minimum Bytes: the minimum amount of data to start the task. Maximum Bytes: the maximum amount of data to stop the task. Step Factor: Specify an integer greater than 1. If you set the parameter to 2, the data specification increases by two times. The first row corresponds to the value of the Start bytes parameter and the last row corresponds to the value of the Number of cut-off bytes parameter. Hosts: Click Select a node to add hosts. mpirun Custom Parameters: Specify custom parameters in the --mca ... - -mca ... format. Example: --mca |   |   |   |
|---|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   | --mca ... - |   |   |
|   |   |   |   |   |   | -mca ... |   |   |   |
|   |   |   |   |   |   |   |   | --mca |   |
|   |   |   |   |   |   | tcp,self --mca btl tcp if include _ _ _ |   |   |   |
|   |   |   |   |   |   | bond0 --mca oob tcp if include _ _ _ |   |   |   |
|   |   |   |   |   |   | bond0 --bind-to none |   |   |   |

5. Click **Submit**.

**What to do next**

The following table describes the operations that you can perform on the **CPN Performance**
**Analysis** page.

| Operation | Procedure |
|---|---|

| Query a test task | Basic filter After you specify the start time and end time, the test tasks that meet the filter condition are displayed. Advanced filter i. Click Advanced Filter. ii. Configure the Start and end time, Test Type, Protocol Type, and Status parameters. iii. Click Search. |
|---|---|
| View performance analysis details | 1. Find the test task that you want to manage and click Details in the Operation column. 2. On the Analysis Task Details page, view the basic information, analysis results, and device information of the task. |
| Export performance analysis details | Note You can export the performance analysis details of a test task of the traffic test or latency test type. 1. Find the test task that you want to manage and click Details in the Operation column. 2. On the Analysis Task Details page, click Export to the right of Analysis Results. 3. View the exported Excel file on your computer. |
| Retry a test task | 1. Find the test task that you want to manage and click Retry in the Operation column. 2. In the message that appears, click OK. The value in the Task Status column changes to Running. |
| Delete a test task | 1. Find the test task that you want to manage and click Delete in the Operation column. 2. In the message that appears, click OK. |
| Terminate a test task | 1. Find the test task that you want to manage and click Stop in the Operation column. 2. In the message that appears, click OK. The value in the Task Status column changes to Stopping. If the value in the Task Status column changes to Stopped, the task is terminated. |

#### 2.2.3 CPN alert center

The CPN Alarm Center module displays alerts, including real-time alerts that are not closed and closed historical alerts.

**Alert Distribution Overview**

1. Log in to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
3. In the left-side navigation pane, choose **Basic Network > CPN Management > CPN**
**Alarm Center**.
4. On the **CPN Alerts** page, click the **Alert Distribution Overview** tab to view the statistics
of various types of CPN alerts. By default, the statistics of **Not Closed** alerts are displayed. You can click **Closed** to view the statistics of closed alerts. You can set **Start and End Time** to filter and view the alerts in the specified time range. CPN alerts are classified into two types: **Client** and **Network**. Network-side alert types include **RASW**, **RDSW**, **EHSW**, **EDSW**, and **CHSW**. You can click **Details** in the **Actions** column to go to the list of alerts of a specified type or a specified alert item.

**Host Alert**

1. Log in to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
3. In the left-side navigation pane, choose **Basic Network > CPN Management > CPN**
**Alarm Center**.
4. On the **CPN Alerts** page, click the **Host Alert** tab to view real-time CPN alerts on the
**Client** side. By default, **Not Closed** alerts are displayed. You can click **Closed** to view the
closed alerts. You can click the up or down arrow next to **Alert Level** or **Last Alert Time/Duration** to sort alerts. The alert information includes **Alert Level**, **Alert Item ID**, **Resource Owner**, **Alert**
**Information**, **Alert Status**, **Alert Start Time**, **Last Alert Time/Duration**, **Alerts**,
**Alert Details**, and **Alert Object Name/ID**.
Click **Advanced Filter** and filter alerts by **Alert Item ID**, **Alert Start Time**, **Alert**
**Level**, **Alert Object Name**, or any combination of them.
Click an alert item ID in the **Alert Item ID** column to go to the **Alert Details** page and view the details of the alert. For more information, see Alert details. Move the pointer over **Details** in the **Alert Details** column of an alert to view the details of the alert.

**Switch Alert**

1. Log in to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
3. In the left-side navigation pane, choose **Basic Network > CPN Management > CPN**
**Alarm Center**.
4. On the **CPN Alerts** page, click the **Switch Alert** tab to view real-time CPN alerts on the
**Network** side. By default, **Not Closed** alerts of the **RASW** type are displayed. You can
click **Closed** to view the closed alerts. You can also switch between tabs to view the real-time alerts of the **RASW**, **RDSW**, **EHSW**,
**EDSW**, and **CHSW** types on the Network side.
You can click the up or down arrow next to **Alert Level** or **Last Alert Time/Duration** to sort alerts. The alert information includes **Alert Level**, **Alert Item ID**, **Resource Owner**, **Alert**
**Information**, **Alert Status**, **Alert Start Time**, **Last Alert Time/Duration**, **Alerts**,
**Alert Details**, and **Alert Object Name/ID**.
Click **Advanced Filter** and filter alerts by **Alert Item ID**, **Alert Start Time**, **Alert**
**Level**, **Alert Object Name**, or any combination of them.
Click an alert item ID in the **Alert Item ID** column to go to the **Alert Details** page and view the details of the alert. For more information, see Alert details. Move the pointer over **Details** in the **Alert Details** column of an alert to view the details of the alert.

#### 2.2.4 CPN access gateways

##### 2.2.4.1 Manage RDMA devices

This topic describes how to manage Remote Direct Memory Access (RDMA) devices, including how to scan for and delete RDMA devices.

**Procedure**

1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
3. In the left-side navigation pane, choose **Basic Network > CPN Management > CPN**
**Access Gateway**.
4. Select the **RDMA Device Management** tab.
5. Manage RDMA devices.
Scan for new devices Click **Scan New Devices** to add new RDMA devices to the system. Query new devices Basic filter a. Select **Device Name**, **Equipment manufacturer**, **Equipment model**, **Device**
**role**, **Device Management IP**, **Serial Number**, or **Device status** from the drop-
down list. b. In the search box, enter the device name or manufacturer, or select the status of the device, and click . Advanced filter a. Click **Advanced Filter**. b. Enter the device name, device manufacturer, device model, device role, device management IP address, and serial number, and select the device status. c. Click **Search**. Delete a new device a. Click **Delete** in the **Actions** column. b. In the message that appears, click **OK**.

##### 2.2.4.2 Manage RDMA device policies

This topic describes how to configure policies for Remote Direct Memory Access (RDMA) devices to manage RDMA devices in a centralized manner.

**Procedure**

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

##### 2.2.4.3 Manage policies for the RDMA device interface

**interface**

This topic describes how to manage interface policies, such as policy configuration, query, and retry.

**Procedure**

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
|---|---|
| Device Role | Select the role of the device to which the policy applies from the drop-down list. Valid values: RASW: the access vSwitch of the data exchange module in Remote Direct Memory Access (RDMA) networking scenarios. RDSW: the core vSwitch of the data exchange module in RDMA networking scenarios. The core vSwitch is used to connect different access vSwitches. EHSW: the vSwitch that is used to connect to the custodian network in RDMA networking scenarios. |
| Device Model | Select the model of the device to which the policy applies from the drop-down list. The system automatically displays the device models on the RDMA Device Management tab. |
| Device List | Select the device to which the policy applies from the drop-down list. The system automatically displays the devices of a specific device model on the RDMA Device Management tab. |
| RoCE queue PFCs configuration (RDMA over Converged Ethernet) | Headroom cache threshold: the size of the RDMA over Converged Ethernet (RoCE) queue buffer, and the maximum number of available cell resources in the headroom. Back pressure frame trigger threshold: the analysis model of network traffic. The model ensures that the sum of the back pressure frame triggering thresholds for all ingresses is less than or equal to the tail-drops threshold for the egress. Offset between back pressure frame stop threshold and trigger threshold: When the number of cell resources used by packets with a 802.1p priority decreases by the value of this parameter after PFC is triggered, PFC stops sending PFC pause frames. PFCs reserved threshold: the number of cell resources reserved for packets with a 802.1p priority in the guaranteed storage capacity. PFCs: If you use PFC and congestion occurs in a specific type of traffic, the routing of other types of traffic is not affected. This ensures that different types of packets on the same link do not affect each other. Deadlock monitoring function: If a link or device failure occurs, temporary loops may occur during the route reconvergence period. In this case, PFC frames are repeatedly sent and received between devices, packets cannot be forwarded, cell resources in the interface buffer are occupied and cannot be released, and the device enters the PFC deadlock state. |
|   | ECN function: Explicit Congestion Notification (ECN) uses the DiffServ field in the IP header to mark the congestion status along the packet transmission path. An ECN-capable terminal can determine whether congestion occurs on the transmission path based on the packet content. If congestion occurs, the terminal adjusts the method to send packets to prevent congestion from being aggravated. Lower limit of average queue length: the lower limit of the length of the queue that the packets of the forwarding device enter in the egress. The lower limit is also called ECN threshold. |

| ud gateway | Operations and Maintenance Gu de·Basic networ |
|---|---|
| RoCE queue WRED configuration | Upper limit of average queue length: When the device assigns packets to a queue in the outbound direction, the queue size reaches the upper threshold (ECN threshold). Discarding probability: the marking probability if ECN is used. A larger value indicates that more packets are marked between the upper and lower limits. Note If the length of the queue that the packets of the forwarding device enter in the egress is smaller than the lower limit, the forwarding device directly forwards the packets from the egress without processing the packets. When the device assigns packets to a queue in the outbound direction, if the average queue size is between the lower threshold and the upper threshold, take note of the following items: If the value of the ECN field in the received packets is 00, the packets are sent out of an ECN-incapable terminal. In this case, the forwarding device determines whether to drop the packets based on the drop probability. If the value of the ECN field in the received packets is 01 or 10, the packets are sent out of an ECN-capable terminal. In this case, the forwarding devices change the value of the ECN field for some of these packets based on the drop probability and forward these packets. All incoming packets are not dropped. If the ECN field is 11 in a packet, the packet on the original device has experienced congestion along the transmission path. In this case, the device does not process the packet and directly forwards the packet out of the outgoing interface. When the device assigns packets to a queue in the outbound direction, if the average queue size exceeds the upper threshold, take note of the following items: If the ECN field is 00, the packets are sent out of an ECN- incapable terminal, the device drops the packets. If the value of the ECN field in the packet received by the device is 01 or 10, it indicates that the packet sender supports the ECN function. After the ECN field of the inbound packet is changed to 11, the packet continues to be forwarded, and all inbound packets are not discarded. If the ECN field is 11 in a packet, the packet on the original device has experienced congestion along the transmission path. In this case, the device does not process the packet and directly forwards the packet out of the outgoing interface. |
| Document Version: 2 | 0260310 3 |

6. Click **OK**.

**What to do next**

On the **RDMA device interface policy management** tab, you can perform the following operations:

| Operation | Procedure |
|---|---|
| Query the policy for an RDMA device interface | 1. Configure the Policy Name, Device Vendor, Device Model, Device Role, or Device Management IP parameter. 2. Enter the policy name, device vendor, device model, device role, or device management IP address in the search box and click the icon. |
| View the details of a policy of an RDMA device interface | 1. Click Details in the Actions column. 2. Click OK or Cancel. |
| Retry the policy for an RDMA device interface | 1. Click Retry in the Actions column. 2. In the message that appears, click OK. |

#### 2.2.5 RDMA NIC O&M

To perform O&M on Remote Direct Memory Access (RDMA) network interface cards (NICs), you must check the performance metrics of RDMA NICs. RDMA NIC O&M allows you to identify and troubleshoot issues and ensure network stability and reliability.

**Terms**

**RDMA**: RDMA is a high-speed network technology developed to reduce the delay of server-
side data processing in network transmission. RDMA transfers data directly into the memory of a computer over the RDMA network and enables direct memory access between hosts without affecting the operating system. This increases the data transfer speed and reduces the CPU load.

**Procedure**

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
|---|---|
| Monitoring Chart | i. Select the start time and the end time on the right side of the monitoring chart to view the monitoring data within the time range. ii. In the Throughput Dashboard section, view the RDMA TX BYTES and _ _ RDMA RX BYTES metrics. _ _ RDMA TX BYTES is the number of bytes sent in the RDMA network. _ _ RDMA RX BYTES is the number of bytes received in the RDMA _ _ network. |
|   | > Document Version: 2026031 |

|   | iii. In the Basic Data of RDMA Network section, view the following data in the specified time range: RDMA IGNORE CNP AVG: the average number of ignored _ _ _ Congestion Notification Packets (CNPs) in the RDMA network. Note |
|---|---|
| RDMA Network Overview | CNPs are packets used for network congestion control. When View the metrics of the nodes in the RDMA network, includingN odes, network congestion occurs, CNPs are sent to notify the sender to Outbound Throughput, Inbound Throughput, Network QP, CNP reduce the sending rate to avoid network congestion and packet Processed by Network, Out-of-order Data Packets, and Network loss. Buffer Overflow. |

**RDMA_TX_PFC_PAUSE_AVG**: the average number of Priority-based
6. On the **Node** tab, view the monitoring information of each node.
Flow Control (PFC) packets when data is sent in the RDMA network.
**RDMA_RX_PFC_PAUSE_AVG**: the average number of PFC packets
when data is received in the RDMA network.
**RDMA_OOB_AVG**: the average amount of out-of-band (OOB) data
processed in the RDMA network. OOB data is a special type of data transmitted in an RDMA network.
**RDMA_OOS_AVG**: the average amount of out-of-order (OOS) data
processed in the RDMA network. OOS data is a special type of data transmitted in an RDMA network. OOS data is generated when packet loss or latency occurs during transmission.
**RDMA_SENT_CNP_AVG**: the average number of CNPs sent in the
RDMA network.
**RDMA_MARKED_ECN_AVG**: the average number of marked Explicit

| Con Parameter RD in t | gestion Notification (ECN) packets in the RDMA network. Description MA HANDLE CNP AVG: the average number of CNPs processed _ _ _ he RDMA network. |
|---|---|
| RD QP in RDMA Network that | MA TX PFC TRANS AVG: the average number of PFC packets _ _ _ _ are enabled in the RDMA network. MA QP CNT AVG: the average number of QPs in the RDMA _ _ _ work. MA TX BYTES AVG: the average number of bytes of data sent in _ _ _ RDMA network. MADiRspXlaBysY tThEeS mAoVnGito: rtihneg advaetara ogfe a n nuomdbee. rF ofr bmyoteres ionff odramtaation, _ _ _ eivseede inth teh ed eRsDcrMipAt inoentsw oofr tkh.e cluster metrics. |
| RD net Abnormal Networks RD |   |
| the Throughput Sent by RDMA RD Network (Mbit/s) rec |   |
| Throughput Received by RDMA Network (Mbit/s) |   |
| Monitoring Chart |   |

#### 2.2.6 CPN management

##### 2.2.6.1 CPN topology

This topic describes how to query the topology information about clusters and nodes.

**Procedure**

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

##### 2.2.6.2 CPN network element

This topic describes how to view network devices and monitoring and O&M information in the cloud platform.

**Procedure**

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
|---|---|
| Aggregation Port Management | Displays the aggregated port information of the network element device. Click View in the Actions column to view the traffic of the port. |
| Alert | Displays the alert information of the network element device. |

**What to do next**

On the **CPN network element** page, you can also perform the following operations:

| Operation | Procedure |
|---|---|
| Delete a CPN network element | 1. Click Delete in the Actions column. 2. In the message that appears, click OK. |

#### 2.2.7 CPN network monitoring

##### 2.2.7.1 CPN host monitoring dashboard

You can use this feature to monitor the key metrics of remote direct memory access (RDMA) networks on the server side of the intelligent computing network. The metrics include bandwidth, packet loss rate, and traffic control.

**Procedure**

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

##### 2.2.7.2 CPN switch dashboard

You can use this feature to monitor the running status metrics of vSwitches. The metrics include bandwidth, packet loss, and traffic control.

**Procedure**

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

##### 2.2.7.3 NAK packet analysis tool

You can use this tool to collect NAK packets in real time. After the packets are aggregated and analyzed, a matrix diagram is generated to help you quickly identify abnormal nodes.

**Procedure**

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

##### 2.2.7.4 High-precision monitoring dashboard

The high-precision monitoring dashboard of Computing Platform Network (CPN) allows you to monitor traffic of network interface cards (NICs) and bond devices with a latency of seconds.

**Procedure**

1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
3. In the left-side navigation pane, choose **Basic Network > CPN Management > CPN**
**Network Dashboard > High Precision Monitoring Dashboard** .
4. In the upper part of the page, select a cluster from the **High Precision Monitoring**
**Clusters** drop-down list and one or more nodes from the **Node** drop-down list, and then
click Start High-precision Task.
5. In the dialog box that appears, configure the **Duration (s)** parameter. Valid values: 1 to
600. Default value: 300. Then, click **OK**.
6. In the upper-right corner of the page, specify the time range of the monitoring. Select a
start time and an end time, and then click **OK**.
7. In the upper-right corner of the page, click the Refresh icon or set the automatic refresh
interval to view the latest monitoring data. If one of the selected nodes is in the Running state, you cannot start the task again until the duration of the task elapses.

##### 2.2.7.5 High-precision vSwitch monitoring dashboard

**dashboard**

The high-precision vSwitch monitoring dashboard of Computing Platform Network (CPN) allows you to monitor traffic of vSwitches with a latency of seconds.

**Procedure**

1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
3. In the left-side navigation pane, choose **Basic Network > CPN Management > CPN**
**Network Dashboard > Switch High Precision Monitoring Dashboard** .
4. In the upper part of the High-precision vSwitch Monitoring page, configure the required
parameters and click **Start High-precision Task**. The following table describes the parameters.

| Parameter | Description |
|---|---|
| idc | The data center on which the high-precision monitoring task is performed. |
| vSwitch | The vSwitch on which the high-precision monitoring task is performed. |
| Port | The port that you want to monitor. |
| Queue | The number of queues configured for the specified port. Valid values: 0 to 7. |

5. In the dialog box that appears, configure the **Duration (s)** and **Task type** parameters.
Valid values of the Duration (s) parameter: 1 to 600. Default value of the Duration (s) parameter: 300. Then, click **OK**. The value of the Task type indicates the monitoring object of the task. The related data of the unselected monitoring object is not displayed on the High-precision vSwitch Monitoring page.
6. In the upper-right corner of the page, click the time range drop-down list. Then, select the
monitoring start time and end time from the drop-down list and click **OK**.
7. In the upper-right corner of the page, click the Refresh icon or set the automatic refresh
time to view the latest monitoring data. If one of the selected nodes is in the Running state, you cannot start the task again until the duration of the task elapses.

##### 2.2.7.6 Job monitoring

Computing Platform Network (CPN) provides the job monitoring feature, including the monitoring of top N metrics for hosts, end-to-end packet loss caused by congestion, and Remote Direct Memory Access (RDMA) packet loss of network interface cards (NICs).

**Prerequisites**

The related tasks are created in the task modeling module of AI Studio.

**Procedure**

1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
3. In the left-side navigation pane, choose **Basic Network > CPN Management > CPN**
**Network Dashboard > Job Monitoring**.
4. In the upper part of the **Job Monitoring** page, click **Expand more** and configure the **idc**,
**Cluster**, **JobType**, **TrainJobId**, **Tips**, **hostIps**, and **swNames** parameters.
5. After you configure these parameters, the corresponding monitoring data appears in the
lower part of the page. You can view the monitoring metrics in each panel. Click the icon to the left of each panel name to fold or unfold the panel.

##### 2.2.7.7 CPN stream monitoring

Computing Platform Network (CPN) supports the global traffic observability feature, including the visualization of communication relationships, communication paths, communication quality, and impacts of congestion.

**Prerequisites**

By default, the stream-based visualization feature of CPN is disabled. Before you use this feature, make sure that the cpn-lsgo database is enabled. Run the following code statement to enable the database:

```
update config_detail_info set config_value='on' where config_key in ('tracing_open','cpn_gtp','cpn_gto','cpn_gts','asnet-cpn-lsgo-agent');
```

After the database is enabled, you must restart the service.

**Procedure**

1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
3. In the left-side navigation pane, choose **Basic Network > CPN Management > CPN**
**Network Dashboard > CPN Flow Monitor**.
4. On the **Host** tab, view the traffic monitoring data by cluster.
Advanced Filter: In this section, configure the **Cluster Name**, **Management Port IP**
**Address of Source NC Filter based on the source IP addresses of the stream.**,
**Source NIC**, **Management Port IP Address of Destination NC Filter based on the**
**destination IP address of the stream.**, **Destination NIC**, and **Time** parameters to
filter and view data. View stream details: You can click **Details** in the **Actions** column to go to the stream details page and view information in the **Stream Change Events**, **Path Change**
**Events**, and **RTT Trend** sections.
5. On the **vSwitch** tab, view the traffic monitoring data by vSwitch.

|   | , |
|---|---|
| parameters to filter and view data. |   |

View stream details a. Click **Details** in the **Actions** column to view the streams loaded on a port. b. In the **Stream List** panel, click **Details** in the **Actions** column to go to the stream details page and view information in the **Stream Change Events**, **Path Change**
**Events**, and **RTT Trend** sections.

### 2.3 CGW

You can connect bare metal instances to a virtual private cloud (VPC) by using Central Gateway (CGW) to manage the bare metal instances in a centralized manner. CGW instances are dedicated hybrid switches (HSWs). The system supports operations such as instance management, operation log viewing, network management of bare metal instances, and O&M configurations to help you complete the daily O&M operations of CGW. By default, the CGW feature is not displayed. To use the feature, click **User Authorities** in the top navigation bar of the Apsara Uni-manager Operations Console. In the left-side navigation pane of the page that appears, click **Menu Management**. On the Menu management page, find Cloud Gateways and click Modify in the Actions column. In the Edit menu items panel, turn on **Show or not**.

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

**Important**

The iBGP role configurations must meet the following networking requirements: Single-data center deployment: At least one group of CGW instances whose iBGP role is an RR and other devices whose iBGP role is a client are deployed in a single data center. Multi-data center deployment: One group of CGW instances whose iBGP role is an RR and other devices whose iBGP role is a client are deployed in at least two data centers. RR role recommendations: We recommend that you set the role to Deploy Client and RR on a Device. If you have higher network stability requirements, we recommend that you set the role to Deploy RR on a Device.
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
| AK | The AccessKey ID and AccessKey secret of the organization, which can be obtained from the Organizations page of the Apsara Uni-manager Management Console based on the organization to which the VPC belongs. For more information, see Manage the AccessKey pairs of an organization in Apsara Uni-manager Management Console User Guide. |
| SK |   |
| Vswitch ID | The ID of the dedicated vSwitch to which the bare metal instance is connected. |

| Region ID | The ID of the region in which the environment resides. |
|---|---|
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
| VBR ID | The VBR ID of the Express Connect circuit created on the HSW by the VPC to which the bare metal instance belongs. |
| BD ID | The value of the hardware bridge-domain (BD) to which the bare metal instance is added. |
| Created At | The time when the bare metal network was created. |

| Bare Metal IP Address | The IP address of the bare metal instance. Click Manage in the Bare Metal IP Address column to assign an IP address to the bare metal instance. This helps you configure the network of bare metal instances. For more information, see the Manage the IP address of a bare metal instance section of this topic. |
|---|---|

3. Find the bare metal instance and click **Details** in the **Actions** column to view the details of
the bare metal instance, such as the ID of the Express Connect circuit, VPC router interface, and VBR interface.

**Disconnect a bare metal instance from a VPC**

After a bare metal instance is disconnected from a VPC, access isolation of resources can be implemented.

**Procedure**

Find the bare metal instance and click **Close the Connection to VPC** or **Delete Instance** in the Actions column. Click **Close the Connection to VPC** in the **Actions** column to disconnect the bare metal instance from the VPC. The Close the Connection to VPC option appears only after the bare metal instance is connected to a VPC. Click **Delete Instance** in the Actions column to disconnect the bare metal instance from the VPC and delete the bare metal instance. The Delete Instance option appears only for bare metal instances created on the Bare Metal Network Management page.

**Manage the IP address of a bare metal instance**

In the Bare Metal IP Address Management panel, you can assign an IP address to a bare metal instance. This helps you configure the network of bare metal instances.

**Background information**

CGW works with Bare-metal Management Service (BMS). BMS is used to install bare metal instances, assign IP addresses, and complete network configurations. CGW is used to connect bare metal instances to VPCs. In some scenarios, you may not install bare metal instances or complete network configurations by using BMS, but you must use CGW to connect bare metal instances to VPCs. In such scenarios, the system cannot assign IP addresses to bare metal instances, and you must manually maintain IP address assignment results. This may cause IP address conflicts and poor usability. Therefore, network management of bare metal instances is supported on the Cloud Gateway page. You can manage IP addresses of bare metal instances in the Bare Metal IP Address Management panel.

**Prerequisites**

A bare metal instance is connected to a VPC.

**Procedure**

1. Find the bare metal instance and click **Manage** in the **Bare Metal IP Address** column.
2. In the **Bare Metal IP Address Management** panel, click **Apply for Bare Metal IP**
**Address**.
3. In the **Apply for Bare Metal IP Address** dialog box, configure the **Bare Metal NIC**, **IP**,
and **IP Address Description** parameters and click **OK**. If you do not specify the IP parameter, an IP address is automatically generated.
4. After you apply for an IP address for a bare metal instance, view the IP address in the **Bare**
**Metal IP Address Management** panel.
Find the IP address of the bare metal instance and click **Edit** to change the IP address. Find the IP address of the bare metal instance and click **Release** to release the IP address.

**O&M configurations**

**Apply for a bare metal instance in a VPC**

In O&M emergency scenarios, you can use this feature to add the physical port of the CGW instance associated with a bare metal instance to the VPC.

**Warning**

This operation is only for emergency scenarios and must be performed under the guidance of R&D engineers. Otherwise, normal business operations may be affected. This feature can only be used to connect the bare metal instance to the CGW instance port but cannot be used to perform operations on the bare metal instance. To configure the network port, IP address, and routing information of the bare metal instance, contact the corresponding product team for guidance. Typically, you cannot use this feature to apply for a bare metal instance in the VPC. You can use the bare metal controller to call an API operation to enable the bare metal network.

**Procedure**

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
|---|---|
| Cloud Gateway Name | The name of the CGW instance to which the bare metal instance is connected. |
| Vswitch ID | The ID of the vSwitch to which the bare metal instance is to be added. You can obtain the vSwitch ID from the VPC console of the Apsara Uni-manager Management Console. |
| Port | The port of the CGW instance to which the bare metal instance is connected. |
| AK | The AccessKey ID and AccessKey secret of the organization, which can be obtained from the Organizations page of the Apsara Uni-manager Management Console based on the organization to which the VPC belongs. For more information, see Manage the AccessKey pairs of an organization in Apsara Uni-manager Management Console User Guide. |
| SK |   |
| Bare Metal Name | The name of the bare metal instance that you want to apply for. The name must be unique. |

If the specified values are invalid, click **Re-enter** in the lower part of the tab and configure the parameters again.
7. Click **Next**.
8. Check the information. If the information is correct, click **Confirm**.
After the configurations are delivered, the **Result: Successful** message appears, and you can search for the bare metal instance by bare metal instance name on the **Bare Metal**
**Network Management** tab. If the bare metal instance is displayed, it is connected to the
VPC.

**Release a bare metal instance in a VPC**

In O&M emergency scenarios, you can use this feature to disconnect the physical port of the CGW instance associated with a bare metal instance from the VPC.

**Warning**

This operation is only for emergency scenarios and must be performed under the guidance of R&D engineers. Otherwise, normal business operations may be affected. This feature can only be used to connect the bare metal instance to the CGW instance port but cannot be used to perform operations on the bare metal instance. To configure the network port, IP address, and routing information of the bare metal instance, contact the corresponding product team for guidance. Typically, you cannot use this feature to release a bare metal instance in the VPC. You can use the bare metal controller to call an API operation to delete the bare metal network.

**Procedure**

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

If the specified values are invalid, click **Re-enter** in the lower part of the tab and configure the parameters again.
7. Click **Next**.
8. Check the information. If the information is correct, click **Confirm**.
After the configurations are delivered, the **Result: Successful** message appears, and you can search for the bare metal instance by bare metal instance name on the **Bare Metal**
**Network Management** tab. If the bare metal instance is not displayed, it is released in
the VPC.

**Delete a route entry**

In O&M emergency scenarios, you can use this feature to delete route entries that point to the bare metal subnet in the VPC and the default route entries of a VBR.

**Warning**

This operation is only for emergency scenarios and must be performed under the guidance of R&D engineers. Otherwise, normal business operations may be affected. Typically, you cannot use this feature to delete a VPC route entry. This operation is only for emergency scenarios. You can perform this operation to delete only one route entry at a time. To delete multiple route entries, you must perform this operation multiple times.

**Procedure**

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
| Routing Destinatio n CIDR | The destination CIDR block to which the VPC points, which can be obtained from the VPC console. For more information about how to obtain a destination CIDR block, see VPC User Guide. | Set the value to 0.0.0.0/0. |

| AK | The AccessKey ID and AccessKey secret of the organization, which can be obtained from the Organizations page of the Apsara Uni-manager Management Console based on the organization to which the VPC belongs. For more information, see Manage the AccessKey pairs of an organization in Apsara Uni-manager Management Console User Guide. | The AccessKey ID and AccessKey secret of the organization, which can be obtained from the Organizations page of the Apsara Uni-manager Management Console based on the organization to which the VBR belongs. For more information, see Manage the AccessKey pairs of an organization in Apsara Uni-manager Management Console User Guide. |
|---|---|---|
| SK |   |   |

If the specified values are invalid, click **Re-enter** in the lower part of the tab and configure the parameters again.
7. Click **Next**.
8. Check the information. If the information is correct, click **Confirm**.
The system begins to deliver the configurations. After the configurations are delivered, the
**Result: Successful** message appears.
9. Optional. In actual fault scenarios, if multiple route entries exist in the route table, repeat
Step 5 to Step 8 to delete other route entries.

**Delete a router interface**

In O&M emergency scenarios, you can use this feature to delete a VPC router interface and a VBR interface.

**Warning**

This operation is only for emergency scenarios and must be performed under the guidance of R&D engineers. Otherwise, normal business operations may be affected.

**Procedure**

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
| AK | The AccessKey ID and AccessKey secret of the organization, which can be obtained from the Organizations page of the Apsara Uni-manager Management Console based on the organization to which the VPC belongs. For more information, see Manage the AccessKey pairs of an organization in Apsara Uni- manager Management Console User Guide. | The AccessKey ID and AccessKey secret of the organization, which can be obtained from the Organizations page of the Apsara Uni-manager Management Console based on the organization to which the VBR belongs. For more information, see Manage the AccessKey pairs of an organization in Apsara Uni-manager Management Console User Guide. |
| SK |   |   |

If the specified values are invalid, click **Re-enter** in the lower part of the tab and configure the parameters again.
7. Click **Next**.
8. Check the information. If the information is correct, click **Confirm**.
The system begins to deliver the configurations. After the configurations are delivered, the
**Result: Successful** message appears.
After the configurations are delivered, you can choose **Product Operation** > **Networking**
> **Network Intelligence** in the navigation bar of the Apsara Uni-manager Operations
Console. On the homepage of Apsara Network Intelligence, enter the ID of the router interface to search for the router interface. If no search result appears, the router interface is deleted.

**Delete a VBR**

In O&M emergency scenarios, you can use this feature to delete a VBR.

**Warning**

This operation is only for emergency scenarios and must be performed under the guidance of R&D engineers. Otherwise, normal business operations may be affected.

**Procedure**

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
|---|---|
| SK |   |

If the specified values are invalid, click **Re-enter** in the lower part of the tab and configure the parameters again.
7. Click **Next**.
8. Check the information. If the information is correct, click **Confirm**.
The system begins to deliver the configurations. After the configurations are delivered, the
**Result: Successful** message appears.
After the configurations are delivered, you can choose **Product Operation** > **Networking**
> **Network Intelligence** in the navigation bar of the Apsara Uni-manager Operations
Console. On the homepage of Apsara Network Intelligence, enter the ID of the VBR to search for the VBR. If no search result appears, the VBR is deleted.

**Delete an Express Connect circuit**

In O&M emergency scenarios, you can use this feature to delete an Express Connect circuit.

**Warning**

This operation is only for emergency scenarios and must be performed under the guidance of R&D engineers. Otherwise, normal business operations may be affected.

**Procedure**

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
| SK |   |

If the specified values are invalid, click **Re-enter** in the lower part of the tab and configure the parameters again.
7. Click **Next**.
8. Check the information. If the information is correct, click **Confirm**.
The system begins to deliver the configurations. After the configurations are delivered, the
**Result: Successful** message appears.
After the configurations are delivered, you can choose **Product Operation** > **Networking**
> **Network Intelligence** in the navigation bar of the Apsara Uni-manager Operations
Console. On the homepage of Apsara Network Intelligence, enter the ID of the Express Connect circuit to search for the Express Connect circuit. If no search result appears, the Express Connect circuit is deleted.

**Delete all resources**

In O&M emergency scenarios, you can use this feature to delete all resources, including VPC route entries, VBR route entries, VPC router interfaces, VBR interfaces, VBRs, and Express Connect circuits.

**Warning**

This operation is only for emergency scenarios and must be performed under the guidance of R&D engineers. Otherwise, normal business operations may be affected.

**Procedure**

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
|---|---|
| VPC CIDR1 | The destination CIDR block 1 to which the VPC points, which can be obtained from the VPC console. For more information about how to obtain a destination CIDR block, see VPC User Guide. |
| VPC CIDR2 | The destination CIDR block 2 to which the VPC points, which can be obtained from the VPC console. For more information about how to obtain a destination CIDR block, see VPC User Guide. |
| VBR Router Interface ID | The ID of the VBR interface. If the bare metal instance involved with the VBR is connected to a VPC, you can search for the bare metal instance by bare metal instance name on the Bare Metal Network Management tab, and then click Details in the Actions column. The value of the VBR Router Interface parameter in the details is the value of this parameter. If the bare metal instance involved with the VBR fails to be connected to a VPC, specify the name and creation time of the bare metal instance to search for the operation logs and find an operation log whose API Operation is add on the Operation Logs tab. Click Details in the Actions column. The value of the VBR Router Interface in the details is the value of this parameter. |
| VBR ID | The ID of the VBR that you want to delete. On theO peration Logs tab, specify the name and creation time of the bare metal instance to search for the operation logs and find an operation log whose API Operation is add. Click Details in the Actions column. The value of the VBR ID parameter in the details is the value of this parameter. |
| Express Connect Circuit ID | The ID of the Express Connect circuit that you want to delete. On the Operation Logs tab, specify the name and creation time of the bare metal instance to search for the operation logs and find an operation log whose API Operation is add. Click Details in the Actions column. The value of the Express Connect Circuit ID parameter in the details is the value of this parameter. |
| Trunk ID | You do not need to specify this parameter. |

If the specified values are invalid, click **Re-enter** in the lower part of the tab and configure the parameters again.
7. Click **Next**.
8. Check the information. If the information is correct, click **Confirm**.
The system begins to deliver the configurations. After the configurations are delivered, the
**Result: Successful** message appears.

**View the bandwidth of an Express Connect circuit**

You can view the bandwidth of the Express Connect circuit to which a router interface corresponds based on your O&M requirements when a CGW instance is connected to a VPC in the system.

**Procedure**

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
|---|---|
| SK |   |

7. View the table on the left and obtain the bandwidth in units of bit/s based on the
specifications. The bandwidth information describes the specifications of the Express Connect circuit bandwidth on the HSW of the current VPC.

| Specifications | Bandwidth (unit: bit/s) |
|---|---|
| Large.1 | 1G |
| Large.2 | 2G |
| Large.4 | 4G |
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

**Procedure**

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

**Procedure**

1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
3. In the left-side navigation pane, choose **Basic Network** > **Cloud Gateways**.
4. On the Cloud Gateway page, click the **O&M Settings** tab.
5. Select **View Trunk Usage** from the drop-down list in the upper-left corner of the tab.
6. Specify a trunk ID and CGW instance name, select a trunk state, and then click **Search** to
view trunk usage. Valid values of the **Status** parameter are **Idle**, **Used**, **Creating**, and
**Deleting**.
Specify the last integer of the value of the **Port** parameter that is obtained from the
**Bare Metal Network Management** tab as a trunk ID. For example, if the value of the
Port parameter is 10GE1/0/40, specify 40 as a trunk ID.

**View VPN usage of a bare metal instance**

You can view the VPN usage of a bare metal instance, and the VPN is assigned to a CGW instance.

**Procedure**

1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
3. In the left-side navigation pane, choose **Basic Network** > **Cloud Gateways**.
4. On the Cloud Gateway page, click the **O&M Settings** tab.
5. Select **View BM VPN Usage** from the drop-down list in the upper-left corner of the tab.
6. Specify the name of a CGW instance, a Virtual Extensible Local Area Network (VXLAN) ID,
and the VPN name of a bare metal instance, select a state, and then click **Search** to view the bare metal instance VPNs assigned to all the HSWs. Valid values of the **Status** parameter are **Succeeded** and **Creating**.

**View BD usage**

You can view BD usage to learn about the BD configuration distribution in a timely manner.

**Procedure**

1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
3. In the left-side navigation pane, choose **Basic Network** > **Cloud Gateways**.
4. On the Cloud Gateway page, click the **O&M Settings** tab.
5. Select **View BD Usage** from the drop-down list in the upper-left corner of the tab.
6. Specify a CGW instance name, BD ID, and vSwitch ID, select a state, and then click **Search**
to view BD usage. Valid values of the **Status** parameter are **Succeeded**, **Creating**, and
**Deleting**.

**Check initialization configurations**

In O&M emergency scenarios, you can use this feature to check whether the initialization configurations of the HSW are successful. This feature only checks the initialization status of the platform access gateway vSwitch and whether the initialization configurations are successful. No operation is performed on the bare metal instance.

**Procedure**

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

If the specified values are invalid, click **Re-enter** in the lower part of the tab and configure the parameters again.
7. After you specify the parameters, click **Next** and click **Check** to check the initialization
configurations of the vSwitch.

**Check route configurations**

In O&M emergency scenarios, you can use this feature to locate abnormal operations and check whether the route configurations of a bare metal instance are valid.

**Background information**

You can use this operation to locate the exception and scan the HSW after a bare metal instance fails to be added. This feature only checks whether the route configurations of the bare metal instance are valid. No operation is performed on the bare metal instance.

**Procedure**

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

If the specified values are invalid, click **Re-enter** in the lower part of the tab and configure the parameters again.
7. After you specify the parameters, click **Next** and click **Check** to check the route
configurations.

**Display the information about a bare metal network gateway**

In O&M emergency scenarios, you can use this feature to check the gateway of a vSwitch.

**Background information**

This operation is only for emergency scenarios in which the bare metal network is inaccessible. This operation is used to check the vSwitch gateway information and has no impact on the bare metal instance.

**Procedure**

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

If the specified values are invalid, click **Re-enter** in the lower part of the tab and configure the parameters again.
7. After you configure the parameters, click **Next** and click **Check** to check the information
about the bare metal network gateway.

### 2.4 Computing access gateways

You can use computing access gateways such as dedicated computing host switches (CHSWs) to connect intelligent computing servers to virtual private clouds (VPCs). This helps implement the centralized management of intelligent computing servers. The system supports operations such as instance management, operation log management, VPC management and Express Connect circuit management of bare metal instances, and O&M configurations to complete routine O&M operations on computing access gateways. By default, the Computing Access Gateway module is not displayed in the left-side navigation pane. To use this module, click **User Authorities** in the top navigation bar of the Apsara Uni-manager Operations Console. In the left-side navigation pane of the page that appears, click **Menu Management**. On the Menus page, find Computing Access Gateway and click Modify in the Actions column. In the Modify Menu panel, turn on **Show**.

**Manage access gateways**

On the Instance Management tab, you can view information about computing access gateways, such as the computing access gateway name, internal Border Gateway Protocol (IBGP) role, and creation time.

**Display devices**

1. Log in to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation > Networking > Network**
3. In the left-side navigation pane, choose **Basic Network > Computing Access Gateway**.
4. On the **Computing Access Gateway** page, click the **Instance Management** tab.
5. On the **Display Devices** tab, view the information about computing access gateways.

| Parameter | Description |
|---|---|
| Computing Access Gateway Name | The name of the computing access gateway. |
| IBGP Role | The role of the computing access gateway in the environment. |

| Manage IP Address | The IP address of the computing access gateway. |
|---|---|
| Manufacturer | The manufacturer of the computing access gateway. |
| Model | The model of the computing access gateway. |
| Management Status | The initialization status of the computing access gateway. Uninitialized Initializing Initialized |
| Authorization Status | The authorization status of the computing access gateway. Unauthorized Authorized Note To use computing access gateways, you must plan the number of computing access gateway licenses in Deployment Planner. If the number of computing access gateway licenses in Deployment Planner is less than the number of computing access gateways in use, the computing access gateways without license authorization are in the Unauthorized state. In this case, you need to increase the number of computing access gateway licenses. |
| Created At | The time when the computing access gateway was created. |

**Scan for new devices**

1. Log in to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation > Networking > Network**
3. In the left-side navigation pane, choose **Basic Network > Computing Access Gateway**.
4. On the **Computing Access Gateway** page, click the **Instance Management** tab.
5. Click the **Scan for New Devices** tab.

**Stacked Networking Devices**

a. View devices On the **Stacked Networking Devices** tab, you can view the following information about devices: **Computing Access Gateway Name**, **Manage IP Address**, **IBGP**
**Role**, **Vendor**, and **Model**.
b. Configure the IBGP role for a device a. In the device list, find the device that you want to manage and click **Manage** in the
**Actions** column.
Alternatively, select multiple devices that you want to manage and click **Batch**
**Manage**.
b. Select an IBGP role from the **IBGP Role** drop-down list. Then, click **OK**. The IBGP role specifies the role of the computing access gateway in the environment. Valid values: Client, Deploy Client and RR on a Device, and Deploy RR on a Device.
**Client**: The computing access gateway serves as the client of the IBGP peer and is
used only for server access.
**Deploy Client and RR on a Device** : The computing access gateway serves as
the RR reflective route of the IBGP peer and is used for server access.
**Deploy RR on a Device**: The computing access gateway serves only as the RR
reflective route of the IBGP peer and cannot be used for server access.

**Important**

The following list describes the networking requirements for the IBGP role: Single-data center deployment: At least one set of computing access gateways is deployed, and the IBGP roles of the computing access gateways are RR roles. The IBGP roles of other devices are Client. Multi-data center deployment: A set of computing access gateways is deployed in at least two data centers, and the IBGP roles of the computing access gateways are RR roles. The IBGP roles of other devices are Client. RR role recommendations: We recommend that you set the role to Deploy Client and RR on A Device. If you have higher network stability requirements, we recommend that you set the role to Deploy RR on a Device.

**Unstacked Networking Devices**

Perform the following operations to manage devices. Click the **Unstacked Networking Devices** tab. You can view the following information about devices: **Name of Computing Platform Access Gateway 1**,
**Management IP Address 1**, **Name of Computing Platform Access Gateway 2**,
**Management IP Address 2**, **IBGP Role**, **Vendor**, and **Model**.
Configure the IBGP role for a device a. In the device list, find the device that you want to manage and click **Manage** in the
**Actions** column.
Alternatively, select multiple devices that you want to manage and click **Batch**
**Manage**.
b. Select an IBGP role from the **IBGP Role** drop-down list. Then, click **OK**. The IBGP role specifies the role of the computing access gateway in the environment. Valid values: Client, Deploy Client and RR on a Device, and Deploy RR on a Device.
**Client**: The computing access gateway serves as the client of the IBGP peer and is
used only for server access.
**Deploy Client and RR on a Device** : The computing access gateway serves as
the RR reflective route of the IBGP peer and is used for server access.
**Deploy RR on a Device**: The computing access gateway serves only as the RR
reflective route of the IBGP peer and cannot be used for server access.

**Important**

The following list describes the networking requirements for the IBGP role: Single-data center deployment: At least one set of computing access gateways is deployed, and the IBGP roles of the computing access gateways are RR roles. The IBGP roles of other devices are Client. Multi-data center deployment: A set of computing access gateways is deployed in at least two data centers, and the IBGP roles of the computing access gateways are RR roles. The IBGP roles of other devices are Client. RR role recommendations: We recommend that you set the role to Deploy Client and RR on A Device. If you have higher network stability requirements, we recommend that you set the role to Deploy RR on a Device.

**Manage operation logs**

To meet O&M requirements, you can view the records and results of API operations that are managed by bare metal instances and called by the Apsara Uni-manager Operations Console. The API records and results are provided by the computing access gateways.
1. Log in to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation > Networking > Network**
3. In the left-side navigation pane, choose **Basic Network > Computing Access Gateway**.
4. On the **Computing Access Gateway** page, click the **Operation History** tab to view the
operation logs. Click **Advanced Filter** and filter operation logs by **Start/End Time**, **Bare Metal Name**,
**VPC ID**, **vSwitch ID**, **VBR ID**, **BD ID**, **Computing Access Gateway Name**, or any
combination of them.

| Parameter | Description |
|---|---|
| ID | The ID of the API operation log entry. |
| Bare Metal Name | The name of the bare metal instance that was applied for or released in the VPC. |
| Created At | The time when the API operation was performed. |
| API Operation | The API operation, such as operations to apply for or release bare metal instances in a VPC. Valid values: add: applies for a bare metal instance in the VPC. del: releases a bare metal instance in the VPC. del pc: deletes an Express Connect circuit. _ del vbr: deletes a virtual border router (VBR). _ del router intf: deletes a router interface. _ _ del route entry: deletes a route entry. _ _ |
| vSwitch ID | The ID of the dedicated vSwitch when the bare metal instance is applied for or released in the VPC. |
| Computing Access Gateway Name | The name of the computing access gateway that is involved in the current API operation. |
| Port | The port to which the bare metal instance is connected. |

| Status | The status of the API operation. success: The API operation was successful. If the API operation is in progress, the value indicates the real-time status of the API operation. If the API operation is complete but the state is nots uccess, you can view the failure information in this column. Example: create vpc connection fail. |
|---|---|

5. In the operation history list, find the operation log that you want to view and click **Details**
in the **Actions** column. In the panel that appears, view the details of the operation log.

**VPC Management**

Create a bare metal instance and connect it to a VPC based on your O&M requirements. After the bare metal instance is connected to the VPC, the bare metal instance can communicate with other resources in the VPC over a private network.
1. Log in to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation > Networking > Network**
3. In the left-side navigation pane, choose **Basic Network > Computing Access Gateway**.
4. On the **Computing Access Gateway** page, click the **VPC Management** tab.
5. Click **Create Bare Metal Instance**.
6. In the **Create Bare Metal Instance** dialog box, configure the **Bare Metal Name**, **SN**, and
**Description** parameters, and then click **OK**.
7. On the **Computing Access Gateway** page, view the bare metal instances.
Click **Advanced Filter** and filter bare metal instances by **Bare Metal Name**, **VPC ID**,
**vSwitch ID**, **Computing Access Gateway Name**, or any combination of them.

| Parameter | Description |
|---|---|
| Bare Metal Name | The name of the bare metal instance. |
| SN | The serial number of the bare metal instance. |

| Status | The status of the bare metal instance. |
|---|---|
| VPC ID | The ID of the VPC to which the bare metal instance belongs. |
| vSwitch ID | The ID of the vSwitch to which the bare metal instance belongs. |
| Computing Access Gateway Name | The name of the computing access gateway to which the bare metal instance is connected. You can distinguish between stacked networking devices and unstacked networking devices based on Computing Access Gateway Name to perform operations on the devices. |
| Port | The port of the computing access gateway to which the bare metal instance is connected. |
| Created At | The time when the network of the bare metal instance was created. |
| Bare Metal IP Address | The IP address of the bare metal instance. Click Manage in the Bare Metal IP Address column to assign an IP address to the bare metal instance. This helps you configure the network of the bare metal instance. For more information, see the Manage the IP address of a bare metal instance section of this topic. |

**View the network information about a bare metal instance**

**in a VPC**

a. In the bare metal instance list, find the bare metal instance that you want to view and click **Details** in the **Actions** column. In the panel that appears, view the details of the bare metal instance.

**Connect the bare metal instance to a VPC**

a. In the bare metal instance list, find the bare metal instance that you want to manage and click **Connect to VPC** in the **Actions** column. b. In the **Connect to VPC** dialog box, configure the following parameters and click **OK**.

| Parameter | Description |
|---|---|
| Bare Metal Name | The name of the bare metal instance. You do not need to specify this parameter. |
| Bare Metal SN | The serial number of the bare metal instance. You do not need to specify this parameter. |

| AccessKey ID | The AccessKey ID and AccessKey secret of the organization, which can be obtained from the Organizations page of the Apsara Uni- manager Management Console based on the organization to which the VPC belongs. For more information, see Manage the AccessKey pairs of an organization in Apsara Uni-manager Management Console User Guide. |
|---|---|
| AccessKey Secret |   |
| vSwitch ID | The ID of the dedicated vSwitch to which the bare metal instance is connected. |
| Region ID | The ID of the region in which the current environment resides. |
| Computing Access Gateway Name | The name of the computing access gateway to which the bare metal instance is connected. You can distinguish between stacked networking devices and unstacked networking devices based on Computing Access Gateway Name to perform operations on the devices. |
| Port | The port of the computing access gateway to which the bare metal instance is connected. |
| Bare Metal Description | The description of the bare metal instance. |

**Close the Connection to VPC**

After a bare metal instance is connected to a VPC, you can click **Close the**
**Connection to VPC** to disconnect the bare metal instance from the VPC.
After you disconnect the bare metal instance from the VPC, the connection cannot be recovered. Proceed with caution. a. In the bare metal instance list, find the bare metal instance that you want to manage and click **Close the Connection to VPC** in the **Actions** column. b. In the message that appears, click **Exit**.

**Delete a bare metal instance**

You can delete a bare metal instance only if the instance is created on the **VPC**
**Management** page.
After a bare metal instance is connected to a VPC, you can click **Delete**
**Instance** to disconnect the bare metal instance from the VPC and delete the
instance. After you delete a bare metal instance, it cannot be recovered. Proceed with caution. a. In the bare metal instance list, find the bare metal instance that you want to delete and click **Delete Instance** in the **Actions** column. b. In the message that appears, click **Delete**.

**Manage the IP address of a bare metal instance**

Computing access gateways work with Bare Metal Management Service (BMS). BMS is used to install bare metal instances, assign IP addresses, and complete network configurations. Computing access gateways are used to connect bare metal instances to VPCs. In some scenarios, you may not install bare metal instances or complete network configurations by using BMS, but you must use computing access gateways to connect bare metal instances to VPCs. In such scenarios, the system cannot assign IP addresses to bare metal instances, and you must manually maintain IP address assignment results. This may cause IP address conflicts and poor usability. Therefore, network management of bare metal instances is supported on the Computing Access Gateway page. You can manage IP addresses of bare metal instances in the Bare Metal IP Address Management panel. a. In the bare metal instance list, find the bare metal instance that you want to manage and click **Manage** in the **Bare Metal IP Address** column. b. In the **Bare Metal IP Address Management** panel, click **Apply for Bare Metal IP**
**Address**.
c. In the **Apply for Bare Metal IP Address** dialog box, configure the **Bare Metal NIC**,
**IP**, and **IP Address Description** parameters and click **OK**.
If you leave the **IP** parameter empty, the system automatically generates an IP address. d. After you apply for an IP address for a bare metal instance, view the IP address in the
**Bare Metal IP Address Management** panel. The IP address information includes **ID**,
**IP Address**, **Bare Metal Name/SN**, **Bare Metal NIC**, **Created At**, **Modified At**,
**Description**, **VPC ID**, and **vswitch id**.
Find the bare metal IP address that you want to manage and click **Edit** in the
**Actions** column to modify the **IP** and **IP Address Description** parameters.
Find the bare metal IP address that you want to manage and click **Release** in the
**Actions** column to release the bare metal IP address.

**Private Line Management**

On the Private Line Management tab, you can view the bare metal networks associated with Express Connect Routers (ECRs).
1. Log in to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation > Networking > Network**
3. In the left-side navigation pane, choose **Basic Network > Computing Access Gateway**.
4. On the **Computing Access Gateway** page, click the **Private Line Management** tab to
view the Express Connect circuit information about bare metal instances. Click **Advanced Filter** and filter bare metal instances by **vSwitch ID**, **VPC ID**, **Private**
**Line Gateway Name**, or any combination of them.

| Parameter | Description |
|---|---|
| VPC ID | The ID of the VPC to which the bare metal instance belongs. |

| vSwitch ID | The ID of the vSwitch to which the bare metal instance belongs. |
|---|---|
| Status | The status of the bare metal instance. |
| Name of Private Line Gateway 1 | The name of ECR 1 to which the bare metal instance is connected. |
| Source IP Address that Probes Gateway 1 | The source IP address of ECR 1. |
| Name of Private Line Gateway 2 | The name of ECR 2 to which the bare metal instance is connected. |
| Source IP Address that Probes Gateway 2 | The source IP address of ECR 2. |
| Created At | The time when the network of the bare metal instance was created. |

**View Express Connect circuit details of a bare metal**

**instance**

In the bare metal instance list, find the bare metal instance that you want to view and click **Details** in the **Actions** column. In the panel that appears, view the Express Connect circuit details of the bare metal instance.

**Delete an Express Connect circuit for a bare metal instance**

In the bare metal instance list, find the bare metal instance that you want to manage and click **Delete** in the **Actions** column to delete the Express Connect circuit for the bare metal instance.

**O&M Settings**

1. Log in to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation > Networking > Network**
3. In the left-side navigation pane, choose **Basic Network > Computing Access Gateway**.
4. On the **Computing Access Gateway** page, click the **O&M Settings** tab to perform
routine O&M operations.

**Apply for a bare metal instance in a VPC**

In O&M emergency scenarios, you can use this feature to add the physical port of the computing access gateway associated with a bare metal instance to the VPC.

**Warning**

This operation is only for emergency scenarios and must be performed under the guidance of R&D engineers. Otherwise, normal business operations may be affected. This feature can be used only to connect a bare metal instance to the port of a computing access gateway but cannot be used to perform operations on the bare metal instance. To configure the network port, IP address, and routing information of the bare metal instance, contact the corresponding product team for guidance. In most cases, you cannot use this feature to apply for a bare metal instance in a VPC. You can use the bare metal controller to call an API operation to enable the bare metal network. i. Select **Apply for Bare Metal in VPC** from the drop-down list in the upper-left corner of the tab. ii. Configure the following parameters and click **Next**.

| Parameter | Description |
|---|---|
| Region ID | The name of the region in which the current environment resides. |
| Computing Access Gateway Name | The name of the computing access gateway to which the bare metal instance is connected. You can distinguish between stacked networking devices and unstacked networking devices based on Computing Access Gateway Name to perform operations on the devices. |
| vSwitch ID | The ID of the vSwitch to which you want to add the bare metal instance. You can obtain the vSwitch ID from the VPC console of the Apsara Uni-manager Management Console. |
| Port | The port of the bare metal instance that is connected to the computing access gateway. |
| AccessKey ID | The AccessKey ID and AccessKey secret of the organization, which can be obtained from the Organizations page of the Apsara Uni-manager Management Console based on the organization to which the VPC belongs. For more information, see Manage the AccessKey pairs of an organization in Apsara Uni-manager Management Console User Guide. |
| AccessKey Secret |   |
| Bare Metal Name | The name of the bare metal instance that you want to apply for. The name must be unique. |

If the specified values are invalid, click **Re-enter** in the lower part of the tab and configure the parameters again. iii. Check whether the parameter configurations are valid. If yes, click **Confirm**. The system starts to apply the configurations. After the configurations are applied, the **Result: Successful** message appears. If not, click **Back to Modify** to configure the parameters again. iv. Optional. After the configurations are applied, you can search for the bare metal instance by bare metal instance name on the **VPC Management** tab. If the bare metal instance is displayed, it is connected to the VPC.

**Release a bare metal instance from a VPC**

In O&M emergency scenarios, you can use this feature to disconnect the physical port of the computing access gateway associated with a bare metal instance from a VPC.

**Warning**

This operation is only for emergency scenarios and must be performed under the guidance of R&D engineers. Otherwise, normal business operations may be affected. This feature can be used only to disconnect a bare metal instance from the port of a computing access gateway but cannot be used to perform operations on the bare metal instance. To configure the network port, IP address, and routing information of the bare metal instance, contact the corresponding product team for guidance. In most cases, you cannot use the feature to release a bare metal instance in a VPC. You can use the bare metal controller to call an API operation to delete the network of the bare metal instance. i. Select **Release Bare Metal in VPC** from the drop-down list in the upper-left corner of the tab. ii. Configure the following parameters and click **Next**.

| Parameter | Description |
|---|---|
| Region ID | The name of the region in which the current environment resides. |
| Computing Access Gateway Name | The name of the computing access gateway to which the bare metal instance is connected. You can distinguish between stacked networking devices and unstacked networking devices based on Computing Access Gateway Name to perform operations on the devices. |
| Bare Metal Name | The name of the bare metal instance that you want to release. You can obtain the name of the bare metal instance on theV PC Management tab. |

If the specified values are invalid, click **Re-enter** in the lower part of the tab and configure the parameters again. iii. Check whether the parameter configurations are valid. If yes, click **Confirm**. The system starts to apply the configurations. After the configurations are applied, the **Result: Successful** message appears. If not, click **Back to Modify** to configure the parameters again. iv. Optional. After the configurations are applied, you can search for the bare metal instance by bare metal instance name on the **VPC Management** tab. If the bare metal instance is not displayed, it is released from the VPC.

**Delete a route entry**

In O&M emergency scenarios, you can use this feature to delete route entries that point to the subnet of a bare metal instance in a VPC and the default route entries of a VBR.

**Warning**

This operation is only for emergency scenarios and must be performed under the guidance of R&D engineers. Otherwise, normal business operations may be affected. In most cases, you cannot use this feature to delete a VPC route entry. This operation is only used for emergency scenarios. You can perform this operation to delete only one route entry at a time. To delete multiple route entries, you must perform this operation multiple times. i. Select **Delete Route Table Entry** from the drop-down list in the upper-left corner of the tab. ii. Configure the following parameters and click **Next**.

| Parameter | Description about deleting a VPC route entry | Description about deleting a VBR route entry |
|---|---|---|
| Region ID | The name of the region in which the current environment resides. | The name of the region in which the current environment resides. |

| Route Table ID | The ID of the VPC route table, which can be obtained from the VPC console. For more information about how to obtain the ID of a VPC route table, see VPC User Guide. | The ID of the VBR route table. If the bare metal instance associated with the VBR is connected to a VPC, you can search for the bare metal instance by bare metal instance name on the VPC Management tab, click Details in the Actions column, and then view the value of the VBR Route Table ID parameter. If the bare metal instance associated with the VBR is not added to the VPC, specify the bare metal instance name and creation time to search for the operation log entry whose API Operation is add on the Operation History tab. Click Details and view the value of the VBR Route Table ID parameter. |
|---|---|---|
| Router Interface ID | The ID of the VPC router interface, which can be obtained from the VPC console. For more information about how to obtain the ID of a VPC router interface, see VPC User Guide. | The ID of the VBR interface. If the bare metal instance associated with the VBR is added to VPC, you can search for the bare metal instance on the VPC Management tab based on the bare metal instance name, and then click Detail to view the value of the VBR Router Interface parameter. If the bare metal instance associated with the VBR is not added to the VPC, specify the bare metal instance name and creation time to search for the operation log entry whose API Operation is add on the Operation History tab. Click Details and view the value of the VBR Router Interface parameter. |
| Routing Destinatio n CIDR | The destination CIDR block to which the VPC points, which can be obtained from the VPC console. For more information about how to obtain a destination CIDR block, see VPC User Guide. | Set the value to 0.0.0.0/0. |
| AccessKey ID | The AccessKey ID and AccessKey secret of the organization, which can be obtained from the Organizations page of the Apsara Uni-manager Management Console based on the organization to which the VPC belongs. For more information, see Manage the AccessKey pairs of an organization in Apsara Uni- manager Management Console User Guide. | The AccessKey ID and AccessKey secret of the organization, which can be obtained from the Organizations page of the Apsara Uni-manager Management Console based on the organization to which the VBR belongs. For more information, see Manage the AccessKey pairs of an organization in Apsara Uni- manager Management Console User Guide. |
| AccessKey Secret |   |   |

If the specified values are invalid, click **Re-enter** in the lower part of the tab and configure the parameters again. iii. Check whether the parameter configurations are valid. If yes, click **Confirm**. The system starts to apply the configurations. After the configurations are applied, the **Result: Successful** message appears. If not, click **Back to Modify** to configure the parameters again. iv. Optional. In actual fault scenarios, if multiple route entries exist in the route table, repeat Step 5 to Step 8 to delete other route entries.

**Delete a router interface**

In O&M emergency scenarios, you can use this feature to delete a VPC router interface and a VBR interface.

**Warning**

This operation is only for emergency scenarios and must be performed under the guidance of R&D engineers. Otherwise, normal business operations may be affected. i. Select **Delete Router Interface** from the drop-down list in the upper-left corner of the tab. ii. Configure the following parameters and click **Next**.

| Parameter | Description about deleting a VPC router interface | Description about deleting a VBR interface |
|---|---|---|
| Region ID | The name of the region in which the current environment resides. | The name of the region in which the current environment resides. |
| Router Interface ID | The ID of the VPC router interface. On the Operation History tab, specify the name and creation time of the bare metal instance to search for the operation log entry whose API Operation is add. Click Details in the Actions column and view the value of the VPC Router Interface parameter. | The ID of the VBR interface. If the bare metal instance associated with the VBR is added to VPC, you can search for the bare metal instance on the VPC Management tab based on the bare metal instance name, and then click Detail to view the value of the VBR Router Interface parameter. If the bare metal instance associated with the VBR is not added to the VPC, specify the bare metal instance name and creation time to search for the operation log entry whose API Operation is add on the Operation History tab. Click Details and view the value of the VBR Router Interface parameter. |
| AccessKey ID | The AccessKey ID and AccessKey secret of the organization, which can be obtained from the Organizations page of the Apsara Uni-manager Management Console based on the organization to which the VPC belongs. For more information, see Manage the AccessKey pairs of an organization in Apsara Uni- manager Management Console User Guide. | The AccessKey ID and AccessKey secret of the organization, which can be obtained from the Organizations page of the Apsara Uni-manager Management Console based on the organization to which the VBR belongs. For more information, see Manage the AccessKey pairs of an organization in Apsara Uni-manager Management Console User Guide. |
| AccessKey Secret |   |   |

If the specified values are invalid, click **Re-enter** in the lower part of the tab and configure the parameters again. iii. Check whether the parameter configurations are valid. If yes, click **Confirm**. The system starts to apply the configurations. After the configurations are applied, the **Result: Successful** message appears. If not, click **Back to Modify** to configure the parameters again. iv. Optional. After the configurations are applied, you can choose **Product Operation** >
**Networking** > **Network Intelligence** in the top navigation bar of the Apsara Uni-
manager Operations Console. On the homepage of Apsara Network Intelligence, enter the ID of the router interface to search for the router interface. If no search result appears, the router interface is deleted.

**Delete a VBR**

In O&M emergency scenarios, you can use this feature to delete a VBR.

**Warning**

This operation is only for emergency scenarios and must be performed under the guidance of R&D engineers. Otherwise, normal business operations may be affected. i. Select **Delete VBR** from the drop-down list in the upper-left corner of the tab. ii. Configure the following parameters and click **Next**.

| Parameter | Description |
|---|---|
| Region ID | The name of the region in which the current environment resides. |
| VBR ID | The ID of the VBR that you want to delete. On theO peration History tab, specify the name and creation time of the bare metal instance to search for the operation log entry whose API Operation is add. Click Details in the Actions column to view the value of the VBR ID parameter. |
| AccessKey ID | The AccessKey ID and AccessKey secret of the organization, which can be obtained from the Organizations page of the Apsara Uni-manager Management Console based on the organization to which the VBR belongs. For more information, see Manage the AccessKey pairs of an organization in Apsara Uni-manager Management Console User Guide. |
| AccessKey Secret |   |

If the specified values are invalid, click **Re-enter** in the lower part of the tab and configure the parameters again. iii. Check whether the parameter configurations are valid. If yes, click **Confirm**. The system starts to apply the configurations. After the configurations are applied, the **Result: Successful** message appears. If not, click **Back to Modify** to configure the parameters again. iv. Optional. After the configurations are applied, you can choose **Product Operation** >
**Networking** > **Network Intelligence** in the top navigation bar of the Apsara Uni-
manager Operations Console. On the homepage of Apsara Network Intelligence, enter the ID of the VBR to search for the VBR. If no search result appears, the VBR is deleted.

**Delete an Express Connect circuit**

In O&M emergency scenarios, you can use this feature to delete an Express Connect circuit.

**Warning**

This operation is only for emergency scenarios and must be performed under the guidance of R&D engineers. Otherwise, normal business operations may be affected. i. Select **Delete Express Connect Circuit** from the drop-down list in the upper-left corner of the tab. ii. Configure the following parameters and click **Next**.

| Parameter | Description |
|---|---|
| Region ID | The name of the region in which the current environment resides. |
| Express Connect Circuit ID | The ID of the Express Connect circuit that you want to delete. On the Operation History tab, specify the bare metal instance name and creation time to search for the operation log entry whose API Operation is add. Click Details to view the value of the Express Connect Circuit ID parameter. |
| AccessKey ID | The AccessKey ID and AccessKey secret of the organization, which can be obtained from the Organizations page of the Apsara Uni-manager Management Console based on the organization to which the VPC belongs. For more information, see Manage the AccessKey pairs of an organization in Apsara Uni-manager Management Console User Guide. |
| AccessKey Secret |   |

If the specified values are invalid, click **Re-enter** in the lower part of the tab and configure the parameters again. iii. Check whether the parameter configurations are valid. If yes, click **Confirm**. The system starts to apply the configurations. After the configurations are applied, the **Result: Successful** message appears. If not, click **Back to Modify** to configure the parameters again. iv. Optional. After the configurations are applied, you can choose **Product Operation** >
**Networking** > **Network Intelligence** in the top navigation bar of the Apsara Uni-
manager Operations Console. On the homepage of Apsara Network Intelligence, enter the ID of the Express Connect circuit to search for the Express Connect circuit. If no search result appears, the Express Connect circuit is deleted.

**Delete all resources**

In O&M emergency scenarios, you can use this feature to delete all resources, including VPC route entries, VBR route entries, VPC router interfaces, VBR interfaces, VBRs, and Express Connect circuits.

**Warning**

This operation is only for emergency scenarios and must be performed under the guidance of R&D engineers. Otherwise, normal business operations may be affected. i. Select **Delete ALL Resources** from the drop-down list in the upper-left corner of the tab. ii. Configure the following parameters and click **Next**.

| Parameter | Description |
|---|---|
| Region ID | The ID of the region in which the environment resides. |
| Computing Access Gateway Name | The name of the computing access gateway to which the bare metal instance is connected. |

| AccessKey ID | The AccessKey ID and AccessKey secret of the organization, which can be obtained from the Organizations page of the Apsara Uni- manager Management Console based on the organization to which the VPC belongs. For more information, see Manage the AccessKey pairs of an organization in Apsara Uni-manager Management Console User Guide. |
|---|---|
| AccessKey Secret |   |
| VPC Router Interface ID | The ID of the VPC router interface, which can be obtained from the VPC console. For more information about how to obtain the ID of a VPC router interface, see VPC User Guide. |
| VPC Route Table ID | The ID of the VPC route table, which can be obtained from the VPC console. For more information about how to obtain the ID of a VPC route table, see VPC User Guide. |
| VBR Route Table ID | The ID of the VBR route table. If the bare metal instance associated with the VBR is connected to a VPC, you can search for the bare metal instance by bare metal instance name on the VPC Management tab, click Details in the Actions column, and then view the value of the VBR Route Table ID parameter. If the bare metal instance associated with the VBR is not added to the VPC, specify the bare metal instance name and creation time to search for the operation log entry whose API Operation is add on the Operation History tab. Click Details and view the value of the VBR Route Table ID parameter. |
| VPC CIDR1 | The Destination CIDR Block 1 to which the VPC points, which can be obtained from the VPC console. For more information about how to obtain a destination CIDR block, see VPC User Guide. |
| VPC CIDR2 | The Destination CIDR Block 2 to which the VPC points, which can be obtained from the VPC console. For more information about how to obtain a destination CIDR block, see VPC User Guide. |
| VBR Router Interface ID | The ID of the VBR interface. If the bare metal instance associated with the VBR is connected to a VPC, you can search for the bare metal instance by bare metal instance name on the VPC Management tab, click Details in the Actions column, and then view the value of the VBR Router Interface parameter. If the bare metal instance associated with the VBR is not added to the VPC, specify the bare metal instance name and creation time to search for the operation log entry whose API Operation is add on the Operation History tab. Click Details and view the value of the VBR Router Interface parameter. |
| VBR ID | The ID of the VBR that you want to delete. On theO peration History tab, specify the name and creation time of the bare metal instance to search for the operation log entry whose API Operation is add. Click Details in the Actions column to view the value of the VBR ID parameter. |

| Express Connect Circuit ID | The ID of the Express Connect circuit that you want to delete. On the Operation History tab, specify the bare metal instance name and creation time to search for the operation log entry whose API Operation is add. Click Details to view the value of the Express Connect Circuit ID parameter. |
|---|---|
| Trunk ID | You do not need to specify this parameter. |

If the specified values are invalid, click **Re-enter** in the lower part of the tab and configure the parameters again. iii. Check whether the parameter configurations are valid. If yes, click **Confirm**. The system starts to apply the configurations. After the configurations are applied, the **Result: Successful** message appears. If not, click **Back to Modify** to configure the parameters again.

**View the bandwidth of an Express Connect circuit**

You can view the bandwidth of the Express Connect circuit for a router interface when the computing access gateway is connected to a VPC based on your O&M requirements. i. Select **View Express Connect Circuit Bandwidth** from the drop-down list in the upperleft corner of the tab. ii. Configure the following parameters and click **Query**. The system displays the bandwidth of the Express Connect circuit that meets the filter conditions.

| Parameter | Description |
|---|---|
| Region ID | The name of the region in which the current environment resides. |
| Router Interface ID | The ID of the VBR interface. On the VPC Management tab, specify a VPC ID and computing access gateway name and click Search. Click Details in the Actions column to view the value of the VBR Router Interface parameter. |
| AccessKey ID | The AccessKey ID and AccessKey secret of the organization, which can be obtained from the Organizations page of the Apsara Uni-manager Management Console based on the organization to which the VPC belongs. For more information, see Manage the AccessKey pairs of an organization in Apsara Uni-manager Management Console User Guide. |
| AccessKey Secret |   |

iii. View the table on the left and obtain the bandwidth in units of bit/s based on the specifications. The bandwidth information describes the specifications of the Express Connect circuit bandwidth on the HSW of the current VPC.

| Specification | Bandwidth (bit/s) |
|---|---|
| Large.1 | 1G |
| Large.2 | 2G |
| Large.4 | 4G |
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

This operation may affect your business. Unauthorized operations are prohibited. Configuration changes must be performed under the guidance of technical support. i. Select **Change Express Connect Circuit Bandwidth** from the drop-down list in the upper-left corner of the tab. ii. Configure the following parameters and click **Next**.

| Parameter | Description |
|---|---|
| Region ID | The name of the region in which the current environment resides. |
| Router Interface ID | The ID of the VBR interface. On the VPC Management tab, specify a VPC ID and computing access gateway name and click Search. Click Details in the Actions column to view the value of the VBR Router Interface parameter. |
| Router Interface Specifications | The new bandwidth of the Express Connect circuit. |
| AccessKey ID | The AccessKey ID and AccessKey secret of the organization, which can be obtained from the Organizations page of the Apsara Uni-manager Management Console based on the organization to which the VPC belongs. For more information, see Manage the AccessKey pairs of an organization in Apsara Uni-manager Management Console User Guide. |
| AccessKey Secret |   |

iii. Check whether the parameter configurations are valid. If yes, click **Confirm**. The system starts to apply the configurations. After the configurations are applied, the **Result: Successful** message appears. If not, click **Back to Modify** to configure the parameters again. iv. Optional. After the configurations are applied, check whether the bandwidth of the Express Connect circuit is changed. For more information, see the View the bandwidth of an Express Connect circuit section of this topic.

**View trunk usage**

You can view trunk usage to obtain up-to-date information about the usage of hardware ports. i. Select **View Trunk Usage** from the drop-down list in the upper-left corner of the tab. ii. View the trunk usage in the list. By default, all data in the **idle** state is displayed. Specify a trunk ID and computing access gateway name, select a trunk state, and then click **Search** to view trunk usage. Valid values of the **Status** parameter are **Idle**, **Used**,
**Creating**, and **Deleting**.
Specify the last integer of the value of the **Port** parameter that is obtained from the
**VPC Management** tab as the **trunk ID**. For example, if the value of the Port
parameter is 10GE1/0/40, specify 40 as the **trunk ID**.

**View VPN usage of a bare metal instance**

You can view the VPN usage of a bare metal instance and the VPN assigned to a computing access gateway. i. Select **View BM VPN Usage** from the drop-down list in the upper-left corner of the tab. ii. In the list, view the bare metal instance VPNs assigned to all the HSWs. By default, all data in the **Succeeded** state is displayed. Specify the **name of a computing access gateway** , a **Virtual Extensible Local Area**
**Network (VXLAN) ID**, and the **VPN name of a bare metal instance** , select a state,
and then click **Search** to view the bare metal instance VPNs assigned to all the HSWs. Valid values of the **Status** parameter are **Succeeded** and **Creating**.

**View BD usage**

You can view BD usage to learn about the BD configuration distribution in a timely manner. i. Select **View BD Usage** from the drop-down list in the upper-left corner of the tab. ii. View the BD usage in the list. By default, all data in the **Succeeded** state is displayed. Specify a **computing access gateway name**, a **BD ID**, and a **vSwitch ID**, select a state, and then click **Search** to view BD usage. Valid values of the **Status** parameter are
**Succeeded**, **Creating**, and **Deleting**.

**Check initialization configurations**

In O&M emergency scenarios, you can use this feature to check whether the initialization configurations of the HSW are successful. This feature only checks the initialization status of vSwitches for computing access gateways and whether the initialization configurations are successful. No operation is performed on the bare metal instance. i. Select **Check the Initialization Configuration** from the drop-down list in the upper-left corner of the tab. ii. Configure the following parameters and click **Next**.

| Parameter | Description |
|---|---|
| Region ID | The name of the region in which the current environment resides. |
| HSW Name | The name of the vSwitch to be checked in instance management. |

If the specified values are invalid, click **Re-enter** in the lower part of the tab and configure the parameters again. iii. Click **Check** to check the initial configuration of the vSwitch.

**Check route configurations**

In O&M emergency scenarios, you can use this feature to locate abnormal operations and check whether the route configurations of a bare metal instance are valid. You can use this operation to locate the exception and scan the HSW after a bare metal instance fails to be added. This feature checks only whether the route configurations of a bare metal instance are valid. No operation is performed on the bare metal instance. i. Select **Check the Route Configuration** from the drop-down list in the upper-left corner of the tab. ii. Configure the following parameters and click **Next**.

| Parameter | Description |
|---|---|
| Region ID | The name of the region in which the current environment resides. |
| Bare Metal Name | The name of the bare metal instance that was applied for or released in a VPC. It uniquely identifies the bare metal instance within a region. |
| AccessKey ID | The AccessKey ID and AccessKey secret of the organization, which can be obtained from the Organizations page of the Apsara Uni-manager Management Console based on the organization to which the VPC belongs. For more information, see Manage the AccessKey pairs of an organization in Apsara Uni-manager Management Console User Guide. |
| AccessKey Secret |   |

If the specified values are invalid, click **Re-enter** in the lower part of the tab and configure the parameters again. iii. Click **Check** to check the route configurations.

**Display the information about a bare metal network gateway**

In O&M emergency scenarios, you can use this feature to check the gateway of a vSwitch. This operation is only for emergency scenarios in which bare metal networks are unavailable. The feature only checks the gateway information of vSwitches. It does not perform operations on bare metal instances. i. Select **Display the Information of Bare Metal Network Gateways** from the dropdown list in the upper-left corner of the tab. ii. Configure the following parameters and click **Next**.

| Parameter | Description |
|---|---|
| Region ID | The name of the region in which the current environment resides. |
| vSwitch ID | The ID of the vSwitch. You can obtain the vSwitch ID from the VPC console. |
| AccessKey ID | The AccessKey ID and AccessKey secret of the organization, which can be obtained from the Organizations page of the Apsara Uni-manager Management Console based on the organization to which the VPC belongs. For more information, see Manage the AccessKey pairs of an organization in Apsara Uni-manager Management Console User Guide. |
| AccessKey Secret |   |

If the specified values are invalid, click **Re-enter** in the lower part of the tab and configure the parameters again. iii. Click **Check** to check the information about the bare metal network gateway.

**Upgrade single-RR deployment to double-RR deployment**

In O&M emergency scenarios, you can use this feature to upgrade single-RR deployment to double-RR deployment.

**Warning**

This operation may affect your business. Unauthorized operations are prohibited. Configuration changes must be performed under the guidance of technical support. i. Select **Change Single-RR Deployment to Double-RR Deployment** from the dropdown list in the upper-left corner of the tab. ii. Configure the following parameters and click **Submit**.

| Parameter | Description |
|---|---|
| Region ID | The name of the region in which the current environment resides. |
| Existing RR Device Name | The name of RR device that you want to upgrade. |
| New RR Device Name | The name of the new RR device that you want to use. |

**History of changing single-RR deployment to double-RR**

**deployment**

You can view the history of changing single-RR deployment to double-RR deployment to obtain the up-to-date status of your RR device. i. Select **History of Changing Single-RR Deployment to Double-RR Deployment** from the drop-down list in the upper-left corner of the tab. ii. You can view the history of changing single-RR deployment to double-RR deployment. Specify **Existing RR Device Name**, **New RR Device Name**, and **Request ID** to view the records of RR device upgrades that meet the filter conditions. iii. Find the record that you want to view and click **Details** in the **Actions** column to view the details of the record, such as the additional information and HTTP status code.

**Associate a vSwitch with an ECR**

**Warning**

This operation is only for emergency scenarios and must be performed under the guidance of R&D engineers. Otherwise, normal business operations may be affected. i. Select **vSwitch Bound to Private Line Gateway** from the drop-down list in the upperleft corner of the tab. ii. Configure the following parameters and click **Next**.

| Parameter | Description |
|---|---|
| Region ID | The name of the region in which the current environment resides. |
| vSwitch ID | The ID of the vSwitch. You can obtain the vSwitch ID from the VPC console. |
| AccessKey ID | The AccessKey ID and AccessKey secret of the organization, which can be obtained from the Organizations page of the Apsara Uni- manager Management Console based on the organization to which the VPC belongs. For more information, see Manage the AccessKey pairs of an organization in Apsara Uni-manager Management Console User Guide. |
| AccessKey Secret |   |
| Name of Border Gateway 1 | The name of ECR 1 to which the bare metal instance is connected. On the Private Line Management tab, specify a VPC ID and computing access gateway name and click Search. Then, view the value in the Name of Private Line Gateway 1 column. |
| Source IP Address that Probes Gateway 1 | The source IP address of ECR 1. On the Private Line Management tab, specify a VPC ID and computing access gateway name and click Search. Then, view the value in the Source IP Address that Probes Gateway 1 column. |
| Name of Border Gateway 2 | The name of ECR 2 to which the bare metal instance is connected. On the Private Line Management tab, specify a VPC ID and computing access gateway name and click Search. Then, view the value in the Source IP Address that Probes Gateway 2 column. |
| Source IP Address that Probes Gateway 2 | The source IP address of ECR 2. On the Private Line Management tab, specify a VPC ID and computing access gateway name and click Search. Then, view the value in the Source IP Address that Probes Gateway 2 column. |

If the specified values are invalid, click **Re-enter** in the lower part of the tab and configure the parameters again. iii. Check whether the parameter configurations are valid. If yes, click **Confirm**. The system starts to apply the configurations. After the configurations are applied, the **Result: Successful** message appears. If not, click **Back to Modify** to configure the parameters again.

**Disassociate a vSwitch from an ECR**

**Warning**

This operation is only for emergency scenarios and must be performed under the guidance of R&D engineers. Otherwise, normal business operations may be affected. i. Select **vSwitch Unbound from Private Line Gateway** from the drop-down list in the upper-left corner of the tab. ii. Configure the following parameters and click **Next**.

| Parameter | Description |
|---|---|
| Region ID | The name of the region in which the current environment resides. |
| vSwitch ID | The ID of the vSwitch. You can obtain the vSwitch ID from the VPC console. |
| AccessKey ID | The AccessKey ID and AccessKey secret of the organization, which can be obtained from the Organizations page of the Apsara Uni- manager Management Console based on the organization to which the VPC belongs. For more information, see Manage the AccessKey pairs of an organization in Apsara Uni-manager Management Console User Guide. |
| AccessKey Secret |   |

If the specified values are invalid, click **Re-enter** in the lower part of the tab and configure the parameters again. iii. Check whether the parameter configurations are valid. If yes, click **Confirm**. The system starts to apply the configurations. After the configurations are applied, the **Result: Successful** message appears. If not, click **Back to Modify** to configure the parameters again.

## 3 Networking products

### 3.1 CGW O&M

By default, the **CGW O&M** module is hidden in the navigation pane. If you need to perform O&M operations on CGW clusters, you can modify the corresponding menu settings by referring to **User permissions** > **Menu Management** in Apsara Unimanager Operations Console User Guide.

#### 3.1.1 CGW cluster management

**Procedure**

1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
3. In the left-side navigation pane, choose **Network Services** > **CGW O&M** > **CGW Cluster**
**Management**.
4. On the CGW Cluster Management page, select a region from the **Region** drop-down list.
The zones and cluster topology in the selected region are displayed in the **Zone List** and
**Cluster Topology** sections.
Only x86-based physical machines can be managed.
5. Find the zone that you want to manage and click **Set Secondary Zone** in the **Actions**
column. You can perform this operation on zones for which the secondary zone is not configured.
6. In the Set Secondary Zone dialog box, select a secondary zone from the **Secondary Zone**
drop-down list and click **OK**. The cluster that you select as the secondary zone must have the same architecture and reside in the same region as the current cluster. The secondary zone that you select cannot be the secondary zone of another zone.

**What to do next**

**Remove a secondary zone**

You can perform this operation on zones for which the secondary zone is configured.
1. Find the zone that you want to manage and click **Remove Secondary Zone** in the
**Actions** column.
2. In the message that appears, click **OK**.

**View the change history of a zone**

1. Find the zone that you want to manage and click **View Change History** in the **Actions**
column.
2. In the View Change History dialog box, view the change history of the zone.
3. Find the change record that you want to manage and click **View details** in the **Operation**
column. On the **Execution Details** page, view detailed information. For more information, see Execution history.

#### 3.1.2 CGW management

## 4 Traffic visualization

The Traffic Visualization module can monitor physical and virtual networks in the cloud platform, and analyze real-time and historical traffic in the networks. This module also analyzes traffic by virtual network, public network, and border physical network and generates visualized charts. You can also troubleshoot issues based on the traffic data or monitored traffic metrics. By default, the Traffic Visualization module is not displayed. To use this module, perform the following operations: Log on to the Apsara Uni-manager Operations Console. In the top navigation bar, choose More > **User Authorities**. In the left-side navigation pane, click **Menu Management**. On the Menu management page, modify the menu settings to display the Traffic Visualization module.

### 4.1 Visual settings

Before you use traffic visualization, you must configure items such as analyzers, collection rules, and scenarios to collect, process, and analyze traffic based on your business requirements.

**Workflow**

The following flowchart shows how to initialize traffic visualization.
1. Create an analyzer and an analysis port. For more information, see Manage analysis
devices.
2. Create a collection rule. For more information, see Manage collection rules.
3. Create an analysis scenario. For more information, see Manage scenarios.

**Manage analysis devices**

Analysis devices include analyzers and analysis ports. The collection and analysis of traffic depend on the analysis devices. Before you collect and analyze traffic, you must create the required analysis devices.

**Usage notes**

An **analyzer**, also known as a network performance monitor (NPM), refers to a device that performs traffic analysis. The following types of analyzers are supported: NPM physical machines and NPM central control machines. An **analysis port**refers to the traffic collection port of an NPM device. Traffic is received on the port for collection and analysis.

**Procedure**

1. Log in to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
3. In the left-side navigation pane, choose **Traffic Visualization** > **Visual Settings**.
4. On the **System Management** page, click the **Analyze Device Management** tab. On this
tab, you can perform operations that are described in the following table.

| Section | Operation | Description |
|---|---|---|
|   | Create an analyzer | i. In the Analyzer management section, click Add analyzer above the analyzer list. |

| Analyzer management |   | ii. In the Add analyzer panel, configure the parameters and click OK. Zone: the zone in which you want to create an analyzer. Analyzer name: the name of the analyzer. The name can be up to 32 characters in length and can contain letters, digits, and underscores. It cannot start with a digit. Analyzer role: the role that the NPM device plays. Valid values: NPM physical machine: collects and processes traffic. NPM central control machine: displays traffic analysis results. |
|---|---|---|
|   |   | Galaxy Security Gateway: preferentially forwards traffic to the traffic gateway when you configure virtual private cloud (VPC) traffic mirroring rules. Manage IP addresses: the IP address of the NPM device. Username: the username that is used to log in to the NPM device. Password: the password that is used to log in to the NPM device. Serial Number: the serial number of the NPM device. Portal: the web page URL of the NPM central control |
|   | machine, which is used for daily O&M and management of the NPM device. After an analyzer is created, a portal for the analyzer is automatically generated by the system and can be viewed in the analyzer list. Analyzer description: the description of the analyzer. |   |

|   | View an analyzer | i. In the analyzer list of the Analyzer management section, you can view information about an analyzer, including Device ID, Analyzer name, Zone, Manage IP addresses, Authorization Status, Running status, Role, Description, Serial Number, Portal, Creation date, and Modified At. ii. Find the analyzer that you want to view and clickD etails in the Actions column. In the Details panel, view the details of the analyzer. |
|---|---|---|
|   | Modify an analyzer | i. In the analyzer list of the Analyzer management section, find the analyzer that you want to modify and click Edit in the Actions column. ii. In the Edit analyzer panel, modify the parameters and click OK. For more information about the parameters, see Create an analyzer. Note The Analyzer role parameter cannot be modified. |
|   | Delete an analyzer | Important If an analyzer is associated with an analysis port, you cannot delete the analyzer. If an analyzer is associated with a collection rule, you cannot delete the analyzer. i. In the analyzer list of the Analyzer management section, find the analyzer that you want to delete and click Delete in the Actions column. ii. In the message that appears, click OK. |
|   |   | Note Before you create an analysis port, make sure that an analyzer is created. i. In the Analysis Port Management section, click Add an analysis Port above the analysis port list. |

|   |   | ii. In the Add an analysis Port panel, configure the parameters and click OK. |
|---|---|---|
| Analysis Port Management | Create an analysis port | Analysis port name: the name of the analysis port. The name can be up to 32 characters in length and can contain letters, digits, and underscores. It cannot start with a digit. Analyzer name: the name of the analyzer that you want to use. Analyzer physical interface name: the physical interface of the analyzer. Analysis Port Type: the type of the analysis port. Valid values: VPC Physical ACK ALL Analysis port IP: the IP address of the analysis port. Standard IPv4 address is supported. Description: the description of the analysis port. |

|   | View an analysis port | i. In the analysis port list of the Analysis Port Management section, you can view information about an analysis port, including No., Analysis port name, Analyzer name, Analyzer physical network port name, Analysis Port Type, Analysis port IP, Description, and Creation date. ii. Find the analysis port that you want to view and clickD etails in the Actions column. In the Details panel, view the details of the analysis port. |
|---|---|---|
|   | Modify an analysis port | i. In the analysis port list of the Analysis Port Management section, find the analysis port that you want to modify and click Edit in the Actions column. ii. In the Edit analysis Port panel, modify the parameters and click OK. For more information about the parameters, see Create an analysis port. Note The Analyzer name and Analyzer physical interface name parameters cannot be modified. |
| 9 | > Document Version: 2026031 |   |

|   | Delete an analysis port | Important If an analysis port is associated with a collection rule, you cannot delete the analysis port. i. In the analysis port list of the Analysis Port Management section, find the analysis port that you want to delete and click Delete in the Actions column. ii. In the message that appears, click OK. |
|---|---|---|

**Manage collection rules**

A collection rule defines the data source and analysis mode of traffic. The analysis devices specified in a collection rule collect and analyze traffic based on the collection rule.

**Prerequisites**

Before you create a collection rule, make sure that an analyzer and an analysis port are created. For more information, see Manage analysis devices.

**Procedure**

1. Log in to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
3. In the left-side navigation pane, choose **Traffic Visualization** > **Visual Settings**.
4. On the **System Management** page, click the **Collection Rule Management** tab. On this
tab, you can perform operations that are described in the following table.

| Operation | Description |
|---|---|
|   | i. Click Add collection rules above the collection rule list. |

| Create a collection rule | ii. In the Add collection rules panel, configure the parameters and click OK. For more information about the parameters, see Collection rule parameters. |
|---|---|
| View a collection rule | In the collection rule list, you can view information about a collection rule, including Rule ID, Collection rule name, Zone, Data source type, Data source host device, Data source port, VPC ID, Data Source Port ID, SLB ID, ACK Cluster ID, Flow direction, Traffic analysis mode, Analyzer name, Analysis port name, Analysis Port VLAN ID, Status, Description, Creation date, and Modified At. |

| Retry a collection rule | Note If the Status of a collection rule is other than Failed, you can retry the collection rule. i. In the collection rule list, find the collection rule that you want to retry and click Retry in the Actions column. ii. In the panel that appears, configure the parameters and clickO K. |
|---|---|
| Modify a collection rule | Note If the Status of a collection rule is Effective, or if the Status is Failed and the failure is caused by insufficient resources, you can edit the collection rule. i. In the collection rule list, find the collection rule that you want to modify and click Edit in the Actions column. ii. In the Edit collection rules panel, modify the parameters and click OK. For more information about the parameters, see Collection rule parameters. Note If the Data source type parameter is set to Elastic network card, you can modify the Zone, Rule name, Display VPC Image Filtering Rules, SLB Instance, and Description parameters. If the Data source type parameter is set to Physical switch, you can modify the Zone, Rule name, and Description parameters. If the Data source type parameter is set to ACK container, you can modify the Rule name and ACK Cluster ID parameters. |
| Delete a collection rule | Important If a collection rule is associated with an analysis scenario, you cannot delete the collection rule. i. In the collection rule list, find the collection rule that you want to delete and click Delete in the Actions column. ii. In the message that appears, click OK. |

**Collection rule parameters**

| Parameter | Description |
|---|---|
| Zone | Select a zone for the collection rule. |
| Rule name | Enter a name for the collection rule. |

| Data source type | Select the type of the data source. By default, Physical switch is selected. Valid values: Elastic network card: collects traffic from elastic network interfaces (ENIs). Physical switch: collects traffic from physical switches. ACK container: collects traffic from Container Service for Kubernetes (ACK) containers. |
|---|---|
| Traffic analysis mode | Select a mode for traffic analysis. Only Traffic Image is supported. Traffic Image: specifies that all traffic is copied to the analysis port. Note This parameter is required if you set the Data source type parameter to Elastic network card or Physical switch. |
| Create Resource Type | Select the type of the resource to be created. OnlyS LB Instance is supported. Note This parameter is required if you set the Data source type parameter to ACK container. |
| SLB Type (ACK container selected) | Select the purpose of the SLB instance to be created. Valid values: Data Channel: creates an SLB instance to connect the ACK cluster to the ACK traffic analysis port of the NPM device. This serves as a data channel to carry the ACK traffic. Signaling Channel: creates an SLB instance to connect the ACK cluster to the management port of the NPM device. This serves as a signal channel. Note This parameter is required if you set the Data source type parameter to ACK container. |

| AliUid/Level-1 Organization AliUid | Enter the Alibaba Cloud account ID of the level-1 organization for Cloud Gateway (CGW) for authorization. You can obtain the ID in the Apsara Uni- manager Operations Console. Note This parameter is required if you set the Data source type parameter to Elastic network card or ACK container. After authorization is complete, the system creates a VPC image, creates a Server Load Balancer (SLB) instance, and then attaches an NPM server or traffic gateway to the backend servers of the SLB instance for tenants in the level-1 organization. |
|---|---|
| ACK Cluster ID | Enter the ID of an ACK cluster. Note This parameter is required if you set the Data source type parameter to ACK container. |
| Select VPC | Select the VPC to which your ENI or ACK cluster belongs. Note This parameter is required if you set the Data source type parameter to Elastic network card or ACK container. |
| Select a VSwitch | Select the vSwitch to which the ACK cluster belongs. Note This parameter is required if you set the Data source type parameter to ACK container. |
| Select ENI | Select the ENI that you want to use. Note This parameter is required if you set the Data source type parameter to Elastic network card. |

| Display VPC Image Filtering Rules | Select Show or Hide. Note This parameter is required if you set the Data source type parameter to Elastic network card. |
|---|---|
| Collection Policy for Inbound Rules | Select the collection action of the inbound rule. Valid values: Collect Network Traffic Network Traffic Is Not Collected Note This parameter is required if you set the Data source type parameter to Elastic network card and the Display VPC Image Filtering Rules parameter to Show. |
| Source CIDR Block of Inbound Traffic | Specify the source CIDR block of inbound traffic. You must enter a valid CIDR block. Note This parameter is required if you set the Data source type parameter to Elastic network card and the Display VPC Image Filtering Rules parameter to Show. |
| Source Port Range of Inbound Traffic | Enter the source port range of inbound traffic. Note This parameter is required if you set the Data source type parameter to Elastic network card and the Display VPC Image Filtering Rules parameter to Show. Valid values: 1 to 65535. Separate the first port and the last port with a forward slash (/). Examples: 1/200 and 80/80. If you set the protocol type to ALL or ICMP, all ports are available. In this case, you do not need to configure this parameter. |
| Protocol Type Used by Inbound Traffic to Be Mirrored | Select the protocol type that is used by inbound traffic to be mirrored. Valid values: ALL, ICMP, TCP, and UDP. Note This parameter is required if you set the Data source type parameter to Elastic network card and the Display VPC Image Filtering Rules parameter to Show. |

| Destination CIDR Block of Inbound Traffic | Specify the destination CIDR block of inbound traffic. You must enter a valid CIDR block. Note This parameter is required if you set the Data source type parameter to Elastic network card and the Display VPC Image Filtering Rules parameter to Show. |
|---|---|
| Destination Port Range of Inbound Traffic | Enter the destination port range of inbound traffic. Note This parameter is required if you set the Data source type parameter to Elastic network card and the Display VPC Image Filtering Rules parameter to Show. Valid values: 1 to 65535. Separate the first port and the last port with a forward slash (/). Examples: 1/200 and 80/80. If you set the protocol type to ALL or ICMP, all ports are available. In this case, you do not need to configure this parameter. |
| Collection Policy for Outbound Rules | Select the collection action of the outbound rule. Valid values: Collect Network Traffic Network Traffic Is Not Collected Note This parameter is required if you set the Data source type parameter to Elastic network card and the Display VPC Image Filtering Rules parameter to Show. |
| Source CIDR Block of Outbound Traffic | Specify the source CIDR block of outbound traffic. You must enter a valid CIDR block. Note This parameter is required if you set the Data source type parameter to Elastic network card and the Display VPC Image Filtering Rules parameter to Show. |
| Source Port Range of Outbound Traffic | Enter the source port range of outbound traffic. Note This parameter is required if you set the Data source type parameter to Elastic network card and the Display VPC Image Filtering Rules parameter to Show. Valid values: 1 to 65535. Separate the first port and the last port with a forward slash (/). Examples: 1/200 and 80/80. If you set the protocol type to ALL or ICMP, all ports are available. In this case, you do not need to configure this parameter. |

| Protocol Type Used by Outbound Traffic to Be Mirrored | Select the protocol type that is used by outbound traffic to be mirrored. Valid values: ALL, ICMP, TCP, and UDP. Note This parameter is required if you set the Data source type parameter to Elastic network card and the Display VPC Image Filtering Rules parameter to Show. |
|---|---|
| Destination CIDR Block of Outbound Traffic | Specify the destination CIDR block of outbound traffic. You must enter a valid CIDR block. Note This parameter is required if you set the Data source type parameter to Elastic network card and the Display VPC Image Filtering Rules parameter to Show. |
| Destination Port Range of Outbound Traffic | Enter the destination port range of outbound traffic. Note This parameter is required if you set the Data source type parameter to Elastic network card and the Display VPC Image Filtering Rules parameter to Show. Valid values: 1 to 65535. Separate the first port and the last port with a forward slash (/). Examples: 1/200 and 80/80. If you set the protocol type to ALL or ICMP, all ports are available. In this case, you do not need to configure this parameter. |
| SLB Type (Elastic network card selected) | You can select Use Existing SLB Instance or Create SLB Instance for this parameter. Note This parameter is required if you set the Data source type parameter to Elastic network card. If you select Create SLB Instance, the system automatically creates an SLB instance. |
| SLB Instance | Select an existing SLB instance. Note This parameter is required if you set the Data source type parameter to Elastic network card and the SLB Type parameter to Use Existing SLB Instance. |

| SLB Backend Device Name | Specify an analyzer for SLB backend collection. This parameter is available only if you set the Data source type parameter to Elastic network card or ACK container. Note This parameter is required if you set the Data source type parameter to Elastic network card and the SLB Type parameter to Create SLB Instance, or if you set the Data source type parameter to ACK container. |
|---|---|
| Analysis Port Name of SLB Backend Device | Specify an analysis port for SLB backend collection. Note This parameter is required if you set the Data source type parameter to Elastic network card and the SLB Type parameter to Create SLB Instance, or if you set the Data source type parameter to ACK container. |
| Data source host device | Select the host device of the physical switch. Note This parameter is required if you set the Data source type parameter to Physical switch. |
| Port name of the data source host device | Select a port for the physical switch host device based on the data source host device that you select. Note This parameter is required if you set the Data source type parameter to Physical switch. |
| Data Source Port ID | The value is automatically matched and displayed based on the data source host device and the port name of the data source host device that you select. Note This parameter is required if you set the Data source type parameter to Physical switch. |

| Analyzer Name | Select the analyzer that you want to use to collect traffic. Note This parameter is required if you set the Data source type parameter to Physical switch. |
|---|---|
| Analysis Port Name | Select the analysis port that you want to use to collect traffic. Note This parameter is required if you set the Data source type parameter to Physical switch. |
| Analysis Port VLAN ID | Enter the VLAN ID of the analysis port. Note This parameter is required if you set the Data source type parameter to Physical switch. |
| Description | Enter a description for the collection rule. Note This parameter is required if you set the Data source type parameter to Elastic network card or Physical switch. |

**Manage scenarios**

You can associate different collection rules with different analysis scenarios based on your business requirements.

**Prerequisites**

Before you create an analysis scenario, make sure that collection rules are created. For more information, see Manage collection rules.

**Procedure**

1. Log in to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
3. In the left-side navigation pane, choose **Traffic Visualization** > **Visual Settings**.
4. On the **System Management** page, click the **Scenario Management** tab. On this tab,
you can perform operations that are described in the following table.

| Operation | Description |
|---|---|
| Create an analysis scenario | i. Click Create an analysis scenario above the analysis scenario list. ii. In the Add scenario panel, configure the parameters and click OK. Zone: the zone in which you want to create an analysis scenario. Scene name: the name of the analysis scenario. The name can be up to 32 characters in length and can contain letters and digits. Network Type: the network type of the analysis scenario. Valid values: VPC: the virtual network. BORDER: the border physical network. Collection rules: the one or more collection rules that you want to associate with the analysis scenario. You can select multiple collection rules. Description: the description of the analysis scenario. |

| View an analysis scenario | i. In the analysis scenario list, you can view information about an analysis scenario. ii. Find the analysis scenario that you want to view and clickD etails in the Actions column. In the Details panel, view the details of the analysis scenario. |
|---|---|

| Modify an analysis scenario | i. In the analysis scenario list, find the analysis scenario that you want to modify and click Edit in the Actions column. ii. In the panel that appears, modify the analysis scenario parameters and click OK. For more information about the parameters, see Create an analysis scenario. Note The Network Type parameter cannot be modified. |
|---|---|
| Delete an analysis scenario | i. In the analysis scenario list, find the analysis scenario that you want to delete and click Delete in the Actions column. ii. In the message that appears, click OK. |

**Network Resource List**

You can view all the SLB instances that are created in the traffic visualization module.

**Procedure**

1. Log in to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
3. In the left-side navigation pane, choose **Traffic Visualization** > **Visual Settings**.
4. On the **System Management** page, click the **Network Resource List** tab. On this tab,
view the network resource information in the following columns: **Zone**, **Resource ID**,
**Resource Value**, **Resource Type**, **VpcId**, **Resource Usage**, **Resource Owner**, and
**Created At**.
