---
title: "Alibaba Cloud Apsara Stack V3.18.3 CloudMonitor User Guide 20250304"
product_version: "V3.18.3"
doc_version: "20250304"
pdf_pages: 155
source_pdf: "Alibaba Cloud Apsara Stack V3.18.3 CloudMonitor User Guide 20250304.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/V3.18.3/%E4%BA%91%E7%9B%91%E6%8E%A7CMS/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.3%20CloudMonitor%20User%20Guide%2020250304.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes+edge-junk)
---

# Alibaba Cloud Apsara Stack V3.18.3 CloudMonitor User Guide 20250304

## Table of Contents

- 1 Overview
- 2 Overview
- 3 Host monitoring
  - 3.1 Install the CloudMonitor agent
  - 3.2 Monitor processes
- 4 Cloud service monitoring
  - 4.1 Metrics
    - 4.1.1 Elastic computing
      - 4.1.1.1 ECS
      - 4.1.1.2 BMCP nodes
      - 4.1.1.3 BMCP containers
    - 4.1.2 Database services
      - 4.1.2.1 ApsaraDB RDS
      - 4.1.2.2 ApsaraDB RDS (New)
      - 4.1.2.3 PolarDB
      - 4.1.2.4 PolarDB databases that use local SSDs
      - 4.1.2.5 PolarDB-X 2.0
        - 4.1.2.5.1 Compute nodes of PolarDB-X 2.0
        - 4.1.2.5.2 Data nodes of PolarDB-X 2.0
      - 4.1.2.6 PolarDB-X 1.0
      - 4.1.2.7 ApsaraDB for MongoDB (Old)
      - 4.1.2.8 ApsaraDB for MongoDB (New)
      - 4.1.2.9 Tair (Redis OSS-compatible) (Old)
      - 4.1.2.10 Tair (Redis OSS-compatible) (New)
      - 4.1.2.11 DTS
    - 4.1.3 Storage and CDN
      - 4.1.3.1 NAS
      - 4.1.3.2 OSS
      - 4.1.3.3 Tablestore
    - 4.1.4 Network
      - 4.1.4.1 NAT Gateway
      - 4.1.4.2 SLB
      - 4.1.4.3 EIP
      - 4.1.4.4 VPN Gateway
      - 4.1.4.5 DNS
    - 4.1.5 Application services
      - 4.1.5.1 API Gateway
    - 4.1.6 Middleware services
      - 4.1.6.1 ApsaraMQ for RocketMQ
    - 4.1.7 Big data
      - 4.1.7.1 Stream Computing (Blink)
      - 4.1.7.2 DataHub
    - 4.1.8 Security (Apsara Stack Security)
      - 4.1.8.1 Tenant-side bastion hosts
      - 4.1.8.2 Vulnerability scanner engines
  - 4.2 Manage cloud service monitoring
- 5 Alert service
  - 5.1 Alert history
  - 5.2 Alert rules
    - 5.2.1 Create an alert rule
    - 5.2.2 Manage alert rules
  - 5.3 Alert templates
    - 5.3.1 Common alerting templates
    - 5.3.2 Create an alert template
    - 5.3.3 Manage alert templates
  - 5.4 Use the initiative alerting feature
- 6 Statistical analysis
  - 6.1 Sort monitoring data
- 7 Event monitoring
  - 7.1 System events
    - 7.1.1 System events of cloud services
    - 7.1.2 View system events
    - 7.1.3 Create a system event-triggered alert rule
    - 7.1.4 Manage system event-triggered alert rules
  - 7.2 Report custom events
- 8 Application group
  - 8.1 Create an application group
  - 8.2 Manage application groups
  - 8.3 Availability monitoring
    - 8.3.1 Create an availability monitoring task
    - 8.3.2 Manage availability monitoring tasks
    - 8.3.3 Status codes
- 9 Download a report
- 10 Namespaces
  - 10.1 Time series metrics
  - 10.2 System events
    - 10.2.1 Event monitoring metrics of cloud services
    - 10.2.2 View system event metrics
- 11 Monitor service availability

## 1 Overview

CloudMonitor provides an out-of-the-box all-in-one enterprise-grade monitoring solution for you to monitor resources on Apsara Stack..

**Background information**

CloudMonitor supports the cloud service monitoring, host monitoring, alerting, statistical analysis, event monitoring, application group, report export, namespace, and service availability monitoring features. You can use CloudMonitor to collect data on the monitoring metrics of various cloud services, such as Elastic Compute Service (ECS), Server Load Balancer (SLB), Object Storage Service (OSS), and Simple Log Service. The metrics include event-based metrics and custom metrics. CloudMonitor helps you implement comprehensive and efficient monitoring. You can improve system service availability and reduce the O&M costs of IT infrastructure.

**Usage notes**

> **Important:** You can view the business data of CloudMonitor based on different dimensions. To do so, select an organization, a resource set, and a region in the top navigation bar of the CloudMonitor console.
> Do not perform operations in the root organization.

## 2 Overview

**Monitoring overview**

CloudMonitor provides an overview of your cloud resources. You can monitor the resource usage and status of your cloud services. You can also receive and resolve alerts at the earliest opportunity to ensure the availability of your applications. The following sections are displayed on the Overview page in CloudMonitor: The cloud product that is alarming, Alarm Rules, Event alarm, Alarm History, and Cloud product monitoring.
1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Products** > **Migration and O&M Management** > **O&M**
**and Monitoring** > **CloudMonitor**.
3. In the left-side navigation pane, click **Overview**.
4. On the**Overview**page, click the**Monitoring Overview**tab to view the monitoring
overview.

| Module | Description |
|---|---|
| The cloud product that is alarming | This section displays the number of alerts from cloud services that are supported by CloudMonitor and for which alerting is enabled. You can click View Details to go to the Alarm History page to view the alert details. |

| Alarm Rules | This section displays the numbers of alert rules in theA larm in progress, Insufficient data, and Normal states. Note An alert rule in the Insufficient data state may be generated in the following scenarios: The cloud service does not report data of the specified metric. The cloud service instance is deleted. The cloud service instance is missing or is not created in the Logstore of Simple Log Service. In this case, further troubleshooting is required. You can click View Details to go to the Alarm Rules page to view the details of alert rules. |
|---|---|
| Event alarm | This section displays the status of system events and event-triggered alerts for cloud services. This helps you troubleshoot business exceptions in an efficient manner. You can click View Details to go to the System Events page to view the alert details. |
| Alarm History | This section displays the detailed records of recent alerts from cloud services that are supported by CloudMonitor and for which alerting is enabled. You can click View Details to go to the Alarm History page to view the alert details. |
| Cloud product monitoring | CloudMonitor automatically collects the statistics of cloud service instances and alerts within the current Apsara Stack account. You can click the cloud service name to go to the corresponding monitoring page and view the monitoring chart and alert rules of each instance. To view the alert rules of the cloud service, click the icon. To view the monitoring data of the cloud service, click the icon. |

**Governance detection**

The governance detection feature analyzes the resource instance metrics and alert rules in the current resource set and organization, evaluates and diagnoses the validity of metrics and alerts, and then provides suggestions. This feature allows you to fix issues with a few clicks.
1. On the**Overview**page, click the**Governance detection**tab to view the governance
detection information.

| Module | Description |
|---|---|
| Governance detection | In the Governance detection section, you can click Detect Now or Re-detection. Note If no governance detection is performed, Detect Now is displayed. If a governance detection is performed, Re-detection is displayed. The latest detection results are also displayed. |

| Detection details | If an anomaly is detected, click View Details and Governance Guidelines to the right of the detection item. In the DETECTION DETAILS panel, you can view information, such as the detection mechanism, detection range, and governance objects. Indicator Validity Detection ECS host plug-in status check: Checks whether all plug-ins of Elastic Compute Service (ECS) instances are running. No data alarm rule detection: Checks whether no-data alert is enabled for at least one instance of a cloud service in the current resource set and organization to monitor the metric data existence for all metrics of the cloud service. No data indicator detection: Checks whether all metrics of monitored cloud services have data and the data can be queried. Alarm Validity Detection Continuous alarm rule detection: Checks whether an alert rule has been in the alerting state within the previous 24 hours. Alarm Validity Test: Checks whether the callback URL of an alert rule fails to be queried within the previous 24 hours. Invalid alarm rule detection: Checks whether cloud service resources have invalid alert rules. Cloud product alarm coverage detection: Checks whether no alert rules are configured for cloud service resources. Note By default, if the initiative alerting feature is enabled for all instances of a cloud service in the level-1 organization, all instances of the cloud service are configured with alert rules. If the alert rules of a cloud service take effect only for a specific resource set, all instances of the cloud service in the specified resource set within the current Apsara Stack account are configured with the alert rules. If at least one metric of a resource instance is configured with an alert rule, the resource instance is configured with the alert rule. |
|---|---|

## 3 Host monitoring

After the CloudMonitor agent is installed on your Elastic Compute Service (ECS) instances, CloudMonitor can collect various monitoring data of metrics about the operating system that the ECS instances run. You can configure alert rules for the metrics to reduce monitoring costs.
**Easy-to-use agent**: After the CloudMonitor agent is installed on your ECS instances,
CloudMonitor can collect various monitoring data of metrics about the operating system that the ECS instances run.
**Various metrics**: Host monitoring supports various metrics about the operating system,
GPUs, inbound and outbound traffic, disk reads and writes, processes, cloud disks, and Azure VMware Solution (AVS) network.
**Business-specific process monitoring**: Host monitoring collects the CPU utilization,
memory usage, and number of opened files for active processes. This helps you monitor the resource usage of your ECS instances.
**Flexible alerting**: Host monitoring allows you to manage ECS instances across regions and
configure alert rules by application group. This reduces the costs of monitoring management.

### 3.1 Install the CloudMonitor agent

You can install the CloudMonitor agent on Elastic Compute Service (ECS) instances to collect the monitoring data of operating systems.

**Procedure**

1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Products** > **Migration and O&M Management** > **O&M**
**and Monitoring** > **CloudMonitor**.
3. In the left-side navigation pane, click **Host Monitoring**.
4. On the **Host Monitoring** page, select the ECS instances for which you want to install or
upgrade the agent and click **Bulk install or upgrade plug-ins** in the lower-left corner of the instance list.

**Note**

You can only install the plug-in of CloudMonitor for ECS instances that run the **Linux** and **Windows** operating systems.
5. In the message that appears, click **OK**.

**Note**

The installation or upgrade process takes approximately five minutes. After the agent changes from the **In Installation** state to the **In operation** state, the CloudMonitor agent is installed or upgraded.

### 3.2 Monitor processes

CloudMonitor provides the process monitoring feature to help you collect information about the active processes of Elastic Compute Service (ECS) instances during a period of time. You can collect the following information: CPU utilization, memory usage, and the number of opened files. If you add a process keyword, you can obtain the number of processes that match the keyword.

**Prerequisites**

The CloudMonitor agent is installed on the ECS instances. For more information, see Install the CloudMonitor agent.

**Background information**

CloudMonitor identifies the top five processes with the highest CPU utilization at 1-minute intervals and records the CPU utilization, memory usage, and the number of opened files in these processes. CPU utilization and memory usage of a process: You can check the output of the **top** command in the Linux operating system to understand the two metrics. Number of opened files in a process: You can check the output of the **lsof** command in the Linux operating system to understand this metric. CloudMonitor collects the CPU utilization of only the top five CPU-intensive processes. The following issues may occur: If a process occupies multiple CPU cores, the collected CPU utilization may exceed 100%. This is because CloudMonitor collects the total CPU utilization of the process on all the occupied CPU cores. If the top five CPU-intensive processes change during the period specified in your query, the process list displays all the processes that have ranked top five over the specified period. The time displayed in the list indicates when the processes last ranked top five. CloudMonitor collects the CPU utilization, memory usage, and number of opened files for a process only when the process is among the top five CPU-intensive processes. If a process has not stayed in the top five within the period specified in your query, its monitoring data is displayed as dispersed data points in the monitoring charts. The density of the data points indicates the activity level of the process on the host. Examples: In the following figures, the data points for the wrapper process are sparse and discontinuous in the monitoring charts. This is because the wrapper process did not continuously rank top five with the highest CPU utilization during the specified period. In the following figures, the data points for the java process are dense and continuous in the monitoring charts. This is because the java process continuously ranked top five with the highest CPU utilization during the specified period.

**Add or remove system processes**

You can monitor the number of processes on ECS instances and collect the number of key processes to obtain the availability of the key processes.

**Procedure**

1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Products** > **Migration and O&M Management** > **O&M**
**and Monitoring** > **CloudMonitor**.
3. In the left-side navigation pane, click **Host Monitoring**.
4. On the **Host Monitoring** page, find the ECS instance that you want to manage and click its
name.
5. On the details page of the ECS instance, click the **Process Monitoring** tab. In the **Host**
**Process Number (value)** section, click **Add system processes**.
**Add a system process**: In the **Add system processes** panel, enter a process name
and click **Submission**.
**Remove a system process**: In the **Add system processes** panel, find the system
process that you want to remove and click **Delete** in the **Operation** column.

**Example**

The following processes are running on an ECS instance:

**/usr/bin/java -Xmx2300m -Xms2300m org.apache.catalina.startup.Bootstrap**

**/usr/bin/ruby**

**nginx -c /etc/nginx/nginx.conf**

You can add the following process keywords to obtain the monitoring results: ruby: One process matches this keyword by name. Therefore, the number of processes that match this keyword is 1. nginx: One process matches this keyword by name and parameter. Therefore, the number of processes that match this keyword is 1. /usr/bin: Two processes match this keyword by path. Therefore, the number of processes that match this keyword is 2. apache.catalina: One process matches this keyword by parameter. Therefore, the number of processes that match this keyword is 1. nginx.conf: One process matches this keyword by parameter. Therefore, the number of processes that match this keyword is 1. -c: One process matches this keyword by parameter. Therefore, the number of processes that match this keyword is 1.

**Create an alert rule for process monitoring**

After you add a process for monitoring, you can configure alert rules for processes under monitoring. When the number of processes exceeds the specified threshold, the alert contacts can receive alert notifications.

**Procedure**

1. In the left-side navigation pane, click **Host Monitoring**.
2. On the Host monitoring page, click **Create an alert rule**.
3. In the **Add Rule Description** panel that appears, select the
**(Agent)process.count_processname** metric from the **Metric Name** drop-down list, and
configure other parameters based on your business requirements. If multiple processes run on the host and the number of processes that match each process keyword varies, you can go back to the Create Alert Rule panel and click **Add Rule**
**Description** to configure alert rules for the processes one by one. For more information
about how to configure parameters in an alert rule, see Create an alert rule.
4. Click **OK**.

## 4 Cloud service monitoring

CloudMonitor automatically retrieves the resources of cloud services that belong to the current Apsara Stack account. You can view the monitoring charts of each cloud service. You can also configure alert rules to monitor resources. If an alert is triggered based on an alert rule, CloudMonitor sends an alert notification to you. This way, you are notified about the status of your resources at the earliest opportunity. The following table describes the cloud services that can be monitored by using CloudMonitor.

> **Note:** For information about the metrics of each cloud service, see the "Metrics" topic.

| Category | Cloud service |
|---|---|
| Elastic computing | Elastic Compute Service (ECS) Elastic High Performance Computing (E-HPC) |
| Database services | ApsaraDB RDS ApsaraDB for Redis PolarDB-X 2.0 PolarDB-X 1.0 AnalyticDB for PostgreSQL AnalyticDB for MySQL V3.0 ApsaraDB for MongoDB Data Transmission Service (DTS) |
| Storage and CDN | Cloud Storage Gateway (CSG) Apsara File Storage NAS (NAS) Object Storage Service (OSS) Tablestore |
| Networking | NAT Gateway Server Load Balancer (SLB) VPN Gateway Elastic IP Address (EIP) Apsara Stack DNS |
| Application services | API Gateway |

| Middleware | ApsaraMQ ApsaraMQ for Kafka |
|---|---|
| Big data | MaxCompute Realtime Compute for Apache Flink Realtime Compute DataHub Elasticsearch on Kubernetes Hologres |
| Security | Database Audit Static Data Masking and Watermarking Tenant-side Bastionhost Privileged Access Management |

### 4.1 Metrics

CloudMonitor checks the availability of services based on their metrics. You can configure alert rules and notification policies for these metrics to understand the status and performance of monitored service instances at the earliest opportunity.

#### 4.1.1 Elastic computing

##### 4.1.1.1 ECS

This topic describes the metrics supported by Elastic Compute Service (ECS).

**Basic metrics**

Set the **Namespace** parameter to **acs_ecs_dashboard**. Set the **Period** parameter to an integer multiple of 60. Default value: **60**. Unit: seconds.

> **Note:** The metrics described in the following table are collected from the virtual host layer and are slightly different from metrics collected in the operating system.

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| (ECS) CPU Utilization | % | CPUUtilization | userId and instanceId | The CPU utilization. |

| (ECS)InternetInRa te(Classic Network) | Bit/s | InternetInRate | userId and instanceId | The rate of inbound traffic over the Internet. |
|---|---|---|---|---|
| (ECS)IntranetInRa te | Bit/s | IntranetInRate | userId and instanceId | The rate of inbound traffic over the intranet. |
| (ECS)InternetOut Rate(Classic Network) | Bit/s | InternetOutRate | userId and instanceId | The rate of outbound traffic over the Internet. |
| (ECS)IntranetOut Rate | Bit/s | IntranetOutRate | userId and instanceId | The rate of outbound traffic over the intranet. |
| (ECS)DiskReadBP S | Bytes/s | DiskReadBPS | userId and instanceId | The number of bytes read from all disks per second. |
| (ECS)DiskWriteBP S | Bytes/s | DiskWriteBPS | userId and instanceId | The number of bytes written to all disks per second. |
| (ECS)DiskReadIO PS | Count/s | DiskReadIOPS | userId and instanceId | The number of read I/O operations per second (IOPS) of all disks. |
| (ECS)DiskWriteIO PS | Count/s | DiskWriteIOPS | userId and instanceId | The number of write IOPS of all disks. |

**Operating system-related metrics**

Set the **Namespace** parameter to **acs_ecs_dashboard**. Set the **Period** parameter to an integer multiple of 15. Default value: **15**. Unit: seconds.

> **Note:** To collect operating system-related metrics of ECS instances, you must install a monitoring plug-in.
> To install a monitoring plug-in, perform the following operations: In the left-side navigation pane of the CloudMonitor console, click Cloud Service Monitoring. On the Cloud product monitoring page, click ECS. On the **Host monitoring** page, select the instances that you want to monitor and click **Bulk install or upgrade plug-ins** below the instance list.
> Metric data is displayed in the monitoring chart in 5 to 10 minutes after the monitoring plug-in is installed.

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| (Agent)cpu.total | % | cpu total _ | userId and instanceId | The CPU utilization. |
| (Agent)memory.u sed.utilization | % | memory usedutil _ ization | userId and instanceId | The memory usage. |
| (Agent)load.15m | N/A | load 15m _ | userId and instanceId | The system load in the last 15 minutes. Note This metric is not available for Windows. |
| (Agent)load.1m | N/A | load 1m _ | userId and instanceId | The system load in the last 1 minute. Note This metric is not available for Windows. |

| (Agent)load.5m | N/A | load 5m _ | userId and instanceId | The system load in the last 5 minutes. Note This metric is not available for Windows. |
|---|---|---|---|---|
| Host.diskusage.ut ilization | % | diskusage utiliza _ tion | userId, instanceId, and device | The disk usage. |
| (Agent)fs.inode.u tilization device _ | % | fs inodeutilizatio _ n | userId, instanceId, and device | The inode usage. Note This metric is available only for Linux. |
| (Agent)disk.read. bps device _ | Bytes/s | disk readbytes _ | userId, instanceId, and device | The number of bytes read from the disk per second. |
| (Agent)disk.read.i ops device _ | Count/s | disk readiops _ | userId, instanceId, and device | The number of read IOPS of the disk. |
| (Agent)disk.write. bps device _ | Bytes/s | disk writebytes _ | userId, instanceId, and device | The number of bytes written to the disk per second. |
| (Agent)disk.write. iops device _ | Count/s | disk writeiops _ | userId, instanceId, and device | The number of write IOPS of the disk. |
| (Agent)network.t cp.connection st _ ate | Count | net tcpconnectio _ n | userId, instanceId, and state | The number of TCP connections in each state. |

| (Agent)process.e xpend pid _ | N/A | process.expend | userId, instanceId, name, and pid | The detailed statistical metrics for the top 5 processes. |
|---|---|---|---|---|
| (Agent)process.c ount processnam _ e | Count | process.number | userId, instanceId, and processName | The number of matched processes. |
| io saturation | % | disk io util _ _ | userId, instanceId, and device | The I/O saturation. |
| Agent(zombie pr _ ocess number) _ | Count | zombieProcessNu mber | userId and instanceId | The total number of zombie processes. |
| Agent(total proce _ ss number) _ | Count | totalProcessNum ber | userId and instanceId | The total number of processes. |
| Agent(swap parti _ tion usage) _ | % | swapUtilization | userId and instanceId | The usage of the swap partition. |
| Agent(networkou t drop ratio) _ _ | % | networkout drop _ ratio _ | userId, instanceId, and device | The loss rate of packets that are sent by network interface controllers (NICs). |
| Agent(networkou t error ratio) _ _ | % | networkout error _ ratio _ | userId, instanceId, and device | The sending error rate of NICs. |
| Agent(networkin _ drop ratio) _ | % | networkin drop r _ _ atio | userId, instanceId, and device | The loss rate of packets that are received by NICs. |
| Agent(networkin _ error ratio) _ | % | networkin error r _ _ atio | userId, instanceId, and device | The receiving error rate of NICs. |

**GPU-related metrics**

Set the **Namespace** parameter to **acs_ecs_dashboard**. Set the **Period** parameter to an integer multiple of 60. Default value: **60**. Unit: seconds.

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| (Agent)gpu.deco der.utilization gp _ uid | % | gpu decoder utili _ _ zation | userId, instanceId, and gpuId | The decoder usage of a GPU. |
| (Agent)gpu.enco der.utilization gp _ uid | % | gpu encoder utili _ _ zation | userId, instanceId, and gpuId | The encoder usage of a GPU. |
| (Agent)gpu.temp erature gpuid _ | °C | gpu gpu temper _ _ ature | userId, instanceId, and gpuId | The GPU temperature. |
| (Agent)gpu.used utilization gpuid _ | % | gpu gpu usedutil _ _ ization | userId, instanceId, and gpuId | The GPU utilization. |
| (Agent)gpu.mem ory.free.space gp _ uid | Bytes | gpu memory fre _ _ espace | userId, instanceId, and gpuId | The idle video memory of a GPU. |
| (Agent)gpu.mem ory.free.utilizatio n gpuid _ | % | gpu memory fre _ _ eutilization | userId, instanceId, and gpuId | The percentage of the idle video memory of a GPU. |
| (Agent)gpu.mem ory.used.space g _ puid | Bytes | gpu memory use _ _ dspace | userId, instanceId, and gpuId | The used video memory of a GPU. |
| gpu memory use _ _ dutilization | % | gpu memory use _ _ dutilization | userId, instanceId, and gpuId | The video memory usage of a GPU. |
| (Agent)gpu.powe r.readingspowerd raw gpuid _ | W | gpu power readi _ _ ngs power draw _ _ | userId, instanceId, and gpuId | The GPU power. |

**Disk-related metrics**

Set the **Namespace** parameter to **acs_ecs_dashboard**. Set the **Period** parameter to an integer multiple of 60. Default value: **60**. Unit: seconds.

| Console-based metric | Uni t | API-based metric | Dimension | Description |
|---|---|---|---|---|
| (Agent) Percentage of cloud disk usage | % | DiskSerialUsePercent | userId, instanceId, and id serial _ | The percentage of used disk capacity. |

**Network-related metrics**

Set the **Namespace** parameter to **acs_ecs_dashboard**. Set the **Period** parameter to an integer multiple of 60. Default value: **60**. Unit: seconds.

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| Inline NIC bandwidth | Bit/s | networkin rate avs _ _ | userId and instanceId | The number of bits that the NIC receives per second. |
| Outgoing NIC bandwidth | Bit/s | networkout rate avs _ _ | userId and instanceId | The number of bits that the NIC sends per second. |
| Number of network card incoming packets | Count/s | networkin packages _ avs _ | userId and instanceId | The number of packets that the NIC receives per second. |
| Number of outgoing network card packets | Count/s | networkout package _ s avs _ | userId and instanceId | The number of packets that the NIC sends per second. |
| Number of packets with network card inbound error | Count/s | networkin errorpack _ ages avs _ | userId and instanceId | The number of error packets that the NIC receives per second. |
| Network card outbound error packets | Count/s | networkout errorpac _ kages avs _ | userId and instanceId | The number of error packets that the NIC sends per second. |

| Number of network connections | Count | net tcpconnection a _ _ vs | userId and instanceId | The number of connections. |
|---|---|---|---|---|
| Enter VPC- broadband | Bit/s | VPC PublicTP Intern _ _ etInRate | userId and instanceId | The number of bits that the virtual private cloud (VPC) receives per second. |
| Outbound VPC- broadband | Bit/s | VPC PublicTP Intern _ _ etOutRate | userId and instanceId | The number of bits that the VPC sends per second. |
| ipv6 packet bit | Bit | ipv6 tx bytes sum _ _ _ | userId and instanceId | The number of bits of an outbound IPv6 packet. |
| ipv6 packet receiving bits | Bit | ipv6 rx bytes sum _ _ _ | userId and instanceId | The number of bits of an inbound IPv6 packet. |
| Number of ipv6 packages | Count | ipv6 tx packets su _ _ _ m | userId and instanceId | The number of outbound IPv6 packets. |
| Number of ipv6 packets received | Count | ipv6 rx packets su _ _ _ m | userId and instanceId | The number of inbound IPv6 packets. |
| Number of packets lost to ipv6 outbound security group | Count | ipv6 tx acl error su _ _ _ _ m | userId and instanceId | The number of outbound IPv6 packets dropped from the security group. |
| Number of packets lost to the security group in the direction of ipv6 | Count | ipv6 rx acl error su _ _ _ _ m | userId and instanceId | The number of inbound IPv6 packets dropped from the security group. |
| North-south traffic ipv6 statistics contract number | Count | ipv6 tx igw packets _ _ _ avg _ | userId and instanceId | The number of IPv6 packets that are sent in the north-south traffic. |

| North-south traffic ipv6 statistics number of packets received | Count | ipv6 rx igw packets _ _ _ avg _ | userId and instanceId | The number of IPv6 packets that are received in the north-south traffic. |
|---|---|---|---|---|
| North-South Traffic ipv6 Statistics Packet Bits | Bit/s | ipv6 tx igw bytes a _ _ _ _ vg | userId and instanceId | The number of bits of IPv6 packets that are sent per second in the north- south traffic. |
| North-South Traffic ipv6 Statistics Packet Receiving Bits | Bit/s | ipv6 rx igw bytes a _ _ _ _ vg | userId and instanceId | The number of bits of IPv6 packets that are received per second in the north-south traffic. |

##### 4.1.1.2 BMCP nodes

This topic describes the metrics for nodes in the Bare Metal Computing Power (BMCP) platform. Set the **Namespace** parameter to **acs_bms**. Set the **Period** parameter to an integer multiple of 60. Default value: **60**. Unit: seconds.

**Basic metrics**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| NODE CPU USA _ _ GE | % | NODE CPU USAG _ _ E | instanceId | The CPU utilization. |
| NODE MEM US _ _ AGE | % | NODE MEM USA _ _ GE | instanceId | The memory usage. |
| NODE DISK US _ _ AGE | % | NODE DISK USA _ _ GE | instanceId | The disk usage. |
| NODE LOAD1 _ | value | NODE LOAD1 _ | instanceId | The system load in the last minute. |
| NODE LOAD5 _ | value | NODE LOAD5 _ | instanceId | The system load in the last 5 minutes. |

| NODE LOAD15 _ | value | NODE LOAD15 _ | instanceId | The system load in the last 15 minutes. |
|---|---|---|---|---|
| TCP ESTAB _ | Count | TCP ESTAB _ | instanceId | The number of TCP connections. |
| NETWORK RX _ | MB/s | NETWORK RX _ | instanceId | The outbound bandwidth. |
| NETWORK TX _ | MB/s | NETWORK TX _ | instanceId | The inbound bandwidth. |

**GPU-related metrics**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| GPU TEMP _ | °C | GPU TEMP _ | instanceId | The GPU temperature. |
| GPU POWER US _ _ AGE | W | GPU POWER USA _ _ GE | instanceId | The GPU power. |
| GPU USAGE _ | % | GPU USAGE _ | instanceId | The GPU utilization. |
| GPU ENC USAG _ _ E | % | GPU ENC USAGE _ _ | instanceId | The encoder utilization of the GPU. |
| GPU DEC USAG _ _ E | % | GPU DEC USAGE _ _ | instanceId | The decoder utilization of the GPU. |
| GPU FB USAGE _ _ | % | GPU FB USAGE _ _ | instanceId | The memory usage of the GPU frame buffer. |
| GPU SM CLOCK _ _ | MHz | GPU SM CLOCK _ _ | instanceId | The frequency of the GPU Streaming Multiprocessor (SM) clock. |
| GPU MEM CLOC _ _ K | MHz | GPU MEM CLOCK _ _ | instanceId | The frequency of the GPU memory clock. |

**RDMA-related metrics**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| rdma tx bytes _ _ | MB/s | rdma tx bytes _ _ | instanceId | The throughput sent over the Remote Direct Memory Access (RDMA) network. |
| rdma rx bytes _ _ | MB/s | rdma rx bytes _ _ | instanceId | The throughput received over the RDMA network. |
| rdma out of bu _ _ _ ffer | Count | rdma out of buff _ _ _ er | instanceId | The number of buffer overflows that occur in the RDMA network. |
| rdma out of se _ _ _ q | Count | rdma out of seq _ _ _ | instanceId | The number of out-of-order packets in the RDMA network. |
| rdma cqe error _ _ | Count | rdma cqe error _ _ | instanceId | The number of local completion queue entries (CQEs) with errors in the RDMA network. |
| rdma service m _ _ onitor rnr nak r _ _ _ etry err _ | Count | rdma service mo _ _ nitor rnr nak retr _ _ _ y err _ | instanceId | The number of Receiver Not Ready (RNR) Negative Acknowledgment (NAK) packets sent from the peer. |

##### 4.1.1.3 BMCP containers

This topic describes the metrics for containers in the Bare Metal Computing Power (BMCP) platform. Set the **Namespace** parameter to **acs_bmcp**. Set the **Period** parameter to an integer multiple of 60. Default value: **60**. Unit: seconds.

**Basic metrics**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| NODE CPU USA _ _ GE | % | NODE CPU USAG _ _ E | instanceId | The CPU utilization. |
| NODE MEM US _ _ AGE | % | NODE MEM USA _ _ GE | instanceId | The memory usage. |

| NODE DISK US _ _ AGE | % | NODE DISK USA _ _ GE | instanceId | The disk usage. |
|---|---|---|---|---|
| NODE LOAD1 _ | Value | NODE LOAD1 _ | instanceId | The system load in the last minute. |
| NODE LOAD5 _ | Value | NODE LOAD5 _ | instanceId | The system load in the last 5 minutes. |
| NODE LOAD15 _ | Value | NODE LOAD15 _ | instanceId | The system load in the last 15 minutes. |
| TCP ESTAB _ | Count | TCP ESTAB _ | instanceId | The number of TCP connections. |
| NETWORK RX _ | MB/s | NETWORK RX _ | instanceId | The outbound bandwidth. |
| NETWORK TX _ | MB/s | NETWORK TX _ | instanceId | The inbound bandwidth. |

**GPU-related metrics**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| GPU TEMP _ | °C | GPU TEMP _ | instanceId | The GPU temperature. |
| GPU POWER US _ _ AGE | W | GPU POWER USA _ _ GE | instanceId | The GPU power. |
| GPU USAGE _ | % | GPU USAGE _ | instanceId | The GPU utilization. |
| GPU ENC USAG _ _ E | % | GPU ENC USAGE _ _ | instanceId | The encoder utilization of the GPU. |
| GPU DEC USAG _ _ E | % | GPU DEC USAGE _ _ | instanceId | The decoder utilization of the GPU. |
| GPU FB USAGE _ _ | % | GPU FB USAGE _ _ | instanceId | The memory usage of the GPU frame buffer. |

**RDMA-related metrics**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| rdma tx bytes _ _ | MB/s | rdma tx bytes _ _ | instanceId | The throughput sent over the Remote Direct Memory Access (RDMA) network. |
| rdma rx bytes _ _ | MB/s | rdma rx bytes _ _ | instanceId | The throughput received over the RDMA network. |
| rdma out of bu _ _ _ ffer | Count | rdma out of buff _ _ _ er | instanceId | The number of buffer overflows that occur in the RDMA network. |
| rdma out of se _ _ _ q | Count | rdma out of seq _ _ _ | instanceId | The number of out-of-order packets in the RDMA network. |
| rdma cqe error _ _ | Count | rdma cqe error _ _ | instanceId | The number of local completion queue entries (CQEs) with errors in the RDMA network. |
| rdma service m _ _ onitor rnr nak r _ _ _ etry err _ | Count | rdma service mo _ _ nitor rnr nak retr _ _ _ y err _ | instanceId | The number of Receiver Not Ready (RNR) Negative Acknowledgment (NAK) packets sent from the peer. |

#### 4.1.2 Database services

##### 4.1.2.1 ApsaraDB RDS

This topic describes the metrics supported by ApsaraDB RDS. By default, an old link is used for ApsaraDB RDS. The period of data collection is 60 to 300 seconds. Set the **Namespace** parameter to **acs_rds_dashboard**. Set the **Period** parameter to an integer multiple of 60 in the range of 60 to 300). Default value: **60**. Unit: seconds. ApsaraDB RDS supports four types of engines: MySQL, SQL Server, PolarDB O, and PostgreSQL.

**ApsaraDB RDS for MySQL**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|

| ConnectionsUtiliz ation | % | ConnectionUsage | userId and instanceId | The connection utilization. |
|---|---|---|---|---|
| CPU Utilization | % | CpuUsage | userId and instanceId | The CPU utilization. |
| DiskUtilization | % | DiskUsage | userId and instanceId | The disk usage. |
| IOPSUtilization | % | IOPSUsage | userId and instanceId | The number of I/O requests per second. |
| MemoryUtilizatio n | % | MemoryUsage | userId and instanceId | The memory usage. |
| NetworkInRate | Bit/s | MySQL NetworkI _ nNew | userId and instanceId | The inbound traffic to the ApsaraDB RDS for MySQL instance per second. |
| NetworkOutRate | Bit/s | MySQL NetworkO _ utNew | userId and instanceId | The outbound traffic from the ApsaraDB RDS for MySQL instance per second. |
| MySQL QPS _ | Count/s | MySQL QPS _ | userId and instanceId | The number of queries per second (QPS) for the ApsaraDB RDS for MySQL instance. |
| Docker Cpu Usage | % | DockerCpuUsage | userId and instanceId | The CPU utilization of the Docker container. |

**ApsaraDB RDS for SQL Server**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|

| ConnectionsUtiliz ation | % | ConnectionUsage | userId and instanceId | The connection utilization. |
|---|---|---|---|---|
| CPU Utilization | % | CpuUsage | userId and instanceId | The CPU utilization. |
| DiskUtilization | % | DiskUsage | userId and instanceId | The disk usage. |
| IOPSUtilization | % | IOPSUsage | userId and instanceId | The number of I/O requests per second. |
| NetworkInRate | Bit/s | SQLServer Netw _ orkInNew | userId and instanceId | The inbound traffic to the ApsaraDB RDS for SQL Server instance per second. |
| NetworkOutRate | Bit/s | SQLServer Netw _ orkOutNew | userId and instanceId | The outbound traffic from the ApsaraDB RDS for SQL Server instance per second. |

**ApsaraDB RDS for PolarDB O**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| ConnectionsUtiliz ation | % | ConnectionUsage | userId and instanceId | The connection utilization. |
| CPU Utilization | % | CpuUsage | userId and instanceId | The CPU utilization. |
| DiskUtilization | % | DiskUsage | userId and instanceId | The disk usage. |
| IOPSUtilization | % | IOPSUsage | userId and instanceId | The number of I/O requests per second. |

| MemoryUtilizatio n | % | MemoryUsage | userId and instanceId | The memory usage. |
|---|---|---|---|---|

**ApsaraDB RDS for PostgreSQL**

**ApsaraDB RDS for PostgreSQL instances that use local SSDs**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| ConnectionsUtiliz ation | % | ConnectionUsag e | userId and instanceId | The connection utilization. |
| CPU Utilization | % | CpuUsage | userId and instanceId | The CPU utilization. |
| DiskUtilization | % | DiskUsage | userId and instanceId | The disk usage. |
| IOPSUtilization | % | IOPSUsage | userId and instanceId | The number of I/O requests per second. |
| MemoryUtilizatio n | % | MemoryUsage | userId and instanceId | The memory usage. |

**ApsaraDB RDS for PostgreSQL instances that use cloud disks**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| Average active connections per CPU PG cloud _ disk | Count | ActiveConnectio ns | userId and instanceId | The average number of active connections per CPU. |
| Inode Usage PG _ Disk | % | InodeUsage | userId and instanceId | The inode usage. |
| Read-only synchronization delay PG cloud _ disk | Seconds | ReadLag | userId and instanceId | The synchronization latency of the read-only instance. |

| Database Age PG Disk _ | xids | DBAge | userId and instanceId | The age of the database. |
|---|---|---|---|---|
| Read-only Stream replication state pg cloud _ disk | Value | StreamingStatus | userId and instanceId | The stream replication status of the read-only instance. Valid values: 0: disconnected. 1: normal. |
| Pg connection _ usage | % | conn usage _ | userId and instanceId | The connection utilization. |
| PG CPU usage _ | % | cpu usage _ | userId and instanceId | The CPU utilization. |
| PG IOPS usage _ | % | iops usage _ | userId and instanceId | The IOPS usage. |
| Pg disk space _ usage | % | local fs size usa _ _ _ ge | userId and instanceId | The disk usage. |
| PG Memory _ Usage | % | mem usage _ | userId and instanceId | The memory usage. |

##### 4.1.2.2 ApsaraDB RDS (New)

This topic describes the metrics supported by ApsaraDB RDS (New). ApsaraDB RDS supports a new link. Data is collected at 60-second intervals. Set the **Namespace** parameter to **acs_rds_dashboard**. The default value of the **Period** parameter is **60**. Unit: seconds. ApsaraDB RDS (New) supports three types of engines: MySQL, PolarDB O, and PostgreSQL.

**ApsaraDB RDS for MySQL**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| Connection Usage (New) | % | ConnectionUsage new _ | userId and instanceId | The connection utilization. |

| CPU usage (new) | % | CpuUsage new _ | userId and instanceId | The CPU utilization. |
|---|---|---|---|---|
| Disk usage (new) | % | DiskUsage new _ | userId and instanceId | The disk usage. |
| IOPS usage (new) | % | IOPSUsage new _ | userId and instanceId | The number of I/O requests per second. |
| Memory usage (new) | % | MemoryUsage n _ ew | userId and instanceId | The memory usage. |
| MySQL Network inflow bandwidth (new) | Bit/s | MySQL NetworkI _ nNew new _ | userId and instanceId | The inbound traffic to the ApsaraDB RDS for MySQL instance per second. |
| MySQL Network outflow bandwidth (new) | Bit/s | MySQL NetworkO _ utNew new _ | userId and instanceId | The outbound traffic from the ApsaraDB RDS for MySQL instance per second. |
| MySQL queries per second (new) | Count/s | MySQL QPS new _ _ | userId and instanceId | The number of queries per second (QPS) for the ApsaraDB RDS for MySQL instance. |
| DataDelay | Seconds | DataDelay | userId and instanceId | The latency between primary and secondary instances. |
| RWDelay (New) | Seconds | RWDelay | userId, instanceId, and slave | The read and write latency. |
| ThreadsConnecte d | Count | ThreadsConnecte d | userId and instanceId | The number of thread connections. |

| ThreadsRunning | Count | ThreadsRunning | userId and instanceId | The number of active threads. |
|---|---|---|---|---|
| SlowQueriesPs | Count | SlowQueriesPs | userId and instanceId | The number of slow QPS. |
| Total Wait Time for Row Locks (New) | Milliseconds | InnodbRowLockW aits | userId and instanceId | The total wait time for row locks. |
| Average Wait Time for Row Locks (New) | Milliseconds | InnodbRowLockTi meAvg | userId and instanceId | The average wait time for row locks. |
| Row Lock Waits (New) | Count | InnodbRowLockW aits | userId and instanceId | The number of wait times for row locks. |
| Total Number of Connections (New) | Count | TotalConnections | userId and instanceId | The total number of connections. |

**ApsaraDB RDS for PolarDB O**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| Connection Usage (New) | % | ConnectionUsage new _ | userId and instanceId | The connection utilization. |
| CPU usage (new) | % | CpuUsage new _ | userId and instanceId | The CPU utilization. |
| Disk usage (new) | % | DiskUsage new _ | userId and instanceId | The disk usage. |
| IOPS usage (new) | % | IOPSUsage new _ | userId and instanceId | The number of I/O requests per second. |
| Memory usage (new) | % | MemoryUsage n _ ew | userId and instanceId | The memory usage. |

| PPAS Primary/Standby Disconnect | Count | PPAS Replication _ Num | userId and instanceId | The number of disconnections between primary and secondary ApsaraDB RDS for PPAS instances. |
|---|---|---|---|---|
| PPAS primary/standby delay | Seconds | PPAS Replication _ Lag | userId and instanceId | The latency between primary and secondary ApsaraDB RDS for PPAS instances. |

**ApsaraDB RDS for PostgreSQL**

**ApsaraDB RDS for PostgreSQL instances that use local SSDs**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| Connection Usage (New) | % | ConnectionUsag e new _ | userId and instanceId | The connection utilization. |
| CPU usage (new) | % | CpuUsage new _ | userId and instanceId | The CPU utilization. |
| Disk usage (new) | % | DiskUsage new _ | userId and instanceId | The disk usage. |
| IOPS usage (new) | % | IOPSUsage new _ | userId and instanceId | The number of I/O requests per second. |
| Memory usage (new) | % | MemoryUsage n _ ew | userId and instanceId | The memory usage. |
| PG primary/standby disconnection | Count | PG ReplicationN _ um | userId and instanceId | The number of connections between primary and secondary ApsaraDB RDS for PostgreSQL instances. |

| PG primary/standby delay | Seconds | PG ReplicationLa _ g | userId and instanceId | The latency between primary and secondary ApsaraDB RDS for PostgreSQL instances. |
|---|---|---|---|---|

**ApsaraDB RDS for PostgreSQL instances that use cloud disks**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| Average number of active connections per CPU PG cloud _ disk (new) | Count | ActiveConnectio ns new _ | userId and instanceId | The average number of active connections per CPU. |
| Pg connection _ usage | % | conn usage _ | userId and instanceId | The connection utilization. |
| PG CPU usage _ | % | cpu usage _ | userId and instanceId | The CPU utilization. |
| PG IOPS usage _ | % | iops usage _ | userId and instanceId | The IOPS usage. |
| INODE usage PG _ cloud disk (new) | % | InodeUsage new _ | userId and instanceId | The inode usage. |
| Pg disk space _ usage | % | local fs size usa _ _ _ ge | userId and instanceId | The disk usage. |
| PG Memory _ Usage | % | mem usage _ | userId and instanceId | The memory usage. |
| Read-only synchronization delay PG cloud _ disk (new) | Seconds | ReadLag new _ | userId and instanceId | The synchronization latency of the read-only instance. |
| Database age PG cloud _ disk (new) | xids | DBAge new _ | userId and instanceId | The age of the database. |

| Read-only Stream Copy Status PG Cloud _ Disk (New) | Value | StreamingStatus new _ | userId and instanceId | The streaming replication status of the read-only instance. |
|---|---|---|---|---|
| Number of Primary/Seconda ry Connections (Value 0 indicates disconnected. Value 1 indicates connected.) | Count | PG ESSD Replic _ _ ationNum | userId and instanceId | The number of connections between primary and secondary ApsaraDB RDS for PostgreSQL instances. |
| PG cloud disk primary/sta _ ndby delay | Seconds | PG ESSD Replic _ _ ationLag | userId and instanceId | The latency between primary and secondary ApsaraDB RDS for PostgreSQL instances. |

##### 4.1.2.3 PolarDB

This topic describes the metrics supported by PolarDB. Set the **Namespace** paramter to **acs_polardb_dashboard**. Set the **Period** paramter to an integer multiple of 60. Default value: **60**. Unit: seconds.

**PolarDB for MySQL**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| (PolarDB-M) Connection Usage | % | ConnectionUsa ge new _ | userId and instanceId | The connection utilization. |
| (PolarDB-M) CPU usage | % | CpuUsage new _ | userId and instanceId | The CPU utilization. |
| (PolarDB-M) Memory Usage | % | MemoryUsage _ new | userId and instanceId | The memory usage. |
| Number of active connections | Count | Active Session _ new _ | userId and instanceId | The number of active connections. |

| Storage Engine IO throughput per second | Count/s | Iops throughou _ t new _ | userId and instanceId | The I/O throughput of the storage engine per second. |
|---|---|---|---|---|
| Storage engine IO times per second | Count/s | Mps new _ | userId and instanceId | The number of I/O operations of the storage engine per second. |
| IO times per second | Count/s | DataIo Ps new _ _ | userId and instanceId | The number of I/O operations per second. |
| Queries Ps new _ _ | Count/s | Queries Ps ne _ _ w | userId and instanceId | The number of queries per second (QPS). |
| Slow queries per second | Count/s | SlowQueries Ps _ new _ | userId and instanceId | The number of slow queries per second. |
| TPS | Count/s | Tps M _ | userId and instanceId | The number of transactions per second (TPS). |

**PolarDB O**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| (PolarDB-O)TPS | Count/s | Tps O _ | userId and instanceId | The TPS. |
| (PolarDB-O) database CPU usage | % | Cgroup Cpu To _ _ tal | userId and instanceId | The CPU utilization of the database. |
| Cgroup Mem Usage _ _ | % | Cgroup Mem U _ _ sage | userId and instanceId | The memory usage of the database. |
| (PolarDB-O) Connection Usage | % | Connection Rati _ o | userId and instanceId | The connection utilization. |
| (PolarDB-O) Connections | Count | Connections O _ | userId and instanceId | The number of connections. |
| (PolarDB-O) Active Connections | Count | Active Connecti _ ons | userId and instanceId | The number of active connections. |

| (PolarDB-O)PFS reads IOPS | Count | Pfsd Read Iops _ _ | userId and instanceId | The read IOPS of the Polar file system (PFS). |
|---|---|---|---|---|
| (PolarDB-O)PFS writes IOPS | Count | Pfsd Write Iops _ _ | userId and instanceId | The write IOPS of the PFS. |
| (PolarDB-O) Database Age | Count | Db Age _ | userId and instanceId | The age of the database. |
| (PolarDB-O) Local Disk Usage | % | Local Disk Usa _ _ ge | userId and instanceId | The local disk usage. |

##### 4.1.2.4 PolarDB databases that use local SSDs

This topic describes the metrics supported by PolarDB databases that use local SSDs. Set the **Namespace** parameter to **acs_polardblocal**. Set the **Period** parameter to an integer multiple of 60. Default value: **60**. Unit: seconds.

**PolarDB for MySQL**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| Connection Usage (New) | % | ConnectionUsag e new _ | userId and instanceId | The connection utilization. |
| CPU usage (new) | % | CpuUsage new _ | userId and instanceId | The CPU utilization. |
| Disk usage (new) | % | DiskUsage new _ | userId and instanceId | The disk usage. |
| IOPS usage (new) | % | IOPSUsage new _ | userId and instanceId | The IOPS usage. |
| Memory usage (new) | % | MemoryUsage _ new | userId and instanceId | The memory usage. |
| MySQL Network inflow bandwidth (new) | Bit/s | MySQL Network _ InNew new _ | userId and instanceId | The inbound traffic to the PolarDB for MySQL instance per second. |

| MySQL Network outflow bandwidth (new) | Bit/s | MySQL Network _ OutNew new _ | userId and instanceId | The outbound traffic from the PolarDB for MySQL instance per second. |
|---|---|---|---|---|
| MySQL queries per second (new) | Count/s | MySQL QPS ne _ _ w | userId and instanceId | The number of queries per second for the PolarDB for MySQL instance. |
| DataDelay | Seconds | DataDelay | userId and instanceId | The latency between primary and secondary instances. |
| RWDelay (New) | Seconds | RWDelay | userId, instanceId, and slave | The read and write latency. |
| Threads Connected | Count | ThreadsConnect ed | userId and instanceId | The number of thread connections. |
| ThreadsRunning | Count | ThreadsRunning | userId and instanceId | The number of active threads. |
| SlowQueriesPs | Count | SlowQueriesPs | userId and instanceId | The number of slow queries per second (QPS). |
| Total Wait Time for Row Locks (New) | Millisecon ds | InnodbRowLock Time | userId and instanceId | The total wait time for row locks. |
| Average Wait Time for Row Locks (New) | Millisecon ds | InnodbRowLock TimeAvg | userId and instanceId | The average wait time for row locks. |
| Row Lock Waits (New) | Count | InnodbRowLock Waits | userId and instanceId | The number of wait times for row locks. |
| Total Number of Connections (New) | Count | TotalConnection s | userId and instanceId | The total number of connections. |
| Average number of active MySQL connections | Count/s | MySQL ActiveS _ ession | userId and instanceId | The average number of active connections to the PolarDB for MySQL instance. |
| Innodb row lock cur _ _ _ rent waits _ | Count | Innodb row loc _ _ k current waits _ _ | userId and instanceId | The number of sessions waiting for row locks. |

| mdl lock session _ _ | Count | mdl lock sessio _ _ n | userId and instanceId | The number of connections blocked by the MDL lock. |
|---|---|---|---|---|
| lock deadlocks _ | Count | lock deadlocks _ | userId and instanceId | The number of deadlocks. |

**PolarDB for Oracle and PolarDB for PostgreSQL**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| Connection Usage (New) | % | ConnectionUsa ge new _ | userId and instanceId | The connection utilization. |
| CPU usage (new) | % | CpuUsage new _ | userId and instanceId | The CPU utilization. |
| Disk usage (new) | % | DiskUsage new _ | userId and instanceId | The disk usage. |
| IOPS usage (new) | % | IOPSUsage ne _ w | userId and instanceId | The IOPS usage. |
| Memory usage (new) | % | MemoryUsage _ new | userId and instanceId | The memory usage. |
| PPAS Primary/Standby Disconnect | Count | PPAS Replicatio _ nNum | userId and instanceId | The number of disconnections between primary and secondary ApsaraDB RDS for PPAS instances. |
| PPAS primary/standby delay | Seconds | PPAS Replicatio _ nLag | userId and instanceId | The latency between primary and secondary ApsaraDB RDS for PPAS instances. |
| PG ActiveConnectio _ nsPerCpu | Count | PG ActiveConn _ ectionsPerCpu | userId and instanceId | The average number of active connections per core to the PolarDB for Oracle Enterprise Edition database that uses local disks. |

| PG Database age _ | xids | PG DBAge _ | userId and instanceId | The age of the PolarDB for Oracle Enterprise Edition database that uses local SSDs. |
|---|---|---|---|---|
| PG SwellTime _ | Seconds | PG SwellTime _ | userId and instanceId | The period during which the PolarDB for Oracle Enterprise Edition database that uses local SSDs experiences storage bloat. |
| PG CheckpointLaten _ cyMB | MB | PG Checkpoint _ LatencyMB | userId and instanceId | The size of data written to the PolarDB for Oracle Enterprise Edition database that uses local SSDs with a delay during a checkpoint process. |
| PG InactiveSlots _ | Count | PG InactiveSlot _ s | userId and instanceId | The number of times that the replication slot is disconnected in the PolarDB for Oracle Enterprise Edition database that uses local SSDs. |
| PG ReplayLatencyIn _ MB | MB | PG ReplayLate _ ncyInMB | userId and instanceId | The size of data written to the PolarDB for Oracle Enterprise Edition database that uses local SSDs with a delay. |

##### 4.1.2.5 PolarDB-X 2.0

###### 4.1.2.5.1 Compute nodes of PolarDB-X 2.0

This topic describes the metrics for the compute nodes of PolarDB-X 2.0. Set the **Namespace** parameter to **acs_drds**. Set the **Period** parameter to an integer multiple of 60. Default value: **60**. Unit: seconds.

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| CPU usage | % | CPUUtilization | userId and instanceId | The CPU utilization. |

| Number of connections | Count | ConnectionCount | userId and instanceId | The total number of sessions. |
|---|---|---|---|---|
| Average number of logical requests per second | Count | LogicQPS | userId and instanceId | The number of requests per second. |
| Average Logical Response Time | Millisec onds | LogicRT | userId and instanceId | The average response time of logical requests. |
| Memory Usage | % | MemoryUtilization | userId and instanceId | The memory usage. |
| Network input | Bit/s | NetworkInputTraffi c | userId and instanceId | The inbound bandwidth. |
| Network output | Bit/s | NetworkOutputTra ffic | userId and instanceId | The outbound bandwidth. |
| Average number of physical requests per second | Count | PhysicsQPS | userId and instanceId | The physical queries per second (QPS). |
| Average Physical Response Time | Millisec onds | PhysicsRT | userId and instanceId | The physical response time. |
| Number of active sessions | Count | ThreadCount | userId and instanceId | The number of active threads. |
| Heap memory usage | % | HeapMemoryUsag e | userId and instanceId | The heap memory usage. |
| Log directory size | Bytes | LogSize | userId and instanceId | The size of the log directory. |
| Number of errors per second | Count | SecondErrorCount | userId and instanceId | The number of errors per second. |
| Physical slow SQL per second | Count | SecondPhysicalSql Count | userId and instanceId | The number of physical slow SQL QPS. |
| Slow requests per second | Count | SecondRequestCo unt | userId and instanceId | The number of slow queries per second. |

| spill directory size | Bytes | SpillSize | userId and instanceId | The size of the spill directory. |
|---|---|---|---|---|
| Temporary directory size | Bytes | TmpSize | userId and instanceId | The size of the temporary directory. |

###### 4.1.2.5.2 Data nodes of PolarDB-X 2.0

This topic describes the metrics for the data nodes of PolarDB-X 2.0. Set the **Namespace** parameter to **acs_rds_dashboard**. Set the **Period** parameter to an integer multiple of 60 in the range of 60 to 300. Default value: **60**. Unit: seconds.

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| Connection Usage (New) | % | ConnectionUsage n _ ew | userId and instanceId | The connection utilization. |
| CPU Utilization (New) | % | CpuUsage new _ | userId and instanceId | The CPU utilization. |
| Disk Usage (New) | % | DiskUsage new _ | userId and instanceId | The disk usage. |
| IOPS Usage (New) | % | IOPSUsage new _ | userId and instanceId | The number of I/O requests per second. |
| Memory Utilization (New) | % | MemoryUsage new _ | userId and instanceId | The memory usage. |
| Inbound Bandwidth of an ApsaraDB RDS for MySQL Instance (New) | Bit/s | MySQL NetworkInN _ ew new _ | userId and instanceId | The inbound traffic to the MySQL data node per second. |
| Outbound Bandwidth of an ApsaraDB RDS for MySQL Instance (New) | Bit/s | MySQL NetworkOut _ New new _ | userId and instanceId | The outbound traffic from the MySQL data node per second. |
| QPS of an ApsaraDB RDS for MySQL Instance (New) | Count/ s | MySQL QPS new _ _ | userId and instanceId | The number of queries per second (QPS) on the MySQL data node. |

##### 4.1.2.6 PolarDB-X 1.0

This topic describes the metrics supported by PolarDB-X 1.0. Set the **Namespace** parameter to **acs_polarx_drds**. Set the **Period** parameter to an integer multiple of 60. Default value: **60**. Unit: seconds.

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| CPU usage | % | CPUUtilization | useId and InstanceId | The CPU utilization. |
| Memory Usage | % | MemoryUtilizatio n | useId and InstanceId | The memory usage. |
| Network input | Bytes/s | NetworkInputTraf fic | useId and InstanceId | The inbound traffic. |
| Network output | Bytes/s | NetworkOutputTr affic | useId and InstanceId | The outbound traffic. |
| Average number of logical requests per second | Count | LogicQPS | useId and InstanceId | The average number of logical requests per second. |
| Average Logical Response Time | Millisec onds | LogicRT | useId and InstanceId | The average response time of logical requests. |
| Average number of physical requests per second | Count | PhysicsQPS | useId and InstanceId | The average number of physical requests per second. |
| Average Physical Response Time | Millisec onds | PhysicsRT | useId and InstanceId | The average response time of physical requests. |
| Number of connections | Count | ConnectionCount | useId and InstanceId | The total number of sessions. |
| Number of active sessions | Count | ThreadCount | useId and InstanceId | The number of active sessions. |

##### 4.1.2.7 ApsaraDB for MongoDB (Old)

This topic describes the metrics supported by ApsaraDB for MongoDB (Old). Set the **Namespace** parameter to **acs_mongodb**. Set the **Period** parameter to an integer multiple of 60. Default value: **60**. Unit: seconds.

**Basic metrics**

| Console-based metric | Unit | MetricName | Dimension | Description |
|---|---|---|---|---|
| CPU Utilization | % | CPUUtilization | userId, instanceId, and role | The CPU utilization. |
| MemoryUtilizatio n | % | MemoryUtilizatio n | userId, instanceId, and role | The memory usage. |
| DiskUtilization | % | DiskUtilization | userId, instanceId, and role | The disk usage. |
| IOPSUtilization | % | IOPSUtilization | userId, instanceId, and role | The IOPS usage. |
| Connection Usage | % | ConnectionUtiliza tion | userId, instanceId, and role | The connection utilization. |
| QPS | Count | QPS | userId, instanceId, and role | The number of queries per second (QPS). |
| UsedConnections | Count | ConnectionAmou nt | userId, instanceId, and role | The number of used connections. |

**Disk capacity-related metrics**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| InstanceUsedDisk Space | Bytes | InstanceDiskAmo unt | userId, instanceId, and role | The disk space occupied by the instance. |

| LogUsedDiskSpac e | Bytes | DataDiskAmount | userId, instanceId, and role | The disk space occupied by data. |
|---|---|---|---|---|
| Disk Space Occupied by Logs | Bytes | LogDiskAmount | userId, instanceId, and role | The disk space occupied by logs. |

**Network request-related metrics**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| IntranetIn | Bytes | IntranetIn | userId, instanceId, and role | The inbound traffic over the intranet. |
| IntranetOut | Bytes | IntranetOut | userId, instanceId, and role | The outbound traffic over the intranet. |
| Requests | Count | NumberRequests | userId, instanceId, and role | The number of requests. |

**Operation count-related metrics**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| OpCounters for Command | Count | OpCommand | userId, instanceId, and role | The number of Command operations. |
| OpCounters for Delete | Count | OpDelete | userId, instanceId, and role | The number of Delete operations. |
| OpCounters for Getmore | Count | OpGetmore | userId, instanceId, and role | The number of Getmore operations. |
| OpCounters for Insert | Count | OpInsert | userId, instanceId, and role | The number of Insert operations. |

| OpCounters for Query | Count | OpQuery | userId, instanceId, and role | The number of Query operations. |
|---|---|---|---|---|
| OpCounters for Update | Count | OpUpdate | userId, instanceId, and role | The number of Update operations. |

##### 4.1.2.8 ApsaraDB for MongoDB (New)

This topic describes the metrics supported by ApsaraDB for MongoDB (New). Set the **Namespace** parameter to **acs_mongodb**. Set the **Period** parameter to an integer multiple of 60. Default value: **60**. Unit: seconds.

**Basic metrics**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| CPUUtilization ne _ w | % | CPUUtilization ne _ w | userId, instanceId, and role | The CPU utilization. |
| MemoryUtilizatio n new _ | % | MemoryUtilizatio n new _ | userId, instanceId, and role | The memory usage. |
| Disk Usage (New) | % | DiskUtilization n _ ew | userId, instanceId, and role | The disk usage. |
| IOPSUtilization n _ ew | % | IOPSUtilization n _ ew | userId, instanceId, and role | The IOPS usage. |
| ConnectionUtiliza tion new _ | % | ConnectionUtiliza tion new _ | userId, instanceId, and role | The connection utilization. |
| Visits per second (new) | Count | QPS new _ | userId, instanceId, and role | The number of queries per second (QPS). |
| Connection Usage (New) | Count | ConnectionAmou nt new _ | userId, instanceId, and role | The number of used connections. |

| Current Total Connections (New) | Count | TotalConnections | userId, instanceId, and role | The total number of current connections. |
|---|---|---|---|---|

**Disk capacity-related metrics**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| The amount of disk space occupied by the instance (new) | Bytes | InstanceDiskAmo unt new _ | userId, instanceId, and role | The disk space occupied by the instance. |
| Amount of disk space occupied by data (new) | Bytes | DataDiskAmount new _ | userId, instanceId, and role | The disk space occupied by data. |
| The amount of disk space occupied by the log (new) | Bytes | LogDiskAmount _ new | userId, instanceId, and role | The disk space occupied by logs. |

**Network request-related metrics**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| Intranet Inflow (New) | Bytes | IntranetIn new _ | userId, instanceId, and role | The inbound traffic over the intranet. |
| Intranet outbound traffic (new) | Bytes | IntranetOut new _ | userId, instanceId, and role | The outbound traffic over the intranet. |
| Number of requests (new) | Count | NumberRequests new _ | userId, instanceId, and role | The number of requests. |

**Operation count-related metrics**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|

| Number of Command Operations (new) | Count | OpCommand ne _ w | userId, instanceId, and role | The number of Command operations. |
|---|---|---|---|---|
| Number of Delete operations (new) | Count | OpDelete new _ | userId, instanceId, and role | The number of Delete operations. |
| Number of Getmore operations (new) | Count | OpGetmore new _ | userId, instanceId, and role | The number of Getmore operations. |
| Number of Insert operations (new) | Count | OpInsert new _ | userId, instanceId, and role | The number of Insert operations. |
| Number of Query operations (new) | Count | OpQuery new _ | userId, instanceId, and role | The number of Query operations. |
| Number of Update operations (new) | Count | OpUpdate new _ | userId, instanceId, and role | The number of Update operations. |

**Basic metrics (Cluster Edition)**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| (Cluster) CPU usage | % | CPUUtilization new _ cluster _ | userId, instanceId, and role | The CPU utilization. |
| (Cluster Version) Memory Usage | % | MemoryUtilization _ new cluster _ | userId, instanceId, and role | The memory usage. |
| (Cluster Edition) Disk Usage | % | DiskUtilization ne _ w cluster _ | userId, instanceId, and role | The disk usage. |
| (Cluster version) IOPS usage | % | IOPSUtilization ne _ w cluster _ | userId, instanceId, and role | The IOPS usage. |
| (Cluster Edition) Connection Usage | % | ConnectionUtilizati on new cluster _ _ | userId, instanceId, and role | The connection utilization. |
| (Cluster Version) Visits Per Second | Count | QPS new cluster _ _ | userId, instanceId, and role | The QPS. |

| (Cluster Edition) Connection Usage | Count | ConnectionAmount new cluster _ _ | userId, instanceId, and role | The number of used connections. |
|---|---|---|---|---|
| (Cluster Edition) Total Number of Connections | Count | TotalConnections _ cluster | userId, instanceId, and role | The total number of current connections. |

**Disk capacity-related metrics (Cluster Edition)**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| (Cluster Edition) The amount of disk space occupied by the instance | Bytes | InstanceDiskAmoun t new cluster _ _ | userId, instanceId, and role | The disk space occupied by the instance. |
| (Cluster Edition) The amount of disk space occupied by data | Bytes | DataDiskAmount n _ ew cluster _ | userId, instanceId, and role | The disk space occupied by data. |
| (Cluster Edition) The amount of disk space occupied by logs | Bytes | LogDiskAmount ne _ w cluster _ | userId, instanceId, and role | The disk space occupied by logs. |

**Network request-related metrics (Cluster Edition)**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| (Cluster Version) Intranet Inflow | Bytes | IntranetIn new cl _ _ uster | userId, instanceId, and role | The inbound traffic over the intranet. |
| (Cluster Version) Intranet outbound traffic | Bytes | IntranetOut new _ _ cluster | userId, instanceId, and role | The outbound traffic over the intranet. |
| (Cluster Version) Number of Requests | Coun t | NumberRequests new cluster _ _ | userId, instanceId, and role | The number of requests. |

**Operation count-related metrics (Cluster Edition)**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| (Cluster Edition) Command Operation Times | Count | OpCommand _ new cluster _ | userId, instanceId, and role | The number of Command operations. |
| (Cluster version) Delete operations | Count | OpDelete ne _ w cluster _ | userId, instanceId, and role | The number of Delete operations. |
| (Cluster version) Getmore Operations | Count | OpGetmore n _ ew cluster _ | userId, instanceId, and role | The number of Getmore operations. |
| (Cluster version) Insert operations | Count | OpInsert new _ cluster _ | userId, instanceId, and role | The number of Insert operations. |
| (Cluster Version) Query Operation Times | Count | OpQuery new _ cluster _ | userId, instanceId, and role | The number of Query operations. |
| (Cluster Edition) Update Operation Times | Count | OpUpdate ne _ w cluster _ | userId, instanceId, and role | The number of Update operations. |

##### 4.1.2.9 Tair (Redis OSS-compatible) (Old)

This topic describes the metrics supported by Tair (Redis OSS-compatible) (Old). Set the **Namespace** parameter to **acs_kvstore**. Set the **Period** parameter to an integer multiple of 60. Default value: **60**. Unit: seconds.

| Console-based metric | Unit | Metric | Dimensions | Description |
|---|---|---|---|---|
| ConnectionsUtiliz ation | % | ConnectionUsage | userId and instanceId | The connection utilization. |
| CPU Utilization | % | CpuUsage | userId and instanceId | The CPU utilization. |
| Failed Operations | Count | FailedCount | userId and instanceId | The number of failed operations. |

| Cache Inbound Bandwidth | Bytes/s | IntranetIn | userId and instanceId | The inbound traffic over the intranet. |
|---|---|---|---|---|
| Inbound Bandwidth Usage | % | IntranetInRatio | userId and instanceId | The inbound bandwidth usage. |
| Cache Outbound Bandwidth | Bytes/s | IntranetOut | userId and instanceId | The outbound traffic over the intranet. |
| Outbound Bandwidth Usage | % | IntranetOutRatio | userId and instanceId | The outbound bandwidth usage. |
| MemoryUtilizatio n | % | MemoryUsage | userId and instanceId | The memory usage. |
| Used QPS | Count/s | UsedQPS | userId and instanceId | The number of used QPS. |

##### 4.1.2.10 Tair (Redis OSS-compatible) (New)

This topic describes the metrics supported by Tair (Redis OSS-compatible) (New). Set the **Namespace** parameter to **acs_kvstore**. Set the **Period** parameter to an integer multiple of 60. Default value: **60**. Unit: seconds.

**Standard Edition instances and Read/write splitting instances**

**of Tair (Redis OSS-compatible)**

> **Note:** Tair (Redis OSS-compatible) Standard Edition instances and Tair (Redis OSS-compatible) Read/write splitting instances share a set of metrics.

| Console- based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| Number of Connections Usage (Standard Edition) | % | StandardConnectionU sage | userId and instanceId | The connection utilization. |

| Incoming Bandwidth (Standard Edition) | Kbit/s | StandardIntranetIn | userId and instanceId | The inbound bandwidth. |
|---|---|---|---|---|
| Incoming Bandwidth Utilization (Standard Edition) | % | StandardIntranetInRat io | userId and instanceId | The inbound bandwidth utilization. |
| Outgoing Bandwidth (Standard Edition) | Kbit/s | StandardIntranetOut | userId and instanceId | The outbound bandwidth. |
| Outgoing Bandwidth Usage (Standard Edition) | % | StandardIntranetOutR atio | userId and instanceId | The outbound bandwidth utilization. |
| Memory Usage (Standard Edition) | % | StandardMemoryUsag e | userId and instanceId | The memory usage. |
| QPS usage (standard version) | % | StandardQPSUsage | userId and instanceId | The queries per second (QPS) usage. |
| CPU usage (standard edition) | % | StandardCpuUsage | userId and instanceId | The CPU utilization. |
| Average Visits Per Second (Standard Edition) | Count/s | StandardUsedQPS | userId and instanceId | The average QPS. |
| Total QPS (Standard Edition) | Count/s | StandardTotalQps | userId and instanceId | The total QPS. |
| Current Total Connections (Standard Edition) | Count | StandardTotalConnec tions | userId and instanceId | The total number of current connections. |

**Tair (Redis OSS-compatible) instances that use the cluster**

**architecture**

| Console- based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| Connection Usage (Cluster Edition) | % | ShardingConnec tionUsage | userId and instanceId | The connection utilization. |
| Incoming Bandwidth (Cluster Edition) | Kbit/s | ShardingIntranet In | userId and instanceId | The inbound bandwidth. |
| Outgoing Bandwidth (Cluster Edition) | Kbit/s | ShardingIntranet Out | userId and instanceId | The outbound bandwidth. |
| Incoming Bandwidth Usage (Cluster Edition) | % | ShardingIntranet InRatio | userId and instanceId | The inbound bandwidth utilization. |
| Outgoing Bandwidth Usage (Cluster Edition) | % | ShardingIntranet OutRatio | userId and instanceId | The outbound bandwidth utilization. |
| Memory Usage (Cluster Edition) | % | ShardingMemor yUsage | userId and instanceId | The memory usage. |
| QPS usage (cluster version) | % | ShardingQPSUsa ge | userId and instanceId | The QPS utilization. |
| CPU usage (Cluster Edition) | % | ShardingCpuUsa ge | userId and instanceId | The CPU utilization. |
| Average visits per second (cluster version) | Count/s | ShardingUsedQP S | userId and instanceId | The average QPS. |

| Total QPS (cluster version) | Count/s | ShardingTotalQp s | userId and instanceId | The total QPS. |
|---|---|---|---|---|
| Total Current Connections (Cluster Edition) | Count | ShardingTotalCo nnections | userId and instanceId | The total number of current connections. |

**Cluster Edition - Node**

| Console- based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| Number of Connections Usage (Node) | % | NodeConnection Usage | userId, instanceId, and nodeId | The connection utilization. |
| Incoming Bandwidth (Node) | Kbit/s | NodeIntranetIn | userId, instanceId, and nodeId | The inbound bandwidth. |
| Outgoing Bandwidth (Node) | Kbit/s | NodeIntranetOut | userId, instanceId, and nodeId | The outbound bandwidth. |
| Incoming Bandwidth Utilization (Node) | % | NodeIntranetInR atio | userId, instanceId, and nodeId | The inbound bandwidth usage. |
| Outgoing Bandwidth Utilization (Node) | % | NodeIntranetOut Ratio | userId, instanceId, and nodeId | The outbound bandwidth usage. |
| Memory Usage (Node) | % | NodeMemoryUs age | userId, instanceId, and nodeId | The memory usage. |
| QPS usage (node) | % | NodeQPSUsage | userId, instanceId, and nodeId | The QPS usage. |
| CPU usage (node) | % | NodeCpuUsage | userId, instanceId, and nodeId | The CPU utilization. |

| Average Visits Per Second (Node) | Count | NodeUsedQPS | userId, instanceId, and nodeId | The average QPS. |
|---|---|---|---|---|
| Total QPS (nodes) | Count/S | NodeTotalQps | userId, instanceId, and nodeId | The total QPS. |
| Total Current Connections (Nodes) | Count | NodeTotalConne ctions | userId, instanceId, and nodeId | The total number of current connections. |

##### 4.1.2.11 DTS

This topic describes the metrics supported by Data Transmission Service (DTS). Set the **Namespace** parameter to **acs_dts_dashboard**. Set the **Period** parameter to an integer multiple of 60. Default value: **60**. Unit: seconds.

| Console- based metric | unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| ChangeTrackin gLatency | Seconds | ChangeTrackingLatenc y | userId and instanceId | The latency of the change tracking task. |
| Synchronizatio nLatency | Seconds | SynchronizationLatenc y | userId and instanceId | The latency of the data synchronization task. |
| MigrationLaten cy | Seconds | MigrationLatency | userId and instanceId | The latency of the data migration task. |

#### 4.1.3 Storage and CDN

##### 4.1.3.1 NAS

This topic describes the metrics supported by File Storage NAS (NAS). Set the **Namespace** parameter to **acs_nas**. Set the **Period** parameter to an integer multiple of 60. Default value: **60**. Unit: seconds.

**File system-related metrics**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|

| Aligned Size | Bytes | AlignedSize | userId and fileSystemId | The data volume of General- purpose NAS file systems, excluding the Infrequent Access (IA) storage medium. |
|---|---|---|---|---|
| Storage Usage of IA Storage Medium | Bytes | SecondaryAligned Size | userId and fileSystemId | The data volume of the IA storage medium. |
| File Count | Bytes | FileCount | userId and fileSystemId | The number of files. |
| Read IOPS | Operations/ s | IopsRead | userId and fileSystemId | The average read IOPS per minute. |
| Write IOPS | Operations/ s | IopsWrite | userId and fileSystemId | The average write IOPS per minute. |
| Read Latency | Milliseconds | LatencyRead | userId and fileSystemId | The average read latency per minute. |
| Write Latency | Milliseconds | LatencyWrite | userId and fileSystemId | The average write latency per minute. |
| Metadata QPS | Requests/s | QpsMeta | userId and fileSystemId | The average QPS of metadata per minute. |
| Metadata delay | Milliseconds | LatencyMeta | userId and fileSystemId | The average latency of metadata. |
| Read Throughput | Bytes/s | ThruputRead | userId and fileSystemId | The average read throughput per minute. |
| Write Throughput | Bytes/s | ThruputWrite | userId and fileSystemId | The average write throughput per minute. |

| Maximum usable capacity | Bytes | Quota | userId and fileSystemId | The maximum available capacity. |
|---|---|---|---|---|
| Maximum number of files | Count | MaxFileCount | userId and fileSystemId | The maximum number of files. |
| ErrorRateRead | % | ErrorRateRead | userId and fileSystemId | The percentage of read operations in which errors occur. |
| ErrorRateWrite | % | ErrorRateWrite | userId and fileSystemId | The percentage of write operations in which errors occur. |
| ErrorRateMeta | % | ErrorRateMeta | userId and fileSystemId | The percentage of metadata- related operations in which errors occur. |

##### 4.1.3.2 OSS

This topic describes the metrics supported by Object Storage Service (OSS) Set the **Namespace** parameter to **acs_oss_dashboard**. Set the **Period** parameter to an integer multiple of 60. Default value: **60**. Unit: seconds.

**Basic metrics**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| RequestValidRate | % | RequestValidRat e | userId and BucketName | The rate of valid requests. |
| The number of valid requests. | Count | ValidRequestCou nt | userId and BucketName | The number of valid requests. |

| TotalRequestCou nt | Count | TotalRequestCou nt | userId and BucketName | The total number of requests. |
|---|---|---|---|---|
| Availability | % | Availability | userId and BucketName | The availability. Stay alert if this metric is lower than 100%. |
| InternetSend | Bytes | InternetSend | userId and BucketName | The outbound traffic over the Internet. |
| InternetRecv | Bytes | InternetRecv | userId and BucketName | The inbound traffic over the Internet. |
| IntranetSend | Bytes | IntranetSend | userId and BucketName | The outbound traffic over the intranet. |
| IntranetRecv | Bytes | IntranetRecv | userId and BucketName | The inbound traffic over the intranet. |
| CDNSend | Bytes | CdnSend | userId and BucketName | The CDN outbound traffic. |
| CDNRecv | Bytes | CdnRecv | userId and BucketName | The CDN inbound traffic. |
| SyncSend | Bytes | SyncSend | userId and BucketName | The outbound traffic that is generated when you use the cross-region replication feature. |
| SyncRecv | Bytes | SyncRecv | userId and BucketName | The inbound traffic that is generated when you use the cross-region replication feature. |

| MeteringStorage Utilization | Bytes | MeteringStorage Utilization | userId and BucketName | The size of the storage in use. |
|---|---|---|---|---|
| Storage Usage | % | MeteringStorage UtilizationPercent | userId and BucketName | The storage usage of the OSS bucket. |

**Request status-related metrics**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| ServerErrorCount | Count | ServerErrorCount | userId and BucketName | The number of requests with a server error. |
| ServerErrorRate | % | ServerErrorRate | userId and BucketName | The ratio of requests with a server error. |
| NetworkErrorCou nt | Count | NetworkErrorCou nt | userId and BucketName | The number of requests with a network error. |
| NetworkErrorRate | % | NetworkErrorRat e | userId and BucketName | The ratio of requests with a network error. |
| AuthorizationErro rCount | Count | AuthorizationErro rCount | userId and BucketName | The number of requests with an authorization error. |
| ResourceNotFoun dErrorCount | Count | ResourceNotFoun dErrorCount | userId and BucketName | The number of requests with an error indicating that resources cannot be found. |
| ClientTimeoutErr orCount | Count | ClientTimeoutErr orCount | userId and BucketName | The number of requests with a client timeout error. |
| ClientOtherErrorC ount | Count | ClientOtherError Count | userId and BucketName | The number of requests with other client errors. |

| AuthorizationErro rRate | % | AuthorizationErro rRate | userId and BucketName | The ratio of requests with an authorization error. |
|---|---|---|---|---|
| ResourceNotFoun dErrorRate | % | ResourceNotFoun dErrorRate | userId and BucketName | The ratio of requests with an error indicating that resources cannot be found. |
| Client Timeout Error Request Proportion | % | ClientTimeoutErr orRate | userId and BucketName | The ratio of requests with a client timeout error. |
| ClientOtherErrorR ate | % | ClientOtherError Rate | userId and BucketName | The ratio of requests with other client errors. |
| SuccessCount | Count | SuccessCount | userId and BucketName | The number of successful requests. |
| RedirectCount | Count | RedirectCount | userId and BucketName | The number of redirected requests. |
| SuccessRate | % | SuccessRate | userId and BucketName | The ratio of successful requests. |
| RedirectRate | % | RedirectRate | userId and BucketName | The ratio of redirected requests. |

**Maximum latency-related metrics**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| MaxGetObjectE2 eLatency | Milliseconds | MaxGetObjectE2 eLatency | userId and BucketName | The maximum end-to-end (E2E) latency of GetObject requests. |

| MaxGetObjectSer verLatency | Milliseconds | MaxGetObjectSer verLatency | userId and BucketName | The maximum server latency of GetObject requests. |
|---|---|---|---|---|
| MaxHeadObjectE 2eLatency | Milliseconds | MaxHeadObjectE 2eLatency | userId and BucketName | The maximum E2E latency of HeadObject requests. |
| MaxHeadObjectS erverLatency | Milliseconds | MaxHeadObjectS erverLatency | userId and BucketName | The maximum server latency of HeadObject requests. |
| MaxPutObjectE2e Latency | Milliseconds | MaxPutObjectE2e Latency | userId and BucketName | The maximum E2E latency of PutObject requests. |
| MaxPutObjectSer verLatency | Milliseconds | MaxPutObjectSer verLatency | userId and BucketName | The maximum server latency of PutObject requests. |
| MaxAppendObjec tE2eLatency | Milliseconds | MaxAppendObjec tE2eLatency | userId and BucketName | The maximum E2E latency of AppendObject requests. |
| MaxAppendObjec tServerLatency | Milliseconds | MaxAppendObjec tServerLatency | userId and BucketName | The maximum server latency of AppendObject requests. |
| MaxUploadPartE2 eLatency | Milliseconds | MaxUploadPartE2 eLatency | userId and BucketName | The maximum E2E latency of UploadPart requests. |
| MaxUploadPartSe rverLatency | Milliseconds | MaxUploadPartSe rverLatency | userId and BucketName | The maximum server latency of UploadPart requests. |
| MaxUploadPartCo pyE2eLatency | Milliseconds | MaxUploadPartC opyE2eLatency | userId and BucketName | The maximum E2E latency of UploadPartCopy requests. |

| MaxUploadPartCo pyServerLatency | Milliseconds | MaxUploadPartC opyServerLatenc y | userId and BucketName | The maximum server latency of UploadPartCopy requests. |
|---|---|---|---|---|

**Metrics related to successful requests**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| GetObjectCount | Count | GetObjectCount | userId and BucketName | The number of successful GetObject requests. |
| HeadObjectCount | Count | HeadObjectCount | userId and BucketName | The number of successful HeadObject requests. |
| PostObjectCount | Count | PostObjectCount | userId and BucketName | The number of successful PostObject requests. |
| AppendObjectCo unt | Count | AppendObjectCo unt | userId and BucketName | The number of successful AppendObject requests. |
| UploadPartCount | Count | UploadPartCount | userId and BucketName | The number of successful UploadPart requests. |
| UploadPartCopyC ount | Count | UploadPartCopyC ount | userId and BucketName | The number of successful UploadPartCopy requests. |
| DeleteObjectCou nt | Count | DeleteObjectCou nt | userId and BucketName | The number of successful DeleteObject requests. |
| DeleteObjectsCo unt | Count | DeleteObjectsCo unt | userId and BucketName | The number of successful DeleteObjects requests. |

##### 4.1.3.3 Tablestore

This topic describes the metrics supported by Tablestore. Set the **Namespace** parameter to **acs_ots_dashboard**. Set the **Period** parameter to an integer multiple of 60. Default value: **60**. Unit: seconds.

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| Instance VCU | Count/s | InstanceVCU | userId and instanceName | The virtual compute units (VCUs) of the instance. |
| Reserved VCU | Count/s | InstanceReserve dVCU | userId and instanceName | The reserved VCUs of the instance. |
| Internal Read CU | Count/s | InstanceFreeRea dCU NoOp _ | userId and instanceName | The internal read capacity units (CUs). |
| Internal Write CU | Count/s | InstanceFreeWrit eCU NoOp _ | userId and instanceName | The internal write CUs. |
| Over ReadCU | Count/s | InstanceOverRea dCU NoOp _ | userId and instanceName | The excess read CUs of the instance. |
| Over WriteCU | Count/s | InstanceOverWrit eCU NoOp _ | userId and instanceName | The excess write CUs of the instance. |
| Read CU | Count/s | InstanceReadCU _ NoOp | userId and instanceName | The operation read CUs. |
| Write CU | Count/s | InstanceWriteCU _ NoOp | userId and instanceName | The operation write CUs. |
| Total Request | Count/s | InstanceRequest Number NoOp _ | userId and instanceName | The total number of requests. |
| 2xx Request | Count/s | InstanceCount2x xNumber NoOp _ | userId and instanceName | The number of requests that return a 2XX HTTP status code. |

| 429 Request | Count/s | InstanceCount42 9Number NoOp _ | userId and instanceName | The number of requests that return the HTTP status code 429. |
|---|---|---|---|---|
| 4xx Request | Count/s | InstanceCount4x xNumber NoOp _ | userId and instanceName | The number of requests that return a 4XX HTTP status code. |
| 5xx Request | Count/s | InstanceCount5x xNumber NoOp _ | userId and instanceName | The number of requests that return a 5XX HTTP status code. |
| Internet Inbound | Bytes/s | InstanceExtranetI n NoOp _ | userId and instanceName | The inbound traffic over the Internet. |
| Internet Outbound | Bytes/s | InstanceExtranet Out NoOp _ | userId and instanceName | The outbound traffic over the Internet. |
| Free Outbound Internet | Bytes/s | InstanceFreeExtr anetOut NoOp _ | userId and instanceName | The free outbound traffic over the Internet. |
| Total Rows | Count/s | InstanceRowCou nt NoOp _ | userId and instanceName | The total number of rows. |
| Failed Rows | Count/s | InstanceFailRowC ount NoOp _ | userId and instanceName | The number of failed rows. |
| Storage Size | Byte | StorageSize | userId and instanceName | The storage size. |

#### 4.1.4 Network

##### 4.1.4.1 NAT Gateway

This topic describes the metrics supported by NAT gateways. Set the **Namespace** parameter to **acs_nat_gateway**. Set the **Period** parameter to an integer multiple of 60. Default value: **60**. Unit: seconds.

**Instance-related metrics**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| Total number of sessions | Count | curr num _ | userId and instanceId | The total number of sessions. |
| Capacity Discard Connections (Cumulative Value) | Count | capacity drop _ | userId and instanceId | The number of capacity-dropped connections. |
| Number of new discarded connections (cumulative value) | Count | ratelimit drop _ | userId and instanceId | The number of new dropped connections. |
| Capacity Discard Connections Per Second | Count/s | capacity drop in _ _ c | userId and instanceId | The number of capacity-dropped connections per second. |
| Number of new and discarded connections per second | Count/s | ratelimit drop in _ _ c | userId and instanceId | The number of new dropped connections per second. |
| Number of new connections per second | Count/s | establish rate _ | userId and instanceId | The number of new connections per second. |

**SNAT-related metrics**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| snet rx.rate _ | Bit/s | snet rx.rate _ | userId, instanceId, and snatentryId | The inbound bandwidth. |
| snet tx.rate _ | Bit/s | snet tx.rate _ | userId, instanceId, and snatentryId | The outbound bandwidth. |

##### 4.1.4.2 SLB

This topic describes the metrics supported by Server Load Balancer (SLB). Set the **Namespace** parameter to **acs_slb_dashboard**. Set the **Period** parameter to an integer multiple of 60. Default value: **60**. Unit: seconds.

**Instance-related metrics**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| InstanceActiveCon nection | Count | InstanceActiveConnec tion | userId and instanceId | The number of active TCP connections. |
| InstanceInactiveCo nnection | Count | InstanceInactiveConn ection | userId and instanceId | The number of inactive connections per second on the port. |
| InstanceMaxConne ction | Count/s | InstanceMaxConnecti on | userId and instanceId | The number of concurrent connections per second on the port. |
| InstanceNewConne ction | Count | InstanceNewConnecti on | userId and instanceId | The number of new TCP connections. |
| InstancePacketRX | Count/s | InstancePacketRX | userId and instanceId | The number of inbound packets per second. |
| InstancePacketTX | Count/s | InstancePacketTX | userId and instanceId | The number of outbound packets per second. |
| InternetInRate | Bit/s | InstanceTrafficRXNew | userId and instanceId | The inbound bandwidth. |
| InternetOutRate | Bit/s | InstanceTrafficTXNew | userId and instanceId | The outbound bandwidth. |
| UnhealthyServerCo unt | Count | InstanceUnhealthySer verCount | userId and instanceId | The number of unhealthy backend Elastic Compute Service (ECS) instances. |
| InstanceDropConne ction | Count/s | InstanceDropConnecti on | userId and instanceId | The number of connections dropped from the listener per second. |

| InstanceDropTraffic RX | Bit/s | InstanceDropTrafficR X | userId and instanceId | The number of inbound bits dropped from the listener per second. |
|---|---|---|---|---|
| InstanceDropTraffic RX | Bit/s | InstanceDropTrafficT X | userId and instanceId | The number of outbound bits dropped from the listener per second. |
| InstanceDropTraffic RX | Count/s | InstanceDropPacketR X | userId and instanceId | The number of inbound packets dropped from the listener per second. |
| InstanceDropPacke tTX | Count/s | InstanceDropPacketT X | userId and instanceId | The number of outbound packets dropped from the listener per second. |
| Seven-layer instance Qps | Reques ts/s | InstanceSevenFloorQ ps | userId and instanceId | The QPS at Layer 7. |
| InstanceFailConnec tion | Count | InstanceFailConnectio n | userId and instanceId | The number of failed connections on the instance. |

**Port-related metrics**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| TCPActiveConnectio n | Count | ActiveConnection | userId, instanceId, and port | The number of active TCP connections per second. |
| TCPInactiveConnect ion | Count | InactiveConnectio n | userId, instanceId, and port | The number of inactive connections per second on the port. |
| MaxConnection | Count/s | MaxConnection | userId, instanceId, and port | The number of concurrent connections per second on the port. |
| TCPNewConnection | Count | NewConnection | userId, instanceId, and port | The number of new TCP connections. |

| PacketInPerSecond | Count/s | PacketRX | userId, instanceId, and port | The number of inbound packets per second. |
|---|---|---|---|---|
| PacketOutPerSecon d | Count/s | PacketTX | userId, instanceId, and port | The number of outbound packets per second. |
| IntranetInRate | Bit/s | TrafficRXNew | userId, instanceId, and port | The inbound bandwidth. |
| IntranetOutRate | Bit/s | TrafficTXNew | userId, instanceId, and port | The outbound bandwidth. |
| UnhealthyServerCo unt | Count | UnhealthyServerC ount | userId, instanceId, and port | The number of unhealthy backend ECS instances. |
| DropConnection | Count/s | DropConnection | userId, instanceId, and port | The number of connections dropped from a listener per second. |
| DropTrafficRX | Bit/s | DropTrafficRX | userId, instanceId, and port | The number of inbound bits dropped from the listener per second. |
| DropTrafficTX | Bit/s | DropTrafficTX | userId, instanceId, and port | The number of outbound bits dropped from the listener per second. |
| DropPacketRX | Count/s | DropPacketRX | userId, instanceId, and port | The number of inbound packets dropped from the listener per second. |
| DropPacketTX | Count/s | DropPacketTX | userId, instanceId, and port | The number of outbound packets dropped per second. |
| Seven layers Qps | Reques ts/s | SevenFloorQps | userId, instanceId, and port | The number of queries per second at Layer 7. |

| Number of connection failures per second | Count | FailConnection | userId, instanceId, and port | The number of failed connections per second. |
|---|---|---|---|---|

##### 4.1.4.3 EIP

This topic describes the metrics supported by Elastic IP Address (EIP). Set the **Namespace** parameter to **acs_vpc_eip**. Set the **Period** parameter to an integer multiple of 60. Default value: **60**. Unit: seconds.

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| net rx.rate _ | Bit/s | net rx.rate _ | userId and instanceId | The inbound bandwidth. |
| net rxPkgs.rate _ | Count/s | net rxPkgs.rate _ | userId and instanceId | The rate of inbound packets. |
| net tx.rate _ | Bit/s | net tx.rate _ | userId and instanceId | The outbound bandwidth. |
| net txPkgs.rate _ | Count/s | net txPkgs.rate _ | userId and instanceId | The rate of outbound packets. |
| Out Ratelimit Drop Speed | Packets/s | out ratelimit dro _ _ p speed _ | userId and instanceId | The outbound packet loss rate. |
| In Ratelimit Drop Speed | Packets/s | in ratelimit drop _ _ speed _ | userId and instanceId | The inbound packet loss rate. |

##### 4.1.4.4 VPN Gateway

This topic describes the metrics supported by VPN Gateway. Set the **Namespace** parameter to **acs_vpn**. Set the **Period** parameter to an integer multiple of 60. Default value: **60**. Unit: seconds.

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| IPSec.connection. rxPkgs | Packets/s | ipsec.rxPkgs | userId, instanceId, and ipsecId | The rate of inbound packets of the connection. |

| IPSec.connection. txpkgs | Packets/s | ipsec.txPkgs | userId, instanceId, and ipsecId | The rate of outbound packets of the connection. |
|---|---|---|---|---|
| IPSec.connection. rx.rate | Bit/s | ipsec rx.rate _ | userId, instanceId, and ipsecId | The number of inbound bits of the connection per second. |
| IPSec.connection. tx.rate | Bit/s | ipsec tx.rate _ | userId, instanceId, and ipsecId | The number of outbound bits of the connection per second. |
| SSL Client Count | Count | ssl client.count _ | userId and instanceId | The number of connections. |

##### 4.1.4.5 DNS

This topic describes the metrics supported by DNS. Set the **Namespace** parameter to **acs_dns_dashboard**. Set the **Period** parameter to an integer multiple of 60. Default value: **60**. Unit: seconds.

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| Latency | Milliseco nds | Latency | userId and instanceId | The parsing latency. |
| ParsingSucceed ed | Count | ParsingSucceeded | userId and instanceId | The number of successfully parsed records. |
| Total number of analyses | Count | ParsingTotal | userId and instanceId | The total number of parsed records. |

#### 4.1.5 Application services

##### 4.1.5.1 API Gateway

This topic describes the metrics supported by API Gateway. Set the **Namespace** parameter to **acs_apigateway_dashboard**. Set the **Period** parameter to an integer multiple of 60. Default value: **60**. Unit: seconds.

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| Latency | Milliseconds | Latency | userId and apiUid | The response time. |
| SumQPS | Count | SumQPS | userId and apiUid | The total queries per second (QPS). |
| TrafficRX | KB | TrafficRX | userId and apiUid | The inbound traffic. |
| TrafficTX | KB | TrafficTX | userId and apiUid | The outbound traffic. |
| code2XX Number | Count | code2XX | userId and apiUid | The number of times a 2XX HTTP status code is returned. |
| code4XX Number | Count | code4XX | userId and apiUid | The number of times a 4XX HTTP status code is returned. |
| code5XX Number | Count | code5XX | userId and apiUid | The number of times a 5XX HTTP status code is returned. |

#### 4.1.6 Middleware services

##### 4.1.6.1 ApsaraMQ for RocketMQ

This topic describes the metrics supported by ApsaraMQ for RocketMQ. Set the **Namespace** parameter to **acs_rocketmq_dashboard**. Set the **Period** parameter to an integer multiple of 60. Default value: **60**. Unit: seconds.

**Instance-related metrics**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|

| Message retention duration | Hour | MessageRetentio nPeriod | userId and instanceId | The retention period of the message. |
|---|---|---|---|---|
| ReceiveMessage CountPerInstance | Count/min | ReceiveMessage CountPerInstance | userId and instanceId | The number of messages that the consumer receives per minute. |
| SendMessageCou ntPerInstance | Count/min | SendMessageCou ntPerInstance | userId and instanceId | The number of messages that the producer sends per minute. |
| Consumer(Instan ce) receives messages TPS | Count/min | ReceiveMessage TPSPerInstance | userId and instanceId | The TPS for receiving messages by the consumer per minute. |
| Producer(Instanc e) sends messages TPS | Count/min | SendMessageTPS PerInstance | userId and instanceId | The TPS for sending messages by the producer per minute. |

**Group-related metrics**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| ConsumerLagPer Gid | Count | ConsumerLag | userId, instanceId, and groupId | The number of accumulated messages. |
| ReceiveMessage CountPerGid | Count/min | ReceiveMessage CountPerGid | userId, instanceId, and groupId | The number of messages that the consumer receives per minute. |
| SendDLQMessag eCountPerGid | Count/min | SendDLQMessag eCountPerGid | userId, instanceId, and groupId | The number of dead-letter messages generated per minute. |

| Producer(GroupId ) Number of messages sent per minute | Count/min | SendMessageCou ntPerGid | userId, instanceId, and groupId | The number of messages that the producer sends per minute. |
|---|---|---|---|---|
| Consumer(GroupI d) receives message TPS | Count/min | ReceiveMessage TPSPerGid | userId, instanceId, and groupId | The TPS for receiving messages by the consumer per minute. |
| Producer(GroupId ) sends messages TPS | Count/min | SendMessageTPS PerGid | userId, instanceId, and groupId | The TPS for sending messages by the producer per minute. |

**Topic-related metrics**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| ReceiveMessage CountPerTopic | Count/min | ReceiveMessage CountPerTopic | userId, instanceId, and topic | The number of messages that the consumer receives per minute. |
| SendMessageCou ntPerTopic | Count/min | SendMessageCou ntPerTopic | userId, instanceId, and topic | The number of messages sent by the producer per minute. |
| Consumer(Topic) receives message TPS | Count/min | ReceiveMessage TPSPerTopic | userId, instanceId, and topic | The TPS for receiving messages by the consumer per minute. |
| Producer(Topic) sends messages TPS per minute | Count/min | SendMessageTPS PerTopic | userId, instanceId, and topic | The TPS for sending messages by the producer per minute. |

**Group and topic-related metrics**

| > Document Version | : 20250304 |   |   | 7 |
|---|---|---|---|---|

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| ConsumerLagPer GidTopic | Count | ConsumerLagPer GidTopic | userId, instanceId, groupId, and topic | The number of accumulated messages. |
| ReceiveMessage CountPerGidTopic | Count/min | ReceiveMessage CountPerGidTopi c | userId, instanceId, groupId, and topic | The number of messages that the consumer receives per minute. |
| SendDLQMessag eCountPerGidTop ic | Count/min | SendDLQMessag eCountPerGidTop ic | userId, instanceId, groupId, and topic | The number of dead-letter messages generated per minute. |
| Producer(GroupId & Topic) Number of messages sent per minute | Count/min | SendMessageCou ntPerGidTopic | userId, instanceId, groupId, and topic | The number of messages that the producer sends per minute. |

#### 4.1.7 Big data

##### 4.1.7.1 Stream Computing (Blink)

This topic describes the metrics supported by Stream Computing (Blink) Set the **Namespace** parameter to **acs_blink**. Set the **Period** parameter to an integer multiple of 60. Default value: **60**. Unit: seconds.

| Console-based metric | Unit | API-based metric | Dimensions | Description |
|---|---|---|---|---|
| FetchedDelay | Seconds | FetchedDelay | userId, regionId, projectName, and jobName | The processing latency. |
| Response Delay | % | inputDelay | userId, regionId, projectName, and jobName | The service latency. |

| Read RPS | rps | ParserTpsRate | userId, regionId, projectName, and jobName | The read records per second (RPS). |
|---|---|---|---|---|
| Write RPS | RPS | SinkOutTpsRate | userId, regionId, projectName, and jobName | The write RPS. |
| FailoverRate | % | TaskFailoverRate | userId, regionId, projectName, and jobName | The failover rate. |

##### 4.1.7.2 DataHub

This topic describes the metrics supported by DataHub. Set the **Namespace** parameter to **acs_datahub**. Set the **Period** parameter to an integer multiple of 60. Default value: **60**. Unit: seconds.

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| subscription delay time | Seconds | subscribe delay _ | userId, regionId, project, topic, and subId | The latency between the time when a user subscribes to data and the current system time. |
| Consumption latency | Seconds | consume delay _ | userId, regionId, project, topic, and subId | The latency between the time when a user subscribes to data and the time when the lasted data is generated. |
| Number of accumulated messages | Count | record stacked _ | userId, regionId, project, topic, and subId | The amount of accumulated data to be consumed by the subscriber. |

#### 4.1.8 Security (Apsara Stack Security)

##### 4.1.8.1 Tenant-side bastion hosts

This topic describes the metrics for tenant-side bastion hosts. Set the **Namespace** parameter to **acs_bastionhost**. Set the **Period** parameter to an integer multiple of 60. Default value: **60**. Unit: seconds.

**System-related metrics**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| (ECS)CPU usage | % | CPUUtilization | userId and instanceId | The CPU utilization. |
| CPU system usage | % | CPUSysUtilization | userId and instanceId | The CPU utilization in kernel mode. |
| CPU user usage | % | CPUSysUtilization | userId and instanceId | The CPU utilization in user mode. |
| (ECS) memory usage | % | MemoryUtilization | userId and instanceId | The memory usage. |
| (ECS) system load Load1 | Count/s | SystemLoad1 | userId and instanceId | The system load in the last minute. |
| (ECS) system load Load5 | Count/s | SystemLoad5 | userId and instanceId | The system load in the last 5 minutes. |
| (ECS) System load Load15 | Count/s | SystemLoad15 | userId and instanceId | The system load in the last 15 minutes. |
| (ECS) root directory disk usage | % | RootDiskUtilization | userId and instanceId | The disk usage of the root directory. |
| (ECS)Docker directory disk usage | % | DockerDiskUtilizatio n | userId and instanceId | The disk usage of the Docker directory. |
| (ECS) root directory disk remaining | GB | DfRootBfree | userId and instanceId | The available disk space of the root directory. |
| (ECS) root directory disk used | GB | DfRootUsed | userId and instanceId | The used disk space of the root directory. |
| (ECS) Total number of root directory disks | GB | DfRootBtotl | userId and instanceId | The total disk space of the root directory. |

| (ECS)Docker directory disk remaining | GB | DfDockerBfree | userId and instanceId | The available disk space of the Docker directory. |
|---|---|---|---|---|
| (ECS)Docker directory disk used | GB | DfDockerUsed | userId and instanceId | The used disk space of the Docker directory. |
| (ECS) Total number of Docker directory disks | GB | DfDockerBtotl | userId and instanceId | The total disk space of the Docker directory. |
| (ECS) root Inode usage | % | RootInodeUtilization | userId and instanceId | The inode usage of the root directory. |
| (ECS)Docker directory Inode usage | % | DockerInodeUtilizati on | userId and instanceId | The inode usage of the Docker directory. |
| (ECS) network ingress traffic | Bytes/s | TrafficBytin | userId and instanceId | The inbound traffic. |
| (ECS) network egress traffic | Bytes/s | TrafficBytout | userId and instanceId | The outbound traffic. |
| (ECS)tcp links | Count | TcpConnections | userId and instanceId | The number of TCP connections. |
| (ECS) number of processes | Count | ProcessNumber | userId and instanceId | The number of processes. |
| (ECS)NTP service offset | Second s | NtpOffset | userId and instanceId | The offset of the Network Time Protocol (NTP) service. |
| (ECS) Whether the Docker service is running properly | Count/s | DockerService | userId and instanceId | The status of the Docker service. Valid values: 0: The Docker service does not exist. 1: The Docker service exists. |

**Business-related metrics**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| CountSession | Count | CountSession | instanceId | The number of real- time sessions. |
| CountUser | Count | CountUser | instanceId | The number of users of the bastion host. |
| CountHost | Count | CountHost | instanceId | The number of hosts managed by the bastion host. |
| CountHostQuota | Count | CountHostQuota | instanceId | The quota of hosts that can be managed by the bastion host. |
| CountVisitPolicy | Count | CountVisitPolicy | instanceId | The number of access policies of the bastion host. |
| CountCommandP olicy | Count | CountCommandPolic y | instanceId | The number of command policies of the bastion host. |
| CountWorkorderP olicy | Count | CountWorkorderPolic y | instanceId | The number of ticket policies of the bastion host. |
| CountWarningDay Un | Count | CountWarningDayUn | instanceId | The number of alerts that the bastion host does not handle on the current day. |
| CountWarningDay | Count | CountWarningDay | instanceId | The total number of alerts on the current day. |
| NICBindWidthRx | Mbit/s | NICBindWidthRx | instanceId | The inbound bandwidth of the network interface controller (NIC). |

| NICBindWidthTx | Mbit/s | NICBindWidthTx | instanceId | The outbound bandwidth of the NIC. |
|---|---|---|---|---|
| CountAppServerR un | Count | CountAppServerRun | instanceId | The number of frontend hosts in the normal state. |
| CountAppServerF ault | Count | CountAppServerFault | instanceId | The number of frontend hosts in the abnormal state. |

**Health check-related metrics**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| (Service) Service Health Check | Count/s | ServiceHealthCheck | userId and instanceId | The status of the health check service. Valid values: 0: The service does not work as expected. 1: The service works as expected. |

##### 4.1.8.2 Vulnerability scanner engines

This topic describes the metrics for vulnerability scanner engines. Set the **Namespace** parameter to **acs_scanner**. Set the **Period** parameter to an integer multiple of 60. Default value: **60**. Unit: seconds.

**System-related metrics**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| (ECS)CPU usage | % | CPUUtilization | userId and instanceId | The CPU utilization. |
| CPU system usage | % | CPUSysUtilization | userId and instanceId | The CPU utilization in kernel mode. |
| CPU user usage | % | CPUUserUtilization | userId and instanceId | The CPU utilization in user mode. |

| (ECS) memory usage | % | MemoryUtilization | userId and instanceId | The memory usage. |
|---|---|---|---|---|
| (ECS) system load Load1 | Count/s | SystemLoad1 | userId and instanceId | The system load in the last minute. |
| (ECS) system load Load5 | Count/s | SystemLoad5 | userId and instanceId | The system load in the last 5 minutes. |
| (ECS) System load Load15 | Count/s | SystemLoad15 | userId and instanceId | The system load in the last 15 minutes. |
| (ECS) root directory disk usage | % | RootDiskUtilization | userId and instanceId | The disk usage of the root directory. |
| (ECS)Docker directory disk usage | % | DockerDiskUtilizatio n | userId and instanceId | The disk usage of the Docker directory. |
| (ECS)Docker directory disk remaining | GB | DfDockerBfree | userId and instanceId | The available disk space of the Docker directory. |
| (ECS)Docker directory disk used | GB | DfDockerUsed | userId and instanceId | The used disk space of the Docker directory. |
| (ECS) Total number of Docker directory disks | GB | DfDockerBtotl | userId and instanceId | The total disk space of the Docker directory. |
| (ECS) root directory disk remaining | GB | DfRootBfree | userId and instanceId | The available disk space of the root directory. |
| (ECS) root directory disk used | GB | DfRootUsed | userId and instanceId | The used disk space of the root directory. |
| (ECS) Total number of root directory disks | GB | DfRootBtotl | userId and instanceId | The total disk space of the root directory. |
| (ECS) root Inode usage | % | RootInodeUtilization | userId and instanceId | The inode usage of the root directory. |

| (ECS)Docker directory Inode usage | % | DockerInodeUtilizati on | userId and instanceId | The inode usage of the Docker directory. |
|---|---|---|---|---|
| (ECS) network ingress traffic | Bytes/s | TrafficBytin | userId and instanceId | The inbound traffic. |
| (ECS) network egress traffic | Bytes/s | TrafficBytout | userId and instanceId | The outbound traffic. |
| (ECS)tcp links | Count/s | TcpConnections | userId and instanceId | The number of TCP connections. |
| (ECS) number of processes | Count | ProcessNumber | userId and instanceId | The number of processes. |
| (ECS)NTP service offset | Second s | NtpOffset | userId and instanceId | The offset of the Network Time Protocol (NTP) service. |
| (ECS) Whether the Docker service is running properly | Count/s | DockerService | userId and instanceId | The status of the Docker service. Valid values: 0: The Docker service does not exist. 1: The Docker service exists. |

**Health check-related metrics**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| (Service) Service Health Check | Count/s | ServiceHealthCheck | userId and instanceId | The status of the health check service. Valid values: 0: The service does not work as expected. 1: The service works as expected. |

### 4.2 Manage cloud service monitoring

**monitoring**

On the monitoring page of a cloud service, you can view the monitoring data about resources of the cloud service in monitoring charts. You can also configure alert rules to monitor the status of resources. If an alert is triggered based on an alert rule, CloudMonitor sends an alert notification to you. This way, you are notified about the status of your resources at the earliest opportunity.

> **Important:** In the root organization, you can only view monitoring charts and alert rules, but cannot manage alert rules.

**View monitoring charts**

On the monitoring page of a cloud service, you can view the status of resources and the metrics.
1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Products** > **Migration and O&M Management** > **O&M**
**and Monitoring** > **CloudMonitor**.
3. In the left-side navigation pane, click **Cloud Service Monitoring**.
4. On the **Cloud product monitoring** page, click a cloud service.
5. On the monitoring page of the cloud service, find the resource that you want to view and
click **Monitoring chart** in the **Actions** column. On the page that appears, you can view the monitoring charts of the resource.

> **Note:** You can view the monitoring data that is generated in the last 30 days at most.

**View alert rules**

On the monitoring page of a cloud service, you can view all alert rules that are configured for the cloud service or a specific resource of the cloud service in the current organization and resource set.
1. On the monitoring page of a cloud service, click **View Alert Rules** in the upper part of the
page, or find the resource that you want to view and click **Alarm Rules** in the **Actions** column.
2. On the **Alarm Rules** page, view all alert rules that are configured for the cloud service or
the specified resource in the current organization and resource set. You can view the details of each alert rule, including the cloud service name, alert rule name, status, associated resources, alert condition, whether the rule is enabled, and alert contacts.

> **Note:** On the monitoring page of a cloud service, you can click **Create an alert rule** in the upper part of the page to create an alert rule for the cloud service. For more information, see Create an alert rule.
> For more information about how to manage alert rules, see Manage alert rules.

## 5 Alert service

You can manage alert rules, alert history, and alert templates in the Alert Service module of CloudMonitor. You can configure alert rules to specify how CloudMonitor checks monitoring data. If monitoring data triggers the alert rules, CloudMonitor sends alert notifications. When an alert is generated, CloudMonitor records the alert information in the alert history. You can review and analyze the alert history to troubleshoot issues and make predictions. Alert templates simplify the process of creating and maintaining alert rules when you need to manage a large number of cloud resources. This helps you monitor cloud services more efficiently.

### 5.1 Alert history

You can specify the cloud service, instance, alert level, and other filter conditions to view the alert history. You can also export and download the alert history to your on-premises machine for data analysis.

**Procedure**

1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Products** > **Migration and O&M Management** > **O&M**
**and Monitoring** > **CloudMonitor**.
3. In the left-side navigation pane, choose**Alert Service** > **Alert History**.
4. Optional. On the **Alarm History** page, filter alert records by configuring the **Rule ID**, **Rule**
**Name**, **Cloud product selection**, **Alarm Level**, **Instance ID**, and Starting and ending
time parameters.
5. On the Alarm History page, perform the required operations. The following table describes
the operations that you can perform.

| Operation | Procedure |
|---|---|
| View the alert history | On the Alarm History page, view the information about alerts in the following columns: Product Name, Fault instance, Occurrence time, Rule Name, Status, Grade, and Notification object. Find an alert record that you want to view and click the rule name in the Rule Name column to view the details of the alert rule. Note By default, you can query the alert history of the last two days. |

| Export and download a report on the alert history | i. On the Alarm History page, click the icon in the upper- right corner. ii. In the Export task dialog box, configure the Time Selection and Task name parameters and click OK. iii. In the left-side navigation pane, click Export Report. On the Report Export page, click the Alarm History tab. iv. On the Alarm History tab, find the export task that you created and click Download Report Task in the Operation column. v. In the Download Report Task message, click OK. Note The report is in the .xlsx format. You can find the downloaded report in the default download directory of your browser. |
|---|---|

### 5.2 Alert rules

You can configure alert rules for host monitoring metrics and instances in cloud service monitoring. You can apply an alert rule to all resources, an application group, or an instance. Alert Service sends alert notifications to contacts by using emails, DingTalk messages, and webhook URLs.

> **Note:** You cannot manage alert rules in the root organization.

#### 5.2.1 Create an alert rule

You can create alert rules for cloud services that are connected to CloudMonitor, such as Elastic Compute Service (ECS) instances.

**Background information**

During the validity period of an alert rule, CloudMonitor checks whether the metric values of cloud services exceed the specified thresholds at the default monitoring frequency. If a metric value exceeds the threshold, CloudMonitor sends alert notifications to the specified contacts or alert processing platforms.

> **Note:** For ApsaraDB RDS that uses the old link, the monitoring frequency varies from every 60 to 300 seconds. For all other cloud services, the minimum monitoring frequency is set to once per minute.

**Procedure**

1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose**Products** > **Migration and O&M Management** > **O&M**
**and Monitoring** > **CloudMonitor**.
3. In the left-side navigation pane, choose **Alert Service** > **Alert Rule**.
4. On the Alert Rules page, click **Create an alert rule**.
5. In the **Create an alert rule** panel, configure parameters based on your business
requirements. The following table describes the parameters.

| Parameter | Description |
|---|---|
| Cloud product selection | The cloud service that you want to monitor. |
| Resource scope | The resources that are associated with the alert rule. The supported resource types vary based on cloud services. Valid values: Instance dimension: Select one or more instances in the resource set of the current organization. Resource set dimension: Select a resource set in the current organization and region. Application grouping dimensions: Select an application group in the current organization and region. All resources: By default, you cannot select this value. |
| Resource Selection | The resources to be associated with the alert rule. Select one or more resources based on the selected resource type. |
| Alarm rule description | The trigger conditions of the alert rule. If the metrics meet the specified conditions, the alert rule is triggered. To configure the trigger conditions, perform the following steps: i. Click Add Rule Description. ii. In the Add Rule Description panel, configure the Rule Name, Metric, Metric Dimensions, and Threshold and Alert Level parameters. Note The Metric Dimensions parameter is displayed only if you set the Resource scope parameter to Instance dimension. iii. Click Confirm. |
| Silence channel period | The interval at which you want CloudMonitor to send alert notifications again if the alert is not cleared. Valid values: 5 Minutes, 10 Minutes, 30 Minutes, 1 hour, 3 hours, 6 hours, 12 hours, and 24 hours. An alert is triggered if the conditions of an alert rule are met. CloudMonitor does not resend an alert notification when the alert is triggered within the mute period. If the alert is not cleared after the mute period ends, CloudMonitor resends alert notifications. For example, if you set the Silence channel period parameter to 12 hours, CloudMonitor resends alert notifications only if the alert still persists after 12 hours. |

| Effective time | The period during which the alert rule is effective. CloudMonitor checks whether the monitoring data can trigger the alert rule only during the effective period. |
|---|---|
| Alarm callback | The callback URL to which CloudMonitor sends alert notifications by using the POST request method. Note The callback URL must be accessible for CloudMonitor. You can enter only an HTTP URL. IP addresses are not supported. |
| No data processing method | The method that is used to handle alerts if no monitoring data exists. Valid values: No processing Send no data alarm |
| Alert contact | The contact group or contact that receives alert notifications. By default, the value of this parameter is a dummy user used to test whether the alert rule is effective. |

6. Click **OK**.

**Parameters in the rule description**

| Parameter | Description |
|---|---|
| Rule name | The name of the alert rule. |
| Monitoring Metrics | The metric of the cloud service that you want to monitor. For more information about the metrics of cloud services, see the "Metrics" topic. |
| Metric dimensions | The metric dimensions, excluding the instance ID dimension. This parameter is displayed only if you set the Resource Range parameter to Instance. |
| Threshold and alarm level | Valid values of the alert level: Critical, Warning, and Ordinary. Valid values of the aggregate value type: Average, Minimum, and Maximum. Valid values of the monitoring period: continuous, 5 cycles (1 cycle =60S), 10 cycles (1 cycle =60S), 15 cycles (1 cycle =60S), 30 cycles (1 cycle =60S), and 60 cycles (1 cycle =60S). Valid values of the comparison relationship between the monitoring data and alert threshold: >, >=, <, <=, =, !=, Year-on-year increase at the same time yesterday, and Year-on-year decline at the same time yesterday. You also need to set an alert threshold and a trigger count. An alert is generated if the monitoring data reaches the specified threshold for the specified number of times at a specific interval. |

**Sample rule configuration**

Create an alert rule named example to monitor the CPU utilization of ECS instances. If the maximum CPU utilization is equal to or greater than 70% three times within five intervals, an alert of the Critical level is generated. The following figure shows the parameter configurations in the rule description.

#### 5.2.2 Manage alert rules

You can modify, disable, enable, and delete alert rules on the Alarm Rules page in CloudMonitor.

**Procedure**

1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose**Products** > **Migration and O&M Management** > **O&M**
**and Monitoring** > **CloudMonitor**.
3. In the left-side navigation pane, choose**Alert Service** > **Alert Rule**.
4. On the Alarm Rules page, perform operations based on your business requirements. The
following table describes the operations that you can perform on alert rules.

| Operation | Procedure |
|---|---|

| View the details of an alert rule | Find the alert rule that you want to manage and clickD etails in the Actions column. In the Alarm rule details panel, view the details of the alert rule. |
|---|---|
| Modify an alert rule | i. Find the alert rule that you want to manage and clickE dit in the Actions column. ii. In the Modify alarm rules panel, configure parameters to modify the alert rule. For more information about the parameters, see Create an alert rule. iii. After you modify the alert rule based on your business requirements, click OK. |
| Disable one or more alert rules | If you stop a cloud service for maintenance or upgrade purposes, you can disable the alert rules that are associated with the cloud service. This way, manual operations on the service do not trigger CloudMonitor to send alert notifications. Note Make sure that the alert rule is in the Normal state before you disable the alert rule. Disable a single alert rule a. On the Alarm Rules page, find the alert rule that you want to disable, click the icon in the Actions column, and then click Disable. b. In the Disable alarm rules message, click OK. Disable multiple alert rules at a time a. Select the alert rules that you want to disable and click Disable in the lower-left corner of the alert rule list. b. In the Disable alarm rules message, click OK. |
| Enable one or more alert rules | After you maintain or upgrade a cloud service, you can enable all disabled alert rules. Enable a single alert rule a. Find the alert rule that you want to enable, click the icon in the Actions column, and then click Enable. b. In the Enable alarm rules message, click OK. Enable multiple alert rules at a time a. Select the alert rules that you want to enable and click Enable in the lower-left corner of the alert rule list. b. In the Enable alarm rules message, click OK. |

| Delete one or more alert rules | Delete a single alert rule a. Find the alert rule that you want to delete, click the icon in the Actions column, and then click Delete. b. In the Delete Alert message, click OK. Delete multiple alert rules at a time a. Select the alert rules that you want to delete and click Delete in the lower-left corner of the alert rule list. b. In the Delete alarm rules message, click OK. |
|---|---|
| Export and download an alert rule report | i. On the Alarm Rules page, click the icon. ii. In the Export task dialog box, specify the task name. iii. Click OK. iv. In the left-side navigation pane, click Export Report. v. On the Alarm rules tab, find the report that you want to download and click Download Report in the Actions column. vi. In the Download report task message, click OK. |

### 5.3 Alert templates

#### 5.3.1 Common alerting templates

CloudMonitor provides preset alerting templates for Elastic Computer Service (ECS), ApsaraDB RDS, Object Storage Service (OSS), Server Load Balancer (SLB), Elastic IP Address (EIP), Apsara Stack DNS, Hologres, and KVStore for Redis. You can directly apply the preset alerting templates on resource sets or application groups to implement alerting based on common metrics. You can also create custom templates on top of the preset templates to suit your business requirements. CloudMonitor provides preset alerting templates that help you implement alerting on cloud resources based on common metrics.

**ECS**

| Metric | Threshold | Consecu tive occurre nces | Alert level | Rule description |
|---|---|---|---|---|
| cpu total _ | >=85.00% | 5 | INFO | The CPU utilization of an ECS instance reaches 85% for five consecutive times. |
|   | >=95.00% | 5 | WARN | The CPU utilization of an ECS instance reaches 95% for five consecutive times. |

| memory use _ dutilization | >=80.00% | 5 | INFO | The memory usage of an ECS instance reaches 80% for five consecutive times. |
|---|---|---|---|---|
| diskusage u _ tilization | >=85.00% | 5 | INFO | The disk usage of an ECS instance reaches 85% for five consecutive times. |
|   | >=95.00% | 5 | WARN | The disk usage of an ECS instance reaches 95% for five consecutive times. |

**ApsaraDB RDS**

**ApsaraDB RDS (New)**

The templates are applicable to ApsaraDB RDS instances that run the MySQL, PolarDB for Oracle, and SQL Server engines.

| Metric | Threshold | Consec utive occurre nces | Alert level | Rule description |
|---|---|---|---|---|
| ConnectionUsa ge new _ | >=80.00% | 5 | INFO | The connection usage of an ApsaraDB RDS instance reaches 80% for five consecutive times. |
| CpuUsage new _ | >=65.00% | 5 | INFO | The CPU utilization of an ApsaraDB RDS instance reaches 65% for five consecutive times. |
| DataDelay | >=10 | 5 | WARN | The latency of a read-only ApsaraDB RDS instance reaches 10 seconds for five consecutive times. |
| DiskUsage ne _ w | >=70.00% | 5 | INFO | The disk usage of an ApsaraDB RDS instance reaches 70% for five consecutive times. |
| IOPSUsage ne _ w | >=80.00% | 5 | INFO | The IOPS usage of an ApsaraDB RDS instance reaches 80% for five consecutive times. |
| MemoryUsage _ new | >=80.00% | 5 | INFO | The memory usage of an ApsaraDB RDS instance reaches 80% for five consecutive times. |

**ApsaraDB RDS for PostgreSQL**

The templates are applicable only to ApsaraDB RDS for PostgreSQL instances.

| Metric | Threshold | Consec utive occurre nces | Alert level | Rule description |
|---|---|---|---|---|
| cpu usage _ | >=80.00% | 5 | INFO | The CPU utilization of an ApsaraDB RDS for PostgreSQL instance reaches 80% for five consecutive times. |
| mem usage _ | >=80.00% | 5 | INFO | The memory usage of an ApsaraDB RDS for PostgreSQL instance reaches 80% for five consecutive times. |
| local fs size us _ _ _ age | >=85.00% | 5 | WARN | The disk usage of an ApsaraDB RDS for PostgreSQL instance reaches 85% for five consecutive times. |
| ReadLag new _ | >=7200 | 5 | INFO | The latency of a read-only ApsaraDB RDS for PostgreSQL instance reaches 7,200 seconds for five consecutive times. |

**OSS**

| Metric | Threshold | Consec utive occurre nces | Alert level | Rule description |
|---|---|---|---|---|
| Availability | <100% | 3 | INFO | The availability of an OSS bucket goes below 100% for three consecutive times. |

**SLB**

| Metric | Threshold | Consec utive occurr ences | Alert level | Rule description |
|---|---|---|---|---|
| InstanceTraffi cRXNew SUM _ | >=4000000000 | 1 | WARN | The inbound bandwidth of an SLB instance reaches 4 Gbit/s. |
|   | >=4500000000 | 1 | Critical | The inbound bandwidth of an SLB instance reaches 4.5 Gbit/s. |
|   | >=4000000000 | 1 | WARN | The outbound bandwidth of an SLB instance reaches 4 Gbit/s. |
| 4 | > Document Version: 2025030 |   |   |   |

| loudMonitor | User Guide·Alert servic |   |   |   |
|---|---|---|---|---|
| InstanceTraffi cTXNew SUM _ |   |   |   |   |
|   | >=4500000000 | 1 | Critical | The outbound bandwidth of an SLB instance reaches 4.5 Gbit/s. |
| InstanceNewC onnection | >=16000 | 1 | WARN | The number of new connections to an SLB instance per second reaches 16,000. |
|   | >=18000 | 1 | Critical | The number of new connections to an SLB instance per second reaches 18,000. |
| InstanceMaxC onnection | >=160000 | 1 | WARN | The maximum number of concurrent connections per second on the port of an SLB instance reaches 160,000. |
|   | >=180000 | 1 | Critical | The maximum number of concurrent connections per second on the port of an SLB instance reaches 180,000. |
| InstanceDrop Connection | >=10 | 3 | WARN | The number of connections dropped by an SLB instance per second reaches 10 for three consecutive times. |
|   | >=200 | 3 | Critical | The number of connections dropped by an SLB instance per second reaches 200 for three consecutive times. |
| InstanceDrop TrafficRX | >=100000 | 3 | WARN | An SLB instance drops 100,000 bits of inbound traffic or more per second for three consecutive times. |
|   | >=2000000 | 3 | Critical | An SLB instance drops 2,000,000 bits of inbound traffic or more per second for three consecutive times. |
| InstanceDrop TrafficTX | >=100000 | 3 | WARN | An SLB instance drops 100,000 bits of outbound traffic or more per second for three consecutive times. |
|   | >=2000000 | 3 | Critical | An SLB instance drops 2,000,000 bits of outbound traffic or more per second for three consecutive times. |
| InstanceUnhe althyServerCo unt | One instance more than the previous day | 3 | WARN | The number of abnormal ECS instances detected in the health check of an SLB instance grows by 1 for three consecutive days. |

**EIP**

| Metric | Thr esh old | Consec utive occurre nces | Alert level | Rule description |
|---|---|---|---|---|
| out ratelimit drop s _ _ _ peed | >0 | 3 | INFO | The maximum outbound packet loss rate of an EIP is greater than 0 for three consecutive times. |
| in ratelimit drop sp _ _ _ eed | >0 | 3 | INFO | The maximum inbound packet loss rate of an EIP is greater than 0 for three consecutive times. |

**Apsara Stack DNS**

| Metric | Threshol d | Consec utive occurre nces | Alert level | Rule description |
|---|---|---|---|---|
| ParsingTotal | >40000 | 3 | WARN | The total number of DNS domain names resolved is greater than 40,000 for three consecutive times. |
|   | >45000 | 3 | Cirtical | The total number of DNS domain names resolved is greater than 45,000 for three consecutive times. |

**KVStore for Redis**

**KVStore for Redis (Standard Architecture)**

| Metric | Threshold | Consec utive occurre nces | Alert level | Rule description |
|---|---|---|---|---|
| StandardCpuU sage | >=65.00% | 5 | WARN | The CPU utilization of a KVStore for Redis instance reaches 65% for five consecutive times. |
| StandardIntra netInRatio | >=80.00% | 5 | WARN | The inbound bandwidth usage of a KVStore for Redis instance reaches 80% for five consecutive times. |

| StandardIntra netOutRatio | >=80.00% | 5 | WARN | The outbound bandwidth usage of a KVStore for Redis instance reaches 80% for five consecutive times. |
|---|---|---|---|---|
| StandardMem oryUsage | >=80.00% | 5 | WARN | The memory usage of a KVStore for Redis instance reaches 80% for five consecutive times. |
| StandardQPSU sage | >=80.00% | 5 | WARN | The queries per second (QPS) usage of a KVStore for Redis instance reaches 80% for five consecutive times. |
| StandardConn ectionUsage | >=80.00% | 5 | WARN | The connection usage of a KVStore for Redis instance reaches 80% for five consecutive times. |

**KVStore for Redis (Cluster Architecture)**

| Metric | Threshol d | Consec utive occurre nces | Alert level | Rule description |
|---|---|---|---|---|
| ShardingCpuU sage | >=65.00 % | 5 | WARN | The CPU utilization of a KVStore for Redis instance reaches 65% for five consecutive times. |
| ShardingIntra netIn | >=80.00 % | 5 | WARN | The inbound bandwidth usage of a KVStore for Redis instance reaches 80% for five consecutive times. |
| ShardingIntra netOut | >=80.00 % | 5 | WARN | The outbound bandwidth usage of a KVStore for Redis instance reaches 80% for five consecutive times. |
| ShardingMem oryUsage | >=80.00 % | 5 | WARN | The memory usage of a KVStore for Redis instance reaches 80% for five consecutive times. |
| ShardingQPSU sage | >=80.00 % | 5 | WARN | The QPS usage of a KVStore for Redis instance reaches 80% for five consecutive times. |
| ShardingConn ectionUsage | >=80.00 % | 5 | WARN | The connection usage of a KVStore for Redis instance reaches 80% for five consecutive times. |

#### 5.3.2 Create an alert template

If you want to monitor a large number of resources, you can use the alert template feature. This feature helps you save multiple alert rules on the metrics of various cloud services as a template. You can create or modify alert rules by using alert templates. This prevents repeated workloads of configuring each alert rule.

**Background information**

You must use alert templates together with application groups. You can create an application group first. Then, you can create an alert template and apply the alert template to the application group to create alert rules for the application group. This simplifies the creation and maintenance of alert rules. For more information about how to create an application group, see Create an application group.

**Procedure**

1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose**Products** > **Migration and O&M Management** > **O&M**
**and Monitoring** > **CloudMonitor**.
3. In the left-side navigation pane, choose **Alert Service** > **Alert Templates**.
4. On the **Alarm Template** page, click **Create an alarm Template**.
5. In the **Create an alarm Template** panel, configure the parameters described in the
following table.

| Parameter | Description |
|---|---|
| Template Name | The name of the alert template. The name can contain letters, digits, and underscores ( ). We recommend that the name be 1 to 30 _ characters in length. |
| Description | Optional. The description of the alert template. We recommend that the description be 1 to 100 characters in length. |
| Template Cloning | Optional. The existing alert template that you want to clone. You can modify the configurations of the selected template to create a new alert template. |
| Product selection | The cloud services for which you want to apply the alert template. |

6. Click **Add Rule** to configure an alert rule. The following table describes the parameters of
the alert rule.

| Parameter | Description |
|---|---|
| Rule Name | The name of the alert rule. |
| Indicator Name | The metrics that you want to monitor. For more information about the metrics of cloud services, see the "Metrics" topic. |

| Compare | The comparison condition between metric data and thresholds. If the metric data exceeds the specified thresholds, the alert rule is triggered. Valid values: >, >=, <, <=, =, !=, Year-on-year increase at the same time yesterday, and Year-on-year decline at the same time yesterday. |
|---|---|
| Threshold and Alarm Level | The conditions, alert thresholds, and alert levels of the alert rule. You can specify multiple alert levels with different conditions. Alert levels: Critical Warn Info Number of times for which the metric data is equal to or greater than the threshold: The number of times determines whether the alert notification is sent. Valid values: 1 Consecutive Cycles 2 Consecutive Cycles 3 Consecutive Cycles 4 Consecutive Cycles 5 Consecutive Cycles 10 Consecutive Cycles 15 Consecutive Cycles 20 Consecutive Cycles |

7. After you add rules for each cloud service, click **Confirm**.

#### 5.3.3 Manage alert templates

On the Alarm Template page, you can modify, clone, export, delete, and apply alert templates.

**Procedure**

1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose**Products** > **Migration and O&M Management** > **O&M**
**and Monitoring** > **CloudMonitor**.
3. In the left-side navigation pane, choose **Alert Service** > **Alert Templates**.
4. On the Alarm Template page, select an alert template and perform the required operations.
The following table describes the operations that you can perform on alert templates.

| Operation | Procedure |
|---|---|

| Modify an alert template | i. Find the alert template that you want to modify and click Modification in the Actions column. ii. In the Modify Alarm Template panel, modify the description, Alibaba Cloud services, and rules of the alert template. iii. Click OK. Note You cannot modify default templates. |
|---|---|
| Clone an alert template | You can clone an alert template to copy the template configurations to create a new alert template. i. Find the alert template that you want to clone and clickT emplate Cloning in the Actions column. ii. In the Clone an alarm Template panel, specify a name for the new template, select Alibaba Cloud services, and configure alert rules based on your business requirements. iii. Click OK. iv. In the Alert Template Created/Modified message, click Cancel. Note If you click Cancel, the alert template is created but not applied to the application group. |
| Delete one or more alert templates | Warning Deleted alert templates cannot be restored. Delete a single alert template a. Find the alert template that you want to delete and clickD elete in the Actions column. b. In the Delete Alert Template message, click OK. Delete multiple alert templates at a time a. Select the alert templates that you want to delete and click Delete in the lower-left corner of the page. b. In the Delete Alert Template message, click OK. |

| Apply one or more alert templates to application groups or resource sets | Alert templates must be used together with application groups. You can apply alert templates to application groups to create alert rules for resources from different cloud services. Make sure that application groups or resource sets, and alert templates are available. For information about how to create the resources, see Create an alert template, Create an application group, and Create a resource set. Important After you select and apply an alert template to a specified application group or resource set, CloudMonitor deletes the existing alert rules that are created based on the original alert template except for the process monitoring and availability monitoring rules. Then, CloudMonitor creates new alert rules based on the new alert template. We recommend that you apply an alert template to up to five application groups or resource sets. Otherwise, the alert template may fail to take effect for some application groups or resource sets. Apply an alert template to application groups or resource sets a. Find the alert template that you want to apply, click the icon in the Actions column, and then click Application alarm Template. b. In the Apply Templates to Grouping dialog box, configure the Resource Set, Resource selection, Channel Silence Period, Effective time, Alarm callback, and Alarm Contact Group parameters. You can set the Resource Set parameter to Resource set or Application grouping. c. Click OK. d. In the Apply Template to Group message, click OK. Apply multiple alert templates to application groups or resource sets a. Select the alert templates that you want to apply and click Batch Application Template in the lower-left corner. b. In the Apply Templates to Grouping dialog box, configure the Resource Set, Resource selection, Channel Silence Period, Effective time, Alarm callback, and Alarm Contact Group parameters. You can set the Resource Set parameter to Resource set or Application grouping. c. Click OK. d. In the Apply Template to Group message, click OK. |
|---|---|

| Export and download a report on alert templates | i. On the Alarm Template page, click Export report. ii. In the Create an alarm export task dialog box, enter a name in the Task name field. iii. Click OK. iv. In the left-side navigation pane, click Export Report. On the Report download page, click the Alarm Template tab. v. Find the report that you exported and click Download report in the Actions column. vi. In the Download report task message, click OK. Note The report is in the .xlsx format. You can find the downloaded report in the default download directory of your browser. |
|---|---|

### 5.4 Use the initiative alerting feature

**feature**

CloudMonitor provides the initiative alert feature that allows you to associate the default alert rules with the cloud service resources within all organizations and resource sets in the current level-1 organization. This way, you can enable the alert service with ease.

**Background information**

The initiative alert feature can be enabled or disabled for a specific cloud service. After you enable the initiative alert feature for a cloud service, all the predefined alert rules of the cloud service are enabled by default. CloudMonitor automatically creates an alert system for the specified metrics. After you enable the initiative alert feature for a cloud service, the alert rules of the cloud service are applied to both the existing resources and resources that are subsequently created in the current level-1 organization. After you enable the initiative alert feature for a cloud service, you can create, modify, delete, or disable alert rules for the cloud service based on your business requirements. If an alert rule is triggered after you enable the initiative alert feature for a cloud service, an alert is generated. By default, CloudMonitor sends alert notifications to the alert contacts specified for your Apsara Stack account. After you disable the initiative alert feature for a cloud service, all alert rules of the cloud service are disabled.

**Procedure**

1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Products** > **Migration and O&M Management** > **O&M**
**and Monitoring** > **CloudMonitor**.
3. In the left-side navigation pane, choose **Alert Service** > **Initiative Alerting**.
4. On the Initiative Alert page, perform the following operations.

| Operation | Procedure |
|---|---|
| Enable the initiative alert feature | i. Find the cloud service for which you want to enable the initiative alerting feature and turn on the switch in the A key alarm column. : indicates that the initiative alerting feature is disabled. : indicates that the initiative alerting feature is enabled. ii. In the message that appears, click Enable. Important After the initiative alert feature is enabled, the corresponding alert rules are enabled and added to the Alert Rules page. iii. Click the icon before the name of the cloud service to view the alert rules of the cloud service. |
| Disable the initiative alert feature | i. Find the cloud service for which you want to disable the initiative alerting feature and turn off the switch in the A key alarm column. ii. In the message that appears, click Close. Important After the initiative alert feature is disabled, the corresponding alert rules are removed from the Alert Rules page. |
| Create an alert rule | i. Click the icon before the name of the cloud service for which the initiative alerting feature is enabled. ii. Click Create Alert Rule. iii. In the Create an alert rule panel, configure the Rule name, Monitoring Metrics, and Threshold and alarm level parameters. iv. Click Confirm to return to the Create an alert rule. v. In the Create an alert rule panel, configure the following parameters: Silence channel period, Effective time, Alarm callback, No data processing method, and Alarm contact. vi. Click OK. |

| Enable or disable an alert rule | i. Click the icon before the name of the cloud service for which the initiative alerting feature is enabled. ii. Perform the following operations to enable or disable an alert rule: Find the alert rule that is in the Enable state and clickD isable in the Actions column. In the message that appears, click Disable. After you disable the alert rule, the corresponding alert rule on the Alert Rules page is also disabled. Find the alert rule that is in the Disable state and clickE nable in the Actions column. In the message that appears, click Enable. After you enable the alert rule, the corresponding alert rule on the Alert Rules page is also enabled. |
|---|---|
| Modify an alert rule | i. Click the icon before the name of the cloud service for which the initiative alerting feature is enabled. ii. Perform the following operations to modify a single alert rule or modify multiple alert rules at a time: Modify a single alert rule a. Find the alert rule that you want to modify and clickE dit in the Actions column. b. In the Modify alarm rules panel, modify parameters based on your business requirements. c. Click OK. Modify multiple alert rules at a time a. Select the alert rules that you want to modify. b. Click Batch Edit below the rule list. c. In the Batch Edit dialog box, configure the following parameters: Channel Silence Period, Effective time, Alarm callback, No data processing method, and Alarm Contact Group. d. Click Confirm. |
| Delete an alert rule | i. Click the icon before the name of the cloud service for which the initiative alerting feature is enabled. ii. Find the alert rule that you want to delete and clickD elete in the Actions column. Important After the alert rule is deleted, the corresponding alert rule on theA lert Rules page is also deleted. The deletion is irreversible. Proceed with caution. |

## 6 Statistical analysis

You can use CloudMonitor to analyze the monitoring data of all supported cloud services in a specified organization.

### 6.1 Sort monitoring data

You can use CloudMonitor to sort and analyze the monitoring data of supported cloud services in a specific organization.

**Limits**

CloudMonitor allows you to sort data of the top 1,000 instances of a cloud service in an organization. Data computing fails if the number of instances exceeds this limit.

**Procedure**

1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Products** > **Migration and O&M Management** > **O&M**
**and Monitoring** > **CloudMonitor**.
3. In the left-side navigation pane, choose **Statistical Analysis** **>** **Sorting**.
4. On the Monitoring Sort page, select a cloud service and configure the **Indicator Name**,
**Monitoring Sort**, **Indicator Aggregation Value**, and **Quantity** parameters.

> **Note:** **Monitoring Sort**: You can set this parameter to Ascending or Descending. If you set this parameter to Ascending, the monitoring data is sorted in ascending order. If you set this parameter to Descending, the monitoring data is sorted in descending order.
> **Indicator Aggregation Value**: You can set this parameter to sort the average, minimum, or maximum value of the specified metric of instances.
> **Quantity**: You can set this parameter to 10, 50, 100, or 200 to display the top 10, top 50, top 100, or top 200 monitoring data records.

5. Optional. Click **Report Export** to go to the **Product Data Analysis** page. On the **Product**
**Data Analysis** page, configure custom settings to export a report.

## 7 Event monitoring

The Event Monitoring module provides a unified portal for you to query and manage system events of CloudMonitor, Elastic Compute Service (ECS), Hybrid Disaster Recovery (HDR), Cloud Config, ASR for Backup and Recovery, Elastic Desktop Service (EDS), Open Network Services Platform (ONSP), and Resource Orchestration Service (ROS). You can view the status of the cloud services and receive alert notifications. This helps you troubleshoot business exceptions at the earliest opportunity.

### 7.1 System events

#### 7.1.1 System events of cloud services

This topic describes the cloud services that are supported by CloudMonitor and their system events. For more information about the event metrics, see Event metrics of cloud services.

**CloudMonitor**

| Service | System event |
|---|---|
| CloudMonitor | Agent Status Stopped _ _ Agent Status Running _ _ |

**HDR**

| Service | System event |
|---|---|

| Hybrid Cloud Disaster Recovery (HDR) | PrimarySiteVpc:Deleted SecondarySiteVpc:Deleted PrimarySiteNetwork:Deleted SecondarySiteNetwork:Deleted PrimarySecurityGroup:Deleted SecondarySecurityGroup:Deleted SecurityGroup:Inconsistency ProductSiteNetwork:Inconsistency DrSiteNetwork:Inconsistency ProductSiteStorage:Inconsistency DrSiteStorage:Inconsistency PrimarySiteComputation:Inconsistency DrSiteComputation:Inconsistency ReplicationGroup:Inconsistency ReplicationPair:Inconsistency Gateway:Inconsistency ShadowEcs:Inconsistency |
|---|---|

**ASR-BR**

| Service | System event |
|---|---|
| Apsara Stack Resilience for Backup and Recovery (ASR-BR) | BackupPlan RecoveryTask MigratePlan LICENSE |

**ROS**

| Service | System event |
|---|---|
| Resource Orchestration Service (ROS) | Stack:StatusChange StackResource:StatusChange StackGroup:OperationStatusChange |

**ECS**

| Service | System event |
|---|---|
|   | Disk:ConvertToPostpaidCompleted |

| User Guide·Event moni | toring CloudMonito |
|---|---|
| Elastic Compute Service (ECS) | Disk:DiskOperationCompleted Disk:ErrorDetected:Executed Disk:ErrorDetected:Executing Disk:OverduePaymentRelease Disk:Stalled:Executed Disk:Stalled:Executing Instance:AutoReactivateCompleted Instance:BurstablePerformanceRestricted Instance:InstanceFailure.PerformanceImpact:Executed Instance:InstanceFailure.PerformanceImpact:Executing Instance:InstanceFailure.Reboot:Executed Instance:InstanceFailure.Reboot:Executing Instance:LiveMigrationAcrossDDH Instance:PerformanceModeChange Instance:PreemptibleInstanceInterruption Instance:Security.TpmAlert:Executed Instance:Security.TpmAlert:Executing Instance:StateChange Instance:SystemFailure.Delete:Avoided Instance:SystemFailure.Delete:Executed Instance:SystemFailure.Delete:Executing Instance:SystemFailure.PerformanceImpact:Executed Instance:SystemFailure.PerformanceImpact:Executing Instance:SystemFailure.Reboot:Executed Instance:SystemFailure.Reboot:Executing Instance:SystemFailure.Reboot:Failed Instance:SystemFailure.Redeploy:Avoided Instance:SystemFailure.Redeploy:Canceled Instance:SystemFailure.Redeploy:Executed Instance:SystemFailure.Redeploy:Executing Instance:SystemFailure.Redeploy:Scheduled Instance:SystemFailure.Stop:Executed Instance:SystemFailure.Stop:Executing Instance:SystemMaintenance.IsolateErrorDisk:Avoided Instance:SystemMaintenance.IsolateErrorDisk:Canceled Instance:SystemMaintenance.IsolateErrorDisk:Executed Instance:SystemMaintenance.IsolateErrorDisk:Executing Instance:SystemMaintenance.IsolateErrorDisk:Failed Instance:SystemMaintenance.IsolateErrorDisk:Inquiring Instance:SystemMaintenance.PerformanceImpact:Executed Instance:SystemMaintenance.PerformanceImpact:Executing Instance:SystemMaintenance.ReInitErrorDisk:Avoided |

|   | Instance:SystemMaintenance.ReInitErrorDisk:Canceled Instance:SystemMaintenance.ReInitErrorDisk:Executed Instance:SystemMaintenance.ReInitErrorDisk:Executing Instance:SystemMaintenance.ReInitErrorDisk:Failed Instance:SystemMaintenance.ReInitErrorDisk:Inquiring Instance:SystemMaintenance.Reboot:Avoided Instance:SystemMaintenance.Reboot:Canceled Instance:SystemMaintenance.Reboot:Executed Instance:SystemMaintenance.Reboot:Executing Instance:SystemMaintenance.Reboot:Failed Instance:SystemMaintenance.Reboot:Inquiring Instance:SystemMaintenance.Reboot:Scheduled Instance:SystemMaintenance.RebootAndIsolateErrorDisk:Avoided Instance:SystemMaintenance.RebootAndIsolateErrorDisk:Canceled Instance:SystemMaintenance.RebootAndIsolateErrorDisk:Executed Instance:SystemMaintenance.RebootAndIsolateErrorDisk:Executing Instance:SystemMaintenance.RebootAndIsolateErrorDisk:Inquiring Instance:SystemMaintenance.RebootAndReInitErrorDisk:Avoided Instance:SystemMaintenance.RebootAndReInitErrorDisk:Canceled Instance:SystemMaintenance.RebootAndReInitErrorDisk:Executed Instance:SystemMaintenance.RebootAndReInitErrorDisk:Executing Instance:SystemMaintenance.RebootAndReInitErrorDisk:Inquiring Instance:SystemMaintenance.Redeploy:Avoided Instance:SystemMaintenance.Redeploy:Canceled Instance:SystemMaintenance.Redeploy:Executed Instance:SystemMaintenance.Redeploy:Executing Instance:SystemMaintenance.Redeploy:Inquiring Instance:SystemMaintenance.Redeploy:Scheduled Instance:SystemMaintenance.Stop:Avoided Instance:SystemMaintenance.Stop:Canceled Instance:SystemMaintenance.Stop:Executed Instance:SystemMaintenance.Stop:Executing Instance:SystemMaintenance.Stop:Failed Instance:SystemMaintenance.Stop:Scheduled NetworkInterface:NetworkInterfaceOperateCompleted |
|---|---|
|   | Snapshot:CreateSnapshotCompleted Instance:VmLivemigrateException Instance:VmDownCausedByNcDown Instance:VmDownEnd Instance:VmPanicEvent Instance:VmCrashEvent |

**ASR-DR**

| Cloud service | System event |
|---|---|
| Apsara Stack Resilience for Disaster Recovery (ASR-DR) | ProtectGroupStatus:Failed ProtectGroupLatency:Exceeded RecoveryPlanRTO:Exceeded RecoveryPlanStatus:Failed ProtectEntityLoad:Exceeded ProtectGroupCapacity:Insufficiency ProtectEntityCapacity:Insufficiency RecoveryPlanCapacity:Insufficiency |

**BMCP**

| Cloud service | System event |
|---|---|
| Bare Metal Computing Platform (BMCP) | GPU NVSMI HW POWERLOST _ _ _ GPU HWM LINK GPULOST _ _ _ GPU NVSMI LINK GPULOST _ _ _ GPU HWQC LINK GPULOST _ _ _ GPU KERN LINK FALLENOFF _ _ _ GPU DRIVER XID13ERR _ _ GPU HWM LINK PCIELINKERR _ _ _ GPU NVSMI HW NVLINKERR _ _ _ GPU NVSMI HW TOPONS _ _ _ GPU NVSMI HW MSGERR _ _ _ GPU DRIVER XID61ERR _ _ GPU DRIVER XID62ERR _ _ GPU DRIVER XID119ERR _ _ GPU DRIVER XID74ERR _ _ GPU DRIVER XID48ERR _ _ |

#### 7.1.2 View system events

CloudMonitor provides the event monitoring feature to help you query and analyze system events that are generated for various cloud services. The feature allows you to track the use of cloud services.

**Background information**

For more information about the cloud services and system events to which the event monitoring feature is applicable, see System events of cloud services.

**Procedure**

1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Products** > **Migration and O&M Management** > **O&M**
**and Monitoring** > **CloudMonitor**.
3. In the left-side navigation pane, choose **Event Monitoring** **>** **System Events**.
4. On the System Events page, click the **Event Monitoring** tab. On the **Event Monitoring**
tab, select a cloud service, an event level, an event name, and a time range, and then click
**Search**.
5. View the event monitoring chart.
The x-axis indicates the time, and the y-axis indicates the number of events. Move the pointer over a column in the chart to view the start time, end time, and number of events.
6. In the System events section, view the event information. Find the event that you want to
view and click **Details** in the Operation column. In the System events detail panel, you can view the event details in the **JSON** format.

#### 7.1.3 Create a system event-triggered alert rule

**rule**

You can create alert rules for system events of cloud services. If an exception occurs, an alert is generated and CloudMonitor sends notifications to alert contacts. This helps you analyze and troubleshoot issues.

**Procedure**

1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Products** > **Migration and O&M Management** > **O&M**
**and Monitoring** > **CloudMonitor**.
3. In the left-side navigation pane, choose **Event Monitoring** **>** **System Events**.
4. On the System Events page, click the **Event Alarm rules** tab, and then click **Create**
**Event Alerts Rules**.
5. In the **Create Event Alerts Rules** panel, configure the parameters described in the
following table.

| Category and parameter |   | Description |
|---|---|---|
| Basic information | Alarm rule name | The name of the system event-triggered alert rule. The name must be 1 to 30 characters in length and can contain letters, digits, and underscores ( ). _ |

| Event- triggered alert rule | Product | The cloud service to which the system event-triggered alert rule is applied. For more information about the cloud services that are supported by CloudMonitor, see System events of cloud services. |
|---|---|---|
|   | Event Level | The level of the event that triggers alerts. For more information about the event levels that are supported by each cloud service, see Event metrics of cloud services. |
|   | Event Name | The name of the event that triggers alerts. For more information about the events that are supported by each cloud service, see Event metrics of cloud services. |
| Alert notification | Alarm callback | The callback URL to which CloudMonitor sends alert notifications by using the POST request method. Note The callback URL must be accessible for CloudMonitor. You can enter only an HTTP URL. IP addresses are not supported. |
|   | Alarm contact | The contact group or contact that receives alert notifications. |

6. Click **OK**.

#### 7.1.4 Manage system event-triggered alert rules

**rules**

You can modify, disable, enable, and delete system event-triggered alert rules on the System Events page in CloudMonitor.

**Procedure**

1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Products** > **Migration and O&M Management** > **O&M**
**and Monitoring** > **CloudMonitor**.
3. In the left-side navigation pane, choose **Event Monitoring** > **System Events**.
4. On the System Events page, click the **Event Alarm rules** tab. On the Event Alarm rules
tab, find the system event-triggered alert rule that you want to manage and perform required operations. The following table describes supported operations.

| Operation | Procedure |
|---|---|

| Modify a system event-triggered alert rule | i. Find the system event-triggered alert rule that you want to modify, and click Edit in the Operation column. In the Modify event alerts Rule panel, modify the Product, Event Level, and Event Name parameters based on your business requirements. For more information about the parameters, see Create a system event-triggered alert rule. ii. Click OK. |
|---|---|
| Disable one or more system event- triggered alert rules | Note You can disable only event-triggered alert rules in the Enabled state. After you disable an alert rule, the rule no longer takes effect. Disable a single system event-triggered alert rule a. Find the system event-triggered alert rule that you want to disable and click Disable in the Operation column. b. In the message that appears, click OK. Disable multiple system event-triggered alert rules at a time a. Select the system event-triggered alert rules that you want to disable and click Disable in the lower-left corner of the alert rule list. b. In the message that appears, click OK. |
| Enable one or more system event- triggered alert rules | You can enable system event-triggered alert rules in the Disabled state. Enable a single system event-triggered alert rule a. Find the system event-triggered alert rule that you want to enable and click Enable in the Operation column. b. In the message that appears, click OK. Enable multiple system event-triggered alert rules at a time a. Select the system event-triggered alert rules that you want to enable and click Enable in the lower-left corner of the alert rule list. b. In the message that appears, click OK. |
| Delete one or more system event- triggered alert rules | Delete a single system event-triggered alert rule a. Find the system event-triggered alert rule that you want to delete and click Delete in the Operation column. b. In the message that appears, click OK. Delete multiple system event-triggered alert rules at a time a. Select the system event-triggered alert rules that you want to delete and click Delete in the lower-left corner of the alert rule list. b. In the message that appears, click OK. |

| View the records of system event- triggered alerts | After an event-triggered alert rule is created or enabled, CloudMonitor records the information about alerts that are generated based on the rule. i. Click the Event Alarm history tab. ii. Optional. Enter a rule ID or rule name and specify a time range to search for the alerts that are generated based on the rule. The information about an alert rule is displayed in the following columns: Product, Instance name, Alarm time, Event Level, and Event Name. |
|---|---|

### 7.2 Report custom events

CloudMonitor provides the event monitoring feature that allows you to report custom events. You can collect and report the exception events that occur in your business to CloudMonitor. You can also configure alert rules to receive alert notifications for custom events.

**Prerequisites**

The monitoring data of custom events is reported to CloudMonitor.

**Event monitoring**

**Report event monitoring data**

1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Products** > **Migration and O&M Management** > **O&M**
**and Monitoring** > **CloudMonitor**.
3. In the left-side navigation pane, choose **Event Monitoring** > **Custom Events** to go to the
**Custom Event Monitoring** page.
4. On the **Event Monitoring** tab, click **Data reporting**.
5. In the**SDK Data reporting**panel, view the data in the **Increase dependency POM**and
**Sample code**sections to complete data reporting.

**View custom events**

1. On the **Event Monitoring** tab of the **Custom Event Monitoring** page, enter an event
name and a keyword, and select an event level and a time range.
2. View the column chart that shows the distribution of reported custom events and the list of
custom events.

**Column chart of custom event distribution**

**Custom event list**

> **Note:** To create an alert rule for a custom event, find the custom event and click **Create an** **Event Alarm rule** in the **Operation** column. In the **Create an Event Alarm rule** panel, configure parameters to create an alert rule for the custom event. For more information, see the Create an event-triggered alert rule section of this topic.

**Event-triggered alert rules**

**Create an event-triggered alert rule**

1. On the **Custom Event Monitoring** page, click the **Event alarm rules** tab.
2. On the Event alarm rules tab, click **Create an Event Alarm rule**. In the **Create an Event**
**Alarm rule** panel, configure the parameters described in the following table to create an
event-triggered alert rule.

| Parameter | Description |
|---|---|
| Alarm rule name | The name of the event-triggered alert rule. |
| Event Name | The name of the custom event for which the alert rule is created. |
| Event alarm level | The alert level of the custom event. Valid values:I nformation, Warning, and Serious. |
| Rule Description | The details of the event-triggered alert rule. For example, you can specify that an alert is triggered if the custom event is generated three times or more within 5 minutes. |
| Contact Group | The contact or contact group that receives alert notifications. |

| Alarm callback | The callback URL to which CloudMonitor sends alert notifications by using the POST request method. Note The callback URL must be accessible for CloudMonitor. You can enter only an HTTP URL. IP addresses are not supported. |
|---|---|

3. Click **OK**.

**Modify an event-triggered alert rule**

1. On the **Event alarm rules** tab, find the alert rule that you want to modify and click
**Modification** in the **Operation** column.
2. In the **Modify Event Alarm rules** panel, configure parameters to modify the alert rule.

**Note**

The name of the custom event cannot be modified.
3. Click **OK**.

**Disable one or more event-triggered alert rules**

> **Note:** If you do not need to receive alert notifications about a custom event, you can disable the event-triggered alert rules that are created for the custom event.

**Disable a single event-triggered alert rule**

i. On the **Event alarm rules** tab, find the alert rule that you want to disable and click
**Disable** in the **Operation** column.
ii. In the **Disable alarm rules** message, click **OK**.

**Disable multiple event-triggered alert rules at a time**

i. On the **Event alarm rules** tab, select the alert rules that you want to disable and click Disable in the lower-left corner of the alert rule list. ii. In the **Disable alarm rules** message, click **OK**.

**Enable one or more event-triggered alert rules**

> **Note:** You can enable the custom event-triggered alert rules that are in the **Disabled** state.

**Enable a single event-triggered alert rule**

i. On the **Event alarm rules** tab, find the alert rule that you want to enable and click
**Enable** in the **Operation** column.
ii. In the **Enable alarm rules** message, click **OK**.

**Enable multiple event-triggered alert rules at a time**

i. On the **Event alarm rules** tab, select the alert rules that you want to enable and click Enable in the lower-left corner of the alert rule list. ii. In the **Enable alarm rules** message, click **OK**.

**Delete one or more event-triggered alert rules**

> **Note:** After you delete a custom event-triggered alert rule, CloudMonitor no longer sends the related alert notifications to you.

**Delete a single event-triggered alert rule**

i. On the **Event alarm rules** tab, find the alert rule that you want to delete and click
**Delete** in the **Operation** column.
ii. In the **Delete alarm rules** message, click **OK**.

**Delete multiple event-triggered alert rules at a time**

i. On the **Event alarm rules** tab, select the alert rules that you want to delete and click Delete in the lower-left corner of the alert rule list. ii. In the **Delete alarm rules** message, click **OK**.

**Event-triggered alert history**

**View the records of event-triggered alerts**

1. On the **Custom Event Monitoring** page, click the **Event Alarm History** tab.
2. On the Event Alarm History tab, enter a rule ID and rule name, and select a time range.
3. The event-triggered alerts that meet the specified conditions are displayed on the Event
Alarm History tab. You can view the alert information, including the rule name, rule ID, time when the alert was generated, event name, and event level.

## 8 Application group

Application groups allow you to manage Elastic Compute Service (ECS) instances by group based on your business requirements. You can use an application group to manage businessspecific ECS instances in a centralized manner. You can manage the alert rules and view monitoring data of different application groups. This greatly simplifies management complexity and improves efficiency.

### 8.1 Create an application group

The application group feature allows you to manage resources from different cloud services and regions by group. You can use application groups to manage business-specific alert rules and view business-specific monitoring data to improve O&M efficiency.
1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Products** > **Migration and O&M Management** > **O&M**
**and Monitoring** > **CloudMonitor**.
3. In the left-side navigation pane, click **Application Group**.
4. On the **Application grouping** page, click **Create an application Group**.
5. In the **Create an application Group** panel, configure the parameters described in the
following table.

| Parameter | Description |
|---|---|
| Create an instance method | Create manually: If you want to manage existing instances based on your business requirements, you can manually create a standard application group. Dynamic creation: If you select this option, an application group is dynamically created based on the specified resource set. This way, resource instances created in the resource set are automatically added to the application group, unless explicitly excluded. |
| Resource Set | The resource set in which you want to create an application group. The resource set must belong to the current organization. |
| Application Group Name | The name of the application group. |
| Cloud product selection | The cloud services whose resource instances you want to add to the application group. You can select multiple cloud services from the drop-down list. |
| Alert Contact | The alert contacts to receive alert notifications. You can select multiple alert contacts from the drop-down list. |

| Add Resource Item | Note This parameter is displayed only if the Create an instance method parameter is set to Create manually. The instances that you want to add to the application group in the specified resource set. The application group contains all instances that you select. |
|---|---|
| Exclude Resource Items | Note This parameter is displayed only if the Create an instance method parameter is set to Dynamic creation. The instances that you do not want to add to the application group in the specified resource set. The application group does not contain the instances that you select. |

6. Click **OK**.

### 8.2 Manage application groups

You can modify or delete application groups on the Application grouping page.

**Procedure**

1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Products** > **Migration and O&M Management** > **O&M**
**and Monitoring** > **CloudMonitor**.
3. In the left-side navigation pane, click **Application Group**. On the **Application grouping**
page, perform operations to manage application groups.

| Operation | Procedure |
|---|---|

| View the information about an application group | i. Optional. In the top navigation bar, select the organization for which you want to manage application groups. On the Application grouping page, enter an application group name or ID and click Search to search for the application group. ii. Click the name of the application group whose information you want to view. On the details page of the application group, click tabs in the left-side pane to view the corresponding information. Group Overview: displays the basic information about the application group and the associated cloud services. Group Resources: displays the details of the resources in the application group. Availability Monitoring: displays the availability monitoring data of all Elastic Compute Service (ECS) instances in the current application group. |
|---|---|
| Modify an application group | i. Optional. In the top navigation bar, select the organization for which you want to manage application groups. On the Application grouping page, enter the name or ID of the application group that you want to modify and click Search to search for the application group. ii. Click the icon in the application group card, and then click Modify Group. iii. In the Modify Application Grouping panel, modify the application group. iv. After the modification is complete, click OK. |
| Delete one or more resources from an application group | i. Find the application group that you want to manage and click its name. In the left-side pane, click the Group Resources tab. ii. In the list of ECS instances, delete one or more instances. Delete a single instance a. Find the instance that you want to delete, and clickD elete in the Operation column. b. In the message that appears, click OK. Delete multiple instances at a time a. Select the instances that you want to delete and clickD elete in the lower-left corner of the instance list. b. In the message that appears, click OK. |

| Delete an application group | Note If you delete an application group, all alert rules and event- triggered alerts of the application group are deleted. The instances in the application group are automatically migrated back to the pool that contains all instances. i. Optional. In the top navigation bar, select the organization for which you want to manage application groups. On the Application grouping page, enter the name or ID of the application group that you want to delete and click Search to search for the application group. ii. On the Application grouping page, delete one or more application groups. Delete a single application group a. Find the application group that you want to delete, click the icon in the application group card, and then click Delete Group. b. In the Delete Group message, click OK. Delete multiple application groups at a time a. Select the application groups that you want to delete and click Delete in the lower-left corner of the application group list. b. In the Delete Group message, click OK. |
|---|---|

### 8.3 Availability monitoring

#### 8.3.1 Create an availability monitoring task

CloudMonitor provides the availability monitoring feature to help you check whether a local service or cloud server responds as expected. You can specify the path and port for the local service or cloud server. If the local service or cloud server times out or returns an error code, CloudMonitor sends an alert notification. This way, you can troubleshoot the issue at the earliest opportunity.

**Procedure**

**Note**

The availability monitoring feature is applicable only to Elastic Compute Service (ECS).
1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Products** > **Migration and O&M Management** > **O&M**
**and Monitoring** > **CloudMonitor**.
3. In the left-side navigation pane, click **Application Group**.
4. On the **Application grouping** page, find the application group that you want to manage
and click its name.
5. On the details page of the application group, click **Availability Monitoring** in the left-side
pane.
6. Click **Add Availability Monitoring**. In the **Create/Modify Availability Monitor** wizard,
configure the parameters. The following table describes the parameters.

| Step and parameter |   | Description |
|---|---|---|
|   | Task Name | The name of the availability monitoring task. The name must be 4 to 50 characters in length, and can contain letters, digits, underscores ( ), and hyphens (-). _ |
|   | Probe Source | Displays all ECS instances in the application group. You can select one or more instances that you want to monitor. Note If you create over 500 tasks for an instance, some of the tasks may fail. |
|   | Detection target | The address type of the instances that you want to monitor. Default value: URL or IP. |
|   | Probe Type | The detection method. Valid values: HTTP(S), TELNET, and PING. HTTP(S): sends HTTP or HTTPS requests to detect the health status of the selected instances. You need to enter the URLs of the selected instances. Example: http://localhost:8081/check health.html. _ TELNET: runs the telnet command to detect the health status of the selected instances. You need to enter the endpoints of the instances. Example: 192.168.1.1:22. PING: runs the ping command to detect the health status of the selected instances. You need to enter the IP addresses of the instances. Example: 192.168.1.1. |
|   | Request Method | The HTTP request method. Valid values: HEAD, GET, and POST. Note This parameter is displayed only if the Detection target parameter is set to URL or IP and the Probe Type parameter is set to HTTP(S). |

| Create Task |   |   |
|---|---|---|
|   | Monitoring frequency | The interval at which detection requests are sent. Default value: 1Minutes. Note This parameter is displayed only if the Detection target parameter is set to URL or IP and the Probe Type parameter is set to HTTP(S). |
|   | Headers | The headers of the HTTP or HTTPS request. Format: parameter1:value1 . Separate multiple headers with commas (,). Note If the Detection target parameter is set to URL or IP and the Probe Type parameter is set to HTTP(S), you can click Advanced Configuration to configure this parameter. |
|   | Submitted Content | Note If the Detection target parameter is set to URL or IP, the Probe Type parameter is set to HTTP(S), and the Request Method parameter is set to POST, you can click Advanced Configuration to configure this parameter. The content is submitted in POST requests during site monitoring. Format: parameter1=value1&parameter2=value2. |

|   | Match Response Content | The response content that you want to match and the method to match the response content. If you specify response content, the monitoring task checks whether the first 64 KB of the HTTP response body contains the response content that you specify. Valid values: Alarm if it contains matching content Does not contain matching content will alarm Note If the Detection target parameter is set to URL or IP and the Probe Type parameter is set to HTTP(S), you can click Advanced Configuration to configure this parameter. |
|---|---|---|
| Alarm Settings | Status Code | The range of the status codes that you want to match. CloudMonitor generates an alert if the returned status code meets the alert condition. For more information about status codes, see Status codes. If the status code or response time reaches the specified threshold, an alert is triggered and a notification is sent to the specified alert group. |
|   | Response time | The periods of the response time that you want to match. CloudMonitor generates an alert if the response time meets the condition. Unit: milliseconds. If the status code or response time reaches the specified threshold, an alert is triggered and a notification is sent to the specified alert group. |
|   | Alarm Level | The alert level and the methods that are used to send alert notifications. Valid values: Critical (SMS + Mail + Webhook) Warning (SMS + Mail + Webhook) Info (Mail + Webhook) |
|   | Alarm callback | The URL that can be accessed over the Internet. CloudMonitor sends POST requests to push alert notifications to the specified URL. Note You can enter only an HTTP URL. |

|   | Channel Silence Period | The interval at which you want CloudMonitor to send alert notifications again if the alert is not cleared. Valid values: 5Minutes, 10Minutes, 15Minutes, 30Minutes, 60Minutes, 3Hours, 6Hours, 12Hours, and 24Hours. An alert is triggered if the conditions of an alert rule are met. CloudMonitor does not resend an alert notification when the alert is triggered within the mute period. If the alert is not cleared after the mute period ends, CloudMonitor resends alert notifications. Note You can click Advanced Configuration to configure this parameter for the alert rule. |
|---|---|---|
|   | Effective time | The period during which the alert rule is effective. CloudMonitor sends alert notifications within the effective period and only records alerts beyond the effective period. Note You can click Advanced Configuration to configure this parameter for the alert rule. |

#### 8.3.2 Manage availability monitoring tasks

You can modify, disable, enable, and delete availability monitoring tasks on the Availability Monitoring tab of an instance in CloudMonitor.

**Procedure**

1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Products** > **Migration and O&M Management** > **O&M**
**and Monitoring** > **CloudMonitor**.
3. In the left-side navigation pane, click **Application Group**.
4. On the **Application grouping** page, find the application group that you want to manage
and click its name.
5. On the details page of the application group, click **Availability Monitoring** in the left-side
pane. On the **Availability Monitoring** tab, perform operations to manage availability monitoring tasks.

| Operation | Procedure |
|---|---|

| View availability monitoring charts | i. Find the availability monitoring task that you want to manage and click the icon in the Operation column to view the monitoring details. ii. Select one or more monitored instances from the drop-down list. iii. Select a monitoring time range based on your business requirements. You can select 1 Hour, 6 Hours, 12 Hours, 1 Day, 3 Days, 7 Days, or 14 Days or specify a time range. iv. View the trend charts of the selected instances within the specified monitoring time range. |
|---|---|
| Modify an availability monitoring task | i. Find the availability monitoring task that you want to modify and click Modification in the Operation column. ii. In the Create/Modify Availability Monitor panel, modify the parameters as prompted. For more information about the parameters, see Create an availability monitoring task. iii. After the modification is complete, click OK. |
| Disable or enable one or more availability monitoring tasks | Note You can disable one or more availability monitoring tasks in the Enable state, or enable one or more availability monitoring tasks in the Disable state. Disable or enable a single availability monitoring task a. Click Disable or Enable in the Operation column of the task. b. In the Disable or Enable message, click OK. Disable or enable multiple availability monitoring tasks at a time a. Select the availability monitoring tasks that you want to disable or enable and click Batch Disable or Batch Enable in the lower-left corner of the task list. b. In the Disable or Enable message, click OK. |
| Delete one or more availability monitoring tasks | Delete a single availability monitoring task a. Find the availability monitoring task that you want to delete, move the pointer over the icon in the Operation column, and then click Delete. b. In the Delete message, click OK. Delete multiple availability monitoring tasks at a time a. Select the availability monitoring tasks that you want to delete and click Batch Delete in the lower-left corner of the task list. b. In the Delete message, click OK. |

#### 8.3.3 Status codes

If an error occurs when you use the availability monitoring feature of CloudMonitor to check the availability of a specified path or port, the corresponding status code is returned. The following table describes status codes.

| Protocol type | Status code | Description |
|---|---|---|
| HTTP | 610 | The status code returned because the connection times out. If CloudMonitor does not receive a response within 5 seconds after CloudMonitor sends an HTTP request, CloudMonitor determines that the connection times out. |
|   | 611 | The status code returned because the monitoring fails. |
| Telnet | 630 | The status code returned because the connection times out. If CloudMonitor does not receive a response within 5 seconds after CloudMonitor sends a Telnet request, CloudMonitor determines that the connection times out. |
|   | 631 | The status code returned because the monitoring fails. |

## 9 Download a report

You can export reports of the alert history, alert rules, and alert templates, and then download the reports to your local device.

**Background information**

Before you download the reports of the alert history, alert rules, and alert templates, make sure that the reports are exported. The downloaded reports are in the **.xlsx** format. You can find the downloaded reports in the default download directory of your browser. You can export and download the following types of reports: Alert history report: The report contains the product namespace, instance that triggers the alert, alert rule name, alert rule ID, point in time when the alert occurs, report export status, alert level, alert contact group, metric name, alert expression, and monitoring data of each alert. Alert rule report: The report contains the product namespace, rule name, rule ID, dimension (instance-specific or not), monitored instance, group (resource set), rule status (enabled or disabled), report export status, alert contact group, metric, and alert expression of each alert rule. Alert template report: The report contains the template name, template ID, description, resource set, modification time, and template type (system template or not) of each alert template.

**Procedure**

1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Products** > **Migration and O&M Management** > **O&M**
**and Monitoring** > **CloudMonitor**.
3. In the left-side navigation pane, click**Export Report**.
4. On the**Report Export**page, you can perform the following operations.

| Operation | Procedure |
|---|---|
| Download a report | i. Click the Alarm History, Alarm Rules, or Alarm Template tab. ii. Optional. Filter reports by report status. iii. Find the report that you want to download and clickD ownload Report Task in the Operation column. iv. In the Download report task message, click OK. |
| Delete a report task | i. Click the Alarm History, Alarm Rules, or Alarm Template tab. ii. Optional. Filter reports by report status. iii. Find the report task that you want to delete and clickD elete Report Task in the Operation column. iv. In the Delete report task message, click OK. |

## 10 Namespaces

### 10.1 Time series metrics

The Time series indicator tab on the Namespace page provides a centralized platform for you to query cloud service metrics. This allows you to query the information about each cloud service metric, such as the definition and calculation method.

**Background information**

The Time series indicator tab displays the metrics of all cloud services that are connected to CloudMonitor. The displayed information is consistent with the information about the cloud services and their metrics that are described in the Metrics topic. The Time series indicator tab displays the lineage information about each metric, including how the metric is created as a virtual SQL metric, the underlying source metric (actual SQL metric) on which the metric depends, and the data source, such as the project and Logstore in which data is stored. The lineage information displays the dependency relationships among metrics. This helps you track and troubleshoot data issues. The Time series indicator tab presents metrics in visual charts, which facilitates data analysis and visual representation.

**View time series metrics**

1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Products** > **Migration and O&M Management** > **O&M**
**and Monitoring** > **CloudMonitor**.
3. In the left-side navigation pane, click **Namespace**. By default, the **Time series indicator**
tab appears.
4. In the left-side**List of cloud products** section, click a cloud service. Then, the metric
information about the cloud service is displayed on the right side.
5. Find the metric that you want to view and click the
icon to the left of its name. In the chart that appears, you can view the lineage of the metric, which tracks the flow from the SQL statement that creates the metric through to the dependencies on source data stored in the specific Simple Log Service project and Logstore and also includes the dimension (DIM) table of CloudMonitor that is associated with the metric.

> **Note:** Not all cloud service metrics have DIM table data.

6. Click each node in the flow. On the **Inspection Item Details** tab of the **Availability**
**Monitoring Details** panel, check whether data exists. You can troubleshoot issues based
on the results of inspection items. An issue may occur due to the raw data, intermediate process, or aggregation calculation in the final stage. If an issue occurs, troubleshoot the issue based on the results of the related inspection items.

| Node | Inspection item |
|---|---|
| VIRTUAL SQL _ | Checks whether the virtual metric has data. Checks whether the fields of the virtual metric do not match those of the source metric. Checks whether the fields of the virtual metric are inconsistent with the query results of Tablestore. |
| SQL | Checks whether the source metric has data. Checks whether the fields of the metric are inconsistent with the query results of Tablestore. Indicates the normal latency of the metric. |
| DIM | Checks whether the sampled instances have DIM table data. |
| STREAM | Checks whether the project is running. Checks whether all Logstores within the stream are running. Checks whether all partitions within the project are running. Checks whether traffic exists in the partitions. Checks whether traffic exists in the stream. Checks whether the inbound and outbound data of the stream meets the conditions of the metric. |

| LOGSTORE | Checks whether the shards of the Logstore meet the business requirements. Checks whether the Logstore exists and whether data exists in the Logstore. Checks whether inbound traffic exists in the Logstore. Checks whether the Logstore runs in the source as expected. Checks whether the Logstore has a corresponding Logstore. |
|---|---|

7. On the **Monitoring Details** tab of the **Availability Monitoring Details** panel of the
VIRTUAL_SQL and SQL nodes, configure the Instance ID, Aggregate value, and Time selection parameters, and then click **Query**. The corresponding monitoring data is displayed in the Monitoring Chart section.

| Parameter | Description |
|---|---|
| Namespace | The namespace to which the metric belongs. The default value is used. |
| Indicator Name | The name of the metric. The default value is used. |
| Instance ID | The ID of the cloud service instance that you want to query. |
| Aggregate value | The aggregation method. Note The available aggregation methods vary based on cloud services. |
| Time selection | The time range of the monitoring data. You can select 1 hour, 4 hours, 12 hours, or a custom time range. |
| SLS data | This parameter is displayed only on the Monitoring Details tab of SQL nodes. This parameter specifies whether Simple Log Service data exists. |

| Monitoring chart | A monitoring chart is generated based on the specified instance ID, aggregate value, and time range. You can view the trend of metric data on the monitoring chart. |
|---|---|

**Configure the data retention period**

> **Important:** The data retention period configuration takes effect only for metric data.
> Before you configure the data retention period, you must make sure that your Tablestore instance has sufficient storage capacity. Proceed with caution.
> You cannot configure the data retention period for a specific organization, resource set, or metric dimension. After the data retention period is configured, it takes effect for all organizations, resource sets, and metric dimensions that are connected to CloudMonitor.

**Add the data retention period configuration of a metric**

1. On the **Time series indicator** tab, click the name of a cloud service, find the metric that
you want to manage, and then click **Data lifecycle configuration** in the **Actions** column.
2. In the **Data lifecycle configuration** dialog box, select **New** for the **Operation** parameter.
Set the **Data lifecycle configuration** parameter to the time period within which you want to retain data. Valid values: 0 to 1095. Unit: days. The default data retention period is 31 days. Data can be retained for up to three years, which indicates 1095 days.
3. Click **OK**.

**Modify the data retention period configuration of a metric**

You can modify the data retention period configuration of a metric only after a data retention period is configured for the metric.
1. On the **Time series indicator** tab, click the name of a cloud service, find the metric that
you want to manage, and then click **Data lifecycle configuration** in the **Actions** column.
2. In the **Data lifecycle configuration** dialog box, select **Edit** for the **Operation** parameter.
Set the **Data lifecycle configuration** parameter to the time period within which you want to retain data. Valid values: 0 to 1095. Unit: days. The default data retention period is 31 days. Data can be retained for up to three years, which indicates 1095 days.
3. Click **OK**.

**Delete the data retention period configuration of a metric**

You can delete the data retention period configuration of a metric only after a data retention period is configured for the metric. After the configuration is deleted, the default data retention period of 31 days is used.
1. On the **Time series indicator** tab, click the name of a cloud service, find the metric that
you want to manage, and then click **Data lifecycle configuration** in the **Actions** column.
2. In the **Data lifecycle configuration** dialog box, select **Delete** for the **Operation**
parameter.
3. Click **OK**.

### 10.2 System events

#### 10.2.1 Event monitoring metrics of cloud services

**services**

This topic describes the event monitoring metrics of cloud services. The information about a system event includes the event name, event description, event level, event status, and event type.

**Event monitoring metrics of CloudMonitor**

| Event name | Cloud service | Event description | Event level | Event status | Event type |
|---|---|---|---|---|---|
| Agent Status Stopped _ _ | CloudM onitor | The CloudMonitor agent stops sending heartbeat messages. | CRITICAL | stoppe d | StatusNotif ication |
| Agent Status Running _ _ | CloudM onitor | The CloudMonitor agent resumes the sending of heartbeat messages. | CRITICAL | runnin g | StatusNotif ication |

**Event monitoring metrics of HDR**

| Event name | Cloud service | Event description | Event level | Event status | Event type |
|---|---|---|---|---|---|
| PrimarySiteVpc:Delete d | Hybrid Disaster Recover y (HDR) | The virtual private cloud (VPC) in which the primary site is deployed is deleted. | CRITICAL | Failed | StatusNotif ication |
| SecondarySiteVpc:Del eted | HDR | The VPC in which the secondary site is deployed is deleted. | CRITICAL | Failed | StatusNotif ication |

| PrimarySiteNetwork:D eleted | HDR | The network connection of the primary site is lost. | CRITICAL | Failed | StatusNotif ication |
|---|---|---|---|---|---|
| SecondarySiteNetwor k:Deleted | HDR | The network connection of the secondary site is lost. | CRITICAL | Failed | StatusNotif ication |
| PrimarySecurityGroup :Deleted | HDR | The security group of the primary site is deleted. | CRITICAL | Failed | StatusNotif ication |
| SecondarySecurityGro up:Deleted | HDR | The security group of the secondary site is deleted. | CRITICAL | Failed | StatusNotif ication |
| SecurityGroup:Inconsi stency | HDR | The security group policies are inconsistent. | CRITICAL | Failed | StatusNotif ication |
| ProductSiteNetwork:In consistency | HDR | The network information about the primary site is abnormal. | CRITICAL | Failed | StatusNotif ication |
| DrSiteNetwork:Inconsi stency | HDR | The network information about the secondary site is abnormal. | CRITICAL | Failed | StatusNotif ication |
| ProductSiteStorage:In consistency | HDR | The storage information about the primary site is abnormal. | CRITICAL | Failed | StatusNotif ication |
| DrSiteStorage:Inconsi stency | HDR | The storage information about the secondary site is abnormal. | CRITICAL | Failed | StatusNotif ication |
| PrimarySiteComputati on:Inconsistency | HDR | The computing information about the primary site is abnormal. | CRITICAL | Failed | StatusNotif ication |
| DrSiteComputation:In consistency | HDR | The computing information about the secondary site is abnormal. | CRITICAL | Failed | StatusNotif ication |

| ReplicationGroup:Inco nsistency | HDR | The replication pair- consistent group information is abnormal. | CRITICAL | Failed | StatusNotif ication |
|---|---|---|---|---|---|
| ReplicationPair:Incons istency | HDR | The replication pair information is abnormal. | CRITICAL | Failed | StatusNotif ication |
| Gateway:Inconsistenc y | HDR | The gateway is abnormal. | CRITICAL | Failed | StatusNotif ication |
| ShadowEcs:Inconsiste ncy | HDR | The Elastic Compute Service (ECS) instance replication is abnormal. | CRITICAL | Failed | StatusNotif ication |

**Event monitoring metrics of ASR-BR**

| Event name | Cloud service | Event description | Event level | Event status | Event type |
|---|---|---|---|---|---|
| BackupPlan | Apsara Stack Resilien ce for Backup and Recover y (ASR- BR) | An alert related to backup schedules is triggered. | CRITICAL | FAILED | StatusNotif ication |
| RecoveryTask | ASR-BR | An alert related to recovery tasks is triggered. | CRITICAL | FAILED | StatusNotif ication |
| MigratePlan | ASR-BR | An alert related to migration tasks is triggered. | CRITICAL | FAILED | StatusNotif ication |
| LICENSE | ASR-BR | An alert related to authorized quotas is triggered. | CRITICAL | FAILED | Maintenan ce |

**Event monitoring metrics of ROS**

| 36 |   |   | > Doc | ument Vers | ion: 2025030 |
|---|---|---|---|---|---|

| Event name | Cloud service | Event description | Event level | Event status | Event type |
|---|---|---|---|---|---|
| Stack:StatusChange | Resourc e Orchestr ation Service (ROS) | The status of a stack is changed. | INFO | Normal | StatusNotif ication |
| StackResource:Status Change | ROS | The status of the resources in a stack is changed. | INFO | Normal | StatusNotif ication |
| StackGroup:Operation StatusChange | ROS | The operation status of a stack group is changed. | INFO | Normal | StatusNotif ication |

**Event monitoring metrics of ECS**

| Event name | Cloud service | Event description | Event level | Event status | Event type |
|---|---|---|---|---|---|
| Disk:ConvertToPostpai dCompleted | ECS | The billing method of the disk is changed to pay-as-you-go. | INFO | Normal | StatusNotif ication |
| Disk:DiskOperationCo mpleted | ECS | The disk operations are complete. | INFO | Normal | StatusNotif ication |
| Disk:ErrorDetected:Ex ecuted | ECS | The alert about the damage to a local disk ends | CRITICAL | Execut ed | Exception |
| Disk:ErrorDetected:Ex ecuting | ECS | The alert about the damage to a local disk starts. | CRITICAL | Executi ng | Exception |
| Disk:OverduePayment Release | ECS | A disk is released due to overdue payments. | CRITICAL | Normal | StatusNotif ication |
| Disk:Stalled:Executed | ECS | The impact on the disk performance ends. | CRITICAL | Execut ed | Exception |

| Disk:Stalled:Executing | ECS | The impact on the disk performance starts. | CRITICAL | Executi ng | Exception |
|---|---|---|---|---|---|
| Instance:AutoReactiva teCompleted | ECS | An ECS instance is automatically restarted. | INFO | Normal | StatusNotif ication |
| Instance:BurstablePer formanceRestricted | ECS | The performance of a burstable instance is restricted. | WARN | Normal | StatusNotif ication |
| Instance:InstanceFailu re.PerformanceImpact :Executed | ECS | The potential impact of an instance error on the instance performance ends. | WARN | Execut ed | Exception |
| Instance:InstanceFailu re.PerformanceImpact :Executing | ECS | The potential impact of an instance error on the instance performance starts. | WARN | Executi ng | Exception |
| Instance:InstanceFailu re.Reboot:Executed | ECS | The instance reboot that is caused by an instance error ends. | CRITICAL | Execut ed | Exception |
| Instance:InstanceFailu re.Reboot:Executing | ECS | The instance reboot that is caused by an instance error starts. | CRITICAL | Executi ng | Exception |
| Instance:LiveMigratio nAcrossDDH | ECS | An instance is hot migrated between dedicated hosts. | INFO | Normal | StatusNotif ication |
| Instance:Performance ModeChange | ECS | The performance mode of a burstable instance is changed. | INFO | Normal | StatusNotif ication |
| Instance:PreemptibleI nstanceInterruption | ECS | A preemptible instance is interrupted. | WARN | Normal | StatusNotif ication |
| Instance:Security.Tpm Alert:Executed | ECS | A Trusted Platform Module (TPM) security alert ends | WARN | Execut ed | Exception |
| Instance:Security.Tpm Alert:Executing | ECS | A TPM security alert starts. | WARN | Executi ng | Exception |

| Instance:StateChange | ECS | The status of an instance is changed. | INFO | Normal | StatusNotif ication |
|---|---|---|---|---|---|
| Instance:SystemFailur e.Delete:Avoided | ECS | The automatic instance release that is caused by an instance creation failure is avoided. | CRITICAL | Avoide d | Exception |
| Instance:SystemFailur e.Delete:Executed | ECS | The automatic instance release that is caused by an instance creation failure is complete. | CRITICAL | Execut ed | Exception |
| Instance:SystemFailur e.Delete:Executing | ECS | The automatic instance release that is caused by an instance creation failure is in progress. | CRITICAL | Executi ng | Exception |
| Instance:SystemFailur e.PerformanceImpact: Executed | ECS | The impact of a system error on the instance performance ends. | WARN | Execut ed | Exception |
| Instance:SystemFailur e.PerformanceImpact: Executing | ECS | The impact of a system error on the instance performance starts. | WARN | Executi ng | Exception |
| Instance:SystemFailur e.Reboot:Executed | ECS | The instance reboot that is caused by a system error ends. | CRITICAL | Execut ed | Exception |
| Instance:SystemFailur e.Reboot:Executing | ECS | The instance reboot that is caused by a system error starts. | CRITICAL | Executi ng | Exception |
| Instance:SystemFailur e.Reboot:Failed | ECS | The instance reboot that is caused by a system error fails. | CRITICAL | Failed | Exception |
| Instance:SystemFailur e.Redeploy:Avoided | ECS | The instance redeployment that is caused by a system error is avoided. | CRITICAL | Avoide d | Exception |
| Instance:SystemFailur e.Redeploy:Canceled | ECS | The instance redeployment that is caused by a system error is canceled. | CRITICAL | Cancel ed | Exception |

| Instance:SystemFailur e.Redeploy:Executed | ECS | The instance redeployment that is caused by a system error is complete. | CRITICAL | Execut ed | Exception |
|---|---|---|---|---|---|
| Instance:SystemFailur e.Redeploy:Executing | ECS | The instance redeployment that is caused by a system error is in progress. | CRITICAL | Executi ng | Exception |
| Instance:SystemFailur e.Redeploy:Scheduled | ECS | The instance redeployment that is caused by a system error is scheduled. | CRITICAL | Schedu led | Exception |
| Instance:SystemFailur e.Stop:Executed | ECS | The instance stop that is caused by a system error is complete. | CRITICAL | Execut ed | Exception |
| Instance:SystemFailur e.Stop:Executing | ECS | The instance stop that is caused by a system error starts. | CRITICAL | Executi ng | Exception |
| Instance:SystemMaint enance.IsolateErrorDi sk:Avoided | ECS | The damaged-disk isolation that is caused by system maintenance is avoided. | CRITICAL | Avoide d | Maintenan ce |
| Instance:SystemMaint enance.IsolateErrorDi sk:Canceled | ECS | The damaged-disk isolation that is caused by system maintenance is canceled. | CRITICAL | Cancel ed | Maintenan ce |
| Instance:SystemMaint enance.IsolateErrorDi sk:Executed | ECS | The damaged-disk isolation that is caused by system maintenance is complete. | CRITICAL | Execut ed | Maintenan ce |
| Instance:SystemMaint enance.IsolateErrorDi sk:Executing | ECS | The damaged-disk isolation that is caused by system maintenance is in progress. | CRITICAL | Executi ng | Maintenan ce |
| Instance:SystemMaint enance.IsolateErrorDi sk:Failed | ECS | The damaged-disk isolation that is caused by system maintenance fails. | CRITICAL | Failed | Maintenan ce |

| Instance:SystemMaint enance.IsolateErrorDi sk:Inquiring | ECS | The damaged-disk isolation that is caused by system maintenance is waiting for confirmation. | CRITICAL | Inquirin g | Maintenan ce |
|---|---|---|---|---|---|
| Instance:SystemMaint enance.PerformanceI mpact:Executed | ECS | The potential impact of system maintenance on the instance performance ends. | CRITICAL | Execut ed | Maintenan ce |
| Instance:SystemMaint enance.PerformanceI mpact:Executing | ECS | The potential impact of system maintenance on the instance performance starts. | CRITICAL | Executi ng | Maintenan ce |
| Instance:SystemMaint enance.ReInitErrorDis k:Avoided | ECS | The damaged-disk reinitialization that is caused by system maintenance is avoided. | CRITICAL | Avoide d | Maintenan ce |
| Instance:SystemMaint enance.ReInitErrorDis k:Canceled | ECS | The damaged-disk reinitialization that is caused by system maintenance is canceled. | CRITICAL | Cancel ed | Maintenan ce |
| Instance:SystemMaint enance.ReInitErrorDis k:Executed | ECS | The damaged-disk reinitialization that is caused by system maintenance is complete. | CRITICAL | Execut ed | Maintenan ce |
| Instance:SystemMaint enance.ReInitErrorDis k:Executing | ECS | The damaged-disk reinitialization that is caused by system maintenance is in progress. | CRITICAL | Executi ng | Maintenan ce |
| Instance:SystemMaint enance.ReInitErrorDis k:Failed | ECS | The damaged-disk reinitialization that is caused by system maintenance fails. | CRITICAL | Failed | Maintenan ce |
| Instance:SystemMaint enance.ReInitErrorDis k:Inquiring | ECS | The damaged-disk reinitialization that is caused by system maintenance is waiting for confirmation. | CRITICAL | Inquirin g | Maintenan ce |

| Instance:SystemMaint enance.Reboot:Avoide d | ECS | The scheduled instance reboot that is caused by system maintenance is avoided. | CRITICAL | Avoide d | Maintenan ce |
|---|---|---|---|---|---|
| Instance:SystemMaint enance.Reboot:Cancel ed | ECS | The scheduled instance reboot that is caused by system maintenance is canceled. | CRITICAL | Cancel ed | Maintenan ce |
| Instance:SystemMaint enance.Reboot:Execut ed | ECS | The scheduled instance reboot that is caused by system maintenance is complete. | CRITICAL | Execut ed | Maintenan ce |
| Instance:SystemMaint enance.Reboot:Execut ing | ECS | The scheduled instance reboot that is caused by system maintenance is in progress. | CRITICAL | Executi ng | Maintenan ce |
| Instance:SystemMaint enance.Reboot:Failed | ECS | The scheduled instance reboot that is caused by system maintenance fails. | CRITICAL | Failed | Maintenan ce |
| Instance:SystemMaint enance.Reboot:Inquiri ng | ECS | The scheduled instance reboot that is caused by system maintenance is waiting for confirmation. | CRITICAL | Inquirin g | Maintenan ce |
| Instance:SystemMaint enance.Reboot:Sched uled | ECS | The instance reboot that is caused by system maintenance is scheduled. | CRITICAL | Schedu led | Maintenan ce |
| Instance:SystemMaint enance.RebootAndIsol ateErrorDisk:Avoided | ECS | The instance reboot and damaged-disk isolation that are caused by system maintenance are avoided. | CRITICAL | Avoide d | Maintenan ce |
| Instance:SystemMaint enance.RebootAndIsol ateErrorDisk:Canceled | ECS | The instance reboot and damaged-disk isolation that are caused by system maintenance are canceled. | CRITICAL | Cancel ed | Maintenan ce |

| Instance:SystemMaint enance.RebootAndIsol ateErrorDisk:Executed | ECS | The instance reboot and damaged-disk isolation that are caused by system maintenance are complete. | CRITICAL | Execut ed | Maintenan ce |
|---|---|---|---|---|---|
| Instance:SystemMaint enance.RebootAndIsol ateErrorDisk:Executin g | ECS | The instance reboot and damaged-disk isolation that are caused by system maintenance are in progress. | CRITICAL | Executi ng | Maintenan ce |
| Instance:SystemMaint enance.RebootAndIsol ateErrorDisk:Inquiring | ECS | The instance reboot and damaged-disk isolation that are caused by system maintenance are waiting for confirmation. | CRITICAL | Inquirin g | Maintenan ce |
| Instance:SystemMaint enance.RebootAndReI nitErrorDisk:Avoided | ECS | The instance reboot and damaged-disk reinitialization that are caused by system maintenance are avoided. | CRITICAL | Avoide d | Maintenan ce |
| Instance:SystemMaint enance.RebootAndReI nitErrorDisk:Canceled | ECS | The instance reboot and damaged-disk reinitialization that are caused by system maintenance are canceled. | CRITICAL | Cancel ed | Maintenan ce |
| Instance:SystemMaint enance.RebootAndReI nitErrorDisk:Executed | ECS | The instance reboot and damaged-disk reinitialization that are caused by system maintenance are complete. | CRITICAL | Execut ed | Maintenan ce |
| Instance:SystemMaint enance.RebootAndReI nitErrorDisk:Executing | ECS | The instance reboot and damaged-disk reinitialization that are caused by system maintenance are in progress. | CRITICAL | Executi ng | Maintenan ce |

| Instance:SystemMaint enance.RebootAndReI nitErrorDisk:Inquiring | ECS | The instance reboot and damaged-disk reinitialization that are caused by system maintenance are waiting for confirmation. | CRITICAL | Inquirin g | Maintenan ce |
|---|---|---|---|---|---|
| Instance:SystemMaint enance.Redeploy:Avoi ded | ECS | The scheduled instance redeployment that is caused by system maintenance is avoided. | CRITICAL | Avoide d | Maintenan ce |
| Instance:SystemMaint enance.Redeploy:Can celed | ECS | The scheduled instance redeployment that is caused by system maintenance is canceled. | CRITICAL | Cancel ed | Maintenan ce |
| Instance:SystemMaint enance.Redeploy:Exe cuted | ECS | The scheduled instance redeployment that is caused by system maintenance is complete. | CRITICAL | Execut ed | Maintenan ce |
| Instance:SystemMaint enance.Redeploy:Exe cuting | ECS | The scheduled instance redeployment that is caused by system maintenance is in progress. | CRITICAL | Executi ng | Maintenan ce |
| Instance:SystemMaint enance.Redeploy:Inqu iring | ECS | The scheduled instance redeployment that is caused by system maintenance is waiting for confirmation. | CRITICAL | Inquirin g | Maintenan ce |
| Instance:SystemMaint enance.Redeploy:Sch eduled | ECS | The instance redeployment that is caused by system maintenance is scheduled. | CRITICAL | Schedu led | Maintenan ce |
| Instance:SystemMaint enance.Stop:Avoided | ECS | The scheduled instance stop that is caused by system maintenance is avoided. | CRITICAL | Avoide d | Maintenan ce |
| Instance:SystemMaint enance.Stop:Canceled | ECS | The scheduled instance stop that is caused by system maintenance is canceled. | CRITICAL | Cancel ed | Maintenan ce |

| Instance:SystemMaint enance.Stop:Executed | ECS | The scheduled instance stop that is caused by system maintenance is complete. | CRITICAL | Execut ed | Maintenan ce |
|---|---|---|---|---|---|
| Instance:SystemMaint enance.Stop:Executin g | ECS | The scheduled instance stop that is caused by system maintenance is in progress. | CRITICAL | Executi ng | Maintenan ce |
| Instance:SystemMaint enance.Stop:Failed | ECS | The scheduled instance stop that is caused by system maintenance fails. | CRITICAL | Failed | Maintenan ce |
| Instance:SystemMaint enance.Stop:Schedule d | ECS | The instance stop that is caused by system maintenance is scheduled. | CRITICAL | Schedu led | Maintenan ce |
| NetworkInterface:Net workInterfaceOperate Completed | ECS | The network interface controller (NIC) operations are complete. | INFO | Normal | StatusNotif ication |
| Snapshot:CreateSnap shotCompleted | ECS | A disk snapshot is created. | INFO | Normal | StatusNotif ication |
| Instance:VmLivemigra teException | ECS | The VM status is abnormal after hot migration. | WARN | Normal | StatusNotif ication |
| Instance:VmDownCau sedByNcDown | ECS | A VM breaks down due to a numerical control (NC) breakdown. | WARN | Normal | StatusNotif ication |
| Instance:VmDownEnd | ECS | A VM is recovered from a breakdown. | WARN | Execut ed | StatusNotif ication |
| Instance:VmPanicEve nt | ECS | A VM is restarted after a panic event caused by internal errors. | WARN | Normal | StatusNotif ication |
| Instance:VmCrashEve nt | ECS | A VM crashes due to exceptions. | WARN | Normal | StatusNotif ication |

**Event monitoring metrics of ASR-DR**

| Event name | Clou d servi ce | Event description | Event level | Event status | Event type |
|---|---|---|---|---|---|
| ProtectGroupStatus:Fa iled | Apsar a Stack Resili ence for Disast er Recov ery (ASR- DR) | The protection group is in the Failed state. | CRITICAL | Failed | Exception |
| ProtectGroupLatency: Exceeded | ASR- DR | The synchronization latency of the protection group is high. | CRITICAL | Exceeded | Exception |
| RecoveryPlanRTO:Exc eeded | ASR- DR | The recovery time objective (RTO) of the disaster recovery plan is high. | CRITICAL | Exceeded | Exception |
| RecoveryPlanStatus:F ailed | ASR- DR | The disaster recovery plan is in the Failed state. | CRITICAL | Failed | Exception |
| ProtectGroupCapacity: Insufficiency | ASR- DR | The capacity of the protection group is insufficient. | WARN | Insufficiency | Maintenance |
| ProtectEntityCapacity: Insufficiency | ASR- DR | The capacity of the synchronization entity is insufficient. | WARN | Insufficiency | Maintenance |
| RecoveryPlanCapacity :Insufficiency | ASR- DR | The capacity of the disaster recovery plan is insufficient. | WARN | Insufficiency | Maintenance |
| ProtectEntityLoad:Exc eeded | ASR- DR | The tasks that the synchronization entity processes is excessive. | CRITICAL | Exceeded | Maintenance |

**BMCP**

| Event name | Clou d servi ce | Event description | Event level | Event status | Event type |
|---|---|---|---|---|---|
| GPU NVSMI HW POW _ _ _ ERLOST | Bare Metal Comp uting Platfo rm (BMC P) | The external power cable is not detected. | CRITICAL | N/A | Exception |
| GPU HWM LINK GPUL _ _ _ OST | BMCP | The GPU Peripheral Component Interconnect Express (PCIe) device is lost. | CRITICAL | N/A | Exception |
| GPU NVSMI LINK GPU _ _ _ LOST | BMCP | The GPU driver is lost. | CRITICAL | N/A | Exception |
| GPU HWQC LINK GPU _ _ _ LOST | BMCP | The number of GPUs does not meet the model configuration. | CRITICAL | N/A | Exception |
| GPU NVSMI HW MSG _ _ _ ERR | BMCP | An error is returned when the nvidia- smi command is executed to check the GPU fan. | WARN | N/A | Exception |
| GPU KERN LINK FALL _ _ _ ENOFF | BMCP | The GPU driver is lost and the XID 79 error code is returned. | CRITICAL | N/A | Exception |
| GPU DRIVER XID13ER _ _ R | BMCP | The computing engine of the GPU is abnormal. | CRITICAL | N/A | Exception |
| GPU DRIVER XID61ER _ _ R | BMCP | A GPU microcontroller breakpoint alert is triggered. | WARN | N/A | Exception |

| GPU DRIVER XID62ER _ _ R | BMCP | The GPU controller halts. | WARN | N/A | Exception |
|---|---|---|---|---|---|
| GPU DRIVER XID119E _ _ RR | BMCP | A Remote Procedure Call (RPC) timeout occurs when the host communicates with the GSP core of the GPU. | WARN | N/A | Exception |
| GPU HWM LINK PCIEL _ _ _ INKERR | BMCP | The bandwidth of the GPU PCIe link decreases. | CRITICAL | N/A | Exception |
| GPU DRIVER XID74ER _ _ R | BMCP | The GPU NVLink is abnormal. | WARN | N/A | Exception |
| GPU NVSMI HW NVLI _ _ _ NKERR | BMCP | The GPU NVLink connection fails. | CRITICAL | N/A | Exception |
| GPU NVSMI HW TOPO _ _ _ NS | BMCP | The GPU NVLink is disconnected. | CRITICAL | N/A | Exception |
| GPU DRIVER XID48ER _ _ R | BMCP | A multi-bit error occurs in GPU memory. | INFO | N/A | Exception |

#### 10.2.2 View system event metrics

The System Events tab on the Namespace page provides a centralized platform for you to query the system event metrics of cloud services. This allows you to query the information about each system event metric, including the level, status, and type of the metric.

**Background information**

The system event metrics on the System Event tab are the same as those that are described in the System events of cloud services topic.

**Procedure**

1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Products** > **Migration and O&M Management** > **O&M**
**and Monitoring** > **CloudMonitor**.
3. In the left-side navigation pane, click **Namespace**.
4. On the Namespace page, click the **System Events** tab.
5. In the left-side **List of cloud products** section, click a cloud service. Then, the system
event metrics of the cloud service are displayed in the right-side section. availability

## 11 Monitor service availability

**availability**

CloudMonitor provides the availability monitoring feature to help you check whether a local service or cloud server responds as expected. You can specify the path and port for the local service or cloud server. If the local service or cloud server times out or returns an error code, CloudMonitor sends an alert notification. This way, you can troubleshoot the issue at the earliest opportunity. The availability monitoring feature is applicable only to Elastic Compute Service (ECS).

**Create an availability monitoring task**

1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Products** > **Migration and O&M Management** > **O&M**
**and Monitoring** > **CloudMonitor**.
3. In the left-side navigation pane, click**Service Availability Monitoring**.
4. On the Service Availability Monitoring page, click**Add Availability Monitoring**. In the
**Create Availability Monitoring**panel, configure the parameters. The following tables
describe the parameters. i. Create Task step

| Parameter | Description |
|---|---|
| Task Name | The name of the availability monitoring task. The name must be 4 to 50 characters in length, and can contain letters, digits, underscores ( ), and hyphens _ (-). |
| Probe Source | The instances that you want to monitor. You can select one or more instances. |
| Detection target | The address type of the instances that you want to monitor. Default value:U RL or IP. |
| Probe Type | The detection method. Valid values: HTTP(S), TELNET, and PING. HTTP(S): sends HTTP or HTTPS requests to detect the health status of the selected instances. You need to enter the URLs of the instances. Example: http://localhost:8081/check health.html. _ TELNET: runs the TELNET command to detect the health status of the selected instances. You need to enter the endpoints of the instances. Example: 192.168.1.1:22. PING: runs the PING command to detect the health status of the selected instances. You need to enter the IP addresses of the instances. Example: 192.168.1.1. |

availability

| Request Method | The HTTP request method. Valid values: HEAD, GET and POST. Note This parameter is displayed only if the Detection target is set to URL or IP and the Probe Type parameter is set to HTTP(S). |
|---|---|
| Advanced Configurati on | Note If the Detection target is set to URL or IP and the Probe Type parameter is set to HTTP(S), you can click Advanced Configuration to configure the following parameters. Request Parameters Headers: the headers of the HTTP or HTTPS request. Format: key1:value1. Enter each header in a separate line. Submitted Content: the content to be submitted in POST requests during site monitoring. This parameter is displayed only if you set the Request Method parameter to POST. Format: parameter1=value1&parameter2=value2. Match Response Content: the response content that you want to match and the method to match the response content. If you specify response content, the monitoring task checks whether the first 64 KB of the HTTP response body contains the response content that you specify. Valid values: Alarm if it contains matching content Does not contain matching content will alarm User Authentication HTTP authentication User name: the username for HTTP authentication. HTTP authentication password: the password for HTTP authentication. Monitoring frequency: the interval at which detection requests are sent. Valid values: 15Seconds, 30Seconds, 1Minutes, 2Minutes, 5Minutes, 15Minutes, 30Minutes, and 60Minutes. |

ii. Alarm Settings step

| Parameter | Description |
|---|---|

availability

| Alarm Rules | If you set the Probe Type parameter to HTTP(S) or TELNET, the Status Code and Response time parameters are displayed and required. If you set the Probe Type parameter to PING, the Packet loss and Response time parameters are displayed and required. Note Status Code: the range of the status codes that you want to match. CloudMonitor generates an alert if the returned status code meets the alert condition. For more information, see Status codes. Packet loss: the range of the packet loss rates that you want to match. CloudMonitor generates an alert if the packet loss rate meets the alert condition. Response time: the periods of the response time that you want to match. CloudMonitor generates an alert if the response time meets the alert condition. Unit: milliseconds. If the status code, packet loss rate, or response time reaches the specified threshold, an alert is triggered and a notification is sent to the specified alert group. |
|---|---|
| Alarm Level | The alert level and the methods that are used to send alert notifications. Valid values: Critical (SMS + Mail + Webhook) Warning (SMS + Mail + Webhook) Info (Mail + Webhook) |
| Alarm callback | The URL that can be accessed over the Internet. CloudMonitor sends POST requests to push alert notifications to the specified URL. Note You can enter only an HTTP URL. |
| Configure Alarm Contact Group | The alert groups that receive alert notifications. Select alert groups in the Contact group to be selected section and add them to the Selected section. |

availability

| Advanced Configuration | Note Click Advanced Configuration to configure the following parameters. Channel Silence Period: the interval at which you want CloudMonitor to send alert notifications again if the alert is not cleared. Valid values: 5Minutes, 10Minutes, 15Minutes, 30Minutes, 60Minutes, 3Hours, 6Hours, 12Hours, and 24Hours. An alert is triggered if the conditions of an alert rule are met. CloudMonitor does not resend an alert notification when the alert is triggered within the mute period. If the alert is not cleared after the mute period ends, CloudMonitor resends alert notifications. Effective time: the period during which the alert rule is effective. CloudMonitor sends alert notifications within the effective period and only records alerts beyond the effective period. |
|---|---|

iii. Create Results step After the availability monitoring task is created, you can view the task in the task list.

**View an availability monitoring task**

1. In the task list of the **Service Availability Monitoring** page, view the information about
availability monitoring tasks displayed in the following columns: **Task Name/Task ID**,
**Monitoring Status**, **Detection target**, **Probe Type**, **Number of abnormal machines**
**probed**, **Number of abnormal plug-in machines**, **Total number of machines** ,
**Availability**, and **Average Latency**.

> **Note:** You can click the
> icon above the list to set the automatic refresh interval or
> perform manual refresh. The automatic refresh interval can be set to 1, 3, or 5 minutes.
> You can click the
> icon above the list to select the columns to be displayed. If
> you clear a column, the column is not displayed.

2. Find the availability monitoring task that you want to manage and click the
icon in the
**Operation** column to view the monitoring details.
3. In the upper part of the task details page, view the basic information about the monitoring
task.
4. Select one or more monitored instances from the drop-down list.
availability
5. Select a monitoring time range based on your business requirements. You can select **1**
**Hour**, **6 Hours**, **12 Hours**, **1 Day**, **3 Days**, **7 Days**, or **14 Days** or specify a custom time
range.
6. View the trend charts of the selected instances within the specified monitoring time range.

**Modify an availability monitoring task**

If the information about an existing availability monitoring task changes, you can modify the availability monitoring task based on your business requirements.
1. On the **Service Availability Monitoring** page, find the availability monitoring task that
you want to manage and click **Modification** in the Operation column.
2. In the **Modifying Availability Monitoring** panel, modify the parameters based on your
business requirements. For more information about the parameters, see the Create an availability monitoring task section of this topic.

> **Important:** The Detection target and Probe Type parameters cannot be modified.

**Disable one or more availability monitoring tasks**

You can disable an availability monitoring task if you do not need to monitor the corresponding resources.

> **Important:** You can disable only availability monitoring tasks in the **Enable** state.

Disable a single availability monitoring task i. On the**Service Availability Monitoring**page, find the availability monitoring task that you want to disable and click **Disable** in the Operation column. ii. In the message that appears, click **OK**. Disable multiple availability monitoring tasks at a time On the**Service Availability Monitoring**page, select the availability monitoring tasks that you want to disable. Click **Batch Disable** in the lower-left corner of the task list. In the message that appears, click **OK**.

**Enable one or more availability monitoring tasks**

availability You can enable a disabled availability monitoring task if you want to monitor the corresponding resources again.

> **Important:** You can enable only availability monitoring tasks in the **Disable** state.

Enable a single availability monitoring task i. On the**Service Availability Monitoring**page, find the service availability monitoring task that you want to enable and click **Enable** in the Operation column. ii. In the message that appears, click **OK**. Enable multiple availability monitoring tasks at a time i. On the**Service Availability Monitoring**page, select the availability monitoring tasks that you want to enable. ii. Click **Batch Enable** in the lower-left corner of the task list. iii. In the message that appears, click **OK**.

**Delete one or more availability monitoring tasks**

You can delete an availability monitoring task if you no longer need it. Delete a single availability monitoring task i. On the**Service Availability Monitoring**page, find the availability monitoring task that you want to delete and click**Delete** in the Operation column. ii. In the message that appears, click **OK**. Delete multiple availability monitoring tasks at a time On the**Service Availability Monitoring**page, select the availability monitoring tasks that you want to delete. Click **Batch Delete** in the lower-left corner of the task list. In the message that appears, click **OK**.
